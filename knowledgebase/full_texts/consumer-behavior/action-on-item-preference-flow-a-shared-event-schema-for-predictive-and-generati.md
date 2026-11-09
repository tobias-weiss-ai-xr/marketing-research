---
title: 'Action-On-Item Preference Flow: A Shared Event Schema for Predictive and Generative Personalization'
url: https://arxiv.org/abs/2610.01375
category: consumer-behavior
subcategory: empirical
date: 2026-10
venue: arXiv (Cornell University)
authors:
- Parthiv Chatterjee
- Kashish Kanjaria
- Vashisth Purani
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.01375
pages: 55
chars: 159038
fetched_at: '2026-11-08T13:16:49+00:00'
kb_version: 1
---

# Action-On-Item Preference Flow: A Shared Event Schema for Predictive and Generative Personalization

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Action-On-Item Preference Flow: A Shared Event Schema for
Predictive and Generative Personalization
Parthiv Chatterjee 1 Kashish Kanjaria 1 Vashisth Purani 2
Sourish Dasgupta 1 Tanmoy Chakraborty3
1 KDM Lab, Dhirubhai Ambani University 2 Dhirubhai Ambani University
3 LCS2 Lab, Indian Institute of Technology Delhi
DHIRUBHAI AMBANI UNIVERSITY
 INDIAN INSTITUTE OF TECHNOLOGY DELHI
Version note. This author-prepared archival manuscript presents work accepted to NeurIPS 2026. The discussion and interpretation
are expanded in this version; the research content, tables, and reported results are preserved from the accepted manuscript source.
ABSTRACT
A user’s movie, news, and dialogue histories differ in their native actions and outputs, yet each interaction supplies
evidence that can update user memory. We study whether these histories can train one reusable update mechanism. An
action-on-item schema pairs a mapped interaction role with a content embedding, allowing shared update parameters to
operate on separate user states. We establish invariance to native relabeling, bounded state changes under item-embedding
perturbations, and a pooled-training bound under explicit compatibility conditions. The Multi-Timescale State Hypothesis
(MTSH) specifies how this evidence enters, persists, and is consumed;PerTIDE implements it with action gating, three state-
space traces, fusion, and command-conditioned readout. On PENS, the same history encoder supports both next-news
prediction and personalized headline generation. In a controlled PENS-to-MovieLens experiment, a frozen source-trained
core exceeds an identically structured random core by 15.23 MRR points after fitting the same target consumer. On MIND,
PerTIDE retains a 4.12-point MRR advantage over a same-input three-branch state-space control. Action, readout, and
trace interventions identify complementary contributions to these gains. Together, the theory and experiments support
learning history updates across compatible sources and reusing them through predictive and generative consumers.
1 Introduction
Personalization systems use a user’s interaction history to recommend or generate content. A user may
watch or skip movies, click or ignore news, request headlines or summaries, or respond in dialogue. These
behaviors differ in their action vocabularies, item types, temporal structures, and downstream objectives. Each
interaction nevertheless provides evidence about an evolving user and can change what the system retains.
We study whether their common form, an action on an item, allows one history encoder to learn from diverse
trajectories and reuse its learned updates across predictive and generative tasks.
Suppose Alice watches a political thriller and a television series with similar themes, while Bob watches
the series but skips the film. A common encoder can learn how an action modulates the content written
to memory, how that evidence persists, and how a later task uses it. Alice and Bob share these operations,
while their histories determine separate states. At a fixed timestep, holding the history, action, and command
constant lets us ask a precise question: how much does the update change when the film is replaced by a
similar series or by unrelated content?
1
arXiv:2610.01375v1  [cs.LG]  1 Oct 2026

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Prior work provides several forms of sharing. P5 and NEO express multiple recommendation or user-
understanding tasks through a common language interface (Geng et al., 2022; De Nadai et al., 2026). UniSRec
and RecGURU learn transferable item or sequence representations (Hou et al., 2022; Li et al., 2022), and LaMP
and Persona-Plug condition generation on retrieved histories or user embeddings (Salemi et al., 2024; Liu
et al., 2025). These capabilities establish reuse at the task or representation level. Successful reuse at those
levels alone does not establish how an evolving state responds to controlled changes in an individual action or
item. We examine that response, its formal stability, and whether the learned update operations remain useful
through different consumers.
Using the action-on-item interface of the user interaction graph (UIG) (Chatterjee et al., 2025), we map
native interactions to action roles and content embeddings. This abstraction enables one update mechanism to
learn from different native histories. It has three precise properties: identical mapped events induce identical
state evolution from equal initial states and commands; small item-embedding changes produce bounded
state changes under stability and readout conditions; and compatible domains admit a pooled-training bound
with explicit distribution and label-semantic discrepancies. An item can therefore change category without
requiring a new update rule: its role and content representation determine how it enters the shared mechanism.
The stability result describes that response in the supplied embedding geometry, while the pooling result
specifies when evidence from different sources can support learning together.
We formulate the Multi-Timescale State Hypothesis (MTSH) to separate what enters memory, how it
persists, and how a task uses the retained history. PerTIDE (Personalization via multi-Timescale Interaction
Drift Encoder) first applies a learned action gate to the item embedding. Three state-space traces retain
the resulting evidence with long-term, short-term, and episodic biases. Adaptive fusion combines their
contributions, with a residual path carrying the current event directly. A command-conditioned readout then
forms a task-ready user representation for a predictive head or a prefix-conditioned text decoder. Sharing these
operations lets the encoder learn from pooled event trajectories while each user maintains a history-specific
state. The traces provide different retention choices for the same evidence; their combinations are tested
through temporal probes and ablations.
The results identify both reusable learning and the contributions of its components. On PENS, the same
history encoder supports next-news prediction and personalized headline generation. In a controlled PENS-to-
MovieLens experiment, a frozen source-trained core exceeds an identically structured random core by 15.23
MRR points after fitting the same target consumer. Source training therefore supplies useful structure that
target-head fitting alone does not recover from the random core; the low score with an untrained consumer
locates the consumer’s role in accessing that structure. On MIND,PerTIDE retains a 4.12-point MRR advantage
over a same-input three-branch SSM control, supporting the additional retention design. The trace ablations
reveal why isolated strength is insufficient for judging a component: E alone reaches only 24.18 MRR, while
adding E to L+S raises MRR from 41.26 to 46.65. The same addition raises PENS PSE-METEOR from 0.182 to
0.355. A weak isolated trace can thus provide useful complementary evidence to the fused state.
Contributions. We make three contributions. (i) A formal account of history-update reuse establishes native-
label invariance, item-embedding stability, and compatible pooled learning on the existing action-on-item
interface. (ii) MTSH and its PerTIDE implementation organize action-dependent entry, complementary retention,
fusion, and command-conditioned consumption into a shared encoder. (iii) Controlled evidence of learned reuse
connects predictive and generative consumers, source-frozen domain transfer, same-input comparisons, and
mechanism interventions. Together, these contributions explain what is shared, how the shared operations are
realized, and where the reported evidence supports their usefulness.
2 Related Work
Sharing tasks and representations. P5 unifies recommendation tasks through language modeling, and NEO
combines recommendation, search, and user understanding through language-steered generation (Geng
et al., 2022; De Nadai et al., 2026). Multi-behavior and multi-task methods share parameters or objectives
across related signals (Gao et al., 2019; Ma et al., 2018). RecGURU aligns user representations adversarially,
UniSRec transfers item and sequence representations, and GenCDR combines universal and domain-specific
representations (Li et al., 2022; Hou et al., 2022; Hu et al., 2026). We build on this established reuse. Our
question concerns the action-dependent update applied to each event, its stability under item substitution,
and the retention and readout operations learned on the common interface. UniSRec and RecGURU provide
direct empirical comparisons for transfer.
Temporal history encoders.News and sequential recommendation use profile pooling, recurrence, attention,
2

KDM LAB / LCS2 RESEARCH MANUSCRIPT
and state-space models (Wu et al., 2019a; Okura et al., 2017; Wu et al., 2019b; Hidasi et al., 2016; Sun et al., 2019;
Liu et al., 2024). Long/short-term models, time-aware attention, and multi-interest encoders already represent
persistent interests and recent intent (An et al., 2019; Yu et al., 2019; Li et al., 2020; Cen et al., 2020). PRIME and
Reflective Memory Management organize episodic, semantic, or dialogue memory, while generalized user
representations aggregate behavior across temporal windows (Zhang et al., 2025; Tan et al., 2025; Fazelnia et al.,
2025). Building on temporal modeling, MTSH separates event entry, persistence, fusion, and task consumption
on one action-on-item interface; a same-input three-branch control tests the additional value of its retention
parameterization.
Personalized generation and event construction. Generation can use retrieved profile evidence, compact
user embeddings, or user-specific parameters, as in LaMP , Persona-Plug, and OPPU (Salemi et al., 2024; Liu
et al., 2025; Tan et al., 2024). PENS and GTP study personalized news generation (Ao et al., 2021; Song et al.,
2023). UIG and PerAugy supply the event representation and trajectory augmentation used here (Chatterjee
et al., 2025); they are precursors to the present encoder. PerTIDE learns shared update parameters and supplies
a command-adapted history state to predictive heads or a prefix-conditioned decoder. Reusing that learned
core is evaluated separately from training a consumer for a new output space.
3 Action-On-Item Preference Flow
3.1 A Shared Event Interface
For dataset D, a deterministic mapping ρD assigns native interactions to positive, negative, request, or
generated-response transitions. The last two distinguish the sides of a command-like interaction. Each event
is b(t) u = ⟨a(t), tl(t)⟩, where a(t) is the mapped role and tl(t) is the item or response acted upon. Its embedding
e(t) tl ∈ Rd supplies the continuous content representation. The concrete task is specified separately by command
seed gq. Roles are supplied by preprocessing; the encoder learns how each role modulates content.
UIG represents these events as action-labeled edges among user, content, and response nodes (Chatterjee
et al., 2025). A user’s ordered path gives a trajectory τu, consumed as a sequence of compact interaction
blocks. Explicit clicks and non-clicks map directly to roles; ratings and dialogue stance require derived labels.
Appendix B.1 records those construction rules and their different provenance.
What remains shared when the item changes? Fix Alice’s history, watch action, command, and current
timestep. Replace the current movie first by a similar movie, then by a series, and finally by unrelated content.
The update consumes the role and embedding, rather than the native item type. For equal initial states and
commands, identical mapped trajectories give identical states (Appendix B.2, Proposition B.1). For the trace
update mr t = Armr t−1 + B[µ(at) ⊙ et], replacing only that item changes its contribution at a later lag k by at
most
∥∆mr t+k∥2 ≤ ∥B∥2βk r ∥et − e′ t∥2, ∥Ar∥2 ≤ βr < 1, (1)
when subsequent inputs agree. The complete-state bound additionally accounts for fusion, the current-input
residual, and recurrent readout (Appendix B.2, Proposition B.2). Thus a similar item can inherit a similar
update without a hand-built taxonomy of movies, series, and other content. For fixed history, action, and
command, halving the embedding perturbation halves this upper bound. A movie-to-series replacement uses
the same operations as a movie-to-movie replacement; embedding distance governs the guarantee. More
distant items permit a larger change without forcing one.
Why pool different trajectories? Alice’s movie and series histories, and Bob’s histories, train the same
role-conditioned update parameters while maintaining separate user states. The pooled-training result in
Appendix B.2 decomposes target risk into pooled empirical risk, an estimation term, schema-distribution
distance, and a discrepancy in labels or command semantics. When distributions and labels are compatible,
examples from every participating domain contribute to the estimation bound for one shared update rule.
The explicit mismatch terms identify what must remain comparable for that gain to carry to a target domain.
Under matching schema distributions and conditional label semantics, a common model-class complexity
bound C/√n yields an estimation allowance that scales with 1/ √ N for N independent pooled examples
(Corollary B.5). Compatible histories can therefore contribute to estimating the shared rule even when they
come from another native domain.
From History States To Preference Flow. Profile aggregation (PAH) discards order, Markovian drift (MDH)
carries the prefix through a recurrent state, and long-horizon dynamics (LDH) models learned dependencies
over earlier events. These are overlapping design families, not mutually exclusive laws of user behavior. The
3

KDM LAB / LCS2 RESEARCH MANUSCRIPT
action-on-item interface poses a further design question within any family: what should be written, how should it
persist, and how should a task consume it?
3.2 Multi-Timescale State Hypothesis
MTSH retains action-conditioned evidence through complementary temporal traces before task consumption.
Long-term (L), short-term (S), and episodic (E) describe intended slow, recent, and event-related retention.
Their usefulness and differentiation require empirical tests. With entry Ψ, persistence Pr, fusion Φ, routing Π,
and readout G, the implemented decomposition is
b(t) u = Ψ(e(t) tl , a(t)), m(t,r) u = Pr(m(t−1,r) u , b(t) u ),
h(t) u = Φ(m(t,L) u , m(t,S) u , m(t,E) u , b(t) u ),
π(t) u = Π(gq, z(t−1) u ), z(t) u = G(π(t) u , h(t) u ).
(2)
The current event can reach fusion through a residual path, and routing uses the preceding task-ready
state. Section 4 specifies each operator. Sharing these operators leaves both the retained history and its
command-adapted output specific to the user.
4 PerTIDE: Instantiating MTSH
We instantiate MTSH through the four operations in Eq. 2: action-conditioned evidence entry, trace-specific
persistence, adaptive trace fusion, and command-conditioned consumption. We illustrate the architecture in
Figure 1. Each schema-normalized event is converted into action-conditioned evidence, propagated through
long-, short-, and episodic traces, and fused into a user-specific preference-history state. The active command
then converts this user-specific history state into a task-ready representation for a predictive or generative
consumer.
Action entry. We initialize item and response nodes with MPNet embeddings (Song et al., 2020). At timestep
t, the supplied action role a(t) controls how target-locus evidence enters the state:
µ(t) = σ  MLPgate(a(t))  , b(t) u = µ(t) ⊙ e(t) tl . (3)
Here, a(t) comes from the deterministic event mapping in Section 3.1; the learned gate determines how the
supplied role modulates content evidence. A negative-role gate still has nonnegative entries; it does not
automatically subtract the item embedding or impose a monotone dislike score. Thus, a clicked and an ignored
article may share the same content space while contributing differently through their positive and negative
roles. The resulting b(t) u instantiates the evidence-entry operator Ψ in Eq. 2.
Trace persistence. The action-conditioned event enters three lag-biased state-space model (SSM) traces.
The implementation shares an orthogonal eigenbasis Q across traces and uses diagonal real spectra Λr. The
transition matrices are defined by the following maps, with QL = QS = QE = Q and Q−1 = Q⊤:
m(t,L) u = QL exp(δΛL)Q−1 L m(t−1,L) u + Bb(t) u ,
m(t,S) u = QSσ(−κΛS)Q−1 S m(t−1,S) u + Bb(t) u ,
m(t,E) u = QE(I + ηΛE)Q−1 E m(t−1,E) u + Bb(t) u .
(4)
For the generic recurrence m(t,r) u = Arm(t−1,r) u + Bb(t) u , unrolling yields the lag response Kr(∆) =A∆ r . A modal
base a assigns weight a∆ at lag ∆. Slow and fast bases yield different retention, while event inputs leave
decaying tails. The three formulas permit overlapping kernels; their names describe intended biases rather
than guaranteeing an ordering or semantic partition. These kernels instantiate the persistence operators Pr in
Eq. 2.
Trace fusion. The updated long-, short-, and episodic traces are adaptively fused into the preference-history
state through
h(t) u = MLPΦ([m(t,L) u ; m(t,S) u ; m(t,E) u ]) +Wψb(t) u + bψ. (5)
The residual supplies the current event directly without adding another recurrent trace. This realizes the
fusion operator Φ in Eq. 2. See Appendix D.1-D.3 for stability conditions, modal responses, and the kernel
derivations.
4

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Figure 1: PerTIDE pipeline: a user’s UIG trajectory is mapped to action-gated b-cells and encoded by a
tri-trace SSM with an adaptive memory mixer; a command-conditioned readout produces a task-ready state
that conditions task-specific heads for prediction (MLP) and generation (DistilGPT2 decoder). The equations in
Section 4 additionally specify the shared eigenbasis, current-event residual, and routing through the preceding
task-ready state.
Command consumption. The fused state h(t) u represents the user’s preference history before resolving the
concrete downstream operation. Given task seed gq, a supervised command classifier uses the preceding
task-ready state as routing context and estimates
π(t) u = SoftMax  Wtask[z(t−1) u ; gq]  . (6)
The corresponding task-ready state is
z(t) u = (Wππ(t) u ) ⊙ h(t) u + bG. (7)
Thus, h(t) u is the user-specific history state learned under the shared event schema, while z(t) u resolves how that
state is consumed for the active task. The same news history can therefore support next-news prediction or
headline generation, while the command seed and downstream consumer determine the required task-ready
representation. This instantiates G ◦ Π in Eq. 2.
Recurrent user memory. The encoder retains three 768-dimensional traces and the preceding task-ready
state for each user. These four vectors require 12 KiB in FP32, independent of history length. Each new event
updates this fixed recurrent cache, while the predictive or generative consumer accesses the resulting state.
Appendix J.1 gives the calculation and separates it from model weights and runtime estimates.
Training and heads. We train the shared encoder with temporal-position, next-event, and command-
classification objectives: Lenc = 0.2Lpos + 0.4Lnext + 0.4Ltask. One encoder is trained jointly on the MovieLens,
MIND, PENS, and OpenAI training trajectories after schema construction. The source-only transfer exper-
iments train a separate PENS-only encoder. The three loss weights are globally fixed choices, not learned
optima. Predictive consumers optimize task-specific ranking or classification objectives.
Generative consumers. For generation, we use a pretrained DistilGPT2 decoder conditioned through a
learned prefix. User-fused injection (UFI) combines the predicted query-conditioned representation with the
query-document embedding, while user-gated injection (UGI) additionally uses the task-ready user state to
apply feature-wise affine modulation to the query-conditioned representation before fusion. The resulting
control is combined with query-document evidence and projected to the decoder prefix. During generation
training, the contextualization modules, final two decoder blocks, and final layer normalization are optimized,
while the remaining decoder parameters stay frozen. The generation-specific stage also keeps the history
5

