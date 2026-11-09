---
title: 'SAiFE-gym: Model-based Environments for Automated Market Making with Concentrated Liquidity'
url: https://arxiv.org/abs/2609.17788
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Georgios Chionas
- Charalampos Kleitsikas
- Stefanos Leonardos
- Leandro Sánchez-Betancourt
- Carmine Ventre
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.17788
pages: 8
chars: 46966
fetched_at: '2026-11-08T13:20:01+00:00'
kb_version: 1
---

# SAiFE-gym: Model-based Environments for Automated Market Making with Concentrated Liquidity

SAiFE-gym: Model-based Environments for Automated Market
Making with Concentrated Liquidity
Georgios Chionas∗
University of Liverpool
Liverpool, UK
g.chionas@liverpool.ac.uk
Charalampos Kleitsikas∗
King’s College London
London, UK
charalampos.kleitsikas@kcl.ac.uk
Stefanos Leonardos
King’s College London
London, UK
stefanos.leonardos@kcl.ac.uk
Leandro Sánchez-Betancourt
University of Oxford
Oxford, UK
leandro.sanchezbetancourt@maths.ox.ac.uk
Carmine Ventre
King’s College London
London, UK
carmine.ventre@kcl.ac.uk
Abstract
We present SAiFE_gym, a Python module that provides a collec-
tion of simulation environments for studying trading problems in
Constant Product Markets (CPMs) with Concentrated Liquidity
(CL). These markets give Liquidity Providers (LPs) granular control
over how their capital is allocated and enable them to adjust their
range of liquidity provision dynamically based on market condi-
tions, which in turn, dictates how they earn fees. We decompose
the microstructure of CPMs with CL in interactive components that
allow researchers and practitioners to capture various economic
settings. We employ a vectorized approach to optimize our environ-
ments, making them scalable for high dimensional Reinforcement
Learning (RL) workflows that best describe sequential decision
problems. We demonstrate the benefits of our environments by
evaluating the performance of RL agents in CPMs with CL under
uncertainty in market parameters.
1 Introduction
Automated market makers (AMMs) are some of the most used ap-
plications built on top of blockchains for trading. These markets
were proposed as an alternative to Limit Order Books, tailored to
the computational and storage limitations of blockchains. AMMs,
which mainly operate as constant function markets (CFMs), dictate
the rules of clearing demand and supply through bonding curves,
with the most dominant example being the constant product bond-
ing curve. Despite their simple design and the inefficiencies in its
first iterations, AMMs have facilitated $4 trillion in trading volume
across Ethereum and other Ethereum-compatible networks [25].
Consequently, AMMs have attracted the interest of researchers
within the mathematical finance community [ 5, 12, 27]. Most of
these works study stylized models, either from the Liquidity Provider
(LP) perspective [12] or from Liquidity Takers (LTs) [6, 27], by cap-
turing the AMM mechanics associated with their model specific
assumptions. Despite the mathematical elegance of those methods,
they are often low dimensional to accommodate analytical solutions
and, thus, are unable to capture the high dimensionality observed
in practice. Reinforcement Learning (RL), in turn, has emerged as a
paradigm for tackling such high dimensional control problems. Nev-
ertheless, we observe that there is fragmentation in model-based
simulation environments tailored to the AMM microstructure, and
∗Authors contributed equally to the paper.
to this day, there is not an open sourced unified and extensible
collection of environments available to the research community.
We introduce SAiFE_gym, a collection of Reinforcement Learn-
ing (RL) environments, that assembles components which govern
each AMM case study. Environments have the property that once
the skeleton is in place, the research community and practition-
ers can parallelize across different domains. For that reason, RL
environments sit at the centre of current AI progress, where each
new one expands what we can train, study, and evaluate. By lower-
ing the barriers to conducting research on AMMs, ourSAiFE_gym
contributes directly to the intersection between Crypto and AI [3].
The goal of this work is to assemble different aspects of the
AMM microstructure in an extensible way while also demonstrat-
ing the potential of RL for solving this type of stochastic control
problem. Broadly, the AMM microstructure is built from several
interacting components, namely the evolution of market prices,
the orderflow and the toxicity thereof, the price impact and the
liquidity distribution, and the frictions imposed by blockchains,
namely the gas costs for interacting with them and their inherent
latency. Our main architecture design for the RL environments is a
vectorized approach, whereby a batch of trajectories runs in parallel,
aggregating the results. This design choice significantly improves
computational efficiency (wall-clock efficiency) while also provid-
ing more stable estimates for policy optimization. The summary of
our contributions is given below.
Our Contributions.
(1) We provide a unified set of RL environments that replicate
the mechanics of AMMs under a wide range of combinations
of market dynamics. This is a key strength of our approach
as it supports picking and choosing different components of
modelling that can simulate various economic settings.
(2) We connect our environments to Stable Baselines 3 (SB3) [21],
which provides a rich suite of state-of-the-art RL algorithms.
These algorithms allow a “plug-and-play” approach to train RL
agents on previously unstudied problems, while also enabling
users to develop their own customizable agents.
(3) Following the design principles of [17], we develop a high de-
gree of parallelism in our collection of RL environments, which
can work on top of common existing multiprocessing methods,
achieving a level of efficiency for training AI agents that makes
the task feasible even for conventional machines.
arXiv:2609.17788v1  [q-fin.TR]  15 Sep 2026

