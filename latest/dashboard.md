# Weekly US Stock Screen — 2026-10-09

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-10-09**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 515 | - |
| step2_hard_filters | 515 | 313 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 16 |
| step3_standardize | 313 | 313 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 313 | 304 | no_normalized_earnings: 9 |
| step5_quality_risk | 304 | 299 | - |
| step6_scenario_valuation | 299 | 274 | insufficient_post_valuation_model_confidence: 18, roic_not_meaningful:meaningless_capital: 5, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 333 | 333 | - |

## Eligible Candidates (7)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | VICI | 8.2% | 29.0% | 14.7% | 29.0% | 0.0% | 0% | 0.56 | 0.48 |
| 2 | ARE | 7.2% | 27.0% | 18.4% | 27.0% | 0.0% | 0% | 0.71 | 0.48 |
| 3 | UHS | 6.8% | 25.1% | 8.8% | 34.6% | 3.2% | 0% | 0.77 | 0.76 |
| 4 | CMCSA | 5.5% | 22.8% | 17.0% | 25.6% | 0.0% | 0% | 0.76 | 0.51 |
| 5 | BXP | 3.5% | 20.4% | 11.5% | 20.4% | 0.5% | 0% | 0.68 | 0.48 |
| 6 | FOXA | 2.5% | 22.8% | 7.0% | 31.5% | 5.0% | 0% | 0.90 | 0.69 |
| 7 | CPT | 1.3% | 20.6% | 9.2% | 20.6% | 2.8% | 0% | 0.61 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | VICI | 8.2% | 29.0% | 14.7% | 29.0% | 0.0% | 0% | 0.56 | 0.48 |
| 2 | ARE | 7.2% | 27.0% | 18.4% | 27.0% | 0.0% | 0% | 0.71 | 0.48 |
| 3 | UHS | 6.8% | 25.1% | 8.8% | 34.6% | 3.2% | 0% | 0.77 | 0.76 |
| 4 | CMCSA | 5.5% | 22.8% | 17.0% | 25.6% | 0.0% | 0% | 0.76 | 0.51 |
| 5 | BXP | 3.5% | 20.4% | 11.5% | 20.4% | 0.5% | 0% | 0.68 | 0.48 |
| 6 | FOXA | 2.5% | 22.8% | 7.0% | 31.5% | 5.0% | 0% | 0.90 | 0.69 |
| 7 | CPT | 1.3% | 20.6% | 9.2% | 20.6% | 2.8% | 0% | 0.61 | 0.48 |
| 8 | CF | -0.5% | 32.8% | 3.9% | 50.5% | 8.1% | 0% | 0.89 | 0.36 |
| 9 | VMRK | -3.6% | 16.7% | 6.2% | 20.6% | 5.8% | 0% | 0.62 | 0.48 |
| 10 | UDR | -4.1% | 17.7% | 5.2% | 17.7% | 6.8% | 0% | 0.57 | 0.48 |
| 11 | GIS | -4.2% | 19.8% | 2.0% | 29.0% | 10.0% | 0% | 0.80 | 0.74 |
| 12 | ELV | -4.4% | 9.7% | 7.6% | 15.6% | 4.4% | 0% | 0.81 | 0.67 |
| 13 | DECK | -5.1% | 15.2% | 4.5% | 22.1% | 7.5% | 0% | 0.96 | 0.75 |
| 14 | HUM | -7.3% | 13.5% | 3.8% | 21.1% | 8.2% | 0% | 0.75 | 0.62 |
| 15 | OMC | -7.6% | 12.3% | 4.2% | 18.1% | 7.8% | 0% | 0.82 | 0.61 |
| 16 | CTSH | -7.6% | 12.6% | 3.9% | 18.6% | 8.1% | 0% | 0.85 | 0.87 |
| 17 | ADBE | -8.1% | 12.8% | 3.2% | 18.7% | 8.8% | 0% | 0.98 | 0.79 |
| 18 | INVH | -8.2% | 13.5% | 3.1% | 13.5% | 8.9% | 0% | 0.62 | 0.48 |
| 19 | HST | -8.6% | 11.3% | 3.4% | 11.3% | 8.6% | 0% | 0.69 | 0.48 |
| 20 | MKC | -9.1% | 15.9% | -0.4% | 25.1% | 12.4% | 0% | 0.73 | 0.85 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CF | 30.0% | 32.8% | 3.9% | 50.5% | 75% | 150% |
| 2 | CI | 28.1% | 31.9% | -12.3% | 61.0% | 75% | 173% |
| 3 | VICI | 25.4% | 29.0% | 14.7% | 29.0% | 100% | 257% |
| 4 | ARE | 24.9% | 27.0% | 18.4% | 27.0% | 100% | 230% |
| 5 | UHS | 23.4% | 25.1% | 8.8% | 34.6% | 75% | 72% |
| 6 | CHTR | 22.8% | 54.4% | -95.0% | 77.4% | 75% | 397% |
| 7 | CMCSA | 22.0% | 22.8% | 17.0% | 25.6% | 100% | 91% |
| 8 | FOXA | 21.0% | 22.8% | 7.0% | 31.5% | 75% | 72% |
| 9 | BXP | 18.2% | 20.4% | 11.5% | 20.4% | 75% | 153% |
| 10 | CPT | 17.7% | 20.6% | 9.2% | 20.6% | 75% | 155% |
| 11 | GIS | 17.7% | 19.8% | 2.0% | 29.0% | 75% | 63% |
| 12 | FISV | 16.0% | 28.1% | -44.4% | 52.3% | 75% | 113% |
| 13 | VMRK | 15.0% | 16.7% | 6.2% | 20.6% | 75% | 116% |
| 14 | UDR | 14.6% | 17.7% | 5.2% | 17.7% | 75% | 126% |
| 15 | DECK | 14.3% | 15.2% | 4.5% | 22.1% | 75% | 19% |
| 16 | MKC | 14.1% | 15.9% | -0.4% | 25.1% | 75% | 38% |
| 17 | HUM | 13.0% | 13.5% | 3.8% | 21.1% | 75% | 26% |
| 18 | EOG | 12.9% | 13.2% | -4.7% | 30.0% | 75% | 28% |
| 19 | ZTS | 12.5% | 13.9% | 1.2% | 21.1% | 75% | 21% |
| 20 | CTSH | 11.9% | 12.6% | 3.9% | 18.6% | 75% | 12% |

