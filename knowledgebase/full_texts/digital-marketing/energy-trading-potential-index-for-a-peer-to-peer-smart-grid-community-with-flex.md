---
title: Energy Trading Potential Index for a Peer-to-Peer Smart Grid Community with Flexible Prosumer Role
  Switching
url: https://arxiv.org/abs/2606.22087
category: digital-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Zain Imran
- Sana Humayun
- Muhammad Shahzaib Saleem
- Naveed Ul Hassan
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.22087
pages: 10
chars: 39465
fetched_at: '2026-11-08T13:08:40+00:00'
kb_version: 1
---

# Energy Trading Potential Index for a Peer-to-Peer Smart Grid Community with Flexible Prosumer Role Switching

Energy Trading Potential Index for a Peer-to-Peer
Smart Grid Community with Flexible Prosumer
Role Switching
Zain Imran, Sana Humayun, Muhammad Shahzaib Saleem, Naveed Ul Hassan
Lahore University of Management Sciences (LUMS), Lahore, Pakistan 54792
Emails: zain.imran@lums.edu.pk, 26100273@lums.edu.pk, muhammad.shahzaib@lums.edu.pk, naveed.hassan@lums.edu.pk
Abstract—In many electricity markets, declining feed-in tariffs
have made grid export increasingly unattractive for residential
solar prosumers, while retail electricity prices remain high. Peer-
to-peer (P2P) energy trading offers a direct alternative, but it
requires a dedicated infrastructure layer for real-time bilateral
matching, automated settlement, and tamper-proof transaction
records, for which blockchain is widely proposed. Deploying such
infrastructure must be economically justified by the community’s
actual trading potential. A critical and underexplored question
is whether trading potential survives as communities become
prosumer-heavy, since under fixed role assignment all households
eventually end up on the supply side with no buyers remaining.
This paper addresses these gaps by proposing the Energy Trading
Potential Index (ETPI), a normalized data-driven metric that
quantifies the structural impact of flexible role switching on
community-level trading potential, where prosumers dynamically
join the buyer side whenever they are in energy deficit. The P2P
market is modeled as a generalized bipartite graph and pairwise
interaction scores aggregated over trading rounds compute the
ETPI in [0, 1]. Simulation results using the PRECON residential
dataset and NREL PVWatts solar profiles show that for the (1:9)
prosumer-heavy mix, the flexible policy achieves an ETPI of 0.61
versus only 0.15 under the static policy, a fourfold improvement
that the static model entirely misses. The ETPI framework serves
as a lifecycle decision-support tool for evaluating and monitoring
P2P energy trading infrastructure.
Index Terms—Peer-to-peer energy trading, Energy Trading Po-
tential Index, flexible role switching, bipartite graph, blockchain,
prosumer, ETPI, smart grid.
I. INTRODUCTION
Energy systems worldwide are undergoing a fundamental
structural shift. The rapid decline in the cost of rooftop
solar photovoltaic (PV) panels has made distributed energy
generation economically accessible to ordinary households,
transforming passive consumers intoprosumers, which are
entities that both produce and consume electrical energy [1],
[2]. In many electricity markets, feed-in tariffs for residential
solar export have declined significantly, with global data
showing that feed-in tariffs and premiums have dropped from
being the dominant procurement mechanism to representing
just 10% of renewable energy growth [3]. This growing
spread between buyback rates and retail electricity prices
makes selling surplus energy back to the grid increasingly
unattractive for prosumers. Peer-to-peer (P2P) energy trading
offers a direct alternative, enabling surplus-holding prosumers
to trade directly with energy-deficient neighbors at mutually
beneficial prices. Unlike net metering, P2P trading requires
a dedicated infrastructure layer capable of real-time bilateral
matching, automated settlement without a utility intermediary,
and tamper-proof transaction records [4].
Blockchain technology is widely proposed to deliver these
infrastructure properties through distributed consensus, cryp-
tographic data integrity, and automated smart-contract set-
tlement [5]–[11]. Despite these advantages, blockchain car-
ries substantial computational and operational overhead, and
that overhead can exceed the benefits in communities where
trading activity is low [12]. Advanced P2P infrastructure
should therefore only be deployed where trading potential is
sufficiently high to justify the cost — yet the literature offers
no principled, data-driven metric for making that determina-
tion. Works demonstrating blockchain-based P2P systems [7]–
[10] uniformly assume the community is already suitable for
trading, leaving the prior question ofwhetherit is suitable
entirely unanswered. Assessments of trading potential in the
residential sector have largely been confined to technology
and tariff availability scenarios [13], without accounting for
the structural composition of the community itself. Meanwhile,
the broader P2P trading literature has examined market designs
[2], [4], [14], game-theoretic pricing among prosumers [15],
[16], and grid-level constraints [17], yet none of these works
treats community readiness as a prerequisite for infrastructure
deployment. A closely related gap concerns prosumer role
flexibility. In practice, a prosumer’s role as buyer or seller
changes dynamically each round according to its instantaneous
net energy balance [14], [15], [18], yet no prior work has quan-
tified how much trading potential is unlocked or suppressed
by the role-assignment policy. Bipartite matching frameworks
[19] similarly treat role assignment as a given rather than
a design variable, overlooking how policy choices shape the
aggregate supply-demand structure of the community.
This paper addresses these gaps by proposing the Energy
Trading Potential Index (ETPI), a normalized data-driven
metric that quantifies the structural impact of flexible role
switching on community-level P2P trading potential. The P2P
market is modeled as a generalized bipartite graph, with edge
weights derived from pairwise interaction scores combining
price compatibility, demand-supply balance, and communi-
cation link reliability. The aggregate of all edge weights
gives the Energy Trading Potential (ETP), normalized into the
arXiv:2606.22087v1  [cs.CY]  20 Jun 2026

