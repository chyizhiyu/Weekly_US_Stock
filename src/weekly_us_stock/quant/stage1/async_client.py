"""Async FMP gateway: bounded concurrency, throttling, backoff retry.

All network IO for Stage 1 lives here. The class is deliberately thin and
side-effect-isolated so the parsers (:mod:`endpoints`) and the resampler
(:mod:`resampler`) stay pure and unit-testable on canned payloads.

Design choices, each defending a specific failure mode:

- **Bounded concurrency** via an ``asyncio.Semaphore`` caps in-flight sockets so
  a wide universe sweep cannot exhaust file descriptors or trip FMP's burst
  guard.
- **Global throttle** via an async rate limiter enforces a minimum spacing
  between request *starts*, independent of concurrency, to stay under the
  plan's requests-per-minute ceiling.
- **Exponential backoff with full jitter** retries only *transient* failures
  (connection errors, timeouts, HTTP 429/5xx). A ``Retry-After`` header, when
  present, overrides the computed delay. Deterministic 4xx (other than 429) are
  surfaced immediately - retrying a 401/403/404 only wastes quota.

The session is created lazily inside ``__aenter__`` and can be injected for
tests, so the retry/backoff logic is exercised without a real socket.
"""

from __future__ import annotations

import asyncio
import logging
import random
from typing import TYPE_CHECKING, Any

from weekly_us_stock.quant.stage1.config import GatewayConfig, RetryConfig

if TYPE_CHECKING:  # avoid importing aiohttp at module import for non-network users
    import aiohttp

logger = logging.getLogger(__name__)


class TransientHTTPError(Exception):
    """A retryable HTTP status (429 or 5xx). Carries an optional ``retry_after``
    (seconds) parsed from the response header so the backoff can honour it."""

    def __init__(self, status: int, retry_after: float | None = None) -> None:
        super().__init__(f"transient HTTP {status}")
        self.status = status
        self.retry_after = retry_after


class FMPHTTPError(Exception):
    """A non-retryable HTTP error (e.g. 401/403/404). Fails fast."""

    def __init__(self, status: int, body: str) -> None:
        super().__init__(f"HTTP {status}: {body[:200]}")
        self.status = status
        self.body = body


def compute_backoff(
    attempt: int,
    policy: RetryConfig,
    *,
    retry_after: float | None = None,
    rng: random.Random | None = None,
) -> float:
    """Seconds to sleep before retry ``attempt`` (1-indexed).

    ``Retry-After`` from the server wins outright (still clamped to
    ``max_delay``). Otherwise: ``base * factor**(attempt-1)``, clamped, then
    full-jitter scaled into ``[delay*(1-jitter), delay*(1+jitter)]``.
    """

    if retry_after is not None and retry_after >= 0:
        return min(retry_after, policy.max_delay)
    raw = policy.base_delay * (policy.backoff_factor ** (attempt - 1))
    delay = min(raw, policy.max_delay)
    if policy.jitter <= 0:
        return delay
    draw = (rng or random).uniform(-policy.jitter, policy.jitter)
    return max(0.0, delay * (1.0 + draw))


def _parse_retry_after(raw: str | None) -> float | None:
    if not raw:
        return None
    try:
        return max(0.0, float(raw))  # delta-seconds form
    except (TypeError, ValueError):
        return None  # HTTP-date form is rare from FMP; fall back to backoff


class _AsyncRateLimiter:
    """Enforce a minimum spacing between request *starts* across all coroutines."""

    def __init__(self, min_interval: float) -> None:
        self._min_interval = max(0.0, min_interval)
        self._lock = asyncio.Lock()
        self._next_allowed = 0.0

    async def acquire(self) -> None:
        if self._min_interval <= 0:
            return
        async with self._lock:
            loop = asyncio.get_running_loop()
            now = loop.time()
            wait = self._next_allowed - now
            if wait > 0:
                await asyncio.sleep(wait)
                now = loop.time()
            self._next_allowed = now + self._min_interval


