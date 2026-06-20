# Weekly US Stock Screen — 2026-06-18

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-06-18**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 512 | - |
| step2_hard_filters | 512 | 321 | persistent_negative_fcf: 22, interest_coverage: 21, adr_excluded: 17 |
| step3_standardize | 321 | 321 | - |
| step4_specialist_models | 95 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 321 | 314 | no_normalized_earnings: 7 |
| step5_quality_risk | 314 | 305 | - |
| step6_scenario_valuation | 305 | 279 | insufficient_post_valuation_model_confidence: 19, roic_not_meaningful:meaningless_capital: 6, invalid_valuation_output: 1 |
| step7_risk_adjusted_ranking | 338 | 338 | - |

## Eligible Candidates (14)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 17.1% | 34.3% | 16.4% | 44.4% | 0.0% | 0% | 0.79 | 0.77 |
| 2 | FOXA | 13.3% | 33.7% | 13.9% | 44.0% | 0.0% | 0% | 0.90 | 0.62 |
| 3 | KLAC | 11.7% | 29.0% | 15.4% | 37.3% | 0.0% | 0% | 0.97 | 0.68 |
| 4 | VICI | 10.8% | 34.6% | 15.7% | 34.6% | 0.0% | 0% | 0.47 | 0.48 |
| 5 | CTSH | 10.7% | 24.2% | 14.1% | 30.6% | 0.0% | 0% | 0.87 | 0.87 |
| 6 | OMC | 8.4% | 28.3% | 19.0% | 34.8% | 0.0% | 0% | 0.80 | 0.52 |
| 7 | TTD | 7.9% | 28.5% | 8.1% | 37.0% | 3.9% | 0% | 0.91 | 0.71 |
| 8 | ARE | 6.9% | 26.3% | 16.9% | 26.3% | 0.0% | 0% | 0.68 | 0.48 |
| 9 | BXP | 5.1% | 22.6% | 12.1% | 22.6% | 0.0% | 0% | 0.64 | 0.48 |
| 10 | CPT | 3.9% | 24.1% | 10.1% | 24.1% | 1.9% | 0% | 0.55 | 0.48 |
| 11 | CMCSA | 3.6% | 19.8% | 16.5% | 25.2% | 0.0% | 0% | 0.76 | 0.46 |
| 12 | AVB | 2.5% | 23.5% | 9.0% | 23.5% | 3.0% | 0% | 0.54 | 0.48 |
| 13 | ADBE | 2.2% | 19.3% | 8.4% | 25.7% | 3.6% | 0% | 0.98 | 0.79 |
| 14 | UDR | 0.1% | 23.0% | 6.8% | 23.0% | 5.2% | 0% | 0.49 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 17.1% | 34.3% | 16.4% | 44.4% | 0.0% | 0% | 0.79 | 0.77 |
| 2 | FOXA | 13.3% | 33.7% | 13.9% | 44.0% | 0.0% | 0% | 0.90 | 0.62 |
| 3 | KLAC | 11.7% | 29.0% | 15.4% | 37.3% | 0.0% | 0% | 0.97 | 0.68 |
| 4 | VICI | 10.8% | 34.6% | 15.7% | 34.6% | 0.0% | 0% | 0.47 | 0.48 |
| 5 | CTSH | 10.7% | 24.2% | 14.1% | 30.6% | 0.0% | 0% | 0.87 | 0.87 |
| 6 | OMC | 8.4% | 28.3% | 19.0% | 34.8% | 0.0% | 0% | 0.80 | 0.52 |
| 7 | TTD | 7.9% | 28.5% | 8.1% | 37.0% | 3.9% | 0% | 0.91 | 0.71 |
| 8 | ARE | 6.9% | 26.3% | 16.9% | 26.3% | 0.0% | 0% | 0.68 | 0.48 |
| 9 | BXP | 5.1% | 22.6% | 12.1% | 22.6% | 0.0% | 0% | 0.64 | 0.48 |
| 10 | CPT | 3.9% | 24.1% | 10.1% | 24.1% | 1.9% | 0% | 0.55 | 0.48 |
| 11 | CMCSA | 3.6% | 19.8% | 16.5% | 25.2% | 0.0% | 0% | 0.76 | 0.46 |
| 12 | AVB | 2.5% | 23.5% | 9.0% | 23.5% | 3.0% | 0% | 0.54 | 0.48 |
| 13 | ADBE | 2.2% | 19.3% | 8.4% | 25.7% | 3.6% | 0% | 0.98 | 0.79 |
| 14 | UDR | 0.1% | 23.0% | 6.8% | 23.0% | 5.2% | 0% | 0.49 | 0.48 |
| 15 | CPAY | -0.2% | 19.3% | 5.7% | 26.8% | 6.3% | 0% | 0.99 | 0.84 |
| 16 | ELV | -0.9% | 12.5% | 10.7% | 18.7% | 1.3% | 0% | 0.84 | 0.67 |
| 17 | IT | -1.2% | 22.7% | 2.9% | 34.5% | 9.1% | 0% | 0.91 | 0.74 |
| 18 | HUM | -2.1% | 17.7% | 6.4% | 26.3% | 5.6% | 0% | 0.66 | 0.60 |
| 19 | EQR | -2.4% | 18.2% | 6.6% | 26.0% | 5.4% | 0% | 0.60 | 0.48 |
| 20 | HPQ | -2.8% | 9.2% | 9.2% | 14.3% | 2.8% | 0% | 0.97 | 0.67 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | UHS | 32.4% | 34.3% | 16.4% | 44.4% | 100% | 143% |
| 2 | FOXA | 31.3% | 33.7% | 13.9% | 44.0% | 100% | 162% |
| 3 | VICI | 29.9% | 34.6% | 15.7% | 34.6% | 100% | 341% |
| 4 | KLAC | 27.7% | 29.0% | 15.4% | 37.3% | 100% | 74% |
| 5 | OMC | 27.6% | 28.3% | 19.0% | 34.8% | 100% | 161% |
| 6 | TTD | 25.5% | 28.5% | 8.1% | 37.0% | 75% | 103% |
| 7 | FISV | 25.0% | 32.8% | -21.9% | 56.4% | 75% | 160% |
| 8 | EOG | 24.7% | 26.4% | -0.5% | 46.5% | 75% | 122% |
| 9 | ARE | 24.0% | 26.3% | 16.9% | 26.3% | 100% | 222% |
| 10 | CTSH | 23.3% | 24.2% | 14.1% | 30.6% | 100% | 79% |
| 11 | IT | 20.7% | 22.7% | 2.9% | 34.5% | 75% | 68% |
| 12 | CPT | 20.6% | 24.1% | 10.1% | 24.1% | 75% | 195% |
| 13 | CMCSA | 20.3% | 19.8% | 16.5% | 25.2% | 100% | 73% |
| 14 | BXP | 19.9% | 22.6% | 12.1% | 22.6% | 100% | 176% |
| 15 | AVB | 19.9% | 23.5% | 9.0% | 23.5% | 75% | 187% |
| 16 | UDR | 19.0% | 23.0% | 6.8% | 23.0% | 75% | 182% |
| 17 | ADBE | 18.2% | 19.3% | 8.4% | 25.7% | 75% | 33% |
| 18 | ACGL | 17.9% | 19.9% | 5.0% | 26.6% | 75% | 148% |
| 19 | CPAY | 17.8% | 19.3% | 5.7% | 26.8% | 75% | 57% |
| 20 | LDOS | 17.6% | 20.7% | -4.7% | 33.6% | 75% | 73% |

