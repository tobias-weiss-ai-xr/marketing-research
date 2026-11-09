---
title: When AI Gets Cheaper, Do Prices Follow? Information Delays and Algorithmic Pricing
url: https://arxiv.org/abs/2610.31693
category: consumer-behavior
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Krish Tadigotla
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.31693
pages: 12
chars: 24276
fetched_at: '2026-11-08T13:18:22+00:00'
kb_version: 1
---

# When AI Gets Cheaper, Do Prices Follow? Information Delays and Algorithmic Pricing

When AI Gets Cheaper, Do Prices Follow?
Information Delays and Algorithmic Pricing
Krish Tadigotla
Texas Academy of Mathematics and Science (TAMS)
University of North Texas
Computer Science
KrishTadigotla@my.unt.edu
Abstract
As AI models become cheaper to run, a central question for buyers and market designers is whether
providers will lower their prices accordingly. The answer may depend on how automated pricing systems
respond to competitors. A firm can observe outdated rival prices even when it can revise its own price
frequently; another may have current information but be unable to reprice immediately. These are distinct
constraints, and their combined effects on cost pass-through and consumer welfare are uncertain. We
isolate these mechanisms in a controlled simulation to examine how information delays and repricing
restrictions interact when production costs fall. In a differentiated duopoly with tabular Q-learning
agents, a2 × 2 × 2 × 2factorial design crosses information age, repricing cadence, cost regime, and
firm asymmetry. We train 60 paired market seeds in each of 16 conditions (960 market-condition runs)
and evaluate frozen policies using expected logit consumer surplus. In the symmetric declining-cost
environment, the prespecified lag-by-cadence interaction is−0.00025normalized welfare units, with a
95% paired-seed bootstrap interval of[−0.0402, 0.0393]. Neither this interaction nor the two prespecified
moderation contrasts is statistically distinguishable from zero. In the fast-information, fast-repricing
treatment, mean discrete price changes amount to 55.6% and 44.0% of the imposed cost reductions for
the two firms. Welfare under learned policies is below the corresponding static grid-Nash benchmark
in every treatment cell. The study provides a reproducible comparison of pricing-timing rules, but the
findings are conditional on the simulated market and do not establish the pricing practices or collusion of
actual AI providers.
Keywords:algorithmic pricing; Q-learning; information delay; cost pass-through; consumer welfare; compu-
tational industrial organization.
JEL classification:C63, D43, L13, L86.
1 Introduction
The price of large-language-model inference has fallen sharply, while available models and hosting arrangements
increasingly differ in quality, cost, and specialization. Evidence from the OpenRouter inference marketplace
documents sharp reductions in quality-adjusted prices and considerable entry [8]; theoretical work describes
the richer token-budget and menu choices facing LLM suppliers [2]. A basic industrial-organization question
follows: when production becomes cheaper, how much of the saving reaches buyers?
Whether firms pass cost savings to consumers may depend on both how frequently they adjust prices and
how quickly they observe competitors’ prices. A firm’s ability to reprice every period does not imply that
it has a current rival-price feed. Conversely, a firm can observe today’s rival price while being constrained
to maintain yesterday’s quote. Repricing frequency and information delay are separate constraints. Prior
research has investigated automated price adjustment, strategic choice of update frequency, and the emergence
of supracompetitive outcomes [4, 5, 6, 10]. Related work also studies Q-learning with stochastic production
costs [1]. We therefore do not claim that either dynamic updating, imperfect information, or variable costs is
novel in itself.
We test how delayed rival-price information interacts with synchronized repricing under constant or
declining marginal costs. Firms are either symmetric or differ jointly in quality and cost. Outcomes are
1
arXiv:2610.31693v1  [econ.GN]  20 Oct 2026

