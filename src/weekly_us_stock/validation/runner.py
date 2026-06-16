"""Production wiring for forward validation: build a price table from a provider's
load_prices and run the (pure) evaluation over an archive directory.

Still no look-ahead: the signal is read only from the frozen archive and forward
prices are consumed strictly after each run's as_of (the pure layer enforces it).
"""
from __future__ import annotations

from collections.abc import Callable, Iterable
from datetime import date
from pathlib import Path

import pandas as pd

from weekly_us_stock.validation.forward import (
    DEFAULT_BENCHMARK,
    DEFAULT_HORIZONS,
    PriceTable,
    evaluate,
    forward_returns,
    load_archived_runs,
)

# Mirrors DataProvider.load_prices(tickers, as_of, lookback_days) -> DataFrame.
PriceLoader = Callable[[list[str], date, int], pd.DataFrame]


def build_price_table(
    tickers: Iterable[str], start: date, end: date, price_loader: PriceLoader
) -> PriceTable:
    """Fetch daily closes spanning [start, end] via a provider's load_prices and
    shape them into the {ticker: [(date, close), ...]} table the pure layer uses."""

    lookback = max((end - start).days + 5, 1)
    frame = price_loader(sorted({str(t) for t in tickers}), end, lookback)
    table: PriceTable = {}
    if frame is None or frame.empty:
        return table
    work = frame.dropna(subset=["close"]).copy()
    work["trade_date"] = pd.to_datetime(work["trade_date"]).dt.date
    for ticker, group in work.groupby("ticker"):
        series = sorted(
            (
                (bar_date, float(close))
                for bar_date, close in zip(group["trade_date"], group["close"], strict=False)
            ),
            key=lambda item: item[0],
        )
        table[str(ticker)] = series
    return table


def run_forward_validation(
    archive_dir: str | Path,
    price_loader: PriceLoader,
    *,
    benchmark: str = DEFAULT_BENCHMARK,
    horizons: dict[str, int] | None = None,
    today: date | None = None,
    out_dir: str | Path | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load the archive, fetch forward prices, and score the rankings. Returns
    (per-name long frame, cohort x horizon report)."""

    runs = load_archived_runs(Path(archive_dir))
    horizons = horizons or DEFAULT_HORIZONS
    if not runs:
        return pd.DataFrame(), pd.DataFrame()
    today = today or date.today()
    tickers: set[str] = {benchmark}
    for run in runs:
        tickers.update(str(t) for t in run.portfolio["ticker"].tolist())
    earliest = min(run.as_of for run in runs)
    prices = build_price_table(tickers, earliest, today, price_loader)
    long = forward_returns(runs, prices, horizons=horizons, benchmark=benchmark, today=today)
    report = evaluate(runs, prices, horizons=horizons, benchmark=benchmark, today=today)
    if out_dir is not None:
        write_reports(long, report, Path(out_dir))
    return long, report


def _fmt(value: object) -> str:
    return f"{value:.4f}" if isinstance(value, float) else str(value)


def _to_markdown(report: pd.DataFrame) -> str:
    header = [
        "# Forward validation (out-of-sample)",
        "",
        "Scenario weights are analyst-set, not calibrated probabilities. Read the",
        "IC / hit-rate / excess as DIRECTIONAL evidence only. Cohorts are grouped",
        "by config_fingerprint, so only same-model runs are ever compared.",
        "",
    ]
    if report.empty:
        return "\n".join([*header, "_No fully-elapsed forward windows yet._"]) + "\n"
    columns = [
        "config_fingerprint", "horizon", "n_runs", "n_names", "hit_rate",
        "mean_excess", "median_excess", "rank_ic", "top_minus_bottom",
    ]
    rows = ["| " + " | ".join(columns) + " |", "|" + "---|" * len(columns)]
    for _, row in report.iterrows():
        rows.append("| " + " | ".join(_fmt(row[column]) for column in columns) + " |")
    return "\n".join([*header, *rows]) + "\n"


def write_reports(long: pd.DataFrame, report: pd.DataFrame, out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    long_path = out_dir / "forward_returns.csv"
    report_path = out_dir / "forward_validation.csv"
    md_path = out_dir / "forward_validation.md"
    long.to_csv(long_path, index=False)
    report.to_csv(report_path, index=False)
    md_path.write_text(_to_markdown(report), encoding="utf-8")
    return [long_path, report_path, md_path]
