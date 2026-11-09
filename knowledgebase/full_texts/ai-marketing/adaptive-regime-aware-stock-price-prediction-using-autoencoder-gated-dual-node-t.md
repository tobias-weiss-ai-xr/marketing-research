---
title: Adaptive Regime-Aware Stock Price Prediction Using Autoencoder-Gated Dual Node Transformers with
  Reinforcement Learning Control
url: https://arxiv.org/abs/2603.19136
category: ai-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Mohammad Al Ridhawi
- Mahtab Haj Ali
- Hussein Al Osman
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.19136
pages: 17
chars: 94048
fetched_at: '2026-11-08T13:00:27+00:00'
kb_version: 1
---

# Adaptive Regime-Aware Stock Price Prediction Using Autoencoder-Gated Dual Node Transformers with Reinforcement Learning Control

1
This work has been submitted to Applied Intelligence (Springer) for possible publication.
Adaptive Regime-Aware Stock Price Prediction Using
Autoencoder-Gated Dual Node Transformers with Reinforcement
Learning Control
Mohammad Al Ridhawi, Mahtab Haj Ali, and Hussein Al Osman
School of Electrical Engineering and Computer Science,
University of Ottawa, Ottawa, Canada
e-mail: malri039@uottawa.ca
Abstract—Stock markets exhibit regime-dependent behavior
where prediction models optimized for stable conditions often
fail during volatile periods. Existing approaches typically treat
all market states uniformly or require manual regime label-
ing, which is expensive and quickly becomes stale as market
dynamics evolve. This paper introduces an adaptive prediction
framework that adaptively identifies deviations from normal
market conditions and routes data through specialized predic-
tion pathways. The architecture consists of three components:
(1) an autoencoder trained on normal market conditions that
identifies anomalous regimes through reconstruction error, (2)
dual node transformer networks specialized for stable and event-
driven market conditions respectively, and (3) a Soft Actor-
Critic reinforcement learning controller that adaptively tunes
the regime detection threshold and pathway blending weights
based on prediction performance feedback. The reinforcement
learning component enables the system to learn adaptive regime
boundaries, defining anomalies as market states where standard
prediction approaches fail. Experiments on 20 S&P 500 stocks
spanning 1982 to 2025 demonstrate that the proposed framework
achieves 0.68% mean absolute percentage error (MAPE) for one-
day predictions without the reinforcement controller and 0.59%
MAPE with the full adaptive system, compared to 0.80% for
the baseline integrated node transformer. Directional accuracy
reaches 72% with the complete framework. The system maintains
robust performance during high-volatility periods, with MAPE
below 0.85% when baseline models exceed 1.5%. Ablation studies
confirm that each component contributes meaningfully: autoen-
coder routing accounts for 36% relative MAPE degradation upon
removal, followed by the SAC controller at 15% and the dual-
path architecture at 7%.
Index Terms—Stock price forecasting, autoencoder, regime
detection, node transformer, reinforcement learning, Soft Actor-
Critic, adaptive systems, deep learning.
I. INTRODUCTION
F
INANCIAL markets operate across distinct regimes char-
acterized by different statistical properties, volatility lev-
els, and correlation structures [1]. During stable periods, price
movements follow relatively predictable patterns driven by
fundamental factors and gradual information incorporation.
Crisis periods, earnings announcements, and macroeconomic
shocks induce abrupt shifts in market behavior where historical
patterns provide limited guidance. Models trained on aggregate
historical data often perform well on average but degrade un-
der volatile or event-driven conditions, where robust prediction
is especially important.
Prior work on stock prediction has often treated market
conditions as homogeneous. Graph neural networks capture
cross-sectional dependencies [2], transformers model temporal
dynamics [3], and sentiment analysis incorporates qualitative
signals [4]. Our previous work demonstrated that combining
node transformer architectures with BERT (Bidirectional En-
coder Representations from Transformers) sentiment analysis
achieves 0.80% mean absolute percentage error (MAPE) and
65% directional accuracy (DA) on S&P 500 stocks [5]. Yet
this integrated model applies the same processing regardless of
market conditions, leaving potential gains from regime-aware
specialization unexploited.
The challenge of regime detection compounds prediction
difficulties. Traditional approaches rely on hidden Markov
models [1] or threshold rules on volatility indicators [6],
both requiring manual specification of regime definitions.
Supervised classifiers demand labeled training data identifying
which historical periods constitute crises or anomalies. Such
labels are subjective, backward-looking, and fail to generalize
as market structure evolves. A system that automatically dis-
covers regime boundaries from prediction performance itself
would avoid these limitations.
This paper introduces an adaptive framework addressing
both challenges. An autoencoder trained on normal market
data learns to reconstruct typical price patterns; high recon-
struction error indicates departure from learned normality. This
weakly supervised anomaly score gates data flow through
dual node transformer pathways: one optimized for stable
conditions, another incorporating event-specific features for
turbulent periods. A Soft Actor-Critic (SAC) reinforcement
learning controller observes prediction outcomes and adjusts
the autoencoder threshold and pathway blending weights to
maximize forecasting accuracy. The SAC component adapts
the anomaly-routing threshold by discovering which threshold
settings improve downstream predictions.
The contributions of this work are:
1) An autoencoder-based regime detection mechanism that
identifies market state shifts using weakly supervised
anomaly detection trained on historically stable market
arXiv:2603.19136v2  [cs.LG]  2 Apr 2026

2
periods. The autoencoder learns a compressed represen-
tation of normal market dynamics; deviations from this
representation trigger event-aware processing.
2) A dual node transformer architecture with specialized
pathways for stable and volatile market conditions. The
event pathway incorporates additional features including
volatility regime indicators, sentiment spikes, and event
characterization signals.
3) A Soft Actor-Critic reinforcement learning controller
that adaptively tunes the regime detection threshold and
pathway blending based on realized prediction perfor-
mance. This enables the system to learn adaptive regime
definitions from prediction outcomes rather than relying
on fully hand-labeled regime annotations.
4) Experimental validation demonstrating a 26% MAPE
reduction over the baseline integrated node transformer
(0.59% vs 0.80%) and a 7 percentage point improvement
in directional accuracy (72% vs 65%).
Section II reviews related work on regime detection, adap-
tive prediction, and reinforcement learning for financial appli-
cations. Section III presents the proposed architecture. Sec-
tion IV reports experimental results, and Section V discusses
findings, limitations, and implications.
II. LITERATUREREVIEW
A. Regime Detection in Financial Markets
Market regime identification has a long history in economet-
rics and quantitative finance. Hamilton [1] introduced Markov-
switching models that probabilistically transition between
states with distinct statistical properties. These models esti-
mate regime-specific parameters (means, variances, transition
probabilities) via maximum likelihood, enabling classification
of historical periods into regimes. Extensions incorporate time-
varying transition probabilities [7] and multivariate dependen-
cies.
Threshold models offer an alternative where regime
switches occur when observable variables cross specified
boundaries. The Self-Exciting Threshold Autoregressive (SE-
TAR) model [8] switches dynamics based on lagged values
of the series itself. In finance, volatility indices such as VIX
(CBOE V olatility Index) commonly serve as regime indicators,
with thresholds separating low, medium, and high volatility
states.
Machine learning approaches to regime detection include
clustering methods that partition historical periods based on
feature similarity [9], hidden Markov models with neural
network emission distributions, and change-point detection al-
gorithms [10]. These methods generally require either explicit
labels or assumptions about the number and nature of regimes.
The framework proposed in this paper does not entirely avoid
such assumptions, as the primary routing is binary and the
event pathway conditions on three VIX-based volatility levels.
This design nonetheless requires fewer structural commitments
than methods that must specify the number, boundaries, and
statistical properties of multiple regime states. The autoen-
coder learns to distinguish normal from anomalous market
conditions through reconstruction error without requiring ex-
plicit regime definitions, and the SAC controller continuously
adapts the routing threshold based on prediction feedback
rather than relying on fixed, manually chosen boundaries. The
regime structure is therefore partially discovered from data
rather than imposed entirely by the modeler.
B. Autoencoders for Anomaly Detection
Autoencoders learn compressed representations by recon-
structing inputs through an information bottleneck [11]. The
encoder maps inputs to a lower-dimensional latent space, and
the decoder reconstructs the original input from this represen-
tation. When trained on normal data, autoencoders reconstruct
typical patterns with low error; anomalous inputs that deviate
from the training distribution yield higher reconstruction error,
providing an anomaly score.
Variational autoencoders (V AEs) extend this framework
by imposing distributional constraints on the latent space
[12]. The V AE objective combines reconstruction loss with
a regularization term encouraging the latent distribution to
match a prior (typically standard Gaussian). This probabilistic
formulation enables principled uncertainty quantification and
generation of novel samples.
In financial applications, autoencoders have been applied to
fraud detection [13], anomaly identification in trading patterns
[14], and feature extraction for downstream prediction tasks
[15]. Liu et al. [16] employed autoencoder-based feature
extraction combined with bidirectional LSTM (Long Short-
Term Memory) for stock price prediction, reporting improved
performance from the learned representations.
C. Graph Neural Networks for Stock Prediction
Graph neural networks (GNNs) model relational structure
among entities through message passing over graph topology
[17]. In stock prediction, nodes represent individual securities
while edges capture relationships including sectoral affiliation,
supply chain connections, or return correlations.
Chen et al. [2] proposed a graph convolutional feature-based
CNN combining graph convolutions with dual convolutional
networks for market-level and stock-level features. Wang et al.
[18] introduced multi-graph architectures defining both static
(sector) and dynamic (correlation) graphs, achieving 5.11%
error reduction over LSTM baselines on Chinese market
indices.
The node transformer architecture [19] extends transformers
to graph-structured data through attention mechanisms that
respect graph topology. Unlike standard graph neural networks
with fixed message-passing schemes, node transformers learn
contextualized representations through adaptive attention over
graph neighborhoods.
D. Reinforcement Learning in Finance
Reinforcement learning (RL) optimizes sequential decision-
making through interaction with an environment, learning
policies that maximize cumulative reward [20]. Financial ap-
plications include portfolio optimization [21], order execution
[22], and trading strategy development [23].

