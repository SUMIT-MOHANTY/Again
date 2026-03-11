import { Pool } from 'pg';
import { CONFIG } from '../config';

export const pool = new Pool({
  connectionString: CONFIG.DATABASE_URL
});

pool.on('error', (err) => {
  console.error('Unexpected error on idle client', err);
  process.exit(-1);
});
