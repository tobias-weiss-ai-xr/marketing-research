---
title: Liquid Neural Network Models for Natural Gas Spot Price Time-Series Forecasting
url: https://arxiv.org/abs/2604.24788
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Yiqian Liu
- Jiayi Niu
- Adam Kelleher
- Subhabrata Das
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.24788
pages: 10
chars: 50491
fetched_at: '2026-11-08T13:09:29+00:00'
kb_version: 1
---

# Liquid Neural Network Models for Natural Gas Spot Price Time-Series Forecasting

Liquid Neural Network Models for Natural Gas
Spot Price Time-Series Forecasting
Yiqian Liu, Jiayi Niu, Adam Kelleher, Subhabrata Das ∗
Department of Data Science, Columbia University
New York, NY , USA
*Corresponding author: sd2957@columbia.edu
Abstract—Natural gas is undoubtedly an essential component
of the global energy system. Accurate short-term forecasting of
natural gas price is challenging due to pronounced volatility
driven by seasonal demand patterns, geopolitical developments,
and shifting macroeconomic conditions. The nonlinear dynamics
and frequent regime changes can limit the effectiveness of
traditional time-series models. In this study, we explore the use
of Liquid Neural Networks (LNNs) for short-horizon forecasting
of the Henry Hub spot price, a primary benchmark for pricing.
LNNs are designed to adapt continuously to evolving temporal
patterns through dynamic internal state updates, making them
well suited for nonstationary price behavior . By improving
forecast accuracy in volatile market conditions, this work aims to
reduce uncertainty and enhance decision support across energy
trading and power market applications.
Index Terms—natural gas spot price; time-series forecasting;
liquid neural networks; machine learning
I. INTRODUCTION
A. Background and Motivation
Natural gas remains a cornerstone of the global energy
matrix, serving as a critical bridge fuel in the transition
toward low-carbon energy systems while providing baseload
reliability for power generation [1]. In the United States, the
Henry Hub spot price functions as the primary benchmark
for futures, options, and physical trading [2], making its
predictability of paramount importance to utility operators,
energy traders, and financial institutions alike.
The natural gas market is characterized by pronounced
volatility and nonstationary behavior driven by weather
shocks, geopolitical developments, and supply disruptions
[3]. Traditional econometric models such as ARIMA and
GARCH offer statistical interpretability, but are limited by
linear assumptions and stationarity conditions during periods
of structural change [4]. Rolling-window OLS addresses some
of this rigidity through adaptive re-estimation, yet remains
constrained by its linear functional form and cannot capture
the nonlinear dependencies and regime-dependent volatility
clustering characteristic of natural gas markets. Deep learning
approaches, particularly LSTM networks, improve on this by
modeling nonlinear temporal dependencies, but their fixed
internal dynamics limit responsiveness when market regimes
shift rapidly [5]. Thus, many existing approaches rely on
fixed or discretely updated parameters, limiting their ability to
continuously adapt to evolving market conditions. This study
examines whether adaptivity improves short-term forecast ac-
curacy compared to rolling-window linear regression.
B. Research Scope and Contributions
To address this gap, we formulate Henry Hub price
forecasting as a nonstationary time-series prediction problem
and investigate Liquid Neural Networks (LNNs) — recurrent
architectures whose dynamic time constants allow internal
states to adapt continuously to incoming information — as
a candidate solution. We construct a ten-and-a-half-year daily
dataset (January 2015–August 2025) integrating Henry Hub
spot prices with financial, energy, and operational variables,
and focus on next-day short-horizon forecasting rather than
long-term price projection.
This study makes three principal contributions. First, we
conduct a systematic comparison of five liquid neural archi-
tectures — LTC, Strict CfC, Hybrid CfC, CT-LTC, and a
standard LSTM benchmark — against a rolling-window linear
regression baseline for short-horizon Henry Hub forecasting.
Second, we employ a stratified expanding-window evaluation
protocol with Moving Block Bootstrap uncertainty quantifica-
tion to produce statistically reliable performance estimates that
account for temporal autocorrelation in nonstationary forecast
errors. Third, through controlled architectural comparison, we
identify which design characteristics — specifically, input-
conditioned timescale modulation versus fixed or calendar-
based step sizing — drive performance differences under the
high-frequency regime shifts that typify natural gas markets.
II. RELATEDWORK
Forecasting energy prices has been widely studied us-
ing both statistical and machine learning approaches. Early
econometric models, such as autoregressive and cointegration
frameworks, effectively captured short-term correlations but
struggled during periods of structural market change caused by
supply disruptions or policy shifts. Later, neural models such
as LSTM and GRU improved nonlinear pattern recognition
but often at the expense of interpretability and computational
stability. Several studies have proposed rolling-window regres-
sion frameworks to better handle time-varying relationships.
Dbouk and Jamali introduced a rolling estimation approach
for daily crude oil prices, where model parameters are re-
estimated within a fixed-length moving window to adapt to re-
cent market conditions while discarding outdated information
arXiv:2604.24788v1  [cs.LG]  24 Apr 2026

