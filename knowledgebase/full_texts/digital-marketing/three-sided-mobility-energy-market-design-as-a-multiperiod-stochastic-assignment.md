---
title: Three-sided mobility-energy market design as a multiperiod stochastic assignment game
url: https://arxiv.org/abs/2609.05449
category: digital-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Hai Yang
- Joseph Y. J. Chow
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.05449
pages: 38
chars: 89906
fetched_at: '2026-11-08T13:19:28+00:00'
kb_version: 1
---

# Three-sided mobility-energy market design as a multiperiod stochastic assignment game

Three-sided mobility-energy market design as a multiperiod
stochastic assignment game
Hai Yanga, Joseph J. Y. Chowa,∗
aC2SMART Center, Department of Civil, Urban, and Environmental Engineering, New York University
Tandon School of Engineering, 6 MetroTech Center, Brooklyn, NY 11201, USA
Abstract
As mobility service providers (MSPs) and energy providers (EPs) expand electric vehicle ecosys-
tems, models are needed to understand their interactions within a three-sided market. Existing
frameworks often overlook the temporal interdependencies between mobility and charging de-
mands. We address this gap by proposing a bilevel problem as an assignment game overseen
by a market regulator. The upper level optimizes service pricing to maximize platform prof-
itability. The lower level models a multi-stakeholder equilibrium using a scalable, link-based
Perturbed Utility Route Choice (PURC) framework. The evaluation time frame is divided into
discrete intervals, capturing the temporal lag between mobility and charging demand via an
empirical affine function. We solve the model by chronologically decomposing the lower level
into interacting mobility service and recharge subnetworks. Numerical experiments on the ex-
panded Nguyen-Dupuis network reveal several key insights. First, a critical charging capacity
threshold exists; operating below it forces a severe reduction in the deployable fleet and creates
localized transit deserts. Second, modeling endogenous operating costs reveals a concave profit
trajectory, demonstrating that total profit maximizes at a specific fleet size just before market
saturation. Third, optimal dynamic pricing operates within a narrow range, where peak pric-
ing acts as a steady revenue driver and off-peak pricing serves as a highly sensitive operational
buffer. These findings provide actionable strategies for coordinating fleet sizing and charging
infrastructure deployment.
1. Introduction
Sustainable cities must reduce non-renewable energy use in transportation, which accounts
for 25% of global output (Conti et al., 2016). Yet electrification alone is insufficient. Prior stud-
ies show that uncoordinated charging can substantially increase peak electricity demand, while
the environmental benefits of electric vehicles remain sensitive to the energy mix and operating
conditions (Van Vliet et al., 2011; Ma et al., 2012; Huo et al., 2015). A key sustainability
strategy is therefore to shift travel toward more efficient, renewable-oriented modes, including
shared and pooled mobility services and micromobility. However, these services remain difficult
to operate sustainably because long charging times and limited charging infrastructure raise
operating costs (Jung et al., 2014; Jung and Chow, 2019), and their performance varies across
∗Corresponding author
Email address:joseph.chow@nyu.edu(Joseph J. Y. Chow)
arXiv:2609.05449v1  [cs.GT]  3 Aug 2026

built environments, creating challenges such as the first- and last-mile problem (Chang and
Schonfeld, 1991).
In a mobility–energy ecosystem, charging demand at one time of day is driven by mobility
demand at other times, while the cost and capacity of energy provision affect mobility fares,
travelerchoices, and, inturn, energy-providerprofitability. Thisinterdependencefundamentally
changesthemathematicalstructureofthemarket: onceenergyprovidersaretreatedasstrategic
actors, the conventional two-sided market of travelers and mobility providers becomes a three-
sided market. Modeling and governing such a system therefore requires a framework that jointly
captures traveler routing, mobility service assignment, and physical energy constraints.
Existing literature does not yet provide such an integrated approach. Instead, two related
but largely parallel streams have developed. One focuses on EV fleet planning, routing, and
charging infrastructure, showing that electrification introduces additional spatiotemporal con-
straints, longer service interruptions, and stronger dependence on charging-facility availability
(Li et al., 2024). Studies on electric routing and fleet operations show that charging behavior
shapes feasible routing and service decisions (Montoya et al., 2017), and that fleet operations,
battery depletion, and charging choices must be considered jointly in electrified systems (Jung
et al., 2014; Jung and Chow, 2019; Pantelidis et al., 2022; Yi and Smart, 2021; Kullman et al.,
2022; Zhan et al., 2022). Planning studies likewise integrate transportation and power con-
siderations into charging infrastructure and fleet design (Nourinejad et al., 2016; Wang et al.,
2018; Zhang et al., 2018; Chen et al., 2020). More recent work shows that charging stations
and battery swapping may serve as complementary facilities for electrified ride-hailing fleets
(Lai and Li, 2024), and that fleet management, pricing, and energy costs are jointly shaped in
coupled transport–power planning settings (Ding et al., 2022). Together, these studies show
that charging is a core system-design component rather than a secondary operational detail.
A second stream examines mobility market design, platform pricing, operator competition,
and traveler participation. MaaS and MOD studies use assignment-game and bilevel formu-
lations to represent strategic interactions among users, operators, and platforms (Daou and
Leurent, 2024; Rasulkhani and Chow, 2019; Pantelidis et al., 2020; Liu and Chow, 2024; Yao
and Zhang, 2024; Xi et al., 2024a; Bandiera et al., 2024).
An assignment game, unlike a noncooperative game, is an assignment problem that also
determines the cost transfers between players to sufficiently incentivize them to participate in
the coalition. In a one-to-one stable matching assignment game without network effects, the
problem can be represented as a simple linear program where the dual variables can be used
to determine allocations (Shapley and Shubik, 1971). Liu and Chow (2024) showed that for
multimodal networks, such assignment games can be represented in a bilevel framework, which
can further be extended to a unique set of cost transfers when the lower level matches are
stochastically assigned with endogenous capacities (Liu et al., 2025). Yang and Chow (2026)
show that a bilevel mobility-hub design model with a lower-level link-based perturbed utility
route choice (PURC) assignment can achieve strong computational scalability. These studies
provide an important methodological foundation by endogenizing pricing, capacity allocation,
cost transfers, and traveler participation within a platform-based equilibrium. However, they
remain largely two-sided, as charging-related decisions and the strategic role of energy providers
are omitted or only indirectly represented.
Recent electrified mobility studies move closer to integration. Data-driven studies identify
the spatiotemporal distribution of charging demand from travel demand or ride-hailing activity
(Zhang et al., 2020; Li et al., 2022; Jin et al., 2025). Other work shows that charging cost in
2

electric ride-hailing depends not only on electricity price but also on waiting time, and that
these charging costs directly affect the equilibrium between service supply and demand (Chen
et al., 2024). Studies of electric autonomous MOD systems similarly emphasize that charging
demand is linked to passenger demand and shaped by both platform and government decisions
(Gao and Li, 2024). On the infrastructure and operations side, the energy sector is increasingly
modeled as an active decision maker (Ding et al., 2022; Cai et al., 2024; Zhao et al., 2025).
More broadly, Garcia et al. (2019) conceptualize eMaaS as an ecosystem of interdependent
participants, while Xi et al. (2024b) examine how EV-related incentives affect electric mobility
use under competition.
Despite this progress, the literature still lacks a unified network-based equilibrium frame-
work that jointly models mobility assignment and recharge assignment over multiple periods
with explicit strategic interactions among travelers, mobility providers, and energy providers.
We address this gap by proposing a three-sided assignment game with a bilevel framework for a
mobility–energy market with explicit time-of-day interdependencies between mobility demand
and charging demand. The upper level represents a market regulator, interpreted as either
a public agency or a private platform hosting the three groups of market participants, and
determines cost-transfer decisions to maximize market profit distributed between mobility and
energy providers. The lower level captures the equilibrium decisions of travelers, service oper-
ators, and energy providers across multiple periods. To represent the temporal link between
mobility demand and charging demand, we propose using an affine function to relate them
across periods as shown to be effective by Jin et al. (2025). Although the present model focuses
on fixed charging stations as a starting point, it provides a foundation for future extensions to
other charging technologies like mobile charging and battery swapping.
The problem is computationally challenging because, relative to earlier bilevel mobility de-
sign models such as Yang and Chow (2026), it introduces time-of-day coupling, energy-provider
decision variables, and fleet-positioning decisions associated with recharging. To address this
complexity, we retain the scalable link-based PURC formulation of Fosgerau et al. (2022), as
adopted in Yang and Chow (2026), and further decompose the lower-level equilibrium into
two interconnected subnetworks: a mobility service network for passenger movement and a
recharge service network for charging and fleet rebalancing. This decomposition preserves the
key strategic and physical interactions while keeping the model tractable for planning analysis.
We make three contributions. First, we develop a network-based bilevel framework as an
electrified mobility market assignment game that explicitly integrates mobility assignment and
recharge assignment over multiple time periods. Second, we extend the predominantly two-
sided mobility market-design literature by endogenizing energy providers within a three-sided
market. Third, we propose a scalable decomposition-based solution method and evaluate it
on an expanded Nguyen–Dupuis network to analyze both lower-level equilibrium behavior and
upper-level profit optimization.
2. Proposed model and solution method
We propose a strategic planning model assuming perfect information symmetry between
the regulator and the operators, not mechanism design. As such, the detailed mechanisms to
ensure truth-telling (i.e. incentives compatibility) are outside the scope of this study; however,
we do need to consider individual rationality (IR) of travelers and operators.
3

2.1. Network structure and model assumptions
We consider a network served by one or more MOD servicesm∈Mwith exclusive access to
one or more energy providerse∈E, regulated by a platformP. The regulator can be a public
agency or a private enterprise, or even the mobility service if it is the sole mobility service in the
platform. Other mobility services and modes are considered to be out-of-platform options. The
services operate in a cyclic operating horizon, such as a 24-hour cycle, which is partitioned into
a set of discrete time intervalsT. Each intervalt∈ Texhibits a distinct, steady-state travel
demandq t that includes users of both the platform mobility servicesqI t and out-of-platform
optionsq O t , whereq O t +q I t =q t.
2.1.1. Cyclic temporal horizon
The mobility–energy platform is represented as a multilayer network composed of two inter-
connected components: mobility service subnetworksGand recharge service subnetworks˜G, as
shown inFig. 1. This structure captures the spatial and temporal coupling between EV-based
mobility service and charging service. It is not intended to represent dynamic traffic effects such
as spillovers or FIFO conditions; rather, it provides a macroscopic steady-state representation
of time-of-day interactions.
The mobility service subnetworks, shown as blue layers inFig. 1, represent the spatial
assignment of mobility flows in each time interval under steady-state conditions. Although
each layer has its own demand pattern and cost structure, together they represent the variation
in urban mobility over the day. To model a cyclic steady-state day, the demand pattern in the
first interval,q 1, is assumed to follow that of the final interval,T. This assumption allows the
model to capture overnight capacity carryover and long-run system consistency.
Between consecutive mobility layers are recharge service subnetworks, shown as green layers
inFig. 1. These subnetworks serve two purposes: they assign charging demand spatially
to designated stations and redistribute fleet capacity as vehicles move between active service
and charging states. In this way, the network captures the temporal trade-off between service
availability and vehicle state-of-charge. The arc definitions and mathematical properties of
both subnetworks are introduced below.
Figure 1: Illustration of mobility-energy platform network structure
2.1.2. Mobility service subnetwork
We first describe the mobility service subnetworkG. Although each time layert∈ T
has different node capacities and demand levels, the underlying topology is identical across
4

