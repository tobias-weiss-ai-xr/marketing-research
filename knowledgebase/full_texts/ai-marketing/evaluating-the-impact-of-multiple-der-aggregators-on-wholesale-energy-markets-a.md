---
title: 'Evaluating the Impact of Multiple DER Aggregators on Wholesale Energy Markets: A Hybrid Mean Field
  Approach'
url: https://arxiv.org/abs/2409.00107
category: ai-marketing
subcategory: empirical
date: 2024-08
venue: ''
authors:
- Jun He
- Andrew L. Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2409.00107
pages: 13
chars: 33501
fetched_at: '2026-11-08T13:16:25+00:00'
kb_version: 1
---

# Evaluating the Impact of Multiple DER Aggregators on Wholesale Energy Markets: A Hybrid Mean Field Approach

arXiv:2409.00107v2  [eess.SY]  4 Jul 2025
Evaluating the Impact of Multiple DER Aggregators on Wholesale Energy
Markets: A Hybrid Mean Field Approach
Jun He∗ and Andrew L. Liu †
∗ School of Industrial Engineering, Purdue University, West Lafayette, IN 47906. Email: he184@purdue.edu
† School of Industrial Engineering, Purdue University, West Lafayette, IN 47906. Email:
andrewliu@purdue.edu
Summary
The integration of distributed energy resources (DERs) into wholesale energy markets can greatly enhance
grid flexibility, improve market efficiency, and contribute to a more sustainable energy future. As DERs
– such as solar PV panels and energy storage – proliferate, effective mechanisms are needed to ensure
that small prosumers can participate meaningfully in these markets. To address this, the Federal Energy
Regulatory Commission (FERC) in the U.S. issued Order 2222 in 2020, to enable DERs to aggregate and
participate in wholesale markets alongside traditional resources. However, detailed mechanisms are still
under development, and there remains uncertainty about which approaches are most effective for ensuring
small-scale participation.
In response to this challenge, we study a wholesale market model featuring multiple DER aggregators,
each controlling a portfolio of DER resources and bidding into the market on behalf of the DER asset
owners. The key of our approach lies in recognizing the repeated nature of market interactions the ability
of participants to learn and adapt over time. Specifically, Aggregators repeatedly interact with each other
and with other suppliers in the wholesale market, collectively shaping wholesale electricity prices (aka the
locational marginal prices (LMPs)). We model this multi-agent interaction using a mean-field game (MFG),
which uses market information – reflecting the average behavior of market participants – to enable each
aggregator to predict long-term LMP trends and make informed decisions. Unlike traditional game models,
where the strategies of all individual agents must be considered, the mean-field approach focuses on the
collective impact, simplifying the decision-making process.
For each aggregator, because they control the DERs within their portfolio under certain contract struc-
tures, we employ a mean-field control (MFC) approach (as opposed to a MFG) to learn an optimal policy
that maximizes the total rewards of the DERs under their management. This approach accounts for various
uncertainties, such as solar output variability, demand fluctuations, and LMP dynamics, allowing aggregators
to learn how to better manage their resources and optimize their market participation strategies.
The innovation of our work lies in the combination of a hybrid MFG and MFC approach, which allows
for the scalable modeling of multiple DER aggregators interacting within a wholesale market. This hybrid
approach effectively captures both the decentralized decision-making of individual aggregators and their
collective impact on market dynamics. We also propose a reinforcement learning (RL)-based method to help
each agent learn optimal strategies within the MFG framework, enhancing their ability to adapt to market
conditions and uncertainties. Unlike descriptive models that merely outline market participant behavior, our
model is prescriptive, designed for control automation. With the installation of grid edge devices running
our RL algorithms, market participants can automatically achieve the market outcomes described in this
paper.
We validate our approach using an electricity network model based on Oahu Island, incorporating realistic
1

