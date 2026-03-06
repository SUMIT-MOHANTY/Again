import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import LoginForm from '../components/LoginForm';
import { useAuth } from '../hooks/useAuth';

const LoginPage: React.FC = () => {
  const navigate = useNavigate();
  const { auth } = useAuth();

  useEffect(() => {
    if (auth.isAuthenticated) navigate('/dashboard');
  }, [auth.isAuthenticated, navigate]);

  return <LoginForm />;
};
export default LoginPage;