all intervals.Fig. 2illustrates the detailed structure of one such layer within the broader
framework ofFig. 1.
The service network is denoted byG= (N, A), whereNis the set of service-related nodes
andAis the set of service links used to satisfy origin–destination (OD) demand. Demand is
aggregated at centroid nodes{O∪D} ⊆N. The network supports two categories of service:
the platform’s on-demand MOD services and a composite out-of-platform (OOP) option. The
OOP option is represented by the lower subgraph inFig. 2, consisting of linksAf (brown links)
between centroids.
In parallel, each MOD fleetm∈Moperates its own subnetworkG m, represented by the
upper subgraph inFig. 2. This subgraph contains mobility service nodesNm (blue nodes) and
service linksA m (solid blue links). These links describe average travel performance between
nodes rather than real-time routing outcomes, consistent with macroscopic ride-pooling network
models (Yang and Wong, 1998; Xu et al., 2021; Yang and Chow, 2026). Travelers move between
the physical demand subgraph and each MOD subgraph through access and egress links, shown
as dashed blue arrows. The access links represent the average waiting cost through a "meeting
function" (Yang et al., 2010; Liu and Chow, 2024). When multiple MOD operators compete,
each is represented by a separate service subgraph connected to the common centroids through
its own access and egress links.
To represent operational constraints such as cruising and congestion, MOD access links are
modeled as store-and-forward links with service queues. Congestion effects, including waiting
delay for vehicle pickup, are governed by the capacity of the access links. Accordingly, each
MOD operatormchooses the service capacity of its access linksl∈A + m in each intervalt,
thereby limiting inflow to the service network and capturing queueing delays caused by supply–
demand imbalance.
Figure 2: Illustration of mobility service subnetwork structure
2.1.3. Charging service subnetwork
As shown inFig. 1, the recharge service subnetwork˜Gforms the temporal interface between
two consecutive mobility service layers. Charging is modeled as a discrete transition phase
linking operations in intervaltto those in intervalt+1. This construction discretizes continuous
time while preserving the flow conservation needed for multiperiod fleet management.
The main purpose of this subnetwork is to model redistribution flow: the movement of
average vehicle presence needed to satisfy different steady-state capacity requirements across
time intervals, together with additional idle vehicles caused by charging or demand–supply
imbalance. This differs from Yang and Chow (2026), which assumes a time-invariant steady-
state fleet distribution over service nodes, and from rebalancing models that track individual
vehicle locations (Nourinejad et al., 2015; Sayarshad and Chow, 2017). Instead, the present
5

framework assumes that an operator’s steady-state fleet distribution changes over time and
must be redistributed accordingly to preserve flow capacity. The charging subnetwork therefore
defines OD pairs connecting every mobility service node in layertto every mobility service
node in layert+ 1for each operatorm∈M. These flows ensure that the average fleet capacity
assigned to each MOD nodei∈N m is properly transferred and conserved between consecutive
intervals.
Within this structure, redistribution can occur along two path types, illustrated inFig. 3.
Vehicles that require charging follow charging-based links (solid green), passing through a charg-
ing nodei∈ ˜NE ⊆ ˜Nbefore reaching their destination in layert+ 1. Vehicles that do not
need charging use fleet redistribution links (dashed purple arrows) to move directly between
service nodes across intervals. This topology includes both direct cross-period links and indirect
paths through charging infrastructure, thereby coupling spatial relocation with energy manage-
ment. Redistribution patterns can be calibrated through link weights. For example, nighttime
charging policies or redistribution limited to nearby zones can be represented by assigning high
weights to daytime charging links or to transfers toward distant service nodes.
A complete list of sets, parameters, and decision variables is provided in as follows. Key
notation is also introduced inline when first used in the model.
•T: Set of discrete time intervals representing a cyclic planning horizon.
•M: Set of Mobility-on-Demand (MOD) fleet operators.
•E: Set of energy providers/charging operators.
•N: Set of service network nodes.
• ˜N: Set of charging network nodes.
•N m: Subset of service nodes managed by operatorm.
• ˜Ne: Subset of charging station nodes managed by energy providere.
•A: Set of service network links.
• ˜A: Set of recharge network links.
•A a m: Subset of MOD access links.
• ˜Aa i: Subset of links entering charging nodei.
•S: Set of Origin-Destination (OD) pairs for travelers.
•s +, s−: Origin and destination of OD pairs∈S.
• ˜S: Set of OD pairs for fleet redistribution in the recharge network.
•˜s+,˜s−: Origin and destination of redistribution OD pair˜s∈˜S.
6

Parameters and Input Variables
•q t s: Travel demand for OD pairs∈ Sin time intervalt∈ T.
•π τ t: Propagation coefficient of the autoregression function connecting service demand in
intervalτto intervalt
•v l: Maximum physical capacity scaling factor for access linkl.
•h i: Maximum physical capacity scaling factor for nodei.
•d l: Length of linkl.
•c l: Operating cost per unit distance on linkl.
•g l: Cost per unit capacity on MOD access linkl
•c i: Cost per unit capacity at nodei.
•δ il: Node-link incidence matrix indicator (1if linklenters nodei,−1if it leaves,0
otherwise).
•V m: Total fleet size available for operatorm.
•w o: Weight between mobility service and recharge service.
•w sd: Mobility service dispersion weight.
•w uc: Traveler utility weight.
•w oc: Operator utility weight.
•w rd: Recharge dispersion weight.
•w ocr: Operator recharge utility weight.
•w rs: Recharge station utility.
Decision Variables
•p t l: Service link pricing for all linkl∈Aoperated bym∈M(Upper level) (note that
charging pricing, i.e., cost allocation between mobility provider and charging provider, is
assumed exogenous and set equal to the operating cost)
•x t s,l: Unit flow for ODs∈ {S∪˜S}on linkl∈Ain intervalt∈ T(Lower level)
•z t l: Percent of max capacity allocated for service nodel∈A m form∈Mfort∈ T
(Lower level)
•µ t i: Percent of max deployed fleet size for service nodei∈N m form∈Mfort∈ T
(Lower level)
•u t i: Percent of max capacity allocated for charging station nodei∈Ne fore∈Efort∈ T
(Lower level)
•r t,m ij : Redistribution of expected mobility service fleet (shortened as redistribution flow in
the following context) between nodeiand nodejfor operatorm. (Lower level)
7

Figure 3: Illustration of recharge service subnetwork structure
2.2. Lower level formulation
min
x,z,u,r,µ
Φ1 = ΦS +w oΦR (1a)
ΦS =
X
t∈T
" X
s∈S,l∈A
dl

wucU(x t s,l) +w sdF(x t s,l) 
+w oc
X
s∈S,l∈A
dlclqt sxt s,l +w oc
X
m∈M,l∈Aam
glvlzt l
#
(1b)
ΦR =
X
t∈T
" X
˜s∈˜S,˜l∈ ˜A
d˜l

wocr ˜U(x t ˜s,˜l) +w rdF(x t ˜s,˜l) 
+w rs
X
e∈E,i∈Ne
cihiut i,e
#
(1c)
s.t.
X
l∈A
δi,lxt s,l =



−1, i=s +,
1, i=s −,
0,otherwise,
∀s∈ S, t∈ T, i(1d)X
s∈S
xt s,lqt s ≤z t l vl,
∀l∈ Aa m, m∈ M, t∈ T(1e)
µt i=l− ≥z t l ,∀l∈ A a m, m∈ M, t∈ T(1f)
0≤z t i ≤1,∀i∈ N m, m∈ M, t∈ T(1g)
0≤µ t i ≤1 +ϵ,∀i∈ N m, m∈ M, t∈ T(1h)X
l∈Aam
vlµt i=l− ≤V m,∀m∈ M, t∈ T(1i)
Vm ≥κ
X
τ∈T
X
l∈Am
πτ t vlzτ l + X
l∈Am
vlzt+1,m l ,
8

∀m∈ M, t∈ T \ {|T |}(1j)
Vm ≥κ
X
τ∈T
X
l∈Am
πτ |T |vlzτ l + X
l∈Am
vlz1,m l ,
∀m∈ M(1k)
0≤x t s,l ≤1,∀l∈ A, s∈ S, t∈ T(1l)
vlµt i=l− = X
j∈Nm
rt,m i=l−,j,
∀l∈ Aa m, m∈ M, t∈ T(1m)X
i∈Nm
rt,m i,j=l− =v lµt+1,m j=l− ,
∀l∈ Aa m, m∈ M, t∈ T \ {|T |}(1n)X
i∈Nm
r|T |,m i,j=l− =v lµ1,m j=l−,
∀l∈ Aa m, m∈ M(1o)
qt ˜s=r t,m ˜s+,˜s−,
∀˜s∈ ˜S, m∈ M, t∈ T(1p)
rt,m ˜s+,˜s− ≥0,
∀˜s∈ ˜S, m∈ M, t∈ T(1q)
X
˜l∈ ˜A
δi,˜lxt ˜s,˜l =



−1, i= ˜s +,
1, i= ˜s −,
0,otherwise,
∀˜s∈ ˜S, t∈ T, i(1r)X
˜l∈ ˜Aa i
X
˜s∈˜S
xt ˜s,˜lqt ˜s=h iut i,e,
∀i∈ Ne, e∈E, t∈ T(1s)X
e∈E
X
i∈Ne
hiut i,e = X
m∈M
X
τ∈T
X
l∈Aam
πt,τ vlzτ i ,
∀t∈ T(1t)
The complete lower-level model encompasses both the mobility service capacity allocation,
traveler assignment, capacity redistribution, as well as charging service capacity allocation and
charging assignment. The three-sided market decision-makers collectively make simultaneous
matching decisions, and the coalitions of these matches are being stochastically chosen through
the PURC framework as a coalitional choice model. We first present the integrated formulation
for the entire lower level. The full lower-level formulation is shown inEq. 1.
2.2.1. Mobility service network subproblem
The objective functionEq. 1bminimizes the total perturbed utility, representing a weighted
aggregation of the disutility of the three-sided market coalitions of travelers, mobility operators,
9

