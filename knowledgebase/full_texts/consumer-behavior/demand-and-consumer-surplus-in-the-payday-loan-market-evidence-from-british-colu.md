---
title: 'Demand and consumer surplus in the payday-loan market: Evidence from British Columbia'
url: https://arxiv.org/abs/2509.15247
category: consumer-behavior
subcategory: empirical
date: 2025-09
venue: ''
authors:
- Tim Zhang
- Amity Quinn
source: arxiv
pdf_url: https://arxiv.org/pdf/2509.15247
pages: 8
chars: 15736
fetched_at: '2026-11-08T13:09:08+00:00'
kb_version: 1
---

# Demand and consumer surplus in the payday-loan market: Evidence from British Columbia

Demand and consumer surplus in the payday-loan
market: Evidence from British Columbia
Qi Zhang∗1 and Amity Quinn 1
1 University of Calgary, Calgary, AB, Canada
January 6, 2026
Abstract
This study examines how interest-rate caps affect the demand for payday loans, using
aggregate data from British Columbia from 2012 to 2019, during which the province’s
maximum fee was reduced from$23 to$17 and then to$15 per$100 borrowed. Es-
timating a linear demand function via OLS, we find that lowering interest-rate caps
significantly increases loan demand. We estimate that the$8 decrease from$23 to$15
raised annual consumer surplus by roughly$28.6 million (2012 CAD). A further re-
duction to$14, starting in January 2025, is projected to add an additional$3.9 million
per year. These results suggest that stricter interest-rate caps within a certain range
can yield substantial consumer welfare gains, with no evidence of restricted access to
payday loans due to lender exit from the market.
JEL:D14, G21, L51.
Keywords:Consumer finance; Demand; Payday loans; Interest rate cap; Consumer surplus.
1 Introduction
Payday loans are typically extended to borrowers with limited liquidity. The high cost of
this credit can lead to repeat borrowing and persistent debt cycles (Stegman (2007)). Users
of these products in North America are disproportionately young and from marginalized
communities; often women with have low or volatile incomes, precarious employment, and
thin or impaired credit histories (Buckland (2018); Apgar and Herbert (2006); Visano (2008);
Chen et al. (2022); Spotton Visano (2018)). To reduce the risk of exploitative practices
and protect vulnerable consumers, most jurisdictions in the United States and Canada have
enacted payday lending regulations. One common measure is a cap on borrowing costs, aimed
at curbing the harmful features of payday lending (Kaufman (2013); Dilay and Williams
(2018)).
∗Corresponding author: qitim.zhang@ucalgary.ca
1
arXiv:2509.15247v3  [econ.GN]  2 Jan 2026

Payday lenders typically price at or near the prevailing cap (Avery and Samolyk (2011);
Robinson (2018)). For example, a 15% cap (i.e., a$15 fee per$100 borrowed for a two-week
loan) translates into an annual percentage rate (APR) of approximately 391%. Where market
power exists, price ceilings may enhance efficiency. In addition, interest rate caps can serve
as a rudimentary form of social insurance by reallocating surplus from lower-marginal-utility
lenders to higher-marginal-utility borrowers (Glaeser and Scheinkman (1998)).
Studies on interest-rate caps for mainstream consumer loans, which typically have APRs
between 6% and 50%, show that increasing interest-rate caps raises the likelihood that
credit-constrained consumers can obtain a loan, whereas lowering the cap may restrict ac-
cess and potentially harm these borrowers (Rigbi (2013); Madeira (2019)). However, the
population targeted by payday loans is very different from that of mainstream consumer
loans, and there is little existing evidence examining how interest rates affect the demand
for payday loans and the resulting consumer surplus. Only one earlier study exploited
transaction-level data to examine the reduction of the maximum fee per$100 borrowed from
$15 to$10 in Rhode Island and estimated an annual consumer-surplus gain of approximately
$3.4 million (USD) (Fekrazad (2020)). In this study, we exploit multiple policy changes in
British Columbia—which has a payday loan market roughly five times larger than Rhode
Island’s—to analyze cap reductions between 2012 and 2019 that lowered the maximum fee
per$100 borrowed from$23 to$17, and subsequently to$15. Using provincial-level aggre-
gate data on borrowing costs and total loan volume, we estimate a linear demand curve for
payday loans and calculate the associated welfare effects. We estimate that the$8 reduction
from$23 to$15 increased consumer surplus by approximately$28.6 million per year (2012
CAD). A more recent policy, effective January 2025, further reduces the cap from$15 to$14
per$100, and we estimate that this change will generate an additional$3.9 million (2012
CAD) in annual consumer surplus.
2 Data
The payday-loan industry in British Columbia is licensed and regulated by Consumer
Protection BC, which compiles annual operational statistics from all licensed lenders. The
available dataset includes each year’s average borrowing cost (the fee charged per$100 loan
on a two-week term), total loan volume in nominal dollars, and total loan volume in real 2012
CAD (adjusted for inflation). Our sample covers 2012 through 2023, and summary statistics
are provided in Table 1 (loan volumes are rounded to the nearest$0.1 million). Over this
period, the regulated maximum fee per$100 was progressively lowered from$23 (2012–2016)
to$17 in 2017, and to$15 from 2018 onward. In practice, lenders priced loans at or very
near the cap in each year. The reported annual average borrowing cost can slightly exceed
the nominal cap in some years due to reporting cycle misalignment.
It is also worth noting that the number of physical storefront lenders began declining in
2015, rebounded slightly in 2018 and 2019, and has continued to decline since then, while
online payday lending in British Columbia began expanding in 2020.
2

