---
title: Multiagent Reinforcement Learning for Liquidity Games
url: https://arxiv.org/abs/2601.00324
category: ai-marketing
subcategory: empirical
date: 2026-01
venue: ''
authors:
- Alicia Vidler
- Gal A. Kaminka
source: arxiv
pdf_url: https://arxiv.org/pdf/2601.00324
pages: 9
chars: 40901
fetched_at: '2026-11-08T13:18:28+00:00'
kb_version: 1
---

# Multiagent Reinforcement Learning for Liquidity Games

Multiagent Reinforcement Learning for Liquidity Games
Alicia Vidler1, Gal A. Kaminka1
1Bar-Ilan University
aliciavidler@gmail.com, galk@cs.biu.ac.il
Abstract
Making use of swarm methods in financial market modeling
of liquidity, and techniques from financial analysis in swarm
analysis, holds the potential to advance both research areas.
In swarm research, the use of game theory methods holds the
promise of explaining observed phenomena of collective util-
ity adherence with rational self-interested swarm participants.
In financial markets, a better understanding of how indepen-
dent financial agents may self-organize for the betterment and
stability of the marketplace would be a boon for market de-
sign researchers. This paper unifies Liquidity Games, where
trader payoffs depend on aggregate liquidity within a trade,
with Rational Swarms, where decentralized agents use differ-
ence rewards to align self-interested learning with global ob-
jectives. We offer a theoretical frameworks where we define a
swarm of traders whose collective objective is market liquid-
ity provision while maintaining agent independence. Using
difference rewards within a Markov team games framework,
we show that individual liquidity-maximizing behaviors con-
tribute to overall market liquidity without requiring coordi-
nation or collusion. This Financial Swarm model provides a
framework for modeling rational, independent agents where
they achieve both individual profitability and collective mar-
ket efficiency in bilateral asset markets.
Introduction
Cleared trading volume, and the system’s ability to achieve
it efficiently, is commonly referred to asliquidity. In
modern markets, it is anemergentanddesiredproperty
of decentralized interactions among heterogeneous agents,
not a fixed attribute. It denotes the ease of trading an asset
quickly and at low cost without materially moving its price
(Frank J. Fabozzi 2005). To quote Kevin Warsh, a member
of the U.S. Federal Reserve Board of Governors: “Liquidity
is confidence”.
Increasing market liquidity is a challenging problem.
Market clearing—turning intent into executed trades—
comes from myriad local choices (quotes, inventories, risk
limits) that produce system-level effects (such as aggregate
trading volumes). However, since agent coalition and coor-
dination are typically illegal in real-world modern financial
markets, these local choices arerequiredto be uncoordi-
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
nated. The trading intents (and their execution) of indepen-
dent learners (agents) must be based on their strictlylocal
rewards, that have no clear link to market-wide objectives.
In this paper, we address the tension between theself-
interesteddecisions of the independent agents, and the
desiredmaximal liquidityof market-wide trading vol-
umes. Specifically, we unifyLiquidity Games (LG), a
game-theoretic model of liquidity formation (Vidler and
Walsh 2024b), with a decentralized multiagent reinforce-
ment learning method,rational swarms(Kaminka 2025).
Here, multiple financial agents (investors, banks, or market
makers) act on local information. Their collective decisions
determine system-level liquidity patterns. The decentralized
learning framework allows independent learners to act in a
way that increases liquidity, while remaining independently
self-interested.
Concretely, we cast the market system as a Markov team-
game, i.e., a fully cooperative stochastic repeated game,
where agents theoretically receive the same global (system-
level) payoff resulting from their joint actions. we treatag-
gregate cleared volumeas a global measure of liquidity. This
is a system-level performance measure of the quantity of or-
ders that are actuallyexecuted(i.e., matched and settled)
within a period, as distinct from quoted or submitted vol-
ume (Bank of England 2015). Aggregated cleared volume is
the desired property to be maximized. Following (Kaminka
2025), we address the challenge resulting from the fact that
agents are unable to receive (observe) this joint payoff, but
are only exposed to a local proxy of it. Instead, each agent
learns using a local difference reward (marginal contribu-
tion to liquidity), yielding an individual reward signal that is
aligned with global liquidity. This allows fully independent
learning with no orchestration or collusion. We examine two
hypotheses:
[H1]: Liquidity with difference rewards.In bilateral
trading with random pairing, agents trained withdiffer-
ence rewardswill achieve higheraggregate liquidityand
individual trading quantitiesthan those using other local
or global signals, or baselines without learning, thereby
maximizing local utility and global utility without
coordination.
[H2]: Robustness under exact match.Inexact-match
Liquidity Games (no partial fills), agents trained with
difference rewardswill learn policies that achieve and
arXiv:2601.00324v1  [cs.AI]  1 Jan 2026

