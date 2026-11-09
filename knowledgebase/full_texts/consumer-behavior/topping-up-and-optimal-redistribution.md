---
title: Topping Up and Optimal Redistribution
url: https://arxiv.org/abs/2606.28919
category: consumer-behavior
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Zi Yang Kang
- Mitchell Watt
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.28919
pages: 74
chars: 116278
fetched_at: '2026-11-08T12:59:41+00:00'
kb_version: 1
---

# Topping Up and Optimal Redistribution

Topping Up and Optimal Redistribution∗
Zi Yang Kang† Mitchell Watt‡
June 2026
Abstract
Thispaperstudieshowtoppingup—allowingrecipientsofin-kindtransferstosupplementsubsidized
consumptioninaprivatemarket—affectsoptimalredistribution. Consumerscanaccessacompetitive
private market, while a social planner offers an alternative nonlinear price schedule. We show that
the effect of topping up depends on the correlation between redistributive priority and demand.
When the correlation is positive, topping up does not affect the optimal mechanism. When the
correlation is negative, topping up weakens screening and reduces redistribution. At the extensive
margin,toppingupreducesthesetofenvironmentsinwhichinterventionisoptimal. Attheintensive
margin, topping up weakly reduces both the scope of a free public option and the mass of consumers
served,andshiftsredistributionawayfromtheconsumerswiththehighestredistributivepriority. We
characterize the optimal mechanisms and show how topping up changes the comparative statics of
optimal redistribution with respect to redistributive priorities.
JEL classification: D47, D63, D82, H21, H42
Keywords: in-kindredistribution, toppingup, publicprovision, subsidies, optimalmechanismdesign
∗ WeareespeciallyindebtedtoLauraDoval,PaulMilgrom,MarcinPęski,andAndySkrzypaczforilluminatingdiscussions.
We thank Piotr Dworczak, Liran Einav, Marina Halac, Caroline Hoxby, Ravi Jagadeesan, Rishabh Kirpalani, Anton
Kolotilin, Simon Loertscher, Guillaume Roger, Ilya Segal, Xianwen Shi, Philipp Strack, Satoru Takahashi, Filip Tokarski,
and Kai Hao Yang for comments and suggestions. We gratefully acknowledge the support of the Center of Mathematical
Sciences and Applications at Harvard University (Kang) and the Koret Fellowship, the Ric Weiland Graduate Fellowship,
and the Gale and Steve Kohlhagen Fellowship in Economics at Stanford University (Watt). This paper subsumes and
extends our previous two working papers circulated under the titles of “Optimal In-Kind Redistribution” and “Optimal
Redistribution Through Subsidies.”Refine.ink was used to check the paper for consistency and clarity.
† Department of Economics, University of Toronto;zy.kang@utoronto.ca.
‡ Department of Economics, Monash University;mitch.watt@monash.edu.
arXiv:2606.28919v1  [econ.GN]  27 Jun 2026

1 Introduction
Governments often redistribute in kind. Food stamps, public housing, childcare subsidies, and health
care programs all transfer resources to eligible individuals by changing the effective prices they face.
These programs differ, however, in an important respect: whether recipients cantop uptheir subsidized
consumption through private-market purchases. For example, food stamp recipients may use their
benefits to purchase groceries and then supplement those benefits with cash, whereas public housing
recipients generally cannot supplement the housing services provided by the program in the same way.
This distinction is often itself a design choice: housing assistance, for instance, can be delivered through
housingvouchersratherthandirectpublicprovision,makingiteasierforrecipientstorentmoreexpensive
apartments by supplementing their vouchers with cash.
Importantly, topping up can affect the social planner’s ability to screen consumers in redistribution
programs. When topping up is allowed, high-demand consumers can choose subsidized allocations
intended for low-demand consumers and then purchase additional units privately. However, preventing
toppingupmayitselfbecostly,becauseitcanrequiremonitoringsupplementarypurchasesorrestricting
recipients’ ability to combine program benefits with private spending. While such administrative and
enforcement costs may often be estimated directly, the effect of topping up on screening is much less
transparent. Despite a growing literature on inequality-aware mechanism design, the role of topping up
in shaping optimal redistribution programs remains poorly understood.
Thispaperstudieshowtoppingupaffectstheoptimaldesignofredistributionprograms. Weaskthree
questions. First, how does topping up affect when the social planner should intervene? Second, when
does topping up change the optimal mechanism? Third, when topping up changes the mechanism, how
does it change the structure of optimal redistribution?
To answer these questions, we develop a mechanism-design model that accommodates both topping
up and no topping up. Consumers differ in their demand for a homogeneous good and can purchase
any quantity in a perfectly competitive private market at marginal cost. A social planner can offer
an alternative, potentially nonlinear, price schedule for the same good. Following the recent literature
on inequality-aware mechanism design (e.g., Dworczakr⃝ Kominers r⃝ Akbarpour, 2021; Akbarpourr⃝
Dworczak r⃝ Kominers,2024),wemodelthesocialplanner’sredistributiveobjectiveusingheterogeneous
1

welfare weights. The welfare weight𝜔(𝜃) represents the gross social value of giving one unit of money
to a type-𝜃 consumer, where higher types have higher demand. A higher welfare weight thus captures
higher redistributive priority, such as lower income, disability, or other dimensions of social need. To
focus on in-kind redistribution, we rule out lump-sum cash transfers within the mechanism. Instead, we
capture the opportunity cost of public funds by assigning a welfare weight𝛼 to profit.
The key feature of our model is that the social planner has only partial control of the market. On
the one hand, the social planner faces a screening problem: she wants to distort consumption in order
to redirect surplus toward consumers with higher welfare weights. On the other hand, consumers retain
accesstotheprivatemarket. Thisgeneratesparticipationconstraintsthatlimitthesocialplanner’sability
to distort consumption and redirect surplus. Topping up changes these participation constraints: with
topping up, each consumer can purchase from both the social planner’s price schedule and the private
market; but without topping up, each consumer must choose between the two.
Our first main result characterizes the extensive margin: when the social planner should intervene.
Withouttoppingup,thesocialplannercanstrictlyimproveonlaissez-faireifandonlyifsomeconsumer’s
welfare weight exceeds the opportunity cost of public funds:
max
ˆ𝜃
𝜔( ˆ𝜃) >𝛼.
With topping up, the corresponding condition is stronger and requires the maximal upper-tail average
welfare weight to exceed the opportunity cost of public funds:
max
ˆ𝜃
E

𝜔(𝜃)| 𝜃≥ ˆ𝜃  >𝛼.
This comparison gives a precise, yet intuitive, sense in which topping up weakens screening. A small
subsidy targeted at typeˆ𝜃 cannot benefit only that type when topping up is allowed: all higher types
can also take the subsidized allocation and supplement in the private market. The first-order benefit of
intervention is thus governed by the average welfare weight in the upper tail rather than by the welfare
weightofthetargetedtypealone. Weformalizethisintuitiontoshowthatthesearepreciselytherelevant
sufficient statistics that determine when the social planner should intervene.
2

This extensive-margin result has sharp implications. First, suppose welfare weight and demand are
positively correlated, so that higher-demand consumers have higher redistributive priority—such as in
disabilitycareprograms. Inthiscase,toppingupdoesnotaffectthesocialplanner’sinterventiondecision,
because
max
ˆ𝜃
E

𝜔(𝜃)| 𝜃≥ ˆ𝜃  = max
ˆ𝜃
𝜔( ˆ𝜃).
Second, suppose welfare weight and demand are negatively correlated, so that lower-demand consumers
have higher redistributive priority—such as in housing assistance programs. In this case, topping up
reduces the scope for intervention, because
max
ˆ𝜃
E

𝜔(𝜃)| 𝜃≥ ˆ𝜃  = E[𝜔]≤ max
ˆ𝜃
𝜔( ˆ𝜃),
with strict inequality whenever welfare weights are not constant. Thus, the direction of correlation
between welfare weights and demand determines when topping up changes the intervention decision.
Our second main result characterizes the intensive margin: when topping up changes the optimal
mechanism. Whereas the extensive margin is governed by simple sufficient statistics, the intensive
margin depends on the entire distribution of welfare weights. The key object is a cutoff𝜃𝐿, the lowest
typeabovewhichtheupper-tailaveragewelfareweightexceedstheopportunitycostofpublicfunds. We
show that topping up and no topping up yield the same optimal mechanism if and only if two conditions
simultaneously hold: (i) there is no redistributive motive to intervene below𝜃𝐿, and (ii) the optimal
mechanism without topping up weakly expands the consumption of consumers above𝜃𝐿.
To show how topping up changes the optimal mechanism, we then characterize optimal mechanisms
under two benchmark correlations between welfare weights and demand. By solving for the optimal
allocation functions explicitly, we also obtain clean comparative static results on how the distribution of
welfare weights affects optimal redistribution.
Under positive correlation, topping up does not affect the optimal mechanism. Thus, both the social
planner’s extensive-margin and intensive-margin decisions are unaffected by topping up. The reason is
self-targeting: higher-demandconsumershavehigherredistributivepriority,sotoppingupdoesnotcreate
leakage away from the intended beneficiaries. In this case, the optimal mechanism has a lower-cutoff
3

demand
public option or private market subsidy program
(a) Positive correlation between welfare weight and demand
demand
public option subsidy program private market
(b) Negative correlation between welfare weight and demand
Figure 1: Graphical depictions of the optimal mechanism.
structure, shown in Figure 1(a). High types are served by a nonlinear subsidy program, while low types
are either served by a free public option or left to the private market, depending on whether the average
welfare weight exceeds the opportunity cost of public funds.
Undernegativecorrelation,however,toppingupcanchangetheoptimalmechanism. Withouttopping
up, the social planner can use low quantities to screen consumers: high-demand consumers must give
up their private-market consumption if they choose subsidized allocations intended for low-demand
consumers. With topping up, the social planner’s screening ability is weakened because high-demand
consumers can consume subsidized allocations and then supplement privately. In each case, the optimal
mechanism may involve a combination of a free public option, a nonlinear subsidy program, and the
private market, as shown in Figure 1(b). However, topping up reduces redistribution by reducing the
scope of intervention, the use of a free public option, and the mass of consumers served. Moreover,
topping up shifts redistribution away from consumers with higher redistributive priority to those with
lower redistributive priority.
Our comparative static results further highlight the differences between topping up and no topping
up. With topping up, a pointwise increase in welfare weights expands redistribution on all margins,
including a pointwise weakly higher optimal allocation. Without topping up, this monotonicity can fail:
under negative correlation, a pointwise increase in welfare weights can reduce the optimal allocations of
high-demand consumers. This is because low quantities retain screening value when topping up is not
allowed: the social planner may optimally distort subsidized allocations for higher-demand consumers
downward to redirect surplus toward the bottom.
4

This difference is even sharper under mean-preserving spreads of welfare weights, when demand
becomesstatisticallymoreinformativeaboutredistributivepriority. Withtoppingup,amean-preserving
spread of welfare weightsreduces redistribution under negative correlation: the loss from leakage to
higher types always dominates the gain in statistical informativeness. By contrast, without topping up,
a mean-preserving spread expands the scope of a free public option. Thus, topping up changes not just
optimalredistribution,butalsohowoptimalredistributionrespondstochangesinredistributivepriorities.
From a methodological perspective, we obtain explicit characterizations and comparative statics
by solving two mechanism-design problems with type-dependent outside options. With topping up, the
socialplannerfacesapointwiselower-boundconstraintrequiringeachtype’sconsumptiontoremainabove
his laissez-faire consumption. Without topping up, private-market access instead generates participation
constraintsthatcanbewrittenasmajorizationconstraints. Theseproblemsarerelated,butmathematically
distinct. Recent work solves linear programs with majorization constraints using extreme-point methods
(e.g., Kleiner, Moldovanu and Strack, 2021); by contrast, our programs maximize strictly concave
objectives,sotheoptimumneednotbeanextremepointofthefeasibleset. Instead,weuseaLagrangian
approach and generalized ironing methods. Whereas Jullien (2000) uses duality methods to show the
existence of Lagrange multipliers for such problems, we explicitly characterize the relevant Lagrange
multipliers in terms of primitives by adapting the approach of Amador and Bagwell (2013). In this
sense, our approach is closer to that of Dworczak and Muir (2024), who explicitly solve a class of linear
programs with majorization constraints in this way.1
1.1 Related Literature
Our paper contributes to the growing literature on inequality-aware mechanism design, which builds on
Weitzman’s(1977)observationthatdeparturesfromcompetitiveallocationscanfacilitateredistribution.
More recent work, including by Che, Gale and Kim (2013), Condorelli (2013), Dworczakr⃝ al. (2021),
Akbarpour r⃝ al.(2024),andPaiandStrack(2024),usesmechanism-designtoolstocharacterizeoptimal
1 A contemporaneous contribution by Kolotilin and Wolitzky (2026) also studies concave maximization with a majorization
constraint. Intheirmany-to-onematchingmodel,majorizationdescribesfeasibleworkforcecompositions,andthesolution
ischaracterizedusingdualpricesandfirst-orderconditions. Inourno-topping-upproblem,majorizationconstraintsinstead
arise from type-dependent participation constraints. We construct the corresponding Lagrange multipliers directly from
primitives, yielding generalized-ironing formulas and comparative statics.
5

redistributive allocations. Whereas most of this literature studies settings in which the social planner
designs the entire market, we study a social planner with only partial control of the market. Consumers
canalwaysaccessacompetitiveprivatemarket,andthisoutsideoptiongeneratesparticipationconstraints
that shape the optimal redistribution program.
The presence of a private market also connects our paper to the literature on partial mechanism
design, where only part of the market can be designed. This includes work on optimal interventions in
markets with adverse selection (Philippon and Skreta, 2012; Tirole, 2012; Fuchs and Skrzypacz, 2015),
pricing with resale (Loertscher and Muir, 2022), and optimal redistribution with a public option (Kang,
2023). Relative to this literature, we study a novel—but economically important—benchmark in which
thesocialplannerandtheprivatemarkethaveaccesstothesameproductiontechnology. Thisrepresents
a benchmark in which the social planner can costlessly contract with private producers to supply the
good. This benchmark also presents a greater technical challenge as it precludes any simplifications to
themechanism-designproblemthatmayarisefromproductive-efficiencyandtechnologicalasymmetries
between the social planner and private producers.
Finally, our paper also complements a large public finance literature on in-kind redistribution and
publicprovisionofprivategoods. StartingwithNicholsandZeckhauser(1982),thisliteratureemphasizes
that in-kind transfers can screen consumers better than cash transfers when intended beneficiaries value
the subsidized good differently from other consumers. Subsequent work studies how private markets
affect this screening logic, including by Blackorby and Donaldson (1988), Besley and Coate (1991), and
Gahvari and Mattos (2007).2 The closest paper in this literature is that of Blomquist and Christiansen
(1998),whostudywhetherpublicprovisionshouldallowrecipientstotopuptheirconsumptioninamodel
of labor supplyà laMirrlees (1971). Our paper differs in two respects. First, we focus on screening
through heterogeneous consumption preferences. Second, we allow the social planner to design an
arbitrary nonlinear price schedule rather than choosing only whether to provide a fixed quantity of the
2 FollowingRamsey(1927)andDiamond(1975),aseparateliteraturestudieshowcommoditytaxesshouldtradeoffefficiency
and redistributive concerns. The Atkinson–Stiglitz theorem (Atkinson and Stiglitz, 1976) provides a benchmark in which
differential commodity taxation is unnecessary when nonlinear income taxation is available and preferences are suitably
separable. This benchmark does not apply in our environment because consumers’ demand for the good is informative
about their welfare weights. In this sense, our paper is closer to work emphasizing preference heterogeneity as a reason
for goods-market interventions, including by Saez (2002) and Doligalskir⃝ Dworczak r⃝ Akbarpour r⃝ Kominers (2025).
Relativetothisliterature,wefocusonthedesignofnonlinearredistributionprogramswhenthesocialplannercannotfreely
redistribute in cash and consumers retain access to a private market.
6

good, which allows us to characterize how topping up affects both the extensive margin of intervention
and the intensive margin of optimal mechanism design.
1.2 Organization
The rest of the paper proceeds as follows. Section 2 introduces the model, and Section 3 characterizes
how topping up affects the extensive and intensive margins of optimal redistribution. Section 4 studies
the case of positive correlation between welfare weights and demand, while Section 5 studies the case of
negative correlation. Section 6 concludes. Proofs are collected in Appendices A and B.
2 Framework
Inthissection,wedevelopaframeworkthataccommodatesbothtoppingupandnotoppingup. Webegin
with a standard model of a private market and describe the laissez-faire benchmark. We then formulate
the social planner’s problem under the two participation structures.
2.1 Setup
There is a unit mass of consumers. Each consumer demands a quantity𝑞∈[ 0,𝐴] of a homogeneous,
perfectly divisible good, where𝐴 is the maximum feasible quantity. As is standard,𝑞 can equivalently
be interpreted as the quality level of an indivisible good of which each consumer consumes one unit.
Although that interpretation may be more natural in some applications, we use the language of quantity
throughout for consistency. The good is supplied competitively in a private market by producers with
constant marginal cost𝑐 >0.
Consumers have quasilinear preferences over money and differ in their demand for the good. Each
consumer privately observes his type𝜃 ∈ [𝜃,𝜃] ⊂R++, drawn from a continuously differentiable
distribution𝐹 with positive density𝑓 on[𝜃,𝜃]. A type-𝜃 consumer who consumes𝑞 units of the good
and makes total payment𝑡 obtains utility
𝜃𝑣(𝑞)− 𝑡.
7

We assume that𝑣 :[0,𝐴]→ R+ is twice continuously differentiable, increasing,3 and strictly concave
with𝑣′′< 0, so consumers have positive but diminishing marginal utility from consumption.
Laissez-faire benchmark. Given a constant marginal price𝑝 for the good, denote the demand curve
of a type-𝜃 consumer by
𝐷(𝑝,𝜃)∈ arg max
𝑞∈[ 0,𝐴]
[𝜃𝑣(𝑞)− 𝑝𝑞].
Because𝑣 is strictly concave,𝐷(𝑝,𝜃) is uniquely defined for any𝑝,𝜃 > 0. For notational convenience,
extend the domain of(𝑣′)−1 toR by setting(𝑣′)−1(𝑧)= 0 for𝑧≥𝑣′(0) and(𝑣′)−1(𝑧)= 𝐴 for𝑧≤𝑣′(𝐴);
then𝐷(𝑝,𝜃)=(𝑣′)−1(𝑝/𝜃) for𝑝,𝜃 > 0.
Under perfect competition, the good is sold at marginal cost𝑐. Let 𝑞LF(𝜃) ≔ 𝐷(𝑐,𝜃) denote the
laissez-faire consumption of a type-𝜃 consumer, and denote his corresponding laissez-faire utility by
𝑈LF(𝜃). For simplicity, we assume throughout that laissez-faire demand is interior:im𝑞LF⊆( 0,𝐴).
2.2 Social Planner’s Problem
A social planner seeks to redistribute by offering an alternative price schedule for the good. Unlike
the private-market price schedule, which is linear under perfect competition, the social planner’s price
schedule may be nonlinear.
Weassumethatthesocialplannerhasaccesstothesameproductiontechnologyastheprivatemarket
and hence faces the same marginal cost𝑐. Equivalently, the social planner may be able either to contract
with producers or to reimburse consumers for private purchases at no additional resource cost. This
assumption allows us to isolate the effects of topping up on screening, abstracting from other frictions.
We can therefore formulate the social planner’s problem in terms oftotalconsumption and payment.
The social planner chooses a direct mechanism(𝑞,𝑡) consisting of:
(i) an allocation function𝑞 :[𝜃,𝜃]→[ 0,𝐴], where𝑞(𝜃) is the consumer’s total consumption; and
(ii) a payment function𝑡 :[𝜃,𝜃]→ R, where𝑡(𝜃) is the consumer’s total payment.
3 Throughout,“increasing”and“decreasing”meanstrictlyincreasingandstrictlydecreasing,respectively;weakmonotonicity
is denoted by “nondecreasing” and “nonincreasing.”
8

This formulation implicitly restricts attention to deterministic mechanisms; as we show in Appendix A,
this restriction is without loss of generality.
We require the mechanism to satisfy incentive compatibility, so truthful reporting is optimal:
𝜃∈ arg max
𝜃′∈[𝜃,𝜃]
[𝜃𝑣(𝑞(𝜃′))− 𝑡(𝜃′)], for all𝜃∈[ 𝜃,𝜃]. (IC)
By the revelation principle (Myerson, 1979), this restriction is without loss of generality.
Wealsofocusonmechanismsforin-kindredistributionbyrulingoutlump-sumcashtransferswithin
the mechanism. Specifically, we impose the no-lump-sum-transfers constraint
𝑡(𝜃)≥ 0, for all𝜃∈[ 𝜃,𝜃]. (LS)
Thus,whilethesocialplannermayfullysubsidizesomeunitsofthegood—thatis,settheirpricetozero—
she cannot make direct cash transfers through the mechanism. Cash transfers outside the mechanism are
nonetheless permitted in reduced form through the social planner’s objective, via the weight assigned to
the monetary surplus generated by the mechanism, as described below.
Thekeydifferencebetweentoppingupandnotoppingupliesinhowprivatemarketaccessconstrains
feasible mechanisms:
(i) No topping up.When topping up is not allowed, each consumer may purchase the good either
from the social planner or in the private market, but not both. The consumer’s outside option is
therefore the laissez-faire utility:
𝜃𝑣(𝑞(𝜃))− 𝑡(𝜃)≥ 𝑈LF(𝜃), for all𝜃∈[ 𝜃,𝜃]. (IR)
(ii) Toppingup. Whentoppingupisallowed,eachconsumermaysupplementconsumptionpurchased
from the social planner by buying additional units in the private market at marginal price𝑐.
Equivalently, the socialplanner maysubsidize marginalunits ofconsumption, but cannotraise the
consumer’s effective marginal price above𝑐. Relative to the no-topping-up case, this imposes an
9

