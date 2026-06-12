# Weekly US Stock Screen — 2026-06-11

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from probabilistic
valuation and risk-adjusted return, never from fixed factor weights.

## Data Freshness

- Expected market data date: **2026-06-11**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 10000 | - |
| step2_hard_filters | 10000 | 1031 | security_type: 5964, adr_excluded: 753, market_cap: 641 |
| step3_standardize | 1031 | 1031 | - |
| step4_normalized_model | 1031 | 964 | no_normalized_earnings: 61 |
| step5_quality_risk | 964 | 964 | - |
| step6_scenario_valuation | 964 | 964 | - |
| step7_risk_adjusted_ranking | 964 | 964 | - |

## Robust Top 20 (risk-adjusted)

| # | Ticker | Robust | E[IRR] | P10 | P90 | P(IRR>hurdle) | ES | P(perm loss) | Conf (model/data) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OPFI | 70.4% | 95.8% | 39.1% | 137.4% | 100% | 0.0% | 0% | 0.46/1.00 |
| 2 | WU | 56.6% | 65.0% | 46.3% | 78.9% | 100% | 0.0% | 0% | 0.86/1.00 |
| 3 | CRBG | 53.1% | 59.0% | 51.4% | 70.5% | 100% | 0.0% | 0% | 0.33/1.00 |
| 4 | BRBR | 45.7% | 54.0% | 35.8% | 67.7% | 100% | 0.0% | 0% | 0.82/1.00 |
| 5 | APO | 42.5% | 54.6% | 34.8% | 79.3% | 100% | 0.0% | 0% | 0.37/1.00 |
| 6 | VRRM | 37.3% | 49.7% | 23.9% | 70.6% | 100% | 0.0% | 0% | 0.55/1.00 |
| 7 | HRB | 27.2% | 38.1% | 14.4% | 56.2% | 100% | 0.0% | 0% | 0.68/1.00 |
| 8 | BNY | 27.0% | 31.3% | 25.9% | 39.3% | 100% | 0.0% | 0% | 0.38/1.00 |
| 9 | GDOT | 26.7% | 31.4% | 24.0% | 40.4% | 100% | 0.0% | 0% | 0.61/1.00 |
| 10 | TNET | 25.2% | 29.9% | 20.8% | 37.9% | 100% | 0.0% | 0% | 0.77/1.00 |
| 11 | EFOR | 24.6% | 28.1% | 21.1% | 34.1% | 100% | 0.0% | 0% | 0.79/1.00 |
| 12 | UHS | 22.1% | 29.4% | 13.3% | 41.7% | 100% | 0.0% | 0% | 0.85/1.00 |
| 13 | INVA | 20.5% | 26.1% | 17.2% | 37.0% | 100% | 0.0% | 0% | 0.58/1.00 |
| 14 | OMC | 19.9% | 24.1% | 15.6% | 31.2% | 100% | 0.0% | 0% | 0.84/1.00 |
| 15 | EEFT | 19.3% | 28.9% | 8.7% | 44.9% | 75% | 0.0% | 0% | 0.70/1.00 |
| 16 | FHI | 18.9% | 25.2% | 11.5% | 35.8% | 75% | 0.0% | 0% | 0.81/1.00 |
| 17 | MMS | 18.5% | 28.2% | 7.0% | 44.2% | 75% | 0.0% | 0% | 0.75/1.00 |
| 18 | ALSN | 18.5% | 25.3% | 10.6% | 36.3% | 75% | 0.0% | 0% | 0.76/1.00 |
| 19 | SMPL | 18.4% | 24.0% | 12.5% | 32.6% | 100% | 0.0% | 0% | 0.66/1.00 |
| 20 | HLF | 18.1% | 21.1% | 17.7% | 28.4% | 100% | 0.0% | 0% | 0.78/1.00 |

## Upside Top 20 (expected IRR)

| # | Ticker | E[IRR] | Median | P10 | P90 | P(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | HRMY | 510.3% | 20.5% | 20.5% | 1000.0% | 100% | 57% |
| 2 | LHX | 489.9% | -20.2% | -20.2% | 1000.0% | 50% | -80% |
| 3 | REPX | 166.2% | 29.3% | -95.0% | 701.4% | 75% | 185% |
| 4 | OPFI | 95.8% | 103.4% | 39.1% | 137.4% | 100% | 811% |
| 5 | WU | 65.0% | 67.3% | 46.3% | 78.9% | 100% | 488% |
| 6 | CRBG | 59.0% | 57.0% | 51.4% | 70.5% | 100% | 308% |
| 7 | APO | 54.6% | 52.1% | 34.8% | 79.3% | 100% | 355% |
| 8 | BRBR | 54.0% | 56.2% | 35.8% | 67.7% | 100% | 447% |
| 9 | VRRM | 49.7% | 52.0% | 23.9% | 70.6% | 100% | 377% |
| 10 | CI | 41.4% | 47.7% | -14.6% | 84.8% | 75% | 299% |
| 11 | HRB | 38.1% | 40.9% | 14.4% | 56.2% | 100% | 213% |
| 12 | GDOT | 31.4% | 30.7% | 24.0% | 40.4% | 100% | 174% |
| 13 | CF | 31.4% | 34.4% | 0.7% | 56.2% | 75% | 166% |
| 14 | BNY | 31.3% | 30.0% | 25.9% | 39.3% | 100% | 115% |
| 15 | BBT | 30.3% | 25.1% | 9.4% | 61.6% | 75% | 103% |
| 16 | TNET | 29.9% | 30.4% | 20.8% | 37.9% | 100% | 122% |
| 17 | UHS | 29.4% | 31.4% | 13.3% | 41.7% | 100% | 115% |
| 18 | EEFT | 28.9% | 30.9% | 8.7% | 44.9% | 75% | 114% |
| 19 | DVN | 28.6% | 30.5% | -8.9% | 62.2% | 75% | 176% |
| 20 | MMS | 28.2% | 30.8% | 7.0% | 44.2% | 75% | 140% |

