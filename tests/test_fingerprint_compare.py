"""P0-3: universe/config fingerprints gate week-over-week comparison."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from weekly_us_stock.config import load_settings
from weekly_us_stock.reports.compare import compare_with_previous
from weekly_us_stock.utils.fingerprint import (
    config_fingerprint,
    stable_hash,
    ticker_set_hash,
    universe_fingerprint,
)


def test_stable_hash_is_order_independent_and_normalized() -> None:
    assert stable_hash({"a": 1, "b": 2}) == stable_hash({"b": 2, "a": 1})
    assert ticker_set_hash(["AAPL", "MSFT"]) == ticker_set_hash(["MSFT", "AAPL"])
    assert ticker_set_hash(["BRK.B"]) == ticker_set_hash(["BRK-B"])  # normalized match


def test_universe_fingerprint_tracks_membership() -> None:
    a, b = load_settings(), load_settings()
    assert universe_fingerprint(a) == universe_fingerprint(b)
    b.universe.index_membership = []  # full market: a different pool definition
    assert universe_fingerprint(a) != universe_fingerprint(b)


def test_config_fingerprint_ignores_paths_tracks_model() -> None:
    a, b = load_settings(), load_settings()
    assert config_fingerprint(a) == config_fingerprint(b)
    b.app.output_dir = "/tmp/elsewhere"  # path/display knob: must NOT matter
    assert config_fingerprint(a) == config_fingerprint(b)
    b.risk_preferences.hurdle_rate = 0.20  # scoring knob: must matter
    assert config_fingerprint(a) != config_fingerprint(b)


def _write_previous(tmp_path: Path, uf: str | None, cf: str | None) -> Path:
    run_dir = tmp_path / "20251231"
    run_dir.mkdir()
    pd.DataFrame({"rank": [1, 2], "ticker": ["AAA", "BBB"]}).to_csv(
        run_dir / "robust_ranking.csv", index=False
    )
    pd.DataFrame({"rank": [1, 2], "ticker": ["AAA", "CCC"]}).to_csv(
        run_dir / "upside_ranking.csv", index=False
    )
    meta: dict = {"as_of": "2025-12-31"}
    if uf is not None:
        meta["universe_fingerprint"] = uf
    if cf is not None:
        meta["config_fingerprint"] = cf
    (run_dir / "run_metadata.json").write_text(json.dumps(meta), encoding="utf-8")
    return run_dir


def _current_rankings() -> tuple[pd.DataFrame, pd.DataFrame]:
    robust = pd.DataFrame({"rank": [1, 2], "ticker": ["AAA", "ZZZ"]})  # BBB->out, ZZZ->in
    upside = pd.DataFrame({"rank": [1, 2], "ticker": ["AAA", "CCC"]})
    return robust, upside


def test_matching_fingerprints_compare_normally(tmp_path: Path) -> None:
    previous = _write_previous(tmp_path, "U1", "C1")
    robust, upside = _current_rankings()
    result = compare_with_previous(
        robust, upside, previous, 20,
        current_universe_fingerprint="U1", current_config_fingerprint="C1",
    )
    assert result.comparable and not result.baseline_reset
    assert result.robust_entered == ["ZZZ"]
    assert result.robust_exited == ["BBB"]


def test_universe_change_resets_baseline(tmp_path: Path) -> None:
    previous = _write_previous(tmp_path, "U_OLD", "C1")
    robust, upside = _current_rankings()
    result = compare_with_previous(
        robust, upside, previous, 20,
        current_universe_fingerprint="U_NEW", current_config_fingerprint="C1",
    )
    assert result.baseline_reset and "universe" in (result.reset_reason or "")
    assert result.robust_entered == [] and result.robust_exited == []


def test_missing_previous_fingerprint_resets_baseline(tmp_path: Path) -> None:
    previous = _write_previous(tmp_path, None, None)  # legacy run, no fingerprints
    robust, upside = _current_rankings()
    result = compare_with_previous(
        robust, upside, previous, 20,
        current_universe_fingerprint="U1", current_config_fingerprint="C1",
    )
    assert result.baseline_reset
