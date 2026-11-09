---
title: 'Proof-of-Stake Dynamics: The Elusive Price Anchor and Endogenous Volatility Harvesting'
url: https://arxiv.org/abs/2607.16622
category: consumer-behavior
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Mikhail Perepelitsa
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.16622
pages: 20
chars: 43020
fetched_at: '2026-11-08T13:01:40+00:00'
kb_version: 1
---

# Proof-of-Stake Dynamics: The Elusive Price Anchor and Endogenous Volatility Harvesting

Proof-of-Stake Dynamics: The Elusive Price Anchor and
Endogenous Volatility Harvesting
Mikhail Perepelitsa
University of Houston
3551 Cullen Blvd, PGH
Houston, TX 77204-3008, USA
Abstract
In this paper, we develop an open-economy macroeconomic model of a Proof-of-
Stake network to analyze nominal token-price dynamics and the systemic effects of
speculative capital.
We first consider a network populated solely by active utility users, who finance
network activity through a steady exogenous inflow of fiat currency. We prove the
existence of a unique, globally asymptotically stable steady-state equilibrium with a
well-defined nominal token price and derive a closed-form expression for the network’s
relaxation time. Calibrating the model using parameters representative of the cur-
rent Ethereum network, we estimate a relaxation half-life of approximately 46 years.
This extreme macroeconomic inertia implies that the token price may remain persis-
tently displaced from its evolving steady-state benchmark, producing sustained price
overshooting as the network adjusts to changing fundamentals.
We then introduce an Investor class to examine the effects of passive and active
speculative capital. We show that passive institutional staking compresses the native
staking yield and creates a structural imbalance that systematically raises the nominal
token price while shifting consensus ownership away from active utility users. Active
speculative capital has a qualitatively different effect. In response to capital shocks, the
Consumer class’s rigid preference for fiat-denominated consumption generates an en-
dogenous constant-value strategy. This mechanism shifts staked-token ownership from
the Investor class toward active utility users, with potentially favorable implications
for consensus decentralization.
1 Introduction
This paper develops an explanatory open-economy macroeconomic model to address
two fundamental questions concerning Proof-of-Stake (PoS) networks. Contemporary
macroeconomic discussions of Ethereum (ETH) are increasingly shaped by the net-
work’s rapid financialization. The expansion of liquid-staking protocols and the in-
troduction of yield-bearing exchange-traded products have attracted substantial insti-
tutional capital, encouraging investors to treat ETH as a passive yield-bearing asset
rather than primarily as a transactional utility token.
1
arXiv:2607.16622v1  [econ.GN]  18 Jul 2026

This structural transformation raises two central questions. First, is the absence of
an observable macroeconomic equilibrium token price an intrinsic feature of the net-
work, or is it a consequence of institutional speculation? Second, how does speculative
capital affect the network’s economic functioning, token distribution and issuance, and
consensus security?
To answer the first question, we start with the model, called the Dual-Consumption
Model of the economy of Proof-of-Stake networks, introduced in [10] and strip away
the speculative layer contained in it to isolate the network’s intrinsic economic drivers.
We consider a market populated initially only by Consumers: active utility users with
well-defined preferences who periodically inject exogenous, real-world fiat to finance
network transactions and staking. We analyze the behavior of the dynamical system
at the center of this model for the existence and stability of the steady-states which
represent the economic macroscopic equilibria.
To address the second question, we extend the model by adding a financial agent
(the Investor) who passively keeps capital in the network and subjects the network to
buy/sell shocks, allowing us to quantify the effects of these shocks on the system.
Our main findings are as follows.
The Price Anchor and Macroeconomic Inertia.We first prove that the Consumer-only
economy possesses a unique, globally asymptotically stable steady-state equilibrium.
At this equilibrium, the network satisfies two mass-balance conditions: newly issued
tokens equal tokens burned, while external fiat inflows equal fiat liquidations. The
resulting equilibrium nominal price therefore provides a well-defined long-run price
anchor.
Our quantitative analysis, however, reveals substantial macroeconomic inertia. Un-
der a calibration based on current Ethereum network parameters, the estimated relax-
ation half-life is approximately 50 years. Because economically relevant shocks and
changes in network fundamentals occur on much shorter time scales, the system is un-
likely to approach its prevailing steady state before that steady state shifts again. The
network may therefore remain in persistent transition toward a moving equilibrium
benchmark.
This mechanism is analogous to the overshooting dynamics of classical open-economy
models [2, 9]. In both settings, the interaction between fast and slow variables gener-
ates prolonged departures from equilibrium. In our model, the nominal token price is
the fast variable, responding immediately to changes in external conditions, whereas
the physical token stock adjusts gradually through issuance, burning, and portfolio
reallocation. Thus, persistent nominal-price disequilibrium can arise as an intrinsic
consequence of the network’s adjustment dynamics, even in the absence of speculative
capital.
The Centralizing Effect of Passive Capital.In the second part of the paper, we examine
the systemic effect of passive institutional staking. We prove that when a large Investor
class holds and stakes tokens without contributing to transactional demand, its partic-
ipation compresses the endogenous staking yield below the Consumer-only equilibrium
level. The resulting imbalance causes the nominal token price to rise monotonically
while the Consumer’s share of the staked token stock declines monotonically.
Passive capital therefore moves the system away from the Consumer-only steady
state and gradually reallocates consensus ownership from active utility users toward
non-transactional Investors. This result identifies a centralizing macroeconomic chan-
2

