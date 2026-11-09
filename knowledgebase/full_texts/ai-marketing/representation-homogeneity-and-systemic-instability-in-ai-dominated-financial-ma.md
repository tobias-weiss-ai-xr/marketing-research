---
title: 'Representation Homogeneity and Systemic Instability in AI-Dominated Financial Markets: A Structural
  Approach'
url: https://arxiv.org/abs/2604.22818
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Yimeng Qiu
- Qiwei Han
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.22818
pages: 21
chars: 55981
fetched_at: '2026-11-08T13:01:23+00:00'
kb_version: 1
---

# Representation Homogeneity and Systemic Instability in AI-Dominated Financial Markets: A Structural Approach

Representation Homogeneity and Systemic Instability in
AI-Dominated Financial Markets: A Structural Approach
Yimeng Qiu, Qiwei Han
Draft Version
Abstract
This paper investigates how similarity in the informational representation of market states
among Artificial Intelligence (AI) trading agents can generate systemic instability in financial
markets. We construct a structural multi-agent market model calibrated using high-frequency
microstructural moments. AI agents are modeled through a two-layer decision architecture con-
sisting of a nonlinear representation layer and an adaptive linear readout layer. The representa-
tion layer maps raw market states into high-dimensional feature vectors, while the readout layer
generates return forecasts that feed into a risk-controlled trading rule. This representation-based
microfoundation separates two objects that are often conflated in the literature:representation
homogeneity—the degree to which agents encode market states into similar feature spaces—
andforecast overlap—the degree to which agents produce similar return predictions. We show
theoretically that these two concepts are related but not equivalent, and that representation
homogeneity can compress the effective space of forecast disagreement under stress even when
predictions appear diverse in normal times. Through controlled factorial experiments that vary
representation homogeneity while conditioning on alternative risk-aversion and learning-rate
distributions, we hypothesize that increasing representation similarity amplifies synchronization
in beliefs and positions, leading to volatility clustering, liquidity stress, and elevated tail risk.
Our structural mechanisms suggest that low perceived volatility regimes can endogenously ac-
cumulate hidden leverage through position stickiness, which subsequently collapses when shocks
trigger synchronized deleveraging. The results provide a structural foundation for macropru-
dential policies aimed at monitoring and preserving diversity in how AI systems represent and
process market information.
1 Introduction
The rapid expansion of algorithmic trading and AI-driven financial decision systems has raised
growing regulatory concerns about “model monoculture risk” within financial infrastructures, par-
ticularly as firms converge on shared foundation models and common feature-extraction pipelines.
Evidence indicates that highly synchronized algorithmic behavior can amplify market volatility and
flash crashes.
This paper asks whether similarity in how AI agentsrepresentmarket states—as distinct from
similarity in their realized predictions—increases systemic fragility in financial markets. More
specifically, can representation homogeneity compress the effective space of forecast disagreement
under stress, even when agents appear diverse in normal times?
To answer these questions, this paper develops a structural multi-agent framework that com-
bines a representation-based AI microfoundation with a tractable reduced-form trading rule. The
objective is not to replicate every engineering detail of deployed AI systems, but to construct a
class of agents that is sufficiently rich to capture meaningful differences in information encoding
1
arXiv:2604.22818v1  [q-fin.TR]  14 Apr 2026

while remaining sufficiently comparable to quantify representation overlap across agents. This
makes it possible to study how structural similarity in the feature space through which agents
interpret market states propagates into synchronized beliefs, correlated positions, and aggregate
market instability.
A central contribution of the paper is the formal separation ofrepresentation homogeneityfrom
forecast overlap. Two agents may produce similar return forecasts for transient reasons—correlated
noise, similar recent experience—without sharing a common feature space. Conversely, agents that
encode market states through similar representations are structurally predisposed to emphasize
the same signals, neglect the same signals, and commit similar forecast errors, especially under
stress. We formalize this distinction using function-space distances and show that representation
convergence can compress the bound on forecast disagreement even when readout parameters differ.
The experimental design is structured to test this specific claim: by constructing agent populations
that are matched on forecast overlap but differ in representation distance, we can isolate the
independent contribution of representation homogeneity to systemic fragility.
Risk-aversion heterogeneity and learning-rate heterogeneity enter the framework as static, agent-
specific parameters whose cross-sectional distributions are varied as control dimensions in a factorial
design. This allows us to verify that observed representation effects are robust to variation in
downstream decision-making characteristics, without treating these dimensions as co-equal objects
of investigation.
2 Conceptual Framework
The objective of the framework is to studyrepresentation homogeneityas a structural object,
rather than to classify traders into coarse strategy types. In heterogeneous-agent finance, aggregate
outcomes depend not only on average behavior but also on the extent to which individual decision
rules overlap [Tesfatsion, 2002, Brock and Hommes, 1998, Hommes, 2006, LeBaron, 2006]. This
perspective is especially relevant in AI-mediated trading environments, where agents may differ in
parameters while remaining highly similar in how they encode market states.
We represent agentias a two-stage decision system,
Agenti = (fi, gi),(1)
wheref i maps the observable market state into a return forecast andg i maps that forecast into a
portfolio decision. Let
St ∈ S ⊆RKs
denote the publicly observable market state at timet. The state vector may include prices, returns,
order-flow statistics, volatility measures, and other variables available prior to trading.
Agenti’s forecast of the next-period return is written abstractly as
ˆri,t =f i(St),(2)
and the resulting portfolio decision is
Di,t =g i(ˆri,t, σt, Di,t−1),(3)
whereσ t denotes the volatility signal entering the trading rule andD i,t−1 is the inherited posi-
tion. This notation is deliberately general. It accommodates statistical forecasting rules, machine-
learning predictors, and adaptive trading heuristics while preserving a common decision architecture
[Arthur, 1994, Brock and Hommes, 1998, LeBaron, 2006].
2

