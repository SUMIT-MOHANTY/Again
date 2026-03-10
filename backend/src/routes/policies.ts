import { Router } from 'express';
import { listPolicies, createPolicy } from '@/services/policyService';
import asyncHandler from '@/lib/asyncHandler';

const router = Router();

router.get(
  '/policies',
  asyncHandler(async (req, res) => {
    const policies = await listPolicies(req.query.userId as string);
    res.json({ success: true, policies });
  }),
);

router.post(
  '/policies',
  asyncHandler(async (req, res) => {
    const { userId, productId, effectiveDate } = req.body;
    const policy = await createPolicy(userId, productId, effectiveDate);
    res.json({ success: true, data: policy });
  }),
);

export default router;
