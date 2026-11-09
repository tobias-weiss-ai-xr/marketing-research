---
title: 'Contagion on the Trading Floor: How Adversarial Signals Spread in Multi-Agent Trading Systems'
url: https://arxiv.org/abs/2609.19789
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Qi Rong Sua
- Junhao Dong
- Nguyen Duc Thai
- Yuqing Wen
- Cheston Tan
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.19789
pages: 25
chars: 63419
fetched_at: '2026-11-08T13:24:18+00:00'
kb_version: 1
---

# Contagion on the Trading Floor: How Adversarial Signals Spread in Multi-Agent Trading Systems

Contagion on the Trading Floor: How Adversarial
Signals Spread in Multi-Agent Trading Systems
Qi Rong Sua1, Junhao Dong1,3, Nguyen Duc Thai1, Yuqing Wen2, Cheston
Tan3, and Yew-Soon Ong1,3 ()
1 Nanyang Technological University, Singapore
{suaq0001,junhao003,ducthai001,asysong}@ntu.edu.sg
2 National University of Singapore, Singapore
e1351400@u.nus.edu
3 Centre for Frontier AI Research, IHPC, A*STAR, Singapore
cheston_tan@a-star.edu.sg
Abstract.Multi-agent trading systems built on large language models
(LLMs) are beginning to appear in quantitative finance, yet their robust-
ness to adversarial inputs is largely unknown. We study the vulnerability
ofLLMtrading stacks to black-box, input-only attacks that enter solely
via admissible social-media feeds. We introduce theGeneric Multi-Agent
Trading System(GMATS), a framework that captures modern multi-
agent trading architectures and instantiate a class of black-box poison-
ing attackers that treat an LLM as a post generator and inject budget-
constrained, plausibly benign social-media content into the analyst’s ev-
idence stream. We define contagion metrics that trace how adversarial
content propagates through the stack, including belief-shift scores at ana-
lyst and coordinator layers and attack–clean deltas on standard backtest
metrics. Experiments on a safe offline benchmark with historical market
and social data show that even simple input-only attackers can materi-
ally degrade risk–return profiles, sharply reducing Sharpe ratios. At the
same time, we find that suitably designed multi-agent topologies and co-
ordinator prompts can dampen adversarial shocks and improve average
robustness under identical poisoning budgets. Our code and dataset are
available in this repository.
1 Introduction
The rapid rise of large language models (LLMs) has led to a corresponding
surge in LLM-based agents and multi-agent systems [28,13,10,21,9]. In quan-
titative finance, a growing line of work has built multi-agent trading systems
on top of LLM agents, reporting substantial gains in backtested performance
metrics. These architectures typically decompose a trading desk into specialized
agents (fundamental, sentiment, risk, execution) that communicate via natu-
ral language to produce trades [29,26,33,30]. At the same time, recent results
such asAgentSmith[8] showing that a single adversarial input can jailbreak
many multimodal LLM agents exponentially fast highlight how composition can
arXiv:2609.19789v1  [cs.AI]  17 Sep 2026

2 Sua et al.
amplifyrather than mitigate vulnerabilities. When agents reason about one an-
other’s outputs, small perturbations at one node may cascade into large changes
in the final decision.
ThistensionraisesanaturalquestionforemergingLLM-nativetradingstacks:
How vulnerable are multi-agent, LLM-only trading systems to input-only,
black-box attacks that enter solely through admissible evidence streams?
We present, to the best of our knowledge, the first systematic study of the
robustness of multi-agent trading systems to such black-box, input-only adver-
saries. We focus on attacks that operate entirely through a realistic and im-
portant channel: equity-related social media. Among typical evidence streams
(fundamentals, news, social), social media poses the largest adversarial surface
[19,15,11]. It is high-volume, weakly curated, and easily seeded with misinfor-
mation [20], yet removing social-media analysts is often not realistic: sentiment
and flow signals from social platforms are a major driver of performance in many
equity strategies [3,25,1,23]. To analyze these threats in a way that is compara-
ble across architectures, we introduce theGeneric Multi-Agent Trading System
(GMATS), a framework tailored for LLM-based multi-agent trading systems.
GMATS captures a common pattern across existing systems:analystagents in-
gest environment data (fundamentals, news, social media) and produce textual
insights; one or morecoordinatoragents fuse these insights into a trading stance
and critically evaluate them; optionalcontrollerandexecutorcomponents en-
force risk and translate stances into trades.
Contributions.
1.GMATS: a unifying framework for LLM trading stacks.We intro-
duce theGeneric Multi-Agent Trading System(GMATS), a framework for
LLM multi-agent trading systems and we prove that a broad class of existing
trading agents can be compiled into this form.
2.Contagion metrics and evaluation protocol.We define contagion met-
rics that track how adversarial content propagates through the stack, includ-
ing belief-shift scores (BSS) at analyst and coordinator layers and attack–
clean deltas on standard backtest metrics (returns, volatility, Sharpe). This
yields a reusable protocol for stress-testing multi-agent LLM trading sys-
tems.
3.Dataset and reference implementation.We use an offline one-year cor-
pus of equity-related social-media posts (Twitter and Reddit) to drive the
social analyst’s evidence stream. Dataset details and release information are
provided in Section 5.
4.Empirical study of attacks and defenses.We instantiate input-only
poisoning attackers and quantify their impact on belief contagion and risk–
return profiles under varying poisoning rates. We then compare alternative
GMATSarchitecturesincludingsingle-agent,multi-analyst,andtwodefense-
oriented coordinator designs (wide bull–bear and a pairwise-triangulation

Contagion on the Trading Floor 3
coordinator) and show that coordinator-level structure can substantially
dampen adversarial shocks and improve robustness under identical poisoning
budgets.
Related works.Recent LLM-driven trading frameworks coordinate specialized
agents (e.g., fundamental, sentiment, technical, risk) via debate and role decom-
position to emulate trading desks.TradingAgentsformalizes this pattern with
analyst teams feeding a decision agent under risk controls, whileTradingGroup
adds structured self-reflection and an end-to-end data-synthesis loop to improve
coordination and backtested performance.ContestTradeintroduces an internal
contest mechanism with separate Data and Research teams whose outputs are
continuously scored and filtered by real-market feedback, andQuantAgenttar-
gets high-frequency trading with price-driven Indicator, Pattern, Trend, and
Risk agents operating over short-horizon market signals. Together, these sys-
tems highlight the importance of inter-agent communication, ranking, and in-
gestion pipelines that GMATS abstracts and that our input-only attacker seeks
to perturb [29,26,33,30]. However, these systems are typically evaluated only on
backtested performance under benign data, leaving their robustness to adversar-
ial evidence especially social media and the resultingcontagion dynamicsacross
agents largely unexplored.
2 Generic Multi-Agent Trading System (GMATS)
Definition 1 (GMATS).(Architecture in Figure 1.) LetAbe the asset set
(|A|=n) and letTbe a discrete time index set. AGMATSinstance is the tuple
G=

A, A, C, K, X,S, Σ,D,L, Λ,E

,
with the following components:
–Agents.AnalystsA(|A| ≥1), coordinatorsC(|C| ≥1), controllersK(|K| ≥
0), executorsX(|X| ≥0). Agents may be LLM-based or programmatic.
–Typed messages and schema.Sis a finite set of message types. A mes-
sage is
m= (id,src,dst, τ,payload,ts),
withτ∈ Sand timestampts∈T. Messages live on a shared bus; at round
t∈T, only messages withts≤tmay be consumed (point-in-time, PIT).
–Schedule.Σspecifies, for each roundt, the order in which agents are ac-
tivated together with any random seeds used in their calls (e.g., LLM sam-
pling seeds). Each roundtexecutes the pipelineA→C→K→X, with
micro-rounds permitted inside each stage.
–Data and environment.D={D t}t∈T denotes point-in-time data sources
(market, news, social, fundamentals, etc).Eis the execution environment
with state spaceX, which maps orders and current state to fills and next
state:
(fills, χt+1) =E(o t, χt), χ t ∈ X.

4 Sua et al.
Risk Management!
Financial News
Social Media
Stock Market
Environment
Analysts Coordinators
ControllersExecutors
. . .
P/E has compressed from
22x to ...
Spike in negative posts
(+240%) ...
Recent headlines focused
on cut ...
The stock’s sell-off appears
... SELL
Current valuation discount
... BUY
If already long, suggest
reducing ... SELL
SELL
    Action back to env
