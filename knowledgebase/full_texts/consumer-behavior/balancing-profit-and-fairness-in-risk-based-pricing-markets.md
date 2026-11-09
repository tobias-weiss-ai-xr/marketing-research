---
title: Balancing Profit and Fairness in Risk-Based Pricing Markets
url: https://arxiv.org/abs/2506.00140
category: consumer-behavior
subcategory: empirical
date: 2025-05
venue: ''
authors:
- Jesse Thibodeau
- Hadi Nekoei
- Afaf Taïk
- Janarthanan Rajendran
- Golnoosh Farnadi
source: arxiv
pdf_url: https://arxiv.org/pdf/2506.00140
pages: 11
chars: 50486
fetched_at: '2026-11-08T13:09:36+00:00'
kb_version: 1
---

# Balancing Profit and Fairness in Risk-Based Pricing Markets

arXiv:2506.00140v2  [cs.AI]  4 Jun 2025
Balancing Profit and Fairness in Risk-Based Pricing Markets
Jesse Thibodeau1, Hadi Nekoei1,2, Afaf Ta¨ık1,2, Janarthanan Rajendran3, Golnoosh Farnadi1,4
1Mila - Qu´ebec AI Institute
2Universit´e de Montr´eal
3Dalhousie University
4McGill University
{jesse.thibodeau, nekoeihe, afaf.taik, farnadig }@mila.quebec
janarthanan.rajendran@dal.ca
Abstract
Dynamic, risk-based pricing can systematically exclude vul-
nerable consumer groups from essential resources such as
health insurance and consumer credit. We show that a reg-
ulator can realign private incentives with social objectives
through a learned, interpretable tax schedule. First, we pro-
vide a formal proposition that bounding each firm’s local
demographic gap implicitly bounds the global opt-out dis-
parity, motivating firm-level penalties. Building on this in-
sight we introduce MarketSim—an open-source, scalable
simulator of heterogeneous consumers and profit-maximizing
firms—and train a reinforcement learning (RL) social plan-
ner (SP) that selects a bracketed fairness-tax while remaining
close to a simple linear prior via anℓ1 regularizer. The learned
policy is thus both transparent and easily interpretable. In two
empirically calibrated markets, i.e., U.S. health-insurance and
consumer-credit, our planner simultaneously raises demand-
fairness by up to 16% relative to unregulated Free Market
while outperforming a fixed linear schedule in terms of social
welfare without explicit coordination. These results illustrate
how AI-assisted regulation can convert a competitive social
dilemma into a win–win equilibrium, providing a principled
and practical framework for fairness-aware market oversight.
1 Introduction
Firms equipped with modern computational power and ex-
tensive consumer data logs may reap financial gains by
adopting dynamic (or personalized) pricing, which tailors
prices to potential customers or customer segments based
on their estimated willingness-to-pay. This approach en-
ables firms to extract the greatest economic value from con-
sumer data. From an efficiency perspective, dynamic pric-
ing has been shown to boost firm profitability and acceler-
ate sales speeds (Schlosser and Boissier 2018; Wang et al.
2023). However, its welfare implications are less consis-
tent. In some markets, including insurance and lending,
dynamic pricing can yield undesirable distributional out-
comes (Zhu et al. 2023; Betancourt et al. 2022). For in-
stance, while health insurers often rely on dynamic pricing,
recent census data indicate that members of the Hispanic
population in the U.S. are, on average, roughly twice as un-
likely to have healthcare coverage as members of the Afro-
descendent population, who in turn are twice as unlikely as
members of the Caucasian and Asian populations (Martinez
2022; Keisler-Starkey, Bunch, and Lindstrom 2024). Simi-
larly, data reveal a negative correlation between likelihood
of coverage and income, and since income and ethnicity
are themselves correlated, there are justifiable concerns that
healthcare coverage may be systemically biased.
White Black Asian
Hispanic (any race)
7
11.1
6.8
23.6
% Uninsured
Race & Hispanic Origin
Lowest quintileSecond quintileThird quintileFourth quintileHighest quintile
21.2 18.8
13.1
7.4
3.8
Income
Figure 1: Percentage of working-age adults without health
insurance in 2023, by race and income.
Beyond this, substantial price discrepancies between
consumers may also give rise to perceptions of unfair-
ness (Lee, Illia, and Lawson-Body 2011), potentially
discouraging market participation and perpetuating existing
disparities. Moreover, in markets where personal assets can
be leveraged to negotiate more favourable terms, goods may
become relatively more affordable for higher-income con-
sumers. In such scenarios, scarce goods tend to be allocated
to privileged groups, leaving fewer units—or lower-quality
alternatives—to those with fewer resources. This pattern is
well documented in the lending market, where it amplifies
wealth gaps (for example, through restricted access to home
equity) and drives gentrification. Similar issues arise in
sectors such as education services and public transportation,
where buyer distributions should ideally reflect those of the
underlying population.
Dynamic pricing typically enables firms to set prices
for different consumer segments in order to maximize the
expected profits derived from each. Thus, a firm adopting
dynamic pricing rarely accounts for its resulting buyer
distribution, which can be considered unfair if it diverges
too sharply from that of the broader population. In this

