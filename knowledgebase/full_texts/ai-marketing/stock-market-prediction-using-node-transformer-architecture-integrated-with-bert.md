---
title: Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis
url: https://arxiv.org/abs/2603.05917
category: ai-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Mohammad Al Ridhawi
- Mahtab Haj Ali
- Hussein Al Osman
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.05917
pages: 18
chars: 99199
fetched_at: '2026-11-08T13:01:46+00:00'
kb_version: 1
---

# Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis

1
Accepted for publication in IEEE Access. DOI: 10.1109/ACCESS.2026.3691980. © 2026 IEEE.
Stock Market Prediction Using Node Transformer
Architecture Integrated with BERT Sentiment
Analysis
Mohammad Al Ridhawi, Mahtab Haj Ali, and Hussein Al Osman
School of Electrical Engineering and Computer Science,
University of Ottawa, Ottawa, Canada
e-mail: malri039@uottawa.ca
Abstract—Stock market prediction presents considerable chal-
lenges for investors, financial institutions, and policymakers
operating in complex market environments characterized by
noise, non-stationarity, and behavioral dynamics. Traditional
forecasting methods, including fundamental analysis and tech-
nical indicators, often fail to capture the intricate patterns
and cross-sectional dependencies inherent in financial markets.
This paper presents an integrated framework combining a node
transformer architecture with Bidirectional Encoder Represen-
tations from Transformers (BERT)-based sentiment analysis for
stock price forecasting. The proposed model represents the stock
market as a graph structure where individual stocks form nodes
and edges capture relationships including sectoral affiliations,
correlated price movements, and supply chain connections. A
fine-tuned BERT model extracts sentiment information from
social media posts and combines it with quantitative market
features through attention-based fusion mechanisms. The node
transformer processes historical market data while capturing
both temporal evolution and cross-sectional dependencies among
stocks. Experiments conducted on 20 S&P 500 stocks spanning
January 1982 to March 2025 demonstrate that the integrated
model achieves a mean absolute percentage error (MAPE) of
0.80% for one-day-ahead predictions, compared to 1.20% for
ARIMA and 1.00% for LSTM. The inclusion of sentiment
analysis reduces prediction error by 10% overall and 25% during
earnings announcements, while the graph-based architecture con-
tributes an additional 15% improvement by capturing inter-stock
dependencies. Directional accuracy reaches 65% for one-day
forecasts. Statistical validation through paired t-tests confirms the
significance of these improvements (p <0.05for all comparisons).
The model maintains lower error during high-volatility periods,
achieving MAPE of 1.50% while baseline models range from
1.60% to 2.10%.
Index Terms—Stock price forecasting, node transformer,
BERT, sentiment analysis, graph neural networks, financial time
series, deep learning, multimodal fusion.
I. INTRODUCTION
S
TOCK price forecasting represents a fundamental chal-
lenge in quantitative finance with substantial implications
for portfolio management, risk assessment, and capital allo-
cation [1]. The task of predicting stock market movements is
complicated by several interconnected factors: non-stationary
price dynamics, high-dimensional feature spaces, complex
inter-stock dependencies, and the influence of investor psy-
chology on market behavior.
A. Challenges in Stock Price Forecasting
A primary challenge in financial forecasting is the presence
of noise and irregularities in market data. Microstructure noise,
arising from bid-ask bounces and discrete price movements,
significantly impacts short-term price observations [2]. Ran-
dom fluctuations that do not reflect fundamental changes
in asset value can obscure meaningful signals, complicating
model training and evaluation. The efficient market hypothesis
posits that stock prices incorporate all available information,
suggesting that consistently outperforming market benchmarks
through prediction is theoretically difficult [1]. Empirical ev-
idence indicates partial efficiency, with information incorpo-
rated into prices at varying speeds depending on asset liquidity,
market conditions, and information type [3], [4].
Behavioral factors introduce additional complexity. Investor
sentiment and cognitive biases lead to market movements not
easily explained by quantitative fundamentals alone [5]. Fear,
greed, and herd behavior drive price fluctuations in patterns
that resist traditional modeling approaches. These behavioral
dynamics manifest particularly during market stress, when
correlations among assets increase and volatility clusters tem-
porally.
The regulatory environment compounds these difficulties.
Shifts in financial regulations, monetary policy, and fiscal
interventions can trigger sudden market movements that in-
validate learned patterns. The 2008 financial crisis and 2020
pandemic response demonstrated how policy actions create
discontinuities in price dynamics that historical models may
not anticipate.
B. Existing Approaches
Current approaches to stock price forecasting span multi-
ple methodological traditions. Fundamental analysis evaluates
company financial health and market position to estimate
intrinsic value [6]. Technical analysis examines historical price
arXiv:2603.05917v3  [cs.LG]  14 May 2026

2
and volume patterns to identify trading signals. Machine learn-
ing methods, including support vector machines and ensemble
methods, apply algorithms to discover patterns in feature-
engineered datasets [2].
Deep learning architectures have demonstrated particular
promise in capturing temporal dependencies. Recurrent neu-
ral networks, especially Long Short-Term Memory (LSTM)
networks, model sequential data through gating mechanisms
that address vanishing gradient problems [7]. While effec-
tive for short-to-medium range dependencies, LSTMs pro-
cess sequences step by step, which limits their ability to
capture interactions between distant time steps efficiently.
The transformer architecture [8] overcomes this limitation
through self-attention mechanisms that relate all positions
in a sequence directly, enabling explicit modeling of long-
range dependencies without recurrent connections. In parallel,
graph neural networks have emerged to address a different
shortcoming: the inability of standard sequence models to rep-
resent relationships between entities [9]. The node transformer
architecture bridges these two lines of work by combining
attention mechanisms with graph structure, learning contex-
tualized node representations through attention applied over
graph neighborhoods [10].
C. Research Motivation and Contributions
These advances notwithstanding, the literature reveals per-
sistent shortcomings. Few approaches combine graph-based
modeling of inter-stock relationships with transformer archi-
tectures for temporal modeling. The integration of unstruc-
tured textual data, particularly social media sentiment, with
structured numerical data remains limited. Performance often
deteriorates during volatile market conditions, with accuracy
varying substantially between stable and turbulent periods.
This paper presents an integrated framework addressing
these gaps through multiple coordinated components:
1) A node transformer architecture adapted for stock price
forecasting that represents the market as a dynamic
graph with learnable edge weights. The model cap-
tures interdependencies among stocks including sectoral
relationships, correlated price movements, and supply
chain connections while processing multivariate stock-
level inputs.
2) Integration of Bidirectional Encoder Representations
from Transformers (BERT)-based sentiment analysis
through multimodal fusion, enabling incorporation of
qualitative market sentiment alongside quantitative price
and volume data. Sentiment information extracted from
social media posts is incorporated as additional features
for each stock node.
3) An attention-based fusion mechanism that dynamically
weights price-based features and sentiment signals based
on current market conditions and volatility indicators.
4) A comprehensive dataset comprising historical prices for
20 S&P 500 companies from January 1982 to March
2025, augmented with sentiment scores derived from
social media posts from 2007 onward.
5) Extensive experimental validation across different mar-
ket conditions, prediction horizons, and volatility
regimes, with statistical tests confirming significance of
performance improvements.
The remainder of this paper is organized as follows. Sec-
tion II reviews related work. Section III describes datasets and
preprocessing. Section IV presents the methodology. Section V
reports experimental results. Section VI discusses findings
and limitations. Section VII concludes and outlines future
directions.
II. LITERATUREREVIEW
Stock price forecasting has evolved through statistical mod-
eling, machine learning, and deep learning paradigms, each
offering distinct trade-offs between interpretability, capacity,
and data requirements. The following subsections trace this
progression and identify the gaps that motivate the present
work.
A. Statistical Methods
Autoregressive Integrated Moving Average (ARIMA) mod-
els remain widely used due to their capacity to capture linear
temporal dependencies and interpretable coefficient structures.
ARIMA combines autoregressive (AR) and moving average
(MA) components after differencing to achieve stationarity.
The ARIMA(p, d, q)model is specified as:
ϕ(B)(1−B) dXt =θ(B)ϵ t (1)
whereBis the backshift operator such thatBX t =X t−1,
ϕ(B) = 1−ϕ 1B− · · · −ϕpBp is the AR polynomial of order
p,θ(B) = 1 +θ 1B+· · ·+θqBq is the MA polynomial of
orderq,dis the differencing order, andϵ t ∼ N(0, σ2)is white
noise.
Low and Sakk [11] compared ARIMA and LSTM networks
for stock prediction across ten exchange-traded funds, finding
that ARIMA demonstrates comparable accuracy to LSTM
for longer-term predictions. Wahyudi [12] applied ARIMA to
Indonesian stock prices, demonstrating effectiveness for short-
term volatility prediction with model selection via the Akaike
Information Criterion (AIC).
Vector Autoregression (V AR) extends univariate ARIMA
to multivariate settings, modeling each variable as a linear
function of its own lags and lags of other variables. However,
ARIMA and V AR are limited in handling nonlinear dynamics,
regime shifts, and high-dimensional interactions.
B. Classical Machine Learning
Support Vector Machines (SVM), k-Nearest Neighbors
(KNN), and ensemble methods leverage engineered features
for prediction. Nayak et al. [13] developed a hybrid SVM-
KNN model for Indian stock market indices, outperforming
individual models in mean squared error. Siddique and Panda
[14] combined kernel Principal Component Analysis (PCA)
with Support Vector Regression (SVR) and teaching-learning-
based optimization, achieving improved accuracy through di-
mension reduction.
Basak et al. [15] applied XGBoost for long-term stock
price forecasting using technical indicators, achieving F-scores

