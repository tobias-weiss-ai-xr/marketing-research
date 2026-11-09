---
title: 'CrashGym: Measuring the Decision Value of Experimentation for LLM Agents in Counterfactual Market
  Crashes'
url: https://arxiv.org/abs/2610.29245
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Haocheng Lu
- Haoxuan Cheng
- Mingyang Chen
- Minjun Zhu
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.29245
pages: 14
chars: 53067
fetched_at: '2026-11-08T13:31:54+00:00'
kb_version: 1
---

# CrashGym: Measuring the Decision Value of Experimentation for LLM Agents in Counterfactual Market Crashes

CrashGym: Measuring the Decision Value of
Experimentation for LLM Agents
in Counterfactual Market Crashes
Haocheng Lu1,∗,† Haoxuan Cheng2,* Mingyang Chen3 Minjun Zhu4
1Columbia University 2Cornell University
3Hithink RoyalFlush Information Network Co., Ltd. 4New York University
*Equal contribution. †Corresponding author: haocheng409@gmail.com
Abstract
Language-model agents are increasingly asked to run experiments, yet benchmarks rarely measure whether those experi-
ments improve the decisions they are meant to inform. We introduceCrashGym, a deterministic, replayable limit-order-
book simulator in which an agent must choose between a deleveraging intervention and a liquidity backstop for a market
about to suffer a shock-triggered crash. Before committing, the agent may query intervention experiments in a laboratory
realization of the market. Its choice is then scored on an independently seeded target realization in which the simulator
executes every feasible intervention, so regret relative to the best intervention is computed by directly simulating every
alternative on the same target repeats, with no human or model-based judging. The simulator implements each amplifica-
tion channel—persistent price impact, liquidity withdrawal, margin-driven liquidation, and an evolving strategy mix—as
an explicit mechanism that can be switched on in stages. In a prospectively specified study on 24 newly sampled worlds,
laboratory access reduces the mean regret of the one deployment with a complete record (Luna) from 8.878 to 3.785, a
paired reduction of 5.092 utility units (nominal 95% world-bootstrap interval: 1.028–9.507), or 57.4% of the OBSERVE-
ONLY mean. Prospective comparisons for two further deployments are incomplete; in a separate exploratory study, mean
regretislowerwithlaboratoryaccessforallfourdeploymentsevaluated. Alaboratorywhosestrategymixevolvesendoge-
nously yields no established advantage over one with a fixed mix. CrashGym thus measures the value of experimentation
as avoided decision loss and lets simulator detail be judged by the decisions it supports.
1 Introduction
A market is about to fall sharply. A policy agent must recommend one of two interventions: force leveraged holders
to cut their positions, or post a standing bid that supplies liquidity. Both are defensiblea priori. Deleveraging can pre-
empt the cycle of margin calls and forced selling, whereas a liquidity backstop can absorb that selling before it moves
prices [1, 11, 25]. Which intervention is better depends on which amplification channel dominates in the market at hand.
We ask whether an agent that can first experiment on a laboratory copy of the market chooses better, and by how much.
Language-model agents are increasingly evaluated as experimenters: they design studies, run code, and report find-
ings [15, 16, 22]. Most evaluations, however, score the research process or its products—task completion, explanation
quality, or recovery of a latent structure. Completing an experiment andbenefiting from it are different outcomes. Mea-
suring the benefit requires two ingredients that are rarely available together: the same decision-maker observed with and
without experimental access, and the counterfactual outcome of every action it could have taken. The second ingredient is
unobservable in historical data.
Approach. CrashGym supplies both ingredients inside a deterministic agent-based market (Figure1). An agent re-
ceives a public observation, may query intervention experiments in a laboratory realization, and then commits to one
intervention. The simulator executesevery feasible intervention on an independent target realization that the agent never
observes. Regret—the utility gap between the best intervention and the chosen one—is therefore exact for the realized tar-
get repeats. Comparing regret across information conditions yields the gross decision value of experimentation, a realized
counterpart of the classical value of sample information [14, 21, 23]. Because the simulator’s amplification channels are
explicit mechanisms that can be enabled in stages, the same outcome also tests whether added simulator detail improves
the decision it is meant to support.
Contributions.
• A counterfactual market laboratory.We describe an exchange core with exact integer accounting, event-sourced
replay, and counter-based randomness, together with a crash construction whose amplification channels can be enabled
in cumulative stages (Section3).
1
arXiv:2610.29245v1  [cs.AI]  21 Oct 2026

(a) Laboratory realization
seed cohort 𝑗 · 8 repeats
(b) Independent target realization
seed cohort1 − 𝑗 · 8 repeats
World 𝑤: shared constructor
parameters · participants · shock
experiment menu
LEVERAGE
LIQUIDITY
NULL
LLM agent
≤ 8 calls
run_experiment
8-repeat summary
Committed
action 𝑎
submit_decision
never shown to agent
¯𝑈 (CAP)
¯𝑈 (BACKSTOP)
every feasible
action executed
Regret
max𝑎′ ¯𝑈 (𝑎′ )
− ¯𝑈 (𝑎)
chosen 𝑎
Figure 1: Task overview.A world constructor𝑤 is instantiated with two disjoint seed cohorts. (a) In the laboratory cohort the agent
may run intervention experiments and receives public eight-repeat summaries. (b) Its committed action is scored on the other cohort,
where the simulator executes both feasible interventions; regret is the utility gap to the better one. Target outcomes are never visible to
the agent. Under OBSERVE-ONLY, the agent decides from the initial observation alone.
• A decision-grounded evaluation task.A laboratory in which the agent acquires interventional evidence is separated
from an independently seeded target on which every feasible intervention is executed and scored. This yields exact
counterfactual regret for every decision (Section4).
• Controlled evidence.With identical targets, we compare no access, two laboratory designs, and a tool placebo, sam-
pling new worlds prospectively and using a stratified whole-world bootstrap (Section5). Laboratory access lowers
Luna’s mean regret by 5.092 units on 24 newly sampled worlds, meeting the prespecified criterion. An evolving strat-
egy mix in the laboratory yields no established additional benefit (Section6).
The measured value is avoided loss in simulator utility units. Net value would additionally require the costs of experimen-
tation and inference, which we do not measure.
2 Related work
LLM agents as experimenters.Tool-using language models interleave reasoning with external actions [24, 33], and a
growing set of environments evaluates them as scientists. ScienceWorld and DiscoveryWorld assess task completion and
discovery in simulated worlds [16, 29]; MLAgentBench evaluates machine-learning experimentation [15]; and end-to-
end systems generate complete research papers [22]. CausaLab distinguishes predictive success from recovery of causal
structure, and CausalGame evaluates causal reasoning and experimental protocols in games [5, 32]; see also Kıcıman et al.
[17]. We measure a different quantity: how much an agent’s experiments improve a subsequent, independently scored
decision. An agent may use informative intervention results well without reconstructing the latent mechanism.
LLM agents in finance.Domain-adapted models and agents have been applied to financial analysis and trading [30,
31, 34], and InvestorBench evaluates financial decision-making across tasks [20]. These evaluations typically rely on
historical data, in which the outcomes of untaken actions are unavailable. Our simulator supplies those counterfactuals for
a policy intervention, at the cost of using synthetic rather than historical markets.
Marketsimulation. Agent-basedmodelshavelongbeenusedtostudymarketdynamics[ 9,12,19]. ABIDESsupports
high-fidelity, message-level market research [2]; JAX-LOB targets accelerated, parallel limit-order-book simulation [10];
and realism metrics assess how closely simulated order books reproduce stylized facts [28]. Our crash construction draws
ontheleverage-cycleandfire-saleliterature, inwhichmarginconstraints, forcedselling, andliquiditywithdrawalreinforce
one another [1, 11, 25, 26]. Rather than maximizing realism, we use the simulator as an instrument that supplies exact
counterfactual intervention outcomes and lets each amplification channel be switched on or off.
Value of information and decision-aware model evaluation.Statistical decision theory values an experiment by the
improvement in the expected utility of the decision it informs [4, 14, 21, 23]. Our gross value𝑉𝑏 (Section 7) is a realized,
empirical counterpart for an LLM agent. A related literature argues that models should be judged by the decisions they
induce rather than by predictive accuracy alone [6, 8, 18], and the value-equivalence principle motivates retaining only
those model distinctions that matter for planning [13]. Our comparison of laboratory designs examines this motivation
2

