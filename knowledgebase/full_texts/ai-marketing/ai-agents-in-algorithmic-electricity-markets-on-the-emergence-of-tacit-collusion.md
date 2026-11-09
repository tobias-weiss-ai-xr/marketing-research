---
title: 'AI agents in Algorithmic Electricity Markets: On the Emergence of Tacit Collusion'
url: https://arxiv.org/abs/2608.26896
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Jakub Seredyński
- Georgios Tsaousoglou
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.26896
pages: 10
chars: 50361
fetched_at: '2026-11-08T13:10:23+00:00'
kb_version: 1
---

# AI agents in Algorithmic Electricity Markets: On the Emergence of Tacit Collusion

1
AI agents in Algorithmic Electricity Markets:
On the Emergence of Tacit Collusion
Jakub Seredy ´nski, Georgios Tsaousoglou
Abstract—As electricity market participants increasingly adopt
learning-based agents for their bidding strategies, electricity
markets are becomingalgorithmic. Evidence from algorithmic
markets in other domains shows that tacit collusion can arise
purely through independent learning. Moreover, electricity mar-
kets are typically oligopolistic and feature repeated interaction
among a small number of participants, making them structurally
susceptible to non-competitive behavior. In the face of these
observations, this paper investigates the hypothesis that tacit
collusion may emerge in electricity markets where participants’
actions are controlled by autonomous learning-based algorithms.
We model strategic bidding as a repeated game with imperfect
public monitoring, and model the participants’ emergent behav-
ior using multi-agent reinforcement learning. We propose a multi-
dimensional set of criteria (going beyond profit comparisons
against Nash equilibria) to assess whether the resulting behavior
constitutes tacit collusion. Our experimental results showcase that
such a danger is realistic for electricity markets: there are cases
where agents do learn to sustain supra-competitive outcomes that
are supportive of tacit collusion indicators, even though the agents
were never instructed to collude.
Index Terms—Electricity Markets, Multi-agent Reinforcement
Learning, Tacit Collusion, Strategic Behavior.
I. INTRODUCTION
A. Motivation and Research Question
C
OLLUSION in electricity markets refers to an agree-
ment among competing firms to coordinate their actions
towards avoiding competition and increasing their profits.
It is severely detrimental, not only to consumers who face
supra-competitive prices, but also to the market’s economic
efficiency in general. While collusion is associated with cartel-
like practices and is thereby strictly prohibited by law, the
more challenging case to deal with is when collusion istacit.
Definition:Tacit Collusionrefers to a group of oligopolists’
ability to coordinate, even in the absence of explicit agreement,
in order to raise prices or, more generally, increase profits at
the detriment of consumers [1].□
Importantly, the absence of a need for an explicit agree-
ment makes it possible for Tacit Collusion to emerge “au-
tonomously”. This is directly relevant to the new reality of
electricity markets where participants are increasingly out-
sourcing their market participation strategies to autonomous
learning-based algorithms, generally referred to as Artificial
Intelligence (AI) agents. Experience from other domains has
The authors are with the Department of Applied Mathematics and Computer
Science, Technical University of Denmark.
e-mail correspondance: geots@dtu.dk.
This work was supported by the Villum Young Investigator award (Project
no. 80181).
already established that AI agents, particularly Reinforcement
Learning (RL), often exhibit the ability to maximize their
prescribed reward (read: profit) in ways unforeseen by their
designers. The study in [2] demonstrates that independently
designed reinforcement-learning pricing algorithms can indeed
learn to sustain supracompetitive prices, in general contexts.
In the authors’ own words: “We find that the algorithms
consistently learn to charge supracompetitive prices, without
communicating with one another [...] The algorithms learn
these strategies purely by trial and error. They are not designed
or instructed to collude, they do not communicate with one an-
other, and they have no prior knowledge of the environment”.
Taken to electricity markets, such agents could give rise
to Tacit Collusion phenomena, even without the firms’ inten-
tion or awareness. Moreover, the fact that electricity markets
historically tend to be oligopolistic while also featuring re-
peated interaction among participants, makes them particularly
vulnerable to Tacit Collusion emergence. Motivated by the
possibility and implications of this phenomenon in electricity
markets, we put forward the following hypothesis:
Hypothesis:In an electricity market where the participants’
actions are controlled by autonomous learning-based algo-
rithms, Tacit Collusion may emerge.
B. Related Work
An electricity market comprises participants, each of which
is interested in optimizing its own profit. Thereby, studying
possibilities over electricity market outcomes involves mod-
eling the bidding strategy optimization problem of individual
participants, in an agent-based modeling fashion [3]. In the
earlier literature, a participant’s bidding strategy was predomi-
nantly modeled through bi-level programming (e.g. [4]), giving
rise to mixed-complementarity problems modeling the multi-
participant interactive decision-making [5], [6]. The recent
literature, however, has substantially pivoted toward learning-
based approaches, for at least three reasons:
•Learning algorithms are able to handle realistic aspects
of electricity markets such as complexity, partial ob-
servability, and stochasticity, departing from simplifying
assumptions arising from computational constraints of the
model [7].
•The model-free nature of learning algorithms makes them
a generic modeling tool which, taken to a sufficient level
of richness, can in principle reproduce a wide range of
different intelligent strategies [8], [9].
•Real market participants increasingly experiment with
learning-based bidding strategies [10]. This motivates the
arXiv:2608.26896v1  [cs.AI]  27 Aug 2026