3
Deep RL algorithms combine neural network function ap-
proximation with RL principles. Deep Q-Networks (DQN)
learn action-value functions for discrete action spaces [24],
while policy gradient methods directly optimize policies for
continuous action spaces. Actor-critic algorithms unify both
approaches by combining value estimation (critic) with policy
optimization (actor) for improved stability and sample effi-
ciency.
Soft Actor-Critic (SAC) [25] incorporates entropy regular-
ization into the actor-critic framework, encouraging explo-
ration while maintaining policy stability. By adding policy
entropy to the reward, the maximum entropy objective prevents
premature convergence to deterministic policies, and SAC
performs well across continuous control tasks with delayed,
noisy reward signals [25], [26].
Here, SAC serves not as a trading agent but as a meta-
controller that learns to configure the prediction system itself.
The controller adjusts the autoencoder threshold and pathway
blending weights based on observed prediction performance,
effectively learning what regime definitions optimize down-
stream forecasting accuracy.
E. Research Positioning
Prior work has addressed regime detection and stock predic-
tion as separate problems. Regime-switching models identify
market states but do not adapt prediction methods accordingly
[1], [27], [28], while stock prediction models treat all con-
ditions uniformly or rely on hand-crafted regime indicators
[2], [29]. Our framework integrates these elements by pairing
unsupervised regime detection (autoencoder) with specialized
prediction pathways (dual node transformers) and a SAC con-
troller that learns optimal regime definitions from prediction
outcomes. This closed-loop architecture enables the system to
discover useful regime boundaries rather than imposing them
a priori.
III. METHODOLOGY
A. System Overview
Figure 1 presents the complete system architecture. Raw
market data flows through feature engineering to produce
technical indicators and normalized price features. The autoen-
coder processes these features, producing a reconstruction er-
ror score that quantifies deviation from normal market patterns
and serves as the basis for regime classification. Based on this
score and a learned threshold, the router directs data to either
the normal or event node transformer pathway depending on
the detected regime. Both pathways produce predictions that
are blended according to learned weights. The final prediction
is evaluated, and the SAC controller uses this feedback to
adjust the autoencoder threshold and blending parameters for
subsequent iterations.
The termregimein this framework operates at two distinct
levels. At the primary level, the autoencoder performs a
binary classification of each trading day as eithernormalor
anomalousbased on whether its reconstruction error exceeds a
learned thresholdτ. This binary decision determines routing:
days classified as normal are processed by the normal node
Market Data Featuresx t
Autoencoder
Router
NodeFormer
(Normal)
NodeFormer
(Event)
Adaptive
Blending
Evaluation SAC Controller
et
et < τ et ≥τ
yN t+h yE t+h
ˆyt+h
RMSE, DA
τ
α
Fig. 1. System architecture overview. Market featuresx t enter the autoen-
coder, which produces reconstruction errore t (shown on arrow). The router
directs data to normal or event node transformer pathways based on whetheret
exceeds the learned thresholdτ. Each pathway produces a prediction (y N t+h,
yE t+h), and adaptive blending combines them into the final forecastˆy t+h. The SAC controller observes evaluation metrics and adjusts bothτandα
(dashed blue arrows) to optimize forecasting accuracy.
transformer, while anomalous days are directed to the event
node transformer. A binary primary classification is chosen
rather than a multi-class scheme for both practical and theoret-
ical reasons. The autoencoder’s reconstruction error is a scalar
anomaly score that naturally lends itself to thresholding rather
than clustering into multiple categories, and the fundamental
distinction in anomaly detection is between in-distribution and
out-of-distribution inputs. Attempting to subdivide anomalous
states at the routing stage would require assumptions about the
number and nature of anomaly categories that the unsupervised
autoencoder is not designed to make; instead, that finer-grained
characterization is deferred to the event pathway itself.
Within the event pathway, a secondary level of regime
characterization captures the heterogeneity of anomalous pe-
riods. The event context vectorc t provides the event node
transformer with descriptive features including a VIX-based
volatility classification into three levels (low, medium, or high,
determined by training-period terciles), sentiment spike indica-
tors, earnings event proximity, and cross-asset stress measures.
This secondary characterization does not constitute a sepa-
rate routing mechanism; rather, it conditions the event trans-
former’s internal representations by supplying information
about the nature of the detected anomaly. An earnings-driven
disruption during a period of otherwise low market volatility
produces different price dynamics than a systemic sell-off
during an already elevated volatility regime, and the context
vector enables the transformer to learn these distinctions
from the data. The normal transformer does not receive this
additional context because it processes in-distribution samples
where market dynamics follow the stable patterns learned dur-
ing the autoencoder’s training phase, making regime-specific
conditioning unnecessary.

4
B. Feature Engineering
Input features follow established methodologies for financial
time series. For each stockiat timet, the raw feature vector
comprises:
xraw i,t = [Ot, Ht, Lt, Ct, Vt](1)
whereO t,H t,L t,C t denote open, high, low, and closing
prices, andV t is trading volume (collectively referred to as
OHLCV data). Technical indicators include simple moving
averages (SMA) at 5, 10, and 20-day windows, exponen-
tial moving averages (EMA) at matching windows, 14-day
Relative Strength Index (RSI), Moving Average Convergence
Divergence (MACD) with standard (12, 26, 9) parameters,
daily returns, log returns, and 20-day rolling volatility. Figure 2
illustrates this pipeline.
Raw OHLCV
Data
SMA
5, 10, 20
EMA
5, 10, 20
RSI, MACD
Returns
Rolling
V olatility
Z-Score Normalization
(Expanding Window)
Prediction Features
xi,t ∈R 17
Router Features
xrouter i,t ∈R 6
Fig. 2. Feature engineering pipeline. Raw OHLCV data is processed through
technical indicator computations (SMA, EMA, RSI, MACD, volatility). All
features undergo expanding-window z-score normalization to prevent look-
ahead bias, producing prediction features and router-specific features.
In addition to prediction features, router-specific features
capture regime-relevant signals:
xrouter i,t = [σ(5) t , σ(20) t ,∆VIX t, ρ∆ t ,|S t|, νpost t ](2)
whereσ (k) t isk-day rolling volatility,∆VIX t is VIX per-
centage change,ρ ∆ t is change in average pairwise correlation
among stocks,|S t|is absolute sentiment magnitude, and
νpost t is post velocity (count of X posts mentioning crisis-
related keywords within the trading day). Sentiment enters the
router as an absolute value because the router’s function is
anomaly detection rather than directional prediction. For the
purpose of identifying unusual market conditions, the magni-
tude of sentiment deviation is the relevant signal: both strongly
negative sentiment (indicating panic) and strongly positive
sentiment (indicating euphoria or speculative excess) represent
departures from typical market behavior. The signed sentiment
scoreS t is retained in the full prediction feature vectorx i,t
that reaches the node transformers, so directional information
contributes to the price forecasts themselves even though the
routing decision depends only on sentiment intensity. These
six router features are chosen to capture both gradual shifts
(rolling volatility, correlation changes) and abrupt events (VIX
spikes, sentiment surges, social media clustering).
Missing values in price data (due to trading halts or data
gaps) are handled through temporally-aware imputation. For
training data, short gaps (1-2 trading days) use linear interpo-
lation between surrounding known values. For validation and
test data, only forward-filling from the most recent observed
value is applied to ensure no future information leaks into
predictions. Technical indicators (SMA, EMA, RSI, MACD)
are computed only after imputation, using the forward-filled
values.
Normalization uses expanding-window z-scores to prevent
look-ahead bias. During training, each feature is standardized
using the mean and standard deviation computed over all
available data from the start of the training period up to time
t:
˜xi,t = xi,t −µ 1:t σ1:t (3)
whereµ 1:t andσ 1:t are the cumulative mean and standard
deviation from the first training observation through timet.
This expanding window ensures that normalization at each
time step uses only past information. During validation and
testing, normalization statistics are fixed at the full training-
period values (µ 1:Ttrain andσ 1:Ttrain), ensuring that no informa-
tion from the evaluation period influences standardization.
C. Autoencoder for Regime Detection
The autoencoder learns a compressed representation of
normal market dynamics. It is trained exclusively on data from
stable market periods, defined during training as days where
VIX remains below the 75th percentile of its training-period
distribution. Figure 3 presents the detailed architecture.
xt
din 64 32
zt
dz 32 64
ˆxt
din et =∥x t − ˆxt ∥2 2
W1 W2 W3 W4
ReLU
ReLU ReLU
ReLU
Encoderf enc Decoderf dec
Fig. 3. Autoencoder architecture for regime detection. The encoder com-
presses the input feature vector through two hidden layers (64, 32 units) to a
latent representationz t of dimensiond z = 32. The decoder reconstructs the
input through symmetric layers. Reconstruction errore t serves as the anomaly
score for regime classification.
1) Architecture and Training:The encoder maps the con-
catenated feature vector to a latent representation through two
hidden layers:
zt =f enc(xt) =ReLU(W 2 ·ReLU(W 1xt +b 1) +b 2)(4)
wherex t ∈R din is the input feature vector,z t ∈R dz is
the latent representation withd z = 32, andW 1 ∈R 64×din,
W2 ∈R 32×64 are weight matrices. The decoder reconstructs
the input through a symmetric architecture:
ˆxt =f dec(zt) =W 4 ·ReLU(W 3zt +b 3) +b 4 (5)

5
whereW 3 ∈R 64×32 andW 4 ∈R din×64. The autoencoder
is trained to minimize reconstruction loss over the stable-
period data:
LAE = 1 T
TX
t=1
∥xt − ˆxt∥2 2 (6)
Training uses the Adam optimizer with learning rate10 −3,
batch size 64, for a maximum of 20 epochs with early stopping
based on validation reconstruction loss.
2) Anomaly Score and Routing:At inference time, the re-
construction error serves as an anomaly scoree t =∥x t − ˆxt∥2 2.
Data points withe t exceeding thresholdτare classified as
anomalous and routed to the event pathway, while those below
τproceed through the normal pathway. The thresholdτis
initialized at the 95th percentile of training-set reconstruction
errors and subsequently adjusted by the SAC controller.
D. Dual Node Transformer Architecture
Two node transformer networks process data depending on
regime classification. Both follow the same base architectural
design (6 layers, 8 attention heads, 512 model dimension)
but maintain independent weights trained on different data
subsets, and the event pathway accepts a larger input due
to additional context features. Figure 4 illustrates the dual
pathway structure.
Router:e t ≷τ
Normal Path (e t < τ) Event Path (e t ≥τ)
Input:x i,t
Stock Embedding
Temporal Encoding
Multi-Head Attention×6
Feed-Forward + LayerNorm
Prediction Head
ynormal i,t+h
Input:[x i,t ∥ct ]
Stock + Event Embedding
Temporal Encoding
Multi-Head Attention×6
Feed-Forward + LayerNorm
Prediction Head
yevent i,t+h
Adaptive Blending:ˆy=αy normal + (1−α)y event
Event Contextc t:
- Regime embedding
- Sentiment spike
- Days to earnings
- Cross-asset stress
Fig. 4. Dual node transformer architecture. The router directs data based
on reconstruction error. The normal pathway (left, orange) processes typi-
cal market conditions with base features. The event pathway (right, blue)
augments inputs with event context featuresc t. Both pathways follow the
same architectural design (layer count, attention heads, model dimension) but
maintain independently trained weights and differ in input dimensionality, as
the event pathway accepts additional context features. Outputs are blended
with adaptive weightα.
1) Normal Node Transformer:The normal pathway pro-
cesses typical market conditions using the node transformer ar-
chitecture [19], which extends standard transformers to graph-
structured data by incorporating relational inductive biases into
the attention mechanism. The stock market is represented as
a graphG= (V,E)withN= 20stock nodes and a fully-
connected edge set. While graph neural networks are often
applied to larger graphs, theN= 20design balances cross-
sectional breadth against temporal depth (252-day sequences
per stock), and ablation results confirm that the graph structure
contributes 7% MAPE improvement (Table VII), indicating
that cross-sectional dependencies carry predictive value even
at this scale.
Each stockireceives a learned embeddings i ∈R ds that
captures persistent stock-specific characteristics such as sector
behavior and volatility profile. The input representation for
stockiat timetconcatenates the normalized feature vector
with temporal encoding and the stock embedding:
h(0) i,t = [xi,t∥TE(t)∥si]∈R din (7)
Temporal encoding follows Vaswani et al. [3], us-
ing sinusoidal positional encodings where TE(t,2k) =
sin(t/100002k/d)and TE(t,2k+ 1) = cos(t/10000 2k/d)for
dimension indexkand model dimensiond= 512. This
encoding allows the model to distinguish trading days and
capture periodic patterns at multiple frequencies.
Edge weights in the graph are initialized from sector rela-
tionships and return correlations computed strictly on training
data (1982-2010):
e(0) ij = 0.5·δ sector(i, j) + 0.5·max(0, ρtrain ij )(8)
whereδ sector(i, j) = 1if stocksiandjshare the same
sector classification and0otherwise, andρ train ij is the Pearson
correlation of daily returns computed over the training period
only, preventing any leakage from validation or test data.
During training, edge weights are refined through a learnable
functione (ℓ+1) ij =σ(w T e [h(ℓ) i ∥h(ℓ) j ] +b e), whereσis the
sigmoid function andh (ℓ) i is the node representation at layer
ℓ. This allows the model to discover relationship patterns
not captured by initial sector and correlation priors. Figure 5
illustrates the resulting graph structure with representative
edge weights.
At each layer, the node transformer applies multi-head self-
attention with causal masking to jointly process all stocks
across the temporal dimension. The input representations are
projected into queries, keys, and values through learned linear
transformationsQ=XW Q,K=XW K,V=XW V , and
attention output is computed as:
A=softmax
 QKT
