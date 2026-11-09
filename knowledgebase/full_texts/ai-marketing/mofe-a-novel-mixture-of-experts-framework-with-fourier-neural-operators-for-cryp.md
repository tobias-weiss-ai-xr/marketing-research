---
title: 'MoFE: A Novel Mixture-of-Experts Framework with Fourier Neural Operators for Cryptocurrency Forecasting'
url: https://arxiv.org/abs/2608.17342
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Bowen Liu
- Mingming Sun
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.17342
pages: 9
chars: 44521
fetched_at: '2026-11-08T13:23:09+00:00'
kb_version: 1
---

# MoFE: A Novel Mixture-of-Experts Framework with Fourier Neural Operators for Cryptocurrency Forecasting

MoFE: A Novel Mixture-of-Experts Framework
with Fourier Neural Operators for Cryptocurrency
Forecasting
Bowen Liu
School of Art and Science
University of Rochester
Rochester, USA
bliu59@u.rochester.edu
Mingming Sun
AGI Lab
Beijing Institute of Mathematical Sciences and Applications
Beijing, China
sunmingming@bimsa.cn
Abstract—Forecasting cryptocurrency prices remains a
formidable challenge due to inherent non-stationarity, abrupt
regime shifts, and multi-scale stochastic dependencies. Conven-
tional deep learning models often struggle to capture complex
underlying dynamics, frequently resulting in persistent phase-
lagged predictions. To address these limitations, we propose
MoFE, a novel deep learning framework that integrates Fourier
Neural Operators (FNOs) within a Mixture-of-Experts (MoE)
architecture. Rooted in the theoretical framework of stochas-
tic differential equations, MoFE conceptualizes cryptocurrency
volatility as a superposition of multi-frequency components,
which includes user network based fundamental growth, min-
ing costs and halving mechanism caused seasonal volatility,
and market sentiment-induced chaos. Specifically, specialized
adaptive FNO (AFNO) and Convolution dual-domain experts
learn continuous function-to-function mappings to encapsulate
global spectral trends, cyclical adjustments and microstructures,
while a dynamic gating based MoE mechanism enables adaptive
strategy switching across diverse market regimes. Extensive
experiments on Bitcoin datasets spanning January 2020 to
December 2025 demonstrate that MoFE achieves state-of-the-art
(SOTA) performance in both T+1 and T+5 forecasting horizons.
Notably, the model effectively mitigates the phase-lag effect,
delivering superior Directional Accuracy (DA) and Information
Coefficient (IC). In high-fidelity simulated trading environments,
these predictive gains transfer into significant excess returns
and robust risk-adjusted performance, characterized by a high
Sharpe ratio.
Index Terms—Cryptocurrency Forecasting, Fourier Neural
Operators, Mixture-of-Experts.
I. INTRODUCTION
Cryptocurrency price forecasting represents a pivotal fron-
tier in computational finance, increasingly shifting from
heuristic technical analysis toward sophisticated data-driven
machine learning paradigms [1], [2]. Robust predictive capa-
bilities are fundamental to enhancing market transparency and
© 2026 IEEE. Personal use of this material is permitted. Permission from
IEEE must be obtained for all other uses, in any current or future media,
including reprinting/republishing this material for advertising or promotional
purposes, creating new collective works, for resale or redistribution to servers
or lists, or reuse of any copyrighted component of this work in other works.
DOI: 10.1109/ICBC67748.2026.11575439
facilitating informed decision-making for both institutional
investors and regulatory stakeholders.
Unlike traditional assets anchored by fundamental yields,
cryptocurrencies are governed by algorithmic scarcity and
network-driven valuations—dynamics often modeled by fun-
damental growth guided by Metcalfe’s Law, seasonal volatility
driven by mining costs and halving mechanisms, and chaos
induced by market sentiment [3]. The absence of intrinsic valu-
ation anchors leaves the market susceptible to sentiment-driven
volatility, frequently invalidating traditional mean-reversion
frameworks [4]. Developing robust predictive models remains
a formidable challenge due to inherent non-stationarity, abrupt
regime shifts, and multi-scale stochasticity [3]. Furthermore,
compared to the centuries of data in equity markets, the
relatively brief history of cryptocurrencies induces a “data
scarcity” problem, particularly when analyzing low-frequency
cyclical patterns like the quadrennial “halving” events [5].
The landscape of cryptocurrency price forecasting has tran-
sitioned from heuristic technical analysis toward sophisticated
data-driven machine learning paradigms. Initially, classical sta-
tistical and ensemble frameworks [6]–[8] leveraged historical
inertia to model market trends. Meanwhile, some research
introduced sentiment-based approaches [4] based on on-chain
data and social media psychology to quantify market value
beyond endogenous price action. However, these methods
primarily capture linear dynamics or non-inherent dynamics
and are often inadequate for the pervasive non-stationarity of
crypto-markets.
Initially, classical statistical frameworks (e.g., ARIMA [6]
and GARCH [7]) and ensemble models leveraged historical
inertia to model market trends.
Currently, deep representation learning defines the state-of-
the-art, utilizing non-linear optimization to decode intricate
dependencies. This evolution spans Recurrent Neural Net-
works (RNNs) for temporal modeling [9], [10], Transformers
and State-Space-Models (SSMs) for long-range dependency
modeling [11], [12], which would like capture cross-period
stochastic volatilization. Despite their success, conventional
deep learning models primarily minimize point-wise statistical
arXiv:2608.17342v1  [cs.LG]  18 Aug 2026

