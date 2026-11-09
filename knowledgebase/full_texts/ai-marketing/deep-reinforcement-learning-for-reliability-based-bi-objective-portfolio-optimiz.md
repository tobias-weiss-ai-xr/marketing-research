---
title: Deep Reinforcement Learning for Reliability Based Bi-Objective Portfolio Optimization
url: https://arxiv.org/abs/2607.06610
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Sounaq Das
- Tanmay Sen
- Raghu Nandan Sengupta
- Aditya Gupta
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.06610
pages: 24
chars: 64093
fetched_at: '2026-11-08T13:01:14+00:00'
kb_version: 1
---

# Deep Reinforcement Learning for Reliability Based Bi-Objective Portfolio Optimization

DEEPREINFORCEMENTLEARNING FORRELIABILITYBASED
BI-OBJECTIVEPORTFOLIOOPTIMIZATION
Sounaq Das
Indian Institute of Management Amritsar
Amritsar, India
dassounaq@gmail.com
Tanmay Sen
SQC & OR Unit
Indian Statistical Institute Kolkata
Kolkata, India
tanmay.sen@isical.ac.in
Raghu Nandan Sengupta
Department of Management Sciences
Indian Institute of Technology Kanpur
Kanpur – 208 016, India
raghus@iitk.ac.in
Aditya Gupta
McKinsey and Company
Gurgaon, India
aditya_gupta-guva@mckinsey.com
July 9, 2026
ABSTRACT
Portfolio optimization under uncertainty is inherently a multi-objective decision problem involving
complex interactions among return, risk, market dynamics, and practical investment constraints.
Existing reliability based portfolio optimization approaches primarily rely on static optimization
frameworks and often fail to capture sequential decision making, tail risk, and market frictions such as
transaction costs. To address these limitations, we propose a deep reinforcement learning framework
for multi-objective reliability based portfolio optimization (MORP-DRL). The proposed framework
jointly optimizes expected return and downside risk using three complementary risk measures: vari-
ance, Conditional Value-at-Risk (CVaR), and Entropic Value-at-Risk (EVaR). To model uncertainty
and heavy-tailed market behavior, asset returns are represented using GARCH(1,1), Extreme Value
Theory, and a t-copula dependence structure, while realistic scenarios are generated through quasi-
Monte Carlo simulation. A Proximal Policy Optimization (PPO) based strategy is developed under
practical constraints including transaction costs and portfolio bounds, and is benchmarked against
NSGA-II. Experiments on ten global equity indices across pre-COVID, COVID, and post-COVID
market regimes demonstrate that MORP-DRL achieves competitive risk-return performance, reduced
downside risk during periods of market stress, and scalability to high-dimensional portfolio settings.
Keywords:Bi-objective, Portfolio Optimization, Deep Reinforcement Learning, Extreme Value Theory (EVT),
Entropic Value-at-Risk (EVaR), NSGA-II , QMC, t-copula
1 Introduction
Portfolio optimization is one of the most fundamental problems in quantitative finance and investment management.
The primary objective is to allocate capital among different financial assets in a way that balances expected return and
investment risk while satisfying practical investment constraints. The seminal work of Markowitz [1, 2] introduced
the modern portfolio theory (MPT), which formulated portfolio selection as a mean-variance optimization problem.
This framework established the foundation of modern portfolio management by emphasizing diversification and the
trade-off between return and risk. Subsequent developments, including the capital asset Pricing model (CAPM)
[3], Black-Litterman model, and factor based investment strategies, further extended classical portfolio theory by
incorporating systematic market risk and investor preferences. Despite their importance, these traditional models rely on
several simplifying assumptions, such as normally distributed returns, linear dependence structures, constant covariance
arXiv:2607.06610v1  [cs.LG]  7 Jul 2026

APREPRINT- JULY9, 2026
matrices, and frictionless markets. However, financial markets behave very differently. Asset returns frequently
exhibit sudden fluctuations, changing dependence patterns, periods of high volatility, and extreme market movements,
particularly during financial crises and uncertain economic conditions. As a result, traditional variance-based approaches
may not adequately capture downside and extreme market risks. To address these limitations, alternative downside risk
measures have been extensively investigated in the literature. Value-at-Risk (VaR) [4] emerged as one of the earliest
and most widely adopted downside risk measures in financial risk management. Later, [ 5] introduced Conditional
Value-at-Risk (CVaR), which measures the expected loss beyond the VaR threshold and satisfies the properties of a
coherent risk measure. More recently, Entropic Value-at-Risk (EVaR) [6, 7] and related tail-risk measures have gained
attention due to their stronger theoretical properties and ability to capture extreme losses under non-Gaussian market
conditions.
At the same time, practical portfolio optimization problems have become increasingly challenging due to the incorpo-
ration of realistic investment constraints such as transaction costs, cardinality restrictions, minimum and maximum
holding limits, and budget constraints. The inclusion of such constraints often leads to highly nonlinear and non-convex
optimization problems that are difficult to solve using conventional convex optimization techniques. To overcome these
challenges, several studies have explored metaheuristic and evolutionary optimization methods, including Genetic
Algorithms (GA), Particle Swarm Optimization (PSO), Ant Colony Optimization (ACO), and Non-dominated Sorting
Genetic Algorithm-II (NSGA-II) [ 8, 9, 10]. These approaches have demonstrated strong capabilities in handling
multi-objective optimization problems and complex feasible regions.
In recent years, the rapid growth of financial data and increasing market complexity have encouraged the use of Machine
Learning (ML) and Deep Learning (DL)[11] techniques in portfolio optimization [12, 13]. Early ML based approaches
primarily focused on predicting asset returns using methods such as Support Vector Machines, Random Forests, and
Artificial Neural Networks. Although these approaches improved predictive capability, portfolio decisions were typically
generated through separate static optimization procedures and lacked adaptability to rapidly changing market conditions.
Furthermore, these methods often failed to capture the sequential and dynamic nature of investment decisions. To
address these limitations, Deep Reinforcement Learning (DRL) [ 14, 15] has emerged as a promising paradigm for
dynamic portfolio management by learning allocation strategies directly through interactions with market environments.
Unlike supervised learning methods, DRL can optimize long term investment objectives while continuously adapting to
evolving market conditions. Recent studies have shown the effectiveness of actor-critic architectures, Deep Q-Networks,
and policy gradient methods in financial applications [16]. Despite recent progress, several important limitations remain
insufficiently addressed in the existing literature. First, many DRL based portfolio optimization frameworks either
neglect transaction costs or model them in a simplified manner, resulting in unrealistic rebalancing strategies. Second,
although tail-risk measures such as CVaR and EVaR have been investigated independently [ 17], their integration
within a reliability based portfolio optimization framework remains limited. Third, most existing DRL approaches
do not explicitly incorporate probabilistic reliability constraints to ensure robust portfolio feasibility under uncertain
market conditions and nonlinear dependence structures. Finally, comparative studies between classical evolutionary
optimization approaches and DRL based optimization across different market regimes remain relatively scarce.
Motivated by these research gaps, this study proposes a reliability based Bi-objective portfolio optimization framework
integrated with Deep Reinforcement Learning. The proposed framework incorporates transaction costs, probabilistic
reliability constraints, and multiple downside risk measures within a unified optimization setting. In particular, three
complementary portfolio optimization models are developed using variance, Conditional Value-at-Risk (CVaR), and
Entropic Value-at-Risk (EVaR) as alternative risk measures. To capture nonlinear dependence and tail co-movement
among financial assets, Quasi-Monte Carlo (QMC) simulation is combined with a t-copula based dependence structure
for reliability estimation under uncertainty.
Furthermore, a PPO-based reinforcement learning framework is developed to dynamically optimize portfolio allocation
policies under realistic market constraints. The proposed approach is evaluated using a diversified portfolio consisting
of major global equity indices across three distinct market regimes, namely the pre-COVID, COVID, and post-COVID
periods. The performance of the proposed DRL framework is compared with equal weight benchmark portfolios and
the classical NSGA-II multi-objective optimization algorithm.
The major contributions of this work are summarized below:
1. We develop a reliability based bi-objective portfolio optimization framework for practical portfolio rebalancing
under transaction cost constraints using three complementary risk measures: variance, Conditional Value-at-
Risk (CVaR), and Entropic Value-at-Risk (EVaR).
2. Reliability constraints are evaluated using Quasi-Monte Carlo (QMC) simulation together with a t-copula
dependence model, enabling the framework to capture uncertainty, nonlinear dependence, and tail dependence
among global financial assets.
2

