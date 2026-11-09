---
title: Dynamic Sparse Causal-Attention Temporal Networks for Interpretable Causality Discovery in Multivariate
  Time Series
url: https://arxiv.org/abs/2507.09439
category: ai-marketing
subcategory: empirical
date: 2025-07
venue: ''
authors:
- Meriem Zerkouk
- Miloud Mihoubi
- Belkacem Chikhaoui
source: arxiv
pdf_url: https://arxiv.org/pdf/2507.09439
pages: 12
chars: 34812
fetched_at: '2026-11-08T13:15:40+00:00'
kb_version: 1
---

# Dynamic Sparse Causal-Attention Temporal Networks for Interpretable Causality Discovery in Multivariate Time Series

Dynamic Sparse Causal-Attention Temporal Networks for
Interpretable Causality Discovery in Multivariate Time Series
Meriem Zerkouk †,*, Miloud Mihoubi†, Belkacem Chikhaoui†
† Artificial Intelligence Institute, University of TELUQ, 5800, rue Saint-Denis, Montreal, Quebec, H2S 3L5, Canada
*meriem.zerkouk@teluq.ca
Abstract
Understanding causal relationships in multivariate time series (MTS) is essential for
effective decision-making in fields such as finance and marketing, where complex depen-
dencies and lagged effects challenge conventional analytical approaches. We introduce
Dynamic Sparse Causal-Attention Temporal Networks for Interpretable Causality Dis-
covery in MTS (DyCAST-Net), a novel architecture designed to enhance causal discovery
by integrating dilated temporal convolutions and dynamic sparse attention mechanisms.
DyCAST-Net effectively captures multiscale temporal dependencies through dilated con-
volutions while leveraging an adaptive thresholding strategy in its attention mechanism
to eliminate spurious connections, ensuring both accuracy and interpretability. A statis-
tical shuffle test validation further strengthens robustness by filtering false positives and
improving causal inference reliability. Extensive evaluations on financial and marketing
datasets demonstrate that DyCAST-Net consistently outperforms existing models such
as TCDF, GCFormer, and CausalFormer. The model provides a more precise estimation
of causal delays and significantly reduces false discoveries, particularly in noisy envi-
ronments. Moreover, attention heatmaps offer interpretable insights, uncovering hidden
causal patterns such as the mediated effects of advertising on consumer behavior and
the influence of macroeconomic indicators on financial markets. Case studies illustrate
DyCAST-Net’s ability to detect latent mediators and lagged causal factors, making it
particularly effective in high-dimensional, dynamic settings. The model’s architecture
enhanced by RMSNorm stabilization and causal masking ensures scalability and adapt-
ability across diverse application domains.
Causal Discovery, Multivariate Time Series, Dilated Convolutions, Sparse
Attention, Financial Analytics, Marketing Impact Analysis
1. Introduction
Understanding causal mechanisms in multivariate time series is critical for uncovering
the underlying dynamics in complex systems, with far-reaching applications in fields such
as healthcare, finance, urban planning, and marketing [wu2024causal].
Traditional machine learning models, including decision trees and standard neural net-
works, are primarily designed to capture correlations rather than directional causal influ-
ences. This limitation is significant because correlation, being symmetrical, often fails to
reveal the true underlying causes that drive system behavior, potentially leading to mislead-
ing conclusions [Chikhaoui2015ANG].
Historically, controlled interventions have been the gold standard for establishing causal-
ity. However, such approaches are often impractical in many real-world scenarios due to ethi-
cal, financial, or logistical constraints. Consequently, the rise of observational data combined
with sophisticated analytical techniques has spurred research into inferring causal relation-
ships without direct interventions [Chikhaoui2017DetectingCO]. Recent advances in
deep learning have demonstrated promising directions for causal discovery. Convolutional
Neural Networks (CNNs) have been applied to time series data to extract localized fea-
tures [nauta2019causal], while transformer-based models employing self-attention mecha-
nisms have proven effective in capturing long-range dependencies [vaswani2017attention].
Nevertheless, standard CNNs and vanilla transformers face challenges when dealing with
the non-linear, dynamic, and high-dimensional nature of multivariate time series. For in-
stance, conventional CNNs may struggle to model long-term dependencies, and transformers
arXiv:2507.09439v1  [cs.LG]  13 Jul 2025