study, we explore the challenge of dynamic pricing, and
specifically that of regulating its use under demand fairness
criteria in markets where buyer distributions should mirror
those of the underlying population. Motivating this, we
first demonstrate how profit-maximizing price allocations
fail to satisfy demand fairness under purely competitive
or collusive dynamics. Broadly, we recognize that it is
unrealistic to expect a profit-maximizing firm to voluntarily
consider fairness notions in its pricing strategy. Therefore,
we consider how a benevolent social planner (SP) might use
policy tools such as taxation to encourage market participa-
tion among underrepresented consumer groups and penalize
unfair firm behavior. To achieve this, we use reinforcement
learning to train an SP capable of devising financial incen-
tives that promote demand fairness—namely, by shrinking
market opt-out disparities between population subgroups.
To conduct our experiments, we introduce MarketSim,
a simple yet robust and scalable simulation framework
wherein arbitrarily many firms engage in price Free Market
to capture a market of arbitrarily many consumer profiles
with heterogeneous utility. Our findings indicate that
social welfare can be enhanced by taxing firms in ways
that incentivize fairer market-specific conduct . Further,
by endowing the learning agent with a domain-specific
prior, we observe that interpretability can be maintained
at the policy level, confirming the effectiveness of our
approach at solving specific markets while retaining certain
desirable properties such as tax monotonicity. Contributions
of our work include:
• A formal demonstration of how local, firm-level incen-
tives can satisfy a global fairness criterion and thereby
raise social welfare in a setting of multiple self-interested
stakeholders with incomplete information.
• The introduction of MarketSim, a robust and easy-to-
use open-source simulator for experimenting with vari-
ous market dynamics and regulatory policies imposed on
arbitrarily many heterogeneous firms and consumers, and
evaluating their welfare implications.1
• An application of reinforcement learning to generate
optimal regulatory policies in two different instances
of MarketSim (replicating the markets for insurance
and consumer credit), showing that we can incentivize
welfare-improving firm behaviour in each market, while
retaining policy interpretability.
2 Related Work
The interdisciplinary nature of this work requires a review
of topics from economics, specifically in the subfields of
welfare economics and consumer choice theory, as well as a
broad overview of applications of artificial intelligence (AI)
to welfare economics.
2.1 Economics Foundations
In this work, we explore consumer choice and pricing dy-
namics in competitive markets with heterogeneous agents.
1Code will be made publicly available upon acceptance of this
work.
On the demand side, consumers exhibit varying sensitivities
to price fluctuations, while on the supply side, firms face het-
erogeneous marginal costs that proxy for technological and
scale advantages. Our demand system borrows the random-
utility framework of Berry, Levinsohn, and Pakes (1993), yet
departs from it in two key respects: first, we replace perfectly
rational choice with a stochastic rule that captures bounded
rationality and behavioural noise; second, we model multi-
ple competing firms rather than a representative producer,
thereby enabling firm-level strategic interaction. These ex-
tensions link our analysis to early work on preference het-
erogeneity by Becker (1962) and its discrete-choice formal-
isation by McFadden (1972), whose insights remain central
to modern consumer-choice theory (Ben-Akiva et al. 2002).
Finally, following the process-based welfare view of Fleur-
baey (2008), we evaluate outcomes not only by efficiency
but also by the fairness of the mechanisms that generate
them, an angle largely absent from the original random-
utility literature.
2.2 Fairness in Dynamic Pricing
The welfare-theoretic study of price design has migrated
from economics to operations research (Gallego, Topaloglu
et al. 2019) and computer science (Das et al. 2022), giv-
ing rise to a rich taxonomy of fairness definitions. Co-
hen, Elmachtoub, and Lei (2022) prove that price, demand,
consumer-surplus, and no-purchase fairness cannot be si-
multaneously satisfied in dynamic settings; we therefore
adopt demand fairness (Cohen, Elmachtoub, and Lei 2022;
Kallus and Zhou 2021), which directly measures disparate
impact on group participation and is well motivated in edu-
cation, consumer credit and healthcare domains. Alternative
notions such as proportional fairness (Bertsimas, Farias, and
Trichakis 2011) highlight welfare trade-offs but do not read-
ily extend to sequential, multi-firm games. RL approaches
such as Maestre et al. (2019) impose fairness via Jain’s index
under monopoly; in contrast, our regulator shapes compet-
itive firms’ incentives so that they voluntarily choose fairer
prices, thereby filling the gap between single-seller RL treat-
ments and static constrained-optimisation models.
2.3 AI for Economic Policy Generation
The closest application to our work combining economic
simulations and sequential modelling is the AI Economist
(Zheng et al. 2020), where agents interact in a simulated
gather-build-trade society, while a social planner aims to
learn an income taxation strategy that improves social wel-
fare, defined as the product of equality and economic pro-
ductivity. While their work is effective at showcasing emer-
gent behaviours among simulated consumer-workers under
incumbent tax regimes, we introduce a new layer to our ex-
ploration which instead focuses on how a dynamic regula-
tor can impact societal outcomes by aligning the objectives
of self-interested firms with its own. Further, our work fo-
cuses on markets involving dynamic pricing, where firms
assign prices based on consumer group membership. This
added complexity allows for a deeper analysis of firm re-
sponses to incumbent policy frameworks. In addition, we

refer to the safe RL literature to impose domain-specific pol-
icy constraints in order to maintain a degree of interpretabil-
ity, which is critical for the widespread adoption of AI-
generated public policy. In fact, safe RL methods routinely
incorporate domain constraints to ensure an agent’s policy
remains feasible or respects regulatory standards (Garcıa
and Fern´andez 2015). These constraints can be implicit (e.g.,
penalizing the agent for violating constraints) (Achiam et al.
2017). By tethering our AI regulator’s reward function to a
baseline monotonic schedule, we encourage the learned reg-
ulatory policy to align with essential policy norms, namely,
that higher fairness should generally not be penalized by
higher tax rates, while preserving the safety and inter-
pretability required in real-world economic regulation.
3 Preliminaries
We provide an overview of notation and definitions referred
to throughout the remainder of this work. Among these, we
refer to local and global notions of fairness within this con-
text. Further, we motivate our policy mechanism design by
demonstrating how local fairness incentives have global fair-
ness implications. Going forward, let A be a random vari-
able representing a consumer profile, taking values in the set
A = {1, . . . , m}, and let F be a random variable denot-
ing the firm selected by a given consumer, taking values in
F = {0, . . . , n}, with F = 0 referring to opting out of the
market.
3.1 Definitions and Fairness Metrics
Definition 1 (ϵ-Local Fairness). For any firm j ∈ F, and
for any consumer profile pair i, k∈ A, we say that firm j is
ϵ-locally fair if
max
i,k

Pr(F = j | A = i) − Pr(F = j | A = k)

 ≤ ϵ.
Remark. When ϵ = 0, it means that every consumer group’s
consumption choice is conditionally independent from their
group membership.
We quantify market-wide fairness via the opt-out disparity
between consumer groups, which we call global fairness
in order to relate it to its local counterpart. This definition
draws on demand fairness, proposed by Cohen, Miao, and
Wang (2021).
Definition 2 (ϵ–Global Fairness ). The entire market is
ϵ–globally fair if the opt-out rate is (approximately) pro-
file–independent:
max
i,k

Pr(F = 0 | A = i) − Pr(F = 0 | A = k)

 ≤ ϵ.
