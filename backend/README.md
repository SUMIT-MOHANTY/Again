# Project README

... existing content ...

## 🔐 Data Encryption at Rest
- **Placeholder key**: `ENCRYPTION_KEY=your-key-here` (set in `.env`).
- **Column‑level encryption** uses `sqlalchemy-utils.EncryptedType` with AES‑256.
- **Key rotation**: update `ENCRYPTION_KEY` env var, run an Alembic migration that recreates tables or re‑encrypts columns.
