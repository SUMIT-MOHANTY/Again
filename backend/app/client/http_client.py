import httpx, asyncio
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
import pybreaker
from ..config import RETRY_COUNT, RETRY_WAIT, CB_FAILURE_THRESHOLD, CB_RECOVERY_TIMEOUT
from ..util.logger import logger
class ResilientClient:
    def __init__(self):
        self._client = httpx.AsyncClient()
        self._breaker = pybreaker.CircuitBreaker(fail_max=CB_FAILURE_THRESHOLD, reset_timeout=CB_RECOVERY_TIMEOUT)
    def _retry_decorator(self):
        return retry(stop=stop_after_attempt(RETRY_COUNT), wait=wait_fixed(RETRY_WAIT), retry=retry_if_exception_type(httpx.RequestError))
    async def get(self, url: str, **kwargs):
        @self._retry_decorator()
        async def _call():
            return await self._breaker.call_async(self._client.get, url, **kwargs)
        try:
            response = await _call()
            response.raise_for_status()
            return response
        except pybreaker.CircuitBreakerError as e:
            logger.error(f'Circuit breaker open for {url}: {e}')
            raise
        except httpx.HTTPError as e:
            logger.error(f'HTTP error for {url}: {e}')
            raise