Table 1: British Columbia payday-loan market statistics, 2012-2023
Year Borrowing cost Annual loan volume Total loan volume # of locations # of locations
(per CAD 100) (nominal CAD) (2012 CAD) (H.O. +Branches) (Online only)
2012 21.50 318.1 Mil 318.1 Mil 274 -
2013 21.70 351.4 Mil 344.4 Mil 275 -
2014 21.90 385.3 Mil 370.3 Mil 274 -
2015 21.70 340.9 Mil 321.2 Mil 226 -
2016 21.70 369.7 Mil 341.5 Mil 209 -
2017 19.30 397.3 Mil 359.8 Mil 192 -
2018 16.82 416.1 Mil 369.5 Mil 202 -
2019 15.30 441.5 Mil 384.4 Mil 204 -
2020 14.92 390.7 Mil 333.5 Mil 194 14
2021 14.69 271.5 Mil 227.2 Mil 187 15
2022 14.85 305.7 Mil 250.8 Mil 173 21
2023 14.92 327.2 Mil 263.2 Mil 170 21
Notes:Borrowing cost is the dollar fee per CAD 100 borrowed on 14-day terms. Loan volumes are annual
totals and are rounded to the nearest 0.1 million CAD. Real dollars are deflated to 2012 CAD.
3 Model
3.1 Demand of payday loans
As in Fekrazad (2020), we assume that borrowers face a linear inverse demand curve for
payday loans, given by:
Q=a−bp, b >0,(1)
wherepis the borrowing cost per CAD 100 (the fee per$100 loan for a two-week term) and
Qis the total annual real loan volume (in year 2012 values). Under a binding interest rate
cap,pis effectively set by policy andQis determined by demand at that price.
3.2 Estimation of demand
To empirically estimate the demand curve, we focus on the period before 2020. We ex-
clude observations from 2020–2023 because the Canadian government’s temporary COVID-
19 income-support programs during those years materially altered consumers’ short-term
credit needs. These developments could confound the price–quantity relationship in the
later data. Given that we have only annual observations, adding additional control variables
or policy dummies is not feasible (doing so would exhaust our degrees of freedom and ob-
scure identification). We therefore restrict the sample to 2012–2019 and run a simple OLS
regression of annual real loan volume (2012 CAD) on the actual borrowing cost per$100.
Although this yields only eight data points, prior research suggests that even a small
sample can produce informative estimates when the underlying relationship is strong and
stable (Jenkins and Quintana-Ascencio (2020)). Consistent with theory, the estimated slope
coefficient is negative and statistically significant: ˆβ=−6.61 million CAD (SE = 2.62
3

Table 2: Demand estimation: real loan volume on borrowing cost (2012–2019)
DV: Real loan volume (2012$)
Borrowing cost (per$100) -6,621,526**
(2,618,230)
Constant 483,509,000***
(52,700,000)
Observations 8
R-squared 0.5154
F-statistic 6.38
Prob>F 0.0449
Notes: OLS regression of annual real loan volume
(2012 CAD) on the borrowing cost per$100, restricted
to years with fee cap above the 2020 change (2012–
2019;N= 8). Robust standard errors in parentheses.
∗p <0.10, ∗∗p <0.05, ∗∗∗p <0.01.
million). This implies that a$1 increase in the fee per$100 is associated with about a 6.61
million CAD decrease in annual loan volume. The estimated intercept is ˆα= 483.5 million
CAD (SE = 52.7 million). These OLS results are reported in Table 2.
4 Consumer surplus gains from lower interest rate caps
We quantify consumer-surplus (CS) gains from two cap reductions: (i) lowering the cap
from$23 to$15 per$100 borrowed, and (ii) lowering it further from$15 to$14 per$100
(implemented Canada-wide in January 2025). Using the estimated demand curve ˆQ(p) =
ˆa−ˆbpwith ˆa= 483.509 and ˆb= 6.621 (whereQis in millions of 2012 CAD andpin dollars
per$100), predicted volumes are
Q23 = ˆQ(23) = 331.226 million, Q 15 = ˆQ(15) = 384.194 million, Q 14 = ˆQ(14) = 390.815 million.
The CS change from reducing the cap fromp 1 top 2 (p2 < p1) equals the area under demand
betweenp 1 andp 2:
∆CS(p 1 →p 2) = 1 100 Z p1 p2 ˆQ(p)dp= 1 100 h ˆa(p1 −p 2)− ˆb 2  p2 1 −p 2 2 i ,(2)
where the factor 1/100 converts the fee (quoted per$100) to a per$1 price for integration.
Plugging in ˆaandˆb, we obtain ∆CS23→15 ≈28.62 million (2012 CAD) and ∆CS 15→14 ≈3.88
million (2012 CAD) per year. The latter figure is the projected annual benefit from the new
cap introduced in 2025.
4

