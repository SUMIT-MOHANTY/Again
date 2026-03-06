from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    PROJECT_NAME: str = Field(default="AI Service", env="PROJECT_NAME")
    AZURE_OPENAI_ENDPOINT: str = Field(..., env="AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_KEY: str = Field(..., env="AZURE_OPENAI_KEY")
    AZURE_OPENAI_DEPLOYMENT: str = Field(..., env="AZURE_OPENAI_DEPLOYMENT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
