# Weekly US Stock Screen — 2026-07-02

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-07-02**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 514 | - |
| step2_hard_filters | 514 | 307 | adr_excluded: 31, interest_coverage: 21, persistent_negative_fcf: 21 |
| step3_standardize | 307 | 307 | - |
| step4_specialist_models | 92 | 58 | asset_management_model_not_supported: 16, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 307 | 300 | no_normalized_earnings: 7 |
| step5_quality_risk | 300 | 291 | - |
| step6_scenario_valuation | 291 | 265 | insufficient_post_valuation_model_confidence: 19, roic_not_meaningful:meaningless_capital: 6, invalid_valuation_output: 1 |
| step7_risk_adjusted_ranking | 323 | 323 | - |

## Eligible Candidates (13)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 15.5% | 32.2% | 14.7% | 42.1% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | CTSH | 13.9% | 27.9% | 17.4% | 34.4% | 0.0% | 0% | 0.87 | 0.87 |
| 3 | FOXA | 13.4% | 33.7% | 13.9% | 44.1% | 0.0% | 0% | 0.90 | 0.62 |
| 4 | VICI | 10.6% | 34.0% | 15.4% | 34.0% | 0.0% | 0% | 0.47 | 0.48 |
| 5 | ACN | 9.8% | 23.1% | 13.2% | 28.5% | 0.0% | 0% | 0.99 | 0.88 |
| 6 | TTD | 8.9% | 29.2% | 8.6% | 37.6% | 3.4% | 0% | 0.91 | 0.71 |
| 7 | OMC | 8.2% | 27.8% | 18.5% | 34.2% | 0.0% | 0% | 0.80 | 0.52 |
| 8 | ARE | 6.4% | 25.3% | 16.0% | 25.3% | 0.0% | 0% | 0.68 | 0.48 |
| 9 | BXP | 4.2% | 21.8% | 11.5% | 21.8% | 0.5% | 0% | 0.64 | 0.48 |
| 10 | CMCSA | 2.6% | 17.7% | 14.0% | 23.2% | 0.0% | 0% | 0.76 | 0.46 |
| 11 | CPT | 2.0% | 22.7% | 8.9% | 22.7% | 3.1% | 0% | 0.55 | 0.48 |
| 12 | CPAY | 1.5% | 20.4% | 6.5% | 27.9% | 5.5% | 0% | 0.99 | 0.84 |
| 13 | AVB | 0.2% | 21.7% | 7.5% | 21.7% | 4.5% | 0% | 0.54 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 15.5% | 32.2% | 14.7% | 42.1% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | CTSH | 13.9% | 27.9% | 17.4% | 34.4% | 0.0% | 0% | 0.87 | 0.87 |
| 3 | FOXA | 13.4% | 33.7% | 13.9% | 44.1% | 0.0% | 0% | 0.90 | 0.62 |
| 4 | VICI | 10.6% | 34.0% | 15.4% | 34.0% | 0.0% | 0% | 0.47 | 0.48 |
| 5 | ACN | 9.8% | 23.1% | 13.2% | 28.5% | 0.0% | 0% | 0.99 | 0.88 |
| 6 | TTD | 8.9% | 29.2% | 8.6% | 37.6% | 3.4% | 0% | 0.91 | 0.71 |
| 7 | OMC | 8.2% | 27.8% | 18.5% | 34.2% | 0.0% | 0% | 0.80 | 0.52 |
| 8 | ARE | 6.4% | 25.3% | 16.0% | 25.3% | 0.0% | 0% | 0.68 | 0.48 |
| 9 | BXP | 4.2% | 21.8% | 11.5% | 21.8% | 0.5% | 0% | 0.64 | 0.48 |
| 10 | CMCSA | 2.6% | 17.7% | 14.0% | 23.2% | 0.0% | 0% | 0.76 | 0.46 |
| 11 | CPT | 2.0% | 22.7% | 8.9% | 22.7% | 3.1% | 0% | 0.55 | 0.48 |
| 12 | CPAY | 1.5% | 20.4% | 6.5% | 27.9% | 5.5% | 0% | 0.99 | 0.84 |
| 13 | AVB | 0.2% | 21.7% | 7.5% | 21.7% | 4.5% | 0% | 0.54 | 0.48 |
| 14 | ADBE | -0.4% | 17.8% | 7.0% | 24.3% | 5.0% | 0% | 0.98 | 0.78 |
| 15 | ELV | -0.8% | 12.6% | 10.8% | 18.8% | 1.2% | 0% | 0.84 | 0.67 |
| 16 | HPQ | -1.2% | 10.8% | 10.8% | 16.0% | 1.2% | 0% | 0.97 | 0.67 |
| 17 | UDR | -2.2% | 21.3% | 5.4% | 21.3% | 6.6% | 0% | 0.50 | 0.48 |
| 18 | IT | -2.3% | 22.0% | 2.3% | 33.8% | 9.7% | 0% | 0.91 | 0.74 |
| 19 | EQR | -4.5% | 16.6% | 5.3% | 24.3% | 6.7% | 0% | 0.60 | 0.48 |
| 20 | HUM | -6.0% | 15.2% | 4.1% | 23.6% | 7.9% | 0% | 0.66 | 0.60 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | FOXA | 31.4% | 33.7% | 13.9% | 44.1% | 100% | 163% |
| 2 | UHS | 30.3% | 32.2% | 14.7% | 42.1% | 100% | 126% |
| 3 | VICI | 29.4% | 34.0% | 15.4% | 34.0% | 100% | 332% |
| 4 | OMC | 27.1% | 27.8% | 18.5% | 34.2% | 100% | 156% |
| 5 | CTSH | 26.9% | 27.9% | 17.4% | 34.4% | 100% | 102% |
| 6 | TTD | 26.1% | 29.2% | 8.6% | 37.6% | 75% | 107% |
| 7 | EOG | 24.3% | 26.1% | -1.0% | 46.0% | 75% | 118% |
| 8 | FISV | 24.1% | 31.9% | -22.8% | 55.4% | 75% | 152% |
| 9 | ARE | 23.0% | 25.3% | 16.0% | 25.3% | 100% | 209% |
| 10 | ACN | 22.0% | 23.1% | 13.2% | 28.5% | 100% | 65% |
| 11 | IT | 20.0% | 22.0% | 2.3% | 33.8% | 75% | 63% |
| 12 | CPT | 19.3% | 22.7% | 8.9% | 22.7% | 75% | 178% |
| 13 | BXP | 19.2% | 21.8% | 11.5% | 21.8% | 75% | 168% |
| 14 | CPAY | 18.8% | 20.4% | 6.5% | 27.9% | 75% | 63% |
| 15 | LDOS | 18.6% | 21.8% | -3.9% | 34.8% | 75% | 80% |
| 16 | AVB | 18.2% | 21.7% | 7.5% | 21.7% | 75% | 167% |
| 17 | CMCSA | 18.1% | 17.7% | 14.0% | 23.2% | 100% | 59% |
| 18 | UDR | 17.3% | 21.3% | 5.4% | 21.3% | 75% | 162% |
| 19 | ADBE | 16.7% | 17.8% | 7.0% | 24.3% | 75% | 26% |
| 20 | EQR | 15.7% | 16.6% | 5.3% | 24.3% | 75% | 116% |

