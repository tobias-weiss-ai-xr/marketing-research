---
title: Most certainly certain? The Impact of Contract for Difference Design on Renewables' Strike Prices
  and Electricity Market Risks
url: https://arxiv.org/abs/2512.17508
category: consumer-behavior
subcategory: empirical
date: 2025-12
venue: ''
authors:
- Silke Johanndeiter
- Jonas Finke
- Justus Heuer
source: arxiv
pdf_url: https://arxiv.org/pdf/2512.17508
pages: 39
chars: 74947
fetched_at: '2026-11-08T13:07:29+00:00'
kb_version: 1
---

# Most certainly certain? The Impact of Contract for Difference Design on Renewables' Strike Prices and Electricity Market Risks

Highlights
Most certainly certain? The Impact of Contract for Difference Design
on Renewables’ Strike Prices and Electricity Market Risks
Silke Johanndeiter, Jonas Finke, Justus Heuer
•Derivation of optimal strike prices in competitive CfD auction under uncer-
tainty
•Investor expectations formed through 36 market scenarios in energy system
model
•CfDs significantly reduce both profit and consumer price volatility
•CfD design affects profit volatility, but hardly consumer price volatility
•Reference power plant drives both profit volatility and system-friendly invest
arXiv:2512.17508v1  [econ.GN]  19 Dec 2025

Most certainly certain? The Impact of Contract for
Difference Design on Renewables’ Strike Prices and
Electricity Market Risks
Silke Johanndeitera,∗, Jonas Finkea, Justus Heuerb
aRuhr-Universität Bochum, Universitätsstr. 150, 44801 Bochum, Germany
bUniversität zu Köln, Albertus-Magnus-Platz, 50923 Köln, Germany
Abstract
Weather, technological and regulatory uncertainties expose actors in highly renew-
able electricity markets to substantial price and volume risks. Two-way Contracts
for Difference (CfDs) can mitigate these risks. They stipulate payments between
the government and generators of renewable electricity based on the difference of
a strike and a reference price, whose definition and unit of payment differ between
CfD designs. We study the effect of three different CfD designs on wind power
profit and consumer price volatility under the consideration of uncertain market
outcomes in a highly renewable, sector-coupled electricity market. First, we an-
alytically derive optimal strike prices under uncertainty. Second, we numerically
determine optimal strike prices based on market expectations retrieved from opti-
mising a set of 36 market scenarios in an energy system model. Third, we study
the distribution of ex post market revenues, CfD payments and consumer prices
across all 36 scenarios. Compared to purely market-based consumer prices and
investor profits, we find all CfDs to significantly reduce volatility. For consumer
prices, results show no substantial differences between CfD designs. For investor
profits, we identify the highest volatility reduction under a capacity-based CfD
with a reference price similar to power plants’ individual market revenues. Since
such a CfD design is known to diminish the effect of price signals on investment
decisions, our results reveal a trade-off between incentivising system-friendliness
and reducing investor risk.
Keywords:support schemes, renewables, electricity market, uncertainty,
Contract for Difference, volatility, CfD auction
∗silke.johanndeiter@rub.de

1. Introduction
The transition to a climate-neutral energy system exposes electricity market
actors to significant risks. Consequences of a severe price shock in the European
electricity market became evident during the energy crisis in 2022, when renewables
achieved windfall profits at the expense of rising consumer bills (Antón, 2023). As a
response, the European Union introduced two-way Contracts for Difference (CfDs)
as the mandatory support scheme for renewables due to their capability to mitigate
risks for both generators and consumers of electricity (Directive 2024/1711, 2024).
They stipulate payments between the government and producers of renewable elec-
tricity defined by the difference of an ex post realised reference price and an ex ante
agreed-upon strike price over a given contracting period – typically the expected
plant operation time (Schlecht et al., 2024). Two-way CfDs generally decrease
generator revenues in times of high electricity prices, and increase them, when
electricity prices are low, affecting both average revenues and revenue volatility.
If CfD expenses and revenues are passed on to consumers via levies, they impact
consumer prices in the opposite direction. There exist numerous design options of
CfDs that affect their potential to reduce volatility of investor profits and consumer
prices. Our work assesses the impact of three two-way CfD design options on these
values in a highly renewable European electricity market.
1.1. Derisking and financing costs
In the last decade, renewables became competitive with fossil fuels in terms of
levelised cost of electricity (LCOE) (Kost et al., 2024). Since then, the primary ob-
jective of renewable support schemes has shifted from increasing average revenues
to reducing revenue uncertainty (Beiter et al., 2024). Underlying revenue risks can
be split into two components (Schlecht et al., 2024):
1. Volume risk: The uncertainty about the amount of generated electricity,
which mainly depends on the weather and curtailment.
2. Price risk: The uncertainty about the market value of the generated elec-
tricity, which depends on overall market trends, the total fleet of generators,
infrastructure constraints, and political factors.
2

Several studies provide empirical or model-based evidence that lowering these
revenue risks leads to reduced financing costs for renewable investments. For the
Australian electricity market, Gohdes et al. (2022) show an empirical correlation
between the availability of long-term risk hedging options for renewable invest-
ments and lower LCOEs. Using a liquidity management model, Ðukan et al. (2025)
demonstrate how revenue stabilisation with CfDs decreases financing costs by al-
lowing to decrease debt size. In a costly state verification framework, Soysal (2025)
predicts the effect of revenue variability on the default risk and, subsequently, cost
of capital. Lévêque et al. (2026) combine a model-based calculation of cost of debt
and equity with global data on policy regimes and cost of capital across different
countries to show an empirical correlation between risk reduction through policy
and lower financing costs. These, in turn, have a significant positive effect on the
expansion of renewable electricity generation as a capital-cost-intensive technology
(Bachner et al., 2019; Egli et al., 2020) and thus also reduce total costs in highly
renewable power system (Helistö et al., 2024).
There exist private markets for long-term contracts to hedge risks. Forward
and future contracts provide hedges up to 5 or even 10 years ahead of delivery
(EEX, 2025). In the context of renewables, the market for private power purchase
agreements (PPAs) with contract durations of 15 years or more is growing (RE-
Source, 2025). However, the market for long-term private-to-private risk hedging
instruments still lacks liquidity – an issue coined the missing risk market problem
by Dimanchev et al. (2024). Various instruments, such as market-maker obliga-
tions, can increase market liquidity (Schittekatte and Batlle, 2023). Nevertheless,
some scholars argue for the necessity of governmentally issued long-term contracts
(Fabra, 2022; Neuhoff et al., 2023). In addition to addressing the lack of liquid-
ity, they reduce price risks for household consumers, who lack access to long-term
private risk-hedging instruments, such as PPAs, whose offtakers are dominated by
corporate consumers (Mili and Côté, 2025).
1.2. CfD design elements
Two-way CfDs are such governmentally issued long-term contracts. They have
two main design elements that affect their potential to reduce risk and their impact
3

on system costs. The first element is thereference price. It is mainly determined
by the length of the reference period, i.e., the time frame used to calculate it, and
the selection of reference generators, i.e., whether all or only some power plants
are considered. The simplest CfD types compare individual market performance
in (quarter-)hourly trading windows to the strike price. Such simple CfDs en-
tirely hedge price risks (Wagner et al., 2026). However, this also implies that they
eliminate market price signals, thereby incentivising to design, site and operate
a power plant in a manner that merely maximises full load hours. Conversely,
more sophisticated CfDs preserve market price signals in both the investment and
operational phase by decoupling individual market revenues from CfD payments.
These CfD types use market revenues of a reference power plant (e.g., the market’s
average) over longer periods (e.g., a month or a year) as reference price. In this
case, power plants can retain market revenues above the reference price. Thus, this
CfD design incentivises investments in power plants with an above-average market
performance (Schmidt et al., 2013; May, 2017; Meus et al., 2021). These power
plants can be deemed moresystem-friendly, as higher market values typically im-
ply a higher temporal match of a power plant’s supply and load, therefore inducing
lower balancing costs (Ueckerdt et al., 2013). Similarly, Diallo and Kitzing (2024)
associate market values with the social value of a power plant. For highly renewable
energy systems, CfDs that retain market price signals are indeed shown to lower
system costs (Veenstra and Mulder, 2024; Johanndeiter et al., 2025a). However,
such CfD designs also imply that not all price risks are fully hedged (Wagner et al.,
2026).
The second important design element of CfDs is theunit of payment: Reference
and strike prices can either be production- or capacity-based, influencing both risk
reduction as well as investment and operational incentives. Production-based CfDs
only capture price risks, while capacity-based CfDs also hedge against volume risk.
Furthermore, production-based CfDs are known to distort dispatch decisions in the
sense that they cause power plants to be dispatched at prices below their marginal
production costs (De Vos, 2015; Andor and Voss, 2016; Frondel et al., 2022). If the
reference price is equal to the (quarter-)hourly spot market price, they incentivise
4

