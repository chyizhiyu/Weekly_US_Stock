# Weekly US Stock Screen — 2026-07-24

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-07-24**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 515 | - |
| step2_hard_filters | 515 | 308 | adr_excluded: 33, persistent_negative_fcf: 22, interest_coverage: 18 |
| step3_standardize | 308 | 308 | - |
| step4_specialist_models | 93 | 59 | asset_management_model_not_supported: 16, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 308 | 301 | no_normalized_earnings: 7 |
| step5_quality_risk | 301 | 293 | - |
| step6_scenario_valuation | 293 | 269 | insufficient_post_valuation_model_confidence: 17, roic_not_meaningful:meaningless_capital: 6, invalid_valuation_output: 1 |
| step7_risk_adjusted_ranking | 328 | 328 | - |

## Eligible Candidates (12)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 13.5% | 29.6% | 12.6% | 39.3% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | CMCSA | 12.7% | 33.9% | 30.1% | 36.7% | 0.0% | 0% | 0.87 | 0.58 |
| 3 | FOXA | 11.7% | 30.0% | 11.4% | 39.9% | 0.6% | 0% | 0.90 | 0.68 |
| 4 | VICI | 8.9% | 30.6% | 13.8% | 30.6% | 0.0% | 0% | 0.50 | 0.48 |
| 5 | TTD | 8.6% | 28.7% | 8.7% | 37.1% | 3.3% | 0% | 0.91 | 0.71 |
| 6 | CTSH | 8.2% | 21.4% | 12.0% | 27.5% | 0.0% | 0% | 0.86 | 0.87 |
| 7 | ARE | 6.5% | 25.6% | 16.4% | 25.6% | 0.0% | 0% | 0.68 | 0.48 |
| 8 | OMC | 6.0% | 24.5% | 15.4% | 30.9% | 0.0% | 0% | 0.80 | 0.48 |
| 9 | HCA | 3.0% | 20.0% | 8.5% | 26.6% | 3.5% | 0% | 0.98 | 0.81 |
| 10 | BXP | 2.2% | 20.2% | 10.2% | 20.2% | 1.8% | 0% | 0.65 | 0.48 |
| 11 | CPT | 1.1% | 21.7% | 8.4% | 21.7% | 3.6% | 0% | 0.56 | 0.48 |
| 12 | ELV | 0.6% | 13.6% | 11.5% | 19.7% | 0.5% | 0% | 0.82 | 0.67 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 13.5% | 29.6% | 12.6% | 39.3% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | CMCSA | 12.7% | 33.9% | 30.1% | 36.7% | 0.0% | 0% | 0.87 | 0.58 |
| 3 | FOXA | 11.7% | 30.0% | 11.4% | 39.9% | 0.6% | 0% | 0.90 | 0.68 |
| 4 | VICI | 8.9% | 30.6% | 13.8% | 30.6% | 0.0% | 0% | 0.50 | 0.48 |
| 5 | TTD | 8.6% | 28.7% | 8.7% | 37.1% | 3.3% | 0% | 0.91 | 0.71 |
| 6 | CTSH | 8.2% | 21.4% | 12.0% | 27.5% | 0.0% | 0% | 0.86 | 0.87 |
| 7 | ARE | 6.5% | 25.6% | 16.4% | 25.6% | 0.0% | 0% | 0.68 | 0.48 |
| 8 | OMC | 6.0% | 24.5% | 15.4% | 30.9% | 0.0% | 0% | 0.80 | 0.48 |
| 9 | HCA | 3.0% | 20.0% | 8.5% | 26.6% | 3.5% | 0% | 0.98 | 0.81 |
| 10 | BXP | 2.2% | 20.2% | 10.2% | 20.2% | 1.8% | 0% | 0.65 | 0.48 |
| 11 | CPT | 1.1% | 21.7% | 8.4% | 21.7% | 3.6% | 0% | 0.56 | 0.48 |
| 12 | ELV | 0.6% | 13.6% | 11.5% | 19.7% | 0.5% | 0% | 0.82 | 0.67 |
| 13 | AVB | -1.5% | 20.0% | 6.7% | 20.0% | 5.3% | 0% | 0.55 | 0.48 |
| 14 | ZTS | -2.9% | 17.4% | 4.3% | 24.5% | 7.7% | 0% | 0.98 | 0.90 |
| 15 | UDR | -3.2% | 20.0% | 4.9% | 20.0% | 7.1% | 0% | 0.51 | 0.48 |
| 16 | HUM | -5.2% | 15.7% | 4.6% | 24.2% | 7.4% | 0% | 0.66 | 0.60 |
| 17 | CPAY | -5.4% | 16.0% | 3.3% | 23.2% | 8.7% | 0% | 0.99 | 0.84 |
| 18 | EQR | -5.7% | 15.5% | 4.7% | 22.7% | 7.3% | 0% | 0.61 | 0.48 |
| 19 | ADBE | -5.7% | 14.6% | 4.3% | 20.8% | 7.7% | 0% | 0.98 | 0.78 |
| 20 | HPQ | -6.0% | 6.0% | 6.0% | 11.1% | 6.0% | 0% | 0.97 | 0.67 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CMCSA | 34.4% | 33.9% | 30.1% | 36.7% | 100% | 170% |
| 2 | CI | 30.8% | 34.4% | -9.7% | 64.3% | 75% | 204% |
| 3 | FOXA | 27.8% | 30.0% | 11.4% | 39.9% | 75% | 129% |
| 4 | UHS | 27.8% | 29.6% | 12.6% | 39.3% | 100% | 105% |
| 5 | VICI | 26.4% | 30.6% | 13.8% | 30.6% | 100% | 279% |
| 6 | TTD | 25.8% | 28.7% | 8.7% | 37.1% | 75% | 101% |
| 7 | OMC | 23.9% | 24.5% | 15.4% | 30.9% | 100% | 121% |
| 8 | ARE | 23.3% | 25.6% | 16.4% | 25.6% | 100% | 213% |
| 9 | CHTR | 22.8% | 54.8% | -95.0% | 76.5% | 75% | 413% |
| 10 | CTSH | 20.6% | 21.4% | 12.0% | 27.5% | 75% | 59% |
| 11 | EOG | 19.7% | 21.4% | -5.0% | 40.8% | 75% | 80% |
| 12 | FISV | 19.5% | 29.0% | -32.7% | 52.8% | 75% | 123% |
| 13 | HCA | 18.8% | 20.0% | 8.5% | 26.6% | 75% | 40% |
| 14 | CPT | 18.4% | 21.7% | 8.4% | 21.7% | 75% | 167% |
| 15 | BXP | 17.7% | 20.2% | 10.2% | 20.2% | 75% | 151% |
| 16 | AVB | 16.7% | 20.0% | 6.7% | 20.0% | 75% | 149% |
| 17 | GIS | 16.6% | 18.7% | 1.0% | 27.9% | 75% | 58% |
| 18 | UDR | 16.3% | 20.0% | 4.9% | 20.0% | 75% | 149% |
| 19 | LDOS | 15.9% | 19.0% | -6.1% | 31.7% | 75% | 62% |
| 20 | ZTS | 15.9% | 17.4% | 4.3% | 24.5% | 75% | 42% |

