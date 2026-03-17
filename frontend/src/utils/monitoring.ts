/**
 * Frontend monitoring integration using Datadog
 * Provides utilities for tracking frontend metrics and performance
 */

import { datadogRum } from '@datadog/browser-rum';
import { datadogLogs } from '@datadog/browser-logs';

// Configuration interfaces
interface MonitoringConfig {
  applicationId: string;
  clientToken: string;
  site: string;
  service: string;
  env: string;
  version: string;
  sampleRate: number;
  trackInteractions: boolean;
  defaultPrivacyLevel?: 'mask' | 'mask-user-input' | 'allow';
}

// Default configuration
const defaultConfig: MonitoringConfig = {
  applicationId: process.env.DD_APPLICATION_ID || '',
  clientToken: process.env.DD_CLIENT_TOKEN || '',
  site: 'datadoghq.com',
  service: 'calculator-frontend',
  env: process.env.NODE_ENV || 'development',
  version: process.env.VITE_APP_VERSION || '1.0.0',
  sampleRate: 100,
  trackInteractions: true,
  defaultPrivacyLevel: 'mask-user-input'
};

/**
 * Initialize Datadog RUM and Logs monitoring
 * @param config - Optional configuration to override defaults
 * @returns boolean indicating if initialization was successful
 */
export const initializeMonitoring = (config: Partial<MonitoringConfig> = {}): boolean => {
  try {
    const finalConfig = { ...defaultConfig, ...config };

    // Verify required configuration is present
    if (!finalConfig.applicationId || !finalConfig.clientToken) {
      console.warn('Monitoring initialization failed: Missing required configuration');
      return false;
    }

    // Initialize Real User Monitoring
    datadogRum.init({
      applicationId: finalConfig.applicationId,
      clientToken: finalConfig.clientToken,
      site: finalConfig.site,
      service: finalConfig.service,
      env: finalConfig.env,
      version: finalConfig.version,
      sampleRate: finalConfig.sampleRate,
      trackInteractions: finalConfig.trackInteractions,
      defaultPrivacyLevel: finalConfig.defaultPrivacyLevel,
      trackResources: true,
      trackLongTasks: true,
      trackUserInteractions: true
    });

    // Initialize Logs
    datadogLogs.init({
      clientToken: finalConfig.clientToken,
      site: finalConfig.site,
      service: finalConfig.service,
      env: finalConfig.env,
      forwardErrorsToLogs: true,
      sampleRate: finalConfig.sampleRate
    });

    console.log('Frontend monitoring initialized successfully');
    return true;
  } catch (error) {
    console.error('Error initializing frontend monitoring:', error);
    return false;
  }
};

/**
 * Track a custom user action timing
 * @param actionName - Name of the action being performed
 * @param durationMs - Duration in milliseconds
 * @param tags - Additional tags for the action
 */
export const trackUserAction = (
  actionName: string,
  durationMs: number,
  tags: Record<string, string> = {}
): void => {
  try {
    datadogRum.addAction('user_action', {
      name: actionName,
      duration: durationMs,
      ...tags
    });
  } catch (error) {
    console.error('Error tracking user action:', error);
  }
};

/**
 * Track calculator operation timing
 * @param operation - Type of calculation operation
 * @param durationMs - Time taken for the calculation to complete
 */
export const trackCalculation = (
  operation: 'add' | 'subtract' | 'multiply' | 'divide' | 'calculate',
  durationMs: number
): void => {
  try {
    datadogRum.addAction('calculation', {
      operation,
      duration: durationMs
    });
  } catch (error) {
    console.error('Error tracking calculation:', error);
  }
};

/**
 * Higher Order Component to add performance tracking to API calls
 * @param apiCall - Original API function
 * @param endpointName - Name of the endpoint being called
 * @returns Wrapped function with performance tracking
 */
export const withApiTracking = <T, R>(
  apiCall: (data: T) => Promise<R>,
  endpointName: string
): (data: T) => Promise<R> => {
  return async (data: T): Promise<R> => {
    const startTime = performance.now();
    try {
      const result = await apiCall(data);
      const duration = performance.now() - startTime;

      // Track successful API call
      datadogRum.addAction('api_call', {
        endpoint: endpointName,
        duration,
        status: 'success'
      });

      return result;
    } catch (error) {
      const duration = performance.now() - startTime;

      // Track failed API call
      datadogRum.addAction('api_call', {
        endpoint: endpointName,
        duration,
        status: 'error',
        error: error instanceof Error ? error.message : 'Unknown error'
      });

      throw error;
    }
  };
};

/**
 * Track page load performance metrics
 */
export const trackPagePerformance = (): void => {
  try {
    // Get performance timing entries
    const perfEntries = performance.getEntriesByType('navigation');
    if (perfEntries.length > 0) {
      const navEntry = perfEntries[0] as PerformanceNavigationTiming;

      // Track page load timings
      datadogRum.addTiming('page_load_time', navEntry.loadEventEnd - navEntry.startTime);
      datadogRum.addTiming('dom_interactive', navEntry.domInteractive - navEntry.startTime);
      datadogRum.addTiming('dom_content_loaded', navEntry.domContentLoadedEventEnd - navEntry.startTime);
    }
  } catch (error) {
    console.error('Error tracking page performance:', error);
  }
};

/**
 * Utility to handle and report frontend errors
 * @param error - Error object or message
 * @param context - Additional context about the error
 */
export const reportError = (
  error: Error | string,
  context: Record<string, any> = {}
): void => {
  try {
    const errorMessage = error instanceof Error ? error.message : error;
    const errorStack = error instanceof Error ? error.stack : undefined;

    // Report to Datadog
    datadogLogs.logger.error('Frontend error occurred', {
      error: {
        message: errorMessage,
        stack: errorStack
      },
      ...context
    });
  } catch (logError) {
    // Fallback to console if Datadog logging fails
    console.error('Original error:', error);
    console.error('Error reporting to monitoring service:', logError);
  }
};

// Export a monitoring instance for use throughout the app
export default {
  initialize: initializeMonitoring,
  trackAction: trackUserAction,
  trackCalculation,
  trackPagePerformance,
  reportError,
  withApiTracking
};