additional feasibility constraint on total consumption:
𝑞(𝜃)≥ 𝑞LF(𝜃), for all𝜃∈[ 𝜃,𝜃]. (TU)
This distinction captures the key tradeoff between flexibility and targeting. Holding fixed the social
planner’s price schedule, topping up weakly benefits consumers because it expands their choice set. At
the same time, it restricts the set of feasible mechanisms available to the social planner, because the
mechanism must now deter consumers from a broader set of deviations from their intended allocations.
Thesocialplannerevaluatesmechanismsaccordingtoweightedtotalsurplus,consistingofconsumer
surplus and profit (i.e., total revenue net of production cost):
(i) Consumersurplus. Thesocialplannerassignswelfareweight 𝜔(𝜃) toaconsumeroftype 𝜃. This
is the gross social value of transferring one unit of money to that consumer.4 Throughout, we
assume for simplicity that𝜔 :[𝜃,𝜃]→ R+ is continuous.
(ii) Profit. The social planner assigns welfare weight𝛼∈ R++ to the monetary surplus generated by
the mechanism, namely revenue net of production cost. Thus,𝛼 captures the opportunity cost of
public funds. This opportunity cost is high when, for example, the social planner has alternative
redistributiveinstruments—suchascashtransfers—thatcompeteforthesamefunds,andlowwhen
the social planner faces political constraints5 that limit redistribution outside the mechanism.
Accordingly, the social planner chooses a feasible mechanism to maximize weighted total surplus:
max
(𝑞,𝑡)
∫ 𝜃
𝜃

𝜔(𝜃)[𝜃𝑣(𝑞(𝜃))− 𝑡(𝜃)]|                 {z                 }
consumer surplus
+𝛼[𝑡(𝜃)− 𝑐𝑞(𝜃)]|            {z            }
total profit

d𝐹(𝜃), (OBJ)
s.t.(𝑞,𝑡) satisfies (IC), (IR), (LS), and, when topping up is allowed, (TU).
The set of feasible mechanisms is nonempty, since the laissez-faire mechanism(𝑞LF,𝑐𝑞 LF) is feasible
4 Dworczak r⃝ al.(2021)microfoundsuchwelfareweightsasexpectedmarginalutilitiesofmoneyconditionalonconsumers’
demand types.
5 Forinstance,LiscowandPershing(2022)showthatthegeneralpopulationintheU.S.largelyprefersin-kindredistribution
to cash transfers.
10

under both participation structures. In Appendix A, we show that each program admits an essentially
uniquesolution. 6 Wewrite(𝑞∗,𝑡∗) fortheoptimalmechanismwithouttoppingupand (𝑞∗ TU,𝑡∗ TU) forthe
optimal mechanism with topping up.
3 Topping Up vs. No Topping Up
Wenowcompareoptimalredistributionwithandwithouttoppingup. Wefirstcharacterizetheextensive
marginofintervention: whentheoptimalmechanismstrictlyimprovesonthelaissez-faireoutcomeunder
each participation structure. We then turn to the intensive margin: when, conditional on intervention,
topping up changes the optimal mechanism itself.
3.1 How Does Topping Up Change When the Social Planner Intervenes?
Our first main result addresses the extensive margin of intervention by characterizing the intervention
region under each participation structure.7
Theorem 1.The optimal mechanism strictly improves on the laissez-faire outcome if and only if
 

max
ˆ𝜃∈[𝜃,𝜃]
E

𝜔(𝜃)| 𝜃≥ ˆ𝜃  >𝛼, when topping up is allowed,
max
ˆ𝜃∈[𝜃,𝜃]
𝜔( ˆ𝜃) >𝛼, when topping up is not allowed.
Theorem 1 shows that the extensive-margin intervention decision is pinned down by two sufficient
statistics: with topping up, the maximal upper-tail average welfare weight; and without topping up, the
pointwise maximal welfare weight. If all welfare weights are equal to𝛼, then Theorem 1 implies that
6 Throughout, we consider mechanisms to be equivalent if their allocations differ only on a set of measure zero. We show
the optimal allocation function is unique in both programs. For any given allocation function, incentive compatibility
pins down the payment function up to an additive constant. WhenE[𝜔] ≠ 𝛼, the social planner’s objective pins down
this constant at one endpoint of the feasible interval. WhenE[𝜔] = 𝛼, the objective is independent of this constant, so
there may be multiple optimal payment functions implementing the same allocation. In that case, whenever a selection is
needed, we select the pointwise-smallest feasible payment function. This selection is consumer-optimal among optimal
implementations because it gives every type the highest feasible utility conditional on the optimal allocation.
7 Foreaseofnotation,weextendthedomainoftheupper-tailconditionalexpectationfunction ˆ𝜃↦→ E  𝜔(𝜃)| 𝜃≥ ˆ𝜃  to ˆ𝜃=𝜃
by continuity. By the Lebesgue differentiation theorem,E
h
𝜔(𝜃)| 𝜃≥𝜃
i
≔ lim ˆ𝜃→𝜃 E

𝜔(𝜃)| 𝜃≥ ˆ𝜃  =𝜔(𝜃).
11

laissez-faireisoptimalunderbothparticipationstructures,whichistheFirstWelfareTheorembenchmark
inthepresentenvironment. Moregenerally,departuresofwelfareweightsfrom 𝛼canjustifyintervention,
and topping up matters precisely because these two sufficient statistics need not coincide.
ByTheorem1,toppingupreplacesthepointwisemaximalwelfareweightwiththemaximalupper-tail
average welfare weight in determining the intervention decision. Since averages cannot exceed maxima,
max
ˆ𝜃∈[𝜃,𝜃]
𝜔( ˆ𝜃)≥ max
ˆ𝜃∈[𝜃,𝜃]
E

𝜔(𝜃)| 𝜃≥ ˆ𝜃  .
It follows that the social planner intervenes in weakly fewer environments when topping up is allowed.
Equality holds if and only if the highest type has the highest welfare weight:𝜔(𝜃)= max ˆ𝜃∈[𝜃,𝜃]𝜔( ˆ𝜃).
An immediate corollary characterizeswhentopping up changes the optimal intervention decision:
Corollary 1.Topping up changes the optimal intervention decision if and only if
max
ˆ𝜃∈[𝜃,𝜃]
𝜔( ˆ𝜃) >𝛼 ≥ max
ˆ𝜃∈[𝜃,𝜃]
E

𝜔(𝜃)| 𝜃≥ ˆ𝜃  .
Taken together, Theorem 1 and Corollary 1 identify a precise sense in which topping up weakens
screening: it reduces the social planner’s marginal incentive to intervene. The intuition is easiest to see
from the first-order welfare effects of a small subsidy:
(i) Topping up. When topping up is allowed, the subsidy cannot be targeted to a single type in
isolation. If the social planner subsidizes consumption beyond the laissez-faire quantity of some
type ˆ𝜃, then all higher types benefit, since they can always mimic the consumer of typeˆ𝜃 and then
supplementtheirsubsidizedallocationsintheprivatemarket. Thefirst-orderbenefitofintervention
therefore depends on whether the upper-tail average welfare weightE

𝜔(𝜃)| 𝜃≥ ˆ𝜃  exceeds𝛼.
Although some nearby lower types may also distort their consumption upward to qualify for the
subsidy, those distortion costs are local and higher-order for sufficiently small interventions.
(ii) No topping up.When topping up is not allowed, the social planner can target the subsidy more
narrowly as consumers must choose between the subsidized allocation and the private market. It
therefore suffices that some type has welfare weight above𝛼.
12

We prove Theorem 1 in Appendix A by formalizing this intuition.
3.2 When Does Topping Up Change the Optimal Mechanism?
While Theorem 1 shows how topping up reduces the social planner’s marginal incentive to intervene, it
does not yet say when topping up changes the solution to the social planner’s full problem. As such, we
now compare the optimal mechanisms across the two participation structures.
Our second main result characterizes when topping up changes the optimal mechanism. To state it,
we introduce three objects. First, for any𝜇≥ 0, define thegeneralized virtual valuation,
𝐽𝜇(𝜃)≔𝜃+
𝜇𝜃·𝛿𝜃(𝜃)+
∫ 𝜃
𝜃 [𝜔(𝑠)− 𝛼] d𝐹(𝑠)
𝛼𝑓(𝜃) . (1)
Here,𝜇≥ 0istheshadowcostofthe(LS)constraint. Thus, 𝐽𝜇(𝜃) capturesthesocialvalueofincreasing
the allocation of type𝜃 once the in-kind restriction and incentive constraints are taken into account.
Second, following Myerson (1981) and Toikka (2011), define theironing operatoras follows. For any
generalized functionℎ with domain[𝜃,𝜃], let its ironed versionℎ :[𝜃,𝜃]→ R be the nondecreasing
function
ℎ(𝜃)≔− d d𝑧

𝑧↦→ co
∫ 𝜃
𝐹−1(𝑧)
ℎ(𝑠) d𝐹(𝑠)
!

𝑧=𝐹(𝜃)
,
where co𝐻 isthepointwisesmallestconcavefunctionthatweaklyexceedsagivenfunction 𝐻 :[0, 1]→
R. More generally, for any interval𝐼 ⊆ [𝜃,𝜃], we writeℎ|𝐼 for the ironing of the restriction ofℎ to
𝐼, defined analogously with the concavification over the corresponding quantile interval𝐹(𝐼). Finally,
define thetopping-up cutoff type,
𝜃𝐿 ≔ min
(
ˆ𝜃∈[ 𝜃,𝜃] :
∫ 𝜃
ˆ𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)≥ 0
)
. (2)
Equivalently,𝜃𝐿 is the lowest type above which the upper-tail average welfare weight weakly exceeds𝛼.
13

Theorem 2.Let𝜇∗ ≔(E[𝜔]− 𝛼)+. The optimal mechanisms with and without topping up coincide if
and only if:
 

𝐽𝜇∗|[𝜃𝐿,𝜃](𝜃)≥ 𝜃, for𝜃𝐿≤𝜃≤𝜃,
𝜔(𝜃)≤ 𝛼, for𝜃≤𝜃 <𝜃𝐿.
Moreover, if these conditions are satisfied, then the optimal allocation function is
𝑞∗(𝜃)=
 

𝐷

𝑐,𝐽𝜇∗|[𝜃𝐿,𝜃](𝜃)

, for𝜃𝐿≤𝜃≤𝜃,
𝑞LF(𝜃), for𝜃≤𝜃 <𝜃𝐿.
Theorem 2 provides a sharp characterization of when topping up changes the optimal mechanism.
The optimal mechanisms with and without topping up coincide if and only if the social planner has no
redistributive motive to intervene below𝜃𝐿 and, above𝜃𝐿, the no-topping-up solution already distorts
consumption upward relative to the laissez-faire allocation.
Although Theorem 2 is proven formally in Appendix A, the intuition is straightforward. Below𝜃𝐿,
topping up is most restrictive because any subsidized option can be supplemented by higher types in
the private market, making narrowly targeted transfers difficult to implement. If some type below𝜃𝐿
has welfare weight above𝛼, then by Theorem 1 the social planner would like to intervene there without
toppingup,butcannotdosointhesamewayoncetoppingupisallowed. Above 𝜃𝐿,interventionbecomes
potentiallysociallydesirable,andtherelevantquestioniswhethertheoptimalallocationwithouttopping
upsatisfiesthe(TU)constraint. ThecorrespondingconditioninTheorem2characterizespreciselywhen
that constraint is satisfied for these types.
Theorem 2 also clarifies how the intensive-margin effects of topping up differ from the extensive-
margin effects in Theorem 1. The intervention decision depends only on two sufficient statistics of the
welfare weights, whereas whether topping up changes the optimal mechanism depends on the entire
distribution of welfare weights.
In the next sections, we study how topping up changes the structure of optimal redistribution.
14

4 Optimal Redistribution: Positive Correlation
We now study the case in which welfare weights are positively correlated with demand.
Assumption 1(positive correlation). The welfare weight function𝜔 :[𝜃,𝜃]→ R+ is increasing.
Assumption1capturesenvironmentsinwhichthesocialplanner’sredistributiveprioritiesarealigned
with consumer demand. A natural example is disability care: social programs may place greater weight
on individuals with more severe disabilities, whose consumption of care services is likely to be higher.
Under Assumption 1, the two sufficient statistics in Theorem 1 coincide:
max
ˆ𝜃∈[𝜃,𝜃]
E

𝜔(𝜃)| 𝜃≥ ˆ𝜃  =𝜔(𝜃)= max
ˆ𝜃∈[𝜃,𝜃]
𝜔( ˆ𝜃).
Hence topping up does not affect the extensive margin of optimal redistribution. In fact, under positive
correlation it does not affect the intensive margin either:
Corollary 2.Under Assumption 1, the optimal mechanisms with and without topping up coincide.
4.1 Characterization of the Optimal Mechanism
Given Corollary 2, we can characterize the optimal mechanism under positive correlation without
distinguishing between the two participation structures.
Theorem 3.Let𝜇∗≔(E[𝜔]− 𝛼)+. Under Assumption 1, the optimal allocation function is
𝑞∗(𝜃)=
 

𝐷

𝑐,𝐽𝜇∗|[𝜃𝐿,𝜃](𝜃)

, for𝜃𝐿≤𝜃≤𝜃,
𝑞LF(𝜃), for𝜃≤𝜃 <𝜃𝐿.
As in Theorem 2, the structure of the optimal mechanism under positive correlation is governed by
twoobjects: thetopping-upcutofftype 𝜃𝐿,definedinequation(2),andthemultiplier 𝜇∗=(E[𝜔]− 𝛼)+.
As we now explain,𝜃𝐿 determines which consumers are served by the social planner rather than left to
the private market, while𝜇∗ determines whether a free public option is used.
15

By Theorem 3, the optimal allocation has a cutoff structure. Consumers with𝜃 < 𝜃𝐿 receive their
laissez-faireallocationandmakethecorrespondingprivate-marketpayment,whilethosewith 𝜃≥𝜃𝐿 are
served by the social planner. Under positive correlation, these higher types have higher welfare weights,
and they face a nonlinear subsidy schedule that weakly raises consumption relative to laissez-faire.
The multiplier𝜇∗ determines whether the bottom of this subsidized region takes the form of a free
public option. When𝜇∗ > 0, the generalized virtual valuation𝐽𝜇∗ has an atom at𝜃, so𝐽𝜇∗|[𝜃𝐿,𝜃]—and
hence the allocation𝑞∗—is flat on an initial interval. Moreover, the proof of Theorem 3 shows that𝜇∗
is the shadow cost of the (LS) constraint. Since𝜇∗ > 0, that constraint binds on this interval, implying
that consumers there pay zero. We therefore interpret this flat initial segment of the allocation as a free
public option. By contrast, when𝜇∗ = 0, the social planner does not use a free public option. Any
redistributionusesonlyanonlinearsubsidyschedule,withtheassociatedpaymentschedulepinneddown
by the allocations characterized by Theorem 3 and the envelope theorem.
These observations imply that the optimal mechanism takes one of the following forms:
(i) If𝛼≥ E[𝜔], low types are left to the private market, while high types are served by the social
planner. In this case,𝜇∗ = 0, so there is no free public option. Moreover, the definition of𝜃𝐿
implies that𝜃𝐿 > 𝜃if𝛼 >E[𝜔] (with𝜃𝐿 =𝜃 if𝛼= E[𝜔]). Consumers with𝜃 < 𝜃𝐿 receive their
laissez-faire allocation, whereas consumers with𝜃≥𝜃𝐿 are subsidized and consume weakly more
than under laissez-faire. Figure 2(a) illustrates this case. As a special case, if𝛼 > max𝜔, then
𝜃𝐿 =𝜃, so the subsidized region is empty and laissez-faire is optimal, consistent with Theorem 1.
Bycontrast,if 𝛼= E[𝜔],then 𝜃𝐿 =𝜃andallconsumersareservedbyanonlinearsubsidyprogram.
(ii) If𝛼 <E[𝜔], all consumers are served by the social planner, and the optimal mechanism always
includes a free public option as𝜇∗ =(E[𝜔]− 𝛼)+ > 0. The lowest types are pooled into the
free public option, while higher types purchase additional quantities through the social planner’s
nonlinear subsidy program. Figure 2(b) illustrates this case.
16

𝑞LF 𝑞∗
private market subsidy program
0 𝜃
quantity,𝑞
𝜃 𝜃𝜃𝐿
(a)𝛼≥ E[𝜔]
𝑞LF 𝑞∗
𝑞∗(𝜃)
public option subsidy program
0 𝜃
quantity,𝑞
𝜃 𝜃
(b)𝛼 <E[𝜔]
Figure 2: Structure of the optimal allocation function under positive correlation characterized by Theorem 3.
17

4.2 Discussion
TheexplicitcharacterizationoftheoptimalallocationinTheorem3yieldstransparentcomparativestatics
withrespecttothewelfareweightfunction 𝜔. Weconsidertwopartialordersonwelfareweightfunctions.
Thefirstcompareswelfareweightspointwiseandcapturesincreasesinredistributiveprioritiesrelativeto
the opportunity cost of public funds𝛼. The second compares welfare weights through mean-preserving
spreads and captures changes in how redistributive priorities are distributed across types while holding
their average level fixed.
We begin with pointwise increases in welfare weights.
Proposition 1.Let𝜔𝐻 and𝜔𝐿 be welfare weight functions satisfying Assumption 1, such that𝜔𝐻≥𝜔𝐿
pointwise. Then:
(i) the multiplier𝜇∗ is weakly higher under𝜔𝐻;
(ii) the topping-up cutoff type𝜃𝐿 is weakly lower under𝜔𝐻; and
(iii) the optimal allocation function𝑞∗ is weakly higher under𝜔𝐻.
Proposition1showsthatapointwiseincreaseinwelfareweightsweaklyexpandsredistributiononall
margins. ByTheorem3, thesocialplannerservesweaklymoretypesandweaklyraisesconsumptionfor
a larger set of consumers. Moreover, sufficiently large increases in welfare weights can change the form
ofoptimalredistribution: when E[𝜔] risesabove 𝛼,thesocialplannerbeginstouseafreepublicoption.
Because only the welfare weights relative to𝛼 matter for the social planner’s problem, Proposition 1
canequivalentlybeinterpretedasacomparativestaticintheopportunitycostofpublicfunds. Holding 𝜔
fixed,adecreasein 𝛼 increasestherelativevalueofredistributioninexactlythesamewayasapointwise
increase in welfare weights: more consumers are served, consumption rises for a larger set of types, and
the social planner is more likely to provide a free public option.
Next,considerchangesinthedistributionofwelfareweightsacrosstypeswhileholdingtheiraverage
level fixed. For increasing welfare weight functions with the same mean, we say that𝜔𝐻 is amean-
preserving spreadof𝜔𝐿 if
∫ 𝜃
𝜃
𝜔𝐻(𝑠) d𝐹(𝑠)≥
∫ 𝜃
𝜃
𝜔𝐿(𝑠) d𝐹(𝑠), for all𝜃∈[ 𝜃,𝜃]. (3)
18

Proposition 2.Suppose𝜔𝐻 and𝜔𝐿 are welfare weight functions satisfying Assumption 1 such that𝜔𝐻
is a mean-preserving spread of𝜔𝐿, as defined in equation(3). Then:
(i) the multiplier𝜇∗ is unchanged;
(ii) the topping-up cutoff type𝜃𝐿 is weakly lower for𝜔𝐻; and
(iii) the optimal allocation function𝑞∗ is weakly higher under𝜔𝐻.
Proposition 2 shows that a mean-preserving spread of welfare weights, like a pointwise increase,
also weakly expands redistribution. By shifting welfare weight toward consumers with higher types, a
mean-preservingspreadalignsredistributiveprioritiesmorecloselywithmarketdemand. ByTheorem3,
thesocialplannerservesweaklymoretypesandweaklyraisesconsumptionforalargersetofconsumers.
UnlikeProposition1,however,amean-preservingspreaddoesnotaffecttheformofoptimalredistribution:
since𝜇∗ is unchanged, this comparative static does not affect whether a free public option is used.
Taken together, Propositions 1 and 2 identify two distinct channels through which welfare weights
shape optimal redistribution. Specifically, both comparative statics expand redistribution, but they do
so for different reasons: pointwise increases in welfare weights raise the social value of redistribution
overall, whereas mean-preserving spreads better align redistributive priorities with market demand.
More broadly, our results in this section complement the classic self-targeting logic in the literature.
Thatliteratureemphasizesthatredistributivesubsidiesworkbestwhenintendedbeneficiariesarealsothe
consumersmostlikelytopurchasethesubsidizedgood. InthelanguageoftheIMF’s PublicExpenditure
Handbook (Mackenzie, 1991), “[m]arketed goods with a negative income elasticity (i.e., inferior goods)
are ideal candidates for a redistributive subsidy.” Our results show that the same logic also governs
how much topping up constrains optimal redistribution. When welfare weight is positively correlated
with demand, the market helps rather than hinders redistribution, so the screening loss from allowing
topping up disappears. In this sense, the familiar principle that inferior goods are attractive targets for
redistribution has a further implication here: such goods are not only easier to target, but also more
compatible with topping up.
19

5 Optimal Redistribution: Negative Correlation
Next, we turn to the case in which welfare weights are negatively correlated with demand.
Assumption 2(negative correlation). The welfare weight function𝜔 :[𝜃,𝜃]→ R+ is decreasing.
Assumption2capturesenvironmentsinwhichthesocialplanner’sredistributiveprioritiesrunagainst
consumer demand. Housing is a natural example: the intended beneficiaries of redistribution are often
those with lower demand, reflecting lower ability to pay. More generally, many normal goods are likely
to exhibit this pattern, as higher demand is associated with lower marginal value for money (Dworczak
r⃝ al., 2021).
This case reverses the self-targeting logic from Section 4. As Theorem 1 shows, when topping up is
allowed,thefirst-orderbenefitsofinterventionaccruetoalltypesabovethetargetedtype. Underpositive
correlation, this is consistent with the social planner’s redistributive priorities, since higher types have
higherwelfareweights. Undernegativecorrelation,however,thesameforcegeneratesleakage: subsidies
intended for low types also benefit higher types, weakening the social planner’s ability to screen.
This difference is already apparent at the extensive margin. Under Assumption 2, the two sufficient
statistics in Theorem 1 are
max
ˆ𝜃∈[𝜃,𝜃]
E

