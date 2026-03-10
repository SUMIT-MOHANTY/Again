import { Router } from 'express';
import multer from 'multer';
import { createClaim } from '@/services/claimService';
import asyncHandler from '@/lib/asyncHandler';

const upload = multer({ limits: { fileSize: 5 * 1024 * 1024 } });
const router = Router();

router.post(
  '/claims/new',
  upload.any(),
  asyncHandler(async (req, res) => {
    const { policyId, amount, description } = req.body;
    const attachments = req.files as Express.Multer.File[];
    const data = await createClaim(policyId, Number(amount), description, attachments);
    res.json({ success: true, data });
  }),
);

export default router;