Our interest, however, is not in this abstract decomposition itself, but in the structural layers
through which homogeneity can arise. In the model developed below, agenti’s forecasting rule is
represented as
fi(S) =θ ⊤ i hi(S), h i(S) =ϕ(W iS),
whereh i :S →RK is the representation map,W i is the representation matrix,ϕ(·) is an elementwise
activation function, andθ i is the readout vector.
This decomposition separates three distinct objects. Therepresentation layergoverns how
raw market states are encoded into features. Theforecast layergoverns how encoded features are
mapped into return expectations. Therisk-control layergoverns how those forecasts are trans-
lated into positions through risk tolerance, leverage limits, and adjustment frictions. Although all
three layers can in principle contribute to agent similarity, the central premise of the paper is that
upstreamsimilarity in representation is qualitatively different from, and potentially more destabi-
lizing than, downstream similarity in forecasts or risk parameters. This is because representation
homogeneity creates structural overlap in how agentsperceivemarket states, which can remain
latent during normal times but become acutely consequential under stress.
This distinction is economically important because parameter similarity is not, by itself, a
meaningful measure of overlap. Neural representations are not uniquely identified at the parameter
level. Two agents may have different matricesWi andW j while generating similar feature maps over
economically relevant states, and conversely, numerically similar parameter matrices may induce
materially different encodings under nonlinear activation. For this reason, homogeneity is measured
primarily in function space rather than raw parameter space.
2.1 Structural Measures of Homogeneity
We begin with the representation layer. For agentsiandj, define the pairwise representation
distance as theL 2(µ) distance between their feature maps:
drepr(i, j) =
Z
S
∥hi(S)−h j(S)∥2 2 dµ(S)
1/2
.(4)
Hereµis a reference distribution over economically relevant market states. This distance measures
whether two agents encode the same market state into similar feature vectors.
At the forecast layer, define
dforecast(i, j) =
Z
S

fi(S)−f j(S)
2 dµ(S) 1/2 .(5)
This object compares prediction rules directly. Two agents may generate similar forecasts even when
their internal representations differ, and similar representations do not imply identical forecasts
when readout vectors differ. Distinguishingd repr fromd forecast is therefore essential for separating
structural overlap in information processing from overlap in realized predictions.
At the risk-control layer, letϖ i ∈R KR denote the vector of parameters governing agenti’s
position-sizing rule, including, for example, risk aversion, leverage limits, and adjustment frictions.
We define the pairwise risk-control distance as
drisk(i, j) =∥ϖi −ϖ j∥W ,(6)
where∥ · ∥W is a weighted norm chosen so that the resulting distances are comparable across
components.
3

These three objects are the primitive measures used throughout the paper. When a scalar
summary is useful, we define the composite distance
D(i, j) =w1drepr(i, j) +w2dforecast(i, j) +w3drisk(i, j),(7)
wherew 1, w2, w3 ≥0 andw 1 +w 2 +w 3 = 1. The associated homogeneity index is
H(i, j) = 1− D(i, j),(8)
and average market homogeneity is
H= 2 N(N−1) X 1≤i<j≤N H(i, j).(9)
In the analysis below, the weightsw 1, w2, w3 are treated as normative baseline settings for compara-
tive statics and robustness checks rather than as structurally estimated parameters. The composite
indexH(i, j) is used as a summary statistic, not as a substitute for the layer-specific distances.
2.2 Operational Choice of the Reference Distribution
The distances in (4) and (5) depend on the reference distributionµ. Operationally, three choices
are useful.
A first approach uses the empirical distribution of realized states{S t}T t=1 observed during cali-
bration or simulation:
drepr(i, j) =

1
T
TX
t=1
∥ϕ(WiSt)−ϕ(W jSt)∥2 2
!1/2
.(10)
This evaluates similarity over the region of the state space actually visited by the market, but it
may underweight rare stress states.
A second approach evaluates distances over a predetermined benchmark grid
SM ={S (1), . . . , S(M) },
yielding
drepr(i, j) =

1
M
MX
m=1
∥ϕ(WiS(m))−ϕ(W jS(m))∥2 2
!1/2
.(11)
This allows explicit coverage of extreme states, but requires choosing a grid that is economically
meaningful.
A third approach uses a weighted reference measureµ=ω(S)µ 0(S), whereω(S) places greater
mass on states of particular interest, such as stress regimes:
drepr(i, j) =
Z
S
∥hi(S)−h j(S)∥2 2 ω(S)dµ 0(S)
1/2
.(12)
This formulation is especially useful when the object of interest is not average similarity over normal
times but overlap under tail conditions. In the analysis below, the choice ofµis treated as part of
the measurement design rather than as a primitive feature of the model.
4

2.3 Why Representation and Forecast Homogeneity Are Distinct
Representation similarity and forecast similarity are related, but they are not equivalent. Under
mild regularity conditions, one can bound the second object using the first without collapsing the
two concepts.
Assume thatϕ(·) is Lipschitz continuous, that∥θ i∥ ≤Bθ, and that the relevant state space is
bounded. Then for any stateS,
|fi(S)−f j(S)|=|θ ⊤ i hi(S)−θ ⊤ j hj(S)|(13)
≤ ∥θi −θ j∥ ∥hi(S)∥+∥θ j∥ ∥hi(S)−h j(S)∥.(14)
Integrating with respect toµyields
dforecast(i, j)≤C 1∥θi −θ j∥+C 2drepr(i, j),(15)
for constantsC 1, C2 >0 determined by norm bounds and the choice ofµ. Equation (15) shows
that representation convergence can compress forecast heterogeneity, but it does not eliminate the
role of readout heterogeneity.
Importantly,d forecast(i, j) is an integrated distance defined over the full reference measureµ,
whereas the theoretical results developed below focus on the state-conditional cross-sectional dis-
agreementV f (S). This distinction is important: the former summarizes average overlap across
states, while the latter isolates how representation convergence may contract the effective space of
disagreement in economically important states, especially under stress.
3 Model
To study how representation homogeneity propagates into market-wide instability, we construct
a discrete-time multi-agent market with four linked components: (i) a reduced-form pricing block
with inventory-sensitive liquidity provision, (ii) a representation-based forecasting architecture, (iii)
a risk-controlled portfolio choice rule, and (iv) an adaptive learning rule with an explicit prediction
target and internally consistent timing.
Time is indexed byt= 0,1,2, . . .. Each period follows the sequence
state observation→forecast formation→portfolio choice→price formation→learning update.
This timing implies that agents form forecasts using information available at timet, choose positions
within periodt, and update their forecasting rules only after the next-period realization becomes
observable.
3.1 State Variables and Market Timeline
Let
St ∈ S ⊆RKs
denote the observable market state at the beginning of periodt. The state vector may include lagged
returns, prices, realized volatility measures, and order-flow statistics. Crucially,S t is measurable
with respect to the information set available before agents choose their period-ttrades.
A single period unfolds in five steps. First, agents observe the public stateS t. Second, each
agent mapsS t into features and forms a forecast of the next-period return. Third, agents choose
their period-tpositionsD i,t, thereby generating order flow. Fourth, a reduced-form market maker
5

