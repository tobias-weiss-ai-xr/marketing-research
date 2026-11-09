---
title: Addressing Market Regime Changes and Heavy-Tailed Returns in Portfolio Optimization via Bayesian
  VAR and Elliptical Black-Litterman
url: https://arxiv.org/abs/2606.09104
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors: []
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.09104
pages: 9
chars: 45414
fetched_at: '2026-11-08T13:03:04+00:00'
kb_version: 1
---

# Addressing Market Regime Changes and Heavy-Tailed Returns in Portfolio Optimization via Bayesian VAR and Elliptical Black-Litterman

Addressing Market Regime Changes and Heavy-Tailed Returns in Portfolio
Optimization via Bayesian V AR and Elliptical Black-Litterman
Daniil Mikriukov1,2 ,Ruoyu Sun 2 ,Angelos Stefanidis 2 ,Jionglong Su 2 ,Zhengyong Jiang 2
1Department of Computer Science, University of Liverpool, Liverpool, United Kingdom
2School of AI and Advanced Computing, Xi’an Jiaotong-Liverpool University, Suzhou, China
D.Mikriukov@liverpool.ac.uk, fiez0303@outlook.com, angelos.stefanidis@xjtlu.edu.cn,
jionglong.su@xjtlu.edu.cn, zhengyong.jiang02@xjtlu.edu.cn
Abstract
Deep reinforcement learning (DRL) frameworks
for portfolio optimization have shown promise
for their ability to learn allocation rules dynam-
ically from market data. However, these mod-
els fail to account for fat-tailed returns, which
characterize actual market behavior with more fre-
quent extreme events. Furthermore, historical data
is treated homogeneously, without accounting for
temporal importance, leading models to fail dur-
ing regime changes. We propose a new BA V AR-
BLED algorithm that combines methods derived
from Bayesian-Averaging Vector Autoregressive
(BA V AR) and the Black-Litterman model using El-
liptical Distributions (BLED) within a TD3 archi-
tecture. BA V AR captures a set of vector autore-
gressive representations that consider multi-scale
temporal features, enabling adaptive allocation de-
cisions based on regime-aware estimates of return
expectations and dispersion matrices. These esti-
mates serve as prior inputs to BLED, a model that
uses Student’st-distributions, allowing for more
realistic fat tail return estimates. The BA V AR-
BLED algorithm uses transformer networks for
view construction and CNNs for risk-aversion es-
timates, which modify dynamic allocation deci-
sions based on market conditions. An evaluation
of 29 Dow Jones Industrial Average constituents
over a decade-long market period shows that
BA V AR-BLED significantly outperforms state-of-
the-art methods, achieving Sharpe and Sortino ra-
tios of 1.72 and 2.70, respectively, and total returns
of 57.26%.
1 Introduction
Portfolio optimization (PO) is a well-known problem in quan-
titative finance, where investors have to balance expected re-
turns against associated risks. One of the earliest works in this
field belongs to Markowitz with his mean-variance frame-
work [1952]. While it remains quite influential in PO, its high
sensitivity to estimation errors in the sample mean and co-
variance matrix often leads to unstable portfolio allocations,
particularly during market stress when correlations increase
and historical estimates become unreliable.
Recent advances in deep reinforcement learning (DRL)
demonstrate great potential for adaptive portfolio manage-
ment, as agents can directly learn to make allocation de-
cisions purely from market data by continuously captur-
ing and adapting to market conditions [Jianget al., 2017;
Fischer and Krauss, 2018 ]. However, the majority of ex-
isting DRL frameworks for PO fail to account for the well-
documented fat-tailed nature of financial returns [Officer,
1972; Kringet al., 2009; Koldanov, 2019 ], which leads to an
underestimation of tail risks and potentially significant losses
during market turbulence.
The Black-Litterman model addresses the mean-variance’s
estimation error by combining market equilibrium returns
with investor views inside of the Bayesian framework [Black
and Litterman, 1992]. More recent work by Xiao and Valdez
further generalized this framework to elliptical distributions
to more realistically model heavy-tailed returns [2015]. In
our prior work [Mikriukovet al., 2025 ], we introduced
the Black-Litterman under Elliptical Distributions (BLED)
framework, which embeds this elliptical extension into a
transformer-based DRL agent and demonstrated improved
risk-adjusted performance compared to both traditional meth-
ods and standard DRL models. However, BLED still faces a
fundamental limitation during regime changes when comput-
ing the market prior (the expected return vector derived from
market equilibrium) and dispersion matrix (the generalization
of covariance that captures return co-movements under ellip-
tical distributions) by treating the historical data uniformly,
whereas recent observations should carry more weight than
distant ones.
To address this limitation, we propose a novel BA V AR-
BLED framework that integrates Bayesian-Averaging Vec-
tor Autoregressive (BA V AR) methods with our BLED frame-
work inside a DRL agent, where the first component is based
on the methodology of Anderson and Cheng and maintains
an ensemble of heterogeneous V AR models that are contin-
uously updated via Bayesian learning [2022]. This ensem-
ble replaces the static historical estimates used in standard
BLED with adaptive ones for expected returns and disper-
sion matrix that respond to regime changes. Furthermore,
to capture multi-scale temporal dynamics and to incorporate
information from daily, weekly and monthly return patterns,
arXiv:2606.09104v1  [cs.LG]  8 Jun 2026