2
can be computationally demanding and data-hungry. In this work, we propose DyCAST-
Net, a novel hybrid architecture that integrates an enhanced Temporal Convolutional Net-
work (TCN) [Krishna2024AutoIE] with dynamic sparse [Jiang2024MInference1A],
and multi-head attention mechanisms. Our model leverages dilated convolutions to capture
extended temporal dependencies efficiently, while the incorporation of a dynamic sparse
attention module allows it to selectively focus on key causal features, reducing noise and
redundancy. Additionally, we employ advanced normalization techniques, including RM-
SNormandLayerScale, toenhancetrainingstabilityandimproveinterpretability. DyCAST-
Net builds upon and extends recent developments in deep learning for causal inference
[Mihoubi2024DiscoveringCR] by fusing the localized feature extraction of improved
TCNs with the powerful long-range modeling capabilities of transformer-inspired attention.
We validate our approach on datasets from the finance and marketing sectors and com-
pare its performance against state-of-the-art methods such as TCDF, CausalFormer, and
GCFormer. Experimental results demonstrate that DyCAST-Net not only achieves higher
predictive accuracy and computational efficiency but also offers enhanced interpretability
through detailed attention score visualizations and delay heatmaps. Our work makes the
following significant contributions:
(1) HybridTCN–TransformerArchitecturewithSparseAttention[Lee2024ATS]
and RMSNorm. DyCAST-Net combines a Temporal Convolutional Network
(TCN) for short-range features and a Transformer branch with multihead attention
for long-range dependencies. RMSNorm stabilizes training, while optional attention
sparsity boosts efficiency.
(2) Localized Feature Cross Modules (LFCM/HFCM) to Merge Multi-scale
Context. Custom modules merge multi-scale context by exchanging intermedi-
ate features between TCN stages and Transformer blocks via up/down-sampling,
blending local (TCN) and global (Transformer) dynamics
(3) Enhanced Interpretability through Attention Visualization and Delay
Heatmaps. Beyond causal predictions, our framework visualizes channel-level at-
tentionandtemporaldelayheatmaps, clarifyinglearnedcausallinksandtime-lagged
dependencies.
(4) Superior Accuracy and Efficiency on Financial & Marketing Benchmarks.
ExperimentsonfinancialandmarketingdatasetsshowDyCAST-NetsurpassesBase-
lines models in accuracy, efficiency, and fine-grained interpretability.erving inter-
pretability and enabling more fine-grained causal inference.
The remainder of the paper is organized as follows: Section 2 reviews related work in causal
discovery and deep learning-based time series analysis. Section 3 details the proposed model
and its architecture. Section 4 presents experimental evaluations and comparative analyses,
and Section 5 concludes the paper with discussions on future research directions.
2. Related Work
Recent advancements in deep learning and attention mechanisms have significantly ad-
vanced causal discovery in multivariate time series (MTS), enabling the detection of complex
causal patterns and the handling of massive datasets.
Statistical and graph-based methods. Methods such as PCMCI [runge2019] integrate con-
ditional independence testing with time series structures to provide an effective multivariate
framework, though their scalability is limited by the computational overhead of repeated
tests across numerous variables and time steps in high-dimensional settings.
CNN approaches. Convolutional neural network approaches, exemplified by the Temporal
Causal Discovery Framework (TCDF) [nauta2019causal], excel at extracting localized