## Week-over-week

Previous run: 2026-07-17

- Entered Robust Top: ADBE, HCA
- Exited Robust Top: HST, INVH
- Entered Upside Top: CHTR, CI, HCA
- Exited Upside Top: CPAY, ELV, IT

Largest robust-rank moves:

- FISV: 155 → 212 (-57)
- HON: 152 → 190 (-38)
- GOOGL: 151 → 119 (+32)
- NOW: 250 → 277 (-27)
- DHR: 243 → 269 (-26)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.7% | 8.9% | 8.2% | 172.91 | 12.6% | 66% |
| UHS | base | 50% | 6.9% | 10.7% | 17.2% | 318.77 | 29.6% | 239% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.5% | 449.88 | 39.3% | 388% |
| CMCSA | bear | 25% | -5.3% | 16.4% | 7.7% | 48.78 | 30.1% | 203% |
| CMCSA | base | 50% | 0.9% | 18.7% | 7.7% | 60.31 | 36.7% | 329% |
| CMCSA | bull | 25% | 5.9% | 20.4% | 7.7% | 64.85 | 33.9% | 341% |
| FOXA | bear | 25% | -1.0% | 17.5% | 6.8% | 65.69 | 11.4% | 61% |
| FOXA | base | 50% | 4.9% | 20.1% | 54.5% | 126.63 | 30.0% | 249% |
| FOXA | bull | 25% | 9.5% | 22.0% | 60.0% | 177.15 | 39.9% | 399% |
| TTD | bear | 25% | 13.5% | 13.1% | 9.6% | 16.96 | 8.7% | 46% |
| TTD | base | 50% | 19.8% | 17.1% | 41.0% | 34.77 | 28.7% | 240% |
| TTD | bull | 25% | 24.8% | 20.7% | 44.1% | 46.05 | 37.1% | 358% |
| CTSH | bear | 25% | -0.1% | 12.8% | 8.8% | 51.58 | 12.0% | 63% |
| CTSH | base | 50% | 4.8% | 15.0% | 14.2% | 72.21 | 21.4% | 147% |
| CTSH | bull | 25% | 8.7% | 16.6% | 15.0% | 90.40 | 27.5% | 217% |
| OMC | bear | 25% | 18.3% | 12.7% | 6.7% | 118.07 | 15.4% | 113% |
| OMC | base | 50% | 25.0% | 14.6% | 6.7% | 176.09 | 24.5% | 215% |
| OMC | bull | 25% | 30.3% | 15.9% | 6.7% | 228.60 | 30.9% | 307% |
| HCA | bear | 25% | 1.2% | 13.3% | 9.9% | 356.70 | 8.5% | 42% |
| HCA | base | 50% | 5.4% | 14.9% | 53.8% | 535.59 | 20.0% | 133% |
| HCA | bull | 25% | 8.7% | 16.2% | 54.5% | 672.25 | 26.6% | 199% |
| ELV | bear | 25% | -0.8% | 4.9% | 7.2% | 453.61 | 11.5% | 64% |
| ELV | base | 50% | 5.4% | 5.9% | 7.2% | 511.49 | 13.6% | 92% |
| ELV | bull | 25% | 10.3% | 6.6% | 7.2% | 667.31 | 19.7% | 151% |
| ZTS | bear | 25% | 1.0% | 32.2% | 7.7% | 63.74 | 4.3% | 20% |
| ZTS | base | 50% | 5.1% | 36.0% | 24.5% | 107.06 | 17.4% | 115% |
| ZTS | bull | 25% | 8.4% | 39.1% | 24.8% | 140.17 | 24.5% | 187% |
| HUM | bear | 25% | 12.4% | 2.5% | 7.9% | 335.78 | 4.6% | 25% |
| HUM | base | 50% | 19.0% | 3.7% | 7.9% | 556.12 | 15.7% | 109% |
| HUM | bull | 25% | 24.3% | 4.8% | 7.9% | 794.37 | 24.2% | 199% |
| CPAY | bear | 25% | 7.7% | 39.8% | 7.8% | 302.69 | 3.3% | 16% |
| CPAY | base | 50% | 13.3% | 44.0% | 30.0% | 505.58 | 16.0% | 106% |
| CPAY | bull | 25% | 17.9% | 47.4% | 30.3% | 664.30 | 23.2% | 177% |
| ADBE | bear | 25% | 8.6% | 29.7% | 11.4% | 169.11 | 4.3% | 20% |
| ADBE | base | 50% | 13.3% | 33.6% | 57.2% | 248.16 | 14.6% | 90% |
| ADBE | bull | 25% | 17.1% | 36.9% | 58.3% | 309.62 | 20.8% | 144% |
| HPQ | bear | 25% | -3.6% | 5.7% | 9.2% | 23.34 | 7.7% | 37% |
| HPQ | base | 50% | 1.8% | 6.6% | 9.2% | 21.12 | 6.0% | 35% |
| HPQ | bull | 25% | 6.2% | 7.3% | 9.2% | 27.24 | 11.1% | 75% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 9.2%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- UHS — bounds: share_change_floor_hit;intrinsic_2x_price
- CMCSA — bounds: share_change_floor_hit;reinvestment_cap_hit;intrinsic_2x_price
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- TTD — bounds: intrinsic_2x_price
- ARE — bounds: specialist_model_v1
- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- HCA — bounds: share_change_floor_hit
- BXP — bounds: specialist_model_v1
- CPT — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- AVB — bounds: specialist_model_v1
- UDR — bounds: specialist_model_v1
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- EQR — bounds: specialist_model_v1
- ADBE — bounds: share_change_floor_hit
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| ORCL | drawdown_from_high | nan% | -53% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| IBM | weekly_drop | -26% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| GLW | drawdown_from_high | nan% | -43% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SMCI | drawdown_from_high | nan% | -40% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- VICI: nan
- TTD: heavy_sbc
- ARE: nan
- OMC: incremental_roic_below_wacc
- BXP: nan
- CPT: nan
- ELV: incremental_roic_below_wacc
- AVB: nan
- UDR: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- CPAY: thin_interest_coverage
- EQR: nan
- ADBE: heavy_sbc
- HPQ: incremental_roic_below_wacc