nel that operates independently of any direct technological advantage enjoyed by in-
stitutional staking providers.
Endogenous Volatility Harvesting.We next use numerical simulations to examine the
propagation of speculative capital shocks, modeled as periodic inflows into and outflows
from network staking. We observe that the Consumer’s fixed propensity to consume
in fiat generates an automated constant-value strategy: it sells tokens to Investors
when speculative inflows raise the token price and repurchases them when subsequent
outflows depress it. This response creates a Shannon’s-demon-like volatility-harvesting
mechanism. Under a symmetric fiat cycle and frictionless market clearing, the Con-
sumer’s accumulated fiat-denominated wealth remains unchanged, while physical to-
kens are systematically transferred from the Investor to the Consumer. Speculative
volatility is therefore harvested in token units rather than in fiat.
Active speculative capital thus has an effect fundamentally different from passive
staking. Although it amplifies short-run price volatility, it shifts staked-token owner-
ship toward active utility users, with potentially favorable implications for consensus
decentralization.
1.1 Literature Overview
The open-economy macroeconomic framework developed in this paper builds on Jer-
mann’s models of Ethereum under Proof-of-Stake and EIP-1559 [6, 7], which char-
acterize its long-run equilibrium and connect token valuation, staking, issuance, and
network activity. Related models derive token value from transactional demand and
platform adoption [1] and examine the interaction between utility users and speculative
traders [13]. Our framework extends this literature by introducing distinct Consumer
and Investor classes, explicit external fiat flows, and large deterministic capital shocks.
More specifically, we replace the homogeneous-agent and quasi-linear utility specifi-
cations with a nested utility structure that generates a nonzero wealth effect and a fixed
marginal propensity to consume in fiat. This directly links nominal token-price dynam-
ics to external capital flows. We also shift the focus from small stochastic disturbances
to speculative purchase and liquidation cycles, allowing us to identify endogenous sta-
bilizing and redistributive mechanisms. The underlying Consumer–Investor structure
builds on the Dual-Consumption model introduced in [10]; the present paper estab-
lishes the stability and relaxation properties of the Consumer-only equilibrium and
distinguishes the effects of passive staking from those of active speculative capital.
Our analysis also relates to research on equilibrium staking and consensus own-
ership. Existing studies examine how heterogeneous investment horizons and staking
rewards affect participation and redistribution [8], as well as whether Proof-of-Stake
reward mechanisms concentrate token holdings [12, 4]. Empirical work further docu-
ments the growing concentration of Ethereum’s validating power among centralized and
liquid-staking services [5]. Our model identifies a complementary mechanism through
which external yield-seeking capital compresses staking yields and shifts consensus
ownership away from transactional users.
Finally, Elowsson [3] characterizes Ethereum’s steady-state token supply by equat-
ing validator issuance with EIP-1559 token burn, but does not endogenize the nominal
token price through behavioral agents and fiat flows. Our analysis of price adjustment
instead draws an analogy with classical open-economy overshooting models [2, 9]: the
3

nominal token price responds rapidly to capital shocks, whereas the staked-token stock
adjusts slowly, producing persistent deviations from a moving steady-state benchmark.
2 The Dual-Consumption Model
In the Dual-Consumption Model, the Consumer class represents the active utility users
of the network. Unlike speculative actors, Consumers possess well-defined preferences
for transacting on the network, staking tokens, and liquidating a portion of their hold-
ings for outside-world consumption. Each period, they introduce a predictable, ex-
ogenous inflow of fiat (I c) derived from their outside-world income to finance their
ongoing network activities. The Consumer’s economic behavior is rigidly governed by
a hierarchical utility maximization framework.
The first-level utility functionU1(C, V) utilizes a standard logarithmic Cobb-Douglas
specification to model the trade-off between immediate real-world fiat consumption
Cand the aggregate capital volumeVretained within the digital asset ecosystem.
This formulation yields fixed expenditure shares, parameterizingνas the consumer’s
marginal propensity to consume out of total crypto-inclusive wealthWc, andξ= 1−νas
the crypto retention rate. Conditional on the top-level macro allocationV, the second-
level utility functionU 2(Sc, Lc) governs the network portfolio optimization, splitting
the consumer’s crypto-fiat allocation between yield-bearing physical staked supplyS c
and active gas transaction utilityL c. We implement a quasi-linear utility structure at
this second tier to capture an asymmetry in user behavior: while the demand for stak-
ing assetsS c is highly elastic and scales linearly with wealth allocations, the demand
for core transactional throughputγlogL c is inelastic. In this formula,γ >0 measures
the intensity of the Consumer’s demand for transactional token use.
Thus, the first-level utility is given by the formula
U1(C, V) =νlogC+ (1−ν) logV, ν∈(0,1),(1)
with the budget constraint
C+V=W c,
and the second-level utility:
U2(Sc, Lc) =E[p]S c(1 +y) +γlogL c,(2)
with the budget
pSc +pL c =V.
Here,E[p] is the next period token price. Optimizing the consumption we get:
C=νW c, V=ξW c, ξ= 1−ν.
Optimizing the crypto balance, we obtain:
Lc = γ E[p](1 +y) ,(3)
Sc =V /p−L c = ξWc p −L c.(4)
4