absorbs aggregate order flow and sets the end-of-period priceP t. Fifth, after the subsequent return
realization is observed, agents update their forecasting readouts using the realized prediction error.
A forecast formed at timetis therefore evaluated against the realized return fromttot+ 1, not
against a contemporaneous return already embedded inS t.
3.2 Price Dynamics and Inventory-Sensitive Liquidity Provision
We model a single risky asset traded against a reduced-form, risk-averse market maker. LetD i,t
denote agenti’s position at the end of periodt, and define the agent’s order flow as
∆Di,t =D i,t −D i,t−1.(16)
Aggregate net order flow in periodtis
∆Qt =
NX
i=1
∆Di,t.(17)
To eliminate mechanical predictability from fundamentals, we assume that the asset’s funda-
mental value follows a random walk:
Ft =F t−1 +ϵ t, ϵ t ∼ N(0, σ2 ϵ ).(18)
LetI t denote the market maker’s inventory after absorbing period-torder flow:
It =I t−1 −∆Q t.(19)
The end-of-period transaction price is
Pt =F t +λ t∆Qt −ψ tIt,(20)
whereλ t is a temporary order-flow impact coefficient andψ t is an inventory-holding premium.
To capture endogenous liquidity withdrawal under stress while preserving boundedness, we let
both coefficients depend nonlinearly on lagged dealer inventory:
λt =λ 0

1 + αλI 2 t−1
1 +β λI 2 t−1

,(21)
ψt =ψ 0

1 + αψI 2 t−1
1 +β ψI 2 t−1

.(22)
Here,λ 0, ψ0 >0 are baseline liquidity-friction parameters,α λ, αψ >0 govern stress amplification,
andβ λ, βψ >0 ensure bounded responses.
The realized return fromttot+ 1 is
rt+1 =P t+1 −P t.(23)
Substituting (18)–(20) and using (19) yields
rt+1 =ϵ t+1 + (λt+1 +ψ t+1)∆Qt+1 −λ t∆Qt −(ψ t+1 −ψ t)It.(24)
Equation (24) shows that next-period returns combine exogenous news, current order-flow pressure,
lagged impact reversal, and inventory revaluation induced by time-varying dealer stress.
6

3.3 Representation-Based Forecasting Architecture
At the beginning of periodt, agentiobservesS t and transforms it into aK-dimensional feature
vector:
Xi,t =ϕ(W i,tSt),(25)
whereW i,t ∈R K×Ks is the agent’s representation matrix andϕ(·) is an elementwise nonlinear
activation function.
Conditional on this representation, the agent forms a forecast of the next-period return:
ˆri,t =θ ⊤ i,tXi,t,(26)
whereθ i,t ∈R K is the readout vector. By construction, ˆr i,t is a forecast forr t+1, not for a
contemporaneous realized return.
3.4 Perceived Trading Frictions and Local Slippage Estimation
Agents do not observe the market maker’s true impact coefficientλ t, aggregate order flow ∆Q t, or
inventoryI t. Instead, each agent maintains a local estimate of execution frictions based on its own
realized trading experience.
We model agenti’s perceived impact coefficient as an exponentially weighted moving average
of realized slippage, conceptually related to an Amihud-style local illiquidity proxy:
ˆλi,t = (1−ρ) ˆλi,t−1 +ρ

 rt max{|∆Di,t−1|, ε}

 , ρ∈(0,1), ε >0.(27)
The regularization constantεprevents the estimator from exploding when an agent submits negli-
gible volume. This object is interpreted as a reduced-form local slippage indicator rather than as
a consistent estimate of the true aggregate impact coefficient.
Because the forecast ˆri,t is used to guide a position change ∆D i,t, the agent evaluates forecast
performance using an execution-adjusted next-period return:
˜ri,t+1 =r t+1 − ˆλi,t |∆Di,t|.(28)
This target penalizes aggressive turnover under perceived illiquidity and prevents the agent from
mechanically attributing all realized returns to predictive success.
3.5 Risk-Controlled Portfolio Choice
After forming the forecast ˆri,t, agentichooses its period-tpositionD i,t. To capture the interaction
between expected returns, risk control, and adjustment frictions, we assume that the agent solves
Ui,t =D i,tˆri,t − γi 2 ˆσ2 t D2 i,t − κ+ ˆλi,t 2 (Di,t −D i,t−1)2,(29)
whereγ i >0 is a static, agent-specific risk aversion parameter,κ >0 is a baseline position-
adjustment friction, and ˆλi,t is the local slippage estimate defined in (27).
The volatility signal entering the objective is endogenous and updated from realized returns
using a centered exponential moving average:
ˆµt = (1−β)ˆµt−1 +βr t,(30)
ˆσ2 t = (1−β)ˆσ2 t−1 +β(r t −ˆµt)2,(31)
7

withβ∈(0,1). This specification allows prolonged smooth price trends to compress perceived risk
even while positions are gradually accumulating.
The first-order condition for (29) yields the unconstrained target position:
D∗ i,t = ˆri,t + (κ+ ˆλi,t)Di,t−1
γiˆσ2 t +κ+ ˆλi,t .(32)
Equation (32) is a partial-adjustment portfolio rule. The numerator captures both directional
conviction and position persistence, while the denominator scales responsiveness by perceived risk
and trading frictions.
Imposing a hard capital or leverage limit ¯Di >0, the actual position is
Di,t = sgn(D∗ i,t) min  |D∗ i,t|, ¯Di 	 .(33)
3.6 Learning Dynamics and Representation Drift
We assume that the representation matrixW i,t evolves slowly relative to the high-frequency trading
horizon, so that within a short execution window the primary adaptive margin is the readout vector
θi,t. Learning therefore takes the form of stochastic gradient descent on squared prediction error
using the execution-adjusted target ˜ri,t+1.
Afterr t+1 is realized, agentiupdates its readout according to
θi,t+1 =θ i,t +η θ,i