𝜔(𝜃)| 𝜃≥ ˆ𝜃  = E[𝜔] <𝜔(𝜃)= max
ˆ𝜃∈[𝜃,𝜃]
𝜔( ˆ𝜃).
It follows from Corollary 1 that topping up strictly reduces the set of environments in which the social
planner intervenes whenever the opportunity cost of public funds satisfiesE[𝜔]≤ 𝛼 <𝜔(𝜃).
The next corollary shows that topping up can affect the intensive margin as well.
Corollary3. UnderAssumption2,thereexists 𝛼min∈R+ satisfying min𝜔≤𝛼min < E[𝜔],suchthatthe
optimal mechanisms with and without topping up differ if and only if𝛼min <𝛼 < max𝜔.
5.1 Characterization of the Optimal Mechanisms
Wenowcharacterizehowtheoptimalmechanismsdifferwhen 𝛼liesintheregionidentifiedbyCorollary3.
20

Unlikeunderpositivecorrelation,theoptimalmechanismshaveanupper-cutoffstructure. Lowtypes,
who have high welfare weights, are served by the social planner, whereas sufficiently high types are left
to the private market.
The cutoff differs across the two participation structures because topping up weakens the screening
value of low quantities. With topping up, high types can choose a subsidized allocation and supplement
itintheprivatemarket. Withouttoppingup,choosingasubsidizedallocationrequiresgivingupprivate-
market consumption.
Wecharacterizetheoptimalmechanismsusingcutoffs 𝜃𝐻 TU and𝜃𝐻,whichdeterminethehighesttype
servedbythesocialplannerwithandwithouttoppingup,respectively. Forthetopping-upproblem,using
the generalized virtual valuation in equation (1), define𝜃𝐻 TU :R+→[ 𝜃,𝜃] by
𝜃𝐻 TU(𝜇)≔ inf n 𝜃∈[ 𝜃,𝜃] :𝐽𝜇|[𝜃,𝜃](𝜃)≤ 𝜃 o , (4)
with the convention that𝜃𝐻 TU(𝜇)=𝜃 if the set is empty. For the no-topping-up problem, let
𝜇max≔ max
𝜃∈[𝜃,𝜃]
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠). (5)
For𝜇∈[ 0,𝜇 max], define
𝜃𝐻(𝜇)≔ max
(
𝜃∈[ 𝜃,𝜃] :
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)≥ 𝜇
)
. (6)
Next, define the optimal multipliers on the no-lump-sum-transfers constraint (LS). For the topping-up
problem, the optimal multiplier is the same as under positive correlation (see Theorem 3):
𝜇∗ TU≔(E[𝜔]− 𝛼)+. (7)
21

For the no-topping-up problem, let
 

𝑞𝜇(𝜃)≔𝐷

𝑐,

𝐽𝜇+ 𝜇+𝛼− E[𝜔] 𝛼𝑓 

 [𝜃,𝜃𝐻(𝜇)] (𝜃) ! ,
𝑈𝐻(𝜇)≔𝜃𝑣(𝑞𝜇(𝜃))+
∫ 𝜃𝐻(𝜇)
𝜃
𝑣(𝑞𝜇(𝑠)) d𝑠.
(8)
The optimal multiplier is then given by
𝜇∗≔ min  𝜇∈[(E[𝜔]− 𝛼)+,𝜇 max] :𝑈𝐻(𝜇)≥ 𝑈LF(𝜃𝐻(𝜇)) 	 . (9)
Theorem 4.Under Assumption 2:
(i) the optimal allocation function with topping up is
𝑞∗ TU(𝜃)=
 

𝑞LF(𝜃), for𝜃𝐻 TU(𝜇∗ TU) <𝜃 ≤𝜃,
𝐷

𝑐,𝐽𝜇∗ TU|[𝜃,𝜃𝐻 TU(𝜇∗ TU)](𝜃)

, for𝜃≤𝜃≤𝜃𝐻 TU(𝜇∗ TU);
(ii) the optimal allocation function without topping up is
𝑞∗(𝜃)=
 

𝑞LF(𝜃), for𝜃𝐻(𝜇∗) <𝜃 ≤𝜃,
𝑞𝜇∗(𝜃), for𝜃≤𝜃≤𝜃𝐻(𝜇∗).
Theorem 4 shows that each optimal mechanism is governed by the same two kinds of objects—a
cutoff and a multiplier—as in Theorems 2 and 3, albeit in a more complex way. As before, the cutoffs
𝜃𝐻 TU(𝜇∗ TU) and𝜃𝐻(𝜇∗) determinewhichconsumersareservedbythesocialplanner,whilethemultipliers
𝜇∗ TU and𝜇∗ determine whether a free public option is used. Under negative correlation, however, these
objects are now constructed differently:
(i) Toppingup. Whentoppingupisallowed,theseobjectsaredeterminedsequentially: themultiplier
is pinned down by(E[𝜔]− 𝛼)+ as in Theorems 2 and 3, and the cutoff is then determined by the
ironed generalized virtual valuation corresponding to this multiplier.
22

(ii) Notoppingup. Whentoppingupisnotallowed,theseobjectsarejointlydetermined: themultiplier
acts as the threshold for the cumulative welfare-weight condition determining the cutoff, while the
cutoff determines the marginal participation constraint that pins down the multiplier.
Wenowexplaintheimplicationsforoptimalmechanisms. AlthoughTheorem4appliesmorebroadly,
we focus on𝛼min <𝛼 < max𝜔 to highlight the effect of topping up, following Corollary 3.
(i) If E[𝜔]≤ 𝛼 <max𝜔, topping up changes the extensive margin. Figure 3(a) illustrates this case.
With topping up, the social planner does not intervene. In this case,𝜇∗ TU = 0, so there is no free
public option; moreover, since𝜔 is decreasing,
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)≤ 0 =⇒ 𝐽0(𝜃)≤ 𝜃, for all𝜃∈[ 𝜃,𝜃].
Thus, by equation (4),𝜃𝐻 TU(0) = 𝜃, so the social planner does not use a subsidy program either.
This is consistent with Theorem 1.
Without topping up, high types are left to the private market, while low types are served by the
socialplanner. Thecutoff 𝜃𝐻(𝜇∗) andmultiplier 𝜇∗arejointlydeterminedbyequations(6)and(9);
the mechanism includes a free public option if and only if𝜇∗ > 0. In the limit as𝛼→ max𝜔,
𝜇max = 0 and𝜃𝐻(0) =𝜃 by equations (5) and (6). Equation (9) then implies𝜇∗ = 0, so the social
planner does not intervene, consistent with Theorem 1.
(ii) If𝛼min <𝛼 < E[𝜔], topping up changes the intensive margin. Figure 3(b) illustrates this case.
With topping up, high types are left to the private market, while low types are served by the social
planner. Since 𝜇∗ TU =(E[𝜔]− 𝛼)+ > 0, the optimal mechanism always includes a free public
option and serves consumers up to the cutoff𝜃𝐻 TU(𝜇∗ TU) determined by equation (4).
Withouttoppingup,lowtypesareservedbythesocialplanner,uptothecutoff 𝜃𝐻(𝜇∗). Thecutoff
isequalto 𝜃if𝜇∗= E[𝜔]−𝛼,inwhichcaseallconsumersareserved;however,thecutoffisinterior
if𝜇∗ > E[𝜔]− 𝛼,inwhichcasehightypesarelefttotheprivatemarket. Since 𝜇∗≥ E[𝜔]− 𝛼 >0
by equation (9), the optimal mechanism always includes a free public option.
23

𝑞∗ TU
𝑞LF
𝜃𝐻(𝜇∗)
𝑞∗
𝑞∗(𝜃)
private market
private marketpublic option subsidy program
0 𝜃
quantity,𝑞
𝜃 𝜃
(a) E[𝜔]≤ 𝛼 <max𝜔
𝑞∗ TU
𝑞∗ TU(𝜃) 𝜃𝐻 TU(𝜇∗ TU)
𝑞LF
𝑞∗
𝜃𝐻(𝜇∗)
𝑞∗(𝜃)
p.o. subsidy program private market
public option subsidy program p.m.
0 𝜃
quantity,𝑞
𝜃 𝜃
(b)𝛼min <𝛼 < E[𝜔]
Figure 3: Structure of the optimal allocation function under negative correlation characterized by Theorem 4.
24

5.2 Discussion
The explicit characterization of the optimal allocations in Theorem 4 allows us to compare the two
participation structures directly. We begin by comparing the levels of optimal redistribution with and
without topping up.
Proposition 3.The multipliers𝜇∗ TU,𝜇∗ and cutoffs𝜃𝐻 TU(𝜇∗ TU),𝜃 𝐻(𝜇∗) satisfy
𝜇∗ TU≤ 𝜇∗ and 𝜃𝐻 TU(𝜇∗ TU)≤ 𝜃𝐻(𝜇∗).
Moreover, the optimal allocation function without topping up𝑞∗ crosses the optimal allocation function
with topping up𝑞∗ TU at most once from above: that is, there existsˆ𝜃∈[ 𝜃,𝜃] such that
 

𝑞∗(𝜃)≤ 𝑞∗ TU(𝜃), for𝜃 > ˆ𝜃,
𝑞∗(𝜃)≥ 𝑞∗ TU(𝜃), for𝜃 < ˆ𝜃.
As Proposition 3 shows, topping up weakly reduces redistribution on two margins. First, it weakly
reduces the multiplier on the no-lump-sum-transfers constraint, and hence weakly reduces the scope for
a free public option. Second, it weakly lowers the highest type served by the social planner. Thus, under
negativecorrelation,toppingupnotonlyreducesthesetofenvironmentsinwhichinterventionisoptimal,
as shown in Theorem 1; it also weakly reduces the level of redistribution conditional on intervention.
Thereasonisthattoppingupweakensthescreeningvalueoflowquantities. Withouttoppingup,ahigh
type who chooses a subsidized low quantity must give up his laissez-faire private-market consumption.
With topping up, the same high type can choose the subsidized allocation and then purchase additional
units in the private market. This additional deviation opportunity makes redistribution toward low types
more costly. The social planner responds by weakly reducing the scope for a free public option and
serving weakly fewer types.
Thesamelogicalsoexplainshowtoppingupchangestheoptimalallocation. AsProposition3shows,
topping up results in arotationof the optimal allocation function in a single-crossing sense: relative to
theoptimalallocationwithouttoppingup, consumptionisweaklylowerforlowtypesandweaklyhigher
for high types. Topping up therefore reduces the extent to which the social planner can tilt consumption
25

towardlowtypesandawayfromhigher-demandconsumerswithlowerredistributivepriority—andhence
the amount of surplus the social planner can redirect toward the bottom.
As in Section 4, the explicit characterization of the optimal allocations in Theorem 4 also yields
transparent comparative statics with respect to the welfare weight function𝜔. We again consider two
partialordersonwelfareweightfunctions: pointwiseincreasesandmean-preservingspreads. Incontrast
to the comparative statics of Section 4, however, the effects of these changes on optimal redistribution
now depend on whether topping up is allowed.
We begin with pointwise increases in welfare weights.
Proposition 4.Let𝜔𝐻 and𝜔𝐿 be welfare weight functions satisfying Assumption 2, such that𝜔𝐻≥𝜔𝐿
pointwise. Then:
(i) the multipliers𝜇∗ TU and𝜇∗ are weakly higher under𝜔𝐻;
(ii) the cutoffs𝜃𝐻 TU(𝜇∗ TU) and𝜃𝐻(𝜇∗) are weakly higher under𝜔𝐻; and
(iii) the optimal allocation function𝑞∗ TU is pointwise weakly higher under𝜔𝐻, while there exists
ˆ𝜃∈[ 𝜃,𝜃] such that the optimal allocation function𝑞∗ is pointwise weakly lower for𝜃 > ˆ𝜃 and
pointwise weakly higher for𝜃 < ˆ𝜃 under𝜔𝐻.
With topping up, Proposition 4 gives the same qualitative comparative statics as in Proposition 1. A
pointwise increase in welfare weights expands redistribution by increasing the scope for a free public
option,themassofconsumersserved,andtheallocationsofallservedconsumers. Theonlydifferenceis
the direction in which the served region expands: under positive correlation, service expands downward
from the top; under negative correlation, service expands upward from the bottom.
Without topping up, the same pointwise increase in welfare weights has a different effect. There is
still an increased scope for a free public option and mass of consumers served, but the allocations of
servedconsumersdonotnecessarilyincrease. Instead,allocationsrotate: lowtypesreceiveweaklymore,
while high types receive weakly less. This reflects the screening role of low quantities. When the social
planner places more weight on low types, she raises their consumption directly, but she may also reduce
the consumption of higher served types in order to preserve incentives and redirect surplus toward the
bottom. This force is absent with topping up, because high types can supplement privately.
26

Next, consider mean-preserving spreads. For decreasing welfare weight functions with the same
mean, we say that𝜔𝐻 is amean-preserving spreadof𝜔𝐿 if
∫ 𝜃
𝜃
𝜔𝐻(𝑠) d𝐹(𝑠)≥
∫ 𝜃
𝜃
𝜔𝐿(𝑠) d𝐹(𝑠), for all𝜃∈[ 𝜃,𝜃]. (10)
Thus,𝜔𝐻 shifts welfare weight toward lower types while holding the average welfare weight fixed.
Proposition 5.Suppose𝜔𝐻 and𝜔𝐿 are welfare weight functions satisfying Assumption 2 such that𝜔𝐻
is a mean-preserving spread of𝜔𝐿. Then:
(i) the multiplier𝜇∗ TU is unchanged while the multiplier𝜇∗ is weakly higher for𝜔𝐻;
(ii) the cutoff𝜃𝐻 TU(𝜇∗ TU) is weakly lower for𝜔𝐻; and
(iii) the allocation function𝑞∗ TU is pointwise weakly lower for𝜔𝐻.
With topping up, Proposition 5 shows that a mean-preserving spread of welfare weights reduces
redistribution. This is the opposite of Proposition 2 and may be surprising: a mean-preserving spread
increasesdispersioninwelfareweights,implyingthatconsumerdemandismorestatisticallyinformative
about redistributive priority—a property that should improve screening, at least in principle (Dworczak
r⃝ al., 2021). Under positive correlation, this improves self-targeting, leading to increased redistribution.
However,undernegativecorrelation,thisgeneratesgreaterleakageofsubsidiestohightypes,whomimic
the behavior of low types and supplement privately. As Proposition 5 shows, this force dominates the
increase in statistical informativeness and leads to an optimal reduction in redistribution.
Withouttoppingup,theeffectofamean-preservingspreadisdifferent. Aslowquantitiescannowhelp
screen, the increase in statistical informativeness leads to a nontrivial tradeoff with incentive constraints.
Thistradeoffalwaysfavorsweaklyexpandingthescopeofthefreepublicoption,butleadstoambiguous
comparative statics for the mass of consumers served and the allocations for served consumers.
Taken together, Propositions 3 to 5 show that topping up changes both the level of redistribution
and its comparative statics. Under negative correlation, topping up weakens screening, reduces the
level of optimal redistribution, and rotates the optimal allocation away from consumers with the highest
redistributive priority. It also changes how the social planner responds to redistributive priorities: with
27

toppingup,increasesinwelfareweightshavemonotoneallocationeffects,whilemean-preservingspreads
reduce redistribution; without topping up, the social planner can still use low quantities to screen, so
stronger redistributive priorities toward low types may expand the scope of a free public option while
reducing allocations for higher served types.
6 Concluding Remarks
In an inspiring review article on redistribution, Currie and Gahvari (2008) write that
“[p]rograms with or without the possibility of topping up have different welfare properties.
Currently, there are no general results regarding the relative merits of the two. [...] Nor are
thereanygeneralresultsonthecharacterizationofoptimalpublicprovisionpolicies,targeted
or universal.”
This paper provides such a comparison in a mechanism-design model of in-kind redistribution. Our
resultsshowthattoppingupgenerallyweakensthesocialplanner’sabilitytoscreenandchangesoptimal
redistribution in at least three ways—at the extensive margin, at the intensive margin, and through
comparative statics with respect to changes in redistributive priorities.
At the extensive margin, we show that the social planner’s optimal intervention decision under each
participation structure is characterized by a sufficient statistic of the welfare weight distribution. With
topping up, the social planner optimally intervenes if and only if the maximal upper-tail average welfare
weight exceeds the opportunity cost of public funds. Without topping up, the relevant sufficient statistic
is the maximal welfare weight. This leads the social planner to optimally intervene in strictly fewer
environments when topping up is allowed under negative correlation, but not positive correlation.
At the intensive margin, we show that the effect of topping up depends on the correlation between
redistributive priorities and demand. Under positive correlation, topping up does not change the optimal
mechanism. Under negative correlation, however, topping up weakens screening, reduces the level of
optimal redistribution, and rotates consumption away from those with the highest redistributive priority.
The comparative statics of optimal redistribution with respect to changes in redistributive priorities
reinforce this distinction. Under positive correlation, stronger redistributive priorities and greater
28

statistical informativeness of demand weakly expand optimal redistribution. Under negative correlation,
however, topping up undermines the social planner’s ability to screen with low quantities: stronger
redistributiveprioritiesforceabluntexpansionofconsumptionforallservedtypesratherthanatargeted
rotation, and greater statistical informativeness of demand weakly reduces the overall level of
redistribution. Thus, topping up changes not only the level of redistribution, but also how optimal
redistribution responds to changes in redistributive priorities.
Our results can therefore be interpreted as characterizing the gross screening costs of topping up.
Under positive correlation, these costs are zero, providing a strong rationale for allowing consumers to
topup. Undernegativecorrelation,bycontrast,toppingupgeneratesscreeningcostsatboththeextensive
and intensive margins. A complete policy evaluation must therefore weigh these screening costs against
the administrative and enforcement costs of preventing topping up.
From a methodological perspective, our analysis and results show that mechanism-design problems
with type-dependent outside options can, somewhat surprisingly, remain tractable. We solve two such
problems explicitly. With topping up, private-market access imposes a pointwise lower bound on
consumption;withouttoppingup,itgeneratesparticipationconstraintsthatcanbewrittenasmajorization
constraints. Although these constraints are mathematically distinct, we solve both problems by adapting
the approach of Amador and Bagwell (2013): we characterize the relevant Lagrange multipliers directly
from primitives and reduce the remaining optimization to generalized ironing (Myerson, 1981; Toikka,
2011). The resulting tractability delivers not only explicit characterizations of the optimal mechanisms,
but also global comparative statics with respect to pointwise changes and mean-preserving spreads in
redistributive priorities. Such comparative statics are often difficult to obtain in nonlinear mechanism-
design problems because changes in primitives generally alter both the optimal allocation and the set
of binding participation constraints. We expect these methods to be useful in other mechanism-design
environments with type-dependent outside options as well.
More broadly, the ability of consumers to access the private market is a prominent feature of many
real-worldredistributionprograms,and—aswehaveshowninthispaper—itsinclusioninanalysesaffects
the design of optimal mechanisms in substantial and realistic ways. By developing a mechanism-design
model of in-kind redistribution that incorporates these participation constraints, we have quantified
29

when a social planner can strictly improve on the laissez-faire outcome and characterized the optimal
redistributionprogramasacombinationofafreepublicoption,nonlinearsubsidies,andthelaissez-faire
allocation. Ourresultshighlightthatwhileprivate-marketaccesslimitsthescopeofin-kindredistribution,
it also strengthens the case for non-market allocations, such as free public options.
Finally, while we have focused on redistribution as our application, our analysis is also useful for
characterizingtheParetofrontierofoptimalmechanisms(Dworczak r⃝ al.,2021). Inparticular,although
private market access is the source of participation constraints in our application, the same constraints
can also be interpreted as a pointwise allocation lower bound or Pareto improvement requirement. Such
requirementsmayarisewhenasocialplannerwithfullcontrolovertheentiremarketdesignsamechanism
that benefits all consumers (in either allocation or utility space) relative to the laissez-faire outcome—an
idea that naturally fits within political economy models of reform with consensus or majority voting, as
noted by Fuchs and Skrzypacz (2015). Recently, Baron, Lombardo, Ryan, Suh and Valenzuela-Stookey
(2026) consider such a constraint in the reform of assignment schemes used to allocate Child Protective
Servicesinvestigators. DworczakandMuir(2024)examinearelatedprobleminthecontextofdesigning
propertyrights. Ourapproachinthispaperalsocontributestothesetoftoolsforanalyzingthesemodels.
30

References
Akbarpour, M. r⃝ P . Dworczak r⃝ S. D. Kominers (2024): “Redistributive Allocation Mechanisms,”
Journal of Political Economy, 132, 1831–1875.
Amador, M., and K. Bagwell (2013): “The Theory of Optimal Delegation With an Application to
Tariff Caps,”Econometrica, 81, 1541–1599.
Atkinson, A. B., and J. E. Stiglitz (1976): “The Design of Tax Structure: Direct Versus Indirect
Taxation,”Journal of Public Economics, 6, 55–75.
Barlow, R. E., D. J. Bartholomew, J. M. Bremner, and H. D. Brunk (1972): Statistical Inference
UnderOrderRestrictions: TheTheoryandApplicationofIsotonicRegression ,NewYork,NY:Wiley.
Baron, E. J., R. Lombardo, J. Ryan, J. Suh, and Q. V alenzuela-Stookey (2026): “Reforming
Rotations,”Working paper.
Besley , T., and S. Coate(1991): “PublicProvisionofPrivateGoodsandtheRedistributionofIncome,”
American Economic Review, 81, 979–984.
Blackorby , C., and D. Donaldson(1988): “CashVersusKind,Self-Selection,andEfficientTransfers,”
American Economic Review, 78, 691–700.
Blomquist, S., and V . Christiansen (1998): “Topping up or Opting Out? The Optimal Design of
Public Provision Schemes,”International Economic Review, 39, 399–411.
Che, Y .-K., I. Gale, and J. Kim (2013): “Assigning Resources to Budget-Constrained Agents,”Review
of Economic Studies, 80, 73–107.
Condorelli, D. (2013): “Market and Non-Market Mechanisms for the Optimal Allocation of Scarce
Resources,”Games and Economic Behavior, 82, 582–591.
Currie, J., and F. Gahvari (2008): “Transfers in Cash and In-Kind: Theory Meets the Data,”Journal
of Economic Literature, 46, 333–83.
31

