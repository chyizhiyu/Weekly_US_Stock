# Weekly US Stock Screen — 2026-11-20

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-11-20**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 514 | - |
| step2_hard_filters | 514 | 288 | adr_excluded: 32, persistent_negative_fcf: 23, material_event_requires_reunderwriting: 22 |
| step3_standardize | 288 | 288 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 288 | 283 | no_normalized_earnings: 5 |
| step5_quality_risk | 283 | 280 | - |
| step6_scenario_valuation | 280 | 259 | insufficient_post_valuation_model_confidence: 15, roic_not_meaningful:meaningless_capital: 4, invalid_valuation_output: 1 |
| step7_risk_adjusted_ranking | 318 | 318 | - |

## Eligible Candidates (9)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FOX | 16.1% | 32.7% | 16.0% | 41.5% | 0.0% | 0% | 0.94 | 0.78 |
| 2 | VICI | 9.7% | 32.1% | 15.6% | 32.1% | 0.0% | 0% | 0.51 | 0.48 |
| 3 | ARE | 9.4% | 31.5% | 22.3% | 31.5% | 0.0% | 0% | 0.70 | 0.48 |
| 4 | UHS | 7.9% | 26.3% | 9.0% | 36.2% | 3.0% | 0% | 0.76 | 0.77 |
| 5 | CPT | 6.2% | 25.2% | 11.8% | 25.2% | 0.2% | 0% | 0.57 | 0.48 |
| 6 | CF | 5.8% | 34.8% | 8.1% | 52.0% | 3.9% | 0% | 0.89 | 0.43 |
| 7 | BXP | 4.5% | 21.6% | 11.9% | 21.6% | 0.1% | 0% | 0.66 | 0.48 |
| 8 | HUM | 1.6% | 18.6% | 9.5% | 26.0% | 2.5% | 0% | 0.87 | 0.63 |
| 9 | CMCSA | 0.4% | 17.8% | 9.1% | 21.9% | 2.9% | 0% | 0.73 | 0.57 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FOX | 16.1% | 32.7% | 16.0% | 41.5% | 0.0% | 0% | 0.94 | 0.78 |
| 2 | VICI | 9.7% | 32.1% | 15.6% | 32.1% | 0.0% | 0% | 0.51 | 0.48 |
| 3 | ARE | 9.4% | 31.5% | 22.3% | 31.5% | 0.0% | 0% | 0.70 | 0.48 |
| 4 | UHS | 7.9% | 26.3% | 9.0% | 36.2% | 3.0% | 0% | 0.76 | 0.77 |
| 5 | CPT | 6.2% | 25.2% | 11.8% | 25.2% | 0.2% | 0% | 0.57 | 0.48 |
| 6 | CF | 5.8% | 34.8% | 8.1% | 52.0% | 3.9% | 0% | 0.89 | 0.43 |
| 7 | BXP | 4.5% | 21.6% | 11.9% | 21.6% | 0.1% | 0% | 0.66 | 0.48 |
| 8 | HUM | 1.6% | 18.6% | 9.5% | 26.0% | 2.5% | 0% | 0.87 | 0.63 |
| 9 | CMCSA | 0.4% | 17.8% | 9.1% | 21.9% | 2.9% | 0% | 0.73 | 0.57 |
| 10 | DECK | -1.3% | 18.3% | 6.5% | 25.5% | 5.5% | 0% | 0.96 | 0.67 |
| 11 | ADBE | -1.5% | 17.0% | 6.6% | 23.1% | 5.4% | 0% | 0.98 | 0.79 |
| 12 | UDR | -1.9% | 20.3% | 6.1% | 20.3% | 5.9% | 0% | 0.53 | 0.48 |
| 13 | VMRK | -2.2% | 18.2% | 6.8% | 22.6% | 5.2% | 0% | 0.60 | 0.48 |
| 14 | CTSH | -2.3% | 15.3% | 6.8% | 21.0% | 5.2% | 0% | 0.86 | 0.88 |
| 15 | ELV | -2.8% | 12.3% | 9.0% | 18.1% | 3.0% | 0% | 0.84 | 0.67 |
| 16 | APA | -3.7% | 25.6% | 3.0% | 45.8% | 9.0% | 0% | 0.76 | 0.39 |
| 17 | INVH | -4.4% | 17.0% | 5.2% | 17.0% | 6.8% | 0% | 0.59 | 0.48 |
| 18 | OMC | -4.9% | 13.7% | 6.0% | 19.1% | 6.0% | 0% | 0.86 | 0.62 |
| 19 | EOG | -6.1% | 20.7% | 2.4% | 39.0% | 9.6% | 0% | 0.87 | 0.40 |
| 20 | INTU | -6.6% | 14.9% | 3.0% | 21.7% | 9.0% | 0% | 0.97 | 0.83 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CF | 32.4% | 34.8% | 8.1% | 52.0% | 75% | 171% |
| 2 | CI | 32.3% | 35.8% | -7.8% | 65.5% | 75% | 220% |
| 3 | FOX | 30.7% | 32.7% | 16.0% | 41.5% | 100% | 139% |
| 4 | ARE | 29.2% | 31.5% | 22.3% | 31.5% | 100% | 293% |
| 5 | VICI | 28.0% | 32.1% | 15.6% | 32.1% | 100% | 303% |
| 6 | APA | 25.0% | 25.6% | 3.0% | 45.8% | 75% | 144% |
| 7 | UHS | 24.4% | 26.3% | 9.0% | 36.2% | 75% | 84% |
| 8 | CPT | 21.8% | 25.2% | 11.8% | 25.2% | 75% | 207% |
| 9 | EOG | 20.7% | 20.7% | 2.4% | 39.0% | 75% | 80% |
| 10 | BXP | 19.2% | 21.6% | 11.9% | 21.6% | 75% | 166% |
| 11 | HUM | 18.1% | 18.6% | 9.5% | 26.0% | 75% | 59% |
| 12 | DECK | 17.1% | 18.3% | 6.5% | 25.5% | 75% | 33% |
| 13 | UDR | 16.8% | 20.3% | 6.1% | 20.3% | 75% | 152% |
| 14 | CMCSA | 16.6% | 17.8% | 9.1% | 21.9% | 75% | 54% |
| 15 | VMRK | 16.5% | 18.2% | 6.8% | 22.6% | 75% | 131% |
| 16 | ADBE | 15.9% | 17.0% | 6.6% | 23.1% | 75% | 20% |
| 17 | CTSH | 14.6% | 15.3% | 6.8% | 21.0% | 75% | 26% |
| 18 | CHTR | 14.2% | 42.7% | -95.0% | 66.6% | 75% | 335% |
| 19 | LDOS | 14.2% | 17.0% | -6.5% | 29.2% | 75% | 48% |
| 20 | INVH | 14.1% | 17.0% | 5.2% | 17.0% | 75% | 120% |