KDM LAB / LCS2 RESEARCH MANUSCRIPT
encoder fixed. Personalization therefore enters through the encoded preference-history state rather than a
user-specific decoder. Architecture and decoder variants are given in Appendix D; objectives, dimensions, and
training are in Appendix E.
5 Evaluation
Datasets and tasks. Table 5 in Appendix A maps the five main settings to their event evidence, consumers,
and metrics. We evaluate naturally ordered predictive histories on MovieLens-1M, MIND (Wu et al., 2020),
and PENS (Ao et al., 2021); PENS also provides personalized headline generation from the same news-
side history abstraction. OpenAI-Reddit is used only as an eventization stress test since it lacks observed
chronology. For OpenAI, native train/evaluation pools are separated before construction, and PerAugy is
applied independently within both pools. PENS surrogate responses and augmentation are used in training;
MIND uses its native interaction histories without that surrogate construction. MPChat is tested as a boundary
case where event roles must be inferred from dialogue/discourse.
Task-specific baselines. Task-native baselines cover PAH, MDH, and LDH families, including NAML,
PLM-NR, EBNR (GRU), NRMS, MINER, SASRec, BERT4Rec, Mamba4Rec, and other dataset-standard systems.
Prompted instruction-tuned LLMs provide a fixed-parameter functional alternative for generation. To separate
input construction from state design, we additionally evaluate schema-matched MeanPool-B, MaxPool-
B, GRU-B, LSTM-B, D-FM-Attention-B, Discretized-SSM-B, and Tri-SSM-B controls on the same ordered
interaction-block trajectories as PerTIDE. Tri-SSM-B further matches the three-branch organization while
omitting the explicit L/S/E retention maps. These MIND controls hold the input representation fixed;
task-native comparisons may use their original input constructions.
Transfer stress-test baselines. For the source-only reuse stress test, we train on PENS and withhold Movie-
Lens from source-encoder training. We compare PerTIDE with two methods explicitly designed for transfer:
UniSRec (Hou et al., 2022) and RecGURU (Li et al., 2022). Each method uses the same PENS/MovieLens
content-embedding interface and receives either 500 or 3,000 MovieLens trajectories for target-side alignment.
The evaluation uses the same held-out MovieLens protocol.
Metrics and protocol. Predictive settings use one positive target and 699 sampled negatives and report MRR,
nDCG, and HR@10. Generation uses PerSEval (Dasgupta et al., 2024) (PSE-JSD, PSE-SU4, PSE-METEOR),
together with reference-based content metrics and human ratings of headline similarity (Appendices I and K).
These evaluate agreement with references, rather than directly measuring article factuality. Main comparisons
use paired bootstrap evaluation with 10,000 resamples; robustness studies keep trajectories and candidate
sets fixed so only the perturbed factor changes. Full dataset, preprocessing, hyperparameter, statistical, and
evaluation details are in Appendices A–E.
6 Results And Analysis
6.1 RQ1: Can The Shared Encoder Serve Prediction And Generation?
Across the five main settings in Table 1, PerTIDE improves the reported primary metrics over the listed
task-native comparators. MovieLens gains are 2.36/3.47 MRR/nDCG points over SSD4Rec; MIND gains are
10.05/9.01 over MINER; and PENS prediction gains are 0.90/1.42 over LSTUR. On PENS, the same history
encoder also supports headline generation through a different consumer. UGI reaches 0.366/0.341/0.355
PSE-JSD/PSE-SU4/PSE-METEOR, compared with 0.263/0.125/0.174 for the strongest listed two-shot LLM,
DeepSeek-R1-Distill-Qwen-32B. These complete-system gains use trained contextualization and partial de-
coder tuning for PerTIDE and two-shot prompting for the LLM. OpenAI’s gains concern constructed trajecto-
ries; dialogue boundary results and metric-specific exceptions are reported in Appendix J.
Generation With Sparse Positive Evidence. The encoder retains an advantage when fewer positive events
are available. On the click-only sparse subset, PerTIDE achieves 0.211/0.244/0.262 PSE-JSD/PSE-SU4/PSE-
METEOR, compared with 0.152/0.087/0.092 for the prompted DeepSeek-R1-32B baseline (Appendix J.5.5).
The SU4 and METEOR drops are 28.45% and 26.2%, versus 30.4% and 47.2% for that baseline. JSD falls by
about 42% for both systems. Thus the advantage persists with limited positive evidence, with stronger relative
retention on two personalization metrics. The result concerns this sparse subset and does not isolate which
trace supplies the retained benefit.
6

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Table 1: One encoder supports prediction and generation. Predictive scores are MRR/nDCG (0–100), with
nDCG@5 for MIND and nDCG@10 for MovieLens and PENS; generative scores are PSE-JSD/PSE-METEOR
(0–1). Each row uses its strongest listed task-native comparator. Full scores appear in Appendix J.2, Tables 13–
15; Appendix J.4, Table 18; and Appendix J.5.4, Table 23. Table 2 gives the same-input controls.
Setting Comparator Baseline PerTIDE Gain
MovieLens-1M
movie ranking
SSD4Rec 14.95 / 20.31 17.31 / 23.78 +2.36 / +3.47
MIND news ranking MINER 36.60 / 40.20 46.65 / 49.21 +10.05 / +9.01
PENS next-news
ranking
LSTUR 9.04 / 10.16 9.94 / 11.58 +0.90 / +1.42
PENS headline gen-
eration
DeepSeek-R1-32B (2-shot) 0.263 / 0.174 0.366 / 0.355 +0.103 / +0.181
OpenAI-Reddit
TL;DR generation
DeepSeek-14B (2-shot) 0.243 / 0.109 0.285 / 0.294 +0.042 / +0.185
Table 2: Same-input state-model control on MIND. All “-B” controls consume the same ordered schema-
normalized interaction-block embeddings as PerTIDE. Tri-SSM-B provides a structurally matched three-branch
SSM control without the explicit long-, short-, and episodic retention maps used by PerTIDE. Full task-native
results appear in Appendix J.2.2, Table 14.
State family Model MRR nDCG@5 HR@10
PAH MeanPool-B 29.43 31.22 33.17
PAH MaxPool-B 28.32 31.16 32.41
MDH GRU-B 32.64 35.17 37.92
MDH LSTM-B 32.17 34.92 37.05
LDH D-FM Attention-B 32.17 34.56 36.21
LDH Discretized SSM-B 35.14 38.53 37.27
LDH Tri-SSM-B 42.53 43.84 46.33
MTSH PerTIDE 46.65 49.21 55.48
6.2 RQ2: Do Entry, Retention, And Readout Explain The Gains?
Holding the input and branch count fixed. In the MIND comparison, a single Discretized-SSM-B reaches 35.14
MRR and three ordinary SSM branches reach 42.53. PerTIDE reaches 46.65, adding 4.12 MRR, 5.37 nDCG@5,
and 9.15 HR@10 points over Tri-SSM-B (Table 2). The advantage survives both common input construction
and a three-branch control, supporting the additional retention parameterization in this setting.
Action-dependent entry and command-dependent readout. Removing action conditioning reduces MIND
MRR/HR@10 from 46.65/55.48 to 40.13/46.35; removing command-conditioned readout gives 42.51/51.06.
These interventions locate useful contributions at two different stages of the update. A separate fixed-trajectory
role-corruption experiment progressively flips positive and negative labels: MRR falls from 12.14 to 10.13, 9.17,
7.71, and 2.81 at 0%, 10%, 25%, 50%, and 100% corruption (Appendix J, Table 21). Correct action roles therefore
carry predictive information that the encoder uses (Figure 2a).
Retention behavior and complementary traces. Target-fixed probes alter where preference-similar evidence
occurs (Appendix J.3, Table 16). L-Tr retains the top 75% of history nodes ranked by embedding proximity to
the target in their original order; S-Tr concentrates such evidence in the final 30%; E-Tr inserts a consistent
3–4-step burst among unrelated content. On MIND, each isolated trace is strongest in its corresponding
regime: L obtains 49.54/54.78 on L-Tr, S obtains 50.07/55.35 on S-Tr, and E obtains 50.35/55.84 on E-Tr in
MRR/nDCG@10. MovieLens has an exception: L slightly exceeds S on S-Tr, 27.18/29.35 versus 27.13/29.22.
The fused state leads every reported probe, including the setting where isolated specialization overlaps.
Natural-task ablations further separate isolated strength from contribution to a combination (Appendix J,
7

KDM LAB / LCS2 RESEARCH MANUSCRIPT
(a) PENS Role Corruption
0
4
8
12
0 25 50 75 100
12.14
2.81
MRR
Corrupted roles (%)
(b) MIND Trace Subsets
0
10
20
30
40
50
24.18
41.26
46.65
E L+S L+S+E
MRR
Retained traces
(c) PENS Trace Subsets
0
0.1
0.2
0.3
0.4
0.045
0.182
0.355
E L+S L+S+E
PSE-METEOR
Retained traces
Figure 2: Correct action roles and complementary traces improve personalization. (a) On fixed PENS
trajectories, targets, and candidates, only positive/negative roles change. (b,c) The episodic trace is weak
alone, yet adding it to L+S improves MIND MRR by 5.39 points and PENS PSE-METEOR by 0.173. The panels
use separate protocols and metric scales. Full interventions are in Tables 21 and 17.
Table 17). On MIND, E alone reaches only 24.18 MRR, yet adding E to L+S raises MRR from 41.26 to 46.65.
On PENS generation, the same addition raises PSE-METEOR from 0.182 to 0.355. The full model benefits
from the episodic contribution even though E is weak alone (Figure 2b,c); the appendix also reports smaller
combinations that hurt performance.
6.3 RQ3: Do Learned Updates Survive A New Consumer Or Domain?
One history, different consumers. PENS prediction reaches 9.94/11.58 MRR/nDCG@10, while the same
encoded news histories condition personalized headlines. UGI improves on UFI by 0.034/0.052/0.052 in
the three PSE metrics (Appendix D.5; Table 18). The state is reusable across the evaluated objectives, and its
decoder conditioning still affects how effectively generation uses it.
Source-trained reuse with target alignment. A PENS-only encoder, trained with MovieLens excluded, is
aligned using either 500 or 3,000 target trajectories. Against the strongest transfer baseline at each budget,
gains are 0.15/0.21/1.47 and 1.43/2.98/5.26 MRR/nDCG@10/HR@10 points, respectively (Table 3). More
target alignment substantially improves all three methods. A fitted consumer thus makes source-trained
updates useful in the new output space.
Table 3: PENS-trained state reuse with target alignment. MovieLens is withheld from source-encoder training.
Methods receive the same target budget and one-positive/699-negative protocol. Scores use the 0–100 scale.
The frozen-core control in Table 4 uses a different slice, so absolute scores should be compared within each
table.
500 Target Trajectories 3K Target Trajectories
Method MRR nDCG@10 HR@10 MRR nDCG@10 HR@10
UniSRec 4.31 3.79 8.23 15.18 16.92 33.49
RecGURU 6.03 5.73 11.49 14.21 16.17 29.44
PerTIDE 6.18 5.94 12.96 16.61 19.90 38.75
8

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Table 4: Learned updates survive frozen-core transfer.
PENS→MovieLens with PerTIDE cores and the same head
architecture. Trained heads use 3K target rows and matched
candidates, loss, and optimization. Scores use the 0–100 scale.
Table 3 gives the separate transfer-baseline comparison.
Frozen core Head MRR
nDCG
@10 HR@10
Random Trained 1.115 0.780 1.44
PENS-trained Untrained 1.371 0.960 2.18
PENS-trained Trained 16.344 16.002 20.28
Separating learned updates from
an adaptable random representation.
The controlled frozen-core experiment
fixes the MovieLens head, 3,000 tar-
get rows, negatives, loss, and optimiza-
tion. A frozen PENS-trained core with
the trained head reaches 16.344 MRR;
a frozen random core with the same
trained head reaches 1.115; and the
learned core with an untrained head
reaches 1.371 (Table 4). The 15.23-
point advantage isolates information
learned in the source encoder, while the
untrained-head result exposes the need for target alignment. This protocol is separate from the transfer-baseline
comparison, so their absolute scores should not be combined.
Schema Proximity And Transfer. Nearby schema representations are associated with easier transfer in the
separate diagnostic on 500 MovieLens trajectories from 99 users. Schema distance has Spearman correlations of
0.11 and 0.16 with frozen and adapted target risk, and −0.09 and −0.11 with reciprocal-rank gain, respectively.
All four user-clustered 95% confidence intervals exclude zero (Appendix J.5.1, Table 20). The directions connect
schema proximity to lower risk and greater benefit from reuse. The associations are modest and do not
establish that the theorem’s stability or conditional-label assumptions hold in these runs.
7 Discussion And Limitations
The reusable object is the learned history update: different users retain separate states, and aligned consumers
access those states for prediction or generation. The frozen-core comparison demonstrates useful source
learning, while same-input controls locate an advantage beyond schema construction and parallel branches.
On PENS, reference-content agreement also improves over DeepSeek-32B on RG-SU4 (41.32 versus 29.42)
and BLEU-4 (27.64 versus 19.31). Human similarity ratings are 3.21 versus 3.12 on a six-point scale, while
BERTScore is slightly lower, 90.84 versus 90.87 (Appendix J.4.2). These findings support reference agreement
rather than article factuality.
This reuse depends on supplied action mappings, informative content embeddings, and compatible down-
stream semantics. OpenAI evaluates constructed chronology, and MPChat combines useful generation results
with deficits in response prediction and speaker identification (Appendix J.6). Stable traces and the three
branch names alone do not certify readout contraction or semantic disentanglement. The objectives use glob-
ally fixed weights, and reported resource figures are estimates rather than matched hardware measurements.
Uncertainty-aware action mappings, richer discourse representations, and adaptive objective weighting are
concrete extensions of the current design.
8 Conclusion
Heterogeneous personalization histories can teach a common way to update user memory when their in-
teractions are represented as actions on embedded items. The schema gives an exact invariance property, a
conditional continuity bound under item changes, and a pooled-training bound that makes compatibility
explicit. MTSH specifies how this evidence enters, persists, and is consumed, and PerTIDE implements those
operations in a shared encoder. Prediction and generation results demonstrate multiple uses of the learned
history state; the controlled frozen-core experiment provides direct evidence that source-trained updates
remain useful after a domain change and consumer alignment. Same-input controls and trace interventions
connect that reuse to the proposed update structure. The resulting opportunity is to learn history updates
across compatible data sources and reuse them through task-appropriate consumers.
9

