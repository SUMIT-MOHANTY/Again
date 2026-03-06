import os
from dataclasses import dataclass

@dataclass
class Config:
    POSTGRES_URI: str = os.getenv('POSTGRES_URI', 'postgres://user:password@localhost/db')
    AZURE_OPENAI_KEY: str = os.getenv('AZURE_OPENAI_KEY', 'your-key-here')
    AZURE_OPENAI_ENDPOINT: str = os.getenv('AZURE_OPENAI_ENDPOINT', 'https://your-resource.openai.azure.com/')
    AZURE_OPENAI_DEPLOYMENT: str = os.getenv('AZURE_OPENAI_DEPLOYMENT', 'gpt-4o')

config = Config()