## Week-over-week

Previous run: 2026-06-26

- Entered Robust Top: FOXA
- Exited Robust Top: ZTS
- Entered Upside Top: FOXA
- Exited Upside Top: ZTS

Largest robust-rank moves:

- J: 289 → 311 (-22)
- AMT: 139 → 121 (+18)
- BDX: 291 → 308 (-17)
- TGT: 145 → 131 (+14)
- MDLZ: 138 → 124 (+14)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.7% | 8.9% | 8.0% | 180.78 | 14.7% | 80% |
| UHS | base | 50% | 6.9% | 10.7% | 17.2% | 335.95 | 32.2% | 272% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.6% | 475.45 | 42.1% | 436% |
| CTSH | bear | 25% | 0.0% | 12.9% | 8.3% | 54.65 | 17.4% | 99% |
| CTSH | base | 50% | 4.9% | 15.0% | 14.2% | 78.17 | 27.9% | 213% |
| CTSH | bull | 25% | 8.8% | 16.6% | 15.0% | 98.78 | 34.4% | 304% |
| FOXA | bear | 25% | -1.0% | 17.5% | 6.5% | 69.36 | 13.9% | 78% |
| FOXA | base | 50% | 4.7% | 20.1% | 54.7% | 137.13 | 33.7% | 298% |
| FOXA | bull | 25% | 9.3% | 22.0% | 60.0% | 193.55 | 44.1% | 473% |
| ACN | bear | 25% | 2.1% | 13.4% | 9.3% | 145.26 | 13.2% | 72% |
| ACN | base | 50% | 6.9% | 14.7% | 18.9% | 204.72 | 23.1% | 166% |
| ACN | bull | 25% | 10.8% | 15.8% | 19.0% | 248.26 | 28.5% | 230% |
| TTD | bear | 25% | 13.6% | 13.1% | 9.3% | 17.90 | 8.6% | 46% |
| TTD | base | 50% | 19.8% | 17.1% | 41.0% | 37.51 | 29.2% | 247% |
| TTD | bull | 25% | 24.8% | 20.7% | 44.1% | 49.78 | 37.6% | 368% |
| OMC | bear | 25% | 18.4% | 12.7% | 6.5% | 125.76 | 18.5% | 145% |
| OMC | base | 50% | 25.0% | 14.6% | 6.5% | 186.37 | 27.8% | 260% |
| OMC | bull | 25% | 30.3% | 15.9% | 6.5% | 241.30 | 34.2% | 364% |
| CMCSA | bear | 25% | -6.1% | 16.1% | 6.5% | 30.82 | 14.0% | 75% |
| CMCSA | base | 50% | 1.2% | 18.7% | 6.5% | 38.95 | 17.7% | 129% |
| CMCSA | bull | 25% | 7.0% | 20.4% | 6.5% | 52.39 | 23.2% | 209% |
| CPAY | bear | 25% | 7.7% | 39.8% | 7.4% | 318.46 | 6.5% | 34% |
| CPAY | base | 50% | 13.3% | 44.0% | 30.0% | 543.28 | 20.4% | 147% |
| CPAY | bull | 25% | 17.9% | 47.4% | 30.3% | 719.28 | 27.9% | 233% |
| ADBE | bear | 25% | 8.6% | 29.7% | 11.0% | 174.61 | 7.0% | 34% |
| ADBE | base | 50% | 13.3% | 33.6% | 57.2% | 257.76 | 17.8% | 116% |
| ADBE | bull | 25% | 17.1% | 36.9% | 58.3% | 322.80 | 24.3% | 178% |
| ELV | bear | 25% | -1.3% | 4.9% | 7.0% | 452.83 | 10.8% | 58% |
| ELV | base | 50% | 4.9% | 5.9% | 7.0% | 503.94 | 12.6% | 83% |
| ELV | bull | 25% | 9.9% | 6.6% | 7.0% | 662.41 | 18.8% | 141% |
| HPQ | bear | 25% | -3.6% | 5.7% | 8.8% | 25.06 | 13.2% | 69% |
| HPQ | base | 50% | 1.8% | 6.6% | 8.8% | 23.33 | 10.8% | 70% |
| HPQ | bull | 25% | 6.2% | 7.3% | 8.8% | 30.06 | 16.0% | 120% |
| IT | bear | 25% | -2.2% | 13.0% | 8.0% | 100.06 | 2.3% | 10% |
| IT | base | 50% | 3.2% | 17.1% | 47.6% | 211.90 | 22.0% | 157% |
| IT | bull | 25% | 7.5% | 20.7% | 51.6% | 318.55 | 33.8% | 298% |
| HUM | bear | 25% | 12.4% | 2.5% | 8.0% | 334.90 | 4.1% | 22% |
| HUM | base | 50% | 19.0% | 3.7% | 8.0% | 554.58 | 15.2% | 104% |
| HUM | bull | 25% | 24.3% | 4.8% | 8.0% | 792.13 | 23.6% | 192% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 8.8%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- UHS — bounds: share_change_floor_hit;intrinsic_2x_price
- CTSH — bounds: intrinsic_2x_price
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit;wacc_floor_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- TTD — bounds: intrinsic_2x_price
- OMC — bounds: base_growth_cap_hit;wacc_floor_hit;reinvestment_cap_hit;intrinsic_2x_price
- ARE — bounds: specialist_model_v1
- BXP — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- CPT — bounds: specialist_model_v1
- AVB — bounds: specialist_model_v1
- ADBE — bounds: share_change_floor_hit
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- UDR — bounds: specialist_model_v1
- EQR — bounds: specialist_model_v1
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| ORCL | drawdown_from_high | nan% | -41% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| ZTS | drawdown_from_high | nan% | -41% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| HON | weekly_drop;drawdown_from_high | -51% | -53% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| CHTR | drawdown_from_high | nan% | -41% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- VICI: nan
- TTD: heavy_sbc
- OMC: incremental_roic_below_wacc
- ARE: nan
- BXP: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- CPT: nan
- CPAY: thin_interest_coverage
- AVB: nan
- ADBE: heavy_sbc
- ELV: incremental_roic_below_wacc
- HPQ: incremental_roic_below_wacc
- UDR: nan
- EQR: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc

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
- MCO Moody's Corporation — financial_sector_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
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
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- ORCL Oracle Corporation — material_event_requires_reunderwriting
- ZTS Zoetis Inc. — material_event_requires_reunderwriting
- HON Honeywell International Inc. — material_event_requires_reunderwriting
- CHTR Charter Communications, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- COP ConocoPhillips — insufficient_model_confidence
- VLO Valero Energy Corporation — insufficient_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_model_confidence
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
- TRGP Targa Resources Corp. — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
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