[6]. Artemovaet al.and Khanet al.similarly demonstrate that
rolling-window linear regression provides a strong baseline
for short-term forecasting of volatile energy commodities [7],
[8], supporting the principle that rolling estimation enhances
robustness and responsiveness — a design choice we adopt in
our baseline model. The challenge of applying deep learning
to volatile energy time-series has motivated a range of hybrid
and adaptive architectures. Daset al.propose a PCA-PR-
Seq2Seq-Adam-LSTM framework for power outage predic-
tion, demonstrating that structured preprocessing and temporal
architectures substantially improve robustness under abrupt
distributional shifts analogous to Henry Hub regime changes
[9]. Multi-headed recurrent networks tuned via meta-heuristic
optimization have also been applied to energy price forecast-
ing, reinforcing the broader insight that models adapting to
evolving dynamics outperform those with fixed parameters
[10]. The study most closely related to ours is Liuet al.[11],
who compare feedforward networks, support vector machines,
random forests, and LSTM for multi-step Henry Hub forecast-
ing. Their results establish LSTM as a strong neural baseline
and highlight systematic accuracy degradation with increasing
horizon. However, their recurrent dynamics remain governed
by fixed time scales, which may limit responsiveness under
abrupt regime shifts. Zaragozaet al.address adaptivity from
a different angle, proposing a time-varying graph learning
framework for electricity price forecasting in which inter-node
dependencies evolve dynamically [12], underscoring a broader
trend toward adaptive modeling in energy markets. Building
on this literature, we introduce Liquid Neural Networks —
recurrent architectures designed to capture fast-changing tem-
poral dependencies through adaptive internal dynamics with
fewer parameters and improved stability compared to standard
recurrent models [13], [14], making them particularly suitable
for the volatile, regime-prone behavior of Henry Hub spot
prices.
III. DATASET
A. Data
We utilize Henry Hub Natural Gas Spot Prices [15] as the
target variable. Since gas pricing is driven by a mix of supply,
demand, and market conditions, we construct a predictor set
combining fundamentals and market indicators. WTI crude
oil spot prices [16] serve as a benchmark for broader energy
market trends and cross-commodity substitution. U.S. Treasury
yield curve rates [17] — specifically the 2-year, 5-year, 10-
year, and 20-year maturities — capture macroeconomic and
capital cost conditions relevant to natural gas investment and
trading. The U.S. Dollar Index [18] reflects dollar strength,
which influences the competitiveness of U.S. LNG exports.
Equity-based measures, including the S&P Energy Index [19]
and the Dow Jones U.S. Coal Index [20], provide signals
of sector-wide sentiment and coal–gas substitution effects.
Firm-level production sentiment is proxied using daily stock
prices of EQT [21]. Finally, U.S. nuclear generation data
— represented by installed capacity, outage capacity (both
in megawatts), and percentage outage — reflects shifts in
electricity supply capacity where reductions in nuclear avail-
ability can increase residual demand for natural gas [22]. All
datasets were merged by date over the period January 6, 2015
to August 29, 2025. Variables with a high proportion of
missing observations — specifically Coal V olatility, USD
Index V olatility, the CBOE Crude Oil ETF V olatility Index
(VIX), Treasury 1.5 Month, Treasury 4 Month, S&P Energy
V olatility, Treasury 2 Month, and Treasury 30-Year rates —
were excluded due to insufficient daily coverage. At the ob-
servation level, 54 rows were removed from the original 2,699
daily observations (approximately 2.0%), primarily reflecting
missing values associated with market holidays, and including
three observations where the spot price level exceeded 5.5
standard deviations from the median. Large single-day return
spikes are deliberately retained, as they represent genuine
market events — most notably the February 2021 Winter
Storm Uri disruption — and removing them would introduce
survivorship bias into the forecasting evaluation.
The final dataset spans January 6, 2015 to August 29,
2025, contains 2,645 observations and 30 predictor features
for the standard neural models (29 for the CT-LTC variant,
which additionally excludes the lagged return to avoid target
leakage), with the daily natural gas spot price (USD per
MMBtu) as the target variable.
B. Exploratory Data Analysis
To characterize the empirical structure of the dataset, we
conduct exploratory analyses of the Henry Hub natural gas
spot price and selected energy and financial market indicators
over the period 2015–2025.
1) Henry Hub Natural Gas Spot Price Dynamics:Figure 1
presents the daily Henry Hub natural gas spot price together
with a 30-day moving average, with observations exceeding
the 95th percentile highlighted to emphasize periods of ex-
treme price behavior. The series exhibits pronounced volatility
and distinct regime changes, with particularly large price
dislocations during 2021–2022, reflecting heightened stress in
global energy markets.
Figure 1. Henry Hub Natural Gas Spot Price Trend (2015–2025)
2) Energy and Financial Market Performance:Figure 2
places Henry Hub in the energy and finance context. Compared
to other series, natural gas cumulative returns (black line)
exhibit extreme volatility, ranging from -80% to +220%, while
the USD Index (purple) barely moves beyond ±15%. Several

structural observations stand out. Coal (orange dashed) has lost
60–80% of its 2015 starting value. S&P 500 Energy (green)
and EQT (green dash-dot) track each other well, collapsing
during the COVID-19 pandemic and recovering in 2021–2022,
supporting the heatmap’s strong inter-feature correlations. En-
ergy commodity moves are least correlated with the USD
Index, the most stable series. The shaded event windows show
how external shocks change the return landscape: the COVID
crash erased cumulative gains across all series, the post-
COVID recovery saw divergent recoveries (energy equities
rebounded while coal did not), and the 2022 energy spike
produced the largest natural gas returns in the sample due to
the Russia-Ukraine conflict and European supply disruptions.
Figure 2. Energy and Financial Market Performance (2015–2025)
3) Feature Correlations:Figure 3 shows the pairwise
Pearson correlation structure between the Henry Hub spot
price and selected predictor variables. The heatmap shows
weak linear correlations between the spot price and most
individual predictors, with the exception of capacity (MW) and
WTI crude oil spot prices. In contrast, several predictors show
strong inter-feature correlations, particularly U.S. Treasury
yields, coal prices, energy equity indices, the US Dollar
Index, and EQT stock prices. These patterns demonstrate
the presence of multicollinearity and complex cross-market
relationships, providing empirical context for the forecasting
problem addressed in this study.
Figure 3. Correlation Heatmap
4) Rolling 30-Day Volatility:Figure 4 illustrates the re-
alized volatility of natural gas spot returns, calculated as
the 30-day rolling standard deviation. The plot demonstrates
distinct volatility clustering, a phenomenon where periods of
relative stability are interrupted by sudden, sustained regimes
of high variance. This behavior provides strong evidence
of non-stationarity in the data’s second moment (variance).
Unlike a stationary process, where volatility would oscillate
around a constant mean, the spot prices exhibit heteroskedas-
ticity—meaning the dispersion of returns is time-dependent.
These structural shifts in market risk confirm that the under-
lying data distribution changes over time, so it’s better to use
models that can adapt to evolving volatility environments.
Figure 4. 30-Day Rolling Standard Deviation of Spot Returns
5) Autocorrelation Function:The ACF plot (Figure 5)
demonstrates the Autocorrelation Function (ACF) of daily nat-
ural gas spot returns, supporting a 30-day expanding window
size for the LNN model. The ACF reveals two significant
autocorrelation zones relative to the 95% confidence interval
(±0.038). The first zone, spanning lags 1–8, has the most
negative autocorrelation at lag 3 (ACF=−0.112), indicating
a short-term mean-reversion dynamic in which large price
movements are partially reversed over subsequent trading days.
The second zone has a statistically significant spike at lag
19 (ACF= 0.059) due to the monthly United States Energy
Information Administration (EIA) natural gas storage reports,
a market-moving event every 20 trading days. These findings
led to an expanding window of 30 trading days to capture the
full autocorrelation structure in the model’s input sequence.
Figure 5. Autocorrelation Function of Natural Gas Spot Price Returns
Collectively, exploratory analyses show that the Henry Hub
natural gas price series has strong nonstationarity, volatility
clustering, weak long-horizon linear dependence, and complex
cross-market relationships. Based on these findings, the next
section introduces this study’s forecasting framework and
modeling methods.

