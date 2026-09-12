# Weekly US Stock Screen — 2026-09-11

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-09-11**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 516 | - |
| step2_hard_filters | 516 | 312 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 16 |
| step3_standardize | 312 | 312 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 312 | 305 | no_normalized_earnings: 7 |
| step5_quality_risk | 305 | 300 | - |
| step6_scenario_valuation | 300 | 276 | insufficient_post_valuation_model_confidence: 17, roic_not_meaningful:meaningless_capital: 5, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 335 | 335 | - |

## Eligible Candidates (9)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OMC | 11.7% | 29.3% | 19.7% | 36.1% | 0.0% | 0% | 0.83 | 0.68 |
| 2 | TTD | 10.2% | 31.0% | 9.4% | 41.1% | 2.6% | 0% | 0.91 | 0.67 |
| 3 | UHS | 8.8% | 26.3% | 9.8% | 35.9% | 2.2% | 0% | 0.78 | 0.76 |
| 4 | VICI | 8.4% | 29.4% | 14.1% | 29.4% | 0.0% | 0% | 0.53 | 0.48 |
| 5 | ARE | 6.0% | 24.5% | 15.7% | 24.5% | 0.0% | 0% | 0.69 | 0.48 |
| 6 | CMCSA | 3.0% | 17.9% | 12.5% | 22.1% | 0.0% | 0% | 0.76 | 0.51 |
| 7 | BXP | 2.8% | 20.4% | 10.8% | 20.4% | 1.2% | 0% | 0.66 | 0.48 |
| 8 | FOXA | 2.8% | 23.4% | 6.9% | 32.3% | 5.1% | 0% | 0.90 | 0.69 |
| 9 | CPT | 2.7% | 22.4% | 9.7% | 22.4% | 2.3% | 0% | 0.58 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OMC | 11.7% | 29.3% | 19.7% | 36.1% | 0.0% | 0% | 0.83 | 0.68 |
| 2 | TTD | 10.2% | 31.0% | 9.4% | 41.1% | 2.6% | 0% | 0.91 | 0.67 |
| 3 | UHS | 8.8% | 26.3% | 9.8% | 35.9% | 2.2% | 0% | 0.78 | 0.76 |
| 4 | VICI | 8.4% | 29.4% | 14.1% | 29.4% | 0.0% | 0% | 0.53 | 0.48 |
| 5 | ARE | 6.0% | 24.5% | 15.7% | 24.5% | 0.0% | 0% | 0.69 | 0.48 |
| 6 | CMCSA | 3.0% | 17.9% | 12.5% | 22.1% | 0.0% | 0% | 0.76 | 0.51 |
| 7 | BXP | 2.8% | 20.4% | 10.8% | 20.4% | 1.2% | 0% | 0.66 | 0.48 |
| 8 | FOXA | 2.8% | 23.4% | 6.9% | 32.3% | 5.1% | 0% | 0.90 | 0.69 |
| 9 | CPT | 2.7% | 22.4% | 9.7% | 22.4% | 2.3% | 0% | 0.58 | 0.48 |
| 10 | UDR | -1.5% | 20.6% | 6.4% | 20.6% | 5.6% | 0% | 0.53 | 0.48 |
| 11 | DECK | -3.8% | 16.1% | 5.2% | 23.0% | 6.8% | 0% | 0.96 | 0.75 |
| 12 | VMRK | -3.8% | 17.0% | 5.8% | 21.3% | 6.2% | 0% | 0.60 | 0.48 |
| 13 | ELV | -4.0% | 10.3% | 8.0% | 16.2% | 4.0% | 0% | 0.82 | 0.67 |
| 14 | HUM | -4.5% | 15.3% | 5.4% | 23.1% | 6.6% | 0% | 0.76 | 0.62 |
| 15 | ZTS | -5.7% | 16.0% | 2.7% | 23.4% | 9.3% | 0% | 0.98 | 0.89 |
| 16 | CF | -5.9% | 28.4% | 0.1% | 46.4% | 11.9% | 0% | 0.89 | 0.36 |
| 17 | HST | -6.4% | 13.4% | 4.9% | 13.4% | 7.1% | 0% | 0.68 | 0.48 |
| 18 | GIS | -6.5% | 18.5% | 0.7% | 27.7% | 11.3% | 0% | 0.81 | 0.74 |
| 19 | CTSH | -6.5% | 13.4% | 4.3% | 19.6% | 7.7% | 0% | 0.85 | 0.87 |
| 20 | MO | -6.5% | 16.3% | 1.5% | 24.0% | 10.5% | 0% | 0.98 | 0.92 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CI | 30.1% | 33.8% | -10.7% | 63.4% | 75% | 196% |
| 2 | OMC | 28.6% | 29.3% | 19.7% | 36.1% | 100% | 165% |
| 3 | TTD | 28.1% | 31.0% | 9.4% | 41.1% | 75% | 115% |
| 4 | CF | 25.8% | 28.4% | 0.1% | 46.4% | 75% | 119% |
| 5 | VICI | 25.6% | 29.4% | 14.1% | 29.4% | 100% | 263% |
| 6 | UHS | 24.6% | 26.3% | 9.8% | 35.9% | 75% | 81% |
| 7 | ARE | 22.3% | 24.5% | 15.7% | 24.5% | 100% | 199% |
| 8 | EOG | 22.0% | 24.0% | -1.8% | 41.6% | 75% | 92% |
| 9 | FOXA | 21.5% | 23.4% | 6.9% | 32.3% | 75% | 80% |
| 10 | CPT | 19.2% | 22.4% | 9.7% | 22.4% | 75% | 175% |
| 11 | BXP | 18.0% | 20.4% | 10.8% | 20.4% | 75% | 153% |
| 12 | CMCSA | 17.6% | 17.9% | 12.5% | 22.1% | 100% | 58% |
| 13 | UDR | 17.0% | 20.6% | 6.4% | 20.6% | 75% | 155% |
| 14 | GIS | 16.3% | 18.5% | 0.7% | 27.7% | 75% | 57% |
| 15 | CHTR | 15.3% | 44.9% | -95.0% | 66.4% | 75% | 283% |
| 16 | VMRK | 15.3% | 17.0% | 5.8% | 21.3% | 75% | 119% |
| 17 | FISV | 15.2% | 26.0% | -40.8% | 49.8% | 75% | 99% |
| 18 | DECK | 15.1% | 16.1% | 5.2% | 23.0% | 75% | 23% |
| 19 | HUM | 14.8% | 15.3% | 5.4% | 23.1% | 75% | 38% |
| 20 | ZTS | 14.5% | 16.0% | 2.7% | 23.4% | 75% | 33% |