3
ranging from 0.82 to 0.97 for 60-day and 90-day prediction
horizons on Apple and Yahoo stocks. While effective for
specific tasks, these methods rely heavily on feature engineer-
ing and often struggle to generalize across different market
regimes.
C. Deep Learning Methods
1) Convolutional Neural Networks:Convolutional Neural
Networks (CNNs) extract hierarchical patterns from structured
data through local receptive fields and parameter sharing.
Chandar [16] proposed TI-CNN, converting technical indica-
tors into images using Gramian Angular Fields before CNN
processing. Wen et al. [17] applied CNNs to S&P 500 data, ex-
ploiting spatial structure in time series representations. CNNs
capture local dependencies effectively but are less suited for
modeling long-range temporal dynamics.
2) Recurrent Neural Networks:Recurrent Neural Networks
(RNNs), particularly LSTM networks and Gated Recurrent
Units (GRU), model sequential data through hidden states that
propagate information across time steps. LSTM networks in-
corporate input, forget, and output gates to control information
flow, addressing the vanishing gradient problem inherent in
standard RNNs.
Di Persio and Honchar [18] compared RNN variants for
Google stock prediction, with LSTM achieving 72% direc-
tional accuracy, outperforming standard RNN and GRU archi-
tectures. Hossain et al. [19] applied cascaded LSTM-GRU to
S&P 500 data spanning 1950-2016, achieving mean squared
error of 0.00098. Bidirectional LSTM extends this by pro-
cessing sequences in both directions. Xu et al. [20] integrated
wavelet transform, stacked autoencoder, and BiLSTM for
stock forecasting. Liu et al. [21] employed autoencoder-based
feature extraction with BiLSTM for price series prediction.
D. Graph Neural Networks
Graph Neural Networks (GNNs) capture interdependen-
cies by modeling markets as graphs where nodes represent
companies and edges represent relationships such as sec-
toral ties, price correlations, or supply chain connections.
Kipf and Welling [22] introduced the graph convolutional
network (GCN) framework, which aggregates features from
neighboring nodes through symmetric normalization of the
adjacency matrix, providing a scalable approach to semi-
supervised learning on graph-structured data. This founda-
tional architecture enabled subsequent applications to financial
markets, where inter-stock relationships form natural graph
topologies.
Chen et al. [23] proposed a graph convolutional feature-
based CNN model combining graph convolutional networks
with dual CNNs to capture market-level and stock-level fea-
tures simultaneously. Testing on Chinese stocks demonstrated
superior performance compared to non-graph approaches.
Wang et al. [24] introduced a multi-graph convolutional neural
network defining both static and dynamic correlation graphs.
Testing on 42 Chinese market indices showed average pre-
diction error reduction of 5.11% compared to LSTM and
attention-based baselines. Beyond equity markets, graph-based
forecasting methods have been applied to other financial
domains. Le et al. [25] developed an entropy-based GCN
framework for real estate market prediction that segments
spatial regions into anomalous and normal clusters before ap-
plying separate forecasting models, reducing prediction error
across multiple horizons on U.S., U.K., and Australian housing
data. A related study by Le et al. [26] combined entropy-
based multivariate clustering with sentiment extracted from
news headlines and macroeconomic indicators, demonstrating
that this segmentation approach improves forecasting accuracy
when paired with deep learning architectures such as trans-
formers and LSTMs. These cross-domain results underscore
the generality of graph-based representations for capturing
complex dependencies in financial data.
E. Transformer Models
The transformer architecture [8] introduced a fundamentally
different approach to sequence-to-sequence modeling. Self-
attention mechanisms compute pairwise interactions between
all positions:
Attention(Q,K,V) =softmax
 QKT
√dk

V(2)
whereQ,K,Vare query, key, and value matrices, and
dk is the key dimension. The scaling factor √dk prevents dot
products from growing large in magnitude.
Multi-head attention extends this by projecting queries,
keys, and values multiple times with different learned pro-
jections:
MultiHead(Q,K,V) =Concat(head 1, . . . ,headh)WO (3)
where head i =Attention(QW Q i ,KW K i ,VW V i ).
Li and Qian [27] developed a financial transformer process-
ing multiple timeframes simultaneously, improving sensitivity
to regime changes. The node transformer [10] extends at-
tention to graph-structured data, learning contextualized node
representations through attention over graph neighborhoods.
F . Hybrid Models and Research Gaps
Hybrid models seek to integrate complementary architec-
tural strengths by pairing spatial feature extractors with se-
quential learners. Lu et al. [28] proposed a CNN-BiLSTM-
attention model that uses convolutional layers to extract local
patterns, feeds them into a bidirectional LSTM for temporal
modeling, and applies attention to weight the most informative
time steps, outperforming standalone approaches on multiple
benchmarks. These composite designs show particular promise
during volatile periods, where the diversity of learned rep-
resentations confers robustness that single-paradigm models
lack.
More recent work has explored integrating transformer at-
tention with sentiment signals and privacy-preserving training
strategies. Nejatbakhsh and Aliasgari [29] combined LSTM
networks with transformer-based attention and FinBERT-
derived sentiment in a federated learning framework, achieving

4
an averageR 2 of 0.91 across ten technology stocks. Their
approach demonstrated that sentiment integration improves
short-term forecasting accuracy, though the architecture treats
each stock independently without modeling inter-stock re-
lationships, and the evaluation was restricted to a single
sector. These findings reinforce the value of multimodal fusion
while highlighting the continued need for architectures that
simultaneously capture cross-asset dependencies.
Despite progress along each of these fronts, critical gaps
persist at their intersections. Few approaches combine graph-
based inter-stock modeling with transformer temporal process-
ing within a unified architecture. While sentiment integration
has been explored alongside recurrent and attention-based
models, simultaneous learning of inter-stock graph structure,
long-range temporal patterns, and textual sentiment remains
largely unaddressed. Performance often deteriorates during
volatile conditions, with accuracy varying by 40% between
stable and turbulent periods [11]. Computational demands
present additional barriers to real-time deployment.
The present work addresses these gaps through integration
rather than through the introduction of a fundamentally new
learning primitive. Each individual component, namely graph
structure learning, transformer-based attention, and BERT sen-
timent analysis, draws on established techniques. The con-
tribution lies in the architectural design required to com-
bine them within a single end-to-end framework. The node
transformer must compute attention simultaneously across
temporal positions and graph neighborhoods, which requires
adapting the standard self-attention mechanism to operate over
a three-dimensional input tensor rather than a flat sequence.
The adaptive gating mechanism that fuses continuous sen-
timent scores with numerical price features handles tempo-
ral sparsity and missing data without degrading the price-
based pathway, a challenge that simple feature concatenation
does not address. The jointly learned edge weights provide
an interpretable structural layer connecting model internals
to domain knowledge about market relationships, offering
a qualitative advantage that pure performance comparisons
cannot capture. This integrative design philosophy follows a
productive tradition in deep learning, where combining known
components in carefully engineered architectures has yielded
substantial advances over any single technique deployed in
isolation.
III. DATASETS ANDPREPROCESSING
A. Financial Market Dataset
The Financial Market Dataset (FMD) integrates historical
stock market data with engineered technical indicators. The
dataset spans January 1, 1982 to March 31, 2025, covering
twenty companies from the S&P 500 index selected for
sectoral diversity, market capitalization variation, and data
availability.
The selected companies span multiple sectors: technology
(Apple, Microsoft, Salesforce, Netflix), financial services (JP-
Morgan Chase, Visa), healthcare (Johnson & Johnson, Unit-
edHealth Group, Pfizer), retail (Walmart, Home Depot, Mc-
Donald’s), energy (ExxonMobil, Chevron), consumer goods
(Procter & Gamble, Coca-Cola, Nike), telecommunications
(Verizon), and industrials (Boeing, Caterpillar). For companies
with initial public offerings after 1982, data collection begins
at the first available trading date. For example, Salesforce data
begins in June 2004 following its IPO. The effective analysis
period for each stock corresponds to its available trading
history within the 1982-2025 window. This cross-sectional
design ensures the dataset reflects behavior across multiple
industries and economic cycles. The 20-stock universe was
chosen deliberately to balance temporal depth with cross-
sectional coverage: a smaller, well-established set of equities
allows for training on over four decades of data with complete
and reliable records, which would be difficult to achieve with
a much larger or historically reconstructed universe where data
quality varies substantially. This design is best understood as a
proof-of-concept demonstrating the architecture’s capacity to
learn inter-stock dependencies and integrate sentiment signals,
rather than a comprehensive market simulation. The selection
of current index constituents does introduce survivorship bias,
which is examined in detail in Section VI.
For each company, daily Open, High, Low, Close, and
V olume (OHLCV) trading variables, along with the adjusted
closing price, were collected: opening price (Ot), highest price
(Ht), lowest price (L t), closing price (C t), adjusted closing
price (C adj t ), and trading volume (V t). Technical indicators
were computed following established methodologies [16],
[20]:
Simple Moving Average (SMA):The SMA smooths short-
term price fluctuations to reveal underlying trends. Computing
it at multiple window lengths (n∈ {5,10,20}days) allows the
model to distinguish short-term momentum from longer-term
directional shifts:
SMAn(t) = 1 n
n−1X
i=0
Ct−i (4)
Exponential Moving Average (EMA):Unlike the SMA,
the EMA assigns greater weight to recent observations through
an exponential decay controlled by smoothing factorα=
2/(n+ 1). This makes it more responsive to recent price
changes, which is valuable for detecting early trend reversals:
EMAn(t) =α·C t + (1−α)·EMA n(t−1)(5)
Relative Strength Index (RSI):The RSI is a bounded mo-
mentum oscillator that measures the speed and magnitude of
recent price changes on a scale from 0 to 100. Values above 70
typically indicate overbought conditions, while values below
30 suggest oversold conditions. It is computed using a 14-day
window:
RSI(t) = 100− 100
1 + G14(t) L14(t) (6)
where G14(t)and L14(t)are the average gains and average
losses over the preceding 14 trading days.
Moving Average Convergence Divergence (MACD):The
MACD captures changes in trend strength and direction by
measuring the difference between a short-term (12-day) and a

5
long-term (26-day) EMA. A positive MACD indicates upward
momentum, while a negative value signals downward pressure.
Crossovers between the MACD and its 9-day signal line are
commonly used as trade triggers:
MACD(t) =EMA 12(t)−EMA 26(t)(7)
with 9-day signal line Signal(t) =EMA 9(MACD(t)).
Daily Returns and Log Returns:Daily returns quantify
the relative price change between consecutive trading days
and serve as the primary measure of stock performance.
Log returns are included alongside arithmetic returns because
they are additive over time and more closely approximate
a normal distribution, properties that benefit gradient-based
optimization:
rt = Ct −C t−1 Ct−1 , r log t = ln  Ct Ct−1  (8)
Rolling Volatility:Rolling volatility measures the disper-
sion of returns over a trailing 20-day window, providing a real-
time estimate of price uncertainty. Higher volatility indicates
greater risk and wider expected price ranges, which is critical
for the model’s gating mechanism to adjust feature emphasis
across market regimes:
σt =
vuut 1
19
19X
i=0
(rt−i −¯rt)2 (9)
Missing values were addressed through a temporally aware
imputation strategy designed to prevent information leakage.
During training data preparation, short gaps (1-2 trading days)
used linear interpolation:
Ct =C t−k + Ct+m −C t−k k+m ·k(10)
wherekandmare distances to nearest observed values.
For validation and test data, only forward-filling from the
most recent observed value was applied to ensure no future
information leaked into predictions:C t =C t−k wherekis
the distance to the most recent observation. Longer gaps in
training data also employed forward filling. Each observation
contains 6 raw variables and 11 derived indicators.
Feature normalization used an expanding window z-score
approach to prevent look-ahead bias. For each featurex i,t,
the normalized value was computed as:
˜xi,t = xi,t −µ 1:t σ1:t (11)
whereµ 1:t andσ 1:t are the mean and standard deviation
computed over all available data from the start of the training
period up to timet. For test data, normalization statistics were
fixed using the full training set, ensuring no information from
the test period influenced the standardization.
Fig. 1 illustrates the feature engineering pipeline.
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
Z-Score
Normalization
Feature Vector
xi,t ∈R 17
Fig. 1. Feature engineering pipeline. Raw OHLCV data is processed through
multiple technical indicator computations, normalized using z-score standard-
ization, and concatenated into the final feature vector.
B. Sentiment Datasets
The sentiment component relies on two complementary
datasets that together capture both benchmark-labeled senti-
ment and large-scale real-world social media activity. The first
provides expert-annotated ground truth for training the BERT
classifier, while the second supplies the raw social media text
processed at inference time.
The Market Sentiment Evaluation (MSE) dataset is a pub-
licly available corpus containing finance-related messages
from social media platforms [30]. Each message has been
annotated by financial experts with sentiment scoress∈
[−1,+1], where−1indicates strongly negative,0neutral,
and+1strongly positive sentiment. The dataset includes
source platform identifiers, message IDs, relevant cashtags,
and annotated sentiment spans. Because it contains human-
labeled ground truth, the MSE dataset serves as the primary
training and validation resource for fine-tuning the BERT
sentiment module.
The Comprehensive Stock Sentiment (CSS) dataset was
constructed using the X (formerly Twitter) API through sys-
tematic searches for the cashtag corresponding to each of the
twenty stocks listed in Table I. Since the platform was founded
in 2006, the CSS dataset covers January 2007 to March 2025,
yielding approximately 4.2 million posts across all stocks.
TABLE I
SEARCH TAGS USED FORCSSDATASET COLLECTION.
Cashtag Company Cashtag Company
$AAPL Apple $KO Coca-Cola
$MSFT Microsoft $CVX Chevron
$JPM JPMorgan Chase $HD Home Depot
$JNJ Johnson & Johnson $VZ Verizon
$WMT Walmart $BA Boeing
$XOM ExxonMobil $MCD McDonald’s
$PG Procter & Gamble $NFLX Netflix
$V Visa $CAT Caterpillar
$UNH UnitedHealth Group $PFE Pfizer
$NKE Nike $CRM Salesforce
Once the BERT model is fine-tuned on the MSE labels, it is
applied to the CSS corpus to generate daily sentiment scores
for each stock. These scores are then aggregated at multiple

