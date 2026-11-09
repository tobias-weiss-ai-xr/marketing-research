---
title: Comparing Socially-Equitable Renewable Energy Budget Allocation MDP Policies in Mature and Emerging
  Economies
url: https://arxiv.org/abs/2607.10201
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Riya Kinnarkar
- Mansur M. Arief
- Yan Pratama Akhra
- Dino Arla
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.10201
pages: 6
chars: 26202
fetched_at: '2026-11-08T13:21:54+00:00'
kb_version: 1
---

# Comparing Socially-Equitable Renewable Energy Budget Allocation MDP Policies in Mature and Emerging Economies

Comparing Socially-Equitable Renewable Energy
Budget Allocation MDP Policies
in Mature and Emerging Economies
Riya Kinnarkar
Management & Technology
University of Pennsylvania
Philadelphia, PA, USA
Yan Pratama Akhra
Industrial and Systems Engineering
Institute Technology of Sepuluh Nopember (ITS)
Surabaya, Indonesia
Mansur M. Arief
Industrial and Systems Engineering
King Fahd University of Petroleum
and Minerals (KFUPM), Saudi Arabia
Dino Arla
PT PLN Persero
Indramayu, Indonesia
Abstract—Equitable renewable-energy planning is a
sequential decision problem, but the decision variables
available to a public planner differ sharply between
mature and emerging economies. In the former the
government largely builds generation, while in the latter
it steers private investment through incentives and quo-
tas. We formulate socially-equitable renewable-energy
budget allocation as a Markov Decision Process (MDP)
and, using a single problem-agnostic solver interface,
compare the same policies across the two settings:
eight U.S. cities (a mature economy) and West Java,
Indonesia (an emerging economy). The results show that
across both settings, a receding-horizon value-iteration
policy dominates. In the U.S., it reaches 66% renewable
penetration while cutting the underserved low-income
population by 96% versus a random baseline. In West
Java it closes the low-access gap while crowding in about
seven times the private capital of a naive market-chasing
heuristic. More interestingly, this heuristic, which is
mildly sub-optimal in the U.S., could yield catastrophic
outcomes in Indonesia, by underserving every low-access
region, because chasing attractive markets and serving
the underserved diverge once the planner acts through
private developers.
Index Terms—Renewable energy, social equity,
Markov Decision Process, grid optimization, energy
justice
I. INTRODUCTION
The transition to renewable energy spans both
technical and societal considerations. Grids designed
for dispatchable fossil generation struggle to absorb
variable wind and solar. While renewable investment
has surged, grid infrastructure funding has lagged,
leaving thousands of gigawatts of projects awaiting
connection [1]. At the same time, the burdens of an
unreliable grid fall disproportionately on low-income
and socially vulnerable communities: U.S. households
in poverty spend more than twice the average share of
income on energy [2]. After major storms, for example,
communities lower on the CDC social vulnerability
index wait significantly longer for power to return [3].
Yet, most renewable-energy planning tools optimize
cost and reliability while treating equity as an add-
on. Embedding social equity directly into the planner’s
objective is therefore both a modeling and a policy
need.
The crux of our study is that the public levers for
driving an equitable renewable transition differ fun-
damentally betweenmatureandemergingeconomies.
In a mature economy such as the U.S., a public
planner can directly finance and build generation under
a capital budget. In an emerging economy such as
Indonesia, most renewable capacity is built by private
companies and independent power producers selling to
the state utility. To that end, the government’s lever is
not construction butincentives and quotasthat steer
where private capital flows. A planning model, and
the policy insights drawn from it, may not survive
this shift. We therefore formulate socially-equitable
budget allocation as a Markov Decision Process (MDP)
and evaluate thesameset of policies on two set-
tings: eight U.S. cities (the planner builds) and West
arXiv:2607.10201v2  [eess.SY]  11 Oct 2026