errors via regression. Consequently, they often fail to internal-
ize the underlying continuous spectral dynamics of the market,
resulting in significant phase lags and an inability to adapt to
rapid regime shifts.
Many existing approaches primarily optimize point-wise
regression errors, which often leads to phase lag and weak
adaptability to rapid market regime shifts [13], [14]. In ad-
dition, purely time-domain models tend to be sensitive to
high-frequency market noise, which is particularly common
in cryptocurrency markets [15].
Beyond traditional architectures, Fourier Neural Operators
(FNOs) [16] have redefined sequence modeling by learning
continuous function-to-function mappings in the frequency do-
main. Notably, the Adaptive FNO (AFNO) [17] optimizes this
process via frequency sparsification, allowing for continuous
global convolutions that are invariant to input resolution. Fur-
ther advancements in frequency-domain Mixture-of-Experts
(MoE) [18] have demonstrated superior performance in mod-
eling complex Partial Differential Equation (PDE) systems and
non-stationary time series. Motivated by the success of these
spectral methods, this work introduces a frequency-domain
motivated MoE-FNO framework. By modeling cryptocurrency
volatility as a superposition of multi-frequency components,
our framework captures the multi-scale stochasticity inherent
in digital assets to improve the accuracy of return forecasting.
The proposed MoFE framework complements these ap-
proaches by combining frequency-domain and time-domain
modeling. The global FNO component captures long-range
dependencies and cyclical market dynamics, while the convo-
lutional branch extracts short-term temporal microstructures.
The main contributions of this study are as follows:
•We design a novel MoE-FNO framework tailored
for cryptocurrency markets, capable of modeling non-
stationary volatility and abrupt regime shift through
multi-experts decomposition and nonlinear optimization.
•We introduce an AFNO-Conv dual-domain operator that
simultaneously captures global cyclical patterns in the
frequency domain and transient local microstructures in
the temporal domain, addressing the multi-scale nature of
financial data.
•Our proposed model, MoFE, achieves state-of-the-art
(SOTA) performance across statistical metrics (RMSE,
R2) and financial indicators (Sharpe Ratio, Information
Coefficient, ROI). High-fidelity back-testing demonstrates
significant risk-adjusted returns and robust predictive
consistency.
II. RELATEDWORK
Bitcoin, as the pioneer of decentralized cryptocurrencies,
has become one of the most volatile and scrutinized assets
in global financial markets [2]. Unlike traditional financial in-
struments such as stocks and bonds, Bitcoin operates indepen-
dently of centralized monetary authorities, and its valuation is
influenced by a complex interplay of factors including market
liquidity, mining costs, macroeconomic changes, and investor
sentiment [1]. This extreme volatility, structural instability, and
inherent non-linearity make Bitcoin price prediction excep-
tionally difficult. Therefore, establishing a robust forecasting
framework is crucial for improving market transparency and
providing institutional investors and regulators with a rigorous,
data-driven basis for decision-making.
The corpus of existing literature on cryptocurrency
forecasting is generally taxonomized into three distinct
paradigms. First, statistical methodologies predicate their pre-
dictions on linear dynamical systems and stochastic pro-
cesses—exemplified by ARIMA [6] and GARCH [7]. These
models operate under strong assumptions of stationarity and
historical autocorrelation. However, such approaches are in-
herently constrained to capturing local or univariate features.
Consequently, these conventional architectures often fail to
simultaneously resolve global frequency-domain patterns and
localized temporal dynamics in highly volatile markets. Sec-
ond, fundamental and sentiment analysis paradigms attempt
to quantify intrinsic asset value through on-chain network
adoption metrics (e.g., stock-to-flow models) and behavioral
indicators [4]. These methods are premised on the hypothesis
that information dissemination and social media discourse
serve as leading indicators for subsequent price fluctuations.
In recent years, deep learning methodologies have estab-
lished a new state-of-the-art by leveraging non-linear optimiza-
tion to capture high-dimensional dependencies within financial
datasets. Recurrent Neural Network (RNN) variants, most
notably Long Short-Term Memory (LSTM) [9] and Gated
Recurrent Units (GRU) [10], employ sophisticated gating
mechanisms to characterize temporal dynamics. Specifically,
the GRU architecture enhances computational efficiency by
consolidating the LSTM’s forget and input gates into a single
update gate, often facilitating superior convergence in Bitcoin
volatility modeling. Beyond recurrent paradigms, gradient-
boosted frameworks such as XGBoost [8] have demonstrated
competitive performance in minimizing mean deviation errors
relative to traditional LSTMs. More recently, self-attention-
based Transformer architectures [11], [19] have achieved sig-
nificant performance gains by exploiting global long-range
dependencies. Despite these advancements, a fundamental
limitation still persists: these predominantly time-domain mod-
els—including LSTMs and Transformers—exhibit high sus-
ceptibility to high-frequency noise, which frequently obscures
the latent low-frequency trends inherent in cryptocurrency
markets [15]. Furthermore, recent studies highlight that models
relying exclusively on conventional point-wise regression loss
functions are prone to structural phase lag, thereby failing
to capture regime-specific dynamics under the extreme non-
stationarity of digital assets [13], [14]. While contemporary
innovations like Smamba [20] and CryptoMamba [12] at-
tempt to mitigate these issues through enhanced structural
generalizability, the inability to disentangle complex dynamics
within the frequency domain remains a critical barrier to
achieving robust generalization. However, they often struggle
with multi-scale feature extraction in the presence of non-
stationary volatility.
Frequency-domain methodologies, such as Fourier analy-