6
time scales and fed into the node transformer as additional
input features.
Both datasets underwent identical preprocessing before en-
tering the sentiment pipeline. This included removal of HTML
encodings and special characters, anonymization of user iden-
tifiers, removal of retweet markers, URL standardization with
placeholder tags, de-elongation of exaggerated words (e.g.,
“victoryyyyy”→“victory”), spacing correction for ticker
symbols (e.g., “$ AAPL”→“$AAPL”), and ordinal expression
normalization.
C. Dataset Partitioning
Temporal splits were applied to prevent look-ahead bias,
following the standard practice in financial time series fore-
casting. Because stock prices exhibit serial dependence and
evolving distributional properties, random or stratified parti-
tioning schemes such as k-fold cross-validation would allow
future observations to inform predictions of earlier time steps,
producing artificially inflated accuracy estimates that do not
reflect realistic forecasting conditions. In a forecasting context,
the model must never train on data that postdates the prediction
target; violating this constraint renders performance metrics
unreliable regardless of their magnitude. Chronological parti-
tioning ensures that the model is evaluated exclusively on data
that postdates the training window, mirroring the information
constraints faced by a real-time forecaster.
The training set comprises January 1, 1982 to December
31, 2010 (70% of temporal range). The validation set spans
January 1, 2011 to December 31, 2016 (15%), serving as both
a hyperparameter tuning period and a temporal buffer that sep-
arates training from test data by six calendar years. The test set
covers January 1, 2017 to March 31, 2025 (15%), deliberately
spanning multiple distinct market regimes including the pre-
pandemic bull market (2017–2019), the COVID-19 crash and
recovery (2020–2021), and the inflationary tightening period
(2022–2024). The inclusion of the COVID-19 pandemic in the
test set rather than in training provides a rigorous assessment
of the model’s ability to generalize to market conditions
qualitatively different from those observed during training.
The volatility regime analysis in Section V-E confirms that
the model maintains reasonable accuracy across these diverse
conditions, with MAPE rising from 0.70% in low-volatility
periods to 1.50% in high-volatility periods, a degradation
consistent with the inherent difficulty of forecasting during
market stress rather than a failure of generalization.
The full 1982-2025 training window is retained because
the price-based components of the model, including the node
transformer, graph structure learning, and temporal encoding,
benefit substantially from exposure to diverse market regimes
spanning over four decades. Restricting training to the post-
2007 period would sacrifice the 1982-2006 data that contains
the 1987 crash, the dot-com bubble, and the 2008 financial cri-
sis, all of which are critical for learning robust representations
of market dynamics.
For sentiment data, partitioning aligns with financial splits
for the overlapping period. Since X (formerly Twitter) data
begins in 2007, the sentiment training period covers January
2007 to December 2010. For pre-2007 financial data, sen-
timent features are set to neutral (zero). This zero-padding
is handled by the adaptive gating mechanism (Section IV-E),
which learns to down-weight the sentiment channel when its
signal is absent, effectively allowing the model to operate in
a price-only mode for the pre-2007 training window and tran-
sition to multimodal operation when sentiment data becomes
available. The sentiment integration component is primarily
evaluated on the test set (2017-2025), where sentiment data is
abundant and the model can fully leverage both data streams.
The MSE dataset used for BERT fine-tuning is partitioned
separately into 70% training, 15% validation, and 15% test,
stratified by sentiment class to preserve label distribution.
The BERT model is fine-tuned and evaluated on this split
independently before its outputs are integrated into the full
forecasting pipeline (see Section V-D). Table II summarizes
the key characteristics of the financial and sentiment datasets.
TABLE II
DATASET SUMMARY STATISTICS.
Characteristic FMD CSS
Time period 1982-2025 2007-2025
Number of stocks 20 20
Trading days≈10,300≈4,100
Features per stock-day 17 3
Total observations≈206,000≈4.2M posts
IV. METHODOLOGY
The proposed framework integrates a node transformer
architecture with BERT-based sentiment analysis, combining
quantitative financial indicators with qualitative textual sig-
nals. The design follows a modular structure in which the
graph-based transformer and the sentiment pipeline operate as
independent components, coupled through an attention-based
fusion layer that dynamically adjusts the relative weighting of
each stream based on current market conditions.
A. System Architecture Overview
Fig. 2 presents the overall system architecture. The frame-
work processes historical market data and sentiment informa-
tion through two parallel pathways. The quantitative branch
normalizes all market features (price, volume, and technical
indicators), constructs the graph structure, applies temporal
encoding, and feeds the processed representations into the
node transformer. The qualitative branch passes social media
text through the BERT encoder and aggregates sentiment
scores at multiple time scales. The two streams converge at
an attention-based fusion layer that produces the final price
prediction.
B. Graph Representation of the Stock Market
The stock market is represented as a graphG= (V,E,E)
whereV={1, . . . , N}is the set ofN= 20stock nodes,
E ⊆ V ×Vis the edge set (fully connected), andE∈RN×N is
the edge weight matrix. The choice ofN= 20nodes balances
computational tractability with sufficient cross-sectional cov-
erage to capture major sector interactions. While larger graphs

7
Market Data: Pricep i,t, V olumevi,t, Technical IndicatorsI i,t Social Media Posts
Z-Score
Normalization
Graph
Construction
Temporal
Encoding
BERT
Encoder
Node Transformer
(6 Layers, 8 Heads)
Sentiment
Aggregation
Attention-Based
Multimodal Fusion
Price Prediction
ˆyi,t+h
Fig. 2. System architecture. Price data, volume, and technical indicators are
jointly processed through normalization, graph construction, and temporal
encoding before the node transformer. Social media posts are processed
through BERT and sentiment aggregation. Both streams combine through
attention-based multimodal fusion.
might better represent full market topology, the current design
enables deep temporal analysis (252-day input sequences)
across diverse sectors. The fully-connected structure with
learnable edge weights ensures all pairwise relationships can
be discovered during training. Ablation results (Section V-E)
confirm that the graph structure contributes meaningful pre-
dictive improvement over models without explicit inter-stock
connections.
Edge weights are initialized based on sector relationships
and historical price correlations:
e(0) ij =α·δ sector(i, j) + (1−α)·max(0, ρij)(12)
whereδ sector(i, j) = 1if stocksiandjshare the same
Global Industry Classification Standard (GICS) sector clas-
sification and0otherwise,ρ ij is the Pearson correlation
coefficient between daily returns computed over the training
period,max(0,·)ensures non-negative weights, andα= 0.5
balances sector and correlation information.
During training, edge weights are refined iteratively:
e(ℓ+1) ij =σ  wT e [h(ℓ) i ∥h(ℓ) j ] +b e  (13)
whereσis the sigmoid function,w e ∈R 2d is a learnable
weight vector,h (ℓ) i ,h (ℓ) j ∈R d are node representations at layer
ℓ,∥denotes concatenation, andb e is a learnable bias. Edges
are undirected:e ij =e ji.
At each training step, the model receives a batch of temporal
windows. For a single sample, the input is a three-dimensional
tensorX∈R T×N×d in, whereT= 252is the sequence length
(trading days),N= 20is the number of stock nodes, and
din = 17is the per-stock feature dimension after concatenating
raw OHLCV data with technical indicators. The edge weight
matrixE∈R N×N is initialized once from Equation 12 and
shared across all time steps within a given forward pass. At
each time stept, the node transformer processes the slice
Xt ∈R N×d in jointly across allNnodes, with the attention
mechanism modulated byEso that information flows prefer-
entially along stronger graph connections. The edge weights
are then updated via Equation 13 at each transformer layer,
allowing the graph structure to co-evolve with the learned node
representations as the input propagates through the network.
C. Node Transformer Architecture
The node transformer extends the standard transformer by
incorporating graph-structured relational inductive biases [10].
Rather than treating each stock’s time series independently,
the architecture processes all nodes jointly at each time step,
allowing information to propagate across the graph through
attention weighted by the learned edge structure described
above.
1) Input Representation:Each stock is represented by a
composite feature vector that concatenates raw market data,
engineered indicators, positional information, and a learned
identity embedding. For stockiat timet, this vector is:
xi,t = [pi,t∥vi,t∥Ii,t∥TE(t)∥si]∈R din (14)
wherep i,t ∈R 5 contains normalized prices (open, high,
low, close, adjusted close),v i,t ∈Ris normalized volume,
Ii,t ∈R 11 contains technical indicators, TE(t)∈R d is the
temporal encoding, ands i ∈R ds is a learned stock-specific
embedding capturing persistent characteristics.
2) Temporal Encoding:Following Vaswani et al. [8], tem-
poral encoding injects positional information:
TE(t,2k) = sin
 t
100002k/d

TE(t,2k+1) = cos
 t
100002k/d

(15)
wheretis the trading day index,k∈ {0, . . . , d/2−1}is
the dimension index, andd= 512is the model dimension.
A clarification on the role of this encoding is warranted,
as the use of sinusoidal functions may appear counterintuitive
for financial data that does not follow periodic patterns. The
temporal encoding does not model or approximate the shape of
the price series. Instead, it provides the attention mechanism
with information about where each observation falls within
the input sequence, which is necessary because self-attention
is inherently permutation-invariant and would otherwise treat
a shuffled sequence identically to the original ordering. The
sinusoidal functions are chosen for three specific properties
identified in the original transformer work [8]. First, each
positiontreceives a unique encoding vector, allowing the
model to distinguish any two time steps. Second, the relative
offset between two positionstandt+ ∆can be expressed as
a linear transformation of the encoding att, which enables
the attention heads to learn relative temporal relationships
(such as “five trading days ago”) rather than only absolute
positions. Third, the deterministic formulation generalizes to
sequence lengths not encountered during training without
requiring additional learned parameters. The volatile price and
volume data are encoded separately in the 17-dimensional
feature vectorx i,t, which captures the actual market dynamics;