Remark. When ϵ = 0, every profile opts out with exactly the
same probability, i.e. P r(F = 0) is constant in A. This re-
sult is akin to demographic parity (Dwork et al. 2012), where
profile i ⊥ ⊥firm j.
3.2 Fairness alignment
Local and global fairness capture different levels of dis-
crimination, though both measurements have shortcomings
if considered on their own. On one hand, perfect local fair-
ness fails to capture consumer counts, that is, a firm’s con-
sumers can mirror the population while including very few
in total. Similarly, global fairness is satisfied under no mar-
ket participation, i.e. the case where everyone opts out. Thus,
any policy objective involving global fairness should also in-
clude some notion of economic productivity. Further, global
fairness does not imply local fairness and is not directly
addressable. Figure 2 illustrates a market in which global
fairness holds—both consumer profiles opt out ∼ 20 % of
the time—yet the two firms serve very different mixes of
profiles ( F1 serving A1 and F2 serving A2), violating lo-
cal fairness. How then can an external regulator, unable to
F2 F1 A1
F2 F1 A2
Figure 2: Perfect global fairness does not imply local fair-
ness.
address global fairness explicitly, make global fairness im-
provements by deploying firm-level incentives? This chal-
lenge constitutes a mechanism design problem, which we
formalize as an optimization problem in the following sec-
tion.
3.3 From Local to Global Fairness
We first show that enforcing an ϵ–local–fairness constraint
on each firm automatically bounds the market-wide opt-out
disparity. The result motivates our policy design: penalties
can be assessed at the firm level, yet they control the global
metric of interest.
Proposition 1 (Local ⇒ Global Fairness Bound) . If every
firm j ∈ {1, . . . , n} satisfies the local-fairness condition
max
i,k∈A

Pr(F = j | A = i) − Pr(F = j | A = k)

 ≤ ϵ,
then the market is ε′-globally fair, i.e.

Pr(F = 0 | A = i)−Pr(F = 0 | A = k)

 ≤ ε′ ∀ i, k∈ A,
with
ε′ = min { nϵ, 1 } .
Proof. For brevity write pj|i := Pr( F = j | A = i). The
hypothesis gives |pj|i − pj|k| ≤ϵ for every firm j ≥ 1 and
every pair of profiles i, k.
From local to opt-out gap. Because the opt-out probability
is the complement of the in-market mass,
p0|i = 1 −
nX
j=1
pj|i, p 0|k = 1 −
nX
j=1
pj|k.
Hence
|p0|i − p0|k| =

 nX
j=1
(pj|k − pj|i)

 ≤ nX
j=1
|pj|k − pj|i| ≤ nϵ.

Probabilistic range. Because each p0|· is a probability, their
difference cannot exceed 1: |p0|i − p0|k| ≤1.
Combining the two bounds,
|p0|i − p0|k| ≤ min{ nϵ, 1 },
which yields the stated ε′.
Policy insight. Because global fairness follows directly
from firm-level constraints, a regulator can simply penal-
ize firms based on their own ϵ–local gap; no market-wide
coordination term is needed. This concludes the motivation
for our social planner’s policy mechanism. In the following
section, we outline the market environments in which policy
explorations take place.
4 Market Environment
We model an oligopolistic market with heterogeneous con-
sumers and profit-maximizing firms. We then introduce a so-
cial planner whose policy consists of a bracketed tax sched-
ule to incentivize fairness. An illustration of this market can
be found in Figure 3. We proceed with formal definitions for
our simulated agents.
4.1 Consumers
Each consumer profile i obtains utility
Ui,j = α − βi pi,j
from consuming firm j’s product, where αj is base prod-
uct utility, βi is the price sensitivity of profile i, and pi,j is
the per-profile price. For the outside option F = j = 0 ,
let Ui,0 = α0. A consumer of profile i chooses among
{0, . . . , n} with probability
pj|i = exp

Ui,j

nX
j=0
exp

Ui,j
 .
4.2 Firms
Each firm j ∈ {1, . . . , n} may compute its expected profit:
E[Πj] =
mX
i=1
pj|i

pi,j − mci,j

,
where mci,j is the average marginal cost for profilei. Under
free-market dynamics, firm j’s problem is
max
{pi,j }
E[Πj] subject to 0 ≤ pi,j ≤ pmax.
Due to the inherent jump discontinuities in consumer
choices under Free Market, firms solve for prices using Pow-
ell’s derivative-free method (Powell 1964) in the SciPy
Python optimization library (Virtanen et al. 2020). While we
found this to achieve better stability, we note that alternative
optimization methods may be used to solve the firms’ prob-
lem.
4.3 Social Planner and Welfare Maximization
We now introduce a social planner who aims to maximize
overall social welfare, a hybrid measure of fairness and firm
profits. To maintain policy interpretability, we also penalize
large deviations from a simple,naive bracketed-tax baseline.
Bracketed Fairness Tax. To incentivize firms to adopt
fairer outcomes, we partition the fairness range [0, 1] into B
brackets, each of width 1/B. Suppose firm j achieves fair-
ness fj ∈ [0, 1] and hence belongs to bracket bj, defined
by
fj ∈
h
bj −1
B , bj B

.
We index tax brackets by b ∈ {1, . . . , B} and associate to
each bracket a rate τb ∈ [0, 1]. In general, we collect these
into the vector
τ = [τ1, . . . , τB] ∈ [0, 1]B.
A firm in bracket bj thus faces an effective per-profile mar-
gin

pi,j −mci,j

1−τbj

. Consequently, under regulation,
firm j’s profit-maximization problem becomes
max
{pi,j }
E[Πj]

1 − τbj

, p min ≤ pi,j ≤ pmax.
Social Welfare Objective. Let W

τ

be the total social
welfare,
W

τ

=
 1
n
nX
j=1
E[Πj]

1 − τbj

× fairnessglobal

τ

,
capturing both global fairness (measured via the gap pre-
sented in Definition 2) and net firm profits (under the cho-
sen τ ). We note that this multiplicative welfare expression
is one of many possible ways to combine fairness and profit,
however the intuition here is that fairness ∈ [0, 1] effec-
tively scales profit. A similar formulation of welfare is used
in (Zheng et al. 2020). The planner’s goal is to select τ to
solve maxτ W

τ

. To this end, we use a soft actor-critic al-
gorithm (Haarnoja et al. 2018) to train an RL agent whose
reward is W

τ

