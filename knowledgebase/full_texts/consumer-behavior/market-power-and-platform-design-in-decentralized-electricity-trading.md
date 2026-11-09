---
title: Market Power and Platform Design in Decentralized Electricity Trading
url: https://arxiv.org/abs/2603.19988
category: consumer-behavior
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Nicolas Eschenbaum
- Nicolas Greber
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.19988
pages: 39
chars: 101273
fetched_at: '2026-11-08T13:04:55+00:00'
kb_version: 1
---

# Market Power and Platform Design in Decentralized Electricity Trading

Market Power and Platform Design in
Decentralized Electricity Trading
Nicolas Eschenbaum* Nicolas Greber†
March 2026
Abstract
This paper studies how platform design shapes strategic behavior in decentralized electricity
trading. We develop a finite-horizon dynamic game in which photovoltaic- and battery-equipped
players (‘prosumers’) trade on a platform that maps aggregate imports and exports into internal
buy and sell prices. We establish existence of a perfect conditional ε-equilibrium and character-
ize a Cournot-like market-power mechanism in an observable-types benchmark of the game:
because the producer price is decreasing in aggregate exports, strategic prosumers withhold
supply and underutilize storage relative to the price-taking benchmark. To quantify these effects,
we use a multi-agent computational framework that exploits the differentiable structure of the
platform’s clearing rule to compare planner, price-taking, and strategic outcomes under alterna-
tive pricing mechanisms. In our baseline calibration, strategic play raises grid settlement cost
by about 6 percent relative to price-taking. The magnitude of the distortion depends strongly
on platform design: some designs can largely eliminate strategic incentives, while increased
competition in storage ownership sharply reduces withholding, with most of the distortion
disappearing once storage is split across (more than) three owners. We also find that information
disclosure can improve competitive coordination but also increase the market power effects.
Despite these distortions, the platform remains highly valuable overall, reducing a passive con-
sumer’s annual electricity bill by roughly 40 percent relative to exclusive grid settlement, with
strategic behaviour clawing back only about 8 percent of that saving. The results show that
pricing rules, information disclosure, and ownership structure determine how much of the
gains from decentralized electricity trading are realized.
JEL Classification:C63, C73, D43, D47 , L94, Q41
Keywords:electricity trading platforms; market power; pricing mechanisms; battery storage; multi-
agent learning
*Swiss Economics, Zürich, Switzerland. nicolas.eschenbaum@swiss-economics.ch. This work was supported by the
Swiss Federal Office of Energy (SFOE) under grant number SI/502525.
†University of Zurich and Swiss Economics, Zürich, Switzerland. nicolasjoel.greber@uzh.ch.
arXiv:2603.19988v1  [econ.GN]  20 Mar 2026

1. Introduction
Digital platforms increasingly intermediate transactions in markets that were historically orga-
nized through centralized pricing or bilateral contracting. Electricity is a particularly interesting
setting, because participants trade a homogeneous good in repeated interactions, the outside
option is regulated by retail and feed-in tariffs that are fixed by regulators, and users may control
decentralized productive assets such as photovoltaic generation and battery storage. In this envi-
ronment, a platform is not merely a coordination device. By mapping aggregate buying and selling
quantities into internal prices, it becomes a market institution that shapes strategic behavior.
This paper studies market power and platform design in decentralized electricity trading. We
consider a platform that clears local trade inside a community of prosumers and settles residual
imbalances with the external grid. The platform precommits to a pricing rule that maps aggregate
imports and exports into internal buy and sell prices, subject to a tariff corridor given by the
regulated import and export prices. Prosumers choose when to charge or discharge their battery,
whether to self-consume or sell locally, and when to buy from the platform rather than the grid.
Because individual decisions affect aggregate market conditions, they also affect the prices that
prosumers themselves face. The resulting game therefore combines intertemporal arbitrage
incentives with price effects.
To study this setting, we formulate prosumer trading as a finite-horizon dynamic game with
batteries, photovoltaics (PV), platform pricing, and private information. Each prosumer privately
observes her type—a sequence of electricity consumption and PV generation realizations—and her
own battery history, so that the current state of charge is payoff-relevant but not publicly observed.
This yields a dynamic game with continuous actions and expanding private histories, a setting in
which standard existence results do not directly apply. We show that the game can be embedded
in the framework of Myerson and Reny (2020), which implies existence of a perfect conditional
ε-equilibrium for everyε >0.
We then characterize equilibrium behavior and the market-power mechanism in a transparent
benchmark of the game with publicly observable types and battery states. We show that a pure-
strategy Markov perfect equilibrium exists under mild curvature conditions, and that net exporters
withhold supply relative to the corresponding price-taking benchmark. The intuition is classic
Cournot: when the producer price is decreasing in aggregate exports, an exporting prosumer values
marginal sales at marginal revenue rather than price. The same logic has a dynamic analogue. If
an additional unit stored today is expected to be sold later, then a strategic prosumer charges less
than a price-taker because future sales are discounted by the effect of own exports on future prices.
Decentralized storage therefore creates a prosumer-scale version of a familiar Cournot finding.
Strategic players underinvest in capacity in equilibrium (i.e., underutilize storage in our setting)
when discharging lowers the price they receive. As a result, an intuitive ordering of outcomes
emerges: total grid settlement cost is lowest when all assets are controlled by a social planner,
intermediate when prosumers are price-takers, and highest when prosumers play strategically.
Since internal transfers between players and the platform cancel, grid cost is the appropriate
measure of total welfare, and market power effects are thus costly for welfare.
We then apply a computational framework developed in Eschenbaum et al. (2026) to compare
1

alternative platform rules and provide quantitative measurements of the outcome of the game. We
model each prosumer by a neural-network policy and train agents in a differentiable multi-agent
environment in which the platform’s clearing rule is known. Because prices are a differentiable
function of aggregate trades, gradients can be propagated through the clearing routine and through
the full multi-period trajectory. This allows us to compare, within a common architecture, three
counterfactuals: a centralized planner, price-taking prosumers, and strategic prosumers. The
unilateral-deviation regret is consistently very low, confirming that the strategic outcome is an
approximate Nash equilibrium, making us confident that agents converged to a perfect conditional
ε-equilibrium. We use this framework to study pricing mechanisms commonly used in local
electricity markets and to quantify how competition, heterogeneity, and information design affect
equilibrium outcomes.
Our quantitative results confirm the theoretical ordering. The social planner achieves the
lowest grid cost, the price-taking benchmark lies close behind, and strategic play raises cost
by roughly 6%. Market power manifests by prosumers withholding evening discharge of their
batteries. As competition among storage ownership increases, it erodes market power. Moving
from a single storage owner to three eliminates most of the strategic distortion, and the welfare loss
is predominantly deadweight rather than rent transfer. Across pricing mechanisms however, the
effect of market power incentives vary by an order of magnitude. A mid-market rate mechanism
virtually removes strategic incentives, while also removing incentives for pure arbitrage. The
linear mechanism permits individual withholding but limits aggregate efficiency loss. Allowing
agents to observe past clearing prices improves competitive outcomes but amplifies strategic
distortions, more than doubling the welfare premium from market power.
Overall, however, the platform remains highly valuable. A passive consumer saves roughly
40% on annual electricity costs by trading on the platform. Strategic behaviour by battery owners
erodes about 8% of that saving. The policy implication is therefore not that platforms should
be avoided, but that their design, in particular the pricing rule, information disclosure, and the
competitive structure of storage ownership, materially affects who captures the surplus from
decentralized trade.
The paper contributes to three strands of the literature. The first studies storage and market
power in electricity markets. Existing work shows that storage can smooth prices and improve
welfare under competition, but that concentrated ownership can also lead to strategic underuti-
lization of storage capacity (Andrés-Cerezo and Fabra, 2023; Schill and Kemfert, 2011; Sioshansi,
2014; Garcia et al., 2001; Bushnell, 2003; Williams and Green, 2022). Related work emphasizes that
market design and ownership structure are central for determining whether decentralized trade
improves welfare (Baake et al., 2023). Our contribution is to bring these ideas to prosumer-scale
storage on trading platforms and to make the platform pricing rule itself part of the strategic
environment.
The second strand of literature studies peer-to-peer and community energy markets, often
from the perspective of market architecture, clearing rules, and network constraints (Parag and
Sovacool, 2016; Mengelkamp et al., 2018; Morstyn et al., 2018; Le Cadre et al., 2020; Zhang et al.,
2020; Etesami et al., 2018; IRENA, 2020; Tushar et al., 2020). Related contributions study battery-
enabled peer-to-peer sharing, local pricing, and prosumer incentives such as flexibility provision
2

and cost recovery (He et al., 2021; Hoseinpour and Haghifam, 2024). Relative to that literature, we
focus on strategic price impact in a dynamic game and on how mechanism design and information
design shape the exercise of market power.
The third strand of literature uses machine learning to analyze strategic interaction and eval-
uate economic designs. Calvano et al. (2020) show that reinforcement-learning algorithms in
repeated pricing games can learn supracompetitive outcomes, Zheng et al. (2022) develop a multi-
agent learning framework for tax-policy design, and Curry et al. (2022) use deep multi-agent
reinforcement learning to compute approximate equilibria in microfounded general-equilibrium
environments. Closer to our application, Kastius and Schlosser (2022) study reinforcement learn-
ing in competitive dynamic pricing. Our computational contribution differs from model-free
approaches because we exploit the known, differentiable structure of the platform’s clearing
rule and backpropagate through the full trading environment, enabling a controlled comparison
between strategic and price-taking behavior. More broadly, the paper connects to the industrial
organization of electricity markets (Fabra, 2021; Fabra and Imelda, 2023; Wolfram, 1999; Hortaçsu
and Puller, 2008), bringing themes of strategic bidding and market power measurement to the
emerging setting of prosumer trading platforms.
The remainder of the paper is structured as follows. Section 2 introduces the model. Section 3.1
establishes equilibrium existence in the private-information game. Section 3.2 analyzes market
power in the observable-types benchmark. Section 4 presents the computational framework, data,
and pricing mechanisms. Section 5 reports the quantitative results. Section 6 concludes.
2. A model of prosumer trading
This section develops the model of prosumer trading that we are studying in this paper. The
players (i.e. prosumers) may have access to a battery to engage in intertemporal arbitrage and
self-consumption of their PV-generated electricity. As the battery state is private information, but
payoff-relevant for all players, the game features private information with infinite action spaces,
implying standard existence theorems do not apply and making equilibrium characterization
complex. Therefore, we first establish equilibrium existence in the full private-information game
in subsection 3.1 by mapping it into the framework of Myerson and Reny (2020), implying that a
perfect conditional ε-equilibrium exists for everyε >0. In subsection 3.2 we then study a simplified
benchmark setting in which players’ types and battery states are publicly observed. This allows us
to characterize the static and dynamic market power effects that arise in a transparent complete-
information setting. In what follows, we will refer to these two settings as the ‘private-types’ and
‘observable-types’ settings respectively.
2.1. Setup
Time is t∈ {1, . . . , T}and players are i∈I:={1, . . . , N}, where N <∞ and T <∞ . At date 0,
nature draws a type profile θ= (θ i)i∈I ∈Θ := Q i∈I Θi, where each Θi is finite, according to a
common prior π∈∆(Θ) . Player i privately observes θi at the start of period 1. A type θi specifies a
3

T-period sequence of inelastic demand and supply,
θi =

(dt i(θi), st i(θi)) T t=1, ℓ t i(θi) :=s t i(θi)−d t i(θi).
We interpretℓ t i(θi)as the exogenous physical surplus (deficit) in periodt. 1
Player i has a battery with state of charge Sit ∈[0, ¯Si], with Si1 = 0 (common knowledge). In
period t, player i chooses a battery flow bit, where a positive value denotes charging and a negative
value discharging, which updates the battery via
Si,t+1 =S it +b it.
Feasibility requires power bounds bit ∈[b i, ¯bi] and capacity bounds 0≤S it +b it ≤ ¯Si. Hence the
feasible set givenS it is
Bi(Sit) :=

