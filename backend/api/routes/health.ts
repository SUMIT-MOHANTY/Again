import { Router } from 'express';
import { healthCheck } from '../controllers/healthController';
export const healthRouter = Router();
healthRouter.get('/health', healthCheck);