˜ri,t+1 −ˆri,t

Xi,t,(34)
whereη θ,i >0 is the agent’s fixed learning rate. Substituting (28), the update can equivalently be
written as
θi,t+1 =θ i,t +η θ,i

rt+1 − ˆλi,t|∆Di,t| −ˆri,t

Xi,t.(35)
This timing is internally consistent:X i,t and ˆri,t are computed from information available at time
t, ∆D i,t is the trade implied by that forecast,r t+1 is the realized next-period outcome, and the
forecast error is evaluated only after the outcome becomes observable.
To capture gradual convergence in the underlying feature space, we allow individual represen-
tation matrices to evolve according to a matrix-valued Ornstein–Uhlenbeck process:
dWi,t =ν W

Wbase,t −W i,t

dt+σ W dBW i,t ,(36)
whereν W >0 governs the speed of convergence toward a common benchmark representation,σ W >
0 governs idiosyncratic exploratory drift, andW base,t denotes a shared foundation representation
following a common external updating process. This component allows the model to capture the
slow-moving process by which firms adopt common AI infrastructure, while the readout layer adapts
at high frequency to realized market conditions.
Note that the risk-aversion parameterγ i and the learning rateη θ,i are both static and agent-
specific: they are drawn from cross-sectional distributions at initialization and remain fixed through-
out the simulation. The only dynamic convergence mechanism in the model operates at the rep-
resentation level through (36). This design choice reflects the empirical observation that the most
consequential source of structural convergence in AI-driven finance is the adoption of common
foundation models and shared feature-extraction pipelines, rather than the standardization of risk
preferences or learning algorithms per se.
8

4 Structural Calibration via Simulated Method of Moments
To avoid arbitrary parameterization of the market microstructure, we calibrate the baseline pricing
and liquidity parameters using the Simulated Method of Moments (SMM) [Duffie and Singleton, 1993].
The calibration targets the reduced-form pricing block—specifically, the liquidity provision mech-
anism and fundamental volatility—rather than the agent-level decision parameters.
The structural parameter vector entering the SMM is
Θ ={λ 0, αλ, βλ, ψ0, αψ, βψ, κ, σϵ}.
This vector governs the market maker’s pricing rule, the nonlinear liquidity response, and the scale
of exogenous fundamental innovation.
Agent-level parameters—specifically, the risk-aversion distributionγ i ∼LogNormal(µ γ, σγ) and
the learning-rate distributionη θ,i ∼LogNormal(µ η, ση)—are treated as exogenous background het-
erogeneity. Their distributional parameters (µ γ, σγ) and (µ η, ση) are set to empirically reasonable
values drawn from existing literature on institutional trading behavior and held fixed during cal-
ibration. These distributions are subsequently varied in the experimental design (Section 5) as
control dimensions, not as calibration targets. In the baseline calibration, both distributions are
set to moderate heterogeneity levels; sensitivity to alternative baseline means is assessed in the
robustness analysis.
To improve identification of the nonlinear fragility parameters (α) and the capacity saturation
parameters (β), we expand the SMM target vector to include conditional tail moments at multiple
volatility thresholds.
Table 1: SMM Target Moments and Identification Strategy
T arget Empirical Moment Primary Structural Role
Annualized Volatility Exogenous fundamental risk (σ ϵ)
Unconditional Price Impact Baseline temporary impact (λ 0)
Conditional T ail Price Impact (T op 5% V ol) Liquidity fragility parameter (αλ)
Extreme T ail Price Impact (T op 1% V ol) Liquidity capacity saturation (β λ)
Return Autocorrelation (Lag 1) Baseline inventory premium (ψ 0)
Conditional T ail Return Autocorrelation (T op 5%) Inventory fragility parameter (αψ)
Extreme T ail Return Autocorrelation (T op 1%) Inventory capacity saturation (βψ)
Order Flow Autocorrelation (Lag 1) Adjustment friction / Stickiness (κ)
The calibration proceeds in two stages. In the first stage, a global search over the parameter
space identifies candidate regions using Sobol quasi-random sequences. In the second stage, local
optimization from the best candidates refines the estimates. Bootstrap resampling of the empirical
moments provides confidence intervals. The calibrated baseline market serves as the common
environment for all subsequent experiments: comparative statics on representation homogeneity
are conducted on top of this calibrated pricing block.
5 Experimental Design: Identification of Representation Homo-
geneity Effects
The experimental design is structured to answer a specific identification question:does repre-
sentation homogeneity increase systemic fragility, and does this effect persist after controlling for
variation in risk-aversion and learning-rate distributions?
9

Unlike many agent-based studies that vary multiple structural parameters simultaneously, we
adopt a controlled factorial design in which representation homogeneity serves as the primary
treatment variable, while risk-control and learning-rate heterogeneity serve as control dimensions
whose cross-sectional distributions are independently varied to verify robustness.
5.1 Treatment and Control Dimensions
Primary T reatment: Representation Homogeneity (HW )Representation homogeneity
measures similarity in the feature-extraction layerh i(S) =ϕ(W iS). This is the central object
of investigation.
•Low Homogeneity(H W = 0): Representation matrices are drawn from a wide distribution
Wi ∼ Dwide W , producing large average pairwise representation distances.
•High Homogeneity(H W = 1): Representation matrices are tightly clustered around a
common benchmarkW i ∼ Dtight W , producing small average pairwise representation distances.
The mean scale ofW i is preserved across regimes so that the treatment modifies only the average
pairwise representation distance
drepr = 2 N(N−1) X i<j drepr(i, j).
Control Dimension: Risk-Aversion Distribution (Hγ)Risk-aversion parameters are drawn
from
γi ∼LogNormal(µ γ, σγ)
and remain fixed throughout the simulation. The two regimes differ only in cross-sectional disper-
sion:
•H γ = 0:σ γ =σ high γ (heterogeneous risk preferences)
•H γ = 1:σ γ =σ low γ (uniform risk preferences)
while maintainingE[γ i] = ¯γin both regimes. This dimension serves as a control: it verifies that
representation effects are not confounded by variation in downstream risk-taking behavior.
Control Dimension: Learning-Rate Distribution (Hη)Learning rates are drawn from
ηθ,i ∼LogNormal(µ η, ση)
and remain fixed throughout the simulation. The two regimes are:
•H η = 0:σ η =σ high η (heterogeneous learning speeds)
•H η = 1:σ η =σ low η (uniform learning speeds)
while holdingE[η θ,i] = ¯ηfixed.
10

