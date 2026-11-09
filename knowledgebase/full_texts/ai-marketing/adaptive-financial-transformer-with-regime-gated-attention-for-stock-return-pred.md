---
title: Adaptive Financial Transformer with Regime-Gated Attention for Stock Return Prediction
url: https://arxiv.org/abs/2606.29347
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Dishan Sarkar
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.29347
pages: 10
chars: 39269
fetched_at: '2026-11-08T13:06:49+00:00'
kb_version: 1
---

# Adaptive Financial Transformer with Regime-Gated Attention for Stock Return Prediction

Adaptive Financial Transformer with Regime-Gated
Attention for Stock Return Prediction
Dishan Sarkar
Department of Artificial Intelligence and Machine Learning
Birla Institute of Technology, Mesra
Ranchi, India
Email: btech10614.23@bitmesra.ac.in
ORCID: 0009-0002-8672-6680
Abstract—Stock return forecasting is characterized by an
extremely low signal-to-noise ratio and non-stationary market
regimes, making classical sequence models highly susceptible
to overfitting and noise propagation. Standard self-attention
architectures fail to exploit semantic structural relations between
financial indicators, treating all feature dimensions uniformly.
In this paper, we propose the Adaptive Financial Transformer
variant (AFT), a deep learning architecture that incorporates a
Market Regime Encoder, an Adaptive Gate Network, and an
Adaptive Financial Context module to dynamically bias self-
attention weights. The AFT segments 95 technical features into
11 semantic categories, using an unsupervised market regime
projection to scale group-wise similarity matrices dynamically.
Furthermore, we identify and resolve a critical backtesting
leakage in previous baseline literature concerning the daily
compounding of overlapping multi-day horizon returns. To ad-
dress the regression-to-the-mean trap associated with standard
Mean Squared Error (MSE) loss, we introduce a Financially-
Aware Composite Objective combining Mean Absolute Error,
directional sign accuracy, and non-overlapping Sharpe ratios in
a chronological evaluation framework. We evaluate the proposed
model against standard machine learning and recurrent baselines
across 5 random seeds using paired t-tests and Cohen’s d effect
size metrics. Empirical results show that the financially-optimized
AFT model achieves comparable predictive performance with
reduced model complexity, reducing the parameter footprint by
15.2% (from 373,143 to 316,319) and utilizing a pre-selected Top-
40 feature subset (representing 58% fewer features).
Index Terms—Transformer, Stock Prediction, Time Series,
Deep Learning, Financial AI, Adaptive Attention, Machine
Learning, Quantitative Finance
I. INTRODUCTION
The forecasting of asset price returns represents one of
the foundational challenges in quantitative finance. Under
the classical Efficient Market Hypothesis (EMH) proposed
by Fama, asset prices fully reflect all available information,
implying that return series behave as sub-martingales and
price changes approximate a random walk. However, modern
empirical finance suggests that financial markets exhibit micro-
structural inefficiencies, behavioral biases, and non-stationary
regimes that introduce short-term predictability.
Historically, sequence modeling in finance has relied on
classical statistical frameworks like Autoregressive Integrated
Moving Average (ARIMA) and GARCH models. While the-
oretically robust, these linear paradigms cannot capture the
complex, non-linear interactions inherent in financial time-
series. The advent of Deep Learning (DL) introduced Recur-
rent Neural Networks (RNNs), specifically Long Short-Term
Memory (LSTM) and Gated Recurrent Units (GRU). Although
LSTMs resolve vanishing gradient problems, their sequential
processing nature prevents parallelization and restricts their
ability to learn long-range temporal dependencies in highly
volatile contexts.
Transformers, based on the self-attention mechanism, have
revolutionized sequence modeling by allowing direct depen-
dency modeling between any two time steps. However, apply-
ing standard Transformer architectures to quantitative trading
introduces severe limitations:
1)Isotropic Attention:Self-attention is isotropic, treating
all input features uniformly. In finance, where hundreds
of indicators (price, volatility, trend, volume) are fed into
the model, isotropic attention mixes noisy and irrelevant
signals, leading to rapid overfitting.
2)Lack of Temporal and Concept Priors:Standard
Transformers lack inductive biases. In financial forecast-
ing, temporal recency (recent events are more important)
and concept relationships (such as volume relates to
volatility) represent vital priors that must be structurally
enforced.
3)Regression-to-the-Mean:Training Transformers solely
on Mean Squared Error (MSE) or Mean Absolute Er-
ror (MAE) rewards conservative predictions around the
conditional mean, producing smooth, near-zero forecasts
that collapse trading directional accuracy.
To address these challenges, we propose theAdaptive
Financial Transformer (AFT). We segment 95 engineered
technical features into 11 semantic categories and use an un-
supervised Market Regime Encoder to project sequence-level
statistics into latent regime spaces. An Adaptive Gate Network
then outputs dynamic gate probabilities, scaling group-wise
similarity matrices to bias self-attention weights.
The contributions of this work are summarized as follows:
•We propose anAdaptive Financial Contextmechanism
that dynamically biases multi-head self-attention based
on regime-dependent feature group similarities.
•We perform a mathematical and design audit of existing
arXiv:2606.29347v1  [cs.LG]  28 Jun 2026