2
RL framework, in particular, to be leveraged as a suitable
modeling framework that captures the exploration aspect
of modern algorithmic trading.
RL has attracted special interest as a generic model for a
participant’s bidding strategy optimization problem [11], [12],
[13]. From a system perspective, when it comes to modeling
the interactive learning among several strategic participants
and the emergent outcomes thereof, the concept naturally
evolves into multi-agent RL (MARL) [14]. To that end, [15] ar-
gues for MARL-based fit-for-purpose simulators that retain the
market and physical features relevant to the research question
at hand, while [16] formulates day-ahead bidding with multiple
strategic generators as algorithmic traders and applies a MARL
algorithm to approximate Nash-equilibrium bidding. Recent
work on generator modeling further shows that simplified
bidding and marginal-cost representations can affect conclu-
sions in market-mechanism simulations, especially when re-
newable integration changes the operating regimes of thermal
generators [17].
The potential emergence of Tacit Collusion has been val-
idated by research in other domains, namely algorithmic
pricing, where RL agents have been shown to sustain supra-
competitive prices without communication or explicit collusive
instructions [2]. This result has been extended to sequential
pricing environments, where Q-learning algorithms may con-
verge either to collusive equilibria or to supra-competitive
price cycles [18]. Recent experimental evidence further com-
pares algorithmic and human collusion in the same market
environments, showing that self-learning pricing algorithms
can generate more collusive outcomes than human decision-
makers in some oligopoly settings [19].
Taken to the electricity-market setting, it is particularly
timely to understand the implications of algorithmic trading
and, in particular, whether Tacit Collusion can emerge endoge-
nously from the interaction of autonomous learning agents.
To that end, a MARL agent-based model is employed in
[3], where the authors investigate how the agents’ discount
factors affect the resulting market outcomes. More recently,
[20] explicitly investigates the emergence of Tacit Collusion
and define a collusive state as one in which the profit of each
participant exceeds that attained under all Nash equilibria.
While this provides a useful benchmark for identifying supra-
competitive outcomes, establishing such a condition requires
the computation of the Nash equilibria of the underlying
market game. This requirement substantially constrains the
complexity of the market model and makes the approach
difficult to extend to richer electricity-market settings.
C. Research Gap and Contributions
The emergence of algorithmic trading, and the risks it
poses for electricity markets, points to a major research need
around the emergence of Tacit Collusion. To our knowledge,
this phenomenon has been addressed by only a handful of
studies (namely [20] and [3]). These studies provide important
evidence that intelligent agents may learn supra-competitive
bidding strategies. Their identification of Tacit Collusion, how-
ever, is closely tied to the structure of the underlying market
game. In particular, [20] identifies collusion by comparing the
agents’ profits with those attained at all Nash equilibria. Such
an approach is informative in a stylized market model whose
equilibria can be fully characterized, but becomes difficult
to apply once the market model incorporates the structural
features of actual electricity markets.
More fundamentally, supra-competitive profits alone do not
establish Tacit Collusion: elevated profits can arise for rea-
sons unrelated to collusive coordination. Conversely, because
realistic market models rarely converge to a stage-game Nash
equilibrium, the absence of such convergence is, on its own,
equally uninformative about whether collusion has occurred.
In fact, in our numerical results in this paper, we present
examples on both ends: cases where supra-competitive out-
comes emerge which are, or are not necessarily, supportive of
a case for Tacit Collusion. Tacit Collusion is thus a subtle phe-
nomenon that resists identification through any single criterion
and calls instead for a multi-dimensional examination. This
motivates the contributions of this paper, positioned towards
investigating the Hypothesis defined in Section I-A:
1) We adopt Tacit Collusion criteria (beyond merely supra-
competitive outcomes) from other domains, with richer
experience in this context, and adapt them to the elec-
tricity market setting. We also propose a novel criterion
which quantifies the central characteristic of collusion as
defined in itsDefinition(cf Section I-A), in the context
of electricity markets.
2) We model emergent bidding profiles using a MARL
framework and examine their collusive properties across
multiple such criteria.
3) We experimentally investigate which market character-
istics (e.g. grid constraints’ tightness, demand level,
marginal costs’ variance) enhance the possibility of
emergent collusion.
The remainder of the paper is organized as follows. Section II
presents the system model. Section III defines the different
Tacit Collusion criteria of our study. Section IV presents
the experimental setting, including the details of the MARL
algorithm. Section V presents our experimental results, while
Section VI concludes the paper.
II. SYSTEMMODEL
A. Electricity Market
We consider a single-timeslot electricity market, operating
over a setNof buses, which is cleared by solving the standard
DC optimal power flow (OPF) problem. Specifically, a bus
n∈ Nfeatures an inelastic demandD n and a setI n of
energy-providing resources. The resources can generally be of
various types and technologies (including conventional power
plants, renewable energy sources, storage, flexible demand,
etc) but we will simply call them “generators” to simplify the
exposition. We denote the superset of generators (across all
nodes) byI= S n∈N In.
The active power flow from busnto busmis denoted as
fnm and is subject to line capacity bounds per
−Fnm ≤f nm ≤F nm,∀(n, m)∈ N 2,(1)

3
where, for pairs of buses that are not connected by a line,
we simply setF nm = 0. Denoting the output of a generator
i∈ In asq i, the power balance constraint at a node reads:
X
i∈In
qi −
X
m∈N
fnm = Dn,∀n∈ N.(2)
The phase angle at a busnis denoted asϕ n and is subject to
safety limits per
ϕn ≤ϕ n ≤ ϕn,∀n∈ N.(3)
The phase angles and the power flows are linked by the
standard DC power flow model:
fnm = Bnm(ϕn −ϕ m),∀(n, m)∈ N 2,(4)
whereB nm is the susceptance of transmission linenm.
The output of a generatori∈ Iis partitioned into a setS i
of segments, as in:
qi =
X
s∈Si
qi,s,∀i∈ I,(5)
where the outputq i,s of a segment is bounded by
0≤q i,s ≤Q s,∀s∈ S i, i∈ I.(6)
Finally, each generator declares a per-unit energy costc i,s
for each of its segmentss∈ Si, such that the operator receives
a piecewise linear cost function for each generator. The market
is cleared by solving the standard DC-OPF problem:
min
qi,qi,s,fnm,ϕn
n X
i∈I
X
s∈Si
ci,sqi,s
o
(7)
subject to
(1)−(4):Network constraints
(5)−(6):Generators’ constraints.
The optimal dual variableλ n of the power balance con-
straint (2) instantiates the Locational Marginal Price (LMP) of
noden. The market-clearing problem (7) is implemented se-
quentially for a set of instances (timeslots)Twhere in each in-
stancet∈ Tthe generators can submit different bidsc i,s[t]re-
sulting in timeslot-specific solutions