ETPI in[0,1]. Central to the framework is aflexible role-
switching policy, under which a prosumer’s market role is
determined dynamically each round by its instantaneous net
energy balance, in contrast to astatic policythat permanently
fixes prosumers on the supplier side. The ETPI can be seeded
from historical consumption and generation data before de-
ployment and continuously updated as real trading interac-
tions accumulate, evolving from a pre-deployment estimate
into a live monitoring instrument that tracks whether trading
potential justifies sustained infrastructure costs over the system
lifecycle.
The framework is validated through one-year simulations
using real residential consumption data from the PRECON
dataset [20] and NREL PVWatts solar profiles across ten
consumer-to-prosumer mix configurations. Under the static
policy, the balanced mix of five consumers and five prosumers
(5:5) yields the highest ETPI of 0.42, while prosumer-heavy
mixes score poorly due to the absence of buyer-side pro-
sumers. Under the flexible policy, the mix of one consumer
and nine prosumers (1:9) yields the best ETPI of 0.61,
compared to only 0.15 for the same mix under the static policy.
This fourfold improvement shows that communities with high
solar penetration retain substantial trading potential when role
flexibility is accounted for, directly answering whether trading
activity collapses as neighborhoods become prosumer-heavy.
The ETPI thus provides a principled pre-deployment signal
for whether a community’s trading activity justifies advanced
P2P infrastructure investment. Sensitivity analysis further re-
veals that ETP is non-monotonically related to PV capacity
in prosumer-heavy communities, meaning that maximizing
installed solar capacity does not necessarily maximize trading
potential.
The remainder of the paper is organized as follows. Sec-
tion II describes the system model. Section III describes
the interaction model. Section IV develops the flexible role-
switching ETPI. Section V formulates the static policy as a
special case and compares it to the flexible model. Section VI
presents and discusses the simulation methodology and results.
Section VII concludes the paper.
II. SYSTEMMODEL
A. Community Structure
We consider a P2P energy trading community ofNresi-
dential households divided into two groups. LetN C denote
the number offixed consumers, which are households with
no local generation capability that always participate in the
market as buyers. LetN P denote the number ofprosumers,
which are households equipped with rooftop solar PV systems
that can potentially supply surplus energy to others. We have
NC +N P =N. No energy storage is assumed in the system.
Any consumer demand not fulfilled through P2P trading is met
by drawing from the utility grid at the prevailing retail tariff.
We define thecommunity mixas the tuple(N C :N P ), which
characterizes the composition of the community. A perfectly
balanced mix hasN C =N P , while skewed mixes reflect a
dominance of one group over the other. The community mix
governs the structure of the trading graph and has a significant
impact on the ETPI, as demonstrated through analysis and
simulation in the following sections.
B. Trading Rounds
The trading horizon is divided into discretetrading rounds
indexed byr, each spanning one hour. The market operates
only during daylight hours when solar generation is available.
Each prosumerP j is equipped with a solar PV system of
fixed rated capacity. In roundr, its gross solar generation is
gr j (kWh) and household demand isd r j (kWh), yielding anet
energy balance:
sr j =g r j −d r j (1)
Ifs r j >0, the prosumer holds a surplus and participates as
a supplier. Ifs r j ≤0, the prosumer is in deficit and joins the
demand side. This distinction underlies the flexible and static
policies described in Sections IV and V.
In each roundr, consumerC i submits abid priceb r i
(PKR/kWh) anddemand ˜dr i (kWh). ProsumerP j, when
sr j >0, submits anoffer priceo r j (PKR/kWh) andsurplus
energys r j (kWh). On the other hand, a prosumerP k, when
sr k <0submits abid priceb r k (PKR/kWh) anddemand ˜dr k (kWh) like a consumer. A complete bipartite graph is
formed each round as shown in Figure 1, with consumers
(including deficit prosumers) on the left and surplus prosumers
on the right. Each edge carries a label of+1,0, or−1
reflecting the outcome of the pairwise interaction. A label
of+1denotes strong trading potential from favorable price
alignment, sufficient surplus, and reliable links. A label of−1
denotes a non-viable trade due to price mismatch, insufficient
surplus, or poor link reliability. A label of0marks a neutral
pair at the margin of viability.
III. INTERACTIONMODEL ANDEDGEWEIGHT
COMPUTATION
The core of the ETPI framework is a pairwise interaction
model that evaluates, for every potential consumer-supplier
pair in every trading round, the feasibility and quality of a
trade. The edge labels+1,0, and−1introduced in Section II
correspond to the Positive, Neutral, and Negative sentiment
categories defined formally in this section. We identify three
key trading factors that govern this quality, combine them
into an interaction function, and accumulate classification
outcomes over time to compute edge weights.
A. Trading Factors
Price Compatibility(W r ij): A trade between consumer
Ci and supplierP j in roundris price-feasible only if the
consumer is willing to pay at least as much as the supplier
demands. We define the price compatibility factor as
W r ij =b r i −o r j (2)
A trade is price-feasible only ifW r ij ≥0. The magnitude
ofW r ij captures the degree of price alignment or mismatch
between the pair. Whether positive or negative, the value is

