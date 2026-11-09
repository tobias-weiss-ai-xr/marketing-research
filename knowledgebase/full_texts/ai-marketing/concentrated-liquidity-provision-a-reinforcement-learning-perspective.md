---
title: 'Concentrated Liquidity Provision: a Reinforcement Learning Perspective'
url: https://arxiv.org/abs/2608.19389
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Georgios Chionas
- Charalampos Kleitsikas
- Stefanos Leonardos
- Leandro Sánchez-Betancourt
- Carmine Ventre
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.19389
pages: 8
chars: 46084
fetched_at: '2026-11-08T13:00:35+00:00'
kb_version: 1
---

# Concentrated Liquidity Provision: a Reinforcement Learning Perspective

Concentrated Liquidity Provision: a Reinforcement Learning
Perspective
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
Automated market makers (AMMs) are a cornerstone of decen-
tralised finance (DeFi). Constant product markets with concentrated
liquidity, such as UniswapV3, are now a well-established design. In
these markets, liquidity providers (LPs) face a sequential decision
problem: they must decide when to rebalance their positions and
which price ranges to allocate capital to as market conditions evolve.
We formulate dynamic liquidity provision as a stochastic impulse
control problem and use reinforcement learning (RL) to solve it, fo-
cusing on providing interpretable solutions. We show that learned
policies exhibit rich state-dependent behaviour, allocating liquidity
according to mispricing, rebalancing costs, uncertainty, inventory
exposure, and heterogeneous risk preferences. These behaviours
help compress the left tail of the Profit and Loss (PnL) distribution
and avoid catastrophic outcomes under high uncertainty. Finally,
we benchmark the RL agents against baseline and sophisticated
agents from the AMM microstructure literature and analyse their
performance.
1 Introduction
Decentralised finance (DeFi) has introduced financial exchanges in
which trading is executed by smart contracts. The most prominent
examples are automated market makers (AMMs), popularised by
Uniswap. Most AMMs are implemented as constant product mar-
kets (CPMs), a special class of constant function market makers
[3], where prices are determined algorithmically by an invariant
function and the reserves locked in the liquidity pool. In these mar-
kets, liquidity providers (LPs) deposit capital into a pool and earn
fees from users trading against it. While LPs were largely passive
in designs such as UniswapV2, the introduction of concentrated
liquidity (CL) in UniswapV3 significantly expanded their action
space, allowing them to allocate capital to specific price ranges [2].
CL changed the economics of liquidity provision. By concentrat-
ing capital around the current price, LPs can earn more trading
fees, but narrower positions stop earning fees once the price ex-
its the chosen interval. Hence, LPs face a trade-off between wide
positions, which cover more possible prices but earn lower fees,
and narrow positions, which are more profitable while active but
expose the LP to greater concentration risk. As prices evolve, LPs
can dynamically move their capital and create new positions, but
∗Authors contributed equally to the paper.
doing so incurs blockchain frictions, such as gas fees, and may
also require additional trades due to changes in the token composi-
tion of the new position. These costs must therefore be weighed
against the expected benefits of rebalancing. Thus, we formulate
optimal liquidity provision as a stochastic impulse control problem,
which includes stochastic order arrivals, price dynamics, and gas
costs. Since Hamilton-Jacobi-Bellman-Quasi-Variational Inequal-
ity (HJBQVI)-style methods are intractable in such realistic high-
dimensional settings, we employ reinforcement learning (RL) to
study dynamic liquidity provision strategies. Our objective is to pro-
vide a tractable computational representation of state-dependent
policies in settings where closed-form impulse-control solutions
are unavailable.
Our contribution.We make the following contributions.
• We show that learned policies generate rich and interpretable
liquidity provision strategies: agents adapt their rebalancing fre-
quency to blockchain frictions such as gas costs, while choosing
position width and asymmetry in response to their risk profile,
inventory holdings, existing deployed position, and the degree
and direction of arbitrage pressure in the market.
• We demonstrate a trade-off between narrow and flexible learned
strategies. Narrow-position agents achieve higher fee income
in risk-neutral settings but incur higher Impermanent Loss (IL)
and gas costs due to more frequent rebalancing, whereas wider-
position agents require less active risk management when inven-
tory risk is considered.
Related Work:Academic work on AMMs dates back to [ 22], but
AMMs saw widespread adoption more recently as a computation-
ally cheaper alternative to limit order books in blockchain-based
exchanges. Their use in decentralised exchanges was first proposed
in [9, 20], the latter introducing a CPM market maker. This mech-
anism was first analysed by [4], who identified conditions under
which such markets can closely track the price of an external refer-
ence market. Subsequently, [3] studied the broader class of constant
function market makers (CFMMs) and showed that they can incen-
tivise participants to reveal external market prices. Simple AMMs
such as UniswapV2 suffer from capital inefficiency. Newer proto-
cols such as UniswapV3 [2] address this issue through CL, which
allows LPs to specify the price ranges over which their liquidity is
active and gives them more granular control over fee generation.
Our work contributes to the work on profitable strategies for LPs
arXiv:2608.19389v1  [q-fin.TR]  19 Aug 2026

