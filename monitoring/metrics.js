/**
 * Key metrics definitions for the calculator application
 * This file defines all metrics collected across frontend and backend
 */

const { appName } = require('./config').datadog;

// Create consistent metric naming using the pattern:
// calculator.{environment}.{component}.{metric}
const createMetricName = (component, metricName) => {
  return `${appName}.${component}.${metricName}`;
};

const metrics = {
  // Backend metrics
  backend: {
    // API response time metrics
    apiResponseTime: {
      name: createMetricName('backend', 'api.response_time'),
      description: 'API endpoint response time in milliseconds',
      type: 'histogram',
      unit: 'millisecond',
      tags: ['endpoint', 'status_code', 'http_method']
    },

    // Error rate metrics
    errorRate: {
      name: createMetricName('backend', 'errors.rate'),
      description: 'Rate of errors occurring in backend services',
      type: 'rate',
      unit: 'error',
      tags: ['endpoint', 'error_type', 'error_source']
    },

    // Request volume metrics
    requestVolume: {
      name: createMetricName('backend', 'requests.count'),
      description: 'Number of API requests received',
      type: 'count',
      unit: 'request',
      tags: ['endpoint', 'http_method']
    },

    // Resource utilization metrics
    cpuUsage: {
      name: createMetricName('backend', 'system.cpu.usage'),
      description: 'CPU usage percentage of the backend service',
      type: 'gauge',
      unit: 'percent',
      tags: ['service']
    },
    memoryUsage: {
      name: createMetricName('backend', 'system.memory.usage'),
      description: 'Memory usage of the backend service',
      type: 'gauge',
      unit: 'byte',
      tags: ['service']
    },

    // Calculator specific metrics
    calculationCount: {
      name: createMetricName('backend', 'calculations.count'),
      description: 'Number of calculations performed',
      type: 'count',
      unit: 'calculation',
      tags: ['operation_type']
    },
    calculationErrors: {
      name: createMetricName('backend', 'calculations.errors'),
      description: 'Number of calculation errors (e.g. division by zero)',
      type: 'count',
      unit: 'error',
      tags: ['operation_type', 'error_reason']
    }
  },

  // Frontend metrics
  frontend: {
    // Page performance metrics
    pageLoadTime: {
      name: createMetricName('frontend', 'page.load_time'),
      description: 'Total time to load the page',
      type: 'histogram',
      unit: 'millisecond',
      tags: ['page', 'browser', 'device_type']
    },
    timeToInteractive: {
      name: createMetricName('frontend', 'page.time_to_interactive'),
      description: 'Time until page is fully interactive',
      type: 'histogram',
      unit: 'millisecond',
      tags: ['page', 'browser', 'device_type']
    },

    // User interaction metrics
    interactionTime: {
      name: createMetricName('frontend', 'interaction.response_time'),
      description: 'Time between user action and response',
      type: 'histogram',
      unit: 'millisecond',
      tags: ['action_type', 'component']
    },

    // JS error metrics
    jsErrors: {
      name: createMetricName('frontend', 'errors.js'),
      description: 'JavaScript errors occurring in the frontend',
      type: 'count',
      unit: 'error',
      tags: ['error_type', 'component', 'browser']
    },

    // API call performance from frontend
    apiCallDuration: {
      name: createMetricName('frontend', 'api.call_duration'),
      description: 'Time taken for API calls from frontend',
      type: 'histogram',
      unit: 'millisecond',
      tags: ['endpoint', 'status_code']
    },

    // Calculator UI metrics
    calculatorInputTime: {
      name: createMetricName('frontend', 'calculator.input_time'),
      description: 'Time user spends inputting calculation values',
      type: 'histogram',
      unit: 'millisecond',
      tags: ['operation_type']
    }
  }
};

// Thresholds for alerts
const thresholds = {
  [metrics.backend.apiResponseTime.name]: 500, // ms
  [metrics.backend.errorRate.name]: 0.05, // 5% error rate
  [metrics.frontend.pageLoadTime.name]: 2000, // ms
  [metrics.frontend.timeToInteractive.name]: 3000, // ms
  [metrics.frontend.interactionTime.name]: 100, // ms
  [metrics.frontend.apiCallDuration.name]: 1000, // ms
};

module.exports = {
  metrics,
  thresholds
};