(q∗ i [t])i∈I,(λ n[t])n∈N  .
B. Agent-based Market Participation Strategies
A generator’s market participation strategy is instantiated
by an agent. We use the terms “agent” and “generator”
interchangeably and we index either byi. After each market-
clearing instancet, the stage profitπ i[t]ofiis
πi[t] =λ n(i)[t]q∗ i [t]−C i(q∗ i [t]).(8)
The first term is the generator’s revenue, withλ n(i)[t]be-
ing the LMP at busn(i)whereiis located. The second
term is the generator’s real cost for generating its dis-
patched quantityq ∗ i [t], which is given by the generator’s cost
functionC i :R→R.
The values forq ∗ i [t]andλ n(i)[t]are given from problem (7),
and are therefore affected by theactions, i.e. bids,(c i,s[t])s∈Si
of the focal agenti, as well as by those of the other agents.
This directly leads to the definition of the stage gameG:
•Players:i∈ I
•Actions:c i[t] = (ci,s[t])s∈Si
•Payoffs:π i[t]as in Eq. (8)
We consider agents that learn to improve their strategies
through experience. After each instance, an agent gets to
observe its own dispatch and profit, as well as the resulting
LMP at every node of the network:
oi[t] =

q∗ i [t], πi[t],(λ n[t])n∈N  .(9)
This gives rise to a repeated game with imperfect monitoring,
since an agent does not observe the actions or profits of other
agents but only a public signal (i.e. the LMPs) from which the
others’ actions and profits cannot be inferred. Furthermore,
we do not assume that agents know the structure of the
network or even the market mechanism and consider agents
that learn purely through experience. To that end, each agent
accumulates a private history of its actions and observations
(up toζepisodes behind):
hi[t] =

ci[t−1], oi[t−1],c i[t−2], oi[t−2], ...,ci[t−ζ], oi[t−ζ]

(10)
and selects its bid at each stagetaccording to astrategyσ i that
maps the current historyh i[t]to its decisionc i[t]. We denote
the joint strategy asσ= (σ i)i∈I. Based on the above, we can
define the objective of an agent as a search for a strategy that
maximizes its cumulative profits over time:
max
σi
n
Eσ
∞X
t=0
πi[t]
o
(11)
subject to
(8):Profits depend on actions,
ci[t] =σ i(hi[t]) :Actions are given by strategy and history
(10):The history stacks part actions and observations
(9):Observations are: dispatch, profit, and LMPs.
Problem (11) is intractable in general: each agent optimizes
its own strategy while the strategies of all other agents are un-
known and simultaneously evolving, making the environment
non-stationary from any single agent’s perspective. In line
with the learning-through-experience consideration, we adopt
Multi-Agent Reinforcement Learning(MARL) as a model of
how AI agents learn and play in practice. At each instancet,
every agentiselects a bidc i[t] =σ i(hi[t]), the market clears,
and each agent receives the observationo i[t]and uses it to
update its strategyσ i. This process is iterated over successive
instances, and the agents’ strategies co-evolve. The details of
the MARL algorithm will be presented in Section IV-C.
The output of this process is a joint strategy profileσ ∗ =
(σ∗ i )i∈I, representing the emergent bidding behaviour that
arises when self-interested agents learn to bid. The paper’s
Hypothesisthereby refers to analyzing the emergent joint
strategiesσ ∗ in terms of indications for Tacit Collusion. The
next section formalizes the Tacit Collusion indices to be used.
III. TACITCOLLUSION
In this section, we define three criteria that constitute
indicators of the emergent joint strategyσ ∗ being tacitly

