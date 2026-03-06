import pytest
import respx
import httpx
from backend.client.resilient_http_client import client
from pybreaker import CircuitBreakerError
from backend.config import Config

@pytest.mark.asyncio
@respx.mock
async def test_retry_logic():
    attempts = 0

    @respx.route(method="GET", url="https://example.com/api/test")
    def handler(request):
        nonlocal attempts
        attempts += 1
        if attempts < Config.RETRY_COUNT:
            return httpx.Response(500)
        return httpx.Response(200, json={"ok": True})

    response = await client.get("https://example.com/api/test")
    assert response.status_code == 200
    assert attempts == Config.RETRY_COUNT

@pytest.mark.asyncio
@respx.mock
async def test_circuit_breaker_opens():
    @respx.route(method="GET", url="https://example.com/api/fail")
    def handler(request):
        return httpx.Response(500)

    for _ in range(Config.CIRCUIT_BREAKER_FAIL_MAX):
        with pytest.raises(httpx.HTTPStatusError):
            resp = await client.get("https://example.com/api/fail")
            resp.raise_for_status()

    with pytest.raises(CircuitBreakerError):
        await client.get("https://example.com/api/fail")