5 Robustness Check
To further ensure the reliability of our primary findings, we estimate a quadratic demand
curve using 2012–2019 data, modeling real annual payday loan volumeQ(p) (in 2012 dollars)
as a function of the cost of borrowingp(in dollars per$100):
Q(p) =a−b p+c p 2, b >0,
where the estimated coefficients from OLS are:
ˆa= 671,000,000, ˆb= 26,900,000,ˆc= 539,434.
This functional form allows for curvature in borrower response to price, with a slight flat-
tening at higher prices.
Evaluating ˆQ(p) at the relevant cap levels yields: ˆQ(23) = 337.936 million, ˆQ(15) =
388.872 million, ˆQ(14) = 400.130 million.
The change in consumer surplus (CS) when price falls fromp 1 top 2 is:
∆CS(p 1 →p 2) = 1 100 Z p1 p2 ˆQ(p)dp= 1 100 h ˆa(p1 −p 2)− ˆb 2  p2 1 −p 2 2  + ˆc 3  p3 1 −p 3 2 i .(3)
Plugging in ˆaandˆb, we obtain ∆CS23→15 ≈28.59 million (2012 CAD) and ∆CS 15→14 ≈3.94
million (2012 CAD) per year. These figures are very close to the estimates obtained from
the linear demand specification.
6 Conclusion
Using a small set of annual aggregate data, we estimate a linear demand curve for payday
loans and approximate the associated consumer surplus. Despite the coarse granularity of the
data—and the necessarily approximate welfare calculations—the results are consistent and
policy-relevant. In British Columbia, lowering the cap from$23 to$15 per$100 borrowed
coincided with a sizable increase in annual loan volume (from roughly$331 million to$384
million, 2012 CAD) and an estimated$28.6 million gain in consumer surplus per year. A
further cap reduction to$14 per$100 (implemented nationally in 2025) is projected to
add about$3.9 million annually. These findings are consistent with an earlier study that
investigated a similar policy change in the United States, which suggests that tighter interest-
rate ceilings can enhance borrower welfare without suppressing overall loan usage (Fekrazad
(2020)).
The contraction of storefront lenders alongside the rise of online providers points to
heterogeneous cost structures: online firms may profitably extend credit at lower fees than
brick-and-mortar lenders. Nevertheless, policymakers should consider potential supply-side
responses when evaluating further cap reductions. Prior research suggests that lowering the
interest-rate cap from$15 to$10 per$100 borrowed may have contributed to lender exit
and reduced consumer access in Oregon (Zinman (2010)). However, these findings should be
interpreted with caution, as the average payday-loan default rate in Oregon—approximately
5