to maximise output regardless of the electricity price. If the reference period is
longer, they induce so-called virtual variable costs or revenues equal to anticipated
CfD payments to or from the government. Virtual costs cause power plants to
be dispatched only at price levels above the amount of the CfD payment, whereas
virtual revenues lead to dispatch even at negative prices (Rosnes, 2014; Pahle et al.,
2016; Chaves-Avila et al., 2017; Frey et al., 2020). The cited studies are described
in more detail in Johanndeiter et al. (2025a), while conceptual discussions of these
and further design aspects are provided by Huntington et al. (2017), Newbery
(2023) and Schlecht et al. (2024).
1.3. Market risks in the energy transition
Our work focuses on the impact of CfD design on risks in highly renewable elec-
tricity markets. A main driver of both volume and price risks in an energy system
dominated by weather-dependent power supply is weather risk (Blazquez et al.,
2018; Alonzo et al., 2022; Sanchez Jimenez et al., 2024). Volume risk is addition-
ally affected by curtailment risk (Egli, 2020). Further risks arise from technological
uncertainty that, amongst others, is reflected in unknown cost and demand levels:
Cost degression rates of both renewables and battery storages have been system-
atically underestimated (Xiao et al., 2021; Ziegler and Trancik, 2021). Electricity
demand levels for Europe can vary by 2000 TWh in just one single study (European
Commission, 2018), and future hydrogen demand levels are even more uncertain
(Hanley et al., 2018). Furthermore, fuel costs are shown to continue to affect
market prices in highly renewable electricity markets (Ruhnau, 2022; Johanndeiter
et al., 2025b) and historically proven to be volatile (Furió and Chuliá, 2012). Fur-
thermore, regulatory uncertainty exposes investors to significant price and volume
risks, including uncertainty regarding the introduction of capacity remuneration
mechanisms, coal or nuclear phase outs, renewable targets, revenue caps or CO2
prices. Together with other macro risks, such as general macroeconomic and po-
litical stability, Lévêque et al. (2026) find this type of risk to constitute the main
share of renewable projects’ cost of capital.
5

1.4. CfD design and derisking
In a CfD setting, the above-described uncertainties are reflected in CfDs’ under-
lying strike prices that are agreed upon prior to the investment and kept constant
for the entire contract duration. Compliant with European regulation (Directive
2018/2001), strike prices are determined within competitive auctions that allocate
CfDs to specific renewable energy capacities (Anatolitis and Welisch, 2017). Di-
allo and Kitzing (2024) and Johanndeiter et al. (2025a) show how optimal strike
prices in a competitive auction for a CfD take into account the above-described
incentives: If the CfD auction for the strike price is perfectly competitive, an in-
vestor bids a strike price that sets expected profits including CfD payments over
the economic lifetime of the investment project to zero. Therefore, the strike price
also reflects the relative market performance of a power plant, if the CfD design
includes incentives for system-friendly investments. However, expected electricity
generation and market revenues over economic lifetimes of typically 15 or more
years are subject to the above-described uncertainties. Therefore, investors are re-
quired to form expectations on these revenue determinants to calculate their strike
price bids for the auction. Actual market revenues and subsequent CfD payments,
in turn, are determined based on ex post outcomes, i.e., market prices and electric-
ity generation. Hence, ex post investor profits are not necessarily zero, if expected
market outcomes used to determine strike prices deviate from ex post outcomes.
Previous work analyses the effect of support scheme design on risk exposure,
financing cost and/or strike prices: Using models of renewable projects’ financing
structure, Neuhoff et al. (2022) and Ðukan and Kitzing (2023) show that strike
prices are lower under a one-way (also deemed sliding market premia) than under
a two-way CfD, while financing costs are higher due to their greater exposure to
electricity market price risks. Breitschopf and Alexander-Haw (2022) provide em-
pirical evidence that lower market price exposure indeed decreases financing costs.
Relatedly, in a real-options approach applied to a Nordic wind power case study,
Boomsma et al. (2012) conclude that renewable support schemes with a higher
risk exposure, particularly tradable green certificates compared to feed-in tariffs,
require higher revenues to trigger investments. Boomsma and Linnerud (2015), in
6

turn, show how risk exposure can be decreased by diversification and Fagiani et al.
(2013) highlight the impact of risk preferences on the cost-efficiency of the two
support schemes. Based on a conceptual discussion, Hiroux and Saguan (2010)
suggest that price premia strike an ideal balance between support schemes that
expose power plants to accurate market price signals and risk reduction. Finally,
Wagner et al. (2026) study the interaction of forward markets and CfDs and show
that CfD designs with shorter reference periods decrease forward market liquidity
– possibly undermining the purpose of CfDs. Yet, besides Wagner et al. (2026),
existing studies are limited to simple support scheme designs, such as feed-in tar-
iffs, fixed market premia or sliding market premia/CfDs based on the hourly spot
market price. Furthermore, to the best of our knowledge, there exists no previous
work that focuses on the deviation of ex post market realisations from ex ante
expectations used to determine a support scheme’s underlying strike price.
We close this gap by analysing profit volatility of wind onshore power plants
and consumer prices under three designs of two-way CfDs. The novelty of our work
lies in the consideration of uncertain market outcomes in a sector-coupled, highly
renewable European power system that are reflected in the CfDs’ underlying strike
prices. Furthermore, we uniquely consider CfD designs that vary in terms of the
reference price and the unit of payment. Particularly, we consider two production-
based CfDs and one capacity-based CfD. One production-based CfD’s reference
price is defined as the hourly spot market price, while the other considered CfD
types use average revenues of all wind power plants in one bidding zone as ref-
erence price. Furthermore, we consider two wind production profiles by bidding
zone: one with above-average full load hours and one with an above-average mar-
ket value, where the latter would be considered moresystem-friendlyaccording to
our definition above. In this study, we first build an analytic model to determine
strike price bids for three different CfD designs based on ex ante price and vol-
ume expectations (Section 2). Second, we retrieve required expectations from a
sector-coupled power system model that we apply to optimise a set of scenarios of
a highly renewable European electricity market that reflect both weather risks and
7

technological risks (Section 3). Third, we use the optimisation results to deter-
mine ex ante optimal strike prices by CfD design and calculate each power plant’s
revenues from market sales, CfD payments and costs that would result ex post in
each scenario realisation. This allows us to determine the level of cost recovery as
well as subsequent effects on consumer prices, if CfD payments are financed via a
levy. We then analyse the volatility of cost recovery and consumer prices by CfD
type across scenarios (Section 4). Finally, Section 5 concludes.
2. Theoretical background
Consider a renewable power planti∈Ilocated in bidding zonen∈N. Its
annual profit
Πtype i,n = X
t∈T
qt,i,npt,n −C i,n +P type i,n (1)
is given by spot market revenues minus costs plus net CfD payments from or to
the government. Spot market revenues result from selling power quantitiesqt,i,n
for pricesp t,n in every time stept∈Tof the year. Costs
Ci,n =c·
X
t∈T
qt,i,n +A·M·Q i,n (2)
include variable costscincurred per quantity produced and investment costsM
incurred per installed capacityQ i,n that are annualised with annuity factorA.
CfD payments and therefore profitsP type i,n differ by type∈ {basic, 2way, fin}of
CfD. They depend on a possibly time-dependent reference pricepR,type t,n , which is
uniform within each bidding zone and determined ex post, as well as an individual
strike priceStype i,n per power plant that is set ex ante. For simplicity, we assume that
c,AandMdo not depend on bidding zone or power plant, i.e. we consider only
one power plant technology with homogeneous cost assumptions across countries.
Hence, power plantsi∈Ionly differ in terms of their generation profiles.
In the following, we introduce the three CfD types together with how strike
prices are formed. Then we derive optimal strike prices for each CfD type, first
without and then with uncertainty.
8

Table 1: Overview of considered CfD designs
CfD type Unit of payment Reference price
BasicAC/MWh Hourly spot market price
2wayAC/MWh Average wind market value
FinancialAC/MW Average wind revenues per capacity
2.1. Definition of CfD types
Following Johanndeiter et al. (2025a), we consider two production-based CfDs,
the basic and the 2way CfD that differ in terms of their reference price. For the
basic CfD, the reference price is the hourly market price,pR,basic t,n =p t,n, so that
payments are given by
Pbasic i,n = X
t∈T
(Sbasic i,n −p t,n)q t,i,n.(3)
Forthe2wayCfD,thereferencepriceequalstheyearlyzonalmarketvalue,p R,2way t,n =
vn for allt∈T, which is defined as the generation-weighted market revenues aver-
aged over the entire year and all power plants in bidding zonen1. That is,
P2way i,n = (S2way i,n −v n) X
t∈T
qt,i,n,(4)
where
vn =
P
t∈T
P
i∈I qt,i,n pt,nP
t∈T
P
i∈I qt,i,n
.(5)
Substituting the CfD payments (3) and (4) in the profit function (1) shows that
in some cases, generation may increase profit even at negative prices or decrease
profit even at prices above the variable cost. Therefore, both production-based
CfD types may distort optimal dispatch.
Moreover, weconsiderthecapacity-basedfinancialCfDasproposedbySchlecht
et al. (2024) that resembles the capacity-based support scheme proposed by Hunt-
1Although all of the considered CfD designs are two-way CfDs, we name this type of CfD
“2way” as it most closely corresponds to two-way CfDs as implemented in practice. In contrast,
the “basic” CfD is equivalent to a feed-in tariff.
9

