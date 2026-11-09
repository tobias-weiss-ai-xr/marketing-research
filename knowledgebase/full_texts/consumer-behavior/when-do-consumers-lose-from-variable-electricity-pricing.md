---
title: When Do Consumers Lose from Variable Electricity Pricing?
url: https://arxiv.org/abs/2509.01499
category: consumer-behavior
subcategory: empirical
date: 2025-09
venue: ''
authors:
- Nathan Engelman Lado
- Richard Chen
- Saurabh Amin
source: arxiv
pdf_url: https://arxiv.org/pdf/2509.01499
pages: 56
chars: 132358
fetched_at: '2026-11-08T13:10:56+00:00'
kb_version: 1
---

# When Do Consumers Lose from Variable Electricity Pricing?

Graphical Abstract
When Do Consumers Lose from Variable Electricity Pricing?
Nathan Engelman Lado, Richard Chen, Saurabh Amin
Vulnerability Factors
• High peak consumption
• Limited flexibility
• High price sensitivity
Key Insights
• Flexibility has the greatest impact
in periods of large price shifts
• Peak period inflexibility
increases peak price shift
Theory Contribution
Sufficient conditions identifying
when consumers lose from
pricing transitions.
Distributional Pattern
Benefits concentrate among
flexible consumers with
less peak-dominated usage and
high peak period flexibility.
Contribution: Theoretical framework identifying conditions
for consumer welfare losses from the transition to variable pricing
Figure 1: Theoretical framework for analyzing consumer vulnerability to variable electricity pricing transi-
tions.
arXiv:2509.01499v1  [econ.GN]  1 Sep 2025

Highlights
When Do Consumers Lose from Variable Electricity Pricing?
Nathan Engelman Lado, Richard Chen, Saurabh Amin
• We derive sufficient conditions identifying when consumers lose utility from variable
electricity pricing transitions based on consumption patterns, demand flexibility, and
price sensitivity.
• Demand flexibility provides welfare protection only when coincident with large price
changes, explaining why higher-income consumers typically benefit more from time-
varying rates.
• Low-income consumers face amplified welfare effects from pricing reforms due to higher
price sensitivity, experience larger utility changes even when their consumption and
flexibility patterns are identical.
• Our results suggest variable pricing policies require complementary measures to prevent
disproportionate harm to vulnerable consumers.

When Do Consumers Lose from Variable Electricity Pricing?
Nathan Engelman Lado a,∗, Richard Chen b, Saurabh Amin c
aInstitute for Data Systems and Society, MIT, 77 Massachusetts Ave, Cambridge, 02139, MA, USA
bCivil and Environmental Engineering, MIT, 77 Massachusetts Ave, Cambridge, 02139, MA, USA
cLaboratory for Information and Decision Systems, MIT, 77 Massachusetts
Ave, Cambridge, 02139, MA, USA
Abstract
Time-varying electricity pricing better reflects the varying cost of electricity compared to
flat-rate pricing. Variations between peak and off-peak costs are increasing due to weather
variation, renewable intermittency, and increasing electrification of demand. Empirical and
theoretical studies suggest that variable pricing can lower electricity supply costs and reduce
grid stress. However, the distributional impacts, particularly on low-income consumers, re-
main understudied. This paper develops a theoretical framework to analyze how consumer
heterogeneity affects welfare outcomes when electricity markets transition from flat-rate to
time-varying pricing, considering realistic assumptions about heterogeneous consumer de-
mand, supply costs, and utility losses from unmet consumption.
We derive sufficient conditions for identifying when consumers lose utility from pricing
reforms and compare welfare effects across consumer types. Our findings reveal that con-
sumer vulnerability depends on the interaction of consumption timing, demand flexibility
capabilities, and price sensitivity levels. Consumers with high peak-period consumption and
inflexible demand, characteristics often associated with low-income households, are most vul-
nerable to welfare losses. Critically, we demonstrate that demand flexibility provides welfare
protection only when coincident with large price changes, a condition more easily met by
higher-income consumers in most empirical studies. Our equilibrium analysis reveals that
aggregate flexibility patterns generate spillover effects through pricing mechanisms, with
peak periods experiencing greater price changes when they have less aggregate flexibility,
potentially concentrating larger price increases among vulnerable populations that have a
limited ability to respond. These findings suggest that variable pricing policies designed
to support clean energy transitions risk exacerbating energy inequality unless accompanied
by targeted policies ensuring equitable access to demand response capabilities and pricing
benefits.
Keywords: Variable electricity pricing, Consumer heterogeneity, Demand flexibility,
Distributional effects
∗Corresponding author
Email addresses: engelm25@mit.edu (Nathan Engelman Lado), rachen@mit.edu (Richard Chen),
amins@mit.edu (Saurabh Amin)
Preprint submitted to Energy Policy September 3, 2025

1 INTRODUCTION
1. Introduction
The high demand for electricity during peak hours drives up supply costs, making reliable
production and delivery more expensive. Flat rates obscure these temporal costs, pushing
demand up during peaks and down during off-peak hours (Borenstein and Bushnell, 2022).
Time-varying electricity pricing better aligns consumption with supply costs by providing
price signals that can lower system costs and increase reliability. Yet variable pricing also
creates distributional concerns. Consumers with flexible demand or new technologies can
adapt, but low-income households often face higher bills and welfare losses from foregone
consumption. We develop a theoretical framework to identify which consumers gain or lose
from this transition, and under what conditions low-income households are disproportion-
ately harmed.
In practice, most regions experience pronounced peaks during evening hours and lower
demand overnight and mid-day (U.S. Energy Information Administration, 2020). Climate
change intensifies these fluctuations by increasing cooling demand during hot afternoons,
while renewable integration creates additional variability as solar generation peaks mid-
day but drops during evening demand peaks. Electrification of transportation and heating
further concentrates demand during specific hours when people return home and charge
vehicles. Together, these trends widen the gap between peak and off-peak supply costs, as
grid operators must maintain expensive backup generation and transmission capacity to meet
increasingly sharp demand spikes (Auffhammer et al., 2017). Grid operators can respond by
adding storage or backup generation, expanding transmission, or implementing demand-side
measures that shift consumption to lower cost periods (Schittekatte et al., 2023).
Even when flexibility is technically possible, this might come at a significant cost. Low-
income households often keep electricity use at subsistence levels for health and safety needs
such as heating, cooling, and lighting (Anderson et al., 2012; Cong et al., 2022; Kwon et al.,
2023). Evidence from multiple regions shows that cost pressures already force compromises:
in Britain, households reduce heating at the expense of health (Anderson et al., 2012); in
the U.S., poor insulation makes basic cooling unaffordable (Best and Sinha, 2021), and in
Arizona, low-income households delay air conditioning until homes are 4.7–7.5◦F hotter than
those of higher-income households (Cong et al., 2022). Such constraints lead to elevated rates
of heat-related hospitalization and mortality (Kwon et al., 2023).
This creates a double burden for low-income households under variable pricing. Budget
pressures may force them to be highly price-responsive (Br¨ annlund and Vesterberg, 2021).
However, their flexibility is unlikely to be uniform across periods: off-peak discretionary
uses may be highly elastic, while peak-period services tied to health and safety may remain
relatively inelastic due to health constraints. This asymmetric flexibility pattern suggests
that low-income households could appear responsive in aggregate demand studies, yet remain
less able to adjust consumption during the peak periods when variable pricing raises costs.
Our theoretical analysis reveals that demand flexibility increases the change in welfare
when aligned with large price changes: consumers who are flexible during periods with small
price adjustments gain little benefit, while those who can adjust consumption during periods
with substantial price changes receive significant welfare protection. This helps explain why
variable pricing benefits might be concentrated among higher-income consumers who have
greater access to high-quality housing, flexible work schedules, and other demand response
Preprint submitted to Energy Policy – please cite published version once available

1.1 Contributions 1 INTRODUCTION
capabilities. Additionally, our equilibrium analysis demonstrates important spillover effects:
individual flexibility contributes to aggregate demand responsiveness, which affects the mag-
nitude of price adjustments across periods. A peak period with higher aggregate flexibility
experiences smaller price changes than one in which consumers are flexible. This creates
interactions between consumers in which one consumer’s flexibility influences the welfare of
the other.
This paper contributes to the literature by developing a theoretical framework that iden-
tifies conditions under which consumers lose utility from variable pricing reforms and when
low-income consumers are disproportionately harmed. We derive sufficient conditions based
on three key consumer characteristics: consumption patterns across periods, flexibility, and
price sensitivity. We show that consumers with high peak use, limited flexibility, and high
price sensitivity face the greatest risk from a switch to variable pricing. By incorporating het-
erogeneous consumer utility functions and realistic assumptions about price responsiveness,
we provide analytical tools for evaluating the distributional impacts of pricing reforms before
implementation. This theoretical foundation connects empirical work on energy poverty and
consumption patterns with the growing literature on electricity market design, offering in-
sights essential for designing variable pricing policies that achieve both efficiency and equity
objectives in the transition to more flexible, renewable-powered electricity systems.
1.1. Contributions
Theoretical Framework for Consumer Heterogeneity: We develop a framework that ex-
plicitly incorporates three dimensions of consumer heterogeneity in electricity pricing: con-
sumption patterns across time, flexibility, and price sensitivity (marginal disutility of expen-
diture). While prior studies often assume constant elasticity across consumers and periods,
our framework allows these traits to vary and shows how they affect welfare outcomes.
Sufficient Conditions for Identifying Vulnerable Consumers: We derive tractable suffi-
cient conditions that identify which consumers lose from variable pricing transitions, both
in absolute terms and relative to other groups. For quadratic loss functions, these condi-
tions are necessary and sufficient; for general demand functions, they provide conservative
screening tools. These analytical tools enable ex-ante assessment of distributional impacts.
Timing of Flexibility Benefits: We demonstrate that demand flexibility provides welfare
protection only when coincident with large price changes. Because welfare benefits scale with
the square of price changes, consumers who are flexible during small shifts gain little. This
timing-dependent relationship explains why higher-income consumers often benefit more
from variable pricing.
Equilibrium Spillover Effects: We show how individual flexibility aggregates to shape
market prices. High aggregate peak flexibility dampens peak price increases, while low peak
flexibility allows larger price adjustments that disproportionately harm inflexible consumers.
These spillovers create cross-consumer interactions where one household’s flexibility directly
affects others through equilibrium price formation.
Distributional Impact Mechanisms: Price sensitivity (Ai) amplifies welfare changes with-
out affecting their direction. Even with identical consumption patterns and flexibility, con-
sumers with higher marginal disutility of expenditure (e.g., low-income households with
Al > Ah) experience larger magnitude welfare swings from variable pricing.
Preprint submitted to Energy Policy – please cite published version once available

1.2 Related Literature 1 INTRODUCTION
Together, these contributions connect empirical research on energy poverty and consump-
tion with theoretical work on electricity market design, providing analytical foundations for
designing variable pricing policies that balance efficiency with equity in demand-responsive
systems.
1.2. Related Literature
Previous Work on Time-Varying Pricing: The economic theory underlying variable
electricity pricing dates back at least to Mohring’s (1970) peak-load pricing model, which es-
tablished that efficiency requires marginal-cost pricing in each period (Mohring, 1970). Early
work by Feldstein (1972) identified key equity concerns, noting that lower-income consumers
have less flexibility to adapt to peak pricing due to constraints in appliance ownership and
housing quality, while also benefiting more from low prices for essential goods due to higher
marginal utility of income (Feldstein, 1972). This analysis highlighted that pricing policies
ignoring heterogeneity in flexibility and electricity’s relative importance across periods risk
disproportionately impacting vulnerable households.
More recent theoretical work has quantified the efficiency gains from time-varying pricing.
(Borenstein, 2005) demonstrates how real-time pricing reduces reliance on expensive peak-
ing plants and improves capacity cost recovery, while Borenstein and Bushnell (2022) shows
that flat-rate pricing creates larger deadweight losses than other common pricing distortions,
including emissions externalities and volumetric recovery of fixed costs. These studies estab-
lish the strong efficiency case for variable pricing but give limited attention to distributional
consequences.
Empirical Evidence from Pricing Experiments: Early empirical studies of time-of-use
(TOU) tariffs in the United States, reviewed in (Aigner, 1985), found significant behavioral
responses, with consumers primarily reducing peak demand rather than shifting consumption
to off-peak periods. (Caves et al., 1984) provided crucial insights into consumer heterogeneity,
demonstrating that responsiveness to time-varying prices depends on appliance ownership,
weather conditions, and climate control needs. Importantly, they found that households
with fewer appliances, typically lower income—showed limited responsiveness to TOU tar-
iffs, reducing their ability to benefit from time-varying prices compared to households with
more appliances. More recent studies of critical peak pricing (CPP) programs confirm these
patterns, with greater load reductions than TOU but continued evidence that benefits vary
across income groups based on appliance flexibility (Faruqui and Sergici, 2010).
Simulation Studies and Distributional Analysis: When experimental data is unavail-
able, researchers use historical consumption data to simulate variable pricing impacts, typi-
cally assuming constant elasticity across consumers and periods. Results from these studies
are mixed regarding distributional effects. Horowitz and Lave (2014) find that low-income
consumers often perform worse under real-time pricing due to smaller, less flexible loads
and limited appliance ownership. Conversely, Simshauser and Downer (2016) conclude that
lower-income households with flatter load profiles can benefit from TOU and CPP rates.
Burger et al. (2020) shows that while low-income consumers may face higher bills under
time-varying tariffs, those with demand flexibility can gain consumer surplus due to lower
marginal electricity costs. These conflicting empirical findings reflect a key limitation in
the existing literature: the assumption of homogeneous elasticity across consumers and time
periods obscures the heterogeneity in flexibility that our theoretical analysis shows is crucial
Preprint submitted to Energy Policy – please cite published version once available

1.2 Related Literature 1 INTRODUCTION
for understanding distributional outcomes. Our work addresses this gap by developing a
framework that explicitly incorporates variation in demand responsiveness across consumer
types and time periods, providing theoretical foundations for understanding when and why
variable pricing creates winners and losers.
Table 1: Key Notation and Definitions
Symbol Definition
Periods and Consumers
t ∈ {PE, OP} Time periods: peak (PE) and off-peak (OP)
i ∈ {l, h} Consumer types: low-income ( l) and high-income ( h)
Superscripts v, f Variable pricing and flat pricing regimes
Prices and Consumption
πf Flat-rate electricity price (uniform across periods)
πv t Variable price in period t
df it, dv it Consumption by consumer i in period t under flat/variable pricing
d∗ it Optimal consumption by consumer i in period t ¯dit Maximum consumption capacity for consumer i in period t
Consumer Preferences
Ui Total utility of consumer i across periods
Jit(d) Loss function from consuming d units in period t
Ai Price sensitivity (marginal disutility of expenditure)
Al > Ah Low-income consumers more price-sensitive
ˆJit(d) = Jit(d)/Ai Normalized loss function
Supply and Welfare
C(dt) Cost of supplying dt units in period t
Lt Social loss in period t
L = P t Lt Total social loss
Flexibility and Elasticity

 ∂d∗ it ∂πt

 Consumer i’s demand flexibility in period t

 ∂dt ∂πt

 Aggregate flexibility in period t
ϵit Price elasticity of consumer i in period t
Key Differences
∆Ui Change in consumer i’s utility from flat to variable pricing
∆πt = |πv t − πf | Absolute price change in period t
∆Uh − ∆Ul Difference in utility changes between consumer types
Preprint submitted to Energy Policy – please cite published version once available

2 MODEL
2. Model
2.1. Consumer Model
We model a two-period electricity market with peak (1) and off-peak (2) periods, denoted
t ∈ T := {1, 2}. This market serves two consumer types i ∈ N:= {l, h}, representing
low-income ( l) and high-income ( h) households. Let dit denote consumer i’s electricity
consumption in period t, constrained by maximum consumption ¯dit, reflecting physical or
technological limits. Taking the per-kWh price πt as given, consumer i’s utility is:
Ui := Mi −
X
t∈T
(Jit(dit) + Aiπtdit), (1)
where Jit(dit) represents the loss from consuming dit < ¯dit, Mi is consumer i’s maximum
attainable utility, and Ai > 0 captures consumer i’s marginal disutility of expenditure. We
assume Al > Ah to reflect the greater marginal utility of income for low-income consumers.
We normalize utility so that consuming zero electricity yields zero net utility: when dit = 0,
we have Ui = Mi − Jit(0) = 0, which implies Mi = Jit(0). We use the hat notation ˆJit := Jit Ai
to denote electricity loss normalized by the marginal disutility of expenditure. Consumer
surplus, measuring net benefit relative to cost, equals Ui/Ai.
We focus on a two-period model to capture the fundamental distinction between high-
demand periods (when air conditioning or heating needs are critical) and low-demand pe-
riods. This stylized framework isolates the key distributional mechanisms while remaining
simple for exposition. As shown in Section 5, the form of the results holds for a more general
N consumer, T period model.
For any feasible consumption level d ∈ [0, ¯dit], we assume the consumer model satisfies:
Assumption 1. The electricity loss function Jit(d) satisfies:
1.a Regularity: Jit is three times differentiable with Jit ≥ 0, J ′ it < 0, J ′′ it > 0, and J ′′′ it < 0.
1.b Peak period criticality:Loss from under-consumption is greater during peak periods:
Ji2(d) ≤ Ji1(d) for all d.
1.c Marginal loss ordering:The marginal reduction in loss from additional consump-
tion satisfies |J ′ i1(d)| ≥ |J ′ i2(d)| for all d.
1.d Curvature ordering: The rate of change in marginal loss is greater during peak
periods: J ′′ i1(d) ≥ J ′′ i2(d) > 0 for all d.
Assumption 1 provides the foundation for our consumer model. The regularity conditions
in 1.a are standard for non-appliance-based models of electricity consumption (Jiang and
Low, 2011; Jordehi, 2019; Deng et al., 2015). The decreasing loss function ( J ′ it < 0) reflects
that consuming more electricity reduces loss, while convexity ( J ′′ it > 0) ensures diminishing
marginal loss reduction: initial units serve critical needs (lighting, basic appliances), while
later units provide smaller benefits (comfort, non-essential uses). The third derivative condi-
tion (J ′′′ it < 0) implies convex demand curves (see (B.9)). This means that demand becomes
more price-responsive at higher prices, consistent with models where non-essential uses are
Preprint submitted to Energy Policy – please cite published version once available