Everyone’s operating like
a real-world trading firm.
Fig.1.Architecture of the Generic Multi-Agent Trading System (GMATS).
–Coordination and control.L={L t}t∈T denotes coordinator logic that
maps analyst insights and context to stances and draft orders, andΛ=
{Λt}t∈T denotes controller logic that enforces risk and constraint policies on
these stances or orders. We writeξt for any additional context (e.g., portfolio
summaries, constraints) supplied to coordinators and controllers at roundt.
Contracts (per roundt).
1.Analysts (A).Eacha∈Aemits zero or moreinsightmessagesm (a) j with
typeτ∈ Sandts≤t, computed from PIT dataD t and the inbox ofa.
2.Coordinators (C).Consuming all analyst insights at roundt, the coordi-
nator logicL t produces astance
(st, ρt) =L t(insightst, ξt), s t ∈R n,
with metadataρt. Optionally, a draft orderot ∈ Omay be produced in place
ofs t.
3.Controllers (K).The risk/constraints gate
(okt, o′ t) =Λ t(zt, ξt), z t ∈ {st, ot}, o ′ t ∈ O,
enforces limits (exposure, leverage, liquidity, CVaR/SL/TP, compliance) and
yields an executable ordero′ t (orok t = falseif no trade is allowed).
4.Executors (X).If|X|>0, an executor submitso ′ t to the environment:
(fillst, χt+1) =E(o ′ t, χt).
If|X|= 0,Eis called directly by the coordinator/controller as the final step.

Contagion on the Trading Floor 5
Orders space.Discrete orders live in
Odisc ={−1,0,1} n,
and continuous portfolio weights live in
Ocont ⊆R n,
e.g., withℓ 1/ℓ∞ and leverage caps. We writeO=O disc ∪ Ocont for the overall
order space.
Invariants.(i)PIT:all consumed evidence/messages satisfyts≤t; (ii)Re-
playability:each run emits a complete log of messages, prompts, LLM re-
sponses, and orders, so that the resulting trajectory can be replayed offline for
the sameΣwithout re-querying the LLMs; (iii)Schema safety:only well-typed
messages (τ∈ S) are routable.
Theorem 1 (Expressivity of GMATS).LetMbe a multi-agent trading
pipeline that satisfies:
1.Typed message passing.Agents inMcommunicate only via messages
from a finite schemaS M, and each agent’s behavior is a function of its
inbox and point-in-time environment data.
2.Point-in-time discipline.At roundt, every agent inMmay only consume
messages and environment data with timestamps≤t.
3.Stage separation.For each roundt, the computation of trading decisions
inMcan be decomposed into four phases: (i) evidence ingestion, (ii) fusion
and scoring, (iii) constraints and risk checks, and (iv) order execution.
Then there exists a GMATS instance
G= (A, A, C, K, X,S, Σ,D,L, Λ,E)
such that, for any initial environment state and fixed random seeds, the sequence
of executed orders produced byMis identical to the sequence produced byG. We
provide the proof in supplementary materials.
Corollary 1 (Compilation of existing frameworks).TradingAgents, Trad-
ingGroup, ContestTrade, and QuantAgent all satisfy the conditions of Theorem 1
and can be compiled into GMATS by mapping their ingestion, fusion, risk, and
execution components into theA→C→K→Xpipeline and unrolling their
internal coordination into micro-rounds ofΣ.
3 Metrics
Setup.We evaluate anattackrun against aclean(no-poison) baseline overT
decision times andNtradable assets. LetPbe the set of poisoned messages, and

6 Sua et al.
letTop k(t)denote thekhighest-ranked items actually consumed by the social
analyst at timet. We define the poison-consumption rate
ppoison = 1 T
TX
t=1

Topk(t)∩ P

k ,(1)
and in Experiments A–C we vary the attacker’s budget untilppoison hits target
levels (e.g.,15%,30%, . . . ,75%). Unless stated otherwise, performance metrics
are reported asattack minus clean.
3.1 Contagion Metrics
Belief Signal Shift (BSS).BSS measures how the attack systematically shifts
the agent’s internal numeric beliefs, even before trades are placed. Letfattack i,t
andf clean i,t denote the forecast for assetiat timetunder the attacked and clean
runs, respectively. We define the aggregate belief shift as
BSS = 1 T N
TX
t=1
NX
i=1

f attack i,t −f clean i,t  .(2)
A positive BSS indicates that, on average, forecasts become more bullish under
attack, while a negative BSS indicates a net shift toward more bearish beliefs.
3.2 Performance Metrics (FinSABER; attack–clean)
Protocol.We adopt the FinSABER performance protocol as described in [14].
Let{r t}T t=1 be the net (after-cost) portfolio returns at the chosen frequency
(daily by default). DefineAas the annualization factor (A=252for daily).
Cumulative and annualized return.These metrics quantify how much the port-
folio grows in total (CR) and what that growth corresponds to as an annualized
rate (AR), under attack versus clean.
CR =
TY
t=1
(1 +r t)−1,AR = (1 + CR) A/T −1.(3)
Annualized volatility.Annualized volatility captures the scale of return fluctua-
tions, i.e., how “noisy” or risky the strategy is over a year.
A V =
√
Asd(r t).(4)
Sharpe ratio.Sharpesummarizesrisk-adjusted performanceusing totalvolatility
[22].
SR =
√
Amean(r t)
sd(rt) .(5)

Contagion on the Trading Floor 7
Delta reporting.To isolate the effect of the attack, we report performance as the
difference between attack and clean runs. For each metricm∈ {CR,A V,SR},
we compute
∆m=m attack −m clean.(6)
4 Attacker Model
Attacker taxonomyWe consider two simple but representative attack policies.
Both respect the same daily budgetBon the single target asset.random at-
tackerserves as a minimal baseline. On each daytit spends its budgetB
by generating posts with random sentiment directions, independent across posts
and days (e.g., sampling bullish vs. bearish with equal probability). This attacker
injects noise without targeting and any contagion it induces reflects a general
sensitivity of GMATS to low-level social perturbations. Thealways-negative
attackeris a simple one-sided stressor. On each daytit spends its entire budget
Bgenerating strongly bearish posts about the target asset. This policy approxi-
mates a persistent negative-narrative campaign (e.g., a “short-and-distort” style
effort) that continuously pushes sentiment in the same direction. Together, these
two attackers span a simple design space: untargeted, sign-symmetric noise (ran-
dom) and untargeted but persistently one-sided pressure (always-negative). Our
experimentsinSection5comparetheirinducedcontagionprofilesundercommon
budgetsBand varyingp poison.
Scope and admission assumption.We measuredownstream contagion condi-
tioned on adversarial content being present in the social evidence stream, rather
than modeling how such content is created, promoted, or filtered. Because real
tradingstacksdifferwidelyinpostscoring/admission(heuristics,sentimentmod-
els, LLM filters), an end-to-end seeding model would confound results with
system-specific details. We therefore assume attacker posts areadmissibleand
vary attack strength via theeffective poison rateppoison, defined as the fraction
ofconsumed(top-k) posts attributable to the attacker, which isolates suscep-
tibility under a fixed retriever. This is realistic on open social channels where
volume can surface some posts without retriever compromise [6,27], and where
pipelines often upweight high-salience or strongly valenced content [18,24,34].
Thusp poison serves as an abstract knob capturing posting intensity and any up-
stream amplification while keeping evaluation focused on what happensafter
poisoned posts enter the system.
5 Experiments
5.1 Data and Setup
We instantiate GMATS with three analyst roles (social, fundamentals, news),
one coordinator, one risk controller, and one executor. All experiments use
gpt-4o-miniand ran over the same historical window (01 Nov 2021–01 Dec

8 Sua et al.
Table 1.Experiment A (GMATS, fixed architecture): results are attack–clean deltas
across fraction of consumed posts that are poisoned,ppoison. Values are averaged across
5 runs.
Metric15% 30% 45% 60% 75%
Random Attacker
BSSanalyst +0.077 +0.163 +0.214 +0.252 +0.280
BSScoord +0.091 +0.269 +0.270 +0.332 +0.360
∆CR+0.020 +0.009 +0.023 +0.016 +0.017
∆Sharpe+0.360 +1.080 +2.040 +0.998 +0.600
∆Vol+0.082 +0.036 +0.051 +0.104 +0.150
Always Negative Attacker
BSSanalyst −0.777−1.084−1.204−1.291−1.413
BSScoord −0.409−0.544−0.544−0.642−0.594
∆CR−0.006−0.032−0.036−0.043−0.044
∆Sharpe+0.864−5.501−5.970−6.167−6.060
∆Vol+0.005 +0.010 +0.020 +0.035 +0.046
2021) for AAPL. We focus on a single ticker/month for controlled mechanis-
tic analysis. Extending to more tickers or months primarily increases sample
size (tightening uncertainty) but does not change the propagation mechanism
captured by our contagion metrics under the same PIT evidence-admission and
poisoning budget. We also release a one-year corpus of equity-related social me-
dia posts collated from tweets and reddit for the top 7 large-cap tech companies
(AAPL, AMZN, GOOG, META, MSFT, TSLA, NFLX) spanning 30 Sept 2021 –
29 Sept 2022. Each record provides a timestamp, tweet text, ticker, and company
name. We build an offline environment using historical equity prices. GMATS
agents operate strictly in PIT mode, consuming only the data available at each
round preventing leakage of future information [7].
5.2 Experiment A: Contagion vs Poisoning Rate in GMATS
Experiment A asks:how much contagion and damage can an input-only attacker
cause in a fixed GMATS instance as we increase the share of poisoned evidence
seen by the system?
Table 1 summarizes the dose–response across attacker type and realized poi-
soning rate (ppoison ∈ {15,30,45,60,75}%). For each(attacker, ppoison)pair we
report attack–clean deltas for belief-contagion metrics and trading performance.
Across metrics, we observe a clear dose–response in belief shift. For both at-
tackers, the absolute value of BSS increases withppoison, but the effect is much
stronger for the Always Negative attacker: BSSanalyst moves from roughly−0.78
at15%to about−1.41at75%, while BSS coord tracks a smaller but still sub-
stantial negative shift. The coordinator is therefore less sensitive than the social
analyst, reflecting partial damping by the fundamentals and news analysts, but
the negative bias propagates through the stack rather than being fully absorbed.