empirically; it does not test Bellman-operator equivalence. The setting also relates to sim-to-real transfer, in which the
deployment environment differs from the training simulator [27].
3 The CrashGym simulator
The simulator is a discrete-time, single-asset market with a central limit-order book. We describe its components in turn:
the exchange core, the participants, the episode schedule, the amplification mechanisms, the evolving strategy mix, the
mechanism stages, and the determinism and replay layer. Parameter values refer to the crash construction used in all
experiments; AppendixA lists them in full.
3.1 Exchange core
Order book and matching.Prices are integers in ticks. Each side of the book maps a price level to a first-in-first-out
queue, giving strict price–time priority. The only order primitive is a limit order, together with cancellation by the owning
account. A marketable order is emulated as a limit order priced 100 ticks through the best opposite quote; any unfilled
remainder is cancelled immediately, so it behaves as an immediate-or-cancel order with a price band. Incoming orders
walk the opposite side best-first, and each fill executes at theresting order’s price for the smaller of the two quantities; a
partially filled resting order keeps its queue position. The reference price𝑚𝑡 is the sum of best bid and best ask, i.e. the
midpoint in half-tick units, so it remains an exact integer. If one side of the book is empty, the reference falls back to the
lasttwo-sidedquote,andaggressiveordersarepricedfromthelastpublishedbidorask. Bookinvariants—noemptylevels,
no zero quantities, strictly increasing priorities, and no crossed book—are checked after every mutation.
Accounts,riskadmission,andfees. Each participant owns an account with integer cash and inventory, with positions
tracked as first-in-first-out lots. Before an order is accepted, the exchange checks a position limit (106 lots) and a leverage
limit: the worst-case position notional along the order’s potential fill path may not exceed20× the account’s initial cash.
Rejected orders are logged and have no effect. A fee of one cash unit per lot is charged tobothcounterparties of every fill;
resting orders that never fill pay nothing. Every fill must conserve total inventory and total cash plus fees, global invariants
are re-checked after each operation, and a full canonical audit closes every run.
3.2 Participants
Table1summarizes the six participant classes and the two exogenous accounts. Each step, amarket makerposts a 40-level
ladder on each side, at offsets of2 + 𝑘 ticks (𝑘 = 0, . . . , 39) around a center that tracks the previous reference price. Its
depth per level is a world-specific¯𝑄 ∈ { 24, . . . , 56} lots in the initial ladder (step 0), 400 lots during steps 1–7, and¯𝑄
again from the shock onward. Every world therefore experiences a scheduled liquidity cliff at the shock, in addition to the
stress-driven withdrawal described below. Ladders are reconciled rather than rebuilt: unchanged levels keep their queue
priority, andsupersededordersarecancelled. Noise traderssubmiteightmarketableordersoffourlotsperstep, eachabuy
or sell with probability1/2. A fundamental trader trades four lots per tick of deviation between the fundamental value𝑣
and the midpoint. Atrend followertrades 4𝑒𝑡 lots, where𝑒𝑡 = trunc((3𝑒𝑡 −1 + 𝑟𝑡 −1)/4) is a moving average of past returns
𝑟𝑡 = 𝑚𝑡 − 𝑚𝑡 −1 (half-ticks) andtrunc rounds toward zero. The fundamental value is held constant at𝑣 = 10,000 ticks: no
newsarrives,sopost-shockdynamicsareresponsestotheshock,thescheduledpost-shockdepth,andtheintervention. The
leveraged traderbuilds a long position at step 1 and afterwards trades only through forced liquidation or the deleveraging
intervention. The adaptive participant chooses each step between two candidate strategies (Section3.5).
3.3 Episode schedule
An episode lasts𝑇 = 96 steps (Figure2a). At step 0 the maker posts its initial ladder around𝑣. At step 1 the leveraged
trader builds its position; at step 4 the chosen intervention takes effect; at step 7 the pre-shock reference𝑚𝑡0 −1 is recorded;
and at step𝑡0 = 8 the shock account sells 160–240 lots at market. Within each step, operations execute in a fixed order
(Figure 2b): the maker re-quotes; last step’s shadow trades are settled and strategy shares updated; intervention orders are
placed; the shock and its persistent impact are applied; forced liquidations execute; noise, fundamental, and trend orders
arrive; the adaptive participant trades; and the end-of-step reference price and objective are recorded.
3

