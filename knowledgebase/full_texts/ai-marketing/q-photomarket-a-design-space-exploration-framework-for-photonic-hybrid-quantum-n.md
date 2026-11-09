---
title: 'Q-PhotoMarket: A Design Space Exploration Framework for Photonic Hybrid Quantum Neural Networks
  in Financial Market Prediction'
url: https://arxiv.org/abs/2610.09641
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Alberto Marchisio
- Hanzalah Mohamed Siraj
- Muhammad Kashif
- Nouhaila Innan
- Muhammad Shafique
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.09641
pages: 8
chars: 43287
fetched_at: '2026-11-08T13:24:55+00:00'
kb_version: 1
---

# Q-PhotoMarket: A Design Space Exploration Framework for Photonic Hybrid Quantum Neural Networks in Financial Market Prediction

To appear at the IEEE International Conference on Quantum Artificial Intelligence (QAI), Nottingham, UK, December 2026.
Q-PhotoMarket: A Design Space Exploration
Framework for Photonic Hybrid Quantum Neural
Networks in Financial Market Prediction
Alberto Marchisio §†‡∗ , Hanzalah Mohamed Siraj §†, Muhammad Kashif §†, Nouhaila Innan §†, Muhammad Shafique §†
§ eBrain Lab, Division of Engineering, New York University Abu Dhabi, PO Box 129188, Abu Dhabi, UAE
† Center for Quantum and Topological Systems, NYUAD Research Institute, New York University Abu Dhabi, UAE
‡ SDU Microelectronics, Institute of Mechanical and Electrical Engineering, University of Southern Denmark, Odense, Denmark
Emails: chisio@sdu.dk,{sm12152, muhammadkashif, nouhaila.innan, muhammad.shafique}@nyu.edu
Abstract—Photonic quantum computing has recently emerged
as a promising platform for hybrid quantum machine learning
due to its native realization of linear-optical circuits and the
computational complexity of boson sampling. However, despite
growing interest in quantum methods for finance, the influence
of photonic circuit design choices on predictive performance
remains largely unexplored. Existing studies typically evaluate
a single architecture, leaving the broader photonic design
space unexamined. In this work, we present Q-PhotoMarket,
a systematic design space exploration (DSE) framework for
photonic hybrid quantum neural networks (HQNNs) applied
to financial market prediction. We explore over 5,000 valid
photonic configurations spanning input photon states, circuit
architectures, entangling models, and measurement strategies
across their compatible computation spaces, for U.S., Indian,
and cryptocurrency markets. To improve search efficiency,
the exhaustive exploration is complemented with Bayesian
optimization. We further incorporate threshold calibration and
prediction-collapse diagnostics to enable reliable evaluation under
increasingly imbalanced return thresholds. Experimental results
show that systematic exploration of more than 5,000 photonic
HQNN configurations reveals consistent architectural patterns
across financial markets, identifies robust high-performing designs,
and demonstrates competitive performance relative to classical
machine learning baselines.
Index Terms—Quantum Machine Learning, Photonic Quantum
Computing, Design Space Exploration, Financial Market
Prediction
I. INTRODUCTION
Quantum Machine Learning (QML) has emerged as a
promising direction for extending machine learning with quantum
computational primitives [1], [2]. Among the various QML
paradigms, Hybrid Quantum Neural Networks (HQNNs) have
attracted considerable attention due to their compatibility with
near-term quantum hardware and their ability to combine quantum
representations with classical optimization [3]. While HQNNs
have demonstrated encouraging results across a growing range of
applications, understanding how quantum architectural choices
influence learning performance remains an important open
problem.
Recent advances in photonic quantum computing have
established linear-optical processors as a promising alternative
to conventional gate-based quantum hardware. Compared with
many qubit-based platforms, photonic systems offer practical
advantages such as room-temperature operation, relatively low
susceptibility to decoherence, and compatibility with existing
optical communication technologies [4], [5]. Coupled with
increasingly mature software ecosystems, these advances have
made photonic HQNNs more accessible for developing and
evaluating practical quantum machine learning models [6],
∗This work has been carried out while at NYUAD.
S&P 500 NIFTY 50 Crypto
0.44
0.46
0.48
0.50
0.52
0.54
0.56
0.58
0.60AUC
Mean AUC
Best AUC
Random-ranking reference
Fig. 1: Distribution of AUC across valid photonic HQNN configurations for
the S&P 500, NIFTY 50, and cryptocurrency markets.
[7]. Unlike gate-based implementations, however, photonic
HQNNs expose a rich architectural design space involving
multiple interacting design decisions [8], [9]. Despite this
flexibility, existing studies typically adopt a single manually
designed architecture, leaving the impact of these design choices
largely unexplored. This gap is particularly important given the
demonstrated sensitivity of HQNN performance to circuit design
in gate-based models [10] and the computational potential of
linear-optical circuits based on boson sampling [11].
To illustrate the practical importance of this design problem,
Figure 1 shows the distribution of AUC across the explored
photonic HQNN configurations for the three considered markets.
Although the median performance remains close to the random-
ranking reference, the observed distributions are broad, and the
best configurations achieve notably higher AUC. This spread
indicates that predictive performance is highly sensitive to
photonic design choices and that manually selecting a single
architecture may lead to misleading conclusions about the
capability of a photonic HQNN.
Financial market prediction provides a realistic and challenging
benchmark for studying this problem. The task is characterized
by weak predictive signals, non-stationary dynamics, and severe
class imbalance, while state-of-the-art classical approaches
generally achieve only modest improvements under rigorous
walk-forward evaluation [12]. Existing QML studies for finance
typically employ fixed quantum circuit architectures with limited
architectural analysis [13], [14], making it difficult to understand
how photonic design choices influence predictive performance.
To address this gap, we proposeQ-PhotoMarket, a systematic
design space exploration (DSE) framework for photonic HQNNs.
Q-PhotoMarket explores multiple photonic design dimensions,
including input photon states, circuit architectures, entangling
models, measurement strategies, and computation spaces, while
combining exhaustive exploration with Bayesian optimization to
arXiv:2610.09641v1  [quant-ph]  7 Oct 2026