Diamond, P . A.(1975): “A Many-Person Ramsey Tax Rule,”Journal of Public Economics, 4, 335–342.
Doligalski, P . r⃝ P . Dworczakr⃝ M. Akbarpour r⃝ S. D. Kominers (2025): “Optimal Redistribution
via Income Taxation and Market Design,”Working paper.
Dworczak, P . r⃝ S. D. Kominers r⃝ M. Akbarpour (2021): “Redistribution Through Markets,”
Econometrica, 89, 1665–1698.
Dworczak, P ., and E. V . Muir(2024): “A Mechanism-Design Approach to Property Rights,”Working
paper.
Fuchs, W ., and A. Skrzypacz(2015): “Government Interventions in a Dynamic Market with Adverse
Selection,”Journal of Economic Theory, 158, 371–406.
Gahvari, F., and E. Mattos (2007): “Conditional Cash Transfers, Public Provision of Private Goods,
and Income Redistribution,”American Economic Review, 97, 491–502.
Jullien, B. (2000): “Participation Constraints in Adverse Selection Models,”Journal of Economic
Theory, 93, 1–47.
Kang, Z. Y .(2023): “The Public Option and Optimal Redistribution,”Working paper.
Kleiner, A., B. Moldovanu, and P . Strack (2021): “Extreme Points and Majorization: Economic
Applications,”Econometrica, 89, 1557–1593.
Kolotilin, A., and A. Wolitzky (2026): “Competitive Many-to-One Matching: Sorting vs. Equality,”
Working paper.
Liscow, Z., and A. Pershing (2022): “Why Is So Much Redistribution In-Kind and Not in Cash?
Evidence From a Survey Experiment,”National Tax Journal, 75, 313–354.
Loertscher, S., and E. V . Muir(2022): “Monopoly Pricing, Optimal Rationing, and Resale,”Journal
of Political Economy, 130, 566–635.
Luenberger, D. G.(1969): OptimizationbyVectorSpaceMethods ,NewYork,NY:JohnWiley&Sons.
32

Mackenzie, G. A.(1991): “PriceSubsidies,”in PublicExpenditureHandbook: AGuidetoPublicPolicy
Issues in Developing Countriesed. by Chu, K.-Y., and Hemming, R. Washington, D.C.: International
Monetary Fund, Chap. IX, 60–67.
Milgrom, P ., and I. Segal(2002): “Envelope Theorems for Arbitrary Choice Sets,”Econometrica, 70,
583–601.
Mirrlees, J. A. (1971): “An Exploration in the Theory of Optimum Income Taxation,”Review of
Economic Studies, 38, 175–208.
Myerson, R. B. (1979): “Incentive Compatibility and the Bargaining Problem,”Econometrica, 47,
61–73.
(1981): “Optimal Auction Design,”Mathematics of Operations Research, 6, 58–73.
Nichols, A. L., and R. J. Zeckhauser(1982): “TargetingTransfersthroughRestrictionsonRecipients,”
American Economic Review, 72, 372–377.
Pai, M., and P . Strack(2024): “Taxing Externalities Without Hurting the Poor,”Working paper.
Philippon, T., and V . Skreta (2012): “Optimal Interventions in Markets with Adverse Selection,”
American Economic Review, 102, 1–28.
Ramsey , F. P .(1927): “A Contribution to the Theory of Taxation,”Economic Journal, 37, 47–61.
Saez, E. (2002): “The Desirability of Commodity Taxation Under Non-Linear Income Taxation and
Heterogeneous Tastes,”Journal of Public Economics, 83, 217–230.
Tirole, J. (2012): “Overcoming Adverse Selection: How Public Intervention Can Restore Market
Functioning,”American Economic Review, 102, 29–59.
Toikka, J. (2011): “Ironing Without Control,”Journal of Economic Theory, 146, 2510–2526.
Topkis, D. M. (1998): Supermodularity and Complementarity, Princeton, NJ: Princeton University
Press.
33

Weitzman, M. L. (1977): “Is the Price System or Rationing More Effective in Getting a Commodity to
Those Who Need It Most?”Bell Journal of Economics, 8, 517–524.
34

A Proofs of Main Results
A.1 Preliminary Analysis
We begin by characterizing the (IC) and (LS) constraints in order to rewrite the social planner’s problem
in a more tractable form. As these characterizations are well-known, we state them without proof.
Claim 1.A mechanism(𝑞,𝑡) satisfies (IC)if and only if𝑞 is nondecreasing and
𝜃𝑣(𝑞(𝜃))− 𝑡(𝜃)=𝜃𝑣(𝑞(𝜃))− 𝑡(𝜃)
|              {z              }
=:𝑈
+
∫ 𝜃
𝜃
𝑣(𝑞(𝑠)) d𝑠.
Claim 1 follows from standard arguments in the literature on mechanism design. Myerson’s (1981)
lemma implies that, given an allocation function𝑞, there exists a payment function𝑡 such that(𝑞,𝑡) is
incentive-compatibleifandonlyif 𝑞isnondecreasing. Theenvelopetheorem(MilgromandSegal,2002)
uniquelypinsdownthepaymentfunctionuptoanadditiveconstant, 𝑈,equaltotheutilitythatthelowest
consumer type receives under the mechanism.
Claim 2.An incentive-compatible mechanism(𝑞,𝑡) satisfies (LS) if and only if𝑈≤𝜃𝑣(𝑞(𝜃)).
Claim 2 shows that the no-lump-sum-transfers constraint is equivalent to imposing an upper bound
on𝑈 intermsofthequantity 𝑞(𝜃) allocatedtothelowesttype. When(LS)binds, 𝑡(𝜃)= 0,inwhichcase
the social planner allocates the good for free to the lowest type.
Wenowreformulatethesocialplanner’sprobleminutilityspaceratherthanallocationspace. Tothis
end,wemakethechangeofvariables 𝜈≔𝑣◦𝑞;wereferto 𝜈henceforthasthesubutilityfunctioninduced
by the mechanism. Since𝑣 is increasing by assumption, Claim 1 implies that any incentive-compatible
mechanism induces a nondecreasing subutility function.
Next, we apply Claim 1 to rewrite the (IR) constraints and the social planner’s objective. Let𝑈LF
be the utility that the lowest consumer type receives under the laissez-faire mechanism, and let𝜈LF be
the subutility function induced by the laissez-faire mechanism. Then the envelope theorem (cf. Claim 1)
35

implies that the (IR) constraints can be written as
𝑈+
∫ 𝜃
𝜃
𝜈(𝑠) d𝑠≥𝑈LF+
∫ 𝜃
𝜃
𝜈LF(𝑠) d𝑠, for all𝜃∈[ 𝜃,𝜃].
For notational convenience, extend the domain of𝑣−1 toR and its range toR≔R∪{+∞} by defining
Ψ( ˆ𝜈)≔
 

𝑣−1( ˆ𝜈), if ˆ𝜈∈[ 𝑣(0),𝑣(𝐴)],
+∞, otherwise.
The envelope theorem also allows us to eliminate dependence on the payment function in the objective:
(OBJ)=[E[𝜔]− 𝛼]𝑈+𝛼
∫ 𝜃
𝜃
[𝐽0(𝜃)𝜈(𝜃)− 𝑐Ψ(𝜈(𝜃))] d𝐹(𝜃).
Here, we have used the generalized virtual valuation𝐽𝜇 defined in equation (1) to simplify notation.
Wesummarizetheaboveanalysisbyrewritingthesocialplanner’sproblem. Denotingthesetofright-
continuous, nondecreasing functions byI ≔
n
ℎ :[𝜃,𝜃]→ R is right-continuous and nondecreasing
o
,
Claims 1 and 2 allow us to rewrite the social planner’s problem as follows:
max
𝑈∈R,𝜈∈I
(
[E[𝜔]− 𝛼]𝑈+𝛼
∫ 𝜃
𝜃
[𝐽0(𝜃)𝜈(𝜃)− 𝑐Ψ(𝜈(𝜃))] d𝐹(𝜃)
)
,
s.t.
 

𝑈≤𝜃𝜈(𝜃),
𝑈+
∫ 𝜃
𝜃
𝜈(𝑠) d𝑠≥𝑈LF+
∫ 𝜃
𝜃
𝜈LF(𝑠) d𝑠, for all𝜃∈[ 𝜃,𝜃].
If topping up is allowed, we impose the additional constraint:
𝜈(𝜃)≥ 𝜈LF(𝜃), for all𝜃∈[ 𝜃,𝜃].
Weconcludeourpreliminaryanalysisbymakingfourobservationsaboutthesocialplanner’sproblems
with and without topping up that are clearer from this rewriting.
1. Existence of solution.To see that an optimal solution to each problem exists, we endowI with
36

the metric
𝑑(𝜈1,𝜈 2)=∥𝜈1−𝜈2∥𝐿1+|𝜈1(𝜃)− 𝜈2(𝜃)|.
Observe that the social planner’s objective is continuous in(𝑈,𝜈). Without loss of generality, we
focus on the set𝐾 ≔[𝑈LF,𝜃𝑣(𝐴)]× n ℎ∈ I :[𝜃,𝜃]→[ 𝑣(0),𝑣(𝐴)] o . By the Helly selection
theorem and the dominated convergence theorem,𝐾 is compact; hence the constraint set in each
problem(asaclosedsubsetof 𝐾)isalsocompact. Finally, (𝑈LF,𝜈 LF)∈ 𝐾 satisfiestheconstraints;
hence the constraint set is nonempty.
2. Generaluniquenessofsolution. Wenowarguethattheoptimalsolutiontoeachproblemisunique
when E[𝜔] ≠ 𝛼. Suppose that(𝑈1,𝜈 1) and(𝑈2,𝜈 2) are distinct optimal solutions with distinct
allocation functions𝜈1 ≠ 𝜈2, and consider(𝑈∗,𝜈∗) = (𝑈1+𝑈2)/2,(𝜈1+𝜈2)/2. Clearly,𝜈∗ is
nondecreasing,and(𝑈∗,𝜈∗)satisfiestheconstraints(sincetheconstraintsarelinear). However, 𝑣−1
isstrictlyconvexsince 𝑣 isincreasingandstrictlyconcave;because 𝜈1 and𝜈2 areright-continuous,
𝜈1 ≠ 𝜈2 implies they differ on a set of positive measure, hence Jensen’s inequality implies that
the social planner’s objective is strictly larger under(𝑈∗,𝜈∗), a contradiction. Thus, the optimal
allocation function for each problem must be unique. When the (LS) constraint binds and/or
when the (IR) constraint binds for any type,𝑈∗ is uniquely pinned down by the envelope theorem
(cf. Claim 1). Consequently, the optimal solution can fail to be unique only if both the (LS) and
(IR) constraints are slack, in which caseE[𝜔]=𝛼.
3. Optimality of deterministic mechanisms.Next, we observe that the restriction to deterministic
mechanisms entails no loss of generality. For any stochastic mechanism, let𝜈†(𝜃) be the expected
subutility allocated to type𝜃, and let𝑈† be the expected utility of the lowest type. The constraints
are preserved by linearity, and the deterministic mechanism(𝑈†,𝜈†) delivers the same subutility.
Moreover, sinceΨ is convex, Jensen’s inequality impliesΨ(𝜈†(𝜃))≤ E𝜈[Ψ(𝜈(𝜃))], so the social
planner’s objective is weakly larger.
4. Convex program with majorization constraints.Finally, we point out that the problem without
toppingupcanbewrittenasaconvexprogramwithmajorizationconstraints. Toillustrate,suppose
37

that the (IR) constraint binds for the highest type. Then the (IR) constraints can be rewritten as
∫ 𝜃
𝜃
𝜈(𝑠) d𝑠≤
∫ 𝜃
𝜃
𝜈LF(𝑠) d𝑠, for all𝜃∈[ 𝜃,𝜃].
Since 𝜈 and 𝜈LF are nondecreasing, this condition is equivalent to𝜈 being weakly majorized by
𝜈LF. This argument can be adapted for any typeˆ𝜃 whose (IR) constraint binds by partitioning the
type space into two intervals,[𝜃, ˆ𝜃] and[ ˆ𝜃,𝜃]: the problem on each interval is a convex program
with majorization constraints.
Recent papers (e.g., Kleiner et al., 2021; Akbarpourr⃝ al., 2024) solve linear programs with
majorizationconstraintsandshowthattheirsolutionscoincidewithextremepointsoftheconstraint
set. However, extreme-point methods do not apply in our setting as our program has a strictly
concave objective (due to diminishing marginal utility) over a convex feasible set; hence, the
solution need not be an extreme point of the feasible set (i.e., it can be a convex combination of
extreme points). To overcome this technical challenge, we develop an alternate approach below.
A.2 Proof of Theorem 1
𝑈LF Δ𝜎
O(|Δ𝜎|1/2)
0 𝜃
utility,𝑈
𝜃 ˆ𝜃𝐿 ˆ𝜃 𝜃
Figure 4: Proof sketch of Theorem 1 with topping up.
38

Toppingup. Webeginbyprovingtheresultwhentoppingupisallowed. Considertheutilitythateach
consumerreceives,asshowninFigure4. Bytheenvelopetheorem(cf.Claim1),thegradientoftheutility
curve must be nondecreasing in𝜃 for any incentive-compatible mechanism; hence, incentive-compatible
mechanisms must result in convex utility curves. In addition, individually rational mechanisms must
result in utility curves that lie weakly above𝑈LF, shown as a gray dashed curve in Figure 4.
Consider a small subsidyΔ𝜎 > 0 that is targeted at consumers of typeˆ𝜃. Because topping up is
allowed, all consumers of higher type will mimic the behavior of typeˆ𝜃 by consuming the subsidyand
topping up their consumption in the private market. This is shown by the blue utility curve in Figure 4,
which is a parallel upward shift of𝑈LF for consumer types in the interval[ ˆ𝜃,𝜃]. Consumers with types
just below ˆ𝜃 will also mimic the behavior of typeˆ𝜃; however, these types overconsume, and their utility
is obtained by extending the blue utility curve linearly downwards until it intersects𝑈LF at type ˆ𝜃𝐿.
Thewelfareeffectofthissubsidyisthesumoftwocomponents,representedbythegreenandorange
areas in Figure 4. In the green area, since the subsidy does not distort consumption, the net impact
on weighted total surplus is exactly equal toΔ𝜎, multiplied by the mass of consumers aboveˆ𝜃 and the
difference between the welfare weights of consumers and the opportunity cost of public funds:
Δ𝜎·

1−𝐹( ˆ𝜃)   E  𝜔(𝜃)| 𝜃≥ ˆ𝜃  −𝛼  .
In the orange area, the subsidy distorts each type’s surplus by no more thanO(Δ𝜎); however, the
measureofaffectedtypesisboundedfromaboveby O(|Δ𝜎|1/2). Thisisbecause ˆ𝜃𝐿 canbegeometrically
determined from Figure 4 and the envelope theorem:
ˆ𝜃𝐿𝑣(𝑞LF( ˆ𝜃𝐿))− 𝑡LF( ˆ𝜃𝐿)= ˆ𝜃𝑣(𝑞LF( ˆ𝜃))− 𝑡LF( ˆ𝜃)+ Δ𝜎−  ˆ𝜃− ˆ𝜃𝐿 𝑣(𝑞LF( ˆ𝜃))
= ˆ𝜃𝑣(𝑞LF( ˆ𝜃))− 𝑡LF( ˆ𝜃)−
∫ ˆ𝜃
ˆ𝜃𝐿
𝑣(𝑞LF(𝜃)) d𝜃.
Equivalently, denoting𝜈LF≔𝑣◦𝑞LF, Taylor’s theorem implies that
Δ𝜎=
∫ ˆ𝜃
ˆ𝜃𝐿

𝜈LF( ˆ𝜃)− 𝜈LF(𝜃)  d𝜃= ∫ ˆ𝜃
ˆ𝜃𝐿
h ˆ𝜃−𝜃(𝜈LF)′( ˆ𝜃)+ O  | ˆ𝜃−𝜃|2 i d𝜃.
39

Since𝑣 is strictly concave, observe that
(𝜈LF)′( ˆ𝜃)=𝑣′(𝑞LF( ˆ𝜃))·( 𝑞LF)′( ˆ𝜃)= 𝑐 ˆ𝜃 · −𝑐 ˆ𝜃2𝑣′′(𝑞LF( ˆ𝜃)) =− 𝑐2 ˆ𝜃3𝑣′′(𝑞LF( ˆ𝜃)) > 0.
Thus,
Δ𝜎= 1 2  ˆ𝜃− ˆ𝜃𝐿  2 (𝜈LF)′( ˆ𝜃)+ O  | ˆ𝜃− ˆ𝜃𝐿|3  =⇒ ˆ𝜃𝐿 = ˆ𝜃− O  |Δ𝜎|1/2  .
Since𝐹 is absolutely continuous, the mass of types in the interval[ ˆ𝜃𝐿, ˆ𝜃] is similarly bounded. Hence,
the net impact on weighted total surplus from the distorted types is bounded from above byO(|Δ𝜎|3/2).
Inthelimitas Δ𝜎→ 0,thissmallsubsidyhasapositivemarginalimpactifandonlyifthefirst-order
term is positive:
E

𝜔(𝜃)| 𝜃≥ ˆ𝜃  >𝛼.
Consequently, the optimal mechanism strictly improves on the laissez-faire outcome if there existsˆ𝜃
satisfying this condition, that is,
max
ˆ𝜃∈[𝜃,𝜃]
E

𝜔(𝜃)| 𝜃≥ ˆ𝜃  >𝛼.
We now prove the opposite direction. Suppose that
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)≤ 0, for all𝜃∈[ 𝜃,𝜃].
For any feasible mechanism(𝑈,𝜈), letΔ𝑈 ≔𝑈−𝑈LF andΔ𝜈 ≔ 𝜈−𝜈LF. The (TU) constraint gives
Δ𝜈≥ 0, and the (IR) constraint of the lowest type givesΔ𝑈≥ 0. The change in weighted total surplus
relative to laissez-faire is
[E[𝜔]− 𝛼]Δ𝑈+
∫ 𝜃
𝜃
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)· Δ𝜈(𝜃) d𝜃
+𝛼
∫ 𝜃
𝜃

𝜃Δ𝜈(𝜃)− 𝑐

Ψ(𝜈(𝜃))− Ψ(𝜈LF(𝜃))  d𝐹(𝜃).
The first two terms are weakly negative by assumption, while the last term is weakly negative because
𝜈LF(𝜃) maximizes𝑧↦→𝜃𝑧−𝑐Ψ(𝑧) pointwise. Hence, laissez-faire is optimal.
40

𝑈LF Δ𝜎
O(|Δ𝜎|1/2) O(|Δ𝜎|1/2)
0 𝜃
utility,𝑈
𝜃 ˆ𝜃𝐿 ˆ𝜃 ˆ𝜃+Δ𝜃 ˆ𝜃𝐻 𝜃
Figure 5: Proof sketch of Theorem 1 without topping up.
No topping up. We now consider the case of no topping up. As before, we consider a small subsidy
Δ𝜎 >0thatistargetedatconsumersoftypes 𝜃∈[ ˆ𝜃, ˆ𝜃+Δ𝜃],asshowninFigure5. Themaindifference
isthat,becausetoppingupisnotallowed,theconsumptionoftypesabove ˆ𝜃+Δ𝜃 isinfactdistorted: these
types underconsume, and their utility is obtained by extending the blue utility curve linearly upwards
until it intersects𝑈LF at type ˆ𝜃𝐻. A similar argument as before yields
ˆ𝜃𝐻 = ˆ𝜃+Δ𝜃+ O

|Δ𝜎|1/2

.
Thus, the net impact on weighted total surplus due to distortions in consumption—given by the orange
area in Figure 5—is bounded from above byO(|Δ𝜎|3/2). Since𝜔( ˆ𝜃) > 𝛼, by continuity there exists an
interval[ ˆ𝜃, ˆ𝜃+Δ𝜃] such that ∫ ˆ𝜃+Δ𝜃
ˆ𝜃
[𝜔(𝜃)− 𝛼] d𝐹(𝜃) > 0.
Fixsuchanintervalandtake Δ𝜎→ 0. Thefirst-ordergainisoforder Δ𝜎, whilethedistortiontermsare
bounded from above byO(Δ𝜎3/2). Hence, the perturbation is profitable for sufficiently smallΔ𝜎.
Conversely, suppose that𝜔(𝜃) ≤𝛼 for all𝜃∈ [𝜃,𝜃]. Let 𝑢(𝜃) = 𝜃𝑣(𝑞(𝜃))− 𝑡(𝜃) be the utility
41

delivered by any feasible mechanism. The contribution of type𝜃 to the objective can be written as
𝛼[𝜃𝑣(𝑞(𝜃))− 𝑐𝑞(𝜃)]+[𝜔(𝜃)− 𝛼]𝑢(𝜃).
Subtracting the laissez-faire contribution gives
𝛼

𝜃𝑣(𝑞(𝜃))− 𝑐𝑞(𝜃)− 𝑈LF(𝜃)  +[𝜔(𝜃)− 𝛼]  𝑢(𝜃)− 𝑈LF(𝜃)  .
The first term is weakly negative by the definition of𝑈LF. The second term is weakly negative because
𝜔(𝜃)− 𝛼≤ 0and𝑢(𝜃)≥ 𝑈LF(𝜃) by the (IR) constraint. Hence, laissez-faire is optimal.
A.3 Proof of Theorem 2
Sufficiency. Let𝜇∗=(E[𝜔]− 𝛼)+, and suppose that
 

𝐽𝜇∗|[𝜃𝐿,𝜃](𝜃)≥ 𝜃, for𝜃𝐿≤𝜃≤𝜃,
𝜔(𝜃)≤ 𝛼, for𝜃≤𝜃 <𝜃𝐿.
We show that the optimal allocation function for both programs is given by
𝑞∗(𝜃)=𝑞∗ TU(𝜃)=
 

𝐷

𝑐,𝐽𝜇∗|[𝜃𝐿,𝜃](𝜃)

, for𝜃𝐿≤𝜃≤𝜃,
𝑞LF(𝜃), for𝜃≤𝜃 <𝜃𝐿.
To this end, we consider two cases:
• Case #1: 𝜃𝐿 =𝜃.
Consider the social planner’s relaxed problem without the (IR) and (TU) constraints:
max
𝑈∈R,𝜈∈I
(
[E[𝜔]− 𝛼]𝑈+𝛼
∫ 𝜃
𝜃
[𝐽0(𝜃)𝜈(𝜃)− 𝑐Ψ(𝜈(𝜃))] d𝐹(𝜃) :𝑈≤𝜃𝜈(𝜃)
)
.
42

The solution to the relaxed problem is given by
𝑈∗=
 