Chionas et al.
(4) To demonstrate the applicability of our set of environments,
we evaluate the performance of RL agents under uncertainty
in market parameters embedded in the AMM microstructure.
This approach, known asdomain randomization, has found
great applicability in simulation-to-real work, c.f., [20].
The module is available on Github.
2 Related Work
Automated Market Makers.The computational efficiency of using
invariant functions (fixed trading functions) together with the com-
putational constraints of the early blockchains led simple AMMs,
in the form of Constant Product Markets, like Uniswap v2 [1], to
become a cornerstone in decentralised finance. The work in [ 5]
generalized the notion of the constant product invariant to the
broader class of Constant Function Market Makers (CFMMs) and
characterised conditions under which arbitrage aligns the price
quoted by a CFMM with the (true) price of an asset on an external
market, thus establishing the usefulness of CFMMs as price oracles.
Despite their widespread adoption, simple AMMs such as Uniswap
v2 suffer from capital inefficiency, since a substantial part of the
provided liquidity is never used. Newer protocols such as Uniswap
v3 [2] enable LPs to specify price ranges within which their liq-
uidity is active. This mechanism, known as concentrated liquidity
(CL), gives LPs more granular control over the allocation of their
capital. Consequently, Uniswap v3 significantly expands the LPs’
action space, which was previously considered passive.
This transition has sparked a significant line of research on
profitable strategies for LPs in CPMs with CL. We outline notable
works that inspired the collection of environments presented in
this work. The authors in [14, 15] study dynamic liquidity provision
strategies in Uniswap v3 and provide insights on how aspects of
a Uniswap v3 contract, notably the partition of price space, have
implications for LPs’ profit. The authors in [ 11] decompose the
LP’s losses in CPMs with CL into two parts; the convexity cost,
arising from the convexity of the pool’s invariant function, and the
opportunity cost, arising from the LP’s locking assets in the pool
instead of investing them in a risk-free account. The subsequent
work in [12] formulates dynamic liquidity provision as a stochastic
control problem and derives a closed form solution, under which the
LP reallocates its accumulated wealth continuously across intervals
as the price evolves. However, their model abstracts away from
frictions inherent to blockchain, mainly the gas fees and latency.
Reinforcement Learning for Market Making.In recent years, Re-
inforcement Learning has gained considerable traction in tackling
model-based problems in high frequency trading. This is because
market making in LOBs, as well as liquidity provision in CPMs with
CL, can naturally be formulated as stochastic control problems. RL
offers a complementary method to numerical solutions, which usu-
ally suffer from the curse of dimensionality and therefore struggle
to capture realistic models. While there is now substantial literature
and open-source infrastructures for model-based RL environments
in LOB trading, similar tools remain limited in the DeFi space.
In traditional finance, the work in [ 23] introduces one of the
earliest RL frameworks for market making in a LOB simulator
and shows that inventory-aware RL agents can outperform simple
known benchmarks. Closely related in spirit to our work, [17] pro-
vides a modular suite of Gym-compatible environments for model-
based LOB trading that supports picking different components of
existing models in the mathematical finance literature. However,
in that work, a reduced-form model of the LOB is implemented by
abstracting away from the statefulness of the entire order book. In
contrast, our implementation of the CPM with CL closely mirrors
the respective pools that are implemented in practice.
An alternative to model-based simulators has been the agent-
based simulators. Rather than specifying the market dynamics di-
rectly, agent-based simulators generate these dynamics through the
interaction of agents. Some notable works that implement agent-
based simulators to train RL agents in financial markets include
[18], [4], and [19]. These are some of the most important works that
demonstrate the effectiveness of RL in traditional finance settings.
Our work is one of the first to provide a modular infrastructure for
testing RL agents in AMMs.
3 Design of the Module
In the following sections, we give a detailed description of the im-
plemented RL environments, including the mechanics of a CPM
with CL and the microstructural dynamics that specify the environ-
ments. Formally, the interaction of the LP with the CPM with CL
can be viewed as a stochastic control problem over a continuous
time horizonI=[ 0,𝑇] , with terminal time𝑇 . In our RL environ-
ments, we approximate this problem on a discrete time grid with𝑛
steps. At each time step, every RL environment performs the ob-
servation phase, where the LP agent observes market information,
action phase, where the agent takes a new action, market opera-
tion phase, where the market processes the new orders and time
advancement phase. These phases are implemented in the class
AMMEnvironmentand it is inherited by all the RL environments.
We then present experiments demonstrating the capabilities of our
environments collection. Finally we discuss the implications of our
work and outline directions for future research.
3.1 Constant product markets and concentrated
liquidity
Constant Product Markets.Let 𝑋 denote a numéraire asset, such
as USDC, and let𝑌 denote a risky asset, such as ETH. A liquidity
pool for the pair(𝑋,𝑌) quotes a marginal exchange rate𝑍, mea-
sured in units of asset𝑋 per unit of asset𝑌 . Let𝑞𝑋,𝑞𝑌 > 0denote
the pool reserves of assets𝑋 and𝑌 , respectively. The reserves of a
CPM satisfy the invariant
𝑓(𝑞 𝑋,𝑞𝑌)=𝑞 𝑋𝑞𝑌 =𝜅 2,(1)
where𝜅> 0is the liquidity parameter, or depth, of the pool. In
the absence of fees, LT trades move the reserves along the level set
defined in (1). Differentiating the invariant shows that the marginal
exchange rate (the spot price) is𝑍=− d𝑞𝑋 d𝑞𝑌 = 𝑞𝑋 𝑞𝑌 . Thus,𝑍 is the pre-
fee marginal price of asset𝑌 in units of asset𝑋 for an infinitesimal
trade. The CPM charges a proportional trading fee𝜏∈[ 0, 1) on the
input amount. Consequently, only the fraction1 −𝜏 of a trade’s
gross input is used in the swap calculation.
Consider now an LT who submitsΔ𝑥> 0units of asset 𝑋 and re-
ceives Δ𝑦out > 0units of asset 𝑌 . The output amount is determined

SAiFE-gym: Model-based Environments for Automated Market Making with Concentrated Liquidity
by the invariant equation 𝑞𝑋+(1−𝜏)Δ𝑥  𝑞𝑌−Δ𝑦 out =𝑞 𝑋𝑞𝑌.
Solving forΔ𝑦 out gives
Δ𝑦out =𝑞𝑌− 𝑞𝑋𝑞𝑌
𝑞𝑋+(1−𝜏)Δ𝑥 .
Conversely, suppose that the LT submits Δ𝑦> 0units of asset 𝑌
and receives Δ𝑥out > 0units of asset 𝑋 . The invariant equation is𝑞𝑋−Δ𝑥 out 𝑞𝑌+(1−𝜏)Δ𝑦  =𝑞𝑋𝑞𝑌,which implies that
Δ𝑥out =𝑞𝑋− 𝑞𝑋𝑞𝑌
𝑞𝑌+(1−𝜏)Δ𝑦 .
Concentrated Liquidity.In a CPM with CL, an LP can restrict a
liquidity position to a specified interval of marginal exchange rates
(𝑍ℓ,𝑍𝑢]. The endpoints of the position are selected from a finite,
ordered grid
G=

