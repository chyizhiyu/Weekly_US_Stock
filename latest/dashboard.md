# Weekly US Stock Screen — 2026-10-02

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-10-02**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 517 | - |
| step2_hard_filters | 517 | 310 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 16 |
| step3_standardize | 310 | 310 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 310 | 302 | no_normalized_earnings: 8 |
| step5_quality_risk | 302 | 296 | - |
| step6_scenario_valuation | 296 | 272 | insufficient_post_valuation_model_confidence: 17, roic_not_meaningful:meaningless_capital: 5, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 331 | 331 | - |

## Eligible Candidates (8)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OMC | 12.1% | 29.7% | 20.3% | 36.3% | 0.0% | 0% | 0.82 | 0.68 |
| 2 | VICI | 7.9% | 28.5% | 14.5% | 28.5% | 0.0% | 0% | 0.56 | 0.48 |
| 3 | UHS | 6.4% | 24.8% | 8.6% | 34.2% | 3.4% | 0% | 0.77 | 0.76 |
| 4 | ARE | 6.1% | 24.8% | 16.4% | 24.8% | 0.0% | 0% | 0.71 | 0.48 |
| 5 | CMCSA | 4.7% | 21.2% | 15.5% | 24.3% | 0.0% | 0% | 0.75 | 0.51 |
| 6 | FOXA | 3.6% | 23.7% | 7.6% | 32.5% | 4.4% | 0% | 0.90 | 0.69 |
| 7 | BXP | 3.1% | 20.2% | 11.2% | 20.2% | 0.8% | 0% | 0.68 | 0.48 |
| 8 | CPT | 2.5% | 21.6% | 9.9% | 21.6% | 2.1% | 0% | 0.60 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OMC | 12.1% | 29.7% | 20.3% | 36.3% | 0.0% | 0% | 0.82 | 0.68 |
| 2 | VICI | 7.9% | 28.5% | 14.5% | 28.5% | 0.0% | 0% | 0.56 | 0.48 |
| 3 | UHS | 6.4% | 24.8% | 8.6% | 34.2% | 3.4% | 0% | 0.77 | 0.76 |
| 4 | ARE | 6.1% | 24.8% | 16.4% | 24.8% | 0.0% | 0% | 0.71 | 0.48 |
| 5 | CMCSA | 4.7% | 21.2% | 15.5% | 24.3% | 0.0% | 0% | 0.75 | 0.51 |
| 6 | FOXA | 3.6% | 23.7% | 7.6% | 32.5% | 4.4% | 0% | 0.90 | 0.69 |
| 7 | BXP | 3.1% | 20.2% | 11.2% | 20.2% | 0.8% | 0% | 0.68 | 0.48 |
| 8 | CPT | 2.5% | 21.6% | 9.9% | 21.6% | 2.1% | 0% | 0.60 | 0.48 |
| 9 | CF | -1.9% | 31.6% | 3.0% | 49.2% | 9.0% | 0% | 0.89 | 0.36 |
| 10 | ELV | -2.7% | 11.4% | 9.3% | 17.4% | 2.7% | 0% | 0.81 | 0.67 |
| 11 | UDR | -2.7% | 18.9% | 6.0% | 18.9% | 6.0% | 0% | 0.56 | 0.48 |
| 12 | VMRK | -3.1% | 16.9% | 6.5% | 20.8% | 5.5% | 0% | 0.63 | 0.48 |
| 13 | DECK | -3.5% | 16.2% | 5.4% | 23.0% | 6.6% | 0% | 0.96 | 0.75 |
| 14 | HUM | -3.6% | 15.9% | 6.0% | 23.6% | 6.0% | 0% | 0.75 | 0.62 |
| 15 | GIS | -4.2% | 19.8% | 2.0% | 29.0% | 10.0% | 0% | 0.80 | 0.74 |
| 16 | ZTS | -5.4% | 16.0% | 3.0% | 23.3% | 9.0% | 0% | 0.98 | 0.89 |
| 17 | CTSH | -6.8% | 13.1% | 4.3% | 19.2% | 7.7% | 0% | 0.85 | 0.87 |
| 18 | ADBE | -7.1% | 13.5% | 3.7% | 19.4% | 8.3% | 0% | 0.98 | 0.79 |
| 19 | INVH | -7.5% | 13.9% | 3.5% | 13.9% | 8.5% | 0% | 0.62 | 0.48 |
| 20 | MO | -7.8% | 15.4% | 1.1% | 22.9% | 10.9% | 0% | 0.98 | 0.92 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CI | 29.1% | 33.0% | -12.0% | 62.4% | 75% | 184% |
| 2 | OMC | 29.0% | 29.7% | 20.3% | 36.3% | 100% | 168% |
| 3 | CF | 28.8% | 31.6% | 3.0% | 49.2% | 75% | 140% |
| 4 | VICI | 25.0% | 28.5% | 14.5% | 28.5% | 100% | 250% |
| 5 | UHS | 23.1% | 24.8% | 8.6% | 34.2% | 75% | 69% |
| 6 | ARE | 22.7% | 24.8% | 16.4% | 24.8% | 100% | 203% |
| 7 | EOG | 22.1% | 24.1% | -1.1% | 41.4% | 75% | 91% |
| 8 | FOXA | 21.9% | 23.7% | 7.6% | 32.5% | 75% | 79% |
| 9 | CHTR | 20.6% | 51.5% | -95.0% | 74.4% | 75% | 359% |
| 10 | CMCSA | 20.6% | 21.2% | 15.5% | 24.3% | 100% | 79% |
| 11 | CPT | 18.6% | 21.6% | 9.9% | 21.6% | 75% | 166% |
| 12 | BXP | 17.9% | 20.2% | 11.2% | 20.2% | 75% | 151% |
| 13 | GIS | 17.7% | 19.8% | 2.0% | 29.0% | 75% | 63% |
| 14 | FISV | 16.4% | 28.7% | -44.9% | 53.1% | 75% | 117% |
| 15 | UDR | 15.7% | 18.9% | 6.0% | 18.9% | 75% | 137% |
| 16 | HUM | 15.3% | 15.9% | 6.0% | 23.6% | 75% | 40% |
| 17 | VMRK | 15.3% | 16.9% | 6.5% | 20.8% | 75% | 119% |
| 18 | DECK | 15.2% | 16.2% | 5.4% | 23.0% | 75% | 22% |
| 19 | ZTS | 14.6% | 16.0% | 3.0% | 23.3% | 75% | 31% |
| 20 | MKC | 14.1% | 15.9% | -0.4% | 25.1% | 75% | 38% |