measured in expected logit buyer surplus as well as prices and profits. The design does not treat high prices
or recurrent price paths as proof of autonomous collusion, an interpretation disputed in recent methodological
work [7, 9]. The model permits us to attribute differences to programmed interventions within a synthetic
market, not to actual provider conduct.
The primary interaction is not statistically distinguishable from zero; differences across individual
treatment-cell means do not establish the proposed interaction. We also find average discrete price adjustment
smaller than the assumed cost reduction in one highlighted treatment; however, only one cost-shock magnitude
is imposed, so the data do not identify a general pass-through schedule. Results are sensitive to several
learning assumptions, and the available data do not establish Q-value convergence during training. The
interpretation is confined to the simulated environment.
2 Related research and contribution
Simulations by Calvano et al. [5] show that independent Q-learning agents can generate high prices in
a differentiated Bertrand market. Klein [10] studies sequential price setting, and Brown and MacKay [4]
model differences in pricing technology and algorithmic responses in market equilibrium. Conjeaud et al.
[6] investigate asynchronous updates under Poisson clocks and different rival-price information interfaces,
showing that synchronization and observability matter for simulated prices. Our design does not replicate
their continuous-time Poisson environment: it independently fixes feed age and update cadence in discrete
market ticks.
Recent contributions impose further caution. Ballestero [1] varies production costs under sequential
learning; hence cost shocks alone cannot anchor novelty. den Boer et al. [9] question whether learned high
prices satisfy economically relevant collusion criteria. de Moraes and De-Losso [7] illustrate why simple
frozen-policy perturbations cannot unambiguously identify deterrence mechanisms. Bichler et al. [3] find that
agent-interface choices can alter price competition. We use these studies to motivate explicit timing controls,
nonlearning benchmarks, direct consumer-welfare measurement, and restrained mechanism claims. We did
not run deviation-response experiments.
The design has three methodological features. First, the price-feed lag and the timing of permissible quote
revisions are independently varied and structurally distinguishable even when firms update simultaneously.
Second, the analysis tests whether the timing interaction changes with an exogenous production-cost reduction
and asymmetric service values/costs. Third, inference proceeds at the independent market-seed level and
preserves all treatment cells, including results unfavorable to a dramatic hypothesis. The estimates apply to
this simulated market. The comparison does not establish priority over all related work or describe actual
providers’ pricing practices.
3 Environment and methods
3.1 Differentiated demand and welfare
Two sellersi∈{A,B} quote pricespit from a finite setP ={0.60, 0.75,..., 3.00}. With perceived qualityvi,
logit scaleµ = 0.25, and an outside good with normalized deterministic utility zero, their demand shares and
expected buyer surplus are
sit = exp[(vi−p it)/µ] 1 +∑ j∈{A,B} exp[(vj−p jt)/µ],(1)
s0t = 1−s At−s Bt, CS t =µlog

1 + ∑
j∈{A,B}
exp[(vj−p jt)/µ]

.(2)
Firm profit isπit = (pit−c it)sit. The potential-buyer mass is one. Prices, costs, and welfare measures are
expressed in normalized units per market tick, not dollars or billed tokens. The simulation uses numerical
log-sum-exp for stability.
The symmetric treatment usesv = (2.0, 2.0)with initial cost cH = (1.00, 1.00)and final cost cL =
(0.70, 0.70). The jointly asymmetric treatment usesv = (2.2, 1.9), cH = (1.00, 0.78), andcL = (0.70, 0.55).
2