Fig. 1. Set of all possible pairs for (5:5) mix under both flexible and static policy. Only 3 of the 5 prosumers have surplus energy in the example round.
Blue edges represent consumer-prosumer pairs (T r ij), whereas red edges represent prosumer-prosumer pairs (T r kj).
retained in full as an input to the interaction function rather
than merely its sign.
Demand Fulfillment(F r ij): This factor reflects the energy
compatibility between the supplier and the consumer, defined
as the difference between the supplier’s available surplus and
the consumer’s demand.
F r ij =s r j − ˜dr i (3)
A positive value (F r ij ≥0) indicates that the supplier can fully
satisfy the consumer’s energy requirement. A negative value
indicates a shortfall where the supplier’s surplus is insufficient
to cover the consumer’s full demand.
Network Robustness(R r ij): Each consumer-prosumer pair
(i, j)is connected via a communication link with reliability
Rr ij ∈[0,1], drawn independently for each round. A value of
Rr ij = 0indicates total link failure whileR r ij = 1indicates
perfect connectivity. Poor link quality reduces the effective
trading potential even when price and energy conditions are
otherwise favorable. This factor serves as a conditional weight
whose role in the interaction function changes depending on
whether the energy condition is satisfied.
B. Interaction Function
The interaction functionf(·)combines the three factors into
a single real-valued score quantifying the trading potential
for pair(i, j)in roundr. Network robustness acts as a
conditional weighting factor. When the supplier can fulfill the
consumer’s demand (F r ij ≥0), higher robustness amplifies
the positive contribution of surplus. When the supplier cannot
fully meet demand (F r ij <0), the reciprocal of robustness acts
as a penalty where poor link quality compounds the energy
shortfall. A small constantϵ >0(e.g.,ϵ= 0.001) is introduced
to prevent division by zero, representing a minimum residual
link quality below which the link is considered effectively
failed. The interaction function is:
f

W r ij, Fr ij, Rr ij  =



W r ij +R r ij ·F r ij,ifF r ij ≥0
W r ij + 1 Rr ij +ϵ ·F r ij,ifF r ij <0
(4)
A positive score indicates a feasible and favorable inter-
action, while a negative score indicates an unfavorable or
infeasible one. The output of (4) is a real-valued continuous
score with no fixed range. To normalize it, we apply the
hyperbolic tangent:
¯f r ij = tanh  f  W r ij, Fr ij, Rr ij  (5)
The functiontanh(·)mapsRinto(−1,1), where values
close to+1indicate highly favorable interactions, values close
to−1indicate poor or failed interactions, and values near
0indicate neutral or marginal conditions. When interaction
magnitudes are very large due to high price scales, most values
saturate toward±1, reducing sensitivity. In such cases, a robust
normalization based on the median and interquartile range
(IQR) can be used instead, ensuring that the full dynamic

range of(−1,1)is utilized regardless of the absolute scale
of the interaction values.
˜f r ij = tanh
 f r ij −median
0.5·IQR

(6)
For notational brevity, the indices(i, j)are used as a generic
pair reference throughout this section. For prosumer-prosumer
pairs, the same equations apply with indices(k, j)wherek
denotes the deficit prosumer acting as consumer andjdenotes
the surplus prosumer acting as supplier.
To categorize each normalized score, we define two thresh-
oldsθ 1 <0< θ 2 and assign one of three sentiment labels to
each interaction:
Sentimentr ij =



