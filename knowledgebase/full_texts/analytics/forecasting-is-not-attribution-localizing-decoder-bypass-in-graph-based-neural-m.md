---
title: 'Forecasting Is Not Attribution: Localizing Decoder Bypass in Graph-Based Neural Marketing Mix
  Models'
url: https://arxiv.org/abs/2606.12687
category: analytics
subcategory: measurement
date: 2026-06
venue: arXiv (Cornell University)
authors:
- Yunbo Wang
- Bolbi Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.12687
pages: 15
chars: 46730
fetched_at: '2026-11-08T12:57:56+00:00'
kb_version: 1
---

# Forecasting Is Not Attribution: Localizing Decoder Bypass in Graph-Based Neural Marketing Mix Models

Forecasting Is Not Attribution:
Localizing Decoder Bypass in Graph-Based Neural Market-
ing Mix Models
Yunbo Wang yunbow4@uci.edu
Department of Electrical Engineering and Computer Science
University of California, Irvine
Bolbi Liu bolbi@adsgency.ai
AdsGency AI
Abstract
Marketing mix models are used both to forecast business outcomes and to attribute those
outcomes to marketing channels. These two goals are not equivalent. We study a failure
mode in graph-based neural MMM, which we callattribution bypass: a high-capacity de-
coder can obtain low forecasting error through target autoregression, dense communication,
channel co-movement, context, or latent memory while failing to route its counterfactual
sensitivity through the graph later used as the attribution object.
This paper makes a deliberately bounded claim. We do not claim that observational neu-
ral MMM identifies causal effects. Instead, we introduce DICE-MMM as a graph-learning
and graph-use diagnostic framework that separates three questions often conflated in graph-
basedMMM:whetherthemodelrecoversaplausibletemporalgraph, whetheritforecastsac-
curately, and whether the trained decoder’s perturbation-induced influence is graph aligned.
DICE Stage 1 trains a graph encoder with a restricted graph-mediated decoder. Stage 2
freezes the selected encoder and trains a graph-safe latent decoder whose cross-node com-
munication must pass through the supplied graph. We evaluate decoder use with coun-
terfactual influence graphs (CIG), autoregressive rollout influence graphs (AR-CIG), and
frozen-decoder graph-swap tests.
The empirical picture is intentionally not overclaimed. DICE improves stable graph recovery
over CausalMMM across controlledR/d/Tswaps and an external multi-graph rawlog stress
test. However, forecasting accuracy is not an attribution certificate: in a non-degenerate
sparse-target benchmark, no-graph and full-graph decoders achieve MSE@7 around0.004
while AR-CIG nAUPRC remains near or below zero, whereas an oracle graph achieves AR-
CIG nAUPRC0.807±0.129at comparable MSE. Frozen graph-swap further shows that the
decoder and AR-CIG diagnostic are functional: the same DICE-hard-trained decoder moves
from nAUPRC−0.044±0.006under hard/raw/full learned graph inputs to0.894±0.027
when supplied with the oracle graph. The remaining failure is also clear. Learned DICE
graph interfaces and label-free sparsification rules such as validation-MSE selection and
stability selection remain insufficient. The contribution is therefore a stress test and failure-
localization framework: it proves that low MSE can hide attribution bypass and localizes
the unsolved bottleneck to deployable graph-support selection rather than to forecasting or
decoder capacity.
1 Introduction
Marketing mix modeling (MMM) is a decision tool, not merely a forecasting tool(Borden, 1964; Gujar et al.,
2024). A deployed MMM system is used to decide which channels deserve budget, which channels should
1
arXiv:2606.12687v1  [cs.LG]  10 Jun 2026

be reduced, and which historical changes would have mattered under a different allocation. These decisions
require attribution. Yet many neural MMM evaluations validate only prediction error. This creates a
dangerous shortcut: a model can forecast well by exploiting target history, shared seasonality, channel
co-movement, dense communication, or latent memory, without learning a graph that supports faithful
attribution.
Graph-based neural MMM tries to expose the attribution interface by learning a directed temporal graph
and forecasting through it. This is appealing only if the decoder actually uses the graph. A strong decoder
can route information around a weak or dense graph and still reduce held-out MSE. We call this failure
modeattribution bypass. It is especially problematic in MMM because a low validation error can make an
unfaithful attribution graph look validated.
This paper is written to withstand the strictest interpretation of that concern. We do not present DICE-
MMM as a solved causal-attribution method. We present it as a diagnostic framework for separating graph
recovery, forecasting, and decoder-induced graph use. DICE Stage 1 trains a graph encoder with a restricted
graph-mediated decoder, so the graph-discovery gradients are not immediately dominated by a high-capacity
response model. DICE Stage 2 freezes the selected encoder and trains a graph-safe latent decoder, so response
modeling cannot rewrite the graph. To test whether the supplied graph matters, we measure decoder-induced
influence under source perturbations and perform frozen-decoder graph swaps.
The main empirical result is a separation. In the sparse-target benchmark, full and no-graph decoders
forecast about as well as oracle-graph decoders, but their AR-CIG alignment is near chance. Oracle graph
support yields high AR-CIG. More importantly, the same trained decoder produces near-chance AR-CIG
under dense learned graph inputs and high AR-CIG when swapped to the oracle graph. Thus the decoder
is not simply graph blind, and the AR-CIG diagnostic is not vacuous. The bottleneck is the learned graph-
to-support interface: current raw/hard posterior interfaces are too dense, and simple label-free selectors are
not yet reliable.
This leads to a conservative but useful conclusion. DICE-MMM does not show that a learned neural MMM
graph is already a deployable attribution object. It shows how to detect when it is not, how to rule out
several misleading explanations, and where the remaining technical problem lies.
Contributions.
1. We identifyattribution bypass, a failure mode in graph-based neural MMM where low forecasting error
coexists with decoder-induced influence that is not aligned with the attribution graph.
2. We propose DICE-MMM, a two-stage graph-learning and diagnostic framework that protects the graph
as an interface between discovery and high-capacity response modeling.
3. We define CIG/AR-CIG diagnostics and frozen graph-swap tests to distinguish three failure explana-
tions: a broken metric, a graph-blind decoder, and a weak learned graph support.
4. We provide empirical failure localization. Oracle graphs produce high AR-CIG, and the same frozen
decoder responds correctly when swapped to the oracle graph, but current learned graph interfaces
and label-free sparsification remain insufficient. This localizes the open problem to deployable sparse
graph-support selection.
2