.
In Algorithm 1, we outline the simultaneous Nash Free Mar-
ket in which firms select prices to optimize for profit given a
policy generated by the social planner.
5 Market Parameterization and Empirical
Results
We consruct two market environments,health insurance and
consumer lending , because both combine risk-based pric-
ing with pronounced distributional concerns. Income-group
proportions follow Pew Research Center (2024); insurance-
coverage rates draw on Keisler-Starkey, Bunch, and Lind-
strom (2024); and home-ownership patterns (a proxy for
credit demand) follow U.S. Census Bureau (2023). The pop-
ulation is divided into High, Middle, and Low income seg-
ments, each assigned a price elasticity (β) and a firm-specific
marginal cost (mc). These parameters, which can be found
for both markets in table 1, introduce system-wide hetero-
geneity.

Figure 3: A dynamic-pricing market consisting of 3 agent types, each with their own optimization objective. The social planner
generates welfare-maximizing tax schedules applied to firms based on their local fairness gap. Firms then compute their best
responses and assign consumer group-level prices. Finally, consumers make their selection from these prices.
Why heterogeneity matters. Heterogeneity arises among
both agent participant types in the market and shapes every
dimension of the policy problem:
• Consumers. Differences in disposable income, outside
options, and risk exposure create a spread of price elastic-
ities. In insurance, demand is relatively inelastic at higher
incomes because coverage quality is valued more than
marginal dollars. In credit, by contrast, wealthier house-
holds can leverage their assets to negotiate better terms,
pay cash or source cheaper capital altogether, making
them more price-sensitive. Such a cross-market reversal
broadly illustrates how elasticity is a joint outcome of
preference intensity and available substitutes.
• Firms. Marginal cost is tightly linked to borrowers’ or
policyholders’ income. Low-income consumers are gen-
erally riskier to serve as they face higher job volatil-
ity, have thinner financial buffers (Bertoletti, Borraz, and
Sanroman 2024; Fout et al. 2020), and—in the case of
health insurance—experience more occupational hazards
and reduced access to preventive care (Nicholson, Bunn,
and Costich 2008). These factors translate into (i) higher
expected claim costs for insurers and (ii) elevated de-
fault probabilities for lenders, raising the average per-
unit cost of coverage or credit. By contrast, high-income
consumers offer steadier cash flows, better health pro-
files, and superior collateral, enabling firms to price at
lower cost. Even within a single industry, providers dif-
fer in their ability to manage this risk—large insurers
leverage pooled data and predictive analytics, whereas
smaller or niche firms often specialize in higher-risk
pools—amplifying cost dispersion and strategic asym-
metry.
From a regulatory standpoint, it is important to consider
both sources of heterogeneity in order for policies to achieve
realistic social welfare improvements. Our bracketed tax
is therefore designed to be piecewise—simple enough for
transparency yet flexible enough to align marginal incentives
across diverse firms. We compare three baselines:
• Free Market: Firms compete in a simultaneous price-
setting game with the aim of maximizing their individual
profits in the absence of policy intervention.
• Linear regulation: a monotonic, bracketed linear tax
τ base b = 1 − b B , for b = 1, . . . , B.
intended as a hand-crafted fairness correction. Intuitively,
this baseline approximates a simple rule ( τ = (1 −
fairness)), discretized into B brackets.
• Collusion: Firms jointly maximize aggregate profit. This
benchmark reveals the upper bound on total profitability
under perfect coordination, and can be seen as an oracle
case for profit.
For these benchmarks, we report outcomes after conver-
gence to Nash equilibrium prices.
Demand elasticity. Elasticity captures both willingness
and ability to substitute. For health insurance, the ab-
sence of close substitutes renders wealthier consumers less

Algorithm 1: Multi-Agent Price-Setting Game
1: Input:
2: Number of firms n (indexed by j); consumer profiles
i = 1, . . . , mwith size Si and price sensitivity βi;
3: Base utility αj for each firm j; outside option utility
α0;
4: Tax brackets τ = [ τ1, . . . , τB] set by planner;
marginal costs mci,j.
5: Initialize:
6: Each firm j has prices pi,j (possibly random or pre-
viously set).
7: Step 1: Social Planner Sets Tax Policy
8: for j ← 1 to n do
9: Compute fairness fj for firm j
10: Assign bracket bj ← bracket index such that fj ∈h
bj −1
B , bj B

11: Set effective tax rate τbj for firm j
12: end for
13: ▷ Firm j’s margin becomes (pi,j − mci,j)(1 − τbj )
14: Step 2: Firms Simultaneously Update Prices
15: for j ← 1 to n do
16: pi,j ← arg maxpi,j
Pm
i=1 pj|i · (pi,j − mci,j)(1 −
τbj ) · Si
17: ▷ Firm j chooses prices to maximize expected profit
18: end for
19: Step 3: Consumers Choose Firm or Outside Option
20: for i ← 1 to m do
21: for j ← 1 to n do
22: Ui,j ← αj − βi pi,j
23: end for
24: Ui,0 ← α0
25: pj|i ← exp(Ui,j ) exp(Ui,0)+Pn k=1 exp(Ui,k) ∀j
26: end for
27: Step 4: Outcome and Payoffs
28: for j ← 1 to n do
29: Demandi,j ← Si · pj|i ∀i
30: Πj ← Pm i=1(pi,j − mci,j)(1 − τbj ) · Demandi,j
31: end for
32: Step 5: End of Game
33: Output final τ , prices {pi,j}, demands, and profits
{Πj}.
price-responsive. In credit, abundant alternatives (e.g. home-
equity lines, credit cards, or abstention) make the same
group more price-elastic, whereas low-income borrowers
confront a near take-it-or-leave-it contract.
Marginal cost. Risk-adjusted cost falls with income in
both markets but for distinct reasons: fewer costly medical
claims in insurance, and lower default probabilities in lend-
ing. Firms, heterogeneous in ressources and capability, mod-
ulate these costs further.
Finally, the social planner learns a piecewise-constant tax
via Soft Actor–Critic (Table 2). By explicitly targeting cross-
Insurance Credit
Group N β mc 1 mc2 β mc 1 mc2 mc3 mc4 mc5
High (H) 200 0.25 2.50 2.25 3.00 0.40 0.65 0.45 0.60 0.44
Middle (M) 520 0.70 3.00 2.75 2.70 1.20 1.45 1.12 1.35 1.29
Low (L) 280 0.825 3.50 3.25 2.25 2.05 2.30 2.25 2.28 2.10
Table 1: Baseline demand elasticities and marginal costs.
The insurance market is modelled with two competing in-
surers, and the credit market with five lenders. Price bounds
are Pmin = 1, Pmax = 20.
Shared social-planner parameters
Algorithm Brackets B τ min τmax λins/λcred
SAC 20 0% 100% 100 / 10
Table 2: Social-planner initialization parameters.
segment disparities, the learned policy reflects heterogeneity
on both the consumer and the firm side, in contrast to the
na¨ıve linear schedule.
ℓ1 Penalty on Deviation from Baseline. To retain policy
interpretability, we penalize the planner for learning a tax
schedule τ that deviates excessively from the naive baseline.
Specifically, we add an ℓ1 regularizer
λ
BX
b=1

 τb − τ base b