Contagion on the Trading Floor 9
Experiment B  Does Topology Matter?
Baseline Wide Coordinator Single
News
Social
Fundamentals
News
Social
Fundamentals
Coord
Coord1
Coord2
Coord
Fig.2.Experiment B (architectural contagion).Three GMATS realizations with
identical tools but different topologies.
On the performance side, the Random attacker produces only mild changes:
∆CR and∆Sharpe remain small and sometimes slightly positive, suggesting
that low-rate, directionally symmetric noise in the social channel does not reli-
ably harm the system and may occasionally coincide with beneficial risk adjust-
ments. In contrast, the Always Negative attacker systematically degrades sharpe
and cumulative return asppoison increases. There is a pronounced regime change
around30%–45%ingestion:∆Sharpe flips from mildly positive at15%to sharply
negative (around−6), while volatility also worsen. Overall, Experiment A in-
dicates that GMATS is relatively robust to low-level random perturbations but
becomes highly vulnerable once a single channel is populated with sufficiently
dense, directional adversarial signals. Sharpe is annualized and can be sensi-
tive to short evaluation windows [17,2], as a result, absolute Sharpe levels in our
one-monthstudyarenotintendedasstandaloneperformanceclaims.Ourconclu-
sions are based onattack–clean deltas(including the direction/sign of∆Sharpe)
and are cross-checked against∆CR and∆Vol. We also ran Experiment A on
TradingAgents, the full results are reported in the supplementary materials.
5.3 Experiment B: Architectural Contagion Across Topologies
Experiment B asks a complementary question:does a multi-agent message-
passing topology amplify adversarial shocks compared to a single-agent system?
To isolate architectural effects, we study two additional realizations of GMATS
with identical tools, prompts, and budgets but different message-passing graphs
(Figure 2):

10 Sua et al.
Table 2.Experiment B (GMATS, Topology): attack–clean deltas across fraction of
consumed posts that are poisoned,ppoison. Values are averaged across 5 runs.
Metric15% 30% 45% 60% 75%
Wide Coordinator
BSSanalyst −0.754−0.964−1.136−1.213−1.291
BSScoord1 −0.271−0.339−0.455−0.478−0.467
BSScoord2 −0.284−0.356−0.470−0.506−0.471
BSSfuse −0.281−0.353−0.471−0.499−0.480
∆CR−0.003−0.014−0.022−0.024−0.014
∆Sharpe+3.235 +0.436−1.980−3.113−0.062
∆Vol−0.005−0.012−0.010−0.015−0.007
Single Agent
BSSanalyst −1.148−1.364−1.415−1.491−1.386
∆CR−0.052−0.056−0.057−0.062−0.054
∆Sharpe−7.153−7.150−7.274−6.773−8.670
∆Vol+0.007 +0.015 +0.019 +0.043 +0.015
– Wide coordinator (multi-agent): the three analysts feed into two coor-
dinators with cross-talk before a shared controller, increasing the number of
aggregation hops and inter-agent interactions.
– Single agent: a monolithic agent that directly ingests social, news, and
fundamentalstreamsandoutputsportfolioweights,withnointernalanalyst–
coordinator decomposition.
Table 2 reveals that architecture has a first-order effect on both belief shift
and trading damage. Under the Single Agent baseline, the Always Negative
Attacker induces consistently larger-magnitude belief shifts and substantially
worse performance: BSSanalyst is around−1.1to−1.5across poisoning rates,
and the corresponding∆Sharpe remains strongly negative (roughly−7to−9)
with sizeable drops in cumulative return compared to the wide coordinator.
In contrast, the Wide Coordinator topology attenuates the attack. The social
analyst still becomes increasingly bearish asppoison grows, but the downstream
coordinator ensemble (coord1, coord2, and their fused view) exhibits smaller-
magnitude BSS values, indicating partial damping of the contaminated social
signal by the additional analysts and coordination stages. Trading impact is also
milder:∆CR remains close to zero,∆Sharpe is even positive at low poisoning
ratesandonlymoderatelynegativeathigherrates,andvolatilitydeltastaymuch
closer to the clean baseline. Overall, Experiment B suggests that multi-agent
message passing with heterogeneous information sources candampen, rather
than amplify, adversarial shocks.

Contagion on the Trading Floor 11
Experiment C  More Robust Topology
Pairwise Triangulation Coordinator Wide Coordinator Bull - Bear
News
Social
Fundamentals
News
Social
Fundamentals
Bullish
Bearish
Coord1
Coord2
Coord3
Coord
 Coord
Fig.3. Experiment C (robust coordinators).Two defense-oriented coordinator
designs—pairwise triangulation and wide bull–bear—aimed at making GMATS more
robust to adversarial social signals.
5.4 Experiment C: Robust Architectures for Contagion Mitigation
Experiment C turns to defenses:given a fixed attacker, how far can we push
down contagion and trading damage by redesigning the coordinator layer?
We modify only the coordinator topology, instantiating two defense-oriented
designs (Figure 3):
– WideCoordinatorBull–Bear.Twocoordinatorsreceivethesameanalyst
inboxes but are instructed via prompts and routing to focus exclusively on
either bullish or bearish signals. A fuse coordinator then aggregates their
reports and scorecards into a final stance. This forces the system to explicitly
surface and reconcile opposing narratives [5] instead of allowing a single
coordinator to ignore minority evidence.
– Pairwise Triangulation Coordinator.Three coordinators with partially
overlapping mandates read the same analyst outputs. Their views are then
fused by a meta-coordinator that is encouraged to downweight outliers and
reward pairwise agreement, yielding a more conservative aggregate stance
when the inputs disagree.
As in Table 3, in theWide Coordinator Bull–Beardesign, the bull and
bear specialists each move only modestly in the negative direction, and the fused
coordinator stays in an intermediate regime (e.g., BSSfuse between about−0.4
and−0.6across poisoning rates). This suggests that forcing separate bullish and
bearish views limits the extent to which a unidirectional attack can fully domi-
nate the final stance. Trading impact is likewise muted:∆CR remains very close
to zero, volatility and drawdown deltas stay small, and∆Sharpe ispositiveat all