4
collusive: Punishment of Deviation, Unsustainability under
Shortsight, and Short-term Profitability of Deviations. In the
three subsection below, we describe how each criterion is
instantiated in our electricity market context.
A. Punishment of Deviation Criterion
This criterion checks whether an agent that deviates from
the joint strategyσ ∗ and reverts to an explicitly competitive
strategy will face a punitive response by other agents.
A deviator reverting to a competitive strategy means that
it starts to optimize its short-term profits aggressively. In
our context, we can model such a situation by choosing
one agentjas the deviator and, after the MARL strategies
have converged toσ ∗, switching the deviator’s strategy to the
one that optimizes its stage profit under the assumption that
other agentsi̸=jcontinue to play their previous strategies
(specifically, their most recently observed ones). To implement
this, at each after-convergence staget, we forcej’s strategy
to the solution of the following bi-level optimization problem:
max
cj [t]
n
λn(j)[t]q∗ j [t]−C j(q∗ j [t]) o (12)
subject to
q∗ j [t], λn(j) ∈(7)
where the constraint specifies that the dispatch and LMP result
through the market clearing problem (7). Problem (12) can
be solved by casting the lower-level problem (7) as a set of
KKT conditions and introducing auxiliary binary variables to
handle the resulting complementarity constraints. This results
in a single-level mixed-integer linear program which can be
tackled by commercial solvers. The full derivation is ommited
here as it is fairly standard in the literature.
While the deviator is using its aggressive profit-maximizing
strategy (12), the other agents continue to play by the MARL
regime. A punitive response is considered to be one that has
other agents lowering their mark-ups in a way that reduces the
deviator’s profit. The test is considered positive if the post-
deviation dynamics display the qualitative pattern of punish-
and-forgive strategies:
•Immediately after the deviation, competitors temporarily
switch to more competitive (i.e. lower) bids, reducing
pricesandthe deviator’s market share;
•After a punishment phase, competitors gradually return
to their pre-deviation strategies, while prices recover.
B. Unsustainability under Shortsight Criterion
Two elements that generally facilitate Tacit Collusion are:
•agents playing the long game, by adopting a high discount
factor which increases the importance of future payoffs
over immediate ones;
•agents having memory of past actions and rewards, which
allows them to condition their behaviour on history;
The rationale of this criterion is that reducing or eliminating
these elements should make it substantially more difficult for
agents to learn coordinated strategies. In practice, this test
is implemented by executing the MARL algorithm under a
very low discount factor while also severely truncating the
memory of past actions and rewards. Compared to the baseline
case, this run would presumably result in more competitive
strategies, i.e. lower prices and profits.
C. Short-term Profitability of Deviations Criterion
Given that collusive outcomes are not Nash equilibria of the
stage game, one or more agents do have a profitable unilateral
strategy deviation. Yet the collusion is sustained when agents
refrain from switching to opportunistic strategies, despite
this being profitable in the short-run, presumably because
they understand that those would lead to down-the-road less
profitable outcomes. This criterion checks the emergent joint
strategyσ ∗ precisely for these two conditions: agents having
profitable unrealized deviations from it, and whether those, if
realized, would trigger joint adaptation dynamics that indeed
lead to less profitable trajectories.
Similarly to the first criterion, we instantiate profitable
deviations by solving the bi-level problem (12). This time,
however, we solve problem (12) iteratively and for every agent
in turn, thereby simulating a relapse into competitive (non-
collusive) strategy adaptation. The relevant algorithm is called
“Iterative Best Response” (IBR) or “diagonalization” and it
is widely used in the electricity markets’ literature (see e.g.
[21] and references therein) to approximate Nash Equilibria
under the so-called Equilibrium-Problem with Equilibrium-
Constraints (EPEC) model. The criterion considers thatσ ∗
passes the collusion test if, upon switching from MARL to
the IBR regime, the profits of the first deviating agents:
•increase at first, and
•they eventually drop below those underσ ∗, as the IBR
process continues towards a Nash Equilbirium.
The rationale is that, if both of these conditions hold true,
it means that each agent has a profitable unilateral deviation
which it doesn’t realize, possibly because it foresees that
it is not profitable under the other agents’ corresponding
competitive response, thereby staying true to a coordinated
(collusive) strategy.
IV. EXPERIMENTALSETTING
A. Electricity Market Setup
We conduct the experiments on a stylised seven-bus elec-
tricity market adapted from the case study of [20]. The
original system is an extended version of the well-known
Pennsylvania–New-Jersey–Maryland (PJM) five-node test sys-
tem and was designed as a compact networked market in
which strong collusive equilibria can arise. We use it here as a
controlled benchmark that preserves the elements needed for
our hypothesis: an oligopolistic supply side, inelastic nodal de-
mand, transmission constraints, and locational marginal prices.
The market contains four strategic generators located at
busesN 1,N 2,N 5, andN 6. Nodal demand is perfectly inelastic
and the market is cleared, at each instance, by the DC-OPF
problem (7). The resulting dispatch and nodal prices determine
each generator’s stage profit according to (8), where revenues
are computed at the LMP of the generator’s bus and costs are

5
TABLE I
STRATEGIC GENERATORS AND MARGINAL-COST CASES.
Generator BusP max i [MW] Marginal cost [EUR/MWh]
Low Medium High
G1 N1 42 20 20 20
G2 N2 35 20 20 20
G5 N5 40 20 30 40
G6 N6 40 20 10 1
computed using the generator’s true marginal cost. The main
generation and cost parameters used in the experiments are
reported in Table I.
All exogenous fundamentals are kept fixed within a sce-
nario. In particular, nodal demand, marginal costs, and net-
work parameters do not vary over time. The three de-
mand cases, indexed by buses(N 1, . . . , N7), areD L =
(17,10,8,6,13,0,12),D M = (22,14,10,8,18,0,13), and
DH = (26,15,12,9,20,0,14). Thus, the temporal dynamics
observed in the simulations are induced by the repeated
interaction of bidding strategies and by the feedback of the
market-clearing mechanism, rather than by exogenous factors.
To isolate the role of transmission constraints, we consider
two network representations. In theGridcase, the network
constraints (1)–(4) are enforced using the topology and line
limits of the test system. In theNoGridcase, the same
demand and generator data are retained, but line capacities are
set sufficiently high so that the bounds in (1) never become
binding, while the corresponding admittance values are chosen
so that the DC flow relation (4) and phase-angle bounds
(3) do not restrict the optimal dispatch. Operationally, this
produces a copper-plate counterfactual. Mathematically, for all
solved instances, theNoGridcase is equivalent to relaxing
the network-induced restrictions in (1), (3), and (4), so that
problem (7) clears the market as a single unconstrained zone.
The experimental design is a full factorial combination of
three axes: network representationGrid/NoGrid, demand
levelLow/Medium/High, and marginal-cost heterogeneity
Low/Medium/High. This gives2×3×3 = 18market
environments. The selected scenario dimensions correspond
to market characteristics that are widely discussed in the
Tacit Collusion literature as factors influencing the emergence
and sustainability of collusive outcomes, namely network
topology, demand conditions, and cost heterogeneity [1], [22].
All scenarios are trained and screened, while the behavioural
collusion tests are applied only to the most informative cases
selected according to the procedure described next.
B. Scenario Selection Methodology
Instead of running our tests in randomly selected market
instances, we identify instances that are most suspicious for
potential Tacit Collusion emergence. In this subsection, we
describe the methodology that we use to select which market
instances will be tested for the criteria of Section III.
Our starting point is the 18 scenarios of the full factorial
design described in the previous subsection. For each of them,
we compute screening indicators over the final evaluation
window of each training run, after exploratory noise has
TABLE II
SCENARIOS SELECTED FOR BEHAVIOURAL VALIDATION.
Scenario Demand Cost diff. Rationale
Grid–LowDemand–
HighCostDiff
Low High Structured non-stationary
regime with non-trivial de-
viation incentives.
Grid–LowDemand–
MediumCostDiff
Low Medium Reference low-demand
case with a more
stationary learned profile.
Grid–MediumDemand–
HighCostDiff
Medium High Higher-demand case that
remains non-boundary and
strategically informative.
decayed. The competitive benchmark is obtained by solving
the same market-clearing problem (7) under marginal-cost
bidding, i.e. with all generators bidding their true marginal
costs. Denoting the average realised price and total profit by
¯λobs andΠ obs, and their competitive counterparts by ¯λcomp
andΠ comp, we define
M λ = ¯λobs − ¯λcomp ¯λcomp ,(13)
M Π = Πobs −Π comp
max{Πcomp, ϵΠ} ,(14)
whereΠ = P i∈I πi denotes aggregate generator profit andϵ Π
is a small denominator floor used to avoid degenerate ratios
when competitive profits are close to zero.
To separate high-price outcomes from coordinated be-
haviour, the markup indicators are complemented by three
dynamic indicators. First, price variance measures whether the
learned market regime is stable enough for an intervention test
to be meaningful. Second, action correlation and action-change
correlation measure, respectively, whether agents maintain
similar bidding levels or move their bidding strategies together
over time. Third, Best Response Deviation Gain (BRDG)
measures the short-run profitability of unilateral deviations.
For agenti, it is defined as
BRDGi = πi(cBR i ,¯c−i)−π i(¯ci,¯c−i) πi(¯ci,¯c−i) ,(15)
where¯ci denotes the bid prescribed by the learned policy
of agenti,¯c −i denotes the learned bids of all other agents,
andc BR i is the one-shot best response to¯c −i. A positive
BRDG therefore indicates that the learned profile contains an
unrealised short-run deviation incentive.
The selection favours cases that satisfy three practical
requirements: (i) the learned regime is sufficiently stable to be
meaningfully perturbed, (ii) the outcome is not a degenerate
boundary solution in which all agents simply bid at the
action-space limit, and (iii) there is a non-trivial unilateral
deviation incentive that can be tested through the criteria
of Section III. The selected cases are then evaluated using
the Punishment of Deviation Criterion, the Unsustainability
under Shortsight Criterion, and the Short-term Profitability of
Deviations Criterion described in Section III.
C. MARL implementation
The action of agentiat each instancetis to select a bid
vectorc i[t] = (c i,s[t])s∈Si, i.e. one declared marginal cost