## Week-over-week

Previous run: 2026-10-02

- Entered Robust Top: HST, MKC
- Exited Robust Top: MO, ZTS
- Entered Upside Top: CTSH
- Exited Upside Top: OMC

Largest robust-rank moves:

- AMGN: 146 → 105 (+41)
- VZ: 142 → 112 (+30)
- BMY: 81 → 110 (-29)
- CSGP: 132 → 157 (-25)
- PTC: 224 → 249 (-25)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.6% | 8.8% | 8.7% | 166.58 | 8.8% | 44% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 305.52 | 25.1% | 189% |
| UHS | bull | 25% | 11.4% | 12.1% | 19.5% | 431.53 | 34.6% | 316% |
| CMCSA | bear | 25% | -6.9% | 16.1% | 6.7% | 28.94 | 17.0% | 95% |
| CMCSA | base | 50% | 0.5% | 18.7% | 6.7% | 39.40 | 22.8% | 172% |
| CMCSA | bull | 25% | 6.3% | 20.4% | 6.7% | 49.40 | 25.6% | 248% |
| FOXA | bear | 25% | -1.4% | 17.3% | 7.7% | 60.26 | 7.0% | 35% |
| FOXA | base | 50% | 4.4% | 19.7% | 54.6% | 107.34 | 22.8% | 166% |
| FOXA | bull | 25% | 8.9% | 21.5% | 60.0% | 145.47 | 31.5% | 270% |
| CF | bear | 25% | -10.2% | 22.8% | 7.4% | 96.85 | 3.9% | 18% |
| CF | base | 50% | 11.8% | 31.1% | 17.9% | 279.17 | 32.8% | 294% |
| CF | bull | 25% | 29.4% | 38.4% | 19.1% | 556.91 | 50.5% | 668% |
| GIS | bear | 25% | -8.0% | 14.7% | 6.7% | 25.29 | 2.0% | 9% |
| GIS | base | 50% | -2.2% | 17.0% | 10.1% | 52.78 | 19.8% | 125% |
| GIS | bull | 25% | 2.4% | 18.6% | 11.0% | 76.22 | 29.0% | 227% |
| ELV | bear | 25% | -0.8% | 4.8% | 7.9% | 411.70 | 7.6% | 39% |
| ELV | base | 50% | 5.4% | 5.9% | 7.9% | 453.57 | 9.7% | 61% |
| ELV | bull | 25% | 10.4% | 6.6% | 7.9% | 592.13 | 15.6% | 110% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.6% | 66.66 | 4.5% | 21% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 98.38 | 15.2% | 95% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 124.88 | 22.1% | 157% |
| HUM | bear | 25% | 13.7% | 2.5% | 8.6% | 348.66 | 3.8% | 20% |
| HUM | base | 50% | 19.1% | 3.7% | 8.6% | 543.15 | 13.5% | 89% |
| HUM | bull | 25% | 23.5% | 4.8% | 8.6% | 752.86 | 21.1% | 163% |
| OMC | bear | 25% | 18.6% | 12.8% | 7.4% | 95.36 | 4.2% | 25% |
| OMC | base | 50% | 25.0% | 14.6% | 7.4% | 142.67 | 12.3% | 85% |
| OMC | bull | 25% | 30.1% | 15.9% | 7.4% | 185.70 | 18.1% | 140% |
| CTSH | bear | 25% | -0.4% | 12.8% | 9.2% | 47.53 | 3.9% | 18% |
| CTSH | base | 50% | 4.6% | 15.0% | 13.9% | 66.56 | 12.6% | 76% |
| CTSH | bull | 25% | 8.6% | 16.6% | 14.8% | 83.57 | 18.6% | 128% |
| ADBE | bear | 25% | 9.1% | 29.7% | 11.9% | 171.39 | 3.2% | 15% |
| ADBE | base | 50% | 13.6% | 33.6% | 58.7% | 246.05 | 12.8% | 77% |
| ADBE | bull | 25% | 17.1% | 36.9% | 59.8% | 303.60 | 18.7% | 125% |
| MKC | bear | 25% | 3.6% | 13.5% | 7.7% | 30.25 | -0.4% | -2% |
| MKC | base | 50% | 10.0% | 16.0% | 20.5% | 61.78 | 15.9% | 101% |
| MKC | bull | 25% | 15.0% | 17.7% | 24.0% | 89.52 | 25.1% | 192% |

