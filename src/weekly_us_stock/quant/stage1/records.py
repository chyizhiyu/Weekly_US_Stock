"""Dual-track timestamp data model for the point-in-time gateway.

Every observation that enters the monthly resampler carries **two** timestamps,
and the whole no-look-ahead guarantee rests on never confusing them:

- ``event_time``      - when the fact economically *happened* (fiscal period
                        end, the quarter an EPS number belongs to, the month a
                        GDP print measures). Used only for labelling/joining.
- ``disclosure_time`` - when the fact first became *publicly usable* (the SEC
                        ``acceptedDate``, an analyst grade's publish ``date``,
                        an economic release's announcement ``date``). This is
                        the ONLY timestamp the alignment gateway is allowed to
                        compare against a rebalance date ``T``.

A "point-in-time panel" is just a tidy :class:`pandas.DataFrame` that carries at
least ``[symbol, disclosure_time]`` plus one or more feature columns. Macro
panels are symbol-less (a single cross-sectional series broadcast to every
name), so ``symbol`` is optional and validated per call site.

Keeping these as plain column constants (rather than a bespoke class) means the
panels flow straight into pandas' ``merge_asof`` machinery in
:mod:`weekly_us_stock.quant.stage1.resampler` with zero copying.
"""

from __future__ import annotations

from collections.abc import Sequence

import pandas as pd

# -- Canonical column names ---------------------------------------------------

SYMBOL = "symbol"
EVENT_TIME = "event_time"
DISCLOSURE_TIME = "disclosure_time"
SOURCE = "source"

#: Columns every point-in-time panel must carry (besides its feature columns).
PIT_INDEX_COLUMNS = [SYMBOL, EVENT_TIME, DISCLOSURE_TIME, SOURCE]

#: The output of Stage 1: one row per (symbol, month-end rebalance date).
SYMBOL_COL = SYMBOL
PERIOD_COL = "year_month"  # e.g. "2024-01", the calendar month of the rebalance


class LookAheadError(AssertionError):
    """Raised when an observation with ``disclosure_time`` strictly after the
    rebalance date ``T`` reaches the aligned matrix. This is a hard, unrecoverable
    invariant violation: a backtest that trips it is silently using the future.
    """


def require_pit_columns(
    frame: pd.DataFrame,
    *,
    dataset: str,
    symbol_required: bool = True,
) -> pd.DataFrame:
    """Validate that ``frame`` is a well-formed point-in-time panel.

    Enforces presence and dtype of the disclosure timestamp (the load-bearing
    column) and, for cross-sectional panels, the symbol key. Returns the frame
    with ``disclosure_time``/``event_time`` coerced to tz-naive datetimes so the
    downstream ``merge_asof`` never trips on mixed dtypes.
    """

    required: list[str] = [DISCLOSURE_TIME]
    if symbol_required:
        required = [SYMBOL, *required]
    missing = [column for column in required if column not in frame.columns]
    if missing:
        raise ValueError(f"{dataset} panel is missing point-in-time columns: {missing}")

    out = frame.copy()
    # Pin nanosecond resolution: pandas refuses an as-of merge across mixed
    # datetime64 resolutions (e.g. [s] grid vs [us] payload), so normalise here.
    out[DISCLOSURE_TIME] = pd.to_datetime(out[DISCLOSURE_TIME], errors="coerce").astype(
        "datetime64[ns]"
    )
    if out[DISCLOSURE_TIME].isna().any():
        bad = int(out[DISCLOSURE_TIME].isna().sum())
        raise ValueError(
            f"{dataset} panel has {bad} row(s) with an unparseable disclosure_time; "
            "an observation with no disclosure time cannot be aligned without "
            "risking look-ahead and must be dropped at the source."
        )
    if EVENT_TIME in out.columns:
        out[EVENT_TIME] = pd.to_datetime(out[EVENT_TIME], errors="coerce").astype(
            "datetime64[ns]"
        )
    if symbol_required:
        out[SYMBOL] = out[SYMBOL].astype("string").str.strip().str.upper()
    return out


def feature_columns(frame: pd.DataFrame, *, exclude: Sequence[str] = ()) -> list[str]:
    """Feature columns of a panel: everything that is not bookkeeping."""

    reserved = {*PIT_INDEX_COLUMNS, *exclude}
    return [column for column in frame.columns if column not in reserved]