our framework utilizes Heterogeneous Autoregressive (HAR)
features [Corsi, 2009].
The four key contributions of this paper are as follows:
• To the best of our knowledge, we are first to propose
the integration of BA V AR methodology with our BLED
framework inside a DRL agent, providing adaptive mar-
ket prior and dispersion estimation that responds to
regime changes.
• We also show the significant improvement of the port-
folio performance during volatile market periods by the
addition of adaptive BA V AR-derived priors in compari-
son with static ones.
• Validation on 29 stocks from the DJIA from 2014
to 2024 is conducted, where we demonstrate the out-
performance of state-of-the-art methods by the pro-
posed BA V AR-BLED framework, which achieves supe-
rior risk-adjusted performance (Sharpe ratio of 1.72 and
Sortino ratio of 2.70).
• Lastly, we conduct comprehensive ablation studies,
where the individual contribution of each component to
overall performance is demonstrated.
Our framework operates under standard assumptions for
portfolio optimization: trading at adjusted closing prices,
fractional shares permitted, zero market impact, immediate
execution without slippage, and a transaction cost of 0.25%
per rebalance, which is calibrated for a $100,000 USD port-
folio trading liquid US equities [Frazziniet al., 2018 ]. Short
selling is also permitted in our simulated environment.
2 Related Work
2.1 Deep Reinforcement Learning for Portfolio
Optimization
Deep reinforcement learning has gained significant attention
for portfolio management due to its ability to learn com-
plex decision policies from data [Gaoet al., 2020; Songet
al., 2023 ]. Jianget al.introduced the Ensemble of Iden-
tical Independent Evaluators (EIIE) topology, using convo-
lutional neural networks to process price tensors and gener-
ate portfolio weights [2017]. Subsequent work has explored
various architectures including LSTM networks [Fischer and
Krauss, 2018 ], attention mechanisms [Yanget al., 2023 ],
and multi-agent systems [Shavandi and Khedmati, 2022;
Huang and Tanaka, 2022 ]. The Twin Delayed Deep Deter-
ministic Policy Gradient (TD3) algorithm [Fujimotoet al.,
2018] has also become quite a popular choice for continuous
action spaces in portfolio optimization due to its stability and
reduced overestimation bias. Besides that, recent applications
include risk-controlled portfolios [Jiang and Wang, 2022;
Choudharyet al., 2025 ] and hierarchical approaches [Gao
et al., 2021 ]. Transformer architectures have also shown
promise for capturing long-range dependencies in financial
time series [Yanget al., 2023; Liuet al., 2024b; Zhanget al.,
2024]. Despite these advances, most DRL methods fail to ac-
count for the heavy-tailed nature of financial returns, leading
to underestimation of tail risks.
2.2 Black-Litterman Model and Extensions
To address the fat-tailed nature of financial returns, Xiao and
Valdez extended the Black-Litterman model [Black and Lit-
terman, 1992 ] to elliptical distributions, thus allowing for
more realistic modeling of heavy-tailed returns through dis-
tributions such as the Student’st [2015].
Some recent works have integrated the Black-Litterman
framework with deep learning. For instance, Sunet al.
combined transformer-based DRL with the Black-Litterman
model for portfolio optimization [2024]. Our prior work
[Mikriukovet al., 2025 ] further extended this direction by
incorporating elliptical distributions (BLED) and combin-
ing transformer view generation with CNN-based risk aver-
sion estimation. Zhu and Yen had slightly different vision
and explored GAN-based view generation within the Black-
Litterman framework [2024]. However, these approaches
treat historical data uniformly when computing market priors,
which becomes rather problematic during regime changes
when recent observations should carry more weight.
2.3 Bayesian V AR Methods in Finance
Vector autoregressive models have a long history in financial
econometrics for modeling multivariate time series. Bayesian
approaches may be used to further improve them by provid-
ing natural uncertainty quantification and incorporating prior
knowledge about coefficient stability. Using this fact, Ander-
son and Cheng developed the BA V AR methodology, which
maintains an ensemble of V AR models with different hy-
perparameters and uses Bayesian model averaging to pro-
duce forecasts, thus making it well-suited for non-stationary
environments where model parameters may shift over time
[2022]. This approach further benefits from the Heteroge-
neous Autoregressive (HAR) model of Corsi that captures
multi-scale temporal dynamics by including lagged values
at different frequencies [2009]. HAR features were origi-
nally developed for realized volatility forecasting, but have
demonstrated their effectiveness for modeling various finan-
cial time series. Furthermore, the combination of these fea-
tures with Bayesian V AR methods enables models to capture
both short-term fluctuations and longer-term trends. Unlike
regime-switching models that require a predefined number of
regimes, BA V AR handles regime changes implicitly through
its ensemble structure, outputting adaptive priors that respond
to structural shifts.
2.4 Research Gap
Existing work in DRL-based portfolio optimization faces two
fundamental limitations. First, most approaches fail to ac-
count for the well-documented fat-tailed nature of financial
returns [Officer, 1972; Kringet al., 2009; Koldanov, 2019 ].
While our BLED framework [Mikriukovet al., 2025 ] ad-
dresses this by using elliptical distributions, it inherits a sec-
ond limitation: reliance on static historical estimates for mar-
ket priors, which becomes quite troublesome during regime
changes when asset relationships evolve.
Our BA V AR-BLED framework addresses both of the
aforementioned gaps within a unified architecture, where the
key innovation lies in the integration of Bayesian V AR meth-
ods with the elliptical Black-Litterman model, which pro-