class AsyncFMPClient:
    """Async HTTP gateway to the FMP ``/stable`` API.

    Use as an async context manager so the underlying session is always closed::

        async with AsyncFMPClient(config) as client:
            payload = await client.get("income-statement", {"symbol": "AAPL"})
    """

    def __init__(
        self,
        config: GatewayConfig,
        *,
        session: aiohttp.ClientSession | None = None,
        rng: random.Random | None = None,
    ) -> None:
        self.config = config
        self._session = session
        self._owns_session = session is None
        self._semaphore = asyncio.Semaphore(config.max_concurrency)
        self._rate_limiter = _AsyncRateLimiter(config.min_request_interval)
        self._rng = rng or random.Random()

    async def __aenter__(self) -> AsyncFMPClient:
        if self._session is None:
            import aiohttp  # imported lazily: pure-parser users never need it

            timeout = aiohttp.ClientTimeout(total=self.config.request_timeout)
            self._session = aiohttp.ClientSession(timeout=timeout)
        return self

    async def __aexit__(self, *exc: object) -> None:
        if self._owns_session and self._session is not None:
            await self._session.close()
            self._session = None

    # -- public API -----------------------------------------------------------

    async def get(self, path: str, params: dict[str, Any], *, raw: bool = False) -> Any:
        """GET ``{base}/{path}`` with the api key injected, retried on transient
        failures. Returns parsed JSON (``raw=False``) or the raw text body."""

        if self._session is None:
            raise RuntimeError("AsyncFMPClient must be used as an async context manager")
        merged = {**params, "apikey": self.config.api_key}
        url = f"{self.config.base_url.rstrip('/')}/{path.lstrip('/')}"
        policy = self.config.retry
        last_exc: Exception | None = None
        for attempt in range(1, policy.max_attempts + 1):
            await self._rate_limiter.acquire()
            try:
                async with self._semaphore:
                    return await self._request_once(url, merged, raw=raw, policy=policy)
            except TransientHTTPError as exc:
                last_exc = exc
                retry_after = exc.retry_after
            except (TimeoutError, OSError, _aiohttp_client_error()) as exc:
                last_exc = exc
                retry_after = None
            if attempt >= policy.max_attempts:
                break
            delay = compute_backoff(attempt, policy, retry_after=retry_after, rng=self._rng)
            logger.warning(
                "FMP %s attempt %d/%d failed (%s); backing off %.2fs",
                path,
                attempt,
                policy.max_attempts,
                last_exc,
                delay,
            )
            await asyncio.sleep(delay)
        assert last_exc is not None  # loop only exits via break after a failure
        raise last_exc

    async def get_many(
        self, requests: list[tuple[str, dict[str, Any]]], *, raw: bool = False
    ) -> list[Any]:
        """Fan out many GETs concurrently (bounded by the shared semaphore),
        preserving request order. Exceptions from any call propagate."""

        tasks = [asyncio.create_task(self.get(path, params, raw=raw)) for path, params in requests]
        return await asyncio.gather(*tasks)

    # -- internals ------------------------------------------------------------

    async def _request_once(
        self, url: str, params: dict[str, Any], *, raw: bool, policy: RetryConfig
    ) -> Any:
        assert self._session is not None
        async with self._session.get(url, params=params) as response:
            status = response.status
            if status in policy.retry_statuses:
                retry_after = _parse_retry_after(response.headers.get("Retry-After"))
                raise TransientHTTPError(status, retry_after)
            if status >= 400:
                raise FMPHTTPError(status, await response.text())
            return await response.text() if raw else await response.json()


def _aiohttp_client_error() -> type[BaseException]:
    """Resolve ``aiohttp.ClientError`` lazily so importing this module never
    requires aiohttp (only network use does)."""

    try:
        import aiohttp

        return aiohttp.ClientError
    except ModuleNotFoundError:  # pragma: no cover - aiohttp absent
        return OSError