Table 1:Claim–evidence map.The manuscript is framed around claims that the current experiments
can support. The boundary column states what isnotbeing claimed.
Claim Evidence Boundary
DICE improves graph recov-
ery.
Table 2 shows higher stable Final-20 AUROC than
CausalMMM across controlledR/d/Tswaps; Table 8
shows the same direction in an external rawlog stress
test.
Graph recovery alone does
not certify attribution.
Low MSE is not an attribu-
tion certificate.
Tables 4 and 5 show no/full/random or dense graph
decoders with competitive MSE but near-zero or neg-
ative AR-CIG nAUPRC.
This is a controlled graph-
known diagnostic, not a
real-world causal proof.
The decoder and AR-CIG di-
agnostic are functional under
correct graph support.
Oracle graph rows reach AR-CIG nAUPRC0.807±
0.129in sparse-target retraining and0.894±0.027in
frozen graph-swap.
Oracle support is an up-
per bound, not a deploy-
able learned graph.
The decoder is not simply ig-
noring graph input.
In Table 6, the same DICE-hard-trained decoder
changes from−0.044±0.006nAUPRC under
hard/raw/full graph inputs to0.894±0.027under
oracle graph input.
This does not imply the
learned graph support is
sufficient.
Current learned graph inter-
faces remain insufficient.
Tables 7 and 4 show validation-MSE sparsification,
stability selection, and true-density top-konly mod-
estly improve over dense/no/full controls and remain
far below oracle.
The paper localizes the
bottleneck; it does not
solve deployable support
selection.
What this paper does not claim.We do not claim that CIG or AR-CIG is a causal estimand. We do not
claim that observational graph learning identifies marketing causal effects without temporal, experimental,
and confounding assumptions. We do not claim that the current learned DICE graph is already a deployable
attribution graph. The strongest supported claim is narrower: forecasting accuracy, graph recovery, and
decoder-induced attribution faithfulness can sharply diverge, and the proposed diagnostics can localize the
divergence.
2 Related Work
Marketing mix modeling.Classical and Bayesian MMM models incorporate carryover, adstock, and
nonlinear shape effects to estimate channel response and support budget allocation decisions (Jin et al.,
2017). Recent graph-based MMM extends this line by learning heterogeneous channel structures and re-
sponse patterns from data. The closest baseline is CausalMMM, which formulates causal MMM as a graph
variational autoencoder with a causal relational encoder and a marketing response decoder (Gong et al.,
2024). Our work keeps the graph-based MMM motivation but asks a different question: after a graph is
learned, does the final decoder actually use it for attribution?
Temporal causal discovery and Granger-style graphs.Granger causality interprets temporal influ-
ence as predictive usefulness of one variable’s past for another variable’s future under conditioning (Granger,
1969). Neural Granger methods extend this idea with sparse neural predictors (Tank et al., 2021); PCMCI
and DYNOTEARS provide alternative time-series causal discovery approaches based on conditional indepen-
dence testing and score-based dynamic Bayesian network learning (Runge et al., 2019; Pamfil et al., 2020).
These methods help define and recover temporal dependence structures, but a recovered graph is not auto-
matically a faithful explanation of a separate high-capacity decoder. DICE focuses on this decoder-interface
gap.
High-capacity decoders and explanation faithfulness.Transformers and latent-memory decoders
can model long-range temporal patterns and nonlinear interactions (Vaswani et al., 2023; Fang et al., 2026;
Bailie et al., 2025). Their flexibility is useful for forecasting, but it also creates shortcut routes around
explicit attribution interfaces. Explanation literature has similarly warned that model-internal weights such
3

as attention are not guaranteed to be faithful explanations of model behavior (Jain and Wallace, 2019). We
adapt this concern to neural MMM: the relevant explanation object is not only a learned graph, but whether
the trained decoder’s counterfactual sensitivity is mediated by that graph.
3 Problem Setup
3.1 Multivariate MMM Time Series
We observeNentities, such as shops, brands, regions, or campaign groups. For entityn, let
Vn,t = [Xn,t,1,...,X n,t,d,yn,t]∈R C, C=d+ 1,(1)
whereX n,t,i is the spend, exposure, or activity of marketing variablei, andyn,t is the target KPI. Each
entity also has optional contextcn. The forecasting task is to predict a future horizon
ˆyn,t+1:t+M =F θ(Vn,1:t,cn,Zn),(2)
whereZ n is an entity-specific directed temporal graph.
In our controlled synthetic benchmark, the graph label is known. We use the directed off-diagonal edge set
E={(i,j) :i,j∈{1,...,C},i̸=j},|E|=C(C−1),(3)
and store labels as edge vectors. We follow the source-to-receiver convention:Aij = 1means variablei
influences variablej. Self-links are excluded from graph recovery metrics.
3.2 Granger-Style Graph Interpretation
We interpretZn,ij = 1as a Granger-style temporal influence: the past trajectory of source variableiis
predictivelyusefulforreceivervariablejafterconditioningontheobservedmultivariatehistory. Onsynthetic
data,Z n is compared to the ground-truth data-generating graph. On observational data,Zn should be read
as a structural predictive graph unless stronger assumptions hold: temporal precedence, adequate variation,
observed confounder control, and stable response mechanisms.
3.3 Attribution Bypass
A high-capacity decoder can be accurate for the wrong reason. LetLpred(F)denote forecasting loss on the
observational distribution:
Lpred(F) =E V∼Pobs
[
∥F(V)−Y∥ 2 2 ] .(4)
Prediction loss only constrains the model on observed trajectories. Attribution probes evaluate the model
under perturbed trajectories, which may lie outside the observational support. Therefore two decoders can
have identical observational forecasting loss but different counterfactual behavior.
Diagnostic proposition.LetMbe the support of observed trajectories. Suppose two decodersF 1 and
F2 satisfyF 1(V) =F 2(V)for allV∈M. For a perturbation operatorB i that modifies source variablei,
Bi(V)need not lie inM. ThusF 1(Bi(V))andF 2(Bi(V))can differ even whenF 1 andF 2 have the same
forecasting error. Forecasting accuracy alone therefore cannot certify attribution faithfulness.
3.4 Decoder-Induced Counterfactual Influence Graph
We define the decoder-induced counterfactual influence graph (CIG) as a diagnostic for attribution bypass.
CIG is not a causal estimand. It measures how the trained decoder’s prediction changes when one source
variable is perturbed.
LetB m i (V)be a perturbation of source variableiunder modem∈{zero,mean,shuffle}. Zero replacement
removesthesourcehistory, meanreplacementsubstitutesthetraining-setnodemean, andshufflereplacement
4