𝑍(−𝑁) =𝑍, 𝑍(−𝑁+1) ,...,𝑍 (0),...,𝑍 (𝑁−1) , 𝑍(𝑁) =𝑍 	 ,(2)
for some𝑁≥ 1. Each pair of neighbouring grid points

𝑍(𝑖),𝑍(𝑖+1) 
is called atick range. Within a tick range, the pool satisfies a trans-
lated constant-product invariant. Equivalently, the CPM with CL is
a segmented CPM tailored to the liquidity in each tick range
When opening a position, the LP selects a range of rates(𝑍ℓ,𝑍𝑢]
and a liquidity amount ˜𝜅> 0. These variables combined with
current marginal exchange rate 𝑍, determine the corresponding
quantities𝑥and𝑦of assets𝑋and𝑌respectively, according to
(𝑥,𝑦)=
 


0, ˜𝜅

(𝑍ℓ)−1/2−(𝑍 𝑢)−1/2

, 𝑍≤𝑍 ℓ,

˜𝜅

𝑍 1/2−(𝑍 ℓ) 1/2

, ˜𝜅

𝑍−1/2−(𝑍 𝑢)−1/2

, 𝑍 ℓ <𝑍≤𝑍 𝑢,

˜𝜅

(𝑍𝑢) 1/2−(𝑍 ℓ) 1/2

,0

, 𝑍>𝑍 𝑢.
(3)
In words, when𝑍≤𝑍 ℓ, the position consists only of asset𝑌 , while
when𝑍>𝑍 𝑢, it consists only of asset𝑋 . When𝑍ℓ <𝑍≤𝑍 𝑢, the
position is active and contains quantities of both assets.
In a tick range𝑖, the total liquidity depth𝜅𝑖 is obtained by sum-
ming the liquidity amounts ˜𝜅𝑖 of each individual position in tick
range𝑖. Thus, the whole liquidity depth profile is captured by
𝜿= (𝜅𝑖)𝑁−1 𝑖=−𝑁 .(4)
The formulas in (3) and (4) give a reparameterization of the state of
the CPM with CL from the quantities𝑥,𝑦 of assets𝑋,𝑌 respectively,
to the total liquidity depth in each tick range and the marginal
exchange rate. The latter is more convenient, since, an LP action
changes only the liquidity depth profile (4), while an LT action
changes only the marginal exchange rate𝑍.
Lastly, the trading fees are stored in each tick range, and are
distributed pro-rata to each LP. For example, if the LP’s position
with depth ˜𝜅 is in a tick range with total depth 𝜅, then for every
liquidity taking trade that pays in fees an amount of𝑝, the LP earns
the amount of ˜𝑝= ˜𝜅 𝜅𝑝1𝑍ℓ <𝑍≤𝑍𝑢 .
3.2 Mid-price processes
In our RL environments, we follow the standard assumption in the
literature on AMMs, under which the price formation of the risky
asset𝑌 is exogenous to the AMM. Concurrently, the AMM quotes
its own price for the risky asset𝑌, the marginal exchange rate𝑍.
External Midprice (Exogenous).We call this process, the external
mid-price and denote it by𝑆𝑡 . There are various mid-price models
implemented in our environments, such as the Geometric Brownian
motion which is the solution of the stochastic differential equation
𝑑𝑆𝑡 =𝜇𝑆 𝑡𝑑𝑡+𝜎𝑆 𝑡𝑑𝑊𝑡, 𝑆 0 >0,(5)
with drift𝜇, volatility𝜎> 0, and where𝑊𝑡 is a Brownian motion.
Another implemented model is the Arithmetic Brownian motion,
where the mid-price can be written as
𝑆𝑡 =𝑆 0+𝜇𝑡+𝜎𝑊 𝑡, 𝑆 0 >0.
We also provide an arithmetic midprice model with an Ornstein–Uhlenbeck
alpha signal, from the algorithmic trading literature.
𝑑𝑆𝑡 =𝛼𝑡𝑑𝑡+𝜎𝑑𝑊 𝑡, 𝑆 0 >0,
𝑑𝛼𝑡 =−𝑘 𝛼𝛼𝑡𝑑𝑡+𝜎 𝛼𝑑𝑊𝛼 𝑡 , 𝛼 0∈R,
where𝑘𝛼 is the mean-reversion rate,𝜎𝛼 > 0is the volatility of the
signal, and𝑊 𝛼 is a Brownian motion independent of𝑊.
Marginal Exchange Rate (Endogenous).The marginal exchange
rate𝑍 is modelled as a pure jump process. We assume that the
marginal exchange rate takes values from the same discrete grid(2).
The evolution of the marginal exchange rate is endogenous because
it depends on the state of the environment as explained next.
3.3 Arrival processes
Currently in AMMs, the formation of the marginal exchange rate is
mainly due to LTs’ activity. In our RL environments, we decouple
the LTs’ activity into an exogenous and an endogenous component.
Noise Traders, Liquidity-attracted Traders and Informed Traders.
The entire LT action is captured by the next model for intensities.
𝜆± 𝑡 =max  𝛼0, 𝛼1+𝛼 2𝐾± 𝑡−+𝛼 3(𝑆𝑡−𝑍𝑡−) 	 (6)
where𝜆+ 𝑡 (resp.𝜆− 𝑡 ) is the intensity for LT sells (resp. LT buys).
The linear model (6), which was introduced in [7], captures three
stylized facts. The parameter𝛼1 is the baseline intensity of order
arrivals, which corresponds to noise traders, and this part is ex-
ogenous to the state of the AMM. The parameter 𝛼2 models the
relationship between arrivals and depth (which means that higher
depth implies more arrivals) and𝛼3 captures the impact of LT action
by informed traders who align the marginal exchange rate𝑍 with
the external mid-price𝑆.1 Lastly,𝛼0 > 0is a safeguard parameter
to prevent intensities from becoming negative. More specifically,
when𝑆𝑡−𝑍 𝑡− > 0(resp. 𝑆𝑡−𝑍 𝑡− < 0), all else being equal, we
expect a higher (resp. lower) buying intensity and a lower (resp.
higher) selling intensity, given that the marginal exchange rate is
underpriced (resp. overpriced). The subscript𝑡− represents the time
just before𝑡given that we are working with processes that jump.
The liquidity statistic𝐾± 𝑡− in (6) is implemented through expo-
nential kernelsK±, which are illustrated in Figure 1. These kernels
encode how the liquidity standing ahead of the current tick𝑖 affects
future arrivals. In particular, we implement
K+ 𝑖 =
𝐻−1∑︁
ℎ=0
𝑤ℎ+1𝜅𝑖+ℎ andK − 𝑖 =
𝐻−1∑︁
ℎ=0
𝑤ℎ+1𝜅𝑖−ℎ (7)
1Linear intensity models are widely used in the literature, see e.g., [24]. Writing the
dynamics of the AMMs à la Avellaneda-Stoikov was first proposed in [13].

