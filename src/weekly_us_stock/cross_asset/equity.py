"""Equity plugin for the cross-asset spine - the first and only plugin.

It adapts the EXISTING equity engine (no reimplementation): CompanyInputs is the
Layer-2 anchor and value_company is the Layer-3 scenario model, re-expressed as a
ReturnDistribution the shared RiskAggregator can score.
"""
from __future__ import annotations

from weekly_us_stock.config import RiskPreferenceSettings, ScenarioSettings
from weekly_us_stock.cross_asset.base import ReturnDistribution, ScenarioOutcome
from weekly_us_stock.cross_asset.registry import register_asset_model
from weekly_us_stock.models.valuation import CompanyInputs
from weekly_us_stock.valuation.irr import LOWER_BOUND
from weekly_us_stock.valuation.scenarios import value_company


class EquityScenarioModel:
    """Adapter: the equity scenario engine -> a ReturnDistribution."""

    def __init__(
        self, cfg: ScenarioSettings | None = None, prefs: RiskPreferenceSettings | None = None
    ) -> None:
        self._cfg = cfg or ScenarioSettings()
        self._prefs = prefs or RiskPreferenceSettings()

    def distribution(self, anchor: CompanyInputs) -> ReturnDistribution:
        valuation = value_company(anchor, self._cfg, self._prefs)
        outcomes = tuple(
            ScenarioOutcome(
                label=scenario.assumptions.name,
                value=float(scenario.irr_5y if scenario.irr_5y is not None else LOWER_BOUND),
                probability=float(scenario.assumptions.probability),
            )
            for scenario in valuation.scenarios
        )
        return ReturnDistribution(outcomes, valuation.data_confidence, valuation.model_confidence)


class _EquityEligibility:
    def is_eligible(self, asset: CompanyInputs) -> tuple[bool, str]:
        # The production survival gate is the hard-filter pipeline; this skeleton
        # only asserts the anchor is well-formed enough to be valued.
        ok = asset.shares_outstanding > 0 and asset.price > 0
        return (ok, "" if ok else "non_positive_price_or_shares")


class _EquityAnchor:
    def anchor(self, asset: CompanyInputs) -> CompanyInputs:
        return asset  # CompanyInputs already IS the normalized anchor


class EquityAssetModel:
    asset_class = "equity"

    def __init__(self) -> None:
        self._scenarios = EquityScenarioModel()
        self._eligibility = _EquityEligibility()
        self._anchor = _EquityAnchor()

    def eligibility_gate(self) -> _EquityEligibility:
        return self._eligibility

    def anchor_model(self) -> _EquityAnchor:
        return self._anchor

    def scenario_model(self) -> EquityScenarioModel:
        return self._scenarios


register_asset_model(EquityAssetModel())
