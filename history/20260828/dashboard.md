# Weekly US Stock Screen — 2026-08-28

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-08-28**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 517 | - |
| step2_hard_filters | 517 | 310 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 16 |
| step3_standardize | 310 | 310 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 310 | 302 | no_normalized_earnings: 8 |
| step5_quality_risk | 302 | 298 | - |
| step6_scenario_valuation | 298 | 272 | insufficient_post_valuation_model_confidence: 19, roic_not_meaningful:meaningless_capital: 5, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 331 | 331 | - |

## Eligible Candidates (9)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | TTD | 13.1% | 33.0% | 11.0% | 43.3% | 1.0% | 0% | 0.91 | 0.67 |
| 2 | UHS | 11.3% | 28.0% | 11.1% | 37.7% | 0.9% | 0% | 0.78 | 0.76 |
| 3 | OMC | 10.4% | 27.4% | 18.0% | 34.0% | 0.0% | 0% | 0.83 | 0.68 |
| 4 | VICI | 9.0% | 30.7% | 14.2% | 30.7% | 0.0% | 0% | 0.51 | 0.48 |
| 5 | ARE | 6.5% | 25.5% | 16.3% | 25.5% | 0.0% | 0% | 0.68 | 0.48 |
| 6 | CPT | 3.4% | 23.4% | 9.9% | 23.4% | 2.1% | 0% | 0.56 | 0.48 |
| 7 | FOXA | 2.9% | 23.7% | 6.8% | 32.8% | 5.2% | 0% | 0.91 | 0.69 |
| 8 | BXP | 1.8% | 19.9% | 10.0% | 19.9% | 2.0% | 0% | 0.65 | 0.48 |
| 9 | CMCSA | 1.4% | 16.7% | 11.2% | 21.1% | 0.8% | 0% | 0.76 | 0.46 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | TTD | 13.1% | 33.0% | 11.0% | 43.3% | 1.0% | 0% | 0.91 | 0.67 |
| 2 | UHS | 11.3% | 28.0% | 11.1% | 37.7% | 0.9% | 0% | 0.78 | 0.76 |
| 3 | OMC | 10.4% | 27.4% | 18.0% | 34.0% | 0.0% | 0% | 0.83 | 0.68 |
| 4 | VICI | 9.0% | 30.7% | 14.2% | 30.7% | 0.0% | 0% | 0.51 | 0.48 |
| 5 | ARE | 6.5% | 25.5% | 16.3% | 25.5% | 0.0% | 0% | 0.68 | 0.48 |
| 6 | CPT | 3.4% | 23.4% | 9.9% | 23.4% | 2.1% | 0% | 0.56 | 0.48 |
| 7 | FOXA | 2.9% | 23.7% | 6.8% | 32.8% | 5.2% | 0% | 0.91 | 0.69 |
| 8 | BXP | 1.8% | 19.9% | 10.0% | 19.9% | 2.0% | 0% | 0.65 | 0.48 |
| 9 | CMCSA | 1.4% | 16.7% | 11.2% | 21.1% | 0.8% | 0% | 0.76 | 0.46 |
| 10 | UDR | -1.3% | 21.4% | 6.2% | 21.4% | 5.8% | 0% | 0.51 | 0.48 |
| 11 | HUM | -1.6% | 17.4% | 7.1% | 25.4% | 4.9% | 0% | 0.76 | 0.61 |
| 12 | ELV | -1.6% | 12.4% | 10.1% | 18.4% | 1.9% | 0% | 0.82 | 0.67 |
| 13 | VMRK | -2.0% | 18.8% | 6.8% | 23.5% | 5.2% | 0% | 0.59 | 0.48 |
| 14 | CF | -2.5% | 31.7% | 2.3% | 50.0% | 9.7% | 0% | 0.89 | 0.36 |
| 15 | MO | -4.5% | 17.6% | 2.3% | 25.5% | 9.7% | 0% | 0.98 | 0.92 |
| 16 | HST | -5.7% | 14.1% | 5.3% | 14.1% | 6.7% | 0% | 0.67 | 0.48 |
| 17 | EOG | -6.3% | 26.2% | -0.2% | 44.3% | 12.2% | 0% | 0.87 | 0.41 |
| 18 | DECK | -6.9% | 14.2% | 3.5% | 21.1% | 8.5% | 0% | 0.96 | 0.75 |
| 19 | ZTS | -7.2% | 15.3% | 1.9% | 22.8% | 10.1% | 0% | 0.98 | 0.89 |
| 20 | INVH | -7.3% | 15.1% | 3.2% | 15.1% | 8.8% | 0% | 0.58 | 0.48 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CI | 31.8% | 35.5% | -9.3% | 65.6% | 75% | 218% |
| 2 | TTD | 30.1% | 33.0% | 11.0% | 43.3% | 75% | 131% |
| 3 | CF | 28.9% | 31.7% | 2.3% | 50.0% | 75% | 148% |
| 4 | OMC | 26.7% | 27.4% | 18.0% | 34.0% | 100% | 147% |
| 5 | VICI | 26.6% | 30.7% | 14.2% | 30.7% | 100% | 281% |
| 6 | UHS | 26.2% | 28.0% | 11.1% | 37.7% | 75% | 94% |
| 7 | EOG | 24.1% | 26.2% | -0.2% | 44.3% | 75% | 111% |
| 8 | ARE | 23.2% | 25.5% | 16.3% | 25.5% | 100% | 211% |
| 9 | FOXA | 21.8% | 23.7% | 6.8% | 32.8% | 75% | 84% |
| 10 | CPT | 20.0% | 23.4% | 9.9% | 23.4% | 75% | 186% |
| 11 | UDR | 17.6% | 21.4% | 6.2% | 21.4% | 75% | 163% |
| 12 | BXP | 17.4% | 19.9% | 10.0% | 19.9% | 75% | 148% |
| 13 | VMRK | 16.9% | 18.8% | 6.8% | 23.5% | 75% | 136% |
| 14 | HUM | 16.8% | 17.4% | 7.1% | 25.4% | 75% | 53% |
| 15 | FISV | 16.7% | 26.4% | -36.0% | 50.1% | 75% | 104% |
| 16 | CMCSA | 16.4% | 16.7% | 11.2% | 21.1% | 75% | 51% |
| 17 | CHTR | 15.9% | 45.8% | -95.0% | 67.0% | 75% | 298% |
| 18 | MO | 15.8% | 17.6% | 2.3% | 25.5% | 75% | 51% |
| 19 | ZTS | 13.8% | 15.3% | 1.9% | 22.8% | 75% | 31% |
| 20 | ELV | 13.3% | 12.4% | 10.1% | 18.4% | 75% | 28% |