Chionas et al.
in CPMs with CL. In fact, empirical studies such as [ 14, 19, 21]
show that, currently, LPs are on average incurring a loss. [18] study
the risk-return trade-off faced by LPs in UniswapV3, while [ 17]
analyse optimal static liquidity provision and show how contract
design choices, affect LP profits and trader gas costs. More recently,
[11] decompose LP losses in concentrated-liquidity CPMs into con-
vexity costs, arising from the convexity of the pool invariant, and
opportunity costs, arising from locking assets in the pool instead
of investing them in a risk-free account. For dynamic liquidity
provision, [12] derive a closed-form solution for frictionless LP al-
locations, abstracting gas costs and latency, [16] use approximation
techniques to obtain profitable strategies, while [13] introduce a
broader family of AMMs, in which LPs participate in price discov-
ery. RL works for CL such as [23, 24] employ training in historical
data, while [6] uses a hybrid setup. Contributing to these efforts, our
work focuses primarily on a model-based approach that replicates
the full CL mechanics instead, allowing for state-dependent and
interpretable analyses in multiple economic regimes.
2 Preliminaries
Constant Product Markets.Let 𝑋 be a numéraire asset (e.g.
USDC) and𝑌 be a risky asset (e.g. ETH). A liquidity pool for the
pair of assets𝑋,𝑌 defines the marginal exchange rate of asset 𝑌
in units of asset𝑋 , denoted by𝑍. The state of a CPM is described
by the invariant function𝑓(𝑞 𝑋,𝑞𝑌)=𝑞 𝑋𝑞𝑌 =𝜅 2, where𝑞𝑋 and𝑞𝑌
are the reserves of assets𝑋 and𝑌 and𝜅 is the liquidity parameter
(depth) of the pool, a measure of its available liquidity. The invariant
function𝑓 connects the state of the CPM before and after a trade is
executed. The marginal exchange rate,𝑍, in a CPM is defined as
𝑍 :=𝑞 𝑋/𝑞𝑌 . In other words, the marginal exchange rate𝑍 is the
price quoted by the CPM at its current state for an infinitesimal
trade. Moreover, the CPM charges a fee,𝜏, proportional to the size
of the trade and thus,1−𝜏is the net percentage of the trade after
the trading fee.
Consider now a liquidity taker’s (LT) trade of size Δ𝑥 (i.e., the
LT provides Δ𝑥 units of asset𝑋 in exchange for asset𝑌 ). The LT
receives Δ𝑦′ units of asset𝑌 such that𝑓(𝑞 𝑋+( 1−𝜏)Δ𝑥,𝑞 𝑌−Δ𝑦′)=
𝑓(𝑞 𝑋,𝑞𝑌), which, for a CPM, implies thatΔ𝑦′ =𝑞𝑌− 𝑞𝑋𝑞𝑌 𝑞𝑋+(1−𝜏)Δ𝑥 .
Similarly, when the LT sells Δ𝑦 units of asset𝑌 , she receives Δ𝑥′
units of asset𝑋 such that𝑓(𝑞 𝑋−Δ𝑥′,𝑞𝑌+( 1−𝜏)Δ𝑦)=𝑓(𝑞 𝑋,𝑞𝑌),
which, for a CPM implies thatΔ𝑥′ =𝑞𝑋− 𝑞𝑋𝑞𝑌 𝑞𝑌+(1−𝜏)Δ𝑦 .
Concentrated Liquidity.In CPMs with CL, LPs can concentrate
their liquidity over a specific range of rates(𝑍ℓ,𝑍𝑢]. The rates𝑍ℓ
and𝑍 𝑢 take values from a discrete grid
{𝑍−𝑁 =𝑍,𝑍−𝑁+1,...,𝑍 0,...,𝑍 𝑁−1,𝑍 𝑁 =𝑍}(1)
where𝑁∈N 0. The smallest possible liquidity range is defined by
two consecutive ticks(𝑍𝑖,𝑍𝑖+1] and it is called atick range. Within
each tick range, the CPM with CL behaves locally as a CPM.
When an LP opens a new position, she specifies a range of rates
(𝑍ℓ,𝑍𝑢] and a liquidity depth ˜𝜅 (or liquidity units), which deter-
mines the quantities𝑥 and𝑦 in assets𝑋 and𝑌 respectively that the
LP should provide, namely
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
(2)
To obtain the total liquidity depth in a tick range, one needs to
sum the depths of the individual liquidity positions in the same
tick range. The formulas in (2) define a reparametrization whereby
the state of the CPM with CL can be fully described by the total
liquidity depth in each tick range and the marginal exchange rate.
This representation is more convenient since an LP action changes
the liquidity depths of the respective ticks, while an LT action
changes the marginal exchange rate𝑍.1 Lastly, the trading fees are
stored in each tick range, and are distributed pro-rata to each LP.
For example, if the LP’s position with depth ˜𝜅 is in a tick range
with total depth𝜅, then for every liquidity taking trade that pays in
fees an amount of𝑝, the LP earns the amount of ˜𝑝= ˜𝜅 𝜅𝑝1𝑍ℓ <𝑍≤𝑍𝑢 .
3 An impulse control formulation
Having introduced the mechanics of CPMs with CL, we now turn
to the dynamic liquidity provision problem faced by an individual
LP. In this problem, the LP observes the market conditions, which
are defined in the next paragraph, and decides when to close her
position and open a new one, i.e. when to rebalance, and what
the new position should be. When the LP rebalances, she collects
the accumulated fees from her last position and then reinvests
her initial wealth to the new position. Moreover, each rebalancing
incurs a fixed transaction cost, which captures the gas cost paid for
interacting with the blockchain, and for that reason, we formulate
the problem as an impulse control problem. 2 More formally, the
controller is an LP who, at a sequence of intervention times, chooses
a range of ticks from (1) to post her liquidity, with𝐿𝑡 =(𝐿 𝑖 𝑡)𝑁−1 𝑖=−𝑁
denoting the existing liquidity as a vector in the pool, excluding
the agent.3
We consider that the price formation of the risky asset 𝑌 is
exogenous to the CPM with CL and we denote its external midprice
at time𝑡as𝑆 𝑡 . The external midprice𝑆𝑡 follows the dynamics
𝑑𝑆𝑡 =𝜇𝑆 𝑡𝑑𝑡+𝜎𝑆 𝑡𝑑𝑊𝑡, 𝑆 0 >0,(3)
with drift𝜇, volatility𝜎> 0, and where𝑊𝑡 is a Brownian motion.
Concurrently, at each time 𝑡, the CPM with CL quotes its own
price for the risky asset𝑌 , the marginal exchange rate𝑍𝑡 . Thus, at
each time𝑡, there are two prices quoted for the risky asset𝑌 ; the
marginal exchange rate (the price quoted by the AMM) denoted by
𝑍𝑡 , and the external price, denoted by𝑆𝑡 .
In terms of the dynamics of the marginal exchange rate𝑍, we
assume it lives within the grid (1). In particular, when it is at tick
𝑖, an LT trade can only move it from 𝑍𝑖 to𝑍𝑖+1 or𝑍𝑖−1 provided
it stays in the grid. Hence, the marginal exchange rate𝑍 evolves
1For a more thorough treatment on the mechanics of CPMs with CL, see [2, 12]
2The difference between an impulse control problem and a continuous stochastic
control problem is that, in the former case, the controller takes actions occasionally
(interventions) because of the transaction costs, while in the latter case, the controller
takes actions continuously; cf. [15].
3For simplicity we take this liquidity vector to be deterministic; however, our RL
implementation supports Markovian stochastic counterparts.