8
the temporal encoding is simply added to this representation
so that the model knows the temporal ordering of those
observations. Lower encoding dimensions oscillate at higher
frequencies, capturing fine-grained positional distinctions be-
tween adjacent trading days, while higher dimensions vary
more slowly and provide coarser temporal context across the
full 252-day input window. The ablation study (Section V-E)
confirms that removing temporal encoding degrades MAPE by
18.8%, indicating that positional ordering carries substantial
predictive information even though the encoding itself bears
no resemblance to price dynamics.
3) Graph-Aware Multi-Head Self-Attention with Causal
Masking:The attention mechanism incorporates the learned
edge weight matrixEfrom Section IV-B as a structural bias,
so that stock pairs with stronger graph connections receive
higher baseline attention. Causal masking ensures predictions
at timetuse only information from times≤t:
A(Q,K,V) =softmax
 QKT
√dk +M+E

V(16)
whereQ=XW Q,K=XW K,V=XW V are linear
projections,d k = 64is the key dimension,Mis the causal
mask withM ab = 0ifa≥bandM ab =−∞otherwise, and
E∈R N×N is the edge weight matrix. The additive graph bias
allows content-based attention (viaQK T ) and structural priors
(viaE) to jointly determine how information flows between
stocks at each layer.
WithH= 8attention heads, each operating ind k =
dv = 64dimensions, the total model dimension isd model =
H×d k = 512. Fig. 3 illustrates the internal structure of
a single transformer layer, showing the residual connections,
layer normalization, and dropout placement.
InputX (ℓ)
Multi-Head Self-Attention
(8 heads, causal mask)
+
LayerNorm
Feed-Forward Network
dff = 2048
+
LayerNorm
OutputX (ℓ+1)
dropout=0.1
dropout=0.1
Fig. 3. Single transformer layer architecture. Input passes through multi-head
self-attention with residual connection and layer normalization, followed by
a position-wise feed-forward network with another residual connection and
normalization.
4) Time-Based Feature Gating:A gating mechanism adap-
tively weights features based on temporal context:
gi,t =σ(W gxi,t +b g)∈(0,1) din (17)
x′ i,t =g i,t ⊙x i,t (18)
whereW g ∈R din×din,b g ∈R din are learnable parameters,
and⊙denotes element-wise multiplication. This mechanism
enables adaptive emphasis on different features during volatile
versus stable periods.
5) Feed-Forward Network:Each layer includes a position-
wise Feed-Forward Network (FFN):
FFN(x) =ReLU(xW 1 +b 1)W2 +b 2 (19)
whereW 1 ∈R 512×2048,W 2 ∈R 2048×512, andb 1,b 2 are
biases.
The complete architecture consists ofL= 6stacked layers
with residual connections and layer normalization after each
sub-layer. Dropout withp= 0.1is applied for regularization.
D. BERT-Based Sentiment Analysis
The sentiment component employs BERT (bert-base-
uncased) with 12 transformer layers, 768 hidden dimensions,
and 12 attention heads [31]. BERT’s bidirectional attention is
well suited to financial text, where sentiment often depends
on contextual modifiers (e.g., “not bullish” vs. “bullish”) that
unidirectional models may miss.
1) Domain Adaptations:A financial domain embedding
layer augments the standard BERT token embeddings with
additional representations for financial terminology, enabling
the model to distinguish domain-specific usage of terms such
as “short,” “call,” and “bear” from their everyday meanings.
Maximum sequence length is set to 512 tokens, which ac-
commodates the vast majority of social media posts without
truncation.
2) Fine-Tuning Process:Fine-tuning on the MSE dataset
follows a three-stage progressive unfreezing schedule designed
to preserve BERT’s pretrained language representations while
adapting the upper layers to financial sentiment classifica-
tion. In the first stage, the embedding layer and the first 8
transformer blocks are frozen so that only the upper layers
and the classification head receive gradient updates; these are
trained for 3 epochs with a learning rate of2×10 −5 and
batch size 32. The second stage progressively unfreezes layers
from top to bottom over 5 additional epochs, allowing each
block to adapt incrementally to the financial domain without
catastrophic forgetting of general language knowledge. In the
final stage, all layers are unfrozen and trained jointly with a
reduced learning rate of5×10 −6 and gradient accumulation
over 4 steps to stabilize updates across the full parameter
space.
Because sentiment labels in financial text are typically im-
balanced, with neutral posts far outnumbering strongly positive
or negative ones, focal loss is used instead of standard cross-
entropy:
LFL(pt) =−α t(1−p t)γ log(pt)(20)
whereα t is class weight (inverse frequency),p t is predicted
probability for correct class, andγ= 2focuses training on
hard examples by down-weighting easily classified instances.
The classification head that maps BERT’s output to a
sentiment score consists of three stages. The 768-dimensional
[CLS] token representation is first passed through a dropout
layer (p= 0.1) followed by a linear projection to 256

9
dimensions and a tanh activation, which compresses the rep-
resentation while preserving the sign structure needed for
sentiment polarity. A second dropout layer (p= 0.1) precedes
the final linear projection to three logits corresponding to
negative, neutral, and positive classes. Softmax converts these
logits to class probabilities[p neg, pneu, ppos], and the continuous
sentiment score is computed ass=p pos −p neg ∈[−1,+1].
This formulation produces a score that is exactly zero only
when the positive and negative probabilities are equal, and
it varies smoothly with confidence, providing a richer signal
than a hard class assignment. Fig. 4 illustrates the complete
sentiment extraction pipeline from raw input to final score.
Raw Tweet: “$AAPL crushing it!”
Preprocessing & Tokenization
BERT Encoder (12 layers)
[CLS] Token Pooling
Sentiment Scores∈[−1,+1]
Fig. 4. BERT sentiment extraction pipeline. Raw social media posts are
preprocessed, tokenized, encoded through BERT, pooled via [CLS] token,
and classified to sentiment scores.
E. Integration of Node Transformer and BERT
1) Multi-Scale Sentiment Features:Raw daily sentiment
scores are noisy and sensitive to individual posts. To capture
both immediate market reactions and sustained sentiment
trends, scores are smoothed at multiple time scales before
entering the model:
Si,t = [S(1d) i,t , S(5d) i,t , S(20d) i,t ]∈R 3 (21)
whereS (kd) i,t is thek-day exponential moving average of
sentiment scores for stocki. This captures both immediate
reactions and sustained sentiment trends.
Social media activity varies substantially across stocks and
calendar days, creating sparsity that requires explicit handling.
On trading days where a stock receives fewer than 5 posts,
the raw daily score is replaced by the 5-day exponential
moving average from preceding days, preventing noisy esti-
mates derived from one or two posts from dominating the
signal. On days with no posts at all, all three sentiment
features (S (1d),S (5d),S (20d)) fall back to their respective
moving average values from the most recent day with sufficient
coverage. Stocks that consistently receive low social media
volume, such as industrials (Caterpillar, Boeing) relative to
technology names (Apple, Netflix), naturally produce senti-
ment scores closer to neutral over time, which the adaptive
gating mechanism (Section IV-E) learns to down-weight in
favor of price-based features. This design ensures that sparse
sentiment data degrades gracefully to a price-only prediction
rather than introducing noise.
2) Sentiment-Guided Attention:Rather than simply con-
catenating sentiment as an additional input feature, the model
allows sentiment to modulate the attention mechanism itself.
Specifically, sentiment scales the key representations so that
time steps with strong sentiment signals receive amplified or
dampened attention:
K′ t =K t ·(1 +β·S t)(22)
whereS t ∈[−1,1]is the sentiment score at timetand
β∈Ris a learnable parameter. The attention computation
becomes:
Asent =softmax
 QK′T
√dk +M

V(23)
3) Adaptive Integration:Because the relative predictive
value of price-based features and sentiment varies with market
conditions, the final prediction is produced by a learned convex
combination rather than a fixed weighting. A sigmoid gate
dynamically adjusts the balance between the node transformer
output and the sentiment-based prediction:
αt =σ(w T α [vt∥ ¯St] +b α)∈(0,1)(24)
ˆyi,t+h =α t ·y node i,t+h + (1−α t)·y sent i,t+h (25)
wherev t ∈R 3 contains rolling volatility computed over
5, 10, and 20-day windows, ¯St is mean absolute sentiment
across stocks,y node i,t+h is the node transformer prediction, and
ysent i,t+h is the sentiment-based prediction. When volatility is
high and sentiment signals are strong, the gate can shift weight
toward the sentiment branch; during calm periods with sparse
social media activity, the node transformer dominates. Fig. 5
illustrates this adaptive fusion mechanism.
ynode i,t+h ysent i,t+h
V olatilityvt
Sentiment ¯St
αt =σ(·)
ˆy=αt ynode + (1−αt )ysent
Final Prediction
ˆyi,t+h
Fig. 5. Adaptive fusion mechanism. The weighting coefficientα t is computed
from volatility and sentiment magnitude, then used to blend node transformer
and sentiment-based predictions.
F . Training Objective
Training a model that is useful for both price forecasting and
trading decisions requires optimizing more than point accuracy
alone. The composite loss function therefore combines four
terms that target complementary aspects of prediction quality:
Ltotal =λ 1LMSE +λ 2LDIR +λ 3LCORR +λ 4LREG (26)