√dk +M+E

V(9)
whered k = 64is the key dimension,Mis the causal
mask withM ab =−∞ifa < bandM ab = 0other-
wise, andE∈R N×N is the learned edge weight matrix.
The additive graph bias allows content-based attention (via
QKT ) and structural priors (viaE) to jointly determine how
information flows between stocks at each layer, ensuring that
predictions at timetuse only information from times up to and
includingt. The architecture usesH= 8attention heads, each
operating in 64 dimensions, yielding a total model dimension
ofd model = 512.
Each transformer layer follows the standard pre-norm resid-
ual pattern. The multi-head attention output is added to the

6
AAPL
MSFT
CRM
JPM
JNJ
UNH
PFE
XOM
CVX
KO
PG
0.78
0.65
0.82
■Technology■Financial■Healthcare■Energy■Consumer
Fig. 5. Graph representation of stock relationships (representative subset
of 11 stocks shown for clarity; full graph contains all 20 stocks). Nodes
represent individual stocks, colored by sector. Solid edges indicate same-sector
connections with higher learned weights (annotated values show correlation-
based initialization from training data). Dashed edges represent weaker cross-
sector correlations that are learned during training.
input through a residual connection, followed by layer normal-
ization. The normalized output then passes through a position-
wise feed-forward network consisting of two linear transfor-
mations with a ReLU activation, expanding the representation
tod ff = 2048dimensions before projecting back to 512. A
second residual connection and layer normalization follow
the feed-forward block. Dropout at rate 0.1 is applied after
both the attention and feed-forward sublayers. The architecture
stacks 6 such layers, with the output of the final layer fed into
a prediction head consisting of a linear projection from the
model dimension to a single scalar price prediction per stock.
Figure 6 illustrates the detailed layer structure.
InputX (ℓ)
Multi-Head Attention (8 heads)
Add & LayerNorm
FFN (512→2048→512)
Add & LayerNorm
OutputX (ℓ+1)
Dropout 0.1
Dropout 0.1
×6layers
Fig. 6. Single transformer layer architecture. Input passes through multi-
head self-attention, residual connection with layer normalization, feed-forward
network, and another residual connection with normalization. The architecture
stacks 6 such layers.
2) Event Node Transformer:The event pathway augments
the base architecture with additional inputs capturing regime-
specific information. The input to the event transformer con-
catenates the standard feature vector with an event context
vector,x event i,t = [x i,t∥ct], wherec t ∈R dc withd c = 12.
This vector comprises four groups of features. A learned
regime embeddingr t ∈R 4 maps the current VIX regime
(low, medium, or high, determined by training-period VIX
terciles) through a trainable embedding layer. A sentiment
spike components t ∈R 2 encodes a binary flag and scaled
magnitude when daily sentiment exceeds two standard de-
viations of training-period sentiment. An event characteriza-
tion componenta t ∈R 4 captures proximity to scheduled
earnings announcements (days-to-announcement, normalized),
historical earnings surprise magnitude for the stock, a bi-
nary earnings-window indicator, and sector-average surprise.
Finally, a cross-asset stress vector¯e cross t ∈R 2 encodes the
mean and standard deviation of reconstruction error across all
20 stocks at timet, distinguishing systemic anomalies (high
mean error) from idiosyncratic ones (high variance). The full
context vector is the concatenationc t = [rt∥st∥at∥¯ecross t ].
Architecturally, the event transformer differs from the nor-
mal pathway in two respects beyond its independently trained
weights. First, the input projection layer is wider: while
the normal transformer’s first linear layer maps fromd in
dimensions (the concatenation of market features, temporal
encoding, and stock embedding), the event transformer maps
fromd in +d c dimensions to accommodate the appended
context vector. This wider projection maps back to the shared
model dimension ofd model = 512before entering the first
transformer layer, so all subsequent layers (the 6 transformer
blocks, feed-forward networks, and prediction head) operate at
the same dimensionality as the normal pathway. Second, the
event pathway includes a trainable embedding layer that maps
the discrete VIX regime label (one of three categories) to the
continuous regime embeddingr t ∈R 4. This embedding layer
is an additional learnable component with no counterpart in the
normal pathway, adding3×4 = 12trainable parameters for the
three regime categories. The remaining context features (s t,
at,¯ecross t ) are continuous values that enter the context vector
directly without additional learned transformations.
3) Pathway Blending:Rather than hard routing, predictions
from both pathways are blended with an adaptive weight:
ˆyi,t+h =α t ·y normal i,t+h + (1−α t)·y event i,t+h (10)
The blending coefficientα t ∈[0,1]is determined by the
SAC controller based on current market state. During high-
confidence normal periods,α t approaches 1; during clear
anomalies, it approaches 0. Intermediate values enable smooth
transitions and hedge against misclassification.
E. Soft Actor-Critic Controller
The SAC controller learns to configure the prediction system
by adjusting the autoencoder thresholdτand blending weight
αbased on observed prediction performance. Although these
are only two scalar parameters, the optimization landscape
is non-trivial: the reward signal is delayed (prediction er-
rors are observed only after the threshold decision), noisy
(financial returns are inherently stochastic), and non-stationary

7
(optimal thresholds shift as market regimes evolve). SAC is
well suited to this setting because its entropy regularization
prevents premature convergence to fixed threshold values, and
its off-policy learning with experience replay enables sample-
efficient adaptation from sparse, delayed feedback. Simpler
alternatives such as grid search or bandit methods typically
assume stationary reward distributions [20] and cannot adapt
continuously to shifting regime dynamics. Figure 7 presents
the actor-critic network architecture.
States t
[et ,¯e, σt ,RMSE t−1 ,DA t−1 , αt−1 , τt−1 ]
FC(256) + ReLU
FC(256) + ReLU
µϕ,logσ ϕ
Actiona t = [∆τ,∆α]
FC(256) + ReLU
FC(256) + ReLU
Qθ1 (s, a)
FC(256) + ReLU
FC(256) + ReLU
Qθ2 (s, a)
min(Qθ1 , Qθ2 )
Actorπ ϕ Twin Critics
Fig. 7. Soft Actor-Critic network architecture. The actor network (left,
orange) maps states to a Gaussian policy over actions[∆τ,∆α]. Twin critic
networks (right, green/cyan) estimate Q-values; the minimum is used to
prevent overestimation. All networks use two hidden layers with 256 units
and ReLU activation.
1) Markov Decision Process Formulation:The control
problem is formulated as a Markov Decision Process (MDP).
The states t comprises:
st = [et,¯et−k:t, σt,RMSE t−1,DA t−1, αt−1, τt−1](11)
including current reconstruction error, recent error history
over the pastk= 5trading days (one week), volatility, pre-
vious prediction metrics (Root Mean Squared Error (RMSE)
and Directional Accuracy (DA)), and current parameter set-
tings. The action space consists of continuous adjustments
at = [∆τ,∆α]∈[−0.1,0.1] 2 to threshold and blending
weight, clipped to maintainτ∈[e min, emax]andα∈[0,1].
The reward signal combines prediction accuracy and stability:
rt =−RMSE t −λ dir ·(1−DA t)−λ stable · |∆τ|(12)
whereλ dir = 0.5weights directional accuracy andλ stable =
0.1penalizes threshold instability to prevent oscillation.
2) SAC Algorithm:SAC maximizes the entropy-regularized
objective:
J(π) =
TX
t=0
E[r t +α entH(π(·|st))](13)
whereHis policy entropy andα ent is the temperature
parameter controlling exploration. The actor networkπ ϕ(a|s)
outputs a Gaussian distribution over actions,π ϕ(a|s) =
N(µ ϕ(s), σϕ(s)2), while two critic networksQ θ1,Q θ2 esti-
mate action values. To prevent overestimation, the minimum
of both critics is used:
Q(s, a) = min(Qθ1 (s, a), Qθ2 (s, a))(14)
All networks are feed-forward with two hidden layers of 256
units each. Training uses the Adam optimizer with learning
rate3×10 −4, soft target updates withτ soft = 0.005, and
replay buffer size10 5.
3) Training Protocol:The SAC controller is trained after
the autoencoder and node transformers are pre-trained. Train-
ing begins by initializingτat the 95th percentile of training
reconstruction errors andα= 0.5. At each step, the controller
computes predictions using the currentτandα, evaluates them
against actual outcomes to obtain the reward signal, updates
the SAC networks from collected transitions, and applies the
learned action adjustments to both parameters. This loop runs
for 50 epochs with 1000 steps per epoch. Temperatureα ent
is automatically tuned to target entropy−dim(a)following
Haarnoja et al. [25].
F . Training Pipeline
Figure 8 illustrates the complete multi-stage training
pipeline.
Stage 1: AE
20 epochs
Stable data
Stage 2: NodeFormer
60 epochs
Normal + Event
Stage 3: SAC
50 epochs
Learnτ,α
Stage 4: Fine-tune
20 epochs
All unfrozen
Training Progression
Fig. 8. Multi-stage training pipeline. Stage 1 trains the autoencoder on stable
market data. Stage 2 trains both node transformers on their respective data
subsets. Stage 3 trains the SAC controller with frozen prediction components.
Stage 4 performs end-to-end fine-tuning with all weights unfrozen.
The complete training pipeline proceeds in four stages. In
Stage 1 (20 epochs), the autoencoder is trained on stable-
period data where VIX falls below the 75th percentile of its
training-period distribution. Stage 2 (60 epochs) trains both
node transformers: the normal pathway on data with low
reconstruction error (below the 95th percentile), and the event
pathway on high-error data augmented with context features.
In Stage 3 (50 epochs), autoencoder and node transformer
weights are frozen while the SAC controller learns to optimize
the threshold and blending parameters. Finally, Stage 4 (20
epochs) unfreezes all components for end-to-end fine-tuning
with reduced learning rates. The architecture is modular by
design: Stages 1 and 2 produce a fully functional prediction
system in which the routing threshold and blending weight
remain at their initialization values (τat the 95th percentile
of training-set reconstruction errors,α= 0.5). Stage 3 adds
adaptive control on top of this static configuration, allowing
the experimental evaluation to quantify the marginal contri-
bution of the SAC controller by comparing the system with
and without it. At inference time, all weights, including the
SAC policy network, are frozen. The policy produces state-
dependent routing decisions through its fixed learned mapping,
with no gradient updates or reward computation during the test
period.
G. Loss Functions
The prediction networks minimize a composite loss:
L=λ 1LMSE +λ 2LDIR +λ 3LREG (15)

