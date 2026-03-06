import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    # Placeholder 32‑byte base64 key (44 chars). Replace in production.
    ENCRYPTION_KEY: str = os.getenv('ENCRYPTION_KEY', 'MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMA==')

settings = Settings()