APREPRINT- JULY9, 2026
3. We develop a Proximal Policy Optimization (PPO) based deep reinforcement learning framework that learns
adaptive portfolio allocation policies under joint risk and reliability constraints, and compare its performance
with the classical NSGA-II multi-objective optimization algorithm
4. Extensive experiments are conducted across pre-COVID, COVID, and post-COVID market regimes. The
proposed approaches are benchmarked against equal-weight portfolios and NSGA-II under variance, CVaR,
and EVaR risk measures.
5. To evaluate the scalability of the proposed framework, additional experiments are performed on the FTSE100
universe, showing that both NSGA-II and PPO remain effective in high-dimensional portfolio optimization
while exhibiting distinct portfolio allocation characteristics.
The remainder of this paper is organized as follows. Section 2 presents a comprehensive literature survey on recent
advances and research trends in portfolio optimization. Section 3 formulates the portfolio optimization problem and
introduces the background concepts and risk measures considered in this study. Section 4 describes the proposed
bi-objective portfolio optimization models. Section 5 presents the proposed methodology, including the PPO-based
deep reinforcement learning framework. Section 6 details the experimental setup, data preprocessing procedures, and
implementation settings. Section 7 reports the experimental results and discussion, including a comparative analysis
across different market regimes. Finally, Section 8 concludes the paper and highlights potential directions for future
research.
2 Literature Survey
Portfolio optimization has been one of the central problems in financial decision making since the seminal work of
[18], who introduced the mean–variance framework to balance expected return and risk. Over the years, several
extensions of the classical portfolio optimization problem have been proposed, including multi-objective formulations,
stochastic programming approaches, and portfolio models incorporating transaction costs and practical investment
constraints [19, 20]. Although these traditional optimization frameworks are mathematically rigorous, they are typically
based on static assumptions and often struggle to capture the highly dynamic and uncertain nature of real financial
markets. To overcome these limitations, researchers increasingly explored machine learning (ML) and deep learning
(DL) methods for financial forecasting and portfolio management. Early studies primarily focused on predicting stock
returns, volatility, or market trends using neural networks and deep architectures [12, 13]. However, in many of these
approaches, prediction and portfolio allocation are treated as separate tasks. Specifically, the models first estimate future
returns or volatility and subsequently perform portfolio optimization, which may lead to suboptimal decision-making
under rapidly changing market conditions.
Recently, Deep Reinforcement Learning (DRL) has emerged as a promising framework for portfolio optimization
due to its ability to model sequential decision-making under uncertainty. Unlike traditional optimization methods,
DRL enables an agent to continuously interact with the market environment and learn adaptive portfolio allocation
policies over time. [ 21] provides a theoretical foundation for reinforcement learning in portfolio optimization by
reformulating continuous-time portfolio selection as an entropy-regularized sequential decision-making problem. The
proposed framework demonstrates the feasibility of integrating reinforcement learning with stochastic optimal control
under realistic portfolio constraints, thereby motivating subsequent DRL-based portfolio optimization research. [22]
investigated the use of DRL algorithms for generating profitable trading strategies within a Markov Decision Process
(MDP) framework. Li et al. [23] proposed a deep reinforcement learning ensemble framework combining PPO, A2C,
and DDPG for stock trading. Their method achieved improved risk adjusted returns and outperformed traditional
portfolio allocation strategies. Similarly, [24] proposed a DQN-based portfolio management framework with discretized
portfolio weights and dueling network architectures to improve trading performance. Hierarchical DRL architectures
incorporating transaction costs were further explored in [25]. More recent studies have focused on improving robustness,
scalability, and risk sensitivity in portfolio optimization. [ 26] proposed a model free DRL framework for dynamic
portfolio allocation in high-dimensional financial markets by integrating transaction costs and investor risk aversion
into a mean-variance reward function. [27] developed predictive multi-period multi-objective portfolio optimization
models using deep learning techniques to forecast future market behavior. [ 28] introduced an industry grade DRL
framework incorporating sim to real methodologies and realistic trading constraints for robust portfolio optimization
across multiple asset classes. Furthermore, [ 29] proposed a deep portfolio optimization framework that explicitly
incorporates transaction costs and risk-aware reward functions into reinforcement learning-based portfolio management.
Several recent studies have investigated advanced reinforcement learning formulations tailored to financial markets.
The first work in this regard was done by [ 30]. their work lies in integrating Modern Portfolio Theory (MPT) with
deep reinforcement learning through a multimodal tensor-based framework. The paper combines technical indicators
and asset correlation information using Tucker tensor decomposition within a DDPG-based portfolio optimization
3

APREPRINT- JULY9, 2026
model, enabling dynamic portfolio allocation that captures both temporal market patterns and cross-asset dependencies.
The key contribution of [31] lies in integrating model-based deep reinforcement learning with portfolio optimization,
enabling the agent to learn market dynamics through an internal environment model rather than relying solely on
historical interactions. This improves sample efficiency and allows more stable long-term portfolio allocation decisions
under changing market conditions. For example, [26] developed a model free deep reinforcement learning framework
for dynamic portfolio allocation in high-dimensional financial markets, while [29] incorporated transaction costs and
risk-aware reward functions into deep portfolio optimization. These studies highlight the importance of designing
portfolio learning frameworks that can effectively capture market dynamics, asset dependencies, and realistic trading
constraints.
Despite the significant progress in DRL-based portfolio optimization, most existing studies primarily focus on return
maximization and variance-based risk control, while limited attention has been given to reliability-based optimization
and tail-risk-aware decision-making. In parallel, reliability-based portfolio optimization frameworks have been
studied in the operations research literature. In particular, [ 32] developed a bi-objective reliability-based portfolio
optimization framework under uncertainty. However, their approach relies on static optimization techniques and does
not consider sequential portfolio decision-making through reinforcement learning. Moreover, existing DRL based
portfolio optimization methods generally employ standard risk measures such as variance or Sharpe ratio and rarely
incorporate coherent tail risk measures such as Conditional Value-at-Risk (CVaR) and Entropic Value-at-Risk (EVaR)
within a reliability constrained framework. In addition, practical aspects such as transaction costs are often included
only as penalty terms in the reward function, without integrating them into probabilistic reliability constraints.
Motivated by these gaps, this paper proposes a novel framework termed MORP-DRL for multi-objective reliability based
portfolio optimization using deep reinforcement learning. The proposed framework integrates reliability constraints,
transaction costs, and multiple risk measures including variance, CVaR, and EVaR within a unified DRL based sequential
decision making framework. Unlike existing static reliability based optimization methods and conventional DRL
portfolio models, the proposed approach simultaneously addresses tail risk control, probabilistic reliability guarantees,
and dynamic portfolio rebalancing under realistic market conditions.
3 Problem Formulation
3.1 Risk Measures
Risk management plays an important role in portfolio optimization under uncertain and volatile market environments. In
this study, we consider three commonly used downside risk measures: Value-at-Risk (VaR), Conditional Value-at-Risk
(CVaR), and Entropic Value-at-Risk (EVaR), which capture different aspects of tail risk.
For a portfolio return Rp and confidence level α,VaRestimates the loss threshold exceeded with probability 1−α :
VaRα = inf{l:P(R p ≤ −l)≥1−α}.
CVaRextends VaR by measuring the expected loss beyond the VaR threshold: CVaRα =E[−R p | −Rp ≥VaR α].
Unlike VaR, CVaR satisfies coherence properties and captures tail losses more effectively.
EVaRprovides an exponential upper bound on tail risk: EVaRα(X) = inf z>0
n
1
z ln

