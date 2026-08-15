# Weekly US Stock Screen — 2026-08-14

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-08-14**
- Fresh price coverage: **99.8%** (1 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 518 | - |
| step2_hard_filters | 518 | 310 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 17 |
| step3_standardize | 310 | 310 | - |
| step4_specialist_models | 95 | 60 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 310 | 302 | no_normalized_earnings: 8 |
| step5_quality_risk | 302 | 294 | - |
| step6_scenario_valuation | 294 | 269 | insufficient_post_valuation_model_confidence: 18, roic_not_meaningful:meaningless_capital: 5, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 329 | 329 | - |

## Eligible Candidates (9)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | TTD | 17.1% | 36.0% | 14.5% | 44.9% | 0.0% | 0% | 0.91 | 0.71 |
| 2 | UHS | 12.3% | 28.6% | 11.6% | 38.3% | 0.4% | 0% | 0.78 | 0.77 |
| 3 | OMC | 10.7% | 27.8% | 18.4% | 34.5% | 0.0% | 0% | 0.83 | 0.68 |
| 4 | VICI | 9.1% | 31.1% | 14.2% | 31.1% | 0.0% | 0% | 0.50 | 0.48 |
| 5 | ARE | 7.4% | 27.5% | 18.1% | 27.5% | 0.0% | 0% | 0.68 | 0.48 |
| 6 | FOXA | 2.7% | 23.6% | 6.7% | 32.7% | 5.3% | 0% | 0.91 | 0.69 |
| 7 | CPT | 2.6% | 22.9% | 9.3% | 22.9% | 2.7% | 0% | 0.56 | 0.48 |
| 8 | BXP | 2.6% | 20.5% | 10.5% | 20.5% | 1.5% | 0% | 0.65 | 0.48 |
| 9 | CMCSA | 2.5% | 17.5% | 12.2% | 21.8% | 0.0% | 0% | 0.76 | 0.46 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | TTD | 17.1% | 36.0% | 14.5% | 44.9% | 0.0% | 0% | 0.91 | 0.71 |
| 2 | UHS | 12.3% | 28.6% | 11.6% | 38.3% | 0.4% | 0% | 0.78 | 0.77 |
| 3 | OMC | 10.7% | 27.8% | 18.4% | 34.5% | 0.0% | 0% | 0.83 | 0.68 |
| 4 | VICI | 9.1% | 31.1% | 14.2% | 31.1% | 0.0% | 0% | 0.50 | 0.48 |
| 5 | ARE | 7.4% | 27.5% | 18.1% | 27.5% | 0.0% | 0% | 0.68 | 0.48 |
| 6 | FOXA | 2.7% | 23.6% | 6.7% | 32.7% | 5.3% | 0% | 0.91 | 0.69 |
| 7 | CPT | 2.6% | 22.9% | 9.3% | 22.9% | 2.7% | 0% | 0.56 | 0.48 |
| 8 | BXP | 2.6% | 20.5% | 10.5% | 20.5% | 1.5% | 0% | 0.65 | 0.48 |
| 9 | CMCSA | 2.5% | 17.5% | 12.2% | 21.8% | 0.0% | 0% | 0.76 | 0.46 |
| 10 | AVB | -0.1% | 21.2% | 7.5% | 21.2% | 4.5% | 0% | 0.55 | 0.48 |
| 11 | ZTS | -1.0% | 18.6% | 5.1% | 25.9% | 6.9% | 0% | 0.98 | 0.90 |
| 12 | UDR | -1.5% | 21.4% | 6.0% | 21.4% | 6.0% | 0% | 0.51 | 0.48 |
| 13 | HUM | -1.7% | 17.3% | 7.0% | 25.4% | 5.0% | 0% | 0.76 | 0.61 |
| 14 | MO | -1.8% | 19.2% | 3.6% | 27.1% | 8.4% | 0% | 0.98 | 0.93 |
| 15 | EQR | -1.9% | 18.9% | 6.8% | 23.7% | 5.2% | 0% | 0.58 | 0.48 |
| 16 | ELV | -2.0% | 12.1% | 9.9% | 18.2% | 2.1% | 0% | 0.82 | 0.67 |
| 17 | CTSH | -3.5% | 15.3% | 5.6% | 21.7% | 6.4% | 0% | 0.86 | 0.87 |
| 18 | HST | -6.3% | 13.7% | 4.9% | 13.7% | 7.1% | 0% | 0.67 | 0.48 |
| 19 | EOG | -7.1% | 26.2% | -0.9% | 44.5% | 12.9% | 0% | 0.87 | 0.41 |
| 20 | INVH | -8.0% | 14.7% | 2.7% | 14.7% | 9.3% | 0% | 0.58 | 0.48 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | TTD | 32.9% | 36.0% | 14.5% | 44.9% | 100% | 157% |
| 2 | OMC | 27.1% | 27.8% | 18.4% | 34.5% | 100% | 152% |
| 3 | VICI | 26.8% | 31.1% | 14.2% | 31.1% | 100% | 287% |
| 4 | UHS | 26.8% | 28.6% | 11.6% | 38.3% | 75% | 98% |
| 5 | ARE | 25.1% | 27.5% | 18.1% | 27.5% | 100% | 237% |
| 6 | EOG | 24.0% | 26.2% | -0.9% | 44.5% | 75% | 111% |
| 7 | FOXA | 21.6% | 23.6% | 6.7% | 32.7% | 75% | 84% |
| 8 | CPT | 19.5% | 22.9% | 9.3% | 22.9% | 75% | 181% |
| 9 | FISV | 18.2% | 26.7% | -30.8% | 50.0% | 75% | 107% |
| 10 | BXP | 18.0% | 20.5% | 10.5% | 20.5% | 75% | 154% |
| 11 | AVB | 17.8% | 21.2% | 7.5% | 21.2% | 75% | 161% |
| 12 | UDR | 17.5% | 21.4% | 6.0% | 21.4% | 75% | 164% |
| 13 | MO | 17.3% | 19.2% | 3.6% | 27.1% | 75% | 61% |
| 14 | CMCSA | 17.3% | 17.5% | 12.2% | 21.8% | 100% | 56% |
| 15 | EQR | 17.1% | 18.9% | 6.8% | 23.7% | 75% | 138% |
| 16 | ZTS | 17.0% | 18.6% | 5.1% | 25.9% | 75% | 49% |
| 17 | HUM | 16.8% | 17.3% | 7.0% | 25.4% | 75% | 53% |
| 18 | CHTR | 16.2% | 46.3% | -95.0% | 67.3% | 75% | 305% |
| 19 | CTSH | 14.5% | 15.3% | 5.6% | 21.7% | 75% | 28% |
| 20 | GIS | 14.4% | 16.4% | -0.9% | 25.6% | 75% | 46% |

## Week-over-week

Previous run: 2026-08-07

- Entered Robust Top: CPT, TTD
- Exited Robust Top: GIS, WAT
- Entered Upside Top: CPT, TTD
- Exited Upside Top: ELV, WAT

Largest robust-rank moves:

- WAT: 1 → 230 (-229)
- FERG: 158 → 255 (-97)
- CVS: 305 → 234 (+71)
- GEN: 178 → 222 (-44)
- HON: 180 → 223 (-43)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| TTD | bear | 25% | 13.5% | 13.1% | 9.6% | 17.68 | 14.5% | 86% |
| TTD | base | 50% | 19.8% | 17.1% | 40.5% | 36.31 | 36.0% | 340% |
| TTD | bull | 25% | 24.8% | 20.7% | 43.5% | 48.08 | 44.9% | 493% |
| UHS | bear | 25% | 1.8% | 8.9% | 8.2% | 182.30 | 11.6% | 61% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 337.45 | 28.6% | 228% |
| UHS | bull | 25% | 11.3% | 12.1% | 19.5% | 477.22 | 38.3% | 373% |
| OMC | bear | 25% | 18.2% | 12.8% | 6.9% | 147.50 | 18.4% | 145% |
| OMC | base | 50% | 25.0% | 14.6% | 6.9% | 220.60 | 27.8% | 263% |
| OMC | bull | 25% | 30.4% | 15.9% | 6.9% | 288.11 | 34.5% | 371% |
| FOXA | bear | 25% | -1.3% | 17.3% | 6.9% | 67.89 | 6.7% | 33% |
| FOXA | base | 50% | 4.4% | 19.7% | 55.2% | 126.92 | 23.6% | 177% |
| FOXA | bull | 25% | 8.8% | 21.5% | 60.0% | 174.92 | 32.7% | 291% |
| CMCSA | bear | 25% | -6.6% | 16.1% | 6.5% | 30.91 | 12.2% | 64% |
| CMCSA | base | 50% | 0.8% | 18.7% | 6.5% | 40.87 | 17.5% | 123% |
| CMCSA | bull | 25% | 6.6% | 20.4% | 6.5% | 52.80 | 21.8% | 191% |
| ZTS | bear | 25% | 0.9% | 32.2% | 7.6% | 64.69 | 5.1% | 24% |
| ZTS | base | 50% | 5.1% | 36.0% | 24.3% | 109.67 | 18.6% | 126% |
| ZTS | bull | 25% | 8.4% | 39.1% | 24.5% | 144.08 | 25.9% | 203% |
| HUM | bear | 25% | 13.4% | 2.5% | 8.0% | 375.72 | 7.0% | 40% |
| HUM | base | 50% | 19.2% | 3.7% | 8.0% | 593.35 | 17.3% | 123% |
| HUM | bull | 25% | 23.8% | 4.8% | 8.0% | 830.25 | 25.4% | 213% |
| MO | bear | 25% | -2.2% | 48.7% | 6.7% | 56.51 | 3.6% | 17% |
| MO | base | 50% | 1.3% | 54.9% | 45.6% | 105.62 | 19.2% | 128% |
| MO | bull | 25% | 4.0% | 60.1% | 46.5% | 142.28 | 27.1% | 212% |
| ELV | bear | 25% | -0.8% | 4.9% | 7.3% | 449.33 | 9.9% | 53% |
| ELV | base | 50% | 5.4% | 5.9% | 7.3% | 506.08 | 12.1% | 80% |
| ELV | bull | 25% | 10.3% | 6.6% | 7.3% | 660.27 | 18.2% | 135% |
| CTSH | bear | 25% | -0.4% | 12.8% | 8.4% | 52.17 | 5.6% | 27% |
| CTSH | base | 50% | 4.6% | 15.0% | 13.9% | 75.37 | 15.3% | 97% |
| CTSH | bull | 25% | 8.6% | 16.6% | 14.8% | 95.90 | 21.7% | 158% |
| EOG | bear | 25% | -9.1% | 22.6% | 7.0% | 102.44 | -0.9% | -4% |
| EOG | base | 50% | 13.1% | 32.4% | 14.3% | 300.43 | 26.2% | 212% |
| EOG | bull | 25% | 30.8% | 41.1% | 15.4% | 621.76 | 44.5% | 541% |

## Boundary Assumptions & Valuation Alerts

- TTD — bounds: intrinsic_2x_price
- UHS — bounds: share_change_floor_hit
- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- ARE — bounds: specialist_model_v1
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit
- CPT — bounds: specialist_model_v1
- BXP — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- AVB — bounds: specialist_model_v1
- UDR — bounds: specialist_model_v1
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- EQR — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HST — bounds: specialist_model_v1
- EOG — bounds: reinvestment_cap_hit;intrinsic_2x_price
- INVH — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| DVA | weekly_drop | -25% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| APP | drawdown_from_high | nan% | -49% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- TTD: heavy_sbc
- OMC: incremental_roic_below_wacc
- VICI: nan
- ARE: nan
- CPT: nan
- BXP: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- AVB: nan
- UDR: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- EQR: nan
- ELV: incremental_roic_below_wacc
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
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- DVA DaVita Inc. — material_event_requires_reunderwriting
- APP AppLovin Corporation — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_model_confidence
- XYZ Block, Inc. — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- NRG NRG Energy, Inc. — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- TSLA Tesla, Inc. — insufficient_model_confidence
- GM General Motors Company — irr_below_solver_bound
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- EXPE Expedia Group, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- COP ConocoPhillips — insufficient_post_valuation_model_confidence
- VLO Valero Energy Corporation — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- PSX Phillips 66 — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- CI Cigna Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- TRGP Targa Resources Corp. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
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