swaps the source trajectory across entities. For a trained decoderFθ, the one-step CIG score from sourcei
to receiverjis
S1step ij =E n,t [|Fθ,j(Vn,1:t)−F θ,j(Bm i (Vn,1:t))|].(5)
For forecasting, perturbations can propagate autoregressively. We therefore define
SAR ij =E n,t,h
[⏐⏐⏐ ˆV AR n,t+h,j(V)− ˆV AR n,t+h,j(Bm i (V)) ⏐⏐⏐ ] , h= 1,...,M.(6)
AR-CIG perturbs only the observed prefix and compares the rolled-out forecasts over the final horizon. We
convert CIG scores to edge rankings and report AUROC, AUPRC, and normalized AUPRC against the true
graph on synthetic data.
4 DICE-MMM
4.1 Overview
DICE-MMM is a two-stage graph-mediated MMM framework. It consists of a DICE graph encoderqϕ(Z|X)
and a graph-safe latent response decoderpψ(Y|X,c,Z). The design is intentionally asymmetric. Stage 1
is optimized for graph discovery: the encoder is trained with a restricted graph-mediated decoder so that
predictive information must pass through candidate edges. Stage 2 is optimized for response modeling:
the selected encoder is frozen and a stronger latent decoder is trained under the fixed graph. The central
invariant is that the final decoder may be high-capacity in time and within-node latent memory, but every
cross-node path must be mediated by the learned graph.
This separation is the meaning ofdecoder invariance. The graph should not depend on whether the final
response model is an MLP, an RNN, a transformer, or a latent-memory decoder. If the graph changes
whenever the decoder becomes stronger, then the graph is not an attribution object; it is merely a byproduct
of a forecasting architecture. DICE-MMM therefore treats the graph as a protected interface between
discovery and forecasting.
4.2 DICE Graph Encoder
The encoder parameterizes a factorized categorical posterior over directed off-diagonal edges:
qϕ(Z|X) =
∏
(i,j)∈E
qϕ(zij|X), q ϕ(zij|X) = Cat(zij;πij).(7)
It returns edge logitsaij∈R 2 for no-edge and edge classes, withπij = softmax(aij). The interface remains
compatible with CausalMMM-style graph-VAE training: the encoder returns[B,E,2]edge logits, which can
be sampled with Gumbel-softmax during Stage 1 and converted into soft or hard graph inputs during Stage
2.
The DICE encoder adds two graph-discovery biases. First, it uses strictly causal temporal node encodings:
each node history is projected and passed through left-padded dilated residual temporal convolutions, fol-
lowed by attention pooling and summary statistics. This prevents the encoder from using future observations
when constructing node representations. Second, it constructs directed pair features from sender and re-
ceiver summaries, including sender–receiver contrasts, elementwise interactions, and lag-aware past(source)
→future(receiver) correlations. For lagsD, a directed lag feature is
ρd(i→j) = 1 T−d
T−d∑
t=1
¯xt,i¯xt+d,j, d∈D,(8)
combined with antisymmetric contrastsρd(i→j)−ρ d(j→i). These features provide a lightweight Granger-
style inductive bias without using ground-truth edge labels.
Figure 1 shows the implemented encoder pipeline. The important architectural point is that DICE is not
simply a larger encoder. Its temporal blocks make the node summaries causal; its lag features make the edge
5

Figure 1:DICE graph encoder used in Stage 1.The encoder maps node histories to strictly causal
temporal representations, summarizes each node, constructs directed sender–receiver features with lag-aware
Granger-style cues, initializes edge logits with an MLP, and refines the edge states through edge–node–edge
relational interaction. Stage 1 pairs this encoder with a restricted graph-mediated decoder so that graph
discovery cannot be hidden by a high-capacity response decoder.
candidates directional; and its relational refinement lets a candidate edge be judged in the context of other
incoming evidence. The output remains ordinary edge logits, so the same graph metrics, Gumbel sampling,
and KL terms used by CausalMMM still apply.
4.3 Stage 1: Restricted-Decoder Graph Discovery
Stage 1 trains the graph encoder with a restricted graph-mediated decoderfθ0. We sample a relaxed graph
using Gumbel-softmax:
˜zij,k = exp((aij,k +gij,k)/τ)∑
k′∈{0,1} exp((aij,k′ +gij,k′)/τ), g ij,k∼Gumbel(0,1).(9)
The Stage-1 objective is a graph-VAE loss:
Jstage1(ϕ,θ 0) =E qϕ(Z|X)[−logp θ0(X2:T|X1:T−1,c,Z)] +λKL(q ϕ(Z|X)∥p(Z)).(10)
The restricted decoder is not a performance concession; it is an identification device for the graph-learning
problem. If a powerful response decoder is used during graph discovery, prediction gradients can improve
MSE by exploiting shortcuts that do not require correct edges. In the controlled synthetic setting, ground-
truth edges are used for evaluation and diagnostic checkpointing only; no edge cross-entropy, ranking, or
Brier supervision is used in the main Stage-1 training loss. A deployable observational system would require
label-free checkpointing and sparsification, which we report as a limitation rather than hide.
4.4 Stage 2: Frozen Graph-Safe Latent Response Decoder
After Stage 1, we select a graph encoder checkpoint by the synthetic validation graph diagnostic or by a
pre-specified late-window rule, freeze the encoder, and train only the Stage-2 decoder. The Stage-2 decoder
6