## Week-over-week

Previous run: 2026-08-21

- Entered Robust Top: TTD
- Exited Robust Top: CTSH
- Entered Upside Top: TTD
- Exited Upside Top: GIS

Largest robust-rank moves:

- DE: 183 → 321 (-138)
- LOW: 110 → 153 (-43)
- URI: 252 → 231 (+21)
- DLTR: 312 → 296 (+16)
- CDW: 65 → 80 (-15)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| TTD | bear | 25% | 3.4% | 13.1% | 9.6% | 14.72 | 11.0% | 59% |
| TTD | base | 50% | 12.4% | 17.1% | 40.5% | 31.29 | 33.0% | 293% |
| TTD | bull | 25% | 19.5% | 20.7% | 43.5% | 43.42 | 43.3% | 458% |
| UHS | bear | 25% | 1.7% | 8.9% | 8.3% | 179.62 | 11.1% | 57% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 333.15 | 28.0% | 222% |
| UHS | bull | 25% | 11.4% | 12.1% | 19.5% | 472.34 | 37.7% | 365% |
| OMC | bear | 25% | 18.2% | 12.8% | 6.9% | 145.29 | 18.0% | 140% |
| OMC | base | 50% | 25.0% | 14.6% | 6.9% | 217.65 | 27.4% | 256% |
| OMC | bull | 25% | 30.4% | 15.9% | 6.9% | 284.47 | 34.0% | 363% |
| FOXA | bear | 25% | -1.3% | 17.3% | 6.9% | 67.63 | 6.8% | 34% |
| FOXA | base | 50% | 4.4% | 19.7% | 55.2% | 126.22 | 23.7% | 178% |
| FOXA | bull | 25% | 8.8% | 21.5% | 60.0% | 173.84 | 32.8% | 293% |
| CMCSA | bear | 25% | -6.6% | 16.1% | 6.5% | 30.89 | 11.2% | 58% |
| CMCSA | base | 50% | 0.7% | 18.7% | 6.5% | 40.90 | 16.7% | 115% |
| CMCSA | bull | 25% | 6.6% | 20.4% | 6.5% | 52.77 | 21.1% | 181% |
| HUM | bear | 25% | 13.4% | 2.5% | 8.1% | 373.00 | 7.1% | 41% |
| HUM | base | 50% | 19.1% | 3.7% | 8.1% | 588.80 | 17.4% | 124% |
| HUM | bull | 25% | 23.7% | 4.8% | 8.1% | 823.73 | 25.4% | 214% |
| ELV | bear | 25% | -0.7% | 4.9% | 7.3% | 446.73 | 10.1% | 55% |
| ELV | base | 50% | 5.4% | 5.9% | 7.3% | 503.05 | 12.4% | 82% |
| ELV | bull | 25% | 10.4% | 6.6% | 7.3% | 656.31 | 18.4% | 137% |
| CF | bear | 25% | -10.0% | 22.8% | 6.9% | 104.11 | 2.3% | 10% |
| CF | base | 50% | 12.0% | 31.1% | 17.8% | 311.79 | 31.7% | 281% |
| CF | bull | 25% | 29.6% | 38.4% | 19.1% | 633.84 | 50.0% | 658% |
| MO | bear | 25% | -2.3% | 48.7% | 6.8% | 55.73 | 2.3% | 11% |
| MO | base | 50% | 1.3% | 54.9% | 45.6% | 103.93 | 17.6% | 115% |
| MO | bull | 25% | 4.1% | 60.1% | 46.5% | 140.04 | 25.5% | 194% |
| EOG | bear | 25% | -7.7% | 22.6% | 7.0% | 106.01 | -0.2% | -1% |
| EOG | base | 50% | 14.0% | 32.4% | 14.3% | 302.58 | 26.2% | 213% |
| EOG | bull | 25% | 31.4% | 41.1% | 15.4% | 620.66 | 44.3% | 537% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.3% | 68.26 | 3.5% | 16% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 101.60 | 14.2% | 88% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 129.42 | 21.1% | 148% |
| ZTS | bear | 25% | -1.8% | 32.2% | 7.6% | 59.09 | 1.9% | 8% |
| ZTS | base | 50% | 2.8% | 36.0% | 24.3% | 101.27 | 15.3% | 97% |
| ZTS | bull | 25% | 6.4% | 39.1% | 24.5% | 134.26 | 22.8% | 168% |

