import * as dotenv from 'dotenv';
dotenv.config();
export const config = {
  PORT: process.env.PORT ? parseInt(process.env.PORT) : 3000,
  POSTGRES_URL: process.env.POSTGRES_URL || '',
  REDIS_URL: process.env.REDIS_URL || ''
};
