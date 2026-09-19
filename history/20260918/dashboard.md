# Weekly US Stock Screen — 2026-09-18

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-09-18**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 516 | - |
| step2_hard_filters | 516 | 311 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 16 |
| step3_standardize | 311 | 311 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 311 | 304 | no_normalized_earnings: 7 |
| step5_quality_risk | 304 | 299 | - |
| step6_scenario_valuation | 299 | 274 | insufficient_post_valuation_model_confidence: 18, roic_not_meaningful:meaningless_capital: 5, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 333 | 333 | - |

## Eligible Candidates (9)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OMC | 12.2% | 29.9% | 20.5% | 36.6% | 0.0% | 0% | 0.83 | 0.68 |
| 2 | TTD | 11.5% | 31.8% | 10.2% | 41.8% | 1.8% | 0% | 0.91 | 0.67 |
| 3 | VICI | 8.7% | 30.0% | 14.8% | 30.0% | 0.0% | 0% | 0.54 | 0.48 |
| 4 | UHS | 7.8% | 25.7% | 9.3% | 35.3% | 2.7% | 0% | 0.78 | 0.76 |
| 5 | ARE | 5.4% | 23.2% | 14.6% | 23.2% | 0.0% | 0% | 0.69 | 0.48 |
| 6 | CMCSA | 4.5% | 20.8% | 15.4% | 24.5% | 0.0% | 0% | 0.76 | 0.51 |
| 7 | CPT | 3.6% | 22.9% | 10.3% | 22.9% | 1.7% | 0% | 0.58 | 0.48 |
| 8 | FOXA | 3.6% | 23.9% | 7.4% | 32.8% | 4.6% | 0% | 0.90 | 0.69 |
| 9 | BXP | 3.3% | 20.7% | 11.1% | 20.7% | 0.9% | 0% | 0.66 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OMC | 12.2% | 29.9% | 20.5% | 36.6% | 0.0% | 0% | 0.83 | 0.68 |
| 2 | TTD | 11.5% | 31.8% | 10.2% | 41.8% | 1.8% | 0% | 0.91 | 0.67 |
| 3 | VICI | 8.7% | 30.0% | 14.8% | 30.0% | 0.0% | 0% | 0.54 | 0.48 |
| 4 | UHS | 7.8% | 25.7% | 9.3% | 35.3% | 2.7% | 0% | 0.78 | 0.76 |
| 5 | ARE | 5.4% | 23.2% | 14.6% | 23.2% | 0.0% | 0% | 0.69 | 0.48 |
| 6 | CMCSA | 4.5% | 20.8% | 15.4% | 24.5% | 0.0% | 0% | 0.76 | 0.51 |
| 7 | CPT | 3.6% | 22.9% | 10.3% | 22.9% | 1.7% | 0% | 0.58 | 0.48 |
| 8 | FOXA | 3.6% | 23.9% | 7.4% | 32.8% | 4.6% | 0% | 0.90 | 0.69 |
| 9 | BXP | 3.3% | 20.7% | 11.1% | 20.7% | 0.9% | 0% | 0.66 | 0.48 |
| 10 | UDR | -0.8% | 21.0% | 6.9% | 21.0% | 5.1% | 0% | 0.54 | 0.48 |
| 11 | VMRK | -1.9% | 18.2% | 7.1% | 22.5% | 4.9% | 0% | 0.61 | 0.48 |
| 12 | DECK | -2.3% | 17.0% | 6.0% | 24.0% | 6.0% | 0% | 0.96 | 0.75 |
| 13 | HUM | -2.5% | 16.6% | 6.6% | 24.4% | 5.4% | 0% | 0.76 | 0.62 |
| 14 | ELV | -3.6% | 10.6% | 8.4% | 16.5% | 3.6% | 0% | 0.82 | 0.67 |
| 15 | CF | -4.5% | 29.6% | 1.0% | 47.5% | 11.0% | 0% | 0.89 | 0.36 |
| 16 | ZTS | -4.9% | 16.4% | 3.1% | 23.9% | 8.9% | 0% | 0.98 | 0.89 |
| 17 | HST | -6.1% | 13.6% | 5.2% | 13.6% | 6.8% | 0% | 0.68 | 0.48 |
| 18 | CTSH | -6.6% | 13.3% | 4.2% | 19.5% | 7.8% | 0% | 0.85 | 0.87 |
| 19 | INVH | -6.6% | 15.0% | 3.9% | 15.0% | 8.1% | 0% | 0.60 | 0.48 |
| 20 | LEN | -7.0% | 12.9% | 4.7% | 21.5% | 7.3% | 0% | 0.49 | 0.36 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CI | 30.3% | 34.1% | -10.5% | 63.7% | 75% | 199% |
| 2 | OMC | 29.2% | 29.9% | 20.5% | 36.6% | 100% | 172% |
| 3 | TTD | 28.9% | 31.8% | 10.2% | 41.8% | 75% | 120% |
| 4 | CF | 26.9% | 29.6% | 1.0% | 47.5% | 75% | 127% |
| 5 | VICI | 26.2% | 30.0% | 14.8% | 30.0% | 100% | 272% |
| 6 | UHS | 24.0% | 25.7% | 9.3% | 35.3% | 75% | 77% |
| 7 | EOG | 22.3% | 24.5% | -3.5% | 43.6% | 75% | 96% |
| 8 | FOXA | 22.0% | 23.9% | 7.4% | 32.8% | 75% | 82% |
| 9 | ARE | 21.1% | 23.2% | 14.6% | 23.2% | 100% | 184% |
| 10 | CMCSA | 20.3% | 20.8% | 15.4% | 24.5% | 100% | 78% |
| 11 | CPT | 19.8% | 22.9% | 10.3% | 22.9% | 75% | 181% |
| 12 | CHTR | 18.5% | 49.0% | -95.0% | 71.0% | 75% | 332% |
| 13 | BXP | 18.3% | 20.7% | 11.1% | 20.7% | 75% | 156% |
| 14 | FISV | 17.7% | 28.3% | -38.3% | 52.4% | 75% | 117% |
| 15 | UDR | 17.4% | 21.0% | 6.9% | 21.0% | 75% | 159% |
| 16 | VMRK | 16.5% | 18.2% | 7.1% | 22.5% | 75% | 131% |
| 17 | HUM | 16.1% | 16.6% | 6.6% | 24.4% | 75% | 46% |
| 18 | DECK | 16.0% | 17.0% | 6.0% | 24.0% | 75% | 27% |
| 19 | GIS | 15.6% | 17.7% | 0.1% | 26.9% | 75% | 52% |
| 20 | ZTS | 15.0% | 16.4% | 3.1% | 23.9% | 75% | 35% |

