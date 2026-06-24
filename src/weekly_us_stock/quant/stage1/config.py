"""Configuration for the Stage 1 FMP point-in-time gateway.

Network behaviour (concurrency, throttling, retry) and alignment behaviour
(month grid, publish-lag assumptions) are kept in one immutable dataclass so a
run is fully reproducible from its config plus the raw payloads.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field, replace

# FMP's free sandbox only serves a handful of high-liquidity names and caps each
# request to 10 historical rows. Hard-coding the allow-list lets the client fail
# fast with a clear message instead of silently returning an upstream error page.
SANDBOX_SYMBOLS = ("AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "META", "NVDA")
SANDBOX_MAX_HISTORY = 10

DEFAULT_BASE_URL = "https://financialmodelingprep.com/stable"


@dataclass(frozen=True)
class RetryConfig:
    """Exponential-backoff-with-jitter policy for transient FMP failures."""

    max_attempts: int = 5
    base_delay: float = 1.0  # seconds; first backoff is ~base_delay
    max_delay: float = 30.0  # cap a single sleep
    backoff_factor: float = 2.0
    jitter: float = 0.25  # +/- fraction of the computed delay (full jitter band)
    # HTTP statuses worth retrying: 429 (rate limit) + the 5xx family.
    retry_statuses: frozenset[int] = frozenset({429, 500, 502, 503, 504})

    def __post_init__(self) -> None:
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be >= 1")
        if self.base_delay <= 0 or self.max_delay <= 0:
            raise ValueError("delays must be positive")


@dataclass(frozen=True)
class GatewayConfig:
    """Top-level Stage 1 configuration."""

    api_key: str
    base_url: str = DEFAULT_BASE_URL
    sandbox: bool = False

    # -- concurrency / throttling --------------------------------------------
    max_concurrency: int = 8  # in-flight requests cap (asyncio.Semaphore)
    min_request_interval: float = 0.21  # ~285 req/min, under the 300/min plan cap
    request_timeout: float = 60.0
    retry: RetryConfig = field(default_factory=RetryConfig)

    # -- alignment behaviour -------------------------------------------------
    # Macro releases (GDP/CPI) carry an event date but are published with a lag.
    # When a payload exposes no explicit release timestamp we conservatively add
    # this many days to the event date to approximate the true disclosure time,
    # so a month-end never sees a print before it could have been announced.
    macro_publish_lag_days: int = 30
    # History depth requested per endpoint (rows). Clamped to the sandbox cap.
    history_limit: int = 120

    def __post_init__(self) -> None:
        if not self.api_key:
            raise ValueError("api_key is required for the FMP gateway")
        if self.max_concurrency < 1:
            raise ValueError("max_concurrency must be >= 1")

    @property
    def effective_history_limit(self) -> int:
        return min(self.history_limit, SANDBOX_MAX_HISTORY) if self.sandbox else self.history_limit

    def assert_symbol_allowed(self, symbol: str) -> None:
        """Sandbox keys only resolve a fixed allow-list; refuse anything else up
        front so a bounded test run fails loudly instead of on an opaque 403."""

        if self.sandbox and symbol.upper() not in SANDBOX_SYMBOLS:
            raise ValueError(
                f"symbol {symbol!r} is not available in the FMP sandbox; "
                f"allowed: {', '.join(SANDBOX_SYMBOLS)}"
            )

    def with_overrides(self, **changes: object) -> GatewayConfig:
        return replace(self, **changes)  # type: ignore[arg-type]

    @classmethod
    def from_env(cls, **overrides: object) -> GatewayConfig:
        """Build from ``FMP_API_KEY`` / ``FMP_SANDBOX`` with explicit overrides."""

        api_key = str(overrides.pop("api_key", None) or os.environ.get("FMP_API_KEY", ""))
        sandbox_env = os.environ.get("FMP_SANDBOX", "").strip().lower() in {"1", "true", "yes"}
        sandbox = bool(overrides.pop("sandbox", sandbox_env))
        return cls(api_key=api_key, sandbox=sandbox, **overrides)  # type: ignore[arg-type]