max{bi,−S it},min{ ¯bi, ¯Si −S it}  .
We assume parameters are such that Bi(S) is nonempty for all S∈[0, ¯Si]. Given (Sit, θi), the
induced net import (net trade) is
xit :=d t i(θi) +b it −s t i(θi) =b it −ℓ t i(θi).
Define x+ := max{x,0} and x− := max{−x,0} so that x=x + −x −. Imports and exports are then
given by
mit :=x + it, q it :=x − it.
LetM t := P i∈I mit,Q t := P i∈I qit, andY t := P i∈I xit =M t −Q t.
2.2. Prices, platform settlement, and payoffs
External grid prices are given by (P E, PI ) for exports/imports respectively and are constant
throughout the game. The platform precommits to internal price schedules pc(M, Q)(consumer
price) and pp(M, Q)(producer price), which are time-invariant and common knowledge. Given
bounded battery flows and finite Θ, for each t there exists a compact set Kt ⊂R 2 + such that
(Mt, Qt)∈K t for all feasible action profiles and all θ∈Θ . Let K:= ST t=1 Kt. We impose the
following assumption on the price schedules on the attainable setK.
Assumption 1(Prices on the attainable set).The functions pc and pp are continuous on K and satisfy
for all(M, Q)∈K,
0≤P E ≤p p(M, Q)≤p c(M, Q)≤P I <∞.
Assumption 1 places weakly positive bounds on the platform prices, which are typically given by
the relevant feed-in tariff (i.e., the export price) and energy tariff (i.e., the import price). We can
1Assuming perfectly inelastic demand for electricity is standard in the literature. However, because players in our
setting can adjust their battery flow (which affects their total demand), this assumption could be relaxed as long as players
per-period demand remains bounded.
4

then define playeri’s period-tpayment to be
cit :=p c(Mt, Qt)m it −p p(Mt, Qt)q it,
so player i’s per-period payoff is uit :=−c it, and total payoff is ui := PT t=1 uit. The platform settles
any net imbalanceY t with the external grid at cost
Ct(Yt) :=P I Y + t −P E Y − t .
Platform profit in periodtis given by
Πt :=p c(Mt, Qt)Mt −p p(Mt, Qt)Qt −C t(Yt).
Thus, internal transfers cancel and total (players and platform) period-tsurplus equals−C t(Yt).
2.3. Information, timing, strategies, and beliefs
In each period t∈ {1, . . . , T}, (i) players simultaneously choose bit ∈B i(Sit); (ii) the platform
computes (Mt, Qt) from the action profile and θ, and (iii) payments cit are realized and the battery
state updates via Si,t+1 =S it +b it. Players do not observe payments or opponents’ actions; player
i’s only private information is her type θi (observed at t= 1 ) and her own past battery flows. 2
There is no payoff after periodT, i.e. there is no salvage value.
Playeri’s private history at the start of periodtis
hit :=

θi, bi1, . . . , bi,t−1

, h i1 :=θ i.
The battery state Sit = Pt−1 τ=1 biτ (with Si1 = 0 ) is computed from hit, and feasibility requires
bit ∈B i(Sit(hit)). A (behavioral) strategy for playeriin periodtis a stochastic kernel
σit(· |hit)∈∆(B i(Sit)).
A strategy profile isσ= (σ i)i∈I with σi = (σit)T t=1. A belief system is a collectionµ= (µ it)i∈I, t∈{1,...,T}
where each
µit(· |hit)∈∆

Θ−i ×
Y
j̸=i
[0, ¯Sj]

represents player i’s posterior over (θ−i, S−i,t) at information set hit. Beliefs are consistent with
(π, σ)if, for each player i and period t, µit(· |hit) coincides with a regular conditional distribution
of(θ −i, S−i,t)givenh it under the probability measure induced by(π, σ).
Given(σ, µ), playeri’s continuation value can be defined recursively by
Vit(hit;σ, µ) :=Eπ,σ,µ
" TX
τ=t
uiτ

 hit # , V i,T+1 ≡0.
2Payments cit are deterministic functions of the full action profile and types. We exclude them from observed signals
in the primitive description for expositional convenience. In subsection 3.1 we show that allowing each player to observe
her own realized payment (equivalently per-period payoff) is without loss via a purely formal reporting stage, while
maintaining compatibility with the projected-signal structure required by Myerson and Reny (2020).
5

The equilibrium concept for the private-information game is introduced in subsection 3.1. For the
observable-types benchmark we use Markov perfect equilibrium as formally defined in subsec-
tion 3.2.
3. Equilibrium analysis
3.1. Equilibrium existence with private types
We establish equilibrium existence in the full private-information game of section 2 by mapping
it into the framework of Myerson and Reny (2020). Their Theorem 9 .3 guarantees existence of a
perfect conditional ε-equilibrium for every ε >0 in any regular projective game. We verify that
our game satisfies their conditions R.1–R.5.
Proposition 1(Private Types).For every ε >0, the private-information game possesses a perfect condi-
tional ε-equilibrium [Myerson & Reny, 2020, Theorem 9 .3]. Moreover, this existence result is unchanged
(without loss) if each player also observes her realized per-period payment cit (equivalently uit =−c it) at
the end of each period.
Proposition 1 establishes that an approximate equilibrium exists in the full private-information
game for any ε >0. This result is non-trivial because the game combines private information
with continuous actions and an expanding private history: each player’s battery state Sit is private
information (it is determined by past battery flows that only the owner observes) but it is payoff-
relevant for all players through its effect on aggregate quantities and thus on prices. Standard
existence theorems for finite Bayesian games do not directly apply in this setting.
The proof proceeds by mapping an equivalent representation of the game into the framework of
Myerson and Reny (2020). The key elements are: (i) representing battery feasibility via an intended
action in a fixed compact interval together with an implemented flow given by projection onto
Bi(Sit), which makes the available (intended) action set independent of the signal (Condition R.1),
and (ii) exploiting that each player’s private signal is a projection of the outcome history onto
her own coordinates (Condition R.2). Continuity of payoffs on the attainable set (Assumption 1),
compactness of action sets, and the finiteness of Θ establish the remaining regularity conditions.
Allowing a player to observe her own per-period payment cit is without loss because it can be
incorporated into the projected-signal structure by adding a purely formal reporting stage (as
done in the proof), so the same existence conclusion continues to hold.
In a perfect conditional ε-equilibrium, no player can improve her expected continuation payoff
by more than ε at any information set, conditional on reaching that information set. The parameter
ε thus bounds the expected continuation gain from deviation in monetary units. Having established
equilibrium existence in the full private-information game, we now turn to the observable-types
benchmark in subsection 3.2 to characterize the market power mechanisms that drive strategic
behavior.
3.2. Market power effects with observable types
This section analyzes a benchmark setting in which the type profile θ is publicly observed before
period 1 and battery states are also publicly observed. All other primitives (battery constraints,
6

price schedules, and payoffs) are unchanged. This allows us to provide a clean characterization of
the static and dynamic incentives for players that are driven by market power.
In this setting, the public state at the start of periodtis
ωt := (t, θ, St), S t := (Sit)i∈I ∈
Y
i∈I
[0, ¯Si],
with ω1 = (1, θ,0)where 0 denotes the zero vector in Q i∈I [0, ¯Si]. In each period t∈ {1, . . . , T},
players observe ωt, choose bit ∈B i(Sit) simultaneously, payoffs accrue, and the state updates via
Si,t+1 =S it +b it.
A (mixed) Markov strategy for playeriis a collectionβ i = (βit)T t=1 where, for eacht,
βit(· |θ, St)∈∆

Bi(Sit)

,(θ, S t)∈Θ×
Y
j∈I
[0, ¯Sj].
Let β= (β i)i∈I be a Markov strategy profile. For each t and public state (θ, St), β induces a
distribution over the action profile bt = (bit)i∈I and thus over (Mt, Qt, Yt) and the payoff vector
(uit)i∈I . The next-period state isS t+1 =S t +b t componentwise.
Given β, define player i’s continuation value recursively by Wi,T+1 ≡0 and, for t∈ {1, . . . , T},
Wit(θ, St;β) :=E β
h
uit(bt;θ, St) +W i,t+1(θ, St+1;β)

 θ, St i ,
where the expectation is taken overb t ∼β t(· |θ, St) := Q j∈I βjt(· |θ, St).
A Markov strategy profile β∗ is aMarkov perfect equilibrium (MPE)if for every i∈I , every
t∈ {1, . . . , T}, and every public state (θ, St), the distribution β∗ it(· |θ, St) assigns probability 1 to
actionsb it ∈B i(Sit)that maximize
Eβ∗
h
uit

(bit, b−i,t);θ, St

+W i,t+1

θ, St + (bit, b−i,t);β ∗

 θ, St, bit i
givenβ ∗ −i,t(· |θ, St).
We place the following shape and curvature assumptions on the price schedules.
Assumption 2(Monotonicity and curvature of price schedules).The functions pc and pp are contin-
uously differentiable and satisfy:
(i) The price schedule pc is weakly increasing in M for each fixed Q≥0 and for every Q≥0 and every
M−i ≥0, the total import-cost function
m pc(M−i +m, Q)
is convex inm.
(ii) The price schedule pp is weakly decreasing in Q for each fixed M≥0 and for every M≥0 and
everyQ −i ≥0, the total export-revenue function
q pp(M, Q−i +q)
7

is concave inq.
(iii) For the strict inequality in Proposition 2(ii), we additionally require that pp is strictly decreasing in
Qat the relevant arguments, i.e.∂ Qpp(M, Q)<0whenever the solution is interior.
Assumption 2 places intuitive shape assumptions on the price schedules. The consumption price
increases in consumption (import) and the sell price decreases in supply (export). In addition,
to guarantee existence of pure-strategy equilibria in the one-shot and continuation games in
Proposition 2, the respective cost and revenue functions are assumed to be convex and concave,
respectively.
The MMR mechanism satisfies Assumption 2 globally (see Appendix C.4). The SDR and linear
mechanisms satisfy the monotonicity conditions and the curvature conditions within each smooth
pricing regime, but price clamping (for the linear mechanism) and regime-boundary effects
(for SDR) can create kinks that violate global concavity or convexity. For these mechanisms, we
verify in Appendix C.4 that thetotalperiod- t objective—stage payoff plus continuation value—
remains concave in bit on the attainable set, which is the condition actually used in the proof of
Proposition 2(i).
To analyze market power effects, we define two benchmarks for player i at state (θ, St). Fix a
period t and a public state (θ, St) in the observable-types benchmark. For any opponents’ action
profile b−i,t ∈ Q j̸=i Bj(Sjt), let (M−i,t, Q−i,t) denote the induced aggregates and define player i’s
(period-t) import/export quantities as
mit(bit) :=

bit −ℓ t i(θi) + , q it(bit) :=  ℓt i(θi)−b it + .
WriteS t+1 =S t + (bit, b−i,t).
Let W ∗ i,t+1(θ,·) denote player i’s equilibrium continuation value at t+ 1 induced by an MPE β∗,
and let L∗ −i,t(· |θ, St) denote the distribution of b−i,t induced by β∗ −i,t(· |θ, St). In MPE, the best
reply by playeriis given byb it ∈B i(Sit)that maximizes
Eb−i,t∼L∗ −i,t
h
−p c(Mt, Qt)m it(bit) +p p(Mt, Qt)q it(bit) +W ∗ i,t+1(θ, St+1) i ,
where (Mt, Qt) depend on (bit, b−i,t, θ). Let b∗ it denote the resulting battery action and write q∗ it :=
qit(b∗ it)for the corresponding export quantity.
The two benchmarks are defined as follows. First, we defineprice-takingbehavior as a bench-
mark in which the player optimizes individually but treats the internal price level as given when
evaluating marginal deviations, i.e. the player ignores the effect of her own action on the price
schedule. Formally, fix opponents’ actions b−i,t and let player i’s objective be written as a function
of bit ∈B i(Sit). A price-taking action bP T it is any action satisfying the KKT conditions of player i’s
problem after removing the own-price-impact terms from the stationarity condition (the terms
generated by ∂M pc and ∂Qpp), while keeping the realized price levels pc(Mt, Qt) and pp(Mt, Qt)
unchanged.
On the interior export branch ( q=ℓ t i(θi)−b it >0 ), with opponents fixed and Qt =Q −i,t +q ,
8

