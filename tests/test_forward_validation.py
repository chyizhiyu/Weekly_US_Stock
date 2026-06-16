"""Offline tests for forward (out-of-sample) validation (P2-2)."""
from __future__ import annotations

import json

import pandas as pd

from weekly_us_stock.validation.forward import (
    ArchivedRun,
    evaluate,
    forward_returns,
    load_archived_runs,
)

_DATES = list(pd.bdate_range("2025-01-02", periods=300).date)


def _series(slope: float, start: float = 100.0, n: int = 300, first: float | None = None):
    series = [(_DATES[i], start + slope * i) for i in range(n)]
    if first is not None:
        series[0] = (_DATES[0], first)
    return series


def _run(fingerprint: str, names: list[tuple[str, int, float, float]]) -> ArchivedRun:
    portfolio = pd.DataFrame(
        [
            {"as_of": _DATES[0].isoformat(), "ticker": t, "rank": r,
             "robust_return": rr, "entry_price": ep}
            for (t, r, rr, ep) in names
        ]
    )
    return ArchivedRun(as_of=_DATES[0], config_fingerprint=fingerprint, portfolio=portfolio)


def test_excess_uses_frozen_entry_and_strictly_forward_prices() -> None:
    run = _run("fpA", [("AAA", 1, 0.30, 100.0)])
    # series[0]=999 (the as_of bar) must be IGNORED; the frozen entry is 100.
    prices = {"AAA": _series(1.0, first=999.0), "SPY": _series(0.5)}
    long = forward_returns([run], prices, horizons={"3m": 63}, benchmark="SPY")
    row = long[long["ticker"] == "AAA"].iloc[0]
    assert abs(row["forward_return"] - (163.0 / 100.0 - 1.0)) < 1e-9   # frozen 100, not 999
    assert abs(row["benchmark_return"] - (131.5 / 100.0 - 1.0)) < 1e-9
    assert abs(row["excess_return"] - (0.63 - 0.315)) < 1e-9


def test_immature_window_is_skipped() -> None:
    run = _run("fpA", [("AAA", 1, 0.30, 100.0)])
    prices = {"AAA": _series(1.0, n=70), "SPY": _series(0.5, n=70)}  # only ~70 sessions
    long = forward_returns([run], prices, benchmark="SPY")
    assert set(long["horizon"]) == {"1m", "3m"}   # 126/252 not elapsed -> dropped


def test_cohorts_are_not_pooled() -> None:
    runs = [
        _run("fpA", [("AAA", 1, 0.30, 100.0), ("BBB", 2, 0.10, 100.0)]),
        _run("fpB", [("CCC", 1, 0.30, 100.0), ("DDD", 2, 0.10, 100.0)]),
    ]
    prices = {
        "AAA": _series(0.4), "BBB": _series(0.1),
        "CCC": _series(0.4), "DDD": _series(0.1), "SPY": _series(0.2),
    }
    report = evaluate(runs, prices, horizons={"3m": 63}, benchmark="SPY")
    assert set(report["config_fingerprint"]) == {"fpA", "fpB"}
    assert len(report) == 2


def test_rank_ic_sign_tracks_predictiveness() -> None:
    names = [("AAA", 1, 0.30, 100.0), ("BBB", 2, 0.20, 100.0),
             ("CCC", 3, 0.10, 100.0), ("DDD", 4, 0.00, 100.0)]
    # forward-return order matches robust_return order -> IC > 0, top beats bottom
    good = evaluate(
        [_run("good", names)],
        {"AAA": _series(0.4), "BBB": _series(0.3), "CCC": _series(0.2),
         "DDD": _series(0.1), "SPY": _series(0.15)},
        horizons={"3m": 63}, benchmark="SPY",
    ).iloc[0]
    assert good["rank_ic"] > 0.9 and good["top_minus_bottom"] > 0
    # reversed mapping -> IC < 0
    bad = evaluate(
        [_run("bad", names)],
        {"AAA": _series(0.1), "BBB": _series(0.2), "CCC": _series(0.3),
         "DDD": _series(0.4), "SPY": _series(0.15)},
        horizons={"3m": 63}, benchmark="SPY",
    ).iloc[0]
    assert bad["rank_ic"] < -0.9


def test_load_archived_runs_reads_portfolio_and_fingerprint(tmp_path) -> None:
    for key, fp, as_of in [("20250103", "fpX", "2025-01-03"), ("20250110", "fpY", "2025-01-10")]:
        run_dir = tmp_path / key
        run_dir.mkdir()
        row = {"as_of": as_of, "ticker": "AAA", "rank": 1,
               "robust_return": 0.2, "entry_price": 100.0}
        pd.DataFrame([row]).to_csv(run_dir / "paper_portfolio.csv", index=False)
        (run_dir / "run_manifest.json").write_text(
            json.dumps({"as_of": as_of, "config_fingerprint": fp}), encoding="utf-8"
        )
    runs = load_archived_runs(tmp_path)
    assert len(runs) == 2
    assert {r.config_fingerprint for r in runs} == {"fpX", "fpY"}