data on solar panel output profile, penetration levels, and generator characteristics. Numerical simulations
show that LMPs quickly reach a steady state in the hybrid mean-field approach. Furthermore, our re-
sults demonstrate that the combination of energy storage and mean-field learning significantly reduces price
volatility compared to scenarios without storage.
Keywords: Mean-field equilibrium; multi-agent reinforcement learning; distributed energy resource;
wholesale energy market; locational marginal price; energy storage, solar PV, aggregators.
1 Introduction
The growing adoption of distributed energy resources (DERs), such as solar photovoltaic (PV) panels and en-
ergy storage systems, will lead to significant changes in the dynamics of electricity markets. Once considered
peripheral, these resources are now central to discussions about enhancing grid flexibility, improving market
efficiency, and promoting sustainability. The FERC Order 2222 [16] issued in 2020 recognizes the potential
of DERs to improve grid reliability and economic efficiency and encourages the participation of DERs in
wholesale energy markets, allowing them to compete alongside traditional power resources. However, it also
introduces significant challenges, particularly in ensuring meaningful participation for small-scale prosumers
– those who both produce and consume electricity.
While the FERC order lays the groundwork for DER-integration into wholesale markets, the detailed
mechanisms are still under development, with different RTOs/ISOs proposing different approaches. There
remains uncertainty about which approaches are most effective for integrating these resources into market
operations. Current research predominantly focuses on how a single aggregator manages its portfolio of
DER assets, often assuming that the whole energy prices (aka the locational marginal prices (LMPs)) are
exogenously given and remain unaffected by the aggregator’s actions. These models typically optimize the
aggregator’s strategy to maximize rewards based on these fixed LMPs, without considering the feedback
loop between the aggregator’s decisions and market prices.
In contrast, our work addresses a more complex setting where multiple aggregators operate within the
same market, each capable of influencing LMPs endogenously. In this setting, the aggregators are engaged
in a non-cooperative game, which we model as a mean field game (MFG). An MFG is a game-theoretic
framework used to study the behavior of a large number of interacting agents whose decisions are influenced
by the average behavior of the group. In an MFG, each agent, like an aggregator, optimizes its own strategy
based on both its individual objectives and the ‘mean field,’ which represents the average effect or state of
all agents in the market. This allows each agent to account for how their actions, combined with those of
many others, impact key market outcomes like prices.
Another innovation in our approach is that within each aggregator, we employ a mean field control
(MFC) approach, as opposed to a centralized optimization, to manage the portfolio of DERs. MFC focuses
on finding a policy for a representative agent (the mean field) that, when applied across all agents, optimizes
the overall collective outcome, rather than solving a complex optimization problem for each individual DER
owner. This approach reflects a cooperative framework (in contrast to the non-cooperative interactions
among different aggregators in an MFG), where the DER assets are treated as if they are working together
to maximize their collective rewards. The MFC method is more scalable than centralized optimization and is
well-suited for incorporating reinforcement learning (RL) techniques. This allows the aggregator to learn and
adapt to uncertainties such as solar output variability, demand fluctuations, and LMP dynamics, ultimately
developing optimal bidding strategies over time.
2

