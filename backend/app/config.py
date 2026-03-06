import os
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Prompt Service"
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    AZURE_OPENAI_ENDPOINT: str = Field(..., env="AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_KEY: str = Field(..., env="AZURE_OPENAI_KEY")

    class Config:
        env_file = ".env"

settings = Settings()