Negative,if ¯f r ij ≤θ 1
Neutral,ifθ 1 < ¯f r ij < θ2
Positive,if ¯f r ij ≥θ 2
(7)
This three-way classification allows interaction histories to
be accumulated compactly over long time windows, retaining
only counts rather than full continuous scores for every pair
and round.
There are two types of trading pairs. Consumer-prosumer
pairs(C i, Pj)are active in any round where prosumerP j
holds a surplus. Prosumer-prosumer pairs(P k, Pj)are active
in rounds whereP j holds a surplus andP k is in deficit, having
switched to the consumer role under the flexible policy.
ETP is computed over a sliding window ofW= 11
rounds, corresponding to one day. Each window produces
one ETP value, and these are averaged across all windows
to yield the final ETP for a given mix. The first step is
computing the edge weight for each trading pair over the
window. Figure 1 demonstrates all possible pairs for (5:5) mix
for both flexible and static approach. The quantitiesH r ij and
H r kj denote the number of rounds within the window in which
the respective pair was active. For instance,H r ij counts how
many of the 11 rounds saw houseiacting as a consumer and
housejas a surplus-holding prosumer. As more windows are
observed, the averaged ETP converges toward a more reliable
characterization of the community’s trading behavior.
For consumer-prosumer pairs, letα CP ij ,β CP ij , andδ CP ij
denote the number of active rounds within the window that
were classified as positive, neutral, and negative respectively,
whereiis the fixed consumer andjis the surplus-holding
prosumer. For prosumer-prosumer pairs, the analogous counts
αP P kj ,β P P kj , andδ P P kj apply, withkas the deficit prosumer
acting as consumer andjas the surplus prosumer. Rounds
in which a pair is inactive do not increment any counter.
Negative interactions implicitly bring down the edge weight by
increasing the denominatorH r ij while keeping the numerator
same.
The edge weights for the two pair types are then defined
as:
T CP ij = αCP ij +γ βCP ij H r ij , T CP ij ∈[0,1](8)
T P P kj = αP P kj +γ βP P kj H r kj , T P P kj ∈[0,1](9)
whereγ∈[0,1]is a hyperparameter controlling the con-
tribution of neutral interactions to the edge weight. Setting
γ= 0treats neutral interactions as non-contributory, while
γ= 1treats them as fully equivalent to positive ones.
Intermediate values allow context-aware tuning depending on
whether neutral outcomes reflect marginal but genuine trades
or genuine infeasibility.
IV. FLEXIBLEROLE-SWITCHING
Flexible role-switching determines a prosumer’s market role
dynamically each trading round based on its instantaneous net
energy balance (1). Ifs r j >0, prosumerP j acts as a supplier
in roundr. Ifs r k ≤0, prosumerP k switches to the consumer
role, submits a bid priceb r k drawn from the consumer price
range, and its unmet demand is|s r k|=d r k −g r k. Lettingm r
denote the number of surplus-holding prosumers in roundr,
the effective community composition becomes:
Consumers in roundr=N C + (NP −m r) =N−m r
(10)
Suppliers in roundr=m r (11)
A. Active Edges
Since trades can only occur between a supplier and a
consumer, the number of active trading edges in roundris:
Er flex =m r ·(N−m r)(12)
This is a concave quadratic function inm r, with boundary
cases confirming expected behavior:E r flex = 0whenm r = 0
(no suppliers) orm r =N(no consumers). When prosumerP j
switches to the consumer role, it becomes eligible to trade with
any surplus-holding prosumerP k, creating prosumer-prosumer
edges entirely absent in the static model. The total number of
possible edges across all rounds is:
Etotal flex =N P (N−1)(13)
which decomposes as:
NP (N−1) =N C NP| {z }
consumer-prosumer pairs
+N P (NP −1)| {z }
prosumer-prosumer pairs
(14)
The second term quantifies the additional trading relationships
that flexible switching unlocks. For a prosumer-heavy commu-
nity(1:9)withN= 10, this yields9×9 = 81possible edges
under the flexible policy versus only1×9 = 9under the static
policy, a ninefold expansion.
B. ETP under Flexible Policy
For the trading pair consisting of deficit prosumerP k acting
as consumer and surplus prosumerP j acting as supplier, the
three trading factors are:
W r kj =b r k −o r j (15)
F r kj =s r j − |sr k|=s r j −(d r k −g r k)(16)
Rr kj ∈[0,1](17)

