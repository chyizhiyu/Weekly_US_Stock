"""Point-in-time monthly resampler: the no-look-ahead alignment gateway.

Given a set of point-in-time panels (from :mod:`endpoints`) and a monthly
rebalance grid of month-end trading days, this builds the aligned feature matrix
``[symbol, year_month, features...]`` under one ironclad rule:

    At a rebalance date ``T``, a feature may only use the latest observation
    whose ``disclosure_time <= T``.

That "latest value at or before T" is exactly a backward as-of join, so the core
is :func:`pandas.merge_asof` with ``direction="backward"``. Forward-fill of
sparse, irregular releases (quarterly fundamentals, event-driven grades, lagged
macro) falls out for free: between two disclosures the most recent one is
carried forward; before the first disclosure the feature is simply null.

Every merge keeps the *disclosure timestamp it actually used* in a hidden
``__asof_*`` audit column, and :meth:`PointInTimeMonthlyResampler.build`
asserts none exceeds ``T``. A backtest that trips :class:`LookAheadError` is, by
construction, peeking at the future - so we make that loud rather than silent.
"""

from __future__ import annotations

import calendar as _calendar
from datetime import date

import numpy as np
import pandas as pd

from weekly_us_stock.quant.stage1.records import (
    DISCLOSURE_TIME,
    PERIOD_COL,
    SYMBOL,
    LookAheadError,
    feature_columns,
    require_pit_columns,
)
from weekly_us_stock.utils.calendar import is_trading_day, previous_trading_day

REBALANCE_COL = "rebalance_date"  # the month-end trading day T (a Timestamp)


def month_end_trading_day(year: int, month: int) -> date:
    """Last NYSE trading day on or before the final calendar day of the month."""

    last_day = _calendar.monthrange(year, month)[1]
    candidate = date(year, month, last_day)
    while not is_trading_day(candidate):
        candidate = previous_trading_day(candidate)
    return candidate


def month_end_grid(start: date, end: date) -> pd.DataFrame:
    """Month-end trading days spanning ``[start, end]`` inclusive by month.

    Returns a frame with ``year_month`` (``YYYY-MM``) and ``rebalance_date``
    (a tz-naive Timestamp at the month-end trading day). Both endpoints'
    *months* are included regardless of day-of-month.
    """

    if start > end:
        raise ValueError(f"start {start} is after end {end}")
    rows: list[dict[str, object]] = []
    year, month = start.year, start.month
    while (year, month) <= (end.year, end.month):
        t = month_end_trading_day(year, month)
        rows.append(
            {
                PERIOD_COL: f"{year:04d}-{month:02d}",
                # nanosecond resolution to match the panels' disclosure_time
                REBALANCE_COL: pd.Timestamp(t).as_unit("ns"),
            }
        )
        month += 1
        if month > 12:
            year, month = year + 1, 1
    return pd.DataFrame(rows, columns=[PERIOD_COL, REBALANCE_COL])


def _asof_join_cross_sectional(
    grid: pd.DataFrame,
    panel: pd.DataFrame,
    *,
    dataset: str,
) -> pd.DataFrame:
    """Per-symbol backward as-of join of one cross-sectional panel onto the grid.

    The grid is broadcast to every symbol present in ``panel``; each
    (symbol, T) row receives the latest observation with
    ``disclosure_time <= T``. Returns long form: one row per (symbol, T).
    """

    panel = require_pit_columns(panel, dataset=dataset, symbol_required=True)
    features = feature_columns(panel)
    panel = panel.sort_values(DISCLOSURE_TIME)
    audit = f"__asof_{dataset}"
    panel = panel.assign(**{audit: panel[DISCLOSURE_TIME]})

    symbols = panel[SYMBOL].dropna().unique()
    grid_keyed = grid.assign(_one=1)
    broadcast = (
        pd.DataFrame({SYMBOL: symbols, "_one": 1})
        .merge(grid_keyed, on="_one")
        .drop(columns="_one")
        .sort_values(REBALANCE_COL)
    )

    merged = pd.merge_asof(
        broadcast,
        panel[[SYMBOL, DISCLOSURE_TIME, audit, *features]].sort_values(DISCLOSURE_TIME),
        left_on=REBALANCE_COL,
        right_on=DISCLOSURE_TIME,
        by=SYMBOL,
        direction="backward",
    )
    return merged.drop(columns=[DISCLOSURE_TIME])


def _asof_join_macro(
    grid: pd.DataFrame,
    panel: pd.DataFrame,
    *,
    dataset: str,
) -> pd.DataFrame:
    """Backward as-of join of a symbol-less macro panel onto the bare grid.

    Produces one row per rebalance date with the macro features; the caller
    broadcasts these across symbols.
    """

    panel = require_pit_columns(panel, dataset=dataset, symbol_required=False)
    features = feature_columns(panel)
    audit = f"__asof_{dataset}"
    panel = panel.sort_values(DISCLOSURE_TIME).assign(**{audit: lambda d: d[DISCLOSURE_TIME]})

    merged = pd.merge_asof(
        grid.sort_values(REBALANCE_COL),
        panel[[DISCLOSURE_TIME, audit, *features]],
        left_on=REBALANCE_COL,
        right_on=DISCLOSURE_TIME,
        direction="backward",
    )
    return merged.drop(columns=[DISCLOSURE_TIME])


