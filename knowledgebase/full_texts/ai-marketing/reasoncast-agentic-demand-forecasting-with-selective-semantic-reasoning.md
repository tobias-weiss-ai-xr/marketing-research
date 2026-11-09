---
title: 'ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning'
url: https://arxiv.org/abs/2608.15291
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Ziyue Yang
- Chaolin Xu
- Yijing Wang
- Tiankai Gu
- Hui Yang
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.15291
pages: 14
chars: 74597
fetched_at: '2026-11-08T13:31:39+00:00'
kb_version: 1
---

# ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning

ReasonCast: Agentic Demand Forecasting with Selective
Semantic Reasoning
Ziyue Yang∗
Taobao and Tmall Group, Alibaba
Group
China
Chaolin Xu∗
Taobao and Tmall Group, Alibaba
Group
China
Yijing Wang
Taobao and Tmall Group, Alibaba
Group
China
Tiankai Gu
Taobao and Tmall Group, Alibaba
Group
China
Hui Yang
Taobao and Tmall Group, Alibaba
Group
China
Yanhong Lin
Taobao and Tmall Group, Alibaba
Group
China
Kaiyuan Liu
Taobao and Tmall Group, Alibaba
Group
China
Fei Xiao†
Taobao and Tmall Group, Alibaba
Group
China
Abstract
Demand forecasting increasingly requires combining two comple-
mentary sources of information: historical sales reveal recurring nu-
merical dynamics, while future promotions, holidays, price changes,
and platform interventions provide forward-looking knowledge
that may not be recoverable from past observations alone. Time-
series foundation models are strong numerical forecasters, and
large language models can interpret heterogeneous event context.
However, existing text-enhanced forecasting methods often encode
such context into generic representations and fuse it uniformly
with time-series features, without explicitly distinguishing which
semantic effects are forecast-relevant, where they should interact
with temporal representations, or how they should modify future
dynamics.
We introduce ReasonCast, a structured semantic intervention
framework that translates event knowledge into forecast-specific
operations. Before constructing an intervention, a lightweight agent
examines the event context, the no-text forecast, and its predictive
uncertainty to determine whether textual reasoning is needed and
whether additional evidence or temporal-statistics tools should be
invoked. For known regime-changing events, including holidays
and mega-sales, semantic reasoning is activated by default. Rather
than injecting free-form text, ReasonCast represents event knowl-
edge through structured fields describing event relevance, demand
direction, temporal shape, amplitude, and peak intensity. These
fields interact selectively with event-related temporal components
of a pretrained time-series foundation model. An additive path
corrects local trends and temporal shapes, a multiplicative path
captures event-driven level shifts, and an instance-wise mecha-
nism calibrates intervention strength. When semantic intervention
is unnecessary, the original numerical forecast can be preserved
exactly.
To make the resulting semantics not only well-formed but
forecast-effective, ReasonCast introduces a forecast-grounded post-
training curriculum. Schema SFT establishes valid and internally
∗Ziyue Yang and Chaolin Xu contributed equally to this work.
†Corresponding author.
consistent semantic fields; semantic-field RL calibrates direction,
shape, amplitude, and peak judgments using forecast-derived
supervision; and forecast-utility RL evaluates candidate semantic
interventions through a frozen forecaster, aligning reasoning out-
puts with marginal forecast improvement while penalizing negative
transfer and unnecessary tool cost. ReasonCast lowers WMAPE
by 3.29, 1.25, and 0.47 percentage points on holiday-sensitive
categories, mega-sale-sensitive categories, and M5 event windows,
respectively. On stable-sales periods, indiscriminate semantic
intervention increases WMAPE by 1.68 percentage points, whereas
suppressing unnecessary intervention preserves the numerical
backbone. These results demonstrate the value of moving beyond
generic text fusion toward structured, forecast-aligned semantic
intervention.
Keywords
time series forecasting, demand forecasting, large language models,
agentic reasoning, multimodal learning, text–time-series fusion,
event-aware forecasting
1 Introduction
Commerce demand reflects two fundamentally different sources of
variation. Recurring regularities—such as trend, seasonality, auto-
correlation, and repeated campaign patterns—can be learned from
historical observations. Future promotions, holidays, price changes,
platform interventions, and product-specific events, however, may
cause shifts that are not identifiable from past sales alone, a distinc-
tion also reflected in demand benchmarks and models of known fu-
ture covariates [13, 23, 33]. Time-series foundation models (TSFMs)
provide strong numerical backbones by transferring recurring struc-
ture across large collections of series [2, 4, 5, 22, 35], with recent
work further scaling model capacity, context length, and pattern
specialization [17, 20, 21]. Yet a numerical backbone cannot infer a
future event that is absent from its inputs.
Large language models (LLMs) offer a complementary capabil-
ity: they can interpret heterogeneous event records and convert
contextual knowledge into forecasting-relevant judgments. The
arXiv:2608.15291v1  [cs.AI]  15 Aug 2026

