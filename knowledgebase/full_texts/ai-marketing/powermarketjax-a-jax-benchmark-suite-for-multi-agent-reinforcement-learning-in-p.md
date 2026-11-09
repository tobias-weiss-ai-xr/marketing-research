---
title: 'PowerMarketJax: A JAX Benchmark Suite for Multi-Agent Reinforcement Learning in Power Markets'
url: https://arxiv.org/abs/2609.37321
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Zhanhua Pan
- Xin Qin
- Xiao Liu
- Zhilong Cao
- Jianhong Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.37321
pages: 69
chars: 199698
fetched_at: '2026-11-08T13:19:59+00:00'
kb_version: 1
---

# PowerMarketJax: A JAX Benchmark Suite for Multi-Agent Reinforcement Learning in Power Markets

Preprint.
POWERMARKETJAX: A JAX BENCHMARKSUITE
FORMULTI-AGENTREINFORCEMENTLEARNING IN
POWERMARKETS
Zhanhua Pan1†, Xin Qin1†, Xiao Liu2, Zhilong Cao1, Jianhong Wang3‡, Dawei Qiu1‡∗
1Nanyang Technological University, Singapore. 2Cornell University, USA. 3University of Bristol, UK.
ABSTRACT
Power markets are a natural testbed for multi-agent reinforcement learning
(MARL), where multiple self-interested participants repeatedly submit bids. A
market-clearing mechanism then determines dispatch and prices subject to power
grid constraints and market settlement rules. However, existing MARL environ-
ments typically focus on a single market setting, implement simplified clearing
mechanisms, or rely on CPU-based optimization solvers that slow large-scale
training and limit the systematic study of bidding strategies and market behavior.
We introduce PowerMarketJax, a benchmark suite for MARL across five power
markets: day-ahead wholesale, real-time balancing, ancillary services, peer-to-
peer double auctions, and local flexibility. Each environment implements its own
clearing, pricing, and settlement rules while providing a common framework for
learning and evaluation. We find that learned bidding behavior depends strongly
on the market design: independent learners can miss better strategies when gains
require many agents to change together, when more profitable strategies lie beyond
a region of lower profit, or when profits disappear as more agents adopt the same
strategy. PowerMarketJax implements both market simulation and policy training
in JAX, allowing the entire pipeline to run on the GPU with 1 024×1 200 par-
allelisms across both environments and market participants, achieving up to 33×
speedup over CPU-based baselines. Our open-source benchmark is available at:
https://github.com/powermarketjax/PowerMarketJax.
1 INTRODUCTION
Unlike most commodities, electricity cannot be stored efficiently at scale, so power markets are
needed to continuously match supply and demand through mechanisms that determine which re-
sources produce and at what price. Historically, these markets involved a relatively small set of large
generators and mainly traded energy, making bidding strategies easier to characterize (David & Wen,
2000). This structure is now changing. Renewable generation, flexible demand, and energy storage
have expanded both who participates and what is traded (Matamala & Strbac, 2025): alongside en-
ergy, markets now trade reserves, balancing, and ancillary services across multiple timescales and
grid levels, each with its own clearing, pricing, and settlement rules (Zhu et al., 2025). This grow-
ing diversity of participants, products, and market mechanisms makes bidding behavior increasingly
difficult to understand, creating an urgent need to study how participants bid and interact across
different market settings. The repeated interactions among many market participants make power
markets a natural setting for multi-agent reinforcement learning (MARL) (Liang et al., 2020).
In a MARL formulation, each market participant can be modeled as an agent that observes market
information, submits bids, receives clearing outcomes, and updates its bidding strategy over time.
Since a participant’s profit depends on both its own bid actions and the actions of others through
market clearing, bidding in power markets is inherently a multi-agent decision problem. MARL
enables participants to learn such bidding strategies through repeated market interactions without
requiring explicit knowledge of competitors’ exact strategies (Du et al., 2021).
∗Corresponding author:dawei.qiu@ntu.edu.sg. †These authors contributed equally. ‡Co-
supervisors.
1
arXiv:2609.37321v1  [cs.MA]  29 Sep 2026

Preprint.
A number of environments have been developed for learning-based bidding in power markets, but
important gaps remain for systematic MARL study. Most focus on a single market study, limit-
ing their use as general benchmarks for MARL-based bidding (Yeh et al., 2023; Harder et al., 2025;
El Helou et al., 2023; Salazar-Pe˜na et al., 2026). A second gap is computational burden. An environ-
ment must solve a market-clearing optimization subject to grid physical constraints after every round
of bids. Existing implementations typically rely on CPU solvers, making the millions of clearing
problems required during MARL training a major computational bottleneck, especially with many
agents and parallel environments (Wolgast & Nieße, 2024). To reduce this computational cost, some
environments simplify pricing or settlement rules, but these simplifications can remove important
market features that shape bidding incentives (Wolgast & Nieße, 2024). As a result, it remains
difficult to systematically study how bidding strategies emerge and differ across power markets.
Here, we introduce PowerMarketJax, a power market MARL benchmark implemented entirely in
JAX (Bradbury et al., 2018). It parallelizes both optimization-based market environments and multi-
agent policy computation on the GPU. By compiling clearing and learning into a single computation
graph, PowerMarketJax avoids repeated CPU solver calls and host-device synchronization at each
market step, enabling large-scale exploration of bidding strategies across different markets. This de-
sign achieves up to 33×higher throughput than CPU-based implementations and runs 1 024 parallel
1 200-participant market environments at over 27 000 environment steps per second (Appendix B).
Our contributions are summarized as follows. First, we present a unified MARL benchmark covering
five power markets: day-ahead wholesale, real-time balancing, ancillary services, peer-to-peer en-
ergy trading, and local flexibility. The benchmark spans different clearing mechanisms, timescales,
and grid levels while preserving each market’s clearing, pricing, and settlement rules under a com-
mon interface. Second, we implement both market-clearing optimization and MARL policy training
entirely in JAX, enabling GPU-based parallel computation across environments and agents for large-
scale training and evaluation. Third, using this benchmark, we empirically show that market design
strongly shapes what independent learners can discover from their own profit signals: profitable
outcomes may require coordinated changes by many agents, lie beyond locally unfavorable regions,
or disappear as more agents adopt the same strategy. These findings reveal learning challenges that
arise from the interaction between strategic incentives and physically constrained power markets.
2 RELATEDWORK
Power Market RL Benchmarks.A growing number of environments support RL for bidding in
power markets. At the transmission level, SustainGym (Yeh et al., 2023) studies storage bidding in
a network-constrained real-time market. ASSUME (Harder et al., 2025) supports RL-based bidding
in European power markets. At the distribution level, OpenGridGym (El Helou et al., 2023) studies
competing bidding agents under distribution network constraints. MARLEM (Salazar-Pe ˜na et al.,
2026) considers MARL-based storage participation in local energy markets. Collectively, these
works demonstrate the potential of (MA)RL for learning bidding strategies under different market
mechanisms and physical constraints.
However, existing environments typically focus on a single market, limiting systematic study of
bidding strategies across diverse power markets. PowerMarketJax instead covers five representative
markets spanning transmission and distribution levels. It further provides a unified framework for
agent–market interaction while preserving each market’s clearing, pricing, settlement, and physical
constraints. Finally, existing environments commonly separate CPU-based market simulation from
GPU-based policy learning, creating repeated CPU–GPU data transfers and making market clearing
a major bottleneck for MARL training. PowerMarketJax implements both market clearing and agent
policy computation in JAX, enabling parallel execution on the GPU.
JAX-based RL Benchmarks.A growing number of RL benchmarks have been implemented in
JAX, motivated by the need for fast and highly parallel simulation (Rutherford et al., 2024). Isaac
Gym (Makoviychuk et al., 2021) showed that moving environment simulation onto the GPU can re-
duce CPU–GPU communication overhead. JAX (Bradbury et al., 2018) further supports accelerator-
native RL through compilation and vectorization. These advances have enabled high-throughput
JAX environments across video games (Koyamada et al., 2023; Radji et al., 2026), physics (Free-
man et al., 2021), robot learning (Zakka et al., 2025), and autonomous driving (Gulino et al., 2023).
2

Preprint.
Recent work has also brought JAX-based acceleration to economic and trading environments.
EconoJax (Ponse et al., 2025) simulates agent-based markets with order matching, JAX-LOB (Frey
et al., 2023) accelerates limit-order-book simulation. These environments primarily rely on pre-
defined if–else rule-based matching logic rather than constrained optimization. In contrast, power
markets provide a distinctive setting where strategic economic decisions are tightly coupled to a
real-world physical grid, requiring market outcomes to satisfy both market rules and engineering
constraints. PowerMarketJax targets this setting by implementing optimization-based market clear-
ing and strategic bidding entirely in JAX across five representative power markets.
3 BACKGROUND
Power systems maintain supply-demand balance through a range of markets for energy, reserves,
and flexibility operating at different timescales and grid levels. Following the market structures
and flexibility mechanisms discussed in Kirschen & Strbac (2026), this benchmark considers five
representative settings: day-ahead wholesale, real-time balancing, ancillary services, peer-to-peer
(P2P) energy trading, and local flexibility, as illustrated in Figure 1. They cover dispatch scheduling
against day-ahead forecasts, adjustment to real-time imbalances, procurement of system reserves,
local energy exchanges among prosumers, and distribution network support from flexible resources.
These markets share a common decision structure but differ in their mechanisms. In each market,
self-interested participants such as generators, storages, and consumers submit bids based on their
asset states and public market signals, without knowing competitors’ private information. Their bids
jointly determine market clearing, prices, and profits. However, the five markets differ in their traded
products, information structures, physical constraints, and clearing and settlement rules. These dif-
ferences shape participants’ incentives and bidding behavior, ultimately affecting market outcomes.
M1 Day-ahead
M4 P2P
Power
plants
Wind
farms
Energy &
reserve bids
Market operator
Demand
bids
Day dDay d-1
M2 Balancing
M3 Ancillary service
15-30min
sec
M5 Flexibility
Power delivery
⋯⋯
⋯
1hour
Figure 1: Five power markets in PowerMarketJax across dif-
ferent timescales and grid levels.
M1: Day-ahead wholesale(Day
d−1, transmission level). Genera-
tion must be scheduled before deliv-
ery daydbecause thermal units re-
quire time to start up and are subject
to time-coupling constraints such as
minimum up/down times. The day-
ahead market clears supply–demand
bids using forecasts for dayd, deter-
mining unit commitment, generation
schedules, and locational marginal
prices (LMPs) that reflect transmis-
sion constraints. Cleared schedules
then establish the baseline for subse-
quent real-time balancing.
M2: Real-time balancing(Dayd,
transmission level). Actual demand
and renewable generation may deviate from day-ahead forecasts because weather and consumption
patterns cannot be predicted exactly one day in advance. The real-time market redispatches available
resources over short intervals, typically every 15–30 minutes on dayd, to maintain supply-demand
balance under updated system conditions. Deviations from day-ahead schedules are settled at real-
time prices, which can be more volatile and therefore expose participants to greater price risk.
M3: Ancillary services(Dayd, transmission level). Scheduled energy alone cannot ensure reliable
operation because system disturbances such as a sudden generator outage can unbalance the system
within seconds, far faster than the 15–30-minute energy dispatch interval. The ancillary services
market procures capabilities such as frequency regulation and operating reserves, with requirements
on availability and response speed. In this market, service providers are paid for reserved capacity, so
their revenue can depend on maintaining available capacity rather than solely on energy production.
M4: Peer-to-peer energy trading(Dayd, distribution level). Prosumers with rooftop solar and
storage can trade energy directly with nearby consumers instead of relying solely on upstream re-
tailers. The P2P market matches buy bids and sell offers within a local energy community. The
3

Preprint.
market-clearing price is determined by the intersection of the aggregated supply and demand curves,
while matched quantities are determined from the submitted buy and sell quantities. Unmatched de-
mand is supplied by the upstream grid at the higher retail price, while unmatched supply is exported
to the grid at the lower feed-in tariff, creating an economic incentive for local peer-to-peer trading.
M5: Local flexibility(Dayd, distribution level) Even when sufficient electricity is available from
the transmission system, distribution networks may become overloaded or local voltages may vi-
olate operating limits. To address these issues, the distribution system operator (DSO) procures
flexibility from local resources, paying them to increase or decrease generation or consumption at
specified locations, times, and durations. Under the pay-as-bid rule considered here, accepted flexi-
bility providers are paid their submitted bid prices rather than a common clearing price.
4 POWERMARKETJAX: POWERMARKETENVIRONMENTS INJAX
PowerMarketJax is a suite of five power market environments implemented in JAX, with each mar-
ket formulated as a MARL environment, as illustrated in Figure 2. The environments span day-
ahead wholesale (M1), real-time balancing (M2), ancillary services (M3), peer-to-peer energy trad-
ing (M4), and local flexibility (M5). The markets preserve their distinct clearing, pricing, settlement,
and physical constraints while following a common agent–market interaction interface.
Despite their different market rules, all five environments follow the same step sequence. Agents
first observe the information available to them and submit their market actions. The market then
clears according to its specific mechanism, the resulting dispatches and prices are settled, and the
environment returns the next states and rewards. We define the reward as the participant profit
under the corresponding settlement rule. Together, these operations define one transition of the
corresponding POSG and are implemented through a commonstepinterface. Further details of
the five environments and their accelerator-based execution are provided below.
JAX code
Batch B
Batched environments
@jax.vmap
POSG
trajectories
[ I × B × T ]
Power market model Accelerated Linear Algebra (XLA)-compatible training process @jax.jit
obs × B
action × B
Agent 1
Learner
(policy)
Day-ahead
POSG transition T
JAX formulation
@lax.scanBalancing
Ancillary
service
Flexibility
P2P
⋯ Agent 2
Agent I
Figure 2: Execution paradigm of PowerMarketJax.
4.1 FIVE MARKET ENVIRONMENTS ASPOSGS
We formulate each market environment as a general-sum partially observable stochastic game
(POSG) (Hansen et al., 2004). For each environment, we describe the market step, agent obser-
vations and actions, the clearing mechanism, reward, and state transition. Detailed market models
and complete POSG formulations are provided in Appendix A.1–A.5.
M1: Day-ahead wholesale.One step corresponds to one day-ahead market clearing, in which all 24
hours of the following day are cleared jointly. Each generator agent observes its initial commitment
status, initial power output, and residual minimum up- and down-time requirements, together with
the public day-ahead demand forecast. Its action consists of the prices submitted across all bid
segments and delivery periods. Given the joint bids, the market-clearing mechanism determines unit
commitment, dispatches, and LMPs, and each generator receives its daily profit as the reward.
M2: Real-time balancing.One step corresponds to one 30-minute real-time market clearing dur-
ing the delivery day. Each generator agent observes its previous realized dispatch, the day-ahead
commitment and schedule for the corresponding hour, the associated day-ahead LMP, and the pub-
lic realized net-demand conditions. Its action consists of the prices submitted across all bid seg-
4

Preprint.
ments for the current real-time interval. Given the joint bids from all generators, the market-clearing
mechanism redispatches the committed generators subject to network and ramping constraints and
determines the real-time LMPs. Each generator receives its realized interval profit under the two-
settlement rule as the reward, where the day-ahead schedule remains settled at the day-ahead LMP
and only deviations are settled at the real-time LMP. The realized dispatch of the current interval is
carried forward as the previous dispatch for the next interval.
M3: Ancillary services.One step corresponds to one 30-minute joint energy–reserve market clear-
ing during the delivery day. Each generator agent observes its previous realized dispatch, the day-
ahead commitment and schedule for the corresponding hour, the associated day-ahead LMP, the
public realized net-demand conditions, and the published reserve requirements. Its action consists
of the energy bid prices across all bid segments together with one reserve bid price for each re-
serve product. Given the joint bids of both energy and reserve, the market-clearing mechanism
co-optimizes energy dispatch and reserve procurement subject to network, ramping, response time,
and reserve capacity constraints, and determines both real-time LMPs and reserve prices. Each
generator then receives its realized interval profit as the reward, including day-ahead and real-time
energy settlements and reserve capacity payments. The realized dispatch of the current interval is
carried forward as the previous dispatch for the next interval.
M4: Peer-to-peer energy trading.One step corresponds to one 15-minute P2P trading interval.
Each prosumer agent observes its own battery state of charge, net energy position, and the public
retail and export prices, where a positive net position corresponds to a buy bid and a negative net
position to a sell offer. It does not observe the private states or contemporaneous bids and asks of
other prosumers. Its trading quantity is fixed before the auction based on its local generation, de-
mand, and battery operation, so its action is the price submitted as an ask when selling or a bid when
buying. Given the joint submissions, the double-auction mechanism sorts sellers and buyers, deter-
mines the matched quantities and uniform local clearing price, and settles any unmatched surplus or
deficit with the upstream grid. Each prosumer then receives its realized interval profit as the reward,
accounting for both P2P and residual grid transactions. The battery state of charge evolves to the
next interval, while generation and demand update the prosumer’s next net energy position.
M5: Local flexibility.One step corresponds to one 1-hour local flexibility procurement interval.
Each aggregator agent observes its own battery state of charge, photovoltaic generation, local de-
mand, and available flexibility, together with the public voltage and line-congestion requirements
published by the DSO. It does not observe the private operating states, delivery costs, or contempo-
raneous bids of competing aggregators. Its action is a price–quantity bid specifying the requested
payment and the maximum flexibility quantity it is willing to provide. Given the joint offers, the
DSO clears the market by minimizing procurement cost subject to network voltage, line flow, and
flexibility delivery constraints, and may partially accept a bid. Each aggregator then receives its
realized interval profit as the reward under the pay-as-bid rule, with accepted flexibility paid at the
submitted bid price. The accepted flexibility changes the battery state of charge and therefore deter-
mines the flexibility available in the next interval, while photovoltaic generation, local demand, and
network conditions evolve to form the next market state.
4.2 CLEARING AND LEARNING IN A SINGLE COMPUTATION GRAPH
Despite their different clearing and settlement mechanisms, all five environments share the same
accelerator-based execution framework, with market simulation and policy learning running within
a single compiled computation graph.
Every operation within a training iteration, including market clearing, runs inside a single compiled
computation graph on the device.resetandstepare pure functions: each step sequentially
applies action submission, market clearing, settlement, and observation construction, while the en-
vironment state is represented as a fixed-structurepytreethat is passed as input and returned as
output. Each step is compiled withjit, vectorized across parallel environments withvmap, and
repeated over a fixed rollout horizon usinglax.scan. The policy is evaluated within the same
graph: during rollout, it maps observations to actions that are passed directly to the environment
step. Policy updates are implemented with a secondlax.scanover epochs and minibatches. A
complete training iteration, consisting of rollout and update, is compiled as a single function. Further
details of the compiled execution graph are provided in Appendix C.8.
5

Preprint.
Market clearing remains inside the compiled graph because each clearing mechanism is expressed
with fixed shape operations and iteration counts. The optimization-based markets use a common
primal–dual interior-point solver for linear programs, with a fixed number of Newton iterations.
The day-ahead market additionally includes binary commitment decisions. Rather than invoking
a mixed-integer solver inside the compiled graph, we use a three-stage procedure. We first relax
the commitment problem to a linear program, round the resulting commitment decisions, and then
re-solve the continuous dispatch problem with the rounded commitment fixed (Appendix A.1.1).
It is noted that the P2P market does not require an optimization solver. Its sorting, matching, and
settlement operations are implemented directly using JAX Primitives (Bradbury et al., 2018).
We validate these market-clearing implementations in three ways (Appendix B.4). First, clear-
ing and settlement results are compared against a NumPy reference implementation. Second,
dual prices produced by the JAX linear-program solver are compared with those obtained from
HiGHS (Huangfu & Hall, 2018), an independent high-performance optimization solver. Third, the
three-stage procedure is compared with the exact mixed-integer solution from HiGHS, with the
commitment decisions kept binary. The resulting optimality gap is reported in Appendix B.4.
We parallelize computation across both environments and agents. Each environment has its own
market state and random key, andvmapbatches multiple environments for parallel execution.
Within each environment, agents remain coupled through the market-clearing mechanism, since
their submitted actions jointly determine the market outcome. For policy evaluation, agents are also
vectorized, so the actions of all agents across all parallel environments are computed simultaneously
on the GPU in a single batched policy evaluation.
5 RESULTS
Systems and data.The three transmission-level markets (M1–M3) use the Britishcase29gb
system1 with 29 buses and 66 generators as the main test case (Appendix E.1.1). They use one year
of Great Britain demand and day-ahead forecast data, with 329 days for training and 36 held-out
days for evaluation. M2 and M3 inherit the commitment and schedules obtained from the day-
ahead market M1. Additional experiments on the 73-unit RTS-GMLC system 2 and the 151-unit
Australian NEM system3 are reported in Appendices E.1 to E.3. At the distribution level, M4 uses
1,200 Belgian households with PV from the Fluvius smart meter dataset 4. M5 uses the 129-bus
SwissDN feeder (Zapparoli et al., 2025) with battery fleets of 24 and 34 aggregators under its 2040
and 2050 scenarios. Detailed market formulations, system parameters, and data descriptions are
provided in Appendices A and E.
MARL algorithms.We evaluate two independent MARL algorithms, IPPO (de Witt et al., 2020)
and SAC (Haarnoja et al., 2018) (the independent version), each with parameter sharing (PS) and
agent-specific parameters (NoPS), giving four learners: IPPO-PS, IPPO-NoPS, SAC-PS, and SAC-
NoPS. Each agent observes only its own available information and maximizes its own market profit,
without a centralized critic or inter-agent communication. We use common default hyperparame-
ters across markets and parallel environment rollouts on the GPU. Full training configurations and
market-specific hyperparameters are provided in Appendix D.
Baselines and evaluation.We compare the learned policies against truthful bidding and the corre-
sponding untrained networks. Truthful bidding provides a competitive reference, while the untrained
network is used to measure the effect of policy training. We further compare the learned policies with
market-specific predefined non-learning strategies, including tests over different generator bidding
levels in M1–M3, a fixed battery arbitrage schedule in M4, and unilateral flexibility-price deviations
in M5. M1–M4 use 3 random seeds per experiment, while M5 uses 3–10 depending on the config-
uration. Evaluation uses held-out data and averages results across seeds. Full evaluation protocols
and additional results are reported in Appendix E.
All experiments run on a workstation with RTX 4500 Ada GPUs, described in Appendix B. The
market models and data, the evaluation protocol and further results are in Appendices A to E.
1https://webhomes.maths.ed.ac.uk/OptEnergy/NetworkData/reducedGB/
2https://github.com/GridMod/RTS-GMLC
3https://github.com/akxen/egrimod-nem-dataset
4https://opendata.fluvius.be/
6