Because quality and cost vary together, their individual effects cannot be identified. This treatment also says
nothing about model licensing. Flat-cost cells remain atcH. Declining-cost cells undergo an exogenous shift
to cL at t = 1000during frozen evaluation. During training, a geometric waiting time is drawn independently
in each episode, avoiding a known deterministic shock date in learning.
3.2 Separate information and price-revision clocks
At tickt, each agent observes its own prevailing price and cost regime plus the rival’s historically posted
price p−i,t−L. We vary the feed ageL∈{ 1, 4} market ticks. An agent can revise its own price only when
t≡ 0 ( modF ), whereF∈{ 1, 3}; otherwise its quote is held. Both agents use simultaneous, synchronized
eligibility schedules within the prespecified experiment. This isolates cadence from staggered updating; it
does not examine unequal firm clocks.
The L = 1versus L = 4contrast ensures variation in observed rival history even with synchronized
three-tick repricing. With synchronized revisions every three ticks, an age-one feed reflects the rival’s last
revision, while an age-four feed can omit that revision. WithF = 3, ages one and three would otherwise
produce identical observed rival quotes. No contemporaneous rival action leaks into the agent’s observation.
3.3 Learning and equilibrium references
Each firm has a tabular action-value table with observed stateSit = (pit−,p−i,t−L,k t), wherekt denotes
the observable high/low cost regime. This is a partially observed state representation, not a claim that
the opponent’s strategy is fully Markov. Training usesα = 0.10, per-tick discount factorγ = 0.95, and
epsilon-greedy exploration declining from 1.00 to 0.02 over each agent’s scheduled decisions. Profits accrue
every tick. For a held price durationd, the duration-aware update is
Q(St,a t)←(1−α)Q(S t,a t) +α


d−1∑
j=0
γjπi,t+j +γ d max a′ Q(St+d,a′)

,(3)
with the continuation value removed at episode termination. Each market trains for 10 episodes of 15,000
ticks; Q tables persist while market prices and feed buffers reset at episode boundaries. Separate seeded
streams govern agents and cost-shock waiting times.
We compute cost/configuration-specific finite-grid one-shot Nash prices and joint-profit-maximizing prices.
The Nash profile satisfies
πi
(
pN i ,p N −i;c i ) ≥π i ( pi,p N −i;c i ) for everyp i∈P.(4)
The computed pure-grid equilibrium is unique in each required state. A separate continuous-price first-order-
condition solver provides a numerical cross-check, but the grid Nash is the operative comparison. The static
Nash is a one-period benchmark, not the equilibrium of the repeated stochastic game.
3.4 Design, evaluation, and prespecified analysis
The prespecified 16 cells crossL∈{ 1, 4}, F∈{ 1, 3}, cost type (flat/declining), and configuration (symmet-
ric/asymmetric). Independently initialized market seed IDs 200000–200059 are reused across all conditions,
yielding 60 paired markets per cell (960 market-condition training runs). Following 150,000 training ticks
per market, Q is frozen and the model is evaluated for 2,000 ticks, starting from the high-cost static grid
Nash. The frozen evaluation is a standardized reset experiment, not continuation from the final training price
history. All 960 markets were retained, including unsuccessful or uncompetitive learned outcomes.
Our prespecified market-level outcome is mean consumer surplus over post-shock ticks 1050–1999, 950
ticks in total:
Ys,L,F,C,A = 1 950
1999∑
t=1050
CS s,L,F,C,A,t.(5)
Let Ds(C,A ) = [ Ys,4,3,C,A−Y s,1,3,C,A]− [Ys,4,1,C,A−Y s,1,1,C,A]. The prespecified contrasts are (H1)
E[Ds(declining,symmetric )], (H2) the difference of H1 between declining and flat cost regimes, and (H3) the
3

