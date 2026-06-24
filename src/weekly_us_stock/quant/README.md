# `quant/` — GNN-Transformer-DRL monthly quant stack

A research stack layered on top of the weekly screener's FMP plumbing, built in
six independently testable stages. **Only Stage 1 is implemented today**; later
stages consume the aligned monthly matrix it produces.

| Stage | Module | Status | Purpose |
|------:|--------|--------|---------|
| 1 | `stage1` | ✅ shipped | FMP dual-track timestamp alignment gateway + monthly resampler |
| 2 | `stage2` | deferred | Markov regime-switching (MRSM) + AMA defensive front switch |
| 3 | `stage3` | deferred | SSA decomposition + Lambert-W feature de-noising |
| 4 | `stage4` | deferred | Combinatorial purged & embargoed cross-validation (CPCV) |
| 5 | `stage5` | deferred | GNN-Transformer encoder + Focal-Loss/OHEM head |
| 6 | `stage6` | deferred | DRL-PPO allocator + deflated-Sharpe backtest |

## Stage 1 — what it guarantees

Every observation carries **two** timestamps, and only one of them may ever be
compared to a rebalance date:

- `event_time` — when the fact economically happened (fiscal period end, the
  quarter an EPS belongs to, the month a GDP print measures). Labelling only.
- `disclosure_time` — when it first became publicly usable (SEC `acceptedDate`,
  an analyst grade's publish `date`, a lagged macro release). **The only
  timestamp the gateway aligns against `T`.**

At each month-end trading day `T`, a feature uses the latest observation with
`disclosure_time <= T` (a backward `merge_asof`). Sparse, irregular releases
forward-fill for free; the first disclosure before `T` is null, never the
future. A hidden `__asof_*` audit column records the disclosure actually used
and `PointInTimeMonthlyResampler.build` raises `LookAheadError` if any exceeds
`T`.

### Components

- `config.py` — `GatewayConfig` / `RetryConfig` (concurrency, throttle, backoff,
  sandbox allow-list, macro publish lag).
- `async_client.py` — `AsyncFMPClient`: bounded-concurrency, throttled, async FMP
  gateway with exponential-backoff-with-jitter retry that honours `Retry-After`
  and retries only transient (429/5xx/network) failures. This is the **only**
  module that touches the network.
- `endpoints.py` — pure payload → point-in-time panel parsers (income statement,
  grades-historical, earnings-surprise, economic indicators, treasury rates,
  EOD prices). Unit-tested on literal payloads.
- `resampler.py` — `PointInTimeMonthlyResampler`: month-end grid, the look-ahead-
  safe as-of joins, monthly log returns, and the forward label.
- `pipeline.py` — `MonthlyAlignmentPipeline`: fan-out fetch → parse → align into
  `[symbol, year_month, features…]`.

### Usage

```python
import asyncio
from datetime import date
from weekly_us_stock.quant.stage1 import (
    AsyncFMPClient, GatewayConfig, MonthlyAlignmentPipeline,
)

async def main():
    config = GatewayConfig.from_env()  # FMP_API_KEY, FMP_SANDBOX
    async with AsyncFMPClient(config) as client:
        pipeline = MonthlyAlignmentPipeline(client, config)
        result = await pipeline.run(["AAPL", "MSFT"], date(2020, 1, 1), date(2024, 12, 31))
        print(result.matrix.head())

asyncio.run(main())
```

Install the network extra with `pip install -e ".[quant]"`. The parsers and
resampler import without `aiohttp`; only `AsyncFMPClient` needs it.