𝜃𝜈∗(𝜃), if𝜇∗ > 0,
𝑈LF, if𝜇∗= 0, and 𝜈∗(𝜃)=𝑣(𝑞∗(𝜃)) =𝑣  𝐷  𝑐,𝐽𝜇∗(𝜃)  .
By assumption,𝐽𝜇∗(𝜃)≥ 𝜃 for all𝜃∈[ 𝜃,𝜃]; hence,𝑞∗≥𝑞LF, meaning that the (TU) constraint is
satisfied. Moreover,𝑈∗≥𝑈LF; together with𝑞∗≥𝑞LF, this implies that the (IR) constraint is also
satisfied. Thus,(𝑈∗,𝜈∗) solves both programs, as claimed.
• Case #2: 𝜃𝐿 >𝜃 .
Bydefinitionof 𝜃𝐿,weinferthat E[𝜔] <𝛼 ; hence,𝜇∗=(E[𝜔]− 𝛼)+= 0. Definethemechanism
(𝑈∗,𝜈∗)=(𝑈LF,𝑣◦𝑞∗),andconsiderafeasiblemechanism (𝑈,𝜈)fortheproblemwithouttopping
up. By the (IR) constraint,
Δ(𝜃)≔𝑈−𝑈LF+
∫ 𝜃
𝜃

𝜈(𝑠)− 𝜈LF(𝑠)  d𝑠≥ 0, for all𝜃∈[ 𝜃,𝜃].
Since𝜈−𝜈LF is bounded and measurable,Δ is absolutely continuous andΔ′(𝜃) = 𝜈(𝜃)− 𝜈LF(𝜃)
almost everywhere. Moreover, the definition of𝜃𝐿 implies that
𝛼[𝐽0(𝜃)− 𝜃] 𝑓(𝜃)=
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)=
∫ 𝜃𝐿
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠), for all𝜃∈[ 𝜃,𝜃].
By assumption,𝜔(𝜃)≤ 𝛼 for𝜃≤𝜃 <𝜃𝐿, implying that
0≥
∫ 𝜃𝐿
𝜃
[𝜔(𝜃)− 𝛼]Δ(𝜃) d𝐹(𝜃)
=−Δ(𝜃)
∫ 𝜃𝐿
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)

 𝜃𝐿
𝜃
+𝛼
∫ 𝜃𝐿
𝜃
[𝐽0(𝜃)− 𝜃]Δ′(𝜃) d𝐹(𝜃)
=[E[𝜔]− 𝛼]

𝑈−𝑈LF

+𝛼
∫ 𝜃𝐿
𝜃
[𝐽0(𝜃)− 𝜃]

𝜈(𝜃)− 𝜈LF(𝜃)  d𝐹(𝜃). (11)
43

Since𝜈LF(𝜃) maximizes the function𝑧↦→𝜃𝑧−𝑐Ψ(𝑧) for each𝜃∈[ 𝜃,𝜃], we also obtain
𝛼
∫ 𝜃𝐿
𝜃

𝜃

𝜈(𝜃)− 𝜈LF(𝜃)  −𝑐  Ψ(𝜈(𝜃))− Ψ(𝜈LF(𝜃))  d𝐹(𝜃)≤ 0. (12)
Finally, letM denote the set of measurable functions that map from[𝜃,𝜃] into[𝑣(0),𝑣(𝐴)]. A
standard ironing argument (Myerson, 1981; Toikka, 2011) yields
𝛼
∫ 𝜃
𝜃𝐿
[𝐽0(𝜃)𝜈(𝜃)− 𝑐Ψ(𝜈(𝜃))] d𝐹(𝜃)≤ 𝛼 max ˆ𝜈∈I
∫ 𝜃
𝜃𝐿
[𝐽0(𝜃) ˆ𝜈(𝜃)− 𝑐Ψ( ˆ𝜈(𝜃))] d𝐹(𝜃)
=𝛼 max
ˆ𝜈∈M
∫ 𝜃
𝜃𝐿
h
𝐽0|[𝜃𝐿,𝜃](𝜃) ˆ𝜈(𝜃)− 𝑐Ψ( ˆ𝜈(𝜃))
i
d𝐹(𝜃)
=𝛼
∫ 𝜃
𝜃𝐿
[𝐽0(𝜃)𝜈∗(𝜃)− 𝑐Ψ(𝜈∗(𝜃))] d𝐹(𝜃). (13)
Adding up inequalities (11), (12), and (13) yields
[E[𝜔]− 𝛼] 𝑈−𝑈∗+𝛼 ∫ 𝜃
𝜃
[𝐽0(𝜃)[𝜈(𝜃)− 𝜈∗(𝜃)]−𝑐[Ψ(𝜈(𝜃))− Ψ(𝜈∗(𝜃))]] d𝐹(𝜃)≤ 0.
Since(𝑈∗,𝜈∗)satisfiesthe(IR)constraintandtheaboveinequalityholdsforanyfeasiblemechanism
(𝑈,𝜈) for the problem without topping up,(𝑈∗,𝜈∗) solves the problem without topping up. Also,
since(𝑈∗,𝜈∗) satisfiesthe(TU)constraint,itfollowsthat (𝑈∗,𝜈∗) solvestheproblemwithtopping
up as well. Thus,(𝑈∗,𝜈∗) solves both programs, as claimed.
Necessity. Supposethat 𝑞∗=𝑞∗ TU. Definethecutofftype 𝜅 where𝑞∗ potentiallyfirstdeviatesfrom 𝑞LF:
𝜅≔
 

𝜃, if𝑞∗=𝑞LF,
inf
n
ˆ𝜃∈[ 𝜃,𝜃] :𝑞∗( ˆ𝜃) >𝑞 LF( ˆ𝜃) o , otherwise.
Lemma 1.𝜔(𝜃)≤ 𝛼 for all𝜃≤𝜃 < 𝜅.
Proof. By definition of𝜅,𝑞∗(𝜃) = 𝑞LF(𝜃) for all𝜃≤ 𝜃 < 𝜅. Suppose on the contrary that there exists
𝜃0 < 𝜅such that𝜔(𝜃0) > 𝛼; by continuity of𝜔, there must be a neighborhood containing𝜃0 on which
44

𝜔 > 𝛼. Our construction in the proof of Theorem 1 implies that there must be a strict improvement to
𝑞∗=𝑞LF on this neighborhood in the problem without topping up, a contradiction. □
Lemma 2.𝜃𝐿≤ 𝜅.
Proof. If E[𝜔]≥ 𝛼, then the claim holds trivially:
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)= E[𝜔]− 𝛼≥ 0 =⇒ 𝜃𝐿 =𝜃≤ 𝜅.
It remains only to consider the caseE[𝜔] <𝛼 , which implies that𝜇∗=(E[𝜔]− 𝛼)+= 0and𝑈∗=𝑈LF.
Moreover, the claim holds trivially if𝜅=𝜃; thus, we also suppose that𝜅 <𝜃.
Consider the problem without topping up. By the Lagrange multiplier theorem (Luenberger, 1969,
Theorem 1, p. 217) there exists a nonincreasing functionΛ :[𝜃,𝜃]→ R such thatΛ(𝜃)= 0 and
𝑞∗(𝜃)=𝐷

𝑐,

𝐽0+ Λ 𝛼𝑓  (𝜃) ! ,
where Λ is the cumulative multiplier associated with the (IR) constraint and satisfies complementary
slackness. Define the slack in the (IR) constraint by
Δ(𝜃)≔𝑈∗−𝑈LF+
∫ 𝜃
𝜃
h
𝑣(𝑞∗(𝑠))− 𝑣  𝑞LF(𝑠) i d𝑠= ∫ 𝜃
𝜅
h
𝑣(𝑞∗(𝑠))− 𝑣  𝑞LF(𝑠) i d𝑠,
where the second equality uses𝑈∗=𝑈LF. Since𝑞∗=𝑞∗ TU≥𝑞LF pointwise,Δ(𝜃)≥ 0 for all𝜃∈[ 𝜃,𝜃].
Moreover,Δ(𝜃)= 0for all𝜃≤ 𝜅 because𝑞∗(𝜃)=𝑞LF(𝜃) for all𝜃 < 𝜅, by definition of𝜅.
We now show thatΔ(𝜃) > 0 for all𝜃 > 𝜅. To this end, fix𝜃 > 𝜅. By definition of𝜅, there exists
some ˆ𝜃∈[ 𝜅,𝜃) such that𝑞∗( ˆ𝜃) > 𝑞LF( ˆ𝜃). Since𝑞∗ is nondecreasing and𝑞LF is continuous and strictly
increasing, theinequality𝑞∗(𝑠) >𝑞 LF(𝑠) holdsonanondegenerateopensubintervalof [𝜅,𝜃). Itfollows
that
Δ(𝜃)=
∫ 𝜃
𝜅
h
𝑣(𝑞∗(𝑠))− 𝑣  𝑞LF(𝑠) i d𝑠 >0.
Thisimpliesthatthe(IR)constraintisslackforevery 𝜃 > 𝜅. Bycomplementaryslackness,itfollowsthat
Λ(𝜃)= 0 for all𝜃 > 𝜅.
45

In addition, ironing cannot cross𝜅. Suppose an ironing interval𝐼 intersects both[𝜃,𝜅) and(𝜅,𝜃].
On𝐼∩[𝜃,𝜅), the allocation is𝑞LF, which is strictly increasing. But the ironed function—and hence the
induced allocation—is constant on𝐼, a contradiction.
Hence, the restriction of𝐽0+Λ/(𝛼𝑓) to[𝜅,𝜃] coincides with the ironing of𝐽0 on that interval:
𝑞∗(𝜃)=𝐷  𝑐,𝐽0|[𝜅,𝜃](𝜃)  , for all𝜃∈[ 𝜅,𝜃].
In particular, this holds at𝜅. Thus, we have
𝐷

𝑐,𝐽0|[𝜅,𝜃](𝜅)

=𝑞∗(𝜅)≥ 𝑞LF(𝜅)=𝐷(𝑐,𝜅) ⇐⇒𝐽0|[𝜅,𝜃](𝜅)≥ 𝜅
⇐⇒ inf
ˆ𝜃∈(𝜅,𝜃]
∫ ˆ𝜃
𝜅 𝐽0(𝑠) d𝐹(𝑠)
𝐹( ˆ𝜃)− 𝐹(𝜅) ≥ 𝜅.
Since𝐽0 is continuous, the latter inequality implies that𝐽0(𝜅)≥ 𝜅. Rearranging yields
∫ 𝜃
𝜅
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)≥ 0 ⇐⇒ 𝜅∈
(
ˆ𝜃∈[ 𝜃,𝜃] :
∫ 𝜃
ˆ𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)≥ 0
)
.
Since𝜃𝐿 is defined as the minimum of the set, we conclude that𝜃𝐿≤ 𝜅. □
Together, Lemmas 1 and 2 imply that𝜔(𝜃)≤ 𝛼 for all𝜃≤ 𝜃 < 𝜃𝐿, as claimed. It remains to prove
the first condition in Theorem 2. Define
𝐺(𝜃)≔
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠).
ByLemma1andthecontinuityof 𝜔,𝜔(𝜃)≤ 𝛼forall 𝜃∈[ 𝜃,𝜅]. Since𝜃𝐿≤ 𝜅 byLemma2,thisimplies
that𝐺 is nondecreasing on[𝜃𝐿,𝜅]. By construction,𝐺(𝜃𝐿)≥ 0; hence,𝐺(𝜃)≥ 0 for all𝜃∈[ 𝜃𝐿,𝜅]. It
follows that
𝐽𝜇∗(𝜃)− 𝜃≥ 𝐺(𝜃) 𝛼𝑓(𝜃)≥ 0 =⇒ 𝐽𝜇∗(𝜃)≥ 𝜃, for all𝜃∈[ 𝜃𝐿,𝜅]. (14)
Lemma 3.𝑞∗(𝜃)=𝐷  𝑐,𝐽𝜇∗|[𝜅,𝜃](𝜃)  for all𝜅≤𝜃≤𝜃.
Proof. AsshownintheproofofLemma2,theclaimholdsinthecaseof E[𝜔] <𝛼 and𝜅 <𝜃. Moreover,
46

the claim holds trivially if𝜅 = 𝜃 (in which case𝑞∗ = 𝑞LF). Thus, it remains only to consider the case
E[𝜔]≥ 𝛼, where𝜃𝐿 =𝜃 and𝑈∗≥𝑈LF.
As in the proof of Lemma 2, consider the problem without topping up. By the Lagrange multiplier
theorem (cf. Luenberger, 1969, Theorem 1, p. 217) there exists a nonincreasing functionΛ :[𝜃,𝜃]→ R
such thatΛ(𝜃)= 0and
𝑞∗(𝜃)=𝐷

𝑐,

𝐽𝜇∗+ Λ 𝛼𝑓  (𝜃) ! ,
where Λ is the cumulative multiplier associated with the (IR) constraint and satisfies complementary
slackness. Define the slack in the (IR) constraint by
Δ(𝜃)≔𝑈∗−𝑈LF+
∫ 𝜃
𝜃
h
𝑣(𝑞∗(𝑠))− 𝑣  𝑞LF(𝑠) i d𝑠≥ ∫ 𝜃
𝜃
h
𝑣(𝑞∗(𝑠))− 𝑣  𝑞LF(𝑠) i d𝑠,
where the inequality uses𝑈∗≥ 𝑈LF. Since 𝑞∗ = 𝑞∗ TU≥ 𝑞LF pointwise, we haveΔ(𝜃)≥ 0 for all𝜃.
Moreover,Δ(𝜃) > 0 for all𝜃 > 𝜅. This implies that the (IR) constraint is slack for every𝜃 > 𝜅. By
complementary slackness, it follows thatΛ(𝜃)= 0 for all𝜃 > 𝜅. Hence, the restriction of𝐽𝜇∗+Λ/(𝛼𝑓)
to[𝜅,𝜃] coincides with𝐽𝜇∗ on that interval:
𝑞∗(𝜃)=𝐷  𝑐,𝐽𝜇∗|[𝜅,𝜃](𝜃)  , for all𝜃∈[ 𝜅,𝜃].
This proves the desired result. □
Lemma 3 implies that𝐽𝜇∗|[𝜅,𝜃](𝜃)≥ 𝜃 for all𝜃∈[ 𝜅,𝜃]. We now show that𝐽𝜇∗|[𝜃𝐿,𝜃](𝜃)≥ 𝜃 for all
𝜃∈[ 𝜃𝐿,𝜃]. Since this result holds trivially if𝜃𝐿 =𝜃, suppose𝜃𝐿 <𝜃. Observe that:
(i) If𝜅=𝜃𝐿, then our desired result holds trivially.
(ii) If𝜅=𝜃,thenourdesiredresultisimpliedbyequation(14)andmonotonicityoftheironingoperator
(Lemma 7).
(iii) If𝜃𝐿 < 𝜅 <𝜃, then the min-max formula for ironing (Barlow, Bartholomew, Bremner and Brunk,
47

1972) implies that, for𝜃∈[ 𝜅,𝜃],
𝐽𝜇∗|[𝜃𝐿,𝜃](𝜃)= inf
𝑧∈[𝜃,𝜃]
sup
𝑦∈[𝜃𝐿,𝜃]
∫
[𝑦,𝑧]𝐽𝜇∗ d𝐹
𝐹(𝑧)− 𝐹(𝑦)≥ inf 𝑧∈[𝜃,𝜃] sup 𝑦∈[𝜅,𝜃]
∫
[𝑦,𝑧]𝐽𝜇∗ d𝐹
𝐹(𝑧)− 𝐹(𝑦) =𝐽𝜇∗|[𝜅,𝜃](𝜃)≥ 𝜃.
Moreover,for 𝜃∈[ 𝜃𝐿,𝜅] and𝑧≥𝜃,choose 𝑦=𝜃 inthemax-minformula. If 𝑧≤ 𝜅,equation(14)
gives ∫ 𝑧
𝜃
𝐽𝜇∗(𝑠) d𝐹(𝑠)≥ 𝜃[𝐹(𝑧)− 𝐹(𝜃)].
If𝑧 > 𝜅, equation (14) gives
∫ 𝜅
𝜃
𝐽𝜇∗(𝑠) d𝐹(𝑠)≥ 𝜃[𝐹(𝜅)− 𝐹(𝜃)].
Moreover, lettingcx𝐻 denote the convex minorant of any function𝐻,
∫ 𝑧
𝜅
𝐽𝜇∗(𝑠) d𝐹(𝑠)≥ cx

ˆ𝑧↦→
∫ ˆ𝑧
𝜅
𝐽𝜇∗(𝑠) d𝐹(𝑠)

[𝜅,𝜃]
!
(𝑧)=
∫ 𝑧
𝜅
𝐽𝜇∗|[𝜅,𝜃](𝑠) d𝐹(𝑠)
≥𝜃[𝐹(𝑧)− 𝐹(𝜅)].
Thus, ∫ 𝑧
𝜃
𝐽𝜇∗(𝑠) d𝐹(𝑠)≥ 𝜃[𝐹(𝜅)− 𝐹(𝜃)]+𝜃[𝐹(𝑧)− 𝐹(𝜅)]=𝜃[𝐹(𝑧)− 𝐹(𝜃)].
It follows that for𝜃∈[ 𝜃𝐿,𝜅],
𝐽𝜇∗|[𝜃𝐿,𝜃](𝜃)= inf
𝑧∈[𝜃,𝜃]
sup
𝑦∈[𝜃𝐿,𝜃]
∫
[𝑦,𝑧]𝐽𝜇∗ d𝐹
𝐹(𝑧)− 𝐹(𝑦)≥𝜃.
As noted earlier,𝜔(𝜃)≤ 𝛼 for all𝜃≤𝜃 <𝜃𝐿. From the above discussion, we conclude that
𝐽𝜇∗|[𝜃𝐿,𝜃](𝜃)≥ 𝜃, for all𝜃∈[ 𝜃𝐿,𝜃].
This completes the proof of Theorem 2.
48

A.4 Proof of Theorem 3
By Corollary 2, the optimal mechanisms with and without topping up coincide; hence, it remains to
identify the common optimal allocation function. The proof of the sufficiency direction of Theorem 2
shows that, whenever the two conditions in Theorem 2 hold, the common optimal allocation is given by
𝑞∗(𝜃)=
 

𝐷

𝑐,𝐽𝜇∗|[𝜃𝐿,𝜃](𝜃)

, for𝜃𝐿≤𝜃≤𝜃,
𝑞LF(𝜃), for𝜃≤𝜃 <𝜃𝐿.
UnderAssumption1,Corollary2verifiesbothconditionsinTheorem2;hencetheallocationconstructed
in the sufficiency proof of Theorem 2 is optimal. As the proof of Theorem 2 shows, the multiplier
𝜇∗ =(E[𝜔]− 𝛼)+ is the shadow cost of the (LS) constraint. IfE[𝜔] > 𝛼, then𝜇∗ > 0, and the (LS)
constraintbinds. Equivalently,thelowesttypepayszero. Since 𝐽𝜇∗ hasanatomat 𝜃,theironedallocation
is flat on an initial interval, which gives a free public option. IfE[𝜔]≤ 𝛼, then𝜇∗ = 0, so the (LS)
constraint does not force such an initial pooling region. This completes the proof of Theorem 3.
A.5 Proof of Theorem 4
Topping up. As in the proof of Theorem 2, together with the (IR) constraint𝑈≥ 𝑈LF of the lowest
type, the (TU) constraint implies all (IR) constraints. Define the candidate subutility function
𝜈∗ TU(𝜃)≔
 

𝜈LF(𝜃), for𝜃𝐻 TU(𝜇∗ TU) <𝜃 ≤𝜃,
𝑣

𝐷

𝑐,𝐽𝜇∗ TU|[𝜃,𝜃𝐻 TU(𝜇∗ TU)](𝜃)

, for𝜃≤𝜃≤𝜃𝐻 TU(𝜇∗ TU).
Also define
𝑈∗ TU≔
 

𝑈LF, if𝛼 >E[𝜔],
𝜃𝜈∗ TU(𝜃), if𝛼≤ E[𝜔].
We begin by verifying feasibility. To ensure that the candidate𝜈∗ TU is nondecreasing, it suffices to
checkthatitisnondecreasingat 𝜃𝐻 TU(𝜇∗ TU). If𝜃𝐻 TU(𝜇∗ TU)=𝜃,thereisnojumptocheck. If 𝜃𝐻 TU(𝜇∗ TU)=𝜃,
the allocation matches laissez-faire almost everywhere; by our right-continuity convention, we evaluate
the singleton at the lower endpoint as𝜈∗ TU(𝜃) = 𝜈LF(𝜃), which trivially satisfies the (TU) constraint
49