2.2 Optimal Demand 2 MODEL
eliminated first and consumers reduce more critical consumption as prices continue to rise
(Burger et al., 2020). Note that the consumer utility function (1) is concave in dit since
∂2Ui
∂d2 it = −J ′′ it(dit) < 0. We are especially concerned with the energy demand of heating or cooling devices during
critical high-demand periods. The period-specific assumptions 1.b–1.d capture systematic
differences between peak and off-peak electricity demand during weather extremes. As-
sumption 1.b reflects that peak periods involve additional critical electricity uses (e.g., air
conditioning during heat waves), leading to greater loss from forgone consumption at any
given level compared to off-peak periods. Assumption 1.c implies that each unit of electricity
results in less loss during peak periods, since appliances work harder to maintain temperature
under extreme conditions, and more appliances are in use. Assumption 1.d indicates that
marginal benefits of consumption decrease more quickly during peak periods—the first units
address critical health and safety needs, but once satisfied, additional consumption yields
rapidly diminishing benefits compared to the more gradual decline in the off-peak period.
These assumptions enable analysis using standard electricity loss functions, including the
quadratic specifications commonly employed in demand response models (Burger et al., 2020;
Fell et al., 2014), while ensuring our results reflect realistic consumption patterns across time
periods and income groups.
2.2. Optimal Demand
Formally, for a given pricing schemeπt, t∈ T, consumer i’s decision problem is equivalent
to:
min
dit
X
t∈T
(Jit(dit) + Aiπtdit) (2a)
s.t. 0 ≤ dit ≤ ¯dit ∀t ∈ T (2b)
For interior solutions where 0 < d∗ it < ¯dit, the first-order condition is necessary and
sufficient:
∂Jit
∂dit

d∗ it
+ Aiπt = 0 = ⇒ −∂ ˆJit
∂dit

d∗ it
= πt ∀i ∈ N, t∈ T. (3)
That is, when optimal consumption lies in the interior of the interval [0, ¯dit], the marginal
avoided loss, or willingness to pay, equals the price. We focus on interior solutions throughout
this work, which allows us to use the first-order condition (3) to characterize a consumer’s
optimal demand as a function of price (full derivation in Appendix B.1). Note that since
J ′ it < 0 and J ′′ it > 0 from Assumption 1, the function J ′ it is strictly decreasing and therefore
invertible on the relevant domain.
Proposition 1. Optimal demand as a function of price is:
d∗ it(πt) = min{max{( ˆJ ′ it)−1(−πt), 0}, dit} ∀i, t. (4)
Preprint submitted to Energy Policy – please cite published version once available

2.2 Optimal Demand 2 MODEL
The min{max{·}} construction ensures that demand respects both the non-negativity con-
straint (dit ≥ 0) and the capacity constraint ( dit ≤ ¯dit).
We refer to the optimal consumption function (4) as the demand curve; see Figure 2.
The normalized utility formulation ensures that ˆJit(d∗ it) +πtd∗ it produces the same willingness
to pay and demand curve, given ˆJit(d∗ it), regardless of the consumer’s exact price sensitivity
Ai or loss Jit(d∗ it). The first-order condition represents the trade-off between the marginal
benefit from avoided electricity loss and the marginal cost of consumption. Consequently,
although a low-income consumer may have greater marginal avoided loss from electricity
consumption (due to higher Ai), they do not necessarily demand more electricity than high-
income consumers, as this depends on the interaction between Ai, ¯dit, and the loss function
Jit(·).
πt
dit
d∗ it(πt)
( ˆJ ′ it)−1(−πt)¯dit
− ˆJ ′ it( ¯dit) − ˆJ ′ it(0)
Figure 2: Consumption d∗ it as a function of price πt; dit is bounded below by 0 and above by ¯dit.
Having characterized optimal demand, we now derive how demand responds to price
changes—a key determinant of distributional outcomes under variable pricing. Consumer
flexibility—the responsiveness of demand to price changes—is given by the derivative of the
demand function. Taking the derivative of (4), we obtain:
∂d∗ it(πt)
∂πt
=



0 d∗ it(πt) = dit,
−Ai
J ′′ it(d∗ it(πt)) = − 1 ˆJ ′′ it(d∗ it(πt)) d∗ it(πt) ∈ (0, dit),
0 d∗ it(πt) = 0.
(5)
Therefore, for interior solutions, consumer flexibility is

 ∂d∗ it ∂πt

 = 1 ˆJ ′′ it(d∗ it(πt)) . For identical
loss functions Jlt = Jht, the condition Al > Ah implies ˆJ ′′ lt < ˆJ ′′ ht, so low-income consumers
are more flexible than high-income consumers. From Assumption 1, we know that ˆJ ′′ it > 0
and ˆJ ′′ it is decreasing in demand, so flexibility increases with demand. Furthermore, since ˆJ ′′ it(d∗ it(πt)) is the composition of two decreasing functions ˆJ ′′ it(dit) and d∗ it(πt), flexibility also
decreases as price increases.
Finally, we examine how consumer utility changes with price. We apply the chain rule
to (1) and use (3) and (5) to show that the decrease in utility is proportional to optimal
Preprint submitted to Energy Policy – please cite published version once available

2.3 Consumer Heterogeneity 2 MODEL
consumption:
∂U ∗ it(πt)
∂πt
=



0 d∗ it(πt) = dit,
−Aid∗ it(πt) d∗ it(πt) ∈ (0, dit),
0 d∗ it(πt) = 0.
(6)
For the same level of demand, the low-income consumer experiences larger changes in
utility than the high-income consumer because Al > Ah; the low-income consumer gains
more utility from a price decrease but loses more from a price increase.
Finally, we introduce the aggregate consumer to analyze market-level behavior. The ag-
gregate consumer represents the sum of all individual consumers with aggregate consumption
dt = P i∈N dit in period t. We construct an aggregate loss function such that the aggregate
consumer’s optimization problem mirrors that of individual consumers. In Appendix B.2, we
prove that under Assumption 1, an appropriately constructed aggregate consumer satisfies
the same optimality conditions as individual consumers: the aggregate first-order condition
− ˆJ ′ t(d∗ t ) = πt, the aggregate demand characterization d∗ t = ( ˆJ ′ t)−1(−πt), and aggregate flex-
ibility | ∂d∗ t ∂πt | = 1 ˆJ ′′ t (d∗ t ) . We also establish that ˆJ ′′ t is increasing in the curvature of individual loss functions, so aggregate flexibility falls when consumers are less flexible individually.
2.3. Consumer Heterogeneity
Our modeling approach addresses two critical gaps identified above. First, despite empir-
ical evidence of substantial heterogeneity in price responsiveness (Faruqui and Sergici, 2010;
Aigner, 1985), existing studies typically assume uniform elasticity when analyzing variable
pricing impacts (Burger et al., 2020; Horowitz and Lave, 2014). Second, while empirical stud-
ies document varying distributional outcomes (Simshauser and Downer, 2016; Borenstein,
2012), the literature lacks a unified theoretical framework for predicting when low-income
consumers will be harmed by pricing reforms (Joskow and Wolfram, 2012).
We address these gaps through two key modeling innovations: heterogeneous demand
flexibility and parameterized consumption patterns.
Demand flexibility. From (5), consumer flexibility is

 ∂d∗ it ∂πt

 = 1 ˆJ ′′ it(d∗ it(πt)) . Existing stud- ies of variable pricing typically assume either price-insensitive consumers or price-sensitive
consumers with isoelastic demand (constant proportional response to price changes) (Burger
et al., 2020; Horowitz and Lave, 2014; Simshauser and Downer, 2016). In these studies,
elasticity is constant across consumers and periods. However, experimental studies reveal
substantial heterogeneity in price responsiveness. Faruqui and Sergici (2010) document dif-
ferent elasticities between peak and off-peak periods, while Aigner (1985) and Caves et al.
(1984) show that elasticity varies with temperature, appliance use, and local climate—factors
that differ systematically between periods and across consumer groups. Our framework cap-
tures this heterogeneity by allowing flexibility to vary through the parameters Ai and J ′′ it,
enabling analysis of how different responsiveness patterns affect distributional outcomes. We
use flexibility (quantity response per unit price change) rather than elasticity (proportional
response) because flexibility directly determines the magnitude of consumption adjustments
and their welfare implications.
Preprint submitted to Energy Policy – please cite published version once available

2.4 Social Welfare 2 MODEL
Consumption patterns. A consumer’s consumption pattern—encompassing demand
levels and timing across periods—largely determines how they are affected by variable pricing
transitions. Empirical studies reveal that low-income households exhibit different patterns
than higher-income groups, but these differences vary significantly across contexts. In Aus-
tralia, Simshauser and Downer (2016) find that low-income households have larger overall
consumption with more consistent demand across peak and off-peak periods. Conversely,
Horowitz and Lave (2014) document that such households in their sample have more peak-
dominated usage, while Borenstein (2012) find that high-income households are the largest
overall electricity users. These differences translate directly into distributional outcomes:
Simshauser and Downer (2016) find that low-income households benefit most from tariff
reform due to their flatter profiles, while Horowitz and Lave (2014) and Borenstein (2012)
conclude that low-income households face higher bills under variable pricing due to their
peak-heavy or low overall usage patterns, respectively. Our framework captures this empir-
ical heterogeneity by parameterizing maximum consumption ( ¯dit) and loss curvature ( J ′′ it),
allowing analysis of how consumption patterns and pricing structures interact to determine
distributional impacts.
Our parameterization generates heterogeneity in consumer flexibility


 ∂d∗ it ∂πt

 = Ai J ′′ it(d∗ it(πt)) 
and consumption patterns under flat pricing. We use this framework to derive general prop-
erties of optimal consumption and characterize how flexibility and consumption patterns
determine consumer welfare changes. Using no assumptions regarding the differences be-
tween consumers beyond Al > Ah (reflecting higher marginal disutility of expenditure for
low-income consumers), we identify conditions under which pricing changes disproportion-
ately impact low-income consumers, providing theoretical foundations for understanding the
distributional consequences of electricity rate design.
2.4. Social Welfare
We model a social welfare-maximizing planner who sets electricity prices and procures
supply to serve consumer demand. Following Deng et al. (2015), this setup simplifies the two-
stage market structure of Joskow and Tirole (2006) by combining wholesale procurement and
retail pricing decisions into a single optimization problem. The planner faces a cost function
C(dt) representing the cost of procuring aggregate electricity dt in period t, where the same
cost technology applies across both peak and off-peak periods. The cost function satisfies:
Assumption 2. The electricity procurement cost function is non-negative, non-decreasing,
and convex: C(d) ≥ 0, C ′(d) ≥ 0, and C ′′(d) ≥ 0 for all d ≥ 0.
These conditions reflect standard properties of electricity supply: non-negative costs,
non-decreasing marginal costs (as cheaper generation units are dispatched first), and convex
costs (reflecting capacity constraints and the merit order of generation). We assume identical
cost functions across periods to isolate the role of demand-side heterogeneity in driving price
differences and distributional outcomes. This assumption isolates the effect of heterogeneity
in consumer demand on price variation rather than mixing these effects with those of supply-
side factors.
The planner maximizes total economic surplus by maximizing aggregate consumer surplus
minus electricity procurement costs. Equivalently, we formulate this as minimizing total
Preprint submitted to Energy Policy – please cite published version once available

