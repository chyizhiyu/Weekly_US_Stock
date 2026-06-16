"""Task #3-C engine: FMP-vs-SEC divergence classifier and SEC extraction."""
from __future__ import annotations

from weekly_us_stock.providers.sec import (
    _REVENUE_TAGS,
    _SHARES_TAGS,
    extract_annual_concept,
    sec_divergence,
)

_SEC = {
    "revenue": {2024: 1000.0},
    "operating_income": {2024: 200.0},
    "net_income": {2024: 150.0},
    "shares_diluted": {2024: 100.0},
}
_KW = {"soft": 0.10, "hard": 0.25, "min_metrics": 2}


def test_divergence_classifies_ok_soft_hard() -> None:
    ok = sec_divergence(
        {"revenue": 1010, "operating_income": 205, "net_income": 150, "shares_diluted": 100},
        _SEC, 2024, **_KW,
    )
    assert ok[0] == "ok"
    soft = sec_divergence(
        {"revenue": 1000, "operating_income": 200, "net_income": 172.5, "shares_diluted": 100},
        _SEC, 2024, **_KW,
    )
    assert soft[0] == "soft_divergence" and soft[2] == "net_income" and abs(soft[1] - 0.15) < 1e-9
    hard = sec_divergence(
        {"revenue": 1300, "operating_income": 200, "net_income": 150, "shares_diluted": 100},
        _SEC, 2024, **_KW,
    )
    assert hard[0] == "hard_divergence" and hard[2] == "revenue"


def test_divergence_unchecked_when_too_few_common_metrics() -> None:
    # Only one metric overlaps -> below min_metrics
    one = sec_divergence(
        {"revenue": 1000, "operating_income": 200}, {"revenue": {2024: 1000.0}}, 2024, **_KW
    )
    assert one[0] == "unchecked"
    # Fiscal year not present in SEC -> nothing to compare
    miss = sec_divergence(
        {"revenue": 1000, "net_income": 150},
        {"revenue": {2023: 1000.0}, "net_income": {2023: 150.0}}, 2024, **_KW,
    )
    assert miss[0] == "unchecked"


def test_extract_annual_concept_honours_unit_and_10k_fy_only() -> None:
    facts = {"facts": {"us-gaap": {
        "Revenues": {"units": {"USD": [
            {"fy": 2024, "fp": "FY", "form": "10-K", "val": 1000},
            {"fy": 2024, "fp": "Q1", "form": "10-Q", "val": 250},  # not FY 10-K -> ignored
        ]}},
        "WeightedAverageNumberOfDilutedSharesOutstanding": {"units": {"shares": [
            {"fy": 2024, "fp": "FY", "form": "10-K", "val": 100},
        ]}},
    }}}
    assert extract_annual_concept(facts, _REVENUE_TAGS) == {2024: 1000.0}
    assert extract_annual_concept(facts, _SHARES_TAGS, unit="shares") == {2024: 100.0}