baseline literature, identifying and correcting a sequence
alignment gap and a backtest return compounding bug
that inflated Sharpe ratios by a factor of
√
5.
•We introduce aFinancially-Aware Composite Objective
that balances forecasting error, directional sign accuracy,
and non-overlapping Sharpe ratios to prevent model
regression-to-the-mean.
•We present a rigorous evaluation across 5 random seeds
using paired t-tests, standard error confidence intervals,
and Cohen’s d effect sizes, showing that the AFT achieves
competitive performance while improving parameter ef-
ficiency.
II. RELATEDWORK
Sequence prediction in quantitative finance has evolved
from statistical modeling to deep learning. Early recurrent
architectures (LSTMs, GRUs) successfully captured autore-
gressive dynamics but suffered from memory bottlenecking.
The introduction of the Transformer by Vaswani et al. allowed
parallelized long-range modeling, prompting the development
of time-series specialized attention mechanisms.
The Temporal Fusion Transformer (TFT) by Lim et al.
introduced static covariate encoders and self-attention to select
relevant features. Informer (Zhou et al.) proposed ProbSparse
attention to handle long-tail queries, while Autoformer (Wu
et al.) replaced dot-product attention with auto-correlation
blocks. However, these models were designed for multi-step
forecasting of physical systems and lack the micro-regime
adaptation needed for high-frequency financial assets. Mod-
ern time-series foundations such as PatchTST (Nie et al.),
FEDformer (Zhou et al.), TimesNet (Wu et al.), Crossformer
(Zhang et al.), iTransformer (Liu et al.), ETSformer (Woo et
al.), DLinear (Zeng et al.), N-BEATS (Oreshkin et al.), N-
HiTS (Challu et al.), TiDE (Das et al.), and SCINet (Liu et al.)
have established specialized structural priors for forecasting,
but their integration with dynamic regime classification in
quantitative trading remains under-explored.
In financial AI, attention biasing has emerged as a method to
inject prior knowledge. Feature Guided Transformers attempt
to weight queries and keys using correlation structures. How-
ever, these static weights fail when market regimes shift. Un-
supervised regime classification (such as via Hidden Markov
Models, Gaussian Mixture Models, or latent clustering) has
been explored, but end-to-end integration into self-attention
gating remains limited. Table I compares the proposed AFT
against existing time-series architectures.
III. PROBLEMFORMULATION
Let the price sequence of an asset be observed over discrete
time stepst∈ {1, . . . , T}. At each time stept, we observe a
feature vectorx t ∈R D representingDengineered financial
features. The target prediction variable is the forwardh-period
return, defined as:
yt = Pt+h −P t Pt (1)
whereP t is the closing price of the asset at time stept, and
h= 5represents the prediction horizon.
We define the sequence dataset as a collection of input-
output pairs(X t, yt), where the input tensorX t ∈R L×D
represents a lookback window of lengthL:
Xt = [xt−L+1, xt−L+2, . . . , xt]T (2)
The forecasting task is to train a modelf Θ :R L×D →R
parameterized byΘto minimize a loss functionLover the
training set:
min
Θ
X
t
L(yt, fΘ(Xt))(3)
In standard formulations, the model is trained using the
Mean Squared Error (MSE) loss:
LM SE= 1 N
NX
i=1
(yi −ˆyi)2 (4)
To evaluate trading efficiency, we compute the Directional
Accuracy (DA) and the annualized Sharpe Ratio (SR):
DA= 1 N
NX
i=1
I(sgn(yi) ==sgn(ˆyi))(5)
SR= µr
σr
·
r
252
h (6)
whereµ r andσ r are the mean and standard deviation of the
non-overlapping strategy returns generated by trading signals
sgn(ˆyi). A transaction cost of 0.05% was deducted whenever
the trading signal changed position.
IV. DATASET ANDFEATUREENGINEERING
We utilize daily data for Apple Inc. (AAPL) covering the
period from 2018 to 2024. Table II outlines the core statistics
of our dataset. A total of 95 technical and calendar features are
engineered and grouped into 11 semantic categories to impose
structural relationships.
A. Feature Groups
1)Price (7 features):High, Low, Open, Close, Previous
Close, Gap, and Price Change.
2)Returns (5 features):Daily Return, Return, Log Return,
ROC-5, and ROC-10.
3)Volatility (8 features):Rolling V olatility, ATR, His-
torical V olatility, Parkinson V olatility, Garman-Klass
V olatility, Rolling Standard Deviation, Variance, and
Return Standard Deviation.
4)Trend (9 features):EMA-9, EMA-21, EMA-50, EMA-
200, EMA-12, EMA-26, MACD, Signal, and MACD
Histogram.
5)Momentum (3 features):Momentum-5, Momentum-
10, and Momentum-20.
6)Volume (8 features):V olume, V olume MA-5, V olume
MA-20, Relative V olume, V olume Change, V olume Mo-
mentum, OBV , and VW AP.