8
whereL MSE = 1 N P i,t,h(yi,t+h −ˆyi,t+h)2 is the mean
squared error between predicted and actual prices. The direc-
tional lossL DIR is a binary cross-entropy term that explicitly
rewards correct prediction of price movement direction, since
minimizing magnitude error alone does not guarantee direc-
tional accuracy:
LDIR =− 1 N X i,t,h [di,t,h logp i,t,h + (1−d i,t,h) log(1−p i,t,h)]
(16)
whered i,t,h =I(y i,t+h > yi,t)is the true direction indicator
andp i,t,h is the predicted probability of a price increase. The
regularization termL REG =∥θ∥ 2 2 applies L2 weight decay over
all trainable parametersθ, penalizing large weight magnitudes
to prevent overfitting. Loss weights areλ 1 = 1.0,λ 2 = 0.5,
λ3 = 10−4.
Table I summarizes all model hyperparameters across the
three components.
TABLE I
MODELHYPERPARAMETERS
Component Parameter Value
Autoencoder
Hidden layers [64, 32]
Latent dimension 32
Learning rate10 −3
Training epochs 20
Node Transformer
Layers 6
Attention heads 8
Model dimension 512
FFN dimension 2048
Dropout 0.1
Learning rate10 −4
Input sequence length 252 days
SAC Controller
Hidden layers [256, 256]
Learning rate3×10 −4
Soft updateτ0.005
Replay buffer10 5
Training epochs 50
Stage 4 Fine-tuning
AE learning rate10 −4
Node Transformer learning rate10 −5
SAC learning rate3×10 −5
IV. EXPERIMENTS ANDRESULTS
A. Dataset and Experimental Setup
The dataset comprises two complementary data streams for
20 S&P 500 stocks spanning January 1982 to March 2025.
The Financial Market Data (FMD) stream consists of daily
OHLCV (open, high, low, close, volume) price data sourced
from Yahoo Finance, providing adjusted close prices that ac-
count for stock splits and dividends. Each trading day produces
a five-dimensional price vector per stock alongside the trading
volume, from which 11 additional technical indicators are
derived (SMA, EMA, RSI, MACD, returns, log returns, and
rolling volatility) as described in Section III. The sentiment
stream draws on two datasets. The first is the Market Sentiment
Evaluation (MSE) dataset [30], a publicly available corpus of
finance-related social media messages annotated by financial
experts with sentiment scores in[−1,+1], which serves as
ground truth for fine-tuning the BERT sentiment classifier. The
second is the Comprehensive Stock Sentiment (CSS) dataset,
which was introduced in [5] and was constructed using the X
(formerly Twitter) API through systematic searches for posts
mentioning the 20 stock tickers, yielding approximately 4.2
million posts covering January 2007 to March 2025. The
fine-tuned BERT model is applied to the CSS corpus to
generate daily sentiment scores for each stock, which are then
aggregated and fed into the prediction framework as additional
input features.
Table II lists the complete stock universe. Stocks were
selected to span nine distinct sectors, ensuring that the graph
structure captures both intra-sector and cross-sector depen-
dencies. The selection also prioritizes variation in market
capitalization, trading volume, and volatility characteristics to
evaluate robustness across different stock profiles. For compa-
nies with IPO dates after 1982 (e.g., Salesforce incorporated
1999, Netflix 2002, Visa 2008), data begins at their first
available trading date, and these stocks are included in training
only from their listing date onward.
TABLE II
STOCKUNIVERSE: 20 S&P 500 CONSTITUENTSACROSS9 SECTORS
Sector Stock (Ticker) Data Start
Technology
Apple (AAPL) 1982
Microsoft (MSFT) 1986
Salesforce (CRM) 1999
Financial Services JPMorgan Chase (JPM) 1982 Visa (V) 2008
Healthcare
Johnson & Johnson (JNJ) 1982
UnitedHealth Group (UNH) 1984
Pfizer (PFE) 1982
Retail Walmart (WMT) 1982 Home Depot (HD) 1982
Energy ExxonMobil (XOM) 1982 Chevron (CVX) 1982
Consumer Goods
Procter & Gamble (PG) 1982
Coca-Cola (KO) 1982
Nike (NKE) 1982
McDonald’s (MCD) 1982
Entertainment Netflix (NFLX) 2002
Telecommunications Verizon (VZ) 1982
Industrials Boeing (BA) 1982 Caterpillar (CAT) 1982
Temporal splits maintain strict chronological separation
to prevent any leakage of future information into training.
The training set spans January 1982 to December 2010
(approximately 70% of the temporal range), encompassing
multiple market cycles including the 1987 crash, the dot-
com bubble and its collapse, and the 2008 financial crisis.
The validation set covers January 2011 to December 2016
(approximately 15%), a period of relatively steady recovery
used for hyperparameter tuning and early stopping. The test
set spans January 2017 to March 2025 (approximately 15%),
including the 2018 correction, the 2020 COVID crash, and the

9
2022 market decline, which provide rigorous evaluation under
diverse volatility conditions.
Since the X platform (formerly Twitter) was founded in
2006, sentiment data covers January 2007 to March 2025. For
the 1982-2006 portion of training, sentiment features are set
to zero, meaning the model learns to operate with and without
sentiment depending on the data period. During the validation
and test periods, full sentiment coverage is available.
B. Evaluation Metrics
Model performance is assessed using five complementary
metrics. The primary metric is Mean Absolute Percentage
Error (MAPE), defined as:
MAPE= 100 N
NX
i=1

 yi −ˆyi yi

 (17)
MAPE provides intuitive interpretation as percentage devi-
ation from actual prices. As a complementary measure, Root
Mean Squared Error (RMSE) penalizes large errors more
heavily due to the squaring operation and is computed in
normalized price units, where each stock’s prices are z-scored
individually to enable fair cross-stock aggregation:
RMSE=
vuut 1
N
NX
i=1
(yi −ˆyi)2 (18)
Directional Accuracy (DA) measures the proportion of
correctly predicted price movement directions, which is par-
ticularly relevant for trading applications where the sign of the
predicted move often matters more than its magnitude:
DA= 100 N
NX
i=1
I(sign(ˆyi,t+h −y i,t) =sign(y i,t+h −y i,t))
(19)
Theil’s U statistic provides a scale-independent benchmark
by comparing forecast error to that of a naive random walk
that predicts tomorrow’s price as today’s price:
U=
pP
t(yt+1 −ˆyt+1)2 pP
t(yt+1 −y t)2 (20)
Values ofU <1indicate that the model outperforms the
naive baseline, making this metric particularly informative for
long time series where absolute price level changes can affect
percentage-based measures. Finally, the Confidence Tracking
Rate (CTR) captures the proportion of predictions where
model confidence (measured as inverse prediction variance
across the dual pathway outputs) agrees with actual accuracy:
CTR= 1 N T X i,t I((confi,t >¯c) = (|ˆyi,t+h −y i,t+h|<¯ϵ))
(21)
where confi,t is the inverse prediction variance from the two
pathways,¯cis the median confidence, and¯ϵis the median
absolute error across all predictions. CTR indicates whether
the model “knows when it knows,” a property valuable for
risk-sensitive downstream applications.
C. Baseline Models
Baselines span statistical methods (ARIMA, V AR, MS-
V AR [31]), classical machine learning (Random Forest, SVR,
XGBoost), deep learning (LSTM, Simple Transformer), mul-
timodal and regime-switching approaches (BERT Sentiment +
LSTM, HMM-LSTM), recent time-series transformers (Times-
Net [32], PatchTST [33], iTransformer [34]), and the Inte-
grated NodeFormer-BERT model from prior work [5].
To ensure fair comparison, all baselines share the same
experimental conditions wherever the model class permits.
Every model uses identical temporal splits (training: 1982–
2010, validation: 2011–2016, test: 2017–2025), the same
expanding-window z-score normalization described in Sec-
tion III, and the same missing-data imputation strategy. Models
capable of multivariate input (Random Forest, SVR, XG-
Boost, LSTM, Simple Transformer, BERT Sentiment + LSTM,
TimesNet, PatchTST, iTransformer, HMM-LSTM, Integrated
NodeFormer-BERT) receive the same 17-dimensional feature
vector comprising OHLCV data and 11 derived technical
indicators. Daily sentiment scores produced by the fine-
tuned BERT classifier are appended to the feature set for all
multivariate models, so that any advantage from sentiment
information is available to baselines as well as to the proposed
framework. ARIMA operates on the univariate closing price
series for each stock independently, V AR jointly models the
closing prices of all 20 stocks, and MS-V AR extends the V AR
specification with Markov-switching regime dynamics over the
same joint price series, since these statistical methods are not
designed to incorporate arbitrary exogenous feature vectors.
The target variable for all models is identical: the closing price
at horizonh∈ {1,5,20}trading days ahead.
The Simple Transformer baseline uses the same encoder
architecture as the proposed node transformer (6 layers, 8 at-
tention heads, 512-dimensional representations) but processes
each stock’s time series independently without graph structure
or inter-stock attention, isolating the contribution of graph-
based relational modeling. The BERT Sentiment + LSTM
baseline combines the same BERT-derived sentiment scores
with a two-layer LSTM through concatenation-based fusion,
testing whether the attention-based integration in the proposed
architecture provides meaningful improvement over straight-
forward feature combination. The Integrated NodeFormer-
BERT model reproduces our prior work [5] with its published
hyperparameters, serving as the primary single-pathway base-
line against which architectural additions are measured.
PatchTST [33] segments each stock’s multivariate input
time series into overlapping patches and applies a transformer
encoder with self-attention over the patch sequence, capturing
local temporal patterns within patches and long-range depen-
dencies across them. Its channel-independent design processes
each feature dimension separately before aggregating predic-
tions, which limits its ability to model cross-feature interac-
tions. iTransformer [34] inverts the conventional transformer
architecture by applying self-attention across the variate (fea-
ture) dimension rather than the temporal dimension, enabling
it to capture dependencies among price, volume, technical
indicators, and sentiment features at each time step. Times-