sis [21] and Fourier Neural Networks [22], have demonstrated
significant efficacy in time-series forecasting by leveraging
the inherent time-frequency duality of spectral representations.
Concurrently, Mixture-of-Experts frameworks [23]–[25] have
advanced financial predictive modeling through the dynamic
coordination of specialized experts. While recent hybrid ar-
chitectures like FreqMoE [18] have successfully integrated
FNOs with MoE for solving complex PDE systems, the
synergistic application of MoE-driven expert collaboration
and FNO-based function-to-function mapping remains largely
unexplored in the context of cryptocurrency markets. Conse-
quently, there is a notable research gap in utilizing these com-
bined paradigms to address the pervasive challenges of non-
stationarity, abrupt regime shifts, and multi-scale stochasticity
inherent in digital asset dynamics.
III. METHODOLOGY
A. Architecture Overview
The architecture of the proposed MoFE model is illus-
trated in Figure 1. The process begins with a Stem Block
comprising aLinearlayer, which projects the input data
sequence into a high-dimensional latent space withd model.
Subsequently, these features are concurrently processed byK
parallel Experts and a Gating Network (MoE block). Each
expert is designed as a time-frequency dual-domain feature
extraction module. Specifically, the global FNO path employs
an adaptive FNO to capture global cyclical fluctuations fea-
tures via a sparse MLP in the frequency domain, while the
local context path utilizes an×1convolution (e.g.,n= 3) to
extract local microstructure features in the temporal domain.
Simultaneously, the Gating Network regresses expert weights
through an MLP and a Softmax layer. These weights are
then applied to the expert outputs via Batch Matrix Multi-
plication (BMM) to dynamically re-weight their contributions.
Finally, the aggregated features are passed through a Prediction
Head—consisting ofLinear,GELU, andDropoutlayers—to
produce the final forecasts for prices and returns.
B. Our MoFE Model
1) FNO-Expert:Each expertE k(X)∈R B×K×C in our
MoFE framework, whereX∈R B×L×C denotes the hidden
representation (withB, L, Crepresenting batch size, sequence
length, and channel dimensiond model, respectively), employs
a dual-path architecture. This design is specifically engineered
to synergistically capture global periodic patterns and local
transient microstructures.
Global FNO Path -The core of the FNO-expert uti-
lizes a one-dimensional Adaptive Fourier Neural Operator
(AFNO) [17] to model long-range dependencies and cyclical
market fluctuations. This path operates under the premise
that financial time-series evolution can be decomposed into
complex modal interactions within the frequency domain. The
global path is formulated as:
Xglobal = LN

X+F −1 (LPF(MLP complex(F(X))))  ,(1)
whereX global ∈R B×K×C ,F(·)is a Fast Fourier Transform
(FFT),F −1(·)is an Inverse FFT (IFFT),LNis the Layer-
Norm, MLP complex(·)is a complex-valued MLP block.
The operator LPF represents a spectral filtering mecha-
nism using a Low Pass Filter (LPF) to mitigate noise and
redundancy through two operators:Hard Thresholding, which
truncates high-frequency components to retain only the most
significant low-frequency modes andSoft Shrinkage (SS),
which sparsifies the spectral coefficients by filtering out low-
amplitude noise withSS(Z) = sign(Z) max(0,|Z|−λ), where
λis a sparsity threshold.
Local Context Path -To complement the spectral path’s
inherent lack of spatial localization, we introduce a parallel
local context branch. It consists of a 1D-convolution with a
kernel size ofn(n= 3), followed by Batch Normalization
(BN), to capture short-term momentum, abrupt shocks, and
localized trend variations:
Xlocal = BN(Conv1D(X))(2)
whereX local ∈R B×K×C .
Feature Fusion -The global spectral features and local
spatial contexts are integrated via element-wise summation.
The fused representation is then projected back to the model
dimension using a point-wise convolution (1×1) and a
LeakyReLUactivation:
Ek(X) =Conv(LeakyReLU(Xglobal +X local)).(3)
2) Mixture-of-Experts System:Cryptocurrency markets are
characterized by high non-stationarity, exhibiting distinct dy-
namic regimes (e.g., bullish, bearish, or sideways). The MoE
module adaptively manages this regime-switching via a Gating
Network, which performs conditional computation by select-
ing the most relevant experts for a given market state. The
gating mechanism and expert aggregation are defined as:
ˆX=
KX
k=1
Softmax(MLP(vec(X)))k| {z }
Gating weightg k
·E k(X)| {z }
Expert output
,(4)
wherevec(·)is used to flatten the input to a vector,Softmax(·)
is the Softmax operation, theMLP(·)denotes a learnable
MLP that maps the flattened inputvec(X)∈R B×LC to
gating logits. The aggregation is implemented as a batch-wise
weighted sum, allowing the model to dynamically reconfigure
its internal logic based on the latent state of the batch.
3) Prediction Head:The final forecast is decoded from the
aggregated latent features ˆXthrough a multi-layer perceptron
(MLP) based prediction head. To ensure robust mapping and
mitigate potential overfitting, the head incorporates non-linear
activations and stochastic regularization:
Ypred = Linear(Dropout(GELU(Linear(ˆX)))),(5)
whereY pred ∈R B×Horizon ,GELUdenotes the activation
function. This head structure allows the model to refine the
high-dimensional latent representations into precise price or
return forecasts while maintaining generalization capability.

