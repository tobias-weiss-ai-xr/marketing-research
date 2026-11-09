---
title: 'Regression Models Meet Foundation Models: A Hybrid-AI Approach to Practical Electricity Price
  Forecasting'
url: https://arxiv.org/abs/2603.06726
category: ai-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Yunzhong Qiu
- Binzhu Li
- Hao Wei
- Shenglin Weng
- Chen Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.06726
pages: 15
chars: 78845
fetched_at: '2026-11-08T13:08:54+00:00'
kb_version: 1
---

# Regression Models Meet Foundation Models: A Hybrid-AI Approach to Practical Electricity Price Forecasting

Regression Models Meet Foundation Models:
A Hybrid-AI Approach to Practical Electricity Price Forecasting
Yunzhong Qiu∗
qiuyz24@mails.tsinghua.edu.cn
School of Software, BNRist
Tsinghua University
Beijing, China
Binzhu Li∗
lbz25@mails.tsinghua.edu.cn
School of Software, BNRist
Tsinghua University
Beijing, China
Hao Wei
weihao2@gcl-et.com
Suzhou Indus-
trial Park Xingzhixun CS Co., Ltd.
Jiangsu, China
Shenglin Weng
wengshenglin@gcl-et.com
Suzhou Indus-
trial Park Xingzhixun CS Co., Ltd.
Jiangsu, China
Chen Wang
wang_chen@tsinghua.edu.cn
School of Software, BNRist
Tsinghua University
Beijing, China
Zhongyi Pei†
peizhyi@tsinghua.edu.cn
School of Software, BNRist
Tsinghua University
Beijing, China
Mingsheng Long
mingsheng@tsinghua.edu.cn
School of Software, BNRist
Tsinghua University
Beijing, China
Jianmin Wang
jimwang@tsinghua.edu.cn
School of Software, BNRist
Tsinghua University
Beijing, China
Abstract
Electricity market prices exhibit extreme volatility, nonlinearity,
and non-stationarity, making accurate forecasting a significant chal-
lenge. While cutting-edge time series foundation models (TSFMs)
effectively capture temporal dependencies, they typically underuti-
lize cross-variate correlations and non-periodic patterns that are
essential for price forecasting. Conversely, regression models excel
at capturing feature interactions but are limited to future-available
inputs, ignoring crucial historical drivers that are unavailable at
forecast time. To bridge this gap, we propose FutureBoosting, a
novel paradigm that enhances regression-based forecasts by inte-
grating forecasted features generated from a frozen TSFM. This
approach leverages the TSFM’s ability to model historical patterns
and injects these insights as enriched inputs into a downstream
regression model. We instantiate this paradigm into a lightweight,
plug-and-play framework for electricity price forecasting. Extensive
evaluations on real-world electricity market data demonstrate that
our framework consistently outperforms state-of-the-art TSFMs
and regression baselines, achieving reductions in Mean Absolute
Error (MAE) of more than 30% at most. Through ablation studies
and explainable AI (XAI) techniques, we validate the contribution
of forecasted features and elucidate the model’s decision-making
process. FutureBoosting establishes a robust, interpretable, and ef-
fective solution for practical market participation, offering a general
framework for enhancing regression models with temporal context.
CCS Concepts
•Computing methodologies→ Artificial intelligence;Ensem-
ble methods.
∗Both authors contributed equally to this research.
†Corresponding Author.
Keywords
regression models, foundation models, electricity price forecasting
1 Introduction
A healthy energy market is essential for achieving high utilization
of new energy and preventing global warming. As a critical support-
ing technology, electricity price forecasting (EPF) plays a pivotal
role in activating energy markets, by which market participants are
able to make informed decisions, including bidding strategies, risk
management, and resource allocation. However, electricity prices
are inherently volatile, nonlinear, and non-stationary due to in-
creasingly complex supply-demand dynamics, posing a significant
challenge for accurate EPF with cutting-edge AI technologies.
Auto-regressive and regression modeling are two mainstream
paradigms in electricity price forecasting. Recently, time-series
foundation models (TSFMs) have emerged as a state-of-the-art
approach in the auto-regressive paradigm, thanks to their large-
scale pretraining on diverse time series corpora. On public bench-
marks [1, 37], TSFMs [2, 4, 10, 25–27] demonstrate superior zero-
shot capability, surpassing statistical models [6, 13] and some end-
to-end deep learning models [20, 30, 31, 43].
However, as shown by Figure 1, these superior benchmark per-
formance gains are not guaranteed in real-world electricity price
forecasting, where electricity price exhibits volatile, nonlinear, and
non-stationary temporal dynamics. For electricity trading, the vi-
olent changes in prices have a significant impact on the supply-
demand balancing and participants’ profits. By Table 1, which sum-
marizes key difficulty indicators computed over the full year of 2025,
we find that both day-ahead and real-time prices exhibit a large tail
ratio (𝑝99/𝑝50≈ 5) and a non-negligible extreme-event frequency
(P(𝑝> 1000) ≈6%). The distribution is strongly non-Gaussian
(excess kurtosis≈ 5), and the change is also highly fierce (the top
1% of absolute changes exceed 400; large jumps|Δ𝑝|> 200occur
arXiv:2603.06726v1  [cs.LG]  6 Mar 2026

0
500
1000
1500Electricity Price
Day-Ahead Clearing Price Forecasts
0
500
1000
1500Electricity Price
Real-Time Clearing Price Forecasts
GT (Day-ahead)
GT (Real-time)
timerxl
tirex
chronos2
timesfm
sundial
moirai2
(a) Volatile, nonlinear, and non-stationary temporal dynamics.
0 200 400 600 800 1000 1200 1400
Electricity Price
0
5
10
15
20Percentage (%)
Day-ahead Clearing Price
Real-time Clearing Price
Extreme Low Values
Extreme High ValuesNon-Gaussian Heavy Tailed
(b) Non-Gaussian, heavy-tailed, and extreme value distribution.
Figure 1: Electricity price characteristics in the Shanxi spot
market (15-min). (a) Day-ahead vs real-time forecasts in a
representative October 2025 window. (b) Price distribution
over the full year 2025, showing heavy tails and extremes.
Table 1: Key difficulty indicators of Shanxi electricity prices
in 2025. Higher values indicate more challenging dynamics.
Indicator Day-ahead Real-time Gaussian
Tail ratio𝑝99/𝑝504.86 5.33≈2 (1.5–2.5)
Extreme freq.P(𝑝>1000)5.45% 5.88%≈0% (<0.1%)
Excess kurtosis 5.05 5.39 0
Jump size𝑝99(|Δ𝑝|)399.8 439.9≈200(2.576×𝜎 Δ𝑝)
Jump freq.P(|Δ𝑝|>200)2.92% 3.33%≈1% (0.5–1.5%)
in about 3% of intervals), implying that rare but impactful spikes
are much more frequent than a normal assumption of noise. These
properties jointly make auto-regressive forecasting challenging.
Instead of relying on temporal dependencies like auto-regressive
modeling, the regression modeling paradigm [ 39] directly esti-
mates correlations between features and demonstrates strong per-
formance in previous literature [ 11, 35]. However, correlations
between variables are often diversified in different downstream
domains, making regression modeling hard to generalize across
large-scale cross-domain data. As a representative branch in a va-
riety of classical regression models [ 12, 14, 16, 21, 28, 33, 34, 38],
gradient boosting trees [9, 18] demonstrate superior capability in
handling structured feature interactions and capturing domain-
specific patterns through their hierarchical decision structures.
However, traditional regression approaches are unable to capture
temporal dynamics and are sensitive to data quality and feature
engineering [12, 14, 21]. Such drawbacks limit the forward-looking
predictive capability of regression models.
To address these limitations separately from auto-regressive and
regression models, we propose a novel modeling paradigm,Fu-
tureBoosting. Our paradigm bridges these approaches through a
two-stage process: (1) Using TSFMs to generate forecasts of un-
certain future price drivers that are not yet available at the time
of forecasting; (2) Integrating these forecasts with available future
variables into an enriched feature set, on which a regression model,
such as LightGBM [18], is trained to forecast final electricity prices.
By bridging large-scale pretrained foundation models and light-
weight machine learning models, we fully leverage generalizable
cross-domain knowledge for a specific downstream domain.
OurFutureBoostingparadigm builds on a key insight: while
TSFMs can generally capture temporal patterns that follow consis-
tent and generalizable trends, cross-variate dependencies tend to
be highly task-specific and require more domain-aware modeling.
By expanding the feature set with forecasts of future price drivers,
we reframe the forecasting problem from directly modeling com-
plex temporal-price relationships to learning more interpretable
cross-variate associations within an enriched feature space that
incorporates forward-looking expectations.
Following theFutureBoostingparadigm, we propose a light-
weight, plug-and-play, and flexible EPF framework, based on which
extensive experiments and analysis are conducted on real-world
electricity market datasets, demonstrating significant improvements
in forecasting accuracy over both standalone TSFMs and traditional
cross-variate regression models. The major contributions are sum-
marized as follows:
• Innovative paradigm:We propose theFutureBoostingpar-
adigm, a novel hybrid approach based on insights into the
differences between TSFMs and regression modeling.
• EPF framework:Following theFutureBoostingparadigm,
we propose a lightweight, plug-and-play EPF framework
based on TSFMs and regression models.
• Empirical validation:We conduct comprehensive experi-
ments and analysis on real-world electricity market datasets,
demonstrating significant improvements compared to stan-
dalone auto-regressive and regression models.
2 Related Works
2.1 Time Series Foundation Models
Time series foundation models (TSFMs) are large-scale models
pretrained on diverse time series corpora and designed for zero- or
few-shot forecasting across domains without task-specific training.
The most prevalent structure in TSFMs is the transformer-based
architecture, ranging from univariate decoder-only models to multi-
variate encoder-only models. Representative work includes Chronos
[3], Chronos-2 [2], Timer-XL [26] and Sundial [27], Moirai 2.0 [25]
and TimesFM2.5 [10]. Besides, an xLSTM-based model TiRex [4]
also generates outstanding performance. These models are typically
evaluated on public benchmarks such as GiftEval [1] and FEV [37],
where they substantially outperform classical statistical methods
(e.g., AutoARIMA [6], AutoETS [13]) and many end-to-end deep
learning baselines (e.g., N-BEATS [31], DLinear [43], PatchTST [30],
xLSTM-Mixer [20]). Their strength lies in capturing long-range tem-
poral dependencies and generalizing across series via large-scale
pretraining, and they are often used in zero-shot mode without