Participant Rule per step Active from
Market maker 40-level ladder per side at±(2 + 𝑘) ticks; ¯𝑄 lots/level at step 0, 400
during steps 1–7, ¯𝑄 from the shock on, thinned under stress (Eq.1)
all configurations
Noise traders 8 marketable orders of 4 lots, side drawn with probability1/2 all configurations
Leveraged trader buys 160–240 lots at step 1; forced sales when below maintenance
margin (Eq.2)
margin rule: leveragestage
Fundamental trader 4 lots per tick of𝑣 − mid, marketable leveragestage
Trend follower 4𝑒𝑡 lots, 𝑒𝑡 = trunc(( 3𝑒𝑡 −1 + 𝑟𝑡 −1)/4), marketable leveragestage
Adaptive participant after the shock, draws the FUNDAMENTAL or TREND candidate from shares
(𝑠F, 𝑠Tr); shares fixed or evolving (Eq.3)
leveragestage
Shock account (exogenous) marketable sale of 160–240 lots at step 8 all configurations
Intervention account executes the chosen intervention (Section4.2) all configurations
Table1: Participantsinthecrashconstruction. Ranges are sampled per world (AppendixA). “Active from” refers to the mechanism
stages of Figure3a; theleveragestage is the first stage used in our laboratories.
(a) Episode timeline and scored drawdown (conceptual path)
reference price𝑚𝑡
0 1 4 7 8 32 64 96
step (pre-shock steps expanded)
pre-shock reference𝑚𝑡0 −1
scored drawdown∑ 𝑡 ≥𝑡0 max{0, 𝑚 𝑡0 −1 − 𝑚𝑡 }
exposure build
intervention
reference
shock
(b) Order of operations within each step
Maker re-quotes
(stress-scaled depth)
1
Settle shadow P&L,
update shares
2
Intervention orders
(deleveraging,
backstop bid)
3
Shock order and
persistent impact
4
Margin check,
forced liquidation
5
Noise orders
(8 × 4 lots)
6
Fundamental and
trend traders
7
Adaptive trader: fork
shadows, draw, trade
8
Record 𝑚𝑡 and
objective
9 liquidity
adaptation
intervention
shock and stress
order flow and bookkeeping
Figure 2: Episode anatomy.(a) Fixed schedule of a 96-step episode. The utility’s drawdown term is the shaded area between the
pre-shock reference and the post-shock reference path (the path drawn is illustrative, not a sampled trajectory). (b) Deterministic order
of operations within a step. Shadow-trade settlement (2) and forking (8) run only when the strategy mix evolves; margin checks (5),
fundamental and trend traders (7), and the adaptive participant (8) are active from theleveragestage onward (Figure3a).
3.4 Amplification mechanisms
The shock is a burst of order flow, not a change in fundamentals. Three mechanisms convert it into a crash whose depth
and duration depend on the world (Figure3b).
Persistent impact. The maker’s quote center shifts by40 𝑥/𝐷0 ticks, where 𝑥 is the executed shock volume and
𝐷0 = 10 ¯𝑄 is the depth of the ten best bids in the initial (step-0) ladder; integer remainders are carried forward. The shock
therefore moves the price permanently rather than only transiently.
Liquidity withdrawal.After the shock, the maker measures stress𝜎𝑡 = max{0, 𝑚 𝑡0 −1 − 𝑚𝑡 −1} + | 𝑟𝑡 −1| in half-ticks
and thins its ladder to
𝑄𝑡 = ¯𝑄 · max { 0.25, 1 − 𝛽 𝜎𝑡 /𝜅 } , (1)
where 𝛽 ∈ [ 0, 1] is the world’s withdrawal strength and𝜅 ∈ { 24, . . . , 56} its stress scale. Withdrawal reduces depth but
never widens the spread or empties the book.
Margin-driven liquidation.At the start of step𝑡, the leveraged trader’s equity is𝐸𝑡 = 𝑐𝑡 + 𝑞𝑡 𝑝𝑡, where𝑐𝑡 and 𝑞𝑡 are
its cash and inventory at the close of step𝑡 − 1 and 𝑝𝑡 = 𝑚𝑡 −1/2 is the previous closing midpoint in ticks; its maintenance
4

requirement is𝑀𝑡 = 𝜇 |𝑞𝑡 | 𝑝𝑡 with 𝜇 ∈ [ 3%, 7%]. From step𝑡0 + 1 onward, whenever𝐸𝑡 < 𝑀 𝑡 it must sell
ℓ𝑡 =
⌈
𝛼 |𝑞𝑡 |
⌉
(2)
lots at market, where𝛼 ∈ [ 0, 1] is the world’s liquidation strength. Because forced sales lower the price and therefore
equity, the rule can repeat over consecutive steps and form a liquidation spiral.
The strengths𝛼 and 𝛽 are both held at zero until the shock order has filled, and they define the four world strata used
in sampling: neither mechanism, liquidation only, withdrawal only, or both (Section4.1).
3.5 Reflexive strategy ecology
The adaptive participant holds shares(𝑠F, 𝑠Tr) over two candidate strategies, initialized at( 1 2 , 1 2 ). Both candidates are
inactive until the shock order has filled. The FUNDAMENTAL candidate buysmin{80, 4(𝑣 −ask −fee)} lots when the ask is
below value net of fees, sells symmetrically when the bid is above it, and otherwise does nothing. The TREND candidate
is a fixed, signal-independent order pair that sells 160 lots and then buys back 80, a net sale of 80 lots. Each step after the
shock, the participant draws one candidate with probabilities(𝑠F, 𝑠Tr) and submits it at market.
When the strategy mix evolves, the simulator first executesshadow trades: at the point just before the adaptive partici-
pant’s real order, each candidate is executed on its own copy of the exchange. At the start of the next step, after the maker
re-quotes, each shadow position is marked to the refreshed midpoint, giving one-step counterfactual profits𝜋F, 𝜋Tr (net of
fees, in half-tick cash units). Shares are then updated by a multiplicative replicator rule,
𝑠′ 𝑖 ∝ 𝑠𝑖 (1 + 𝜂 (𝜋𝑖 − min𝑘 𝜋𝑘)), 𝜂 = 10−3, (3)
with exact integer normalization in parts per million. An intervention therefore affects not only the current order book
but also the strategy mix that generates future order flow. When the mix is fixed, the adaptive participant still trades, but
shadow trades and Eq. (3) are disabled and the shares stay at( 1 2 , 1 2 ).
3.6 Switchable mechanism stages
Mechanisms are enabled cumulatively in five stages (Figure3a): a mechanical stage with only maker, noise, leveraged
exposure,shock,andinterventions; +impact,whichaddspersistentimpact; +withdrawal,whichaddsliquiditywithdrawal;
+leverage, which adds margin-driven liquidation, the fundamental and trend traders, and the adaptive participant with a
fixed mix; and+evolution, which adds shadow trades and replicator updates. Our experiments use two laboratories whose
dynamics differ in exactly one mechanism. Thefixed-mixlaboratory runs the+leveragestage. Theadaptivelaboratory
runs the full+evolution stage, which is also the configuration of every target. The first three stages are implemented but
not used in the experiments reported here.
3.7 Determinism, replay, and seed hygiene
Counter-based randomness.Random numbers are not drawn from a stateful generator. Each draw is the top 53 bits of
an HMAC-SHA256 of its address—namespace, step, entity, and draw index—under a key derived from the seed. Draws
are therefore independent of call order and of the market state. Every step consumes exactly ten draws (one reserved
for fundamental innovations, which are disabled in this construction; eight for noise traders; and one for the adaptive
participant), and each draw is recorded and recomputed during verification. All arms that share a seed, such as the two
interventions in the same repeat, thus face identical random inputs: their contrasts are evaluated under common random
numbers.
Eventsourcingandreplay. Theexchangeappendseveryorderacceptance,rejection,fill,rest,cancellation,andcancel
rejection to an event log with contiguous identifiers and non-decreasing steps, and maintains a running SHA-256 over its
canonical serialization. A replayer rebuilds the full state from events alone and re-validates risk admission, price–time
priority, resting prices, fill quantities, counterparties, and fees.
Seed hygiene. Seeds are derived by hashing a domain tag, master entropy, the world constructor’s hash, the cohort,
and the repeat index. Only a commitment to each seed is stored; seeds that collide with any previously used commitment
are re-derived. In the prospective study this yields 384 unique seeds (24 worlds× 2 cohorts× 8 repeats), and each seed is
simulated for ten run roles (initial observation, control, three paired experiments, and two interventions) in both laboratory
configurations: 7,680 logical runs, or 4,608 after deduplicating identical executions.
5