The interaction function (4), tanh normalization (5), and
sentiment classification (7) apply to these values without
modification, and the edge weightT P P kj is computed from (9)
over all rounds. The ETP under the flexible policy is:
ETPflex =
NCX
i=1
NPX
j=1
T CP ij +
NPX
k=1
NPX
j=1
j̸=k
T P P kj (18)
where the first term aggregates all consumer-prosumer pair
weights and the second term aggregates all prosumer-prosumer
pair weights enabled by role switching. This ETP is calculated
over a fixed window of W=11 rounds, and different 11-
round sets produce different ETPs which are averaged up. The
ETP is then normalized against the maximum possible ETP
achievable by anN-household community with the mix giving
highest ETP, ETP max, to obtain the ETPI:
ETPIflex = ETPflex ETPmax (19)
For example, in a 10-household community in our simulations,
the(1:9)configuration under the flexible policy has the largest
possible ETP of 38.052 when all interactions are assumed to
be positive. This value is used as ETP max for normalization
across various community mixes. The normalization yields a
dimensionless index in[0,1]enabling consistent comparison
across different community compositions and evaluation hori-
zons.
V. STATICPOLICY
The static policy represents the special case in which
prosumer roles are fixed for the entire simulation horizon
regardless of the per round energy balance. A prosumer always
appears on the supplier side of the bipartite graph in every
round. In rounds wheres r j ≤0, the prosumer is treated as
an inactive supplier, submits no offer, and participates in no
trades. It is never reclassified as a consumer and does not
gain access to buy energy from other prosumers. Figure 1
demonstrates the difference between the static and flexible
approaches with an example round of a (5:5) mix where 2 of
the 5 prosumers have no surplus. Those 2 deficit prosumers
remain isolated on the supplier side in the static case, while
in the flexible case they move to the consumer side and form
edges with the surplus-holding prosumers.
Under the static policy, the set of tradeable pairs is the fixed
set of consumer-prosumer pairs:
Estatic ={(C i, Pj) : 1≤i≤N C,1≤j≤N P }(20)
withE total static =N C ×N P .
A. ETP under the Static Policy
The ETP and ETPI under the static policy follow the same
structure as the flexible case but are computed only over the
fixed edge setE static, which contains consumer-prosumer pairs
exclusively. No prosumer-prosumer pairs exist under the static
policy, so the second term in (18) vanishes:
ETPstatic =
NCX
i=1
NPX
j=1
T CP ij (21)
We get multiple ETP values (one over each trading window
of W=11 rounds) and average them all out.
ETPIstatic = ETPstatic ETPmax (22)
The static policy thus provides a conservative lower bound
on trading activity, counting only pairs that could trade under
the most restrictive role assignment.
B. Per-Round Edge Gain and Optimal Role Switching
In roundr, only them r prosumers with positive surplus
participate as active suppliers. The remainingN P −m r deficit
prosumers are inactive. The number of active trading edges
under the static policy is:
Er static =m r ·N C (23)
Comparing (23) with (12), it is clear thatE r flex ≥E r static for
allm r, with equality only whenm r = 0orm r =N P . The
per-round gain from adopting the flexible policy is:
∆E(mr) =E r flex −E r static =m r(N−m r)−m rNC (24)
∆E(mr) =m r(NP −m r)(25)
Since0≤m r ≤N P , it follows that∆ E(mr)≥0with
strict inequality whenever0< m r < NP . The gain vanishes
only in the degenerate casesm r = 0(no suppliers) and
mr =N P (all prosumers are suppliers), where both policies
are equivalent. For the(6:4)mix,∆ E(mr)peaks at∆ E = 4
whenm r = 2, and∆ E = 3whenm r ∈ {1,3}.
SinceE r flex =m r(N−m r)is a concave quadratic inm r,
the optimal number of active suppliers is found by solving:
max
mr mr(N−m r),subject to0≤m r ≤N P (26)
Differentiating and setting equal to zero gives the uncon-
strained stationary pointm s =N/2. Applying the KKT
conditions for the bound constraintm r ≤N P , the constrained
optimum is:
m∗ = min
 N
2 , NP

(27)
The number of prosumers that should ideally switch to the
consumer role to maximize active edges isn ∗ switch =N P −m ∗,
which simplifies to:
n∗ switch =N P −min
 N
2 , NP

(28)
Example:N C = 2,N P = 8,N= 10. Thenm ∗ =
min(5,8) = 5andn ∗ switch = 3. Three prosumers should switch
roles, yielding a balanced(5:5)configuration with5×5 = 25
edges, compared to5×2 = 10under the static policy. When
NP < N/2, the unconstrained optimum is never reached and