IV. METHODOLOGY
A. Baseline Model: Multivariate Rolling-window Linear Re-
gression
As a benchmark, we employ a multivariate rolling-window
linear regression to predict the daily return of the Henry Hub
natural gas spot price. Let the spot price at daytbeP t. The
spot return (target variable) is defined as
Rt = Pt −P t−1 Pt−1 ×100,(1)
so thatR t represents the daily percentage change in the spot
price.
Denote byZ t−1 the vector of exogenous predictors ob-
served at timet−1, including lagged returns and other market
variables (spreads, fundamentals, macro indicators, etc.). The
baseline model at timetis:
Rt =α+β 1Rt−1 +γ ⊤Zt−1 +ε t,(2)
whereαis the intercept,β 1 is the autoregressive coefficient on
the lagged return,γare coefficients on the exogenous features,
andε t is the error term.
To allow for time-varying relationships, the regression is
estimated in a daily rolling window of lengthW= 30. For
each forecast timet≥W, the model uses the most recent
30 observations(t−W, . . . , t−1)as the training set. The
fitted coefficients are then used to generate the one-step-ahead
forecast ˆRt, producing a series of rolling one-day-ahead return
forecasts{ ˆRt}that serve as a linear baseline for comparison
with the LNN models.
B. Neural Forecasting Models
We evaluate five neural architectures: (i)LSTM, (ii)Strict
CfC, (iii)LTC(uniform-step continuous-time), (iv)Hybrid
CfC, and (v)CT-LTC(calendar-gap continuous-time).
All five models share the same input interface. Letx t ∈
Rd denote the standardised feature vector at timet. At each
evaluation timet eval, every model receives theL= 30most
recent observations as a fixed-length input window:
X=

xteval−L+1, . . . ,xteval

∈R L×d, L= 30,(3)
and produces a scalar one-step-ahead return forecast via a
linear readout ˆRteval+1 =w ⊤hL +b. The window lengthL
is fixed; thetraining historyexpands over evaluation times
(Section IV-C).
1) LSTM:As a nonlinear recurrent benchmark, we use a
standard single-layer LSTM. Leth t andc t denote the hidden
and cell states at timet. The recurrence is
ft =σ(W f xt +U f ht−1 +b f ),(4)
it =σ(W ixt +U iht−1 +b i),(5)
ot =σ(W oxt +U oht−1 +b o),(6)
˜ct = tanh(Wcxt +U cht−1 +b c),(7)
ct =f t ⊙c t−1 +i t ⊙ ˜ct,(8)
ht =o t ⊙tanh(c t).(9)
The final hidden state is mapped to a one-step-ahead forecast
by
ˆRt+1 =w ⊤hL +b.(10)
This model provides a discrete-time gated recurrent baseline
without continuous-time dynamics or liquid time constants.
2) Strict CfC:The Strict CfC implements the gated-
interpolation form of the Closed-form Continuous-time Neural
Network [14]. Letu t = [xt;h t−1]denote the concatenation of
the current input and previous hidden state. A shared backbone
MLP, given by one linear layer followed by Tanh, mapsu t to
st = tanh(Wbbut +b bb)∈R m,(11)
wherem= max(2n,32); in our experiments, this givesm=
32for all hidden sizes considered. Three independent heads
then branch froms t. Two Tanh heads define the candidate
trajectory limits,
gt = tanh(Wgst +b g),f t = tanh(Wf st +b f ),(12)
while two linear heads parameterize the sigmoid interpolation
gate,
t(a) t =W ast +b a,t (b) t =W bst +b b,(13)
so that
σt =σ

t(a) t ·∆t+t (b) t

,∆t= 1.(14)
The hidden state is updated by gated interpolation between
these two trajectory limits:
ht =g t ⊙(1−σ t) +σ t ⊙f t.(15)
Thus, the Strict CfC replaces the explicit exponential decay
of the LTC closed-form solution with an input-dependent
sigmoid interpolation gate, while retaining a closed-form re-
current update without numerical ODE integration. Matrix-
valued trainable parameters are initialized with Xavier uniform
initialization.
3) LTC (uniform-step):The LTC model implements a
Liquid Time-Constant network whose hidden state evolves ac-
cording to the continuous-time dynamics of Hasaniet al.[13].
For hidden uniti, the underlying continuous-time dynamics
are
dxi(t)
dt =−
 1
τi
+f i(x(t),I(t), θ)

xi(t)+fi(x(t),I(t), θ)Ai,
(16)
whereτ i >0is a learnable base time constant andA i is a
learnable attractor parameter. In the implementation, the time
constants are parameterized in log-space as
τi = exp(θτ,i),(17)
which guarantees positivity.
Rather than numerically solving the ODE with a generic
solver, each discrete time step is advanced using the fused
semi-implicit Euler update withL ode = 6internal unfolding
steps. Leth (0) =h t−1 and
δt= 1 Lode .(18)