maintain highermatching efficiencyand will reach a high
trade success threshold earlier in training than agents
using alternative reward designs.
We examine these hypotheses across differentclearing
regimes, which define how trade offers convert to exe-
cuted transactions and thereby shape the global objective
G(cleared volume and hence, liqudity). We explore two
regimes: (i)partial fill, allowing fractional execution (which
we termMinFillregime) and (ii)exact match, requiring
full quantity alignment between buyers and sellers follow-
ing (Vidler and Walsh 2024b).
We show using difference rewards provides advantages
over alternative learning and non-learning methods. Antic-
ipating our results, under a partial clearing rule (MinFill),
difference reward agents achieve the highest total liquidity
and clearing efficiency; under exact matching, they remain
competitive, rapidly reaching∼70%trade success despite
stricter constraints.
This paper is structured as follows. First, we explore the
relevant literature. Then, we detail the methodology and
framework to combine difference reward functions of dis-
tributed multiagent reinforcement learning and the game
theoretic model of bond markets focused on liquidity. In the
following sections, we outline specific instances of the com-
bined paradigm and discuss the results.
Financial Markets as Multiagent Systems:
A Literature Review
Traditional economic theory has employed several mathe-
matical frameworks to model agent interactions in financial
markets, each offering distinct perspectives on collective be-
havior and market dynamics. Financial markets can be mod-
eled as multiagent environments (MAS) where heteroge-
neous participants, ranging from retail traders to institutional
algorithms, interact under shared protocols and constraints
(Vidler and Walsh 2024a; Epstein and Axtell 1996; Epstein
and Schneider 2010; Hull 2022). The degree of agent hetero-
geneity varies between market segments, shaping systemic
behavior and stability (Vidler and Walsh 2024a).
We suggest that there are theoretical and structural analo-
gies between agents in financial markets (Vidler 2025), and
multiagent reinforcement learning by independent learners
in swarms (Kaminka 2025). These can provide a foundation
for understanding distributed decision-making in economic
contexts.
Regulated Interaction and Implicit Coordination.Un-
like engineered MAS, financial systems restrict explicit co-
operation due to legal prohibitions on collusion and infor-
mation sharing (Federal Reserve Bank of New York 2021;
Bank of England 2015). Despite this, coordination can still
emerge implicitly through indirect channels such as strategic
signaling, herding, and reaction to shared market data, re-
sembling the stigmergic interactions observed in swarm sys-
tems. These markets thus function as decentralized, swarm-
like systems, where coordination arises without central con-
trol. This analogy motivates our view of financial markets as
distributed systems that process information and adapt dy-
namically, which we expand on below.
Distributed Information Processing.Financial markets
aggregate private information through the distributed trading
mechanism, where individual beliefs are expressed through
price signals (equity markets) and available liquidity (bond
markets). This resembles distributed sensing in swarms. In
some markets, such as government bonds, this process af-
fects liquidity (Pinter 2023; Pinter, Wang, and Zou 2024;
Vidler 2025). System-level feedback highlights the tension
in the system: Markets (systems) can adapt through feed-
back, but this adaptive capacity works best in smooth, un-
obstructed environments. When faced with significant chal-
lenges or resistance, the system’s ability to maintain stable
operation while adapting becomes limited. In bond markets,
this has translated into several systemic shocks in the past
few years in the UK and US markets alone ((Pinter 2023),
(Duffie 2020)). Our work, in part, is motivated by these chal-
lenges and the opportunity to link markets when global goals
are crucial (i.e. functioning bond markets) but where indi-
vidual agents are both selfish and unable to explicitly coor-
dinate to maximize global outcomes. We introduce literature
specifically relevant to bond market liquidity below.
Market Liquidity: Bilateral Market Structure and
Liquidity Provision in Government Bond Markets
Liquidity in bilateral, over-the-counter (OTC) markets
emerges from decentralized interactions between counter-
parties rather than from centralized order books. Many insti-
tutional settings, including government bonds, concentrate
asset trading. For example, in the UK market for govern-
ment bonds (the gilt market), bonds are issued and traded
via a network of regulated dealers (GEMMs)1, with broadly
comparable arrangements in Australia, the US, and Canada
(Cheshire 2015). While institutional details vary, large in-
vestors in such markets typically transact through these in-
termediaries (or their functional equivalents). Large partic-
ipants supply quotes and warehouse risk but face balance-
sheet, capital, and regulatory constraints (Pinter, Wang, and
Zou 2024; Czech and Pinter 2022).
Across bilateral OTC environments, transaction prices
are often anchored to public benchmarks or reference rates
rather than discovered solely within each local match. Liq-
uidity constraints arise from limits on inventories, funding
capacity, and the topology of trading relationships (Duffie
and Singleton 2015; Frank J. Fabozzi 2005; Pinter 2023).
As a result, liquidity is an emergent property of many de-
centralized decisions (such as inventory management and
risk tolerance) rather than a centrally controlled input (Frank
J. Fabozzi 2005). Supervisors and monitoring authorities
(Bank of England 2015) observe cleared volume: the amount
of bonds which convert into executed trades, a metric that is
used to assesmarket liquidity. In this paper we will refer
to market liquidity and liquidity, interchangeably.
Gaps remain in how liquidity can be modeled as a global
outcome emerging from local agent behavior. Existing ap-
proaches capture either structural features of market mi-
crostructure or the strategic interactions of participants. We
1https://www.dmo.gov.uk/responsibilities/gilt-market/market-
participants/