5.2 Factorial Structure
The three dimensions produce a 2×2×2 factorial design:
(HW , Hγ, Hη)∈ {0,1}3.
This yields eight experimental configurations. The factorial structure is used not to identify “which
dimension matters most,” but to estimate the representation homogeneity effectβ W while control-
ling for potential confounds from risk-aversion and learning-rate distributions.
A key identification requirement is that treatments alter thedispersionof agent characteristics
rather than their mean levels. Otherwise, treatment effects could reflect shifts in average behavior
rather than structural homogeneity.
5.3 Monte Carlo Simulation Procedure
For each experimental configurationc∈ {1, . . . ,8}, we performMindependent Monte Carlo simu-
lations of the market model. LetY c,m denote a systemic outcome statistic from simulationmunder
configurationc. The estimated outcome is
¯Yc = 1 M MX m=1 Yc,m.
Standard errors are computed across Monte Carlo replications.
5.4 Mechanism Decomposition
To understand how representation homogeneity propagates through the system, we evaluate out-
comes at multiple layers of the market dynamics.
Representation SynchronizationAverage representation distance:
drepr = 2 N(N−1) X i<j drepr(i, j).
F orecast SynchronizationCross-agent forecast correlation:
ρforecast = Corr(ˆri,t,ˆrj,t).
Position SynchronizationCross-agent position correlation:
ρposition = Corr(Di,t, Dj,t).
Order Flow ConcentrationAggregate order-flow concentration is measured by
Ct = | P i ∆Di,t|P
i |∆Di,t| .
Higher values indicate more directional market-wide trading.
Liquidity StressLiquidity pressure is measured using the average price impact coefficientλ t,
the average inventory premiumψ t, and dealer inventory stress|I t|.
11

T ail RiskSystemic outcomes include crash frequency (proportion of returns exceeding a threshold
multiple of unconditional volatility), extreme return quantiles (1% and 5% Value-at-Risk), and
maximum drawdown.
These measures allow us to trace the mechanism
representation similarity→forecast synchronization→position synchronization→order-flow concentration→liquidity stress→tail risk.
5.5 Factorial Effect Estimation
To quantify treatment effects, we estimate a factorial regression across experimental configurations:
Y=α+β W HW +β γHγ +β ηHη +β W γHW Hγ +β W ηHW Hη +β γη HγHη +β W γηHW HγHη +ε.
(37)
The primary object of interest isβ W , which measures the direct effect of representation ho-
mogeneity on the outcome variable. The coefficientsβ γ andβ η serve as controls, verifying that
observed effects are not driven by variation in risk-aversion or learning-rate distributions. Interac-
tion termsβ W γandβ W ηare reported in the appendix as secondary findings, capturing whether
the representation effect is amplified when downstream decision parameters are also more uniform.
5.6 Single-Factor Representation Scan
In addition to the factorial design, we conduct a continuous single-factor experiment that varies
only representation dispersion while holding risk-aversion and learning-rate distributions fixed at
their heterogeneous baseline levels (H γ = 0,H η = 0). Representation dispersion is varied across
15 grid points fromσ wide W toσ tight W . This experiment provides transparent visual evidence of how
representation distance relates to tail risk, and is used to identify potential threshold effects.
As a robustness check, the same scan is repeated under uniform risk-aversion and learning-rate
distributions (H γ = 1,H η = 1). If the two curves are close, this supports the conclusion that
the representation effect is the dominant channel; if they diverge, the interaction merits further
investigation.
5.7 Operational Identification of the Critical Representation Threshold
The hypothesis developed in Section 7 posits the existence of a critical representation-distance
threshold d
crit
repr below which tail risk rises sharply. The single-factor scan provides the natural
setting for estimating an operational counterpart of this threshold.
Let
F(d) =E

Y| drepr =d

,
whereYdenotes a tail-risk outcome such as crash frequency, extreme return quantiles, or peak
execution cost. We define the estimated critical threshold
bd crit repr
as the change-point in the relationship between drepr andF(d), obtained from a segmented linear
fit. Intuitively, this is the point at which marginal reductions in representation distance begin to
produce disproportionately large increases in fragility. Spline-based maximum-curvature estimates
and event-probability crossing rules are reported as robustness checks.
12

Because this threshold is outcome-specific by construction, we report estimates for multiple
tail-risk measures and assess whether they cluster within a narrow range. Convergence of the
estimated thresholds across different outcome variables would provide evidence that the critical
transition reflects a structural regime shift in synchronization dynamics rather than an artifact of
a particular fragility measure.
5.8 Matched Forecast-Distance Identification Experiment
A distinctive feature of this paper’s framework is the formal separation of representation homo-
geneity from forecast overlap. To test this distinction empirically, we construct a matched-design
experiment in which two groups of agents are selected to have similar integrated forecast distances
dforecast but different representation distancesd repr.
ConstructionWe generate a large number of candidate agent populations and compute both
¯drepr and ¯dforecast for each, using the empirical approximation ofd forecast under the same reference
distributionµdefined in Section 2. Two groups are then selected:
•Group A(lowd repr, moderated forecast): Agents encode market states through similar rep-
resentations but maintain moderate forecast diversity through differences in readout vectors
θi.
•Group B(highd repr, moderated forecast): Agents encode market states through diverse rep-
resentations, with forecast diversity at a similar level to Group A.
The matching criterion requires that the two groups’ average forecast distances fall within a
narrow band (difference<5%), while their representation distances differ substantially.
If strict matching yields insufficient candidate populations (success rate<3%), the design
automatically transitions to a conditional binning approach: all candidate populations are sorted
by ¯dforecast into bins, and within each bin, high- versus low- ¯drepr subgroups are compared.
Experimental ProtocolEach group is simulated through two phases. In thecalm phase, the
market operates under normal fundamental volatility for an extended period. In thestress phase, a
sequence of large fundamental shocks is injected. The hypothesis is that Groups A and B will behave
similarly during the calm phase—since their forecast distances are matched—but that Group A will
exhibit significantly greater synchronization, liquidity stress, and tail risk during the stress phase,
because its agents share a common representational lens that compresses forecast disagreement
under extreme states.
This experiment is designed to assess whether representation homogeneity carries incremental
explanatory power for tail risk beyond what is captured by realized forecast overlap. A necessary
condition for the matched comparison to be informative is that the two groups are well-matched
during the calm phase; we therefore report calm-phase differences in forecast correlation, position
correlation, and volatility as a diagnostic check before interpreting stress-phase results.
5.9 Negative Control Experiments
To ensure that observed fragility arises from representation-driven synchronization rather than from
model-specific nonlinearities, we implement several negative controls:
1.Constant liquidity: fixingλ t =λ 0 andψ t =ψ 0, which disables the nonlinear amplification
channel.
13