and charging operators along with the perturbed utility term across all service intervalst. The
termU(x t s,l)denotes the link-additive traveler disutility calculated from flowx t s,l.F(x t s,l)is
a convex perturbation function capturing the dispersion effect in route choice as established
in Fosgerau et al. (2022). In this study, we use the form ofx 2 as suggested in Fosgerau
et al. (2022) for simplicity, but it can be replaced with other recommend convex functions
(e.g.,(x+ 1)ln(x+ 1)−x). The second component accounts for the mobility providers’ costs
including link operating cost and access link capacity cost. All terms are scaled by their
corresponding coefficientw uc,w sd, andw oc. These tunable parameters balance operator and
traveler disutilities, as well as the dispersion effect depicted byF(x), effectively representing a
coalition as discussed in Liu et al. (2025) and Yang and Chow (2026), but designed to capture
three sides. Since the charging costs are embodied by the mobility operator in matching with
the travelers, only one parameter is used for the subcoalition of mobility and charging providers.
Operator disutility encompasses both link operating and fixed capacity costs: link costs are the
product of unit flowxt s,l, demandq t s, link lengthd l, and unit costcl; fixed capacity costs are
derived from the decision variablezt l and the access link capacity scalervl.
The constraints ensure network physical feasibility and consistent loading.Eq. 1denforces
flow conservation for every OD pairsat each nodeiduring intervalt, using the node-link
incidence indicatorδ i,l.Eq. 1eimposes a critical access link capacity constraint, mandating
that the service flow using access linksl∈ Am does not exceed the capacity allocated by the
operator. This constraint functions as the mechanism for generating endogenous congestion
delays when demand approaches the allocated supply as shown in Liu et al. (2025) and Yang
and Chow (2026).
ConstraintsEq. 1f–1kgovern the interaction between service capacity and fleet availability.
Eq.1fdefinesµ t i asthephysicalfleetresourcesactuallydeployedtoservetheaccesslinksl∈A m
where nodeiis the sink node ofl, and it must meet or exceed the allocated service capacityzt l.
zt l captures the active fleet currently engaged in passenger service, whileµt i represents the total
fleet present in the area, including cruising, idling, or charging vehicles.Eq. 1gandEq. 1h
governs the range ofµandz.ϵis an input parameter that determines the level of excessive
volume allowable to stage at service nodes.Eq. 1iensures that the total deployed fleet for each
operatormdoes not exceed the total fleet sizeV m in any interval. Finally, the system must
maintain a sufficient buffer to account for vehicles unavailable due to charging. InEq. 1j-
1k, the first term of the Right-Hand Side (RHS) is an empirical affine function of multiple
intervals of the platform’s mobility demand to determine the charging demand. This represents
a temporal macroscopic relationship between mobility demand and charging demand that can
be empirically fitted to data.πτ t is the propagation coefficient for the interval pair(t, τ), andκ
represents the percentage of charging demand deemed unavailable for the subsequent interval.
These coefficients can be calibrated to either observed or simulated data of such dynamics. The
second term captures the total service capacity of mobility fleetmin the subsequent interval.
Eq. 1jrepresents whentis not the last interval, andEq. 1kreflects the cyclic manner whent
is the last interval. The sum of the two represents the actual fleet size that is required for the
mobility service constraints, which shall be smaller than or equal to the total deployable fleet
Vm.Eq. 1lrestricts the normalized flow variables to the valid range[0,1].
The mobility service network subproblem adopts a structure analogous to the lower-level
problem proposed in Yang and Chow (2026), which demonstrates that this formulation yields a
flow assignment model characterizing a traveler-operator coalition within the PURC framework.
Interested readers are referred to Yang and Chow (2026) for the complete mathematical proof.
10

The weightsw uc andw oc governs the relative influence of each stakeholder on the resulting
flow assignment behavior. Furthermore, the relative weight betweenwsd andw uc, woc regulates
the magnitude of the dispersion effect, as established in Fosgerau et al. (2022). These three
parameters can be calibrated using empirical data observed during each defined service interval.
Proposition 1.The mobility service network subproblem provides a standalone PURC-based
flow assignment model with a traveler-operator coalition when the link utility functionu(x)is
linear.
Proof.Let the objective function of the service subproblem be denoted asΦ1(x, z, µ, V). We
construct the LagrangianLfor the mobility service subproblem:
L(x, z, µ, V, ω, η, σ, ρ, ι, χ, υ)
= Φ1(x, z, µ, V) +
X
ωK(x) +
X
ηV(x, z)
+
X
σR(z, µ) +
X
ιB(µ, V)
+
X
χD(z, V) +
X
υP(x, µ, z)
(2)
Whereω,η,σ,ι,χ,υare the respective dual variables for the flow conservation, service
node capacity, node coefficient, total fleet size, fleet buffer, and variable bound constraints.
The Karush-Kuhn-Tucker (KKT) condition with respect tox, given by∇xL= 0, is written as:
∇xL=∇ xΦ1(x) +ω∇ xK(x) +η∇ xV(x) +υ∇ xP(x) = 0 (3)
Sincexis linearly connected with other decision variables, the first-order derivative with
respect toxdropsz, µ, Ventirely. Because the utility functionu(x)is linear, Eq. 3 implies
that the optimal flow assignmentxis determined by the marginal disutility of traversing service
network links, the difference in Lagrangian multipliers of source and sink nodes for each link,
the Lagrangian multipliers of the capacity constraintsη, and the Lagrangian multiplier of link
flow upper bounds. The Lagrangian multipliersηcan be obtained using∇zL= 0:
∇zL=∇ zΦ1(z) +η∇ zV(z) +σ∇ zR(z) +χ∇ zD(z) +υ∇ zP(z) = 0 (4)
Rearranging Eq. 4 yields:
η=− ∇zΦ1(z) +σ∇ zR(z) +χ∇ zD(z) +υ∇ zP(z) ∇zV(z) (5)
Eq. 5 represents the marginal cost of service node capacity assignment along with the
Lagrangianmultipliersσ, χ, υ, whicharenotrelatedtothedisutilityvaluesintheobjective. By
combining Eq. 3 and Eq. 5, the optimal flow is decided by the marginal disutility of link usage
from the coalition of travelers and operators, along with the marginal disutility of assigning
service node capacity from the operator side. This is in the same structure as shown in Yang
et al. (2026). This concludes the proof.
2.2.2. Recharge and redistribution network subproblem
The second component of the lower-level model is the Recharge and Redistribution Network
Subproblem. This formulation manages the transition phase between consecutive service of each
pair of intervalstandt+ 1, governing both the fleet repositioning and the allocation of charging
11

infrastructure capacity. Unlike the mobility service subproblem, where demand is exogenous
(traveler requests), the demand in this subproblem is endogenous. It is derived explicitly from
the fleet redistribution requirements determined by mobility operators to maintain service levels
while minimizing total system disutility. The formulation for the recharge and redistribution
assignment is defined by the objective functionEq. 1cand the constraintsEq. 1l–1t.
Eq. 1cpresents the objective function, which minimizes the combined disutility of fleet
movement and charging capacity establishment. Analogous toEq. 1b, the first term represents
the link-additive disutility of routing vehicles through the recharge network, wherext ˜s,˜l denotes
the flow on recharge network link˜lfor the redistribution pair˜s. The second term captures
the cost incurred by energy providers, wherezt i,e is the capacity decision variable for charging
stationimanaged by providere. The parametersw rd, wocr, wrs govern the weight between fleet
routing, charging infrastructure investment, and route dispersion effect in the recharge network.
The constraints ensure that fleet movements are physically feasible and that energy demands
are satisfied.Eq. 1m - 1ogovern the vehicle movement between mobility service node pairs in
Nm for each operatormduring the recharge interval. Here,r t,m i,j represents the redistribution
flow bridging the temporal progression between service intervaltandt+ 1.Eqs. 1m–1o
maintain fleet size consistency across time intervals by ensuring that vehicle inflows and outflows
match the deployed fleet,µt i. Specifically,Eq. 1mmandates that the total flow departing from
service nodeiequals the deployed fleet atiduring intervalt. Similarly,Eqs. 1n–1oensure
the flow entering nodejsatisfies the fleet deployment decision atjfor the subsequent interval.
Notably, these conservation constraints are governed by the deployed fleetµt i rather than the
active fleetz t l. Because the active fleet strictly reflects MOD service demand, its sum naturally
fluctuates across time intervals. The total deployed fleet, however, must remain conserved.
The gap between these two values quantifies resource redundancy, representing vehicles that
are idling due to supply-demand mismatches or mandatory charging.
Eq. 1pserves as the critical coupling constraint between the mobility service and recharge
subproblems. It defines the demandqt ˜sfor the recharge network as exactly equal to the redis-
tribution flowr t,m i,j from the mobility operator’s fleet management decisions.
Finally,Eq. 1renforces standard flow conservation within the recharge network topology,
identical in structure toEq. 1l.Eq. 1sconstrains the flow through charging stations, ensuring
thattheaggregatefleetflowusingchargingstationidoesnotexceedthecapacityh iut i,e allocated
by the energy provider. Finally,Eq. 1tenforces a system-wide energy balance, requiring
that the total allocated charging capacity across all energy providers must equal the aggregate
charging demand generated by the mobility services.
We useProposition2 andProposition3 to show the characteristics of the recharge and
redistribution network subproblem formulation.
Proposition 2.Each unique distribution ofrwith fixed ¯µ, ¯zinput to the recharge and redistri-
bution subproblem results in a standalone PURC-based flow assignment model with a operator-
energy provider coalition when the utility function˜u(x)is linear.
Proof.Let the objective function of the recharge subproblem be denoted as˜Φ1(x,u). The op-
timization problem, conditional on fixed service decisions¯µand ¯zalong a unique distribution
of ¯r, reduces to minimizing ˜Φ1 subject to the feasibility constraints. The corresponding La-
grangian ˜Lmimics the structure of the mobility service network subproblem’s LagrangianL.
This results in the optimal flow being decided by the coalition of marginal operator disutility
12