(a) Mechanisms enabled in each stage
Mechanical +impact +withdrawal +leverage +evolution
Persistent impact of the shock
Liquidity withdrawal (Eq. 1)
Margin-driven liquidation (Eq. 2)
Fundamental and trend traders
Adaptive participant (fixed mix)
Shadow trades + replicator (Eq. 3)
fixed-mix
laboratory
adaptive lab.
and targetimplemented; not used in these experimentsAll stages: maker, noise flow, leveraged exposure, shock, and both interventions.
(b) Amplification loops and intervention entry points
Price
decline
Shock sale
(step 8)
Margin
deficit
Forced
selling
Maker
stress
Thinner
ladder
𝛼𝛽
liquidation loop
withdrawal loop
LEVERAGE_CAP
sell half, step 4
LIQUIDITY_BACKSTOP
40-lot bid each step
(c) Evolving strategy mix (adaptive only)
Exchange
at step 𝑡
shadow FUND.
shadow TREND
mark at mid
of step 𝑡+1
replicator update
𝑠′ 𝑖 ∝ 𝑠𝑖 (1+𝜂 Δ 𝜋𝑖 ) draw strategy, real order
𝜋F, 𝜋 Tr
𝑠
order
flow
an intervention changes𝜋𝑖, hence the future mix
Figure3: Switchablemechanisms. (a) Mechanisms are enabled cumulatively; filled circles mark the active ones. The two laboratories
differ only in the outlined last row. (b) The shock’s price decline feeds a liquidation loop (red; strength𝛼) and a withdrawal loop (teal;
strength 𝛽). Thedeleveraginginterventionshrinkstheleveragedinventorybeforetheshockandsocapsthemargindeficit; thebackstop’s
resting bid offsets the thinning of the ladder. (c) With an evolving mix, each step forks both candidate strategies onto exchange copies,
marks them one step later, and re-weights the mix (Δ𝜋𝑖 = 𝜋𝑖 − min𝑘 𝜋𝑘).
4 The decision task
4.1 World population
A world is a parameterization of the crash construction. Each world draws a liquidation strength𝛼 and a withdrawal
strength 𝛽 uniformly from [0.05, 1] and then sets the inactive one to zero according to its stratum: neither mechanism,
liquidation only, withdrawal only, or both. It also draws the shock size (160–240 lots), the leveraged exposure (160–240
lots), the leveraged trader’s cash (84k–124k, raised if necessary to satisfy the20× leverage limit), the maintenance margin
𝜇, the maker depth ¯𝑄, and the stress scale𝜅 (Appendix A). Candidate worlds are rejected only for schema violations or
duplicate constructors, never on the basis of outcomes.
4.2 Interventions
The agent chooses one of two interventions, both taking effect at step 4, four steps before the shock.
• LEVERAGE_CAP (deleveraging): a one-time deleveraging sale in which the leveraged trader sells⌈|𝑞|/2⌉ lots at market,
halving its position; the intervention account also buys two lots at market. Despite its identifier, it imposes no lasting
leverage limit.
6

• LIQUIDITY_BACKSTOP: the intervention account buys one lot at market and then, at every step from step 4 onward, posts
a single resting 40-lot bid at the best bid, cancelling the previous step’s unfilled bid.
An intervention is feasible in a world if, in all eight target repeats, every scheduled marketable order (exposure build,
intervention trades, shock, and forced liquidations) executes in full, every backstop bid rests, and no order is rejected by
risk admission. Regret is defined only for feasible chosen actions.
4.3 Utility and regret
For one native repeat, the utility of intervention𝑎 is
𝑈 (𝑎) = −
𝑇∑
𝑡=𝑡0
max{0, 𝑚 𝑡0 −1 − 𝑚𝑡 (𝑎)} − 𝐶I (𝑎) + 𝐶L (𝑎) 𝜆 , (4)
with 𝑡0 = 8, 𝑇 = 96, and 𝑚𝑡 the reference price in half-ticks. The first term is the area by which the reference price falls
below its pre-shock level (Figure2a). The second term charges implementation costs inside the market:𝐶I is the fees paid
bythe interventionaccount (including backstopfills),𝐶L thefeespaidbythe leveragedtrader on thedeleveragingsale, and
𝜆 = 100 a fixed cost scale. These are market costs of the intervention, not costs of querying the agent. LetA𝑤, 1− 𝑗 be the
feasible interventions in target cohort1 − 𝑗 and ¯𝑈𝑤, 1− 𝑗 (𝑎) the mean of (4) over its eight repeats. The regret of a decision
made with laboratory cohort𝑗 is
R𝑤, 𝑗 (𝑎) = max 𝑎′ ∈ A𝑤, 1− 𝑗 ¯𝑈𝑤, 1− 𝑗 (𝑎′) − ¯𝑈𝑤, 1− 𝑗 (𝑎). (5)
With two feasible interventions, regret is zero for an optimal choice and equals the target utility gap otherwise. Lower
mean regret therefore means avoidingcostly mistakes, not merely making more correct choices. Because every feasible
intervention is executed on the same target repeats, Eq. (5) is exact counterfactual ground truth for those eight realized
repeats; it is a finite-sample estimate of the world’s expected regret. Its units are those of the simulator objective; a
monetary interpretation would require external calibration.
4.4 Experiments and observations
Experiment menu.Each experiment is a paired comparison on the eight laboratory repeats, using the same seed for both
arms. LEVERAGE compares the deleveraging arm with an otherwise identical arm whose deleveraging trade is removed;
LIQUIDITY does the same for the backstop bids; andNULL compares the control arm with itself. Each experiment therefore
isolates the effect of the intervention’s market action, but the two experiments use different controls, so their effects are not
directly on a common baseline.
Summary packets.An experiment returns an aggregate over the eight repeats of the treated arm’s public statistics—
return, spread, volume, depth, reference drawdown, order flow, price impact, strategy and adaptation statistics, quote-
availability statistics, and counts of forced liquidations and maker order cancellations—together with the paired utility
difference (mean, 5th/50th/95th percentiles, and a per-step effect size). Packets never contain target-cohort outcomes.
Initial observation.Every condition begins with a public message of the same form: an eight-repeat summary of a
shock-freecontrol run on the laboratory seeds, simulated in the condition’s laboratory configuration; the public objective;
the names of the two candidate amplification mechanisms and a graph of their possible causal paths to utility; the transfer
context (laboratory configuration, adaptive target, disjoint randomness); and the experiment budget and menu. Across
conditions, only the stated laboratory configuration and the budget and menu (none under OBSERVE-ONLY) differ. Because
theinitialruncontainsnoshock,anagentwithoutexperimentsmustinferthecrashdynamicsfromthisstructuraldescription
alone.
5 Experimental protocol
5.1 Information conditions
The agent interacts through two strict JSON tools,run_experiment and submit_decision. All conditions are scored
on adaptive targets:
• OBSERVE-ONLY: the initial observation only;run_experiment is not offered.
7

