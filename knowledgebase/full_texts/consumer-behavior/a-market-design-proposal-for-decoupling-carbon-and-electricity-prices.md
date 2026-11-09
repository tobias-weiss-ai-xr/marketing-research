---
title: A Market Design Proposal for Decoupling Carbon and Electricity Prices
url: https://arxiv.org/abs/2603.25874
category: consumer-behavior
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Simon Finster
- Bernhard Kasberger
- Simon Rütten
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.25874
pages: 23
chars: 66326
fetched_at: '2026-11-08T12:59:53+00:00'
kb_version: 1
---

# A Market Design Proposal for Decoupling Carbon and Electricity Prices

A Market Design Proposal for Decoupling Carbon and Electricity
Prices
Simon Finster∗ Bernhard Kasberger† Simon R¨ utten‡
March 30, 2026
Abstract
In European day-ahead electricity markets, carbon allowance costs passed through by
marginal fossil plants raise consumer expenditure and generate inframarginal rents for non-
emitting generators. We propose a settlement modification: when the zonal day-ahead price
exceeds a threshold, non-emitting generation is remunerated at the clearing price minus a
fixed CO2-proxy deduction, while all other units continue to receive the uniform price. The
mechanism thus reallocates a part of the inframarginal rents to consumers. Using hourly
data we estimate static average expenditure reductions of about 8.5% in Austria and 4.7%
in Germany in 2025. We discuss bidding incentives around the threshold, interactions with
Contracts for Difference, implementation in coupled bidding zones, and a gas-cost variant
for the 2022 energy crisis.
1 Introduction
This article proposes a modification to the wholesale electricity market design with the intention
to attenuate the link between CO 2 prices and electricity expenditures. Empirical research indi-
cates that emissions costs are substantially passed through to wholesale prices in auction-based
electricity markets (Fabra and Reguant, 2014). Therefore, we introduce the conditional deduc-
tion of a CO2 price proxythat is applied to the remuneration of inframarginal eligible non-fossil
generators (wind, solar, hydro, nuclear, geothermal, and biomass) during high-price periods.
Concretely, when the day-ahead price exceeds a pre-specified threshold (e.g., 100e/MWh), a
fixed proxy amount (e.g., 28e/MWh) is deducted from the uniform market-clearing price paid
to eligible non-fossil generators. The deduction is intended to approximate the embedded CO 2
cost component in the wholesale price and can be periodically updated to reflect prevailing
allowance prices. To reduce undesirable bidding incentives around the activation point, the
deduction can be phased in over a price interval rather than activated at a single cutoff, thereby
eliminating the payoff discontinuity that would otherwise create incentives for price bunching
near the threshold (see Section 4). The aim is a transfer effect from inframarginal rents of eligi-
ble non-fossil technologies to consumers, while largely preserving marginal dispatch incentives
and the allocative efficiency properties of a uniform-price auction.
∗Department of Economics, Johannes Kepler University Linz; Austrian Institute of Economic Research
(WIFO); Email address: simon.finster@jku.at
†Department of Economics, Johannes Kepler University Linz; Austrian Institute of Economic Research
(WIFO); Email address: bernhard.kasberger@jku.at
‡Austrian Institute of Economic Research (WIFO); Email address: simon.ruetten@wifo.ac.at
Acknowledgments: We thank Gabriel Felbermayr for helpful comments.
1
arXiv:2603.25874v1  [econ.GN]  26 Mar 2026

1 Jan 2019 1 Jan 2021 1 Jan 2023 1 Jan 2025
0
20
40
60
80
100
Carbon price (e/t)
EU
California
China
Figure 1: Carbon prices in major emissions trading systems
Note:Data represents daily allowance prices in the EU ETS, Chinese National ETS, and Californian
Cap-and-Trade Program. Missing values (NAs) are linearly approximated. Data source: International
Carbon Action Partnership.
Carbon prices exist to internalize the negative externality of burning fossil fuels, which
generates CO 2 emissions and adversely affects the climate. A standard efficiency-oriented pol-
icy response is to cap total CO 2 emissions and allocate tradable emission certificates to firms
(Schmalensee and Stavins, 2017). Such a cap-and-trade system induces a market price for emis-
sion allowances. In theory, this price equals the marginal cost of abatement for the last unit
required to meet the cap, and thereby provides decentralized incentives to undertake relatively
low-cost emission reductions first.
The European Union introduced the European Union Emissions Trading System (EU ETS)
for carbon dioxide in 2005. 1 Electricity and heat generators, as well as a broad set of energy-
intensive industrial installations, are required to surrender CO 2 allowances for their emissions.
Figure 1 shows the evolution of allowance prices across three major emission trading systems.
In 2019, the EU ETS allowance price stood at approximately 20e/t CO 2 and has since risen to
about 80e/t by 2025, reflecting the tightening of allowance supply and growing policy ambition.
California’s Cap-and-Trade Program has seen a more moderate increase over the same period,
with prices rising gradually from roughly 15e/t, peaking in 2024 before retreating slightly.
Despite trading at an even lower price level, remaining below 15e/t throughout its existence,
China’s recent national ETS followed a similar trajectory, peaking in 2024, before decreasing
slightly in 2025. The EU ETS has thus emerged as the most stringent and highest-priced carbon
market among the three and CO 2 prices have become an important driver of production costs
in the power sector and other covered industries.
Because gas- and coal-fired power plants must surrender allowances for each ton of CO 2
they emit, the CO 2 price enters their marginal production costs, whereas the marginal costs
of renewable generators remain essentially unaffected. As a result, the allowance price tends
to shift the merit order toward low- and zero-carbon technologies and to raise the wholesale
electricity price in all hours in which fossil plants are marginal. Since gas-fired plants operate
only if their expected revenues exceed fuel, carbon allowance, and operating costs, a higher CO2
price increases the electricity price whenever gas (or coal) units set the clearing price.
On the demand side, the pass-through of carbon prices into electricity prices decreases incen-
tives for substitution to (low-carbon) electric technologies outside the power sector, for example
electric vehicles. If higher CO 2 prices substantially raise wholesale electricity prices, the relative
1Other regions with cap-and-trade systems for CO 2 include California and Quebec, China, the United King-
dom, Switzerland, and South Korea.
2

price of (relatively clean) electricity compared to directly burned fossil fuels (gas, oil, coal) may
change only modestly. In that case, carbon pricing strengthens incentives to switch from coal
to gas or renewableswithinthe power sector, but may provide weak incentives for households
and firms to substitute away from fossil-based end-use technologies. Put differently: the same
policy that decreases the supply-side carbon intensity of electricity can—via wholesale-price
pass-through—dampen demand-side electrification incentives because it raises, in conjunction
with a uniform clearing price across technologies, inframarginal electricity remuneration.
A second concern with carbon prices increasing electricity prices is competitiveness and
carbon leakage. When electricity prices rise, energy-intensive and trade-exposed industries
face stronger pressure to relocate production to jurisdictions with lower energy costs. Such
relocation may leave global emissions largely unchanged—or even increase them if production
shifts to less regulated regions outside the EU ETS—while imposing domestic costs in the form
of lost output, employment, and industrial capability. From a climate perspective, shifting CO2-
intensive production abroad can therefore represent displacement rather than decarbonization.
These concerns are particularly salient in Europe, where energy prices have been persistently
high in international comparison (see Figure 2). While multiple factors contribute to this gap—
including fuel prices, network costs, and taxes—CO2 pricing is a systematic component in hours
when fossil generators set the marginal price.
Figure 2: Industrial retail power prices
Note:Adapted from European Commission (2024), The Draghi Report, Figure 1.
Our market design proposal is motivated by this trade-off. The objective is to reduce the ex-
tent to which CO2 costs translate into inframarginal rents for non-emitting electricity producers
and into electricity expenditures for consumers during high-price periods. By attenuating the
pass-through channel on the revenue side for inframarginal non-emitting technologies—while
preserving the marginal cost signal for fossil plants—the CO 2 proxy deduction has two major
advantages: (1) it strengthens electrification incentives, and (2) it alleviates pressure on indus-
trial competitiveness and consumer budgets; and both are achieved without undermining the
original goal of carbon pricing.
There are academic and recent real-world discussions of the welfare effects of climate policies
in the electricity sector. Academically, Hirth and Ueckerdt (2013) argue that carbon prices
increase producer surplus and decrease consumer surplus (similar to our motivation) and show
that subsidies to renewables can transfer welfare from producers to consumers (via the merit
order effect (Sensfuß et al., 2008)). In the policy domain, the Italian government suggested in
3