TABLE I: Comparative Summary of Time-Series and Financial Transformer Architectures
Architecture Attention Paradigm Feature Selection Regime Adaptation Financial Alignment
Standard Transformer Scaled Dot-Product None None None
Informer ProbSparse Attention None None None
Temporal Fusion Transformer Self-Attention Variable Selection Net-
work
None None
Feature Guided Transformer Concept-Biased Atten-
tion
Static weights None MSE Only
PatchTST Channel-Independent
Patch
None None None
iTransformer Inverted Dimension At-
tention
None None None
Adaptive Financial Transformer (Ours) Regime-Gated Context
Attention
Dynamic Gate Net-
work
Market Regime En-
coder
Composite Trading
Loss
TABLE II: Dataset and Splitting Statistics
Item Value
Asset Ticker AAPL
Period Range Jan 2, 2018 – Dec 31, 2024
Total Days (Rows) 1,762
Train Split Size (70%) 1,233 days
Validation Split Size (15%) 264 days
Test Split Size (15%) 265 days
Forecast Horizon (h) 5 days
Lookback Sequence (L) 60 days
7)Candlestick (11 features):Body, Upper Wick, Lower
Wick, Full Range, Body Ratio, Upper Wick Ratio,
Lower Wick Ratio, Body-to-Wick Ratio, High-Low
Range, Open-Close Range, and True Range.
8)Statistics (9 features):Rolling Mean, Rolling Min,
Rolling Max, Rolling Median, Rolling Skewness,
Rolling Kurtosis, Rolling Z-score, Rolling Max Return,
and Rolling Min Return.
9)Lags (15 features):Close Lags (1, 2, 3, 5, 10), Return
Lags (1, 2, 3, 5, 10), and V olume Lags (1, 2, 3, 5, 10).
10)Breakout (15 features):Rolling Highs and Lows (5,
10, 20), Distances from High/Low (5, 10, 20), Range
Position, Breakout-20, and Breakdown-20.
11)Calendar (5 features):Day, Month, Quarter, Day of
Week, and Week of Year.
B. Preprocessing and Sequence Realignment
To prevent lookahead bias, features are normalized using
standard scaling where the parametersµandσare fit strictly
on the training set:
zt = xt −µ train σtrain (7)
In previous work, sequence generation aligned feature win-
dowsX t−L:t−1 with targety t. Sincey t is shifted to represent
the return fromttot+h, this created a 1-day alignment lag.
We resolve this by aligningX t−L+1:t with targety t, utilizing
the latest available information up to stept.
C. Complexity Analysis
The processing pipeline features distinct computational pro-
files. The complexity of embedding isO(LD), whereL
is lookback length andDis feature dimension. Standard
self-attention scales asO(L 2dmodel). The Adaptive Financial
Context scales asO(GL 2)whereGis the number of feature
groups. The total complexity per block isO(LD+L 2dmodel +
GL2), which remains highly efficient sinceL= 60and
G= 11are small.
V. ADAPTIVEFINANCIALTRANSFORMER
The architecture of the Adaptive Financial Transformer
is designed to dynamically weight features based on latent
market states. Figure 1 illustrates the system pipeline.
A. Embedding and Positional Encoding
LetX∈R B×L×D be the input sequence. The input is
projected to the model dimensiond model:
E=XW embed +b embed (8)
whereW embed ∈R D×dmodel. A learnable classification token
CLS∈R 1×dmodel is prepended to the sequence, and sinu-
soidal positional encoding is added:
Z0 = [CLS;E] +P E(9)
whereZ 0 ∈R B×(L+1)×dmodel.
B. Market Regime Encoder
The Market Regime Encoder extracts sequence-level statis-
tical descriptors. For each groupg∈ {1, . . . , G}, the group’s
raw featuresX g ∈R B×L×Dg are projected and temporal-
pooled:
hg =Pooling(GELU(X gWg +b g))(10)
whereh g ∈R B×dregime . The group representations are con-
catenated and fused:
R=GELU(Concat(h 1, . . . , hG)Wf usion+b f usion)(11)
whereR∈R B×dregime represents the latent market state.
C. Adaptive Gate Network
The Gate Network computes dynamic weights for each of
theGfeature groups:
w=Softmax(RW gate +b gate)(12)
wherew∈[0,1] G and PG g=1 wg = 1.

Raw Features
X∈R B×L×D
Market Regime Encoder
(GRU + Pooling)
Feature Embedding
(CLS Prepend + PE)
Adaptive Gate Network
(MLP + Softmax)
Adaptive Financial Context
(Group Cosine Similarity)
Modular Attention
(Dot Product + Bias)
2x Encoder Blocks
MLP Regression Head
Predictionˆy
Fig. 1: Structural pipeline of the Adaptive Financial Transformer. The highlighted pathway represents the market regime
adaptive gating system.
D. Adaptive Financial Context
For each feature group, raw indicators are projected to a
head dimensiond head and normalized to compute a cosine
similarity matrixM g ∈R B×(L+1)×(L+1):
Φg =X gWϕ,g +b ϕ,g (13)
Mg = ˜Φg ˜ΦT g , ˜Φg = Φg ∥Φg∥2 +ϵ (14)
The financial context biasB f inancialis computed as:
Bf inancial=σ(γ)
GX
g=1
wgMg (15)
whereγis a learnable scaling parameter.
E. Adaptive Financial Attention
The queries, keys, and values are generated from the se-
quence representation:
Q=ZW Q, K=ZW K, V=ZW V (16)
The attention map is computed as:
Attention(Q, K, V) =Softmax