this means that the strategic stationarity condition
pp(M−i,t, Q−i,t +q) +q ∂Qpp(M−i,t, Q−i,t +q) +∂ qΨi(q) = 0
is replaced by the price-taking condition
pp(M−i,t, Q−i,t +q) +∂ qΨi(q) = 0,
together with the corresponding boundary/complementarity conditions. Here Ψi(q) denotes the
continuation term expressed in the export variable q (and Ψi ≡0 in the stage-game). We denote
the associated export quantity byq P T it .
Second, consider that a social planner chooses (bjt)j∈I (and continuation actions) to minimize
total grid cost PT τ=t Cτ (Yτ ) subject to all feasibility and battery constraints. Let bSP it (θ, St) denote
player i’s period-t component of a planner-optimal plan (if not unique, any selection) and qSP it :=
qit(bSP it )the corresponding export quantity.
For the observable-types setting, we can then state the following result.
Proposition 2(Observable Types).For the observable-types setting and under Assumptions 1 and 2:
(i) A pure-strategy Nash equilibrium exists in the one-shot game. Moreover, for everyε >0the dynamic
observable-types game possesses a perfect conditional ε-equilibrium (by the same Myerson and Reny
(2020) argument as in Proposition 1). If the equilibrium continuation values W ∗ it(θ, St) are concave
inS it for eachi,t,θ, andS −i,t, then a pure-strategy MPE exists in the dynamic game.
(ii) Fix a period t and state (θ, St), and consider the associated one-shot game. For any player i with
an interior export solution (q ∗ it >0),
q∗ it ≤q P T it =q SP it
with strict inequality in the first comparison whenever pp(M, Q)is strictly decreasing in Q at the
relevant arguments.
(iii) Fix any t < T, player i, state (θ, St), and opponents’ continuation path (b−i,τ )T τ=t . If both period-t
solutions are interior import choices and the marginal stored unit is exported at someτ > t, then
b∗ it ≤b P T it .
(iv) Fix any t < Tand state (θ, St). Let (bP T iτ )T i,τ=t denote the price-taking continuation from (θ, St),
and let(b SP,t iτ )T i,τ=t be a planner-optimal continuation. If
X
i
bP T it < X
i
bSP,t it ,
then, if the additional period- t charge is fully discharged through future exports, there exists some
τ > tsuch that
QSP,t τ > QP T τ .
9

Proposition 2 clarifies the static and dynamic market-power effects that arise in the observable-
types setting. Part(i)first establishes existence of a pure-strategy Nash equilibrium in the one-shot
stage game. It also notes that the dynamic observable-types game admits a perfect conditional
ε-equilibrium for every ε >0, and that under concavity of the equilibrium continuation values a
pure-strategy MPE exists in the dynamic game. We make this concavity condition explicit because
it is not directly implied by Assumptions 1 and 2, but can be shown to hold for the mechanisms stud-
ied in this paper (see Appendix C.4). Part(ii)then provides an intuitive ranking among exporting
players in the stage game: prosumers will export weakly less than the corresponding price-taking
benchmark, while the price-taking and social-planner export choices coincide. Part(iii)provides
the dynamic analogue and similarly shows that a strategic prosumer charges weakly less than a
price-taker because future sales are valued at marginal revenue rather than price. Finally, part(iv)
clarifies the planner comparison from part(ii)for the dynamic game. If a planner-optimal contin-
uation charges more in period t than the price-taking continuation and this additional charge is
later discharged through exports, then the planner must export strictly more than the price-taking
path in at least one future period. This implies that whenever prosumers undercharge relative to a
price-taking player and thereby limit future exports, a stricter ranking of quantities supplied arises
in the dynamic game than in the stage game. Note that the corresponding strategic behaviour does
not arise among net importers for whom minimizing imports is always a best-response both in
MPE and when being price-takers.
20
 10
 0 10 20
xi
20
10
0
10
20
xj
Static NE
Social planner
Price-taking
BRi
BRj
Figure 1: Best-response curves and convergence to Nash equilibrium in a two-prosumer stage
game with net exporters.
Figure 1 illustrates the strategic interaction for the simplest case: a single-period game with two
symmetric prosumers and fixed exogenous demand to ensure the price reacts to players’ actions. 3
In the illustrated case, both players have positive surplus ( ℓt i >0 ) and hence the equilibrium
lies in the both-export region ( xi, xj <0 ), where the game becomes a Cournot duopoly against
the exogenous demand. The best-response curves BRi (solid) and BRj (dashed) are downward-
3If both players are net exporters, there is no demand on the platform. The price mechanisms we consider will then
default to the lower bound, i.e. the constant export price P E . For the illustration of the strategic interaction we therefore
add a positive exogenous demand.
10

sloping—quantities are strategic substitutes—and intersect at the symmetric Nash equilibrium
x∗ i =x ∗ j =−D ext/3. Each player withholds exports relative to the price-taking optimum because
she internalizes the effect of her supply on the market-clearing price; the resulting quantity is
strictly less than the price-taking export. The social planner solution coincides with the price-
taking optimum, illustrating the ranking developed in Proposition 2 ofq SP it =q P T it ≥q ∗ it.
The gradient-play trajectories (thin curves with arrows) show the adjustment dynamics under
simultaneous best-response improvement: from any initial action profile, the system converges
to the Nash equilibrium. In the upper right quadrant, both players are net importers and the
best-response for a net importer in the stage game is to minimize their imports. Thus the trajectory
is a diagonal line. This can also be seen in the dashed indifference curves shown for player i which
are vertical in the top right quadrant: the best-response is to move horizontally towards xi = 0. In
the top left and bottom right quadrants in turn, one player is a net exporter and the other player
a net importer. In this case, the net importer continues to want to minimize imports, while the
net exporter faces a convex indifference curve and engages in strategic withholding. Because of
this strategic incentive, the curvature of player i’s indifference curves reflects the concavity of
the export-revenue function q pp(M, Q−i +q) from Assumption 2(ii). In the dynamic game, these
stage game incentives interact with the intertemporal incentives. First, a player who anticipates
future market power effects may strategically undercharge her battery today in order to limit her
exports tomorrow. Second, a player may charge in order to sell at a higher price in the future and
engage in arbitrage. This incentive can be greater than the market power effects, depending on
the realizations of types—including the expectations of future realizations—and the price schedule
design.
Figure 2: Best-response curves and convergence to MPE in a two-prosumer, two-period game with
net exporters.
Figure 2 illustrates this for the simplest case of two symmetric players and two periods with
exogenous demand in both periods and a positive battery state in the first period. The stage
11

game equilibrium in the first period (left panel) sees both players discharging their battery to the
maximum. In MPE however, both players insteadchargetheir battery—incurring extra cost—in
order to discharge more in the second period (right panel) when prices are higher, i.e. to engage
in intertemporal arbitrage. But players charge less and subsequently also discharge less than
either a price-taking player or the social planner would, implying they are withholding capacity
because they correctly account for the price effect their discharging will have in the second period.
As before, the gradient-play trajectories show that the best-response dynamics lead players to
converge to the MPE. Note that the intersection of the best-response curves and the equilibrium
in the second period do not coincide, because the restriction on the battery size limits players to
discharging a total amount in the second period that is below the equilibrium level.
The observable-types setting can be interpreted as a complete-information benchmark for the
private-types model: it corresponds to augmenting the private-information game with a public
signal that reveals (θ, St) before play in each period. In that case, players’ posteriors are degenerate
and the period-by-period optimization that underlies Markov perfect equilibrium coincides with
the complete-information best-response analysis in Proposition 2. In the private-types game,
players instead choosebit based on their private history and beliefs about(θ−i, S−i,t). Nevertheless,
the market power effects identified in Proposition 2 translate directly to this case: conditional on
any information set at which a player is an interior exporter, her marginal incentive accounts for the
effect of qit on the producer price through∂Qpp, so exports are shaded relative to the corresponding
price-taking benchmark that removes own-price-impact terms from the stationarity condition.
Similarly, if the marginal unit stored today is expected to be exported in a future period, the
dynamic analogue arises because future sales are valued at (expected) marginal revenue rather
than (expected) price. Thus, while Proposition 2 provides sharp state-by-state comparative statics
under full observability, in the private-information game the same mechanisms operate up to the
approximation errorε.
4. Computational framework
4.1. Multi-agent differentiable market-clearing
Each controllable agent i is represented by a feedforward neural network f ϕi mapping her ob-
servation (battery state, time, demand, PV generation, and a price signal) to a battery action.
Training proceeds by unrolling the full T -period trajectory and computing policy gradients via
backpropagation through the entire computational graph. The method builds on the deep hedging
paradigm of Buehler et al. (2019) and is developed in detail in Eschenbaum et al. (2026). Because the
platform’s clearing rule is a known, differentiable mapping from aggregate quantities to prices, the
gradient ∇ϕi ¯C i can be computed exactly through the chain bit 7→x it 7→(M t, Qt)7→(p c, pp)7→c it,
providing each agent with exact information about her price impact. At each period, agents’ actions
and market prices are determined jointly through a differentiable tatonnement procedure that
iterates price estimates to convergence within the automatic differentiation graph (Appendix B.2).
The method provides a controlled switch between two learning modes. Instrategicmode, the
gradient propagates through the clearing rule, so each agent’s update accounts for her effect on
prices; per-agent gradients ensure each agent optimises her own cost, not the system cost. In
12

price-takingmode, a stop-gradient operator detaches prices from the graph: agents optimise while
treating prices as exogenous, corresponding to the price-taking benchmark of Section 3.2. The
two modes share identical architectures and hyperparameters; the only difference is whether the
gradient passes through the price formation step, providing a controlled ablation for quantifying
market power. As a welfare benchmark, we also train a centralised network minimising total
grid settlement cost P t Ct(Yt). Architecture, hyperparameters, and convergence diagnostics are
reported in Appendix B.
Convergence to Nash equilibrium is assessed via unilateral deviation regret. For each con-
trollable agent, we freeze all other agents’ policies and retrain a single agent. 4 We train on 1,000
stochastic days and evaluate on 100 held-out days, averaging over five seeds. We report four
metrics: the ε-regret; the withholding ratio w:= (q PT −q S)/qPT; the average daily grid cost
¯C:= (1/D) P d P t Ct(Y d t ); and per-agent payoffs (i.e., cost).
4.2. Data and calibration
Time is discretized into T= 24 hourly periods per day (∆t= 1 h). The baseline community consists
of six agent types (Table 1): three controllable types with batteries (prosumer A, large prosumer B,
pure storage C) and three passive types (PV generator D, small PV E, consumer F). The battery is
lossless (Si,t+1 =S it +b it) with charge/discharge rate¯bi = ¯Si/3 and initial state Si1 = 0.5 Although
the model sets Vi,T+1 ≡0 , the computation includes a terminal value Vi,T+1 =P E ·S i,T+1 to
prevent degenerate end-of-day discharge; since this is linear in Si,T+1 , the results of Propositions 1
and 2 are unaffected.
Table 1: Agent types in the baseline platform.
Type Role PV (kWp) Battery (kWh) Demand (kWh/d) Controllable
A Prosumer 8 8 13 Yes
B Large prosumer 11 14 15 Yes
C Pure storage 0 10 0 Yes
D PV generator 8 0 10 No
E Small PV 3 0 12 No
F Consumer 0 0 14 No
Table 1 shows the parameterization in our baseline platform setting. We distinguish between
six types of prosumers for tractability. Three possess controllable assets, in our baseline setting
batteries, and three do not. Note that having pure consumers on the platform is important to study
the market power incentives, as evening (net) demand for electricity is necessary for platform
prices to be able to react to (net) sellers decisions. We fix the charge/discharge rate at ¯bi = ¯Si/3.
PV generation follows a sinusoidal clear-sky curve (sunrise 6h, sunset 18h) scaled by agent-
specific peak capacity ¯si and perturbed by a mean-reverting AR(1) process with random cloud
dips. Demand follows a composite time-of-use profile (morning and evening peaks, low midday
trough) perturbed by an AR(1) process with random activity pulses and log-normal daily variation
(≈ ±20%). Full stochastic model parameters are in Appendix B. Figure 3 shows example patterns.
4Specifically, we freeze other players and retrain agentifor350episodes and then computeε i :=c eq i −c BR i . 5During training, initial battery states are drawn uniformly from [0, ¯Si] for exploration; all reported results use Si1 = 0.
13

(a) PV generations t i
 (b) Demandd t i
Figure 3: PV generation and demand patterns (T= 24) with three example stochastic days.
Figure 3 shows the photovoltaic (PV) and demand underlying patterns and three realized
example days for one agent. The actual realizations vary depending on the stochastic perturbations,
as discussed above.
4.3. Pricing mechanisms
The platform’s pricing rule maps aggregate supply Qt (total selling power) and demand Mt (total
buying power) to a producer pricepp and consumer price pc, both within the tariff corridor[P E, PI ]
where P E = 0.05 USD/kWh (feed-in tariff) and P I = 0.30 USD/kWh (retail tariff). We implement
three mechanisms that are typical in the literature.
The baseline mechanism is the supply-demand ratio (SDR) applied for example in (Liu et al.,
2017). Formally, it is given by ρt :=Q t/Mt. The producer (sell) and consumer (buy) prices are,
respectively
pSDR p =