3
temporal features to model short-term dependencies, yet they may struggle with capturing
long-range or evolving interactions critical for constructing complete causal graphs.
Transformer and hybrid models. Transformer-based architectures [vaswani2017attention]
leverage self-attention mechanisms to capture global dependencies by dynamically attend-
ing to all time steps and variables, effectively uncovering intricate relationships; however,
these models demand extensive computational resources and large datasets to avoid overfit-
ting, posing challenges in resource-constrained scenarios. Further advances include recent
work leveraging latent contexts from multiple datasets [Gunther2023LatentContexts],
which emphasizes dataset-specific structures, as well as emerging methods such as GC-
Former [Xing2023GCFormerGC], inductive Granger causal modeling [chu2020], Daring
[he2021], andcausalfeatureselectionunderlatentconfounding[ Chikhaoui2014PatternbasedCR]
that strive to balance scalability, precision, and interpretability while contending with the
inherent trade-offs between computational complexity and robust causal inference.
AnotabledevelopmentinthislandscapeisCausalFormer[ Kong2024CausalFormerAI],
an interpretable transformer-based model specifically designed for temporal causal discovery.
Unlike earlier work that primarily examines only certain model components (e.g., attention
or convolution weights) to infer causality, CausalFormer incorporates a âĂĲcausality-aware
transformerâĂİ [Wang2024CausalityAwareTN] employing multi-kernel causal convolu-
tion and a decomposition-based causality detector. By leveraging regression relevance prop-
agation to interpret the trained modelâĂŹs global structure, CausalFormer constructs de-
tailed causal graphs that capture intricate temporal interactions. Experiments on synthetic,
simulated, and real datasets demonstrate its state-of-the-art performance in uncovering tem-
poral causality, underscoring the importance of interpretability in deep learning for causal
inference.
Despite these advances, critical challenges persist in temporal causal discovery presented
in table 1:
• Multi-scaleDependencyModeling : CNN-basedapproacheslikeTCDF[ nauta2019causal]
excelatlocalfeaturesbutneglectglobalinteractions, whileTransformers[ vaswani2017attention]
capture long-range dependencies at the cost of local granularity.
• Dynamic Sparsity: Most attention mechanisms [Xing2023GCFormerGC] em-
ploy dense computations, retaining noisy connections in high-dimensional MTS
[Kong2024CausalFormerAI].
• Interpretability-Complexity Trade-off: Though methods like CausalFormer
[Kong2024CausalFormerAI] improve transparency, their reliance on dense at-
tention obscures lag-specific causal pathways.
• Resource Constraints: Graph-based methods (e.g., PCMCI [runge2019]) scale
quadratically with variables, while Transformers require extensive data to avoid
overfitting [he2021].
3. Causal Discovery paradigm Using DyCAST-Net
The DyCAST-Net is designed to uncover causal relationships in multivariate time series
(MTS)data. Theparadigmleveragesacombinationofmulti-headattentionmechanismsand
convolutional neural networks to process temporal data and construct a Temporal Causal
Graph (TCG). This graph represents the discovered causal relationships and their associated
delays, providing insights into the temporal dynamics of the system under study. Figure 1
illustrates the architecture of DyCAST-Net, which operates usingN independent parallel
networks. Each network has the same structure but processes different input variables.

4
Table 1. Comparative Analysis of DyCAST-Net, TCDF, CausalFormer, and GCformer
Feature DyCAST-Net TCDF CausalFormer GCformer
Architecture
Dilated Convolutions
+ Multi-head Attention
+ Dynamic Sparsity
Dilated Convolutions
+ Attention Mechanism
Transformer
+ Self-Attention
GCN
+ Transformer
Attention
Type
Multi-head with
Dynamic Sparsity Local Attention Global Self-Attention Graph + Self-Attention
Normalization RMSNorm + LayerScale LayerNorm LayerNorm BatchNorm
Key Compo-
nents
- Depth-wise Convolutions
- Dynamic Pruning
- Skip Connections
- Causal Masking
- Dilated Convolutions
- Attention for Delay
Estimation
- Multi-head Attention
- Positional Encoding
- Graph Convolution
- Temporal Transformer
Handling
Long Depen-
dencies
Dilated Convolutions
+ Sparse Attention Dilated Convolutions Self-Attention GCN + Dilated Convo- lutions
Dynamic
Sparsity
Yes (Threshold-based) No No No
Computational
Efficiency
High (Sparse Attention) Medium Low (Dense Attention) Medium
Interpretability Attention Scores + Delay Heatmaps Attention Weights Attention Maps Graph Edges
Strengths
- Efficient Sparse-Attention
- Stable Training
- Explicit Delay
Estimation
- Temporal Delay
Detection
- Simple Architecture
- Long-Range
Dependencies
- Non-Linear Effects
- Spatial-Temporal
Modeling
- Graph-Based Causality
Limitations - Tuning Sparse Thresholds - Limited to Local Contexts - Computationally Heavy - Data-Hungry - Requires Predefined Graph Structure
3.1. Problem Statement
ThetaskoftemporalcausaldiscoveryfromMTSdatainvolvesanalyzingadataset X com-
posedof N continuoustimeseries, eachwithauniformlength T (i.e., X = {X1, X2, . . . , XN } ∈
RN ×T).
The primary goal is to uncover the causal relationships that exist among these time
series, quantify the time delays between causes and their corresponding effects, and represent
these findings within a temporal causal graph. In this approach, a directed causal graph
G = (V, E) is constructed, where each vertexvi ∈ V represents a distinct time seriesXi.
A directed edge ei,j ∈ E from vertex vi to vertex vj indicates that Xi causally influences
Xj. Additionally, the graph may include pathsp = {vi, . . . , vj}, which denote the sequence
of causal influence fromvi to vj. Importantly, each edge ei,j in the graph is labeled with
a weight d(ei,j), representing the time delay between the initial causeXi and the resulting
effect on Xj.
3.2. Our Proposed Architecture (DyCAST-Net)
We proposeDyCAST-Net, a novel deep learning architecture designed to uncover causal
relationships in multivariate time series (MTS) Our approach starts from raw time series
data (with N variables/channels and T time steps each) and culminates in acausal graph
whose nodes represent the original variables, while directed edges denote discovered causal
influences (along with an estimated time delay or strength). The architecture integrates:
• Dilated Convolution Blocks(a TCN-style backbone) to capture long-range tem-
poral dependencies.