Chionas et al.
−40 −20 0 20 40
0.0
0.5
1.0
1.5
2.0
2.5Liquidity
Liquidity distribution around current tick
Symmetric depth
Buy-side depth
Sell-side depth
Gap near price
Current tick
Sell kernel window
Buy kernel window
Figure 1: Smoothed kernels with exponential weights captur-
ing the impact of the neighbouring liquidity of the current
marginal exchange rate to the arrivals intensity.
where the weights𝑤 determine how liquidity in ticks away from
the current tick𝑖 affects future arrivals. Through this channel, the
LP’s action influences the future order flow.2
In our RL environments, the parameters𝛼1,𝛼 2,𝛼 3 and the ker-
nelsK± can be modulated to represent different AMM economic
settings, or they may be estimated from empirical data, as in [7].
3.4 Price Impact
The price impact refers to the function that connects the marginal
exchange rate before and after the execution of an LT trade. We
provide two such classes. We remind that the marginal exchange
rate𝑍 is implemented as a jump process and it lives in the grid (2).
Depth-independent price impact.This is a reduced-form model
whereby each LT trade pushes the marginal exchange rate to the
neighbouring tick based on the direction of the trade. If the marginal
exchange rate is at tick𝑖, a buy LT trade (resp. a sell trade) pushes
𝑍 to tick𝑖+ 1(resp. to tick 𝑖− 1). This reduced-form price impact
model in CPMs with CL has been used in the works [14, 15].
Depth-dependent price impact.In practice, price impact depends
on the curvature of the CPM and the concentration of liquidity
around the current marginal exchange rate. In order to capture
these factors, we compute a smoothed forward and backward depth
of the CPM with CL, over a given horizon of neighbouring ticks. The
smoothing approach is similar in spirit to the kernel implementation
for the order arrivals (7). We choose a smoothing horizon𝐻 and
non-negative weights𝑤1,𝑤 2,...,𝑤 𝐻 and
𝐻˝
𝑗=1
𝑤ℎ = 1. The smoothed
forward depth at tick𝑖is
𝐷+ 𝑖 =
𝐻−1∑︁
ℎ=0
𝑤ℎ+1𝜅𝑖+ℎ(𝑍𝑖+ℎ)1/2 and𝐷 − 𝑖 =
𝐻−1∑︁
ℎ=0
𝑤ℎ+1𝜅𝑖−ℎ(𝑍𝑖−ℎ)−1/2
(8)
where𝜅𝑗 is the total liquidity at tick 𝑗. A buy trade (resp. a sell
trade) causes a price impact tailored to the smoothed forward depth
(resp. smoothed backward depth). In particular, the size𝑄 of the LT
2These liquidity kernels are similar in spirit to the queue-reactive model studied in
LOBs [16], but, to the best of our knowledge, this is the first time considered in the
context of CPMs with CL.
trade (in units of the numeraire asset𝑋 ) is drawn from a custom
distribution (e.g. a lognormal distribution). 3 The price impact is
the number of jumps of the marginal exchange rate in the grid (2)
and it is calculated by𝑚=⌊𝑄/𝐷 𝑖 ±⌋. Therefore, when the marginal
exchange rate is at tick𝑖, a buy (resp. sell) trade of size𝑄 moves it
to tick𝑖+𝑚(resp. to tick𝑖−𝑚).
3.5 Blockchain Frictions
Gas Costs.Our RL environments capture the cost of rebalancing
as a fixed transaction cost. The fixed transaction cost corresponds
to the so-called gas fees paid by the LP to the network for interact-
ing with the blockchain. Gas fees are mostly a flat fee paid to the
blockchain and do not depend on LP’s specific position. Thus, gas
fees scale with the frequency of rebalancing. In particular, one can
write the cumulative cost up to time𝑡as
𝐶𝑡 =
∑︁
𝑟≤𝑡
𝑔𝑟,
where𝑟 are the times at which a rebalancing took place and𝑔𝑟 > 0
is the gas cost associated with the rebalancing.
Latency.In blockchain environments, there is inherent latency,
which prevents the LP from reallocating her liquidity and rebalance
her asset continuously. In our RL environments, we capture latency
by specifying the number of decisions throughout training and the
evaluation time. In other words, we allow deterministic latency.
Overall, all the components described in this section, are sum-
marized in Table 1.
3.6 Agents
We have implemented custom agents by primarily focusing on liq-
uidity provision in CPMs with CL. All the agents inherit from a base
classAgentwith the main function beingget_action(state).
Liquidity Providers.We implement two ways in which the LP
agent can interact with the CPM with CL that aligns with the
admissible actions of an LP in CPMs with CL such as Uniswap v3
and v4. Firstly, the agent can open an active position, where she
decides the lower and upper tick (𝑍ℓ,𝑍𝑢] such that, the current
marginal exchange rate𝑍∈(𝑍 ℓ,𝑍𝑢]. Secondly, the LP agent can
approximate a limit order by opening a position(𝑍ℓ,𝑍𝑢] outside
of the current marginal exchange rate, whereby𝑍≤𝑍 ℓ or𝑍>𝑍 𝑢.
This is essentially a single-sided asset provision and in particular,
provision of the risky asset𝑌 in the former case and provision of the
numeraire asset𝑋 in the latter case as defined in (3). In both cases,
every time the LP agent takes a new action, she first withdraws her
holdings in assets𝑋,𝑌 , collects the accumulated fees from her last
position and then reinvests her whole wealth to the new position.
Liquidity Takers.Although our main focus on the presented RL
environments is liquidity provision, we also provide an LT agent for
statistical arbitrage against the CPM with CL.4 The control of the LT
agent is the signed trading speed𝑣 at which the agent is buying or
selling the asset𝑌 . In particular, if𝑣> 0(resp. 𝑣< 0), the agent sells
(resp. buys) the risky asset𝑌 . If𝑣= 0, the LT agent does not trade.
3For a sell LT trade, the size in units of asset𝑌 is given by dividing the size𝑄 with
the current external price𝑆.
4We refer to the work [27] for a detailed treatment on liquidity taking in CPMs.