10
Net [32] extends temporal modeling by transforming one-
dimensional time series into two-dimensional tensors based on
learned multi-periodicity structure, applying inception-based
convolution blocks to capture both intra-period and inter-
period variation. All three recent time-series transformers
process each stock’s feature set independently without graph
structure or cross-stock attention, isolating the contribution of
relational modeling in the proposed framework.
The Markov-Switching V AR (MS-V AR) [31] extends the
V AR baseline withK= 3latent regime states governed
by a first-order Markov chain, allowing the intercepts and
error covariance to vary across regimes while the autore-
gressive coefficients remain regime-invariant (MSIH specifi-
cation). Regime transitions are inferred through maximum
likelihood estimation of the full joint model, in contrast
to our autoencoder-based approach which detects anomalies
from reconstruction error without specifying the number or
parametric structure of regimes a priori. The HMM-LSTM
baseline combines a Hidden Markov Model withK= 3
states for regime detection with three regime-specific two-
layer LSTMs, each trained on data assigned to its correspond-
ing regime by the Viterbi decoder. At inference, the HMM
identifies the most likely current regime and routes the input
to the corresponding LSTM, producing a regime-conditional
forecast. This architecture provides the most direct comparison
to our framework: it replaces the autoencoder with an HMM
for regime detection, the node transformers with LSTMs for
prediction, and omits adaptive control entirely, using fixed
routing with no blending across pathways.
Each baseline underwent hyperparameter tuning via grid
search on validation data, with the search ranges and selected
values reported in Table X (Appendix).
D. Main Results
Results are reported for two variants of the proposed frame-
work. The full model (AE-NodeFormer + SAC) includes all
components and completes all four training stages. The ablated
variant (AE-NodeFormer, no SAC) retains the autoencoder and
dual node transformers but removes the reinforcement learning
controller entirely, skipping Stage 3 of the training pipeline.
In this variant, the routing threshold is fixed atτ=e 95, the
95th percentile of training-set reconstruction errors, which is
the same initialization used by the full model before SAC
adaptation begins. This percentile is a standard choice in
anomaly detection, classifying the top 5% of reconstruction
errors as anomalous. The blending weight is held constant
atα= 0.5, assigning equal contribution to both pathways
regardless of market conditions. Comparing the two variants
isolates the contribution of adaptive parameter tuning from the
architectural benefits of autoencoder routing and dual-pathway
specialization.
Table III presents 1-day ahead closing price prediction
results across all baselines and proposed variants.
The proposed AE-NodeFormer + SAC achieves 0.59%
MAPE, representing a 26% relative improvement over the
Integrated NodeFormer-BERT baseline (0.80%) and a 28%
improvement over iTransformer (0.82%), the strongest recent
TABLE III
1-DAYAHEADCLOSINGPRICEPREDICTIONRESULTS. BESTRESULTS IN
BOLD.
Model MAPE RMSE DA Theil’s U CTR
ARIMA [35] 1.20% 1.35 55% 0.98 51%
V AR [36] 1.10% 1.30 56% 0.95 52%
MS-V AR [31] 1.02% 1.22 57% 0.90 53%
Random Forest [37] 1.10% 1.25 57% 0.92 53%
SVR [38] 1.20% 1.40 54% 1.02 50%
XGBoost [39] 1.00% 1.15 59% 0.85 55%
LSTM [40] 1.00% 1.20 58% 0.88 54%
Simple Transformer [3] 0.90% 1.10 61% 0.80 57%
BERT Sent. + LSTM [4] 0.90% 1.05 62% 0.78 58%
HMM-LSTM [1] 0.87% 1.02 64% 0.76 60%
TimesNet [32] 0.85% 1.00 63% 0.75 59%
PatchTST [33] 0.83% 0.98 64% 0.74 59%
iTransformer [34] 0.82% 0.97 64% 0.73 61%
Integrated NF-BERT [5] 0.80% 0.95 65% 0.72 62%
AE-NodeFormer (no SAC) 0.68% 0.88 69% 0.68 64%
AE-NodeFormer + SAC 0.59% 0.82 72% 0.64 67%
time-series transformer. Directional accuracy reaches 72%,
a 7 percentage point gain over the graph-based baseline.
Among regime-switching approaches, HMM-LSTM achieves
0.87% MAPE, outperforming the basic LSTM (1.00%) by
13% through regime-specific specialization, yet still trailing
the proposed model by 32%, indicating that the combina-
tion of autoencoder-based anomaly detection, graph-aware
dual pathways, and adaptive control provides substantially
greater benefit than parametric regime detection with indepen-
dent LSTMs. The recent time-series transformers (TimesNet
0.85%, PatchTST 0.83%, iTransformer 0.82%) cluster near
the Integrated NodeFormer-BERT (0.80%), confirming that
the prior single-pathway architecture was already competitive
with current state-of-the-art forecasting models and that the
improvements in the present work stem from the regime-
aware architectural innovations rather than from a weak base-
line. All pairwise improvements of the proposed model over
iTransformer, PatchTST, and HMM-LSTM are statistically
significant (Diebold-Mariano test [41],p <0.001in each
case).
To contextualize the directional accuracy, we computed a
naive long-only baseline: predicting “up” for every day. Over
the 2017-2025 test period, this naive strategy achieves 54% DA
on average across the 20 stocks, reflecting the slight upward
drift in equity markets. The 72% DA of the proposed model
thus represents an 18 percentage point improvement over this
trivial baseline, confirming that the model captures predictive
signal beyond simple market drift.
To assess generalization across forecasting horizons, Ta-
ble IV and Table V present 5-day and 20-day ahead closing
price results.
Performance improvements persist across all prediction
horizons. At the 5-day horizon, the proposed model achieves
1.05% MAPE compared to 1.30% for the Integrated
NodeFormer-BERT and 1.35% for iTransformer, maintaining
a 19% and 22% relative advantage respectively. At 20 days,
these gaps widen further: the proposed model reaches 1.55%
MAPE versus 1.90% for the graph-based baseline and 2.00%
for iTransformer, reflecting the increasing value of regime-
aware routing as the prediction horizon extends and structural

11
TABLE IV
5-DAYAHEADCLOSINGPRICEPREDICTIONRESULTS
Model MAPE RMSE DA Theil’s U CTR
ARIMA [35] 2.05% 2.30 51% 1.05 47%
V AR [36] 1.88% 2.10 52% 1.00 48%
MS-V AR [31] 1.70% 1.90 53% 0.95 49%
Random Forest [37] 1.92% 2.15 52% 1.02 48%
SVR [38] 2.10% 2.35 50% 1.08 46%
XGBoost [39] 1.68% 1.88 54% 0.92 50%
LSTM [40] 1.65% 1.85 54% 0.93 50%
Simple Transformer [3] 1.50% 1.68 56% 0.85 53%
BERT Sent. + LSTM [4] 1.48% 1.65 57% 0.83 54%
HMM-LSTM [1] 1.45% 1.60 59% 0.82 55%
TimesNet [32] 1.40% 1.55 58% 0.81 56%
PatchTST [33] 1.38% 1.52 59% 0.79 55%
iTransformer [34] 1.35% 1.50 59% 0.80 57%
Integrated NF-BERT [5] 1.30% 1.45 61% 0.78 58%
AE-NodeFormer (no SAC) 1.15% 1.32 64% 0.74 60%
AE-NodeFormer + SAC 1.05% 1.25 67% 0.70 63%
TABLE V
20-DAYAHEADCLOSINGPRICEPREDICTIONRESULTS
Model MAPE RMSE DA Theil’s U CTR
ARIMA [35] 3.10% 3.45 48% 1.12 44%
V AR [36] 2.85% 3.20 49% 1.05 45%
MS-V AR [31] 2.55% 2.85 50% 0.98 46%
Random Forest [37] 2.90% 3.25 49% 1.08 45%
SVR [38] 3.20% 3.55 47% 1.15 43%
XGBoost [39] 2.60% 2.90 51% 0.98 47%
LSTM [40] 2.50% 2.80 51% 0.96 47%
Simple Transformer [3] 2.25% 2.52 53% 0.90 50%
BERT Sent. + LSTM [4] 2.20% 2.45 54% 0.88 51%
HMM-LSTM [1] 2.12% 2.35 55% 0.87 52%
TimesNet [32] 2.08% 2.30 56% 0.85 52%
PatchTST [33] 2.05% 2.28 55% 0.84 53%
iTransformer [34] 2.00% 2.22 56% 0.86 53%
Integrated NF-BERT [5] 1.90% 2.15 57% 0.85 54%
AE-NodeFormer (no SAC) 1.70% 2.00 60% 0.82 56%
AE-NodeFormer + SAC 1.55% 1.85 63% 0.78 59%
regime shifts become more consequential. Several statistical
and classical ML baselines (ARIMA, V AR, Random Forest,
SVR) produce Theil’s U values exceeding 1.0 at the 20-
day horizon, indicating that they underperform the naive
random walk at longer horizons, a well-known limitation of
models without explicit temporal or regime-adaptive struc-
ture. In contrast, all transformer-based and regime-switching
models maintain Theil’s U below 1.0 across all horizons.
Directional accuracy for the proposed model declines from
72% at 1-day to 63% at 20-day, a more gradual degradation
than iTransformer (64% to 56%) or HMM-LSTM (64% to
55%), suggesting that the combination of autoencoder routing
and SAC adaptation captures structural signals that remain
informative beyond short-term momentum.
E. Per-Stock Results
To examine cross-sectional variation, Table VI presents 1-
day ahead closing price results for all 20 stocks in the universe,
grouped by sector.
Individual stock performance spans from 0.42% MAPE
(WMT) to 1.10% (XOM), with 16 of 20 stocks falling
below 0.70%. The error distribution aligns with established
differences in equity predictability. Defensive stocks with
TABLE VI
PER-STOCK1-DAYAHEADCLOSINGPRICERESULTS(AE-NODEFORMER
+ SAC)
Sector Stock MAPE RMSE DA Theil’s U
Technology
AAPL 0.62% 0.88 69% 0.68
MSFT 0.50% 0.72 74% 0.60
CRM 0.63% 0.89 70% 0.67
Financial Services JPM 0.70% 1.02 67% 0.72 V 0.48% 0.69 76% 0.58
Healthcare
JNJ 0.44% 0.64 77% 0.55
UNH 0.52% 0.74 73% 0.61
PFE 0.58% 0.80 72% 0.64
Retail WMT 0.42% 0.62 78% 0.54 HD 0.48% 0.68 75% 0.59
Energy XOM 1.10% 1.38 63% 0.82 CVX 0.95% 1.22 64% 0.79
Consumer Goods
PG 0.43% 0.62 77% 0.55
KO 0.44% 0.65 76% 0.56
NKE 0.56% 0.73 72% 0.63
MCD 0.45% 0.65 77% 0.56
Entertainment NFLX 0.75% 1.05 66% 0.75
Telecommunications VZ 0.47% 0.67 75% 0.58
Industrials BA 0.68% 0.94 68% 0.71 CAT 0.60% 0.81 71% 0.66
Mean 0.59% 0.82 72% 0.64
stable revenue profiles, including WMT (0.42%), PG (0.43%),
JNJ (0.44%), KO (0.44%), and MCD (0.45%), cluster at the
low end regardless of sector classification, suggesting that
the predictability advantage stems from fundamental business
stability rather than broad sectoral factors. Energy stocks
occupy the highest error positions, with both XOM (1.10%)
and CVX (0.95%) exhibiting MAPE values roughly double
the universe mean, consistent with the dominant influence
of exogenous commodity price movements that the autoen-
coder’s feature-based reconstruction cannot fully anticipate.
Within sectors, meaningful variation persists: in healthcare,
JNJ (0.44%) substantially outperforms PFE (0.58%), plausibly
reflecting Pfizer’s heightened pipeline-driven volatility during
the test period; in technology, MSFT (0.50%) outperforms
both AAPL (0.62%) and CRM (0.63%), consistent with dif-
ferences in revenue diversification and product-cycle exposure.
Financial services exhibit a similar spread, where Visa’s stable
payment-processing model yields considerably lower error
(0.48%) than JPMorgan’s sensitivity to interest rate and credit
dynamics (0.70%). Although the sample of two to four stocks
per sector does not support formal statistical claims about
sectoral predictability, the consistency of observed patterns,
with both energy stocks at the top of the error distribution
and five defensive consumer and healthcare names clustered
near the bottom, suggests that stock-level characteristics such
as earnings stability, commodity exposure, and idiosyncratic
volatility interact with the regime detection mechanism in in-
terpretable ways. Theil’s U remains below 1.0 for all 20 stocks
without exception, confirming that the model outperforms
the naive random-walk baseline across the full predictability
spectrum. Directional accuracy ranges from 63% (XOM) to