To simplify the analysis, we assume myopic price expectations,E[p t+1] =p t.
In contrast to the utility-driven Consumer, the Investor class represents purely spec-
ulative capital. These actors do not participate in the network’s endogenous transac-
tional utility, meaning they do not consume block space or incur transaction fees. In-
stead, they interact with the protocol strictly as a yield-bearing digital bond, passively
staking their entire token balance to capture the native issuance. Within the Dual-
Consumption framework, the Investor acts as the primary catalyst for macroeconomic
volatility by injecting or extracting exogenous capital shocks (Λ t) during speculative
boom-and-bust cycles.
We summarize the state variables and parameters for the open-economy model that
we use in this paper in Table 1.
Symbol Description
MTotal active physical supply of the native token (e.g.,
ETH).
STotal physical tokens staked in the network.
pFiat-denominated unit price of the native token (e.g.,
USD price of ETH).
yNative staking yield, defined asy= c√ S , wherecis the network issuance parameter.
Wc Fiat-denominated budget of the Consumer.
Ic Rate of Consumer fiat in-flow.
Sc Physical tokens demanded for staking by the Con-
sumer.
Lc The physical quantity of tokens expended on network
transactions during the period.
Si Physical tokens demanded for staking by the Investor.
Λt Rate of Investor fiat in/out flow.
Table 1: State variables and parameters for the Dual-Consumption Model.
2.0.1 Network supply evolutionM t+1
We denote byM t the active token stock represented in the model, comprising staked
tokens and tokens allocated to transactional expenditure. Passive unstaked token bal-
ances that are neither staked nor allocated to current transactional expenditure are
outside the modeled active stock.
The total active supply of ETH at periodtis split between tokens staked and tokens
designated for burn:
M t =S t +L t c.
The number of tokens changes due to the network inflation and burn:
M t+1 =S t(1 +y t).
The new amount of tokens staked is determined from equation
M t+1 =S t+1 +L t+1 c ,
5

whereL t+1 c is the new demand for gas by the consumers. And finally,
St+1 =S t(1 +y t)−L t+1 c .(5)
2.0.2 The Consumer and the Investor staking evolution
The total network staking is composed of the Investor and the Consumer staking
amounts:
St =S t i +S t c, t= 0,1,2...
We consider an open-loop model in which the Investor stakes all the wealth that
exogenously changes with the in-flow rate of capital Λ t.
The wealth accumulated by the Investor and the Consumer over one period:
•Next Period Investor Staking Amount
St+1 i =S t i (1 +y t) + Λt+1 pt+1 .(6)
•Next Period Consumer Total Wealth (including exogenous fiat incomeI t+1 c ):
W t+1 c =p t+1St c(1 +y t) +I t+1 c (7)
=p t+1
 ξW t c
pt −L t c

(1 +y t) +I t+1 c .(8)
2.0.3 Clearing Price Equation
To derive the next period pricep t+1, we begin with the market-clearing identity. The
total token supply available for allocation at datet+ 1 must equal the sum of the
Investor’s new physical demand and the Consumer’s new physical demand:
St(1 +y t) =S t i (1 +y t) + Λt+1 pt+1 + ξW t+1 c pt+1 .(9)
SinceS t(1+y t) =S t c(1+y t)+S t i (1+y t),and using equation (7), we get the Balance
equation
(1−ξ)S t c(1 +y t) = Λt+1 pt+1 + ξI t+1 c pt+1 ,(10)
where the left-hand side represents the number of tokens sold by the Consumer class
and the right-hand side represents the amounts purchased by the Investor and the
Consumer, respectively.
Using (4) on the left-hand side of (10), and solving forp t+1,we get,
pt+1 =p t
 Λt+1 +ξI t+1 c
ν(ξW tc −p tLtc) (1 +y t)

.(11)
This formula can also be written in terms of the Consumer staking amountS t c :
pt+1 = Λt+1 +ξI t+1 c
νS tc(1 +y t) .(12)
6

Finally, we substitute the liquid gas demand constraintL t c = γ pt(1+yt) into the
denominator to reach the fully expanded, actionable price equation:
pt+1 =p t
 Λt+1 +ξI t+1 c
νξW tc (1 +y t)−νγ

.(13)
Substituting (11) in (8) we observe the balance of the fiat inflow (Right) and outflow
(Left):
νW t+1 c = Λt+1 +I t+1 c .(14)
Here and below, we restrict Λ t >−ξI t c.
For future use, we record
•Next Period Consumer Staking Amount
St+1 c =ξS t c(1 +y t) + ξI t+1 c pt+1 −L t+1 c (15)
=ξS t c(1 +y t) + 1 pt+1

ξI t+1 c − γ 1 +y t+1

.(16)
Comment 1.Since the Consumer fiat inflow rateI t c is vastly larger than the gas burn
fees γ 1+yt+1 under the Ethereum calibration, equation(16)shows that there is a lower
bound on the rate of decrease of the Consumer staking level:
St+1 c > ξSt c
no matter how hard the Investor is buying off tokens,(Λ t >0), preventing a fast
takeover of the network by the Investor.
2.0.4 The Next-Period Staking Level
Once the market-clearing pricep t+1 is established, it determines the required fiat-
equivalent gas burn, which dictates the physical supply evolution. The law of motion
for the physical staked supply states that the next period’s staked tokens equal the
newly inflated total supply minus the tokens burned for transactional utility:
St+1 =S t(1 +y t)−L t+1 c .(17)
We substitute the functional definitions for both the next-period gas demandL t+1 c
and the next-period yieldy t+1:
Lt+1 c = γ pt+1(1 +y t+1) ,wherey t+1 = c√ St+1 .(18)
Plugging these into (17), yieldsS t+1:
St+1 =S t(1 + c√
St )− γ pt+1  1 + c√ St+1  .(19)
7