5
• Multi-Head Attentionto highlight the most important temporal elements (posi-
tions) and channels (variables) [vaswani2017attention].
• Dynamic Sparse Attention, which prunes small attention weights to focus on
dominant causal signals.
• RMSNorm or LayerNormfor stable training, optionally combined withLayer-
Scale for better gradient flow.
• Skip Connectionsto preserve original signals and improve gradient propagation.
Figure 1 illustrates this pipeline, from raw MTS input to causal graph construction.
Figure 1. Illustration of DyCAST-Net’s training and optimization process.
3.2.1. Dilated Convolution Blocks with Skip Connections
We employ anN-channelTemporal Convolutional Network(TCN), stacking several layers
(DyCAST-Block) in sequence. Each block contains:

6
(1) Depthwise Dilated Convolution(stride=1) with a chosen kernel size (e.g., 2)
and dilation factord = 2l at layer l, to expand the receptive field.
(2) Causal Masking (a “chomp” operation) ensuring the convolution only uses past
and present information, preserving temporal causality.
(3) Normalization via RMSNorm or LayerNorm. RMSNormnormalizes based on the
RMS (root mean square) of each channel, while LayerNorm normalizes across fea-
tures. One can optionally addLayerScale if desired.
(4) Residual / Skip Connectionwith a non-linear activation, enabling deeper archi-
tectures without vanishing gradients.
Stacking L such blocks allows DyCAST-Net to model long-range dependencies effectively.
3.2.2. Multi-Head Attention with Dynamic Sparsity
Ineach DyCAST-Block, weintegratea multi-headattention module[vaswani2017attention]:
Attn(Q, K, V) = softmax
 QK⊤
√dhead + Mask

V,
where Q, K, V are projected embeddings of the blockâĂŹs features. Acausal maskensures
no attention to future time steps. Additionally, to promote interpretability and reduce noise,
we useDynamic Sparse Attention: any attention weight below a threshold is zeroed out
(pruning) so that the model focuses on the most significant relationships. This pruning is
especially useful in highlighting potential causal links.
3.2.3. Channel-Level Weighting for Variable Selection
Before or after the convolution blocks, a learnablechannel-level attention vectorα ∈ RN
(one weight per channel) modulates the input data:
Xweighted = X ⊙ Softmax(α),
where X is the original MTS, andSoftmax(α) ensures the weights sum to 1 and remain
positive. Channels whose corresponding learned weights are large are more influential in
predicting the target.
3.2.4. Training and Objective
DyCAST-Net is trained via a standardmean squared error(MSE) loss for next-step
(or multi-step) prediction. We may addℓ1 regularization to (a) the channel-level weights
α or (b) convolution kernels and attention matrices, thus encouragingchannel sparsity or
attention sparsity, respectively:
L(Θ) = 1 Teff
TeffX
t=1