6
per segments. This renders the action space of each agent
to be of dimension|S i|. To reduce this dimensionality and
facilitate learning, we parameterize the bid vector through a
supply function. Specifically, each agentimaintains a linear
supply function
f(q i;β i) =α i +β i · qiP
s∈Si Qs
,(16)
which maps an output levelq i,s to a declared marginal
cost (bid)c i,s. Note that this function is generally different
than the agent’s true cost function (defined in the previous
subsection); it is an auxiliary bidding curve used internally
to generate a consistent set of segment bids. The bidc i,s
for segmentsis obtained by evaluatingfat the midpoint
¯qi,s = P s′∈{0,1,...s−1} Qs′ + Qs 2 of the segment’s capacity
range:
ci,s[t] =f i(¯qi,s;β i) =α i +β i · ¯qi,sP
s∈Si Qs
, s∈ S i,(17)
whereα i is set to the agent’s true marginal cost andβ i
is the parameter to be learned by the agent. This defines a
deterministic mappingβ i[t]7→c i[t], so that the full bid vector
is determined by a single scalar parameter. The agent’s internal
action at each instancetis therefore the choice ofβ i[t]∈R ≥0,
which is then translated into the game actionc i[t]via (17).
Remark 1:This parameterization reduces the dimensionality
of an agent’s action space from|S i|to1. This is a choice that
only makes the validation of ourHypothesismore difficult:
by reducing the agents’ degrees of freedom, we reduce the
richness of their policies, possibly excluding instances of
collusive joint policies. Thus, if collusive policies are not
discovered with this model, it does not necessarily mean that
they don’t exist. But if collusive policiesarediscovered with
this model, then the validation of theHypothesisholds also
for the general model where each agent’s action comprises an
arbitrary choice for each segment’s bid.□
In the experiments, the supply function of each generator is
discretised into 12 equal-capacity bid segments. The bidding
parameterβ i is constrained to the interval[0,4000], where the
upper bound corresponds to the maximum admissible value of
the slope parameter. The upper bound is consistent with the
market price cap of 4000 EUR/MWh.
The agents are trained using a multi-agent implementation
of TD3 under the centralized-training/decentralized-execution
paradigm. Each generator is represented by a deterministic
actor that maps its private history to the bidding parameter
used to construct its offer. During training, critics are allowed
to condition on joint market information in order to stabilize
learning in the non-stationary multi-agent environment. During
execution and evaluation, however, only the decentralized
actors are used. The agents therefore do not communicate
when submitting bids.
Each of the 18 scenarios is trained for 100,000 market
instances, organised as 50 episodes of 2,000 instances. The
first 4,000 instances are used as a warm-up phase, during
which agents execute randomly generated actions to populate
the replay buffer. Exploration is introduced through action
noise and is gradually removed over the course of train-
ing, so that the final evaluation window reflects the learned
TABLE III
MAINMARLHYPERPARAMETERS.
Parameter Value
Algorithm Multi-agent TD3
Bid segments 12
Bidding parameter bounds[0,4000]
Training length 100,000 market instances
Episodes / horizon50×2,000
Evaluation window Final 10,000 instances
Warm-up phase 4,000 instances
Discount factor 0.99
Replay buffer size 50,000
Batch size 256
Actor / critic learning rate10 −4 /3·10 −4
Hidden layers[256,256]
Exploration decay 90,000 instances
deterministic policies rather than exploratory behaviour. All
screening indicators reported in the previous subsection are
computed over the final 10,000 market instances. The main
hyperparameters are reported in Table III.
V. RESULTS
A. Screening Outcomes
Among the screening indicators introduced in Section IV,
Fig. 1 reports the price markup across the full set of 18
market environments. Markups are generally modest in the
NoGridcases and do not exhibit a clear ordering across
demand levels or cost heterogeneity. In contrast, theGrid
cases produce substantially higher supra-competitive markups
and display a systematic pattern in which higher demand and
lower marginal-cost heterogeneity are associated with higher
markups. This indicates that transmission constraints mate-
rially amplify market power and make the resulting market
outcomes more sensitive to the underlying demand and cost
structure. At the same time, elevated markups alone cannot
distinguish coordinated behaviour from market power arising
directly from network constraints.
Applying the screening procedure described in Section IV
leaves three non-boundaryGridcases for behavioural
validation:Grid-LowDemand-HighCostDiff,
Grid-LowDemand-MediumCostDiff, andGrid-
MediumDemand-HighCostDiff. These cases all exhibit
supra-competitive outcomes while differing in demand
conditions, cost asymmetry, and learned strategic dynamics.
B. Punishment of Deviations
Figure 2 shows the bidding responses to the forced devi-
ation in the three selected scenarios. InGrid-LowDemand-
HighCostDiff, the deviation ofG 1 triggers a pronounced
response from the remaining agents, which temporarily lower
their bidding slopes and subsequently return towards their
pre-deviation strategies, producing a clear punish-and-forgive
pattern. A similar pattern emerges inGrid-LowDemand-
MediumCostDiff, although the response is asymmetric:G 5
andG 6 react strongly, whileG 2 remains close to its pre-
deviation strategy. A plausible explanation for this difference
is the change in the residual-supply structure induced by the
different relative competitiveness ofG 5 andG 6, rather than