of link usage and marginal energy provider disutility of allocating charging capacities, similar
to Proposition 1. This concludes the proof.
Proposition 3.Given fixed mobility service network decision variables ¯µand ¯z, the bind-
ing constraintsEq. 1m–1pandEq. 1tensure that the resulting rebalancing flow vectorr ∗
minimizes the operator disutility within the charging network.
Proof.The recharge network demand is defined as a function of the rebalancing flowr. Specif-
ically, the charging OD demand˜ q=M(r), whereMis the incidence mapping relating re-
distribution OD pairs to flow variables. Consequently, the flow conservation constraints and
capacity constraints become implicitly dependent onr. In addition, the system-wide capacity
constraint becomes onlyzdependent. The optimality of the system therefore only depends on
variables (x,u,r) withrbeing embedded inside the Lagrangian ˜L. As a result, the binding
constraints compel the rebalancing flowralong withxanduto distribute fleet size in a manner
that minimizes the operator’s generalized disutility in the charging network. This concludes
the proof.
The recharge network subproblem is nonconvex when (x,u,r) are solved simultaneously.
This is caused by the product ofxandqinEq. 1s. This results in the combined lower level
problem becoming a nonconvex Quadratic Program with Quadratic Constraints (QPQC).
2.3. Upper-Level Formulation
The upper-level optimization problem represents the profit maximization strategy of the
MOD service providers. In this leader-follower framework, operators determine the optimal
link-based service pricingp, anticipating the equilibrium response of travelers and operator
decisions in the lower level. The formulation is shown inEq. 6.
The objective functionEq. 6amaximizes the total system profit across all time intervals
t∈ Tand operatorsm∈ M. The first and second term capture the service operation profit,
which is calculated by the total service income minus the link operating cost and capacity
allocation cost. The third term represents the charging related cost. In this way, the upper
level objective function optimizes the MOD service profit that also considers the charging
service. Welfare-based objectives can also be used for public platforms.
ConstraintsEq. 6bregulate link based service pricespt l must be less than the price capˆpl.
Eq. 6crepresents the IR constraint for the MOD operator’s budget balance, ensuring that
each operatormremains profitable (or above a minimum cost threshold for public operators)
while participating in the platform. The variablesx,z,uare determined from the lower-level
PURC assignment (Φ1), representing the optimal response on both traveler, operator, and
energy provider to the upper-level pricing and capacity decisions.
max
p
Φ0 =
X
t∈T
X
m∈M
X
s∈S
X
l∈Am
dl(pt l −c l)qt sxt s,l
−
X
t∈T
X
m∈M
X
l∈Aam
glvlzt l
−
X
t∈T
X
e∈E
X
i∈Ne
cihiut i (6a)
Subject to:
13

0≤p t l ≤ˆpl ∀l∈ Am,∀t∈ T,∀m∈ M(6b)
0≤
X
t∈T
X
s∈S
X
l∈Am
dl(pt l −c l)qt sxt s,l − X
t∈T
X
l∈Aam
glvlzt l
∀m∈ M(6c)
(x,z,u) = arg min Φ 1(p)(6d)
2.4. Proposed heuristic
2.4.1. Lower Level Lexicographic Decomposition
Figure 4: Decomposition heuristic flowchart
The nonconvexity in the lower level QPQC problem leads to excessive computational com-
plexity when facing larger-scale instances. To overcome this bottleneck, we propose a lexico-
graphic decomposition heuristic strategy to tackle the complexity of the integrated lower-level
model. This approach decouples theService Assignment Problem(Stage 1) from theRecharge
and Redistribution Problem(Stage 2), solving them sequentially as illustrated inFig. 4. The
optimal fleet deployment states determined in Stage 1 serve as binding constraints for Stage 2.
Stage 1: Mobility Service Optimization.
In the first stage, we solve the service network subproblemΦS in isolation, incorporating
additional constraints to prevent feasibility violations in the subsequent stage. The decision
variables are the passenger flowsx, service capacitiesz, and fleet deploymentµ.
We modify constraintEq. 1itoEq. 7to ensure that the total fleet size of each operatorm
remains consistent acrossT; otherwise, the redistribution flow balance inEq. 1m - 1owould
be violated when passingµto the subsequent step.
X
l∈Aam
vl ·µ t i=l− =V m ∀m∈ M, t∈ T(7)
ConstraintEq. 8is introduced to ensure that the total charging demand derived from the
regression function does not exceed the maximum allowable charging capacity.
X
m∈M
X
τ∈T
X
l∈Aam
πτ t vlzτ l ≤ X
e∈E
X
i∈Ne
vi ∀t∈ T(8)
14

Stage 2: Recharge and Redistribution Optimization.
We fixz ∗ andµ ∗ obtained from stage 1 and treat them as input parameters. In the sec-
ond stage, we optimize the recharge and redistribution network subproblemΦR. This stage
determines the redistribution flowsr, the network flow assignment˜x, and recharge capacities
u.
Eq. 9b - 9dexplicitly couple the two stages, ensuring that the redistribution flowsrmatch
the fleet inventory changes dictated by the optimal service solutionµ∗.Eq. 9eusesz ∗ to
regulate the total charging capacity.
(r∗, ˜x∗,u ∗) = arg min
r,˜x,ze
ΦR (9a)
Subject to:
Constraints (1r)−(1s)X
j∈Nm
rt,m i=l−,j =v l ·µ t∗ i=l− ∀l∈ Aa m, t∈ T(9b)
X
i∈Nm
rt,m i,j=l− =v j=l− ·µ t+1,m j=l− ∗ ∀l∈ Nm, t∈ T/|T |(9c)
X
i∈Nm
r|T |,m i,j =v j=l− ·µ 1,m j=l− ∗ ∀j∈ Nm (9d)
X
m∈M
X
τ∈T
X
l∈Aam
πt,τ vlzτ l ∗ ≤ X
e∈E
X
i∈Ne
hiut i,e ∀t∈ T(9e)
Proposition 4 shows that, under the appropriate conditions, the optimality gap of the results
relative to solvingEq. 1directly can be bounded.
Proposition 4.The sequential decomposition method yields solutions that areϵ-optimal with
respect to the integrated model inEq. 1if the marginal utility of the service network assignment
strictly exceeds that of the associated fleet recharge and redistribution assignment.
Proof.The Service Dominance Condition requires that the marginal utility (or gradient mag-
nitude) of the service network assignment strictly exceeds that of the associated fleet recharge
and redistribution assignment. Sinceµ ∗ andz ∗ are the only coupling variables shared across
the two stages, the condition is formally stated as:
 ∂ΦS ∂µ  ≫  ∂ΦR ∂µ  ,  ∂ΦS ∂z  ≫  ∂ΦR ∂z  (10)
Under this condition, the optimal deployment strategy is driven primarily by the optimization of
the service network subproblem, rendering the redistribution and recharge disutility surface flat
relative to the service disutility surface. Consequently, the optimal trajectory of the combined
objective functionΦ 1 = ΦS + ΦR aligns asymptotically with the trajectory ofΦS, justifying the
lexicographic solving approach.
The condition shown in Proposition 4 typically holds true for the majority of real-world
applications. We can also apply such condition when solving the integrated lower level model
by assigning sufficiently small values to the weight (wo) inEq. 1c.
15

The stage 2 model is still a QPQC. To further accelerate the solution speed, we introduce
the Alternating Minimization (AM) heuristic. The AM heuristics systematically avoids the
computational bottleneck by decoupling the optimization into two alternating steps. First, by
holding ˜xconstant, the charging node capacity constraintEq. 1sis strictly linearized, reducing
the optimization of the redistribution flowsrto an efficient Linear Program (LP). In this step,
the flow conservation constraintEq. 1ris not considered. Subsequently, by fixing the newly
updatedr, the model reduces to a standard Quadratic Program (QP) to solve for the flow
assignment problem. By iteratively alternating between these two strictly convex subproblems
until convergence, the proposed AM heuristics ensures tractability and rapid execution for
large-scale problems. The full heuristic is presented inAlgorithm 1.
Algorithm 1Alternating Minimization Heuristic for Stage 2
Require:Stage 1 optimal parametersµ ∗,z ∗, Toleranceϵ bcd, Max IterationsKAM.
1:Initialization:
2:Initialize routing fractions ˜x(0) uniformly (e.g.,˜x(0) ˜s˜l = 1/| ˜A˜s|).
3:Set iteration counterk←0, andΦ (0) R ← ∞.
4:whilek < K AM do
5:Step A: Redistribution Flow Optimization (r-Step)
6:Fix ˜x← ˜x(k).
7:Solve forr (k+1) andu (k+1) by minimizingΦ R subject to:
8:Fleet inventory constraints (9b) - (9d).
9:Linearized charging constraint: P(˜x(k) ·r) =u·v i.
10:Step B: Recharge Routing Optimization ( ˜x-Step)
11:Fixr←r (k+1).
12:Solve for ˜x(k+1) andu (k+1) by minimizingΦ R subject to:
13:Flow conservation (1r).
14:Linearized charging constraint: P(˜x·r(k+1)) =u·h.
15:Convergence Check:
16:Evaluate current objectiveΦ (k+1) R .
17:if|Φ (k) R −Φ (k+1) R | ≤ϵbcd then
18:break
19:end if
20:k←k+ 1
21:end while
22:returnLocal optimal variables(r ∗, ˜x∗,u ∗)←(r (k), ˜x(k),u (k)).
2.5. Bilevel model solution method
The bilevel problemEq. 6is a nonconvex function because of the complex interaction
between the upper and lower level problems, along with the nonconvexity of the lower-level
problem itself. To address this, we employ a Projected Gradient Ascent (PGA) algorithm
coupled with a Finite Difference approximation scheme. This approach treats the lower-level
problems as a "black box" that returns the system state (x,r,z) for any given price vector.
The solution procedure iterates through three key phases: gradient estimation, step size
determination, and projection. Since analytical gradients are unavailable, we estimate the
16