• ADAPTIVE-LAB: up to eight experiment calls in the adaptive laboratory.
• FIXED-MIX-LAB: up to eight experiment calls in the fixed-mix laboratory.
• PLACEBO-TOOLS: identical tooling, but every call returns one fixed packet—theLEVERAGE packet of a single previously
examined world—with all paired-difference fields set to zero (prospective study only).
Each experiment’s packet is prepared once; repeating a call returns the same packet and consumes budget, so eight calls do
not imply eight independent experiments. The ADAPTIVE-LAB–FIXED-MIX-LAB contrast isolates the evolving strategy mix
(Figure 3a) together with the stated laboratory configuration, rather than comparing a generic “unrealistic” market with
a “realistic” one. Because the placebo packet contains real crash statistics from another world, PLACEBO-TOOLS separates
world-specific evidence from tool interaction combined with generic crash information.
5.2 Agents and interaction
The primary agent is ChatGPT 5.6.4, evaluated in its three served variants Sol, Terra, and Luna (API model identifiers
gpt-5.6-sol, gpt-5.6-terra, and gpt-5.6-luna). Each variant is analyzed as a separate deployment. GPT-5.5 is
a supplementary deployment evaluated in the exploratory study only (AppendixB). Requests use temperature zero, one
completion, a 4,096-token completion limit, and no parallel tool calls. An episode allows at most 32 turns with one tool
call each. Once the experiment budget is spent, or during the last two of the 32 turns, onlysubmit_decision is offered
and the request forces a tool call. The first legal submission is final. Malformed or illegal calls receive a deterministic
error message and consume a turn; a third error is terminal. The agent’s history contains only the public message, its own
messages and tool calls, and tool results: target outcomes, feasibility, optimal actions, and correctness are never revealed,
and completed nonoptimal decisions are never retried.
5.3 Studies and statistical analysis
Prospective confirmation. After the primary protocol, population, and analysis were fixed in an internal specification
(not a public registry), we sampled 24 new worlds, excluding all previously examined constructors and seed commitments,
with six worlds in each stratum. Within each world and cohort, the order of conditions was rotated. The design crosses 24
worlds, two transfer directions, four conditions, and three deployments, for 576 planned decisions.
Exploratory study. An earlier study used 24 previously examined worlds, two directions, and three conditions
(OBSERVE-ONLY, ADAPTIVE-LAB, FIXED-MIX-LAB) for four deployments, again 576 decisions, with the same tool interface.
Its intervals were specified after observing outcomes and are descriptive.
Primary contrast.For each deployment the primary contrast is the paired meanΔ = mean𝑤, 𝑗
[
RADAPT 𝑤, 𝑗 − ROBS 𝑤, 𝑗 ] over
the48world–directionunits. Uncertaintyisestimatedwith10,000bootstrapresamplesofwholeworldswithinstrata[ 3,7],
preserving both directions and all conditions of each resampled world. The prespecified criterion is met whenΔ < 0, the
nominal 95% interval lies entirely below zero, and all 48 pairs are available. Deployments are analyzed separately; we
make no pooled or multiplicity-adjusted claim.
6 Results
6.1 Prospective confirmation on new worlds
Of the 576 planned prospective decisions, 362 were scored, 123 ended without an action (empty outputs), and 91 Sol
decisions were blocked by an infrastructure failure. Luna completed all 192 of its decisions. Its mean regret falls from
8.878 under OBSERVE-ONLY to 3.785 under ADAPTIVE-LAB:Δ = −5.092, with nominal 95% interval[−9.507, −1.028]
(Table2, Figure4). This is a 57.4% reduction in mean regret and meets the prespecified primary criterion.
Sol and Terra produced 88 and 82 scored decisions of 192, leaving only 20 and 16 of 48 complete primary pairs, re-
spectively. Their planned primary comparisons therefore remain unresolved; we do not substitute complete-case estimates
for them.
6.2 What the controls establish
Placebo. ForLuna,thesecondaryADAPT −PLACEBOdifferenceis −2.724withinterval [−6.263, 0.972],andPLACEBO −OBS
is −2.369 with interval [−6.145, 1.360]. The prespecified secondary FIXED −OBS contrast is −6.218 with interval
[−10.645, −2.269], so the fixed-mix laboratory also improves on observation alone. Its post hoc contrast with the placebo,
8