E[ezX ]
α
o
. Owing to its strong
theoretical properties and sensitivity to extreme downside risk, EVaR serves as an effective alternative risk measure
for reliability based and robust portfolio optimization frameworks. Both CVaR and EVaR are coherent risk measures
satisfying the following properties, whereρ α(·)denotes a generic coherent risk measure at confidence levelα:
Monotonicity:X≤Y⇒ρ α(X)≤ρ α(Y),
Translation Invariance:ρ α(X+c) =ρ α(X) +c,
Positive Homogeneity:ρ α(λX) =λ ρα(X), λ≥0,
Subadditivity:ρ α(X+Y)≤ρ α(X) +ρ α(Y).
These risk measures are subsequently incorporated into the proposed portfolio optimization framework for evaluating
downside risk.
3.2 Reliability Based Portfolio Optimization
Reliability Based Design Optimization (RBDO) [33, 34] incorporates uncertainty directly into optimization through
probabilistic constraints. Rather than enforcing deterministic feasibility, RBDO seeks solutions that satisfy constraints
with a prescribed reliability level under uncertain conditions. In portfolio optimization, uncertainty naturally arises from
4

APREPRINT- JULY9, 2026
fluctuating asset returns and market volatility. Therefore, portfolio decisions should remain feasible with high probability
rather than under a single deterministic realization. Following the RBDO framework, the portfolio optimization problem
can be formulated as
max
x
Rp =
nX
i=1
E(ri)xi
s.t.P(g j(x, r)≥0)≥β j, j= 1, . . . , J,
nX
i=1
xi = 1,
xL i ≤x i ≤x U i , i= 1, . . . , n.
(3)
where xi denotes the portfolio weight of the ith asset, ri represents the return of the ith asset, and gj(x, r)denotes
the jth portfolio constraint under uncertain market conditions. The parameter βj ∈(0,1) represents the prescribed
reliability level, where larger values imply lower probabilities of constraint violation. To incorporate realistic portfolio
rebalancing effects, proportional transaction costs based on changes in portfolio allocations are also considered within
the return formulation [35, 36].
4 Proposed Bi-Objective Portfolio Optimization Models
Most existing reliability based multi-objective portfolio optimization (MORBPO) models [32] ignore transaction costs
during portfolio rebalancing, leading to unrealistic trading behavior and overestimated returns. To address this limitation,
proportional transaction costs are explicitly incorporated into the proposed framework. To the best of our knowledge,
transaction cost aware reliability based portfolio optimization under variance , CVaR , and EVaR based risk formulations
has not been explored in existing literature.
The notations used throughout the proposed models are summarized below:
•N: Total number of assets considered in the portfolio.
•w i: Portfolio weight allocated to thei th asset, wherei= 1,2, . . . , Nand0≤wi ≤1.
•w i,min andw i,max: Minimum and maximum allowable investment weights for thei th asset, respectively.
•w 0 i : Initial portfolio weight of thei th asset before rebalancing.
•¯ri: Expected return of thei th asset.
•r i,t: Return of thei th asset at time periodt.
•ˆσi,j: Estimated covariance between the returns of assetsiandj.
•α: Confidence level associated with the VaR/CVaR/EVaR calculations.
•T: Number of scenarios or historical observations used for risk estimation.
•γ: Auxiliary variable associated with the VaR threshold in the CVaR and EVaR formulations.
•β 1: Reliability level associated with the portfolio return constraint.
•β 2: Reliability level associated with the portfolio risk constraint.
•r ∗ p: Minimum target portfolio return specified by the investor.
•σ 2∗ p : Maximum acceptable portfolio variance in Model A.
•CV aR ∗: Maximum acceptable CVaR threshold in Model B.
•EV aR ∗: Maximum acceptable EVaR threshold in Model C.
•k i: Proportional transaction cost coefficient associated with buying or selling thei th asset.
•(x) + = max(x,0): Positive-part operator used in the CVaR formulation.
To capture different aspects of portfolio risk under uncertainty, we develop three reliability based bi-objective portfolio
optimization models. Although all three formulations aim to maximize expected portfolio return while minimizing
5

APREPRINT- JULY9, 2026
portfolio risk, they differ in the choice of risk measure employed. Specifically, Model A uses portfolio variance as
the risk metric, Model B incorporates Conditional Value-at-Risk (CVaR) to capture downside tail risk, and Model C
employs Entropic Value-at-Risk (EVaR), which provides a tighter and more conservative characterization of extreme
losses.
Model A: Variance-Based FormulationModel A extends the bi-objective reliability-based portfolio optimization
framework proposed in [ 32] by incorporating proportional transaction costs into the return reliability constraint.
Reliability constraints ensure that the net portfolio return, after accounting for proportional transaction costs, exceeds a
target return r∗ p with confidence level β1, while the portfolio variance remains below a prescribed threshold σ2∗ p with
confidence levelβ 2. It is further subject to budget and bound constraints.
max
w
NX
i=1
wi¯ri,min w
NX
i=1
NX
j=1
wiwj ˆσi,j
s.t.Pr
" NX
i=1
wiri,t −
NX
i=1
ki|wi −w 0 i | ≥r∗ p
#
≥β 1,
Pr


NX
i=1
NX
j=1
wiwj ˆσi,j ≤σ 2∗ p

 ≥β 2,
NX
i=1
wi = 1,
0≤w i,min ≤w i ≤w i,max ≤1, i= 1, . . . , N.
(6)
Model B: CVaR-Based Formulation:Unlike variance, which treats gains and losses symmetrically, CVaR focuses
on downside risk by measuring expected losses beyond the VaR threshold. This is also in extension to the framework
used in [32] Therefore, Model B maximizes expected return while minimizing CVaR under reliability and transaction
cost constraints.
max
w
NX
i=1
wi¯ri,min w



1
αT
TX
t=1

γ−
NX
i=1
wiri,t
!+
+γ



s.t.Pr
" NX
i=1
wiri,t −
NX
i=1
ki|wi −w 0 i | ≥r∗ p
#
≥β 1,
Pr

 1
αT
TX
t=1

γ−
NX
i=1
wiri,t
!+
+γ≤CV aR ∗

 ≥β 2,
NX
i=1
wi = 1,
0≤w i,min ≤w i ≤w i,max ≤1, i= 1, . . . , N.
(7)
Model C: EVaR-Based Formulation:Unlike CVaR, which measures average tail losses, EVaR provides a tighter and
more conservative characterization of extreme risk. Therefore, Model C maximizes expected return while minimizing
EVaR under reliability and transaction cost constraints and is an extension of the work done in [32]
6

APREPRINT- JULY9, 2026
max
w
NX
i=1
wi¯ri,min w γln

1
T
TX
t=1
exp

−γ−1
NX
i=1
wiri,t
!!
s.t.Pr
" NX
i=1
wiri,t −
NX
i=1
ki|wi −w 0 i | ≥r∗ p
#
≥β 1,
Pr
"
γln

1
T
TX
t=1
exp

−γ−1
NX
i=1
wiri,t
!!
≤EV aR∗ p
#
≥β 2,
NX
i=1
wi = 1,
0≤w i,min ≤w i ≤w i,max ≤1, i= 1, . . . , N.
(8)
5 Proposed Methodology
We propose a reliability aware multi-objective deep reinforcement learning framework (MORP-DRL) for sequential
portfolio optimization under uncertainty. The framework integrates transaction costs, probabilistic reliability constraints,
and multiple risk measures within a Proximal Policy Optimization (PPO) [37] based Actor-Critic architecture. Unlike
static portfolio optimization models, the proposed framework enables dynamic portfolio rebalancing by continuously
adapting allocations according to evolving market conditions.
5.1 MDP Based Portfolio Optimization Framework
The portfolio optimization problem is formulated as a Markov Decision Process (MDP) represented by (S,A,P, R, γ),
where S, A, P, R, and γ denote the state space, action space, transition dynamics, reward function, and discount factor,
respectively.
State Space ( S).The state at time t is defined as st = [pt,I t,w t−1, ct], where pt denotes normalized asset prices, It
represents market indicators and statistical features, wt−1 corresponds to previous portfolio weights, and ct denotes
available cash. Includingw t−1 enables the agent to account for portfolio rebalancing and transaction costs.
Action Space (A).The action corresponds to portfolio allocation weights
at =w t = [w1,t, w2,t, . . . , wN,t],
subject to
NX
i=1
wi,t = 1, w i,min ≤w i,t ≤w i,max.
Since portfolio weights are continuous, PPO is adopted to solve the optimization problem.
Transition Dynamics (P).The transition dynamics describe the evolution from st to st+1 after taking action at.
Since financial market dynamics are unknown, transitions are learned implicitly from historical data and simulated
scenarios. Asset returns are modeled using GARCH(1,1), extreme losses are characterized through EVT, and cross-asset
dependence is captured using at-copula. QMC simulation is then employed to generate training scenarios.
Reward Function (R).The reward jointly captures return improvement, risk-adjusted performance, and reliability
satisfaction(1):
rt = ∆St + ∆Rt +R rel t ,(1)
where
∆St = (St −S base)×100, S t = Rt Rt ,
andR t denotes the selected portfolio risk measure. The return improvement is defined as
∆Rt = (Rt −R base t )×100,
7