ˆyt − yt
2
+ λK∥Kernels∥1 + λM ∥Masks∥1,
where Teff is the effective prediction range, and(ˆyt, yt) are predicted and true target values
at timet. Minimizing this loss encourages an accurate yet parsimonious (i.e., sparser) model.
3.3. Causality Detection
Once the DyCAST-Net model is trained to predict a specific target variable, we analyze
the learned parameters to:
(1) Identify causal channels(which input variables most strongly affect the target),
(2) Estimate causal delays(how far in the past each cause matters),
(3) Construct a directed causal graphthat encodes these relationships.

7
3.3.1. Channel Selection and Shuffle Test
Toextract potential causes, wefirstexaminethe channel-level attention vectorα(Sec.3.2.2).
Any channelj whose weightαj exceeds a thresholdτ is considered acandidate cause. Next,
to validate these candidates, we use ashuffle test:
• Randomly permute the time points of channelj.
• Recompute the prediction errorLtest with this permuted input.
• If Ltest degrades substantially compared to the baseline, channel j likely has a
genuine causal influence on the target.
3.3.2. Delay Estimation from Dilated Convolution Kernels
A key advantage of TCN-based models is thatdilated convolution filtersdirectly reveal
how far back in time a variable contributes. For each validated channelj, we examine the
learned convolution filter parameterswj at each block/layer. Theindex of the maximum
absolute weight indicates the dominant receptive field location. Combining that with the
dilation factor d yields the approximatetime delay:
delayj→target ≈ arg maxk

wj[k]

 × d.
This can be aggregated if multiple layers contribute.
3.3.3. Constructing the Causal Graph
To form thecausal graph, we do the following foreach targetvariable in the MTS:
• Node Definition: each channel/variablev ∈ {1, 2, . . . , N} is a node in the graph.
• Edge Definition: if a channel j is found to be a cause of the targeti, we add a
directed edge (j → i).
• Edge Weights (Delays): each edge is labeled with the discovered time delay or
an attention-based importance score. Thus,
(j → i) has edge attribute (delay)= delayj→i.
The final result is a directed graphG = (V, E) that encodes thewho-causes-whom relation-
ships along withhow far in the pastthey exert influence. Typically, large delays or minimal
attention scores might be pruned to yield a more concise causal subgraph.
Remark on Interpretation.In this causal graph:
• Nodes represent individual time series (variables) in the dataset.
• Directed edgesindicate the discovered causal effect from one variable to another.
• Edge values (labels)represent theestimated time lag(delay), or alternatively the
confidence/strength derived from final attention weights.
Hence, DyCAST-Net provides anend-to-end pipeline: from raw multivariate time series to
a concise, interpretable directed graph detailing the likely causes, their strengths, and their
temporal offsets.
4. Experiments Result and Discussion
To rigorously evaluate DyCAST-NetâĂŹs capabilities in temporal causal discovery, we
conductextensiveexperimentsaddressingthreecriticalquestions: Accuracy: DoesDyCAST-
Net outperform state-of-the-art baselines in identifying causal relationships and estimating
time delays? Robustness: How does the model handle noise and high-dimensional regimes?
Interpretability: Do attention patterns align with domain-specific causal mechanisms? We
evaluate DyCAST-Net on financial time series (Fama-French Three-Factor Model) and fMRI