2.Shared signals without shared representations: all agents observe the sameSt but use
highly dispersed representation matrices.
3.Linear representation benchmark:h i(S) =W iS, which removes the nonlinear activation.
These controls verify that the tail risk amplification identified in the main experiments is driven
by structural synchronization in the representation layer, not by mechanical features of the pricing
equation.
6 Representation Convergence Experiments
The factorial design in Section 5 identifies the effect of representation homogeneity by independently
manipulating the dispersion of agent characteristics at initialization. While this approach isolates
structural effects in a controlled setting, real-world AI ecosystems are unlikely to transition abruptly
from heterogeneous to homogeneous states. Instead, convergence typically occurs gradually as firms
adopt common infrastructure, share training data pipelines, or deploy increasingly standardized
foundation models.
To capture these transition dynamics, we now study environments in which representation
matrices evolve stochastically over time toward a shared industry architecture. The objective of
this section is not identification—which is already established in the factorial design—but rather to
examine thetemporal propagationof synchronization and tail risk as representation homogeneity
increases endogenously. The baseline convergence experiments treat the common benchmarkW base
as static; Section 8 relaxes this assumption by allowing the foundation model itself to evolve over
time.
6.1 Dynamic Evolution of Representation Matrices
Representation matrices evolve according to the matrix-valued Ornstein–Uhlenbeck process intro-
duced in Section 3:
dWi,t =ν W (Wbase −W i,t)dt+σ W dBW i,t ,(38)
whereW base represents an industry-standard foundation model,ν W controls the speed of represen-
tation convergence, andσ W governs exploratory deviations across agents.
Crucially, the risk-aversion parametersγ i and learning ratesη θ,i remain fixed at their initialized
values throughout the convergence process. This isolates the effect of representation convergence
from any simultaneous changes in risk preferences or learning behavior, consistent with the model
specification in Section 3.
Ast→ ∞orν W → ∞, representation mapsh i(S) =ϕ(W i,tS) converge toward a common
feature space, reducing the pairwise representation distanced repr(i, j) defined in Section 2.
6.2 Dynamic Homogeneity Metrics
To track convergence over time, we compute time-varying measures:
drepr,t = 2 N(N−1) X i<j drepr,t(i, j),(39)
ρforecast t = Corr  ˆri,t,ˆrj,t  ,(40)
ρposition t = Corr  Di,t, Dj,t  .(41)
14

These statistics allow us to track the progressive tightening of the synchronization chain
representation convergence→forecast synchronization→position synchronization.
6.3 Convergence Scenarios
We simulate the dynamic system starting from a heterogeneous initial condition in which represen-
tation matrices are drawn from a wide cross-sectional distribution. Risk-aversion and learning-rate
parameters are drawn from their baseline heterogeneous distributions and held fixed. The conver-
gence process in equation (38) is then activated at different speeds:
Scenarioν W Interpretation
No convergence 0 Negative control
Slow convergence 0.001 Gradual industry standardization
Baseline convergence 0.01 Moderate adoption of common AI infrastructure
Fast convergence 0.1 Rapid industry consolidation
For each scenario, we track representation distance drepr,t, forecast correlationρ forecast t , position
correlationρ position t , order-flow concentration, dealer inventory stress|I t|, and the liquidity coeffi-
cientsλ t andψ t. A key object of interest is whether the time path of drepr,t crosses the critical
threshold estimated in Section 5, and whether downstream fragility indicators deteriorate sharply
at or near this crossing.
7 Mechanism-Based Hypotheses
7.1 Hypothesis I: The Volatility Paradox and Hidden Leverage
Driven by the partial-adjustment rule in Equation (32), we hypothesize that rising representation
homogeneity will generate smoother collective trends in returns. According to Equation (31),
these trends compress the centered perceived variance ˆσ 2 t . Paradoxically, low perceived volatility
then encourages agents to expand positions, while the stickiness termκD i,t−1 allows leverage to
accumulate gradually and opaquely.
This mechanism does not require that agents share identical risk preferences or learning rates.
Even with heterogeneousγ i andη θ,i, agents whose representations converge will tend to forecast in
the same direction, producing smoother aggregate returns and triggering the volatility-compression
channel through the common perceived-volatility estimator.
7.2 Hypothesis II: Critical Representation Threshold
Representation homogeneity is not equivalent to temporary similarity in forecasts. Two agents may
occasionally produce similar return forecasts even if they process information through very different
feature spaces. By contrast, representation homogeneity means that agents interpret market states
through similar informational lenses. As a result, they are likely to emphasize the same signals,
neglect the same signals, and commit similar forecast errors.
The key theoretical implication concerns thestate-conditionalnature of this overlap. The
integrated forecast distanced forecast(i, j) averages disagreement over all states weighted by the
reference measureµ. However, the systemic consequences of homogeneity depend primarily on
15