ington et al. (2017). For this CfD type, the reference price (now in units ofAC/MW)
is given by the average annual revenues per unit capacity of a reference power plant,
pR,fin t,n =r n. Here, we form the average across all power plants in one bidding zone,
i.e.
rn =
P
t∈T
P
i∈I qt,i,n pt,nP
i∈I Qi,n
,(6)
so that CfD payments are given by
Pfin i,n =Q i,n(Sfin i,n −r fin n ).(7)
2.2. Optimal strike prices without uncertainty
Compliant with European law (Directive 2018/2001), we assume CfDs to be
awarded within a tendering procedure. Particularly, we suppose a limited number
of renewable capacities to be awarded within a competitive pay-as-bid auction for
the strike price for a contract duration that equals power plants’ economic lifetime.
Then, a rational, risk-neutral investor chooses a strike price that sets expected
profits over lifetime to zero. For this case, Johanndeiter et al. (2025a) derive
optimal ex ante strike pricesStype* i,n under perfect foresight.
For the basic CfD, the optimal strike price equals the individual levelised cost
of electricity (LCOE),
Sbasic* i,n = Ci,nP
t∈T qt,i,n
≡lcoe i,n.(8)
For the 2way CfD, the optimal strike price equals the LCOE, but adopted for the
difference between the power plant-averaged market valuevn and the individual
market valuev i,n,
S2way* i,n = Ci,nP
t∈T qt,i,n
+
P
t∈T
P
i∈I qt,i,npt,nP
t∈T
P
i∈I qt,i,n
−
P
t∈T qt,i,npt,nP
t∈T qt,i,n | {z }
≡vi,n
=lcoe i,n +v n −v i,n.(9)
10

For the financial CfD, the optimal strike price (inAC/MW) follows the same pattern,
but costs and revenues are normalised per capacity instead of generation. That is,
with market revenues per capacity given byri,n for an individual power plant and
byr n when averaged over all power plants, the optimal strike price equals
Sfin* i,n = Ci,n Qi,n + P t∈T P i∈I qt,i,npt,nP i∈I Qi,n | {z }
≡rn
−
P
t∈T qt,i,npt,n
Qi,n| {z }
≡ri,n
= Ci,n
Qi,n
+r n −r i,n.(10)
Here, we assume that the total generationP t∈T qt,i,n and the capacityQi,n are
strictly positive. The definitions of lcoei,n, vn, vi,n, rn, ri,n can simply be extended
to equal zero otherwise.
The optimal strike prices illustrate investment incentives set by each type of
CfD: in a competitive auction, the basic CfD is awarded to power plants with
the lowest LCOE, typically driven by a high expected number of full load hours.
Conversely, the 2way and financial CfDs allow power plants to accept a strike
price lower (higher) than their expected average costs, if expected market revenues
are higher (lower) than the reference price. Thus, they incentivise system-friendly
investment decisions as indicated by a higher market value (cf. Section 1.2).
2.3. Optimal strike prices under uncertainty
Several variables in Equations (8), (9) and (10) are uncertain at the time of
the auction, requiring investors to form expectations. We assume that the uniform
cost parametersc,AandMfeeding intoC i,n are known to investors with certainty.
Hence, for calculating its optimal strike price, the power plantiin bidding zonen
needs the following parameters for the own bidding zone that remain uncertain:
•Hourly market pricesp t,n for allt∈T
•Hourly capacity factorf t,i,n ≡q t,i,n/Qi,n of the own power plant for allt∈T
•Hourly capacity factorsf j,t,n of all other power plantsj∈I\ {i}for allt∈T
•Ratio of the capacity of power plantito total capacities (of the considered
technology)w i,n ≡Q i,n/ P i∈I Qi,n for alli∈I.
11

We assume investors to form expectations as expected valuesE{s∈S}[·]of the
relevant uncertain terms throughout a discrete, finite set of electricity market sce-
narios represented from here on by introducing a new indexs∈S. Accordingly,
optimal strike prices under uncertainty ˜Stype i,n can be derived by substituting the
cost Equation (2) andP t∈T ft,i,n,s = P t∈T qt,i,n,s/Qi,n,s as well as using linearity of
expectation in Equations (8), (9) and (10).
For the basic CfD, uncertainty only occurs in the own capacity factor,
˜Sbasic i,n =E {s∈S}[lcoei,n,s] =c+E {s∈S}
 A·MP
t∈T ft,i,n,s

=c+ A·MP
t∈T E{s∈S}[ft,i,n,s].(11)
For the 2way CfD, we approximate
˜S2way i,n =E {s∈S}[lcoei,n,s] +E {s∈S}[vn,s]−E {s∈S}[vi,n,s]
=c+ A·MPT
t=1 E{s∈S}[ft,i,n,s]
+E {s∈S}
" PT
t=1
P
i∈I[ft,i,n,s ·p t,n,s] PT
t=1
P
i∈I[ft,i,n,s]
#
−E {s∈S}
" PT
t=1[ft,i,n,s ·p t,n,s]PT
t=1[ft,i,n,s]
#
≈c+ A·MPT
t=1 E{s∈S}[ft,i,n,s]
+
PT
t=1
P
i∈I E{s∈S}[ft,i,n,s ·p t,n,s] PT
t=1
P
i∈I E{s∈S}[ft,i,n,s]
−
PT
t=1 E{s∈S}[ft,i,n,s ·p t,n,s]PT
t=1 E{s∈S}[ft,i,n,s]
(12)
byusingasecondorderTaylorexpansionE
 X
Y

≈ E(X) E(Y) −Cov(X,Y) (E(Y)) 2 + E(X)Var(Y) (E(Y)) 3 ≈
E(X)
E(Y) as in our caseCov(X,Y) (E(Y)) 2 + E(X)Var(Y) (E(Y)) 3 ≈0(Stuart and Ord, 2010).
For the financial CfD, we derive
˜Sfin i,n =E {s∈S}
 Ci,n,s
Qi,n,s

+E {s∈S}[rn]−E {s∈S}[ri,n]
=
X
t∈T
c·E {s∈S}[ft,i,n,s] +A·M+
X
i∈I
X
t∈T
E{s∈S} [wi,n,s ·f t,i,n,s ·p t,n,s]
−
X
t∈T
E{s∈S}[ft,i,n,s ·p t,n,s].(13)
12

Now, wecancomputetheremainingexpectedvaluesinEquations(11), (12)and
(13) by assigning an equal weight of1 S to each scenario, and using the covariance
Cov [X, Y] =E[(X−E[X]) (Y−E[Y])] =E[XY]−E[X]E[Y].
For the simple expected values we use
E{s∈S}[fi,t,n,s] = 1 S
SX
s=1
ft,i,n,s (14)
and
E{s∈S}[pt,n,s] = 1 S
SX
s=1
pt,n,s (15)
for products of two uncertain variables,
E{s∈S}[ft,i,n,s ·p t,n,s] =E {s∈S}[ft,i,n,s]·E {s∈S}[pt,n,s] + Cov{s∈S}[ft,i,n,s, pt,n,s],(16)
where the covariance for a finite, discrete set of scenarios can be simplified as
Cov{s∈S}[ft,i,n,s, pt,n,s] = 1 S
SX
s=1
(ft,i,n,s −E {s∈S}[ft,i,n,s])(pt,n,s −E {s∈S}[pt,n,s]).(17)
Finally, this covariance can also be used to simplify the product of three variables
E{s∈S}[wi,n,s ·f t,i,n,s ·p t,n,s] =E {s∈S}[wi,n,s]·E {s∈S}[ft,i,n,s]·E {s∈S}[pt,n,s]
+E {s∈S}[wi,n,s]·Cov {s∈S}[ft,i,n,s, pt,n,s]
+ Cov{s∈S}[wi,n,s, ft,i,n,s ·p t,n,s],(18)
where the last covariance term may be dropped if assuming that the share of own
capacity compared to total capacity is independent of the own revenues per unit
capacity.
13

3. Methodology
We study volatility of wind power plant revenues and consumer costs under dif-
ferent types of CfDs in three steps. First, we optimise an ensemble of deterministic
scenarios of a fully decarbonised European electricity market with a high share of
variable renewables. Second, we assume the optimisation results to represent a set
of plausible futures of the electricity market considered by investors. This allows
us to determine optimal strike prices under uncertainty per CfD type in three bid-
ding zones for two wind power plants each, based on the Equations in Section 2.3.
Third, we calculate ex post CfD payments resulting in each scenario realisation to
study ex post cost recovery and consumer prices.
Step 2
Optimal strike prices for 3 CfD types under
uncertainty according to Eqs. (11) - (13)
Step 1
Investment and dispatch optimisation with
energy system model for4×9 = 36scenarios
Step 3
CfD paymentsP type i,n,s for 3 CfD types for 36 scenarios
according to Eqs. (3) – (7) and ex post analysis
pt,n,s, qt,i,n,s, Qi,n,s
˜Stype i,n
Figure 1: Methodology.
3.1. Invest and dispatch optimisation for ensemble of scenarios
We apply the sector-coupled European electricity market model developed by
Johanndeiter et al. (2025b) to optimise an ensemble of fully decarbonised market
scenarios. The model is implemented in the energy system modelling and optimi-
sation tool Backbone (Helistö et al., 2019) and covers all EU-27 countries except
for Malta, but including Great Britain, Switzerland and Norway, aggregated to 19
bidding zones – all of which are connected by power and H2 transmission lines.
In the following, we will use country and bidding zone interchangeably. Power
supply is dominated by variable renewables (solar PV, wind onshore and offshore,
run of river) and complemented by carbon-free thermal power plants (biomass,
H2, nuclear and waste) and different storage technologies (batteries, H2 caverns,
14

hydro reservoirs with natural inflow and pumped hydro storage). Power demand
represents 2050 projections of conventional electricity demand as well as load from
flexible electric vehicle charging, heat pumps and electrolysers. The latter are built
to supply 2050 industrial H2 demand projections, which can also be covered by im-
ports from outside the EU for a constant price. Detailed data and technology
assumptions are described in Johanndeiter et al. (2025b). Importantly, we con-
sider three wind onshore profiles in each bidding zone that differ in terms of their
capacity factor time series. Existing wind onshore power plants are represented by
the country average. For wind onshore investment options in each bidding zone, a
profile namedHigh FLHincurs higher full load hours (FLH), but a lower market
value (MV) than the second profileHigh MV, such that the latter can be considered
more system-friendly (cf. Johanndeiter et al. (2025a) for details).
We employ a sequential optimisation approach starting with an investment
optimisation of four scenarios, each resulting in a different capacity mix. All sce-
narios share the assumption that the fully decarbonised European energy system
will be dominated by variable renewables and build on 2030 national capacity ex-
pansion targets. Technically, these assumptions imply that all scenarios start from
a brownfield energy system with existing carbon-free electricity generation capaci-
ties that represent 2030 national targets. Additional electricity and H2 generation
capacities are determined by minimising system costs under the consideration of
a European target share of variable renewables (solar, wind and run of river) of
annual electricity demand (including storage losses) of at least 95%, enforced by
a respective constraint. The optimisation is conducted based on sample weeks of
hourly capacity factor and load time series from the weather year 2019, which is
considered average. The four scenarios vary in terms of two variables that affect
the (i) level and (ii) technological composition of capacities. Particularly, we vary
(i) the H2 import price that drives the level of capacities installed in the EU; and
(ii) cost assumptions for solar PV and battery that influence the distribution of
capacities between solar PV and wind power (cf. Table 2).
For our analysis we focus on three bidding zones with different characteristics:
Denmark (DK), Spain (ES) and France (FR). Figure 2 shows capacities resulting
15