SAiFE-gym: Model-based Environments for Automated Market Making with Concentrated Liquidity
Economic component Role in the environment Implemented models
External midprice Generates the exogenous market reference price𝑆𝑡 observed by the AMM
and the LP.
BrownianMotionMidpriceModel;
GeometricBrownianMotionMidpriceModel;
OrnsteinUhlenbeckMidpriceModel
Order arrivals Generates LT action and updates its intensity from AMM state. LiquidityKernelArrivalModel
Price impact Maps LT trades into jumps of the marginal exchange rate. OneTickUniswapV3PriceImpact; LiquidityDepthUniswapV3PriceImpact
Reward function Defines the objective optimized by the agent. PnL; RunningInventoryPenalty
Table 1: Components in SAiFE_gym. Each setting is exposed through a small interface, enabling plug-and-play of different
components while keeping the remaining AMM engine fixed.
For each timestep𝑑𝑡 , the trading speed𝑣 implies the size𝑞 of the
LT’s trade is𝑣·𝑑𝑡 . The LT’s execution cost is specified through the
price impact that depends on the LT trade size𝑞, which is calculated
by theDepth-dependent price impactgiven in Section 3.4.
3.7 Reward Functions
Let𝑇> 0be the terminal time of the simulation and I=[ 0,𝑇] .
The reward PnL (the risk-neutral reward) consists of the mark-to-
market value of the LP’s position. Let(𝑥𝑡)𝑡∈I be the process of the
agent’s holdings in the numeraire asset,(𝑦𝑡)𝑡∈I be the process of
the agent’s holding in the risky asset and(𝑆𝑡)𝑡∈I be the external
midprice process. The final mark-to-market agent’s value is𝑉𝑇 =
𝑥𝑇+𝑦𝑇𝑆𝑇 . For the LP agent, the gas fees are subtracted from𝑥𝑡 , at
every rebalancing step. The PnL is the change in the agent’s value
between steps and therefore it can be written as𝑉𝑇−𝑉 0.
Risk A version.We implement a reward that captures risk aver-
sion through an inventory penalty. We use the Cartea-Jaimungal
criterion [10]. The rewardRunningInventoryPenaltyis calculated as
𝑉𝑇−𝑉 0−𝜂(𝑦𝑇− ˆ𝑦)2−𝜙
∫ 𝑇
0
(𝑦𝑡− ˆ𝑦) 2𝑑𝑡,(9)
where the constants𝜂,𝜙∈R + determine the terminal and running
penalty respectively from deviating from some target level ˆ𝑦. The
units of𝜂,𝜙 are such that the penalty terms are in units of𝑋 , while
the parameter𝜙 quantifies the urgency of the agent to liquidate the
risky asset𝑌.
4 Reinforcement Learning
In this Section, we describe how the AMM engine, presented in
Section 3, works along with RL workflows. This is achieved through
the wrappers that we outline in Section 4.1. Subsequently, in Sec-
tion 4.2, we present the custom vectorized approach that we follow
across all the environments, which enables noticeably faster conver-
gence in the agents’ rewards. Lastly, in Section 4.3, we demonstrate
a potential use case of our collection of environments in domain
randomized reinforcement learning; specifically, the evaluation
of RL agents when training is driven by uncertainty in the mar-
ket parameters embedded in the stochastic processes presented in
Section 3.
4.1 Wrappers
SAiFE_gym provides Gymnasium APIs for single agent deep rein-
forcement learning in the simulated CPM with CL. Figure 2 illus-
trates how a learning agent interacts with the AMM engine through
the SB3 wrapper. From the learning agent’s perspective, the AMM
SB3 Wrapper
Gymnasium Environment
Flatten dict
observations
step async
step wait
Auto-reset
terminal obs
reset / step
Gymnasium API
update agent state
update market state
Rewards and
batched info
LP rebalance
AMM Engine
Process swaps
walk tick grid
Accrue fees
portfolio features
calls env.step(action)
calls update state
Figure 2: Deep RL wrapper workflow
mechanics, the external midprice, and the arrivals are all part of the
environment. At each decision time, the learning agent observes
the current state, chooses an action, and passes this action to the
environment through the step interface. The environment then
updates the AMM state by applying the agent’s action together with
the simulated market dynamics. The resulting transition follows
the standard Gymnasium convention; the step(action) returns
the next observation, reward, and episode termination information.
In this way, the wrapper layer exposes transition tuples consisting
of observation, action, and next observation, while remaining ag-
nostic to the specific RL algorithm used. This wrapper is the main
compatibility layer between the AMM engine and the SB3 training
algorithms. Next, we briefly describe the functionality of the main
agent-specific wrappers that are implemented.
StructuredMultiDiscreteVecEnv.This wrapper re-parameterizes
the action space from [lower_offset, upper_offset, hold] ,
which is given in(3), to [center, half_width, hold] . The former
parameterization is Uniswap v3-native, while the latter one is more
suitable for RL training since the decisions are separable.
DecisionStrideEnv.This wrapper separates the market decision
frequency from the agent’s decision frequency. The role of this
wrapper is to capture the latency inherent in blockchain environ-
ments. Intuitively, it transforms a high-frequency control problem
into a lower-frequency decision problem.5 Through this wrapper,
one can customize the number of decisions per episode the agent
5Dynamic liquidity provision strategies are often slower than the underlying mar-
ket simulation. The AMM pool might update every time step, but an LP would not
necessarily rebalance after every LT trade.