## Watchlist (not rankable under the general model)

- V Visa Inc. — consumer_finance_model_not_supported
- MA Mastercard Incorporated — consumer_finance_model_not_supported
- MS Morgan Stanley — asset_management_model_not_supported
- GS The Goldman Sachs Group, Inc. — asset_management_model_not_supported
- AXP American Express Company — consumer_finance_model_not_supported
- SCHW The Charles Schwab Corporation — asset_management_model_not_supported
- BLK BlackRock, Inc. — asset_management_model_not_supported
- BX Blackstone Inc. — asset_management_model_not_supported
- SPGI S&P Global Inc. — financial_sector_model_not_supported
- COF Capital One Financial Corporation — consumer_finance_model_not_supported
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
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- ORCL Oracle Corporation — material_event_requires_reunderwriting
- IBM International Business Machines Corporation — material_event_requires_reunderwriting
- GLW Corning Inc — material_event_requires_reunderwriting
- SMCI Super Micro Computer, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_model_confidence
- VLO Valero Energy Corporation — insufficient_model_confidence
- PSX Phillips 66 — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- TSLA Tesla, Inc. — insufficient_model_confidence
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- EXPE Expedia Group, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- CSGP CoStar Group, Inc. — roic_not_meaningful:meaningless_capital
- COP ConocoPhillips — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- TRGP Targa Resources Corp. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- XYZ Block, Inc. — insufficient_post_valuation_model_confidence
- IR Ingersoll Rand Inc. — insufficient_post_valuation_model_confidence
- DVN Devon Energy Corporation — insufficient_post_valuation_model_confidence
- IFF International Flavors & Fragrances Inc. — insufficient_post_valuation_model_confidence
- CF CF Industries Holdings, Inc. — insufficient_post_valuation_model_confidence
- BLDR Builders FirstSource, Inc. — insufficient_post_valuation_model_confidence
- NVDA NVIDIA Corporation — insufficient_post_valuation_model_confidence
- AMD Advanced Micro Devices, Inc. — insufficient_post_valuation_model_confidence
- APP AppLovin Corporation — insufficient_post_valuation_model_confidence
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