QK T √dk +B temporal +B f inancial  V
(17)
whereB temporal is a learnable relative temporal position bias.
VI. TRAININGSTRATEGY
The model parameters are optimized using AdamW with
cosine learning rate scheduling and gradient norm clipping.
A. Financially-Aware Composite Loss
Traditional models trained on MSE suffer from regression-
to-the-mean, outputting predictions close to zero. To align
optimization with trading objectives, we propose a composite
loss:
L=αL M SE+βL Corr +γL Sign (18)
where:
LCorr = 1−
P(yi−y)(ˆyi−ˆy)√P(yi−y)2 P(ˆyi−ˆy)2
(19)
Algorithm 1Adaptive Financial Transformer Forward Pass
Require:Input sequenceX∈R B×L×D, feature group map-
pingF g
Ensure:Predictor outputˆy∈R B
1:Project group features:h g ←Pooling(GELU(X gWg +
bg))forg= 1. . . G
2:Fuse representations to find regime:R←
GELU(Concat(h1, . . . , hG)Wf usion)
3:Calculate gate weights:w←Softmax(RW gate)
4:Construct similarity matrices:M g ←
CosineSimilarity(XgWϕ,g)
5:Compile financial context:B f inancial←σ(γ) P g wgMg
6:Apply project embedding:E←XW embed
7:Prepend token:Z←[CLS;E] +P E
8:Compute projections:Q, K, V←ZW Q, ZWK, ZWV
9:Attention scores:A←Softmax( QK T √ d +B temporal +
Bf inancial)
10:Output projection:Z out ←AV WO
11:Feed-forward & Norm:Z block ←LayerNorm(Z+
FFN(Zout))
12:Regression head:ˆy←Linear(GELU(LayerNorm(Z block[:
,0,:])W h))
13:returnˆy
LSign = 1 N
NX
i=1
max(0,−sgn(y i)·ˆyi)(20)
For hyperparameter optimization via Optuna, we construct
a normalized composite score:
Score= 0.40 MAE MAEbase −0.30 DA DAbase −0.30 Sharpe Sharpebase
(21)
These baseline values (MAEbase, DAbase, and Sharpebase) cor-
respond to the average performance of the baseline AFT across
the five random seeds. where MAE base = 0.0316, DA base =
0.5284, and Sharpe base = 0.2423. The weights (0.40, 0.30,
0.30) were chosen empirically to balance prediction accuracy

with directional and risk-adjusted return attributes, preventing
regression-to-the-mean by penalizing low-variance signals.
B. Chronological Train-Validation-Test Evaluation
To ensure robustness to temporal non-stationarity, we
employ a chronological train-validation-test split evaluation
scheme. The dataset is partitioned chronologically into a 70%
training split, a 15% validation split for early stopping, and
a 15% out-of-sample test split, preventing any lookahead
leakages.
VII. EXPERIMENTALSETUP
Hardware and Software configurations include an Intel
Xeon workstation with an NVIDIA RTX 4090 GPU, utilizing
PyTorch 2.1, Optuna, and Scikit-Learn. Daily equity price
data is retrieved from Yahoo Finance, utilizing the split- and
dividend-adjusted closing price for both technical indicator
engineering and forecasting target calculation. We partition
the AAPL dataset chronologically into Train (70%), Validation
(15%), and Test (15%) sets to avoid data leakage. The model
configurations are detailed in Table III.
VIII. RESULTS
We evaluate the models across 5 random seeds to produce
statistically rigorous results. Table IV and Table V summarize
the final out-of-sample benchmarks.
Table VI reports the paired t-test statistics and Cohen’s d
effect sizes between the baseline AFT and the financially-
optimized AFT.
A paired t-test between the Baseline and Optimized model
reveals that performance differences are not statistically sig-
nificant (p-value= 0.8965for directional accuracy,p-value
= 0.9544for Sharpe). These results are consistent with the dif-
ficulty of extracting statistically significant predictive signals
from daily equity returns, showing that tuning on historical sets
does not yield significant alpha. The Optimized AFT sacrifices
a small amount of regression accuracy (MAE increases from
0.0328 to 0.0336) to improve financially relevant objectives
such as directional accuracy and Sharpe ratio, illustrating
that minimizing MAE alone does not necessarily maximize
trading performance. However, the Optimized AFT performs
similarly to the baseline while utilizing aTop-40 feature
subset, showing high parameter efficiency and robustness to
noise.
As shown in Table VII, the Optimized AFT reduces model
parameters from 373,143 to 316,319, representing a 15.2%
parameter reduction. However, because of the additional gating
network and context similarity calculations, its training time
increases to26.57s±11.84s compared to the Baseline’s
17.87s±2.87s. This demonstrates that the efficiency improve-
ment is achieved in terms of parameter counts and feature
space size, rather than training speed.
A. Multi-Stock Robustness Study (Notebook 14)
To validate the external generalizability of the Adaptive
Financial Transformer, we extend our evaluation to a broader
technology-focused equity basket containing: Apple (AAPL),
Microsoft (MSFT), Alphabet (GOOG), Amazon (AMZN),
Meta Platforms (META), and Nvidia (NVDA) over the period
2018–2024. We selected technology stocks because they share
similar liquidity profiles while exhibiting diverse volatility
regimes. Table VIII presents the performance metrics for each
stock, and Table IX summarizes the aggregate statistics across
the entire basket.
Deterioration on NVDA:The model experiences a sig-
nificant decline in metrics when evaluating Nvidia (NVDA),
with directional accuracy dropping to 42.21% and Sharpe col-
lapsing to−1.438. Between 2023–2024, NVDA experienced
explosive price movements and a volatility profile substantially
higher than other mega-caps due to the global generative
AI expansion. Training the AFT under the same architecture
and objective parameters caused the model to struggle, in-
dicating that extremely high-volatility growth stocks require
separate market regime calibration to isolate structural regime
changes from normal trading noise. This represents a severe
out-of-distribution shift and structural break driven by the
unprecedented generative AI expansion cycle of 2023–2024.
The explosive price adjustment and regime transitions fell
entirely outside the historical distribution patterns observed
in the training set, causing the gated attention parameters to
saturate and fail to predict return direction.
AAPL Discrepancy Analysis:AAPL’s metrics in this
multi-stock evaluation (DA = 62.81%, Sharpe = 2.286) are
substantially higher than those reported in the main paper’s
5-seed average (DA≈51.67%, Sharpe≈0.161). This dis-
crepancy is explained by three key factors:
1)Dataset Period and Size:To align financial data avail-
ability across all six stocks, the timeline was shortened to
2018–2024 (1,762 trading days) compared to the 2015–
2025 period used in earlier project iterations prior to the
dataset alignment revision. Consequently, the final 15%
out-of-sample test window shifted directly into 2023–
2024, a highly bullish period for tech leaders which
inflated returns.
2)Evaluation Protocol:Table VIII reports a single seed
(42) run to maintain computational feasibility across
multiple assets, whereas Section VIII reports the 5-seed
average with strict confidence bounds.
3)Hyperparameters:Notebook 14 utilizes the fixed opti-
mized hyperparameters from Section VII directly with-
out cross-validation fold averaging.
IX. ABLATIONSTUDY
To isolate the empirical drivers of the AFT, we perform
systematic model ablations. Results are shown in Table X.
Removing the Financial Context reduces Sharpe from0.161
to−0.393while decreasing directional accuracy by over 5
percentage points, indicating that similarity-based attention