address this by contributing a model that integrates the Liq-
uidity Game (which formalizes the constraints and incen-
tives of bilateral OTC trading (Vidler and Walsh 2024b))
with decentralized multiagent learning via rational swarms
(Kaminka 2025). This unified framework allows agents to
act independently using local rewards, yet collectively re-
produce system-level liquidity through emergent clearing
(trading of bonds). We add to this further by allowing agents
to ”learn” how to trade larger volumes, which increased ag-
gregate system liquidity. It thereby connects micro-level de-
cision processes with macro-level market outcomes, provid-
ing a new method for studying liquidity formation without
centralized coordination and agent policy learning.
Game Theory applied to Financial Multiagent
Systems
Game Theory.Game-theoretic approaches have been ap-
plied to financial markets, but most frameworks analyze
micro-level interactionsrather than holistic market behav-
ior, limiting insight into the emergent properties of large-
scale systems of independent trading agents, such as liquid-
ity analysis. The central challenge is scaling game-theoretic
insights to capture the complex interdependencies in multi
participant markets.
Against this backdrop, applications of heterogeneous and
homogeneous multiagent systems span small and largescale
settings, notably in game theory, negotiation, and fair-
ness (Wooldridge 2009; Axtell and Farmer 2022; Parkes
2006; Shoham and Leyton-Brown 2008; Fatima, Kraus,
and Wooldridge 2014), with related lines in (Fagiolo et al.
2017; Lussange et al. 2020; Vermeir and Bersini 2015).
The foundations for agent reasoning and communication
provide logic-based frameworks for cooperation (Fatima,
Kraus, and Wooldridge 2014; Kl ¨ugl, Fehler, and Herrler
2005; Thangarajah, Padgham, and Harland 2002). Exten-
sions to automated negotiation and decision making under
uncertainty blend game theory and AI (Baumeister 2019),
with results on repeated interaction and “playing the wrong
game” bounds (Burkov and Chaib-Draa 2014; Meir and
Parkes 2018). Research on goal modeling within ABMs in-
cludes (Winikoff et al. 2002) and simulations are found to
be crucial for reproducing complex dynamics (Bai, Raskob,
and M ¨uller 2020). These ideas underpin autonomous bid-
ding agents (including financial agents) and market-oriented
MAS explored in (Wellman, Greenwald, and Stone 2007;
Lin et al. 2014; Shoham 2008). We make use of these ele-
ments and extend LG to include multiagent learning abil-
ities, with the goal that market participant (agents) learn
the best strategy for trading to mazimize their own liquidity
(selfishly) while benefiting overall from global maximized
market liquidity.
Markov Games and Market Memory.Markov deci-
sion processes and stochastic (Markov) games have found
widespread application in financial modeling due to their
mathematical tractability and the assumption of memory-
less state transitions (Shapley 1953; Littman 1994). The
Markov property assumes that future market states depend
only on current conditions, independent of historical tra-
jectories. However, this assumption has faced increasing
scrutiny, as empirical evidence points to long-memory and
path-dependent behavior in returns, volatility, and liquid-
ity (order flow) (Ding, Granger, and Engle 1993; Lillo and
Farmer 2004, 2005). In particular, volatility dynamics ex-
hibits rough (fractional) behavior that departs from Marko-
vian models (Gatheral, Jaisson, and Rosenbaum 2018). Sim-
ilarly, trading systems comprise repeated games, where par-
ticipants see value in learning features of the counterparties
they trade with (Massa and Simonov 2003).
Across these approaches,a gap remains: existing
models do not reconcile local agent incentives (with or with-
out learning) and the emergence of global liquidity as an
outcome.
We address this gap by contributing a unified framework
that combines the structural rigor of the Liquidity Game (Vi-
dler and Walsh 2024b) with decentralized learning via ra-
tional swarms (Kaminka 2025). We show agents can learn
locally, while preserving legal non-coordination, yielding a
scalable, adaptive model of how liquidity emerges endoge-
nously in complex financial systems.
Swarm Characteristics of Financial Markets
Reward mechanisms and swarms
Reward mechanisms in multiagent financial systems
span individual incentives and system level objectives
(Wooldridge and Jennings 1995; Shoham 2008). At the
agent level, rewards naturally map to monetary gains from
trading. At the collective level, rewards correspond to at-
tributes of market qualities such as stability, liquidity, and
sustained participation. In certain markets (such as bond
markets), agents derive direct benefit from liquidity (facil-
ity to transact the bonds they wish, at the time they desire)
rather than from directional price dynamics.
This paper seeks to unify two aspects of financial and
swarm research: we build a unified framework for swarm-
scale market liquidity that marries LG’s (payoffs tied to ag-
gregate liquidity (Vidler and Walsh 2024b))
with Rational Swarms (self-interested agents aligned via
difference rewards (Kaminka 2025; Tumer and Agogino
2007)) inside a Markov team-game formalism. We make ex-
plicit that the difference reward is the marginal contribution
of the agent to a global liquidity objective, providing a trans-
parent, incentive compatible signal that preserves the inde-
pendence of the agent and avoids coordination or collusion.
This shifts the focus from two-party transactions to emer-
gent, large population dynamics, linking individual trading
incentives to system-level properties such as overall market
liquidity.
Model and Method Description
In this section we detail our theoretical model definition.
The following subsections specify the environment (random
pairing, clearing rules), agent types, and learning signals. All
are defined relative to a bilateral trading market in which the
team objective isaggregate liquidityG(total cleared vol-
ume).