## Boundary Assumptions & Valuation Alerts

- TTD — bounds: intrinsic_2x_price
- UHS — bounds: share_change_floor_hit
- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- ARE — bounds: specialist_model_v1
- CPT — bounds: specialist_model_v1
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit
- BXP — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- UDR — bounds: specialist_model_v1
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- VMRK — bounds: specialist_model_v1
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- HST — bounds: specialist_model_v1
- EOG — bounds: reinvestment_cap_hit;intrinsic_2x_price
- DECK — bounds: forward_roic_cap_hit
- INVH — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| GLW | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| KLAC | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| APP | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| ON | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- TTD: heavy_sbc
- OMC: incremental_roic_below_wacc
- VICI: nan
- ARE: nan
- CPT: nan
- BXP: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- UDR: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- ELV: incremental_roic_below_wacc
- VMRK: nan
- CF: cyclical_revenue
- HST: nan
- EOG: cyclical_revenue
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
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- GLW Corning Inc — material_event_requires_reunderwriting
- KLAC KLA Corporation — material_event_requires_reunderwriting
- APP AppLovin Corporation — material_event_requires_reunderwriting
- ON ON Semiconductor Corporation — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- HLT Hilton Worldwide Holdings Inc. — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- GM General Motors Company — irr_below_solver_bound
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- EXPE Expedia Group, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- CVX Chevron Corporation — insufficient_post_valuation_model_confidence
- COP ConocoPhillips — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_post_valuation_model_confidence
- PSX Phillips 66 — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- TRGP Targa Resources Corp. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- DVN Devon Energy Corporation — insufficient_post_valuation_model_confidence
- XYZ Block, Inc. — insufficient_post_valuation_model_confidence
- IR Ingersoll Rand Inc. — insufficient_post_valuation_model_confidence
- IFF International Flavors & Fragrances Inc. — insufficient_post_valuation_model_confidence
- BLDR Builders FirstSource, Inc. — insufficient_post_valuation_model_confidence
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
