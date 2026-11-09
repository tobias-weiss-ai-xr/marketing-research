---
title: 'Agentic Limit Order Books: Phase Transitions and Market Impact'
url: https://arxiv.org/abs/2609.31260
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Jan Rosenzweig
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.31260
pages: 6
chars: 16548
fetched_at: '2026-11-08T13:20:17+00:00'
kb_version: 1
---

# Agentic Limit Order Books: Phase Transitions and Market Impact

Agentic Limit Order Books: Phase Transitions and Market Impact
Jan Rosenzweig
September 28, 2026
Abstract
We investigate the systemic macroscopic dynamics emerging from Limit Order Books (LOBs) populated
exclusively by autonomous reinforcement-learning agentic traders. By formalizing agent interactions within a
microscopic order-matching engine, we examine two fundamental quantitative phenomena: equilibrium phase
transitions in order flow regime shifts, and the structural dynamics of market impact. We show that agen-
tic LOBs exhibit distinct phase boundaries separating orderly price discovery from hyper-volatile cascade
states, governed by critical thresholds in the number of agents and observable market depth. Furthermore, we
demonstrate that market impact under agentic liquidity provision deviates from classical square-root dynamics,
exhibiting distinct dissipative, balanced, and non-dissipative regimes under non-linear feedback loops.
1 Introduction
Modern quantitative finance is undergoing a fundamental structural paradigm shift. The historical transition from
manual execution to rule-based algorithms (such as TW AP, VW AP etc) is now giving way to fully autonomous,
agentic trading architectures. Driven by advances in reinforcement learning and large-scale reasoning systems,
contemporary software agents do not simply execute static instructions; they dynamically interpret order book
states, infer competitor intent, adapt execution horizons, and adjust inventory limits in real time.
While agentic workflows promise enhanced micro-structural efficiency and superior adaptive execution for
individual market participants, their aggregate behavior in closed-loop ecosystems presents unprecedented systemic
challenges. As emphasized by Farmer & Foley [1], classical equilibrium models fail to capture emergent macro-
level dynamics in financial networks, making agent-based modeling essential. When limit order books (LOBs) are
populated predominantly by adaptive agents, it is unclear whether standard market microstructure assumptions
regarding order arrival rates, liquidity provision, and price impact still stand, or whether they break down and
how [5, 6]. The strategic co-adaptation of these agents creates intricate non-linear feedback loops, giving rise to
emergent macro-level phenomena that cannot be predicted by analyzing single-agent behavior in isolation.
Our main concern, however, is the potential use of agents in simulation. By populating an LOB with au-
tonomous agents, we get a reactive environment against which to test trading strategies. Unlike in traditional
tick-level simulations, which rely on impact models to predict how the other traders would or could react to trading
and order flow from a given strategy, an agentic order book is by construction a reactive environment, in which
such reactions are played out as they would be in live trading.
To use a chess analogy, if trading against a historical simulation is analogous to studying historical chess games,
trading against agents is then analogous to playing against a chess engine.
To better understand the statistical physics and quantitative market microstructure [4] of such systems, this
manuscript presents a formal mathematical and computational framework for analyzing aggregate dynamics in
Agentic Limit Order Books(A-LOBs). Specifically, we focus on two core financial phenomena:
1.Phase T ransitions and Market Stability:We map the parameter space governing agent population sizes
and market depth to establish critical phase boundaries separating stable, efficient price discovery regimes
from frozen order books and catastrophic liquidity collapse.
2.Market Impact and Dissipation Dynamics:We examine how transient and permanent market impact
functions behave when liquidity providers are themselves dynamic agents, detailing the transition from
dissipative (absorptive) markets to non-dissipative (cascade-inducing) regimes.
Understanding these dynamics is paramount not only for quantitative traders seeking to optimize execution
strategies in agent-dominated markets, but also for risk managers and market regulators charged with maintaining
orderly price discovery amidst automated cascade risks.
2 Model Setup & Agent Topology
Consider a discrete-time continuous double auction populated byNautonomous agents, partitioned into three
functional classes: Market Agents (M), Scalpers (S), and Liquidity-Providing agents (L).
1
arXiv:2609.31260v1  [q-fin.TR]  25 Sep 2026