receives either the posterior mean graph ¯Z=E qϕ⋆ (Z|X)[Z]or a deterministic hard graph. Its objective
emphasizes target forecasting:
Jstage2(ψ;ϕ⋆) =β allLall +βyLy +βMLy,M,(11)
whereL all is all-node MSE,Ly is target MSE over the full prediction sequence, andLy,M is target MSE
over the final forecasting horizon. The Stage-2 checkpoint is selected by validation target-horizon MSE. This
stage answers the forecasting question without allowing forecasting gradients to rewrite the graph.
4.5 Graph-Safe Latent Decoder
The Stage-2 decoder features a high-capacity yet graph-safe architecture, drawing inspiration from Latent
Thought Models (LTM) (Kong et al., 2025) and the factored attention framework of NNN (Mulc et al., 2025).
It converts frozen edge probabilities into an adjacency matrixA, restricting cross-node communication to
graph message passing while independently applying temporal self-attention.
˜ht,j =h t,j +η
∑
iAijWght,i∑
iAij +ϵ .(12)
Temporal self-attention is applied independently per node, not over all time–node tokens. Node-specific
causal latent memory slots are generated from graph-filtered prefixes:
pt,j = 1 t
t∑
s=1
hs,j, ζ t,j,1:K =m ψ(pt,j,c,d j),(13)
whered j contains graph degree features. Each node attends only to its own latent slots. Thus, the target
node cannot access a global latent memory that pools all channels and bypasses the graph. Optional context-
conditioned Hill saturation can be applied to the raw target prediction to model diminishing returns.
Figure 2 illustrates why Stage 2 can be expressive without destroying attribution. The latent decoder can
model nonlinear carryover, delayed response, contextual heterogeneity, and temporal dependencies, but the
only way one channel can affect another node’s state is through the frozen graph adjacency. This is the
mechanism that turns graph recovery into graph-mediated forecasting rather than merely reporting a graph
next to a separate black-box forecaster.
5 Experiments
We organize the empirical section around six questions a strict reviewer should ask. Table 2 asks whether the
DICEencoderimprovesgraphrecovery. Table3askswhetherrestrictedgraphdiscoverysacrificesforecasting.
Table 4 asks whether low MSE certifies attribution in a non-degenerate sparse-target benchmark. Table 5
repeats the bypass diagnostic in the original response setting. Table 6 asks whether the decoder is graph-
blind by swapping graph inputs while freezing decoder weights. Table 7 asks whether current learned graph
interfaces and label-free sparsification solve the support-selection problem. Table 8 reports an external
graph-recovery stress test.
5.1 Experimental Protocol
Data.We use controlled synthetic MMM datasets with known directed graphs, following the data gen-
eration protocol established by CausalMMM(Gong et al., 2024). Each sample is an entity-level time series
withdmarketing nodes and one target node. The generator samples one ofRlatent graph prototypes
for each entity, then generates channel, mediator, and target trajectories with lagged nonlinear temporal
dependencies and optional Hill-style saturation. Table 2 follows one-factor-at-a-timeR/d/Tgraph-recovery
swaps. The original response-diagnostic setting usesR= 10,d= 10,T= 120and contains a degenerate
target-parent label set, so attribution is evaluated over all directed off-diagonal edges. The new sparse-target
benchmark removes that degeneracy by making only a subset of channels direct or mediated drivers of the
target, allowing target-facing attribution diagnostics in addition to all-edge AR-CIG.
7

Figure 2:Graph-safe latent decoder used in Stage 2.The decoder builds causal token states from
historical data and context, generates node-specific latent memory slotsζ, and applies factored graph–
temporal–latent updates. Spatial communication is constrained by the frozen graph, temporal attention is
per node, and latent cross-attention uses node-specific slots rather than a global memory that could bypass
Z.
Graph convention and metrics.We use the source-to-receiver convention:Aij = 1means source node
iinfluences receiver nodej. Self-links are excluded. Graph recovery is evaluated by AUROC. For Table 2,
we reportFinal-20AUROC, the late-window average over the last 20 epochs, andMaxAUROC, the best
validationAUROCdiagnostic. Final-20isthemaincheckpoint-stablenumber; Maxisasensitivitydiagnostic.
Forecasting is evaluated by target MSE at fixed horizons. Attribution faithfulness is evaluated by AR-CIG
AUPRC and normalized AUPRC,
nAUPRC = AUPRC−π 1−π ,(14)
whereπis the edge prevalence. ThusnAUPRC≈0indicates prevalence-level attribution even when raw
AUPRC is numerically nonzero. Negative nAUPRC indicates worse-than-prevalence ranking.
Seeds and checkpointing.All main tables report mean±standard deviation over 10 pre-specified seeds
unless otherwise stated. Stage-1 graph checkpoints are selected by the same late-window rule or validation
graph diagnostic across graph-discovery methods in synthetic graph-known experiments. Stage-2 decoder
checkpoints are selected by validation target-horizon MSE. Graph-swap experiments freeze decoder weights
and change only the graph input at evaluation time. No seed is selected based on test performance.
8