Preprint.
5.1 DAY-AHEAD WHOLESALE MARKET
We start with the day-ahead market (M1) oncase29gb. Each generatoribids atα i times its
marginal generation cost, whereα i ≥1. Here,α i = 1corresponds to truthful bidding, while
αi >1represents bidding above marginal cost. Figure 3(a) shows that all four learners end near
a bidding strategy aroundα i = 1.5. Over the 36 evaluation days, IPPO-PS and IPPO-NoPS learn
to raise market prices withα i = 1.50andα i = 1.56, respectively, and thereby increase the total
generator profits by £643 and £917 million. The other two test systems show the same effect on a
smaller scale, withα i reaching 1.07–1.29 (Appendix E.1.3).
0 100 200 300 400
Training iteration
1.5
1.6
1.7Bidding strategy α
(a)
IPPO-PS
IPPO-NoPS
SAC-PS
SAC-NoPS
1.00 1.25 1.50 1.75 2.00
Bidding strategy α
-400
-200
0
200
400
600
Profit (million £)
697
199
(b)
Bidding together
Bidding individually
Learned policy
Figure 3: M1 day-ahead wholesale market (a) learning curves,
(b) profit evaluation under joint and unilateral bidding strategies.
However, the learned policies
still leave substantial joint profit
unrealized. As shown in Fig-
ure 3(b), when all 66 genera-
tors use the sameα, total profit
reaches the learned policy level
nearα= 1.5and rises to £697
million atα= 2. In contrast,
when one generator’sαis in-
creased at a time while the others
keep their learned IPPO-PS bids
fixed, the resulting profit never
exceeds the learned-policy level
and is highest aroundα= 1.5–
1.7. The learners therefore settle
near a level where raising the bid further does not benefit an individual generator, even though all
generators could gain substantially by raising their bids together.
This gap arises for two reasons. First, the joint gain is not visible in each agent’s individual learning
signal. An independent learner observes only how its own bidding strategy affects its own profit. For
example, cheap nuclear units almost never set the market price (Appendix E.1.4), so raising their
bids alone has little effect on price. Second, independent exploration rarely reaches the high-profit
joint bidding region. The sampledαvalues remain concentrated around 1.5, making it unlikely that
all units simultaneously explore the higher-bid region where the joint gain occurs.
5.2 REAL-TIME BALANCING AND ANCILLARY SERVICES MARKETS
1 10 20 30
Committed units
1.0
1.2
1.4
1.6
1.8
2.0Bidding strategy α
IPPO-PS
IPPO-NoPS
SAC-PS
SAC-NoPS
Untrained
Truthful offer
(a)
0 50 100 150 200
Training iteration
1.0
1.2
1.4
1.6
1.8
2.0Bidding strategy α
IPPO-PS
IPPO-NoPS
SAC-PS
SAC-NoPS
Truthful offer
(b)
0 50 100 150
Reserve offer price (£/MWh)
0
5
10
Profit change
(million £ per day)
Bidding together
Bidding individually
(c)
Figure 4: M2 real-time balancing market (a) bidding strategy,
(b) learning curves, and M3 ancillary services market (c) profit
under joint and unilateral bidding strategies.
We next consider the real-time
balancing (M2) and ancillary ser-
vices (M3) markets. In M2, rais-
ing a bid alone is rarely prof-
itable because a generator can
lose output to its competitors.
Accordingly,α i of the 30 day-
ahead committed generators de-
creases during training under all
four learners, reaching 1.04 un-
der IPPO-PS and 1.24–1.40 un-
der the other three methods (Fig-
ure 4(a,b)). This contrasts with
the day-ahead market, where bid-
ding above cost can increase an
individual generator’s profit.
The difference between individ-
ual and joint incentives is even
clearer in M3 (Figure 4(c)). Rais-
ing the reserve bid of a single
generator produces little gain: across the 29 committed generators, the largest profit increase is
only £0.08 million per day. However, when all 66 generators raise their reserve bids together to
7

Preprint.
£150/MWh, total profit increases by £9.05 million per day. However, the learned policies remain
far below this joint gain, earning only £0.56–£3.69 million per day more than truthful bidding, and
none outperforms its corresponding non-learning strategies.
These results show how markets shape the learning signal available to each independent learner. In
M2, raising a bid can reduce a generator’s own profit, pushing the learned bid toward cost. In M3,
the individual profit signal is nearly zero, making the much larger joint gain difficult to discover.
5.3 PEER-TO-PEER ENERGY MARKET
We next consider the P2P energy market (M4), where 1,200 households with PV and a battery trade
in a double auction every 15 minutes. The learned policies improve household economics relative
to truthful bidding. IPPO-NoPS increases household profit on all evaluation days, while IPPO-PS
achieves the highest average profit, reducing the daily net cost per household from C1.20 under
truthful bidding to C0.69–0.77 (Appendix E.4.3).
The learners, however, adopt different battery strategies (Figure 5(a)). IPPO-NoPS and SAC-NoPS
charge during the midday PV surplus and discharge during the evening demand peak. IPPO-PS and
SAC-PS keep their batteries close to the minimum state of charge after selling their initial energy.
To understand these differences, we let an increasing number of households follow a fixed schedule
that charges from 11:00–15:00 and discharges from 18:00–22:00. A single household gains about
C1.13 per day, but this gain decreases as more households adopt the same strategy and becomes
negative at around 210–240 households (black line in Figure 5(b)), detailed in Appendix E.4.4.
The decline is caused by the resulting change in market prices (Figure 5(c)). Simultaneous charging
raises the midday clearing price, while simultaneous discharging lowers the evening price, reduc-
ing the price differentials on which the arbitrage relies. Once enough households participate, the
remaining differential no longer covers efficiency losses and degradation costs. Thus, a strategy that
is profitable for one household may become unprofitable when widely adopted. Figure 5(b) fur-
ther suggests that PS can make market outcomes requiring heterogeneous behavior harder to learn:
IPPO-NoPS leads only a subset of households to arbitrage, while IPPO-PS leads none to do so.
0 6 12 18 24
Hour of day
0.15
0.5
0.75State of charge
IPPO-NoPS
IPPO-PS
SAC-NoPS
SAC-PS
Single households
(a)
0 1 10 100 1,200
Households on the schedule
−1
0
+1Gain (EUR)
gain
loss
Fixed schedule
IPPO-PS
IPPO-NoPS
(b)
0 6 12 18 24
Hour of day
73
export
203
333
retail
Price (EUR/MWh)
Households
on the
schedule
0
240
1,200
(c)
Figure 5: P2P energy market (a) battery state of charge, (b) household gain, (c) local clearing price.
5.4 LOCAL FLEXIBILITY MARKET
Finally, we consider the local flexibility market (M5), where the DSO procures flexibility from
battery aggregators to relieve network congestion. The market is pay-as-bid with a price floor. All
four learners remain close to the floor. Yet a single aggregator can earn more by raising its offer
sufficiently far above the floor; in the two 3.9 MW configurations, its return exceeds the floor-level
return again at prices around 3.2 times the floor (Figure 6(a,b)).
The reason is the shape of the individual return. A small bidding price increase from an aggregator
causes the operator to procure from other cheaper aggregators instead, sharply reducing the deviating
aggregator’s award and profit. Only at much higher prices does its return recover. Gradient-based
learners therefore encounter a local barrier: small moves away from the floor reduce profit, while
the more profitable region lies much farther away. The price parameterization further weakens
exploration near the floor because the softplus mapping becomes nearly flat.
8

Preprint.
The learners instead increase profit through their planned charging decisions. Planned charging
raises the baseline flow on the congested line and therefore increases the flexibility requirement
that the operator subsequently procures. With SAC-PS learners, the share of periods with procure-
ment rises from 5.0% to 18.7% with 24 aggregators and from 4.9% to 15.4% with 34 aggregators
(Figure 6(c)). A baseline monitor that excludes this learner-induced charging largely removes the
effect, causing both procurement and learner returns to fall sharply. Thus, M5 exposes two distinct
challenges for MARL in markets: profitable deviations may lie beyond a local learning barrier, and
agents can change the demand for the service they are paid to provide.
price floor price cap
Bidding strategy α
Single-agent profit
softplus is flat
here: no gradient
alone above:
operator buys
from others
(a)
150 1 000 10 000
Single-agent offer price (CHF/MWh, log)
0.1
1
10
100
1 000Single-agent profit (CHF, log)
dashed: what it earns
when all offer at the floor
2040 plan, 3.9 MW
2040 plan, 6.3 MW
2050 plan, 3.9 MW
2050 plan, 6.3 MW
(b)
1 8 16 24 34
Number of learners
0
5
10
15
20
Periods in which the
operator buys (%)all truthful: 4.9–5.0%
2040 plan
2050 plan
Bootstrap 95% CI
(c)
Figure 6: M5 local flexibility market (a) schematic return versus own offer price, (b) measured return
in four system configurations, (c) procurement frequency versus the number of SAC-PS learners
(seed mean with 95% bootstrap CI).
6 CONCLUSION
PowerMarketJax shows that MARL benchmarks for power markets can preserve market-design fi-
delity while remaining computationally scalable. By integrating market clearing, settlement, policy
evaluation, and learning into a GPU-accelerated JAX pipeline, the benchmark supports fast multi-
agent rollouts while retaining the mechanisms and physical constraints that shape strategic bidding.
The five markets provide a common POSG framework for evaluating learned bidding behavior and
market outcomes across diverse market designs.
Discussion.The experiments show that learned bidding behavior depends strongly on market design
and the profit signal available to each agent. Across the five markets, learners may miss profitable
joint outcomes, move toward truthful bidding when individual deviations are unprofitable, lose ar-
bitrage gains when many agents adopt the same strategy, or fail to reach more profitable strategies
beyond lower-profit regions. More broadly, these results show that market mechanisms shape the
learning landscape itself: they determine which incentives are applied to individual agents and how
the actions of many learners feed back into prices, dispatch, and procurement. This reflects chal-
lenges for MARL beyond maximizing return, including coordinated exploration, endogenous mar-
ket responses, and heterogeneous agent behavior. Such learning-based simulations can also help
stress-test market designs and reveal strategic incentives before new mechanisms are deployed.
Limitations.PowerMarketJax is a research benchmark rather than a deployment-ready market sim-
ulator or bidding system, and the five environments simplify aspects of real market operation, net-
work modeling, participant constraints, and market rules. Our experiments cover only the considered
systems and independent PPO and SAC variants, so the learned policies should not be interpreted as
predictions of real participant behavior or as equilibrium strategies. Future work could extend the
benchmark to richer market designs, participant models, uncertainty, and broader classes of MARL
algorithms.
ACKNOWLEDGEMENT
Dawei Qiu is supported by the Nanyang Technological University (NTU) Start-Up Grant project
#026749-00001 “Market Design for Low-Carbon Power Systems: Towards a Reliable, Affordable,
and Resilient Transition”. Jianhong Wang is supported by the Engineering and Physical Sciences
Research Council (EPSRC) [Grant Ref: EP/Y028732/1].
9

Preprint.
REFERENCES
Akshay Agrawal, Robin Verschueren, Steven Diamond, and Stephen Boyd. A rewriting system for
convex optimization problems.Journal of Control and Decision, 5(1):42–60, 2018.
James Bradbury, Roy Frostig, Peter Hawkins, Matthew James Johnson, Yash Katariya, Chris Leary,
Dougal Maclaurin, George Necula, Adam Paszke, Jake VanderPlas, Skye Wanderman-Milne,
and Qiao Zhang. JAX: Composable transformations of Python+NumPy programs, 2018. URL
http://github.com/jax-ml/jax.
Thomas Brown, Jonas H¨orsch, and David Schlachtberger. PyPSA: Python for power system analy-
sis.Journal of Open Research Software, 6(1):4–4, 2018.
A.K. David and Fushuan Wen. Strategic bidding in competitive electricity markets: a literature
survey. In2000 Power Engineering Society Summer Meeting (Cat. No.00CH37134), volume 4,
pp. 2168–2173 vol. 4, 2000.
Christian Schroeder de Witt, Tarun Gupta, Denys Makoviichuk, Viktor Makoviychuk, Philip H. S.
Torr, Mingfei Sun, and Shimon Whiteson. Is independent learning all you need in the StarCraft
Multi-Agent Challenge? arXiv:2011.09533, 2020.
Steven Diamond and Stephen Boyd. CVXPY: A Python-embedded modeling language for convex
optimization.Journal of Machine Learning Research, 17(83):1–5, 2016.
Yan Du, Fangxing Li, Helia Zandi, and Yaosuo Xue. Approximating Nash equilibrium in day-
ahead electricity market bidding with multi-agent deep reinforcement learning.Journal of Modern
Power Systems and Clean Energy, 9(3):534–544, 2021.
Rayan El Helou, Kiyeob Lee, Dongqi Wu, Le Xie, Srinivas Shakkottai, and Vijay Subramanian.
OpenGridGym: An open-source AI-friendly toolkit for distribution market simulation.IEEE
Transactions on Smart Grid, 14(2):1555–1565, 2023.
Daniel Freeman, Erik Frey, Anton Raichuk, Sertan Girgin, Igor Mordatch, and Olivier Bachem.
Brax - a differentiable physics engine for large scale rigid body simulation. InProceedings of the
Neural Information Processing Systems Track on Datasets and Benchmarks, volume 1, 2021.
Sascha Yves Frey, Kang Li, Peer Nagy, Silvia Sapora, Christopher Lu, Stefan Zohren, Jakob Foer-
ster, and Anisoara Calinescu. JAX-LOB: A gpu-accelerated limit order book simulator to unlock
large scale reinforcement learning for trading. InProceedings of the Fourth ACM International
Conference on AI in Finance, pp. 583–591, 2023.
Cole Gulino, Justin Fu, Wenjie Luo, George Tucker, Eli Bronstein, Yiren Lu, Jean Harb, Xinlei
Pan, Yan Wang, Xiangyu Chen, et al. Waymax: An accelerated, data-driven simulator for large-
scale autonomous driving research.Advances in Neural Information Processing Systems, 36:
7730–7742, 2023.
Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. Soft actor-critic: Off-policy
maximum entropy deep reinforcement learning with a stochastic actor. In Jennifer Dy and An-
dreas Krause (eds.),Proceedings of the 35th International Conference on Machine Learning,
volume 80 ofProceedings of Machine Learning Research, pp. 1861–1870. PMLR, 2018.
Eric A. Hansen, Daniel S. Bernstein, and Shlomo Zilberstein. Dynamic programming for partially
observable stochastic games. InProceedings of the Nineteenth National Conference on Artificial
Intelligence, Sixteenth Conference on Innovative Applications of Artificial Intelligence, July 25-
29, 2004, San Jose, California, USA, pp. 709–715. AAAI Press / The MIT Press, 2004.
Nick Harder, Kim K. Miskiw, Manish Khanra, Florian Maurer, Parag Patil, Ramiz Qussous, Christof
Weinhardt, Marian Klobasa, Mario Ragwitz, and Anke Weidlich. ASSUME: An agent-based sim-
ulation framework for exploring electricity market dynamics with reinforcement learning.Soft-
wareX, 30:102176, 2025.
Q. Huangfu and J. A. J. Hall. Parallelizing the dual revised simplex method.Mathematical Pro-
gramming Computation, 10(1):119–142, 2018.
10

Preprint.
Daniel S. Kirschen and Goran Strbac.Fundamentals of Power System Economics. Wiley, 3rd
edition, 2026.
Sotetsu Koyamada, Shinri Okano, Soichiro Nishimori, Yu Murata, Keigo Habara, Haruka Kita,
and Shin Ishii. Pgx: Hardware-accelerated parallel game simulators for reinforcement learning.
Advances in Neural Information Processing Systems, 36:45716–45743, 2023.
Yanchang Liang, Chunlin Guo, Zhaohao Ding, and Huichun Hua. Agent-Based modeling in elec-
tricity market using deep deterministic policy gradient algorithm.IEEE Transactions on Power
Systems, 35(6):4180–4192, 2020.
Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin,
David Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, and Gavriel State. Isaac Gym: High
performance GPU-Based physics simulation for robot learning. arXiv:2108.10470, 2021.
Carlos Matamala and Goran Strbac. Strategic bidding in the frequency-containment ancillary ser-
vices market.Applied Energy, 401:126811, 2025.
Koen Ponse, Aske Plaat, Niki van Stein, and Thomas M. Moerland. Econojax: A fast & scalable
economic simulation in jax. InAAMAS ’25: Proceedings of the 24th International Conference on
Autonomous Agents and Multiagent Systems, pp. 1679–1687, Richland, SC, 2025.
Waris Radji, Thomas Michel, and Hector Piteau. Octax: Accelerated chip-8 arcade environments for
reinforcement learning in jax. InInternational Conference on Learning Representations, volume
2026, pp. 72220–72256, 2026.
Antonin Raffin, Ashley Hill, Adam Gleave, Anssi Kanervisto, Maximilian Ernestus, and Noah Dor-
mann. Stable-Baselines3: Reliable reinforcement learning implementations.Journal of Machine
Learning Research, 22(268):1–8, 2021.
Alexander Rutherford, Benjamin Ellis, Matteo Gallici, Jonathan Cook, Andrei Lupu, Gardar In-
gvarsson, Timon Willi, Ravi Hammond, Akbir Khan, Christian Schroeder de Witt, Alexandra
Souly, Saptarashmi Bandyopadhyay, Mikayel Samvelyan, Minqi Jiang, Robert Lange, Shimon
Whiteson, Bruno Lacerda, Nick Hawes, Tim Rockt ¨aschel, Chris Lu, and Jakob Foerster. Jax-
MARL: Multi-Agent RL environments and algorithms in JAX. InAdvances in Neural Informa-
tion Processing Systems 37 (NeurIPS 2024), Datasets and Benchmarks Track, pp. 50925–50951,
2024.
Nelson Salazar-Pe˜na, Alejandra Tabares, and Andr´es Gonz´alez-Mancera. MARLEM: A multi-agent
reinforcement learning simulation framework for implicit cooperation in decentralized local en-
ergy markets.Applied Energy, 412:127546, 2026.
Thomas Wolgast and Astrid Nieße. Approximating energy market clearing and bidding with Model-
Based reinforcement learning.IEEE Access, 12:145106–145117, 2024.
Christopher Yeh, Victor Li, Rajeev Datta, Julio Arroyo, Nicolas Christianson, Chi Zhang, Yize
Chen, Mohammad Mehdi Hosseini, Azarang Golmohammadi, Yuanyuan Shi, Yisong Yue, and
Adam Wierman. SustainGym: Reinforcement learning environments for sustainable energy sys-
tems. InAdvances in Neural Information Processing Systems 36, pp. 59464–59476, 2023.
Kevin Zakka, Baruch Tabanpour, Qiayuan Liao, Mustafa Haiderbhai, Samuel Holt, Jing Luo, Arthur
Allshire, Erik Frey, Koushil Sreenath, Lueder Kahrs, Carmelo Sferrazza, Yuval Tassa, and Pieter
Abbeel. Demonstrating MuJoCo Playground. InRobotics: Science and Systems XXI, 2025.
Lorenzo Zapparoli, Alfredo Oneto, Mar ´ıa Parajeles Herrera, Blazhe Gjorgiev, Gabriela Hug, and
Giovanni Sansavini. Future deployment and flexibility of distributed energy resources in the
distribution grids of Switzerland.Scientific Data, 12:1491, 2025.
Ziqing Zhu, Siqi Bu, Ka Wing Chan, Fangxing Li, Yujian Ye, Chi Yung Chung, and Goran Strbac.
Designing the future electricity spot market with high renewables via reliable simulations.Nature
Reviews Electrical Engineering, 2(5):320–337, 2025.
11

Preprint.
APPENDIXCONTENTS
A Market Models and Partially Observable Stochastic Game 13
A.1 M1: Day-ahead Wholesale Market . . . . . . . . . . . . . . . . . . . . . . . . . . 13
A.2 M2: Real-Time Balancing Market . . . . . . . . . . . . . . . . . . . . . . . . . . 17
A.3 M3: Ancillary Services Market . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
A.4 M4: Peer-to-Peer Local Energy Market . . . . . . . . . . . . . . . . . . . . . . . 24
A.5 M5: Local Flexibility Market . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
B Computation Performance 33
B.1 Three layouts on the peer-to-peer market . . . . . . . . . . . . . . . . . . . . . . . 33
B.2 Across the five markets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
B.3 Against open-source tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
B.4 Implementation validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
C Quickstart and API 37
C.1 Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
C.2 Minimal rollout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
C.3 The environment interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
C.4 Constructing the five markets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
C.5 Scenario and learner configuration . . . . . . . . . . . . . . . . . . . . . . . . . . 40
C.6 Command-line usage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
C.7 Cases and data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
C.8 Clearing and learning in a single computation graph . . . . . . . . . . . . . . . . . 41
D Training Setup and Hyperparameters 44
D.1 Four learners . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
D.2 Hyperparameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
D.3 Training scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
D.4 Evaluation protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
E Additional Market Results 46
E.1 M1: Day-ahead Wholesale Market . . . . . . . . . . . . . . . . . . . . . . . . . . 46
E.2 M2: Real-Time Balancing Market . . . . . . . . . . . . . . . . . . . . . . . . . . 54
E.3 M3: Ancillary Services Market . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
E.4 M4: Peer-to-Peer Local Energy Market . . . . . . . . . . . . . . . . . . . . . . . 61
E.5 M5: Local Flexibility Market . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
12

Preprint.
A MARKETMODELS ANDPARTIALLYOBSERVABLESTOCHASTICGAME
A.1 M1: DAY-AHEADWHOLESALEMARKET
The day-ahead market is a centralized auction held on dayd−1that clears allThourly delivery
periods of daydsimultaneously, with∆ da = 1hour. Market participants submit their strategic bids,
which the market operator clears through a security-constrained unit commitment (SCUC) problem.
The resulting schedules are priced and settled using locational marginal prices (LMPs). Section
A.1.1 presents the market clearing model, section A.1.2 introduces the pricing and settlement rules,
and section A.1.3 formulates the partially observable stochastic game (POSG) for strategic bidding
in day-ahead wholesale market.
A.1.1 MARKET MODEL
Each generator agentisubmits, for each delivery periodt, a stepwise supply curve consisting ofK
segments. Each segmentkhas quantity
Gi,k =
¯pi −p i
K (1)
and bid priceπ i,k,t, wherep i and¯pi are the minimum and maximum outputs of the unit. Bid prices are required to be non-decreasing across segments, i.e.,π i,k,t ≤π i,k+1,t. Technical parameters,
including ramp rates, minimum up- and down-times, start-up costs, and no-load costs, are registered
with the market operator and are not part of the per-period bid. Demand is inelastic and treated as
exogenous.
The day-ahead market jointly determines unit commitment and dispatch over allThourly delivery
periods by solving
min
{g, u, v, w, s}
TX
t=1
 X
i,k
πi,k,t gi,k,t +
X
i
∆da NLi ui,t + VOLL X
n
sn,t

+
X
i,t
Si vi,t,(2a)
subject to
pi,t =p i ui,t +
X
k
gi,k,t,(2b)
0≤g i,k,t ≤G i,k ui,t,(2c)
Pn,t =
X
i: bus(i)=n
pi,t +s n,t −d n,t,(2d)
X
n
Pn,t = 0 (:λ t),(2e)
−F≤PTDF·P t ≤F(:µ + t , µ− t ),(2f)
0≤s n,t ≤d n,t (:ρ n,t),(2g)
−Rdn i ∆da −¯pi wi,t ≤p i,t −p i,t−1 ≤R up i ∆da +p i vi,t,(2h)
ui,t −u i,t−1 =v i,t −w i,t,(2i)
vi,t +w i,t ≤1,(2j)
tX
τ=t−UT i+1
vi,τ ≤u i,t,(2k)
tX
τ=t−DT i+1
wi,τ ≤1−u i,t,(2l)
ui,t, vi,t, wi,t ∈ {0,1}.(2m)
The objective (2a) minimizes the total offered operating cost over the delivery day. The first term
represents the cost of accepted energy offers, the second accounts for the no-load cost of commit-
ted generators, and the third penalizes involuntary load shedding. The start-up costS i is incurred
13