Fig. 1. The overall architecture of the MoFE model. The input features are processed through parallel global (FNO) and local (Conv) paths within the experts,
dynamically weighted by the gating network.
C. Loss Function
To address the inherent complexities of financial time-series
forecasting, we propose a multi-objective function termed
the Break-even Optimized Loss. Unlike conventional ap-
proaches that rely solely on Euclidean distance minimization,
our composite loss functional integrates magnitude accuracy,
correlation-based alignment, and directional consistency to
better capture market dynamics:
LT ask=αL w M SE+βL IC + (1−α−β)L Dir,(6)
where the componentsL w M SE,L IC , andL Dir represent the
weighted Mean Squared Error of log return, Information Coef-
ficient loss, and Directional Accuracy loss, respectively. These
metrics are grounded in established financial econometrics
and forecasting literature [26]–[28]. The hyperparametersα,
βgovern the trade-offs between these competing objectives.
From a mathematical standpoint, discrete post-hoc strategy
metrics derived from executed trading signals, such as the
Win/Loss ratio, are non-differentiable. Therefore, they are
structurally incompatible as direct penalty terms in backprop-
agation.
However, the proposed Break-even Optimized Loss is ex-
plicitly architected to achieve this trade-off without compro-
mising differentiability via the existing continuous hyperpa-
rametersαandβ. Specifically, Magnitude Accuracy is directly
governed byα(which weights the LMSE term), whereas
Directional Frequency is controlled by the residual weight
(1−α−β)for LDir andβfor LIC.
This formulation allows practitioners to tune the existing
αandβparameters to customize the model’s risk-reward
profile. For instance, aggressive trading strategies prioritizing
directional hit rates (Win/Loss) over magnitude suppression
can simply lower theαweight, thereby achieving trading style
flexibility.
A common challenge in MoE architectures is “expert col-
lapse” (or mode collapse), where the gating mechanism con-
verges to a state that activates the same subset of experts for all
inputs, thereby sacrificing model capacity. To enforce expert
specialization and diversity, we introduce an orthogonality
constrained regularization lossL Reg on the gating activations,
LT otal=L T ask+γL Reg,(7)
whereγis the weight of the regularization loss.
LetG∈R B×K denote the gating activation matrix for a
batch sizeBwithKexperts. We first performL 2 normaliza-
tion on the activation vectorsg k (gk ∈R B×1, seen in Equ. 4)
of each expertk(representing thek-th column ofG) to ensure
scale invariance:
ˆgk = gk |gk|2 +ϵ ,(8)
where| · |2 is anL 2 normalization,ϵis a small constant for
numerical stability, resulting in the normalized matrix ˆG∈
RB×K .
To promote decorrelation among experts, we penalize the
off-diagonal elements of the Gram matrix ˆGT ˆG∈R K×K to
drive it toward the identity matrixIas
LReg =∥ ˆGT ˆG−I∥ F ,(9)
where∥ · ∥F denotes the Frobenius norm. This regularization
term effectively encourages disjoint expert activation patterns,
ensuring that different experts specialize in distinct market
regimes or latent feature subspaces.
IV. EXPERIMENTALANALYSIS ANDDISCUSSION
A. Datasets
The dataset for this study was collected via a bespoke
web crawler from historical Bitcoin repositories, spanning
the period from January 1, 2020 to December 27, 2025.
The raw data comprises daily Open-High-Low-Close-V olume
(OHLCV) metrics organized in strict chronological order.
To maintain temporal integrity, the dataset was physically
partitioned into training, validation, and testing sets with an
approximate ratio of 4:1:1 prior to any preprocessing.

The dataset for this study was collected using a Python
script accessing the Binance Public API (specifically the
v3/klines endpoint). The raw exchange data comprises daily
cryptocurrency K-line data organized in strict chronological
order, spanning the period from January 1, 2020, to December
27, 2025. It includes six primary attributes: Timestamp, Open,
High, Low, Close, and V olume.
To preclude data leakage, normalization was applied locally
to each sliced window, while global standardization parameters
and z-score were derived exclusively from the training set. All
data used in the test set, including for forecasting inference and
performance metric calculations, only uses data from before
the given time point, and not data from after that time point.
It is imperative to explicitly recognize the scope and
boundaries of our methodology. First, our data collection
strictly relies on endogenous market variables (OHLCV data)
from the Binance exchange, explicitly excluding external
macroeconomic indicators (e.g., interest rates, inflation) that
might drive long-term valuations. Second, while the MoFE
model demonstrates robustness, its predictive reliability may
diminish under extreme market conditions or systemic ”black
swan” events where historical patterns fundamentally break
down. Finally, the current 32-day look-back window may be
insufficient to capture very low-frequency cyclical patterns,
such as the quadrennial Bitcoin halving events.
To enhance the representative capacity of the MoFE model,
the feature space is expanded into an 8-dimensional vector.
This includes the logarithmic returns of the OHLC prices,
supplemented by four technical indicators, including Relative
Strength Index (RSI), Moving Average Convergence Diver-
gence (MACD), Relative V olume (RV ol), and a V olatility
Proxy (VolProxy). TheVolProxycharacterizes price fluctua-
tions based on the log returns over a rolling window ofn= 5
days. These features are derived according to established
technical analysis methodologies [29], [30] to capture both
momentum and volatility dynamics.
B. Performance Metrics
To rigorously evaluate the predictive efficacy and practical
profitability of the MoFE model within the volatile Bitcoin
market, we implement a multi-dimensional evaluation frame-
work. This framework is categorized into three dimensions:
Statistical Predictive Metrics, Trading Strategy Metrics, and
Profitability Metrics.
Statistical forecasting metrics quantify a model’s ability to
minimize forecast error and capture market return variance.
These metrics include root mean square error (RMSE), mean
absolute error (MAE), andR 2 [31]. These metrics are all
back-calculated prices statistical error computed from the log
return forecasting from the MoFE. The trading strategy metrics
are used to evaluate the quality and persistence of investment
signals or “alpha models”, including Information Coefficient
(IC) [26] and Directional Accuracy (DA) [28]. Beyond sta-
tistical accuracy, we assess the model’s utility in simulated
trading environments, including Win/Loss Ratio [32], Cumu-
lative Return (ROI) [26], and Annualized Sharpe Ratio [33].
In this experiment, Transaction Fee rate and slippage fee are
set0.1%and0.2%respectively on day-line trading.
C. Experiments Setup
All proposed models and baselines were implemented using
the PyTorch framework and executed on a platform equipped
with an NVIDIA GeForce RTX 4060 Laptop GPU. To ensure
experimental rigor and a fair benchmarking environment, we
maintained consistent configurations across all evaluated mod-
els. This includes a fixed random seed (42) for deterministic
behavior, uniform data partitioning, identical input features.
All models were optimized using the AdamW optimizer
with a standardized learning rate schedule.
All models were optimized using the AdamW optimizer.
To mitigate overfitting and ensure optimal generalization, we
incorporated a ReduceLROnPlateau learning rate scheduler,
weight decay, and an early stopping mechanism with a pa-
tience of 20 epochs. The model checkpoint with the lowest
validation loss was selected for testing.
Tab. I summarizes the experimental configuration. We uti-
lize a look-back window ofL= 32days for forecasting
cumulative log-returns. Given the high susceptibility ofT+ 1
predictions to transient noise, our evaluation emphasizes the
T+5horizon to better assess the capture of persistent temporal
dependencies. The model dimension is set tod model = 48.
Within the MoE-FNO framework, we deployK= 2experts
to prevent overfitting, with each expert operating onM= 8
frequency modes. This design strikes an optimal balance
between model capacity and computational efficiency.
TABLE I
HYPERPARAMETERCONFIGURATION OFMOFE
Category Hyperparameter Value
DataLook-back Window (L) 32
Forecast Horizon (T p) 1, 5
ModelHidden Dimension (d model) 48
Frequency Modes 8
Number of Experts (K) 2
FNO Blocks 1
Dropout Rate 0.5
TrainingBatch Size 128
Initial Learning Rate5×10 −4
Weight Decay1×10 −2
Loss Weights (α, β) 0.20, 0.30
Reg. Loss Weights (γ) 0.05
D. Price Forecasting Experiments
1) Overall Performance:The quantitative results of our
comparative study are summarized in Tab. II and III. We
benchmark the proposed MoFE framework against a suite of
state-of-the-art baselines across prediction horizons ofT+ 1
andT+ 5.
In terms of specific comparisons, traditional RNN-based
architectures (e.g., LSTM [9] and GRU [10]) achieve com-
petitive DA but yield suboptimal results in profitability and
precision compared to MoFE. While the iTransformer [11]

