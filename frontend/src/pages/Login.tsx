import React, { useState } from 'react';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [token, setToken] = useState('');
  const [code, setCode] = useState('');
  const [message, setMessage] = useState('');

  const handleLogin = async () => {
    const resp = await fetch('http://localhost:8000/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    const data = await resp.json();
    if (resp.ok) setToken(data.2fa_token);
    else setMessage(data.detail || 'Login failed');
  };

  const handleVerify = async () => {
    const resp = await fetch('http://localhost:8000/auth/verify-2fa', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ token, code })
    });
    const data = await resp.json();
    if (resp.ok) setMessage('Authenticated');
    else setMessage(data.detail || 'Verification failed');
  };

  return (
    <div>
      <h2>Login</h2>
      <input placeholder="email" value={email} onChange={e=>setEmail(e.target.value)} />
      <input placeholder="password" type="password" value={password} onChange={e=>setPassword(e.target.value)} />
      <button onClick={handleLogin}>Send 2FA</button>
      {token && (
        <>
          <input placeholder="2FA code" value={code} onChange={e=>setCode(e.target.value)} />
          <button onClick={handleVerify}>Verify</button>
        </>
      )}
      <p>{message}</p>
    </div>
  );
}