Figure 3:Synthetic heterogeneous causal structures for theR= 5benchmark.The top row shows
five graph prototypes over ten channel nodes and one KPI node, and the bottom row shows the corresponding
directed causal matrices. We use the conventionA(i,j) = 1if source nodeiinfluences receiver nodej.
5.2 Graph Recovery underR/d/TSwaps
Table 2 evaluates whether DICE improves stable graph discovery. DICE Stage 1 improves Final-20 AUROC
over CausalMMM in every completed column. This table supports the graph-recovery claim only; it does
not imply that a downstream decoder uses the graph for attribution.
Table 2:Graph recovery underR/d/Tswaps.We report AUROC mean±std over 10 seeds. “Final-20”
is the late-window average over the last 20 epochs and is the main checkpoint-stable number. “Max” is the
best validation AUROC diagnostic and is treated as a sensitivity number. Bold indicates the higher value
within each completed column.
(a) Channel-number swap:R= 5,T= 120
d= 5d= 10d= 20
Method Final-20 Max Final-20 Max Final-20 Max
CausalMMM0.672±0.239 0.814±0.061 0.688±0.058 0.761±0.031 0.611±0.007 0.625±0.009
DICE-MMM Stage 10.726±0.019 0.823±0.032 0.707±0.020 0.762±0.018 0.614±0.030 0.653±0.029
(b) Series-length swap:R= 5,d= 10
T= 30T= 120T= 720
Method Final-20 Max Final-20 Max Final-20 Max
CausalMMM0.763±0.013 0.777±0.015 0.688±0.058 0.761±0.031 0.687±0.065 0.779±0.027
DICE-MMM Stage 10.776±0.031 0.796±0.014 0.707±0.020 0.762±0.018 0.738±0.010 0.781±0.013
(c) Latent-structure-number swap:d= 10,T= 120
R= 5R= 10R= 20
Method Final-20 Max Final-20 Max Final-20 Max
CausalMMM0.688±0.058 0.761±0.031 0.643±0.065 0.681±0.041 0.580±0.073 0.615±0.021
DICE-MMM Stage 10.707±0.020 0.762±0.018 0.668±0.024 0.752±0.009 0.612±0.080 0.702±0.055
9

Interpretation.DICE Stage 1 is consistently better under the stable Final-20 rule, but several improve-
ments are modest. We therefore use this table only to establish that the DICE encoder carries graph-recovery
signal. The later attribution tables decide whether that signal becomes decoder-induced attribution.
5.3 Forecasting Sanity Check
Table 3 tests whether restricted graph discovery comes at a prediction cost. It does not. DICE Stage 1
with a restricted graph-mediated decoder is already the strongest forecaster in this table. Therefore Stage
2 should not be justified as an MSE improvement; its purpose is to test graph-safe high-capacity response
modeling under a frozen graph interface.
Table 3:Forecasting sanity check on theR= 10,d= 10,T= 120response-diagnostic setting.All
rows are selected by validation forecasting MSE under the same seed/split protocol. This table tests whether
DICE graph learning incurs a prediction penalty. It is not evidence of attribution faithfulness.
Method Graph source Final decoder Encoder in final stage MSE@1↓MSE@7↓MSE@30↓
CausalMMM original CREncoder MRDecoderS trained end-to-end0.051±0.068 0.253±0.212 0.421±0.098
DICE-MMM Stage-1 only DICE encoder restricted graph-mediated MRDecoderS trained0.011±0.006 0.129±0.097 0.238±0.062
DICE-MMM Stage-2 freeze frozen DICE encoder LatentGraphDecoder frozen0.058±0.104 0.173±0.198 0.244±0.282
Interpretation.The restricted decoder is restricted in bypass capacity, not in forecasting usefulness. This
prevents a misleading explanation in which graph recovery improves only because prediction is sacrificed. It
also reinforces the central point: forecasting sanity is necessary, but not sufficient for attribution.
5.4 Non-Degenerate Sparse-Target Bypass Diagnostic
Table 4 is the cleanest attribution result. The sparse-target benchmark removes the degenerate target-parent
issue from the original response-diagnostic setting. The decisive pattern is that no-graph and full-graph
decoders achieve essentially the same MSE@7 as oracle-graph decoders, but their AR-CIG nAUPRC is near
or below zero. Oracle graph support reaches high AR-CIG. This validates the diagnostic separation between
prediction and graph-mediated influence.
Table 4:Sparse-target decoder diagnostic.The sparse-target setting is non-degenerate for target-facing
attribution. All rows use the same decoder family and report MSE@7 and AR-CIG nAUPRC. Low MSE
alone is uninformative: no-graph and full-graph inputs forecast as well as oracle graph input but remain
near prevalence in AR-CIG.
Graph input / selector Uses graph labels? MSE@7↓AR-CIG nAUPRC↑Interpretation
Oracle graph yes0.004±0.001 0.807±0.129Correct support yields graph-mediated influ-
ence at the same forecasting scale as shortcut
controls.
Stability selection, freq≥60%no0.004±0.002 0.091±0.004Modest positive signal, far below oracle.
Top-ktrue density yes0.005±0.002 0.077±0.027Diagnostic sparse support using oracle density;
still far below oracle, so ranking is weak.
No graph no0.004±0.001−0.005±0.005Temporal shortcut control: excellent MSE
without graph-mediated influence.
Full graph no0.004±0.001−0.047±0.014Dense communication control: excellent MSE
but worse-than-prevalence attribution ranking.
Interpretation.This table is deliberately unfavorable to overclaiming. It proves that the decoder and AR-
CIG can work under correct graph support, while showing that current learned supports do not approach that
upper bound. It also gives the strongest version of the paper’s central warning: in this benchmark, MSE@7 is
essentially indistinguishable across oracle, no-graph, and full-graph inputs, while AR-CIG nAUPRC ranges
from0.807to negative values.
10