Preprint, August 2026, Ziyue Yang, Chaolin Xu, Yijing Wang, Tiankai Gu, Hui Yang, Yanhong Lin, Kaiyuan Liu, and Fei Xiao
value of such context is nevertheless conditional. Text helps when
it supplies future events, constraints, or background information
unavailable from numerical history [34]; broad empirical evidence
further shows that multimodal gains depend strongly on whether
text contributes signals not already captured by the temporal input
and backbone [40]. Event-aware studies likewise find that unfil-
tered news can degrade forecasting relative to carefully selected
evidence [32]. Thus, the central question is not simply how to fuse
more text, butwhether, where, and to what extent semantic reasoning
should alter a strong numerical forecast.
Representative forecasting designs, summarized in Table 1, leave
three challenges unresolved. First, semantic value is heterogeneous
across products, events, and forecast windows, requiringinstance-
adaptive control. Second, useful semantics must enter the computa-
tion at an appropriate location and in an appropriate form: some
events change local trends and shapes, whereas major campaigns
produce multiplicative level shifts. Third, language supervision
rewards plausible reasoning but does not ensure downstream pre-
dictive value. These challenges call for a forecaster that separates
semantic reasoning from numerical prediction and treats text as a
controlled intervention rather than an always-on modality.
We introduceReasonCast, an agentic demand forecasting
framework following aroute–reason–intervene–forecastparadigm.
Given event context, the no-text forecast, and its entropy, the agent
selects Skip, low-cost Basic semantics, or tool-augmented Tool
semantics; holidays and mega-sales rule out Skip. A pretrained
TSFM remains responsible for numerical prediction.
For non-skip actions, event-related temporal components alone
query semantic tokens. An instance-wise gate controls intervention
strength, while additive and multiplicative paths model local and
level changes. Skip disables both paths and exactly recovers the
no-text computation. Alignment pretraining grounds event seman-
tics, and forecast-aligned policy optimization rewards routing and
outputs by their marginal improvement over the backbone.
We evaluate ReasonCast on large-scale commerce data at multi-
ple granularities and public item-level demand benchmarks, sepa-
rating normal and event-driven periods and stress-testing corrupted
context. Our contributions are:
• We formulate event-enhanced demand forecasting asselec-
tive semantic intervention, shifting the focus from extracting
more text to controlling its marginal influence on a strong
numerical forecaster.
• We propose a three-action agent policy that routes each in-
stance to no intervention, low-cost structured reasoning, or
tool-augmented reasoning, with mandatory semantic activa-
tion for holidays and mega-sales.
• We combine selective event interaction, per-instance gating,
additive and multiplicative corrections, and exact recovery of
the no-text backbone whenever the agent skips intervention.
2 Related Work
2.1 Numerical and Language-Based Forecasting
Numerical forecasting has progressed from probabilistic and
covariate-aware models [13, 25] to specialized linear, patch-based,
inverted, and multiscale architectures [ 18, 24, 31, 33, 39]. Time-
series foundation models further transfer recurring structure across
datasets through value tokenization, decoder-style generation, or
heterogeneous-series pretraining [2, 4, 5, 17, 22, 35]. These models
are strong numerical specialists, but they cannot infer a future
event absent from their inputs.
Other work repurposes pretrained language models as numer-
ical forecasters or representation learners [3, 6, 10, 16, 19, 27, 42].
Because language components do not consistently explain the re-
sulting gains [28], ReasonCast retains a TSFM as forecast owner and
assigns the LLM a distinct role: reasoning over event knowledge
rather than generating sales values.
2.2 Multimodal Forecasting and Cross-Modal
Alignment
Text-enhanced forecasting uses either endogenous descriptions
derived from the series [ 9, 10, 15, 27, 41] or exogenous evidence
such as news, events, and domain conditions [ 8, 12, 14, 29, 36].
The former can improve representation transfer but may duplicate
numerical information; the latter can reveal shifts unavailable from
history. Empirical studies accordingly find that multimodal gains
depend on backbone capacity, alignment, data scale, and whether
text adds predictive information [ 34, 40]. ReasonCast turns this
conditional utility into an instance-level control objective.
2.3 Event Reasoning and Forecast-Aware Agents
Language agents can interleave reasoning, actions, and tool use [26,
38]. In forecasting, From News to Forecast refines evidence selec-
tion using validation feedback [32], while VoT combines event and
numerical branches with retrieval and adaptive fusion [30]. Reason-
Cast instead routes each instance among no intervention, low-cost
reasoning, and tool-augmented reasoning; structured semantics
modify a dedicated TSFM only when selected. Forecast-aligned
optimization trains this policy for marginal utility, and the no-text
forecast is retained exactly when the agent skips.
3 Problem Formulation
For each item or leaf category𝑖, let
x𝑖 =[𝑥 𝑖,1,...,𝑥 𝑖,𝐿](1)
denote an observed demand history of length𝐿, and letc𝑖 denote
the event records and contextual information available before the
forecast origin. The goal is to predict the next𝐻= 7observations,
ˆy𝑖 =[ ˆ𝑦𝑖,1,..., ˆ𝑦𝑖,𝐻].(2)
A pretrained Chronos-2 model𝑓𝜃 [1] provides the no-text forecast
ˆyts 𝑖 =𝑓 𝜃(x𝑖) and entropyH𝑖. Witho 𝑖 =( c𝑖, ˆyts 𝑖 ,H𝑖), the agent
chooses
𝑎𝑖∼𝜋 route 𝜙 (o𝑖), 𝑎 𝑖∈{Skip,Basic,Tool},(3)
where holidays and mega-sales enforce𝑎𝑖 ≠Skip . We setT𝑖 =∅
for Skip and otherwise generate semantic tokens with𝜋 sem 𝜙 (o𝑖,𝑎𝑖).
The forecast𝐹 𝜃,𝜓(x𝑖,T𝑖)satisfies
𝑎𝑖 =Skip=⇒𝐹 𝜃,𝜓(x𝑖,∅)=𝑓 𝜃(x𝑖).(4)

ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning Preprint, August 2026,
Table 1: Comparison of representative forecasting designs. ✓,△, and× denote explicit, partial or method-dependent, and
no explicit support. Reasoning over exogenous events goes beyond encoding external text to infer forecast-relevant effects.
Selective semantic intervention combines instance-levelSkip/Basic/Toolrouting with continuous control over intervention
strength; designs without an explicit abstention route provide only partial support. Reasoner adaptation covers both parametric
post-training and non-parametric use of forecasting feedback.
Forecasting design
Numerical
forecast owner
Reasoning over
exogenous events
Selective semantic
intervention
Exact no-text
preservation Reasoner adaptation
TS-only / TSFM [2, 4] TSFM× ×– N/A
LLM numerical forecasting [6, 10] LLM× × ×Frozen / prompting
Joint multimodal forecasting [8, 12, 29, 36, 41] Joint model△ × ×Task-level training / SFT
From News to Forecast [32] LLM✓× ×Reflection + evidence reselection
VoT [30] Hybrid branches✓△ ×Retrieval + historical ICL
ReasonCast TSFM✓ ✓ ✓
SFT + semantic-field RL
+ forecast-utility RL
4 ReasonCast
4.1 Framework Overview
ReasonCast is trained with a three-phase curriculum. First, schema
SFT establishes valid structured outputs, after which semantic-field
RL calibrates forecast-derived direction, temporal shape, ampli-
tude, and peak fields. Second, the semantic-field policy regenerates
the fusion-training corpus, on which we learn orthogonal event-
subspace grounding, multimodal alignment, and selective dual-path
fusion. Third, the trained forecaster is frozen and reused as a stable
downstream evaluator for forecast-utility RL, which jointly opti-
mizes routing and semantic outputs without updating the numerical
model. Figure 1 summarizes the framework.
4.2 Agentic Event Routing and Semantic
Reasoning
Skip terminates semantic processing, Basic uses available context,
and Tool retrieves evidence or invokes temporal-statistics tools
for ambiguous or high-entropy cases. Hard-triggered holidays and
mega-sales use at least Basic. For either non-skip action, Qwen3-
32B [37] produces
s𝑖 =(𝑟 𝑖, 𝑒𝑖,𝑑 𝑖,𝑞 𝑖,𝑢 𝑖, 𝑝𝑖, 𝑧𝑖),(5)
where𝑟𝑖 denotes event relevance,𝑒𝑖 the dominant event,𝑑𝑖 demand
direction,𝑞𝑖 temporal shape, 𝑢𝑖 the amplitude multiplier, 𝑝𝑖 the
peak multiplier, and𝑧𝑖 a concise forecast-trend narrative. A text
encoder and MLP aligner produce𝐷-dimensional tokensT𝑖. SFT
teaches the schema; forecast-aligned optimization calibrates routing
and semantic utility. The agent decides whether and how much to
reason, while the TSFM retains numerical forecasting.
Reasoner supervision.We stratify 40,000 item–window candi-
dates by trajectory regime and obtain 11,627 teacher generations.
Deterministic field-consistency filters retain 7,312 responses, which
are compressed, deduplicated, and rebalanced into 4,590 SFT exam-
ples; Appendix B provides the full construction protocol.
4.3 Event-Selective Temporal Interaction
LetH𝑖∈R 𝑀×𝐷 be temporal tokens at a fusion layer. From a learned
basisB ∈R 𝐷×𝑑𝐸 , QR factorization yields an orthonormal event
basisQwithQ ⊤Q = I. We define the orthogonal projectorP 𝐸 =
QQ⊤ and decompose
H𝐸 𝑖 =H𝑖 P𝐸,H 𝑁 𝑖 =H𝑖(I−P 𝐸).(6)
BecauseP⊤ 𝐸 = P𝐸 andP 2 𝐸 = P𝐸, the decomposition guarantees
H𝐸 𝑖 + H𝑁 𝑖 = H𝑖 and⟨H𝐸 𝑖, H𝑁 𝑖⟩𝐹 = 0. Textual interaction is computed
with the event component as query:
ΔH𝑖 =CrossAttn(𝑄=H 𝐸 𝑖,𝐾=T 𝑖,𝑉=T 𝑖).(7)
The fused representation is
eH𝑖 =H𝑁 𝑖 +H𝐸 𝑖 +𝑚𝑖𝛼𝑔𝑖 ΔH𝑖,(8)
where𝑚𝑖 is a text-availability mask,𝛼is a residual scale, and𝑔 𝑖 is
an instance-wise gate. The interface is applied to the Chronos-2
future-token representation before the prediction head. Thus, only
the event component queries text; because the attention output
is not reprojected, we make no stronger claim that the semantic
update itself remains in the event component.
4.4 Multimodal Alignment Pretraining
Before end-to-end forecasting training, we align pooled event se-
manticsz𝑇 𝑖 with event-related temporal representationsz𝐸 𝑖 . Moti-
vated by contrastive cross-modal alignment [7] and its recent use
in language–time-series forecasting [15, 41], a contrastive objective
encourages matched event–series pairs to be close and mismatched
pairs to remain separated:
Lalign =− 1 𝐵 𝐵∑︁ 𝑖=1 log exp(sim(z𝐸 𝑖,z𝑇 𝑖)/𝜏) ˝𝐵 𝑗=1 exp(sim(z𝐸 𝑖,z𝑇 𝑗)/𝜏) .(9)
The denominator uses the other text embeddings in the same mini-
batch as negatives.
4.5 Instance-Adaptive Dual-Path Correction
The value of semantic context varies across items and forecast
windows. ReasonCast uses an instance-wise gate
𝑔𝑖 =𝑔 max𝜎(MLP(u𝑖)),(10)
whereu𝑖 concatenates pooled semantic features, recent-demand
volatility, entropy of the no-text forecast, and encoded event de-
scriptors, all available at inference time. The gate modulates the
additive latent residual in Eq. (8).

Preprint, August 2026, Ziyue Yang, Chaolin Xu, Yijing Wang, Tiankai Gu, Hui Yang, Yanhong Lin, Kaiyuan Liu, and Fei Xiao
(a) Reason–Align–Intervene–Forecast Inference
Historical Time-series
Sales and Related Covariates
Temporal Statistics
Recent level · trend · volatility
Historical event responses · YOY
Platform Signals
Trending queries · search heat
Promotion Intelligence
Calendar · campaign rhythm
 event position · covered categories
External Signals
News · social hotspots
External events
Reasoning Agent
Stage 1：Evidence-Augmented Event Reasoning
Direction
Textual intervention:
Yes/No
Dominant event
Shape
Forecast Trend
Direction
Stage 2：Selective Semantic Intervention for Forecasting
Token Embeddings
 Aligned Tokens
T
Text
Encoder
MLP
Aligner
Future Token
h!
① Reason ② Structure Semantics
③ Encode
Pretrained TSFM
Chronos-2 instantiation
∆∆∆
Event-Selective Cross-attention
K,V = aligned tokens T
Q= event component 𝒉𝑬
Output: Semantic
response
∆SEM
Orthogonal
Decomposition
Additive Latent Correction
h‘	=h!+αg$∆SEM
Adaptive Semantic Gate
g$=entrophy(h!)
Remaining TSFM
blocks + Forecast
Head
Final
Forecast
Multiplicative Correction
c$=f(T)
(b) Training Curriculum: From Semantic Fidelity to Forecast Utility
① Decompose ② Interact ③ Control
④ Forecast
1. Reasoner Post-training 2. Event Subspace Grounding 3. Text-Event Alignment 4. Selective Fusion Training 5. Forecast-Aligned
Reasoner RL
Teacher Corpus
Future-ground-truth ﬁltered
trajectories
Field-Reward GRPO
format · direction/shape ·
mean/peak
SFT
Future Token
h!
QR Projector
𝑃=𝑄𝑄ᵀ
Auxiliary grounding
mean · peak · minimum · YoY
ℎ𝑁⟂ℎ𝐸
Event vector
Aligned Tokens
T
Aligner
Contrastive learning
Event query
𝑄=ℎ𝐸
Text tokens
𝐾,𝑉=𝑇
Cross-Attention
𝛥𝑠𝑒𝑚
Forecast loss
MultiplicateAdditive gate
❄
❄
Marginal forecast reward
𝑅ₖ
=𝐿𝑛𝑜−𝑡𝑒𝑥𝑡−𝐿𝑠𝑒𝑚𝑎𝑛𝑡𝑖𝑐,𝑘
Frozen fused
forecaster
Baseline
𝑠=∅
GRPO
Update
Figure 1: Overview of ReasonCast. (a) ReasonCast follows a reason–align–intervene–forecast pipeline. An evidence-augmented
LLM agent combines the historical series with temporal statistics, promotion intelligence, platform signals, and external
signals to produce structured event semantics. A text encoder and an MLP aligner map these semantics to aligned tokensT. In
parallel, a pretrained time-series foundation model (TSFM) produces a future tokenh 𝐹 , which is orthogonally decomposed at
the fusion interface into event-related and complementary componentsh 𝐸 andh 𝑁 . Onlyh 𝐸 queriesTthrough event-selective
cross-attention. An adaptive semantic gate modulates the additive latent correction for local trend and shape changes, while a
complementary multiplicative path handles large event-driven level shifts. Without semantic context, both correction paths
are disabled and the fusion interface exactly recovers the original TSFM computation. (b) The training curriculum comprises
schema SFT, semantic-field RL, orthogonal event-subspace grounding and selective fusion training, and forecast-utility RL.
During forecast-utility RL, candidate semantics are compared with the cached semantic-field-policy fusion result, while
degradation beyond the no-text TSFM is explicitly penalized.
Latent residuals are well suited to fine-grained temporal pattern
changes but may have limited authority over large level shifts. We
therefore introduce a complementary multiplicative correction:
ˆy𝑖 = ˆylat 𝑖 ⊙exp 𝑚𝑖𝛽𝑔𝑖 𝝆𝑖 ,(11)
where ˆylat 𝑖 is decoded from the additively fused representation,𝝆𝑖 is
a bounded semantic level-shift signal, and𝛽 controls the correction
scale.
4.6 Exact No-Text Identity
When the agent selects Skip, or when textual context is unavailable,
𝑚𝑖 =0. Equations (8) and (11) then reduce to
eH𝑖 =H𝑖, ˆy𝑖 = ˆyts 𝑖 .(12)
The property is enforced by the routing action and an explicit
mask rather than learned approximately. Consequently, a skipped
stable-sales instance recovers the Chronos-2 backbone prediction
exactly. The guarantee applies to the fusion interface. Although
its event subspace is geometrically orthogonal to the complement,
this constraint does not make the subspace causally or globally
identifiable.
4.7 Forecast-Aligned Reasoner Post-Training
Language supervision alone can yield plausible but forecast-
irrelevant text, whereas direct loss optimization may reward
malformed semantics that happen to improve a prediction. Fol-
lowing schema SFT, we optimize the reasoner with two RL stages:
semantic-field RL calibrates verifiable semantic fields, and forecast-
utility RL optimizes their downstream value against a frozen
forecaster.
Semantic-field RL: structured semantic calibration.For prompt
𝑖, GRPO samples𝐺 structured responses. Forecast-derived targets
score direction, temporal shape, amplitude, and peak:
𝐴𝑖𝑗 =
∑︁
𝑘∈{𝑑,𝑞,𝑎,𝑝}
𝑤𝑘𝑎𝑘 𝑖𝑗−𝐶 struct 𝑖𝑗 ,(13)

ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning Preprint, August 2026,
where𝐶struct 𝑖𝑗 penalizes invalid formats and cross-field contradic-
tions. Group-normalized rewards and a KL reference to the SFT
policy yield the field-calibrated reasoner𝜋 1.
Forecast-utility RL: frozen-forecaster optimization.We use 𝜋1 to
regenerate the fusion corpus, train the alignment and dual-path
forecaster𝐹1, and then freeze it. Each rollout selects Skip, Basic,
or Tool; holidays and mega-sales disallow Skip. Non-skip candi-
dates must remain parseable, cross-field consistent, and close to the
cached semantic-field score before being evaluated by𝐹 1.
Let𝑀𝑖𝑗 be candidate MAE,𝑀 ref 𝑖 the cached semantic-field-policy
fusion MAE,𝑀 ts 𝑖 the no-text MAE, and𝑆𝑖 a sample-specific scale.
We measure downstream improvement and one-sided harm as
𝐷𝑖𝑗 = 𝑀 ref 𝑖 −𝑀𝑖𝑗 𝑆𝑖 , 𝐻 𝑖𝑗 =[𝑀𝑖𝑗−(1+𝜂)𝑀 ts 𝑖]+ 𝑆𝑖 .(14)
With semantic-validity indicator𝑣𝑖𝑗 , semantic margin𝐶𝑖𝑗 , and route
cost𝑐(𝑎 𝑖𝑗), the reward is
𝑅𝑖𝑗 =
 