2.1 Dynamical System Formalism
For the study of the dynamics of the Dual-Consumption Model described in the previ-
ous sections, it will be convenient to represent the state of the network at periodtby
a vector of the staking level of the Consumer (S t c),total staked ETH in the network
(St) and pricep t :
(St c, St, pt).
The values of all other variables are functions of this state. The change of the state
vector over one period is governed by the system consisting of equations (12), (16) and
(19). This system implicitly defines the next period values from the current values and
exogenous inputs:
(St+1 c , St+1, pt+1) =F(S t c, St, pt,Λ t+1, It+1 c ),(20)
for some vector-valued functionF.The model is completed by the choice of the initial
values for
(S0 i , S0, p0).
2.2 Steady-State Equilibrium for the Consumer-only Econ-
omy
We consider first the Consumer-only Economy (S t i = 0,Λ t = 0). In this caseS t =S t c,
andW t c = I t c ν .The dynamics is described by the equations
pt+1 = ξI t+1 c
νS t(1 +y t) ,(21)
St+1 =S t(1 +y t)− γ pt+1 (1 +y t+1) .(22)
The Consumer dynamics admits a unique steady state if we assume that the Consumer
fiat inflow is constant:I t c =I c.In such a case, the steady-state values for the price, the
consumer wealth, the staking amount, and ETH yield can be obtained from the above
equations, see [11]:
S∗ =
 cξIc
γν
2
, p ∗ = γ2ν c2(ξIc +γν) , y ∗ = γν ξIc , W ∗ c = Ic ν .(23)
The steady-state is the intersection point of the equilibrium for fiat in-flow and
out-flow rates:
Ic =νW ∗ c ,(24)
the equilibrium between newly minted tokens and the tokens burned:
S∗y∗ = γ p∗(1 +y ∗) ,
and the price at which tokens demanded and tokens liquidated are equal:
ξIc
p∗ =νS ∗(1 +y ∗).
We will call the set of all steady-states parametrized by the fiat inflow rateI c the
steady-state manifold.
8

Comment 2(Network Expansion).The formula for the equilibrium price of ETH can
be used to obtain a crude quantitative estimate of the effect of the expansion of the
network. If there isNparticipants in the economy, then bothγ∼NandI c ∼Nand
from the formula forp ∗ in(23)we conclude that the equilibrium price will grow linearly
inNduring such expansion.
Comment 3.Notice that the equilibrium pricep ∗ in(23)is inversely proportional
to fiat inflow rateI c,which we can informally identify as the Consumer demand for
tokens. Increased demand does lead to an increase in the token price, but only in the
short term. The price jump triggers the issuance of tokens above the burn level, which
over time brings the system back to the equilibrium manifold, with the lower equilibrium
pricep ∗.
Numerical ExampleWe illustrate convergence to equilibrium after an increase in
demand by the following numerical example. We consider the system at a steady-state
initially with values reflecting realistic network conditions, as summarized in Table 2.
Description Parameter Value
Monthly periodic yield (3% annualized target)y ∗ 0.0025
Initial physical staked supply (tokens)S 0 40×10 6
Baseline exogenous monthly fiat inflow (USD)I 0 c 350×10 6
Fiat consumption propensityν0.01
Crypto retention rateξ0.99
Gas utility parameterγ86.625×10 6
Network issuance parameterc15.81
Table 2: Baseline calibration parameters for the steady-state equilibrium.
Att= 1, we introduce a macroeconomic shock where the fiat inflow demand per-
manently increases by 50%, jumping toI 1 c = 525×10 6 USD.
Following the shock, the system is bound to an asset-market clearing locus derived
from equations (21) and (22):
p= 1 S  ξI 1 c ν − γ 1 +y  .(25)
The system then moves along this curve until it reaches a new steady state (see Figure
1).
The dynamics in this example goes through the following causal sequence.
The Price Jump:When the demand,I c, jumps, the market-clearing pricepmust
spike instantaneously because the physical staked supplyScannot jump.
The Burn Collapse:With a significantly higher nominal token price, the physical
tokens required to satisfy the Consumer’s constant fiat gas demand decrease sharply
from the previous steady-state level.
The Supply Expansion:Because the physical burn rate collapses while the protocol’s
native yield continues to issue tokens, the network suddenly mints more tokens than it
burns, leading to expansion of the physical staked supplyS.
9

The Monotone Slide:The system then enters a slow, multi-decade monotone sliding
mode along the short-run equilibrium schedule (25). As more tokens are minted and the
physical supply expands, the nominal price incrementally decreases. This decreasing
price causes the burned tokens to increase, see (3), until the burn rate finally catches
up to perfectly balance the minting rate at the new steady-state equilibrium.
The stability and slow adjustment rate in this example are generic properties of the
network. We address these properties in the next section.
2.2.1 Stability of the Steady State and the Rate of Relaxation
In the case of the Consumer-only Economy, the dynamical system (20) reduces to 1-
dimensional system for the staking amountS t.The non-linear equation for the next
periodS t+1 is given by
St+1 =S t(1 +y t)

1− y∗
1 +y t+1