10
The primary term is the mean squared error, which penalizes
deviations between predicted and realized prices and serves as
the dominant gradient signal during training:
LMSE = 1 N X i,t,h (yi,t+h −ˆyi,t+h)2 (27)
Because minimizing magnitude error does not guarantee
correct directional predictions, a binary cross-entropy term
explicitly rewards the model for predicting whether prices rise
or fall. Hered i,t,h =I(y i,t+h > yi,t)is the true direction
indicator andp i,t,h is the predicted probability of an increase:
LDIR =− 1 N X i,t,h [di,t,h logp i,t,h + (1−d i,t,h) log(1−p i,t,h)]
(28)
A correlation loss encourages the model to preserve cross-
sectional ranking among stocks at each time step, which is
critical for portfolio construction strategies that depend on
relative rather than absolute performance. It is defined as one
minus the Pearson correlationρbetween predicted and actual
return vectors:
LCORR = 1−ρ( ˆrt,r t)(29)
Finally, L2 regularization on all trainable parametersθ
prevents overfitting by penalizing large weight magnitudes:
LREG =∥θ∥ 2 2 (30)
The weightsλ 1 = 1.0,λ 2 = 0.5,λ 3 = 0.2, andλ 4 = 10−4
were tuned on validation data. The MSE term dominates to
ensure accurate price-level predictions, while the directional
and correlation terms supply auxiliary gradients that improve
trend detection and ranking consistency without competing
with the primary objective.
G. Training Process
The BERT encoder is fine-tuned separately on the MSE
dataset (Section IV-D) and remains frozen throughout the fore-
casting pipeline, serving purely as a fixed feature extractor that
produces sentiment scores. Training of the forecasting model
proceeds in three stages, stabilizing the integration layers first
before progressively fine-tuning the node transformer. During
the first 10 epochs, the node transformer is frozen while the
sentiment aggregation, fusion, and output layers are trained
with a learning rate of10 −4. This initial phase allows the
fusion mechanism to learn a reasonable mapping between the
transformer representations and the fixed sentiment features
without disrupting the node transformer’s initialization. In the
second stage, spanning 20 epochs, the top three layers of the
node transformer are unfrozen and the learning rate is reduced
to5×10 −5, enabling the upper representations to adapt to the
downstream task while preserving the lower-level features. The
final 30 epochs unfreeze all node transformer parameters at a
learning rate of10 −5, allowing end-to-end fine-tuning of the
forecasting architecture.
Throughout all three stages, optimization uses Adam with
β1 = 0.9,β 2 = 0.999, andϵ= 10 −8. The learning rate sched-
ule begins with a linear warmup over 4000 steps followed
by cosine decay to zero. A batch size of 32 with gradient
accumulation over 4 steps yields an effective batch size of
128, balancing memory constraints with gradient stability.
Hyperparameters were selected through a combination of
grid search and established conventions from the transformer
literature. Architectural parameters (number of layers, at-
tention heads, model dimension) were searched overL∈
{4,6,8},H∈ {4,8}, andd∈ {256,512}, with the con-
figurationL= 6,H= 8,d= 512selected based on
lowest validation MAPE. The feed-forward dimension was
fixed atd ff = 4d= 2048following the standard trans-
former scaling convention [8]. Dropout rate was searched
over{0.05,0.1,0.2}, withp= 0.1yielding the best trade-
off between underfitting and overfitting on the validation set.
The input sequence length of 252 days (one trading year) was
chosen to provide the model with a full annual cycle of price
dynamics, and was compared against 120-day and 504-day
alternatives on validation data. Learning rates for each train-
ing stage were determined through preliminary runs, starting
from the range[10 −5,10 −3]and narrowing based on training
stability and convergence speed. The loss function weights
(λ1 = 1.0,λ 2 = 0.5,λ 3 = 0.2,λ 4 = 10 −4) were tuned by
first training with MSE loss alone, then incrementally adding
each auxiliary term and adjusting its weight until validation
directional accuracy and ranking correlation stabilized. The
edge weight balancing parameterα= 0.5was searched over
{0.3,0.5,0.7}, with equal weighting of sector and correlation
information performing best. Table III summarizes the final
hyperparameter configuration for both the node transformer
and BERT components.
TABLE III
MODEL HYPERPARAMETERS.
Parameter Value
Node transformer layers 6
Attention heads 8
Model dimension 512
FFN dimension 2048
Dropout rate 0.1
Input sequence length 252 days
BERT layers 12
BERT hidden dimension 768
Batch size 32
Total training epochs 60
V. EXPERIMENTS ANDRESULTS
A. Experimental Setup
Experiments used the dataset described in Section III, span-
ning January 1982 to March 2025, a timeframe that captures
multiple market cycles including the 1987 Black Monday
crash, the 2000 dot-com bubble, the 2008 financial crisis,
and the 2020 COVID-19 volatility spike. The temporal split
allocates 1982-2010 for training, 2011-2016 for validation, and
2017-2025 for testing. Although a single temporal split is used
rather than rolling retraining, the eight-year test window itself

11
encompasses several distinct market regimes: the post-2016
bull market, the 2018 volatility correction, the 2020 pandemic
crash and recovery, the 2022 inflation-driven drawdown, and
the subsequent 2023-2024 rebound. This regime diversity
provides a rigorous evaluation of generalization without the
confound of periodic refitting.
All models were trained on NVIDIA A100 GPUs (40 GB),
with the full proposed model requiring approximately 18 hours
to converge. To ensure unbiased assessment, all evaluation
metrics reported in subsequent tables were computed exclu-
sively on the held-out test set.
B. Evaluation Metrics
The prediction targety i,t+h is the closing priceC t+h at
horizonh∈ {1,5,20}trading days. Price-level prediction
was chosen as the primary target because it provides intuitive
interpretation of forecast accuracy and aligns directly with
practical trading applications where position sizing depends on
expected price levels rather than percentage changes. A known
concern with price-level forecasting is that daily stock prices
exhibit strong persistence, meaning that even a trivial model
predicting tomorrow’s price as today’s can achieve low MAPE.
To guard against this artifact, the evaluation framework in-
cludes metrics specifically designed to measure predictive skill
beyond persistence: Theil’s U benchmarks against the naive
random walk, directional accuracy assesses trend detection
independent of magnitude, and the Information Coefficient
evaluates cross-sectional ranking. Return-based metrics are
also reported (Section V-E) to complement the price-level
analysis. Together, these metrics assess model performance
from complementary angles, covering magnitude accuracy,
scale sensitivity, directional correctness, relative forecasting
skill, and cross-sectional ranking.
Mean Absolute Percentage Error (MAPE) measures the
average magnitude of prediction errors as a percentage of ac-
tual values, making it scale-invariant and directly interpretable
across stocks with different price levels:
MAPE= 100 N
NX
i=1

 yi −ˆyi yi

 (31)
Root Mean Squared Error (RMSE) captures prediction
accuracy in the original price units and penalizes large errors
more heavily than MAPE due to the squaring operation. This
makes it particularly sensitive to outlier predictions during
volatile periods:
RMSE=
vuut 1
N
NX
i=1
(yi −ˆyi)2 (32)
Directional Accuracy (DA) measures the proportion of
correctly predicted price movement directions, independent
of magnitude. For trading applications, correctly forecasting
whether a stock will rise or fall is often more valuable than
minimizing absolute price error, since many strategies depend
on directional signals rather than precise price targets.
Theil’s U statistic benchmarks the model against a naive
random walk forecast that simply predicts tomorrow’s price
as today’s price. It is defined as:
U=
pP
t(yt+1 −ˆyt+1)2 pP
t(yt+1 −y t)2 (33)
A value ofU <1indicates that the model outperforms this
naive baseline, whileU= 1implies no improvement over
persistence forecasting. This metric is especially informative
for financial time series, where beating the random walk is
itself a non-trivial achievement given the near-efficient nature
of liquid equity markets.
The Information Coefficient (IC) is the Spearman rank
correlation between predicted and realized returns across the
stock universe at each time step. Unlike the other metrics,
which evaluate absolute accuracy for individual stocks, the IC
assesses cross-sectional ranking ability, measuring whether the
model correctly orders stocks from best to worst performer
on a given day. This property makes it directly relevant to
long-short portfolio construction, where relative performance
matters more than absolute price forecasts.
C. Baseline Models
Eight baseline models spanning statistical, classical machine
learning, and deep learning paradigms were trained on identi-
cal data splits to ensure fair comparison. All hyperparameters
were tuned via grid search on the validation set (2011-
2016), with final performance reported on the held-out test
set (2017-2025). To ensure comparability across deep learning
baselines, all models received the same 17-dimensional feature
vector and were trained under equivalent early stopping and
regularization protocols.
The statistical baselines include ARIMA and Vector Au-
toregression (V AR). ARIMA orders(p, d, q)were selected
via AIC withp, q∈[0,5]andd∈[0,2], fitting a separate
model per stock. V AR extends this to the multivariate setting,
modeling cross-stock dependencies with lag order selected via
the Bayesian Information Criterion (BIC) up to 10 lags. Both
statistical models operate on their own optimal lookback hori-
zons as determined by information criteria, which is standard
practice since ARIMA and V AR performance degrades when
forced to consume long input windows that introduce noise.
Three classical machine learning models were evaluated.
Random Forest used 100 trees with maximum depth 10 and
the same 17-dimensional feature vector as the proposed model.
Support Vector Regression (SVR) employed a Radial Basis
Function (RBF) kernel with regularization parameterCand
kernel widthγselected via grid search. XGBoost used 1000
estimators with early stopping on validation loss to prevent
overfitting, and its gradient boosting framework provides a
strong tree-based benchmark. All three classical models used a
60-day lookback window, selected via validation performance
from candidates of 20, 60, 120, and 252 days.
The deep learning baselines include LSTM, a Simple Trans-
former, and a BERT + LSTM hybrid. The LSTM used 2
layers with 128 hidden units and a 60-day lookback window
(≈0.5M parameters). During preliminary experiments, the