,
where λ ≥ 0 tunes how much the planner is incentivized
to remain close to τ base. Thus, the planner tweaks the naive
schedule only to the extent that it increases overall social
welfare. This can be interpreted as an “expert planner” ca-
pable of taking a known policy mechanism understood by
domain experts and adapting it to specific markets. The so-
cial planner’s full optimization problem is therefore
max
τ
"
W

τ

− λ
BX
b=1

τb − τ base b

#
.
Hence, while large deviations from the baselineτ base are pe-
nalized, the planner retains the flexibility to adjust tax rates
to increase overall social welfare (e.g., by nudging firms to-
ward more equitable pricing where the naive schedule is sub-
optimal).
5.1 Case Study 1: Health Insurance
Market Overview and Motivation. Census data report
7.9% of the U.S. working population uninsured ( ∼25M).
Though law-abiding insurance providers do not explicitly
use sensitive attributes in the determination of premia, these
can often be inferred from occupation and ZIP code (Dwork
et al. 2012; Barocas and Selbst 2016), making health insur-
ance an ideal market for dynamic regulation. As mentioned,
this instance of our simulation represents a market for a ne-
cessity good, and thus we endow low-risk profiles with low
demand elasticity, and high-risk profiles with high demand
elasticity.

Policy Generation and Empirical Results. Use of our
method to regulate the health insurance market yields sub-
stantial welfare gains over benchmarks. We measure net
profit (after tax), fairness, and social welfare at both the
per-firm and global level. Table 3 (left) shows the outcomes
under four market regimes: (Free Market) purely competi-
tive, (Linear-SP) a simplistic bracket policy with fixed cut-
offs, (RL-SP) our proposed social planner, and (Collusion),
a stable cartel-like coordination (used solely for revealing
an upper bound on profit from which we provide normal-
ized profit values for the benchmarks of interest). From re-
sults, we note that the RL method achieved the highest social
welfare, not only by improving fairness, but also in improv-
ing total market profitability, indicating that it was able to
mitigate the social dilemma inherent to competitive games,
instead forcing firms into a kind of policy-induced tacit co-
operation that makes the market more stable and friendly
to consumers. This is evidence that a fairness-seeking pol-
icy can outperform selfish Nash firms in terms of aggre-
gate profits, suggesting that the RL policy might act as an
implicit coordination device, getting firms closer to the co-
operative outcome without explicit collusion. Broadly, our
RL social planner improved social welfare in the market for
health insurance compared to the baseline competitive case
by approximately 11%, and outperformed the linear policy
by 10%. After 2M training steps, the RL social planner con-
verged to the policy found in Figure 4a, with which, as seen
in Table 3 ( left), it was able to funnel firms into welfare-
improving fairness brackets. Further, providing the agent
with an intuitive prior allowed it to maintain interpretability
in brackets with few or no training examples. Specifically,
it tweaked the Linear-SP baseline in fairness areas where it
was able to achieve substantial welfare gains.
5.2 Case Study 2: Consumer Credit
Market Overview and Motivation. A second key appli-
cation of our framework pertains to consumer credit, where
financial institutions offer loans or lines of credit to hetero-
geneous borrowers through competitive interest rates. Un-
like health insurance, credit is generally less “essential” yet
the stakes remain high for consumers with limited collateral
or volatile income. For these groups, restricted credit access
can hamper opportunities to secure home equity, reinforcing
wealth gaps. As such, credit markets present a core tension
between risk-based pricing (necessary for profitable lend-
ing) and equitable access (necessary for social welfare and
fairness), making them an ideal testing ground for dynamic
regulation.
Policy Generation and Empirical Results. We evaluate
the outcomes of our credit market simulation across the
same four market regimes, though in this instance each as-
sessed over five firms. In this market, we observe a quali-
tatively similar dynamic to the insurance scenario: the RL
social planner consistently improves upon linear policy in-
terventions and competitive baselines, even in a setting with
greater firm heterogeneity and tighter fairness-profit trade-
offs. Evaluated over five competing lenders, Table 3 (right)
shows that the competitive market yields high profit levels
(a) Taxation policy generated by the RL social planner for the insur-
ance market.
(b) Taxation policy generated by the RL social planner for the credit
market.
Figure 4: Comparison of policy generation across two dif-
ferent markets: Insurance (a) and Credit (b).
(0.630) but suffers from low fairness (0.660). The Linear-SP
baseline improves fairness to 0.712 but imposes a blunt re-
striction on risk-based interest rates, thereby driving down
profits and yielding modest improvements in participation.
By contrast, the RL policy exhibits adaptive behaviour,
learning market-specific bracket assignments that improve
fairness further (0.767) while also maintaining profitability
approaching that of the Free Market baseline. However, we
note an increase in the global opt-out rate under the RL pol-
icy, a result discussed further in the next section. Nonethe-
less, overall social welfare increases to 0.477, reversing the
decline observed under the Linear-SP baseline (0.392). This
represents social welfare gains of 15% and 22% over the
competitive and Linear-SP baselines, respectively.
Altogether, these results confirm that an RL-based regula-
tor can foster an equilibrium where profitability and fairness
minimally conflict.
6 Discussion
A notable aspect of our experiments is how tacit coopera-
tion emerges within certain policy frameworks, evidenced
by how markets under the RL policy yield comparable or
even higher profits than under unregulated Free Market. This
is indicative of a social dilemma in unregulated Free Mar-