12 Sua et al.
Table 3.Experiment C (GMATS, Defense): attack–clean deltas across fraction of
consumed posts that are poisoned,ppoison. Values are averaged across 5 runs.
Metric15% 30% 45% 60% 75%
Wide Coordinator Bull–Bear
BSSanalyst −0.668−0.895−0.980−0.983−1.057
BSSbull −0.138−0.184−0.208−0.219−0.211
BSSbear −0.036−0.074−0.085−0.081−0.084
BSSfuse −0.403−0.568−0.559−0.552−0.590
∆CR−0.005−0.006−0.001−0.006−0.013
∆Sharpe+1.871 +2.524 +5.513 +3.234 +0.252
∆Vol+0.002−0.003−0.006 +0.000−0.006
Pairwise Triangulation Coordinator
BSSanalyst −0.790−1.024−1.100−1.185−1.275
BSS1 −0.368−0.502−0.538−0.571−0.615
BSS2 −0.523−0.622−0.678−0.724−0.759
BSS3 −0.029−0.024−0.043−0.038−0.026
BSSfuse −0.314−0.389−0.405−0.403−0.397
∆CR+0.001−0.006−0.011−0.010−0.008
∆Sharpe+2.347 +1.586 +1.069 +0.359 +1.713
∆Vol+0.010 +0.001−0.005 +0.011 +0.005
poisoning levels, often substantially so. Under attack, this coordinator behaves
like a regularizer, improving risk-adjusted performance instead of collapsing as
in the naive coordinator from Experiment A.
ThePairwise Triangulation Coordinatorgoes further in damping con-
tagion at the fused output. Although two of the internal coordinators (1and
2) exhibit sizeable negative BSS values, the third stays near zero and the fused
BSS is consistently less negative than any individual coordinator and than the
baseline coordinator in Experiment A. This indicates that the triangulation rule
is successfully downweighting extreme, attack-aligned views. Again, trading per-
formance under attack is stable: cumulative-return deltas are close to zero, draw-
down changes are small, and∆Sharpe remains positive across all poisoning rates.
Taken together, Experiment C shows that coordinator-level defenses can sub-
stantially reduce effective contagion at the decision layer and prevent the Sharpe
collapse observed in earlier experiments. Rather than being inherently fragile,
multi-LLM architectures can be configured so that additional coordination struc-
ture acts as a form of robustness.
Qualitative contagion traces.To complement the aggregate deltas in Tables 2–3,
we inspect a representativecontagion tracefor AAPL on2021-11-05(Figure 4).
Each panel shows the internal message chain from intermediate coordinators to
the final fused stance, together with the resulting(µ, σ,confidence)scorecards.
Across coordinator designs, the same directional pressure from the social channel
leads to qualitatively different decision-layer outcomes: (i)Wide coordinator

Contagion on the Trading Floor 13
Wide Coordinator Bull-Bear Pairwise Triangulation
Apple Inc. (AAPL) presents a compelling
investment opportunity...I recommend an
Accumulate stance on AAPL. Investors should
consider entering positions at current levels...
Coord1 Coord_bull
Coord_bear
Coord1
fund/social
Coord2
social/news
Coord3
news/fund
"symbol": "AAPL",
"mu": 0.45,
"sigma": 0.45,
"confidence": 0.8
The sentiment surrounding Apple Inc. ($AAPL)
has turned overwhelmingly negative in recent
discussions...Investors may want to adopt a wait-
and-see approach, monitoring for any signs of
stabilization...
"symbol": "AAPL",
"mu": -0.35,
"sigma": 0.4,
"confidence": 0.72
As of November 5, 2021, the investment outlook
for Apple Inc. (AAPL) presents a complex
picture...I recommend a Hold stance on AAPL...
Coord_fuse
"symbol": "AAPL",
"mu": 0.05,
"sigma": 0.425,
"confidence": 0.76
...significant divergence among social,
fundamental, and news analyses ...overwhelming
negative sentiment from social...The current
environment suggests a potential for volatility...
"symbol": "AAPL",
"mu": -0.25,
"sigma": 0.45,
"confidence": 0.83
Coord2
...the overwhelming negative sentiment from
social discussions and the potential for supply
chain issues create a significant risk of
volatility... current sentiment indicates that
significant downward pressure may persist in the
short term.
"symbol": "AAPL",
"mu": -0.33,
"sigma": 0.45,
"confidence": 0.83
...The mixed sentiment from news sources
indicates that while there are opportunities for
growth, the potential for increased volatility
remains high due to external challenges...
Coord_fuse
"symbol": "AAPL",
"mu": -0.25,
"sigma": 0.45,
"confidence": 0.83
...strong negative sentiment...The elevated P/E
ratio suggests that the stock may be overvalued...
"symbol": "AAPL",
"mu": -0.175,
"sigma": 0.3,
"confidence": 0.85
...news analyst report highlights a cautiously
optimistic sentiment...significant volume of social
media discussions reflecting investor unease...
"symbol": "AAPL",
"mu": -0.3,
"sigma": 0.45,
"confidence": 0.8
...strong business quality and profitability... strong
demand for its products...
"symbol": "AAPL",
"mu": 0.275,
"sigma": 0.45,
"confidence": 0.8
Coord_fuse
...concerns about the stock's stability...showcasing
Apple's strong fiscal Q4 earnings...
"symbol": "AAPL",
"mu": 0.1,
"sigma": 0.45,
"confidence": 0.8
Fig.4.Experimental Traces. Bubbles are truncated for space.
produces consistently bearish intermediate stances and a bearish fuse (µ <0),
indicating that the negative social narrative largely survives aggregation. (ii)
Wide bull–bearforces an explicit pro/con decomposition: the bull coordina-
tor remains strongly positive while the bear coordinator turns negative, and the
fuse lands near neutral (µ≈0), yielding a “hold”-like stance rather than a col-
lapse into the attacker’s direction. (iii)Pairwise triangulationmixes channels
before fusion (fund/social, social/news, news/fund), surfacing cross-channel dis-
agreements. The final fuse stays mildly positive (µ >0) despite negative social
evidence, consistent with the quantitative finding that defense-oriented coordi-
nators reduce effective contagion at the decision layer.
5.5 Model Sensitivity: Replication withQwen2.5-7B-Instruct
To test whether our conclusions depend on a single LLM backend, we replicate
the core GMATS experiments withQwen2.5-7B-Instruct[31]. We keep the
ticker, historical window, PIT data protocol, attacker policies, poisoning-rate
targets, prompts, and topologies fixed, changing only the model backend. Table 4
reports attack–clean deltas averaged over 5 runs.
The Qwen replication preserves the main qualitative findings. First, direc-
tional poisoning remains substantially more damaging than random sentiment
injection. Under the Random attacker, performance deltas remain small and of-
tenpositive.UndertheAlwaysNegativeattacker,thebaselineGMATScoordina-
tor shifts sharply negative: BSSanalyst ranges from−1.159to−1.694, BSS coord
ranges from−0.554to−0.871,∆CR decreases from−0.015to−0.061, and
∆Sharpe falls to roughly−5to−6oncep poison ≥30%. This matches the main

