---
title: 'EXAONE Finance 1.0: An Attention-free Time Series Foundation Model for Financial Time Series'
url: https://arxiv.org/abs/2609.04239
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Seunghan Lee
- Jaehoon Lee
- Jun Seo
- Tae Yoon Lim
- Dongwan Kang
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.04239
pages: 18
chars: 71355
fetched_at: '2026-11-08T13:29:21+00:00'
kb_version: 1
---

# EXAONE Finance 1.0: An Attention-free Time Series Foundation Model for Financial Time Series

EXAONE Finance 1.0:
An Attention-free Time Series Foundation Model for Financial Time Series
LG AI Research∗
Seunghan Lee, Jaehoon Lee, Jun Seo, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Minjae Kim,
Sungdong Yoo, Junhyeok Kang, Sangjun Han, Soonyoung Lee, Wonbin Ahn
This technical report presentsEXAONE Forecast for Finance(EXAONE Finance), a financial time
series foundation model (TSFM) tailored to financial forecasting. While recent TSFMs achieve
strong zero-shot performance through large-scale pretraining, they are primarily developed for
general-domaintime series and largely rely on self-attention backbones whose computational cost
grows quadratically with sequence length and variate count. Moreover, they assume fully observed
inputs and are pretrained on corpora that fail to adequately capture the unique dynamics of finan-
cial markets. These limitations hinder their applicability to finance, where long, many-channel, in-
termittently observed panels are common. To address these challenges, EXAONE Finance adopts
anattention-freearchitecture, replacing self-attention with two simple yet effective linear-time op-
erators: (1) acausal 1D convolutionfor temporal mixing and (2) agroup-aware pooling multi-layer
perceptron (MLP)for variate mixing. Furthermore, amasked-context augmentationexposes the
model to contiguous missing spans during training, improving robustness to the missingness per-
vasive in financial markets. EXAONE Finance is pretrained on asynthetic financialcorpus whose
generative process is designed to reproduce the properties of financial series such as heavy tails,
volatility clustering, jumps, regime shifts, and cross-asset dependence, combined with a domain-
agnostic synthetic source. On FinVerse, a financial forecasting benchmark covering diverse asset
classes, EXAONE Finance attains state-of-the-art performance, ranking first across all three evalu-
ation tiers: point-forecast accuracy, cross-sectional asset ranking, and portfolio profitability.
Modelhttps://huggingface.co/LG-AI-Research/EXAONE-Finance-1.0
Codehttps://github.com/LGAI-Research/EXAONE-Forecast
1 Introduction
Time series (TS) forecasting underpins decision-making across domains such as finance [28, 32, 43] and energy [23].
To address these forecasting needs, deep learning models, including recurrent [42], convolutional [5, 38], and
transformer-based [40, 52] architectures, capture temporal structure effectively, yet are typically trained for individ-
ual datasets and transfer poorly across domains. To address this limitation, time series foundation models (TSFMs)
pursue generalizable forecasting through large-scale pretraining [3, 11, 18, 20, 29, 31, 48], achieving strong zero-shot
performance across diverse TS benchmarks [1, 19].
Despite their success on general-domain benchmarks,applying TSFMs to financial forecasting remains challenging
due to three gaps.(i) Cost:the self-attention backbones used by most TSFMs incur a cost that grows quadratically with
the sequence length and the number of variates, which is expensive for the long, many-channel panels in finance.(ii)
Missingness:financial series are interrupted by market closures and trading halts, yet most TSFMs assume contiguous
inputs.(iii) Domain mismatch:pretraining corpora are dominated by non-financial domains, under-representing
financial dynamics such as heavy tails and low signal-to-noise.
Broad view of financial assets.Crucially,financial forecastingis far broader than stock-price prediction. Finan-
cial decision-making spans a heterogeneous universe of assets with distinct sampling frequencies, scales, and dy-
namics: equities, exchange-traded funds (ETFs), foreign exchange (FX), commodities, crypto-assets, fixed-income
instruments, and macroeconomic indicators. These asset classes exhibit diverse characteristics, ranging from high-
frequency, heavy-tailed crypto series to low-frequency, smoothly varying macroeconomic indicators, and are often
arXiv:2609.04239v2  [cs.AI]  7 Sep 2026

Table 1:Comparison of TSFMs.EXAONE Finance is the onlyattention-freeconvolutional TSFM and the only
model in this comparison pretrained onfinancial-domain data, which we generate synthetically. (CNN: convolutional
neural network, RNN: recurrent neural network, SSM: state-space model, MLP: multi-layer perceptron)
Models
Architecture Dataset
Temporal mixing Variate mixing Financial
Chronos, Chronos-Bolt, TimesFM, Lag-Llama, TimeGPT, Timer,
MOMENT, Sundial, TEMPO, ROSE, Time-MoE, PatchTST-FM,
Kairos, YingLong, CleanTS, TabPFN-TS, VisionTS
Attention – ×
Chronos-2, Moirai, Moirai-MoE, Toto, UniTS Attention Attention ×
TiRex (xLSTM), TempoPFN, FlowState, Reverso RNN / SSM – ×
TTM (TinyTimeMixer) MLP MLP ×
EXAONE Finance (Ours) CNN MLP (Group pooling) ✓
observed jointly as multi-channel panels (e.g., the open/high/low/close/volume fields of a single security). Afinan-
cial TSFMshould therefore support this spectrum of asset classes, enabling a single model to address the diverse
forecasting needs encountered across financial markets.
Inter-country
T1: Point
Country
T1: Point
Sector
T1: Point
Individual
T1: Point
Inter-country
T2: IC
Country
T2: IC
Sector
T2: IC
Individual
T2: IC
Inter-country
T3: Portf.
Sector
T3: Portf.
Individual
T3: Portf.
25
50
75
100
EXAONE Finance
Chronos-2
Moirai
TimesFM-2.0
T oto-2.0
VisionTS
Figure 1:FinVerse benchmark.EXAONE Finance
outperforms five representative TSFMs.
To this end, we proposeEXAONE Finance, a TSFM tai-
lored to financial forecasting. Unlike general-purpose TSFMs,
EXAONE Finance is designed to address the unique charac-
teristics of financial TS. It adopts an 1)attention-freearchitec-
ture by replacing self-attention with two linear-time operators,
namely a causal 1D convolution for temporal mixing and a
group-aware pooling MLP for variate mixing, and is trained
with a 2)masked-context augmentationthat improves robust-
ness to missing observations. Furthermore, our method is pre-
trained on a 3)synthetic financial corpus, generated so that the
sampled series carry the properties of financial markets such
as heavy tails, volatility clustering, jumps, regime shifts, and
cross-asset dependence. We evaluate it on FinVerse [26], a
standardized financial benchmark that assesses models across
three tiers (point accuracy, cross-sectional skill, and portfo-
lio backtesting) over a broad range of financial assets. Ta-
ble 1 contrasts EXAONE Finance with representative TSFMs
in terms of their mixing architecture and pretraining domain.
The main contributions are as follows:
• We proposeEXAONE Finance, an attention-free TSFM that mixes time withcausal convolutionsand variates with
agroup-aware pooling MLPfor linear-time cost (with a patch-based forecasting head), made robust to missing data
by a masked-context augmentation that masks contiguous spans of the input.
• We pretrain EXAONE Finance on asynthetic financial corpus, using a generator whose sampling process is de-
signed to reproduce the properties of financial series such as heavy tails, volatility clustering, jumps, regime shifts,
and cross-asset dependence. The model therefore sees no real market data during pretraining.
• Through evaluation onFinVerse, a financial benchmark that spans a broad range of asset classes and scores models
on three tiers (point accuracy, cross-sectional skill, and portfolio backtesting), EXAONE Finance attains state-of-
the-art (SoTA) performance across financial forecasting tasks. As shown in Figure 1, it traces a near-maximal
envelope across the scope×tier grid, ranking in the top percentiles for nearly every cell.
2 Related Work
2.1 Time Series Foundation Models
Inspired by the success of large language models, recent work pretrains a single model on large, heterogeneous TS
corpora for zero-shot forecasting. Chronos [3] tokenizes scalar values and reuses a T5 encoder–decoder language-
model backbone, later distilled into the faster Chronos-Bolt and extended to multivariate inputs by Chronos-2 [2].
TimesFM [11] adopts a decoder-only, patch-based transformer, while Moirai [48] uses a masked encoder with any-
2

