export const CONFIG = {
  JWT_SECRET: process.env.JWT_SECRET || 'development-secret-change-in-production',
  DATABASE_URL: process.env.DATABASE_URL || 'postgresql://localhost/captive_core',
  MFA_ISSUER: 'CaptiveCore',
  TOKEN_EXPIRY: 3600, // 1 hour in seconds
  BCRYPT_ROUNDS: 10,
  TOTP_WINDOW: 1
} as const;

export default CONFIG;