from the four investment optimisations: In terms of variable renewable capacities,
Spain is dominated by solar PV, Denmark by wind onshore and France’s capacity
mix is rather balanced between the two technologies. In Spain, variable renewable
generation is complemented by hydro storage, in Denmark by biofuel power plants
and in France by nuclear generators and hydrogen turbines.
Table 2: Overview of varying assumptions for investment scenarios
H2 Price (AC/MWh)
PV cost
(AC/GW)
Battery cost
(AC/GW) 45.07 116.9
308 220 H2Price–PVcost– H2Price+PVcost–
400 290 H2Price–PVcost+ H2Price+PVcost+
Sources: Danish Energy Agency (2023), ENTSO-E (2022), Brändle et al. (2021).
H2Price+PVCost+
H2Price+PVCost-
H2Price-PVCost+
H2Price-PVCost-
0
10
20
30
40
50
60
70
80
H2Price+PVCost+
H2Price+PVCost-
H2Price-PVCost+
H2Price-PVCost-
0
100
200
300
400
H2Price+PVCost+
H2Price+PVCost-
H2Price-PVCost+
H2Price-PVCost-
0
100
200
300
400
500
600 Technology
H2 electrolyser
Waste
Nuclear
H2 Turbine
Biofuel
Run of River
PHS Discharge
Hydro Discharge
Wind Oﬀshore
Batteries Discharge
Wind Onshore High MV
Wind Onshore High FLH
Wind Onshore
Solar
GW
DK ES FR
Figure 2: Electricity and hydrogen generation capacities installed in four investment scenarios in
Denmark (DK), Spain (ES) and France (FR).
Hourly dispatch of the four resulting capacity mixes is optimised for nine full-
year scenarios each. The nine scenarios vary in terms of variables that particularly
affectmarketprices: threealternativeH 2 importpriceassumptions 2 incombination
2Initially we used all three H2 price assumptions for the investment scenarios, but found no
significant difference in capacities between the H2Price+ and H2Price++ scenario.
16

with the weather years 2010, 2015 and 2019 (cf. Tables 3 and 4).
Weather year 2010 is characterised by relatively low renewable capacity factors
and high peak demand, whereas 2015 represents the opposite. To mimic behavior
of myopic market actors, we apply a rolling-horizon approach that sequentially
optimises each day in hourly resolution with the remaining days aggregated at
an increasingly coarse resolution in the forward-looking window. In total, our
approach results in 36 scenario outcomes.
Table 3: Overview of varying assumptions regarding weather years for the dispatch scenarios.
Capacity factors are averaged across Europe.
Weather
year
Average capacity factor (%) Electric load
Offshore Onshore Onshore High FLH Onshore High MV PV Total (TWh) Peak (GW)
2010 35.2 23.2 30.9 26.0 12.7 4286 695
2015 39.1 26.1 34.7 29.6 13.0 4107 644
2019 34.3 25.3 34.4 28.8 13.0 4110 619
Sources: Staffell and Pfenninger (2016), ENTSO-E (2022).
Table 4: Overview of varying assumptions regarding H2 prices for the dispatch scenarios.
H2 price
level
H2 price
(AC/MWh)
H2Price– 45.07
H2Price+ 116.90
H2Price++ 188.73
Sources: ENTSO-E (2022),
Brändle et al. (2021), own as-
sumption.
Figure 3 shows a letter-value-plot (Hofmann et al., 2017) of electricity price
distributions resulting from the nine dispatch scenarios for each invest scenario.
Overall, prices differ more strongly between investment scenarios than between
countries. Across all scenarios, more than 75% of all prices are below 100AC/MWh.
Differences are mainly driven by the H2 import price assumption of the investment
scenario: If it is high, median prices are approximately 35AC/MWh; when it is low,
median prices range between 10 and 25AC/MWh.
Due to our sequential optimisation approach, we observe involuntary load shed-
ding at a maximum price of 4000AC/MWh across all scenarios, particularly those
that represent the weather year 2010. However, the energy crisis of 2022 revealed
17

0 25 50 75 100 125 150 175 200
Price ( /MWh)
H2Price+PVCost+
H2Price+PVCost-
H2Price-PVCost+
H2Price-PVCost-
Bidding zone
FR ES DK
200 400 600
Figure 3: Electricity price distribution for each investment scenario each across 9 dispatch sce-
narios in Denmark (DK), Spain (ES) and France (FR) with prices capped at 617AC/MWh. Lines
represent the median, the largest box spans from the 25% and 75%-quartiles and successively
smaller boxes from 12.5%– to 87.5%-percentiles, from 6.25%- to 93.75%-percentiles and so on.
that such extremely high electricity prices are politically undesired, when revenues
were capped across Europe (Council Regulation 2022/1854, 2022). Therefore, we
cap electricity prices at the value of lost load of the most expensive industrial de-
mand response unit in our model, but also conduct a sensitivity analysis without
the cap (see Appendix A).
3.2. Optimal strike prices under uncertainty
We assume the optimised dispatch results to represent investors’ expectations
on possible market outcomes at the time of the auction for the Contracts for Dif-
ference. Hence, we use the results of all 36 dispatch scenarioss∈Sto determine
optimal strike prices under uncertainty ˜Stype i,n for each CfD type and both wind
power plantsi∈I={High FLH,High MV}in each bidding zonen∈Nbased on
Equations (11), (12) and (13). The distribution of the components used to deter-
mine optimal strike prices are depicted in Figure 4. The cost-based components,
LCOE and costs per capacity, are only affected by volume risk, and thus have
lower volatility than the revenue-based components, market value and revenues
per capacity, which also reflect price risk. As variable costs of wind power plants
18

are low, the cost per capacity even has very little volume risk. The volatility of
revenue-based components is largely driven by weather years. The year 2010 in
particular has significantly higher market values and revenues than the other two
years and also higher volatility. Therefore, we study a sensitivity analysis with-
out the year 2010. The difference in FLH, thus in LCOE, between the High FLH
and High MV profiles is highest in France, followed by Spain and then Denmark.
The difference in the production-based market values follows this trend, but the
difference in revenues per capacity does not – the latter is highest in Denmark.
LCOE
Market Value
DK
LCOE
Market Value
ES
0 50 100 150 200
/MWh
LCOE
Market Value
FR
Profile
High FLH
High MV
Reference
(a) Production-based strike price components lcoei,n,s
andv i,n,s (High FLH, High MV) as well asvn,s (Ref-
erence).
Costs per
capacity
Revenues per
capacity
DK
Costs per
capacity
Revenues per
capacity
ES
0 100 200 300 400 500 600
1000 /MW
Costs per
capacity
Revenues per
capacity
FR
Profile
High FLH
High MV
Reference
(b) Capacity-based strike price components
Ci,n,s/Qi,n,s andr i,n,s (High FLH, High MV) as well
asr n,s (Reference).
Figure 4: Distribution of production-based and capacity-based strike price components across 36
dispatch scenarios for two power plants and the reference power plant in Denmark (DK), Spain
(ES) and France (FR). Lines represent the median, the largest box spans from the 25% and
75%-quartiles and successively smaller boxes from 12.5%– to 87.5%-percentiles, and so on.
As a result, we consider all 36 scenarios to form one optimal strike price for
each wind power plant in all bidding zones and for all three CfD types.
3.3. Ex post analysis of CfD payments, cost recovery and consumer cost
Based on the optimal strike prices, we examine ex post CfD payments, wind
power plants’ cost recovery and consumer prices in each scenario realisation. First,
we calculate each wind onshore power plant’s cost recoveryΨtype i,n,s as the ratio of
19

market revenues and CfD payments to annual costs resulting ex post from each
scenario:
Ψtype i,n,s =
PT
t=1(qt,i,n,spt,n,s) +P type i,n,s
Ci,n,s
.(19)
For instance, for the basic CfD we calculate
Ψbasic i,n,s =
P
t∈T (qt,i,n,spt,n,s) + PT t=1 qt,i,n,s ( ˜Sbasic i,n −p t,n,s)
Ci,n,s
.(20)
As a measure of volatility, we determine the coefficient of variation (Sachs and
Hedderich, 2006, p. 73) of cost recovery for each power plant, bidding zone and
CfD type as
s
1
S
X
s∈S