12
LSTM was also evaluated with 120-day and 252-day lookback
windows, but performance degraded at longer horizons due
to gradient attenuation over extended sequences, consistent
with known limitations of recurrent architectures on very long
time series [7]. The 60-day configuration yielded the best
validation performance and is therefore reported. The Simple
Transformer used 4 layers, 8 attention heads, 256-dimensional
embeddings, and a 252-day lookback window matching the
proposed model (≈4.2M parameters versus≈21.3M for the
full proposed architecture including graph and fusion compo-
nents). This configuration provides a controlled comparison
that isolates the contribution of graph structure and sentiment
integration while holding the input horizon and attention
mechanism constant. The BERT + LSTM hybrid combined
BERT-extracted sentiment features with an LSTM price model
through simple concatenation (≈1.1M parameters excluding
the frozen BERT encoder), serving as an ablation baseline
that tests whether the attention-based fusion mechanism in the
proposed architecture provides meaningful improvement over
naive feature combination.
The ablation study (Table VII) further addresses baseline
fairness by providing graph-free variants of the proposed archi-
tecture. The “Without Graph Structure” configuration removes
edge weights and inter-stock attention while retaining all other
components, effectively reducing the model to a standard
transformer with sentiment fusion. This variant isolates the
contribution of graph-based relational modeling independent
of other architectural advantages.
D. Sentiment Model Evaluation
Before evaluating the full forecasting pipeline, the fine-
tuned BERT sentiment classifier was assessed independently
on the MSE dataset. The dataset was partitioned into training
(70%), validation (15%), and test (15%) splits, stratified to
preserve the class distribution across all three subsets. The
model was fine-tuned on the training split using the progressive
unfreezing schedule described in Section IV-D, with early
stopping based on validation loss. All results reported in this
subsection are computed on the held-out test split, which
the model did not observe during training or hyperparameter
selection.
Table IV presents per-class and aggregate classification
metrics. Because the MSE dataset exhibits class imbalance,
with neutral posts outnumbering positive and negative ones,
macro-averaged scores are reported alongside accuracy to
avoid inflating performance through the majority class.
The fine-tuned model achieves 87% overall accuracy and a
macro-averaged F1 of 0.85, with per-class F1 scores ranging
from 0.81 (negative) to 0.90 (neutral). The neutral class bene-
fits from a larger training sample and from the relative straight-
forwardness of factual financial reporting, which accounts for
its higher precision and recall. The negative class exhibits the
lowest recall at 0.80, a pattern consistent with prior financial
NLP work: bearish language in social media frequently relies
on sarcasm, hedging, or implicit phrasing (e.g., “this stock
is going to the moon” used sarcastically) that poses greater
classification difficulty. Cohen’sκ= 0.79falls within the
TABLE IV
BERTSENTIMENT CLASSIFICATION PERFORMANCE ON THEMSETEST
SET.
Class / Metric Precision Recall F1-Score
Negative 0.83 0.80 0.81
Neutral 0.89 0.92 0.90
Positive 0.85 0.82 0.83
Macro Average 0.86 0.85 0.85
Overall Accuracy0.87
Cohen’sκ0.79
substantial agreement range, confirming that the classifier
discriminates sentiment beyond what class priors alone would
predict. Given that the ablation study (Section V-E) attributes
a 10% MAPE reduction to sentiment integration, the 13%
classification error rate suggests that the node transformer’s
gating mechanism is robust enough to extract predictive value
even from an imperfect sentiment signal.
E. Results
1) Overall Performance:Table V presents MAPE across
prediction horizons for all models. Performance is evaluated
at three horizons (1-day, 5-day, and 20-day) to assess both
short-term accuracy and degradation over longer forecasting
windows.
TABLE V
MAPE (%)ANDTHEIL’SUACROSS PREDICTION HORIZONS. BEST
RESULTS IN BOLD. STANDARD ERRORS IN PARENTHESES.
Model 1-Day 5-Day 20-Day Theil’s U
Na¨ıve Random Walk 1.35 (0.09) 3.40 (0.18) 5.80 (0.28) 1.00
ARIMA 1.20 (0.08) 2.80 (0.15) 4.50 (0.22) 0.89
V AR 1.15 (0.07) 2.60 (0.14) 4.20 (0.20) 0.85
LSTM 1.00 (0.06) 2.30 (0.12) 3.80 (0.18) 0.74
Random Forest 1.10 (0.07) 2.50 (0.13) 4.00 (0.19) 0.81
SVR 1.05 (0.06) 2.40 (0.12) 3.90 (0.18) 0.78
XGBoost 0.95 (0.05) 2.20 (0.11) 3.50 (0.16) 0.70
Simple Transformer 0.90 (0.05) 2.10 (0.10) 3.30 (0.15) 0.67
BERT + LSTM 0.88 (0.05) 2.00 (0.10) 3.10 (0.14) 0.65
Proposed Model 0.80 (0.04) 1.80 (0.09) 2.80 (0.13) 0.59
A persistent concern in short-horizon financial forecasting
is the naive persistence artifact, where a model achieves
seemingly low error by tracking the previous day’s closing
price (ˆyt+1 =y t). Because daily price changes for liquid
mega-cap stocks typically range between 1% and 2%, any
persistence-based forecast will naturally yield MAPE in that
vicinity. The naive random walk baseline in Table V produces
a 1-day MAPE of 1.35% on our test set, and the proposed
model’s Theil’s U of 0.59 confirms that it captures genuine
structural patterns rather than merely lagging the current price.
All learned models achieveU <1, but only the proposed
model reduces the random walk error by more than 40%,
with the gap widening at longer horizons where persistence
forecasting degrades rapidly.
The proposed model achieves 0.80% MAPE for 1-day pre-
dictions, representing 33% relative improvement over ARIMA
(∆ = 0.40percentage points) and 20% improvement over

13
LSTM (∆ = 0.20percentage points). Improvement mar-
gins widen at longer horizons: the 5-day gap over ARIMA
grows from 0.40 to 1.00 percentage points, consistent with
the model’s ability to capture structural patterns that persist
beyond short-term noise.
2) Directional Accuracy:Beyond magnitude accuracy, di-
rectional accuracy measures the proportion of correctly pre-
dicted price movement directions. Table VI presents direc-
tional accuracy with 95% confidence intervals computed via
bootstrap resampling.
TABLE VI
DIRECTIONAL ACCURACY(%)FOR1-DAY PREDICTIONS WITH95%
CONFIDENCE INTERVALS.
Model DA (%)
Random Baseline 50.0
ARIMA 55.0 [53.2, 56.8]
V AR 56.0 [54.2, 57.8]
LSTM 58.0 [56.2, 59.8]
Random Forest 57.0 [55.2, 58.8]
XGBoost 60.0 [58.2, 61.8]
Simple Transformer 62.0 [60.2, 63.8]
BERT + LSTM 63.0 [61.2, 64.8]
Proposed Model 65.0 [63.2, 66.8]
The proposed model achieves 65% directional accuracy, ex-
ceeding the 50% random baseline by 15 percentage points and
outperforming LSTM by 7 percentage points. The confidence
interval [63.2, 66.8] does not overlap with the best baseline
(BERT + LSTM at [61.2, 64.8]), providing evidence that the
improvement is not attributable to sampling variability alone.
3) Ablation Studies:To isolate the contribution of each
architectural component, Table VII presents results from sys-
tematic ablation experiments. Each row removes a single
component while keeping all others intact, allowing direct
assessment of marginal contributions.
TABLE VII
ABLATION STUDY: MAPE (%)FOR1-DAY PREDICTIONS.
Configuration MAPE∆vs Full
Full Model 0.80 –
Without Sentiment 0.88 +10.0%
Without Graph Structure 0.92 +15.0%
Without Temporal Encoding 0.95 +18.8%
Without Feature Gating 0.84 +5.0%
Price Features Only 1.02 +27.5%
Graph structure contributes the second-largest improve-
ment at 15%, confirming that explicit inter-stock relationship
modeling provides predictive value beyond treating stocks
independently. Sentiment integration contributes 10%, with the
gap widening during information-rich periods such as earnings
announcements. Temporal encoding contributes 18.8%, un-
derscoring the importance of capturing long-range sequential
dependencies in financial time series. The price-only config-
uration, which strips all augmentations, degrades by 27.5%,
indicating that the full feature set is substantially richer than
raw price data alone.
The ablation results also address a natural question about
the sentiment data horizon. Because social media data begins
in 2007 while the financial dataset extends to 1982, the
model’s price-based components receive training signal over
the full temporal range whereas the sentiment components
train on only four years of labeled data (2007-2010). The
“Without Sentiment” configuration in Table VII is function-
ally equivalent to a price-only evaluation of the architecture,
achieving MAPE of 0.88% and demonstrating that the node
transformer and graph structure are fundamentally competent
without any sentiment signal. The full model’s improvement
to 0.80% then isolates the incremental contribution of senti-
ment integration. Because the entire test set (2017-2025) falls
within the sentiment-available period, these two configurations
effectively provide the decomposition of a long-horizon price-
based evaluation alongside a sentiment-augmented evaluation
on the same test window, confirming that the 10% reduction
represents genuine predictive value rather than an artifact
of the training mismatch. Given that the sentiment fusion
mechanism was trained on only four years of multimodal data
(2007-2010), this improvement likely represents a conservative
estimate of the contribution sentiment could offer with a longer
training history.
4) Performance Across Volatility Regimes:Table VIII
presents MAPE across volatility regimes classified by the
CBOE V olatility Index (VIX) (Low: VIX<15; Medium:15≤
VIX<25; High: VIX≥25).
TABLE VIII
MAPE (%)BY MARKET VOLATILITY REGIME.
Model Low VIX Medium VIX High VIX
ARIMA 1.00 1.30 2.10
LSTM 0.85 1.10 1.80
XGBoost 0.80 1.00 1.60
Proposed0.70 0.90 1.50
The proposed model achieves MAPE of 1.50% during
high-volatility periods, compared to 1.60–2.10% for baseline
models. This robustness gap is most pronounced during VIX
spikes accompanying earnings surprises and macroeconomic
shocks, precisely the conditions where accurate forecasts carry
the greatest practical value for risk management. The gating
mechanism likely contributes to this resilience by increasing
the weight of momentum features during volatile periods while
favoring longer-term indicators during calm markets.
Directional accuracy also varies with market regime. Dur-
ing low-volatility periods (VIX<15), the proposed model
achieves 68.2% DA, benefiting from the relatively stable trend
structure that characterizes calm markets. In medium-volatility
conditions (15≤VIX<25), DA decreases to 64.5%,
and during high-volatility episodes (VIX≥25) it falls to
59.8%. While the high-volatility DA represents a meaningful
decline from calm-market performance, it remains well above
the 50% random baseline and exceeds all baseline models
by 3-5 percentage points in the same regime. This pattern
is consistent with the expectation that directional prediction
becomes inherently more difficult as volatility increases and
price movements are dominated by sudden information shocks
rather than gradual trends.

