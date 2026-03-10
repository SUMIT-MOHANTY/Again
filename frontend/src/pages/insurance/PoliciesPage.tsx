import { useEffect, useState } from 'react';
import { policiesApi } from '@/services/api/policies';
import { Policy } from '@/types/insurance';
import { useAuth } from '@/hooks/auth';

export default function PoliciesPage() {
  const { user } = useAuth();
  const [policies, setPolicies] = useState<Policy[]>([]);
  if (!user) return null;

  useEffect(() => { policiesApi.list(user.id).then(setPolicies); }, [user.id]);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">My Policies</h1>
      <ul className="space-y-4">
        {policies.map(p => (
          <li key={p.id} className="border p-4 rounded">
            <p>Policy: {p.id}</p>
            <p>From {p.effectiveDate} to {p.expiryDate}</p>
            <p>Status: {p.status}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