difference between asymmetric and symmetric firms in the declining-cost regime. These expectations refer
only to the model’s random initialization and training streams.
For each hypothesis, 95% percentile confidence intervals use 10,000 resamples of whole paired market-seed
blocks with a fixed bootstrap seed of 987654321. Secondary H2 and H3 paired-t p-values receive Holm
adjustment as a two-test family. A separate saturated24 descriptive regression includes market-seed fixed
effects and standard errors clustered by the 60 independent seed blocks. The 1.92 million serially dependent
tick observations are never interpreted as independent regression units.
4 Results
4.1 Prespecified interactions: no rejection of the primary null
Hypothesis Estimate 95% paired bootstrap CIn
H1: Lag×cadence−0.0003 [−0.0402,+0.0393]60
H2: Additional cost moderation+0.0166 [−0.0348,+0.0685]60
H3: Additional asymmetry moderation−0.0504 [−0.1020,+0.0009]60
Table 1: Prespecified seed-paired interaction estimates. Units: normalized logit buyer surplus per potential buyer per
market tick. Percentile 95% intervals resample 60 entire market seeds, 10,000 times. All intervals include zero. H2/H3
Holm-adjusted paired-t p-values are 0.5312 and 0.1210 respectively.
The H1 point estimate is−0.0002533and the confidence interval ranges from−0.04022to+0 .03929. The
estimate does not establish equivalence: the interval still admits meaningful effects in either direction on
the model’s normalized welfare scale. The secondary cost and asymmetry moderation intervals also include
zero, and neither passes its adjusted inference criterion. The estimates do not establish whether outdated
rival-price information strengthens or weakens the welfare effect of slower repricing.
Figure 1: Prespecified interaction contrasts. Points indicate paired-seed means and bars indicate 95% percentile
bootstrap intervals over 60 market seeds. The vertical reference line denotes zero interaction.
4.2 Cell means and consumer welfare
Figure 2 displays mean post-window welfare for all 16 cells and their whole-seed uncertainty. Differences
between raw cell means exist, but individual pairwise differences do not substitute for the prespecified
difference-in-differences test. For every learned-treatment cell mean, post-window welfare is below the
appropriate current-cost one-shot grid Nash benchmark; mean gaps range from roughly−0.333to −0.123
normalized units. This finding does not establish algorithmic deterrence, joint profit maximization, a stable
4

Figure 2: Mean post-window logit consumer surplus across all 16 simulation conditions. Intervals are 95% confidence
intervals over market seeds; panels use comparable welfare scales.
5

learned equilibrium, or illegal collusion. The baseline itself is static and omits the adaptive strategies and
partial observability of the repeated learning environment.
4.3 Responses to cost reductions
Every falling-cost cell has a negative mean change in posted price after the forced cost decline, but the
price reductions are generally smaller than the imposed reductions in marginal cost. For the symmetric,
L = 1, F = 1case, the mean ratio of price change to cost change is 0.5559 for firm A and 0.4397 for firm B.
The ratio uses prices averaged over ticks 800–999 versus 1050–1249, divided by the cost difference of−0.30.
Confidence intervals based on market seeds are shown in Figure 4. There is only one shock magnitude per
firm; a conventional continuous pass-through slope or empirical elasticity is not identified here.
Figure 3: Post-learning price and buyer-surplus response centered on the synthetically imposed cost decline at tick 1000
in the symmetric market. Trajectories are averaged into disclosed nonoverlapping 10-tick bins; bands are pointwise
95% seed-bootstrap intervals, not simultaneous event-study bands.
4.4 Benchmarks, learning sensitivity, and convergence
As an implementation check, the constant-price control is invariant to the rival-price feed age. A deterministic
myopic-best-response policy produces the corresponding grid-Nash reference in the saved control configurations,
whilethelearnedpoliciesgenerallydonot. Thefourprespecifiednonconfirmatorylearning-parametervariations
yield timing-interaction estimates ranging from about−0.068to+0 .040, with exploratory intervals including
zero; this does not exhaust parameter robustness. In a separate 10-seed longer-training comparison the
exploratory interaction is about+0.093, but the intervention changes market time, learning decisions, and
training exposure jointly.
The experiment does not establish convergence of training Q values. There are late price changes in
frozen greedy evaluation in 882/960 market-condition runs; frozen cyclic policies can do this even if Q has
6

