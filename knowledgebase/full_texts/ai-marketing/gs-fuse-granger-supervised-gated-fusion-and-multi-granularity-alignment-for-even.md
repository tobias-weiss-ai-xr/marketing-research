---
title: 'GS-FUSE: Granger-Supervised Gated Fusion and Multi-Granularity Alignment for Event-Driven Financial
  Forecasting'
url: https://arxiv.org/abs/2605.28520
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Yang Zhang
- En Chun
- Ziyun Mao
- Yulu Wu
- Jun Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.28520
pages: 12
chars: 66735
fetched_at: '2026-11-08T13:06:09+00:00'
kb_version: 1
---

# GS-FUSE: Granger-Supervised Gated Fusion and Multi-Granularity Alignment for Event-Driven Financial Forecasting

{GS-Fuse}: Granger-Supervised Gated Fusion and
Multi-Granularity Alignment for Event-Driven Financial
Forecasting
Yang Zhang∗
zhang.yang.r54@kyoto-u.jp
Southwestern University of Finance
and Economics
Chengdu, China
En Chun
enchun33@gmail.com
Southwestern University of Finance
and Economics
Chengdu, China
Ziyun Mao
224120100004@smail.swufe.edu.cn
Southwestern University of Finance
and Economics
Chengdu, China
Yulu Wu
225120100001@smail.swufe.edu.cn
Southwestern University of Finance
and Economics
Chengdu, China
Jun Wang∗
wangjun1987@swufe.edu.cn
Southwestern University of Finance
and Economics
Chengdu, China
Abstract
Accurately forecasting the impact of salient financial events on mar-
kets is critical for investors and policymakers. However, existing
multimodal time-series models typically fuse text and prices sym-
metrically, without an explicit way to decide when event text is truly
predictive, and thus struggle to exploit the directional event-to-price
structure and the heterogeneous roles of textual and price signals.
In this work, we propose GS-Fuse, a multimodal event-based fore-
casting framework that employs (i) a Granger-supervised, causal-
aware gated fusion module, which learns to open toward event
text only when it provides incremental predictive value beyond
historical prices, and (ii) a multi-granularity alignment mechanism
that jointly aligns high-level event representations and fine-grained
textual cues with future market trajectories. Built as a flexible, plug-
and-play adapter on top of off-the-shelf large language models and
time-series foundation models, GS-Fuse can be instantiated across
diverse backbones and market settings. Extensive experiments on
real-world financial datasets show that GS-Fuse consistently outper-
forms state-of-the-art time-series and multimodal baselines across
multiple assets and forecasting horizons. The implementation is
publicly available in ourGitHub repository.
CCS Concepts
•Applied computing → Economics;•Computing methodolo-
gies→Neural networks.
Keywords
Financial Forecasting; Multimodal Learning; Time-Series Forecast-
ing
∗Corresponding authors.
This work is licensed under a Creative Commons Attribution 4.0 International License.
KDD 2026, Jeju Island, Republic of Korea.
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2259-2/2026/08
https://doi.org/10.1145/3770855.3817927
ACM Reference Format:
Yang Zhang, En Chun, Ziyun Mao, Yulu Wu, and Jun Wang. 2026.{GS-
Fuse}: Granger-Supervised Gated Fusion and Multi-Granularity Alignment
for Event-Driven Financial Forecasting. InProceedings of the 32nd ACM
SIGKDD Conference on Knowledge Discovery and Data Mining V.2 (KDD ’26),
August 09–13, 2026, Jeju Island, Republic of Korea.ACM, New York, NY, USA,
12 pages. https://doi.org/10.1145/3770855.3817927
1 Introduction
Fama’s Efficient Market Hypothesis (EMH) posits that financial
asset prices fully incorporate all available information and adjust
when new information enters the market [15, 16]. Event-based fi-
nancial forecasting is a classic problem in finance, and extensive
empirical work shows that major macroeconomic announcements,
including monetary policy decisions, inflation releases, employ-
ment reports, and GDP revisions, can trigger significant market
movements by reshaping investors’ expectations about growth,
risk, and liquidity [ 6, 9, 39, 41, 53, 58, 65, 66]. In Fig. 1, we high-
light several recent events where such announcements triggered
pronounced S&P 500 moves: the Fed’s first post-pandemic 25-basis-
point rate hike on March 16, 2022 sparked a relief rally (S&P +2.24%,
Nasdaq +3.77%); Chair Powell’s “far greater pain” Jackson Hole
speech on August 26, 2022 instead triggered a sharp risk-off move,
with all three major U.S. indices falling by more than 3%; another
25-basis-point hike on February 1, 2023, accompanied by Powell’s
first acknowledgement that disinflation had begun, lifted the S&P
by 1.05% and the Nasdaq by 2.0%; and a hotter-than-expected Jan-
uary 2024 CPI release led to a broad sell-off, with the S&P losing
1.37%, the Dow 1.35%, and the 10-year Treasury yield jumping to
about 4.31%. Accurately estimating such event-driven market im-
pacts is crucial not only for investors, who need to assess potential
risks and returns, but also for policymakers, who must evaluate the
consequences of their decisions.
With the rise of large language models (LLMs) and large time-
series foundation models, recent forecasting research has advanced
along three closely related directions. First,LLM-based time-series
approachesadapt pre-trained LLMs for prediction either by attach-
ing task-specific predictive heads [ 8, 34, 43, 63] or by carefully
arXiv:2605.28520v1  [cs.AI]  27 May 2026

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Yang Zhanget al.
Figure 1: Illustration of financial event–based forecasting. The S&P500 index exhibits pronounced movements around key
macro and policy events: employment situation reports (unemployment rate 5.4% in July 2021; nonfarm payroll +187,000 in
July 2023), FOMC meetings with +0.25% rate hikes (March 16, 2022 and February 1, 2023), Chair Powell’s “far greater pain”
speech (August 26, 2022), and a CPI release (+0.6 in January 2024).
designing prompts [7, 59]. Second, a line ofTransformer-based time-
series modelsleverages Transformer architectures for time-series
forecasting, such as Informer [65], FEDformer [66], and Autoformer
[9], which are trained from scratch on forecasting tasks. More re-
cently, large time-series foundation models, including MOMENT
[21], Chronos [1], and Kronos [54], extend this paradigm by pre-
training on massive collections of time series to learn generic tem-
poral representations, and have demonstrated strong performance
across diverse datasets and tasks. However, these approaches are in-
herently unimodal, overlooking either textual information or time-
series patterns. This has motivated a third direction:multimodal
forecasting frameworksthat combine event text with time-series
signals for prediction, such as GPT4MTS [25], Time-LLM [26], and
TimeCMA [32]. Nevertheless, existing multimodal methods for
event-driven forecasting still face three key limitations:
Limitation 1: Event-invariant fusion.Current multimodal fore-
casters typically fuse text and time-series representations via shared
MLP layers [64] or attention blocks [25, 32], implicitly assuming
a stable, event-independent balance between modalities that is
reused across all events. However, event-driven markets are highly
heterogeneous and non-stationary: some price movements are cat-
alyzed by the sentiment and surprises in event scripts, while others
are largely governed by pre-existing technical patterns. An event-
invariant fusion scheme cannot adaptively reweight modalities
across events, leading to suboptimal performance in heterogeneous
market regimes.
Limitation 2: Lack of causal-aware fusion.Existing multimodal
methods [39, 41] do not incorporate explicit mechanisms that ex-
ploit thedirectionalinfluence of textual events on subsequent mar-
ket reactions. They typically fuse modalities in a symmetric fashion
and lack a principled, per-event criterion for deciding when event
text is predictively useful beyond historical prices. Without such
causal-aware fusion, these approaches may overuse noisy or unin-
formative text and fail to fully capture the fundamental drivers of
market behavior, thereby limiting forecasting performance.
Limitation 3: Coarse-grained alignment.Existing alignment mech-
anisms are often instance-level, aligning a global event embedding
with a global time-series embedding [39, 41, 64]. In practice, only
specific passages in financial releases are truly market-moving. For
example, in FOMC statements, forward guidance on policy rates
or the inflation outlook typically matters more than boilerplate
language. Purely instance-level alignment can therefore be diluted
by irrelevant or noisy content and fails to localize the fine-grained
textual cues that drive market reactions.
Our contributions.To address these challenges, we proposeGS-
Fuse, a Granger-supervised and causal-aware multimodal frame-
work for event-based financial forecasting. Our main contributions
are:
➣ Granger-supervised, causal-aware gated fusion.We de-
sign an event-adaptive gating module that leverages a Granger-
style utility signal to decide when to trust event text. The gate
is encouraged to open for events where incorporating the
textual narrative yields incremental predictive value beyond
a time-series-only baseline, and to close when the text is
uninformative or harmful, leading to selective, utility-aware
fusion.
➣ Multi-granularity cross-modal alignment.We introduce
a joint alignment scheme that operates both at the instance
level (aligning global event and time-series embeddings) and
at a finer granularity (linking salient textual cues to specific
temporal patterns), enabling the model to localize which
parts of the text account for observed market reactions.
➣ Plug-and-play multimodal framework.We provide a
model-agnostic adapter that can wrap arbitrary LLMs and
time-series foundation models. GS-Fuse requires only light-
weight projection, fusion, and decoding modules, making it