APREPRINT- JULY9, 2026
with portfolio net return
Rt =w ⊤ t µt −T Ct,
whereT Ct represents transaction costs. The reliability component is given by
Rrel t = Ψ(ρret t , β1) + Ψ(ρrisk t , β2),
where ρret t and ρrisk t denote the estimated return and risk reliability probabilities, respectively. The reliability function is
defined as
Ψ(ρ, β) =
30(ρ−β), ρ≥β,
−100(β−ρ), ρ < β.
Reliability Constraints:To account for uncertainty, reliability measures are estimated using simulated market
scenarios and incorporated into the reward design. Let {r(m) t }M m=1 denote M scenarios generated using the proposed
GARCH, EVT,t-copula, and QMC framework. The empirical return reliability is estimated as
ρret t = ˆPreturn = 1 M
MX
m=1
1
 NX
i=1
wir(m) i,t −
NX
i=1
ki|wi −w 0 i | ≥r∗ p
!
,
while the empirical risk reliability is computed as
ρrisk t = ˆPrisk = 1 M
MX
m=1
1

R(m)(w)≤ R∗

.
Here, R(m)(w) denotes the scenario-wise portfolio risk measure (variance, CVaR, or EVaR), andR∗ is the correspond-
ing risk threshold. These estimated reliabilities are compared against predefined confidence levels:
ρret t ≥β 1, ρ risk t ≥β 2.
The resulting reliability estimates are incorporated into the reward component Rrel t through Ψ(·), thereby encouraging
reliability feasible and risk aware portfolio decisions.
5.2 Proximal Policy Optimization (PPO) Agent
The proposed MORP–DRL framework employs a PPO-based Actor–Critic architecture consisting of a policy network
(Actor) and a value network (Critic). The Actor generates portfolio allocation decisions, while the Critic estimates the
expected cumulative reward of the current market state. The reward signal incorporates portfolio return improvement,
risk-adjusted performance, and reliability satisfaction, enabling the agent to learn reliability-aware portfolio strategies.
Since portfolio allocation involves continuous decision variables, PPO is adopted due to its effectiveness in continuous
action spaces and stable policy updates [37]. Policy optimization is performed using the clipped surrogate objective(2):
LCLIP(θ) =E t
h
min

rt(θ) ˆAt,clip(r t(θ),1−ϵ,1 +ϵ) ˆAt
i
−c 1LV F+c 2H(2)
where rt(θ) = πθ(at|st) πθold (at|st) denotes the policy probability ratio between the updated and previous policies, and ˆAt
represents the estimated advantage function. The clipping operation limits excessively large policy updates and
improves training stability. Here, LV F=E t[(Vϕ(st)−G t)2] denotes the value function (critic) loss, which minimizes
the prediction error between the estimated state value and the discounted return, whileH denotes the policy entropy that
encourages exploration and prevents premature convergence. The coefficients c1 and c2 control the relative importance
of the value loss and entropy regularization, respectively. Algorithm 1 outlines the complete training procedure of the
proposed MORP–DRL framework. The overall workflow of the proposed PPO-based portfolio optimization model is
illustrated in Figure 1.
6 Experiments
6.1 Data Collection and Pre-processing
The empirical analysis was conducted using a diversified set of major global equity market indices representing different
geographic regions and economic environments. The dataset includes the NIFTY 50 (India), S&P 500 (United States),
8

APREPRINT- JULY9, 2026
Figure 1: Workflow of the Proposed PPO-Based Portfolio Optimization Model
FTSE 100 (United Kingdom), DAX (Germany), Nikkei 225 (Japan), SSE Composite (China), Hang Seng Index (Hong
Kong), KOSPI (South Korea), CAC 40 (France), and ASX 200 (Australia). The inclusion of these indices enables the
proposed framework to capture heterogeneous market dynamics and evaluate portfolio behavior under varying economic
conditions. In addition to the index-level experiments, a separate large-scale portfolio optimization experiment was
conducted using the constituent stocks of the FTSE 100 index in order to assess the scalability and robustness of the
proposed methodology in higher-dimensional portfolio settings. Historical daily market data were collected using
the yfinance API. The analysis period spans from January 2018 to December 2023 and is divided into three distinct
market regimes. The first period, referred to as thePre-COVIDregime, covers January 2018 to December 2019 and
represents relatively stable market conditions prior to the pandemic. The second period corresponds to theCOVID
regime (January 2020 to December 2021), characterized by higher volatility and significant market disruptions caused
by the global pandemic. The final period, denoted as thePost-COVIDregime, spans January 2022 to December
2023 and captures the subsequent market recovery and stabilization phase.Daily closing prices were transformed into
logarithmic returns to ensure time-additive return aggregation. The log-return of asset i at time t is computed as
ri,t = ln

Pi,t
Pi,t−1

, where Pi,t denotes the closing price of asset i at time t. Financial return series typically exhibit
volatility clustering and conditional heteroskedasticity. To model these characteristics, a GARCH(1,1) model was fitted
to the return series of each asset. The GARCH framework enables time-varying estimation of conditional volatility
and provides a more realistic representation of financial market dynamics. To capture extreme market movements and
tail-risk behavior, Extreme Value Theory (EVT) was employed. In particular, excess losses beyond the 95th percentile
threshold were modeled using the Generalized Pareto Distribution (GPD). This approach facilitates more reliable
estimation of downside risk measures such as CVaR and EVaR, which are incorporated within the proposed portfolio
optimization framework. Expected asset returns were estimated using bootstrap resampling in order to account for
sampling uncertainty. For each asset, 1000 bootstrap samples were generated from the historical return distribution, and
the mean of the resampled returns was used as the expected return estimate. The resulting values were annualized for
consistency with the portfolio evaluation metrics.Portfolio risk was estimated using the empirical covariance matrix of
daily returns. To obtain annualized risk estimates, the covariance matrix was scaled by a factor of 252.
9