Figure 4: Ratio of the mean simulated price change to the imposed marginal-cost change, by firm and treatment.
Intervals resample market seeds; the reference value of one denotes full absolute pass-through.
converged, while a stable price path alone would also not prove Q convergence. The archived experiment lacks
sequential training Q-table snapshots necessary for a direct convergence analysis. Accordingly, equilibrium
and deterrence mechanisms remain unverified. Figure 5 and the appendix report all robustness outcomes
rather than selecting favorable scenarios.
Figure 5: Nonconfirmatory lag-by-cadence contrasts under changed learning rates or per-tick discount factors (10
seeds per setting), alongside the prespecified 60-seed baseline. All intervals cross zero; this panel is exploratory, not
additional primary evidence.
5 Discussion and limits
Slower rival-price feeds can plausibly weaken rapid undercutting, but they can also impede responses that
otherwise sustain higher prices. Neither sign is guaranteed in a partially observed repeated game. The
7

estimated interaction is too imprecise to distinguish between these mechanisms. Interpreting an intervention
therefore requires knowing which timing rule changes, how welfare is measured, which evaluation baseline is
used, and how many learning opportunities the agents receive.
External validity is limited in several specific ways. The model has two firms with a single scalar price per
firm, whereas actual LLM pricing often uses input/output token rates, budgets, volume discounts, context
windows and model-specific quality. Demand elasticities, prices, marginal costs and timing distributions were
stipulated rather than fit to market microdata. The asymmetric treatment jointly alters costs and consumer
valuations. The agents are tabular Q-learners, not documented corporate pricing algorithms; real providers
are not known to use this policy. Both firms update synchronously in every confirmatory cell. The discounted
learning state is partially observed, and no global convergence or equilibrium existence result is demonstrated
for the stochastic game.
A nonsignificant result does not imply that the effect is exactly zero. The confidence interval for H1 is
nontrivial on the welfare scale, and the sensitivity analysis covers only a small subset of learning choices. Future
studies should prespecify finer price grids, alternative demand scales, nonsynchronous update offsets, quality-
only/cost-only asymmetry, and richer agents; retain training-time Q snapshots; and obtain price/quality
observations from actual markets for external calibration. These extensions would require a separate design
and independent data generation.
6 Conclusion
In this prespecified inference-market simulation, the interaction between rival-price feed age and repricing
cadence is not statistically distinguishable from zero for post-cost-shock consumer welfare in the primary
symmetric condition. Average discrete pass-through of the modeled production-cost reduction is incomplete
in a highlighted treatment, and learned-policy mean welfare lies below static grid-Nash references, but the
evidence does not prove strategic collusion, equilibrium convergence, or effects in observed LLM provider
markets. The study provides a reproducible test of this timing interaction and a baseline for richer models of
adaptive pricing. More comprehensive learning-convergence and external-validity analysis is needed before
economic-policy or provider-level claims would be appropriate.
References
[1] Gonzalo Ballestero. Algorithmic collusion under sequential pricing and stochastic costs.International
Journal of Industrial Organization, 106:103281, 2026. doi: 10.1016/j.ijindorg.2026.103281.
[2] Dirk Bergemann, Alessandro Bonatti, and Alex Smolin. Menu pricing of large language models. Cowles
Foundation Discussion Paper 2502, Yale Cowles Foundation, 2026. URL:https://cowles.yale.edu/
research/cfdp-2502-menu-pricing-large-language-models.
[3] Martin Bichler, Philip Hierhager, Kassian Köck, and Fabian Pieroth. How language model agents reshape
price competition, 2026. URL:https://arxiv.org/abs/2610.21711.
[4] Zach Y. Brown and Alexander MacKay. Competition in pricing algorithms.American Economic Journal:
Microeconomics, 15(2):109–156, 2023. doi: 10.1257/mic.20210158.
[5] Emilio Calvano, Giacomo Calzolari, Vincenzo Denicolò, and Sergio Pastorello. Artificial intelli-
gence, algorithmic pricing, and collusion.American Economic Review, 110(10):3267–3297, 2020. doi:
10.1257/aer.20190623.
[6] Ivan Conjeaud, Gaspard Abel, and Argyris Kalogeratos. Algorithmic collusion under asynchronous price
updating, 2026. URL:https://arxiv.org/abs/2608.01406.
[7] Kauê Lopes de Moraes and Rodrigo De-Losso. Algorithmic collusion without deterrence: Auditing the
punishment mechanism in q-learning pricing agents, 2026. URL:https://arxiv.org/abs/2610.21867.
[8] Mert Demirer, Andrey Fradkin, and Nadav Tadelis. The emerging market for intelligence: How firms
buy and sell AI.Journal of Economic Perspectives, 40(3):23–46, 2026. doi: 10.1257/jep.20261506.
8