sensitivity of the objective function∇Φ0 numerically. To handle the strict budget constraint
(Eq. 6c), we incorporate it into the upper-level objective using a penalty method. Letγdenote
the penalty coefficient andBrepresent the magnitude of the budget violation (whereB= 0if
the constraint is satisfied). We define the augmented objective function asΦ′ 0 = Φ0 −γB.
For each pricing decisionpt, we apply a small perturbationδand solve the complete lower-
level system to observe the resulting change in profit. The partial derivative is approximated
as ∂Φ′ 0 ∂pt ≈ Φ ′ 0(p+δ)−Φ ′ 0(p) δ . The decomposition algorithm can be applied to solve the lower-level problem efficiently, allowing quick capture of the aggregate response of the user equilibrium
and fleet redistribution logic to price signals.
To ensure practical feasibility, the candidate price vector˜pis projected onto the feasible
setΩat each iteration. This projection operatorΠ Ω(·)enforces box constraints, ensuring
prices remain within a pre-defined valid range[p ,¯p], and ramp constraints, which cap the
change in price between iterations to prevent market shocks and ensure algorithmic stability.
Furthermore, to guarantee monotonic convergence to a local optimum, we employ a back-
tracking line search strategy. Instead of a fixed step size, we dynamically adjust the learning
ratew uc. A candidate step is accepted only if it satisfies the Armijo condition, which en-
sures that the improvement in profit is sufficiently proportional to the gradient magnitude:
Φ
′
0(p(k) +w ucdk)≥Φ ′ 0(p(k)) +c 1wuc∇Φ ′ 0(p(k))T dk. If the condition is not met, the step size
wuc is reduced by a decay factorβuntil the condition holds or the step becomes negligible.
To expand the solution strategy to a global optimum, we employ a Multi-Start Initialization
Strategy. The optimization algorithm is executed in parallel, each initialized with a distinct
pricing vectorp (0). This parallelized exploration of the solution space reduces the likelihood of
trapping in local optima. Upon convergence of all instances, we select runs that do not violate
budget constraints (B= 0). The solution yielding the highest system profitΦ∗ 0 is selected as
the global output. If none of the converged results meet the budget constraints, the platform
is deemed unsustainable. The complete solution procedure is summarized inAlgorithm 2.
3. Numerical experiments
We begin by validating the proposed heuristic for solving the lower-level model. Using a syn-
thetic network and simulated demand patterns, we benchmark the exact solutions against those
generated by the decomposition and AM heuristic to demonstrate the method’s computational
efficiency and accuracy. Afterwards, we conduct a series of numerical experiments to validate
the proposed bilevel eMaaS assignment framework and evaluate its analytical properties. The
current experimental setup assumes a monopolistic market structure featuring a single MOD
service provider and one charging provider operating within the platform. Extending the anal-
ysis to capture the complex competitive dynamics among multiple MSPs is reserved for future
research.
All computational instances are executed on a workstation equipped with an Intel Core i7-
13705H processor and 32 GB of RAM. For brevity in the subsequent discussions, the "recharge
and redistribution network subproblem" is referred to simply as the "recharge network sub-
problem."
3.1. Evaluation of the proposed heuristic
To validate the proposed heuristic for the lower level problem, we construct a synthetic
service network with 65 nodes and 540 links and solve only that lower level minimization
17

Algorithm 2Multi-Start Projected Gradient Ascent with Lexicographic Decomposition
Require:bounds[p ,¯p], toleranceϵrel, max iterationsK, perturbationδ, penaltyγ, number of
startsN starts
1:functionPenalizedProfit(p)
2:Solve Service Subproblem→(x ∗,z ∗,µ ∗)
3:Solve Recharge Subproblem given(z ∗,µ ∗)
→(r ∗, ˜x∗,u ∗)using Algorithm 1
4:Evaluate profitΦ 0(p)and budget violationB(p)
5:returnΦ ′ 0(p) = Φ0(p)−γmax{B(p),0}
6:end function
7:forrun= 1toN starts do in parallel
8:Initializep (0) ∼Uniform(p ,¯p),k←0
9:Φ ′ 0(p(0))←PenalizedProfit(p (0))
10:whilek < Kand not convergeddo
11:for allt∈ T,m∈ Mdo
12:p ′ ←p (k);p ′ t ←p (k) t +δ
13:∇ tΦ′ 0 ← Φ′ 0(p′)−Φ ′ 0(p(k)) δ , whereΦ ′ 0(p′) =PenalizedProfit(p ′)
14:end for
15:w uc ←1/max|∇Φ ′ 0|
16:repeat
17: ˜p←Π Ω

p(k) +w uc∇Φ′ 0 
18:EvaluateΦ ′ 0(˜p) =PenalizedProfit( ˜p)
19:ifArmijo condition failsthen
20:w uc ←βw uc
21:end if
22:untilArmijo condition holds orw uc is too small
23:p (k+1) ← ˜p,k←k+ 1
24:Check relative convergence usingϵ rel
25:end while
26:Recordp ∗ run ←p (k),Φ ∗ run ←Φ 0(p(k)), andB(p (k))
27:end for
28:Selectn= arg max run{Φ∗ run :B(p ∗ run) = 0}
29:returnp ∗ n andΦ ∗ n
18

problem. The test instance includes two time intervals with simulated demand patterns. In
addition, the recharge network contains 570 inter-layer links connecting the service layers across
the two time intervals. The data for the test case is available in project’s GitHub repository
(Yang, 2026).
All solution approaches are evaluated under the same parameter settings. In particular, the
weight parameter of recharge objective is set towo = 0.01, which satisfies the condition stated
inProposition 4. We first use Gurobi to solve the integrated lower-level model directly within
a 10-minute time limit, then tackle the same problem using the proposed decomposition and
AM heuristics.
AsshowninFig.5, theAMheuristicquicklyconvergesandreachesthestoppingtoleranceof
10−4 within 8 iterations. Most of the improvement occurs during the first three iterations, after
which the stage-2 objective value stabilizes, indicating good numerical convergence behavior.
The final results are summarized inTable 1. The decomposition and AM heuristics achieve an
objective value of 455.80, which is lower than the benchmark solution value of 455.91 achieved
within the 10-minute timeframe. Meanwhile, the proposed approach reduces the computation
time from 600 seconds to 13.2 seconds, a reduction rate of 2.2% of the runtime. These results
demonstrate that the proposed heuristic can produce near-exact solutions with substantially
improved computational efficiency.
Figure 5: Convergence of the stage-2 objective value under the AM heuristics
Table 1: Comparison between the exact solution and the proposed decomposition and AM heuristics.
Objective (ΦS + 0.01ΦR) Optimality gap Run time (second)
Exact solution via Gurobi 455.91 0.13% 600
Decomposition & AM heuristic 455.8 - 13.2
3.2. Case study to illustrative analytical insights from model
WeimplementthemodelusingtheNguyen-Dupuisnetwork. Theanalysisbeginsbyisolating
the lower-level model to assess system performance under fixed service prices and a predefined
total fleet size. We first establish a baseline scenario to explore flow assignment and capacity
allocation across the service and recharge networks. We then conduct two sensitivity analyzes:
19

the first evaluates the impact of power grid constraints by varying charging infrastructure limits,
and the second examines how the route dispersion function influences network equilibrium and
capacity allocations.
We then evaluate the complete bilevel formulation to explore the strategic interplay between
long-term total fleet sizing, dynamic service pricing, and operational routing decisions. Because
of the small size of the instance, we can solve the integrated lower-level problem directly with
Gurobi in this section to guarantee an exact solution for the lower level. The results illustrate
insights that can be gained about the trade-offs made in operating such a mobility-energy
platform.
3.2.1. Nguyen-Dupuis Network
The original Nguyen-Dupuis network comprises 13 nodes and 19 directional links. We
expand it to make the 19 links bidirectional and use it as the OOP subnetwork. To represent
the added MOD service, we add another MOD subnetwork based on nodes 2, 5, 6, 7, 8, 9, 10,
and 11, as shown in the shaded area ofFig. 6. We label the MOD service nodes as 102, 105,
106, 107, 108, 109, 110, and 111 to distinguish them from the OOP network. All MOD nodes
and links are operated by a single operator. Therefore, only one MOD subnetwork is created.
The MOD service subnetwork has a higher link service fee compared to the OOP network, while
providing significantly shorter link travel times. Specifically, the MOD links operate at a speed
of 25 miles/h compared to 15 miles/h on the base links, reflecting the premium nature of the
service. As a result, the mobility service network contains 21 nodes and 74 links.
Figure 6: Expanded Nguyen-Dupuis service network
Two charging stations are placed at Node 7 and Node 9, both operated by one provider. The
recharge network is constructed by directly linking each node pair representing a redistribution
movement between two subsequent time intervals. By adding direct links connecting each
node from intervaltto the charging node, and links between the charging node to each node
in subsequent intervalt+ 1, we create a recharge network containing 96 links and 18 nodes.
Fig. 7illustrates the links out from node 109 at intervaltto all service nodes in intervalt+ 1
as an example. We label the charge nodes as 207 and 209 respectively.
20

Figure 7: Recharge network illustration using node 109 as an example
3.2.2. Baseline scenario
We establish the baseline scenario that serves as the foundation for the subsequent numerical
experiments. All input parameters defined here are held constant throughout the sensitivity
analyses, unless explicitly treated as the variable of interest in later sections. All detailed
input settings, including the complete passenger demand matrices and system parameters, are
provided inAppendix A.
We involve three intervals (t= 1,2,3) in a cyclic manner for our numerical experiments.
Nodes 1, 2, 3, and 4 serve as both origin and destination centroids with OD demand exhibiting
distinct temporal distributions. As detailed inTable A1, demand peaks shift significantly
across intervals; for instance, traffic from Origin 1 to Destination 3 drops from 1200 int= 1to
360 int= 2, then stabilizes at 240 int= 3, requiring the system to dynamically adjust fleet
distribution.
The input parameters for the integrated mobility-energy platform model are summarized in
Table A2. The traveler disutility functionUl in the mobility service network subproblem is
modeled as a generalized cost combining travel time and link price:
Ul =β V OT·t l +p l (11)
wheret l denotes the link travel time andβV OTrepresents the traveler’s Value of Time, assumed
to be $20/h. The termpl refers to the link-specific pricing. For the MOD subnetwork, pricing
is distance based at a rate of $0.5 per unit length. In contrast, the OOP network uses a fixed
pricing structure, charging a "flat fee" of $1 per link traversal regardless of its length. We use
this "flat fee" to reflect the combined fixed and variable costs associated with modes other than
the MOD service.
The operator’s disutility ˜U˜l in the recharge network is defined by operational distances and
facility access fees:
˜U˜l =c ˜ld˜l +δ ˜l∈ ˜Aa i pstation (12)
wherec ˜l is the operational cost per unit length,d˜l is the length of the link length,pstation is the
fixed charging price, andδ˜l∈ ˜Aa i is a binary indicator that equals 1 if the link involves accessing a charging station.
Regarding the coalition weights, we set the traveler utility weightwuc to 1 and the operator
utility weightwoc to5×10 −4. Since traveler disutility is captured by unit value while operator
21

disutility is captured by aggregated cost, the operator weight must be sufficiently small to
balance the two objectives. The value of5×10−4 effectively normalizes the operator’s influence
to approximately 0.225 of the average weight relative to the traveler, prioritizing traveler choice
in the equilibrium.
In this initial baseline scenario, only one operator provides the MOD service, and the total
fleet size is 1600. Both service nodes and charging stations are subject to a capacity limit of
300 units per interval. The operational cost is set to $0.2 per unit length for MOD links and
$0.1 for recharge network links, while other links having zero cost. Charging prices are location-
dependent to test spatial sensitivity, with the station at node 7 charging $4 per usage and the
station at node 9 charging $2 per usage. Finally, the temporal propagation of charging load is
governed by the empirical multiperiod function with factors[0.05,0.1,0.2], meaning that 5%,
10%, and 20% of the service demand from previous intervals (t, t−1, t−2) propagates into the
current charging load, simulating a lag effect between mobility demand and charging demand.
Let ˜Dt andD t denote the charging and service demands, respectively.Eq. 13illustrates
the calculation. We solve the model using these input parameters and use the results as the
benchmark for further sensitivity analysis.


