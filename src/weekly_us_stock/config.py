from __future__ import annotations

import os
from pathlib import Path

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


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


class RiskPreferenceSettings(BaseModel):
    """Investor risk preferences shaping the robust ranking; not factor weights."""

    hurdle_rate: float = 0.12
    downside_aversion: float = 1.0
    ambiguity_aversion: float = 0.5
    permanent_loss_penalty: float = 0.5
    cvar_alpha: float = 0.25
    permanent_loss_threshold: float = -0.30
    uncertainty_per_missing_confidence: float = 0.03
    # "penalized_expected": E[IRR] minus all three penalties (the project
    # spec's decomposition). "median_cvar": Median IRR - downside_aversion x
    # CVaR, with uncertainty/permanent-loss shown but not double-subtracted.
    formula: str = "penalized_expected"


class ConfidenceSettings(BaseModel):
    min_model_confidence: float = 0.2
    min_data_confidence: float = 0.2
    watchlist_data_confidence: float = 0.45
    watchlist_model_confidence: float = 0.35


class RankingSettings(BaseModel):
    top_n: int = 20


class ReportSettings(BaseModel):
    feishu_top_n: int = 10


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
    risk_preferences: RiskPreferenceSettings = Field(default_factory=RiskPreferenceSettings)
    confidence: ConfidenceSettings = Field(default_factory=ConfidenceSettings)
    ranking: RankingSettings = Field(default_factory=RankingSettings)
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