exactly everywhere. Hence, we proceed by assuming the interior case𝜃𝐻 TU(𝜇∗ TU)∈( 𝜃,𝜃). To this end,
observe that𝜃↦→𝐽𝜇∗ TU|[𝜃,𝜃](𝜃)− 𝜃 is continuous (following the min-max formula of ironing in the proof
of Theorem 2). Thus, since𝜃𝐻 TU(𝜇∗ TU)∈( 𝜃,𝜃), the continuity of𝜃↦→𝐽𝜇∗ TU|[𝜃,𝜃](𝜃)− 𝜃 and equation (4)
imply that
𝐽𝜇∗ TU|[𝜃,𝜃𝐻 TU(𝜇∗ TU)](𝜃𝐻 TU(𝜇∗ TU)) =𝜃𝐻 TU(𝜇∗ TU).
By Assumption 2,𝜃↦→
∫ 𝜃
𝜃 [𝜔(𝑠)− 𝛼] d𝐹(𝑠) is quasiconvex on[𝜃,𝜃] and equal to zero at𝜃=𝜃; hence,
𝜃↦→𝐽𝜇∗ TU(𝜃)crosses𝜃↦→𝜃atmostoncefromaboveon [𝜃,𝜃]. Thus,forany𝜃∈( 𝜃,𝜃], ˆ𝜃↦→𝐽𝜇∗ TU|[𝜃,𝜃]( ˆ𝜃)
crosses ˆ𝜃↦→ ˆ𝜃 at most once from above on[𝜃,𝜃] by Lemma 8. By the definition of𝜃𝐻 TU in equation (4),
𝐽𝜇∗ TU|[𝜃,𝜃](𝜃) >𝜃, for all𝜃 <𝜃𝐻 TU(𝜇∗ TU).
It follows that
𝐽𝜇∗ TU|[𝜃,𝜃]( ˆ𝜃)≥ ˆ𝜃, for all ˆ𝜃≤𝜃 <𝜃𝐻 TU(𝜇∗ TU).
Bythecontinuityof 𝜃↦→𝐽𝜇∗ TU|[𝜃,𝜃]( ˆ𝜃) (againfollowingthemin-maxformulaintheproofofTheorem2),
this implies
𝐽𝜇∗ TU|[𝜃,𝜃𝐻 TU(𝜇∗ TU)](𝜃)≥ 𝜃, for all𝜃≤𝜃𝐻 TU(𝜇∗ TU),
with equality at𝜃 = 𝜃𝐻 TU(𝜇∗ TU). Thus, 𝜈∗ TU is nondecreasing at𝜃𝐻 TU(𝜇∗ TU) and 𝜈∗ TU≥ 𝜈LF, so the (TU)
constraint holds. With our choice of𝑈∗ TU, this implies that the (LS) and (IR) constraints hold.
Next, we verify optimality. Let𝜆∗ TU ≔(𝛼− E[𝜔])+ denote the multiplier on the (IR) constraint
𝑈≥𝑈LF of the lowest type. In addition, define the multiplier on the (TU) constraint by
𝜌∗ TU(𝜃)≔𝛼𝑓(𝜃) h 𝜃−𝐽𝜇∗ TU(𝜃) i 1{𝜃>𝜃𝐻 TU(𝜇∗ TU)}.
We first show that𝜌∗ TU(𝜃) ≥ 0 for all𝜃 ∈ [𝜃,𝜃]. If 𝜃𝐻 TU(𝜇∗ TU) = 𝜃, 𝜌∗ TU has empty support and
nonnegativity is vacuous. If𝜃𝐻 TU(𝜇∗ TU)=𝜃, we already established that𝐽𝜇∗ TU(𝜃)≤ 𝜃. Hence, we proceed
by assuming𝜃𝐻 TU(𝜇∗ TU)∈( 𝜃,𝜃). As argued above, continuity implies that𝐽𝜇∗ TU|[𝜃,𝜃𝐻 TU(𝜇∗ TU)](𝜃𝐻 TU(𝜇∗ TU)) =
𝜃𝐻 TU(𝜇∗ TU). By the standard min-max formula for ironing, the ironed function evaluated at the upper
endpoint is weakly bounded below by the unironed function:𝐽𝜇∗ TU(𝜃𝐻 TU(𝜇∗ TU))≤ 𝜃𝐻 TU(𝜇∗ TU) in the signed
50

measure order. Because𝜃↦→𝐽𝜇∗ TU(𝜃) crosses𝜃↦→𝜃 at most once from above on[𝜃,𝜃], it follows that
𝐽𝜇∗ TU(𝜃)≤ 𝜃, for all𝜃≥𝜃𝐻 TU(𝜇∗ TU).
Thus,𝜌∗ TU(𝜃)≥ 0 for all𝜃∈[ 𝜃,𝜃], as claimed. Up to terms independent of(𝑈,𝜈), the Lagrangian can
be written as
LTU(𝑈,𝜈)=

E[𝜔]− 𝛼−𝜇∗ TU+𝜆∗ TU  𝑈+𝛼 ∫ 𝜃 𝜃  𝐽𝜇∗ TU(𝜃)+ 𝜌∗ TU(𝜃) 𝛼𝑓(𝜃)  𝜈(𝜃)− 𝑐Ψ(𝜈(𝜃))  d𝐹(𝜃).
Byconstruction,thefirsttermiszero. For 𝜃≤𝜃𝐻 TU(𝜇∗ TU),thecoefficientof 𝜈(𝜃)intheintegralis 𝐽𝜇∗ TU(𝜃);
the candidate𝜈∗ TU maximizes the Lagrangian over nondecreasing subutility functions on[𝜃,𝜃 𝐻 TU(𝜇∗ TU)].
For𝜃 >𝜃𝐻 TU(𝜇∗ TU),thecoefficientof 𝜈(𝜃) intheintegralis 𝜃,sothepointwisemaximizeroftheintegrand
is exactly𝜈LF(𝜃). Thus,(𝑈∗ TU,𝜈∗ TU) maximizes the Lagrangian.
Finally,weverifythatthecomplementaryslacknessconditionshold. Themultiplier 𝜌∗ TU issupported
only where𝜈∗ TU = 𝜈LF. If E[𝜔] > 𝛼, then𝜇∗ TU > 0 and the (LS) constraint binds by construction. If
E[𝜔] < 𝛼, then𝜆∗ TU > 0 and the (IR) constraint of the lowest type binds by construction. IfE[𝜔] =𝛼,
thenbothmultipliersarezero. Consequently,bytheLuenberger(1969)sufficiencytheorem(seeAmador
and Bagwell, 2013, Theorem 1 of Appendix B),(𝑈∗ TU,𝜈∗ TU) solves the topping-up problem.
No topping up. We first show that𝜇∗ is well-defined in equation (9). By equation (5),
𝜇max≥ max
(
0,
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)
)
=(E[𝜔]− 𝛼)+.
Thus, the interval[(E[𝜔]− 𝛼)+,𝜇 max] is nonempty. By the definition of𝜇max, for any𝜃∈[ 𝜃,𝜃],
𝐽𝜇max(𝜃)+ 𝜇max+𝛼− E[𝜔] 𝛼𝑓(𝜃) =𝜃+ 𝜇max𝜃·𝛿𝜃(𝜃)+ 𝜇max−
∫ 𝜃
𝜃 [𝜔(𝑠)− 𝛼] d𝐹(𝑠)
𝛼𝑓(𝜃) ≥𝜃.
51

Here, the inequality is interpreted in the signed measure order. Lemma 7 then implies that for any
𝜃∈[ 𝜃,𝜃 𝐻(𝜇max)],

𝐽𝜇max+ 𝜇max+𝛼− E[𝜔] 𝛼𝑓 

 [𝜃,𝜃𝐻(𝜇max)] (𝜃)≥ 𝜃 =⇒ 𝜈𝜇max(𝜃)≥ 𝜈LF(𝜃).
As such,
𝑈𝐻(𝜇max)=𝜃𝜈𝜇max(𝜃)+
∫ 𝜃𝐻(𝜇max)
𝜃
𝜈𝜇max(𝑠) d𝑠
≥𝜃𝜈LF(𝜃)+
∫ 𝜃𝐻(𝜇max)
𝜃
𝜈LF(𝑠) d𝑠≥𝑈LF(𝜃𝐻(𝜇max)).
Thisshowsthatthesetinequation(9)isnonempty. Moreover,observethatthefunction 𝜇↦→𝑈LF(𝜃𝐻(𝜇))
is continuous since𝑈LF is continuous and𝜃𝐻(𝜇) is, by equation (6), the continuous right inverse of the
upper branch of the quasiconcave function𝜃↦→
∫ 𝜃
𝜃 [𝜔(𝑠)− 𝛼] d𝐹(𝑠). The function 𝜇↦→ 𝑈𝐻(𝜇) is
also continuous since ironing is continuous with respect to the total variation norm; hence, the function
𝜇↦→𝑈𝐻(𝜇)− 𝑈LF(𝜃𝐻(𝜇)) iscontinuous. Consequently,theminimuminequation(9)isattainedand 𝜇∗
is well-defined.
For any𝜇∈[ 0,𝜇 max], denote𝜈𝜇(𝜃)≔𝑣(𝑞𝜇(𝜃)) and𝜈∗(𝜃)≔𝑣(𝑞∗(𝜃)), so that
𝜈∗(𝜃)≔
 

𝜈LF(𝜃), for𝜃𝐻(𝜇∗) <𝜃 ≤𝜃,
𝜈𝜇∗(𝜃), for𝜃≤𝜃≤𝜃𝐻(𝜇∗).
We choose the utility of the lowest type by
𝑈∗≔
 

𝜃𝜈𝜇∗(𝜃), if𝜇∗ > 0,
𝑈LF(𝜃𝐻(𝜇∗))−
∫ 𝜃𝐻(𝜇∗)
𝜃
𝜈𝜇∗(𝑠) d𝑠, if𝜇∗= 0.
We begin by verifying feasibility. We make our argument in three steps, showing each in a separate
lemma: (i) 𝜈∗ crosses 𝜈LF at most once from above on[𝜃,𝜃 𝐻(𝜇∗)]; (ii) 𝜈∗ is nondecreasing; and
(iii)(𝑈∗,𝜈∗) satisfies the (LS) and (IR) constraints.
52

Lemma 4.The subutility function𝜈𝜇∗ crosses𝜈LF at most once from above on[𝜃,𝜃 𝐻(𝜇∗)].
Proof. By Assumption 2, the following function is quasiconcave:
𝐺(𝜃)≔
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠).
Itfollowsthat 𝜃↦→𝜇∗−𝐺(𝜃) isquasiconvex;bythedefinitionof 𝜃𝐻(𝜇∗) inequation(6), 𝜃↦→𝜇∗−𝐺(𝜃)
crosses 0 at most once from above on[𝜃,𝜃 𝐻(𝜇∗)]. Hence, the following generalized function crosses𝜃
at most once from above on[𝜃,𝜃 𝐻(𝜇∗)] in the signed measure order:
𝜃↦→𝐽𝜇∗(𝜃)+ 𝜇∗+𝛼− E[𝜔] 𝛼𝑓(𝜃) =𝜃+ 𝜇∗𝜃·𝛿𝜃(𝜃)+ 𝜇∗−𝐺(𝜃) 𝛼𝑓(𝜃) .
Lemma 8 implies that single-crossing is preserved under ironing, so the following function crosses𝜃 at
most once from above on[𝜃,𝜃 𝐻(𝜇∗)]:
𝜃↦→

𝐽𝜇∗+ 𝜇∗+𝛼− E[𝜔] 𝛼𝑓 

 [𝜃,𝜃𝐻(𝜇∗)] (𝜃).
We conclude that𝜈𝜇∗ crosses𝜈LF at most once from above on[𝜃,𝜃 𝐻(𝜇∗)], as claimed. □
Lemma 5.The subutility function𝜈∗ is nondecreasing.
Proof. Since𝜈𝜇∗ isnondecreasingon [𝜃,𝜃 𝐻(𝜇∗)] and𝜈LF isnondecreasingon [𝜃𝐻(𝜇∗),𝜃],itremainsto
check that𝜈∗ is nondecreasing at𝜃𝐻(𝜇∗) whenever𝜃𝐻(𝜇∗)∈( 𝜃,𝜃).
Suppose𝜇∗= 0. Bythedefinitionof 𝜃𝐻(𝜇∗) inequation(6), 𝐺(𝜃)≥ 0forall 𝜃∈[ 𝜃,𝜃 𝐻(𝜇∗)]. Thus,
for any𝜃∈[ 𝜃,𝜃 𝐻(𝜇∗)],
𝐽𝜇∗(𝜃)+ 𝜇∗+𝛼− E[𝜔] 𝛼𝑓(𝜃) =𝜃+ 𝜇∗𝜃·𝛿𝜃(𝜃)+ 𝜇∗−𝐺(𝜃) 𝛼𝑓(𝜃) =𝜃− 𝐺(𝜃) 𝛼𝑓(𝜃)≤𝜃.
Here, the inequality is again interpreted in the signed measure order. Lemma 7 then implies that for any
𝜃∈[ 𝜃,𝜃 𝐻(𝜇∗)], 
𝐽𝜇∗+ 𝜇∗+𝛼− E[𝜔] 𝛼𝑓 

 [𝜃,𝜃𝐻(𝜇∗)] (𝜃)≤ 𝜃.
53

In particular,𝜈0(𝜃𝐻(𝜇∗))≤ 𝜈LF(𝜃𝐻(𝜇∗)). Thus,𝜈∗ is nondecreasing at𝜃𝐻(𝜇∗) if𝜇∗= 0.
Now suppose𝜇∗ > 0. By the minimality of𝜇∗ and continuity of𝜇↦→𝑈𝐻(𝜇)− 𝑈LF(𝜃𝐻(𝜇)), and
since𝜃𝐻(𝜇∗)∈( 𝜃,𝜃) by assumption, the inequality in equation (9) must in fact bind at𝜇∗:
𝑈𝐻(𝜇∗)=𝑈LF(𝜃𝐻(𝜇∗)) =⇒ 𝜃𝜈𝜇∗(𝜃)+
∫ 𝜃𝐻(𝜇∗)
𝜃
𝜈𝜇∗(𝑠) d𝑠=𝑈LF(𝜃𝐻(𝜇∗)).
(Otherwise,iftheinequalitywerestrict,itwouldcontinueholdingafterasmalldecreasein 𝜇,contradicting
the minimality of𝜇∗.) To show that 𝜈∗ is nondecreasing at𝜃𝐻(𝜇∗), suppose on the contrary that
𝜈𝜇∗(𝜃𝐻(𝜇∗)) > 𝜈LF(𝜃𝐻(𝜇∗)). Since𝜈𝜇∗ crosses𝜈LFatmostoncefromaboveon [𝜃,𝜃 𝐻(𝜇∗)] byLemma4,
we deduce that
𝜈𝜇∗(𝜃)≥ 𝜈LF(𝜃), for all𝜃∈[ 𝜃,𝜃 𝐻(𝜇∗)].
Strict inequality must hold on a subset of positive measure. Therefore,
𝑈𝐻(𝜇∗)=𝜃𝜈𝜇∗(𝜃)+
∫ 𝜃𝐻(𝜇∗)
𝜃
𝜈𝜇∗(𝑠) d𝑠 >𝜃𝜈LF(𝜃)+
∫ 𝜃𝐻(𝜇∗)
𝜃
𝜈LF(𝑠) d𝑠
=𝑈LF(𝜃𝐻(𝜇∗))+ 𝑐𝑞 LF(𝜃)≥ 𝑈LF(𝜃𝐻(𝜇∗)).
But this contradicts𝑈𝐻(𝜇∗)=𝑈LF(𝜃𝐻(𝜇∗)). Thus,𝜈∗ is nondecreasing at𝜃𝐻(𝜇∗) if𝜇∗ > 0. □
Lemma 6.(𝑈∗,𝜈∗) satisfies the(LS) and (IR)constraints.
Proof. If𝜇∗ > 0, then𝑈∗=𝜃𝜈∗(𝜃) by construction. If𝜇∗= 0, then equation (9) implies that
𝑈∗=𝑈LF(𝜃𝐻(𝜇∗))−
∫ 𝜃𝐻(𝜇∗)
𝜃
𝜈∗(𝑠) d𝑠≤𝜃𝜈∗(𝜃).
Thus,(𝑈∗,𝜈∗) satisfies the (LS) constraint.
It remains to show that(𝑈∗,𝜈∗) satisfies the (IR) constraint. To this end, define the slack in the (IR)
constraint as
Δ(𝜃)≔𝑈∗−𝑈LF+
∫ 𝜃
𝜃

𝜈∗(𝑠)− 𝜈LF(𝑠)  d𝑠.
There are two cases:
54

(i) Suppose 𝜃 ≤ 𝜃𝐻(𝜇∗). By Lemma 4, 𝜈∗ crosses 𝜈LF at most once from above on[𝜃,𝜃 𝐻(𝜇∗)];
hence,Δ is quasiconcave on[𝜃,𝜃 𝐻(𝜇∗)]. Consequently,Δ attains its minimum on[𝜃,𝜃 𝐻(𝜇∗)] at
an endpoint of that interval.
At the upper endpoint𝜃𝐻(𝜇∗),
Δ(𝜃𝐻(𝜇∗)) =𝑈∗−𝑈LF+
∫ 𝜃𝐻(𝜇∗)
𝜃

𝜈∗(𝑠)− 𝜈LF(𝑠)  d𝑠.
If𝜇∗= 0,Δ(𝜃𝐻(𝜇∗)) = 0by our definition of𝑈∗. If𝜇∗ > 0, equation (9) implies
0≤𝑈𝐻(𝜇∗)− 𝑈LF(𝜃𝐻(𝜇∗)) =𝜃𝜈𝜇∗(𝜃)− 𝑈LF+
∫ 𝜃𝐻(𝜇∗)
𝜃

𝜈𝜇∗(𝑠)− 𝜈LF(𝑠)  d𝑠
=𝑈∗−𝑈LF+
∫ 𝜃𝐻(𝜇∗)
𝜃

𝜈𝜇∗(𝑠)− 𝜈LF(𝑠)  d𝑠=Δ(𝜃𝐻(𝜇∗)).
Thus, in either case,Δ(𝜃𝐻(𝜇∗))≥ 0.
At the lower endpoint𝜃,
Δ(𝜃)=𝑈∗−𝑈LF.
If𝜇∗= 0,thenourproofofLemma5showsthat 𝜈𝜇∗(𝜃)≤ 𝜈LF(𝜃)forall𝜃∈[ 𝜃,𝜃 𝐻(𝜇∗)]. Moreover,
sinceΔ(𝜃𝐻(𝜇∗)) = 0 as shown above,
Δ(𝜃)=Δ(𝜃𝐻(𝜇∗))−
∫ 𝜃𝐻(𝜇∗)
𝜃

𝜈𝜇∗(𝑠)− 𝜈LF(𝑠)  d𝑠≥ 0.
If𝜇∗ > 0, then𝑈∗=𝜃𝜈𝜇∗(𝜃) by construction. If𝜈𝜇∗(𝜃)≥ 𝜈LF(𝜃), then
Δ(𝜃)=𝜃

𝜈𝜇∗(𝜃)− 𝜈LF(𝜃)  +𝑐𝑞 LF(𝜃)≥ 0.
If𝜈𝜇∗(𝜃) < 𝜈LF(𝜃),thenLemma4impliesthat 𝜈𝜇∗(𝜃)≤ 𝜈LF(𝜃) forall 𝜃∈[ 𝜃,𝜃 𝐻(𝜇∗)]. Therefore,
Δ(𝜃)=Δ(𝜃𝐻(𝜇∗))−
∫ 𝜃𝐻(𝜇∗)
𝜃

𝜈𝜇∗(𝑠)− 𝜈LF(𝑠)  d𝑠≥ 0.
55

Thus, in any case,Δ(𝜃)≥ 0.
We conclude that for any𝜃∈[ 𝜃,𝜃 𝐻(𝜇∗)], the (IR) constraint holds:
Δ(𝜃)≥ min

Δ(𝜃),Δ(𝜃𝐻(𝜇∗)) 	 ≥ 0.
(ii) Suppose𝜃 >𝜃𝐻(𝜇∗). Since𝜈∗(𝜃)=𝜈LF(𝜃) by construction,
Δ(𝜃)=Δ(𝜃𝐻(𝜇∗))≥ 0.
Hence, the (IR) constraint holds as well. □
Next, we verify optimality. Define the cumulative multiplier functionΛ∗ for the (IR) constraint by
Λ∗(𝜃)≔
 

E[𝜔]− 𝛼+
∫ 𝜃
𝜃
[𝛼−𝜔(𝑠)] d𝐹(𝑠), if𝜃𝐻(𝜇∗) <𝜃 ≤𝜃,
E[𝜔]− 𝛼−𝜇∗, if𝜃≤𝜃≤𝜃𝐻(𝜇∗).
By construction,Λ∗ is nondecreasing. Up to terms independent of(𝑈,𝜈), the Lagrangian can be written
as
L(𝑈,𝜈)=

E[𝜔]− 𝛼−𝜇∗−Λ∗(𝜃)  𝑈+𝛼 ∫ 𝜃
𝜃

𝐽𝜇∗(𝜃)− Λ∗(𝜃) 𝛼𝑓(𝜃)  𝜈(𝜃)− 𝑐Ψ(𝜈(𝜃))  d𝐹(𝜃).
The first term is zero by construction. For𝜃≤𝜃𝐻(𝜇∗),
𝐽𝜇∗(𝜃)− Λ∗(𝜃) 𝛼𝑓(𝜃) =𝐽𝜇∗(𝜃)+ 𝜇∗+𝛼− E[𝜔] 𝛼𝑓(𝜃) .
Thus, the subutility function𝜈𝜇∗ maximizes the Lagrangian over nondecreasing subutility functions on
[𝜃,𝜃 𝐻(𝜇∗)]. For𝜃 >𝜃𝐻(𝜇∗), the coefficient of𝜈(𝜃) in the integral is
𝐽𝜇∗(𝜃)− Λ∗(𝜃) 𝛼𝑓(𝜃) =𝜃.
Thus, the pointwise maximizer of the integrand is𝜈LF(𝜃). Hence,(𝑈∗,𝜈∗) maximizes the Lagrangian.
56

Finally, we verify that the complementary slackness conditions hold. For the (LS) constraint, if
𝜇∗ > 0, then𝑈∗ = 𝜃𝜈∗(𝜃) by construction, so the (LS) constraint binds. For the (IR) constraint, the
measure dΛ∗ is supported on[𝜃𝐻(𝜇∗),𝜃]. If𝜃𝐻(𝜇∗) < 𝜃, thenΔ(𝜃𝐻(𝜇∗)) = 0: if𝜇∗ = 0, this follows
from the definition of𝑈∗; if𝜇∗ > 0, this follows from the minimality of𝜇∗ and the continuity argument
above. Since𝜈∗=𝜈LF on(𝜃𝐻(𝜇∗),𝜃],theslackinthe(IR)constraintremainszeroonallof [𝜃𝐻(𝜇∗),𝜃].
Hence, ∫ 𝜃
𝜃
Δ(𝜃) dΛ∗(𝜃)= 0.
If 𝜃𝐻(𝜇∗) = 𝜃, then𝜇∗ = E[𝜔]− 𝛼, soΛ∗ is identically zero; hence, the complementary slackness
condition for the (IR) constraint holds.
Consequently, applying the Luenberger (1969) sufficiency theorem (see Amador and Bagwell, 2013,
Theorem 1 of Appendix B), we conclude that(𝑈∗,𝜈∗) solves the no-topping-up problem.
57