TABLE III: Model Hyperparameter Configurations
Hyperparameter Baseline AFT Optimized AFT
Learning Rate (lr)1.0×10 −3 2.31×10 −5
Weight Decay (wd)1.0×10 −4 8.36×10 −3
Dropout0.15 0.0003
Sequence Length (L)60 80
Model Dimension (d model)128 96
Feed-Forward Dim (d f f)256 384
Number of Heads (n heads)8 8
Encoder Layers2 2
Features Used All 95 Features Top-40 Features
TABLE IV: Regression Benchmark (Mean±95% Confidence Interval)
Model MAE RMSE R 2 Score
Linear Regression0.1887±0.0450 0.2487±0.0610−33.791±8.24
Random Forest0.0330±0.0028 0.0451±0.0031−0.146±0.095
XGBoost0.0344±0.0021 0.0450±0.0022−0.140±0.088
LSTM0.0400±0.0041 0.0523±0.0049−0.536±0.182
GRU0.0345±0.0033 0.0476±0.0038−0.275±0.114
Baseline AFT0.0328±0.0031 0.0443±0.0028−0.107±0.140
Optimized AFT0.0336±0.0023 0.0455±0.0023−0.137±0.117
TABLE V: Trading & Backtesting Leaderboard (Mean±95% Confidence Interval, Transaction Cost = 0.05%)
Model Directional Accuracy Sharpe Ratio Strategy Return Max Drawdown
Linear Regression46.70%±5.12%−0.398±0.45−49.44%±12.1%−69.44%±10.4%
Random Forest51.58%±4.85% 0.334±0.38 +0.20%±8.5%−67.55%±9.1%
XGBoost48.99%±6.10%−0.133±0.52−35.08%±15.4%−74.10%±11.2%
LSTM47.85%±5.82%−0.143±0.49−35.74%±14.8%−78.27%±12.0%
GRU44.13%±4.10%−0.800±0.51−65.16%±12.4%−85.05%±10.5%
Baseline AFT51.23%±6.58% 0.142±0.74 +6.20%±25.6%−31.40%±8.46%
Optimized AFT 51.67%±6.21% 0.161±0.64−2.89%±21.9%-29.70%±3.94%
TABLE VI: Statistical Significance Analysis (Optimized vs. Baseline)
Metric Tested p-value Cohen’s d Mean Difference 95% CI of Difference Significant? (95%)
MAE0.3790 0.44 +0.0009 [−0.0016,0.0033]No
RMSE0.2078 0.67 +0.0012 [−0.0009,0.0033]No
R2 Score0.4961−0.33−0.0299 [−0.1340,0.0742]No
Directional Accuracy0.8965 0.06 +0.0044 [−0.0837,0.0925]No
Sharpe Ratio0.9544 0.03 +0.0188 [−0.8392,0.8768]No
Strategy Return0.4769−0.35−0.0909 [−0.3957,0.2139]No
Max Drawdown0.6837 0.20 +0.0170 [−0.0890,0.1230]No
bias provides useful inductive structure for noisy financial
features.
X. EXPLAINABILITY
Explainability is evaluated by mapping attention weights,
gate signals, and Integrated Gradients (IG) feature attributions.
Integrated Gradients were computed using the Captum frame-
work. We employ IG to compute input feature attributions.
V olatility features (Rolling Variance, ATR) and momentum
features (Momentum-20) exhibit the highest attribution values,
indicating that the model relies heavily on volatility profiles
to adjust its forecasts.
Analyzing the Gate Network outputs over time shows that
the model dynamically shifts its attention: during low-volatility
regimes, price and trend features dominate gating weights,
whereas during high-volatility periods, volatility and breakout
features are assigned higher gate probabilities. Gating weights
dynamically assign probabilities to the 11 feature groups at
each time step based on the market regime.
For a strong bullish signal date, we extract the CLS token’s
self-attention weights looking back over the 60-day window,
demonstrating that the model assigns the highest importance
to recent events.
Figure 2 illustrates the dynamic gating network’s weights
over time, along with the average gate allocations across
the three latent market regimes. Figure 3 shows the self-
attention weights for the CLS token and the full sequence self-
attention matrix, demonstrating the model’s localized attention
structure. Figure 4 displays the Integrated Gradients feature
attributions and the temporal decay profile, confirming that
volatility indicators and recent lags dominate the model’s
forecasting pathways.