## Week-over-week

Previous run: 2026-09-25

- Entered Robust Top: MO
- Exited Robust Top: EOG
- Entered Upside Top: MKC
- Exited Upside Top: MO

Largest robust-rank moves:

- JBL: 226 → 185 (+41)
- KR: 293 → 312 (-19)
- AMAT: 199 → 215 (-16)
- QCOM: 174 → 159 (+15)
- MKC: 38 → 23 (+15)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| OMC | bear | 25% | 18.6% | 12.8% | 7.3% | 133.09 | 20.3% | 168% |
| OMC | base | 50% | 25.0% | 14.6% | 7.3% | 198.62 | 29.7% | 296% |
| OMC | bull | 25% | 30.1% | 15.9% | 7.3% | 258.24 | 36.3% | 412% |
| UHS | bear | 25% | 1.6% | 8.8% | 8.8% | 162.51 | 8.6% | 43% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 297.08 | 24.8% | 185% |
| UHS | bull | 25% | 11.5% | 12.1% | 19.4% | 419.16 | 34.2% | 311% |
| CMCSA | bear | 25% | -6.9% | 16.1% | 6.7% | 28.53 | 15.5% | 85% |
| CMCSA | base | 50% | 0.5% | 18.7% | 6.7% | 38.64 | 21.2% | 157% |
| CMCSA | bull | 25% | 6.4% | 20.4% | 6.7% | 48.69 | 24.3% | 230% |
| FOXA | bear | 25% | -1.3% | 17.3% | 7.5% | 61.94 | 7.6% | 38% |
| FOXA | base | 50% | 4.4% | 19.7% | 54.7% | 111.46 | 23.7% | 175% |
| FOXA | bull | 25% | 8.9% | 21.5% | 60.0% | 151.58 | 32.5% | 284% |
| CF | bear | 25% | -10.3% | 22.8% | 7.4% | 95.97 | 3.0% | 13% |
| CF | base | 50% | 11.7% | 31.1% | 17.9% | 275.73 | 31.6% | 277% |
| CF | bull | 25% | 29.3% | 38.4% | 19.1% | 549.02 | 49.2% | 635% |
| ELV | bear | 25% | -0.7% | 4.8% | 7.8% | 414.73 | 9.3% | 50% |
| ELV | base | 50% | 5.5% | 5.9% | 7.8% | 459.75 | 11.4% | 73% |
| ELV | bull | 25% | 10.5% | 6.6% | 7.8% | 600.12 | 17.4% | 127% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.8% | 65.72 | 5.4% | 26% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 96.49 | 16.2% | 102% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 122.24 | 23.0% | 165% |
| HUM | bear | 25% | 13.7% | 2.5% | 8.6% | 348.09 | 6.0% | 34% |
| HUM | base | 50% | 19.1% | 3.7% | 8.6% | 542.19 | 15.9% | 110% |
| HUM | bull | 25% | 23.5% | 4.8% | 8.6% | 751.49 | 23.6% | 192% |
| GIS | bear | 25% | -8.0% | 14.7% | 6.8% | 25.05 | 2.0% | 9% |
| GIS | base | 50% | -2.2% | 17.0% | 10.1% | 52.24 | 19.8% | 125% |
| GIS | bull | 25% | 2.4% | 18.6% | 11.0% | 75.39 | 29.0% | 226% |
| ZTS | bear | 25% | -1.8% | 32.2% | 8.1% | 54.75 | 3.0% | 14% |
| ZTS | base | 50% | 2.8% | 36.0% | 24.3% | 91.57 | 16.0% | 102% |
| ZTS | bull | 25% | 6.5% | 39.1% | 24.5% | 120.44 | 23.3% | 172% |
| CTSH | bear | 25% | -0.4% | 12.8% | 9.1% | 47.89 | 4.3% | 20% |
| CTSH | base | 50% | 4.6% | 15.0% | 13.9% | 67.21 | 13.1% | 80% |
| CTSH | bull | 25% | 8.6% | 16.6% | 14.8% | 84.47 | 19.2% | 133% |
| ADBE | bear | 25% | 9.1% | 29.7% | 11.9% | 171.53 | 3.7% | 17% |
| ADBE | base | 50% | 13.6% | 33.6% | 58.7% | 246.85 | 13.5% | 81% |
| ADBE | bull | 25% | 17.1% | 36.9% | 59.8% | 304.45 | 19.4% | 131% |
| MO | bear | 25% | -2.3% | 48.7% | 7.3% | 50.76 | 1.1% | 5% |
| MO | base | 50% | 1.3% | 54.9% | 45.6% | 91.22 | 15.4% | 96% |
| MO | bull | 25% | 4.1% | 60.1% | 46.5% | 121.33 | 22.9% | 164% |