vides adaptive, regime-aware prior estimates that respond to
changing market conditions while modeling heavy-tailed re-
turns more realistically.
3 Methodology
3.1 Framework Overview
Figure 1 illustrates the overall system design of the BA V AR-
BLED framework, which includes data preprocessing, three
parallel processing branches, Black-Litterman optimization,
and TD3 reinforcement learning. Here the raw price data for
29 DJIA constituent stocks is fetched from yfinance and pro-
cessed through feature engineering to extract 12 features per
asset: adjusted close price, volume, five exponential moving
averages (EMA10,20,50,100,200), MACD with signal line, RSI,
and Bollinger Bands, which produces a state tensor of shape
(29×15×12)that represent 29 assets over a 15-day win-
dow with 12 features each. The state tensor is then fed into
three parallel branches: (1) the BA V AR module extracts HAR
features and maintains an ensemble of 600 V AR models to
produce adaptive prior estimatesµand dispersion matrixD;
(2) a transformer encoder generates investor viewsQ; and
(3) a CNN estimates the risk aversion parameterδ. These
outputs are then used in the BLED calculation, which com-
putes Black-Litterman optimal weights under elliptical distri-
butions. Lastly, the model undergoes the TD3 training loop
through interactions with the environment.
3.2 MDP Formulation
We formulate the PO problem as a Markov Decision Process
(MDP) with continuous state and action spaces.
State Space.At each time stept, the states t ∈R n×w×f
represents a tensor of historical observations, wheren= 29
is the number of assets,w= 15is the lookback window in
trading days, andf= 12is the number of features per asset.
Features include adjusted close price, trading volume, and
exponential moving averages (EMA 10,20,50,100,200), MACD
with signal line, RSI, and Bollinger Bands.
Action Space.The actiona t ∈R n+1 represents target port-
folio weights fornassets plus a cash position. Also to enable
both long and short positions, we employ absolute-value nor-
malization to weights: Pn+1 i=1 |wi|= 1withw i ∈[−1,1], where negative weights represent short positions.
Reward Function.The reward is the logarithmic portfolio
return after transaction costs:
rt = log(Vt +ε)−log(V t−1 +ε),(1)
whereV t =V t−1 ·(1+r p)·(1−µ t)is the portfolio value after
returns and costs,r p = P i wi ·r i,t is the weighted portfolio
return,µ t =c· P i |wi,t −w i,t−1|is the transaction cost
proportional to turnover withc= 0.0025, andε= 10 −8
ensures numerical stability.
3.3 BA V AR Component
BA V AR maintains an ensemble of V AR models that update
continuously with new data, thereby providing adaptive esti-
mates of expected returns and dispersion matrix.
HAR Feature Extraction.Following Corsi [2009], we
construct multi-scale temporal features from asset returns:
xt−1 =
h
1,¯r(d) t−1,¯r(w) t−1,¯r(m) t−1
i⊤
,(2)
where superscriptsd,w, andmdenote daily, weekly, and
monthly scales respectively. Specifically,¯r (d) t−1 is the previ-
ous day’s return, while¯r(w) t−1 and¯r(m) t−1 represent returns aver-
aged over the previous 5 and 22 trading days. These features
capture both short-term momentum and medium-term mean
reversion patterns.
V AR Model Specification.We assume that asset returns
follow a time-varying coefficient V AR:
rt =B txt−1 +ϵ t,(3)
wherer t ∈R n are excess returns fornassets,B t is the true
(unobserved) coefficient matrix that may shift when regimes
change, andϵ t ∼ N(0,Σt). Each modelmin the ensem-
ble maintains a posterior estimate ¯Bm,t ofB t based on its
assumed regime structure and hyperparameters.
Bayesian Update Equations.Following Anderson and
Cheng [2022], we update each model’s sufficient statistics us-
ing the following recursions:
Λm,t = Λm,t−1 + em,te⊤ m,t
1 +x ⊤ t−1Φm,t−1xt−1 (4)
νm,t =ν m,t−1 + 1(5)
Φm,t =

Φ−1 m,t−1 +x t−1x⊤ t−1 −1 (6)
¯Bm,t = Φm,t  Φ−1 m,t−1 ¯Bm,t−1 +x t−1r⊤ t  ,(7)
wheree m,t =r t − ¯Bm,t−1xt−1 is the prediction error,Λ m,t
accumulates the sum of squared errors,ν m,t tracks degrees
of freedom,Φ m,t is the precision matrix for coefficients, and
¯Bm,t is the posterior mean estimate of the true coefficient
matrixB t. Each modelmis initialized with diffuse pri-
ors:ν m,0 =n+ 2,Λ m,0 = ¯σ2In where¯σ2 is the sam-
ple variance, and ¯Bm,0 sets the constant term to the sam-
ple mean with remaining coefficients at zero. The precision
matrixΦ m,0 =diag(α i, βiIk−1)varies across models with
αi ∈ {0.01,0.1,1}andβ i ∈ {1,10,100}, creating 9 hyper-
parameter combinations that ensure ensemble diversity. Up-
dates proceed fort= 1,2, . . . , T.
Model Weight Update.The weight of each model is up-
dated via Bayes’ rule based on predictive likelihood:
P(m|F t) = P(r t|m, Ft−1)P(m|F t−1)P
m′∈Mt P(r t|m′, Ft−1)P(m ′|Ft−1) ,(8)
whereF t denotes all information up to timet,P(r t|m, Ft−1)
is the predictive density under modelm, and the summation
in the denominator runs over all modelsm ′ in the active set
Mt to ensure weights sum to one.
Bayesian Model Averaging.The BA V AR predictions com-
bine individual model forecasts weighted by posterior model

Raw Price Data
(29 DJIA, w/o NVDA)
yfinance
Feature Engineering
Price, Volume, EMAs
MACD, RSI, BBs
State Tensor
(29×15×12)
HAR Features
(1,5,22) days
V AR Ensemble
(600 models)
Bayesian Model
Averaging µ, D
Transformer
Encoder Q(Views)
CNN Risk
Network δ(Risk)
BLED
Calculation
w∗ = 1 δ D−1 BLµBL
TD3 Actor
(Refinement)
Portfolio
Weights Environment
Twin Critics
Q1, Q2
Replay Buffer rt,s t+1
Done?
Performance
Evaluation
Sharpe, Sortino, MDD
BA V AR Module TD3
YesNo
Figure 1: BA V AR-BLED framework architecture. Historical price data is fed into feature engineering to produce state tensors. Three parallel
branches process the state: (1) the BA V AR module extracts HAR features and maintains an ensemble of V AR models to produce adaptive
prior estimatesµand dispersionD; (2) the Transformer encoder generates investor viewsQ; (3) the CNN estimates risk aversionδ. These
outputs feed into the BLED calculation, which computes Black-Litterman optimal weights under elliptical distributions. The TD3 actor
refines these weights, and twin critics estimate Q-values for policy optimization.
weights. Each modelmproduces mean and covariance pre-
dictions:
µm = ¯B⊤ mxt−1 (9)
Σm = Λm νm −n−1 ,(10)
which are combined via:
µ=
X
m
P(m|F t)µm (11)
D=
X
m
P(m|F t)