Ψtype i,n,s − Ψ type i,n 2 Ψ type i,n ,(21)
where Ψ
type
i,n = 1 S P s∈S Ψtype i,n,s is the mean of the cost recovery.
Second, we assess consequences for consumers by analysing average consumer
priceΦ type n,s in bidding zonenas the sum of the volume-weighted electricity price
and a uniform levy that finances CfD payments,
Φtype n,s =
P
t∈T pt,n,s ·d t,n,sP
t∈T dt,n,s
+ Ptype n,sP
t∈T dt,n,s
,(22)
whered t,n,s is the hourly electricity demand in bidding zonenand scenarios. We
also calculate the coefficient of variation of the total consumer prices
s
1
S
X
s∈S

Φtype n,s − Φ type i,n 2 Φ type i,n ,(23)
where Φ
type
i,n = 1 S P s∈S Φtype i,n,s.
20

4. Results and discussion
We first present numerical results for optimal strike prices under uncertainty
for two wind power plants in three bidding zones by CfD type. Then, we analyse
the distribution of the power plants’ cost recovery and consumer prices resulting
ex post across all 36 scenarios.
4.1. Optimal strike prices
Figure 5 depicts optimal strike prices under uncertainty by wind power plant –
as distinguished by generation profile –, bidding zone and CfD type. In line with
the theory in Section 2, strike prices of the basic CfD equal expected LCOE. As
these are lower for the High FLH profile by design in every country, this CfD design
does not incentivise system-friendly design and siting. For the 2way and financial
CfDs, the differences between strike prices and expected costs (per generation or
per capacity) are indicated as markups (if positive) or markdowns (if negative).
The 2way CfD results in markups for the High FLH and markdowns for the High
MV profile in all three countries. Markups and markdowns reflect the difference
in a power plant’s individual market value and the bidding zone’s average, i.e.
the reference price: an above-average market performance allows a power plant to
decrease the strike price below LCOE by a markdown and requires an increase by a
markup in the opposite case. Therefore, the 2way CfD consistently incentivises the
more system-friendly High MV profile with the effect size driven by the difference
in market values. The difference between profiles, both in terms of LCOE and
market value, is lowest in Denmark and highest in France. Here, the markup and
markdown are so high that the optimal strike price of the High FLH profile is above
the optimal strike price of the High MV profile.
By design, the expected cost per capacity, which serves as baseline for the opti-
mal strike price of the financial CfD, is nearly equal for all countries and scenarios
and only differs in terms of total variable costs. Hence, strike prices only differ
in terms of their markups or markdowns. We observe markups for High MV and
markdowns for High FLH profiles, illustrating that the financial CfD does not offer
the same siting and design incentive in favour of the High MV profile as the 2way
21

CfD, because a higher market value, i.e. higher revenues per generation, does not
necessarily imply higher revenues per capacity (cf. Figure 4).
Basic CfD
2way CfD
Basic CfD
2way CfD
Basic CfD
2way CfD
DK ES FR
Financial CfD
Financial CfD
Financial CfD 0
10
20
30
40
50
60
0
20
40
60
80
100
120
High FLH
Markup
Markdown
Costs
Strike Price
High MV
Markup
Markdown
Costs
Strike Price
€/MWh
1000 €/MW
Figure 5: Optimal strike prices under uncertainty for two wind onshore power plants (High FLH,
left bar and High MV, right bar) in Denmark (DK), Spain (ES) and France (FR). Differences
between the strike price and expected costs (expected value of LCOE for basic and 2way CfD,
expected value of total cost per capacity for financial CfD, according to Equations (11) to (13))
is called markup if positive and markdown if negative. Note that strike prices for the financial
CfD are shown on the right y-axis in units of 1000AC/MW.
4.2. Ex post cost recovery
Figure 6 shows ex post cost recovery for three selected scenarios in France. The
scenarios illustrate three characteristic cases: (i) high cost recovery from market
revenues without the CfD, where both wind power plants make significant pay-
mentstothe government for any CfD, (ii) low cost recovery from market revenues,
where all power plants receive varying amounts of payments from the government
for all CfD types, and (iii) cost recovery from market revenues around 100% with-
out a CfD, where payments from or to the government are comparably low and
made depending on CfD type and power plant.
More comprehensively, Figure 7 shows the distribution of ex post recovery for
all three bidding zones across all 36 scenarios. The following key observations can
be made. First, any type of CfD decreases the spread of the cost recovery distribu-
tion significantly compared to a situation, where power plants solely rely on market
revenues (“no CfD”). This holds for the illustrated 25%...75% and 12.5%...87.5%
22

No CfD
Basic CfD
2way CfD
Financial CfD
No CfD
Basic CfD
2way CfD
Financial CfD
No CfD
Basic CfD
2way CfD
Financial CfD
H2Price-PVCost+H2Price+2010 H2Price+PVCost+H2Price-2015 H2Price+PVCost-H2Price+2019
0
20
40
60
80
100
120
140
160
180
High FLH
Payment to government
Payment from government
Market Revenues
High MV
Payment to government
Payment from government
Market Revenues
FR
% of costs
Figure 6: Ex post cost recovery across three selected scenarios in France. Scenario names are
composed of the two determinants of the investment scenario variation followed by the two
determinants of the dispatch scenario variation.
percentiles as well as outliers across all countries. It is also confirmed by the coeffi-
cients of variation (CVs) shown in Figure 8a for all bidding zones with endogenous
investments in both profiles.
Second, when comparing the different CfD types, the basic CfD mostly has a
lower CV than the 2way CfD. Moreover, Figure 7 shows that for the High FLH
profile, the financial CfD achieves the lowest spread of cost recovery for all three
countries considered. However, this neither holds for the High MV profile, nor
for every country individually. And indeed the CV is lowest under the financial
CfD for several power plants, but highest for the others. This can be explained by
the difference in revenues per capacity between the individual power plant and the
reference shown in Figure 8b for 20 power plants and all scenarios. If the difference
is high in some scenarios, like for the High MV profile in ES, Finland (FI) and the
Netherlands (NL), then the variation of cost recovery increases significantly driven
by the revenue side. If the difference in revenues per capacity is low, however, as is
the case for both profiles in Belgium (BE), then costs are the main driver of cost
recovery. And as shown in Figure 4 in Section 3.2, costs vary less when divided by
capacity than when divided by generation (as for the basic and 2way CfDs).
Third, while reducing the volatility of cost recovery, the CfDs do not generally
increase the cost recovery overall. With the exception of the High MV profile in
23

Denmark, the median cost recovery is above 100% without any CfD and decreases
with a CfD in a majority of cases. This result highlights that the purpose of CfDs
in highly renewable electricity markets is to reduce revenue volatility rather than
increasing average revenues.
Basic CfD
2way CfD
Financial CfD
No CfD
DK
Basic CfD
2way CfD
Financial CfD
No CfD
ES
0 50 100 150 200 250 300
Cost Recovery (%)
Basic CfD
2way CfD
Financial CfD
No CfD
FR
Profile
High FLH High MV
Figure 7: Distribution of ex post cost recovery across 36 dispatch scenarios for two wind power
plants in Denmark (DK), Spain (ES) and France (FR). Plot is truncated at 300% excluding 2
observations in FR and 5 in ES.
4.3. Consumer prices
The distribution of the total consumer price and total levies per unit of elec-
tricity in the three bidding zones DK, ES and FR is shown in Figure 9. Figure
10 shows the corresponding coefficients of variation of the consumer price for all
bidding zones. Overall, there are significant variations of average consumer price
and levies between countries. However, there are no significant differences between
CfD types and only a small decrease of the consumer price spread through intro-
duction of any CfD as compared to no CfD. In line with the observation that all
three CfDs do not generally increase the overall cost recovery, the median levy is
24

2way CfD Basic CfD Financial CfD No CfD
BE High FLH
BE High MV
DE High FLH
DE High MV
DK High FLH
DK High MV
ES High FLH
ES High MV
FI High FLH
FI High MV
FR High FLH
FR High MV
GB High FLH
GB High MV
NL High FLH
NL High MV
NO High FLH
NO High MV
PL High FLH
PL High MV
7.9% 8.5% 0.9% 47.3%
8.2% 7.2% 1.8% 46.8%
7.4% 6.4% 18.5% 53.8%
8.2% 5.0% 8.5% 51.2%
8.3% 6.9% 1.8% 59.5%
5.2% 5.9% 6.6% 61.2%
18.7% 8.0% 6.2% 84.0%
10.0% 3.0% 39.4% 67.9%
13.1% 7.6% 8.3% 64.7%
5.9% 8.9% 22.4% 58.2%
20.2% 5.2% 2.4% 53.8%
19.3% 9.3% 18.1% 56.3%
14.7% 11.5% 3.1% 46.7%
10.5% 10.4% 8.9% 46.3%
4.6% 5.3% 7.6% 49.8%
10.5% 7.9% 20.7% 45.7%
7.5% 9.9% 11.6% 92.1%
17.1% 13.7% 9.7% 87.2%
10.2% 3.3% 3.0% 43.3%
6.2% 3.1% 8.4% 40.5%
 0%