task-specific fine-tuning. However, benchmark superiority does not
always carry over to domain-specific applications, such as electric-
ity price forecasting, where cross-variate structure, regime shifts,
and heavy-tailed price distributions may require complementary
modeling beyond purely auto-regressive forecasting.
2.2 Regression Models
Regression analysis provides a broad family of methods for forecast-
ing a continuous target from a set of exogenous variables. Classical
approaches include ordinary least squares (OLS) [8], generalized lin-
ear models (GLMs) [29], and polynomial regression [17]; regularized
variants such as Ridge [28] and Lasso [33] control overfitting and
support feature selection. Nonlinear and nonparametric methods
range from support vector regression (SVR) [16] to tree-based en-
sembles: random forests [34], gradient boosting (e.g., XGBoost [9],
LightGBM [18]), and related decision-tree methods [38]. The per-
formance of these models is often highly dependent on feature
engineering and selection, as they are sensitive to the relevance and
scale of inputs [12, 14, 21]. For structured tabular data with mixed
covariate types and strong interaction effects, tree-based meth-
ods—especially gradient boosting—have repeatedly shown strong
empirical performance and are widely used in industrial forecast-
ing applications [9, 18]. In electricity price forecasting, tree-based
regressors are commonly used to capture nonlinear relationships
between prices and exogenous variables such as load, electricity
mix, and temporal indicators. Their interpretability (e.g., via feature
importance) also supports deep domain analysis [11, 35].
2.3 Electricity Price Forecasting
Electricity price forecasting (EPF) has been studied from statisti-
cal, machine learning, and hybrid perspectives [ 23]. Early work
relied on ARIMA [7], GARCH-type models [5] for volatility, and
regression on load and other drivers [42]. Later, neural networks,
support vector machines, and tree-based models were applied to
capture nonlinearities and complex feature interactions [11, 23, 35].
Recent efforts have incorporated deep learning methods, such as
LSTMs [22] and transformers [24], to model prices and related vari-
ables. EPF is typically framed as day-ahead or real-time forecasting,
with submission deadlines and horizons dictated by market rules
(e.g., day-ahead markets requiring forecasts by a fixed time for the
next day) [19]. Key challenges include the non-Gaussian, heavy-
tailed price data distribution, strong temporal cross-variate depen-
dencies, renewable penetration impact, supply-demand balance,
and non-stationarity due to regulatory and structural changes [42].
Our work connects this literature by combining zero-shot TSFMs
for forecasting future-unavailable and future-uncertain drivers with
a tree-based regressor that models cross-variate relationships on an
enriched feature set, thus addressing both temporal generalization
and domain-specific correlation structure in a single framework.
3 Preliminaries
3.1 Electricity Market Trading
The regulations in different electricity markets can vary in details,
but they generally follow similar settings [ 15, 41]. Take the elec-
tricity market in China, for example. Electricity market prices are
primarily divided into two parts: day-ahead and real-time prices.
As illustrated in Figure 2, before the trading process begins on Day
𝐷+ 1, the consumers and suppliers in the market are required to
report their supply and demand plans for Day 𝐷+ 1on Day 𝐷.
Then the trading platform, serving as an authoritative third party,
aggregates all market participants’ plans and derives the equitable
day-ahead electricity prices for the Day𝐷+1market on Day𝐷.
Since the day-ahead electricity market is planned in advance,
actual supply and demand may not be fully scheduled. For exam-
ple, establishments might adjust their electricity consumption in
response to extreme weather or emerging events. The real-time
electricity market is designed to support just-in-time electricity
trading. Unlike the day-ahead electricity market price, which is
set in advance, the real-time electricity market price is determined
dynamically based on real-time supply and demand, and is more
random and volatile.
For buyers and suppliers, both day-ahead and real-time elec-
tricity price forecasts are critical for developing trading strate-
gies. Additionally, an authoritative third party provides historical
and future-available supply-and-demand data—including system
load, transmission capacity, power generation, and interconnection
plans—which are highly beneficial for electricity price forecasting.
Time
D 10:00
Supplier
Consumer
D 17:00
PREDICTION
Day D+1 Forecasted Day-
ahead Clearing Price
Day D+1 Forecasted
Supply/Demand
Day D+1 Supplier Plan
Day D+1 Consumer Plan
Administrator
ANNOUNCEMENT
Day D+1 Day-ahead
Clearing Price
Day D+1 Adjusted Supply/
Demand Plan
D 00:00 D+1 00:00
Pricing Day D
AI Model Administrator
Figure 2: Illustration of electricity market trading back-
ground. Suppliers and consumers must provide day-ahead
plans for day 𝐷+ 1on day 𝐷. More accurate forecasts from
the AI model improve the trading plan’s foresight, yielding
greater benefits.
3.2 Problem Formulation
The electricity prices and related grid data are published at 15-
minute resolution, i.e.,𝐻= 96timesteps per day. We index each
timestep within a day byℎ∈{1,...,𝐻}.
Inputs.At the end of day 𝐷, three parts of data are accessible:
(Y:𝐷,X :𝐷,Z𝐷+1).
Historical target variable(Y:𝐷∈R 𝐷·𝐻×2 ): history day-ahead and
real-time clearing prices for days𝑑≤𝐷 and timestepsℎ= 1,...,𝐻 .
Y:𝐷 =

𝑦da 𝑑,ℎ,𝑦 rt 𝑑,ℎ

𝑑≤𝐷,ℎ=1,...,𝐻 	 .(1)
Historical exogenous variables(X :𝐷∈R 𝐷·𝐻×𝐶 ):𝐶 variables ob-
served only up to day𝐷, including historical load, power generation,
and clearing prices of related markets.
Future available exogeneous variables(Z 𝐷+1 ∈R 𝐻×𝑝 ): 𝑝 vari-
ables worked out in advance for the forecast day𝐷+ 1, including
timestamps, production plans, grid-provided forecasts, and weather
forecasts for each timestepMon day𝐷+1.

Outputs.The goal is to forecast either the day-ahead or the
real-time price curve for day𝐷+1.
Y𝐷+1 =

𝑦da 𝑑,ℎ,𝑦 rt 𝑑,ℎ

𝐷<𝑑≤𝐷+1,ℎ=1,...,𝐻 	 .(2)
Day-ahead price forecasting( 𝑓 da): the output is the vector of
day-ahead clearing prices for day𝐷+1.
ˆyda 𝐷+1 =𝑓 da(Y:𝐷,X :𝐷,Z𝐷+1),
yda 𝐷+1 = 𝑦da 𝐷+1,1,...,𝑦 da 𝐷+1,𝐻 ⊤∈R 𝐻. (3)
Real-time price forecasting( 𝑓 rt): the output is the vector of real-
time clearing prices for day𝐷+1.
ˆyrt 𝐷+1 =𝑓 rt(Y:𝐷,X :𝐷,Z𝐷+1),
yrt 𝐷+1 = 𝑦rt 𝐷+1,1,...,𝑦 rt 𝐷+1,𝐻 ⊤∈R 𝐻. (4)
4 Methodology
4.1 FutureBoosting Paradigm
The electricity price in actual market scenarios is often driven
by instantaneous supply-demand balance fluctuations, making the
electricity price sensitive to relevant future time series expectations.
However, only historical observations and numerical weather pre-
diction variables are available at planning time, making electricity
price forecasting challenging due to information insufficiency. Our
proposedFutureBoostingparadigm addresses the limitations in a
two-stage pipeline:
Stage 1 (forecast):Given historical data (Y, X), we employ
TSFMs to generate forecasts of future-unavailable variables denoted
ˆXforecast =ℎ(Y, X), whereM is the auto-regressive forecaster.
These forecasts serve as augmented features that capture temporal
patterns and provide expectations of future supply-demand drivers.
Stage 2 (regress):We form an enriched feature setFthat concate-
nates ˆXforecast, future-available exogenous variablesZ, and optional
domain-constructed factors. Then a regression model𝑓 forecasts
the target price ˆy=𝑓(F).
This design decouples temporal forecasting from cross-variate
correlation modeling, enabling better leverage of the capabilities of
TSFMs and regression models while compensating for each other’s
limitations. Particularly,M provides high-fidelity forecasts of fu-
ture drivers ˆXforecast, and 𝑓 captures complex cross-variate rela-
tionships on the enriched feature space that includes these future
expectations. A comparison between the FutureBoosting paradigm
and other existing paradigms is presented in Figure 3.
4.2 FutureBoosting Framework for EPF
4.2.1 Framework Overview.We instantiate theFutureBoostingpara-
digm as a lightweight, plug-and-play framework for electricity price
forecasting, which uses TSFM forecasts as afeature augmentation
mechanism to enrich the input space for downstream regression.
The framework operates in two sequential stages:
Given historical dataY:𝐷 andX :𝐷 available at the end of day
𝐷, we employ pre-trained TSFMs in zero-shot mode to generate
forecasts for future-unavailable variables over the forecasting hori-
zon for day 𝐷+ 1. These forecasts serve as augmented features
that capture temporal patterns and provide expectations of future
supply-demand drivers. We then form an enriched feature setF𝐷+1
Lookback
V
T
Future
Exo
Endo
Temporal      Dependency
Variate      Dependency
Future InformedPast Only
(I) Auto-regressive Modeling (III) Covariate Awared Modeling
(II) Regression Modeling (IV) Ours: FutureBoosting
Known Future Exo
Future Endo
History Exo History Endo
Unknown Future Exo Forecast
Figure 3: Comparison of forecasting paradigms. Our Future-
Boosting paradigm first forecasts future-unavailable exoge-
nous variables using TSFM, then uses these augmented fea-
tures, along with future-available exogenous variables, for
regression-based target forecasting.
by combining the forecasts, domain-knowledge-guided constructed
factors (Section 4.2.3), and future available exogenous variables.
A tree-based regressor𝑓 (e.g., LightGBM) is trained on the en-
riched feature setF𝐷+1 to forecast electricity prices ˆyda 𝐷+1 =𝑓( F𝐷+1)
or ˆyrt 𝐷+1 =𝑓( F𝐷+1), enabling the model to capture complex cross-
variate interactions between TSFM-augmented features, domain-
constructed factors, and future-available exogenous variables.
4.2.2 TSFMs-Based Feature Augmentation.We apply a pre-trained
TSFMM to forecast a set of variables V=(Y :𝐷, X:𝐷) over the
horizon of day𝐷+ 1. For each𝑣∈V , such as system load, renewable
or thermal generation, M yields forecasts ˆ𝑣𝐷+1,1,..., ˆ𝑣𝐷+1,𝐻 for
all𝐻 timesteps. We assemble these into the augmented feature
block, which is then concatenated with domain-knowledge-guided
constructed factorsC 𝐷+1 and future available exogenous variables
Z𝐷+1 by Eq. 5:
ˆXforecast 𝐷+1 =M(Y :𝐷,X :𝐷)
F𝐷+1 =[ ˆXforecast 𝐷+1 ,C𝐷+1,Z𝐷+1] (5)
The role of ˆXforecast 𝐷+1 is twofold: (i) it supplies expectations of
future supply-demand drivers that are not directly observable at
planning time, and (ii) it encodes long-range temporal structure
via the TSFM’s pretrained knowledge. The setV is selected based
on domain knowledge: we include variables that are strongly cor-
related with electricity prices but are unavailable or uncertain at
planning time (e.g., system load, renewable generation). Optionally,
the TSFM can also forecast the target price series and include it as
an augmented feature, allowing the downstream regressor to refine
it using cross-variate information.