n∗ switch = 0, meaning no switching is beneficial and keeping
all prosumers as suppliers is already optimal.
To characterize the expected benefit in a stochastic setting,
we model each prosumer as independently having surplus with
probabilityqin any round, som r ∼Binomial(N P , q)with
E[m] =N P qand Var(m) =N P q(1−q). The expected per-
round edge gain is then:
E[∆E] =E[m(N P −m)]
=N P E[m]−E[m 2]
=N 2 P q−N P q(1−q)−(N P q)2
=N P (NP −1)q(1−q)(29)
This is maximized atq= 1/2, yielding a peak expected
gain of:
E[∆E]max = NP (NP −1) 4 (30)
ForN P = 9, this gives9×8/4 = 18additional active edges
per round. The quadratic scaling with prosumer count confirms
that flexible role switching is most beneficial in prosumer-
heavy communities.
VI. SIMULATIONS
A. Simulation Methodology
Both the flexible and static simulations are implemented in
Python using a 13-segment pipeline. Each trading round spans
one hour and there are 11 trading rounds per day from 08:00
to 19:00. The ETP of each day is computed (W=11 rounds
per day). 365 ETP values were calculated over 1 year, and
averaged out. The(0:10)mix is included only for the flexible
case since under the static policy all prosumers remain on
the supplier side with no buyers present, yielding zero trading
activity. The(10:0)case is excluded entirely since without
any prosumers there is no surplus energy to trade under either
policy.
Hourly energy consumption data is drawn from the PRE-
CON dataset [20] for a one-year period (June 2018 to May
2019). The dataset provides residential load profiles collected
in Pakistan, with average monthly energy demand across the
ten selected households ranging from approximately 352 kWh
to 535 kWh. Only demand values during market operating
hours (08:00 to 19:00) are used. Hourly solar generation
data is obtained from the NREL PVWatts tool for 3 kW,
5 kW, 7 kW, and 10 kW PV system specifications, alternating
across prosumer households. Independent random perturba-
tions of±10–20% are applied to each prosumer’s base profile
to simulate inter-household variability in panel orientation,
shading, and inverter efficiency. All values are constrained to
be non-negative. Consumer bid prices are drawn uniformly
from [PKR 10, PKR 14]/kWh and prosumer offer prices from
[PKR 8, PKR 14]/kWh, reflecting the spread between retail
electricity tariff rates and net metering buyback rates in Pak-
istan during the simulation period. The sentiment classification
thresholds are set toθ 1 =−0.5andθ 2 = 0.5, and the floor
constant toϵ= 0.001.
B. Simulation Results
Edge Counts:Figure 2 presents the annual active edge counts
broken down by interaction sentiment alongside the total edge
counts in both approaches across all ten community mixes. In
both policies, positive interactions dominate the edge count
at every mix. The most pronounced differences appear in
prosumer-heavy configurations. For the(1:9)configuration,
the flexible policy generates 45,594 total active edges across
the simulation year, compared to only 26,370 under the static
policy, a 73% increase. With nine prosumers, role switching
creates up to9×8 = 72possible prosumer-prosumer pairs
that are entirely absent under the static model. This confirms
the analytical result from (14). As solar penetration grows
and communities become prosumer-heavy, the static model
discards a substantial portion of realizable trading activity,
precisely the scenario motivating the flexible policy.
As the mix shifts toward consumer-heavy configurations, the
two policies converge. For the(9:1)mix, total edges under the
two policies are nearly identical (27,144 vs. 27,072), consistent
with the analytical result from (24). WithN P = 1there is
only one prosumer to role switch, which does not have a
significant impact. The peak total edge count under the flexible
policy occurs at the(5:5)mix with 79,676 annual active edges,
compared to 74,130 for the static policy at the same mix, a
more modest 7.5% difference. The total edge curves form an
inverted-U shape as a function of mix in both policies, with
the flexible curve lying strictly above the static curve for all
prosumer-skewed configurations.
ETP:Figure 3 shows the variation of ETP across community
mixes under both policies. A striking feature of the flexible
policy is the near-plateau in ETP for prosumer-heavy mixes.
The flexible ETP remains approximately 22–23 across the
(0:10)through(3:7)configurations before declining toward
consumer-heavy mixes. This stability arises because role
switching in prosumer-heavy communities creates a large and
diverse pool of active pairs, many of which achieve positive
or neutral interaction scores, keeping the aggregate ETP high
regardless of composition. This result directly addresses the
open question of whether trading potential collapses as neigh-
borhoods become prosumer-heavy. Under the flexible policy it
does not, even in the extreme(0:10)case where all households
are prosumers. Notably, although the total edge count peaks at
the(5:5)mix under both policies, the flexible ETP does not.
This is because ETP measures the quality-weighted sum of
trading pairs throughT CP ij andT P P kj , not merely their count.
Prosumer-prosumer pairs unlocked by role switching tend to
achieve higher interaction scores, driving higher edge weights
in prosumer-heavy configurations even when raw edge count
is lower.
The static ETP follows a fundamentally different profile,
forming a smooth near-symmetric bell curve peaking near the
(5:5)mix. The static(1:9)configuration achieves an ETP
value of 5.5, which is more than four times lower than the
flexible(1:9)value of23.3. This divergence quantifies the
trading activity discarded by the static model when deficit

