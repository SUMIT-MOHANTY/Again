import { Router } from 'express';
import { getProducts } from '@/services/insuranceService';
import asyncHandler from '@/lib/asyncHandler';

const router = Router();

router.get(
  '/insurance/products',
  asyncHandler(async (_req, res) => {
    const products = await getProducts();
    res.json({ success: true, products });
  }),
);

export default router;