𝑏+𝜆 𝑢 clip(𝐷𝑖𝑗), 𝑎 𝑖𝑗 =Skip,
𝐴𝑖𝑗−𝛾, 𝑣 𝑖𝑗 =0,
𝑏+𝜆 𝑐𝐶𝑖𝑗+𝜆𝑢 clip(𝐷𝑖𝑗−𝜆ℎ𝐻𝑖𝑗)−𝜆 cost𝑐(𝑎𝑖𝑗), 𝑣 𝑖𝑗 =1.
(15)
Thus, abstention competes directly with semantic intervention,
while tool use must justify its additional cost. GRPO is initialized
from𝜋1 and uses the semantic-field policy globally, plus SFT condi-
tionally, as KL references to preserve semantic fidelity. Appendix B
provides the validity threshold, reference conditions, and optimiza-
tion settings.
5 Experiments
5.1 Research Questions
We evaluate ReasonCast through four questions:
• RQ1:Does ReasonCast improve event-period forecasting
and transfer to M5 while preserving stable-period perfor-
mance?
• RQ2:Do discrete routing and entropy-conditioned gating
allocate semantic intervention more effectively than always-
on, ungated, or globally weighted fusion?
• RQ3:What do orthogonal decomposition, alignment, gating,
and additive–multiplicative correction each contribute?
• RQ4:How do SFT, semantic-field RL, and forecast-utility RL
affect semantic fidelity and downstream forecast utility?
5.2 Datasets and Evaluation Protocol
The proprietary commerce dataset contains 15,696 daily sales series
at the leaf-category level, spanning August 10, 2024 to May 30, 2026.
We adopt a chronological split: August 10, 2024 to August 31, 2025
for training, September 1 to October 31, 2025 for model selection,
and November 1, 2025 to May 30, 2026 for evaluation. The test
set comprises 15 seven-day forecasting windows, including three
mega-sale, ten holiday, and two stable-sales windows. To prevent
temporal leakage, all textual descriptions and event information
are restricted to records available before the corresponding forecast
origin. For M5 [23], we evaluate 3,049 item-level series aggregated
across all ten stores over 14 seven-day event-centered windows,
using only calendar, event, and price covariates available at each
forecast origin.
5.3 Baselines
We compare Seasonal Naive with LightGBM [11], PatchTST [24],
and iTransformer [18]; pretrained TimesFM [4], Chronos [2], and
Chronos-2 small [1]; and the text-enhanced Time-LLM [ 10] and
VoT [30]. Chronos-2 small is evaluated zero-shot and with the
Uni-FT and Multi-FT variants shown in the tables. Numerical mod-
els receive historical demand, while covariate-enabled and text-
enhanced variants additionally receive only calendar, event, price,
or text fields available before the forecast origin. All methods use the
same split, rolling origins, seven-day horizon, and metrics; trainable
baselines are selected by validation WMAPE without test-window
tuning.
5.4 Metrics
We evaluate point forecasting accuracy using weighted mean abso-
lute percentage error (WMAPE) and mean absolute error (MAE).
LetD𝑠 denote the set of leaf-category–day observations in an eval-
uation slice𝑠. We compute
WMAPE𝑠 =
˝
(𝑖,𝑡)∈D 𝑠|𝑦𝑖,𝑡− ˆ𝑦𝑖,𝑡| ˝
(𝑖,𝑡)∈D 𝑠|𝑦𝑖,𝑡| ,(16)
and
MAE𝑠 = 1 |D𝑠| ∑︁ (𝑖,𝑡)∈D 𝑠 |𝑦𝑖,𝑡− ˆ𝑦𝑖,𝑡|.(17)
WMAPE is the primary metric because it measures aggregate fore-
casting error relative to realized demand and places greater empha-
sis on high-volume observations. MAE complements WMAPE by
retaining the absolute magnitude of forecasting errors. Both met-
rics are computed separately for each evaluation slice, including
stable-sales periods, holiday and mega-sale periods, event-sensitive
and event-insensitive leaf categories, and the M5 dataset. Lower
values indicate better performance.
5.5 Main Results
Table 2 compares event-centered performance on the proprietary
dataset and M5. Holiday and mega-sale categories are split into
sensitive and insensitive groups using training data only; M5 uses
windows around major calendar events. Table 3 separately tests the
boundary case in which regular temporal dynamics already explain
most demand.
ReasonCast obtains the lowest WMAPE on all six proprietary
event slices and on M5 event windows, with the largest margins
during holidays. It also achieves the best WMAPE and second-
best MAE on mega-sale-insensitive categories, indicating that the
gain transfers beyond the most responsive groups and beyond the
proprietary dataset.
Table 3 isolates routing. Always-on semantics degrade the
Chronos2-small backbone from 7.91%/185.15 to 9.59%/224.43.
Agent-routed ReasonCast selects Skip and recovers the back-
bone exactly. Event windows, by contrast, require at least Basic
reasoning.

