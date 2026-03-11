import { pool } from './pool';
import fs from 'fs';
import path from 'path';

export async function setupDatabase() {
  try {
    const migration = fs.readFileSync(
      path.join(__dirname, 'migrations', '001_mfa_tables.sql'),
      'utf8'
    );
    
    await pool.query(migration);
    console.log('MFA tables created successfully');
  } catch (error) {
    console.error('Error setting up database:', error);
    throw error;
  }
}