APREPRINT- JULY9, 2026
Algorithm 1PPO-Based Reliability-Aware Multi-objective Portfolio Optimization
1: Initialize policy networkπ θ(a|s)and value networkV ϕ(s)
2: Initialize PPO hyperparameters(η, ϵ, γ)
3: Set reliability thresholdsβ 1, β2
4: Define portfolio boundsw i,min, wi,max
5:foreach training episodedo
6: Generate market scenarios using GARCH(1,1), EVT,t-copula, and QMC
7: Observe initial states 0 = [p0,I 0,w −1, c0]
8: Initialize trajectory bufferD
9:fort= 0,1, . . . , T−1do
10: Sample action:a t ∼Dirichlet(π θ(st))
11: Project portfolio weights onto feasible simplex:w i,min ≤w i,t ≤w i,max, PN i=1 wi,t = 1
12: Execute action and observe next states t+1
13: Compute net returnR t =w ⊤ t µt −T Ct
14: Compute risk measureR t ∈ {Variance,CVaR,EVaR}
15: Estimate reliability probabilities:ρ ret t , ρrisk t
16: Compute rewardr t using Eq. (1)
17: Store(s t, at, rt, st+1)inD
18: Sets t ←s t+1
19:end for
20: Compute discounted cumulative returns:G t = PT−t k=0 γkrt+k
21: Estimate advantages ˆAt =G t −V ϕ(st)
22:foreach PPO update epochdo
23: Compute policy ratior t(θ) = πθ (at|st) πθold (at|st)
24: Update using clipped objective Eq. (2)
25: Update policy and value networks
26:end for
27:end for
28: Return trained policy networkπ θ
6.2 Experimental Setup
The proposed framework is evaluated under practical portfolio constraints, where the asset weights satisfy
0.03≤w i ≤0.35,
NX
i=1
wi = 1,
with reliability thresholds fixed at β1 =β 2 = 0.65. Portfolio rebalancing incorporates proportional transaction costs of
2 basis points at each trading step based on changes in portfolio weights between consecutive periods. The PPO agent
adopts an actor–critic architecture and is trained using the AdamW optimizer with a learning rate of 3×10 −4. The
discount factor and clipping parameter are set to γ= 0.99 and ϵ= 0.2 , respectively, and the agent is trained for 1000
episodes using the PPO clipped surrogate objective ( 2).
6.3 Benchmarks and Performance Evaluation
The proposed PPO framework is compared with two benchmark strategies: (i) an equal-weighted (EW) portfolio,
wherew i = 1/Nfor all assets, and (ii) an NSGA-II optimized portfolio solved under the same return, risk, reliability,
transaction cost, budget, and bound constraints. Performance is evaluated across the Pre-COVID, COVID, and Post-
COVID market regimes using return, volatility, Sharpe ratio, and the corresponding risk measure (Variance, CVaR,
or EVaR). In addition, Pareto frontiers are constructed for all optimization models to analyze the trade-off between
expected portfolio return and the selected risk measure.
6.3.1 Performance Metrics
The performance of the proposed MORP-DRL framework and benchmark strategies is evaluated using several standard
portfolio performance measures. These metrics assess not only profitability, but also the associated risk, downside
exposure, and computational efficiency of the portfolio optimization framework under different market regimes.
Scalability to FTSE100 Constituents:To ensure scalability in high-dimensional portfolio settings, we modify
the original quasi-Monte Carlo (QMC) t-copula scenario generation procedure. The baseline approach constructs a
10

APREPRINT- JULY9, 2026
single Sobol sequence over the full joint space of assets and time, resulting in a dimensionality of N×T , which
quickly exceeds the practical limits of Sobol sequences (≈ 21,201 dimensions) for large portfolios. To address this, we
adopt a time-decomposed QMC strategy, wherein Sobol sequences are generated independently at each time step with
dimensionalityN, and subsequently transformed via a Student-t copula using Cholesky-based correlation embedding.
This approach preserves cross-sectional dependence across assets while significantly reducing computational complexity
and avoiding high-dimensional degeneration of low-discrepancy sequences. Although this introduces an approximation
by relaxing inter-temporal dependence, it enables efficient and stable scenario generation for large-scale portfolios such
as FTSE 100, making it well-suited for reinforcement learning-based optimization frameworks.
7 Results and Discussion
Tables 1-3 together with the corresponding Pareto frontiers provide a detailed comparison between the baseline portfolio,
NSGA-II optimization, and PPO-based reinforcement learning optimization under different market regimes and risk
measures.
Variance-Based Portfolio Optimization (Model A).Table 1 together with Figures 2–3 summarizes the performance
of the variance-based portfolio optimization framework across the three market regimes. In all periods, both NSGA-
II and PPO produce portfolios that outperform the equal-weight benchmark, demonstrating the effectiveness of
optimization based on the mean-variance criterion. During the Pre-COVID period, NSGA-II achieves the highest
annualized return (19.63%) together with the highest Sharpe ratio (2.231), whereas PPO attains slightly lower volatility
(8.61%) and portfolio variance (0.0074). As shown in Figures 2 and 3, the Pareto frontiers are concentrated within a
low-variance region, reflecting the relatively stable market conditions. During the COVID period, the Pareto frontiers
shift towards portfolios with substantially higher expected returns accompanied by increased variance, illustrating the
elevated market uncertainty. NSGA-II marginally outperforms PPO by achieving the highest return (29.58%), the
highest Sharpe ratio (1.894), and the lowest portfolio variance (0.0244), while PPO provides comparable performance
with only a slight increase in risk. In the Post-COVID period, the feasible return–variance region becomes narrower
than during the pandemic, indicating a smaller range of attainable risk-return trade-offs. PPO achieves the highest
annualized return (13.08%), whereas NSGA-II maintains lower volatility, lower portfolio variance, and the highest
Sharpe ratio (1.250), indicating superior risk adjusted performance. In all three market regimes, the optimized portfolios
clearly dominate the equal-weight benchmark in terms of return-risk characteristics. NSGA-II consistently provides
stronger risk-adjusted performance under the variance objective, whereas PPO generates competitive portfolios with
only marginal differences in return and risk.
CVaR-Based Portfolio Optimization (Model B):Table 2 together with Figures 4–5 summarizes the performance of
the CVaR-based portfolio optimization model, where Conditional Value-at-Risk (CVaR) is used to explicitly control
downside tail risk. Across all three market regimes, both NSGA-II and PPO substantially outperform the equal-weight
benchmark in terms of return and risk-adjusted performance, demonstrating the effectiveness of incorporating downside-
risk considerations into portfolio optimization. During the Pre-COVID period, NSGA-II achieves the highest Sharpe
ratio (2.249) while maintaining the lowest CVaR (0.2281), indicating the most favorable balance between return and
downside risk. PPO attains a comparable annualized return (19.57%) but with slightly higher volatility and CVaR.
As illustrated in Figures 4a and 5a, the Pareto frontiers are concentrated within a relatively narrow return-CVaR
region, reflecting the comparatively stable market environment. During the COVID period, the Pareto frontiers shift
towards portfolios with substantially higher expected returns accompanied by increased downside risk, illustrating
the challenging market conditions. PPO identifies the highest-return portfolio (33.28%), but this improvement is
accompanied by the highest CVaR (0.4601). In contrast, NSGA-II achieves the highest Sharpe ratio (1.914) with a
lower CVaR (0.4462), providing a more balanced trade-off between return and downside risk. Moreover, the PPO
Pareto frontier spans a wider range of return-CVaR combinations, indicating greater flexibility in generating portfolios
corresponding to different levels of downside-risk tolerance. In the Post-COVID period, the Pareto frontiers become
more concentrated than during the pandemic, suggesting a narrower range of feasible return-risk trade-offs. NSGA-II
marginally outperforms PPO in annualized return (13.88% versus 13.64%), Sharpe ratio (1.277 versus 1.241), and
CVaR (0.2912 versus 0.2935), although the differences between the two approaches are relatively small. In all three
market regimes, both optimization methods produce portfolios that dominate the equal-weight benchmark by achieving
superior return-risk characteristics. The results indicate that NSGA-II consistently produces portfolios with lower
downside risk and better risk-adjusted performance under the CVaR objective, whereas PPO exhibits greater flexibility
by identifying higher return portfolios during periods of elevated market uncertainty, albeit at the expense of increased
tail risk.
11

