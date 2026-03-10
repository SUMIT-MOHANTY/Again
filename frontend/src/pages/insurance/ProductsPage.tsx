import { useEffect, useState } from 'react';
import { insuranceApi } from '@/services/api/insurance';
import { Product } from '@/types/insurance';

export default function ProductsPage() {
  const [products, setProducts] = useState<Product[]>([]);
  useEffect(() => { insuranceApi.getProducts().then(setProducts); }, []);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Insurance Products</h1>
      <ul className="space-y-4">
        {products.map(p => (
          <li key={p.id} className="border p-4 rounded">
            <h2 className="font-semibold">{p.name}</h2>
            <p>{p.description}</p>
            <p>Premium: ${p.premium} | Max coverage: ${p.maxCoverage}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