3 EQUILIBRIUM CHARACTERIZATION
social loss:
L∗ =min
{πt}
X
t∈T
Lt(πt) (7a)
where Lt(πt) = C(d∗ t (πt)) + ˆJt(d∗ t (πt)) (7b)
and d∗ t (πt) = argmin
d∈[0, ¯dt]
{ ˆJt(d) + πtd} (7c)
s.t. πt ≥ 0 ∀t ∈ T (7d)
Here, Lt(πt) represents the social loss in period t, comprising procurement costs and ag-
gregate consumer loss from under-consumption (where ˆJt(d∗ t (πt)) = P i∈N Jit(d∗ it(πt)). The
constraint (7c) reflects that consumers optimally respond to prices by minimizing their in-
dividual loss functions, where ¯dt = P i∈N ¯dit represents aggregate maximum consumption in
period t. Under Assumptions 1 and 2, both C(d) and ˆJt(d) are convex, and the constraint
set is compact, ensuring that Lt is convex in dt and that the planner’s problem has a unique
solution.
Under flat pricing, we add the constraint:
πt = πf for all t ∈ T (8)
We use superscript v to denote variable pricing equilibrium outcomes andf for flat pricing
equilibrium outcomes. The key difference is that variable pricing allows period-specific prices
that reflect marginal costs, while flat pricing uses a single price across all periods.
Since variable pricing does not include the constraint (8), the planner achieves a weakly
lower social loss under variable pricing: Lv ≤ Lf . However, improved aggregate welfare does
not guarantee that all consumers benefit, nor that impacts are distributed equally. Therefore,
our analysis focuses on distributional outcomes, particularly for low-income consumers who
may be most vulnerable to pricing changes.
We introduce notation for changes resulting from the transition from flat to variable
pricing:
∆dt := dv t − df t (change in consumption in period t) (9)
∆πt := πv t − πf (change in price in period t) (10)
∆Uit := U v it − U f it (change in period- t utility for consumer i) (11)
∆Ui := ∆Ui1 + ∆Ui2 (total utility change for consumer i) (12)
In Section 3, we characterize equilibrium prices and consumption under both regimes.
Section 4 then analyzes consumer welfare impacts is examining two key distributional ques-
tions: (1) when does a consumer experience utility losses (∆ Ui < 0), and (2) when do
low-income consumers fare worse than high-income consumers (∆ Ul − ∆Uh < 0)?
3. Equilibrium Characterization
This section characterizes equilibrium solutions under variable and flat pricing, focusing
on how differences in prices, demand, and welfare shape consumer outcomes. A central in-
Preprint submitted to Energy Policy – please cite published version once available

3.1 Equilibrium Properties 3 EQUILIBRIUM CHARACTERIZATION
sight from this section is that the magnitude of price changes depends on the curvature of
the planner’s welfare function. Steeper functions (higher curvature) limit price adjustments,
while flatter functions allow larger ones. Flexibility drives this sensitivity: greater flexibility
in the peak period steepens the welfare function, while inflexibility flattens it and increases
price movements. To demonstrate these effects, we begin by showing the equilibrium condi-
tions under both regimes.
3.1. Equilibrium Properties
Under variable pricing , the planner chooses period-specific prices πv t to minimize social
loss. The first-order conditions require that the marginal effect of a price change on social
welfare equals zero in each period:
∂Lt(πt)
∂πt

πv t
= 0, ∀t ∈ T (13)
Using the chain rule and the definition Lt(πt) = C(d∗ t (πt)) + ˆJt(d∗ t (πt)):
∂Lt
∂πt
=

∂C (dt)
∂dt
+ ∂ ˆJt(dt) ∂dt
!
∂d∗ t (πt)
∂πt
(14)
For interior aggregate demand (0 < dv t < P i ¯dit), Assumption 1 ensures that ˆJ ′ t is strictly
decreasing and therefore invertible, which implies ∂d∗ t ∂πt = − 1 ˆJ ′′ t (d∗ t ) ̸= 0. Therefore, the first-
order condition (13) requires:
∂C (dv t )
∂dt
+ ∂ ˆJt(dv t ) ∂dt = 0 ⇐ ⇒∂C (dv t ) ∂dt = − ∂ ˆJt(dv t ) ∂dt = πv t , (15)
where the final equality uses the aggregate consumer’s first-order condition from Section 2.
This equilibrium condition shows that marginal procurement cost equals marginal avoided
loss, which in turn equals the equilibrium price. This aligns consumer incentives with social
costs: consumers pay exactly the marginal cost of providing additional electricity, ensuring
efficient consumption decisions.
Under flat pricing , consumers still optimize according to (3), so marginal avoided loss
equals the flat price in both periods:
− ∂ ˆJ1(df 1 ) ∂d1 = − ∂ ˆJ2(df 2 ) ∂d2 = πf (16)
However, marginal costs need not equal marginal avoided loss in each period under flat
pricing, since the planner is constrained to use a single price. The planner’s first-order
condition for the constrained problem is:
d
dπf

L1(πf ) + L2(πf )  = 0
Preprint submitted to Energy Policy – please cite published version once available

3.1 Equilibrium Properties 3 EQUILIBRIUM CHARACTERIZATION
This yields:
∂L1(πf )
∂π f + ∂L2(πf ) ∂π f = 0 ⇐ ⇒∂L1(πf ) ∂π f = − ∂L2(πf ) ∂π f (17)
This condition shows that the marginal welfare loss from raising the price in one period
must exactly offset the marginal welfare gain from the same price change in the other period.
This cross-period balancing is the key difference from variable pricing, where each period’s
price independently balances marginal costs and benefits within that period alone. Figure
3 illustrates this equilibrium condition: at the flat price πf , the slopes of the period-specific
welfare functions (shown as tangent lines) are equal in magnitude but opposite in sign,
representing the marginal welfare balance described in (17).
Figure 3 illustrates the equilibrium condition (17). At the flat price πf , the slopes of the
period-specific welfare functions are equal in magnitude but opposite in sign, visualizing the
balance of marginal welfare between periods at the flat price.
π
L(π)
πv 1
L(πv 1 )
L1(πv 1 ) L1(π)
L2(πf )
L2(πv 2 )
πv 2
L(πv 2 )
L2(π)
πf
L(πf )
L(π)
Lf 1 ∂Lf 1 ∂π f
∂Lf 2
∂π f
Figure 3: The planner’s welfare functions by period and pricing regime. The peak period objective L1(π)
(blue) and off-peak period objective L2(π) (red) sum to the total objective L(π) (green). Under variable
pricing, each period’s price independently minimizes its welfare function (πv 1 and πv 2 ). Under flat pricing, the
single price πf balances welfare effects across periods: the tangent lines show that ∂L1 ∂π f = − ∂L2 ∂π f , satisfying
the equilibrium condition (17).
Since the flat pricing problem is simply the variable pricing problem with the additional
constraint (8), we can order the total welfare under the two pricing regimes:
Proposition 2. Under equilibrium conditions, the planner’s loss under variable pricing is
no more than the loss under flat pricing: Lv ≤ Lf .
Under variable pricing, consumers pay the marginal cost of provision, eliminating the
cross-subsidization inherent in flat pricing.
Preprint submitted to Energy Policy – please cite published version once available

3.1 Equilibrium Properties 3 EQUILIBRIUM CHARACTERIZATION
In addition to establishing an order between the operator’s objective under both regimes,
the equilibrium conditions shown in (16)-(17) allow us to understand how a pricing change
impacts each period. We begin by discussing the relationship between equilibrium prices
and quantities under both regimes.
Price Ordering: Using the convexity of Lt and the first-order conditions, we can show
that the flat price lies between the variable prices. Since the cost function C(d) is identical
across periods but demand patterns differ due to consumer preferences (Assumptions 1.b–
1.d), the period with a higher baseline demand (peak) will have a higher variable price to
balance marginal costs and benefits.
Demand Ordering: Since demand is decreasing in price (equation (5)), the price order-
ing directly implies the consumption ordering. Variable pricing reduces peak consumption
and increases off-peak consumption relative to flat pricing.
We provide a detailed characterization in the following proposition, with formal proof in
Appendix C:
Proposition 3. Aggregate prices and demand under both pricing regimes satisfy:
πv 1 ≥ πf ≥ πv 2, d f 2 ≤ dv 2 ≤ dv 1 ≤ df 1
Individual consumer demand orderings depend on their flexibility response to price changes:
Case 1: df i2 ≤ dv i2 ≤ dv i1 ≤ df i1. This occurs when the consumer’s demand remains
greater in the peak period than off-peak under variable pricing.
Case 2: df i2 ≤ dv i1 ≤ dv i2 ≤ df i1. This occurs when the consumer is sufficiently flexible
that their usage pattern reverses and they consume at least as much in the off-peak as
in the peak period.
Economic Interpretation: Flat pricing implicitly subsidizes peak consumption: off-
peak is overpriced relative to marginal cost, and peak is underpriced, leading to inefficient
overuse at peak and underuse off-peak. Variable pricing eliminates this by setting period-
specific prices that reflect true marginal costs.
The distributional implications depend on individual consumption patterns. Consumers
who use relatively more electricity during off-peak periods effectively subsidize those who
consume more during peak periods under flat pricing. The individual demand also reveals
an important insight about flexibility. All consumers reduce peak and increase off-peak
use under variable pricing, but highly flexible consumers may shift so much that off-peak
consumption exceeds peak use, benefiting disproportionately from lower off-peak prices.
Having established the equilibrium price and quantity relationships, we now examine the
magnitude of price changes when switching from flat to variable pricing. The key determinant
is the curvature of the planner’s welfare function Lt(πt). As shown in (17), the flat price
balances marginal welfare effects across periods, but Figure 3 illustrates that the curvature
∂2Lt
∂π 2 dictates how far prices can deviate from this balance. As Figure 3 shows, flatter welfare
functions allow larger price changes, amplifying impact on consumers. We formalize the
relationship between curvature and price changes with the following proposition:
Preprint submitted to Energy Policy – please cite published version once available

3.2 Price Adjustment Analysis 3 EQUILIBRIUM CHARACTERIZATION
Proposition 4. The ratio of price changes when switching from flat to variable pricing is
inversely related to the average curvature of the planner’s welfare functions:
|∆π1|
|∆π2| = ∂2L2 ∂π 2  ∂2L1 ∂π 2
where ∂2Lt ∂π 2 denotes the average second derivative of Lt over the interval between the flat price
and the variable price for period t.
See Appendix C for proof. This result highlights a key trade-off: flatter welfare functions
permit larger price adjustments with smaller welfare penalties, while steeper functions limit
deviations. Thus, consumers with high usage in flatter periods face the largest utility impacts
from pricing reform.
Consumer flexibility plays an important role in determining the curvature of the oper-
ator’s problems, which, in turn, determines the change in prices. Combining the consumer
and planner first-order conditions (16) and (17), yields an expression for πf as a flexibility-
weighted average of marginal procurement costs:
πf =

 ∂df 1 ∂π

 ∂df 1 ∂π

 +

 ∂df 2 ∂π

 · C ′(df 1 ) +

 ∂df 2 ∂π

 ∂df 1 ∂π

 +

 ∂df 2 ∂π

 · C ′(df 2 ), (18)
where the weights are the relative flexibilities of aggregate demand in each period (shown in
Appendix C). This expression demonstrates that the flat price lies closer to the marginal
cost of the period with higher consumer flexibility . As this is evaluated at the flat price
rather than variable prices, we further examine the role of flexibility in determining operator
problem curvature in the next subsection.
3.2. Price Adjustment Analysis
We next expand the second derivative ∂2Lt ∂π 2 t to better understand the relationship between the curvature of the operator’s problem and aggregate consumer flexibility. Using the chain
rule:
∂2Lt
∂π 2 t = ∂ ∂πt
"
∂d∗ t
∂πt
· ∂Lt
∂dt

d∗ t
#
= ∂2d∗ t
∂π 2 t · ∂Lt ∂dt

d∗ t
+
 ∂d∗ t
∂πt
2
· ∂2Lt
∂d2 t

d∗ t
= ∂2d∗ t
∂π 2 t ·
h
C ′(d∗ t ) + ˆJ ′ t(d∗ t ) i +  ∂d∗ t ∂πt 2 · h C ′′(d∗ t ) + ˆJ ′′ t (d∗ t ) i (19)
The first term of (19) involves the second derivative of demand with respect to price,
which relates to flexibility through ∂2dt/∂π 2 t = ˆJ ′′′ t (dt)(∂dt/∂πt)3. The curvature of the
welfare function also depends on aggregate consumer flexibility through the second term,
Preprint submitted to Energy Policy – please cite published version once available

3.2 Price Adjustment Analysis 3 EQUILIBRIUM CHARACTERIZATION
where higher flexibility

 ∂d∗ t ∂πt

 directly increases the curvature. The net effect on curvature
depends on the relative magnitudes and signs of these terms.
Examining the first term of (19), the sign depends on C ′(d∗ t ) + ˆJ ′ t(d∗ t ) as ∂2d∗ t ∂π 2 t > 0. From Proposition 3, we know that at the flat price:
• In the off-peak period: πf ≥ πv 2, so consumption is below the efficient level. This means
C ′(df 2 ) < πf and πf < | ˆJ ′ 2(df 2 )| = − ˆJ ′ 2(df 2 ). Therefore: C ′(df 2 ) + ˆJ ′ 2(df 2 ) < πf − πf = 0.
• In the peak period: πf ≤ πv 1, so consumption exceeds the efficient level. This means
C ′(df 1 ) > πf and πf > | ˆJ ′ 1(df 1 )| = − ˆJ ′ 1(df 1 ). Therefore: C ′(df 1 ) + ˆJ ′ 1(df 1 ) > πf − πf = 0.
The second term is always positive since

∂d∗ t
∂πt
2
> 0 and both C ′′ and ˆJ ′′ t are positive.
This analysis suggests that peak and off-peak flexibility influence curvature differently,
and thus affect price adjustments under variable pricing in different ways. For the peak
period, we can establish that higher flexibility increases curvature. Since both terms in (19)
are positive, and the second term

∂d∗ 1
∂π
2
· [C ′′ + ˆJ ′′ 1 ] increases directly with flexibility

 ∂d∗ 1 ∂π

,
higher peak flexibility unambiguously increases ∂2L1 ∂π 2 . For the off-peak period, the negative
first term and positive second term create offsetting effects, making the net impact of flexi-
bility on curvature ambiguous. Since steeper welfare functions (higher curvature) constrain
the planner’s ability to deviate prices from the flat rate, these curvature effects directly de-
termine the magnitude of price adjustments. To summarize, combining flexibility’s effect on
operator problem curvature with Prop. 4, we can identify the implications of flexibility for
price changes:
• Peak period flexibility: Higher consumer flexibility in the peak period increases the
curvature of the welfare function ∂2L1 ∂π 2 1 , which by Proposition 4 leads to smaller peak
price adjustments |∆π1| and therefore a larger ratio |∆π2|/|∆π1|.
• Off-peak period flexibility: The effect of off-peak flexibility on curvature ∂2L2 ∂π 2 2 remains
ambiguous due to offsetting effects in equation (19). Consequently, the overall impact of
off-peak flexibility on the relative magnitude of price adjustments |∆π2|/|∆π1| cannot
be determined without additional assumptions about the relative magnitudes of the
cost and loss function derivatives.
Together with Proposition 4, these curvature effects map directly into asymmetric peak vs.
off-peak price adjustments. This reveals a key insight: lower consumer flexibility in the
peak period decreases curvature of the operator’s problem and increases price changes. This
counterintuitive result occurs because flexible peak consumers increase the curvature ∂2L1 ∂π 2 1 , making the planner’s welfare function more sensitive to peak price deviations, restricting the
extent to which the peak price can move from the flat rate and forcing larger adjustments in
the off-peak price to maintain the overall balance. This creates complex interactions where
demand-side management programs targeted at flexible consumers may generate spillover
benefits for less responsive consumer groups, as established through the price formation
mechanisms in Section 3. During temperature extremes with low aggregate peak flexibility,
Preprint submitted to Energy Policy – please cite published version once available

4 EFFECTS OF PRICING CHANGE ON CONSUMER UTILITY
peak prices rise sharply. Consumers with below-average flexibility suffer most from large peak
price increases while benefiting little from smaller off-peak decreases. Policymakers should
note when peak demand reflects essential needs (e.g., temperature control for health), since
large peak price increases then have large welfare impacts and may warrant protections.
To summarize, this section established the equilibrium conditions under both pricing
regimes and demonstrated that:
1. Flat prices lie between variable prices: πv 2 ≤ πf ≤ πv 1
2. Cross-subsidization occurs under flat pricing, with redistribution across periods due to
overconsumption in the peak period and underconsumption in the off-peak period.
3. Consumer flexibility determines the magnitude of price changes through curvature
effects
In Section 4, we utilize these equilibrium results to analyze how individual consumers are
affected by the transition from flat to variable pricing, examining both the magnitude and
distribution of welfare changes across different consumer types. We will show that the rela-
tionship between flexibility and price adjustments has important distributional implications.
4. Effects of Pricing Change on Consumer Utility
This section analyzes how the transition from flat to variable pricing affects individual
consumer welfare. We examine the role of individual consumption patterns, flexibility, and
price sensitivity in determining individual welfare changes. The analysis reveals that the
effects of pricing reform are heterogeneous across consumers. Utility changes depend on the
interaction of relative price shifts, consumption, and flexibility. We show that consumers
with high peak demand, low off-peak demand, and little flexibility lose the most, especially
when peak prices rise more than off-peak prices fall. Additionally, price sensitivity scales the
magnitude of changes but not their direction. We develop our theoretical results using general
demand functions, but illustrate the key insights using two specific functional forms: linear
demand (derived from quadratic utility) and isoelastic demand. These examples demonstrate
how our general results apply in commonly used modeling frameworks and provide concrete
illustrations of the distributional effects. Details of both demand functions are provided in
Appendix A.
4.1. Change in Utility When Switching from Flat to Variable Pricing
The total change in utility for consumer i in period t when switching from flat to variable
pricing is ∆ Uit = U v it − U f it. Using the envelope theorem and equation (6), this can be
expressed as:
∆Uit =
Z πv t
πf
∂Uit(πt)
∂πt
dπt = −
Z πv t
πf
Aid∗ it(πt)dπt. (20)
This integral represents the change in consumer surplus over the price interval, scaled by
price sensitivity. We can then find the total change in utility of a consumer by summing
(20) across both periods:
∆Ui = ∆Ui1 + ∆Ui2
Preprint submitted to Energy Policy – please cite published version once available

4.1 Change in Utility When Switching from Flat to Variable Pricing 4 EFFECTS OF PRICING CHANGE ON CONSUMER UTILITY
Hence, the total utility change depends on the consumer’s consumption profile across periods
and the relative magnitude of price changes in each period.
Figure 4 illustrates the geometric interpretation of utility changes for consumer i. The
figure plots demand curves for both periods, with price on the vertical axis and quantity
(scaled by Ai) on the horizontal axis. Based on equation (20), we note:
- The red shaded area between πf and πv 1 represents the utility loss |∆Ui1| from higher
peak prices
- The blue shaded area between πv 2 and πf represents the utility gain ∆ Ui2 from lower
off-peak prices
Aidit
π
(Aid∗ i1(π), π)
(Aid∗ i2(π), π)
πf
πv 2
πv 1πv 1
Figure 4: Consumer utility changes from switching to variable pricing. The red area shows utility loss
from higher peak prices ( |∆Ui1|), while the blue area shows utility gain from lower off-peak prices (∆ Ui2).
Net utility loss occurs when the red area exceeds the blue area. The crosshatched region represents the
conservative lower bound on peak utility loss used in condition (22), while the gridded region represents
the conservative upper bound on off-peak utility gain, illustrating how the linear demand condition provides
sufficient conditions through these approximations used in Theorem 5.
Consumer i experiences a net utility loss when the red area (peak period loss) exceeds the
blue area (off-peak period gain). This occurs when the consumer has: (i) High peak period
consumption relative to off-peak consumption; or (ii) Low flexibility (steep demand curves
that create large areas for given price changes), or (iii) Exposure to periods where price
increases are large relative to price decreases. In practice, consumers are most vulnerable
when they exhibit multiple of these characteristics simultaneously, but any single factor can
be sufficient for net utility losses if it is pronounced enough.
We now formalize these intuitions and identify the conditions under which consumers
lose utility from pricing reform. Recall that from (5), ∂d∗ it ∂πt = −Ai ˆJ ′′ it(d∗ it) . From Assumption 1, ˆJ ′′′ it (d∗ it) < 0, which implies that ˆJ ′′ it is decreasing in consumption. Since higher prices reduce
consumption, ˆJ ′′ it increases with price, causing flexibility

 ∂d∗ it ∂πt

 = Ai ˆJ ′′ it(d∗ it) to decrease as price increases. This establishes that demand curves are convex.
Flexibility Bounds: Since demand curves are convex (flexibility decreases with price):
Preprint submitted to Energy Policy – please cite published version once available

4.1 Change in Utility When Switching from Flat to Variable Pricing 4 EFFECTS OF PRICING CHANGE ON CONSUMER UTILITY
• In the peak period: Since πv 1 ≥ πf , flexibility ranges from highest at πf to lowest at πv 1
• In the off-peak period: Since πf ≥ πv 2, flexibility ranges from highest at πv 2 to lowest at
πf
These bounds allow us to construct conservative estimates in Theorem 5 by evaluating
flexibility at the most favorable points for the consumer.
Demand Bounds: Since demand decreases with price:
• Peak consumption: decreases from df i1 (at lower price πf ) to dv i1 (at higher price πv 1)
• Off-peak consumption: increases from df i2 (at higher price πf ) to dv i2 (at lower price πv 2)
These bounds allow us to establish sufficient conditions for utility loss by finding the extreme
cases. If a consumer loses utility even under the most favorable assumptions about their
flexibility and consumption levels, they will certainly lose utility under actual conditions.
Theorem 5. Consumer i’s total utility change under a switch from flat to variable pricing
is:
∆Ui = Ai

−
Z πv 1
πf
d∗ i1(πt)dπt +
Z πf
πv 2
d∗ i2(πt)dπt
!
(21)
Consumer i experiences a utility loss ( ∆Ui < 0) under the following conditions:
(a) Linear Demand:If and only if:
(|∆π2|df i2 − |∆π1|df i1) + (∆π1)2 2

 ∂df i1 ∂π1

 + (∆π2)2 2

 ∂dv i2 ∂π2

 < 0 (22)
(b) Isoelastic Demand:If and only if:
df i1
1 + ϵf i1
"
1 −
 πv 1
πf
1+ϵf i1 #
+ df i2
1 + ϵf i2
"
1 −
 πv 2
πf
1+ϵf i2 #
< 0 (23)
Applicability and interpretation of conditions: The linear demand condition (22) is
necessary and sufficient under two scenarios: when Jit is quadratic (yielding linear demand),
where the convexity bounds used in the derivation become equalities, and when consumer
flexibility approaches zero ( ˆJ ′′ it → ∞) in both periods, where the quadratic flexibility terms
vanish and the condition reduces to purely consumption-weighted price changes: (|∆π2|df i2 −
|∆π1|df i1) < 0.
The isoelastic condition (23) provides a necessary and sufficient condition for ∆ Ui < 0
when demand is isoelastic. The 1 1+ϵf it

1 −

πv t
πf
1+ϵf it  terms capture the interaction between
elasticity and price changes. This becomes clearer in the alternative formulation of (21):
∆Ui = −
Z πv 1
πf
df i1 ·  π1 πf ϵf i1 · dπ1 + Z πf πv 2 df i2 ·  π2 πf ϵf i2 dπ2, (24)
Preprint submitted to Energy Policy – please cite published version once available

4.1 Change in Utility When Switching from Flat to Variable Pricing 4 EFFECTS OF PRICING CHANGE ON CONSUMER UTILITY
which shows that utility change increases in |ϵit|. Like flexibility in the linear case, elasticity
has a uniformly positive impact on the change in utility.
For general demand functions that are neither linear nor isoelastic, the linear demand
condition provides a conservative screening test:
Corollary 6. Under Assumption 1, if condition (22) holds for consumer i, then they expe-
rience a utility loss ( ∆Ui < 0) from the pricing change regardless of the specific functional
form of their loss functions Ji1 and Ji2.
Condition (22) is sufficient because it uses conservative bounds that underestimate the
welfare benefits of flexibility. Since the convexity bounds become equalities for linear demand
and inequalities otherwise, any consumer satisfying condition (22) will experience utility
losses under their actual demand curve. The areas used for condition (22) are illustrated in
Figure 4, where the crosshatched region shows how the utility loss is lower bounded using
the slope of the demand curve (reciprocal of flexibility) and the demand at the flat price.
The gridded region shows how utility gain is upper bounded using demand at the flat price
and flexibility at the variable price. The generality of these bounds makes condition (22) a
valuable screening tool: policymakers can identify consumers who will definitely lose from
pricing reform, even without knowing the exact functional form of their demand curves.
Economic interpretation: Both conditions decompose utility changes into four distinct
effects:
1. Consumption Level Effects: The terms (|∆π2|df i2 − |∆π1|df i1) capture the direct impact
of price changes on consumers’ flat-rate consumption levels. This represents what would
happen if consumers could not adjust their consumption in response to price changes—pure
incidence effects based on existing consumption patterns.
2. Flexibility Effects: The quadratic terms (∆πt)2 2 | ∂df it ∂πt | (linear case) or elasticity-weighted terms (isoelastic case) capture second-order welfare effects from consumers’ ability to adjust
consumption in response to price changes. These terms represent the welfare value of demand
responsiveness—the benefit consumers derive from being able to partially offset adverse price
changes through consumption adjustments.
3. Price sensitivity effects: From (21), Ai scales the magnitude of utility changes: more
sensitive consumers experience larger gains or losses from the same price shift. This scaling
effect becomes crucial when comparing low- and high-income consumers.
4. Relative price change effects: As |∆π1| increases relative to |∆π2|, the balance shifts
toward utility losses. The term ( |∆π2|df i2 − |∆π1|df i1) becomes more negative as peak price
increases dominate off-peak price decreases. This means consumers are worse off when peak
period price adjustments are large relative to off-peak adjustments, independent of their
flexibility.
Policy Implications: The decomposition in (22) shows that flexibility mitigates losses
(or enhances gains). However, the quadratic terms (∆πt)2 2 | ∂df it ∂πt | demonstrate that demand responsiveness has differential value depending on timing. Those flexible only during periods
with small price changes gain little additional protection since the flexibility terms remain
negligible. However, consumers who are flexible during periods with large price changes
benefit substantially as the quadratic terms provide significant welfare protection through
Preprint submitted to Energy Policy – please cite published version once available

4.2 Difference in Change of Utility Between Consumers 4 EFFECTS OF PRICING CHANGE ON CONSUMER UTILITY
consumption adjustments. Consumers who are inflexible in both periods face utility changes
determined purely by consumption-weighted price differences ( |∆π2|df i2 − |∆π1|df i1).
These results suggest two sets of policies for different consumer types. Policies that
directly promote demand responsiveness, such as smart meter deployment, time-varying
rate education, or flexible appliance adoption, should be prioritized for consumers who lack
flexibility due to technical limitations. However, a different set of policies may be needed
for consumers who have very different levels of flexibility between periods or who remain
inflexible after technical limitations have been addressed. These consumers are more likely
to be trapped between negative health impacts from foregone electricity consumption and
high electricity bills. It is not the ability to decrease consumption that is limiting their
response, but the negative effects of doing so. Here, targeted protection mechanisms such
as bill assistance programs, gradual rate transitions, or programs to insulate homes may be
more effective.
4.2. Difference in Change of Utility Between Consumers
We now derive conditions under which the low-income consumer loses more utility than
the high-income consumer from pricing reform.
Proposition 7. The difference in utility changes between high-income and low-income con-
sumers is:
∆Uh − ∆Ul =
Z πv 1
πf
(Ald∗ l1(π) − Ahd∗ h1(π))dπ +
Z πf
πv 2
(Ahd∗ h2(π) − Ald∗ l2(π))dπ (25)
The low-income consumer loses more utility ( ∆Ul < ∆Uh) if and only if the following con-
ditions hold:
Linear Demand:
Al

(|∆π2|df l2 − |∆π1|df l1) + (∆π1)2 2

 ∂df l1 ∂π

 + (∆π2)2 2

 ∂dv l2 ∂π

 !
< Ah

(|∆π2|df h2 − |∆π1|df h1) + (∆π1)2 2

 ∂dv h1 ∂π

 + (∆π2)2 2

 ∂df h2 ∂π

 ! (26)
Isoelastic Demand:
Al

df l1
1 + ϵl1
"
1 −
 πv 1
πf
1+ϵl1 #
+ df l2
1 + ϵl2
"
1 −
 πv 2
πf
1+ϵl2 #!
< Ah

df h1
1 + ϵh1
"
1 −
 πv 1
πf
1+ϵh1 #
+ df h2
1 + ϵh2
"
1 −
 πv 2
πf
1+ϵh2 #!
(27)
Proposition 7 provides conditions under which low-income consumers experience worse
utility changes than high-income consumers under variable pricing reform. The linear de-
mand condition is necessary and sufficient when consumer demand is linear (quadratic utility)
and in the limit where flexibility approaches zero ( ˆJ ′′ it → ∞). This latter case corresponds to
Preprint submitted to Energy Policy – please cite published version once available

4.2 Difference in Change of Utility Between Consumers 4 EFFECTS OF PRICING CHANGE ON CONSUMER UTILITY
studies that only consider the change in incidence for consumers at a fixed historical demand.
The linear demand condition provides a conservative test for identifying when pricing re-
form will disproportionately harm low-income consumers for general demand functions that
satisfy Assumption 1.
Corollary 8. Under Assumption 1, if condition (26) holds, then low-income consumers lose
more utility than high-income consumers ( ∆Ul < ∆Uh) from the pricing change, regardless
of the specific functional forms of their loss functions Jl1, Jl2, Jh1, and Jh2.
As with Corollary 6, this condition uses convexity bounds to ensure reliable screening
across all demand functions satisfying Assumption 1. To establish conservative bounds, we
lower bound low-income consumer welfare losses (making their situation appear better) while
upper bounding high-income consumer welfare losses (making their situation appear worse),
ensuring the sufficient condition is robust.
The interpretation of Proposition 7 mirrors that of Theorem 5:
• Consumers fare better relative to others when their consumption is less concentrated
in the peak (i.e., relatively more off-peak demand).
• When high-income consumers are more flexible than low-income consumers, they ben-
efit from price decreases and are hurt less by price increases, as the ability to reduce
peak consumption and increase off-peak consumption results in greater cost savings
relative to low-income consumers.
• As with individual utility analysis, the timing of flexibility matters: consumers benefit
when aggregate peak flexibility is high (constraining peak price increases) and when
they personally can adjust during periods with large price changes, as shown by the
squared price terms in (26).
Consumer price sensitivity plays a crucial role in both conditions of Proposition 7. The
ratio Al/Ah > 1 acts as a multiplier that amplifies the relative impact of pricing changes
on low-income consumers’ utility. Because low-income consumers have a higher marginal
disutility of expenditure ( Al > Ah), they experience larger utility changes from any given
pricing reform, even when consumption patterns and flexibility are held constant. When
consumers have substantially different price sensitivities, a pricing change can have dis-
proportionately large impacts on low-income households while barely affecting high-income
consumers. This creates an inherent distributional asymmetry in electricity pricing policy:
reforms that appear modest in aggregate can impose significant welfare costs on vulnerable
populations. Consequently, rate-makers implementing variable pricing should recognize that
these changes may have outsized impacts on low-income consumers and consider comple-
mentary measures—such as targeted bill assistance or gradual rate transitions—to mitigate
potential distributional harms.
For isoelastic demand, condition (27) shows that elasticity parameters mediate the impact
of price changes on relative welfare outcomes, with higher elasticity allowing consumers to
better adjust to price changes and providing advantages in the distributional comparison
similar to flexibility benefits in the linear demand case.
Preprint submitted to Energy Policy – please cite published version once available

5 MODEL EXTENSIONS
These results demonstrate that distributional outcomes from variable pricing depend crit-
ically on the interaction between individual consumption patterns, flexibility characteristics,
and aggregate market responses. The conditions derived provide policymakers with analyt-
ical tools for identifying vulnerable consumer groups before implementing pricing reforms.
5. Model Extensions
While Sections 2-4 consider a model with only two periods, two consumers, and no profit
restrictions, the core results generalize under more complex settings. In this section, we
discuss how our model extends to (1) incorporate profit constraints and (2) account for
arbitrarily many periods and consumers. In the following, we present a concise version of
our results. For the full proofs, please see Appendix E.
5.1. Profit Constraints in Variable Pricing Implementation
Real-world implementations of variable pricing face regulatory constraints requiring util-
ities to maintain financial viability while transitioning from flat-rate structures. Unlike our
baseline model, where the social planner freely optimizes welfare through marginal cost
pricing, utility regulators typically mandate that pricing reforms satisfy revenue adequacy
requirements or predetermined profit levels. These constraints ensure recovery of sunk in-
frastructure investments while addressing political economy concerns about utility earnings
under rate restructuring. While such requirements move prices away from first-best welfare
outcomes, they better reflect practical policy implementation constraints.
To analyze how profit constraints reshape equilibrium pricing and consumer outcomes, we
extend the baseline operator problem in (7a)-(7d) to include an explicit profit requirement.
We constrain total profit to equal a predetermined level ¯P , such as the profit under flat
pricing: P t∈T dt(πf ) · πf − C(dt(πf )). The modified optimization problem becomes:
L∗ =min
{πt}
X
t∈T
Lt(πt) (28a)
where Lt(πt) = C(d∗ t (πt)) + ˆJt(d∗ t (πt)) and d∗ t (πt) = argmin
d∈[0, ¯dt]
{ ˆJt(d) + πtd} ∀t ∈ T (28b)
s.t. πt ≥ 0 ∀t ∈ T (28c)X
t∈T
Pt(πt) = ¯P , (28d)
where Pt(πt) = d∗ t (πt)πt − C(d∗ t (πt)) represents period- t profit. The Lagrangian for this
problem is:
L =
X
t
Lt(πt) + ν
 X
t
Pt(πt) − ¯P
!
. (29)
Let π∗ t denote the optimal price in period t for the profit-constrained operator problem.
Preprint submitted to Energy Policy – please cite published version once available

5.2 Extension to Many Consumers and Periods 5 MODEL EXTENSIONS
Taking the first-order condition from the Lagrangian (29) with respect to πt yields:
(C ′(d∗ t ) − π∗ t ) + ν

1 + 1 ϵt

π∗ t − C ′(d∗ t )

= 0, (30)
where ν is the Lagrange multiplier associated with the profit constraint and ϵt < 0 is the
price elasticity of demand in period t.
Rearranging equation (30) gives:
ν
1 − ν = π∗ t − C ′(d∗ t ) π∗ t /ϵt . (31)
Since ν is constant across periods, equating expressions for any two periods t and t′ yields
the ratio of price distortions:
π∗ t − C ′(d∗ t )
π∗ t′ − C ′(d∗ t′) = π∗ t /ϵt π∗ t′/ϵt′ . (32)
This shows that price distortions from marginal cost are inversely related to demand elastic-
ity, with less elastic periods experiencing larger markups under binding profit constraints.
The direction of price adjustment depends on whether the required profit level binds
above or below the unconstrained optimum:
1. Revenue adequacy constraint: If ¯P >P t∈T [πv t dv t −C(dv t )] (requiring higher profits than
welfare-optimal pricing generates), then π∗ t > πv t in all periods to increase total profit.
2. Profit limitation constraint: If ¯P < P t∈T [πv t dv t − C(dv t )] (capping profits below the
welfare-optimal level), then π∗ t < πv t in all periods to reduce total profit.
Since price distortions are inversely related to demand elasticity, periods with less elas-
tic demand experience larger deviations from marginal cost pricing under binding profit
constraints.
The distributional implications follow directly from our main results in Section 4. The
sufficient conditions in Theorem 5 remain valid with profit-constrained prices π∗ t substituted
for unconstrained prices πv t . Revenue adequacy constraints that increase price deviations
will expand the set of consumers satisfying the loss condition, while profit caps that reduce
price deviations will contract this set. The consumer characteristics that determine vul-
nerability—consumption timing, flexibility, and price sensitivity—remain the same, but the
magnitude of distributional effects changes with the binding profit constraint.
5.2. Extension to Many Consumers and Periods
Our model readily accommodates more than two consumers since the aggregate con-
sumer properties (Assumption 1 and equations (3)-(5)) hold for any number of consumers.
The distributional analysis extends to comparisons across consumer quantiles or relative to
population means rather than simple pairwise comparisons.
Preprint submitted to Energy Policy – please cite published version once available

6 DISCUSSION
For multiple time periods, the key results generalize with appropriate notation changes.
The flat price remains a flexibility-weighted average of marginal costs:
πf =
P
t∈T C ′(dt(πf ))

 ∂dt ∂π

 πf P
t∈T

 ∂dt
∂π

πf
(33)
The sufficient conditions for utility loss extend by summing across all periods, maintaining
the same form as our two-period analysis. Complete proofs are provided in Appendix E.
6. Discussion
Our theoretical framework identifies conditions under which consumer heterogeneity cre-
ates systematic patterns of winners and losers under variable electricity pricing reforms.
Theorem 5 and Proposition 7 demonstrate that consumers most vulnerable to utility losses
from variable pricing exhibit predictable characteristics: high consumption during peak pe-
riods, limited consumption during off-peak periods, and inflexible demand during periods
with large price changes. Empirical studies such as Horowitz and Lave (2014) and Borenstein
(2012) find that this vulnerability profile often corresponds to households with limited eco-
nomic resources, older housing stock, or constrained ability to shift electricity usage across
time periods.
Conversely, consumers who benefit from pricing reforms typically have more balanced
consumption profiles and greater flexibility to respond to price incentives. While these
characteristics are more often associated with higher-income households that have better
appliances and housing stock, our theoretical framework demonstrates that the underlying
consumption and flexibility patterns matter more than income categories per se.
6.1. Empirical Literature and Theoretical Insights
Much of the empirical literature on variable pricing impacts predominantly relies on simu-
lation studies that impose constant elasticity assumptions across consumers and time periods
(Burger et al., 2020; Horowitz and Lave, 2014; Simshauser and Downer, 2016; Borenstein,
2007). While these studies provide valuable insights into aggregate demand response, the
constant elasticity approach obscures two critical sources of heterogeneity that our analysis
shows are fundamental to distributional outcomes: variation in flexibility across consumer
groups and variation in flexibility across time periods for individual consumers.
The empirical literature’s conflicting findings on distributional impacts can be understood
through our theoretical lens. Studies finding that low-income consumers are harmed by vari-
able pricing typically examine contexts where these consumers have peak-dominated con-
sumption profiles—such as heating-intensive usage in cold climates—combined with limited
flexibility during high-price periods (Horowitz and Lave, 2014). Conversely, studies find-
ing benefits for low-income consumers analyze settings where these consumers have more
balanced consumption profiles across time periods (Simshauser and Downer, 2016). Our
theoretical results explain these divergent empirical findings: it is not income per se that
determines outcomes, but rather the interaction between consumption patterns, flexibility
capabilities, and the specific pattern of price changes across periods.
Preprint submitted to Energy Policy – please cite published version once available

6.2 Methodological Considerations and Limitations 6 DISCUSSION
The constant elasticity assumption used in simulation studies creates an artificial link
between baseline consumption and demand responsiveness, meaning that consumers’ flexibil-
ity patterns mechanically mirror their consumption patterns. However, our analysis demon-
strates that if flexibility and consumption patterns are not completely dependent, each plays
an important role in determining distributional outcomes. For example, a consumer with
high peak consumption might have flexibility concentrated in off-peak periods (due to work
schedules, appliance constraints, or housing characteristics), leading to very different welfare
outcomes than would be predicted by uniform elasticity assumptions. Proposition 7 shows
that distributional outcomes depend on how each consumer group’s flexibility aligns with
the pattern of price changes across periods. Consumers who are flexible during periods with
small price adjustments gain little benefit, while those who can adjust consumption dur-
ing periods with large price changes receive substantial welfare benefits. This suggests that
empirical evaluations of variable pricing programs should incorporate more sophisticated
representations of heterogeneous demand response capabilities, particularly when assessing
equity implications.
Beyond reconciling empirical findings, the equilibrium analysis reveals a spillover effect
operating through the pricing mechanism: individual flexibility contributes to aggregate
demand flexibility, which in turn affects the curvature of the planner’s welfare function
and the magnitude of price adjustments across periods (Proposition 4). This creates a
counterintuitive result: when consumers are highly flexible in peak periods, the planner
constrains peak price increases because small price deviations cause large welfare losses
when consumption changes drastically. Conversely, when peak flexibility is low, prices can
rise substantially without triggering major demand shifts, leading to larger price increases
that disproportionately harm inflexible consumers.
Price sensitivity ( Ai), and its role in encouraging flexibility create a tension inherent in
encouraging demand response. Higher price sensitivity enables greater demand flexibility,
which can provide welfare protection. Simultaneously, price sensitivity also amplifies the
utility impacts of any pricing change. Low-income consumers, who tend to have higher Ai,
are more heavily affected by pricing reforms regardless of their flexibility or usage profile,
leaving them systematically more vulnerable to adverse changes and greater beneficiaries of
positive ones.
This amplification effect has implications for energy justice. When low-income con-
sumers are less flexible than high-income consumers during periods experiencing large price
increases—a common scenario given differential access to well-insulated housing and health
needs—they face a double burden: they face a higher loss from foregone electricity use when
adjusting consumption, and their higher price sensitivity magnifies the welfare impact of
those changes.
6.2. Methodological Considerations and Limitations
Our analysis uses utility rather than consumer surplus as the primary welfare measure
to capture broader impacts of electricity access on household well-being. Consumer surplus,
calculated by normalizing utility by the marginal disutility of expenditure ( Ai), measures
welfare changes in terms of willingness to pay and facilitates interpersonal comparisons by
expressing all impacts in monetary units. However, this approach may be inadequate for
evaluating policies affecting essential services like electricity, where foregone consumption
Preprint submitted to Energy Policy – please cite published version once available

6.2 Methodological Considerations and Limitations 6 DISCUSSION
can have serious health and safety consequences that extend beyond consumers’ revealed
willingness to pay. The choice of welfare measure has particular importance for energy
justice analysis. When low-income households reduce electricity consumption in response
to price increases, the welfare loss encompasses not just the monetary burden but also the
health impacts of inadequate heating or cooling (Anderson et al., 2012; Cong et al., 2022; Shi
et al., 2024). We highlight temperature control, but other impacts, include the educational
consequences of insufficient lighting and the social isolation caused by the inability to power
communication devices, are worthy of attention as well. Our utility-based approach captures
these broader welfare impacts while maintaining analytical tractability, with the parameter
Ai representing not just price sensitivity but also the relative importance of electricity versus
other goods in each consumer’s welfare function. This methodological choice aligns with
growing recognition in energy policy that traditional economic metrics may inadequately
capture the stakes involved in electricity access for vulnerable populations.
Our analysis prioritizes distributional precision over supply-side complexity, making sev-
eral simplifying assumptions that highlight opportunities for future research while preserving
the core insights about consumer heterogeneity and equity. The most significant simplifi-
cation is our focus on short-run marginal costs, which abstracts from fixed cost recovery,
capacity payments, and long-term investment incentives. This choice reflects both analyti-
cal tractability and the extensive existing literature on these topics (Borenstein and Bush-
nell, 2022; Burger et al., 2020; Borenstein, 2005; Joskow and Tirole, 2006, 2007), which has
established efficient mechanisms for recovering non-marginal costs through various pricing
structures.
However, combining our heterogeneous consumer framework with realistic fixed cost re-
covery represents an important avenue for future research, particularly as utilities increas-
ingly face pressure to recover grid modernization investments while maintaining equitable
rate structures. The interaction between distributional concerns and cost recovery methods,
such as capacity charges, connection fees, or progressive rate structures, could significantly
affect the welfare impacts we identify. Similarly, incorporating investment in demand re-
sponse technologies and grid infrastructure could reveal how capital cost allocation affects
the distribution of variable pricing benefits.
Our exclusion of supply cost variation, while analytically convenient, may understate
the distributional challenges of variable pricing in practice. As electricity systems integrate
higher shares of renewable energy, the variation in net load between peak and off-peak periods
is likely to increase (Chao, 2010), amplifying the price differences that drive our distributional
results. Climate policies promoting renewable integration may thus intensify the equity
challenges we identify, making our findings increasingly policy-relevant as decarbonization
accelerates.
Our assumption of perfect price responsiveness, while providing an upper bound on de-
mand flexibility benefits, may actually understate risks to low-income consumers. Limited
access to smart appliances, home automation systems, and flexible work arrangements means
that low-income households often cannot fully respond to price signals even when they un-
derstand them (Calver and Simcock, 2021). Future research incorporating these realistic
constraints on demand response would likely find even larger distributional disparities, re-
inforcing our key finding that variable pricing requires complementary policies to protect
vulnerable populations.
Preprint submitted to Energy Policy – please cite published version once available

6.3 Policy Implications 6 DISCUSSION
6.3. Policy Implications
The conditions we derive reveal that successful variable pricing programs must go beyond
promoting aggregate demand response to ensure that flexibility capabilities are equitably
distributed across consumer groups. Policies that enhance demand flexibility only among
high-income consumers may inadvertently worsen distributional outcomes by creating larger
welfare gaps between consumer groups. Understanding the spillover effects through price
formation is crucial for designing equitable variable pricing programs and complementary
policies to protect vulnerable populations.
Our results demonstrate that standard variable pricing implementations risk exacerbat-
ing energy inequality unless accompanied by targeted policy interventions. Several policy
mechanisms can preserve the efficiency benefits of marginal cost pricing while protecting
vulnerable consumers from adverse distributional impacts.
Rate Design Modifications: Progressive block pricing structures can address both
volumetric inefficiencies and equity concerns by incorporating consumer income or historical
usage patterns into rate design (Burger et al., 2020; Borenstein, 2008). Opt-in variable pricing
programs offer another pathway that maintains system benefits while providing consumer
protection (Borenstein, 2007; Gambardella and Pahle, 2018).
Technology Access and Infrastructure: Beyond rate design modifications, com-
plementary technology and assistance programs are essential for equitable variable pricing
implementation. Subsidized access to smart thermostats, programmable appliances, and bat-
tery storage can democratize demand flexibility capabilities, while targeted bill assistance
during high-price periods can provide safety nets for vulnerable households.
Targeted Protection Measures: Demand response initiatives targeting vulnerable
populations should prioritize measures not directly tied to demand response, such as insula-
tion investments and assistance with healthcare during temperature extremes. This should
be done not just because of fairness concerns, but because it will help these consumers reduce
electricity consumption when it is expensive for society to produce.
The key insight from our analysis is that successful variable pricing requires coordinated
policy packages that address both individual flexibility constraints and the systemic factors
that concentrate benefits among already-advantaged consumers. The distributional chal-
lenges identified in our analysis stem from a fundamental tension in electricity policy: the
increasing need for demand flexibility to support renewable energy integration and grid re-
liability conflicts with the potential for time-varying prices to harm vulnerable populations.
As electrification accelerates and intermittent renewables compose larger shares of the gen-
eration mix, peak demand management becomes increasingly critical, making some form of
dynamic pricing essential for system efficiency.
Acknowledgements
We thank the MIT Portugal Program and the IDSS Initiative for Combatting Sys-
temic Racism for financial support of this research. We also gratefully acknowledge support
from the MIT UROP program, which enabled undergraduate research contributions to this
project.
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX A LINEAR AND ISOELASTIC DEMAND FUNCTIONS
Appendix A. Linear and Isoelastic Demand Functions
Linear Demand (Quadratic Utility) Linear demand arises from quadratic utility
functions of the form: r
Uit = kit ¯d2 it − kit( ¯dit − dit)2 − Aiπtdit
where kit > 0 measures consumer i’s sensitivity to electricity shortfalls in period t, and ¯dit
represents the consumer’s ideal consumption level. This specification, commonly used in
demand response models (Deng et al., 2015), yields the loss function:
Jit(dit) = kit( ¯dit − dit)2
with derivatives ∂Jit ∂dit = −2kit( ¯dit − dit) and ∂2Jit ∂d2 it = 2kit. The resulting optimal demand is:
d∗ it(πt) = min

max

¯dit − Aiπt
2kit
, 0

, ¯dit

For interior solutions, this yields linear demand with flexibility

 ∂d∗ it ∂πt

 = Ai 2kit .
Isoelastic Demand Standard isoelastic demand functions exhibit constant price elas-
ticity:
dit(πt) = df it
 πt
πf
ϵit
where df it is consumption at the reference price πf , and ϵit < 0 is the constant price elasticity.
However, pure isoelastic demand creates integrability issues at extreme prices.
Piecewise Specification: To ensure analytical tractability while maintaining isoelastic
properties over relevant price ranges, we use the following piecewise specification:
dit(πt) =



df it  πt πf ϵit if πlow ≤ πt ≤ πhigh
d(πhigh) − mhigh · (πt − πhigh) if πt > πhigh
d(πlow) + mlow · (πt − πlow) if πt < πlow
(A.1)
where the boundary values and slopes ensure continuity:
Upper boundary ( πt > πhigh):
d(πhigh) = df it
 πhigh
πf
ϵit
(A.2)
mhigh = ϵit · df it
 πhigh
πf
ϵit−1
· 1 πf (A.3)
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX B SECTION 2 PROOFS
Lower boundary ( πt < πlow):
d(πlow) = df it
 πlow
πf
ϵit
(A.4)
mlow = ϵit · df it
 πlow
πf
ϵit−1
· 1 πf (A.5)
This construction ensures that both the demand function and its derivative are continuous
at the boundary points πlow and πhigh. By setting these thresholds sufficiently far from the
relevant price range (e.g., πlow = 0 .01 · πf and πhigh = 100 · πf ), the linear regions have
negligible impact on the analysis while ensuring integrability.
Properties: In the isoelastic region, the price elasticity is:
ϵit = d ln dit
d ln πt
= ϵit
and the flexibility is:

 ∂dit ∂πt

 = |ϵit|df it πf  πt πf ϵit−1
Relationship Between Functional Forms Both specifications satisfy Assumption 1
regarding convexity and monotonicity. The key difference lies in flexibility patterns. Linear
demand exhibits constant flexibility

 ∂d∗ it ∂πt

 = Ai 2kit while isoelastic demand exhibits price-
dependent flexibility that varies with price level.
Appendix B. Section 2 Proofs
We derive the KKT conditions for the consumer and planner problems. Because the
consumer problem is a convex optimization problem that satisfies Slater’s condition, the KKT
conditions provide necessary and sufficient conditions for optimality Boyd and Vandenberghe
(2004).
Appendix B.1. Consumer Problem
Proof of (3) and Proposition 1
Proof. The objective function Jit(dit) Ai +πtdit is convex in dit since Jit is convex by Assumption
1 and positive scaling preserves convexity, while πtdit is linear. The constraint set [0 , ¯dit] is
convex and compact. For any dit ∈ (0, ¯dit), both inequality constraints are satisfied with
strict inequality, so Slater’s condition holds. Therefore, the KKT conditions are necessary
and sufficient for optimality.
The Lagrangian is:
L(dit, λ1 it, λ2 it) = Jit(dit) Ai + πtdit − λ1 itdit + λ2 it(dit − ¯dit)
Preprint submitted to Energy Policy – please cite published version once available

Appendix B.1 Consumer Problem APPENDIX B SECTION 2 PROOFS
The KKT conditions are:
Stationarity: 1 Ai ∂Jit ∂dit

d∗ it
+ πt − λ1 it + λ2 it = 0 (B.1)
Primal feasibility: 0 ≤ d∗ it ≤ ¯dit (B.2)
Dual feasibility: λ1 it, λ2 it ≥ 0 (B.3)
Complementary slackness: λ1 itd∗ it = 0, λ 2 it( ¯dit − d∗ it) = 0 (B.4)
Case 1: Interior solution (0 < d∗ it < ¯dit) Both constraints are slack, so λ1 it = λ2 it = 0. The
stationarity condition gives:
∂Jit
∂dit

d∗ it
= −Aiπt
Since J ′ it < 0 and strictly decreasing by Assumption 1, the inverse function exists and:
d∗ it = (J ′ it)−1(−Aiπt) = ( ˆJ ′ it)−1(−πt)
Case 2: Boundary solutions
- If d∗ it = 0: then λ1 it ≥ 0 and λ2 it = 0
- If d∗ it = ¯dit: then λ1 it = 0 and λ2 it ≥ 0
Combining all cases yields the characterization in (4).
Proof of (5)
Proof. We compute the derivative ∂d∗ it(πt) ∂πt for each case in the demand function (4).
Interior case: For d∗ it(πt) ∈ (0, dit), we have d∗ it(πt) =  J ′ it Ai −1 (−πt). Using the inverse
function theorem:
∂d∗ it(πt)
∂πt
= ∂ ∂πt
" J ′ it
Ai
−1
(−πt)
#
(B.5)
= 1
J ′ it
Ai
′
(d∗ it(πt))
· (−1) (B.6)
= 1 J ′′ it(d∗ it(πt))
Ai
· (−1) (B.7)
= −Ai
J ′′ it(d∗ it(πt)) (B.8)
Since J ′′ it > 0 by Assumption 1, this derivative is negative.
Boundary cases:
Preprint submitted to Energy Policy – please cite published version once available

Appendix B.1 Consumer Problem APPENDIX B SECTION 2 PROOFS
- When d∗ it(πt) = dit, demand is constrained at the maximum, so ∂d∗ it ∂πt = 0
- When d∗ it(πt) = 0, demand is constrained at zero, so ∂d∗ it ∂πt = 0
Combining all cases yields the derivative formula in (5).
Demand is strictly convex if and only if the third derivative of the electricity loss function
is negative:
∂2d∗ it(πt)
∂π 2 t > 0 ⇐ ⇒J ′′′ it (d∗ it(πt)) < 0. (B.9)
Proof. For interior solutions where d∗ it(πt) ∈ (0, ¯dit), we differentiate (5):
∂2d∗ it(πt)
∂π 2 t = ∂ ∂πt
 −Ai
J ′′ it(d∗ it(πt))

(B.10)
= AiJ ′′′ it (d∗ it(πt)) (J ′′ it(d∗ it(πt)))2 · ∂d∗ it ∂πt (B.11)
= AiJ ′′′ it (d∗ it(πt)) (J ′′ it(d∗ it(πt)))2 · −Ai J ′′ it(d∗ it(πt)) (B.12)
= −A2 i J ′′′ it (d∗ it(πt)) (J ′′ it(d∗ it(πt)))3 (B.13)
Since Ai > 0 and J ′′ it(d∗ it(πt)) > 0 by Assumption 1, we have:
∂2d∗ it(πt)
∂π 2 t > 0 ⇐ ⇒J ′′′ it (d∗ it(πt)) < 0
At the boundary solutions (d∗ it = 0 or d∗ it = ¯dit), the second derivative is zero, so convexity
is determined by the interior behavior.
∂Jit(d∗ it(πt))
∂πt
=



0 d∗ it(πt) = dit,
A2 i πt
J ′′ it(d∗ it(πt)) d∗ it(πt) ∈ (0, dit)
0 d∗ it(πt) = 0
(B.14)
Proof of (6) and (B.14)
Proof. We first prove (B.14). For boundary cases where d∗ it(πt) ∈ {0, dit}, (5) shows that
consumption doesn’t change with price, so the derivative of electricity loss is zero.
For interior solutions where d∗ it(πt) ∈ (0, dit), we use the chain rule:
∂Jit(d∗ it(πt))
∂πt
= ∂Jit
∂dit

d∗ it(πt)
· ∂d∗ it(πt) ∂πt
Preprint submitted to Energy Policy – please cite published version once available

Appendix B.2 Aggregate Consumer APPENDIX B SECTION 2 PROOFS
From the first-order condition (3), we have ∂Jit ∂dit

d∗ it(πt)
= −Aiπt. Substituting this and
(5):
∂Jit(d∗ it(πt))
∂πt
= (−Aiπt) ·
 −Ai
J ′′ it(d∗ it(πt))

= A2 i πt
J ′′ it(d∗ it(πt))
Since Ai > 0, πt ≥ 0, and J ′′ it > 0, this derivative is non-negative, proving (B.14).
We now prove (6). For boundary cases, since consumption doesn’t change with price,
∂U ∗ it(πt)
∂πt = −Ai · 0 = 0. For interior solutions, we differentiate U ∗ it(πt) = Mit − Jit(d∗ it(πt)) − Aiπtd∗ it(πt):
∂U ∗ it(πt)
∂πt
= − ∂Jit(d∗ it(πt)) ∂πt − Ai  πt ∂d∗ it(πt) ∂πt + d∗ it(πt)  (B.15)
We know that ∂Jit(d∗ it(πt)) ∂πt = −Aiπt ∂d∗ it(πt) ∂πt . Substituting:
∂U ∗ it(πt)
∂πt
= −

−Aiπt
∂d∗ it(πt)
∂πt

− Aiπt
∂d∗ it(πt)
∂πt
− Aid∗ it(πt) (B.16)
= Aiπt
∂d∗ it(πt)
∂πt
− Aiπt
∂d∗ it(πt)
∂πt
− Aid∗ it(πt) (B.17)
= −Aid∗ it(πt) (B.18)
This completes the proof of (6).
In Appendix Appendix B.2, we provide complete technical details of these constructions
and proofs. The key result is that the aggregate consumer satisfies all the same behavioral
properties as individual consumers, enabling market-level analysis while preserving microe-
conomic foundations.
Appendix B.2. Aggregate Consumer
We construct an aggregate consumer to analyze market-level behavior. Given individual
optimal demands d∗ it(πt), we define aggregate consumption as d∗ t = P i∈N d∗ it and aggregate
utility as Ut = P i∈N Uit. The key question is: does there exist an aggregate loss function
ˆJt(dt) such that the aggregate consumer behaves like individual consumers?
Construction of Aggregate Loss Function: We define the aggregate normalized loss
function implicitly through the optimization problem:
ˆJt(dt) = min
{dit}:P i dit=dt,dit∈[0, ¯dit]
X
i∈N
ˆJit(dit)
This represents the minimum loss when aggregate consumption dt is optimally allocated
across consumers.
Verification that Assumption 1 holds for the aggregate consumer:
Preprint submitted to Energy Policy – please cite published version once available

Appendix B.2 Aggregate Consumer APPENDIX B SECTION 2 PROOFS
Proposition 9. The aggregate electricity loss function ˆJt(dt) is non-negative, decreasing,
and convex. When Assumptions 1.a–1.d are satisfied for individual consumers, they are also
satisfied for the aggregate consumer.
Proof. Since all ˆJit ≥ 0, their sum satisfies ˆJt ≥ 0.
We compute the first derivative of aggregate loss using the relationship between loss and
price derivatives. Since:
∂ ˆJt
∂πt
= ∂ ˆJt
∂dt
· ∂dt
∂πt
we have:
∂ ˆJt
∂dt
= ∂ ˆJt/∂πt
∂dt/∂πt
From individual optimization, we know that for interior solutions, ˆJ ′ it(d∗ it) = πt for all
consumers. By the envelope theorem, this implies:
∂ ˆJt
∂πt
= −πt · ∂dt
∂πt
Therefore:
∂ ˆJt
∂dt
= −πt · ∂dt/∂πt
∂dt/∂πt
= −πt
This confirms that marginal aggregate loss is negative, consistent with Assumption 1.a.
For the second derivative:
∂2 ˆJt
∂d2 t =
∂
∂πt (−πt)
∂dt
∂πt
= − 1 ∂dt/∂πt
Since ∂dt/∂πt < 0, we have ˆJ ′′ t > 0, confirming convexity.
For the third derivative:
ˆJ ′′′ t (dt) = ∂2dt/∂π 2 t (∂dt/∂πt)3
Since individual demands are convex ( ∂2dit ∂π 2 t > 0), aggregate demand is also convex, so
∂2dt
∂π 2 t > 0. Combined with ∂dt/∂πt < 0, this gives ˆJ ′′′ t < 0.
Relationship between aggregate and individual curvatures:
We can relate aggregate curvature to individual curvatures. From individual flexibility:
∂d∗ t
∂πt
=
X
i∈N
∂d∗ it
∂πt
=
X
i∈N
−1
ˆJ ′′ it(d∗ it(πt)) (B.19)
Combining with (Appendix B.2):
ˆJ ′′ t (d∗ t ) = − 1 ∂dt/∂πt = 1P i∈N 1 ˆJ ′′ it(d∗ it(πt)) (B.20)
Preprint submitted to Energy Policy – please cite published version once available

Appendix B.2 Aggregate Consumer APPENDIX B SECTION 2 PROOFS
This shows that aggregate curvature is the harmonic mean of individual curvatures.
Period-specific assumptions for aggregate consumer:
Proof. First-Order Condition: From (Appendix B.2), we have ∂ ˆJt ∂dt = −πt, confirming that
(3) holds for the aggregate consumer. Inverting gives d∗ t = ( ˆJ ′ t)−1(−πt), showing that (4)
holds.
Period Loss Ordering (Assumption 1.b): For any aggregate consumption level d:
ˆJ2(d) = minP
i di2=d
X
i
ˆJi2(di2) ≤ minP
i di1=d
X
i
ˆJi1(di1) = ˆJ1(d)
where the inequality follows from the individual assumption.
Marginal Loss Ordering (Assumption 1.c): At any price π, individual consumers satisfy
| ˆJ ′ i1(d∗ i1(π))| ≥ |ˆJ ′ i2(d∗ i2(π))|. Since both equal π in equilibrium, this transfers to the aggregate
level through the envelope theorem.
Curvature Ordering (Assumption 1.d): From (B.20), since ˆJ ′′ i1(d) ≥ ˆJ ′′ i2(d) for all i and
all d, the harmonic mean preserves this ordering:
ˆJ ′′ 1 (d∗ 1) = 1P
i
1
ˆJ ′′ i1(d∗ i1)
≥ 1P
i
1
ˆJ ′′ i2(d∗ i2)
= ˆJ ′′ 2 (d∗ 2)
Additional properties:
Proposition 10. Aggregate curvature increases in individual curvatures: For any consumer
j, ∂ ˆJ ′′ t
∂ ˆJ ′′ jt > 0.
Proof. Using (B.20):
∂
∂ ˆJ ′′ jt
ˆJ ′′ t = ∂ ∂ ˆJ ′′ jt 1P i∈N 1 ˆJ ′′ it = 1P i∈N 1 ˆJ ′′ it 2 · 1 ( ˆJ ′′ jt)2 > 0
This shows that when individual consumers become less price-responsive, the aggregate
consumer also becomes less flexible.
Proposition 11. Aggregate demand convexity: ∂2d∗ t (πt) ∂π 2 t > 0 ⇐ ⇒ˆJ ′′′ t (d∗ t (πt)) < 0.
Proof. From (Appendix B.2):
ˆJ ′′′ t (dt) = ∂2dt/∂π 2 t (∂dt/∂πt)3
Since ∂dt/∂πt < 0, the signs of ˆJ ′′′ t and ∂2dt/∂π 2 t are opposite. Since individual demands
are convex ( ∂2dit ∂π 2 t > 0), aggregate demand is also convex, giving ˆJ ′′′ t < 0.
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX C PROOFS FOR SECTION 3
Appendix C. Proofs for Section 3
The explanations for (13), (16), and (17) are in the main text.
Proof of (18)
Proof. Using the first-order condition of the consumer problem (3) we have
− ∂ ˆJ1(df 1 ) ∂d1 = − ∂ ˆJ2(df 2 ) ∂d2 = πf ,
while using the first-order condition of (7a), we find that
∂L1
∂π

πf
= − ∂L2
∂π

πf
=⇒
X
t∈T
∂ ˆJt(d∗ t (πf ))
∂π = −
X
t∈T
∂C (d∗ t (πf ))
∂π .
Expanding each term using the chain rule, we find that
X
t∈T

∂ ˆJt(d)
∂d

d∗ t (πf )
· ∂d∗ t (π) ∂π

 πf ! = − X t∈T  ∂C (d) ∂d

 d∗ t (πf ) ∂d∗ t (π) ∂π

 πf !
As we know that ∂ ˆJt(d) ∂d

d∗ t (πf )
= −πf , we can rewrite this as,
=⇒ −πf
X
t∈T
∂d∗ t (π)
∂π

πf
= −
X
t∈T

∂C (d)
∂d

d∗ t (πf )
∂d∗ t (π)
∂π

πf
!
=⇒ πf =
P
t∈T

∂C (d)
∂d

d∗ t (πf )
−1
ˆJ ′′ t (d∗ t (πf ))
!
P
t∈T
−1
ˆJ ′′ t (d∗ t (πf ))
=⇒ πf =
 1
ˆJ ′′ 1 (d∗ 1(πf ))
1
ˆJ ′′ 1 (d∗ 1(πf )) + 1 ˆJ ′′ 2 (d∗ 2(πf ))
!
∂C (d)
∂d

d∗ 1(πf )
+
 1
ˆJ ′′ 2 (d∗ 2(πf ))
1
ˆJ ′′ 1 (d∗ 1(πf )) + 1 ˆJ ′′ 2 (d∗ 2(πf ))
!
∂C (d)
∂d

d∗ 2(πf )
.
Proof of Proposition 2
Proof. Any solution πf to the planner’s problem (7a) with constraint (8) is also feasible
under the variable tariff by setting πv 1 = πv 2 = πf . Thus, minimum total loss under the
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX C PROOFS FOR SECTION 3
variable tariff is at most equal to total loss under the flat tariff.
Proof of Proposition 3
Proof. We first show the price order πv 1 ≥ πf ≥ πv 2.
In the variable pricing scenario, we can optimize for L1(π) and L2(π) separately to find
the optimal price in each time period. For the flat pricing scenario, we must have one
common price across time periods, so we optimize the total value L1(π) + L2(π).
Examining the relationship between the two variable prices first, using Assumption (1.c),
we can say that ˆJ ′ 1(d) + C ′(d) ≤ ˆJ ′ 2(d) + C ′(d) for any d. When total loss is optimized, we
know that dv 1 satisfies ˆJ ′ 1(dv 1) + C ′(dv 1) = 0 and dv 2 satisfies ˆJ ′ 2(dv 2) + C ′(dv 2) = 0. Since ˆJ1, ˆJ2,
and C are also convex in d, we conclude
ˆJ ′ 1(dv 2) + C ′(dv 2) ≤ ˆJ ′ 2(dv 2) + C ′(dv 2) = ˆJ ′ 1(dv 1) + C ′(dv 1) = 0 = ⇒ dv 1 ≥ dv 2.
Recall from (13) that πt = C ′(dt) > 0. Since C ′′(dt) > 0 according to Assumption 2,
πv 1 = C ′(dv 1) ≥ C ′(dv 2) = πv 2.
We now show that πf lies between πv 2 and πv 1 by utilizing the fact that C and ˆJt are
convex functions with respect to consumption d, so the planner’s problem in each period, Lt,
is also convex with respect to consumption d. Suppose πf = π′ > πv 1 were the optimal price
under flat pricing. Then, based on (5), d1(π′) ≤ d1(πv 1) = dv 1 and d2(π′) ≤ d2(πv 1) ≤ d2(πv 2).
Thus, the amount of consumption in both periods are below the optimum in the variable
case as shown in Figure C.5, so the planner’s objective function increases in both periods
with the price set at π′ compared to price πv 1. We compute the difference
L1(d1(π′)) − L1(dv 1) = −
Z dv 1
d1(π′)
L′ 1(a) da.
Since L′ 1(dv 1) = 0 by (13) and L′ 1 is an increasing function by the convexity of L1 with
respect to consumption,
Z dv 1
d1(π′)
L′ 1(a) da <
Z dv 1
d1(π′)
L′ 1(dv 1) da = 0
=⇒ L1(d1(π′)) − L1(dv 1) = −
Z dv 1
d1(π′)
L′ 1(a) da >0 = ⇒ L1(d1(π′)) > L1(dv 1).
Similarly, we can compute that
L2(d2(π′)) − L2(d2(πv 1)) = −
Z d2(πv 1 )
d2(π′)
L′ 2(a) da >−
Z d2(πv 1 )
d2(π′)
L′ 2(dv 2) da = 0
=⇒ L2(d2(π′)) > L2(d2(πv 1)).
Thus, we have shown that L1(d1(π′)) + L2(d2(π′)) > L1(dv 1) + L2(d2(πv 1)), showing that
π′ is not the optimal price under flat pricing.
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX C PROOFS FOR SECTION 3
Similarly, we can show that any price π′′ < πv 2 is not the optimal price under flat pricing.
This is because the amount of consumption is greater than the optimum variable amount in
both periods as shown in Figure C.6, so the planner objective function increases when the
price is set to π′′ compared to πv 2. We find that
L1(d1(π′′)) − L1(d1(πv 2)) =
Z d1(π′′)
d1(πv 2 )
L′ 1(a) da >
Z d1(π′′)
d1(πv 2 )
L′ 1(dv 1) da = 0
and
L2(d2(π′′)) − L2(d2(πv 2)) = L2(d2(π′′)) − L2(dv 2) =
Z d2(π′′)
dv 2
L′ 2(a) da
>
Z d2(π′′)
dv 2
L′ 2(dv 2) da = 0
so that L1(d1(π′′))+ L2(d2(π′′)) > L1(d1(πv 2))+ L2(dv 2), showing that π′′ is not the optimal
price under flat pricing.
Thus, the optimal value of πf must lie in the interval [ πv 2, πv 1].
d
L(d)
L2(d)
L1(d)
d1(πv 1 )d2(πv 1 )
d1(π′)
d2(π′)
Figure C.5: Because d1(π′) and d2(π′) both lie
to the left of the consumption values d for which
L1 and L2 reach their optimum, π′ cannot be the
price that minimizes L1 + L2.
d
L(d)
L2(d)
L1(d)
d2(πv 2 )
d2(π′′)
d1(πv 2 )
d1(π′′)
Figure C.6: Because d1(π′′) and d2(π′′) both lie
to the right of the consumption valuesd for which
L1 and L2 reach their optimum, π′′ cannot be the
price that minimizes L1 + L2.
Using the price order πv 1 ≥ πf ≥ πv 2, we now show the demand order. Based on the
ordering of prices, the difference between period 1 of the variable versus the flat pricing
is that the price in the variable case is higher. Thus, as (5) implies that consumption is
non-decreasing in price, dv i1 ≤ df i1. Similarly, the difference between the off-peak period of
the variable versus the flat pricing is that the price in the flat case is higher. Again, because
demand is a non-decreasing function of price, df i2 ≤ dv i2.
We now show that df i2 ≤ df i1. Note that from (4) we can write
df i1 = min{max{(J ′ 1)−1(−πf ), 0}, di1}, d f i2 = min{max{(J ′ 2)−1(−πf ), 0}, di2}.
Because J ′ 1(d) ≤ J ′ 2(d) < 0 at every point by Assumption 1.c and furthermore J ′ 1 and J ′ 2 are
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX C PROOFS FOR SECTION 3
increasing functions of d, we conclude that J ′ 1 reaches −πf at a higher consumption level
than J ′ 2. Thus, ( J ′ 1)−1(−πf ) > (J ′ 2)−1(−πf ). Combined with the assumption in the corollary
statement that di1 ≥ di2, this implies that df i1 ≥ df i2.
Additionally, for the aggregate consumer, dv 2 ≤ dv 1. This is because πv 2 ≥ πv 1, and C ′(dv t ) =
πv t as shown in (13)). C ′ is increasing in dt, so a higher peak period price implies more
electricity is consumed in the peak period.
Proof of Proposition 4
Proof. We start with the first-order conditions of the SWM’s problem under flat and variable
pricing. By (17), we know that
∂(L2 + L1)
∂π

