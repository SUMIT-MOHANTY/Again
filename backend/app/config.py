from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL: str
    ENCRYPTION_KEY: str = os.getenv('ENCRYPTION_KEY', 'your-key-here')
    class Config:
        env_file = '.env'