## Week-over-week

Previous run: 2026-06-17

- Entered Robust Top: EQR, IT
- Exited Robust Top: ACN, ZTS
- Entered Upside Top: none
- Exited Upside Top: none

Largest robust-rank moves:

- EFX: 330 → 308 (+22)
- CVS: 323 → 310 (+13)
- JBL: 253 → 241 (+12)
- ROP: 176 → 165 (+11)
- TXT: 147 → 136 (+11)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.7% | 8.9% | 7.9% | 183.68 | 16.4% | 92% |
| UHS | base | 50% | 6.9% | 10.7% | 17.2% | 342.39 | 34.3% | 300% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.6% | 485.08 | 44.4% | 475% |
| FOXA | bear | 25% | -1.1% | 17.5% | 6.5% | 69.31 | 13.9% | 77% |
| FOXA | base | 50% | 4.7% | 20.1% | 54.7% | 137.04 | 33.7% | 297% |
| FOXA | bull | 25% | 9.3% | 22.0% | 60.0% | 193.42 | 44.0% | 472% |
| KLAC | bear | 25% | 7.9% | 32.5% | 11.9% | 293.12 | 15.4% | 83% |
| KLAC | base | 50% | 14.6% | 37.6% | 58.4% | 452.11 | 29.0% | 218% |
| KLAC | bull | 25% | 19.9% | 41.9% | 60.0% | 590.48 | 37.3% | 326% |
| CTSH | bear | 25% | 0.1% | 12.9% | 8.3% | 54.67 | 14.1% | 77% |
| CTSH | base | 50% | 4.9% | 15.0% | 14.2% | 78.15 | 24.2% | 175% |
| CTSH | bull | 25% | 8.7% | 16.6% | 15.0% | 98.67 | 30.6% | 255% |
| OMC | bear | 25% | 18.4% | 12.7% | 6.5% | 125.76 | 19.0% | 150% |
| OMC | base | 50% | 25.0% | 14.6% | 6.5% | 186.37 | 28.3% | 268% |
| OMC | bull | 25% | 30.3% | 15.9% | 6.5% | 241.30 | 34.8% | 374% |
| TTD | bear | 25% | 13.6% | 13.1% | 9.3% | 17.94 | 8.1% | 43% |
| TTD | base | 50% | 19.9% | 17.1% | 41.0% | 37.63 | 28.5% | 239% |
| TTD | bull | 25% | 24.9% | 20.7% | 44.1% | 49.95 | 37.0% | 358% |
| CMCSA | bear | 25% | -6.0% | 16.1% | 6.5% | 30.85 | 16.5% | 92% |
| CMCSA | base | 50% | 1.2% | 18.7% | 6.5% | 38.90 | 19.8% | 151% |
| CMCSA | bull | 25% | 7.0% | 20.4% | 6.5% | 52.43 | 25.2% | 239% |
| ADBE | bear | 25% | 8.8% | 29.7% | 10.9% | 176.23 | 8.4% | 42% |
| ADBE | base | 50% | 13.2% | 33.6% | 57.2% | 258.74 | 19.3% | 129% |
| ADBE | bull | 25% | 16.8% | 36.9% | 58.3% | 322.36 | 25.7% | 192% |
| CPAY | bear | 25% | 7.7% | 39.8% | 7.4% | 317.74 | 5.7% | 29% |
| CPAY | base | 50% | 13.3% | 44.0% | 30.0% | 541.51 | 19.3% | 137% |
| CPAY | bull | 25% | 17.9% | 47.4% | 30.3% | 716.67 | 26.8% | 219% |
| ELV | bear | 25% | -1.3% | 4.9% | 7.0% | 453.94 | 10.7% | 58% |
| ELV | base | 50% | 4.9% | 5.9% | 7.0% | 505.49 | 12.5% | 83% |
| ELV | bull | 25% | 9.9% | 6.6% | 7.0% | 664.44 | 18.7% | 141% |
| IT | bear | 25% | -2.1% | 13.0% | 7.9% | 101.01 | 2.9% | 13% |
| IT | base | 50% | 3.3% | 17.1% | 47.6% | 213.81 | 22.7% | 164% |
| IT | bull | 25% | 7.5% | 20.7% | 51.6% | 321.18 | 34.5% | 308% |
| HUM | bear | 25% | 12.7% | 2.5% | 7.9% | 339.93 | 6.4% | 36% |
| HUM | base | 50% | 19.3% | 3.7% | 7.9% | 563.37 | 17.7% | 128% |
| HUM | bull | 25% | 24.6% | 4.8% | 7.9% | 804.86 | 26.3% | 226% |
| HPQ | bear | 25% | -3.6% | 5.7% | 8.8% | 24.85 | 11.2% | 57% |
| HPQ | base | 50% | 1.8% | 6.6% | 8.8% | 23.06 | 9.2% | 58% |
| HPQ | bull | 25% | 6.2% | 7.3% | 8.8% | 29.71 | 14.3% | 103% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 8.8%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- UHS — bounds: share_change_floor_hit;intrinsic_2x_price
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit;wacc_floor_hit;intrinsic_2x_price
- KLAC — bounds: forward_roic_cap_hit
- VICI — bounds: specialist_model_v1
- OMC — bounds: base_growth_cap_hit;wacc_floor_hit;reinvestment_cap_hit;intrinsic_2x_price
- TTD — bounds: intrinsic_2x_price
- ARE — bounds: specialist_model_v1
- BXP — bounds: specialist_model_v1
- CPT — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- AVB — bounds: specialist_model_v1
- ADBE — bounds: share_change_floor_hit
- UDR — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- EQR — bounds: specialist_model_v1
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| ACN | weekly_drop | -28% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SMCI | weekly_drop | -26% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| CHTR | drawdown_from_high | nan% | -48% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- VICI: nan
- OMC: incremental_roic_below_wacc
- TTD: heavy_sbc
- ARE: nan
- BXP: nan
- CPT: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- AVB: nan
- ADBE: heavy_sbc
- UDR: nan
- CPAY: thin_interest_coverage
- ELV: incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- EQR: nan
- HPQ: incremental_roic_below_wacc