Chionas et al.
100 101 102 103
Number of trajectories
10 2
10 1
100
Rollout time (s)
concurrent.futures (1 traj / process)
NumPy vectorized (1 process)
Figure 3: Speedup of vectorization using NumPy.
will take in equally split time intervals. For example, by setting
K_stride=0, we recover the continuous-time setting where the
market decision frequency aligns with the agent’s decision fre-
quency.
ReduceStateSizeWrapper.The implementation of the CPM with
CL is stateful enough; hence, one could customize the observation
space of the agent. We do offer several standard features that can
be used as components of the observations, namely:
•time remaining𝑇−𝑡,
• the mispricing𝑆𝑡−𝑍𝑡 between the external midprice and
the marginal exchange rate,
•the LP’s current position,
•the accrued fees.
4.2 Vectorized approach
RL agents require training policies across many market paths in
order to obtain reliable gradient estimates and reduce sensitivity to
any single price or order-flow realization. To support this at scale,
our implementation adopts a vectorized simulation architecture
in which all state variables; actions, rewards, and the associated
stochastic processes presented in Section 3 carry a leading batch
dimension of size num_trajectories, the number of rollouts sim-
ulated in parallel, using NumPy arrays [ 26]. Consequently, each
environment step produces num_trajectories transitions.6 Our
design contrasts with the typical approach to parallelize RL “roll-
outs” at the process level, which instantiates many environments
across multiple CPU cores and sequentially generates trajectories
on each one. Our implementation, instead, amortizes memory al-
location and mathematical operations over the full batch in a sin-
gle pass. Figure 3 illustrates the speedup offered by our NumPy
implementation over the multiprocessing approach that uses the
concurrent.futures package for identical per-trajectory workload.7
For rolling out 1000 trajectories, the vectorized approach takes
≈ 0.05s versus≈ 1.6s for the multiprocessing approach, achieving
a speedup of roughly 30×. Typical RL training involves millions of
rollouts, making the multiprocessing approach prohibitively slow.
Additionally, in Figure 4, we plot the evolution of the mean reward
6This vectorization is native to the AMM structure, and it differs from Gymnasium
genericVectorEnv, which is agnostic to the AMM simulation engine.
7The benchmark was run on a single machine with 8 CPU cores and 16 GB of RAM.
0 50 100 150 200 250
Training epoch / rollout update
0.8
1.0
1.2
1.4
1.6
1.8
2.0Mean episode reward
Reward convergence under vectorized rollouts
10 trajectories
100 trajectories
1,000 trajectories
10,000 trajectories
Figure 4: Impact of vectorization in the stability of rewards.
per episode for different degrees of parallelization in terms of the
number of parallel trajectories. By increasing the number of parallel
trajectories from 10 to 10,000 the variance in the reported mean
episode reward drops across training updates, though we observe
little difference in the training performance for𝑛=100 and𝑛=1000.
4.3 Reinforcement Learning under Domain
Randomization
To demonstrate the potential of SAiFE_gym, we consider the eval-
uation of liquidity provision policies under distributional shifts
in market parameters. As a warmup, we provide an example of a
nominal RL agent, understationary transition dynamics, whereby
the learning agent is trained and evaluated under the same market
parameters. Subsequently, we proceed to domain randomization,
whereby we sample market parameters during training, a process
that we callnon-stationary transition dynamics.
Stationary Transition Dynamics.As a first example of training
an agent using SAiFE_gym, we use proximal policy optimization
(PPO) [22] to train an LP agent in a CPM with CL under fixed mar-
ket parameters. In this example, the external midprice𝑆𝑡 follows
a geometric Brownian motion (5), with 𝜇= 0and 𝜎= 0.03. The
evolution of the marginal exchange rate 𝑍𝑡 is formed by incom-
ing LT trades, for which we use the intensity model in (6), with
𝛼1 = 450,𝛼 2 = 10and 𝛼3 = 4000, where the latter captures the arbi-
trage pressure and is the main driver through which the marginal
exchange rate𝑍𝑡 follows the external midprice𝑆𝑡 throughout the
simulation period. We use the depth-dependent price impact model
described in Section 3.4. We set the initial price at𝑍0 =𝑆 0 = 100
and the LP agent’s initial wealth at1000in asset X. We initialize the
liquidity depth profile (4) with100, 000liquidity units in each tick
range. Near the tick ranges of the initial marginal exchange rate at
100, these liquidity units correspond to roughly50units in asset 𝑋 .
Moreover, we fix the size𝑄 of each LT trade at250units in asset
𝑋 , which causes a price impact of around 5 ticks in the marginal
exchange rate𝑍. We set a fixed gas cost at2units in asset𝑋.
We allow the agent to take one action every100time steps
through the wrapper DecisionStrideEnv, and we allow the agent
to choose her new positions within an interval of50tick ranges
from the current marginal exchange rate. The restrictions on the
agent’s action space are natural, but, importantly, they improve