early 2026 that consumers pay the fossil power plants’ CO 2 costs, which would reduce their
marginal costs and lower electricity prices (Kazmin et al., 2026). This would lower the non-
emitting producers’ profits and change the merit order in favor of emitting producers. In
contrast, our proposal does not change the merit order in favor of emitting producers while also
lowering consumers’ electricity expenditures.
Section 2 discusses the impact of CO 2-prices on electricity prices. We present the proposed
market design in Section 3 and quantify the impact on electricity expenditure. Section 4 provides
an analysis of how the settlement rule impacts the incentives in the day-ahead auction. We
discuss implementation and institutional details in Section 5. Finally, Section 6 discusses how
a related mechanism could be used for “decoupling” gas and electricity prices during extreme
gas price hikes.
2 The Impact ofCO 2-Prices on Electricity Prices
In this section, we discuss how CO2 prices affect wholesale electricity prices and the distribution
of surplus between producers and consumers. To build intuition, we begin with a stylized single-
period benchmark under perfect competition. We then discuss how intertemporal constraints
(e.g., start-up costs, ramping, storage, block bids) and imperfect competition can alter price
formation and pass-through in practice.
We consider a wholesale electricity market in which prices are determined by several uniform-
price auctions, one for each time period. In each auction, suppliers submit offer schedules (bid
supply curves) and wholesale buyers (retailers and large industrial consumers) submit demand
schedules. The market-clearing price equates aggregate supply and demand in the respective
period, and all accepted quantities are settled at this uniform price. Across periods, bids
and operational decisions may be independent or linked through intertemporal constraints and
bidding formats. For example, the European day-ahead market determines electricity prices for
each 15-minute interval of the following day. The auction allows “block bids” that link intervals,
introducing non-convexities that we ignore in the single-period benchmark.
A relevant concept is thepass-throughof CO 2 costs into wholesale electricity prices. Pass-
through describes how much of a change in marginal emissions costs faced by fossil generators is
reflected in the market-clearing electricity price. Formally, lettingp t denote the wholesale price
and lettingm t denote the per-MWh emissions-cost component of the marginal technology in
periodt, the pass-through rate can be defined as∂p t/∂mt. A pass-through of one means that
a one-euro increase in marginal emissions cost raises the wholesale price by one euro whenever
a fossil unit is marginal. A pass-through below one means that prices rise by less than the
cost increase. A pass-through above one means that prices rise by more than the increase in
marginal emissions cost, so that the price response amplifies the underlying cost shock. Since
marginal pricing applies the market-clearing price to all accepted output, the degree of pass-
through determines both the expenditure impact on consumers and the extent to which higher
CO2 prices translate into inframarginal rents for non-emitting generators.
To illustrate the price impact of CO 2 prices in a simple setting, we assume perfect com-
petition and a single-period market (no intertemporal linkages in bidding), so that bids equal
marginal costs and the supply curve coincides with the merit order. Figure 3 then illustrates
supply and demand in the electricity market. Without a CO2 price, the market clears at pricep 0
and quantityq 0 (pointE 0). Introducing a CO 2 price raises the marginal costs of fossil-fired
plants but leaves those of renewable generators unchanged, shifting the fossil supply curve up-
ward. In this benchmark, the pass-through of marginal emissions costs is one whenever a fossil
unit is price-setting. Whenever a fossil-fired plant is marginal (as depicted), the new equilibrium
features a higher pricep 1 > p0 and lower quantityq 1 < q0, reflecting both the cost increase
for carbon-intensive technologies and the demand response to higher prices. Because all in-
framarginal generators receive the higher clearing price, the producer surplus of non-emitting
4

Quantityq
Pricep
Demand
Supply with a CO 2 price
E0
q0
p0
E1
q1
p1
Marginal costs of renewable generators
Marginal costs of fossil fuel power plants
Figure 3: Equilibrium effect with CO 2-prices
Note:The CO 2-price increases the marginal costs of fossil fuel power plants. Supply curves respond
to an increase in marginal costs. In the new equilibrium, the price is higher and demand lower when
fossil fuel power plants are active.
technologies rises, redistributing welfare from consumers to producers in high-price periods (see
also, e.g., Sijm et al. (2006) and Hirth and Ueckerdt (2013)).
Intertemporal linkages can weaken the one-period merit-order logic. In hours in which
no emitting unit is marginal, an increase in the CO 2 price does not mechanically raise the
marginal cost of the price-setting technology, and the direct pass-through channel is therefore
absent. However, electricity supply is not fully separable across hours. Many thermal plants
face non-convex operating constraints—such as start-up costs, minimum stable generation levels,
and ramping limits—and market designs allow intertemporal bids (e.g., block bids) that link
acceptance decisions across periods. In such settings, a plant may be committed in low-price
hours as part of an intertemporal schedule even when the day-ahead price in those hours is
below its short-run marginal cost. Losses incurred in these hours must then be recovered in
other hours of operation in order for the plant (or the linked bid) to break even. An increase in
the CO 2 price raises the variable cost of emitting units in all hours in which they operate and
can therefore increase the required scarcity rents in the hours that finance these commitments.
As a result, CO2 price changes can affect electricity prices even in hours in which emitting units
are not marginal, and price responses can be amplified in peak hours if these hours are the
margin on which intertemporal recovery takes place. These intertemporal linkages imply that
the response of peak-hour prices to changes in CO 2 costs need not be one-for-one and can, in
principle, exceed the contemporaneous increase in marginal emissions costs (pass-through above
one).
Intertemporal effects can also operate across bidding zones through market coupling. For
example, even if no domestic coal plant is running, interconnector flows may transmit scarcity
conditions and cost shocks from neighboring zones; when imports are marginal, foreign units
subject to higher CO 2 costs can influence domestic prices.
Imperfect competition can also modify cost pass-through because bids need not equal
marginal costs. In a day-ahead auction, the market-clearing price can be decomposed as the
marginal cost of the price-setting unit plus a markup that reflects the competitiveness of resid-
ual demand. When marginal costs increase (e.g., through higher CO 2 prices), the equilibrium
markup may adjust: markups can fall if competition intensifies at higher cost levels or if de-
mand becomes more elastic, implying pass-through below one. In that case, part of the cost
increase is absorbed by producers through lower margins rather than being fully transmitted
5