By combining MFC for managing internal operations within each aggregator and MFG for modeling
interactions among different aggregators, our model offers a comprehensive perspective on how multiple
aggregators, each with their own portfolio of DERs, can strategically interact and impact market outcomes
in a decentralized manner. Integrating these advanced modeling techniques with RL algorithms, our research
presents a novel and scalable approach that is conducive to control automation. The RL algorithms designed
for MFC can be embedded into smart controllers at DER owner sites, enabling efficient integration of DERs
under the management of aggregators. This approach enhances market efficiency and stability, especially as
DER adoption grows, by enabling aggregators to dynamically learn and adjust their strategies, taking into
account both market interactions and inherent uncertainties.
While RL algorithms have been extensively studied and applied in various domains, their traditional
applications often focus on single-agent scenarios or environments with fully observable states. Our work,
however, deals with multi-agent reinforcement learning (MARL), which introduces additional challenges,
particularly in scalability and coordination among agents. The majority of existing MARL algorithms are
designed for cooperative games, with only a few exceptions addressing non-cooperative scenarios. Regardless,
the MARL algorithms often struggle with scalability due to the need for each agent to consider the state
and actions of all other agents in the system. Both MFC and MFG offer specific ways to make MARL
scalable, as agents update their policies based on the mean field – a representation of the average effect of all
agents—rather than relying on the detailed state information of every individual agent. In this work, we also
contribute a MARL algorithm tailored for our hybrid MFC-MFG approach, drawing on recent advancements
in RL algorithms for MFC and MFG [1]–[3] and proposing a two-phase learning approach.
The rest of the paper is organized as follows: Section 2 introduces the wholesale energy market model and
explains the calculation of LMPs. In Section 3, we outline the decision-making problem faced by aggregators.
Section 4 details our proposed two-phase learning algorithm. In Section 5, we validate our approach using a
case study of an electric network model based on Oahu Island. Finally, Section 6 concludes with a summary
of our findings and potential directions for future research.
2 Wholesale Market Model and Locational Marginal Prices
In this section, we present a wholesale energy market model. Consider a power system network withM buses,
L transmission lines, and G generators. Each bus m ∈ {1, . . . , M} serves Nm household agents, consisting
of N p m prosumers and N c m consumers. Each generator g ∈ {1, . . . , G} has an associated cost function Cg(·).
Since each generator is linked to a specific bus, let Gm ⊆ {1, . . . , G} denote the set of generators located at
bus m. Clearly, ∪M m=1Gm = {1, . . . , G} and Gm ∩ Gm′ = ∅ for any distinct m, m′ ∈ {1, . . . , M}.
Let t ∈ {1, 2, . . .} represent the timestep, with each timestep corresponding to a fixed time interval, such
as an hour. At each time t, an aggregator at bus m collects the bids (which are determined through the
MFC approach to be described in the next section) from all the agents under its management and submits
the aggregated bids to the system operator. For prosumers, the specific quantity dimt represents the net
demand, defined as the prosumer’s demand minus the solar output from their own solar panel outputs. If
dimt ≥ 0, it indicates net energy demand; if dimt < 0, it represents net supply.
To avoid (unrealistic) scenarios where the net energy supply from prosumers exceeds the total demand
of all pure consumers, we assume that the total demand of all agents (both prosumers and consumers) in
the system is always greater than or equal to the total PV generation from all prosumers across all M buses.
3

Mathematically, this is expressed as:
MX
m=1
NmX
i=1
dimt ≥ 0, ∀ t = 1, 2, . . . (1)
Upon receiving all bids from power plants, aggregators, and other market participants, the system oper-
ator solves an economic dispatch problem to determine the least-cost way of meeting demand from available
supply sources while accounting for network constraints. This can be formulated as an optimization problem
for each timestep t as follows:
min
pt
GX
g=1
Cg(pgt) (2)
s.t.
GX
g=1
pgt =
MX
m=1
NmX
i=1
dimt, (3)
− F l ≤
MX
m=1
P T DFlm

 X
g∈Gm
pgt −
NmX
i=1
dimt

 ≤ F l, ∀ l ∈ {1, . . . , L}, (4)
0 ≤ pgt ≤ pg, ∀ g ∈ {1, . . . , G}, (5)
where pt =
h
p1t · · ·pGt
iT
represents the vector of power outputs from each generator. The parameter
P T DFlm denotes the power transfer distribution factor for line l, which connects bus m to a designated hub
in a hub-spoke network representation. In this representation, power flow from any bus m to another bus is
assumed to flow through the hub, so a line l is considered to connect a bus directly to the hub. F l in (4) is
the flow limit for line l, and pg in (5) is the maximum output capacity of generator g. For a fixed network,
the parameters Cg(·), P T DFlm, F l, and pg are known constants. Given the collected bids dimt at each time
t, the optimization problem can be efficiently solved using an optimization solver.
Upon solving the economic dispatch problem, the LMPs are determined from the dual values associated
with the constraints, denoted by λmt for each bus m at time t. The dual variables λHUB t , µlt, µlt, νgt, νgt
correspond to the Lagrange multipliers for constraints (3), (4), and (5), respectively. Here, λHUB t represents
the hub price, while the underlined and overlined µ and ν variables represent the dual variables of the lower
and upper bounds of the flow and power limits. Defining Dmt = PNm i=1 dimt as the total demand at bus m
at time t, the LMP λmt at bus m can be computed as:
λmt := ∂Lt ∂Dmt = λHUB t −
LX
l=1
P T DFlm(µlt − µlt), ∀ m ∈ {1, . . . , M}, (6)
where Lt is the Lagrangian function of the economic dispatch problem, defined as:
Lt =
GX
g=1
Cg(pgt) − λHUB t
 GX
