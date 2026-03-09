export interface LoginRequest { username: string; password: string; }
export interface LoginResponse { token: string; }
export interface Verify2FARequest { code: string; token: string; }
export interface Verify2FAResponse { success: boolean; }