## Watchlist (not rankable under the general model)

- V Visa Inc. — consumer_finance_model_not_supported
- MA Mastercard Incorporated — consumer_finance_model_not_supported
- MS Morgan Stanley — asset_management_model_not_supported
- GS The Goldman Sachs Group, Inc. — asset_management_model_not_supported
- AXP American Express Company — consumer_finance_model_not_supported
- BLK BlackRock, Inc. — asset_management_model_not_supported
- SCHW The Charles Schwab Corporation — asset_management_model_not_supported
- BX Blackstone Inc. — asset_management_model_not_supported
- COF Capital One Financial Corporation — consumer_finance_model_not_supported
- SPGI S&P Global Inc. — financial_sector_model_not_supported
- BNY Bank of New York Mellon Corp — asset_management_model_not_supported
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- ARES Ares Management Corporation — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- RJF Raymond James Financial, Inc. — asset_management_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
- BEN Franklin Resources, Inc. — asset_management_model_not_supported
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- IVZ Invesco Ltd. — asset_management_model_not_supported
- FDS FactSet Research Systems Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- CME CME Group Inc. — financial_sector_model_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- INSM Insmed Incorporated — preprofit_biotech_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- ACN Accenture plc — material_event_requires_reunderwriting
- SMCI Super Micro Computer, Inc. — material_event_requires_reunderwriting
- CHTR Charter Communications, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- COP ConocoPhillips — insufficient_model_confidence
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
- PFE Pfizer Inc. — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- CI Cigna Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- TRGP Targa Resources Corp. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- XYZ Block, Inc. — insufficient_post_valuation_model_confidence
- IR Ingersoll Rand Inc. — insufficient_post_valuation_model_confidence
- DVN Devon Energy Corporation — insufficient_post_valuation_model_confidence
- IFF International Flavors & Fragrances Inc. — insufficient_post_valuation_model_confidence
- CF CF Industries Holdings, Inc. — insufficient_post_valuation_model_confidence
- BLDR Builders FirstSource, Inc. — insufficient_post_valuation_model_confidence
- NVDA NVIDIA Corporation — insufficient_post_valuation_model_confidence
- MU Micron Technology, Inc. — insufficient_post_valuation_model_confidence
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