Concentrated Liquidity Provision: a Reinforcement Learning Perspective
solely through LT trades, which constitute the order flow. More
precisely, letN+,𝑖 andN−,𝑖 denote the counting processes of trades
moving the marginal exchange rate from𝑍𝑖 to𝑍𝑖+1 and from𝑍𝑖+1
to𝑍𝑖, respectively. The total number of up/down movementsN±
is given byN± 𝑡 = ˝ 𝑖N±,𝑖 𝑡 .
We work under a probability measure P under which the count-
ing processesN± 𝑡 (counting the number of LT trades that move the
marginal exchange rate up/down in the grid (1)) have intensities
𝜆± 𝑡 =max n 𝜆0, 𝜆1±𝜆 2(𝑆𝑡−𝑍𝑡−) o ,(4)
where𝜆0 > 0and 𝜆1,𝜆 2≥ 0. The term 𝜆1 captures the baseline
order flow (i.e. the noise traders), while the term ±𝜆2(𝑆𝑡−𝑍 𝑡−)
captures arbitrage pressure. The term𝜆0 > 0is a safeguard param-
eter to prevent intensities from becoming negative. This model for
intensities has been studied previously in [5].
The LP’s filtration (the LP’s observable information when taking
new actions) will be generated by𝑆𝑡 andN± 𝑡 , sinceN±,𝑖 𝑡 is deter-
mined byN± 𝑡 and the marginal exchange rate𝑍𝑡 . Hence, the LP’s
control is an impulse strategy
𝛼:= 𝑟𝑛,𝑍 ℓ 𝑛,𝑍𝑢 𝑛  𝑛≥1,(5)
where(𝑟𝑛)𝑛≥1 is an increasing sequence of stopping times and, at
each intervention time𝑟𝑛, the LP chooses a lower and an upper tick
satisfying𝑍 ≤𝑍 ℓ 𝑛 <𝑍 𝑢 𝑛≤𝑍.
The pair(𝑍ℓ 𝑛,𝑍𝑢 𝑛] specifies the liquidity range until the next
intervention. Equivalently, if𝑖𝑡 denotes the active tick at time𝑡, the
LP’s liquidity vector is
˜𝐿𝛼,𝑖 𝑡 = ˜𝜅𝛼 𝑡 1{𝑍ℓ 𝑡 <𝑍𝑖𝑡≤𝑍𝑖𝑡+1≤𝑍𝑢 𝑡}, 𝑖=−𝑁,...,𝑁−1,(6)
where ˜𝜅𝛼 𝑡 is the liquidity depth deployed in the selected range,
determined by the LP’s available capital at rebalancing and the
value per liquidity unit in that range. We then define the total
liquidity depth in tick range(𝑍 𝑖,𝑍𝑖+1]by𝜅 𝛼,𝑖 𝑡 :=𝐿𝑖 𝑡+ ˜𝐿𝛼,𝑖 𝑡 .
The fees collected by the LP are proportional to her share of
liquidity in the current tick. Thus, for a fee rate 𝜏∈ ( 0, 1), the
cumulative fee process is
𝑃𝛼 𝑡 = ˝𝑁−1 𝑖=−𝑁 h∫ 𝑡 0 ˜𝐿𝛼,𝑖 𝑠− 𝜅𝛼,𝑖 𝑠−  𝜏 1−𝜏  Δ𝑥𝑖 𝑠𝑑N+,𝑖 𝑠 + ∫ 𝑡 0 ˜𝐿𝛼,𝑖 𝑠− 𝜅𝛼,𝑖 𝑠−  𝜏 1−𝜏 𝑆𝑠 Δ𝑦𝑖 𝑠𝑑N−,𝑖 𝑠 i
where Δ𝑥𝑖 𝑠 and Δ𝑦𝑖 𝑠 are the trade sizes required to move the mar-
ginal exchange rate by one tick in the corresponding direction.
The dependence on the chosen width enters through ˜𝐿𝛼,𝑖 : for fixed
amounts of capital, a narrower range creates a larger liquidity share
in the active tick, while a wider range lowers the share but remains
active in more price states. In our setup, each intervention incurs
a fixed transaction cost; this is a key distinction from the friction-
less case in [12]. When the LP changes her position at time𝑟𝑛, she
pays a fixed gas cost. We write the cumulative cost up to time𝑡 as
𝐶𝛼 𝑡 = ˝ 𝑟𝑛≤𝑡𝑔, where𝑔>0is the gas cost for each new LP action.
Let𝑉𝛼 𝑡 be the value of the LP’s current position in units of asset
𝑋 at the current external price, i.e. 𝑉𝛼 𝑡 =𝑥 𝛼 𝑡 +𝑆 𝑡𝑦𝛼 𝑡 . Relative to
holding the initial token amounts outside the pool, the realised IL
term isIL𝛼 𝑡 =− h 𝑉𝛼 𝑡 − 𝑥𝛼 0+𝑆𝑡𝑦𝛼 0 i . The risk-neutral LP solves
sup
𝛼∈A
EP𝛼  𝑃𝛼 𝑇−IL𝛼 𝑇−𝐶𝛼 𝑇  .(7)
where𝑃𝛼 𝑇 denotes collected fees, IL𝛼 𝑇 denotes impermanent loss,
and𝐶𝛼 𝑇 denotes rebalancing costs.
The problem therefore captures the main trade-off faced by a LP
in a CPM with CL; narrow ranges increase the fee share conditional
on being active, but expose the position to concentration risk and
more frequent rebalancing, while wider ranges lower the fee share
but reduce the probability of falling out of range. The impulse
structure makes the rebalancing friction explicit.
Risk Aversion through Running Inventory Penalty.Besides
the risk neutral case defined in (7), we will modulate the perfor-
mance of the LP under different levels of risk aversion. The simplest
way to introduce risk aversion is through an inventory penalty. We
therefore extend the objective function in (7) as follows
sup
𝛼∈A
EP𝛼