Domains
Energy
Environment
Transport
Nature Web
Industy Health
IoT
Sundial
Timer
Moirai
Chronos
TimesFM
TiRex
Frozen
TSFMs
Candidates Pretraining Data
Historical
Observations
Future
Expectations
Numerical Weather
Forecasting
Time Series Foundational Models
Future
Available
Grid Production
Plan
TSFMs-Based Feature Augmentation Lightweight Downstream Regression
Boosting Machine Linear Regression
Enriched Feature Set
Final Electricity Price Forecast
Figure 4: The pipeline of our FutureBoosting framework for electricity price forecasting. TSFM-augmented features, future
available exogenous variables, and the grid production plan form an enriched feature set for downstream regression models.
4.2.3 Domain-knowledge-guided Constructed Factors.Beyond raw
variables, we introduce domain-knowledge-guided constructed fac-
torsC𝐷+1 that aggregate market structure information for the next
trading day. These factors enable the downstream regressor to cap-
ture the supply-side structure more comprehensively by leveraging
a richer feature pool.
Thermal auction spacequantifies the effective capacity avail-
able for thermal generation in the day-ahead or real-time auction,
reflecting the headroom for conventional units to set clearing prices
when demand is high. It is computed as the difference between total
thermal capacity and committed thermal generation, normalized
by system load.
Renewable ratiois defined as the proportion of renewable gen-
eration (wind and solar) relative to total system load or generation.
It encodes the degree of renewable penetration, which strongly
affects price levels and volatility due to near-zero marginal costs
and intermittency. High renewable ratios typically correlate with
lower average prices but higher price volatility.
4.2.4 Lightweight Downstream Regression.Given the enriched fea-
ture setF𝐷+1, we train a regression model𝑓 to forecast day-ahead
or real-time electricity prices. In our Chinese electricity price fore-
casting experiments, we use a tree-based regressor, LightGBM [18],
to fit the enriched feature space and capture nonlinear interactions
among TSFM-augmented features, domain-constructed factors, and
future available exogenous variables. The regressor is trained to
minimize the mean squared error between predicted and observed
prices. For a training set of𝑁samples, the loss is
L= 1 𝑁 𝑁∑︁ 𝑖=1 (𝑦𝑖− ˆ𝑦𝑖)2,(6)
where𝑦𝑖 is the observed price and ˆ𝑦𝑖 =𝑓( F𝐷+1,𝑖) is the forecast.
Standard regularization strategies, including early stopping and
L2 regularization, are applied to reduce overfitting. The trained
model then yields forecasts ˆyda 𝐷+1 or ˆyrt 𝐷+1 for the target horizon.
Explainability tools, such as feature importance and Shapley values,
are used to analyze each feature’s contribution to forecasts.
4.3 Method Flexibility and Extensibility
Take the above EPF framework as an example, the FutureBoosting-
driven framework is intuitively flexible, enabling extension with
various TSFMs and regression models. Specifically, both univariate
TSFMs (like TimerXL and Sundial) and multivariate TSFMs (like
Chronos2) are supported. For the regression model, any regressor,
such as tree-based methods like XGBoost [ 9] and Random For-
est [34], linear models [28, 33], or other learners, can be applied in
the FutureBoosting-driven framework. To demonstrate flexibility,
we conduct comprehensive experiments using several state-of-the-
art TSFMs on online data from China. Besides, additional experi-
ments on public datasets are also provided in Section 5.2.2, where
another regression model is adopted.
5 Experiments
5.1 Experimental Settings
We introduce a real-world datasetShanxiand a public bench-
markRealEfor the evaluation of electricity price forecasting.
Shanxibenchmark includes actual industrial electricity market
data and weather conditions collected from Shanxi Province, China.
Two price objectives in the Shanxi dataset, namely the“day-ahead
clearing price”and the“real-time clearing price”, are included in
a monthly rolling evaluation from January to December in 2025.
RealEis a publicly presented benchmark in previous work [ 36]
with sufficient spatial and temporal scope. We use hourly data from
France (FR) and Germany (DE) for evaluation, following the offi-
cial split protocol. AverageMSEandMAEare reported for fair
comparison. Zero-shot TSFM inference and covariate-only regres-
sion are introduced as baselines. We also fine-tune Chronos2 [3]
following the official implementation as a representative baseline
for fine-tuned TSFMs. All inputs comply with the planning-time
availability constraint to avoid leakage. Dataset details, feature lists,
baseline setups, and implementation are in Appendix B.
5.2 Forecasting Performance
5.2.1ShanxiDay-ahead and Real-time Results.Table 2 summa-
rizes the 12-month rolling evaluation onShanxifor both day-ahead
and real-time forecasting.FutureBoostingachieves consistent im-
provements compared to zero-shot TSFM inference and regression
models on exogenous variables. Relative to zero-shot TSFMs,Future-
Boostingreduces MSE/MAE by45.43%/32.40%for day-ahead and
39.27%/24.98%for real-time relative to the corresponding zero-shot
TSFM baselines (ΔZS in Table 2). Relative to regression models on

Table 2: China 12-month summary (Day-ahead on the left; Real-time on the right). For each metric: Val is the raw score; ΔLGBM
is the improvement vs LGBM (ic27);ΔZS is the improvement of FutureBoosting vs its corresponding zero-shot TSFM.
Method Day-ahead Real-time
MSE MAE MSE MAE
ValΔLGBMΔZS ValΔLGBMΔZS ValΔLGBMΔZS ValΔLGBMΔZS
LGBM (ic27) 35658.52 0.00% – 100.53 0.00% – 49182.67 0.00% – 121.63 0.00% –
TimerXL 76278.90 -113.91% – 162.69 -61.83% – 86353.72 -75.58% – 171.63 -41.11% –
+ FutureBoosting 33978.45 +4.71% +55.45% 94.78 +5.72% +41.74% 44522.21 +9.48% +48.44% 117.10 +3.72% +31.77%
Sundial 62979.60 -76.62% – 143.60 -42.84% – 72219.22 -46.84% – 154.30 -26.86% –
+ FutureBoosting 35586.43 +0.20% +43.50% 97.09 +3.42% +32.39% 45415.52 +7.66% +37.11% 117.45 +3.44% +23.88%
Chronos2(mv) 63465.48 -77.98% – 144.60 -43.84% – 72517.75 -47.45% – 160.76 -32.17% –
+ FutureBoosting 34344.18 +3.69% +45.89% 94.90 +5.60% +34.37% 46697.19 +5.05% +35.61% 118.93 +2.22% +26.02%
Chronos2(future) 52197.23 -46.38% – 137.00 -36.27% – 64820.38 -31.80% – 162.88 -33.91% –
+ FutureBoosting 35315.01 +0.96% +32.34% 97.14 +3.37% +29.09% 46683.65 +5.08% +27.98% 119.53 +1.73% +26.61%
TimesFM 66423.97 -86.28% – 138.97 -38.24% – 81627.66 -65.97% – 154.98 -27.42% –
+ FutureBoosting 35411.86 +0.69% +46.69% 95.04 +5.46% +31.61% 46778.28 +4.89% +42.69% 118.04 +2.95% +23.84%
Moirai2 65750.80 -84.39% – 137.58 -36.85% – 79852.29 -62.36% – 155.49 -27.84% –
+ FutureBoosting 34930.18 +2.04% +46.87% 95.73 +4.77% +30.42% 45987.65 +6.50% +42.41% 117.70 +3.23% +24.30%
TiRex 67450.65 -89.16% – 133.14 -32.44% – 79122.98 -60.88% – 143.93 -18.33% –
+ FutureBoosting 35543.37 +0.32% +47.30% 96.94 +3.57% +27.19% 46944.86 +4.55% +40.67% 117.35 +3.52% +18.47%
Avg Improve–+1.80% +45.43%–+4.56% +32.40%–+6.17% +39.27%–+2.97% +24.98%
exogenous variables,FutureBoostingimproves day-ahead MSE/MAE
by1.80%/4.56%and real-time MSE/MAE by6.17%/2.97%compared
with LightGBM (ΔLGBM), with larger gains on the more volatile
real-time task. Such results demonstrate the effectiveness ofFuture-
Boostingin practical electricity price forecasting.
Among all variants, TimerXL + FutureBoosting achieves the
best overall performance, reaching 33978.45 MSE and 94.78 MAE
for day-ahead, and 44522.21 MSE and 117.10 MAE for real-time.
Month-wise results are provided in Table 9 (day-ahead) and Table 10
(real-time) in the appendix.
5.2.2RealEFrance and Germany Results.Table 3 reports results
on RealE for France (FR) and Germany (DE). UnlikeShanxi, zero-
shot TSFMs generally outperform the covariate-only regressors on
RealE, suggesting that temporal dependency is more dominant.
FutureBoostingconsistently brings additional improvements over
zero-shot TSFMs and regression models on exogenous variables.
Relative to zero-shot TSFMs,FutureBoostingimproves MSE/MAE by
16.92%/8.41%on FR and36.52%/18.52%on DE ( ΔZS). Relative to
regression models on exogenous variables,FutureBoostingachieves
substantial gains as well, improving MSE/MAE by85.54%/58.24%
on FR and87.00%/63.06%on DE ( ΔLinear). Overall, Chronos2 +
FutureBoosting performs best, achieving MSE/MAE of 2.90/1.11 on
FR and 1.49/0.87 on DE.
5.3 Ablation Studies
5.3.1 Regressor Choices.Table 4 compares downstream regression
models under the same TSFM backbone (Chronos2). InShanxi,
LightGBM yields clear gains over linear regression for both day-
ahead and real-time forecasting. For the day-ahead electricity price
forecast, MAE drops from 128.01 to 94.90, and MSE drops from
41165.74 to 34344.18. For the real-time electricity price forecast,
MAE drops from 142.88 to 118.93, and MSE drops from 50634.74 to
46697.19. These consistent improvements on both metrics suggest
a strongly nonlinear cross-variate mapping with interaction and
threshold effects.
InRealE, the linear regression is consistently better than Light-
GBM. For FR, MAE increases from 1.11 to 1.90, and MSE increases
from 2.90 to 6.21. For DE, MAE increases from 0.87 to 0.97, and
MSE increases from 1.49 to 2.13. This suggests that different data
distributions exhibit different preferences for regression modeling.
5.3.2 Fine-tuning Comparison.Figure 5 reports a fine-tuning com-
parison on Shanxi day-ahead forecasting (12-month average). We
select Chronos2, the latest state-of-the-art foundation model, as the
backbone and compare three settings: zero-shot inference, LoRA
fine-tuning, andFutureBoostingwith Chronos2 features. Both mul-
tivariate inputs and future available exogenous variables are con-
sidered for the Chronos2 backbone.
FutureBoostingsubstantially improves over Chronos2 zero-shot
inference. Under the multivariate setting, FutureBoosting reduces
MSE/MAE from 63310.40/144.53 to 34344.18/94.90. Adding future ex-
ogenous variables improves Chronos2 zero-shot inference (52197.23
MSE; 136.99 MAE).
Chronos2 LoRA fine-tuning with future exogenous variables
achieves the lowest MAE (83.71). This matches the MAE-based
model selection used in our fine-tuning pipeline. FutureBoosting