efficiently identify promising regions of the design space.
The main contributions of this work are:
• We proposeQ-PhotoMarket, a systematic DSE framework
for photonic HQNNs, enabling the analysis of key photonic
design dimensions for real-world QML applications.
• We perform a large-scale empirical evaluation of the photonic
design space by exploring thousands of valid HQNN
configurations across multiple financial markets and return
prediction thresholds.
• We integrate exhaustive exploration with Bayesian optimization
to efficiently identify promising photonic architectures while
reducing the search cost of high-dimensional design spaces.
• We provide empirical insights into the impact of photonic
architectural choices on HQNN performance and establish a
reproducible benchmark to support future research in photonic
QML.
II. BACKGROUND ANDRELATEDWORK
A. Photonic HQNNs
HQNNs integrate parameterized quantum circuits with classical
neural networks, combining quantum feature transformations
with classical optimization. In photonic HQNNs, information is
encoded into bosonic modes and processed through trainable
linear-optical circuits composed of beam splitters, phase shifters,
and interferometers. Universal interferometer decompositions,
such as the Reck and Clements architectures, enable the
realization of arbitrary unitary transformations and constitute
the foundation of many photonic quantum learning models [15].
Recent software frameworks, including Perceval and Merlin, have
further facilitated the development of photonic QML models by
providing differentiable simulation environments for training and
evaluation [6], [7].
B. Design Space Exploration in HQNNs
The predictive performance of HQNNs is strongly influenced
by architectural design choices, including data encoding,
circuit topology, variational ans ¨atze, measurement strategies,
and optimization protocols. Consequently, recent studies have
explored systematic design space exploration (DSE) for gate-
based HQNNs to identify architectures that balance expressivity,
trainability, and hardware efficiency [10], [16], [17]. In contrast,
comparable studies for photonic HQNNs remain scarce, despite
the considerably richer design space introduced by photon-state
preparation, linear-optical circuit topologies, and measurement
schemes [8]. Existing photonic QML studies typically evaluate
a single manually designed architecture, providing limited
understanding of how individual design choices influence learning
performance. This gap motivates the systematic photonic DSE
framework proposed in this work.
III. Q-PHOTOMARKETFRAMEWORK
Q-PhotoMarket systematically explores the design space of
photonic hybrid quantum neural networks (HQNNs) for financial
market prediction across three asset classes: U.S. equities
(S&P 500), Indian equities (NIFTY 50), and cryptocurrencies.
The design space comprises four independent dimensions: input
photon state, photonic circuit architecture, entangling model, and
measurement strategy. The corresponding computation space is
determined by the selected measurement strategy. As illustrated
in Figure 2, the framework consists of four main stages: (i)
leakage-safe dataset construction, (ii) photonic HQNN design
space exploration, (iii) unified experimental evaluation, and (iv)
Bayesian optimization for refining promising configurations.
A. Problem Formulation
We formulate financial market prediction as a binary
classification task that predicts the direction of the next-day
asset return. Let rt→t+h denote the forward return of an asset
over prediction horizon h from time t. The binary label is defined
as
yt =1(r t→t+h > τ),(1)
where 1(·) is the indicator function and τ is a user-defined
return threshold. Setting τ= 0 corresponds to conventional
up/down direction prediction, whereas larger thresholds ( τ∈
{0.5%,1.0%} ) require economically more significant price
movements, resulting in progressively imbalanced classification
tasks. Throughout this work, we evaluate three thresholds,
τ∈ {0,0.5%,1.0%}, with a one-day prediction horizon ( h= 1).
To ensure realistic evaluation on non-stationary financial
time series, all experiments employ an expanding-window walk-
forward protocol where each validation window strictly follows
its corresponding training window to prevent look-ahead bias.
B. Dataset Construction
1) Data Acquisition and Feature Engineering
Daily OHLCV (Open, High, Low, Close, V olume) data for
each asset class are collected from Yahoo Finance for the period
2018-2025. For each asset, we construct a leakage-safe feature
set using only information available at time t. The resulting
dataset comprises 23 engineered features covering return and
momentum, volatility and risk, technical indicators, liquidity and
microstructure, and price structure:
• Return and momentum: ret_1, ret_5, ret_10, ret_20,
cross_momentum
• Volatility and risk: vol_5, vol_10, vol_20,
vol_ratio_5_20,ret_autocorr_20
• Technical indicators: rsi_14, sma20_dist,
bb_width_20,vwap_deviation
• Liquidity and microstructure: volume_ratio_20,
amihud_illiquidity,obv_slope_10
• Price structure and event: high_low_ratio,
overnight_gap, day_of_week, vix_bucket,
month_end_flag,earnings_event_flag
Macro-contextual features are incorporated through a 5-day
rolling index return ( index_ret_5d), a discretized VIX
volatility regime proxy ( vix_bucket), and a binary earnings-
event indicator ( earnings_event_flag). Samples with
missing values are removed before label construction.
To satisfy the photonic mode constraints imposed by the Merlin
simulation framework, the HQNN operates on a fixed subset of 16
input features throughout all experiments. The selected features
correspond exclusively to price-derived market descriptors,
including return, momentum, volatility, technical, liquidity, and
price-structure indicators, while external contextual signals (e.g.,
market-index and event-related features) are excluded.
2) Label Construction
Future return labels are generated only after feature engineering
to eliminate look-ahead leakage. For each threshold τ, labels are
computed independently using the forward return rt→t+h =
Pt+h/Pt −1 . As τ increases, the positive class prevalence
decreases from approximately 50% (τ= 0) to 20–34% (τ= 1%),
inducing increasing label imbalance across all three markets.
3) Walk-Forward Cross-Validation
To respect the temporal ordering of financial data and prevent
look-ahead bias, we construct time-consistent evaluation folds