{GS-Fuse}: Granger-Gated Multimodal Fusion for Event-Driven Financial Forecasting KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
easy to instantiate on different backbones and market set-
tings.
We evaluate GS-Fuse on a curated event dataset that integrates
macroeconomic releases from CAMEF [64] and salient financial-
event news from FNSPID [13], and perform event-based forecasting
for major equity indices and Treasury yields. Experiments show that
GS-Fuse consistently outperforms strong unimodal and multimodal
baselines, and ablations confirm the benefit of Granger-supervised,
causal-aware fusion and multi-granularity alignment.
2 Related Work
2.1 Event-Driven Financial Forecasting
Event-driven financial forecasting [3] studies how event signals
such as macroeconomic releases, news, corporate announcements,
and social media [19, 33, 60, 68] affect asset prices and volatility
[20, 37]. Existing work falls into three directions. (1)Text-driven
methodsmodel event semantics to predict market reactions, evolv-
ing from TF–IDF/topic models [ 30, 40, 44, 55] to RNNs and pre-
trained transformers [23, 33, 53, 68]. (2)Time-series-driven meth-
odsfocus on numerical modeling, from ARIMA/GARCH [ 2, 4, 24]
to deep RNN/CNN architectures and Transformer-based forecasters
such as Informer and FEDformer [14, 33, 52, 65, 66]. Recently, time-
series foundation models such as MOMENT, Timer, and TOKEN
[21, 35, 57] learn general, transferable temporal representations.
(3)Multi-modal methodscombine heterogeneous signals. Early
work fused text and audio [45, 61], and later studies integrated text
and time series via SVM/GRU-style architectures [ 50, 51]. These
approaches often rely on relatively shallow temporal/semantic mod-
eling, motivating recent transformer-based designs [25, 29]. Our
work follows this direction but leverages pre-trained encoders and
a causally supervised fusion gate to better capture event impacts
on market trends.
2.2 Multi-Modal Alignment and Fusion
In multimodal learning,alignmentmaps modalities into a shared
space, whilefusionintegrates them for prediction [ 31]. Vision–
language models move from instance-level contrastive alignment
in CLIP [46] to token/patch-level matching in FILIP [ 62, 67]. By
contrast, text–time-series models [ 29, 32, 64] largely operate at
instance level and miss links between salient phrases and local
temporal patterns. Our model jointly performs instance-level and
token/step-level alignment to better ground event semantics in
market trajectories. Gated fusion [ 42] weights modality-specific
representations, and later work proposes more structured gates
[5, 17, 69]. In event-driven financial forecasting, however, event
text is anexogenousdriver of post-event prices, so gates trained only
from end-task loss may track spurious correlations or the dominant
modality. We instead introduce a Granger-supervised gate that ties
fusion weights to the text modality’sincrementalpredictive gain.
2.3 Deep Causality Learning
Granger causality (GC) is a foundational framework for temporal
causal analysis [12, 22], stating that a source variable is causal to
a target if adding its history improves the target’s predictability.
Neural GC methods extend this idea with nonlinear predictors and
sparsity-based graph inference [28], and GC-inspired techniques
have been applied to anomaly localization, spatiotemporal impu-
tation, and learning under missing observations [10, 27, 36]. Most
prior work (i) operates in a single-modality setting and (ii) focuses
on discovering causal graphs rather than exploiting causality for
forecasting. In contrast, we propose a cross-modal Granger module
that uses the causal modality’s incremental predictive ability to
supervise fusion and enhance event-driven forecasts.
3 Preliminaries and Problem Formulation
We formalize event-driven financial forecasting, where a discrete
macroeconomic release interacts with pre-event market dynamics
to shape post-event price movements.
3.1 Notation
LetD={(𝐸 𝑖,𝑋𝑖,𝑌𝑖)}𝑁 𝑖=1 be a dataset of 𝑁 aligned multimodal
instances:
• Event.𝐸𝑖 =(𝑆 𝑖,𝜏𝑖,𝑐𝑖), where 𝑆𝑖 =(𝑤 𝑖,1,...,𝑤 𝑖,𝑚𝑖) is the
event script,𝜏𝑖 is its release time, and𝑐𝑖 is the event category.
• Pre-event market context.A multivariate look-back win-
dow
𝑋𝑖 =(𝑥 𝜏𝑖−𝐿+1,...,𝑥 𝜏𝑖), 𝑥 𝑡∈R 𝑑𝑥,(1)
where𝐿 is the length of the pre-event window (number of
historical time steps) and𝑥𝑡 aggregates basic price/volume
and technical features.
•Post-event target.A future horizon segment
𝑌𝑖 =(𝑦 𝜏𝑖+1,...,𝑦 𝜏𝑖+𝐻), 𝑦 𝑡∈R 𝑑𝑦,(2)
which represents the market response over the forecasting
horizon𝐻.
Definition 3.1(Event-driven causal response).Let 𝐸 denote an
event script,𝑋 the pre-event market segment, and𝑌 the post-event
segment. We treat the release as an exogenous information shock
and posit the directed dependence
(𝐸,𝑋)→𝑌,(3)
so that𝑌 is jointly driven by salient information in𝐸 and endoge-
nous dynamics encoded in𝑋.
Definition 3.2(Event-driven forecasting task).Given (𝐸𝑖,𝑋𝑖) ob-
served up to𝜏𝑖, the goal is to learn a mapping
𝑓𝜃 :(𝐸 𝑖,𝑋𝑖)↦→ ˆ𝑌𝑖 (4)
that approximates𝑌𝑖 over horizon𝐻. Unlike standard time-series
forecasting, which extrapolates from𝑋𝑖 alone, event-driven fore-
casting must model the exogenous impact of𝐸𝑖 together with the
endogenous dynamics in𝑋𝑖.
4 Granger-Supervised Causal Gating
GS-Fuse supervises the fusion gate using a Granger-style criterion:
the gate should open only when the event text provides incremental
predictive value beyond a time-series-only baseline.

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Yang Zhanget al.
Figure 2: The Neural Architecture of GS-Fuse.
4.1 Granger Causality Theory
Granger causality formalizes the idea that a time series𝑋 Granger-
causes a target𝑌 if past values of𝑋 improve forecasts of𝑌 beyond
what can be achieved from the past of𝑌alone [22]. Let
ˆ𝑌 res 𝑡+1 =𝑓 res(𝑌1:𝑡),(5)
ˆ𝑌 unres 𝑡+1 =𝑓 unres(𝑌1:𝑡,𝑋 1:𝑡),(6)
denote arestrictedpredictor and anunrestrictedpredictor, respec-
tively. Given a loss functionℓ(·,·),𝑋Granger-causes𝑌if
E

ℓ(𝑌𝑡+1, ˆ𝑌 unres 𝑡+1 )  <E  ℓ(𝑌𝑡+1, ˆ𝑌 res 𝑡+1)  .(7)
In classical econometrics, this condition is evaluated via post-hoc
statistical tests. In GS-Fuse, we reinterpret this principle as aGranger-
supervision utilitythat provides a local, instance-wise signal to
regularize multimodal fusion.
4.2 Granger-Supervised Gating
Building on the classical framework, we extend the restricted-
versus-unrestricted comparison to a multimodal setting. For each
instance𝑖, we compare arestrictedpredictor that only observes the
time-series modality𝑋𝑖 and anunrestrictedpredictor that addition-
ally observes the event text𝐸𝑖:
ˆ𝑌 ts 𝑖 =𝑔 ts 𝜃(𝑋𝑖),(8)
ˆ𝑌 full 𝑖 =𝑔 full 𝜃 (𝑋𝑖,𝐸𝑖).(9)
We define theGranger utilityof the text for instance 𝑖 as the loss
differential:
Δ𝑖 :=ℓ(𝑌 𝑖, ˆ𝑌 ts 𝑖 )−ℓ(𝑌 𝑖, ˆ𝑌 full 𝑖 ),(10)
whereℓ(·,·) is the forecasting loss (e.g., MSE) and 𝑌𝑖 is the post-
event target segment defined in § 3.
Posterior Responsibility.To convert this utility into a supervision
objective, we treat the predictors as competing experts and map
their losses to soft responsibilities. Specifically, we pass the per-
expert losses through a Gibbs-style transform
𝑝(𝑌𝑖|𝑔𝑘)∝exp(−ℓ 𝑘 𝑖/𝜏gc), 𝑘∈{ts,full},
withℓ𝑘 𝑖 =ℓ(𝑌 𝑖, ˆ𝑌𝑘 𝑖) and normalize them with a two-way softmax to
obtain
𝑟𝑖 = 𝑝(𝑌𝑖|𝑔 full) 𝑝(𝑌𝑖|𝑔 full)+𝑝(𝑌 𝑖|𝑔 ts) =𝜎  Δ𝑖 𝜏gc  ,(11)
where𝜎(·) is the logistic sigmoid and𝜏gc is a temperature hyperpa-
rameter. Here,𝑟𝑖∈[ 0, 1] serves as a soft “text usefulness” target:
events where text yields significant predictive gains result in𝑟𝑖≈ 1,
while instances where text is redundant or noisy result in𝑟𝑖≈ 0.
This construction can be interpreted as a Bayesian posterior over
the two experts under a Gibbs-style likelihood and a uniform prior.
Gate Supervision.We introduce a gating function𝛼𝑖 =Gate(𝑋 𝑖,𝐸𝑖)∈
[0, 1] that predicts this usefulness score directly from the inputs.
The gate is trained to match𝑟𝑖 via a distillation loss:
Lgate = 1 𝑁 𝑁∑︁ 𝑖=1 (𝛼𝑖−𝑟𝑖)2.(12)
MinimizingLgate encourages the gate to open (large𝛼𝑖) exactly on
instances where the multimodal predictor exhibits positive Granger
utility, allowing the fusion module to lean on the text branch. At
inference time,𝛼𝑖 is computed solely from(𝑋𝑖,𝐸𝑖); the Granger-
based losses andΔ𝑖 are used only during training.
5 Model Architecture
Building on the problem formulation in § 3 and the Granger-supervised
gating mechanism in § 4, we now present the architecture of GS-
Fuse. The model consists of four components: (i) a textual en-
coder for the event script 𝐸𝑖, (ii) a time-series encoder for the
pre-event segment 𝑋𝑖, (iii) a Granger-gated fusion module with
multi-granularity alignment, and (iv) a decoder that generates the
future segment𝑌𝑖. All the hyperparameter values in this section
are explained in Appendix B and Table 5.
5.1 Event and Time-Series Encoders
Encoding event scripts via an LLM.For each event 𝐸𝑖 =(𝑆 𝑖,𝜏𝑖,𝑐𝑖)
with token sequence𝑆𝑖 =(𝑤 𝑖,1,...,𝑤 𝑖,𝑚𝑖), we obtain token-wise
text representations. A pretrained LLM 𝑓 LLM followed by a pro-
jection head𝜙text maps tokens into a shared space of dimension