5.5 Strong-Decoder Bypass Diagnostic in the Original Response Setting
Table 5 evaluates the same LatentGraphDecoder family under different graph inputs in the originalR=
10,d= 10,T= 120response-diagnostic setting. Because target-parent labels are degenerate in this setting,
we report all-edge AR-CIG. The oracle graph again yields high AR-CIG, while no/full/random graph controls
forecast competitively with near-prevalence AR-CIG.
Table 5:Strong-decoder bypass diagnostic in the original response setting.All rows use the same
LatentGraphDecoder family; only the graph input changes. Low MSE is not sufficient for faithful attribution:
full/no/random graph inputs can forecast competitively while producing chance-level AR-CIG.
Model / graph input Graph AUROC↑MSE@7↓AR-CIG AUPRC↑AR-CIG nAUPRC↑Interpretation
DICE-MMM learned graph + latent decoder0.750±0.0090.334±0.247 0.199±0.006−0.036±0.008Better learned graph and MSE than
the CausalMMM-graph hybrid, but
all-edge AR-CIG remains weak.
CausalMMM graph + latent decoder0.627±0.112 0.521±0.264 0.239±0.038 0.016±0.049Weaker learned graph; CIG remains
near prevalence.
Oracle graph + latent decoder oracle0.428±0.2380.903±0.024 0.874±0.031Attribution upper bound; validates
the AR-CIG diagnostic.
No graph + latent decoder –0.337±0.261 0.222±0.010−0.007±0.013Temporal shortcut control: compet-
itive MSE without graph-mediated
attribution.
Full graph + latent decoder –0.305±0.2230.192±0.005−0.046±0.007Dense communication control: low-
est MSE but poor attribution align-
ment.
Random graph + latent decoder random0.434±0.277 0.213±0.009−0.018±0.011Sparse wrong-graph control; CIG
collapses to chance.
Interpretation.The full graph has the best MSE@7 but negative AR-CIG nAUPRC. The oracle graph
does not have the best MSE@7 but has high AR-CIG alignment. Thus observational forecasting error cannot
validate attribution. The learned DICE graph improves graph AUROC, but the hard/raw learned-graph
interface remains near chance. This motivates the graph-swap and graph-interface analyses below.
5.6 Frozen-Decoder Graph Swap
Table 6 is the strongest failure-localization experiment. It freezes decoder weights and changes only the graph
input. If the decoder were completely graph blind, swapping to the oracle graph would not change AR-CIG.
Instead, the same DICE-hard-trained decoder jumps from negative AR-CIG nAUPRC under hard/raw/full
graph inputs to0.894±0.027under oracle graph input.
Table 6:Frozen-decoder graph swap.Decoder weights are fixed; only the graph input is swapped.
∆Pred MAE@7 measures the prediction change relative to the trained graph input and is diagnostic rather
than an accuracy metric. The large AR-CIG jump under oracle graph input shows that the decoder can use
a correct graph.
Fixed decoder Evaluation graph MSE@7↓∆Pred MAE@7 AR-CIG nAUPRC↑
DICE-hard trained hard / raw / full0.336±0.244 0.000±0.000−0.044±0.006
DICE-hard trained oracle0.360±0.244 0.036±0.0180.894±0.027
DICE-hard trained top-ktrue density0.513±0.265 0.080±0.032 0.137±0.066
Oracle-trained oracle0.428±0.238 0.000±0.000 0.874±0.031
Oracle-trained top-ktrue density0.590±0.251 0.063±0.026 0.142±0.063
Oracle-trained no / full / random low / competitive nonzero near0
Interpretation.The graph-swap experiment rules out two misleading explanations. First, AR-CIG is not
merely broken: oracle graph input yields high AR-CIG. Second, the latent decoder is not incapable of using
graph input: the same frozen decoder becomes graph aligned when supplied with the oracle graph. The
11

remaining failure is more specific: the learned graph support delivered to the decoder is too dense or too
weakly ranked. The top-krows show modest transfer signal, but they remain far from oracle.
5.7 Learned Graph Interfaces and Label-Free Selectors
Table 7 asks whether the learned DICE posterior can be converted into deployable sparse graph support.
The answer is currently no. Raw and hard interfaces collapse into dense support; true-density top-kis
diagnostic because it uses graph-label information; and two label-free selectors, validation-MSE sufficiency
and stability selection, do not recover attribution-aligned support.
Table 7:Learned graph interfaces and graph-support selectors.These experiments test whether
learned edge scores can be converted into decoder-consumable sparse support. Label-free selectors are
deployable in principle but remain insufficient in the current implementation. True-density top-kis an
oracle-density diagnostic, not a deployable method.
Setting Graph interface / selector Uses graph labels? Density / support MSE@7↓AR-CIG nAUPRC↑Interpretation
Old R10/M7 raw posterior no mean weight1.000±0.000 0.305±0.220−0.039±0.010Posterior ranking exists, but soft in-
terface is effectively dense.
Old R10/M7 hard thresholdp(e)>0.5no110.0±0.0edges0.336±0.244−0.044±0.006Threshold selects all edges; equiva-
lent to full graph.
Old R10/M7 temperature soft,τ= 5no mean weight0.893±0.016 0.322±0.195−0.043±0.006Softer probabilities remain too
dense.
Old R10/M7 validation-MSE sparse,ϵ= 3%no selected0.297±0.232−0.028±0.021MSE-sufficient sparsification fails as
attribution selection.
Old R10/M7 stability selection, freq≥60%no selected0.265±0.217−0.048±0.011Stable edges are not necessarily
attribution-faithful edges.
Old R10/M7 top-ktrue density yes25.0±0.0edges0.417±0.335 0.132±0.064Oracle-density sparsification gives
modest lift, not a deployable solu-
tion.
Old R10/M7 top-khigh precision partly diagnostic13.0±0.0edges0.315±0.236 0.080±0.048Higher precision support gives a
small positive signal.
Old R10/M7 one-stage strong end-to-end no learned0.158±0.168−0.051±0.011Lowest MSE, but graph AUROC
collapses and AR-CIG is negative.
Sparse-target stability selection, freq≥60%no selected0.004±0.002 0.091±0.004Positive but far below oracle0.807±
0.129.
Sparse-target top-ktrue density yes true density0.005±0.002 0.077±0.027Even oracle-density top-kremains
weak, showing edge ranking is not
sufficient.
Interpretation.This table is the main reason the manuscript must be framed as diagnostic rather than
as a solved attribution method. Validation-MSE selection fails because MSE is itself the wrong certificate.
Stability selection fails because stable predictive edges can reflect seasonality, autoregression, or channel
co-movement rather than target-relevant attribution structure. True-density top-kand high-precision top-k
show only modest transfer signal. Therefore the remaining problem is not merely choosing a threshold; it is
learning or selecting sparse graph support that is faithful to decoder-induced target influence.
5.8 External Multi-Graph Rawlog Stress Test
Table 8 tests whether the DICE graph encoder advantage is specific to the controlled synthetic generator.
This is an external graph-recovery stress test, not an attribution table. DICE rawlog with magnitude prior
substantially improves Final-20 AUROC over CausalMMM original rawlog. The Hill/saturation toggle has
little effect on DICE graph recovery, suggesting that the gain comes primarily from the graph encoder and
magnitude prior rather than from the saturation head.
12