def monthly_price_features(grid: pd.DataFrame, prices: pd.DataFrame) -> pd.DataFrame:
    """Month-end close + monthly log return per (symbol, T).

    The month-end close is the last close with ``trade_date <= T`` (a backward
    as-of join, identical look-ahead discipline). The monthly log return is
    ``ln(close_T / close_{T-1})`` over consecutive rebalance dates.
    """

    prices = require_pit_columns(prices, dataset="prices", symbol_required=True)
    prices = prices.dropna(subset=["close"]).sort_values(DISCLOSURE_TIME)
    audit = "__asof_prices"
    prices = prices.assign(**{audit: prices[DISCLOSURE_TIME]})

    symbols = prices[SYMBOL].dropna().unique()
    broadcast = (
        pd.DataFrame({SYMBOL: symbols, "_one": 1})
        .merge(grid.assign(_one=1), on="_one")
        .drop(columns="_one")
        .sort_values(REBALANCE_COL)
    )
    merged = pd.merge_asof(
        broadcast,
        prices[[SYMBOL, DISCLOSURE_TIME, audit, "close"]].sort_values(DISCLOSURE_TIME),
        left_on=REBALANCE_COL,
        right_on=DISCLOSURE_TIME,
        by=SYMBOL,
        direction="backward",
    ).drop(columns=[DISCLOSURE_TIME])
    merged = merged.rename(columns={"close": "month_end_close"})
    merged = merged.sort_values([SYMBOL, REBALANCE_COL])
    prev_close = merged.groupby(SYMBOL, observed=True)["month_end_close"].shift(1)
    ratio = merged["month_end_close"] / prev_close
    merged["log_return_1m"] = np.log(ratio.where(ratio > 0))
    return merged


class PointInTimeMonthlyResampler:
    """Assemble the aligned monthly feature matrix from point-in-time panels.

    Parameters
    ----------
    start, end:
        Inclusive month range (any day within the boundary months works).
    """

    def __init__(self, start: date, end: date) -> None:
        self.grid = month_end_grid(start, end)

    def build(
        self,
        *,
        prices: pd.DataFrame,
        cross_sectional: dict[str, pd.DataFrame] | None = None,
        macro: dict[str, pd.DataFrame] | None = None,
    ) -> pd.DataFrame:
        """Return ``[symbol, year_month, rebalance_date, features...]``.

        ``cross_sectional`` and ``macro`` map a dataset name (used for the audit
        column and feature provenance) to its point-in-time panel.
        """

        cross_sectional = cross_sectional or {}
        macro = macro or {}

        base = monthly_price_features(self.grid, prices)
        audit_columns = ["__asof_prices"]

        for name, panel in cross_sectional.items():
            if panel is None or panel.empty:
                continue
            joined = _asof_join_cross_sectional(self.grid, panel, dataset=name)
            audit = f"__asof_{name}"
            audit_columns.append(audit)
            base = base.merge(
                joined.drop(columns=[PERIOD_COL]),
                on=[SYMBOL, REBALANCE_COL],
                how="left",
            )

        macro_frame = self.grid.copy()
        for name, panel in macro.items():
            if panel is None or panel.empty:
                continue
            joined = _asof_join_macro(self.grid, panel, dataset=name)
            audit_columns.append(f"__asof_{name}")
            macro_frame = macro_frame.merge(
                joined.drop(columns=[PERIOD_COL]), on=REBALANCE_COL, how="left"
            )
        if macro:
            base = base.merge(
                macro_frame.drop(columns=[PERIOD_COL]), on=REBALANCE_COL, how="left"
            )

        self._assert_no_lookahead(base, audit_columns)
        base = base.drop(columns=[c for c in audit_columns if c in base.columns])

        ordered = [SYMBOL, PERIOD_COL, REBALANCE_COL]
        features = [c for c in base.columns if c not in ordered]
        return base[[*ordered, *features]].sort_values([SYMBOL, REBALANCE_COL]).reset_index(
            drop=True
        )

    @staticmethod
    def _assert_no_lookahead(frame: pd.DataFrame, audit_columns: list[str]) -> None:
        """Hard invariant: no used disclosure timestamp may exceed its T."""

        for audit in audit_columns:
            if audit not in frame.columns:
                continue
            used = pd.to_datetime(frame[audit])
            leaked = used > frame[REBALANCE_COL]
            if bool(leaked.any()):
                offenders = frame.loc[leaked, [SYMBOL, REBALANCE_COL, audit]].head()
                raise LookAheadError(
                    f"{audit}: {int(leaked.sum())} row(s) use a disclosure time after "
                    f"their rebalance date. First offenders:\n{offenders}"
                )


def add_forward_label(matrix: pd.DataFrame, *, horizon: int = 1) -> pd.DataFrame:
    """Attach the realised next-period return label ``fwd_log_return_{h}m``.

    The label at month ``T`` is the log return realised between ``T`` and
    ``T+horizon`` - strictly future and never an input feature. It is the
    supervised target Stages 5/6 predict and must be dropped from any feature
    set fed to the model.
    """

    if "log_return_1m" not in matrix.columns:
        raise ValueError("matrix must contain 'log_return_1m' to derive a forward label")
    out = matrix.sort_values([SYMBOL, REBALANCE_COL]).copy()
    label = f"fwd_log_return_{horizon}m"
    out[label] = out.groupby(SYMBOL, observed=True)["log_return_1m"].shift(-horizon)
    return out