Preprint.
whenever generatoritransitions from off to on. Here,∆ da = 1 his the duration of each day-ahead
delivery period,NL i is the no-load cost, andVOLLis the value of lost load, which is set sufficiently
high so that load shedding is used only as a last resort.
Constraints (2b) and (2c) define the output of each generator. The binary variableu i,t indicates
whether generatoriis committed. Whenu i,t = 1, its output consists of the minimum generation
levelp i plus the accepted quantitiesgi,k,t from its offer segments. Each accepted segment is bounded
byG i,k, so the total output remains within[p i,¯pi]. Whenu i,t = 0, all segment quantities and the generator output are zero.
Constraints (2d)–(2f) impose the network constraints. Equation (2d) defines the net injectionP n,t at
busnas local generation plus load shedding minus exogenous demandd n,t. Constraint (2e) enforces
system-wide supply–demand balance. Under the DC power-flow approximation, constraint (2f)
maps the nodal injections to transmission-line flows through the power transfer distribution factor
matrixPTDF∈R N line×N bus and limits each line flow by its ratingF. Network losses are not
modeled.
Constraint (2g) bounds load shedding at each bus by the local demand. The variables n,t provides
emergency feasibility when available generation and transmission capacity are insufficient to serve
all demand. Because load shedding carries the large penaltyVOLLin the objective, it is used only
when lower-cost feasible alternatives are unavailable.
Constraint (2h) limits the change in generator output between consecutive delivery periods according
to the upward and downward ramp ratesR up i andR dn i . The start-up termp ivi,t allows a unit that starts in periodtto move from zero output to at least its minimum generation level, while the shut-
down term¯piwi,t allows a unit that shuts down to reduce its output to zero.
Constraints (2i) and (2j) describe commitment transitions. The binary variablesv i,t andw i,t denote
start-up and shut-down events, respectively. Equation (2i) links these events to changes in commit-
ment status, while equation (2j) prevents a generator from starting up and shutting down in the same
period.
Constraints (2k) and (2l) enforce the minimum up- and down-timesUT i andDT i. After a start-up,
the unit must remain committed for at leastUT i periods; after a shut-down, it must remain offline
for at leastDT i periods. The initial commitment statusu i,0, initial outputp i,0, and any residual
minimum up- or down-time requirements from the previous day are treated as exogenous initial
conditions.
Solution method.Optimization (2) is a security-constrained unit commitment (SCUC) problem
formulated as a mixed-integer linear program (MILP). Exact MILP solvers rely on dynamic branch-
and-bound procedures that are difficult to batch and compile efficiently on accelerators. We there-
fore use a relax-round-resolve procedure. First, the binary commitment variables are relaxed to
ui,t ∈[0,1], and the resulting linear program is solved. Second, the relaxed commitment is rounded
by settingu int i,t = 1ifu i,t > εandu int i,t = 0otherwise, from which the start-up and shut-down indi-
catorsv int i,t andw int i,t are determined. Third, these commitment decisions are fixed and the continuous
dispatch problem is re-solved as a security-constrained economic dispatch (SCED). Dispatch sched-
ules are obtained from this final solve, while LMPs are computed from the dual variables of its
power balance and transmission constraint. This separation follows the common practice of deter-
mining commitment first and obtaining dispatch and prices with commitment fixed. The optimality
gap relative to the exact solution is evaluated offline and reported in Appendix B.4.
A.1.2 PRICING AND SETTLEMENT
Given the fixed commitment obtained from the solution procedure above, LMPs are computed from
the dual variables of the final SCED problem. The LMP at busnat periodtis the marginal cost of
serving one additional MWh at that bus and is given by
LMPn,t =λ t −
X
l

µ+ l,t −µ − l,t  PTDFl,n −ρ n,t,(3a)
where the first term is the system marginal energy price, which is common across the transmis-
sion network; the second term is the congestion component, which is zero when no transmission
14

Preprint.
constraint is binding and causes nodal prices to differ under congestion; and the third term can be
non-zero only when the upper bound on load curtailment is binding. There is no loss component
because transmission losses are not modeled.
Cleared quantitiesp i,t are settled at the LMP of the bus where unitiis located. The revenue, cost,
and profit of unitiover the market day are
revenuei =
X
t
∆da ·LMP bus(i),t pi,t,(3b)
costi =
X
t

∆da ·TC i(pi,t) + ∆da ·NL i ui,t  + X
t
Si vi,t,(3c)
profiti = revenuei −cost i,(3d)
whereTC i(p) =
R p
0 MCi(x)dxis the true variable generation cost rate of uniti, andMC i(p) =
aip2 +bip+c i is its true marginal cost. Settingai = 0recovers a linear marginal cost curve. The true
variable generation costTC i(·)is used only to evaluate participant profit and does not enter market
clearing; the clearing problem instead uses submitted energy offer prices together with the registered
no-load and start-up costs. Settlement does not include uplift payment, so a committed unit may earn
negative profit when its energy market revenue does not recover its start-up and no-load costs.
A.1.3 PARTIALLYOBSERVABLESTOCHASTICGAME
We formulate repeated participation in the day-ahead wholesale market as a general-sum POSG
GDA =⟨ I,S,{O i}i∈I,{A i}i∈I, P,{ri}i∈I, γ⟩,(4)
whereIis the set of strategic generator agents,Sis the market state space,O i andA i are the
observation and action spaces of agenti,Pis the state transition kernel,r i is the individual profit-
based reward, andγ∈[0,1]is the discount factor. One episodic market step corresponds to one
day-ahead market clearing, in which allTdelivery periods of the following day are cleared jointly.
State.At market dayd, the underlying state contains the system information required to clear the
following delivery day,
sd = (x sys d ,{x i,d}i∈I )∈ S,(5)
wherex sys d contains the day-ahead forecast of system demandd n,t,d and other exogenous system conditions such as renewable generation. The generator state is
xi,d =

u0 i,d, p0 i,d, τup i,d , τdn i,d

,(6)
whereu 0 i,d andp 0 i,d are the commitment status and power output of generatorientering the delivery
day, andτ up i,d andτ dn i,d denote any residual minimum up- and downtime requirements carried over
from the previous day. Other system and generator parameters, such as the PTDF matrixPTDF,
transmission limitsF, generation capacity limits(p i, Gi,k), and ramp rates(R up i , Rdn i ), are fixed environment parameters known to the market operator.
Observation.Each generatoriobserves its own private information and the public information
available before bidding,
oi,d ∈ Oi(sd) =

xi,d, xpub d

,(7)
wherex pub d includes the public day-ahead system information of demand forecastd n,t,d. An agent does not observe the private generation costs or contemporaneous offers of competing generators
before market clearing. Hence,o i,d does not fully reveals d, making the bidding problem partially
observable.
Action.The action of generatoriis a single markupα i,d on its truthful offerπ 0 i,1 ≤ · · · ≤π0 i,K,
in which each segment is priced at the unit’s true marginal costMCi, giving its complete day-ahead
price bid over all segments and delivery periods,
ai,d =α i,d ∈ Ai = [1,¯α], π i,k,t,d =α i,d π0 i,k, k= 1, . . . , K;t= 1, . . . , T,(8)
15

Preprint.
where¯αis the largest admissible markup. The segment quantitiesG i,k are fixed as defined in
Section A.1.1, while the agent chooses the markup. Admissible bids satisfy the market price bounds
and the monotonicity rule
π ≤π i,1,t,d ≤π i,2,t,d ≤ · · · ≤πi,K,t,d ≤ π,∀t.(9)
The joint actiona d = (a1,d, . . . , a|I|,d)therefore represents the set of supply bids submitted by all
strategic generators for the following delivery day.
Market clearing and outcome.Given states d and joint actiona d, the market operator applies
the day-ahead clearing model and pricing rules described in Sections A.1.1–A.1.2. We denote this
mapping by
zd =C DA(sd, ad),(10)
where the market outcomez d contains the commitment decisionsu i,1...T,d, accepted generation
quantitiesg i,k,1...T,d , dispatch schedulesp i,1...T,d, load curtailments n,1...T,d, and nodal LMPs
LMPn,1...T,d for allTdelivery periods. Through this clearing mechanism, the payoff of one agent
depends not only on its own offer but also on the bids submitted by the other agents.
Reward.Each agentireceives its realized market profit as reward. Using the settlement defined
in Section A.1.2,
ri,d = profiti,d = revenuei −cost i
=
TX
t=1
∆da LMPbus(i),t,d pi,t,d
−
TX
t=1

∆da TCi(pi,t,d) + ∆da NLiui,t,d  − TX
t=1
Si vi,t,d.(11)
Thus, submitted bidding prices affect the reward only through the resulting market-clearing out-
comes; the true variable generation costTC i(·)is used only to evaluate the realized cost and then
profit. Since each generator maximizes its own profit rather than a common system-wide reward,
the resulting POSG is general-sum.
State transition.After the delivery periods cleared at market stepd, the terminal operating condi-
tion of each generator is carried into the next market step. Specifically, the initial commitment status
and power output for the next day are
u0 i,d+1 =u i,T,d , p 0 i,d+1 =p i,T,d ,(12)
while the residual minimum up- or downtime requirementsτ up i,d+1 andτ dn i,d+1 are updated according
to the terminal commitment trajectory. Hence, the next generator state
xi,d+1 =

u0 i,d+1, p0 i,d+1, τup i,d+1, τdn i,d+1

(13)
depends on the commitment and dispatch outcomes produced by the joint bids at market stepd.
The exogenous system statex sys d+1, including the next day-ahead forecasts of demand, evolves ac- cording to the underlying data process. The overall state transition is therefore
sd+1 ∼P(· |s d, ad),(14)
where the dependence ona d arises through the cleared commitment and dispatch decisions carried
into the next market step.
Agent objective.Each generator uses a policyσ i(ai,d |o i,d)to choose its day-ahead bid and seeks
to maximize its expected discounted profit over an episode ofHmarket days,
Ji(σi, σ−i) =E
" HX
d=1
γd−1ri,d
#
.(15)
whereσ −i denotes the joint policies of all other generators. Because market clearing depends on
the joint bids of all generators, the expected return of agentidepends on both its own policyσ i and
the policies of the other agentsσ −i. Each agent therefore learns its bidding policy through repeated
market interactions without observing competitors’ private information or policies.
16

Preprint.
A.2 M2: REAL-TIMEBALANCINGMARKET
The real-time balancing market consists of a sequence of auctions during delivery dayD, with
one auction for each real-time interval∆ rt = 30mins. It takes the commitment and schedules
established by the day-ahead wholesale market as fixed and redispatches available resources against
realized system demand. Only deviations from the day-ahead schedules are settled at real-time
LMPs, while the day-ahead schedules remain settled at day-ahead LMPs. This section presents the
real-time balancing market clearing model in subsection A.2.1, the two-settlement rule in subsection
A.2.2, and the corresponding POSG in subsection A.2.3.
A.2.1 MARKET MODEL
Letτindex the 30-minute real-time intervals and leth(τ)denote the corresponding hourly period in
the day-ahead market. The day-ahead outcome enters the real-time market as fixed data through the
commitmentu da i,h(τ) , scheduled generationq da i,h(τ) , and day-ahead priceLMP da n,h(τ) . The realized
net demand at busnis ˜dn,τ . Generators submit price–quantity bids with the same structure as in the
day-ahead market, and one market clearing problem is solved for each real-time interval:
min
{g, s}
X
i,k
πi,k,τ gi,k,τ + VOLL
X
n
sn,τ ,(16a)
subject to
pi,τ =p i uda i,h(τ) + X
k
gi,k,τ ,(16b)
0≤g i,k,τ ≤G i,k uda i,h(τ) ,(16c)
Pn,τ =
X
i:bus(i)=n
pi,τ +s n,τ − ˜dn,τ ,(16d)
X
n
Pn,τ = 0 (:λ τ ),(16e)
−F≤PTDF·P τ ≤F(:µ + τ , µ− τ ),(16f)
0≤s n,τ ≤max( ˜dn,τ ,0) (:ρ n,τ ),(16g)
−Rdn i ∆rt −¯piwda i,τ ≤p i,τ −p i,τ−1 ≤R up i ∆rt +p ivda i,τ .(16h)
The objective minimizes the as-bid redispatch cost and load-shedding penalty for each real-time
interval∆ rt. Unlike the day-ahead market, unit commitment is not re-optimized:u da i,h(τ) is fixed
by the day-ahead outcome, and the real-time market only adjusts the dispatch of committed units.
The nodal balance and transmission constraints ensure that the resulting dispatch remains physically
feasible under realized net demand. Consecutive real-time intervals are coupled through the ramping
constraint, wherep i,τ−1 is the realized dispatch from the previous interval. The start-up and shut-
down indicatorsv da i,τ andw da i,τ are determined by changes in the mapped day-ahead commitment and
are non-zero only when the commitment status changes between consecutive real-time intervals.
Constraint (16b) defines the real-time output of generatori. Because the commitmentu da i,h(τ) is
fixed by the day-ahead market, only generators committed in the corresponding day-ahead period
can produce in real time. Their output equals the minimum generation level plus the accepted
quantities from the submitted bid segments. Constraint (16c) limits each accepted segmentg i,k,τ
to its available quantityG i,k. Constraint (16d) defines the net injectionP n,τ at busnas local
generation plus load shedding minus realized net demand. Constraint (16e) enforces system-wide
supply–demand balance, while constraint (16f) keeps transmission flows within the line ratings. The
associated dual variablesλ τ ,µ + τ , andµ − τ are used to determine the real-time LMPs.
Constraint (16g) allows emergency load curtailment only up to the positive net demand at each
bus. Hence,s n,τ = 0when renewable generation exceeds local demand. The dual variableρ n,τ
is associated with the upper bound on load shedding. Constraint (16h) limits changes in generator
output between consecutive real-time intervals according to the upward and downward ramp rates.
17

Preprint.
Here,p i,τ−1 is the realized dispatch from the previous real-time interval. The fixed indicatorsv da i,τ
andw da i,τ account for start-up and shut-down transitions implied by the day-ahead commitment.
Unlike the day-ahead market, the real-time market does not re-optimize unit commitment. The
day-ahead commitment is fixed, and the real-time clearing adjusts only the dispatch quantities in re-
sponse to realized system conditions. Consecutive real-time intervals are coupled through generator
ramping.
A.2.2 PRICING AND SETTLEMENT
Real-time LMPs are computed from the dual variables of the real-time clearing problem using the
same energy–congestion decomposition as in equation (3a):
LMPrt n,τ =λ τ − X
l

µ+ l,τ −µ − l,τ

PTDFl,n −ρ n,τ .(17)
Unlike day-ahead LMPs, the real-time LMPs reflect realized demand and short-term operating con-
straints. They can therefore be more volatile and may become negative under local oversupply or
binding downward-flexibility constraints.
The market follows a two-settlement rule. The day-ahead schedule remains settled at the day-ahead
LMP, while only the deviation from that schedule is settled at the real-time LMP. For generatoriin
real-time intervalτ,
revenueda i,τ = ∆rt LMPda bus(i),h(τ) qda i,h(τ) ,(18a)
revenuert i,τ = ∆rt LMPrt bus(i),τ

pi,τ −q da i,h(τ)

,(18b)
costi,τ = ∆rt TCi(pi,τ ) + ∆rt NLiuda i,h(τ) +S ivda i,τ ,(18c)
profiti,τ = revenueda i,τ + revenuert i,τ −cost i,τ .(18d)
In this context, a generator producing above its day-ahead schedule sells the positive deviation at the
real-time LMP, while a generator producing below its schedule effectively buys back the shortfall at
the real-time LMP. The day-ahead revenue, commitment status, and associated no-load and start-up
costs are fixed by the day-ahead outcome and do not depend on the real-time bid. They are retained
in the reward so that the reported profit represents the full economic outcome of delivery.
Remark on the day-ahead and real-time coupling.In practice, the two markets operate at different
temporal scales: the day-ahead market is cleared on dayD−1, while the real-time market is cleared
at each interval of delivery dayD. The commitmentu da i,h(τ) , binding scheduleq da i,h(τ) , and day-
ahead priceLMP da n,h(τ) are fixed parameters of the real-time clearing, while the real-time market
prices deviations arising from uncertainty not captured by the day-ahead forecast.
A.2.3 PARTIALLYOBSERVABLESTOCHASTICGAME
The real-time balancing market can be also formulated as a general-sum partially observable
stochastic game (POSG),
Grt =⟨ I,S,{O i}i∈I,{A i}i∈I, P,{ri}i∈I, γ⟩,(19)
whereIis the set of strategic generators. One episodic market stepτcorresponds to one 30-minute
real-time interval∆ rt. For a 24-hour delivery day, the real-time market therefore containsT rt = 48
sequential clearing steps.
State.The state at intervalτis
sτ =

xsys τ , xda τ ,{x i,τ }i∈I  ∈ S,(20)
wherex sys τ contains the realized system conditions used for real-time clearing, i.e., the net bus
demand ˜dn,τ . The day-ahead component is
xda τ = n uda i,h(τ) , qda i,h(τ) ,LMP da n,h(τ) o i,n ,(21)
18

Preprint.
which contains the fixed commitmentu da i,h(τ) , binding generation schedulesq da i,h(τ) , and nodal prices
LMPda n,h(τ) from the corresponding day-ahead period. The operating state of generatoriis
xi,τ =

pi,τ−1 , vda i,τ , wda i,τ  ,(22)
wherep i,τ−1 is the realized dispatch from the previous real-time intervalτ−1, andv da i,τ andw da i,τ
are the start-up and shut-down indicators implied by the mapped day-ahead commitment, which
are used in the ramping constraint (16h) to account for output changes associated with start-up and
shut-down transitions. Network parameters, generator operating limits, and cost parameters are fixed
environment parameters and are omitted from the dynamic state.
Observation.Each generatoriobserves its own operating information together with public market
information. Its observation at real-time intervalτis
oi,τ =

pi,τ−1 , uda i,h(τ) , qda i,h(τ) ,LMP da bus(i),h(τ) , xpub τ

= Ωi(sτ )∈ Oi,(23)
wherep i,τ−1 is the generator’s realized dispatch in the previous real-time intervalτ−1,u da i,h(τ)
andq da i,h(τ) are its day-ahead commitment and schedule, andLMP da bus(i),h(τ) is the corresponding
day-ahead LMP. The public real-time market information is denoted byx pub τ , which is the realized
system conditions of net bus demandx sys τ = ˜dn,τ . A generator does not observe the private parame-
ters or contemporaneous bids of other generators. The market is therefore partially observable from
the perspective of each participant.
Action.At each real-time interval, generatorisubmits a stepwise supply bidπ i,τ , obtained from
a single markupα i,τ on its truthful offerπ 0 i,1 ≤ · · · ≤π0 i,K, in which each segment is priced at the
unit’s true marginal costMC i,
ai,τ =α i,τ ∈ Ai = [1,¯α], π i,k,τ =α i,τ π0 i,k, k= 1, . . . , K,(24)
where¯αis the largest admissible markup, subject to the admissible bid-price bounds and the mono-
tonicity condition
πi,1,τ ≤π i,2,τ ≤ · · · ≤πi,K,τ .(25)
The segment quantitiesG i,k are fixed, so the strategic action determines the bid prices associated
with these quantities. The joint action isa τ = (ai,τ )i∈I.
Market clearing and reward.Given the current state and joint bids, the market-clearing mecha-
nism
zτ =C rt(sτ , aτ )(26)
solves optimization (16) and returns the realized dispatchp i,τ , accepted bid quantitiesg i,k,τ , and
real-time LMPsLMP rt n,τ . Each generator receives its realized profit as the stage reward,
ri,τ = profiti,τ = revenueda i,τ + revenuert i,τ −cost i,τ
= ∆rt LMPda bus(i),h(τ) qda i,h(τ) + ∆rt LMPrt bus(i),τ

pi,τ −q da i,h(τ)

−

∆rt TCi(pi,τ ) + ∆rt NLiuda i,h(τ) +S ivda i,τ  .(27)
whereprofit i,τ is defined by the two-settlement rule in equation (18). The reward therefore accounts
for the fixed day-ahead position, the real-time settlement of deviations, and the realized generation
cost.
State transition.The clearing result determines the operating state entering the next real-time
interval. In particular, the realized dispatchp i,τ becomes the previous-period dispatch in interval
τ+ 1, so that
xi,τ+1 =

pi,τ , vda i,τ+1 , wda i,τ+1  .(28)
Thus, the dispatch determined at intervalτenters the ramping constraint of intervalτ+ 1. The
corresponding day-ahead commitment, schedule, and price are updated deterministically according
toh(τ+ 1), while realized net demand evolves according to the exogenous data process. The overall
state transition is therefore
sτ+1 ∼P(· |s τ , aτ ).(29)
19

Preprint.
Agent objective.Each generator uses a policyσ i(ai,τ |o i,τ )to select its real-time bid. Over a
horizon ofHreal-time intervals, generatoriseeks to maximize its expected discounted profit,
Ji(σi, σ−i) =E
" HX
τ=1
γτ−1 ri,τ
#
,(30)
whereσ −i denotes the joint policies of the other generators. Because both dispatch and real-time
prices are determined jointly by all submitted bids, the return of each generator depends on both its
own bidding policy and those of the other participants. Agents therefore learn their real-time bidding
policies through repeated market interactions without observing competitors’ private information or
policies.
A.3 M3: ANCILLARYSERVICESMARKET
The ancillary services market procures operating reserve, where generation capacity is held available
to respond to system contingencies. Unlike the energy market, it primarily trades availability: a
provider is paid for maintaining reserve capacity that can be activated when needed but may never
be called. In some market designs, operating reserve is co-optimized with real-time energy, so
energy dispatch and reserve procurement are determined jointly for the same resources subject to
shared operating constraints. This section presents the ancillary services market clearing model in
subsection A.3.1, the pricing and settlement rules in subsection A.3.2, and the corresponding POSG
in subsection A.3.3.
A.3.1 MARKET MODEL
The market containsN prod = 2reserve products distinguished by their response times: a fast
product withθ 1 = 10 minsand a slow product withθ 2 = 30 mins. Before bids are submitted,
the system operator publishes the reserve requirement for each product, which can be modeled as a
fraction of forecast system demand,
dres j,τ =β j X
n
dforecast n,τ ,(31)
whered forecast n,τ is the published demand forecast at busnandβ j is the requirement fraction for
reserve productj.
For each real-time interval, generatorisubmits the energy offer described in section A.2.1, together
with a reserve offer priceπ res i,j,τ ≥0for each productj, expressed in $/MW-h. The energy and
reserve markets are cleared jointly as
min
{g, r, s, sres}
X
i,k
πi,k,τ gi,k,τ +
X
i,j
πres i,j,τ ri,j,τ + VOLL X
n
sn,τ + VOLR
X
j
sres j,τ ,(32a)
subject to
pi,τ =p i uda i,h(τ) + X
k
gi,k,τ ,(32b)
0≤g i,k,τ ≤G i,k uda i,h(τ) ,(32c)
Pn,τ =
X
i:bus(i)=n
pi,τ +s n,τ − ˜dn,τ ,(32d)
X
n
Pn,τ = 0 (:λ τ ),(32e)
−F≤PTDF·P τ ≤F(:µ + τ , µ− τ ),(32f)
0≤s n,τ ≤max( ˜dn,τ ,0) (:ρ n,τ ),(32g)
−Rdn i ∆rt −¯piwda i,τ ≤p i,τ −p i,τ−1 ≤R up i ∆rt +p ivda i,τ ,(32h)
0≤r i,j,τ ≤R up i θj,(32i)
pi,τ +
X
j
ri,j,τ ≤¯pi uda i,h(τ) (:ν cap i,τ ),(32j)
20

