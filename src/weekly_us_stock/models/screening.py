from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any

import pandas as pd
from pydantic import BaseModel, Field


class PipelineRequest(BaseModel):
    as_of: date
    provider: str | None = None
    strict_freshness: bool = False
    previous_dir: str | None = None


class StepSummary(BaseModel):
    name: str
    input_count: int
    output_count: int
    elapsed_seconds: float
    rejection_counts: dict[str, int] = Field(default_factory=dict)
    notes: list[str] = Field(default_factory=list)
    artifacts: list[str] = Field(default_factory=list)


class DataFreshness(BaseModel):
    expected_as_of: str
    fresh_price_coverage: float
    stale_tickers: int
    degraded_sources: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)

    @property
    def is_fresh(self) -> bool:
        return self.stale_tickers == 0


class PipelineResult(BaseModel):
    request: PipelineRequest
    robust_top: list[dict[str, Any]]
    upside_top: list[dict[str, Any]]
    watchlist: list[dict[str, Any]]
    steps: list[StepSummary]
    freshness: DataFreshness
    artifacts: list[str] = Field(default_factory=list)


class DataNotReadyError(RuntimeError):
    """Raised under --strict-freshness when source data has not caught up yet."""


@dataclass(slots=True)
class FilterFrameResult:
    candidates: pd.DataFrame
    rejected: pd.DataFrame = field(default_factory=pd.DataFrame)
    rejection_counts: dict[str, int] = field(default_factory=dict)
