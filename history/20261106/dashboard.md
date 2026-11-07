# Weekly US Stock Screen — 2026-11-06

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-11-06**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 514 | - |
| step2_hard_filters | 514 | 298 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 17 |
| step3_standardize | 298 | 298 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 298 | 291 | no_normalized_earnings: 7 |
| step5_quality_risk | 291 | 287 | - |
| step6_scenario_valuation | 287 | 265 | insufficient_post_valuation_model_confidence: 16, roic_not_meaningful:meaningless_capital: 4, invalid_valuation_output: 1 |
| step7_risk_adjusted_ranking | 324 | 324 | - |

## Eligible Candidates (8)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FOX | 14.8% | 30.9% | 14.5% | 39.7% | 0.0% | 0% | 0.94 | 0.78 |
| 2 | VICI | 9.4% | 31.6% | 15.1% | 31.6% | 0.0% | 0% | 0.51 | 0.48 |
| 3 | ARE | 8.2% | 29.1% | 20.0% | 29.1% | 0.0% | 0% | 0.69 | 0.48 |
| 4 | CMCSA | 3.8% | 19.4% | 13.3% | 22.1% | 0.0% | 0% | 0.76 | 0.51 |
| 5 | CPT | 3.7% | 23.1% | 10.4% | 23.1% | 1.6% | 0% | 0.58 | 0.48 |
| 6 | UHS | 3.1% | 23.3% | 6.4% | 33.1% | 5.6% | 0% | 0.76 | 0.76 |
| 7 | BXP | 2.9% | 20.5% | 10.8% | 20.5% | 1.2% | 0% | 0.66 | 0.48 |
| 8 | CF | 1.0% | 34.5% | 4.8% | 53.1% | 7.2% | 0% | 0.89 | 0.36 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FOX | 14.8% | 30.9% | 14.5% | 39.7% | 0.0% | 0% | 0.94 | 0.78 |
| 2 | VICI | 9.4% | 31.6% | 15.1% | 31.6% | 0.0% | 0% | 0.51 | 0.48 |
| 3 | ARE | 8.2% | 29.1% | 20.0% | 29.1% | 0.0% | 0% | 0.69 | 0.48 |
| 4 | CMCSA | 3.8% | 19.4% | 13.3% | 22.1% | 0.0% | 0% | 0.76 | 0.51 |
| 5 | CPT | 3.7% | 23.1% | 10.4% | 23.1% | 1.6% | 0% | 0.58 | 0.48 |
| 6 | UHS | 3.1% | 23.3% | 6.4% | 33.1% | 5.6% | 0% | 0.76 | 0.76 |
| 7 | BXP | 2.9% | 20.5% | 10.8% | 20.5% | 1.2% | 0% | 0.66 | 0.48 |
| 8 | CF | 1.0% | 34.5% | 4.8% | 53.1% | 7.2% | 0% | 0.89 | 0.36 |
| 9 | HUM | -2.3% | 16.0% | 7.2% | 23.3% | 4.8% | 0% | 0.87 | 0.63 |
| 10 | UDR | -2.3% | 20.2% | 5.8% | 20.2% | 6.2% | 0% | 0.53 | 0.48 |
| 11 | VMRK | -3.0% | 17.8% | 6.2% | 22.3% | 5.8% | 0% | 0.60 | 0.48 |
| 12 | ELV | -4.4% | 10.6% | 7.6% | 16.6% | 4.4% | 0% | 0.84 | 0.67 |
| 13 | INVH | -4.9% | 16.8% | 4.8% | 16.8% | 7.2% | 0% | 0.58 | 0.48 |
| 14 | OMC | -5.1% | 13.6% | 5.9% | 19.0% | 6.1% | 0% | 0.86 | 0.62 |
| 15 | ADBE | -5.8% | 14.3% | 4.3% | 20.4% | 7.7% | 0% | 0.98 | 0.79 |
| 16 | DECK | -5.9% | 15.3% | 3.9% | 22.4% | 8.1% | 0% | 0.96 | 0.67 |
| 17 | APA | -6.4% | 25.4% | 0.5% | 45.2% | 11.5% | 0% | 0.76 | 0.38 |
| 18 | CTSH | -6.7% | 13.3% | 4.1% | 19.5% | 7.9% | 0% | 0.86 | 0.87 |
| 19 | O | -7.3% | 17.2% | 2.2% | 17.2% | 9.8% | 0% | 0.50 | 0.48 |
| 20 | TSN | -7.3% | 15.1% | 2.9% | 27.8% | 9.1% | 0% | 0.60 | 0.58 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CF | 31.7% | 34.5% | 4.8% | 53.1% | 75% | 170% |
| 2 | CI | 30.1% | 33.6% | -9.8% | 63.1% | 75% | 195% |
| 3 | FOX | 29.0% | 30.9% | 14.5% | 39.7% | 100% | 127% |
| 4 | VICI | 27.5% | 31.6% | 15.1% | 31.6% | 100% | 295% |
| 5 | ARE | 26.8% | 29.1% | 20.0% | 29.1% | 100% | 259% |
| 6 | APA | 24.1% | 25.4% | 0.5% | 45.2% | 75% | 139% |
| 7 | UHS | 21.6% | 23.3% | 6.4% | 33.1% | 75% | 65% |
| 8 | CPT | 19.9% | 23.1% | 10.4% | 23.1% | 75% | 183% |
| 9 | EOG | 19.7% | 20.1% | 0.2% | 38.5% | 75% | 74% |
| 10 | CHTR | 19.1% | 49.9% | -95.0% | 71.6% | 75% | 341% |
| 11 | CMCSA | 18.5% | 19.4% | 13.3% | 22.1% | 100% | 66% |
| 12 | BXP | 18.1% | 20.5% | 10.8% | 20.5% | 75% | 154% |
| 13 | UDR | 16.6% | 20.2% | 5.8% | 20.2% | 75% | 151% |
| 14 | VMRK | 16.0% | 17.8% | 6.2% | 22.3% | 75% | 126% |
| 15 | HUM | 15.6% | 16.0% | 7.2% | 23.3% | 75% | 43% |
| 16 | TSN | 15.2% | 15.1% | 2.9% | 27.8% | 75% | 45% |
| 17 | DECK | 14.2% | 15.3% | 3.9% | 22.4% | 75% | 20% |
| 18 | KDP | 14.0% | 16.3% | -6.8% | 30.3% | 75% | 53% |
| 19 | INVH | 13.8% | 16.8% | 4.8% | 16.8% | 75% | 117% |
| 20 | O | 13.5% | 17.2% | 2.2% | 17.2% | 75% | 121% |