g=1
pgt −
MX
m=1
Dmt
!
+
LX
l=1
µlt


MX
m=1
P T DFlm

 X
g∈Gm
pgt − Dmt

 − F l


−
LX
l=1
µlt


MX
m=1
P T DFlm

 X
g∈Gm
pgt − Dmt

 + F l

 +
GX
g=1

νgt(pgt − pg) − νgtpgt

.
(7)
In essence, the LMP λmt represents the marginal cost of supplying an additional unit of electricity to bus
m at time t, reflecting both generation costs and network constraints.
4

3 Aggregators’ Problem – A Two-Phase Learning Approach
In this section, we consider the problem faced by aggregators managing DERs, specifically prosumers with
photovoltaic (PV) panels and energy storage systems. Aggregators develop strategies to optimally charge
and discharge these storages under their control using RL algorithms. The RL algorithm employed here is
sophisticated, involving a two-phase learning approach. The key elements in presenting the algorithm are
listed below.
Time: At each timestep t = 0, 1, 2, . . ., each aggregator performs reinforcement learning using algorithms
such as Proximal Policy Optimization (PPO), Trust Region Policy Optimization (TRPO), Soft Actor-Critic
(SAC), and others for Ttrain steps. We use τ = 1 , 2, . . . , Ttrain to denote training timesteps, during which
aggregators learn a policy. The actual play phase involves submitting bids and calculating LMPs, and these
two phases are detailed in Section 4.
Prosumers: We consider a total of N heterogeneous prosumers in this game, where N = PM m=1 N p m.
Each prosumer i is assigned a fixed type θ ∈ Θ throughout the game, where Θ is a finite set. Prosumers of
the same type θ share the same net demand distribution, bus location, and reward function. For simplicity,
we assume all prosumers at the same bus have the same type, which differs across buses. Thus, the set Θ
corresponds to the set of buses {1, . . . , M}.
Aggregators: The assumption of prosumer types allows us to designate an aggregator as a “representa-
tive” for each type. In our setup, each bus has one aggregator who employs an RL algorithm for all prosumers
at that bus. Let xim denote the storage capacity of the i-th prosumer at bus m. The aggregator for bus
m thus has a total storage capacity of xm = PN p m i=1 xim.1 This is the essential idea of the MFC approach as
described in [2], which significantly reduces computational costs since typically |Θ| is much less than N .
LMP Beliefs: Let H be the total number of timesteps in one day. Define two mappings: h(·) and k(·),
which map the time index to the corresponding timestep of the day and the day index, respectively. In our
case, h(t) = t mod H and k(t) = ⌊t/H⌋. Each aggregator maintains its own belief about the LMPs for each
timestep of the day, represented as a vector of length H. Let ˆλmt ∈ RH denote the LMP belief of Aggregator
m at time t. After the system operator solves the economic dispatch problem, the aggregator is updated
with the new LMP λmt for its bus and updates its belief according to:
[ˆλm,t+1]h(t) = [ˆλmt]h(t) − δ [ˆλmt]h(t) − λmt p k(t) + 1 , (8)
where δ ∈ [0.5, 1] is a learning rate hyper-parameter for the LMP update rule.
Actions: Let A ⊆[−1, 1] represent the discrete action space. Each action corresponds to a percentage of
charging or discharging relative to the storage capacity. At time τ , each aggregator selects an action aτ ∈ A.
If aτ ≥ 0, the aggregator charges the storage by aτ , and if aτ < 0, it discharges aτ . For example, if each
action represents 1%, then A = {−1, −0.99, . . . ,0, 0.01, . . . ,0.99, 1}.
Action Masking: Action masking is a technique widely used in RL policy gradient algorithms. The
idea is to ‘mask out’ invalid actions and sample only from the set of valid actions. This technique has been
successfully applied in the context of video games, as demonstrated in [4]–[6], and is theoretically supported
in [7]. Mathematically, the algorithm assigns a value of −∞ to each invalid action based on the current state,
resulting in zero probability for those actions. For instance, if the current storage level is 0.8, any a <−0.8
1For simplicity, we assume that each bus m is served by a single aggregator, which we refer to as Aggregator m. This
assumption is made for ease of presentation, and relaxing it will not affect any outcomes.
5