P E
P E ·P I
(P I −P E)ρ t +P E
ifρ t >1,
ifρ t ≤1,
pSDR c =



P E
pSDR p ·ρ t +P I ·(1−ρ t)
ifρ t >1,
ifρ t ≤1.
When supply exceeds demand ( ρt >1 ), all volume clears at the feed-in tariff. When demand
exceeds supply, the producer price rises hyperbolically toward P I and the consumer price is a
weighted average of the internal and external prices.
An alternative mechanism we consider is the mid-market rate (MMR), used in (Long et al.,
14

2017). pmid := (P E +P I )/2 = 0.175 USD/kWh. The short side of the market faces pmid; the long
side is adjusted toward the external tariff via pro-rata weighting:
pMMR p =



pmid ifM t ≥Q t,
(Mt ·p mid + (Qt −M t)·P E)/Qt ifM t < Qt,
pMMR c =



pmid ifM t ≤Q t,
(Qt ·p mid + (Mt −Q t)·P I )/Mt ifM t > Qt.
The MMR mechanism produces less price variation than SDR, as the clearing price depends only
on which side is short, not on the magnitude of the imbalance.
Finally, we also consider a simple linear pricing mechanism. This mechanism implements an
inverse-demand clearing price
pLIN =p mid −κ(Q t −M t),clamped to[P E, PI ],
where κ= (P I −P E)/10 = 0.025 USD/kWh2 spans the tariff corridor over a ±5 kWh imbalance.
The long side clears pro-rata at the internal price, with the remainder settled at the external tariff:
pLIN p = min(Mt/Qt,1)·p LIN + (1−min(M t/Qt,1))·P E,
pLIN c = min(Qt/Mt,1)·p LIN + (1−min(Q t/Mt,1))·P I .
The linear mechanism has a particularly simple structure. The clearing price is a smooth, monotone
function of net supply, making it the most transparent for identifying market power effects.
Note that all three mechanisms produce prices in [P E, PI ] and satisfy Assumption 1. All three
mechanisms satisfy the monotonicity conditions of Assumption 2: an increase in aggregate supply
weakly reduces the producer price, and an increase in aggregate demand weakly raises the con-
sumer price, with strict monotonicity whenever the price is in the interior of the tariff corridor
[P E, PI ]. The convexity and concavity conditions of Assumption 2 hold globally for the MMR mech-
anism. For the SDR and linear mechanisms, the curvature conditions hold within each smooth
pricing regime, but can fail at regime boundaries: the SDR mechanism has a convex kink in the
export-revenue function at Q=M and loses import-cost convexity at extreme supply-demand
ratios, while the linear mechanism’s price clamping at P E and P I creates kinks that can break
both global concavity and convexity. For both mechanisms, we verify in Appendix C.4 that the total
objective (stage payoff plus continuation value) remains concave in bit on the attainable set. The
concavity of the equilibrium continuation value function required for pure-strategy MPE existence
is also verified in that appendix.
5. Computational Results
We present computational results from three treatments designed to test the theoretical predictions
of Section 3.2: a baseline ordering that confirms the cost ranking of Proposition 2, a competition
treatment that varies the number of storage operators, and a heterogeneity treatment that com-
15

pares pricing mechanisms across the six agent types. All results are averaged over five random
seeds; error bars or bands show ±1 standard deviation across seeds. The baseline community is
described in Table 1. For each treatment, we train price-taking and strategic benchmarks—and,
where noted, a social planner—using the computational framework of Section 4. Full experimental
configurations and hyperparameters are reported in Appendix B.
5.1. Baseline ordering
We fix the SDR mechanism with private information and train all three regimes on the baseline
community (Table 1). Table 2 reports grid cost, community cost, and the withholding ratio.
Table 2: Baseline cost ordering (SDR mechanism, five seeds). Standard deviations in parentheses.
Grid cost is the community’s total settlement with the external grid; since internal transfers cancel,
grid cost equals the welfare-relevant total surplus (up to sign).
Regime Grid cost (USD/day)
Social planner 5.67 (0.67)
Price-taking 5.71 (0.58)
Strategic 6.07 (0.45)
Strategic−Price-taking+0.36 [+6.3%]
Withholding ratiow0.029 (0.039)
Grid cost follows the ordering predicted by Proposition 2: Planner (USD 5.67/day)≤ Price-taking
(5.71) < Strategic (6.07). The strategic premium of USD 0.36/day ( 6.3%) is the aggregate welfare
loss from export withholding (w= 0.029 ). The planner–price-taking gap is small (USD 0.04/day),
indicating that the primary source of inefficiency is strategic behaviour. Since internal transfers
between players and the platform cancel, grid cost is the welfare-relevant measure of total surplus;
per-agent costs, reported in subsequent tables, capture only the distribution of surplus across
participants.
0 4 8 12 16 20 24
Hour (Planner)
0
2
4
6
8
10
12
14Battery SOC (kWh)
A
B
C
0 4 8 12 16 20 24
Hour (Price-Taking)
A
B
C
0 4 8 12 16 20 24
Hour (Strategic)
A
B
C
Figure 4: Average battery SOC over 24 hours by regime (SDR, five seeds, ±1 s.d.). The planner
uses all three batteries; storage agent C is idle under price-taking. Strategic agents retain higher
terminal SOC.
Figure 4 shows battery SOC over 24 hours. All regimes follow the expected diurnal cycle: charge
16

during midday PV surplus, discharge during the evening peak. The planner uses all three batteries
aggressively, including agent C (peak SOC 6.3 kWh of 10 kWh). Under price-taking, C is nearly idle
(peak 0.4 kWh): without own generation or demand, the bid–ask spread does not compensate
enough round-trip trading.
0 5 10 15 20
Hour
0.05
0.10
0.15
0.20
0.25
0.30Sell price (USD / kWh)
Planner
Price-Taking
Strategic
0 5 10 15 20
Hour
Buy price (USD / kWh)
Planner
Price-Taking
Strategic
Figure 5: Average sell and buy prices over 24 hours (SDR, five seeds, ±1 s.d.). Strategic play raises
evening buy prices by≈0.03USD/kWh relative to price-taking.
Figure 5 shows market prices. Nighttime prices equal the retail tariff ( P I = 0.30); midday PV
surplus pushes prices to USD 0.08–0.13/kWh across regimes with minimal inter-regime differences.
The key distinction appears in the evening (hours18–23): strategic buy prices average USD0.16/kWh
versus USD 0.13/kWh under price-taking—a premium of USD 0.03/kWh (+23%). This is the price-
side reflection of quantity withholding: restricted evening exports shift the supply–demand ratio,
raising the clearing price at the expense of passive consumers. The planner pushes evening prices
down to USD0.07–0.12/kWh through aggressive discharge.
Table 3 reports the unilateral-deviation ε-regret for each controllable agent. The regret is
computed by freezing all opponents’ policies at their strategic equilibrium values and retraining the
focal agent as a best-responder for 350 episodes (see Section 4.1). All regrets are below USD0.01/day
in absolute value, confirming that the strategic outcome is an approximate Nash equilibrium: no
agent can reduce her daily cost by more than one cent through unilateral deviation.
Table 3: Unilateral-deviation ε-regret (USD/day, SDR, five seeds).εi :=C eq i −C BR i ; positive values
mean the equilibrium cost exceeds the best response (agent could improve), negative values mean
the best-responder fared worse. Standard deviations in parentheses.
Agent Typeε i (USD/day)|ε i|/|C eq i |
A Prosumer (8 kWh)+0.005 (0.004) 0.7%
B Large prosumer (14 kWh)−0.002 (0.005) 0.5%
C Pure storage (10 kWh)+0.006 (0.008) —
5.2. Competition and market power
We vary the number of symmetric storage agents N∈ {1,2,3} , holding total capacity fixed at
10 kWh ( ¯S= 10/N per agent, ¯b= ¯S/3). Two passive agents (D, E) provide supply and demand. The
17

mechanism is SDR; all results average five seeds.
Table 4: Grid cost, withholding, and price impact by number of storage agents N (SDR, five seeds).
Standard deviations in parentheses. Price impact computed via automatic differentiation through
the clearing rule.
Grid cost (USD/day) Gap Withholding Price impact
NStrategic Price-taking (%)w|∂p/∂b i|
1 2.77 (0.18) 2.02 (0.23)+37 .1 0.707 (0.036) 0.198 (0.002)
2 2.45 (0.23) 2.10 (0.21)+16.7 0.342 (0.068) 0.162 (0.002)
3 2.30 (0.23) 2.28 (0.24)+0.9−0.005 (0.214) 0.140 (0.002)
The results show the expected patterns. With a single storage agent, the strategic grid cost
exceeds the price-taking benchmark by 37% and the agent withholds 71% of competitive exports.
A duopoly reduces the gap to 17% (withholding 34%). With three storage agents, strategic and
price-taking outcomes become statistically indistinguishable. The largest welfare gain comes
from the first entrant, consistent with classic oligopoly theory. Figure 6 illustrates the mechanism
directly. Total battery utilisation under strategic play rises monotonically in N . Whereas a single
storage agent charges to a peak SOC of only 1.9 kWh (out of a total of 10 kWh), two competing
agents reach 3.1 kWh and three competing agents reach 4.1 kWh. Competition therefore erodes
each agent’s incentive to withhold, pushing battery behaviour toward the competitive outcome.
0 4 8 12 16 20 24
Hour (N=1)
0
1
2
3
4
5Total battery SOC (kWh)
0 4 8 12 16 20 24
Hour (N=2)
0 4 8 12 16 20 24
Hour (N=3)
Figure 6: Total battery SOC over 24 hours under strategic play, by number of competing storage
agents N (SDR, five seeds, ±1 s.d.). Battery utilisation increases monotonically with competition.
Table 5 shows the resulting payoff (or cost) by agent type. With a single storage agent (a monop-
olist), this agent earns USD 0.12/day in the approximate equilibrium compared to USD 0.04/day
when ignoring their own price impact. This additional rents is redistributed from inflexible agents
whose costs rise by USD 0.36 (D) and USD 0.46 (E). The monopolist captures only USD 0.08/day—
roughly 10% of passive agents’ losses—with the remaining 90% dissipated as deadweight through
increased grid reliance. Under a duopoly, this rent reduces by half. With three competing storage
agents, the distributional effects vanish.
18

Table 5: Per-agent costs by market structure (USD/day, five seeds). Battery cost is the per-agent
average across N symmetric agents. ∆ =Strategic−Price-taking ; negative values indicate rent
extraction. Standard deviations in parentheses.
NAgent Price-taking Strategic∆
1 Battery (×1)−0.04 (0.02)−0.12 (0.01)−0.08
PV generator (D) 0.42 (0.13) 0.77 (0.09)+0.36
Small PV (E) 1.62 (0.12) 2.07 (0.08)+0.46
2 Battery (×2, avg)−0.03 (0.03)−0.05 (0.01)−0.02
PV generator (D) 0.47 (0.11) 0.63 (0.12)+0.16
Small PV (E) 1.68 (0.11) 1.88 (0.12)+0.20
3 Battery (×3, avg)−0.02 (0.04)−0.03 (0.01)≈0
PV generator (D) 0.55 (0.12) 0.55 (0.12)≈0
Small PV (E) 1.79 (0.13) 1.78 (0.12)≈0
5.3. Heterogeneity and mechanism design
We now exploit the full heterogeneity of the baseline community to compare the distributional
consequences of strategic play across pricing mechanisms. Table 6 reports the per-agent cost
difference, where we define ∆ =Strategic−Price-taking in all three mechanisms. As before, we
provide the results across five seeds.
Table 6: Per-agent strategic premium∆i =C S i −C P T i (USD/day, five seeds). Negative values indicate
that the agent benefits from strategic play. The grid cost row reports the difference in total grid
settlement cost. Standard deviations in parentheses.
∆: Strategic−Price-taking (USD/day)
Agent Type SDR MMR LINEAR
A Prosumer (8 kWh)−0.018 (0.009)−0.002 (0.023)−0.054 (0.028)
B Large prosumer (14 kWh)−0.005 (0.020)−0.007 (0.035)−0.028 (0.033)
C Pure storage (10 kWh)−0.032 (0.008) 0.000 (0.000)−0.001 (0.002)
D PV generator+0.120 (0.053)+0.007 (0.009)+0.042 (0.015)
E Small PV+0.134 (0.063)+0.001 (0.006)+0.025 (0.010)
F Consumer+0.139 (0.070)−0.001 (0.007)+0.017 (0.009)
Grid cost∆ +0.491 (0.182)−0.011 (0.023)+0.042 (0.038)
Withholdingw0.040 (0.029)−0.003 (0.008) 0.033 (0.008)
The distributional pattern is consistent across mechanisms—battery owners gain, passive
agents lose—but the magnitudes differ by an order of magnitude. Under SDR, the pattern follows
directly from the baseline withholding mechanism: battery-equipped agents lower their costs by
USD 0.005–0.032/day, while passive agents face increases of USD 0.12–0.14/day. The total grid cost
increase (USD 0.49/day) exceeds battery owners’ combined savings (USD 0.06/day) by a factor of
six, so the welfare loss is predominantly deadweight.
The choice of pricing mechanism has a substantial effect on these findings. Under MMR, all
per-agent gains from equilibrium play are indistinguishable from zero: the fixed mid-market rate
eliminates the price sensitivity that strategic agents exploit (w≈0 ). With a linear price mechanism,
19