𝑃𝛼 𝑇−IL𝛼 𝑇−𝐶𝛼 𝑇−𝜙
∫ 𝑇
0
(𝑦𝛼 𝑡 − ˆ𝑦) 2𝑑𝑡

,(8)
where the constant𝜙∈R + determine the running penalty deviat-
ing from some level ˆ𝑦 (see [13]). In particular, the LP’s performance
criterion (8) aims to maintain a target reserve level ˆ𝑦. Note that
without a target reserve ˆ𝑦, the performance criterion would es-
sentially force the LP to liquidate the risky asset that she holds.
It is well-known in the algorithmic trading literature (as shown
in [10]) that the running penalty term in (8) can be interpreted as
arising from the agent’s ambiguity aversion with respect to the
external price𝑆𝑡 . As we show in Section 4, the per-step running
inventory penalty is the main component pushing the LP towards
wider positions.
Theoretical Results.Two structural properties of the LP’s PnL
follow directly from the CL mechanics of Section 2, and both are
used to interpret the learned policies in Section 4.
Lemma 3.1(Fee revenue is linear in own liquidity).Under one-
tick jumps, the fees collected by an individual LP are linear in ˜𝜅 and
independent of the other LPs liquidity𝐿 𝑖 in the pool.
Proof Sketch. Moving from𝑍𝑖 to𝑍𝑖+1 requires an after-fee
trade of size Δ𝑥𝑖 =𝜅𝑖(𝑍𝑖+1)1/2−(𝑍 𝑖)1/2 in𝑋 , and symmetrically
Δ𝑦𝑖 =𝜅𝑖(𝑍𝑖)−1/2−(𝑍 𝑖+1)−1/2 in𝑌 in the opposite direction: the
volume needed to cross a tick is proportional to thetotaldepth
𝜅𝑖 of that tick. Since the LP earns the pro-rata share ˜𝜅𝑖/𝜅𝑖 of the
resulting fee,𝜅𝑖 cancels in the LP’s fee revenue process𝑃𝛼 𝑡 , leaving
an integrand proportional to ˜𝜅𝑖 𝑠− and free of𝐿𝑖. Deeper liquidity
in a range absorbs more volume per tick crossed, and the pro-rata
rule returns to the LP exactly her share of that extra volume.□
Lemma 3.2(IL is linear in own liquidity).For a position of depth ˜𝜅
in(𝑍 ℓ,𝑍𝑢], the IL between posting and withdrawal is linear in ˜𝜅.
Proof Sketch. Every branch of (2) is positively homogeneous
of degree one in˜𝜅, so𝑥𝑡 ,𝑦𝑡 , and henceIL𝑡 =−

𝑥𝑡+𝑦𝑡𝑆𝑡−(𝑥 0+𝑦0𝑆𝑡)

,
are linear in ˜𝜅, whether or not the position is in range. While
𝑍𝑡∈(𝑍 ℓ,𝑍𝑢] the boundary terms cancel and IL𝑡 = ˜𝜅  𝑍 1/2 0 −𝑍 1/2 𝑡 +
𝑆𝑡
𝑍−1/2 0 −𝑍−1/2 𝑡  , so the range enters only through ˜𝜅. For fixed
capital, a narrower range implies a larger ˜𝜅, which makes the IL
curve locally steeper, showing the cost side of concentration.□
From Theorem 3.1 and Theorem 3.2, we thus have:
Theorem 3.3(Affinity of the LP’s PnL in liquidity).The LP’s PnL
𝑃𝛼 𝑇−IL𝛼 𝑇−𝐶𝛼 𝑇 is affine in ˜𝜅: it is linear through the fee and IL terms,
while the gas cost𝐶 𝛼 𝑇 enters as a ˜𝜅-independent constant.