Table 3: Real-E 24-step summary (FR on the left; DE on the right). For each metric: Val is the raw score; ΔLinear is the
improvement vs Regression-only Linear;ΔZS is the improvement of FutureBoosting vs its corresponding zero-shot TSFM.
Method FR_24 DE_24
MSE MAE MSE MAE
ValΔLinearΔZS ValΔLinearΔZS ValΔLinearΔZS ValΔLinearΔZS
Linear 22.33 0.00% – 2.79 0.00% – 13.63 0.00% – 2.55 0.00% –
TimerXL 4.41 +80.25% – 1.37 +50.86% – 3.00 +77.99% – 1.21 +52.48% –
+ FutureBoosting 3.66 +83.61% +16.98% 1.26 +54.81% +7.72% 1.85 +86.43% +38.40% 0.95 +62.69% +21.36%
Sundial 4.00 +82.09% – 1.29 +53.73% – 4.23 +68.96% – 1.42 +44.23% –
+ FutureBoosting 3.45 +84.56% +13.75% 1.20 +56.96% +6.74% 2.32 +82.98% +45.12% 1.09 +57.18% +23.25%
Chronos2 3.61 +83.83% – 1.23 +55.89% – 2.28 +83.28% – 1.03 +59.55% –
+ FutureBoosting 2.90 +87.01% +19.53% 1.11 +60.19% +9.63% 1.49 +89.07% +34.55% 0.87 +65.83% +15.69%
TiRex 3.76 +83.16% – 1.24 +55.53% – 2.31 +83.06% – 1.05 +58.76% –
+ FutureBoosting 3.15 +85.90% +16.24% 1.14 +59.11% +8.58% 1.63 +88.05% +29.51% 0.90 +64.65% +13.87%
Moirai2 3.81 +82.94% – 1.25 +55.17% – 2.30 +83.13% – 1.07 +57.96% –
+ FutureBoosting 3.21 +85.63% +15.63% 1.16 +58.39% +7.86% 1.53 +88.78% +33.77% 0.88 +65.44% +17.16%
TimesFM 3.723 +83.33% – 1.239 +55.55% – 2.908 +78.67% – 1.188 +53.34% –
+ FutureBoosting 3.001 +86.56% +19.40% 1.116 +59.98% +9.95% 1.810 +86.72% +37.75% 0.953 +62.57% +19.76%
Avg Improve–+85.54% +16.92%–+58.24% +8.41%–+87.00% +36.52%–+63.06% +18.52%
Table 4: Regressor choice ablation with the same TSFM back-
bone (Chronos2).
Dataset Chronos2 + Linear Chronos2 + LGBM Gain
MSE MAE MSE MAE (best)
Shanxi (DA) 41165.74 128.0134344.18 94.90LGBM
Shanxi (RT) 50634.74 142.8846697.19 118.93LGBM
RealE (FR)2.90 1.116.21 1.90 Linear
RealE (DE)1.49 0.872.13 0.97 Linear
ZS (mv)ZS (fut)LoRA (mv)LoRA (fut)
FutureBoosting (mv)FutureBoosting (fut)
MSE
63310
52197
66163
35978 34344 35315
ZS (mv)ZS (fut)LoRA (mv)LoRA (fut)
FutureBoosting (mv)FutureBoosting (fut)
MAE
144.53
137.00
129.50
83.71
94.90 97.14
Pre-trained Model Zero-shot Pre-trained Model Adaptation FutureBoosting  (Ours)
Figure 5: Adaptation study on Shanxi day-ahead forecasting.
We compare zero-shot inference, LoRA fine-tuning, and Fu-
tureBoosting regression, with and without future-available
exogenous variables.
achieves the lowest MSE (34344.18), indicating a metric trade-off
between fine-tuning and regression in this setting.
Table 5: Efficiency comparison on Shanxi day-ahead (per
monthly window).
Method GPUs GPU Mem (MB) Total Time (s)
FutureBoosting 1×4090 11049.85 151.57
FutureBoosting (cached) CPU only 0.00 59.24
Fine-tuning 4×4090 24518.00 8867.00
5.4 Efficiency Analysis
FutureBoostingis a lightweight framework that achieves perfor-
mance comparable to finetuned TSFMs with much less computa-
tional resources. We compare the efficiency performance of “Chronos2
+ FutureBoost” and “Chronos2+LoRA Fintuning”, results demon-
strated in Table 5. AsFutureBoostingapply zero-shot TSFMs in-
ference strategy, we therefore further improve the inference ef-
ficiency through caching TSFM inference results. This caching
method makes the inference process ofFutureBoostingCPU-only,
making it highly applicable to resource-limited computing devices.
More detailed efficiency analyses are presented in Appendix C.
6 Deployed System Evaluation
Our proposed solution, based on theFutureBoostingparadigm, has
been deployed on Xingzhixun’s private IoTDB [40] server for real-
world online evaluation in December, 2025. As illustrated in Fig-
ure 6, data relevant to electricity price forecasting are gathered
and written into IoTDB every day. For convenience, the raw data
are reorganized and aligned from multiple sources into a single,
timestamp-indexed time series table. On each pricing day, theFu-
tureBoostingframework is invoked to infer the day-ahead clearing

price and the real-time clearing price with the given IoTDB data
series.
Raw Data Table
Online Input Online Inference
FutureBoosting
Result Table
Trader
Make Trading Plan
Optimize Bidding Strategy
Get Future Expectations
Expected Electricity Price
Figure 6: Application of FutureBoosting in Xingzhixun’s
IoTDB business server.
For clarity, we include the Shapley value calculation in our
analysis to demonstrate that our online deployment results are
robust and explainable. Figure 7 demonstrates deployed showcases
of the day-ahead clearing price in the Shanxi electricity market.
Compared with previous state-of-the-art time series foundational
models such as Chronos2,FutureBoostingoutperforms in overall
performance, especially for extreme electricity prices. Specifically,
Figure 7a presents an example of a low-price regime on trading
day December 17, 2025, and Figure 7b presents an example of a
high-price regime on trading day December 9, 2025. Sample-level
SHAP explanations are presented as waterfall plots, respectively.
The highlighted purple variables are TSFMs-based features gener-
ated by Chronos2, demonstrating the effectiveness of our enriched
feature set design. More detailed explainability assessments are
presented in Appendix D.
7 Conclusion and Future Works
We propose FutureBoosting, a hybrid AI paradigm for electricity
price forecasting that synergistically combines time-series foun-
dation models (TSFMs) with regression. By using frozen TSFM
forecasts as enriched forward-looking features, the method enables
regression models to capture both complex temporal dynamics and
cross-variate interactions. Evaluations on real-world market data
show that FutureBoosting consistently outperforms standalone
TSFMs and regression baselines. The framework is lightweight,
interpretable via XAI, and offers a practical, high-accuracy solution
for energy market decision-making.
Future directions include exploring automated feature selec-
tion methods to optimize the enriched feature set, particularly via
TSFMs. Methods such as LASSO regularization or Shapley-based
selection could help identify the most informative TSFM-derived
forecasts and exogenous variables, reducing redundancy and en-
hancing model efficiency. Additionally, dynamic or adaptive feature
selection strategies may be developed to respond to changing mar-
ket regimes, further improving robustness and interpretability in
real-world deployments.
References
[1] Taha Aksu, Gerald Woo, Juncheng Liu, Xu Liu, Chenghao Liu, Silvio Savarese,
Caiming Xiong, and Doyen Sahoo. 2024. Gift-eval: A benchmark for general time
series forecasting model evaluation.arXiv preprint arXiv:2410.10393(2024).
[2] Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken, Andreas Auer, Boran Han,
Pedro Mercado, Syama Sundar Rangapuram, Huibin Shen, Lorenzo Stella, Xiyuan
100 200 300
473.066 = transmission available
   capacity changnan
142.232 = day ahead clearing price
112 other features
 32957.629 = system load forecast
 16914.869 = forecast pv power
 23532.949 = thermal auction space
0.581 = renewable ratio load
22683.949 = thermal auction space st
 12 = month
0.458 = renewable ratio power
+10.09
−66.43
−50.11
−41.91
−40.82
−29.82
−20.41
−17.18
−9.05
−16.88 0
200
400
600
800
1000
1200
1400Price
E[f(X)] = 323.453
f(x) = 40.939
Time
2025-12-17
True
Chronos2
FutureBoosting
(a) Low-price regime: FutureBoosting corrects the Chronos2 high
bias and better follows the trough.
400 600 800
3.899 = wind speed 80m mean
44642.836 = forecast total power
112 other features
 3988.81 = forecast wind power
 9 = day
 44625.988 = forecast total power
 0.105 = renewable ratio load
 40635.82 = thermal auction space st
41540.82 = thermal auction space
0.089 =  renewable ratio power +224.03
+144.96
+130.37
+34.39
+21.4
+18.64
+16.97
+17.04
−17.59
−16.41
Time
0
200
400
600
800
1000Price
True
Chronos2
FutureBoosting
2025-12-09
E[f(X)] = 323.453
f(x) = 897.258
(b) High-price regime: FutureBoosting amplifies the forecast and
better matches the spike.
Figure 7: Sample SHAP explanations on deployed data. The
TSFM-based feature derived from Chronos2 is highlighted.
Zhang, Mononito Goswami, Shubham Kapoor, Danielle C. Maddix, Pablo Guerron,
Tony Hu, Junming Yin, Nick Erickson, Prateek Mutalik Desai, Hao Wang, Huzefa
Rangwala, George Karypis, Yuyang Wang, and Michael Bohlke-Schneider. 2025.
Chronos-2: From Univariate to Universal Forecasting.CoRRabs/2510.15821
(2025). arXiv:2510.15821 doi:10.48550/ARXIV.2510.15821
[3] Abdul Fatir Ansari, Lorenzo Stella, Caner Turkmen, Xiyuan Zhang, Pedro
Mercado, Huibin Shen, Oleksandr Shchur, Syama Sundar Rangapuram, Sebas-
tian Pineda Arango, Shubham Kapoor, Jasper Zschiegner, Danielle C. Maddix,
Michael W. Mahoney, Kari Torkkola, Andrew Gordon Wilson, Michael Bohlke-
Schneider, and Yuyang Wang. 2024. Chronos: Learning the Language of Time
Series.ArXivabs/2403.07815 (2024). https://api.semanticscholar.org/CorpusID:
268363551
[4] Andreas Auer, Patrick Podest, Daniel Klotz, Sebastian Böck, Günter Klambauer,
and Sepp Hochreiter. 2025. TiRex: Zero-Shot Forecasting Across Long and Short
Horizons with Enhanced In-Context Learning.CoRRabs/2505.23719 (2025).
arXiv:2505.23719 doi:10.48550/ARXIV.2505.23719
[5] Tim Bollerslev. 1986. Generalized Autoregressive Conditional Heteroskedasticity.
Journal of Econometrics31, 3 (April 1986), 307–327. doi:10.1016/0304-4076(86)
90063-1
[6] G. E. P. Box, Gwilym M. Jenkins, Gregory C. Reinsel, and Greta M. Ljung. 1978.
Time Series Analysis: Forecasting and Control.The Statistician27 (1978), 265–265.
https://api.semanticscholar.org/CorpusID:62556607
[7] George E. P. Box, Gwilym M. Jenkins, Gregory C. Reinsel, and Greta M. Ljung.
2015.Time Series Analysis: Forecasting and Control. John Wiley & Sons.
[8] Alexander L Burton. 2021. OLS (Linear) regression.The encyclopedia of research
methods in criminology and Criminal Justice2 (2021), 509–514.
[9] Tianqi Chen and Carlos Guestrin. 2016. XGBoost: A Scalable Tree Boosting Sys-
tem.Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining(2016). https://api.semanticscholar.org/CorpusID:
4650265

