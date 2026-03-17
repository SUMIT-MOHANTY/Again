/**
 * Backend monitoring middleware using Datadog
 * Provides Express middleware and utilities for monitoring backend performance
 */

import express from 'express';
import { tracer, dogstatsd } from 'dd-trace';
import os from 'os';
import v8 from 'v8';

// Initialize Datadog tracer with configuration from environment
tracer.init({
  service: process.env.DD_SERVICE || 'calculator-backend',
  env: process.env.NODE_ENV || 'development',
  version: process.env.APP_VERSION || '1.0.0',
  logInjection: true,
  analytics: true,
  runtimeMetrics: true
});

// Metric name prefix for consistency
const METRIC_PREFIX = 'calculator.backend.';

/**
 * Express middleware for tracking API response time and request count
 * @returns Express middleware function
 */
export const responseTimeMiddleware = (): express.RequestHandler => {
  return (req: express.Request, res: express.Response, next: express.NextFunction) => {
    const startTime = process.hrtime();

    // Track request count
    const tags = [
      `endpoint:${req.path}`,
      `method:${req.method}`,
    ];

    dogstatsd.increment(`${METRIC_PREFIX}requests.count`, 1, tags);

    // Function to finalize the request tracking
    const finishTracking = () => {
      const diff = process.hrtime(startTime);
      const responseTimeMs = (diff[0] * 1e3) + (diff[1] * 1e-6);

      // Add status code tag
      tags.push(`status:${res.statusCode}`);

      // Track response time
      dogstatsd.histogram(
        `${METRIC_PREFIX}api.response_time`,
        responseTimeMs,
        tags
      );

      // Track errors
      if (res.statusCode >= 400) {
        const errorTags = [
          ...tags,
          `error_type:${res.statusCode >= 500 ? 'server' : 'client'}`
        ];
        dogstatsd.increment(`${METRIC_PREFIX}errors.count`, 1, errorTags);
      }

      // Remove response listeners
      res.removeListener('finish', finishTracking);
      res.removeListener('close', finishTracking);
    };

    // Listen for response finish or close events
    res.on('finish', finishTracking);
    res.on('close', finishTracking);

    next();
  };
};

/**
 * Middleware for tracking calculator operations
 * @returns Express middleware function
 */
export const calculatorMetricsMiddleware = (): express.RequestHandler => {
  return (req: express.Request, res: express.Response, next: express.NextFunction) => {
    // Only track POST requests to calculator endpoints
    if (req.method !== 'POST') {
      return next();
    }

    // Extract operation type from path
    const path = req.path;
    let operationType = 'unknown';

    if (path === '/api/calculate') {
      operationType = req.body.operation || 'calculate';
    } else if (path === '/api/add') {
      operationType = 'add';
    } else if (path === '/api/subtract') {
      operationType = 'subtract';
    } else if (path === '/api/multiply') {
      operationType = 'multiply';
    } else if (path === '/api/divide') {
      operationType = 'divide';
    }

    // Only track if it's a calculator operation
    if (operationType !== 'unknown') {
      const tags = [`operation_type:${operationType}`];
      dogstatsd.increment(`${METRIC_PREFIX}calculations.count`, 1, tags);

      // Intercept the response to track errors
      const originalSend = res.send;
      res.send = function(body) {
        try {
          // Check for calculation errors
          if (res.statusCode >= 400 || (body && body.error)) {
            const errorReason = body && body.error ? body.error : 'unknown';
            const errorTags = [...tags, `error_reason:${errorReason}`];
            dogstatsd.increment(`${METRIC_PREFIX}calculations.errors`, 1, errorTags);
          }
        } catch (error) {
          console.error('Error tracking calculation metrics:', error);
        }

        return originalSend.apply(res, arguments as any);
      };
    }

    next();
  };
};

/**
 * Setup periodic system metrics collection
 * @param intervalMs - Interval in milliseconds to collect metrics
 */
export const setupSystemMetrics = (intervalMs: number = 60000): NodeJS.Timeout => {
  return setInterval(() => {
    try {
      // CPU usage metrics
      const cpuUsage = os.loadavg()[0] / os.cpus().length;
      dogstatsd.gauge(`${METRIC_PREFIX}system.cpu.usage`, cpuUsage);

      // Memory usage metrics
      const usedMemory = process.memoryUsage().rss;
      const totalMemory = os.totalmem();
      const memoryUsage = usedMemory / totalMemory;
      dogstatsd.gauge(`${METRIC_PREFIX}system.memory.usage`, memoryUsage);

      // Heap metrics
      const heapStats = v8.getHeapStatistics();
      dogstatsd.gauge(
        `${METRIC_PREFIX}system.heap.used`,
        heapStats.used_heap_size / heapStats.total_heap_size
      );

      // Event loop lag metrics
      const start = Date.now();
      setImmediate(() => {
        const lag = Date.now() - start;
        dogstatsd.gauge(`${METRIC_PREFIX}system.event_loop.lag`, lag);
      });
    } catch (error) {
      console.error('Error collecting system metrics:', error);
    }
  }, intervalMs);
};

/**
 * Error tracking middleware
 * @returns Express error handling middleware
 */
export const errorTrackingMiddleware = (): express.ErrorRequestHandler => {
  return (err: Error, req: express.Request, res: express.Response, next: express.NextFunction) => {
    try {
      // Track error in Datadog
      const tags = [
        `endpoint:${req.path}`,
        `method:${req.method}`,
        `error_type:${err.name || 'UnknownError'}`
      ];

      dogstatsd.increment(`${METRIC_PREFIX}errors.count`, 1, tags);

      // Add span for error tracking if tracing is active
      const span = tracer.scope().active();
      if (span) {
        span.setTag('error', true);
        span.setTag('error.type', err.name);
        span.setTag('error.message', err.message);
        span.setTag('error.stack', err.stack);
      }
    } catch (monitoringError) {
      console.error('Error in error tracking middleware:', monitoringError);
    }

    // Continue to the next error handler
    next(err);
  };
};

/**
 * Initialize all monitoring middleware and systems
 * @param app - Express application
 */
export const initializeMonitoring = (app: express.Application): void => {
  // Apply middleware
  app.use(responseTimeMiddleware());
  app.use(calculatorMetricsMiddleware());
  app.use(errorTrackingMiddleware());

  // Start system metrics collection
  const systemMetricsInterval = setupSystemMetrics();

  // Clean up on process termination
  process.on('SIGTERM', () => {
    clearInterval(systemMetricsInterval);
    console.log('Shutting down monitoring');
  });

  console.log('Backend monitoring initialized successfully');
};

// Export default object for easy importing
export default {
  initializeMonitoring,
  responseTimeMiddleware,
  calculatorMetricsMiddleware,
  errorTrackingMiddleware,
  setupSystemMetrics,
  tracer
};
