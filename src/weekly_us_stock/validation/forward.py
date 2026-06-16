"""Forward (out-of-sample) validation of the weekly rankings (P2-2).

Consumes the point-in-time archive (paper_portfolio.csv + run_manifest.json under
each runs/YYYYMMDD/) and measures how the FROZEN entry decisions actually played
out. No look-ahead: the signal is read only from the frozen archive, forward
prices are taken strictly after each run's as_of, windows that have not fully
elapsed are skipped, and runs are cohorted by config_fingerprint so different
model versions are never pooled together. No network here - prices are injected.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import pandas as pd

# Forward windows in trading sessions (~1m / 3m / 6m / 12m).
DEFAULT_HORIZONS: dict[str, int] = {"1m": 21, "3m": 63, "6m": 126, "12m": 252}
DEFAULT_BENCHMARK = "SPY"

PriceSeries = list[tuple[date, float]]  # ascending by date
PriceTable = dict[str, PriceSeries]


@dataclass(slots=True)
class ArchivedRun:
    as_of: date
    config_fingerprint: str
    portfolio: pd.DataFrame  # paper_portfolio rows: ticker, rank, entry_price, robust_return, ...


def load_archived_runs(history_dir: Path) -> list[ArchivedRun]:
    """Read every archived run dir holding paper_portfolio.csv + run_manifest.json."""

    runs: list[ArchivedRun] = []
    if not history_dir.exists():
        return runs
    for run_dir in sorted(p for p in history_dir.iterdir() if p.is_dir()):
        portfolio_path = run_dir / "paper_portfolio.csv"
        manifest_path = run_dir / "run_manifest.json"
        if not portfolio_path.exists() or not manifest_path.exists():
            continue
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        portfolio = pd.read_csv(portfolio_path)
        if portfolio.empty:
            continue
        as_of_raw = manifest.get("as_of") or str(portfolio["as_of"].iloc[0])
        runs.append(
            ArchivedRun(
                as_of=date.fromisoformat(str(as_of_raw)[:10]),
                config_fingerprint=str(manifest.get("config_fingerprint") or ""),
                portfolio=portfolio,
            )
        )
    return runs


def _entry_index(series: PriceSeries, entry_date: date) -> int | None:
    for index, (bar_date, _close) in enumerate(series):
        if bar_date >= entry_date:
            return index
    return None


def _exit_bar(series: PriceSeries, entry_date: date, sessions: int) -> tuple[date, float] | None:
    """The bar `sessions` trading days at/after entry_date, or None when the series
    does not extend that far (i.e. the window has not elapsed)."""

    index = _entry_index(series, entry_date)
    if index is None:
        return None
    exit_index = index + sessions
    if exit_index >= len(series):
        return None
    return series[exit_index]


def forward_returns(
    runs: list[ArchivedRun],
    prices: PriceTable,
    *,
    horizons: dict[str, int] | None = None,
    benchmark: str = DEFAULT_BENCHMARK,
    today: date | None = None,
) -> pd.DataFrame:
    """Long frame of per (run, horizon, name) forward & excess returns, ONLY for
    windows that have fully elapsed. Entry prices come from the frozen archive;
    forward prices are looked up strictly after as_of."""

    horizons = horizons or DEFAULT_HORIZONS
    bench_series = prices.get(benchmark, [])
    rows: list[dict] = []
    for run in runs:
        bench_entry_index = _entry_index(bench_series, run.as_of)
        for label, sessions in horizons.items():
            bench_exit = _exit_bar(bench_series, run.as_of, sessions)
            if bench_exit is None or bench_entry_index is None:
                continue  # benchmark window not elapsed -> immature, skip
            exit_date, bench_exit_close = bench_exit
            if today is not None and exit_date > today:
                continue
            bench_entry_close = bench_series[bench_entry_index][1]
            if bench_entry_close <= 0:
                continue
            bench_ret = bench_exit_close / bench_entry_close - 1.0
            for _, holding in run.portfolio.iterrows():
                entry_price = holding.get("entry_price")
                if entry_price is None or float(entry_price) <= 0:
                    continue
                ticker = str(holding.get("ticker"))
                name_exit = _exit_bar(prices.get(ticker, []), run.as_of, sessions)
                if name_exit is None:
                    continue  # short/delisted series at this horizon (survivorship: v1 note)
                fwd_ret = name_exit[1] / float(entry_price) - 1.0
                rows.append(
                    {
                        "config_fingerprint": run.config_fingerprint,
                        "as_of": run.as_of.isoformat(),
                        "horizon": label,
                        "sessions": sessions,
                        "ticker": ticker,
                        "rank": holding.get("rank"),
                        "robust_return": holding.get("robust_return"),
                        "forward_return": fwd_ret,
                        "benchmark_return": bench_ret,
                        "excess_return": fwd_ret - bench_ret,
                    }
                )
    return pd.DataFrame(rows)


def _spearman(left: pd.Series, right: pd.Series) -> float:
    if len(left) < 3 or left.nunique() < 2 or right.nunique() < 2:
        return float("nan")
    return float(left.rank().corr(right.rank()))


def _top_minus_bottom(group: pd.DataFrame, fraction: float = 1.0 / 3.0) -> float:
    if len(group) < 2:
        return float("nan")
    ordered = group.sort_values("rank")  # rank 1 = best
    take = max(1, int(len(ordered) * fraction))
    top = ordered.head(take)["forward_return"].mean()
    bottom = ordered.tail(take)["forward_return"].mean()
    return float(top - bottom)


def evaluate(
    runs: list[ArchivedRun],
    prices: PriceTable,
    *,
    horizons: dict[str, int] | None = None,
    benchmark: str = DEFAULT_BENCHMARK,
    today: date | None = None,
) -> pd.DataFrame:
    """Cohort (config_fingerprint) x horizon scorecard: hit rate, mean/median
    excess, Spearman rank IC (robust_return vs realized forward return) and the
    top-minus-bottom forward-return spread. Cohorts are never pooled."""

    columns = [
        "config_fingerprint", "horizon", "n_names", "n_runs", "hit_rate",
        "mean_excess", "median_excess", "rank_ic", "top_minus_bottom",
    ]
    long = forward_returns(runs, prices, horizons=horizons, benchmark=benchmark, today=today)
    if long.empty:
        return pd.DataFrame(columns=columns)
    summaries: list[dict] = []
    for (fingerprint, horizon), group in long.groupby(["config_fingerprint", "horizon"]):
        summaries.append(
            {
                "config_fingerprint": fingerprint,
                "horizon": horizon,
                "n_names": int(len(group)),
                "n_runs": int(group["as_of"].nunique()),
                "hit_rate": float((group["excess_return"] > 0).mean()),
                "mean_excess": float(group["excess_return"].mean()),
                "median_excess": float(group["excess_return"].median()),
                "rank_ic": _spearman(group["robust_return"], group["forward_return"]),
                "top_minus_bottom": _top_minus_bottom(group),
            }
        )
    return pd.DataFrame(summaries, columns=columns)