[10] Abhimanyu Das, Weihao Kong, Rajat Sen, and Yichen Zhou. 2024. A decoder-
only foundation model for time-series forecasting. InForty-first International
Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024.
OpenReview.net. https://openreview.net/forum?id=jn2iTJas6h
[11] Guzmán Díaz, José Coto, and Javier Gómez-Aleixandre. 2019. Prediction and
explanation of the formation of the Spanish day-ahead electricity price through
machine learning regression.Applied Energy(2019). https://api.semanticscholar.
org/CorpusID:115447108
[12] Pedro M. Domingos. 2012. A few useful things to know about machine learning.
Commun. ACM55 (2012), 78 – 87. https://api.semanticscholar.org/CorpusID:
2559675
[13] Everette S Gardner Jr. 1985. Exponential smoothing: The state of the art.Journal
of forecasting4, 1 (1985), 1–28.
[14] Isabelle M Guyon and André Elisseeff. 2003. An Introduction to Variable
and Feature Selection.J. Mach. Learn. Res.3 (2003), 1157–1182. https:
//api.semanticscholar.org/CorpusID:379259
[15] Ahmed MA Haidar, Lai Carmen, and Kashem M Muttaqi. 2021. A market frame-
work for energy bidding decision-making strategy to provide a competitive
mechanism in the context of deregulated electricity market. In2021 IEEE 4th
International Conference on Computing, Power and Communication Technologies
(GUCON). IEEE, 1–7.
[16] Marti A. Hearst, Susan T Dumais, Edgar Osuna, John Platt, and Bernhard
Scholkopf. 1998. Support vector machines.IEEE Intelligent Systems and their
applications13, 4 (1998), 18–28.
[17] Richard M Heiberger and Erich Neuwirth. 2009. Polynomial regression. InR
through excel: a spreadsheet interface for statistics, data analysis, and graphics.
Springer, 269–284.
[18] Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma,
Qiwei Ye, and Tie-Yan Liu. 2017. Lightgbm: A highly efficient gradient boosting
decision tree.Advances in neural information processing systems30 (2017).
[19] Daniel S Kirschen and Goran Strbac. 2018. Fundamentals of Power System
Economics.John Wiley & Sons(2018).
[20] Maurice Kraus, Felix Divo, Devendra Singh Dhami, and Kristian Kersting. 2024.
xLSTM-Mixer: Multivariate Time Series Forecasting by Mixing via Scalar Mem-
ories.CoRRabs/2410.16928 (2024). arXiv:2410.16928 doi:10.48550/ARXIV.2410.
16928
[21] Max Kuhn and Kjell Johnson. 2013. Applied Predictive Modeling. https://api.
semanticscholar.org/CorpusID:60246745
[22] Jesus Lago, Fjo De Ridder, Peter Vrancx, and Bart De Schutter. 2018. Forecasting
spot electricity prices: Deep learning approaches and empirical comparison of
traditional algorithms.Applied Energy221 (2018), 386–405.
[23] Jesus Lago, Grzegorz Marcjasz, Bart De Schutter, and Rafał Weron. 2021. Fore-
casting day-ahead electricity prices: A review of state-of-the-art algorithms, best
practices and an open-access benchmark.Applied Energy293 (2021), 116983.
[24] Yifan Li, Yifan Zhang, Yifan Zhang, and Yifan Zhang. 2024. Deep Learning-Based
Electricity Price Forecast for Virtual Bidding in Wholesale Electricity Market.
arXiv preprint arXiv:2412.00062(2024).
[25] Chenghao Liu, Taha Aksu, Juncheng Liu, Xu Liu, Hanshu Yan, Quang Pham,
Silvio Savarese, Doyen Sahoo, Caiming Xiong, and Junnan Li. 2025. Moirai 2.0:
When Less Is More for Time Series Forecasting.CoRRabs/2511.11698 (2025).
arXiv:2511.11698 doi:10.48550/ARXIV.2511.11698
[26] Yong Liu, Guo Qin, Xiangdong Huang, Jianmin Wang, and Mingsheng Long.
2025. Timer-XL: Long-Context Transformers for Unified Time Series Forecasting.
InThe Thirteenth International Conference on Learning Representations, ICLR 2025,
Singapore, April 24-28, 2025. OpenReview.net. https://openreview.net/forum?id=
KMCJXjlDDr
[27] Yong Liu, Guo Qin, Zhiyuan Shi, Zhi Chen, Caiyin Yang, Xiangdong Huang, Jian-
min Wang, and Mingsheng Long. 2025. Sundial: A Family of Highly Capable Time
Series Foundation Models. InForty-second International Conference on Machine
Learning, ICML 2025, Vancouver, BC, Canada, July 13-19, 2025. OpenReview.net.
https://openreview.net/forum?id=LO7ciRpjI5
[28] Gary C McDonald. 2009. Ridge regression.Wiley Interdisciplinary Reviews:
Computational Statistics1, 1 (2009), 93–100.
[29] John Ashworth Nelder and Robert WM Wedderburn. 1972. Generalized linear
models.Journal of the Royal Statistical Society Series A: Statistics in Society135, 3
(1972), 370–384.
[30] Yuqi Nie, Nam H. Nguyen, Phanwadee Sinthong, and Jayant Kalagnanam. 2023.
A Time Series is Worth 64 Words: Long-term Forecasting with Transformers.
InThe Eleventh International Conference on Learning Representations, ICLR 2023,
Kigali, Rwanda, May 1-5, 2023. OpenReview.net. https://openreview.net/forum?
id=Jbdc0vTOcol
[31] Boris N. Oreshkin, Dmitri Carpov, Nicolas Chapados, and Yoshua Bengio. 2019.
N-BEATS: Neural basis expansion analysis for interpretable time series forecast-
ing.ArXivabs/1905.10437 (2019). https://api.semanticscholar.org/CorpusID:
166228758
[32] Fabian Pedregosa, Gaël Varoquaux, Alexandre Gramfort, Vincent Michel,
Bertrand Thirion, Olivier Grisel, Mathieu Blondel, Peter Prettenhofer, Ron Weiss,
Vincent Dubourg, et al . 2011. Scikit-learn: Machine learning in Python.the
Journal of machine Learning research12 (2011), 2825–2830.
[33] Jonas Ranstam and Jonathan A Cook. 2018. LASSO regression.Journal of British
Surgery105, 10 (2018), 1348–1348.
[34] Steven J Rigatti. 2017. Random forest.Journal of insurance medicine47, 1 (2017),
31–39.
[35] Deepak Kumar Saini, Akash Saxena, and Ramesh C. Bansal. 2016. Electricity
price forecasting by linear regression and SVM.2016 International Conference
on Recent Advances and Innovations in Engineering (ICRAIE)(2016), 1–7. https:
//api.semanticscholar.org/CorpusID:24576146
[36] Chen Shao, Michael Färber, Sebastian Pütz, Benjamin Schäfer, Yue Wang, Tobias
Käfer, Zhanbo Huang, and Zhenyi Zhu. 2025. Real-E: A Foundation Benchmark
for Advancing Robust and Generalizable Electricity Forecasting. InProceedings of
the 34th ACM International Conference on Information and Knowledge Management.
6523–6527.
[37] Oleksandr Shchur, Abdul Fatir Ansari, Caner Turkmen, Lorenzo Stella, Nick
Erickson, Pablo Guerron, Michael Bohlke-Schneider, and Yuyang Wang. 2025.
fev-bench: A Realistic Benchmark for Time Series Forecasting. (2025).
arXiv:2509.26468 [cs.LG]
[38] Yan-Yan Song and Ying Lu. 2015. Decision tree methods: applications for classifi-
cation and prediction.Shanghai archives of psychiatry(2015).
[39] Alan O Sykes. 1993. An introduction to regression analysis. (1993).
[40] Chen Wang, Jialin Qiao, Xiangdong Huang, Shaoxu Song, Haonan Hou, Tian
Jiang, Lei Rui, Jianmin Wang, and Jiaguang Sun. 2023. Apache iotdb: A time
series database for iot applications.Proceedings of the ACM on Management of
Data1, 2 (2023), 1–27.
[41] Linian Wang, Jianghong Liu, Huibin Zhang, and Leye Wang. 2024. Revisit-
ing Day-ahead Electricity Price: Simple Model Save Millions.arXiv preprint
arXiv:2405.14893(2024).
[42] Rafał Weron. 2014. Electricity price forecasting: A review of the state-of-the-
art with a look into the future.International journal of forecasting30, 4 (2014),
1030–1081.
[43] Ailing Zeng, Mu-Hwa Chen, L. Zhang, and Qiang Xu. 2022. Are Transformers
Effective for Time Series Forecasting?. InAAAI Conference on Artificial Intelligence.
https://api.semanticscholar.org/CorpusID:249097444
A FutureBoosting Framework
Algorithm 1 formalizes the core logic of the FutureBoosting frame-
work under theFutureBoostingparadigm:Stage 1uses an auto-
regressive model such as a state-of-the-art TSFM to forecast future-
unavailable variables and form an enriched feature set;Stage 2
trains a regression model on that feature set to predict day-ahead
or real-time prices.
Algorithm 1FutureBoosting Framework
Require: Historical target Y:𝐷, historical exogenous variables
X:𝐷, future-forecast exogenous variablesZ𝐷+1; TSFM (or auto-
regressive forecaster)M; variate listV to forecast; domain-
constructed factorsC 𝐷+1; regression model𝑓
Ensure:Price forecasts ˆyda 𝐷+1 or ˆyrt 𝐷+1
Stage 1: Auto-Regressive Feature Augmentation
1:foreach variate𝑣∈Vdo
2: RunM in zero-shot mode onV(Y:𝐷, X:𝐷) to produce fore-
casts ˆ𝑣𝐷+1,1,..., ˆ𝑣𝐷+1,𝐻 for day𝐷+1
3:end for
4:Assemble augmented features: ˆXforecast 𝐷+1 ←{ ˆ𝑣𝐷+1,·}𝑣∈V
5:Form enriched feature set:F 𝐷+1←[ ˆXforecast 𝐷+1 ,C𝐷+1,Z𝐷+1]
Stage 2: Cross-Variate Regression
6: Train regressor𝑓 onF𝐷+1 (and historical labels) to minimize
forecasting error
7:Forecast: ˆyda 𝐷+1←𝑓(F 𝐷+1)or ˆyrt 𝐷+1←𝑓(F 𝐷+1)
8:return ˆyda 𝐷+1 or ˆyrt 𝐷+1

