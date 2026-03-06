import { useDispatch, useSelector } from 'react-redux';
import type { RootState } from '../store';
import {
  loginRequest,
  loginSuccess,
  loginFailure,
  verify2FARequest,
  verify2FASuccess,
  verify2FAFailure,
  clearLoginError,
  clearTwoFAError,
} from '../store/authSlice';
import { apiClient } from '../services/apiClient';
import { LoginRequest, LoginResponse, Verify2FARequest, Verify2FAResponse } from '../types/auth';

export const useAuth = () => {
  const dispatch = useDispatch();
  const auth = useSelector((state: RootState) => state.auth);

  const dispatchLogin = async (payload: LoginRequest) => {
    dispatch(loginRequest());
    try {
      const data = await apiClient.post<LoginResponse>('/api/login', payload);
      dispatch(loginSuccess(data.token));
    } catch (e: any) {
      dispatch(loginFailure(e?.message || 'Login failed'));
    }
  };

  const dispatchVerify2FA = async (payload: Verify2FARequest) => {
    dispatch(verify2FARequest());
    try {
      const data = await apiClient.post<Verify2FAResponse>('/api/verify-2fa', payload);
      if (data.success) dispatch(verify2FASuccess()); else throw new Error('Invalid code');
    } catch (e: any) {
      dispatch(verify2FAFailure(e?.message || '2FA verification failed'));
    }
  };

  const clearErrors = () => {
    dispatch(clearLoginError());
    dispatch(clearTwoFAError());
  };

  return { auth, dispatchLogin, dispatchVerify2FA, clearErrors };
};