KDM LAB / LCS2 RESEARCH MANUSCRIPT
AI Use Statement
Generative AI tools were used to cross-check technical reasoning, assist with literature retrieval, mathematical
exposition and verification, manuscript drafting and editing, and code cleaning/documentation. The authors
determine the research questions, experimental decisions, scientific claims, and final interpretations, and retain
responsibility for the veracity, originality, and integrity of the paper.
References
Jaewoo Ahn, Yeda Song, Sangdoo Yun, and Gunhee Kim. MPCHAT: Towards multimodal persona-grounded
conversation. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume
1: Long Papers), pages 3354–3377, Toronto, Canada, July 2023. Association for Computational Linguistics.
doi: 10.18653/v1/2023.acl-long.189. URL https://aclanthology.org/2023.acl-long.189/.
Mingxiao An, Fangzhao Wu, Chuhan Wu, Kun Zhang, Zheng Liu, and Xing Xie. Neural news recommendation
with long- and short-term user representations. In Anna Korhonen, David Traum, and Lluís Màrquez,
editors, Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, pages 336–345,
Florence, Italy, July 2019. Association for Computational Linguistics. doi: 10.18653/v1/P19-1033. URL
https://aclanthology.org/P19-1033/.
Xiang Ao, Xiting Wang, Ling Luo, Ying Qiao, Qing He, and Xing Xie. PENS: A dataset and generic framework
for personalized news headline generation. In Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli,
editors, Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th
International Joint Conference on Natural Language Processing (Volume 1: Long Papers) , pages 82–92, Online,
August 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.acl-long.7. URL
https://aclanthology.org/2021.acl-long.7/.
Pengshan Cai, Kaiqiang Song, Sangwoo Cho, Hongwei Wang, Xiaoyang Wang, Hong Yu, Fei Liu, and Dong
Yu. Generating user-engaging news headlines. In Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki,
editors, Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), pages 3265–3280, Toronto, Canada, July 2023. Association for Computational Linguistics. doi:
10.18653/v1/2023.acl-long.183. URL https://aclanthology.org/2023.acl-long.183/.
Yukuo Cen, Jianwei Zhang, Xu Zou, Chang Zhou, Hongxia Yang, and Jie Tang. Controllable multi-interest
framework for recommendation. In Proceedings of the 26th ACM SIGKDD International Conference on Knowledge
Discovery & Data Mining, KDD ’20, page 2942–2951, New York, NY, USA, 2020. Association for Computing
Machinery. ISBN 9781450379984. doi: 10.1145/3394486.3403344. URL https://doi.org/10.1145/3394486.
3403344.
Parthiv Chatterjee, Shivam Sonawane, Amey Hengle, Aditya Tanna, Sourish Dasgupta, and Tanmoy
Chakraborty. Diversity augmentation of dynamic user preference data for boosting personalized text
summarizers. Trans. Mach. Learn. Res., 2025. URL https://openreview.net/forum?id=JVx7Qi8tz3.
Sourish Dasgupta, Ankush Chander, Tanmoy Chakraborty, Parth Borad, and Isha Motiyani. PerSEval:
Assessing personalization in text summarizers. Transactions on Machine Learning Research , 2024. ISSN
2835-8856. URL https://openreview.net/forum?id=yqT7eBz1VJ.
Marco De Nadai, Edoardo D’Amico, Max Lefarov, Alexandre Tamborrino, Divita Vohra, Mark VanMid-
dlesworth, Shawn Lin, Jacqueline Wood, Jan Stypka, Eliza Klyce, Keshi Dai, Matthew N. K. Smith, Timothy
Heath, Martin D. Gould, Yves Raimond, Sandeep Ghael, Tony Jebara, Andreas Damianou, Vladan Ra-
dosavljevic, Paul Bennett, Mounia Lalmas, and Praveen Chandar. A unified model for personalization:
Language-steerable generative recommendation, search, and user understanding. In Proceedings of the 32nd
ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pages 779–790. Association for Computing
Machinery, 2026. doi: 10.1145/3770855.3817955.
Ghazal Fazelnia, Sanket Gupta, Claire Keum, Mark Koh, Timothy Christopher Heath, Guillermo Carrasco
Hernández, Stephen Xie, Nandini Singh, Ian Anderson, Maya Hristakeva, Petter Pehrson Skidén, and
Mounia Lalmas. Generalized user representations for large-scale recommendations and downstream tasks.
In Proceedings of the Nineteenth ACM Conference on Recommender Systems , pages 962–966. Association for
Computing Machinery, 2025. doi: 10.1145/3705328.3748132.
10

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Chen Gao, Xiangnan He, Dahua Gan, Xiangning Chen, Fuli Feng, Yong Li, Tat-Seng Chua, and Depeng Jin.
Neural multi-task recommendation from multi-behavior data. In 2019 IEEE 35th International Conference on
Data Engineering (ICDE), pages 1554–1557, 2019. doi: 10.1109/ICDE.2019.00140.
Shijie Geng, Shuchang Liu, Zuohui Fu, Yingqiang Ge, and Yongfeng Zhang. Recommendation as language
processing (rlp): A unified pretrain, personalized prompt & predict paradigm (p5). In Proceedings of
the 16th ACM Conference on Recommender Systems , 2022. doi: 10.1145/3523227.3546767. URL https:
//arxiv.org/abs/2203.13366.
Balázs Hidasi, Alexandros Karatzoglou, Linas Baltrunas, and Domonkos Tikk. Session-based recommendations
with recurrent neural networks, 2016. URL https://arxiv.org/abs/1511.06939.
Yupeng Hou, Shanlei Mu, Wayne Xin Zhao, Yaliang Li, Bolin Ding, and Ji-Rong Wen. Towards universal
sequence representation learning for recommender systems. In Proceedings of the 28th ACM SIGKDD
Conference on Knowledge Discovery and Data Mining, 2022.
Peiyu Hu, Wayne Lu, and Jia Wang. From ids to semantics: A generative framework for cross-domain
recommendation with adaptive semantic tokenization. In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 40, pages 14874–14882, 2026. doi: 10.1609/aaai.v40i17.38508.
Hugging Face. Distilgpt2. Hugging Face Model Hub, n.d. URL https://huggingface.co/distilbert/dist
ilgpt2. Model card; accessed 13 September 2026.
Wang-Cheng Kang and Julian McAuley. Self-attentive sequential recommendation. In 2018 IEEE International
Conference on Data Mining (ICDM) , pages 197–206, 2018. doi: 10.1109/ICDM.2018.00035. URL https:
//arxiv.org/abs/1808.09781.
Chenglin Li, Mingjun Zhao, Huanming Zhang, Chenyun Yu, Lei Cheng, Guoqiang Shu, Beibei Kong, and
Di Niu. Recguru: Adversarial learning of generalized user representations for cross-domain recommen-
dation. In Proceedings of the Fifteenth ACM International Conference on Web Search and Data Mining , pages
571–581, 2022. doi: 10.1145/3488560.3498388.
Jiacheng Li, Yujie Wang, and Julian McAuley. Time interval aware self-attention for sequential recommendation.
In Proceedings of the 13th International Conference on Web Search and Data Mining, WSDM ’20, page 322–330,
New York, NY, USA, 2020. Association for Computing Machinery. ISBN 9781450368223. doi: 10.1145/3336
191.3371786. URL https://doi.org/10.1145/3336191.3371786.
Zhixuan Lin, Evgenii Nikishin, Xu Owen He, and Aaron Courville. Forgetting transformer: Softmax attention
with a forget gate, 2025. URL https://arxiv.org/abs/2503.02130.
Chengkai Liu, Jianghao Lin, Jianling Wang, Hanzhou Liu, and James Caverlee. Mamba4rec: Towards efficient
sequential recommendation with selective state space models, 2024. URL https://arxiv.org/abs/2403.0
3900.
Jiongnan Liu, Yutao Zhu, Shuting Wang, Xiaochi Wei, Erxue Min, Yu Lu, Shuaiqiang Wang, Dawei Yin, and
Zhicheng Dou. LLMs + persona-plug = personalized LLMs. In Proceedings of the 63rd Annual Meeting
of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 9373–9385, Vienna, Austria,
July 2025. Association for Computational Linguistics. doi: 10.18653/v1/2025.acl-long.461. URL https:
//aclanthology.org/2025.acl-long.461/.
Jiaqi Ma, Zhe Zhao, Xinyang Yi, Jilin Chen, Lichan Hong, and Ed H. Chi. Modeling task relationships in
multi-task learning with multi-gate mixture-of-experts. In Proceedings of the 24th ACM SIGKDD International
Conference on Knowledge Discovery & Data Mining , KDD ’18, page 1930–1939, New York, NY, USA, 2018.
Association for Computing Machinery. ISBN 9781450355520. doi: 10.1145/3219819.3220007. URL
https://doi.org/10.1145/3219819.3220007.
Shumpei Okura, Yukihiro Tagami, Shingo Ono, and Akira Tajima. Embedding-based news recommendation
for millions of users. In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery
and Data Mining, KDD ’17, page 1933–1942, New York, NY, USA, 2017. Association for Computing Machinery.
ISBN 9781450348874. doi: 10.1145/3097983.3098108. URL https://doi.org/10.1145/3097983.3098108.
11

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Ethan Perez, Florian Strub, Harm de Vries, Vincent Dumoulin, and Aaron C. Courville. FiLM: Visual reasoning
with a general conditioning layer. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 32,
pages 3942–3951, 2018. doi: 10.1609/aaai.v32i1.11671.
Alireza Salemi, Sheshera Mysore, Michael Bendersky, and Hamed Zamani. LaMP: When large language
models meet personalization. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, Proceedings of the
62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 7370–7392,
Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-lon
g.399. URL https://aclanthology.org/2024.acl-long.399/.
Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu, and Tie-Yan Liu. Mpnet: masked and permuted pre-training for
language understanding. In Proceedings of the 34th International Conference on Neural Information Processing
Systems, NIPS ’20, Red Hook, NY, USA, 2020. Curran Associates Inc. ISBN 9781713829546.
Yun-Zhu Song, Yi-Syuan Chen, Lu Wang, and Hong-Han Shuai. General then personal: Decoupling and
pre-training for personalized headline generation. Transactions of the Association for Computational Linguistics,
11:1588–1607, 2023. doi: 10.1162/tacl_a_00621. URL https://aclanthology.org/2023.tacl-1.90/.
Nisan Stiennon, Long Ouyang, Jeff Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario
Amodei, and Paul Christiano. Learning to summarize from human feedback. arXiv preprint arXiv:2009.01325,
2020. URL https://arxiv.org/abs/2009.01325.
Fei Sun, Jun Liu, Jian Wu, Changhua Pei, Xiao Lin, Wenwu Ou, and Peng Jiang. Bert4rec: Sequential
recommendation with bidirectional encoder representations from transformer. InProceedings of the 28th ACM
International Conference on Information and Knowledge Management, CIKM ’19, page 1441–1450, New York, NY,
USA, 2019. Association for Computing Machinery. ISBN 9781450369763. doi: 10.1145/3357384.3357895.
URL https://doi.org/10.1145/3357384.3357895.
Zhaoxuan Tan, Qingkai Zeng, Yijun Tian, Zheyuan Liu, Bing Yin, and Meng Jiang. Democratizing large
language models via personalized parameter-efficient fine-tuning. In Proceedings of the 2024 Conference
on Empirical Methods in Natural Language Processing , pages 6476–6491, Miami, Florida, USA, November
2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.emnlp-main.372. URL https:
//aclanthology.org/2024.emnlp-main.372/.
Zhen Tan, Jun Yan, I-Hung Hsu, Rujun Han, Zifeng Wang, Long Le, Yiwen Song, Yanfei Chen, Hamid Palangi,
George Lee, Anand Rajan Iyer, Tianlong Chen, Huan Liu, Chen-Yu Lee, and Tomas Pfister. In prospect and
retrospect: Reflective memory management for long-term personalized dialogue agents. In Proceedings of the
63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 8416–8439,
Vienna, Austria, July 2025. Association for Computational Linguistics. doi: 10.18653/v1/2025.acl-long.413.
URL https://aclanthology.org/2025.acl-long.413/.
Rahul Vansh, Darsh Rank, Sourish Dasgupta, and Tanmoy Chakraborty. Accuracy is not enough: Evaluating
personalization in summarizers. In Findings of the Association for Computational Linguistics: EMNLP 2023 ,
pages 2582–2595, Singapore, December 2023. Association for Computational Linguistics. doi: 10.18653/v1/
2023.findings-emnlp.169. URL https://aclanthology.org/2023.findings-emnlp.169.
Michael Völske, Martin Potthast, Shahbaz Syed, and Benno Stein. TL;DR: Mining Reddit to learn automatic
summarization. In Lu Wang, Jackie Chi Kit Cheung, Giuseppe Carenini, and Fei Liu, editors, Proceedings
of the Workshop on New Frontiers in Summarization, pages 59–63, Copenhagen, Denmark, September 2017.
Association for Computational Linguistics. doi: 10.18653/v1/W17-4508. URL https://aclanthology.org
/W17-4508.
Chuhan Wu, Fangzhao Wu, Mingxiao An, Jianqiang Huang, Yongfeng Huang, and Xing Xie. Neural news
recommendation with attentive multi-view learning. In Proceedings of the Twenty-Eighth International Joint
Conference on Artificial Intelligence, pages 3863–3869. International Joint Conferences on Artificial Intelligence
Organization, 2019a. doi: 10.24963/ijcai.2019/536.
Chuhan Wu, Fangzhao Wu, Suyu Ge, Tao Qi, Yongfeng Huang, and Xing Xie. Neural news recommendation
with multi-head self-attention. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages
6389–6394, Hong Kong, China, November 2019b. Association for Computational Linguistics. doi: 10.18653
/v1/D19-1671. URL https://aclanthology.org/D19-1671.
12

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Fangzhao Wu, Ying Qiao, Jiun-Hung Chen, Chuhan Wu, Tao Qi, Jianxun Lian, Danyang Liu, Xing Xie, Jianfeng
Gao, Winnie Wu, and Ming Zhou. MIND: A large-scale dataset for news recommendation. In Dan Jurafsky,
Joyce Chai, Natalie Schluter, and Joel Tetreault, editors,Proceedings of the 58th Annual Meeting of the Association
for Computational Linguistics, pages 3597–3606, Online, July 2020. Association for Computational Linguistics.
doi: 10.18653/v1/2020.acl-main.331. URL https://aclanthology.org/2020.acl-main.331.
Wei Xiao, Huiying Wang, Qifeng Zhou, and Qing Wang. Ss4rec: Continuous-time sequential recommendation
with state space models, 2025. URL https://arxiv.org/abs/2502.08132.
Zeping Yu, Jianxun Lian, Ahmad Mahmoody, Gongshen Liu, and Xing Xie. Adaptive user modeling with long
and short-term preferences for personalized recommendation. InProceedings of the Twenty-Eighth International
Joint Conference on Artificial Intelligence, IJCAI-19 , pages 4213–4219. International Joint Conferences on
Artificial Intelligence Organization, 7 2019. doi: 10.24963/ijcai.2019/585. URL https://doi.org/10.24963
/ijcai.2019/585.
Xinliang Frederick Zhang, Nicholas Beauchamp, and Lu Wang. PRIME: Large language model personalization
with cognitive dual-memory and personalized thought process. In Proceedings of the 2025 Conference on
Empirical Methods in Natural Language Processing , pages 33707–33736, Suzhou, China, November 2025.
Association for Computational Linguistics. doi: 10.18653/v1/2025.emnlp-main.1711. URL https:
//aclanthology.org/2025.emnlp-main.1711/.
Yifeng Zhang, Haohao Qu, Liangbo Ning, Wenqi Fan, and Qing Li. SSD4Rec: A structured state space duality
model for efficient sequential recommendation. ACM Transactions on Information Systems, 44(2):29:1–29:26,
2026. doi: 10.1145/3773038.
13

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Appendix Contents
A Datasets 15
A.1 MIND-Large Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
A.2 PENS Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
A.3 OpenAI (Reddit) Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
A.4 MPChat Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
B Schema Construction And Generalizability 16
B.1 Dataset-Specific Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
B.2 What The Schema Shares . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
B.3 Transfer And Pooled Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
C UIG Augmentation 19
D PerTIDE Architectural Details 21
D.1 Discrete-Time SSM Stability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
D.2 SSM Hyperparameter Choices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
D.3 Kernel Interpretation Of The Three PerTIDE Traces . . . . . . . . . . . . . . . . . . . . . . . . . . 24
D.4 Capacity Beyond The Branch Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
D.5 Decoder Contextualization Variants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
E Training Details 29
E.1 Compute Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
E.2 Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
E.3 Statistical Significance Testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
F Baseline Details 35
F.1 Encoder Baselines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
F.2 Baseline Personalized Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
G Measuring Personalization 39
G.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
G.2 PerSEval Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
G.3 PSE Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
H Prediction Accuracy Metrics 41
I Reference-Based Content Metrics 42
J Detailed Results And Additional Analysis 43
J.1 Efficiency And Deployment Cost . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
J.2 Full Predictive Personalization Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
J.3 Retention Probes And Trace Complementarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
J.4 Generation And Reference Agreement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
J.5 Transfer And Sparse-Evidence Stress Tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
J.6 Dialogue As An Additional Application And Boundary . . . . . . . . . . . . . . . . . . . . . . . 52
K Human Reference-Similarity Evaluation (PENS) 53
L LLM Prompting Protocol 55
L.1 LLMs As Summarizers (Personalized Headline Generation) . . . . . . . . . . . . . . . . . . . . 55
L.2 LLMs As Dialogue Generators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
M Assets And Usage Terms 55
14

KDM LAB / LCS2 RESEARCH MANUSCRIPT
A Datasets
Table 5: One event interface, five predictive and generative settings. Ranking uses one positive target and 699
sampled negatives. Generation appends produced responses to the running trajectory. PSE denotes PerSEval;
metric definitions are in Appendices G and I.
Dataset Event evidence and consumer Primary metrics
MovieLens-1M Positive/negative movie events; movie rank-
ing
MRR, nDCG@10, HR@10
MIND Click/ignore news events; news ranking MRR, nDCG@5, HR@10
PENS Click/skip news events; next-news ranking MRR, nDCG@10
PENS News history and headline request; person-
alized generation
PSE-JSD, PSE-SU4, PSE-METEOR
OpenAI-Reddit Feedback-derived summary events and re-
quest; eventized TL;DR generation
PSE-JSD, PSE-SU4, PSE-METEOR
A.1 MIND-Large Dataset
MIND (Large) (Wu et al., 2020) is the full-scale release of the Microsoft News recommendation dataset,
collected from anonymized user behavior logs. It contains 1,000,000 users and 161,013 English news articles,
and the associated interaction logs include over 15 million impressions on the platform (Wu et al., 2020). The
data is organized around impression logs that record the impression ID, anonymized user ID, timestamp, a
user click-history list before the impression, and the displayed candidate news with click/non-click labels; the
release also includes per-article metadata (e.g., title, abstract, category, and entities) (Wu et al., 2020). A small
subsampled variant (MIND-small) is also provided by the dataset maintainers by randomly sampling 50,000
users and their behavior logs from the full dataset (Wu et al., 2020).
A.2 PENS Dataset
PENS (Ao et al., 2021) contains 113,762 news articles spanning 15 topical categories. Each article includes an
ID, title (avg. 10.5 words), body (avg. 549 words), and category label; titles are also linked to WikiData entities.
The dataset further provides user interaction logs (impressions and clicks) and extends MIND news records
with article bodies and personalized headline annotations (Wu et al., 2020).
PENS training set. For training, 500k user–news impressions were sampled from June 13 to July 3, 2019.
Each log entry is recorded as [uID, tmp, clkNews, uclkNews, clkedHis], where clkNews and uclkNews denote
clicked and unclicked news in the impression, and clkedHis is the user’s previously clicked history sorted by
click time. The resulting training pool for PerTIDE exhibits substantial temporal variation in user interactions,
motivating explicit modeling of preference dynamics in offline personalization settings.
PENS test set. To construct an offline evaluation set, 103 English-speaking students first reviewed 1,000
headlines and selected at least 50 articles to indicate their interests. Each participant was then asked to write
preferred headlines for 200 previously unseen articles; assignments overlapped across participants.
Each test article has four participant-written references on average. Editorial checks verified factual
correctness and removed incorrect headlines, yielding a high-quality set of personalized gold references for
evaluation.
A.3 OpenAI (Reddit) Dataset
The OpenAI feedback dataset (Stiennon et al., 2020), built from the Reddit TL;DR corpus (Völske et al., 2017),
contains 123,169 Reddit posts drawn from 29 subreddits. It provides both human-written and OpenAI-
generated summaries and is organized into two splits: Comparisons (training/validation) and Axis (valida-
tion/testing). A curated subset of 1,038 posts was processed under 13 summarization policies, producing
7,713 summaries, which were evaluated by 64 annotators via paired comparisons with auxiliary signals (e.g.,
selection preference, confidence, and ratings along dimensions such as accuracy, coherence, coverage, and
overall quality). In contrast to PENS, these annotations are not indexed by stable user identities or reading
histories.
15

KDM LAB / LCS2 RESEARCH MANUSCRIPT
A.4 MPChat Dataset
MPChat (Ahn et al., 2023) is a multimodal persona-grounded dialogue dataset in which personas are rep-
resented as image–sentence pairs intended to capture episodic memories, and dialogues are curated to be
grounded in these multimodal persona elements. The dataset is released with retrieval-style benchmarks
for multimodal persona-grounded dialogue understanding, including next response prediction, grounding
persona prediction, and speaker identification. In total, MPChat contains 15,000 multi-turn dialogues with
42,531 utterances written by 25,877 users, and it is split chronologically into 11,975/1,516/1,509 dialogues for
train/validation/test (Ahn et al., 2023).
B Schema Construction And Generalizability
B.1 Dataset-Specific Construction
UIG represents an interaction as an action directed at a document or response node. Its construction depends
on what a dataset records: explicit interactions, ratings of generated text, or dialogue turns. The following
mappings preserve these differences in provenance while providing the encoder with the same event interface.
PENS. The recorded clkNews and uclkNews events become click and skip edges to document nodes. In the
training pool, selected sentences from the corresponding articles supply surrogate response nodes, linked
by request (genRes) and generated-response (resGen) transitions. These responses provide training targets;
they are not observed user-authored summaries or evidence that the user’s interests actually evolved in the
sampled order. PENS has user-written test headlines, whereas its training histories primarily record article
interactions (Ao et al., 2021).
OpenAI–Reddit. The source training and evaluation records are kept in separate pools before construction
and augmentation. For each rater identifier, an article receives a derived positive label if at least one associated
generated summary has a feedback-confidence score above the chosen threshold, 6 on the nine-point scale;
the remaining articles receive a derived negative label. Among a rater’s summaries for an article, the highest-
rated summary supplies the response node. Article–response pairs and negative article nodes are randomly
ordered into a trajectory. PerAugy is applied separately within both pools. The confidence threshold, rating-
based selection, and random order are construction rules, rather than observed clicks, skips, or longitudinal
preferences. Rater identifiers therefore index the constructed histories without establishing stable real-world
user identity across time.
MPChat. Dialogue histories pair recent context utterances with a speaker’s subsequent response. Algo-
rithm 1 assigns positive or negative edges to context nodes using response cues, sentiment, and text similarity;
ties and neutral cases are assigned negative. These are inferred stance labels, not explicit preference judgments.
A response used to annotate a historical event belongs to the observed prefix; a response being predicted must
remain outside that prefix. This cutoff is necessary to interpret the response-prediction task as prediction from
history.
B.2 What The Schema Shares
Let domain D have native actions AD and items XD. An item may be a document, movie, or response node.
The schema maps a native event (α, x) to
SD(α, x) =

ρD(α), ψD(x)

, ρD : AD → A, ψD : XD → Rd.
Here A contains positive, negative, request, and generated-response transitions; the latter two distinguish the
input and output sides of a command-like interaction. The same parameterized update consumes these roles
and item embeddings across users and domains. User states remain separate. Thus Alice’s watched movie
and Bob’s watched series can exercise the same update rule without asserting that Alice and Bob have the
same preferences.
For fixed parameters, write the implemented update in compact form as
bi = µ(ai) ⊙ ei, µ(a) =σ(MLPgate(a)),
mr i = Armr i−1 + Bbi, r ∈ {L, S, E},
hi = Φ([mL i ; mS i ; mE i ]) +Wψbi + bψ, (8)
zi = Fgi (hi, zi−1).
16

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Algorithm 1 HYBRID STANCE INFER : MPChat-Style Turn-Level Stance Inference
Require: Context utterances {d}; target response s; sentiment encoder SentEnc; text encoder TxtEnc; cue
lexicons {C}
Ensure: Binary stance labels for linked context turns
1: xs ← lower(s); es ← TxtEnc(xs); σs ← SentEnc(xs)
2: κ ← splitClauses(xs)
3: for each recent context turn d ∈ {d} do
4: xd ← lower(d); ed ← TxtEnc(xd)
5: p ← 0, n ← 0 (positive / negative evidence)
6: for each clause κi ∈ κ do
7: (p, n) ← CueScore(κi, {C}, p, n)
8: end for
9: (p, n) ← SentScore(σs, p, n)
10: (p, n) ← SimScore(cos(es, ed), p, n)
11: ℓd ← I[p > n] (neutral → negative)
12: end for
13: return {ℓd}
Figure 3: Construction of the User Interaction Graph (UIG) from multi-user, multi-turn dialogue. Turn-level
interactions are annotated with behavioral actions and sentiment signals, then projected into a unified UIG
over participating users and content nodes.
The last line includes the command-conditioned routing through the preceding task-ready state (Appendix D).
Keeping the residual input and this state dependence explicit is necessary when extending a trace bound to
the complete encoder.
Proposition B.1 (Invariance to native action relabeling). Suppose two trajectories have identical schema pairs (ai, ei)
at every step, identical command seeds gi, and equal initial trace and task-ready states. Their mr i , hi, and zi are equal at
every step under the same deterministic encoder parameters.
Proof. Equal roles and embeddings give equal bi. Equal previous states and inputs give equal trace updates,
residual fusion, and readout in Eq. (8). Induction from the equal initial states proves the result. □
Native names such as watch, click, and open therefore cease to matter once both the role and item represen-
tation match. A role match alone does not make two items, histories, or users equivalent.
Proposition B.2 (Stability under item-embedding changes). Consider equal-length trajectories with equal initial
states, roles, and command seeds. Let their item-embedding differences be δi = ∥ei − e′ i∥2. Assume ∥Ar∥2 ≤ βr < 1.
Then
∥mr i − m′r i ∥2 ≤ ∥B∥2
i
∑
j=1
βi−j r δj.
17

KDM LAB / LCS2 RESEARCH MANUSCRIPT
If Φ is LΦ-Lipschitz, define
Hi = LΦ∥B∥2 ∑
r
i
∑
j=1
βi−j r δj + ∥Wψ∥2δi.
Then ∥hi − h′ i∥2 ≤ Hi. If the readout satisfies
∥Fg(h, z) − Fg(h′, z′)∥2 ≤ LH∥h − h′∥2 + LZ∥z − z′∥2
on the states under consideration, then
∥zi − z′ i∥2 ≤ LH
i
∑
j=1
Li−j Z Hj.
Proof. Since the shared sigmoid gate has entries in [0, 1], ∥bi − b′ i∥2 ≤ δi. Unrolling the trace difference from
zero initial difference gives ∑i j=1 Ai−j r B(bj − b′ j); the operator-norm bound yields the first inequality. Apply
the Lipschitz bound to concatenated traces, upper-bound their concatenated norm by the sum of component
norms, and add the residual difference to obtain Hi. Finally, the readout gives Di ≤ LH Hi + LZDi−1 with
D0 = 0; unrolling gives the stated bound. □
For the implemented readout, π = softmax(Wzz + Wgg) and Fg(h, z) = (Wππ) ⊙ h + bG. On a set with
∥h∥∞ ≤ H, valid constants are LH = ∥Wπ∥2 and LZ = H∥Wπ∥2Lsm∥Wz∥2, where Lsm is a Lipschitz constant
for softmax. The finite-prefix bound does not require LZ < 1; a uniform long-horizon readout bound needs an
additional contraction condition. Stable traces alone do not establish that condition.
Changing only the item at a fixed step. Fix Alice’s preceding history, action, command, and timestep t,
and replace the current movie by another item. At that step, the trace difference is B diag(µ(at))(et − e′ t). If
all subsequent inputs agree, its contribution at lag k has norm at most ∥B∥2βk r ∥et − e′ t∥2. Nearby embeddings
therefore induce nearby continuous states under the stated assumptions. Moving progressively farther away
enlarges this upper bound; it does not force the states to separate monotonically. Semantic similarity must
be represented by the embedding map, and continuity of a state does not imply continuity of a discrete
recommendation or generated token.
B.3 Transfer And Pooled Training
For equal-length schema trajectories and a command seed g, let x = (SD(τ), g) and define
dsch(x, x′) =
T
∑
i=1
ωi

