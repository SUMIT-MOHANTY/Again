from pydantic import BaseSettings, PostgresDsn, Field

class Settings(BaseSettings):
    POSTGRES_URL: PostgresDsn = Field(
        "postgresql+asyncpg://user:password@localhost:5432/lms",
        env="POSTGRES_URL",
    )
    JWT_SECRET_KEY: str = Field("supersecret", env="JWT_SECRET_KEY")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