Preprint, August 2026, Ziyue Yang, Chaolin Xu, Yijing Wang, Tiankai Gu, Hui Yang, Yanhong Lin, Kaiyuan Liu, and Fei Xiao
Table 2: Main forecasting results on event-centered evaluations. Cells report WMAPE/MAE; lower values are better. Sens. and
Insens. denote event-sensitive and event-insensitive leaf categories, respectively. The best results are highlighted in bold, and
the second-best results are underlined.
Method Holiday Mega-sale M5 event windows
Sens. Insens. All Sens. Insens. All WMAPE MAE
Seasonal Naive 119.96% 2738.47 56.69% 609.09 47.39% 571.90 27.94% 766.85 12.49% 283.57 16.55% 434.69 44.55% 5.47
LightGBM 74.61% 1671.02 43.20% 489.11 34.23% 447.08 26.94% 732.37 12.83% 290.49 16.23% 425.58 34.06% 4.17
PatchTST 84.90% 1771.26 47.80% 516.75 39.78% 485.47 22.94% 652.38 9.91% 214.3413.41% 355.74 48.31% 5.91
iTransformer 79.29% 1849.54 42.03% 486.83 33.64% 450.65 23.07% 653.62 11.30% 248.18 14.49% 382.73 34.39% 4.21
TimesFM 67.23% 1586.46 48.82% 557.09 39.37% 517.45 24.20% 701.77 14.57% 316.56 17.63% 465.66 34.63% 4.23
Chronos1 44.54% 1163.21 37.25% 450.04 29.70% 417.03 26.99% 730.93 10.97% 248.37 14.90% 391.61 35.38% 4.33
Chronos2-small 55.42% 1412.40 38.50% 464.16 31.28% 437.37 24.59% 681.33 10.83% 245.81 14.64% 389.11 34.40% 4.20
Chronos2-small (Uni-FT) 42.39% 1185.03 34.94% 415.31 27.89% 388.79 25.20% 694.97 10.75% 242.43 14.55% 382.88 33.21% 4.08
Chronos2-small (Multi-FT) 45.30% 1268.46 31.64% 390.67 25.59% 370.86 22.14% 622.10 10.02% 222.37 13.35% 352.24 33.10% 4.06
Time-LLM 87.76% 1972.79 57.31% 602.99 47.03% 556.71 25.89% 721.11 13.57% 306.44 16.97% 445.65 38.99% 4.78
VoT 61.51% 1514.34 32.38% 417.44 27.33% 400.96 24.74% 711.91 13.42% 295.53 16.83% 444.76 38.05% 4.69
ReasonCast (agent-routed)39.10% 1080.71 25.08% 331.09 21.06% 322.24 20.89% 589.94 9.71%215.61 12.87% 339.68 32.63% 4.00
Table 3: Forecasting performance during stable-sales periods
on the proprietary commerce dataset. Lower values are better.
The best results are highlighted in bold, and the second-best
results are underlined.
Method WMAPE MAE
Seasonal Naive 10.89% 254.82
LightGBM 11.10% 259.88
PatchTST 9.72% 227.22
iTransformer 10.26% 239.83
TimesFM 13.19% 308.73
Chronos1 8.33% 194.61
Chronos2-small7.91% 185.15
Chronos2-small (Uni-FT) 9.57% 223.80
Chronos2-small (Multi-FT) 8.85% 206.99
Time-LLM 13.34% 312.68
VoT 11.31% 264.57
ReasonCast (always-on semantics) 9.59% 224.43
ReasonCast (agent-routed)7.91% 185.15
5.6 Dissecting Selective Semantic Intervention
Table 4 tests where, how strongly, and in what form semantics enter
the forecast. Its stable-sales column forces Basic to isolate fusion
from routing; positive changes denote degradation.
Removing orthogonal decomposition–alignment degrades every
internal slice, although its M5 effect is negligible. Removing the
adaptive gate also increases WMAPE in all four slices, with much
larger changes during event-sensitive periods; this supports adap-
tive aggregate control but does not establish sample-level harm
rates. The correction paths are complementary: the additive path
improves both event regimes, whereas the multiplicative path is
especially important for the large holiday level shift. Under forced
Basic, simplified fusion can perform better on stable sales, con-
firming that unnecessary semantics still add noise; discrete routing
removes this failure mode through the exact no-text path.
5.7 Reasoner Post-Training: From Semantic
Fidelity to Forecast Utility
We evaluate cumulative reasoner stages with the same frozen fu-
sion forecaster; only the reasoning policy changes. Event WMAPE
pools the absolute-error numerator and demand denominator over
holiday- and mega-sale-sensitive slices. For seven-day instance𝑖,
letℓ𝑚 𝑖 = ˝ ℎ|𝑦𝑖,ℎ− ˆ𝑦𝑚 𝑖,ℎ|/(˝ ℎ|𝑦𝑖,ℎ|+𝜖) . We retain the sample-level
negative transfer rate NTR=𝑁 −1 ˝ 𝑖 I[ℓ text 𝑖 >ℓ no-text 𝑖 ], using the
exact no-text path of the same frozen forecaster.
SFT establishes parseability and improves direction and shape;
semantic-field RL further calibrates direction, amplitude, and peak.
Forecast-utility RL targets Event WMAPE and NTR while preserv-
ing semantic fidelity, separating well-formed text from interven-
tions that improve the final forecast.
5.8 Entropy-Adaptive Semantic Intervention
We isolate continuous gate control after a non-skip route. Within
each forecast window, item–window pairs are grouped into entropy
tertiles and compared with a global- 𝛼 control that replaces the
instance-wise gate with one shared additive coefficient.
Figure 2 links higher no-text entropy to stronger semantic cor-
rection. Adaptive gating outperforms global𝛼 in every tier, with
larger gains at medium and high entropy, showing that intervention
strength tracks the reliability of the numerical forecast.
Semantic inversion stress test.We invert all six structured seman-
tic fields and the trend narrative while holding the time series,
checkpoint, and inference configuration fixed. Incorrect semantics
increase WMAPE in 13 of 15 windows, with mean and median in-
creases of 2.67 and 0.76 percentage points and a worst-case increase
of 25.33 points. Thus, the forecast responds to semantic content
rather than merely to the presence of text; gating attenuates many

ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning Preprint, August 2026,
Table 4: Selective-fusion ablations (WMAPE/MAE). The stable-sales column forcesBasicto isolate fusion from routing. Gray
values report changes from the full fusion mechanism as WMAPE percentage points / relative MAE (%); positive values indicate
degradation. Lower is better.
Design axis Variant Holiday Sens. Mega-sale Sens.
Stable-sales
(forced Basic) M5
Full fusion mechanism
39.10% / 1080.71
reference
20.89% / 589.94
reference
9.59% / 224.43
reference
32.63% / 4.00
reference
Interaction targetw/o orthogonal decomposition–alignment
40.04% / 1155.23
Δ+0.94 pp/+6.90%
21.14% / 596.19
Δ+0.25 pp/+1.06%
11.31% / 264.57
Δ+1.72 pp/+17.89%
32.64% / 4.00
Δ+0.01 pp/+0.00%
Intervention strengthw/o adaptive semantic gate
39.76% / 1112.21
Δ+0.66 pp/+2.91%
21.54% / 608.01
Δ+0.65 pp/+3.06%
9.64% / 225.53
Δ+0.05 pp/+0.49%
32.64% / 4.01
Δ+0.01 pp/+0.25%
Correction formw/o additive correction
40.12% / 1189.98
Δ+1.02 pp/+10.11%
22.14% / 622.09
Δ+1.25 pp/+5.45%
8.85% / 206.99
Δ−0.74 pp/−7.77%
32.84% / 4.03
Δ+0.21 pp/+0.75%
w/o multiplicative correction
44.29% / 1159.19
Δ+5.19 pp/+7.26%
20.89% / 589.95
Δ+0.00 pp/+0.00%
9.59% / 224.43
Δ+0.00 pp/+0.00%
32.65% / 4.01
Δ+0.02 pp/+0.25%
ReferenceBase fusion only
44.30% / 1229.05
Δ+5.20 pp/+13.73%
21.50% / 606.18
Δ+0.61 pp/+2.75%
8.74% / 204.43
Δ−0.85 pp/−8.91%
33.03% / 4.04
Δ+0.40 pp/+1.00%
Table 5: Semantic fidelity and downstream forecast utility across cumulative reasoner post-training stages. Event WMAPE
pools holiday-sensitive and mega-sale-sensitive observations. Negative Transfer Rate is the proportion of instances for which
text-conditioned seven-day normalized absolute error exceeds the exact no-text forecast from the same frozen forecaster.
Arrows indicate whether higher or lower values are better.
Training stage
Parse
Rate↑
Direction
MAE↓
Shape
Weighted-F1↑
Amplitude
log-MAE↓
Peak
log-MAE↓
Event
WMAPE↓
Negative Transfer
Rate↓
Original LLM 91.36% 1.14 0.25 0.44 0.54 20.52% 23.59%
+ Schema SFT 100.00% 0.91 0.34 0.44 0.53 19.48% 16.20%
+ Semantic-Field RL (GRPO) 100.00% 0.85 0.33 0.39 0.52 19.16% 16.03%
+ Forecast-Utility RL (GRPO) 100.00% 0.83 0.35 0.38 0.53 18.96% 15.08%
corruptions but does not guarantee per-window immunity. Full
window-level results appear in Table 10.
6 Discussion
Our results support interpreting event-enhanced forecasting as
conditional intervention rather than uniform multimodal fusion.
ReasonCast yields its clearest gains when future context supplies
information that is difficult to recover from historical demand
alone: relative to the strongest non-ReasonCast baselines, it re-
duces WMAPE by 7.8% on holiday-sensitive categories, 5.6% on
mega-sale-sensitive categories, and 1.4% on M5 event windows. In
contrast, forcing semantic intervention during stable-sales periods
increases WMAPE from 7.91% to 9.59%. This asymmetry is central
to our formulation: semantic context has regime-dependent mar-
ginal utility and should modify a strong numerical forecaster only
when it contributes information beyond the observed history.
The analyses further explain how ReasonCast realizes this princi-
ple. Discrete routing and continuous gating determine when seman-
tic reasoning is invoked and how strongly it influences the forecast;
the orthogonal decomposition determines where interaction occurs
by restricting the semantic query interface to event-related tempo-
ral components; and the additive and multiplicative paths express
different forms of correction. Removing orthogonal decomposition
and alignment degrades all evaluated slices, while the multiplicative
path is particularly important for holiday-driven level shifts. The
additive path improves event-sensitive forecasts but can be harm-
ful when intervention is unnecessarily forced on stable demand.
Adaptive gating also outperforms a global-strength control across
all forecast-entropy tiers, assigning greater influence to semantics
when the numerical forecast is less reliable. Finally, semantic in-
version increases WMAPE in 13 of 15 windows, confirming that
the forecast responds to semantic content rather than merely to
the presence of text. These results support forecast-conditioned
semantic interaction, although they do not imply that the learned
event subspace is a causally identifiable factor.
The stable-sales analysis clarifies the distinct roles of routing
and fusion. In Table 4, the stable-sales column deliberately over-
rides the routing policy and forces every instance to take theBasic
route. It therefore diagnoses how the fusion mechanism behaves
under unnecessary intervention rather than reporting end-to-end
ReasonCast performance. In deployment, the agent may instead
chooseSkip, disable both correction paths, and exactly recover the
numerical backbone. The evidence thus supports two narrower
claims: the fusion components improve forecasting when semantic
intervention is warranted, while the exact-identity skip path pre-
vents the model from systematically modifying the backbone when
no intervention is selected. It does not imply that the fusion gate
alone guarantees the absence of sample-level negative transfer.
The post-training results highlight a related distinction between
semantic fidelity and forecast utility. Schema SFT establishes