Table 6: Key difficulty indicators of Shanxi electricity prices
in 2025. Higher values indicate more challenging dynamics.
Indicator Day-ahead Real-time
Tail ratio𝑝99/𝑝504.86 5.33
Extreme freq.P(𝑝>1000)5.45% 5.88%
Excess kurtosis 5.05 5.39
Jump size𝑝99(|Δ𝑝|)399.8 439.9
Jump freq.P(|Δ𝑝|>200)2.92% 3.33%
Drift (KSmax, m/m−1) 0.477 0.487
Risk shift (monthly p95 range) 763.9 1074.3
B Experimental Details
B.0.1 Datasets.Shanxi Electricity Price Dataset.We use a real-
world electricity market dataset from Shanxi, China, containing
both day-ahead and real-time clearing prices. The data is sampled
every 15 minutes. We perform D+1 forecasting at 00:00 each day
with a 96-step horizon. The test period covers January–December
2025 with rolling monthly evaluation: for each test month, we train
on the previous 12 months, validate on the previous 2 months, and
test on the current month. To match real-world trading settings,
we restrict Shanxi experiments to workdays and exclude dates that
fall on Chinese statutory holidays. Both day-ahead and real-time
settings follow the same split. For direct regression on Shanxi, we
use a selected set of 27 future-available exogenous variables (ic27),
which include market tightness indicators, system operation and
interconnection plans, renewable generation forecasts, and weather
and calendar variables. The complete covariate list is provided in
Appendix B.0.2. For scaling, LightGBM [18] is trained on the original
units of prices and exogenous variables, while TSFM inference
follows each model’s default preprocessing. All reported metrics
are computed on the original scale.
Table 6 summarizes key difficulty indicators computed over the
full year of 2025. In addition to the issues mentioned, the market is
markedly non-stationary: the worst-case month-to-month distribu-
tion shift is large (KSmax≈ 0.48), and the monthly high price level
varies substantially (p95 range up to 1074). These properties jointly
make forecasting challenging, especially under rolling evaluation,
where models must generalize across shifting regimes.
RealE Benchmark Dataset.We use the RealE benchmark [ 36]
and evaluate on the France (FR) and Germany (DE) subsets. Both
subsets are hourly, with the day-ahead price as the forecasting
target. We perform D+1 forecasting with a 24-hour horizon. The
FR subset spans January 2015 to June 2024, while the DE sub-
set spans October 2018 to April 2023. We split each subset into
train/validation/test sets in a 0.7/0.1/0.2 ratio and merge train+validation
when fitting regressors. For direct regression, we use 15 exogenous
variables for FR and 19 exogenous variables for DE; the full lists
are provided in Appendix B.0.2. Following the benchmark protocol,
RealE is standardized using mean and standard deviation computed
on the training split only, and the same statistics are applied to
validation and test splits to avoid leakage. All RealE results are
reported under this standardized evaluation setting.
B.0.2 Covariate Feature Lists.In this section, we summarize the co-
variate sets used fordirect regressionbaselines and FutureBoosting
regressors. For Shanxi, we use a curated set of 27 future-available
future exogenous variables (ic27). For RealE, we use 15 exogenous
variables (excluding the time index and the target), following the
data availability in the benchmark.
The future-available exogenous variables (ic27) used in the Shanxi
dataset are shown in Table 7. The future-available exogenous vari-
ables used in the RealE dataset are shown in Table 8.
B.0.3 Evaluation Metrics.We evaluate forecasting accuracy using
Mean Squared Error (MSE) and Mean Absolute Error (MAE). Given
the ground-truth prices{𝑦𝑡}𝑁 𝑡=1 and forecasts{ ˆ𝑦𝑡}𝑁 𝑡=1, we compute:
MSE= 1 𝑁 𝑁∑︁ 𝑡=1 (𝑦𝑡− ˆ𝑦𝑡)2,(7)
MAE= 1 𝑁 𝑁∑︁ 𝑡=1 |𝑦𝑡− ˆ𝑦𝑡|.(8)
For rolling evaluation on Shanxi, metrics are computed on each
monthly test window and then averaged across the 12 months.
B.0.4 Baselines.TSFM-only (zero-shot).We evaluate six pre-
trained time-series foundation models (TSFMs) in a zero-shot man-
ner: Sundial [27], TimerXL [26], Chronos2 [2], TiRex [4], Moirai2 [25],
and TimesFM [ 10]. All TSFMs forcast the day-ahead/real-time
price directly from historical context without any downstream
fine-tuning. Chronos2 is used in a multivariate setting with two
variants: (i) Chronos2(mv), which performs multivariate inference
using only historical exogenous variables and the target; and (ii)
Chronos2(future), which additionally takes the future-available
values of exogenous variables as future inputs during inference.
TSFM fine-tuning (LoRA).To benchmark task adaptation, we
include fine-tuned TSFM baselines based on Chronos2 using LoRA.
We evaluate two fine-tuning settings: (i) Chronos2-FT(mv), which
fine-tunes in a multivariate setting using historical exogenous vari-
ables and the target; and (ii) Chronos2-FT(future), which addition-
ally provides the future-available future exogenous variables as
future inputs during training and inference. All fine-tuned models
are evaluated by directly forecasting prices (without any down-
stream regressor).
Regressor-only (direct regression).We include a strong direct-
regression baseline that forecasts prices solely from the future-
available exogenous variables (without TSFM forecasts). On the
Shanxi dataset, we use LightGBM [18] with the selected 27 exoge-
nous variables (ic27). On RealE, we use Ridge regression with 15
exogenous variables for FR and 19 exogenous variables for DE.
B.0.5 Implementation Details.TSFM inference is performed on a
single NVIDIA RTX 4090 GPU, while the downstream regressor is
trained on CPU.
TSFM inference.We perform zero-shot inference with a D+1
forecasting horizon. Each TSFM follows its default sampling setup
for probabilistic forecasting, with a batch size of 16. We cache TSFM
forecasts to disk to avoid repeated inference across runs. For the
input context, we use model-specific historical window lengths
in our implementation: 2880 for Sundial, 2048 for Chronos2 and
TimesFM, and 1440 for the remaining TSFMs (including TimerXL,
TiRex, and Moirai2).

Table 7: The set of 27 future-available exogenous variables (ic27) used as direct inputs to the regressor on the Shanxi dataset.
Category Variables
Market tightness & constructed
trading factors
thermal_auction_space, thermal_auction_space_st, renewable_ratio_load, renewable_ratio_power
System operation &
interconnection plans
system_load_forecast, day_ahead_interconnection_plan_total, non_market_unit_output,
transmission_available_capacity_yanhuai
Renewable / generation
forecasts
forecast_total_power, forecast_wind_power, forecast_pv_power, forecast_new_energy_total
Calendar variables month, weekday, day
Weather variables (summary
statistics)
dew_point_2m_mean, dew_point_2m_max, dew_point_2m_min, temperature_2m_mean, temperature_2m_max,
relative_humidity_2m_mean, cloud_cover_low_max, precipitation_probability_mean, extraterrestrial_ghi_mean,
surface_pressure_mean, pressure_msl_mean, pressure_msl_min
Table 8: Exogenous variables used for direct regression on RealE.
FR Variables (15) DE Variables (19)
System / load
genf_Scheduled Generation
ntc_Net Position
total_Day-ahead Total Load Forecast
total_Actual Total Load
System / load
genf_Scheduled Generation
ntc_Net Position
total_Actual Total Load
Fuel-type
generation
Biomass – Actual Aggregated
Fossil Gas – Actual Aggregated
Fossil Hard coal – Actual Aggregated
Fossil Oil – Actual Aggregated
Hydro Pumped Storage – Actual Aggregated
Hydro Run-of-river and poundage – Actual Aggregated
Hydro Water Reservoir – Actual Aggregated
Nuclear – Actual Aggregated
Solar – Actual Aggregated
Waste – Actual Aggregated
Wind Onshore – Actual Aggregated
Fuel-type
generation
Biomass – Actual Aggregated
Fossil Brown coal/Lignite – Actual Aggregated
Fossil Gas – Actual Aggregated
Fossil Hard coal – Actual Aggregated
Fossil Oil – Actual Aggregated
Geothermal – Actual Aggregated
Hydro Pumped Storage – Actual Aggregated
Hydro Run-of-river and poundage – Actual Aggregated
Hydro Water Reservoir – Actual Aggregated
Nuclear – Actual Aggregated
Other renewable – Actual Aggregated
Solar – Actual Aggregated
Waste – Actual Aggregated
Wind Offshore – Actual Aggregated
Wind Onshore – Actual Aggregated
Other – Actual Aggregated
Regressor training.In Shanxi, we use LightGBM with 30,000
boosting rounds and 1,000 early-stopping rounds. Key hyperparam-
eters are: learning rate 0.05, num_leaves 63, feature_fraction 0.9,
bagging_fraction 0.8, bagging_freq 5, and min_gain_to_split 0.08,
with 32 CPU threads and random seed 42. In RealE, we use Ridge
regression with default hyperparameters from scikit-learn [32].
C Detailed Efficiency Analysis
We report end-to-end efficiency on Shanxi day-ahead forecasting at
the monthly-window level. Our FutureBoosting pipeline instanti-
ates Chronos2 inference once per window, then trains a lightweight
regressor and evaluates on the same window. To contextualize the
computational cost, we compare FutureBoosting against LoRA fine-
tuning under the same monthly setting and summarize the results
in Table 5.
Without caching, TSFM inference takes 96.37s with a peak GPU
memory allocation of 11,049.85 MB (peak reserved 12,142 MB). The
remaining stages are comparatively lightweight: feature construc-
tion takes 2.12s, LightGBM training takes 29.04s, and test-time
evaluation takes 0.90s. Optional SHAP analysis adds 23.14s. Overall,
the measured end-to-end runtime for one month is 151.57s, with a
peak process CPU RSS of 2,058 MB.
With cached TSFM forecasts enabled, the same month reduces
the inference stage to 4.24s and eliminates GPU usage in that step
(0 MB peak allocation), while keeping the downstream cost similar:
feature construction 2.17s, LightGBM training 29.23s, evaluation
0.72s, and SHAP 22.88s. This yields a total runtime of 59.24s per
month, with a peak process CPU RSS of 1,295 MB.
In contrast, LoRA fine-tuning requires multi-GPU training. For
the same monthly window, our LoRA setting uses 4× RTX 4090 and
takes approximately 2h 27m 47s end-to-end, with a monitored peak