˜D1
˜D2
˜D3

 =


0.05 0.20 0.10
0.10 0.05 0.20
0.20 0.10 0.05




D1
D2
D3

 .(13)
We solve the base case model using both the exact approach and the proposed heuristics for
further validation. We achieve global optimality using Gurobi in just 4 seconds, demonstrating
robust computational efficiency for moderate scale instances. By comparison, implementing the
proposed decomposition and AM heuristic yields a solution with an objective value within a
0.01% margin of the global optimum in 0.3 seconds. This further demonstrates the effectiveness
of the proposed heuristic. For all subsequent analyses, the moderate scale of the test instances
is small enough to solve the integrated lower-level model directly using Gurobi.
The eMaaS system reaches an optimal operational state with a total objective value of
1,463.20. The maximum active fleet size is 1,473 vehicles. In other words, during the system’s
peak demand window, 1,473 out of the 1,600 total available vehicles are actively deployed to
satisfy passenger mobility, leaving the remainder strategically buffered for concurrent charging
or simply idling due to demand-supply mismatch.
The mobility service network exhibits significant variability in access link capacity.Fig. 8
illustrates the utilization rates of access linkszl, which are labeled by the linked service nodes.
These values reflect the active fleet size for service, not counting the vehicles that are idling,
cruising, or recharging. The access link connected to 105 emerges as a critical bottleneck,
operating at full saturation (100%) during periods 1 and 2, and remaining highly utilized
(86%) in period 3. Similarly, access links connected to node 106 and node 111 experience high
demands, reaching 100% utilization in periods 1 and 3, respectively. The access link connected
to node 102 shows a gradual load increase, starting at moderate levels and reaching full capacity
by the final period. In contrast, Node 110 is heavily underused, suggesting a potential service
redundancy at this location.
The charging infrastructure maintains high utilization without reaching saturation points.
As shown inFig. 9, station 209 consistently experiences a higher load than station 207 due to
its lower charging price. It peaks at 84% utilization in period 2, while station 207 reaches a
22

Figure 8: Heatmap of baseline case mobility service access link utilization (labeled by connected service node
ID) across time periods.
maximum of 77% in the same interval. Both stations maintain activity levels above 60% across
all periods, indicating effective load balancing and a steady need for fleet recharging.
Figure 9: Utilization Levels of Charging Stations 207 and 209 across Charging Intervals.
3.2.3. Charging station capacity sensitivity
We conduct a sensitivity analysis on charging station capacity. Holding all other parameters
constant, we vary the capacity of both charging stations from 300 to 100 units in decrements
of 10. As a result, we obtain 20 results from the created instances.
As illustrated inFig. 10, system performance shows a threshold at a charging capacity of
280 units per station. Above this threshold, the system operates stably with the objective value
remaining flat around 1,463 and the the active fleet size stays at 1,474 vehicles.This indicates
that 280 units per charging station adequately support the fleet, and further capacity increases
provide marginal benefit. Below 280 units, charging constraints restrict the active fleet, which
decreases linearly to 600 vehicles as capacity drops to 100. Consequently, the objective value
23

increases due to higher system disutility from unmet MOD demand and inefficient routing in
OOP subnetwork.
Figure 10: Sensitivity of System Objective and Maximum Fleet in Service to Charging Capacity.
Charging infrastructure constraints directly affect MOD service availability. The heatmaps
inFig. 11shows access link utilization across different periods. For visual clarity, access links
are labeled according to their corresponding service nodes. In period 1 (Fig. 11(a)), utilization
across most access links declines as charging capacity decreases, consistent with the system-wide
fleet reduction. However, access links connected to nodes 105 and 106 maintain high utilization,
indicating their importance as key service locations. This is expected due to their proximity to
origin 1 and 4, which generate significantly higher outbound flow than origins 2 and 3.
In period 2 (Fig. 11(b)), overall demand is lower. Access link connected to node 105
remains fully utilized despite capacity reductions, while utilization at other access links drops
sharply. This shows that under vehicle shortages, the system prioritizes allocating the limited
fleet to the highest-demand locations. In period 3 (Fig. 11(c)), utilization at access links
connected to nodes 106 and 110 drops to near zero as charging capacity declines. The limited
fleet consolidates to serve specific nodes, such as 102 and 111. This highlights how capacity
constraints force the system to sacrifice broad network coverage to maintain service on high-
yield locations.
3.2.4. Route dispersion effect sensitivity
We analyze the model’s sensitivity to the service dispersion weight,wsd. Keeping other
parameters constant (including a charging station capacity of 300 units), we varywsd from 0.5
to 2.0 in 0.1 increments. We obtain a total of 16 instances.
The analysis demonstrates a linear relationship between network dispersion and system
efficiency. As shown inFig. 12, the objective value increases linearly from 1,301 atw sd =
0.5to 1,758 atw sd = 2.0. This occurs because a higher dispersion weight penalizes route
concentration, forcing passenger and vehicle flows onto more diverse, less cost-effective routes,
thereby increasing total system disutility.
24

Figure 11: Access link utilization heatmap.
25

Theactivefleetsizeremainsrelativelystable, rangingfrom1,453to1,500vehicles, exhibiting
a slight upward trend. Because users choose more dispersed routes rather than aggregating on
more efficient ones, a slightly larger fleet is required to serve the network when the value of
wsd is higher. Notably, this increase in active fleet size more closely approximates a step-wise
pattern rather than a strictly continuous one. Consequently, when calibrating this parameter
with empirical data, interval fitting is sufficient and computationally more efficient than precise
point estimation.
Figure 12: Sensitivity of system objective and fleet size to mobility service dispersion weight.
The spatiotemporal utilization of service nodes (Fig. 13) further illustrates how increasing
wsd forces a broader spatial distribution of capacity allocation. In period 1 (Fig. 13(a)),
high-demand access links like the ones linking node 105 and 106 remain fully saturated (100%)
across all weights. However, utilization of other access links shift significantly: as dispersion
increases, utilization at access links connected to node 107 drops from 85% to 55%, while traffic
is diverted to alternative service locations like node 109 (increasing from 55% to 87%) and node
110 (rising from near-zero to active utilization).
In period 2 (Fig. 13(b)), access link connected to node 105 remains highly utilized, while
usage at access link connected to node 102 drops slightly from 87% to 77%. In period 3
(Fig. 13(c)), the dispersion effect ofwsd is most prominent. At low dispersion weights (wsd ≤
0.8), access link to node 105 is fully utilized (100%). Aswsd approaches 2.0, the system shifts
traffic toward underutilized locations. Consequently, the utilization of the access link to node
105 drops to 73%, while the access link to node 109 increases from 27% to 69%, and the value
for the access link entering node 110 rises from 16% to 45%.
Ultimately, the service dispersion weight serves as a key empirical parameter capturing the
diversity of route choices within the network. In practice,wsd must be estimated directly from
real-world travel data. For networks with highly heterogeneous routing behaviors, higher values
shall be fitted towsd.
26

Figure 13: Service node utilization heatmap when (a) t=1, (b) t=2, and (c) t=3.
27

3.2.5. Bilevel optimization: Sensitivity to fleet size constraints with service-wide distance-based
pricing
We focus on a long-term resource strategy by evaluating the system’s sensitivity to varying
total fleet size and their endogenously linked operational costs. By optimizing both the upper-
level pricing decisions and lower level allocation responses, we explore how the platform and
operators jointly optimize dynamic service pricing and fleet deployment to maximize profitabil-
ity. Throughout this analysis, we employ a platform-wide, time-dependent distance pricing
strategy, applying a single uniform rate across the entire MOD subnetwork for each of the three
time intervals.
The fleet size parameterVm controls the total number of vehicles available in the network.
The scale of this fleet directly impacts and operator cost coefficients. Specifically, an expanded
fleet incurs higher unit operating costs due to increased vehicle idling and deadhead cruising.
Given a known initial fleet sizeVm and operating costs parameters (cl andc i), we assume a
relationship between them for scaling cost parameters to different fleet size scenarios for input
into the model. The relationships are formulated inEq. 14andEq. 15:
cl =c l ×(V m/V )λ,∀m∈M, l∈A m (14)
ci =c i ×(V m/V )λ,∀m∈M, i∈N m (15)
These relationships follow a Cobb-Douglas functional form. Here,cl andc i represent the
baseline link travel time, link operating cost, and node operating cost, respectively, calibrated
at a baseline fleet size ofV. For this sensitivity analysis,t l corresponds to the baseline link
times defined in the previous section. We define the baseline cost parameters ascl = 0.2and
ci = 1at a reference fleet size ofV = 500. The parameterλrepresents the elasticity of the
cost function with respect to fleet size. We follow the empirical findings for modern e-hailing
systems in Zhang et al. (2019), noting that microtransit would tend to be less elastic than
ridehail, and setλ= 0.2accordingly.
We solve the bi-level model by varying the total fleet size from 500 to 1,600 vehicles in
increments of 50, keeping all other parameters constant except MOD service pricing. This
illustrates how fleet scaling influences optimal service pricing and resource allocation. For each
scenario, we update the relevant cost coefficients and optimize the model using the framework
ofAlgorithm 2. Given the moderate scale of this case study, we bypass the proposed lower-
level heuristic and directly solve the integrated lower-level model using Gurobi while preserving
the remaining algorithmic steps. Executed with 15 multi-start points and a maximum of 15
iterations, each scenario requires approximately 25 minutes of runtime.
To reflect the platform’s economics, we introduce a fleet deployment cost,cm ×V m, to the
upper-level objective function. The unit deployment cost,cm, incorporates economies of scale
by scaling with fleet size, defined by a baseline cost ofcm = 1(at a reference fleetV = 500) and
an elasticity parameter ofλ=−0.2. This formulation explicitly captures the trade-off between
fleet capital investment and the operational penalties of supply-demand mismatches.
The final results meet the budget constraints requirement.Fig. 14shows that operational
and total profit exhibit concave growth relative to total fleet size.Fig. 15illustrates the
corresponding supply-demand dynamics by comparing total fleet size with active fleet size.
The gap between total and active fleet size widens significantly above 800 vehicles. Below this
threshold, over 93% of the fleet operates during peak periods, indicating minimal fleet idling
28

