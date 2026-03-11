export interface LoginRequest {
  email: string;
  password: string;
  totp_code?: string;
}

export interface LoginResponse {
  access_token?: string;
  expires_in?: number;
  refresh_token?: string;
  mfa_required?: boolean;
}

export interface MfaSetupResponse {
  qr_code: string;
  backup_codes: string[];
}

export interface MfaVerifyRequest {
  totp_code: string;
}

export interface MfaVerifyResponse {
  ok: boolean;
}