SAiFE-gym: Model-based Environments for Automated Market Making with Concentrated Liquidity
97
98
99
100
101Price
Periodic 100-tick - path 1
Pool price
External midprice
LP range
Deploy/rebalance
Price
Nominal PPO seed 47 - path 1
Pool price
External midprice
LP range
Deploy/rebalance
100
101
102
103
104Price
Periodic 100-tick - path 2
Price
Nominal PPO seed 47 - path 2
0.0 0.2 0.4 0.6 0.8 1.0
Time
98
99
100
101
102
103Price
Periodic 100-tick - path 3
0.0 0.2 0.4 0.6 0.8 1.0
Time
Price
Nominal PPO seed 47 - path 3
Dynamic liquidity provision - sampled trajectories during evaluation ( = 0.03, 1 = 450)
Figure 5: Dynamic liquidity provision policies. On the left
column, we plot the strategy of the baseline agent (periodic
rebalancing), that rebalances symmetrically around the mar-
ginal exchange rate. On the right column, we plot sampled
trajectories from the learnt policy of the PPO agent. This is
for illustrative purposes to visualize how the agent react to
market conditions.
the agent’s exploration. As a reward class, we choose the running
inventory penalty from(9), setting the per-step inventory penalty at
𝜙= 0.4, the terminal inventory penalty at𝜂= 0, and the target level
at ˆ𝑦= 0. We compare the performance of the RL agent with that of
a baseline agent that rebalances every100time steps symmetrically
around the current marginal exchange rate𝑍, with50tick ranges
on each side. We spawn1000trajectories that run in parallel, and we
sample three of those during evaluation, as illustrated in Figure 5.
Non-Stationary Transition Dynamics.In order to expose the agent
to market uncertainty, we implement episode-level domain ran-
domization through a wrapper around the base environment class
AMMEnvironment. We consider the market domain 𝜃=(𝜎,𝛼 1),
where𝜎 is the volatility of the external midprice process𝑆𝑡 , and𝛼1
is the baseline arrival intensity in (6), which captures the intensity
of noise trading. During training, these market parameters are sam-
pled from the joint distribution𝜌𝜃 for the independent random vari-
ables𝜎,𝛼 1, according to𝜎∼U(0.01,0.05)and𝛼 1∼U(300,600).
At the start of each rollout, the wrapper samples𝐷 domains; that
is,𝐷 tuples of(𝜎,𝛼 1) and assigns them into balanced groups across
the𝑛 trajectories that run in parallel. The wrapper creates𝐷 groups,
each containing𝑛/𝐷 trajectories, and uses the same domain within
the group throughout the episode. The hyperparameter𝐷 offers the
following simple tradeoff. Larger𝐷 gives each PPO update broader
coverage of the domain distribution. Smaller𝐷 gives more repeated
stochastic trajectories per sampled domain. The remaining market
parameters are kept fixed across domains.
Naturally, the market domain 𝜃=(𝜎,𝛼 1) is not included in
the RL agent’s observation space; thus, the agent faces alatent-
parameterpartially observable decision problem. Consequently,
the domain randomized agent must learn behaviors that perform
well across the domain distribution. We use the exact same market
configuration as in theStationary Transition Dynamicsexample
in the previous paragraph. The reward is the running-inventory
criterion defined in (9) with a per-step inventory penalty𝜙= 0.4.
The objective is now modified to maximize the expected reward
across the distribution𝜌 𝜃
E𝜃∼𝜌𝜃
"
E𝜁∼𝑝(𝜁|𝜋,𝜃)
"𝑁−1∑︁
𝑛=0
𝑉𝑛+1−𝑉𝑛−𝜙Δ𝑡𝑦 2 𝑛+1 
##
,(10)
the trajectory𝜁 is sampled from the trajectory distribution induced
by policy𝜋in the environment with the market domain𝜃.
For evaluation, we compare the domain-randomized agent with
thenominalPPO, trained under the fixed domain(𝜎,𝛼 1)=( 0.03, 450).
Policies are evaluated using Monte Carlo trajectories at each of the
9 parameter points{0.01,..., 0.05}×{ 300,..., 600}, which include
in-distribution parameters as well as a few out of distribution mar-
ket parameters for stress testing. We report the mean objective
within each regime, which is illustrated in Figure 6. We note that
the policy of domain-randomized agent uses a feedforward method.
An alternative approach would be to implement a recurrent policy
that learns to infer dynamics from observation and action history,
as is done in [20].
Conclusion and Further Research
In this paper, we introduce SAiFE_gym, a collection of RL environ-
ments for solving trading problems in constant product markets
with concentrated liquidity. The goal was to assemble the com-
ponents of the AMM microstructure in a modular way, whereby
researchers and practitioners can create their desired economic
settings. We demonstrate the versatility of SAiFE_gym through ex-
periments under different economic settings. The vectorized design
of the environments makes these experiments computationally
tractable and allows policies to be evaluated across many trajecto-
ries under controlled variations of the underlying market model.
While SAiFE_gym provides a solid foundation for research, there
are several natural directions for future work. A first extension is
to develop multi-agent RL environments. In practice, liquidity pro-
vision is strategic, and, unlike market making in limit order books,
it is highly transparent. Hence, multiple LPs compete for order flow
by adjusting to common market signals and to other LPs’ actions [9].
A second direction is to further expand the action space of LPs in
our gym environment. In particular, our implementation is forward-
compatible, allowing LPs to set dynamic trading fees [8]. Last but
not least, we invite the community to implement additional agents
from the LT perspective. Our SpeedControlArbitrageurAgent is
a first building block towards this direction. Such extensions would
make it possible to study settings that interpolate between the
model-based environments developed in this work and more agent-
based simulations, in which market dynamics emerge from the
interaction of heterogeneous LPs, arbitrageurs, and noise traders
rather than from exogenously specified stochastic processes.