GPU memory allocation of 24,518 MB (Table 5). Overall, fine-tuning
incurs substantially higher wall-clock time and GPU resource de-
mands, whereas FutureBoosting keeps the expensive TSFM infer-
ence cacheable and shifts most computation to efficient regression
and evaluation.
D Detailed Explainability Assessments
We assess interpretability for Shanxi day-ahead electricity price
forecasting by applying SHAP to the downstream regressor in Fu-
tureBoosting. All explanations are computed on the final LightGBM
model trained on the enriched feature space, which combines TSFM
rollouts with future-available exogenous variables. We report both
global feature importance and instance-level attributions.
Global explanations.We compute SHAP values on the held-
out test split in the rolling evaluation and summarize the results
with two complementary global views in Fig. 8 and Fig. 9.
Fig. 8 presents a beeswarm distribution for the top features,
where each point corresponds to one test sample and the horizontal
axis indicates the signed SHAP contribution to the forecast. The
color encodes the raw feature value from low to high, revealing
how feature magnitude relates to positive or negative impacts on
the model output.
Fig. 9 reports the mean absolute SHAP values, providing an
overall importance ranking across all test samples. Across both
views, the most influential drivers are renewable-ratio variables
and thermal-auction-space indicators, indicating that renewable
availability and supply tightness play central roles in the regres-
sor corrections. The Chronos2-derived day-ahead clearing price
forecast feature is highlighted to distinguish TSFM-derived signals
from other exogenous variables, and it consistently appears among
the top drivers, suggesting that the final model leverages the TSFM
forecast while still relying substantially on domain exogenous in-
formation.
-100 0 100 200 300
SHAP value (impact on model output)
cloud cover low mean
system load forecast
forecast pv power
day ahead clearing price
forecast wind power
month
thermal auction space
renewable ratio load
thermal auction space st
renewable ratio power
Low
High
Feature value
Figure 8: Global SHAP explanations on the test split. The
Chronos2-derived forecast feature is highlighted to distin-
guish TSFM-predicted drivers from other exogenous vari-
ables.
Case studies.Fig. 7 shows two representative deployed in-
stances that illustrate how FutureBoosting improves extreme-regime
0 20 40 60 80
mean(|SHAP|)
renewable ratio power
thermal auction space st
renewable ratio load
thermal auction space
month
forecast wind power
day ahead clearing price
forecast pv power
system load forecast
cloud cover low mean
Figure 9: Global SHAP explanations on the test split. The
Chronos2-derived forecast feature is highlighted to distin-
guish TSFM-predicted drivers from other exogenous vari-
ables.
forecasting beyond the Chronos2-only baseline. Each instance is
presented with two aligned views. The left view is a SHAP waterfall
for the selected step marked by the dashed vertical line in the wave-
form. The right view plots the full trajectory over the same instance,
comparing the ground truth, the Chronos2 forecast, and the Future-
Boosting forecast. In the waterfall, the model output is expressed
as a global baseline plus feature-wise SHAP contributions, where
positive values increase the forecast and negative values decrease it.
The TSFM-based feature derived from Chronos2 is highlighted to
emphasize how the downstream regressor adjusts the base TSFM
forecast using exogenous drivers.
In the low-price regime shown in Fig. 7a, the true price drops
sharply while Chronos2 remains biased high. FutureBoosting fol-
lows the trough more closely, indicating systematic downward
corrections learned in the enriched feature space. The correspond-
ing waterfall attributes the correction primarily to large negative
contributions from renewable ratio power, month, thermal auc-
tion space st, and renewable ratio load, with additional negative
effects from thermal auction space and other supporting variables.
These attributions suggest that renewable-availability signals and
tightness-related indicators jointly drive the mitigation of overesti-
mation during extreme low-price events.
In the high-price regime shown in Fig. 7b, the true price ex-
hibits a pronounced spike that is underestimated by Chronos2.
FutureBoosting amplifies the forecast and better matches the ob-
served surge. The waterfall assigns most of the upward adjustment
to thermal auction space and thermal auction space st, together
with positive contributions from renewable ratio power and other
supply-demand drivers.
To further complement the qualitative evidence, we provide two
additional representative instances in Fig. 10, covering one low-
price and one high-price case from January 2025.

50 100 150 200 250 300
112 other features
26.558 = relative humidity 2m max
0.001 = precipitation probability std
23852.609 = thermal auction space
0.534 = renewable ratio load
22802.609 = thermal auction space st
−16.679 = dew point 2m max​
518.599 = day ahead clearing price
0.43 = renewable ratio power
17203.75 = forecast new energy total
112 other features
 relative humidity 2m max
 precipitation probability std
 thermal auction space
 renewable ratio load
 thermal auction space st
 dew point 2m max​
 day ahead clearing price
 renewable ratio power
 forecast new energy total
+35.77
−73.41
−71.96
−31.2
−23.15
−21.56
−9.7
−9.08
−6.78
−59.76
2025-01-10 00:00:00+08:002025-01-10 00:15:00+08:002025-01-10 00:30:00+08:002025-01-10 00:45:00+08:002025-01-10 01:00:00+08:002025-01-10 01:15:00+08:002025-01-10 01:30:00+08:002025-01-10 01:45:00+08:002025-01-10 02:00:00+08:002025-01-10 02:15:00+08:002025-01-10 02:30:00+08:002025-01-10 02:45:00+08:002025-01-10 03:00:00+08:002025-01-10 03:15:00+08:002025-01-10 03:30:00+08:002025-01-10 03:45:00+08:002025-01-10 04:00:00+08:002025-01-10 04:15:00+08:002025-01-10 04:30:00+08:002025-01-10 04:45:00+08:002025-01-10 05:00:00+08:002025-01-10 05:15:00+08:002025-01-10 05:30:00+08:002025-01-10 05:45:00+08:002025-01-10 06:00:00+08:002025-01-10 06:15:00+08:002025-01-10 06:30:00+08:002025-01-10 06:45:00+08:002025-01-10 07:00:00+08:002025-01-10 07:15:00+08:002025-01-10 07:30:00+08:002025-01-10 07:45:00+08:002025-01-10 08:00:00+08:002025-01-10 08:15:00+08:002025-01-10 08:30:00+08:002025-01-10 08:45:00+08:002025-01-10 09:00:00+08:002025-01-10 09:15:00+08:002025-01-10 09:30:00+08:002025-01-10 09:45:00+08:002025-01-10 10:00:00+08:002025-01-10 10:15:00+08:002025-01-10 10:30:00+08:002025-01-10 10:45:00+08:002025-01-10 11:00:00+08:002025-01-10 11:15:00+08:002025-01-10 11:30:00+08:002025-01-10 11:45:00+08:002025-01-10 12:00:00+08:002025-01-10 12:15:00+08:002025-01-10 12:30:00+08:002025-01-10 12:45:00+08:002025-01-10 13:00:00+08:002025-01-10 13:15:00+08:002025-01-10 13:30:00+08:002025-01-10 13:45:00+08:002025-01-10 14:00:00+08:002025-01-10 14:15:00+08:002025-01-10 14:30:00+08:002025-01-10 14:45:00+08:002025-01-10 15:00:00+08:002025-01-10 15:15:00+08:002025-01-10 15:30:00+08:002025-01-10 15:45:00+08:002025-01-10 16:00:00+08:002025-01-10 16:15:00+08:002025-01-10 16:30:00+08:002025-01-10 16:45:00+08:002025-01-10 17:00:00+08:002025-01-10 17:15:00+08:002025-01-10 17:30:00+08:002025-01-10 17:45:00+08:002025-01-10 18:00:00+08:002025-01-10 18:15:00+08:002025-01-10 18:30:00+08:002025-01-10 18:45:00+08:002025-01-10 19:00:00+08:002025-01-10 19:15:00+08:002025-01-10 19:30:00+08:002025-01-10 19:45:00+08:002025-01-10 20:00:00+08:002025-01-10 20:15:00+08:002025-01-10 20:30:00+08:002025-01-10 20:45:00+08:002025-01-10 21:00:00+08:002025-01-10 21:15:00+08:002025-01-10 21:30:00+08:002025-01-10 21:45:00+08:002025-01-10 22:00:00+08:002025-01-10 22:15:00+08:002025-01-10 22:30:00+08:002025-01-10 22:45:00+08:002025-01-10 23:00:00+08:002025-01-10 23:15:00+08:002025-01-10 23:30:00+08:002025-01-10 23:45:00+08:00
Time
0
200
400
600
800
1000
1200
1400
1600Price
True
Chronos2
Hybrid
E[f(X)] = 321.446
f(x) = 50.612
(a) A low-price case in January 2025.
400 600 800 1000
112 other features
43350.352 = forecast total power
1442.085 = non market unit output​
−14.133 = dew point 2m max​
0.047 = renewable ratio load
1667.79 = forecast new energy total
1443 = non market unit output
0.038 = renewable ratio power
43125.562 = thermal auction space
41682.562 = thermal auction space st
112 other features
 forecast total power
 non market unit output​
 dew point 2m max​
 renewable ratio load
 forecast new energy total
 non market unit output
 renewable ratio power
 thermal auction space
 thermal auction space st +345.41
+109.12
+67.71
+67.28
+46.38
+43.82
+31.81
+27.08
+15.92
+21.79
2025-01-16 00:00:00+08:002025-01-16 00:15:00+08:002025-01-16 00:30:00+08:002025-01-16 00:45:00+08:002025-01-16 01:00:00+08:002025-01-16 01:15:00+08:002025-01-16 01:30:00+08:002025-01-16 01:45:00+08:002025-01-16 02:00:00+08:002025-01-16 02:15:00+08:002025-01-16 02:30:00+08:002025-01-16 02:45:00+08:002025-01-16 03:00:00+08:002025-01-16 03:15:00+08:002025-01-16 03:30:00+08:002025-01-16 03:45:00+08:002025-01-16 04:00:00+08:002025-01-16 04:15:00+08:002025-01-16 04:30:00+08:002025-01-16 04:45:00+08:002025-01-16 05:00:00+08:002025-01-16 05:15:00+08:002025-01-16 05:30:00+08:002025-01-16 05:45:00+08:002025-01-16 06:00:00+08:002025-01-16 06:15:00+08:002025-01-16 06:30:00+08:002025-01-16 06:45:00+08:002025-01-16 07:00:00+08:002025-01-16 07:15:00+08:002025-01-16 07:30:00+08:002025-01-16 07:45:00+08:002025-01-16 08:00:00+08:002025-01-16 08:15:00+08:002025-01-16 08:30:00+08:002025-01-16 08:45:00+08:002025-01-16 09:00:00+08:002025-01-16 09:15:00+08:002025-01-16 09:30:00+08:002025-01-16 09:45:00+08:002025-01-16 10:00:00+08:002025-01-16 10:15:00+08:002025-01-16 10:30:00+08:002025-01-16 10:45:00+08:002025-01-16 11:00:00+08:002025-01-16 11:15:00+08:002025-01-16 11:30:00+08:002025-01-16 11:45:00+08:002025-01-16 12:00:00+08:002025-01-16 12:15:00+08:002025-01-16 12:30:00+08:002025-01-16 12:45:00+08:002025-01-16 13:00:00+08:002025-01-16 13:15:00+08:002025-01-16 13:30:00+08:002025-01-16 13:45:00+08:002025-01-16 14:00:00+08:002025-01-16 14:15:00+08:002025-01-16 14:30:00+08:002025-01-16 14:45:00+08:002025-01-16 15:00:00+08:002025-01-16 15:15:00+08:002025-01-16 15:30:00+08:002025-01-16 15:45:00+08:002025-01-16 16:00:00+08:002025-01-16 16:15:00+08:002025-01-16 16:30:00+08:002025-01-16 16:45:00+08:002025-01-16 17:00:00+08:002025-01-16 17:15:00+08:002025-01-16 17:30:00+08:002025-01-16 17:45:00+08:002025-01-16 18:00:00+08:002025-01-16 18:15:00+08:002025-01-16 18:30:00+08:002025-01-16 18:45:00+08:002025-01-16 19:00:00+08:002025-01-16 19:15:00+08:002025-01-16 19:30:00+08:002025-01-16 19:45:00+08:002025-01-16 20:00:00+08:002025-01-16 20:15:00+08:002025-01-16 20:30:00+08:002025-01-16 20:45:00+08:002025-01-16 21:00:00+08:002025-01-16 21:15:00+08:002025-01-16 21:30:00+08:002025-01-16 21:45:00+08:002025-01-16 22:00:00+08:002025-01-16 22:15:00+08:002025-01-16 22:30:00+08:002025-01-16 22:45:00+08:002025-01-16 23:00:00+08:002025-01-16 23:15:00+08:002025-01-16 23:30:00+08:002025-01-16 23:45:00+08:00
Time
0
200
400
600
800
1000
1200
1400Price
True
Chronos2
Hybrid
E[f(X)] = 321.446
f(x) = 1097.773
(b) A high-price case in January 2025.
Figure 10: Additional sample SHAP explanations on deployed
data. The TSFM-based feature derived from Chronos2 is high-
lighted.
E Month-wise Results on Shanxi
Tables 9 and 10 provide the detailed month-wise results for the 12
rolling test windows in 2025. For each TSFM, we report the zero-shot
forecast (ZS) and its corresponding FutureBoosting regressor (FBR)
for every month, where lower values indicate better performance.
Each month is listed with two rows (ZS/FBR) to facilitate a direct
within-window comparison.