Insurance Credit
Free Market Linear-SP RL-SP Collusion Free Market Linear-SP RL-SP Collusion
Profit ↑ 0.697 0.642 0.707 ± 0.002 1.0 0.630 0.551 ± 0.003 0.622 ± 0.003 1.0
Fairness ↑ 0.821 0.895 0.895 0.851 0.660 0.712 ± 0.006 0.767 ± 0.004 0.709
Opt Out ↓ 0.137 0.120 0.121 0.335 0.173 0.1593 ± 0.002 0.218 ± 0.002 0.395
Welfare 0.572 0.575 0.633 ± 0.002 0.851 0.416 0.392 ± 0.004 0.477 ± 0.003 0.709
Table 3: Comparison of Profit, Fairness, and Welfare across market scenarios and dynamics. We include market-wide opt-out
rates to broadly outline market outcomes. Profit values are normalized with respect to the theoretical maximum determined by
the collusive (oracle) market setting. We report standard errors (SE) over 5 seeds, and omit SE values under 0.001.
ket: profit-maximizing individual firm behavior reduces ag-
gregate profits. Meanwhile, by coordinating firm incentives,
the regulator resolves this inefficiency, while simultaneously
aligning firm and consumer welfare. Crucially, this “cooper-
ation” among firms is driven not by explicit collusion, but
instead by an understanding of specific market dynamics ac-
quired by the social planner, allowing it to design incentives
which mirror cooperation. From a policy perspective, these
insights suggest that partial regulation in the form of adap-
tive bracket constraints that do not artificially cap or flatten
prices can be more attractive than rigid price bounds or un-
regulated Free Market. This approach preserves profitabil-
ity for firms while simultaneously broadening access and
mitigating discriminatory pricing. In practice, such bracket
tuning could be made transparent to both firms and policy-
makers, enabling oversight of how fairness categorizations
evolve over time.
18
10 10
15
22
15 15
40
13 13 13
33
4 5 5
25
Low Middle High
Free Market Linear-SP RL-SP Collusion
34 29 19
29
37 32 35
54
12 12 18
37
3 3
16
25
Opt-out probability (%)
Health InsuranceConsumer Credit
Figure 5: Mean consumer-group opt-out rates under multi-
ple market frameworks. The arrow indicates the maximum
difference in opt-out rate means between population groups.
By global fairness, lower is better.
Despite obtaining welfare improvements with our RL
method, we deem it necessary to highlight a shortcoming re-
garding our fairness criterion. While demand fairness advo-
cates for equal access to goods (as doesdemographic parity,
it is insufficient on its own at ensuring that consumer par-
ticipation rates improve, as it simply requires that they be
agnostic to group membership, with no weight accorded to
their actual values. From Table 3, we find that fairness un-
der collusion, an illicit market practice in most jurisdictions,
actually outperforms Free Market in both markets, despite
yeilding the highest opt out rates by a substantial margin.
This is not because it truly encourages participation among
underrepresented groups, but because it simply makes all
consumers more equally unlikely to participate. This is ev-
ident from Figure 5, where we report group-level opt-out
rates. From these, we observe that this share is higher for
each subgroup under collusion. We note further that, under
the RL policy, there are reductions in opt-out rates among
the low-income group in both markets compared to Free
Market, albeit at the cost of an opt-out rate increase among
the high and middle-income groups. Thus, it is important
to examine resulting market distributions in order to qual-
itatively assess the impact of policy generations. Broadly,
while equal access is a desirable goal, it should not come
in the form of increased exclusion. A fairness criterion that
improves parity in access but leads to a larger number of
individuals being priced out or discouraged from partici-
pation can ultimately exacerbate structural harms and de-
crease overall social welfare. To alleviate this concern, one
might consider alternate metrics, such as consumer surplus
fairness (Cohen, Miao, and Wang 2021), which, when us-
ing our probabilistic setting, can be defined via the log-sum
rule (Small and Rosen 1981) as

maxi CS (τ )i − mink CS (τ )k

 ≤ ϵ, ∀ i, k,
where
CS (τ )i = 1 βi log  NX j exp(αj − βipi,j)  .
Accordingly, MarketSim makes it straightforward to swap
any welfare metric desired by the user and evaluate out-
comes in terms of firm performance and consumer distri-
bution.
6.1 Ablation Study: Market Bounds on Fairness
While fairness, according to our local and global definitions,
has a theoretical upper bound of 1.0, the empirical upper
bound is largely dependent upon market dynamics and pa-
rameter initializations. Thus, to uncover the empirical upper
bounds on fairness in both markets, we train a new social
planner with the sole objective of maximizing global de-
mand fairness with no weight on profit. Results reveal that
our instance of the market for insurance has an empirical up-
per bound on global fairness of 0.895, which was achieved

Insurance Credit
Firm A 0.947 0.823
Firm B 0.947 0.885
Firm C - 0.793
Firm D - 0.902
Firm E - 0.763
Global 0.895 0.791
Table 4: Local and global fairness values under a fairness-
maximizing SP tax policy.
by both Linear-SP baselines and welfare-maximizing RL
policies. Meanwhile, in the credit market, our fairness-
maximizing SP reveals an empirical upper bound of 0.791,
which was approached but never achieved by our welfare-
maximizing SP. This can influence the degree of improve-
ment one can expect when experimenting with regulatory
frameworks in MarketSim.
7 Runtime & Scalability of MarketSim
We explore runtimes to demonstrate the approximately-
linear scalability of price Free Market in MarketSim, re-
porting wall-clock convergence times on markets of 2 to
100 firms. As the number of participating firms may vary
between markets, our simulation should scale well over a
broad range of firm counts. For instance, 80% the U.S.
0 20 40 60 80 100
0
1
2
3
4
5
Number of Firms
Mean Runtime (s)
Figure 6: Mean wall-clock runtime per 10 rounds as a func-
tion of the number of firms (on CPU). Error bars represent
standard deviation over 5 seeds.
health insurance market is dominated by 10 firms, with 57%
concentrated in the top 3 (American Medical Association
2023). Meanwhile, the credit market is more fragmented,
with many non-bank lenders making up 65% of the mort-
gage lending market (Chopra 2024). Conversely, 70% of
the credit card market is dominated by 5 issuers (McCann
2025), indicating a broader range for participation within
lending markets. MarketSim nonetheless accommodates
arbitrarily many firms and consumers, with runtimes scaling
linearly.
Limitations and Future Work. While these findings of-
fer promising evidence, we highlight several directions for
further inquiry:
1. Multi-step Taxation Dynamics: While this work fo-
cused on a single-step taxation policy, an exciting di-
rection for future research is to frame taxation as a se-
quential decision-making task. Such settings could fur-
ther emphasize the advantages of RL approaches.
2. Data Quality and Bias: Real-world transactional
datasets often contain inaccuracies, missing fields, or his-
torical biases, which could skew bracket assignments. In-
vestigating robustness under such conditions remains an
essential next step.
3. Bracket Design: We implement a straightforward
bracket structure here. Future work might explore more
sophisticated, flexible brackets or alternative reward
functions that accommodate multiple fairness definitions
or risk preferences.
4. Legal and Ethical Context: As bracketed interventions
shape competitive behavior at scale, deeper analysis is
warranted to confirm compatibility with antitrust laws
and to guard against new forms of collusion or bias.
In summary, our case studies demonstrate that dynamic
bracket regulation can notably enhance fairness and welfare
in a competitive market scenario feature dynamic pricing
with heterogeneous firms and consumer profiles. By align-
ing private incentives with public interest goals, RL-driven
brackets exemplify a viable pathway toward more inclusive
market systems for essential products and services.
8 Conclusion
In this work, we explore social welfare outcomes under var-
ious policy mechanisms in markets featuring risk-based dy-
namic pricing. We mathematically demonstrate the relation-
ship between local and global notions of fairness, thereby
motivating a firm-level policy approach. We then introduce
MarketSim, a simulator for risk-based dynamic pricing,
which we render open-source. Finally, we reproduce two
distinct real world markets where global opt-out gaps have
been empirically recorded (health insurance and consumer
credit) and demonstrate how RL can be successfully lever-
aged to generate interpretable policy mechanisms aimed at
improving social welfare.
9 Ethical Statement
If rigorously validated and overseen, AI-assisted regulation
could help align private incentives with societal fairness
goals in essential-goods markets (e.g. health insurance, con-
sumer credit). Conversely, careless application risks legit-
imising opaque pricing schemes and deepening existing dis-
parities. We urge future work to prioritise transparency, mul-
tidisciplinary oversight, and the voices of affected commu-
nities.
Acknowledgements
Funding support for project activities has been partially
provided by Canada CIFAR AI Chair, Google award, and
FRQNT scholarships. We also express our gratitude to Com-
pute Canada and Mila clusters for their support in providing
facilities for our evaluations.

References
Achiam, J.; Held, D.; Tamar, A.; and Abbeel, P. 2017. Con-
strained policy optimization. In Proceedings of the 34th
International Conference on Machine Learning, ICML ’17,
22–31. JMLR.org.
American Medical Association. 2023. AMA identifies mar-
ket leaders in health insurance. Accessed: 2025-04-19.
Barocas, S.; and Selbst, A. D. 2016. Big data’s disparate
impact. California Law Review, 104(3): 671–732.
Becker, G. S. 1962. Irrational behavior and economic theory.
Journal of political economy, 70(1): 1–13.
Ben-Akiva, M.; McFadden, D.; Train, K.; Walker, J.; Bhat,
C.; Bierlaire, M.; Bolduc, D.; Boersch-Supan, A.; Brown-
stone, D.; Bunch, D. S.; et al. 2002. Hybrid choice models:
Progress and challenges. Marketing Letters, 13: 163–175.
Berry, S. T.; Levinsohn, J. A.; and Pakes, A. 1993. Automo-
bile prices in market equilibrium: Part I and II.
Bertoletti, L.; Borraz, F.; and Sanroman, G. 2024. Consumer
Debt and Poverty: the Default Risk Gap. Technical report,
GLO Discussion Paper.
Bertsimas, D.; Farias, V . F.; and Trichakis, N. 2011. The
price of fairness. Operations research, 59(1): 17–31.
Betancourt, J. M.; Hortac ¸su, A.; Oery, A.; and Williams,
K. R. 2022. Dynamic price competition: Theory and evi-
dence from airline markets. Technical report, National Bu-
reau of Economic Research.
Chopra, R. 2024. Statement by CFPB Director Rohit Chopra
on the Financial Stability Oversight Council’s Nonbank
Mortgage Company Report. Accessed: 2025-04-21.
Cohen, M. C.; Elmachtoub, A. N.; and Lei, X. 2022. Price
discrimination with fairness constraints. Management Sci-
ence, 68(12): 8536–8552.
Cohen, M. C.; Miao, S.; and Wang, Y . 2021. Dynamic pric-
ing with fairness constraints. Available at SSRN 3930622.
Das, S.; Dhamal, S.; Ghalme, G.; Jain, S.; and Gujar,
S. 2022. Individual fairness in feature-based pricing for
monopoly markets. In Uncertainty in Artificial Intelligence,
486–495. PMLR.
Dwork, C.; Hardt, M.; Pitassi, T.; Reingold, O.; and Zemel,
R. 2012. Fairness through awareness. In Proceedings of the
3rd innovations in theoretical computer science conference,
214–226.
Fleurbaey, M. 2008. Fairness, responsibility, and welfare.
OUP Oxford.
Fout, H.; Li, G.; Palim, M.; and Pan, Y . 2020. Credit risk of
low income mortgages. Regional Science and Urban Eco-
nomics, 80: 103390.
Gallego, G.; Topaloglu, H.; et al. 2019. Revenue manage-
ment and pricing analytics, volume 209. Springer.
Garcıa, J.; and Fern´andez, F. 2015. A comprehensive survey
on safe reinforcement learning. Journal of Machine Learn-
ing Research, 16(1): 1437–1480.
Haarnoja, T.; Zhou, A.; Hartikainen, K.; Tucker, G.; Ha,
S.; Tan, J.; Kumar, V .; Zhu, H.; Gupta, A.; Abbeel, P.; and
Levine, S. 2018. Soft Actor-Critic Algorithms and Applica-
tions.
Kallus, N.; and Zhou, A. 2021. Fairness, welfare, and equity
in personalized pricing. In Proceedings of the 2021 ACM
conference on fairness, accountability, and transparency ,
296–314.
Keisler-Starkey, K.; Bunch, L. N.; and Lindstrom, R. 2024.
Health Insurance Coverage in the United States: 2023.
Lee, S.; Illia, A.; and Lawson-Body, A. 2011. Perceived
price fairness of dynamic pricing. Industrial Management
& Data Systems.
Maestre, R.; Duque, J.; Rubio, A.; and Ar´evalo, J. 2019. Re-
inforcement learning for fair dynamic pricing. In Intelligent
Systems and Applications: Proceedings of the 2018 Intel-
ligent Systems Conference (IntelliSys) Volume 1 , 120–135.
Springer.
Martinez, M. E. 2022. QuickStats: Percentage of Unin-
sured Adults Aged 18–64 Years, by Race and Selected His-
panic Origin Subgroup — National Health Interview Survey,
United States, 2020. MMWR Morb Mortal Wkly Rep 2022 ,
71(834).
McCann, A. 2025. Credit Card Market Share by Issuer. Ac-
cessed: 2025-04-19.
McFadden, D. 1972. Conditional logit analysis of qualitative
choice behavior.
Nicholson, V . J.; Bunn, T. L.; and Costich, J. F. 2008. Dis-
parities in work-related injuries associated with worker com-
pensation coverage status. American journal of industrial
medicine, 51(6): 393–398.
Pew Research Center. 2024. Are you in the American mid-
dle class? [Accessed: 2025-02-28].
Powell, M. J. 1964. An efficient method for finding the min-
imum of a function of several variables without calculating
derivatives. The computer journal, 7(2): 155–162.
Schlosser, R.; and Boissier, M. 2018. Dynamic pricing un-
der competition on online marketplaces: A data-driven ap-
proach. In Proceedings of the 24th ACM SIGKDD interna-
tional conference on knowledge discovery & data mining ,
705–714.
Small, K. A.; and Rosen, H. S. 1981. Applied welfare eco-
nomics with discrete choice models. Econometrica: Journal
of the Econometric Society, 105–130.
U.S. Census Bureau. 2023. Homeownership by Race and
Ethnicity of Householder. https://www.census.gov/library/
visualizations/interactive/homeownership-by-race-and-
ethnicity-of-householder.html. Interactive visualization,
released September 28, 2023. Accessed April 29, 2025.
Virtanen, P.; Gommers, R.; Oliphant, T. E.; Haberland,
M.; Reddy, T.; Cournapeau, D.; Burovski, E.; Peterson, P.;
Weckesser, W.; Bright, J.; et al. 2020. SciPy 1.0: fundamen-
tal algorithms for scientific computing in Python. Nature
methods, 17(3): 261–272.
Wang, Q.; Huang, Y .; Singh, P. V .; and Srinivasan, K. 2023.
Algorithms, artificial intelligence and simple rule based
pricing. Available at SSRN 4144905.
Zheng, S.; Trott, A.; Srinivasa, S.; Naik, N.; Gruesbeck, M.;
Parkes, D. C.; and Socher, R. 2020. The ai economist: Im-
proving equality and productivity with ai-driven tax policies.
arXiv preprint arXiv:2004.13332.

Zhu, Y .; Yuan, Y .; Gu, J.; and Fu, Q. 2023. Neoliberalization
and inequality: disparities in access to affordable housing in
urban Canada 1981–2016. Housing Studies, 38(10): 1860–
1887.
A Price Convergence in Insurance
Simulation
Firms converge to different price allocations dependent upon
the market dynamics. Under fairness incentives (linear and
RL policies), firms are nudged to adopt lower prices for the
low income group than under Free Market. When firms col-
lude, they set prices much higher to maximize total market
profits.
Free Market Linear-SP RL Collusion
0
5
10
15
20Premia
Insurance Premia Convergence
P A low P A middle P A high
P B low P B middle P B high
We note that the RL policy leads firms to converge to
prices similar to those resulting from the linear policy.
This is likely due to these fairness brackets being optimal,
as uncovered in Section 6.1. However, the SP is able to
improve welfare further by lowering taxes in those brackets,
allowing firms to keep more of their profit for achieving
optimal fairness.
B A Probabilistic Bound on Global Fairness
With more assumptions, we derive a tighter, albeit proba-
bilistic bound on opt-out gaps as a result of bounds on local
gaps.
Proposition 2 (Local fairness ⇒ global fairness). We wish
to bound, with high probability, the deviation

 Pr(F = 0 | A = i) − Pr(F = 0 | A = k)

=

 NX j=1  Pr(F = j | A = k) − Pr(F = j | A = i) 

=

 NX
j=1
Xj

,
where we set the random variables
Xj := Pr( F = j | A = k) − Pr(F = j | A = i),
j = 1, . . . , N.
Assumptions.
1. The variables {Xj}N j=1 are independent.
2. Each Xj is bounded: |Xj| ≤ϵ.
3. Optionally, Var[Xj] ≤ σ2 (needed only for Bernstein).
a) Hoeffding’s Inequality (bounded differences) Be-
cause the Xj’s are bounded in [−ϵ, ϵ], Hoeffding’s inequal-
ity gives, for a candidate bound t,
Pr