## Week-over-week

Previous run: 2026-11-13

- Entered Robust Top: EOG, INTU
- Exited Robust Top: BRK-B, HPQ
- Entered Upside Top: CHTR, LDOS
- Exited Upside Top: BRK-B, KDP

Largest robust-rank moves:

- BRK-B: 1 → 184 (-183)
- KEYS: 250 → 157 (+93)
- CARR: 323 → 276 (+47)
- J: 316 → 279 (+37)
- EFX: 315 → 283 (+32)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| FOX | bear | 25% | -1.0% | 19.8% | 7.5% | 77.03 | 16.0% | 90% |
| FOX | base | 50% | 4.4% | 22.2% | 47.7% | 134.42 | 32.7% | 275% |
| FOX | bull | 25% | 8.6% | 24.1% | 50.3% | 179.88 | 41.5% | 411% |
| UHS | bear | 25% | 1.9% | 8.8% | 8.2% | 171.55 | 9.0% | 45% |
| UHS | base | 50% | 7.1% | 10.7% | 16.7% | 329.94 | 26.3% | 205% |
| UHS | bull | 25% | 11.3% | 12.1% | 18.9% | 472.22 | 36.2% | 344% |
| CF | bear | 25% | -6.6% | 22.8% | 7.0% | 119.94 | 8.1% | 39% |
| CF | base | 50% | 11.1% | 31.1% | 18.7% | 312.93 | 34.8% | 322% |
| CF | bull | 25% | 25.2% | 38.4% | 20.1% | 586.75 | 52.0% | 688% |
| HUM | bear | 25% | 14.6% | 2.6% | 8.3% | 416.60 | 9.5% | 57% |
| HUM | base | 50% | 19.3% | 3.7% | 8.3% | 618.69 | 18.6% | 135% |
| HUM | bull | 25% | 23.1% | 4.8% | 8.3% | 840.48 | 26.0% | 220% |
| CMCSA | bear | 25% | -6.9% | 15.0% | 6.7% | 25.72 | 9.1% | 45% |
| CMCSA | base | 50% | 0.3% | 18.4% | 6.7% | 38.40 | 17.8% | 120% |
| CMCSA | bull | 25% | 6.2% | 20.7% | 6.7% | 49.93 | 21.9% | 193% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.2% | 68.36 | 6.5% | 31% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 103.92 | 18.3% | 120% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 133.55 | 25.5% | 192% |
| ADBE | bear | 25% | 9.1% | 29.7% | 11.4% | 180.01 | 6.6% | 32% |
| ADBE | base | 50% | 13.6% | 33.6% | 58.7% | 261.71 | 17.0% | 109% |
| ADBE | bull | 25% | 17.1% | 36.9% | 59.8% | 324.30 | 23.1% | 166% |
| CTSH | bear | 25% | -0.4% | 12.9% | 8.7% | 53.58 | 6.8% | 33% |
| CTSH | base | 50% | 4.4% | 15.0% | 12.4% | 73.28 | 15.3% | 98% |
| CTSH | bull | 25% | 8.2% | 16.5% | 13.0% | 90.80 | 21.0% | 152% |
| ELV | bear | 25% | 0.4% | 4.9% | 7.5% | 422.62 | 9.0% | 49% |
| ELV | base | 50% | 6.2% | 5.9% | 7.5% | 495.45 | 12.3% | 81% |
| ELV | bull | 25% | 10.9% | 6.6% | 7.5% | 640.40 | 18.1% | 134% |
| APA | bear | 25% | -9.5% | 21.3% | 6.9% | 40.55 | 3.0% | 13% |
| APA | base | 50% | 14.0% | 31.8% | 8.5% | 110.00 | 25.6% | 217% |
| APA | bull | 25% | 32.8% | 40.8% | 8.9% | 243.08 | 45.8% | 599% |
| OMC | bear | 25% | 18.8% | 12.9% | 7.3% | 117.20 | 6.0% | 36% |
| OMC | base | 50% | 25.0% | 14.6% | 7.3% | 170.15 | 13.7% | 97% |
| OMC | bull | 25% | 30.0% | 15.9% | 7.3% | 217.53 | 19.1% | 151% |
| EOG | bear | 25% | -1.8% | 20.2% | 7.2% | 121.95 | 2.4% | 11% |
| EOG | base | 50% | 21.0% | 29.6% | 8.2% | 267.61 | 20.7% | 162% |
| EOG | bull | 25% | 39.2% | 38.1% | 8.3% | 557.40 | 39.0% | 442% |
| INTU | bear | 25% | 10.9% | 22.6% | 9.1% | 206.23 | 3.0% | 14% |
| INTU | base | 50% | 15.9% | 26.1% | 23.9% | 333.98 | 14.9% | 97% |
| INTU | bull | 25% | 19.9% | 29.1% | 24.4% | 431.78 | 21.7% | 161% |