πf
= 0,
which implies that
∂L1
∂π

πf
= − ∂L2
∂π

πf
= B,
where B is a constant.
For the variable price, (13), we know that
∂L1
∂π

πv 1
= ∂L2
∂π

πv 2
= 0.
Taking the difference of the derivatives of the SWM’s objective function with respect to
price under flat and variable pricing, we find that
∂L1
∂π

πv 1
− ∂L1
∂π

πf
= ∂L2
∂π

πf
− ∂L2
∂π

πv 2
. (C.1)
Using the mean value theorem, we know that for at least one pair π1 ∈ [πf , πv 1], π2 ∈ [πv 2, πf ],
there is a mean value of the second derivative of the period-specific operator problem
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX C PROOFS FOR SECTION 3
∂2L1(π1)
∂π 2 =
∂L1
∂π

πv 1
− ∂L1 ∂π

πf
πv 1 − πf ,
∂2L2(π2)
∂π 2 =
∂L2
∂π

πf
− ∂L2 ∂π

πv 2
πf − πv 2 ,
which we can rearrange and substitute into (C.1) to find,
(πv 1 − πf ) ∂2L1(π1) ∂π 2 = (πf − πv 2) ∂2L2(π2) ∂π 2 . (C.2)
Thus, if ∂2L1(π1) ∂π 2 > ∂2L2(π2) ∂π 2 , then πv 1 − πf = |∆π1| < |∆π2| = πf − πv 2. Otherwise if
∂2L1(π1)
∂π 2 < ∂2L2(π2) ∂π 2 , then |∆π1| > |∆π2|.
Proof of (19)
Proof. We can see that
∂2Lt
∂d2 = ∂2 ∂d2 (C(d) + ˆJt(d)) = C ′′ + ˆJ ′′ t .
As C ′′ is constant between periods and ˆJ ′′ 1 > ˆJ ′′ 2 , ∂2L1 ∂d2 > ∂2L2 ∂d2 evaluated at any d.
Using (19) we calculate the second derivative of the planner’s problem. As ∂2d∗ t (π) ∂π 2 = 0,
we have ∂2L ∂π 2 = d′ t(π)2 · (C ′′ + ˆJ ′′ t ) with both cost and loss as constants. Using (5), we find
∂2Lt
∂π 2 = C ′′ + ˆJ ′′ t ( ˆJ ′′ t )2 .
As C is constant between periods and ˆJ ′′ 1 > ˆJ ′′ 2 everywhere, ∂2L1 ∂π 2 < ∂2L2 ∂π 2 evaluated at any
π. We show that both Lt are convex. First, we compute the second derivative of Lt with
respect to price.
∂2
∂π 2 t Lt(d∗ t )
= ∂ ∂π  ∂d∗ t ∂πt · L′(d∗ t ) 
= ∂2d∗ t
∂π 2 t · L′(d∗ t ) +
 ∂d∗ t