B Online Appendix: Additional Proofs
B.1 Preliminary Analysis
Webeginbyprovingtwousefullemmas. Thefirstshowsthattheironingoperatorpreservesmonotonicity,
while the second shows that the ironing operator preserves the single-crossing property.
Lemma 7.Let𝐼0=[𝜃𝐿,𝜃 0]⊆ 𝐼1=[𝜃𝐿,𝜃 1]⊆[ 𝜃,𝜃] be closed intervals with the same lower endpoint,
𝜃𝐿. Let ℎ0 and ℎ1 be generalized functions defined on𝐼0 and 𝐼1 respectively, such thatℎ1≤ ℎ0 on 𝐼0
in the signed measure order. That is, letting𝜂0 and𝜂1 denote the finite signed measures represented by
ℎ0 d𝐹 andℎ1 d𝐹,
(𝜂1−𝜂0)(𝐵)≤ 0, for every Borel set𝐵⊆ 𝐼0.
Then, for every𝜃∈ 𝐼0,ℎ1|𝐼1(𝜃)≤ ℎ0|𝐼0(𝜃).
Proof. By the min-max formula for ironing (see, for example, Barlow et al., 1972), for any generalized
functionℎ and any interval𝐼 =[𝜃𝐿,𝜃 𝐻],
ℎ|𝐼(𝜃)= inf
𝑧∈[𝜃,𝜃𝐻]
sup
𝑦∈[𝜃𝐿,𝜃]
∫
[𝑦,𝑧]ℎ d𝐹
𝐹(𝑧)− 𝐹(𝑦).
This implies that
ℎ1|𝐼1(𝜃)= inf
𝑧∈[𝜃,𝜃 1]
sup
𝑦∈[𝜃𝐿,𝜃]
∫
[𝑦,𝑧]ℎ1 d𝐹
𝐹(𝑧)− 𝐹(𝑦)≤ inf 𝑧∈[𝜃,𝜃 0] sup 𝑦∈[𝜃𝐿,𝜃]
∫
[𝑦,𝑧]ℎ1 d𝐹
𝐹(𝑧)− 𝐹(𝑦) =ℎ1|𝐼0(𝜃)
≤ inf
𝑧∈[𝜃,𝜃 0]
sup
𝑦∈[𝜃𝐿,𝜃]
∫
[𝑦,𝑧]ℎ0 d𝐹
𝐹(𝑧)− 𝐹(𝑦) =ℎ0|𝐼0(𝜃). □
Remark 1.Symmetrically, let𝐼0 =[𝜃0,𝜃 𝐻]⊆ 𝐼1 =[𝜃1,𝜃 𝐻]⊆[ 𝜃,𝜃] be closed intervals with the same
upper endpoint,𝜃𝐻. Letℎ0 andℎ1 be generalized functions defined on𝐼0 and𝐼1 respectively, such that
ℎ1≥ ℎ0 on𝐼0 in the signed measure order. Then a similar proof to that of Lemma 7 shows that for every
𝜃∈ 𝐼0,ℎ1|𝐼1(𝜃)≥ ℎ0|𝐼0(𝜃).
58

Lemma 8.Let𝐼0=[𝜃𝐿,𝜃 0]⊆ 𝐼1=[𝜃𝐿,𝜃 1]⊆[ 𝜃,𝜃] be closed intervals with the same lower endpoint,
𝜃𝐿. Letℎ0 andℎ1 be generalized functions defined on𝐼0 and𝐼1 respectively. Suppose there existsˆ𝜃∈ 𝐼0
such that in the signed measure order,
 

ℎ1≤ ℎ0, on[ ˆ𝜃,𝜃 0],
ℎ1≥ ℎ0, on[𝜃𝐿, ˆ𝜃].
(We say thatℎ1 crossesℎ0 at most once from above in𝐼0.) Then there exists𝜅∈ 𝐼0 such that
 

ℎ1|𝐼1(𝜃)− ℎ0|𝐼0(𝜃)≤ 0, for all𝜃∈[ 𝜅,𝜃 0],
ℎ1|𝐼1(𝜃)− ℎ0|𝐼0(𝜃)≥ 0, for all𝜃∈[ 𝜃𝐿,𝜅].
Proof. Let𝜂0and𝜂1denotethesignedmeasureson 𝐼0and𝐼1representedbyℎ0 d𝐹andℎ1 d𝐹,respectively.
We use the following standard variational characterization of ironing: for each𝑖∈{ 0, 1},
∫
𝐼𝑖

𝑦−ℎ𝑖|𝐼𝑖

d𝜂𝑖≤
∫
𝐼𝑖

𝑦−ℎ𝑖|𝐼𝑖

ℎ𝑖|𝐼𝑖 d𝐹, for all nondecreasing functions𝑦 :𝐼𝑖→R.
Suppose on the contrary thatℎ1|𝐼1 does not crossℎ0|𝐼0 at most once from above in𝐼0. Then there exist
nondegenerate intervals𝐼− =(𝜃− 𝐿,𝜃− 𝐻) and𝐼+ =(𝜃+ 𝐿,𝜃+ 𝐻), where𝜃𝐿≤ 𝜃− 𝐿 < 𝜃− 𝐻≤ 𝜃+ 𝐿 < 𝜃+ 𝐻≤ 𝜃0, such
that  

ℎ1|𝐼1(𝜃)− ℎ0|𝐼0(𝜃) > 0, for all𝜃∈ 𝐼+,
ℎ1|𝐼1(𝜃)− ℎ0|𝐼0(𝜃) < 0, for all𝜃∈ 𝐼−.
Let𝐼− and𝐼+ be the maximal such intervals, in the sense that there do not exist open intervals𝐼′ − ⊋ 𝐼−
and𝐼′ + ⊋ 𝐼+ such thatℎ1|𝐼1(𝜃)− ℎ0|𝐼0(𝜃) > 0 for all𝜃∈ 𝐼′ +, andℎ1|𝐼1(𝜃)− ℎ0|𝐼0(𝜃) < 0 for all𝜃∈ 𝐼′ −.
We first show that the signed measure𝜂1−𝜂0 has negative mass on some Borel subset of𝐼−. Since
ℎ1|𝐼1 < ℎ0|𝐼0 on𝐼−, the function𝑤≔ℎ0|𝐼0−ℎ1|𝐼1 defined on𝐼− is positive. Define
𝑦1≔
 

ℎ1|𝐼1, on𝐼1 𝐼−,
ℎ0|𝐼0, on𝐼−.
59

By the maximality of𝐼−,𝑦1 is nondecreasing on𝐼1. Moreover, by construction,
𝑦1−ℎ1|𝐼1 =
 

0, on𝐼1 𝐼−,
𝑤, on𝐼−.
By the earlier variational characterization of ironing,
∫
𝐼−
𝑤 d𝜂1≤
∫
𝐼−
𝑤ℎ1|𝐼1 d𝐹.
Similarly, define
𝑦0≔
 

ℎ0|𝐼0, on𝐼0 𝐼−,
ℎ1|𝐼1, on𝐼−.
By the maximality of𝐼−,𝑦0 is nondecreasing on𝐼0 as well. Moreover, by construction,
𝑦0−ℎ0|𝐼0 =
 

0, on𝐼0 𝐼−,
−𝑤, on𝐼−.
By the earlier variational characterization of ironing,
∫
𝐼−
(−𝑤) d𝜂0≤
∫
𝐼−
(−𝑤)ℎ0|𝐼0 d𝐹 =⇒
∫
𝐼−
𝑤 d𝜂0≥
∫
𝐼−
𝑤ℎ0|𝐼0 d𝐹.
It follows that
∫
𝐼−
𝑤 d(𝜂1−𝜂0)=
∫
𝐼−
𝑤 d𝜂1−
∫
𝐼−
𝑤ℎ1|𝐼1 d𝐹

|                               {z                               }
≤0
−
∫
𝐼−
𝑤 d𝜂0−
∫
𝐼−
𝑤ℎ0|𝐼0 d𝐹

|                               {z                               }
≥0
+
∫
𝐼−
𝑤

ℎ1|𝐼1−ℎ0|𝐼0

|            {z            }
=−𝑤
d𝐹≤−
∫
𝐼−
𝑤2 d𝐹 <0.
Strictinequalityholdsbecause 𝐼− isnondegenerateand 𝑤 ispositiveon 𝐼−. Thus,thereexistsaBorelset
𝐵−⊆ 𝐼− such that(𝜂1−𝜂0)(𝐵−) < 0, as claimed.
60

Next,weobservethatasymmetricargumentshowsthatthesignedmeasure 𝜂1−𝜂0 haspositivemass
on some Borel subset𝐵+ of𝐼+.
Finally,wederiveacontradictionfrombothoftheprecedingobservations. Byourassumptionthat ℎ1
crossesℎ0atmostoncefromabove,thereexists ˆ𝜃∈ 𝐼0forwhich𝜂1≤𝜂0on[ ˆ𝜃,𝜃 0]and𝜂1≥𝜂0on[𝜃𝐿, ˆ𝜃].
But 𝐼− cannot lie on the left ofˆ𝜃 (i.e., 𝜃− 𝐻 ≰ ˆ𝜃) as there exists𝐵−⊆ 𝐼− such that(𝜂1−𝜂0)(𝐵−) < 0.
Similarly,𝐼+cannotlieontherightof ˆ𝜃 (i.e.,𝜃+ 𝐿 ≱ ˆ𝜃)asthereexists 𝐵+⊆ 𝐼+suchthat(𝜂1−𝜂0)(𝐵+) > 0.
Thus,
ˆ𝜃 <𝜃− 𝐻≤𝜃+ 𝐿 < ˆ𝜃,
a contradiction. We conclude that our earlier assumption was wrong; hence,ℎ1|𝐼1 crossesℎ0|𝐼0 at most
once from above in𝐼0, as was desired to prove. □
B.2 Proof of Corollary 2
We verify the conditions in Theorem 2. First, consider any𝜃 ∈ [𝜃𝐿,𝜃]. By Assumption 1 and the
definition of𝜃𝐿, ∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)≥ 0.
Since𝜇∗=(E[𝜔]− 𝛼)+≥ 0, it follows from equation (1) that𝐽𝜇∗(𝜃)≥ 𝜃 for all𝜃∈[ 𝜃𝐿,𝜃]. Therefore,
by Lemma 7, its ironed version on the interval also satisfies
𝐽𝜇∗|[𝜃𝐿,𝜃](𝜃)≥ 𝜃, for all𝜃∈[ 𝜃𝐿,𝜃].
Consequently, the first condition in Theorem 2 holds. Next, consider any𝜃 < 𝜃𝐿. Since𝜔 is increasing,
if𝜔(𝜃) >𝛼 , then𝜔(𝑠)≥ 𝜔(𝜃) >𝛼 for all𝑠≥𝜃, which would imply
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)≥ 0.
But this contradicts the definition of𝜃𝐿, so the second condition in Theorem 2 also holds. We conclude
from Theorem 2 that the optimal mechanisms with and without topping up coincide.
61

B.3 Proof of Proposition 1
For welfare weight functions𝜔𝐻≥𝜔𝐿 satisfying Assumption 1,
(E[𝜔𝐻]− 𝛼)+≥(E[𝜔𝐿]− 𝛼)+.
It follows that𝜇∗ is weakly higher under𝜔𝐻, proving claim (i). Moreover, for all𝜃∈[ 𝜃,𝜃],
∫ 𝜃
𝜃
[𝜔𝐻(𝑠)− 𝛼] d𝐹(𝑠)≥
∫ 𝜃
𝜃
[𝜔𝐿(𝑠)− 𝛼] d𝐹(𝑠).
Consequently,
(
ˆ𝜃∈[ 𝜃,𝜃] :
∫ 𝜃
ˆ𝜃
[𝜔𝐻(𝑠)− 𝛼] d𝐹(𝑠)≥ 0
)
⊇
(
ˆ𝜃∈[ 𝜃,𝜃] :
∫ 𝜃
ˆ𝜃
[𝜔𝐿(𝑠)− 𝛼] d𝐹(𝑠)≥ 0
)
.
Equation (2) implies that𝜃𝐿 is weakly lower under𝜔𝐻, proving claim (ii). Finally, let𝜃𝐿 𝐻 and 𝜃𝐿 𝐿
denote the cutoffs under𝜔𝐻 and 𝜔𝐿, respectively; claim (ii) establishes𝜃𝐿 𝐻 ≤ 𝜃𝐿 𝐿. For 𝜃 < 𝜃𝐿 𝐻, both
environments assign the laissez-faire allocation𝑞LF. For𝜃∈[ 𝜃𝐿 𝐻,𝜃 𝐿 𝐿), the allocation under𝜔𝐿 is𝑞LF,
while the allocation under𝜔𝐻 is weakly higher than𝑞LF (as verified in the proof of Corollary 2). Next,
let𝜇∗ 𝐻 and𝜇∗ 𝐿 denote the multipliers under𝜔𝐻 and𝜔𝐿; claim (i) establishes that𝜇∗ 𝐻≥ 𝜇∗ 𝐿. For𝜃≥𝜃𝐿 𝐿,
𝜃+
𝜇∗ 𝐻𝜃·𝛿𝜃(𝜃)+ ∫ 𝜃 𝜃 [𝜔𝐻(𝑠)− 𝛼] d𝐹(𝑠)
𝛼𝑓(𝜃) ≥𝜃+
𝜇∗ 𝐿𝜃·𝛿𝜃(𝜃)+ ∫ 𝜃 𝜃 [𝜔𝐿(𝑠)− 𝛼] d𝐹(𝑠)
𝛼𝑓(𝜃) .
Applying Remark 1 yields that𝐽𝜇∗ 𝐻|[𝜃𝐿 𝐻,𝜃]≥ 𝐽𝜇∗ 𝐿|[𝜃𝐿 𝐿,𝜃] on[𝜃𝐿 𝐿,𝜃]. Thus, the optimal allocation function
𝑞∗ is pointwise weakly higher under𝜔𝐻, proving claim (iii) and completing the proof of Proposition 1.
62

B.4 Proof of Proposition 2
Let𝜔𝐻 and𝜔𝐿 be welfare weight functions satisfying Assumption 1 with the same mean, and suppose
that𝜔𝐻 is a mean-preserving spread of𝜔𝐿. Since E[𝜔𝐻]= E[𝜔𝐿],
(E[𝜔𝐻]− 𝛼)+=(E[𝜔𝐿]− 𝛼)+.
It follows that𝜇∗ is unchanged, proving claim (i). Moreover, for all𝜃∈[ 𝜃,𝜃],
∫ 𝜃
𝜃
𝜔𝐻(𝑠) d𝐹(𝑠)≥
∫ 𝜃
𝜃
𝜔𝐿(𝑠) d𝐹(𝑠).
AsintheproofofProposition1,thisimpliesthat 𝜃𝐿 isweaklylowerunder 𝜔𝐻,provingclaim(ii). Finally,
combining claims (i) and (ii) and invoking Remark 1, we conclude as in the proof of Proposition 1 that
𝐽𝜇∗|[𝜃𝐿,𝜃]—andhencetheoptimalallocationfunction 𝑞∗—ispointwiseweaklyhigherunder 𝜔𝐻, proving
claim (iii) and completing the proof of Proposition 2.
B.5 Proof of Corollary 3
We consider three cases:
(i) If𝛼≥ max𝜔, then laissez-faire is optimal under both participation structures by Theorem 1, so
topping up does not affect the optimal mechanism.
(ii) If max𝜔 > 𝛼≥ E[𝜔], then Theorem 1 implies that the social planner intervenes without topping
up but not with topping up, so the two mechanisms differ.
(iii) If E[𝜔] >𝛼 , then the topping-up cutoff type defined in equation (2) is𝜃𝐿 =𝜃 since
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)= E[𝜔]− 𝛼 >0.
Observe from equation (1) that the ironed version𝐽𝜇∗(𝜃) of the generalized virtual valuation is
nonincreasing (from the signed measure monotonicity of𝐽𝜇∗ in𝛼 and because ironing preserves
63

monotonicity by Lemma 7) and continuous in𝛼 for fixed𝜃∈[ 𝜃,𝜃] (due to continuity of𝐽𝜇∗ in𝛼
and because ironing preserves continuity by the min-max formula). Define
C≔
n
𝛼∈( 0, E[𝜔]) :𝐽𝜇∗(𝜃)≥ 𝜃, for all𝜃∈[ 𝜃,𝜃]
o
.
Let𝛼min ≔ sup C, with𝛼min = 0 if C is empty. Monotonicity in𝛼 implies that C is a lower set
ofR++. By Theorem 2, the optimal mechanisms with and without topping up must differ for any
𝛼 >𝛼min, and they must coincide for any𝛼≤𝛼min.
For𝛼≤ min𝜔, observe that
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)≥ 0, for all𝜃∈[ 𝜃,𝜃].
Therefore,𝐽𝜇∗(𝜃)≥ 𝜃—and hence𝐽𝜇∗(𝜃)≥ 𝜃, by Lemma 7—for all𝜃∈[ 𝜃,𝜃]. It follows that
𝛼min≥ min𝜔. Moreover, at𝛼 = E[𝜔], Theorem 1 implies that the optimal mechanisms differ
because max𝜔 >E[𝜔] under Assumption 2. Thus,𝛼min < E[𝜔].
B.6 Proof of Proposition 3
First, observe that the comparison between𝜇∗ TU and𝜇∗ follows from equations (7) and (9):
𝜇∗ TU=(E[𝜔]− 𝛼)+≤ 𝜇∗.
Next,weshowthatthecutoffwithouttoppingupisweaklyhigher: 𝜃𝐻 TU(𝜇∗ TU)≤ 𝜃𝐻(𝜇∗). Tothisend,
consider two cases.
(i) Suppose𝜇∗ TU= 0. In this case,E[𝜔]≤ 𝛼. Since𝜔 is decreasing by Assumption 2,
∫ 𝜃
𝜃
[𝜔(𝑠)− 𝛼] d𝐹(𝑠)≤ 0 =⇒ 𝐽0(𝜃)≤ 𝜃, for all𝜃∈[ 𝜃,𝜃].
64

Thus, equations (4) and (6) imply that
𝜃𝐻 TU(𝜇∗ TU)=𝜃≤𝜃𝐻(𝜇∗).
(ii) Suppose𝜇∗ TU > 0. Then𝜇∗ TU= E[𝜔]− 𝛼= ∫ 𝜃 𝜃 [𝜔(𝑠)− 𝛼] d𝐹(𝑠).
If𝜇∗=𝜇∗ TU, then equation (6) implies that
𝜃𝐻(𝜇∗)=𝜃𝐻(E[𝜔]− 𝛼)=𝜃≥𝜃𝐻 TU(𝜇∗ TU).
If𝜇∗ > 𝜇∗ TU, then equation (6) implies that𝜃𝐻(𝜇∗) <𝜃. Now, observe that
𝐽𝜇∗(𝜃)+ 𝜇∗+𝛼− E[𝜔] 𝛼𝑓(𝜃) =𝜃+ 𝜇∗𝜃·𝛿𝜃(𝜃)+ 𝜇∗− ∫ 𝜃 𝜃 [𝜔(𝑠)− 𝛼] d𝐹(𝑠) 𝛼𝑓(𝜃)
≥𝜃+
𝜇∗ TU𝜃·𝛿𝜃(𝜃)+ 𝜇∗ TU− ∫ 𝜃 𝜃 [𝜔(𝑠)− 𝛼] d𝐹(𝑠)
𝛼𝑓(𝜃)
=𝐽𝜇∗ TU(𝜃)+ 𝜇∗ TU+𝛼− E[𝜔] 𝛼𝑓(𝜃) =𝐽𝜇∗ TU(𝜃), for all𝜃∈[ 𝜃,𝜃].
Thus, Lemma 7 implies that

𝐽𝜇∗+ 𝜇∗+𝛼− E[𝜔] 𝛼𝑓

 [𝜃,𝜃𝐻(𝜇∗)] ! (𝜃)≥ 𝐽𝜇∗ TU|[𝜃,𝜃𝐻(𝜇∗)](𝜃), for all𝜃∈[ 𝜃,𝜃 𝐻(𝜇∗)].
In particular, we obtain
𝜃𝐻(𝜇∗)≥

𝐽𝜇∗+ 𝜇∗+𝛼− E[𝜔] 𝛼𝑓

 [𝜃,𝜃𝐻(𝜇∗)] ! (𝜃𝐻(𝜇∗))≥ 𝐽𝜇∗ TU|[𝜃,𝜃𝐻(𝜇∗)](𝜃𝐻(𝜇∗)).
Here, the first inequality follows from the feasibility verification in the proof of Theorem 4, since
the optimal mechanism without topping up is nondecreasing at the cutoff𝜃𝐻(𝜇∗). By minimality
in equation (4), it follows that
𝜃𝐻 TU(𝜇∗ TU)≤ 𝜃𝐻(𝜇∗).
65

Finally, we show that𝑞∗ crosses𝑞∗ TU at most once from above. For a given𝜃0∈[ 𝜃,𝜃], suppose that
𝑞∗(𝜃0)≤ 𝑞∗ TU(𝜃0). We consider two cases.
(i) Suppose𝜃0≤𝜃𝐻 TU(𝜇∗ TU). Our computation above showed that
ℎ(𝜃)≔𝐽𝜇∗(𝜃)+ 𝜇∗+𝛼− E[𝜔] 𝛼𝑓(𝜃) ≥ 𝐽𝜇∗ TU(𝜃)≕ℎTU(𝜃), for all𝜃∈[ 𝜃,𝜃].
In particular,ℎ crossesℎTU at most once from above in[𝜃,𝜃 𝐻 TU(𝜇∗ TU)]. By Lemma 8,ℎ|[𝜃,𝜃𝐻(𝜇∗)]
crossesℎTU|[𝜃,𝜃𝐻 TU(𝜇∗ TU)] at most once from above in[𝜃,𝜃 𝐻 TU(𝜇∗ TU)]; this implies that𝑞∗ crosses𝑞∗ TU
at most once from above in[𝜃,𝜃 𝐻 TU(𝜇∗ TU)]. Thus,𝑞∗(𝜃)≤ 𝑞∗ TU(𝜃) for all𝜃∈[ 𝜃0,𝜃 𝐻 TU(𝜇∗ TU)].
It remains to extend the comparison beyond𝜃𝐻 TU(𝜇∗ TU). If𝜃𝐻 TU(𝜇∗ TU) = 𝜃, there is nothing further
to prove; hence, we assume below that𝜃𝐻 TU(𝜇∗ TU) < 𝜃. By construction,𝑞∗ TU(𝜃) = 𝑞LF(𝜃) for all
𝜃∈( 𝜃𝐻 TU(𝜇∗ TU),𝜃]. In particular, because the ironed generalized virtual valuation is weakly below
identity at the cutoff, Lemma 4 implies that
𝑞∗(𝜃𝐻 TU(𝜇∗ TU))≤ 𝑞∗ TU(𝜃𝐻 TU(𝜇∗ TU))≤ 𝑞LF(𝜃𝐻 TU(𝜇∗ TU)).
By Lemma 4, it follows that
𝑞∗(𝜃)≤ 𝑞LF(𝜃)=𝑞∗ TU(𝜃), for all𝜃∈[ 𝜃𝐻 TU(𝜇∗ TU),𝜃].
This shows that, in fact,𝑞∗(𝜃)≤ 𝑞∗ TU(𝜃) for all𝜃≥𝜃0.
(ii) Suppose𝜃0 > 𝜃𝐻 TU(𝜇∗ TU). Since𝑞∗ crosses𝑞LF at most once from above in[𝜃,𝜃 𝐻(𝜇∗)], a similar
argument to that of the previous case shows that
𝑞∗(𝜃)≤ 𝑞LF(𝜃)=𝑞∗ TU(𝜃), for all𝜃∈[ 𝜃0,𝜃].
Hence,𝑞∗(𝜃)≤ 𝑞∗ TU(𝜃) for all𝜃≥𝜃0.
Thus,𝑞∗ remains pointwise weakly lower than𝑞∗ TU once𝑞∗ crosses𝑞∗ TU from above. Consequently,𝑞∗
crosses𝑞∗ TU at most once from above.
66