Fig. 2. Positive, Negative and Neutral edges count for all the mixes using both the flexible and static policy. The left axis is for the bars, and the right one
is for the total edge count lines.
Fig. 3. ETP of all the mixes under both the flexible and static policies
Fig. 4. ETPI of all the mixes under both the flexible and static policies
prosumers are prevented from buying surplus energy from
peers. A dashed green line at ETP max = 38.052is included
for reference, and all realized ETP values lie well below this
ceiling, highlighting the room for improvement that motivated
the ETPI as a normalized index.
ETPI:Figure 4 shows the ETPI across community mixes for
both policies. Under the flexible policy, the ETPI is highest for
prosumer-heavy mixes, with values around 0.56–0.62 for the
(0:10)through(3:7)range, declining to approximately 0.15
for the(9:1)configuration. The flexible ETPI does not peak
at(5:5)but remains elevated across the prosumer-heavy range,
reflecting the large prosumer-prosumer edge pool enabled by
role switching. These results have a direct practical implication
for communities in markets with declining feed-in tariffs and
growing rooftop solar penetration. Such communities tend
toward prosumer-heavy compositions yet retain substantial
P2P trading potential and can justify advanced infrastructure
investment when assessed under the flexible policy.
Under the static policy, the ETPI peaks at the(5:5)mix at
approximately 0.42 and falls steeply for both prosumer-heavy
and consumer-heavy extremes. The static(1:9)mix achieves
an ETPI of only 0.15, which would incorrectly disqualify
it from advanced infrastructure investment under a static
assessment. The flexible ETPI of≈0.61for the same mix
reveals that the community is far more active than the static
model suggests, underscoring the importance of accounting for
role flexibility when evaluating P2P infrastructure deployment.
ETP vs. PV Capacity:Figure 5 shows how ETP varies with
PV system capacity across all mixes under both policies.
Six capacity configurations are evaluated, ranging from all
3 kW systems to alternating configurations such as 3 kW and
5 kW systems across prosumer households. The results reveal

Fig. 5. ETP with different capacities for all mixes under both flexible and static policies.

Fig. 6. ETP with different gamma values for all mixes using both flexible and static method