to consumers. More generally, the pass-through rate depends on market structure, demand
elasticity, and the curvature of supply and residual demand (Sijm et al., 2012).
The extent to which carbon allowance costs are passed through to wholesale prices is there-
fore central for consumer expenditure and the distribution of surplus in electricity markets.
Empirical evidence indicates that the pass-through of CO2 costs into wholesale electricity prices
in European markets is high. Fabra and Reguant (2014) study the Spanish day-ahead market
during the first phase of the EU ETS using plant-level bid data and an instrumental-variables
strategy.2 They find that a one euro increase in emissions costs raises wholesale prices by more
than eighty cents on average, with pass-through close to one during peak hours when dynamic
constraints are less binding. Their structural analysis shows that generators fully internalize the
opportunity cost of permits, and that the high pass-through reflects the combination of highly
inelastic short-run demand, correlated cost shocks across firms, and limited price rigidities in
the auction format. Changes in the CO 2 price therefore feed almost one-for-one into wholesale
electricity prices, with direct consequences for the distribution of rents between carbon-intensive
and low-carbon technologies. Hintermann (2016) documents similarly high pass-through rates
for Germany.
Finally, a back-of-the-envelope calculation illustrates the magnitude of the cost increases.
Letηdenote the thermal efficiency of a fossil plant,p fuel the fuel price per MWh th, ande fuel
the emission intensity per MWh th of fuel burned. The marginal cost of electricity production
is then approximately
MC≈ 1 η  pfuel +e fuel pCO2  ,(1)
wherep CO2 is the allowance price per ton. The terme fuel pCO2/ηcaptures the CO 2 cost per
MWh of electricity; its share in total marginal cost rises with both the emission intensity and
the allowance price.
For a combined-cycle gas plant withη= 0.55 ande fuel = 0.2 tCO 2/MWhth, the implied
emission intensity is approximately 0.36 tCO2/MWhel. At a gas price ofe30/MWh and a CO 2
price ofe80/t, Equation (1) yields a marginal cost of roughlye84/MWh, of which about one
third is attributable to CO 2 costs. Doubling the allowance price raises the marginal cost to
approximatelye113/MWh, with CO 2 costs accounting for more than half.
For a lignite plant withη= 0.40 ande fuel = 0.4 tCO 2/MWhth, the emission intensity is
1.0 tCO2/MWhel—nearly three times that of gas. At a lignite price ofe10/MWh th and a CO2
price ofe80/t, the implied marginal cost is aboute105/MWh, of which roughly three quarters
are CO 2 costs. Doubling the allowance price would raise marginal costs to approximately
e185/MWh, making CO 2 the dominant cost component.
3 Market Design Proposal
This section proposes a mechanism that reduces the extent to which carbon costs translate into
electricity expenditures during high-price periods.
3.1 The Mechanism
The key idea is a simple settlement rule in the electricity wholesale market: a conditional CO 2
proxy deductionis applied only to the remuneration of eligible non-fossil generators (wind, solar,
hydro, nuclear, geothermal, and biomass) in hours in which the uniform day-ahead price is high.
2Fabra and Reguant (2014) use detailed plant-level bid data for the Spanish wholesale market from 2004–
2006, instrumenting marginal emissions costs with the allowance price. They estimate both reduced-form and
structural models of bidding behavior.
6

Cost/Price
(EUR / MWh)
Quantity (MWh)
28 EUR/MWh
100 EUR/MWh
pt
qt
W elfare redistributionA
B
C
Demand
Figure 4: Conditional CO 2 proxy deduction in high-price hours
Note:The figure illustrates a settlement rule under which eligible non-fossil generators receiveep=p−δ
whenever the uniform day-ahead pricepexceeds a threshold (e.g., 100e/MWh). The deducted
amountδproxies embedded CO 2 costs and is rebated to consumers. Under uniform marginal pric-
ing (without the deduction), all inframarginal generators receivep t; eligible producer surplus would
correspond to areasA+B, and fossil producer surplus to areaC. Under the proposed settlement
rule, areaAis transferred from eligible producer surplus to consumer surplus. The blue area (B)
represents the remaining producer surplus of eligible generators, the red area (C) is the producer
surplus of fossil-based plants, and the green area (A) is the welfare gain of consumers and welfare loss
of eligible generators.
Letp t denote the uniform day-ahead market-clearing price in periodt. Fix a price threshold
p(e.g., 100e/MWh) and a proxy amountδ t ≥0 (e.g., 28e/MWh). Eligible non-fossil gener-
ators (wind, solar, hydro, nuclear, geothermal, and biomass) receive an adjusted remuneration
ept =p t −1{p t ≥ p}δ t,
while all other generators continue to receive the uniform pricep t. For example, ifp t =
158e/MWh, p= 100e/MWh, andδ t = 28e/MWh, eligible generators receiveep t =
130e/MWh. Letq t denote total demand andq r t the production of eligible generators. To-
tal electricity expenditure in periodtis then
Expt =q r t ept + (qt −q r t )pt.(2)
A wholesale consumer with demandD t incurs the paymentD t ·Exp t/qt.
Figure 4 illustrates the mechanism in a period wherep t ≥ pand a fossil unit is marginal.
The mechanism implements a conditional redistribution of inframarginal rents from eligible non-
fossil generators to consumers without altering the market-clearing price or dispatch outcome,
while leaving fossil producer surplus unchanged (see figure for details).
The mechanism is not a revenue cap. Unlike a ceiling that limits total remuneration, the
proxy deduction leaves eligible generators fully exposed to marginal price movements. Formally,
∂ept/∂pt = 1 forp t ≥ p: revenue increases one-for-one with the wholesale price above the
threshold. The mechanism therefore preserves scarcity signals and high-price exposure while
redistributing a fixed component of inframarginal rents.
7

3.2 Parameter Design
The threshold pshould be set above the marginal cost of fossil generation excluding carbon
costs (e.g., fuel and operating costs of gas plants). This ensures that the deduction activates
primarily in hours when fossil plants are marginal and carbon allowance costs drive the high
wholesale price. If the threshold were set too low, the mechanism would redistribute rents even
in hours when CO 2 costs do not materially affect prices, weakening its economic rationale.
The proxy amountδ t should reflect the carbon cost component embedded in the marginal
fossil technology. A transparent specification ties the proxy directly to the CO2 cost of electricity
from an efficient gas (or coal) plant:
δt =α·e gas,el ·p CO2,t,(3)
wheree gas,el denotes the reference emissions intensity (tCO 2/MWhel) andα∈[0,1] governs
the degree of redistribution. Settingα= 1 implements full deduction of the estimated carbon
cost component, whileα <1 (e.g.,α= 0.8) leaves a fraction of the carbon rent with eligible
generators as an implicit subsidy. The specification automatically adjusts the deduction from
eligible units to the up-to-date carbon allowance prices. The proxy amountδ t might or might
not be dependent on timet.
To avoid unintended distortions, parameters should satisfy
p−δ t >max i celigible i ,(4)
wherec eligible i denotes the marginal cost of eligible technologies. Otherwise, some eligible tech-
nologies could become temporarily unprofitable despite being cost-efficient, which would create
allocative inefficiencies in the merit order. Storage is a special case: its opportunity cost reflects
past charging prices, so the deduction can mechanically compress storage margins in high-price
hours. Policymakers should therefore decide explicitly whether storage should be eligible and,
if so, calibrate pandδ t accordingly.
To eliminate the payoff discontinuity atp—which, as we show in Section 4, creates incentives
for price bunching—the deduction schedule can be smoothed. Letp < pand let the deduc-
tion scheduled(p t) increase linearly between these two prices. The remuneration to eligible
generators is then
ept =p t −d(p t),
where
d(pt) =



