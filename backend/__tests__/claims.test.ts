import request from 'supertest';
import { describe, it, expect } from 'vitest';
import app from '@/app';

describe('POST /api/claims/new', () => {
  it('creates claim', async () => {
    const res = await request(app)
      .post('/api/claims/new')
      .field('policyId', 'p')
      .field('amount', 100)
      .field('description', 'test');
    expect(res.status).toBe(200);
    expect(res.body.success).toBe(true);
  });
});