Liquidity-Providing Agents operate with a fixed depth horizondand quantity limitL, observing the Order
Book up to±dticks from the best bid and ask. They are trained to maximize trading PnL within a fixed time
horizon by issuing and modifying limit orders, while employing market orders primarily to unwind inventory when
breaching the holding threshold±L.
Scalpers are topologically analogous to Liquidity-Providing Agents but operate with a constrained market
depth ofd= 2, observing only the touch and next-to-touch levels on both sides of the book.
Market Agents act as stochastic liquidity takers, issuing random market buy and sell orders at a fixed frequency
with sizes bounded by a maximum limit.
The limit order book state at discrete time steptis represented by the arrayS t = (S b t , Sa t , Qb t , Qa t ), denoting
bid/ask prices and quantities respectively. Each agenti∈ {1, . . . , N}reacts to book updates, executed trades,
own fills, and timed callbacks by generating order actions:
ai,t ∈ {Limit Buy,Limit Sell,Market Buy,Market Sell,Modify/Cancel}(1)
The mid-price evolution follows the standard relation:
St = Sb,1 t +S a,1 t 2 (2)
whereS b,1 t andS a,1 t denote the best bid and ask prices, respectively.
3 Phase Transitions in Agentic LOBs
The interaction of adaptive agents in a shared order book naturally gives rise to collective phase behavior. Given
that altering the number of Market Agents is mathematically equivalent to scaling their execution frequency, we
fix the number of Market Agents to|M|= 1.
We analyze isotropic order books where all Liquidity Providers share identical parameters (d, L), and all
Scalpers operate with an identical limitL. We evaluate system dynamics as a function of the number of Liquidity
Providersn=|L|and their observable Market Depthd, while scaling the Scalper population proportionally as
max(3,⌊n/3⌋). The floor of three Scalpers is strictly required to prevent instantaneous structural collapse; below
this threshold, 0–2 Scalpers fail to consistently form the touch, depriving Liquidity Providers of reference prices.
Formally, this agentic system maps directly onto an open statistical mechanical system:
•The volume executed by Market Agents serves as the drivingtemperature(T).
•The number of Liquidity Providersnrepresents the system’sthermal capacity(C v).
•The observable Market Depthdmaps to systemvolume(V), or inversely, its effective thermodynamic
pressure(P).
Varyingnanddthus controls the ratio of driving temperature to thermal capacity alongside the effective
system pressure.
Each order book path is instantiated with identical initial conditions and allowed to iterate for 100,000 timer
callbacks across 10,000 Monte Carlo paths per parameter configuration. We track two macroscopic observables:
1. Mid-price normal volatilityσ, measured in ticks.
2. Collapse probabilityp, defined as the empirical likelihood that the order book completely empties (i.e., zero
liquidity on at least one side) before path completion.
3.1 Regime Shifts and Critical Thresholds
As the agent countnand market depthdvary, the system undergoes sharp first-order phase transitions separating
three distinct macroeconomic regimes:
1.V aporized / Collapsed Phase (n < nc):Insufficient liquidity provision to absorb external order flow,
driving the order book to extinguish in finite time (p >90%). Such abrupt regime shifts closely reflect
critical power-law fluctuation behaviors found across financial markets [3].
2.Continuous Liquidity Phase (n > nc, d > dc(n)):Stable, functional markets operating with robust
liquidity, finite non-zero volatility, and efficient price discovery.
3.F rozen Phase (d < dc(n)):Excessive agent density compressed into inadequate market depth. Price
volatility vanishes (σ≪1 tick) as agents lock into tight queue positions, stifling price discovery.
2

