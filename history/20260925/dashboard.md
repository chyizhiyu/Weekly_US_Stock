# Weekly US Stock Screen — 2026-09-25

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-09-25**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 516 | - |
| step2_hard_filters | 516 | 312 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 15 |
| step3_standardize | 312 | 312 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 312 | 303 | no_normalized_earnings: 8, normalization_failed: 1 |
| step5_quality_risk | 303 | 297 | - |
| step6_scenario_valuation | 297 | 274 | insufficient_post_valuation_model_confidence: 16, roic_not_meaningful:meaningless_capital: 5, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 333 | 333 | - |

## Eligible Candidates (8)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OMC | 11.4% | 29.4% | 18.4% | 37.3% | 0.0% | 0% | 0.83 | 0.66 |
| 2 | VICI | 8.0% | 28.6% | 14.2% | 28.6% | 0.0% | 0% | 0.55 | 0.48 |
| 3 | UHS | 6.1% | 24.6% | 8.5% | 34.1% | 3.5% | 0% | 0.77 | 0.76 |
| 4 | ARE | 5.8% | 24.0% | 15.5% | 24.0% | 0.0% | 0% | 0.70 | 0.48 |
| 5 | CMCSA | 4.7% | 21.2% | 15.7% | 24.6% | 0.0% | 0% | 0.76 | 0.51 |
| 6 | FOXA | 3.7% | 23.8% | 7.5% | 32.7% | 4.5% | 0% | 0.90 | 0.69 |
| 7 | CPT | 2.6% | 21.9% | 9.9% | 21.9% | 2.1% | 0% | 0.59 | 0.48 |
| 8 | BXP | 2.2% | 19.7% | 10.5% | 19.7% | 1.5% | 0% | 0.67 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OMC | 11.4% | 29.4% | 18.4% | 37.3% | 0.0% | 0% | 0.83 | 0.66 |
| 2 | VICI | 8.0% | 28.6% | 14.2% | 28.6% | 0.0% | 0% | 0.55 | 0.48 |
| 3 | UHS | 6.1% | 24.6% | 8.5% | 34.1% | 3.5% | 0% | 0.77 | 0.76 |
| 4 | ARE | 5.8% | 24.0% | 15.5% | 24.0% | 0.0% | 0% | 0.70 | 0.48 |
| 5 | CMCSA | 4.7% | 21.2% | 15.7% | 24.6% | 0.0% | 0% | 0.76 | 0.51 |
| 6 | FOXA | 3.7% | 23.8% | 7.5% | 32.7% | 4.5% | 0% | 0.90 | 0.69 |
| 7 | CPT | 2.6% | 21.9% | 9.9% | 21.9% | 2.1% | 0% | 0.59 | 0.48 |
| 8 | BXP | 2.2% | 19.7% | 10.5% | 19.7% | 1.5% | 0% | 0.67 | 0.48 |
| 9 | CF | -1.5% | 32.1% | 3.2% | 49.9% | 8.8% | 0% | 0.89 | 0.36 |
| 10 | UDR | -2.3% | 19.5% | 6.2% | 19.5% | 5.8% | 0% | 0.55 | 0.48 |
| 11 | DECK | -2.9% | 16.6% | 5.7% | 23.5% | 6.3% | 0% | 0.96 | 0.75 |
| 12 | ELV | -3.1% | 11.1% | 8.9% | 17.0% | 3.1% | 0% | 0.82 | 0.67 |
| 13 | VMRK | -3.3% | 17.0% | 6.3% | 21.0% | 5.7% | 0% | 0.62 | 0.48 |
| 14 | HUM | -4.1% | 15.5% | 5.7% | 23.3% | 6.3% | 0% | 0.75 | 0.62 |
| 15 | CTSH | -5.2% | 14.0% | 5.0% | 20.1% | 7.0% | 0% | 0.85 | 0.87 |
| 16 | GIS | -5.5% | 19.0% | 1.3% | 28.2% | 10.7% | 0% | 0.80 | 0.74 |
| 17 | ZTS | -5.8% | 15.9% | 2.8% | 23.2% | 9.2% | 0% | 0.98 | 0.89 |
| 18 | ADBE | -6.3% | 13.9% | 4.1% | 19.9% | 7.9% | 0% | 0.98 | 0.79 |
| 19 | INVH | -7.5% | 14.2% | 3.5% | 14.2% | 8.5% | 0% | 0.61 | 0.48 |
| 20 | EOG | -7.7% | 24.6% | -0.9% | 42.1% | 12.9% | 0% | 0.87 | 0.41 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CI | 29.7% | 33.5% | -11.1% | 62.9% | 75% | 191% |
| 2 | CF | 29.3% | 32.1% | 3.2% | 49.9% | 75% | 145% |
| 3 | OMC | 28.6% | 29.4% | 18.4% | 37.3% | 100% | 165% |
| 4 | VICI | 25.0% | 28.6% | 14.2% | 28.6% | 100% | 252% |
| 5 | UHS | 22.9% | 24.6% | 8.5% | 34.1% | 75% | 69% |
| 6 | EOG | 22.6% | 24.6% | -0.9% | 42.1% | 75% | 95% |
| 7 | FOXA | 21.9% | 23.8% | 7.5% | 32.7% | 75% | 80% |
| 8 | ARE | 21.9% | 24.0% | 15.5% | 24.0% | 100% | 194% |
| 9 | CHTR | 20.7% | 51.7% | -95.0% | 74.3% | 75% | 363% |
| 10 | CMCSA | 20.6% | 21.2% | 15.7% | 24.6% | 100% | 80% |
| 11 | CPT | 18.9% | 21.9% | 9.9% | 21.9% | 75% | 169% |
| 12 | BXP | 17.4% | 19.7% | 10.5% | 19.7% | 75% | 145% |
| 13 | GIS | 16.9% | 19.0% | 1.3% | 28.2% | 75% | 59% |
| 14 | FISV | 16.4% | 27.9% | -42.4% | 52.0% | 75% | 112% |
| 15 | UDR | 16.1% | 19.5% | 6.2% | 19.5% | 75% | 143% |
| 16 | DECK | 15.6% | 16.6% | 5.7% | 23.5% | 75% | 24% |
| 17 | VMRK | 15.3% | 17.0% | 6.3% | 21.0% | 75% | 119% |
| 18 | HUM | 15.0% | 15.5% | 5.7% | 23.3% | 75% | 38% |
| 19 | ZTS | 14.4% | 15.9% | 2.8% | 23.2% | 75% | 31% |
| 20 | MO | 13.6% | 15.3% | 0.9% | 22.8% | 75% | 36% |

