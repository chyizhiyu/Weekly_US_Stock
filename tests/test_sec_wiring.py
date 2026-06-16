"""Task #3-C wiring: composite SEC annotation + confidence haircut."""
from __future__ import annotations

from datetime import date

import pandas as pd

from weekly_us_stock.config import (
    EnvSettings,
    NormalizationSettings,
    SecReconciliationSettings,
    WaccSettings,
)
from weekly_us_stock.providers.composite import CompositeProvider
from weekly_us_stock.steps.step4_normalized import _data_confidence


class _FakeFMP:
    def load_fundamentals(self, tickers: list[str], as_of: date) -> pd.DataFrame:
        return pd.DataFrame(
            [
                {
                    "ticker": t, "fiscal_year": 2024, "revenue": 1000.0,
                    "operating_income": 200.0, "net_income": 150.0, "shares_diluted": 100.0,
                }
                for t in ("AAA", "BBB", "EXM")
            ]
        )


class _FakeSEC:
    def fetch_annual_facts(self, ticker: str) -> dict:
        if ticker == "AAA":  # matches FMP -> ok
            return {
                "revenue": {2024: 1000.0}, "operating_income": {2024: 200.0},
                "net_income": {2024: 150.0}, "shares_diluted": {2024: 100.0},
            }
        # revenue ~40% off -> hard divergence (BBB and EXM)
        return {
            "revenue": {2024: 600.0}, "operating_income": {2024: 200.0},
            "net_income": {2024: 150.0}, "shares_diluted": {2024: 100.0},
        }


def _composite(cfg: SecReconciliationSettings) -> CompositeProvider:
    return CompositeProvider(
        EnvSettings(), WaccSettings(), fmp=_FakeFMP(), sec=_FakeSEC(), sec_reconciliation=cfg
    )


def test_composite_annotates_sec_status_and_honours_exemption() -> None:
    comp = _composite(SecReconciliationSettings(exempt_tickers=["EXM"]))
    out = comp.load_fundamentals(["AAA", "BBB", "EXM"], date(2026, 1, 1)).set_index("ticker")
    assert out.loc["AAA", "sec_status"] == "ok"
    assert out.loc["BBB", "sec_status"] == "hard_divergence"
    assert out.loc["EXM", "sec_status"] == "exempt"  # hard, but exempt -> downgraded
    assert out.loc["BBB", "sec_max_divergence"] > 0.25


def test_sec_disabled_leaves_fundamentals_unannotated() -> None:
    out = _composite(SecReconciliationSettings(enabled=False)).load_fundamentals(
        ["AAA"], date(2026, 1, 1)
    )
    assert "sec_status" not in out.columns


def test_sec_soft_divergence_docks_data_confidence() -> None:
    s = NormalizationSettings()
    base = {
        "years_of_data": 8, "has_estimates": True, "beta": 1.0,
        "is_price_fresh": True, "anchor_source": "ttm",
    }
    clean = _data_confidence({**base, "sec_confidence_penalty": 0.0}, s)
    docked = _data_confidence({**base, "sec_confidence_penalty": 0.20}, s)
    assert abs((clean - docked) - 0.20) < 1e-9