a qualitative split between prosumer-heavy and consumer-
heavy mixes. For consumer-heavy mixes(6:4)through(9:1),
ETP increases monotonically with PV capacity under both
policies. Larger solar systems generate more surplus, creating
more and larger active trading events. For prosumer-heavy
mixes(0:10)through(3:7), ETP under the flexible policy
decreases with increasing capacity. This counterintuitive re-
sult arises because higher capacity systems produce larger
surpluses that are rarely matched by the limited demand on
the consumer side. Larger surpluses also reduce the frequency
with which prosumers enter deficit and switch to the consumer
role, thereby shrinking the prosumer-prosumer edge pool.
This finding carries an important practical implication for
communities in markets with high rooftop solar adoption.
Simply maximizing installed PV capacity is not an effective
strategy for maximizing P2P trading potential. At balanced
mixes such as(4:6)and(5:5), ETP is relatively insensitive to
capacity under the flexible policy, reflecting a balance between
increased surplus-driven supply and reduced role-switching
frequency.
ETP vs. Gamma:Figure 6 presents the sensitivity of ETP
to the hyperparameterγfor all mixes under both policies.
Increasingγfrom 0 to 1 monotonically raises ETP for both
approaches and across all mixes, as expected from (8) and
(9). Counting neutral interactions as fully positive (γ= 1)
inflates the aggregate ETP, while counting them as non-
contributory (γ= 0) deflates it. As the mix shifts toward
consumer-heavy configurations, the flexible and static curves
converge and nearly overlap at the(9:1)mix, consistent with
the analytical result that the per-round edge gain from role
switching vanishes asN P approaches 1.
VII. CONCLUSION
In this paper we proposed an ETPI to quantify the structural
impact of flexible role switching on P2P energy trading
potential in residential smart grid communities. Simulation
results show that prosumer-heavy communities retain substan-
tial trading potential under the flexible role-switching policy.
The fourfold ETPI improvement in the(1:9)mix directly
answers whether trading activity survives as neighborhoods
become prosumer-heavy. In markets where declining feed-
in tariffs are pushing households toward P2P trading, ETPI
provides a principled pre-deployment tool for justifying ad-
vanced infrastructure investment. Sensitivity analysis further
revealed that maximizing installed PV capacity is counter-
productive in prosumer-heavy communities, a non-obvious
result with direct policy implications. The ETPI framework
evolves naturally from a pre-deployment estimate into a live
monitoring instrument as trading data accumulates, supporting
evidence-based infrastructure decisions throughout the system
lifecycle. Future work will explore demand response as an
active mechanism for improving trading potential by reshaping
consumption patterns, and will extend the model to incorporate
battery storage, enabling richer prosumer behavior and more
persistent trading activity.
REFERENCES
[1] E. A. Soto, L. B. Bosman, E. Wollega, and W. D. Leon-Salas, “Peer-
to-peer energy trading: A review of the literature,”Applied Energy, vol.
283, p. 116268, 2021.
[2] W. Tushar, S. Nizami, M. I. Azim, C. Yuen, D. B. Smith, T. Saha,
and H. V . Poor, “Peer-to-peer energy sharing: A comprehensive review,”
Foundations and Trends in Electric Energy Systems, vol. 6, no. 1, pp.
1–82, 2023.
[3] International Energy Agency, “Renewables 2025,” IEA, Paris, Tech.
Rep., 2025. [Online]. Available: https://www.iea.org/reports/renewables-
2025
[4] Z. Tanis, A. Durusu, and N. Altintas, “A comprehensive review on
peer-to-peer energy trading: Market structure, operational layers, energy
cooperatives and multi-energy systems,”IET Renewable Power Gener-
ation, vol. 19, p. e70075, 2025.
[5] G. Bhavana, R. Anand, J. Ramprabhakar, V . Meena, V . K. Jadoun, and
F. Benedetto, “Applications of blockchain technology in peer-to-peer
energy markets and green hydrogen supply chains: A topical review,”
Scientific Reports, vol. 14, no. 1, p. 21954, 2024.
[6] S. Wang, A. F. Taha, J. Wang, K. Kvaternik, and A. Hahn, “Energy
crowdsourcing and peer-to-peer energy trading in blockchain-enabled
smart grids,”IEEE Transactions on Systems, Man, and Cybernetics:
Systems, vol. 49, no. 8, pp. 1612–1623, 2019.
[7] A. Dorri, A. Hill, S. Kanhere, R. Jurdak, F. Luo, and Z. Y . Dong, “Peer-
to-peer energytrade: A distributed private energy trading platform,” in
Proceedings of the IEEE International Conference on Blockchain and
Cryptocurrency (ICBC), 2019, pp. 61–64.
[8] E. Mengelkamp, J. G ¨arttner, K. Rock, S. Kessler, L. Orsini, and
C. Weinhardt, “Designing microgrid energy markets: A case study: The
brooklyn microgrid,”Applied Energy, vol. 210, pp. 870–880, 2018.
[9] M. H. Nazari and A. K. Biswas, “Decentralized p2p trading based on
blockchain for retail electricity markets,” inProceedings of the IEEE
PES Innovative Smart Grid Technologies (ISGT), 2024, pp. 1–5.
[10] M. Khorasany, A. Dorri, R. Razzaghi, and R. Jurdak, “Lightweight
blockchain framework for location-aware peer-to-peer energy trading,”
International Journal of Electrical Power & Energy Systems, vol. 127,
p. 106610, 2021.
[11] T. Alskaif, J. L. Crespo-Vazquez, M. Sekuloski, G. van Leeuwen, and
J. P. S. Catal ˜ao, “Blockchain-based fully peer-to-peer energy trading
strategies for residential energy systems,”IEEE Transactions on Indus-
trial Informatics, vol. 18, no. 1, pp. 231–241, Jan. 2022.
[12] M. Zade, M. Feroce, A. Guridi, S. D. Lumpp, and P. Tzscheutschler,
“Evaluating the added value of blockchains to local energy markets,”
IET Smart Grid, vol. 5, no. 4, pp. 234–245, 2022.
[13] D. Neves, I. Scott, and C. A. Silva, “Peer-to-peer energy trading poten-
tial: An assessment for the residential sector under different technology
and tariff availabilities,”Energy, vol. 205, p. 118023, 2020.
[14] W. Tushar, T. K. Saha, C. Yuen, D. Smith, and H. V . Poor, “Peer-to-
peer trading in electricity networks: An overview,”IEEE Transactions
on Smart Grid, vol. 11, no. 4, pp. 3185–3200, Jul. 2020.
[15] A. Paudel, K. Chaudhari, C. Long, and H. B. Gooi, “Peer-to-peer energy
trading in a prosumer-based community microgrid: A game-theoretic
model,”IEEE Transactions on Industrial Electronics, vol. 66, no. 8, pp.
6087–6097, Aug. 2019.
[16] J. Lee, J. Guo, J. K. Choi, and M. Zukerman, “Distributed energy trading
in microgrids: A game-theoretic model and its equilibrium analysis,”
IEEE Transactions on Industrial Electronics, vol. 62, no. 6, pp. 3524–
3533, Jun. 2015.
[17] M. H. Ullah and J. D. Park, “Peer-to-peer energy trading in transactive
markets considering physical network constraints,”IEEE Transactions
on Smart Grid, vol. 12, no. 4, pp. 3390–3403, Jul. 2021.
[18] W. Liu, D. Qi, and F. Wen, “Intraday residential demand response
scheme based on peer-to-peer energy trading,”IEEE Transactions on
Industrial Informatics, vol. 16, no. 3, pp. 1823–1835, Mar. 2020.
[19] L. Zeng, C. Li, Z. Li, M. Shahidehpour, B. Zhou, and Q. Zhou,
“Hierarchical bipartite graph matching method for transactive v2v power
exchange in distribution power system,”IEEE Transactions on Smart
Grid, vol. 12, no. 1, pp. 301–311, Jan. 2021.
[20] A. Nadeem and N. Arshad, “PRECON: Pakistan residential electricity
consumption dataset,” inProceedings of the 10th ACM International
Conference on Future Energy Systems, 2019, pp. 52–57.