demonstrates competence in select metrics, it generally lacks
the comprehensive competitiveness of our proposed method.
Furthermore, although recent state-space models such as Cryp-
toMamba [12] exhibit promising potential, MoFE maintains
a clear performance margin. Moreover, other MoE models
like FreqMoE [18] and MoLE [24] are also overshadowed
by MoFE. The empirical evidence indicates that MoFE con-
sistently surpasses existing methods, demonstrating significant
improvements in both statistical accuracy and economic utility.
This superiority is largely attributed to MoFE’s modeling
capability on cryptocurrency non-stationary volatilization.
2) T+1 Forecasting:
Predictive Accuracy Analysis:It can be concluded from
Tab. II and Fig. 2 that
MoFE outperforms all baselines, yielding a minimum
RMSE of $1582.64 and a maximumR 2 of 0.9827, signaling
a precise mapping of continuous market dynamics. Unlike
conventional models that often suffer from significant phase
lag by collapsing into a trivial identity function (P t+1 ≈P t),
MoFE captures genuine structural shifts. This distinction is
vital in finance, where high autocorrelation often inflates
RMSE andR 2 scores through a naive Lag-1 imitation of
price persistence. By maintaining high DA far above the 50%
baseline, MoFE proves its robustness against the deceptive
optimism of standard statistical metrics and its ability to
identify actionable volatility clusters.
Fig. 2. Visualized results of the comparison of predicted prices and real
prices.
Directional Predictive Capability:Beyond point-wise con-
vergence, MoFE demonstrates superior directional predictive
strength. From Tab. II, at theT+ 1horizon, it achieves a peak
IC of 0.1957 and DA of 58.43%, with its IC exceeding the
runner-up baseline by 1.6×. This suggests an exceptionally
robust monotonic correspondence between predictive signals
and realized returns.
Visualized results in Figs. 3 and 4 further elucidate these
findings below: (1) In Fig. 3, the predicted cumulative returns
(blue line) exhibit a dampened amplitude relative to market
volatility (grey bars). This reduced variance underscores the
efficacy of our balanced loss function, which induces strategic
conservatism by penalizing significant directional deviations.
(2) Despite this magnitude suppression, the predicted tra-
jectory closely tracks actual market trends. The scatter plot
Fig. 3. Visualized results of the log returns prediction versus the real
situations.
Fig. 4. Visualized results of the correlation scatter of the predicted log-returns
and the realized market returns.
in Fig. 4 confirms this, with the points densely clustered
around the diagonal line (y=x), indicating a strong linear
correlation. Simultaneously, the clustering of points neary= 0
reflects the risk-aversion effect of the loss function. These
results collectively provide empirical evidence that MoFE can
effectively filter out high-frequency noises while preserving
high-fidelity directional signals, which is consistent with its
superior IC and DA metrics.
Financial Performance Evaluation:MoFE model
achieved the superior performance in terms of ROI (4.41)
and Sharpe Ratio (3.89), which indicates that the model not
only achieves a superior return rate while maintaining a low
risk profile. This shows that MoFE model yields substantial
excess returns in unit risk. Although MoFE has Win/Loss
Ratio a slightly lower than GRU and iTransformer, it still
performs better in overall return and risk control.
3) T+5 Forecasting:
Predictive Accuracy Analysis:Even though having slightly
higher MAE ($2593.37) than iTransformer model only at the
difference of 1.05, MoFE model still has the smallest RMSE
($3360.33) andR 2 (0.9186) inT+ 5price prediction. Since
RMSE is more sensitive to large errors, the results showed
that the MoFE model is more stable.
Directional Predictive Capability:Similar to the situation
of T+1 prediction, MoFE model also took the lead in IC
(0.1389) and DA (56.10%).
Financial Performance Evaluation:InT+ 5prediction,
MoFE model also performed best in ROI (4.91) and Sharpe