## Boundary Assumptions & Valuation Alerts

- VICI — bounds: specialist_model_v1
- ARE — bounds: specialist_model_v1
- UHS — bounds: share_change_floor_hit
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;reinvestment_cap_hit
- BXP — bounds: specialist_model_v1
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit
- CPT — bounds: specialist_model_v1
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- VMRK — bounds: specialist_model_v1
- UDR — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- DECK — bounds: forward_roic_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- OMC — bounds: base_growth_cap_hit;share_change_cap_hit;reinvestment_cap_hit
- ADBE — bounds: share_change_floor_hit
- INVH — bounds: specialist_model_v1
- HST — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| FICO | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- VICI: nan
- ARE: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- BXP: nan
- CPT: nan
- CF: cyclical_revenue
- VMRK: nan
- UDR: nan
- GIS: elevated_leverage, thin_interest_coverage
- ELV: incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- OMC: ongoing_dilution, incremental_roic_below_wacc
- ADBE: heavy_sbc
- INVH: nan
- HST: nan
- MKC: thin_interest_coverage

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
- CME CME Group Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- FICO Fair Isaac Corporation — material_event_requires_reunderwriting
- XOM Exxonmobil Holdings Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- PSX Phillips 66 — insufficient_model_confidence
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
- APP AppLovin Corporation — insufficient_post_valuation_model_confidence
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