APREPRINT- JULY9, 2026
EVaR-Based Portfolio Optimization (Model C):Table 3 together with Figures 6–7 presents the performance of the
EVaR-based portfolio optimization model, where Entropic Value-at-Risk (EVaR) provides a conservative measure of
downside risk by emphasizing extreme loss events. Across all market regimes, both NSGA-II and PPO outperform the
equal-weight benchmark, although they exhibit different risk-return characteristics. During the Pre-COVID period,
NSGA-II identifies the highest-return portfolio (22.36%), whereas PPO achieves the highest Sharpe ratio (2.241)
by substantially reducing portfolio volatility. Figures 6a and 7a show that both methods generate Pareto-efficient
portfolios that clearly dominate the equal-weight benchmark. During the COVID period, the Pareto frontiers shift
toward portfolios with higher expected returns, reflecting the increased downside risk associated with market uncertainty.
NSGA-II achieves the highest annualized return (33.55%) together with the highest Sharpe ratio (1.906), while PPO
produces portfolios with lower volatility, indicating a more conservative risk profile despite a modest reduction in
return. The broader range of feasible portfolios obtained by PPO suggests greater flexibility in exploring different
return-risk trade-offs under stressed market conditions. In the Post-COVID period, the performance differences between
the two methods become smaller. NSGA-II continues to achieve the highest annualized return (14.42%), whereas
PPO maintains lower portfolio volatility and attains the highest Sharpe ratio (1.251), indicating superior risk-adjusted
performance. In all three market regimes, both optimization approaches substantially outperform the equal-weight
benchmark. The EVaR based results reveal a consistent trade-off between return maximization and conservative risk
management. NSGA-II prioritizes higher expected returns, whereas PPO consistently favors lower portfolio volatility
and improved risk-adjusted performance.
Comparative Behaviour of NSGA-II and PPO:Across the three risk measures and market regimes, NSGA-II and
PPO exhibit distinct optimization characteristics. NSGA-II generally achieves stronger risk adjusted performance,
consistently requiring substantially lower computational time while producing Pareto-efficient portfolios with com-
petitive or superior returns across most experimental settings. PPO, although computationally more expensive due to
repeated policy updates and environment interactions, produces portfolios with performance comparable to NSGA-II
and, in several cases, attains either the highest annualized return (e.g., the CVaR-based COVID scenario and the
variance-based Post-COVID scenario) or the highest Sharpe ratio (under the EVaR formulation during the Pre-COVID
and Post-COVID periods). During periods of elevated market uncertainty, particularly under the EVaR framework,
PPO tends to favour portfolios with lower volatility, whereas NSGA-II more frequently identifies portfolios with
higher expected returns. Across all experiments, both optimization methods consistently outperform the equal-weight
benchmark, demonstrating the effectiveness of multi-objective optimization for portfolio selection. NSGA-II offers
a computationally efficient optimization strategy with strong and consistent risk-adjusted performance, while PPO
provides a competitive learning-based alternative capable of adapting portfolio decisions through interaction with the
market environment.
The differences in optimization behaviour are further illustrated by the portfolio allocation results reported in Appendix
A (Tables A1–A3), which present the optimal asset weights under the variance, CVaR, and EVaR formulations across
the three market regimes.
FTSE100 Scalability Results:The FTSE100 experiments demonstrate that the proposed framework remains effective
in high-dimensional portfolio optimization settings. As summarized in Table 4, both PPO and NSGA-II consistently
outperform the equal-weight benchmark across all three market regimes and risk measures, confirming the scalability
of the proposed optimization framework to a larger asset universe. Under the variance formulation, NSGA-II achieves
the highest Sharpe ratios in all market regimes, exceeding 2.0 throughout the study, while PPO also provides substantial
improvements over the baseline. Similar trends are observed under the CVaR and EVaR formulations, where both opti-
mization methods consistently achieve higher Sharpe ratios than the equal-weight portfolio, with NSGA-II maintaining
the strongest risk-adjusted performance across all periods. Although PPO does not surpass NSGA-II in terms of Sharpe
ratio, it consistently delivers competitive performance while employing a learning-based optimization strategy. These
results demonstrate that both approaches scale effectively to large portfolio optimization problems, with NSGA-II
providing superior risk-adjusted performance and computational efficiency, whereas PPO offers a flexible reinforcement
learning framework capable of adapting portfolio allocation policies as market conditions evolve.
Additional portfolio concentration statistics are reported in Appendix A (Tables A4, A6, and A7). These results show
that NSGA-II generally allocates a larger proportion of portfolio weight to a smaller subset of assets, whereas PPO
distributes weights across a larger number of assets, leading to more diversified portfolio allocations. This behaviour is
consistent across the variance, CVaR, and EVaR formulations and provides further evidence of the distinct optimization
characteristics of the two approaches in high-dimensional portfolio settings.
12

APREPRINT- JULY9, 2026
Model A
Table 1: Portfolio Performance Comparison Across Market Regimes — Variance Risk Measure
Period Method Return V olatility Sharpe Variance CPU Time
Pre-COVID
Base Portfolio 0.1511 0.0949 1.591 0.0090 –
NSGA-II Optimized0.19630.08802.2310.007758.0s
DRL (PPO) Optimized 0.19180.08612.2260.0074848.3s
COVID
Base Portfolio 0.2338 0.1559 1.499 0.0243 –
NSGA-II Optimized0.2958 0.1562 1.894 0.0244 57.2s
DRL (PPO) Optimized 0.2952 0.1572 1.878 0.0247 848.7s
Post-COVID
Base Portfolio 0.0705 0.1116 0.632 0.0125 –
NSGA-II Optimized 0.13030.1043 1.250 0.0109 63.0s
DRL (PPO) Optimized0.13080.1056 1.239 0.0112 832.4s
Model B
Table 2: Portfolio Performance Comparison Across Market Regimes — CVaR Risk Measure
Period Method Return V olatility Sharpe CVaR CPU Time
Pre-COVID
Base Portfolio 0.1511 0.0949 1.591 0.2502 –
NSGA-II Optimized0.1958 0.0871 2.249 0.2281 303.4s
DRL (PPO) Optimized 0.1957 0.0887 2.206 0.2320 725.1s
COVID
Base Portfolio 0.2338 0.1559 1.499 0.4136 –
NSGA-II Optimized 0.32690.1708 1.914 0.4462 304.6s
DRL (PPO) Optimized0.33280.1754 1.897 0.4601 730.8s
Post-COVID
Base Portfolio 0.0705 0.1116 0.631 0.3028 –
NSGA-II Optimized0.1388 0.1087 1.277 0.2912 305.2s
DRL (PPO) Optimized 0.1364 0.1099 1.241 0.2935 725.8s
Model C
Table 3: Portfolio Performance Comparison Across Market Regimes — EVaR Risk Measure
Period Method Return V olatility Sharpe EVaR CPU Time
Pre-COVID
Base Portfolio 0.1511 0.0949 1.591 4.750728 –
NSGA-II Optimized0.22360.1095 2.041 4.74779873.96s
DRL (PPO) Optimized 0.19120.0853 2.241 0.0013356.8s
COVID
Base Portfolio 0.2338 0.1559 1.499 4.753522 –
NSGA-II Optimized0.33550.17601.9064.75067069.23s
DRL (PPO) Optimized 0.32190.17051.8880.0073351.5s
Post-COVID
Base Portfolio 0.0705 0.1116 0.631 4.757576 –
NSGA-II Optimized0.14420.1230 1.172 4.75425967.82s
DRL (PPO) Optimized 0.13320.1064 1.251 0.0124352.9s
13

APREPRINT- JULY9, 2026
(a) Pre COVID
 (b) COVID
(c) Post COVID
Figure 2: NSGA-II based Pareto frontiers under the Variance risk measure for (a) Pre COVID, (b) COVID, and (c) Post
COVID periods.
Table 4: FTSE100 Performance Comparison Across Risk Measures
Risk Measure Period Baseline PPO NSGA-II
Variance
Pre-COVID 0.959 1.3642.328
COVID 0.607 1.1222.105
Post-COVID 0.645 0.9712.301
CVaR
Pre-COVID 0.974 1.3291.926
COVID 0.607 1.0281.202
Post-COVID 0.645 1.0561.410
EVaR
Pre-COVID 0.959 1.5352.214
COVID 0.607 1.0571.929
Post-COVID 0.645 1.0812.211
14

APREPRINT- JULY9, 2026
(a) Pre COVID
 (b) COVID
(c) Post COVID
Figure 3: PPO based Pareto frontiers under the Variance risk measure for (a) Pre COVID, (b) COVID, and (c) Post
COVID periods.
15

APREPRINT- JULY9, 2026
(a) Pre COVID
 (b) COVID
(c) Post COVID
Figure 4: NSGA-II based Pareto frontiers under the CVaR risk measure for (a) Pre COVID, (b) COVID, and (c) Post
COVID periods.
16

APREPRINT- JULY9, 2026
(a) Pre COVID
 (b) COVID
(c) Post COVID
Figure 5: Pareto frontiers obtained using PPO under the CVaR risk measure for (a) Pre COVID, (b) COVID, and (c)
Post COVID periods.
17

APREPRINT- JULY9, 2026
(a) Pre COVID
 (b) COVID