1(ai ̸= a′ i) +∥ei − e′ i∥2  + λg∥g − g′∥2.
Positive ωi and λg give a metric on these schema representations. Allowing zero weights gives a pseudometric,
interpreted on its quotient. Comparisons of variable-length histories require a common padding or alignment
convention. Trace-influence weights, such as ωi = ∑r βT−i r , emphasize events retained at the endpoint; they
do not by themselves certify a loss Lipschitz constant for the stateful readout.
Proposition B.3 (Schema-level transfer bound). Let source and target joint distributions over (x, y) have input
marginals PS, PT with finite first moments under dsch. For fixed θ, let qD(x) =ED[ℓ( fθ(x), y) | x] for a bounded loss.
Assume a version of qS is defined on both supports and is L-Lipschitz. Set ∆S,T(θ) =EPT |qT(x) − qS(x)|. Then
RT(θ) ≤ RS(θ) +LW1(PS, PT) +∆S,T(θ).
Proof. Add and subtract EPT qS in RT = EPT qT. The conditional-loss difference is at most ∆S,T, while
Kantorovich–Rubinstein duality bounds EPT qS − EPSqS by LW1(PS, PT). □
The bound requires both comparable input geometry and compatible target or command semantics. A
small embedding distance alone cannot control conflicting labels. If a source-risk bound RS ≤ bRS + GS(n, δ)
holds uniformly over the selected model class, it can be substituted into this inequality for a model learned
from the same sample.
For M domains, let nm be fixed sample counts, N = ∑m nm, and πm = nm/N. Let Pπ = ∑m πmPm be the
mixture of input marginals, with joint mixture and risk defined using the same weights. For transfer from a
pooled mixture to target t, write ∆t,π(θ) =EPt |qt(x) − qπ(x)|, where qπ is the conditional expected loss under
the joint mixture. The pooled empirical objective is
bRπ(θ) = 1 N M ∑ m=1 nm ∑ i=1 ℓ( fθ(xm,i), ym,i), bθπ ∈ arg min θ∈Θ bRπ(θ).
18

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Proposition B.4 (Common-substrate training bound). Assume examples are independent within and across domains,
with each domain’s examples drawn from its specified joint distribution. Let ℓ ∈ [0, 1] and F = {(x, y) 7→ ℓ( fθ(x), y) :
θ ∈ Θ}. Let bRN(F ) be its empirical Rademacher complexity on the pooled sample. Assume the preceding transfer
proposition applies to the mixture and target for every θ ∈ Θ, with a common constant L. With probability at least 1 − δ,
Rt(bθπ) ≤ bRπ(bθπ) +2 bRN(F ) +3
r
log(2/δ)
2N
+ LW1(Pt, Pπ) +∆t,π(bθπ).
The empirical-risk term can also be replaced by bRπ(θ⋆) for any comparator θ⋆ ∈ Θ.
Proof. Symmetrization with independent ghost observations from each corresponding domain bounds the
expected uniform risk gap by twice the expected Rademacher complexity. Changing one observation changes
the uniform gap by at most 1/N and the empirical complexity by at most 1/N. Applying bounded differences
to each, with failure probabilityδ/2, gives the uniform boundRπ(θ) ≤ bRπ(θ) +2 bRN(F ) +3 p log(2/δ)/(2N).
It holds at the data-dependent bθπ. Apply the transfer inequality with its common L; empirical optimality gives
the comparator form. □
Corollary B.5 (Estimation bound under compatible pooling). If Pt = Pπ and ∆t,π(θ) =0, only empirical risk
and the estimation terms remain. If the same class admits bRn(F ) ≤ C/√n for the samples considered, the resulting
estimation upper bound for N ≥ nt is no larger than the corresponding bound for a domain-only sample of size nt.
This comparison concerns estimation bounds, not a guarantee of lower empirical risk or higher accuracy
after pooling. Correlated augmentations do not automatically satisfy the independent-example assumption,
and the bounded analysis loss is not the unbounded cross-entropy used in training. The theory identifies
conditions under which shared training is compatible; the frozen-encoder and schema-matched experiments
test whether learned updates are useful in the reported settings. MTSH then specifies how those updates enter,
persist in, and are read from the shared encoder.
C UIG Augmentation
After inserting surrogate response-nodes via genRes and resGen interactions in the base trajectories, we apply
PerAugy-style Chatterjee et al. (2025) augmentation to (i) increase trajectory diversity while preserving selected
local order constraints, and (ii) reduce local incoherence introduced by surrogate responses (r-nodes). We
apply augmentation to u-tier trajectories τuj before training, yielding an expanded trajectory pool used to
instantiate T PENS (and its perturbed variants).
Double shuffling. Given m trajectories sampled within the same permitted pool, we select one target tra-
jectory τ
uj
target and treat the remaining m−1 trajectories as sources. We construct a synthetic trajectory by (i)
preserving an early prefix of the target determined by an offset O, and (ii) substituting later contiguous seg-
ments using source trajectory snippets. To preserve local temporal realism, we enforce a gap hyperparameter
G such that after each substitution, G consecutive steps from the target are kept intact.
Stochastic Markovian perturbation. While shuffling increases structural diversity, it can introduce surrogate
r-nodes whose content is poorly aligned with the target user’s recent context, reducing temporal coherence.
We therefore apply a local, context-aware perturbation that replaces a substituted r-node with a sentence that
better matches the immediate history of the target trajectory. Consider a substituted summary node r(ti) in τ uj DS.
Let τ
uj
ck denote a backward context window of the previous k nodes {cq}k q=1 (most recent first), and let d(ti−1)
be the preceding d-node. We segment d(ti−1) into candidate sentences {stp} n d(ti−1) p=1 . Using SBERT embeddings,
we compute an influence-weighted distance between each candidate sentence and the context window, with
temporal relevance enforced by an exponential decay weight wq = exp(−λ · pos(cq)) and pos(c1) =0.
Let œ ∈ R
n
d(ti−1) ×k be the distance matrix with entries œ(p,q) = σ(estp, ecq ), where σ(v, w) =∥v − w∥2/ √ d
is root mean squared distance (RMSD) for d-dimensional embeddings. We select:
ˆr(ti) = stp∗, p∗ = arg min 1≤p≤n
d(ti−1)
k
∑
q=1
exp

− λ · pos(cq)

σ(estp, ecq ). (9)
19

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Figure 4: UIG Augmentation Pipeline: Chatterjee et al. (2025) proposed framework – (a) Pipeline overview
depicting the two-step augmentation, (b) Double Shuffling (DS) to ensure cross-trajectory augmentation and induce
diffusion, (c) Stochastic Markovian Perturbation (SMP) to smoothen the response-nodes and modulate random diffusion
incorporated in DS stage.
Algorithm 2 DOUBLE SHUFFLING : Cross-Trajectory Segment Substitution
Require: Target trajectory τuj; source trajectories {τui }m−1 i=1 ; offset distribution PO; gap size G
Ensure: Synthetic trajectory ˜τuj
1: Sample offset O ∼ PO
2: ˜τuj ← τuj [1:O] (preserve prefix)
3: t ← O; T ← |τuj |
4: for each source trajectory τui do
5: If t ≥ T, stop; otherwise sample a segment of length s ≤ T − t from τui
6: τseg ← SampleSegment(τui, s); g ← min(G, T − t − s)
7: ˜τuj ← ˜τuj ⊕ τseg (substitute)
8: ˜τuj ← ˜τuj ⊕ τuj [t+s+1:t+s+g] (protected gap)
9: t ← t + s + g
10: end for
11: ˜τuj ← ˜τuj ⊕ τuj [t + 1:T]
12: return ˜τuj
Equivalently, per-sentence scores can be written asœ w where wq = exp(−λ · pos(cq)).
For PENS, these operations construct the augmented training pool τPENS-D. For OpenAI–Reddit, they are
applied separately within the native training and evaluation pools, as described in Appendix B.1; source
segments are not exchanged between pools. The perturbed s-nodes provide additional, coherence-aware
supervision for personalized summarization tasks.
20

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Algorithm 3 SUMMARY PERTURBATION : Local Summary Rewriting
Require: Trajectory τuj; window size k; decay λ; perturbation rate pSMP
Ensure: Perturbed trajectory ˜τuj
1: ˜τuj ← τuj
2: for each substituted summary node s(ti) ∈ ˜τuj do
3: Sample z ∼ Bernoulli(pSMP)
4: if z = 1 then
5: C ←ContextWindow( ˜τuj, ti, k)
6: ˆs(ti) ← RewriteSummary(s(ti), C, λ) (Eq. (9))
7: Replace s(ti) ← ˆs(ti)
8: end if
9: end for
10: return ˜τuj
D PerTIDE Architectural Details
D.1 Discrete-Time SSM Stability
We first state the stability condition used by the discrete state-space traces in PerTIDE. Consider the linear
recursion
ht = Aht−1 + Bxt,
with homogeneous dynamics
ht = Aht−1.
The stability of the homogeneous part determines whether past perturbations decay or persist without bound.
Proposition D.1 (Discrete-time stability by spectral radius). Let A ∈ Cd×d. If
ρ(A) < 1,
where ρ(A) =maxi |λi(A)| is the spectral radius, then the homogeneous recursion
ht = Aht−1
is asymptotically stable, i.e.,
lim
t→∞
Ath0 = 0
for every initial state h0.
Proof. Since ρ(A) < 1, all eigenvalues of A lie strictly inside the unit disk. By the standard spectral-radius
characterization of matrix powers, this implies
lim
t→∞
At = 0.
Therefore,
lim
t→∞
ht = lim t→∞ Ath0 = 0,
which proves asymptotic stability.
Corollary D.2 (Modal stability for diagonalizable transitions). Suppose A is diagonalizable as
A = Q diag(a1, . . . ,ad)Q−1.
Then the homogeneous dynamics are asymptotically stable if
|ai| < 1 for all i = 1, . . . ,d.
For 0 < |ai| < 1, the contribution of mode i after lag ∆ decays as
|ai|∆ = exp

− ∆ τi

, τi = − 1 log |ai| .
21

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Proof. For a diagonalizable transition,
A∆ = Q diag(a∆ 1 , . . . ,a∆ d )Q−1.
Thus A∆ → 0 whenever |ai| < 1 for every mode. The effective decay relation follows by writing
|ai|∆ = exp(∆ log |ai|) =exp

− ∆ τi

,
which gives
τi = − 1 log |ai| .
A zero modal base removes its homogeneous contribution after one step; the logarithmic time constant
above is defined only for nonzero bases. For the shared orthogonal eigenbasis used here, the spectral norm
equals the largest absolute modal base, so modal bounds also supply the contraction constants used in
Appendix B.2.
Connection to continuous-time eigenvalues. If the discrete transition is induced by a continuous-time
generator with eigenvalues λi ∈ C, then continuous-time stability requires
Re(λi) < 0.
Under exponential discretization,
ai = exp(λi∆t),
so
|ai| = exp(Re(λi)∆t).
Hence,
|ai| < 1 ⇐ ⇒Re(λi) < 0.
Under Euler-style discretization,
ai = 1 + ηλi,
and stability requires
|1 + ηλi| < 1.
Thus Euler-style maps impose an explicit step-size constraint coupling η and λi. The following analysis
assumes these discrete-mode constraints. The spectral formulas alone do not ensure the Euler constraint or
order the retention ranges of the three branches.
D.2 SSM Hyperparameter Choices
We next give sufficient rules for selecting the short-memory horizon and the event-step size. These rules
are not claimed to be necessary; they provide simple conservative choices that make the intended timescale
behavior explicit.
Notation. Let ε ∈ (0, 1/2) be a small tolerance, let
σ(x) = 1 1 + e−x
be the sigmoid function, and let τ > 0 denote a desired exponential decay time constant.
22

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Short-Memory Retention And Lag
The short-trace modal base is aS = σ(−κλS), with λS > 0. The parameter κ controls per-step retention; it is
not the lag. Retention at lag H is aH S .
Lemma D.3 (Sufficient per-step suppression). For λS > 0 and ε ∈ (0, 1/2),
κ ≥ 1 λS log 1 − ε ε (10)
implies
aS = σ(−κλS) ≤ ε. (11)
Proof. The inequality 1/(1 + eκλS ) ≤ ε is equivalent to eκλS ≥ (1 − ε)/ε. Taking logarithms gives the stated
condition.
For a fixed base aS ∈ (0, 1), a lag H ≥ log ε/ logaS instead ensures aH S ≤ ε. These are distinct choices: one
selects a base, the other reads its resulting horizon.
Corollary D.4 (Rapid suppression beyond the short-memory horizon) . Let aS = σ(−κλS) ∈ (0, 1) be a
short-trace modal base. If |ut−ℓ| ≤R for all ℓ, then the total contribution from lags at least W is bounded by

 ∞ ∑ ℓ=W aℓ Sut−ℓ

 ≤ R aW S 1 − aS .
Thus, when aS is small, evidence outside a short window is geometrically suppressed.
Proof. By the triangle inequality,

 ∞ ∑ ℓ=W aℓ Sut−ℓ

 ≤ ∞ ∑ ℓ=W aℓ S|ut−ℓ| ≤R ∞ ∑ ℓ=W aℓ S.
Since aS ∈ (0, 1),
∞
∑
ℓ=W
aℓ S = aW S 1 − aS .
This proves the bound.
Event-Kernel Step Size Selection
For the episodic trace, let λE < 0 denote a stable continuous-time decay rate. Under Euler-style discretization
with step size η > 0, the per-step base is
aE = 1 + ηλE.
The event influence at lag ∆ = t − k is therefore
w(E) t,k = (1 + ηλE)t−k. (12)
We choose η so that this discrete kernel exactly matches the target exponential decay
exp

− t − k τ  .
Lemma D.5 (Exact event-kernel matching). Let λE < 0 and τ > 0. Define
η = e−1/τ − 1 λE . (13)
Then
1 + ηλE = e−1/τ,
and for every lag ∆ = t − k,
(1 + ηλE)t−k = exp

− t − k τ  .
Moreover, η > 0 and
0 < 1 + ηλE < 1,
so the induced discrete event mode is stable.
23

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Proof. Substituting Eq. (13) gives
1 + ηλE = 1 +

e−1/τ − 1
λE
!
λE = e−1/τ.
Raising both sides to the power t − k yields
(1 + ηλE)t−k = e−(t−k)/τ.
Since τ > 0, we have e−1/τ ∈ (0, 1). Therefore e−1/τ − 1 < 0. Because λE < 0, Eq. (13) implies η > 0. Finally,
1 + ηλE = e−1/τ ∈ (0, 1),
which proves stability.
D.3 Kernel Interpretation Of The Three PerTIDE Traces
Each branch induces a geometric lag kernel. Different spectral parameterizations can select different bases.
Their attainable kernels nevertheless overlap. Distinct timescales require different learned bases; branch names
do not prove semantic disentanglement. Trace-subset and temporal-regime experiments test their functional
differentiation.
General tri-trace recursion. For each trace r ∈ {L, S, E}, PerTIDE updates a memory state as
m(r) t = Arm(r) t−1 + Bbt, (14)
where bt is the action-gated event cell, B is the input operator, and Ar is the trace-specific transition matrix.
Assume that
Ar = Qr diag(a(r) 1 , . . . ,a(r) d )Q−1 r .
The three PerTIDE spectral maps induce
a(L) i = exp(δλL,i), a(S) i = σ(−κλS,i), a(E) i = 1 + ηλE,i.
For clarity, we state the results for real stable modes satisfying
0 ≤ a(r) i < 1.
For complex modes, the same statements hold for the decay envelope after replacing a(r) i by |a(r) i |.
Proposition D.6 (Mode-wise lag kernels induced by the trace recursion). For each trace r ∈ {L, S, E} and mode i,
the contribution of an input at lag ℓ = t − s to the modal state is weighted by
k(r) i (ℓ) =  a(r) i ℓ , ℓ ≥ 0.
Thus each trace implements an explicit geometric lag kernel in its eigenbasis.
Proof. Move Eq. (14) to the eigenbasis of trace r:
˜m(r) t = Q−1 r m(r) t , u(r) t = Q−1 r Bbt.
Then
˜m(r) t = diag(a(r) 1 , . . . ,a(r) d ) ˜m(r) t−1 + u(r) t .
Therefore, each mode evolves independently:
˜m(r) t,i = a(r) i ˜m(r) t−1,i + u(r) t,i .
Unrolling gives
˜m(r) t,i =  a(r) i t ˜m(r) 0,i + t ∑
s=1

a(r) i t−s u(r) s,i .
Hence an input at lag ℓ = t − s is weighted by

a(r) i ℓ .
This proves the claim.
24

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Proposition D.7 (Effective memory length of a stable modal kernel). Let a ∈ (0, 1) and define the unnormalized
lag kernel
ka(ℓ) =aℓ, ℓ = 0, 1, 2, . . . .
Its normalized version is
¯ka(ℓ) = (1 − a)aℓ.
Then the expected lag is
E¯ka [ℓ] = a 1 − a .
The half-life is
h(a) =log(1/2) log a .
Both quantities increase as a approaches one.
Proof. Since ¯ka is the probability mass function of a geometric distribution over nonnegative lags,
∞
∑
ℓ=0
(1 − a)aℓ = 1.
Its expected lag is
E¯ka [ℓ] = (1 − a)
∞
∑
ℓ=0
ℓaℓ = (1 − a) a (1 − a)2 = a 1 − a .
The half-life is the lag h satisfying
ah = 1 2.
Taking logarithms gives
h(a) =log(1/2) log a .
For a ∈ (0, 1), increasing a slows the geometric decay, and therefore increases both the expected lag and the
half-life.
Corollary D.8 (Trace-specific retention profiles). The three PerTIDE spectral maps induce the following modal
kernels:
k(L) i (ℓ) =(exp(δλL,i))ℓ ,
k(S) i (ℓ) =(σ(−κλS,i))ℓ ,
k(E) i (ℓ) =(1 + ηλE,i)ℓ .
Their effective retention differs when these bases differ. For example, 0 < aS < aE < aL < 1 gives correspondingly
ordered half-lives; this ordering is an additional condition, not a consequence of the three formulas.
Proof. The result follows directly by substituting the three trace-specific spectral maps into Proposition D.6.
Long-Term Trace: Persistent Evidence Accumulation
Proposition D.9 (Slow modes accumulate repeated evidence). Consider a long-term modal direction i with
a(L) i = exp(δλL,i) ∈ (0, 1).
Suppose repeated evidence enters this mode as
u(L) s,i = µi > 0, s = 1, . . . ,t,
and let ˜m(L) 0,i = 0. Then
˜m(L) t,i = µi 1 −

a(L) i t
1 − a(L) i ,
and
lim
t→∞
˜m(L) t,i = µi
1 − a(L) i .
Hence, when a(L) i is close to one, repeated evidence accumulates into a large persistent state.
25

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Proof. By Proposition D.6,
˜m(L) t,i = t ∑
s=1

a(L) i t−s µi.
Let ℓ = t − s. Then
˜m(L) t,i = µi t−1 ∑
ℓ=0

a(L) i ℓ .
Using the finite geometric sum,
t−1
∑
ℓ=0

a(L) i ℓ = 1 −