## Boundary Assumptions & Valuation Alerts

- FOX — bounds: share_change_floor_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- ARE — bounds: specialist_model_v1
- UHS — bounds: share_change_floor_hit
- CPT — bounds: specialist_model_v1
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- BXP — bounds: specialist_model_v1
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;reinvestment_cap_hit
- DECK — bounds: forward_roic_cap_hit;share_change_floor_hit
- ADBE — bounds: share_change_floor_hit
- UDR — bounds: specialist_model_v1
- VMRK — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- APA — bounds: reinvestment_cap_hit;intrinsic_2x_price
- INVH — bounds: specialist_model_v1
- OMC — bounds: base_growth_cap_hit;share_change_cap_hit;reinvestment_cap_hit
- EOG — bounds: reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| CAT | drawdown_from_high | nan% | -41% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| DELL | drawdown_from_high | nan% | -52% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| NOW | drawdown_from_high | nan% | -45% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| GLW | drawdown_from_high | nan% | -44% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| VRT | drawdown_from_high | nan% | -43% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| HPE | drawdown_from_high | nan% | -42% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| FIX | drawdown_from_high | nan% | -43% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| CIEN | drawdown_from_high | nan% | -47% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| P | drawdown_from_high | nan% | -41% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| TWLO | drawdown_from_high | nan% | -43% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| NVDA | weekly_drop;drawdown_from_high | -33% | -48% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| MU | drawdown_from_high | nan% | -46% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| AMAT | drawdown_from_high | nan% | -44% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| LRCX | drawdown_from_high | nan% | -47% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| MRVL | drawdown_from_high | nan% | -57% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| WDC | drawdown_from_high | nan% | -45% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SNDK | drawdown_from_high | nan% | -66% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| DDOG | drawdown_from_high | nan% | -45% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| LITE | drawdown_from_high | nan% | -59% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| TER | drawdown_from_high | nan% | -54% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| FLEX | drawdown_from_high | nan% | -45% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| FSLR | weekly_drop | -32% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- VICI: nan
- ARE: nan
- CPT: nan
- CF: cyclical_revenue
- BXP: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- ADBE: heavy_sbc
- UDR: nan
- VMRK: nan
- ELV: incremental_roic_below_wacc
- APA: cyclical_revenue, incremental_roic_below_wacc
- INVH: nan
- OMC: ongoing_dilution, incremental_roic_below_wacc
- EOG: cyclical_revenue, incremental_roic_below_wacc
- INTU: heavy_sbc

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
- MSCI MSCI Inc. — financial_sector_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
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
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- CAT Caterpillar Inc. — material_event_requires_reunderwriting
- DELL Dell Technologies Inc. — material_event_requires_reunderwriting
- NOW ServiceNow, Inc. — material_event_requires_reunderwriting
- GLW Corning Inc — material_event_requires_reunderwriting
- VRT Vertiv Holdings Co — material_event_requires_reunderwriting
- HPE Hewlett Packard Enterprise Company — material_event_requires_reunderwriting
- FIX Comfort Systems USA, Inc. — material_event_requires_reunderwriting
- CIEN Ciena Corporation — material_event_requires_reunderwriting
- P Everpure, Inc. — material_event_requires_reunderwriting
- TWLO Twilio Inc. — material_event_requires_reunderwriting
- NVDA NVIDIA Corporation — material_event_requires_reunderwriting
- MU Micron Technology, Inc. — material_event_requires_reunderwriting
- AMAT Applied Materials, Inc. — material_event_requires_reunderwriting
- LRCX Lam Research Corporation — material_event_requires_reunderwriting
- MRVL Marvell Technology, Inc. — material_event_requires_reunderwriting
- WDC Western Digital Corporation — material_event_requires_reunderwriting
- SNDK Sandisk Corporation — material_event_requires_reunderwriting
- DDOG Datadog, Inc. — material_event_requires_reunderwriting
- LITE Lumentum Holdings Inc. — material_event_requires_reunderwriting
- TER Teradyne, Inc. — material_event_requires_reunderwriting
- FLEX Flex Ltd. — material_event_requires_reunderwriting
- FSLR First Solar, Inc. — material_event_requires_reunderwriting
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
- PSX Phillips 66 — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- DVN Devon Energy Corporation — insufficient_post_valuation_model_confidence
- XYZ Block, Inc. — insufficient_post_valuation_model_confidence
- IR Ingersoll Rand Inc. — insufficient_post_valuation_model_confidence
- MOS The Mosaic Company — insufficient_post_valuation_model_confidence
- AMD Advanced Micro Devices, Inc. — insufficient_post_valuation_model_confidence
- APP AppLovin Corporation — insufficient_post_valuation_model_confidence
- STLD Steel Dynamics, Inc. — insufficient_post_valuation_model_confidence
- EXPE Expedia Group, Inc. — insufficient_post_valuation_model_confidence

## Data Gaps and Model Limitations

- Stocks missing core financials were rejected (fail closed), never estimated.
- Banks, insurers and REITs use conservative specialist models; rows with
  incomplete specialist inputs stay watchlisted instead of entering ranking.
- Asset managers, consumer-finance names, other financials and pre-profit
  biotech remain watchlisted until dedicated models exist.
- Scenario set is discrete (bear/base/bull); worst-case stress metrics are
  deterministic bear/base/bull stress labels, not calibrated CVaR.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
