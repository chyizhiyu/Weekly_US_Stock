"""Stage 1 orchestrator: fetch -> parse -> align into the monthly matrix.

``MonthlyAlignmentPipeline`` fans every endpoint out concurrently through the
async client, runs the pure parsers, then hands the panels to the point-in-time
resampler. The fetch layer is injected (any object exposing an async
``get(path, params)`` works), so the whole pipeline runs in tests against a
canned, in-memory client with no sockets.
"""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date
from typing import Any, Protocol

import pandas as pd

from weekly_us_stock.quant.stage1 import endpoints
from weekly_us_stock.quant.stage1.config import GatewayConfig
from weekly_us_stock.quant.stage1.resampler import PointInTimeMonthlyResampler, add_forward_label

logger = logging.getLogger(__name__)

# Macro series pulled once per run (symbol-less, broadcast across the universe).
_ECONOMIC_INDICATORS = ("GDP", "CPI", "unemploymentRate")


class SupportsGet(Protocol):
    """Minimal async fetch contract the pipeline depends on."""

    async def get(self, path: str, params: dict[str, Any], *, raw: bool = False) -> Any: ...


@dataclass(frozen=True)
class AlignmentResult:
    """Aligned matrix plus provenance for auditing a run."""

    matrix: pd.DataFrame
    symbols: list[str]
    start: date
    end: date
    sources: list[str]

    @property
    def feature_names(self) -> list[str]:
        reserved = {"symbol", "year_month", "rebalance_date"}
        return [c for c in self.matrix.columns if c not in reserved]


class MonthlyAlignmentPipeline:
    def __init__(self, client: SupportsGet, config: GatewayConfig) -> None:
        self.client = client
        self.config = config

    # -- per-symbol fetch+parse ----------------------------------------------

    async def _fetch_symbol(
        self, symbol: str
    ) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Concurrently pull the four per-symbol endpoints and parse them."""

        self.config.assert_symbol_allowed(symbol)
        limit = self.config.effective_history_limit
        income_p, grades_p, surprise_p, eod_p = await asyncio.gather(
            self.client.get(
                "income-statement",
                {"symbol": symbol, "period": "quarter", "limit": limit},
            ),
            self.client.get("grades-historical", {"symbol": symbol, "limit": limit}),
            self.client.get("earnings-surprises", {"symbol": symbol, "limit": limit}),
            self.client.get("historical-price-eod/full", {"symbol": symbol}),
        )
        return (
            endpoints.parse_income_statement(income_p or [], symbol=symbol),
            endpoints.parse_grades_historical(grades_p or [], symbol=symbol),
            endpoints.parse_earnings_surprise(surprise_p or [], symbol=symbol),
            endpoints.parse_eod_prices(eod_p or [], symbol=symbol),
        )

    async def _fetch_macro(self) -> dict[str, pd.DataFrame]:
        """Pull treasury rates and the economic indicators (symbol-less)."""

        lag = self.config.macro_publish_lag_days
        treasury_task = self.client.get("treasury-rates", {})
        indicator_tasks = [
            self.client.get("economic-indicators", {"name": name})
            for name in _ECONOMIC_INDICATORS
        ]
        treasury_p, *indicator_payloads = await asyncio.gather(treasury_task, *indicator_tasks)
        macro: dict[str, pd.DataFrame] = {
            "treasury": endpoints.parse_treasury_rates(treasury_p or [])
        }
        for name, payload in zip(_ECONOMIC_INDICATORS, indicator_payloads, strict=True):
            macro[f"macro_{name}"] = endpoints.parse_economic_indicator(
                payload or [], name=name, publish_lag_days=lag
            )
        return macro

    # -- public entry points --------------------------------------------------

    async def run(
        self,
        symbols: Sequence[str],
        start: date,
        end: date,
        *,
        with_label: bool = True,
    ) -> AlignmentResult:
        """Build the aligned monthly matrix for ``symbols`` over ``[start, end]``."""

        symbols = [s.strip().upper() for s in symbols if s and s.strip()]
        if not symbols:
            raise ValueError("at least one symbol is required")

        per_symbol = await asyncio.gather(*(self._fetch_symbol(s) for s in symbols))
        macro = await self._fetch_macro()

        income = _concat([r[0] for r in per_symbol])
        grades = _concat([r[1] for r in per_symbol])
        surprise = _concat([r[2] for r in per_symbol])
        prices = _concat([r[3] for r in per_symbol])

        if prices.empty:
            raise ValueError("no price history returned; cannot build a monthly matrix")

        resampler = PointInTimeMonthlyResampler(start, end)
        matrix = resampler.build(
            prices=prices,
            cross_sectional={
                "fundamentals": income,
                "grades": grades,
                "surprise": surprise,
            },
            macro={name: panel for name, panel in macro.items() if not panel.empty},
        )
        if with_label:
            matrix = add_forward_label(matrix, horizon=1)

        sources = sorted(
            {
                *(_sources(income)),
                *(_sources(grades)),
                *(_sources(surprise)),
                *(_sources(prices)),
                *{s for panel in macro.values() for s in _sources(panel)},
            }
        )
        return AlignmentResult(
            matrix=matrix, symbols=symbols, start=start, end=end, sources=sources
        )

    def run_sync(
        self,
        symbols: Sequence[str],
        start: date,
        end: date,
        *,
        with_label: bool = True,
    ) -> AlignmentResult:
        """Blocking wrapper around :meth:`run` for scripts/CLIs."""

        return asyncio.run(self.run(symbols, start, end, with_label=with_label))


def _concat(frames: list[pd.DataFrame]) -> pd.DataFrame:
    non_empty = [f for f in frames if f is not None and not f.empty]
    return pd.concat(non_empty, ignore_index=True) if non_empty else pd.DataFrame()


def _sources(frame: pd.DataFrame) -> set[str]:
    if frame is None or frame.empty or "source" not in frame.columns:
        return set()
    return set(frame["source"].dropna().unique())