## Week-over-week

Previous run: 2026-09-11

- Entered Robust Top: INVH, LEN
- Exited Robust Top: GIS, MO
- Entered Upside Top: none
- Exited Upside Top: none

Largest robust-rank moves:

- CARR: 328 → 297 (+31)
- CPRT: 58 → 35 (+23)
- JBHT: 220 → 201 (+19)
- FISV: 268 → 252 (+16)
- TPL: 146 → 133 (+13)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| OMC | bear | 25% | 18.5% | 12.8% | 7.1% | 140.05 | 20.5% | 170% |
| OMC | base | 50% | 25.0% | 14.6% | 7.1% | 208.58 | 29.9% | 298% |
| OMC | bull | 25% | 30.2% | 15.9% | 7.1% | 271.22 | 36.6% | 414% |
| TTD | bear | 25% | 3.5% | 13.1% | 9.7% | 14.56 | 10.2% | 54% |
| TTD | base | 50% | 12.2% | 17.1% | 40.5% | 30.61 | 31.8% | 276% |
| TTD | bull | 25% | 19.2% | 20.7% | 43.5% | 42.22 | 41.8% | 430% |
| UHS | bear | 25% | 1.6% | 8.8% | 8.6% | 170.10 | 9.3% | 47% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 312.86 | 25.7% | 196% |
| UHS | bull | 25% | 11.4% | 12.1% | 19.5% | 442.32 | 35.3% | 327% |
| CMCSA | bear | 25% | -6.7% | 16.1% | 6.5% | 30.36 | 15.4% | 85% |
| CMCSA | base | 50% | 0.6% | 18.7% | 6.5% | 40.57 | 20.8% | 153% |
| CMCSA | bull | 25% | 6.5% | 20.4% | 6.5% | 51.85 | 24.5% | 229% |
| FOXA | bear | 25% | -1.3% | 17.3% | 7.2% | 64.30 | 7.4% | 37% |
| FOXA | base | 50% | 4.4% | 19.7% | 54.9% | 117.44 | 23.9% | 178% |
| FOXA | bull | 25% | 8.9% | 21.5% | 60.0% | 160.53 | 32.8% | 289% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.5% | 67.25 | 6.0% | 29% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 99.55 | 17.0% | 109% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 126.53 | 24.0% | 175% |
| HUM | bear | 25% | 13.7% | 2.5% | 8.3% | 360.98 | 6.6% | 38% |
| HUM | base | 50% | 19.1% | 3.7% | 8.3% | 563.59 | 16.6% | 117% |
| HUM | bull | 25% | 23.5% | 4.8% | 8.3% | 781.94 | 24.4% | 202% |
| ELV | bear | 25% | -0.7% | 4.8% | 7.6% | 427.43 | 8.4% | 44% |
| ELV | base | 50% | 5.5% | 5.9% | 7.6% | 476.44 | 10.6% | 67% |
| ELV | bull | 25% | 10.4% | 6.6% | 7.6% | 621.82 | 16.5% | 119% |
| CF | bear | 25% | -10.3% | 22.8% | 7.2% | 99.11 | 1.0% | 5% |
| CF | base | 50% | 11.7% | 31.1% | 17.9% | 290.41 | 29.6% | 252% |
| CF | bull | 25% | 29.3% | 38.4% | 19.1% | 583.77 | 47.5% | 595% |
| ZTS | bear | 25% | -1.8% | 32.2% | 7.9% | 56.95 | 3.1% | 14% |
| ZTS | base | 50% | 2.8% | 36.0% | 24.3% | 96.45 | 16.4% | 106% |
| ZTS | bull | 25% | 6.4% | 39.1% | 24.5% | 127.37 | 23.9% | 179% |
| CTSH | bear | 25% | -0.4% | 12.8% | 8.9% | 49.41 | 4.2% | 20% |
| CTSH | base | 50% | 4.6% | 15.0% | 13.9% | 70.08 | 13.3% | 81% |
| CTSH | bull | 25% | 8.6% | 16.6% | 14.8% | 88.49 | 19.5% | 136% |
| LEN | bear | 25% | -10.4% | 9.7% | 10.2% | 59.90 | 4.7% | 21% |
| LEN | base | 50% | 1.3% | 13.8% | 10.2% | 83.88 | 12.9% | 84% |
| LEN | bull | 25% | 10.7% | 16.7% | 10.2% | 126.03 | 21.5% | 178% |

## Boundary Assumptions & Valuation Alerts

- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- TTD — bounds: intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- UHS — bounds: share_change_floor_hit
- ARE — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;reinvestment_cap_hit
- CPT — bounds: specialist_model_v1
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit
- BXP — bounds: specialist_model_v1
- UDR — bounds: specialist_model_v1
- VMRK — bounds: specialist_model_v1
- DECK — bounds: forward_roic_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- HST — bounds: specialist_model_v1
- INVH — bounds: specialist_model_v1
- LEN — bounds: forward_roic_floor_hit;reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| GLW | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| APP | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| ON | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- OMC: incremental_roic_below_wacc
- TTD: heavy_sbc
- VICI: nan
- ARE: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- CPT: nan
- BXP: nan
- UDR: nan
- VMRK: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- ELV: incremental_roic_below_wacc
- CF: cyclical_revenue
- HST: nan
- INVH: nan
- LEN: weak_cash_conversion, incremental_roic_below_wacc

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
- GLW Corning Inc — material_event_requires_reunderwriting
- APP AppLovin Corporation — material_event_requires_reunderwriting
- ON ON Semiconductor Corporation — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- PSX Phillips 66 — insufficient_model_confidence
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