Chionas et al.
These results assume an LP whose liquidity is small relative
to the pool, so that her actions do not affect the liquidity taking
activity in the future.
Learning Agents as Dynamic LPs.The impulse control problems
in (7) and (8) are analytically intractable in realistic settings, since
the LP must jointly decide when to intervene and where to deploy
liquidity under stochastic prices, order arrivals, gas costs, inventory
exposure, and a discrete tick grid. RL provides a natural numerical
approach for learning admissible strategies of the form (5), with
rewards defined as sample-path counterparts of the objectives inside
the supremum. For a risk-neutral LP, the reward is realised PnL
from fees, IL, and rebalancing costs, corresponding to (7); for a risk-
averse LP, we use the inventory-penalised criterion in (8), where𝜙
controls the degree of risk aversion.
The mechanics and frictions of CL, together with Theorem 3.3,
imply the key economic trade-off studied in our experiments. Nar-
rower ranges increase fee income conditional on being active but
expose the LP to concentration risk and costly rebalancing; wider
ranges remain active over more price states and reduce out-of-range
and inventory risk, but dilute liquidity across ticks and lower the
LP’s fee share per tick. In the risk-neutral case, the linearity of fee
revenue and IL in the LP’s own liquidity implies a strong incen-
tive to concentrate liquidity in the expected most profitable tick
range, providing a theoretical benchmark for studying risk aversion,
inventory penalties, and rebalancing frictions.
We therefore consider two action parametrisations. A flexible
agent that freely chooses the lower and upper bounds(𝑍ℓ 𝑛,𝑍𝑢 𝑛] and
a narrow agent with the minimum fixed position width of two
ticks(𝑍𝑖 𝑛,𝑍𝑖+2 𝑛 ] that learns only where to place her liquidity. The
narrow specification isolates the value of learningwhereto post
liquidity from the value of learninghow widethe position should
be. Decisions are made only at intervention times, consistent with
the impulse-control formulation and with the fact that continuous
rebalancing is unrealistic under blockchain frictions.
4 Experimental Results
Based on the above, in the following experiments, we implement
two RL agents with the Proximal Policy Optimisation (PPO) algo-
rithm, namely the PPO and PPO_narrow. For the action space, when
(𝑍ℓ 𝑛+1,𝑍𝑢 𝑛+1]=(𝑍 ℓ 𝑛,𝑍𝑢 𝑛], the agent chooses to hold her previous po-
sition, and thus no extra gas costs are charged. For the first action,
if(𝑍ℓ 0,𝑍𝑢 0]=( 0, 0] the agent chooses not to provide liquidity. The
observation space contains the main variables needed for liquidity
provision: mispricing𝑆𝑡−𝑍𝑡 , distances from the current pool price
to the position boundaries, time, gas cost, cumulative fee income,
and the LP’s current holdings in the risky and numéraire assets.
In our experiments, each trained policy and benchmark strategy
is evaluated on 1000 independent simulations using random seeds
distinct from those used during training. We compare strategies
across scenarios and profile the learned policies as state-dependent
functions, relating their behaviour to empirical liquidity-provision
patterns. The aim is to understand how learned LP policies adapt
their position width, asymmetry, and rebalancing frequency to the
LP’s risk appetite and to the stochastic and blockchain-specific
properties of the environment.
Experimental Setup:We train and evaluate PPO and PPO_narrow,
in the stochastic environment of Section 3. The external price of
the risky asset𝑌 (e.g. ETH) follows the geometric Brownian mo-
tion in (3). The liquidity-taking arrivals follow the linear intensity
model in (4), for which we set𝜆1 = 15and 𝜆2 = 4000. These values
represent an order-flow intensity that is mainly driven by arbi-
trage pressure from deviations between the pool price and the
external price. Equations (3) and (4) are the two sources of stochas-
ticity in the experiments. For the external price, we set𝑆0 = 1000,
𝑑𝑡= 0.001(assuming 𝑇= 1), 𝜇= 0, and vary volatility over
𝜎∈{0.005,0.01,0.015,0.02,0.025,0.03} . Higher𝜎 increases the like-
lihood of sharp price movements, IL, and positions moving out of
range. The main blockchain friction is the gas cost paid at each
rebalance, for which we consider𝑔∈{2,4,6} , corresponding to low,
medium, and high operational costs. We train both risk-neutral and
risk-averse LPs: risk-neutral agents use the cumulative PnL reward
in (7), while risk-averse agents use the inventory-penalised reward
in (8), with𝜙∈{ 20, 50, 80} controlling the strength of inventory
risk aversion. As observed in practice, the pool price 𝑍𝑡 follows
closely𝑆𝑡 due to arbitrage. Therefore, we set the parameters of𝑆𝑡
within the range of empirical estimations calculated in [12]. The
rest of the parameters were calibrated to be economically sensible
based on the above within our model-based setup. The action range
is restricted to[−15, 15] ticks around the current tick. Each LP starts
with 1000 numéraire units, and the proportional fee tier is set to
𝜏=0.3%, a standard UniswapV3 fee tier for token pairs.
We benchmark PPO and PPO_narrow against rule-based and
model-based strategies operating within the same [−15, 15] tick
window. TheDeployOnceAgentdeploys capital at the start and never
rebalances. We use two variants:DeployNarrow, which deploys over
[−1, 1] around the initial pool price, andDeployWide, which deploys
over[−15, 15]. The former represents the narrow single-shot alloca-
tion motivated by the concentration incentives in Section 3, while
the latter maximises the probability of remaining active through-
out the simulation. TheArrivalRebalanceAgentalso posts liquidity
over[−1, 1], but rebalances after every 𝑁𝑎𝑟𝑟 liquidity-taking ar-
rivals, adding a simple timing rule relative toDeployNarrow. Finally,
we compare against theCarteaDrissiMongaAgent(CDM), a model-
based closed-form strategy for concentrated AMMs based on [12].
Each trained RL agent corresponds to an independent environ-
ment instance, giving 72 scenarios in total (6· 3· 4) across𝜎,𝑔, and
risk-aversion settings. To ensure statistical robustness across the
training variability of the RL algorithms, each scenario is assessed
across 10 different training seeds. To reduce policy-gradient vari-
ance and expose policies to a broad state distribution, we collect
rollouts using 𝑁traj,train = 200parallel trajectories advanced syn-
chronously. Each trajectory has𝑁steps = 1000environment steps,
with intervention times every𝐾dec = 100steps. Thus, each rollout
contains𝑁traj,train𝑁steps/𝐾dec = 2000agent-decision transitions. We
set𝐸 train =300, yielding a total training budget of6×10 5
agent-decision transitions for the PPO optimisation objective, after
which average returns stabilise without material performance gains
from further training. For the RL architecture we set: learning rate
= 3× 10−4, batch size = 200,𝛾= 0.99, GAE𝜆= 0.95, clip range
=0.15, entropy=0.03and two hidden MLP layers of 256 units.