14 Sua et al.
Table 4.Additional experiment results underQwen2.5-7B-Instructon GMATS vari-
ants. Entries are attack–clean deltas averaged over 5 runs.
Random Attacker
Metric15% 30% 45% 60% 75%
BSSanalyst −0.368−0.353−0.365−0.515−0.341
BSScoord −0.403−0.457−0.511−0.395−0.439
∆CR+0.010 +0.024 +0.005 +0.016 +0.005
∆Sharpe+0.092 +0.313 +1.969 +1.092 +1.448
∆Vol−0.019 +0.011 +0.012 +0.024 +0.024
Always Negative Attacker
Metric15% 30% 45% 60% 75%
BSSanalyst −1.159−1.606−1.594−1.557−1.694
BSScoord −0.554−0.815−0.782−0.835−0.871
∆CR−0.015−0.036−0.047−0.054−0.061
∆Sharpe+0.227−5.062−5.350−5.873−6.002
∆Vol+0.008 +0.012 +0.014 +0.023 +0.046
Wide Coordinator Bull–Bear
Metric15% 30% 45% 60% 75%
BSSanalyst −0.873−1.123−1.149−1.347−1.313
BSSbull −0.562−0.596−0.630−0.689−0.637
BSSbear +0.008−0.089−0.072−0.171−0.150
BSSfuse −0.293−0.335−0.333−0.409−0.369
∆CR+0.004−0.001−0.005−0.005−0.009
∆Sharpe+3.373 +2.660 +1.341 +0.354−0.115
∆Vol+0.000−0.002−0.004 +0.010 +0.000
Wide Coordinator
Metric15% 30% 45% 60% 75%
BSSanalyst −0.798−0.963−1.119−1.135−1.217
BSScoord1 −0.579−0.697−0.858−0.868−0.777
BSScoord2 −0.632−0.760−0.911−0.985−0.938
BSSfuse −0.634−0.764−0.916−0.939−0.879
∆CR−0.015−0.016−0.021−0.019−0.019
∆Sharpe+0.240−0.210−2.012−0.413−1.100
∆Vol−0.011−0.012−0.012−0.018−0.010
Single Agent
Metric15% 30% 45% 60% 75%
BSSanalyst −1.459−1.805−1.876−1.902−1.859
∆CR−0.045−0.046−0.047−0.052−0.047
∆Sharpe−6.369−6.342−6.242−6.714−7.546
∆Vol+0.002 +0.013 +0.018 +0.028 +0.019
— — — — — —
— — — — — —
— — — — — —
— — — — — —
Pairwise Triangulation
Metric15% 30% 45% 60% 75%
BSSanalyst −0.982−1.241−1.296−1.468−1.522
BSS1 −0.412−0.557−0.601−0.655−0.698
BSS2 −0.584−0.702−0.757−0.803−0.839
BSS3 −0.031−0.028−0.041−0.037−0.030
BSSfuse −0.247−0.318−0.336−0.341−0.334
∆CR+0.002−0.003−0.007−0.008−0.007
∆Sharpe+2.814 +2.031 +1.124 +0.462 +0.736
∆Vol+0.008 +0.002−0.003 +0.009 +0.004
gpt-4o-miniconclusion that dense, one-sided social evidence can induce both
belief contagion and portfolio-level degradation.
Second,thearchitecturalrankingisstable.TheSingleAgentvariantisconsis-
tently brittle, with∆Sharpe between approximately−6.2and−7.5. The Wide
Coordinator still suffers belief shifts, but its trading damage is smaller, with
∆CR close to zero and substantially milder Sharpe degradation. Finally, both
defense-oriented topologies remain robust at the fused decision layer. Wide Co-
ordinator Bull–Bear keeps BSSfuse between−0.293and−0.409, while Pairwise
Triangulation keeps BSSfuse between−0.247and−0.341and maintains posi-
tive∆Sharpe across all poisoning rates. Thus, across two LLM backends, the
same qualitative pattern holds: one-sided social poisoning is the damaging case,
single-agent aggregation is most brittle, and coordinator designs that explicitly
separate or triangulate conflicting evidence reduce downstream damage.
At the same time, the exact magnitudes are model-dependent. Qwen ex-
hibits stronger negative shifts in some intermediate coordinator outputs than
gpt-4o-mini, especially in the Wide Coordinator topology. We therefore in-
terpret BSS and Sharpe deltas as model-conditional stress-test measurements,
while treating the cross-model consistency of the architectural ordering as the
stronger conclusion.

Contagion on the Trading Floor 15
6 Discussion
We deliberately restricted our study to scripted, input-only attackers that are
non-adaptive, single-channel (social), and evaluated under offline replay. An im-
mediate extension is to stress-test GMATS over longer horizons and diverse
market regimes (including prolonged bear markets), where a one-sided narrative
can sometimes align with fundamentals and yield qualitatively different effects.
Building on [4], an RL attacker could be embedded in GMATS to steer an LLM
post generator (e.g., sentiment/timing/style under a budget) and optimize a
contagion-aware objective rather than purely price-based rewards. One simple
form is
rt =−α PnLattack t −PnL clean t scalet +β A BSSanalyst +β C BSScoord,(7)
where scalet = max(ϵ,EMA(|PnL attack t −PnL clean t |))stabilizes learning. Evaluat-
ing such adaptive policies and how coordinator-level defenses shift the resulting
utility–security frontier is an important next step toward characterizing worst-
case brittleness in multi-agent trading stacks.
Beyond sentiment manipulation, an orthogonal threat isinstruction hijack-
ing: untrusted posts may embed prompt injections that subvert role constraints
or induce unintended tool use [16,32,12]. In multi-agent pipelines, a single com-
promised analyst output can cascade through fusion and affect trading decisions.
Future work could benchmark injection success rates in GMATS under realis-
tic retrieval, and test lightweight mitigations (instruction/data separation, tool
gating, and cross-agent consistency checks).
7 Conclusion
We studied how adversarial social signals propagate through LLM-native multi-
agent trading stacks. We introduced the Generic Multi-Agent Trading System
(GMATS) and proposed contagion metrics that trace how poisoned social in-
puts shift beliefs at analyst and coordinator layers and impact downstream risk–
return. Experiments show that these systems are not inherently robust. Injecting
systematically negative posts can cause large belief shifts and materially worsen
returns. We also find certain types of topologies and designs can dampen conta-
gion and improve robustness under attack. Our study is limited to a narrow set of
assets and horizons but is designed as a controlled, reproducible starting point.
We hope that GMATS, together with our contagion metrics and experimen-
tal protocol, can serve as a foundation for future work on attacks and defenses
in multi-agent trading systems, including stronger multi-channel attackers and
principled defenses at both architectural and prompt levels.
Acknowledgments.This research/project is supported by the National Research
Foundation, Singapore under its AI Singapore Programme (AISG Award No: AISG3-
PhD/2025-08-063).

16 Sua et al.
Disclosure of Interests.The authors have no competing interests to declare that
are relevant to the content of this article.
Data Collection and UsageReddit posts were collected from publicly available
Pushshift Reddit dumps. Twitter data were sourced from a public Kaggle dataset; we
do not redistribute tweet text and release only data as permitted.
References
1. Antweiler, W., Frank, M.Z.: Is all that talk just noise? the information content
of internet stock message boards. Journal of Finance59(3), 1259–1294 (2004).
https://doi.org/10.1111/j.1540-6261.2004.00662.x
2. Bailey, D.H., López de Prado, M.: The deflated sharpe ratio: Correcting for selec-
tion bias, backtest overfitting and non-normality. The Journal of Portfolio Man-
agement40(5), 94–107 (2014).https://doi.org/10.3905/jpm.2014.40.5.094
3. Bollen, J., Mao, H., Zeng, X.: Twitter mood predicts the stock market. Jour-
nal of Computational Science2(1), 1–8 (Mar 2011).https://doi.org/10.1016/
j.jocs.2010.12.007,https://www.sciencedirect.com/science/article/abs/
pii/S187775031100007X
4. Byrd, D.: Exploring sentiment manipulation by llm-enabled intelligent trading
agents (2025).https://doi.org/10.48550/arXiv.2502.16343,https://arxiv.
org/abs/2502.16343, arXiv:2502.16343 (v1), 2025-02-22
5. Estornell, A., Liu, Y.: Multi-llm debate: Framework, principals,
and interventions. In: Advances in Neural Information Processing
Systems. vol. 37 (2024).https://doi.org/10.52202/079017-0911,
https://proceedings.neurips.cc/paper_files/paper/2024/hash/
32e07a110c6c6acf1afbf2bf82b614ad-Abstract-Conference.html
6. Ferrara, E., Varol, O., Davis, C., Menczer, F., Flammini, A.: The rise of social bots.
Communications of the ACM59(7), 96–104 (Jul 2016).https://doi.org/10.
1145/2818717,https://cacm.acm.org/research/the-rise-of-social-bots/
7. Glasserman, P., Lin, C.: Assessing look-ahead bias in stock return predictions gen-
eratedbygptsentimentanalysis(2023).https://doi.org/10.48550/arXiv.2309.
17322
8. Gu, X., Zheng, X., Pang, T., Du, C., Liu, Q., Wang, Y., Jiang, J., Lin, M.:
Agent smith: A single image can jailbreak one million multimodal llm agents ex-
ponentially fast (2024).https://doi.org/10.48550/arXiv.2402.08567,https:
//arxiv.org/abs/2402.08567, arXiv:2402.08567 (v2), last revised 2024-06-03;
ICML 2024
9. Guo, T., Chen, X., Wang, Y., Chang, R., Pei, S., Chawla, N.V., Wiest, O., Zhang,
X.: Large language model based multi-agents: A survey of progress and challenges
(2024).https://doi.org/10.48550/arXiv.2402.01680
10. Hong, S., Zhuge, M., Chen, J., Zheng, X., Cheng, Y., Wang, J., Zhang, C., Wang,
Z., Yau, S.K.S., Lin, Z., Zhou, L., Ran, C., Xiao, L., Wu, C., Schmidhuber, J.:
MetaGPT: Meta programming for a multi-agent collaborative framework. In: The
Twelfth International Conference on Learning Representations (2024),https://
openreview.net/forum?id=VtmBAGCN7o
11. Kogan, S., Moskowitz, T.J., Niessner, M.: Social media and financial news manip-
ulation. Review of Finance27(4), 1229–1268 (2023).https://doi.org/10.1093/
rof/rfac058, published online 2022-10-21; Issue July 2023