For each sub-stepℓ= 1, . . . , Lode, the nonlinear response is
computed as
f (ℓ) =σ  Wrech(ℓ−1) +W inxt +b  ,(19)
whereW in is an input-to-hidden linear map computed once
per external time step and reused across all sub-steps,W rec is
a recurrent hidden-to-hidden linear map recomputed at each
sub-step, andbis a learnable bias vector. The hidden state is
then updated by
h(ℓ) = h(ℓ−1) +δtf (ℓ) ⊙A 1+δt  1/τ+f (ℓ) ,(20)
and the final hidden state for the external time step is
ht =h (Lode).(21)
4) Hybrid CfC:The Hybrid CfC uses a closed-form re-
current update with input-dependent time-scale modulation. At
each step, the input and previous hidden state are concatenated
as
ut = [xt;h t−1].(22)
A nonlinear drive and adaptive time constant are then com-
puted by
ft = tanh(Wf ut +b f ),(23)
τ t = exp(θτ )⊙σ(W τ ut +b τ ),(24)
with elementwise lower clipping
τ t ←max(τ t,10 −3).(25)
The effective decay and exponential gate are
At = 1 τ t +|f t|,(26)
gt = exp

−max(A t,10 −3)  .(27)
The hidden state update is
ht =g t ⊙h t−1 + (1−g t)⊙ ft At ,(28)
which can be interpreted as exponential relaxation toward the
data-dependent equilibriumf t/At.
5) CT-LTC (calendar∆t):CT-LTC extends the LTC
formulation (Section IV-B3) by replacing the fixed unit step
size with the observed calendar gap between consecutive
timestamps. The underlying ODE, log-space time constant
parameterization, nonlinear response, and fused semi-implicit
Euler update structure are identical to those of LTC. The sole
modification is that the sub-step size is determined by the
elapsed calendar time∆ t between observations at timest−1
andt, measured in days and clipped below at 1:
δtt = ∆t Lode .(29)
The hidden state update at each internal sub-step then follows
Eq. (20) withδtreplaced byδt t. Weekend and holiday gaps
therefore induce larger integration steps than ordinary adjacent
trading days, making CT-LTC sensitive to irregular calendar
spacing in the observed financial series.
C. Workflow and Evaluation Protocol
Phase 0: Data Preparation:The full dataset ofNobser-
vations is partitioned chronologically at the 50% mark into a
tuning set(first⌊N/2⌋rows) and anevaluation set(remaining
rows). All hyperparameter search is conducted exclusively on
the tuning set; the evaluation set is never observed during
tuning.
Feature exclusion is consistent across all models, with one
exception. The non-CT runs exclude {Date, Spot Return, Spot
Price, AR1 Spot Price}, leaving 30 predictor features. The
CT-LTC run additionally excludes the lagged return to avoid
direct target leakage, leaving 29 predictor features.
Phase 1: Hyperparameter Tuning:Within the tuning set,
a time-ordered 80/20 split yields an inner training segment
and an inner validation segment. AStandardScaleris
fitted on the inner training segment only and applied to both;
no validation data influence the scaler. For each candidate
configuration, the model is trained for 30 epochs using the
Adam optimiser with weight decayλ= 10 −5 and gradient
clipping at maxℓ 2-norm= 1.0. Mean squared error (MSE)
is used as the training loss. The configuration achieving the
highest Pearson correlationron the inner validation segment
is selected.
All five neural models share the hyperparameter grid
shown in Table I.
Table I
HYPERPARAMETER GRID SHARED BY ALL FIVE NEURAL MODELS.
Hyperparameter Candidate values
Hidden size{4,8,12}
Learning rate{5×10 −3,10 −3}
Batch size{32,64}
Number of layers{1}
Note:LTC and CT-LTC additionally fixL ode = 6ODE sub-steps (not
searched).
The search space is intentionally compact for two reasons.
First, LNN architectures are parameter-efficient by design:
continuous-time dynamics and input-dependent time constants
encode rich temporal structure with far fewer hidden units than
comparably expressive discrete recurrent networks [13], [14],
making hidden sizes of 4, 8, and 12 sufficient for a daily
financial series of roughly 2,600 observations. Second, the
expanding-window protocol requires retraining from scratch
at each of theN eval = 160evaluation points; the full grid
already exceeds 9,000 individual training runs across all five
architectures, and extending it further would increase cost
superlinearly with diminishing benefit. Fixing the number of
layers at one is consistent with empirical findings showing
that single-layer LTC and CfC cells match or exceed deeper
discrete recurrent stacks on short-horizon regression tasks [13].
Phase 2: Stratified Expanding-Window Evaluation:Out-
of-sample performance is assessed using a deterministic strat-
ified expanding-window scheme. An expanding rather than
rolling window is used because LNNs benefit from growing
training sets; discarding historical data would systematically

disadvantage them relative to the linear baseline. The evalu-
ation indices are divided intoK= 20equal-length temporal
bins withk= 8evenly spaced points drawn from each,
yieldingN eval = 160evaluation points applied identically
across all architectures. At eacht eval, all preceding observa-
tions form the expanding training set; aStandardScaler
is fitted exclusively on this window; the model is retrained
from scratch for 50 epochs under the tuned hyperparameters;
and the one-step-ahead forecast is generated from theL= 30
most recent standardised observations.
Phase 2b: Moving Block Bootstrap:To quantify sampling
uncertainty of out-of-sample metrics, we apply a Moving
Block Bootstrap (MBB) to theN eval stored forecast–truth
pairs{(y i,ˆyi)}Neval i=1 , with all model predictions held fixed.
Each bootstrap replication draws a resample of sizeN eval
by selecting random starting indices (with wrap-around) and
concatenating contiguous blocks of lengthℓ block, then recom-
putes all performance metrics on the resampled pairs. MBB
preserves the temporal autocorrelation of the forecast error
series that i.i.d. resampling would destroy.
The block length is chosen data-adaptively from the ACF
of residualse i =y i −ˆyi:
ℓblock = max

5,min

ˆℓACF + 2,
 Neval
10