Java, Indonesia (the planner incentivizes). We compare
receding-horizon value iteration [4], Monte Carlo Tree
Search (MCTS) [5], and equity- and market-oriented
heuristics, and cross-deploy each policy’s inductive
bias from one setting to the other.
Our contribution is as follows. First, we build
an MDP model of socially-equitable renewable-
energy budget allocation that extends our earlier U.S.
model [6] and is applicable to both mature and emerg-
ing economies. Second, we compare MDP-based poli-
cies across the two settings that differ in the planner’s
lever, eight U.S. cities (a mature economy) and West
Java, Indonesia (an emerging economy), to study the
robustness of the outcomes and identify modes of
failure from both technical and societal perspectives.
The comparison reveals that while a value-iteration
policy and an equity-targeting objective are robust
across both contexts, a market-chasing heuristic that is
merely sub-optimal when the planner builds becomes
actively harmful when the planner incentivizes, which
is a risk that neither setting reveals on its own.
II. RELATEDWORK
Renewable-energy planning has traditionally been
framed as a cost-and-reliability optimization. Long-
horizon capacity-expansion tools such as ReEDS [7]
simulate grid growth to guide investment. A growing
body of evidence shows that higher renewable pene-
tration correlates with fewer and shorter outages and
not with a more fragile grid [8]. Such models excel
at aggregate trends but assume fixed conditions and
rarely capture the distributional outcomes that matter
for equity. In our view, this omission is consequential,
as outages fall hardest on vulnerable communities, as
socially vulnerable neighborhoods and lower-income
census tracts endure markedly longer losses after ex-
treme weather [9], [10]. Reviews of data-driven grid
resilience nevertheless find that most methods still omit
an explicit equity objective [11], motivating frame-
works that encode disparity in the decision process
itself.
The MDP is a natural framework for handling
stochastic, sequential decisions and admits both ex-
act [4] and sampling-based [5] solvers. MDPs and
related sequential methods have been applied to pho-
tovoltaic voltage regulation [12], community storage
for social welfare [13], uncertainty-aware microgrid
dispatch [14], household technology adoption [15],
and machine-learning-augmented system design [16].
These earlier studies mostly optimized technical ob-
jectives. In this study, we instead add another layer of
social equity directly in the reward.
The social equity aspect and the corresponding pol-
icy levers in renewable energy planning and decision
making are an active area of research. Energy-justice
research asks how the benefits and costs of energy
services are distributed and who takes part in the
decisions [17]. Earlier studies have also examined the
policy levers that emerging economies use to drive
clean-energy investment, including green-finance in-
struments that improve energy accessibility [18], gov-
ernment guidance funds that raise renewable-firm pro-
ductivity [19], and quota mechanisms that shape clean-
energy investment decisions [20]. Empirical work on
Indonesia links slow private investment in renewables
to regulatory barriers, a monopolized power market
and changing pricing rules [21], [22], and finds that
private financing of rural electrification favors large
on-grid projects over small distributed ones [23]. A
core finding of this literature is that, where the state
regulates and does not build, the design of incentives
and quotas, and not direct construction, determines
outcomes. These two research directions, however,
rarely converge: sequential-decision models are typi-
cally posed for a single build-centric planner, while
incentive-design studies rarely cast the problem as a
sequential policy over heterogeneous regions. Our con-
tribution bridges them by evaluating thesameequity-
aware MDP policies across both institutional regimes
and, crucially, bycross-deployingeach policy from one
regime to the other to expose which insights transfer
and what unintended failures and risks could emerge.
III. MDP FORMULATION
We model equitable energy allocation as an MDP
(S,A, T, R, γ)over a set ofnregionsI={1, . . . , n}.
State.The state at timetis given bys t =
(b,[d i, ri, ni, pi, Ii]i∈I),wherebis the remaining bud-
get and, for regioni,d i is energy demand,r i andn i are
renewable (RE) and non-renewable (NRE) supply,p i
is population, andI i ∈ {0,1}is an income indicator (0
= low income). Demand is stochastic,d i ∼ N(µi, σ2 i ).
Action.At each step the planner adds or removes
an RE or NRE facility in a chosen regioni(a capacity
increment∆s r or∆s n), or does nothing (a 0). Each
build/retire action debits the budget by the corre-
sponding capital cost (c a,r, ca,n, cr,r, cr,n) plus per-unit
operating costc o,·,i.
Transition.The dynamics factor into adeterministic
control component and astochasticexogenous compo-

