from __future__ import annotations

import os
from pathlib import Path

import yaml
from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

KNOWN_INDEX_MEMBERSHIPS = {"sp500", "nasdaq100", "dowjones"}


class AppSettings(BaseModel):
    timezone: str = "Asia/Shanghai"
    market_timezone: str = "America/New_York"
    data_source: str = "sample"
    output_dir: str = "runs"
    sample_data_dir: str = "data/samples"


class UniverseSettings(BaseModel):
    exchanges: list[str] = Field(default_factory=lambda: ["NYSE", "NASDAQ", "AMEX"])
    include_adrs: bool = False
    allowed_security_types: list[str] = Field(default_factory=lambda: ["common_stock"])
    # Restrict the screened universe to the union of these index memberships
    # (e.g. ["sp500", "nasdaq100"]). Empty list = full US market. Names are
    # resolved to current constituent lists by the data provider.
    index_membership: list[str] = Field(default_factory=list)
    # Fail closed if a configured index returns fewer than this many
    # constituents (a sign the membership endpoint is broken/partial). Unknown
    # indices fall back to a conservative floor of 1.
    index_min_constituents: dict[str, int] = Field(
        default_factory=lambda: {"sp500": 400, "nasdaq100": 80, "dowjones": 25}
    )

    @field_validator("index_membership")
    @classmethod
    def _normalize_index_membership(cls, value: list[str]) -> list[str]:
        normalized: list[str] = []
        for item in value:
            key = str(item).strip().lower()
            if key not in KNOWN_INDEX_MEMBERSHIPS:
                raise ValueError(
                    f"unknown index_membership '{item}'; "
                    f"allowed: {sorted(KNOWN_INDEX_MEMBERSHIPS)}"
                )
            if key not in normalized:
                normalized.append(key)
        return normalized


class HardFilterSettings(BaseModel):
    min_listing_years: int = 3
    min_market_cap: float = 500_000_000
    min_avg_dollar_volume: float = 5_000_000
    liquidity_window_days: int = 60
    max_consecutive_loss_years: int = 3
    max_negative_fcf_years: int = 4
    min_financial_years: int = 5
    min_interest_coverage: float = 2.0
    max_net_debt_to_ebitda: float = 6.0
    max_share_dilution_cagr_3y: float = 0.07
    min_ocf_to_net_income: float = 0.5


class NormalizationSettings(BaseModel):
    lookback_years: int = 8
    min_years_for_normalization: int = 5
    default_tax_rate: float = 0.21
    min_tax_rate: float = 0.10
    max_tax_rate: float = 0.35
    max_filing_age_days: int = 150  # older anchor filings cut data confidence


class EventGateSettings(BaseModel):
    """Price-shock proxies for material events (contract loss, guidance cut,
    regulatory action...). Flagged names go to the event watchlist for manual
    re-underwriting instead of being ranked on stale earning power."""

    enabled: bool = True
    weekly_drop_threshold: float = 0.25
    drawdown_threshold: float = 0.40
    lookback_high_days: int = 60


class WaccSettings(BaseModel):
    equity_risk_premium: float = 0.05
    default_beta: float = 1.0
    fallback_risk_free: float = 0.042
    base_credit_spread: float = 0.015
    stressed_credit_spread: float = 0.04
    min_wacc: float = 0.065
    max_wacc: float = 0.14


class ScenarioSettings(BaseModel):
    horizon_years: int = 5
    exit_year: int = 3
    terminal_growth: float = 0.025
    probabilities: dict[str, float] = Field(
        default_factory=lambda: {"bear": 0.25, "base": 0.50, "bull": 0.25}
    )
    base_growth_cap: float = 0.25
    base_growth_floor: float = -0.05
    base_growth_spread: float = 0.04
    bear_spread_skew: float = 1.25
    bear_margin_haircut: float = 0.15
    bull_margin_uplift: float = 0.06
    # Above 1.0 the company burns cash to fund growth (negative FCF) — the
    # economically honest outcome for capital hogs growing beyond their ROIC.
    max_reinvestment_rate: float = 1.20
    price_anchor_growth: float = 0.05
    max_share_change_rate: float = 0.08
    min_share_change_rate: float = -0.05
    # P1-3: buybacks are not mechanically extrapolated. The retirement rate
    # decays toward zero each year, spend is capped at a fraction of positive
    # distributable FCF, and buybacks stop when leverage is too high. Dilution
    # (positive share change) is NOT decayed - the SBC/issuance penalty stays.
    buyback_decay: float = 0.80
    buyback_max_fcf_fraction: float = 0.80
    buyback_max_net_debt_to_nopat: float = 4.0


