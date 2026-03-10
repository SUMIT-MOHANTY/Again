import axios from '@/services/api';

interface NewClaimPayload {
  policyId: string;
  amount: number;
  description: string;
  attachments: File[];
}

export const claimsApi = {
  create: async (payload: NewClaimPayload) => {
    const form = new FormData();
    form.append('policyId', payload.policyId);
    form.append('amount', String(payload.amount));
    form.append('description', payload.description);
    payload.attachments.forEach(f => form.append('attachments', f));
    const res = await axios.post('/api/claims/new', form, { headers: { 'Content-Type': undefined } });
    return res.data;
  },
};
