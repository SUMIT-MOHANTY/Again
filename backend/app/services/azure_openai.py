import httpx
import json
import time
from ..config import settings

class AzureOpenAIService:
    def __init__(self):
        self.endpoint = settings.AZURE_OPENAI_ENDPOINT.rstrip('/')
        self.key = settings.AZURE_OPENAI_KEY
        self.deployment = settings.AZURE_OPENAI_DEPLOYMENT
        self.headers = {
            "Content-Type": "application/json",
            "api-key": self.key,
        }

    def _post(self, payload: dict, retries: int = 3, backoff: float = 1.0) -> dict:
        url = f"{self.endpoint}/openai/deployments/{self.deployment}/chat/completions?api-version=2023-05-15"
        for attempt in range(1, retries + 1):
            try:
                response = httpx.post(url, headers=self.headers, json=payload, timeout=30.0)
                response.raise_for_status()
                return response.json()
            except (httpx.HTTPError, json.JSONDecodeError) as exc:
                if attempt == retries:
                    raise
                time.sleep(backoff * attempt)

    def get_completion(self, messages: list[dict], temperature: float = 0.7) -> str:
        payload = {
            "model": "gpt-35-turbo",
            "messages": messages,
            "temperature": temperature,
        }
        result = self._post(payload)
        # Extract the first choice text safely
        try:
            return result["choices"][0]["message"]["content"]
        except (KeyError, IndexError):
            raise RuntimeError("Unexpected response format from Azure OpenAI")
def get_completion(prompt: str) -> str:
    # Placeholder for Azure OpenAI call - returns mock data
    return f'Mocked Azure response for "{prompt}"'
