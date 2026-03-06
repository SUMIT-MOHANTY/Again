import { createSlice, PayloadAction } from '@reduxjs/toolkit';
interface AuthState {
  isAuthenticated: boolean;
  jwt: string | null;
  loginError: string | null;
  twoFAError: string | null;
  loading: boolean;
}
const initialState: AuthState = {
  isAuthenticated: false,
  jwt: null,
  loginError: null,
  twoFAError: null,
  loading: false,
};
export const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    loginRequest(state) { state.loading = true; state.loginError = null; },
    loginSuccess(state, action: PayloadAction<string>) { state.loading = false; state.jwt = action.payload; },
    loginFailure(state, action: PayloadAction<string>) { state.loading = false; state.loginError = action.payload; },
    verify2FARequest(state) { state.loading = true; state.twoFAError = null; },
    verify2FASuccess(state) { state.loading = false; state.isAuthenticated = true; },
    verify2FAFailure(state, action: PayloadAction<string>) { state.loading = false; state.twoFAError = action.payload; },
    clearLoginError(state) { state.loginError = null; },
    clearTwoFAError(state) { state.twoFAError = null; },
  },
});
export const {
  loginRequest,
  loginSuccess,
  loginFailure,
  verify2FARequest,
  verify2FASuccess,
  verify2FAFailure,
  clearLoginError,
  clearTwoFAError,
} = authSlice.actions;
export default authSlice.reducer;