TABLE II
PERFORMANCE COMPARISON OFMOFEAGAINST BASELINE MODELS FORT+1PREDICTION. THE BEST RESULTS ARE INBOLD.
Model Statistical Metrics Strategy Metrics Profitability Metrics
RMSE/$ (↓) MAE/$ (↓)R 2 (↑) IC (↑) DA (%) (↑) Sharpe (↑) W/L Ratio (↑) ROI (x) (↑)
LSTM [9] 1618.35 1134.32 0.9819 0.0611 54.52% 1.00 1.00 1.48
GRU [10] 1605.20 1130.03 0.9819 0.0725 53.01% 1.031.241.16
iTransformer [11] 1603.96 1130.63 0.9822 0.1225 51.51% 2.42 0.96 2.75
S-Mamba [20] 1662.95 1183.44 0.9809 0.0127 54.82% 1.40 0.96 1.86
CryptoMamba [12] 1613.97 1145.64 0.9820 0.1123 51.81% 2.93 1.17 3.13
FreqMoE [18] 1607.94 1140.63 0.9821 0.1156 52.41% 1.34 1.09 1.69
MoLE [24] 1621.76 1151.95 0.9818 0.1181 55.72% 2.11 1.07 2.45
MoFE (Ours) 1582.64 1106.10 0.9827 0.1957 58.43% 3.891.094.41
TABLE III
PERFORMANCE COMPARISON OFMOFEAGAINST BASELINE MODELS FORT+5PREDICTION. THE BEST RESULTS ARE INBOLD.
Model Statistical Metrics Strategy Metrics Profitability Metrics
RMSE/$ (↓) MAE/$ (↓)R 2 (↑) IC (↑) DA (%) (↑) Sharpe (↑) W/L Ratio (↑) ROI (x) (↑)
LSTM [9] 3392.81 2596.66 0.9170 0.101556.10%1.07 0.68 1.07
GRU [10] 3410.93 2618.38 0.9146 0.0326 52.44% 1.11 1.15 0.90
iTransformer [11] 3381.622592.320.9176 0.0760 53.66% 1.071.371.50
S-Mamba [20] 3443.05 2620.90 0.9146 0.0259 54.88% 0.82 1.05 0.92
CryptoMamba [12] 3650.63 2798.99 0.9040 0.0473 54.88% 0.96 1.17 1.60
FreqMoE [18] 3414.83 2620.41 0.9160 0.0678 55.18% 1.29 1.22 1.82
MoLE [24] 3493.51 2699.26 0.9120 0.0142 51.83% 0.36 1.11 0.40
MoFE (Ours) 3360.332593.370.9186 0.1389 56.10% 1.731.264.91
Ratio (1.73). Its exceptional ROI significantly outperforms
competing models, surpassing the second-best approach by a
factor of three. Even though it still did not get the highest
Win/Loss Ratio. It remains the optimal architecture for maxi-
mizing risk-adjusted returns.
4) Robustness and Horizon Sensitivity:While the horizon
extends from 1 to 5, all models exhibit a natural deterioration
in Predictive Metrics, characterized by increased RMSE/MAE
and decreasedR 2. However, MoFE demonstrates superior
robustness, suffering only a marginal and controllable decline.
Crucially, its ROI improves rather than declines over this
longer horizon, which highlights its ability to grasp mid-term
market dynamics. The results indicate that that MoFE model
can not only dominate short-term forecasting but also leads in
medium-term scenarios.
E. Efficiency Analysis
The MoFE model demonstrates high computational and
parameter efficiency for bothT+1 andT+5 forecasting tasks.
Specifically, the model requires 93.6K parameters and con-
sumes 2.36M FLOPs inT+1 mode, while theT+5 con-
figuration requires 94.1K parameters with identical FLOPs.
These metrics are highly competitive with established baseline
models.
Crucially, despite integrating a complex dual-domain struc-
ture, MoFE achieves SOTA performance with a highly
lightweight footprint, making it explicitly competitive against
more parameter-heavy baselines such as iTransformer and
Mamba-based models, which typically demand significantly
higher memory and computational overhead.
F . Interpretability Analysis
Figure 5 indicates that the two experts will change the
weight according to different conditions. Sometimes, the ex-
perts represented in blue dominate the choice depicted in
orange gets more weights. By using the Reg. Loss, the two
experts are incentivized to capture distinct feature subspaces.
One focuses on short-term fluctuations and the other one focus
on long-term trend. This enables the model to possess both the
time and frequency domain perspective.
Fig. 5. Visualized results of two experts’ dynamic weights during mixing.

