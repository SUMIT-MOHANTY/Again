import React, { useState, ChangeEvent, FormEvent } from 'react';
import { useAuth } from '../hooks/useAuth';
import Spinner from './Spinner';

const TwoFAInput: React.FC = () => {
  const { auth, dispatchVerify2FA, clearErrors } = useAuth();
  const [code, setCode] = useState('');

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setCode(e.target.value);
    clearErrors();
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!auth.jwt) return;
    await dispatchVerify2FA({ code, token: auth.jwt });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>2FA Code:</label>
      <input type="text" value={code} onChange={handleChange} required />
      {auth.loading && <Spinner />}
      {auth.twoFAError && <div className="error">{auth.twoFAError}</div>}
      <button type="submit" disabled={auth.loading || !code}>Verify</button>
    </form>
  );
};
export default TwoFAInput;