Condition Mean regret↓ Optimal actions Scored / planned Difference from OBSERVE-ONLY
OBSERVE-ONLY 8.878 30/48 48/48 —
PLACEBO-TOOLS 6.509 33/48 48/48 −2.369
ADAPTIVE-LAB (primary) 3.785 37/48 48/48 −5.092
FIXED-MIX-LAB 2.660 44/48 48/48 −6.218
Table 2: Prospective results for Lunaon 24 newly sampled worlds (48 world–direction units). Optimal-action counts include any
feasible utility maximizer. The last column is the paired mean difference from OBSERVE-ONLY; only ADAPTIVE-LAB versus OBSERVE-
ONLY is the prespecified primary contrast, and the others are secondary (intervals in Figure4b).
0 2 4 6 8 10
FIXED-MIX-LAB
ADAPTIVE-LAB
PLACEBO-TOOLS
OBSERVE-ONLY 8.878 (30/48)
6.509 (33/48)
3.785 (37/48)
2.660 (44/48)
Mean regret (lower is better)
(a) Mean target regret, Luna
−10 −5 0
ADAPT−FIXED
ADAPT−PLACEBO
PLACEBO−OBS
FIXED−OBS
ADAPT−OBS
mean 95% interval
−5.09 [ −9.51, −1.03]
−6.22 [ −10.65, −2.27]
−2.37 [ −6.15, 1.36]
−2.72 [ −6.26, 0.97]
1.13 [ −1.98, 3.76]
Regret difference (< 0 favors first)
(b) Paired differences
Figure 4: Laboratory access lowers Luna’s regret relative to observation alone(prospective study, 24 worlds). (a) Mean target
regret per condition; parentheses give optimal-action counts. (b) Paired mean differences with nominal 95% stratified world-bootstrap
intervals (OBS = OBSERVE-ONLY, ADAPT = ADAPTIVE-LAB, FIXED = FIXED-MIX-LAB, PLACEBO = PLACEBO-TOOLS). The shaded row is the
prespecified primary contrast. Among the secondary contrasts, the fixed-mix laboratory also improves on OBSERVE-ONLY, whereas the
contrasts against the placebo and between the two laboratories are inconclusive.
FIXED −PLACEBO = −3.849, has interval[−8.395, 1.158] under the same bootstrap draws. These controls leave uncertain
how much of the benefit comes from world-specific experimental evidence rather than from tool interaction and generic
crash information. The primary result concerns the complete laboratory-access condition relative to OBSERVE-ONLY.
Laboratory design. An evolving strategy mix in the laboratory shows no clear advantage. Luna’s prospective
ADAPT−FIXED difference is 1.126 with interval [−1.983, 3.756], and all four exploratory ADAPT−FIXED intervals also
include zero (Table3). The interval admits both a benefit and a cost of the evolving mix; it does not establish that the two
laboratories are equivalent.
Binaryoutcomes. Regretweightseachmistakenchoicebyitstargetutilitygap. Luna’soptimal-actioncountalsorises
from 30 to 37 of 48, but the prespecified binary companion tests do not meet their directional criterion (AppendixB). The
primary evidence therefore concerns avoided loss rather than accuracy.
Randomization check. Percentile intervals from 24 resampled clusters can be anti-conservative, so we add a post
hoc exact sign-flip test. It enumerates all224 sign assignments of the 24 world-level mean differences. For ADAPT−OBS,
13 worlds favor ADAPTIVE-LAB, 7 favor OBSERVE-ONLY, and 4 tie; the test gives𝑝 = 0.037 in the prespecified direction
and 𝑝 = 0.075 two-sided. For FIXED−OBS the corresponding values are𝑝 = 0.009 and 𝑝 = 0.018. The direction of the
primary effect is therefore robust to the inference method, but its two-sided strength is borderline at 24 worlds.
How the agent used the laboratory.Luna made 4.71 experiment calls on average with ADAPTIVE-LAB (range 4–7),
4.52withFIXED-MIX-LAB(2–6),and4.25withPLACEBO-TOOLS(3–7),outofeight. Becausethemenuhasthreeexperiments
and repeated calls return the same packet, the budget always sufficed to observe the complete menu, and no Luna episode
exhausted it. The improvement thus does not come from more calls: the placebo episodes were similar in length but
returned no world-specific evidence. Table6 reports calls and outcomes for every deployment and condition.
6.3 Exploratory evidence across deployments
In the exploratory study, all 576 decisions across Sol, Terra, Luna, and the supplementary GPT-5.5 deployment were
scored, and each mean uses 48 world–direction units (Table3, Figure5). Laboratory access lowers mean regret for all four
9

Deployment OBSERVE-ONLY ADAPTIVE-LAB FIXED-MIX-LAB ADAPT −OBS [95% int.] ADAPT −FIXED [95% int.]
Sol 6.121 (37) 0.764 (42) 1.091 (46) −5.357 [−8.951, −2.195] − 0.327 [−1.925, 0.786]
Terra 19.902 (18) 3.550 (40) 4.441 (41) −16.352 [−22.760, −9.686] − 0.891 [−5.934, 4.422]
Luna 7.676 (36) 4.551 (39) 3.287 (43) −3.125 [−8.181, 2.226] 1.264 [−3.186, 5.660]
GPT-5.5 (supp.) 10.017 (31) 1.575 (45) 3.160 (44) −8.441 [−12.393, −4.872] − 1.585 [−4.236, 0.386]
Table 3: Exploratory mean target regreton 24 previously examined worlds (48 units per cell); parentheses give optimal-action
counts out of 48. Intervals are descriptive and were specified after observing outcomes. Terra combines two recorded configurations
(Appendix B). GPT-5.5 is supplementary; no pooled effect is estimated.
0 5 10 15 20
GPT-5.5 (supp.)
Luna
Terra
Sol −5.36 [ −8.95, −2.20]
−16.35 [ −22.76, −9.69]
−3.13 [ −8.18, 2.23]
−8.44 [ −12.39, −4.87]
ADAPT−OBS [95%]
Mean target regret (lower is better)
OBSERVE-ONLY FIXED-MIX-LAB ADAPTIVE-LAB
Figure 5: Exploratory study: laboratory access lowers mean regret for every deployment.Grey bars span OBSERVE-ONLY to
ADAPTIVE-LAB; diamonds mark FIXED-MIX-LAB. Right: post hoc, descriptive world-bootstrap intervals for ADAPT−OBS. Worlds were
previously examined, so these results motivated, rather than confirm, the prospective study.
deployments. Post hoc world-bootstrap intervals for ADAPT−OBS exclude zero for Sol, Terra, and GPT-5.5; Luna’s interval
includes zero. These results motivated the independent prospective evaluation above.
6.4 How much decision information does each laboratory retain?
A simulator can preserve the best action without reproducing every aspect of its utility. To separate these properties, we
use selectors that observe the complete laboratory utility of both interventions, choose the higher one, and commit before
independent evaluation on the adaptive target. Table4 shows that both laboratories preserve the target-optimal choice in
nearly all 48 exploratory units. The selectors receive both full laboratory utilities, whereas the LLM agents receive public
experiment summaries; this diagnostic therefore measures the decision information a laboratory retains, not a comparison
under equal information.
7 Discussion
The value of an experiment is the decision it changes.The task links an agent’s research process to a consequence:
avoided intervention loss. Writing¯𝑅𝑏 for mean regret under an experimental budget of𝑏 calls, the gross value of experi-
mentation is
𝑉𝑏 = ¯𝑅0 − ¯𝑅𝑏, (6)
the loss avoided relative to observation alone. For Luna on new worlds,𝑉8 = 5.092 with the adaptive laboratory. This
quantity makes experimental usefulness comparable across agents, budgets, and laboratories on a common scale, and a
resource-efficiency analysis could weigh it against measured acquisition and inference costs.
Which simulator details matter?For an agent, the relevant question is whether an evolving strategy mix improves
the final choice between deleveraging and a liquidity backstop. In our data it does not demonstrably do so: the prospective
ADAPT−FIXED interval admits either sign, and complete-utility selectors from both laboratories recover nearly all target-
optimal actions. This suggests a concrete evaluation practice: before treating added dynamics as necessary for a task,
test whether they change the intervention ranking or reduce target regret [13, 18]. Because the simulator’s mechanisms
are switchable by stage, the same test can be applied to each stage. Runtime savings and transfer to real markets remain
separate empirical questions.
10