or a >0.2 would be masked out to ensure the storage level remains between 0 and full capacity. From this
point onward, all actions are assumed to be valid.
States: Let S denote the state space. In an RL algorithm, each aggregator takes actions based on their
current state. The state at time τ , sτ ∈ S, is a tuple consisting of the storage level, net load demand, current
LMP belief ([ ˆλmt]h(τ )), and the current timestep of the day ( h(τ )). The storage level for Aggregator m at
time τ is denoted as xmτ ∈ [0, 1]. Let ηm ∈ (0, 1] be the storage efficiency parameter. The state transition
for Aggregator m after taking action amτ is:
xm,τ +1 = xmτ + 1 {amτ <0}ηmamτ + 1 {amτ ≥0}
amτ
ηm
, (9)
where 1 {·} is the indicator function, equal to 1 if the condition is satisfied and 0 otherwise. To simplify, we
define the mapping from an action to the actual percentage of charging or discharging as:
Φ(a, η) = 1 {a<0}ηa + 1 {a≥0}
a
η . (10)
Thus, equation (9) can be rewritten as:
xm,τ +1 = xmτ + Φ(amτ , ηm). (11)
During training, the aggregator samples the net demanddmτ (as a percentage relative to the storage capacity)
from a load shape profile Qp m, which is a probability distribution not known to the aggregator, but learned
from historical data.
Rewards and Policies: The single-period reward function is defined as:
rτ = r(sτ , aτ ) = −[ˆλmt]h(τ ) · xm · (Φ(amτ , ηm) + dmτ ). (12)
This reward function represents the payoff associated with the aggregator’s charging or discharging decisions
at each timestep τ , based on their beliefs of LMPs [ ˆλmt]h(τ ), the total storage capacity xm, and the net
energy adjustment (as a percentage) Φ( amτ , ηm) + dmτ .
Through an RL algorithm, each aggregator learns a policy πmt, a strategy mapping a given state to an
action distribution. The objective of RL is to find a policy πmt that maximizes the total discounted expected
reward:
πmt = arg max πmt E
( ∞X
τ =0
γτ rτ
)
, (13)
where γ ∈ (0, 1) is the discount factor.
4 The Two-Phase RL Algorithm
We now propose a two-phase distributed mean-field RL algorithm based on the setup above. The algorithm
comprises two phases: the training phase, where each aggregator trains its policy using RL algorithms for
a specified number of steps, and the actual play phase, where all prosumers use their aggregators’ trained
policies and submit their bids to the system operator to solve an economic dispatch problem and update the
LMPs. The algorithm is presented in Algorithm 1.
T raining Phase: At each time t, each aggregator fixes its LMP belief and performs RL using an
algorithm such as PPO, TRPO, SAC, etc., for Ttrain steps.
6