Preprint.
dres j,τ − X
i
ri,j,τ −s res j,τ ≤0 (:λ res j,τ ),(32k)
0≤s res j,τ ≤d res j,τ .(32l)
The objective in equation (32a) minimizes the joint as-bid cost of energy dispatch and reserve pro-
curement for each real-time interval∆ rt, together with penalties for unserved energy and unmet
reserve requirements. The first term represents the accepted energy offers, and the second term
represents payments associated with reserve capacity held available for contingency response. The
penaltiesVOLLandVOLRare assigned to load shedding and reserve shortage, respectively. We
setVOLR<VOLLso that, when available capacity is insufficient to satisfy both requirements, the
model permits a reserve shortage before shedding firm load.
Constraints (32b)–(32h) describe the energy dispatch and follow the real-time balancing model in
section A.2.1. Constraint (32b) defines the output of generatorias its committed minimum output
plus the accepted quantities from its energy-offer segments. Constraint (32c) bounds each accepted
segment by its available quantity. Constraints (32d) and (32e) define nodal injections and enforce
system-wide supply–demand balance, respectively. Constraint (32f) keeps transmission flows within
the line ratings, and (32g) allows emergency load shedding when available generation is insufficient.
Constraint (32h) limits the change in generator output between consecutive real-time intervals.
Constraints (32i)–(32l) introduce the reserve products. Constraint (32i) limits the reserve award
ri,j,τ to the amount of additional output that generatorican deliver within the required response
timeθ j. Therefore, a product with a longer response time allows a generator to provide more re-
serve capacity for a given ramp rate. Constraint (32j) couples energy and reserve procurement. The
scheduled energy output and the total reserve capacity awarded to a generator must jointly remain
below its committed capacity. Consequently, capacity used to produce energy cannot simultane-
ously be sold as reserve, creating an opportunity-cost trade-off between the two products. The dual
variableν cap i,τ represents the marginal value of additional available capacity of generatori. Finally,
constraint (32k) requires the total procured capacity for reserve productjto satisfy the published
requirementd res j,τ . The slack variables res j,τ represents any unmet reserve requirement and is bounded
by constraint (32l). The corresponding dual variableλres j,τ gives the marginal clearing price of reserve
productj.
A.3.2 PRICING AND SETTLEMENT
Energy prices follow the same LMP formulation as in equation (17), evaluated using the dual vari-
ables of the joint energy–reserve clearing problem (32). The reserve price of productjis determined
by the dual variableλ res j,τ associated with the reserve requirement constraint (32k). It represents the
marginal cost of increasing the system-wide requirement for reserve productjby one additional unit
of capacity.
A key feature of co-optimization is that the opportunity cost of reserving generation capacity is
determined within the clearing problem. When the response-time constraint is non-binding, the
marginal cost of providing reserve consists of two components: the submitted reserve offer and the
opportunity cost of using generation capacity for reserve rather than energy. The latter is represented
by the shadow priceν cap i,τ of the shared capacity constraint. Hence, for a marginal reserve provider,
λres j,τ =π res i,j,τ +ν cap i,τ .(33)
If the same generator is also marginal in the energy market and no additional operating constraint is
binding, the capacity shadow value corresponds to the energy margin,
νcap i,τ = LMPrt bus(i),τ −π i,k,τ ,(34)
and therefore
λres j,τ =π res i,j,τ +  LMPrt bus(i),τ −π i,k,τ  .(35)
Thus, the reserve price accounts not only for the submitted reserve offer but also for the value of
energy production that the marginal provider gives up when capacity is allocated to reserve.
21

Preprint.
Energy is settled according to the two-settlement rule in equation (18). Reserve capacity is settled
separately at the clearing price of each product. For generatori,
revenueres i,τ = ∆rt X
j
λres j,τ ri,j,τ ,(36)
and its total profit for the interval is
profiti,τ = revenueda i,τ + revenuert i,τ + revenueres i,τ −cost i,τ .(37)
where
revenueda i,τ = ∆rt LMPda bus(i),h(τ) qda i,h(τ) ,(38)
revenuert i,τ = ∆rt LMPrt bus(i),τ

pi,τ −q da i,h(τ)

,(39)
costi,τ = ∆rt TCi(pi,τ ) + ∆rt NLiuda i,h(τ) +S ivda i,τ .(40)
Reserve availability itself does not consume fuel, so no additional generation cost is assigned to a
reserve award unless the reserve is activated. Every cleared MW of the same reserve product is
paid the same product price, so a provider whose reserve offer is below the clearing price earns an
inframarginal margin.
Remark on energy–reserve co-optimization.Constraint (32j) couples energy dispatch and reserve
procurement because both compete for the same generation capacity. Increasing the reserve award
can reduce the capacity available for energy production, while increasing energy output reduces the
headroom available for reserve. The joint clearing therefore allows an agent’s energy and reserve
offers to interact through this shared capacity constraint.
The ancillary services market is implemented as a separate benchmark task that extends the real-time
balancing market with reserve products. The day-ahead commitment, schedule, and prices enter as
fixed inputs, while real-time energy and reserve are cleared jointly. Settingd res j,τ = 0for all reserve
products removes the reserve layer and recovers the real-time balancing model of section A.2.
A.3.3 PARTIALLYOBSERVABLESTOCHASTICGAME
The ancillary services market is formulated as a general-sum POSG,
Gas =⟨ I,S,{O i}i∈I,{A i}i∈I, P,{ri}i∈I, γ⟩,(41)
whereIdenotes the set of strategic generators. One episodic market step corresponds to one 30-
minute real-time intervalτ, during which energy and reserve are cleared jointly.
State.The state at intervalτis
sτ =

xsys τ , xda τ , xres τ ,{x i,τ }i∈I  ∈ S,(42)
wherex sys τ contains the realized system conditions of demand ˜dn,τ used in the joint energy–reserve
clearing. The day-ahead component is
xda τ = n uda i,h(τ) , qda i,h(τ) ,LMP da n,h(τ) o i,n ,(43)
which contains the fixed commitment, binding generation schedules, and nodal prices from the
corresponding day-ahead period. The reserve component is
xres τ =  dres 1,τ , . . . , dres N prod,τ  ,(44)
whered res j,τ is the system-wide requirement for reserve productjpublished before bidding. The
operating state of generatoriis
xi,τ =

pi,τ−1 , vda i,τ , wda i,τ  ,(45)
wherep i,τ−1 is the realized dispatch from the previous real-time interval, andv da i,τ andw da i,τ are
the start-up and shut-down indicators implied by the mapped day-ahead commitment. Network
parameters, reserve-product response times, generator operating limits, and cost parameters are fixed
environment parameters and are omitted from the dynamic state.
22

Preprint.
Observation.Each generator observes its own operating information together with the public en-
ergy and reserve market information available before bidding. Its observation at intervalτis
oi,τ =

pi,τ−1 , uda i,h(τ) , qda i,h(τ) ,LMP da bus(i),h(τ) , xsys τ , xres τ

= Ωi(sτ )∈ Oi.(46)
Thus, the generator observes the realized net-demand conditions and the published reserve require-
ments in addition to its own day-ahead position and previous dispatch. It does not observe competi-
tors’ private cost information or their contemporaneous energy and reserve offers. The market is
therefore partially observable from the perspective of each participant.
Action.At each interval, generatorijointly submits an energy offer and one reserve offer price
for each reserve product. Its action is
ai,τ =

πen i,τ ,π res i,τ  ∈ Ai,(47)
where
πen i,τ = (πi,1,τ , . . . , πi,K,τ ), π i,k,τ =α i,τ π0 i,k,(48)
is the stepwise energy-offer price vector, obtained from a single markupαi,τ ∈[1,¯α]on the truthful
offerπ 0 i,1 ≤ · · · ≤π0 i,K as in the real-time balancing market, and
πres i,τ =  πres i,1,τ , . . . , πres i,N prod,τ  (49)
contains the reserve offer prices. The energy offer satisfies
πi,1,τ ≤π i,2,τ ≤ · · · ≤πi,K,τ ,(50)
while0≤π res i,j,τ ≤VOLRfor each reserve productj. The energy segment quantitiesG i,k are
fixed, and no reserve quantity is submitted by the agent; the reserve awards are determined by the
co-optimization. The joint action isa τ = (ai,τ )i∈I.
Market clearing and reward.Given the current state and joint energy–reserve offers, the market-
clearing mechanism
zτ =C as(sτ , aτ )(51)
solves the co-optimization problem (32). The clearing outcome includes the energy dispatchp i,τ ,
reserve awardsr i,j,τ , real-time LMPsLMP rt n,τ , and reserve pricesλ res j,τ .
Each generator receives its total realized profit as the stage reward,
ri,τ = profiti,τ = revenueda i,τ + revenuert i,τ + revenueres i,τ −cost i,τ
= ∆rt LMPda bus(i),h(τ) qda i,h(τ) + ∆rt LMPrt bus(i),τ

pi,τ −q da i,h(τ)

+ ∆rt X
j
λres j,τ ri,j,τ −  ∆rt TCi(pi,τ ) + ∆rt NLiuda i,h(τ) +S ivda i,τ  .(52)
as defined in section A.3.2. The reward therefore captures both energy-market profit and reserve-
capacity revenue.
State transition.The clearing outcome determines the operating state entering the next real-time
interval. In particular,
xi,τ+1 =

pi,τ , vda i,τ+1 , wda i,τ+1  ,(53)
so the realized dispatchp i,τ enters the ramping constraint of the next interval. The corresponding
day-ahead commitment, schedule, and price are updated deterministically according toh(τ+ 1),
while the realized net demand and reserve requirements evolve according to their exogenous data
processes. The overall transition is therefore
sτ+1 ∼P(· |sτ , aτ ).(54)
23

Preprint.
Agent objective.Each generator uses a policyσ i(ai,τ |o i,τ )to jointly determine its energy and re-
serve offers. Over a horizon ofHreal-time intervals, generatorimaximizes its expected discounted
profit,
Ji(σi, σ−i) =E
" HX
τ=1
γτ−1 ri,τ
#
,(55)
whereσ −i denotes the joint policies of the other generators. Because energy dispatch, reserve
awards, and both energy and reserve prices are jointly determined by all submitted offers, the return
of each generator depends on both its own bidding policy and those of other participants. Agents
therefore learn how to allocate their available capacity between energy and reserve through repeated
market interactions without observing competitors’ private information or policies.
A.4 M4: PEER-TO-PEERLOCALENERGYMARKET
Rooftop photovoltaic generation and behind-the-meter storage have enabled many consumers to
become prosumers that can both consume and supply electricity. When surplus energy is exported
directly to the grid, it is typically settled at an export price such as feed-in-tariff, which is below the
retail tariff paid for grid consumption. A peer-to-peer (P2P) local energy market allows neighboring
participants to trade their surplus and deficit locally at prices between these two outside options,
creating the possibility of mutual benefits for buyers and sellers. Unlike the day-ahead and real-time
markets in sections A.1 and A.2, which operate at the transmission level, the P2P market considered
here operates at the end-use level and facilitates local energy exchange among prosumers.
The P2P market uses 15-minute trading intervals. Before each auction, the net energy position
of every participant is determined from its local generation, consumption, and storage operation.
Hence, a participant knows the quantity it has available to buy or sell before submitting its bid, and
its strategic decisions are its battery power and the submitted price. A local market operator collects
the bids and offers, clears the auction, and settles the resulting transactions. The market does not
issue physical dispatch instructions: the participants’ net quantities are fixed before clearing, so the
auction determines which quantities are matched and at what price rather than how the underlying
devices are operated.
In our model, the P2P local energy market is implemented as a periodic double auction among a fixed
population ofN agent prosumers, each equipped with rooftop photovoltaic generation, an inelastic
local load, and a battery. In each trading interval, a participant appears on one side of the market
according to its net energy position: a surplus is offered for sale, whereas a deficit is submitted
as demand. The local market operator collects one price–quantity pair from each participant and
constructs aggregate supply and demand curves. The market clears at their intersection, with all
matched buyers and sellers settling at a common market clearing price. Any unmatched deficit is
supplied by the upstream grid at the retail tariff, while any unmatched surplus is exported to the grid
at the export price. This section presents the market clearing model in subsection A.4.1, the pricing
and settlement rules in subsection A.4.2, and the corresponding POSG in subsection A.4.3.
A.4.1 MARKET MODEL
Letτindex the 15-minute P2P trading intervals, with∆ p2p = 0.25 h. Before each auction, the local
generation, consumption, and battery operation of participantidetermine its net power position,
pnet i,τ =−p pv i,τ +p ch i,τ +d i,τ −p dis i,τ ,(56a)
and the corresponding quantities available for P2P trading are
qsell i,τ = ∆p2p max  −pnet i,τ ,0  , q buy i,τ = ∆p2p max  pnet i,τ ,0  .(56b)
Here,p pv i,τ andd i,τ denote photovoltaic generation and local demand, respectively.p dis i,τ andp ch i,τ
denote battery discharging and charging power, respectively. Only one ofq sell i,τ andq buy i,τ can be
positive. A participant with surplus energy is therefore a seller, while one with an energy deficit is a
buyer.
24

Preprint.
The battery is the only local device that carries a physical state between trading intervals. Its state
of charge evolves according to
soci,τ+1 = soci,τ + ∆p2p Ei

ηch i pch i,τ − pdis i,τ ηdis i
!
,(57)
whereE i is the battery energy capacity, andη ch i andη dis i are the charging and discharging loss
efficiencies. The feasible charging and discharging powers are bounded by
0≤p dis i,τ ≤min

¯pbat i , (soci,τ −soc i)E iηdis i ∆p2p  ,(58)
and
0≤p ch i,τ ≤min

¯pbat i , (soci −soc i,τ )E i ηch i ∆p2p

,(59)
where¯pbat i is the battery power rating and[soci, soci]is the admissible state-of-charge range. Charg-
ing and discharging are mutually exclusive within each trading interval.
Battery operation is chosen by the participant before the P2P auction. Hence,p net i,τ and the corre-
sponding trading quantity are fixed when the participant submits its bid, and within the auction only
the submitted price is a strategic bidding decision.
The seller and buyer sets in intervalτare
Sτ =

i:q sell i,τ >0 	 ,B τ = n i:q buy i,τ >0 o .(60)
Each participant submits one priceπ i,τ : an ask ifi∈ S τ and a bid ifi∈ Bτ . Submitted prices are
restricted by the outside options provided by the upstream grid,
πexp ≤π i,τ ≤π ret,(61)
whereπ ret is the retail tariff for grid imports andπ exp is the export price for grid injections, with
πexp < πret. The submitted quantity is fixed by the participant’s net position, soπ i,τ is the only
strategic variable in the auction.
The local market operator clears the market through a periodic double auction. Seller asks are sorted
in ascending order of price, while buyer bids are sorted in descending order of price, with ties broken
by participant index. Letσ s τ (j)denote the participant occupying positionjin the sorted seller order
andσ b τ (j)the participant occupying positionjin the sorted buyer order. The associated cumulative
quantities are
Qsell j,τ =
jX
ℓ=1
qsell σsτ (ℓ),τ , Q buy j,τ =
jX
ℓ=1
qbuy σbτ (ℓ),τ .(62)
The total quantities available on the two sides are
Qsell τ = X
i∈Sτ
qsell i,τ , Q buy τ = X
i∈Bτ
qbuy i,τ .(63)
The sorted submissions define the aggregate supply curveS τ (x)and aggregate demand curve
Dτ (x). The supply curve returns the ask price associated with thex-th unit of cumulative supply,
while the demand curve returns the bid price associated with thex-th unit of cumulative demand.
Both are step functions whose breakpoints are given by the cumulative quantities in equation (62).
LetX τ denote the union of the supply and demand breakpoints, together with zero. The cleared P2P
trading volume is
Q⋆ τ = max  x∈ Xτ :x≤min  Qsell τ , Qbuy τ  , Dτ (x)≥S τ (x) 	 .(64)
Thus, trading continues while the marginal buyer’s bid is no lower than the marginal seller’s ask. If
no bid meets an ask,Q ⋆ τ = 0.
Individual awards follow the sorted orders. For the seller occupying positionj,
qsell⋆ σsτ (j),τ = min h max  Q⋆ τ −Q sell j−1,τ ,0  , qsell σsτ (j),τ i ,(65)
25

Preprint.
withQ sell 0,τ = 0. Similarly, the award to the buyer occupying positionjis
qbuy⋆ σbτ (j),τ = min h max  Q⋆ τ −Q buy j−1,τ ,0  , qbuy σbτ (j),τ i ,(66)
withQ buy 0,τ = 0.
Equations (65) and (66) fill the most competitive submissions first: lower-priced sellers and higher-
priced buyers receive priority. SinceQ ⋆ τ coincides with a cumulative-quantity breakpoint on at least
one side of the market, all accepted participants on that side are either fully cleared or rejected. On
the opposite side, only the marginal participant may be partially cleared.
A.4.2 PRICING AND SETTLEMENT
LetS ⋆ τ andD ⋆ τ denote the marginal accepted ask and bid, respectively, and letS + τ andD + τ denote
the first rejected ask and bid beyond the cleared volumeQ ⋆ τ . A uniform clearing price must be high
enough for all accepted sellers and low enough for all accepted buyers, while remaining unattractive
to rejected submissions. This defines the feasible price interval
λτ = max

S⋆ τ , D+ τ  , ¯λτ = min  D⋆ τ , S+ τ  , λ loc τ = 1 2  λτ + ¯λτ  .(67)
The local market therefore publishes the midpoint of the admissible price interval. When an adjacent
accepted or rejected submission does not exist because one side of the market is exhausted, the
export priceπ exp and retail tariffπ ret provide the corresponding lower and upper price bounds.
Consequently,
πexp ≤λ loc τ ≤π ret.(68)
Thus, a matched seller receives no less than the grid export price and a matched buyer pays no
more than the retail tariff. If a marginal participant is only partially cleared, the admissible interval
collapses to that participant’s submitted price.
P2P awards are financially binding, while any unmatched quantity is settled with the upstream grid.
Define the residual export and import quantities as
qex i,τ =q sell i,τ −q sell⋆ i,τ , q im i,τ =q buy i,τ −q buy⋆ i,τ .(69)
The settlement of participantiis then
revenuei,τ =λ loc τ qsell⋆ i,τ +π expqex i,τ ,(70a)
costi,τ =λ loc τ qbuy⋆ i,τ +π retqim i,τ +c deg i ∆p2p  pch i,τ +p dis i,τ  ,(70b)
profiti,τ = revenuei,τ −cost i,τ .(70c)
Here,c deg i is the battery degradation cost in EUR/MWh of throughput. Photovoltaic generation is
assumed to have zero marginal cost, while local demand is inelastic. A participant with a net energy
deficit may therefore have negative profit, corresponding to a net electricity bill; maximizing profit
in this case is equivalent to minimizing that bill. Because all matched buyers and sellers settle at the
same local price, P2P payments are budget balanced within the local market, excluding transactions
with the upstream grid and any network charges not modeled here.
Remark on the P2P local market.The P2P market provides an intermediate trading opportunity
between the two grid settlement prices. Sellers can receive more than the export price, while buyers
can pay less than the retail tariff when mutually acceptable bids are matched. The market can also
increase the share of locally produced renewable energy consumed within the local network. It
therefore complements, rather than replaces, upstream electricity markets and grid transactions.
A.4.3 PARTIALLYOBSERVABLESTOCHASTICGAME
The P2P local energy market is formulated as a general-sum POSG,
Gp2p =⟨ I,S,{O i}i∈I,{A i}i∈I, P,{ri}i∈I, γ⟩,(71)
whereIis the fixed set ofN agent prosumers. One game step corresponds to one 15-minute P2P
trading intervalτ.
26

Preprint.
State.The state at intervalτis
sτ =

{xi,τ }i∈I, πexp, πret  ∈ S,(72)
where the local physical state of prosumeriis
xi,τ =

soci,τ , ppv i,τ , di,τ , pch i,τ , pdis i,τ  .(73)
These variables determine the participant’s net power positionpnet i,τ and therefore its available selling
or buying quantity through equation 56b. The export priceπ exp and retail tariffπ ret define the
outside settlement options with the upstream grid.
Observation.Each participant observes its own physical state and net trading position, together
with the public grid settlement prices. Its observation is
oi,τ =

soci,τ , pnet i,τ , qsell i,τ , qbuy i,τ , πexp, πret

= Ωi(sτ )∈ Oi.(74)
Thus, each participant knows whether it is a seller or buyer and the quantity it has available to trade
before submitting its price. It does not observe the contemporaneous bids, asks, or private local
states of other participants. The market is therefore partially observable from the perspective of
each individual prosumer.
Action.The trading quantity is fixed by the battery power before market clearing, so the strategic
action of participantiis its battery power together with its submitted price,
ai,τ =

pbat i,τ , πi,τ  , π i,τ ∈  πexp, πret ,(75)
wherep bat i,τ =p dis i,τ −p ch i,τ is the signed battery power within the feasible range (58)–(59). Ifqsell i,τ >0,
the submitted price is an ask; ifq buy i,τ >0, it is a bid. A participant with zero net position does not
actively participate in the auction. The joint action isa τ = (ai,τ )i∈I.
Market clearing and reward.Given the participants’ net positions and joint submitted prices, the
local market-clearing mechanism
zτ =C p2p(sτ , aτ )(76)
sorts the asks and bids and applies the double-auction clearing rules in Section A.4.1. The clear-
ing outcome contains the total traded volumeQ ⋆ τ , the uniform local clearing priceλ loc τ , and the
individual awardsq sell⋆ i,τ andq buy⋆ i,τ . Any unmatched quantity is settled with the upstream grid.
The stage reward of participantiis its realized profit,
ri,τ = profiti,τ = revenuei,τ −cost i,τ
=

λloc τ qsell⋆ i,τ +π expqex i,τ  −  λloc τ qbuy⋆ i,τ +π retqim i,τ +c deg i ∆p2p(pch i,τ +p dis i,τ )  (77)
whereprofit i,τ is defined by equation 70. For a seller, the reward reflects revenue from P2P sales
and any residual export to the grid. For a buyer, the reward reflects the cost of P2P purchases and
any residual import from the grid, together with battery degradation cost. A buyer may therefore
receive a negative reward corresponding to its electricity bill, so maximizing reward is equivalent to
minimizing that bill.
State transition.The battery state of charge provides the physical coupling between consecutive
trading intervals. Following equation 57,
soci,τ+1 = soci,τ + ∆p2p Ei

ηch i pch i,τ − pdis i,τ ηdis i
!
.(78)
Photovoltaic generation and local demand evolve according to their exogenous data processes, while
battery operation for the next period is determined before the next P2P auction. The next net position
and trading quantity are then obtained from equation 56b. The overall state transition is
sτ+1 ∼P(· |sτ , aτ ).(79)
Under the market design considered here, the submitted P2P price affects market matching and
settlement but does not directly alter the participant’s physical net position or battery dynamics.
27

Preprint.
Agent objective.Each participant uses a policyσ i(ai,τ |o i,τ )to determine its submitted price.
Over a horizon ofHtrading intervals, participantiseeks to maximize its expected discounted profit,
Ji(σi, σ−i) =E
" HX
τ=1
γτ−1 ri,τ
#
,(80)
whereσ −i denotes the joint policies of the other participants. Because the cleared volume, matching
outcome, and local clearing price depend on all submitted bids and asks, the return of each partici-
pant depends on both its own pricing policy and those of the other prosumers. Participants therefore
learn bidding strategies through repeated local-market interactions without observing competitors’
contemporaneous submissions or private states.
A.5 M5: LOCALFLEXIBILITYMARKET
Growing electrification and distributed generation can place distribution networks under increasing
operational stress, leading to feeder congestion and voltage violations. Reinforcing distribution
infrastructure can be costly and slow, particularly when the underlying constraint occurs only during
a limited number of periods. A local flexibility market provides an alternative means of managing
these constraints by allowing the distribution system operator (DSO) to procure temporary changes
in power injection or consumption from resources already connected to the affected network.
The market operates at the distribution level and clears once per delivery period. It addresses local
network constraints that are not represented in the transmission-level wholesale markets, while the
upstream energy price faced by each aggregator is treated as exogenous. The DSO is the sole buyer,
making the market a one-sided procurement auction. It specifies the locations and periods where
flexibility is required, and accepts offers that restore a feasible distribution-network operating point
at minimum procurement cost. The sellers are aggregators, with one aggregator at each bus, each
representing a portfolio of distributed energy resources.
Two features distinguish this market from the preceding settings. First, the traded product is a
deviation from a predefined baseline rather than energy itself. Second, settlement follows a pay-
as-bid rule: each accepted aggregator is paid its submitted offer price for the flexibility it provides,
rather than a common market-clearing price. The settlement therefore does not rely on dual-based
marginal prices. This section presents the market-clearing model in subsection A.5.1, the pricing
and settlement rule in subsection A.5.2, and the corresponding POSG in subsection A.5.3.
A.5.1 MARKET MODEL
We consider a radial distribution network withN bus buses supplied by a single substation, indexed
by0, whose voltage is fixed atv 0 = 1p.u. Letτindex the local flexibility trading intervals, with
duration∆ flex = 1hour. Before the flexibility market clears, each aggregator has a baseline oper-
ating position determined by local photovoltaic generation, demand, and planned battery charging.
With no flexibility activated, the baseline active-power injection at busnis
P base,inj n,τ = X
i:bus(i)=n

ppv i,τ −d i,τ −p plan i,τ