Laboratory utility selector Optimal target actions Mean target regret
Fixed-mix laboratory→ adaptive target 47/48 0.3802
Adaptive laboratory→ adaptive target 46/48 0.5895
Table 4: Exploratory action-ranking diagnostic.Each selector observes the complete laboratory utilities of both interventions and
commits before independent target evaluation. Nonzero target regret reflects the remaining transfer errors.
Limitations. The evidence covers one synthetic crash construction and two interventions, each with a single fixed
implementation(onedeleveragingsale; onebackstopsize). Thefundamentalvalueisconstant, makerdepthfallsonafixed
scheduleattheshock,theevolvingstrategymixhastwocandidates(oneofthemsignal-independent),andtheshadow-trade
horizon is one step. New constructors and independent target seeds support transferwithin this construction, not to other
constructions or to historical markets. With 24 worlds, the primary effect is clear in direction but modest in two-sided
strength (exact sign-flip𝑝 = 0.075). Incomplete Sol and Terra records limit prospective cross-deployment conclusions,
andtheplacebocomparisonleavesthecontributionofworld-specificevidencerelativetotoolinteractionandgenericcrash
information uncertain. The positive primary result therefore concerns the full laboratory-access condition for Luna within
this construction. Finally, regret is measured in simulator utility units and is not calibrated to monetary outcomes.
Next measurements.The most discriminating next comparison is a strong fixed acquisition schedule with the same
observations and decision rule. It would test whether an agentselects experiments well, beyond benefiting from access to
informative packets.
8 Conclusion
CrashGym measures the decision value of experimentation in a deterministic, replayable market laboratory. Independent
target realizations connect acquired evidence to consequential intervention choices and make regret exact for the realized
target repeats, and staged amplification mechanisms make simulator detail testable by its contribution to a downstream
choice. Prospective results support a laboratory-access benefit for Luna, and a separate exploratory study shows the same
descriptive direction across four deployments. The resulting question for financial agents is concrete: which experiments,
observations, and simulator details are worth acquiring for the decision at hand?
References
[1] M. K. Brunnermeier and L. H. Pedersen. Market liquidity and funding liquidity.Review of Financial Studies, 22(6):2201–2238,
2009.
[2] D. Byrd, M. Hybinette, and T. H. Balch. ABIDES: Towards high-fidelity market simulation for AI research. arXiv:1904.12066,
2019.
[3] A. C. Cameron, J. B. Gelbach, and D. L. Miller. Bootstrap-based improvements for inference with clustered errors.Review of
Economics and Statistics, 90(3):414–427, 2008.
[4] K. Chaloner and I. Verdinelli. Bayesian experimental design: A review.Statistical Science, 10(3):273–304, 1995.
[5] Z. Chen et al. CausalGame: Benchmarking causal thinking of LLM agents in games. arXiv:2607.04293, 2026.
[6] P. L. Donti, B. Amos, and J. Z. Kolter. Task-based end-to-end model learning in stochastic optimization. InAdvances in Neural
Information Processing Systems, 2017.
[7] B. Efron. Bootstrap methods: Another look at the jackknife.Annals of Statistics, 7(1):1–26, 1979.
[8] A. N. Elmachtoub and P. Grigas. Smart “predict, then optimize”.Management Science, 68(1):9–26, 2022.
[9] J. D. Farmer and D. Foley. The economy needs agent-based modelling.Nature, 460:685–686, 2009.
[10] S. Frey et al. JAX-LOB: A GPU-accelerated limit order book simulator to unlock large scale reinforcement learning for trading.
arXiv:2308.13289, 2023.
[11] J. Geanakoplos. The leverage cycle.NBER Macroeconomics Annual 2009, 24:1–66, 2010.
[12] D. K. Gode and S. Sunder. Allocative efficiency of markets with zero-intelligence traders: Market as a partial substitute for
individual rationality.Journal of Political Economy, 101(1):119–137, 1993.
[13] C. Grimm, A. Barreto, S. Singh, and D. Silver. The value equivalence principle for model-based reinforcement learning. In
Advances in Neural Information Processing Systems, 2020.
[14] R. A. Howard. Information value theory.IEEE Transactions on Systems Science and Cybernetics, 2(1):22–26, 1966.
11

[15] Q. Huang, J. Vora, P. Liang, and J. Leskovec. MLAgentBench: Evaluating language agents on machine learning experimentation.
In International Conference on Machine Learning, 2024.
[16] P. Jansen et al. DiscoveryWorld: A virtual environment for developing and evaluating automated scientific discovery agents.
arXiv:2406.06769, 2024.
[17] E. Kıcıman, R. Ness, A. Sharma, and C. Tan. Causal reasoning and large language models: Opening a new frontier for causality.
arXiv:2305.00050, 2023.
[18] N. Lambert, B. Amos, O. Yadan, and R. Calandra. Objective mismatch in model-based reinforcement learning. InLearning for
Dynamics and Control, 2020.
[19] B.LeBaron. Agent-basedcomputationalfinance. In Handbook of Computational Economics,volume2,pages1187–1233.Elsevier,
2006.
[20] H. Li et al. InvestorBench: A benchmark for financial decision-making tasks with LLM-based agent. InProceedings of ACL,
pages 2509–2525, 2025.
[21] D. V. Lindley. On a measure of the information provided by an experiment.Annals of Mathematical Statistics, 27(4):986–1005,
1956.
[22] C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, and D. Ha. The AI Scientist: Towards fully automated open-ended scientific
discovery. arXiv:2408.06292, 2024.
[23] H.RaiffaandR.Schlaifer. Applied Statistical Decision Theory. DivisionofResearch,GraduateSchoolofBusinessAdministration,
Harvard University, 1961.
[24] T. Schick et al. Toolformer: Language models can teach themselves to use tools. InAdvances in Neural Information Processing
Systems, 2023.
[25] A. Shleifer and R. Vishny. Fire sales in finance and macroeconomics.Journal of Economic Perspectives, 25(1):29–48, 2011.
[26] S. Thurner, J. D. Farmer, and J. Geanakoplos. Leverage causes fat tails and clustered volatility.Quantitative Finance, 12(5):695–
707, 2012.
[27] J. Tobin et al. Domain randomization for transferring deep neural networks from simulation to the real world. InIEEE/RSJ
International Conference on Intelligent Robots and Systems, 2017.
[28] S. Vyetrenko, D. Byrd, N. Petosa, M. Mahfouz, D. Dervovic, M. Veloso, and T. Balch. Get real: Realism metrics for robust limit
order book market simulations. InACM International Conference on AI in Finance, 2020.
[29] R. Wang, P. Jansen, M.-A. Côté, and P. Ammanabrolu. ScienceWorld: Is your agent smarter than a 5th grader? InProceedings of
EMNLP, 2022.
[30] S. Wu et al. BloombergGPT: A large language model for finance. arXiv:2303.17564, 2023.
[31] Y. Xiao et al. TradingAgents: Multi-agents LLM financial trading framework. arXiv:2412.20138, 2024.
[32] J. Yang et al. CausaLab: A scalable environment for interactive causal discovery toward AI scientists. arXiv:2605.26029, 2026.
[33] S. Yao et al. ReAct: Synergizing reasoning and acting in language models. InInternational Conference on Learning Representa-
tions, 2023.
[34] Y. Yu et al. FinMem: A performance-enhanced LLM trading agent with layered memory and character design. arXiv:2311.13743,
2023.
A Simulator parameters
B Protocol and evidence details
Models. Sol, Terra, and Luna are the three served variants of ChatGPT 5.6.4 ( gpt-5.6-sol, gpt-5.6-terra,
gpt-5.6-luna); Sol was reached through a separate API gateway. Every request records the exact requested model
identifier, and the analysis rejects any lane with mixed identifiers. GPT-5.5 is supplementary in the exploratory study and
absent from the prospective confirmation. The exploratory Terra results combine 143 decisions under one recorded config-
uration and one OBSERVE-ONLY decision under another; equivalence of the underlying checkpoints was not independently
verified.
Interaction limits. Besides the turn and correction limits in Section5, an episode terminates without an action if
a response cannot be parsed, a single turn exceeds 10,000 output tokens, or the episode exceeds 320,000 output tokens.
Provider-side reasoning content is not returned to the agent in later turns.
Samplinganduncertainty. Theprospectivepopulationcontainssixworldsineachoffourstrata. Thetwoseedcohorts
have eight repeats each, giving 384 unique seed commitments. The analysis uses 10,000 stratum-preserving whole-world
bootstrapdrawswithPCG64seed20260908andlinear2.5/97.5percentiles. Intervalsarenominalanddeployment-specific,
12