disagreement instress states—states where coordinated position adjustments can overwhelm market
maker capacity.
We hypothesize the existence of a positive critical level of average representation distance,
d
crit
repr >0,
such that when
drepr,t > d
crit
repr,
cross-agent disagreement remains sufficiently dispersed to stabilize aggregate order flow, whereas
when
drepr,t ≤ d
crit
repr,
representation-driven synchronization becomes self-reinforcing, directional order flow intensifies,
and tail risk rises sharply. The threshold is therefore interpreted as the point at which cross-
sectional heterogeneity ceases to provide an effective buffer against common forecast errors.
That the critical threshold is strictly positive is important: fragility does not require agents
to be identical. In the present framework, readout heterogeneity, idiosyncratic noise, leverage
constraints, and adjustment frictions all continue to provide residual dispersion even when repre-
sentations converge. The threshold emerges once this residual heterogeneity becomes too weak to
buffer common directional errors induced by shared representations. Equivalently, the dangerous
regime beginsbeforecomplete representational overlap—a distinction with direct implications for
the timing of macroprudential intervention.
This hypothesis implies that matched populations with similar integrated forecast distances but
lower representation distances should exhibit sharper stress-period synchronization and higher tail
risk: by comparing two agent populations with similar integrated forecast distances but different
representation distances, we can assess whether representation homogeneity predicts stress-period
fragility beyond what forecast overlap alone would imply.
7.3 Hypothesis III: Foundation-Model Drift and Common Blind Spots
A distinguishing feature of representation homogeneity, relative to forecast correlation, is the cre-
ation ofcommon blind spots: systematic gaps in how agents perceive market states. Forecast
correlation can be episodic and state-dependent, but representation homogeneity is structural.
When agents share a common feature space, they are predisposed not only to agree when their
shared features are informative, but also tomiss the same signalswhen their shared features are
uninformative.
In the representation convergence experiments (Section 6), we examine whether this structural
vulnerability persists even when the foundation model itself evolves over time. Under the non-
stationary extension (Section 8), the feature manifold is constantly shifting. However, as long as
the industry standardization speedν W is sufficiently large, cross-agent representation distances still
collapse toward zero. The common blind spots therefore move with the foundation model rather
than being eliminated by its evolution.
8 Stress Tests and Robustness Checks
To validate the fragility mechanisms identified above, we conduct a set of out-of-sample stress tests.
16

8.1 Heavy-Tailed Exogenous Shocks
Empirical high-frequency returns often exhibit jumps and heavy tails. We therefore replace the
Gaussian innovationϵ t with a jump-diffusion specification containing a symmetricα-stable L´ evy
component. The hypothesis is that markets with heterogeneous representations can absorb such
shocks through staggered belief adjustments, whereas markets with homogeneous representations
convert the same exogenous shock into an endogenous liquidity event.
8.2 Asynchronous Learning and Stochastic Latency
Institutional AI agents need not refresh their readout layers or execute trades at exactly the same
instant. We therefore introduce stochastic asynchronous update schedules, modeled through inde-
pendent Poisson clocks with agent-specific arrival rates. The hypothesis is that moderate latency
dispersion delays the timing of synchronized deleveraging but does not eliminate the underlying
instability once representation homogeneity is sufficiently high.
8.3 Dynamic Foundation Model and Non-Stationary Environments
In the representation convergence specification introduced in Section 6, the representation matrices
of all agents converge toward a static industry-standard foundation modelW base. While this par-
simonious specification isolates the effect of structural homogeneity, real-world foundation models
are continuously retrained and fine-tuned on new data.
To ensure that our results are driven by the vanishing structural distance between agents rather
than by a stagnant representation space, we introduce a non-stationary baseline model:
dWbase,t =σ base dZt,(42)
wheredZ t is a matrix of standard Brownian motions independent of the agents’ idiosyncratic
exploration terms, andσ base governs the innovation rate of the underlying AI architecture.
Consequently, the individual agent representation dynamics track this moving target:
dWi,t =ν W

Wbase,t −W i,t

dt+σ W dBW i,t .(43)
Under this generalized specification, the feature manifoldϕ(W base,tSt) is constantly shifting,
allowing agents to continuously adapt to new market regimes. However, as the industry standard-
ization speedν W → ∞, cross-agent representation distancesd repr(i, j) still collapse toward zero,
so that agents process market states through increasingly similar—albeit evolving—informational
lenses.
9 Discussion and Mechanistic Interpretation
9.1 Resolving the Paradox: Local Adaptation vs. Global Collapse
A natural question is how a tractable representation-readout architecture can explain far-from-
equilibrium market crashes. The mechanism is bi-phasic. During the calm phase, adaptive readout
updates in Equation (35) progressively align beliefs, while the price system and the volatility
estimator compress perceived risk. During the crash phase, the nonlinear structure of the risk-
control rule in Equation (32) dominates. The sudden expansion of the volatility denominator
clashes with sticky positions, pushing many agents across the same adjustment threshold at nearly
the same time. Representation homogeneity matters because it makes this threshold crossing
synchronized rather than staggered.
17

9.2 Why Representation Homogeneity Is Especially Destabilizing
A key implication of the representation-readout architecture is that representation homogeneity
is not equivalent to temporary similarity in forecasts. Two agents may occasionally produce sim-
ilar return forecasts even if they process information through very different feature spaces. By
contrast, representation homogeneity means that agents interpret market states through similar
informational lenses. As a result, they are likely to emphasize the same signals, neglect the same
signals, and commit similar forecast errors. In systemic-risk terms, this creates common blind spots.
Forecast correlation can be episodic, but representation homogeneity is structural: it increases the
probability that agents will be wrong in the same direction at the same time.
The matched forecast-distance experiment in Section 5 is designed to test this claim directly.
If two agent populations with similar forecast overlap but different representation distances ex-
hibit markedly different behavior under stress, this would constitute evidence that representation
homogeneity carries independent information about tail risk.
9.3 Why the Critical Threshold Is Positive
An important implication of Hypothesis II is that the critical representation threshold d
crit
repr is
expected to be strictly positive. Fragility does not require agents to become identical. In the
present framework, several residual sources of dispersion persist even under high representation
homogeneity: readout heterogeneity from differentθ i, idiosyncratic exploration noise in the OU
process, heterogeneous risk aversionγ i, diverse learning ratesη θ,i, and hard leverage constraints
¯Di. The critical threshold marks the point at which these residual buffers become insufficient to
prevent common directional errors from cascading through the order-flow concentration channel.
This has a direct policy implication: the dangerous regime begins before complete represen-
tational overlap. A regulator monitoring representation distances need not wait until agents are
nearly identical to intervene; the structurally relevant boundary lies at a positive distance that
depends on the market’s liquidity environment, friction parameters, and residual heterogeneity in
downstream decision-making.
9.4 Role of Risk-Control and Learning Heterogeneity
The factorial design treats risk-aversion and learning-rate distributions as control dimensions rather
than primary treatment variables. This does not imply that these characteristics are irrelevant to
systemic stability. Rather, the experimental design is structured to test a more specific claim: that
representation homogeneity is anecessaryupstream condition for the type of synchronized fragility
studied here, and that its effects are robust to variation in downstream decision parameters.
If the factorial results show thatβ W is large and significant whileβ γ andβ η are small, this
supports the conclusion that the primary source of synchronization risk lies in how agents encode
information, not in how they translate forecasts into positions. If interaction effectsβ W γorβ W η
are also significant, this would indicate that risk-control or learning uniformity canamplifythe
representation effect, even if they do not independently generate it.
9.5 Methodological Scope and Empirical Boundaries
A central premise of this framework is the evaluation of financial markets under conditions of se-
vere representation homogeneity among AI trading agents. We acknowledge that current financial
ecosystems remain in a mixed state, characterized by a blend of diverse algorithmic systems, tradi-
tional institutional investors, and noise traders. Consequently, the high-representation-homogeneity
18