nent. Given actiona t acting on regioni, the capacity
and budget update deterministically:
r′ i =r i ±∆s r (RE)(1)
n′ i =n i ±∆s n (NRE),(2)
b′ =b−c(a t)− P j co,·,j x′ j,(3)
wherec(a t)is the capital cost ofa t and the last term
is total operating cost over installed capacityx ′ j; all
other regions are unchanged. The stochasticity enters
through demand: at every step each region’s demand
is resampled,d ′ i ∼ N(µi, σ2 i ), so the planner commits
capacity before demand is realized and must be robust
to demand fluctuation instead of optimizing against a
fixed forecast. The transition kernel is thus
T(s ′ |s, a) =1(r ′, n′, b′), Y
i
N(d ′ i;µ i, σ2 i ),(4)
i.e., a Dirac mass on the controllable variables times
an independent Gaussian on demand. An episode ter-
minates after a fixed horizon ofHdecisions or when
the budget is exhausted. The discountγthen trades off
near- versus long-term coverage. This structure keeps
the model tractable for exact solvers on a discretized
budget grid while preserving the demand uncertainty
that makes purely myopic “fill-the-largest-deficit” rules
fragile.
Reward.The reward balances three competing ob-
jectives, evaluated on the resulting states t+1 (the
standardR(s, a, s′)convention, so an investment is
credited in the step it is made). Letκ(a t)be the
expenditure ofa t,P 0 = P i:Ii=0 pi, andP= P i pi:
R(st, at) =w 1κ(at) + w2 P0 X i:Ii=0 pi min  1, r′ i+n′ i d′ i 
+ w3
P
X
i∈I
pi min

1, r′ i d′ i  ,(5)
withw 1 =−0.02,w 2 = 200,w 3 = 80(Table I) and
γ= 0.95. The three terms are cost, the population-
weightedcoverage servedamong low-income regions
(equity), and the population-weighted renewable cov-
erage (decarbonization). Rewarding coverageserved
instead of penalizing shortfall keeps the objective
positive without changing the policy ranking, and
charging the budget throughκ(a t)instead of crediting
the remaining budget each step prevents the degenerate
“do nothing to preserve cash” optimum.
IV. NUMERICALEXPERIMENTS
We study two cases that share the MDP structure of
Section III and thesamesolver code, but differ in the
planner’s lever: a mature economy where the planner
builds generation (Case 1) and an emerging economy
where the planner steers private capital through incen-
tives and quotas (Case 2). Results for both are reported
together in Section V.
Case 1: U.S. Model.We instantiate the MDP on
eight major U.S. cities (Atlanta, New York, Houston,
Phoenix, Denver, Memphis, Seattle, San Antonio),
chosen for diverse demographics, incomes, and energy
mixes, using synthetic-but-plausible data (a city is
“low-income” if≥25%of its population is low-
income). The planner starts with a $3,000M budget
and makes 20 sequential decisions; costs, capacity
increments, and reward weights are in Table I.
TABLE I: Case 1 Experiment Parameters (U.S. Model)
Parameter Value
Initial budget $3,000M
Add RE / NRE cost (c a,r, ca,n) $180M / $120M
Remove RE / NRE cost (c r,r, cr,n) $120M / $180M
RE / NRE operating cost (c o,·,i) $8–14 / $35–48 per MWh
Supply increment (∆s r,∆s n) 10 GW
Horizon / discount (γ) 20 decisions / 0.95
Weights (w1, w2, w3)−0.02,200,80
TABLE II: Case 2 Parameters (West Java Model)
Parameter Value
Initial incentive budget IDR 1,000 bn
Incentive / off-grid / quota cost 40 / 90 / 5 (IDR bn)
Incentive / off-grid capacity 20 / 18 GW
Quota release per action 20 GW
Max private leverage (×incentive) 3.0
Cost weight (w 1)−0.02
Access-coverage weight (w 2)180
RE-coverage weight (w 3)70
Leverage / deadweight weight+25/−20
Horizon / discount (γ) 20 decisions / 0.95
Case 2: West Java Model.In many emerging
economies the government does not build butregu-
lates and finances: in West Java (Jawa Barat), most
renewable capacity is built by private developers and
IPPs selling to the state utility PLN. We recast the
MDP accordingly. Theaction spaceshifts from “what
to build” to “where to direct an incentive or quota”:
the planner can issue an on-grid incentive (realized by
private capital), fund an off-grid project directly, or
release on-grid quota. On-grid deployment is capped
by a per-region PLNquota(post net-metering, based
on local regulations), while off-grid projects serve re-
mote regencies (Sukabumi, Garut, Tasikmalaya) where