{GS-Fuse}: Granger-Gated Multimodal Fusion for Event-Driven Financial Forecasting KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
𝐹=1024:
H𝐸 𝑖 = h𝐸 𝑖,1,...,h 𝐸 𝑖,𝑚𝑖  =𝜙 text  𝑓 LLM(𝑆𝑖)  ∈R 𝑚𝑖×𝐹.(13)
Encoding time series via a TS foundation model.Given the pre-
event segment𝑋𝑖 =(𝑥 𝜏𝑖−𝐿+1,...,𝑥 𝜏𝑖), we extract step-wise repre-
sentations. A pretrained time-series foundation encoder𝑓 TS (e.g.,
MOMENT, Chronos) followed by a projection head𝜙ts maps the
segment into the embedding space𝐹=1024:
H𝑋 𝑖 = h𝑋 𝑖,1,...,h 𝑋 𝑖,𝐿  =𝜙 ts  𝑓 TS(𝑋𝑖)  ∈R 𝐿×𝐹.(14)
We initialize𝑓 LLM and𝑓 TS from public foundation models and
keep them frozen. Concretely, for the textual modality 𝑓 LLM is
instantiated from open-source LLM backbones (LLaMA-family and
Phi-3, 3B) selected from the top ranked HuggingFace leaderboard
1, while for the time-series modality𝑓 TS is instantiated from large
time-series foundation models (MOMENT [21] and Kronos [54]),
where MOMENT is among the first generic TS foundation models
and Kronos is further tuned on stock-market data. The projection
heads(𝜙text,𝜙 ts) and all downstream fusion/decoder modules in
GS-Fuse are trained, while the backbone LLM and TS foundation
models remain frozen across all experiments.
5.2 Multi-Granularity Cross-Modal Alignment
To reduce the modality gap and stabilize the joint representation
space, we enforce pre-fusion alignment at both instance and token
granularities.
5.2.1 Instance-Level Global Alignment.Given token/step represen-
tationsH𝐸 𝑖 ∈R 𝑚𝑖×𝐹 andH𝑋 𝑖 ∈R 𝐿×𝐹 , we first interleave information
with bi-directional cross-attention:
˜H𝐸 𝑖 =CA𝑋→𝐸

Q=H 𝐸 𝑖,K=H 𝑋 𝑖 ,V=H 𝑋 𝑖

,(15)
˜H𝑋 𝑖 =CA𝐸→𝑋

Q=H 𝑋 𝑖 ,K=H 𝐸 𝑖,V=H 𝐸 𝑖

,(16)
where CA(·) is standard multi-head cross-attention. We then pool
to obtain instance-level embeddings
t𝑖 =Pool( ˜H𝐸 𝑖),s 𝑖 =Pool( ˜H𝑋 𝑖)∈R 𝐹,
and apply an InfoNCE loss over in-batch negatives:
Lctr =− 1 𝑁 𝑁∑︁ 𝑖=1 log exp(⟨ ˆs𝑖, ˆt𝑖⟩/𝜏ctr) ˝𝑁neg 𝑘=0 exp(⟨ ˆs𝑖, ˆt(𝑘) 𝑖 ⟩/𝜏ctr) ,(17)
where ˆs𝑖 = s𝑖/∥s𝑖∥2 and ˆt(𝑘) 𝑖 = t(𝑘) 𝑖 /∥t(𝑘) 𝑖 ∥2 denoteℓ2-normalized
embeddings,t(0) 𝑖 = t𝑖 is the positive pair,{t(𝑘) 𝑖 } 𝑁neg 𝑘=1 are in-batch
negatives, and𝜏 ctr is the contrastive temperature.
5.2.2 Token/Step Fine-Grained Alignment.To capture local corre-
spondences between salient phrases and specific temporal patterns,
we further align individual text tokens with time-series steps.
Alignment space and soft positives.LetH 𝐸 𝑖 ∈R 𝑚𝑖×𝐹 andH 𝑋 𝑖 ∈
R𝐿×𝐹 be encoder hidden states. We map them into a shared align-
ment space:
Z𝐸 𝑖 =Norm(𝜑 𝐸(H𝐸 𝑖)),Z 𝑋 𝑖 =Norm(𝜑 𝑋(H𝑋 𝑖))∈R 𝐿×𝐹,
1Huggingface LLM Leaderboard: https://huggingface.co/open-llm-leaderboard
where𝜑𝐸,𝜑𝑋 are learnable projections andNorm denotes row-wise
ℓ2-normalization, so thatZ𝐸 𝑖,𝑗 andZ𝑋 𝑖,ℓ are unit-norm token and step
embeddings, respectively. We form a token–step similarity matrix
S𝑖 =Z𝐸 𝑖(Z𝑋 𝑖)⊤/𝜏al∈R 𝑚𝑖×𝐿,(18)
with alignment temperature𝜏al. An attention distribution from each
token to time steps is
P𝐸→𝑋 𝑖 =softmaxℓ(S𝑖)∈R 𝑚𝑖×𝐿,(19)
where softmaxℓ is applied row-wise over the time-step dimension
ℓ. The correspondingsoft-positivetime-series vector for token𝑗is
z𝑋,+ 𝑖,𝑗 =
𝐿∑︁
ℓ=1
P𝐸→𝑋 𝑖 (𝑗,ℓ)Z 𝑋 𝑖,ℓ.(20)
Salient anchors and contrastive loss.We score token salience with
a linear scorer:
𝑎𝑖,𝑗 =softmax 𝑗

w⊤h𝐸 𝑖,𝑗

,(21)
whereh 𝐸 𝑖,𝑗 is the original text hidden state,wis learnable, and
softmax𝑗 is taken over tokens 𝑗= 1,...,𝑚 𝑖. The Top-𝐾top tokens
under𝑎𝑖,𝑗 form an anchor setA𝑖. For each anchor token 𝑗∈A 𝑖,
we encourage its text embeddingZ 𝐸 𝑖,𝑗 to matchz𝑋,+ 𝑖,𝑗 and repel time-
series steps from other instances via a salience-weighted InfoNCE
loss with cross-sample negatives:
Ltok = 1 𝑁 𝑁∑︁ 𝑖=1 ∑︁ 𝑗∈A𝑖 𝑎𝑖,𝑗  −log exp(⟨Z𝐸 𝑖,𝑗,z𝑋,+ 𝑖,𝑗 ⟩/𝜏nce) exp(⟨Z𝐸 𝑖,𝑗,z𝑋,+ 𝑖,𝑗 ⟩/𝜏nce)+ ˝ 𝑖′≠𝑖,ℓ exp(⟨Z𝐸 𝑖,𝑗,Z𝑋 𝑖′,ℓ⟩/𝜏nce)  ,
(22)
where𝜏nce is the NCE temperature and the sum over(𝑖′,ℓ) ranges
over all time-series steps ℓ in other instances 𝑖′ ≠𝑖 . The overall
alignment loss is
Lalign =L ctr+L tok,(23)
withLctr aligning instance-level representations andLtok enforcing
fine-grained token–step correspondences.
5.3 Granger-Gated Fusion
We implement the Granger-supervised fusion principle from § 4:
the gate should open only when the event text provides incremental
predictive utility beyond a TS-only baseline. Concretely, we produce
a restricted (TS-only) forecast and an unrestricted (text-augmented)
forecast using thesamedecoder, and convert their loss gap into a
stop-gradient supervision signal for the fusion gate.
Gating and fusion.Given instance embeddingst 𝑖 (event) ands𝑖
(time series) from §5.2, the gating network takes their concatenation
v𝑖 =[t 𝑖 ;s𝑖]∈R 2𝐹,(24)
(a𝐸 𝑖,a𝑋 𝑖)=𝜓 gate(v𝑖),a 𝐸 𝑖,a𝑋 𝑖 ∈R 𝐹,(25)
where𝜓gate is a small MLP. It produces feature-wise modality
weights via a two-way softmax:
𝛼𝐸 𝑖,𝑓 = exp(𝑎𝐸 𝑖,𝑓/𝜏gate) exp(𝑎𝐸 𝑖,𝑓/𝜏gate)+exp(𝑎 𝑋 𝑖,𝑓/𝜏gate), 𝛼 𝑋 𝑖,𝑓 =1−𝛼 𝐸 𝑖,𝑓,(26)
for𝑓= 1,...,𝐹 , with temperature𝜏gate. Let 𝜶𝐸 𝑖,𝜶 𝑋 𝑖 ∈( 0, 1)𝐹 and
𝜶𝐸 𝑖 +𝜶 𝑋 𝑖 =1. The fused context is
z𝑖 =𝜶 𝐸 𝑖 ⊙t𝑖+𝜶 𝑋 𝑖 ⊙s𝑖∈R 𝐹,(27)

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Yang Zhanget al.
Table 1: Statistics of Dataset
A. Statistics of Event Script (Textual Data)
Event Type # Event Days # Articles Avg. Length (words) Coverage
FOMC decisions 1482 16,302 444 2002–2024
Employment situation 1494 16,434 682 2002–2024
Unemployment insurance 2505 27,729 647 2002–2024
CPI releases 1905 20,955 1,058 2002–2024
PPI releases 2007 22,357 792 2002–2024
GDP announcements 2874 31,616 778 2002–2024
B. Statistics of Financial Assets (Time-Series Data)
Time Series Data Type # Data Points Range Frequency
S&P500 index Equity index 331,256 2008–2024 5-min
Dow Jones Equity index 187,241 2012–2022 5-min
NASDAQ Equity index 332,615 2009–2024 5-min
US 1M Treasury (USGG1M) Treasury yield 689,304 2013–2024 5-min
US 5Y Treasury (USGG5YR) Treasury yield 711,140 2012–2024 5-min
where⊙ denotes element-wise multiplication. For gate supervision
we use a scalar openness summary
𝛼𝑖 = 1 𝐹 𝐹∑︁ 𝑓=1 𝛼𝐸 𝑖,𝑓 ∈(0,1),(28)
i.e., the average responsibility assigned to the event modality.
Granger utility (restricted vs. unrestricted).To realize 𝑔ts 𝜃 and𝑔full 𝜃
in §4 with a fair comparison, we reuse the same decoder 𝑓dec (cf.
§5.4) and compute
ˆ𝑌 full 𝑖 =𝑓 dec(z𝑖), ˆ𝑌 ts 𝑖 =𝑓 dec(s𝑖).(29)
We define per-instance losses (MSE over horizons and target di-
mensions)
ℓ full 𝑖 =MSE( ˆ𝑌 full 𝑖 ,𝑌𝑖), ℓ ts 𝑖 =MSE( ˆ𝑌 ts 𝑖 ,𝑌𝑖),(30)
and obtain the Granger-supervision incremental utility
Δ𝑖 =ℓ ts 𝑖 −ℓ full 𝑖 ,(31)
where Δ𝑖 > 0indicates that incorporating text reduces the forecast-
ing loss beyond the TS-only baseline.
Responsibility target and gate supervision.We map the utility gap
Δ𝑖 to a soft responsibility target via a sigmoid:
𝑟𝑖 =𝜎 clip(Δ𝑖/𝜏gc,−𝑐,𝑐) ,(32)
where𝜎(·) is the logistic sigmoid,𝜏gc > 0is a temperature hyper-
parameter, and𝑐> 0is a clipping threshold to avoid saturated
gradients. Here,𝑟𝑖∈[ 0, 1] serves as a soft “text usefulness” target:
events where text yields significant predictive gains result in𝑟𝑖≈ 1,
while instances where text is redundant or noisy result in𝑟𝑖≈ 0.
We then supervise the gate by
Lgate = 1 𝑁 𝑁∑︁ 𝑖=1 (𝛼𝑖−𝑟𝑖)2,(33)
encouraging the gate to open when text provides reliable utility
and to close otherwise. Finally, the training objective combines the
forecasting loss with gate supervision:
L= 1 𝑁 𝑁∑︁ 𝑖=1 ℓ full 𝑖 +𝜆 gateLgate,(34)
where𝑁 is the batch size and 𝜆gate > 0controls the strength of
gate supervision.
5.4 Time-Series Decoder
Given the fused representationz 𝑖 ∈R 𝐹 , we decode the future
segment𝑌𝑖 =(𝑦 𝜏𝑖+1,...,𝑦 𝜏𝑖+𝐻) using a lightweight Transformer
decoder with𝐿 dec=3blocks and𝑛 head=16attention heads.
Decoder input.We first expandz 𝑖 into a length-𝐻 sequence by
projecting it to the decoder dimension and adding horizon posi-
tional encodings:
D𝑖[ℎ]=𝑊 inz𝑖+PE(ℎ), ℎ=1,...,𝐻,(35)
yieldingD𝑖∈R 𝐻×𝑑 dec.
Transformer decoding.A stack of 𝐿dec standard Transformer de-
coder blocks is applied toD𝑖:
H𝑖 =𝑓 dec(D𝑖)∈R 𝐻×𝑑 dec,(36)
where𝑓dec denotes the Transformer decoder (composition of𝐿dec
blocks).
Regression head.A small feed-forward head maps each horizon
state to the target dimension𝑑 𝑦. For each stepℎ,
ˆ𝑦𝜏𝑖+ℎ =𝑊 out MLPreg(H𝑖[ℎ])+b out,(37)
where MLPreg is a𝐾reg-layer MLP with GELU activations. Collecting
overℎyields the forecast
ˆ𝑌𝑖 =( ˆ𝑦𝜏𝑖+1,..., ˆ𝑦𝜏𝑖+𝐻)∈R 𝐻×𝑑𝑦.(38)
5.5 Three-Stage Training Scheme and Objectives
We trainGS-Fusein three stages for stable optimization.
Stage 1: TS-only pre-training.We first train the time-series branch
in a sliding-window setting: given segments of length𝐿, the model
predicts the next𝐻 steps. Text inputs and fusion modules are omit-
ted; only TS-side projections and the decoder are updated. The
forecasting loss is
Lforecast = 1 𝑁 𝑁∑︁ 𝑖=1 MSE( ˆ𝑌𝑖,𝑌𝑖)+ 1 𝑁 𝑁∑︁ 𝑖=1 MAE( ˆ𝑌𝑖,𝑌𝑖),(39)
where ˆ𝑌𝑖 is the decoded multi-horizon prediction for instance𝑖 and
𝑌𝑖 is the ground-truth trajectory.
Stage 2: Text-only warm-up.We then warm up the textual branch
on the event-aligned dataset, using the same Lforecast. The time-
series branch and fusion modules are bypassed; we update only
text-side projections and the decoder so that event representations
become directly forecasting-relevant.