∂πt
2
· L′′(d∗ t )
= −
ˆJ ′′′ t (d∗ t )
( ˆJ ′′ t (d∗ t ))3 (C ′(d∗ t ) + ˆJ ′ t(d∗ t )) +

1
ˆJ ′′ t (d∗ t )
!2
· (C ′′(d∗ t ) + ˆJ ′′ t (d∗ t )).
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX C PROOFS FOR SECTION 3
As C ′(d∗ 1) + ˆJ ′ 1(d∗ 1) > 0 in the peak period, we know that ∂2 ∂π 2 1 L1(d∗ 1) > 0. Re-examining
(C.2), we know that ∂2L1(π1) ∂π 2 > 0, πv 1 −πf > 0, and πf −πv 2 > 0 with the latter two inequalities
coming from Prop. 3. Thus, ∂2L2(π2) ∂π 2 > 0 as well and Lt is convex in both periods.
Further Analysis:
Starting from
∂2Lt
∂π 2 t = ∂2d∗ t ∂π 2 t h C ′(d∗ t ) + ˆJ ′ t(d∗ t ) i +  ∂d∗ t ∂πt 2h C ′′(d∗ t ) + ˆJ ′′ t (d∗ t ) i . (C.3)
Recall identities
∂2d∗ t
∂π 2 t = ˆJ ′′′ t (d∗ t )  ∂d∗ t ∂πt 3 , ˆJ ′′ t (d∗ t ) = − 1 ∂d∗ t ∂πt ,
and the consumer interior first-order condition ˆJ ′ t(d∗ t ) = −πt, to rewrite (C.3) as
∂2Lt
∂π 2 t = ˆJ ′′′ t (d∗ t )  ∂d∗ t ∂πt 3h C ′(d∗ t ) − πt i +  ∂d∗ t ∂πt 2 C ′′(d∗ t ) − ∂d∗ t ∂πt . (C.4)
Taking the partial derivative of (C.4) with respect to ∂d∗ t ∂πt holding d∗ t fixed gives
∂
∂