Chionas et al.
250 300 450 600 800
Baseline arrival rate
0.015
0.030
0.045
0.050Volatility
+49.15 +57.12 +79.45 +98.93 +120.67
+24.96 +28.65 +46.60 +61.23 +80.75
-1.75 +3.44 +18.69 +29.09 +45.02
-7.32 -2.80 +7.65 +18.15 +32.03
Periodic rebalancing
250 300 450 600 800
Baseline arrival rate
0.015
0.030
0.045
0.050Volatility
+61.66 +69.94 +93.43 +114.24 +137.10
+31.97 +36.04 +55.43 +71.31 +92.80
+1.44 +7.18 +23.52 +35.10 +52.08
-5.54 -0.43 +10.37 +21.58 +37.01
Nominal PPO
250 300 450 600 800
Baseline arrival rate
0.015
0.030
0.045
0.050Volatility
+61.24 +69.55 +93.08 +113.60 +136.64
+31.75 +35.94 +55.38 +70.82 +92.09
+1.81 +7.55 +23.90 +35.20 +52.28
-4.79 +0.11 +10.99 +22.07 +37.26
Domain-randomized PPO
0
20
40
60
80
100
120
Mean terminal PnL (gas included)
Expected terminal reward
Figure 6: Evaluation of the agents under different market regimes. The left panel shows the periodic-rebalancing baseline
agent, the middle panel shows the nominal PPO agent, trained in the market domain ((𝜎,𝛼 1)=( 0.03, 450)) and the right panel
shows the domain-randomized agent, trained on market domains sampled from the distribution (𝜌𝜃). The evaluation covers
both in-distribution market parameters (the dashed area) and out-of-distribution market parameters.
References
[1] Hayden Adams, Noah Zinsmeister, and Dan Robinson. 2020.Uniswap v2 Core.
https://app.uniswap.org/whitepaper.pdf
[2] Hayden Adams, Noah Zinsmeister, Moody Saleh, River Keefer, and Dan Robinson.
2021. Uniswap v3 Whitepaper.
[3] Sarah Allen, Pranay Anchuri, James Austgen, Maryam Bahrani, Samuel Breck-
enridge, Aaron Buchwald, Christian Cachin, Andrés Fábrega, Jared Fernan-
dez, James Hsin-yu Chiang, et al . 2026. Crypto x AI, AI x Crypto: A Survey.
arXiv:2606.13892(2026).
[4] Selim Amrouni, Aymeric Moulin, Jared Vann, Svitlana Vyetrenko, Tucker Balch,
and Manuela Veloso. 2022. ABIDES-gym: gym environments for multi-agent
discrete event simulation and application to financial markets. InProceedings of
the Second ACM International Conference on AI in Finance(Virtual Event)(ICAIF
’21). Article 30, 9 pages. doi:10.1145/3490354.3494433
[5] Guillermo Angeris and Tarun Chitra. 2020. Improved Price Oracles: Constant
Function Market Makers. InProceedings of the 2nd ACM AFT Conference(New
York, NY, USA)(AFT ’20). 80–91. doi:10.1145/3419614.3423251
[6] Guillermo Angeris, Alex Evans, Tarun Chitra, and Stephen Boyd. 2022. Optimal
Routing for Constant Function Market Makers. InProceedings of the 23rd ACM
Conference on Economics and Computation(Boulder, CO, USA)(EC ’22). 115–128.
doi:10.1145/3490486.3538336
[7] Alif Aqsha, Philippe Bergault, and Leandro Sánchez-Betancourt. 2026. Equilib-
rium Reward for Liquidity Providers in Automated Market Makers.Mathematical
Finance, to appear, arXiv:2503.22502(2026).
[8] Leonardo Baggiani, Martin Herdegen, and Leandro Sánchez-Betancourt. 2025.
Optimal dynamic fees in automated market makers.arXiv:2506.02869(2025).
[9] Leonardo Baggiani, Martin Herdegen, and Leandro Sanchez-Betancourt. 2026.
Competition between DEXs through Dynamic Fees.arXiv:2603.09669(2026).
[10] Álvaro Cartea, Ryan Donnelly, and Sebastian Jaimungal. 2017. Algorithmic
Trading with Model Uncertainty.SIAM Journal on Financial Mathematics8, 1
(2017), 635–671. doi:10.1137/16M106282X
[11] Á. Cartea, F. Drissi, and M. Monga. 2023. Predictable Losses of Liquidity Provision
in Constant Function Markets and Concentrated Liquidity Markets.Applied
Mathematical Finance30 (2023), 69–93.
[12] Á. Cartea, F. Drissi, and M. Monga. 2024. Decentralized Finance and Automated
Market Making: Predictable Loss and Optimal Liquidity Provision.SIAM Journal
on Financial Mathematics15, 3 (2024), 931–959.
[13] Álvaro Cartea, Fayçal Drissi, Leandro Sánchez-Betancourt, David Siska, and
Lukasz Szpruch. 2024. Strategic bonding curves in automated market makers.
A vailable at SSRN 5018420(2024).
[14] Zhou Fan, Francisco Marmolejo-Cossio, Daniel Moroz, Michael Neuder, Rithvik
Rao, and David C. Parkes. 2023. Strategic Liquidity Provision in Uniswap V3.
In5th ACM AFT Conference (AFT 2023), Vol. 282. 25:1–25:22. doi:10.4230/LIPIcs.
AFT.2023.25
[15] Zhou Fan, Francisco J Marmolejo-Cossío, Ben Altschuler, He Sun, Xintong Wang,
and David Parkes. 2022. Differential Liquidity Provision in Uniswap v3 and
Implications for Contract Design. InProceedings of the Third ACM International
Conference on AI in Finance. 9–17.
[16] Weibing Huang, Charles-Albert Lehalle, and Mathieu Rosenbaum. 2015. Sim-
ulating and Analyzing Order Book Data: The Queue-Reactive Model.J. Amer.
Statist. Assoc.110, 509 (2015), 107–122. doi:10.1080/01621459.2014.982278
[17] Joseph Jerome, Leandro Sánchez-Betancourt, Rahul Savani, and Martin Herdegen.
2023. Mbt-gym: Reinforcement learning for model-based limit order book trading.
In4th ACM International Conference on AI in Finance, ICAIF 2023, Brooklyn, NY,
USA. ACM, 619–627. doi:10.1145/3604237.3626873
[18] Pankaj Kumar. 2020. Deep Reinforcement Learning for Market Making. In
Proceedings of the International Conference on Autonomous Agents and Multiagent
Systems (AAMAS). 1892–1894.
[19] Chris Mascioli, Anri Gu, Yongzhao Wang, Mithun Chakraborty, and Michael
Wellman. 2024. A Financial Market Simulation Environment for Trading Agents
Using Deep Reinforcement Learning. InProceedings of the 5th ACM International
Conference on AI in Finance(Brooklyn, NY, USA)(ICAIF ’24). 117–125. doi:10.
1145/3677052.3698639
[20] Xue Bin Peng, Marcin Andrychowicz, Wojciech Zaremba, and Pieter Abbeel.
2018. Sim-to-real transfer of robotic control with dynamics randomization.
In2018 IEEE international conference on robotics and automation (ICRA). IEEE,
3803–3810.
[21] Antonin Raffin, Ashley Hill, Adam Gleave, Anssi Kanervisto, Maximilian Ernes-
tus, and Noah Dormann. 2021. Stable-baselines3: reliable reinforcement learning
implementations.J. Mach. Learn. Res.22, 1, Article 268 (Jan. 2021), 8 pages.
[22] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.
2017. Proximal Policy Optimization Algorithms. (2017). arXiv:1707.06347
https://arxiv.org/abs/1707.06347
[23] Thomas Spooner, John Fearnley, Rahul Savani, and Andreas Koukorinis. 2018.
Market Making via Reinforcement Learning. InProceedings of the 17th Interna-
tional Conference on Autonomous Agents and MultiAgent Systems(Stockholm,
Sweden)(AAMAS ’18). International Foundation for Autonomous Agents and
Multiagent Systems, Richland, SC, 434–442.
[24] Sasha Stoikov and Mehmet Sağlam. 2009. Option Market Making under Inventory
Risk.Review of Derivatives Research12 (2009), 55–79. doi:10.1007/s11147-009-
9036-3
[25] Uniswap Labs. 2026.Uniswap Powers ~31% of MetaMask Swaps. https://blog.
uniswap.org/uniswap-powers-31-of-metamask-swaps
[26] Stefan van der Walt, S. Chris Colbert, and Gael Varoquaux. 2011. The NumPy
Array: A Structure for Efficient Numerical Computation.Computing in Science
& Engineering13, 2 (March 2011), 22–30. doi:10.1109/mcse.2011.37
[27] Álvaro Cartea, Fayçal Drissi, and Marcello Monga. 2025. Decentralised finance
and automated market making: Execution and speculation.Journal of Economic
Dynamics and Control177 (2025), 105134.