class RiskPreferenceSettings(BaseModel):
    """Investor risk preferences shaping the robust ranking; not factor weights."""

    hurdle_rate: float = 0.12
    downside_aversion: float = 1.0
    ambiguity_aversion: float = 0.5
    permanent_loss_penalty: float = 0.5
    cvar_alpha: float = 0.25
    permanent_loss_threshold: float = -0.30
    uncertainty_per_missing_confidence: float = 0.03
    # hurdle_cvar (default): confidence-scaled positive excess over the hurdle
    # minus the hurdle-relative tail shortfall. "penalized_expected": E[IRR]
    # minus all three penalties (the original spec decomposition).
    # "median_cvar": Median IRR - downside_aversion x zero-anchored CVaR.
    formula: str = "hurdle_cvar"


class ConfidenceSettings(BaseModel):
    min_model_confidence: float = 0.2
    min_data_confidence: float = 0.2
    watchlist_data_confidence: float = 0.45
    watchlist_model_confidence: float = 0.35


class RankingSettings(BaseModel):
    top_n: int = 20


class EligibilitySettings(BaseModel):
    """Minimum bar a ranked name must clear to be an actionable candidate
    (P0-4). Ranking != investability: a name can be ranked yet ineligible.
    Stricter optional gates default to off (None)."""

    require_robust_return_positive: bool = True
    require_median_above_hurdle: bool = True
    min_p10_irr: float | None = None
    min_above_hurdle_weight: float | None = None
    max_model_uncertainty: float | None = None
    min_evidence_confidence: float | None = None


class ReportSettings(BaseModel):
    feishu_top_n: int = 10


class AlertSettings(BaseModel):
    """Boundary-assumption and extreme-valuation alert thresholds (P1-2).

    A hit does not prove the valuation is wrong, but it lowers model confidence
    and/or routes the name to manual review so a boundary-driven number is never
    read as an ordinary precise estimate. All thresholds are configurable."""

    intrinsic_to_price_flag: float = 2.0   # base intrinsic >= 2x price -> soft flag
    intrinsic_to_price_review: float = 3.0  # >= 3x price -> manual review
    median_irr_review: float = 1.0          # median IRR >= 100% -> manual review
    bull_return_review: float = 10.0        # bull 5y total return >= 1000% -> review
    scenario_span_review: float = 2.0       # P90 - P10 >= 200 points -> review
    model_confidence_haircut_per_flag: float = 0.9  # per boundary assumption hit


class FreshnessSettings(BaseModel):
    max_price_staleness_days: int = 3
    min_fresh_price_coverage: float = 0.8


class Settings(BaseModel):
    app: AppSettings = Field(default_factory=AppSettings)
    universe: UniverseSettings = Field(default_factory=UniverseSettings)
    hard_filters: HardFilterSettings = Field(default_factory=HardFilterSettings)
    normalization: NormalizationSettings = Field(default_factory=NormalizationSettings)
    wacc: WaccSettings = Field(default_factory=WaccSettings)
    scenarios: ScenarioSettings = Field(default_factory=ScenarioSettings)
    events: EventGateSettings = Field(default_factory=EventGateSettings)
    risk_preferences: RiskPreferenceSettings = Field(default_factory=RiskPreferenceSettings)
    confidence: ConfidenceSettings = Field(default_factory=ConfidenceSettings)
    ranking: RankingSettings = Field(default_factory=RankingSettings)
    eligibility: EligibilitySettings = Field(default_factory=EligibilitySettings)
    alerts: AlertSettings = Field(default_factory=AlertSettings)
    report: ReportSettings = Field(default_factory=ReportSettings)
    freshness: FreshnessSettings = Field(default_factory=FreshnessSettings)


class EnvSettings(BaseSettings):
    fmp_api_key: str | None = None
    polygon_api_key: str | None = None
    fred_api_key: str | None = None
    sec_user_agent: str | None = None
    weekly_us_stock_data_source: str | None = None
    weekly_us_stock_output_dir: str | None = None

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_settings(config_path: str | Path | None = None) -> Settings:
    path = Path(config_path) if config_path else project_root() / "config" / "default.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}
    settings = Settings.model_validate(data or {})
    env = EnvSettings()

    if env.weekly_us_stock_data_source:
        settings.app.data_source = env.weekly_us_stock_data_source
    if env.weekly_us_stock_output_dir:
        settings.app.output_dir = env.weekly_us_stock_output_dir

    os.environ.setdefault("TZ", settings.app.timezone)
    return settings