,(30)
where ˆℓACF is the last lag at which|ˆρ(ℓ)|>1/ √Neval in
the sample ACF. We useB= 300bootstrap replications and
report the bootstrap mean, standard deviation, and 2.5th–97.5th
percentile interval (95% CI) for each metric.
Training Details:All five neural models share the same
settings: sequence lengthL= 30(fixed lookback window),
30 epochs per tuning trial, 50 epochs per expanding-window
retrain, and silent skipping of batches containing NaN inputs,
predictions, or losses.
Selection Criterion:The primary model selection metric
is the Pearson correlationrbetween predicted and actual
returns on the validation segment. The hyperparameter set
with the highest validation Pearsonris retained as the best
configuration.
V. RESULTS
A. Metrics
To evaluate predictive performance, we employ Pearson’s
correlation coefficient, Spearman’s rank correlation coefficient,
directional accuracy, the coefficient of determination (R2), root
mean squared error (RMSE), and mean absolute error (MAE).
Pearson’s correlation serves as the primary model selection
and evaluation metric for two reasons. Scale-dependent metrics
such asR 2, RMSE, and MAE can become unstable during
structural breaks or volatility spikes, where a single extreme
observation may dominate the aggregate statistic. Directional
accuracy evaluates the fraction of correctly predicted return
signs:
DA= 1 n
nX
i=1
I[sign(yi) =sign(ˆyi)].(31)
Together, Pearson’srcaptures proportional co-movement,
Spearman’sρreflects monotonic structure, and DA measures
practical forecasting value in trading applications where direc-
tional correctness often matters more than exact magnitude.
B. Results and Analysis
1) Extreme Event Behavior and Forecast Deviations:For
all model predictions, visualizations comparing predicted and
actual returns reveal several large and abrupt deviations that
none of the evaluated models adequately capture, reflecting ex-
treme market movements caused by exogenous shocks rather
than typical market dynamics.
One example occurred in February 2021 during Winter
Storm Uri, when extremely cold temperatures increased heat-
ing demand while freezing conditions disrupted production
and infrastructure, particularly in Texas, significantly straining
natural gas and electricity markets. [23] A similar pattern was
observed in early 2022, when prices rose due to high storage
withdrawals, strong LNG exports, and declining production
exacerbated by cold weather. [24] Another fluctuation occurs
in December 2022 during Winter Storm Elliott [25], while the
spike around April 2024 reflects transient market imbalances
such as strong LNG export demand and thin market liquid-
ity. [26] Finally, in November 2024, an abrupt reversal after
exceptionally low prices generates disproportionately large
positive percentage returns as anticipated winter risks triggered
a quick recovery. [27]
These findings highlight a key limitation of data-driven
models: even adaptive architectures cannot anticipate exoge-
nous shocks outside the historical data distribution, suggesting
that incorporating real-time external signals such as weather
forecasts may be required to better capture tail-risk events.
Figure 6. Baseline 30-Day Rolling Regression: Actual vs. Predicted Spot
Returns (First 50% of Timeline)
Figure 7. Baseline 30-Day Rolling Regression: Actual vs. Predicted Spot
Returns (Second 50% of Timeline)
2) Baseline Model: AR(1) Spot Price + All Features:
Using a 30-day rolling window, the baseline model generated

Table II
MODEL PERFORMANCE ON THE TEST SET AND UNDER BOOTSTRAP RESAMPLING.
Panel A: Test-set performance
Model PearsonrSpearmanρDA (%)R 2 RMSE MAE
Baseline−0.0408−0.0122 43.30−91.03 61.12 32.45
LSTM0.1035 0.1714 55.00−0.0133 8.129 5.149
Strict CfC0.1059 0.1593 52.50−0.0528 8.285 5.398
LTC0.2548 0.2262 51.88 0.0540 7.854 5.026
Hybrid CfC0.3011 0.2680 53.75 0.0573 7.840 4.968
CT-LTC0.0972 0.1307 52.50 0.0076 8.044 5.087
Panel B: Bootstrap performance (mean±std, 95% CI[2.5 th,97.5 th],R= 300)
Model PearsonrSpearmanρDA (%)R 2 RMSE MAE
LSTM0.119±0.099 0.164±0.055 55.08±2.67−0.009±0.039 8.014±1.800 5.168±0.740
[−0.058,0.294] [0.063,0.272] [50.63,60.00] [−0.064,0.081] [5.271,11.502] [3.972,6.747]
Strict CfC0.110±0.055 0.150±0.060 52.42±3.35−0.069±0.042 8.207±1.656 5.421±0.753
[0.016,0.227] [0.039,0.283] [46.25,59.38] [−0.164,−0.004] [5.661,11.455] [4.148,7.116]
LTC0.259±0.054 0.222±0.050 51.92±2.20 0.049±0.016 7.761±1.651 5.041±0.714
[0.163,0.368] [0.128,0.314] [47.50,55.63] [0.018,0.080] [5.281,10.972] [3.923,6.620]
Hybrid CfC0.302±0.052 0.263±0.058 53.80±3.86 0.051±0.016 7.750±1.638 4.986±0.708
[0.194,0.398] [0.151,0.365] [45.63,60.00] [0.015,0.084] [5.202,10.950] [3.840,6.545]
CT-LTC0.112±0.100 0.128±0.093 52.58±3.07 0.006±0.019 7.939±1.712 5.103±0.747
[−0.063,0.304] [−0.060,0.304] [45.63,58.13] [−0.026,0.047] [5.252,11.293] [3.937,6.732]
Note:Panel B reports bootstrap mean±standard deviation with the 95% confidence interval (2.5 th–97.5th percentile) on the second line of
each model row. Best value in each Panel B column isbolded.
2,615 one-step-ahead forecasts for daily spot price percentage
changes. Correlation-based metrics indicated no predictive
structure, with Pearson’sr=−0.039and Spearman’sρ=
−0.012, and directional accuracy of 43.33% failed to outper-
form a random 50% benchmark. Error metrics were substantial
(RMSE: 61.12; MAE: 32.45). TheR 2 of−91.03indicates that
the baseline model’s forecasts explain far less variance than
a naive mean predictor; while such extreme negative values
may appear unusual, they are a common outcome when a
linear model with many parameters is applied to heavy-tailed,
regime-switching return series where the conditional mean is
highly unstable, causing the sum of squared forecast errors
to greatly exceed the total variance of the target. This result
confirms the fundamental limitations of linear models in this
forecasting setting.
3) LSTM:As reported in Table II, the LSTM achieves
the highest directional accuracy among the non-hybrid ar-
chitectures, yet itsR 2 remains near zero and its correlation
coefficients are the weakest in the neural model tier. This
dissociation reflects a structural limitation of the discrete
gating mechanism: the forget, input, and output gates regulate
information flow through fixed sigmoid activations that are
insensitive to both the elapsed time between observations and
the magnitude of the current input shock. Consequently, while
the model can associate input configurations with a return di-
rection, it cannot modulate the rate at which stale hidden-state
information is discarded in response to abrupt market events.
In a series characterised by sudden regime shifts, volatility
clustering, and heavy-tailed spikes, this rigidity causes the
hidden state to retain outdated information and smooth through
the dynamics that drive magnitude variation.
Bootstrap resampling confirms that this weakness is a
systematic property of the architecture rather than an artefact
of the evaluation window. The confidence intervals for both
PearsonrandR 2 straddle zero, indicating that co-movement
with realised returns and explanatory power relative to a naive
mean predictor are both unreliable across different market
regimes. The LSTM therefore serves as a useful nonlinear
recurrent benchmark but is ill-suited to the adaptive demands
of volatile commodity forecasting.
Figure 8. LSTM model: actual vs. predicted spot returns.
4) Strict CfC:As shown in Table II, the Strict CfC fails to
outperform the LSTM in any metric of practical significance.
Despite its continuous-time motivation, the architecture’s sig-
moid interpolation gate controls only the mixture ratio between
two candidate trajectory limits, not the rate at which the hidden
state transitions between them. A large return shock can shift

