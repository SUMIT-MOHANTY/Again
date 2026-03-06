import os
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    AZURE_OPENAI_KEY: str = Field('your-azure-openai-key', env='AZURE_OPENAI_KEY')
    POSTGRES_USER: str = Field('postgres', env='POSTGRES_USER')
    POSTGRES_PASSWORD: str = Field('postgres', env='POSTGRES_PASSWORD')
    POSTGRES_DB: str = Field('postgres', env='POSTGRES_DB')
    POSTGRES_HOST: str = Field('db', env='POSTGRES_HOST')
    POSTGRES_PORT: int = Field(5432, env='POSTGRES_PORT')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