0, p t ≤p ,
δt
pt −p
p−p , p < pt < p,
δt, p t ≥ p
(5)
whereδ t is given by Equation (3). Under the linear ramp, the deduction increases continuously
from zero toδ. As a result, a marginal reduction in the clearing price no longer produces a
discrete jump in eligible-generator profit; instead, the lower deduction and the lower price trade
off smoothly, eliminating the region in which small supply shifts generate discontinuously large
profit gains. We argue in Section 4.5 that this removes the threshold-bunching incentive. Other
functional forms (e.g., concave phase-ins) can be used in place of a linear ramp.
3.3 Quantification
To assess the magnitude of the proposed CO 2 proxy deduction, we conduct a static accounting
exercise using hourly data on day-ahead prices, load, and generation by technology. The ob-
jective is to quantify the mechanical redistribution implied by our settlement rule, abstracting
from behavioral responses in demand, bidding, dispatch, or investment.
8

We construct an hourly panel each for the German and the Austrian price zone, respectively,
by merging day-ahead prices with realized load and generation data; the data source is ENTSO-
E. Eligible non-fossil generation is defined as wind (onshore and offshore), solar, hydro (run-
of-river and reservoir), nuclear, geothermal, and biomass; pumped storage is excluded in the
baseline quantification to guarantee that the inequality in (4) holds for all eligible technologies.
Letp t denote the observed day-ahead price in hourt,L t the realized load, andR t the eligible
non-fossil generation. Status quo electricity expenditure in hourtis given by
Expbase t =p t ·L t.
Under the proposed mechanism, a transfer is triggered whenever the price exceeds the threshold
p= 100e/MWh. For each such hour, the redistributed amount is
Tt =1{p t ≥ p} ·δ·Rt,(6)
whereδis the proxy deduction and equal to 28e/MWh. 3 The counterfactual electricity ex-
penditure faced by consumers is then
Expnew t = Expbase t −T t.
Aggregating across hours yields annual baseline expenditure and the counterfactual expenditure
together with total redistributed inframarginal rents. Average electricity expenditure per MWh
before and after the reform is computed by dividing total expenditure by total load. Importantly,
quantities (Lt andR t) and prices (p t) are held fixed throughout this exercise. The calculation
therefore captures only the direct redistribution effect of our settlement rule, not any induced
changes in dispatch, bidding strategies, demand, or investment behavior.
This static approach provides a transparent benchmark for the immediate mechanical redis-
tribution under fixed market outcomes. In reality, lower effective consumer prices in high-price
hours may stimulate demand, while reduced inframarginal rents could affect long-run investment
incentives. These dynamic responses are intentionally left out in order to isolate the immediate
expenditure channel targeted by the proposal. Our analysis in Section 4 suggests that bidders
may have an incentive to alter their bidding functions in some time periods.
Applying the settlement rule to hourly data for 2025 yields economically meaningful redis-
tribution magnitudes. In Austria, the total annual load amounts to 59.2 TWh and baseline
electricity expenditure sums to approximately 6.18 billione. The proposed proxy deduction
would redistribute about 528 millionefrom inframarginal eligible non-fossil generation to con-
sumers. Under the maintained assumption of fixed quantities and prices, average electricity
expenditure falls from 104.4e/MWh to 95.5e/MWh, corresponding to a reduction of roughly
8.9e/MWh, or about 8.5%.
For Germany, with an annual load of 466 TWh and baseline expenditure of about 43.2 bil-
lione, the implied redistribution amounts to approximately 2.04 billione. The average ex-
penditure decreases from 92.8e/MWh to 88.4e/MWh, a reduction of around 4.4e/MWh, or
approximately 4.7%.
Figure 5 decomposes the total redistribution implied by the proxy deduction across eligible
non-fossil technologies for Austria and Germany. In Austria, the transfer is dominated by
hydropower, reflecting the large share of run-of-river generation in high-price hours: run-of-
river hydro accounts for about 61% of the redistributed amount, followed by onshore wind (21%)
and reservoir hydro (11%) while solar contributes around 6%. In Germany, the redistribution
is more diversified and driven primarily by wind: onshore wind represents the largest share
(43%), followed by biomass (21%), solar (15%), offshore wind (12%), run-of-river hydro (7%)
and reservoir hydro (1%). These patterns mirror the technology mix available in high-price
3Table 2 reports outcomes for alternative parameter values, and Table 3 for a specification with a linear ramp.
9

Figure 5: Redistributed expenditures by technology, Austria and Germany (2025).
Note:The bars decompose the total redistribution implied by the proxy-deduction mechanism across
eligible non-fossil technologies in Austria (AT) and Germany (DE). Heights are in million euros; labels
within segments report each technology’s share of the total redistribution in the respective country.
Results are aggregated over all hours in 2025 using day-ahead prices and realized generation by
technology. Note the different y-axis scales across panels. Technologies with less than 1% contribution
are left out for readability.
10

hours and illustrate that the incidence of the mechanism across producers is system-specific.
Table 1 shows the implied revenue losses by technology and zone resulting from the policy-
induced redistribution in expenditure.
Aggregating transfers by four-hour blocks reveals that the redistribution is concentrated
in peak hours. In both Austria and Germany, the largest reductions in average electricity
expenditure occur during late afternoon and early evening (4–7pm), when fossil generation is
frequently marginal and wholesale prices highest (Figure 6). In Austria, the average expenditure
reduction in this block reaches 11.4%, compared to around 6% in Germany. Morning peak hours
(4–7am) also show above-average reductions, while nighttime hours are largely unaffected.
Figure 6: Electricity expenditure and redistribution by four-hour blocks for Austria (left) and
Germany (right), 2025.
Note:Blue bars show net consumer expenditure; red bars show the redistributed amount under the
proposed proxy deduction. Note the differenty-axis scales for readability.
This pattern is by design: the deduction activates when fossil units set the marginal price,
concentrating the redistribution in peak-load periods rather than compressing the entire whole-
sale price distribution.
The average reduction in consumer expenditure per MWh implied by Equation (6) is
δ·
P
t:p t≥p Rt P
t Lt
,
i.e., the proxy amount scaled by the share of eligible non-fossil generation in high-price hours
relative to total load. This identity explains the cross-country differences: Austria exhibits
a larger proportional reduction because a comparatively large volume of hydro generation is
available in high-price hours—its renewable share exceeds Germany’s by 18.3 percentage points
in the 4–7pm block and by 16.1 percentage points in the 4–7am hours. In Germany, high-price
periods coincide with lower renewable availability, and the larger load base further dilutes the
per-MWh transfer.
4 Incentives
The proposed mechanism creates a payoff discontinuity at the price threshold p: when the
market-clearing price lies above the threshold, non-emitting generators receive a reduced remu-
neration, but when it falls below, they retain the full market price. This discontinuity generates
11

distinctive incentives for bidding in the day-ahead auction. We begin with the economic intu-
ition illustrated by Figure 7, then formalize the underlying incentives, and distinguish general
market incentives from strategic portfolio behavior.
0 100 200 300 400 500 600 700 800 900
Quantity q
10
30
50
70
90
110
130
150Price p
E0
q0
p0
E1
q1
p1
A
B
Carbon tax equivalent
at CO2 price of 28
Demand
Renewables
Renewables (expanded)
Fossils with CO2 price
Fossils (shifted)
Tax threshold (p = 100)
Figure 7: Incentives of renewables to expand demand around the threshold price.
4.1 Threshold Incentives
Figure 7 illustrates the threshold incentive. In the initial equilibriumE 0, the market clears at
pricep 0 slightly above p. The proxy deduction applies, so renewable generators receivep 0 −δ
per unit, earning profit equal to area A.
Now suppose aggregate supply shifts rightward to equilibriumE1, where the clearing pricep 1
falls below p. Although the price is lower, the deduction no longer applies: renewable generators
receive the full pricep 1 on all output. Their profit inE 1—area A+B—strictly exceeds their
profit inE 0, despite the lower clearing price. As a result, the load-weighted average price paid
to renewables may be higher inE 1 than inE 0.
When the clearing price lies slightly above the threshold, even a modest increase in supply
can yield a discrete profit gain: the removal of the proxy deduction—which applies to all
renewable output—more than compensates for the revenue lost from a lower price. This creates
a region in which the marginal value of additional supply is discontinuously large.
4.2 Formal Characterization
To formalize this incentive, consider a market with downward-sloping aggregate demandD(p)
and supply from two types of generators: non-emitting generators with total outputq r, and
12