Contagion on the Trading Floor 17
12. Lee, D., Tiwari, M.: Prompt infection: Llm-to-llm prompt injection within multi-
agent systems (2024).https://doi.org/10.48550/arXiv.2410.07283
13. Li, G., Hammoud, H., Itani, H., Khizbullin, D., Ghanem, B.: Camel: Communica-
tive agents for “mind” exploration of large language model society. In: Advances
in Neural Information Processing Systems. vol. 36, pp. 51991–52008. Cur-
ran Associates, Inc. (2023).https://doi.org/10.48550/arXiv.2303.17760,
https://proceedings.neurips.cc/paper_files/paper/2023/hash/
a3621ee907def47c1b952ade25c67698-Abstract-Conference.html
14. Li, W., Kim, H., Cucuringu, M., Ma, T.: Can llm-based financial investing strate-
gies outperform the market in long run? (2025).https://doi.org/10.48550/
arXiv.2505.07078,https://arxiv.org/abs/2505.07078
15. Liu, C., Low, A., Putnins, T.: The real impacts of public short campaigns: Evidence
from stakeholders. Journal of Corporate Finance88, 102624 (2024).https://
doi.org/10.1016/j.jcorpfin.2024.102624,https://www.sciencedirect.com/
science/article/pii/S0929119924000865, open-access version via UTS OPUS
(published version PDF).
16. Liu, Y., Deng, G., Li, Y., Wang, K., Wang, Z., Wang, X., Zhang, T., Liu, Y., Wang,
H., Zheng, Y., Zhang, L.Y., Liu, Y.: Prompt injection attack against llm-integrated
applications (2023).https://doi.org/10.48550/arXiv.2306.05499, houYi at-
tack; revised 2025-12-29 on arXiv
17. Lo, A.W.: The statistics of sharpe ratios. Financial Analysts Journal58(4), 36–52
(2002).https://doi.org/10.2469/faj.v58.n4.2453
18. Milli, S., Carroll, M., Wang, Y., Pandey, S., Zhao, S., Dragan, A.D.: Engagement,
user satisfaction, and the amplification of divisive content on social media. PNAS
Nexus4(3), pgaf062 (2025).https://doi.org/10.1093/pnasnexus/pgaf062
19. Nam, D., Skillicorn, D.B.: Detecting pump & dump stock market manipulation
from online forums. Digital Finance7(1), 1–20 (Mar 2025).https://doi.org/
10.1007/s42521-024-00121-4,https://link.springer.com/article/10.1007/
s42521-024-00121-4
20. Pohl, J., Griesbach, M., Samiei, A., de Araujo, A.: Social bots spreading dis-
information about finance: Research trends, and ethical challenges. In: Code
and Conscience: Exploring Technology, Human Rights, and Ethics in Multidis-
ciplinary AI Education. Lecture Notes in Computer Science, Springer (2024).
https://doi.org/10.1007/978-3-031-52082-2_6
21. Qian, C., Liu, W., Liu, H., Chen, N., Dang, Y., Li, J., Yang, C., Chen, W., Su,
Y., Cong, X., Xu, J., Li, D., Liu, Z., Sun, M.: ChatDev: Communicative agents for
software development. In: Ku, L.W., Martins, A., Srikumar, V. (eds.) Proceedings
of the 62nd Annual Meeting of the Association for Computational Linguistics (Vol-
ume 1: Long Papers). pp. 15174–15186. Association for Computational Linguistics,
Bangkok, Thailand (Aug 2024).https://doi.org/10.18653/v1/2024.acl-long.
810,https://aclanthology.org/2024.acl-long.810/
22. Sharpe, W.F.: Mutual fund performance. The Journal of Business39(1), 119–138
(1966).https://doi.org/10.1086/294846
23. Sprenger, T.O., Tumasjan, A., Sandner, P.G., Welpe, I.M.: Tweets and trades: The
information content of stock microblogs. European Financial Management20(5),
926–957 (2014).https://doi.org/10.1111/j.1468-036X.2013.12007.x,https:
//doi.org/10.1111/j.1468-036X.2013.12007.x
24. Su, J., Nakov, P., Cardie, C.: Corpus poisoning via approximate greedy gradient
descent. In: Findings of the Association for Computational Linguistics: ACL 2025.
pp. 4274–4294 (2025),https://aclanthology.org/2025.findings-acl.222/

18 Sua et al.
25. Tetlock, P.C.: Giving content to investor sentiment: The role of me-
dia in the stock market. The Journal of Finance62(3), 1139–1168
(2007).https://doi.org/10.1111/j.1540-6261.2007.01232.x,https://www.
columbia.edu/~pt2238/papers/Tetlock_Media_Sentiment_JF.pdf, journal arti-
cle; commonly circulated as a PDF preprint/author version.
26. Tian, F., Salim, F.D., Xue, H.: Tradinggroup: A multi-agent trading system
with self-reflection and data-synthesis (2025).https://doi.org/10.48550/arXiv.
2508.17565,https://arxiv.org/abs/2508.17565, arXiv:2508.17565 (v1), 2025-
08-25
27. Vykopal, I., Pikuliak, M., Srba, I., Moro, R., Macko, D., Bielikova, M.: Disinfor-
mation capabilities of large language models. In: Proceedings of the 62nd Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Pa-
pers). pp. 14830–14847 (2024).https://doi.org/10.18653/v1/2024.acl-long.
793,https://aclanthology.org/2024.acl-long.793/
28. Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X.,
Zhang, S., Liu, J., Awadallah, A.H., White, R.W., Burger, D., Wang, C.: Au-
togen: Enabling next-gen LLM applications via multi-agent conversation (2023).
https://doi.org/10.48550/arXiv.2308.08155,https://arxiv.org/abs/2308.
08155, arXiv:2308.08155 (v2), last revised 2023-10-03
29. Xiao, Y., Sun, E., Luo, D., Wang, W.: Tradingagents: Multi-agents llm finan-
cial trading framework (2025).https://doi.org/10.48550/arXiv.2412.20138,
https://arxiv.org/abs/2412.20138, arXiv:2412.20138 (v7), last revised 2025-06-
03
30. Xiong, F., Zhang, X., Feng, A., Sun, S., You, C.: Quantagent: Price-driven multi-
agent llms for high-frequency trading (2025).https://doi.org/10.48550/arXiv.
2509.09995,https://arxiv.org/abs/2509.09995, arXiv:2509.09995 (v3), last re-
vised 2025-09-27
31. Yang, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Li, C., Liu, D., Huang,
F., Wei, H., Lin, H., Yang, J., Tu, J., Zhang, J., Yang, J., Yang, J., Zhou, J., Lin,
J., Dang, K., Lu, K., Bao, K., Yang, K., Yu, L., Li, M., Xue, M., Zhang, P., Zhu,
Q., Men, R., Lin, R., Li, T., Tang, T., Xia, T., Ren, X., Ren, X., Fan, Y., Su, Y.,
Zhang, Y., Wan, Y., Liu, Y., Cui, Z., Zhang, Z., Qiu, Z.: Qwen2.5 technical report
(2025),https://arxiv.org/abs/2412.15115
32. Zhan, Q., Liang, Z., Ying, Z., Kang, D.: Injecagent: Benchmarking indirect prompt
injections in tool-integrated large language model agents (2024).https://doi.
org/10.48550/arXiv.2403.02691, findings of ACL 2024
33. Zhao, L., Sun, R., Jiang, Z., Yang, B., Bai, Y., Chen, M., Wang, X., Li, J.,
Bai, Z.: Contesttrade: A multi-agent trading system based on internal con-
test mechanism (2025).https://doi.org/10.48550/arXiv.2508.00554,https:
//arxiv.org/abs/2508.00554, arXiv:2508.00554 (v3), last revised 2025-08-18
34. Zou, W., Geng, R., Wang, B., Jia, J.: Poisonedrag: Knowledge corruption attacks
to retrieval-augmented generation of large language models. In: Proceedings of
the 34th USENIX Security Symposium (USENIX Security ’25). pp. 3827–3844.
USENIX Association, Seattle, WA, USA (Aug 2025),https://www.usenix.org/
conference/usenixsecurity25/presentation/zou-poisonedrag