HQNN Model Training
Experimental Protocol
Threshold Calibration for
Class Imbalance Handling
Prediction Collapse
Diagnostic
Bayesian
Optimization
Stage 1: TPE-
Guided Search
Stage 2: Local
Refinement and
Warm-Starting
Primary Metrics:
AUC, MCC, F1, Acc, AP
Performance Evaluation
Composite Metrics:
GPS1-4
Finance-Specific
Metrics
Best-Performing Photonic HQNN
Designs
Output: Results and Analysis
Cross-Market
Generalization
Design
Recommendations
S&P 500
US equities
NIFTY 50
Indian equities
Crypto assets
Digital assets
Data Acquisition and
Feature Pre-Processing
Dataset Construction
Label Construction
Walk-Forward
Cross-Validation
Cross-Market Analysis
t-SNE
❑ Input Photon State
(4 options)
❑ Photonic Circuit
Architecture (5 options)
❑ Entangling Model
(2 options)
❑ Measurement Strategy
(5 options)
Photonic HQNN Design Space
Fig. 2: Overview of the proposed Q-PhotoMarket framework.
75
 50
 25
 0 25 50 75
t-SNE 1
75
50
25
0
25
50
75
t-SNE 2
S&P 500
NIFTY 50
Crypto
Fig. 3: Two-dimensional t-SNE visualization of the engineered feature spaces
for the S&P 500, NIFTY 50, and cryptocurrency datasets.
using an expanding-window walk-forward scheme. Training
windows grow monotonically, while each validation window
is strictly subsequent to its corresponding training window
(nfolds = 5, minimum training fraction = 0.5). This protocol
provides reproducible evaluation across all dataset-threshold
combinations.
4) Dataset and Cross-Market Feature-Space Analysis
The proposed framework is evaluated on three market domains:
U.S. equities, Indian equities, and cryptocurrencies. Daily
OHLCV data from 2018-2025 are transformed into a common
leakage-safe feature representation and subsequently analyzed
across markets. Since these datasets exhibit different volatility
characteristics, trend persistence, and class distributions, we
assess the similarity of their engineered feature spaces before
performing cross-market architectural comparisons.
To this end, we employ t-distributed Stochastic Neighbor
Embedding (t-SNE) [18] as a qualitative visualization technique.
Feature vectors are first normalized to[0,1], pre-reduced using
PCA for embedding stability, and projected into two dimensions
using a perplexity of min(30, N/4), 500 optimization iterations,
and a fixed random seed.
As shown in Figure 3, the three markets occupy overlapping
yet distinguishable regions in feature space. This qualitative
analysis suggests that the datasets share sufficient statistical
structure to support meaningful cross-market comparisons while
preserving market-specific characteristics, allowing architectural
differences to be interpreted with reduced influence from dataset-
level distributional effects.
TABLE I: Photonic HQNN design space explored by Q-PhotoMarket.
Computation space is determined by the selected measurement strategy. Total
valid configurations per (market, τ) are approximately 600 after invalid-
combination pruning.
Dimension Options Count
Input photon state Alternating, Bunched, Pair-bunched, Thermal-like 4
Circuit architecture Simple, Ring NN, Clements Mesh, Phase-only, 5
Permuted Ring
Entangling model MZI, Bell 2
Measurement strategy Probs-Fock, Probs-Unbunched, Probs-Dual-Rail, 5
Mode expectations, Mode correlations
Valid configs per (market,τ), after pruning≈600
Total runs (×3 markets,×3 thresholds)≈5,400
C. Photonic HQNN Architecture and Design Space
The proposed HQNN is implemented using the Merlin
photonic simulation framework and trained end-to-end in PyTorch.
Since Merlin provides a differentiable simulation backend,
gradients are computed through standard backpropagation without
requiring parameter-shift evaluation. The hybrid architecture
couples a trainable photonic QuantumLayer with a classical
MLP prediction head ( LazyLinear→ReLU→Linear(1)),
which maps measurement-derived photonic features to the final
prediction logit. Throughout the design space exploration, the
number of photonic modes is fixed as nmodes =n features + 1,
with nfeatures = 16. Q-PhotoMarket explores four configurable
dimensions of the photonic HQNN architecture: input photon
state, circuit architecture, entangling model, and measurement
strategy. The resulting design space is summarized in Table I.
1) Input Photon State
The input state determines the initial photon occupation used
to encode classical features into the photonic Hilbert space. We
consider four configurations:
•Alternating: photons distributed across alternating modes.
•Bunched: photons initialized in adjacent low-index modes.
•Pair-bunched: photons injected in paired modes.
• Thermal-like: photon occupations sampled from a thermal
distribution.
2) Photonic Circuit Architecture
Five linear-optical circuit topologies are investigated:
•Simple: single-layer beamsplitter mesh.
•Ring NN: circular beamsplitter topology.
• Clements Mesh: universal rectangular interferometer [15],
providing maximal expressivity.
• Phase-only: phase-shifter network without beamsplitter
entanglement.
• Permuted Ring: ring topology with randomized mode
permutations.
3) Entangling Model
Two entangling primitives are evaluated:

•MZI: Mach-Zehnder Interferometer, the canonical two-mode
entangling unit.
• Bell: Bell-state-inspired entangling structure, generating
stronger inter-mode correlations.
4) Measurement Strategy
Five measurement strategies are explored to extract classical
representations from the output photonic state. Invalid
combinations (e.g., non-binary input states paired with
probs_unbunched or probs_dual_rail) are discarded
during the search. The associated computation space is
determined by the selected measurement strategy.
• Fock probabilities( probs_fock): output occupation
probabilities in the Fock basis; restricted to nmodes ≤4
because of memory requirements.
• Unbunched probabilities( probs_unbunched):
distinguishable-photon probabilities in the unbunched
computation space.
• Dual-rail probabilities( probs_dual_rail): probabilities
obtained under dual-rail logical encoding.
• Mode expectations( mode_expectations): first-order
expectations⟨ˆni⟩.
• Mode correlations( mode_correlations): second-order
correlations⟨ˆni ˆnj⟩.
D. Experimental Protocol
1) HQNN Model Training
All HQNN configurations are trained under a unified protocol.
We employ the Adam optimizer with learning rate η= 3×10 −4
and binary cross-entropy loss ( BCEWithLogitsLoss). Each
model is trained for 8 epochs during Stage 1 and for 20 epochs
during Stage 2, using a batch size of 128 and 100 measurement
shots per circuit execution with a random seed fixed to 42. An
optional cosine annealing scheduler and early stopping based on
validation AUC (patience = 5 epochs) are supported. Gradients
are propagated through Merlin’s differentiable simulation backend
using automatic differentiation [7].
2) Class Imbalance Handling and Threshold Calibration
Increasing the return threshold τ substantially reduces the
positive-class prevalence, producing increasingly imbalanced
classification tasks. For τ >0 , class imbalance is mitigated
through inverse-frequency class weighting,
w+ = N− max(N+,1) ,(2)
where N+ and N− denote the numbers of positive
and negative training samples, respectively. Empirically,
S&P 500 and NIFTY 50 achieve the best performance using
class-weighting=balanced, whereas cryptocurrency
datasets benefit fromclass-weighting=none.
To avoid suboptimal fixed decision boundaries, the
classification threshold is calibrated on the validation fold by
maximizing a selected objective using Eq. 3, where Obj∈
{MCC,F1,BalAcc}.
ˆτ∗ = arg max
τ∈[0,1]
Obj(yval,1(ˆpval ≥τ)),(3)
3) Prediction Collapse Diagnostics
A common failure mode was identified at τ >0 , where
positive class prevalence drops to 20-34% and predicted
probabilities remain below the conventional decision threshold
of 0.5, causing all samples to be assigned to the majority class 0.
Although ranking performance (AUC) may remain meaningful,
0.35 0.40 0.45 0.50
Calibrated threshold
0.00
0.25
0.50
0.75
1.00
Positive
 prediction rate
Collapse diagnostics
0.0% 0.5% 1.0%
0.0
0.1
0.2
0.3Collapse fraction
Collapse by threshold
Fig. 4: Prediction-collapse diagnostics. Left: calibrated decision thresholds
versus positive prediction rate (PPR). Right: fraction of configurations
exhibiting prediction collapse under different return thresholds.
threshold-dependent metrics such as F1-score and MCC collapse
to zero,
F1= 0,MCC= 0,BalAcc= 0.5,(4)
To identify this behavior, each experiment records the
calibrated decision threshold, its optimization objective, the
positive prediction rate (PPR), and a prediction-collapse warning
whenPPR/∈[0.02,0.98].
Figure 4 illustrates the effectiveness of this diagnostic
procedure. The left panel shows that calibrated thresholds
successfully recover meaningful positive prediction rates across
a wide range of operating points, while the right panel quantifies
how the frequency of prediction collapse increases as the return
threshold becomes more stringent. These diagnostics provide an
additional validation of the proposed calibration strategy before
comparing HQNN architectures.
E. Bayesian Optimization
To complement the exhaustive grid search, we employ
Bayesian optimization (BO) using the Tree-structured Parzen
Estimator (TPE) sampler implemented in Optuna [19]. BO
explores the same photonic design space while efficiently
concentrating the search on promising regions identified during
earlier trials.
1) Stage 1: TPE-Guided Search
The TPE sampler models the distribution of high-performing
configurations and proposes new candidates by jointly optimizing
the photonic design parameters, the number of input features,
and the circuit shot count. Candidate configurations are ranked
using the composite objective
L=w AUC ·AUC+w F1 ·F1+w GPS ·GPS−δ collapse,(5)
where wAUC = 0.6, wF1 = 0.3, wGPS = 0.1, and δcollapse =
0.15 is a penalty applied when PPR/∈[0.05,0.95] . A resource
guardrail skips configurations whose heuristic cost index, defined
as (n3 modes ×m factor ×a factor ×shots/100) , exceeds a threshold,
preventing memory or runtime instability for high-mode, high-
shot combinations. A median pruner with twarmup = 5 epochs
additionally terminates unpromising trials early.
2) Stage 2: Local Refinement and Warm-Starting
After Stage 1, the top- k discovered configurations are used
to seed a local dense refinement pass. In subsequent studies,
prior sweep results are enqueued directly into the optimization
process, allowing the sampler to incorporate all prior grid and
confirm-run evidence before proposing new trials. Warm-start
rows are ranked by AUC and filtered to respect mode and shot
constraints.
3) Optimization Protocol
The BO phase is performed independently for each market with
separate Optuna studies, using ntrials = 150per shard, nstartup =