fossil generators whose costs include emission allowance prices.
Whenp t ≥ p, the proxy deduction applies and non-emitting profit is
Πr high = (pt −δ t)q r.
Whenp t < p, no deduction applies and non-emitting profit is
Πr low =p t qr.
The profit function is therefore discontinuous atp t = p. A price reduction from p+εto p−ε
changes non-emitting profit by approximately
∆Πr ≈(δ t −2ε)q r,
which is strictly positive for smallεwheneverδ t >0. The discrete gain from removing the
deduction—equal toδ t qr—dominates the continuous loss from the price reduction 2ε qr. Near
the threshold, even small shifts in supply generate discrete profit gains, creating strong incentives
to push the equilibrium price below p.
4.3 General Market Incentives
The threshold discontinuity creates incentives that may operate even without strategic behavior
or market power, through three channels. Overall, we may observe bunching of electricity prices
just below the threshold.
First,supply expansion: (owners of) non-emitting generators face strengthened incentives
to expand output or capacity, shifting the aggregate supply curve rightward. If this moves the
equilibrium price below p, all non-emitting output avoids the deduction.
Second,bid shading: lowering bids from above to below the threshold pmay be profitable
when these bids push the market-clearing price below p. This might mean that profit margins
of emitting generators are smaller.
Third,demand-side contraction: consumers and storage operators facing the threshold dis-
continuity may have an incentive to curtail demand in hours when the clearing price lies slightly
above the threshold. For example, a storage unit that would otherwise charge during such an
hour may find it profitable to defer consumption if doing so helps push the market-clearing price
below the threshold, thereby lowering the load-weighted average price it faces. This short-run
demand response channel reinforces the supply-side incentives discussed above.
Strategic considerations arise particularly for firms with mixed renewable and fossil port-
folios, which can internalize the tradeoff between lower fossil margins and avoided deductions
on renewable output. Consider a firm producingRunits with non-emitting generators andF
units with emitting. Suppose the market clears atp ∗ > pabsent any strategic adjustment. If
the firm can push the clearing price below p, renewable revenue rises from (p ∗ −δ)Rto p R.
Let ∆p=p ∗ − p >0. The gain from avoiding the deduction is (δ−∆p)R. However, lowering
the price also reduces inframarginal revenue on the firm’s fossil output. The total profit change
is approximately
∆Πi ≈(δ−∆p)R| {z }
net renewable gain
−∆p·F| {z }
lost fossil revenue
.
Decreasing the pricep ∗ below the threshold pis profitable only if ∆Π i >0, that is, when
∆p < δ· R R+F .(7)
The incentive is increasing in the renewable portfolio shareR/(R+F): firms with large renew-
able and small fossil positions gain most from crossing the threshold. Note that the marginal
13

cost of fossil plants does not enter Equation (7): it may even be attractive to bid below marginal
cost on emitting units to gain on non-emitting output.
When no single firm has sufficient price influence, threshold manipulation is unlikely. When
residual demand is steep and firms hold large mixed portfolios, bunching of prices just below p
may occur. As we show in Section 4.5, this bunching incentive can be eliminated by phasing
in the deduction linearly over an interval [p , p] as described in Section 3.2. Alternatively, the
regulator could randomize the threshold, reducing the predictability of the cutoff and thereby
the attractiveness of bunching strategies. Note that bunching, even if it distorts the price
distribution around p, still lowers the clearing price relative to the status quo. However, it
may increase electricity expenditures relative to the counterfactual without strategic responses,
since prices cluster just below rather than above the threshold where the deduction would have
applied.
4.4 Dispatch Efficiency within Regimes
Away from the threshold, the mechanism preserves dispatch incentives. The deduction is a
post-clearing settlement adjustment that does not enter the auction algorithm (apart from the
pricing stage). Whenp t ≪ p, the policy is ineffective and the dispatch incentives are therefore
as withδ t = 0. Whenp t ≫ p, each additional unit of renewable output earnsp t −δ t, still
well above near-zero marginal cost; fossil generators continue to earnp t −c i. Neither the cost
ranking nor the marginal return to output changes, so dispatch order is preserved within each
regime.
Near the threshold, this no longer holds. As shown above, firms may find it profitable to bid
emitting units below marginal cost to push the clearing price below pand avoid the deduction
on non-emitting output. The threshold thus introduces bid distortions in a neighborhood of p.
While distortions may be profitable for a portfolio bidder, they still decrease the clearing price.
Around the threshold price, extreme bunching incentives can be smoothed out as we discuss in
the next section.
4.5 Incentives under the Linear Ramp
The bunching incentives analyzed above arise from the payoff discontinuity at a single thresh-
old p. Under the linear phase-in scheduled(p t) defined in Section 3.2, the deduction increases
continuously over the interval [p, p], and the discontinuity is eliminated.
Within the ramp, the remuneration of non-emitting generators is
ept =p t −δ pt −p p−p ,
so the marginal remuneration with respect to the clearing price is
∂ept
∂pt
= 1− δ p−p .
This derivative is constant throughout the phase-in interval and non-negative wheneverδ≤
p−p . In particular, the profit function of non-emitting generators is continuous everywhere:
there is no price at which a small supply shift produces a discrete profit gain. The strategic
manipulation condition (7)—which requires a discrete gainδ·Rfrom crossing a threshold—
therefore ceases to apply.
Intuitively, under the ramp a marginal reduction in the clearing price simultaneously lowers
the deduction and the price. These two effects offset each other smoothly, so that there is no
region in which pushing the price downward is discontinuously profitable. The three channels
identified in Section 4—supply expansion, bid shading, and demand-side contraction—no longer
produce bunching because no single price point serves as a discrete trigger.
14

60 p 120
60
70
80
90
100
110
p
p−δ(p)
δ= 0
δ= 16
δ= 20
δ= 28
(a) Threshold at 100
60 p p 120
60
70
80
90
100
110
p
δ= 0
δ= 16
δ= 20
δ= 28
(b) Linear ramp fromp = 80 to p= 100
Figure 8: Remuneration of non-emitting generators under a threshold and a linear ramp deduc-
tion
The phase-in interval should satisfy p−p > δ. Ifδ > p−p , the marginal remuneration
becomes negative and non-emitting generators would prefer lower clearing prices within the
ramp, creating bunching incentives that are similar (but attenuated) compared to the discrete
threshold case. At the boundaryδ= p−p , the remuneration is flat across the phase-in interval:
generators are indifferent to price movements within the ramp. Figure 8 illustrates the muted
bunching incentives, for different carbon deductionsδ. Note that bunching incentives are most
attenuated whenδ < p−p .
5 Discussion
Several practical objections arise when translating the proposed mechanism from a stylized
market model to real-world wholesale electricity markets. We address three issues: institutional
implementation (including the identification of generation technologies in order books), the
interaction with long-term incentives for renewables, and cross-border price formation in coupled
bidding zones.
5.1 Institutional Implementation
The mechanism admits two equivalent implementations: (i) as an alternative auction design
in the day-ahead market, or (ii) a technology-specific levy imposed outside the market with
revenue recycled to consumers.
Auction implementation.The design of the day-ahead auction can be changed to implement
the mechanism. Under the new auction design, the auctioneer determines the market-clearing
pricep t as in a standard uniform-price auction. Eligible non-fossil generators receive the carbon
cost-adjusted priceep t, while all other generators receive the market-clearing pricep t in the
day-ahead auction. Consumers pay total expenditure as defined in Equation (2). The wedge
betweenp t andept is thus embedded directly in wholesale settlement.
Our binary pricing rule requires identifying which cleared volume comes from eligible non-
fossil generation. This is impossible in current European day-ahead auctions: order books
contain price–quantity bids, but not unit identity or fuel type at the bidding stage. In addi-
tion, many markets—including Austria—use portfolio bidding, so a single bid (function) can
aggregate multiple technologies. Cleared bids are therefore not mapped one-to-one to generat-
15