14
5) Return-Based Evaluation:To verify that the reported
improvements reflect genuine return prediction rather than
an artifact of price persistence, prediction accuracy was also
assessed in return space. For each model, the implied daily
return is computed asˆr t = (ˆyt+1 −y t)/yt and compared
against the realized returnr t = (yt+1 −y t)/yt. Because daily
price changes for mega-cap equities are small relative to the
price level (|rt| ≪1), the return prediction MAE is mathemat-
ically close to the price-level MAPE: specifically, return MAE
=MAPE×(y t+h/yt), which approaches MAPE ash→0. For
the 1-day horizon, the proposed model achieves a return MAE
of 0.81%, the naive random walk yields 1.36% (reflecting the
average absolute daily return of the 20-stock universe), and
all intermediate models fall between these bounds in the same
rank order as Table V. This near-equivalence between price
and return metrics at the daily horizon confirms that the MAPE
rankings are not inflated by the choice of evaluation target.
The more informative return-based assessments for this
dataset are the metrics already reported: Theil’s U (0.59)
explicitly benchmarks against persistence forecasting, direc-
tional accuracy (65%) evaluates trend detection independent
of magnitude, and the Information Coefficient measures cross-
sectional ranking on returns. At longer horizons where the
gap betweeny t andy t+h widens, return-based evaluation
becomes more distinct from price-level metrics. The proposed
model’s 5-day return MAE of 1.82% and 20-day return MAE
of 2.85% remain proportionally below all baselines, with the
performance gap widening at longer horizons consistent with
the MAPE results.
6) Statistical Significance:To assess whether the observed
improvements are statistically significant rather than artifacts
of sampling variability, paired t-tests were conducted com-
paring daily absolute prediction errors between the proposed
model and each baseline across the 1,580 test days. Table IX
presents the results along with Cohen’sdeffect sizes.
TABLE IX
PAIRED T-TEST RESULTS(n= 1,580TEST DAYS). NEGATIVEtINDICATES
PROPOSED MODEL SUPERIORITY.
Baselinet-statisticp-value Cohen’sd
ARIMA−4.25<0.00010.34
LSTM−3.120.0018 0.25
XGBoost−2.450.0145 0.19
Simple Transformer−2.180.0295 0.17
BERT + LSTM−3.900.0001 0.31
All comparisons achievep <0.05, with the strongest
significance observed against ARIMA (p <0.0001) and the
weakest against the Simple Transformer (p= 0.0295). Effect
sizes (Cohen’sd) range from 0.17 to 0.34, indicating small
to medium practical effects. The larger effect sizes against
ARIMA and BERT + LSTM reflect more fundamental archi-
tectural differences, while the smaller effect size against the
Simple Transformer suggests that much of the improvement
stems from the graph and sentiment components rather than
the transformer backbone itself.
Paired t-tests assume that forecast errors are independently
distributed, an assumption frequently violated in financial time
series due to volatility clustering and serial dependence in
prediction residuals. To account for this, we supplement the
analysis with the Diebold-Mariano (DM) test [32], which
evaluates equal predictive accuracy between two forecasting
models using Newey-West heteroskedasticity and autocorrela-
tion consistent standard errors. Table X reports DM statistics
computed on mean absolute error loss differentials over the
1,580-day test period, with the naive random walk included
as a reference benchmark.
TABLE X
DIEBOLD-MARIANO TEST RESULTS(n= 1,580TEST DAYS, MAELOSS).
NEGATIVEDM-STATISTIC INDICATES PROPOSED MODEL SUPERIORITY.
Baseline DM-statisticp-value
Na¨ıve Random Walk−5.82<0.0001
ARIMA−3.580.0002
LSTM−2.670.0038
XGBoost−2.080.0189
Simple Transformer−1.840.0330
BERT + LSTM−3.310.0005
The DM statistics are uniformly attenuated relative to the
paired t-test values, consistent with the inflation of standard
errors once serial dependence in forecast residuals is accounted
for. All comparisons remain significant atp <0.05, though the
margin against the Simple Transformer narrows (p= 0.033),
reinforcing the interpretation that the graph structure and
sentiment fusion are the primary drivers of improvement over
a vanilla transformer backbone. The strongest DM statistic
appears against the naive random walk (−5.82,p <0.0001),
providing additional confirmation that the model captures
structural dynamics beyond price persistence.
7) Economic Significance:To assess practical utility be-
yond statistical accuracy, a simulated long-short portfolio strat-
egy was constructed over the full test period. Each trading day,
the strategy takes long positions in the top 5 predicted perform-
ers and short positions in the bottom 5, equally weighted and
rebalanced daily. The following results should be interpreted
as a preliminary indication of economic viability rather than a
definitive backtest, given the simplified assumptions regarding
execution and the use of survivor-biased stock selection.
Over the full test period (January 2017 to March 2025), the
strategy achieved gross annualized returns of 22.8%, compared
to 13.9% for S&P 500 buy-and-hold. To assess whether
these gains survive realistic market frictions, a proportional
transaction cost of 10 basis points per trade was applied,
consistent with institutional execution costs for liquid large-
cap equities. The strategy exhibited an average daily portfolio
turnover of 32%, reflecting the sentiment-driven rebalancing
that shifts positions as new social media signals arrive. After
deducting transaction costs, the net annualized return was
14.6%, still exceeding the buy-and-hold benchmark by 0.7
percentage points. The net annualized Sharpe ratio was 0.84
(down from 1.35 gross), and the maximum drawdown reached
14.3%, compared to 23.9% for the buy-and-hold benchmark
during the same period.
Table XI summarizes the portfolio statistics. The sub-
period breakdown reveals that performance varied across mar-
ket regimes: net annualized returns reached 19.1% during

15
the 2017-2019 bull market but compressed to 8.7% during
the 2022 inflationary drawdown, when elevated volatility in-
creased turnover and eroded returns through higher transaction
costs. This regime sensitivity reinforces the observation that
the strategy’s profitability is not uniform and that lower-
frequency rebalancing or dynamic cost-awareness could im-
prove net performance in turbulent conditions.
TABLE XI
PORTFOLIO BACKTEST STATISTICS(JANUARY2017TOMARCH2025).
Statistic Gross Net (10 bps)
Annualized Return 22.8% 14.6%
Annualized Sharpe Ratio 1.35 0.84
Maximum Drawdown 12.1% 14.3%
Average Daily Turnover 32%
S&P 500 Buy-and-Hold Return 13.9%
S&P 500 Maximum Drawdown 23.9%
VI. DISCUSSION
A. Interpretation of Results
Within the scope of this evaluation, the integrated model
shows consistent improvements across metrics, horizons, and
market conditions, with the magnitude of gains varying by
component and context in ways that shed light on the mech-
anisms underlying the model’s predictive performance.
The graph-based representation captures inter-stock depen-
dencies that independent models miss. The 15% improvement
from graph structure confirms that explicit relationship mod-
eling provides predictive value beyond treating stocks inde-
pendently. Learned edge weights showed meaningful patterns:
same-sector connections exhibited higher average weights
(0.72 vs. 0.41 for cross-sector), while cross-sector weights
increased during market-wide movements, consistent with
empirical observations that correlations increase during market
stress [5].
Deeper inspection of the learned graph reveals three struc-
tural properties that align with established financial theory.
First, edge weights cluster by sector in a manner that goes
beyond the initialization prior. Technology stocks (Apple,
Microsoft, Salesforce, Netflix) form the tightest cluster with
average intra-group weights of 0.81, followed by energy
(ExxonMobil, Chevron) at 0.79 and healthcare (Johnson &
Johnson, UnitedHealth, Pfizer) at 0.74. Consumer goods and
industrials exhibit weaker internal cohesion (0.63 and 0.58
respectively), consistent with the greater heterogeneity of
business models within those sectors. Second, the temporal
stability of edge weights varies predictably with economic
conditions. During the low-volatility period of 2017-2019, the
standard deviation of edge weights across consecutive months
averaged 0.04, indicating a stable relationship structure. This
stability broke down during the March 2020 COVID crash,
when the month-over-month standard deviation spiked to 0.11
and cross-sector edge weights increased by an average of 0.18,
reflecting the well-documented phenomenon of correlation
convergence during systemic stress. By mid-2021, the weight
distribution had largely reverted to pre-crisis levels. Third, cer-
tain cross-sector edges exhibited persistently high weights that
reflect supply-chain or macroeconomic linkages rather than
sector proximity. The learned weight between ExxonMobil and
Caterpillar (0.67, the highest cross-sector pair) likely captures
the shared sensitivity of energy and heavy-industry firms to
commodity cycles and capital expenditure trends. Table XII
lists the five highest and five lowest learned edge weights to
illustrate the range of discovered relationships.
TABLE XII
TOP-5AND BOTTOM-5LEARNED EDGE WEIGHTS AFTER TRAINING.
StockiStockjWeight Same Sector
Apple Microsoft 0.86 Yes
ExxonMobil Chevron 0.82 Yes
Microsoft Salesforce 0.78 Yes
J&J UnitedHealth 0.76 Yes
ExxonMobil Caterpillar 0.67 No
Netflix Chevron 0.19 No
Pfizer Nike 0.21 No
Verizon Salesforce 0.23 No
Boeing Coca-Cola 0.24 No
McDonald’s Netflix 0.26 No
The top weights are dominated by same-sector pairs whose
business fundamentals are closely linked, while the bottom
weights connect companies with minimal overlap in revenue
drivers, customer bases, or macroeconomic exposures. The
one exception among the top five, ExxonMobil-Caterpillar,
reflects a learned cross-sector dependency that the initialization
prior alone would not have produced. These patterns suggest
that the edge refinement mechanism successfully discovers
economically meaningful relationships that go beyond the
sector and correlation priors used for initialization.
Sentiment integration appears particularly valuable around
information events. The 25% improvement during earnings
seasons suggests that social media sentiment may carry early
signals not yet fully reflected in contemporaneous prices.
Sector-level heterogeneity aligns with expectations: consumer-
facing companies show stronger sentiment-price relationships
(14% MAPE reduction) compared to utilities (6%), likely
reflecting differential retail investor engagement.
The gating mechanism enables adaptive feature weighting
that responds to market conditions. Analysis of learned gate
activations showed that momentum features (RSI, MACD,
short-term returns) received higher weights during volatile
periods, while longer-term indicators (20-day SMA, rolling
volatility) received higher weights during stable periods. This
adaptive behavior aligns with the intuition that different in-
dicators carry different predictive value depending on market
regime, and it emerges naturally through training rather than
being imposed through manual feature selection.
B. Implications
For practitioners, the model’s directional accuracy could
support more informed trading decisions, particularly for
short-term strategies where predicting price direction is often
more important than predicting magnitude. The ability to
maintain lower error during volatile conditions could assist
risk management, as these are precisely the periods when

16
forecast reliability matters most for position sizing and draw-
down control. The graph structure provides interpretable inter-
stock relationships that may inform portfolio diversification,
as the learned edge weights can surface dependencies that
traditional correlation matrices might obscure. These practical
implications remain conditional on the caveats discussed in
Section VI-C, including survivorship bias in the evaluation
universe and simplified transaction cost assumptions.
From a theoretical perspective, performance gains from
sentiment integration suggest that markets may not fully
incorporate qualitative information immediately, a finding con-
sistent with bounded efficiency [1]. The 25% improvement
during earnings seasons suggests that social media may con-
tain early signals about investor reactions that have not yet
been absorbed into price. The effectiveness of graph-based
modeling is consistent with the view that markets function
as complex, interconnected systems rather than collections of
independent securities, though the limited evaluation universe
prevents strong generalization of this observation.
C. Limitations
The findings should be interpreted in light of limitations
spanning data selection, modeling assumptions, and economic
validity.
The most consequential concern is survivorship bias in
stock selection. The 20 stocks were chosen based on current
S&P 500 membership and data availability, meaning that
companies which failed, were acquired, or were delisted
between 1982 and 2025 are absent from the dataset. Because
the selected universe consists exclusively of companies that
ultimately succeeded, the dataset omits firms that experienced
bankruptcy, prolonged decline, or delisting, which are typically
less predictable and more volatile. Reported performance is
therefore likely inflated relative to what a real-time investor
would have experienced using historical index constituents,
and the results should be interpreted as demonstrating the
architecture’s effectiveness on a stable set of well-established,
liquid equities rather than as a guarantee of generalizable
performance across the full market. Constructing a point-in-
time universe from historical S&P 500 membership records,
including reconstitution events, would provide a more realistic
evaluation and is identified as a priority for future work.
Relatedly, the 20-node graph structure, while demonstrating
meaningful contribution in ablation studies (15% improve-
ment), represents a limited cross-section of the market. Larger
universes might better capture complex market topology, and
whether the learned edge weights retain predictive value as
the graph grows from 20 nodes to hundreds remains an open
question. The current design prioritizes temporal depth over
cross-sectional breadth, serving as a controlled environment
to validate the graph-based modeling approach before scaling
to broader equity populations.
Beyond stock selection, data-related assumptions also affect
generalizability. Edge weight initialization relies on corre-
lations computed over the training period (1982-2010), but
market correlations are inherently non-stationary. Relation-
ships that held during this window may weaken or reverse
by the test period. The learnable edge refinement mechanism
partially compensates by adapting weights during training,
though fundamental correlation regime shifts could still limit
generalization. Similarly, X (formerly Twitter) data availability
from 2007 onward means sentiment features are set to zero
for the 1982-2006 training period, creating a pronounced
imbalance: the sentiment fusion mechanism trains on only
four years of multimodal data (2007-2010) while the price-
based components benefit from 28 years of signal. Although
the adaptive gating mechanism mitigates this by learning
to suppress the sentiment channel when its input is zero,
the limited multimodal training window may constrain the
model’s ability to fully exploit sentiment-price interactions.
The ablation study (Section V-E) confirms that the architecture
retains strong performance without sentiment (MAPE 0.88%),
and the reported 10% improvement from sentiment integration
should be understood as a lower bound that could increase
with a longer sentiment training history. Sentiment analysis
also relies on English-language content from a single social
media platform, and changes to API access policies may affect
reproducibility.
From a practical standpoint, the economic significance
analysis applies a fixed 10 basis point transaction cost but
does not model variable market impact or execution slippage,
both of which increase with order size and decrease with
liquidity. The 32% daily turnover observed in the backtest
would amplify these unmodeled frictions, and the net re-
turns reported in Section V-E should be viewed as an upper
bound on realizable performance. Model complexity also
presents challenges for real-time high-frequency applications,
as the 252-day input sequence length and multi-head attention
mechanisms demand substantial computational resources. The
evaluation is performed on the same 20 stocks used for model
development, which limits assessment of external validity on
unseen securities.
D. Future Directions
Multiple directions merit investigation. A critical next step
is evaluating the framework on a point-in-time stock uni-
verse reconstructed from historical index membership records,
which would eliminate survivorship bias and provide a more
realistic assessment of real-world performance. Beyond bias
correction, expanding the stock universe to the full S&P 500
or international markets would test whether the graph-based
architecture scales effectively and whether inter-stock depen-
dencies remain informative as the number of nodes grows.
Incorporating multilingual sentiment sources and alternative
platforms (Reddit, financial news, earnings call transcripts)
would broaden the information base and reduce single-source
dependency. On the architectural side, developing more ef-
ficient attention mechanisms, such as sparse or linear atten-
tion variants, could enable real-time deployment for higher-
frequency trading applications. Regime-shift detection mech-
anisms that adjust model behavior during structural market
transitions (e.g., policy changes or liquidity crises) represent a
natural extension of the gating mechanism already present in
the model. Finally, integrating the forecasting framework with