∂d∗ t
∂πt

 ∂2Lt
∂π 2 t

= 3 ˆJ ′′′ t (d∗ t )  ∂d∗ t ∂πt 2h C ′(d∗ t ) − πt i + 2∂d∗ t ∂πt C ′′(d∗ t ) − 1. (C.5)
This is the exact sensitivity of curvature to flexibility at the given ( πt, d∗ t ). At πv t we have
C ′(d∗ t ) = πv t , hence the first term in (C.5) vanishes and
At Variable Price: ∂
∂

∂d∗ t
∂πt

 ∂2Lt
∂π 2 t


πt=πv t
= 2 ∂d∗ t
∂πt
C ′′(d∗ t ) − 1. (C.6)
At πf the same formula yields
At Flat Price: ∂
∂

∂d∗ t
∂πt

 ∂2Lt
∂π 2 t


πt=πf
= 3 ˆJ ′′′ t (d∗ t )  ∂d∗ t ∂πt 2h C ′(d∗ t ) − πf i + 2∂d∗ t ∂πt C ′′(d∗ t ) − 1.
(C.7)
If one lets d∗ t and ∂d∗ t ∂πt co-move with π along the interval between πf and πv t , then the situation is more subtle. By definition,
d∗ t = d∗ t (πt), ∂d∗ t ∂πt = ∂d∗ t ∂πt (πt),
so both the level of demand and its slope vary as π varies. Consequently, the higher-order
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX D PROOFS FOR SECTION 4
primitives
ˆJ ′′′ t (d∗ t ), C ′′(d∗ t ), and ∂d∗ t ∂πt
are not constants but functions of the equilibrium demand d∗ t (πt).
Flexibility slope is still given point-wise as in (C.5), but now every component of (C.5)
is π-dependent. Explicitly,
∂
∂