withholding is comparable to SDR (w= 0.033 ) and battery owners benefit from strategic play, but
the grid cost increase is negligible ( ∆≈0 ). The linear mechanism’s smooth price response allows
individual agents to exercise market power, but the surplus they extract comes almost entirely
from redistribution rather than deadweight loss—grid settlement cost is roughly identical even as
the division of surplus on the platform shifts toward battery owners.
5.4. Discussion: magnitudes, information, and platform value
We conclude the results section by assessing the value of the platform for participating players and
examining how information design affects our results. We assume that without the platform, each
agent settles exclusively with the external grid at the retail tariff P I = 0.30 USD/kWh (imports)
and feed-in tariff P E = 0.05 USD/kWh (exports). Table 7 projects annual costs with and without
the platform (we assume the platform operates under the SDR mechanism).
Table 7: Annual cost projection (USD/year, SDR, five seeds). “No platform” assumes exclusive grid
settlement at regulated tariffs with self-consumption of own PV . Platform saving = No platform −
Price-taking. Market power cost=Strategic−Price-taking.
No platform Platform (annual) Platform Market power
Agent (grid only) Price-taking Strategic saving cost
F (consumer, 14 kWh/d) 1,585 921 971 664 51
E (small PV , 12 kWh/d) 884 588 637 295 49
D (PV gen, 10 kWh/d) 375 140 184 235 44
Community (6 agents) 4,102 2,071 2,250 2,080 179
The pure consumer F provides the cleanest comparison: without a platform, F settles ex-
clusively with the grid at the retail tariff, paying USD 1,585/year. Platform trade reduces this to
USD 921/year (−42%), and strategic behaviour adds USD51/year back—roughly8% of the platform’s
saving. The PV generator D benefits most from the platform in relative terms ( −63%), because
it can sell surplus generation internally at prices well above the feed-in tariff. The community-
wide cost of market power is USD 179/year, of which battery owners capture roughly USD 21 in
rents; the remaining 89% is dissipated as deadweight loss through increased grid reliance. The
platform is thus overwhelmingly valuable despite strategic distortions, but the welfare loss falls
disproportionately on passive agents, reinforcing the case for careful mechanism design.
We further compare two information structures under the SDR mechanism (as before with five
seeds):private information, where each agent observes only her own type and battery state, and
price observation, where agents additionally observe past clearing prices. Table 8 shows community
cost and withholding under each structure. 6
Price observation lowers price-taking grid cost by 0.9% (USD 5.69→5.64 /day), showing the
efficiency value of information disclosure, but it raises the strategic grid cost by 8.5% (USD 6.22→
6.75/day), more than doubling the strategic premium from 9.3% to 19.7%. The welfare effect of
price transparency thus depends on whether agents exercise market power: richer signals help
competitive agents coordinate with market conditions but also enable strategic agents to exploit
6The private-information treatment in Table 8 uses an independent training run; the small difference from Table 2
reflects cross-run variation.
20

Table 8: Information design treatment (SDR, five seeds). Standard deviations in parentheses.
Strategic premium is the percentage increase in grid cost:( ¯C S − ¯C P T)/ ¯C P T.
Information Grid cost (USD/day) Strategic Withholding
structure Strategic Price-taking premiumw
Private 6.22 (0.55) 5.69 (0.66) 9 .3% 0.051 (0.025)
Price observation 6.75 (0.94) 5.64 (0.57) 19 .7% 0.038 (0.070)
their price impact more effectively. This echoes the classical IO debate on whether information
facilitates or disciplines strategic behaviour (cf. Stigler, 1964; Calvano et al., 2020). We note that
the cross-seed variance under strategic price observation is high (s.d. = 0.84), so these magnitudes
should currently be interpreted cautiously.
Experiments replicating the six-agent communityk times (k∈ {1,2,3}, single seed) suggest that
market power diminishes rapidly with community size. The strategic premium falls from 9.3% at
N= 6 to near zero at N= 12 –18, consistent with the 1/N Cournot convergence in the competition
treatment. Internal matching rates are roughly stable under replication of identical types (≈12% of
trade) implying that platforms with genuinely diverse consumption and generation profiles—where
stochastic variation across agents creates natural surpluses and deficits that partially substitute for
battery-mediated arbitrage—would likely yield higher matching rates and are a natural direction
for future work.
6. Conclusion
This paper studies market power and platform design in decentralized electricity trading. We
develop a dynamic game in which photovoltaic (PV) and battery-equipped prosumers trade on
a platform that precommits to a pricing rule, and we characterize how the interaction between
mechanism design, information design, and storage ownership shapes equilibrium outcomes.
Three findings stand out. First, strategic behaviour by battery owners generates a welfare
loss that is predominantly deadweight: under the supply-demand ratio mechanism, strategic play
raises grid cost by roughly 6%, but battery owners capture only a small fraction of passive agents’
losses. The distortion falls most heavily on passive agents who lack storage. Second, competition
among storage operators is the most effective discipline on market power. Moving from monopoly
to triopoly eliminates nearly all strategic distortion, consistent with standard Cournot conver-
gence. This suggests that policies encouraging fragmented storage ownership, such as subsidies
for residential batteries rather than community-scale installations controlled by a single operator,
can have beneficial effects beyond the direct value of storage capacity. Third, the choice of pricing
rule has first-order effects on the magnitude of distortions. A mid-market rate mechanism virtu-
ally eliminates strategic incentives by removing the price sensitivity that agents exploit, while a
linear mechanism permits individual withholding but confines the resulting transfers largely to
redistribution rather than deadweight loss. Platform operators thus have a concrete design lever
to mitigate market power.
Our results also carry a more reassuring message. The platform is overwhelmingly valuable
despite these distortions: a passive consumer saves roughly 40% on annual electricity costs relative
21

to exclusive grid settlement, and market power claws back only about 8% of that saving. The policy
question is therefore not whether to allow decentralized trading, but how to design the institutions
that govern it.
Several limitations of the current analysis point to directions for future work. First, our com-
munity comprises six agents with stylized demand and generation profiles. Scaling the analysis to
larger and more heterogeneous communities, where stochastic variation across agents creates
natural surpluses and deficits that partially substitute for battery-mediated arbitrage, would clarify
how quickly market power dissipates with community size. Preliminary results suggest rapid
convergence, but a systematic treatment with diverse agent compositions remains open. Second,
we consider three pricing mechanisms that are typical in the literature, but the design space is
much richer. Exploring mechanisms that condition on richer signals, that incorporate dynamic
elements such as intertemporal price linkages, or that allow the platform to optimise its rule
endogenously would connect this work more directly to the mechanism design literature. Third,
our model is a finite-horizon game with a fixed set of players. Extending the framework to an
infinite-horizon setting with discounting would allow the analysis of long-run dynamics, includ-
ing the possibility that patient agents sustain collusive outcomes through repeated interaction.
Whether the Cournot-style withholding we document can be amplified by tacit coordination, and
whether platform design can forestall such outcomes, are important open questions. Finally, our
computational framework treats the pricing rule as given and compares mechanisms ex post. An
ambitious extension would be to let the platform learn its own mechanism, along the lines of
recent work on differentiable mechanism design, subject to regulatory constraints such as the
tariff corridor and budget balance.
More broadly, our analysis illustrates that the industrial economics of electricity markets ex-
tends naturally to the emerging setting of prosumer trading platforms. The same forces that shape
strategic behaviour in wholesale markets, namely market concentration, information asymmetries,
and the design of price formation rules, operate at the prosumer scale. As decentralized genera-
tion and storage continue to expand, understanding these forces will be essential for designing
platforms that deliver on the promise of local energy trading.
22

References
Andrés-Cerezo, David and Natalia Fabra, “Storing Power: Market Structure Matters, ”The RAND
Journal of Economics, 2023,54(1), 3–53.
Baake, Pio, Sebastian Schwenen, and Christian von Hirschhausen, “Local Energy Markets, ”
Journal of Industrial Economics, 2023,71(3), 855–882.
Buehler , Hans, Lukas Gonon, Josef Teichmann, and Ben Wood, “Deep Hedging, ”Quantitative
Finance, 2019 ,19(8), 1271–1291.
Bushnell, James, “ A Mixed Complementarity Model of Hydrothermal Electricity Competition in
the Western United States, ”Operations Research, 2003,51(1), 80–93.
Cadre, Hélène Le, Paulin Jacquot, Cheng Wan, and Clémence Alasseur, “Peer-to-peer electric-
ity market analysis: From variational to generalized Nash equilibrium, ”European Journal of
Operational Research, 2020,282(2), 753–771.
Calvano, Emilio, Giacomo Calzolari, Vincenzo Denicolo, and Sergio Pastorello, “ Artificial intelli-
gence, algorithmic pricing, and collusion, ”American Economic Review, 2020,110(10), 3267–3297 .
Curry , Michael, Alexander Trott, Soham Phade, Yu Bai, and Stephan Zheng, “Finding General
Equilibria in Many-Agent Economic Simulations Using Deep Reinforcement Learning, ”arXiv
preprint arXiv:2201.01163, 2022.
Eschenbaum, Nicolas, Nicolas Greber , and Oleg Szehr, “Differentiable Market Clearing for Multi-
Agent Learning in Peer-to-Peer Electricity Trading, ”arXiv, 2026.
Etesami, S. Rasoul, Walid Saad, Narayan B. Mandayam, and H. Vincent Poor, “Stochastic Games
for the Smart Grid Energy Management with Prospect Prosumers, ”IEEE Transactions on Automatic
Control, 2018,63(8), 2327–2342.
Fabra, Natalia, “The Energy Transition: An Industrial Economics Perspective, ”International Journal
of Industrial Organization, 2021,79, 102734.
and Imelda, “Market Power and Price Exposure: Learning from Changes in Renewable Energy
Regulation, ”American Economic Journal: Economic Policy, 2023,15(4), 323–358.
Garcia, Alfredo, James D. Reitzes, and Ennio Stacchetti, “Strategic Pricing When Electricity Is
Storable, ”Journal of Regulatory Economics, 2001,20(3), 223–247 .
He, Li, Yuanzhi Liu, and Jie Zhang, “Peer-to-peer energy sharing with battery storage: Energy
pawn in the smart grid, ”Applied Energy, 2021,297, 117129 .
Hortaçsu, Ali and Steven L. Puller, “Understanding Strategic Bidding in Multi-Unit Auctions: A
Case Study of the Texas Electricity Spot Market, ”The RAND Journal of Economics, 2008,39(1),
86–114.
Hoseinpour , Milad and Mahmoud-Reza Haghifam, “Prosumers’ cost recovery in peer-to-peer
electricity markets, ”Electric Power Systems Research, 2024,226, 109934.
23

