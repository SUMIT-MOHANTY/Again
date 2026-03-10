import request from 'supertest';
import { describe, it, expect } from 'vitest';
import app from '@/app';

describe('POST /api/policies', () => {
  it('creates policy', async () => {
    const res = await request(app)
      .post('/api/policies')
      .send({ userId: 'u', productId: 'p', effectiveDate: '2024-01-01' });
    expect(res.status).toBe(200);
    expect(res.body.success).toBe(true);
  });
});