the blend toward a new candidate state, but the transition car-
ries no explicit timescale dependence, leaving the model with
an inertia that is unsuitable for a series in which consecutive
observations can differ by an order of magnitude. TheR 2
bootstrap distribution demonstrates structural rigidity, with a
confidence interval below 0. Sample mean return forecasts
explain more than strict CfC forecasts across all resampled
evaluation windows. Architectures that capture continuous-
time dynamics are especially affected. The model’s limited
positive co-movement in point-estimate evaluation may be due
to favorable sampling, not a strong learned signal, as both
correlation coefficients have wide confidence intervals. As the
weakest neural architecture, strict CfC shows that the closed-
form continuous-time formulation without input-conditioned
timescale modulation does not outperform a standard recurrent
benchmark in this forecasting scenario.
Figure 9. Strict CfC model: actual vs. predicted spot returns.
5) LTC:The LTC model greatly outperforms the LSTM
and Strict CfC, as shown in Table II. Pearson and Spearman
correlations are nearly double those of weaker architectures,
with positiveR 2 and low error metrics in the neural tier.
Significantly, these improvements focus on magnitude-related
metrics, while directional accuracy remains modest. The LTC
architecture’s continuous-time ODE formulation, governed by
learnable time constants and attractor parameters, enables the
model to track return path levels and shapes more accurately
than discrete recurrent networks. The LTC solves hidden-state
dynamics with multiple internal sub-steps per observation,
allowing for finer temporal resolution than the observed daily
frequency. This allows for smooth drift components to be
captured, even with noisy surface-level returns.
Figure 10. Liquid Time-Constant (LTC) model: actual vs. predicted spot
returns.
The Boostrap results show that the PearsonrandR 2
confidence intervals are strictly positive across the bootstrap
distribution. This property is only shared by Hybrid CfC
among all evaluated models. The advantage of LTC over a
naive predictor is not due to a favorable evaluation window,
but rather to a reliable and consistent learned signal. The LTC’s
uniform sub-step size∆t= 1/L ode, which remains constant
regardless of input dynamics, is an important architectural
constraint. As shown in Figure 5, the model’s ability to
represent both short-horizon mean-reversion dynamics and
longer-horizon trend components is limited by the fact that
all hidden units integrate at the same frequency. The Hybrid
CfC addresses this constraint, explaining why, despite its high
performance, LTC is consistently outperformed by its hybrid
counterpart.
6) Hybrid CfC:The Hybrid CfC is the best overall
performer across all metrics in both the point-estimate and
bootstrap panels, as shown in Table II. Its superiority over the
LTC — the second-strongest model — is narrow in absolute
terms but consistent across all resampled evaluation windows,
which is the more important criterion for assessing genuine
architectural advantage. The mechanism underlying this edge
lies in the adaptive decay rateA t = 1 τt +|f t|(Eq. 26), which couples a learned base time constant with the instantaneous
magnitude of the driving signal. This single modification has
a profound consequence for how the model responds to market
shocks: when a large return is observed,|f t|increases, directly
raising the effective decay rate and causing the hidden state
to shed stale information more rapidly. Conversely, during
quiet periods, the decay rate falls toward the baseline1/τ t,
allowing the model to integrate information over a longer
effective horizon. This dynamic adjustment is precisely what
is required for a series with the empirical properties of Henry
Hub returns — abrupt, heavy-tailed shocks that demand rapid
state updating, interspersed with calmer regimes where longer
memory improves forecast stability.
Figure 11. Hybrid CfC model: actual vs. predicted spot returns.
The bootstrapR 2 confidence interval lying entirely above
zero provides the strongest statistical evidence that the Hybrid
CfC’s advantage is systematic rather than sample-specific. The
partial overlap between itsR 2 interval and that of LTC sug-
gests the two architectures occupy a statistically close superior
tier, well separated from the LSTM, Strict CfC, and CT-LTC.
The relatively wide directional accuracy interval, however,
indicates that sign prediction remains noisy — the model’s pri-
mary contribution is to return-level fidelity rather than binary