Concentrated Liquidity Provision: a Reinforcement Learning Perspective
Table 1: Mean PnL and5%CVaR in USDC over 1000 com-
mon evaluation trajectories. Values following± denote the
standard deviation across 10 independently trained policies.
Bold marks the best RL and benchmark method. 𝑝 tests their
difference, treating training seeds as replication units and
additionally propagating trajectory sampling error.
𝜎=0.01, 𝑔=2𝜎=0.02, 𝑔=4
Agent PnL CVaR PnL CVaR
DeployNarrow 15.85 -14.52 6.48 -35.37
DeployWide 12.78 -15.11 4.09 -36.48
ArrivalRebalance49.726.86 5.69 -36.23
CDM 35.1811.55 15.01 -26.23
Risk neutral
PPO 42.31±0.97 6.08±0.97 5.33±0.65 -36.51±0.77
PPO_narrow49.91±0.389.15±0.656.51±0.20-35.69±0.42
𝑝0.81 0.0014<10 −10 <10−4
Risk averse (𝜙=50)
PPO 30.36±1.60 3.07±1.56 1.49±0.16 -9.14±0.46
PPO_narrow 46.11±0.679.32±0.742.27±0.40-8.86±0.87
𝑝<10 −10 0.04<10 −10 <10−4
Table 2: Under adversarial conditions ( 𝜎= 0.03,𝑔= 6), the
risk-averse RL agents learn mainly not to deploy.
𝜎=0.03, 𝑔=6
Agent PnL CVaR
DeployNarrow0.10 -56.17
DeployWide -2.12 -57.33
ArrivalRebalance -5.38 -62.64
CDM -3.10 -56.93
Risk neutral Risk averse (𝜙=50)
PPO -1.42±0.80 -54.78±6.610.00±0.04-0.68±1.47
PPO_narrow -0.06±0.56 -52.68±7.73 -0.01±0.03-0.16±0.51
𝑝0.64 0.19 0.88<10 −4
Performance of Learned Policies:Tables 1 and 2 compare the
performance of the RL agents and the benchmark strategies across
representative market settings chosen as a coherent regime ladder,
corresponding to low, medium, and high combinations of𝜎 and𝑔,
under both risk neutrality and an intermediate level of risk aversion
(𝜙= 50). The significance tests for PnL use a hierarchical paired
𝑡-test and for CVaR, a paired bootstrap over both seeds and tra-
jectories (104 replicates). CDM does not directly account gas costs.
Thus, for an optimistic frictionless analytical benchmark version
against the RL agents, we consider that the strategy rebalances
every𝐾𝑑𝑒𝑐 free of costs. Its risk aversion lies in its formulation that
depends on𝜎. For the ArrivalRebalance agent, we finetuned𝑁𝑎𝑟𝑟
for each scenario from a gridsearch ranging from𝑁𝑎𝑟𝑟 = 10to800,
optimising both PnL and CVaR (Conditional Value at Risk).
Under the low-volatility, low-gas setting, for the risk neutral case,
PPO_narrow achieves similar PnL with ArrivalRebalance, however
with higher CVaR than it, resulting in a better overall strategy.
Figure 1: Differences in the mean decomposed PnL compo-
nents between the RL agents across volatility, by risk profile
(rows) and gas cost (columns). ΔNet PnL=ΔFees+(−ΔIL)+
(−ΔGas)=PPO_narrow(PnL)−PPO(PnL) denotes the differ-
ence in mean PnL and is shown by the diamond marker. A
positive ΔFees (green), negative−ΔIL (purple), and negative
−ΔGas (orange) indicate that PPO_narrow earns more fees,
incurs greater IL, and pays more gas than PPO, respectively.
Each quantity is averaged over 1,000 trajectories. Missing
bars indicate that one or both agents did not deploy.
CDM achieves slightly improved CVaR than the risk averse agent,
however the PnL of PPO_narrow is better even though gas costs
were paid for its positions. As volatility and gas costs increase, prof-
itability declines across all strategies, and the mean-PnL advantage
of the RL agents becomes less pronounced.
CDM outperforms (with significant𝑝 values) in PnL both risk-
neutral and risk averse agents under the medium volatility con-
dition. However, the risk aversion case clearly demonstrates the
benefits of the RL agents under these market conditions. At𝜎= 0.02
and𝑔= 4, the risk-averse RL agents achieve substantially improved
CVaR than CDM. Relative to their risk-neutral counterparts under
the same market conditions, they sacrifice approximately 4 USDC
in mean PnL while improving CVaR by approximately 27 USDC,
illustrating their ability to trade modest expected profitability for
substantially stronger downside protection, reducing extreme losses
as market conditions deteriorate. At𝜎= 0.03and 𝑔= 6, the risk-
averse agents learn mostly not to deploy liquidity, approximating
a "DoNothing" benchmark that would report PnL= 0and CVaR =
0. Thus, under sufficiently adverse conditions, the economically
meaningful learned behaviour is endogenous market exit rather
than superior active liquidity management. Finally, the relatively
small standard deviations across independently trained policies
indicate stable training outcomes.
As discussed, PPO_narrow generally achieves better performance
than PPO because its fixed narrow range gives it the theoretically
favourable concentration implied by Theorem 3.3. However, by
decomposing the PnL of the agents, we notice that this advantage

Chionas et al.
(a) Mean Spreads in ticks of the two RL agents. The shaded area
corresponds to the±1standard deviation around the mean.
(b) Rebalancing Rate (%) of the RL agents.
Figure 2: Position width and rebalancing behaviour of PPO
and PPO_narrow. Panel (a) shows mean quoted width, while
Panel (b) shows per-decision rebalance rates. Labels and Leg-
ends as in Figure 1.
comes with higher IL and gas costs (Figure 1), since narrow positions
require more frequent rebalancing. Therefore, when risk aversion
is taken into account; by learning wider positions, PPO has lower
fee intensity but less active risk management. This mechanism is
confirmed in Figure 2. PPO systematically increases its average
width as volatility, gas costs, and risk aversion rise, provided that
the average rebalancing rate is not near zero. Both agents reduce
their rebalancing frequency across these dimensions. PPO_narrow
rebalances more often on average, reflecting the greater manage-
ment required by fixed concentrated positions. Note that PPO_narrow
incurs lower IL and gas costs in the few instances where PPO had a
Figure 3: Liquidity provision behaviour of all strategies for
one random simulation from the evaluation trajectories (sce-
nario:𝜎= 0.01,𝑔= 2, risk neutral agents). The red thin vertical
lines show when agents rebalance.
Figure 4: Illustration of the empirical CL shapes around pool
prices (left) in our model-based environment (right). Left
figure shows the normalised liquidity distribution around
the current tick for Optimism (red), Arbitrum (black) and
Ethereum (purple) as observed from real on-chain data cal-
culated in [ 1]. Right figure shows a superposition of all four
PPO risk-profile agents, PPO_narrow, and a wide background
liquidity. Each agent’s position is her reported average width
for𝜎=0.02and𝑔=2with indicative relative wealths.
higher rebalance rate, as shown in Figure 2b. Figure 3 provides an
example of how agents provide liquidity, for high level intuition.
A Qualitative Illustration of Aggregate Liquidity Shapes:
The results of Figure 2a show that the learned width of the PPO
agent varies systematically with the LP’s risk profile and the fric-
tions of the environment. This provides a natural qualitative in-
terpretation of the liquidity concentration observed empirically
around the pool prices in real concentrated AMM pools as the
aggregate result of heterogeneous LPs with different risk appetites.
Figure 4 illustrates this mechanism by superimposing the average
positions of PPO agents trained with different risk profiles and a
wide passive existing background liquidity component. The result-
ing aggregate allocation forms a bell-shaped liquidity profile around
the current pool price, providing a model-based illustration of the

