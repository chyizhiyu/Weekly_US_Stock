# Weekly US Stock Screen — 2026-06-11

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-06-11**
- Fresh price coverage: **100.0%** (1 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 5888 | - |
| step2_hard_filters | 5888 | 971 | market_cap: 1381, adr_excluded: 1287, listing_age: 477 |
| step3_standardize | 971 | 971 | - |
| step4_normalized_model | 971 | 905 | no_normalized_earnings: 60 |
| step5_quality_risk | 905 | 883 | - |
| step6_scenario_valuation | 883 | 883 | - |
| step7_risk_adjusted_ranking | 883 | 883 | - |

## Robust Top 20 (risk-adjusted)

| # | Ticker | Robust | E[IRR] | P10 | P90 | W(IRR>hurdle) | ES | W(perm loss) | Conf (model/data) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | BRBR | 41.5% | 48.9% | 32.8% | 61.2% | 100% | 0.0% | 0% | 0.82/1.00 |
| 2 | VRRM | 39.3% | 52.2% | 25.2% | 74.1% | 100% | 0.0% | 0% | 0.55/1.00 |
| 3 | TNET | 34.2% | 42.0% | 25.0% | 55.0% | 100% | 0.0% | 0% | 0.80/1.00 |
| 4 | HRB | 31.7% | 42.6% | 19.0% | 60.8% | 100% | 0.0% | 0% | 0.68/1.00 |
| 5 | HLF | 28.7% | 31.1% | 27.5% | 35.7% | 100% | 0.0% | 0% | 0.75/1.00 |
| 6 | EFOR | 25.8% | 29.4% | 22.3% | 35.4% | 100% | 0.0% | 0% | 0.79/1.00 |
| 7 | UHS | 25.0% | 32.3% | 16.3% | 44.4% | 100% | 0.0% | 0% | 0.85/1.00 |
| 8 | OMC | 23.5% | 27.7% | 19.2% | 34.9% | 100% | 0.0% | 0% | 0.84/1.00 |
| 9 | GTM | 22.0% | 41.0% | 0.5% | 72.9% | 75% | 0.0% | 0% | 0.39/1.00 |
| 10 | ALSN | 21.8% | 31.0% | 10.8% | 46.0% | 75% | 0.0% | 0% | 0.73/1.00 |
| 11 | SMPL | 20.8% | 27.1% | 13.8% | 37.0% | 100% | 0.0% | 0% | 0.66/1.00 |
| 12 | CF | 20.0% | 34.8% | 4.1% | 59.6% | 75% | 0.0% | 0% | 0.37/1.00 |
| 13 | INVA | 19.1% | 25.7% | 14.4% | 38.3% | 100% | 0.0% | 0% | 0.56/1.00 |
| 14 | EEFT | 18.8% | 28.3% | 8.0% | 44.5% | 75% | 0.0% | 0% | 0.70/1.00 |
| 15 | FOX | 18.5% | 25.9% | 9.3% | 38.1% | 75% | 0.0% | 0% | 0.85/1.00 |
| 16 | NSP | 18.3% | 28.2% | 7.6% | 45.3% | 75% | 0.0% | 0% | 0.65/1.00 |
| 17 | CMCSA | 17.8% | 20.9% | 15.6% | 26.9% | 100% | 0.0% | 0% | 0.83/1.00 |
| 18 | MMS | 15.9% | 24.5% | 5.9% | 38.9% | 75% | 0.0% | 0% | 0.75/1.00 |
| 19 | DOX | 15.7% | 23.3% | 6.4% | 36.0% | 75% | 0.0% | 0% | 0.83/1.00 |
| 20 | FOXA | 15.1% | 22.5% | 6.1% | 34.5% | 75% | 0.0% | 0% | 0.84/1.00 |

## Upside Top 20 (expected IRR)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | HRMY | 110.0% | 20.0% | 20.0% | 200.0% | 100% | 54% |
| 2 | LHX | 93.6% | -12.9% | -12.9% | 200.0% | 50% | -66% |
| 3 | VRRM | 52.2% | 54.7% | 25.2% | 74.1% | 100% | 393% |
| 4 | BRBR | 48.9% | 50.8% | 32.8% | 61.2% | 100% | 350% |
| 5 | HRB | 42.6% | 45.4% | 19.0% | 60.8% | 100% | 251% |
| 6 | TNET | 42.0% | 43.9% | 25.0% | 55.0% | 100% | 230% |
| 7 | GTM | 41.0% | 45.3% | 0.5% | 72.9% | 75% | 226% |
| 8 | IRWD | 37.2% | 63.8% | -95.0% | 116.2% | 75% | 527% |
| 9 | CF | 34.8% | 37.8% | 4.1% | 59.6% | 75% | 195% |
| 10 | FISV | 33.8% | 41.3% | -14.2% | 66.9% | 75% | 216% |
| 11 | CI | 32.3% | 36.5% | -13.1% | 69.2% | 75% | 201% |
| 12 | UHS | 32.3% | 34.1% | 16.3% | 44.4% | 100% | 131% |
| 13 | HLF | 31.1% | 27.5% | 27.5% | 35.7% | 100% | 166% |
| 14 | ALSN | 31.0% | 33.6% | 10.8% | 46.0% | 75% | 142% |
| 15 | EFOR | 29.4% | 29.9% | 22.3% | 35.4% | 100% | 138% |
| 16 | EEFT | 28.3% | 30.5% | 8.0% | 44.5% | 75% | 116% |
| 17 | NSP | 28.2% | 30.0% | 7.6% | 45.3% | 75% | 138% |
| 18 | OMC | 27.7% | 28.4% | 19.2% | 34.9% | 100% | 156% |
| 19 | SMPL | 27.1% | 28.8% | 13.8% | 37.0% | 100% | 130% |
| 20 | DVN | 26.8% | 29.0% | -11.6% | 60.9% | 75% | 158% |

## Week-over-week

Previous run: 2026-06-11

- Entered Robust Top: CF, CMCSA, DOX, FOX, FOXA, GTM, NSP
- Exited Robust Top: APO, BNY, CRBG, FHI, GDOT, OPFI, WU
- Entered Upside Top: ALSN, EFOR, FISV, GTM, HLF, IRWD, NSP, OMC, SMPL
- Exited Upside Top: APO, BBT, BNY, CRBG, GDOT, MMS, OPFI, REPX, WU

Largest robust-rank moves:

- GTM: 698 → 9 (+689)
- JBI: 730 → 48 (+682)
- WEX: 27 → 709 (-682)
- TFX: 916 → 242 (+674)
- IQV: 864 → 243 (+621)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| BRBR | bear | 25% | 2.7% | 13.7% | 7.0% | 21.49 | 32.8% | 285% |
| BRBR | base | 50% | 8.6% | 16.1% | 12.3% | 40.10 | 50.8% | 654% |
| BRBR | bull | 25% | 13.3% | 18.1% | 12.9% | 57.19 | 61.2% | 995% |
| VRRM | bear | 25% | -4.1% | 15.0% | 6.9% | 8.54 | 25.2% | 160% |
| VRRM | base | 50% | 8.8% | 20.9% | 38.9% | 22.20 | 54.7% | 604% |
| VRRM | bull | 25% | 19.1% | 25.6% | 47.6% | 39.38 | 74.1% | 1165% |
| TNET | bear | 25% | 20.2% | 6.5% | 8.4% | 83.43 | 25.0% | 205% |
| TNET | base | 50% | 25.0% | 8.1% | 28.8% | 157.95 | 43.9% | 502% |
| TNET | bull | 25% | 28.8% | 9.5% | 30.3% | 223.13 | 55.0% | 763% |
| HRB | bear | 25% | -3.9% | 17.2% | 6.5% | 54.04 | 19.0% | 121% |
| HRB | base | 50% | 3.9% | 21.5% | 56.3% | 126.09 | 45.4% | 473% |
| HRB | bull | 25% | 10.0% | 25.3% | 60.0% | 199.67 | 60.8% | 833% |
| HLF | bear | 25% | -5.0% | 8.5% | 8.9% | 31.08 | 33.9% | 221% |
| HLF | base | 50% | 2.6% | 11.0% | 8.9% | 32.44 | 27.5% | 253% |
| HLF | bull | 25% | 8.7% | 12.8% | 8.9% | 44.88 | 35.7% | 389% |
| EFOR | bear | 25% | -7.5% | 6.8% | 6.5% | 33.98 | 22.3% | 152% |
| EFOR | base | 50% | 0.7% | 8.1% | 6.5% | 47.98 | 29.9% | 295% |
| EFOR | bull | 25% | 7.3% | 8.9% | 6.5% | 64.53 | 35.4% | 460% |
| UHS | bear | 25% | 1.7% | 8.9% | 8.0% | 181.50 | 16.3% | 101% |
| UHS | base | 50% | 6.9% | 10.7% | 17.2% | 337.57 | 34.1% | 303% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.6% | 477.87 | 44.4% | 485% |
| OMC | bear | 25% | 18.5% | 12.8% | 6.9% | 130.23 | 19.2% | 154% |
| OMC | base | 50% | 25.0% | 14.6% | 6.9% | 193.52 | 28.4% | 273% |
| OMC | bull | 25% | 30.2% | 15.9% | 6.9% | 251.07 | 34.9% | 382% |
| GTM | bear | 25% | -18.6% | 11.4% | 8.3% | 2.05 | 0.5% | 2% |
| GTM | base | 50% | 16.2% | 16.8% | 14.8% | 8.74 | 45.3% | 474% |
| GTM | bull | 25% | 44.1% | 20.1% | 20.0% | 21.38 | 72.9% | 1388% |
| ALSN | bear | 25% | 15.5% | 25.9% | 7.9% | 121.35 | 10.8% | 66% |
| ALSN | base | 50% | 25.0% | 30.5% | 49.1% | 279.63 | 33.6% | 312% |
| ALSN | bull | 25% | 32.6% | 33.7% | 59.5% | 423.47 | 46.0% | 538% |
| SMPL | bear | 25% | -8.2% | 13.2% | 6.5% | 16.32 | 13.8% | 80% |
| SMPL | base | 50% | 5.5% | 15.9% | 7.2% | 29.13 | 28.8% | 244% |
| SMPL | bull | 25% | 16.4% | 17.5% | 7.4% | 42.26 | 37.0% | 418% |
| CF | bear | 25% | -10.1% | 22.8% | 6.8% | 96.78 | 4.1% | 21% |
| CF | base | 50% | 14.3% | 31.1% | 16.8% | 314.63 | 37.8% | 390% |
| CF | bull | 25% | 33.8% | 38.4% | 18.0% | 674.65 | 59.6% | 1005% |
| INVA | bear | 25% | -4.9% | 54.5% | 7.0% | 29.70 | 14.4% | 90% |
| INVA | base | 50% | 8.8% | 76.9% | 7.0% | 46.09 | 25.1% | 226% |
| INVA | bull | 25% | 19.7% | 94.1% | 7.0% | 74.94 | 38.3% | 445% |
| EEFT | bear | 25% | 0.5% | 8.7% | 7.8% | 64.80 | 8.0% | 43% |
| EEFT | base | 50% | 7.5% | 12.1% | 26.2% | 142.41 | 30.5% | 252% |
| EEFT | bull | 25% | 13.1% | 15.1% | 29.3% | 226.14 | 44.5% | 479% |
| FOX | bear | 25% | -1.0% | 17.5% | 6.8% | 66.23 | 9.3% | 53% |
| FOX | base | 50% | 4.7% | 20.1% | 54.5% | 127.45 | 28.1% | 231% |
| FOX | bull | 25% | 9.2% | 22.0% | 60.0% | 177.82 | 38.1% | 377% |
| NSP | bear | 25% | -6.3% | 2.4% | 7.5% | 38.06 | 7.6% | 41% |
| NSP | base | 50% | 4.8% | 3.8% | 12.5% | 89.79 | 30.0% | 243% |
| NSP | bull | 25% | 13.7% | 4.9% | 15.1% | 153.61 | 45.3% | 495% |
| CMCSA | bear | 25% | -6.1% | 16.1% | 6.5% | 30.83 | 15.6% | 95% |
| CMCSA | base | 50% | 1.2% | 18.7% | 6.5% | 38.94 | 20.6% | 174% |
| CMCSA | bull | 25% | 7.0% | 20.4% | 6.5% | 52.39 | 26.9% | 284% |
| MMS | bear | 25% | -2.2% | 7.5% | 6.5% | 58.97 | 5.9% | 31% |
| MMS | base | 50% | 4.8% | 9.6% | 12.6% | 126.00 | 26.6% | 213% |
| MMS | bull | 25% | 10.3% | 11.2% | 14.0% | 196.61 | 38.9% | 405% |
| DOX | bear | 25% | -2.6% | 11.6% | 6.7% | 55.11 | 6.4% | 34% |
| DOX | base | 50% | 2.8% | 14.0% | 32.3% | 108.10 | 25.4% | 194% |
| DOX | bull | 25% | 7.1% | 15.8% | 36.3% | 154.89 | 36.0% | 335% |
| FOXA | bear | 25% | -1.1% | 17.5% | 6.8% | 65.67 | 6.1% | 33% |
| FOXA | base | 50% | 4.7% | 20.1% | 54.5% | 126.68 | 24.7% | 192% |
| FOXA | bull | 25% | 9.3% | 22.0% | 60.0% | 177.18 | 34.5% | 324% |

## Key Risks and Failure Conditions

- BRBR: elevated_leverage, thin_interest_coverage, incremental_roic_below_wacc
- VRRM: thin_interest_coverage, cyclical_revenue
- TNET: thin_interest_coverage
- HLF: thin_interest_coverage, incremental_roic_below_wacc
- EFOR: thin_interest_coverage, incremental_roic_below_wacc
- OMC: incremental_roic_below_wacc
- GTM: heavy_sbc, cyclical_revenue
- ALSN: elevated_leverage
- SMPL: cyclical_revenue
- CF: cyclical_revenue
- INVA: weak_cash_conversion, incremental_roic_below_wacc
- NSP: thin_interest_coverage
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc

## Watchlist (not rankable under the general model)

- BRK-B Berkshire Hathaway Inc. — insurance_model_not_supported
- BRK-A Berkshire Hathaway Inc. — insurance_model_not_supported
- JPM JPMorgan Chase & Co. — bank_model_not_supported
- V Visa Inc. — consumer_finance_model_not_supported
- MA Mastercard Incorporated — consumer_finance_model_not_supported
- BAC Bank of America Corporation — bank_model_not_supported
- MS Morgan Stanley — asset_management_model_not_supported
- GS The Goldman Sachs Group, Inc. — asset_management_model_not_supported
- WFC Wells Fargo & Company — bank_model_not_supported
- C Citigroup Inc. — bank_model_not_supported
- AXP American Express Company — consumer_finance_model_not_supported
- BLK BlackRock, Inc. — asset_management_model_not_supported
- SCHW The Charles Schwab Corporation — asset_management_model_not_supported
- WELL Welltower Inc. — reit_model_not_supported
- BX Blackstone Inc. — asset_management_model_not_supported
- PLD Prologis, Inc. — reit_model_not_supported
- SPGI S&P Global Inc. — financial_sector_model_not_supported
- PGR The Progressive Corporation — insurance_model_not_supported
- COF Capital One Financial Corporation — consumer_finance_model_not_supported
- PNC The PNC Financial Services Group, Inc. — bank_model_not_supported
- USB U.S. Bancorp — bank_model_not_supported
- AMT American Tower Corporation — reit_model_not_supported
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- MRSH Marsh & McLennan Companies, Inc. — insurance_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- AON Aon plc — insurance_model_not_supported
- SPG Simon Property Group, Inc. — reit_model_not_supported
- TRV The Travelers Companies, Inc. — insurance_model_not_supported
- DLR Digital Realty Trust, Inc. — reit_model_not_supported
- TFC Truist Financial Corporation — bank_model_not_supported
- AFL Aflac Incorporated — insurance_model_not_supported
- O Realty Income Corporation — reit_model_not_supported
- PSA Public Storage — reit_model_not_supported
- AJG Arthur J. Gallagher & Co. — insurance_model_not_supported
- ALL The Allstate Corporation — insurance_model_not_supported
- MET MetLife, Inc. — insurance_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- ARES Ares Management Corporation — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
- VTR Ventas, Inc. — reit_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- CCI Crown Castle Inc. — reit_model_not_supported
- AIG American International Group, Inc. — insurance_model_not_supported
- RKT Rocket Companies, Inc. — consumer_finance_model_not_supported
- IRM Iron Mountain Incorporated — reit_model_not_supported
- PRU Prudential Financial, Inc. — insurance_model_not_supported
- HIG The Hartford Financial Services Group, Inc. — insurance_model_not_supported
- MTB M&T Bank Corporation — bank_model_not_supported
- VICI VICI Properties Inc. — reit_model_not_supported
- RJF Raymond James Financial, Inc. — asset_management_model_not_supported
- CFG Citizens Financial Group, Inc. — bank_model_not_supported
- AVB AvalonBay Communities, Inc. — reit_model_not_supported
- WRB W. R. Berkley Corporation — insurance_model_not_supported
- EQR Equity Residential — reit_model_not_supported
- RF Regions Financial Corporation — bank_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
- KEY KeyCorp — bank_model_not_supported
- MKL Markel Corporation — insurance_model_not_supported
- L Loews Corporation — insurance_model_not_supported
- BRO Brown & Brown, Inc. — insurance_model_not_supported
- ESS Essex Property Trust, Inc. — reit_model_not_supported
- INVH Invitation Homes Inc. — reit_model_not_supported
- KIM Kimco Realty Corporation — reit_model_not_supported
- WPC W. P. Carey Inc. — reit_model_not_supported
- BEN Franklin Resources, Inc. — asset_management_model_not_supported
- NLY Annaly Capital Management, Inc. — reit_model_not_supported
- MAA Mid-America Apartment Communities, Inc. — reit_model_not_supported
- SUI Sun Communities, Inc. — reit_model_not_supported
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- OWL Blue Owl Capital Inc. — asset_management_model_not_supported
- UNM Unum Group — insurance_model_not_supported
- DOC Healthpeak Properties, Inc. — reit_model_not_supported
- EVR Evercore Inc. — asset_management_model_not_supported
- RGA Reinsurance Group of America, Incorporated — insurance_model_not_supported
- OHI Omega Healthcare Investors, Inc. — reit_model_not_supported
- ALLY Ally Financial Inc. — consumer_finance_model_not_supported
- EG Everest Re Group, Ltd. — insurance_model_not_supported
- CRBG Corebridge Financial, Inc. — asset_management_model_not_supported
- GL Globe Life Inc. — insurance_model_not_supported
- FNF Fidelity National Financial, Inc. — insurance_model_not_supported
- AIZ Assurant, Inc. — insurance_model_not_supported
- RNR RenaissanceRe Holdings Ltd. — insurance_model_not_supported
- UDR UDR, Inc. — reit_model_not_supported
- IVZ Invesco Ltd. — asset_management_model_not_supported
- ELS Equity LifeStyle Properties, Inc. — reit_model_not_supported
- EQH Equitable Holdings, Inc. — insurance_model_not_supported
- JEF Jefferies Financial Group Inc. — asset_management_model_not_supported
- CNA CNA Financial Corporation — insurance_model_not_supported
- AMH American Homes 4 Rent — reit_model_not_supported
- FHN First Horizon Corporation — bank_model_not_supported
- WBS Webster Financial Corporation — bank_model_not_supported
- VIRT Virtu Financial, Inc. — asset_management_model_not_supported
- CPT Camden Property Trust — reit_model_not_supported
- AFG American Financial Group, Inc. — insurance_model_not_supported
- SF Stifel Financial Corp. — asset_management_model_not_supported
- EGP EastGroup Properties, Inc. — reit_model_not_supported
- FRT Federal Realty Investment Trust — reit_model_not_supported
- BXP BXP, Inc. — reit_model_not_supported
- BRX Brixmor Property Group Inc. — reit_model_not_supported
- SSB SouthState Corporation — bank_model_not_supported
- CUBE CubeSmart — reit_model_not_supported
- HLI Houlihan Lokey, Inc. — asset_management_model_not_supported
- ORI Old Republic International Corporation — insurance_model_not_supported
- ARE Alexandria Real Estate Equities, Inc. — reit_model_not_supported
- CFR Cullen/Frost Bankers, Inc. — bank_model_not_supported
- AMG Affiliated Managers Group, Inc. — asset_management_model_not_supported
- WAL Western Alliance Bancorporation — bank_model_not_supported
- ADC Agree Realty Corporation — reit_model_not_supported
- NNN NNN REIT, Inc. — reit_model_not_supported
- PRI Primerica, Inc. — insurance_model_not_supported
- CTRE CareTrust REIT, Inc. — reit_model_not_supported
- FDS FactSet Research Systems Inc. — financial_sector_model_not_supported
- FR First Industrial Realty Trust, Inc. — reit_model_not_supported
- VOYA Voya Financial, Inc. — financial_sector_model_not_supported
- REXR Rexford Industrial Realty, Inc. — reit_model_not_supported
- RHP Ryman Hospitality Properties, Inc. — reit_model_not_supported
- JXN Jackson Financial Inc. — insurance_model_not_supported
- AXS AXIS Capital Holdings Limited — insurance_model_not_supported
- VNO Vornado Realty Trust — reit_model_not_supported
- STAG STAG Industrial, Inc. — reit_model_not_supported
- PB Prosperity Bancshares, Inc. — bank_model_not_supported
- PNFP Pinnacle Financial Partners, Inc. — bank_model_not_supported
- HR Healthcare Realty Trust Incorporated — reit_model_not_supported
- KNSL Kinsale Capital Group, Inc. — insurance_model_not_supported
- MAC The Macerich Company — reit_model_not_supported
- TRNO Terreno Realty Corporation — reit_model_not_supported
- LNC Lincoln National Corporation — insurance_model_not_supported
- THG The Hanover Insurance Group, Inc. — insurance_model_not_supported
- FAF First American Financial Corporation — insurance_model_not_supported
- EPRT Essential Properties Realty Trust, Inc. — reit_model_not_supported
- OMF OneMain Holdings, Inc. — consumer_finance_model_not_supported
- FNB F.N.B. Corporation — bank_model_not_supported
- GBCI Glacier Bancorp, Inc. — bank_model_not_supported
- STWD Starwood Property Trust, Inc. — reit_model_not_supported
- FLG Flagstar Financial, Inc. — bank_model_not_supported
- KRG Kite Realty Group Trust — reit_model_not_supported
- ABCB Ameris Bancorp — bank_model_not_supported
- AUB Atlantic Union Bankshares Corporation — bank_model_not_supported
- HOMB Home Bancshares, Inc. — bank_model_not_supported
- OBDC Blue Owl Capital Corporation — consumer_finance_model_not_supported
- MCY Mercury General Corporation — insurance_model_not_supported
- OUT Outfront Media Inc. — reit_model_not_supported
- MTG MGIC Investment Corporation — insurance_model_not_supported
- ESNT Essent Group Ltd. — insurance_model_not_supported
- PIPR Piper Sandler Companies — asset_management_model_not_supported
- RITM Rithm Capital Corp. — reit_model_not_supported
- MC Moelis & Company — asset_management_model_not_supported
- AX Axos Financial, Inc. — bank_model_not_supported
- RLI RLI Corp. — insurance_model_not_supported
- WTM White Mountains Insurance Group, Ltd. — insurance_model_not_supported
- MAIN Main Street Capital Corporation — asset_management_model_not_supported
- ASB Associated Banc-Corp — bank_model_not_supported
- HASI HA Sustainable Infrastructure Capital, Inc. — financial_sector_model_not_supported
- CUZ Cousins Properties Incorporated — reit_model_not_supported
- ENVA Enova International, Inc. — consumer_finance_model_not_supported
- CNO CNO Financial Group, Inc. — insurance_model_not_supported
- NNI Nelnet, Inc. — consumer_finance_model_not_supported
- SKT Tanger Inc. — reit_model_not_supported
- RDN Radian Group Inc. — insurance_model_not_supported
- EPR EPR Properties — reit_model_not_supported
- KRC Kilroy Realty Corporation — reit_model_not_supported
- RYAN Ryan Specialty Holdings, Inc. — insurance_model_not_supported
- SFBS ServisFirst Bancshares, Inc. — bank_model_not_supported
- FHI Federated Hermes, Inc. — asset_management_model_not_supported
- LMND Lemonade, Inc. — insurance_model_not_supported
- LAZ Lazard Ltd — asset_management_model_not_supported
- PFSI PennyMac Financial Services, Inc. — consumer_finance_model_not_supported
- COLD Americold Realty Trust, Inc. — reit_model_not_supported
- BFH Bread Financial Holdings, Inc. — consumer_finance_model_not_supported
- UCB United Community Banks, Inc. — bank_model_not_supported
- AB AllianceBernstein Holding L.P. — asset_management_model_not_supported
- BNL Broadstone Net Lease, Inc. — reit_model_not_supported
- PJT PJT Partners Inc. — asset_management_model_not_supported
- IRT Independence Realty Trust, Inc. — reit_model_not_supported
- CNS Cohen & Steers, Inc. — asset_management_model_not_supported
- RNST Renasant Corporation — bank_model_not_supported
- CDP COPT Defense Properties — reit_model_not_supported
- FBP First BanCorp. — bank_model_not_supported
- APLE Apple Hospitality REIT, Inc. — reit_model_not_supported
- FG F&G Annuities & Life, Inc. — insurance_model_not_supported
- SLG SL Green Realty Corp. — reit_model_not_supported
- UWMC UWM Holdings Corporation — consumer_finance_model_not_supported
- BKU BankUnited, Inc. — bank_model_not_supported
- NSA National Storage Affiliates Trust — reit_model_not_supported
- NHI National Health Investors, Inc. — reit_model_not_supported
- CBU Community Bank System, Inc. — bank_model_not_supported
- GNW Genworth Financial, Inc. — insurance_model_not_supported
- AGO Assured Guaranty Ltd. — insurance_model_not_supported
- HIW Highwoods Properties, Inc. — reit_model_not_supported
- RYN Rayonier Inc. — reit_model_not_supported
- BOH Bank of Hawaii Corporation — bank_model_not_supported
- LXP LXP Industrial Trust — reit_model_not_supported
- BXMT Blackstone Mortgage Trust, Inc. — reit_model_not_supported
- BANC Banc of California, Inc. — bank_model_not_supported
- FSK FS KKR Capital Corp. — asset_management_model_not_supported
- PFS Provident Financial Services, Inc. — bank_model_not_supported
- UE Urban Edge Properties — reit_model_not_supported
- MPT Medical Properties Trust, Inc. — reit_model_not_supported
- AKR Acadia Realty Trust — reit_model_not_supported
- HTGC Hercules Capital, Inc. — asset_management_model_not_supported
- PK Park Hotels & Resorts Inc. — reit_model_not_supported
- DBRG DigitalBridge Group, Inc. — asset_management_model_not_supported
- FBK FB Financial Corporation — bank_model_not_supported
- SPNT SiriusPoint Ltd. — insurance_model_not_supported
- AAMI Acadian Asset Management — asset_management_model_not_supported
- IVT InvenTrust Properties Corp. — reit_model_not_supported
- FCPT Four Corners Property Trust, Inc. — reit_model_not_supported
- CXW CoreCivic, Inc. — reit_model_not_supported
- WT WisdomTree, Inc. — asset_management_model_not_supported
- CUBI Customers Bancorp, Inc. — bank_model_not_supported
- BBT Beacon Financial Corp. — asset_management_model_not_supported
- APAM Artisan Partners Asset Management Inc. — asset_management_model_not_supported
- RCUS Arcus Biosciences, Inc. — preprofit_biotech_not_supported
- NIC Nicolet Bankshares, Inc. — bank_model_not_supported
- NTB The Bank of N.T. Butterfield & Son Limited — bank_model_not_supported
- WU The Western Union Company — consumer_finance_model_not_supported
- HTH Hilltop Holdings Inc. — bank_model_not_supported
- SHO Sunstone Hotel Investors, Inc. — reit_model_not_supported
- BBUC Brookfield Business Corporation — asset_management_model_not_supported
- ARR ARMOUR Residential REIT, Inc. — reit_model_not_supported
- LC LendingClub Corporation — consumer_finance_model_not_supported
- HCI HCI Group, Inc. — insurance_model_not_supported
- DEI Douglas Emmett, Inc. — reit_model_not_supported
- PEB Pebblebrook Hotel Trust — reit_model_not_supported
- GTY Getty Realty Corp. — reit_model_not_supported
- OFG OFG Bancorp — bank_model_not_supported
- FCF First Commonwealth Financial Corporation — bank_model_not_supported
- GNL Global Net Lease, Inc. — reit_model_not_supported
- AGM Federal Agricultural Mortgage Corporation — consumer_finance_model_not_supported
- STC Stewart Information Services Corporation — insurance_model_not_supported
- HMN Horace Mann Educators Corporation — insurance_model_not_supported
- STEL Stellar Bancorp, Inc. — bank_model_not_supported
- DX Dynex Capital, Inc. — reit_model_not_supported
- LTC LTC Properties, Inc. — reit_model_not_supported
- WD Walker & Dunlop, Inc. — consumer_finance_model_not_supported
- LOB Live Oak Bancshares, Inc. — bank_model_not_supported
- IIPR Innovative Industrial Properties, Inc. — reit_model_not_supported
- TFIN Triumph Financial, Inc. — bank_model_not_supported
- XHR Xenia Hotels & Resorts, Inc. — reit_model_not_supported
- DCOM Dime Community Bancshares, Inc. — bank_model_not_supported
- NTST NETSTREIT Corp. — reit_model_not_supported
- RLJ RLJ Lodging Trust — reit_model_not_supported
- NUVB Nuvation Bio Inc. — preprofit_biotech_not_supported
- NBHC National Bank Holdings Corporation — bank_model_not_supported
- TSLX Sixth Street Specialty Lending, Inc. — asset_management_model_not_supported
- BY Byline Bancorp, Inc. — bank_model_not_supported
- CBL CBL & Associates Properties, Inc. — reit_model_not_supported
- OBK Origin Bancorp, Inc. — bank_model_not_supported
- AAT American Assets Trust, Inc. — reit_model_not_supported
- KMPR Kemper Corporation — insurance_model_not_supported
- ARI Apollo Commercial Real Estate Finance, Inc. — reit_model_not_supported
- EFC Ellington Financial Inc. — reit_model_not_supported
- ALX Alexander's, Inc. — reit_model_not_supported
- UMH UMH Properties, Inc. — reit_model_not_supported
- TWO Two Harbors Investment Corp. — reit_model_not_supported
- LADR Ladder Capital Corp — consumer_finance_model_not_supported
- PRA ProAssurance Corporation — insurance_model_not_supported
- GOLD Gold.com, Inc. — asset_management_model_not_supported
- BHVN Biohaven Ltd. — preprofit_biotech_not_supported
- SAFE Safehold Inc. — reit_model_not_supported
- PDM Piedmont Office Realty Trust, Inc. — reit_model_not_supported
- CIM Chimera Investment Corporation — reit_model_not_supported
- DEA Easterly Government Properties, Inc. — reit_model_not_supported
- OPY Oppenheimer Holdings Inc. — asset_management_model_not_supported
- UVE Universal Insurance Holdings, Inc. — insurance_model_not_supported
- ASA ASA Gold and Precious Metals Limited — asset_management_model_not_supported
- EIG Employers Holdings, Inc. — insurance_model_not_supported
- GSBD Goldman Sachs BDC, Inc. — asset_management_model_not_supported
- MCB Metropolitan Bank Holding Corp. — bank_model_not_supported
- ORC Orchid Island Capital, Inc. — reit_model_not_supported
- ABR Arbor Realty Trust, Inc. — reit_model_not_supported
- FSCO FS Credit Opportunities Corp. — asset_management_model_not_supported
- WSR Whitestone REIT — reit_model_not_supported
- MFA MFA Financial, Inc. — reit_model_not_supported
- CPF Central Pacific Financial Corp. — bank_model_not_supported
- AMTB Amerant Bancorp Inc. — bank_model_not_supported
- BUR Burford Capital Limited — asset_management_model_not_supported
- DFIN Donnelley Financial Solutions, Inc. — asset_management_model_not_supported
- ESRT Empire State Realty Trust, Inc. — reit_model_not_supported
- ABX Abacus Global Management, Inc. — insurance_model_not_supported
- BBDC Barings BDC, Inc. — consumer_finance_model_not_supported
- PMT PennyMac Mortgage Investment Trust — reit_model_not_supported
- JBGS JBG SMITH Properties — reit_model_not_supported
- PSTL Postal Realty Trust, Inc. — reit_model_not_supported
- HPP Hudson Pacific Properties, Inc. — reit_model_not_supported
- PFLT PennantPark Floating Rate Capital Ltd. — asset_management_model_not_supported
- GDOT Green Dot Corporation — consumer_finance_model_not_supported
- TYG Tortoise Energy Infrastructure Corporation — asset_management_model_not_supported
- BRSP BrightSpire Capital, Inc. — reit_model_not_supported
- NXRT NexPoint Residential Trust, Inc. — reit_model_not_supported
- CTO CTO Realty Growth, Inc. — reit_model_not_supported
- INN Summit Hotel Properties, Inc. — reit_model_not_supported
- HRTG Heritage Insurance Holdings, Inc. — insurance_model_not_supported
- AHRT AH Realty Trust, Inc. — reit_model_not_supported
- TRTX TPG RE Finance Trust, Inc. — reit_model_not_supported
- RWT Redwood Trust, Inc. — reit_model_not_supported
- FBRT Franklin BSP Realty Trust, Inc. — reit_model_not_supported
- IVR Invesco Mortgage Capital Inc. — reit_model_not_supported
- BDN Brandywine Realty Trust — reit_model_not_supported
- DNA Ginkgo Bioworks Holdings, Inc. — preprofit_biotech_not_supported
- IBKR Interactive Brokers Group, Inc. — bank_model_not_supported
- EQIX Equinix, Inc. — reit_model_not_supported
- CME CME Group Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- FITB Fifth Third Bancorp — bank_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- HBAN Huntington Bancshares Incorporated — bank_model_not_supported
- ACGL Arch Capital Group Ltd. — insurance_model_not_supported
- RVMD Revolution Medicines, Inc. — preprofit_biotech_not_supported
- CINF Cincinnati Financial Corporation — insurance_model_not_supported
- FCNCA First Citizens BancShares, Inc. — bank_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- LPLA LPL Financial Holdings Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — reit_model_not_supported
- SOFI SoFi Technologies, Inc. — consumer_finance_model_not_supported
- TW Tradeweb Markets Inc. — asset_management_model_not_supported
- INSM Insmed Incorporated — preprofit_biotech_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- EWBC East West Bancorp, Inc. — bank_model_not_supported
- HST Host Hotels & Resorts, Inc. — reit_model_not_supported
- TPG TPG Inc. — asset_management_model_not_supported
- CG The Carlyle Group Inc. — asset_management_model_not_supported
- LAMR Lamar Advertising Company — reit_model_not_supported
- REG Regency Centers Corporation — reit_model_not_supported
- ARCC Ares Capital Corporation — asset_management_model_not_supported
- GLPI Gaming and Leisure Properties, Inc. — reit_model_not_supported
- BBIO BridgeBio Pharma, Inc. — preprofit_biotech_not_supported
- HUT Hut 8 Corp. — asset_management_model_not_supported
- AXSM Axsome Therapeutics, Inc. — preprofit_biotech_not_supported
- WULF TeraWulf Inc. — asset_management_model_not_supported
- IONS Ionis Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- AGNC AGNC Investment Corp. — reit_model_not_supported
- MDGL Madrigal Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- SEIC SEI Investments Company — asset_management_model_not_supported
- WTFC Wintrust Financial Corporation — bank_model_not_supported
- ARWR Arrowhead Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- ERIE Erie Indemnity Company — insurance_model_not_supported
- SNEX StoneX Group Inc. — asset_management_model_not_supported
- BPOP Popular, Inc. — bank_model_not_supported
- SMMT Summit Therapeutics Inc. — preprofit_biotech_not_supported
- UMBF UMB Financial Corporation — bank_model_not_supported
- RIOT Riot Platforms, Inc. — asset_management_model_not_supported
- ZION Zions Bancorporation, National Association — bank_model_not_supported
- FCFS FirstCash Holdings, Inc — consumer_finance_model_not_supported
- ONB Old National Bancorp — bank_model_not_supported
- CIFR Cipher Mining Inc. — asset_management_model_not_supported
- NUVL Nuvalent, Inc. — preprofit_biotech_not_supported
- CYTK Cytokinetics, Incorporated — preprofit_biotech_not_supported
- BOKF BOK Financial Corporation — bank_model_not_supported
- CBSH Commerce Bancshares, Inc. — bank_model_not_supported
- VLY Valley National Bancorp — bank_model_not_supported
- IBRX ImmunityBio, Inc. — preprofit_biotech_not_supported
- COLB Columbia Banking System, Inc. — bank_model_not_supported
- PTGX Protagonist Therapeutics, Inc. — preprofit_biotech_not_supported
- PCVX Vaxcyte, Inc. — preprofit_biotech_not_supported
- KYMR Kymera Therapeutics, Inc. — preprofit_biotech_not_supported
- IMVT Immunovant, Inc. — preprofit_biotech_not_supported
- MORN Morningstar, Inc. — financial_sector_model_not_supported
- LQDA Liquidia Corporation — preprofit_biotech_not_supported
- UBSI United Bankshares, Inc. — bank_model_not_supported
- PTCT PTC Therapeutics, Inc. — preprofit_biotech_not_supported
- RYTM Rhythm Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- ACT Enact Holdings, Inc. — insurance_model_not_supported
- HWC Hancock Whitney Corporation — bank_model_not_supported
- CACC Credit Acceptance Corporation — consumer_finance_model_not_supported
- OZK Bank OZK — bank_model_not_supported
- COGT Cogent Biosciences, Inc. — preprofit_biotech_not_supported
- SIGI Selective Insurance Group, Inc. — insurance_model_not_supported
- VCTR Victory Capital Holdings, Inc. — asset_management_model_not_supported
- STEP StepStone Group Inc. — asset_management_model_not_supported
- SRRK Scholar Rock Holding Corporation — preprofit_biotech_not_supported
- BGC BGC Group, Inc — asset_management_model_not_supported
- PRAX Praxis Precision Medicines, Inc. — preprofit_biotech_not_supported
- PECO Phillips Edison & Company, Inc. — reit_model_not_supported
- MARA Marathon Digital Holdings, Inc. — asset_management_model_not_supported
- MIRM Mirum Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- SYRE Spyre Therapeutics, Inc. — preprofit_biotech_not_supported
- EBC Eastern Bankshares, Inc. — bank_model_not_supported
- FFIN First Financial Bankshares, Inc. — bank_model_not_supported
- TFSL TFS Financial Corporation — bank_model_not_supported
- IBOC International Bancshares Corporation — bank_model_not_supported
- SBRA Sabra Health Care REIT, Inc. — reit_model_not_supported
- TVTX Travere Therapeutics, Inc. — preprofit_biotech_not_supported
- FULT Fulton Financial Corporation — bank_model_not_supported
- TCBI Texas Capital Bancshares, Inc. — bank_model_not_supported
- HLNE Hamilton Lane Incorporated — asset_management_model_not_supported
- CELC Celcuity Inc. — preprofit_biotech_not_supported
- ERAS Erasca, Inc. — preprofit_biotech_not_supported
- SLM SLM Corporation — consumer_finance_model_not_supported
- CLSK CleanSpark, Inc. — asset_management_model_not_supported
- MKTX MarketAxess Holdings Inc. — asset_management_model_not_supported
- CATY Cathay General Bancorp — bank_model_not_supported
- INDB Independent Bank Corp. — bank_model_not_supported
- WSFS WSFS Financial Corporation — bank_model_not_supported
- BANF BancFirst Corporation — bank_model_not_supported
- EWTX Edgewise Therapeutics, Inc. — preprofit_biotech_not_supported
- BHF Brighthouse Financial, Inc. — insurance_model_not_supported
- FIBK First Interstate BancSystem, Inc. — bank_model_not_supported
- NAMS NewAmsterdam Pharma Company N.V. — preprofit_biotech_not_supported
- CRNX Crinetics Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- GBDC Golub Capital BDC, Inc. — asset_management_model_not_supported
- WSBC WesBanco, Inc. — bank_model_not_supported
- TNGX Tango Therapeutics, Inc. — preprofit_biotech_not_supported
- FHB First Hawaiian, Inc. — bank_model_not_supported
- MCHB Mechanics Bank — bank_model_not_supported
- DNLI Denali Therapeutics Inc. — preprofit_biotech_not_supported
- FFBC First Financial Bancorp. — bank_model_not_supported
- VKTX Viking Therapeutics, Inc. — preprofit_biotech_not_supported
- SFNC Simmons First National Corporation — bank_model_not_supported
- DNTH Dianthus Therapeutics, Inc. — preprofit_biotech_not_supported
- CRVL CorVel Corporation — insurance_model_not_supported
- ARQT Arcutis Biotherapeutics, Inc. — preprofit_biotech_not_supported
- PLMR Palomar Holdings, Inc. — insurance_model_not_supported
- SBCF Seacoast Banking Corporation of Florida — bank_model_not_supported
- UPST Upstart Holdings, Inc. — consumer_finance_model_not_supported
- BEAM Beam Therapeutics Inc. — preprofit_biotech_not_supported
- ADPT Adaptive Biotechnologies Corporation — preprofit_biotech_not_supported
- DYN Dyne Therapeutics, Inc. — preprofit_biotech_not_supported
- CVBF CVB Financial Corp. — bank_model_not_supported
- NMIH NMI Holdings, Inc. — insurance_model_not_supported
- WAFD WaFd, Inc. — bank_model_not_supported
- TARS Tarsus Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- TOWN TowneBank — bank_model_not_supported
- TRMK Trustmark Corporation — bank_model_not_supported
- DFTX Definium Therapeutics, Inc. — preprofit_biotech_not_supported
- IRON Disc Medicine, Inc. — preprofit_biotech_not_supported
- FRME First Merchants Corporation — bank_model_not_supported
- ALMS Alumis Inc. Common Stock — preprofit_biotech_not_supported
- ORKA Oruka Therapeutics, Inc. — preprofit_biotech_not_supported
- FBNC First Bancorp — bank_model_not_supported
- IDYA IDEAYA Biosciences, Inc. — preprofit_biotech_not_supported
- RLAY Relay Therapeutics, Inc. — preprofit_biotech_not_supported
- NBTB NBT Bancorp Inc. — bank_model_not_supported
- ELVN Enliven Therapeutics, Inc. — preprofit_biotech_not_supported
- DRH DiamondRock Hospitality Company — reit_model_not_supported
- VERA Vera Therapeutics, Inc. — preprofit_biotech_not_supported
- BUSE First Busey Corporation — bank_model_not_supported
- RARE Ultragenyx Pharmaceutical Inc. — preprofit_biotech_not_supported
- TBBK The Bancorp, Inc. — bank_model_not_supported
- ANAB AnaptysBio, Inc. — preprofit_biotech_not_supported
- EFSC Enterprise Financial Services Corp — bank_model_not_supported
- MBIN Merchants Bancorp — bank_model_not_supported
- BANR Banner Corporation — bank_model_not_supported
- SYBT Stock Yards Bancorp, Inc. — bank_model_not_supported
- CLBK Columbia Financial, Inc. — bank_model_not_supported
- NWBI Northwest Bancshares, Inc. — bank_model_not_supported
- DHC Diversified Healthcare Trust — reit_model_not_supported
- GCMG GCM Grosvenor Inc. — asset_management_model_not_supported
- SKWD Skyward Specialty Insurance Group, Inc. — insurance_model_not_supported
- CLDX Celldex Therapeutics, Inc. — preprofit_biotech_not_supported
- TRVI Trevi Therapeutics, Inc. — preprofit_biotech_not_supported
- OCUL Ocular Therapeutix, Inc. — preprofit_biotech_not_supported
- SRCE 1st Source Corporation — bank_model_not_supported
- STOK Stoke Therapeutics, Inc. — preprofit_biotech_not_supported
- CHCO City Holding Company — bank_model_not_supported
- EZPW EZCORP, Inc. — consumer_finance_model_not_supported
- KOD Kodiak Sciences Inc. — preprofit_biotech_not_supported
- BCRX BioCryst Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- IMNM Immunome, Inc. — preprofit_biotech_not_supported
- CASH Pathward Financial, Inc. — bank_model_not_supported
- ECPG Encore Capital Group, Inc. — consumer_finance_model_not_supported
- AGIO Agios Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- GABC German American Bancorp, Inc. — bank_model_not_supported
- STBA S&T Bancorp, Inc. — bank_model_not_supported
- QURE uniQure N.V. — preprofit_biotech_not_supported
- TCBK TriCo Bancshares — bank_model_not_supported
- HOPE Hope Bancorp, Inc. — bank_model_not_supported
- CNOB ConnectOne Bancorp, Inc. — bank_model_not_supported
- BFC Bank First Corporation — bank_model_not_supported
- QCRH QCR Holdings, Inc. — bank_model_not_supported
- MLYS Mineralys Therapeutics, Inc. — preprofit_biotech_not_supported
- SNDX Syndax Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- SRPT Sarepta Therapeutics, Inc. — preprofit_biotech_not_supported
- TYRA Tyra Biosciences, Inc. — preprofit_biotech_not_supported
- RBCAA Republic Bancorp, Inc. — bank_model_not_supported
- LKFN Lakeland Financial Corporation — bank_model_not_supported
- NVAX Novavax, Inc. — preprofit_biotech_not_supported
- NRIX Nurix Therapeutics, Inc. — preprofit_biotech_not_supported
- PWP Perella Weinberg Partners — asset_management_model_not_supported
- CSWC Capital Southwest Corporation — asset_management_model_not_supported
- VRDN Viridian Therapeutics, Inc. — preprofit_biotech_not_supported
- MRVI Maravai LifeSciences Holdings, Inc. — preprofit_biotech_not_supported
- KALV KalVista Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- URGN UroGen Pharma Ltd. — preprofit_biotech_not_supported
- VIR Vir Biotechnology, Inc. — preprofit_biotech_not_supported
- ARDX Ardelyx, Inc. — preprofit_biotech_not_supported
- IOVA Iovance Biotherapeutics, Inc. — preprofit_biotech_not_supported
- RXRX Recursion Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- ATAI Atai Beckley Inc. — preprofit_biotech_not_supported
- TSHA Taysha Gene Therapies, Inc. — preprofit_biotech_not_supported
- NTLA Intellia Therapeutics, Inc. — preprofit_biotech_not_supported
- BWIN The Baldwin Insurance Group, Inc. — insurance_model_not_supported
- ATLC Atlanticus Holdings Corporation — consumer_finance_model_not_supported
- ASST Strive, Inc. — asset_management_model_not_supported
- PGEN Precigen, Inc. — preprofit_biotech_not_supported
- WABC Westamerica Bancorporation — bank_model_not_supported
- AMAL Amalgamated Financial Corp. — bank_model_not_supported
- PEBO Peoples Bancorp Inc. — bank_model_not_supported
- CTBI Community Trust Bancorp, Inc. — bank_model_not_supported
- TRIN Trinity Capital Inc. — asset_management_model_not_supported
- PVLA Palvella Therapeutics, Inc. — preprofit_biotech_not_supported
- MBX MBX Biosciences, Inc. Common Stock — preprofit_biotech_not_supported
- XERS Xeris Biopharma Holdings, Inc. — preprofit_biotech_not_supported
- UVSP Univest Financial Corporation — bank_model_not_supported
- NKTR Nektar Therapeutics — preprofit_biotech_not_supported
- AMLX Amylyx Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- CAPR Capricor Therapeutics, Inc. — preprofit_biotech_not_supported
- OSBC Old Second Bancorp, Inc. — bank_model_not_supported
- PSEC Prospect Capital Corporation — asset_management_model_not_supported
- GLUE Monte Rosa Therapeutics, Inc. — preprofit_biotech_not_supported
- SLS SELLAS Life Sciences Group, Inc. — preprofit_biotech_not_supported
- CCB Coastal Financial Corporation — bank_model_not_supported
- SVRA Savara Inc. — preprofit_biotech_not_supported
- SBET Sharplink, Inc. — asset_management_model_not_supported
- OCFC OceanFirst Financial Corp. — bank_model_not_supported
- OCSL Oaktree Specialty Lending Corporation — consumer_finance_model_not_supported
- SAFT Safety Insurance Group, Inc. — insurance_model_not_supported
- EYPT EyePoint Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- CFFN Capitol Federal Financial, Inc. — bank_model_not_supported
- NBN Northeast Bank — bank_model_not_supported
- FSUN FirstSun Capital Bancorp — bank_model_not_supported
- TRUP Trupanion, Inc. — insurance_model_not_supported
- ABSI Absci Corporation — preprofit_biotech_not_supported
- HIVE HIVE Digital Technologies Ltd. — financial_sector_model_not_supported
- HBNC Horizon Bancorp, Inc. — bank_model_not_supported
- BHRB Burke & Herbert Financial Services Corp. — bank_model_not_supported
- HFWA Heritage Financial Corporation — bank_model_not_supported
- ESQ Esquire Financial Holdings, Inc. — bank_model_not_supported
- CRVS Corvus Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- TRST TrustCo Bank Corp NY — bank_model_not_supported
- VRTS Virtus Investment Partners, Inc. — asset_management_model_not_supported
- SPRY ARS Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- BFST Business First Bancshares, Inc. — bank_model_not_supported
- MBWM Mercantile Bank Corporation — bank_model_not_supported
- HAFC Hanmi Financial Corporation — bank_model_not_supported
- ABTC American Bitcoin Corp — asset_management_model_not_supported
- GSHD Goosehead Insurance, Inc — insurance_model_not_supported
- OXLC Oxford Lane Capital Corp. — asset_management_model_not_supported
- XNCR Xencor, Inc. — preprofit_biotech_not_supported
- MGTX MeiraGTx Holdings plc — preprofit_biotech_not_supported
- THFF First Financial Corporation — bank_model_not_supported
- ETON Eton Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- EGBN Eagle Bancorp, Inc. — bank_model_not_supported
- MPB Mid Penn Bancorp, Inc. — bank_model_not_supported
- OLMA Olema Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- TBPH Theravance Biopharma, Inc. — preprofit_biotech_not_supported
- ABUS Arbutus Biopharma Corporation — preprofit_biotech_not_supported
- MFIC MidCap Financial Investment Corporation — asset_management_model_not_supported
- JANX Janux Therapeutics, Inc. — preprofit_biotech_not_supported
- WRLD World Acceptance Corporation — consumer_finance_model_not_supported
- GSBC Great Southern Bancorp, Inc. — bank_model_not_supported
- PHAT Phathom Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- ORIC ORIC Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- KURA Kura Oncology, Inc. — preprofit_biotech_not_supported
- SMBC Southern Missouri Bancorp, Inc. — bank_model_not_supported
- SANA Sana Biotechnology, Inc. — preprofit_biotech_not_supported
- AGNT eXp World Holdings, Inc. Common Stock — financial_sector_model_not_supported
- ORRF Orrstown Financial Services, Inc. — bank_model_not_supported
- ROOT Root, Inc. — insurance_model_not_supported
- ZVRA Zevra Therapeutics, Inc. — preprofit_biotech_not_supported
- CGBD Carlyle Secured Lending, Inc. — asset_management_model_not_supported
- NMFC New Mountain Finance Corporation — asset_management_model_not_supported
- CLYM Climb Bio, Inc. — preprofit_biotech_not_supported
- NAVI Navient Corporation — consumer_finance_model_not_supported
- OMER Omeros Corporation — preprofit_biotech_not_supported
- GERN Geron Corporation — preprofit_biotech_not_supported
- IBCP Independent Bank Corporation — bank_model_not_supported
- REPL Replimune Group, Inc. — preprofit_biotech_not_supported
- FDUS Fidus Investment Corporation — asset_management_model_not_supported
- SLRC SLR Investment Corp. — asset_management_model_not_supported
- CRMD CorMedix Inc. — preprofit_biotech_not_supported
- DSGN Design Therapeutics, Inc. — preprofit_biotech_not_supported
- CARE Carter Bankshares, Inc. — bank_model_not_supported
- ESPR Esperion Therapeutics, Inc. — preprofit_biotech_not_supported
- HIFS Hingham Institution for Savings — bank_model_not_supported
- GOOD Gladstone Commercial Corporation — reit_model_not_supported
- GAIN Gladstone Investment Corporation — asset_management_model_not_supported
- NRDS NerdWallet, Inc. — consumer_finance_model_not_supported
- BTBT Bit Digital, Inc. — asset_management_model_not_supported
- RRBI Red River Bancshares, Inc. — bank_model_not_supported
- AMSF AMERISAFE, Inc. — insurance_model_not_supported
- PRAA PRA Group, Inc. — consumer_finance_model_not_supported
- SFST Southern First Bancshares, Inc. — bank_model_not_supported
- SLDB Solid Biosciences Inc. — preprofit_biotech_not_supported
- ANNX Annexon, Inc. — preprofit_biotech_not_supported
- TECX Tectonic Therapeutic, Inc. — preprofit_biotech_not_supported
- HBCP Home Bancorp, Inc. — bank_model_not_supported
- ACRS Aclaris Therapeutics, Inc. — preprofit_biotech_not_supported
- XOMA XOMA Royalty Corp. — preprofit_biotech_not_supported
- TREE LendingTree, Inc. — consumer_finance_model_not_supported
- PRME Prime Medicine, Inc. — preprofit_biotech_not_supported
- CBIO Crescent Biopharma, Inc. — preprofit_biotech_not_supported
- PRK Park National Corporation — bank_model_not_supported
- TMP Tompkins Financial Corporation — bank_model_not_supported
- KRYS Krystal Biotech, Inc. — preprofit_biotech_not_supported
- KNSA Kiniksa Pharmaceuticals, Ltd. — preprofit_biotech_not_supported
- VCYT Veracyte, Inc. — preprofit_biotech_not_supported
- VCEL Vericel Corporation — preprofit_biotech_not_supported
- MNKD MannKind Corporation — preprofit_biotech_not_supported
- RIGL Rigel Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- COP ConocoPhillips — insufficient_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_model_confidence
- PSX Phillips 66 — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- APG APi Group Corporation — insufficient_model_confidence
- DINO HF Sinclair Corporation — insufficient_model_confidence
- AR Antero Resources Corporation — insufficient_model_confidence
- GTLS Chart Industries, Inc. — insufficient_model_confidence
- AGX Argan, Inc. — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- SWX Southwest Gas Holdings, Inc. — insufficient_model_confidence
- EE Excelerate Energy, Inc. — insufficient_model_confidence
- PARR Par Pacific Holdings, Inc. — insufficient_model_confidence
- TSLA Tesla, Inc. — insufficient_model_confidence
- FWONK Formula One Group — insufficient_model_confidence
- FWONA Formula One Group — insufficient_model_confidence
- PAA Plains All American Pipeline, L.P. — insufficient_model_confidence
- HLIT Harmonic Inc. — insufficient_model_confidence
- LZ LegalZoom.com, Inc. — insufficient_model_confidence
- REPX Riley Exploration Permian, Inc. — insufficient_model_confidence

## Data Gaps and Model Limitations

- Stocks missing core financials were rejected (fail closed), never estimated.
- Banks, insurers, REITs and pre-profit biotech are watchlisted: the general
  owner-earnings DCF does not apply and no substitute model is forced on them.
- Scenario set is discrete (bear/base/bull); a Monte Carlo layer is a planned
  extension and the aggregation already operates on generic distributions.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