30 random trials before activating the TPE sampler, and a per-
trial subprocess timeout of 300 seconds. The resulting studies are
merged for downstream analysis, enabling parameter-importance
estimation and convergence analysis across the explored photonic
design space.
F . Performance Evaluation
1) Primary Metrics
Increasing return thresholds produce progressively imbalanced
classification tasks, making raw accuracy alone insufficient for
performance evaluation. Accordingly, we emphasize threshold-
robust metrics including the Area Under the ROC Curve (AUC),
Matthews Correlation Coefficient (MCC), and balanced accuracy,
while reporting conventional accuracy only as a complementary
measure. All configurations are evaluated using accuracy, F1-
score, MCC, Area Under the ROC Curve (AUC), and Average
Precision (AP). MCC is defined as:
MCC= T P·T N−F P·F Np
(T P+F P)(T P+F N)(T N+F P)(T N+F N)
,(6)
and is particularly suitable for imbalanced financial
classification because it accounts for all elements of the confusion
matrix. Balanced accuracy is defined as(T P R+T N R)/2.
2) Composite Metrics
Following [20], we report four General Performance Score
(GPS) variants, each defined as the harmonic mean of a
complementary subset of metrics:
GPS1 = 3 1
BalAcc + 1 AUC + 1 F1 (7)
GPS2 = 4 1
Acc + 1 Prec + 1 Recall + 1 F1 (8)
GPS3 = 3 1
BalAcc + 1 AUC + 1 AccCV
(9)
GPS4 = 4 1
BalAcc + 1 AUC + 1 F1 + 1 AccCV
(10)
where AccCV denotes the mean walk-forward cross-validation
accuracy. These composite metrics provide a unified ranking
while emphasizing different performance trade-offs.
3) Finance-Specific Metrics
To complement conventional classification metrics, we report
two finance-oriented measures.Pseudo-Sharpeapproximates the
risk-adjusted return of a strategy that enters a long position
whenever ˆyt = 1, computed as the ratio between the mean
predicted-positive return and its standard deviation.Magnitude-
weighted accuracyweights each correct prediction by |rt→t+h|,
assigning greater importance to larger market movements.
4) Baselines and Diagnostic Outputs
For each dataset-threshold combination, we compare the
proposed photonic HQNNs against three classical baselines:
a majority-class classifier, logistic regression, and a shallow
multilayer perceptron. These baselines provide reference points
for assessing whether photonic quantum models offer meaningful
improvements over classical machine learning approaches [10].
Each experiment records calibrated decision thresholds,
positive prediction rates, prediction probabilities, and collapse
diagnostics. Bayesian optimization studies additionally store the
composite objective value, parameter importance estimates, and
convergence history for subsequent analysis.
m_corrm_exp p_fock
cmesh
pring
phase
ring
simple
0.560 0.558 0.565
0.498 0.510 0.512
0.500 0.500 0.500
0.520 0.521 0.534
0.545 0.534 0.565
S&P 500
m_corrm_exp p_fock
0.535 0.531 0.546
0.502 0.498 0.503
0.500 0.500 0.500
0.518 0.508 0.522
0.523 0.519 0.546
NIFTY 50
m_corrm_exp p_fock
0.523 0.513 0.536
0.515 0.501 0.500
0.500 0.500 0.501
0.518 0.497 0.510
0.514 0.504 0.525
Crypto
0.50
0.51
0.52
0.53
Fig. 5: Mean AUC obtained across the explored photonic HQNN design space
for different combinations of circuit architectures and measurement strategies
atτ= 1%.
IV. RESULTS ANDDISCUSSION
A. Overall Design Space Exploration
We first evaluate the complete photonic design space using the
exhaustive screening protocol comprising approximately 1,080
configurations per market. For each market, approximately 600
candidate architectures are subsequently re-evaluated using multi-
fold validation to confirm robustness. Throughout this section,
we emphasize AUC, MCC, and balanced accuracy because
increasing return thresholds introduce progressively stronger class
imbalance.
Figure 5 summarizes the mean AUC obtained for different
combinations of photonic circuit architectures and measurement
strategies under the most challenging return threshold ( τ= 1%).
Several consistent trends emerge across all three markets.
Architectures based on theClements MeshandSimple
interferometer generally achieve higher mean AUC than the
Phase-onlyandPermuted Ringvariants, while probability-
based measurements in the Fock basis frequently outperform
expectation- and correlation-based alternatives. Although the
optimal configuration remains market-dependent, these results
demonstrate that architectural decisions have a measurable and
systematic impact on HQNN performance.
B. Influence of Photonic Design Choices
Figures 6-8 illustrate the impact of the explored photonic
design dimensions on HQNN performance across the three
financial markets. The results reveal consistent performance
differences arising from input photon states, circuit architectures,
entangling models, and measurement strategies.
Input photon state.The choice of input photon state has a
relatively modest influence on predictive performance compared
with the remaining architectural dimensions. Across all three
markets, the four investigated input states exhibit similar GPS
and AUC distributions, suggesting that photonic circuit design
and measurement strategy play a more dominant role than the
initial photon occupation.
Circuit architecture.Among the investigated architectures,
theClements Meshconsistently achieves the strongest average
performance across markets, particularly for the S&P 500
and cryptocurrency datasets. Ring-based architectures also
demonstrate competitive behavior, whereas thePhase-only
architecture generally produces the weakest results. These
observations indicate that expressive interferometer topologies
provide a measurable advantage for financial prediction tasks.
Entangling model.The choice of entangling primitive has
a comparatively smaller impact than circuit topology. Across
all three markets, the performance distributions of the Bell-
inspired and Mach-Zehnder Interferometer (MZI) entangling
models overlap substantially, although MZI exhibits a slight
advantage on the NIFTY 50 dataset. Overall, these results suggest
that circuit architecture contributes more strongly to predictive
performance than the specific entangling primitive.