Preprint, August 2026, Ziyue Yang, Chaolin Xu, Yijing Wang, Tiankai Gu, Hui Yang, Yanhong Lin, Kaiyuan Liu, and Fei Xiao
Prediction uncertainty− →
(a) Backbone WMAPE (%)
10
25
40
12.12
22.38
36.58
(b) Additive injection magnitude|αg i|
0.28
0.33
0.38 Only-α: 0.343
0.307
0.340
0.367
(c) WMAPE gain over only-αcontrol (pp)
0.0
0.2
0.4
+0.11
+0.37
+0.15
Low
meanH=−1.55
Medium
meanH=−0.41
High
meanH= 0.42
Figure 2: Entropy-adaptive semantic intervention across
within-window forecast-entropy tertiles. (a) WMAPE of the
no-text backbone; (b) mean additive-injection magnitude|𝑔𝑖|,
with the dashed line denoting the global- 𝛼 control; and (c)
WMAPE gain over that control in percentage points.
parseable and internally consistent outputs, and semantic-field RL
improves forecast-critical judgments such as direction, amplitude,
and peak intensity. Forecast-utility RL then evaluates valid candi-
dates through a frozen forecaster, incorporating marginal predictive
improvement, potential harm, and tool cost into the reasoning
objective. This separation is important because well-formed event
descriptions are not necessarily useful interventions.
Several broader challenges remain for deploying event-aware
forecasting systems. Event effects are intrinsically non-stationary
across products, regions, and seasons, requiring semantic interpre-
tation and forecast intervention to be recalibrated under distribu-
tion shift. External signals also vary in timeliness, completeness,
and reliability, making evidence validation and uncertainty-aware
reasoning essential. At production scale, tool-augmented reason-
ing introduces a fundamental trade-off among predictive accuracy,
latency, and computational cost, while sparse counterfactual obser-
vations make it difficult to separate forecast-relevant associations
from causal event effects. A specific limitation of the current study
is that it does not yet provide a complete accounting of tool-call
frequency, end-to-end latency, or realized inference cost. Future
work may combine online adaptation, calibrated abstention, source-
reliability modeling, and resource-aware routing to make semantic
intervention more robust and operationally efficient.
7 Conclusion
We presented ReasonCast, an agentic framework that treats event
semantics as a routed intervention rather than an always-on fore-
casting input. The agent selects among no intervention, low-cost
structured reasoning, and tool-augmented reasoning, while continu-
ous gating controls intervention strength after a non-skip decision.
Schema SFT, semantic-field RL, and forecast-utility RL progres-
sively align structured reasoning with downstream predictive value.
The results show that forecast-aligned routing can exploit contex-
tual signals during event-driven shifts while exactly preserving
the numerical backbone when semantics are unnecessary, thereby
avoiding systematic negative transfer in stable-sales periods.
References
[1] Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken, Andreas Auer, Boran Han,
Pedro Mercado, Syama Sundar Rangapuram, Huibin Shen, Lorenzo Stella, Xiyuan
Zhang, et al . 2025. Chronos-2: From Univariate to Universal Forecasting.
arXiv:2510.15821 [cs.LG] doi:10.48550/arXiv.2510.15821
[2] Abdul Fatir Ansari, Lorenzo Stella, Ali Caner Turkmen, Xiyuan Zhang, Pedro
Mercado, Huibin Shen, Oleksandr Shchur, Syama Sundar Rangapuram, Sebastian
Pineda-Arango, Shubham Kapoor, Jasper Zschiegner, Danielle C. Maddix, Hao
Wang, Michael W. Mahoney, Kari Torkkola, Andrew Gordon Wilson, Michael
Bohlke-Schneider, and Bernie Wang. 2024. Chronos: Learning the Language of
Time Series. Transactions on Machine Learning Research. https://openreview.
net/forum?id=gerNCVqqtR
[3] Defu Cao, Furong Jia, Sercan Ö. Arik, Tomas Pfister, Yixiang Zheng, Wen Ye, and
Yan Liu. 2024. TEMPO: Prompt-Based Generative Pre-Trained Transformer for
Time Series Forecasting. International Conference on Learning Representations.
https://openreview.net/forum?id=YH5w12OUuU
[4] Abhimanyu Das, Weihao Kong, Rajat Sen, and Yichen Zhou. 2024. A Decoder-
Only Foundation Model for Time-Series Forecasting. InProceedings of the 41st
International Conference on Machine Learning (Proceedings of Machine Learning
Research, Vol. 235). PMLR, Vienna, Austria, 10148–10167. https://proceedings.
mlr.press/v235/das24c.html
[5] Mononito Goswami, Konrad Szafer, Arjun Choudhry, Yifu Cai, Shuo Li, and
Artur Dubrawski. 2024. MOMENT: A Family of Open Time-Series Foundation
Models. InProceedings of the 41st International Conference on Machine Learning
(Proceedings of Machine Learning Research, Vol. 235). PMLR, Vienna, Austria,
16115–16152. https://proceedings.mlr.press/v235/goswami24a.html
[6] Nate Gruver, Marc Finzi, Shikai Qiu, and Andrew Gordon Wilson. 2023. Large
Language Models Are Zero-Shot Time Series Forecasters. Advances in Neural In-
formation Processing Systems. https://proceedings.neurips.cc/paper_files/paper/
2023/hash/3eb7ca52e8207697361b2c0fb3926511-Abstract-Conference.html
[7] Chao Jia, Yinfei Yang, Ye Xia, Yi-Ting Chen, Zarana Parekh, Hieu Pham, Quoc V.
Le, Yun-Hsuan Sung, Zhen Li, and Tom Duerig. 2021. Scaling Up Visual
and Vision-Language Representation Learning With Noisy Text Supervision.
InProceedings of the 38th International Conference on Machine Learning (Pro-
ceedings of Machine Learning Research, Vol. 139). PMLR, Virtual, 4904–4916.
https://proceedings.mlr.press/v139/jia21b.html
[8] Furong Jia, Kevin Wang, Yixiang Zheng, Defu Cao, and Yan Liu. 2024. GPT4MTS:
Prompt-Based Large Language Model for Multimodal Time-Series Forecasting.
Proceedings of the AAAI Conference on Artificial Intelligence38, 21 (2024), 23343–
23351. doi:10.1609/aaai.v38i21.30383
[9] Shuning Jia, Baijun Song, Canming Ye, and Chun Yuan. 2026. M3Time: LLM-
Enhanced Multi-Modal, Multi-Scale, and Multi-Frequency Multivariate Time
Series Forecasting.Proceedings of the AAAI Conference on Artificial Intelligence
40, 27 (2026), 22265–22273. doi:10.1609/aaai.v40i27.39383
[10] Ming Jin, Shiyu Wang, Lintao Ma, Zhixuan Chu, James Y. Zhang, Xi-
aoming Shi, Pin-Yu Chen, Yuxuan Liang, Yuan-Fang Li, Shirui Pan, and
Qingsong Wen. 2024. Time-LLM: Time Series Forecasting by Repro-
gramming Large Language Models. International Conference on Learn-
ing Representations. https://proceedings.iclr.cc/paper_files/paper/2024/hash/
680b2a8135b9c71278a09cafb605869e-Abstract-Conference.html
[11] Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma,
Qiwei Ye, and Tie-Yan Liu. 2017. LightGBM: A Highly Efficient Gradient Boosting
Decision Tree. InAdvances in Neural Information Processing Systems, Vol. 30.
Curran Associates, Inc., Long Beach, CA, USA, 3146–3154. https://proceedings.
neurips.cc/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html
[12] Zihao Li, Xiao Lin, Zhining Liu, Jiaru Zou, Ziwei Wu, Lecheng Zheng, Dongqi Fu,
Yada Zhu, Hendrik Hamann, Hanghang Tong, and Jingrui He. 2026. Language
in the Flow of Time: Time-Series-Paired Texts Weaved into a Unified Temporal
Narrative. International Conference on Learning Representations. https://

ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning Preprint, August 2026,
openreview.net/forum?id=a1zBg9cBvt
[13] Bryan Lim, Sercan Ö. Arik, Nicolas Loeff, and Tomas Pfister. 2021. Temporal
Fusion Transformers for Interpretable Multi-Horizon Time Series Forecasting.
International Journal of Forecasting37, 4 (2021), 1748–1764. doi:10.1016/j.ijforecast.
2021.03.012
[14] Haoxin Liu, Shangqing Xu, Zhiyuan Zhao, Lingkai Kong, Harshavardhan Ka-
marthi, Aditya B. Sasanur, Megha Sharma, Jiaming Cui, Qingsong Wen, Chao
Zhang, and B. Aditya Prakash. 2024. Time-MMD: Multi-Domain Multimodal
Dataset for Time Series Analysis. Advances in Neural Information Processing
Systems. doi:10.52202/079017-2476
[15] Peiyuan Liu, Hang Guo, Tao Dai, Naiqi Li, Jigang Bao, Xudong Ren, Yong Jiang,
and Shu-Tao Xia. 2025. CALF: Aligning LLMs for Time Series Forecasting via
Cross-Modal Fine-Tuning.Proceedings of the AAAI Conference on Artificial Intel-
ligence39, 18 (2025), 18915–18923. doi:10.1609/aaai.v39i18.34082
[16] Xu Liu, Junfeng Hu, Yuan Li, Shizhe Diao, Yuxuan Liang, Bryan Hooi, and Roger
Zimmermann. 2024. UniTime: A Language-Empowered Unified Model for Cross-
Domain Time Series Forecasting. InProceedings of the ACM Web Conference
2024. Association for Computing Machinery, Singapore, 4095–4106. doi:10.1145/
3589334.3645434
[17] Xu Liu, Juncheng Liu, Gerald Woo, Taha Aksu, Yuxuan Liang, Roger Zimmer-
mann, Chenghao Liu, Junnan Li, Silvio Savarese, Caiming Xiong, and Doyen Sa-
hoo. 2025. Moirai-MoE: Empowering Time Series Foundation Models with Sparse
Mixture of Experts. InProceedings of the 42nd International Conference on Machine
Learning (Proceedings of Machine Learning Research, Vol. 267). PMLR, Vancouver,
BC, Canada, 38940–38962. https://proceedings.mlr.press/v267/liu25an.html
[18] Yong Liu, Tengge Hu, Haoran Zhang, Haixu Wu, Shiyu Wang, Lintao Ma, and
Mingsheng Long. 2024. iTransformer: Inverted Transformers Are Effective for
Time Series Forecasting. International Conference on Learning Representations.
https://openreview.net/forum?id=JePfAI8fah
[19] Yong Liu, Guo Qin, Xiangdong Huang, Jianmin Wang, and Mingsheng Long. 2024.
AutoTimes: Autoregressive Time Series Forecasters via Large Language Models.
Advances in Neural Information Processing Systems. doi:10.52202/079017-3882
[20] Yong Liu, Guo Qin, Xiangdong Huang, Jianmin Wang, and Mingsheng Long.
2025. Timer-XL: Long-Context Transformers for Unified Time Series Forecasting.
International Conference on Learning Representations. https://openreview.net/
forum?id=KMCJXjlDDr
[21] Yong Liu, Guo Qin, Zhiyuan Shi, Zhi Chen, Caiyin Yang, Xiangdong Huang,
Jianmin Wang, and Mingsheng Long. 2025. Sundial: A Family of Highly Capable
Time Series Foundation Models. InProceedings of the 42nd International Conference
on Machine Learning (Proceedings of Machine Learning Research, Vol. 267). PMLR,
Vancouver, BC, Canada, 39295–39317. https://proceedings.mlr.press/v267/liu25be.
html
[22] Yong Liu, Haoran Zhang, Chenyu Li, Xiangdong Huang, Jianmin Wang, and
Mingsheng Long. 2024. Timer: Generative Pre-trained Transformers Are Large
Time Series Models. InProceedings of the 41st International Conference on Machine
Learning (Proceedings of Machine Learning Research, Vol. 235). PMLR, Vienna,
Austria, 32369–32399. https://proceedings.mlr.press/v235/liu24cb.html
[23] Spyros Makridakis, Evangelos Spiliotis, and Vassilios Assimakopoulos. 2022. M5
Accuracy Competition: Results, Findings, and Conclusions.International Journal
of Forecasting38, 4 (2022), 1346–1364. doi:10.1016/j.ijforecast.2021.11.013
[24] Yuqi Nie, Nam H. Nguyen, Phanwadee Sinthong, and Jayant Kalagnanam. 2023.
A Time Series Is Worth 64 Words: Long-Term Forecasting with Transformers.
International Conference on Learning Representations. https://openreview.net/
forum?id=Jbdc0vTOcol
[25] David Salinas, Valentin Flunkert, Jan Gasthaus, and Tim Januschowski. 2020.
DeepAR: Probabilistic Forecasting with Autoregressive Recurrent Networks.
International Journal of Forecasting36, 3 (2020), 1181–1191. doi:10.1016/j.ijforecast.
2019.07.001
[26] Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli,
Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. 2023. Toolformer:
Language Models Can Teach Themselves to Use Tools. Advances in Neural Infor-
mation Processing Systems. https://proceedings.neurips.cc/paper_files/paper/
2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html
[27] Chenxi Sun, Hongyan Li, Yaliang Li, and Shenda Hong. 2024. TEST: Text
Prototype Aligned Embedding to Activate LLM’s Ability for Time Series.
International Conference on Learning Representations. https://proceedings.iclr.
cc/paper_files/paper/2024/hash/a4352e2c9d93582898a2a20e1f514e8f-Abstract-
Conference.html
[28] Mingtian Tan, Mike A. Merrill, Vinayak Gupta, Tim Althoff, and Thomas
Hartvigsen. 2024. Are Language Models Actually Useful for Time Series Forecast-
ing? Advances in Neural Information Processing Systems. doi:10.52202/079017-
1922
[29] Chengsen Wang, Qi Qi, Jingyu Wang, Haifeng Sun, Zirui Zhuang, Jinming Wu,
Lei Zhang, and Jianxin Liao. 2025. ChatTime: A Unified Multimodal Time Series
Foundation Model Bridging Numerical and Textual Data. InProceedings of the
AAAI Conference on Artificial Intelligence, Vol. 39. AAAI Press, Philadelphia, PA,
USA, 12694–12702. doi:10.1609/aaai.v39i12.33384
[30] Siyuan Wang, Peng Chen, Yihang Wang, Wanghui Qiu, Chenjuan Guo, Bin Yang,
and Yang Shu. 2026. Unlocking the Value of Text: Event-Driven Reasoning and
Multi-Level Alignment for Time Series Forecasting. International Conference on
Learning Representations. https://openreview.net/forum?id=0TAFiyHgEl
[31] Shiyu Wang, Haixu Wu, Xiaoming Shi, Tengge Hu, Huakun Luo, Lintao Ma,
James Y. Zhang, and Jun Zhou. 2024. TimeMixer: Decomposable Multiscale
Mixing for Time Series Forecasting. International Conference on Learning
Representations. https://openreview.net/forum?id=7oLshfEIC2
[32] Xinlei Wang, Maike Feng, Jing Qiu, Jinjin Gu, and Junhua Zhao. 2024. From News
to Forecast: Integrating Event Analysis in LLM-Based Time Series Forecasting
with Reflection. InAdvances in Neural Information Processing Systems, Vol. 37.
Curran Associates, Inc., Vancouver, BC, Canada, 58118–58153. doi:10.52202/
079017-1853
[33] Yuxuan Wang, Haixu Wu, Jiaxiang Dong, Guo Qin, Haoran Zhang, Yong Liu,
Yunzhong Qiu, Jianmin Wang, and Mingsheng Long. 2024. TimeXer: Empowering
Transformers for Time Series Forecasting with Exogenous Variables. Advances
in Neural Information Processing Systems. doi:10.52202/079017-0015
[34] Andrew Robert Williams, Arjun Ashok, Étienne Marcotte, Valentina Zantedeschi,
Jithendaraa Subramanian, Roland Riachi, James Requeima, Alexandre Lacoste,
Irina Rish, Nicolas Chapados, and Alexandre Drouin. 2025. Context is Key: A
Benchmark for Forecasting with Essential Textual Information. InProceedings of
the 42nd International Conference on Machine Learning (Proceedings of Machine
Learning Research, Vol. 267). PMLR, Vancouver, BC, Canada, 66887–66944. https:
//proceedings.mlr.press/v267/williams25a.html
[35] Gerald Woo, Chenghao Liu, Akshat Kumar, Caiming Xiong, Silvio Savarese,
and Doyen Sahoo. 2024. Unified Training of Universal Time Series Forecasting
Transformers. InProceedings of the 41st International Conference on Machine
Learning (Proceedings of Machine Learning Research, Vol. 235). PMLR, Vienna,
Austria, 53140–53164. https://proceedings.mlr.press/v235/woo24a.html
[36] Xingjian Wu, Jianxin Jin, Wanghui Qiu, Peng Chen, Yang Shu, Bin Yang, and
Chenjuan Guo. 2026. Aurora: Towards Universal Generative Multimodal Time
Series Forecasting. International Conference on Learning Representations. https:
//openreview.net/forum?id=VVJ6Ck9JBl
[37] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng,
Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. 2025. Qwen3 Technical
Report. arXiv:2505.09388 [cs.CL] doi:10.48550/arXiv.2505.09388
[38] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R. Narasimhan,
and Yuan Cao. 2023. ReAct: Synergizing Reasoning and Acting in Language Mod-
els. International Conference on Learning Representations. https://openreview.
net/forum?id=WE_vluYUL-X
[39] Ailing Zeng, Muxi Chen, Lei Zhang, and Qiang Xu. 2023. Are Transformers
Effective for Time Series Forecasting?. InProceedings of the AAAI Conference on
Artificial Intelligence, Vol. 37. AAAI Press, Washington, DC, USA, 11121–11128.
doi:10.1609/aaai.v37i9.26317
[40] Xiyuan Zhang, Boran Han, Haoyang Fang, Abdul Fatir Ansari, Shuai Zhang,
Danielle C. Maddix, Cuixiong Hu, Andrew Gordon Wilson, Michael W. Mahoney,
Hao Wang, Yan Liu, Michael Bohlke-Schneider, Huzefa Rangwala, George Karypis,
and Bernie Wang. 2026. When Does Multimodality Lead to Better Time Series
Forecasting? Transactions on Machine Learning Research. https://dblp.org/rec/
journals/tmlr/ZhangHFAZMHWMWLBRKW26
[41] Shiqiao Zhou, Holger Schöner, Huanbo Lyu, Edouard Fouché, and Shuo Wang.
2025. BALM-TSF: Balanced Multimodal Alignment for LLM-Based Time Series
Forecasting. InProceedings of the 34th ACM International Conference on Informa-
tion and Knowledge Management. Association for Computing Machinery, Seoul,
Republic of Korea, 4498–4508. doi:10.1145/3746252.3761278
[42] Tian Zhou, Peisong Niu, Xue Wang, Liang Sun, and Rong Jin. 2023. One Fits All:
Power General Time Series Analysis by Pretrained LM. InAdvances in Neural
Information Processing Systems, Vol. 36. Curran Associates, Inc., New Orleans,
LA, USA, 43322–43355. https://proceedings.neurips.cc/paper_files/paper/2023/
hash/86c17de05579cde52025f9984e6e2ebb-Abstract-Conference.html

