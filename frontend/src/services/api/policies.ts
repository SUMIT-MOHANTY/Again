import axios from '@/services/api';
import { Policy } from '@/types/insurance';

export const policiesApi = {
  list: async (userId: string): Promise<Policy[]> => {
    const res = await axios.get('/api/policies', { params: { userId } });
    return res.data.policies;
  },
  create: async (userId: string, productId: string, effectiveDate: string): Promise<Policy> => {
    const res = await axios.post('/api/policies', { userId, productId, effectiveDate });
    return res.data;
  },
};