, y t = c√
St ,(26)
which implicitly determinesS t+1 =F(S t).
Our main result, which we prove in Section 5, is that the steady state is unique and
is globally and asymptotically stable.
Theorem 1(Global Asymptotic Stability of the Consumer-only Economy).Consider
the deterministic discrete-time dynamical system governing the physical staked supply
in a Consumer-only economy, defined implicitly by the transition mapS t+1 =F(S t)
from equation
St+1 =S t(1 +y(S t))

1− y∗
1 +y(S t+1)

(27)
wherey(S) = c√ S and the steady-state baseline yield isy ∗ = νγ ξIc . Assume standard
macroeconomic conditions such that0< y ∗ <1. Then, the unique steady stateS ∗ is
globally asymptotically stable. Specifically:
i. For any arbitrary initial physical supplyS 0 >0, the state sequence{S t}∞ t=0 con-
verges monotonically to the steady stateS ∗.
ii. SequenceS t converges toS ∗ at the relaxation rateλ,
lim
t→∞
St+1 −S ∗
St −S ∗ =λ= 1 + 1 2 y∗ 1 +y ∗ + 1 2 (y∗)2 ≈1− 1 2 y∗.(28)
Numerical ExampleTo illustrate the macroeconomic inertia of the network in reality,
we evaluate the convergence rate using the baseline parameters from Table 2. According
to Theorem 1 the relaxation rate of the physical supplyS t and the pricep t given by
λ≈1− 1 2 y∗ = 0.99875.
This value ofλis exceptionally close to 1.The macroeconomic half-life (t 1/2), which
represents the time required for a network shock to dissipate by exactly 50%, is
t1/2 = ln(0.5) ln(λ) ≈554.17 months.
10

This translates to an adjustment half-life of approximately 46 years.
This calculation shows that while the Consumer-only economy is globally and
asymptotically stable, it takes decades for the physical consensus layer to move the
system to the steady-state manifold.
The steady-state is entirely determined by the exogenous fiat inflow,I c. In reality,
this inflow is highly dynamic, fluctuating in response to real-world business cycles,
shifts in market sentiment, and technological innovation. These traditional economic
drivers operate on relatively short timescales—business cycles typically unfold over a
few years, while broader macroeconomic trends can alter fiat liquidity in a matter of
months. Because these real-world fluctuations happen faster than the network’s 46-
year relaxation time, the physical layer is structurally too slow to ever catch up. The
network is repeatedly hit by new shocks long before it can resolve the previous ones.
Consequently, the system exists in a perpetual state of transition, constantly chasing
an ever-changing target on the attractor. This dynamic closely mirrors the classic
Asset Price Overshooting model introduced by Dornbusch [2], and further formalized
by Obstfeld and Rogoff [9]. Just as in those established frameworks, our network
features a fast variable (the nominal pricep t) that instantaneously absorbs any change
inI c (Equation (12)), alongside a slow variable (the physical supplyS t) that drags the
system toward the new steady state at a crawling pace.
Figure 1: Simulated dynamics of the Consumer-only Market. At time
t= 0, the market is at equilibrium State 1. Att= 1 the fiat inflow rateI c
increases by 50%. The fast variablep t immediately adjusts to the new level
(State 2). The network proceeds slowly to the steady-state equilibrium
State 3. The simulation stops aftert= 1,200 months, or 100 years.
11

3 Consumer/Investor Dynamics
In this section, we will extend the Consumer-only Economy with an additional financial
sector represented by the Investor who keeps capital in ETH staking. The financial
goals of the Investor are outside of the scope of our model. Here we will focus on
two simple scenarios. (A) Passive Accumulation: the Investor has a certain amount
of staked ETH that remains in the network for a long period of time. (B) Buy/Sell
Shocks: The Investor who has a substantial amount of staked ETH occasionally buys
or sells large amounts of tokens.
In both scenarios, the question is how the network reacts to the addition of the
Investor class. Specifically, we will be interested in the (de)centralization: the share of
tokens owned by the Consumer and the Investor, and the nominal price dynamics.
We start with scenario (A).
Lemma 1(Effects of Passive Investor Accumulation).Assume that the Consumer fiat
inflow is constant,
I t c =I c >0,
and that the Investor makes no additional purchases or liquidations after the initial
date,
Λt = 0, t≥1.
Let the equilibrium yieldy ∗ = νγ ξIc ,0< y ∗ <1.Then the following statements hold.
(i)For any initial Consumer wealthW 0 c >0, the Consumer’s fiat-denominated wealth
satisfies
W t c = Ic ν , t≥1.
(ii)Suppose that att= 1the state is interior and satisfies
0< S1 c < S1,0< y 1 < y∗, S1 c S1 < y1 y∗ .
Then, for everyt≥1,
St+1 > St,0< y t+1 < yt < y∗,
pt+1 > pt, S t+1 c < St c, S t+1 i > St i .
Consequently, the Consumer’s share of the total staked-token stock decreases
monotonically:
St+1 c
St+1 < St c St , t≥1.
The exact one-period price-inflation rate is
pt+1 −p t
pt = y∗ −y t 1−(y ∗ −y t) =y ∗ −y t +O  (y∗ −y t)2 .
Proof.Under passive accumulation, Λ t+1 = 0. The fiat-balance identity gives
νW t+1 c =I c,
12