Best for
Clements Mesh
Best for Fock Meas
Fig. 6: S&P 500: 8-panel DSE diagnostics from the screening grid.
Best for
MZI
Higher threshold => higher
specifity, lower sensitivity
Fig. 7: NIFTY 50: 8-panel DSE diagnostics from the screening grid.
Measurement strategy.Measurement strategy emerges as one
of the most influential design dimensions. While probability-
based Fock measurements provide strong performance on the
S&P 500 and NIFTY 50 datasets, correlation-based measurements
become increasingly competitive on the crypto dataset. This
behavior indicates that the optimal measurement representation
is application-dependent and should be treated as an important
hyperparameter during photonic HQNN design.
C. Cross-Market and Threshold Sensitivity
Having established the influence of individual photonic design
dimensions, we next examine whether these trends remain
consistent across financial markets and prediction settings.
Figure 9 shows the mean and best AUC obtained across
all evaluated configurations under increasing return thresholds.
Across the three markets, both the average and best-performing
photonic HQNNs exhibit improved ranking performance as the
return threshold increases. The largest improvement is observed
for the S&P 500, where the mean AUC increases from 0.500
at τ= 0 to 0.528 at τ= 1% , followed by NIFTY 50
(0.499→0.517) and cryptocurrencies (0.500 →0.510). Although
higher thresholds produce increasingly imbalanced datasets, they
also define more discriminative prediction tasks by focusing on
economically significant price movements, enabling improved
class separability.
D. Configuration Selection and Bayesian Refinement
Following the exhaustive screening stage, the highest-
performing configurations were re-evaluated using the staged
multi-fold protocol described in Section III. Figure 10 compares
the fold-wise AUC distributions obtained during Phase 1 and
Phase 2. While the variance across validation folds remains
comparable, the longer Phase 2 training consistently improves
the median AUC, indicating that the shortlisted architectures
maintain their performance under more rigorous evaluation.
The highest-performing configurations obtained after Phase 2
are summarized for each market. For the S&P 500, the best-
performing architecture combines theSimplecircuit with Bell
entangling and Fock probability measurements, achieving a
mean AUC of 0.528 ( ±0.019). For NIFTY 50, the strongest
configuration employs aClements Mesharchitecture with MZI
entangling and Fock measurements, reaching a mean AUC of
0.514 (±0.028).
Tables II-IV summarize representative high-performing
configurations (top-10 per market) identified during the
exhaustive search, revealing recurring architectural patterns across
multiple evaluation metrics. In particular, Clements Mesh, Ring
NN, and Simple architectures appear repeatedly among the
highest-ranked configurations, confirming the trends observed
during the design space exploration.