due to charging. Because passenger demand is fully met at 750 vehicles, adding vehicles beyond
this level causes oversupply and sharply reduces fleet utilization.
Insupply-constrainedscenarios(capacitybelow800), eachadditionalvehiclecapturesunmet
demand and increases revenue. Beyond 1,000 vehicles, the marginal benefit of adding vehicles
diminishes. Platform profit plateaus between 650 and 750 vehicles, which remains entirely
within the supply-constrained scenario. Total profit peaks at approximately $55,800 before
declining steadily as fleet size increases. This demonstrates that with endogenous operating
costs, the platform maximizes profitability before market supply saturates. Because profit
peaks across a fleet size range rather than at a single point, operators have strategic flexibility
in fleet deployment, provided they avoid oversupply.
Remark1. There exists an optimal fleet size for mobility providers to maximize profit in an
mobility-energy market when considering operating costs as a function of fleet size, serving as
a critical threshold between under-supplied and over-supplied scenarios in fleet size.
Figure 14: Comparison of Operator Profit and True Profit under varying Fleet Size.
Figure 15: Fleet Utilization Dynamics: Fleet Size vs. Active Service Size.
Fig. 16illustrates the optimal time-dependent pricing strategy across varying fleet capaci-
ties. This dynamic pricing mechanism manages the transition from supply scarcity to oversup-
ply. Under severe constraints (e.g., 500 vehicles), prices peak to ration the limited fleet. As fleet
29

size increases, the platform lowers peak-hour prices to ensure new vehicles are utilized, thereby
increasing total profit. Upon reaching market saturation, the pricing structure stabilizes.
Remark2. The optimal pricing trends across time periods may fluctuate under under-supplied
fleet sizes and exhibit steady trends under over-supplied fleet sizes.
This insight suggests that for steady pricing planning, it is more reliable to risk over-supply
than under-supply in fleet size.
Figure 16: Optimal Dynamic Pricing Strategy per Time Period.
Peak-hour prices (periods 1 and 3) decrease nearly monotonically before stabilizing in the
oversupply regime. However, off-peak pricing (period 2) fluctuates before reaching stability,
indicating high sensitivity to fleet transitions. During period 2, pricing functions as a sec-
ondary buffer to manage residual supply, network rebalancing, and charging demand, rather
than driving primary profit. Thus, the system prioritizes peak-period demand capture while
leveraging off-peak pricing to maintain operational equilibrium. Despite these dynamic adjust-
ments, optimal prices remain confined between $0.95 and $1.11, representing a variance of less
than 17%. This narrow range indicates high price elasticity of demand; aggressive price surging
would significantly reduce ridership and revenue. Consequently, maximizing vehicle utilization
and trip volume is more critical to profitability than aggressive pricing.
Remark3. With under-supplied fleet sizes, prices in high-demand periods follow a steady trajec-
tory while low-demand prices fluctuate to accommodate residual supply and system transition.
This result suggests that more attention needs to be paid to the optimal pricing in low-
demand periods because they are less predictable.
3.3. Bilevel optimization: heterogeneous MOD fleets
We expand the scenario to convert the single MOD fleet into two heterogeneous fleets partic-
ipating in the platform. All final results meet the budget constraints requirement. As illustrated
inFig. 17, the fleets cover distinct regions with an overlapping service area. Operator 1 (blue
region) manages a fleet of 700 vehicles across 6 service nodes, while Operator 2 (orange region)
operates 300 vehicles across 4 service nodes. Their service areas overlap at nodes 6 and 9 in the
base OOP network. Both fleets adhere to the cost scaling rules defined inEq. 14andEq. 15,
applying the same elasticity (λ= 0.2) and reference fleet size (V= 500). The link attributes
30

for both MOD subnetworks and the passenger demand patterns remain identical to the baseline
case.
For the subsequent analyzes, we evaluate two dynamic pricing strategies. The first is an
operator-specific distance-based pricing strategy, where each operator independently optimizes
its fee in each time period. The second is a platform-wide distance-based strategy, which
enforces a single, unified per-distance fee across both fleets in each period serving as a bundled
fare.
Figure 17: Service network with two MOD service providers.
Table 2summarizes the two pricing strategies used in the two-fleet scenario and the results
from the previous case study with a total fleet size of 1000. The single-fleet case yields the
highest profit compared to both profits under the two-fleet scenarios Relative to the single-fleet
benchmark, operator-specific pricing with a two-fleet configuration decreases profit by 4.16%,
and profit further decreases by 5.14% when platform-wide pricing is enforced.
In the two-fleet setting, operator-wide pricing strictly dominates platform-wide pricing from
a revenue maximization perspective. Profit increases from $52,857.06 to $53,404.41, while the
maximum active fleet size falls from 898 to 708, a reduction of 190 vehicles (21.2%). When
the pricing rule varies across operators, the system can internalize differences in effective ca-
pacity allocations at the operator-level. The optimal price profiles are consistent with this
interpretation. Under operator-wide pricing, operator 2 charges more than operator 1 in all
three periods. This pattern indicates that the optimal pricing rule differentiates systematically
across operators. In contrast, the platform-wide rule compresses cross-operator variation into
a single average price.
When vehicles are pooled, capacity can be allocated more effectively. The optimal prices
under the single-fleet scenario are lower than those under the two-fleet scenarios while obtaining
higher total profit. This is mainly due to the reduced capacity allocation cost. Under the two-
fleet scenarios, travelers need to switch between operators when making their trips, leading to
additional capacity required at the overlapping area. Pooling reduces the inefficiencies created
by operator boundaries and allows the system to attain a higher-profit allocation with only a
modest peak fleet requirement.
Remark4. The proposed model captures the inefficiency of mobility-energy markets with multiple
fleet operators and corresponding operating costs of each individual fleet. When bundling fares,
the combined fleet size increases to accommodate the common fare used by the platform.
31

Table 2: Comparison of outcomes under different fleet and pricing structures
Two fleets Single fleet
Metric Detail Operator-Specific pricing Platform-wide pricing Pricing
Profit ($) – 53404.41 52857.06 55721.60
Price ($)
Period 1 Operator 1: 1.07; Operator 2: 1.28 1.10 0.96
Period 2 Operator 1: 1.03; Operator 2: 1.27 1.08 1.02
Period 3 Operator 1: 1.06; Operator 2: 1.34 1.03 1.03
Maximum active
fleet size – 708 898 714
4. Discussion and Conclusion
The transition to mobility-energy markets shifts urban transportation from a two-sided mar-
ket to a three-sided ecosystem comprising travelers, mobility providers, and energy providers.
This paper proposes a bilevel assignment game to count the additional interdependencies be-
tween mobility demand and energy infrastructure. Using a link-based PURC framework, the
modelachieveshigh computationalefficiencyandeffectivelymodels thetemporallag ofcharging
demand, enabling scalable, multi-period optimization of fleet distribution, capacity allocation,
and dynamic pricing. Using an expanded Nguyen–Dupuis network, the case study shows why
mobility operations and energy constraints should be modeled together rather than as separate
planning layers: as service demand varies across time, charging demand propagates across pe-
riods, and the platform’s strategic decisions must balance traveler utility, operator cost, and
infrastructure capacity simultaneously. The case study demonstrates the practical value of the
proposed framework as both an operational analysis tool and a long-term planning instrument.
At the operational level, the model identifies clear bottlenecks in specific MOD access links
while pinpointing underused locations. At the same time, both charging stations remain heav-
ily used without becoming fully saturated, with the cheaper station attracting consistently
higher load. These patterns show that even when total fleet can meet the required demand,
performance is still constrained by localized service-node pressure and the spatial distribu-
tion of charging demand. In other words, fleet adequacy alone does not guarantee operational
efficiency; access capacity and charging resource differences also shape equilibrium outcomes.
At the strategic level, the model shows that profitability is maximized not by only expanding
fleet size, but by sizing the fleet near the upper bound of the supply-constrained scenario. As
fleet size grows, additional vehicles initially improve demand capture and raise revenue, but
the benefit diminishes once demand is fully served. Oversupply widens the gap between total
and active fleet, increases idle and repositioning burdens, and reduces utilization, causing total
profit to flatten and then decline. Therefore, platform planners should target high service
utilization before saturation rather than pursue fleet expansion beyond the point of effective
demand absorption.
Optimal prices vary with fleet availability and demand conditions, but remain within a
relatively narrow band, indicating that the system is sensitive to price increases and that
sharp surges would likely suppress ridership more than they would improve profitability. Prices
during high-demand periods decline steadily as the fleet expands, while low-demand prices
32