ing units ex ante. This is a technical implementation issue rather than a conceptual problem.
To implement the settlement rule in the day-ahead market, bidders must reveal the share of
eligible production associated with each price–quantity pair. A practical solution is to adopt
unit-based bidding (used, e.g., in Spain and Portugal) instead of the portfolio bidding used in
most European countries.
Implementation as a levy.Alternatively, the wholesale market is not changed so that all gen-
erators receive the uniform market-clearing pricep t in the auction. However, eligible generator
isupplyingq it in periodtpays a levy ofδ tqit wheneverp t ≥ p. The collected revenue is rebated
to consumers, for example via network charge reductions or lower electricity taxes. The levy
reduces total consumer expenditure by exactly the same amount as the two-price settlement
rule, so economic incidence is identical. The difference is purely administrative: the levy leaves
wholesale settlement formally unchanged and may be easier to align with existing regulatory
and tax infrastructure.
Compared with windfall taxes such as the Austrian Energiekrisenbeitrag–Strom (EKB-S,
Republik ¨Osterreich, 2022), the key difference is the treatment of marginal incentives above
the trigger price. EKB-S applies a high tax rateτto the revenues of electricity generators
excluding gas and pump-storage above a statutory benchmark ˆp(e.g., activation aroundp t ≥
ˆp).4 While the law aggregates over monthly revenue, an hourly stylization leads to a marginal
profit of ˆp+ (1−τ)(pt −ˆp). For sufficiently highτ, this can weaken renewable output incentives
relative to exempt emitting generation. The CO 2 proxy deduction instead subtracts a fixed
amount in high-price hours: it shifts revenue levels but preserves the full marginal increase
inp t, maintaining scarcity-price exposure while still transferring the allowance-cost component
embedded in wholesale prices to consumers.
Two further differences are worth emphasizing. First, the proxy deduction is a transparent,
rule-based adjustment that can be mechanically indexed to the prevailing allowance price (and
activated by an explicit price rule), which makes the redistribution predictable ex ante and
avoids ad hoc calibration of “excess” revenues. Second, the proposal is designed to reduce
electricity expenditure directly: the deducted amount is rebated to electricity consumers (e.g.,
through lower network charges or electricity taxes), thereby lowering effective prices in the
hours in which the mechanism is active. By contrast, windfall taxes typically accrue to the
general government budget and need not translate into lower electricity prices unless revenues
are explicitly earmarked and recycled back to electricity consumers.
5.2 Interaction with Long-Term Contracts
Fundamental incentive effects arise over longer horizons. Inframarginal rents in high-price hours
are an important part of the expected return to capital-intensive renewable investments, and
the mechanism reduces these rents.
As part of the recent European electricity market reform, two-way Contracts for Differ-
ence (CfDs) have been established as the standard support mechanism for new renewable and
non-emitting generation. Under the revised Electricity Regulation (European Parliament and
Council, 2024), if a member state provides state aid via direct price support for new renew-
able and nuclear generation, it must use two-way CfDs or schemes that have the same effect.
In these contracts a public counterparty and the generator agree on a strike price; when the
market price is below the strike price, the public counterparty compensates the generator, and
when the market price is above it, the generator pays back the difference. CfDs are intended
to provide revenue certainty and reduce investment risk while preserving market responsiveness
and avoiding distortions to short-term price signals. Two-way contracts for difference reduce
revenue risk and have been increasingly central to European market design reforms (Newbery,
4The numbers ofτand ˆphave changed since 2022. For example, the initialτwas 0.9 and later changed to
0.95. The threshold price ˆphas ranged from an initial 140e/MWh to 90e/MWh.
16

2016).
With CfDs in place for new plants, the proposed proxy deduction applies only to existing
generators operating purely in the spot market. A new plant under a CfD is exempt from the
deduction: its contract settles against the unadjusted uniform clearing pricep t, not against
the reduced remuneration priceept. Since the proxy deduction is a settlement adjustment that
leavesp t unchanged (see Section 3), the CfD reference price is unaffected and the generator
continues to receive the agreed strike price. The two instruments are therefore complementary:
CfDs stabilize revenue for investment-grade projects, while the proxy deduction redistributes
cyclical inframarginal rents from existing spot-exposed generation during high-price episodes
without blunting the carbon price signal in marginal bidding. We propose to apply the proxy
deduction to existing spot-exposed, non-emitting generation, and to offer two-way CfD remu-
neration to new, renewable investments.
5.3 Cross-Border Price Formation in Coupled Bidding Zones
European day-ahead markets are coupled across bidding zones through implicit allocation of
cross-border transmission capacity. As a result, the marginal generator setting the price in a
given zone need not be located within that zone. In particular, a gas-fired peaking plant abroad
(but inside the EU ETS agreement) can set the market-clearing price in the domestic zone
whenever cross-border transmission capacity is not binding. In such hours, the wholesale price
in the domestic zone reflects the foreign plant’s marginal cost, including its CO 2 component,
even though the marginal unit is not subject to domestic settlement rules.
The proposed mechanism should apply to domestic non-emitting generation irrespective
of whether the price-setting unit is located domestically or abroad. What matters for the
deduction is that the wholesale price exceeds the threshold and thereby embeds an allowance-
cost component—not the geographic location of the marginal plant, as long as it is within the
ETS zone. The settlement rule is defined over the zonal clearing price and domestic eligible
generation; both are observable within the zone regardless of cross-border flows.
A subtler case arises when cross-border transmission capacity is binding and the domestic
zone clears at a price above the threshold despite having abundant low-cost renewable genera-
tion. If the domestic zone is a net exporter in such an hour, the binding constraint fixes export
flows and decouples the domestic price from the importing zone. The price spread between zones
constitutes the congestion rent accruing to the TSO. With export volumes fixed at the trans-
mission limit, domestic generators face a locally perfectly inelastic residual demand—domestic
load plus the fixed export quantity—and may exercise market power by bidding above marginal
cost. In this setting, the proxy deduction serves a dual purpose: it redistributes inframarginal
rents to domestic consumers during such episodes, and it dampens the incentive for domes-
tic non-emitting generators to inflate bids against inelastic residual demand. The mechanism
therefore remains well-targeted even in the presence of binding interconnector constraints.
6 Application to Gas Price Shocks
In this section, we discuss how the proposed settlement adjustment can be used as a crisis
response to rising gas prices. Under uniform marginal pricing, any increase in the marginal cost
of the price-setting technology is transmitted to the market-clearing price and thereby to all
inframarginal output. The European gas crisis in 2022 highlighted this mechanism: natural gas
prices and CO 2 allowance prices were unusually high, which raised wholesale electricity prices
and generated large inframarginal rents (“windfall profits”) for non-gas technologies.
This motivates a crisis-oriented variant of the proxy deduction that targets the fossil marginal-
17

