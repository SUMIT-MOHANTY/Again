import pytest
from backend.app.config import settings
from backend.app.services.mock_azure_openai import MockAzureOpenAI

def test_use_mock_and_azure_completion():
    assert settings.use_mock is True
    client = MockAzureOpenAI()
    assert client.get_completion("test") == "Mocked completion for: test"