## Week-over-week

Previous run: 2026-10-30

- Entered Robust Top: APA, FOX
- Exited Robust Top: FOXA, HPQ
- Entered Upside Top: FOX, KDP, O
- Exited Upside Top: FISV, FOXA, OMC

Largest robust-rank moves:

- CVS: 252 → 116 (+136)
- KDP: 141 → 40 (+101)
- FICO: 169 → 96 (+73)
- TPL: 115 → 69 (+46)
- EXPD: 132 → 88 (+44)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| FOX | bear | 25% | -1.0% | 19.8% | 7.4% | 77.25 | 14.5% | 80% |
| FOX | base | 50% | 4.4% | 22.2% | 47.7% | 134.95 | 30.9% | 254% |
| FOX | bull | 25% | 8.6% | 24.1% | 50.3% | 180.66 | 39.7% | 383% |
| CMCSA | bear | 25% | -6.7% | 16.1% | 6.6% | 29.91 | 13.3% | 71% |
| CMCSA | base | 50% | 0.4% | 18.7% | 6.6% | 40.40 | 19.4% | 135% |
| CMCSA | bull | 25% | 6.0% | 20.4% | 6.6% | 49.52 | 22.1% | 195% |
| UHS | bear | 25% | 1.8% | 8.8% | 8.3% | 167.71 | 6.4% | 31% |
| UHS | base | 50% | 7.1% | 10.7% | 16.7% | 322.67 | 23.3% | 173% |
| UHS | bull | 25% | 11.3% | 12.1% | 18.9% | 462.44 | 33.1% | 298% |
| CF | bear | 25% | -10.1% | 22.8% | 7.0% | 108.91 | 4.8% | 22% |
| CF | base | 50% | 11.9% | 31.1% | 18.7% | 321.85 | 34.5% | 319% |
| CF | bull | 25% | 29.5% | 38.4% | 20.1% | 651.40 | 53.1% | 731% |
| HUM | bear | 25% | 14.6% | 2.6% | 8.3% | 418.19 | 7.2% | 41% |
| HUM | base | 50% | 19.2% | 3.7% | 8.3% | 619.36 | 16.0% | 111% |
| HUM | bull | 25% | 22.8% | 4.8% | 8.3% | 839.28 | 23.3% | 187% |
| ELV | bear | 25% | -0.1% | 4.9% | 7.5% | 430.28 | 7.6% | 40% |
| ELV | base | 50% | 6.2% | 5.9% | 7.5% | 495.71 | 10.6% | 68% |
| ELV | bull | 25% | 11.2% | 6.6% | 7.5% | 646.94 | 16.6% | 119% |
| OMC | bear | 25% | 18.8% | 12.9% | 7.3% | 118.28 | 5.9% | 36% |
| OMC | base | 50% | 25.0% | 14.6% | 7.3% | 171.56 | 13.6% | 95% |
| OMC | bull | 25% | 30.0% | 15.9% | 7.3% | 219.26 | 19.0% | 149% |
| ADBE | bear | 25% | 9.1% | 29.7% | 11.3% | 180.34 | 4.3% | 20% |
| ADBE | base | 50% | 13.6% | 33.6% | 58.7% | 262.31 | 14.3% | 88% |
| ADBE | bull | 25% | 17.1% | 36.9% | 59.8% | 325.09 | 20.4% | 140% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.1% | 68.57 | 3.9% | 18% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 104.36 | 15.3% | 96% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 134.17 | 22.4% | 161% |
| APA | bear | 25% | -12.7% | 21.3% | 6.9% | 36.37 | 0.5% | 2% |
| APA | base | 50% | 11.6% | 31.8% | 8.5% | 106.60 | 25.4% | 208% |
| APA | bull | 25% | 31.1% | 40.8% | 8.9% | 236.37 | 45.2% | 585% |
| CTSH | bear | 25% | -0.6% | 12.8% | 8.7% | 53.60 | 4.1% | 19% |
| CTSH | base | 50% | 4.4% | 15.0% | 14.0% | 76.06 | 13.3% | 83% |
| CTSH | bull | 25% | 8.4% | 16.6% | 14.9% | 95.99 | 19.5% | 137% |
| TSN | bear | 25% | -4.0% | 4.2% | 7.2% | 49.24 | 2.9% | 14% |
| TSN | base | 50% | 3.4% | 6.8% | 7.2% | 86.83 | 15.1% | 112% |
| TSN | bull | 25% | 9.3% | 8.9% | 7.2% | 151.29 | 27.8% | 266% |