8
data, comparing against table 1. Metrics include F1-score, precision, recall, and Delay Es-
timation Accuracy (DEA).
4.1. Dataset
We validate our model on two benchmarks: Finance and FMRI. The Finance benchmark
includes10datasetsgeneratedusingtheFama-FrenchThree-FactorModel[ Kleinberg2013],
focusing on factors like volatility, size, and value. We excluded one dataset lacking causal
relationships. The FMRI benchmark features 28 simulated BOLD datasets [Smith2011],
each representing distinct brain networks and tracking neural activity across various regions.
We excluded one dataset with 50 nodes due to processing limitations. These selections en-
sure that our model is tested on relevant and manageable datasets. The preprocessing of
data for DyCAST-Net involves several crucial steps. For the Finance dataset, we normal-
ized the time series using the z-score method. For the FMRI dataset, we applied a low-pass
filter to reduce noise. The data were then converted into PyTorch tensors of dimension
X ∈ RN ×T, where N is the number of time series and T is the number of time steps,
in accordance with the Input Representation and Preprocessing stage of the DyCAST-Net
model.
4.2. Experimental Setup
Hardware Configuration: All experiments were performed on a machine with the following
specifications:
• Processor: Intel Core i9-10700K @ 3.60GHz (12 cores, 24 threads)
• Memory: 64GB DDR4 RAM @ 3200MHz
• Graphics Card: NVIDIA GeForce RTX 3090 with 24GB GDDR6X
• Storage: 1TB NVMe SSD andOperating System: Windows 11
Evaluation protocol. We use 5-foldexpanding-window cross-validation: fold i trains on the
first 60+ 5i% of the timeline and tests on the next 10 %. Hyper-parameters (kernel, dilation
base, learning rate) are optimised on fold 0 via Bayesian search (50 trials). Early stopping
(patience 15) relies on validation loss. are retrained on thesame splits with seed 1111.
The configuration of key hyperparameters for training the DyCAST-Net are presented in
table 2, model was designed to ensure optimal learning while capturing complex temporal
dependencies.
Table 2. Training Configuration Parameters
Parameter Value
CUDA Enabled True (training conducted with GPU acceleration)
Number of Epochs 2000 (for prolonged and comprehensive learning)
Kernel Size 6 (optimized for capturing diverse temporal dependencies)
Number of Levels 2 (enhancing the modeling of complex relationships)
Learning Rate 0.001 (using the Adam optimizer for fine-tuned updates)
Dilation Rate 4 (expanding the receptive field for long-range dependency modeling)
Log Interval 500 (for detailed monitoring of model performance)
Seed 1111 (ensuring reproducibility of results)
Significance Level 0.5 (threshold for determining causal relationships)
4.3. Layer-wise specification
Table 3 specifies each layer of DyCAST-Net. The number of headsH is automatically
set to the number of seriesN (so that embed_dim=N remains divisible byH).

