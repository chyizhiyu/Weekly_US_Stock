# Weekly US Stock Screen — 2026-08-07

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-08-07**
- Fresh price coverage: **99.8%** (1 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 515 | - |
| step2_hard_filters | 515 | 306 | adr_excluded: 33, persistent_negative_fcf: 23, interest_coverage: 18 |
| step3_standardize | 306 | 306 | - |
| step4_specialist_models | 92 | 57 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 306 | 298 | no_normalized_earnings: 7, normalization_failed: 1 |
| step5_quality_risk | 298 | 290 | - |
| step6_scenario_valuation | 290 | 264 | insufficient_post_valuation_model_confidence: 18, roic_not_meaningful:meaningless_capital: 5, irr_below_solver_bound: 2 |
| step7_risk_adjusted_ranking | 321 | 321 | - |

## Eligible Candidates (9)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | WAT | 47.4% | 102.8% | 80.7% | 116.5% | 0.0% | 0% | 0.74 | 0.52 |
| 2 | OMC | 11.3% | 28.7% | 19.3% | 35.4% | 0.0% | 0% | 0.83 | 0.68 |
| 3 | UHS | 11.1% | 27.8% | 11.0% | 37.4% | 1.0% | 0% | 0.78 | 0.77 |
| 4 | VICI | 9.1% | 31.1% | 14.0% | 31.1% | 0.0% | 0% | 0.50 | 0.48 |
| 5 | ZTS | 7.1% | 22.6% | 10.5% | 29.2% | 1.5% | 0% | 0.98 | 0.81 |
| 6 | ARE | 6.9% | 26.5% | 17.1% | 26.5% | 0.0% | 0% | 0.68 | 0.48 |
| 7 | FOXA | 6.4% | 26.0% | 8.7% | 35.3% | 3.3% | 0% | 0.91 | 0.69 |
| 8 | CMCSA | 2.9% | 18.3% | 13.0% | 22.6% | 0.0% | 0% | 0.76 | 0.46 |
| 9 | BXP | 2.1% | 20.3% | 10.2% | 20.3% | 1.8% | 0% | 0.65 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | WAT | 47.4% | 102.8% | 80.7% | 116.5% | 0.0% | 0% | 0.74 | 0.52 |
| 2 | OMC | 11.3% | 28.7% | 19.3% | 35.4% | 0.0% | 0% | 0.83 | 0.68 |
| 3 | UHS | 11.1% | 27.8% | 11.0% | 37.4% | 1.0% | 0% | 0.78 | 0.77 |
| 4 | VICI | 9.1% | 31.1% | 14.0% | 31.1% | 0.0% | 0% | 0.50 | 0.48 |
| 5 | ZTS | 7.1% | 22.6% | 10.5% | 29.2% | 1.5% | 0% | 0.98 | 0.81 |
| 6 | ARE | 6.9% | 26.5% | 17.1% | 26.5% | 0.0% | 0% | 0.68 | 0.48 |
| 7 | FOXA | 6.4% | 26.0% | 8.7% | 35.3% | 3.3% | 0% | 0.91 | 0.69 |
| 8 | CMCSA | 2.9% | 18.3% | 13.0% | 22.6% | 0.0% | 0% | 0.76 | 0.46 |
| 9 | BXP | 2.1% | 20.3% | 10.2% | 20.3% | 1.8% | 0% | 0.65 | 0.48 |
| 10 | AVB | -0.8% | 20.7% | 7.1% | 20.7% | 4.9% | 0% | 0.55 | 0.48 |
| 11 | HUM | -0.8% | 17.9% | 7.5% | 26.0% | 4.5% | 0% | 0.76 | 0.61 |
| 12 | ELV | -1.1% | 12.7% | 10.5% | 18.7% | 1.5% | 0% | 0.82 | 0.67 |
| 13 | UDR | -1.8% | 21.2% | 5.8% | 21.2% | 6.2% | 0% | 0.51 | 0.48 |
| 14 | EQR | -2.4% | 18.6% | 6.5% | 23.4% | 5.5% | 0% | 0.58 | 0.48 |
| 15 | MO | -3.6% | 18.2% | 2.7% | 26.1% | 9.3% | 0% | 0.98 | 0.93 |
| 16 | CTSH | -3.6% | 15.1% | 5.6% | 21.4% | 6.4% | 0% | 0.85 | 0.87 |
| 17 | EOG | -5.0% | 28.0% | 0.5% | 46.4% | 11.5% | 0% | 0.87 | 0.41 |
| 18 | HST | -6.5% | 13.5% | 4.7% | 13.5% | 7.3% | 0% | 0.67 | 0.48 |
| 19 | GIS | -7.5% | 18.1% | 0.5% | 27.3% | 11.5% | 0% | 0.81 | 0.67 |
| 20 | INVH | -8.1% | 14.6% | 2.7% | 14.6% | 9.3% | 0% | 0.58 | 0.48 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | WAT | 100.7% | 102.8% | 80.7% | 116.5% | 100% | 23213% |
| 2 | OMC | 28.0% | 28.7% | 19.3% | 35.4% | 100% | 162% |
| 3 | VICI | 26.8% | 31.1% | 14.0% | 31.1% | 100% | 287% |
| 4 | UHS | 26.0% | 27.8% | 11.0% | 37.4% | 75% | 93% |
| 5 | EOG | 25.7% | 28.0% | 0.5% | 46.4% | 75% | 125% |
| 6 | ARE | 24.1% | 26.5% | 17.1% | 26.5% | 100% | 223% |
| 7 | FOXA | 24.0% | 26.0% | 8.7% | 35.3% | 75% | 100% |
| 8 | ZTS | 21.2% | 22.6% | 10.5% | 29.2% | 75% | 68% |
| 9 | FISV | 19.5% | 28.0% | -29.6% | 51.5% | 75% | 117% |
| 10 | CMCSA | 18.0% | 18.3% | 13.0% | 22.6% | 100% | 61% |
| 11 | BXP | 17.7% | 20.3% | 10.2% | 20.3% | 75% | 152% |
| 12 | UDR | 17.4% | 21.2% | 5.8% | 21.2% | 75% | 162% |
| 13 | HUM | 17.3% | 17.9% | 7.5% | 26.0% | 75% | 57% |
| 14 | AVB | 17.3% | 20.7% | 7.1% | 20.7% | 75% | 156% |
| 15 | CHTR | 17.0% | 47.4% | -95.0% | 68.3% | 75% | 316% |
| 16 | EQR | 16.7% | 18.6% | 6.5% | 23.4% | 75% | 134% |
| 17 | MO | 16.3% | 18.2% | 2.7% | 26.1% | 75% | 55% |
| 18 | GIS | 16.0% | 18.1% | 0.5% | 27.3% | 75% | 55% |
| 19 | CTSH | 14.3% | 15.1% | 5.6% | 21.4% | 75% | 26% |
| 20 | ELV | 13.7% | 12.7% | 10.5% | 18.7% | 75% | 30% |

## Week-over-week

Previous run: 2026-07-31

- Entered Robust Top: EOG, HST, INVH, WAT
- Exited Robust Top: CPAY, CPT, HPQ, TTD
- Entered Upside Top: CTSH, ELV, MO, WAT, ZTS
- Exited Upside Top: APA, CI, CPT, REGN, TTD

Largest robust-rank moves:

- WAT: 228 → 1 (+227)
- FIS: 107 → 303 (-196)
- ADM: 282 → 108 (+174)
- PCAR: 132 → 234 (-102)
- BALL: 308 → 211 (+97)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| WAT | bear | 25% | 17.9% | 25.0% | 10.2% | 53365.85 | 80.7% | 24677% |
| WAT | base | 50% | 25.0% | 28.8% | 10.2% | 94852.97 | 102.8% | 41400% |
| WAT | bull | 25% | 30.7% | 31.1% | 10.2% | 130468.01 | 116.5% | 55748% |
| OMC | bear | 25% | 18.2% | 12.8% | 6.8% | 149.59 | 19.3% | 154% |
| OMC | base | 50% | 25.0% | 14.6% | 6.8% | 223.38 | 28.7% | 276% |
| OMC | bull | 25% | 30.4% | 15.9% | 6.8% | 291.55 | 35.4% | 388% |
| UHS | bear | 25% | 1.8% | 8.9% | 8.3% | 181.03 | 11.0% | 57% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 334.71 | 27.8% | 219% |
| UHS | bull | 25% | 11.3% | 12.1% | 19.5% | 473.15 | 37.4% | 360% |
| ZTS | bear | 25% | 0.9% | 32.2% | 8.4% | 79.36 | 10.5% | 54% |
| ZTS | base | 50% | 5.1% | 36.0% | 59.2% | 121.74 | 22.6% | 159% |
| ZTS | bull | 25% | 8.4% | 39.1% | 60.0% | 153.29 | 29.2% | 232% |
| FOXA | bear | 25% | -1.2% | 17.3% | 6.9% | 68.39 | 8.7% | 44% |
| FOXA | base | 50% | 4.4% | 19.7% | 55.2% | 128.29 | 26.0% | 203% |
| FOXA | bull | 25% | 8.8% | 21.5% | 60.0% | 177.02 | 35.3% | 328% |
| CMCSA | bear | 25% | -6.6% | 16.1% | 6.5% | 30.91 | 13.0% | 69% |
| CMCSA | base | 50% | 0.8% | 18.7% | 6.5% | 40.87 | 18.3% | 130% |
| CMCSA | bull | 25% | 6.6% | 20.4% | 6.5% | 52.80 | 22.6% | 201% |
| HUM | bear | 25% | 13.4% | 2.5% | 7.9% | 382.45 | 7.5% | 44% |
| HUM | base | 50% | 19.2% | 3.7% | 7.9% | 604.65 | 17.9% | 129% |
| HUM | bull | 25% | 23.7% | 4.8% | 7.9% | 846.46 | 26.0% | 221% |
| ELV | bear | 25% | -0.7% | 4.9% | 7.2% | 454.10 | 10.5% | 57% |
| ELV | base | 50% | 5.4% | 5.9% | 7.2% | 512.81 | 12.7% | 84% |
| ELV | bull | 25% | 10.3% | 6.6% | 7.2% | 668.99 | 18.7% | 141% |
| MO | bear | 25% | -2.2% | 48.7% | 6.7% | 56.65 | 2.7% | 13% |
| MO | base | 50% | 1.3% | 54.9% | 45.6% | 106.00 | 18.2% | 120% |
| MO | bull | 25% | 4.0% | 60.1% | 46.5% | 142.85 | 26.1% | 201% |
| CTSH | bear | 25% | -0.4% | 12.8% | 8.6% | 50.87 | 5.6% | 27% |
| CTSH | base | 50% | 4.6% | 15.0% | 13.9% | 72.85 | 15.1% | 95% |
| CTSH | bull | 25% | 8.6% | 16.6% | 14.8% | 92.37 | 21.4% | 155% |
| EOG | bear | 25% | -9.1% | 22.6% | 6.9% | 103.06 | 0.5% | 2% |
| EOG | base | 50% | 13.1% | 32.4% | 14.3% | 303.47 | 28.0% | 235% |
| EOG | bull | 25% | 30.8% | 41.1% | 15.4% | 629.27 | 46.4% | 586% |
| GIS | bear | 25% | -8.0% | 14.7% | 6.5% | 27.15 | 0.5% | 2% |
| GIS | base | 50% | -2.2% | 17.0% | 10.1% | 57.05 | 18.1% | 112% |
| GIS | bull | 25% | 2.4% | 18.6% | 11.0% | 82.87 | 27.3% | 208% |

## Boundary Assumptions & Valuation Alerts

- WAT ⚠ manual review — bounds: base_growth_cap_hit;share_change_floor_hit;reinvestment_cap_hit; alerts: intrinsic_3x_price;median_irr_extreme;bull_return_extreme
- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- UHS — bounds: share_change_floor_hit
- VICI — bounds: specialist_model_v1
- ZTS — bounds: forward_roic_cap_hit
- ARE — bounds: specialist_model_v1
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit;intrinsic_2x_price
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- BXP — bounds: specialist_model_v1
- AVB — bounds: specialist_model_v1
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- UDR — bounds: specialist_model_v1
- EQR — bounds: specialist_model_v1
- EOG — bounds: reinvestment_cap_hit;intrinsic_2x_price
- HST — bounds: specialist_model_v1
- GIS — bounds: wacc_floor_hit
- INVH — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| ORCL | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SNDK | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| WDC | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| APP | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| TTD | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- WAT: elevated_leverage, thin_interest_coverage, incremental_roic_below_wacc
- OMC: incremental_roic_below_wacc
- VICI: nan
- ARE: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- BXP: nan
- AVB: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- ELV: incremental_roic_below_wacc
- UDR: nan
- EQR: nan
- EOG: cyclical_revenue
- HST: nan
- GIS: elevated_leverage, thin_interest_coverage
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
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- ARES Ares Management Corporation — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
- RJF Raymond James Financial, Inc. — asset_management_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- BEN Franklin Resources, Inc. — asset_management_model_not_supported
- IVZ Invesco Ltd. — asset_management_model_not_supported
- FDS FactSet Research Systems Inc. — financial_sector_model_not_supported
- CME CME Group Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- ORCL Oracle Corporation — material_event_requires_reunderwriting
- SNDK Sandisk Corporation — material_event_requires_reunderwriting
- WDC Western Digital Corporation — material_event_requires_reunderwriting
- APP AppLovin Corporation — material_event_requires_reunderwriting
- TTD The Trade Desk, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_model_confidence
- XYZ Block, Inc. — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- NRG NRG Energy, Inc. — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- TSLA Tesla, Inc. — insufficient_model_confidence
- PH Parker-Hannifin Corporation — irr_below_solver_bound
- GM General Motors Company — irr_below_solver_bound
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- EXPE Expedia Group, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- COP ConocoPhillips — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- VLO Valero Energy Corporation — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- PSX Phillips 66 — insufficient_post_valuation_model_confidence
- CI Cigna Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- TRGP Targa Resources Corp. — insufficient_post_valuation_model_confidence
- IR Ingersoll Rand Inc. — insufficient_post_valuation_model_confidence
- DVN Devon Energy Corporation — insufficient_post_valuation_model_confidence
- IFF International Flavors & Fragrances Inc. — insufficient_post_valuation_model_confidence
- CF CF Industries Holdings, Inc. — insufficient_post_valuation_model_confidence
- BLDR Builders FirstSource, Inc. — insufficient_post_valuation_model_confidence
- NVDA NVIDIA Corporation — insufficient_post_valuation_model_confidence
- AMD Advanced Micro Devices, Inc. — insufficient_post_valuation_model_confidence
- STLD Steel Dynamics, Inc. — insufficient_post_valuation_model_confidence
- APA APA Corporation — insufficient_post_valuation_model_confidence

## Data Gaps and Model Limitations

- Stocks missing core financials were rejected (fail closed), never estimated.
- Banks, insurers and REITs use conservative specialist models; rows with
  incomplete specialist inputs stay watchlisted instead of entering ranking.
- Asset managers, consumer-finance names, other financials and pre-profit
  biotech remain watchlisted until dedicated models exist.
- Scenario set is discrete (bear/base/bull); worst-case stress metrics are
  deterministic bear/base/bull stress labels, not calibrated CVaR.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