{GS-Fuse}: Granger-Gated Multimodal Fusion for Event-Driven Financial Forecasting KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
Table 2: Event-Driven Forecasting Performance. We report MSE (×10−4), MAE (×10−3), DHR (×10−2), and Sharpe on real-world
financial datasets (S&P500, NASDAQ, INDU, USGG1M, USGG5YR) across varying prediction horizons. GS-Fuse (Ours) and
applied Time-Series Foundation Models Moment/Kronos are highlighted. Best results are in bold.
Model Horizon S&P500 NASDAQ INDU USGG1M USGG5YR
MSE MAE DHR Sharpe MSE MAE DHR Sharpe MSE MAE DHR Sharpe MSE MAE DHR Sharpe MSE MAE DHR Sharpe
L=35 52.95 52.98 52.58 0.61 107.05 77.94 49.16 0.08 363.6 124.6 46.19 -0.91 15.85 16.99 40.00 -0.92 10.92 19.80 46.47 -0.73
L=70 62.35 57.65 -0.36 1.26 128.10 85.28 48.08 0.18 427.4 133.8 45.82 -0.48 18.12 31.97 37.66 -1.99 23.79 31.32 47.53 -0.25ARIMA
L=140 101.25 60.12 50.36 -0.19 200.89 106.43 52.15 0.23 684.1 166.7 44.84 -0.65 22.48 64.01 39.02 -0.99 61.98 52.14 49.47 -0.11
L=35 81.36 68.78 45.27 -1.18 110.68 79.69 53.46 0.71 357.2 127.655.95 2.61 21.00 20.2152.98 2.38 13.57 25.01 46.47 -0.98
L=70 100.29 77.4554.011.13 186.35 105.96 54.84 0.90 539.6 162.8 55.37 0.59 26.97 42.2870.85 4.35 39.51 45.45 48.23 -0.50Dlinear
L=140 223.97 118.85 44.48 -0.51 250.49 123.09 53.85 0.44 566.0 235.7 43.41 0.12 28.31 76.03 60.34 2.41 102.17 76.52 53.72 0.69
L=35 55.95 55.18 50.86 1.08 110.20 79.29 53.61 0.12 333.4 125.0 50.24 1.35 17.50 21.30 40.85 -1.01 66.92 66.80 47.00 -1.28
L=70 73.57 63.40 50.43 1.13 145.67 92.23 54.69 1.42 417.1 135.8 49.64 0.49 24.19 42.44 59.57 0.83 28.50 35.54 51.41 0.37Autoformer
L=140 115.67 78.18 51.94 0.14 255.20 121.84 51.08 0.49 759.4 180.3 46.28 0.21 26.90 85.15 62.05 1.46 72.78 59.80 48.05 -0.23
L=35 52.98 53.12 49.00 -0.56 106.43 77.64 54.22 0.75 362.7 124.9 52.38 0.16 15.81 16.80 50.21 1.36 10.97 20.05 50.18 0.68
L=70 63.53 58.17 51.43 -0.15 128.09 84.83 55.15 1.00 427.2 133.7 49.40 -0.62 18.10 31.63 62.13 2.08 23.75 31.42 50.18 1.01iTransformer
L=140 103.30 73.82 49.64 -0.06 207.48 108.06 50.46 -0.19 695.6 167.8 49.64 -0.01 22.83 60.02 59.91 1.09 62.49 52.53 53.01 0.53
L=35 52.82 53.0154.290.81 107.42 78.00 50.38 0.61 107.4 78.00 51.58 0.84 16.59 19.57 40.00 -2.30 10.72 19.99 46.29 -0.65
L=70 65.40 60.17 53.46 0.68 140.15 89.68 49.92 0.80 135.6 88.20 49.43 0.57 25.87 43.19 49.79 0.09 28.86 37.70 48.94 0.76FEDformer
L=140 115.96 78.48 49.16 0.42 233.03 115.41 51.38 0.78 681.7 168.2 52.370.95 23.50 82.98 65.19 2.16 73.27 59.58 50.71 0.20
L=35 34.40 33.05 50.57 1.16 42.62 43.78 51.311.69 108.8 55.20 51.67 0.88 9.36 19.28 49.14 1.02 20.36 27.23 51.06 1.04
L=70 47.92 48.30 51.72 1.24 83.96 64.22 48.08 0.80 175.6 161.6 53.46 1.61 14.54 34.49 56.81 1.15 37.10 39.49 52.47 0.76TimesFM
L=140 95.16 69.45 53.08 0.75 177.22 98.01 51.08 0.74 346.8 313.7 47.00 -0.23 21.27 49.34 68.87 1.87 77.14 60.82 46.00 -0.92
L=35 21.19 30.43 53.70 0.34 38.73 42.10 52.79 0.62 118.4 61.80 50.14 -0.19 8.97 15.31 47.28 1.05 17.84 26.50 48.68 0.16
L=70 42.75 44.39 53.59 1.00 77.44 60.96 51.47 0.56 227.7 88.90 50.37 -0.42 13.73 27.35 57.06 2.07 34.62 37.84 49.34 -0.30Chronos
L=140 77.74 62.22 53.91 0.46 151.34 88.60 52.63 0.31 451.7 127.9 52.43 -0.29 21.55 44.30 69.21 1.56 66.00 54.73 50.15 -0.61
L=35 22.19 30.86 49.98 -0.00 41.14 42.98 49.68 -0.08 135.3 66.20 50.07 -0.17 9.28 16.03 47.88 1.68 18.61 27.07 49.49 0.46
L=70 43.86 45.23 49.72 0.02 81.34 63.06 50.00 0.05 268.6 97.40 50.13 -0.25 13.80 27.37 53.71 2.14 36.53 39.17 49.48 0.25Moment
L=140 85.06 64.77 52.37 0.44 159.01 90.41 50.36 0.14 538.6 140.2 51.17 -0.09 19.93 44.01 66.12 2.58 70.52 56.57 48.93 -0.04
L=35 10.17 24.08 49.55 0.12 51.49 67.55 50.59 0.55 176.1 97.00 49.54 -0.19 36.94 22.19 28.55 0.49 25.05 29.31 49.15 0.22
L=70 15.80 36.88 48.43 -0.07 80.97 66.89 50.37 -0.11 321.2 124.6 50.04 -0.47 39.65 27.07 41.31 0.96 31.37 37.73 49.21 0.27Kronos
L=140 85.39 90.82 51.69 0.26 178.01 104.73 51.21 0.02 666.2 466.1 50.38 0.43 53.57 61.05 37.74 -1.57 79.77 87.48 50.12 0.28
L=35 64.41 60.31 46.50 -1.42 75.83 66.45 48.18 -0.86 526.9 158.2 50.52 1.82 81.65 65.46 28.69 1.32 163.45 85.12 48.24 0.50
L=70 72.16 59.09 51.14 0.69 62.80 55.61 49.51 0.55 141.1 94.40 49.48 0.26 107.04 61.94 41.88 0.47 112.89 73.99 50.37 0.27GPT4MTS
L=140 87.86 72.62 51.23 0.08 47.81 50.96 51.77 -0.17 185.9 102.6 49.68 0.81 126.11 68.82 52.67 1.95 100.71 73.03 49.23 0.18
L=35 13.65 17.01 46.30 -0.61 12.54 15.07 43.82 0.20 33.6 46.60 52.59 2.28 36.49 37.01 19.80 -1.81 34.43 37.94 51.26 1.14
L=70 10.69 24.71 50.491.36 13.47 27.16 44.53 -0.07 34.5 42.70 51.85 0.92 39.80 36.33 43.56 4.04 32.47 43.67 48.24 0.26TEST
L=140 9.93 22.32 45.57 -0.47 10.07 22.93 42.20 -0.17 39.2 42.10 48.89 -0.15 39.97 26.60 56.44 3.06 26.19 37.2256.28 2.95
L=35 32.43 39.60 49.47 0.16 59.96 55.21 48.64 0.27 187.6 82.00 50.00 -0.59 9.16 21.31 49.48 2.27 27.37 34.40 49.44 0.50
L=70 65.14 58.74 48.52 -0.06 78.80 62.60 49.90 0.11 394.6 124.6 50.90 -0.20 13.80 30.71 52.84 1.55 37.28 40.22 49.16 0.18TimeCMA
L=140 130.52 84.43 48.76 -0.00 155.42 89.60 50.60 0.25 536.4 141.8 50.68 0.03 19.71 46.95 67.90 2.35 108.16 75.68 48.84 -0.17
L=35 3.38 11.44 53.16 1.92 3.08 9.90 55.79 1.08 8.2 18.30 54.55 1.13 2.85 4.73 33.94 1.17 6.79 16.08 55.18 3.29
L=70 3.98 12.48 53.84 1.25 3.66 10.80 59.82 1.78 10.1 20.00 59.23 1.84 3.13 5.24 68.11 2.77 8.94 19.19 58.23 2.88GS-Fuse (LLaMa + MOMENT) L=140 6.60 15.67 56.03 0.79 6.86 15.49 58.78 0.87 18.2 25.00 61.40 0.86 3.84 6.89 73.96 3.27 12.45 23.17 54.19 1.44
Table 3: Backbone interaction on long-horizon forecasting
(𝐿=140). Metrics: MSE (×10−4) and MAE (×10−3). Δ denotes the
relative change when swapping the LLaMA text backbone
for Phi;↓improves and↑degrades.
Foundation
MSE (10−4) MAE (10 −3)
LLaMA Phi Gap (Δ) LLaMA Phi Gap (Δ)
(a) Dataset: INDU
Moment 18.220.3↑11.5%25.026.6↑6.4%
Kronos25.925.4↓1.9% 29.028.2↓2.8%
(b) Dataset: USGG1M
Moment 3.844.06↑5.7%6.897.33↑6.4%
Kronos4.093.97↓2.9% 8.097.38↓8.8%
Stage 3: Multimodal fine-tuning.Finally, we enable the fullGS-
Fusemodel and jointly train with both modalities. The LLM and
TS foundation encoders are frozen, while the fusion stack (cross-
modal alignment and Granger-gated fusion) and prediction heads
are trained with the combined objective
Ltotal =L forecast+𝜆 alignLalign+𝜆 gateLgate,(40)
whereLalign andLgate are defined in § 5.2 and § 4, and𝜆align,𝜆 gate
are scalar weights.
6 Experiments
We evaluateGS-Fuseon event-driven market forecasting and ad-
dress four research questions:RQ1 (Accuracy).How well does
GS-Fuseforecast markets across datasets and horizons?RQ2 (Gen-
erality).How robust isGS-Fusewith different LLM text and time-
series foundation backbones?RQ3 (Ablation).Which components
contribute most to performance?RQ4 (Causal Gating).Does the
Granger gate increase reliance on text when it helps and down-
weight it otherwise? We also provide case studies on aligned tokens
from token-wise alignment module in Appendix D.
6.1 Experimental Setting
6.1.1 Dataset and Curation.
Event Script Set.We start from the six categories of salient macroe-
conomic events curated in theCAMEFdataset [64], monetary policy
decisions, employment reports (employment situation and unem-
ployment insurance), inflation releases (CPI and PPI), and GDP
announcements.2 To enrich each category, we retrieve additional
financial news fromFNSPID 3 using Sentence-BERT embeddings: an
article is retained if its cosine similarity to an event-type prototype
(mean-pooledCAMEFarticles of that type) exceeds 0.55, with edge
cases manually checked.
Financial Time-Series Data.We directly use the high-frequency
market data fromCAMEF, which provides 5-minute trading series
for three major U.S. equity indices (S&P500, Dow Jones Industrial
Average, NASDAQ) and two U.S. Treasury bonds (1-month and
5-year). These assets are well documented as sensitive to macroe-
conomic announcements.
The train, validation, and test sets are split in a 6 / 2 / 2 ratio
over time: the early events and time series are used for training and
validation, and the latest data are reserved for testing.
2CAMEF Dataset: https://github.com/lakebodhi/CAMEF
3FNSPID Dataset: https://github.com/Zdong104/FNSPID_Financial_News_Dataset

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Yang Zhanget al.
Figure 3: Ablation of GS-Fuse components. We compare
text-only and time-series-only variants (Unimodal-Text,
Unimodal-TS) with multimodal variants that progressively
remove Granger-gated fusion and instance- and token-level
alignment (w/o Alignment & Gating,w/o Alignment,w/o Gat-
ing,w/o Token-Align,Full Model). Bars show MSE (top) and
MAE (bottom); lower is better.
6.1.2 Test Setting.Following prior work on macro announcement
effects [11, 18, 37, 38, 47–49, 56], we assume that event information
is incorporated into prices within at most two trading days. We
therefore evaluate three forecasting horizons: half a trading day, one
full trading day, and two trading days, which at 5-minute frequency
correspond to horizon lengths𝐻∈{ 35, 70, 140}. As in § 3, we set
the look-back length equal to the horizon and use 𝐿=𝐻 in all
experiments.
6.1.3 Implementation Overview.For the single-modality time-series
baselines (ARIMA, DLinear, Autoformer, FEDformer, iTransformer),
we train each model on continuous historical data in a sliding-
window fashion: given a past segment𝑋𝑡−𝐿+1:𝑡 , the model predicts
the next𝐻 steps𝑋𝑡+1:𝑡+𝐻 , with𝐿=𝐻∈{ 35, 70, 140}. At evaluation
time, for an event 𝑖 released at timestamp 𝜏𝑖, we extract its pre-
event window𝑋𝑖 =(𝑥 𝜏𝑖−𝐿+1,...,𝑥 𝜏𝑖) and forecast the subsequent
segment(𝑥𝜏𝑖+1,...,𝑥 𝜏𝑖+𝐻). For multimodal approaches (GPT4MTS,
TEST, TimeCMA, andGS-Fuse), we use the same event-aligned
windows but provide both the event script𝐸𝑖 and pre-event context
𝑋𝑖 as input to predict the post-event trajectory over horizon𝐻. We
provide detailed implementations in Appendices A and B.
6.2 Event-based Market Trend Forecasting
(RQ1)
To answerRQ1, we compare GS-Fuse with twelve statistical, neural,
and foundation-model baselines on five financial datasets (S&P500,
INDU, NASDAQ, USGG1M, USGG5YR) over three horizons (𝐿∈
{35, 70, 140}), reporting MSE and MAE in Table 2. Across all assets
and horizons, GS-Fuse achieves the lowest errors, substantially im-
proving over both time-series foundation models (e.g., on S&P500
with𝐿= 35, GS-Fuse reduces MSE from 1.017 for Kronos to 0.338)
and multimodal baselines such as GPT4MTS and TimeCMA. These
gains are particularly pronounced when event text is noisy or boil-
erplate, where standard cross-attention fusion can overfit irrelevant
tokens, while our Granger-supervised gate only incorporates text
when it provides measurable incremental utility beyond the TS-only
branch. GS-Fuse also remains stable as the horizon extends to two
Table 4: Internal comparison between the TS-only branch
and the full GS-Fuse model. We report MSE (×10−4) and MAE
(×10−3) and the relative improvement ( Δ). The "Avg. Gate"
row indicates the model’s reliance on the text branch.
Method INDU S&P500 USGG1M
MSE MAE MSE MAE MSE MAE
TS-only Branch 18.53 25.30 6.70 15.82 3.99 8.05
Full Model 18.16 24.99 6.60 15.67 3.84 6.89
Improv. (Δ%) +2.0% +1.2% +1.5% +1.0% +3.8% +14.4%
Avg. Text Gate 52.89% 51.55% 60.68%
trading days and generalizes across equity indices and Treasury
yields, with MAE exhibiting the same pattern of improvements as
MSE. The additional DHR and Sharpe results further confirm that
GS-Fuse improves not only point-wise forecasting accuracy, but
also directional prediction and risk-adjusted trading utility.
6.3 Ablation Study on Gating and Alignment
(RQ3)
Fig. 3 illustrates that both unimodal variants (Unimodal-Textand
Unimodal-TS) perform markedly worse than all multimodal config-
urations, confirming that jointly modeling event scripts and pre-
event time series is essential. Among multimodal variants, removing
both Granger-gated fusion and alignment (w/o Alignment & Gating)
yields the largest performance drop, while reintroducing either
the gate (w/o Alignment) or the multi-granularity alignment (w/o
Gating) recovers a substantial portion of the lost accuracy. Further
enabling token-level alignment (w/o Token-Align) brings consistent
additional gains, and the full GS-Fuse model attains the lowest MSE
and MAE across all settings, indicating that Granger-supervised
gating and instance/token-level alignment are complementary and
jointly responsible for the overall improvements.
6.4 Backbone Generality: Performance Across
LLM and Time-Series Encoders (RQ2)
To addressRQ2(backbone generality), we instantiate GS-Fuse with
two compact LLMs, namely LLaMA-3B and Phi-3B, chosen from
top-ranked models on the Hugging Face LLM Leaderboard 4 that
remain trainable on a single RTX 4090 GPU, and with two leading
time-series foundation models, MOMENT (broad multi-domain pre-
training) and Kronos (finance-focused pretraining). Table 3 reports
long-horizon (𝐿= 140) results on INDU and USGG1M and reveals
clear interaction effects: MOMENT pairs best with LLaMA (switch-
ing to Phi consistently worsens both MSE and MAE), whereas
Kronos slightly prefers Phi (yielding small but consistent error re-
ductions). All four combinations remain strong and outperform
time-series-only baselines, indicating that GS-Fuse is backbone-
agnostic but not backbone-independent: carefully matching LLM
and time-series foundations can provide an additional∼5–10% im-
provement on top of the gains established in Table 3.
4Hugging Face LLM Leaderboard: https://huggingface.co/open-llm-leaderboard