configurations in the factorial design should be interpreted as boundary cases for macroprudential
stress testing rather than as strictly contemporaneous empirical descriptions of current markets.
However, the methodological choice to simulate these boundary conditions is both deliberate
and necessary. The objective of this structural approach is not to provide high-frequency point
forecasts of current market states, but rather to conduct counterfactual analyses of fragility. By
isolating the mechanics of representation-driven synchronization, the model functions as a controlled
laboratory to identify the structural thresholds where a resilient heterogeneous ecology transitions
into a fragile synchronized state.
Furthermore, while an ecosystem completely dominated by overlapping foundation models has
not yet fully materialized, the underlying mechanisms of synchronized deleveraging have historical
precedents. Localized episodes of structural convergence, such as the synchronized unwinding of
quantitative models during historical liquidity events, provide empirical proxies for the dynamics
captured here. By formalizing how hidden leverage accumulates during low-volatility regimes and
violently unwinds during shocks, this framework equips regulators with the theoretical scaffolding
required to monitor and mitigate representation monoculture risk before it manifests as extreme
tail events in AI-dominated infrastructures.
10 Policy Implications
•Monitoring representation-level concentration: Regulators should develop tools to as-
sess the degree of representational overlap among AI trading systems, going beyond the
current focus on strategy classification or position reporting. Metrics analogous tod repr could
provide early-warning indicators of structural synchronization risk. The finding that the crit-
ical representation threshold is strictly positive implies that intervention may be warranted
well before agents become nearly identical.
•AI ecosystem design and upstream infrastructure: Authorities should monitor con-
centration in upstream AI infrastructure, including common data vendors, shared feature-
extraction pipelines, and heavily concentrated foundation-model providers. The results of
this paper suggest that convergence at the representation level—where agents learn tosee
markets similarly—may be more consequential for systemic stability than convergence in risk
management parameters.
•Re-evaluating macroprudential paradigms: While standardized risk-management re-
quirements serve important prudential objectives, regulators should be aware that exces-
sive standardization in how market participantsprocess informationcan create procyclical
fragility. The key insight is that representation homogeneity can generate synchronized be-
havior even among agents with diverse risk preferences and trading strategies.
11 Conclusion
Similarity in how AI trading systems represent market states can propagate through belief formation
and trading behavior to amplify systemic instability. The central lesson is not simply that AI
agents may trade similarly, but that sufficiently similar agents may come toseemarkets similarly—
encoding the same features, neglecting the same signals, and creating common blind spots that
remain latent until stress exposes them. The formal separation of representation homogeneity from
forecast overlap reveals that the integrated distance between agents’ predictions may understate
19

the degree of structural fragility, because it averages over states and can mask severe disagreement
compression under stress.
The existence of a positive critical representation threshold implies that the transition from
resilience to fragility occurs before agents become identical. Residual heterogeneity in readout
parameters, risk preferences, and learning rates provides a buffer, but this buffer has finite capacity.
Once representation distances fall below the critical level, synchronized forecast errors cascade
through order-flow concentration and nonlinear liquidity responses into elevated tail risk.
The experimental framework—combining factorial identification, matched forecast-distance de-
signs, and dynamic convergence simulations—provides multiple complementary lenses through
which this mechanism can be tested. Preserving diversity in how market participants represent
and process information may therefore be an indispensable stabilizer in AI-dominated financial
ecosystems.
Appendix A: Aligned Representation Distance
Hidden features in neural representations may be equivalent up to permutation. In such cases,
the raw Euclidean distance between feature vectors may exaggerate representation differences even
when the encoded information is similar.
To address this issue, we construct an aligned representation distance.
LetP K denote the set ofK×Kpermutation matrices. We define
dalign repr (i, j) = inf Π∈PK
Z
S
∥hi(S)−Πh j(S)∥2 2 dµ(S)
1/2
.(44)
Operationally, the empirical approximation becomes
dalign repr (i, j) = min Π∈PK

1
T
TX
t=1
∥hi(St)−Πh j(St)∥2 2
!1/2
.(45)
This aligned metric allows hidden units to be reordered before computing distances, thereby
isolating differences in encoded information rather than superficial feature indexing.
In the robustness analysis, all representation homogeneity statistics are recomputed usingd align repr
to verify that the findings are not driven by arbitrary permutations of hidden features.
References
[Arthur, 1994] Arthur, W. B. (1994). Inductive reasoning and bounded rationality.American
Economic Review, 84(2):406–411.
[Brock and Hommes, 1998] Brock, W. A. and Hommes, C. H. (1998). Heterogeneous beliefs and
routes to chaos in a simple asset pricing model.Journal of Economic Dynamics and Control,
22(8–9):1235–1274.
[Duffie and Singleton, 1993] Duffie, D. and Singleton, K. J. (1993). Simulated moments estimation
of markov models of asset prices.Econometrica, 61(4):929–952.
[Hommes, 2006] Hommes, C. H. (2006). Heterogeneous agent models in economics and finance.
Handbook of Computational Economics, 2:1109–1186.
20

[LeBaron, 2006] LeBaron, B. (2006). Agent-based computational finance.Handbook of Computa-
tional Economics, 2:1187–1233.
[Tesfatsion, 2002] Tesfatsion, L. (2002). Agent-based computational economics: Growing
economies from the bottom up.Artificial Life, 8(1):55–82.
21