[9] Arnoud den Boer, Janusz M. Meylahn, and Maarten Pieter Schinkel. Artificial collusion: Examining supra-
competitive pricing by q-learning algorithms.Management Science, 2026. doi: 10.1287/mnsc.2024.08557.
[10] Timo Klein. Autonomous algorithmic collusion: Q-learning under sequential pricing.RAND Journal of
Economics, 52(3):538–558, 2021. doi: 10.1111/1756-2171.12383.
A Full treatment results
Firms CostsF LMean CS SD(CS) Joint profit
Sym Flat 1 1 0.549 0.053 0.551
Sym Flat 1 4 0.566 0.059 0.542
Sym Flat 3 1 0.539 0.070 0.551
Sym Flat 3 4 0.539 0.047 0.548
Sym Decl 1 1 0.677 0.080 0.716
Sym Decl 1 4 0.668 0.074 0.718
Sym Decl 3 1 0.680 0.103 0.702
Sym Decl 3 4 0.671 0.071 0.707
Asy Flat 1 1 0.597 0.056 0.658
Asy Flat 1 4 0.633 0.074 0.627
Asy Flat 3 1 0.575 0.088 0.664
Asy Flat 3 4 0.614 0.075 0.630
Asy Decl 1 1 0.695 0.082 0.818
Asy Decl 1 4 0.739 0.055 0.779
Asy Decl 3 1 0.735 0.083 0.779
Asy Decl 3 4 0.729 0.094 0.772
Table 2: All 16 prespecified treatment cells (60 markets each). Mean and across-seed SD of post-window expected logit
buyer surplus (CS) are in normalized units; joint profit is the sum of both sellers’ mean profits. Sym. = symmetric
firm configuration; Asy. = quality/cost asymmetric.L is competitor-feed age in ticks;F is quote-revision interval. No
cell was dropped.
B Reproduction of the statistical analysis
The analysis reads the archived 960 market-condition simulations (60 paired random seeds in each of 16 cells).
Each frozen-policy evaluation contains 2,000 simulated market ticks. The post-shock estimand averages ticks
1050–1999, while the discrete cost-pass-through calculation compares the specified pre- and post-shock windows
in Section 4.3. Market-level H1–H3 contrasts are computed before inference; 95% percentile confidence
intervals resample all 60 seed blocks with 10,000 bootstrap draws and pseudorandom seed 987654321. No
tick-level observations enter the bootstrap as independent units. The replication materials specify the Python
environment, training protocol, data validation checks, and commands to regenerate tables and figures.
C Supplementary figures
9

Figure 6: Mean simulated consumer surplus for the 16 factorial cells. A common color scale is used across panels;
color differences are descriptive rather than inferential.
Figure 7: Distribution of seed-level post-window consumer surplus for the four symmetric declining-cost cells (n = 60
per cell). Points show individual simulated markets.
10

Figure 8: Learned-policy consumer surplus less current-cost static grid-Nash consumer surplus, with uncertainty over
market seeds. The one-period Nash solution is a descriptive benchmark.
11

Figure 9: Coefficients from the saturated factorial regression with seed fixed effects and standard errors clustered by
seed. This is a secondary descriptive specification.
Figure 10: Frequency of price changes and dispersion in the last 300 frozen-policy evaluation ticks. These diagnostics
do not establish convergence of training Q values.
12