{GS-Fuse}: Granger-Gated Multimodal Fusion for Event-Driven Financial Forecasting KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
6.5 Analysis on Granger-Supervised Gating
(RQ4)
As shown in Table 4, GS-Fuse consistently improves over its internal
TS-only branch across the three assets, including the stock indices
INDU, S&P500 and the treasury bond USGG1M, yielding1.5–2.0%
MSE reductions on INDU and S&P500 and a larger3.8%MSE and
14.4%MAE reduction on USGG1M. The averaged text-gate values
are roughly balanced on the equity indices (≈ 51%), but noticeably
higher on USGG1M (60.68%), indicating that the model relies on
macro texts more frequently when forecasting short-term Treasury
yields. These results support the Granger-supervised design: GS-
Fuse preserves the strong TS baseline while selectively leveraging
textual information where it provides greater incremental predictive
value. Appendix C provides additional gate analyses.
7 Conclusion
We introducedGS-Fuse, a Granger-supervised causal fusion frame-
work that models how macro event texts interact with market time
series via gated fusion and multi-granularity alignment. Across five
major assets and multiple horizons, GS-Fuse outperforms strong
baselines, and gate analyses show it relies on text only when event
narratives add predictive value beyond prices, pointing to a solid
foundation for future extensions to richer markets and decision-
centric applications.
Acknowledgements
This work was supported in part by the National Natural Sci-
ence Foundation of China (NSFC) under Grant Nos. 62402396 and
72471197. We would like to thank the anonymous reviewers for
their valuable comments and suggestions that helped improve the
quality of this paper.
References
[1] Abdul Fatir Ansari, Lorenzo Stella, Ali Caner Turkmen, Xiyuan Zhang, Pedro
Mercado, Huibin Shen, Oleksandr Shchur, Syama Sundar Rangapuram, Sebas-
tian Pineda Arango, Shubham Kapoor, Jasper Zschiegner, Danielle C. Maddix,
Hao Wang, Michael W. Mahoney, Kari Torkkola, Andrew Gordon Wilson, Michael
Bohlke-Schneider, and Bernie Wang. 2024. Chronos: Learning the Language of
Time Series.TMLR(2024).
[2] Adebiyi A. Ariyo, Adewumi O. Adewumi, and Charles K. Ayo. [n. d.]. Stock Price
Prediction Using the ARIMA Model. InUKSim-AMSS 2014.
[3] Wuzhida Bao, Yuting Cao, Yin Yang, Hangjun Che, Junjian Huang, and Shiping
Wen. 2025. Data-driven stock forecasting models based on neural networks: A
review.Information Fusion113 (2025), 102616.
[4] Dinesh Bhuriya, Girish Kaushal, Ashish Sharma, and Upendra Singh. 2017. Stock
market predication using a linear regression. InICECA 2017.
[5] Bing Cao, Yiming Sun, Pengfei Zhu, and Qinghua Hu. 2023. Multi-Modal Gated
Mixture of Local-to-Global Experts for Dynamic Image Fusion. InICCV.
[6] C. Q. Cao and R. S. Tsay. 1992. Nonlinear time-series analysis of stock volatilities.
J. Appl. Econom.7, S1 (1992), 165–185.
[7] Defu Cao, Furong Jia, Sercan O Arik, Tomas Pfister, Yixiang Zheng, Wen Ye,
and Yan Liu. 2024. TEMPO: Prompt-based Generative Pre-trained Transformer
for Time Series Forecasting. InThe Twelfth International Conference on Learning
Representations.
[8] Ching Chang, Wei-Yao Wang, Wen-Chih Peng, and Tien-Fu Chen. 2025. LLM4TS:
Aligning Pre-Trained LLMs as Data-Efficient Time-Series Forecasters.ACM Trans.
Intell. Syst. Technol.16, 3 (2025). doi:10.1145/3719207
[9] Minghao Chen, Houwen Peng, Jianlong Fu, and Haibin Ling. 2021. AutoFormer:
Searching Transformers for Visual Recognition. InICCV 2021.
[10] Yuxiao Cheng, Lianglong Li, Tingxiong Xiao, Zongren Li, Jinli Suo, Kunlun He,
and Qionghai Dai. 2024. CUTS+: High-Dimensional Causal Discovery from
Irregular Time-Series.AAAi(2024).
[11] ANNA CIESLAK, ADAIR MORSE, and ANNETTE VISSING-JORGENSEN. 2019.
Stock Returns over the FOMC Cycle.J. Finance74, 5 (2019), 2201–2248.
[12] Zizhen Deng, Hu Tian, Xiaolong Zheng, and Daniel Dajun Zeng. 2025. Deep
Causal Learning: Representation, Discovery and Inference.ACM Comput. Surv.
58, 2 (2025).
[13] Zihan Dong, Xinyu Fan, and Zhiyuan Peng. 2024. FNSPID: A Comprehensive
Financial News Dataset in Time Series. InProceedings of the 30th ACM SIGKDD
Conference on Knowledge Discovery and Data Mining. doi:10.1145/3637528.3671629
[14] Dr. M. Durairaj and B. H. Krishna Mohan. 2022. A convolutional neural network
based approach to financial time series prediction.Neural Comput. Appl.34, 16
(2022), 13319–13337.
[15] Eugene F. Fama. 1965. The Behavior of Stock-Market Prices.J. Bus.38, 1 (1965),
34–105.
[16] Eugene F. Fama, Lawrence Fisher, Michael C. Jensen, and Richard Roll. 1969. The
Adjustment of Stock Prices to New Information.Int. Econ. Rev.10, 1 (1969), 1–21.
[17] Bianca-Mihaela Ganescu, Suchir Salhan, Andrew Caines, and Paula Buttery.
2025. Looking to Learn: Token-wise Dynamic Gating for Low-Resource Vision-
Language Modelling. InBabyLM.
[18] Pavel Gertler and Roman Horvath. 2018. Central bank communication and
financial markets: New high-frequency evidence.J. Financ. Stab.36 (2018), 336–
345.
[19] T Gilbert, C Scotti, G Strasser, and C Vega. 2010. Why do certain macroeconomic
news announcements have a big impact on asset prices? InAppl. Econom. Forecast.
Macro. Finance Workshop.
[20] Linda Goldberg and Christian Grisse. 2013.Time variation in asset price responses
to macro announcements. Working Papers 2013-11. Swiss National Bank.
[21] Mononito Goswami, Konrad Szafer, Arjun Choudhry, Yifu Cai, Shuo Li, and Artur
Dubrawski. 2024. MOMENT: A Family of Open Time-series Foundation Models.
InICML 2024.
[22] C.W.J. Granger. 1980. Testing for causality: A personal viewpoint.Journal of
Economic Dynamics and Control2 (1980), 329–352.
[23] Huy D. Huynh, L. Minh Dang, and Duc Duong. 2017. A New Model for Stock
Price Movements Prediction Using Deep Neural Network. InSoICT 2017.
[24] Tae Hyup Roh. 2007. Forecasting the volatility of stock price index.Expert Syst.
Appl.33, 4 (2007), 916–922.
[25] Furong Jia, Kevin Wang, Yixiang Zheng, Defu Cao, and Yan Liu. 2024. GPT4MTS:
Prompt-based Large Language Model for Multimodal Time-series Forecasting.
AAAI 2024(2024).
[26] Ming Jin, Shiyu Wang, Lintao Ma, Zhixuan Chu, James Y. Zhang, Xiaoming Shi,
Pin-Yu Chen, Yuxuan Liang, Yuan-Fang Li, Shirui Pan, and Qingsong Wen. 2024.
Time-LLM: Time Series Forecasting by Reprogramming Large Language Models.
InThe Twelfth International Conference on Learning Representations.
[27] Baoyu Jing, Dawei Zhou, Kan Ren, and Carl Yang. 2024. Causality-Aware Spa-
tiotemporal Graph Neural Networks for Spatiotemporal Time Series Imputation.
InCIKM.
[28] Saurabh Khanna and Vincent Y. F. Tan. 2020. Economy Statistical Recurrent
Units For Inferring Nonlinear Granger Causality. InICLR.
[29] Geon Lee, Wenchao Yu, Wei Cheng, and Haifeng Chen. 2024. MoAT: Multi-Modal
Augmented Time Series Forecasting. OpenReview
[30] Qing Li, TieJun Wang, Ping Li, Ling Liu, Qixu Gong, and Yuanzhu Chen. 2014.
The effect of news and public mood on stock movements.Information Sciences
278 (2014), 826–840.
[31] Songtao Li and Hao Tang. 2025. Multimodal Alignment and Fusion: A Survey.
arXiv:2411.17040 [cs.CV]
[32] Chenxi Liu, Qianxiong Xu, Hao Miao, Sun Yang, Lingzheng Zhang, Cheng Long,
Ziyue Li, and Rui Zhao. 2025. TimeCMA: Towards LLM-Empowered Multivariate
Time Series Forecasting via Cross-Modality Alignment.Proceedings of the AAAI
Conference on Artificial Intelligence39, 18 (Apr. 2025), 18780–18788. doi:10.1609/
aaai.v39i18.34067
[33] Huicheng Liu. 2018. Leveraging Financial News for Stock Trend Prediction with
Attention-Based Recurrent Neural Network.arXiv(2018).
[34] Yong Liu, Guo Qin, Xiangdong Huang, Jianmin Wang, and Mingsheng Long.
2024. AutoTimes: Autoregressive Time Series Forecasters via Large Language
Models. InAdvances in Neural Information Processing Systems, A. Globerson,
L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang (Eds.),
Vol. 37. 122154–122184. doi:10.52202/079017-3882
[35] Yong Liu, Haoran Zhang, Chenyu Li, Xiangdong Huang, Jianmin Wang, and
Mingsheng Long. 2024. Timer: Generative Pre-trained Transformers Are Large
Time Series Models. InICML 2024.
[36] Zehao Liu, Mengzhou Gao, and Pengfei Jiao. 2025. GCAD: Anomaly Detection
in Multivariate Time Series from the Perspective of Granger Causality.AAAI
(2025).
[37] DAVID O. LUCCA and EMANUEL MOENCH. 2015. The Pre-FOMC Announce-
ment Drift.J. Finance70, 1 (2015), 329–371.
[38] Donato Masciandaro, Oana Peia, and Davide Romelli. 2024. Central bank com-
munication and social media: From silence to Twitter.J. Econ. Surv.38, 2 (2024),
365–388.
[39] Puneet Mathur, Atula Neerkaje, Malika Chhibber, Ramit Sawhney, Fuming Guo,
Franck Dernoncourt, Sanghamitra Dutta, and Dinesh Manocha. 2022. MONOP-
OLY: Financial Prediction from MONetary POLicY Conference Videos Using

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Yang Zhanget al.
Multimodal Cues. InMM 2022.
[40] Thien Hai Nguyen, Kiyoaki Shirai, and Julien Velcin. 2015. Sentiment analysis
on social media for stock movement prediction.Expert Syst. Appl.42, 24 (2015),
9603–9611.
[41] Kun Ouyang, Yi Liu, Shicheng Li, Ruihan Bao, Keiko Harimoto, and Xu Sun. 2024.
Modal-adaptive Knowledge-enhanced Graph-based Financial Prediction from
Monetary Policy Conference Calls with LLM. InFinNLP-KDF-ECONLP 2024.
[42] John Edison Arevalo Ovalle, Thamar Solorio, Manuel Montes-y-Gómez, and
Fabio A. González. 2017. Gated Multimodal Units for Information Fusion. InICLR
Workshop.
[43] Zijie Pan, Yushan Jiang, Sahil Garg, Anderson Schneider, Yuriy Nevmyvaka, and
Dongjin Song. 2024. $S^2$IP-LLM: Semantic Space Informed Prompt Learning
with LLM for Time Series Forecasting. InICML.
[44] G. Pui Cheong Fung, J. Xu Yu, and Wai Lam. 2003. Stock prediction: Integrating
text mining approach using real-time news. InCIFEr. 395–402.
[45] Yu Qin and Yi Yang. 2019. What You Say and How You Say It Matters: Predicting
Stock Volatility Using Verbal and Vocal Cues. InACL 2019.
[46] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh,
Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark,
Gretchen Krueger, and Ilya Sutskever. 2021. Learning Transferable Visual Models
From Natural Language Supervision. InICML.
[47] Carlo Rosa. 2011. Words that shake traders: The stock market’s reaction to central
bank communication in real time.J. Empir. Finance18, 5 (2011), 915–934.
[48] Carlo Rosa. 2013. The financial market effect of FOMC minutes.Econ. Policy Rev.
(2013), 67–81.
[49] Carlo Rosa. 2016. Fedspeak: Who Moves U.S. Asset Prices?Int. J. Cent. Bank.12,
4 (2016), 223–261.
[50] Ramit Sawhney, Shivam Agarwal, Arnav Wadhwa, and Rajiv Ratn Shah. 2020.
Deep Attentive Learning for Stock Movement Prediction From Social Media Text
and Company Correlations. InEMNLP 2020.
[51] Ramit Sawhney, Puneet Mathur, Ayush Mangal, Piyush Khanna, Rajiv Ratn Shah,
and Roger Zimmermann. 2020. Multimodal Multi-Task Financial Risk Forecasting.
InMM 2020.
[52] Sreelekshmy Selvin, R Vinayakumar, E. A Gopalakrishnan, Vijay Krishna Menon,
and K. P. Soman. 2017. Stock price prediction using LSTM, RNN and CNN-sliding
window model. InICACCI 2017.
[53] Agam Shah, Suvan Paturi, and Sudheer Chava. 2023. Trillion Dollar Words: A
New Financial Dataset, Task & Market Analysis. InACL 2023.
[54] Yu Shi, Zongliang Fu, Shuo Chen, Bohan Zhao, Wei Xu, Changshui Zhang, and
Jian Li. 2025. Kronos: A Foundation Model for the Language of Financial Markets.
InRecent Advances in Time Series Foundation Models Have We Reached the ’BERT
Moment’?
[55] Jianfeng Si, Arjun Mukherjee, Bing Liu, Qing Li, Huayi Li, and Xiaotie Deng.
2013. Exploiting Topic based Twitter Sentiment for Stock Prediction. InACL
2013.
[56] Raul Cruz Tadle. 2022. FOMC minutes sentiments and their impact on financial
markets.J. Econ. Bus.118 (2022), 106021.
[57] Sabera J Talukder, Yisong Yue, and Georgia Gkioxari. 2024. TOTEM: TOkenized
Time Series EMbeddings for General Time Series Analysis.TMLR(2024).
[58] Stephen J Taylor. 2007.Modelling Financial Time Series. World Scientific Publish-
ing.
[59] Qianqian Xie, Weiguang Han, Yanzhao Lai, Min Peng, and Jimin Huang. 2023.
The Wall Street Neophyte: A Zero-Shot Analysis of ChatGPT Over MultiModal
Stock Movement Prediction Challenges.
[60] Yumo Xu and Shay B. Cohen. 2018. Stock Movement Prediction from Tweets
and Historical Prices. InACL 2018.
[61] Linyi Yang, Tin Lok James Ng, Barry Smyth, and Riuhai Dong. 2020. HTML:
Hierarchical Transformer-based Multi-task Learning for Volatility Prediction. In
WWW 2020.
[62] Lewei Yao, Runhui Huang, Lu Hou, Guansong Lu, Minzhe Niu, Hang Xu, Xiaodan
Liang, Zhenguo Li, Xin Jiang, and Chunjing Xu. 2022. FILIP: Fine-grained In-
teractive Language-Image Pre-Training. InInternational Conference on Learning
Representations.
[63] Xinli Yu, Zheng Chen, and Yanbin Lu. 2023. Harnessing LLMs for Temporal Data
- A Study on Explainable Financial Time Series Forecasting. InEMNLP.
[64] Yang Zhang, Wenbo Yang, Jun Wang, Qiang Ma, and Jie Xiong. 2025. CAMEF:
Causal-Augmented Multi-Modality Event-Driven Financial Forecasting by Inte-
grating Time Series Patterns and Salient Macroeconomic Announcements. In
Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data
Mining V.2 (KDD ’25). 3867–3878. doi:10.1145/3711896.3736872
[65] Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianxin Li, Hui Xiong,
and Wancai Zhang. 2021. Informer: Beyond Efficient Transformer for Long
Sequence Time-Series Forecasting. InAAAI 2021.
[66] Tian Zhou, Ziqing Ma, Qingsong Wen, Xue Wang, Liang Sun, and Rong Jin. 2022.
FEDformer: Frequency Enhanced Decomposed Transformer for Long-term Series
Forecasting. InICML 2022.
[67] Wenzhang Zhou, Dawei Du, Libo Zhang, Tiejian Luo, and Yanjun Wu. 2022. Multi-
Granularity Alignment Domain Adaptation for Object Detection. InProceedings
of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).
9581–9590.
[68] Zhihan Zhou, Liqian Ma, and Han Liu. 2021. Trade the Event: Corporate Events
Detection for News-Based Event-Driven Trading. InACL Findings.
[69] Shihao Zou, Xianying Huang, and Xudong Shen. 2023. Multimodal Prompt
Transformer with Hybrid Contrastive Learning for Emotion Recognition in
Conversation. InMM.
A Implementation Details for Baselines and
GS-Fuse
Single-modality baselines (ARIMA, DLinear, Autoformer, FEDformer,
iTransformer, PatchTST) are adapted from Time-Series-Library5 to
the event-driven setting, using pre-event segments to predict 35-,
70-, and 140-step horizons. All these baselines are trained for 10
epochs with batch size 32.
As multimodal baselines, we use TEST6, GPT4MTS7, and TimeCMA
8. We adapt their official implementations to the same event-driven
forecasting horizons (35, 70, and 140 steps) and keep their default
hyperparameters.
For time-series foundation models, including MOMENT, Kronos,
TimesFM, and Chronos, we use the official repositories9 and retrain
them on our event-driven setup for 10 epochs with batch size 32.
ForGS-Fuse, we adopt the three-stage training paradigm de-
scribed in §5, training each stage for 2 epochs with batch size 32.
B Hyperparameter Setting of GS-Fuse
All hyperparameters are fixed across datasets. The shared fusion
dimension is set to𝐹= 1024to match the typical scale of LLM and
time-series foundation model embeddings and to provide sufficient
capacity for cross-modal interactions without making the model
excessively large. The look-back length𝐿 and forecast horizon𝐻
follow standard settings in event-driven forecasting (roughly one
pre-event day and up to two post-event days) so that our setup is
comparable to prior work. For the backbone encoders, we select
compact open-weight LLMs (LLaMA / Phi-3 family) and time-series
foundation models (MOMENT / Kronos) as a pragmatic trade-off
between representation quality and computational cost.
For multi-granularity alignment, we adopt conventional contrastive-
learning temperatures and anchor sizes. The instance-level and
token-level temperatures𝜏ctr,𝜏 al,𝜏 nce are chosen in the typical range
used in contrastive and vision–language models (on the order of
10−2–10−1), which yields non-degenerate softmax distributions
while keeping gradients stable. The number of in-batch negatives
𝑁neg and the top-𝐾 token anchors are set to 𝐾top = 256, which
typically covers about 30%–50% of tokens in our event scripts. This
provides a balance between capturing salient spans and avoiding
excessive influence from noisy or redundant tokens.
For the Granger-supervised gate, we use simple, stable defaults.
The gating temperature𝜏gate = 1.0, gain𝛾= 1.0, minimum scale𝜖,
and clipping threshold𝑐 are set so that the responsibility signal𝑟𝑖
5Time-Series-Library: https://github.com/thuml/Time-Series-Library
6TEST: https://github.com/SCXsunchenxi/TEST
7GPT4MTS: https://github.com/Flora-jia-jfr/GPT4MTS-Prompt-based-Large-
Language-Model-for-Multimodal-Time-series-Forecasting
8TimeCMA: https://github.com/ChenxiLiu-HNU/TimeCMA
9MOMENT: https://github.com/moment/moment
Kronos: https://github.com/shiyu-coder/Kronos
TimesFM: https://github.com/google-research/timesfm
Chronos: https://github.com/amazon-science/chronos-forecasting