10%
20%
30%
40%
50%
60%
70%
Coefficient of variation of cost recovery
(a) Coefficient of variation (CV) of cost recovery by
CfDtypefor20windpowerplantslocatedin10bidding
zones specified by two-digit country codes. The color
code is truncated at 70%
Scenario
BE High FLH
BE High MV
DE High FLH
DE High MV
DK High FLH
DK High MV
ES High FLH
ES High MV
FI High FLH
FI High MV
FR High FLH
FR High MV
GB High FLH
GB High MV
NL High FLH
NL High MV
NO High FLH
NO High MV
PL High FLH
PL High MV
20000
40000
60000
80000
100000
120000
Markup/Markdown ( /MW)
(b) Difference in revenues per capacity between indi-
vidual and reference profile (markup/markdown) for
20 wind power plants located in 10 bidding zones spec-
ified by two-digit country codes.
Figure 8: Cost recovery variation and revenue differences by power plant.
close to zero in all cases. The highest coefficients of variation in Norway, Spain
and Finland can be explained by a higher range of consumer prices due to several
scenarios with very low prices.
Basic CfD
2way CfD
Financial CfD
No CfD
DK
Basic CfD
2way CfD
Financial CfD
No CfD
ES
40
 20
 0 20 40 60 80 100 120 140 160
/MWh
Basic CfD
2way CfD
Financial CfD
No CfD
FR
Component
Consumer Price Levy
Figure 9: Distribution of consumer price composed of electricity price (not depicted) and levy
across 36 dispatch scenarios in Denmark (DK), Spain (ES) and France (FR).
25

2way CfD Basic CfD Financial CfD No CfD
AT
BE
BK
BT
CZ
DE
DK
ES
FI
FR
GB
IE
IT
NL
NO
PL
PT
SE
49.6% 49.6% 49.6% 50.6%
47.8% 47.8% 48.1% 50.2%
48.2% 47.1% 45.2% 51.1%
51.7% 50.2% 45.0% 60.1%
35.8% 35.8% 36.6% 48.4%
46.1% 46.1% 46.4% 47.8%
47.2% 47.6% 48.6% 64.0%
59.5% 59.4% 59.2% 64.4%
55.4% 55.5% 56.1% 61.3%
44.3% 45.9% 46.2% 52.6%
43.1% 43.4% 44.3% 49.2%
39.0% 39.0% 39.7% 62.2%
34.6% 34.9% 34.7% 37.2%
43.9% 43.9% 44.2% 48.7%
78.0% 77.9% 79.2% 91.7%
35.3% 35.8% 36.1% 42.4%
52.5% 52.4% 51.6% 60.4%
64.2% 64.2% 65.5% 84.0%
0%
10%
20%
30%
40%
50%
60%
70%
80%
90%
Coefficient of variation of consumer price
Figure 10: Coefficient of variation of total consumer price by CfD type for all 19 bidding zones
specified by two-digit country codes.
4.4. Sensitivity analysis
To test the robustness of these results, we conduct a sensitivity analysis. We
determine both the cost recovery and consumer prices for two additional cases, (i)
without the cap on extreme prices and (ii) with the weather year 2010 removed
from the set of dispatch scenarios. The results are shown in Appendix A. With-
out the price cap, the volatility and overall level of cost recovery is increased, in
particular in Denmark and France. The same holds for the volatility and level of
consumer prices. Without the year 2010, the volatility and overall level of both
cost recovery and consumer prices are decreased. However, in both cases, our find-
ings on the effect of CfDs in general and the comparison of the three CfD types
remain unchanged.
4.5. Limitations
Our analysis is subject to two main limitations. First, it is important to high-
light that our results only concern the volatility of cost recovery and consumer
prices, and not their level, which would be driven by several factors that we ne-
glect in our analysis. To begin with, we assign an equal weight to each scenario
considered for the calculation of expected values. Hence, our derived strike prices
rely on the assumption that investors are risk-neutral. Strike prices by risk-averse
investors, in turn, would typically reflect the likelihood and volatility of cost recov-
ery by CfD type either by a risk premium (Neuhoff et al., 2022) or by assigning a
higher weight to market scenarios with low profits. In this case, strike prices and
26

therefore, consumer prices, for the 2way CfD are likely to be higher than for the
basic CfDs, if investors are risk-averse. Moreover, auctions for renewable support
schemes have historically not always been competitive. Germany, for instance,
experienced undersubscribed auctions for wind onshore support resulting in av-
erage strike price close to the auction’s price ceiling (Bundesnetzagentur, 2023b).
Conversely, offshore wind auctions were highly competitive, with several investors
submitting bids requiring no financial support (Bundesnetzagentur, 2023a). Lastly,
we do not take into account the reduction in capital costs induced by the reduction
of revenue volatility by all CfD types as documented by previous work (cf. Section
1.2). This reduction would affect investments and lower system costs (Bachner
et al., 2019; Helistö et al., 2019), which in turn would be reflected in lower prices
for consumers. Similarly, we neglect the effect of CfD design on investment and
operational decisions as discussed in Section 1.2. A complete evaluation of CfD
design should take into account a combined assessment of these effects.
Second, we only consider a limited set of scenarios, consequently, a limited set
of risks. Particularly, we focus on a subset of weather and technological risk, rep-
resented by three weather years, varying hydrogen import prices and investment
costs of competing variable renewables. Sanchez Jimenez et al. (2024) and Jo-
hanndeiter et al. (2025b) show that weather variations and the hydrogen import
price are indeed the main drivers of price and volume risk in sector-coupled, highly
renewable electricity markets. Yet, previous work indicates that large-scale energy
system models tend to structurally underestimate price volatility in the day-ahead
market and thus, the underlying price risk that could affect total revenue uncer-
tainty (Terhorst et al., 2025). Further technological uncertainties could arise from
climate change, the degree of electrification in different sectors, total demand as
well as its level of flexibility, or the invention of disruptive technologies. Unlike
weather and short-term price fluctuations, the extent of these uncertainties is itself
uncertain with potentially significant effects on market outcomes. Additionally,
our analysis neglects regulatory uncertainty. Our sensitivity analysis, where we
remove the price cap from market outcomes, reveals that our results on the impact
of CfD design are robust to the introduction of price caps. In a more realistic
27

market setting, such price caps could result from capacity remuneration mecha-
nisms that would additionally affect electricity generation capacities. Therefore,
the interaction of CfDs and capacity remuneration mechanisms should be subject
to further research. Finally, despite their relevance for cost of capital (Lévêque
et al., 2026), we believe that more disruptive regulatory risks, such as a decline in
climate policy ambitions or international cooperation, must not be reflected in a
renewable support scheme and are therefore out of scope of this study.
5. Conclusion
Two-way CfDs can mitigate the price and volume risks of electricity consumers
and investors. In this paper, we studied and compared the risk mitigation effect
of three CfD designs, the production-based basic and 2way CfDs as well as the
capacity-based financial CfD. We started by theoretically deriving optimal strike
price bids under uncertainty for three different CfD types based on investors’ expec-
tations. Then, we assumed a set of highly renewable European electricity market
scenario results from a sector-coupled power system model to represent those ex-
pectations and calculated resulting strike prices and CfD payments. Finally, we
analysed the distribution of investors’ cost recovery for wind turbines and consumer
prices, both including CfD payments, across scenarios and countries.
We find that, first, all three CfD types significantly reduce the volatility of the
profit-to-cost-ratio (cost recovery) compared to full market price exposure. Sec-
ond, consumer price volatility is also reduced by all CfD types, but to a much
lesser extent. Third, we find no significant difference in consumer price volatility
between the three CfD types considered. Fourth, the lowest cost recovery volatil-
ity is achieved by the basic CfD and the financial CfD with a reference power
plant similar to the investor’s one. In contrast, the CfD with highest cost recovery
volatility is the financial CfD with a large difference between the reference price
and the investor’s own market revenues. Existing literature shows that this CfD
design does not cause any dispatch distortions and, to a certain extent, incentivises
system-friendly investments. Overall, our results confirm previous work that de-
signing CfDs is subject to a trade-off between incentivising system-friendliness and
28

Table 5: Comparison of CfD types. The first two rows regarding system-friendly siting and
optimal dispatch are known from the literature, while the last two rows are new insights generated
in this paper.
No CfD Basic CfD 2way CfD Financial CfD
Optimal dispatch + – – +
System-friendly investment + – +◦
Profit volatility – +◦+ /◦
Consumer price volatility –◦ ◦ ◦
reducing risk within a novel framework to assess CfD design under uncertainty.
In conclusion (cf. Table 5), our work suggests that the financial CfD is the
most suitable one to support the energy transition in highly renewable electricity
systems. On the one hand, as already found by other authors, the financial CfD is
the only one among the three CfD types incentivising both optimal dispatch and, to
a certain extent, also system-friendly siting. On the other hand, our novel analysis
of different CfD types under uncertainty shows that, together with the basic CfD,
it also offers the lowest cost recovery volatility for investors, if the reference plant
is similar to the investor’s one. In this case, however, it offers lower incentives
for system-friendly siting. Regarding consumer price volatility, it performs equally
well as the other CfD types considered.
Future work should address the choice of reference profiles for financial CfDs,
which strongly drives profit volatility. For instance, investors may be allowed to
choose the reference plant according to their individual risk preferences. Risk-
averse investors could then use a very similar power plant, while risk-loving in-
vestors could choose the average of their respective bidding zone. A CfD like this
would require a thorough design, e.g. to avoid potential net payments from the
government to investors. Moreover, future work should study interactions with
other regulatory instruments, such as capacity remuneration mechanisms.
CRediT author statement
Silke Johanndeiter: Conceptualization of this study, Methodology, Data cu-
ration, Writing - Original Draft, Visualization, Formal analysis.Jonas Finke:
Methodology, Writing - Original Draft.Justus Heuer: Writing - Original Draft.
29

