import db from '@/lib/db';
import { v4 as uuid } from 'uuid';

export const listPolicies = async (userId: string) =>
  db.select('*').from('policies').where({ user_id: userId });

export const createPolicy = async (userId: string, productId: string, effectiveDate: string) => {
  const [product] = await db.select('*').from('products').where({ id: productId });
  const effective = new Date(effectiveDate);
  const expiry = new Date(effective);
  expiry.setFullYear(effective.getFullYear() + 1);
  const policy = {
    id: uuid(),
    product_id: productId,
    user_id: userId,
    effective_date: effective,
    expiry_date: expiry,
    status: 'ACTIVE',
  };
  await db('policies').insert(policy);
  return policy;
};