{GS-Fuse}: Granger-Gated Multimodal Fusion for Event-Driven Financial Forecasting KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
Table 5: Hyperparameters ofGS-Fuseused in experiments.
Module Symbol Value Role
Encoders
𝐹1024 Shared text–time-series fusion dimen-
sion.
𝐿task-dependent Look-back length of the pre-event
time series.
𝐻task-dependent Forecast horizon length.
𝑓LLM LLaMA / Phi-3 family Backbone text encoder for event
scripts.
𝑓TS MOMENT / Kronos Time-series foundation encoder for
market context.
Alignment
𝜏ctr tuned Temperature in instance-level In-
foNCE loss𝐿 ctr.
𝑁neg in-batch Number of negatives per anchor in
𝐿ctr.
𝜏al 0.2 Temperature in token–step similarity
matrix𝑆𝑖.
𝜏nce 0.07 Temperature in token-level InfoNCE
loss𝐿 tok.
𝐾top 256 Number of top-salience text tokens
forming anchor set𝐴𝑖.
Granger gate
𝜏gate 1.0 Softmax temperature for feature-wise
modality gating.
𝜖10 −6 Minimum scale in 𝑠Δ =
max 1 𝑁 ˝ 𝑖|Δ𝑖|,𝜖 .
𝛾1.0 Gain factor in responsibility target𝑟𝑖.
𝑐6.0 Clipping threshold for scaled utility
before sigmoid.
𝜏gc 𝑠Δ/𝛾 Effective Granger temperature in-
duced by scaling.
Decoder
𝐿dec 3 Number of Transformer decoder
blocks.
𝑛head 16 Attention heads per decoder block.
𝑑dec 𝐹(1024) Decoder hidden dimension.
𝐾reg 2 Depth of regression head MLP.
𝜌(·)GELU Activation function in the regression
head.
Loss weights 𝜆align 0.2 Weight of alignment loss𝐿align in the total objective.
𝜆gate 0.1 Weight of gate loss 𝐿gate in the total
objective.
meaningfully reflects the error gap between the time-series-only
and multimodal branches while keeping logits in a numerically safe
range. The resulting effective Granger temperature𝜏gc =𝑠 Δ/𝛾 can
be viewed as an automatic rescaling of this gap; this mechanism is
kept fixed rather than tuned per dataset.
The decoder configuration is intentionally lightweight. A 3-layer
Transformer decoder with𝑛head = 16and hidden size 𝑑dec =𝐹 (i.e.,
64 dimensions per head) provides a good balance between expres-
siveness and runtime. The regression head is a 2-layer MLP with
GELU activations, a standard choice in Transformer architectures
that introduces mild nonlinearity without many extra parameters.
Finally, the loss weights are set to keep forecasting as the primary
objective. The alignment and gate losses are down-weighted by
𝜆align = 0.2and 𝜆gate = 0.1, respectively, so that they regularize the
model toward consistent cross-modal representations and Granger-
consistent gating but do not overwhelm the core MSE+MAE fore-
casting loss. These settings are intentionally simple, fixed across
all experiments, and consistent with the qualitative role of each
component.
C Additional Analysis of Gate Openness
To better understand how GS-Fuse uses event text, we examine
the distribution of the learned text-gate openness across datasets
and event types. As shown in Fig. 4, gate values for the two equity
indices (S&P500,INDU) concentrate around0 .51–0.53, whereas
USGG1Mexhibits a substantially higher central tendency (around
0.60). This indicates that GS-Fuse relies more heavily on textual
information when forecasting short-term interest rates than when
forecasting equity indices, consistent with the stronger sensitivity
of bond markets to macroeconomic announcements.
Within each dataset, the gate distributions over different macroe-
conomic event types (FOMC decisions, employment situation, un-
employment insurance, CPI releases, PPI releases, and GDP an-
nouncements) vary only within a narrow band, suggesting broadly
consistent usage of text across heterogeneous announcements.
Within this band, monetary policy and inflation-related events
(FOMC, CPI, PPI) tend to show slightly higher openness than labor-
market releases, indicating that the model assigns somewhat greater
incremental predictive value to events that directly convey policy
stance and price-level information.
D Case Study: Token Alignment Analysis
We randomly sample two held-out event scripts, oneFOMC de-
cisionand onePPI release, to qualitatively inspect whether the
top aligned(highlighted) tokens within each script are economi-
cally meaningful rather than boilerplate. The following subsections
illustrate detailed analyses.
D.1 Case 1: FOMC Decision Script
At the meeting , the committee decided to keep the
federal funds rate target range at 0-0.25% . The
committee also decided to end its asset purchase pro-
gram in October and maintain its existing policy
of reinvesting principal payments. The committee noted
that economic activity was expanding at a moderate pace,
with labor market conditions improving further, and
inflation running below its 2% longer-run goal.
From the highlighted tokens above, we observe that the model
consistently attends to the policy instrument and its numerical
setting, aligning the phrase “federal funds rate target range” with
the corresponding interval “0–0.25%. ” At the same time, it empha-
sizes mandate-relevant clauses such as “labor market conditions”
and “inflation. . . 2% longer-run, ” which govern expectations about
future policy. These patterns suggest that the token-wise alignment
module is sensitive to both the current policy threshold and the
macroeconomic conditions that define the event’s market impact.
D.2 Case 2: PPI Report Event Script
The PPI for food and beverages increased by
1.3% from May 2021 to June 2021 ... The PPI for
transportation services increased by 7.2% , driven by
higher prices for gasoline, diesel fuel, and air travel . The PPI
for services related to transportation activities
increased by 23.5% . The PPI for investment services
increased by 25.7% . The PPI for real estate
services increased by 5.5% . The PPI for rental and
leasing of goods increased by 17.8% .

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Yang Zhanget al.
(a) Gate openness across datasets.
 (b)S&P500: gate openness by event type.