TABLE III: Case 1 Policy Comparison: U.S. Model
Policy Reward RE % Budget Low-Inc Low-Inc
↑ ↑($M) Cities↓Pop (M)↓
Value Iteration4319±6466.3±1.6 2962±25 1.3±0.50.22±0.08
Equity-MCTS 3960±89 50.5±4.1 1584±50 3.5±0.6 1.62±0.32
MCTS 3933±86 43.2±4.2 2050±50 3.0±0.7 1.29±0.31
Equity-Greedy 3921±68 67.5±0.6 2916±59 2.4±1.0 0.53±0.45
Market-Greedy 3344±59 24.0±0.0 2430±95 2.3±1.1 0.47±0.42
Random 2439±353 45.9±6.9 2873±206 4.4±0.8 5.61±1.53
TABLE IV: Case 2 Policy Comparison: West Java Model
Policy Reward RE % Budget Low-Acc Leverage
↑ ↑(IDR, billions) Pop (M)↓ ↑
Value Iteration3549±4052.4±0.6 909±430.00±0.00479±18
MCTS 3511±56 55.6±1.0 992±8 0.04±0.11 498±18
Equity-Greedy 3421±55 49.7±1.8 813±84 0.00±0.00 425±40
Equity-MCTS 3406±60 54.1±2.1 947±54 0.22±0.39 468±42
Random 2068±289 46.4±3.5 590±128 2.95±0.85 264±70
Market-Greedy 1411±40 34.7±0.0 167±32 6.26±0.10 68±0
grid extension is costly. Aleverageterm creditsad-
ditionalprivate capital drawn into regions the market
ignores and penalizesdeadweightsubsidies to already-
attractive clusters [18], [19], and a per-clusterquota
constraintfollows the multi-year cycle [20]. The re-
ward keeps the same coverage-served structure, now
over low-accessregions, plus the leverage term. The
experiment parameters are summarized in Table II.
Policies.Every policy is implemented behind a
common problem-agnostic interface (valid actions,
transition, reward, terminal test, and equity/market
scoring hooks) so theidenticalsolver code runs on
both cases. We evaluate six policies:Random; two
one-step greedy heuristics:Equity-Greedy(target the
low-income group’s shortfall) andMarket-Greedy(the
naive “chase the cheap/easy win”); and three planning
solvers: receding-horizonValue Iteration[4] with a
two-step lookahead, baseMCTS(uniform-random roll-
outs, UCT selection) [5], andEquity-MCTS(MCTS
with an equity-biased informed rollout and tree prior).
Each policy is evaluated over 30 seeded replications.
The random and greedy rules serve as rule-based
benchmarks for these established MDP solvers. We
additionallycross-deployeach policy’s inductive bias
(equity vs. market) from one case to the other to study
the transferability and robustness of the policies.
V. RESULTS ANDDISCUSSION
Table III (Case 1) and Table IV (Case 2) give per-
policy metrics, Figure 1 places the two cases together,
and Figure 2 shows the cross-deployment transfer. In
bothcases,value iteration dominates on reward
and equity: in Case 1 it earns the highest reward
(4319±64) at66%renewable penetration while leaving
only0.22M low-income residents underserved (a96%
reduction versus Random); in Case 2 it earns the best
reward (3549), fully closes the access gap, and secures
the second-highest private leverage (479, against498
for MCTS). The other principled solvers (the two
MCTS variants and Equity-Greedy) cluster just behind
in both. The decisive difference is Market-Greedy: the
weakest non-random policy in Case 1 (3344, with, by
coincidence, few underserved because there the largest
raw deficits and the priority group align), itcollapsesin
Case 2 to the worst reward (1411), worst equity (6.26M
underserved, which covers every low-access region),
and lowest leverage (68), falling below Random. Three
findings follow.
First, optimization beats heuristics, and equity
need not cost efficiency.In both cases the value-
iteration policy attains the best rewardandthe best
equity, with the strong planners and the equity heuristic
just behind. That the reward-maximizing policies are
also the most equitable challenges the assumed equity–
efficiency trade-off in infrastructure planning, echoing
evidence that well-targeted green-finance and incentive
policies expand access without sacrificing productiv-
ity [18], [19].
Second, the cost of a naive heuristic is economy-
dependent(Figure 1). The rewardrankingis nearly
identical across cases under the same solver code,

