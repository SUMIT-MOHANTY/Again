from pydantic import BaseSettings, Field

class Config(BaseSettings):
    RETRY_COUNT: int = Field(3, env="RETRY_COUNT")
    RETRY_DELAY: float = Field(0.2, env="RETRY_DELAY")
    CIRCUIT_BREAKER_FAIL_MAX: int = Field(5, env="CIRCUIT_BREAKER_FAIL_MAX")
    CIRCUIT_BREAKER_RESET_TIMEOUT: int = Field(60, env="CIRCUIT_BREAKER_RESET_TIMEOUT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

config = Config()