10 to 12 percent—is substantially higher than the 2 to 5 percent range observed in British
Columbia. In contrast, a more recent study examining the same policy change in Rhode
Island, where default rates are similar to those in British Columbia, found no evidence of
reduced access resulting from the cap reduction (Fekrazad (2020)).
Our main findings are based on only a few aggregate data points from a single province
in Canada, and much more can be learned from future research using aggregate data from
multiple jurisdictions and micro-level data to examine heterogeneity across borrower seg-
ments, default risk, and lender margins, as well as to assess substitution toward other forms
of credit. Overall, our evidence supports carefully calibrated caps within a certain range
as a viable consumer-protection tool in high-cost credit markets—provided that regulators
continue to monitor market composition and credit access as the industry evolves.
Funding
No funding was received for this work.
Disclosure statement
No potential conflict of interest was reported by the authors.
6

References
Apgar, William C and Christopher Edward Herbert (2006),Subprime lending and alternative
financial service providers: A literature review and empirical analysis. US Department of
Housing and Urban Development.
Avery, Robert B and Katherine A Samolyk (2011), “Payday loans versus pawn shops: The
effects of loan fee limits on household use.”Available at SSRN 2634584.
Buckland, Jerry (2018), “A socio-economic examination of payday loan clients: why and how
people use payday loans.” InPayday Lending in Canada in a Global Context: A Mature
Industry with Chronic Challenges, 65–81, Springer.
Chen, Zibei, Terri Friedline, and Catherine M Lemieux (2022), “A national examination on
payday loan use and financial well-being: a propensity score matching approach.”Journal
of Family and Economic Issues, 43, 678–689.
Dilay, Katrine and Byron Williams (2018), “Payday lending regulations.” InPayday lend-
ing in Canada in a global context: A mature industry with chronic challenges, 177–218,
Springer.
Fekrazad, Amir (2020), “Impacts of interest rate caps on the payday loan market: Evidence
from rhode island.”Journal of banking & finance, 113, 105750.
Glaeser, Edward L and Jose Scheinkman (1998), “Neither a borrower nor a lender be: An
economic analysis of interest restrictions and usury laws.”The Journal of Law and Eco-
nomics, 41, 1–36.
Jenkins, David G and Pedro F Quintana-Ascencio (2020), “A solution to minimum sample
size for regressions.”PloS one, 15, e0229345.
Kaufman, Alex (2013), “Payday lending regulation.”FEDS Working Paper.
Madeira, Carlos (2019), “The impact of interest rate ceilings on households’ credit access:
Evidence from a 2013 chilean legislation.”Journal of Banking & Finance, 106, 166–179.
Rigbi, Oren (2013), “The effects of usury laws: Evidence from the online loan market.”
Review of Economics and Statistics, 95, 1238–1248.
Robinson, Chris (2018), “A business analysis of the payday loan industry.” InPayday Lending
in Canada in a Global Context: A Mature Industry with Chronic Challenges, 83–127,
Springer.
Spotton Visano, Brenda (2018), “Mainstream financial institution alternatives to the payday
loans.” InPayday lending in Canada in a global context: A mature industry with chronic
challenges, 147–175, Springer.
Stegman, Michael A (2007), “Payday lending.”Journal of Economic Perspectives, 21, 169–
190.
7

Visano, Brenda Spotton (2008), “Different and unequal: Payday loans and microcredit in
canada.”The Journal of Economic Asymmetries, 5, 109–123.
Zinman, Jonathan (2010), “Restricting consumer credit access: Household survey evidence
on effects around the oregon rate cap.”Journal of banking & finance, 34, 546–556.
8
