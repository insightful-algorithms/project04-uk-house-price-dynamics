# Policy Brief: UK Housing Affordability — Spatial Analysis of Local Authority Variation (2024)

**Prepared by:** Ose Omokhua  
**Date:** April 2026  
**Data sources:** HM Land Registry Price Paid Data 2024, ONS ASHE Table 7.7a 2025,
ONS House Price Statistics for Small Areas 2022, IMD 2019  

---

## Executive Summary

Housing affordability in England has reached a crisis point. The median English
local authority requires nearly ten years of median gross annual earnings to
purchase the median-priced home. This brief presents five findings from a
spatial analysis of 296 English local authorities using 2024 transaction data,
earnings data and deprivation indices. The findings have direct implications
for housing policy, planning reform and place-based investment strategy.

---

## Finding 1 — The Affordability Crisis is Spatially Concentrated

The median affordability ratio across 296 English local authorities is 9.94,
meaning the median home costs nearly ten times the median annual salary.
However this national figure conceals extreme spatial variation. Kensington
and Chelsea has a ratio of 32.0 — the median home costs 32 years of median
earnings. Kingston upon Hull has a ratio of 4.6. The gap between the most
and least affordable local authority is 27.4 ratio points, representing a
profound structural divide in access to homeownership across England.

**Commissioning implication:** Affordability policy cannot be designed at
national scale. Place-based interventions targeting specific local authorities
are required. The 20 least affordable LAs identified in this analysis should
be prioritised for shared ownership and first-homes programme delivery.

---

## Finding 2 — London is Statistically Significantly Less Affordable than England

London local authorities have a mean affordability ratio of 15.6, compared
to 9.7 for the rest of England. This difference is statistically significant
(Welch's t = 8.045, p less than 0.001, Cohen's d = 1.645). The effect size
of 1.645 standard deviations is very large by any conventional benchmark,
exceeding the threshold for a large effect (d = 0.8) by more than double.
Seven of the ten least affordable local authorities in England are London
boroughs. The South East and East of England also exceed the England median,
reflecting commuter belt demand pressure.

**Commissioning implication:** The London housing market requires policy
interventions distinct from the rest of England. Stamp duty reform, build-to-rent
incentives and affordable housing quotas should be calibrated to London-specific
affordability conditions rather than national averages.

---

## Finding 3 — Deprivation and Unaffordability are Negatively Correlated

Counter to the intuitive expectation, more deprived local authorities tend
to have lower affordability ratios (r = -0.509, R2 = 0.260, p less than 0.001).
The OLS regression coefficient of -0.233 per IMD point means that a ten-point
increase in deprivation score is associated with a 2.33-point reduction in
the affordability ratio. This reflects the fact that deprivation suppresses
house prices faster than it suppresses earnings, producing apparently more
affordable markets in the most economically distressed areas.

This finding does not mean deprived areas have good housing outcomes. It means
the price-to-earnings affordability measure does not fully capture housing
stress in deprived communities, where low asset accumulation, poor housing
quality and insecure tenure are the primary concerns rather than purchase
affordability.

**Commissioning implication:** Affordability ratios should not be used in
isolation to assess housing need in deprived areas. MHCLG should complement
price-to-earnings measures with tenure security, housing quality and
overcrowding indicators when allocating Levelling Up housing funding.

---

## Finding 4 — Property Type Premiums Vary Dramatically by Region

In London the median detached property costs £980,000 — more than the median
semi-detached in any other English region. Even London flats at £400,000 exceed
the median detached price in the North East (£257,000). The property type
hierarchy (detached most expensive, flats least expensive) holds across all
regions but the absolute gaps are far larger in London and the South East
than elsewhere. In northern regions the spread between detached and flat
median prices is approximately £150,000. In London it exceeds £580,000.

**Commissioning implication:** National house price statistics that mix property
types obscure the true scale of regional variation. Planning authorities should
set affordable housing requirements by property type within local plan
viability assessments rather than using blended regional averages.

---

## Finding 5 — The Post-COVID Price Surge was Universal but Uneven

All nine English regions experienced significant house price growth between
2020 and 2022. The South West and East of England recorded the sharpest
proportional increases, driven by remote working migration out of London.
London itself, which had shown flat prices between 2017 and 2020, surged
sharply post-2020. Northern regions also grew but from a much lower base,
meaning the absolute gap between London and the North widened even as
proportional growth rates converged.

**Commissioning implication:** The post-COVID price surge was not a London
phenomenon — it was a national structural shift. Mortgage guarantee schemes
and Help to Buy successors must be stress-tested against post-2020 price
levels across all regions, not pre-pandemic baselines.

---

## Methodology Note

Analysis used HM Land Registry Price Paid Data 2024 (758,965 Category A
transactions, 720,215 retained after geographic matching), ONS ASHE Table 7.7a
2025 for median gross annual earnings by local authority, and IMD 2019 aggregated
to LA level using population-weighted means. Affordability ratio defined as
median house price divided by median gross annual earnings, consistent with
MHCLG methodology. Statistical tests used Welch's t-test and OLS regression
via statsmodels. All analysis conducted in Python 3.13.2.