Actual Play Phase: After each aggregator has learned a policy, this policy is distributed to its pro-
sumers. At each bus m, each prosumer i samples an action from the policy aimt ∼ πmt. Let Qc m denote the
net load distribution for consumers at bus m, similar to the definition of Qp m. Each prosumer i and consumer
j samples their net load demand from dimt ∼ Qp m and djmt ∼ Qc m, respectively. The total demand Dmt is
then aggregated and submitted to the system operator as a single bid:
Dmt =
N p mX
i=1
(dimt + aimt) +
N c mX
j=1
djmt. (14)
An economic dispatch is then executed to obtain the new LMP λmt for all m at time t, which is subse-
quently used to update the belief as in Equation (8).
Mean-Field Equilibrium (MFE): Through mean-field learning, the system can reach an equilibrium
point known as an MFE. At an MFE, given a population profile s⋆ (mean-field), the corresponding optimal
policy is π⋆; with π⋆, the population profile remains s⋆ after the state transition. Mathematically, an MFE
is defined as follows:
Definition 1. An optimal policy π⋆ and a population profile s⋆ form an MFE if
s⋆(·) =
Z
S
Z
A
P(·|s⋆, a) dπ⋆(s⋆, s)(a) ds⋆(s), (15)
where P(·|s⋆, a) represents the state transition probability, which is the probability distribution over the
next state, given the current state s⋆ and action a and defines the dynamics of the system within the mean-
field framework, as it determines how the population profile changes in response to the strategies of the
agents.
In our multi-agent RL problem, the information about the mean-field is embedded in the LMPs through
economic dispatch. Thus, we can treat the LMP λ as a function of the mean-field and claim that an MFE
is achieved when a stationary pair of π⋆ and λ⋆ emerge. In Section 5, we empirically demonstrate that the
MFE can be reached.
5 Numerical Experiment
In this section, we conduct numerical experiments to analyze market behavior under the mean-field game
framework described earlier.
5.1 Test Case
We utilize the 37-bus synthetic network from [8], which corresponds to the geographical layout of the Hawaiian
island of Oahu. We modify this case by mapping each power plant from Hawaiian Electric [9] to its nearest
bus. After modification, the network comprises a total of 26 generators: 4 oil, 2 biomass, 17 (grid-scale)
solar, and 3 wind generators. We assume quadratic cost functions for all oil and biomass generators, applying
coefficients from [10], [11] to these respective generator types. The ranges for these coefficients are presented
in Table 1. Additionally, the generation cost for solar and wind generators is set to zero, with actual outputs
adjusted by a capacity factor based on weather conditions. Let ∆( a, b, c) denote a triangular distribution
with lower limit a, upper limit b, and mode c. In our simulation, we assume that solar generation follows
7

Algorithm 1: A two-phase distributed mean-field RL algorithm for prosumers to bid energy and
update the belief of LMP
Input: Initial battery state xm0 ∈ [0, 1]; initial LMP belief ˆλm0 ∈ RH ; LMP belief learning
parameters δm; net demand shapes for prosumers and consumers Qp m, Qc m for each bus
m = 1, . . . , M; training steps Ttrain.
for t = 0, 1, . . .do
# Initialization
Get the timestep of the day h ← t mod H ;
Get the day index k ← ⌊t/H⌋;
Initialize an empty bid collector Dt ← {};
# Training phase
foreach bus m = 1, . . . , Mdo
Use RL to train the aggregator for Ttrain steps with initial storage xmt under ˆλmt and obtain
policy πmt ;
end
# Actual play phase
foreach bus m = 1, . . . , Mdo
Dmt ← 0 ;
foreach Prosumer i = 1, . . . , Np m do
Sample net demand dimt ∼ Qp m ;
Sample charging/discharging actions aimt ∼ πmt ;
end
foreach Consumer j = 1, . . . , Nc m do
Sample net demand djmt ∼ Qc m ;
end
Collect all bids Dmt ← PN p m i=1(dimt + Φ(aimt, ηim)) + PN c m j=1 djmt as in (14) ;
Submit the bid to collector Dt ← Dt ∪ {Dmtxm} ;
Storage state transition: xm,t+1 ← xmt + 1 N p m PN p m i=1 Φ(aimt, ηim) ;
end
Solve economic dispatch and get λmt ;
foreach bus m = 1, . . . , Mdo
Make a copy of the LMP belief: ˆλm,t+1 ← ˆλmt ;
Update the h-th belief only: [ ˆλm,t+1]h ← [ˆλmt]h − δm [ˆλmt]h−λmt√k+1 as in (8) ;
end
end
8