12
78% (WMT), with every stock exceeding the 54% naive
long-only baseline reported in the main results, indicating
that the regime-aware routing mechanism provides meaningful
predictive signal even for the most volatile equities in the
universe.
F . Ablation Study
To quantify the contribution of each architectural compo-
nent, Table VII reports results from systematically removing
one component at a time, with all other components held
constant or adapted to the reduced architecture as described
below.
TheNo SACconfiguration removes the reinforcement
learning controller entirely, skipping Stage 3 of the training
pipeline. The autoencoder and dual node transformers re-
tain their Stage 1 and Stage 2 trained weights. The routing
threshold is fixed atτ=e 95, the 95th percentile of training-
set reconstruction errors, and the blending weight is held at
α= 0.5, assigning equal contribution to both pathways regard-
less of market conditions. This variant isolates the benefit of
adaptive parameter tuning from the architectural contributions
of regime-aware routing and pathway specialization.
TheNo Dual Pathsconfiguration replaces the two spe-
cialized node transformers with a single node transformer
that processes all data regardless of regime classification.
The single pathway retains the same architectural hyperpa-
rameters as each individual pathway in the full model (6
layers, 8 attention heads, 512 model dimension), so that
any performance difference reflects the architectural choice
of pathway specialization rather than a difference in model
capacity. The autoencoder is retained, and its reconstruction
errore t together with a binary regime indicator (determined
by thresholdτ) are concatenated to the single pathway’s input
feature vector, providing regime context without architectural
separation. The SAC controller remains active but operates
over a reduced action space: it adjusts onlyτto optimize
the anomaly detection threshold, since the blending weight
αis undefined when a single pathway produces the output.
This variant quantifies the value of allocating independent
representational capacity to normal and anomalous conditions,
as opposed to conditioning a shared pathway on a regime
signal.
TheNo AEconfiguration removes the autoencoder, which
cascades into removing dual-pathway routing and the SAC
controller, since both depend on the reconstruction error that
the autoencoder produces. The resulting system is a single
node transformer processing the standard feature set aug-
mented with BERT sentiment scores, architecturally equivalent
to the Integrated NodeFormer-BERT baseline from prior work
[5]. This configuration serves as the reference point from
which the incremental contributions of regime-aware routing,
pathway specialization, and adaptive control are jointly mea-
sured.
Autoencoder routing contributes most substantially, with
its removal increasing MAPE by 35.6% relative. This large
degradation reflects the fact that the autoencoder provides
the foundational regime signal upon which both pathway
TABLE VII
ABLATIONSTUDY: 1-DAYMAPE
Configuration MAPE∆vs Full
Full Model (AE + Dual NF + SAC) 0.59% –
No SAC (AE + Dual NF) 0.68% +15.3%
No Dual Paths (AE + Single NF + SAC) 0.63% +6.8%
No AE (Single NF + BERT, baseline) 0.80% +35.6%
routing and adaptive control depend; its removal eliminates
the entire regime-aware processing chain. The SAC controller
contributes the next largest improvement at 15.3%, confirming
that adaptive tuning ofτandαbased on prediction feedback
materially outperforms static initialization, particularly during
regime transitions where the optimal threshold and blending
weight shift over time. The dual-pathway architecture con-
tributes a smaller but meaningful 6.8% improvement, indicat-
ing that allocating independent weights to normal and anoma-
lous conditions yields better representations than conditioning
a single pathway on a binary regime indicator, even when both
configurations receive the same regime information from the
autoencoder. All components provide statistically significant
gains (p <0.01via paired t-tests across stock-day predictions).
G. Volatility Regime Analysis
To evaluate regime-specific performance, Table VIII disag-
gregates MAPE by VIX regime.
TABLE VIII
1-DAYMAPEBYVOLATILITYREGIME
Model Low VIX Medium VIX High VIX
iTransformer 0.72% 0.92% 1.42%
HMM-LSTM 0.78% 0.95% 1.35%
Integrated NodeFormer-BERT 0.70% 0.90% 1.50%
AE-NodeFormer (no SAC) 0.60% 0.75% 1.10%
AE-NodeFormer + SAC0.52% 0.65% 0.85%
The regime-specific results reveal an instructive pattern.
During low-VIX periods, iTransformer (0.72%) slightly out-
performs HMM-LSTM (0.78%), as the superior representa-
tional capacity of the transformer architecture dominates when
market dynamics are stable and regime detection adds limited
value. During high-VIX periods, this relationship reverses:
HMM-LSTM (1.35%) outperforms iTransformer (1.42%) be-
cause its regime-specific LSTMs adapt to volatile conditions
even though its overall architecture is less expressive. The
proposed model outperforms both across all VIX levels, main-
taining MAPE at 0.85% during high-volatility periods where
iTransformer reaches 1.42% and the Integrated NodeFormer-
BERT baseline reaches 1.50%. The 40% relative improvement
over iTransformer in high-VIX conditions, compared to 28%
overall, confirms that regime-aware processing is most valu-
able in precisely the conditions where accurate forecasts matter
most for risk management.
H. SAC Controller Behavior
Because the thresholdτand blending weightαvary across
the test period (Figure 9), it is important to specify precisely

13
what occurs at inference time and to address the resulting
implications for baseline comparability. After Stage 4 training
completes, all model weights are frozen, including the SAC
actor and critic networks. During testing, the actor network
operates as a fixed deterministic function: given the current
states t, it outputs[∆τ,∆α]through a single forward pass
with no gradient computation, no reward evaluation, and no
parameter update. The threshold and blending weight evolve
across the test period because theinputsto this fixed function
change (reconstruction errors rise during volatile markets,
recent prediction metrics shift), not because the policy itself
is modified. In this respect, the SAC policy at inference time
is functionally equivalent to any other feedforward neural
network applied to streaming data: its parameters are static,
but its outputs depend on input features that vary over time.
This state-dependent inference behavior is not unique to
the proposed framework. The HMM-LSTM baseline per-
forms analogous adaptive routing at test time: at each step,
the HMM’s forward algorithm computes regime posterior
probabilities using fixed transition and emission parameters
learned during training, and these probabilities determine
which regime-specific LSTM produces the forecast. The MS-
V AR baseline similarly infers time-varying regime probabil-
ities through its fixed Markov-switching parameters, adjust-
ing intercepts and error covariance accordingly. In all three
cases (the proposed SAC policy, the HMM, and the Markov-
switching model), a frozen statistical or neural model produces
time-varying routing decisions from fixed parameters applied
to changing inputs. The proposed framework thus does not
enjoy an online learning advantage relative to the regime-
switching baselines; rather, the three approaches represent
alternative designs for the same underlying capability of state-
dependent inference-time adaptation.
A separate question is whether state-dependent routing
confers an advantage over the purely static baselines (ARIMA,
Random Forest, LSTM, Simple Transformer, and others) that
apply fixed parameters uniformly across all market conditions.
It does, and this advantage is by design: the central thesis of
this work is that regime-aware processing improves prediction
quality. Crucially, the ablation study (Table VII) demonstrates
that this advantage does not depend on the SAC controller.
The AE-NodeFormer variant without SAC uses entirely static
routing parameters (τ=e 95,α= 0.5) and achieves 0.68%
MAPE, which already outperforms every baseline including
iTransformer (0.82%) and the Integrated NodeFormer-BERT
(0.80%). The architectural contributions of autoencoder-based
regime detection and dual-pathway specialization account for
the majority of the improvement, with the SAC controller
providing an additional 15.3% relative gain through its state-
dependent refinement of routing decisions. The comparison
between the static No SAC variant and the baselines is there-
fore on equal footing with respect to inference-time adaptation.
Regarding the state features themselves, the previous-day
prediction metrics (RMSE t−1, DA t−1) included in the SAC
state vector are computed by comparing the model’s day-
(t−1)forecast with the realized closing price, which is
publicly available at market open on dayt. This introduces
no information leakage: any practitioner would know whether
yesterday’s prediction was accurate before making today’s
forecast. The remaining state features (current reconstruction
errore t, recent error history¯e t−k:t, and market volatility
σt) are computed entirely from the model’s own outputs and
observable market data, with no access to future prices.
Figure 9 illustrates the threshold trajectory produced by
the frozen policy. During stable periods, the policy maps
low reconstruction errors to higher thresholds, routing most
data through the normal pathway. When volatility increases
and reconstruction errors rise, the same fixed policy maps
these elevated states to lower thresholds, directing more data
to the event pathway. The blending weightαfollows a
complementary pattern, reducing normal pathway contribution
during detected anomalies.
0 20 40 60 80 100
0
0.2
0.4
0.6
0.8
1
COVID 2022
Test Period (2017-2025)
Thresholdτ
Learnedτ
Staticτ(No SAC)
Fig. 9. Thresholdτproduced by the frozen SAC policy over the test period.
Dips correspond to volatile periods (COVID crash around index 35, 2022
market decline around index 75) where elevated reconstruction errors cause
the fixed policy to output lower threshold values, routing more data through
the event pathway. The dashed red line shows the static threshold (τ=e 95)
used in the No SAC ablation variant. All policy weights are frozen after
training; the trajectory reflects state-dependent outputs from a fixed function,
not online learning.
The threshold trajectory reveals interpretable behavior. Dur-
ing the pre-COVID period (2017-2019), the frozen policy
maps the prevailing low reconstruction errors to a relatively
high threshold (τ≈0.70-0.75), routing the majority of data
through the normal pathway. As the COVID crash unfolds
in early 2020, the spike in reconstruction errors causes the
policy to output large negative∆τadjustments, dropping
the threshold sharply to approximately 0.35 and activating
the event pathway for most stocks. Recovery is gradual: as
reconstruction errors slowly normalize, the policy produces
small positive adjustments that return the threshold to pre-
crisis levels over several months rather than snapping back,
reflecting the state-to-action mapping learned during training
between persistent elevated errors and cautious threshold re-
covery. A similar but less severe pattern occurs during the 2022
market decline. Importantly, the policy’s mapping was learned
entirely from training-period data; no crisis labels, test-period
supervision, or weight updates inform the threshold trajectory
shown in the figure. The frozen policy generalizes its learned
associations between reconstruction error patterns and routing
decisions to market events it has never encountered.
I. Statistical Significance
To confirm that the observed improvements are not at-
tributable to chance, Table IX presents paired t-test results