IRENA, “Innovation Landscape Brief: Peer-to-Peer Electricity Trading, ” Technical Report, Interna-
tional Renewable Energy Agency, Abu Dhabi 2020.
Kastius, Alexander and Rainer Schlosser, “Dynamic pricing under competition using reinforce-
ment learning, ”Journal of Revenue and Pricing Management, 2022,21(1), 50–63.
Liu, Nian, Xinghuo Yu, Cheng Wang, Chaojie Li, Li Ma, and Jinyong Lei, “Energy-sharing model
with price-based demand response for microgrids of peer-to-peer prosumers, ”IEEE Transactions
on Power Systems, 2017 ,32(5), 3569–3583.
Long, Chao, Jianzhong Wu, Chenghua Zhang, Lee Thomas, Meng Cheng, and Nick Jenkins,
“Peer-to-peer energy trading in a community microgrid, ” in “2017 IEEE power & energy society
general meeting” IEEE 2017 , pp. 1–5.
Mengelkamp, Esther , Johannes Gärttner , Kerstin Rock, Scott Kessler , Lawrence Orsini, and
Christof Weinhardt, “Designing Microgrid Energy Markets: A Case Study: The Brooklyn Micro-
grid, ”Applied Energy, 2018,210, 870–880.
Morstyn, Thomas, Niall Farrell, Sarah J. Darby , and Malcolm D. McCulloch, “Using Peer-to-Peer
Energy-Trading Platforms to Incentivize Prosumers to Form Federated Power Plants, ”Nature
Energy, 2018,3(2), 94–101.
Myerson, Roger B. and Philip J. Reny, “Perfect Conditionalε-Equilibria of Multi-Stage Games with
Infinite Sets of Signals and Actions, ”Econometrica, 2020,88(2), 495–531.
Parag, Yael and Benjamin K. Sovacool, “Electricity Market Design for the Prosumer Era, ”Nature
Energy, 2016,1(4), 16032.
Schill, Wolf-Peter and Claudia Kemfert, “Modeling Strategic Electricity Storage: The Case of
Pumped Hydro Storage in Germany, ”The Energy Journal, 2011,32(3), 59–87 .
Sioshansi, Ramteen, “When Energy Storage Reduces Social Welfare, ”Energy Economics, 2014,41,
106–116.
Stigler , George J., “ A Theory of Oligopoly, ”Journal of Political Economy, 1964,72(1), 44–61.
Tushar , Wayes, Tapan Kumar Saha, Chau Yuen, David Smith, and H Vincent Poor, “Peer-to-
peer trading in electricity networks: An overview, ”IEEE transactions on smart grid, 2020,11(4),
3185–3200.
Williams, Olayinka and Richard Green, “Electricity storage and market power, ”Energy Policy,
2022,164, 112872.
Wolfram, Catherine D., “Measuring Duopoly Power in the British Electricity Spot Market, ”American
Economic Review, 1999 ,89(4), 805–826.
Zhang, Yizhou, Chenghong Gu, Xiangning Yan, and Furong Li, “Cournot Oligopoly Game-Based
Local Energy Trading Considering Renewable Energy Uncertainty Costs, ”Renewable Energy,
2020,159, 1117–1127 .
24

Zheng, Stephan, Alexander Trott, Sunil Srinivasa, David C. Parkes, and Richard Socher, “The
AI Economist: Taxation policy design via two-level deep multiagent reinforcement learning, ”
Science Advances, 2022,8(18), eabk2607 .
25

A. Proofs
A.1. Proof of Proposition 1
Proof. We verify that the required conditions R.1–R.5 of Myerson & Reny (2020, Definition 9 .1) are
met. For this verification, we use an equivalent representation of the battery feasibility constraint
that keeps each player’s available action set independent of her signal (as required by R.1), while
leaving the set of implemented battery flows (and thus the economic outcomes) unchanged.
Formally, at each date t∈ {1, . . . , T}, let player i choose an intended action bit ∈[b i, ¯bi]
(independent of Sit). Given the current state of charge Sit, define the implemented battery flow as
the Euclidean projection onto the feasible interval,
˜bit := Π Bi(Sit)(bit)∈B i(Sit),so thatS i,t+1 =S it + ˜bit.
Imports/exports and payments are computed exactly as in Section 2.1 but using the implemented
flow ˜bit in place of bit (so ˜xit = ˜bit −ℓ t i(θi), ˜mit = ˜x+ it, ˜qit = ˜x− it, and ˜cit =p c( ˜Mt, ˜Qt) ˜mit −
pp( ˜Mt, ˜Qt)˜qit). Because the projection satisfies ΠBi(Sit)(bit) =b it whenever bit ∈B i(Sit), and
because any bit /∈Bi(Sit) induces the same implemented flow and next state as the boundary
action ˜bit ∈B i(Sit), this reformulation does not change the set of attainable outcome paths under
optimal play; it only embeds the feasibility constraint into the state transition. We can now verify
the conditions R.1–R.5 for this equivalent representation in turn.
Condition R.1.The game has T+ 1 dates: at date 0, nature draws the type profile θ∼π ; at
dates t= 1, . . . , T, each player i simultaneously chooses bit ∈[b i, ¯bi]. Thus, taking J={1} in
Myerson–Reny’s notation, we may set Ait = [bi, ¯bi] for all signals sit, so Φit(sit) =A it for every sit
as required by R.1. Nature has no moves att≥1(soA 0t is a singleton fort≥1).
Condition R.2.Player i’s signal at t= 1 is si1 =θ i, a coordinate of nature’s date- 0 move. For
t≥2, define
sit = (θi, bi1, . . . , bi,t−1),
which is a literal projection of nature’s date-0 coordinate and of player i’s own past action coordi-
nates. In particular, Sit is not itself a coordinate in the outcome history; it is computed from the
signal via the recursionS i1 = 0andS i,τ+1 =S iτ + ΠBi(Siτ )(biτ )forτ < t.
Conditions R.3–R.4.Each Ait = [b i, ¯bi] is a nonempty compact metric space and each Θi is
finite (hence compact). Player i’s total payoff is PT t=1 uit with uit =−˜cit, where ˜cit is a continuous
function of (θ,(b jt)j∈I , St) because: (i) projection onto an interval is continuous, (ii) the induced
quantities ( ˜mit,˜qit) are continuous in ˜bit, and (iii) pc and pp are continuous on the attainable set K
by Assumption 1. Thusu i is continuous in all actions and types, satisfying R.4.
Condition R.5.Nature moves only at date 0, drawing θ from π on the finite set Θ. Finite-type
priors satisfy the regularity requirement R.5 under the discrete topology: the Radon–Nikodym
derivative is trivially continuous and its strict-positivity set is closed. At dates t≥1 , nature’s move
set is a singleton.
Since all conditions R.1–R.5 are satisfied, Theorem 9 .3 of Myerson & Reny (2020) applies,
and therefore for every ε >0 the private-information game possesses a perfect conditional
ε-equilibrium.
26

In addition, we can also show that this result holds if, instead of excluding payments from
signals, player i observes her own period-t bill. Then the above projected-signal verification can be
maintained by adding a (purely formal) reporting stage: after players choose (bjt)j∈I at each date t,
an additional player 0 chooses a report vector ˆct = (ˆcit)i∈I in a compact interval C:= Q i∈I [−¯c,¯c],
where ¯c <∞bounds all attainable bills (the existence of such a bound follows directly from
bounded flows, finite Θ, and Assumption 1). Prosumers’ period payoffs are uit =−ˆcit, and player
0’s payoff is
u0t :=−
X
i∈I

ˆcit −˜cit
2
,
so player 0 (approximately) reports the computed bill ˜cit. Define prosumer i’s signal to include her
own past reports (ˆci1, . . . ,ˆci,t−1) in addition to (θi, bi1, . . . , bi,t−1). Because ˆcit is then a coordinate
of player 0’s action history, the signal remains a literal projection and Conditions R.1–R.5 continue
to hold (with player 0 added). Hence Theorem 9 .3 yields existence of a perfect conditional ε-
equilibrium for everyε >0also in the variant with observed own bills.
A.2. Proof of Proposition 2
Proof. We prove the statements in turn.Part (i). Fix a period t, a public state (θ, St), and continuous
continuation values {Wi,t+1(θ,·)} i∈I . Each player’s action set Bi(Sit) is a nonempty compact
convex interval, and playeri’s payoff
uit(bit, b−i,t;θ, St) +W i,t+1(θ, St +b t)
is continuous in all actions (Assumption 1 and continuity ofW i,t+1).
Now suppose Wi,t+1(θ,·) is concave in Si,t+1 for each i. Fix b−i,t. We show player i’s payoff is
concave in bit. First, on the export side ( bit < ℓt i(θi)), let q=ℓ t i(θi)−b it >0 . Then the stage payoff
term equals q pp(M−i,t, Q−i,t +q) , which is concave in q by Assumption 2(ii), hence concave in
bit. Second, on the import side ( bit > ℓt i(θi)), let m=b it −ℓ t i(θi)>0 . Then the stage payoff term
equals −m pc(M−i,t +m, Q−i,t), which is concave in m by Assumption 2(i), hence concave in bit.
Third, at the kink bit =ℓ t i(θi), the left derivative with respect to bit is −pp(Mt, Qt) and the right
derivative is −pc(Mt, Qt); since pp ≤p c (Assumption 1), the left derivative weakly exceeds the right
derivative, so the stage payoff is globally concave in bit. Finally, since Si,t+1 =S it +b it is affine,
concavity of Wi,t+1(θ,·) in Si,t+1 implies bit 7→W i,t+1(θ, St +b t) is concave. Hence player i’s total
payoff is concave inb it.
Therefore, for each i, the best-response correspondence BRi(·) is nonempty and compact-
valued, and by concavity of the objective over a convex domain it is convex-valued (a weakly concave
function on an interval has a convex argmax set). By Berge’s maximum theorem, Q i∈I BRi(·)
is upper hemicontinuous. Hence the product correspondence Q i∈I BRi(·) satisfies Kakutani’s
conditions, and the period-t continuation game admits a pure-strategy Nash equilibrium. Moreover,
the one-shot game is the special caseW i,t+1 ≡0, so a pure-strategy Nash equilibrium exists.
To complete the backward-induction argument for the dynamic game (with a continuum of
states), we select equilibria measurably at each date. Fixt and continuation values {Wi,t+1(θ,·)} i∈I .
27

Let the public-state space be
Ω := Θ×
Y
j∈I
[0, ¯Sj],
and let the action-product space be A:= Q j∈I [bj, ¯bj]. For each (θ, S)∈Ω , write B(θ, S) :=Q
j∈I Bj(Sj)⊂A , and define the set of pure Nash equilibria of the period- t continuation game by
the correspondenceE t : Ω⇒A,
Et(θ, S) :=
n
b∈B(θ, S) :b i ∈BR i(θ, S, b−i)∀i∈I
o
.
We can then show thatEt admits a Borel measurable selection. Consider that we already showed
Et(θ, S)̸=∅ for all (θ, S)by Kakutani; compactness then follows because Et(θ, S)⊂B(θ, S)and
B(θ, S)is compact.
Now we proceed to show that Gr(Et) :={((θ, S), b) :b∈ Et(θ, S)}is closed. Take any sequence
{((θn, Sn), bn)}n≥1 ⊂Gr(E t) with ((θn, Sn), bn)→((θ, S), b)in Ω×A . First, feasibility: for each i,
Bi(Si) = [max{bi,−S i},min{ ¯bi, ¯Si −S i}] has endpoints continuous in Si, hence (θ, S)7→B(θ, S)
has closed graph, implying b∈B(θ, S) . Second, best-response optimality: by Berge’s maximum
theorem (continuity of the objective and compact feasible sets), eachBRi has closed graph. Because
bn i ∈BR i(θn, Sn, bn −i) and (θn, Sn, bn −i, bn i )→(θ, S, b−i, bi), we obtain bi ∈BR i(θ, S, b−i) for every
i. Henceb∈ Et(θ, S), provingGr(Et)is closed.
Then it follows that since Ω is a standard Borel space (finite Θ times a compact metric product)
and A is a compact metric space, a nonempty closed-valued correspondence with closed graph
admits a Borel measurable selection (Kuratowski–Ryll-Nardzewski).
We can then proceed by backward induction using such measurable selections. At t=T ,
Wi,T+1 ≡0 , so the period- T game has a nonempty equilibrium correspondence ET and we select
a Borel measurable b∗ T (θ, ST )∈ ET (θ, ST ). Define the (degenerate) Markov strategy β∗ iT (· |θ, ST )
that assigns probability1tob ∗ iT (θ, ST ), and define the induced valueW ∗ iT (θ, ST )accordingly.
Now fix t < Tand assume measurable {b∗ τ }T τ=t+1 (equivalently {β∗ τ }) and values {W ∗ i,t+1}i∈I
have been constructed. Applying the argument above to the period- t continuation game with
continuation W ∗ i,t+1 yields a nonempty equilibrium correspondence Et, and we select a Borel
measurableb ∗ t (θ, St)∈ Et(θ, St). Letβ ∗ t be the associated degenerate Markov strategy profile and
define W ∗ it(θ, St) by the recursive equation in the main text. Iterating for t=T, T−1, . . . ,1yields
a pure-strategy Markov perfect equilibrium (MPE).
Finally, note that equilibrium existence in the dynamic observable-types game does not require
the concavity condition above. By the same argument as in Proposition 1 (Myerson & Reny, 2020,
Theorem 9 .3), for everyε >0 the observable-types dynamic game admits a perfect conditional
ε-equilibrium. Formally, one may use the same intended-action/projection representation as in
Proposition 1 to make players’ available action sets independent of signals (Condition R.1), and
add a purely formal public reporting stage after each action profile that announces the public
state (and, if included, realized payments) as an explicit coordinate of the outcome history so that
signals are literal projections (Condition R.2). The regularity conditions R.1–R.5 then continue
to hold. The concavity condition is therefore used only to guarantee existence of a pure-strategy
MPE.
28

