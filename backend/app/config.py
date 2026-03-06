import os
from pydantic import BaseSettings, SecretStr

class Settings(BaseSettings):
    POSTGRES_USER: str = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD: SecretStr = SecretStr(os.getenv('POSTGRES_PASSWORD', 'postgres'))
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'appdb')
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST', 'db')
    POSTGRES_PORT: int = int(os.getenv('POSTGRES_PORT', 5432))
    REDIS_HOST: str = os.getenv('REDIS_HOST', 'redis')
    REDIS_PORT: int = int(os.getenv('REDIS_PORT', 6379))
    MAILHOG_HOST: str = os.getenv('MAILHOG_HOST', 'mailhog')
    MAILHOG_PORT: int = int(os.getenv('MAILHOG_PORT', 1025))

    class Config:
        env_file = '.env'

settings = Settings()