Preprint, August 2026, Ziyue Yang, Chaolin Xu, Yijing Wang, Tiankai Gu, Hui Yang, Yanhong Lin, Kaiyuan Liu, and Fei Xiao
A Detailed Window-Level Results
This appendix reports the unaggregated seven-day forecast windows underlying the main-text averages. Each cell contains WMAPE and MAE
for exactly the same items, forecast origin, and horizon; no window-specific model selection is performed. For compactness, Chronos2-small
is abbreviated as C2-small and the time-series backbone as TS backb.
A.1 Commerce Dataset
Tables 6 and 7 contain the 15 commerce windows in chronological
blocks: three mega-sale windows, ten holiday windows, and two
stable-sales windows. The split across two tables is purely presenta-
tional; the rows and evaluation protocol are identical.
The hardest cases are the two Spring Festival–Valentine windows be-
ginning on February 12 and February 15. On February 12, ReasonCast
reduces WMAPE from 108.75% for the strongest non-ReasonCast
comparator in its table to 83.85%; on February 15 it further reduces
the best comparator from 28.77% to 24.53%. These windows combine
a sharp holiday regime change with overlapping event semantics,
precisely the setting in which history-only extrapolation is least
reliable.
The stable-sales rows provide an important counterpoint. Reason-
Cast is not the best model on January 13 or March 23: several purely
numerical models attain lower error. The aggregate benefit therefore
does not come from uniformly overriding the backbone. Instead, the
detailed rows support the intended division of labor: semantic inter-
vention is most useful when future events add information absent
from the observed history, whereas the numerical backbone remains
highly competitive when demand is stable.
A.2 M5 Dataset
Tables 8 and 9 report all 14 M5 event windows. Each holiday is
evaluated at two forecast origins, which prevents a single favorable
alignment between the event day and horizon from determining the
aggregate result.
The public benchmark has a different error profile from the com-
merce data. Absolute differences are smaller, but ReasonCast remains
consistently competitive across Halloween, New Year, Super Bowl,
Easter, and Mother’s Day origins. It does not dominate every ori-
gin: the time-series backbone is slightly better on the first Christ-
mas origin, and the covariate baseline is slightly better on the first
Thanksgiving origin. Reporting both origins therefore exposes where
semantic context helps and where a strong numerical model already
captures most of the predictable event pattern.
Table 6: Commerce window-level results, baseline group A. Each method occupies a WMAPE (%) and MAE pair. Rows 1–3 are
mega-sale windows, rows 4–13 are holiday windows, and rows 14–15 are stable-sales windows.
SNaive LightGBM PatchTST iTransformer TimesFM C2-small
Window WMAPE MAE WMAPE MAE WMAPE MAE WMAPE MAE WMAPE MAE WMAPE MAE
2025-11-11 19.61% 547.89 18.44% 515.27 19.68% 550.02 19.63% 548.61 23.87% 667.14 18.03% 509.35
2025-12-08 15.55% 392.93 17.21% 434.92 10.72% 270.99 12.40% 313.53 15.12% 382.17 15.94% 406.74
2025-12-11 14.51% 363.26 13.04% 326.56 9.84% 246.23 11.43% 286.05 13.89% 347.66 9.94% 251.24
2026-01-01 18.68% 446.77 17.61% 421.21 18.82% 450.14 18.36% 439.06 19.72% 471.68 29.83% 719.76
2026-02-12 210.75% 1614.50 169.72% 1300.13 175.83% 1347.00 159.53% 1222.10 186.35% 1427.55 138.84% 1070.39
2026-02-15 131.99% 1077.18 54.45% 444.35 107.73% 879.20 53.02% 432.70 67.55% 551.23 48.13% 395.08
2026-03-02 16.67% 397.63 15.35% 366.01 12.78% 304.67 14.74% 351.40 15.92% 379.54 15.11% 362.31
2026-03-05 14.25% 336.66 12.75% 301.27 12.37% 292.26 14.06% 332.20 17.03% 402.42 12.23% 290.56
2026-04-28 20.43% 388.59 19.54% 371.61 20.23% 384.60 21.66% 411.86 29.08% 553.03 20.86% 396.73
2026-05-04 23.19% 534.31 16.59% 382.22 16.47% 379.51 17.25% 397.43 19.30% 444.67 19.84% 457.16
2026-05-10 16.17% 391.96 14.31% 346.96 13.93% 337.68 14.39% 348.90 14.68% 355.83 11.73% 284.37
2026-05-16 11.51% 280.86 10.82% 263.98 9.52% 232.32 12.55% 306.24 10.80% 263.47 8.03% 195.89
2026-05-19 10.23% 250.58 11.14% 273.05 10.10% 247.35 10.80% 264.61 13.27% 325.10 8.22% 201.46
2026-01-13 10.02% 236.73 10.88% 257.11 8.46% 199.75 9.10% 214.96 13.12% 309.89 7.49% 176.95
2026-03-23 11.77% 272.90 11.33% 262.64 10.98% 254.70 11.41% 264.70 13.26% 307.57 8.34% 193.35

ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning Preprint, August 2026,
Table 7: Commerce window-level results, baseline group B and ReasonCast. Each method occupies a WMAPE (%) and MAE pair.
TS backb. + covariates Chronos Time-LLM VoTReasonCast
Window WMAPE MAE WMAPE MAE WMAPE MAE WMAPE MAE WMAPE MAE WMAPE MAE
2025-11-11 18.04% 504.26 17.74% 495.69 17.67% 493.82 20.11% 561.93 22.86% 638.72 17.18% 480.21
2025-12-08 13.31% 336.44 11.61% 293.52 16.84% 425.55 16.42% 415.09 15.13% 382.42 11.25% 284.27
2025-12-11 12.30% 307.93 10.69% 267.51 10.20% 255.44 14.38% 359.93 12.51% 313.13 10.17% 254.56
2026-01-01 24.92% 596.10 27.36% 654.40 27.72% 663.06 15.69% 375.23 19.89% 475.70 22.29% 533.21
2026-02-12 131.66% 1008.59 116.26% 890.61 141.52% 1084.17 210.34% 1611.33 108.75% 833.09 83.85% 642.36
2026-02-15 35.95% 293.38 28.77% 234.77 33.26% 271.42 136.70% 1115.56 42.28% 345.02 24.53% 200.21
2026-03-02 11.09% 264.51 10.82% 258.05 14.24% 339.45 16.67% 397.43 16.19% 386.05 10.65% 253.93
2026-03-05 9.03% 213.45 8.88% 209.76 10.79% 254.92 15.62% 369.00 12.63% 298.44 8.78% 207.43
2026-04-28 14.44% 274.63 13.13% 249.78 20.35% 386.90 20.34% 386.70 17.95% 341.31 12.52% 238.09
2026-05-04 17.88% 411.98 16.83% 387.78 20.32% 468.08 19.92% 458.93 18.32% 422.06 16.34% 376.43
2026-05-10 15.42% 373.72 14.70% 356.27 13.05% 316.35 13.34% 323.52 16.22% 393.13 13.76% 333.46
2026-05-16 9.78% 238.51 10.01% 244.12 7.56% 184.29 10.45% 254.90 11.48% 280.11 9.07% 221.16
2026-05-19 8.69% 213.02 9.10% 223.05 8.23% 201.68 11.20% 274.46 9.58% 234.69 8.82% 216.14
2026-01-13 8.43% 199.07 8.43% 199.24 6.91% 163.30 15.35% 362.56 10.59% 250.25 9.60% 226.74
2026-03-23 10.72% 248.52 9.26% 214.74 9.74% 225.93 11.33% 262.80 12.03% 278.88 9.58% 222.12
Table 8: M5 window-level results, baseline group A. Each method occupies a WMAPE (%) and MAE pair.
SNaive LightGBM PatchTST iTransformer TimesFM C2-small
Event and origin WMAPE MAE WMAPE MAE WMAPE MAE WMAPE MAE WMAPE MAE WMAPE MAE
Halloween 10-25 37.20% 4.55 29.25% 3.58 45.65% 5.59 29.45% 3.61 29.84% 3.65 29.29% 3.59
Halloween 10-31 38.36% 4.86 30.46% 3.86 44.79% 5.68 30.71% 3.89 30.17% 3.82 29.38% 3.72
Thanksgiving 11-21 46.84% 5.45 35.41% 4.12 53.78% 6.26 36.71% 4.27 37.91% 4.41 36.64% 4.27
Thanksgiving 11-24 50.78% 5.46 37.95% 4.08 56.76% 6.11 41.32% 4.44 41.86% 4.50 41.30% 4.44
Christmas 12-21 59.59% 6.17 49.74% 5.15 68.18% 7.06 49.61% 5.13 50.30% 5.21 49.69% 5.14
Christmas 12-24 64.00% 6.18 51.91% 5.01 71.71% 6.92 52.24% 5.04 53.95% 5.21 54.07% 5.22
NewYear 12-27 52.48% 6.19 35.05% 4.14 49.38% 5.83 34.11% 4.02 33.76% 3.98 33.91% 4.00
NewYear 12-30 49.21% 6.25 33.68% 4.28 46.54% 5.91 32.62% 4.14 32.30% 4.10 32.79% 4.16
SuperBowl 02-01 37.92% 5.22 29.63% 4.07 42.02% 5.78 30.21% 4.15 29.82% 4.10 30.04% 4.13
SuperBowl 02-07 40.13% 5.72 30.98% 4.41 41.19% 5.87 31.03% 4.42 30.65% 4.37 31.17% 4.44
Easter 03-23 37.29% 4.97 29.70% 3.96 41.53% 5.54 29.23% 3.90 29.57% 3.94 29.89% 3.98
Easter 03-26 37.90% 5.02 28.55% 3.78 41.63% 5.51 29.50% 3.91 30.03% 3.98 30.20% 4.00
Mothers day 05-04 36.55% 5.31 27.77% 4.03 36.62% 5.32 27.95% 4.06 28.01% 4.07 27.26% 3.96
Mothers day 05-07 35.45% 5.19 26.71% 3.91 36.58% 5.35 26.82% 3.93 26.65% 3.90 25.95% 3.80