cost component embedded in wholesale prices rather than carbon costs alone. Let
M Ct = 1 η  pfuel,t +e fuel pCO2,t  ,
denote a proxy for the marginal cost of one MWh of electricity from the reference fossil tech-
nology (as in Equation (1)), and let
M Cref = 1 η  pref fuel +e fuel pref CO2 
denote a reference marginal cost level calibrated to pre-shock fuel and allowance prices (e.g., a
pre-crisis average or a policy benchmark). We define the excess cost component as the deviation
of marginal costs from this reference level:
δt = max{0, M Ct −M Cref}.
By construction,δ t ≥0, so the mechanism never implies a negative deduction when fossil
marginal costs fall below the reference level.
To avoid a discontinuous activation at a single cutoff price, we apply the deduction through
the linear phase-inep t =p t −d(p t) withd(·) as in Equation (5), usingδ t as the maximum
deduction level. Eligible non-emitting generators receiveep t while all other generators continue
to receive the uniform market pricep t.5 The lower boundp may be chosen near typical pre-crisis
wholesale prices. We let the upper bound vary with the excess-cost component,
pt =p +φ δt,
whereφ >0 scales the width of the phase-in region. For prices in the ramp regionp t ∈(p , pt),
we have
d′(pt) = δt pt −p = 1 φ ,and hence d˜pt dpt = 1− 1 φ .
Thus,φdirectly governs how strongly eligible generators’ remuneration responds to changes in
the market price within the phase-in interval: largerφimplies a wider phase-in region and a
slope closer to one, whileφ= 1 implies a flat remuneration ˜p t =p throughout the interval. We
restrict toφ≥1 to ensure d˜pt dpt ∈[0,1] within the phase-in region. 6
After the deduction, eligible generators receivep t −d(p t) per MWh while gas (and other
non-eligible) units continue to earnp t per MWh. The mechanism therefore reallocates part
of the inframarginal rent that arises when fossil marginal costs are high, without suppressing
scarcity signals or weakening incentives to economize on fossil fuel use. If the deducted revenues
are rebated to electricity consumers, the scheme is fiscally neutral and does not require public
funds. The incentive effects mirror those discussed in Section 4.
5The implementing authority must specify the eligible set. In a crisis setting, one natural choice is to apply
the deduction to non-gas generation. Whether coal- and lignite-fired units, storage, or subsidized plants should
be included depends on relative input costs, the policy objective, and on concerns about incentives and windfall
rents.
6The linear phase-in not only mitigates bunching incentives at the activation threshold; it also provides a
built-in lower bound for eligible remuneration. Under the ramp schedule withφ≥1, eligible units receive
ept =p t −d(p t) withd(p t)≤δ t, and in particularept ≥p for allp t ≥p . By contrast, under a discrete rule with a
fixed threshold pand a time-varying deductionδ t (e.g., indexed to gas prices), eligible remuneration in activated
hours is p−δ t. In extreme episodes,δ t may become large enough that p−δ t approaches zero or even turns
negative. This would create unintended short-run incentives for eligible generators to avoid being settled under
the deduction, potentially distorting bidding and participation behavior in high-price hours. One could address
this by allowing the activation threshold pto vary with market conditions (for example, indexing it to a gas-cost
benchmark), but such an approach effectively shifts activation to exceptional price spikes and would leave the
mechanism largely inactive in moderately elevated-price periods.
18

More broadly, the mechanism implements a rule-based risk-sharing arrangement. Under
uniform marginal pricing, fossil-fuel cost shocks are transmitted to electricity consumers through
the market-clearing price, even when most generation is non-emitting (European Commission,
2024). The proxy deduction shifts part of this price risk from consumers to inframarginal
producers by reducing eligible generators’ revenues in high-price states. Under the linear phase-
in, the sensitivity of eligible remuneration to the wholesale price is d˜pt dpt = 1− 1 φ within the ramp
region, so a fraction 1/φof marginal price changes is transferred from eligible producers to
consumers. As power systems decarbonize and fossil units set prices only intermittently, such a
rule-based mechanism offers an institutional alternative to ad hoc windfall taxes or emergency
price caps.
6.1 Illustrating Counterfactual Savings in 2022
To illustrate the magnitude of the crisis mechanism, we simulate the expenditure savings that
the gas-cost variant of the proxy deduction would have delivered during the European gas crisis
of 2022 and compare them to the outcomes of the “Iberian solution” in Spain, the only fuel-cost
intervention actually implemented during the crisis.
To provide intuition for the cost differences of gas power plants due to higher gas prices,
front-month prices on the Title Transfer Facility (TTF), Europe’s main gas benchmark, exceeded
300e/MWh th at their peak, compared to pre-crisis levels of roughly 20e/MWh th. Taking a
reference gas price of 20e/MWh th and an efficiency ofη= 55% for a combined-cycle gas
turbine, the implied excess electricity cost at peak gas prices was
δgas ≈ 1 0.55 (300−20)≈509e/MWh
(ignoring the carbon cost differences). Even at a more moderate gas price of 150e/MWh th,
the excess component was 1 0.55 (150−20)≈236e/MWh. Extreme fuel price shocks thus
mechanically generated very large inframarginal rents for non-gas generation whenever gas set
the marginal price.
For the counterfactual simulation we calibrate the reference marginal cost to a gas price
of 40e/MWh th (the cap used in Spain) and the 2021 average EU ETS carbon price of ap-
proximately 53e/t, yieldingM C ref = 92e/MWh. We setp = 70e/MWh to reflect average
pre-crisis electricity prices in 2020 and 2021 in Austria and Germany. Moreover, we implement
φ= 4/3, so each additional euro in the wholesale pricep t raises eligible generators’ remunera-
tion by 25 cents while 75 cents are redistributed to consumers. It follows that pt = 70 + 4 3 δt.
The maximal proxy deduction isδ t = max(M Ct −M Cref,0).
We apply this mechanism to hourly day-ahead prices in Austria and Germany during July–
December 2022, a period in which the Iberian cap was in force. Average net consumer expendi-
ture per MWh falls from 325.5 to 227.3e/MWh in Austria and from 292.5 to 220.8e/MWh in
Germany. These are reductions of 30.2% and 24.5%, respectively. Eligible generators receive on
average 148e/MWh in Austria and 122.4e/MWh in Germany. For comparison, the electricity
price in Spain averaged 129.7e/MWh over the same period under the Iberian solution (Fabra
et al., 2025). The redistribution channel alone therefore delivers sizable consumer relief without
distorting marginal costs. Headline price reductions remain smaller than in Spain because the
proxy deduction applies only to the eligible (non-gas) portfolio, i.e., fossil generators continue to
recover their full operating costs, whereas the Iberian mechanism directly subsidized gas-fired
generation to suppress the clearing price.
7 Conclusion
European electricity markets face a structural tension. Renewable generation has near-zero
marginal costs, yet under uniform marginal pricing, wholesale electricity prices in hours when
19