directional classification. Taken together, the results suggest
that input-conditioned timescale modulation is the single most
important architectural feature for this forecasting task, and
that the Hybrid CfC’s implementation of this property via a
fully closed-form update represents the most effective balance
between temporal adaptability and computational tractability
among the architectures considered.
7) CT-LTC:The CT-LTC model extends the LTC formu-
lation by replacing the fixed unit step size with the observed
calendar gap between consecutive timestamps, encoding week-
end and holiday spacing directly into the integration dynamics.
Despite the theoretical appeal of this modification — financial
time series are inherently irregularly spaced, and Monday
returns aggregate three calendar days of information — the
empirical results in Table II reveal that calendar-aware step siz-
ing does not translate into improved forecasting performance
relative to the uniform-step LTC. This counterintuitive finding
warrants careful interpretation.
Figure 12. CT-LTC model: actual vs. predicted spot returns.
The fundamental limitation of CT-LTC is that a single
calendar-derived∆tis applied uniformly across all hidden
units, forcing every unit to integrate at the same rate re-
gardless of the informational content of the current input.
Calendar distance is a poor proxy for informational distance
in a market driven by discontinuous, event-specific shocks:
a Monday following a quiet weekend and one following a
major supply disruption carry very different information loads,
yet receive identical step sizes. The Hybrid CfC avoids this
by conditioning its effective timescale on|f t|, tracking signal
magnitude rather than elapsed time.
Bootstrap confidence intervals for both Pearsonrand
R2 straddle zero, confirming that CT-LTC’s marginal point-
estimate gains are not reproducible across evaluation win-
dows. The architecture is a principled extension of LTC, but
its calendar-gap parameterisation imposes temporal rigidity
incompatible with the shock-driven dynamics of the Henry
Hub market. Replacing uniform calendar spacing with input-
conditioned∆tscaling represents a natural direction for future
work.
8) Forecast Bias:To assess whether the evaluated models
produce systematically biased forecasts, we compute the mean
forecast error for each architecture and test its significance
using a two-sidedt-test. A significantly nonzero mean error
would indicate that a model consistently over- or under-
predicts spot returns.
None of the five neural architectures exhibits statistically
significant forecast bias at the 5% level. The LSTM produces
a mean error of−0.250(t=−0.388,p= 0.699), indicating
a slight but insignificant tendency to over-predict returns. The
Strict CfC is the least biased model in absolute terms, with
a mean error of+0.047(t= 0.072,p= 0.943). The LTC
and Hybrid CfC show modest negative mean errors of−0.213
(t=−0.343,p= 0.732) and−0.113(t=−0.182,p=
0.856), respectively. The CT-LTC exhibits the largest absolute
bias at−0.336(t=−0.527,p= 0.599), consistent with its
tendency to under-react to positive return episodes, though this
bias remains statistically insignificant.
VI. DISCUSSION
A. Conclusion
Forecasting natural gas spot returns remains inherently
challenging due to the market’s pronounced nonlinearity,
heavy-tailed distributions, and frequent regime shifts. The
Henry Hub series exhibits not only high volatility but also
abrupt structural changes that violate the assumptions under-
lying many traditional time-series models. As a result, both
linear methods and standard recurrent neural architectures
often struggle to capture the true dynamics of the data-
generating process.
This study compares a variety of Liquid Neural Net-
work (LNN) architectures—including LTC, Strict Closed-form
Continuous-time (CfC), Hybrid CfC, and CT-LTC—with a
multivariate rolling-window linear regression baseline and a
standard LSTM benchmark. The empirical results demonstrate
that LNN-based models consistently outperform the baseline
and offer meaningful advantages over traditional recurrent ap-
proaches, confirming that architectures with adaptive temporal
dynamics are better suited to the nonlinear and nonstationary
behavior observed in energy markets.
Among the evaluated models, the Hybrid CfC and LTC
architectures emerge as the most effective. Both achieve higher
out-of-sampleR 2 values, stronger linear and rank correlations
with realized returns, and lower forecast errors relative to com-
petitors. Their advantage stems not merely from a continuous-
time formulation but from the ability to balance temporal
adaptability with nonlinear flexibility. The Hybrid CfC, in
particular, delivers the most consistent overall performance
by combining continuous-time inductive bias with input-
conditioned gating mechanisms that enhance stability and
predictive accuracy. In contrast, the CT-LTC variant, despite its
theoretical appeal of calendar-aware temporal dynamics, does
not yield significant gains; its uniform application of calendar-
derived step sizes appears to oversmooth the discontinuous,
jump-driven returns characteristic of natural gas markets. The
standard LSTM achieves competitive directional accuracy but
lacks meaningful explanatory power, as indicated by near-
zero or negativeR 2 values. This distinction underscores a key
finding: architectures that predict return direction effectively
do not necessarily capture the magnitude and structure of
return dynamics.