Contagion on the Trading Floor: How Adversarial
Signals Spread in Multi-Agent Trading Systems
(Supplementary Material)
Qi Rong Sua1, Junhao Dong1,3, Nguyen Duc Thai1, Yuqing Wen2, Cheston
Tan3, and Yew-Soon Ong1,3 ()
1 Nanyang Technological University, Singapore
{suaq0001,junhao003,ducthai001,asysong}@ntu.edu.sg
2 National University of Singapore, Singapore
e1351400@u.nus.edu
3 Centre for Frontier AI Research, IHPC, A*STAR, Singapore
cheston_tan@a-star.edu.sg
Abstract.This supplementary material complements the main paper
in two ways. First, it gives the full proof of Theorem 1 (Expressivity of
GMATS), showing that any multi-agent trading pipeline satisfying typed
message passing, point-in-time (PIT) discipline, and stage separation can
be simulated by a GMATS instance that produces the same executed-
order sequence under matched randomness. Second, it gives a concrete
compilation recipe for mapping modern agentic trading frameworks into
GMATS by aligning their ingestion, fusion, risk, and execution compo-
nents with theA→C→K→Xpipeline and unrolling internal debate,
contest, and reflection steps into micro-rounds ofΣ. We also retain an
additionalTradingAgentsbaseline under the Always Negative attacker.
All empirical entries are averaged over 5 runs and reported as attack–
clean deltas.
1 Proof of Theorem 1
Proof (Proof of Theorem 1).LetMbe a multi-agent trading pipeline satisfy-
ing the three assumptions in Theorem 1. Fix the asset universe, the PIT data
stream, an initial environment stateχ1, and a source of randomnessω. We view
every stochastic call inM, including LLM sampling and any stochastic sched-
uler choice, as consuming a contiguous segment ofω. The goal is to construct a
GMATS instance
G= (A, A, C, K, X,S, Σ,D,L, Λ,E)
that, under the sameχ1 andω, executes exactly the same order at every decision
time.
Operational View ofM.At the start of roundt, write the state ofMas
sM t = (χt,Hist t,h t, πt),

2 Sua et al.
whereχ t is the environment state,Histt is the ordered message log,ht collects
all private module states and memories, andπt is the current pointer intoω.
Each message has the form
m= (id,src,dst, τ,payload,ts), τ∈ S M,
whereS M is finite by typed message passing. Let
Vist(Hist) ={m∈Hist:m.ts≤t}
denote the PIT-visible sub-log, preserving the bus order inherited fromHist. The
PIT assumption says that every activation at roundtis a function only of its
PIT-visible inbox, PIT dataDt, the relevant component state, and the next ran-
dom tape segment. The stage-separation assumption says that each terminated
round is organized into evidence ingestion, fusion/scoring, risk/constraints, and
execution phases. Any finite internal debate, reflection, contest, or tool-call se-
quence inside a phase is treated as a sequence of micro-steps. If the original
implementation uses adaptive branching, the branch rule is included in the ac-
tivated component; inactive branches emit no messages and consume no ran-
domness. Equivalently, one may use a finite super-schedule that calls all possible
phase components in a fixed order, with no-ops on branches not taken.
Construction ofG.We define the GMATS instance as follows. Set the asset
universeA, data streamD={D t}t∈T, and execution environmentEequal to
those ofM. Set the message schema to
S=S M ∪ {Stance,DraftOrder,ApprovedOrder},
where the three extra types are wrappers used only whenM’s native artifacts do
not already distinguish stances, draft orders, and approved orders. The payloads
of all native messages are preserved verbatim; the wrappers do not alter the
information available to any agent.
LetUbe the set of components ofM. For each componentu∈ Uand
each phaseϕ∈ {ingest,fuse,risk,exec}in whichuparticipates, create a phase-
restricted GMATS componentuϕ. The transition function ofuϕ is exactly the
transition function used byuin phaseϕofM: on the same PIT-visible inbox,
PIT data, private state, and random tape segment, it appends the same mes-
sages, produces the same local outputs, and updates the same private state. Ifu
spans several phases, the corresponding phase-restricted components share the
same private state cell, so splittinguacross stages does not change its mem-
ory. Fresh message identifiers, counters, and tool-call caches are included in this
private state or inω.
Assign the phase-restricted components to GMATS stages by
A={u ingest}, C={u fuse}, K={u risk}, X={u exec}.
IfMhas no separate risk or execution module, the corresponding set is empty
and the adjacent stage emits the final order, as allowed by GMATS. DefineΣ

Contagion on the Trading Floor: Supplementary Material 3
to activate these components in the same within-round order asM’s phases and
micro-steps, using the same random tape offsets. Finally, defineLt andΛ t as the
aggregate input–output maps induced by the coordinator and controller micro-
steps scheduled at roundt. Thus GMATS exposes the same staged interface as
Definition 1 while preserving the original component-level behavior.
Correctness Invariant.Let
sG t = (χG t ,Hist G t ,h G t , πG t )
betheanalogousGMATSstate.Weprove,byinductionoverrounds,thestronger
invariant
I(t) : χM t =χ G t ,Hist M t =Hist G t as ordered logs,
hM t =h G t , π M t =π G t .
This implies equality of PIT-visible inboxes for every component at roundt.
Base Case.Att= 1, the two systems have the same initial environment state,
the same initial log (typically empty), the same component states by construc-
tion, and the same random-tape pointer. ThereforeI(1)holds.
Inductive Step.AssumeI(t)holds. Consider the micro-steps of roundtin
their scheduled order. Before the first micro-step, all PIT-visible inboxes, PIT
data, private states, and random-tape positions agree. Suppose they agree be-
fore some micro-step. The activated component ofMand the corresponding
phase-restricted component ofGthen apply the same transition function to the
same inputs and the same random tape segment. They therefore append the
same sequence of messages to the bus, update the same private states, produce
the same local output, and advance the random pointer by the same amount.
Thus equality is preserved after that micro-step. A nested induction over all
micro-steps in the round gives equality of the full ordered logs, private states,
and random pointers at the end of the fusion and risk phases. In particular, both
systems obtain the same approved ordero′ t or the same no-trade decision.
The execution environments are identical and are called with the same input
state and order, hence
(fillst, χt+1) =E(o ′ t, χt)
produces the same fills and next environment state in both systems. Messages
with future timestamps, if any, have also been appended identically, so the full
ordered logs remain equal and the PIT-visible logs will agree at the next round.
ConsequentlyI(t+ 1)holds.
Conclusion.By induction,I(t)holds for every round. Therefore the order sub-
mitted to the execution environment is identical at every decision time. The
GMATS instanceGthus produces the same executed-order sequence asMun-
der the same initial state and randomness.

4 Sua et al.
Algorithm 1Compile a staged multi-agent pipeline into GMATS
1:Input:PipelineMwith agents/modulesU, PIT data{D t}, environmentE, and
within-round micro-scheduleΣ M.
2:Output:GMATS instanceGwith identical executed-order sequence under
matched randomness.
3: SetA,{D t}, andEto matchM.
4: Define a finite schemaSby wrapping each artifact class inM(reports, debate
turns, candidate orders, risk checks) as a typed message; optionally addStance,
DraftOrder,ApprovedOrder.
5: Partition computations into phases (i)–(iv) and create phase-restricted agentsuϕ
for eachu∈ Uand phaseϕ.
6: Assignu (i) toA,u (ii) toC,u (iii) toK, andu (iv) toX; use an empty stage when
the original pipeline has no separate module.
7: DefineΣby unrollingΣ M each round; debates, contests, and reflection become
micro-rounds insideA,C,K, orX.
8: DefineL t andΛ t as the maps induced by running the coordinator and controller
micro-rounds underΣ.
9:returnG.
2 Compiling Modern Agentic Trading Frameworks into
GMATS
This section expands Corollary 1 from the main paper by giving a concrete
compilationprocedure from representative multi-agent trading frameworks into
a GMATS instance. The key idea is that most modern LLM trading systems
already implement a firm-like pipeline: (i) evidence ingestion, (ii) multi-signal
fusion and scoring, (iii) risk/constraints checks, and (iv) execution. GMATS
makes this structure explicit via theA→C→K→Xstaging and a schedule
Σthat unrolls internal debates, contests, and reflections as micro-rounds.
2.1 A Generic Compilation Recipe
LetMbe any multi-agent pipeline satisfying Theorem 1. AGMATS compiler
produces a tupleG= (A, A, C, K, X,S, Σ,D,L, Λ,E)as follows.
Typed Message Passing.Many agentic frameworks use free-form natural-
language artifacts internally, such as chat logs, debate turns, or reflective notes.
GMATS requires only a finite schema, so compilation can introduce lightweight
wrappers such asFundReport,BearArg,RiskCheck, andCandidate-
Orderwhile preserving payloads verbatim. This does not change behavior as
long as the routing and inbox functions respect the wrapper types.
PIT Discipline.The GMATS instance inherits PIT discipline from the evalu-
ation harness. At roundt, the compiler provides onlyD t and messages with
timestamps at mosttto all agents. If the original framework has asynchronous
tool calls, the compiler treats tool outputs as environment data with explicit
timestamps and delays delivery until the appropriate round.