Acknowledgements
We would like to thank Masooma Fazili for supporting us in data curation.
Declaration of AI-assisted technologies in the writing process
During the preparation of this work the authors used ChatGPT in order to
support data visualisation code and language proofing. After using this tool, the
authors reviewed and edited the content as needed and take full responsibility for
the content of the publication.
Data availability statement
The data and code that support the findings of this study are openly available in
public repositories at https://github.com/TradeRES/TradeRES-Backbone-demo,
https://doi.org/10.5281/zenodo.10829706andhttps://doi.org/10.5281/zenodo.17986036.
30

References
Alonzo, B., Concettini, S., Creti, A., Drobinski, P., Tankov, P., 2022. Profitability
and revenue uncertainty of wind farms in western europe in present and future
climate. Energies 15, 6446. doi:10.3390/en15176446.
Anatolitis, V., Welisch, M., 2017. Putting renewable energy auctions into action
– an agent-based model of onshore wind power auctions in germany. Energy
Policy 110, 394–402. doi:10.1016/j.enpol.2017.08.024.
Andor, M., Voss, A., 2016. Optimal renewable-energy promotion: Capacity sub-
sidies vs. generation subsidies. Resource and Energy Economics 45, 144–158.
doi:10.1016/j.reseneeco.2016.06.002.
Antón, F.S., 2023. The implementation of the windfall profit tax for energy
providers in spain: Its contested compatibility with european and constitutional
law. Intertax 51. URL:https://kluwerlawonline.com/journalarticle/
Intertax/51.11/TAXI2023074.
Bachner, G., Mayer, J., Steininger, K.W., 2019. Costs or benefits? assessing the
economy-wide effects of the electricity sector’s low carbon transition – the role of
capital costs, divergent risk perceptions and premiums. Energy Strategy Reviews
26, 100373. doi:10.1016/j.esr.2019.100373.
Beiter, P., Guillet, J., Jansen, M., Wilson, E., Kitzing, L., 2024. The enduring role
of contracts for difference in risk management and market creation for renew-
ables. Nature Energy 9, 20–26. doi:10.1038/s41560-023-01401-w.
Blazquez, J., Fuentes-Bracamontes, R., Bollino, C.A., Nezamuddin, N., 2018. The
renewable energy policy paradox. Renewable and Sustainable Energy Reviews
82, 1–5. doi:10.1016/j.rser.2017.09.002.
Boomsma, T.K., Linnerud, K., 2015. Market and policy risk under different renew-
able electricity support schemes. Energy 89, 435–448. doi:10.1016/j.energy.
2015.05.114.
Boomsma, T.K., Meade, N., Fleten, S.E., 2012. Renewable energy investments
under different support schemes: A real options approach. European Journal of
Operational Research 220, 225–237. doi:10.1016/j.ejor.2012.01.017.
Brändle, G., Schönfisch, M., Schulte, S., 2021. Estimating long-term global supply
costs for low-carbon hydrogen. Applied Energy 302, 117481. doi:10.1016/j.
apenergy.2021.117481.
Breitschopf, B., Alexander-Haw, A., 2022. Auctions, risk and the wacc. how auc-
tions and other risk factors impact renewable electricity financing costs. Energy
Strategy Reviews 44, 100983. doi:10.1016/j.esr.2022.100983.
Bundesnetzagentur, 2023a. Results of dynamic bidding procedures in offshore wind
power auctions. URL:https://www.bundesnetzagentur.de/SharedDocs/
Pressemitteilungen/EN/2023/20230712_OffshoreResults.html. visited
11.12.2025.
31

Bundesnetzagentur, 2023b. Results of November onshore wind auction. URL:
https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/EN/
2023/20231215_Onshore.html. visited 11.12.2025.
Chaves-Avila, J.P., Banez-Chicharro, F., Ramos, A., 2017. Impact of support
schemes and market rules on renewable electricity generation and system op-
eration: the spanish case. IET Renewable Power Generation 11, 238–244.
doi:10.1049/iet-rpg.2016.0246.
Council Regulation 2022/1854, 2022. Council Regulation (EU) 2022/1854
of 6 October 2022 on an emergency intervention to address high energy
prices. URL:https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=
celex%3A32022R1854.
Danish Energy Agency, 2023. Technology Catalogues [Dataset]. URL:https:
//ens.dk/en/our-services/projections-and-models/technology-data.
De Vos, K., 2015. Negative wholesale electricity prices in the german, french and
belgian day-ahead, intra-day and real-time markets. The Electricity Journal 28,
36–50. doi:10.1016/j.tej.2015.04.001.
Diallo, A., Kitzing, L., 2024. Selection bias in multi-technology auctions: How to
quantify and assess efficiency implications in renewable energy auctions. Energy
Policy 184, 113864. doi:10.1016/j.enpol.2023.113864.
Dimanchev, E., Gabriel, S.A., Reichenberg, L., Korpås, M., 2024. Consequences of
the missing risk market problem for power system emissions. Energy Economics
136, 107639. doi:10.1016/j.eneco.2024.107639.
Directive 2018/2001, . Directive (EU) 2018/2001 of the European Parliament and
of the Council of 11 December 2018 on the promotion of the use of energy from
renewable sources. URL:https://eur-lex.europa.eu/eli/dir/2018/2001/
oj.
Directive 2024/1711, 2024. Directive (EU) 2024/1711 of the European Parliament
and of the Council of 13 June 2024 amending Directives (EU) 2018/2001 and
(EU) 2019/944 as regards improving the Union’s electricity market design (Text
withEEArelevance). URL:https://eur-lex.europa.eu/legal-content/EN/
TXT/?uri=CELEX%3A32024L1711.
EEX, 2025. Power futures. URL:https://www.eex.com/en/markets/power/
power-futures. visited 01.12.2025.
Egli, F., 2020. Renewable energy investment risk: An investigation of changes over
time and the underlying drivers. Energy Policy 140, 111428. doi:10.1016/j.
enpol.2020.111428.
Egli, F., Steffen, B., Schmidt, T., 2020. Cost of capital for renewable energy:
The role of industry experience and future potentials. De Gruyter. pp. 335–347.
doi:10.1515/9783110607888-012.
32

ENTSO-E, 2022. Ten-Year Network Development Plan 2022 Scenarios [Dataset].
URL:https://2022.entsos-tyndp-scenarios.eu/download/.
European Commission, 2018. In-depth analysis in support of the
commission communcation COM(2018) 773. European Commis-
sion. URL:https://climate.ec.europa.eu/document/download/
dc751b7f-6bff-47eb-9535-32181f35607a_en?filename=com_2018_733_
analysis_in_support_en.pdf.
Fabra, N., 2022. Electricity Markets in Transition: A proposal for reforming Eu-
ropean electricity markets. EEL Discussion Paper 115. URL:https://nfabra.
uc3m.es/wp-content/uploads/2022/12/Electricity_Reform-REV.pdf.
Fagiani, R., Barquín, J., Hakvoort, R., 2013. Risk-based assessment of the cost-
efficiency and the effectivity of renewable energy support schemes: Certificate
markets versus feed-in tariffs. Energy Policy 55, 648–661. doi:10.1016/j.enpol.
2012.12.066.
Frey, U.J., Klein, M., Nienhaus, K., Schimeczek, C., 2020. Self-reinforcing elec-
tricity price dynamics under the variable market premium scheme. Energies 13,
5350. doi:10.3390/en13205350.
Frondel, M., Kaeding, M., Sommer, S., 2022. Market premia for renewables in
germany: Theeffectonelectricityprices. EnergyEconomics109, 105874. doi:10.
1016/j.eneco.2022.105874.
Furió, D., Chuliá, H., 2012. Price and volatility dynamics between electricity
and fuel costs: Some evidence for spain. Energy Economics 34, 2058–2065.
doi:10.1016/j.eneco.2012.02.014.
Gohdes, N., Simshauser, P., Wilson, C., 2022. Renewable entry costs, project
finance and the role of revenue quality in australia’s national electricity market.
Energy Economics 114, 106312. doi:10.1016/j.eneco.2022.106312.
Hanley, E.S., Deane, J., Gallachoir, B.O., 2018. The role of hydrogen in low carbon
energy futures–a review of existing perspectives. Renewable and Sustainable
Energy Reviews 82, 3027–3045. doi:10.1016/j.rser.2017.10.034.
Helistö, N., Kiviluoma, J., Ikäheimo, J., Rasku, T., Rinne, E., O’Dwyer, C., Li, R.,
Flynn, D., 2019. Backbone—an adaptable energy systems modelling framework.
Energies 12, 3388. doi:10.3390/en12173388.
Helistö, N., Johanndeiter, S., Kiviluoma, J., 2024. Accelerating wind power invest-
ments through lower financing costs, in: IET. doi:10.1049/icp.2024.3788.
Hiroux, C., Saguan, M., 2010. Large-scale wind power in european electricity
markets: Timeforrevisitingsupportschemesandmarketdesigns? EnergyPolicy
38, 3135–3145. doi:10.1016/j.enpol.2009.07.030. large-scale wind power in
electricity markets with Regular Papers.
33