Figure 9: Weekly average wholesale price, eligible-generator remuneration, and net consumer
expenditure under crisis mechanisms, July–December 2022
Note:The reference marginal cost is calibrated using a gas price of 40e/MWh th (the Iberian cap)
and the 2021 average carbon price. On days where the realized gas price exceeds this reference,
the resulting marginal cost differential is subtracted from the day-ahead price for non-gas generators
(dot-dashed line). The dashed line shows the resulting average consumer price. Spain’s prices reflect
actual outcomes under the Iberian mechanism over the same period, following Fabra et al. (2025).
fossil plants are marginal reflect carbon allowance and fuel costs that non-emitting generators do
not incur. The resulting inframarginal rents raise consumer expenditures, weaken electrification
incentives, and put pressure on industrial competitiveness.
This paper proposes a settlement rule that addresses this tension directly. A conditional
CO2 proxy deduction is applied to the remuneration of non-emitting generators in high-price
hours, redistributing part of their inframarginal rents to consumers. The mechanism preserves
the uniform clearing price, maintains marginal dispatch and fuel-switching incentives for fossil
generators, and leaves the carbon price signal intact. It thereby separates the distributional
channel—who captures the rent created by carbon pricing—from the allocative channel that
makes carbon pricing effective.
A static accounting exercise using hourly data yields expenditure reductions of about 8.5%
for Austria and 4.7% for Germany, concentrated in peak-load hours when fossil generation sets
the price. A gas-cost variant applied to the second half of 2022 would have reduced average
electricity expenditure by about 30% in Austria and 25% in Germany, delivering consumer relief
comparable to the Iberian mechanism but without subsidizing fossil generation.
The mechanism involves trade-offs. A hard activation threshold creates a payoff discon-
tinuity that may induce price bunching; phasing the deduction in over a price interval via a
linear ramp eliminates this discontinuity and preserves full marginal incentives throughout the
transition range. Over longer horizons, reduced inframarginal rents lower the expected return
on merchant renewable investment. Two-way Contracts for Difference, now the standard EU
support mechanism for new non-emitting capacity, provide a natural complement: new plants
operating under CfDs settle against the unadjusted clearing price and are therefore exempt from
the deduction, while the proxy deduction redistributes cyclical rents from existing spot-exposed
generation. The mechanism can be implemented either as a modified auction settlement or
as an equivalent technology-specific levy, and applies within coupled European bidding zones
20

regardless of whether the marginal unit is located domestically or abroad.
More broadly, the proposal offers a rule-based institutional alternative to ad hoc windfall
taxes and emergency price caps. By reducing effective electricity costs in high-price hours, it
may strengthen demand-side electrification incentives, supporting the broader decarbonization
objective that carbon pricing is designed to serve.
References
EKB-S, Republik ¨Osterreich, “Bundesgesetz ¨ uber den Energiekostenbeitrag
Strom,” Bundesgesetzblatt I Nr. 220/2022 2022. Legislative materials:
https://www.parlament.gv.at/gegenstand/XXVII/A/3024; consolidated version as
amended available at https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage= Bun-
desnormen&Gesetzesnummer=20012141 (accessed 26 January 2026).
European Commission, “The Draghi Report on European Competitiveness,” 2024.
https://commission.europa.eu/topics/competitiveness/draghi-report en (accessed 26 January
2026).
European Parliament and Council, “Regulation of the European Parliament and of the
Council amending Regulations (EU) 2019/943 and (EU) 2019/942 as regards improving the
Union’s electricity market design,” PE-CONS 1/24 INIT 2024.
F abra, Natalia and Mar Reguant, “Pass-Through of Emissions Costs in Electricity Mar-
kets,”American Economic Review, 2014,104(9), 2872–2899.
, Clement Leblanc, and Mateus Souza, “Unpacking the Distributional Implications of
the Energy Crisis,” Technical Report 12093, CESifo Working Papers 2025.
Hintermann, Beat, “Pass-Through of CO2 Emission Costs to Hourly Electricity Prices in
Germany,”Journal of the Association of Environmental and Resource Economists, 2016,3
(4), 857–891.
Hirth, Lion and F alko Ueckerdt, “Redistribution effects of energy and climate policy: The
electricity market,”Energy Policy, 2013,62, 934–947.
Kazmin, Amy , Rachel Millard, and Alice Hancock, “Italy sets up fight with Brussels
over carbon costs,”Financial Times, 2026,1 March 2026.
Newbery , David, “Missing money and missing markets: Reliability, capacity auctions and
interconnectors,”Energy Policy, 2016,94, 401–410.
Schmalensee, Richard and Robert N. Stavins, “Lessons Learned from Three Decades of
Experience with Cap and Trade,”Review of Environmental Economics and Policy, 2017,11
(1), 59–79.
Sensfuß, F rank, Mario Ragwitz, and Massimo Genoese, “The merit-order effect: A
detailed analysis of the price effect of renewable electricity generation on spot market prices
in Germany,”Energy Policy, 2008,36(8), 3086–3094.
Sijm, Jos, Karsten Neuhoff, and Yihsu Chen, “CO2 cost pass-through and windfall profits
in the power sector,”Climate Policy, 2006,6(1), 49–72.
, Yihsu Chen, and Benjamin F. Hobbs, “The impact of power market structure on CO2
cost pass-through to electricity prices under quantity competition – A theoretical approach,”
Energy Economics, 2012,34(4), 1143–1152.
21

A Additional Tables
Table 1: Revenue loss by technology under hard threshold of 100e/MWh
Austria (A T) Germany (DE)
T echnology Gen. (TWh) Rev. Loss (Mio.e) Loss (%) Gen. (TWh) Rev. Loss (Mio.e) Loss (%)
Biomass 0.24 3.7 15.1% 35.9 431 12.9%
Geothermal — — — 0.20 2.4 13.2%
Hydro reservoir 3.52 59.4 15.2% 1.29 21.7 14.8%
Hydro RoR 23.9 322 13.9% 12.8 147 12.7%
Other renewable — — — 0.60 7.2 13.3%
Solar 5.60 31.2 10.7% 73.9 303 8.7%
Wind offshore — — — 26.1 253 11.2%
Wind onshore 8.29 112 13.8% 107 872 10.5%
Note:Values represent percentage reduction in revenue relative to the baseline. “—” indicates the technology is
absent or negligible (<0.01 TWh) in the respective zone.
Table 2: Sensitivity analysis: threshold and deduction (no pumped storage)
Deduction 23e/MWh 28e/MWh 33e/MWh
Threshold
(e/MWh)
Base
Price
New
Price
Reduction
(%)
New
Price
Red.
(%)
New
Price
Red.
(%)
Austria (A T)
80 104.4 93.0 10.9 90.6 13.2 88.1 15.6
90 104.4 94.9 9.10 92.8 11.1 90.7 13.1
100 104.4 97.1 6.99 95.5 8.52 93.9 10.1
110 104.4 99.0 5.17 97.8 6.32 96.6 7.47
Germany (DE)
80 92.8 86.1 7.22 84.6 8.84 83.2 10.3
90 92.8 87.7 5.50 86.6 6.68 85.5 7.87
100 92.8 89.2 3.88 88.4 4.74 87.6 5.60
110 92.8 90.3 2.69 89.8 3.23 89.2 3.88
Note:Prices ine/MWh.
22

Table 3: Policy comparison of linear ramp to hard threshold
Zone Policy Expenditure Base Absolute Red. Expenditure New Reduction (%) Base Price New Price
AT HT 6178 528 5649 8.55 104.4 95.47
AT LR 6178 731 5446 11.84 104.4 92.04
DE HT 43207 2037 41170 4.71 92.79 88.41
DE LR 43207 3235 39973 7.49 92.79 85.84
Note:HT = Hard threshold 100e/MWh; LR = Linear ramp 72→100e.δ= 28e/MWh. Expenditure figures
in millions of euros. Prices ine/MWh.
23
