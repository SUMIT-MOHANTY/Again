# Resilience

| Variable | Default | Description |
|---|---|---|
| RETRY_COUNT | 3 | Number of retry attempts for failing external calls. |
| RETRY_DELAY | 0.2 | Base delay (seconds) for exponential backoff. |
| CIRCUIT_BREAKER_FAIL_MAX | 5 | Failures before circuit opens. |
| CIRCUIT_BREAKER_RESET_TIMEOUT | 60 | Seconds before circuit attempts to close. |

The `ResilientHttpClient` wraps `httpx.AsyncClient` with Tenacity retry and PyBreaker circuit‑breaker.