−d bg n,τ ,(81)
wherep pv i,τ is the photovoltaic output,d i,τ is the local demand of aggregatori,p plan i,τ is its planned
battery charging power, andd bg n,τ denotes background demand not controlled by any aggregator.
Under the radial-network approximation, the corresponding baseline line flows and squared voltages
are obtained from
P base l,τ =− X
m∈D(l)
P base,inj m,τ ,(82)
and
vbase n,τ 2 =v 2 0 + 2 X
m

Rn,mP base,inj m,τ +X n,mQbase,inj m,τ  ,(83)
whereD(l)denotes the set of buses downstream of linel. The quantitiesR n,m andX n,m are the
sums of resistance and reactance over the network path shared by busesnandm, respectively.
Reactive injections are determined from the active loads using a fixed power-factor assumption.
28

Preprint.
Before offers are submitted, the DSO publishes indicators of the local flexibility requirement. For
an undervoltage at busn, the indicator is
reqv n,τ = max
h
(vn +γ v)2 −  vbase n,τ 2 ,0 i
2Rn,n
,(84)
while the requirement associated with forward-flow congestion on linelis
reqth l,τ = max  P base l,τ −  1−γ th ¯Pl,0  .(85)
These quantities are published as market information for the aggregators; the market clearing itself
enforces the full network constraints below.
The traded product is upward flexibility, defined as an increase in net active power injection relative
to the baseline. Aggregatorisubmits one price–quantity offer(π i,τ ,¯qi,τ ), whereπ i,τ is its offer
price and¯qi,τ is the maximum flexibility quantity offered. Any quantityq i,τ ∈[0,¯q i,τ ]may be
accepted by the DSO. Unlike the stepwise offers used in the wholesale markets, each aggregator
submits a single price–quantity pair in each flexibility trading interval.
Upward flexibility can be delivered by reducing planned battery charging or, once planned charging
has been fully removed, by discharging the battery. The offered quantity must therefore satisfy
0≤¯qi,τ ≤q phys i,τ ,(86)
where
qphys i,τ =p plan i,τ + min

¯pdis i , ηdis i Ei (soci,τ −soc i) ∆flex  .(87)
Here,¯pdis i is the battery discharge-power limit,E i is its energy capacity,η dis i is its discharge effi-
ciency, andsoc i is the minimum admissible state of charge. Becauseq phys i,τ depends on the current
state of charge, the amount of flexibility available from an aggregator varies across trading intervals.
Given the submitted offers, the DSO selects flexibility awards by solving
min
{q,s,P inj,P,v} ∆flex
"X
i
πi,τ qi,τ + VOLL
X
n
sn,τ
#
,(88a)
subject to
P inj n,τ = X
i:bus(i)=n

ppv i,τ −d i,τ +q i,τ −p plan i,τ

−d bg n,τ +s n,τ ,(88b)
Pl,τ =−
X
m∈D(l)
P inj m,τ ,(88c)
v2 n,τ =v 2 0 + 2 X
m

Rn,mP inj m,τ +X n,mQinj m,τ  ,(88d)
(vn +γ v)2 ≤v 2 n,τ ≤(¯vn −γ v)2 , n̸= 0,(88e)
−

1−γ th ¯Pl ≤P l,τ ≤  1−γ th ¯Pl,(88f)
0≤q i,τ ≤¯qi,τ ,(88g)
0≤s n,τ ≤d bg n,τ + X
i:bus(i)=n
di,τ .(88h)
The objective (88a) minimizes the total procurement cost of local flexibility in each trading interval.
The first term represents the pay-as-bid cost of accepted flexibility offers, while the second penalizes
emergency load curtailment. The value of lost loadVOLLis set above the admissible flexibility
offer prices so that curtailment is used only when the available flexibility cannot restore a feasible
network operating point.
Constraint (88b) defines the active-power injection at each distribution bus. Without flexibility,
the baseline injection consists of photovoltaic generation minus local demand and planned battery
29

Preprint.
charging. An accepted flexibility quantityq i,τ increases the bus injection relative to this baseline,
either by reducing charging or by discharging the battery. Background demandd bg n,τ represents
demand not controlled by the aggregators, whiles n,τ denotes emergency load curtailment.
Constraint (88c) computes the active-power flow on each line as the total downstream withdrawal
under the radial-network structure. Here,D(l)denotes the set of buses downstream of linel. Con-
straint (88d) uses a linearized radial distribution power-flow model. The quantitiesR n,m andX n,m
represent the resistance and reactance shared by the paths from the substation to busesnandm,
respectively. The reactive injectionsQ inj m,τ are determined from the fixed power-factor assumptions
of the underlying loads and are not strategic decision variables.
Constraints (88e) and (88f) enforce the distribution-network operating limits. The parametersγ v
andγ th introduce safety margins by tightening the admissible voltage range and thermal line ratings
used during clearing. Constraint (88g) allows the DSO to accept any quantity between zero and
the quantity offered by aggregatori. The submitted quantity¯q i,τ must itself satisfy the physical
deliverability condition (87). Consequently, the clearing may partially accept an offer when the full
quantity is not required to restore network feasibility. Finally, constraint (88h) bounds emergency
curtailment by the total active demand at each bus. Curtailment acts as a feasibility backstop when
the submitted flexibility offers are insufficient to satisfy the tightened network constraints.
Since the network equations (88b)–(88d) are affine in the clearing variables under the linearized
radial power-flow model, the resulting flexibility-market clearing problem is a linear program.
A.5.2 PAYMENT AND SETTLEMENT
Settlement follows a pay-as-bid rule. Each accepted aggregator is paid its submitted offer price for
the quantity cleared by the DSO,
revenuei,τ = ∆flexπi,τ qi,τ ,profit i,τ = revenuei,τ −cost i,τ ,(89)
wherecost i,τ is the true delivery cost defined in Section A.5.3. Because settlement is pay-as-bid,
two aggregators providing flexibility at the same bus and in the same interval may receive different
payments if they submit different offer prices.
Although the market imposes no uniform clearing price, the curtailment backstop creates an implicit
upper value for flexibility. Emergency curtailment can relieve the same network constraints at a
marginal cost ofVOLL, so a flexibility offer is selected only when its network benefit justifies
its submitted cost relative to this alternative. This value is inherently locational because the effect
of an injection depends on where it enters the network. For a binding forward-flow constraint,
an additional MW of injection downstream of the constrained line reduces the line flow by one
MW under equation 88c, whereas an injection outside that downstream region does not relieve
that constraint. For a binding voltage constraint, the value of flexibility depends on the voltage
sensitivity of the participant’s bus, so injections at electrically more effective locations can support
higher accepted offer prices than injections with weaker voltage impact.
The flexibility product is defined as a deviation from the pre-market baseline. For aggregatori, this
baseline is determined from its photovoltaic generation, local demand, and planned battery charging,
pbase i,τ =p pv i,τ −d i,τ −p plan i,τ .(90)
An accepted flexibility awardq i,τ therefore requires the aggregator to increase its net injection by
exactly that amount relative to the baseline. In the benchmark, delivery is assumed to equal the
cleared award, so no payment is made for flexibility that is not delivered.
A.5.3 PARTIALLYOBSERVABLESTOCHASTICGAME
The local flexibility market is formulated as a general-sum partially observable stochastic game
(POSG),
Gflex =⟨I,S,{O i}i∈I,{A i}i∈I, P,{ri}i∈I, γ⟩,(91)
whereIdenotes the set of strategic aggregators. One game step corresponds to one local flexibility
trading intervalτ.
30

Preprint.
State.The state at intervalτis
sτ = (xsys τ ,{x i,τ }i∈I)∈ S,(92)
wherex sys τ describes the distribution-network operating condition before flexibility procurement. It
contains the baseline bus injections, line flows, voltages, and the flexibility-need indicators published
by the DSO,
xsys τ =  Pbase,inj τ ,P base τ ,v base τ ,req v τ ,req th τ  .(93)
The local physical state of aggregatoriis
xi,τ =

soci,τ , ppv i,τ , di,τ , pplan i,τ

,(94)
which, together with the planned charging in its action, determines its baseline injection and the
maximum physically deliverable flexibilityq phys i,τ through equation 87. Network parameters, battery
ratings, and other fixed technical parameters are omitted from the dynamic state.
Observation.Each aggregator observes its own operating state together with the public network
information released by the DSO. Its observation is
oi,τ =

soci,τ , ppv i,τ , di,τ ,req v τ ,req th τ  = Ωi(sτ )∈ Oi.(95)
Thus, each aggregator knows its own available flexibility and the locations and magnitudes of the
network needs published before bidding. It does not observe the private operating states, delivery
costs, or contemporaneous offers of other aggregators. The market is therefore partially observable
from the perspective of each participant.
Action.At each trading interval, aggregatorisubmits one price–quantity offer together with its
planned battery charging,
ai,τ =

πi,τ ,¯qi,τ , pplan i,τ

∈ Ai,(96)
subject to
crep ≤π i,τ ≤ π,0≤¯q i,τ ≤q phys i,τ ,0≤p plan i,τ ≤¯pch i,τ .(97)
The offer priceπ i,τ determines the payment requested per unit of flexibility,¯qi,τ specifies the maxi-
mum quantity the aggregator is willing to provide, andpplan i,τ enters the baseline injection (81). Here,
crep is the replacement cost of one delivered MWh, i.e., the energy price and the degradation cost
corrected for the round-trip efficiency, π <VOLLis the market price cap, and¯p ch i,τ is the charging
power the battery can absorb in the interval given its state of charge. The DSO may accept any
quantityq i,τ ∈[0,¯qi,τ ]. The joint action isa τ = (ai,τ )i∈I.
Market clearing and reward.Given the current state and joint offers, the DSO applies the
network-constrained clearing mechanism
zτ =C flex(sτ , aτ ),(98)
which solves equation 88. The clearing outcome contains the accepted flexibility quantitiesq i,τ ,
resulting bus injections, line flows and voltages, together with any emergency load curtailment.
Under the pay-as-bid settlement rule, the revenue of aggregatoriis
revenuei,τ = ∆flexπi,τ qi,τ .(99)
Its stage reward is the realized profit,
ri,τ = profiti,τ = revenuei,τ −C flex i (qi,τ ;x i,τ ),(100)
whereC flex i = ∆flex  λτ pch i,τ +c cyc i  pch i,τ +p dis i,τ  is the true cost of the interval, the energy bought
for charging at the exogenous priceλτ plus the degradation costccyc i per MWh of battery throughput,
withp ch andp dis given by the state transition below. This cost depends on the aggregator’s physical
operating state and the quantity actually delivered rather than on its submitted offer price.
31

Preprint.
State transition.An accepted flexibility award changes the battery operating trajectory and there-
fore affects the flexibility available in subsequent intervals. Let
qred i,τ = min  qi,τ , pplan i,τ  (101)
denote the part of the flexibility award delivered by reducing planned charging, and let
qdis i,τ = max  qi,τ −p plan i,τ ,0  (102)
denote the remaining part delivered through battery discharge. The realized battery charging and
discharging powers are therefore
pch i,τ =p plan i,τ −q red i,τ , p dis i,τ =q dis i,τ .(103)
The state of charge evolves according to
soci,τ+1 = soci,τ + ∆flex Ei

ηch i pch i,τ − pdis i,τ ηdis i
!
.(104)
Hence, providing flexibility in the current interval can reduce the battery energy available for future
flexibility provision. Photovoltaic generation, local demand, planned battery operation, and the
resulting network operating conditions evolve according to their exogenous data processes. The
overall state transition is
sτ+1 ∼P(· |sτ , aτ ).(105)
Agent objective.Each aggregator uses a policyσ i(ai,τ |o i,τ )to determine its flexibility offer.
Over a horizon ofHtrading intervals, aggregatoriseeks to maximize its expected discounted profit,
Ji(σi, σ−i) =E
" HX
τ=1
γτ−1 ri,τ
#
,(106)
whereσ −i denotes the joint policies of the other aggregators. Because the DSO jointly selects
offers according to their submitted prices, available quantities, locations, and effects on network
constraints, the return of each aggregator depends on both its own bidding policy and those of the
other participants. Aggregators therefore learn price–quantity offering strategies through repeated
market interactions without observing competitors’ private states, costs, or contemporaneous offers.
32

Preprint.
B COMPUTATIONPERFORMANCE
This section compares the throughput of the same environment code under three layouts: all on
the GPU; environment on the host CPU, policy on the GPU; all on the host CPU. With 64 parallel
environments, the throughput of all on the GPU is 2.3 to 22 times that of all on the host CPU and
2.3 to 33 times that of environment on the host CPU, policy on the GPU, in every one of the five
markets, and it does not change with the number of host threads allotted. Figure 7 compares the three
layouts in the market with the most participants, the M4 peer-to-peer local energy market with 1 200
households; Figure 8 covers all five markets, and Figure 9 open-source tools. All experiments run
under Python 3.11.15 with JAX and jaxlib 0.10.2, CUDA support added as the same-version plugin
rather than by changing either, and double precision and highest matmul precision enabled, on a
single shared workstation with three NVIDIA RTX 4500 Ada (24 GB) GPUs and an AMD Ryzen
Threadripper PRO 7985WX host (64 cores, 128 threads); each measurement point is run three times
and compilation time is excluded. Throughput is the number of environment steps advanced per
second, summed over the parallel environments, where one step covers the market clearing and one
forward pass of the policy, without gradient updates.
B.1 THREE LAYOUTS ON THE PEER-TO-PEER MARKET
In the peer-to-peer local energy market with 64 parallel environments, all on the GPU advances
27 929 environment steps per second, 22 times the throughput of all on the host CPU and 33 times
that of environment on the host CPU, policy on the GPU (Figure 7a). Raising the number of parallel
environments from 64 to 1 024 leaves the throughput unchanged, and so does the number of host
threads allotted (Figure 7b).
1 64 128 256 512 1024
Parallel environments
100
200
500
1,000
2,000
5,000
10,000
20,000
50,000Environment steps per second
33×
(a) By number of parallel environments
1 8 32 128
Host CPU threads allotted
100
200
500
1,000
2,000
5,000
10,000
20,000
50,000Environment steps per second
22×
(b) By host CPU threads allotted (64 parallel environments)
All on the GPU
Environment on the host CPU, policy on the GPU
All on the host CPU
Throughput ratio between layouts
Bootstrap 95% confidence interval
Figure 7: Throughput of the peer-to-peer local energy market environment (1 200 households, 96
periods per episode) under three layouts: (a) against the number of parallel environments; (b) against
the number of host CPU threads allotted, with 64 parallel environments. Each point is the mean of
three runs with a bootstrap 95% confidence interval; each dotted line joins two points and the number
beside it is their throughput ratio.
B.2 ACROSS THE FIVE MARKETS
All five markets show the speed and throughput advantage of PowerMarketJax: with 64 parallel
environments, all on the GPU gives 2.3 to 22 times the throughput of all on the host CPU and 2.3
to 33 times that of environment on the host CPU, policy on the GPU (Figure 8a); all on the GPU,
raising the number of parallel environments from 1 to 128 multiplies the throughput by 2.9 to 12
(Figure 8b).
B.3 AGAINST OPEN-SOURCE TOOLS
The clearing problem of the M2 real-time balancing market was also implemented in PyPSA (Brown
et al., 2018) and in cvxpy (Diamond & Boyd, 2016; Agrawal et al., 2018), each in its default usage
33

Preprint.
Day-
ahead
Real-time
balancing
Ancillary
services
Peer-
to-peer
Local
flexibility
1
10
100
1,000
10,000
100,000Environment steps per second
4.2× 7.4×
2.4× 3.9×
4.4× 4.4×
33× 22×
2.3× 2.3×
(a) Three layouts (64 parallel environments)
Day-
ahead
Real-time
balancing
Ancillary
services
Peer-
to-peer
Local
flexibility
1
10
100
1,000
10,000
100,000Environment steps per second
7.8×
12×
3.5×
2.9×
4.9×
(b) All on the GPU: 1 vs. 128 parallel environments
All on the GPU
Environment on the host CPU, policy on the GPU
All on the host CPU
All on the GPU, 1 environment
All on the GPU, 128 parallel environments
Figure 8: Throughput of the five market environments: (a) the three layouts with 64 parallel envi-
ronments, the number above each host bar being the ratio of all on the GPU to that layout; (b) all on
the GPU with 1 and with 128 parallel environments, the number above each pair being the ratio of
the two bars. Each bar is the mean of three runs.
(default formulation and solver), stepping one environment at a time. All on the GPU with 64 par-
allel environments gives 71 times the throughput of PyPSA and 8.8 times that of cvxpy (Figure 9).
Training PPO on the real-time balancing market for the same number of environment steps, Pow-
erMarketJax all on the GPU is 3.8 times faster than Stable-Baselines3 (Raffin et al., 2021) with its
default settings (wall-clock time, including gradient updates).
PyPSA
default, 1 env.
cvxpy
default, 1 env.
PowerMarketJax
GPU, 1 env.
PowerMarketJax
GPU, 64 env.
1
10
100
1,000Environment steps per second
2.2
18 16
158
71× slower
8.8× slower
Real-time balancing market: the same clearing problem in three implementations
PyPSA 1.3.0, default, 1 environment
cvxpy 1.9.3, default, 1 environment
PowerMarketJax, GPU, 1 environment
PowerMarketJax, GPU, 64 environments
Figure 9: Throughput of the real-time balancing market environment in three implementations:
PyPSA 1.3.0 and cvxpy 1.9.3 in their default usage, one environment at a time, and PowerMarketJax
all on the GPU with 1 and with 64 parallel environments. Each bar is the mean of three runs; the
label above each grey bar is how many times slower it is than PowerMarketJax with 64 parallel
environments.
B.4 IMPLEMENTATION VALIDATION
We validate the implementation in three ways: market clearing and settlement against a NumPy ref-
erence implementation; the dual prices of the JAX linear-program solver against HiGHS (Huangfu &
Hall, 2018), an independent solver; and the three-stage clearing of the M1 day-ahead market against
the exact solution of the same commitment problem, computed by HiGHS with the commitment
decisions kept binary.
Against a NumPy reference implementation.Each market has a separate NumPy reference im-
plementation that rewrites the same clearing and settlement rules with explicit matrices and loops.
We run both on every period of the evaluation days of each market under truthful offers and com-
pare each quantity (Table 1). In M3, load shedding and reserve shortfall are compared as totals per
period, because the optimum does not fix how they are split across buses and reserve products.
34

Preprint.
Table 1: Largest difference between the JAX implementation and the NumPy reference. The relative
difference divides the absolute difference by the largest absolute reference value.
Market Quantity Data Absolute difference Relative difference
M1
LMP
36 days×24 h,
case29gb
2.2×10 −8 $/MWh1.4×10 −10
Award1.3×10 −11 MW1.7×10 −15
Objective value9.3×10 −10 $4.9×10 −16
Settlement (profit)2.8×10 −9 $6.3×10 −16
M2
LMP 36 days×48
half-hours, case29gb
9.1×10 −8 $/MWh9.1×10 −12
Award1.6×10 −11 MW2.1×10 −15
Settlement (profit)1.5×10 −10 $1.7×10 −17
M3
LMP
36 days×48
half-hours, case29gb
7.3×10 −6 $/MWh7.3×10 −10
Reserve price1.2×10 −4 $/MWh4.7×10 −7
Award5.1×10 −9 MW6.5×10 −13
Load shed, total1.4×10 −11 MW7.7×10 −15
Reserve shortfall, total9.3×10 −12 MW4.0×10 −15
Objective value3.0×10 −4 $3.0×10 −11
Settlement (profit)4.7×10 −2 $5.5×10 −9
M4
Clearing price 64 episodes×96
quarter-hours, 1 200
households
6.1×10 −6 EUR/MWh1.8×10 −8
Traded volume1.4×10 −8 MWh1.0×10 −7
Award1.9×10 −8 MWh3.9×10 −6
Settlement (profit)1.8×10 −6 EUR1.0×10 −6
M5
Award
36 days×24 h, feeder
459 0
3.4×10 −9 MW1.3×10 −8
Load shed1.5×10 −9 MW5.0×10 −7
Objective value5.2×10 −7 CHF1.1×10 −9
Settlement (profit)5.2×10 −7 CHF1.5×10 −8
Dual prices against HiGHS.The prices of M1, M2 and M3 are duals of a linear program. On ev-
ery period of the same evaluation days, we solve the same linear program with HiGHS and compare
its prices with those of the JAX solver (Table 2). M4 and M5 set prices without a linear program.
Table 2: Largest difference between the JAX solver and HiGHS.
Market Test system Price Periods Price difference ($/MWh) Relative objective difference
M1 case29gb LMP 8642.6×10 −8 3.1×10 −16
M1 case73rts LMP 8644.1×10 −8 6.2×10 −8
M1 case813nem LMP 8643.5×10 −7 1.2×10 −7
M2 case29gb LMP 1 7281.1×10 −7 1.8×10 −12
M3 case29gb LMP 1 7287.3×10 −6 3.1×10 −11
M3 case29gb Reserve price 1 7282.1×10 −7 3.1×10 −11
Gap to the exact optimum.The M1 day-ahead clearing has binary commitment variables, and
no mixed-integer solver runs inside the compiled graph, so the market is cleared by a three-stage
procedure: a linear program with the on/off decisions relaxed to values between 0 and 1, rounding
of the relaxed commitment, and a re-solve of the economic dispatch with the commitment fixed.
On the 36 evaluation days of each of the three M1 test systems, under truthful offers, we solve the
same unit commitment problem exactly and offline with HiGHS (commitment variables 0 or 1) and
compare its production cost with that of the three-stage procedure.
Over the 36 evaluation days, the median excess production cost of the three-stage procedure over the
exact optimum is 2.04% on case29gb, 0 on case73rts and 1.10% on case813nem, and the maximum
is 3.78%, 1.79% and 1.95% (Figure 10). On 23 of the 36 evaluation days of case73rts, the three-stage
commitment is the same as the exact optimum and the gap is 0.
35

Preprint.
1 12 24 36
Evaluation day
0
2
4
6
8
10
Cost above the exact
optimum (%)
case29gb
1 12 24 36
Evaluation day
case73rts
1 12 24 36
Evaluation day
case813nem
One evaluation day Median over the 36 days
Figure 10: Production cost of the three-stage clearing above the exact optimum on the evaluation
days of the three M1 test systems, under truthful offers. Each point is one evaluation day, in date
order; the dashed line is the median.
36

Preprint.
C QUICKSTART ANDAPI
This section is a walk-through of how to install PowerMarketJax, run a minimal rollout, read the
interface contract that the five markets share, construct each of them, find where an experimental
configuration is written down, and reproduce a result from the command line. Listing C.2 is a
complete runnable program, Listing C.3 a rollout function that takes an environment built by any
of the five constructors, Listing C.5 is abridged from a released source file, and the bash blocks in
Sections C.1 and C.6 cover installation and experiment script usage. The market models themselves,
including the observation, action, clearing and settlement of each market, are in Appendix A; this
section covers only the software interface to them.
C.1 INSTALLATION
PowerMarketJax requires Python 3.10–3.12 and has no build step. The base install ships a CPU-
only JAX; CUDA 12 support is opt-in via thecudaextra, which adds the CUDA plugin alongside
the already resolvedjaxlibat the same version and therefore does not move the JAX version the
suite is verified on. GPU support follows JAX’s own platform support: the CUDA build is available
on Linux only, so on Windows the package runs on the CPU natively and on the GPU through
WSL2. All reported results and test runs were obtained on Linux. The learning stack ofrlaxand
distraxused by the P2P trading experiment script lives behindrl, and the figure scripts behind
figs. Nothing underpowermarketjax/importsmatplotlib,rlaxordistrax, so the
five markets and both learners are available on adevinstall alone.
Listing C.1: PowerMarketJax Installation commands
git clone https://github.com/powermarketjax/PowerMarketJax
conda create -y -n powermarketjax python=3.11 && conda activate
powermarketjax
pip install -e ".[dev]"# CPU JAX, the five markets,
both learners
pip install -e ".[dev,cuda,rl,figs]"# Linux + CUDA 12, plus
scripts and figures
python -c "import powermarketjax, jax; print(powermarketjax.
__version__, jax.__version__, jax.devices())"
C.2 MINIMAL ROLLOUT
Listing C.2 opens the day-ahead wholesale market on the 29-bus GB case, resets it, and runs a
three-step rollout underjax.lax.scanwith every agent bidding at twice its cost. One step is one
market day, so the rollout clears three consecutive days of a multi-period security-constrained unit
commitment; every transition, the clearing included, stays insidejit.
Listing C.2: Minimal rollout oncase29gb(day-ahead wholesale)
importjax, jax.numpyasjnp
jax.config.update("jax_enable_x64", True)# M1/M2/M3/M5 refuse to
build without it
frompowermarketjax.caseimportload_case
frompowermarketjax.envs.day_aheadimportmake_env, load_commitment,
load_gb_demand
frompowermarketjax.utils.jax_utilsimportscan_rollout
env, spec = make_env(load_case("29gb"),
load_commitment(n_periods=24), load_gb_demand(),
kind="markup", markup_max=2.0,
cap_scale=0.60, ramp_scale=1.00)
params = env.make_params(episode_len=3)
37

