from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    database_url: str = Field(default="postgresql+psycopg2://postgres:postgres@db:5432/postgres")

    class Config:
        env_file = ".env"

settings = Settings()