Part (ii).Fix a period t, state (θ, St), and the associated one-shot game ( Wi,t+1 ≡0 ). Fix player i
and opponents’ actionsb −i,t, and write
q:=ℓ t i(θi)−b it >0
on the export branch, so thatM t =M −i,t andQ t =Q −i,t +q.
The strategic marginal payoff from increasing exports is
D∗(q) =p p(Mt, Qt) +q ∂Qpp(Mt, Qt).
At an interior strategic export solutionq ∗ it, we haveD ∗(q∗ it) = 0, hence
pp(Mt, Qt)

q=q ∗ it =−q ∗ it ∂Qpp(Mt, Qt)

 q=q ∗ it ≥0,
with strict inequality whenever ∂Qpp <0 at the relevant arguments. By the definition of the
price-taking benchmark, the price-taking marginal payoff on the export branch is
DP T(q) =p p(Mt, Qt),
which is weakly decreasing in q by Assumption 2(ii). Since DP T(q∗ it)≥0 , every price-taking
optimizer satisfies
qP T it ≥q ∗ it,
with strict inequality if∂ Qpp <0at the relevant arguments.
For the social planner comparison, holding b−i,t fixed, the one-shot planner chooses bit to
maximize −Ct(Yt). On the export branch, increasing q lowers Yt one-for-one, so the planner’s
marginal payoff is
C ′ t(Yt)∈[P E, PI ]⊆R +.
Hence the planner chooses the maximal feasible export on the export branch. The same is true
for the price-taking benchmark, since its marginal payoff is
DP T(q) =p p(Mt, Qt)≥P E ≥0
by Assumption 1. Therefore (up to tie-breaking),
qP T it =q SP it .
Combining the two comparisons yields
q∗ it ≤q P T it =q SP it ,
with strict inequality in the first comparison under the stated strictness condition.
Part (iii).Fix t < T, player i, state (θ, St), and a continuation path (b−i,τ )T τ=t . Let W ∗ i,τ and W P T i,τ
denote the continuation values induced by the strategic and price-taking problems against this
29

fixed path, and define the marginal continuation values
λk i,τ (s) :=∂ sW k i,τ (s), k∈ {∗, P T},
on the relevant continuation-state interval. Assume that the marginal unit of storage at any future
date τ≥t+ 1 is either carried forward or exported. Hence, for each τ and relevant s, the shadow
value satisfies
λk i,τ (s) = max{ρk i,τ (s), λk i,τ+1 (s)}, λ k i,T+1 ≡0,
where ρk i,τ (s) is the marginal payoff from exporting the marginal unit at date τ . By the definition
of the price-taking benchmark, on the export branch
ρ∗ i,τ (s)≤ρ P T i,τ (s)
because∂ Qpp ≤0(Assumption 2(ii)). Backward induction onτthen yields
λ∗ i,t+1(s)≤λ P T i,t+1(s)
on the relevant interval.
Now consider period t on the import branch and write s=S it +b it. The strategic and price-
taking marginal payoffs from increasingb it are
D∗(bit) =−p c(Mt, Qt)−m it(bit)∂ M pc(Mt, Qt) +λ ∗ i,t+1(s),
DP T(bit) =−p c(Mt, Qt) +λ P T i,t+1(s).
Therefore,
DP T(bit)−D ∗(bit) =m it(bit)∂ M pc(Mt, Qt) +  λP T i,t+1(s)−λ ∗ i,t+1(s)  ≥0,
sincem it(bit)>0on the import branch,∂ M pc ≥0(Assumption 2(i)), andλ P T i,t+1 ≥λ ∗ i,t+1.
By concavity of the period-t objectives, D∗ and DP Tare decreasing and the interior optimizers
satisfy
D∗(b∗ it) = 0, D P T(bP T it ) = 0.
Hence
DP T(b∗ it)≥D ∗(b∗ it) = 0,
implying
b∗ it ≤b P T it .
Part (iv).Let
∆ :=
X
i

bSP,t it −b P T it  >0.
By assumption, this additional period-t charge is fully discharged through future exports. Therefore
30

the cumulative future export difference is strictly positive:
TX
τ=t+1

QSP,t τ −Q P T τ  >0.
Hence not all summands can be weakly negative, and there exists someτ > tsuch that
QSP,t τ > QP T τ .
B. Computational details
This appendix provides full details of the neural-network architectures, training procedure, and
experimental configurations used in Section 5.
B.1. Architecture
Each controllable agent i is assigned an independent feedforward neural network f ϕi with the
architecture shown in Table 9. The network maps the agent’s observation vector to a scalar battery
action ait ∈[−1,1] , which is scaled to the feasible battery flow bit =a it · ¯bi and clamped to the
capacity-feasible set Bi(Sit). PV curtailment is disabled (all available PV is used). All weights are
initialised with orthogonal initialisation (gain0.5) and biases are set to zero.
Table 9: Decentralised policy network architecture (per agent).
Layer Specification Output size
Input Observation vectorn in ∈ {5,9}
Hidden 1 Linear(n in, 32) + ReLU 32
Hidden 2 Linear(32, 32) + ReLU 32
Output Linear(32, 1) + Tanh 1
The observation vector depends on the information-structure treatment. Underprivateinformation
(nin = 5), the agent observes her normalised battery state Sit/ ¯Si, the time of day t/T , normalised
demand, normalised PV generation, and the normalised midpoint price (pp +p c)/(2P I ). Under
price-observableinformation ( nin = 9), the agent additionally observes the normalised sell price,
buy price, bid–ask spread, average total demand, and average total supply. When endogenous
tatonnement is active, the price features are derived from the current tatonnement price estimate
ˆp(k) t rather than from lagged prices.
The social planner uses a single centralised network that observes the full state and outputs
joint actions for all agents. The architecture mirrors the decentralised network but with input size
1 + 3N (time of day, plus normalised battery state, demand, and PV for each of the N agents) and
output size N (one action per agent; passive agents’ outputs have no effect). The hidden-layer width
is 16N , so the network capacity scales with the number of agents. Standard PyTorch initialisation
is used (no orthogonal).
31

B.2. Training procedure
At each period t, agents’ actions and market prices are determined jointly through an endogenous
tatonnement procedure. Starting from an initial price estimate ˆp(0) t (the previous period’s realised
price, or the tariff midpoint at t= 1 ), the procedure iterates: (i) each agent computes her best-
response action b(k) it given ˆp(k) t ; (ii) the implied aggregate quantities (M (k) t , Q(k) t ) and new prices
p(k) t are computed; (iii) the price estimate is updated with damping, ˆp(k+1) t =α p(k) t + (1−α) ˆp(k) t .
The iteration terminates after at most NK steps or when the price change falls below the tolerance.
In strategic mode, no gradients are detached during the iteration: the entire fixed-point chain
carries gradients, so agents’ policy updates account for the equilibrium relationship between
their actions and the resulting prices. In price-taking mode, the iterations are performed without
gradients and only the final forward pass carries gradients through each agent’s own net import to
her cost.
Table 10 lists all training hyperparameters, used consistently across all treatments unless
otherwise noted.
Table 10: Training hyperparameters.
Parameter Symbol Value
Training episodes 350
Mini-batches per episode 5
Mini-batch sizeN B 32
Training days 1,000
Test days 100
Optimiser Adam
Learning rateη5×10 −3
Gradient clipping max norm1.0
Initial noise scaleσ 0 0.5
Noise type Additive Gaussian
Noise decay Linear:σ 0(1−e/300)
Tatonnement iterationsK6
Tatonnement dampingα0.7
Tatonnement tolerance10 −5
Tatonnement mode (strategic) Endogenous (full gradient)
Tatonnement mode (price-taking) Detached (no gradient)
Regret episodes 350
Random seeds{42,43,44,45,46}
For the decentralised networks, exploration noise is additive Gaussian: at each period, the
network’s output action is perturbed as ait ←clamp(a it +ε,−1,1) with ε∼ N(0, σ2 e ) and σe =σ 0 ·
max(1−e/300,0) . Noise is applied only on the final tatonnement iteration to avoid contaminating
the price-discovery process. For the centralised planner, exploration uses random replacement:
each action is replaced with a uniform draw from [−1,1] with probability σe =σ 0 ·0.9 e, decaying
exponentially.
In strategic mode, per-agent gradients are computed via torch.autograd.grad( ¯C i, ϕi) for
each controllable agent i, isolating the gradient ∇ϕi ¯C i from cross-agent terms so that each agent’s
32

update reflects her own best response (see Section 4.1). In price-taking mode, aggregate quan-
tities are detached from the computation graph before price calculation, making sequential
backward() calls safe and equivalent. In both modes, gradients are clipped to unit norm before
the optimiser step. During training, initial battery states are drawn uniformly from [0, ¯Si] in every
episode; during evaluation, all batteries are initialised at Si1 = 0 to match the model specification.
B.3. Experimental configurations
Table 11 summarises the three treatments. Each treatment trains all relevant benchmarks over
five seeds. Abbreviations: SP = social planner, PT = price-taking, S = strategic (Nash).
Table 11: Summary of experimental treatments.
Section Treatment Community Mechanism Info Benchmarks
5.1 Baseline ordering Standard (A–F) SDR Private SP , PT, S
5.2 CompetitionN×C + D + E SDR Private PT, S
5.3 Heterogeneity & mechanisms Standard (A–F) SDR, MMR, LIN Private PT, S
In the competition treatment, the number of symmetric storage agents varies over N∈ {1,2,3}.
Total battery capacity is fixed at 10 kWh and divided equally, so each agent receives ¯S= 10/N kWh
with charge/discharge rate ¯b= 10/(3N) kW; two passive agents (types D and E) provide back-
ground demand and supply. In the information-design treatment, the two information structures
differ only in the policy network’s input vector (5 vs. 9 features, as described above); all other
hyperparameters are identical. In the scaling treatment, the standard six-agent community is
replicated k∈ {1,2,3} times, yielding communities of 6, 12, and 18 agents (3k controllable). The
decentralised hidden-layer width remains at 32 for all agents; the centralised hidden-layer width
scales as16×6k(the total number of agents).
B.4. Stochastic data generation
Each agent’s PV generation is st i = ¯si ·sin  π(t−6)/(18−6)  1[6,18](t), perturbed by a mean-
reverting AR(1) scaling process zPV t =µ+φ(z t−1 −µ) +ε t with φ= 0.85 , σε = 0.20, and daily
mean µ∼U(0.6,0.95) . Additionally,1–4 Gaussian cloud-dip transients (depth20–70%, width 1–2 h)
are superimposed. The scaling factor is clipped to [0.02,1.0] and drawn per day (shared across
agents, with agent-specific¯si).
Demand follows a composite time-of-use profile (morning ramp 5–8h, low midday 9–17h,
evening peak 17–22h), perturbed by an AR(1) process ( φd = 0.6 , σd = 0.25 ) with 1–3 random
activity pulses per day. Daily total demand is scaled by a log-normal factor ( σ= 0.2 ). Average daily
demand varies by agent type (Table 1).
B.5. Convergence
Figure 7 shows training convergence for the baseline community (SDR, private information). Both
the strategic and price-taking learners converge smoothly within approximately 100 episodes.
The strategic cost lies persistently above the price-taking cost throughout training, reflecting the
prisoners’ dilemma: even during learning, gradient-based optimisers that internalise the price
33

impact converge to a costlier equilibrium than those that ignore it. The gap between the two curves
stabilises early and remains essentially constant after convergence, indicating that the welfare
loss from market power is a robust equilibrium property rather than a transient artefact of the
training process.
0 50 100 150 200 250 300 350
Episode
0.00
0.05
0.10
0.15
0.20
0.25Avg daily cost (USD)
Planner
Price-Taking
Strategic
Figure 7: Training convergence (SDR, private information). Average daily grid cost per episode
for strategic and price-taking learning. The strategic cost converges to a persistently higher level,
reflecting the cost of internalising price impact.
C. Verification of Assumption 2 and concave continuation values
This appendix verifies, for each price mechanism, (a) whether Assumption 2 holds and (b) the
concavity condition on equilibrium continuation values required by Proposition 2(i) for pure-
strategy MPE existence. Recall from the proof of Proposition 2(i) that we require each player’s
total period-t objective—the sum of the stage payoff and the continuation value—to be concave
in her own battery action bit. On the export branch ( q >0), this requires concavity of the export-
revenue function q pp(M, Q−i +q) in q; on the import branch ( m >0 ), this requires convexity
of the import-cost function m pc(M−i +m, Q)in m; and across both branches, the continuation
valueW i,t+1(θ,·)must be concave inS i,t+1.
Throughout this appendix, write M=M −i +m for total imports and Q=Q −i +q for total
exports when player i’s quantity varies. For all mechanisms, P E = 0.05, P I = 0.30, and pmid =
(P E +P I )/2 = 0.175. We use the general identity
d2
dm2