Best for
C. Mesh
Best
Fig. 8: Crypto: 8-panel DSE diagnostics from the screening grid.
TABLE II: Top-10 overlap table for S&P 500. Top10Count indicates in how many of 8 metrics a configuration appears in the top-10.
RτArch Ent Meas State Top10Count MetricsHit BestAUC BestMCC BestBalAcc
1 0.0100 simple bell probs fock alternating 4/8 AUC, MCC, BalAcc, GPS 0.573 0.000 0.500
2 0.0100 clements mesh mzi mode correlations pair bunched 4/8 MCC, BalAcc, MW A, PSharpe 0.557 0.008 0.501
3 0.0000 simple mzi mode expectations thermal like 4/8 MCC, F1, BalAcc, AP 0.519 0.022 0.500
4 0.0000 simple mzi mode expectations bunched 3/8 MCC, F1, BalAcc 0.483 0.022 0.500
5 0.0000 ring nn mzi mode correlations pair bunched 3/8 MCC, F1, BalAcc 0.479 0.022 0.501
6 0.0100 clements mesh mzi mode expectations alternating 2/8 AUC, GPS0.5760.000 0.500
7 0.0100 ring nn mzi probs fock pair bunched 2/8 AUC, GPS 0.573 0.000 0.500
8 0.0100 simple bell probs fock pair bunched 2/8 AUC, GPS 0.572 0.000 0.500
9 0.0100 clements mesh mzi mode expectations bunched 2/8 AUC, GPS 0.571 0.000 0.500
10 0.0100 clements mesh mzi mode correlations bunched 2/8 AUC, GPS 0.570 0.000 0.500
TABLE III: Top-10 overlap table for NIFTY 50. Top10Count indicates in how many of 8 metrics a configuration appears in the top-10.
RτArch Ent Meas State Top10Count MetricsHit BestAUC BestMCC BestBalAcc
1 0.0000 ring nn bell mode expectations pair bunched 5/8 MCC, BalAcc, AP, GPS, PSharpe 0.511 0.021 0.507
2 0.0000 ring nn mzi mode expectations pair bunched 4/8 MCC, BalAcc, GPS, PSharpe 0.516 0.048 0.522
3 0.0000 ring nn bell mode expectations bunched 4/8 MCC, BalAcc, GPS, PSharpe 0.512 0.027 0.511
4 0.0000 clements mesh bell mode correlations thermal like 3/8 AP, GPS, PSharpe 0.520 0.003 0.500
5 0.0000 clements mesh bell mode correlations pair bunched 3/8 AP, GPS, PSharpe 0.516 0.002 0.500
6 0.0000 ring nn mzi probs fock pair bunched 3/8 F1, AP, GPS 0.514 0.000 0.500
7 0.0000 ring nn mzi mode correlations bunched 3/8 MCC, BalAcc, AP 0.512 0.051 0.511
8 0.0000 permuted ring bell mode correlations bunched 3/8 MCC, F1, PSharpe 0.500 0.024 0.501
9 0.0000 permuted ring bell mode expectations alternating 2/8 F1, GPS0.5210.000 0.500
10 0.0000 ring nn bell probs fock pair bunched 2/8 AP, GPS 0.514 0.000 0.500
0.0% 0.5% 1.0%
Return threshold ( )
0.50
0.51
0.52
0.53
0.54
0.55
0.56
0.57Test AUC
S&P 500 mean
S&P 500 best
NIFTY 50 mean
NIFTY 50 best
Crypto mean
Crypto best
Fig. 9: Threshold robustness of the explored photonic HQNN design space.
Mean and best AUC are reported across all evaluated configurations, across
τ∈ {0,0.5%,1%}.
E. Comparison with Classical Baselines
Figure 11 compares the best photonic HQNN identified by
Q-PhotoMarket against three classical baselines: a majority-
class classifier, logistic regression, and a shallow multilayer
perceptron. Across the evaluated markets and return thresholds,
0.48
0.50
0.52
0.54
0.56Fold-wise test AUC
Phase 1 (top-100, 8 epochs) Phase 2 (top-20, 20 epochs)
Fig. 10: Fold-variance analysis for shortlisted configurations (Phases 1 vs 2).
the photonic HQNN consistently outperforms the majority
baseline and achieves competitive performance relative to
conventional machine learning models.
The performance gap becomes more apparent at higher return
thresholds, where class imbalance increases and simple classifiers
struggle to identify minority positive samples. Although the
improvements over classical neural networks remain modest,
these results demonstrate that systematic photonic architecture
exploration enables HQNNs to remain competitive on realistic
financial prediction tasks while providing valuable insights into
photonic circuit design.

