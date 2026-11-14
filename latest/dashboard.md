# Weekly US Stock Screen — 2026-11-13

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-11-13**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 514 | - |
| step2_hard_filters | 514 | 307 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 17 |
| step3_standardize | 307 | 307 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 307 | 299 | no_normalized_earnings: 8 |
| step5_quality_risk | 299 | 296 | - |
| step6_scenario_valuation | 296 | 273 | insufficient_post_valuation_model_confidence: 17, roic_not_meaningful:meaningless_capital: 4, invalid_valuation_output: 1 |
| step7_risk_adjusted_ranking | 332 | 332 | - |

## Eligible Candidates (8)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | BRK-B | 158.5% | 342.2% | 238.7% | 382.9% | 0.0% | 0% | 0.26 | 0.48 |
| 2 | FOX | 13.0% | 28.7% | 12.9% | 37.2% | 0.0% | 0% | 0.93 | 0.78 |
| 3 | ARE | 7.8% | 28.2% | 19.5% | 28.2% | 0.0% | 0% | 0.70 | 0.48 |
| 4 | VICI | 7.8% | 28.1% | 13.4% | 28.1% | 0.0% | 0% | 0.54 | 0.48 |
| 5 | CPT | 3.0% | 22.3% | 10.0% | 22.3% | 2.0% | 0% | 0.59 | 0.48 |
| 6 | UHS | 1.8% | 22.5% | 5.8% | 32.0% | 6.2% | 0% | 0.75 | 0.77 |
| 7 | BXP | 1.7% | 19.3% | 10.2% | 19.3% | 1.8% | 0% | 0.67 | 0.48 |
| 8 | CMCSA | 1.4% | 17.0% | 10.8% | 19.8% | 1.2% | 0% | 0.75 | 0.51 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | BRK-B | 158.5% | 342.2% | 238.7% | 382.9% | 0.0% | 0% | 0.26 | 0.48 |
| 2 | FOX | 13.0% | 28.7% | 12.9% | 37.2% | 0.0% | 0% | 0.93 | 0.78 |
| 3 | ARE | 7.8% | 28.2% | 19.5% | 28.2% | 0.0% | 0% | 0.70 | 0.48 |
| 4 | VICI | 7.8% | 28.1% | 13.4% | 28.1% | 0.0% | 0% | 0.54 | 0.48 |
| 5 | CPT | 3.0% | 22.3% | 10.0% | 22.3% | 2.0% | 0% | 0.59 | 0.48 |
| 6 | UHS | 1.8% | 22.5% | 5.8% | 32.0% | 6.2% | 0% | 0.75 | 0.77 |
| 7 | BXP | 1.7% | 19.3% | 10.2% | 19.3% | 1.8% | 0% | 0.67 | 0.48 |
| 8 | CMCSA | 1.4% | 17.0% | 10.8% | 19.8% | 1.2% | 0% | 0.75 | 0.51 |
| 9 | CF | -1.7% | 31.7% | 3.1% | 49.8% | 8.9% | 0% | 0.89 | 0.36 |
| 10 | VMRK | -4.5% | 16.1% | 5.5% | 20.2% | 6.5% | 0% | 0.62 | 0.48 |
| 11 | HUM | -4.6% | 14.6% | 5.8% | 21.8% | 6.2% | 0% | 0.87 | 0.63 |
| 12 | UDR | -4.9% | 17.5% | 4.5% | 17.5% | 7.5% | 0% | 0.56 | 0.48 |
| 13 | ELV | -5.3% | 9.7% | 6.7% | 15.6% | 5.3% | 0% | 0.83 | 0.67 |
| 14 | CTSH | -6.7% | 13.1% | 4.3% | 19.2% | 7.7% | 0% | 0.85 | 0.87 |
| 15 | DECK | -6.8% | 14.6% | 3.5% | 21.6% | 8.5% | 0% | 0.96 | 0.67 |
| 16 | INVH | -6.9% | 14.8% | 3.8% | 14.8% | 8.2% | 0% | 0.60 | 0.48 |
| 17 | OMC | -7.4% | 12.2% | 4.5% | 17.6% | 7.5% | 0% | 0.86 | 0.62 |
| 18 | ADBE | -7.5% | 13.3% | 3.5% | 19.2% | 8.5% | 0% | 0.98 | 0.79 |
| 19 | APA | -8.9% | 22.3% | -0.8% | 42.1% | 12.8% | 0% | 0.76 | 0.38 |
| 20 | HPQ | -9.2% | 2.8% | 2.8% | 8.8% | 9.2% | 0% | 0.97 | 0.67 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | BRK-B | 326.5% | 342.2% | 238.7% | 382.9% | 100% | 169008% |
| 2 | CF | 29.1% | 31.7% | 3.1% | 49.8% | 75% | 143% |
| 3 | CI | 28.2% | 31.6% | -11.0% | 60.4% | 75% | 171% |
| 4 | FOX | 26.9% | 28.7% | 12.9% | 37.2% | 100% | 108% |
| 5 | ARE | 26.0% | 28.2% | 19.5% | 28.2% | 100% | 246% |
| 6 | VICI | 24.5% | 28.1% | 13.4% | 28.1% | 100% | 246% |
| 7 | APA | 21.4% | 22.3% | -0.8% | 42.1% | 75% | 110% |
| 8 | UHS | 20.7% | 22.5% | 5.8% | 32.0% | 75% | 58% |
| 9 | CPT | 19.3% | 22.3% | 10.0% | 22.3% | 75% | 174% |
| 10 | EOG | 17.4% | 17.6% | -1.8% | 36.1% | 75% | 56% |
| 11 | BXP | 17.0% | 19.3% | 10.2% | 19.3% | 75% | 142% |
| 12 | CMCSA | 16.2% | 17.0% | 10.8% | 19.8% | 75% | 48% |
| 13 | VMRK | 14.5% | 16.1% | 5.5% | 20.2% | 75% | 111% |
| 14 | UDR | 14.2% | 17.5% | 4.5% | 17.5% | 75% | 124% |
| 15 | HUM | 14.2% | 14.6% | 5.8% | 21.8% | 75% | 32% |
| 16 | DECK | 13.6% | 14.6% | 3.5% | 21.6% | 75% | 16% |
| 17 | KDP | 12.7% | 14.9% | -7.9% | 28.7% | 75% | 42% |
| 18 | CTSH | 12.4% | 13.1% | 4.3% | 19.2% | 75% | 15% |
| 19 | ADBE | 12.3% | 13.3% | 3.5% | 19.2% | 75% | 4% |
| 20 | INVH | 12.0% | 14.8% | 3.8% | 14.8% | 75% | 99% |

