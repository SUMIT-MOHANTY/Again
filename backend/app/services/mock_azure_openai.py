class MockAzureOpenAI:
    def get_completion(self, prompt: str) -> str:
        return f"Mocked completion for: {prompt}"