and hence
W t c = Ic ν , t≥1.
This proves part (i).
Fort≥1, substitutingW t c =I c/νand
ptLt c = γ 1 +y t
into the market-clearing price equation gives
pt+1
pt = ξIc ξIc(1 +y t)−νγ = 1 1 +y t −y ∗ = 1 1−(y ∗ −y t) .
Therefore, whenevery t < y∗,
pt+1 > pt,
and
pt+1 −p t
pt = y∗ −y t 1−(y ∗ −y t) .
We next determine when total stake increases. Using
pt+1 = ξIc
νS tc(1 +y t)
andy ∗ =νγ/(ξI c), the next-period burn is
Lt+1 c = γ pt+1(1 +y t+1) = y∗St c(1 +y t) 1 +y t+1 .
The total-stake equation therefore becomes
St+1 =S t(1 +y t)− y∗St c(1 +y t) 1 +y t+1 .
We claim thaty tSt > y∗St c impliesS t+1 > St.Sincey(S) =c/ √ S, this implies
yt+1 < yt.
Suppose, to the contrary, thatS t+1 ≤S t. Sincey(S) =c/ √ S, this impliesy t+1 ≥y t.
Therefore,
y∗St c(1 +y t)
1 +y t+1 ≤y ∗St c.
Using the total-stake equation, we obtain
St+1 ≥S t(1 +y t)−y ∗St c =S t +  ytSt −y ∗St c  > St,
which is a contradiction.
Fort≥1, the Consumer’s staked-token position can be written as
St c = 1 pt
 ξIc
ν − γ 1 +y t

= ξIc
νpt

1− y∗
1 +y t

.
13

Ify t+1 < yt, then
1− y∗
1 +y t+1 <1− y∗ 1 +y t .
Together withp t+1 > pt, this gives
St+1 c < St c.
It remains to verify that the sufficient condition
ytSt > y∗St c
is preserved. SinceS t+1 > St andS t+1 c < St c,
yt+1St+1 =c √ St+1 > c √ St =y tSt > y∗St c > y∗St+1 c .
Thus,
yt+1St+1 > y∗St+1 c ,
so the argument applies inductively for everyt≥1.
Finally, because Λt+1 = 0,
St+1 i =S t i (1 +y t)> St i .
SinceS t c decreases whileS t increases,
St+1 c
St+1 < St c St .
This proves part (ii).
The lemma shows that when the network yield is below the Consumer-only equi-
librium level and the Consumer’s share of total staking lies below the state-dependent
threshold (y t/y∗), the system enters a self-reinforcing regime: total stake rises, the
staking yield declines, the nominal token price increases monotonically, and the Con-
sumer’s share of staked tokens decreases monotonically. Passive Investor accumulation
therefore moves the system progressively away from the Consumer-only steady-state
manifold.
3.1 Buy–Sell Shocks
We consider now the Investor/Consumer Economy in the scenario (B). For the presen-
tation we opt for a numerical simulation that captures the main features of the market
dynamics. In our model, the Investor is passively staked in ETH at the beginning of
the simulation and then injects capital, Λ t >0,during a short period (Buy Shock),
and later liquidates the same amount of capital, Λ t <0,during a period of the same
length.
The network is parameterized according to the conditions in Table 3.
The simulation modeled a symmetric shock: the Investor injected Λ t = 300 million
USD monthly from monthst= 20, ...,30,and subsequently extracted the exact same
fiat amount, Λ t =−300 million USD from months 40 to 50.
14

Parameter Symbol Value
Fiat Inflow (Monthly)I c 350 Million USD
Fiat Consumption Propensityν1%
Baseline Staking Yield (Monthly)y ∗ 0.25%
Initial Staked SupplyS 0 40 Million ETH
Initial Consumer Staked SupplyS 0 c 10 Million ETH
Initial Investor Staked SupplyS 0 i 30 Million ETH
Initial Token Pricep 0 ≈3,456 USD
Initial Consumer WealthW 0 c 35 Billion USD
Gas Utility Parameterγ86.625×10 6
Network Issuance Parameterc15.81
Table 3: Market Model Parameters for the Dual-Consumption simulation.
The results of the simulation are summarized in Figure 2. The main characteristic
features of the dynamics are the following.
Price Overshooting and Persistent Displacement:The nominal token price (p t) rises
to nearly 7,000 USD during the buy shock and falls to approximately 300 USD during
the sell shock. Following the cycle, the simulated price recovers to approximately
2,100 over the displayed post-shock horizon, remaining below its initial value during
that interval; see the top-left panel of Figure 2.
Physical Token Redistribution:The Consumer endogenously accumulates staked
tokens, increasingS c from 10 million to approximately 17 million ETH. The Investor’s
staked-token holdings decline by the corresponding amount; see the bottom-left panel
of Figure 2.
Fiat-Denominated Wealth:The cumulative net Investor fiat flow over the complete
cycle is zero: the Investor withdraws the same total amount of fiat that it previously
injected. Nevertheless, the Investor ends the cycle with fewer tokens. The Consumer’s
total accumulated wealth, defined as the total fiat extracted minus total fiat injected,
added to the Consumer’s current token wealth,
 tX
k=1
(νW k c −I k c )
!
+W t c ,
returns to its pre-shock value because Pt k=1(νW k c −I k c ) = Pt k=1 Λk = 0,fort >50.
3.1.1 The asymmetries in the Buy/Sell cycle.
The market mechanics of the Buy/Sell cycle produce visible asymmetries in the dy-
namics of all market variables.
The Buy Shock:When the Investor injects fiat into the token market, the price
spikes instantly. Because they are purchasing tokens at the elevated token price (p t ≈
7,000), their 300 million USD buys a relatively small volume of physical tokens.
The Consumer allocates the fixed share (νW t c ) of its wealth to fiat consumption. As
the price increase raises the fiat-denominated value of the Consumer’s token holdings,
15