Hofmann, H., Wickham, H., Kafadar, K., 2017. Letter-value plots: Boxplots for
large data. Journal of Computational and Graphical Statistics 26, 469–477.
doi:10.1080/10618600.2017.1305277.
Huntington, S.C., Rodilla, P., Herrero, I., Batlle, C., 2017. Revisiting support
policies for res-e adulthood: Towards market compatible schemes. Energy Policy
104, 474–483. doi:10.1016/j.enpol.2017.01.006.
Johanndeiter, S., Helistö, N., Bertsch, V., 2025a. Does the difference make a
difference? Evaluating Contracts for Difference design in a fully decarbonised
European electricity market. Resource and Energy Economics 83, 101495.
doi:10.1016/j.reseneeco.2025.101495.
Johanndeiter, S., Helistö, N., Kiviluoma, J., Bertsch, V., 2025b. Price formation
andintersectoraldistributionaleffectsinafullydecarbonisedeuropeanelectricity
market. Advances in Applied Energy 20, 100245. doi:10.1016/j.adapen.2025.
100245.
Kost, C., Müller, P., Sepúlveda Schweiger, J., Fluri, V., Thomsen, J., 2024.
Levelized cost of electricity-renewable energy technologies URL:https:
//www.ise.fraunhofer.de/content/dam/ise/en/documents/publications/
studies/EN2024_ISE_Study_Levelized_Cost_of_Electricity_Renewable_
Energy_Technologies.pdf.
Lévêque, C., Shirizadeh, B., Trüby, J., 2026. De-risking renewable investments:
Internalizing the risks and quantifying the impact of de-risking instruments.
Renewable and Sustainable Energy Reviews 227, 116570. doi:10.1016/j.rser.
2025.116570.
May, N., 2017. The impact of wind power support schemes on technology choices.
Energy Economics 65, 343–354. doi:10.1016/j.eneco.2017.05.017.
Meus, J., De Vits, S., S’heeren, N., Delarue, E., Proost, S., 2021. Renewable elec-
tricity support in perfect markets: Economic incentives under diverse subsidy in-
struments. Energy Economics 94, 105066. doi:10.1016/j.eneco.2020.105066.
Mili, S., Côté, E., 2025. Green on demand? offtaker preferences for corporate
power purchase agreements. Energy Policy 196, 114408. doi:10.1016/j.enpol.
2024.114408.
Neuhoff, K., May, N., Richstein, J., 2022. Financing renewables in the age of falling
technology costs. Resource and Energy Economics 70, 101330. doi:10.1016/j.
reseneeco.2022.101330.
Neuhoff, K., Richstein, J.C., Kröger, M., 2023. Reacting to changing paradigms:
How and why to reform electricity markets. Energy Policy 180, 113691. doi:10.
1016/j.enpol.2023.113691.
Newbery, D., 2023. Efficient renewable electricity support: Designing an incentive-
compatible support scheme. The Energy Journal 44, 1–22. doi:10.5547/
01956574.44.3.dnew.
34

Pahle, M., Schill, W.P., Gambardella, C., Tietjen, O., 2016. Renewable energy
support, negative prices, and real-time pricing. The Energy Journal 37, 147–
170. doi:10.1146/annurev-resource-111820-030145.
RE-Source, 2025. PPA deal tracker. URL:https://resource-platform.eu/
buyers-toolkit2/ppa-deal-tracker/. visited 26.11.2025.
Rosnes, O., 2014. Subsidies for renewable energy in inflexible power markets. Jour-
nal of Regulatory Economics 46, 318–343. doi:10.1007/s11149-014-9258-7.
Ruhnau, O., 2022. How flexible electricity demand stabilizes wind and solar market
values: The case of hydrogen electrolyzers. Applied Energy 307, 118194. doi:10.
1016/j.apenergy.2021.118194.
Sachs, L., Hedderich, J., 2006. Angewandte Statistik: Methodensammlung mit R.
Springer. doi:10.1007/978-3-540-32161-3.
Sanchez Jimenez, I., Ribó-Pérez, D., Cvetkovic, M., Kochems, J., Schimeczek, C.,
de Vries, L., 2024. Can an energy only market enable resource adequacy in
a decarbonized power system? A co-simulation with two agent-based-models.
Applied Energy 360, 122695. doi:10.1016/j.apenergy.2024.122695.
Schittekatte, T., Batlle, C., 2023. Assuring a sustainable decarbonization: Afford-
ability options. IEEE Power and Energy Magazine 21, 72–79. doi:10.1109/mpe.
2023.3269540.
Schlecht, I., Maurer, C., Hirth, L., 2024. Financial contracts for differences: The
problems with conventional cfds in electricity markets and how forward contracts
can help solve them. Energy Policy 186, 113981. doi:10.1016/j.enpol.2024.
113981.
Schmidt, J., Lehecka, G., Gass, V., Schmid, E., 2013. Where the wind blows:
Assessing the effect of fixed and premium based feed-in tariffs on the spatial
diversification of wind turbines. Energy Economics 40, 269–276. doi:10.1016/
j.eneco.2013.07.004.
Soysal, E.R., 2025. Market-based wind power investments under financial frictions.
Applied Energy 391, 125425. doi:10.1016/j.apenergy.2025.125425.
Staffell, I., Pfenninger, S., 2016. Using bias-corrected reanalysis to simulate current
and future wind power output. Energy 114, 1224–1239. doi:10.1016/j.energy.
2016.08.068.
Stuart, A., Ord, K., 2010. Kendall’s advanced theory of statistics, distribution
theory. John Wiley & Sons. doi:10.2307/2982217.
Terhorst, S., Lange, M., Langerhans, L., 2025. (Price-)Volatility in
Electricity Markets – Developing a Fundamental Modelling Approach.
EWI. URL:https://www.ewi.uni-koeln.de/en/publications/
price-volatility-on-the-electricity-market/.
35

Ueckerdt, F., Hirth, L., Luderer, G., Edenhofer, O., 2013. System LCOE: What
are the costs of variable renewables? Energy 63, 61–75. doi:10.1016/j.energy.
2013.10.072.
Ðukan, M., Keles, D., Kitzing, L., 2025. The impact of two-sided contracts for
difference on debt sizing for offshore wind farms. The Energy Journal , 145–
188doi:10.1177/01956574251331.
Veenstra, A.T., Mulder, M., 2024. Impact of Contracts for Differences for non-
carbon electricity generation on efficiency of electricity market. Energy Eco-
nomics 136, 107674. doi:10.1016/j.eneco.2024.107674.
Wagner, F., Jansen, M., Kitzing, L., 2026. How do two-way contracts-for-difference
affect futures markets? A novel modelling approach of futures market liquidity.
Energy Economics 153, 109069. doi:10.1016/j.eneco.2025.109069.
Xiao, M., Junne, T., Haas, J., Klein, M., 2021. Plummeting costs of renewables
- Are energy scenarios lagging? Energy Strategy Reviews 35, 100636. doi:10.
1016/j.esr.2021.100636.
Ziegler, M.S., Trancik, J.E., 2021. Re-examining rates of lithium-ion battery tech-
nology improvement and cost decline. Energy Environ. Sci. 14, 1635–1651.
doi:10.1039/D0EE02681F.
Ðukan, M., Kitzing, L., 2023. A bigger bang for the buck: The impact of risk
reduction on renewable energy support payments in europe. Energy Policy 173,
113395. doi:10.1016/j.enpol.2022.113395.
36

Appendix A. Supplementary Results
Basic CfD
2way CfD
Financial CfD
No CfD
DK
Basic CfD
2way CfD
Financial CfD
No CfD
ES
0 100 200 300 400 500
Cost Recovery (%)
Basic CfD
2way CfD
Financial CfD
No CfD
FR
Profile
High FLH High MV
(a) Distribution of ex post cost recovery across 36 dis-
patch scenarios without a price cap for two wind power
plants in Denmark (DK), Spain (ES) and France (FR).
Plot is truncated at 500% excluding 6 observations in
each bidding zone.
Basic CfD
2way CfD
Financial CfD
No CfD
DK
Basic CfD
2way CfD
Financial CfD
No CfD
ES
100
 50
 0 50 100 150 200 250 300 350 400
/MWh
Basic CfD
2way CfD
Financial CfD
No CfD
FR
Component
Consumer Price Levy
(b) Distribution of consumer price composed of elec-
tricity price (not depicted) and levy across 36 dispatch
scenarios without a price cap in Denmark (DK), Spain
(ES) and France (FR).
Figure A.1: Distribution of cost recovery and consumer prices across 36 scenarios without an
electricity price cap
37

Basic CfD
2way CfD
Financial CfD
No CfD
DK
Basic CfD
2way CfD
Financial CfD
No CfD
ES
0 50 100 150 200
Cost Recovery (%)
Basic CfD
2way CfD
Financial CfD
No CfD
FR
Profile
High FLH High MV
(a) Distribution of ex post cost recovery across 24 dis-
patch scenarios that only consider the weather years
2015 and 2019 for two wind power plants in Denmark
(DK), Spain (ES) and France (FR).
Basic CfD
2way CfD
Financial CfD
No CfD
DK
Basic CfD
2way CfD
Financial CfD
No CfD
ES
10
 0 10 20 30 40 50 60 70
/MWh
Basic CfD
2way CfD
Financial CfD
No CfD
FR
Component
Consumer Price Levy
(b) Distribution of consumer price composed of elec-
tricity price (not depicted) and levy across 24 dispatch
scenarios that only consider the weather years 2015 and
2019 in Denmark (DK), Spain (ES) and France (FR).
Figure A.2: Distribution of cost recovery and consumer prices across 24 scenarios without the
weather year 2010
38