Table 1: Cost function coefficient ranges for non-renewable fuel types ( C(p) = ap2 + bp)
Fuel Type a ($/MW2h) b ($/MWh)
Oil 0.0059 - 0.0342 19.98
Biomass 0.001 - 0.002 28.45 - 52.65
an average profile from [12], scaled by a factor following ∆(0 .8, 1.2, 1), while wind generation is scaled by a
factor following ∆(0.5, 1.5, 1) from [13].
Each bus in the network hosts two types of agents: prosumers with DERs and energy storage, and pure
consumers. Each energy storage unit is set to a capacity of 10 kWh. The daily demand profiles for prosumers
and consumers are derived from average hourly net demand (gross load minus DER generation) and gross
load data from [14], respectively. We further assume that actual demand is the average demand scaled by
a factor following ∆(0 .9, 1.1, 1). Figure 1 illustrates the net demand shape for prosumers and consumers at
each timestep of the day.
Figure 1: Net demand shape for prosumers and consumers as a percentage with respect to energy storage
capacity (10 kWh). Data is adapted from [14].
5.2 Results
We employ PPO as the learning algorithm and set Ttrain = 3, 600, with H = 12 (corresponding to 2-hour
timesteps). The simulation is run for a period of 50 days and repeated 5 times using different random seeds.
The experiments were conducted on a Windows 11 system equipped with a 13th Gen Intel(R) Core(TM)
i7-13700KF (24 cores) and NVIDIA GeForce RTX 4070. Figures 2, 3, and 4 display the hub prices, storage
levels and charging/discharging actions, and renewable generators’ capacity factors, respectively.
Additionally, to study the impacts of energy storage coupled with the RL algorithms on LMP volatility,
we adopt the incremental mean volatility (IMV) measure from [15] as the metric. We also compare the
average cumulative ex-post cost (the product of the bidding quantity and the real-time LMP) across all
9

(a) Hub prices over the first 5 days during learning
 (b) Hub prices over the last 5 days during learning
Figure 2: Comparison of hub prices with and without energy storage
(a) Average storage level across the network
(b) Average charging/discharging actions across the net-
work
Figure 3: Average storage levels and charging/discharging actions over the last 5 days across the network
buses. The IMV of a sequence of LMPs {λt}∞ t=1 is defined as:
IM V= lim
T →∞
1
T
TX
t=1
|λt+1 − λt|. (16)
We approximate the IMV for a sequence of LMPs and calculate the cumulative ex-post cost over 5
simulation runs. Figure 5 shows the results for IMVs and costs over the last 5 days. It is evident that
learning reduces both volatility and cumulative ex-post costs.
5.3 Discussion
Our results indicate that prosumers can learn strategies to charge when prices are low and discharge when
prices are high using our algorithm. As shown in Figure 2b, hub prices stabilize towards an equilibrium, and
prosumer actions illustrated in Figure 3b align with a mean-field equilibrium (MFE). Some fluctuations are
observed at the 9th timestep in a day, likely due to variations in the solar/wind capacity factor. Since prices
are determined by the next cheapest generator available to supply an additional unit of power, fluctuations in
renewable capacity factors can lead to increased or decreased reliance on non-renewable sources, making prices
sensitive to small changes in charging/discharging actions. Overall, our model demonstrates the potential
for mitigating extreme price swings and fostering a more stable market environment under decentralized
decision-making.
10

(a) Wind generator capacity factor
 (b) Solar generator capacity factor
Figure 4: Capacity factors for renewable generators (wind and solar) over the last 3 days. Wind data is
adapted from [13], and solar data from [12].
(a) IMV of the hub price over 5 runs during the last 5
days
 (b) Cumulative ex-post costs over the last 5 days
Figure 5: Comparison of IMV and cumulative ex-post costs between learning (with storage) and non-learning
(without storage) over 5 runs during the last 5 days
6 Conclusion
In this paper, we propose a decentralized, mean-field-based model where aggregators make informed charging
and discharging decisions on behalf of the prosumers they manage. These decisions are guided by LMPs
in a wholesale energy market, which encapsulate information about aggregate demand, supply dynamics,
and network constraints. Additionally, we introduce a two-phase learning algorithm within the hybrid MFC
and MFG framework, leveraging RL to iteratively learn optimal policies for aggregators while facing various
uncertainties from renewable output, demand fluctuations, and evolving market dynamics.
Our numerical experiments suggest that the proposed approach can achieve convergence to an MFE,
where both the aggregators’ strategies and the LMPs stabilize. Additionally, comparisons between scenarios
with and without energy storage show that integrating energy storage with our RL-based algorithms can
effectively reduce extreme LMP volatility, promoting a more stable market environment under decentralized,
aggregator-led decision-making. This approach also provides cost benefits to consumers by optimizing the
use of energy storage.
Future work will focus on providing a theoretical foundation for our model, specifically proving the
convergence of the two-phase RL algorithm to an MFE. Additionally, we plan to explore the use of different
RL algorithms to further enhance performance under various market conditions.
11