14
comparing daily squared errors.
TABLE IX
STATISTICALSIGNIFICANCE(n= 1,580TESTDAYS)
Comparisont-statisticp-value Cohen’sd
AE-NF+SAC vs Integrated NF-BERT−5.82<0.00010.46
AE-NF+SAC vs AE-NF (no SAC)−3.45 0.00060.27
AE-NF+SAC vs LSTM−7.21<0.00010.57
All comparisons achievep <0.001, with effect sizes
(Cohen’sd) ranging from 0.27 to 0.57 and indicating medium
practical significance. The largest effect size (0.57) appears in
the comparison against LSTM, which lacks both graph struc-
ture and regime awareness. The smallest effect size (0.27) is
between the full model and the non-adaptive AE-NodeFormer
variant, consistent with the SAC controller’s contribution being
a refinement over an already strong base architecture rather
than a wholesale improvement.
V. DISCUSSION
A. Interpretation of Results
Regime-aware prediction with adaptive control outperforms
homogeneous approaches across all metrics. The 26% MAPE
improvement over the baseline integrated model (0.59% vs
0.80%) reflects gains from three sources: regime detection (au-
toencoder), specialized processing (dual node transformers),
and adaptive parameter tuning (SAC controller).
Without requiring explicit per-sample anomaly labels, the
autoencoder identifies market states that deviate from normal
patterns. High reconstruction errors coincide with periods of
elevated volatility, earnings announcements, and macroeco-
nomic shocks, allowing the system to detect anomalies as
deviations from its learned representation of typical behavior.
The SAC controller learns to adjust the detection threshold
based on prediction outcomes, maintaining a higher threshold
during stable periods to prevent unnecessary routing to the
event pathway and lowering it during genuine regime shifts
to engage event-aware processing. This adaptive behavior
emerges from the reward signal rather than hand-crafted rules.
The dual-path architecture enables specialization: the nor-
mal pathway develops representations optimized for sta-
ble conditions where fundamental factors dominate, while
the event pathway incorporates additional context (sentiment
spikes, volatility regimes, event characterization) that proves
informative during turbulent periods but might add noise
during normal conditions.
B. Economic Interpretation
While the performance improvements carry practical im-
plications, they should be interpreted cautiously. A 7 per-
centage point improvement in directional accuracy (72% vs
65%) carries practical value for trading decisions, and the
43% relative improvement during high-volatility periods is
particularly valuable since these are precisely the conditions
where accurate forecasts matter most for risk management.
Transaction costs, market impact, and execution constraints
would reduce realized gains from any trading strategy based
on these predictions. The economic significance analysis in
prior work [5] demonstrated that even the baseline model’s
predictions, when combined with simple trading rules, gener-
ate returns exceeding buy-and-hold benchmarks before costs.
The improvements documented here should amplify these
returns proportionally, though the gap would narrow after
incorporating realistic trading frictions.
C. Limitations
The most consequential limitation concerns data selection.
The 20 stocks used in this study are drawn from the current
S&P 500 universe, which introduces survivorship bias: com-
panies that failed, were acquired, or delisted between 1982
and 2025 are absent from the dataset. Because the selected
stocks are disproportionately successful over the evaluation
period, predictability estimates may be inflated relative to
what a real-time investor would experience when choosing
from the full market. Performance on a point-in-time universe
constructed from historical index constituents could differ,
and the reported results should therefore be interpreted as
evidence of architectural capability rather than guaranteed
trading performance.
Several data-related concerns compound this issue. Edge
weights in the graph are initialized from correlations computed
over the training period (1982-2010), but market correlations
are non-stationary, and relationships that held during this
window may weaken or reverse by the test period (2017-2025).
The learnable edge refinement mechanism partially compen-
sates by adapting weights during training, though fundamental
correlation regime shifts could still affect generalization. Sen-
timent data from X (formerly Twitter) is available only from
2007 onward; for the 1982-2006 portion of training, sentiment
features are set to zero. This means the sentiment modality
effectively “turns on” partway through training, potentially
limiting the model’s ability to learn robust sentiment-price
relationships from the earlier decades.
On the modeling side, the reinforcement learning controller
requires careful tuning of reward weights, temperature, and
network architecture, and suboptimal configurations could
lead to unstable threshold behavior or poor convergence. The
system also learns regime boundaries from its own prediction
performance, which risks feedback loops where poor initial
predictions lead to suboptimal threshold learning; the staged
training protocol mitigates this by pre-training each component
before SAC optimization, but the circularity is not fully
eliminated. The three-component architecture increases com-
putational requirements, with training time approximately 33%
longer than the baseline model, which may constrain real-time
deployment. Although the SAC policy weights are frozen at
inference time, the state-dependent routing decisions produced
by the fixed policy constitute a form of adaptive processing
that purely static baselines (ARIMA, Random Forest, LSTM)
do not possess. The regime-switching baselines (HMM-LSTM,
MS-V AR) share this property, and the ablation study confirms
that the static No SAC variant already outperforms all base-
lines, but the additional gain from state-dependent threshold
tuning should be interpreted as an architectural advantage of

15
the framework rather than an improvement attributable solely
to prediction accuracy.
From an economic standpoint, the analysis excludes trans-
action costs, market impact, and execution constraints. For
strategies involving frequent rebalancing, these frictions would
reduce realized returns. Backtesting is performed on the same
20-stock universe used for model development, leaving ex-
ternal validity on unseen stocks untested. Finally, sentiment
data was collected via the X (formerly Twitter) API, which
has undergone significant access policy changes, making ex-
act replication of the sentiment component challenging with
current API limitations.
D. Future Directions
Several extensions could address the limitations identified
above. Expanding the stock universe to include historical index
constituents would mitigate survivorship bias. Automated SAC
hyperparameter tuning via meta-learning could reduce config-
uration sensitivity. More efficient architectures would enable
real-time deployment, and strictly online regime detection
without training-period VIX percentiles would eliminate any
residual look-ahead.
Beyond addressing limitations, incorporating multiple au-
toencoders for different anomaly types (e.g., separating liquid-
ity crises from earnings shocks) could refine regime classifica-
tion. Extending the framework to portfolio optimization, where
regime-aware allocation could improve risk-adjusted returns,
represents a natural application. Transfer learning to adapt the
system to new markets or asset classes without full retraining
would broaden practical applicability.
VI. CONCLUSION
This paper introduced an adaptive framework for stock
price prediction that automatically detects market regimes
and adjusts processing accordingly. The architecture combines
an autoencoder for regime detection, dual node transformer
networks specialized for stable and volatile conditions, and a
Soft Actor-Critic reinforcement learning controller that learns
adaptive regime thresholds from prediction performance.
Experiments on 20 S&P 500 stocks spanning 1982-2025
demonstrate substantial improvements over prior approaches:
the complete system achieves 0.59% MAPE for one-day
predictions compared to 0.80% for the baseline integrated
node transformer, while directional accuracy reaches 72%, a
7 percentage point improvement. These gains persist across
prediction horizons and are most pronounced during volatile
periods where the baseline struggles.
The key conceptual contribution is the adaptive learning
of regime boundaries. Rather than relying solely on fixed
hand-crafted anomaly definitions, the system discovers useful
boundaries by optimizing downstream prediction accuracy.
This approach avoids the staleness problem of hand-crafted
regime rules and the labeling burden of supervised regime
classification.
Future work should validate the framework on broader uni-
verses, develop more efficient implementations for real-time
deployment, and explore extensions to portfolio optimization
and risk management applications.
APPENDIX
Table X reports the hyperparameter search space explored
for each baseline model. All searches were conducted via grid
search on the validation set (2011–2016), with the configu-
ration yielding the lowest validation MAPE selected for test
evaluation.
TABLE X
HYPERPARAMETERSEARCHRANGES ANDSELECTEDVALUES FOR
BASELINEMODELS
Model Hyperparameter Search Range Selected
ARIMA
AR order (p){0,1,2,3,4,5}Per stock (AIC)
Differencing (d){0,1,2}Per stock (AIC)
MA order (q){0,1,2,3,4,5}Per stock (AIC)
Selection criterion AIC, BIC AIC
V AR
Lag order{1,2,3, . . . ,10}3
Trend{none, constant, both}constant
Selection criterion AIC, BIC BIC
Random Forest
Number of estimators{100,200,500}200
Maximum depth{5,10,15,20,None}15
Min samples split{2,5,10}5
Min samples leaf{1,2,4}2
Max features{
√
d,log 2(d),0.5}
√
d
SVR
Kernel RBF (fixed) RBF
Regularization (C){0.1,1,10,100}10
Kernel width (γ){scale,0.01,0.1}scale
Epsilon (ϵ){0.01,0.05,0.1}0.05
XGBoost
Number of estimators{100,500,1000}500
Maximum depth{3,5,7,10}7
Learning rate{0.01,0.05,0.1}0.05
Subsample ratio{0.7,0.8,0.9,1.0}0.8
Column sample ratio{0.7,0.8,0.9,1.0}0.8
Min child weight{1,3,5}3
L1 regularization (α){0,0.01,0.1}0.01
L2 regularization (λ){1,1.5,2}1.5
LSTM
Hidden dimension{64,128,256,512}256
Number of layers{1,2,3}2
Dropout{0.1,0.2,0.3}0.2
Learning rate{10 −4,5×10 −4,10 −3}5×10 −4
Batch size{32,64}64
Sequence length 252 (fixed) 252
Simple
Transformer
Layers{4,6,8}6
Attention heads{4,8}8
Model dimension{256,512}512
FFN dimension{1024,2048}2048
Dropout{0.1,0.2}0.1
Learning rate{10 −4,5×10 −4,10 −3}10 −4
BERT Sentiment
+ LSTM
LSTM hidden dimension{128,256,512}256
LSTM layers{1,2}2
Sentiment fusion{concat., gated}concatenation
Dropout{0.1,0.2,0.3}0.2
Learning rate{10 −4,5×10 −4}10 −4
MS-V AR
Number of regimes (K){2,3,4}3
Lag order{1,2,3, . . . ,10}3
Switching specification{MSI, MSM, MSIH}MSIH
EM convergence tolerance{10 −6,10 −8}10 −8
HMM-LSTM
HMM states (K){2,3,4}3
HMM covariance{diag., full}diagonal
LSTM hidden dimension{128,256,512}256
LSTM layers{1,2,3}2
Dropout{0.1,0.2,0.3}0.2
Learning rate{10 −4,5×10 −4,10 −3}5×10 −4
Sequence length 252 (fixed) 252
TimesNet
Layers{2,3,4}3
Model dimension{32,64,128}64
Top-kperiods{3,5,7}5
FFN dimension{64,128,256}128
Dropout{0.1,0.2,0.3}0.2
Learning rate{10 −4,5×10 −4,10 −3}10 −4
Sequence length 252 (fixed) 252
PatchTST
Patch length{12,16,24}16
Stride{8,12,16}8
Layers{3,4,6}4
Attention heads{4,8}8
Model dimension{128,256,512}256
Dropout{0.1,0.2,0.3}0.2
Learning rate{10 −4,5×10 −4,10 −3}10 −4
iTransformer
Layers{3,4,6}4
Attention heads{4,8}8
Model dimension{128,256,512}256
FFN dimension{256,512,1024}512
Dropout{0.1,0.2}0.1
Learning rate{10 −4,5×10 −4,10 −3}10 −4
Integrated NF-BERT Architecture and hyperparameters fixed per [5].
For ARIMA, optimal orders vary across stocks because each
stock exhibits different autocorrelation and partial autocorre-
lation structure; the most common selections were(p, d, q) =
(2,1,2)and(1,1,1). XGBoost uses early stopping with a

