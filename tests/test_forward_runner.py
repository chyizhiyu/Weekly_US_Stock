"""Offline tests for the forward-validation runner (price table + orchestration)."""
from __future__ import annotations

import json

import pandas as pd
from typer.testing import CliRunner

from weekly_us_stock.cli import app
from weekly_us_stock.validation.runner import build_price_table, run_forward_validation

_DATES = list(pd.bdate_range("2025-01-02", periods=300).date)
_CLI = CliRunner()


def _loader(table: dict):
    def loader(tickers, as_of, lookback_days):
        rows = [
            {"ticker": t, "trade_date": d.isoformat(), "close": c}
            for t in tickers
            for (d, c) in table.get(t, [])
        ]
        return pd.DataFrame(rows)

    return loader


def test_build_price_table_groups_and_sorts() -> None:
    table = {"AAA": [(_DATES[2], 102.0), (_DATES[0], 100.0)], "SPY": [(_DATES[0], 50.0)]}
    out = build_price_table(["AAA", "SPY"], _DATES[0], _DATES[10], _loader(table))
    assert out["AAA"][0] == (_DATES[0], 100.0)   # sorted ascending
    assert out["AAA"][-1] == (_DATES[2], 102.0)
    assert out["SPY"] == [(_DATES[0], 50.0)]


def test_run_forward_validation_end_to_end(tmp_path) -> None:
    history = tmp_path / "history" / "20250102"
    history.mkdir(parents=True)
    pd.DataFrame(
        [{"as_of": _DATES[0].isoformat(), "ticker": "AAA", "rank": 1,
          "robust_return": 0.3, "entry_price": 100.0}]
    ).to_csv(history / "paper_portfolio.csv", index=False)
    (history / "run_manifest.json").write_text(
        json.dumps({"as_of": _DATES[0].isoformat(), "config_fingerprint": "fp1"}), encoding="utf-8"
    )
    table = {
        "AAA": [(_DATES[i], 100.0 + i) for i in range(300)],        # +63% at session 63
        "SPY": [(_DATES[i], 100.0 + 0.5 * i) for i in range(300)],  # +31.5% at session 63
    }
    out_dir = tmp_path / "out"
    _long, report = run_forward_validation(
        tmp_path / "history", _loader(table),
        benchmark="SPY", horizons={"3m": 63}, today=_DATES[299], out_dir=out_dir,
    )
    assert not report.empty
    row = report.iloc[0]
    assert row["config_fingerprint"] == "fp1" and row["horizon"] == "3m"
    assert abs(row["hit_rate"] - 1.0) < 1e-9   # AAA beat SPY -> 100% hit
    assert (out_dir / "forward_validation.csv").exists()
    assert (out_dir / "forward_validation.md").exists()
    assert (out_dir / "forward_returns.csv").exists()


def test_no_archive_returns_empty(tmp_path) -> None:
    long, report = run_forward_validation(tmp_path / "missing", _loader({}))
    assert long.empty and report.empty


def test_forward_validate_rejects_unknown_provider(tmp_path) -> None:
    result = _CLI.invoke(
        app, ["forward-validate", "--archive", str(tmp_path), "--provider", "typo"]
    )
    assert result.exit_code == 78
    assert "Unsupported data source: typo" in result.output