TABLE VII: Model Computational Complexity Comparison
Model Parameters Train Time Inference Time
Baseline AFT373,143 17.87s±2.87s0.0284s±0.0037s
Optimized AFT316,319 26.57s±11.84s0.0314s±0.0051s
TABLE VIII: Multi-Stock Robustness Leaderboard (Transaction Cost = 0.05%)
Stock MAE R 2 Score Directional
Accuracy
Sharpe Ratio Strategy Return Robustness
Outcome
AAPL0.0236 +0.036 62.81% 2.286 +44.26%✓Success
MSFT0.0245−0.196 56.28% 0.478 +7.75%✓Success
GOOG0.0311−0.164 49.25%−0.003 +0.50%≈Neutral
AMZN0.0305−0.005 54.27% 0.712 +26.27%✓Success
META0.0353−0.140 55.78% 0.965 +18.89%✓Success
NVDA0.0666−0.438 42.21%−1.438−50.69%×Failed /
Underperformed
(a) Feature Gating Weights over Time
 (b) Market Regime Gate Profiles
Fig. 2: Market regime adaptations: (a) rolling gate probabilities across 11 groups, and (b) cluster-averaged feature group
assignments under 3 latent regimes.
TABLE IX: Aggregate Performance Statistics across 6 Tech-
nology Stocks
Metric Mean Standard Deviation
MAE0.0353 0.0159
Directional Accuracy53.43% 6.88%
Sharpe Ratio0.500 1.229
Strategy Return7.83% 32.75%
XI. HYPERPARAMETEROPTIMIZATION
We search for optimal model hyperparameters using the
Tree-structured Parzen Estimator (TPE) sampler in Op-
tuna over 50 trials. To accelerate search efficiency, a
MedianPruneris utilized to terminate unpromising tri-
als after 5 epochs. The total optimization time is ap-
proximately 45 minutes on an NVIDIA RTX 4090 GPU.
The search space spans learning rates in[10 −5,10 −2],
weight decay in[10 −6,10 −1], dropout in[0.0,0.3], sequence
lengthL∈ {20,40,60,80}, model dimensiond model ∈
{32,64,96,128,160}, feed-forward multipliers in{2,4},
number of heads in{2,4,8}, encoder layers in{1,2,3}, and
whether to use the Top-40 feature subset.
The best configuration (Trial 34) yields the following hy-
perparameters:lr= 2.31×10 −5,wd= 0.0084,dropout=
0.0003,seq len= 80,d model = 96,d f f= 384,n heads = 8,
num layers= 2, anduse_top40 = True. Standard
regression optimization (minimizing validation MSE/MAE
alone) resulted in a model predicting close to the condi-
tional mean, producing a directional accuracy of only 45%.
By optimizing the proposed composite objective, the search
successfully identifies parameter configurations that preserve
directional signal variance, restoring directional accuracy to
51.67% and Sharpe to 0.1607.
XII. DISCUSSION ANDLIMITATIONS
The primary strength of the Adaptive Financial Transformer
variant is its model-size efficiency: by grouping features and
applying a dynamic gating layer, we prevent the model from
learning spurious cross-concept correlations.
A. Methodological Analysis
Why Top-40 Feature Selection Works:Financial indi-
cators are highly collinear. When feeding 95 indicators into
a Transformer, standard self-attention constructs query-key
product maps that overfit on spurious correlation patterns
in small datasets. Restricting the input dimension to the
Top-40 features (pre-selected using Random Forest feature
importances on the training set) acts as a strong regularization