Contagion on the Trading Floor: Supplementary Material 5
2.2 Case Study: TradingAgents⇒GMATS
TradingAgents [3] is organized as a trading-firm simulation with (i) an Ana-
lyst Team (fundamental, sentiment, news, technical), (ii) a Researcher Team
with bull and bear researchers that debate the analyst outputs, (iii) a Trader
Agent that synthesizes a transaction proposal, and (iv) a risk-management and
portfolio-manager gate that approves or rejects before simulated execution.
A semantics-preserving mapping into GMATS is:
–A: {Fundamentals Analyst, Sentiment Analyst, News Analyst, Technical An-
alyst} emitting typed insight messages, one per role per round.
–C: {Bull Researcher, Bear Researcher, Trader}. The bull/bear debate is un-
rolled as micro-rounds inΣproducing debate-turn messages; the Trader
consumes the final debate state and emits aDraftOrderor stance vector.
–K: {Risk Management Team, Portfolio Manager}. This stage producesAp-
provedOrderor a reject decision; limits such as exposure, leverage, and
liquidity live inΛt.
–X: the simulated exchange/execution module submittingo′ t toEand logging
fills.
2.3 Case Study: TradingGroup⇒GMATS
TradingGroup [2] consists of specialized signal agents, including news sentiment,
financial-report interpretation, trend forecasting, and style adaptation, plus a
decision agent that merges signals. It also includes self-reflection and a dynamic
risk model with stop-loss/take-profit logic.
A GMATS mapping is:
–A: {Sentiment, Report, Trend, Style} agents emitting typed signals.
–C: a decision-making coordinator that fuses signals into a stance or order.
Self-reflection is compiled into coordinator micro-rounds that write/read a
memory state, still under PIT because memory is generated only from past
rounds.
–K: the dynamic risk-management module enforcing stop-loss/take-profit and
exposure caps asΛt.
–X: the execution interface submitting approved orders toE.
2.4 Other Examples: ContestTrade and QuantAgent
ContestTrade [5] decomposes into a Data Team that compresses raw data into
text factors and a Research Team that proposes candidate decisions. Its internal
contest mechanism can be compiled as coordinator micro-rounds that score and
select candidate orders before risk checks.
QuantAgent [4] decomposes signal extraction into specialized technical
agents, such as Indicator, Pattern, and Trend agents, with a Risk agent. These
map naturally to analyst and controller roles, with a coordinator that fuses
the technical messages into a final stance or order. In both cases, the con-
test/reflection logic is represented as micro-rounds inΣand does not require
any extension to GMATS beyond typed messages and scheduling.

6 Sua et al.
T able 1.Example mappings from agentic frameworks to GMATS stages.
Framework Analysts (A) Coordinators (C) Controllers/Exec
(K/X)
TradingAgents role analysts bull/bear debate, trader risk/PM, exchange
TradingGroup signal agents decision + reflection dynamic risk,
executor
ContestTrade data team research contest risk gate, executor
QuantAgent indicator, pattern,
trend
fusion decision risk, executor
3 Additional Experiment Results: TradingAgents
Baseline
ThissectionreportsanadditionalAlwaysNegativeattackerresultfortheTradin-
gAgents[3] baseline. The protocol is the same attack–clean protocol used in the
main paper. All entries are averaged over 5 runs and are reported as attack
minus clean. As in the main paper, we emphasize deltas rather than absolute
Sharpe levels, since Sharpe can be unstable over short horizons [1].
T able 2.TradingAgentsbaseline under the Always Negative attacker. Entries are
attack–clean deltas averaged over 5 runs.
Metric15% 30% 45% 60% 75%
BSSanalyst −0.788−1.048−1.261−1.243−1.369
BSSbull −0.309−0.302−0.279−0.293−0.250
BSSbear −0.019−0.032−0.029−0.028−0.025
BSSfuse −0.247−0.241−0.193−0.210−0.152
∆CR−0.021−0.020−0.021−0.021−0.017
∆Sharpe+7.764 +5.004 +1.226 +2.018 +1.942
∆Vol−0.030−0.022−0.020−0.019−0.015
TradingAgents exhibits the same directional social contagion observed in
GMATS. The analyst belief shift grows in magnitude with poisoning: BSSanalyst
decreases from−0.788at15%poisoning to−1.369at75%poisoning. However,
contagion is damped downstream. The fused belief shift remains modest and
becomes less negative at higher poisoning, moving from BSSfuse =−0.247at
15%to BSS fuse =−0.152at75%. This is consistent with partial cancellation
or regularization at the coordinator stage rather than full propagation of the
contaminated social signal.
On performance, TradingAgents becomes more conservative under attack:
∆Vol is consistently negative, while∆CR is mildly negative. Over this short
window, lower realized volatility can mechanically yield positive∆Sharpe even

Contagion on the Trading Floor: Supplementary Material 7
when return deltas are slightly negative. Accordingly, we interpret this baseline
as risk-damping under attack rather than as evidence that poisoning improves
profitability.
Acknowledgments.This research/project is supported by the National Research
Foundation, Singapore under its AI Singapore Programme (AISG Award No: AISG3-
PhD/2025-08-063).
Disclosure of Interests.The authors have no competing interests to declare that
are relevant to the content of this article.
Generative AI Assistance Disclosure.Weusedalargelanguagemodelasawriting
aid to improve readability (e.g., grammar, spelling, and wording suggestions). The
model was not used to generate new scientific content, results, proofs, or experimental
data, nor to make decisions about the research contributions. All text was reviewed
and edited by the authors, who take full responsibility for the final manuscript and for
ensuring compliance with applicable research integrity and copyright requirements.
References
1. Lo, A.W.: The statistics of sharpe ratios. Financial Analysts Journal58(4), 36–52
(2002).https://doi.org/10.2469/faj.v58.n4.2453
2. Tian, F., Salim, F.D., Xue, H.: Tradinggroup: A multi-agent trading system with
self-reflection and data-synthesis (2025).https://doi.org/10.48550/arXiv.2508.
17565,https://arxiv.org/abs/2508.17565, arXiv:2508.17565 (v1), 2025-08-25
3. Xiao, Y., Sun, E., Luo, D., Wang, W.: Tradingagents: Multi-agents llm financial
trading framework (2025).https://doi.org/10.48550/arXiv.2412.20138,https:
//arxiv.org/abs/2412.20138, arXiv:2412.20138 (v7), last revised 2025-06-03
4. Xiong, F., Zhang, X., Feng, A., Sun, S., You, C.: Quantagent: Price-driven multi-
agent llms for high-frequency trading (2025).https://doi.org/10.48550/arXiv.
2509.09995,https://arxiv.org/abs/2509.09995, arXiv:2509.09995 (v3), last re-
vised 2025-09-27
5. Zhao, L., Sun, R., Jiang, Z., Yang, B., Bai, Y., Chen, M., Wang, X., Li, J., Bai, Z.:
Contesttrade: A multi-agent trading system based on internal contest mechanism
(2025).https://doi.org/10.48550/arXiv.2508.00554,https://arxiv.org/abs/
2508.00554, arXiv:2508.00554 (v3), last revised 2025-08-18
