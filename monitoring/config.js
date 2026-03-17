/**
 * Core monitoring configuration for the calculator application
 * This file centralizes monitoring settings for both frontend and backend
 */

const appName = 'calculator';

const config = {
  // Core configuration
  datadog: {
    apiKey: process.env.DD_API_KEY,
    appKey: process.env.DD_APP_KEY,
    serviceName: appName,
    env: process.env.NODE_ENV || 'development',
    version: process.env.APP_VERSION || '1.0.0',

    // Sampling rates
    traceSampleRate: 1.0, // 100% sampling in dev/staging, reduce in production
    logSampleRate: 1.0,

    // Feature flags
    enableRealUserMonitoring: true,
    enableDistributedTracing: true,
    enableCustomMetrics: true,

    // Performance impact settings
    maxBatchSize: 100,
    flushIntervalSeconds: 15,

    // Thresholds for alerts
    thresholds: {
      apiResponseTime: 500, // milliseconds
      pageLoadTime: 2000, // milliseconds
      errorRate: 0.05, // 5%
      cpuUsage: 0.8, // 80%
      memoryUsage: 0.8, // 80%
    }
  },

  // Environment-specific overrides
  environments: {
    production: {
      traceSampleRate: 0.1, // 10% sampling in production
      logSampleRate: 0.2,
      flushIntervalSeconds: 30,
    },
    staging: {
      traceSampleRate: 0.5, // 50% sampling in staging
    }
  },

  // Fallback configuration if monitoring service is unavailable
  fallback: {
    enabled: true,
    localLogging: true,
    consoleReporting: process.env.NODE_ENV !== 'production',
    bufferSize: 1000, // store up to 1000 events locally
  }
};

// Apply environment-specific configuration overrides
const applyEnvironmentConfig = (baseConfig) => {
  const env = baseConfig.datadog.env;
  if (env && baseConfig.environments[env]) {
    baseConfig.datadog = {
      ...baseConfig.datadog,
      ...baseConfig.environments[env]
    };
  }
  return baseConfig;
};

module.exports = applyEnvironmentConfig(config);