variate attention to support arbitrary numbers of covariates, and Moirai-MoE [35] sparsifies it with a mixture-of-
experts. Beyond these, the design space broadens through decoder-only autoregressive models [18, 37, 41, 44],
encoder-style representation models [20], further foundation models [6, 9, 17, 36, 46], and even the repurposing
of the vision domain for forecasting [7]. Recently, Toto-2.0 [25] pushes this paradigm into the scaling era with a
family of open models trained at multiple sizes. A common characteristic of most of these models is their reliance
onself-attention, whose computational cost grows quadratically with the sequence length and the number of variates.
EXAONE Finance departs from this paradigm by removing the attention mechanism, while keeping the patch-based,
quantile-decoding interface that these models share. Even the few TSFMs built for finance retain an attention back-
bone. FinCast [53] adopts a channel-independent transformer that models series in isolation, and Delphyne [12] relies
on quadratic any-variate attention, whereas EXAONE Finance mixes grouped variates jointly inlineartime.
2.2 Attention-Free Sequence Models for Time Series
Attention is not the only way to mix information across time. Convolutional sequence models, from the original
Temporal Convolutional Network (TCN) [5] to the more recent ModernTCN [38], use (dilated) causal convolutions
to obtain large receptive fields at linear cost, and have proven competitive with transformers on long-horizon fore-
casting. Purely MLP-based models such as DLinear [50], TSMixer [8], and TiDE [10] show that even simple lin-
ear or token-/channel-mixing layers are strong baselines, and TTM (TinyTimeMixer) [14] carries this idea into the
foundation-model regime with an MLP-Mixer backbone. State-space models, most notably Mamba [22] and its TS
adaptations [27, 47], offer another linear-time alternative with selective recurrence. EXAONE Finance follows this
attention-free lineage: it combines acausal convolutionfor temporal mixing with agroup-aware pooling MLPfor
variate mixing. Unlike most prior attention-free work, trained per-dataset, it is apretrained foundation model.
2.3 Large-scale Pretraining Datasets
Pretraining a TSFM requires large and diverse corpora, drawn from real archives, synthetic generators, or both. On
the real side, the Monash archive [19] aggregates dozens of public datasets, LOTSA [48] scales this to over 27B
observations across nine domains, GIFT-Eval [1] assembles a broad multi-domain corpus, and Time-300B [44] reaches
over 300B time points. On the synthetic side, KernelSynth [3] composes Gaussian-process kernels to synthesize
diverse trend and seasonal patterns, and CauKer [49] augments such kernel compositions with structural causal models
for causally coherent inter-series interactions. In contrast, EXAONE Finance stays synthetic but targets a domain: its
generator is built so that the sampled series reproduce the properties of financial markets (Section 5.1).
3 Problem Definition
Table 2: Notations for TS forecasting.
Symbol Meaning
L Context (Input) length
H Forecast horizon length
C Number of variates in a group
B Batch size (# variate-rows)
P Patch size
d Model hidden dimension
xctx ∈R L Univariate context input
X ctx ∈R C×L Multivariate context input
y∈R H Ground-truth horizon values
m∈{0, 1} L Observation mask
g∈{1, . . . ,G} C Variate group ids
q1, . . . ,qQ Target quantile levels
ˆY∈R Q×H Predicted quantiles
Time series forecasting.Let a single time series bex=
(x1,x 2, . . . )observed at a fixed samplingfrequency(e.g., daily,
weekly, monthly). At a forecast origint, the model is given acontext
windowof the most recentLobservations,x ctx =(x t−L+1 , . . . ,xt )∈
RL, and must predict the nextHvalues, called theforecast horizon,
y=(x t+1 , . . . ,xt+H )∈R H.
Multivariate (grouped) series.Financial assets are fre-
quently observed as aligned multi-channel panels (e.g., the
open/high/low/close/volume fields of one security, or a group of re-
lated assets). We therefore allow agroupofCvariates sharing com-
mon timestamps,X ctx =[x ctx 1 ; . . . ;xctx C ]∈R C×L , with a group-id vec-
torg∈{1, . . . ,G} C indicating which variates may exchange informa-
tion (g i =g j iff variatesi,jbelong to the same group). A univariate
series is the special caseC=1.
Missingness.Financial series contain missing spans (e.g., market closures, trading halts, and unreported periods). We
represent observability with an observation maskm∈{0, 1} L, wherem τ =0marks a missing/padded entry. The model
must handle such missing spans and forecast through them without imputation.
Probabilistic objective.Rather than a single point estimate, we produce a set ofQquantile forecasts. Given target
quantile levelsq 1, . . . ,qQ ∈(0, 1), the modelf θ maps the (masked) context to
ˆY=f θ ¡ X ctx,m,g ¢ ∈R Q×H , ˆyq,h ≈Quantile q (xt+h ) ,(1)
where ˆyq,h estimates theq-th quantile of theh-step-ahead value. Table 2 summarizes the notation.
3

EXAONE Finance: Attention-Free Architecture
Context input
Input Scaler
InstanceNorm(+ arcsinh)
Patch
Embedding
Encoder
Block
Forecasting
Head
Probabilistic forecast
Masked-Context Augmentation
-Maskacontiguousspan
-To learnmissing-spanforecasting
Singleblock:(1) Temporal → (2) Variate → (3) FFN, w/ residual
[Feedforward]
LN → MLP
Output
- Multiplequantile levels
- Inverse-normalized
x N
[Temporal Mixing]
Causal 1DCNN
[Variate Mixing]
Group-Aware Pooling MLP
Attention-Free!
Figure 2:Architecture of EXAONE Finance.The context series is instance-normalized, split into patches, and
embedded, then processed byNattention-freeencoder blocks before a forecasting head produces a probabilistic
forecast. Each encoder block mixes information with two linear-time operators: acausal 1D convolutionfor temporal
mixing and agroup-aware pooling MLPfor variate mixing, followed by a feed-forward network. During training,
amasked-context augmentationmarks a contiguous input span as known-missing, so the model learns to forecast
through the missing spans that occur at inference.
4 EXAONE Finance
4.1 Model Overview
EXAONE Finance is an attention-free TSFM that replaces self-attention with two simple yet effective linear-time
mixers, where each encoder block combines (i) acausal 1D convolutionover the temporal axis (Section 4.3) and (ii)
agroup-aware pooling MLPover the variate axis (Section 4.4), followed by a standard feed-forward network (FFN).
This makes the per-block cost linear in both the sequence lengthLand the number of variatesC. Missing observations
are handled natively using an observation-mask channel that flags missing or padded entries in each patch token
(Section 4.2). Instance normalization (Eq. 3) and the training loss (Section 4.6) ignore these positions, allowing the
model to process and forecast through missing spans without a separate imputation step. The end-to-end pipeline is
summarized as follows:
xctx InstanceNorm− − − − − − − − − →ˆx Patch− − − →PEmbed− − − − →H(0) N×Encoder− − − − − − − − →H(N) Head− − − →ˆY.(2)
We detail the input pipeline (Section 4.2), the two mixing operators (Sections 4.3–4.4), a masked-context training
augmentation (Section 4.5), and the forecasting head (Section 4.6). The overall framework of EXAONE Finance is
illustrated in Figure 2.
4.2 Input Pipeline
Instance normalization.Each context is standardized along the time axis using statistics:
ˆx= xctx −µ σ ,µ=mean(x ctx),σ=std(x ctx),(3)
whereµandσare computed over theobserved(non-missing) entries only and used to restore the predictions to the
original scale. To accommodate the heavy-tailed nature of financial series, an area hyperbolic sine (arcsinh) transform
is then applied to the standardized context:
˜x=arcsinh( ˆx)=log
‡
ˆx+
p
ˆx2 +1
·
.(4)
This transform behaves linearly near zero (arcsinh(u)≈u) and logarithmically in the tails (arcsinh(u)≈
sgn(u) log 2|u|), compressing extreme values while preserving sign. Unlike a log transform, it remains defined for
negative and zero inputs. It reduces to the identity ( ˜x= ˆx) when disabled, and is inverted at inference by ˆx=sinh( ˜x)
before de-standardization.
Patching.The transformed context ˜xis unfolded into non-overlapping patches of sizeP(strideP). When the length
is not a multiple ofP, the sequence is left-padded with missing markers so that the most recent observations remain
patch-aligned. Each patch token concatenates three components,
pτ =
£
eτ ∥ ˜xτ ∥m τ
⁄
∈R 3P ,(5)
4

[Variate Mixing] Group-Aware Pooling MLP
Variates exchange information only within their group Variates (one batch)
Group A
𝑣!:ℎ!  (𝑆×𝑑)
𝑣":ℎ"(𝑆×𝑑)
𝑣#:ℎ#(𝑆×𝑑)
Group B
𝑣$:ℎ$(𝑆×𝑑)
𝑣%:ℎ%(𝑆×𝑑)
Mean pool
(ℎ!	(𝑆	×𝑑)
Mean pool
(ℎ"	(𝑆	×𝑑)
Per-variate Transform  (Examplefor 𝑣!∈Group A )
GELU
ℎ!(self)
Weights shared across all variates & tokens
[ℎ!	||	(ℎ!]
(𝑆	×2𝑑) 2𝑑→𝑑& 𝑑&→𝑑
LinearLinear
Concat
[Temporal Mixing] Causal 1D CNN
Each output sees only current & past inputs
Causal receptive field
padpadℎ! ℎ" ℎ#
ℎ# ’
1×1
ConvLN
Conv1d
→ GELU → Dropout
×	𝑛
Figure 3:The two attention-free mixing operators.Each encoder block mixes information along two axes. [Left]
Temporal mixingapplies a causal 1D convolution, so that each position attends only to current and past inputs. [Right]
Variate mixingis a group-aware pooling MLP, where variates exchange information only within their group, and each
variateh i is concatenated with its group mean ¯hi and passed through a shared MLP with a residual connection.
a time encodinge τ (each position’s index relative to the forecast origin, divided by a fixed scale), the patched values
˜xτ, and an observation maskm τ that marks padded/missing entries. Each token is then embedded into the model
dimension by a residual MLP block: it takes the3P-dimensional token, passes it through a hidden layer of width
dff, and outputs ad-dimensional representation. Stacking the embedded tokens gives the encoder inputH (0) ∈R T×d ,
whereTis the number of patches. An optional learnableregistertoken is then prepended to this sequence.
4.3 Temporal Mixing
Causal convolution block.Self-attention along time is replaced by a stack ofncausal 1D convolutions. Given block
inputH∈R T×d , we layer-normalize, transpose to channel-first, and apply each convolution with a left-only pad of
k−1so that tokenτdepends solely on tokens≤τ(ensuring causality):
U=GELU
¡
Conv1dk (LeftPadk−1 (·))
¢
,(repeatedntimes),(6)
where the first convolution mapsd→cchannels and the rest operate inc. A final1×1convolution restores the model
widthc→d, and a residual connection is added:
H ′ =H+Dropout ¡ Conv1d1×1(U) ¢ .(7)
4.4 Variate Mixing
Group-aware pooling MLP.Information is exchanged across variates onlywithin the same group, so that unrelated
series are never mixed. Letg i denote the group id of variateiand define the group maskΓ i j =1[g i =g j ]. Each variate
is augmented with its group-mean representation,
¯hi =
P
j Γi j h j
P
j Γi j
,h ′ i =h i +Dropout ¡ MLP([h i ∥ ¯hi ]) ¢ ,(8)
where the MLP projects2d→d v →dwith a GELU nonlinearity. Since each variate is mixed only through its group
mean, the output does not depend on the order of variates within a group. When a group contains only a single
variate, no cross-variate information is available, and the operator reduces to a per-variate transformation. After the
two mixers, a standard FFN is applied, that is, layer normalization (LN) followed by a two-layer MLP with hidden
dimensiond ff, with a residual connection. Both mixers are shown in Figure 3.
4.5 Masked-Context Augmentation
Robustness to missingness.Financial series are routinely interrupted by market closures, trading halts, and unreported
periods. To make the encoder robust to such missing spans, during training we randomly mark a single contiguous
span of each context asmissingbefore normalization,
˜xτ =
(
missing,τ∈[s,s+w)
xτ,otherwise, w∼U{1, . . . ,ρL},(9)
5

with masking fractionρ=0.25and a uniformly sampled starts. Since the normalization statistics, the observation
mask, and the loss all treat missing entries consistently as “known-missing,” the model learns to forecast through
missing spans. Note that the augmentation is appliedonly at training time.
Comparison with masking in prior works.Most existing masking schemes in TS are reconstruction objec-
tives [13, 30, 51], in which the masked span is itself theprediction target, i.e., masking is applied to theoutputto
be reconstructed. In contrast, our augmentation masks part of theinputrather than the target: the masked span is
marked known-missing and excluded from the loss, so that the model becomes robust to the missing observations it
encounters at inference, which are common in financial markets (e.g., market closures and trading halts).
4.6 Forecasting Head
Quantile decoding.AfterNencoder blocks and a final LN, the last⌈H/P⌉tokens are decoded by the forecasting
head (a residual MLP) intoQ·Poutputs and rearranged into quantile trajectories ˆY∈R Q×H , which are mapped back
to the original scale by inverting Eq. 3. We predict a set ofQquantile levels and train with the pinball (quantile) loss,
evaluated only at finite target positions via a maskm y:
L= 1 |my | X q X h m y h max ¡ q(y h − ˆyq,h ), (q−1)(y h − ˆyq,h ) ¢ .(10)
Masking the loss lets multivariate groups feed all channels asinputswhile scoring only the designated target chan-
nel(s), matching the evaluation protocol.
4.7 Configuration, Inference, and Complexity
Table 3: Architecture configuration.
Hyperparameter Value
Encoder
Hidden dimension (d) 1024
Feed-forward dimension (dff) 4096
Number of blocks (N) 12
Dropout 0.1
Encoder block
Temporal CNN
Channels (c) 512
Kernel size (k) 7
Conv layers (n) 2
Variate MLP
Hidden dimension (dv) 512
Max groups (G) 16
Patch & head
Patch size (P) 16
Max input length (L) 512
Quantile levels (Q) 21
Model configuration.Table 3 summarizes the hyperparameters
of the released model. The encoder stacksN=12blocks of width
d=1024, each pairing a temporal CNN (c=512channels, kernel
k=7,n=2layers) with a group-aware variate MLP (hidden size
dv =512, up toG=16groups). The forecasting head reads out
patches of sizeP=16asQ=21quantile levels.
Single forward pass.At inference, EXAONE Finance decodes
the entire horizon inoneforward pass rather than autoregressively.
For a requested horizonH, the model appends⌈H/P⌉future to-
kens to the context, runs theNencoder blocks once, and reads
out allQquantiles for every horizon step simultaneously (Sec-
tion 4.6). No step-by-step roll-out and no key/value cache are
needed, as there is no attention to cache. Arbitrary horizons are
supported by varying the number of output tokens, and the predic-
tion is mapped back to the original scale by inverting Eq. 3. Miss-
ing or padded entries in the context are handled by the same ob-
servation mask used in training, so no special preprocessing (e.g.,
imputation) is required at inference. This scheme is identical dur-
ing pretraining: the⌈H/P⌉future tokens are all appended up front
and predicted jointly in a single pass.
Computational complexity.Both mixers are linear in their respective axes. A causal convolution block costs
O(L d c k)for sequence lengthL, and the group-aware pooling MLP costsO(C d)forCvariates: each group mean
is computed once by averaging within each group (written with a group mask in Eq. 8 only for clarity), not by a
pairwise interaction. This contrasts with theO(L 2d)time-axis attention andO(C 2d)variate-axis attention in TSFMs
that adopt self-attention, making EXAONE Finance linear in both the sequence length and the number of variates.
5 Experiments
We evaluate EXAONE Finance onFinVerse, a standardized, unified benchmark covering a broad range of financial
assets. We first describe the pretraining dataset (Section 5.1) and the evaluation protocol, namely the three scoring
tiers and their metrics (Section 5.2), then the baselines and aggregation (Section 5.3), the main results (Section 5.4),
and an analysis of performance broken down by asset scope (Section 5.5).
6

Table 4:Financial time series properties and their generating mechanisms.Each property is induced by an explicit
component of the sampling process. Properties are switched on independently with sampled intensities.
Family Property Generating mechanism
Temporal
dependence
Trend Deterministic drift plus a random-walk drift component
Seasonality / cyclicality Fourier components at calendar periods
Autocorrelation ARMA innovations
Mean reversion Ornstein–Uhlenbeck component
Momentum Positive short-horizon dependence in the drift
Long-range dependence Fractional Gaussian noise with sampled Hurst exponent
Multi-scale dynamics Superposition of components at several time scales
Conditional
variance
V olatility Sampled base volatility level
V olatility clustering GARCH-type conditional variance
Heteroskedasticity Time-varying variance schedules
Marginal
distribution
Fat tails Student-tinnovations with sampled degrees of freedom
Skewness Skewed innovations and a leverage effect
Non-normality Mixture-of-normals innovation distribution
Discontinuity
and regimes
Jump / discontinuity Compound-Poisson jump component
Shock / extreme event Rare large-amplitude shocks with decaying response
Regime switching Markov-switching parameters
Structural break Change-points in the parameter path
Cross-series
structure
Cross-asset correlation Common factors with sampled loadings
Time-varying correlation Dynamic conditional correlation of the factors
Lead–lag relationship Lagged factor loadings across channels
Cointegration Shared stochastic trend with a stationary spread
Observation Liquidity / activity Intermittent observation and activity-driven volume proxies
5.1 Pretraining Dataset
Data mixture.We pretrain EXAONE Finance on a synthetic corpus designed around the nature of financial data. It
combines a domain-agnostic source, KernelSynth [3], with asynthetic financialsource whose sampling process we
design so that the generated series carry the statistical regularities of financial markets. EXAONE Finance therefore
seesno real market data at any point during pretraining, yet transfers to real assets at evaluation.
Synthetic financial datasets.Table 4 lists the properties we ask the generator to reproduce, grouped into six families,
together with the mechanism that induces each. We sample a series as a superposition of these components: a trend and
cyclical part sets the low-frequency shape, an ARMA / Ornstein–Uhlenbeck part sets the short-horizon dependence,
a stochastic-volatility part with heavy-tailed, skewed innovations sets the conditional distribution, a jump and regime
part introduces discontinuities and parameter changes, and a factor part ties channels together so that a group shares
common shocks with lead–lag and cointegration structure. We switch every property on with a randomly sampled
intensity. The corpus therefore spans series close to Gaussian random walks as well as series dominated by clustered
volatility and abrupt regime changes. Figure 4 shows a representative property of each family as it appears in a sampled
series, next to the reference behaviour that the corresponding component departs from.
Table 5: Frequency-aware windows.
Frequency L H
Daily 260 {5, 20, 65, 130, 260}
Weekly 52 {1, 4, 12, 26, 52}
Monthly 12 {1, 3, 6, 12, 24}
Quarterly 4 {1, 2, 4, 8}
Annual 10 {1, 2, 5, 10}
Frequency-aware windowing.Synthetic financial series are gener-
ated at the frequencies of Table 5 and windowed with the geom-
etry listed there, which is the same geometry used at evaluation.
KernelSynth series carry no frequency, so they instead use a vari-
able context length up toLand a horizon sampled uniformly up to
Hmax, broadening the pretraining distribution. In this run every se-
ries is treated as an individual channel. The group-aware mixer (Sec-
tion 4.4) natively supports richer cross-series grouping through the
data pipeline, such as the OHLCV fields of a single security.
7

0 100 200 300 400 500 600
0
10
20
30
TEMPORAL DEPENDENCE
Trend · Seasonality
Trend + seasonality
Drift component only
0 100 200 300 400 500 600
−10
0
10
20
30
TEMPORAL DEPENDENCE
Mean reversion · Momentum
Mean reversion (OU)
Momentum drift
0 100 200 300 400 500 600
−20
−15
−10
−5
0
5
10
TEMPORAL DEPENDENCE
Long-range dependence
Multi-scale superposition
Short-memory AR(1), offset
0 100 200 300 400 500 600
−20
−10
0
10
20
CONDITIONAL VARIANCE
Volatility clustering
Returns rt
±2√ ht  conditional band
0 100 200 300 400 500 600
−10
−5
0
5
MARGINAL DISTRIBUTION
Fat tails · Skewness
Beyond ±3σ: 10 events (7 negative)
Gaussian expectation: 1.6
Standardized returns
Gaussian ±3σ
0 100 200 300 400 500 600
0
5
10
15
20
Rare extreme event
DISCONTINUITY AND REGIMES
Jump · Shock
Price path
Jump arrival
0 100 200 300 400 500 600
−30
−20
−10
0
10
DISCONTINUITY AND REGIMES
Regime switching · Break
Structural break
Price path
Turbulent state
0 100 200 300 400 500 600
−40
−30
−20
−10
0
10
CROSS-SERIES STRUCTURE
Lead–lag · Cointegration
Lag 25
Leading channel
Lagged channel
0 100 200 300 400 500 600
35
40
45
50
55
OBSERVATION
Liquidity / activity
Observed price
Activity proxy
Unobserved span
Figure 4:Properties of the synthetic pretraining corpus.Each panel simulates one property of Table 4 with the
generator component that induces it. The purple curve is the series that shows the property. The black curve, band, or
markers are there for comparison, and what they mean changes from panel to panel, so each panel has its own legend.
5.2 Evaluation Protocol: Tiers and Metrics
Why finance-specific metrics?Standard forecasting metrics such as the mean absolute error (MAE) measure average
pointwise error and are scale-dependent. On a heterogeneous financial panel, a few high-variance series dominate
the average error and reward predicting the raw level rather than the actionable signal. Financial decisions, however,
hinge on different quantities: thedirectionof the next move, therelative orderingof assets at a given time, and the
risk-adjusted returnof a strategy built on the forecasts. FinVerse is therefore designed around these finance-specific
desiderata and organizes evaluation into three tiers. Tier 1 uses scale-free, change-based accuracy. Tier 2 measures
cross-sectional skill. Tier 3 measures realized economic value through a portfolio backtest.
Change-based targets.Tiers 1–2 are computed on a grid of achange period(how far back the change is measured)
and aforecast position(how far ahead of the origin it is evaluated). For an origint, denoting the change period byp
8

Table 6:Tier metrics.This table lists the metrics used by the three benchmark tiers.
Tier Metric Meaning
Tier 1
Point accuracy
MASE↓ Mean absolute error scaled by an in-context naïve forecast
HR / HR′ / HR′′ ↑ Directional accuracy (Sign of change, stricter variants)
MASE (Diff / raw)↓ Differenced and raw-value MASE variants
Tier 2
Cross-sectional IC IC↑ Cross-sectional Spearman correlation of predicted vs. realized change
Tier 3
Portfolio backtest
Return↑ Annualized return of the top-K%long portfolio
Sharpe↑ Annualized return divided by volatility
V olatility↓ Annualized volatility of the strategy
MDD↑ Maximum peak-to-trough loss (Closer to 0 is better)
and the forecast position byh, thepredictedandrealizedchanges are
∆pred = ˆy t+h
xt−p
−1,∆ act = xt+h
xt−p
−1,(11)
wherexdenotes the ground-truth series, so the base valuex t−p is measured a periodpbefore the origin and both
changes run to the same future pointt+h. These changes underlie all three tiers.
The three tiers, whose metrics are summarized in Table 6, are defined as follows.
•Tier 1 (Point accuracy).Per series, we report (i)MASE, the mean absolute error scaled by an in-context naïve
forecast, in both a relative-change and an absolute-difference variant, plus a raw all-position variant, and (ii) thehit
rate (HR), the directional accuracyHR=mean
£
sign(∆pred)=sign(∆ act) ⁄ , together with stricter variantsHR ′/HR′′
that additionally require the sign of the first/second difference to match.
•Tier 2 (Cross-sectional Information Coefficient, IC).For each origint, we rank assets within a subgroup by
predicted change and compute the Spearman rank correlation against the realized change,
IC(t)=SpearmanCorr
¡
{∆pred s (t)} s , {∆act s (t)} s ¢ , IC=mean t IC(t).(12)
IC measures whether a model correctly orders assets cross-sectionally, which is the quantity that matters for
relative-value strategies.
•Tier 3 (Portfolio backtest).We form a top-K%, equal-weight, long-only portfolio by selecting the assets with the
highest predicted change, rebalanced at horizonh, in a multi-start overlapping backtest. We report the annualized
Return,Sharperatio,Volatility, andMaximum Drawdown (MDD). This tier turns forecasts into an executable
strategy and scores the economic value of the predictions.
Overall ranking.We rank modelsper cell: for every (tier, spec, metric) triple, allMmodels are ranked from1(best)
toM. We aggregate these ranks with thegeometric meanrather than the arithmetic mean because it is scale-free and
rewardsconsistentperformance across heterogeneous cells, since a single very poor rank is penalized proportionally
rather than absolutely. A model’s score on a tier is
¯r=
‡ Q
c rc
·1/|C|
=exp
‡
1
|C|
P
c lnr c
·
,(13)
wherer c is the model’s rank on cellcandCis that tier’s set of cells. The headlinerank-sumis the sum of the three
per-tier placements (lower is better).
5.3 Baselines and Aggregation
We compare against43 baselinescovering the major public TSFM families, including Chronos [3] / Chronos-
Bolt / Chronos-2 [2], Moirai (1.1, 2.0) [48], TimesFM (1.0/2.0/2.5) [11], Toto [9] / Toto-2.0 [25], TiRex (1.1,
2) [4], TTM [14], PatchTST-FM [40], FlowState [21], Timer [37], Sundial [36], Kairos [15], YingLong [45], Re-
verso [16], TempoPFN [39], VisionTS [7], CleanTS, PatchFM, Super-Linear, and T0-Alpha. These span univariate and
multivariate-native APIs. Each model is scored on the same windows and ranked with the per-cell geometric-mean-
rank procedure of Section 5.2 (Eq. 13). EXAONE Finance (Section 5.1) is thus evaluated against the baseline pool
as a comparison set of 44 models. EXAONE Finance outputsQ=21quantile levels{0.01, 0.05, 0.1, . . . , 0.9, 0.95, 0.99},
and all tier metrics are computed on the median forecast (q50).
9

Table 7:Main benchmark results on FinVerse.Each tier gives the model’s placement (#) and itsAvg. Rank(The
geometric mean of per-cell ranks, lower is better).Rank Sumis the sum of the three placements, and the 44 models
are ordered from the lowest rank sum to the highest. EXAONE Finance is #1 in all three tiers, for a rank sum of 3.
# Model
Tier 1 Tier 2 Tier 3
Rank Sum
# Avg. Rank # Avg. Rank # Avg. Rank
1 EXAONE Finance 1 6.53 1 7.45 1 7.43 3
2 Chronos-2 (Synthetic) 9 11.68 3 8.74 2 9.90 14
3 Reverso (Small) 6 9.60 2 8.64 6 13.04 14
4 TiRex-1.1 2 6.98 4 9.71 14 15.76 20
5 Chronos-2 8 10.14 13 16.12 9 15.17 30
6 TimesFM-2.5-200M 7 9.96 5 10.66 20 17.10 32
7 Chronos-Bolt (Base) 11 12.88 15 16.48 7 14.54 33
8 Chronos-Bolt (Small) 12 12.94 12 15.85 16 16.10 40
9 T0-Alpha 13 13.47 25 18.73 3 11.11 41
10 TiRex-2 (Pretrain) 3 7.48 6 11.56 34 20.12 43
11 TiRex-2 (Zero-shot) 4 8.37 7 11.67 33 20.06 44
12 Toto-2.0-2.5B 18 15.74 17 16.78 10 15.19 45
13 VisionTS 10 12.05 8 13.00 29 19.31 47
14 PatchFM 5 9.08 14 16.15 30 19.56 49
15 Toto-2.0-4M 15 14.44 24 18.21 13 15.66 52
16 TimesFM-2.0-500M 39 29.32 10 14.38 4 11.12 53
17 TempoPFN 14 14.11 18 16.95 27 18.76 59
18 Kairos-50M 20 16.04 29 20.21 11 15.26 60
19 Toto-2.0-1B 16 15.00 23 17.96 22 17.74 61
20 FlowState (Granite R1) 21 17.00 27 19.12 15 16.09 63
21 TimesFM-1.0-200M 22 17.06 16 16.58 26 18.55 64
22 Super-Linear 24 18.11 11 15.15 31 19.58 66
23 Toto-2.0-22M 19 15.90 26 18.97 21 17.30 66
24 Kairos-10M 28 20.85 28 19.80 12 15.61 68
25 FlowState 23 17.49 30 20.22 17 16.34 70
26 Toto-2.0-313M 17 15.34 31 20.55 23 17.96 71
27 Timer-S1 25 18.45 9 13.50 39 22.81 73
28 Moirai-1.1-R (Large) 38 27.84 35 22.17 5 13.00 78
29 Toto-Open-Base-1.0 27 19.94 33 21.36 19 17.07 79
30 Moirai-1.1-R (Base) 37 27.45 38 24.21 8 14.57 83
31 Moirai-1.1-R (Small) 33 25.62 32 21.15 18 16.87 83
32 PatchTST-FM-R1 34 26.30 22 17.92 28 19.03 84
33 Sundial-Base-128M 26 19.73 20 17.66 41 23.48 87
34 PatchTST-FM (Granite R1) 40 29.35 19 17.34 32 20.05 91
35 Kairos-23M 29 21.69 40 24.41 24 18.35 93
36 TTM-R3 35 27.10 21 17.73 43 24.22 99
37 Moirai-2.0-R (Small) 31 23.87 34 21.91 36 21.39 101
38 TTM-R1 32 24.77 44 27.22 25 18.50 101
39 CleanTS-65M 36 27.13 36 22.70 35 21.19 107
40 TTM-R2 30 22.19 43 27.05 44 25.18 117
41 YingLong-50M 42 35.16 37 24.16 38 22.50 117
42 YingLong-300M 44 35.46 39 24.29 37 21.84 120
43 YingLong-110M 43 35.39 41 24.47 40 23.23 124
44 YingLong-6M 41 34.84 42 24.87 42 23.70 125
5.4 Main Results
Overall performance.Table 7 and Figure 5 present the headline result:EXAONE Finance ranks #1 in all three
tiers, for a perfect rank-sum of 3, while the best baseline reaches only 14. The margin holds across very different
objectives, namely point accuracy (Tier 1), cross-sectional ordering (Tier 2), and realized portfolio performance (Tier
3), indicating that the gains are not an artifact of any single metric. Notably, no single baseline is consistently strong
across tiers. For example, TiRex [4] is strong on Tier 1 but drops on Tier 3, whereas EXAONE Finance leads every
tier simultaneously. The two closest baselines, Chronos-2 (Synthetic) and Reverso (Small), never lead a tier.
10

0 5 10 15
Avg. Rank
EXAONE Finance
TiRex
TiRex-2-pre
TiRex-2-zs
PatchFM
Reverso
TimesFM-2.5
Chronos-2
Chronos-2 (Syn)
VisionTS
Chronos-Bolt
Chronos-Bolt-S
6.5
7.0
7.5
8.4
9.1
9.6
10.0
10.1
11.7
12.0
12.9
12.9
Tier 1 (Point accuracy)
0 5 10 15
Avg. Rank
EXAONE Finance
Reverso
Chronos-2 (Syn)
TiRex
TimesFM-2.5
TiRex-2-pre
TiRex-2-zs
VisionTS
Timer-S1
TimesFM-2.0
Super-Linear
Chronos-Bolt-S
7.5
8.6
8.7
9.7
10.7
11.6
11.7
13.0
13.5
14.4
15.1
15.9
Tier 2 (Cross-sectional IC)
0 5 10 15
Avg. Rank
EXAONE Finance
Chronos-2 (Syn)
T0-Alpha
TimesFM-2.0
Moirai-1.1L
Reverso
Chronos-Bolt
Moirai-1.1B
Chronos-2
T oto-2.0-2.5B
Kairos-50M
Kairos-10M
7.4
9.9
11.1
11.1
13.0
13.0
14.5
14.6
15.2
15.2
15.3
15.6
Tier 3 (Portfolio backtest)
Figure 5:Per-tier ranking.Each panel ranks the twelve best models of one tier by their aggregate rank (The geometric
mean of per-cell ranks). EXAONE Finance attains the lowest aggregate rank in all three tiers.
101 102 103
Model size (Parameters, millions; log scale)
20
30
40
50
60
70
80 Sum of the three per-tier Avg. Ranks
Performance vs. Model Size
T oto-2.0
YingLong
Kairos
Moirai
TimesFM
Chronos
EXAONE Finance
Others
EXAONE Finance
TimesFM-1.0
TimesFM-2.0
TimesFM-2.5
T oto-2.0-4M
T oto-2.0-22M T oto-2.0-313M
T oto-2.0-1B
T oto-2.0-2.5B
Moirai-S
Moirai-B
Moirai-L
Kairos-10M
Kairos-23M
Kairos-50M
YingLong-6M
YingLong-50M
YingLong-110M
YingLong-300M
Sundial
Chronos-Bolt
CleanTS
TiRex
Chronos-2
Chronos-2 (Synth)
Figure 6:Performance vs. model size.Each point is a model, with parameter count on thex-axis (Log scale) and, on
they-axis, the sum of its three per-tier Avg. Ranks. Lower values are better, and the axis is inverted so that higher is
better. EXAONE Finance attains the best aggregate rank at a modest size.
Performance vs. model size.Figure 6 plots each model’s aggregate rank against its parameter count, where the ag-
gregate is the sum of the model’s three per-tier Avg. Ranks from Table 7. EXAONE Finance sits on the Pareto frontier:
at only202M parameters it attains the best overall rank, outperforming models more than an order of magnitude larger
(e.g., the billion-scale Toto-2.0 [25] variants), which is consistent with its linear-time, attention-free design. The same
trend appears across the other families in the figure, where a larger model size does not reliably improve the rank,
suggesting that the scaling law common in general-domain forecasting does not yet hold in finance.
11

EXAONE Finance
Chronos-2 (Syn)
Reverso
TiRex
Chronos-2
TimesFM-2.5
Chronos-Bolt
Chronos-Bolt-S
T0-Alpha
TiRex-2-pre
TiRex-2-zs
T oto-2.0-2.5B
VisionTS
PatchFM
T oto-2.0-4M
TimesFM-2.0
T empoPFN
Kairos-50M
T oto-2.0-1B
FlowState-Gr
TimesFM-1.0
T oto-2.0-22M
Super-Linear
Kairos-10M
FlowState
T oto-2.0-313M
Timer-S1
Moirai-1.1L
T oto-Open
Moirai-1.1S
Moirai-1.1B
PatchTST-FM
Sundial-128M
PatchTST-Gr
Kairos-23M
TTM-R3
Moirai-2.0S
TTM-R1
CleanTS-65M
TTM-R2
YingLong-50M
YingLong-300M
YingLong-110M
YingLong-6M
EXAONE Finance
Chronos-2 (Syn)
Reverso
TiRex
Chronos-2
TimesFM-2.5
Chronos-Bolt
Chronos-Bolt-S
T0-Alpha
TiRex-2-pre
TiRex-2-zs
T oto-2.0-2.5B
VisionTS
PatchFM
T oto-2.0-4M
TimesFM-2.0
T empoPFN
Kairos-50M
T oto-2.0-1B
FlowState-Gr
TimesFM-1.0
T oto-2.0-22M
Super-Linear
Kairos-10M
FlowState
T oto-2.0-313M
Timer-S1
Moirai-1.1L
T oto-Open
Moirai-1.1S
Moirai-1.1B
PatchTST-FM
Sundial-128M
PatchTST-Gr
Kairos-23M
TTM-R3
Moirai-2.0S
TTM-R1
CleanTS-65M
TTM-R2
YingLong-50M
YingLong-300M
YingLong-110M
YingLong-6M
.66 .60 .51 .61 .60 .69 .69 .68 .51 .52 .75 .65 .58 .74 .86 .76 .80 .75 .77 .75 .75 .74 .83 .77 .75 .77 .85 .79 .81 .85 .84 .77 .86 .88 .83 .82 .81 .84 .80 .90 .90 .90 .89
.34 .46 .31 .43 .42 .52 .52 .54 .36 .38 .61 .52 .39 .59 .84 .66 .71 .59 .65 .63 .62 .68 .79 .65 .61 .74 .86 .76 .83 .87 .85 .74 .88 .79 .86 .81 .79 .87 .80 .91 .91 .91 .91
.40 .54 .42 .49 .53 .58 .58 .59 .45 .47 .64 .59 .49 .62 .86 .68 .71 .63 .71 .68 .66 .69 .80 .71 .66 .75 .85 .81 .84 .87 .85 .72 .87 .80 .85 .82 .82 .86 .80 .90 .89 .90 .89
.49 .69 .58 .66 .62 .70 .69 .74 .54 .55 .73 .70 .60 .72 .87 .70 .75 .73 .78 .81 .76 .79 .80 .79 .74 .83 .87 .82 .87 .89 .89 .84 .90 .83 .88 .84 .84 .89 .81 .92 .92 .92 .92
.39 .57 .51 .34 .48 .62 .63 .61 .39 .40 .67 .59 .43 .63 .83 .66 .70 .63 .72 .73 .65 .72 .75 .74 .66 .78 .82 .78 .82 .84 .84 .79 .87 .79 .83 .80 .79 .86 .77 .89 .89 .89 .89
.40 .58 .47 .38 .52 .60 .61 .63 .43 .45 .62 .61 .45 .59 .87 .65 .71 .60 .68 .76 .64 .75 .78 .70 .62 .83 .88 .79 .87 .88 .87 .84 .90 .79 .87 .85 .82 .89 .79 .91 .91 .92 .91
.31 .48 .42 .30 .38 .40 .56 .55 .31 .32 .57 .50 .36 .55 .84 .59 .66 .58 .67 .67 .58 .70 .73 .65 .57 .73 .82 .74 .81 .83 .81 .75 .84 .76 .83 .79 .77 .84 .75 .89 .89 .89 .88
.31 .48 .42 .31 .37 .39 .44 .53 .31 .32 .58 .47 .37 .52 .82 .59 .64 .58 .63 .66 .57 .69 .71 .62 .57 .71 .83 .72 .80 .83 .79 .73 .84 .75 .82 .79 .76 .83 .75 .89 .89 .89 .89
.32 .46 .41 .26 .39 .37 .45 .47 .26 .27 .60 .46 .36 .53 .76 .56 .59 .57 .59 .60 .57 .61 .68 .57 .57 .65 .81 .67 .76 .78 .76 .68 .80 .69 .79 .77 .75 .80 .70 .87 .87 .87 .87
.49 .64 .55 .46 .61 .57 .69 .69 .74 .61 .69 .69 .56 .68 .85 .67 .71 .67 .75 .79 .69 .80 .76 .76 .68 .83 .87 .80 .85 .87 .87 .84 .89 .81 .86 .84 .83 .88 .79 .90 .91 .91 .91
.48 .62 .53 .45 .60 .55 .68 .68 .73 .39 .67 .67 .53 .65 .86 .66 .70 .65 .75 .78 .66 .81 .76 .76 .66 .83 .87 .79 .85 .87 .86 .83 .88 .80 .87 .85 .83 .88 .79 .91 .91 .91 .91
.25 .39 .36 .27 .33 .38 .43 .42 .40 .31 .33 .43 .31 .40 .75 .52 .53 .44 .55 .49 .49 .54 .70 .56 .48 .56 .72 .62 .70 .73 .73 .57 .78 .66 .73 .69 .71 .74 .68 .84 .85 .84 .84
.35 .48 .41 .30 .41 .39 .50 .53 .54 .31 .33 .57 .36 .51 .81 .58 .60 .55 .60 .63 .55 .70 .69 .59 .55 .69 .79 .69 .78 .80 .82 .72 .86 .72 .82 .74 .77 .84 .76 .89 .89 .89 .89
.42 .61 .51 .40 .57 .55 .64 .63 .64 .44 .47 .69 .64 .67 .82 .67 .71 .66 .72 .73 .69 .72 .78 .74 .69 .75 .83 .80 .80 .84 .83 .75 .84 .80 .81 .82 .80 .83 .77 .88 .88 .88 .88
.26 .41 .38 .28 .37 .41 .45 .48 .47 .32 .35 .60 .49 .33 .79 .57 .61 .60 .61 .60 .62 .62 .74 .63 .59 .65 .76 .69 .75 .77 .78 .65 .81 .74 .78 .74 .76 .79 .73 .86 .86 .86 .86
.14 .16 .14 .13 .17 .13 .16 .18 .24 .15 .14 .25 .19 .18 .21 .24 .23 .24 .24 .20 .23 .21 .29 .24 .25 .24 .43 .25 .34 .40 .40 .26 .43 .29 .43 .34 .56 .38 .50 .74 .74 .75 .74
.24 .34 .32 .30 .34 .35 .41 .41 .44 .33 .34 .48 .42 .33 .43 .76 .50 .47 .54 .48 .49 .54 .71 .54 .48 .53 .75 .59 .73 .75 .77 .54 .80 .67 .75 .69 .73 .77 .71 .86 .86 .86 .86
.20 .29 .29 .25 .30 .29 .34 .36 .41 .29 .30 .47 .40 .29 .39 .77 .50 .47 .51 .45 .46 .50 .76 .51 .45 .51 .73 .59 .72 .75 .76 .51 .79 .73 .73 .69 .74 .76 .70 .86 .86 .86 .86
.25 .41 .37 .27 .37 .40 .42 .42 .43 .33 .35 .56 .45 .34 .40 .76 .53 .53 .57 .50 .51 .55 .70 .57 .51 .57 .72 .61 .70 .72 .73 .58 .78 .68 .73 .69 .71 .74 .69 .84 .84 .84 .84
.23 .35 .29 .22 .28 .32 .33 .37 .41 .25 .25 .45 .40 .28 .39 .76 .46 .49 .43 .51 .44 .55 .63 .50 .42 .57 .70 .57 .68 .71 .71 .58 .75 .64 .73 .65 .68 .72 .66 .83 .83 .83 .82
.25 .37 .32 .19 .27 .24 .33 .34 .40 .21 .22 .51 .37 .27 .40 .80 .52 .55 .50 .49 .48 .58 .66 .47 .49 .66 .81 .60 .76 .80 .80 .70 .85 .68 .82 .72 .76 .84 .72 .89 .90 .90 .90
.25 .38 .34 .24 .35 .36 .42 .43 .43 .31 .34 .51 .45 .31 .38 .77 .51 .54 .49 .56 .52 .55 .70 .58 .46 .57 .72 .63 .71 .72 .75 .58 .78 .69 .74 .70 .72 .75 .70 .85 .85 .85 .85
.26 .32 .31 .21 .28 .25 .30 .31 .39 .20 .19 .46 .30 .28 .38 .79 .46 .50 .45 .45 .42 .45 .63 .44 .44 .51 .76 .57 .72 .76 .73 .54 .78 .63 .76 .67 .73 .77 .70 .84 .84 .85 .84
.17 .21 .20 .20 .25 .22 .27 .29 .32 .24 .24 .30 .31 .22 .26 .71 .29 .24 .30 .37 .34 .30 .37 .37 .29 .38 .64 .45 .63 .64 .66 .39 .70 .44 .68 .58 .68 .64 .65 .80 .80 .80 .80
.23 .35 .29 .21 .26 .30 .35 .38 .43 .24 .24 .44 .41 .26 .37 .76 .46 .49 .43 .50 .53 .42 .56 .63 .41 .58 .71 .58 .70 .72 .72 .60 .77 .63 .73 .66 .68 .74 .67 .84 .84 .84 .83
.25 .39 .34 .26 .34 .38 .43 .43 .43 .32 .34 .52 .45 .31 .41 .75 .52 .55 .49 .58 .51 .54 .56 .71 .59 .58 .71 .61 .70 .73 .74 .58 .78 .68 .73 .69 .71 .75 .68 .84 .84 .84 .84
.23 .26 .25 .17 .22 .17 .27 .29 .35 .17 .17 .44 .31 .25 .35 .76 .47 .49 .43 .43 .34 .43 .49 .62 .42 .42 .80 .57 .75 .79 .78 .63 .84 .60 .78 .69 .75 .84 .69 .88 .88 .89 .89
.15 .14 .15 .13 .18 .12 .18 .17 .19 .13 .13 .28 .21 .17 .24 .57 .25 .27 .28 .30 .19 .28 .24 .36 .29 .29 .20 .24 .34 .46 .46 .22 .52 .34 .54 .37 .62 .40 .54 .80 .80 .80 .80
.21 .24 .19 .18 .22 .21 .26 .28 .33 .20 .21 .38 .31 .20 .31 .75 .41 .41 .39 .43 .40 .37 .43 .55 .42 .39 .43 .76 .71 .76 .73 .46 .78 .54 .76 .65 .69 .72 .64 .83 .83 .83 .83
.19 .17 .16 .13 .18 .13 .19 .20 .24 .15 .15 .30 .22 .20 .25 .66 .27 .28 .30 .32 .24 .29 .28 .37 .30 .30 .25 .66 .29 .55 .54 .28 .64 .35 .65 .41 .65 .51 .59 .83 .83 .82 .82
.15 .13 .13 .11 .16 .12 .17 .17 .22 .13 .13 .27 .20 .16 .23 .60 .25 .25 .28 .29 .20 .28 .24 .36 .28 .27 .21 .54 .24 .45 .50 .25 .62 .33 .62 .39 .62 .44 .56 .78 .78 .78 .78
.16 .15 .15 .11 .16 .13 .19 .21 .24 .13 .14 .27 .18 .17 .22 .60 .23 .24 .27 .29 .20 .25 .27 .34 .28 .26 .22 .54 .27 .46 .50 .25 .66 .30 .51 .40 .56 .44 .53 .83 .83 .84 .83
.23 .26 .28 .16 .21 .16 .25 .27 .32 .16 .17 .43 .28 .25 .35 .74 .46 .49 .42 .42 .30 .42 .46 .61 .40 .42 .37 .78 .54 .72 .75 .75 .80 .59 .78 .66 .72 .81 .67 .86 .87 .87 .86
.14 .12 .13 .10 .13 .10 .16 .16 .20 .11 .12 .22 .14 .16 .19 .57 .20 .21 .22 .25 .15 .22 .22 .30 .23 .22 .16 .48 .22 .36 .38 .34 .20 .26 .46 .34 .52 .37 .47 .79 .80 .80 .77
.12 .21 .20 .17 .21 .21 .24 .25 .31 .19 .20 .34 .28 .20 .26 .71 .33 .27 .32 .36 .32 .31 .37 .56 .37 .32 .40 .66 .46 .65 .67 .70 .41 .74 .67 .59 .68 .69 .65 .82 .83 .83 .82
.17 .14 .15 .12 .17 .13 .17 .18 .21 .14 .13 .27 .18 .19 .22 .57 .25 .27 .27 .27 .18 .26 .24 .32 .27 .27 .22 .46 .24 .35 .38 .49 .22 .54 .33 .39 .57 .42 .54 .79 .79 .80 .80
.18 .19 .18 .16 .20 .15 .21 .21 .23 .16 .15 .31 .26 .18 .26 .66 .31 .31 .31 .35 .28 .30 .33 .42 .34 .31 .31 .63 .35 .59 .61 .60 .34 .66 .41 .61 .67 .56 .63 .78 .79 .79 .78
.19 .21 .18 .16 .21 .18 .23 .24 .25 .17 .17 .29 .23 .20 .24 .44 .27 .26 .29 .32 .24 .28 .27 .32 .32 .29 .25 .38 .31 .35 .38 .44 .28 .48 .32 .43 .33 .42 .39 .59 .60 .59 .59
.16 .13 .14 .11 .14 .11 .16 .17 .20 .12 .12 .26 .16 .17 .21 .62 .23 .24 .26 .28 .16 .25 .23 .36 .26 .25 .16 .60 .28 .49 .56 .56 .19 .63 .31 .58 .44 .58 .54 .82 .82 .83 .82
.20 .20 .20 .19 .23 .21 .25 .25 .30 .21 .21 .32 .24 .23 .27 .50 .29 .30 .31 .34 .28 .30 .30 .35 .33 .32 .31 .46 .36 .41 .44 .47 .33 .53 .35 .46 .37 .61 .46 .67 .67 .67 .67
.10 .09 .10 .08 .11 .09 .11 .11 .13 .10 .09 .16 .11 .12 .14 .26 .14 .14 .16 .17 .11 .15 .16 .20 .16 .16 .12 .20 .17 .17 .22 .17 .14 .21 .18 .21 .22 .41 .18 .33 .54 .53 .48
.10 .09 .11 .08 .11 .09 .11 .11 .13 .09 .09 .15 .11 .12 .14 .26 .14 .14 .16 .17 .10 .15 .16 .20 .16 .16 .12 .20 .17 .17 .22 .17 .13 .20 .17 .21 .21 .40 .18 .33 .46 .48 .46
.10 .09 .10 .08 .11 .08 .11 .11 .13 .09 .09 .16 .11 .12 .14 .25 .14 .14 .16 .17 .10 .15 .15 .20 .16 .16 .11 .20 .17 .18 .22 .16 .13 .20 .17 .20 .21 .41 .17 .33 .47 .52 .46
.11 .09 .11 .08 .11 .09 .12 .11 .13 .09 .09 .16 .11 .12 .14 .26 .14 .14 .16 .18 .10 .15 .16 .20 .17 .16 .11 .20 .17 .18 .22 .17 .14 .23 .18 .20 .22 .41 .18 .33 .52 .54 .54
Pairwise win rate (Cell-level, pooled over all tiers)
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Win rate of row vs. column
Figure 7:Pairwise win rate.Each cell reports the cell-level win rate of the row model against the column model,
pooled over all (tier, spec, metric) cells. Models are ordered by rank-sum, as in Table 7, so EXAONE Finance is the
first row and column. EXAONE Finance is the only model that beats every other model head-to-head.
Head-to-head dominance.To probe robustness of the ranking, we also compute thepairwisewin rate between every
pair of models: the fraction of shared (tier, spec, metric) cells on which one model beats the other. Ties are split evenly
between the two models. Rows and columns are ordered by rank-sum, best first, as in Table 7. As shown in Figure 7,
EXAONE Finance is the only model whose row is entirely above0.5, i.e., it wins its head-to-head comparison against
all 43 baselines (per-opponent win rate ranging from0.51to0.90). Within that range, the narrowest margins are against
the TiRex family (TiRex-2-pretrain and TiRex-1.1, both0.51), the only baselines that come close, yet both still trail
EXAONE Finance on every tier of Table 7.
5.5 Analysis by Asset Scope
Profile across all scopes.Because the benchmark spans a broad universe of asset classes, Figure 1 profiles the model
as a percentile over the four datascopes(inter-country, country, sector, individual) crossed with the three tiers, where
100denotes the best of the 44 models. EXAONE Finance traces a near-maximal envelope, scoring in the95–100
percentile on ten of the eleven populated scope×tier cells.
12

0 10 20 30
Aggregate rank
Chronos-2 (Syn)
EXAONE Finance
Reverso
T oto-2.0
TiRex
Chronos-2
Chronos-Bolt
VisionTS
Moirai
TimesFM-2.0
5.6
5.8
7.8
8.8
9.8
10.1
13.1
20.0
31.6
33.0
Inter-country
0 10 20 30
Aggregate rank
EXAONE Finance
TiRex
Chronos-2
Reverso
VisionTS
Chronos-Bolt
Chronos-2 (Syn)
T oto-2.0
Moirai
TimesFM-2.0
6.2
6.5
9.7
9.8
11.7
12.7
12.9
15.7
27.8
31.2
Country (US)
0 10 20 30 40
Aggregate rank
EXAONE Finance
Chronos-2 (Syn)
T oto-2.0
Reverso
Chronos-Bolt
Chronos-2
TiRex
VisionTS
TimesFM-2.0
Moirai
3.6
5.5
7.3
8.1
11.0
11.1
11.7
22.5
32.0
37.4
Sector (US)
0 10 20
Aggregate rank
TiRex
VisionTS
Reverso
EXAONE Finance
Chronos-2 (Syn)
Chronos-2
Chronos-Bolt
TimesFM-2.0
T oto-2.0
Moirai
7.9
9.0
10.0
11.1
11.7
13.9
14.3
16.6
19.1
24.8
Individual (US)
0 10 20
Aggregate rank
Chronos-2 (Syn)
EXAONE Finance
Reverso
TiRex
TimesFM-2.0
Chronos-2
Chronos-Bolt
VisionTS
T oto-2.0
Moirai
7.0
7.2
9.7
12.9
13.0
14.4
14.7
15.9
17.3
21.7
Inter-country
0 10 20 30 40
Aggregate rank
EXAONE Finance
Reverso
TiRex
Chronos-Bolt
T oto-2.0
VisionTS
TimesFM-2.0
Moirai
Chronos-2 (Syn)
Chronos-2
3.2
4.5
10.9
12.9
14.8
15.7
16.5
20.2
24.4
35.8
Country (US)
0 10 20 30 40
Aggregate rank
EXAONE Finance
T oto-2.0
Chronos-2 (Syn)
Reverso
Chronos-2
Chronos-Bolt
TiRex
VisionTS
TimesFM-2.0
Moirai
1.1
3.1
6.8
8.6
12.8
13.4
13.9
19.9
26.0
33.9
Sector (US)
0 10 20
Aggregate rank
TiRex
Reverso
Chronos-2 (Syn)
VisionTS
EXAONE Finance
TimesFM-2.0
Chronos-2
Chronos-Bolt
Moirai
T oto-2.0
7.5
8.7
9.1
10.4
11.3
13.9
16.1
19.0
21.5
24.4
Individual (US)
0 5 10 15 20
Aggregate rank
EXAONE Finance
Chronos-2 (Syn)
TimesFM-2.0
Chronos-Bolt
Reverso
Moirai
Chronos-2
TiRex
VisionTS
T oto-2.0
11.4
11.7
12.6
13.7
14.9
15.3
15.3
17.6
18.3
20.0
Inter-country
0 10 20
Aggregate rank
EXAONE Finance
TimesFM-2.0
Chronos-2 (Syn)
Moirai
TiRex
T oto-2.0
Reverso
Chronos-2
Chronos-Bolt
VisionTS
2.9
5.8
7.5
9.0
10.0
10.5
10.6
11.6
13.1
22.0
Sector (US)
0 10 20
Aggregate rank
EXAONE Finance
Chronos-2 (Syn)
Reverso
Moirai
TimesFM-2.0
TiRex
T oto-2.0
Chronos-2
Chronos-Bolt
VisionTS
2.9
6.2
8.9
9.2
12.2
15.3
17.8
19.0
20.8
21.2
Individual (US)
Tier 1 (Point accuracy)Tier 2 (Cross-sectional IC)Tier 3 (Portfolio backtest)
Per-asset-scope model ranking across the three tiers
Figure 8:Comparison of the top-10 models across the three tiers.Each panel shows the aggregate rank (The
geometric mean of per-(Spec×metric) cell ranks, where lower is better) within the comparison set for one asset scope.
The rows correspond to Tier 1 (Point accuracy), Tier 2 (Cross-sectional IC), and Tier 3 (Portfolio backtest).
Ranking within each scope.To make the comparison concrete, Figure 8 breaks the ranking down model-by-model.
Each row corresponds to one tier and contains a panel per asset scope, plotting the aggregate rank (lower is better)
of EXAONE Finance against representative baselines. Across point accuracy (Tier 1), cross-sectional IC (Tier 2),
and portfolio backtest (Tier 3), EXAONE Finance is top-3 in ten of the eleven scope×tier panels, with Chronos-2
(Synthetic), the 2nd-ranked model in Table 7, as its closest competitor.
13

50
 0 50 100 150 200 250
20
40
60
Commodity (spot)
Inter-country
0 100 200 300
1.5
3.0
4.5
Crypto
Inter-country
50
 0 50 100 150 200 250
3.2
4.0
4.8
1e3 Commodity (future front)
Inter-country
50
 0 50 100 150 200 250
10.0
12.5
15.0
Commodity ETF (broad)
Inter-country
50
 0 50 100 150 200 250
10
15
20
Commodity ETF (single)
Inter-country
50
 0 50 100 150 200 250
20
25
30
Commodity ETF (single)
Inter-country
50
 0 50 100 150 200 250
3.0
4.5
6.0
1e4 Equity index (country)
Inter-country
50
 0 50 100 150 200 250
700
800
900
Equity index (country)
Inter-country
50
 0 50 100 150 200 250
1.5
2.0
2.5
3.0
Fixed income (breakeven)
Country (US)
20
 15
 10
 5
 0 5 10
1.5
2.0
2.5
Fixed income (breakeven)
Country (US)
20
 15
 10
 5
 0 5 10
3.0
4.5
6.0
Fixed income (corp. yield)
Country (US)
50
 0 50 100 150 200 250
0.75
1.00
1.25
1e4 Equity index
Country (US)
50
 0 50 100 150 200 250
2.5
3.0
3.5
1e3 Equity index
Country (US)
50
 0 50 100 150 200 250
690
720
750
Fixed income (bond TR)
Country (US)
50
 0 50 100 150 200 250
2.0
2.4
2.8
Fixed income (fwd. inflation)
Country (US)
20
 15
 10
 5
 0 5 10
3.0
4.5
6.0
Fixed income (inflation exp.)
Country (US)
50
 0 50 100 150 200 250
6
3
0
Fixed income (money market)
Country (US)
50
 0 50 100 150 200 250
1.5
0.0
1.5
Fixed income (money market)
Country (US)
40
 20
 0 20 40
2
4
6
8
Fixed income (mortgage)
Country (US)
50
 0 50 100 150 200 250
0.5
0.0
0.5
1.0
Fixed income (term spread)
Country (US)
50
 0 50 100 150 200 250
0.0
0.6
1.2
Fixed income (treasury)
Country (US)
20
 15
 10
 5
 0 5 10
4.0
4.8
5.6
1e5 Macro (activity)
Country (US)
20
 15
 10
 5
 0 5 10
2.0
2.4
2.8
1e3 Macro (banking)
Country (US)
20
 15
 10
 5
 0 5 10
4.8
5.2
5.6
1e3 Macro (banking)
Country (US)
20
 15
 10
 5
 0 5 10
4.25
4.50
4.75
1e6 Macro (credit)
Country (US)
20
 15
 10
 5
 0 5 10
4
5
6
1e4 Macro (external)
Country (US)
8
 6
 4
 2
 0 2
3
0
3
6
1e5 Macro (portfolio flow)
Country (US)
8
 6
 4
 2
 0 2
3.0
4.5
6.0
7.5
1e3 Macro (TIC flow)
Country (US)
20
 15
 10
 5
 0 5 10
1.2
1.5
1.8
2.1
1e3 Macro (housing)
Country (US)
8
 6
 4
 2
 0 2
0.8
1.0
1.2
1e7 Macro (IIP)
Country (US)
20
 15
 10
 5
 0 5 10
1.6
1.8
2.0
2.2
1e4 Macro (income)
Country (US)
20
 15
 10
 5
 0 5 10
120
128
136
144 Macro (inflation)
Country (US)
20
 15
 10
 5
 0 5 10
5.6
6.4
7.2
8.0
1e5 Macro (inventory)
Country (US)
20
 15
 10
 5
 0 5 10
52
56
60
64
Macro (labor)
Country (US)
20
 15
 10
 5
 0 5 10
90
105
120
135
Macro (labor by industry)
Country (US)
20
 15
 10
 5
 0 5 10
1.50
1.75
2.00
2.25
1e4 Macro (money)
Country (US)
8
 6
 4
 2
 0 2
110
120
130
Macro (productivity)
Country (US)
20
 15
 10
 5
 0 5 10
0
3
6
9
Macro (sentiment)
Country (US)
20
 15
 10
 5
 0 5 10
0.90
1.05
1.20
1e4 Macro (spending)
Country (US)
50
 0 50 100 150 200 250
25
50
75
Implied volatility
Country (US)
Ground truth EXAONE Finance ([q25,q75] CI) Chronos-2 (Synth)
Figure 9:Forecast visualizations across asset classes (Inter-country, Country).Each panel shows a context history,
the ground truth, the EXAONE Finance median forecast with its[q25,q 75]interval, and the median forecast of the 2nd-
ranked Chronos-2 (Synthetic). EXAONE Finance follows the ground truth more closely than the 2nd-ranked model
across diverse sectors.
Visualization of time series forecasts.Figures 9 and 10 visualize forecasts from EXAONE Finance across diverse
asset classes, overlaid with the 2nd-ranked model, Chronos-2 (Synthetic). Our median forecast (purple) tracks the
ground truth more closely than the 2nd-ranked model (orange), and the ground-truth value stays within the predicted
[q25,q 75]interval in most windows. Notably, several series in Figure 10 contain missing spans in their context (visible
as gaps in the ground-truth history), yet EXAONE Finance still forecasts through them accurately, consistent with its
masked-context design. Overall, these visualizations mirror the quantitative results: EXAONE Finance is accurate and
well calibrated across the diverse assets of a financial panel, even under missing observations.
14

0 100 200
60
80
100
Sector ETF
Sector (US)
0 100 200
15
18
21
24
Sector ETF
Sector (US)
0 100 200
12
14
16
Sector ETF
Sector (US)
0 100 200
10.0
12.5
15.0
17.5
Sector ETF
Sector (US)
0 100 200
24.0
25.5
27.0
Sector ETF
Sector (US)
0 100 200
0
40
80
120
Equity
Individual (US)
0 100 200
0.0
0.2
0.4
Equity
Individual (US)
0 100 200
200
250
300
Equity
Individual (US)
0 100 200
20
25
30
35
Equity
Individual (US)
8
 6
 4
 2
 0 2
0.0
1.5
3.0
4.5
1e6 Fundamentals (balance sheet)
Individual (US)
8
 6
 4
 2
 0 2
0.0
0.5
1.0
1e9 Fundamentals (balance sheet)
Individual (US)
8
 6
 4
 2
 0 2
0.4
0.8
1.2
1e9 Fundamentals (balance sheet)
Individual (US)
6
 4
 2
 0 2
0.0
1.5
3.0
1e7 Fundamentals (cash flow)
Individual (US)
6
 4
 2
 0 2
1.5
3.0
1e7 Fundamentals (cash flow)
Individual (US)
6
 4
 2
 0 2
0.4
0.8
1.2
1e7 Fundamentals (income)
Individual (US)
8
 6
 4
 2
 0 2
1.6
1.2
0.8
1e7 Fundamentals (income)
Individual (US)
8
 6
 4
 2
 0 2
0.25
0.50
0.75
1.00
1e7 Fundamentals (income)
Individual (US)
6
 4
 2
 0 2
0
4
8
12
Fundamentals (per share)
Individual (US)
8
 6
 4
 2
 0 2
1.00
0.75
0.50
0.25
Fundamentals (per share)
Individual (US)
6
 4
 2
 0 2
0.5
1.0
1.5
Fundamentals (per share)
Individual (US)
Ground truth EXAONE Finance ([q25,q75] CI) Chronos-2 (Synth)
Figure 10:Forecast visualizations across asset classes (Sector, Individual).Same setup as Figure 9, for the sector
and individual asset scopes.
6 Conclusion
We presentEXAONE Finance, an attention-free time series foundation model for financial forecasting. By replacing
self-attention with a causal 1D convolution for temporal mixing and a group-aware pooling MLP for variate mixing,
the model attains linear-time cost in both sequence length and variate count while retaining a patch-based, multi-
quantile decoding interface. A masked-context augmentation makes it robust to the missingness pervasive in financial
markets. Pretrained on asynthetic financialcorpus, EXAONE Finance ranks #1 in all three tiers of the FinVerse
benchmark and is the only model that wins its head-to-head comparison against every baseline.
Limitations and future works.
•Richer variate grouping.The group-aware pooling mixer natively supports arbitrary cross-series grouping struc-
tures, from the multiple fields of a single security to related instruments within a portfolio. Exploring these grouping
schemes, and scaling to broader multivariate financial panels, is a promising direction for further gains.
•Multimodal extension.Extending the model beyond numerical series to auxiliary modalities, such as the news,
disclosures, and earnings reports that accompany a price series, is a natural next direction [24, 33, 34].
•Broader-domain evaluation.Results are on a financial benchmark, and broad general-domain benchmarking (e.g.,
GIFT-Eval [1]) is complementary future work, since transfer beyond finance remains untested.
References
[1] Taha Aksu, Gerald Woo, Juncheng Liu, Xu Liu, Chenghao Liu, Silvio Savarese, Caiming Xiong, and Doyen
Sahoo. GIFT-Eval: A Benchmark For General Time Series Forecasting Model Evaluation. InNeurIPS 2024
TSALM Workshop, 2024.
[2] Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken, Andreas Auer, Boran Han, Pedro Mercado, Syama Sundar
Rangapuram, Huibin Shen, Lorenzo Stella, Xiyuan Zhang, Mononito Goswami, Shubham Kapoor, Danielle C.
Maddix, Pablo Guerron, Tony Hu, Junming Yin, Nick Erickson, Prateek Mutalik Desai, Hao Wang, Huzefa
Rangwala, George Karypis, Yuyang Wang, and Michael Bohlke-Schneider. Chronos-2: From Univariate to
Universal Forecasting.https://arxiv.org/abs/2510.15821, 2025.
15

[3] Abdul Fatir Ansari, Lorenzo Stella, Caner Turkmen, Xiyuan Zhang, Pedro Mercado, Huibin Shen, Oleksandr
Shchur, Syama Sundar Rangapuram, Sebastian Pineda Arango, Shubham Kapoor, Jasper Zschiegner, Danielle C.
Maddix, Hao Wang, Michael W. Mahoney, Kari Torkkola, Andrew Gordon Wilson, Michael Bohlke-Schneider,
and Yuyang Wang. Chronos: Learning the Language of Time Series.TMLR, 2024.
[4] Andreas Auer, Patrick Podest, Daniel Klotz, Sebastian Böck, Günter Klambauer, and Sepp Hochreiter. TiRex:
Zero-Shot Forecasting Across Long and Short Horizons with Enhanced In-Context Learning. InNeurIPS, 2025.
[5] Shaojie Bai, J. Zico Kolter, and Vladlen Koltun. An Empirical Evaluation of Generic Convolutional and Recur-
rent Networks for Sequence Modeling.https://arxiv.org/abs/1803.01271, 2018.
[6] Defu Cao, Furong Jia, Sercan O. Arik, Tomas Pfister, Yixiang Zheng, Wen Ye, and Yan Liu. TEMPO: Prompt-
based Generative Pre-trained Transformer for Time Series Forecasting. InICLR, 2024.
[7] Mouxiang Chen, Lefei Shen, Zhuo Li, Xiaoyun Joy Wang, Jianling Sun, and Chenghao Liu. VisionTS: Visual
Masked Autoencoders Are Free-Lunch Zero-Shot Time Series Forecasters. InICML, 2025.
[8] Si-An Chen, Chun-Liang Li, Nate Yoder, Sercan O. Arik, and Tomas Pfister. TSMixer: An All-MLP Architecture
for Time Series Forecasting.TMLR, 2023.
[9] Ben Cohen, Emaad Khwaja, Kan Wang, Charles Masson, Elise Ramé, Youssef Doubli, and Othmane Abou-
Amal. Toto: Time Series Optimized Transformer for Observability.https://arxiv.org/abs/2407.07874,
2024.
[10] Abhimanyu Das, Weihao Kong, Andrew Leach, Shaan Mathur, Rajat Sen, and Rose Yu. Long-term Forecasting
with TiDE: Time-series Dense Encoder.TMLR, 2023.
[11] Abhimanyu Das, Weihao Kong, Rajat Sen, and Yichen Zhou. A decoder-only foundation model for time-series
forecasting. InICML, 2024.
[12] Xueying Ding, Aakriti Mittal, and Achintya Gopal. DELPHYNE: A Pre-Trained Model for General and Finan-
cial Time Series.https://arxiv.org/abs/2506.06288, 2025.
[13] Jiaxiang Dong, Haixu Wu, Haoran Zhang, Li Zhang, Jianmin Wang, and Mingsheng Long. SimMTM: A simple
pre-training framework for masked time-series modeling. InNeurIPS, 2023.
[14] Vijay Ekambaram, Arindam Jati, Pankaj Dayama, Sumanta Mukherjee, Nam H. Nguyen, Wesley M. Gifford,
Chandra Reddy, and Jayant Kalagnanam. Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced
Zero/Few-Shot Forecasting of Multivariate Time Series. InNeurIPS, 2024.
[15] Kun Feng, Shaocheng Lan, Yuchen Fang, Wenchao He, Sihan Lu, Shuqi Gu, Lintao Ma, Xingyu Lu, and Kan
Ren. Kairos: Toward Adaptive and Parameter-Efficient Time Series Foundation Models.https://arxiv.org/
abs/2509.25826, 2025.
[16] Xinghong Fu, Yanhong Li, Georgios Papaioannou, and Yoon Kim. Reverso: Efficient Time Series Foundation
Models for Zero-shot Forecasting.https://arxiv.org/abs/2602.17634, 2026.
[17] Shanghua Gao, Teddy Koker, Owen Queen, Thomas Hartvigsen, Theodoros Tsiligkaridis, and Marinka Zitnik.
UniTS: A Unified Multi-Task Time Series Model. InNeurIPS, 2024.
[18] Azul Garza, Cristian Challu, and Max Mergenthaler-Canseco. TimeGPT-1.https://arxiv.org/abs/2310.
03589, 2023.
[19] Rakshitha Godahewa, Christoph Bergmeir, Geoffrey I. Webb, Rob J. Hyndman, and Pablo Montero-Manso.
Monash Time Series Forecasting Archive. InNeurIPS Datasets and Benchmarks Track, 2021.
[20] Mononito Goswami, Konrad Szafer, Arjun Choudhry, Yifu Cai, Shuo Li, and Artur Dubrawski. MOMENT: A
Family of Open Time-series Foundation Models. InICML, 2024.
[21] Lars Graf, Thomas Ortner, Stanisław Wo´ zniak, and Angeliki Pantazi. FlowState: Sampling-Rate-Equivariant
Time-Series Forecasting. InICML, 2026.
[22] Albert Gu and Tri Dao. Mamba: Linear-Time Sequence Modeling with Selective State Spaces. InCOLM, 2024.
16

[23] Tao Hong and Shu Fan. Probabilistic Electric Load Forecasting: A Tutorial Review.International Journal of
Forecasting, 32(3):914–938, 2016.
[24] Ming Jin, Shiyu Wang, Lintao Ma, Zhixuan Chu, James Y . Zhang, Xiaoming Shi, Pin-Yu Chen, Yuxuan Liang,
Yuan-Fang Li, Shirui Pan, and Qingsong Wen. Time-LLM: Time Series Forecasting by Reprogramming Large
Language Models. InICLR, 2024.
[25] Emaad Khwaja, Chris Lettieri, Gerald Woo, Eden Belouadah, Marc Cenac, Guillaume Jarry, Enguerrand Paquin,
Xunyi Zhao, Viktoriya Zhukov, Othmane Abou-Amal, Chenghao Liu, Ameet Talwalkar, and David Asker. Toto
2.0: Time Series Forecasting Enters the Scaling Era.https://arxiv.org/abs/2605.20119, 2026.
[26] Jaehoon Lee, Jun Seo, Seunghan Lee, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Minjae Kim, Sungdong
Yoo, Junhyeok Kang, Sangjun Han, et al. FinVerse: Financial Time-Series Benchmark.https://arxiv.org/
abs/2608.03259, 2026.
[27] Seunghan Lee, Juri Hong, Kibok Lee, and Taeyoung Park. Sequential Order-Robust Mamba for Time Series
Forecasting. InNeurIPS 2024 TSALM Workshop, 2024.
[28] Seunghan Lee, Jaehoon Lee, Jun Seo, Junhyeok Kang, Sangjun Han, Sungdong Yoo, Minjae Kim, Tae Yoon
Lim, Dongwan Kang, Hwanil Choi, et al. Beyond Magnitude and Shape: A Direction-Aware Loss for Time
Series Forecasting.https://arxiv.org/abs/2608.01857, 2026.
[29] Seunghan Lee, Jaehoon Lee, Jun Seo, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil
Choi, Soonyoung Lee, and Wonbin Ahn. Not All Retrievals are Useful: Cross-Attention for Input-Aware RAG
in Time Series Forecasting. InKDD 2026 Workshop on Mining and Learning from Time Series, 2026.
[30] Seunghan Lee, Taeyoung Park, and Kibok Lee. Learning to Embed Time Series Patches Independently. InICLR,
2024.
[31] Seunghan Lee, Taeyoung Park, and Kibok Lee. Dataset-Driven Channel Masks in Transformers for Multivariate
Time Series. InICASSP, pages 2401–2405, 2026.
[32] Seunghan Lee, Jun Seo, Jaehoon Lee, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil
Choi, Soonyoung Lee, and Wonbin Ahn. FinSTaR: Towards Financial Reasoning with Time Series Reasoning
Models. InEMNLP Industry Track, 2026.
[33] Seunghan Lee, Jun Seo, Jaehoon Lee, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil
Choi, Soonyoung Lee, and Wonbin Ahn. Rethinking Multimodal Fusion for Time Series: Auxiliary Modalities
Need Constrained Fusion. InKDD 2026 Workshop on Mining and Learning from Time Series, 2026.
[34] Haoxin Liu, Shangqing Xu, Zhiyuan Zhao, Lingkai Kong, Harshavardhan Kamarthi, Aditya B. Sasanur, Megha
Sharma, Jiaming Cui, Qingsong Wen, Chao Zhang, and B. Aditya Prakash. Time-MMD: Multi-Domain Multi-
modal Dataset for Time Series Analysis. InNeurIPS Datasets and Benchmarks Track, 2024.
[35] Xu Liu, Juncheng Liu, Gerald Woo, Taha Aksu, Yuxuan Liang, Roger Zimmermann, Chenghao Liu, Silvio
Savarese, Caiming Xiong, and Doyen Sahoo. Moirai-MoE: Empowering Time Series Foundation Models with
Sparse Mixture of Experts. InICML, 2025.
[36] Yong Liu, Guo Qin, Zhiyuan Shi, Zhi Chen, Caiyin Yang, Xiangdong Huang, Jianmin Wang, and Mingsheng
Long. Sundial: A Family of Highly Capable Time Series Foundation Models. InICML, 2025.
[37] Yong Liu, Haoran Zhang, Chenyu Li, Xiangdong Huang, Jianmin Wang, and Mingsheng Long. Timer: Genera-
tive Pre-trained Transformers Are Large Time Series Models. InICML, 2024.
[38] Donghao Luo and Xue Wang. ModernTCN: A Modern Pure Convolution Structure for General Time Series
Analysis. InICLR, 2024.
[39] Vladyslav Moroshan, Julien Siems, Arber Zela, Timur Carstensen, and Frank Hutter. TempoPFN: Synthetic
Pre-training of Linear RNNs for Zero-shot Time Series Forecasting.https://arxiv.org/abs/2510.25502,
2025.
[40] Yuqi Nie, Nam H. Nguyen, Phanwadee Sinthong, and Jayant Kalagnanam. A Time Series is Worth 64 Words:
Long-term Forecasting with Transformers. InICLR, 2023.
17

[41] Kashif Rasul, Arjun Ashok, Andrew Robert Williams, Hena Ghonia, Rishika Bhagwatkar, Arian Khorasani,
Mohammad Javad Darvishi Bayazi, George Adamopoulos, Roland Riachi, Nadhir Hassen, Marin Biloš, Sahil
Garg, Anderson Schneider, Nicolas Chapados, Alexandre Drouin, Valentina Zantedeschi, Yuriy Nevmyvaka, and
Irina Rish. Lag-Llama: Towards Foundation Models for Probabilistic Time Series Forecasting. InNeurIPS 2023
R0-FoMo Workshop, 2023.
[42] David Salinas, Valentin Flunkert, Jan Gasthaus, and Tim Januschowski. DeepAR: Probabilistic Forecasting with
Autoregressive Recurrent Networks.International Journal of Forecasting, 36(3):1181–1191, 2020.
[43] Omer Berat Sezer, Mehmet Ugur Gudelek, and Ahmet Murat Ozbayoglu. Financial Time Series Forecasting
with Deep Learning: A Systematic Literature Review: 2005–2019.Applied Soft Computing, 90:106181, 2020.
[44] Xiaoming Shi, Shiyu Wang, Yuqi Nie, Dianqi Li, Zhou Ye, Qingsong Wen, and Ming Jin. Time-MoE: Billion-
Scale Time Series Foundation Models with Mixture of Experts. InICLR, 2025.
[45] Xue Wang, Tian Zhou, Jinyang Gao, Bolin Ding, and Jingren Zhou. Output Scaling: YingLong-Delayed Chain
of Thought in a Large Pretrained Time Series Forecasting Model.https://arxiv.org/abs/2506.11029,
2025.
[46] Yihang Wang, Yuying Qiu, Peng Chen, Kai Zhao, Yang Shu, Zhongwen Rao, Lujia Pan, Bin Yang, and Chenjuan
Guo. Towards a General Time Series Forecasting Model with Unified Representation and Adaptive Transfer. In
ICML, 2025.
[47] Zihan Wang, Fanheng Kong, Shi Feng, Ming Wang, Xiaocui Yang, Han Zhao, Daling Wang, and Yifei Zhang.
Is Mamba Effective for Time Series Forecasting?Neurocomputing, 619:129178, 2025.
[48] Gerald Woo, Chenghao Liu, Akshat Kumar, Caiming Xiong, Silvio Savarese, and Doyen Sahoo. Unified Training
of Universal Time Series Forecasting Transformers. InICML, 2024.
[49] Shifeng Xie, Vasilii Feofanov, Ambroise Odonnat, Lei Zan, Marius Alonso, Jianfeng Zhang, Themis Palpanas,
Lujia Pan, Keli Zhang, and Ievgen Redko. CauKer: Classification Time Series Foundation Models Can Be
Pretrained on Synthetic Data. InICLR, 2026.
[50] Ailing Zeng, Muxi Chen, Lei Zhang, and Qiang Xu. Are Transformers Effective for Time Series Forecasting?
InAAAI, 2023.
[51] George Zerveas, Srideepika Jayaraman, Dhaval Patel, Anuradha Bhamidipaty, and Carsten Eickhoff. A
Transformer-based Framework for Multivariate Time Series Representation Learning. InKDD, pages 2114–
2124, 2021.
[52] Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianxin Li, Hui Xiong, and Wancai Zhang. Informer:
Beyond Efficient Transformer for Long Sequence Time-Series Forecasting. InAAAI, volume 35, pages 11106–
11115, 2021.
[53] Zhuohang Zhu, Haodong Chen, Qiang Qu, and Vera Chung. FinCast: A Foundation Model for Financial Time-
Series Forecasting.https://arxiv.org/abs/2508.19609, 2025.
18