## Week-over-week

First tracked run — no previous ranking to compare against.

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| OPFI | bear | 25% | -6.9% | 13.5% | 11.2% | 13.54 | 39.1% | 202% |
| OPFI | base | 50% | 25.0% | 22.3% | 46.4% | 75.58 | 103.4% | 1790% |
| OPFI | bull | 25% | 50.5% | 29.8% | 56.1% | 191.68 | 137.4% | 4830% |
| WU | bear | 25% | -5.7% | 17.3% | 6.9% | 23.79 | 46.3% | 419% |
| WU | base | 50% | 0.1% | 19.6% | 58.8% | 43.06 | 67.3% | 889% |
| WU | bull | 25% | 4.6% | 21.5% | 60.0% | 58.96 | 78.9% | 1277% |
| CRBG | bear | 25% | -38.2% | -10.0% | 9.8% | 101.43 | 51.4% | 495% |
| CRBG | base | 50% | -5.0% | 34.6% | 9.8% | 115.06 | 57.0% | 588% |
| CRBG | bull | 25% | 21.5% | 128.7% | 9.8% | 176.13 | 70.5% | 1046% |
| BRBR | bear | 25% | 2.7% | 13.7% | 6.5% | 24.16 | 35.8% | 292% |
| BRBR | base | 50% | 8.6% | 16.1% | 16.8% | 48.71 | 56.2% | 705% |
| BRBR | bull | 25% | 13.3% | 18.1% | 17.8% | 70.98 | 67.7% | 1080% |
| APO | bear | 25% | -47.9% | 14.1% | 11.9% | 401.69 | 34.8% | 258% |
| APO | base | 50% | 25.0% | 32.5% | 20.3% | 609.83 | 52.1% | 506% |
| APO | bull | 25% | 83.3% | 47.0% | 26.1% | 1414.05 | 79.3% | 1500% |
| VRRM | bear | 25% | -4.1% | 15.0% | 7.0% | 8.43 | 23.9% | 145% |
| VRRM | base | 50% | 8.8% | 20.9% | 45.4% | 21.47 | 52.0% | 538% |
| VRRM | bull | 25% | 19.1% | 25.6% | 55.9% | 37.71 | 70.6% | 1029% |
| HRB | bear | 25% | -3.9% | 17.2% | 6.5% | 46.61 | 14.4% | 88% |
| HRB | base | 50% | 3.9% | 21.5% | 52.7% | 112.20 | 40.9% | 408% |
| HRB | bull | 25% | 10.0% | 25.3% | 56.1% | 179.48 | 56.2% | 736% |
| BNY | bear | 25% | -19.3% | 14.8% | 9.8% | 262.65 | 25.9% | 182% |
| BNY | base | 50% | 9.5% | 22.2% | 9.8% | 305.53 | 30.0% | 253% |
| BNY | bull | 25% | 32.5% | 26.7% | 9.8% | 409.64 | 39.3% | 404% |
| GDOT | bear | 25% | -3.9% | 0.8% | 8.7% | 27.50 | 24.0% | 156% |
| GDOT | base | 50% | 10.3% | 3.6% | 8.7% | 35.58 | 30.7% | 251% |
| GDOT | bull | 25% | 21.6% | 6.0% | 8.7% | 49.58 | 40.4% | 410% |
| TNET | bear | 25% | 18.1% | 6.2% | 9.5% | 75.36 | 20.8% | 174% |
| TNET | base | 50% | 25.0% | 8.1% | 9.5% | 106.25 | 30.4% | 307% |
| TNET | bull | 25% | 30.5% | 9.5% | 9.5% | 137.90 | 37.9% | 443% |
| EFOR | bear | 25% | -7.4% | 6.8% | 6.5% | 32.64 | 21.1% | 140% |
| EFOR | base | 50% | 0.7% | 8.1% | 6.5% | 45.69 | 28.6% | 274% |
| EFOR | bull | 25% | 7.3% | 8.9% | 6.5% | 61.14 | 34.1% | 429% |
| UHS | bear | 25% | 1.7% | 8.9% | 7.9% | 164.83 | 13.3% | 78% |
| UHS | base | 50% | 6.9% | 10.7% | 17.0% | 314.28 | 31.4% | 265% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.4% | 448.87 | 41.7% | 434% |
| INVA | bear | 25% | -2.6% | 56.1% | 7.0% | 32.73 | 17.2% | 111% |
| INVA | base | 50% | 8.8% | 76.9% | 7.0% | 46.05 | 25.0% | 226% |
| INVA | bull | 25% | 17.9% | 94.1% | 7.0% | 71.68 | 37.0% | 422% |
| OMC | bear | 25% | 18.3% | 12.7% | 7.0% | 109.92 | 15.6% | 115% |
| OMC | base | 50% | 25.0% | 14.6% | 7.0% | 165.17 | 24.8% | 220% |
| OMC | bull | 25% | 30.4% | 15.9% | 7.0% | 215.11 | 31.2% | 315% |
| EEFT | bear | 25% | 0.6% | 8.7% | 7.9% | 66.08 | 8.7% | 48% |
| EEFT | base | 50% | 7.5% | 12.1% | 26.3% | 141.43 | 30.9% | 261% |
| EEFT | bull | 25% | 13.1% | 15.1% | 29.4% | 222.56 | 44.9% | 490% |
| FHI | bear | 25% | 2.5% | 23.7% | 7.6% | 66.83 | 11.5% | 67% |
| FHI | base | 50% | 8.2% | 27.2% | 53.6% | 113.33 | 26.8% | 210% |
| FHI | bull | 25% | 12.8% | 30.2% | 55.0% | 152.41 | 35.8% | 330% |
| MMS | bear | 25% | -2.0% | 7.6% | 6.6% | 61.56 | 7.0% | 36% |
| MMS | base | 50% | 4.8% | 9.6% | 39.7% | 148.87 | 30.8% | 251% |
| MMS | bull | 25% | 10.2% | 11.2% | 46.5% | 234.79 | 44.2% | 462% |
| ALSN | bear | 25% | 17.9% | 26.8% | 8.6% | 120.52 | 10.6% | 63% |
| ALSN | base | 50% | 25.0% | 30.5% | 58.4% | 219.29 | 27.1% | 219% |
| ALSN | bull | 25% | 30.7% | 33.7% | 60.0% | 301.40 | 36.3% | 349% |
| SMPL | bear | 25% | -8.3% | 13.2% | 6.6% | 15.95 | 12.5% | 66% |
| SMPL | base | 50% | 5.5% | 15.9% | 7.2% | 27.45 | 25.4% | 192% |
| SMPL | bull | 25% | 16.5% | 17.5% | 7.4% | 39.11 | 32.6% | 323% |
| HLF | bear | 25% | -2.7% | 8.9% | 7.3% | 20.17 | 20.5% | 120% |
| HLF | base | 50% | 2.6% | 11.0% | 7.3% | 22.06 | 17.7% | 159% |
| HLF | bull | 25% | 6.8% | 12.8% | 7.3% | 36.11 | 28.4% | 312% |

