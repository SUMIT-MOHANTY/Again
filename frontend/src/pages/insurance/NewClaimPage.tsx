import { useState } from 'react';
import { claimsApi } from '@/services/api/claims';
import IdentityVerifiedUpload from '@/components/IdentityVerifiedUpload';
import PdfPreview from '@/components/PdfPreview';

export default function NewClaimPage() {
  const [policyId, setPolicyId] = useState('');
  const [amount, setAmount] = useState('');
  const [description, setDescription] = useState('');
  const [files, setFiles] = useState<File[]>([]);

  const handleSubmit = async () => {
    await claimsApi.create({ policyId, amount: Number(amount), description, attachments: files });
    alert('Claim submitted');
  };

  return (
    <div className="p-8 space-y-4">
      <h1 className="text-2xl font-bold">Submit New Claim</h1>
      <input className="block border p-2" placeholder="Policy ID" value={policyId} onChange={e => setPolicyId(e.target.value)} />
      <input type="number" className="block border p-2" placeholder="Amount" value={amount} onChange={e => setAmount(e.target.value)} />
      <textarea className="block border p-2" placeholder="Description" value={description} onChange={e => setDescription(e.target.value)} />
      <IdentityVerifiedUpload onChange={setFiles} />
      {files.map(f => (
        <PdfPreview key={f.name} file={f} />
      ))}
      <button onClick={handleSubmit} className="bg-blue-600 text-white px-4 py-2 rounded">Submit</button>
    </div>
  );
}