(c)INDU: gate openness by event type.
 (d)USGG1M: gate openness by event type.
Figure 4: Distributions of learned text-gate openness. (a) Aggregate gate openness across datasets. (b)–(d) Gate openness stratified
by macroeconomic event type forS&P500,INDU, andUSGG1M.
From this case, we note that the alignment module consistently
selects the index name (“PPI”), the sector descriptors (“food and bev-
erages, ” “transportation services, ” “investment services, ” “real estate
services, ” “rental and leasing of goods”), and the associated direc-
tional and quantitative cues (“increased, ” along with the percentage
changes such as “1.3%, ” “7.2%, ” “23.5%, ” “25.7%, ” “5.5%, ” “17.8%”). This
pattern suggests that the token-alignment mechanism is sensitive
not only to the overall index label but also to the decomposition
of inflation across sectors and the relative size of each sector’s
price change, which are exactly the components that matter for
downstream market reactions.
Limitations and Future Directions
While GS-Fuse delivers consistent gains over strong unimodal and
multimodal baselines across five major U.S. assets and three hori-
zons, our study still has a bounded scope. We focus on macroeco-
nomic announcements in the U.S. and a small set of highly liquid
benchmarks at 5-minute frequency, and we evaluate point forecasts
(MSE/MAE) of prices and yields rather than volatility or tail risk.
Extending GS-Fuse to additional asset classes, geographies, frequen-
cies, and risk-sensitive or strategy-level evaluations is a natural
direction for future work rather than a limitation of the framework
itself.
From a modeling perspective, we instantiate GS-Fuse with com-
pact LLM backbones and two representative time-series foundation
models, and keep these encoders mostly frozen to respect realis-
tic GPU budgets. We adopt commonly used hyperparameters for
baselines and set GS-Fuse–specific ones by conceptual choices, so
further tuning could in principle improve performance. Our fusion
module also uses a smooth soft gate for stability; sharper gating
settings could be explored in future work.
Finally, our Granger-style supervision should be viewed as a prin-
cipled predictive utility signal rather than a full structural causal
claim. We assume macro texts are exogenous information shocks
and do not explicitly model all possible confounders or regime
shifts. In practice, deploying GS-Fuse in high-stakes settings would
benefit from complementary components such as regime detec-
tion, uncertainty quantification, and more sophisticated document
compression or longer-context encoders, which we leave for future
work.
