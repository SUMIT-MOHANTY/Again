import os
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field(default="postgresql://postgres:postgres@db:5432/postgres")
    REDIS_URL: str = Field(default="redis://redis:6379/0")
    JWT_SECRET: str = Field(default="super-secret-key")
    TWO_FA_SECRET: str = Field(default=os.getenv("2FA_SECRET", "your-2fa-secret-here"))

    class Config:
        env_file = ".env"

settings = Settings()
