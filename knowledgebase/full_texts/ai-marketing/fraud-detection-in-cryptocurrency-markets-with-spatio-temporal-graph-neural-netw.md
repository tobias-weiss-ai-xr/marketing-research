---
title: Fraud Detection in Cryptocurrency Markets with Spatio-Temporal Graph Neural Networks
url: https://arxiv.org/abs/2604.24590
category: ai-marketing
subcategory: measurement
date: 2026-04
venue: ''
authors:
- Lidia Losavio
- Luca Persia
- Madan Sathe
- Dimosthenis Pasadakis
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.24590
pages: 9
chars: 45453
fetched_at: '2026-11-08T13:26:28+00:00'
kb_version: 1
---

# Fraud Detection in Cryptocurrency Markets with Spatio-Temporal Graph Neural Networks

Fraud Detection in Cryptocurrency Markets with
Spatio-Temporal Graph Neural Networks
Lidia Losavio ∗1, Luca Persia ∗†1 , Madan Sathe ‡, and Dimosthenis Pasadakis ∗
∗Faculty of Informatics, Universit `a della Svizzera italiana, Lugano, Switzerland
†School of Management and Law, Zurich University of Applied Sciences, Zurich, Switzerland
‡Forensics and Financial Crime, Deloitte AG, Switzerland
{lidia.anna.maria.losavio, luca.persia, dimosthenis.pasadakis}@usi.ch, msathe@deloitte.ch
Abstract—Technological advancements in cryptocurrency mar-
kets have increased accessibility for investors, but concurrently
exposed them to the risks of market manipulations. Existing
fraud detection mechanisms typically rely on machine learning
methods that treat each financial asset (i.e., token) and its
related transactions independently. However, market manipulation
strategies are rarely isolated events, but are rather characterized
by coordination, repetition, and frequent transfers among related
assets. This suggests that relational structure constitutes an
integral component of the signal and can be effectively represented
through graphical means. In this paper, we propose three
graph construction methods that rely on aggregated hourly
market data. The proposed graphs are processed by a unified
spatio-temporal Graph Neural Network (GNN) architecture
that combines attention-based spatial aggregation with temporal
Transformer encoding. We evaluate our methodology on a
real-world dataset comprised of pump-and-dump schemes in
cryptocurrency markets, spanning a period of over three years.
Our comparative results showcase that our graph-based models
achieve significant improvements over standard machine learning
baselines in detecting anomalous events. Our work highlights
that learned market connectivity provides substantial gains for
detecting coordinated market manipulation schemes.
Index Terms—spatio-temporal Graph Neural Network, market
manipulation, pump-and-dump, cryptocurrency, fraud detection
I. INTRODUCTION ANDRELATEDWORK
Financial market manipulation is the attempt to distort the
process by which the prices of financial assets are formed,
so that they no longer reflect real information about supply
and demand [1]. This encompasses many behaviors, but a
useful research taxonomy distinguishes between trading-based,
information-based and action-based manipulation [2].
These phenomena can be traced back to the stock market
itself [2], yet there has recently been a notable surge in
manipulative behaviour in the cryptocurrency markets. The
fragmented liquidity and less stringent regulation of these
markets may amplify the impact of manipulative activity, as
discussed in [3]. Notable recent cases [4], [5] highlight that such
fraudulent activities have a detrimental effect on both investors
and on the credibility of the blockchain as an innovative system.
The coordination of market manipulation in crypto markets
often occurs on encrypted messaging platforms, where channels
are established with the objective of attracting speculators [6].
1Equal contribution.
Empirically, these ”campaigns” may leave distinct footprints
in the price and the traded volume of the tokens. At the event
level one typically observes: (i) a sudden increase in trading
volume and number of trades over a short time interval, (ii)
heavy concentration of activity on a single exchange or venue,
and (iii) potential clustering of events in time, as the same
groups may run multiple campaigns in quick succession. The
existence of these distinct patterns in cryptocurrency market
manipulation motivates a statistical learning approach for their
early detection.
The current state-of-the-art methods for detecting financial
market frauds exploit the underlying structure of financial
interactions [7]. They leverage graphical representations of
financial data and deep learning, particularly graph neural
networks (GNNs) [8], to capture relational patterns in the
network [9], [10]. For cryptocurrencies in particular, fraud
detection is increasingly graph-oriented, learning directly from
interaction networks rather than just price or volume anomalies.
In [11]–[13] transaction-level cryptocurrency information is
exploited (e.g., sender-receiver directed graphs), which inher-
ently implies a direct notion of the graphical structure of
the problem. However, many accessible real-world datasets
provide only aggregated market observations at the token
level, such as OHLCV information (open, high, low, close
prices and trading volume) over fixed time intervals, number
of trades, and derived indicators. In this context, the relational
structure between activities is not directly observed, as there
are no explicit edges or direct notions of relational interactions.
Consequently, a graph-based approach requires constructing
an adjacency structure from aggregated time series, with
different constructions leading to different inductive biases
in the downstream GNN models.
Contributions and outline
We introduce a framework that enables Spatio-Temporal
GNN (ST-GNN) modeling through specific graph construction
methods, utilizing only aggregated market data. To strictly
evaluate and compare these construction strategies, we employ
a unified ST-GNN predictor across all experiments. This
architecture processes data in two stages: first, for each
timestamp in a lookback window, a Transformer-style spatial
GNN computes node embeddings based on the constructed
1
arXiv:2604.24590v1  [cs.LG]  27 Apr 2026

graph. Second, these spatial embeddings are stacked into a
sequence, enriched with positional encodings, and processed
by a temporal Transformer encoder to map the spatiotemporal
context to a final event probability. For the graph construction,
we follow a correlation-based construction approach [14]
that quantifies co-movement in market aggregates during the
training period. We adapt this idea to the problem of fraud
detection in cryptocurrency markets, and derive the adjacency
matrix from correlation coefficients, which we then sparsify via
set thresholds. This graph construction approach is extended
beyond a single static topology with two dynamic variants.
Additionally, we consider a self-adaptive graph construction
variant that learns latent dependencies directly from the data,
capturing interactions beyond feature-based correlations.
Our approach is evaluated on a real-world dataset of
pump-and-dump (P&D) events extracted from [15] detected
in the period 2017-2021. The three ST-GNN variants are
compared against the widely used decision-tree methods
Random Forests [16] and XGBoost [17]. Unlike existing
P&D detection datasets, where the learning problem is formed
by extracting a local window around each pump event and
concatenating these labeled segments [6], [15], we consider
a global historical window that is shared across all tokens in
the sample. While local windows are well-suited to measuring
event signatures, they also condition the sample on being near
a pump, thereby discarding most daily market variation. This
can reduce background market movements and may lead to
an optimistic assessment of detection difficulty, i.e., a form of
selection bias in the evaluation that results in high accuracy
metrics. Our global window approach shifts the task toward
a more realistic surveillance setting, i.e., a highly imbalanced
learning problem in which fraudulent episodes are rare relative
to the full stream of normal market activity. In particular, in
our constructed dataset, we observe ∼0.016% of anomalous
events in a total of∼1.9×10 6 observations.
The remainder of this paper is organized as follows. In
Section II, we briefly recap the problem of detecting fraudulent
events when assuming aggregated market data samples, and
present a high level overview of our approach. In Section III
we focus on our method for estimating graphs from these
samples, and using them as input in a ST-GNN architecture to
detect anomalous events. In Section IV, we perform numerical
experiments on real-world data and compare with state-of-the-
art decision-tree methods in order to validate our proposed
routines, and finally in Section V we draw conclusions from
this work. Our code and data are publicly available at https:
//github.com/lidialosavio-dotcom/crypto fraud stGNN.
Notation
In what follows, we denote scalar quantities with lowercase,
vectors with lowercase bold, and matrices with uppercase bold
characters. The (i, j)th entry of a matrix A is symbolized
by Aij and all entries in row i or column j by Ai: and A:j,
respectively. Sets are denoted by capital calligraphic characters,
for example, A, the identity matrix as I and the vector of all
ones ase.
II. FRAUDDETECTION WITHAGGREGATEDMARKETDATA
We address the detection of cryptocurrency fraud events
at the token level, with hourly resolution using aggregated
market data. In II-A we formally introduce the problem, and
in II-B its formulation within a Graph Neural Network (GNN)
architecture.
A. Problem setting
Let V={1, . . . , N}be the set of traded tokens and let
t∈ {1, . . . , T}be the index of discrete hourly timestamps. For
each token i∈V at time t, we observe a vector of aggregate
features xi,t ∈R F and a binary label yi,t ∈ {0,1}indicating
whether a fraudulent episode occurs for token i at time t. Let
Xt ∈R N×F be the matrix containing all the feature vectors
of the tokens at time t. Our goal is to learn a predictor fθ that
estimates the probability ˆpi,t of fraud for a specific token i at
timet,
ˆpi,t =f θ(xi,t,x i,t−1, . . . ,xi,t−W+1 )∈[0,1],
ˆyi,t =I{ˆpi,t ≥γ}, (1)
where W is the lookback window and γ∈(0,1) is a decision
threshold to determine the binary prediction ˆyi,t. In practice,
xi,t typically includes OHLCV variables, trade counts, and
additional engineered features, so that time-series information
is available in tabular form.
B. Formulation within a GNN architecture
Graph Neural Networks (GNNs) are architectures designed
to learn from graph-structured data by iteratively updating node
representations through information exchange along edges (i.e.,
message passing) [18]. Let h(k) i ∈R D denote the embedding
of node i after the k-th propagation step, with h(0) i typically
initialized from the input features, i.e., h(0) i =x i,t. A generic
update then reads
h(k) i = U(k)

h(k−1) i ,AGG (k)

{h(k−1) j :j∈N(i)}  ,(2)
where N(i) is the neighborhood of i, AGG(k)(·) is a
permutation-invariant aggregating function over neighbors
(e.g., sum/mean/max), and U(k)(·) is typically implemented
by a Multilayer Perceptron (MLP). The number of steps k
controls the propagation depth; after k steps, h(k) i incorporates
information from nodes up tokhops away.
In our setting, nodes correspond to traded tokens and edges
encode inter-token relations derived from aggregated market
dynamics. A spatio-temporal GNN (ST-GNN) extends message
passing to time-indexed observations by combining a spatial
graph aggregation at each time t with a temporal model that
captures how node representations evolve across a lookback
window [19]–[21]. Many GNN variants can be interpreted
within this message-passing template, differing mainly in the
way neighbor information is computed and propagated [22]–
[24].
A practical constraint in cryptocurrency fraud detection arises
from relying on exchange- or aggregator-provided APIs [25],
[26] for data collection. These sources typically expose only
2

market-level aggregates per token and time (e.g., OHLCV
and related features) rather than transaction-level interactions.
Consequently, the relational structure between assets remains
latent, as there are no explicit edges and any notion of
connectivity must be inferred from the observed time series [27].
This limits the applicability of many graph-based approaches
that rely on a pre-defined interaction network, thus motivating
the development of methods capable of constructing graphs
from aggregated data, and utilizing them in the prediction task.
III. INFERENCEGRAPHSMETHODS AND AUNIFIED
SPATIO-TEMPORALGNN
We infer the graphical structure of token interactions from ag-
gregated data, and utilize it in a spatio-temporal GNN to detect
fraudulent events. Subsection III-A defines data representation
and temporal windowing, and in Subsection III-B introduces
our graph inference strategies. Then, Subsection III-C details
the proposed GNN architecture.
A. Data representation and temporal windowing
Given the node feature matrix Xt ∈R N×F , temporal context
is captured through a fixed lookback window of length W . For
each nodei∈Vat timet, we form the sequence
X(W) i,t =  xi,t−W+1 , . . . ,xi,t  ∈R W×F .(3)
Stacking these sequences for all nodes yields the windowed
tensor X(W) t ∈R N×W×F , whose i-th slice satisfies X(W) t [i,:
,:] =X (W) i,t . The model outputs a probability per node for the
current timet, i.e., ˆpt ∈[0,1] N .
B. Graph inference strategies
We denote by At ∈R N×N a weighted adjacency matrix
at time t, and by Et ={(i, j) :At,ij ̸= 0}the corresponding
directed edge set. Undirected connections are treated as directed
edges from i to j and vice versa. When required for message
passing, we equivalently represent At as an edge list Et with
associated edge weights at ={A t,ij : (i, j)∈E t}. Since
the underlying market graph is latent, we define an inference
operator
At =g t(D≤t),(4)
which constructs At relying solely on information available up
to time t. This ensures that the graph construction respects the
temporal order of observations, and in practice, is restricted only
to training timestamps when building training-time graphs [28].
Here, D≤t denotes the observed aggregated market data up to
time t, i.e., the time series of token-level data used to build Xt
and any scalar time series si,t employed by the graph inference
rule. We evaluate three graph construction methods for gt, and
summarize them in Algorithm 1.
(G1) Static correlation graph
We construct a single weighted adjacency from the training
period and reuse it at every timestamp. Let Ttr ⊆T denote the
set of training timestamps. Given a scalar time series si,t for
each token i, obtained from a single chosen node feature (e.g.,
Algorithm 1Graph inference strategies from aggregated data
Input: Training timestamps Ttr, fraud timestamps Ptr, scalar
feature si,t, density ρ, min threshold τmin, dynamic horizon
L=12, self-adaptive thresholdϵ
Output: Inferred adjacency (static A, dynamic updates
{A(p)}, or self-adaptiveA)
(G1) Static
1:ComputeConT tr fromlog(1 +s i,t)
2:τ←max(τ min, Qρ({Cij}i<j))
3:A ij ←C ij ·I{C ij > τ}
(G2) Dynamic event-driven
4:foreachp∈P tr in chronological orderdo
5:W(p)← {p−L, . . . , p}
6:ComputeC (p) onW(p)
7:τ (p) ←max(τ min, Qρ({C (p) ij }i<j))
8: Add/update edges (i, j)where C (p) ij > τ (p) using
running mean
9:SaveA (p)
10:end for
(G3) Self-adaptive
11:LearnE 1,E 2 ∈R N×d ; computeM←E 1E⊤ 2
12:A←softmax(ReLU(M))(row-wise)
13:Sparsify: keep(i, j)only ifA ij > ϵ
volume or number of trades), we define the log-transformed
token-by-time matrixS∈R |Ttr|×N with entries:
St,i = log(1 +si,t), t∈T tr, i∈ {1, . . . , N}.(5)
We compute the Pearson correlation matrix C∈[−1,1] N×N
and set the diagonal entries to zero:
Cij = Corr

S:,i,S :,j

, C ii = 0.(6)
To sparsify this matrix, we select a data-driven threshold τ via
an off-diagonal quantile, subject to a minimum floorτ min:
τ= max
n
τmin, Qρ

{Cij}i<j
o
, A ij =C ij I{Cij > τ},
(7)
with Aii = 0 and (i̸=j) . Here Qρ denotes the ρ-quantile
of the off-diagonal entries. This threshold retains only the
strongest edges, i.e., the top 1−ρ fraction of them, while τmin
ensured that retained edges represent statistically meaningfull
correlations.
Since the resulting adjacency matrix is time-invariant, we
have At =A,∀t. This approach assumes that even without
explicit interactions, tokens can exhibit synchronized market
activity. A static correlation graph is the simplest relational
inductive bias compatible with aggregated token features [29].
(G2) Event-driven dynamic correlation graph
Static graphs often fail to capture correlation shifts associated
with manipulation episodes, as they rely on a fixed represen-
tation of the data, and do not update over time [30]. Our
second graph construction approach addresses this limitation
by constructing a piecewise-constant adjacency matrix that
updates only around fraud events within the training data.
3

Let Ptr ⊆T tr be the set of training timestamps where at
least one fraud event occurs. For each p∈P tr, we consider a
lookback window ofLhours:
W(p) ={p−L, . . . , p} ∩Ttr.(8)
Note that L denotes a graph construction lookback window,
distinct from the feature window W in Section III-A. Using
the same scalar series si,t as in (G1), derived from volume or
number of trades, we compute a window-specific correlation
matrix C(p) from {log(1 +s i,t) :t∈W(p)} , enforcing
again C (p) ii = 0. We then select edges representing significant
interactions with a density-controlled threshold:
τ (p) = max n τmin, Qρ  {C (p) ij }i<j o ,(9)
E(p) ={(i, j) :i < j, C(p) ij > τ(p)}.(10)
For each undirected edge (i, j)we keep a cumulative sum Sij of
the correlation coefficients C (p) ij , and a counter nij representing
the number of fraud event windows where the edge (i, j)was
part of the graph, i.e., (i, j)∈E (p). The resulting edge weight
is defined as the mean of these correlations, wij =S ij/nij.
The updated adjacency matrix A(p) is formed by setting A(p) ij =
A(p) ji =w ij andA (p) ij = 0otherwise.
At any time t, the model uses the graph state in the training
set of the most recent fraud timestampp ⋆,
At =
(
I,if{p∈P tr :p≤t}=∅,
A(p⋆), p ⋆ = max{p∈P tr :p≤t}. (11)
For timestamps in the validation and testing sets, the graph
A(plast) of the last training update is considered, with plast =
maxP tr being the last fraud event timestamp in the training
set.
(G3) Self-adaptive adjacency from node embeddings
While correlation-based graphs capture statistical synchro-
nization between assets, they rely on fixed heuristic thresholds
to determine connectivity, and thus, may not align with
the optimal latent graph for fraud detection. To allow our
model to discover latent dependencies directly from the data,
we employ a self-adaptive adjacency construction approach
inspired by [31].
We randomly initialize two learnable node embedding
dictionaries E1,E 2 ∈R N×d , representing source and target
node embeddings, respectively. These embeddings are opti-
mized together with the neural network weights via stochastic
gradient descent, guided solely by minimizing the supervised
classificaiton objective. The hyperparameter d controls the rank
of the learned adjacency matrix A. The adjacency matrix, that
can be considered as the transition matrix of a hidden diffusion
process [31], is then computed as
A= SoftMax

ReLU(E1E⊤ 2 )  .(12)
Here, the ReLU activation function eliminates weak or negative
connections, while the row-wise SoftMax normalizes the
weights to obtain a row-stochastic adjacency.
To sparsify this dense graph, we set edges with weights
below a small tuned constantϵto zero:
E={(i, j) :A ij > ϵ}, A ij ←A ijI{Aij > ϵ},(13)
Unlike the undirected graphs in (G1) and (G2), this approach
generates an unsymmetric matrixA̸=A ⊤.
C. ST-GNN architecture
All inferred graphs are used within the same spatio-temporal
model architecture. At each hour t, the inferred adjacency
At defines the neighborhood Nt(i) ={j:A t,ij ̸= 0}. We
encode (i) spatial interactions on At with a Transformer-style
attention GNN layer [32], and (ii) temporal dependencies via a
Transformer encoder over an W -hour lookback window [20],
[33].
First, spatial aggregation is performed at each time step. For
each node i∈V , the input feature vector xi,t is mapped to
a spatial embedding hi,t ∈R D via attentive message passing
overA t:
hi,t = GraphTransformer(xi,t,A t).(14)
Subsequently, we construct the temporal sequence by stacking
the embeddings from the lookback windowW:
Hi,t =

hi,t−W+1 , . . . ,hi,t

∈R W×D .(15)
We add learnable positional encodings intoH i,t, and process
the sequence with a temporal Transformer encoder, denoted
by TE(·). The fraud event probability for node i at time t is
obtained by
ˆpi,t =σ

w⊤TE(Hi,t)[W] +b  ,(16)
where w∈R D and b∈R are learnable output parameters and
σ(·) is the sigmoid logistic function. Algorithm 2 summarizes
the forward pass.
IV. NUMERICALRESULTS
In this section, we present experimental results on real-world
data for an extensive evaluation of the accuracy and efficacy of
the proposed graph-based fraud detection routines outlined in
Section III. We will compare our methods against the following
decision-tree based ensemble methods:
1) Random Forests (RF) [16]: Aggregates predictions from
decorrelated decision trees trained on bootstrap samples
and feature subsampling. We use a grid search to optimize
the number of estimators nest ∈ {500,1000}), maximum
tree depth dmax ∈ {12,∞}, minimum samples per leaf
nmin ∈ {1,10}, and the feature subset size considered at
each splitF sub ∈ {
√
F ,0.8F}.
2) eXtreme Gradient Boosting (XGBoost) [17]: A gradient-
boosted tree method that sequentially fits trees to correct
previous errors. We tune the learning rate η∈ {0.05,0.1},
maximum tree depth ( dmax ∈ {4,10}), number of es-
timators ( nest ∈ {500,1000}), and L2 regularization
parameter λ∈ {1.0,10.0}, while fixing row and column
subsampling rates at0.8.
4

Algorithm 2ST-GNN forward pass
Input: Windowed node features X(W) t ∈R N×W×F , inferred
graph(E t,a t)wherea t are edge weights, parametersθ
Output:Event probabilities ˆpt ∈[0,1] N
1:seq←[ ]▷will store spatial embeddings for each hour
in the window
2:foru= 1toWdo▷iterate over window steps
3:H←W inX(W) t [:, u,:]▷linear projection
4:H←TransformerConv 1(H,E t,a t)
5:H←ReLU(H);H←Dropout(H)
6:H←TransformerConv 2(H,E t,a t)
7:H←ReLU(H)
8:seq.append(H)
9:end for
10:S←Stack(seq)∈R N×W×D
11:S←S+P▷positional embedding
12: ˜S←TemporalTransformerEncoder(S)
13:z← ˜S[:, W,:]▷last time token
14: ˆpt ←σ(W outz+b)
15:return ˆpt
The following Subsection IV-A summarizes our experimental
setup, and then IV-B is devoted in a comparison of the accuracy
of the methods under consideration.
A. Experimental setup
We consider a real-world dataset of pump-and-dump events
from, covering the period July 2017 – January 2021, where
labels where assigned by monitoring encrypted messaging
platforms and linking each market manipulation campaign to
a target token [34]. We collect the available market data for
quote currency BTC through the Binance API [25], and assign
a unique timestamp by combining the date and hour fields and
localizing the resulting time to UTC. Since market data are
represented as hourly candles 1, pump timestamps are rounded
to the nearest hour boundary to enforce a consistent alignment
between the pump schedule and the candle grid. A pump
episode from our dataset is illustrated in Figure 1, where the
number of trades spikes sharply around the event time for two
tokens, highlighting both the market signature of coordinated
activity and the presence of cross-token co-movement that
motivates our graph-based approach.
For each token we download a continuous time interval
spanning from the earliest to the latest pump timestamp in the
schedule, both extended by a fixed margin of seven days.
Consequently, all tokens share the same time boundaries,
resulting in a panel that includes both normal market activity
and rare fraud episodes, contains the candle timestamp, OHLCV
information and trading activity. The binary fraud label flag is
assigned by checking whether the candle timestamp belongs
1In financial market microstructures, a candle (or candlestick) aggregates
trading activity over a fixed time interval and is typically represented by the
OHLC information, together with volume and related trade counts for that
interval.
03-23 03-24 03-25 03-26 03-27
0
2,000
4,000
6,000
Time
Number of Trades
BRD OAX
Fig. 1:Hourly number of trades for BRD and OAX over a four-day window
around one pump event.
to the set of pump timestamps associated with that token. The
dataset contains 1,905,850 observations for N= 84 tokens.
The positive class (flagged pump hours) includes 314 positives,
corresponding to a positive rate of∼0.016%.
We compute 18 additional features on this base panel to
capture abrupt regime shifts, typical of coordinated manipu-
lation. Since our dataset is limited to candle-level aggregates
and does not include order-book information (e.g., bid–ask
depth or spread), we construct a proxy for aggressive buy
pressure using the ratio between taker buy quote volume and
total traded volume at the candle level. For each token, we
compute rolling statistics over a fixed window of 12 hours and
then consider their percentage change over time, following the
feature construction in [34]. Such percentage changes of rolling
means or rolling standard deviations quantify how quickly the
local average or local variability is shifting, which is the type
of signal expected under coordinated activity. Following this
approach, we compute percentage changes of rolling mean
and standard deviation for the buy pressure, traded volume,
number of trades, and close price. We then compute the
same transformation for the rolling mean of the intraperiod
maximum price. Last, since intraday patterns can be relevant
when campaign timing is systematic, we derive an hour feature
as the integer hour extracted from the timestamp. The full list
of the features considered is offered in Table I in Section VI
of the Appendix.
To respect temporal ordering and emulate a surveillance
setting, we adopt a chronological hold-out split for all consid-
ered models. Let T denote the ordered set of unique hourly
timestamps in the panel. We partition T into 60% for training,
20% for validation, and 20% for testing. Graph construction
using historical observations is performed using only the
training data, model hyperparameters and early stopping criteria
are selected on the validation set. The decision threshold γ is
also selected on the validation set by maximizing the F1-score,
and the same threshold is applied unchanged to the test set,
5

XGBoost RF Static (V olume) Dyn (V olume) Dyn (Num. Trades) Static (Num. Trades) Self-Adaptive
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Method
F1 score
(a)
0.5 0.6 0.7 0.8 0.9 1
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Recall
Precision
(b)
Fig. 2:Classification performance for all methods under consideration. (a) F1-score, and (b) mean precision-recall curves forRecall∈[0.5,1].
which is utilized only for the final accuracy estimation. Then, to
mitigate short-range temporal dependence and reduce leakage
around split boundaries, an embargo of z= 5 hours is adopted
and the first z timestamps of the validation and test blocks are
discarded [35]. We evaluate performance in terms of precision,
recall, and F1 score, defined as:
F1-score= 2· Precision·Recall Precision + Recall,(17)
where precision is defined as Precision = TP/(TP + FP)
and recall as Recall = TP/(TP + FN), with TP, FP,
and FN denoting true positives, false positives, and false
negatives classifications, respectively. All the results reported
hereby correspond to their mean value after 9 runs. For all
experiments, we employ the ST-GNN architecture defined in
Section III-C with a fixed learning rate of 10−3, and a spatial
embedding dimension of D= 64 (Eq. 14), 2 attention heads,
and a temporal window of W= 5 hours. Regarding graph
construction, for the correlation-based strategies (G1, G2),
we set the minimum threshold to τmin = 0.15, the dynamic
lookback window to L= 12. The quantile density in (G1) is
set to ρ= 0.90 when considering the number of trades, to 0.75
when considering the volume, and to 0.95 for both dynamic
variants in (G1). Finally, for the self adaptive graph (G3), the
learnable embedding dimension is d= 48 and the sparsity
threshold is ϵ= 0.005. The complete grid search spaces and
selected configurations for all graph inference strategies are
reported in Table II in Appendix VI-B. All the results reported
hereby correspond to their mean value after 9 runs.
B. Classification performance
We present in Figure 2a the F1-score (17) of the classification
of the minority (i.e., fraudulent) class. The two tree-based
methods achieve the lowest scores, with XGBoost (in black)
yielding the lowest F1 = 0.49±0.03 and Random Forests
(in purple) improving upon it with F1 = 0.53±0.01. All our
introduced graph-based variants outperform these baselines
in terms of classification accuracy. The static graph based on
volume correlation (in brown), and its dynamic counterpart
(in orange) achieve F1 = 0.575±0.04 and F1 = 0.58±0.02,
respectively. The strongest correlation-based performance is
obtained when connectivity is derived from the number of
trades as a proxy for trading activity with F1 = 0.58±0.04
for the dynamic graph (in blue) and F1 = 0.60±0.04) for
the static one (in green). The self-adaptive graph (in red)
achieves the best overall accuracy with F1 = 0.62±0.05 ,
indicating that allowing the model to adjust connectivity during
training is beneficial when the graph topology is not available.
The moderate error bars across seeds confirm that these
rankings are stable and not driven by favorable initializations.
To further validate that the observed gains stem from the
graph structure rather than from increased model capacity, we
evaluate temporal-only baselines (GRU, TransformerEncoder)
that process each token independently; full details are provided
in Appendix VI-C. A comparison of model sizes and training
times is reported in Table III in Appendix VI-D.
In Figure 2b, we report the mean Precision-Recall (PR)
curves for Recall∈[0.5,1] . Given the extreme class imbalance
in our test set, containing only ∼0.016% positive pump hours
in a total of ∼1.9×10 6 hours, we prioritize PR curves
over ROC analysis, as the latter can be insensitive to the
false-positive burden when negatives dominate [36]. The plot
highlights a consistent performance gap, with graph-based
models shifting the PR frontier upward relative to the tree-based
baselines, implying higher precision for any given recall level.
6

XGBoost RF Static (V olume) Dyn (V olume) Dyn (Num. Trades) Static (Num. Trades) Self-Adaptive
APPC NXS
0
0.2
0.4
0.6
0.8
1
F1 score
Fig. 3:Classification performance in terms of F1-score for all methods under consideration for tokens (i.e., APPC and NXS) with at least five pump events in
the test set.
While performance naturally degrades as recall approaches 1,
our graph-based methods maintain precision levels significantly
longer than the tree-based baselines. The best method is the
self-adaptive variant, which dominates the frontier across the
majority of the sensitivity range.
In Figure 3 we present the classification performance in
terms of F1-score (17) for the most affected tokens, with at
least five recorded pump events in the test set. All graph-
based variants introduced in Subection III-B report accuracy
scores higher than the competing tree-based methods. The
self-adaptive variant (in red) achieves the highest scores with
F1 = 0.808±0.05for APPC and F1 = 0.931±0.06for NXS,
where APPC and NXS are individual token ticker symbols,
each representing a single node in the graph.
V. CONCLUSIONS
We presented a framework to detect manipulation in cryp-
tocurrency markets, specifically addressing the scenario where
only aggregated market data are available, i.e., OHLCV and
trading activity, while transaction-level information remains
unobservable. To overcome this limitation, we proposed a
methodology that infers token-to-token connectivity from
market dynamics, and processes it via a unified spatio-temporal
GNN (ST-GNN) architecture. We proposed three graph in-
ference methods: static correlation, event-driven dynamic
correlation, and self-adaptive adjacency learning.
We compared our graph-based solutions against tree-based
methods on a real-world labeled dataset of pump-and-dump
schemes spanning the period 2017–2021. Our results demon-
strate that graph-based models are superior in terms of
F1-score and Precision-Recall efficiency. Notably, the self-
adaptive adjacency method achieved the highest fraud detection
performance, confirming that the model can successfully learn
latent interaction structure between tokens. Our work highlights
the effectiveness of the introduced graph-based fraud detection
algorithms, and their applicability for the monitoring of market
manipulation events.
ACKNOWLEDGMENT
We acknowledge the financial supported by the joint DFG-
470857344 and SNSF-204817 project entitled “Numerical Al-
gorithms, Frameworks, and Scalable Technologies for Extreme-
Scale Computing”, and by the Huawei Zurich Research
Center. This work was also funded by the “Resilient Financial
Enterprises” project, supported by the Swiss Innovation Agency
(Innosuisse) under grant agreement 119.321 INT-ICT.
REFERENCES
[1] Netherlands Authority for the Financial Markets (AFM), “Market
manipulation,” Regulatory brochure (Market Abuse Regulation context),
2017, brochure processed ESMA Q&As up to 6 July 2017.
[2] T. J. Putni n ¸ˇs, “Market manipulation: A survey,” Journal of Economic
Surveys, vol. 26, no. 5, pp. 952–967, 2012.
[3] J. T. Hamrick, F. Rouhi, A. Mukherjee, A. Feder, N. Gandal, T. Moore,
and M. Vasek, “An examination of the cryptocurrency pump-and-dump
ecosystem,” Information Processing and Management, vol. 58, no. 4, p.
102610, 2021.
[4] S. Shifflett and P. Vigna, “Some traders are talking up cryptocur-
rencies, then dumping them, costing others millions,” The Wall
Street Journal, Aug. 2018, available at: https://www.wsj.com/graphics/
cryptocurrency-schemes-generate-big-coin/.
[5] B. Merewhuader, C. Polite, and T. Viane, “Class action complaint,
merewhuaderet al.v. safemoon llcet al., no. 2:22-cv-01108 (c.d. cal.
feb. 17, 2022),” Filed in U.S. District Court for the Central District of
California, 2022.
[6] J. Xu and B. Livshits, “The anatomy of a cryptocurrency Pump-and-Dump
scheme,” in 28th USENIX Security Symposium (USENIX Security 19).
Santa Clara, CA: USENIX Association, 2019, pp. 1609–1625.
[7] L. Akoglu, H. Tong, and D. Koutra, “Graph based anomaly detection and
description: a survey,” Data Mining and Knowledge Discovery, vol. 29,
no. 3, pp. 626–688, 2015.
[8] X. Ma, J. Wu, S. Xue, J. Yang, C. Zhou, Q. Z. Sheng, H. Xiong, and
L. Akoglu, “A comprehensive survey on graph anomaly detection with
deep learning,” IEEE transactions on knowledge and data engineering,
vol. 35, no. 12, pp. 12 012–12 038, 2021.
7

[9] Y . Dou, Z. Liu, L. Sun, Y . Deng, H. Peng, and P. S. Yu, “Enhancing graph
neural network-based fraud detectors against camouflaged fraudsters,” in
Proceedings of the 29th ACM International Conference on Information
& Knowledge Management (CIKM ’20). Virtual Event, Ireland:
Association for Computing Machinery, Oct. 2020.
[10] J. Schmidt, D. Pasadakis, M. Sathe, and O. Schenk, “GAMLNet: a graph
based framework for the detection of money laundering,” in 2024 11th
IEEE Swiss Conference on Data Science (SDS), 2024, pp. 241–245.
[11] C. Wu, J. Chen, Z. Zhao, K. He, G. Xu, Y . Wu, H. Wang, H. Li,
Y . Liu, and Y . Xiang, “Tokenscout: Early detection of ethereum scam
tokens via temporal graph learning,” in Proceedings of the 2024 on ACM
SIGSAC Conference on Computer and Communications Security, CCS
2024, Salt Lake City, UT, USA, October 14-18, 2024, B. Luo, X. Liao,
J. Xu, E. Kirda, and D. Lie, Eds. ACM, 2024, pp. 956–970.
[12] C. Wu, J. Chen, J. Li, J. Xu, J. Jia, Y . Hu, Y . Feng, Y . Liu, and Y . Xiang,
“Profit or deceit? mitigating pump and dump in defi via graph and
contrastive learning,” IEEE Transactions on Information Forensics and
Security, vol. 20, pp. 8994–9008, 2025.
[13] Z. Lin, Q. Luo, D. Wu, J. Shen, L. Li, X. Nong, and Z. Qin, “Detecting
illicit transactions in bitcoin: a wavelet-temporal graph transformer
approach for anti-money laundering,” Scientific Reports, vol. 16, no. 1,
p. 1548, 2026.
[14] K. da Costa, “Anomaly detection in global financial markets with graph
neural networks and nonextensive entropy,” 2023, arXiv:2308.02914v2.
[15] M. La Morgia, A. Mei, F. Sassi, and J. Stefa, “The pump and dump
scheme in the bitcoin era: Real time detection of cryptocurrency market
manipulations,” in 2020 29th International Conference on Computer
Communications and Networks (ICCCN). IEEE, 2020, pp. 1–9.
[16] L. Breiman, “Random forests,” Machine Learning, vol. 45, no. 1, pp.
5–32, 2001.
[17] T. Chen and C. Guestrin, “Xgboost: A scalable tree boosting system,”
in Proceedings of the 22nd ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining, ser. KDD ’16. New York, NY ,
USA: Association for Computing Machinery, 2016, p. 785–794.
[18] G. Corso, H. Stark, S. Jegelka, T. Jaakkola, and R. Barzilay, “Graph
neural networks,” Nature Reviews Methods Primers, vol. 4, no. 1, p. 17,
2024.
[19] B. Yu, H. Yin, and Z. Zhu, “Spatio-temporal graph convolutional net-
works: A deep learning framework for traffic forecasting,” in Proceedings
of the 27th International Joint Conference on Artificial Intelligence,
2018, pp. 3634–3640.
[20] G. Jin, Y . Liang, Y . Fang, Z. Shao, J. Huang, J. Zhang, and Y . Zheng,
“Spatio-temporal graph neural networks for predictive learning in
urban computing: A survey,” IEEE transactions on knowledge and data
engineering, vol. 36, no. 10, pp. 5388–5408, 2023.
[21] Z. Wu, S. Pan, G. Long, J. Jiang, X. Chang, and C. Zhang, “Connecting
the dots: Multivariate time series forecasting with graph neural networks,”
in Proceedings of the 26th ACM SIGKDD International Conference on
Knowledge Discovery & Data Mining, 2020, pp. 753–763.
[22] T. N. Kipf and M. Welling, “Semi-supervised classification with
graph convolutional networks,” in 5th International Conference on
Learning Representations, ICLR 2017, Toulon, France, April 24-26,
2017, Conference Track Proceedings, 2017.
[23] P. Velickovic, G. Cucurull, A. Casanova, A. Romero, P. Li `o, and
Y . Bengio, “Graph attention networks,” in 6th International Conference
on Learning Representations, ICLR 2018, Vancouver,BC, Canada, April
30 - May 3, 2018, Conference Track Proceedings, 2018.
[24] K. Xu, W. Hu, J. Leskovec, and S. Jegelka, “How powerful are
graph neural networks?” in 7th International Conference on Learning
Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019,
2019.
[25] Binance, “Binance spot api documentation: Rest api,” https://developers.
binance.com/docs/binance-spot-api-docs/rest-api, accessed: 2026-02-01.
[26] CoinGecko, “Coingecko api documentation,” https://docs.coingecko.com/
reference/introduction, accessed: 2026-02-01.
[27] D. Pasadakis, M. Bollh ¨ofer, and O. Schenk, “Sparse quadratic approxi-
mation for graph learning,” IEEE Transactions on Pattern Analysis and
Machine Intelligence, vol. 45, no. 9, pp. 11 256–11 269, 2023.
[28] C. Shang, J. Chen, and J. Bi, “Discrete graph structure learning for
forecasting multiple time series,” in International Conference on Learning
Representations (ICLR), 2021.
[29] M. Tumminello, T. Aste, T. Di Matteo, and R. N. Mantegna, “Correlation,
hierarchies, and networks in financial markets,” Journal of Economic
Behavior & Organization, vol. 75, no. 1, pp. 40–58, 2010.
[30] D. Matsunaga, T. Suzumura, and T. Takahashi, “Exploring graph neural
networks for stock market predictions with rolling window analysis,”
CoRR, vol. abs/1909.10660, 2019.
[31] Z. Wu, S. Pan, G. Long, J. Jiang, and C. Zhang, “Graph wavenet
for deep spatial-temporal graph modeling,” in Proceedings of the 28th
International Joint Conference on Artificial Intelligence, ser. IJCAI’19.
AAAI Press, 2019, p. 1907–1913.
[32] Y . Shi, Z. Huang, S. Feng, H. Zhong, W. Wang, and Y . Sun, “Masked
label prediction: Unified message passing model for semi-supervised clas-
sification,” in Proceedings of the Thirtieth International Joint Conference
on Artificial Intelligence, IJCAI-21, Z.-H. Zhou, Ed. International Joint
Conferences on Artificial Intelligence Organization, 8 2021, pp. 1548–
1554, main Track.
[33] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in
Neural Information Processing Systems, vol. 30, 2017.
[34] M. La Morgia, A. Mei, F. Sassi, and J. Stefa, “Pump and dumps in the
bitcoin era: Real time detection of cryptocurrency market manipulations,”
in 2020 29th International Conference on Computer Communications
and Networks (ICCCN), 2020, pp. 1–9.
[35] M. L´opez de Prado, Advances in Financial Machine Learning. Hoboken,
NJ: John Wiley & Sons, 2018.
[36] T. Saito and M. Rehmsmeier, “The precision-recall plot is more
informative than the roc plot when evaluating binary classifiers on
imbalanced datasets,” PloS one, vol. 10, no. 3, p. e0118432, 2015.
8