Table 8:External multi-graph rawlog stress test.We report graph AUROC on the CausalRiver/rawlog
multi-graph setting. This table evaluates graph recovery robustness only; it is not a decoder-induced attri-
bution experiment.
Model Hill/saturation Final-20 AUROC↑Max AUROC↑
DICE rawlog + magnitude prior off0.6607±0.01630.6692±0.0019
DICE rawlog + magnitude prior on0.6632±0.0097 0.6692±0.0019
CausalMMM original rawlog on0.4557±0.0112 0.6115±0.0223
CausalMMM original rawlog off0.4281±0.0081 0.6128±0.0212
Interpretation.The external stress test supports the graph-discovery claim from Table 2. It should not be
used to support attribution faithfulness. The paper’s attribution evidence comes from oracle/no/full/random
controls, sparse-target diagnostics, and frozen graph-swap.
6 Discussion
The experiments support a narrower and stronger story than “DICE-MMM is a better forecaster.” They
separate four claims.
First, DICE improves graph discovery. Table 2 shows stronger stable graph recovery underR/d/Tswaps,
and Table 8 shows the same direction in an external multi-graph rawlog stress test. This establishes that
the encoder is not random, but graph recovery is not attribution.
Second, forecasting and attribution are empirically separable. Tables 4 and 5 show that no-graph and full-
graph decoders can forecast competitively while AR-CIG remains near prevalence. The sparse-target result
is particularly stark: oracle, no-graph, and full-graph inputs all obtain MSE@7 around0.004, but only the
oracle graph yields high AR-CIG alignment.
Third, the AR-CIG diagnostic and graph-safe decoder are functional under correct graph input. Oracle graph
supportyields highAR-CIG whenthe decoder is trained with it, and the frozen graph-swap experiment shows
that the same decoder can become graph aligned when supplied with the correct graph. This rules out a
simple “the decoder ignores graphs” explanation.
Fourth, the current learned graph interface is insufficient. Raw posterior and hard-threshold interfaces
are too dense. Validation-MSE sparsification fails because MSE is not an attribution certificate. Stability
selection gives only a small lift in the sparse-target setting and fails in the original response setting. Top-k
true density gives modest positive AR-CIG but is diagnostic because it uses oracle density. The remaining
technical challenge is therefore deployable graph-support selection: converting learned temporal edge scores
into sparse support that is both predictive enough and attribution aligned.
This is the central contribution of the paper. The experiments do not prove that DICE has solved neural
MMM attribution. They prove that a common validation pattern is unsafe, provide controls that expose
the failure, and localize the bottleneck to a specific interface between graph learning and decoder-induced
influence.
7 Limitations
This work does not solve causal attribution in observational MMM. CIG and AR-CIG evaluate a trained de-
coder’s perturbation sensitivity; they are not interventional causal estimands without additional assumptions
such as adequate temporal variation, measured confounding, stable response mechanisms, and plausible in-
tervention support. Real marketing systems may contain hidden confounders, nonstationary platform shocks,
correlated budget rules, delayed effects, and campaign-level constraints that are not fully represented by the
synthetic generator.
13