Concentrated Liquidity Provision: a Reinforcement Learning Perspective
(a) The agent repositions liquidity closer
to the external price due to the expected
arbitrage flow.
(b) The agent’s size of the chosen width de-
pends on the amount of risky token held,
functioning as a risk-management device.
(c) For𝑆−𝑍> 0the agent chooses to hold
her position to get rid of the risky asset
from the expected incoming trades.
Figure 5: The full action response that a risk-averse PPO agent has for fixed wealth, with 𝜙= 50for 𝑔𝑎𝑠_𝑐𝑜𝑠𝑡= 4and 𝜎= 0.01
at𝑡= 0.4, across two important dimensions: the amount of the risky asset she holds (e.g. ETH), and the adversarial signal
(mispricing). It is assumed that the current action of the agent is a symmetrical narrow position (-1,1) around the current tick.
The shaded areas in the first two plots are where the agent holds her existing position and the chosen actions can be ignored.
Figure 6: Action responses of the risk-neutral PPO_narrow
agent for 𝜎= 0.01with gas cost 𝑔= 2(left panel) and 𝑔= 6
(right panel) at time 𝑡= 0.4. The x-axis shows the mispricing
(USDC), while the y-axis shows the policy output, i.e. the
chosen range centre. The colour bar indicates the current
centre (ticks). Both the chosen action and current state are
expressed as centre offsets. Dark purple denotes a position
well below the current tick, bright yellow well above it, and
teal positions partially in range. Solid line segments indicate
rebalancing; dashed segments indicate that the agent ignores
its centre output and holds its position.
real liquidity concentration patterns observed in DeFi pools. Flat-
ter empirical distributions, such as the one observed on Ethereum,
can therefore be associated with stronger risk aversion, higher gas
costs or heterogeneous individual LP objectives. Analogously, the
liquidity distribution of Optimism and Arbitrum can be thought
qualitatively as the superposition of LPs that are more risk seeking
in their approach of capturing the fee share of incoming trades
by narrowing their quotes, resembling our theory informed RL
agent. In this sense, the shape of liquidity in concentrated AMMs
reflects both the local fee incentives of CL and the idiosyncratic
risk-management behaviours of the LP population.
Profiling Learned Policies as State-Dependent Functions:
Figure 5 and 6 examine the policies as state functions to explain
how the agents condition their actions on the observed state. Figure
6 shows the response of the optimal risk-neutral PPO_narrow agent.
Since this agent has a fixed two-tick width, the relevant decisions
are where to centre the position and whether or not to rebalance. In
the low gas-cost case (left subplot), the agent rebalances positions
that are far out of range and places liquidity in the direction of
expected arbitrage flow. Specifically, when mispricing is relatively
small (-1,1) the positions that are deeply out of range (bold yellow
and purple) get rebalanced near the current centre, adjusted to the
direction of the arbitrage. However, when the current position is
already favourably placed, the agent often chooses to hold, since
rebalancing would require paying an additional gas cost. When
mispricing is large, the out of range positions get rebalanced and
their liquidity is placed again in the direction of the arbitrage how-
ever, with heavier asymmetry towards the external price to achieve
better rates while collecting the fees. The positions that are already
in the direction of the arbitrage (e.g. purple lines with𝑆−𝑍< 0
and, conversely, yellow lines with𝑆−𝑍> 0) are not rebalanced.
The existing placement is expected to yield higher fees collected
than rebalancing closer to𝑆, due to incurred gas costs.
The high gas-cost case (right subplot) demonstrates that this
behaviour changes sharply when intervention becomes expensive.
All lines are dashed, which means that the agent holds her current
position (even with large mispricing signal) and the chosen centre
output can be ignored. Thus, high gas costs not only reduce PnL
mechanically but also expand the inaction region. The cost of re-
balancing to correct her position will be larger than the expected
profit, in contrast to the left subplot, where the gas cost was lower.
Figure 5 reports the corresponding state-function analysis for a
risk-averse PPO agent. PPO controls with her actions𝑍ℓ 𝑛,𝑍𝑢 𝑛 essen-
tially both where (i.e. the centre defined as𝑍𝑐 𝑛 := 𝑍ℓ𝑛+𝑍𝑢𝑛 2 ) and how
wide (i.e. a symmetrical half-width |𝑍𝑢𝑛−𝑍ℓ𝑛| 2 around𝑍𝑐) to place
her liquidity. The figure shows how the policy responds jointly to
mispricing and inventory holdings. Specifically, Figure 5a shows
that when𝑆−𝑍< 0, the agent repositions the centre of her liq-
uidity towards the external price, independently of the amount of
ETH held. In doing so, she collects fees from the arbitrage flow,
while avoiding exchanging her liquidity in the worst possible rate
(the current one) due to the expected incoming arbitrage trades.