17
portfolio optimization and formal risk management objectives
could bridge the gap between prediction accuracy and realized
economic value.
VII. CONCLUSION
This paper introduced an integrated framework that com-
bines a node transformer architecture with BERT-based senti-
ment analysis for stock price forecasting. The model represents
the stock market as a graph in which individual stocks serve
as nodes connected by learnable edges that encode sectoral
affiliations and price correlations. A fine-tuned BERT model
processes social media text to extract sentiment signals, which
are then merged with quantitative price features through an
adaptive attention-based fusion mechanism conditioned on
volatility and sentiment magnitude.
Experiments on 20 S&P 500 stocks spanning 1982 to 2025
yielded a MAPE of 0.80% for one-day-ahead predictions,
compared to 1.20% for ARIMA and 1.00% for LSTM. Ab-
lation studies isolated the contribution of each component:
removing sentiment raised error by 10% (and by 25% dur-
ing earnings seasons), while removing the graph structure
increased error by 15%. Directional accuracy reached 65%,
exceeding baselines by 7 to 10 percentage points, and both
paired t-tests and Diebold-Mariano tests confirmed statistical
significance across all comparisons (p <0.05), with the latter
accounting for autocorrelation in forecast residuals.
Taken together, these findings provide preliminary evidence
that jointly modeling inter-stock dependencies and investor
sentiment can improve forecast accuracy relative to architec-
tures that address either dimension in isolation. Several limi-
tations temper the strength of this conclusion: the evaluation
covers 20 large-cap U.S. equities selected with survivorship
bias, the sentiment training window spans only a fraction of
the full training period, and the economic backtest applies
simplified transaction cost assumptions. Whether these im-
provements extend to broader, historically reconstructed equity
universes and withstand realistic trading frictions remains an
open question that the current study cannot resolve. Future
work should prioritize evaluation on a point-in-time stock
universe, incorporate multilingual and multi-platform senti-
ment sources, investigate efficient attention variants for real-
time deployment, and integrate the forecasting pipeline with
portfolio optimization and formal risk management objectives.
ACKNOWLEDGMENT
The first author is grateful to Dr. Hussein Al Osman, whose
mentorship and thoughtful feedback shaped the direction of
this work from its earliest stages. His expertise in both
the technical and conceptual aspects of this research proved
invaluable.
REFERENCES
[1] E. F. Fama, “Efficient capital markets: A review of theory and empirical
work,”The Journal of Finance, vol. 25, no. 2, pp. 383–417, 1970.
[2] J. Zhang, Y . Teng, and W. Chen, “Stock market prediction via deep
learning techniques: A survey,”arXiv preprint arXiv:2212.12717, 2022.
[3] I. W. R. Martin and S. Nagel, “Market efficiency in the age of big data,”
Journal of Financial Economics, vol. 145, no. 1, pp. 154–177, 2022.
[4] I. Goldstein, “Information in financial markets and its real effects,”
Review of Finance, vol. 27, no. 1, pp. 1–32, 2023.
[5] D. Kahneman and A. Tversky, “Prospect theory: An analysis of decision
under risk,”Econometrica, vol. 47, no. 2, pp. 263–291, 1979.
[6] J. J. Murphy,Technical analysis of the financial markets: A comprehen-
sive guide to trading methods and applications. New York Institute of
Finance, 1999.
[7] T. Fischer and C. Krauss, “Deep learning with long short-term memory
networks for financial market predictions,”European Journal of Oper-
ational Research, vol. 270, no. 2, pp. 654–669, 2018.
[8] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” inAdvances in
Neural Information Processing Systems, vol. 30, 2017, pp. 5998–6008.
[9] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and S. Y . Philip, “A
comprehensive survey on graph neural networks,”IEEE Transactions
on Neural Networks and Learning Systems, vol. 32, no. 1, pp. 4–24,
2020.
[10] Q. Wu, W. Zhao, Z. Li, D. P. Wipf, and J. Yan, “Nodeformer: A scalable
graph structure learning transformer for node classification,” inAdvances
in Neural Information Processing Systems, vol. 35, 2022, pp. 27 387–
27 401.
[11] P. R. Low and E. Sakk, “Comparison between autoregressive integrated
moving average and long short-term memory models for stock price
prediction,”IAES International Journal of Artificial Intelligence, vol. 12,
no. 4, pp. 1828–1835, 2023.
[12] S. T. Wahyudi, “The ARIMA model for the indonesia stock price,”
International Journal of Economics and Management, vol. 11, pp. 223–
236, 2017.
[13] R. K. Nayak, D. Mishra, and A. K. Rath, “A na ¨ıve SVM-KNN based
stock market trend reversal analysis for Indian benchmark indices,”
Applied Soft Computing, vol. 35, pp. 670–680, 2015.
[14] M. Siddique and D. Panda, “Prediction of stock index of Tata Steel using
hybrid machine learning based optimization techniques,”International
Journal of Recent Technology and Engineering, vol. 8, pp. 3186–3193,
2019.
[15] S. Basak, S. Kar, S. Saha, L. Khaidem, and S. R. Dey, “Predicting the
direction of stock market prices using tree-based classifiers,”The North
American Journal of Economics and Finance, vol. 47, pp. 552–567,
2019.
[16] S. K. Chandar, “Convolutional neural network for stock trading using
technical indicators,”Automated Software Engineering, vol. 29, pp. 1–
14, 2022.
[17] M. Wen, P. Li, L. Zhang, and Y . Chen, “Stock market trend prediction
using high-order information of time series,”IEEE Access, vol. 7, pp.
28 299–28 308, 2019.
[18] L. Di Persio and O. Honchar, “Recurrent neural networks approach
to the financial forecast of Google assets,”International Journal of
Mathematics and Computers in Simulation, vol. 11, pp. 7–13, 2017.
[19] M. A. Hossain, R. Karim, R. Thulasiram, N. Bruce, and Y . Wang,
“Hybrid deep learning model for stock price prediction,” inProceedings
of the IEEE Symposium Series on Computational Intelligence, 2018, pp.
1837–1844.
[20] Y . Xu, L. Chhim, B. Zhenget al., “Stacked deep learning structure with
bidirectional long-short term memory for stock market prediction,” in
Communications in Computer and Information Science, vol. 1265, 2020,
pp. 447–460.
[21] M. Liu, H. Sheng, N. Zhanget al., “A new deep network model for stock
price prediction,” inInternational Conference on Machine Learning for
Cyber Security, 2022, pp. 413–426.
[22] T. N. Kipf and M. Welling, “Semi-supervised classification with graph
convolutional networks,” inProceedings of the International Conference
on Learning Representations, 2017.
[23] W. Chen, M. Jiang, W.-G. Zhang, and Z. Chen, “A novel graph
convolutional feature based convolutional neural network for stock trend
prediction,”Information Sciences, vol. 556, pp. 67–94, 2021.
[24] C. Wang, H. Liang, B. Wang, X. Cui, and Y . Xu, “MG-Conv: A spa-
tiotemporal multi-graph convolutional neural network for stock market
index trend prediction,”Computers and Electrical Engineering, vol. 103,
p. 108285, 2022.
[25] D. Le, S. Rajasegarar, W. Luo, T. T. Nguyen, N. V o, Q. Nguyen, and
M. Angelova, “EGCN: Entropy-based graph convolutional network for
anomalous pattern detection and forecasting in real estate markets,”
PLoS ONE, vol. 20, no. 10, p. e0334141, 2025.
[26] D. Le, S. Rajasegarar, W. Luo, T. T. Nguyen, and M. Angelova,
“Enhancing real estate prediction with entropy-based pattern analysis
and economic sentiment integration,”Engineering Computations, pp.
1–24, 2025.

18
[27] S. Li and Z. Qian, “A financial forecasting model based on transformer
architecture,” inProceedings of the IEEE International Conference on
Big Data, 2019, pp. 5384–5386.
[28] W. Lu, J. Li, J. Wanget al., “A CNN-BiLSTM-AM method for stock
price prediction,”Neural Computing and Applications, vol. 33, pp.
4741–4753, 2021.
[29] Y . Nejatbakhsh and M. Aliasgari, “Enhancing stock market prediction
with hybrid deep learning: Integrating LSTM, transformer attention,
federated learning, and sentiment analysis,”IEEE Access, vol. 14, pp.
3926–3942, 2025.
[30] K. Cortis, A. Freitas, T. Daudert, M. Huerlimann, M. Zarrouk, S. Hand-
schuh, and B. Davis, “SemEval-2017 task 5: Fine-grained sentiment
analysis on financial microblogs and news,” inProceedings of the 11th
International Workshop on Semantic Evaluation (SemEval-2017), 2017,
pp. 519–535.
[31] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-
training of deep bidirectional transformers for language understanding,”
inProceedings of the Conference of the North American Chapter of the
Association for Computational Linguistics, 2019, pp. 4171–4186.
[32] F. X. Diebold and R. S. Mariano, “Comparing predictive accuracy,”
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
Ottawa, Canada. He is a Full Professor and Associate
Director in the School of Electrical Engineering
and Computer Science at the University of Ottawa,
where he leads the Multimedia Processing and In-
teraction Group. His research focuses on affective
computing, multimodal affect estimation, human–
computer interaction, serious gaming, and multime-
dia systems. He has produced over 50 peer-reviewed
research articles, two patents, and several technology
transfers to industry.