its desired consumption rises. When (νW t c > It c), the Consumer finances the difference
by liquidating tokens, thereby supplying the tokens purchased by the Investor.
The Sell Shock:During the sell shock, the Investor liquidates tokens, while the
Consumer provides the corresponding buying demand required by market clearing.
The price crashes (p t ≈300). The fixed fiat withdrawal requires the Investor to
liquidate a substantially larger volume of tokens than they originally purchased.
At a lower token price, a given fiat surplus allows the Consumer to acquire a larger
physical quantity of tokens. The Consumer algorithmically absorbs this large token
liquidation at the depressed price, resulting in the persistent post-shock increase inS c.
In this cycle, the Consumer effectively executes a constant-value rebalancing strat-
egy: algorithmically selling ”High” and buying ”Low.” The asymmetry of the Buy–Sell
cycle follows from the market-clearing identity
I t c −νW t c =−Λ t, t >0.(29)
In the absence of Investor flows, Λt = 0,this identity yieldsW t c /I t c = 1/ν.We therefore
refer to 1/νas the Consumer’s target Constant-Value Ratio. Investor flows temporarily
displace the Consumer from this target and induce the compensating token sales and
purchases described below.
The left-hand side of (29) represents the Consumer’s net fiat contribution to the
token market: its exogenous fiat inflow (I t c) less its fiat consumption (νW t c ). Thus, the
Consumer’s net order flow exactly offsets the exogenous Investor flow.
During the buy shock, (Λ t >0), and hence (νW t c > It c). The Consumer therefore
liquidates tokens to finance consumption in excess of its current fiat inflow, providing
the token supply purchased by the Investor as the price rises. During the sell shock,
(Λt <0), and hence (νW t c < It c). The Consumer then retains a net fiat surplus and
purchases tokens liquidated by the Investor.
Because a fixed fiat amount purchases fewer tokens at the elevated buy-shock price
and more tokens at the depressed sell-shock price, a symmetric fiat Buy–Sell cycle gen-
erates an asymmetric transfer of physical tokens from the Investor to the Consumer.
The Consumer’s allocation rule therefore produces an endogenous contrarian rebalanc-
ing mechanism: it sells tokens during the price increase and purchases tokens during
the subsequent decline.
The simulation also exhibits persistent finite-horizon displacement in the nominal
token price. Following the Buy–Sell cycle, the price remains below its initial value over
the displayed post-shock period. This displacement is associated with a substantial
redistribution of staked tokens between the two classes: the Consumer holds a larger
post-shock token balance, while its fiat-denominated transactional demand remains
unchanged.
The token-denominated burn rate rises sharply during the sell shock, see Figure
2, bottom right display. In the model, the lower token price increases the quantity of
ETH associated with a given level of fiat-denominated transactional demand; the burn
spike therefore need not represent a comparable increase in real network activity.
3.1.2 Financial and consensus-ownership implications
The symmetric Buy–Sell cycle leaves the Consumer’s accumulated fiat-denominated
wealth unchanged while increasing its physical token holdings. The cycle is there-
16

fore wealth-neutral and token-accretive for the Consumer under the stated accounting
measure.
From the perspective of consensus ownership, the cycle shifts staked tokens from the
non-transactional Investor to the active utility-driven Consumer. This redistribution
may have favorable implications for the alignment of validating power with network use.
Establishing a corresponding improvement in decentralization or consensus security,
however, would require an explicit measure of validator concentration or attack cost.
Figure 2: Simulated dynamics of a Buy-Sell cycle. The Investor is pas-
sively staking tokens in the first 20 periods. At periodst= 20, ...,30
the Investor invests 300 million USD per period into staking. At periods
t= 40, ...,50 the Investor liquidates the same amount, 300 million USD
per period.
4 Conclusions and Limitations
This paper develops a dynamical open-economy model of a Proof-of-Stake network
with utility-driven Consumers and non-transactional Investors. In the Consumer-only
economy, we establish the existence of a unique globally asymptotically stable steady
state that provides a well-defined nominal price anchor. The calibrated local relaxation
half-life is approximately 46 years, indicating that the physical token stock adjusts
much more slowly than the nominal price. Consequently, the observed market price
may remain persistently displaced from an equilibrium benchmark that itself changes
with network fundamentals.
17