9
Table 3. Layer-by-layer specification of DyCAST-Net (N = number of time-series /
channels).
Block Type k Dilation Heads H Norm LayerScale τsparse Params
0 Depthwise Conv1d 4 20 N LayerNorm – 0.01 4N
1 Depthwise Conv1d 4 21 N LayerNorm – 0.01 4N
2 Depthwise Conv1d 4 22 N RMSNorm γ = 10−4 0.01 4N
k: kernel size,τsparse: dynamic pruning threshold (weights <τ are set to 0).
Experimental protocol. For every dataset we perform5-fold expanding-window cross-
validation: fold i trains on the first 60 + 5i% of the timeline and tests on the next 10
%. Hyper-parameters (k, dilation base, learning rate) are optimised on fold 0 via Bayesian
search (50 trials). Early stopping is triggered if the validation loss does not improve for
15 epochs. All modelsâĂŤincluding TCDF, CausalFormer and GCFormerâĂŤare re-trained
with the exact same splits.
4.4. Causal Discovery Results
The following section provides a detailed result of the causal discovery results, we examine
the inferred causal graphs at multiple training epochs and for different target nodes. Figures
3âĂŞ5 illustrate how certain causal links evolve over training, The following section provides
a detailed result of the causal discovery results obtained from our model on the Finance and
fMRI datasets. The analysis is based on the attention heatmaps and causal graphs generated
at different training epochs (100, 300, and the complete graph).
Figure 2. Causal relationships in finance data over different epochs (Left: 100, Middle:
300, Right: 2000)
The Finance dataset consists of 25 time series, each representing a financial variable.
The causal graphs at different epochs (Figures 3 depict the progressive discovery of causal
relationships. At 100 epochs, the graph is relatively sparse, indicating that only the most
dominant causal relationships are detected. By 300 epochs, the graph becomes denser,
revealing additional causal interactions. The final graph presents a comprehensive structure,
capturing the full extent of causal dependencies in the dataset. The attention heatmap
(Figure 5 ( left) illustrates the intensity of causal influence among the time series. The
color distribution in the heatmap highlights strong dependencies, with yellow indicating
high attention scores and dark purple representing weak or no relationships.
4.5. Analysis of the fMRI Dataset
Similar to the Finance dataset, the causal graphs for the fMRI dataset (Figures 4) show
the evolution of causal discovery over training epochs. At 100 epochs, only a few dominant
connections are identified. By 300 epochs, the graph complexity increases as more relation-
ships are discovered. The complete graph encapsulates the full causal structure, offering

10
Figure 3. Causal relationships in RMFI data over different epochs (Left: 100, Middle:
300, Right: 2000)
a comprehensive representation of brain connectivity. The fMRI dataset also consists of
sample of 9 time series, representing neural activity measurements. The attention heatmap
(Figure reveals patterns of interactions between different brain regions. Higher attention
scores (yellow regions) suggest strong causal influence, which aligns with expected neural
connectivity patterns.
(a) Finance-25 variables.
 (b) fMRI-9 variables.
Figure 4. Attention score heat-maps showing variable relationships ((a): Finance
dataset, (b): fMRI dataset)
4.6. Comparative Insights
The comparative analysis between the Finance and fMRI datasets reveals distinct char-
acteristics in causal structure evolution. The Finance dataset exhibits a more heterogeneous
distribution of causal relations, where some variables exert stronger influence over others.
In contrast, the fMRI dataset shows more uniform connectivity, which aligns with the in-
terconnected nature of neural activity. Overall, the results confirm the effectiveness of our
causal discovery model in uncovering meaningful relationships in both financial and neuro-
logical time series data. The progressive enhancement of the causal graphs demonstrates
that longer training durations enable a more refined understanding of causal dependencies.
This finding highlights the modelâĂŹs capability to generalize across different domains,
making it a robust tool for multivariate time series causal analysis.
5. Evaluation Metrics for Causal Discovery:Comparative Study
In this section, we present the evaluation metrics used to compare causal discovery models
in multivariate time series (MTS). Evaluating the performance of causal discovery models
requires multiple metrics that assess various aspects of accuracy, reliability, and structural

11
correctness. Below is a detailed comparison of key evaluation metrics used for causal dis-
covery in MTS :F1-Score, Recall, Precision and Delay Estimation Accuracy (DEA) where:
• Delay Estimation Accuracy (DEA):This metric evaluates how accurately the
model predicts the causal delays between time series. A higher accuracy indicates
a better estimation of temporal dependencies.
DEA = 1 − 1 n
nX
i=1
| ˆdi − di| (5.1)
Where di denotes the ground-truth delay of edgei and ˆdi the delay predicted by
DyCAST-Net, n is the number of true causal edges.
Table 3 presents a comparative analysis of different causal discovery models applied to the
Finance and fMRI datasets. The models are evaluated based on key performance metrics:
F1 Score, Recall, and DEA. The results highlight the strengths and weaknesses of each
approach in detecting causal relations and estimating delays.
Table 4. Comparison of Model Performance on Finance and fMRI Datasets
Model F1 (Finance) F1 (FMRI) Recall (Finance) Recall (FMRI) DEA
(DyCAST-Net 0.91 0.89 0.90 0.89 0.89
TCDF 0.84 0.84 0.83 0.83 0.80
GCFormer 0.86 0.85 0.83 0.84 0.81
Causalformer 0.87 0.87 0.86 0.88 0.85
5.1. Analysis of Model Performance
DyCAST-Net outperforms all other models, achieving the highest F1 Score (0.91 on
Finance, 0.89 on fMRI) and Recall (0.90 on Finance, 0.89 on fMRI). These results confirm
its superior ability to detect causal relationships. TCDF exhibits the weakest performance,
with lower Recall and F1 Scores, indicating challenges in capturing causal links and leading
to more false negatives. In contrast, CausalFormer provides a balanced performance (F1 =
0.87), demonstrating robustness in causal inference. Delay estimation accuracy (DEA) is
crucial for causal discovery. DyCAST-Net achieves the highest DEA (0.89), reinforcing its
ability to model temporal dependencies accurately. CausalFormer follows with 0.85, while
TCDF performs the worst (0.80), highlighting its limitations in delay estimation. Overall,
DyCAST-Net provides the best trade-off between F1 Score, Recall, and DEA, confirming its
effectiveness in causal inference. CausalFormer remains a strong alternative, particularly in
recall. GCFormer achieves moderate performance, outperforming TCDF but falling short
of DyCAST-Net. The findings highlight DyCAST-Net as the most robust model for causal
discovery in multivariate time series, balancing high accuracy and reliable delay estimation.
Conclusion
We introduced DyCAST-Net, a deep learning framework unifying dilated convolutions
and multi-head (sparse) attention for causal discovery and time series forecasting in com-
plex, noisy data. Compared to methods like TCDF, MGCFORMER, and CausalFormer,
it demonstrates robust performance and interpretable causal insights across both synthetic
and real-world domains (e.g., finance, fMRI). By combining local feature extraction with
global attention, DyCAST-Net achieves superior metrics (precision, recall, F1) and lower
MSE while revealing fine-grained causal links. Additionally, it shows resilience to non-
stationary signals, thanks to dynamic sparse attention and a flexible model design. Future
work will focus on improving computational efficiency, incorporating transformer-inspired or

12
hierarchical components, and adapting to irregular sampling and real-time learning. These
enhancements will reinforce DyCAST-NetâĂŹs interpretability and scalability, paving the
way for broader application in fields requiring reliable causal inference from dynamic sys-
tems.
References
[1] Wu, X., et al.: Causal Inference in the Medical Domain: A Survey. In: Applied Intelligence, 54, 4911-4934
(2024).
[2] Chikhaoui, B., et al.: A New Granger Causal Model for Influence Evolution in Dynamic Social Networks:
The Case of DBLP. In: AAAI Conference on Artificial Intelligence, (2015).
[3] Chikhaoui, B., et al.: Detecting Communities of Authority and Analyzing Their Influence in Dynamic
Social Networks. In: ACM Transactions on Intelligent Systems and Technology (TIST), 8, 1-28 (2017).
[4] Nauta, M., et al.: Causal Discovery with Attention-Based Convolutional Neural Networks. In: Proceed-
ings of the 2019 Conference on Neural Information Processing Systems (NeurIPS), 766-776 (2019).
[5] Vaswani, A., et al.: Attention is All You Need. In: Proceedings of the 31st International Conference on
Neural Information Processing Systems (NIPS), 6000-6010 (2017).
[6] Krishna, K., et al.: Auto imputation enabled deep Temporal Convolutional Network (TCN) model for
pm2.5 forecasting. In: ICST Transactions on Scalable Information Systems, (2024).
[7] Jiang, H., et al.: MInference 1.0: Accelerating Pre-filling for Long-Context LLMs Sparse Attention. In:
ArXiv, https://arxiv.org/abs/2407.02490 (2024).
[8] Mihoubi, M., et al.: Discovering Causal Relationships in Noisy Web Data for Sentiment Classifica-
tion Using Attention Mechanisms. In: WISE,https://api.semanticscholar.org/CorpusID:277382252
(2024).
[9] Lee, H., et al.: A Training-free Sub-quadratic Cost Transformer Model Serving Framework With Hier-
archically Pruned Attention. (2024).
[10] Runge, J., et al.: Inferring causation from time series in Earth system sciences. In: Nature Communi-
cations, 10, 2553 (2019).
[11] GÃĳnther, W., et al.: Causal Discovery for Time Series from Multiple Datasets with Latent Contexts.
In: Proceedings of the 2023 Conference on Uncertainty in Artificial Intelligence (UAI), 766-776 (2023).
[12] Xing, S., et al.: GCFormer: Granger Causality based Attention Mechanism for Multivariate Time
Series Anomaly Detection. In: 2023 IEEE International Conference on Data Mining (ICDM), 1433-1438
(2023).
[13] Chu, Y., et al.: Inductive Granger Causal Modeling for Multivariate Time Series. In: Proceedings of
the 2020 IEEE International Conference on Data Mining (ICDM), 972-977 (2020).
[14] He, Y., et al.: Daring: Differentiable Causal Discovery with Residual Independence. In: Proceedings of
the 27th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 596-605 (2021).
[15] Chikhaoui, B., et al.: Pattern-based causal relationships discovery from event sequences for modeling
behavioral user profile in ubiquitous environments. In: Information Sciences, 285, 204-222 (2014).
[16] Kong, L., et al.: CausalFormer: An Interpretable Transformer for Temporal Causal Discovery. In: IEEE
Transactions on Knowledge and Data Engineering, 37, 102-115 (2024).
[17] Wang, R., et al.: Causality-Aware Transformer Networks for Robotic Navigation. In: ArXiv,https:
//arxiv.org/abs/2409.02669 (2024).
[18] Kleinberg, S.: Causality, Probability, and Time. In: Cambridge University Press (2013).
[19] Smith, S.M., et al.: Network modelling methods for FMRI. In: NeuroImage, 54, 875-891 (2011).
