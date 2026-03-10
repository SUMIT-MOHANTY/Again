import axios from '@/services/api';
import { Product } from '@/types/insurance';

export const insuranceApi = {
  getProducts: async (): Promise<Product[]> => {
    const res = await axios.get('/api/insurance/products');
    return res.data.products;
  },
};