Figure 1: Evolution of the Order Book in the Solid (left), Liquid (centre) and Vapour (right) Phases.
Positive quantities denote Bids, negative quantities denote Asks, Mid Price is shown in black.
Figure 2: Mid-price volatilityσand probability of order book collapsepacross varying Liquidity Provider count
nand Market Depthd. System configuration: 1 Market Agent (Max Qty = 50, frequency = 1 trade/callback),n
Liquidity Providers (Max Qty = 50), and max(3,⌊n/3⌋) Scalpers (Max Qty = 10).
Typical Order Book and Mid Price trajectories for all three phases are shown in Figure 1.
The physical regimes and corresponding financial market states are summarized in Table 1.
Empirically, our simulation results show that the boundary separating the Collapsed and Continuous phases
is fixed innand invariant to depthd, whereas the boundary separating Continuous and Frozen regimes scales
linearly with agent density:
dc ∝n, n c = const. (3)
These scaling relations are intuitively clear. Adding a liquidity provider requires proportional expansion in
spatial depthdto maintain queue flexibility. Conversely, once minimum operational capacityn c is met, zero-mean
non-directional flow cannot systematically deplete the book, rendering depth parameterdsecondary to overall
structural stability.
It is important to note that the phase behaviour illustrated in Figure 2 depends on the aggressive flow being
drift-free. If the aggressive flow is significantly biased, it will eventually fill a finite number of Liquidity Providers
for any fixedn, resulting in the system reaching the Collapsed Phase in finite time forn > n c.
4 Market Impact Dynamics
To evaluate market impact, we inject a single aggressive liquidity-taking order into the system. The book is
initialized and run fort Q = 10 timer callbacks, at which point an aggressive buy order of sizeQis executed. The
simulation is then continued for the remainder of the path.
Impact is measured via thez-score comparing impacted paths (Q= 200) against non-impacted control paths
(Q= 0),
z(t) = µI (t)−µ N (t)p
σI (t)σN (t)
(4)
whereµ I (t), σI (t), µN (t), σN (t) are the ensemble mean and standard deviation of the impacted paths and non-
impacted paths respectively, evaluated at timet.
3

Table 1: System Regimes in Agentic Limit Order Books
Phase Control Parameters(n, d)Market State
Collapsed Order Bookn < n c Cascade / Breakdown
Continuous Liquidityn > n c, d > dc(n) Stable / Efficient Price Discovery
Frozen Order Bookd < d c(n) Illiquid / Stalled Price Discovery
4.1 Market Impact in the Continuous Liquidity Phase
Figure 3 illustrates impact propagation within the Continuous Liquidity Phase. The system response decomposes
into three temporal phases:
•Primary Impact:Instantaneous price displacement caused by physical liquidity consumption ofQshares.
•Secondary Impact:Intermediate propagation driven by Scalpers absorbing inventory imbalances and
passing residual risk onto Liquidity Providers.
•Impact Decay / Permanent Shift:Relaxation dynamics determining whether the market absorbs the
trade or enters a cascading regime.
(a) Dissipative;n= 11,d= 38;σ=
3.232 ticks
(b) Balanced;n= 20,d= 38;σ=
4.2105 ticks
(c) Non-dissipative;n= 23,d= 30;
σ= 5.529 ticks
Figure 3: Impact and dissipation in the Continuous Phase: First 100 impacted (green) vs. non-impacted (purple)
price paths, alongside resultingz-scores.
We observe a clear transition fromdissipative dynamicsat low volatility (σ⪅4.21 ticks, Figure 3a), where
impact decays over time, tonon-dissipative dynamicsat high volatility (σ⪆4.21 ticks, Figure 3c), where an initial
trade triggers self-sustaining price cascades. The critical boundary (σ≈4.21 ticks, Figure 3b) exhibits perfectly
permanent, non-decaying market impact.
4.2 Market Impact in the Frozen Phase
In the Frozen Phase (Figure 4), impact dynamics display distinct solid-state mechanical analogs:
•Cracking Regime (σ⪅0.1ticks):Stress from the aggressive order dislodges a small subset of paths,
while the majority remain locked (Figure 4a).
•Melting Regime (σ⪆0.1ticks):Impact energy destabilizes queue positions, causing widespread unfreez-
ing and rapid structural transition across paths (Figure 4b).
Crucially, these agentic impact profiles mirror empirical microstructure anomalies observed in modern equity
and futures markets (see e.g., Bouchaud et al., Figure 4 [2]).
4