## Week-over-week

Previous run: 2026-09-04

- Entered Robust Top: GIS
- Exited Robust Top: INVH
- Entered Upside Top: DECK, ZTS
- Exited Upside Top: MO, TSN

Largest robust-rank moves:

- SWKS: 99 → 135 (-36)
- CARR: 298 → 328 (-30)
- CASY: 241 → 212 (+29)
- AMGN: 150 → 122 (+28)
- APA: 117 → 139 (-22)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| OMC | bear | 25% | 18.2% | 12.8% | 7.1% | 139.20 | 19.7% | 159% |
| OMC | base | 50% | 25.0% | 14.6% | 7.1% | 209.53 | 29.3% | 287% |
| OMC | bull | 25% | 30.5% | 15.9% | 7.1% | 274.41 | 36.1% | 404% |
| TTD | bear | 25% | 3.4% | 13.1% | 9.7% | 14.57 | 9.4% | 50% |
| TTD | base | 50% | 12.3% | 17.1% | 40.5% | 30.81 | 31.0% | 266% |
| TTD | bull | 25% | 19.4% | 20.7% | 43.5% | 42.71 | 41.1% | 419% |
| UHS | bear | 25% | 1.6% | 8.8% | 8.5% | 171.99 | 9.8% | 50% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 316.85 | 26.3% | 202% |
| UHS | bull | 25% | 11.4% | 12.1% | 19.5% | 448.20 | 35.9% | 336% |
| CMCSA | bear | 25% | -6.6% | 16.1% | 6.6% | 30.09 | 12.5% | 66% |
| CMCSA | base | 50% | 0.7% | 18.7% | 6.6% | 39.88 | 17.9% | 126% |
| CMCSA | bull | 25% | 6.6% | 20.4% | 6.6% | 51.37 | 22.1% | 195% |
| FOXA | bear | 25% | -1.3% | 17.3% | 7.2% | 64.68 | 6.9% | 34% |
| FOXA | base | 50% | 4.4% | 19.7% | 54.9% | 118.42 | 23.4% | 173% |
| FOXA | bull | 25% | 8.9% | 21.5% | 60.0% | 162.00 | 32.3% | 283% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.5% | 67.49 | 5.2% | 25% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 100.04 | 16.1% | 102% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 127.22 | 23.0% | 166% |
| ELV | bear | 25% | -0.7% | 4.8% | 7.6% | 429.53 | 8.0% | 42% |
| ELV | base | 50% | 5.5% | 5.9% | 7.6% | 479.40 | 10.3% | 65% |
| ELV | bull | 25% | 10.4% | 6.6% | 7.6% | 625.66 | 16.2% | 116% |
| HUM | bear | 25% | 13.7% | 2.5% | 8.3% | 362.52 | 5.4% | 30% |
| HUM | base | 50% | 19.1% | 3.7% | 8.3% | 566.16 | 15.3% | 105% |
| HUM | bull | 25% | 23.5% | 4.8% | 8.3% | 785.60 | 23.1% | 185% |
| ZTS | bear | 25% | -1.8% | 32.2% | 7.8% | 57.29 | 2.7% | 12% |
| ZTS | base | 50% | 2.8% | 36.0% | 24.3% | 97.20 | 16.0% | 103% |
| ZTS | bull | 25% | 6.4% | 39.1% | 24.5% | 128.42 | 23.4% | 174% |
| CF | bear | 25% | -10.4% | 22.8% | 7.1% | 99.18 | 0.1% | 0% |
| CF | base | 50% | 11.6% | 31.1% | 17.8% | 291.75 | 28.4% | 238% |
| CF | bull | 25% | 29.1% | 38.4% | 19.1% | 587.11 | 46.4% | 570% |
| GIS | bear | 25% | -8.0% | 14.7% | 6.5% | 26.86 | 0.7% | 3% |
| GIS | base | 50% | -2.2% | 17.0% | 10.1% | 56.37 | 18.5% | 115% |
| GIS | bull | 25% | 2.4% | 18.6% | 11.0% | 81.80 | 27.7% | 213% |
| CTSH | bear | 25% | -0.4% | 12.8% | 8.8% | 49.71 | 4.3% | 20% |
| CTSH | base | 50% | 4.6% | 15.0% | 13.9% | 70.64 | 13.4% | 82% |
| CTSH | bull | 25% | 8.6% | 16.6% | 14.8% | 89.27 | 19.6% | 137% |
| MO | bear | 25% | -2.3% | 48.7% | 7.0% | 53.54 | 1.5% | 7% |
| MO | base | 50% | 1.3% | 54.9% | 45.6% | 98.18 | 16.3% | 104% |
| MO | bull | 25% | 4.1% | 60.1% | 46.5% | 131.50 | 24.0% | 177% |

## Boundary Assumptions & Valuation Alerts

- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- TTD — bounds: intrinsic_2x_price
- UHS — bounds: share_change_floor_hit
- VICI — bounds: specialist_model_v1
- ARE — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;reinvestment_cap_hit
- BXP — bounds: specialist_model_v1
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit
- CPT — bounds: specialist_model_v1
- UDR — bounds: specialist_model_v1
- DECK — bounds: forward_roic_cap_hit
- VMRK — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- HST — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| WDC | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| APP | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- OMC: incremental_roic_below_wacc
- TTD: heavy_sbc
- VICI: nan
- ARE: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- BXP: nan
- CPT: nan
- UDR: nan
- VMRK: nan
- ELV: incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- CF: cyclical_revenue
- HST: nan
- GIS: elevated_leverage, thin_interest_coverage

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
- WDC Western Digital Corporation — material_event_requires_reunderwriting
- APP AppLovin Corporation — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- HLT Hilton Worldwide Holdings Inc. — insufficient_model_confidence
- DVN Devon Energy Corporation — insufficient_model_confidence
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
- MPC Marathon Petroleum Corporation — insufficient_post_valuation_model_confidence
- PSX Phillips 66 — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
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