Chionas et al.
However, as shown in Figure 5b with𝑆−𝑍< 0, the chosen width
varies with the amount of ETH held. For low ETH (i.e. more USDC)
holdings, the agent widens her position reflecting her risk man-
agement. She dilutes USDC capital across the arbitrage direction,
reducing exposure to unfavourable prices. For higher ETH holdings
(less USDC), she identifies the profitable rates, resulting in a more
concentrated but still wide position. Lastly, Figure 5c shows that for
𝑆−𝑍> 0the agent chooses to hold her asset at (-1,1) around the
current tick and wait for trades towards the direction of the arbi-
trage. As a risk-averse agent, she prefers to take the trade because
she will exchange the risky token for the safe token (numéraire).
Overall, Figures 5 and 6 show that the learned policies are eco-
nomically interpretable: they use mispricing to infer order-flow
direction, gas costs to decide whether intervention is worthwhile,
and inventory holdings to control risk.
5 Limitations
Our analysis is deliberately scoped to a controlled, model-based set-
ting. Each RL policy is evaluated in the same stationary economic
regime in which it is trained, allowing us to isolate and interpret
learned economic mechanisms without confounding them with
regime-detection or adaptation errors. The results should therefore
be understood as conditional on correctly identified, approximately
stationary transition dynamics. The benchmarks are constrained
by the concentrated-liquidity literature. We compare the RL agents
with tuned static and rebalancing heuristics and with the principal
analytical strategy available for CPM liquidity provision. We do
not claim universal superiority of RL; rather, we show that it can
produce interpretable, state-dependent policies where closed-form
solutions are generally unavailable. These policies may serve as re-
producible model-based references for future work. The continuous-
time impulse-control problem is implemented with discrete decision
opportunities, reflecting the discrete execution of on-chain transac-
tions. The reported policies, therefore, solve the discretized problem
induced by the chosen decision frequency, not the exact continuous-
time formulation. Finally, the superposition experiment shows that
heterogeneous risk preferences can resemble liquidity patterns like
those in concentrated-liquidity pools, without identifying them as a
unique explanation. An empirical approach would require on-chain
data analysis, which is beyond the scope of this work.
6 Conclusion
We studied dynamic liquidity provision in AMMs with CL through
an RL perspective. We formulated the LP’s problem as a stochastic
impulse control problem, where the LP jointly decides when to re-
balance and where to allocate her capital under price uncertainty, ar-
bitrage trades, and operational frictions while managing inventory
risk. Due to the analytical intractability of the problem we employed
RL algorithms to obtain interpretable state-dependent policies. The
results show that learned policies recover economically meaningful
behaviour with complex state-dependent strategies. Higher volatil-
ity and gas costs reduce average PnL, while stronger risk aversion
compresses the left tail of the PnL distribution by inducing wider
positions and lower rebalancing rates. Overall, the learned policies
adapt their position centre, width, and intervention decision to the
state of the market. Lastly, by superimposing learned policies with
heterogeneous risk profiles, our modelling provides one possible
mechanism capable of generating qualitatively similar concentra-
tion patterns with bell-shaped liquidity distributions around the
pool prices that are observed in real DeFi exchanges. Future work
could extend to multi-agent competition among heterogeneous LPs
[8], and AMM designs with dynamic trading fees [7].
References
[1] Austin Adams. 2024. Layer 2 be or Layer not 2 be: Scaling on Uniswap v3.
arXiv:2403.09494 [q-fin.TR]
[2] Hayden Adams, Noah Zinsmeister, Moody Saleh, River Keefer, and Dan Robinson.
2021. Uniswap v3 Whitepaper.
[3] Guillermo Angeris and Tarun Chitra. 2020. Improved Price Oracles: Constant
Function Market Makers. InProceedings of the 2nd ACM AFT Conference(New
York, NY, USA)(AFT ’20). 80–91. doi:10.1145/3419614.3423251
[4] Guillermo Angeris, Hsien-Tang Kao, Rei Chiang, Charlie Noyes, and Tarun Chitra.
2021. An Analysis of Uniswap Markets.Cryptoeconomic Systems(2021).
[5] Alif Aqsha, Philippe Bergault, and Leandro Sánchez-Betancourt. 2026. Equilib-
rium Reward for Liquidity Providers in Automated Market Makers.Mathematical
Finance, to appear, arXiv:2503.22502(2026).
[6] Ricardo Arcifa, Yuhang Ye, Yuansong Qiao, and Brian Lee. 2025. Optimizing Con-
centrated Liquidity Management: A Synthetic-to-Historical Deep Reinforcement
Learning Strategy. In2025 IEEE International Conference on Decentralized Appli-
cations and Infrastructures (DAPPS). 83–90. doi:10.1109/DAPPS65174.2025.00019
[7] Leonardo Baggiani, Martin Herdegen, and Leandro Sánchez-Betancourt. 2025.
Optimal dynamic fees in automated market makers.arXiv:2506.02869(2025).
[8] Leonardo Baggiani, Martin Herdegen, and Leandro Sanchez-Betancourt. 2026.
Competition between DEXs through Dynamic Fees.arXiv:2603.09669(2026).
[9] Vitalik Buterin. 2016.Let’s Run On-Chain Decentralized Exchanges the Way We
Run Prediction Markets. https://shorturl.at/oV8qn
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
[14] Daniele Maria Di Nosse, Federico Gatta, Fabrizio Lillo, and Sebastian Jaimun-
gal. 2025. Deviations from Tradition: Stylized Facts in the Era of DeFi.
arXiv:2510.22834(2025).
[15] Jerome F. Eastham and Kevin J. Hastings. 1988. Optimal Impulse Control of
Portfolios.Mathematics of Operations Research13, 4 (1988), 588–605. doi:10.1287/
moor.13.4.588
[16] Zhou Fan, Francisco Marmolejo-Cossio, Daniel Moroz, Michael Neuder, Rithvik
Rao, and David C. Parkes. 2023. Strategic Liquidity Provision in Uniswap V3.
In5th ACM AFT Conference (AFT 2023), Vol. 282. 25:1–25:22. doi:10.4230/LIPIcs.
AFT.2023.25
[17] Zhou Fan, Francisco J Marmolejo-Cossío, Ben Altschuler, He Sun, Xintong Wang,
and David Parkes. 2022. Differential Liquidity Provision in Uniswap v3 and
Implications for Contract Design. InProceedings of the Third ACM International
Conference on AI in Finance. 9–17.
[18] Lioba Heimbach, Eric Schertenleib, and Roger Wattenhofer. 2022. Risks and re-
turns of uniswap v3 liquidity providers. InProceedings of the 4th ACM Conference
on Advances in Financial Technologies. 89–101.
[19] Stefan Loesch, Nate Hindman, Mark B Richardson, and Nicholas Welch. 2021.
Impermanent Loss in Uniswap v3. arXiv:2111.09192 [q-fin.TR]
[20] Alan Lu and Martin Köppelmann. 2017.Building a Decentralized Exchange in
Ethereum. https://shorturl.at/yAVa8
[21] Jason Milionis, Ciamac C. Moallemi, Tim Roughgarden, and Anthony Lee
Zhang. 2024. Automated Market Making and Loss-Versus-Rebalancing.
arXiv:2208.06046 [q-fin.MF] https://arxiv.org/abs/2208.06046
[22] Abraham Othman and Tuomas Sandholm. 2010. Automated Market-Making in
the Large: The Gates Hillman Prediction Market. InProceedings of the 11th ACM
Conference on Electronic Commerce. 367–376.
[23] Haonan Xu and Alessio Brini. 2025. Improving DeFi Accessibility
through Efficient Liquidity Provisioning with Deep Reinforcement Learning.
arXiv:2501.07508 [q-fin.CP]
[24] Haochen Zhang, Xi Chen, and Lin F. Yang. 2023. Adaptive Liquidity Provision
in Uniswap V3 with Deep Reinforcement Learning. arXiv:2309.10129 [cs.AI]