(c) Post COVID
Figure 6: Pareto frontiers obtained using NSGA-II under the EVaR risk measure for (a) Pre COVID, (b) COVID, and
(c) Post COVID periods.
18

APREPRINT- JULY9, 2026
(a) Pre COVID
 (b) COVID
(c) Post COVID
Figure 7: Pareto frontiers obtained using PPO under the EVaR risk measure for (a) Pre COVID, (b) COVID, and (c)
Post COVID periods.
19

APREPRINT- JULY9, 2026
8 Conclusion and Future Work
This paper proposes a bi-objective reliability-based portfolio optimization framework in which portfolio allocation is
learned as a sequential decision making problem using deep reinforcement learning. The framework jointly optimizes
expected return and downside risk while accounting for market uncertainty, transaction costs, and reliability constraints
under realistic financial conditions. The empirical study, conducted on ten major global equity indices across the pre-
COVID, COVID, and post-COVID periods, demonstrates that the PPO-based policy consistently produces competitive
risk-return portfolios and adapts effectively to changing market regimes. The results show that the framework provides
improved control of downside and extreme-tail risk under the CVaR and EVaR formulations, leading to more stable
portfolio performance during periods of market stress. Pareto frontier analysis further indicates that the learned
policies achieve an effective balance between return maximization and risk minimization while satisfying the prescribed
reliability constraints. Comparison with NSGA-II shows a clear trade-off between the two optimization approaches.
NSGA-II is computationally efficient and often attains higher returns through concentrated portfolio allocations,
whereas PPO learns adaptive and more diversified investment strategies that respond effectively to evolving market
conditions. The framework also scales effectively to high-dimensional portfolio optimization, as demonstrated on
the FTSE100 constituent stocks using a modified time decomposed quasi-Monte Carlo Student-t copula for efficient
scenario generation. Future research may extend the framework to dynamic multi-period portfolio optimization,
incorporate additional market frictions such as liquidity and price impact, and investigate hybrid reinforcement
learning and evolutionary optimization methods for large-scale portfolio selection. Further improvements may include
integrating macroeconomic indicators, news sentiment, and alternative data sources to enable more informed portfolio
decisions under rapidly changing market conditions. The use of multi-agent reinforcement learning and distributional
reinforcement learning may also provide improved modeling of market interactions and uncertainty. Finally, extending
the framework to multi-asset portfolios comprising equities, fixed income securities, commodities, and cryptocurrencies
would further enhance its practical applicability for real-world investment management.
References
[1] Harry Markowitz. Portfolio selection.The Journal of Finance, 7(1):77–91, 1952.
[2] Frank J Fabozzi, Harry M Markowitz, and Francis Gupta. Portfolio selection.Handbook of finance, 2:3–13, 2008.
[3] Eugene F Fama and Kenneth R French. The capital asset pricing model: Theory and evidence.Journal of
economic perspectives, 18(3):25–46, 2004.
[4] Thomas J Linsmeier and Neil D Pearson. Value at risk.Financial analysts journal, 56(2):47–67, 2000.
[5] R Tyrrell Rockafellar and Stanislav Uryasev. Conditional value-at-risk for general loss distributions.Journal of
banking & finance, 26(7):1443–1471, 2002.
[6] Henrique Pinto Ramos, Marcelo Brutti Righi, Pablo Cristini Guedes, and Fernanda Maria Müller. A comparison
of risk measures for portfolio optimization with cardinality constraints.Expert Systems with Applications,
228:120412, 2023.
[7] Marcelo Brutti Righi and Denis Borenstein. A simulation comparison of risk measures for portfolio optimization.
Finance Research Letters, 24:105–112, 2018.
[8] Zi Loke, Say Leng Goh, Graham Kendall, Salwani Abdullah, and Nasser Sabar. Portfolio optimisation problem:
A taxonomic review of solution methodologies.IEEE Access, PP:1–1, 01 2023.
[9] Ahti Salo, Michalis Doumpos, Juuso Liesiö, and Constantin Zopounidis. Fifty years of portfolio optimization.
European Journal of Operational Research, 318(1):1–18, 2024.
[10] Okkes Ertenlice and Can B Kalayci. A survey of swarm intelligence for portfolio optimization: Algorithms and
applications.Swarm and evolutionary computation, 39:36–52, 2018.
[11] Ian Goodfellow, Yoshua Bengio, Aaron Courville, and Yoshua Bengio.Deep learning, volume 1. MIT press
Cambridge, 2016.
[12] Thomas Fischer and Christopher Krauss. Deep learning with long short-term memory networks for financial
market predictions.European journal of operational research, 270(2):654–669, 2018.
[13] Jyotirmayee Behera, Ajit Kumar Pasayat, Harekrushna Behera, and Pankaj Kumar. Prediction based mean-value-
at-risk portfolio optimization using machine learning regression algorithms for multi-national stock markets.
Engineering Applications of Artificial Intelligence, 120:105843, 2023.
[14] Kai Arulkumaran, Marc Peter Deisenroth, Miles Brundage, and Anil Anthony Bharath. Deep reinforcement
learning: A brief survey.IEEE signal processing magazine, 34(6):26–38, 2017.
20

APREPRINT- JULY9, 2026
[15] Himanshu Choudhary, Arishi Orra, Kartik Sahoo, and Manoj Thakur. Risk-adjusted deep reinforcement learning
for portfolio optimization: A multi-reward approach.International Journal of Computational Intelligence Systems,
18(1):126, 2025.
[16] Shihao Gu, Bryan Kelly, and Dacheng Xiu. Empirical asset pricing via machine learning.The Review of Financial
Studies, 33(5):2223–2273, 2020.
[17] Himanshu Choudhary, Arishi Orra, Manoj Thakur, Xiao-Zhi Gao, and Prabhat Kumar Sahu. A cvar-constrained
safe reinforcement learning framework with action repair for practical portfolio optimization.IEEE Transactions
on Artificial Intelligence, 2026.
[18] Harry Markowitz. Portfolio selection.The Journal of Finance, 7(1):77–91, 1952.
[19] Petter N Kolm, Reha Tütüncü, and Frank J Fabozzi. 60 years of portfolio optimization: Practical challenges and
current trends.European Journal of Operational Research, 234(2):356–371, 2014.
[20] Suraj S Meghwani and Manoj Thakur. Multi-objective heuristic algorithms for practical portfolio optimization
and rebalancing with transaction cost.Applied Soft Computing, 67:865–894, 2018.
[21] Huy Chau, Duy Nguyen, and Thai Nguyen. Continuous-time optimal investment with portfolio constraints: a
reinforcement learning approach.European Journal of Operational Research, 2025.
[22] Souradeep Chakraborty. Capturing financial markets to apply deep reinforcement learning.arXiv preprint
arXiv:1907.04373, 2019.
[23] Yuming Li, Pin Ni, and Victor Chang. Application of deep reinforcement learning in stock trading strategies and
stock forecasting.Computing, 2019.
[24] Ziming Gao, Yuan Gao, Yi Hu, Zhengyong Jiang, and Jionglong Su. Application of deep q-network in portfolio
management. In2020 5th IEEE International Conference on Big Data Analytics (ICBDA), pages 268–275. IEEE,
2020.
[25] Yuan Gao, Ziming Gao, Yi Hu, Sifan Song, Zhengyong Jiang, and Jionglong Su. A framework of hierarchical
deep q-network for portfolio management. InICAART (2), pages 132–140, 2021.
[26] Yifu Jiang, Jose Olmo, and Majed Atwi. Deep reinforcement learning for portfolio selection.Global Finance
Journal, 62:101016, 2024.
[27] Shaghayegh Abolmakarem, Farshid Abdi, Kaveh Khalili-Damghani, and Hosein Didehkhani. Predictive multi-
period multi-objective portfolio optimization based on higher order moments: Deep learning approach.Computers
& industrial engineering, 183:109450, 2023.
[28] Philip Ndikum and Serge Ndikum. Advancing investment frontiers: Industry-grade deep reinforcement learning
for portfolio optimization.arXiv preprint arXiv:2403.07916, 2024.
[29] Ruyu Yan, Jiafei Jin, and Kun Han. Reinforcement learning for deep portfolio optimization.Electronic Research
Archive, 32(9):5176, 2024.
[30] Junkyu Jang and NohYoon Seong. Deep reinforcement learning for stock portfolio optimization by connecting
with modern portfolio theory.Expert Systems with Applications, 218:119556, 2023.
[31] Pengqian Yu, Joon Sern Lee, Ilya Kulyatin, Zekun Shi, and Sakyasingha Dasgupta. Model-based deep reinforce-
ment learning for dynamic portfolio optimization.arXiv preprint arXiv:1901.08740, 2019.
[32] Raghu Nandan Sengupta, Aditya Gupta, Subhankar Mukherjee, and Gregor Weiss. Bi-objective reliability based
optimization: an application to investment analysis.Annals of Operations Research, 333(1):47–78, 2024.
[33] Weifei Hu, Sichuang Cheng, Jiquan Yan, Jin Cheng, Xiang Peng, Hyunkyoo Cho, and Ikjin Lee. Reliability-based
design optimization: a state-of-the-art review of its methodologies, applications, and challenges.Structural and
Multidisciplinary Optimization, 67(9):168, 2024.
[34] Raghu Nandan Sengupta, Rachit Seth, and Peter Winker. Reliability in portfolio optimization using uncertain
estimates.Sankhya B, 85(Suppl 1):199–233, 2023.
[35] P Jana, TK Roy, and SK Mazumder. Multi-objective possibilistic model for portfolio selection with transaction
cost.Journal of computational and applied mathematics, 228(1):188–196, 2009.
[36] Wei Chen. Artificial bee colony algorithm for constrained possibilistic portfolio optimization problem.Physica A:
Statistical Mechanics and its Applications, 429:125–139, 2015.
[37] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization
algorithms.ArXiv, abs/1707.06347, 2017.
21