## Week-over-week

Previous run: 2026-09-18

- Entered Robust Top: ADBE, EOG, GIS
- Exited Robust Top: HST, LEN, TTD
- Entered Upside Top: MO
- Exited Upside Top: TTD

Largest robust-rank moves:

- EL: 330 → 289 (+41)
- CARR: 297 → 324 (-27)
- J: 294 → 318 (-24)
- QCOM: 153 → 174 (-21)
- AMGN: 129 → 149 (-20)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| OMC | bear | 25% | 16.4% | 12.8% | 7.3% | 125.94 | 18.4% | 147% |
| OMC | base | 50% | 25.0% | 14.6% | 7.3% | 202.09 | 29.4% | 291% |
| OMC | bull | 25% | 31.9% | 15.9% | 7.3% | 275.95 | 37.3% | 430% |
| UHS | bear | 25% | 1.6% | 8.8% | 8.7% | 164.97 | 8.5% | 42% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 302.16 | 24.6% | 184% |
| UHS | bull | 25% | 11.5% | 12.1% | 19.4% | 426.60 | 34.1% | 309% |
| CMCSA | bear | 25% | -6.8% | 16.1% | 6.7% | 29.32 | 15.7% | 86% |
| CMCSA | base | 50% | 0.6% | 18.7% | 6.7% | 39.43 | 21.2% | 157% |
| CMCSA | bull | 25% | 6.5% | 20.4% | 6.7% | 50.07 | 24.6% | 232% |
| FOXA | bear | 25% | -1.3% | 17.3% | 7.4% | 62.89 | 7.5% | 37% |
| FOXA | base | 50% | 4.4% | 19.7% | 54.8% | 113.84 | 23.8% | 177% |
| FOXA | bull | 25% | 8.9% | 21.5% | 60.0% | 155.13 | 32.7% | 287% |
| CF | bear | 25% | -10.4% | 22.8% | 7.3% | 96.91 | 3.2% | 14% |
| CF | base | 50% | 11.6% | 31.1% | 17.9% | 281.35 | 32.1% | 285% |
| CF | bull | 25% | 29.2% | 38.4% | 19.1% | 562.64 | 49.9% | 653% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.7% | 66.33 | 5.7% | 27% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 97.72 | 16.6% | 106% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 123.96 | 23.5% | 170% |
| ELV | bear | 25% | -0.7% | 4.8% | 7.7% | 419.73 | 8.9% | 47% |
| ELV | base | 50% | 5.5% | 5.9% | 7.7% | 466.68 | 11.1% | 71% |
| ELV | bull | 25% | 10.5% | 6.6% | 7.7% | 609.16 | 17.0% | 124% |
| HUM | bear | 25% | 13.7% | 2.5% | 8.5% | 352.83 | 5.7% | 32% |
| HUM | base | 50% | 19.1% | 3.7% | 8.5% | 550.04 | 15.5% | 107% |
| HUM | bull | 25% | 23.5% | 4.8% | 8.5% | 762.62 | 23.3% | 188% |
| CTSH | bear | 25% | -0.4% | 12.8% | 9.0% | 48.56 | 5.0% | 23% |
| CTSH | base | 50% | 4.6% | 15.0% | 13.9% | 68.44 | 14.0% | 86% |
| CTSH | bull | 25% | 8.6% | 16.6% | 14.8% | 86.17 | 20.1% | 142% |
| GIS | bear | 25% | -8.0% | 14.7% | 6.7% | 25.61 | 1.3% | 6% |
| GIS | base | 50% | -2.2% | 17.0% | 10.1% | 53.49 | 19.0% | 119% |
| GIS | bull | 25% | 2.4% | 18.6% | 11.0% | 77.32 | 28.2% | 218% |
| ZTS | bear | 25% | -1.8% | 32.2% | 8.0% | 55.54 | 2.8% | 13% |
| ZTS | base | 50% | 2.8% | 36.0% | 24.3% | 93.34 | 15.9% | 101% |
| ZTS | bull | 25% | 6.4% | 39.1% | 24.5% | 122.94 | 23.2% | 172% |
| ADBE | bear | 25% | 9.1% | 29.7% | 11.8% | 173.19 | 4.1% | 19% |
| ADBE | base | 50% | 13.6% | 33.6% | 58.7% | 249.85 | 13.9% | 85% |
| ADBE | bull | 25% | 17.1% | 36.9% | 59.8% | 308.40 | 19.9% | 135% |
| EOG | bear | 25% | -7.9% | 22.6% | 7.4% | 99.26 | -0.9% | -4% |
| EOG | base | 50% | 14.0% | 32.4% | 14.4% | 273.91 | 24.6% | 194% |
| EOG | bull | 25% | 31.5% | 41.1% | 15.4% | 553.58 | 42.1% | 492% |

## Boundary Assumptions & Valuation Alerts

- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- UHS — bounds: share_change_floor_hit
- ARE — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;reinvestment_cap_hit
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit
- CPT — bounds: specialist_model_v1
- BXP — bounds: specialist_model_v1
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- UDR — bounds: specialist_model_v1
- DECK — bounds: forward_roic_cap_hit
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- VMRK — bounds: specialist_model_v1
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- ADBE — bounds: share_change_floor_hit
- INVH — bounds: specialist_model_v1
- EOG — bounds: reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| APP | drawdown_from_high | nan% | -41% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| GEN | weekly_drop | -29% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- OMC: incremental_roic_below_wacc
- VICI: nan
- ARE: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- CPT: nan
- BXP: nan
- CF: cyclical_revenue
- UDR: nan
- ELV: incremental_roic_below_wacc
- VMRK: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- GIS: elevated_leverage, thin_interest_coverage
- ADBE: heavy_sbc
- INVH: nan
- EOG: cyclical_revenue

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
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
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
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- APP AppLovin Corporation — material_event_requires_reunderwriting
- GEN Gen Digital Inc. — material_event_requires_reunderwriting
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