The introduction of Investor capital produces two distinct effects. Under the suf-
ficient conditions identified in Lemma 1, passive restaking suppresses the native yield,
raises the nominal token price, and gradually shifts the staked-token share away from
active Consumers. By contrast, symmetric Buy–Sell shocks generate an endogenous
contrarian response. The Consumer sells tokens during speculative inflows and re-
purchases them during subsequent outflows. Under frictionless market clearing, this
Shannon’s-demon-like mechanism leaves the Consumer’s accumulated fiat-denominated
wealth unchanged while increasing its physical token holdings. Speculative volatility
is therefore harvested in token units rather than in fiat.
The model is intentionally stylized. It represents Consumers and Investors as ag-
gregate classes, assumes myopic price expectations, and abstracts from transaction
costs, slippage, taxes, staking delays, leverage, heterogeneous beliefs, and strategic In-
vestor behavior. The Buy–Sell experiment uses deterministic symmetric fiat shocks;
asymmetric or stochastic capital flows need not produce the same redistribution. The
calibration is illustrative rather than a formal empirical estimation, and the model’s
active token stock excludes passive unstaked balances. Finally, a transfer of stake to-
ward the Consumer class does not by itself establish greater validator decentralization
or consensus security. Evaluating those effects would require explicit measures of own-
ership concentration, delegation structure, and attack cost. Another natural extension
is to characterize the volatility-harvesting mechanism analytically for general Buy–Sell
cycles and to determine its robustness to asymmetric capital flows, transaction costs,
and stochastic price dynamics.
5 Appendix
5.1 Proof of Theorem 1
Proof.To prove part i., letS ∗ be the steady-state of (26) and 1−y ∗ >0.GivenS 0 >0
we will show thatS t →S ∗,ast→ ∞.We restructure the implicit recurrence relation
into the form
H(S t+1) =R(S t),
where the auxiliary functions are defined as:
R(x) =x(1 +y(x)),andH(x) = x(1 +y(x)) 1 +y(x)−y ∗ ,(30)
where the yield curvey(x) =cx −1/2.Direct computation shows that bothR(·) and
H(·) are strictly increasing functions.
SinceH(x) is strictly increasing, its continuous inverseH −1(x) exists, allowing us
to explicitly define the transition map asF(x)≡H −1(R(x)). As the composition of
two strictly increasing functions,F(x) is strictly increasing.
To determine the direction of the transition map relative to the liney=x, we
evaluate the sign ofR(x)−H(x):
R(x)−H(x) =x(1 +y(x))
 y(x)−y ∗
1 +y(x)−y ∗

(31)
Because the native yieldy(x) is strictly monotonically decreasing,
18

•forx < S ∗,y(x)> y ∗. The difference (y(x)−y ∗) is strictly positive, ensuring
R(x)> H(x), which impliesF(x)> x;
•forx > S ∗,y(x)< y ∗. The difference (y(x)−y ∗) is strictly negative, ensuring
R(x)< H(x), which impliesF(x)< x.
SinceF(x) is strictly increasing, sequences generated byS t+1 =F(S t) are monotonic.
IfS 0 < S∗, the sequence is strictly increasing and bounded above byS ∗. IfS 0 > S∗,
it is strictly decreasing and bounded below byS ∗. By the Monotone Convergence
Theorem, for anyS 0 >0, lim t→∞ St =S ∗.
The linearized relaxation rateλin part ii. is defined asF ′(S∗).The value ofF ′(S∗)
is obtained by differentiating equation (26) and evaluating it at the steady stateS ∗ :
F ′(S∗) = 1 + 1 2 y∗
1 +y ∗ + 1 2 (y∗)2 = 1− 1 2 y∗ +O((y ∗)2).
References
[1] Lin William Cong, Ye Li, and Neng Wang. Tokenomics: Dynamic adoption and
valuation.The Review of Financial Studies, 34(3):1105–1155, 2021.
[2] Rudiger Dornbusch. Expectations and exchange rate dynamics.Journal of Polit-
ical Economy, 84(6):1161–1176, 1976.
[3] Anders Elowsson. Circulating supply equilibrium for ethereum and minimum
viable issuance during the proof-of-stake era. Ethereum Research Forum, 2021.
Accessed: 2026-07-16.
[4] Giulia Fanti, Leonid Kogan, Sewoong Oh, Kathleen Ruan, Pramod Viswanath,
and Gerui Wang. Compounding of wealth in Proof-of-Stake cryptocurrencies. In
Ian Goldberg and Tyler Moore, editors,Financial Cryptography and Data Secu-
rity, volume 11598 ofLecture Notes in Computer Science, pages 42–61. Springer,
2019.
[5] Dominic Grandjean, Lioba Heimbach, and Roger Wattenhofer. Ethereum Proof-
of-Stake Consensus Layer: Participation and decentralization. InFinancial Cryp-
tography and Data Security: FC 2024 International Workshops, pages 253–280.
Springer, 2024.
[6] Urban Jermann. A macro finance model for proof-of-stake Ethereum. Working
Paper, 2025.
[7] Urban Jermann. Optimal issuance for proof-of-stake blockchains. Working Paper,
University of Pennsylvania, 2025.
[8] Kose John, Thomas J. Rivera, and Fahad Saleh. Equilibrium staking levels in a
proof-of-stake blockchain. Working Paper, SSRN 3965599, 2021.
[9] Maurice Obstfeld and Kenneth S. Rogoff.Foundations of International Macroe-
conomics. MIT Press, Cambridge, MA, 1996.
[10] Mikhail Perepelitsa. Bubbles vs. baselines: Token valuation and institutional
capital in pos networks under eip-1559.arXiv:2606.07445, 2026.
19

[11] Mikhail Perepelitsa. The financialization of proof-of-stake: Asymptotic central-
ization under exogenous risk premiums.arXiv preprint: 2604.26076, 2026.
[12] Ioanid Ro¸ su and Fahad Saleh. Evolution of shares in a proof-of-stake cryptocur-
rency.Management Science, 67(2):661–672, 2021.
[13] Michael Sockin and Wei Xiong. A model of cryptocurrencies.Management Sci-
ence, 69(11):6684–6707, 2023.
20
