import { config } from "dotenv";
config();
export const SERVER_PORT = Number(process.env.SERVER_PORT) || 3000;
export const POSTGRES_URL = process.env.POSTGRES_URL || "postgres://user:pass@localhost:5432/appdb";
export const JWT_SECRET = process.env.JWT_SECRET || "changeme";