Preprint.
obs, state = env.reset(jax.random.PRNGKey(0), params)
actions = jnp.full((3, spec["n_agents"]), 2.0)# (n_steps,
n_agents)
final_state, obs_traj, reward_traj, cost_traj, done_traj, info_traj =
jax.jit(lambdak, s: scan_rollout(env, k, s, params, actions)
)(jax.random.PRNGKey(1), state)
At this configuration the market has 66 agents, one per thermal unit:obs trajis
(3, 66, 112),reward trajis(3, 66)andcost trajis(3, 66, 2), and
info traj["converged"]reports per step whether the clearing met its tolerance.
scan rolloutdrivesstep auto reset, so episodes restart at their boundary without a Python
conditional and the trajectory has a fixed length.
The scenario parameters have no defaults.cap scaleandramp scalein Listing C.2 are re-
quired: omitting either raisesValueError. The two scale the line ratings and the ramp limits the
case ships with, socap scale1.00 means every line keeps the capacity written in the case file and
in that network no line ever reaches its limit. With no line at its limit there is no congestion, and
with no congestion every bus clears at the same price.
Listing C.3 is the same contract on any of the five markets, vectorised over a batch of environments.
unpack envaccepts whichever shape a market’s constructor returns (Section C.4) and yields the
same four objects, so the rollout below is market-agnostic.
Listing C.3: One rollout function for five markets:vmapover environments insidescanover time
importmath, jax, jax.numpyasjnp, numpyasnp
fromfunctoolsimportpartial
frompowermarketjax.learningimportunpack_env
frompowermarketjax.resources.batteryimportmake_battery_bundle
frompowermarketjax.envs.p2pimport(make_p2p_env, make_p2p_params,
load_fluvius_households)
jax.config.update("jax_enable_x64", True)# M1/M2/M3/M5 refuse to
build without it
# ‘built‘ is whatever a market’s constructor returned: the (env, spec)
pair for M1/M2, or the (reset, step, step_auto_reset, spec)
tuple for M3-M5. Here it is M4, the P2P trading market, on 12
metered houses.
N, DT, ETA = 12, 0.25, math.sqrt(0.85)
series = load_fluvius_households(n_households=N)
battery = make_battery_bundle(n_devices=N, dt_hours=DT,
capacity_mwh=[0.01] * N,
power_mw=[0.005] * N,
eta_charge=ETA, eta_discharge=ETA,
soc_min=0.15, soc_max=1.0,
initial_soc=0.5,
cycle_cost_per_mwh=0.0)
params = make_p2p_params(p_pv=series.injection, load=series.offtake,
battery=battery,
kappa=np.full(N, 13.88, np.float32),
learner_mask=np.ones(N,bool),
episode_len=96)
built = make_p2p_env(N, 73.0, 333.4, DT)# n_agents, export/retail,
dt
reset, step, step_auto_reset, spec = unpack_env(built)
# unpack_env takes either shape and gives the four names below.
defrollout(key, params, policy, n_envs, n_steps):
k_reset, k_roll = jax.random.split(key)
obs, state = jax.vmap(reset, in_axes=(0, None))(
jax.random.split(k_reset, n_envs), params)
defone_step(carry, k):
38

Preprint.
obs, state = carry
action = policy(obs)# (n_envs, *
action_shape)
obs, state, reward, costs, done, info = jax.vmap(
step_auto_reset, in_axes=(0, 0, 0, None))(
jax.random.split(k, n_envs), state, action, params)
return(obs, state), (reward, costs, done)
returnjax.lax.scan(one_step, (obs, state),
jax.random.split(k_roll, n_steps))
# The action shape comes from the market, not from the learner.
zero =lambdaobs: jnp.zeros((obs.shape[0], *spec["action_shape"]),
jnp.float32)
(obs, state), (reward, costs, done) = jax.jit(
partial(rollout, policy=zero, n_envs=8, n_steps=6)
)(jax.random.PRNGKey(0), params)
The returnedrewardhas shape(n steps, n envs, N)andcostshas shape(n steps,
n envs, N, C): time, parallel environments and market participants are three separate axes, and
the second and third are the two the accelerator exploits.paramsis closed over as a broadcast
argument, so a sweep over anything carried there is a loop over calls and not a recompilation.
C.3 THE ENVIRONMENT INTERFACE
Signatures.Every market exposes the same three pure functions:
Listing C.4: Market environment signatures
obs, state = reset(key, params)
obs, state, reward, costs, done, info = step(key, state, action,
params)
obs, state, reward, costs, done, info = step_auto_reset(key, state,
action, params)
WithNagents andCconstraint channels,obsis(N, d),rewardis(N,),costsis(N, C)and
doneis a scalar boolean. The agent index is one array axis: observations, actions, rewards and
costs are aligned on it, andNis fixed at compile time.
Reward and constraint costs.The reward of an agent is the profit it earns in that step, settled on the
quantities and prices produced by the market’s own clearing (Appendix A). Violations of physical
or market constraints, such as shed load or an unmet reserve requirement, are returned separately
incosts, one column per name inspec["cost names"], and are never subtracted from the
reward. A user decides how to handle them, for example by adding a penalty to the reward or by
using a constrained learning method.
Episode boundary.spec["termination"]tells a learner what the end of an episode means. In
four markets it is"truncation": the episode is cut off in time, the market would continue, and
the value of the last state should be bootstrapped. In the P2P market it is"terminal": the last
reward already pays each household for the energy left in its battery, so bootstrapping would count
that energy twice.
C.4 CONSTRUCTING THE FIVE MARKETS
Each market has its own constructor, since the scenarios differ: the wholesale markets take a
network case, a precomputed day-ahead commitment and schedule, and a demand series; the
ancillary market adds the reserve products; the P2P trading market takes a population size and
the export and retail tariffs; the local flexibility market takes a feeder and the placement of
the aggregators. The ancillary, P2P and local flexibility constructors return(reset, step,
step auto reset, spec), and the day-ahead and real-time constructors return(env,
spec);powermarketjax.learning.unpack envconverts either to the first form, as in
39

Preprint.
Listing C.3. Anything that changes the size of the clearing problem, such as the network or the
placement of agents, is fixed when the environment is built, and changing it requires recompiling;
anything that varies within a market, such as the demand series or the episode length, is passed in
paramson every call.
C.5 SCENARIO AND LEARNER CONFIGURATION
There is no configuration file format: an experimental configuration is Python. The learner con-
figuration istools/benchmark/hyperparams.py, abridged in Listing C.5. The scenario
parameters are module-level constants of each market’s experiment script, each also exposed as a
command-line flag.
Listing C.5: The shared learner configuration
N_ENVS, MINIBATCHES = 64, 32
HORIZON = {"01": 4, "02": 48, "03": 48}# steps per update, per
market
for_m, _hinHORIZON.items():# the batch must divide into
minibatches
assert(N_ENVS * _h) % MINIBATCHES == 0
SHARED = IPPOConfig(
n_envs=N_ENVS,
horizon=HORIZON["02"],# ours, per market via shared_for()
epochs=10,# update_epochs
minibatches=MINIBATCHES,# num_minibatches
lr=3e-4,# learning_rate (no annealing here)
clip_eps=0.2,# clip_coef
gamma=0.99,# gamma
gae_lambda=0.95,# gae_lambda
vf_coef=0.5,# vf_coef
ent_coef=0.0,# ent_coef
max_grad_norm=0.5,# max_grad_norm
hidden=(64, 64),# Agent: two tanh layers of 64
weight_decay=0.0,# zero reproduces optax.adam exactly
init_scale=1.0,
)
defshared_for(market):
returndataclasses.replace(SHARED, horizon=HORIZON[market])
C.6 COMMAND-LINE USAGE
Each market has one experiment script for its learning runs. The non-learning base-
lines are run by a separate script for the day-ahead, real-time and ancillary markets
(tools/benchmark/run eval 0*.py), by the learning script itself for the P2P trading mar-
ket (--arm truthful) and for the local flexibility market, where they run alongside the learn-
ers. The learning script takes the learner (--algo ippo|sac), parameter sharing or not
(--per-agent-paramsfor one network per agent), the seed, the iteration count, the scenario
parameters and an output directory. It trains on the training days only and then evaluates the mean
action of the policy on the held-out days, so the reported number excludes exploration noise.
Listing C.6: Command line for RL training
# One-year inputs for M1-M3 (2023-07-10 to 2024-07-08), built once.
python tools/commitment/precommit.py --mode relax --start-day 5 --days
365 --cap-scale 0.6 --ramp-scale 1.0 --out commit_y1.npz
python tools/commitment/da_position.py --case29gb --fixture commit_y1
.npz --out position_y1.npz
# M1 day-ahead: parameter sharing, then one network per agent.
40

Preprint.
python tools/benchmark/run_rl_01.py --fixture commit_y1.npz --algo
ippo --seed 0 --iterations 400 --out-dir runs/m1-ippo-ps
python tools/benchmark/run_rl_01.py --fixture commit_y1.npz --algo
ippo --seed 0 --iterations 400 --per-agent-params --out-dir runs/
m1-ippo-nops
# M2 real-time and M3 ancillary settle against the day-ahead position.
python tools/benchmark/run_rl_02.py --position position_y1.npz --seed
0 --out-dir runs/m2-ippo-ps
python tools/benchmark/run_rl_03.py --position position_y1.npz --seed
0 --out-dir runs/m3-ippo-ps
# M4 P2P, 1200 households.
python tools/benchmark/run_rl_04.py --agents 1200 --seed 0 --out-dir
runs/m4-ippo-ps
# M5 local flexibility.
PYTHONPATH=tools/flex_experiment python -m concentration_baseline --
algo ippo --seeds 3 --out runs/m5-ippo-ps
# Non-learning baselines for M1 on the held-out days.
python tools/benchmark/run_eval_01.py --fixture commit_y1.npz --days
eval--out-dir results/m1-baselines
C.7 CASES AND DATA
powermarketjax.case.list cases()returns the 18 built-in network cases, 10 transmis-
sion and 8 distribution, sorted by bus count and with aliases removed;load caseaccepts a canon-
ical identifier or an alias. The demand, generation, price and smart-meter series are carried in the
repository as parquet files, so every listing above runs on a fresh checkout with no separate download
step.
C.8 CLEARING AND LEARNING IN A SINGLE COMPUTATION GRAPH
A training iteration has two parts, a rollout and an update. In the rollout,Nenvironments advance
together forTsteps. In each step the participants submit offers, the market clears, the awards are
settled, and the next observation is constructed; the policy maps the observation to the action at every
step, and the observation, action, reward and constraint cost of one step form one experience. The
update takes gradient steps on theN×Texperiences of the rollout, split by epoch and minibatch.
The whole iteration, including the clearing problem of every step, is compiled as one function on
the GPU: the host makes one call and receives the training metrics, and every clearing, every policy
forward pass and every gradient step in between runs on the GPU in sequence. Figure 11 shows the
data flow of one iteration, and Listing C.7 writes the same iteration as loops, with the JAX primitive
that implements each loop in the comment above it. The values ofNandTfor each market are in
Table 4, the epochs and minibatches in Table 3, andn, the number of agents, in Appendix A.
The loop over theNenvironments isvmap(step). The functionstepadvances one environment
by one step and is written for one environment only;vmapreturns the function that advancesN
environments at once, whose input and output gain one axis of lengthN. The clearing, settlement
and observation of theNenvironments are one batched computation overNsets of data, notN
calls one after another. The forward pass of the policy goes throughvmapin the same way, so the
actions are produced inside the same function and passed directly tostep, and the observations
never reach the host.
41

Preprint.
One training iteration, compiled as a single function @jax.jit
Rollout: N environments in parallel, T steps each
one step of one environment
Submit
offers
Clear
the market
Settle profit
and cost
Observe the
next state
N environments
@jax.vmap
Policy: observation to one action
for each of the n agents
next step;
repeated T times
@lax.scan
N × T experiences
Update the policy on
the N × T experiences

@lax.scan
policy parameters
for the next iteration
Figure 11: One training iteration of IPPO, compiled as a single function. Rollout:Nenvironments
advance in parallel forTsteps; in each step thenagents submit offers, the market clears, the awards
are settled and the next observation is constructed, and the policy maps the observation to the next
action inside the same function. Update: the policy is updated on theN×Texperiences, with a
second scan over epochs and minibatches (Table 3). The values ofNandTfor each market are in
Table 4.
Listing C.7: One training iteration as loops, with the primitive that implements each loop
# iteration = jit(iteration): the whole body below is one compiled
# function on the GPU, called once per training iteration
iteration(params, states, observations):
# rollout
# scan(one_step, carry, length=T): carry = (states, observations);
# returns the final carry and the T records stacked
for t = 1 .. T:
# policy_N = vmap(policy), step_N = vmap(step):
# each takes N inputs and returns N outputs at once
for each of the N environments:
for each of the n agents: action <- policy(observation)
# step(state, actions), one environment
offers <- submit(actions)
awards, prices <- clear(offers)
reward, cost <- settle(awards, prices)
observation <- observe(the state after clearing)
if the episode ended: reset this environment in place
# one record per step, holding the N environments
record (observations, actions, rewards, costs)
# N x T experiences, each with n agents
experiences <- the T records
# update
# scan(gradient_step, ...): the passes over the experiences,
# by epoch and minibatch
for each pass over the experiences:
params <- optimiser step on the gradient of the loss
return params, states, observations, training metrics
The loop over theTsteps islax.scan(one step, carry, length=T). It takes the loop
bodyone step, the initial carry, which is theNstates and theNobservations, and the number
of stepsT; runs the bodyTtimes, feeding the carry returned by one run into the next; stacks the
record of each run into an array of lengthT; and returns the final carry together with this array. The
horizonTis fixed, and an environment whose episode ends before stepTis reset in place inside the
body, so the input and output of the body have the same shape at every step, which is the condition
under whichlax.scanapplies. The gradient steps of the update are a secondlax.scan. None
42

Preprint.
of these loops runs on the host, and the host does not see the boundary between two consecutive
steps.
The outer function isjit(iteration): the rollout followed by the update, compiled for the
GPU at the first call and called once per iteration. The host passes in the parameters, the environment
states and the observations, and receives the updated parameters, states, observations and training
metrics; no intermediate result returns to the host, and the only loop left on the host is the loop over
iterations. The iteration of SAC has the same form: the rollout is the same, and the update first
places the experiences of the rollout into a replay buffer of fixed size, which also lives inside this
function and is carried from one iteration to the next, then samples from it for the gradient steps,
which are again alax.scan.
43

Preprint.
D TRAININGSETUP ANDHYPERPARAMETERS
The results of Section 5 and Appendix E share four learners, one set of hyperparameters and one
evaluation protocol; where a market departs from them, its subsection of Appendix E gives the
difference. Appendix C.5 shows where these values are set in the code.
D.1 FOUR LEARNERS
Each market is run with four learners: IPPO-PS, IPPO-NoPS, SAC-PS and SAC-NoPS. All four are
independent learners: every agent sees only its own observation and optimises only its own profit,
with no centralised value network. PS and NoPS stand for parameter sharing and no parameter
sharing. Under PS all agents share one set of networks and pool their samples for training; under
NoPS each agent has its own set and trains only on its own samples. For IPPO the set is one actor
and one value network that share twotanhlayers, and the log standard deviation of the actor does
not depend on the observation; for SAC it is one stochastic actor and a pair of Q-networks with their
target networks, with an automatically tuned temperature.
D.2 HYPERPARAMETERS
The hyperparameters build on the defaults of the continuous-action PPO and SAC implementations
in CleanRL; the five markets use one set, listed in Table 3, without tuning for each market. The profit
of one step in M1 is of the order of105 to10 6 dollars and the Q regression of SAC is sensitive to this
magnitude, so SAC divides the reward by a constant before the Q regression: the standard deviation
of the rewards under truthful offers, computed once before training. SAC runs the gradient steps of
an iteration as one block after the rollout. In all four learners each component of the observation is
normalised with constants fixed before training.
Table 3: Hyperparameters of the two IPPO and the two SAC learners, shared by the five markets.
Hyperparameter IPPO SAC
Optimiser Adam Adam
Learning rate3×10 −4, constant actor3×10 −4, Q-networks and
temperature10 −3
Discount factorγ0.99 0.99
Hidden layers two layers of 64 units,tanhtwo layers of 256 units, ReLU
GAE parameterλ0.95 —
Clipping range 0.2 —
Update epochs per iteration 10 —
Minibatches per epoch 32 —
Value loss coefficient 0.5 —
Entropy coefficient 0 —
Maximum gradient norm 0.5 —
Initialisation scale of the actor
output layer
1.0 —
Replay buffer — 32 768 environment steps
Batch size — 256 environment steps, each carrying
the transitions of all agents
Gradient steps per environment
step
— 1
Random-action steps before
training
— 0
Actor update interval — every gradient step
Target smoothing coefficientτ— 0.005
Temperature — initial value 0.2, tuned automatically
Target entropy — minus the action dimension
Range of the log standard
deviation
—[−5,2]
The two SAC learners of M4 and the two IPPO learners of M5 differ from Table 3 in the settings
given in Sections E.4.2 and E.5.2.
44

Preprint.
D.3 TRAINING SCALE
Table 4 gives the training scale of each market.
Table 4: Training scale.
Market Seeds
per
learner
Iterations Parallel environments and steps per
iteration
Environment
steps per
iteration
M1 day-ahead
wholesale
3 400 64 environments, 4 steps each 256
M2 real-time
balancing
3 200 64 environments, 48 steps each 3 072
M3 ancillary
services
3 200 64 environments, 48 steps each 3 072
M4 peer-to-peer
local energy
3 400 64 environments, 96 steps each 6 144
M5 local
flexibility
3 to 10 early
stoppinga, at
most 300
64 environments, 24 steps each 1 536
a M5 evaluates a checkpoint on the validation days every 10 iterations and stops early once the mean validation return of the last 5 checkpoints
exceeds that of the 5 checkpoints before them by 0 to 5%.
D.4 EVALUATION PROTOCOL
M1 to M4 evaluate the policy at the last iteration. In M1 to M3, evaluation takes the mean action
of the policy and runs day by day on the 36 evaluation days of the one-year window of case29gb,
2023-07-10 to 2024-07-08 (the dates of the other two test systems are in Table 5). In M4, evaluation
also takes the mean action and runs on 1 024 held-out episodes (Table 7). In M5, the checkpoint with
the highest validation return is evaluated on the 36 test days with sampled actions (Section E.5.2).
The training return is the return under sampled actions and includes exploration noise.
The untrained network is the network of the same parameter layout (PS or NoPS) at iteration 0,
evaluated in the same way.
Truthful offers are the reference policy in which every agent offers at its true cost: in M1 to M3
every unit takes the markupα i = 1, with a reserve offer of 0 in M3; in M4 the batteries are kept
still, sellers ask the export price and buyers bid the retail tariff; and in M5 every aggregator offers
its full deliverable quantity at the replacement cost and plans no charging.
45

Preprint.
E ADDITIONALMARKETRESULTS
E.1 M1: DAY-AHEADWHOLESALEMARKET
This section first presents detailed data, training curves and evaluation results of the three test sys-
tems, and then elaborates the finding in Section 5.1 with the supply curves, the offer distribution and
the joint sampling probability on the British test system.
E.1.1 MARKET SETTING
Each unitioffers a price–quantity curve with a single segment (K= 1in Section A.1.1). Its offer
price isα imi, wherem i is its segment cost (the mean of its true marginal cost over its output range)
andα i ∈[1,¯α]is its markup. Atα i = 1the offer is truthful, and¯α >1is the markup cap. A
markup above one represents economic withholding: the unit offers its capacity at a price above its
cost.
We consider three test systems. As shown in Table 5, each test system uses one year of data, of
which 36 days are used for evaluation and the rest for training. On each test system, three selected
days are taken from the 36 evaluation days: the days at the 10th, 50th and 90th percentiles of total
daily demand, referred to below as the low-load day, the mid-load day and the high-load day.
Table 5: Data of the three test systems.
Test system Grid Demand data Time span
Training /
evaluation
days
Markup
cap¯α
case29gb
A reduced 29-bus
model of the GB
transmission networka
(network diagramb),
66 units
GB transmission
system demand
(NESO)c, day-ahead
forecast from Elexond
2023-07-10
to
2024-07-08
329 / 36 2
case73rts The RTS-GMLC test systeme, 73 units Load, wind, solar and hydro of RTS-GMLCf
2020-01-01
to
2020-12-31
330 / 36 1.4
case813nem
An open grid model
of the Australian
National Electricity
Marketg, 151 units
Operational demand
and day-ahead
forecast of the four
mainland regions
from the Australian
Energy Market
Operator (AEMO)h
2025-02-01
to
2026-01-31
329 / 36 2
a https://webhomes.maths.ed.ac.uk/OptEnergy/NetworkData/reducedGB/;
b https://webhomes.maths.ed.ac.uk/OptEnergy/NetworkData/reducedGB/GBreducednetwork.pdf;
c https://www.neso.energy/data-portal/historic-demand-data; d https://bmrs.elexon.co.uk/;
e https://github.com/GridMod/RTS-GMLC;
f https://github.com/GridMod/RTS-GMLC/tree/master/RTS_Data/timeseries_data_files;
g https://github.com/akxen/egrimod-nem-dataset;
h https://visualisations.aemo.com.au/aemo/nemweb/index.html.
In the British test system case29gb, generation lies mostly in the north and load mostly in the south,
and power flows from north to south: the north has 63% of the total capacity but only 43% of the
load. The three example days are 2024-06-23, 2024-03-16 and 2024-01-23. Under truthful offers, 2,
3 and 5 lines are congested on these days, all on central and southern corridors (Figure 12). Of the
66 units, 14 are nuclear, 23 coal and 29 gas. In order of segment cost, all 14 nuclear units are among
the 16 cheapest units, and their total capacity is only 4.359 GW. These 16 units have a total capacity
of 19.2 GW, while hourly system demand over one year ranges from 17.2 to 47.4 GW and is above
19.2 GW in almost every hour. The nuclear units therefore sit near the left of the supply curve with
demand almost always to their right, which means a unilateral markup by one nuclear unit does not
move the price, and only a joint markup raises it.
In the RTS-GMLC test system, case73rts, wind, solar and hydro (referred to below as renewables)
do not submit offers, and the demand cleared by the market is the net demand (total load minus
46

Preprint.
Generating units by fuel and capacity Load and congested corridors
0 20 40 60 80
Cumulative capacity (GW)
0
25
50
75
100
125
150
175Segment cost ($/MWh)
Units sorted by segment cost
case29gb: 29 buses, 99 lines on 50 corridors, 66 units
Nuclear
Coal
Gas
Unit, 500 MW
Unit, 5,000 MW
Bus
Corridor, 500 MW
Corridor, 5,000 MW
Bus load, annual mean 2,000 MW
Congested on all 3 days
Congested on the mid- and high-load days
Congested on the high-load day
Range of hourly system demand, one year
Figure 12: The test system case29gb. Left: the 66 units at their buses, coloured by fuel and sized
by maximum output; corridor width scales with capacity. Middle: annual mean bus load and the
corridors congested under truthful offers on the three example days. Right: the supply curve ordered
by segment cost, against the range of hourly system demand over one year. Generation sits mostly
in the north and load mostly in the south, so the congested corridors are central and southern. All 14
nuclear units, 4 359 MW in total, are among the 16 cheapest units, which sum to 19.2 GW; hourly
demand ranges from 17.2 to 47.4 GW and exceeds 19.2 GW in almost every hour. The nuclear units
therefore sit near the left of the supply curve with demand almost always to their right: a unilateral
markup does not move the price, while a joint markup lifts the whole curve and the price with it.
renewable output). The three example days are 2020-02-24, 2020-03-24 and 2020-07-16. Under
truthful offers, 0, 2 and 7 lines are congested on these days (Figure 13).
Regarding the Australian test system, case813nem, the three example days are 2025-09-20, 2025-12-
10 and 2025-06-24. Under truthful offers, 3, 4 and 4 lines are congested on these days (Figure 14).
On all three test systems the market clears the demand that actually occurs on the day, while the units
observe the day-ahead forecast before they submit offers (Figure 15). On case73rts, net demand has a
floor of 2 500 MW, and it sits at that floor in more than half of the hours of the year. On case813nem,
demand has a floor of 11 500 MW, reached in only a few hours.
E.1.2 AGENT TRAINING
The training setup of the four learners is that of Appendix D. On the British test system, the training
return of IPPO-NoPS, SAC-PS and SAC-NoPS ends close to its highest level (top row of Figure 16).
IPPO-PS stays below the other three and is the only one whose return rises and then falls; the markup
it samples also rises to about 1.7 and then returns to about 1.5 (Figure 3a).
On the other two test systems only IPPO-PS and IPPO-NoPS are trained (bottom row of Figure 16).
The training return of both learners falls from its starting level. The fall comes from competition
among the units: at the start of training every unit offers near the middle of its markup range, which
amounts to a joint markup; during training the units that set the price learn to offer closer to cost,
because a unit that stays high alone loses its output to its rivals, so the price falls while production
cost does not, and profit falls with it.
47