Table 9: Shanxi Day-Ahead 12-month window-wise results comparing zero-shot (ZS) TSFM-only forecasts and their correspond-
ing FutureBoosting (FBR).
Window Type TimerXL Sundial Chronos2 (mv) Chronos2 (future) TimesFM Moirai2 TiRex
MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE
202501 ZS 96031.92 195.56 77180.33 163.32 89610.94 175.98 66888.00 159.64 73564.20 160.36 81880.01 166.92 79950.36 161.65 FBR 28336.35 89.36 21958.62 84.95 18692.07 77.39 20340.07 87.74 20774.21 79.08 19424.70 80.66 20981.86 83.95
202502 ZS 134084.19 237.77 121219.58 220.57 114767.00 220.21 92523.61 211.76 126918.32 213.88 123831.87 222.76 121434.01 210.61 FBR 40757.15 110.22 45136.53 123.09 44370.32 120.87 48430.27 125.53 44246.05 116.91 48259.19 119.29 43017.85 118.11
202503 ZS 93755.35 196.24 80372.27 185.39 78314.09 172.93 66959.59 161.66 97939.16 180.96 90217.22 173.04 95215.36 165.77 FBR 45468.58 109.31 42478.45 111.75 43072.86 109.83 46726.38 110.72 42435.10 110.51 48687.06 115.28 45406.77 115.15
202504 ZS 77669.32 175.90 57050.10 141.62 53054.38 137.56 41129.56 122.26 60371.87 133.42 58169.98 134.34 62035.25 128.32 FBR 26432.77 79.77 29912.20 83.65 30530.24 83.57 31365.62 84.79 33709.88 86.42 29063.96 83.90 34297.45 88.75
202505 ZS 93666.34 180.71 86903.53 172.03 100305.20 185.01 92857.96 192.45 86284.90 162.18 90186.08 166.77 87845.80 153.05 FBR 32690.44 92.38 37007.00 97.54 37003.55 98.47 36565.64 96.68 35779.71 96.44 31915.10 90.78 36821.45 97.27
202506 ZS 48227.93 128.14 25582.65 95.52 27434.78 92.98 24986.22 88.57 30333.88 94.76 30058.37 91.84 33013.53 88.16 FBR 21909.27 86.89 23753.56 86.64 24089.27 85.46 21861.27 76.54 20864.53 77.29 20510.49 77.03 22181.49 82.93
202507 ZS 47276.94 113.89 34349.32 94.85 35194.34 103.91 24992.95 97.87 37760.89 93.24 41461.06 96.68 45637.71 98.15 FBR 22805.03 85.41 28215.34 90.66 24555.22 87.92 32517.70 96.25 25388.54 86.02 24899.19 86.08 26646.30 88.50
202508 ZS 26194.18 92.84 18446.30 84.86 19041.06 79.95 22911.02 82.82 21042.63 82.44 16232.81 70.61 19955.39 73.31 FBR 31828.17 90.12 25673.99 77.76 28298.30 81.09 24676.54 84.59 31304.71 83.44 35594.87 92.77 30230.98 85.11
202509 ZS 58305.51 124.13 50975.25 115.60 54196.83 128.87 48346.62 120.97 55041.01 122.43 54495.37 118.30 54019.00 113.74 FBR 32633.16 75.44 39071.02 80.19 38111.77 80.32 31227.95 75.61 40301.52 81.39 37861.71 80.32 41216.20 83.26
202510 ZS 106548.72 218.57 88226.08 194.62 77523.35 183.72 54935.98 161.40 91218.39 188.55 87374.95 182.83 90006.81 185.27 FBR 79067.78 167.47 85247.65 173.37 81003.48 169.03 84240.63 175.93 87127.87 176.08 73088.76 163.71 81226.46 167.61
202511 ZS 33343.31 111.37 27710.86 100.95 27223.86 97.97 22383.87 86.41 27917.56 90.34 25812.17 82.76 26125.74 75.93 FBR 11194.69 55.77 9789.58 48.10 8740.34 49.97 11148.39 52.26 8581.90 47.50 11883.00 54.63 8719.66 48.81
202512 ZS 100243.11 177.10 87738.88 153.87 83058.95 155.21 67451.35 158.16 88694.82 145.02 89289.72 144.10 94168.80 143.73 FBR 34617.97 95.26 38793.17 107.41 33662.70 94.84 34679.67 99.04 34428.32 99.38 37974.19 104.36 35774.00 103.80
A VG ZS 76278.90 162.69 62979.60 143.60 63310.40 144.53 52197.23 137.00 66423.97 138.97 65750.80 137.58 67450.65 133.14 FBR 33978.45 94.78 35586.43 97.09 34344.18 94.90 35315.01 97.14 35411.86 95.04 34930.18 95.73 35543.37 96.94
Improve (%)+55.45 +41.74 +43.50 +32.39 +45.75 +34.34 +32.34 +29.09 +46.69 +31.61 +46.87 +30.42 +47.30 +27.19

Table 10: Shanxi Real-time 12-month window-wise results comparing zero-shot (ZS) TSFM-only forecasts and their correspond-
ing FutureBoosting (FBR).
Window Type TimerXL Sundial Chronos2 (mv) Chronos2 (future) TimesFM Moirai2 TiRex
MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE
202501 ZS 118895.21 217.91 97693.37 190.56 114730.62 199.96 99201.90 195.49 98345.31 188.98 114230.96 202.83 114310.87 198.35 FBR 23393.77 100.68 27793.07 107.87 28962.75 108.12 41628.91 127.75 31895.88 114.04 27384.44 106.69 34742.31 121.41
202502 ZS 120379.08 229.16 85619.59 181.18 90050.68 203.80 80630.58 209.08 98546.03 191.38 117523.33 222.87 97648.07 179.53 FBR 32541.10 119.51 36259.24 126.50 38276.06 124.70 37569.89 123.42 32796.34 116.31 35840.88 115.25 38160.78 117.90
202503 ZS 107854.53 206.39 95016.02 202.85 88038.66 191.04 77018.86 187.73 111121.30 196.46 102835.81 195.97 109298.64 178.06 FBR 65560.99 135.07 67539.49 135.37 63971.96 136.43 69542.25 137.31 64435.87 136.05 65943.71 137.51 68689.22 138.64
202504 ZS 82330.52 182.88 67713.56 151.20 68948.49 168.73 64970.55 177.79 80565.65 153.57 75139.75 150.78 76841.29 140.66 FBR 38817.92 116.73 43164.55 121.84 38725.26 106.06 49110.38 120.86 41578.67 106.84 38528.82 108.33 41703.71 107.60
202505 ZS 102967.35 188.26 89835.88 171.51 106919.77 212.81 108991.74 232.27 113641.81 184.17 97904.36 176.92 95134.62 155.97 FBR 45863.10 118.49 44887.32 117.20 49086.25 116.84 47795.90 121.09 48432.05 119.94 46761.93 122.08 53846.44 123.05
202506 ZS 65641.39 139.82 47375.07 121.01 47714.17 120.61 44323.24 120.88 48809.47 109.90 49823.53 115.69 52145.87 112.20 FBR 42519.09 110.62 44953.33 119.60 43102.85 118.05 40441.20 107.20 40049.48 108.22 43203.69 114.87 41016.73 110.74
202507 ZS 41142.87 108.49 30470.52 89.86 31539.87 99.73 27781.38 106.07 32773.53 87.15 41767.10 95.36 36157.71 87.12 FBR 25942.39 99.99 32145.62 99.94 22851.93 97.04 23634.30 92.29 25053.84 104.78 21023.51 93.36 26019.67 96.04
202508 ZS 31030.77 94.68 25916.09 90.20 26063.24 92.93 29037.41 97.29 33563.30 94.70 23631.02 79.13 28671.56 80.56 FBR 42816.39 108.70 36533.89 100.93 43829.60 107.10 36597.41 105.57 40358.88 104.96 45826.41 107.22 43251.67 105.40
202509 ZS 85633.09 156.08 78310.54 154.30 79575.40 165.89 76442.12 172.88 79838.22 146.30 86435.07 156.92 83710.00 146.00 FBR 57474.52 109.76 62770.34 110.22 63742.47 113.22 59888.76 114.83 64865.33 110.78 63983.58 113.40 63109.99 113.77
202510 ZS 143685.32 245.75 125149.12 234.85 91568.20 210.20 66799.12 180.18 155995.52 259.92 127427.50 228.15 134176.60 232.44 FBR 112637.92 203.07 105293.65 196.79 120206.91 215.92 102746.86 200.65 122923.08 214.33 115473.27 205.10 110535.59 199.50
202511 ZS 38809.75 120.18 36503.10 114.82 31784.27 107.45 28197.25 102.97 34545.62 99.15 31778.31 96.23 32763.18 87.15 FBR 16096.67 73.50 16402.15 74.61 16514.01 75.48 17205.48 71.43 16239.71 72.56 16502.11 76.04 15307.39 71.51
202512 ZS 97874.73 169.98 87027.78 149.20 93279.61 155.96 74450.43 171.96 91786.17 148.05 89730.76 145.00 88617.30 129.12 FBR 30602.62 109.11 27243.63 98.49 31096.27 108.19 34042.47 112.00 32710.28 107.72 31379.47 112.55 26954.77 102.59
A VG ZS 86353.72 171.63 72219.22 154.30 72517.75 160.76 64820.38 162.88 81627.66 154.98 79852.29 155.49 79122.98 143.93 FBR 44522.21 117.10 45415.52 117.45 46697.19 118.93 46683.65 119.53 46778.28 118.04 45987.65 117.70 46944.86 117.35
Improve (%)+48.44 +31.77 +37.11 +23.88 +35.61 +26.02 +27.98 +26.61 +42.69 +23.83 +42.41 +24.30 +40.67 +18.47