## Key Risks and Failure Conditions

- OPFI: thin_interest_coverage, cyclical_revenue
- CRBG: thin_interest_coverage, cyclical_revenue, incremental_roic_below_wacc
- BRBR: incremental_roic_below_wacc
- APO: cyclical_revenue
- VRRM: thin_interest_coverage, cyclical_revenue
- BNY: thin_interest_coverage, cyclical_revenue, incremental_roic_below_wacc
- TNET: thin_interest_coverage
- EFOR: thin_interest_coverage, incremental_roic_below_wacc
- INVA: weak_cash_conversion, incremental_roic_below_wacc
- OMC: incremental_roic_below_wacc
- SMPL: cyclical_revenue
- HLF: elevated_leverage, thin_interest_coverage, incremental_roic_below_wacc

## Watchlist (not rankable under the general model)

- BRK-B Berkshire Hathaway Inc. — insurance_model_not_supported
- BRK-A Berkshire Hathaway Inc. — insurance_model_not_supported
- JPM JPMorgan Chase & Co. — bank_model_not_supported
- BAC Bank of America Corporation — bank_model_not_supported
- WFC Wells Fargo & Company — bank_model_not_supported
- C Citigroup Inc. — bank_model_not_supported
- IBKR Interactive Brokers Group, Inc. — bank_model_not_supported
- WELL Welltower Inc. — reit_model_not_supported
- PLD Prologis, Inc. — reit_model_not_supported
- PGR The Progressive Corporation — insurance_model_not_supported
- EQIX Equinix, Inc. — reit_model_not_supported
- PNC The PNC Financial Services Group, Inc. — bank_model_not_supported
- USB U.S. Bancorp — bank_model_not_supported
- AMT American Tower Corporation — reit_model_not_supported
- MRSH Marsh & McLennan Companies, Inc. — insurance_model_not_supported
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
- FITB Fifth Third Bancorp — bank_model_not_supported
- VTR Ventas, Inc. — reit_model_not_supported
- CCI Crown Castle Inc. — reit_model_not_supported
- AIG American International Group, Inc. — insurance_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- IRM Iron Mountain Incorporated — reit_model_not_supported
- PRU Prudential Financial, Inc. — insurance_model_not_supported
- HIG The Hartford Financial Services Group, Inc. — insurance_model_not_supported
- HBAN Huntington Bancshares Incorporated — bank_model_not_supported
- MTB M&T Bank Corporation — bank_model_not_supported
- ACGL Arch Capital Group Ltd. — insurance_model_not_supported
- RVMD Revolution Medicines, Inc. — preprofit_biotech_not_supported
- VICI VICI Properties Inc. — reit_model_not_supported
- CFG Citizens Financial Group, Inc. — bank_model_not_supported
- AVB AvalonBay Communities, Inc. — reit_model_not_supported
- CINF Cincinnati Financial Corporation — insurance_model_not_supported
- WRB W. R. Berkley Corporation — insurance_model_not_supported
- EQR Equity Residential — reit_model_not_supported
- RF Regions Financial Corporation — bank_model_not_supported
- FCNCA First Citizens BancShares, Inc. — bank_model_not_supported
- KEY KeyCorp — bank_model_not_supported
- MKL Markel Corporation — insurance_model_not_supported
- L Loews Corporation — insurance_model_not_supported
- SBAC SBA Communications Corporation — reit_model_not_supported
- INSM Insmed Incorporated — preprofit_biotech_not_supported
- BRO Brown & Brown, Inc. — insurance_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- ESS Essex Property Trust, Inc. — reit_model_not_supported
- EWBC East West Bancorp, Inc. — bank_model_not_supported
- INVH Invitation Homes Inc. — reit_model_not_supported
- KIM Kimco Realty Corporation — reit_model_not_supported
- WPC W. P. Carey Inc. — reit_model_not_supported
- HST Host Hotels & Resorts, Inc. — reit_model_not_supported
- NLY Annaly Capital Management, Inc. — reit_model_not_supported
- MAA Mid-America Apartment Communities, Inc. — reit_model_not_supported
- SUI Sun Communities, Inc. — reit_model_not_supported
- LAMR Lamar Advertising Company — reit_model_not_supported
- REG Regency Centers Corporation — reit_model_not_supported
- UNM Unum Group — insurance_model_not_supported
- DOC Healthpeak Properties, Inc. — reit_model_not_supported
- GLPI Gaming and Leisure Properties, Inc. — reit_model_not_supported
- RGA Reinsurance Group of America, Incorporated — insurance_model_not_supported
- OHI Omega Healthcare Investors, Inc. — reit_model_not_supported
- EG Everest Re Group, Ltd. — insurance_model_not_supported
- BBIO BridgeBio Pharma, Inc. — preprofit_biotech_not_supported
- AXSM Axsome Therapeutics, Inc. — preprofit_biotech_not_supported
- GL Globe Life Inc. — insurance_model_not_supported
- FNF Fidelity National Financial, Inc. — insurance_model_not_supported
- AIZ Assurant, Inc. — insurance_model_not_supported
- RNR RenaissanceRe Holdings Ltd. — insurance_model_not_supported
- UDR UDR, Inc. — reit_model_not_supported
- ELS Equity LifeStyle Properties, Inc. — reit_model_not_supported
- EQH Equitable Holdings, Inc. — insurance_model_not_supported
- IONS Ionis Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- CNA CNA Financial Corporation — insurance_model_not_supported
- AMH American Homes 4 Rent — reit_model_not_supported
- FHN First Horizon Corporation — bank_model_not_supported
- WBS Webster Financial Corporation — bank_model_not_supported
- AGNC AGNC Investment Corp. — reit_model_not_supported
- CPT Camden Property Trust — reit_model_not_supported
- AFG American Financial Group, Inc. — insurance_model_not_supported
- MDGL Madrigal Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- EGP EastGroup Properties, Inc. — reit_model_not_supported
- FRT Federal Realty Investment Trust — reit_model_not_supported
- BXP BXP, Inc. — reit_model_not_supported
- WTFC Wintrust Financial Corporation — bank_model_not_supported
- ARWR Arrowhead Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- ERIE Erie Indemnity Company — insurance_model_not_supported
- BPOP Popular, Inc. — bank_model_not_supported
- SMMT Summit Therapeutics Inc. — preprofit_biotech_not_supported
- UMBF UMB Financial Corporation — bank_model_not_supported
- BRX Brixmor Property Group Inc. — reit_model_not_supported
- ZION Zions Bancorporation, National Association — bank_model_not_supported
- ONB Old National Bancorp — bank_model_not_supported
- SSB SouthState Corporation — bank_model_not_supported
- CUBE CubeSmart — reit_model_not_supported
- ORI Old Republic International Corporation — insurance_model_not_supported
- ARE Alexandria Real Estate Equities, Inc. — reit_model_not_supported
- CFR Cullen/Frost Bankers, Inc. — bank_model_not_supported
- NUVL Nuvalent, Inc. — preprofit_biotech_not_supported
- WAL Western Alliance Bancorporation — bank_model_not_supported
- ADC Agree Realty Corporation — reit_model_not_supported
- NNN NNN REIT, Inc. — reit_model_not_supported
- PRI Primerica, Inc. — insurance_model_not_supported
- CTRE CareTrust REIT, Inc. — reit_model_not_supported
- CYTK Cytokinetics, Incorporated — preprofit_biotech_not_supported
- FR First Industrial Realty Trust, Inc. — reit_model_not_supported
- BOKF BOK Financial Corporation — bank_model_not_supported
- REXR Rexford Industrial Realty, Inc. — reit_model_not_supported
- CBSH Commerce Bancshares, Inc. — bank_model_not_supported
- VLY Valley National Bancorp — bank_model_not_supported
- RHP Ryman Hospitality Properties, Inc. — reit_model_not_supported
- JXN Jackson Financial Inc. — insurance_model_not_supported
- IBRX ImmunityBio, Inc. — preprofit_biotech_not_supported
- AXS AXIS Capital Holdings Limited — insurance_model_not_supported
- COLB Columbia Banking System, Inc. — bank_model_not_supported
- VNO Vornado Realty Trust — reit_model_not_supported
- STAG STAG Industrial, Inc. — reit_model_not_supported
- PB Prosperity Bancshares, Inc. — bank_model_not_supported
- PNFP Pinnacle Financial Partners, Inc. — bank_model_not_supported
- HR Healthcare Realty Trust Incorporated — reit_model_not_supported
- KNSL Kinsale Capital Group, Inc. — insurance_model_not_supported
- MAC The Macerich Company — reit_model_not_supported
- TRNO Terreno Realty Corporation — reit_model_not_supported
- PTGX Protagonist Therapeutics, Inc. — preprofit_biotech_not_supported
- LNC Lincoln National Corporation — insurance_model_not_supported
- THG The Hanover Insurance Group, Inc. — insurance_model_not_supported
- PCVX Vaxcyte, Inc. — preprofit_biotech_not_supported
- KYMR Kymera Therapeutics, Inc. — preprofit_biotech_not_supported
- IMVT Immunovant, Inc. — preprofit_biotech_not_supported
- FAF First American Financial Corporation — insurance_model_not_supported
- EPRT Essential Properties Realty Trust, Inc. — reit_model_not_supported
- FNB F.N.B. Corporation — bank_model_not_supported
- LQDA Liquidia Corporation — preprofit_biotech_not_supported
- GBCI Glacier Bancorp, Inc. — bank_model_not_supported
- STWD Starwood Property Trust, Inc. — reit_model_not_supported
- UBSI United Bankshares, Inc. — bank_model_not_supported
- PTCT PTC Therapeutics, Inc. — preprofit_biotech_not_supported
- FLG Flagstar Financial, Inc. — bank_model_not_supported
- RYTM Rhythm Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- KRG Kite Realty Group Trust — reit_model_not_supported
- ACT Enact Holdings, Inc. — insurance_model_not_supported
- ABCB Ameris Bancorp — bank_model_not_supported
- HWC Hancock Whitney Corporation — bank_model_not_supported
- AUB Atlantic Union Bankshares Corporation — bank_model_not_supported
- OZK Bank OZK — bank_model_not_supported
- HOMB Home Bancshares, Inc. — bank_model_not_supported
- COGT Cogent Biosciences, Inc. — preprofit_biotech_not_supported
- SIGI Selective Insurance Group, Inc. — insurance_model_not_supported
- MCY Mercury General Corporation — insurance_model_not_supported
- OUT Outfront Media Inc. — reit_model_not_supported
- MTG MGIC Investment Corporation — insurance_model_not_supported
- SRRK Scholar Rock Holding Corporation — preprofit_biotech_not_supported
- ESNT Essent Group Ltd. — insurance_model_not_supported
- PRAX Praxis Precision Medicines, Inc. — preprofit_biotech_not_supported
- PECO Phillips Edison & Company, Inc. — reit_model_not_supported
- RITM Rithm Capital Corp. — reit_model_not_supported
- AX Axos Financial, Inc. — bank_model_not_supported
- MIRM Mirum Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- RLI RLI Corp. — insurance_model_not_supported
- WTM White Mountains Insurance Group, Ltd. — insurance_model_not_supported
- SYRE Spyre Therapeutics, Inc. — preprofit_biotech_not_supported
- ASB Associated Banc-Corp — bank_model_not_supported
- EBC Eastern Bankshares, Inc. — bank_model_not_supported
- FFIN First Financial Bankshares, Inc. — bank_model_not_supported
- CUZ Cousins Properties Incorporated — reit_model_not_supported
- TFSL TFS Financial Corporation — bank_model_not_supported
- IBOC International Bancshares Corporation — bank_model_not_supported
- CNO CNO Financial Group, Inc. — insurance_model_not_supported
- SBRA Sabra Health Care REIT, Inc. — reit_model_not_supported
- SKT Tanger Inc. — reit_model_not_supported
- TVTX Travere Therapeutics, Inc. — preprofit_biotech_not_supported
- RDN Radian Group Inc. — insurance_model_not_supported
- EPR EPR Properties — reit_model_not_supported
- KRC Kilroy Realty Corporation — reit_model_not_supported
- RYAN Ryan Specialty Holdings, Inc. — insurance_model_not_supported
- SFBS ServisFirst Bancshares, Inc. — bank_model_not_supported
- FULT Fulton Financial Corporation — bank_model_not_supported
- LMND Lemonade, Inc. — insurance_model_not_supported
- TCBI Texas Capital Bancshares, Inc. — bank_model_not_supported
- CELC Celcuity Inc. — preprofit_biotech_not_supported
- ERAS Erasca, Inc. — preprofit_biotech_not_supported
- COLD Americold Realty Trust, Inc. — reit_model_not_supported
- UCB United Community Banks, Inc. — bank_model_not_supported
- CATY Cathay General Bancorp — bank_model_not_supported
- BNL Broadstone Net Lease, Inc. — reit_model_not_supported
- INDB Independent Bank Corp. — bank_model_not_supported
- IRT Independence Realty Trust, Inc. — reit_model_not_supported
- RNST Renasant Corporation — bank_model_not_supported
- CDP COPT Defense Properties — reit_model_not_supported
- WSFS WSFS Financial Corporation — bank_model_not_supported
- FBP First BanCorp. — bank_model_not_supported
- BANF BancFirst Corporation — bank_model_not_supported
- APLE Apple Hospitality REIT, Inc. — reit_model_not_supported
- FG F&G Annuities & Life, Inc. — insurance_model_not_supported
- EWTX Edgewise Therapeutics, Inc. — preprofit_biotech_not_supported
- SLG SL Green Realty Corp. — reit_model_not_supported
- BHF Brighthouse Financial, Inc. — insurance_model_not_supported
- FIBK First Interstate BancSystem, Inc. — bank_model_not_supported
- NAMS NewAmsterdam Pharma Company N.V. — preprofit_biotech_not_supported
- CRNX Crinetics Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- BKU BankUnited, Inc. — bank_model_not_supported
- NSA National Storage Affiliates Trust — reit_model_not_supported
- NHI National Health Investors, Inc. — reit_model_not_supported
- WSBC WesBanco, Inc. — bank_model_not_supported
- TNGX Tango Therapeutics, Inc. — preprofit_biotech_not_supported
- CBU Community Bank System, Inc. — bank_model_not_supported
- FHB First Hawaiian, Inc. — bank_model_not_supported
- GNW Genworth Financial, Inc. — insurance_model_not_supported
- AGO Assured Guaranty Ltd. — insurance_model_not_supported
- MCHB Mechanics Bank — bank_model_not_supported
- DNLI Denali Therapeutics Inc. — preprofit_biotech_not_supported
- HIW Highwoods Properties, Inc. — reit_model_not_supported
- FFBC First Financial Bancorp. — bank_model_not_supported
- VKTX Viking Therapeutics, Inc. — preprofit_biotech_not_supported
- RYN Rayonier Inc. — reit_model_not_supported
- SFNC Simmons First National Corporation — bank_model_not_supported
- PRK Park National Corporation — bank_model_not_supported
- DNTH Dianthus Therapeutics, Inc. — preprofit_biotech_not_supported
- BOH Bank of Hawaii Corporation — bank_model_not_supported
- LXP LXP Industrial Trust — reit_model_not_supported
- CRVL CorVel Corporation — insurance_model_not_supported
- ARQT Arcutis Biotherapeutics, Inc. — preprofit_biotech_not_supported
- BXMT Blackstone Mortgage Trust, Inc. — reit_model_not_supported
- BANC Banc of California, Inc. — bank_model_not_supported
- PLMR Palomar Holdings, Inc. — insurance_model_not_supported
- SBCF Seacoast Banking Corporation of Florida — bank_model_not_supported
- PFS Provident Financial Services, Inc. — bank_model_not_supported
- BEAM Beam Therapeutics Inc. — preprofit_biotech_not_supported
- ADPT Adaptive Biotechnologies Corporation — preprofit_biotech_not_supported
- UE Urban Edge Properties — reit_model_not_supported
- MPT Medical Properties Trust, Inc. — reit_model_not_supported
- DYN Dyne Therapeutics, Inc. — preprofit_biotech_not_supported
- AKR Acadia Realty Trust — reit_model_not_supported
- PK Park Hotels & Resorts Inc. — reit_model_not_supported
- CVBF CVB Financial Corp. — bank_model_not_supported
- NMIH NMI Holdings, Inc. — insurance_model_not_supported
- FBK FB Financial Corporation — bank_model_not_supported
- SPNT SiriusPoint Ltd. — insurance_model_not_supported
- IVT InvenTrust Properties Corp. — reit_model_not_supported
- FCPT Four Corners Property Trust, Inc. — reit_model_not_supported
- WAFD WaFd, Inc. — bank_model_not_supported
- TARS Tarsus Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- TOWN TowneBank — bank_model_not_supported
- TRMK Trustmark Corporation — bank_model_not_supported
- CXW CoreCivic, Inc. — reit_model_not_supported
- DFTX Definium Therapeutics, Inc. — preprofit_biotech_not_supported
- CUBI Customers Bancorp, Inc. — bank_model_not_supported
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
- RCUS Arcus Biosciences, Inc. — preprofit_biotech_not_supported
- ANAB AnaptysBio, Inc. — preprofit_biotech_not_supported
- EFSC Enterprise Financial Services Corp — bank_model_not_supported
- NIC Nicolet Bankshares, Inc. — bank_model_not_supported
- NTB The Bank of N.T. Butterfield & Son Limited — bank_model_not_supported
- MBIN Merchants Bancorp — bank_model_not_supported
- BANR Banner Corporation — bank_model_not_supported
- HTH Hilltop Holdings Inc. — bank_model_not_supported
- SYBT Stock Yards Bancorp, Inc. — bank_model_not_supported
- SHO Sunstone Hotel Investors, Inc. — reit_model_not_supported
- CLBK Columbia Financial, Inc. — bank_model_not_supported
- NWBI Northwest Bancshares, Inc. — bank_model_not_supported
- DHC Diversified Healthcare Trust — reit_model_not_supported
- ARR ARMOUR Residential REIT, Inc. — reit_model_not_supported
- HCI HCI Group, Inc. — insurance_model_not_supported
- DEI Douglas Emmett, Inc. — reit_model_not_supported
- SKWD Skyward Specialty Insurance Group, Inc. — insurance_model_not_supported
- PEB Pebblebrook Hotel Trust — reit_model_not_supported
- GTY Getty Realty Corp. — reit_model_not_supported
- OFG OFG Bancorp — bank_model_not_supported
- CLDX Celldex Therapeutics, Inc. — preprofit_biotech_not_supported
- FCF First Commonwealth Financial Corporation — bank_model_not_supported
- GNL Global Net Lease, Inc. — reit_model_not_supported
- STC Stewart Information Services Corporation — insurance_model_not_supported
- HMN Horace Mann Educators Corporation — insurance_model_not_supported
- STEL Stellar Bancorp, Inc. — bank_model_not_supported
- DX Dynex Capital, Inc. — reit_model_not_supported
- TRVI Trevi Therapeutics, Inc. — preprofit_biotech_not_supported
- OCUL Ocular Therapeutix, Inc. — preprofit_biotech_not_supported
- LTC LTC Properties, Inc. — reit_model_not_supported
- SRCE 1st Source Corporation — bank_model_not_supported
- STOK Stoke Therapeutics, Inc. — preprofit_biotech_not_supported
- CHCO City Holding Company — bank_model_not_supported
- KOD Kodiak Sciences Inc. — preprofit_biotech_not_supported
- LOB Live Oak Bancshares, Inc. — bank_model_not_supported
- BCRX BioCryst Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- IIPR Innovative Industrial Properties, Inc. — reit_model_not_supported
- TFIN Triumph Financial, Inc. — bank_model_not_supported
- XHR Xenia Hotels & Resorts, Inc. — reit_model_not_supported
- DCOM Dime Community Bancshares, Inc. — bank_model_not_supported
- IMNM Immunome, Inc. — preprofit_biotech_not_supported
- CASH Pathward Financial, Inc. — bank_model_not_supported
- AGIO Agios Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- GABC German American Bancorp, Inc. — bank_model_not_supported
- STBA S&T Bancorp, Inc. — bank_model_not_supported
- QURE uniQure N.V. — preprofit_biotech_not_supported
- TCBK TriCo Bancshares — bank_model_not_supported
- NTST NETSTREIT Corp. — reit_model_not_supported
- RLJ RLJ Lodging Trust — reit_model_not_supported
- HOPE Hope Bancorp, Inc. — bank_model_not_supported
- NUVB Nuvation Bio Inc. — preprofit_biotech_not_supported
- NBHC National Bank Holdings Corporation — bank_model_not_supported
- CNOB ConnectOne Bancorp, Inc. — bank_model_not_supported
- BFC Bank First Corporation — bank_model_not_supported
- BY Byline Bancorp, Inc. — bank_model_not_supported
- QCRH QCR Holdings, Inc. — bank_model_not_supported
- MLYS Mineralys Therapeutics, Inc. — preprofit_biotech_not_supported
- SNDX Syndax Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- SRPT Sarepta Therapeutics, Inc. — preprofit_biotech_not_supported
- CBL CBL & Associates Properties, Inc. — reit_model_not_supported
- OBK Origin Bancorp, Inc. — bank_model_not_supported
- TYRA Tyra Biosciences, Inc. — preprofit_biotech_not_supported
- RBCAA Republic Bancorp, Inc. — bank_model_not_supported
- LKFN Lakeland Financial Corporation — bank_model_not_supported
- AAT American Assets Trust, Inc. — reit_model_not_supported
- NVAX Novavax, Inc. — preprofit_biotech_not_supported
- NRIX Nurix Therapeutics, Inc. — preprofit_biotech_not_supported
- KMPR Kemper Corporation — insurance_model_not_supported
- VRDN Viridian Therapeutics, Inc. — preprofit_biotech_not_supported
- MRVI Maravai LifeSciences Holdings, Inc. — preprofit_biotech_not_supported
- KALV KalVista Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- URGN UroGen Pharma Ltd. — preprofit_biotech_not_supported
- VIR Vir Biotechnology, Inc. — preprofit_biotech_not_supported
- ARDX Ardelyx, Inc. — preprofit_biotech_not_supported
- IOVA Iovance Biotherapeutics, Inc. — preprofit_biotech_not_supported
- ARI Apollo Commercial Real Estate Finance, Inc. — reit_model_not_supported
- RXRX Recursion Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- ATAI Atai Beckley Inc. — preprofit_biotech_not_supported
- TSHA Taysha Gene Therapies, Inc. — preprofit_biotech_not_supported
- NTLA Intellia Therapeutics, Inc. — preprofit_biotech_not_supported
- BWIN The Baldwin Insurance Group, Inc. — insurance_model_not_supported
- PGEN Precigen, Inc. — preprofit_biotech_not_supported
- EFC Ellington Financial Inc. — reit_model_not_supported
- WABC Westamerica Bancorporation — bank_model_not_supported
- ALX Alexander's, Inc. — reit_model_not_supported
- AMAL Amalgamated Financial Corp. — bank_model_not_supported
- TMP Tompkins Financial Corporation — bank_model_not_supported
- PEBO Peoples Bancorp Inc. — bank_model_not_supported
- UMH UMH Properties, Inc. — reit_model_not_supported
- TWO Two Harbors Investment Corp. — reit_model_not_supported
- PRA ProAssurance Corporation — insurance_model_not_supported
- CTBI Community Trust Bancorp, Inc. — bank_model_not_supported
- PVLA Palvella Therapeutics, Inc. — preprofit_biotech_not_supported
- MBX MBX Biosciences, Inc. Common Stock — preprofit_biotech_not_supported
- UFCS United Fire Group, Inc. — insurance_model_not_supported
- BHVN Biohaven Ltd. — preprofit_biotech_not_supported
- XERS Xeris Biopharma Holdings, Inc. — preprofit_biotech_not_supported
- UVSP Univest Financial Corporation — bank_model_not_supported
- NKTR Nektar Therapeutics — preprofit_biotech_not_supported
- AMLX Amylyx Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- SAFE Safehold Inc. — reit_model_not_supported
- CAPR Capricor Therapeutics, Inc. — preprofit_biotech_not_supported
- OSBC Old Second Bancorp, Inc. — bank_model_not_supported
- PDM Piedmont Office Realty Trust, Inc. — reit_model_not_supported
- CIM Chimera Investment Corporation — reit_model_not_supported
- GLUE Monte Rosa Therapeutics, Inc. — preprofit_biotech_not_supported
- DEA Easterly Government Properties, Inc. — reit_model_not_supported
- SLS SELLAS Life Sciences Group, Inc. — preprofit_biotech_not_supported
- CCB Coastal Financial Corporation — bank_model_not_supported
- SVRA Savara Inc. — preprofit_biotech_not_supported
- UVE Universal Insurance Holdings, Inc. — insurance_model_not_supported
- OCFC OceanFirst Financial Corp. — bank_model_not_supported
- SAFT Safety Insurance Group, Inc. — insurance_model_not_supported
- EYPT EyePoint Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- CFFN Capitol Federal Financial, Inc. — bank_model_not_supported
- EIG Employers Holdings, Inc. — insurance_model_not_supported
- NBN Northeast Bank — bank_model_not_supported
- FSUN FirstSun Capital Bancorp — bank_model_not_supported
- TRUP Trupanion, Inc. — insurance_model_not_supported
- ABSI Absci Corporation — preprofit_biotech_not_supported
- MCB Metropolitan Bank Holding Corp. — bank_model_not_supported
- HBNC Horizon Bancorp, Inc. — bank_model_not_supported
- ORC Orchid Island Capital, Inc. — reit_model_not_supported
- BHRB Burke & Herbert Financial Services Corp. — bank_model_not_supported
- ABR Arbor Realty Trust, Inc. — reit_model_not_supported
- WSR Whitestone REIT — reit_model_not_supported
- HFWA Heritage Financial Corporation — bank_model_not_supported
- ESQ Esquire Financial Holdings, Inc. — bank_model_not_supported
- CRVS Corvus Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- TRST TrustCo Bank Corp NY — bank_model_not_supported
- SPRY ARS Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- BFST Business First Bancshares, Inc. — bank_model_not_supported
- MFA MFA Financial, Inc. — reit_model_not_supported
- CPF Central Pacific Financial Corp. — bank_model_not_supported
- MBWM Mercantile Bank Corporation — bank_model_not_supported
- AMTB Amerant Bancorp Inc. — bank_model_not_supported
- HAFC Hanmi Financial Corporation — bank_model_not_supported
- ESRT Empire State Realty Trust, Inc. — reit_model_not_supported
- GSHD Goosehead Insurance, Inc — insurance_model_not_supported
- ABX Abacus Global Management, Inc. — insurance_model_not_supported
- XNCR Xencor, Inc. — preprofit_biotech_not_supported
- MGTX MeiraGTx Holdings plc — preprofit_biotech_not_supported
- THFF First Financial Corporation — bank_model_not_supported
- ETON Eton Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- PMT PennyMac Mortgage Investment Trust — reit_model_not_supported
- EGBN Eagle Bancorp, Inc. — bank_model_not_supported
- MPB Mid Penn Bancorp, Inc. — bank_model_not_supported
- OLMA Olema Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- TBPH Theravance Biopharma, Inc. — preprofit_biotech_not_supported
- ABUS Arbutus Biopharma Corporation — preprofit_biotech_not_supported
- JBGS JBG SMITH Properties — reit_model_not_supported
- LXRX Lexicon Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- JANX Janux Therapeutics, Inc. — preprofit_biotech_not_supported
- PSTL Postal Realty Trust, Inc. — reit_model_not_supported
- HPP Hudson Pacific Properties, Inc. — reit_model_not_supported
- GSBC Great Southern Bancorp, Inc. — bank_model_not_supported
- PHAT Phathom Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- ORIC ORIC Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- KURA Kura Oncology, Inc. — preprofit_biotech_not_supported
- SMBC Southern Missouri Bancorp, Inc. — bank_model_not_supported
- SANA Sana Biotechnology, Inc. — preprofit_biotech_not_supported
- ORRF Orrstown Financial Services, Inc. — bank_model_not_supported
- ROOT Root, Inc. — insurance_model_not_supported
- ZVRA Zevra Therapeutics, Inc. — preprofit_biotech_not_supported
- CLYM Climb Bio, Inc. — preprofit_biotech_not_supported
- OMER Omeros Corporation — preprofit_biotech_not_supported
- GERN Geron Corporation — preprofit_biotech_not_supported
- BRSP BrightSpire Capital, Inc. — reit_model_not_supported
- IBCP Independent Bank Corporation — bank_model_not_supported
- NXRT NexPoint Residential Trust, Inc. — reit_model_not_supported
- REPL Replimune Group, Inc. — preprofit_biotech_not_supported
- CTO CTO Realty Growth, Inc. — reit_model_not_supported
- CRMD CorMedix Inc. — preprofit_biotech_not_supported
- INN Summit Hotel Properties, Inc. — reit_model_not_supported
- HRTG Heritage Insurance Holdings, Inc. — insurance_model_not_supported
- AHRT AH Realty Trust, Inc. — reit_model_not_supported
- TRTX TPG RE Finance Trust, Inc. — reit_model_not_supported
- DSGN Design Therapeutics, Inc. — preprofit_biotech_not_supported
- CARE Carter Bankshares, Inc. — bank_model_not_supported
- ESPR Esperion Therapeutics, Inc. — preprofit_biotech_not_supported
- RWT Redwood Trust, Inc. — reit_model_not_supported
- HIFS Hingham Institution for Savings — bank_model_not_supported
- FBRT Franklin BSP Realty Trust, Inc. — reit_model_not_supported
- GOOD Gladstone Commercial Corporation — reit_model_not_supported
- RRBI Red River Bancshares, Inc. — bank_model_not_supported
- AMSF AMERISAFE, Inc. — insurance_model_not_supported
- SFST Southern First Bancshares, Inc. — bank_model_not_supported
- IVR Invesco Mortgage Capital Inc. — reit_model_not_supported
- SLDB Solid Biosciences Inc. — preprofit_biotech_not_supported
- ANNX Annexon, Inc. — preprofit_biotech_not_supported
- BDN Brandywine Realty Trust — reit_model_not_supported
- TECX Tectonic Therapeutic, Inc. — preprofit_biotech_not_supported
- HBCP Home Bancorp, Inc. — bank_model_not_supported
- ACRS Aclaris Therapeutics, Inc. — preprofit_biotech_not_supported
- XOMA XOMA Royalty Corp. — preprofit_biotech_not_supported
- DNA Ginkgo Bioworks Holdings, Inc. — preprofit_biotech_not_supported
- PRME Prime Medicine, Inc. — preprofit_biotech_not_supported
- CBIO Crescent Biopharma, Inc. — preprofit_biotech_not_supported
- KRYS Krystal Biotech, Inc. — preprofit_biotech_not_supported
- KNSA Kiniksa Pharmaceuticals, Ltd. — preprofit_biotech_not_supported
- VCYT Veracyte, Inc. — preprofit_biotech_not_supported
- VCEL Vericel Corporation — preprofit_biotech_not_supported
- MNKD MannKind Corporation — preprofit_biotech_not_supported
- RIGL Rigel Pharmaceuticals, Inc. — preprofit_biotech_not_supported

## Data Gaps and Model Limitations

- Stocks missing core financials were rejected (fail closed), never estimated.
- Banks, insurers, REITs and pre-profit biotech are watchlisted: the general
  owner-earnings DCF does not apply and no substitute model is forced on them.
- Scenario set is discrete (bear/base/bull); a Monte Carlo layer is a planned
  extension and the aggregation already operates on generic distributions.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