Σm +µ mµ⊤ m  −µµ ⊤,(12)
whereµandDdenote the prior mean and dispersion matrix
used in the subsequent BLED integration.
Ensemble Dynamics.The ensemble initializes new mod-
els with diffuse priors as specified above during each update
call, which then accumulate weight during Bayesian updat-
ing while processing market observations. Models with poor
predictive power receive lower weights and contribute less to
the averaging process, while well-performing models domi-
nate it, allowing the ensemble to implicitly adapt to regime
changes without explicit regime detection.
3.4 BLED Integration
The Black-Litterman model under Elliptical Distributions
combines the BA V AR-derived prior distribution of expected
returns and dispersion with transformer-generated views and
CNN-produced risk aversion to produce posterior estimates
of expected returns and dispersion.
Elliptical Distribution Framework.We model asset re-
turns using the Student’st-distribution, a member of the el-
liptical family with heavier tails than the normal distribution,
which has the density generator:
fX (x;µ, D) =|D|−1/2gn  (x−µ) ⊤D−1(x−µ)  ,(13)
whereµis the location parameter,Dis the dispersion matrix,
andg n is the density generator specific to thet-distribution
withνdegrees of freedom.
Black-Litterman Posterior.The posterior expected return
and dispersion matrix are computed as:
µBL =µ+

(τ D)−1 +P ⊤Ω−1P −1 P ⊤Ω−1(Q−P µ),
(14)
DBL =D−DP ⊤(Q+P DP ⊤)−1P D,(15)
whereµandDare the prior mean and dispersion matrix from
BA V AR (Equations (11) and (12)),Pis the view matrix (iden-
tity matrix for absolute views),Qcontains the view magni-
tudes generated by the transformer,Ωis the view uncertainty
matrix, andτis a scaling parameter that controls the confi-
dence in the prior.
Transformer View Generation.A transformer component
generates investor views on expected returns, while positional
encoding is omitted since the 15-day window already cap-
tures temporal structure, thus allowing it to focus on asset cor-
relations. Within this module, multi-head self-attention layers
and feed-forward networks produce the view vectorQ∈R n
representing expected returns for each asset.
CNN Risk Aversion Estimation.A convolutional neu-
ral network processes the state tensor to estimate a state-
dependent risk aversion parameterδ. This network applies
convolutional layers to extract patterns from price and vol-
ume data, followed by fully connected layers that output a
scalar bounded within a predefined range. This component
allows the model to increase risk aversion during volatile pe-
riods and decrease it during stable conditions. Finally, the
optimal portfolio weights are computed as:
w∗ = 1 δ D−1 BL µBL.(16)
3.5 TD3 Training
Given the MDP formulation with continuous state and action
spaces (Section 3.2), we employ the TD3 algorithm to learn a
policy that maximizes cumulative log returns.
Actor-Critic Architecture.The TD3 algorithm uses twin
Q-networks (Q1,Q 2) to reduce overestimation bias and em-
ploys delayed policy updates for stability, while the actor net-
work takes the BLED-derived weights from Equation (16) as

input and learns refinements under the assumptions and con-
straints specified in Section 1. Experiences are stored in a
replay buffer, from which mini-batches are sampled for train-
ing of the critics and the actor.
Training Loop.At each environment step, the agent ob-
serves the state, computes BLED weights, applies actor re-
finement, and executes the portfolio allocation. The environ-
ment returns the reward and next state, which are stored in
the replay buffer. The critics are updated by minimizing the
Bellman error, and the actor is updated via deterministic pol-
icy gradient with delayed updates. Training continues until
convergence, then performance is evaluated using the Sharpe
ratio, Sortino ratio, and maximum drawdown.
BA V AR Update Strategy.BA V AR models are updated
during environment steps, while the TD3 algorithm samples
batches from the replay buffer for policy and value function
updates. This separation ensures that the BA V AR ensemble
processes observed returns in their natural sequential order,
preventing overfitting to replayed trajectories and maintain-
ing temporal integrity of the Bayesian updates. Lastly, to en-
able parallel execution without blocking the DRL loop, the
actor network uses cached BA V AR priors that are refreshed
asynchronously in a separate computational thread.
Computational Optimization.The computational bottle-
neck is introduced by using synchronous updates for the
BA V AR ensemble at each environment step, requiring ap-
proximately 2600 seconds per training episode. We devel-
oped an adaptive hybrid wrapper that performs BA V AR up-
dates asynchronously at reduced frequency. Empirical testing
showed that 12 updates per year, corresponding to approxi-
mately monthly updates or every 21 trading days, provides
a good balance between computational cost and model accu-
racy. This addition reduced the episode training time to ap-
proximately 750 seconds and allowed for more efficient hy-
perparameter optimization.
4 Experiments
4.1 Experimental Setup
Dataset.We evaluate BA V AR-BLED across 29 Dow Jones
Industrial Average (DJIA) constituent stocks, excluding
NVIDIA due to its outlier performance, which would dis-
tort the comparative analysis. The data spans January 2014
to December 2024, providing over 10 years of daily observa-
tions including multiple market regimes such as the COVID-
19 crash and recovery, interest rate cycles, and sector rota-
tions.
We use a 60/20/20 chronological split for training, valida-
tion, and testing, resulting in 1640 training days, 547 vali-
dation days, and 547 test days. Each trading day, the agent
observes a window of 15 days of historical data. The state
tensor has shape(n×w×f) = (29×15×12), which in-
cludes adjusted close price, volume, and technical indicators
(including EMA, MACD, RSI, and Bollinger Bands).
Implementation.Training was conducted on an HPC clus-
ter using four NVIDIA RTX 4090 GPUs with PyTorch and
the TD3 algorithm for policy optimization. Each configura-
tion was trained for 500 episodes, requiring approximately 80
Table 1: Key hyperparameters from Optuna optimization
Category Parameter Search Range Value
Training
Batch size{128,256,512,1024}1024
Actor LR[10 −6,10 −3]2.58e-4
Critic LR[10 −5,10 −2]6.21e-4
Discount (γ)[0.98,0.999]0.991
Transformer
dmodel {32,64,96,128}128
Num heads{2,4,8}2
Num layers[1,4]4
Critic Num layers[2,5]3 Hidden size{256,512,1024}512
BA V AR
Max models[400,650]600
Burn-in ratio[0.2,0.4]0.34
τBA V AR [0.01,0.1]0.077
Black-Litterman τBL [0.01,0.1]0.039 σ2 Ω [0.01,0.2]0.052
GPU-hours. We note that while training benefits from parallel
GPU acceleration, inference requires minimal computational
resources and can be performed on a single CPU in real-time
for practical deployment. Hyperparameters were optimized
using Bayesian optimization via Tree-structured Parzen Esti-
mator (TPE) [Bergstraet al., 2011 ] over 40 trials, with search
spaces detailed in Table 1. For model selection, we trained
on the training set, selected the best checkpoint based on val-
idation set Sharpe ratio, and report final performance on the
held-out test set.
Hyperparameters.Table 1 presents the key hyperparame-
ters from Trial 30, which is the best-performing configuration
identified through Optuna optimization.
4.2 Baseline Comparisons
We compare BA V AR-BLED against four categories of base-
lines using standard portfolio performance metrics: the
Sharpe ratio (SR) [Sharpe, 1994 ], Sortino ratio (SoR)
[Sortino and Price, 1994 ], accumulated returns (AR), max-
imum drawdown (MDD) [Magdon-Ismail and Atiya, 2004 ],
and annualized volatility. Classic portfolio methods include
Equal Weight (1/N), Mean-Variance optimization, and Min-
imum Variance portfolios. Algorithmic strategies comprise
Momentum and Dual Moving Average approaches. We also
compare against state-of-the-art methods from two domains:
deep reinforcement learning approaches including PPO and
A2C from Stable-Baselines3[Raffinet al., 2021], EIIE [Jiang
et al., 2017 ], and Risk-Adjusted DRL [Choudharyet al.,
2025]; and transformer-based time series methods including
TFT [Limet al., 2021 ], PatchTST [Nieet al., 2023 ], Informer
[Zhouet al., 2021 ], iTransformer [Liuet al., 2024a ], Times-
Net [Wuet al., 2023 ], and TimeXer [Wanget al., 2024 ].
4.3 Results
Table 2 presents the performance comparison on the test set,
with cumulative returns visualized in Figure 2. BA V AR-
BLED achieves the highest Sharpe ratio of 1.72 among all
methods while maintaining competitive volatility at 12.64%.
The proposed method outperforms the best transformer base-
line (TimeXer) by 9.6% in Sharpe ratio and 19.9% in total re-