## Boundary Assumptions & Valuation Alerts

- FOX — bounds: share_change_floor_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- ARE — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;reinvestment_cap_hit
- CPT — bounds: specialist_model_v1
- UHS — bounds: share_change_floor_hit
- BXP — bounds: specialist_model_v1
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- UDR — bounds: specialist_model_v1
- VMRK — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- INVH — bounds: specialist_model_v1
- OMC — bounds: base_growth_cap_hit;share_change_cap_hit;reinvestment_cap_hit
- ADBE — bounds: share_change_floor_hit
- DECK — bounds: forward_roic_cap_hit;share_change_floor_hit
- APA — bounds: reinvestment_cap_hit;intrinsic_2x_price
- O — bounds: specialist_model_v1
- TSN — bounds: forward_roic_floor_hit;reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| DELL | weekly_drop;drawdown_from_high | -28% | -43% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| NOW | weekly_drop | -36% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| FIX | drawdown_from_high | nan% | -44% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| CIEN | drawdown_from_high | nan% | -45% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| LRCX | drawdown_from_high | nan% | -42% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| MRVL | weekly_drop;drawdown_from_high | -38% | -51% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SNDK | weekly_drop;drawdown_from_high | -33% | -56% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| WDC | drawdown_from_high | nan% | -48% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| FTNT | weekly_drop | -34% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| DDOG | weekly_drop | -34% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| LITE | weekly_drop;drawdown_from_high | -29% | -52% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| TER | weekly_drop;drawdown_from_high | -29% | -51% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| FLEX | drawdown_from_high | nan% | -45% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| FFIV | weekly_drop | -32% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- VICI: nan
- ARE: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- CPT: nan
- BXP: nan
- CF: cyclical_revenue
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- UDR: nan
- VMRK: nan
- ELV: incremental_roic_below_wacc
- INVH: nan
- OMC: ongoing_dilution, incremental_roic_below_wacc
- ADBE: heavy_sbc
- APA: cyclical_revenue, incremental_roic_below_wacc
- O: nan
- TSN: thin_interest_coverage, incremental_roic_below_wacc

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
- ARES Ares Management Corporation — asset_management_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
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
- NOW ServiceNow, Inc. — material_event_requires_reunderwriting
- FIX Comfort Systems USA, Inc. — material_event_requires_reunderwriting
- CIEN Ciena Corporation — material_event_requires_reunderwriting
- LRCX Lam Research Corporation — material_event_requires_reunderwriting
- MRVL Marvell Technology, Inc. — material_event_requires_reunderwriting
- SNDK Sandisk Corporation — material_event_requires_reunderwriting
- WDC Western Digital Corporation — material_event_requires_reunderwriting
- FTNT Fortinet, Inc. — material_event_requires_reunderwriting
- DDOG Datadog, Inc. — material_event_requires_reunderwriting
- LITE Lumentum Holdings Inc. — material_event_requires_reunderwriting
- TER Teradyne, Inc. — material_event_requires_reunderwriting
- FLEX Flex Ltd. — material_event_requires_reunderwriting
- FFIV F5, Inc. — material_event_requires_reunderwriting
- CCL Carnival Corporation & plc — insufficient_model_confidence
- NRG NRG Energy, Inc. — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- TSLA Tesla, Inc. — insufficient_model_confidence
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- IFF International Flavors & Fragrances Inc. — irr_below_solver_bound
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- VRSK Verisk Analytics, Inc. — roic_not_meaningful:meaningless_capital
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