References
[1] X. Guo, A. Hu, R. Xu, and J. Zhang, “Learning mean-field games,” Advances in neural information
processing systems, vol. 32, 2019.
[2] W. U. Mondal, V. Aggarwal, and S. V. Ukkusuri, “Mean-field control based approximation of multi-
agent reinforcement learning in presence of a non-decomposable shared global state,” arXiv preprint
arXiv:2301.06889, 2023.
[3] H. Gu, X. Guo, X. Wei, and R. Xu, “Mean-field multiagent reinforcement learning: A decentralized
network approach,” Mathematics of Operations Research, 2024.
[4] O. Vinyals, T. Ewalds, S. Bartunov, et al. , “Starcraft ii: A new challenge for reinforcement learning,”
arXiv preprint arXiv:1708.04782 , 2017.
[5] C. Berner, G. Brockman, B. Chan, et al., “Dota 2 with large scale deep reinforcement learning,” arXiv
preprint arXiv:1912.06680, 2019.
[6] D. Ye, Z. Liu, M. Sun, et al. , “Mastering complex control in moba games with deep reinforcement
learning,” in Proceedings of the AAAI Conference on Artificial Intelligence , vol. 34, 2020, pp. 6672–
6679.
[7] S. Huang and S. Onta˜ n´ on, “A closer look at invalid action masking in policy gradient algorithms,”
arXiv preprint arXiv:2006.14171 , 2020.
[8] A. B. Birchfield, T. Xu, K. M. Gegner, K. S. Shetye, and T. J. Overbye, “Grid structural characteristics
as validation criteria for synthetic networks,” IEEE Transactions on Power Systems , vol. 32, no. 4,
pp. 3258–3265, 2017. doi: 10.1109/TPWRS.2016.2616385.
[9] Hawaiian Electric, Power facts , Mar. 2024. [Online]. Available: https://www.hawaiianelectric.
com/about-us/power-facts.
[10] D. Krishnamurthy, W. Li, and L. Tesfatsion, “An 8-zone test system based on iso new england data:
Development and application,” IEEE Transactions on Power Systems , vol. 31, no. 1, pp. 234–246,
2016. doi: 10.1109/TPWRS.2015.2399171.
[11] R. Tidball, J. Bluestein, N. Rodriguez, and S. Knoke, “Cost and performance assumptions for modeling
electricity generation technologies,” National Renewable Energy Lab.(NREL), Golden, CO (United
States), Tech. Rep., 2010.
[12] A. Robinson, Solar pv analysis of honolulu, united states, 2024. [Online]. Available:https://profilesolar.
com/locations/United-States/Honolulu/.
[13] D. Arg¨ ueso and S. Businger, “Wind power characteristics of oahu, hawaii,”Renewable Energy, vol. 128,
pp. 324–336, 2018, issn: 0960-1481. doi: https : / / doi . org / 10 . 1016 / j . renene . 2018 . 05 . 080.
[Online]. Available: https://www.sciencedirect.com/science/article/pii/S0960148118306013.
[14] M. Coffman, P. Bernstein, S. Wee, and A. Arik, Estimating the opportunity for load-shifting in Hawaii ,
https://uhero.hawaii.edu/RePEc/hae/wpaper/WP_2016-10.pdf, 2016.
[15] M. Roozbehani, M. A. Dahleh, and S. K. Mitter, “Volatility of power grids under real-time pricing,”
IEEE Transactions on Power Systems, vol. 27, no. 4, pp. 1926–1940, 2012. doi: 10.1109/TPWRS.2012.
2195037.
12

[16] FERC, Participation of distributed energy resource aggregations in markets operated by regional trans-
mission organizations and independent system operators , Order No. 2222, 172 FERC ¶61,247, 2020;
FERC, Order on reh’g , Order No. 2222-A, 174 FERC ¶61,197, 2021; FERC, Order on reh’g , Order
No. 2222-B, 175 FERC ¶61,227, 2022.
13
