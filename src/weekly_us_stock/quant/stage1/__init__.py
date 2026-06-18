"""Stage 1 - FMP dual-track timestamp alignment gateway + monthly resampler.

Public surface::

    from weekly_us_stock.quant.stage1 import (
        GatewayConfig,
        AsyncFMPClient,
        MonthlyAlignmentPipeline,
        PointInTimeMonthlyResampler,
    )

The :class:`AsyncFMPClient` is the only component that touches the network;
everything else (parsers in :mod:`endpoints`, alignment in :mod:`resampler`) is
pure and exercised offline. See :mod:`weekly_us_stock.quant` for the six-stage
roadmap this slots into.
"""

from __future__ import annotations

from weekly_us_stock.quant.stage1.async_client import (
    AsyncFMPClient,
    FMPHTTPError,
    TransientHTTPError,
    compute_backoff,
)
from weekly_us_stock.quant.stage1.config import GatewayConfig, RetryConfig
from weekly_us_stock.quant.stage1.pipeline import AlignmentResult, MonthlyAlignmentPipeline
from weekly_us_stock.quant.stage1.records import LookAheadError
from weekly_us_stock.quant.stage1.resampler import (
    PointInTimeMonthlyResampler,
    add_forward_label,
    month_end_grid,
    month_end_trading_day,
)

__all__ = [
    "AlignmentResult",
    "AsyncFMPClient",
    "FMPHTTPError",
    "GatewayConfig",
    "LookAheadError",
    "MonthlyAlignmentPipeline",
    "PointInTimeMonthlyResampler",
    "RetryConfig",
    "TransientHTTPError",
    "add_forward_label",
    "compute_backoff",
    "month_end_grid",
    "month_end_trading_day",
]