## Week-over-week

Previous run: 2026-11-06

- Entered Robust Top: BRK-B, HPQ
- Exited Robust Top: O, TSN
- Entered Upside Top: ADBE, BRK-B, CTSH
- Exited Upside Top: CHTR, O, TSN

Largest robust-rank moves:

- BRK-B: 183 → 1 (+182)
- ADM: 91 → 243 (-152)
- VZ: 90 → 143 (-53)
- TXT: 157 → 117 (+40)
- TSN: 20 → 58 (-38)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| FOX | bear | 25% | -1.0% | 19.8% | 7.7% | 73.94 | 12.9% | 69% |
| FOX | base | 50% | 4.4% | 22.2% | 47.5% | 127.08 | 28.7% | 226% |
| FOX | bull | 25% | 8.7% | 24.1% | 50.3% | 169.21 | 37.2% | 344% |
| UHS | bear | 25% | 1.8% | 8.8% | 8.5% | 160.68 | 5.8% | 28% |
| UHS | base | 50% | 7.1% | 10.7% | 16.7% | 306.83 | 22.5% | 164% |
| UHS | bull | 25% | 11.3% | 12.1% | 18.9% | 438.09 | 32.0% | 283% |
| CMCSA | bear | 25% | -6.7% | 16.1% | 6.9% | 27.59 | 10.8% | 55% |
| CMCSA | base | 50% | 0.4% | 18.7% | 6.9% | 37.22 | 17.0% | 114% |
| CMCSA | bull | 25% | 6.0% | 20.4% | 6.9% | 45.50 | 19.8% | 168% |
| CF | bear | 25% | -9.7% | 22.8% | 7.3% | 105.68 | 3.1% | 14% |
| CF | base | 50% | 12.3% | 31.1% | 18.7% | 303.61 | 31.7% | 280% |
| CF | bull | 25% | 29.8% | 38.4% | 20.1% | 606.98 | 49.8% | 646% |
| HUM | bear | 25% | 14.4% | 2.6% | 8.5% | 401.31 | 5.8% | 32% |
| HUM | base | 50% | 19.3% | 3.7% | 8.5% | 595.53 | 14.6% | 98% |
| HUM | bull | 25% | 23.2% | 4.8% | 8.5% | 809.78 | 21.8% | 170% |
| ELV | bear | 25% | -0.1% | 4.9% | 7.8% | 414.13 | 6.7% | 35% |
| ELV | base | 50% | 6.2% | 5.9% | 7.8% | 472.12 | 9.7% | 60% |
| ELV | bull | 25% | 11.3% | 6.6% | 7.8% | 616.33 | 15.6% | 109% |
| CTSH | bear | 25% | -0.5% | 12.8% | 9.0% | 51.96 | 4.3% | 20% |
| CTSH | base | 50% | 4.4% | 15.0% | 14.0% | 72.72 | 13.1% | 81% |
| CTSH | bull | 25% | 8.3% | 16.6% | 14.9% | 91.10 | 19.2% | 134% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.4% | 66.77 | 3.5% | 16% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 100.67 | 14.6% | 90% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 128.96 | 21.6% | 152% |
| OMC | bear | 25% | 18.7% | 12.9% | 7.6% | 110.67 | 4.5% | 27% |
| OMC | base | 50% | 25.0% | 14.6% | 7.6% | 161.59 | 12.2% | 83% |
| OMC | bull | 25% | 30.0% | 15.9% | 7.6% | 207.07 | 17.6% | 134% |
| ADBE | bear | 25% | 9.1% | 29.7% | 11.6% | 175.39 | 3.5% | 16% |
| ADBE | base | 50% | 13.6% | 33.6% | 58.7% | 253.32 | 13.3% | 80% |
| ADBE | bull | 25% | 17.1% | 36.9% | 59.8% | 313.17 | 19.2% | 130% |
| APA | bear | 25% | -11.0% | 21.3% | 7.1% | 36.96 | -0.8% | -3% |
| APA | base | 50% | 13.4% | 31.8% | 8.6% | 101.81 | 22.3% | 176% |
| APA | bull | 25% | 32.9% | 40.8% | 8.9% | 226.33 | 42.1% | 513% |
| HPQ | bear | 25% | -1.5% | 5.7% | 9.7% | 22.86 | 4.4% | 20% |
| HPQ | base | 50% | 3.8% | 6.6% | 9.7% | 19.64 | 2.8% | 16% |
| HPQ | bull | 25% | 8.0% | 7.3% | 9.7% | 27.06 | 8.8% | 57% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 9.7%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- BRK-B — bounds: specialist_model_v1
- FOX — bounds: share_change_floor_hit;intrinsic_2x_price
- ARE — bounds: specialist_model_v1
- VICI — bounds: specialist_model_v1
- CPT — bounds: specialist_model_v1
- UHS — bounds: share_change_floor_hit
- BXP — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;reinvestment_cap_hit
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- VMRK — bounds: specialist_model_v1
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- UDR — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- DECK — bounds: forward_roic_cap_hit;share_change_floor_hit
- INVH — bounds: specialist_model_v1
- OMC — bounds: base_growth_cap_hit;share_change_cap_hit;reinvestment_cap_hit
- ADBE — bounds: share_change_floor_hit
- APA — bounds: reinvestment_cap_hit;intrinsic_2x_price
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| DELL | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| MRVL | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SNDK | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| LITE | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| TER | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- BRK-B: nan
- ARE: nan
- VICI: nan
- CPT: nan
- BXP: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- CF: cyclical_revenue
- VMRK: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- UDR: nan
- ELV: incremental_roic_below_wacc
- INVH: nan
- OMC: ongoing_dilution, incremental_roic_below_wacc
- ADBE: heavy_sbc
- APA: cyclical_revenue, incremental_roic_below_wacc
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
- SPGI S&P Global Inc. — financial_sector_model_not_supported
- COF Capital One Financial Corporation — consumer_finance_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- ARES Ares Management Corporation — asset_management_model_not_supported
- RJF Raymond James Financial, Inc. — asset_management_model_not_supported
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
- BEN Franklin Resources, Inc. — asset_management_model_not_supported
- IVZ Invesco Ltd. — asset_management_model_not_supported
- FDS FactSet Research Systems Inc. — financial_sector_model_not_supported
- CME CME Group Inc. — financial_sector_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- DELL Dell Technologies Inc. — material_event_requires_reunderwriting
- MRVL Marvell Technology, Inc. — material_event_requires_reunderwriting
- SNDK Sandisk Corporation — material_event_requires_reunderwriting
- LITE Lumentum Holdings Inc. — material_event_requires_reunderwriting
- TER Teradyne, Inc. — material_event_requires_reunderwriting
- CCL Carnival Corporation & plc — insufficient_model_confidence
- NRG NRG Energy, Inc. — insufficient_model_confidence
- TSLA Tesla, Inc. — insufficient_model_confidence
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- IFF International Flavors & Fragrances Inc. — irr_below_solver_bound
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- XOM Exxonmobil Holdings Corporation — insufficient_post_valuation_model_confidence
- CVX Chevron Corporation — insufficient_post_valuation_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_post_valuation_model_confidence
- VLO Valero Energy Corporation — insufficient_post_valuation_model_confidence
- PSX Phillips 66 — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- DVN Devon Energy Corporation — insufficient_post_valuation_model_confidence
- XYZ Block, Inc. — insufficient_post_valuation_model_confidence
- MOS The Mosaic Company — insufficient_post_valuation_model_confidence
- NVDA NVIDIA Corporation — insufficient_post_valuation_model_confidence
- MU Micron Technology, Inc. — insufficient_post_valuation_model_confidence
- AMD Advanced Micro Devices, Inc. — insufficient_post_valuation_model_confidence
- APP AppLovin Corporation — insufficient_post_valuation_model_confidence
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