TABLE IV: Top-10 overlap table for Crypto. Top10Count indicates in how many of 8 metrics a configuration appears in the top-10.
RτArch Ent Meas State Top10Count MetricsHit BestAUC BestMCC BestBalAcc
1 0.0000 clements mesh mzi mode expectations bunched 3/8 MCC, BalAcc, AP 0.536 0.020 0.501
2 0.0000 clements mesh mzi mode expectations alternating 3/8 MCC, BalAcc, AP 0.536 0.031 0.503
3 0.0000 permuted ring bell mode expectations thermal like 3/8 MCC, F1, BalAcc 0.505 0.035 0.503
4 0.0050 clements mesh bell mode correlations thermal like 3/8 MCC, BalAcc, PSharpe 0.505 0.063 0.514
5 0.0050 clements mesh mzi mode correlations thermal like 3/8 MCC, BalAcc, PSharpe 0.503 0.042 0.509
6 0.0000 ring nn bell mode correlations pair bunched 3/8 MCC, F1, BalAcc 0.500 0.031 0.503
7 0.0050 clements mesh bell mode correlations pair bunched 3/8 MCC, BalAcc, PSharpe 0.493 0.063 0.505
8 0.0100 ring nn mzi mode correlations thermal like 2/8 AUC, GPS0.5520.000 0.500
9 0.0100 clements mesh bell probs fock pair bunched 2/8 AUC, GPS 0.550 0.000 0.500
10 0.0100 ring nn mzi probs fock pair bunched 2/8 AUC, GPS 0.546 0.000 0.500
0.0% 0.5% 1.0%
0.0
0.2
0.4
0.6
0.8Accuracy
S&P 500
0.0% 0.5% 1.0%
NIFTY 50
0.0% 0.5% 1.0%
Crypto
HQNN best Majority Logistic MLP
Fig. 11: Accuracy comparison against majority, logistic, and MLP baselines.
F . Discussion
The primary contribution of this work is not the identification
of a single best-performing photonic HQNN, but the systematic
characterization of the photonic design space. Across more
than 5,000 evaluated configurations, the results consistently
demonstrate the influence of architectural decisions on predictive
performance. In particular, circuit topology and measurement
strategy contribute substantially larger performance variations
than input photon states or entangling primitives, suggesting
that future photonic HQNN development should prioritize
architectural exploration over isolated circuit optimization.
Among the investigated architectures, the Clements Mesh
and, in several cases, the Simple and Ring NN topologies
repeatedly appear among the highest-performing configurations.
Their recurring presence across multiple evaluation metrics
and financial markets indicates that expressive interferometer
structures provide a favorable balance between representational
capacity and trainability. Likewise, the influence of the
measurement strategy highlights that the classical representation
extracted from the photonic circuit is an integral component of
the learning pipeline.
An interesting observation is that increasing the return
threshold generally improves AUC despite introducing more
severe class imbalance. By filtering out small price fluctuations,
larger thresholds produce prediction tasks with clearer decision
boundaries, enabling photonic HQNNs to better separate positive
and negative samples. At the same time, this setting increases
the risk of prediction collapse, emphasizing the importance of
calibration-aware evaluation and imbalance-sensitive metrics.
This work has several limitations. All experiments are
performed using differentiable photonic simulation, and the study
focuses on daily market prediction using three representative
financial datasets. In addition, the explored design space is limited
to the investigated circuit topologies, measurement strategies,
and encoding schemes. Future work will extend Q-PhotoMarket
to larger photonic architectures, hardware-aware optimization,
execution on real quantum devices, and additional real-world
QML applications, while investigating automated architecture
search techniques that further reduce the cost of exploring high-
dimensional photonic design spaces.
V. CONCLUSION
This work presents Q-PhotoMarket, a systematic design
space exploration framework for photonic hybrid quantum
neural networks applied to financial market prediction. By
jointly exploring multiple photonic design dimensions under
a unified evaluation protocol, the proposed framework provides
a methodology for understanding how architectural decisions
influence learning performance. Q-PhotoMarket serves not only
as a benchmark for photonic QML in finance but also as a
foundation for future research on automated photonic architecture
optimization and application-driven design space exploration
across various QML domains.
ACKNOWLEDGMENT
This work was supported in part by the NYUAD Center for
Quantum and Topological Systems (CQTS), funded by Tamkeen
under the NYUAD Research Institute grant CG008.
REFERENCES
[1] M. Cerezoet al., “Variational quantum algorithms,”Nature Reviews Physics,
vol. 3, no. 9, pp. 625–644, 2021.
[2] K. Zamanet al., “A survey on quantum machine learning: Current trends,
challenges, opportunities, and the road ahead,”arXiv:2310.10315, 2023.
[3] M. Cerezoet al., “Challenges and opportunities in quantum machine learning,”
Nature computational science, 2022.
[4] H. Zhuet al., “Quantum computing and machine learning on an integrated
photonics platform,”Information, vol. 15, no. 2, 2024.
[5] N. Maringet al., “A general-purpose single-photon-based quantum computing
platform,”arXiv preprint arXiv:2306.00874, 2023.
[6] N. Heurtelet al., “Perceval: A software platform for discrete variable photonic
quantum computing,”Quantum, vol. 7, p. 931, 2023.
[7] C. Nottonet al., “Merlin: A discovery engine for photonic and hybrid quantum
machine learning,”arXiv preprint arXiv:2602.11092, 2026.
[8] N. Maringet al., “A versatile single-photon-based quantum computing platform,”
Nature Photonics, vol. 18, no. 6, pp. 603–609, 2024.
[9] F. Elnakhalet al., “Q-photonas: Hybrid quantum neural architecture search
framework on photonic devices,”arXiv:2605.22097, 2026.
[10] M. Kashif and S. Al-Kuwari, “Design space exploration of hybrid quantum–
classical neural networks,”Electronics, 2021.
[11] S. Aaronson and A. Arkhipov, “The computational complexity of linear optics,”
inSTOC, 2011, pp. 333–342.
[12] N. Ayyildiz and O. Iskenderoglu, “How effective is machine learning in stock
market predictions?”Heliyon, vol. 10, no. 2, p. e24123, 2024.
[13] N. Innanet al., “Financial fraud detection using quantum graph neural networks,”
Quantum Machine Intelligence, vol. 6, no. 1, p. 7, 2024.
[14] P. K. Choudharyet al., “Hqnn-fsp: A hybrid classical-quantum neural network
for regression-based financial stock market prediction,”Quantum Machine
Intelligence, vol. 8, no. 1, p. 55, 2026.
[15] W. R. Clementset al., “Optimal design for universal multiport interferometers,”
Optica, vol. 3, no. 12, pp. 1460–1465, 2016.
[16] Y . Duet al., “Quantum circuit architecture search for variational quantum
algorithms,”npj Quantum Information, 2022.
[17] Z. He, M. Deng, S. Zheng, L. Li, and H. Situ, “Training-free quantum architecture
search,” inAAAI, 2024.
[18] L. Van der Maaten and G. Hinton, “Visualizing data using t-sne.”Journal of
machine learning research, vol. 9, no. 11, 2008.
[19] T. Akibaet al., “Optuna: A next-generation hyperparameter optimization
framework,” inKDD, 2019.
[20] I. M. de Diegoet al., “General performance score for classification problems,”
Applied Intelligence, 2022.