m pc(M−i +m, Q)

= 2 ∂pc
∂M (M, Q) +m ∂2pc ∂M 2 (M, Q),(1)
and the analogous expression ford 2[q pp]/dq2 withQ=Q −i +q.
C.1. Linear mechanism
The linear mechanism admits a fully analytical verification. In theM≥Q regime (demand exceeds
supply),p p =p mid +κ(M−Q)and the revenue is
R(q) =q

pmid +κM−κQ −i −κq

,
34

so d2R/dq2 =−2κ <0 for all parameter values. In the M < Qregime, pp =P E −κM+M D κ/Q
whereD κ = (P I −P E)/2 +κM >0, and applying (1) yields
d2R
dq2 =− 2M Dκ Q−i Q3 <0wheneverQ −i >0.
At the regime boundary Q=M , the slope dR/dq drops discontinuously (from pmid −κ(Q −i −
M) +κM to a lower value), so the kink preserves global concavity. When Q−i = 0, d2R/dq2 = 0 in
the M < Qregime (linear). Hence R(q) is globally weakly concave, and strictly concave whenever
Q−i >0orM≥Q.
In the M < Qregime, pc =p mid −κQ+κ(M −i +m) is affine in m, so C(m) =m pc is quadratic
with d2C/dm2 = 2κ >0 for all parameter values. In the M≥Q regime, pc =P I +κQ+AQ/M
whereA=p mid −κQ−P I <0, and (1) yields
d2C
dm2 = −2AQ M−i M 3 >0wheneverM −i >0,
since A <0 . At the regime boundary M=Q , the slope dC/dm jumps upward (from pmid to
pmid +m(P I −p mid)/Q > pmid), preserving global convexity. When M−i = 0, d2C/dm2 = 0 in the
M≥Q regime. Hence C(m) is globally weakly convex, and strictly convex whenever M−i >0 or
M < Q.
Within each smooth regime, the curvature conditions hold. The stage payoff is concave in bit
on both the export and import branches (strictly so whenever Q−i >0 or M−i >0 , respectively).
Since the within-day stage payoff is quadratic on each branch, the sum of a (weakly) concave stage
payoff and a concave continuation value is concave, so the Kakutani argument in the proof of
Proposition 2(i) applies. However, the analysis above applies only within each smooth pricing
regime. The linear mechanism clamps the clearing price pLIN to the corridor [P E, PI ]. When the
clearing price hits the upper boundP I (at M−Q= (P I −p mid)/κ), the consumer price pc becomes
constant at P I for larger M , and the import-cost slope dC/dm drops from a value above P I to
exactly P I . This creates a concave kink that breaks global convexity of the import-cost function.
Symmetrically, when the clearing price hits P E, a convex kink in the export-revenue function
breaks global concavity.
Within each smooth regime (between the kinks at M=Q and at the clamping boundaries),
the curvature conditions hold as derived above. The regime-boundary kink at M=Q preserves
convexity/concavity (as shown), but the clamping kinks do not.
C.2. MMR mechanism
In the M≥Q regime, pp =p mid is constant, so R(q) =q p mid is linear ( d2R/dq2 = 0 ). In the
M < Qregime,pp =P E +M(p mid −P E)/Q, and (1) yields
d2R
dq2 =− 2M Q−i (pmid −P E) Q3 <0wheneverQ −i >0.
At the regime boundary Q=M , the slope drops from pmid (left) to pmid −q(p mid −P E)/M < pmid
(right), preserving global concavity. Hence R(q) is globally weakly concave, strictly concave in the
35

M < Qregime wheneverQ−i >0.
In the M < Qregime (supply exceeds demand), pc =p mid is constant, so C(m) =m pmid is
linear (d2C/dm2 = 0). In theM≥Qregime,p c =P I −Q(P I −p mid)/M, and (1) yields
d2C
dm2 = 2Q M−i (P I −p mid) M 3 >0wheneverM −i >0.
At the regime boundary M=Q , the slope jumps from pmid (left) to pmid +m(P I −p mid)/Q > pmid
(right), preserving global convexity. Hence C(m) is globally weakly convex, strictly convex in the
M≥Qregime wheneverM −i >0.
Conclusion for the MMR mechanism..Assumption 2 holds globally with weak curvature. In the
regime where a player has price impact (the “long side”), the curvature is strict. In the constant-
price regime (the “short side”), the cost or revenue is linear; however, the continuation valueWi,t+1
provides the concavity needed for a unique best response in the dynamic game.
C.3. SDR mechanism
In the Q≤M regime ( ρ≤1 ), pp =P EP I M/D where D= (P I −P E)Q+P EM . A direct
computation yields
d2R
dq2 =− 2K 1 (P I −P E) D3 , K 1 =P EP I M  (P I −P E)Q−i +P EM  >0.
Since P I > PE and D >0 , we have d2R/dq2 <0 for all attainable (M, Q)with Q≤M . In the
Q > Mregime (ρ >1), pp =P E and R(q) =q PE is linear. In the Q > Mregime (ρ >1), pp =P E
and R(q) =q PE is linear with slope P E. At the boundary Q=M , the left-hand slope (from the
ρ≤1regime) equals
P E + (M−Q −i) P E(P E −P I ) P I M < PE,
because ∂Qpp <0 pulls the marginal revenue below the price. The slope thereforeincreasesat
the boundary, creating a convex kink. Consequently, the export-revenue function isnotglobally
concave: it is strictly concave within the ρ≤1 regime and linear in the ρ >1 regime, but the kink
atQ=Mviolates global concavity.
In the Q > Mregime (ρ >1), pc =P E and C(m) =m PE is linear. In the Q≤M regime, pc is
the sum of two terms with competing curvature:
pc(M, Q) = P EP I Q D| {z }
convex inM
+P I

1− Q M  | {z }
concave inM
,
whereD= (P I −P E)Q+P EM. Applying (1),
d2C
dm2 = 2
 P I Q
M 2 − (P E)2P I Q D2  +m  2(P E)3P I Q D3 − 2P I Q M 3  .
For moderatem (i.e.ρ bounded away from zero), the first bracketed term dominates andd2C/dm2 >
36

0. However, as m→ ∞with Q and M−i fixed, D≈P EM and both terms in the second bracket
converge to 2P I Q/M3 with opposite signs, while the first bracket converges to zero. Numerically,
d2C/dm2 changes sign from positive to negative at a threshold that depends on the ratio m/Q.
For example, with M−i = 1 and Q= 3 , the sign change occurs at m≈8.9 (i.e. ρ≈0.30 ); with
M−i = 0.5andQ= 0.5, it occurs atm≈2.6(ρ≈0.16).
As ρ→0 , pc →P I and the cost functionC(m) =m pc approaches m PI (linear). The hyperbolic
structure of the SDR formula causes C(m) to approach this linear asymptote from above, creating
a region of slight concavity. This means Assumption 2(i)failsfor the SDR mechanism at extreme
quantity ratios, even in its weak (non-strict) form.
On the import branch at period T (where Wi,T+1 ≡0 ), the stage payoff −C(m) is not globally
concave in m, so the standard one-shot Kakutani argument does not apply directly. Two observa-
tions mitigate this. First, Proposition 1 guarantees existence of a perfect conditional ε-equilibrium
for every ε >0 via the Myerson and Reny (2020) argument, which requires no curvature assump-
tions. Second, for the dynamic game ( t < T), the total objective includes the continuation value,
which is concave in Si,t+1 and hence in bit; this additional concavity can dominate the slight
non-convexity of the stage cost in the region where the violation occurs. We verify this numerically
below.
C.4. Verification of concave equilibrium continuation values
We additionally numerically verifies, for each price schedule mechanism considered in the paper,
the concavity-propagation condition required by Proposition 2 namely that the equilibrium value
function W ∗ it(θ, St) inherits concavity in Sit from a concave continuation W ∗ i,t+1(θ, St+1). We
first explain the approach and then report the results of the individual calculations for each
mechanism. Note that for the linear pricing mechanism, the result can be derived analytically and
the verification focuses on SDR and MMR.
C.5. Numerical verification approach
For each mechanism, the numerical verification proceeds by backward induction on a finite grid
for the public battery state. Fix a type profile θ and hence the induced period surpluses ℓt i(θi).
In each period t, we discretize (Sit, S−i,t) on a uniform grid over the feasible state space and,
at each grid point, solve the one-period continuation game in battery flows (bit, b−i,t) given the
continuation value from period t+ 1 . This yields equilibrium actions and the induced equilibrium
value W ∗ it(θ, St) on the state grid. We then test concavity in the own battery state Sit by computing
discrete second differences of the grid values while holding S−i,t fixed (slice-by-slice), and repeat
this recursively from t=T back to t= 1 . Thus, the verification checks directly whether concavity
is preserved by the equilibrium Bellman operator for the mechanism under consideration.
To make the verification feasible on finer grids, we use analytical derivatives of the pricing
mechanisms to solve the repeated best-response optimization at each state grid point. In particular,
for each mechanism we calculate ∂M pc(M, Q)and ∂Qpp(M, Q)(and the corresponding second
derivatives on smooth branches), which yield analytical derivatives of the stage payoff in the
importer and exporter cases. Combined with the derivative of the continuation termW ∗ i,t+1(θ, St+1)
37

with respect to bit, this converts the best-response problem on each smooth segment into a root-
finding problem for the first-order condition. The solver partitions the feasible interval at all
relevant kinks—(i) the trade-regime kink at bit =ℓ t i(θi), (ii) mechanism-specific pricing kinks such
as the SDR/MMR branch boundaries, and (iii) continuation interpolation kinks—and applies a
root solver on each smooth subinterval. If needed, we additionally fall back to a bounded scalar
minimization routine. The use of the derivatives of the price mechanisms reduces computation
time substantially, but note that the concavity check itself is performed on the computed grid
values.
We report multiple verifications for each mechanism. These vary in particular by the horizon
lengthT, the state-grid sizen grid, and the surplus path(ℓ t i, ℓt −i)T t=1.7 We simplify the surplus path
variation by distinguishing three types: whether players’ realizations are symmetric, asymmetric,
or a mix across periods. For each run, we report as “Result” whether the concavity test passes
for the entire run (all periods, both players, and all own-state slices) at the specified numerical
tolerance. “Worst ∆2” reports the largest discrete second difference observed in the concavity
checks across all reported slices and periods; positive values indicate local convexity on the grid,
while very small positive values (near the tolerance) are typically numerical error rather than
economically meaningful violations. Finally, “Time (s)” is the wall-clock runtime of the scenario.
Table 12: Initial numerical concavity-verification runs for SDR and MMR
Mechanism TypeT n grid Interp. Result Worst∆ 2 Time (s)
SDR Sym 2 25 linear PASS 1.03e-09 27 .3
SDR Sym 2 50 linear PASS 2.12e-09 212.8
SDR Asym 2 25 linear PASS 2.09e-09 552.7
SDR Mix 2 25 linear PASS 1.95e-09 522.0
SDR Sym 4 25 linear PENDING – –
SDR Asym 4 25 linear PENDING – –
SDR Mix 4 25 linear PENDING – –
MMR Sym 2 25 linear PENDING – –
MMR Sym 2 50 linear PENDING – –
MMR Asym 2 25 linear PENDING – –
MMR Mix 2 25 linear PENDING – –
Notes:“Type” denotes the surplus-path structure (Sym = symmetric, Asym = asymmetric, Mix = mixed across periods).
T is the horizon length and ngrid is the number of grid points per state dimension. “Result” reports whether the
discrete concavity test passes for the full run. “Worst ∆2” is the largest discrete second difference observed across
all slices and periods; positive values indicate local convexity on the grid. “PENDING” indicates runs deferred to the
post-submission version. For MMR, stage-payoff curvature is established analytically in Appendix C.2; the pending
entries concern the continuation-value verification only.
7We keep solver parameters regarding the best-response tolerance, maximum iterations, and damping constant across
runs.
38