∂d∗ t
∂πt


∂2 πtLt

(πt) = 3 ˆJ ′′′ t (d∗ t (πt))  ∂d∗ t ∂πt (πt) 2h C ′(d∗ t (πt)) − πt i + 2 ∂d∗ t ∂πt (πt) C ′′(d∗ t (πt)) − 1.
(C.8)
Thus, as πt moves from πf to πv t , the direct variation comes from the bracket [C ′(d∗ t (πt))−πt],
but is also indirect variation because ˆJ ′′′ t , C ′′, and ∂d∗ t ∂πt are themselves changing as functions
of πt. Because we know ˆJ ′′′ t < 0, ∂d∗ t ∂πt (πt) ≤ 0, C ′′(d∗ t (πt)) we can see that C ′(d∗ t (πt)) − πt is the only component without a predefined sign.
For the peak period (or any period where marginal cost is above the price), when
C ′(d∗ t (πt)) − π ≥ 0, (C.8) is negative. On the other hand for the off-peak period C ′(d∗ t (πt)) −
πt ≤ 0, so the sign of (C.8) is ambiguous. Because an increase in ∂dt/∂πt ≤ 0, an increase in
this term decreases the flexibility, |∂dt/∂πt|. So, curvature is increasing in flexibility for the
periods where price exceeds marginal cost and is ambiguous in flexibility for periods where
price is exceeded by marginal cost.
Appendix D. Proofs for Section 4
Proof for Theorem 5
The total change in utility from flat to variable pricing ∆ Ui = P t∈T ∆Uit can be written
as the integral of consumption over the interval between equilibrium prices,
∆Uit =
Z πv t
πf
∂Ui(πit)
∂π dπ = −
Z πv t
πf
Aid∗ it(π)dπ. (D.1)
Thus, total change in utility can be written as
∆Ui = −
Z πv 1
πf
Aid∗ i1(π)dπ −
Z πv 2
πf
Aid∗ i2(π)dπ
= Ai

−
Z πv 1
πf
d∗ i1(π)dπ +
Z πf
πv 2
d∗ i2(π)dπ
!
. (D.2)
Proof. We reference 21 to derive this sufficient and necessary condition for linear and isoelas-
tic demand. We work with a scaled quantity ∆Ui Ai , shown in (D.3), for notational simplicity.
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX D PROOFS FOR SECTION 4
∆Ui
Ai
= ∆Ui1
Ai
+ ∆Ui2
Ai
= −
Z πv 1
πf
d∗ i1(π)dπ +
Z πf
πv 2
d∗ i2(π)dπ. (D.3)
As shown in Figure D.7, we use first order approximations to obtain upper bounds on
∆Ui1
Ai and ∆Ui2 Ai .
π
d
di1
πf πv 1
∂di1(πv 1 )
∂π
π
d
di2
πfπv 2
∂di2(πf )
∂π
Figure D.7: The shaded area on the blue curve illustrates a lower bound for |∆Ui1| Ai (upper bound for ∆Ui1 Ai ),
while the shaded area on the red curve illustrates an upper bound for ∆Ui2 Ai .
Because of the assumption of convexity of d∗ i1 with respect to π, we have the lower bound
d∗ i1(π) ≥ df i1 + (π − πf ) ∂d∗ i1(πf ) ∂π for all π ∈ [πf , πv 1]. (D.4)
resulting in the upper bound
∆Ui1
Ai
= −
Z πv 1
πf
d∗ i1(π)dπ ≤ −
Z πv 1
πf

df i1 + (π − πf ) ∂d∗ i1(πf ) ∂π  dπ
= −|∆π1|df i1 − |∆π1|2 2 ∂d∗ i1(πf ) ∂π . (D.5)
Similarly, we have the upper bound
d∗ i2(π) ≤ df i2 − (πf − π) ∂d∗ i2(πv 2) ∂π for all π ∈ [πv 2, πf ],
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX D PROOFS FOR SECTION 4
resulting in the upper bound,
∆Ui2
Ai
=
Z πf
πv 2
d∗ i2(π)dπ ≤
Z πf
πv 2

df i2 − (πf − π) ∂d∗ i2(πv 2) ∂π  dπ (D.6)
= |∆π2|df i2 − |∆π2|2 2 ∂d∗ i2(πv 2) ∂π . (D.7)
Combining equations (D.5) and (D.7), we compute the sufficient condition
∆Ui
Ai
= ∆Ui1
Ai
+ ∆Ui2
Ai
≤ −|∆π1|df i1 − |∆π1|2 2 ∂d∗ i1(πf ) ∂π + |∆π2|df i2 − |∆π2|2 2 ∂d∗ i2(πv 2) ∂π < 0
=⇒ (−|∆π1|df i1 + |∆π2|df i2) +
 |∆π1|2
2

 ∂d∗ i1(πf ) ∂π

 + |∆π2|2 2

 ∂d∗ i2(πv 2) ∂π

  < 0.
Because the approximations made to generate the bound (22) are first-order approxima-
tions, (22) is a sufficient and necessary condition for ∆ Ui < 0 when demand is affine. Thus,
for a consumer i with quadratic electricity loss Jit, ∆Ui < 0 if and only if
−|∆π1|df i1 + |∆π2|df i2 + |∆π1|2 2

 ∂d∗ i1(πf ) ∂π

 + |∆π2|2 2

 ∂d∗ i2(πv 2) ∂π

 < 0,
which occurs exactly when their change in incidence if they were completely inelastic, is
upper bounded by a weighted sum of consumer flexibility.
Now we derive sufficient and necessary conditions for isoelastic utility. Starting with the
general form of demand under a variable price π, we can substitute d(π) = df · ( π πf )ϵ(π) into
the expression of ∆ Ui, which results in the following restatement of total change in utility,
∆Ui = −
Z πv 1
πf
df i1 ·  π1 πf −ϵi1(π1) dπ1 + Z πf πv 2 df i2 ·  π2 πf −ϵi2(π2) dπ2.
This expression incorporates demand responses over two pricing intervals: from πf to πv 1
for peak and from πv 2 to πf for off-peak periods. Each term reflects the demand elasticity as
a function of price within these intervals.
Elasticity at a given price π can be decomposed as follows:
ϵ(π) = ϵf + ∆ϵ(π),
where ϵf is the elasticity at the flat price πf , and ∆ ϵ(π) is movement away from the flat
price as the price changes. Substituting the decomposition ϵ(π) = ϵf + ∆ϵ(π), we rewrite:
d(π) = df ·  π πf ϵf +∆ϵ(π) = df ·  π πf ϵf ·  π πf ∆ϵ(π) . (D.8)
where, for isoelastic utility,
 π
πf
∆ϵ(π)
= 1
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX D PROOFS FOR SECTION 4
Substituting this back into (D.8), we obtain:
d(π) = df ·  π πf ϵf .
This expression of demand reflects the demand function’s response to both the baseline
elasticity at the flat price ϵf and the variability term ∆ ϵ(π). Substituting the decomposed
elasticity into the utility change expression, we obtain:
∆Ui = −
Z πv 1
πf
df i1 ·  π1 πf ϵf i1 · dπ1 + Z πf πv 2 df i2 ·  π2 πf ϵf i2 dπ2.
We then take this integral and find when it is less than zero:
df i1 · πf
1 + ϵf i1
"
1 −
 πv 1
πf
1+ϵf i1 #
+ df i2 · πf
1 + ϵf i2
"
1 −
 πv 2
πf
1+ϵf i2 #
< 0.
We then can then divide by the flat price term,
df i1
1 + ϵf i1
"
1 −
 πv 1
πf
1+ϵf i1 #
+ df i2
1 + ϵf i2
"
1 −
 πv 2
πf
1+ϵf i2 #
< 0.
This condition is necessary and sufficient when elasticity remains constant: a consumer i
loses utility if and only if this inequality is satisfied.
Proof for Corollary 6
The change in utility during peak periods is:
∆Ui = −Ai
Z πv 1
πf
d∗ it(π)dπ + Ai
Z πf
πv 2
d∗ it(π)dπ
In Theorem 5, we presented the following relationships.
∆Ui1
Ai
= −
Z πv 1
πf
d∗ i1(π)dπ ≤ −
Z πv 1
πf

df i1 + (π − πf ) ∂d∗ i1(πf ) ∂π  dπ = −|∆π1|df i1 − |∆π1|2 2 ∂d∗ i1(πf ) ∂π
∆Ui2
Ai
=
Z πf
πv 2
d∗ i2(π)dπ ≤
Z πf
πv 2

df i2 − (πf − π) ∂d∗ i2(πv 2) ∂π  dπ = |∆π2|df i2 − |∆π2|2 2 ∂d∗ i2(πv 2) ∂π .
We can therefore say that (22) is sufficient for all utility functions of the form of (1) that
fall under Assumptions 1.
Proof for Proposition 7
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX D PROOFS FOR SECTION 4
Proof. We rearrange (25) to find that ∆ Ul < ∆Uh is equivalent to the condition
Z πv 1
πf
Ahdh1(π)dπ +
Z πf
πv 2
Aldl2(π)dπ <
Z πf
πv 2
Ahdh2(π)dπ +
Z πv 1
πf
Aldl1(π)dπ. (D.9)
Here, we can use the convexity of dit(π) to upper bound the left hand side and lower
bound the right hand side of (D.9). Similar to Figure D.7, we compute the upper bound on
the left hand side of (D.9) as
Ah
Z πv 1
πf

df h1 + (π − πf ) ∂dv h1 ∂π  dπ + Al Z πf πv 2  df l2 − (πf − π) ∂dv l2 ∂π  dπ
=Ah

|∆π1|df h1 − |∆π1|2 2

 ∂dv h1 ∂π

  + Al  |∆π2|df l2 + |∆π2|2 2

 ∂dv l2 ∂π

  , (D.10)
while we compute the lower bound on the right hand side of (D.9) as
Ah
Z πf
πv 2

df h2 − (πf − π) ∂df h2 ∂π ! dπ + Al Z πv 1 πf  df l1 + (π − πf ) ∂df l1 ∂π ! dπ
=Ah

|∆π2|df h2 + |∆π2|2 2

 ∂df h2 ∂π

 ! + Al  |∆π1|df l1 − |∆π1|2 2

 ∂df l1 ∂π

 ! . (D.11)
Combining the bounds in Equations (D.10) and (D.11),
Al

−|∆π1|df l1 + |∆π2|df l2 + |∆π1|2 2

 ∂df l1 ∂π

 + |∆π2|2 2

 ∂dv l2 ∂π

 !
< Ah

−|∆π1|df h1 + |∆π2|df h2 + |∆π1|2 2

 ∂dv h1 ∂π

 + |∆π2|2 2

 ∂df h2 ∂π

 ! . (D.12)
In the case of quadratic electricity loss, corresponding to affine electricity demand, the
approximations of ∆Ul and ∆Uh in D.12 are exact.
We now examine the isoelastic case. To establish the condition under which ∆Ul −∆Uh <
0, reflecting that the utility loss for a low-income consumer ( l) is smaller than that for a
high-income consumer ( h), we begin with the utility change expression for each consumer.
The change in utility is given by (D.12) (adjusted for common factors).
For a low-income consumer ( l) and a high-income consumer ( h), we subtract their re-
Preprint submitted to Energy Policy – please cite published version once available

APPENDIX E PROOFS FOR SECTION 5
spective utility changes to obtain
∆Ul − ∆Uh ∝Al

df l1
1 + ϵf l1
"
1 −
 πv 1
πf
1+ϵf l1 #
+ df l2
1 + ϵf l2
"
1 −
 πv 2
πf
1+ϵf l2 #!
− Ah

df h1
1 + ϵf h1
"
1 −
 πv 1
πf
1+ϵf h1 #
− df h2
1 + ϵf i2
"
1 −
 πv 2
πf
1+ϵf h2 #!
.
This expression separates the differences in utility loss into peak and off-peak contribu-
tions. For ∆ Ul − ∆Uh < 0 to hold, the peak-period utility difference must be dominated
by the off-peak-period utility difference, such that the net utility loss for the high-income
consumer exceeds that for the low-income consumer. Simplifying further, this inequality
depends on the relative magnitudes of 1 1+ϵ for low- and high-income consumers, as larger ϵ
values amplify the response to price changes.
Proof for Corollary 8
Proof. From the proof for Proposition 7 , combining the bounds in (D.10) and (D.11) results
in the sufficient condition,
Al

−|∆π1|df l1 + |∆π2|df l2 + |∆π1|2 2

 ∂df l1 ∂π

 + |∆π2|2 2

 ∂dv l2 ∂π

 !
< Ah

−|∆π1|df h1 + |∆π2|df h2 + |∆π1|2 2

 ∂dv h1 ∂π

 + |∆π2|2 2

 ∂df h2 ∂π

 ! . (D.13)