TABLE IV
ABLATIONSTUDY
Model Statistical Metrics Strategy Metrics Profitability Metrics
RMSE/$ (↓) MAE/$ (↓)R 2 (↑) IC (↑) DA (%) (↑) Sharpe (↑) W/L Ratio (↑) ROI (x) (↑)
1 Expert (w/o MoE) 1608.70 1127.54 0.9821 0.0903 51.51% 1.661.371.43
4 Experts (w MoE) 1658.03 1184.79 0.9810 0.0680 53.01% 1.29 1.16 1.70
2 Experts (w/o MoE) 1633.03 1142.99 0.9816 0.1077 54.52% 0.67 1.07 1.76
Conv. Kernel in Experts (n= 1) 1597.61 1161.83 0.9824 0.1627 55.12% 2.11 1.13 2.52
Conv. Kernel in Experts (n= 5) 1602.83 1129.21 0.9823 0.1324 54.22% 3.31 1.12 2.66
w/o Reg. Loss1582.591107.910.98270.1937 56.93%3.911.074.44
Ours1582.641106.10 0.9827 0.1957 58.43%3.89 1.09 4.41
Figure 6 shows that the weight of the 8 input features
varies according to different condition. By adjusting the weight
dynamically, the model can adaptively respond to different
conditions in the Bitcoin market. Those factors have roughly
the same weight in most of the cases, however, when the
market experiences high volatility the model will react and
recalibrate weights to make the prediction more accurate.
Fig. 6. Visualized results of the input vector contribution for the forecasting.
G. Ablation Study
We conduct a series of ablation experiments to evaluate the
contribution of each core component in MoFE. The quantita-
tive results are summarized in Table IV.
1) Impact of regularization loss (L reg) - RemovingL reg
leads to a marked decline in DA and Win/Loss Ratio, vali-
dating thatL reg effectively encourages expert specialization.
While metrics such as Sharpe Ratio and ROI exhibit marginal
decreases, the overall enhancement in predictive precision
confirms thatL reg prevents expert collapse and enables the
model to capture diverse market dynamics more accurately.
2) Scaling the number of experts (N) - Varying the expert
count fromN=2 toN=1 orN=4 results in performance
degradation across most metrics. As illustrated in Fig. 7,
increasingNto 4 leads to “expert dilution”, where the gating
weights fluctuate erratically, suggesting that the 32-day look-
back window provides insufficient information to supervise a
high-dimensional expert space, thereby inducing overfitting.
Conversely, a single expert (N=1) fails to simultaneously
resolve high-frequency noise and medium-term trends. The
N=2 configuration achieves the optimal balance by dedicating
specialized capacity to distinct temporal scales.
3) Efficacy of the gating mechanism - To isolate the benefit
of dynamic routing, we replaced the gating network with a
simple averaging operation while retainingL reg. The results
show a significant deterioration in IC, DA, and profitability
metrics. This drop confirms that the gating network is not
merely an aggregator but a critical decision-maker that dynam-
ically prioritizes experts based on shifting market regimes.
4) Sensitivity to convolutional kernel size - The spatial
receptive field of each expert was tested with kernel sizes
of1×1,3×1, and5×1. Reducing the kernel to1×1
severely impairs strategic performance, as the model loses
its ability to extract local temporal correlations. However,
expanding the kernel to5×1also degrades performance,
likely due to the introduction of excessive noise from distant
time steps. A3×1kernel proves to be the “sweet spot” for
capturing meaningful medium-term trends without overfitting
to stochastic fluctuations.
Fig. 7. Visualized results of four experts’ dynamic weights during mixing.
V. CONCLUSION
We introduced MoFE in this work, a novel deep learning
framework that integrates FNOs and MoE to capture the
non-stationary and multi-scale stochasticity of cryptocurrency
markets. By leveraging a dual-domain architecture, MoFE
effectively extracts global spectral trends and local temporal
microstructures, while a dynamic gating mechanism ensures
adaptability to rapid regime shifts.