7
Demand
Low
Medium
High
Cost difference
High
Medium
Low
0
20
40
60
80
100
120
0
20
40
60
80
100
120
Markup (%)
(a)
Demand
Low
Medium
High
Cost difference
High
Medium
Low
0
20
40
60
80
100
120
0
20
40
60
80
100
120
Markup (%)
 (b)
Fig. 1. Price markups across the nine demand and marginal-cost heterogeneity combinations: (a)NoGridscenarios without active transmission constraints
and (b)Gridscenarios with active transmission constraints.
980 990 1000 1010 1020 1030 1040 1050 1060
500
1000
1500
2000
2500
3000
3500
4000
(a) Grid-LowDemand-HighCostDiff
Deviating agent: G1
980 990 1000 1010 1020 1030 1040 1050 1060
(b) Grid-LowDemand-MediumCostDiff
Deviating agent: G1
980 990 1000 1010 1020 1030 1040 1050 1060
(c) Grid-MediumDemand-HighCostDiff
Deviating agent: G5
Time step
Agent's action
G1 G2 G5 G6 Deviating agent Deviation window
Fig. 2. Agents’ bidding actions during the Punishment of Deviation test for the three selected scenarios. The shaded region denotes the forced-deviation
window, and the black line identifies the deviating agent.
any change inG 2’s own marginal cost, which is identical in the
two scenarios. UnderHighCostDiff, the very competitive
G6 is strongly constrained by its network position whileG 5
is a relatively costly substitute, increasing the marginal value
ofG 2’s available capacity and making its participation in
the punishment more important. UnderMediumCostDiff,
G5 becomes more competitive andG 6 retains more marginal
supply headroom, so their combined response can substitute
more effectively forG 2, reducing the marginal value of its
participation and creating a natural free-riding incentive. In
Grid-MediumDemand-HighCostDiff, by contrast, the
deviation ofG 5 does not induce a comparable coordinated
reduction in competitors’ bidding slopes, and no clear punish-
and-forgive pattern is observed.
The corresponding reward trajectories in Fig. 3 show
whether these strategic responses impose an economic
penalty on the deviating agent. InGrid-LowDemand-
HighCostDiff, the response of the other agents reduces
the profitability ofG 1’s deviation, with rewards subsequently
recovering as the agents return towards the previous regime.
InGrid-LowDemand-MediumCostDiff, the response of
G5 andG 6 is likewise sufficient to penalize the deviator
despite the weak reaction ofG 2, supporting the interpre-
tation thatG 2 is not pivotal to punishment in this case.
InGrid-MediumDemand-HighCostDiff, the absence of
a comparable strategic response is reflected in the deviator
retaining the benefit of its deviation, providing no evidence
of an effective punishment mechanism. The Punishment of
Deviation criterion is therefore supported in bothLowDemand
scenarios, although with an asymmetric response in the
MediumCostDiffcase, and is not supported inGrid-
MediumDemand-HighCostDiff.

8
980 990 1000 1010 1020 1030 1040 1050 1060
0
10000
20000
30000
40000
50000
60000
70000
80000
(a) Grid-LowDemand-HighCostDiff
Deviating agent: G1
980 990 1000 1010 1020 1030 1040 1050 1060
(b) Grid-LowDemand-MediumCostDiff
Deviating agent: G1
980 990 1000 1010 1020 1030 1040 1050 1060
(c) Grid-MediumDemand-HighCostDiff
Deviating agent: G5
Time step
Reward
G1 G2 G5 G6 Deviating agent Deviation window
Fig. 3. Agents’ rewards during the Punishment of Deviation test for the three selected scenarios. The shaded region denotes the forced-deviation window,
and the black line identifies the deviating agent.
C. Shortsight Ablation
Figure 4 compares the evolution of episode-average bidding
slopes under the baseline MARL configuration and the short-
sight ablation. Contrary to a simple collapse-to-competition
interpretation, removing memory and long-horizon incentives
does not systematically reduce the learned bidding slopes:
the magnitude and direction of the changes vary across
agents and scenarios, while theGrid-MediumDemand-
HighCostDiffcase remains particularly close to the base-
line. A plausible explanation is that a substantial part of
the on-path supra-competitive outcome is supported by static,
network-induced market power. Transmission constraints, lo-
cal scarcity, and generator pivotality remain unchanged after
the ablation, so high bidding slopes may remain profitable even
for nearly myopic agents. The stationarity of demand, costs,
and network parameters further allows the learned policies
to stabilize around similar actions without relying on long
histories of past market outcomes. The ablated runs also
converge more smoothly, consistent with weaker inter-agent
feedback loops. Hence, the similarity of the on-path outcomes
does not imply that the underlying strategic mechanism is
unchanged; the relevant distinction is between the level of
the learned regime and the agents’ ability to condition their
behaviour on deviations from it.
This distinction becomes apparent when the forced-
deviation experiment is repeated under the shortsight ablation,
as shown in Fig. 5. In bothLowDemandscenarios, the
pronounced punishment-and-forgiveness responses observed
under the baseline disappear, with competitors’ bidding slopes
remaining largely unchanged following the forced deviation.
Removing history eliminates the informational basis for con-
ditioning current actions on a previous deviation, while the
near-myopic discount factor removes much of the incentive
to incur a short-run punishment cost in order to restore a
more profitable future regime. InGrid-MediumDemand-
HighCostDiff, where no clear punishment response was
present under the baseline, the ablation likewise produces
no evidence of an enforcement mechanism. The shortsight
ablation therefore affects primarily the off-path enforcement
mechanism rather than necessarily the on-path level of bids.
It consequently provides supporting evidence for a repeated-
game component in the twoLowDemandscenarios through
the disappearance of punishment, while the persistence of
similar on-path bidding levels indicates that their supra-
competitive outcomes are also partly supported by static
market power; no comparable evidence is obtained forGrid-
MediumDemand-HighCostDiff.
D. Iterative Best Responses
Figure 6 shows the reward trajectories obtained when
the learned MARL outcomes are used as the starting
point for Iterative Best Response. InGrid-LowDemand-
HighCostDiff, unilateral best responses provide short-run
profit opportunities, but the subsequent IBR dynamics move
the agents towards reward levels that are generally below
those sustained under MARL. The pattern is even clearer in
Grid-LowDemand-MediumCostDiff, where the initially
profitable deviations are followed by lower reward levels
for all agents relative to their MARL benchmarks. These
two cases are therefore consistent with a regime in which
unilateral deviation is attractive in the short run, while the
competitive adaptation induced by continued best responses is
less profitable. InGrid-MediumDemand-HighCostDiff,
by contrast, the IBR trajectories do not exhibit the same
combination of profitable short-run deviations and a system-
atically less profitable subsequent regime. The Short-term
Profitability of Deviations criterion is therefore supported in
the twoLowDemandscenarios and not supported inGrid-
MediumDemand-HighCostDiff.