0
2,000
4,000
Reward
(a) United States: avg reward↑
0
1,000
2,000
3,000
Reward
(b) West Java: avg reward↑
VI
Eq-MCTS MCTSEq-GreedyMk-Greedy Random
0
2
4
6
Millions
(c) United States: low-income unserved (M)↓
VI
Eq-MCTS MCTSEq-GreedyMk-Greedy Random
0
2
4
6
Millions
(d) West Java: low-access unserved (M)↓
Fig. 1: Policy comparison: Case 1 U.S. (left, blue) and Case 2 West Java (right, orange). Top: average reward;
bottom: priority-group population left underserved (low-income cities in the U.S., low-access regions in West
Java). Error bars are 1 std over 30 replications. The market-chasing heuristic (Mk-Greedy) is sub-optimal in
Case 1 but catastrophic in Case 2.
Equity Market
0
2,000
4,000
Average reward
(a) Greedy heuristic
Deployed on US Deployed on Indonesia
Equity Market
(b) MCTS (informed)
Fig. 2: Cross-deployment of the two inductive biases
(equity vs. market) as (a) a greedy heuristic and (b)
an informed-rollout MCTS planner, each deployed on
both cases. The market bias collapses when deployed
on Case 2 (a), while lookahead sustains it (b).
but the penalty for a poorly designed heuristic is not.
Market-Greedy is only mildly sub-optimal when the
planner builds, because there the largest raw deficits
and the priority group coincide; it is catastrophic when
the planner incentivizes, because “chase the attractive
market” and “serve the underserved” pull apart once
deployment runs through private developers who avoid
poor and remote regions. A policy’s error is thus not a
property of the policy alone but of how the economy
couples the planner’s lever to the equity objective,
which is the central message of the paper and cannot
be seen in either case alone.
Third, robustness comes from the objective or
from lookahead(Figure 2). A greedyequitybias is
safe in both cases; a greedymarketbias collapses in
Case 2 (1411,6.26M underserved), but adding looka-
head rescues it (market-biased MCTS:3531,0.03M)
because multi-step planning sees past the myopic tar-
get. The dangerous combination is a myopic policy
with a mis-targeted bias; sound incentive design should
pair targeting rules with at least short-horizon planning.
Sensitivity to the reward weights.We rescaled
each reward weight by0.5and1.5, one at a time (six
settings in Case 1, ten in Case 2). Value Iteration keeps
the highest reward in all sixteen settings, and Market-
Greedy stays below Random in every Case 2 setting.
Only the middle policies change order, and the Case 2
lead of Value Iteration over MCTS narrows when the
access weight is halved.
Practical implications.The Case 2 gap is driven
by the quota. Market-Greedy exhausts the on-grid
quota of the attractive clusters after four incentives and
leaves about 83% of the budget unspent, whereas Value
Iteration pairs every incentive with a quota release in
the same low-access region. A provincial energy office
can use the model to screen a proposed targeting rule
before funds are committed.
VI. CONCLUSION
We formulated socially-equitable renewable-energy
budget allocation as an MDP and evaluated the same
policies across a mature economy where the planner
builds (eight U.S. cities) and an emerging economy
where the planner incentivizes (West Java, Indonesia).