turns. Compared to deep RL methods, BA V AR-BLED shows
clear improvements, with Risk-Adjusted DRL achieving only
1.21 Sharpe ratio despite higher raw returns due to elevated
volatility. Traditional methods such as Mean-Variance and
EIIE suffer from drawdowns exceeding 19% and 28% respec-
tively, while BA V AR-BLED maintains a maximum draw-
down of 8.85%. Although PPO achieves the lowest MDD
and volatility, it produces negative returns and near-zero risk-
adjusted performance. We note that BA V AR-BLED does
not achieve the lowest volatility partially because the trad-
ing environment requires each model to invest its full avail-
able balance at every step. Models with higher cumulative
wealth therefore have higher absolute volatility, as larger cap-
ital bases amplify return fluctuations. Since BA V AR-BLED
maintained the highest balance for over 95% of trading days,
its volatility metric is naturally higher, and thanks to the en-
semble’s ability to dynamically adjust the weight of each
model based on its forecasting accuracy, the BA V AR module
is able to detect regime shifts, thus reducing the losses dur-
ing market downturns. This regime-adaptation occurs con-
tinuously without requiring explicit regime detection or la-
beling, further contributing to the robustness of our proposed
approach. This can be observed in Figure 2 around trading
days 250, 430, and 500, where BA V AR-BLED shows smaller
relative declines compared to most baselines.
To validate these results, we conducted binomial tests for
cumulative dominance and both pairedt-tests and sign tests
for rolling Sharpe ratio comparisons across 30, 60, and 90-
day windows (Table 3). The cumulative dominance test
checks whether BA V AR-BLED’s AR exceeds each bench-
mark for more than 50% of trading days. Results show sta-
tistical significance (p <0.05) against 15 of 16 benchmarks.
The exception is Risk-Adjusted DRL, where BA V AR-BLED
was ahead for 49.1% of trading days (p= 0.68), indicat-
ing comparable AR trajectories. However, Risk-Adjusted
DRL achieves this with much higher volatility (17.46% vs
12.64%) and worse maximum drawdown (12.83% vs 8.85%),
resulting in inferior risk-adjusted performance as confirmed
by the rolling Sharpe comparison (p <0.001). For the
rolling Sharpe ratio comparisons, statistical significance is
determined by either the pairedt-test or sign test across any
window. In this test, all 16 benchmarks show significance.
TimeXer shows a sign testp-value of 0.051, approaching
0.05, while the pairedt-test remains significant (p <0.001).
For Momentum, the sign test is not significant (p= 0.15),
indicating that BA V AR-BLED does not have higher rolling
Sharpe for the majority of trading windows. However, the
pairedt-test is highly significant (p <0.001), meaning that
when BA V AR-BLED outperforms, the magnitude of outper-
formance exceeds the periods when it underperforms. Both
methods still trail BA V AR-BLED in final returns (48.03% and
45.41% vs 57.26%) and overall Sharpe ratio (1.44 and 1.53
vs 1.72), confirming the robustness of our approach.
4.4 Ablation Study
To understand the contribution of each component, we con-
ducted ablation experiments by systematically removing or
modifying individual framework elements. Figure 3 shows
the cumulative returns over the test period for each configu-
Table 2: Performance comparison on the test set (best results in bold)
Method Ret. (%) Sharpe Sortino MDD (%) V ol. (%)
BA V AR-BLED 57.26 1.72 2.70-8.85 12.64
Dual MA 48.14 1.59 2.53 -9.22 11.86
TimeXer 47.77 1.57 2.48 -8.49 11.90
Informer 39.59 1.52 2.50 -6.89 10.49
Equal Weight 45.16 1.51 2.39 -8.45 11.84
PatchTST 42.21 1.50 2.34 -7.56 11.28
iTransformer 45.33 1.45 2.30 -8.88 12.44
Momentum 48.03 1.44 2.19 -11.08 13.21
TimesNet 37.76 1.44 2.37 -7.54 10.70
TFT 38.75 1.42 2.30 -7.52 11.05
Risk-Adj DRL 52.70 1.21 1.70 -12.83 17.46
Min Variance 20.92 0.92 1.39 -10.33 10.06
EIIE 34.49 0.73 1.04 -28.61 22.24
Mean-Variance 35.86 0.72 1.11 -19.91 23.46
A2C 7.78 0.65 1.07 -8.66 5.58
PPO -0.39 -0.01 -0.02-6.03 4.91
0 100 200 300 400 500
Trading Day
0.9
1.0
1.1
1.2
1.3
1.4
1.5
1.6Accumulated Return (AR)
Portfolio Performance: BAVAR-BLED vs Benchmarks
BAVAR-BLED (Proposed) (57.3%)
Risk-Adj DRL (52.7%)
Dual MA (48.1%)
Momentum (48.0%)
TimeXer (47.8%)
iTransformer (45.3%)
Equal Weight (1/N) (45.2%)
PatchTST (42.2%)
Informer (39.6%)
TFT (38.8%)
TimesNet (37.8%)
Mean-Variance (35.9%)
EIIE (34.5%)
Min Variance (20.9%)
A2C (7.8%)
PPO (-0.4%)
Figure 2: Cumulative returns over the test period comparing
BA V AR-BLED against benchmark methods. Our method (solid
blue) achieves the highest final return of 57.3% while maintaining
stable growth throughout different market conditions.
ration, and Table 4 summarizes the quantitative results.
The ablation results reveal several important findings.
First, removing BA V AR causes the model to fail, with re-
turns dropping to -6.45% and the Sharpe ratio falling to 0.05,
demonstrating that the adaptive prior estimation is essential
for the framework. Second, removing BLED also leads to
a notable performance drop (Sharpe from 1.72 to 1.41). As
stated previously, financial returns exhibit fatter tails [Offi-
cer, 1972; Kringet al., 2009; Koldanov, 2019 ], which makes
modeling with Student’st-distributions avoid the underesti-
mation of extreme event probabilities, thus leading to more
appropriate position sizing during volatile periods, as shown
in Figure 2. Third, as it can be seen from Table 4, both higher
(1000) and lower (100) number of BA V AR models negatively
impacted the performance of the framework, which can be
explained by the bias-variance trade-off in Bayesian model
averaging, where few models provide insufficient diversity
[Dormannet al., 2018 ] to capture market movements, while
more models can introduce noise from poorly performing
models and dilute the signal from more well-calibrated mod-
els [Jay and Neil, 2021 ], thus further confirming the find-