Preprint, August 2026, Ziyue Yang, Chaolin Xu, Yijing Wang, Tiankai Gu, Hui Yang, Yanhong Lin, Kaiyuan Liu, and Fei Xiao
Table 9: M5 window-level results, baseline group B and ReasonCast. Each method occupies a WMAPE (%) and MAE pair.
TS backb. + covariates Chronos Time-LLM VoTReasonCast
Event and origin WMAPE MAE WMAPE MAE WMAPE MAE WMAPE MAE WMAPE MAE WMAPE MAE
Halloween 10-25 29.59% 3.62 29.24% 3.58 30.50% 3.73 35.20% 4.31 33.53% 4.11 28.83% 3.53
Halloween 10-31 30.52% 3.87 29.76% 3.77 30.55% 3.87 35.21% 4.46 35.73% 4.53 29.52% 3.74
Thanksgiving 11-21 33.77% 3.93 33.46% 3.89 37.69% 4.39 42.81% 4.98 38.81% 4.52 33.81% 3.94
Thanksgiving 11-24 35.85% 3.86 36.40% 3.92 41.53% 4.47 45.59% 4.90 39.83% 4.28 35.71% 3.84
Christmas 12-21 47.10% 4.87 47.72% 4.94 50.25% 5.20 54.21% 5.61 53.72% 5.56 48.34% 5.00
Christmas 12-24 48.43% 4.67 48.65% 4.69 54.20% 5.23 57.83% 5.58 52.18% 5.04 48.46% 4.68
NewYear 12-27 33.74% 3.98 33.14% 3.91 35.64% 4.21 37.86% 4.47 37.64% 4.44 32.49% 3.83
NewYear 12-30 32.65% 4.14 32.59% 4.14 34.97% 4.44 38.05% 4.83 39.46% 5.01 31.53% 4.00
SuperBowl 02-01 29.33% 4.03 29.35% 4.04 31.00% 4.26 34.26% 4.71 35.39% 4.87 29.18% 4.01
SuperBowl 02-07 31.36% 4.47 30.78% 4.38 31.36% 4.47 33.89% 4.83 36.16% 5.15 30.69% 4.37
Easter 03-23 29.87% 3.98 30.21% 4.03 30.40% 4.05 34.76% 4.63 33.63% 4.48 29.28% 3.90
Easter 03-26 29.18% 3.87 29.07% 3.85 30.63% 4.06 34.19% 4.53 34.63% 4.59 28.62% 3.79
Mothers day 05-04 27.36% 3.97 27.08% 3.93 28.64% 4.16 31.35% 4.55 31.25% 4.54 26.87% 3.90
Mothers day 05-07 26.19% 3.83 25.98% 3.80 27.96% 4.09 30.69% 4.49 30.72% 4.50 25.54% 3.74
A.3 Semantic Corruption Stress Test
Table 10 gives the per-window results for the controlled semantic inversion test. We invert the six control fields and the final trend narrative
while holding the time-series input, checkpoint, and inference configuration fixed. Positive ΔWMAPE denotes degradation. Incorrect
semantics increase WMAPE in 13 of 15 windows, by 2.67 percentage points on average.
The distribution is strongly right-skewed. The median increase is 0.76 percentage points, while the February 12 Spring Festival–Valentine
window increases by 25.33 points. Thus, a single aggregate mean would understate the typical harm while obscuring the severe failure mode
on a highly event-sensitive window. The two small negative deltas are also informative: gating attenuates many incorrect interventions, but
it cannot guarantee that every corrupted description worsens every finite test slice.
Table 10: Semantic inversion by window.Δis inverted minus correct WMAPE in percentage points.
Event Window
Correct
WMAPE
Inverted
WMAPEΔ
Correct
MAE
Inverted
MAE
520 2026-05-16 7.38% 7.77% 0.39 252.36 265.70
520 2026-05-19 5.78% 6.47% 0.69 218.79 244.81
Double 11 2025-11-05 13.27% 14.03% 0.76 154.35 163.25
Double 11 2025-11-08 17.54% 19.15% 1.61 959.36 1047.42
Double 11 2025-11-11 13.76% 13.62% -0.15 618.88 612.33
Double 12 2025-12-08 9.89% 11.09% 1.19 163.66 183.39
Double 12 2025-12-11 9.77% 12.15% 2.39 184.16 229.16
Labor Day 2026-04-28 7.61% 8.74% 1.14 175.76 202.01
Labor Day 2026-05-04 13.98% 14.71% 0.74 457.55 481.63
Lantern 2026-03-02 8.42% 9.61% 1.19 225.67 257.55
Mother’s Day 2026-05-10 12.35% 12.89% 0.53 403.99 421.43
New Year 2026-01-01 15.13% 15.09% -0.04 403.91 402.86
Spring–Valentine 2026-02-12 79.37% 104.69% 25.33 943.54 1244.66
Spring–Valentine 2026-02-15 21.21% 24.95% 3.74 286.61 337.10
Women’s Day 2026-03-05 7.66% 8.16% 0.50 206.44 219.89

ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning Preprint, August 2026,
B Agent Policy, Semantic Interpretation, and
Optimization Details
B.1 Agent Policy and Basic Semantic Interpreter
Prompt
We explicitly separate theagent policyfrom thesemantic interpreter.
Given the event context, the no-text forecast, and its predictive
entropy, the policy selects Skip, Basic, or Tool. Skip terminates
semantic processing and preserves the numerical backbone. Basic
invokes the semantic interpreter with the available context. Tool
first augments that context with retrieved event evidence or tempo-
ral statistics and then invokes the same interpreter. Holidays and
mega-sales disallow Skip; other instances may abstain when the
backbone is sufficiently reliable.
The fixed procedure below is therefore not the agent policy. We
retain it as theBasic semantic interpreter prompt, invoked only after
a non-skip policy decision. The Basic route supplies the original
context, whereas the Tool route supplies tool-augmented context.
All scale judgments are expressed relative to the most recent seven-
day mean.
Input: item hierarchy; forecast dates; event calendar and event
positions; recent seven-day demand, mean, and slope; no-
text forecast and entropy; current level𝐶; aligned historical
mean𝐴 and peak𝐴peak when available; platform activities;
and any policy-approved tool observations.
1: Validate the reference scale. If aligned history exists, com-
pute𝐴/𝐶 for the seven-day mean effect and𝐴peak/𝐶 for
the single-day peak; otherwise activate the no-YoY branch.
2: Assess item–event relevance from historical evidence, item
knowledge, recent slope, and event position. Do not infer
relevance solely from the presence of an event.
3: Select the dominant event when multiple events or pro-
motions overlap, and record why weaker candidates are
excluded.
4: Assign demand direction and temporal shape, explicitly
separating the seven-day mean from a concentrated single-
day peak.
5: Calibrate amplitude and peak multipliers to the recent
seven-day reference, using conservative priors when
aligned history is absent.
6: Check cross-field consistency: relevance, direction, shape,
amplitude, peak, and peak timing must describe the same
trajectory.
Return: six structured control fields plus one concise trend narrative.
Never directly generate the numerical demand forecast.
Figure 3: Basic semantic interpreter prompt used after a non-
skip policy decision. The tool route augments its input evi-
dence but does not change the output schema.
This separation also defines the roles of the three post-training
stages. Schema SFT and semantic-field RL train the semantic inter-
preter to produce valid, consistent, and calibrated forecast-specific
fields. Forecast-utility RL trains the agent policy—including route
selection, tool use, and the final intervention decision—against re-
alized downstream utility from the frozen forecaster, with explicit
penalties for negative transfer and tool cost.
Table 12: Representative compressed rationale and structured
output for a laptop forecast from March 7 to March 13, with
Women’s Day on horizon day 2.
Compressed rationale (English translation)
The window covers the March 8 platform campaign on day 2. Laptops are not a
core Women’s Day gift category, but they respond to platform-wide promotions.
Recent demand is already elevated, so the additional effect should be moderate
rather than comparable with Double 11 or 618. We therefore expect a short
peak of about1 .4× on March 8 followed by a return toward the recent level,
producing a seven-day mean of about1.2×.
Structured target
Relevance:related
Dominant event:Women’s Day
Direction:small increase
Shape:rise–fall
Amplitude:1.2
Peak:1.4
Trend:promotion-driven peak on March 8, followed by a return toward the
recent level.
B.2 Structured Fields and Representative
Rationale
Every final policy response begins with one machine-readable rout-
ing action. A Skip response terminates there and activates the
no-text path. Basic and Tool responses additionally contain six
machine-readable control fields and a short natural-language trend
narrative. Tool calls and observations belong to the intermediate
policy trajectory rather than the final output schema. The narra-
tive is encoded together with the fields, but it is not counted as an
additional control label because it has no closed label set.
Table 11: ReasonCast reasoner output schema.
Field Value space and forecasting role
Intervention ac-
tion
Skip, basic, or tool. Controls whether semantic generation is
bypassed, uses available context, or invokes additional evi-
dence/statistics.
Relevance Related / unrelated. Determines whether the context is a plau-
sible intervention rather than incidental calendar text.
Dominant event Event name / none. Resolves overlapping holidays and promo-
tions to a primary driver.
Direction Large decrease, small decrease, flat, small increase, or large
increase; describes the seven-day mean relative to the recent
mean.
Temporal shape Increasing, decreasing, rise–fall, fall–rise, or flat; specifies the
within-horizon trajectory and turning behavior.
Amplitude Positive scalar; ratio of the predicted seven-day mean to the
recent seven-day mean.
Peak Positive scalar; ratio of the largest predicted day to the recent
seven-day mean.
Trend narrative At most 80 Chinese characters; states event timing, turning
point, and coarse magnitude for semantic encoding.
Table 12 shows a representative teacher example. The stored
compressed rationale is Chinese; an English translation is shown
for readability. It is a concise forecasting rationale, not a raw token-
by-token trace of the teacher’s internal generation.
B.3 Teacher Distillation and Rationale
Compression
We construct the initial SFT pool by stratifying 40,000 item–window
examples across upward (40%), downward (22%), flat (33%), and