16
patience of 50 rounds on validation RMSE, so the effective
number of estimators is often lower than the specified max-
imum. The LSTM and Simple Transformer sequence lengths
are fixed at 252 trading days (one calendar year) to match
the proposed model’s input window, ensuring that differences
in performance reflect architectural capacity rather than infor-
mation asymmetry. The MS-V AR uses the MSIH specification
(Markov-switching intercept and heteroscedasticity), which al-
lows both the intercept and the error variance to switch across
regimes while keeping the autoregressive coefficients regime-
invariant; this provides sufficient flexibility to capture volatility
regime changes without overfitting the transition dynamics.
For the HMM-LSTM, regime assignments are determined
by the Viterbi path on the training set, and each regime-
specific LSTM is trained only on data segments assigned
to its corresponding state. PatchTST and iTransformer use
the channel-independent and inverted-attention configurations
recommended in their respective original publications, with
sequence lengths fixed at 252 to match other deep learning
baselines.
REFERENCES
[1] J. D. Hamilton, “A new approach to the economic analysis of nonsta-
tionary time series and the business cycle,”Econometrica, vol. 57, no. 2,
pp. 357–384, 1989.
[2] W. Chen, M. Jiang, W.-G. Zhang, and Z. Chen, “A novel graph
convolutional feature based convolutional neural network for stock trend
prediction,”Information Sciences, vol. 556, pp. 67–94, 2021.
[3] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” inAdvances in
Neural Information Processing Systems, vol. 30, 2017, pp. 5998–6008.
[4] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-
training of deep bidirectional transformers for language understanding,”
inProceedings of the Conference of the North American Chapter of the
Association for Computational Linguistics, 2019, pp. 4171–4186.
[5] M. A. Al Ridhawi, M. Haj Ali, and H. Al Osman, “Stock market
prediction using node transformer architecture integrated with BERT
sentiment analysis,”Submitted to IEEE Access, 2026, under review.
arXiv:2603.05917.
[6] Z. Liu, J. Liu, Q. Zeng, and L. Wu, “VIX and stock market volatility
predictability: A new approach,”Finance Research Letters, vol. 48, p.
102887, 2022.
[7] F. X. Diebold, J.-H. Lee, and G. C. Weinbach, “Regime switching
with time-varying transition probabilities,”Business Cycles: Durations,
Dynamics, and Forecasting, pp. 144–165, 1994.
[8] H. Tong,Non-linear time series: A dynamical system approach. Oxford
University Press, 1990.
[9] P. Nystrup, H. Madsen, and E. Lindstr ¨om, “Regime-based versus static
asset allocation: Letting the data speak,”The Journal of Portfolio
Management, vol. 44, no. 1, pp. 103–115, 2017.
[10] S. Aminikhanghahi and D. J. Cook, “A survey of methods for time series
change point detection,”Knowledge and Information Systems, vol. 51,
no. 2, pp. 339–367, 2017.
[11] G. E. Hinton and R. R. Salakhutdinov, “Reducing the dimensionality of
data with neural networks,”Science, vol. 313, no. 5786, pp. 504–507,
2006.
[12] D. P. Kingma and M. Welling, “Auto-encoding variational Bayes,” in
International Conference on Learning Representations, 2014.
[13] A. Pumsirirat and L. Yan, “Credit card fraud detection using deep
learning based on auto-encoder and restricted Boltzmann machine,”
International Journal of Advanced Computer Science and Applications,
vol. 9, no. 1, pp. 18–25, 2018.
[14] M. Ahmed, A. N. Mahmood, and J. Hu, “A survey of network anomaly
detection techniques,”Journal of Network and Computer Applications,
vol. 60, pp. 19–31, 2016.
[15] W. Bao, J. Yue, and Y . Rao, “A deep learning framework for financial
time series using stacked autoencoders and long-short term memory,”
PLOS ONE, vol. 12, no. 7, p. e0180944, 2017.
[16] M. Liu, H. Sheng, N. Zhanget al., “A new deep network model for stock
price prediction,” inInternational Conference on Machine Learning for
Cyber Security, 2022, pp. 413–426.
[17] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and S. Y . Philip, “A
comprehensive survey on graph neural networks,”IEEE Transactions
on Neural Networks and Learning Systems, vol. 32, no. 1, pp. 4–24,
2020.
[18] C. Wang, H. Liang, B. Wang, X. Cui, and Y . Xu, “MG-Conv: A spa-
tiotemporal multi-graph convolutional neural network for stock market
index trend prediction,”Computers and Electrical Engineering, vol. 103,
p. 108285, 2022.
[19] Q. Wu, W. Zhao, Z. Li, D. P. Wipf, and J. Yan, “Nodeformer: A scalable
graph structure learning transformer for node classification,” inAdvances
in Neural Information Processing Systems, vol. 35, 2022, pp. 27 387–
27 401.
[20] R. S. Sutton and A. G. Barto,Reinforcement learning: An introduction,
2nd ed. MIT Press, 2018.
[21] Z. Jiang, D. Xu, and J. Liang, “A deep reinforcement learning frame-
work for the financial portfolio management problem,”arXiv preprint
arXiv:1706.10059, 2017.
[22] Z. Ning, P. Dong, X. Wang, X. Hu, L. Guo, B. Hu, R. Y . K. Kwok, and
V . C. M. Leung, “A double deep Q-learning model for energy-efficient
edge scheduling,”IEEE Transactions on Services Computing, vol. 14,
no. 5, pp. 1555–1566, 2021.
[23] Y . Deng, F. Bao, Y . Kong, Z. Ren, and Q. Dai, “Deep direct rein-
forcement learning for financial signal representation and trading,”IEEE
Transactions on Neural Networks and Learning Systems, vol. 28, no. 3,
pp. 653–664, 2016.
[24] V . Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G.
Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski
et al., “Human-level control through deep reinforcement learning,”
Nature, vol. 518, no. 7540, pp. 529–533, 2015.
[25] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, “Soft actor-critic: Off-
policy maximum entropy deep reinforcement learning with a stochastic
actor,” inInternational Conference on Machine Learning. PMLR, 2018,
pp. 1861–1870.
[26] T. Haarnoja, A. Zhou, K. Hartikainen, G. Tucker, S. Ha, J. Tan,
V . Kumar, H. Zhu, A. Gupta, P. Abbeel, and S. Levine, “Soft actor-critic
algorithms and applications,”arXiv preprint arXiv:1812.05905, 2019.
[27] A. Ang and G. Bekaert, “International asset allocation with regime
shifts,”The Review of Financial Studies, vol. 15, no. 4, pp. 1137–1187,
2002.
[28] M. Guidolin and A. Timmermann, “Asset allocation under multivariate
regime switching,”Journal of Economic Dynamics and Control, vol. 31,
no. 11, pp. 3503–3544, 2007.
[29] T. Fischer and C. Krauss, “Deep learning with long short-term memory
networks for financial market predictions,”European Journal of Oper-
ational Research, vol. 270, no. 2, pp. 654–669, 2018.
[30] K. Cortis, A. Freitas, T. Daudert, M. Huerlimann, M. Zarrouk, S. Hand-
schuh, and B. Davis, “SemEval-2017 task 5: Fine-grained sentiment
analysis on financial microblogs and news,” inProceedings of the 11th
International Workshop on Semantic Evaluation (SemEval-2017), 2017,
pp. 519–535.
[31] H.-M. Krolzig,Markov-Switching Vector Autoregressions: Modelling,
Statistical Inference, and Application to Business Cycle Analysis.
Berlin: Springer-Verlag, 1997.
[32] H. Wu, T. Hu, Y . Liu, H. Zhou, J. Wang, and M. Long, “TimesNet:
Temporal 2d-variation modeling for general time series analysis,” in
Proceedings of the 11th International Conference on Learning Repre-
sentations (ICLR), 2023.
[33] Y . Nie, N. H. Nguyen, P. Sinthong, and J. Kalagnanam, “A time series is
worth 64 words: Long-term forecasting with transformers,” inProceed-
ings of the 11th International Conference on Learning Representations
(ICLR), 2023.
[34] Y . Liu, T. Hu, H. Zhang, H. Wu, S. Wang, L. Ma, and M. Long, “iTrans-
former: Inverted transformers are effective for time series forecasting,”
inProceedings of the 12th International Conference on Learning Rep-
resentations (ICLR), 2024.
[35] G. E. P. Box and G. M. Jenkins,Time Series Analysis: Forecasting and
Control. San Francisco: Holden-Day, 1976.
[36] C. A. Sims, “Macroeconomics and reality,”Econometrica, vol. 48, no. 1,
pp. 1–48, 1980.
[37] L. Breiman, “Random forests,”Machine Learning, vol. 45, no. 1, pp.
5–32, 2001.
[38] V . N. Vapnik,The Nature of Statistical Learning Theory. New York:
Springer, 1995.

17
[39] T. Chen and C. Guestrin, “XGBoost: A scalable tree boosting system,”
inProceedings of the 22nd ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining, 2016, pp. 785–794.
[40] S. Hochreiter and J. Schmidhuber, “Long short-term memory,”Neural
Computation, vol. 9, no. 8, pp. 1735–1780, 1997.
[41] F. X. Diebold and R. S. Mariano, “Comparing predictive accuracy,”
Journal of Business & Economic Statistics, vol. 13, no. 3, pp. 253–263,
1995.
Mohammad Al Ridhawireceived the B.A.Sc. de-
gree in computer engineering and the M.Sc. degree
in digital transformation and innovation (machine
learning) from the University of Ottawa, Ottawa,
Canada, in 2019 and 2021, respectively. He is cur-
rently pursuing the Ph.D. degree in electrical and
computer engineering at the University of Ottawa,
where he also serves as a Part-Time Engineering
Professor. He has industry experience as a Senior
Data Scientist and Senior Machine Learning Engi-
neer, building production ML systems in financial
and environmental domains. His research interests include deep learning,
graph neural networks, natural language processing, financial time series
analysis, and reinforcement learning.
Mahtab Haj Alireceived the M.Sc. degree in digital
transformation and innovation from the University
of Ottawa, Ottawa, Canada, in 2021. She is cur-
rently pursuing the Ph.D. degree in electrical and
computer engineering at the University of Ottawa,
with a research focus on time series forecasting
and deep learning models. She works as an AI
Research Engineer at the National Research Council
of Canada, where she builds and evaluates large
language models (LLMs) and develops AI-driven
solutions for real-world industrial applications. Her
work includes large-scale time series analysis, advanced feature engineering,
and the application of LLMs in production environments. Her research
interests include deep learning for time series analysis, deep neural networks,
and applied artificial intelligence.
Hussein Al Osmanreceived the B.A.Sc., M.A.Sc.,
and Ph.D. degrees from the University of Ottawa,
Ottawa, Canada. He is an Associate Professor and
Associate Director in the School of Electrical En-
gineering and Computer Science at the University
of Ottawa, where he leads the Multimedia Process-
ing and Interaction Group. His research focuses on
affective computing, multimodal affect estimation,
human–computer interaction, serious gaming, and
multimedia systems. He has produced over 50 peer-
reviewed research articles, two patents, and several
technology transfers to industry.
