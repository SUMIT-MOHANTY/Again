import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_URI: str = os.getenv("POSTGRES_URI", "postgres://user:password@localhost/db")
    AZURE_OPENAI_KEY: str = os.getenv("AZURE_OPENAI_KEY", "your-key-here")
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT", "https://your-openai-instance.openai.azure.com/")

    @property
    def use_mock(self) -> bool:
        placeholders = [
            "postgres://user:password@localhost/db",
            "your-key-here",
            "https://your-openai-instance.openai.azure.com/",
        ]
        return (
            self.POSTGRES_URI in placeholders
            or self.AZURE_OPENAI_KEY in placeholders
            or self.AZURE_OPENAI_ENDPOINT in placeholders
        )

settings = Settings()
