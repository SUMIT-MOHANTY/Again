import db from '@/lib/db';
import { v4 as uuid } from 'uuid';

export const createClaim = async (policyId: string, amount: number, description: string, attachments: any[]) => {
  const urls = attachments.map(() => 'https://s3.mock/url');
  const claim = {
    id: uuid(),
    policy_id: policyId,
    amount,
    description,
    attachments: urls,
    status: 'SUBMITTED',
  };
  await db('claims').insert(claim);
  return { claimId: claim.id, status: 'SUBMITTED' };
};