Table 3: Statistical significance tests. Cumulative dominance uses
a binomial test for whether BA V AR-BLED is ahead>50% of days.
Rolling Sharpe uses pairedt-tests and sign tests across 30, 60, and
90-day windows.
Benchmark Days Ahead % Ahead Dom.pR.SharpepSig.
Mean-Variance 520/546 95.2%<0.001<0.001 YES
Min-Variance 512/546 93.8%<0.001<0.001 YES
Equal Weight 505/546 92.5%<0.001<0.001 YES
Momentum 332/546 60.8%<0.001<0.001 † YES
Dual MA 470/546 86.1%<0.001<0.001 YES
EIIE 412/546 75.5%<0.001<0.001 YES
Risk-Adj DRL 268/546 49.1% 0.681<0.001 YES ∗
PPO 544/546 99.6%<0.001<0.001 YES
A2C 542/546 99.3%<0.001<0.001 YES
TFT 544/546 99.6%<0.001<0.001 YES
PatchTST 545/546 99.8%<0.001 0.006 YES
Informer 526/546 96.3%<0.001 0.047 YES
iTransformer 543/546 99.5%<0.001 0.004 YES
TimesNet 546/546 100.0%<0.001 0.023 YES
TimeXer 526/546 96.3%<0.001 0.051 ‡ YES
∗Cumulative dominance not significant; rolling Sharpe significant.
†Sign test not significant (p= 0.15);t-test highly significant.
‡Sign test approaching significance (p= 0.05);t-test significant.
0 100 200 300 400 500
Trading Day
0.8
1.0
1.2
1.4
1.6Accumulated Return (AR)
Portfolio Performance Comparison - Ablation Study
BAVAR-BLED (Proposed) (57.3%)
BAVAR (100 models) (52.6%)
w/o BLED (46.3%)
BAVAR (1000 models) (43.1%)
w/o CNN Risk (41.3%)
BAVAR w/o HAR (39.3%)
w/o TD3 Delay (39.0%)
w/o Transformer (37.6%)
w/o Enhanced Buffer (36.7%)
w/o BAVAR (-6.5%)
Figure 3: Cumulative returns comparison for ablation study config-
urations over the test period.
ings of the hyperparameter tuning and validating 600 mod-
els as being a sweet spot for the BA V AR-BLED framework.
Fourth, transformer-based view generation and CNN risk es-
timation both contribute meaningfully, with their removal
causing 23% and 22% reductions in the Sharpe ratio respec-
tively. Finally, HAR features improve performance by cap-
turing multi-scale temporal dynamics, and TD3 architectural
choices (delayed updates, enhanced replay buffer) provide
additional stability gains. Similarly, the configuration with-
out enhanced buffer achieves the lowest MDD of 6.86%, but
this comes with a 27% decrease in Sharpe ratio, indicating
that the full framework provides a better trade-off between
risk control and returns.
5 Conclusion
This paper presented BA V AR-BLED, a framework for port-
folio optimization that addresses two fundamental limitations
in existing DRL approaches: the assumption of normally dis-
tributed returns by utilizing the Black-Litterman model under
Table 4: Ablation study results showing the impact of removing in-
dividual components
Configuration Ret. (%) Sharpe Sortino MDD (%)
Full BA V AR-BLED 57.26 1.72 2.70-8.85
BA V AR 100 models 52.62 1.68 2.67 -7.08
w/o BLED 46.26 1.41 2.20 -11.40
BA V AR 1000 models 43.11 1.48 2.27 -8.96
w/o CNN risk est. 41.28 1.35 2.08 -8.78
w/o HAR features 39.28 1.39 2.12 -7.57
w/o TD3 delay 38.99 1.22 1.93 -9.69
w/o Transformer views 37.59 1.33 2.03 -9.63
w/o Enhanced buffer 36.67 1.25 1.91-6.86
w/o BA V AR -6.45 0.05 0.07 -29.33
Elliptical Distributions and the uniform treatment of histor-
ical data by introducing Bayesian-Averaging Vector Autore-
gressive methods. In this way, our approach provides adap-
tive, regime-aware prior estimates that respond to changing
market conditions while modeling fat-tailed return distribu-
tions more realistically. Furthermore, an experimental eval-
uation of 29 DJIA stocks demonstrates that BA V AR-BLED
achieves a Sharpe ratio of 1.72 and total returns of 57.26%,
outperforming both traditional portfolio methods and state-
of-the-art transformer-based approaches, thereby establishing
a new performance benchmark in this domain. These re-
sults were further validated through statistical tests for AR
and rolling SR comparisons, confirming the robustness of
the framework and its adaptability to changing market con-
ditions. The ablation study confirms that each component
contributes meaningfully to performance, with BA V AR being
essential to the framework, as its removal reduces the Sharpe
ratio from 1.72 to 0.05.
The main limitations of our approach include computa-
tional complexity from maintaining a large V AR ensemble
and restricted HAR feature horizons. While the original HAR
methodology [Corsi, 2009] incorporated yearly and 10-year
horizons, our implementation uses only daily, weekly, and
monthly (1, 5, 22 trading days) features due to computational
constraints. This may limit the model’s ability to capture
longer-term market cycles.
Future work will explore several directions. First, the
framework naturally supports continuous learning during de-
ployment, as BA V AR updates through closed-form Bayesian
equations rather than gradient descent, allowing for adapta-
tion to new market observations without retraining the com-
putationally expensive DRL component. Second, extending
HAR features to longer horizons like quarterly, yearly and 10-
year could improve the detection of long-term market trends.
Lastly, incorporating transfer learning and optimizing ensem-
ble management could reduce the burn-in period for new mar-
ket environments.
References
[Anderson and Cheng, 2022] Evan Anderson and Ai-ru
Cheng. Portfolio choices with many big models.
Management Science, 68(1):690–715, 2022.