Equity-focused value iteration dominates on both re-
ward and equity in both settings, but the cost of a
naive market-chasing heuristic is economy-dependent.
It is mildly sub-optimal under direct construction,
yet worse than random under incentive-based deploy-
ment, where it abandons the very communities an For
emerging economies, the results suggest that incentives
should pay for the additional private capital brought
to low-access regions and not for installed capacity.
In addition, quota should be released together with
the incentive in the targeted regions. Finally, off-grid
supply should be funded directly where private appetite
is weak. Targeting rules should also be paired with
short-horizon planning. This study offers new insights
for policy makers by analyzing the MDP policies in
different economies to help us design a more equitable
renewable energy systems for all.
REFERENCES
[1] International Energy Agency, “Electricity grids and secure
energy transitions,” International Energy Agency, Paris,
Special Report, 2023. [Online]. Available: https://www.iea.
org/reports/electricity-grids-and-secure-energy-transitions
[2] Pearl Certification and Elevate, “Understanding the gap:
America’s community-based disparities in energy efficiency,”
Building Performance Association, February 2024. [Online].
Available: https://building-performance.org/bpa-journal/und
erstanding-the-gap-americas-community-based-disparities-i
n-energy-efficiency/
[3] C. Ji and S. C. Ganz, “Power outages leave poor communities
in the dark longer,” February 2024. [Online]. Available:
https://www.governing.com/infrastructure/power-outages-lea
ve-poor-communities-in-the-dark-longer
[4] R. Bellman, “Dynamic programming,”Princeton University
Press, Princeton, NJ, USA, vol. 1, pp. 3–25, 1958.
[5] C. B. Browne, E. Powley, D. Whitehouse, S. M. Lucas, P. I.
Cowling, P. Rohlfshagen, S. Tavener, D. Perez, S. Samoth-
rakis, and S. Colton, “A survey of monte carlo tree search
methods,”IEEE Transactions on Computational Intelligence
and AI in games, vol. 4, no. 1, pp. 1–43, 2012.
[6] R. Kinnarkar and M. Arief, “Optimized renewable energy
planning MDP for socially-equitable electricity coverage in
the US,”arXiv preprint arXiv:2509.00008, 2025.
[7] National Renewable Energy Laboratory, “Regional energy
deployment system (ReEDS),” National Renewable Energy
Laboratory, Golden, CO, 2024. [Online]. Available: https:
//www.nrel.gov/analysis/reeds/
[8] J. Nieman, “How do renewables affect grid reliability?”
EEPower, Dec 2025, accessed: October 14, 2026. [Online].
Available: https://eepower.com/tech-insights/how-do-renew
ables-affect-grid-reliability/
[9] N. Flores and J. Casey, “Power outages linked to heat and
storms are rising, and low-income communities are most at
risk,” May 2024. [Online]. Available: https://theconversat
ion.com/power-outages-linked-to-heat-and-storms-are-risin
g-and-low-income-communities-are-most-at-risk-228778
[10] N. Coleman, A. Esmalian, C.-C. Lee, E. Gonzales, P. Koirala,
and A. Mostafavi, “Energy inequality in climate hazards: em-
pirical evidence of social and spatial disparities in managed
and hazard-induced power outages,”Sustainable Cities and
Society, vol. 92, p. 104491, 2023.
[11] Z. Zhao, N. Holland, and J. Nelson, “Optimizing smart grid
performance: A stochastic approach to renewable energy
integration,”Sustainable Cities and Society, vol. 111, p.
105533, 2024.
[12] R. El Helou, D. Kalathil, and L. Xie, “Fully decentralized
reinforcement learning-based control of photovoltaics in dis-
tribution grids for joint provision of real and reactive power,”
IEEE Open Access Journal of Power and Energy, vol. 8, pp.
175–185, 2021.
[13] L. Deng, X. Zhang, T. Yang, H. Sun, and S. S. Oren,
“Community energy storage management for welfare opti-
mization using a markov decision process,”arXiv preprint
arXiv:2011.13657, 2020.
[14] T. Wang, H. Liu, and M. Su, “Energy optimization for
microgrids based on uncertainty-aware deep deterministic
policy gradient,”Processes, vol. 13, no. 4, p. 1047, 2025.
[15] M. Krisnawati, Y . P. Mulyani, and B. M. Sopha, “Introducing
adaptive Q-learning in agent-based models: A case study
of household climate decision,” in2025 IEEE International
Conference on Industrial Engineering and Engineering Man-
agement (IEEM). Melbourne, Australia: IEEE, 2025, pp.
704–708.
[16] J. L. San Juan and C. Sy, “A machine learning augmented
game theory-based approach to hybrid renewable energy
system optimization,” in2024 IEEE International Confer-
ence on Industrial Engineering and Engineering Management
(IEEM). Bangkok, Thailand: IEEE, 2024, pp. 97–101.
[17] B. K. Sovacool and M. H. Dworkin, “Energy justice: Con-
ceptual insights and practical applications,”Applied Energy,
vol. 142, pp. 435–444, 2015.
[18] J. Gao, G. Hua, and B. Huo, “Green finance policies for
mitigating energy accessibility inadequacies in china: Empir-
ical insights from a supply chain management perspective,”
IEEE Transactions on Engineering Management, vol. 72, pp.
2381–2391, 2025.
[19] J. Xie and B. Lin, “Government guidance funds and total
factor productivity in renewable energy enterprises: Insights
from financing capability and innovation input structure,”
IEEE Transactions on Engineering Management, vol. 73, pp.
962–973, 2026.
[20] W. Chen, R. Zhu, and J. Chen, “Impact of unit carbon
quota mechanism on clean energy investment strategies: A
biform game analysis,”IEEE Transactions on Engineering
Management, vol. 73, pp. 2924–2938, 2026.
[21] P. J. Burke, J. Widnyana, Z. Anjum, E. Aisbett, B. Resosu-
darmo, and K. G. H. Baldwin, “Overcoming barriers to solar
and wind energy adoption in two Asian giants: India and
Indonesia,”Energy Policy, vol. 132, pp. 1216–1228, 2019.
[22] M. Maulidia, P. Dargusch, P. Ashworth, and F. Ardiansyah,
“Rethinking renewable energy targets and electricity sector
reform in Indonesia: A private sector perspective,”Renewable
and Sustainable Energy Reviews, vol. 101, pp. 231–247,
2019.
[23] A. B. Setyowati, “Mitigating inequality with emissions? Ex-
ploring energy justice and financing transitions to low carbon
energy in Indonesia,”Energy Research & Social Science,
vol. 71, p. 101817, 2021.