APREPRINT- JULY9, 2026
A Appendix
Table A1: Portfolio Weights Comparison Across Market Regimes – Variance Optimization
Pre-COVID COVID Post-COVID
Asset NSGA-II PPO NSGA-II PPO NSGA-II PPO
SSE 3.0 6.7 25.7 7.3 3.0 3.0
ASX 34.5 29.6 4.3 9.7 3.1 15.1
CAC40 9.6 17.2 3.2 7.0 3.0 3.0
FTSE 6.2 3.0 3.0 3.0 35.0 17.8
DAX 3.0 3.0 3.0 3.0 3.0 13.4
S&P500 10.5 14.4 25.9 28.0 11.1 5.4
HSI 3.0 3.4 3.0 3.0 3.0 3.0
KOSPI 6.8 3.0 8.2 3.9 3.0 3.0
NIKKEI 3.0 5.8 6.2 4.1 3.0 6.7
NIFTY 20.4 14.1 17.5 31.0 32.8 29.6
Table A2: Portfolio Weights Comparison Across Market Regimes – CVaR Optimization
Pre-COVID COVID Post-COVID
Asset NSGA-II PPO NSGA-II PPO NSGA-II PPO
SSE 3.0 3.0 5.6 3.4 3.1 3.0
ASX 25.3 27.3 3.3 3.4 4.1 10.7
CAC40 22.5 31.7 3.0 3.4 4.0 3.0
FTSE 3.1 3.0 3.0 3.4 20.8 5.2
DAX 3.1 3.0 3.0 3.9 10.9 17.8
S&P500 21.2 11.9 32.5 35.0 13.3 16.1
HSI 3.0 3.0 3.0 3.4 3.0 3.0
KOSPI 3.0 5.3 9.3 3.4 3.0 3.0
NIKKEI 3.0 3.4 3.4 5.8 3.0 4.7
NIFTY 12.7 8.4 33.9 35.0 35.0 33.5
Table A3: Portfolio Weights Comparison Across Market Regimes – EVaR Optimization
Pre-COVID COVID Post-COVID
Asset NSGA-II PPO NSGA-II PPO NSGA-II PPO
SSE 3.0 3.3 3.0 3.0 3.0 3.0
ASX 3.0 32.7 3.0 14.4 3.0 9.7
CAC40 33.4 17.7 4.8 10.1 19.9 5.2
FTSE 3.0 3.0 3.2 3.0 3.0 21.0
DAX 11.7 3.0 3.2 3.0 34.9 6.6
S&P500 33.7 21.2 35.0 28.8 3.0 17.2
HSI 3.1 3.0 3.1 3.0 3.0 3.0
KOSPI 3.0 3.0 6.7 3.0 3.0 3.0
NIKKEI 3.1 3.0 3.0 3.0 3.0 3.2
NIFTY 3.0 10.1 35.0 28.6 24.3 28.2
22

APREPRINT- JULY9, 2026
Table A4: Portfolio Concentration and Weight Distribution(FTSE 100 Variance Risk Measure)
Period Method Top 10 (%) Top 20 (%) Top 50 (%)w >1%Max (%) Min (%)
Pre-COVID
PPO 36.56 55.26 88.66 38 8.54 0.10
NSGA-II 64.49 86.42 95.23 22 10.00 0.10
Baseline 10.00 20.00 50.00 97 1.03 1.03
COVID
PPO 43.77 64.32 90.90 32 7.88 0.10
NSGA-II 66.08 84.97 94.85 20 9.89 0.10
Baseline 10.00 20.00 50.00 99 1.01 1.01
Post-COVID
PPO 39.26 59.38 89.10 31 5.45 0.10
NSGA-II 69.70 86.37 94.88 19 10.02 0.10
Baseline 10.00 20.00 50.00 99 1.01 1.01
Table A5: Top 10 Holdings (PPO Optimized Portfolio)
Rank Pre-COVID Weight (%) COVID Weight (%) Post-COVID Weight (%)
1 RTO 8.54 HLMA 7.88 UU 5.45
2 3IN 3.72 FCIT 5.09 TSCO 5.44
3 DPLM 3.69 SMT 4.56 WPP 5.02
4 HWDN 3.66 EXPN 4.42 WEIR 3.98
5 SPX 3.56 NG 4.35 SSE 3.85
6 SGRO 3.12 BRBY 3.89 A V 3.27
7 HSX 2.97 CNA 3.56 MNDI 3.26
8 SHEL 2.49 SGRO 3.52 CCH 3.05
9 SGE 2.48 AUTO 3.32 BA 3.04
10 ULVR 2.34 GLEN 3.20 SMIN 2.91
Table A6: Portfolio Concentration and Weight Distribution (FTSE100 CVaR Risk Measure)
Period Method Top 10 (%) Top 20 (%) Top 50 (%)w >1%Max (%) Min (%)
Pre-COVID
PPO 34.99 55.75 88.21 37 4.90 0.10
NSGA-II 54.93 79.06 94.41 22 9.82 0.10
Baseline 10.00 20.00 50.00 97 1.03 1.03
COVID
PPO 38.79 59.77 86.35 27 7.06 0.10
NSGA-II 45.24 67.19 93.25 29 8.04 0.10
Baseline 10.00 20.00 50.00 99 1.01 1.01
Post-COVID
PPO 42.71 62.11 89.78 31 8.14 0.10
NSGA-II 60.61 78.99 94.39 24 10.08 0.10
Baseline 10.00 20.00 50.00 99 1.01 1.01
23

APREPRINT- JULY9, 2026
Table A7: Portfolio Concentration and Diversification Analysis(FTSE100 EVaR Risk Measure)
Period Method Top 10 (%) Top 20 (%) Top 50 (%) w>1% Max (%) Min (%)
Pre-COVID
NSGA-II 57.72 77.32 94.88 26 9.80 0.10
PPO 42.84 63.94 91.77 31 9.65 0.10
Base 10.00 20.00 50.00 97 1.03 1.03
COVID
NSGA-II 62.27 81.44 94.30 20 10.10 0.10
PPO 44.58 61.53 89.36 34 8.97 0.10
Base 10.00 20.00 50.00 99 1.01 1.01
Post-COVID
NSGA-II 59.73 82.53 94.39 23 10.03 0.10
PPO 36.53 59.88 92.08 34 5.35 0.10
Base 10.00 20.00 50.00 99 1.01 1.01
24