Preprint.
Generating units by fuel and capacity Load and congested lines
0 2 4 6 8
Cumulative capacity (GW)
0
20
40
60
80
100
120Segment cost ($/MWh)
Units sorted by segment cost
case73rts: 73 buses, 120 lines, 73 units
Nuclear
Coal
Gas
Oil
Unit, 100 MW
Unit, 1,000 MW
Bus
Line, 74 MW
Line, 306 MW
Bus load, annual mean 500 MW
Congested on the mid- and high-load days
Congested on the high-load day
Range of hourly net demand, one year
Figure 13: The test system case73rts, drawn as Figure 12: the three-area RTS-GMLC system with
73 units. Left: units by fuel and maximum output. Middle: annual mean bus load and the lines
congested under truthful offers on the three example days. Right: the supply curve ordered by
segment cost against the range of hourly net demand over one year. Gas units make up most of the
supply curve; no line is congested on the low-load day and seven are on the high-load day.
E.1.3 DISCUSSION OF RESULTS
On each test system, the policies learned by IPPO-PS and IPPO-NoPS are compared with truthful
offers on the 36 evaluation days, each learner taken as the mean of three seeds.
As shown in Figure 17, across all three test systems, the mean LMP under the learned policies (load-
weighted over all periods and buses of the day) is higher than under truthful offers on every one of
the 36 evaluation days (production cost barely changes) and the profit of all units rises accordingly.
Averaged over the 36 days, the mean LMP under the policies learned by IPPO-PS and IPPO-NoPS
is 1.50 and 1.56 times, respectively, its value under truthful offers on case29gb, 1.10 and 1.07 times
on case73rts, and 1.23 and 1.29 times on case813nem. For both learners, the total production cost
over the 36 days differs from that under truthful offers by less than 1%. The increase in mean LMP
is smallest on case73rts, where the mean markups of IPPO-PS and IPPO-NoPS are only 1.19 and
1.21, respectively.
E.1.4 DETAILS OF SUPPLY CURVES
At the peak demand periods of the British test system, the committed units are sorted by offer into
a stepped supply curve as shown in Figure 18. Under both truthful and learned offers, the steps of
the 14 nuclear units lie far to the left of the demand line. The policy learned by IPPO-PS raises the
whole supply curve while the demand line stays in place, and the price rises with it.
E.1.5 MARKUPS OF DIFFERENT LEARNERS
For each of the four learners the mean markup over the 66 units is near 1.5, but the spread across units
differs. IPPO-PS gives almost the same markup to every unit; IPPO-NoPS has the widest spread,
with some units near truthful offers and some near the cap; the two SAC learners fall between the
two, as shown in Figure 19. For each algorithm, NoPS has a wider spread than PS. All four learners
give the 14 nuclear units a mean markup below their own mean over all 66 units, and IPPO-NoPS
gives these units markups close to truthful offers.
48

Preprint.
Generating units by fuel and capacity Load and congested lines
0 5 10 15 20 25 30 35
Cumulative capacity (GW)
0
20
40
60
80
100
120Segment cost ($/MWh)
Units sorted by segment cost
case813nem: 813 buses, 1,278 lines, 151 units
Coal
Gas
Oil
Hydro
Unit, 100 MW
Unit, 1,000 MW
Bus
Line rated 500 MW
Line without a rating
Bus load, annual mean 200 MW
Congested on all 3 days
Congested on the mid- and high-load days
Range of hourly system demand, one year
Figure 14: The test system case813nem, drawn as Figure 12: an open grid model of the mainland
Australian National Electricity Market with 151 units. Only 7 of its 1 278 lines carry a published
rating. Left: units by fuel and maximum output. Middle: annual mean bus load and the lines
congested under truthful offers on the three example days. Right: the supply curve ordered by
segment cost against the range of hourly demand over one year. Hydro and then coal fill the left of
the supply curve; three lines are congested on all three days and a fourth on the mid- and high-load
days.
49

Preprint.
Oct 2023 Jan 2024 Apr 2024 Jul 2024
20
25
30
35
40
Demand,
daily mean (GW)
case29gb: GB transmission system demand
13 Mar 15 Mar 17 Mar 19 Mar
25
30
35
Demand,
hourly (GW)
Hourly, the week around the mid-load day
Jan 2020 Apr 2020 Jul 2020 Oct 2020
0
2
4
6
Demand and output,
daily mean (GW)
case73rts: RTS-GMLC load and renewables, net demand
21 Mar 23 Mar 25 Mar 27 Mar
0
1
2
3
4
Demand and output,
hourly (GW)
Hourly, the week around the mid-load day
Apr 2025 Jul 2025 Oct 2025 Jan 2026
16
18
20
22
24
Demand,
daily mean (GW)
case813nem: mainland Australian NEM operational demand
07 Dec 09 Dec 11 Dec 13 Dec
15
20
25
Demand,
hourly (GW)
Hourly, the week around the mid-load day
Demand cleared by the market
Day-ahead forecast (observed by the agents)
Total load
Wind
Utility-scale PV
Rooftop PV
Hydro
Evaluation day
Mid-load example day
Figure 15: Demand on the three test systems, and the renewable output netted out on case73rts. Left:
daily means over the one-year window, with the 36 evaluation days marked. Right: hourly values in
the week around the mid-load example day. The thick black line is the demand the market clears;
the dashed line is the day-ahead forecast the agents observe. On case73rts the market clears net
demand, total load minus the renewable output shown, raised to a floor of 2 500 MW; it sits at that
floor in more than half of the hours of the year. Demand on case813nem has a floor of 11 500 MW,
reached in a few hours.
50

Preprint.
0 100 200 300 400
Training iteration
50
100
150
200
250
Training return
(kUSD per generator per day)
case29gb, IPPO-PS
0 100 200 300 400
Training iteration
case29gb, IPPO-NoPS
0 100 200 300 400
Training iteration
case29gb, SAC-PS
0 100 200 300 400
Training iteration
case29gb, SAC-NoPS
0 100 200 300 400
Training iteration
-2.0
-1.5
-1.0
-0.5
0.0
Training return
(kUSD per generator per day)
case73rts, IPPO-PS
0 100 200 300 400
Training iteration
case73rts, IPPO-NoPS
0 100 200 300 400
Training iteration
15
20
25
30
Training return
(kUSD per generator per day)
case813nem, IPPO-PS
0 100 200 300 400
Training iteration
case813nem, IPPO-NoPS
Mean of 3 seeds, 11-iteration moving mean Bootstrap 95% confidence interval
Figure 16: Training return on the three test systems. Top: the four learners on case29gb. Bottom:
IPPO-PS and IPPO-NoPS on case73rts and case813nem. Each line is the mean of three seeds, each
seed first smoothed by an 11-iteration centred moving mean, and the shaded band is the bootstrap
95% confidence interval. Return is the mean daily profit per generator over all sampled environment
steps of an iteration. On case29gb IPPO-PS is the only learner that rises and then falls; on the other
two systems the return of both learners falls from its starting level.
51

Preprint.
600
800Demand (GWh)
case29gb: 66 units, markup cap 2.0
60
80
100
case73rts: 73 units, markup cap 1.4
450
500
550
case813nem: 151 units, markup cap 2.0
75
100
125Mean LMP ($/MWh)
 20
25
30
20
30
40
40
60Production cost (M$)
 1.5
2.0
2.5
8
10
12
Jan 2024 Jul 2024
Evaluation day
0
20Profit, all units (M$)
Jan 2020 Jul 2020 Jan 2021
Evaluation day
-0.2
0.0
0.2
0.4
Jul 2025 Jan 2026
Evaluation day
0
5
10
Demand (same under all offers)
Truthful offers
Learned offers, IPPO-PS
Learned offers, IPPO-NoPS
Mean of 3 seeds with bootstrap 95% confidence interval
Figure 17: Daily system quantities on the 36 evaluation days of each test system, truthful offers
(black) against the learned offers of IPPO-PS (orange) and IPPO-NoPS (blue); each learned line is
the mean of three seeds, with a bootstrap 95% confidence interval. Rows: daily demand, the load-
weighted mean LMP, production cost, and the total profit of all units.
52

Preprint.
0 10 20 30
Cumulative committed capacity (GW)
0
50
100
150
200Offer price ($/MWh)
2024-06-23, 19:00–20:00 UTC
0 10 20 30 40
Cumulative committed capacity (GW)
2024-03-16, 18:00–19:00 UTC
0 10 20 30 40
Cumulative committed capacity (GW)
2024-01-23, 17:00–18:00 UTC
Supply curve at the hour of highest demand: units sorted by their offer
Truthful offers (true cost)
Learned offers, IPPO-PS, mean of 3 seeds
Bootstrap 95% confidence interval
LMP range over buses, learned
LMP range over buses, truthful
Demand in that hour
Nuclear units (thick segments)
Figure 18: Supply curves at the hour of highest demand on each example day of case29gb, the
evaluation days at the 10th, 50th and 90th percentiles of daily demand (2024-06-23, 2024-03-16 and
2024-01-23): committed units sorted by offer under truthful (grey) and learned (orange) offers, with
the steps of the 14 nuclear units drawn thicker and the demand in that hour as a dashed line; the
shaded bands are the range of LMP over the 29 buses under each set of offers. The learned offers are
the mean over three IPPO-PS seeds at the end of training, with a bootstrap 95% confidence interval
for each step; the learned LMP band is the range over buses of the seed-mean LMP. The nuclear
steps lie far to the left of demand under both sets of offers, and the learned offers raise the whole
curve.
Learned markup of each unit, mean of 3 seeds
Nuclear units
1 16 22 30 45 66
Unit, by segment-cost rank (1 = cheapest)
IPPO-PS
IPPO-NoPS
SAC-PS
SAC-NoPS 1.00
truthful
1.25
1.50
1.75
2.00
cap
Offer / truthful offer
Figure 19: Markup of each unit under the four learners on case29gb; rows are learners, each the
mean over three seeds, columns the 66 units ordered by segment cost. Colour is the markup of that
unit, averaged over the 36 evaluation days and the three seeds, on the full action range from 1.00
(truthful) to 2.00 (cap). Black triangles above the top row mark the 14 nuclear units.
53

Preprint.
E.2 M2: REAL-TIMEBALANCINGMARKET
In this section, we discuss the result of the four learners in the RTM balancing market.
E.2.1 MARKET SETTING
The action of unitiis a markupα i ∈[1,¯α]on its generation cost (i.e., true marginal cost over its
output range);α i = 1is a truthful offer, and an offer is submitted once per half-hour period. The
test systems of this market are case29gb and case73rts (detailed data in Table 5), with the markup
cap¯αset to 2. The grids and units are shown in Figures 12 and 13.
Most output is scheduled day ahead, so real-time offers price only small deviations: on the 36
evaluation days, the median absolute half-hourly demand deviation is 214 MW, less than 1% of
mean demand (Figure 20). This limits the gain from raising an offer alone (Section E.2.4).
13 Mar 14 Mar 15 Mar 16 Mar 17 Mar 18 Mar 19 Mar
25
30
35Demand (GW)
case29gb: the week around the mid-load day
-1000 0 1000
Deviation (MW)
0
5
10
15Share of half-hours (%)
Half-hourly deviation from the hourly mean
Half-hourly demand cleared in real time
Hourly day-ahead schedule, summed over buses
Day-ahead forecast (observed by the agents)
Mid-load example day
All 365 days
36 evaluation days
Figure 20: Demand on case29gb. Left: the week around the mid-load day (2024-03-16): the half-
hourly demand the real-time market clears (teal), the hourly day-ahead schedule summed over buses,
which equals the hourly mean of that demand (purple steps), and the day-ahead forecast the units
observe (dashed yellow). Right: the deviation of the demand in each half-hour from the mean of its
hour, over all 365 days (grey) and the 36 evaluation days (teal). On the evaluation days the absolute
deviation has a median of 214 MW, a 90th percentile of 638 MW and a maximum of 1 478 MW,
against a mean demand of 27 730 MW. The day-ahead schedule follows the half-hourly demand to
within a few hundred MW.
E.2.2 AGENT TRAINING
The training return is the mean daily profit per unit under sampled actions, which is the objective of
the learner itself. Under all four learners the mean markup of the 30 committed units starts between
1.48 and 1.61; at the end of training it is 1.04 under IPPO-PS, and 1.24, 1.40 and 1.39 under IPPO-
NoPS, SAC-PS and SAC-NoPS; the markup along training is shown in Figure 4b. On case29gb the
training return of IPPO-PS falls throughout and ends lowest of the four learners; IPPO-NoPS and
SAC-PS also fall, by less; SAC-NoPS rises first and then stays level (top row of Figure 21). On
case73rts IPPO-PS and IPPO-NoPS are trained, and the training return of both rises slowly (bottom
row of Figure 21).
E.2.3 DISCUSSION OF RESULTS
On case29gb, IPPO-PS returns to truthful offers, while the other three learners end with higher total
profit and lower system cost, as shown in Figure 22. This position is not learned. The untrained
networks already give the units different markups, and training only moves these markups towards
truthful offers. The reason is that an independent learner sees only how its own return responds to
its own action. A unit that raises its offer alone only loses output, as shown in section E.2.4. If
its output depends on its offer, its gradient points towards truthful offers; if not, its gradient is zero.
Without parameter sharing, each unit follows its own gradient: the first kind returns to truthful offers
and the second stays where it started. With sharing, the updates from the first kind move all units,
so every markup falls together.
54

Preprint.
0 50 100 150 200
Training iteration
-180
-160
Training return
(kUSD per generator per day)
case29gb, IPPO-PS
0 50 100 150 200
Training iteration
case29gb, IPPO-NoPS
0 50 100 150 200
Training iteration
case29gb, SAC-PS
0 50 100 150 200
Training iteration
case29gb, SAC-NoPS
0 50 100 150 200
Training iteration
-3.3
-3.2
-3.1
-3.0
-2.9
Training return
(kUSD per generator per day)
case73rts, IPPO-PS
0 50 100 150 200
Training iteration
case73rts, IPPO-NoPS
Mean over seeds, 11-iteration moving mean Bootstrap 95% confidence interval
Figure 21: Training return on two test systems in the real-time market. Top: the four learners
on case29gb. Bottom: IPPO-PS and IPPO-NoPS on case73rts. Each line is the mean over seeds,
smoothed by an 11-iteration moving mean, and the shaded band is the bootstrap 95% confidence
interval of the mean. Return is the profit of a unit per day, averaged over units and over the environ-
ment steps of an iteration. On case29gb the return of IPPO-PS falls the most, and SAC-NoPS is the
only learner whose return rises. On case73rts the return of both learners rises slowly.
There are 36 units that are never committed, which give a clean test. Their offers never enter the
clearing, so their own return carries no signal. Without information sharing, training leaves their
markups unchanged (IPPO-NoPS from 1.48 to 1.49, SAC-NoPS from 1.50 to 1.51). With sharing,
they fall with the committed units (IPPO-PS from 1.52 to 1.03, SAC-PS from 1.57 to 1.47). SAC-
PS falls much less, because under SAC the committed units themselves stay far from truthful offers
(Section 5.2). These results show an information limit in electricity markets: a unit learns a bidding
strategy only when its offer changes its own outcome. Otherwise, its learned offer comes from the
initialization (without parameter sharing) or from the other units (with it), and should not be read as
a strategy.
E.2.4 UNILATERAL AND JOINT MARKUPS
We extend the discussion in Appendix E.2.3 in this section.
A unit gains little by raising its offer alone. We let each of the 30 committed units raise its offer
alone, at 21 markup levels from 1.00 to 2.00, while the other 65 units offer truthfully as shown in the
left subfigure of Figure 23. For 19 units, the most profitable level is the truthful offer, and no unit
gains more than $0.23 million per day. At a markup of 2.00, 27 of the 30 units lose profit, by up to
$8.0 million per day. The unit that raises its offer produces less, and the other units take over both
its output and its lost profit (Figure 23, right, slope−0.97). A unilateral markup therefore moves
profit between units but leaves the total almost unchanged.
Raising all offers together helps only if the markups differ across units. With the same markup for
all 66 units, the order of the offers and the dispatch schedules do not change as shown in Figure 24.
The reason is the two-settlement rule equation 18. Since the day-ahead market clears the actual
hourly demand, output below the schedule in one half-hour is roughly offset by output above it in
the other. A higher real-time price therefore moves money between units without raising the total.
Different markups, in contrast, change the dispatch, raise total profit and lower system cost, as under
IPPO-NoPS, SAC-PS and SAC-NoPS (as shown in Figure 22). This joint gain appears only when
units offer differently, and no single unit sees it in its own profit.
55

Preprint.
1.0 1.1 1.2 1.3 1.4 1.5
Markup  (offer / truthful offer), mean of 30 units
0.0
0.5
1.0
1.5
2.0
2.5
3.0T otal profit change (M$ per day)
T otal profit of all 66 units
1.0 1.1 1.2 1.3 1.4 1.5
Markup  (offer / truthful offer), mean of 30 units
8
6
4
2
0
System cost change (%)
System cost
IPPO-PS IPPO-NoPS SAC-PS SAC-NoPS Truthful offers
Figure 22: Learned offers against truthful offers on case29gb over the 36 evaluation days. Left:
change in total profit of all 66 units compared to truthful offers (in million dollars per day); right:
change in system cost compared to truthful offers (in percent). Each circle indicates one learner after
training, placed at the mean markup of the 30 committed units. The bars are the 95% confidence
interval of the mean over seeds; the dotted line is truthful offers. IPPO-PS returns to truthful offers;
the other three learners end with higher total profit and lower system cost.
1.0 1.2 1.4 1.6 1.8 2.0
Markup  (offer / truthful offer)
8
6
4
2
0
Own profit change (M$ per day)
One unit raises its offer, the others offer truthfully
8
 6
 4
 2
 0
Own profit change (M$ per day)
0
2
4
6
8
Summed profit change of
the other 65 units (M$ per day)
Own change against the other 65 units
One committed unit
Median over the 30 units
One unit at one markup
Fit through the origin, slope 0.97
No change
Figure 23: Each of the 30 committed units raises its offer alone while the others offer truthfully.
Left: own profit change against markup (one line per unit, median in black). Right: own profit
change against the profit change of the other units (with a least-squares fit, near-zero points are
omitted). Means over the 36 evaluation days, in million dollars per day.
56

Preprint.
1.0 1.2 1.4 1.6 1.8 2.0
Markup  (offer / truthful offer)
0.02
0.01
0.00
0.01
0.02
T otal profit change (M$ per day)
T otal profit of all 66 units
1.0 1.2 1.4 1.6 1.8 2.0
Markup  (offer / truthful offer)
0.02
0.01
0.00
0.01
0.02
System cost change (%)
System cost
All 66 units at one markup Truthful offers
Figure 24: All 66 units at the same markup, from 1.00 to 2.00. Left: change in total profit (million
dollars per day). Right: change in system cost (%). Both are relative to truthful offers (dotted line),
averaged over the 36 evaluation days. A common markup leaves both nearly unchanged.
57

Preprint.
E.3 M3: ANCILLARYSERVICESMARKET
This section first gives the data, training curves and the discussion about results of the ancillary
services market.
E.3.1 MARKET SETTING
We consider the setting in which M2 and M3 are jointly cleared. Therefore, the action of each unit
ihas two parts: an energy offer with markupα i ∈[1,¯α], and one reserve offerπ res i,j,t per periodton
each of the two reserve productsj= 1,2, in £/MWh. The two products require a response within
10 and 30 minutes respectively. The reserve a unit is awarded on a product, called its reserve held,
is at most the output it can ramp up within that time. The reserve requirement of each product is 5%
of the demand forecast of the period. Unmet reserve requirement is priced atVOLR(as shown in
Table 6), and the reserve priceλ res j,t does not exceed it.
This market uses the same three test systems as the day-ahead market: case29gb, case73rts and
case813nem. Table 5 describes their data, and Table 6 gives the markup cap and the value of lost
reserve for each system. Figures 12 to 14 show the grids and units, and Figure 15 shows the demand.
Table 6: Markup cap and value of lost reserve of the ancillary services market on the three test
systems.
Test system Markup cap¯αValue of lost reserveVOLR(£/MWh)
case29gb 2 250
case73rts 2 136
case813nem 2 147
E.3.2 AGENT TRAINING
The four learners are trained as described in Appendix D, and Figure 25 shows their training return.
On the case29gb test system, IPPO-PS is the only learner whose return falls, from−106k £per
generator per day over the first 5 iterations to−126over the last 20. The other three rise slightly and
stay close to where they started. In test systems case73rts and case813nem, the return of both IPPO
learners rises.
E.3.3 DISCUSSION OF RESULTS
Training does not make the learners more profitable in this market. The untrained networks, with
random reserve offers, already earn £2 million to £4.5 million per day more than truthful offers as
shown in Figure 26. IPPO-PS gives almost all of this back: after training, it earns only £0.56 million
per day more than truthful offers, £3.95 million less than its untrained network. The other three
learners stay near their starting point, at £2.71 million to £3.69 million per day above truthful offers.
No learner receives more gains compared to its own untrained network.
A much larger gain is available, but no learner finds it. If all units raise their reserve offers together
to £150/MWh, total profit rises by £9.05 million per day as shown in the subfigure c of Figure 4.
Only £0.51 million to £1.63 million per day of the learners’ profit comes from reserve payments,
and the rest comes from energy. Production cost stays within 0.6% of its truthful level as shown in
the subfigure b of Figure 26.
The other two test systems show the same results, but the differences are small: all changes in profit
are within a few tens of thousands of dollars per day as shown in subfigures c and d of Figure 26.
After training, IPPO-PS again earns the same as or less than before training, while IPPO-NoPS earns
slightly more.
E.3.4 RESERVE OFFER ANALYSIS
In ancillary service markets, a unit gains almost nothing by raising its reserve offer alone, but all
units gain a lot by raising it together as shown in Figure 27. When one of the 29 committed units
raises its reserve offer from 0 to £150/MWh while the others offer truthfully, its own profit usually
58