VI. APPENDIX
A. Features
Feature Type Definition
OHLCV raw Open/high/low/close and volume.
quote asset volume raw V olume in quote currency.
num trades raw Trades per hour.
taker buy base raw Hourly taker-buy volume (base).
taker buy quote raw Hourly taker-buy volume (quote).
std rush order eng Pct. change 12h roll std (buy pressure).
avg rush order eng Pct. change 12h roll mean (buy pres-
sure).
std trades eng Pct. change 12h roll std (num trades).
std volume eng Pct. change 12h roll std (volume).
std price eng Pct. change 12h roll std (close).
avg volume eng Pct. change 12h roll mean (volume).
avg price eng Pct. change 12h roll mean (close).
avg price max eng Pct. change 12h roll mean (high).
hour of the day time UTC hour of the day.
TABLE I.Feature set used in the numerical experiment. Each token
corresponds to a graph node i∈V , and the features listed here constitute the
node feature vector xi,t ∈R F at each hourly timestamp. Raw features are
obtained directly from the market data downloader, engineered features (eng)
are constructed during the feature engineering stage, and temporal features
(time) are derived from the UTC timestamp of each observation.
B. Hyperparameter selection for graph inference
To isolate the effect of the graph inference strategy, the
ST-GNN architecture was kept fixed across all experiments,
and only the graph-inference hyperparameters and the dropout
probability were tuned. For all methods, the learning rate
was fixed to 10−3. For the correlation-based graphs (G1) and
(G2), the scalar series si,t used to construct the graph was
chosen from a single raw feature, namely num_trades or
volume. The final selected configurations are reported in
Table II. The ST-GNN with (G1) and (G2) contains 135,041
learnable parameters, whereas (G3) contains 143,105 due to
the additional learnable node embedding matrices E1 and E2.
Parameter counts are also summarized in Table III.
C. Temporal-only baselines
To further assess the contribution of the inferred graph
structure, we also evaluated two temporal-only baselines,
namely a GRU and a TransformerEncoder, which process
token histories independently and therefore cannot model cross-
token coordination. Among them, the GRU was the strongest
temporal-only baseline, achieving a maximum F1-score of 0.56
and a PR-AUC of 0.51. This remains below the best graph-
based model, for which the self-adaptive graph (G3) reaches
a PR-AUC of0.58.
Importantly, increasing the GRU capacity from approxi-
mately 16k to 164k trainable parameters did not close the gap,
indicating that the improvement of the proposed approach does
not arise merely from higher model capacity, but from the
use of an inferred relational structure that enables cross-token
information exchange.
Signal Search Space Selected
(G1) Static
si,t =num_tradesdropout∈ {0.2,0.3,0.4}
ρ∈ {0.95,0.90,0.75}
dropout= 0.3
ρ= 0.90
si,t =volumedropout∈ {0.2,0.3,0.4}
ρ∈ {0.95,0.90,0.75}
dropout= 0.2
ρ= 0.75
(G2) Dynamic
si,t =num_tradesdropout∈ {0.2,0.3,0.4}
L∈ {12,24}
ρ∈ {0.95,0.90,0.75}
dropout= 0.3
L= 12
ρ= 0.95
si,t =volumedropout∈ {0.2,0.3,0.4}
L∈ {12,24}
ρ∈ {0.95,0.90,0.75}
dropout= 0.2
L= 12
ρ= 0.95
(G3) Self-Adaptive
dropout∈ {0.2,0.3,0.4}
d∈ {16,32,48,64}
ϵ∈ {0.005,0.001,0.02}
dropout= 0.4
d= 48
ϵ= 0.005
TABLE II.Grid search spaces and final selected hyperparameters for the
three graph inference strategies. For (G1) and (G2), the scalar series si,t
used to construct the correlation-based graphs is reported.
D. Computational footprint and training time
Table III reports the approximate model size and training
time of the main baselines and the proposed graph-based
variants. Overall, (G1) Static provides the best trade-off
between performance and computational cost. Although (G3)
Self-Adaptive is the most expensive among the proposed
graph-based models, it remains practically deployable and
is comparable to stronger non-neural baselines in wall-clock
time. All experiments were executed on a single NVIDIA RTX
A6000 GPU, with each model trained in isolation (full GPU
availability).
Model Approx. Num.
Parameters
Approx.
Training Time
GRU (small)∼16k∼3min
GRU (large)∼164k∼4min
TransformerEncoder∼64k∼12min
(G1) Static∼135k∼15min
(G2) Dynamic∼135k∼31min
(G3) Self-Adaptive∼143k∼58min
XGBoost∼15k∼60min
Random Forest∼500k∼60min
TABLE III.Approximate model size and training time of the temporal-only
baselines, graph-based variants, and classical baselines. Times are wall-clock
approximations under the same experimental setup. For classical machine
learning baselines, we report approximate model size rather than neural
trainable parameters.
9