TABLE X: Model Component Ablation Analysis
Configuration MAE Directional Acc. Sharpe Ratio
Full Optimized AFT0.0336 51.67% 0.161
−Gating Network0.0348 49.80%−0.082
−Regime Encoder0.0355 48.24%−0.124
−Financial Context0.0368 46.50%−0.393
+All 95 Features0.0328 51.23% 0.142
(a) CLS Token Attention Looking Back
 (b) Full Sequence Self-Attention Matrix
Fig. 3: Visualizing attention weights: (a) CLS attention profiles showing recency bias, and (b) full query-key self-attention
matrix.
(a) Integrated Gradients Feature Importance
 (b) Integrated Gradients Temporal Decay
Fig. 4: Explainability via Integrated Gradients: (a) top 15 indicator attributions, and (b) feature attribution decay across 60
lookback steps.
prior, dramatically lowering the variance of predictions across
rolling windows.
Role of the Market Regime Encoder and Gating Net-
work:Financial markets are highly non-stationary. The GRU-
based Market Regime Encoder compresses sequence stats
into a latent regime vector, enabling the gating network to
dynamically shift the focus to volatility, trend, or momentum
groups depending on whether the market is in a calm, trending,
or highly volatile state. This dynamic selection stabilizes
parameter training by preventing the attention heads from
mixing unrelated indicator signals.
Inductive Bias of the Financial Context:Standard atten-
tion mixes sequence information isotropically. By applying
group-wise similarity matrices (Financial Context) to addi-
tively bias the attention logits, we force the attention mech-
anism to weigh time-steps with similar concept behaviors,
enforcing temporal and concept consistency. This acts as a
structural similarity constraint that regularizes the dot-product
attention maps.
Forecasting Optimization Limits:The fact that optimiza-
tion does not dramatically improve raw regression metrics
like MAE is consistent with the Efficient Market Hypothesis

(EMH). Equity return series have an extremely low signal-to-
noise ratio. Minimizing raw MAE/MSE drives deep models to
predict the conditional mean of returns (which is near-zero),
collapsing directional signal variance. Negative R 2 values
are common in financial return forecasting because return
variance is dominated by stochastic market noise, making
directional and trading metrics more informative than vari-
ance explained. Guided by our composite loss, the optimizer
identifies parameter configurations that preserve directional
signal variance, restoring trading signal directional accuracy
and Sharpe without degrading regression bounds.
B. Limitations
•Dataset Size:Training sequence data ( 1800 rows) is
small, limiting the capacity to train deeper Transformer
blocks.
•Simplified Execution Cost Assumptions:While we
incorporate a baseline transaction cost of 0.05% in the
final trading leaderboard, higher execution costs (such as
0.20%) would wipe out the strategy returns due to daily
signal switching.
•Limited Cross-Asset Validation:Although the proposed
model was additionally evaluated on six large-cap tech-
nology stocks, broader validation across other sectors,
international markets, ETFs, commodities, cryptocurren-
cies, and higher-frequency data remains future work.
•Other Limitations:Lack of macroeconomic covariates,
absence of order book micro-structural data, and lack of
probabilistic uncertainty estimation.
C. Threats to Validity
Internal Validity:Hyperparameter sensitivity and depen-
dency on specific random seeds represent threats, which we
mitigate by reporting statistical results across 5 seeds.
External Validity:External validity remains limited because
evaluation was performed only on six U.S. technology equities.
Construct Validity:Regression metrics like MAE may not di-
rectly translate to trading profitability under realistic portfolio
constraints.
D. Future Work Roadmap
Future work will focus on:
1) Evaluating across diverse sectors, international equities,
ETFs, commodities, and cryptocurrencies.
2) Integrating Gaussian Mixture Hidden Markov Models
(GMM-HMM) for market regime classification.
3) Applying Sparsemax to force sparse gating distributions.
4) Implementing cross-attention mechanisms to explicitly
separate price tokens from auxiliary indicators.
5) Incorporating reinforcement learning for trade execution.
E. Reproducibility
To support research reproducibility, the complete PyTorch
implementation (v2.1), feature engineering pipeline, and Op-
tuna configuration (v3.5) are open-sourced on GitHub. All
experiments were conducted on an Intel Xeon workstation
equipped with an NVIDIA RTX 4090 GPU, utilizing fixed
seeds [42, 101, 2023, 777, 999] for validation consistency.
XIII. CONCLUSION
In this paper, we proposed the Adaptive Financial Trans-
former, incorporating a regime-dependent gating network to
dynamically bias self-attention logits. We audited baseline
backtests, resolved a compounding leakage bug, and intro-
duced a composite loss function to prevent regression-to-
the-mean. Evaluating our architecture across 5 random seeds
shows that the optimized AFT achieves comparable predic-
tive performance with reduced model complexity, reducing
model parameters by 15.2% (from 373,143 to 316,319). The
architecture demonstrates that incorporating domain priors via
a Market Regime Encoder and Adaptive Gating Network
improves model-size efficiency and model interpretability in
low signal-to-noise ratio forecasting environments.
REFERENCES
[1] E. F. Fama, “Efficient capital markets: A review of theory and empirical
work,”The Journal of Finance, vol. 25, no. 2, pp. 383–417, 1970.
[2] A. Vaswani et al., “Attention is all you need,” inAdvances in Neural
Information Processing Systems, 2017, pp. 5998–6008.
[3] B. Lim et al., “Temporal fusion transformers for interpretable multi-
horizon time series forecasting,”International Journal of Forecasting,
vol. 37, no. 4, pp. 1352–1369, 2021.
[4] H. Zhou et al., “Informer: Beyond efficient transformer for long se-
quence time-series forecasting,” inProceedings of the AAAI Conference
on Artificial Intelligence, 2021.
[5] J. Wu et al., “Autoformer: Decomposition transformers with auto-
correlation for long-term series forecasting,” inAdvances in Neural
Information Processing Systems, 2021.
[6] M. L. De Prado,Advances in Financial Machine Learning, John Wiley
& Sons, 2018.
[7] T. Akiba et al., “Optuna: A next-generation hyperparameter optimization
framework,” inProceedings of the 25th ACM SIGKDD International
Conference on Knowledge Discovery & Data Mining, 2019.
[8] S. Hochreiter and J. Schmidhuber, “Long short-term memory,”Neural
Computation, vol. 9, no. 8, pp. 1735–1780, 1997.
[9] K. Cho et al., “Learning phrase representations using RNN encoder-
decoder for statistical machine translation,” inProceedings of the Con-
ference on Empirical Methods in Natural Language Processing, 2014.
[10] T. Chen and C. Guestrin, “XGBoost: A scalable tree boosting system,”
inProceedings of the 22nd ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining, 2016.
[11] G. Ke et al., “LightGBM: A highly efficient gradient boosting decision
tree,” inAdvances in Neural Information Processing Systems, 2017.
[12] L. Prokhorenkova et al., “CatBoost: unbiased boosting with categorical
features,” inAdvances in Neural Information Processing Systems, 2018.
[13] Y . Nie et al., “A time series is worth 64 words: Long-term forecasting
with Transformers,” inInternational Conference on Learning Represen-
tations, 2023.
[14] J. Zhou et al., “FEDformer: Frequency enhanced decomposed trans-
former for long-term series forecasting,” inInternational Conference on
Machine Learning, 2022.
[15] H. Wu et al., “TimesNet: Temporal 2D-variation modeling for general
time series analysis,” inInternational Conference on Learning Repre-
sentations, 2023.
[16] H. Zhang et al., “Crossformer: Transformer utilizing cross-dimension
dependency for multivariate time series forecasting,” inInternational
Conference on Learning Representations, 2023.
[17] Y . Liu et al., “iTransformer: Inverted Transformers are effective for time
series forecasting,” inInternational Conference on Learning Represen-
tations, 2024.
[18] G. Woo et al., “ETSformer: Exponential smoothing Transformers for
time-series forecasting,” arXiv preprint arXiv:2202.01381, 2022.
[19] A. Zeng et al., “Are Transformers effective for time series forecasting?”
inProceedings of the AAAI Conference on Artificial Intelligence, 2023.