Parameter Value
Fixed across worlds
Horizon; shock step; intervention step; exposure step𝑇 = 96; 𝑡0 = 8; step 4; step 1
Tick size; fee; cost scale𝜆 1 tick; 1 per lot per counterparty; 100
Fundamental value𝑣 10,000 ticks, constant
Risk limits position 106 lots; notional≤ 20× initial cash
Marketable-order band 100 ticks through the best opposite quote
Maker ladder 40 levels per side; half-spread 2 ticks;¯𝑄 lots/level at step 0 and from the shock
on, 400 lots/level in steps 1–7; stress floor 25%
Noise flow 8 orders/step of 4 lots
Fundamental and trend traders 4 lots per tick of mispricing; 4 lots per half-tick of
𝑒𝑡 = trunc(( 3𝑒𝑡 −1 + 𝑟𝑡 −1)/4)
Persistent impact 40𝑥/𝐷0 ticks, 𝐷0 = 10 ¯𝑄 (top-10 step-0 bid depth)
Adaptive participant initial shares ( 1 2 , 1 2 ); FUNDAMENTAL capped at 80 lots; TREND pair
(−160, +80); 𝜂 = 10−3
Interventions deleveraging sells⌈|𝑞|/2⌉ (+2-lot account purchase); backstop: 1-lot purchase,
40-lot bid at best bid each step
Sampled per world
Strata neither / liquidation only / withdrawal only / both; 6 worlds each
Liquidation strength𝛼; withdrawal strength𝛽 uniform on[0.05, 1]; inactive one set to 0
Shock size; leveraged exposure {160, 180, 220, 240} lots sold;{160, . . . , 240} lots bought (step 20)
Leveraged cash {84k, . . . , 124k} (step 10k), raised to cover the20× limit
Maintenance margin𝜇 {3%, . . . , 7%} (step 1%)
Maker depth ¯𝑄; stress scale𝜅 {24, . . . , 56} lots (step 8);{24, . . . , 56} half-ticks (step 8)
Backstop level size† {24, . . . , 56} lots (step 8); not used by this construction
Table5: Parametersofthecrashconstruction usedinbothstudies. †Sampledandincludedintheconstructorhash(henceinduplicate
screening), but the backstop size is fixed at 40 lots in this construction.
with no joint or multiplicity-adjusted success claim. The exploratory intervals come from a post hoc analysis and are
descriptive.
Missingoutcomes. Theprospectivestudyendedwithnopendingdecisions: Luna192scored;Sol88scored,13empty,
and 91 infrastructure-blocked; Terra 82 scored and 110 empty. The infrastructure stop followed a permanent request error.
Missing actions receive no numerical regret. The 110 Terra failures are provider responses that could not be parsed as a
message; the 13 Sol failures are episodes ending after three consecutive responses without exactly one tool call. Table6
shows that Terra’s failures concentrate in the three tool conditions (94 of 110), so missingness depends on condition and
completepairsarenotarandomsubsample. Thefull-denominatorprimarycomparisonsforSolandTerraarethereforenot
replaced by complete-case estimates. For transparency only, the complete-pair mean ADAPT−OBS differences are−8.221
for Sol (20 pairs) and−6.583 for Terra (16 pairs); these are not estimates of the planned contrasts. Separate post hoc
recovery attempts are outside the reported confirmation results.
Replay. An independent replay reproduces all 362 available prospective action scores and preserves the 214 missing
outcomes. A separate replay verifies the complete exploratory decision transcripts and all 576 scores.
Code and data availability.Source code, configurations, transcripts, and replay receipts are retained by the authors;
a public artifact package has not yet been released.
Binarycompaniontests. Theprespecifieddirection-specifictestsofLuna’soptimal-actionoutcomesyield 𝑝 = 0.5811
and 𝑝 = 0.3877. Neither meets the directional criterion, despite the supported primary regret reduction.
Metric interpretation.Utility combines the reference-drawdown objective with implementation costs, and the score
comparesthechoseninterventionwiththebestfeasibleoneonthesametargetrepeats. Experimentpacketsuseintervention-
specific controls, so their paired differences need not directly rank full target utilities. Successful use of these packets is
evidence of decision performance, not proof that an agent recovered the market’s latent causal structure.
13

Deployment Condition Scored Empty Blocked Mean calls (range)
Luna OBSERVE-ONLY 48 0 0 —
ADAPTIVE-LAB 48 0 0 4.71 (4–7)
FIXED-MIX-LAB 48 0 0 4.52 (2–6)
PLACEBO-TOOLS 48 0 0 4.25 (3–7)
Sol OBSERVE-ONLY 25 1 22 —
ADAPTIVE-LAB 22 4 22 4.45 (3–6)
FIXED-MIX-LAB 22 3 23 4.36 (3–6)
PLACEBO-TOOLS 19 5 24 4.42 (3–8)
Terra OBSERVE-ONLY 32 16 0 —
ADAPTIVE-LAB 17 31 0 4.35 (3–6)
FIXED-MIX-LAB 18 30 0 4.56 (4–6)
PLACEBO-TOOLS 15 33 0 4.13 (3–6)
Table 6: Prospective census and laboratory useby deployment and condition (48 planned decisions per row). Experiment calls are
counted over scored episodes, with a budget of eight.
14