Our experiments confirm that MoFE achieves SOTA results
forT+ 1andT+ 5horizons, significantly reducing phase lag
and enhancing directional predictive power.
This superior phase-lag mitigation is achieved because
the frequency-domain modeling effectively separates high-
frequency noise from underlying structural market trends.
Empirically, this theoretical advantage translates into robust
performance particularly during high-volatility periods, where
the spectral representation seamlessly isolates structural trends
from transient short-term noise.
In simulated trading, the model yielded exceptional risk-
adjusted returns, demonstrating high practical utility.
Future research will strictly focus on extending the MoFE
framework to other financial time-series forecasting tasks, such
as cross-asset volatility modeling.
REFERENCES
[1] A. J. Hou, W. Wang, C. Y . Chen, and W. K. H ¨ardle, “Pricing cryptocur-
rency options,”Journal of Financial Econometrics, vol. 18, no. 2, pp.
250–279, 2020.
[2] M. Amjad and D. Shah, “Trading bitcoin and online time series
prediction,” inProceedings of Machine Learning Research (PMLR),
2017, pp. 1–15.
[3] S. Wheatley, D. Sornette, T. Huber, and R. N. G. Max Reppen, “Are
bitcoin bubbles predictable? combining a generalized metcalfe’s law and
the lppls model,” 2018, arXiv:1803.05663.
[4] F. N. Zargar and D. Kumar, “Informational inefficiency of bitcoin: A
study based on high-frequency data,”Research in International Business
and Finance, vol. 47, pp. 344–353, 2019.
[5] J. Y .-L. Chan, S. W. Phoong, S. Y . Phoong, W. K. Cheng, and Y .-L.
Chen, “The bitcoin halving cycle volatility dynamics and safe haven-
hedge properties: A msgarch approach,”Mathematics, vol. 11, no. 3, p.
698, 2023.
[6] H. Tian, “Bitcoin price forecasting using arima model,”Theoretical and
Natural Science, pp. 105–112, 2023.
[7] J. Chu, S. Chan, S. Nadarajah, and J. Osterrieder, “Garch modelling of
cryptocurrencies,”Journal of Risk and Financial Management, vol. 10,
no. 4, p. 17, 2017.
[8] P. C. Sekhar, M. Padmaja, B. Sarangi, and Aditya, “Prediction of
cryptocurrency using lstm and xgboost,” in2022 IEEE International
Conference on Blockchain and Distributed Systems Security (ICBDS),
2022, pp. 32–37.
[9] P. L. Seabe, C. R. B. Moutsinga, and E. Pindza, “Forecasting cryptocur-
rency prices using lstm, gru, and bi-directional lstm: a deep learning
approach,”Fractal and Fractional, vol. 7, no. 2, p. 203, 2023.
[10] A. Dutta, S. Kumar, and M. Basu, “A gated recurrent unit approach to
bitcoin price prediction,”Journal of Risk and Financial Management,
vol. 13, p. 23, 2020.
[11] Y . Liu, T. Hu, H. Zhang, H. Wu, S. Wang, L. Ma, and M. Long, “itrans-
former: Inverted transformers are effective for time series forecasting,”
inInternational Conference on Learning Representations, 2024.
[12] M. S. Sepehri, A. Mehradfar, M. Soltanolkotabi, and S. Avestimehr,
“Cryptomamba: Leveraging state space models for accurate bitcoin
price prediction,” inIEEE International Conference on Blockchain and
Cryptocurrency (ICBC) 2025, 2025.
[13] F. Jamhamed, F. Martin, F. Rondeau, J. Th ´elissaint, and S. Tuff ´ery,
“Regime-specific dynamics and informational efficiency in cryptomar-
kets: Evidence from gaussian mixture models,” Economics Working
Paper Archive, Tech. Rep., 2024.
[14] M. Kang, J. Hong, and S. Kim, “Harnessing technical indicators with
deep learning based price forecasting for cryptocurrency trading,”Phys-
ica A: Statistical Mechanics and its Applications, vol. 660, p. 130359,
2025.
[15] A. Peik, M. A. Zare Chahooki, A. Milani Fard, and M. Agha Sarram,
“Adaptive temporal fusion transformers for cryptocurrency price predic-
tion,”arXiv preprint arXiv:2509.10542, 2025.
[16] Z. Li, N. Kovachki, K. Azizzadenesheli, B. Liu, K. Bhattacharya,
A. Stuart, and A. Anandkumar, “Fourier neural operator for parametric
partial differential equations,” inInternational Conference on Learning
Representations, 2021.
[17] J. Guibas, M. Mardani, Z. Li, A. Tao, A. Anandkumar, and B. Catanzaro,
“Adaptive fourier neural operators: Efficient token mixers for transform-
ers,” 2022, arXiv:2111.13587.
[18] T. Chen, H. Zhou, Y . Li, H. Wang, Z. Zhang, T. Zhu, S. Zhang, and J. Li,
“Freqmoe: Dynamic frequency enhancement for neural pde solvers,”
inProceedings of the Thirty-Fourth International Joint Conference on
Artificial Intelligence (IJCAI-25), 2025.
[19] T. O. Kehinde, O. J. Adedokun, A. Joseph, K. M. Kabirat, H. A.
Akano, and O. A. Olanrewaju, “Helformer: an attention-based deep
learning model for cryptocurrency price forecasting,”Journal of Big
Data, vol. 12, p. 81, 2025.
[20] A. Gu and T. Dao, “Mamba: Linear-time sequence modeling with
selective state spaces,”arXiv:2312.00752 [cs.LG], 2023.
[21] D. Song, A. M. C. Baek, and N. Kim, “Forecasting stock market indices
using padding-based fourier transform denoising and time series deep
learning models,”IEEE Access, vol. 9, pp. 83 786 – 83 796, 2021.
[22] R. Yang, L. Cao, X. You, K. Fang, J. Li, and J. Yang, “Fourier
basis mapping: A time-frequency learning framework for time series
forecasting,” 2025, arXiv:2507.09445v1.
[23] C. Remlinger, C. Alasseur, M. Bri `ere, and J. Mikael, “Expert aggregation
for financial forecasting,”The Journal of Finance and Data Science,
vol. 9, p. 100108, 2023.
[24] N. Ronghao, L. Zinan, W. Shuaiqi, and F. Giulia, “Mixture-of-linear-
experts for long-term time series forecasting,” inProceedings of Machine
Learning Research (PMLR), vol. 238, 2024.
[25] X. Shi, S. Wang, Y . Nie, D. Li, Z. Ye, Q. Wen, and M. Jin, “Time-moe:
Billion-scale time series foundation models with mixture of experts,” in
International Conference on Learning Representations, 2025.
[26] R. C. Grinold and R. N. Kahn,Active Portfolio Management: A
Quantitative Approach for Producing Superior Returns and Controlling
Risk. New York: McGraw-Hill, 1999.
[27] F. X. Diebold and J. A. Lopez, “Forecast evaluation and combination,”
inHandbook of Statistics. Elsevier, 1996, vol. 14, pp. 241–268.
[28] M. H. Pesaran and A. Timmermann, “A simple nonparametric test of
predictive performance,”Journal of Business & Economic Statistics,
vol. 10, no. 4, pp. 461–465, 1992.
[29] M. J. Pring,Technical Analysis Explained. McGraw-Hill, 2002.
[30] G. Appel,Technical Analysis: Power Tools for Active Investors. Finan-
cial Times Prentice Hall, 2005.
[31] R. J. Hyndman and A. B. Koehler, “Another look at measures of forecast
accuracy,”International Journal of forecasting, vol. 22, no. 4, pp. 679–
688, 2006.
[32] R. Pardo,The Evaluation and Optimization of Trading Strategies,
2nd ed. John Wiley & Sons, 2008.
[33] W. F. Sharpe, “The sharpe ratio,”Journal of portfolio management,
vol. 21, no. 1, pp. 49–58, 1994.