As these provide an upper bound on low-income utility change and a lower bound on high-
income utility change (D.13) is sufficient but not necessary for the low income consumer to
lose utility relative to the high income consumer.
Appendix E. Proofs for Section 5
Appendix E.1. Proof of the Profit Constraint Condition
In the unconstrained operator problem shown in (7a)-(7d), the operator sets the period-
specific price equal to marginal cost, πt = C ′(dt). Introducing a profit requirement alters this
outcome if the welfare maximizing profit is not equal to the profit requirement. We examine
how prices change given a profit constraint but do not analyze the results of Section 4 as the
conditions there take price changes as input. To begin, suppose the operator must satisfy
an aggregate profit condition,
X
t∈T
Pt(π) = ¯P , (E.1)
where Pt(π) = πtd∗ t (πt) − C(d∗ t (πt)). Note that instead of the equality we could instead
include an inequality to represent either a floor (to ensure cost recovery) or a cap (to limit
Preprint submitted to Energy Policy – please cite published version once available

Appendix E.1 Proof of the Profit Constraint Condition APPENDIX E PROOFS FOR SECTION 5
rents). To incorporate (E.1), the planner’s problem is written with a Lagrange multiplier ν:
L =
X
t
Lt(πt) + ν
 X
t
Pt(πt) − ¯P
!
,
where Lt(πt) = Ut(dt(πt))−C(dt(πt)) is by-period welfare. We then differentiate with respect
to πt. By the envelope theorem we have,

C ′ − π∗ t  ∂d∗ t ∂πt + ν  d∗ t + (π∗ t − C ′) ∂d∗ t ∂πt  = 0.
Recall the price elasticities relationship to demand, flexibility and price: ϵt = ∂d∗ t
∂πt
· πt
d∗ t (note
ϵt < 0). Then for the optimal π∗,
d∗ t = π∗ t ϵt ∂d∗ t ∂πt .
Substitute and factor ∂d∗ t /∂πt ̸= 0:
(C ′ − π∗ t ) + ν
 π∗ t
ϵt
+ (π∗ t − C ′)

= 0.
Rearrange:
(C ′ − π∗ t )(1 − ν) = ν π∗ t ϵt . (E.2)
When ν >0 binds, prices deviate from marginal cost. Solve (E.2) for the distortion:
π∗ t − C ′(d∗ t ) = − ν 1 − ν π∗ t ϵt
because ϵt < 0. So the wedge from marginal cost is proportional to the markup factor ν 1 − ν
and inversely proportional to the (absolute) demand elasticity.
If the profit floor ¯P is set below the unconstrained profit level, then the constraint binds
with ν >0. Because ∂Lt ∂πt is increasing in price and is zero at πv t , the binding constraint forces prices upward: π∗ t > πv t . In this case, both peak and off-peak prices rise further above the
flat price than in the unconstrained solution.
Conversely, if the profit cap ¯P is set above the unconstrained profit level, the constraint
binds with ν < 0. In this case, equilibrium requires lowering prices relative to πv t , so that
π∗ t < πv t . Both peak and off-peak prices move closer to the flat price compared to the
unconstrained outcome. If the cap exceeds the maximum feasible profit (i.e., monopoly
profit), no feasible solution exists.
This markup (if ν > 0) or markdown (if ν < 0) is inversely proportional to demand
elasticity; the operator adjusts prices more in periods where consumers are less responsive
to price. Because the multiplier ν applies to the profit constraint globally, it ties together all
periods. A tighter profit requirement (larger |ν|) increases the deviation in every period, but
Preprint submitted to Energy Policy – please cite published version once available

Appendix E.1 Proof of the Profit Constraint Condition APPENDIX E PROOFS FOR SECTION 5
the allocation of that deviation across periods is determined by relative elasticities. Taking
the ratio of distortions for two periods t, t′ yields
πt − C ′(dt)
πt′ − C ′(dt′) = πt/ϵt πt′/ϵt′ .
This condition shows that the markups are inversely proportional across periods, so that
periods with smaller |ϵt| bear a larger share of the adjustment. The cross-period link is
essential: regardless of how profits are constrained in aggregate, the optimal adjustment
balances out across periods in inverse proportion to their elasticities.
Multi Period Proofs Recall from (7a) the objective function of the grid operator under
flat pricing:
L =
X
t∈T
Lt =
X
t∈T
ˆJt(dt(πf )) + C(dt(πf )).
To minimize this expression, when all consumer demand levels are in the interior of their
limits dit ∈ (0, ¯dit), we can take the derivative of L with respect to πf , and equate the
derivative to 0. The derivative is as follows:
∂L
∂π f = 0
=⇒
X
t∈T

ˆJ ′ t(dt(πf )) + C ′(dt(πf )) 

 ∂dt(πf ) ∂π f

 = 0.
Recalling that ˆJ ′ t(dt(πf )) = −πf at equilibrium, and that ∂dt/∂π f ̸= 0 is negative for interior
solutions, we simplify to
X
t∈T

−πf + C ′(dt(πf )) 

 ∂dt ∂π f

 = 0
=⇒
X
t∈T
C ′(dt(πf ))

 ∂dt ∂π f

 = πf X t∈T

 ∂dt ∂π f

=⇒ πf =
P
t∈T C ′(dt(πf ))|∂dt/∂π f |P
t∈T |∂dt/∂π f | ,
as desired. We do not include the properties of the variable prices or demands as they need
no further extension from what was presented in Section 3 and Appendix C. This is because
prices and demand chosen period-by period for variable pricing rather across periods as is
the case for flat pricing.
Examining consumer utility change, we first rewrite the change in utility ∆ Ui and ∆Uj
Preprint submitted to Energy Policy – please cite published version once available

Appendix E.1 Proof of the Profit Constraint Condition APPENDIX E PROOFS FOR SECTION 5
of consumers i and j due to a switch from flat to variable pricing as follows:
∆Ui = Ai
"X
t∈T
Z πv t
πf
(−dit(π))dπ
#
,
∆Uj = Aj
"X
t∈T
Z πv t
πf
(−djt(π))dπ
#
.
To obtain a sufficient condition for ∆ Ui < ∆Uj, we seek to upper bound ∆ Ui and lower
bound ∆Uj. We obtain these bounds by employing the following bounds on demand, which
can be verified due to convexity: for π between πf and πv t , we have
dit(π) ≥ dit(πf ) + (π − πf )d′ it(πf ),
dit(π) ≤ dit(πf ) + (π − πf )d′ it(πv t ).
We now use these bounds in two distinct cases:
Case 1: πf < πv t . Here, we can compute that
−
Z πv t
πf
(dit(πf ) + (π − πf )d′ it(πf ))dπ ≥ −
Z πv t
πf
dit(π)dπ ≥ −
Z πv t
πf
(dit(πf ) + (π − πf )d′ it(πv t )).
Carrying out the integral computations, we find
(πf − πv t )df it + |∆πt|2 2 |d′ it(πf )| > − Z πv t πf dit(π)dπ >(πf − πv t )df it + |∆πt|2 2 |d′ it(πv t )|.
Case 2: πf > πv t . Here, we can compute that
−
Z πv t
πf
(dit(πf ) + (π − πf )d′ it(πf ))dπ <−
Z πv t
πf
dit(π)dπ <−
Z πv t
πf
(dit(πf ) + (π − πf )d′ it(πv t )).
Carrying out the integral computations, we find
(πf − πv t )df it + |∆πt|2 2 |d′ it(πf )| < − Z πv t πf dit(π)dπ <(πf − πv t )df it + |∆πt|2 2 |d′ it(πv t )|.
Therefore, for time periods t1 ∈ T∞ where πf < πv t , we can upper bound ∆ Uit by
Ai

(πf − πv t )df it + |∆πt|2 2 |d′ it(πf )|  ,
while we can lower bound ∆ Ujt by
Aj

(πf − πv t )df jt + |∆πt|2 2 |d′ jt(πv t )|  .
Preprint submitted to Energy Policy – please cite published version once available

Appendix E.1 Proof of the Profit Constraint Condition APPENDIX E PROOFS FOR SECTION 5
Similarly, for time periods t2 ∈ T∈ where πf > πv t , we can upper bound ∆ Uit by
Ai

(πf − πv t )df it + |∆πt|2 2 |d′ it(πv t )|  ,
while we can lower bound ∆ Ujt by
Aj

(πf − πv t )df jt + |∆πt|2 2 |d′ jt(πf )|  .
Adding up the respective upper bounds for ∆ Uit and lower bounds for ∆ Ujt across re-
spective time periods t1 in T1 and t2 in T2, we obtain the sufficient condition for ∆ Ui < 0
analogous to (22),
Ai
"X
t∈T
(πf − πv t )df it + X
t1∈T1
|∆πt1|2
2 |d′ it1(πf )| + X t2∈T2 |∆πt2|2 2 |d′ it2(πv t2)| # < 0.
We also reproduce the conditions ∆ Ui < ∆Uj shown in (26),
Ai
"X
t∈T
(πf − πv t )df it + X
t1∈T1
|∆πt1|2
2 |d′ it1(πf )| + X t2∈T2 |∆πt2|2 2 |d′ it2(πv t2)| #
<Aj
"X
t∈T
(πf − πv t )df jt + X
t1∈T1
|∆πt1|2
2 |d′ jt(πv t1)| + X t2∈T2 |∆πt2|2 2 |d′ jt(πf )| # .
We can also find multi-period utility change under isoelastic demand. In (6) have estab-
lished,
∂U ∗ it(π)
∂π = −Aidit(π),
for interior solutions. Integrating from πf to πv t gives the by-period utility change:
∆Uit = U v it − U f it = −Ai
Z πv t
πf
dit(πt)dπt.
Recall isoelastic demand
d∗ it(πt) = df it
 πt
πf
ϵit
= df it(πf )−ϵitπϵit t .
Thus
∆Uit = −Aidf it(πf )−ϵit
Z πv t
πf
πϵit t dπ = −Aidf it(πf )−ϵit
 π1+ϵit t
1 + ϵit
πv t
πf
.
Rearranging,
∆Uit = Ai
df it
1 + ϵit
"
1 −
 πv t
πf
1+ϵit #
.
Preprint submitted to Energy Policy – please cite published version once available

REFERENCES REFERENCES
Summing over t yields the stated expression for ∆ Ui. Since Ai > 0, the sign of ∆ Ui is
determined by the sign of the bracketed sum.
For consumers h and l, we can compare their changes in utility using the following
expression:
∆Uh − ∆Ul =
X
t∈T
"
Ah
df ht
1 + ϵht

1 − ( πv t πf )1+ϵht  − Al df lt 1 + ϵlt  1 − ( πv t πf )1+ϵlt # .
Hence, the low-income consumer loses more utility (∆ Ul < ∆Uh) iff the right-hand side
is positive.
Declaration of generative AI and AI-assisted technologies in the writing process:. During the
preparation of this work the author(s) used generative AI in order to edit this paper. After
using this tool/service, the author(s) reviewed and edited the content as needed and take(s)
full responsibility for the content of the publication.
References
S. Borenstein, J. B. Bushnell, Do two electricity pricing wrongs make a right? cost recovery,
externalities, and efficiency, American Economic Journal: Economic Policy 14 (2022)
80–110.
U.S. Energy Information Administration, Hourly electricity consumption varies throughout
the day and across seasons (2020). URL:https://www.eia.gov/todayinenergy/detail.
php?id=42915.
M. Auffhammer, P. Baylis, C. H. Hausman, Climate change is projected to have severe
impacts on the frequency and intensity of peak electricity demand across the united states,
Proceedings of the National Academy of Sciences 114 (2017) 1886–1891. doi: 10.1073/
pnas.1613193114.
T. Schittekatte, D. Mallapragada, P. L. Joskow, R. Schmalensee, Reforming retail electricity
rates to facilitate economy-wide decarbonization, Joule 7 (2023) 831–836.
W. Anderson, V. White, A. Finney, Coping with low incomes and cold homes, Energy Policy
49 (2012) 40–52. doi: 10.1016/j.enpol.2012.01.002.
S. Cong, D. Nock, Y. L. Qiu, B. Xing, Unveiling hidden energy poverty using the energy
equity gap, Nature Communications 13 (2022) 2456. doi: 10.1038/s41467-022-30146-5 .
M. Kwon, S. Cong, D. Nock, L. Huang, Y. L. Qiu, B. Xing, Forgone summertime comfort
as a function of avoided electricity use, Energy Policy 183 (2023) 113813. doi: 10.1016/j.
enpol.2023.113813.
R. Best, K. Sinha, Fuel poverty policy: Go big or go home insulation, Energy Economics
97 (2021) 105195. doi: 10.1016/j.eneco.2021.105195.
Preprint submitted to Energy Policy – please cite published version once available

REFERENCES REFERENCES
R. Br¨ annlund, M. Vesterberg, Peak and off-peak demand for electricity: Is there a potential
for load shifting?, Energy Economics 102 (2021) 105466. doi: 10.1016/j.eneco.2021.
105466.
H. Mohring, The peak load problem with increasing returns and pricing constraints, The
American Economic Review 60 (1970) 693–705.
M. S. Feldstein, Distributional equity and the optimal structure of public prices, The
American Economic Review 62 (1972) 32–36.
S. Borenstein, The long-run efficiency of real-time electricity pricing, The Energy Journal
26 (2005) 93–116. doi: 10.5547/ISSN0195-6574-EJ-Vol26-No3-5 .
D. Aigner, The residential electricity time-of-use pricing experiments: what have we learned?,
in: Social experimentation, University of Chicago Press, 1985, pp. 11–54.
D. W. Caves, L. R. Christensen, J. A. Herriges, Consistency of residential customer response
in time-of-use electricity pricing experiments, Journal of Econometrics 26 (1984) 179–203.
A. Faruqui, S. Sergici, Household response to dynamic pricing of electricity: a survey
of 15 experiments, Journal of Regulatory Economics 38 (2010) 193–225. doi: 10.1007/
s11149-010-9127-y .
S. Horowitz, L. Lave, Equity in residential electricity pricing, The Energy Journal
35 (2014). URL: http://www.iaee.org/en/publications/ejarticle.aspx?id=2556.
doi:10.5547/01956574.35.2.1.
P. Simshauser, D. Downer, On the inequity of flat-rate electricity tariffs, The Energy Journal
(2016) 199–229.
S. P. Burger, C. R. Knittel, I. J. P´ erez-Arriaga, I. Schneider, F. Vom Scheidt, The efficiency
and distributional effects of alternative residential electricity rate designs, The Energy
Journal 41 (2020).
L. Jiang, S. Low, Multi-period optimal energy procurement and demand response in smart
grid with uncertain supply, in: 2011 50th IEEE conference on decision and control and
European control conference, IEEE, 2011, pp. 4348–4353.
A. R. Jordehi, Optimisation of demand response in electric power systems, a review, Re-
newable and sustainable energy reviews 103 (2019) 308–319.
R. Deng, Z. Yang, M.-Y. Chow, J. Chen, A survey on demand response in smart grids:
Mathematical models and approaches, IEEE Transactions on Industrial Informatics 11
(2015) 570–582.
H. Fell, S. Li, A. Paul, A new look at residential electricity demand using household expen-
diture data, International Journal of Industrial Organization 33 (2014) 37–47.
S. Borenstein, The redistributional impact of nonlinear electricity pricing, American Eco-
nomic Journal: Economic Policy 4 (2012) 56–90.
Preprint submitted to Energy Policy – please cite published version once available

REFERENCES REFERENCES
P. L. Joskow, C. D. Wolfram, Dynamic pricing of electricity, American Economic Review
102 (2012) 381–385.
P. Joskow, J. Tirole, Retail electricity competition, The RAND Journal of Economics 37
(2006) 799–815. doi: 10.1111/j.1756-2171.2006.tb00058.x.
S. Borenstein, Customer risk from real-time retail electricity pricing: Bill volatility and
hedgability, The Energy Journal 28 (2007) 111–130.
H. Shi, B. Wang, Y. L. Qiu, N. Deng, B. Xie, B. Zhang, S. Ma, The unequal impacts of
extremely high temperatures on households’ adaptive behaviors: Empirical evidence from
fine-grained electricity consumption data, Energy Policy 190 (2024) 114170. doi: 10.1016/
j.enpol.2024.114170.
P. Joskow, J. Tirole, Reliability and competitive electricity markets, The RAND Journal of
Economics 38 (2007) 60–84. doi: 10.1111/j.1756-2171.2007.tb00044.x.
H.-p. Chao, Price-responsive demand management for a smart grid world, The Electricity
Journal 23 (2010) 7–20. doi: 10.1016/j.tej.2009.12.007.
P. Calver, N. Simcock, Demand response and energy justice: A critical overview of ethical
risks and opportunities within digital, decentralised, and decarbonised futures, Energy
Policy 151 (2021) 112198.
S. Borenstein, Equity effects of increasing-block electricity pricing (2008). URL: https:
//escholarship.org/uc/item/3sr1h8nc.
C. Gambardella, M. Pahle, Time-varying electricity pricing and consumer heterogeneity:
Welfare and distributional effects with variable renewable supply, Energy Economics 76
(2018) 257–273.
S. P. Boyd, L. Vandenberghe, Convex optimization, Cambridge univerisity press, 2004.
Preprint submitted to Energy Policy – please cite published version once available
