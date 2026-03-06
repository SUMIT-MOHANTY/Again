import httpx
from tenacity import retry, stop_after_attempt, wait_exponential
import pybreaker
from backend.config import Config

retry_decorator = retry(
    stop=stop_after_attempt(Config.RETRY_COUNT),
    wait=wait_exponential(multiplier=Config.RETRY_DELAY),
)

circuit_breaker = pybreaker.CircuitBreaker(
    fail_max=Config.CIRCUIT_BREAKER_FAIL_MAX,
    reset_timeout=Config.CIRCUIT_BREAKER_RESET_TIMEOUT,
)

class ResilientHttpClient:
    def __init__(self):
        self._client = httpx.AsyncClient()

    @circuit_breaker
    @retry_decorator
    async def get(self, url: str, **kwargs):
        return await self._client.get(url, **kwargs)

    @circuit_breaker
    @retry_decorator
    async def post(self, url: str, **kwargs):
        return await self._client.post(url, **kwargs)

    async def close(self):
        await self._client.aclose()

client = ResilientHttpClient()