fluctuate more in response to transitional conditions, residual supply, and charging needs. This
implies that in integrated systems, pricing should be interpreted as a tool for coordinating
utilization across time. In practice, platform performance depends more on maintaining vehicle
productivity and trip volume than on imposing high markups.
Methodologically, the case study also supports the computational efficiency of the frame-
work. For the moderate-size instance, the integrated lower-level problem can be solved di-
rectly to global optimality using commercial solvers, while the proposed decomposition and
AM heuristic achieves a near-optimal solution with negligible error and substantially shorter
runtime. This suggests that the proposed heuristic has strong potential for larger instances.
Several limitations should be acknowledged. First, the current model does not capture
non-linear service-charging relationships. Second, the framework does not include the dynamic
part of the power grid, such as localized voltage stability and time based electricity pricing
fluctuations. Integrating these smart-grid constraints into the charging subproblem would pro-
vide a more complete view of the three-sided mobility-energy ecosystem. Furthermore, future
models could incorporate heterogeneous energy providers with distinct cost structures and tech-
nological capabilities. This inclusion would reflect the growing complexity of modern charging
infrastructure, accommodating varying charging speeds and emerging options such as Charging-
as-a-Service (CaaS) networks with more explicit charging provider behaviors like delivery fleet
allocations and pricing decisions.
Acknowledgment
The authors are grateful for funding support from the U.S. National Science Foundation,
grant number CMMI-2423908.
References
Bandiera, C., Connors, R. D., and Viti, F. (2024). Mobility service providers’ interacting strate-
gies under multi-modal equilibrium.Transportation Research Part C: Emerging Technologies,
168:104766.
Cai, Z., Li, C., Mo, D., Xu, S., Chen, X. M., and Lee, D.-H. (2024). Optimizing consolidated
shared charging and electric ride-sourcing services.Transportation Research Part E: Logistics
and Transportation Review, 184:103484.
Chang, S. K. and Schonfeld, P. M. (1991). Multiple period optimization of bus transit systems.
Transportation Research Part B: Methodological, 25(6):453–478.
Chen, R., Qian, X., Miao, L., and Ukkusuri, S. V. (2020). Optimal charging facility location
and capacity for electric vehicles considering route choice and charging time equilibrium.
Computers & Operations Research, 113:104776.
Chen, X., Lei, Z., and Ukkusuri, S. V. (2024). Modeling the influence of charging cost on electric
ride-hailing vehicles.Transportation Research Part C: Emerging Technologies, 160:104514.
Conti, J., Holtberg, P., Diefenderfer, J., LaRose, A., Turnure, J. T., and Westfall, L. (2016).
International energy outlook 2016 with projections to 2040. Technical report, USDOE Energy
Information Administration (EIA), Washington, DC (United States ....
33

Daou, S.andLeurent, F.(2024). Modellingmobilityasaservice: Aliteraturereview.Economics
of Transportation, 39:100368.
Ding, Y., Li, S., and Jian, S. (2022). Optimal pricing and fleet management for shared electric
vehicle in coupled power and transport networks.Transportation Research Part C: Emerging
Technologies, 141:103727.
Fosgerau, M., Paulsen, M., and Rasmussen, T. K. (2022). A perturbed utility route choice
model.Transportation Research Part C: Emerging Technologies, 136:103514.
Gao, J. and Li, S. (2024). Charging autonomous electric vehicle fleet for mobility-on-demand
services: Plug in or swap out?Transportation Research Part C: Emerging Technologies,
158:104457.
Garcia, J. R. R., Lenz, G., Haveman, S. P., and Bonnema, G. M. (2019). State of the art of
electric mobility as a service (emaas): an overview of ecosystems and system architectures.
In32nd International Electric Vehicle Symposium 2019: A World of E-motion.
Huo, H., Cai, H., Zhang, Q., Liu, F., and He, K. (2015). Life-cycle assessment of greenhouse gas
and air emissions of electric vehicles: A comparison between china and the us.Atmospheric
Environment, 108:107–116.
Jin, Z., Sun, X., Xu, Z., and Tu, H. (2025). A data-driven approach to uncovering the charging
demand of electrified ride-hailing services.Transportation Research Part D: Transport and
Environment, 139:104599.
Jung, J. and Chow, J. Y. (2019). Effects of charging infrastructure and non-electric taxi
competition on electric taxi adoption incentives in new york city.Transportation Research
Record, 2673(4):262–274.
Jung, J., Chow, J. Y., Jayakrishnan, R., and Park, J. Y. (2014). Stochastic dynamic itinerary
interception refueling location problem with queue delay for electric taxi charging stations.
Transportation Research Part C: Emerging Technologies, 40:123–142.
Kullman, N. D., Cousineau, M., Goodson, J. C., and Mendoza, J. E. (2022). Dynamic ride-
hailing with electric vehicles.Transportation Science, 56(3):775–794.
Lai, Z. and Li, S. (2024). Towards a multimodal charging network: Joint planning of charg-
ing stations and battery swapping stations for electrified ride-hailing fleets.Transportation
Research Part B: Methodological, 183:102928.
Li, M., Wang, Y., Peng, P., and Chen, Z. (2024). Toward efficient smart management: A
review of modeling and optimization approaches in electric vehicle-transportation network-
grid integration.Green Energy and Intelligent Transportation, 3(6):100181.
Li, Y., Su, S., Liu, B., Yamashita, K., Li, Y., and Du, L. (2022). Trajectory-driven planning of
electric taxi charging stations based on cumulative prospect theory.Sustainable Cities and
Society, 86:104125.
34

Liu, B. and Chow, J. Y. J. (2024). On-demand mobility-as-a-service platform assignment
games with guaranteed stable outcomes.Transportation Research Part B: Methodological,
188:103060.
Liu, B., Watling, D., and Chow, J. Y. J. (2025). Stochastic assignment games for mobility-as-
a-service markets.arXiv preprint arXiv:2512.19328.
Ma, X., Lei, W., Andréasson, I., and Chen, H. (2012). An evaluation of microscopic emission
models for traffic pollution simulation using on-board measurement.Environmental Modeling
& Assessment, 17(4):375–387.
Montoya, A., Guéret, C., Mendoza, J. E., and Villegas, J. G. (2017). The electric vehicle routing
problem with nonlinear charging function.Transportation Research Part B: Methodological,
103:87–110.
Nourinejad, M., Chow, J. Y., and Roorda, M. J. (2016). Equilibrium scheduling of vehicle-to-
grid technology using activity based modelling.Transportation Research Part C: Emerging
Technologies, 65:79–96.
Nourinejad, M., Zhu, S., Bahrami, S., and Roorda, M. J. (2015). Vehicle relocation and staff
rebalancing in one-way carsharing systems.Transportation Research Part E: Logistics and
Transportation Review, 81:98–113.
Pantelidis, T. P., Chow, J. Y. J., and Rasulkhani, S. (2020). A many-to-many assignment
game and stable outcome algorithm to evaluate collaborative mobility-as-a-service platforms.
Transportation Research Part B: Methodological, 140:79–100.
Pantelidis, T. P., Li, L., Ma, T.-Y., Chow, J. Y., and Jabari, S. E. G. (2022). A node-
charge graph-based online carshare rebalancing policy with capacitated electric charging.
Transportation Science, 56(3):654–676.
Rasulkhani, S. and Chow, J. Y. (2019). Route-cost-assignment with joint user and operator
behavior as a many-to-one stable matching assignment game.Transportation Research Part
B: Methodological, 124:60–81.
Sayarshad, H. R. and Chow, J. Y. (2017). Non-myopic relocation of idle mobility-on-demand
vehicles as a dynamic location-allocation-queueing problem.Transportation Research Part
E: Logistics and Transportation Review, 106:60–77.
Shapley, L. S. and Shubik, M. (1971). The assignment game i: The core.International Journal
of game theory, 1(1):111–130.
Van Vliet, O., Brouwer, A. S., Kuramochi, T., van Den Broek, M., and Faaij, A. (2011). Energy
use, cost and co2 emissions of electric cars.Journal of power sources, 196(4):2298–2310.
Wang, X., Shahidehpour, M., Jiang, C., and Li, Z. (2018). Coordinated planning strategy for
electric vehicle charging stations and coupled traffic-electric networks.IEEE Transactions
on Power Systems, 34(1):268–279.
35

Xi, H., Aussel, D., Liu, W., Waller, S. T., and Rey, D. (2024a). Single-leader multi-follower
games for the regulation of two-sided mobility-as-a-service markets.European Journal of
Operational Research, 317(3):718–736.
Xi, H., Li, M., Hensher, D. A., Xie, C., Gu, Z., and Zheng, Y. (2024b). Strategizing sus-
tainability and profitability in electric mobility-as-a-service (e-maas) ecosystems with carbon
incentives: A multi-leader multi-follower game.Transportation Research Part C: Emerging
Technologies, 166:104758.
Xu, Z., Chen, Z., Yin, Y., and Ye, J. (2021). Equilibrium analysis of urban traffic networks
with ride-sourcing services.Transportation science, 55(6):1260–1279.
Yang, H. (2026). Three-sided mobility-energy market design as a multiperiod stochastic assign-
ment game.
Yang, H. and Chow, J. Y. J. (2026). Bilevel subsidy-enabled mobility hub network design
with perturbed utility coalitional choice-based assignment.Transportation Research Part A:
Policy and Practice, 208 (SI:ISTTT2026):104972.
Yang, H., Leung, C. W., Wong, S. C., and Bell, M. G. (2010). Equilibria of bilateral taxi–
customer searching and meeting on networks.Transportation Research Part B: Methodolog-
ical, 44(8-9):1067–1083.
Yang, H. and Wong, S. C. (1998). A network model of urban taxi services.Transportation
Research Part B: Methodological, 32(4):235–246.
Yao, R. and Zhang, K. (2024). Design an intermediary mobility-as-a-service (maas) platform
using many-to-many stable matching framework.Transportation Research Part B: Method-
ological, 189:102991.
Yi, Z. and Smart, J. G. (2021). A framework for integrated dispatching and charging manage-
ment of an autonomous electric vehicle ride-hailing fleet.Transportation Research Part D:
Transport and Environment, 95:102822.
Zhan, X., Szeto, W. Y., and Chen, X. M. (2022). A simulation–optimization framework for a
dynamic electric ride-hailing sharing problem with a novel charging strategy.Transportation
Research Part E: Logistics and Transportation Review, 159:102615.
Zhang, H., Hu, Z., Xu, Z., and Song, Y. (2018). Optimal planning of plug-in electric vehicle
charging station with service level constraint.Energy, 142:342–353.
Zhang, H., Sheppard, C. J. R., Lipman, T. E., Zeng, T., and Moura, S. J. (2020). Charging
infrastructure demands of shared-use autonomous electric vehicles in urban areas.Trans-
portation Research Part D: Transport and Environment, 78:102210.
Zhang, K., Chen, H., Yao, S., Xu, L., Ge, J., Liu, X., and Nie, M. (2019). An efficiency paradox
of uberization.Available at SSRN 3462912.
Zhao, M., Li, B., Zhang, W., and Xu, Z. (2025). Charging station operation strategies for the
ride-hailing platform with new energy vehicles: Independence, cooperation or registration.
IEEE Transactions on Engineering Management, 72:3094–3108.
36

Appendix A
Table A1: Passenger Demand (qt s) per OD Pair and Time Period
Time (t) Origin (O) Destination (D) Demand
1 1 2 600
1 1 3 1200
1 4 2 900
1 4 3 300
1 2 1 120
1 3 1 240
1 2 4 180
1 3 4 60
2 1 2 180
2 1 3 360
2 4 2 270
2 4 3 90
2 2 1 180
2 3 1 360
2 2 4 270
2 3 4 90
3 1 2 120
3 1 3 240
3 4 2 180
3 4 3 60
3 2 1 600
3 3 1 1200
3 2 4 900
3 3 4 300
Table A2: Sets, Parameters, and Variables of the Integrated eMaaS Model
Input element V alue
Service node capacity limit 300
Charging capacity limit 300
Total fleet size 1600
Operational cost per unit length on MOD link $0.2/mile
Travel time on base link 15 miles/h
Travel time on MOD link 25 miles/h
Continued on next page
37

Input element V alue
Traveler value of time (VOT) $20/h
Service price per unit length on MOD link $0.5/mile
Fixed link price per link usage in OOP network $1
Operator cost per unit length on recharge network link $0.1/mile
Recharge price per usage on node 207 $4
Recharge price per usage on node 209 $2
Unavailable fleet buffer ratio 0.2
Temporal propagation factor from service demand to charging load [0.05, 0.1, 0.2]
Overall weight between service and recharge disutility 0.01
Service dispersion weight 1
Traveler utility weight 1
Operator utility weight 5×10 −4
Recharge dispersion weight 2
Operator recharge utility weight 1
Recharge station utility weight 10−3
38
