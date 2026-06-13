"""P2-2: forward paper-portfolio snapshot + self-describing run manifest."""

from __future__ import annotations

from datetime import date

import pandas as pd

from weekly_us_stock.reports.archive import (
    CALIBRATION_NOTE,
    build_paper_portfolio,
    build_run_manifest,
)

AS_OF = date(2026, 1, 9)


def _eligible() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"rank": 1, "ticker": "AAA", "price": 50.0, "robust_return": 0.06,
             "expected_irr": 0.20, "median_irr": 0.18, "p10_irr": 0.05, "p90_irr": 0.40,
             "business_quality": 0.8, "evidence_confidence": 0.9},
        ]
    )


def test_paper_portfolio_freezes_entry_price_with_only_pit_data() -> None:
    portfolio = build_paper_portfolio(_eligible(), AS_OF)
    row = portfolio.iloc[0]
    assert row["as_of"] == "2026-01-09"
    assert row["ticker"] == "AAA"
    assert row["entry_price"] == 50.0  # frozen entry; forward returns computed later
    assert row["robust_return"] == 0.06


def test_paper_portfolio_empty_is_safe() -> None:
    portfolio = build_paper_portfolio(pd.DataFrame(), AS_OF)
    assert portfolio.empty
    assert {"as_of", "ticker", "entry_price"} <= set(portfolio.columns)


def test_run_manifest_indexes_the_archive() -> None:
    manifest = build_run_manifest(
        as_of=AS_OF,
        fingerprints={"universe_fingerprint": "U1", "config_fingerprint": "C1"},
        counts={"universe": 514, "eligible": 6},
        artifacts=["robust_ranking.csv", "robust_ranking.csv", "run_metadata.json"],
        paper_portfolio_size=6,
    )
    assert manifest["as_of"] == "2026-01-09"
    assert manifest["universe_fingerprint"] == "U1"
    assert manifest["counts"]["eligible"] == 6
    assert manifest["artifacts"] == ["robust_ranking.csv", "run_metadata.json"]  # deduped, sorted
    assert manifest["paper_portfolio_size"] == 6
    # never claim calibrated probabilities until forward history exists
    assert manifest["calibration_note"] == CALIBRATION_NOTE
    assert "NOT calibrated probabilities" in manifest["calibration_note"]
