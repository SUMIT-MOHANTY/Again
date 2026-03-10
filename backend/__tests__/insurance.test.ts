import request from 'supertest';
import { describe, it, expect } from 'vitest';
import app from '@/app';

describe('GET /api/insurance/products', () => {
  it('returns products', async () => {
    const res = await request(app).get('/api/insurance/products');
    expect(res.status).toBe(200);
    expect(res.body.success).toBe(true);
  });
});