(a) Cracking;n= 29,d= 10;σ= 0.0051 ticks
 (b) Melting;n= 14,d= 10;σ= 0.432 ticks
Figure 4: Impact and dissipation in the Frozen Phase: First 100 impacted (green) vs. non-impacted (purple) price
paths, alongside resultingz-scores.
5 Discussion & Implications
The emergence of multi-agent reinforcement learning architectures in execution algorithms introduces non-linear
feedback loops that are absent in classical, rule-based quantitative models. Our findings demonstrate that even
minimal, homogeneous multi-agent LOB systems give rise to complex non-equilibrium thermodynamic behavior,
regime shifts, and phase transitions.
These insights carry significant practical implications across quantitative finance:
•Execution Optimization & Optimal Execution:Traditional execution models based on square-root
impact assumptions [6] fail in non-dissipative agentic regimes. Execution algorithms must dynamically assess
local market phase state (n, d) to prevent triggering strategic agentic cascades.
•Systemic Risk & Circuit Breakers:The sharp first-order boundary separating continuous liquidity from
order book collapse (n < nc) illustrates how rapidly liquidity can evaporate. Regulators and exchanges must
design adaptive circuit breakers that account for automated liquidity cancellation by dynamic agents during
market stress.
•Risk Management:Standard Value-at-Risk (VaR) models assume continuous market clearing [5]. In
agentic markets, transition into frozen or collapsed phases invalidates liquidity adjustments, necessitating
stress-testing regimes built explicitly around multi-agent phase shifts.
An obvious limitation of the analysis in this paper is the homogeneity of the agent population. While this is
helpful in terms of allowing us to map the entire phase space in terms of two parameters (n, d) and summarize the
phase behaviour, it is clearly unrealistic in terms of representing actual live trading LOBs.
6 Conclusion
We have presented a statistical mechanics framework for Agentic Limit Order Books, establishing formal mappings
for phase transitions, liquidity collapse boundaries, and non-dissipative market impact functions. Building on
stochastic order book foundations [4], we show that agentic interactions generate distinct macroscopic regimes —
Collapsed, Continuous, and Frozen — each characterized by unique price discovery and impact profiles.
The main direct implication of this work is to with execution strategies, and we show that it is paramount to
take into account the LOB phase behaviour when designing and running any such strategies, because the market
response to any strategy can be markedly different in different phases.
5

Our main concern is with using the A-LOB as a simulation medium, in order to test, validate and risk assess
any strategy, both before and after deploying it to a live environment. The results presented in this paper validate
this approach, demonstrating that A-LOBs reproduce a number of realistic behaviours encountered in live trading.
References
[1] Farmer, J. D., & Foley, D. (2009). The economy needs agent-based modelling.Nature, 460(7256), 685–686.
[2] Bouchaud, J. P., Gefen, Y., Potters, M., & Wyart, M. (2003). Fluctuations and market impact in financial
markets: an empirical study.Quantitative Finance, 3(4), 251–261.
[3] Gabaix, X., Gopikrishnan, P., Plerou, V., & Stanley, H. E. (2003). A theory of power-law distributions in
financial market fluctuations.Nature, 423(6937), 267–270.
[4] Cont, R., Stoikov, S., & Talreja, R. (2010). A stochastic model for order book dynamics.Operations Research,
58(3), 549–563.
[5] Hasbrouck, J. (2007).Empirical Market Microstructure: The Institutions, Economics, and Econometrics of
Securities Trading. Oxford University Press.
[6] Kyle, A. S. (1985). Continuous auctions and informed trader.Econometrica, 53(6), 1315–1335.
6