[Bergstraet al., 2011 ] James Bergstra, R ´emi Bardenet,
Yoshua Bengio, and Bal ´azs K ´egl. Algorithms for hyper-
parameter optimization. In J. Shawe-Taylor, R. Zemel,
P. Bartlett, F. Pereira, and K.Q. Weinberger, editors,
Advances in Neural Information Processing Systems,
volume 24. Curran Associates, Inc., 2011.
[Black and Litterman, 1992] Fischer Black and Robert Lit-
terman. Global portfolio optimization.Financial analysts
journal, 48(5):28–43, 1992.
[Choudharyet al., 2025 ] Himanshu Choudhary, Arishi Orra,
Kartik Sahoo, and Manoj Thakur. Risk-adjusted deep re-
inforcement learning for portfolio optimization: A multi-
reward approach.International Journal of Computational
Intelligence Systems, 18(1):126, 2025.
[Corsi, 2009] Fulvio Corsi. A simple approximate long-
memory model of realized volatility.Journal of financial
econometrics, 7(2):174–196, 2009.
[Dormannet al., 2018 ] Carsten F Dormann, Justin M Cal-
abrese, Gurutzeta Guillera-Arroita, Eleni Matechou,
V olker Bahn, Kamil Barto´n, Colin M Beale, Simone Ciuti,
Jane Elith, Katharina Gerstner, et al. Model averaging in
ecology: A review of bayesian, information-theoretic, and
tactical approaches for predictive inference.Ecological
monographs, 88(4):485–504, 2018.
[Fischer and Krauss, 2018] Thomas Fischer and Christopher
Krauss. Deep learning with long short-term memory net-
works for financial market predictions.European journal
of operational research, 270(2):654–669, 2018.
[Frazziniet al., 2018 ] Andrea Frazzini, Ronen Israel, and
Tobias J Moskowitz.Trading costs, volume 3229719.
SSRN, 2018.
[Fujimotoet al., 2018 ] Scott Fujimoto, Herke Hoof, and
David Meger. Addressing function approximation error in
actor-critic methods. InInternational conference on ma-
chine learning, pages 1587–1596. PMLR, 2018.
[Gaoet al., 2020 ] Ziming Gao, Yuan Gao, Yi Hu, Zhengy-
ong Jiang, and Jionglong Su. Application of deep q-
network in portfolio management. In2020 5th IEEE In-
ternational Conference on Big Data Analytics (ICBDA),
pages 268–275. IEEE, 2020.
[Gaoet al., 2021 ] Yuan Gao, Ziming Gao, Yi Hu, Sifan
Song, Zhengyong Jiang, and Jionglong Su. A framework
of hierarchical deep q-network for portfolio management.
InICAART (2), pages 132–140, 2021.
[Huang and Tanaka, 2022] Zhenhan Huang and Fumihide
Tanaka. Mspm: A modularized and scalable multi-agent
reinforcement learning-based system for financial portfo-
lio management.Plos one, 17(2):e0263689, 2022.
[Jay and Neil, 2021] William I Jay and Ethan T Neil.
Bayesian model averaging for analysis of lattice field the-
ory results.Physical Review D, 103(11):114502, 2021.
[Jiang and Wang, 2022] Caiyu Jiang and Jianhua Wang. A
portfolio model with risk control policy based on deep re-
inforcement learning.Mathematics, 11(1):19, 2022.
[Jianget al., 2017 ] Zhengyao Jiang, Dixing Xu, and Jinjun
Liang. A deep reinforcement learning framework for the
financial portfolio management problem.arXiv preprint
arXiv:1706.10059, 2017.
[Koldanov, 2019] Petr Koldanov. Testing new property of
elliptical model for stock returns distribution, 2019.
[Kringet al., 2009 ] Sebastian Kring, Svetlozar T
Rachev, Markus H ¨ochst¨otter, Frank J Fabozzi, and
Michele Leonardo Bianchi. Multi-tail generalized ellip-
tical distributions for asset returns.The Econometrics
Journal, 12(2):272–291, 2009.
[Limet al., 2021 ] Bryan Lim, Sercan ¨O Arık, Nicolas Lo-
eff, and Tomas Pfister. Temporal fusion transformers for
interpretable multi-horizon time series forecasting.Inter-
national journal of forecasting, 37(4):1748–1764, 2021.
[Liuet al., 2024a ] Yong Liu, Tengge Hu, Haoran Zhang,
Haixu Wu, Shiyu Wang, Lintao Ma, and Mingsheng Long.
itransformer: Inverted transformers are effective for time
series forecasting, 2024.
[Liuet al., 2024b ] Yuchen Liu, Daniil Mikriukov,
Owen Christopher Tjahyadi, Gangmin Li, Terry R.
Payne, Yong Yue, Kamran Siddique, and Ka Lok Man.
Revolutionising financial portfolio management: The
non-stationary transformer’s fusion of macroeconomic
indicators and sentiment analysis in a deep reinforcement
learning framework.Applied Sciences, 14(1):274, 2024.
[Magdon-Ismail and Atiya, 2004] Malik Magdon-Ismail and
Amir F Atiya. Maximum drawdown.Risk Magazine,
17(10):99–102, 2004.
[Markowitz, 1952] Harry Markowitz. Portfolio selection.
The Journal of Finance, 7(1):77–91, 1952.
[Mikriukovet al., 2025 ] Daniil Mikriukov, Ruoyu Sun, and
Zhengyong Jiang. Deep reinforcement learning-based
portfolio optimization with black-litterman model under
elliptical distributions. In De-Shuang Huang, Chuanlei
Zhang, Qinhu Zhang, and Yijie Pan, editors,Advanced In-
telligent Computing Technology and Applications, pages
273–284, Singapore, 2025. Springer Nature Singapore.
[Nieet al., 2023 ] Yuqi Nie, Nam H. Nguyen, Phanwadee
Sinthong, and Jayant Kalagnanam. A time series is worth
64 words: Long-term forecasting with transformers, 2023.
[Officer, 1972] Robert Rupert Officer. The distribution of
stock returns.Journal of the american statistical associa-
tion, 67(340):807–812, 1972.
[Raffinet al., 2021 ] Antonin Raffin, Ashley Hill, Adam
Gleave, Anssi Kanervisto, Maximilian Ernestus, and Noah
Dormann. Stable-baselines3: Reliable reinforcement
learning implementations.Journal of machine learning
research, 22(268):1–8, 2021.
[Sharpe, 1994] William F Sharpe. The sharpe ratio.Journal
of Portfolio Management, 21(1):49–58, 1994.
[Shavandi and Khedmati, 2022] Ali Shavandi and Majid
Khedmati. A multi-agent deep reinforcement learning
framework for algorithmic trading in financial markets.
Expert Systems with Applications, 208:118124, 2022.