Liquidity Games
Liquidity Games are introduced in (Vidler and Walsh 2024b)
and are defined as a “noncooperative, simultaneous move
game between two agents (or players), modeling a bilateral
market mechanism”. Specific to the game is the unique fea-
ture of endogenous payoff.
Definition 1(Liquidity Game).A game instance is a tuple
I= (N, B, U)defined as follows:
•Players.N={i, j}is the set of players, with|N|= 2.
•Bond balances.Each playeri∈Nholds a private bond
balance
Bi ∈Zwithx≤B i ≤y ,
wherex, y∈Zare public market parameters. Typically
x= 0andy=c, wherecis the total issuance of the
given bond (publicly available).
•Actions.The set of permitted actions for playeriis
Ai ={0,1, . . . ,|Bi|},
and an actiona i ∈A i represents the number of bonds
played by playeriin a round. Equivalently,
0≤a i ≤ |Bi|.
•Utilities.The utility (reward) functionu i :A i →Zfor
playeriis
ui(ai;B i) =|a i|for alla i ∈A i.
Game motivation: Repeated stage game
We model the process as a repeated (one-shot) stage game,
where each episode the game state resets and multiple bilat-
eral agent games occur each episode such that each agent has
the opportunity to trade one time only per episode. Within
the stage game between two agents, simultaneously with-
out the use of prices, each player adopts a (potentially) het-
erogeneous strategy by privately selecting a parcela i ∈B i
with0≤ |a i| ≤ |Bi|to trade, aiming to move their bond
balance toward, but not below, zero while concealing true
inventory to preserve informational advantages and satisfy
regulatory norms. Choices may be formed on beliefs about
the counterparty and agents reflect human players who typi-
cally seek full clearance in a single move. Two game regimes
are utilised: trades execute only if the submitted quantities
are mutually acceptable and the “Minfill” regime where the
minumum is traded. Whilst outside the scope of this work,
we note that these player preferences can be incorporated
in more complex and richer game settings (such as penalty
methods) and we leave this to future work.
In the classic game of (Vidler and Walsh 2024b) payoff
and welfare for a one-shot, simultaneous variant has one
player, a seller withB i >0and a buyer withB j <0each
choosing a non-negative actiona k ∈Z ≥0 witha k ≤ |Bk|.
Trade clears only on an exact positive match:q=a i if
ai =a j >0, elseq= 0. The payoff for each player is
q. This captures the shared goal of moving balances toward
zero; any mismatch (or a zero submission) leaves positions
unchanged.
Agents can belong to one of two mutually exclusive
groups i.e. large or small firm size.
Let there be a finite set of agentsN={1, . . . , n}. Each
agenti∈Nbelongs to one of two mutually exclusive types:
θi ∈Θ ={large,small}.
The typeθ i represents the firm size of agenti. The size of
the firm affects the mean of the bond pay-off distribution in
any trade, but not its tail behaviour.
We extend LG’s in two ways to increase the richness of
their applicability:
Clearing Rules:A trade is said to have occurred at the
lower of|a i|and|a j|such that the minimum liquidity would
be transacted between parties. We call this the ”MinFill”
variant. This then naturally extends the concept of the differ-
ence reward to be the value differential between what each
agent had wished to trade, and what was traded. Formally
We see that in Definition 1 there is the possibility for at
least two policies to exist in the market:
1.LG-Exact (baseline).Trade occurs iffa i =a j >0. The
quantity traded isq=a i, andu i(q) =q.
2.LG-MinFill (extension).Trade occurs whenevera i >0
anda j >0, with traded quantityq= min(a i, aj). The
payoff isu i(q) =q.
Unless stated otherwise, the equilibrium statements for
the baseline refer to LG-Exact, and the learning experi-
ments marked “MinFill” implement the second rule. We
note that in LG-Exact, every diagonal profile(a, a)with
a∈ {1, . . . ,min(|Bi|,|B j|)}is a pure Nash equilibrium
(and(0,0)is also an equilibrium). In LG-MinFill, the unique
pure Nash equilibrium isa ⋆ i =a ⋆ j = min(|Bi|,|B j|).
In extending LG’s to two regimes we generalize beyond
strict constraints.
Learning Agents
We extend the game to a repeated stage game, where initial
agent balances are reset each episode, but agents can learn
what is the optimal amount of bonds to try to trade. Namely,
agents seek to learn the amount of bond to offer that maxi-
mizes the trade amount. The learning needs to take as con-
text the probability what sort of agent is on the other side of
the trade (which impacts the possible trade quantity), whilst
seeking to maximize the total liquidity generated in a trade.
We adoptdifference rewardof (Tumer and Agogino 2007)
as each agent’s reward signal. We build extensively on work
by (Kaminka 2025) which demonstrates the power of ratio-
nal decentralized swarm agents to provide for environment
level benefits. For agentiwith joint outcomezand coun-
terfactualz −i (the system withouti), the difference reward
measuresthe agent’s marginal contributionto the global ob-
jectiveGand is defined as:
Di ≡G(z)−G(z −i)(1)
In our setting,Gis a liquidity metric, soD i quantifies
how much agentiimproves market liquidity while preserv-
ing agent independence and avoiding explicit coordination.
The difference reward measures the marginal contribution