Preprint, August 2026, Ziyue Yang, Chaolin Xu, Yijing Wang, Tiankai Gu, Hui Yang, Yanhong Lin, Kaiyuan Liu, and Fei Xiao
noisy (5%) demand regimes. Claude Opus 4.6 serves as the teacher
and receives only the Basic semantic interpreter prompt, without
agent routing or tool interaction. This stage deliberately super-
vises structured semantic construction rather than the agent policy.
Of 11,627 successful teacher generations, deterministic filters on
direction, amplitude, and peak consistency retain 7,312 candidates.
The teacher rationales are substantially longer than needed by
the student model. We therefore translate the English rationales
into Chinese and compress them to a single 200–300-character
paragraph while preserving the original decision order: item and
window, event position, recent baseline and 𝐶, historical 𝐴 and
𝐴peak or the no-YoY branch, item–event relevance, dominant-event
selection, direction and shape, magnitude and peak, and any neces-
sary recalibration. Numerical evidence may only be copied from the
prompt or teacher response. The six structured labels are held fixed
during compression. After compression validation, deduplication,
and rebalancing, the final SFT set contains 4,590 examples.
This data transformation shortens the student rationale without
discarding the forecasting decision pattern. As shown in Table 5,
mean rationale length decreases from 568.99 to 206.61 tokens after
SFT and to 202.77 tokens after semantic-field RL, a 64.36% reduc-
tion relative to the original LLM. Direction, amplitude, and peak
errors simultaneously decline. Because Table 5 reports cumulative
post-training stages rather than an isolated compression ablation,
we interpret this as an end-to-end distillation result rather than
attributing the quality gain to compression alone.
B.4 SFT, Semantic-Field RL, and Forecast-Utility
RL Configuration
Tables 13 and 14 record the main optimization settings. Both RL
stages use group-relative policy optimization (GRPO). Semantic-
field RL improves the forecast-critical fields; forecast-utility RL
first applies a semantic validity gate and then evaluates only gate-
passing candidates with the frozen fusion model.
Table 13: SFT and semantic-field RL configuration.
Component Configuration
Student model Qwen3-32B [37] for SFT and both GRPO stages.
SFT data 4,590 compressed teacher examples; 2% validation split.
SFT adapter LoRA on all linear layers, rank 16, scale 32, dropout 0.05.
SFT optimization Three epochs; learning rate1 × 10−4; cosine schedule;
warmup ratio 0.03; BF16; effective batch size 32 (eight
workers, batch size 1, four accumulation steps).
Semantic-field adapter New LoRA initialized on the SFT-merged model; rank 8,
scale 16, dropout 0; all linear layers.
Semantic-field sam-
pling
Group size 8; temperature 0.8; top-𝑝 0.95; top-𝑘 50; maxi-
mum prompt/completion lengths 2816/512 tokens.
Semantic-field opti-
mization
1,500 updates (one pass over the consumed subset); learn-
ing rate5 × 10−6; cosine schedule; warmup ratio 0.03;
KL coefficient 0.02 against the SFT policy.
Semantic-field reward Direction/shape/amplitude/peak weights
0.20/0.20/0.30/0.30. Unparseable outputs receive
−1.5; additional penalties enforce peak–amplitude,
direction–amplitude, and narrative consistency.
Table 14: Forecast-utility RL (GRPO) configuration.
Component Configuration
Forecast-utility data
and sampling
5,500 prompts, one epoch (1,834 updates); group size 8;
the same maximum prompt/completion lengths and roll-
out sampling as semantic-field RL.
Forecast-utility opti-
mization
Learning rate2 × 10−6; cosine schedule; warmup ra-
tio 0.03; global KL coefficient 0.02 against the frozen
semantic-field policy, plus a prompt-conditional SFT KL
coefficient in[0,0.004].
Forecast-utility rout-
ing and gate
Sample skip/basic/tool with each rollout; disallow skip
for holidays and mega-sales. Skip bypasses field parsing
and uses the cached no-text forecast. For non-skip routes,
require field reward𝐴𝑖 ≥max(𝐴 ref 𝑖 − 0.08, 0.10) and
reject hard cross-field contradictions before invoking the
frozen fusion model.
Forecast utility Compare candidate MAE with the cached semantic-field-
policy fusion MAE and the no-text TSFM MAE; penal-
ize harm beyond1.05times the no-text MAE. Utility is
clipped on a 0.25 relative-error scale. Its weight is 0.5 in
the reference run and 1.5 after the fixed step-500 diagnos-
tic; a normalized route-cost penalty makes tool use more
expensive than basic reasoning and assigns zero cost to
skip.