## Boundary Assumptions & Valuation Alerts

- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- UHS — bounds: share_change_floor_hit
- ARE — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;reinvestment_cap_hit
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit
- BXP — bounds: specialist_model_v1
- CPT — bounds: specialist_model_v1
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- UDR — bounds: specialist_model_v1
- VMRK — bounds: specialist_model_v1
- DECK — bounds: forward_roic_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- ADBE — bounds: share_change_floor_hit
- INVH — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| FICO | weekly_drop;drawdown_from_high | -28% | -51% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| CTVA | weekly_drop;drawdown_from_high | -85% | -87% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| APP | drawdown_from_high | nan% | -41% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- OMC: incremental_roic_below_wacc
- VICI: nan
- ARE: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- BXP: nan
- CPT: nan
- CF: cyclical_revenue
- ELV: incremental_roic_below_wacc
- UDR: nan
- VMRK: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- GIS: elevated_leverage, thin_interest_coverage
- ADBE: heavy_sbc
- INVH: nan

## Watchlist (not rankable under the general model)

- V Visa Inc. — consumer_finance_model_not_supported
- MA Mastercard Incorporated — consumer_finance_model_not_supported
- MS Morgan Stanley — asset_management_model_not_supported
- GS The Goldman Sachs Group, Inc. — asset_management_model_not_supported
- AXP American Express Company — consumer_finance_model_not_supported
- SCHW The Charles Schwab Corporation — asset_management_model_not_supported
- BLK BlackRock, Inc. — asset_management_model_not_supported
- BX Blackstone Inc. — asset_management_model_not_supported
- COF Capital One Financial Corporation — consumer_finance_model_not_supported
- SPGI S&P Global Inc. — financial_sector_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
- ARES Ares Management Corporation — asset_management_model_not_supported
- RJF Raymond James Financial, Inc. — asset_management_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- BEN Franklin Resources, Inc. — asset_management_model_not_supported
- IVZ Invesco Ltd. — asset_management_model_not_supported
- FDS FactSet Research Systems Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- CME CME Group Inc. — financial_sector_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- FICO Fair Isaac Corporation — material_event_requires_reunderwriting
- CTVA Corteva, Inc. — material_event_requires_reunderwriting
- APP AppLovin Corporation — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- PSX Phillips 66 — insufficient_model_confidence
- HLT Hilton Worldwide Holdings Inc. — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- GM General Motors Company — irr_below_solver_bound
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- EXPE Expedia Group, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- COP ConocoPhillips — insufficient_post_valuation_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_post_valuation_model_confidence
- VLO Valero Energy Corporation — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- DVN Devon Energy Corporation — insufficient_post_valuation_model_confidence
- XYZ Block, Inc. — insufficient_post_valuation_model_confidence
- IR Ingersoll Rand Inc. — insufficient_post_valuation_model_confidence
- IFF International Flavors & Fragrances Inc. — insufficient_post_valuation_model_confidence
- NVDA NVIDIA Corporation — insufficient_post_valuation_model_confidence
- TSLA Tesla, Inc. — insufficient_post_valuation_model_confidence
- MU Micron Technology, Inc. — insufficient_post_valuation_model_confidence
- AMD Advanced Micro Devices, Inc. — insufficient_post_valuation_model_confidence
- LITE Lumentum Holdings Inc. — insufficient_post_valuation_model_confidence
- STLD Steel Dynamics, Inc. — insufficient_post_valuation_model_confidence

## Data Gaps and Model Limitations

- Stocks missing core financials were rejected (fail closed), never estimated.
- Banks, insurers and REITs use conservative specialist models; rows with
  incomplete specialist inputs stay watchlisted instead of entering ranking.
- Asset managers, consumer-finance names, other financials and pre-profit
  biotech remain watchlisted until dedicated models exist.
- Scenario set is discrete (bear/base/bull); worst-case stress metrics are
  deterministic bear/base/bull stress labels, not calibrated CVaR.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
