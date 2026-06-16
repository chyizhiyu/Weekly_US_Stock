"""Cross-asset evaluation spine (#7 skeleton) - STRUCTURE ONLY.

The four-layer framework abstracted so the SHARED spine is reused across asset
classes while the asset-SPECIFIC analytics are plugins:

  Layer 1 Survival/eligibility  -> EligibilityGate  (per-asset thresholds, shared shape)
  Layer 2 Anchor                -> AnchorModel      (per-asset: NOPAT / real yield / parent NAV)
  Layer 3 Scenarios             -> ScenarioModel    (per-asset: emits a ReturnDistribution)
  Layer 4 Risk-adjusted score   -> RiskAggregator   (SHARED: scores any ReturnDistribution)

ReturnDistribution is the asset-agnostic currency between Layer 3 and Layer 4.
Equity is the first and only plugin; crypto/perp are intentionally NOT built -
their Layer 2-3 are separate research problems and must wait for the equity
model's forward validation to accumulate.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable


@dataclass(slots=True, frozen=True)
class ScenarioOutcome:
    label: str
    value: float  # period return / IRR for this scenario
    probability: float


@dataclass(slots=True, frozen=True)
class ReturnDistribution:
    """Asset-agnostic hand-off from Layer 3 (scenarios) to Layer 4 (scoring)."""

    outcomes: tuple[ScenarioOutcome, ...]
    data_confidence: float = 1.0
    model_confidence: float = 1.0

    def median(self) -> float:
        ordered = sorted(self.outcomes, key=lambda outcome: outcome.value)
        cumulative = 0.0
        for outcome in ordered:
            cumulative += outcome.probability
            if cumulative >= 0.5 - 1e-12:
                return outcome.value
        return ordered[-1].value if ordered else 0.0

    def worst(self) -> float:
        return min((outcome.value for outcome in self.outcomes), default=0.0)


@dataclass(slots=True, frozen=True)
class RiskPreferences:
    hurdle_rate: float = 0.12
    downside_aversion: float = 1.0


@dataclass(slots=True, frozen=True)
class RobustScore:
    median: float
    worst_case: float
    worst_case_hurdle_gap: float
    evidence_confidence: float
    robust_return: float


class RiskAggregator:
    """SHARED Layer 4: collapse a ReturnDistribution into a risk-adjusted score.

    Same math as the equity ranking (deterministic worst-case stress, not a
    calibrated CVaR), but asset-agnostic: any plugin emitting a ReturnDistribution
    is scored identically."""

    def score(self, distribution: ReturnDistribution, prefs: RiskPreferences) -> RobustScore:
        median = distribution.median()
        worst = distribution.worst()
        gap = max(0.0, prefs.hurdle_rate - worst)
        evidence = distribution.data_confidence * distribution.model_confidence
        robust = evidence * max(0.0, median - prefs.hurdle_rate) - prefs.downside_aversion * gap
        return RobustScore(median, worst, gap, evidence, robust)


@runtime_checkable
class EligibilityGate(Protocol):
    """Layer 1: survival / tradability. Per-asset thresholds, shared shape."""

    def is_eligible(self, asset: object) -> tuple[bool, str]: ...


@runtime_checkable
class AnchorModel(Protocol):
    """Layer 2: the asset's normalized, point-in-time 'true output' anchor."""

    def anchor(self, asset: object) -> object: ...


@runtime_checkable
class ScenarioModel(Protocol):
    """Layer 3: project a distribution of forward returns from an anchor."""

    def distribution(self, anchor: object) -> ReturnDistribution: ...


@runtime_checkable
class AssetModel(Protocol):
    """A per-asset plugin: Layer 1-3 bundled. Layer 4 (RiskAggregator) is shared."""

    asset_class: str

    def eligibility_gate(self) -> EligibilityGate: ...

    def anchor_model(self) -> AnchorModel: ...

    def scenario_model(self) -> ScenarioModel: ...


@dataclass(slots=True)
class EvidenceRecord:
    """Audit trail for one asset's evaluation, so any decision is reconstructable."""

    asset_class: str
    identifier: str
    eligible: bool
    note: str = ""
    extras: dict = field(default_factory=dict)