9
0 10 20 30 40 50
Episode
1000
1500
2000
2500
3000
3500
4000Slope (Action)
Grid-LowDemand-HighCostDiff
0 10 20 30 40 50
Episode
Grid-LowDemand-MediumCostDiff
0 10 20 30 40 50
Episode
Grid-MediumDemand-HighCostDiff
Agents
G1 (normal) G1 (no-mem) G2 (normal) G2 (no-mem) G5 (normal) G5 (no-mem) G6 (normal) G6 (no-mem)
Fig. 4. Evolution of episode-average bidding slopes under the baseline MARL configuration and the shortsight ablation for the three selected scenarios. Solid
lines denote the baseline agents and dashed lines the ablated agents.
980 990 1000 1010 1020 1030 1040 1050 1060
1000
1500
2000
2500
3000
3500
4000
(a) Grid-LowDemand-HighCostDiff
Deviating agent: G1
980 990 1000 1010 1020 1030 1040 1050 1060
(b) Grid-LowDemand-MediumCostDiff
Deviating agent: G1
980 990 1000 1010 1020 1030 1040 1050 1060
(c) Grid-MediumDemand-HighCostDiff
Deviating agent: G5
Time step
Agent's action
G1 G2 G5 G6 Deviating agent Deviation window
Fig. 5. Agents’ bidding actions during the Punishment of Deviation test under the shortsight ablation for the three selected scenarios. The shaded region
denotes the forced-deviation window, and the black line identifies the deviating agent.
TABLE IV
SUMMARY OF BEHAVIOURAL EVIDENCE FORTACITCOLLUSION.
Scenario Punish. Shortsight IBR Interpretation
Grid–LowDemand–
HighCostDiff
Supportive Supportive Supportive Collusion-consistent
Grid–LowDemand–
MediumCostDiff
Supportive Supportive Supportive Collusion-consistent
Grid–
MediumDemand–
HighCostDiff
Not supp. Not supp. Not supp. Structural market
power
E. Synthesis of Behavioural Evidence
Table IV summarizes the evidence obtained from the three
behavioural criteria. Taken together, the three behavioural
tests provide mutually consistent evidence that the two
LowDemandlearned regimes contain a repeated-game com-
ponent consistent with Tacit Collusion. The persistence of
supra-competitive on-path bidding after the shortsight ab-
lation nevertheless indicates that these outcomes are not
driven by repeated-game incentives alone, but are also sup-
ported by structural, network-induced market power.Grid-
MediumDemand-HighCostDiffprovides the contrasting
case: despite exhibiting a supra-competitive market outcome, it
shows neither a punishment response, an ablation-sensitive en-
forcement mechanism, nor an IBR pattern consistent with the
collusion criteria. Its elevated markup is therefore more plau-
sibly attributed to structural market power than to Tacit Collu-
sion. Overall, the results show that similar supra-competitive
outcomes can arise from qualitatively different strategic mech-
anisms, which cannot be distinguished from price levels alone.
VI. CONCLUSIONS
This paper investigated whether Tacit Collusion can emerge
in electricity markets whose participants delegate their bidding
strategies to autonomous, learning-based algorithms. Strategic
bidding was modeled as a repeated game with imperfect public
monitoring, with agents’ learning-based policies modeled via
multi-agent reinforcement learning. Different cases of market
characteristics were filtered based on susceptibility for Tacit
Collusion and the most suspicious ones were tested against
three Tacit Collusion criteria. Our experimental results show

