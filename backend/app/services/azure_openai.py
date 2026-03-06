from backend.app.config import settings

if settings.use_mock:
    from backend.app.services.mock_azure_openai import MockAzureOpenAI as AzureOpenAIClient
else:
    # Replace the following import with the real Azure OpenAI client when available
    from some_real_azure_module import AzureOpenAIClient  # type: ignore

azure_client = AzureOpenAIClient()