Overall, this study demonstrates that liquid neural archi-
tectures, particularly Hybrid CfC and LTC, provide a reliable
framework for short-term forecasting in volatile commodity
markets. Improved predictive accuracy in this setting can
support operational decisions for utilities, pipeline operators,
and energy producers, inform trading strategies, and strengthen
risk management during periods of elevated volatility. More
broadly, the results confirm that integrating adaptive temporal
mechanisms into neural architectures offers a principled ap-
proach to modeling complex financial time series, especially
when the assumptions of smooth evolution and stationarity are
violated.
B. Future Work
The most consequential limitation of the current frame-
work is the absence of physical market fundamentals. The fea-
ture set relies on financial and equity market proxies, whereas
natural gas prices are ultimately determined by physical supply
and demand dynamics. EIA weekly storage reports, pipeline
flows, LNG export volumes, and rig activity are among the
main price forming drivers in the US natural gas market,
and their exclusion limits the models’ ability to anticipate
structurally driven price movements. Incorporating these vari-
ables alongside temperature driven consumption data, which
captures the strong seasonal and regime dependent demand
patterns that financial proxies cannot represent, is the highest
priority extension for improving signal quality.
Beyond the feature set, the evaluation framework has two
notable gaps. First, the restriction to one-step-ahead forecasts,
while appropriate for controlled architectural comparison, does
not address the multi-day horizons most relevant to practical
applications such as hedging and procurement. Whether the
advantage of Hybrid CfC and LTC persists under multi-step
forecasting, or erodes as forecast uncertainty accumulates,
remains an open question. Second, the absence of classical
time-series benchmarks such as ARIMA and GARCH makes it
difficult to attribute performance gains specifically to nonlinear
learning or continuous-time dynamics, rather than to the adap-
tive re-estimation that any rolling-window method provides.
Taken together, these gaps suggest that enriching the
information set and broadening the evaluation framework
offer greater marginal returns than further increasing model
complexity. The strong performance of Hybrid CfC and LTC
indicates that adaptive temporal dynamics can already extract
meaningful structure from the available data; the priority for
future work is therefore to supply those dynamics with richer,
more price-relevant inputs and to validate their advantages
across a wider range of forecasting conditions.
REFERENCE
[1] A. Safari, N. Das, O. Langhelle, J. Roy, and M. Assadi, “Natural gas:
A transition fuel for sustainable energy system transformation?”Energy
Science & Engineering, vol. 7, no. 4, pp. 1075–1094, 2019.
[2] A. E. H. Mazighi, “Henry hub and national balancing point prices: What
will be the international gas price reference?”OPEC Review, vol. 29,
no. 3, pp. 219–230, 2005.
[3] A. Hailemariam and R. Smyth, “What drives volatility in natural gas
prices?”Energy Economics, vol. 80, pp. 731–742, 2019.
[4] A. Aslan, “Does natural gas consumption follow a nonlinear path over
time? evidence from 50 U.S. states,”Renewable and Sustainable Energy
Reviews, vol. 15, no. 9, pp. 4466–4472, 2011.
[5] F. Ilhan, O. Karaahmetoglu, I. Balaban, and S. S. Kozat, “Markovian rnn:
An adaptive time series prediction network with hmm-based switching
for nonstationary environments,”arXiv preprint arXiv:2006.10119,
2020. [Online]. Available: https://arxiv.org/abs/2006.10119
[6] W. Dbouk, “Predicting daily oil prices: Linear and non-linear models,”
inProceedings of the 2018 EFMA Annual Meetings, Milan, Italy, 2018,
eFMA Paper No. 0192, European Financial Management Association
Annual Meeting.
[7] M. Artemova, F. Blasques, S. J. Koopman, and Z. Zhang, “On
the use of flexible rolling-window estimation and forecasting with
evidence from the Great Recession to the COVID-19 pandemic,”
Working paper, Tinbergen Institute and Vrije Universiteit Amsterdam,
2025. [Online]. Available: https://www.tse-fr.eu/sites/default/files/TSE/
documents/sem2025/eee/artemova.pdf
[8] I. A. Khan, A. Akbar, and Y . Xu, “Sliding window regression
based short-term load forecasting of a multi-area power system,”
arXiv preprint arXiv:1905.08111, 2019. [Online]. Available: https:
//arxiv.org/abs/1905.08111
[9] S. Das, B. Khan, and X.-Y . Liu, “A hybrid PCA-PR-Seq2Seq-Adam-
LSTM framework for time-series power outage prediction,”arXiv
preprint arXiv:2509.16743, 2025.
[10] F. Ilhanet al., “Gasoline and crude oil price prediction using multi-
headed variational neighbour search-tuned recurrent neural networks,”
Computational Economics, 2025.
[11] X. Liu, M. Tang, Y . Feng, T. Fang, Z. Wang, and M. Song, “Natural
gas price prediction based on artificial intelligence models,”PLOS ONE,
vol. 20, no. 12, p. e0336582, 2025.
[12] H. Zaragoza, A. B. Granados, J. M. Peña-González, G. B. Giannakis,
and C. G. Brinton, “Time-varying graph learning for electricity price
forecasting,” in2024 IEEE International Conference on Acoustics,
Speech and Signal Processing (ICASSP), 2024, pp. 1–5.
[13] R. Hasani, M. Lechner, A. Amini, D. Rus, and R. Grosu, “Liquid time-
constant networks,” inProceedings of the Thirty-Fifth AAAI Conference
on Artificial Intelligence (AAAI-21), vol. 35, no. 9. AAAI Press, 2021,
pp. 7657–7666.
[14] R. Hasani, M. Lechner, A. Aminiet al., “Closed-form continuous-time
neural networks,”Nature Machine Intelligence, vol. 4, pp. 992–1003,
2022.
[15] U.S. Energy Information Administration, “Natural gas spot price (henry
hub),” https://www.eia.gov/opendata/browser/natural-gas/pri/fut.
[16] U.S. Energy Information Administration, “Cushing, ok WTI spot price
FOB,” https://www.eia.gov/dnav/pet/hist/RWTCD.htm.
[17] U.S. Department of the Treasury, “Daily treasury par yield curve
rates,” https://home.treasury.gov/resource-center/data-chart-center/
interest-rates/TextView.
[18] Investing.com, “U.s. dollar index historical data,” https://www.investing.
com/indices/usdollar-historical-data.
[19] Investing.com, “S&P 500 energy historical data,” https://www.investing.
com/indices/s-p-500-energy-historical-data.
[20] Investing.com, “Dow jones u.s. coal total stock market
historical data,” https://www.investing.com/indices/dow-jones-u.s.
-coal-total-stock-mar-historical-data.
[21] Investing.com, “EQT corporation historical data,” https://www.investing.
com/equities/eqt-corporation-historical-data.
[22] U.S. Energy Information Administration, “U.s. nuclear outages,” https:
//www.eia.gov/nuclear/outages/.
[23] U.S. Energy Information Administration, “Winter storm uri caused
widespread disruptions to u.s. energy supply and demand,” https://www.
eia.gov/todayinenergy/detail.php?id=50778, 2021.
[24] U.S. Energy Information Administration, “U.s. natural gas prices in-
creased amid strong demand and lower production,” https://www.eia.
gov/todayinenergy/detail.php?id=55119, 2022.
[25] U.S. Energy Information Administration, “Winter storm elliott disrupts
u.s. energy markets and drives price volatility,” https://www.eia.gov/
todayinenergy/detail.php?id=55139, 2022.
[26] U.S. Energy Information Administration, “U.s. natural gas market
dynamics and lng export activity in 2024,” https://www.eia.gov/
todayinenergy/detail.php?id=61563, 2024.
[27] U.S. Energy Information Administration, “U.s. natural gas storage
levels remain elevated entering winter 2024–2025,” https://www.eia.gov/
todayinenergy/detail.php?id=64004, 2024.