a(L) i t
1 − a(L) i .
Since a(L) i ∈ (0, 1), 
a(L) i t → 0,
which yields the stated limit.
This formalizes the role of the long-term trace. If a user repeatedly produces evidence in a stable preference
direction, such as repeated climate-policy interactions, the long-term kernel retains and accumulates this
evidence rather than rapidly discarding it.
Short-Term Trace: Recent Burst Tracking
Proposition D.10 (Small short-trace bases emphasize recent evidence). Consider a short-term modal direction j
with
a(S) j = σ(−κλS,j) ∈ (0, 1).
With zero initial state and the sum truncated at lag t − 1, the modal state can be written as
˜m(S) t,j = u(S) t,j + a(S) j u(S) t−1,j +  a(S) j 2 u(S) t−2,j + · · ·.
If a(S) j is small, then the newest inputs dominate and older inputs are geometrically suppressed.
Proof. The expansion follows from Proposition D.6. The relative weight assigned to an input ℓ steps in the
past is 
a(S) j ℓ .
For a(S) j ∈ (0, 1), this quantity decays geometrically in ℓ. If a(S) j is small, the decay is rapid, so recent inputs
dominate the modal state.
This formalizes the role of the short-term trace. A recent burst of sports-highlight interactions, for example,
enters the short trace with high weight at the current timestep, while older evidence is rapidly suppressed.
Episodic Trace: Decaying Event Imprint
Proposition D.11 (Finite-window events leave controlled decaying imprints) . Consider an episodic modal
direction k with
a(E) k = 1 + ηλE,k ∈ (0, 1).
Suppose an event is active on the finite window t0 ≤ s ≤ t1:
u(E) s,k =
(
βk, t0 ≤ s ≤ t1,
0, otherwise,
βk > 0.
Consider the state component due solely to these event inputs, with zero state before the event. Let W = t1 − t0 + 1. For
t > t1, its remaining post-event imprint is
˜m(E) t,k = βk  a(E) k t−t1 1 −

a(E) k W
1 − a(E) k .
After the active window closes, the event leaves an imprint that decays at rate a(E) k .
26

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Proof. For t > t1, only the event-window inputs contribute:
˜m(E) t,k =
t1
∑
s=t0

a(E) k t−s βk.
Factor out the decay from the end of the event window:
˜m(E) t,k = βk  a(E) k t−t1 W−1 ∑
q=0

a(E) k q .
Using the finite geometric sum gives
W−1
∑
q=0

a(E) k q = 1 −

a(E) k W
1 − a(E) k .
This proves the expression.
Corollary D.12 (Event time constant under exact kernel matching). If the event-step size is chosen as in Lemma D.5,
then
a(E) k = 1 + ηλE,k = e−1/τk.
Therefore,
k(E) k (ℓ) =e−ℓ/τk,
and the post-event imprint becomes
˜m(E) t,k = βke−(t−t1)/τk 1 − e−W/τk 1 − e−1/τk .
Thus τk controls the decay of this mode after the finite input window closes. A shared scalar η cannot independently
match arbitrary target time constants for every fixed λE,k.
Proof. The result follows by substituting
a(E) k = e−1/τk
into Proposition D.11.
This formalizes the role of the episodic trace. A rare debate-night interaction, tournament-final event, or
command-specific burst does not vanish immediately. Its imprint has an infinite geometrically decaying tail,
rather than a hard finite horizon.
D.4 Capacity Beyond The Branch Names
Proposition D.13 (Finite-horizon interpolation by geometric kernels). Fix an integer horizon H ≥ 0 and H + 1
distinct bases a1, . . ., aH+1 ∈ (0, 1). For any real filter values v0, . . ., vH, there are real coefficients c1, . . ., cH+1 such
that
K(ℓ) =
H+1
∑
m=1
cmaℓ m = vℓ, ℓ = 0, . . . ,H.
Proof. The matrix Vℓm = aℓ m, with rows ℓ = 0, . . ., H, is a Vandermonde matrix. Its determinant is ∏j<k(ak −
aj) ̸= 0, so Vc = v has a unique real solution.
This is a finite-horizon representation result with potentially signed coefficients and one mode per con-
strained lag. It gives no conditioning bound, infinite-horizon approximation guarantee, or guarantee that
training discovers these coefficients. A fixed-width encoder cannot invoke the result for arbitrary horizons. If
complex-conjugate modes were allowed, their real combinations would additionally give damped sine and
cosine kernels; the implemented shared real orthogonal parameterization does not establish such complex
modes.
Corollary D.14 (Branch interpretation is not exclusive). The long-term, short-term, and episodic names describe
intended retention behavior, rather than three disjoint classes of temporal filters. Sufficiently rich real geometric mixtures
can match any specified filter on a finite set of lags under the preceding proposition’s conditions.
The empirical question is therefore whether the learned branches supply complementary information.
The temporal probes and trace ablations address that question without assigning each coordinate a human-
interpretable preference.
27

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Implementation refinements. The main-text equations expose the functional MTSH decomposition rather
than every parameter-sharing or residual detail. In our implementation, the three temporal traces share an
orthogonal eigenbasis (QL = QS = QE) while retaining trace-specific spectra and spectral maps. After trace
fusion, we additionally include a linear residual from the current action-conditioned evidence; this provides a
direct current-event path but introduces no additional recurrent state or retention timescale. Command routing
is also implemented statefully: the previous task-ready state carries the routing context, and the resulting
command distribution modulates the current fused history state. These choices are implementation-level
parameterizations of the entry–persistence–fusion–consumption operators and do not introduce additional
temporal-memory components.
D.5 Decoder Contextualization Variants
Setup. For each generative instance, the encoder produces (i) the task-adapted user state z(tl ) u and (ii) the
predicted query-conditioned representation ˆz(tl+1) q,u . Let edq denote the embedding of the query document to be
generated from. We condition a pretrained DistilGPT2 decoder (Hugging Face, n.d.) through a lightweight
contextualization module that maps these representations to a learned prefix.
UFI contextualization. User Fused Injection (UFI) directly combines the predicted query-conditioned repre-
sentation with the query-document embedding:
cuser UFI = MLPUFI
h
ˆz(tl+1) q,u ; edq
i
. (15)
UFI therefore supplies a fused user–query control without explicitly modulating the query-conditioned
representation by the user state.
UGI contextualization. User Gated Injection (UGI) first applies user-conditioned feature-wise affine modula-
tion to the query-conditioned representation, following the FiLM form (Perez et al., 2018):
γ = MLPγ

z(tl ) u  , β = MLPβ  z(tl ) u  ,
˜z(tl+1) q,u = γ ⊙ ˆz(tl+1) q,u + β. (16)
The modulated representation is then fused with the query-document embedding:
cuser UGI = MLPUGI
h
˜z(tl+1) q,u ; edq
i
. (17)
Thus, unlike UFI, UGI allows the user state to emphasize or suppress individual components of the query-
conditioned representation before decoder conditioning.
Prefix construction. For either variant, let cuser denote the resulting user-conditioned control. We further
combine it with query-document evidence:
cdoc = MLPdoc
h
cuser; edq
i
, c = LN

cuser + cdoc

. (18)
The resulting vector is projected into a prefix of K = 8 decoder embeddings:
P = reshapeK×dD

Wp Dropout(c) +bp

, (19)
where dD is the DistilGPT2 embedding dimension. If x1:S denotes the tokenized query document and y1:T the
target headline, teacher-forced training uses
H(0) = [P; Emb(x1); . . . ; Emb(xS); Emb(y1); . . . ; Emb(yT−1)] , (20)
with the standard autoregressive objective p(yt | y<t, x1:S, P).
Decoder tuning. DistilGPT2 is initialized from pretrained weights. Its parameters are initially frozen;
during joint and generation-specific training, the contextualization modules, the final two transformer blocks,
and the final decoder layer normalization are optimized, while all remaining DistilGPT2 parameters stay
fixed. The generation-specific stage freezes the PerTIDE encoder, so personalization continues to enter the
decoder through the learned preference-history state and its UFI/UGI contextualization rather than through
user-specific decoder parameters.
28

KDM LAB / LCS2 RESEARCH MANUSCRIPT
E Training Details
E.1 Compute Resources
All dataset ingestion and feature lookup were performed on CPU, including CSV loading and construction
of the canonical ID maps (id2text/id2phrases) and vocabulary indices (actions2idx, node2idx, user2idx).
Dense node embeddings for dialogue/document/response/summary nodes were loaded from precomputed
pickled files and resolved on-the-fly during training via canonical IDs, with missing embeddings defaulted to
a zero vector of dimension dmodel=768.
Experiments were run on Lightning.ai using A100 and RTX 6000-family GPUs. Pretrained LLMs used
automatic device placement (device_map="auto"). Exact device counts and the experiment-to-GPU mapping
were not preserved in the run records. Appendix J.1 reports estimated resource costs.
E.2 Training
We train the multi-task model using a single-row update scheme: each training example is converted into a
batch of size 1, and one optimizer step is applied per valid row. We train forE = 45 epochs over Ntrain = 78,274
training rows, with rows that fail parsing or target construction skipped. Per epoch, we deterministically
shuffle the active training table with random_state=SEED+epoch. We use training seeds 42, 32, and 22, and
evaluation seeds 1111, 2222, and 3333. We define a processed prefix length Tproc = T − 2 so that the final two
positions serve as query and target.
Optimization uses AdamW with learning rate 3 × 10−4 and gradient clipping at norm 1.0. The shared
encoder is supervised with
Lenc = 0.2Lpos + 0.4Lnext + 0.4Ltask,
The weights are fixed globally. The main encoder uses pooled MovieLens, MIND, PENS, and OpenAI training
trajectories; the source-only transfer encoder instead uses PENS alone. Training adds the corresponding
downstream task objective. Predictive training uses the task-specific ranking or classification loss.
For generation, we condition a pretrained DistilGPT2 decoder through an eight-token learned UFI/UGI
prefix. The generation objective combines autoregressive target-token cross-entropy with a semantic alignment
term,
Lgen = LCE + 0.15 Lsem.
The contextualization modules, final two DistilGPT2 transformer blocks, and final decoder layer normalization
are optimized for generation, while the remaining decoder parameters stay fixed. The generation-specific stage
freezes the PerTIDE encoder. Decoder contextualization and prefix construction are detailed in Appendix D.5.
Crash-safe checkpointing and validation. We save row checkpoints every 15,000 processed rows and an
additional end-of-epoch checkpoint. Row checkpoints store the current epoch and row index, and resumption
continues from the next row. After each epoch, we evaluate on a deterministic validation slice of up to 500
examples per task, reporting overall and per-task mean losses (total loss and its encoder/user/item/generation
components).
E.3 Statistical Significance Testing
We assess evaluation uncertainty using paired bootstrap resampling over the held-out evaluation pool. The
purpose of this analysis is to test whether the observed improvement of PerTIDE over a comparator is stable to
resampling of the same evaluation instances, rather than being driven by a particular subset of users, histories,
rollout positions, or candidates. For every dataset–task–metric tuple, the paired systems are evaluated on
identical held-out examples and identical history prefixes. For predictive recommendation, they additionally
use the same candidate sets containing one ground-truth target and 699 sampled negatives.
Let Teval = {xn}N n=1 denote the held-out evaluation pool for a task. For a modelA and metric M, let M(A; S)
denote the metric computed on resampled evaluation set S. For each paired comparison between PerTIDE
and a comparator A, including the strongest task-native baseline, PAH/MDH/LDH controls, or an ablated
PerTIDE variant, we draw B = 10,000 paired bootstrap samples S1, . . ., SB from Teval. The same sampled
indices are used for both systems within every bootstrap replicate.
For bootstrap replicate b, we compute the paired metric difference
∆b = M(PerTIDE; Sb) − M(A; Sb).
29

KDM LAB / LCS2 RESEARCH MANUSCRIPT
The reported point estimate for each model is the mean over the bootstrap evaluations,
¯MB(A) = 1 B B ∑ b=1 M(A; Sb),
and the reported paired improvement is
¯∆B = 1 B B ∑ b=1 ∆b.
Statistical support for a positive improvement is determined directly from the empirical paired-bootstrap
distribution {∆b}B b=1. We construct a one-sided 95% bootstrap confidence interval for the paired difference
and regard an improvement as statistically supported when its lower confidence bound is greater than zero.
Because the resampling is paired, all variation within a replicate arises from changing the evaluated instances
while holding the two compared systems and their evaluation conditions fixed.
We apply this procedure to predictive metrics including MRR, nDCG@5, nDCG@10, and HR@10, and to the
generation and personalization metrics reported for PENS and OpenAI-Reddit, including PSE-JSD, PSE-SU4,
PSE-METEOR, ROUGE, BLEU-4, BERTScore, and human-judgment scores where applicable.
This analysis measures test-set sampling variability for fixed trained systems. It does not estimate vari-
ability arising from independent retraining, alternative train/test splits, or different negative-sampling pools.
Accordingly, statistical-support statements in the paper refer specifically to paired stability of the reported
gains under the fixed evaluation protocol.
30

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Table 6: Notation and symbol table.
Symbol Meaning Symbol Meaning
UIG and Action-On-Item Schema
Gu = ⟨Nu, Eu⟩ User-specific interaction graph. Nu, Eu User-specific nodes and edges.
u(t0) Initial user anchor node. d(ti) Item/content node at timestep ti.
r(ti) u Response node at timestep ti. α(ti) Domain-native action label.
A Shared action-role vocabulary. a(ti) Schema-level action role.
ρD(·) Domain-specific role mapping. ψD(·) Domain-specific target-locus embedding
map.
SD(e) Schema-normalized native event. τu Time-ordered user trajectory.
Ttrain, Ttest Train and test trajectory pools. dq Query item/content node.
gq Query or task seed embedding. Q Set of task/command types.
Interaction Blocks and Target-Locus Embeddings
b(ti) u =
⟨a(ti), tl(ti)⟩
Action role applied to target locus. tl(ti) Target locus of current action.
e(ti) tl Target-locus embedding. µ(ti) Action-conditioned gating vector.
b(ti) u Action-gated event cell. ϕ(·) Optional generic block embedder.
xj Generic baseline block embedding. d Hidden and embedding dimensionality.
MTSH and PerTIDE State Variables
m(ti,L) u Long-term preference trace. m(ti,S) u Short-term preference trace.
m(ti,E) u Episodic preference trace. Ar Trace transition matrix.
Qr, Λr Shared eigenbasis ( Qr = Q) and trace
spectrum.
B Shared trace input operator.
Φ(·) Multi-trace fusion map. Ψ(·) Action-conditioned evidence injection
map.
h(ti) bu Fused preference-history state. Π(·) Command/task inference map.
G(·) Command-conditioning gate. π(ti) u Predicted command/task distribution.
z(ti) bu Task-ready user state.
Task Heads and Encoder Objectives
T Downstream task or command type. fT(·) Task-specific prediction head.
ˆz(tl +1) q,u Query-conditioned next-step state. ˆyT Predicted task output.
ˆp(·) Task-head predictive distribution. y∗ T Ground-truth task target.
B Vocabulary of observed block nodes. Lpos Temporal-position alignment loss.
Lnext Next-block prediction loss. Ltask Command/task classification loss.
Lenc Combined encoder training objective. Lobj Downstream task objective.
Decoder Contextualization: UFI and UGI
edq Query-document/item embedding. c Final decoder control vector.
cuser UFI User-fused control before document
grounding.
γ FiLM scale vector.
β FiLM shift vector. ⊙ Elementwise product.
˜z(tl +1) q,u User-gated query representation. cuser UGI User-gated control before document
grounding.
cdoc Document-grounding control vector. K Learned prefix length (K = 8).
P Learned decoder prefix embeddings. Wp, bp Control-to-prefix projection parameters.
H(0) Decoder input states after prefix and
source-token concatenation.
H(L) Final decoder hidden states.
θD Pretrained DistilGPT2 parameters, par-
tially fine-tuned.
31

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Table 7: Event input, traces, and fusion. Architecture dimensions for d = 768. MLPs have two layers with
hidden width 768 unless stated otherwise.
Symbol Meaning Dimensions
Action-Gated Event Cells
d Model / latent width (seed embeddings, memory traces,
user state, task embeddings)
768
da Action-role input width 4
e(ti) tl Target-locus embedding at timestep ti; induces item-side
abstraction
R768
a(ti) One-hot action-role input to the gate MLP R4
W(1) gate, b(1) gate Gate MLP layer-1 parameters (4 →768) R768×4, R768
W(2) gate, b(2) gate Gate MLP layer-2 parameters (768 →768) R768×768, R768
µ(ti) Action-specific gate, µ(ti) = σ(MLPgate(a(ti))) R768
b(ti) u Action-gated event cell, b(ti) u = µ(ti) ⊙ e(ti) tl R768
Tri-Trace SSM (Long / Short / Episodic)
m(ti,r) u Memory trace for timescale r ∈ {L, S, E} R768
Q Learned orthogonal eigenbasis shared across traces (QL =
QS = QE = Q)
R768×768
Λr Trace-specific diagonal spectrum for r ∈ {L, S, E} (stored
as diagonal entries)
R768
B Input operator shared across traces R768×768
δ Long-term spectral-map scalar in exp(δΛL) scalar
κ Short-term spectral-map scalar in σ(−κΛS) scalar
η Episodic spectral-map scalar in (I + ηΛE) scalar
Adaptive Memory Mixer
h(ti) bu Fused preference-history state; implementation addition- ally includes a direct current-event residual R768
W(1) Φ , b(1) Φ Mixer MLP layer-1 parameters ( [m(L); m(S); m(E)] ∈
R2304 →768)
R768×2304, R768
W(2) Φ , b(2) Φ Mixer MLP layer-2 parameters (768 →768) R768×768, R768
Wψ, bψ Linear current-event residual projection applied after
trace fusion
R768×768, R768
32

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Table 8: Command readout, supervision, and decoder settings. Architecture dimensions for d = 768. MLPs
have two layers with hidden width 768 unless stated otherwise.
Symbol Meaning Dimensions
Command-Conditioned Readout (Realization of Π and G)
gq Task / command seed embedding R768
π(ti) u Command/task distribution π(ti) u =
SoftMax(Wtask[z(ti−1) bu ; gq]); routing uses the preced- ing task-ready state (Section 4)
R|Q|
Wtask Task-distribution projection R|Q|×1536
Wπ Command-to-state gating projection in G(·) R768×|Q|
bG Command-gate bias R768
z(ti) bu Command-conditioned task-ready preference state after gating R768
Encoder Supervision Heads
l Trajectory slice length used for encoder supervision scalar
Wpos Position classifier over {1, . . . ,l − 1} R(l−1)×768
Wlin, blin Linear head mapping z(tl−1) bu → ˆz(tl ) bu R768×768, R768
|B| b-node vocabulary size for next-step prediction 63,000
Wnext, bnext Query b-node predictor logits over B R|B|×768, R|B|
λpos, λnext, λtask Encoder-loss weights in Lenc = λposLpos + λnextLnext +
λtaskLtask
0.2, 0.4, 0.4
Shared Decoder-Side Quantities
dD Pretrained DistilGPT2 decoder embedding width 768
dc Decoder control-vector width 768
K Learned decoder-prefix length 8
nFT Number of final DistilGPT2 transformer blocks fine-tuned
during generation training; final decoder LayerNorm is
also optimized
2
ˆz(tl+1) q,u Predicted query-conditioned representation from the en-
coder
R768
z(tl ) u Task-adapted user state from the encoder R768
edq Query-document embedding R768
Table 9: User fused and user gated injection. Architecture dimensions for d = 768. MLPs have two layers
with hidden width 768 unless stated otherwise.
Symbol Meaning Dimensions
Decoder-UFI (User Fused Injection)
W(1) UFI, b(1) UFI UFI MLP layer-1 parameters ([ˆzq,u; edq ] ∈ R1536 →768) R768×1536, R768
W(2) UFI, b(2) UFI UFI MLP layer-2 parameters (768 →768) R768×768, R768
cuser UFI User-fused control, cuser UFI = MLPUFI([ˆzq,u; edq ]) R768
Decoder-UGI (User Gated Injection)
W(1) γ , b(1) γ FiLM-scale MLP layer-1 parameters (z(tl ) u ∈ R768 →768) R768×768, R768
W(2) γ , b(2) γ FiLM-scale MLP layer-2 parameters (768 →768) R768×768, R768
W(1) β , b(1) β FiLM-shift MLP layer-1 parameters (z(tl ) u ∈ R768 →768) R768×768, R768
W(2) β , b(2) β FiLM-shift MLP layer-2 parameters (768 →768) R768×768, R768
γ, β FiLM scale/shift vectors from the user state R768, R768
˜z(tl+1) q,u Gated query representation, ˜zq,u = γ ⊙ ˆzq,u + β R768
W(1) UGI, b(1) UGI UGI MLP layer-1 parameters ([˜zq,u; edq ] ∈ R1536 →768) R768×1536, R768
W(2) UGI, b(2) UGI UGI MLP layer-2 parameters (768 →768) R768×768, R768
cuser UGI User-gated control, cuser UGI = MLPUGI([˜zq,u; edq ]) R768
33

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Table 10: Document grounding, prefix, and generation loss. Architecture dimensions for d = 768. MLPs have
two layers with hidden width 768 unless stated otherwise.
Symbol Meaning Dimensions
Decoder Document Grounding
W(1) doc, b(1) doc Document-grounding MLP layer-1 parameters
([cuser; edq ] ∈ R1536 →768)
R768×1536, R768
W(2) doc, b(2) doc Document-grounding MLP layer-2 parameters ( 768 →
768)
R768×768, R768
cdoc Document-grounding control, cdoc = MLPdoc([cuser; edq ]) R768
c Final normalized decoder control, c = LN(cuser + cdoc) R768
Learned Prefix Injection
Wp, bp Control-to-prefix projection, P = reshapeK×dD (Wpc + bp) R6144×768, R6144
P Learned prefix embeddings prepended to the decoder
input
R8×768
H(0) Decoder input states formed from the learned prefix,
source tokens, and teacher-forced target-prefix tokens
R(K+S+T−1)×768
Generation Supervision
λsem Semantic-alignment weight in Lgen = LCE + λsemLsem 0.15
34

KDM LAB / LCS2 RESEARCH MANUSCRIPT
F Baseline Details
F.1 Encoder Baselines
Notation and grouping principle. Let τu 1:i−1 = (b(t1) u , . . ., b(ti−1) u ) denote the ordered prefix of a user’s I-tier
trajectory before timestep ti. Each interaction block is embedded as xj = ϕ

b
(tj)
u

∈ Rd, and the history encoder
exposes a task-facing state z(ti) u ∈ Rd after processing this prefix. Following Section 3.1, we organize baselines
into Profile Aggregation (PAH), Markovian Drift (MDH), and Long-Horizon Dynamics (LDH) families
according to the form of the state exposed downstream. These are operational state-design families, not
mutually exclusive assumptions about user dynamics. Architectures can admit more than one mathematical
description; assignments below follow the dominant mechanism by which each model constructs its task-facing
history state.
Profile aggregation family (PAH). PAH groups encoders that expose an order-invariant profile obtained by
aggregating past interaction representations. Its generic form is a permutation-invariant operator fAgg(·):
z(ti) u = fAgg  {xj}i−1 j=1  . (21)
We use the following PAH-family baselines.
MeanPool-B.
z(ti) u = 1 i − 1 i−1 ∑ j=1 xj. (22)
MaxPool-B. 
z(ti) u  k = max 1≤j≤i−1  xj  k, ∀k ∈ {1, . . . ,d}. (23)
NAML (PAH-aligned). NAML-style encoders first produce per-item representations hj from multi-view
features and then aggregate them through attention pooling:
z(ti) u = i−1 ∑
j=1
αj hj, αj = exp(s(hj)) ∑i−1 q=1 exp(s(hq)) . (24)
Under this history-level formulation, the task-facing state is an order-invariant weighted aggregation of
per-item representations, placing NAML in the PAH family.
PLM-NR (PAH-aligned). PLM-NR-style encoders replace the item representation module with a pretrained
language model to obtain hj, while retaining an order-invariant history aggregation operator, typically
attention pooling as in Eq. (24). We therefore place PLM-NR in PAH according to its exposed history state,
while ϕ(·) provides the stronger content representation.
Recurrent state and Markovian drift family (MDH). MDH groups encoders that expose a single sequentially
updated or recency-bounded state rather than an order-invariant profile or an explicitly long-horizon task-
facing representation. For recurrent members, the generic first-order update is
z(ti) u = fRec  z(ti−1) u , xi−1; ρ  + ξ(ti), (25)
where ρ parameterizes the effective update or recency behavior and ξ(ti) denotes an optional perturbation
term. The family label refers to the form of the exposed state, not to a claim that the underlying user process
itself is Markovian.
GRU-B (MDH instantiation). We instantiate the recurrent form with a gated recurrent unit over the ordered
interaction-block embeddings {xi}L i=1. Given hi−1 ∈ Rd and xi ∈ Rd,
ri = σ(Wrxi + Urhi−1), ui = σ(Wuxi + Uuhi−1), (26)
˜hi = tanh(Whxi + Uh(ri ⊙ hi−1)) , (27)
hi = (1 − ui) ⊙ hi−1 + ui ⊙ ˜hi, z(tL+1) u ≡ hL. (28)
35

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Here, σ(·) is the logistic sigmoid, ⊙ denotes element-wise multiplication, and {W·, U·} are learned parameters.
GRU-B therefore realizes the recurrent MDH form by compressing the processed prefix into one evolving
hidden state.
EBNR (MDH-aligned). EBNR encodes click-order information through a recurrent user encoder and ranks
candidates by matching the resulting user embedding to candidate-news representations. In its recurrent
user-modeling form, each clicked news item di is represented by ni ∈ Rd and the history state evolves as
hi = GRU(hi−1, ni), u ≡ hL. (29)
For candidate news item d with representation n(d),
s(u, d) =u⊤n(d). (30)
A probabilistic implementation may use ˆy(u, d) =σ(s(u, d)) with observed clicks and sampled or impression-
based non-clicks. For our operational grouping, EBNR belongs to MDH because its downstream user repre-
sentation is produced by a single recurrently updated history state.
Long-horizon state family (LDH). LDH groups encoders whose task-facing state can retain or directly
aggregate information across the observed prefix through attention, sequence kernels, or long-range state-
space dynamics. In the notation of Section 3.1, the generic form is
z(ti) u = fLDH  {xj}i−1 j=1; KΘ  , (31)
where KΘ denotes the learned long-horizon sequence operator. A common kernelized realization is
z(ti) u = i−1 ∑
j=1
KΘ(ti, tj, x1:i−1) ψΘ(xj). (32)
The operator may be content-dependent, as in attention, or induced implicitly by state-space dynamics.
Unrolling a recurrent state-space model yields an explicit lag kernel over the full prefix. We group these
models here by that long-horizon sequence property. The grouping is used to organize comparisons rather
than to define disjoint architectural classes.
D-FM Attention (LDH-aligned control). We use a decay-modulated causal-attention control inspired
by forgetting-based attention (Lin et al., 2025). The control below uses a lag penalty; FoX itself uses data-
dependent forgetting, so this equation describes our adapted control. Given qi = WQxi, kj = WKxj, and
vj = WVxj, the causal logits are
ℓij = q⊤ i kj√ d − γ(ti − tj), j < i, (33)
with
αij = exp(ℓij ) ∑i−1 q=1 exp(ℓiq) , z(ti) u = i−1 ∑ j=1 αijvj. (34)
This is LDH-aligned because the task-facing state aggregates the observed prefix through a learned attention
kernel with explicit temporal decay.
Discretized SSM-B (single-timescale LDH control). Our ordinary linear state-space control supplies
one recurrent state. SS4Rec (Xiao et al., 2025) uses a richer time- and relation-aware state-space design; the
following equations specify the control evaluated here. Let mi ∈ Rdm denote the latent state and xi ∈ Rd the
current input:
mi = Ami−1 + Bxi, z(ti+1) u = Cmi. (35)
Unrolling the recurrence gives
mi = Aim0 +
i
∑
j=1
A i−jBxj. (36)
Thus, although the implementation is recurrent, the exposed state contains a full-prefix lag expansion through
powers of A. We place this baseline in LDH because the comparison of interest is its induced long-horizon
kernel, while it still exposes only one temporal state and one retention mechanism.
36

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Tri-SSM-B (three-branch LDH control). Tri-SSM-B extends the ordinary SSM recurrence to three indepen-
dently parameterized parallel branches while retaining the same schema-normalized input and corresponding
downstream fusion/readout organization used for the PerTIDE comparison. For r ∈ {1, 2, 3},
m(r) i = Arm(r) i−1 + Brxi. (37)
Unlike PerTIDE, the branches use the same generic SSM transition form and are not assigned explicit long-,
short-, or episodic spectral maps. Tri-SSM-B therefore controls for schema input and parallel three-branch
state organization while leaving trace-specific retention design absent.
Transformer-style LDH baselines (NRMS / FastFormer-PLM / MINER).These models construct contextu-
alized history representations through attention-style interactions over the observed prefix. Schematically,
Attn(Q, K, V) =softmax

QK⊤
√
d
!
V, MHSA (X) =Concat(head1, . . . , headH)WO, (38)
where X = [x1; . . . ;xi−1] and
headh = Attn

XW(h) Q , XW(h) K , XW(h) V  .
A single task-facing user state can then be obtained through additive attention pooling:
αj =
exp(v⊤ tanh(Wx′ j))
∑i−1 q=1 exp(v⊤ tanh(Wx′q)) , z(ti) u = i−1 ∑ j=1 αjx′ j, (39)
where x′ j denotes the contextualized sequence representation. NRMS uses self-attentive history encoding
followed by pooling, FastFormer-PLM uses additive/global-context attention to construct contextualized
representations, and MINER extracts multiple interest representations from long histories before candidate
matching. We group these models under LDH because their task-facing representations are constructed from
learned interactions over extended history rather than an order-invariant profile or a single recency-bounded
state.
F.2 Baseline Personalized Models
PENS-NRMS Injection-Type 1. The PENS framework (Ao et al., 2021) generates personalized headlines
by conditioning on a user representation together with the input news article. In this variant, the user
representation is produced by NRMS (Wu et al., 2019b), whose news encoder represents article content
and whose user encoder applies self-attention over interacted news. Injection-Type 1 initializes the decoder
hidden state with the resulting user representation, allowing personalization to influence generation from the
beginning of decoding.
PENS-NRMS Injection-Type 2. This variant uses the same NRMS user representation but introduces it
through the decoder attention mechanism rather than the initial hidden state. The user representation therefore
modulates attention over the source article during generation.
PENS-NAML Injection-Type 1. NAML (Wu et al., 2019a) constructs news representations from multiple
content views, including title, body, and category information, and aggregates interacted news into a user
representation. In PENS Injection-Type 1, this representation initializes the decoder hidden state.
PENS-EBNR Injection-Type 1. EBNR (Okura et al., 2017) produces a user representation with a recurrent
encoder over browsing history. Under PENS Injection-Type 1, this user representation initializes the decoder
and thereby conditions generation from its initial state.
PENS-EBNR Injection-Type 2. This configuration uses the same recurrent EBNR user representation but
introduces it through the decoder attention mechanism, allowing the user state to modulate source-side
attention during generation.
37

KDM LAB / LCS2 RESEARCH MANUSCRIPT
General Then Personal (GTP). General Then Personal (GTP) (Song et al., 2023) follows a two-stage per-
sonalized headline-generation pipeline. A general encoder–decoder first learns content-focused headline
generation, after which a headline customizer incorporates a user-specific control representation. GTP further
uses Information Self-Boosting (ISB) to recover relevant article information during customization and Masked
User Modeling (MUM) to regularize the use of user representations.
Signature Phrase. Signature Phrase personalization (Cai et al., 2023) represents a user’s reading history
through a compact set of learned phrases. These phrases act as a dynamic profile of higher-level interests and
are used to condition personalized headline generation while retaining grounding in the source article.
MovieLens-1M baselines. For MovieLens-1M, we organize predictive recommendation baselines using
the same operational state-family grouping introduced in Section 3.1 and Appendix F.1. Each user history is
an ordered prefix τu 1:i−1 = (vu 1, . . ., vu i−1), where vu j denotes the movie interacted with by user u at timestep j.
Each model produces a candidate score s(u, c) for movie candidate c, and all candidates are ranked under the
same one-positive plus sampled-negative evaluation protocol. The PAH/MDH/LDH labels below describe
the exposed history-state form used for comparison; they do not imply mutually exclusive assumptions about
the underlying user process.
BPR-MF (PAH-aligned). BPR-MF is used as a static profile-based matrix-factorization baseline. It assigns
each user u a persistent embedding pu ∈ Rd and each candidate c an item embedding qc ∈ Rd:
s(u, c) =p⊤ u qc.
The pairwise ranking objective is
LBPR = − ∑
(u,i+,i−)
log σ

s(u, i+) − s(u, i−)  .
Its exposed user representation is persistent and order-insensitive rather than computed from the ordered
prefix, so we place BPR-MF in the PAH family.
GRU4Rec (MDH instantiation). GRU4Rec is used as a recurrent sequential recommendation baseline. Given
item embeddings {qvj }j<i,
hj = GRU(hj−1, qvj ), z(ti) u = hi−1,
and candidates are scored by
s(u, c) =z(ti)⊤ u qc.
GRU4Rec is an MDH instantiation because its task-facing state is a single recurrently updated representation
obtained from the previous hidden state and the current interaction.
Caser (MDH-aligned local-window baseline). Caser encodes a bounded recent interaction window as
Xi = [qvi−L; . . . ;qvi−1 ],
then applies horizontal and vertical convolutional filters:
z(ti) u = MLP([Convh(Xi); Convv(Xi); pu]) , s(u, c) =z(ti)⊤ u qc.
Caser is not a recurrent realization of Eq. (25); we place it in the MDH family operationally because its
task-facing sequential representation is dominated by a bounded recent-history window rather than an
order-invariant profile or an explicit long-horizon sequence operator.
S3Rec (LDH-aligned). S3Rec uses a self-supervised Transformer-style sequence encoder:
Hi = SeqEncθ

[qv1 + p1; . . . ;qvi−1 + pi−1]

, z(ti) u = Readout(Hi),
with
s(u, c) =z(ti)⊤ u qc.
We place S 3Rec in LDH because the exposed recommendation state is constructed from a self-attentive
representation of the observed prefix.
38

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Diff4Rec (LDH-aligned). Diff4Rec uses curriculum-scheduled diffusion augmentation for sequential recom-
mendation. Its recommendation stage scores candidates from a sequence representation:
z(ti) u = SeqEncθ(τu 1:i−1), s(u, c) = fθ(z(ti) u , qc).
For our operational grouping, Diff4Rec is LDH-aligned because candidate prediction is conditioned on a
representation of the extended interaction prefix rather than a static user profile or bounded local state.
SASRec (LDH-aligned). SASRec (Kang and McAuley, 2018) applies causal self-attention over the ordered
interaction prefix:
Hi = CausalSelfAttnθ

[qv1 + p1; . . . ;qvi−1 + pi−1]

, z(ti) u = Readout(Hi),
s(u, c) =z(ti)⊤ u qc.
We place SASRec in LDH because its task-facing state is constructed through a learned attention operator over
the observed prefix.
BERT4Rec (LDH-aligned). BERT4Rec learns contextualized item representations through masked-item
prediction with a bidirectional Transformer:
Hi = BiTransformerθ

[qv1 + p1; . . . ;qvi−1 + pi−1]

, z(ti) u = Readout(Hi).
Candidate movies are scored as
s(u, c) =z(ti)⊤ u qc.
We place BERT4Rec in LDH because the downstream recommendation state is obtained from a contextualized
representation of the observed interaction sequence.
Mamba4Rec (LDH-aligned state-space baseline). Mamba4Rec uses selective state-space sequence modeling:
mj = Ajmj−1 + Bjqvj, z(ti) u = Ci−1mi−1, s(u, c) =z(ti)⊤ u qc.
The recurrent implementation uses learned state-space dynamics to retain long-range dependence over the
processed prefix. We therefore group Mamba4Rec under LDH according to its long-horizon sequence operator,
while noting that the PAH/MDH/LDH families are operational rather than disjoint architectural classes.
SSD4Rec (LDH-aligned state-space baseline). SSD4Rec (Zhang et al., 2026) uses bidirectional structured
state-space duality blocks for variable-length recommendation sequences. Its sequence representation incor-
porates forward and backward processing of the observed history; it should not be identified with a single
forward linear recurrence. We group it under LDH because of its sequence-level history modeling. The
evaluated comparison concerns this architecture versus PerTIDE’s action-gated, trace-specific updates, rather
than a claim that all state-space recommenders expose the same computation.
G Measuring Personalization
G.1 Motivation
EGISES (Vansh et al., 2023) measures how insensitive a personalized summarizer is to user subjectivity, where
lower values indicate less insensitivity and therefore better personalization. Following this idea, PerSEval
(Dasgupta et al., 2024) evaluates whether a model changes its generated summary when the target user’s
expected summary changes, while also penalizing poor reference agreement. We use the notation di for a
document, uij for the expected summary of user j for document di, and ˆsij for the model-generated summary
for the same user-document pair. Let Ui be the set of users who provide references for document di, and let
σ(·, ·) be a distance function between two summaries.
39

KDM LAB / LCS2 RESEARCH MANUSCRIPT
The summary-level degree of responsiveness, denoted as DEGRESS, compares two quantities: the diver-
gence between user references and the divergence between corresponding model outputs. For user j and
document di, it is defined as
Dij = 1 |Ui| |Ui| ∑ k=1 min(Xijk , Yijk ) +ϵ max(Xijk , Yijk ) +ϵ , (40)
where
Xijk = wu ijk σ(uij, uik), Yijk = ws ijk σ(ˆsij, ˆsik). (41)
Here, Xijk measures the distance between the expected summaries of users j and k, and Yijk measures the
corresponding distance between the model-generated summaries. The weights wu ijk and ws ijk are softmax-
normalized document-relative weights. They control how much each user-pair comparison contributes to the
final responsiveness score.
The system-level DEGRESS score is
D(M) = 1 |D| |D| ∑ i=1 1 |Ui| |Ui| ∑ j=1 Dij. (42)
A low value indicates that the model does not respond sufficiently to user-specific reference variation. A high
value indicates stronger responsiveness to different user preferences.
G.2 PerSEval Formulation
DEGRESS only measures responsiveness. It does not penalize a model that produces personalized but
inaccurate summaries. PerSEval addresses this limitation by multiplying DEGRESS with an accuracy-sensitive
penalty. For user j and document di, the summary-level PerSEval score is
Pij = Dij · Eij, (43)
where Eij is the effective DEGRESS penalty factor:
Eij = 1 − 1 1 + 10α exp(−10βQij ) , α ≥ 3, β ≥ 1. (44)
The penalty input Qij combines document-level accuracy loss and user-level accuracy inconsistency:
Qij = Ai + Cij. (45)
The document-level accuracy penalty is
Ai = 1
1 + 10γ exp

−10 · a∗ i 1−a∗ i +ϵ  , γ ≥ 4, (46)
where
a∗ i = min j∈Ui aij. (47)
Here, aij is the distance-based accuracy score for ˆsij against the corresponding user reference uij, and a∗ i is the
best document-level accuracy term under the chosen distance convention.
The accuracy-inconsistency penalty is
Cij = 1
1 + 10γ exp

−10 ·
aij −a∗ i
¯ai−a∗ i +ϵ
 , γ ≥ 4, (48)
where
¯ai = 1 |Ui| |Ui| ∑ j=1 aij. (49)
40

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Thus, Ai penalizes poor best-case accuracy, while Cij penalizes inconsistency across user-specific generations
for the same document.
The system-level PerSEval score is
P(M) = 1 |D| |D| ∑ i=1 1 |Ui| |Ui| ∑ j=1 Pij. (50)
The score lies in [0, 1], with higher values indicating better personalization under the chosen reference-distance
convention, and remains bounded by the system-level DEGRESS score.
G.3 PSE Metrics
We use three PerSEval variants by changing the distance or similarity function used inside the formulation.
PSE-SU4. This variant uses ROUGE-SU4 as the base comparison function. ROUGE-SU4 measures
overlap through unigrams and skip-bigrams, where a skip-bigram is an ordered word pair with up to
four skipped words between the pair. We convert its F1 similarity to the required distance, σ(G, R) =
1 − ROUGE-SU4F1(G, R), as in PerSEval (Dasgupta et al., 2024).
PSE-JSD. This variant uses Jensen-Shannon divergence between the normalized unigram or n-gram
distributions of the generated and reference summaries. For distributions P and Q,
JSD(P∥Q) =1 2KL(P∥M) +1 2KL(Q∥M), M = 1 2 (P + Q). (51)
We set σ(G, R) =JSD(PG∥PR) to obtain PSE-JSD.
PSE-METEOR. This variant uses METEOR as the base similarity score. METEOR aligns generated and
reference unigrams using exact, stem, synonym, and paraphrase matches, then combines precision, recall, and
a fragmentation penalty. Since PerSEval requires a distance, we use
σ(G, R) =1 − METEOR(G, R). (52)
This gives PSE-METEOR.
H Prediction Accuracy Metrics
(i) nDCG@5 and HR@10. We report normalized Discounted Cumulative Gain (nDCG) at cutoffs K ∈ {5, 10}
to evaluate ranking quality while emphasizing higher-ranked items. For each query instance with a ranked list
of candidates, let reli denote the relevance of the item at rank i (binary relevance in our setup). We compute
DCG@K =
K
∑
i=1
2reli − 1
log2(i + 1) , nDCG@K = DCG@K IDCG@K, (53)
where IDCG@K is the maximum possible DCG@K achievable by an ideal ordering for that instance. nDCG
rewards higher placement of relevant items. HR@10 is the fraction of instances whose positive target occurs in
the top ten and does not distinguish positions within that set. Under the one-positive protocol, HR@K equals
Recall@K. All ranking scores in the result tables are multiplied by 100.
(ii) MRR. We report Mean Reciprocal Rank (MRR) to measure how early the first relevant item appears in
the ranked list. For each instance, let rank⋆ be the rank position of the first relevant item; the reciprocal rank is
1/rank⋆. The aggregate metric is
MRR = 1 N N ∑ n=1 1 rank⋆ n , (54)
where N is the number of evaluation instances. MRR heavily rewards placing a relevant item at the very top
and is therefore sensitive to early precision.
(iii) Recall@K. We report Recall at cutoffK (denoted Recall@K) to quantify whether at least one relevant
item is retrieved among the top- K predictions. With binary relevance and (typically) one target item per
instance, Recall@K reduces to an indicator of whether the target appears in the top-K list:
Recall@K = 1 N N ∑ n=1 I  rank⋆ n ≤ K  , (55)
where I[·] is the indicator function. Larger Recall@K indicates higher top-K hit rate, complementing MRR and
nDCG by focusing on retrieval coverage rather than graded ordering.
41

KDM LAB / LCS2 RESEARCH MANUSCRIPT
I Reference-Based Content Metrics
(i) ROUGE-2. ROUGE-2 measures bigram overlap between a generated text y and a reference text r using
recall-oriented matching of contiguous 2-grams. Let G2(·) denote the set of distinct bigram types, and let
countx(g) be the count of bigram g in text x. The ROUGE-2 recall is
ROUGE-2 = ∑g∈G2(r) min

county(g), countr(g)

∑g∈G2(r) countr(g) . (56)
Higher values indicate that the generation covers more of the reference bigram content.
(ii) ROUGE-L. ROUGE-L evaluates sequence-level overlap via the Longest Common Subsequence (LCS),
capturing in-order matching without requiring contiguity. Let LCS(y, r) be the length of the LCS between y
and r, and let |y|, |r| be token lengths. Define LCS-based precision and recall as
PLCS = LCS(y, r) |y| , RLCS = LCS(y, r) |r| . (57)
ROUGE-L is commonly reported as an F-measure:
ROUGE-L = (1 + β2)PLCSRLCS
RLCS + β2PLCS , (58)
where β controls the relative weight of recall versus precision (often set to favor recall in summarization).
(iii) ROUGE-SU4. ROUGE-SU4 measures overlap of skip-bigrams with a maximum skip distance of 4,
together with unigrams (the “U” component). A skip-bigram is any ordered pair of tokens (wi, wj) such that
1 ≤ j − i ≤ 5 (i.e., up to four skipped tokens between them). Let GSU4(x) be the set of distinct unigram and
SU4 skip-bigram types from text x. The ROUGE-SU4 recall is
ROUGE-SU4 = ∑g∈GSU4(r) min

county(g), countr(g)

∑g∈GSU4(r) countr(g) . (59)
This metric is more permissive than ROUGE-2 because it credits in-order matches even when tokens are
separated by a small gap.
(iv) METEOR. METEOR aligns generated and reference tokens using exact matches and (optionally)
linguistic matches (e.g., stem/synonym), then computes a harmonic mean of unigram precision and recall
with a fragmentation penalty for disordered alignments. Let m be the number of matched unigrams under the
alignment, and let |y|, |r| be token lengths. Define
P = m |y| , R = m |r| , Fα = PR αP + (1 − α)R , (60)
where α weights precision versus recall (commonly set to emphasize recall). Let c be the number of matched
“chunks” (contiguous sequences of matches in the aligned order). The penalty is
Pen = γ
 c
m
θ
, (61)
and the final METEOR score is
METEOR = (1 − Pen) Fα, (62)
with γ, θ controlling the strength of the fragmentation penalty.
(v) BLEU-4. BLEU-4 evaluates n-gram precision up to n = 4 with a brevity penalty to discourage overly
short outputs. Let pn denote the modified precision for n-grams, computed using clipped counts against the
reference. BLEU-4 is
BLEU-4 = BP · exp

4
∑
n=1
wn log pn
!
, (63)
where typically wn = 1 4. The brevity penalty is
BP =
(
1, |y| > |r|,
exp

1 − |r| |y|  , |y| ≤ |r|. (64)
42

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Higher BLEU-4 indicates greater n-gram precision while accounting for length adequacy via BP.
(vi) BERTScore. BERTScore measures semantic similarity between a generated text y = {yi}m i=1 and a
reference text r = {rj}n j=1 by aligning contextual token embeddings from a pretrained encoder. Let h(yi)
and h(rj) denote the contextualized embeddings, and let sij = cos(h(yi), h(rj)) be their cosine similarity.
BERTScore precision and recall are computed via soft token matching:
PBS = 1 m m ∑ i=1 max 1≤j≤n sij, RBS = 1 n n ∑ j=1 max 1≤i≤m sij, (65)
and combined into an F-score
FBS = 2PBSRBS PBS + RBS . (66)
Higher BERTScore indicates stronger semantic alignment between the generation and the reference, even
when surface n-gram overlap is low.
J Detailed Results And Additional Analysis
J.1 Efficiency And Deployment Cost
Table 11: Runtime and deployment costs for PerTIDE. We report approximate resource figures forPerTIDE
and comparison systems. The action-on-item encoder supports online updates from cached user state without
replaying the full history, whereas prompted LLM personalization conditions on history through the inference
context. Numbers correspond to d=768, |Q|=4, and, for generation, a pretrained DistilGPT2 decoder condi-
tioned by a learned K=8 prefix. The final two decoder blocks and final layer normalization are fine-tuned
during generation training; the remaining decoder parameters stay fixed. Latency, throughput, VRAM, FLOPs,
and training time are source estimates, not a matched hardware benchmark; the per-user cache is computed
directly from the state dimensions.
Metric PerTIDE (Ours) Single-scale encoder Prompted LLM (ICL)
A. Parameter and Memory Footprint
Trainable parameters (encoder only) ∼154.36M ∼130–145M 0
Decoder contextualization parame-
ters
∼8.27M (UFI) / ∼10.63M (UGI) task-dependent 0
Encoder + contextualization parame-
ters
∼162.63M (UFI) / ∼164.99M
(UGI)
∼130–145M + context 0
Decoder parameters fine-tuned for
generation
∼14.18M (last 2 blocks + final
LN)
same protocol if DistilGPT2 is
used
0 (ICL)
Pretrained decoder backbone de-
ployed
∼82M (DistilGPT2) ∼82M (if used) 7B–32B
Deployable parameters (generation) ∼245–247M ∼212–227M + context 7B–32B
Per-user cached state 4 × 768 floats (≈12 KiB) history replay or single state 0
Peak VRAM (predictive inference) ∼1.1–1.3 GB ∼1.0–1.2 GB ≥18 GB
Peak VRAM (generative inference) ∼1.6–1.9 GB ∼1.5–1.8 GB ≥28 GB
B. History Dependence and Online Updates
History dependence at inference cached state only (no replay) windowed / cached state / re-
play
full prompt history
Online update cost per interaction O(d2) (three trace updates + fu-
sion)
O(d2) –
State refresh frequency every timestep every timestep –
PerTIDE supports incremental history updates with a fixed cache: three 768-dimensional traces and the
previous 768-dimensional task-ready state require 12 KiB per user in FP32. The cache does not grow with
history length. Each new event updates it directly, and subsequent predictive or generative requests reuse the
retained state. This is the deployment benefit of the recurrence even though the encoder has more parameters
than the single-scale comparison.
Generation uses DistilGPT2 with an eight-token contextual prefix and partial decoder tuning, whereas
the evaluated 7B–32B LLMs receive histories through prompting. The analytical or approximate resource
estimates in Table 11 describe expected costs; they are not measurements from a matched hardware benchmark.
43

KDM LAB / LCS2 RESEARCH MANUSCRIPT
The fixed cache is determined by the architecture; realized throughput and latency additionally depend on
implementation, hardware, and request lengths.
44

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Table 12: Approximate serving and training resources. Continuation of the resource estimates in Appendix J.1,
Table 11. These estimates are not a matched hardware benchmark.
Metric PerTIDE Single-scale encoder Prompted LLM
C. Predictive Serving Cost
Latency per sample (end-to-end) ∼2–6 ms ∼2–5 ms ∼20–60 ms
Throughput (samples/sec) ∼160–420 ∼180–450 ∼20–60
FLOPs per sample ∼3.8×109 ∼2.5–3.2×109 ≥1×1011
D. Generative Serving Cost
Contextualization UFI / UGI learned prefix concat / none ICL prompt
Personalization context injected 8 learned prefix tokens 0–1 learned tokens 130–250 history to-
kens
Generation length task-dependent task-dependent task-dependent
End-to-end latency per sample 0.4–3 s 0.4–3 s 15–160 s
FLOPs per output (est.) ∼6.1×1010 ∼6.0×1010 ∼1.6×1012
E. Training Cost
Training GPU-hours ∼22 ∼18–30 –
Decoder backbone fine-tuning Partial (last 2 blocks + final LN) task-dependent None (ICL)
45

KDM LAB / LCS2 RESEARCH MANUSCRIPT
J.2 Full Predictive Personalization Results
J.2.1 MovieLens-1M Recommendation
Table 13: MovieLens movie recommendation under action-on-item preference flow. We compare PerTIDE
against task-native recommendation baselines on next-item ranking. Baselines expose profile, recurrent, or
long-horizon history states, while PerTIDE uses schema-normalized action evidence with multi-timescale
persistence. Point estimates are means under the paired-bootstrap evaluation in Appendix E; ± denotes
standard deviation over three uniformly sampled 25% evaluation subsets for PerTIDE variants.
Regime Model MRR nDCG@10 HR@10
PAH BPR-MF 6.50 6.12 12.81
MDH
GRU4Rec 12.76 16.42 29.01
Caser 13.54 19.21 28.92
Diff4Rec 12.02 15.72 22.38
LDH
S3Rec 10.62 13.67 19.21
SASRec 13.20 19.96 30.23
BERT4Rec 14.41 20.22 31.71
Mamba4Rec 14.56 19.83 31.24
SSD4Rec 14.95 20.31 31.52
MTSH
PerTIDE w/o AC 15.21 ± 0.93 19.53 ± 1.12 28.16 ± 1.26
PerTIDE w/o CR 17.05 ± 0.95 19.08 ± 1.43 27.85 ± 0.56
PerTIDE 17.31 ± 0.65 23.78 ± 0.84 33.20 ± 1.17
PerTIDE reaches 17.31/23.78/33.20 MRR/nDCG@10/HR@10. Compared with SSD4Rec, the gains are
2.36/3.47/1.68 points (Table 13). BERT4Rec has the strongest baseline HR@10, 31.71, while SSD4Rec leads
baseline MRR and nDCG. The full model exceeds both. Removing action conditioning gives 15.21 MRR
and 28.16 HR@10; removing command readout gives 17.05/19.08/27.85 across the three metrics. These
interventions connect the ranking advantage to how evidence enters and is consumed, beyond changing the
history-model family.
J.2.2 MIND News Recommendation
Table 14: Action-on-item encoder performance on MIND. We compare task-native history encoders and
schema-matched controls with PerTIDE on sequential ranking. AC denotes action-conditioned evidence
entry, and CR denotes command-conditioned readout. Point estimates are means under the paired-bootstrap
evaluation in Appendix E; ± denotes standard deviation over three uniformly sampled 25% evaluation subsets
for PerTIDE variants.
Regime Model MRR nDCG@5 HR@10
PAH
NAML 32.75 35.66 41.40
PLM-NR 35.39 38.71 44.38
Mean Pooling-B (ours) 29.43 31.22 33.17
Max Pooling-B (ours) 28.32 31.16 32.41
MDH EBNR 31.26 32.18 39.04 GRU-B (ours) 32.64 35.17 37.92
LDH
NRMS 33.25 36.28 41.98
MINER 36.60 40.20 46.30
Fastformer+PLM-NR 35.91 39.16 45.03
D-FM Attention (ours) 32.17 34.56 36.21
Discretized SSM (ours) 35.14 38.53 37.27
Tri-SSM-B (ours) 42.53 43.84 46.33
MTSH
PerTIDE w/o AC (ours) 40.13 ± 2.43 43.75 ± 1.37 46.35 ± 1.16
PerTIDE w/o CR (ours) 42.51 ± 2.16 46.44 ± 1.75 51.06 ± 1.56
PerTIDE (ours) 46.65 ± 2.24 49.21 ± 1.64 55.48 ± 1.14
The task-native comparison spans profile, recurrent, attention, and state-space encoders (Table 14). PerTIDE
exceeds MINER by 10.05/9.01/9.18 MRR/nDCG@5/HR@10 points. The more controlled same-input compari-
son in main-text Table 2 gives gains of 4.12/5.37/9.15 over Tri-SSM-B. Holding the trajectory representation
46

KDM LAB / LCS2 RESEARCH MANUSCRIPT
and three-branch organization fixed therefore leaves a measurable advantage for the proposed retention
design. The action and readout ablations additionally reduce MRR from 46.65 to 40.13 and 42.51, respectively.
J.2.3 PENS Next-News Prediction
Table 15: Structured news prediction on PENS-Structured. We report same-user next-news ranking under
the action-on-item schema. Baselines are grouped by the exposed history-state assumption in Section 3. All
values are on a 0–100 scale.
Regime Model MRR nDCG@5 nDCG@10 HR@10
MDH EBNR 2.65 1.82 2.45 4.87
PAH NAML 1.29 0.43 0.81 2.01
LDH NRMS 1.18 0.39 0.74 1.92
LDH TrRMIo 8.02 7.85 8.53 12.77
LDH LSTUR 9.04 8.21 10.16 12.93
LDH MINER 5.17 4.71 5.61 9.77
LLM DeepSeek-32B 1.31 0.28 0.64 1.53
LLM Qwen2.5-32B 1.24 0.26 0.59 1.47
MTSH PerTIDE 9.94 9.88 11.58 18.32
PerTIDE reaches 9.94 MRR, 9.88 nDCG@5, 11.58 nDCG@10, and 18.32 HR@10 (Table 15). Relative to LSTUR,
gains are 0.90 MRR, 1.42 nDCG@10, and 5.39 HR@10 points. With one positive target per candidate set, HR@10
measures how often that target appears anywhere in the top ten; it does not assess its order within that set.
These histories also support headline generation below, providing a common domain in which to test both
consumers.
J.3 Retention Probes And Trace Complementarity
Table 16: Temporal regime-specific trace specialization. Controlled L-Tr, S-Tr, and E-Tr probes emphasize
persistent, recent, and event-local evidence. Scores are MRR/nDCG@10 on the 0–100 scale. Bold denotes the
overall best result; underlining marks the strongest isolated PerTIDE trace in each regime. The full model
leads every reported probe; the long trace narrowly leads the short trace on MovieLens S-Tr.
Dataset Family Model / Variant L-Tr S-Tr E-Tr
MovieLens
Baseline
Mamba4Rec 26.43/29.38 26.12/28.87 25.72/28.31
GRU4Rec 24.17/27.32 23.65/26.58 22.13/24.71
SASRec 25.82/28.16 25.85/28.45 25.17/27.91
PerTIDE
PerTIDE-L 27.31/29.96 27.18/29.35 25.83/28.77
PerTIDE-S 25.21/28.64 27.13/29.22 22.16/24.84
PerTIDE-E 22.19/24.08 22.75/25.04 27.14/30.36
PerTIDE-L+S+E 29.33/32.17 29.04/31.85 29.12/32.09
MIND
Baseline
NAML 46.21/51.23 46.25/51.35 45.32/49.18
EBNR 47.44/52.25 48.32/53.17 44.19/48.79
LSTUR 49.31/54.41 48.93/53.86 45.64/49.84
PerTIDE
PerTIDE-L 49.54/54.78 48.65/53.22 47.32/51.66
PerTIDE-S 49.21/53.94 50.07/55.35 48.65/52.81
PerTIDE-E 47.31/51.26 47.13/51.06 50.35/55.84
PerTIDE-L+S+E 52.75/59.32 51.76/57.92 51.34/57.56
Target-fixed probes place preference-similar evidence in persistent (L-Tr), recent (S-Tr), or short-burst
(E-Tr) configurations. Table 16 gives the complete scores. On MIND, the intended isolated trace leads each
regime. On MovieLens S-Tr, the long trace narrowly exceeds the short trace, 27.18/29.35 versus 27.13/29.22
MRR/nDCG@10. The full model leads all six dataset–regime combinations, supporting the use of the traces
together even where isolated specialization overlaps. The full L+S+E model is strongest across all reported
metrics on MIND, MovieLens, and PENS generation (Table 17). A trace can make a larger contribution in
47

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Table 17: Trace-subset ablation for schema-normalized evidence persistence. We ablate long-term (L),
short-term (S), and episodic (E) persistence channels individually and in combination. Recommendation
results are reported on MIND and MovieLens-1M, and personalized summarization is reported on PENS. Best
results are bolded.
Variant MIND Recommendation ML-1M Recommendation PENS Summarization
MRR nDCG@5 HR@10 MRR nDCG@10 HR@10 PSE-JSD PSE-SU4 PSE-METEOR
L only 40.41 43.75 46.13 12.31 16.15 20.34 0.231 0.095 0.107
S only 37.65 41.32 44.24 12.47 16.62 20.81 0.238 0.106 0.111
E only 24.18 27.73 31.23 10.18 13.17 18.54 0.076 0.042 0.045
L + S 41.26 43.95 46.72 14.17 18.44 22.11 0.264 0.143 0.182
L + E 40.45 43.82 46.44 14.03 18.07 22.74 0.246 0.103 0.108
S + E 38.26 42.34 45.07 13.43 17.18 21.67 0.093 0.062 0.077
L + S + E 46.65 49.21 55.48 17.31 23.78 33.20 0.366 0.341 0.355
combination than its isolated performance suggests. E alone reaches 24.18 MRR on MIND, while adding it to
L+S raises MRR from 41.26 to 46.65. On PENS, L+S reaches 0.264 PSE-JSD and 0.182 PSE-METEOR; the full
model reaches 0.366 and 0.355. The weakest isolated branch can therefore supply information useful to the
fused state.
This contribution depends on the combination. PENS S+E gives 0.093/0.062/0.077 in the three PSE metrics,
below S alone at 0.238/0.106/0.111. The full model’s advantage demonstrates measured complementarity
under the evaluated training setup, rather than proving that every extra trace helps or that the learned
coordinates recover distinct latent interests.
J.4 Generation And Reference Agreement
J.4.1 PENS Personalized Headlines
Table 18: Command-conditioned personalized headline generation on PENS. We compare prompted LLMs,
task-native personalized generators, schema-matched history controls, and PerTIDE. AC denotes action-
conditioned evidence entry, CR denotes command-conditioned readout, and UFI/UGI denote User Fused/-
Gated Injection. Point estimates are means under the paired-bootstrap evaluation in Appendix E; ± denotes
standard deviation over three uniformly sampled 25% evaluation subsets for PerTIDE variants.
Category Model PSE-JSD PSE-SU4 PSE-METEOR
LLMs (2-shot)
LLaMA-13B 0.227 0.078 0.081
DeepSeek-14B 0.248 0.094 0.097
Gemini-2.5-Flash 0.222 0.104 0.124
DeepSeek-R1-32B 0.263 0.125 0.174
Qwen-2.5-32B 0.162 0.103 0.115
Prompt-Chaining Mistral-7B 0.072 0.026 0.023 DeepSeek-14B 0.078 0.028 0.024
PAH
Signature-Phrase 0.017 0.015 0.016
PENS-NAML-T1 0.021 0.014 0.016
MaxPool-B 0.008 0.005 0.005
MDH
PENS-EBNR-T1 0.015 0.010 0.011
PENS-EBNR-T2 0.011 0.008 0.009
GRU-B 0.021 0.018 0.019
LDH
GTP 0.024 0.017 0.019
Discretized SSM 0.037 0.032 0.031
D-FM Attention-B 0.028 0.019 0.025
PENS-NRMS-T1 0.015 0.011 0.011
PENS-NRMS-T2 0.008 0.007 0.007
MTSH
PerTIDE w/o AC 0.314 ± 0.023 0.271 ± 0.007 0.292 ± 0.006
PerTIDE w/o CR 0.317 ± 0.024 0.276 ± 0.005 0.284 ± 0.008
PerTIDE (UFI) 0.332 ± 0.019 0.289 ± 0.009 0.303 ± 0.003
PerTIDE (Full; UGI) 0.366 ± 0.011 0.341 ± 0.002 0.355 ± 0.005
UGI reaches 0.366/0.341/0.355 PSE-JSD/PSE-SU4/PSE-METEOR, exceeding UFI’s 0.332/0.289/0.303 and
48

KDM LAB / LCS2 RESEARCH MANUSCRIPT
the listed two-shot LLMs (Table 18). Its gains over UFI are 0.034/0.052/0.052, supporting user-conditioned
modulation before decoder injection. The compact decoder can thus use a learned history state effectively
across the reported personalization metrics. Training differs from the two-shot LLM protocol, so these scores
compare the complete evaluated systems.
J.4.2 Reference Overlap And Human Similarity Ratings
Table 19: Reference agreement for command-driven headline generation. Automatic metrics measure
reference overlap or semantic similarity; HJ is the six-point reference-similarity rating described in Appendix K.
Category Model RG-SU4 BLEU-4 BScore HJ
Specialized (Personalized)
PENS-NRMS-T2 13.64 4.48 86.13 2.95
GTP-TrRMIo 21.91 10.31 88.53 2.44
SP-Individual 19.54 8.90 86.61 2.86
LLMs (2-shot history)
LLaMA-13B 18.31 11.85 88.76 3.05
DeepSeek-14B 19.57 12.68 89.43 3.03
DeepSeek-32B 29.42 19.31 90.87 3.12
Qwen-2.5-32B 19.22 14.31 89.17 3.04
MTSH PerTIDE-Full 41.32 27.64 90.84 3.21
The improvement extends beyond PerSEval to other forms of reference agreement (Table 19). PerTIDE
reaches 41.32 RG-SU4 and 27.64 BLEU-4, compared with DeepSeek-32B’s 29.42 and 19.31. BERTScore is slightly
lower, 90.84 versus 90.87. Human reference-similarity ratings average 3.21 versus 3.12 on the six-point scale.
These measures provide complementary evidence of agreement with personalized reference headlines; they
do not directly establish factual consistency with the article or a user’s experienced utility. Appendix K gives
the actual judgment task.
J.5 Transfer And Sparse-Evidence Stress Tests
J.5.1 Frozen-Core Reuse And Schema Distance
Table 20: Schema-distance diagnostic for conditional reuse on 500 MovieLens trajectories from 99 users.
Larger distance is associated with higher risk and smaller reciprocal-rank gain.
Relation Spearman ρ User-clustered 95% CI
dsch vs. frozen risk +0.109 [+0.002,+0.207]
dsch vs. adapted risk +0.160 [+0.060,+0.258]
dsch vs. frozen RR gain -0.089 [-0.169,-0.004]
dsch vs. adapted RR gain -0.114 [-0.195,-0.029]
The frozen-core protocol holds target rows, candidates, head architecture, and training fixed. The PENS-
trained core with a trained MovieLens head achieves 16.344 MRR, versus 1.115 for the random core with a
trained head and 1.371 for the trained core with an untrained head (Table 4). The 15.229-point difference,
rounded to 15.23, attributes useful structure to source learning while revealing the consumer’s role in accessing
it. Table 3 separately compares UniSRec and RecGURU at 500 and 3,000 target trajectories. At 3,000, PerTIDE
improves on the strongest baseline by 1.43/2.98/5.26 MRR/nDCG@10/HR@10 points. Target alignment
improves all three systems; the two protocols use different slices.
Across 99 users and 500 trajectories, schema-distance correlations with target risk are 0.109 and 0.160,
and correlations with reciprocal-rank gain are −0.089 and −0.114 (Table 20). Their reported confidence
intervals support small associations in the expected directions. The geometric quantities and conditional-loss
assumptions in the theoretical bound are not empirically certified by these associations.
49

KDM LAB / LCS2 RESEARCH MANUSCRIPT
J.5.2 Role Corruption
Table 21: Action-role corruption on fixed PENS trajectories.
Only positive/negative roles are flipped; trajectories, targets, and
candidate sets are held fixed.
Role flips MRR nDCG@10 HR@10
0% 12.14 16.02 32.0
10% 10.13 13.02 25.0
25% 9.17 11.10 22.0
50% 7.71 8.93 15.0
100% 2.81 4.90 10.0
Correct action labels help the encoder use
otherwise identical histories. With trajec-
tories, targets, and candidates fixed, posi-
tive/negative role corruption reduces MRR
from 12.14 to 2.81 (Table 21). A 10% cor-
ruption rate already reduces MRR by 2.01
points, and 50% corruption lowers HR@10
from 32.0 to 15.0. Both the ordering of the
target and its inclusion in the top ten deteri-
orate as supplied roles become less reliable.
The intervention therefore supports retain-
ing the action component of each event; it
measures predictive dependence on those
labels.
J.5.3 History Length
Table 22: History-length sensitivity on the same 500 PENS tra-
jectories. The target and 1+699 candidate sets are fixed while the
visible history grows from 10 to 40 events.
Events MRR nDCG@10 HR@10
10 11.874 14.904 27.8
20 11.881 15.011 28.2
30 11.909 15.091 28.4
40 11.926 15.157 28.6
Additional history offers a small benefit
in the separate 500-trajectory PENS study.
Extending the visible prefix from 10 to
40 events changes MRR from 11.874 to
11.926 and HR@10 from 27.8 to 28.6 (Ta-
ble 22). The target and candidate set re-
main fixed while the encoder receives more
past events. The modest changes across all
three metrics quantify the return from extra
history under this protocol. They comple-
ment the role-corruption study: changing
which action is attached to an event and
increasing the number of observed events test different aspects of the history representation.
J.5.4 Eventized OpenAI–Reddit Summaries
Table 23: Eventized TL;DR personalization on OpenAI-Reddit. We treat OpenAI-Reddit as an eventization
stress test under surrogate trajectory construction, not as evidence of unconstrained cross-domain user-history
transfer.
Category Model PSE-JSD PSE-SU4 PSE-METEOR
LLMs (2-shot)
LLaMA-13B 0.232 0.093 0.107
Zephyr-7B 0.214 0.087 0.104
Mistral-7B 0.226 0.088 0.103
DeepSeek-14B 0.243 0.095 0.109
MTSH PerTIDE-Full 0.285 0.261 0.294
The action-on-item interface also accommodates feedback-derived summary trajectories. PerTIDE reaches
0.285/0.261/0.294 PSE-JSD/PSE-SU4/PSE-METEOR, versus DeepSeek-14B’s 0.243/0.095/0.109 (Table 23).
This extends the evaluated generation setting beyond PENS. The chronology and positive/negative roles are
constructed from feedback, and augmentation occurs separately within the native training and evaluation
pools; the result concerns that eventized protocol.
J.5.5 Sparse Positive-Action Histories
PerTIDE retains 0.211 PSE-JSD under sparse positive evidence, compared with 0.366 originally, a 42.35% drop
(Table 24). Its relative retention is stronger on PSE-SU4 and PSE-METEOR, with reported drops of 28.45% and
26.2%. For DeepSeek-R1-32B, the JSD change from 0.263 to 0.152 corresponds to 42.21%, and the reported
SU4/METEOR drops are 30.4%/47.2%. GTP changes from 0.017 to 0.009 on PSE-SU4. The sparse scores
establish robustness under the particular intervention, while causal attribution to a specific trace would require
50

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Table 24: Robustness under sparse positive-action evidence. We evaluate each model on a click-only sparse
subset and report the original score (left) and sparse-action score (right), with the relative drop in parentheses.
Smaller drops indicate higher robustness when positive evidence is limited in the action-on-item trajectory.
Model PSE-JSD PSE-SU4 PSE-METEOR
DeepSeek-R1-32B (2-shot) 0.263 → 0.152 (−42.21%) 0.125 → 0.087 (−30.4%) 0.174 → 0.092 (−47.2%)
Gemini-2.5-Flash (2-shot) 0.222 → 0.122 (−45.0%) 0.104 → 0.061 (−41.3%) 0.124 → 0.070 (−43.5%)
Best Baseline (GTP) 0.024 → 0.016 (−33.3%) 0.017 → 0.009 (−47.1%) 0.019 → 0.011 (−42.1%)
PerTIDE 0.366 → 0.211 (−42.35%) 0.341 → 0.244 (−28.45%) 0.355 → 0.262 (−26.2%)
the corresponding controlled ablation.
51

KDM LAB / LCS2 RESEARCH MANUSCRIPT
J.6 Dialogue As An Additional Application And Boundary
MPChat tests the encoder on dialogue histories with inferred stance roles. The generation result demonstrates
a useful extension: PerTIDE exceeds Discretized SSM by 8.48/7.08/9.09/3.52 points in RG-2/RG-L/BLEU-
4/BERTScore (Table 25). The event interface and decoder-conditioning route can therefore operate with
dialogue-derived events as well as explicit news interactions.
Table 25: MPChat broader-applicability stress test: dialogue generation. AC denotes action-conditioned
evidence injection, CR denotes command-conditioned readout, UFI denotes user fused injection, and Full
denotes PerTIDE encoder with UGI decoder. These results test dialogue eventization under imperfect prefer-
ence logs rather than serving as primary evidence for schema-level generalizability; µ ± σ denotes mean and
standard deviation over three evaluations on uniformly random test-set subsamples.
Category Model RG-2 RG-L BLEU-4 BScore
LLMs (2-shot)
DeepSeek-32B 9.71 8.46 5.61 71.42
Qwen-2.5-32B 9.43 8.21 4.75 68.83
MS/Phi-Instruct 9.49 8.05 3.21 69.52
PAH Meanpool-B 8.54 ± 1.33 6.31 ± 1.21 3.43 ± 2.15 62.18 ± 1.45 Maxpool-B 7.21 ± 1.12 4.12 ± 1.43 2.55 ± 2.11 61.42 ± 1.65
MDH GRU-B 11.11 ± 1.31 10.82 ± 1.43 4.17 ± 0.78 63.18 ± 2.43
LDH D-FM Attention 8.25 ± 0.89 6.07 ± 1.32 3.18 ± 1.44 62.05 ± 2.78 Discretized SSM 12.17 ± 1.32 11.44 ± 1.56 6.48 ± 1.73 74.83 ± 1.66
MTSH
PerTIDE w/o AC 14.38 ± 1.32 12.73 ± 1.42 8.33 ± 0.93 73.89 ± 1.65
PerTIDE w/o CR 13.15 ± 1.77 10.91 ± 1.14 7.34 ± 1.55 71.64 ± 2.42
PerTIDE (UFI) 18.22 ± 1.55 15.73 ± 1.21 11.58 ± 1.36 75.23 ± 2.51
PerTIDE-Full 20.65 ± 1.23 18.52 ± 2.31 15.57 ± 2.06 78.35 ± 1.55
Response prediction. PerTIDE reaches 45.64/54.25 R@1/MRR, while the text-only SBERT comparator
reaches 51.32/64.76 (Table 26). A multimodal CLIP configuration with full persona reaches 72.65/81.12.
Because a text-only baseline already exceeds PerTIDE, missing images or persona cannot fully explain its
shortfall. Comparisons across different inputs measure performance differences, not a causal upper bound on
the value of those inputs.
Table 26: MPChat broader-applicability stress test: response prediction. Dialogue eventization is compared
with text-only and multimodal consumers. Scores use the 0–100 scale; µ ± σ denotes the reported mean and
standard deviation over three uniformly sampled 25% test subsets, shared across methods.
Model R@1 MRR
SBERT (zero-shot) 35.67 45.75
SBERT 51.32 ± 1.32 64.76 ± 0.92
SBERT+ViT (c) 57.70 ± 0.71 69.39 ± 0.40
SBERT+ViT (c, pi) 58.55 ± 0.70 70.17 ± 0.45
SBERT+ViT (c, pt) 64.32 ± 0.64 74.31 ± 0.45
SBERT+ViT (c, pi+t, Full) 65.29 ± 0.66 75.08 ± 0.43
SBERT+CLIP (c) 59.68 ± 0.70 70.99 ± 0.49
SBERT+CLIP (c, pi) 60.30 ± 0.50 71.47 ± 0.27
SBERT+CLIP (c, pt) 64.32 ± 0.75 74.33 ± 0.57
SBERT+CLIP (c, pi+t, Full) 65.43 ± 0.42 75.19 ± 0.32
CLIP+CLIP (ci) 40.85 ± 0.64 54.32 ± 0.30
CLIP+CLIP (c) 69.11 ± 0.74 78.22 ± 0.49
CLIP+CLIP (c, pi) 69.87 ± 0.40 78.85 ± 0.27
CLIP+CLIP (c, pt) 72.13 ± 0.61 80.72 ± 0.38
CLIP+CLIP (c, pi+t, Full) 72.65 ± 0.38 81.12 ± 0.26
DeepSeek-R1-32B (c, pt) 41.45 54.42
Qwen2.5-32B (c, pt) 41.32 52.17
PerTIDE-Full (ct) (ours) 45.64 ± 0.45 54.25 ± 0.67
Speaker identification. PerTIDE reaches 41.77/47.19 R@1/MRR (Table 27). Text persona improves several
comparator configurations, and CLIP with multimodal persona reaches 62.17/73.08. The results motivate
richer representation of discourse and speaker information while documenting where the current encoder
trails specialized alternatives.
The dialogue results separate applicability from uniform superiority: inferred events support improved
52

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Table 27: MPChat broader-applicability stress test: speaker identification. We report speaker identification
under dialogue eventization and compare against systems using persona and multimodal context; c: dialogue
context, ct: text-only context, r: response, Pc: candidate set with profile information
Category Model R@1 MRR
Text Only SBERT ( ct, r, P t c) 56.47 ± 0.58 67.92 ± 0.52
SBERT+ViT
c, r, P i c 19.56 ± 0.64 35.84 ± 0.45
c, r, P t c 56.87 ± 0.60 68.33 ± 0.37
c, r, P i+t c (Full) 57.28 ± 0.44 68.86 ± 0.33
SBERT+CLIP
c, r, P i c 25.71 ± 0.49 42.47 ± 0.34
c, r, P t c 56.63 ± 0.66 68.15 ± 0.42
c, r, P i+t c (Full) 57.24 ± 0.63 68.69 ± 0.39
CLIP+CLIP
c, r, P i c 44.27 ± 0.66 59.04 ± 0.35
c, r, P t c 59.89 ± 0.71 70.87 ± 0.53
c, r, P i+t c (Full) 62.17 ± 0.56 73.08 ± 0.35
LLMs (2-shot)
DeepSeek-32B (c, r, P t c) 48.13 54.37
Qwen-2.5-32B (c, r, P t c) 45.31 51.62
DeepSeek-32B (c, r) 28.56 31.43
Qwen-2.5-32B (c, r) 25.61 29.67
MTSH (ours) PerTIDE-Full (ct, r) 41.77 ± 0.82 47.19 ± 1.30
generation in the reported comparison, while response prediction and speaker identification remain more
difficult. The transfer theory in Appendix B.2 makes compatibility explicit; it does not measure the effect of
missing persona or multimodal evidence in these experiments.
K Human Reference-Similarity Evaluation (PENS)
To assess agreement with personalized reference headlines, we conduct a survey-based evaluation in which
each participant1 is shown (i) the gold-reference summary and (ii) one model-generated summary for the same
PENS news article. Model identities are hidden to mitigate brand and expectation bias, and participants rate
reference–generation similarity on a 1–6 scale (1: low, 6: high). We evaluate PerTIDE against representative
strong baselines spanning specialized personalized models (PENS-NRMS-T2, GTP-TrRMIo, SP-Individual)
and 2-shot history-conditioned LLMs (DeepSeek-14B, DeepSeek-32B, Qwen-2.5-32B).
We report average human-judgment (HJ) scores alongside automatic metrics (RG-SU4, BLEU-4, BScore) in
Table 19. PerTIDE attains the highest HJ score (3.21), exceeding the best 2-shot LLM (DeepSeek-32B: 3.12) and
all specialized baselines (e.g., PENS-NRMS-T2: 2.95; GTP-TRRMIO: 2.44; SP-Individual: 2.86).
Participation was voluntary, responses were de-identified before analysis, and the study involved only
minimal-risk similarity judgments over news headlines. We collected only aggregate demographic information
and did not collect identifiable participant information or private user histories. The study followed the
applicable institutional approval, exemption, or equivalent review process under anonymized reporting.
1Demography: 65 male, 22 female graduate students from Computer Science, Humanities, Mathematics, & Natural Sciences.
53

KDM LAB / LCS2 RESEARCH MANUSCRIPT
Figure 5: HJ-annotation survey format
.
Figure 6: Prompt Templates for LLMs for (a)Personalized Summarization, (b)Dialogue Generation
.
54

KDM LAB / LCS2 RESEARCH MANUSCRIPT
L LLM Prompting Protocol
Overview. We use prompted LLMs for generative tasks using temperature 0.4 and nucleus sampling with
top_p = 0.9 for all LLM runs.
L.1 LLMs As Summarizers (Personalized Headline Generation)
Each instance is a conditional generation problem, where we prompt the LLMs using user-history as the
context and a single query document body and instruct the LLM to generate one personalized headline. The
instruction ties personalization to the history (clicked topics should be emphasized; skipped topics should
be deprioritized) while requiring factual consistency with the query document. We constrain the output to a
single field (Headline: ... ) and ignore any additional text.
L.2 LLMs As Dialogue Generators
We prompt the LLMs using the entire dialogue discourse as the context and instruct the LLM to generate one
next response. The instruction ties personalization to factual consistency with the persona information and the
discourse context.
M Assets And Usage Terms
Roles of pretrained models. The prompted LLM baselines use fixed pretrained weights. PerTIDE instead
partially tunes DistilGPT2 and its contextualization modules as specified in Appendix D.5; its item embeddings
are precomputed. The DistilGPT2 model card lists Apache 2.0 ( https://huggingface.co/distilber
t/distilgpt2 ). DeepSeek-R1 models use the provider’s MIT terms ( https://github.com/deepsee
k- ai/DeepSeek- R1/blob/main/LICENSE ); Mistral-7B-Instruct-v0.2 lists Apache 2.0 ( https://huggin
gface.co/mistralai/Mistral-7B-Instruct-v0.2 ); Llama-2 uses its Community License Agreement
(https://huggingface.co/meta-llama/Llama-2-13b-chat-hf ); and Zephyr-7B-beta lists MIT ( https:
//huggingface.co/HuggingFaceH4/zephyr-7b-beta ). Hosted-model use is additionally governed by the
relevant provider’s service terms. Model citations and baseline descriptions identify their roles; a provider
license does not by itself certify compliance of every downstream use.
Datasets. MovieLens usage conditions are supplied by GroupLens (https://grouplens.org/datasets/m
ovielens/1m/). MIND and PENS are distributed for research under the Microsoft Research License Terms
linked from their official pages ( https://msnews.github.io/ ; https://msnews.github.io/pens.html ).
OpenAI’s summarization release includes its repository license ( https://github.com/openai/summar
ize-from-feedback/blob/master/LICENSE ); MPChat provides CC BY 4.0 terms in its release ( https:
//github.com/ahnjaewoo/MPCHAT/blob/main/LICENSE ). These assets retain their original attribution and
access conditions. The paper describes derived event trajectories and does not grant redistribution rights to
the underlying data.
55