PN j=1 Xj

 ≥ t  ≤ 2 exp  − 2t2 N (2ϵ)2  .
Setting t = 2 ϵ
q
N
2 log
 2
δ

yields, with probability at least
1 − δ,

 NX
j=1

P (F = j | A = k) − P (F = j | A = i)


≤ 2ϵ
r
N
2 log

2
δ

.
(1)
b) Bernstein’s Inequality (variance information avail-
able) If in addition Var[Xj] ≤ σ2, Bernstein’s inequality
states
Pr


PN j=1 Xj

 ≥ t  ≤ 2 exp  − t2 2N σ2+ 2 3 ϵ t  ,
which can be tighter when most differences are very small
(i.e. σ2 ≪ ϵ2).
High–Probability Bound From (1), we conclude that,
with probability at least 1 − δ,

 Pr(F = 0 | A = i) − Pr(F = 0 | A = k)

 ≤
2ϵ
r
N
2 log

2
δ

.
This Hoeffding bound, while not a convergence guarantee, is
sufficient to demonstrate the tight relationship between local
and global fairness.
C SAC Hyperparameters
We outline the hyperparameters used with SAC to train
our Social Planner agent. They are the same as the de-
fault hyperparameters encouraged by Haarnoja et al. (2018).
SAC Hyperparameters
Hyperparameters
Hidden-layer sizes (actor/critic) [256, 256]
Activation function ReLU
Learning rate η 0.0003
Batch size 256
Replay-buffer size 1M
Discount factor γ 0.00 (RL)
Target-update coef. τsoft 0.005
Entropy coef. αent auto
Updates per env step 1
Warm-up steps 100
Total training steps 2M
Random seed [0, 1, 2, 3, 4]