10
0 50 100 150 200 250 300
IBR iteration (0 = MARL endpoint)
10000
15000
20000
25000
30000Reward
Grid-LowDemand-HighCostDiff
0 50 100 150 200 250 300
IBR iteration (0 = MARL endpoint)
10000
15000
20000
25000
30000
Grid-LowDemand-MediumCostDiff
0 50 100 150 200 250 300
IBR iteration (0 = MARL endpoint)
10000
20000
30000
40000
50000
60000
70000
80000
Grid-MediumDemand-HighCostDiff
Agents
G1 G2 G5 G6
Fig. 6. Agent reward trajectories under Iterative Best Response (IBR), initialized from the learned MARL outcomes. Iteration 0 corresponds to the MARL
endpoint, while the horizontal dashed lines indicate the corresponding MARL reward levels.
that the danger of Tacit Collusion in electricity markets is
realistic: particularly under binding network constraints, agents
learn to sustain supra-competitive outcomes that satisfy several
independent indicators of Tacit Collusion, despite never being
instructed or designed to collude. Our results should not be
taken as conclusive but rather as an alarm bell that encourages
extensive research on this topic. Specifically, investigating
the learning mechanics that make Tacit Collusion emergent
and investigating market-design countermeasures constitute
important future work directions.
REFERENCES
[1] M. Ivaldi, B. Jullien, P. Rey, P. Seabright, and J. Tirole,The Economics
of Tacit Collusion: Implications for Merger Control. Elsevier, 2007, p.
217–239. [Online]. Available: http://dx.doi.org/10.1016/S0573-8555(06)
82008-0
[2] E. Calvano, G. Calzolari, V . Denicol `o, and S. Pastorello, “Artificial
intelligence, algorithmic pricing, and collusion,”American Economic
Review, vol. 110, no. 10, p. 3267–3297, Oct. 2020. [Online]. Available:
http://dx.doi.org/10.1257/aer.20190623
[3] Y . Liang, C. Guo, Z. Ding, and H. Hua, “Agent-based modeling in
electricity market using deep deterministic policy gradient algorithm,”
IEEE transactions on power systems, vol. 35, no. 6, pp. 4180–4192,
2020.
[4] E. G. Kardakos, C. K. Simoglou, and A. G. Bakirtzis, “Optimal bidding
strategy in transmission-constrained electricity markets,”Electric Power
Systems Research, vol. 109, pp. 141–149, 2014.
[5] X. Hu and D. Ralph, “Using epecs to model bilevel games in restructured
electricity markets with locational prices,”Operations research, vol. 55,
no. 5, pp. 809–827, 2007.
[6] S. A. Gabriel, A. J. Conejo, J. D. Fuller, and B. F. Hobbs,Complemen-
tarity modeling in energy markets. Springer New York, NY , 2013.
[7] G. Tsaousoglou, J. S. Giraldo, and N. G. Paterakis, “Market mechanisms
for local electricity markets: A review of models, solution concepts and
algorithmic techniques,”Renewable and Sustainable Energy Reviews,
vol. 156, p. 111890, 2022.
[8] Q. Tang, H. Guo, K. Zheng, and Q. Chen, “Forecasting individual bids in
real electricity markets through machine learning framework,”Applied
Energy, vol. 363, p. 123053, 2024.
[9] S. Baltaoglu, L. Tong, and Q. Zhao, “Algorithmic bidding for virtual
trading in electricity markets,”IEEE Transactions on Power Systems,
vol. 34, no. 1, pp. 535–543, 2018.
[10] N. Eschenbaum, “Shared bidding algorithms and competition: Evidence
from electricity markets,” 2026. [Online]. Available: https://arxiv.org/
abs/2607.13002
[11] Y . Ye, D. Qiu, M. Sun, D. Papadaskalopoulos, and G. Strbac, “Deep
reinforcement learning for strategic bidding in electricity markets,”IEEE
Transactions on Smart Grid, vol. 11, no. 2, pp. 1343–1355, 2019.
[12] Z. Zhu, Z. Hu, K. W. Chan, S. Bu, B. Zhou, and S. Xia, “Reinforcement
learning in deregulated energy market: A comprehensive review,”
Applied Energy, vol. 329, p. 120212, 2023. [Online]. Available:
https://doi.org/10.1016/j.apenergy.2022.120212
[13] F. Hu, Y . Zhao, Y . Yu, C. Zhang, Y . Lian, C. Huang, and
Y . Li, “Strategic bidding with price-quantity pairs based on
deep reinforcement learning considering competitors’ behaviors,”
Applied Energy, vol. 391, p. 125874, 2025. [Online]. Available:
https://doi.org/10.1016/j.apenergy.2025.125874
[14] H. Zhang, G. Tsaousoglou, S. Zhan, K. Kok, and N. G. Paterakis,
“Taming deep reinforcement learning agents with pricing mechanism:
Validation in power distribution systems,”Energy and AI, p. 100635,
2025.
[15] N. Harder, R. Qussous, and A. Weidlich, “Fit for purpose: Modeling
wholesale electricity markets realistically with multi-agent deep
reinforcement learning,”Energy and AI, vol. 14, p. 100295, 2023.
[Online]. Available: https://doi.org/10.1016/j.egyai.2023.100295
[16] Y . Du, F. Li, H. Zandi, and Y . Xue, “Approximating nash
equilibrium in day-ahead electricity market bidding with multi-agent
deep reinforcement learning,”Journal of Modern Power Systems and
Clean Energy, vol. 9, no. 3, pp. 534–544, 2021. [Online]. Available:
https://doi.org/10.35833/MPCE.2020.000502
[17] Z. Pan and Z. Jing, “Decision-making and cost models of generation
company agents for supporting future electricity market mechanism
design based on agent-based simulation,”Applied Energy, vol. 391, p.
125881, 2025. [Online]. Available: https://doi.org/10.1016/j.apenergy.
2025.125881
[18] T. Klein, “Autonomous algorithmic collusion: Q-learning under
sequential pricing,”The RAND Journal of Economics, vol. 52, no. 3,
p. 538–558, Aug. 2021. [Online]. Available: http://dx.doi.org/10.1111/
1756-2171.12383
[19] T. Werner, “Algorithmic and human collusion,”SSRN Electronic Journal,
2021. [Online]. Available: http://dx.doi.org/10.2139/ssrn.3960738
[20] D. Esmaeili Aliabadi and K. Chan, “The emerging threat of artificial
intelligence on competition in liberalized electricity markets: A deep
q-network approach,”Applied Energy, vol. 325, p. 119813, 2022.
[Online]. Available: https://doi.org/10.1016/j.apenergy.2022.119813
[21] M. S. `Avila, R. Ebrahimy, and G. Tsaousoglou, “How inefficient can
an electricity market be?” in2025 IEEE Kiel PowerTech. IEEE, 2025,
pp. 1–6.
[22] J. Mikl ´os-Thal, “Optimal collusion under cost asymmetry,”Economic
Theory, vol. 46, no. 1, pp. 99–125, 2011. [Online]. Available:
http://www.jstor.org/stable/41485808
