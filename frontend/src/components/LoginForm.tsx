import React, { useState, ChangeEvent, FormEvent } from 'react';
import { useAuth } from '../hooks/useAuth';
import Spinner from './Spinner';
import TwoFAInput from './TwoFAInput';

const LoginForm: React.FC = () => {
  const { auth, dispatchLogin, clearErrors } = useAuth();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const onUserChange = (e: ChangeEvent<HTMLInputElement>) => {
    e.target.name === 'username' ? setUsername(e.target.value) : setPassword(e.target.value);
    clearErrors();
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    await dispatchLogin({ username, password });
  };

  const canSubmit = username && password && !auth.loading;

  return (
    <div>
      {auth.jwt && !auth.isAuthenticated ? (
        <TwoFAInput />
      ) : (
        <form onSubmit={handleSubmit}>
          <label>Username:</label>
          <input name="username" value={username} onChange={onUserChange} required />
          <label>Password:</label>
          <input type="password" name="password" value={password} onChange={onUserChange} required />
          {auth.loading && <Spinner />}
          {auth.loginError && <div className="error">{auth.loginError}</div>}
          <button type="submit" disabled={!canSubmit}>Login</button>
        </form>
      )}
    </div>
  );
};
export default LoginForm;