of an agent’s presence to the overall system performance.
Such marginal contribution can be quantified through met-
rics such as total trading volume for example. In this way,
applying difference rewards to bilateral trading environ-
ments (such as bonds as one example (Vidler and Walsh
2024b) would allow a framework to evaluate the nonlinear
impact of agent inclusion versus exclusion, extending be-
yond simple proportional contributions to capture emergent
effects arising from agent interactions. We propose making
use of this approach to understand market liquidity.
This pairing of Liquidity Games (endogenousG) with Ra-
tional Swarms (difference rewards) aligns rational learning
individually with the market-level goal while avoiding ex-
plicit coordination. We note that this “marginal contribu-
tion” view is conceptually analogous to familiar ideas of
risk attribution (e.g., marginal or incremental contributions
to portfolio risk) (Hull 2018).
Experiments with a Unified Financial Swarms
model
In this section we detail our programmatic model testing en-
vironment. The code base implements a multiagent simu-
lation environment to investigate coordination and liquidity
provision in a simplified market setting. We use the simula-
tion environment to explore the impact of different clearing
rules and reward mechanisms on agent behavior and aggre-
gate market outcomes.
Simulation environment
The core of the simulation is theLiquidityGameEnv
class, which models a market with a fixed number of agents
(n agents). In each episode (time step), the agents are
randomly paired. Within each pair, agents simultaneously
announce an amount of liquidity they are willing to offer
for trade to their compatriot. Such details are never broad-
cast to other agents. The actual amount traded depends on
the chosen clearing rule. After trades occur, agents’ bal-
ances are updated, and a new episode begins with agents
having potentially altered balances. Agents are designated
assmallorlargebased on their initial balance ranges
(max balance smallandmax balance large), al-
lowing for the study of asymmetric liquidity endowments.
See Figure 1 for a schematic representation of the interac-
tion model.
Simulation settings.We make use of estimated agent
numbers within real life markets in (Pinter 2023) and set
agents to 1300, with large and small participants set at 33%
and 66% respectively (drawing approximate values from
(Vidler and Walsh 2024b). The analysis is run on 10,000
episodes. The initial balance caps for each agent in each
episode are set to small≤10units; large≤40units, where
the agents initialize a balance as a random value between 1
and the cap at each episode, inline with the probability of be-
ing part of a large or small agent cohort. Our goal remains to
test the ability for agents learning what amount of bonds to
offer to trade such that they maximize their traded quantities
and liquidity of the environment as a whole.
Agenti
Observe
Local State
Choose
Trade Action
Receive
Difference Reward
Observe
Local State
Agentj
Observe
Local State
Choose
Trade Action
Receive
Difference Reward
Observe
Local State
Market Liquidity
(Sum of successful trades)
Decentralized
Environment
Bilateral Trade
Figure 1: Schematic of the Liquidity Swarm model. Agents
iandjinteract via bilateral trades. Actions affect global liq-
uidity, which feeds into local reward signals via difference
rewards.
Learning Agents (Tabular Q-Learning)
We make use of simple Q learning agents. However, the sim-
ulation compares the performance of learning agents em-
ploying different reward mechanisms against non-learning
baseline agents. All learning agents share the same tabular
Q-learning core and differ only in thereward signal(differ-
ence, local, or global).
Q-table.Statesis the agent’s current balance; the action
set isA(s) ={1, . . . , s}(offered amount). The Q-table has
one row per discrete balance and one column per feasible
action.
Update.After takingainsand observing rewardrand
next states ′,
Q(s, a)←Q(s, a) +α
h
r+γmax
a′
Q(s′, a′)−Q(s, a) i ,
with fixedα= 0.1. The reward termris instantiated by the
chosen signal; no other hyperparameters differ across sig-
nals.
Action selection (epsilon-greedy).With probabilityϵ=
0.2the agent explores by sampling uniformly fromA(s);

otherwise it exploits, choosing anya∈arg max a′ Q(s, a′)
(ties broken uniformly at random).
The learning agents are differentiated by thereward
modeused to compute the signal they receive after each
step.
1.Diff Reward:Agents receive a difference reward, ap-
proximating their marginal contribution to the liquidity
in the system. The reward for an agent is the quantity
traded in their pair minus the quantity that would have
been traded if they had offered zero (while their partner’s
offer remained the same). Under theMinFillrule, this
simplifies to the trade quantityq.
2.Local Reward:Agents receive a reward based on a local
utility function:R i = 2q−a i −π ij, whereqis the trade
quantity,a i is the agent’s offer, andπ ij is a penalty for
repeating a partner from the previous step, designed to
explore adverse selection and set to a modest penalty of
0.1 units.
3.Global Reward:Agents receive the total liquidity
cleared across all pairs in the market during that step.
This requires agents to learn to contribute to the global
outcome without direct individual feedback on their im-
pact.
Baseline AgentsTwo non-learning baseline strategies are
implemented for comparison:
1.randomAgent:In each step, random agents offer a uni-
formly random amount between 1 and their current bal-
ance (inclusive).
2.greedyAgent:In each step, greedy agents offer their
entire current balance for trade. This strategy aims to
maximize individual trade volume by being “greedy”.
A penalty is applied to the recorded liquidity for greedy
agents under theMinFillrule if they offer more than
their partner, reflecting a potential cost to over-offering
and it set to20%of the excess offered amount. In this
way the agent is designed to be penalized for pure greed.
Metrics
The simulation tracks several metrics per episode to evalu-
ate the performance of different configurations: agent type
(learning, non learning and different learning methods) and
clearing rule (exact and MinFill).
•Cumulative Liquidity over episodesG(z):The sum of
quantities traded across all pairs in a given episode (re-
ported in Figure 3 and 2).
•Convergence on clearing rates:Looking at the
smoothed percentage of each episodes initial balance that
is traded between agents per episode. (see Figure 5).
•Hit Rate:The fraction of paired agents that successfully
complete a trade withq >0(see Figure 4).
By running experiments across the different clearing
rules, reward modes, and baseline strategies, with config-
urable heterogeneity, the code base allows for a comprehen-
sive analysis of factors influencing liquidity in this decen-
tralized simulated market environment.
Results
The experimental results demonstrate the effectiveness of
the difference reward learning framework across different
market clearing mechanisms (see Figure 2). Under the ‘min-
fill‘ clearing rule, which permits partial order execution,
the difference reward approach achieves the highest total
liquidity cleared, outperforming both alternative learning
methods (’Learning (global)’ and ’Learning (local)’) and
baseline agents. This superiority is particularly pronounced
compared to ‘exact‘ clearing, where the difference reward
method maintains strong performance while other learning
approaches converge to similar levels, although still exceed-
ing the baseline benchmarks, as seen in Figure 5 and Figure
6.
Figure 2: Learning agents surpassing baselines.
The cumulative liquidity trajectories reinforce the advan-
tage of difference reward learning, especially under ‘min-
fill‘ where the framework’s ability to attribute credit ef-

Figure 3: Cumulative liquidity through episodes for MinFill
rules
fectively translates into higher liquidity accumulation over
episodes(Figure 3. In particular, the smoothed percentage of
initial balance cleared per episode reveals that difference re-
ward learning consistently achieves the highest clearing ef-
ficiency under ‘minfill‘, demonstrating its capacity to maxi-
mize liquidity utilization relative to available resources.
Figure 4: Hit ratios are high for learning algorithms, shown
here for the exact fill rule (note: by construction, for MinFill
they are 100%).Note:Learning (exact dif f) and learning
(exactlocal) are almost identical results and graphs over-
write each other
As expected, regimes that permit partial clearing pro-
duced higher levels of liquidity, although learning agents
in exact fill environments that used difference rewards were
able to trade still successfully 70% of the time despite con-
straints (Figure 4. These findings support difference rewards
as a practical, incentive-compatible signal for liquidity pro-
vision when microstructure.
While the ‘exact‘ rule constrains overall performance and
compresses differences between methods, the difference re-
ward framework remains competitive, highlighting its ro-
bustness across varying market microstructures and its po-
tential as a powerful approach for multiagent coordination
in financial market simulations.
Figure 5: Clearing rates clearly converge early with learning,
and difference functions in the exact rule being identical to
local learning.
Figure 6: Clearing rates for Minfill learning.
Conclusion
In this work, we show how to integrate Liquidity Games
with decentralized difference-reward learning (Rational
Swarms) to test whether self-interested agents can increase
liquidity for themselves and the market. The results sup-
port both hypotheses.H1:Under the partial clearing rule
(MinFill), the difference reward agents achieved the high-
est aggregate liquidity and per agent throughput, outper-
forming alternative local/global signals and non-learning
baselines.H2:Even under exact-fill constraints, where per-
formance gaps compress difference-reward agents, adapted
quickly, reaching∼70%trade-success rates early in train-
ing and sustaining them thereafter. These findings indicate
that difference rewards provide a practical and incentive-
compatible signal for liquidity provision across microstruc-
ture regimes, with especially strong gains when partial clears
are permitted. These results are particular helpful in the de-
centralized system where agent co-ordination is not accept-
able. Difference rewards implement marginal-contribution
utilities: agents optimize private payoffs that track their
contribution to total liquidity, promoting welfare-improving
outcomes in bilateral markets.
In this paper, we demonstrate that by combining Liquid-
ity Games with Rational Swarms, it is possible to design lo-

cal incentives such that myopic best responses yield system
level gains, turning the liquidity externality into an individ-
ually rational objective. This offers a practical template for
scalable market design without the need for central coordi-
nators or agent co-ordination.
Limitations and next steps.Our experiments use stylized
dynamics (random pairing, reset endowments, no price for-
mation), so external validity requires caution. Future work
will (i) add persistent state and frictions (inventory, transac-
tion costs), (ii) test richer clearing mechanisms and market
impact models, and (iii) analyze sensitivity to agent hetero-
geneity and partial observability. Extending the analysis to
real data or hybrid ABM–RL settings can further probe how
difference rewards scale.
References
Axtell, R. L.; and Farmer, J. D. 2022. Agent-Based Mod-
eling in Economics and Finance: Past, Present, and Future.
Journal of Economic Literature, 1–96.
Bai, S.; Raskob, W.; and M ¨uller, T. 2020. Agent based
model.Radioprotection, 55.
Bank of England. 2015. GEMM Guidebook: A guide to the
roles of the DMO and Primary Dealers in the UK Govern-
ment bond market.
Baumeister, D. 2019.The Future of Decision-Making, 15–
20. Cham: Springer International Publishing. ISBN 978-3-
030-18050-8.
Burkov, A.; and Chaib-Draa, B. 2014. Repeated games for
multiagent systems: a survey.Knowledge Engineering Re-
view, 29(1): 1–30.
Cheshire, J. 2015. Market Making in Bond Markets.RBA
Bulletin March Quater 2015, March 2015(March): 63–74.
Czech, R.; and Pinter, G. 2022. Informed Trading and the
Dynamics of Client-Dealer Connections in Corporate Bond
Markets.Bank of England, Staff Working Paper(895).
Ding, Z.; Granger, C. W. J.; and Engle, R. F. 1993. A
Long Memory Property of Stock Market Returns and a New
Model.Journal of Empirical Finance, 1(1): 83–106.
Duffie, D. 2020. Still the World’s Safe Haven?Hutchins
Working Paper, 62.
Duffie, D.; and Singleton, K. J. 2015. Modeling Term Struc-
tures of Defaultable Bonds.The Review of Financial Studies,
12(4): 687–720.
Epstein, J. M.; and Axtell, R. L. 1996.Growing Artificial
Societies: Social Science from the Bottom Up. MIT Press
Books. The MIT Press. ISBN ARRAY(0x58c9d590).
Epstein, L.; and Schneider, M. 2010. Ambiguity and Asset
Markets.
Fagiolo, G.; Guerini, M.; Lamperti, F.; Moneta, A.; and
Roventini, A. 2017. Validation of Agent-Based Models in
Economics and Finance.Simulation Foundations, Methods
and Applications.
Fatima, S.; Kraus, S.; and Wooldridge, M. 2014.Princi-
ples of Automated Negotiation. Cambridge University Press.
ISBN 9781107002548.
Federal Reserve Bank of New York. 2021. The Netting Ef-
ficiencies of Marketwide Central Clearing.
Frank J. Fabozzi, S. M. 2005.The Handbook of Fixed In-
come Securities, Seventh Edition. New York: McGraw-Hill.
Gatheral, J.; Jaisson, T.; and Rosenbaum, M. 2018. V olatility
is rough.Quantitative Finance, 18(6): 933–949.
Hull, J. C. 2018.Risk Management and Financial Institu-
tions. Hoboken, NJ: John Wiley & Sons, 5 edition. ISBN
978-1119448112.
Hull, J. C. 2022.Options, Futures, and Other Derivatives.
London: Pearson, 11 edition. ISBN 9781292410654.
Kaminka, G. A. 2025. Swarms can be rational.Philo-
sophical Transactions of the Royal Society A: Mathemati-
cal, Physical and Engineering Sciences, 383(2289: Theme
issue ‘The road forward with swarm systems’ compiled and
edited by Hussein A. Abbass and Sanaz Mostaghim).
Kl¨ugl, F.; Fehler, M.; and Herrler, R. 2005. About the Role
of the Environment in Multi-agent Simulations. In Weyns,
D.; Van Dyke Parunak, H.; and Michel, F., eds.,Environ-
ments for Multi-Agent Systems, 127–149. Berlin, Heidel-
berg: Springer Berlin Heidelberg. ISBN 978-3-540-32259-
7.
Lillo, F.; and Farmer, J. D. 2004. The Long Memory of the
Efficient Market.Studies in Nonlinear Dynamics & Econo-
metrics, 8(3).
Lillo, F.; and Farmer, J. D. 2005. Theory for Long Memory
in Supply and Demand.Physical Review E, 72(6): 066122.
Lin, R.; Kraus, S.; Baarslag, T.; Tykhonov, D.; Hindriks, K.;
and Jonker, C. M. 2014. Genius: An integrated environment
for supporting the design of generic automated negotiators.
Computational Intelligence, 30(1): 48–70.
Littman, M. L. 1994. Markov Games as a Framework for
Multi-Agent Reinforcement Learning. InICML, 157–163.
Lussange, J.; Belianin, A.; Bourgeois-Gironde, S.; and
Gutkin, B. 2020. Learning and Cognition in Financial Mar-
kets: A Paradigm Shift for Agent-Based Models.IntelliSys.
Massa, M.; and Simonov, A. 2003. Reputation and in-
terdealer trading: a microstructure analysis of the Treasury
Bond market.Journal of Financial Markets, 6(2): 99–141.
Meir, R.; and Parkes, D. 2018. Playing the Wrong Game:
Bounding Externalities in Diverse Populations of Agents.
arXiv:1411.1751.
Parkes, D. C. 2006.Iterative Combinatorial Auctions Chap-
ter 2 : Iterative Combinatorial Auctions. MIT Press.
Pinter, G. 2023. An anatomy of the 2022 gilt market crisis.
Bank of England, Staff Working Paper 1019.
Pinter, G.; Wang, C.; and Zou, J. 2024. Size Discount and
Size Penalty: Trading Costs in Bond Markets.Review of
Financial Studies, 37(7): 2156–2190.
Shapley, L. S. 1953. Stochastic Games.Proceedings of the
National Academy of Sciences, 39(10): 1095–1100.
Shoham, Y . 2008. Computer science and game theory.Com-
munications of the ACM, 51(8): 74–79.
Shoham, Y .; and Leyton-Brown, K. 2008.Multiagent Sys-
tems: Algorithmic, Game-Theoretic, and Logical Founda-
tions. NY , USA: Cambridge University Press.

Thangarajah, J.; Padgham, L.; and Harland, J. 2002. Repre-
sentation and reasoning for goals in BDI agents.Australian
Computer Science Communications, 24(1): 259–265.
Tumer, K.; and Agogino, A. 2007. Distributed agent-based
air traffic flow management. InIn Proceedings of the 6th in-
ternational joint conference on Autonomous agents and mul-
tiagent systems (AAMAS ’07), 255.
Vermeir, A.; and Bersini, H. 2015. Best Practices in Pro-
gramming Agent-Based Models in Economics and Finance.
Lecture Notes in Economics and Mathematical Systems.
Vidler, A. 2025.Agentic Intelligence in Financial Markets:
A Multi-Agent System with Embedded LLMs for Bilateral
Fixed Income Trading. Ph.D. thesis, UNSW, Australia.
Vidler, A.; and Walsh, T. 2024a. Decoding OTC Govern-
ment Bond Market Liquidity: An ABM Model for Market
Dynamics. InForthcomming, 2025 IEEE Symposium on
Computational Intelligence for Financial Engineering and
Economics.
Vidler, A.; and Walsh, T. 2024b. Non cooperative Liq-
uidity Games and their application to bond market trading.
arXiv:2405.02865.
Wellman, M.; Greenwald, A.; and Stone, P. 2007.Au-
tonomous Bidding Agents: Strategies and Lessons from the
Trading Agent Competition. MIT Press. ISBN 978-0-262-
23260-9.
Winikoff, M.; Padgham, L.; Harland, J.; and Thangarajah,
J. 2002. Declarative & procedural goals in intelligent agent
systems. InProceedings of the Eights International Confer-
ence on Principles of Knowledge Representation and Rea-
soning, KR’02, 470–481. San Francisco, CA, USA: Morgan
Kaufmann Publishers Inc. ISBN 1558605541.
Wooldridge, M. 2009.An Introduction to MultiAgent Sys-
tems, Second Edition. NJ, USA: John Wiley and Sons.
Wooldridge, M.; and Jennings, N. R., eds. 1995.Intelli-
gent Agents, ECAI-94 Workshop on Agent Theories, Archi-
tectures, and Languages, volume 890 ofLecture Notes in
Computer Science. Amsterdam, The Netherlands: Springer.