[Songet al., 2023 ] Zitao Song, Yining Wang, Pin Qian,
Sifan Song, Frans Coenen, Zhengyong Jiang, and Jion-
glong Su. From deterministic to stochastic: an in-
terpretable stochastic model-free reinforcement learning
framework for portfolio optimization.Applied Intelli-
gence, 53(12):15188–15203, 2023.
[Sortino and Price, 1994] Frank A Sortino and Lee N Price.
Performance measurement in a downside risk framework.
the Journal of Investing, 3(3):59–64, 1994.
[Sunet al., 2024 ] Ruoyu Sun, Angelos Stefanidis, Zhengy-
ong Jiang, and Jionglong Su. Combining transformer
based deep reinforcement learning with black-litterman
model for portfolio optimization.Neural Computing and
Applications, 36(32):20111–20146, 2024.
[Wanget al., 2024 ] Yuxuan Wang, Haixu Wu, Jiaxiang
Dong, Guo Qin, Haoran Zhang, Yong Liu, Yunzhong Qiu,
Jianmin Wang, and Mingsheng Long. Timexer: Empow-
ering transformers for time series forecasting with exoge-
nous variables.Advances in Neural Information Process-
ing Systems, 37:469–498, 2024.
[Wuet al., 2023 ] Haixu Wu, Tengge Hu, Yong Liu, Hang
Zhou, Jianmin Wang, and Mingsheng Long. Timesnet:
Temporal 2d-variation modeling for general time series
analysis, 2023.
[Xiao and Valdez, 2015] Yugu Xiao and Emiliano A Valdez.
A black–litterman asset allocation model under elliptical
distributions.Quantitative Finance, 15(3):509–519, 2015.
[Yanget al., 2023 ] Bing Yang, Ting Liang, Jian Xiong,
and Chong Zhong. Deep reinforcement learning based
on transformer and u-net framework for stock trading.
Knowledge-Based Systems, 262:110211, 2023.
[Zhanget al., 2024 ] Zhilu Zhang, Procheta Sen, Zimu Wang,
Ruoyu Sun, Zhengyong Jiang, and Jionglong Su. Finbpm:
A framework for portfolio management-based financial in-
vestor behavior perception model. InProceedings of the
18th Conference of the European Chapter of the Associ-
ation for Computational Linguistics (Volume 1: Long Pa-
pers), pages 246–257, 2024.
[Zhouet al., 2021 ] Haoyi Zhou, Shanghang Zhang, Jieqi
Peng, Shuai Zhang, Jianxin Li, Hui Xiong, and Wan-
cai Zhang. Informer: Beyond efficient transformer for
long sequence time-series forecasting. InProceedings of
the AAAI conference on artificial intelligence, volume 35,
pages 11106–11115, 2021.
[Zhu and Yen, 2024] Enmin Zhu and Jerome Yen. Enhanc-
ing portfolio optimization with transformer-gan integra-
tion: A novel approach in the black-litterman framework,
2024.