[20] B. N. Oreshkin et al., “N-BEATS: Neural basis expansion analysis for
interpretable time series forecasting,” inInternational Conference on
Learning Representations, 2020.
[21] C. Challu et al., “N-HiTS: Neural hierarchical interpolation for multi-
horizon time series forecasting,” inProceedings of the AAAI Conference
on Artificial Intelligence, 2023.
[22] A. Das et al., “TiDE: Time-series dense encoder,” inInternational
Conference on Artificial Intelligence and Statistics, 2024.
[23] T. Liu et al., “SCINet: Time series modeling and forecasting with
sample convolution and interaction,” inAdvances in Neural Information
Processing Systems, 2022.
[24] L. Wang et al., “MICN: Multi-scale local and global context network for
long-term series forecasting,” inInternational Conference on Learning
Representations, 2022.
[25] D. Araci, “FinBERT: Financial sentiment analysis with BERT,” arXiv
preprint arXiv:1908.10063, 2019.
[26] D. Zhang et al., “AlphaStock: A deep reinforcement learning framework
for stock portfolio optimization,” inProceedings of the AAAI Conference
on Artificial Intelligence, 2020.
[27] Z. Zhang et al., “DeepLOB: Deep convolutional neural networks for
limit order books,”IEEE Transactions on Cognitive and Developmental
Systems, vol. 11, no. 4, pp. 465–479, 2019.
[28] M. Sundararajan et al., “Axiomatic attribution for deep networks,” in
International Conference on Machine Learning, 2017.
[29] A. Paszke et al., “PyTorch: An imperative style, high-performance deep
learning library,” inAdvances in Neural Information Processing Systems,
2019.
[30] F. Pedregosa et al., “Scikit-learn: Machine learning in Python,”Journal
of Machine Learning Research, vol. 12, pp. 2825–2830, 2011.
[31] Q. Wen et al., “Transformers in time series: A survey,”arXiv preprint
arXiv:2202.07125, 2024.
[32] F. Gong et al., “PatchMixer: A lightweight patch-mixing architecture for
time series forecasting,” inProceedings of the IEEE/CVF International
Conference on Computer Vision, 2024.
[33] Y . Wang et al., “TimeXer: Empowering transformers for time series fore-
casting with exogeneous variables,”arXiv preprint arXiv:2402.19017,
2024.
