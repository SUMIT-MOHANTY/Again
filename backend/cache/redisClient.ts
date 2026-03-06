import { createClient } from 'redis';
import { config } from '../config/config';
export const redisClient = createClient({
  url: config.REDIS_URL
});
redisClient.on('error', (err) => console.error('Redis Client Error', err));
redisClient.connect().catch(console.error);