The most important method limitation is exposed by our own experiments. The learned DICE posterior
contains graph-recovery signal, but current graph interfaces do not reliably turn that signal into sparse
decoder-consumable attribution support. Raw and hard interfaces become dense. Validation-MSE support
selection fails. Stability selection remains weak. Even true-density top-kgives only modest AR-CIG in the
new sparse-target benchmark. A deployable attribution method needs label-free support selection or training
objectives that directly improve calibrated sparse target-relevant graph support.
The baseline set is also intentionally focused. We compare to CausalMMM because it is the closest graph-
MMM architecture and shares the graph-VAE interface. Broader temporal causal discovery baselines such
as PCMCI, DYNOTEARS, and Neural Granger methods are relevant for graph recovery but do not by
themselves test graph-mediated decoder attribution. Future work should include those baselines for graph
recovery while preserving the decoder-bypass diagnostics introduced here.
Finally, the synthetic design provides known graphs but cannot exhaust real MMM behavior. The sparse-
target benchmark removes the original target-parent degeneracy, but future studies should include richer
mediated effects, budget constraints, paired generator counterfactuals, mROI ranking, budget-regret metrics,
reversed-graph controls, degree-preserving random graphs, and out-of-distribution perturbation checks.
8 Conclusion
Our experiments show that attribution bypass is not merely a theoretical concern. In sparse-target MMM
benchmarks, no-graph and full-graph decoders achieve nearly identical forecasting error to oracle-graph
decoders, yet their AR-CIG alignment is near chance. Oracle graph support yields high AR-CIG, and
frozen graph-swap shows that the same decoder can produce graph-aligned influence when supplied with
the correct graph. Thus, the diagnostic and graph-safe decoder are functional. However, learned graph
interfaces, including validation-MSE sparsification and stability selection, remain insufficient. This localizes
the remaining challenge to deployable graph-support selection rather than forecasting or decoder capacity.
The paper’s claim is therefore deliberately bounded. DICE-MMM is not presented as a final causal attri-
bution engine. It is a diagnostic framework for exposing and localizing attribution bypass in graph-based
neural MMM. Its main scientific value is to prevent low forecasting error from being mistaken for attribution
faithfulness.
Reproducibility Statement
All main results are reported as mean±standard deviation over pre-specified seeds. We use the same
generated datasets, splits, and evaluation protocol across methods. The graph convention isA ij = 1
when sourceiinfluences receiverj; self-links are excluded from graph recovery and AR-CIG edge rank-
ings. Graph-recovery sweeps follow theR/d/Tsettings in Table 2. The original response-diagnostic setting
usesR= 10,d= 10,T= 120with 11 nodes including the target node. The sparse-target benchmark uses
a non-degenerate target-parent structure. Stage-1 graph checkpoints are selected by validation graph diag-
nostics or the same late-window rule; Stage-2 decoder checkpoints are selected by validation target-horizon
MSE. Graph-swap experiments freeze decoder weights and change only the graph input. CIG/AR-CIG per-
turbations use source replacement modes described in Section 3.4, with AR-CIG as the main attribution
diagnostic. All experiments were conducted using two NVIDIA GeForce RTX 3090 Ti GPUs.
Acknowledgments
This work was conducted while Yunbo Wang was an intern at Adsgency AI.
References
Thomas Bailie, S. Karthik Mukkavilli, Varvara Vetrova, and Yun Sing Koh. Hierarchical graph networks for
accurate weather forecasting via lightweight training, 2025. URLhttps://arxiv.org/abs/2510.22094.
14

Neil H. Borden. The concept of the marketing mix.Journal of Advertising Research, 1964. URLhttps:
//api.semanticscholar.org/CorpusID:155259223.
Juntao Fang, Shifeng Xie, Shengbin Nie, Yuhui Ling, Yuming Liu, Zijian Li, Keli Zhang, Lujia Pan, Themis
Palpanas, and Ruichu Cai. Rethinking zero-shot time series classification: From task-specific classifiers to
in-context inference, 2026. URLhttps://arxiv.org/abs/2602.00620.
Chang Gong, Di Yao, Lei Zhang, Sheng Chen, Wenbin Li, Yueyang Su, and Jingping Bi. Causalmmm:
Learning causal structure for marketing mix modeling. InProceedings of the 17th ACM International
Conference on Web Search and Data Mining, WSDM ’24, pages 238–246. ACM, March 2024. doi: 10.
1145/3616855.3635766. URLhttp://dx.doi.org/10.1145/3616855.3635766.
C. W. J. Granger. Investigating causal relations by econometric models and cross-spectral methods.Econo-
metrica, 37(3):424–438, 1969. ISSN 00129682, 14680262. URLhttp://www.jstor.org/stable/1912791.
Praveen Gujar, Gunjan Paliwal, Sriram Panyam, and Chhaya Kewalramani. The evolution of ads mar-
keting mix modeling (mmm): From regression models to ai-powered planning for smbs.2024 IEEE
Technology and Engineering Management Society (TEMSCON LATAM), pages 1–6, 2024. URLhttps:
//api.semanticscholar.org/CorpusID:273592420.
Sarthak Jain and Byron C. Wallace. Attention is not explanation, 2019. URLhttps://arxiv.org/abs/
1902.10186.
Yuxue Jin, Yueqing Wang, Yunting Sun, David Chan, and Jim Koehler. Bayesian methods for media mix
modeling with carryover and shape effects. Technical report, Google Inc., 2017.
Deqian Kong, Minglu Zhao, Dehong Xu, Bo Pang, Shu Wang, Edouardo Honig, Zhangzhang Si, Chuan Li,
Jianwen Xie, Sirui Xie, and Ying Nian Wu. Latent thought models with variational bayes inference-time
computation, 2025. URLhttps://arxiv.org/abs/2502.01567.
Thomas Mulc, Mike Anderson, Paul Cubre, Huikun Zhang, Ivy Liu, and Saket Kumar. Nnn: Next-generation
neural networks for marketing measurement, 2025. URLhttps://arxiv.org/abs/2504.06212.
Roxana Pamfil, Nisara Sriwattanaworachai, Shaan Desai, Philip Pilgerstorfer, Paul Beaumont, Konstantinos
Georgatzis, and Bryon Aragam. Dynotears: Structure learning from time-series data, 2020. URLhttps:
//arxiv.org/abs/2002.00498.
Jakob Runge, Peer Nowack, Marlene Kretschmer, Seth Flaxman, and Dino Sejdinovic. Detecting and quanti-
fying causal associations in large nonlinear time series datasets.Science Advances, 5(11), November 2019.
ISSN 2375-2548. doi: 10.1126/sciadv.aau4996. URLhttp://dx.doi.org/10.1126/sciadv.aau4996.
Alex Tank, Ian Covert, Nicholas Foti, Ali Shojaie, and Emily B Fox. Neural granger causality.IEEE
Transactions on Pattern Analysis and Machine Intelligence, pages 1–1, 2021. ISSN 1939-3539. doi:
10.1109/tpami.2021.3065601. URLhttp://dx.doi.org/10.1109/TPAMI.2021.3065601.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser,
and Illia Polosukhin. Attention is all you need, 2023. URLhttps://arxiv.org/abs/1706.03762.
15
