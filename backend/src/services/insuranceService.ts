import db from '@/lib/db';

export const getProducts = async () => db.select('*').from('products');