B.7 Proof of Proposition 4
Topping up. For welfare weight functions𝜔𝐻≥𝜔𝐿 satisfying Assumption 2,
(E[𝜔𝐻]− 𝛼)+≥(E[𝜔𝐿]− 𝛼)+.
It follows that𝜇∗ TU is weakly higher under𝜔𝐻, proving claim (i). Moreover, for all𝜃∈[ 𝜃,𝜃],
∫ 𝜃
𝜃
[𝜔𝐻(𝑠)− 𝛼] d𝐹(𝑠)≥
∫ 𝜃
𝜃
[𝜔𝐿(𝑠)− 𝛼] d𝐹(𝑠).
Thus,𝐽𝜇∗ TU|[𝜃,𝜃](𝜃)—andhence 𝐽𝜇∗ TU|[𝜃,𝜃](𝜃),byLemma7—isweaklyhigherunder 𝜔𝐻 forall 𝜃∈[ 𝜃,𝜃].
Consequently, the following set is weakly smaller (in the sense of set inclusion) under𝜔𝐻:
n
𝜃∈[ 𝜃,𝜃] :𝐽𝜇∗ TU|[𝜃,𝜃](𝜃)≤ 𝜃
o
.
Equation (4) therefore implies that𝜃𝐻 TU(𝜇∗ TU) is weakly higher under𝜔𝐻, proving claim (ii). Finally, the
topping-up allocation is the unique solution to the constrained problem
max
𝜈∈I
(∫ 𝜃
𝜃
[𝐽(𝜃)𝜈(𝜃)− 𝑐Ψ(𝜈(𝜃))] d𝐹(𝜃) :𝜈(𝜃)≥ 𝜈LF(𝜃), for all𝜃∈[ 𝜃,𝜃]
)
.
Observe that the feasible set is a sublattice under pointwise maximum and minimum, the objective has
increasing differences in(𝜈,𝐽) in the signed measure order, and strict convexity ofΨ yields a unique
maximizer. Since𝐽𝜇∗ TU isweaklyhigherunder 𝜔𝐻,itfollowsthat 𝜈∗ TU isweaklyhigherunder 𝜔𝐻 (Topkis,
1998, Theorem 2.8.1). Thus,𝑞∗ TU is weakly higher under𝜔𝐻, proving claim (iii).
No topping up. For𝑖∈{ 𝐻,𝐿}, let𝜃𝐻 𝑖(𝜇) denote the cutoff under𝜔𝑖:
𝜃𝐻 𝑖(𝜇)≔ max
(
𝜃∈[ 𝜃,𝜃] :
∫ 𝜃
𝜃
[𝜔𝑖(𝑠)− 𝛼] d𝐹(𝑠)≥ 𝜇
)
.
67

Also define
 

𝜇max,𝑖≔ max
𝜃∈[𝜃,𝜃]
∫ 𝜃
𝜃
[𝜔𝑖(𝑠)− 𝛼] d𝐹(𝑠),
𝑞𝜇,𝑖(𝜃)≔𝐷
'››
«
𝑐, '›
«
𝑧↦→𝑧+
𝜇𝜃·𝛿𝜃(𝑧)+ 𝜇−
∫ 𝑧
𝜃 [𝜔𝑖(𝑠)− 𝛼] d𝐹(𝑠)
𝛼𝑓(𝑧)
“ﬁ
‹

[𝜃,𝜃𝐻 𝑖 (𝜇)]
(𝜃)
“ﬁﬁ
‹
,
𝑈𝐻 𝑖 (𝜇)≔𝜃𝑣(𝑞𝜇,𝑖(𝜃))+
∫ 𝜃𝐻 𝑖 (𝜇)
𝜃
𝑣(𝑞𝜇,𝑖(𝑠)) d𝑠,
Φ𝑖(𝜇)≔𝑈𝐻 𝑖 (𝜇)− 𝑈LF(𝜃𝐻 𝑖(𝜇)).
Lemma 9.IfΦ𝐻(𝜇)≥ 0 for some𝜇∈[ 0,𝜇 max,𝐿], thenΦ𝐿(𝜇)≥ 0.
Proof. We begin by showing that𝜃𝐻 𝐻(𝜇)≥ 𝜃𝐻 𝐿(𝜇). Since𝜔𝐻≥𝜔𝐿,
∫ 𝜃
𝜃
[𝜔𝐻(𝑠)− 𝛼] d𝐹(𝑠)≥
∫ 𝜃
𝜃
[𝜔𝐿(𝑠)− 𝛼] d𝐹(𝑠), for all𝜃∈[ 𝜃,𝜃].
Thus,
(
𝜃∈[ 𝜃,𝜃] :
∫ 𝜃
𝜃
[𝜔𝐻(𝑠)− 𝛼] d𝐹(𝑠)≥ 𝜇
)
⊇
(
𝜃∈[ 𝜃,𝜃] :
∫ 𝜃
𝜃
[𝜔𝐿(𝑠)− 𝛼] d𝐹(𝑠)≥ 𝜇
)
.
As the maximum of a larger set,𝜃𝐻 𝐻(𝜇)≥ 𝜃𝐻 𝐿(𝜇). Now, for𝜃∈[ 𝜃,𝜃 𝐻 𝐿(𝜇)],
𝜇𝜃·𝛿𝜃(𝜃)+ 𝜇−
∫ 𝜃
𝜃 [𝜔𝐻(𝑠)− 𝛼] d𝐹(𝑠)
𝛼𝑓(𝜃) ≤
𝜇𝜃·𝛿𝜃(𝜃)+ 𝜇−
∫ 𝜃
𝜃 [𝜔𝐿(𝑠)− 𝛼] d𝐹(𝑠)
𝛼𝑓(𝜃) .
By Lemma 7, this implies that𝑞𝜇,𝐻(𝜃)≤ 𝑞𝜇,𝐿(𝜃) for all𝜃∈[ 𝜃,𝜃 𝐻 𝐿(𝜇)]. Next, consider two cases:
• Case #1. Suppose that
∫ 𝜃𝐻 𝐻(𝜇)
𝜃𝐻 𝐿(𝜇)

𝑣(𝑞𝜇,𝐻(𝑠))− 𝑣(𝑞LF(𝑠))  d𝑠≤ 0.
68

Then
0≤Φ𝐻(𝜇)=𝜃𝑣(𝑞𝜇,𝐻(𝜃))− 𝑈LF(𝜃)+
∫ 𝜃𝐻 𝐻(𝜇)
𝜃

𝑣(𝑞𝜇,𝐻(𝑠))− 𝑣(𝑞LF(𝑠))  d𝑠
≤𝜃𝑣(𝑞𝜇,𝐻(𝜃))− 𝑈LF(𝜃)+
∫ 𝜃𝐻 𝐿(𝜇)
𝜃

𝑣(𝑞𝜇,𝐻(𝑠))− 𝑣(𝑞LF(𝑠))  d𝑠
≤𝜃𝑣(𝑞𝜇,𝐿(𝜃))− 𝑈LF(𝜃)+
∫ 𝜃𝐻 𝐿(𝜇)
𝜃

𝑣(𝑞𝜇,𝐿(𝑠))− 𝑣(𝑞LF(𝑠))  d𝑠=Φ 𝐿(𝜇).
Consequently,Φ𝐻(𝜇)≥ 0implies thatΦ𝐿(𝜇)≥ 0 also, as claimed.
• Case #2. Suppose that
∫ 𝜃𝐻 𝐻(𝜇)
𝜃𝐻 𝐿(𝜇)

𝑣(𝑞𝜇,𝐻(𝑠))− 𝑣(𝑞LF(𝑠))  d𝑠 >0.
This implies that𝑞𝜇,𝐻 > 𝑞LF on a subset of positive measure in the interval𝜃𝐻 𝐿(𝜇),𝜃 𝐻 𝐻(𝜇).
However, by Lemma 8,𝑞𝜇,𝐻 crosses𝑞LF at most once in[𝜃,𝜃 𝐻 𝐻(𝜇)] from above. It follows that
𝑞𝜇,𝐿(𝜃𝐻 𝐿(𝜇))≥ 𝑞𝜇,𝐻(𝜃𝐻 𝐿(𝜇))≥ 𝑞LF(𝜃𝐻 𝐿(𝜇)).
By Lemma 8 again,𝑞𝜇,𝐿 crosses 𝑞LF at most once in[𝜃,𝜃 𝐻 𝐿(𝜇)] from above, implying that
𝑞𝜇,𝐿(𝜃)≥ 𝑞LF(𝜃) for all𝜃∈[ 𝜃,𝜃 𝐻 𝐿(𝜇)].
Consequently,
Φ𝐿(𝜇)=𝜃𝑣(𝑞𝜇,𝐿(𝜃))− 𝑈LF(𝜃)+
∫ 𝜃𝐻 𝐿(𝜇)
𝜃

𝑣(𝑞𝜇,𝐿(𝑠))− 𝑣(𝑞LF(𝑠))  d𝑠
|                                           {z                                           }
≥0
≥𝜃𝑣(𝑞LF(𝜃))− 𝑈LF(𝜃)=𝑐𝑞 LF(𝜃)≥ 0.
Thus,Φ𝐿(𝜇)≥ 0 in either case, concluding the proof of the lemma. □
69

We now show that𝜇∗ is weakly higher under𝜔𝐻. Suppose on the contrary that𝜇∗ 𝐻 < 𝜇∗ 𝐿. Then
𝜇∗ 𝐻 < 𝜇∗ 𝐿≤ 𝜇max,𝐿 =⇒ 𝜇∗ 𝐻∈[ 0,𝜇 max,𝐿].
SinceΦ𝐻(𝜇∗ 𝐻)≥ 0,Lemma9impliesthat Φ𝐿(𝜇∗ 𝐻)≥ 0;butthiscontradictstheminimalityof 𝜇∗ 𝐿. Thus,
the multiplier𝜇∗ is weakly higher under𝜔𝐻, proving claim (i).
Next, we show that the cutoff𝜃𝐻(𝜇∗) is weakly higher under𝜔𝐻. For𝑖∈{ 𝐻,𝐿}, define
 

𝜅𝑖 ≔ max
(
𝜃∈[ 𝜃,𝜃] :
∫ 𝜃
𝜃
[𝜔𝑖(𝑠)− 𝛼] d𝐹(𝑠)≥ (E[𝜔𝑖]− 𝛼)+
)
,
𝜅𝑖∈ arg max
𝜃∈[𝜃,𝜃]
∫ 𝜃
𝜃
[𝜔𝑖(𝑠)− 𝛼] d𝐹(𝑠).
Since each𝜔𝑖 is decreasing by Assumption 2,𝜅𝑖 is uniquely defined. In addition, define𝜇𝑖 :[𝜅𝑖,𝜅𝑖]→
[(E[𝜔𝑖]− 𝛼)+,𝜇 max,𝑖] by
𝜇𝑖(𝜅)≔
∫ 𝜅
𝜃
[𝜔𝑖(𝑠)− 𝛼] d𝐹(𝑠).
As defined,𝜅𝐿≤ 𝜅𝐻 (Topkis, 1998, Theorem 2.8.1). Moreover, we claim that𝜅𝐻≥ 𝜅𝐿:
(i) Suppose E[𝜔𝐿] >𝛼 . Then E[𝜔𝐻]≥ E[𝜔𝐿] >𝛼 , in which case𝜅𝐻 =𝜅𝐿 =𝜃.
(ii) Suppose E[𝜔𝐻] >𝛼 ≥ E[𝜔𝐿]. Then𝜅𝐻 =𝜃≥ 𝜅𝐿, so the claim holds.
(iii) Suppose𝛼≥ E[𝜔𝐻]. Then(E[𝜔𝐻]− 𝛼)+ =(E[𝜔𝐿]− 𝛼)+ = 0. Since 𝜔𝐻≥ 𝜔𝐿 pointwise, it
follows from the definition of𝜅𝑖 that𝜅𝐻≥ 𝜅𝐿.
Since𝜔𝐻 and𝜔𝐿 are decreasing,𝜇𝐻 and𝜇𝐿 are decreasing as well. By construction,
𝜅= max
(
𝜃∈[ 𝜃,𝜃] :
∫ 𝜃
𝜃
[𝜔𝑖(𝑠)− 𝛼] d𝐹(𝑠)≥ 𝜇𝑖(𝜅)
)
.
Next, for𝑖∈{ 𝐻,𝐿}, define
𝑞𝑖(𝜃;𝜅)≔𝐷'›
«
𝑐,

𝑧↦→𝑧+
𝜇𝑖(𝜅)𝜃·𝛿𝜃(𝑧)+
∫ 𝜅
𝑧 [𝜔𝑖(𝑠)− 𝛼] d𝐹(𝑠)
𝛼𝑓(𝑧)
!

[𝜃,𝜅]
(𝜃)“ﬁ
‹
.
70

For every𝜅∈[ 𝜅𝐿,𝜅𝐿]∩[ 𝜅𝐻,𝜅𝐻],𝜔𝐻≥𝜔𝐿 implies
𝑞𝐻(·;𝜅)≥ 𝑞𝐿(·;𝜅), on[𝜃,𝜅].
By equation (9), the optimal cutoff under𝜔𝑖 is
𝜅∗ 𝑖 ≔ max
(
𝜅∈[ 𝜅𝑖,𝜅𝑖] :𝜃𝑣(𝑞𝑖(𝜃;𝜅))+
∫ 𝜅
𝜃
𝑣(𝑞𝑖(𝑠;𝜅)) d𝑠≥𝑈LF(𝜅)
)
.
If𝜅∗ 𝐻 < 𝜅∗ 𝐿, then𝜅∗ 𝐿 > 𝜅∗ 𝐻≥ 𝜅𝐻 and𝜅∗ 𝐿≤ 𝜅𝐿≤ 𝜅𝐻; hence,𝜅∗ 𝐿∈[ 𝜅𝐻,𝜅𝐻]. By the maximality of𝜅∗ 𝐻, we
obtain a contradiction:
𝑈LF(𝜅∗ 𝐿) >𝜃 𝑣(𝑞𝐻(𝜃;𝜅∗ 𝐿))+
∫ 𝜅∗ 𝐿
𝜃
𝑣(𝑞𝐻(𝑠;𝜅∗ 𝐿)) d𝑠
≥𝜃𝑣(𝑞𝐿(𝜃;𝜅∗ 𝐿))+
∫ 𝜅∗ 𝐿
𝜃
𝑣(𝑞𝐿(𝑠;𝜅∗ 𝐿)) d𝑠≥𝑈LF(𝜅∗ 𝐿).
Therefore,𝜅∗ 𝐻≥ 𝜅∗ 𝐿, proving claim (ii).
Finally, for𝑖∈{ 𝐻,𝐿}, define the generalized functionℎ𝑖 on the interval[𝜃,𝜅∗ 𝑖] by
ℎ𝑖(𝜃)≔𝜃+
𝜇∗ 𝑖𝜃·𝛿𝜃(𝜃)+ 𝜇∗ 𝑖− ∫ 𝜃 𝜃 [𝜔𝑖(𝑠)− 𝛼] d𝐹(𝑠)
𝛼𝑓(𝜃) .
For all𝜃∈[ 𝜃,𝜅∗ 𝐿],
ℎ𝐻(𝜃)− ℎ𝐿(𝜃)=
𝜇∗ 𝐻−𝜇∗ 𝐿 𝜃·𝛿𝜃(𝜃)+ 𝜇∗ 𝐻−𝜇∗ 𝐿 − ∫ 𝜃 𝜃 [𝜔𝐻(𝑠)− 𝜔𝐿(𝑠)] d𝐹(𝑠)
𝛼𝑓(𝜃) .
Thus,ℎ𝐻 crossesℎ𝐿 atmostoncefromabovein [𝜃,𝜅∗ 𝐿]. ByLemma8, ℎ𝐻|[𝜃,𝜅∗ 𝐻] crossesℎ𝐿|[𝜃,𝜅∗ 𝐿] atmost
once from above in[𝜃,𝜅∗ 𝐿]; this implies that𝑞𝜇∗ 𝐻,𝐻 crosses 𝑞𝜇∗ 𝐿,𝐿 at most once from above in[𝜃,𝜅∗ 𝐿].
Moreover,byLemma4, 𝑞𝜇∗ 𝐻,𝐻 crosses𝑞LFatmostoncefromabovein [𝜃,𝜅∗ 𝐻]. Thefeasibilityverification
in the proof of Theorem 4 also implies that𝑞𝜇∗ 𝐿,𝐿(𝜅∗ 𝐿)≤ 𝑞LF(𝜅∗ 𝐿). It remains to show that𝑞∗ 𝐻 crosses𝑞∗ 𝐿
at most once from above in the full interval[𝜃,𝜃]:
71

(i) If𝑞∗ 𝐻( ˆ𝜃)≤ 𝑞∗ 𝐿( ˆ𝜃) for some ˆ𝜃≤ 𝜅∗ 𝐿, then
𝑞𝜇∗ 𝐻,𝐻(𝜃)≤ 𝑞𝜇∗ 𝐿,𝐿(𝜃), for all𝜃∈[ ˆ𝜃,𝜅∗ 𝐿].
In particular,
𝑞𝜇∗ 𝐻,𝐻(𝜅∗ 𝐿)≤ 𝑞𝜇∗ 𝐿,𝐿(𝜅∗ 𝐿)≤ 𝑞LF(𝜅∗ 𝐿).
Since𝑞𝜇∗ 𝐻,𝐻 crosses𝑞LF at most once from above in[𝜃,𝜅∗ 𝐻] by Lemma 4, it follows that
𝑞𝜇∗ 𝐻,𝐻(𝜃)≤ 𝑞LF(𝜃), for all𝜃∈[ 𝜅∗ 𝐿,𝜅∗ 𝐻].
Thus,𝑞∗ 𝐻(𝜃)≤ 𝑞∗ 𝐿(𝜃) for all𝜃≥ ˆ𝜃.
(ii) If𝑞∗ 𝐻( ˆ𝜃)≤ 𝑞∗ 𝐿( ˆ𝜃) for some ˆ𝜃 > 𝜅∗ 𝐿, then𝑞∗ 𝐿( ˆ𝜃) = 𝑞LF( ˆ𝜃). If ˆ𝜃≤ 𝜅∗ 𝐻, then Lemma 4 implies that
𝑞∗ 𝐻(𝜃)≤ 𝑞LF(𝜃)=𝑞∗ 𝐿(𝜃) for all𝜃≥ ˆ𝜃. If ˆ𝜃 > 𝜅∗ 𝐻, then𝑞∗ 𝐻(𝜃)=𝑞∗ 𝐿(𝜃)=𝑞LF(𝜃) for all𝜃≥ ˆ𝜃.
Weconcludethattheoptimalallocationfunctionunder 𝜔𝐻 crossestheoptimalallocationfunctionunder
𝜔𝐿 at most once from above in[𝜃,𝜃], proving claim (iii).
B.8 Proof of Proposition 5
Topping up. Since E[𝜔𝐻]= E[𝜔𝐿], it follows that
(E[𝜔𝐻]− 𝛼)+=(E[𝜔𝐿]− 𝛼)+.
Hence,𝜇∗ TU is unchanged, proving claim (i). Moreover, for all𝜃∈[ 𝜃,𝜃]:
𝜃+
𝜇∗ TU𝜃·𝛿𝜃(𝜃)+ ∫ 𝜃 𝜃 [𝜔𝐻(𝑠)− 𝛼] d𝐹(𝑠)
𝛼𝑓(𝜃) ≤𝜃+
𝜇∗ TU𝜃·𝛿𝜃(𝜃)+ ∫ 𝜃 𝜃 [𝜔𝐿(𝑠)− 𝛼] d𝐹(𝑠)
𝛼𝑓(𝜃) .
72

Thus,𝐽𝜇∗ TU|[𝜃,𝜃](𝜃)—andhence 𝐽𝜇∗ TU|[𝜃,𝜃](𝜃)—isweaklylowerfor 𝜔𝐻 foreveryfixed 𝜃∈[ 𝜃,𝜃]. Assuch,
the following set is weakly larger (in the sense of set inclusion) under𝜔𝐻:
n
𝜃∈[ 𝜃,𝜃] :𝐽𝜇∗ TU|[𝜃,𝜃](𝜃)≤ 𝜃
o
.
By equation (4),𝜃𝐻 TU(𝜇∗ TU) is weakly lower under𝜔𝐻, proving claim (ii). Finally, as in our proof of
Proposition 4, the topping-up allocation is the unique solution to the constrained problem
max
𝜈∈I
(∫ 𝜃
𝜃
[𝐽(𝜃)𝜈(𝜃)− 𝑐Ψ(𝜈(𝜃))] d𝐹(𝜃) :𝜈(𝜃)≥ 𝜈LF(𝜃), for all𝜃∈[ 𝜃,𝜃]
)
.
The feasible set is common across𝜔𝐻 and𝜔𝐿. Since𝐽𝜇∗ TU is weakly lower under𝜔𝐻, it follows that𝜈∗ TU
is weakly lower under𝜔𝐻 (Topkis, 1998, Theorem 2.8.1). Thus,𝑞∗ TU is weakly lower under𝜔𝐻, proving
claim (iii).
No topping up. Our proof of claim (i) in Proposition 4—and, in particular, Lemma 9—holds with𝜔𝐻
being a mean-preserving spread of𝜔𝐿. Thus, the same argument applies here, proving claim (i).
73