Preprint.
0 50 100 150 200
Training iteration
-130
-120
-110
-100
Training return
(kUSD per generator per day)
case29gb, IPPO-PS
0 50 100 150 200
Training iteration
case29gb, IPPO-NoPS
0 50 100 150 200
Training iteration
case29gb, SAC-PS
0 50 100 150 200
Training iteration
case29gb, SAC-NoPS
0 50 100 150 200
Training iteration
-4
-3
-2
Training return
(kUSD per generator per day)
case73rts, IPPO-PS
0 50 100 150 200
Training iteration
case73rts, IPPO-NoPS
0 50 100 150 200
Training iteration
2
4
6
case813nem, IPPO-PS
0 50 100 150 200
Training iteration
case813nem, IPPO-NoPS
Mean of 3 seeds, 11-iteration moving mean Bootstrap 95% confidence interval
Figure 25: Training return on the three test systems. Top: the four learners on case29gb. Bottom:
IPPO-PS and IPPO-NoPS on case73rts and case813nem. Return is the mean daily profit per genera-
tor in each iteration. Lines are the mean of three seeds, each smoothed over 11 iterations, and bands
are bootstrap 95% confidence intervals. On case29gb, only the return of IPPO-PS falls, and on the
other two systems, both learners rise.
does not change. Across the 29 units, the median change is zero, the largest gain is £0.08 million per
day, and the largest loss is £0.32 million per day. When all 66 units raise their reserve offers together,
total profit rises linearly with the offer, by £9.05 million per day at £150/MWh, while production
cost changes by less than 0.001%.
59

Preprint.
Total Reserve
settlement
Energy
0
1
2
3
4
5
6Million $ per day
(a) Profit change vs truthful offers
-0.5
0.0
0.5
1.0
1.5
% vs truthful offers
(b) Production cost change
-1.25 -1.00 -0.75 -0.50 -0.25 0.00 0.25
Production cost change (%)
-0.04
-0.02
0.00
0.02
Profit change,
million $ per day
(c) case73rts, vs untrained network, same layout and seed
0.00 0.05 0.10 0.15 0.20 0.25 0.30
Production cost change (%)
0.000
0.005
0.010
0.015
0.020
0.025
(d) case813nem, vs truthful offers
IPPO-PS
IPPO-NoPS
SAC-PS
SAC-NoPS
Untrained network, same layout
Learned policy, mean with 95% CI
Truthful offers
Reference, (c) (d)
Figure 26: Evaluation on the 36 evaluation days. (a) case29gb: change in total profit of all 66
units relative to truthful offers (million dollars per day), split into reserve payments and energy.
(b) case29gb: change in production cost. Filled markers are trained policies; hollow markers are
untrained networks. (c) case73rts, relative to the untrained network (truthful offers not evaluated),
and (d) case813nem, relative to truthful offers: change in total profit against change in production
cost for IPPO-PS (orange) and IPPO-NoPS (blue). The black square marks the reference. Markers
are seed means with bootstrap 95% confidence intervals. On case29gb, all learners earn more than
truthful offers at nearly unchanged cost, but only IPPO-PS earns less than its untrained network; on
the other two systems, the differences are small.
0 10 25 50 100 150
Reserve offer ($/MWh)
0
2
4
6
8Profit change (million $ per day)
Raising the reserve offer: one unit alone, and all 66 units together
One unit alone: its own profit (one line per committed unit)
Median over the 29 units
All 66 units together: total profit
Truthful offers
Figure 27: Raising the reserve offer on case29gb from 0 to £150/MWh on both energy and reserve
products. Teal: own profit change of each of the 29 committed units when it raises its offer alone,
with the others truthful. Black: the median. Orange: total profit change of all 66 units when all raise
their offers together. Values in million dollars per day. Raising alone gains almost nothing, while
raising together gains £9.05 million per day at £150/MWh.
60

Preprint.
E.4 M4: PEER-TO-PEERLOCALENERGYMARKET
Section 5.3 finds that an arbitrage that pays for a single household (charging at noon and discharging
in the evening) cancels itself when many households adopt it, and that whether a learner finds it
depends on the parameter layout. This section first describes the community and its metering data
(Section E.4.1), then gives the training curves (Section E.4.2) and the evaluation results on held-
out episodes (Section E.4.3); the last section covers how the gain from arbitrage changes with the
number of households arbitraging (Section E.4.4).
E.4.1 MARKET SETTING
The test system at community level has the 1 200 households with PV in the Fluvius 2024 metering
data, as shown in Figure 28. Each household is considered as one agent. Each period is a quarter-
hour, and an episode is the 96 periods of one day. The smart meters record only the injection and the
offtake of each household, and the market takes their difference as the net position of each household.
The export price isπ exp = 73.0EUR/MWh and the retail tariff isπ ret = 333.4EUR/MWh. Each
household has one battery with a capacity of 0.011 MWh, a round-trip efficiency of 0.85 and a
battery degradation cost of 13.88 EUR per MWh of throughput; its state of charge (as a fraction of
capacity) stays between 0.15 and 1.0 and starts at 0.5.
In every period, each household chooses a battery power (charge or discharge) and a price between
the two grid prices. A household with a positive net position sells, and the price is its ask; one with a
negative net position buys, and the price is its bid. As shown in Figure 29, at noon most households
inject more than they take off and are sellers: around 15:00 about 80% households are sellers, and
at night injection is close to zero.
The peer-to-peer market of the test community
1,200 households
Sellers
Buyers
...
Double auction, every 15 min
πret
πexp
λloc t
price
energy
asks
bids
Grid
net export
sold at πexp
net import
bought at πret
trades settled at λloc t
Asks of sellers Bids of buyers Export price Retail tariff Clearing price
Figure 28: The P2P market of the test community. Each of the 1 200 households has PV and a
battery. In every quarter-hour, sellers ask and buyers bid in a community double auction, which
sets the clearing priceλ loc t between the export priceπ exp and the retail tariffπ ret; trades in the
community are settled atλ loc t . Energy the auction leaves unmatched is settled with the grid.
Table 7: Data of the test community.
Data source Households Period covered Training and held-out Licence
Quarter-hour
injection and offtake
from Fluvius smart
metersa
1 200, all
with PV
2024-04-01 to
2024-10-26,
209 days
3 consecutive days held out
of every 15; 14 702 training
and 2 702 held-out episode
starts; evaluation on 1 024
held-out episodes, of which
the figures below use 64
Fluvius open
data licence
a opendata.fluvius.be/explore/dataset/1 50-verbruiksprofielen-dm-elek-kwartierwaarden-voor-een-
volledig-jaar/.
61

Preprint.
0 6 12 18 24
Hour of day
0.0
0.5
1.0
1.5
Injection and offtake
(MW, sum over households)
Community injection and offtake
0 6 12 18 24
Hour of day
0
20
40
60
80
100Share of households (%)
Households injecting more than they take off
Injection, median
Offtake, median
Share, median
Interquartile range over 64 held-out episodes
Figure 29: The test community of 1 200 households: community injection and offtake (left) and the
share of households injecting more than they take off (right), by hour of day over the 64 held-out
episodes.
E.4.2 AGENT TRAINING
The training setup of the four learners is that of Appendix D, and the two SAC learners differ from
Table 3 only in using two hidden layers of 64 units, a replay buffer of 8 192 environment steps, a
batch size of 16 environment steps and one gradient step every 4 environment steps. The training
return of both IPPO learners rises fastest in the first 50 iterations, and both SAC learners level off
within the first few dozen iterations. After that the return changes little, as shown in Figure 30: from
iterations 100–149 to iterations 351–400, the mean return of each IPPO learner rises by only 0.0009
to 0.0027 EUR per household per quarter-hour.
0 100 200 300 400
Training iteration
-0.05
-0.04
-0.03
-0.02
-0.01
0.00
Training return (EUR per
household per quarter-hour)
IPPO-PS
0 100 200 300 400
Training iteration
IPPO-NoPS
0 100 200 300 400
Training iteration
SAC-PS
0 100 200 300 400
Training iteration
SAC-NoPS
Mean of 3 seeds, 11-iteration moving mean Bootstrap 95% confidence interval
Figure 30: Training return of the four learners up to iteration 400; the policy at iteration 400 is
the one evaluated throughout this section. Shown is the mean over three seeds of the 11-iteration
moving mean of the return on 64 sampled training episodes, with the shading the bootstrap 95%
confidence interval. Both IPPO learners rise fastest in the first 50 iterations and both SAC learners
reach their level within a few dozen; after iteration 50 all four change little.
E.4.3 DISCUSSION OF RESULTS
We evaluate the results under truthful offers and under the considered learners. Truthful offers mean
that households with batteries stay idle, and sellers ask the export price and buyers bid the retail
tariff. As shown in Figure 31, IPPO-NoPS is the most consistent learner: all three of its seeds lower
the clearing price and raise the profit per household on every one of the 64 episodes. IPPO-PS and
SAC-NoPS are less consistent, with all three seeds earning more than under truthful offers on 54 and
57 episodes, respectively. Averaged over the 64 episodes, the profit per household is−1.201EUR
per episode under truthful offers and−0.769to−0.685EUR over the three seeds of IPPO-PS, the
highest of the four learners. The three seeds of SAC-PS disagree on the clearing price: the mean
clearing price of two of them is 270.3 and 272.9, against 238.1 EUR/MWh under truthful offers.
62

Preprint.
73
203
333
Mean clearing price
(EUR/MWh)
1 16 32 48 64
Held-out episode, in order of start time
-4
-2
0
Profit per household
(EUR per episode)
The 64 held-out episodes: truthful offers against the four learners
Truthful offers
IPPO-PS
IPPO-NoPS
SAC-PS
SAC-NoPS
Bootstrap 95% confidence interval over 3 seeds
Export price (73), retail tariff (333)
Figure 31: Results on the 64 held-out episodes ordered by start time. Top: mean clearing price per
episode. Bottom: profit per household per episode. Black is truthful offers; each learner is the mean
of three seeds with a bootstrap 95% confidence interval. IPPO-NoPS lowers the price and raises the
profit on every episode, while IPPO-PS and SAC-NoPS gain on 54 and 57 episodes. The seeds of
SAC-PS disagree, and two of them raise the price.
Figure 32 shows the actions each learner learns. The state of charge in each period of the day (the
last 12 hours of each episode only: in every episode the learned policies first sell the energy stored
at the initial state of charge of 0.5) splits the different learners into two behaviours according to
whether they share parameters: IPPO-NoPS and SAC-NoPS charge in the hours of PV surplus and
discharge in the evening, IPPO-NoPS by a large amount and SAC-NoPS by a small one; IPPO-PS
and SAC-PS stay near the lowest state of charge. The learners also differ in their bidding prices.
Under both IPPO learners, most sellers ask a price close to the export price. Buyers lean towards
the retail tariff under IPPO-PS, but bid at all levels under IPPO-NoPS. Under SAC-NoPS, most asks
and bids are close to one of the two grid prices, and few lie in between. The three seeds of SAC-PS
learn very different prices, so SAC-PS has the widest confidence intervals in the figure.
E.4.4 ARBITRAGE GAIN AND PARTICIPATION
This section asks how the gain from arbitrage changes with the number of households arbitraging
at the same time. The fixed schedule of Section 5.3 charges at 2.62 kW from 11:00 to 15:00 and
discharges at 2.62 kW from 18:00 to 22:00, with all households offering truthfully; it is replayed on
the 64 held-out episodes withkhouseholds on the schedule and the rest idle (Figure 33). The gain
is the change in profit per household per episode (EUR) relative to all batteries idle.
Arbitrage pays only when few households take part, as shown in the left subfigure in Figure 33. A
single arbitraging household gains 1.129 EUR per episode, but the gain falls as more households
join, turns negative at 210 to 240 households, and reaches−1.248EUR when all 1 200 take part.
The households that keep their batteries idle benefit instead: with 600 households arbitraging, each
idle household gains 0.573 EUR.
More specifically, arbitrage closes the price spread it relies on as shown in the right subfigure in
Figure 33: charging at noon raises the noon price, and discharging in the evening lowers the evening
price. Once about 240 households take part, the remaining spread no longer covers the round-trip
losses and the degradation cost. This saturation comes from the market, not from the learner. For a
single agent (household) the price is exogenous, but as more agents follow the same strategy, their
actions change the price, which becomes endogenous. A profit measured for one agent, or against
historical prices, therefore overstates what the strategy earns when many adopt it.
63

Preprint.
0 6 12 18 24
Hour of day
0.15
0.25
0.35
State of charge,
mean over households
IPPO-PS
0 0.5 1
0
20
40Share of asks (%)
0 0.5 1
Price submitted
(0 = export price, 1 = retail tariff)
0
20
40Share of bids (%)
0 6 12 18 24
Hour of day
IPPO-NoPS
0 0.5 1
0 0.5 1
Price submitted
(0 = export price, 1 = retail tariff)
0 6 12 18 24
Hour of day
SAC-PS
0 0.5 1
0 0.5 1
Price submitted
(0 = export price, 1 = retail tariff)
0 6 12 18 24
Hour of day
SAC-NoPS
0 0.5 1
0 0.5 1
Price submitted
(0 = export price, 1 = retail tariff)
Mean of 3 seeds Bootstrap 95% confidence interval PV surplus hours Lowest state of charge, 0.15
Figure 32: Learned actions of the four learners on the 64 held-out episodes (mean of three seeds,
bootstrap 95% confidence interval). Top: state of charge averaged over households by hour of day
(last 12 hours of each episode only). The band marks the PV surplus hours, those in which the
community injects more than it draws on most days. Middle and bottom: asks and bids, scaled from
the export price (0) to the retail tariff (1).
0 240 600 1200
Households following the schedule, of 1,200
-1.0
-0.5
0.0
0.5
1.0
Gain (EUR per household per
episode, vs. all batteries still)
Gain from the arbitrage schedule
0 240 600 1200
Households following the schedule, of 1,200
73
203
333Clearing price (EUR/MWh)
Mean clearing price in the two windows
Each household on the schedule
Each household keeping its battery still
Charging window, 11:00 to 15:00
Discharging window, 18:00 to 22:00
Export price
Retail tariff
No gain
Figure 33: On the 64 held-out episodes,khouseholds follow a fixed arbitrage schedule (charge
11:00–15:00, discharge 18:00–22:00) and the rest keep their batteries idle. Left: gain per household,
for those arbitraging and those idle, relative to all batteries idle. Right: mean clearing price in the
charging and discharging windows. The horizontal axis of both panels isk. Arbitrage pays while
few households take part and turns into a loss at 210 to 240 households, before the two window
prices cross.
E.5 M5: LOCALFLEXIBILITYMARKET
In this appendix section, we provide detailed market simulation settings and the discussion of the
performance of the four learners.
64

Preprint.
E.5.1 MARKET SETTING
The test system is the Swiss distribution feeder 459 0, as shown in Figure 34. The system has 129
buses and 128 lines, and we scale its load by 1.50. We consider an episode as one day, and the
market is cleared hour by hour. Each aggregator operates one battery, and aggregatorisubmits
three quantity bids at periodt, including a priceπ i,t, an offered quantity, and planned charging. The
distribution system operator (the operator) clears the market by minimising the cost of satisfying
demand, as detailed in Appendix A.5. Each winning aggregator is paid its own offer. The price floor
is set to the replacement costc rep = 149.88CHF/MWh.
Feeder 459_0 on the national map
 The congested line: 7.5 m, rating 7.24 MVA
Lake Geneva
Basemap © swisstopo, National Maps (grey), via wms.geo.admin.ch.
Enlarged view and locator map © CNES, Spot Image, swisstopo, NPOC, SWISSIMAGE Background, via wms.geo.admin.ch.
Network data: Zapparoli et al., Sci Data 12:1491 (2025), CC BY 4.0.
Battery bus, 2040 plan (24)
New in the 2050 plan (12 of 34)
Substation
Red box: the area enlarged next to it
Behind the congested line: 57 buses;
12 of 24 batteries in 2040, 16 of 34 in 2050
Rest of the feeder: 72 buses
Figure 34: Feeder 459 0 in Switzerland. Bottom right: its location in the Lake Geneva region.
Left: the feeder, with a small red box marking the congested line. Top right: an aerial image of
the congested line. Lines behind the congested line are blue, and only batteries on these lines can
relieve it.
The system requires that the bus voltage stays above 0.9 per unit and that the flow of every line
keeps within its maximum value. The operator buys flexibility to keep voltage within its range and
the congested line within its rating. The requirement is how much the flow on the line would exceed
98% of its rating if the operator bought nothing. This flow includes the load and the charging the ag-
gregators plan, so the aggregators can raise the requirement themselves as detailed in Section E.5.3.
In the Swiss test system, voltage stays within its limits all year, so the line is the only reason to buy.
The flexibility market trades much less than the P2P energy market, because it buys only what
is needed to keep the network within its limits. With all batteries idle, it buys on only 9 of the
65

Preprint.
36 test days, and never more than 0.43 MW, as shown in the left subfigure of Figure 35. Only
batteries downstream of the line can relieve it: 12 of 24 in the 2040 placement and 16 of 34 in
the 2050 placement. The 12 batteries alone can supply 2.51 MW, almost six times over the largest
requirement as shown in the right subfigure of Figure 35. Supply therefore far exceeds demand.
0 6 12 18 23
Hour of day
0.0
0.1
0.2
0.3
0.4
0.5Requirement (MW)
Requirement on the congested line, 36 test days
1 12 24
Aggregator, behind the line first, then by power
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8Power (MW)
Battery power per aggregator
one test day with a requirement
example day
behind the congested line
elsewhere on the feeder
peak requirement
Figure 35: Demand and supply of flexibility. Left: the requirement in each hour of the 36 test days,
with all batteries idle. Right: the power of each of the 24 batteries in the 2040 placement, with the
12 downstream of the congested line first.
Table 8: Overview of Swiss test system data.
Data Source Licence Training
days
Validation days Test days
Swiss
distribution
feeder 459 0
SwissDNa,
Zapparoli et al.
(2025)b
CC BY 4.0 293
days
36 days (the 5th,
15th and 25th of
each month)
36 days (the 1st,
11th and 21st of
each month)
Energy price
(category
C2, 2026)
ElComc opendata.swiss
Open use
— — —
a https://doi.org/10.5281/zenodo.15056134; b https://doi.org/10.1038/s41597-025-05830-y;
c https://energy.ld.admin.ch/elcom/electricityprice.
E.5.2 AGENT TRAINING
The training setup is that of Appendix D, and IPPO differs from Table 3 only in the following: each
iteration takes 4 full-batch gradient steps, the learning rate of3×10 −4 decays linearly to zero over
300 iterations, the log standard deviation of exploration is annealed linearly from−0.5to−3.0over
the same span, and the initialisation scale of the actor output layer is 0.01 rather than 1.0. Training
uses the training days of Table 8; the stopping rule and the checkpoint evaluated on the test days are
given in Table 4. On the test days the selected checkpoint acts with sampled actions, IPPO at a log
standard deviation of−3.0, the end point of its annealing, and SAC at the log standard deviation of
its own actor.
E.5.3 ANALYSIS OF THE PROCUREMENT REQUIREMENT
Under truthful offers, the operator buys flexibility in about 5% of periods: 43 of 864 hours across
the 36 test days in the 2040 placement, as shown in Figure 35. All four learners increase this share.
More than 80% of daily procurement lies above what truthful offers buy, and aggregator returns
track procurement as shown in Figure 37. The excess comes from planned charging, which raises
baseline flow on the congested line above 98% of its rating and leads the operator to buy flexibility
from batteries behind it. Cleared prices remain near the floor: on the test days, all IPPO seeds and
75% of SAC seeds clear within 1% of it.
66

Preprint.
0 100 200 300
Training iteration
10−1
100
101
102
103
Training return
(CHF per aggregator per day)
IPPO-PS
0 100 200 300
Training iteration
IPPO-NoPS
0 100 200 300
Training iteration
SAC-PS
0 100 200 300
Training iteration
SAC-NoPS
24 aggregators, 3.9 MW
24 aggregators, 6.3 MW
34 aggregators, 3.9 MW
34 aggregators, 6.3 MW
geometric mean over seeds
bootstrap 95% confidence interval
Figure 36: Training return of the four learners against training iteration; lines are the geometric mean
over the seeds of each configuration and shaded bands the bootstrap 95% confidence interval, each
seed held at its last value after it stops. All four learners reach a plateau within about 100 iterations.
In the two 3.9 MW configurations, replacing truthful-offer aggregators with SAC-PS learners raises
the share of periods with flexibility procurement from 5.0% to 18.7% with 24 aggregators, and from
4.9% to 15.4% with 34 aggregators (Figure 6(c)). With the monitor on, all six paired runs in the
34-aggregator configuration show daily procurement falling from about 3.2 to 0.15 MWh and daily
return per learner falling from about 118 to 1 CHF.
E.5.4 ANALYSIS OF A UNILATERAL MARKUP
In the 24-aggregator, 3.9 MW configuration, aggregator 7’s return from a unilateral offer rises with
the offer up to the highest offer swept, 9 900 CHF/MWh, as shown in Figure 6(b). With all others at
the floor, raising its offer to 150.25 CHF/MWh (0.25% above the floor) lets the cheaper aggregators
behind the congested line clear first. On the example day, aggregator 7 is awarded only from 13:00
to 18:00, when their offers cannot meet the requirement as shown in the right subfigure of Figure 38.
Its award over the 36 test days falls from 8.86 to 2.53 MWh and remains at 2.53 MWh even at
9 900 CHF/MWh. Its return therefore drops sharply (just above the floor), then rises almost linearly
with its offer. For the curves in Figure 6(b), return exceeds its floor value again at about 481 and
489 CHF/MWh in the two 3.9 MW configurations, but only at about 4 590 CHF/MWh in the 34-
aggregator, 6.3 MW configuration.
Near the floor, the bidding offer becomes nearly flat:π=c rep[1 + softplus(απ)]givesdπ/dα π =
crepsigmoid(απ), which approaches zero asαπ decreases as shown in the left subfigure of Figure 38.
This weakens the return gradient reaching the price action and helps explain why learners stay near
the floor.
67

Preprint.
0
10
20
30
Periods in which the
operator buys (%)
24 aggregators, 3.9 MW
0
5
10
15
Procurement
per day (MWh)
0
25
50
75
100
Return per aggregator
per day (CHF)
24 aggregators, 6.3 MW 34 aggregators, 3.9 MW
mean 263
34 aggregators, 6.3 MW
mean 175
Truthful offers
Untrained network
IPPO-PS
IPPO-NoPS
SAC-PS
SAC-NoPS
procurement also bought under truthful offers
procurement above truthful offers
bootstrap 95% confidence interval
Figure 37: Source of the flexibility requirement over the 36 test days of the four configurations.
Bars show truthful offers, the untrained shared and per-agent networks pooled in one bar, and the
four learners at validation-selected checkpoints (seed mean and bootstrap 95% confidence interval).
Two SAC-PS return bars exceed the axis and are cut at its top, with their means shown above. Rows
show the share of periods with procurement; daily procurement split into what truthful offers also
buy and the excess; and daily return per aggregator. Learners raise procurement above the truthful-
offer level, and their returns rise with it.
68

Preprint.
-7.5 -5.0 -2.5 0.0 2.5
Price action απ
0.01%
0.1%
1%
10%
100%
1000%Offer above floor
Offer above the floor against the action
0 6 12 18 23
Hour of day
0.0
0.5
1.0
1.5
2.0
2.5Award (MW)
Award of one aggregator, the others at the floor
offer = floor × (1 + softplus(απ))
within 1% of the floor: all IPPO seeds
requirement
requirement the others behind the line cannot cover
its award, at the floor
its award, alone at 150.25 CHF/MWh
its award, alone at 9,900 CHF/MWh
Figure 38: Unilateral offer increase. Left: offer above the floor against price action (log scale).
Near the floor, the gap shrinks by about a factor ofefor each unit decrease in the action. Cleared
prices for all IPPO seeds are within 1% of the floor. Right: aggregator 7’s hourly award on the
example day at offers of the floor, 150.25 and 9 900 CHF/MWh, with all other aggregators at the
floor.
69
