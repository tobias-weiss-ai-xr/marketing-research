---
title: Pushing the Limits of High-Resolution Weather Forecasting through Data Scaling
url: https://arxiv.org/abs/2608.14652
category: ai-marketing
subcategory: measurement
date: 2026-07
venue: ''
authors:
- Yang Zhao
- Peisong Niu
- Tian Zhou
- Ziqing Ma
- Guanlong Ma
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.14652
pages: 43
chars: 104920
fetched_at: '2026-11-08T13:29:45+00:00'
kb_version: 1
---

# Pushing the Limits of High-Resolution Weather Forecasting through Data Scaling

Pushing the Limits of High-Resolution Weather
Forecasting through Data Scaling
Yang Zhao*1,2,4 , Peisong Niu*3,4 , Tian Zhou*3,4 , Ziqing Ma4 , Guanlong
Ma1,2 , Rong Jin4, Huiling Yuan†1,2 , and Liang Sun†3,4
1 State Key Laboratory of Severe Weather Meteorological Science and Technology,
Nanjing University, Nanjing, China
2 School of Atmospheric Science, Nanjing University, Nanjing, China
3 Ant Healthcare, Ant Group, Hangzhou, China
4 DAMO Academy, Alibaba Group, Hangzhou, China
{zhaoy2024,guanlongma}@smail.nju.edu.cn,yuanhl@nju.edu.cn
{niupeisong.nps,tian.zt,ls.537724}@antgroup.com
maziqing.mzq@alibaba-inc.com,rongjinemail@gmail.com
Abstract.The development of0.1 ◦ global weather forecasting models
based on machine learning (ML) is constrained by the limited availabil-
ity of high-resolution data, as decades of reanalysis are only available
at0.25 ◦ resolution. While existing approaches fine-tune0.25 ◦ forecast
models on limited0.1 ◦ samples, we show that this transfer is hindered
by the irreversible information loss inherent in coarse-resolution fore-
casting. Therefore, we proposeBaguanHR, a framework that shifts
the focus from transferring models to transferring data. We first show
that super-resolution (SR) has lower conditional entropy and input am-
plification than forecasting, making it a more robust vehicle for reso-
lution transfer. By leveraging this advantage through variable-wise SR,
we synthesize extensive0.1◦ data from ERA5. BaguanHR’s performance
on the synthetic-plus-real dataset exceeds both ML-based methods and
IFS-HRES, achieving superior performance across over 85% of the lead
times within 72 hours. Furthermore, our findings highlight a power-law
scaling effect, as a twofold increase in data reduces RMSE by 4.6% for 72-
hour forecasting and 4.9% for 120-hour forecasting. Our results demon-
strate that scaling high-resolution ML-based forecasting is primarily a
data bottleneck, and that variable-wise super-resolution provides a sim-
ple yet general solution to unlock long coarse-resolution reanalyses for
high-resolution training.
Keywords:Weather forecasting·Scaling law·High-resolution
1 Introduction
The field of global weather forecasting is witnessing a profound change, with
data-driven models now outperforming established numerical weather prediction
*These authors contributed equally to this work.
†Corresponding authors.
arXiv:2608.14652v1  [cs.LG]  31 Jul 2026

2 Y. Zhao et al.
systems at medium ranges [3,5,6,21,22,24,31]. However, advancing these mod-
els toward higher spatial resolution remains fundamentally constrained by the
availability of long, consistent, high-resolution global datasets. For example, the
European Center for Medium-Range Weather Forecasts (ECMWF) operational
analysis provides global0.1 ◦ (roughly 9km) data only after 2016 [27], yielding
at most about 10 years of training data up to 2026, which is far too limited for
training large-scale ML forecast models without severe overfitting. In contrast,
reanalysis data such as ERA5 [16] provides 47 years of data (up to 2026) only at
a coarser0.25◦ resolution, creating a resolution–data imbalance that has become
a critical bottleneck for high-resolution ML weather forecasting.
A recent line of work attempts to overcome this challenge by transferring a
pretrained0.25 ◦ forecast model to0.1 ◦ through architectural design and fine-
tuning on the small amount of0.1◦ high-resolution data [4,14]. This strategy
leverages prior dynamical knowledge encoded in the coarse model but is inher-
ently limited by two factors. First, the pretrained coarse-resolution model cannot
fully exploit the rich information contained in the0.1◦ analysis fields because its
learned representation is tied to the low-resolution grid. Second, weather predic-
tion is a significantly more complex task than downscaling; adapting a coarse-
resolutionforecastmodeltoafinergridrequireslearningbothfine-scaleprocesses
and the correct multiscale dynamics, which is difficult to achieve through limited
fine-tuning. As a result, coarse-to-fine transfer often yields restricted accuracy
improvements and depends heavily on sophisticated architectural modifications.
We propose a paradigm shift: transfer data, not models.Our core insight is
that super-resolution (SR) is a same-time conditional reconstruction
task with provably lower conditional entropy than multi-step fore-
casting.Following this insight, SR should be (i) intrinsically easier to learn,
(ii) more stable under imperfect inputs, and (iii) suitable as a scalable mecha-
nism to break the data bottleneck in high-resolution forecasting. We test these
implications through a set of experiments that sequentially close this reasoning
loop.
SR FC
0.600
0.625
0.650
0.675
0.700
0.725
0.750
0.775
0.800
RMSE
t2m
0.709
0.744
Amp (SR)
Amp (FC)
0.4
0.6
0.8
1.0
1.2
Amplification
0.01 0.05 0.1 0.15 0.2 0.25
Noise level
SR FC
0.600
0.625
0.650
0.675
0.700
0.725
0.750
0.775
0.800
RMSE
u10
0.691
0.708
0.6
0.8
1.0
1.2
Amplification
0.01 0.05 0.1 0.15 0.2 0.25
Noise level
SR FC
10
12
14
16
18
20
22
24
26
28
RMSE
z500
13.8
23.6
0.7
0.8
0.9
1.0
1.1
1.2
Amplification
0.01 0.05 0.1 0.15 0.2 0.25
Noise level
Fig.1:Entropy-based Robustness evaluation for t2m, u10, and z500. Thex-axis cor-
responds to different noise levels, and they-axis is the RMSE and amplification factor.
Lower amplification factors reflect greater inherent stability.

High-Resolution Weather Forecasting via Data Scaling 3
Weinvestigatethemechanismsunderlyingourapproachthroughtwoprimary
lenses. First, we analyze the robustness of SR and forecasting (FC) for t2m, u10
and z500, as shown in Fig. 1. By measuring the error growth per unit of injected
Gaussian noise (amplification factor) for both tasks, we find that: (i)SR is a
simpler task, yielding much lower RMSE than one-step forecasting (e.g., 13.8
vs. 23.6 for z500), which aligns with [13,28]; and (ii)SR is more stable, with an
amplification factor (0.6–0.8×) significantly lower than that of forecasting (1.0–
1.2×). Second, ourdata scaling law analysis(Sec. 5.2) demonstrates that
0.1◦ forecasting is strongly data-limited, exhibiting power-law improvements as
training volume increases. Specifically, expanding the training data from 7 to 18
years reduces RMSE by more than 4.5% at long lead times.
Buildingonthesefindings,weemployasynthetic-plus-realstrategy.Specif-
ically, we train per-variable SR models on limited paired0.1◦–0.25◦ samples,
apply them to decades of ERA5 to synthesize high-resolution0.1◦ training data,
and then train0.1 ◦ forecast models from scratch. This data-transfer approach
substantially outperforms coarse-to-fine baselines without specialized architec-
tures or fine-tuning, indicating that scaling high-resolution ML forecasting is
best addressed by data construction via variable-wise super-resolution.
The main contributions of our work are as follows:
–We propose BaguanHR, a framework leveraging the low conditional entropy
of super-resolution (SR) as a robust data augmentation strategy for high-
resolution weather forecasting. BaguanHR outperforms various ML-based
models and IFS-HRES. Specifically, over85%of lead times show superior
performance within 72 hours, highlighted by a4.0%RMSE reduction com-
pared specifically to IFS-HRES.
–We conduct a comprehensive investigation from both experimental and the-
oretical perspectives to elucidate the mechanisms underlying the effective-
ness of synthetic-plus-real strategy. By leveraging the inherent robustness
of per-variable SR, our approach achieves up to a 20% reduction in RMSE
compared to traditional coarse-to-fine methods, establishing a more stable
framework for high-resolution modeling.
–We establish fundamental data scaling laws in high-resolution forecasting,
revealing that performance improves following a power law as data volume
increases. Specifically, expanding the training dataset from 7 to 18 years
yields a4.9%reduction in RMSE for long-term (120-hour) forecasts and
4.6%for 72-hour forecasts.
–Our study highlights a shift in perspective: for high-resolution ML-based
weather forecasting, data construction via super-resolution proves more scal-
able and effective than architectural design or transfer learning. As the
data availability is the primary bottleneck in high-resolution forecasting,
our paradigm addresses the data directly, and can be expanded to other
high-resolution tasks.

4 Y. Zhao et al.
2 Related Work
2.1 Data-Driven Weather Forecasting Models
Moving beyond the resolution limits of0.25 ◦ models [3–6,22,31], recent0.1 ◦
forecasting efforts [4,14] focus on transferring knowledge from pretrained coarse-
grained systems. Aurora [4] introduces bilinear upscaling for patch alignment,
whileFengwu-GHR[14]employsidentity-preservingmappingsforhigh-resolution
extrapolation. These methods highlight a growing trend of leveraging trans-
fer learning to achieve operational-grade precision, but they still treat high-
resolution forecasting primarily as a model-transfer problem under limited0.1◦
data. In contrast, our approach tackles the same challenge from a data-centric
perspective by expanding the effective0.1 ◦ dataset via super-resolution. This
data-centricrouteiscomplementarytoneural-operatormethods,includingFourier
Neural Operators and coarse-graining operators [25,36], which address multi-
resolution physical modeling from an architecture-centric perspective.
2.2 Scaling in Weather Forecasting Task
Inspired by the scaling laws in NLP [19] and CV [7,38], recent studies have
begun exploring the relationship between compute, data, and performance in
meteorology. While [31] analyzed model and data scaling at resolutions below
0.25◦, [37] reported fundamental power laws across model size and compute
budget. However,whether these performance gains persist when scaling
data at0.1◦ resolutionremains an open question, especially given the scarcity
of high-resolution analysis data. This motivates our investigation into effective
data-scaling strategies within high-resolution regimes.
3 Rationale for Synthetic-to-Real Transfer
3.1 Robustness Evaluation: Super-Resolution vs. Forecasting
To justify the adoption of Super-Resolution as a superior data augmentation
strategy, we conduct a comparative analysis between two paradigms: forecasting
(temporal evolution) and super-resolution (spatial reconstruction) under varying
levels of input noise. The formulations for these tasks are defined as follows:
– High-Resolution Forecasting (FC):BaguanHR is designed to generate
global medium-range forecasts at a0.1◦ spatial resolution (H= 1801, W=
3600). LetX t ∈R V×H×W represent the atmospheric state at timet, where
Vdenotes the number of variables. The forecasting model aims to learn a
mappingΦ F :X t →X t+∆t, where∆t= 6hours. Future states are predicted
in an auto-regressive manner, utilizing the previous output as input for the
subsequent step.

High-Resolution Weather Forecasting via Data Scaling 5
– Super-Resolution (SR):To augment the training data, we define a spa-
tial reconstruction task to bridge the gap between coarse reanalysis and
high-resolution analysis data. Given a low-resolution stateZt ∈R V×H ′×W ′
(0.25◦), the SR model learns a mappingΦSR :Z t → ˆXt, producing a0.1 ◦
pseudo-label ˆXt that maintains physical consistency with the source data
while enhancing spatial detail.
To evaluate model robustness, we perturb input fields with Gaussian noise
δ∼ N(0, σ2)at varying intensitiesσ. Sensitivity is quantified by anamplifica-
tion factor, defined as the change in prediction error relative to the baseline,
normalized by the noise magnitude:(|RMSEσ −RMSE 0|/σ). This metric cap-
tures the marginal response of SR and FC models to input perturbations. By
isolating the incremental error caused solely by input perturbations, this factor
reveals the intrinsic stability of the model’s mapping function. A high amplifi-
cation factor suggests that small input fluctuations are significantly magnified
during the inference process, whereas a low factor signifies a resilient architec-
ture.
Our analysis reveals that the SR approach offers distinct advantages over the
FC method in two key aspects. First, as illustrated in Fig. 1, SR consistently
exhibits significantly lower amplification factors than forecasting across all tested
meteorological variables, including t2m, u10, and z500. Second, SR maintains
a substantial advantage in RMSE compared to the FC model at every noise
intensity. Together, these findings suggest that SR is fundamentally less sensitive
to input uncertainties and more effective at suppressing error propagation. These
results demonstrate thatSR’s inherent stability and resilience to input
perturbations validate its application in robust data augmentation.
3.2 Synthetic-plus-Real vs. Coarse-to-Fine Adaptation
1 5 10
500
600
700
850
925
1000 Pressure (hPa)
u
1 5 10
v
1 5 10
t
1 5 10
q
1 5 10
z
 t2m
 u10
v10
 msl
d2m
 tcw
1 5 10
tcc
1 5 10
tp6h
20%
0%
+20%
RMSE relative to Coarse-to-fine
Lead time (days)
Fig.2:Comparative performance of the “synthetic-plus-real” training-from-scratch
paradigm versus the “coarse-to-fine transfer” approach. Thex-axis is the lead time
(days), and different colors show different values of relative RMSE difference.
At the onset of our study, we conduct a comprehensive comparison between
two technical paradigms for high-resolution adaptation: the conventional “coarse-

6 Y. Zhao et al.
to-fine” approach and our proposed “synthetic-plus-real” strategy. This compar-
ison serves to identifywhether model-level transfer or data-driven aug-
mentation provides a more effective route for0.1◦ modeling.
Experimental SetupCurrent0.1 ◦ resolution models, represented primarily
by [14] and [4], both follow a ‘coarse-to-fine’ technical route. In this work, we
choose to implement our scheme by reproducing the methodology established
by [14], which adapts a pre-trained0.25◦ model to0.1 ◦ resolution through de-
compositional and combinational transfer learning. In contrast, the “synthetic-
plus-real” paradigm, as described in Sec. 4, augments the training set by gen-
erating high-resolution synthetic data and trains the0.1◦ model from scratch.
To ensure a fair comparison, both paradigms are evaluated on 2025 real-time
analysis data.
Training DatasetsThe “synthetic-plus-real” training set integrates two key
components:
– Real-Time Analysis Data:We utilize0.1◦ ECMWF 4D-Var analysis data
(2017–2024). For accumulated variables (fdir, ssrd, and tp) unavailable in the
analysis archive, we source them from zero-hour IFS-HRES forecasts.
– Synthetic Data:To supplement the limited0.1◦ archive, we apply a per-
variable super-resolution (SR) model to0.25◦ ERA5 reanalysis (2007–2016).
This yields 10 years of0.1◦ pseudo-labels that maintain the physical consis-
tency of the original ERA5 records.
The complete dataset encompasses 13 standard pressure levels (50–1000 hPa)
for upper-air variables (z, t, u, v, q) and a comprehensive set of surface param-
eters, including standard meteorological fields (t2m, d2m, u10, v10, msl, sp),
specialized variables (u100, v100, lcc, tcc, sst), radiation metrics (ssrd, fdir), and
moisture metrics (tcw, tcwv, tp). This dataset serves as the foundation for the
experimental results presented in Sec. 5.
ResultsAs illustrated in Fig. 2, the synthetic-plus-real paradigm significantly
outperforms the coarse-to-fine baseline across the majority of variables. Notably,
RMSE reductions reach as much as 20% (highlighted by the prominent blue re-
gions).Thesefindingsprovideempiricalevidenceforwhydatatransferworks:
training directly on high-fidelity synthetic data facilitates the learning of more
robust spatial representations than parameter-level fine-tuning on interpolated
inputs. Thus,we adopt the synthetic-plus-real paradigm as our core
methodology for all subsequent stages.
3.3 Theoretical Justification of Synthetic Data Transfer
While including clean data can mitigatemodel collapsein iterative learning
[9,34], the consensus remains that synthetic data generally impairs generaliza-
tion [2]. We challenge this view by demonstrating that an appropriate synthetic

High-Resolution Weather Forecasting via Data Scaling 7
generation procedure can significantly reduce generalization error in linear re-
gression.
Consider a multi-cluster distribution where samples(x, y)are generated via
x=u⊗e k withu∼ N(µk, σ2I)andy=⟨w, x⟩+zwith noisez∼ N(0, γ 2). Let
Da ={(x i, yi)}n i=1 denote the training set. Under assumptions onµk (normal-
ization, orthogonality, and separation) andσ=o(1), we obtain an estimation of
w(denoted asbw) using the standard linear regression model:
bw=

1
n
nX
i=1
xix⊤ i
!−1
1
n
nX
i=1
xiyi
!
.(1)
The following theorem shows the estimation error forbwin Eq. (6).
Theorem 1With a probability≥1−δ, we have
|w−bw| ≤O

γ
r
dm
n log 1 δ
!
.(2)
Suppose that we haveNadditional noisy examplesDb ={(u i, yi)}N i=1 (N≫
n), where eachu i is generated via the same process but lacks its cluster index
ki. Because this key information is latent, we refer toDb as noisy data. The
following theorem indicates that a linear regression model learned directly from
Db will suffer a substantially larger error compared toˆwdefined in Eq. (6).
Theorem 2Letw u ∈R d be the linear regression model we learned fromDb.
AssumeN= +∞. We have
Ek∈[m]Eu∼N(µ k,σ2Id)
h
|⟨u, wu⟩ − ⟨u, wk⟩|2
i
≥σ 2VAR(w1, . . . , wm),(3)
where
VAR(w1, . . . , wm) = Ek∈[m]
h
|wk −E j [wj]|2
i
.(4)
Compared tobwin Eq. (6), we will havebwyields a smaller regression error
thanw u, even whenN→+∞. Our second approach is to learn fromDa a model
to predict the index of Gaussian distribution, and apply the learned prediction
model to augment the input patterns with the predicted index. The following
theorem bounds the recovery error forew.
Theorem 3Assumen≥mdlog N δ . Then, with a probability at least1−δ, we
have
|ew−w| ≤O
 r
dm
N log 1 δ
!
.(5)
Comparing Theorem 3 to Theorem 1, we can see that the solution estimated
from the synthetical datasetDc is significantly closer to the oraclewthan the one
that is learned from the clean datasetDa.This result theoretically validates
the feasibility of employing super-resolution models for robust data
augmentation. Further details and proofs are provided in the supplementary
material.

8 Y. Zhao et al.
4 System Architecture and Training Strategies
4.1 Framework of BaguanHR
As illustrated in Fig. 3, BaguanHR comprises a per-variable super-resolution
generator and a high-resolution forecasting model. To mitigate the scarcity of
0.1◦ EC analysis data, we employ the SR generator to synthesize0.1◦ pseudo-
labels from0.25 ◦ ERA5 data.
Mixed Data
(a) Training Data Composition
ERA5
Swin2SR
Swin2SR
Swin2SR
Per Variable Super Resolution
EC Analysis
(2017-2024)
ERA5-SR data
(2007-2016)
EC Analysis
(b) High Resolution Forecasting
Group 1
Aggregation
Group 2
Aggregation
Group 3
Aggregation
Aggregation ℝ
𝑯
𝒑×𝑾 𝒑×𝑫
𝑿"!∈ℝ𝑽×𝑯×𝑾
𝑿"!’∆"∈ℝ𝑽×𝑯×𝑾
Projection Head
(c) Large Scale I/O Strategy
60TB data
4nodes X 8 A800 GPUs
Large Storage NAS12TB SSD
12TB SSD
12TB SSD
12TB SSD
UTC 00:00 / 12:00
UTC 06:00 / 18:00
Situation 1Situation 2Situation 3Situation 4
Input00:00 (SSD)06:00 (NAS)12:00 (SSD)18:00 (NAS)
Output06:00 (NAS)12:00 (SSD)18:00 (NAS)00:00 (SSD)
(d) Self-adaptive Rollout
Forecasts&
LeadTime
Training Data
Buffer(Queue)
Value: Forecasts, Targets, Lead Times
Pop ratio: stochastic buffer replacement schedule
1.Input: Forecasts 2.Output: Targets
3.Lead-time-aware Loss Weight: W[Lead]
Shift Window MSA
PatchMerging
Multi-head Self-
Attention
×N
Layer Norm
Feed-Forward
Network
Push Pop
Fig.3:Overview of BaguanHR’s architecture. (a) Training Data Composition. (b)
High-resolution forecasting model. (c) Large-scale I/O strategy. (d) Self-adaptive roll-
out strategy.
Per-Variable Super-ResolutionUnlike weather forecasting, which is for-
mulated as a physics-constrained initial value problem, super-resolution em-
phasizes topographic-guided spatial reconstruction. Given that variable-specific
training yields higher fidelity [1,15,35], we adopt Swin2SR [8] to downscale0.25◦
ERA5 data, treating each atmospheric variable independently. Each SR model
is trained on paired 0.25◦–0.1◦ fields using an MAE reconstruction objective.
High-Resolution Forecasting ModelAs illustrated in Fig. 3(b), the fore-
casting model processes inputs through variable-specific tokenization and hier-
archical weather embedding, followed by multiple Swin Transformer blocks [26],
and a linear projection head for spatial restoration.
Variable-Specific Tokenization and Hierarchical Embedding.Given an input of
shapeV×H×W×D, whereVis 80 (tp solely as an output),His 1801
andWis 3600. Then each variable is independently tokenized via patchification
with a patch sizep, resulting in a reshaped tensor ofV×h×w×D(where
h=H/pandw=W/p). However, the “brute-force” cross-attention aggregation
common in prior works [29–31] becomes computationally prohibitive for such

High-Resolution Weather Forecasting via Data Scaling 9
high-resolution atmospheric data. To mitigate this, we propose ahierarchical
weather embedding. By partitioning variables into 12 groups, our model first
distills them into group-specific queries and then fuses them into a global sum-
mary. This two-level aggregation strategy effectively minimizes GPU memory
overhead while streamlining the training process.
Swin Transformer Blocks and Projection Head.The embeddings are processed
by Swin Transformer blocks to facilitate patch interactions. Finally, a linear
projection head (RD×V p2 ) restores the representation to its original spatial di-
mensions.
4.2 Self-Adaptive Rollout Strategy
To mitigate error accumulation in auto-regressive forecasting, recent models [4,
14] have adopted RL-inspired replay buffers for long-range stability. However,
over-emphasizing long-lead horizons often degrades short-term accuracy due to a
forgetting effect. To resolve this, we introduce two strategies for optimized replay
buffer utilization that balance long-range stability with short-term fidelity.
– Lead-Time-AwareLossWeighting:Weemploylead-time-dependentwei-
ghts to ensure short-lead predictions retain sufficient gradient influence.
This prevents long-lead cumulative errors from dominating the optimization,
thereby preserving foundational accuracy and mitigating error propagation
during auto-regression.
– Stochastic Buffer ReplacementTo enhance data diversity, we implement
a randomized buffer update strategy rather than a standard FIFO approach.
Bymaintainingaheterogeneousmixtureofleadtimesperbatch,thismethod
stabilizes distributed training and mitigates the instability typically caused
by small local batch sizes.
4.3 Training and I/O Optimization
We also implement a scalable training framework for BaguanHR, leveraging
advanced I/O partitioning and multi-stage optimization to ensure high-fidelity
forecasting and high-throughput training.
– Training PipelineBaguanHR utilizes 32 NVIDIA A800 GPUs in three
stages: (1)Pretraining, for 250k steps (14 days) on 8-year EC analysis
data; (2)Synthetic Fine-tuning, for 70k steps (4 days) incorporating 10-
year super-resolution data; and (3)Rollout Training, for 2 days with a
self-adaptive replay buffer to suppress long-range error accumulation.
– I/O StrategiesTo address the I/O bottleneck caused by 32-bit data files of
4–5 GB each, weachieve a4×speedupvia: (1)Data Partitioning, sharding
data across local 12 TB SSDs per node; (2)Hybrid Storage, caching UTC
00:00/12:00 data on SSDs while keeping 06:00/18:00 data on NAS.
Overall, the training pipeline takes about 20 days on 32 NVIDIA A800 GPUs
and uses about 60 TB of storage for 18 years of 0.1◦ synthetic-plus-real data;
detailed compute and I/O costs are provided in Supplementary Sec. C.4.

10 Y. Zhao et al.
5 Experiments
5.1 Dataset & Metrics
Detailed data descriptions are provided in Sec. 3.2. We adopt the standard
weatherevaluationmethodologyoutlinedinWeatherBench[33],focusingonfore-
casts initialized at 00/12 UTC for the year 2025. We use weighted Root Mean
Square Error (RMSE) and weighted Anomaly Correlation Coefficient (ACC),
which have also been widely used in AI-based weather models [3,6,22,31], as
our main metrics.
5.2 The Scaling of Data Volume
Fig. 4 reveals consistent power-law-like improvements in forecast skill as the
volume of training data increases. This confirms the pivotal role of data scaling
in ML-based weather models. Beyond this overall trend, we observe:
5 10 20 40
Data Range (Years)
0.68
0.70
0.72
0.74
0.76
0.78t2m RMSE
6h - t2m
Actual Data
Per-variable SR Data
Full-variable SR Data
Fit Curve
Extrapolation
5 10 20 40
Data Range (Years)
0.70
0.72
0.74
0.76
0.78
0.80
0.82
0.84u10 RMSE
6h - u10
Actual Data
Per-variable SR Data
Full-variable SR Data
Fit Curve
Extrapolation
5 10 20 40
Data Range (Years)
34
36
38
40
42
44
46
48msl RMSE
6h - msl
Actual Data
Per-variable SR Data
Full-variable SR Data
Fit Curve
Extrapolation
5 10 20 40
Data Range (Years)
18
20
22
24
26
28
30z500 RMSE
6h - z500
Actual Data
Per-variable SR Data
Full-variable SR Data
Fit Curve
Extrapolation
5 10 20 40
Data Range (Years)
1.2
1.3
1.4
1.5t2m RMSE
72h - t2m
Actual Data
Per-variable SR Data
Full-variable SR Data
Fit Curve
Extrapolation
5 10 20 40
Data Range (Years)
1.6
1.7
1.8
1.9
2.0
2.1u10 RMSE
72h - u10
Actual Data
Per-variable SR Data
Full-variable SR Data
Fit Curve
Extrapolation
5 10 20 40
Data Range (Years)
120
140
160
180
200msl RMSE
72h - msl
Actual Data
Per-variable SR Data
Full-variable SR Data
Fit Curve
Extrapolation
5 10 20 40
Data Range (Years)
120
140
160
180
200z500 RMSE
72h - z500
Actual Data
Per-variable SR Data
Full-variable SR Data
Fit Curve
Extrapolation
5 10 20 40
Data Range (Years)
1.6
1.7
1.8
1.9
2.0t2m RMSE
120h - t2m
Actual Data
Per-variable SR Data
Full-variable SR Data
Fit Curve
Extrapolation
5 10 20 40
Data Range (Years)
2.5
2.6
2.7
2.8
2.9
3.0
3.1u10 RMSE
120h - u10
Actual Data
Per-variable SR Data
Full-variable SR Data
Fit Curve
Extrapolation
5 10 20 40
Data Range (Years)
280
300
320
340
360
380msl RMSE
120h - msl
Actual Data
Per-variable SR Data
Full-variable SR Data
Fit Curve
Extrapolation
5 10 20 40
Data Range (Years)
260
280
300
320
340
360
380
400z500 RMSE
120h - z500
Actual Data
Per-variable SR Data
Full-variable SR Data
Fit Curve
Extrapolation
Fig.4:Scaling law curves for different variables and lead times. Different subplots
correspond to different variables and forecasting horizons. We plot thex-axis in log
scale to reflect the scaling law.
1.Scaling Consistency Across Lead Times:The power-law behavior of er-
ror reduction remains remarkably stable across different forecast lead times.
Thisconsistentscalingslopesuggeststhatincreasingdatavolumeisauniver-
sally robust strategy for improving both short-term deterministic and long-
term atmospheric predictions. Notably, for long-term forecasting, RMSE is
reduced by4.6%at 72 hours and4.9%at 120 hours.

High-Resolution Weather Forecasting via Data Scaling 11
2.Theoretical Saturation and Diminishing Returns:To provide practi-
cal guidance for large-scale training, we conducted an extrapolation analysis
beyond the 18-year data threshold. While the full 47-year ERA5 archive
could be leveraged for data augmentation via SR, this extrapolation should
be interpreted as a trend analysis rather than a definitive performance esti-
mate. The fitted curves suggest that marginal performance gains may grad-
ually diminish beyond 18 years, indicating a practical trade-off where fur-
ther data expansion yields sub-linear improvements relative to the increasing
storage and I/O cost.
3.Variable-Specific Sensitivity to Data Volume:Sensitivity to data scal-
ingvariessignificantlybyphysicalfield:whilemostvariables(e.g.,z500,t2m)
plateau early, others like msl exhibit sustained headroom for improvement.
This heterogeneity informs our decision to standardize on an 18-year period
to optimize overall storage and I/O efficiency.
4.Efficacy of Granular Data Augmentation:Comparative analysis shows
that models trained on data generated by per-variable SR outperform those
trained on full-variable SR output at a 10-year scale. This advantage is par-
ticularly pronounced for surface variables (e.g., t2m), highlighting the value
of decoupled strategies in data synthesis.
5.3 Performance Evaluation and Benchmarking
To evaluate the model’s efficacy, we adopt a dual-perspective approach: first,
a holistic global assessment across multiple variables to establish baseline pre-
dictive skill, followed by a rigorous investigation into model robustness under
diverse extreme scenarios.
General Comparison of VariablesTo show the superiority of BaguanHR, we
evaluate it against both physics-based and ML-based baselines. IFS-HRES [10]
serves as the operational physics-based 0.1◦ reference. For ML baselines, we use
Baguan+swin2sr as the primary comparison, where 0.25◦ Baguan forecasts are
adapted to the 0.1◦ grid using Swin2SR. Since the first 3-day forecast is more
accurate, directly actionable, and therefore especially important, we further in-
clude GraphCast+swin2sr, Pangu+swin2sr, and Baguan+GHR for short-term
lead times. As Fengwu-GHR [14] cannot be directly replicated, Baguan+GHR is
re-implemented based on Baguan [31] as a coarse-to-fine high-resolution adap-
tation baseline.
BaguanHR surpasses the baselines (Fig. 5), improving over85%of lead
times within 72 hours and reducing RMSE by4.0%compared to IFS-HRES.
Specifically, BaguanHR achieves an average RMSE reduction of5.8%at 24
hours and9.7%at 72 hours relative to the IFS-HRES baseline. Furthermore,
BaguanHR demonstrates a clear performance edge over 0.25°outputs upscaled
via Swin2SR [8], particularly in short-range windows. While auto-regressive sys-
tems often suffer from variance loss and converge toward the ensemble mean
over time, post-processing techniques are inherently limited by the informa-
tion bottleneck of coarse-grained inputs. In contrast,BaguanHR’s end-to-end

12 Y. Zhao et al.
1.0
1.5
2.0
2.5
RMSE
T2M (K)
24 48 720.6
0.8
1.0
1.2
1
2
3
4
U10 (m/s)
24 48 72
1.0
1.5
1
2
3
4
5
V10 (m/s)
24 48 72
1.0
1.5
0
200
400
600
MSL (Pa)
24 48 72
50
100
150
1
2
3
RMSE
T850 (K)
24 48 72
0.5
1.0
0.0005
0.0010
0.0015
0.0020
Q850 (kg/kg)
24 48 72
0.0005
0.0010
0.0015
0
200
400
600
800
Z500 (m2/s2)
24 48
25
50
75
0
200
400
600
800
SP (Pa)
24 48 720
200
400
0.5
0.6
0.7
0.8
0.9
ACC
T2M (K)
24 48 72
0.900
0.925
0.950
0.975
0.4
0.5
0.6
0.7
0.8
0.9
1.0
U10 (m/s)
24 48 72
0.900
0.925
0.950
0.975
0.4
0.5
0.6
0.7
0.8
0.9
1.0
V10 (m/s)
24 48 72
0.900
0.925
0.950
0.975
0.5
0.6
0.7
0.8
0.9
1.0
MSL (Pa)
24 48 72
0.98
0.99
1.00
0 48 96 144 192 240
Lead time (h)
0.5
0.6
0.7
0.8
0.9
1.0
ACC
T850 (K)
24 48 72
0.94
0.96
0.98
0 48 96 144 192 240
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Q850 (kg/kg)
24 48 72
0.8
0.9
0 48 96 144 192 240
Lead time (h)
0.6
0.7
0.8
0.9
1.0
Z500 (m2/s2)
24 48
0.996
0.998
1.000
0 48 96 144 192 240
Lead time (h)
0.4
0.5
0.6
0.7
0.8
0.9
1.0
SP (Pa)
24 48 72
0.8
0.9
1.0
Lead time h)
Fig.5:Overall performance of BaguanHR against several baselines. ‘Baguan+GHR’
denotes the version replicated from [14]. We zoom in the first 72 hours for better
comparison among different methods.
high-resolution framework circumvents these limitations by capturing
fine-grained dynamics natively, yielding a more physically consistent and
detailed atmospheric representation.
Predictive Skill in Extreme ScenariosTo evaluate BaguanHR’s reliability
in high-impact scenarios, we assess its performance across three categories of
extremes: categorical detection of intense moisture events, predictive accuracy
for both relative (percentile-based) and absolute (threshold-based) extremes.
1 2 3 4 5 6 7 8 9 10
Lead Time (days)
0.20
0.25
0.30
0.35
0.40Q850 TS
(a) Categorical Extremes
1 2 3 4 5 6 7 8 9 10
Lead Time (days)
0.75
1.00
1.25
1.50
1.75
2.00
2.25
2.50T2M RMSE
(b) Percentile-based Extremes (hot)
1 2 3 4 5 6 7 8 9 10
Lead Time (days)
1.0
1.5
2.0
2.5
3.0
3.5T2M RMSE
(c) Percentile-based Extremes (cold)
1 2 3 4 5 6 7 8 9 10
Lead Time (days)
10
20
30
40
50
60Z850 RMSE
(d) Threshold-based Extremes
BG-HR Baguan+swin2sr IFS-HRES
Fig.6:Extreme event verification. Higher TS represents better categorical skill; lower
RMSE signifies enhanced accuracy for percentile and threshold-based extremes.

High-Resolution Weather Forecasting via Data Scaling 13
Categorical Extreme Event Detection.Usingq850≥14g/kgasathermodynamic
proxy for heavy precipitation [17], we evaluate detection skill via the Threat
Score(TS;Fig.6(a)).BaguanHRconsistentlyoutperformsbothBaguan+swin2sr
and IFS-HRES, achieving gains exceeding 10% in most cases. This confirms its
superior ability to resolve the intense moisture convergence required for high-
impact events.
Percentile-based Relative Extremes.To identify statistical anomalies across lati-
tudes, we define extreme heat and cold using the local 90th and 10th percentiles
of t2m [40] (Fig. 6(b–c)). BaguanHR outperforms competitors in more than 70%
of cases, surpassing Baguan+swin2sr by 15% in the short term and maintaining
a 3% edge in long-term extremes. This highlights its precision in capturing the
“heavy-tail” thermal distributions often smoothed by lower-resolution models.
Threshold-based Absolute Extremes.To evaluate dynamical intensity, we identify
mid-latitude low-pressure systems using an absolute threshold (z850<13,500
m2/s2) [18] (Fig. 6(d)). BaguanHR delivers the best results, outperforming IFS-
HRES by over 30% and maintaining a significant lead over Baguan+swin2sr at
both short (1–2 days) and long (9–10 days) lead times. These results demonstrate
its capacity to reconstruct the sharp pressure gradients of severe storms.
5.4 Controlled Comparisons
We perform controlled comparisons to justify the core components of BaguanHR
across four dimensions: variable modeling (independent vs. joint), physical con-
sistency of SR fields, power spectral analysis, and optimization stability (replay
buffer and adaptive weighting).
Full-Variable vs. Per-Variable Super-ResolutionFig. 7 (a) shows the
RMSE improvement of per-variable SR over full-variable SR across variables. It
shows that per-variable SR significantly improves surface variables (e.g., 90.7%
for sp, >20% for t2m and msl) by capturing local specificities. Upper-air fields
achieve modest improvements (1.6%–4.7% for temperature and geopotential).
Thissuggeststhatunlikeforecasting,SRfavorsintra-variabletexturesovercross-
variable coupling, making variable-independent modeling more effective.
Physical Consistency of SR FieldsWe diagnose the physical consistency
of SR-generated pseudo-labels using three diagnostics based on relative humidity
(RH), geostrophic wind speed|V g|, and potential temperature differences∆θ.
Their latitude-weighted correlations against the 0.1◦ analysis remain high across
pressure levels (RH≥0.94,|V g| ≥0.82,∆θ≥0.93), indicating that per-
variable SR preserves key moisture, dynamical, and thermodynamic structures,
alleviating concerns about physically inconsistent high-frequency artifacts. Per-
level numbers and the power-spectrum analysis are in Supplementary Sec. E.3.
Power Spectral AnalysisWe compute power spectral density (PSD; vari-
ance/energy as a function of spatial wavelength) for 6–72h forecasts over the full
2025 validation dataset; EC analysis denotes the corresponding year-mean PSD

14 Y. Zhao et al.
5
 0 5 10 15 20 25
RMSE Improvement by Variable (%)
t2m
u10
v10
msl
tp6h
sp
tcc
tcwv
t_500
z_500
u_500
q_500
t_850
q_850
23.9%
10.7%
9.9%
23.8%
1.2%
90.7%
2.2%
8.0%
4.7%
2.0%
0%
-1.1%
1.7%
-2.5% Surface Variables Pressure Level Variables
500 200 100 50 20
Wavelength (km)
106
107
108
109
1010
Power Spectral Density of t2m
BaguanHR
Baguan+swin2sr
EC Analysis
500 200 100 50 20
Wavelength (km)
105
106
107
108
109
1010
Power Spectral Density of u10
BaguanHR
Baguan+swin2sr
EC Analysis
(a) (b) (c)
Fig.7:(a) Relative RMSE improvement of per-variable versus full-variable super-
resolution. (b-c) Power spectral analysis of t2m and u10.
of analysis data. The results in Fig. 7 (b-c) demonstrate that BaguanHR main-
tains higher short-wavelength spectral power, effectively preserving mesoscale
structures. Conversely, the Baguan+swin2sr pipeline exhibits systematic energy
attenuation, suggesting that post-hoc SR tends to smooth fields rather than
recovering fine-scale variability from coarse inputs.
Self-Adaptive Rollout StrategyTab. 1 validates our enhanced replay
buffer strategy. Loss weighting suppresses auto-regressive error propagation, as
its removal leads to degraded performance on long-range forecasts. Stochastic re-
placement further boosts performance by ensuring lead-time diversity. Together,
BaguanHR harmonizes divergent loss magnitudes across horizons, ensuring sta-
ble optimization and superior metrics across all variables.
Table 1:Performance comparison of different strategies on replay buffer.
Methods T2M-72h U10-72h MSL-72h TCC-72h RMSE↓ACC↑ RMSE↓ACC↑ RMSE↓ACC↑ RMSE↓ACC↑
w/o Random & loss weight 1.12 0.90 1.64 0.91 147.80 0.980 0.289 0.61
w/o Random 1.12 0.91 1.63 0.91 147.41 0.980 0.288 0.62
w/o loss weight 1.11 0.91 1.63 0.92 145.32 0.981 0.289 0.62
BaguanHR 1.09 0.92 1.62 0.92 144.57 0.981 0.287 0.64
5.5 Case Studies
The aforementioned capabilities of BaguanHR are further demonstrated through
the case studies of tropical cyclone and cold-air outbreak prediction.
Tropical Cyclone PredictionTropical cyclones are among Earth’s most
hazardous weather events. While prior ML methods typically lag behind the
IFS-HRES in intensity [3,4], BaguanHR achieves comparable intensity while
maintaining superior track accuracy. For the double-landfall cyclone CO-MAY,
BaguanHR precisely identifies two landfall sites, outperforming the IFS-HRES
track (Fig. 8(a)). Furthermore, as shown in Fig. 8(b), BaguanHR substantially
outperforms Baguan+swin2sr in both intensity and track errors.

High-Resolution Weather Forecasting via Data Scaling 15
120°E 124°E 128°E 132°E
26°N
28°N
30°N
32°N
Initialization time: 12 UTC 27 July 2025
BaguanHR
IFS-HRES
Baguan+swin2sr
IBTrACS
1st landfall
2nd landfall
3
4
5
6
Maximum 10-m Wind
RMSE (m s 1)
12 24 36 48 60 72
Lead time (hours)
0
100
200
300Track RMSE (km)
92°W 88°W 84°W 80°W 76°W
42°N
44°N
46°N
48°N
BaguanHR
92°W 88°W 84°W 80°W 76°W
Baguan+swin2sr
92°W 88°W 84°W 80°W 76°W
EC Analysis
92°W 88°W 84°W 80°W 76°W
42°N
44°N
46°N
48°N
T: BaguanHR  EC
92°W 88°W 84°W 80°W 76°W
T: Baguan+swin2sr  EC
30
 25
 20
 15
 10
T emperature (°C)
5
0
5
T (°C)
(a) Typhoon CO-MAY Track Forecast
BaguanHR
 IFS-HRES
 Baguan+swin2sr
(b) Typhoon CO-MAY Forecast Errors (c) 2m Temperature Forecast & Difference Maps
RMSE(BaguanHR, EC) = 1.774 °C    RMSE(Baguan+swin2sr, EC) = 2.543 °C
Fig.8:(a) Typhoon CO-MAY tracking forecast, which is initialized at 12 UTC, 27
July 2025. (b) Forecast errors of track and intensity. (c) Case study of 2m temperature
forecast over the U.S. Great Lakes region, initialized at 00 UTC, 20 January 2025.
Cold-Air OutbreakFig. 8(c) presents a 2m temperature (t2m) forecast
case study in a cold-air outbreak over the U.S. Great Lakes region. BaguanHR
successfully captures the spatial structure characteristics, e.g., the distinct tem-
perature characteristics over lake surfaces compared to surrounding land areas,
a level of physical detail that the post-hoc Baguan+swin2sr baseline fails to
resolve, demonstrating its superior performance in extreme value prediction.
6 Conclusion
In this paper, we present BaguanHR, a0.1◦ global weather forecasting model
builtonadata-transferframeworkthatleveragessuper-resolution-generatedsyn-
thetic data. We demonstrate fundamental data scaling laws in high-resolution
forecasting, showing that model performance follows a power-law improvement
with training data volume. Using synthetic0.1◦ data, BaguanHR achieves su-
perior performance across nearly all variables, especially in the first 72 hours,
outperforming both IFS-HRES and SR-enhanced0.25 ◦ models. At 10–15 day
lead times, BaguanHR brings limited gains as forecasts are increasingly con-
trolled by large-scale atmospheric patterns and fine-scale details become weakly
predictable. Building on Baguan, we are developing the NJU-Earth series as an
evolving model family for global weather forecasting, with BaguanHR as its high-
resolution component. This work will be extended toward ensemble forecasting
and operational applications such as tropical cyclone intensity prediction.
Acknowledgements
This work was supported by the National Natural Science Foundation of China
(U2342218), the Fundamental and Interdisciplinary Disciplines Breakthrough
Plan of the Ministry of Education of China (JYB2025XDXM907), the DAMO
Academy Research Intern Program, and the High Performance Computing Cen-
ter, Nanjing University (NJU).

16 Y. Zhao et al.
References
1. Addison, H., Kendon, E., Ravuri, S., Aitchison, L., Watson, P.A.: Machine learning
emulationofalocal-scaleukclimatemodel.arXivpreprintarXiv:2211.16116(2022)
2. Amin, K., Bie, A., Kong, W., Syed, U., Vassilvitskii, S.: Learning from synthetic
data: Limitations of erm (2026),https://arxiv.org/abs/2601.15468
3. Bi, K., Xie, L., Zhang, H., Chen, X., Gu, X., Tian, Q.: Accurate medium-range
global weather forecasting with 3d neural networks. Nature619(7970), 533–538
(2023)
4. Bodnar, C., Bruinsma, W.P., Lucic, A., Stanley, M., Allen, A., Brandstetter, J.,
Garvan, P., Riechert, M., Weyn, J.A., Dong, H., Gupta, J.K., Thambiratnam, K.,
Archibald, A.T., Wu, C.C., Heider, E., Welling, M., Turner, R.E., Perdikaris, P.: A
foundation model for the earth system. Nature641(8065), 1180–1187 (May 2025).
https://doi.org/10.1038/s41586-025-09005-y
5. Chen, K., Han, T., Gong, J., Bai, L., Ling, F., Luo, J., Chen, X., Ma, L., Zhang, T.,
Su, R., Ci, Y., Li, B., Yang, X., Ouyang, W.: The operational medium-range deter-
ministic weather forecasting can be extended beyond a 10-day lead time. Commu-
nications Earth & Environment (2025).https://doi.org/10.1038/s43247-025-
02502-y
6. Chen, L., Zhong, X., Zhang, F., Cheng, Y., Xu, Y., Qi, Y., Li, H.: Fuxi: a cascade
machinelearningforecastingsystemfor15-dayglobalweatherforecast.npjClimate
and Atmospheric Science6(1), 190 (2023).https://doi.org/10.1038/s41612-
023-00512-1
7. Cherti, M., Beaumont, R., Wightman, R., Wortsman, M., Ilharco, G., Gordon, C.,
Schuhmann, C., Schmidt, L., Jitsev, J.: Reproducible scaling laws for contrastive
language-image learning. In: Proceedings of the IEEE/CVF conference on com-
puter vision and pattern recognition. pp. 2818–2829 (2023)
8. Conde, M.V., Choi, U.J., Burchi, M., Timofte, R.: Swin2sr: Swinv2 transformer
for compressed image super-resolution and restoration. In: European Conference
on Computer Vision. pp. 669–687. Springer (2022)
9. Dey, A., Donoho, D.: Universality of theπ2/6pathway in avoiding model collapse
(2024),https://arxiv.org/abs/2410.22812
10. European Centre for Medium-Range Weather Forecasts: ECMWF Integrated Fore-
casting System (IFS) High Resolution (HRES) Forecasts.https://www.ecmwf.
int/(2024), accessed: 2025-01-01
11. Gahtan, J., Knapp, K.R., Schreck, C.J.I., Diamond, H.J., Kossin, J.P., Kruk, M.C.:
International best track archive for climate stewardship (ibtracs) project, version
4.01 (2024).https://doi.org/10.25921/82ty-9e16, western North Pacific and
North Atlantic subset. NOAA National Centers for Environmental Information.
2026-03-12.
12. Gerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., Sleight, H., Hughes, J., Kor-
bak, T., Agrawal, R., Pai, D., Gromov, A., Roberts, D.A., Yang, D., Donoho, D.L.,
Koyejo, S.: Is model collapse inevitable? breaking the curse of recursion by accu-
mulating real and synthetic data (2024),https://arxiv.org/abs/2404.01413
13. Guen, V.L., Thome, N.: Disentangling physical dynamics from unknown factors
for unsupervised video prediction. In: Proceedings of the IEEE/CVF conference
on computer vision and pattern recognition. pp. 11474–11484 (2020)
14. Han,T.,Guo,S.,Ling,F.,Chen,K.,Gong,J.,Luo,J.,Gu,J.,Dai,K.,Ouyang,W.,
Bai, L.: Fengwu-ghr: Learning the kilometer-scale medium-range global weather
forecasting. arXiv preprint arXiv:2402.00059 (2024)

High-Resolution Weather Forecasting via Data Scaling 17
15. Harris, L., McRae, A.T., Chantry, M., Dueben, P.D., Palmer, T.N.: A generative
deeplearningapproachtostochasticdownscalingofprecipitationforecasts.Journal
of Advances in Modeling Earth Systems14(10), e2022MS003120 (2022)
16. Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A., Muñoz-Sabater, J.,
Nicolas, J., Peubey, C., Radu, R., Schepers, D., et al.: The era5 global reanalysis.
Quarterly Journal of the Royal Meteorological Society146(730), 1999–2049 (2020)
17. Holton, J.R., Hakim, G.J.: An introduction to dynamic meteorology, vol. 88. Aca-
demic press (2013)
18. Hoskins, B.J., McIntyre, M.E., Robertson, A.W.: On the use and significance of
isentropic potential vorticity maps. Quarterly Journal of the Royal Meteorological
Society111(470), 877–946 (1985)
19. Kaplan, J., McCandlish, S., Henighan, T., Brown, T.B., Chess, B., Child, R., Gray,
S., Radford, A., Wu, J., Amodei, D.: Scaling laws for neural language models. arXiv
preprint arXiv:2001.08361 (2020)
20. Knapp, K.R., Kruk, M.C., Levinson, D.H., Diamond, H.J., Neumann, C.J.: The
international best track archive for climate stewardship (ibtracs) unifying tropi-
cal cyclone data. Bulletin of the American Meteorological Society91(3), 363–376
(2010)
21. Kurth, T., Subramanian, S., Harrington, P., Pathak, J., Mardani, M., Hall, D.,
Miele, A., Kashinath, K., Anandkumar, A.: Fourcastnet: Accelerating global high-
resolution weather forecasting using adaptive fourier neural operators. In: Huebl,
A., Silvano, C., Robinson, T. (eds.) Proceedings of the Platform for Advanced
Scientific Computing Conference, PASC 2023, Davos, Switzerland, June 26-28,
2023. pp. 13:1–13:11. ACM (2023).https://doi.org/10.1145/3592979.3593412
22. Lam, R., Sanchez-Gonzalez, A., Willson, M., Wirnsberger, P., Fortunato, M., Alet,
F.,Ravuri,S.,Ewalds,T.,Eaton-Rosen,Z.,Hu,W.,Merose,A.,Hoyer,S.,Holland,
G., Vinyals, O., Stott, J., Pritzel, A., Mohamed, S., Battaglia, P.: Learning skillful
medium-range global weather forecasting. Science382(6677), 1416–1421 (2023).
https://doi.org/10.1126/science.adi2336
23. Lamprecht, C.S.: Meteostat python, software package
24. Lang, S., Alexe, M., Chantry, M., Dramsch, J., Pinault, F., Raoult, B., Clare,
M.C.A., Lessig, C., Maier-Gerber, M., Magnusson, L., Bouallègue, Z.B., Nemesio,
A.P., Dueben, P.D., Brown, A., Pappenberger, F., Rabier, F.: Aifs – ecmwf’s data-
driven forecasting system (2024),https://arxiv.org/abs/2406.01465
25. Li, Z., Kovachki, N.B., Azizzadenesheli, K., Liu, B., Bhattacharya, K., Stuart,
A.M., Anandkumar, A.: Fourier neural operator for parametric partial differential
equations. In: 9th International Conference on Learning Representations, ICLR
2021, Virtual Event, Austria, May 3-7, 2021. OpenReview.net (2021),https://
openreview.net/forum?id=c8P9NQVtmnO, accessed: 2026-06-28
26. Liu, Z., Lin, Y., Cao, Y., Hu, H., Wei, Y., Zhang, Z., Lin, S., Guo, B.: Swin
transformer:Hierarchical visiontransformerusingshiftedwindows.In:Proceedings
of the IEEE/CVF International Conference on Computer Vision (ICCV) (2021)
27. Malardel, S., Wedi, N., Deconinck, W., Diamantakis, M., Kühnlein, C., Mozdzyn-
ski, G., Hamrud, M., Smolarkiewicz, P.: A new grid for the ifs. ECMWF newsletter
146(23-28), 321 (2016)
28. Mardani, M., Brenowitz, N., Cohen, Y., Pathak, J., Chen, C.Y., Liu, C.C., Vahdat,
A., Kashinath, K., Kautz, J., Pritchard, M.: Generative residual diffusion modeling
for km-scale atmospheric downscaling. arXiv preprint arXiv:2309.1521410(2023)
29. Nguyen, T., Brandstetter, J., Kapoor, A., Gupta, J.K., Grover, A.: Climax: A
foundationmodelforweatherandclimate.In:InternationalConferenceonMachine
Learning (2023),https://api.semanticscholar.org/CorpusID:256231457

18 Y. Zhao et al.
30. Nguyen, T., Shah, R., Bansal, H., Arcomano, T., Madireddy, S., Maulik, R., Ko-
tamarthi, V.R., Foster, I.T., Grover, A.: Scaling transformer neural networks for
skillful and reliable medium-range weather forecasting. Advances in Neural Infor-
mation Processing Systems37, 13689–13723 (2024)
31. Niu, P., Ma, Z., Zhou, T., Chen, W., Shen, L., Jin, R., Sun, L.: Utilizing strategic
pre-training to reduce overfitting: Baguan-a pre-trained weather forecasting model.
In: Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery
and Data Mining V. 2. pp. 2186–2197 (2025)
32. Raoult, B., Pinault, F., Mertes, G., Dramsch, J.S., Cook, H., Chantry, M.: ai-
models,https://github.com/ecmwf-lab/ai-models, accessed: 2026-06-28
33. Rasp, S., Hoyer, S., Merose, A., Langmore, I., Battaglia, P., Russel, T., Sanchez-
Gonzalez, A., Yang, V., Carver, R., Agrawal, S., Chantry, M., Bouallegue, Z.B.,
Dueben, P., Bromberg, C., Sisk, J., Barrington, L., Bell, A., Sha, F.: Weatherbench
2: A benchmark for the next generation of data-driven global weather models
(2024),https://arxiv.org/abs/2308.15560
34. Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., Gal, Y.: Ai
models collapse when trained on recursively generated data. Nature631, 755–759
(2024)
35. Vandal, T., Kodra, E., Ganguly, S., Michaelis, A., Nemani, R., Ganguly, A.R.:
Deepsd: Generating high resolution climate change projections through single im-
age super-resolution. In: Proceedings of the 23rd acm sigkdd international confer-
ence on knowledge discovery and data mining. pp. 1663–1672 (2017)
36. Wang, C., Berner, J., Li, Z., Zhou, D., Wang, J., Bae, J., Anandkumar, A.: Coarse
graining with neural operators for simulating chaotic systems. arXiv preprint
arXiv:2408.05177 (2024)
37. Yu, Y., Huang, L., Calotoiu, A., Hoefler, T.: Scaling laws of global weather models
(2026),https://arxiv.org/abs/2602.22962
38. Zhai, X., Kolesnikov, A., Houlsby, N., Beyer, L.: Scaling vision transformers. In:
Proceedings of the IEEE/CVF conference on computer vision and pattern recog-
nition. pp. 12104–12113 (2022)
39. Zhang, F., Sun, Y.Q., Magnusson, L., Buizza, R., Lin, S.J., Chen, J.H., Emanuel,
K.: What is the predictability limit of midlatitude weather? Journal of the Atmo-
spheric Sciences76(4), 1077–1091 (2019)
40. Zhang, X., Alexander, L., Hegerl, G.C., Jones, P., Tank, A.K., Peterson, T.C.,
Trewin, B., Zwiers, F.W.: Indices for monitoring changes in extremes based on
dailytemperatureandprecipitationdata.WileyInterdisciplinaryReviews:Climate
Change2(6), 851–870 (2011)

High-Resolution Weather Forecasting via Data Scaling 19
Supplementary Material
A Theoretical Justification of Synthetic Data Transfer
A.1 Introduction
People have observed the phenomenon of model collapse when training a LM
from iteratively generated data [34]. Later studies [9,12] showed that model
collapse will not take place if we can ensure that the clean data is always included
ineveryiterationoftraining.However,itisoverallaconsensusthatlearningfrom
synthetic data will result in worse generalization error compared to learning from
the clean data [2,9,12]. In this note, we will show that this is not always the case.
We demonstrate that with appropriate procedure of generating synthetic data,
we are able to significantly reduce the generalization error for linear regression.
We note that our study is different from [12] where the introduction of synthetic
data is resulted in an increase in variance and therefore a worse regression error.
In our study, we focused on the case of synthetic data where a simple model is
learned to predict additional features that lead to a better prediction model.
A.2 Analysis
We first describe the data generation process. To create an input patternx, we
first choose an indexk∈[m]from1tomuniformly at random, and sample
u∈R d thekth Gaussian distributionN(µ k, σ2Id). Then, the final input pattern
x∈R md is computed asx=u⊗e k, wheree k ∈ {0,1}m is a one-hot vector with
itskth element being1. Finally, the corresponding output valueyis given asy=
⟨u, wk⟩+z=⟨w, x⟩+z, wherew= (w ⊤ 1 , . . . , w⊤ m)⊤ ∈R md andz∼ N(0, γ2). Let
Da ={(x i, yi), i= 1, . . . , n}be the set of training examples that are generated
by the above procedure. For the convenience of our analysis, we assume that (a)
|µk|=
√
d,∀k∈[m], (b) 1 m Pm k=1 µkµ⊤ k =I, (c)min j̸=k |µk −µ j|=Ω( √ d)and (d)
σ=o(1).
Using the standard regression model, we obtain an estimation ofw, denoted
asbw, i.e
bw=

1
n
nX
i=1
xix⊤ i
!−1
1
n
nX
i=1
xiyi
!
(6)
The following theorem shows the estimation error forbwin (6).
Theorem 4With a probability at least1−δ, we have
|w−bw| ≤O

γ
r
dm
n log 1 δ
!

20 Y. Zhao et al.
We skip its proof as it is standard to obtain the above bound using the concen-
tration inequality.
Next, we assume that we have additionalNnoisy training examplesD b =
{(ui, yi)}N i=1, whereN≫nandu i ∈R d. Each training example(ui, yi)inD b
is generated by the same procedure as described above, but onlyu i (thed-
dimensional vector sampled from the selected Gaussian distribution) is saved,
and the corresponding index information—i.e., which Gaussian is used for sam-
plingu i—is missing. Because of the lost information, we refer to examples inDb
as noisy training examples. For convenience, we denote byik the index of the
Gaussian distribution used to generateui. As indicated by the theorem below,
a linear regression model directly learned fromDb yields a significantly larger
regression error thanbwin (6).
Theorem 5Letw u ∈R d be the linear regression model we learned fromDb.
AssumeN= +∞. We have
Ek∈[m]Eu∼N(µ k,σ2Id)
h
|⟨u, wu⟩ − ⟨u, wk⟩|2
i
≥σ 2VAR(w1, . . . , wm)
where
VAR(w1, . . . , wm) = Ek∈[m]
h
|wk −E j [wj]|2
i
Proof.Given thatNis infinite large, we can replace the average in the expression
of linear regression with expectation, leading to the following expression forwu
wu =

E[uiu⊤ i ] −1 E[uiyi] = 1 (1 +σ2)m mX k=1 µkµ⊤ k wk
We then compute the expected regression error, i.e.
E
h
(⟨ui, wu⟩ − ⟨ui, wik ⟩)2
i
=E
h
(⟨ui, wu −w ik ⟩)2
i
= 1 m
mX
k=1

σ2∥wu −w k∥2 +

⟨µk, wu −w k⟩

2
≥ σ2
m
mX
k=1
∥wu −w k∥2
≥ σ2
m
mX
k=1
 wk − 1 m mX j=1 wj  2
=σ 2 V AR(w1, . . . , wm).
Compared tobwin (6), whose regression error is given by
E
h
|⟨xi,bw−w⟩| 2
i
≤O
 γ2dm
n log 1 δ 

High-Resolution Weather Forecasting via Data Scaling 21
Thus, when
n≥Ω
 γ2dm
σ2VAR(w1, . . . , wm) log 1 δ 
we will havebwyields a smaller regression error thanwu, even whenN→+∞.
Our second approach is to learn fromDa a model to predict the index of
Gaussian distribution, and apply the learned prediction model to augment the
input patterns with the predicted index. To this end, we will simply estimate the
center of each Gaussian distribution by averaging the input patterns assigned
with the same index, i.e.
bµk =
Pn
i=1 I(|M kxi|>0)M kxiPn
i=1 I(|M kxi⟩|>0) ,∀k∈[m](7)
where
Mk =

 0d×d, . . . ,0d×d| {z }
k−1zero matrices
, Id,0 d×d, . . . ,0d×d| {z }
m−kzero matrices

 (8)
Using the mean vectorsbµk, k∈[m]estimated from dataD a, we will find the
index of Gaussian distribution for each training examples(u i, yi)∈ D b, i=
1, . . . , Nas follows
ˆki = arg min
j∈[m]
|ui −bµj|(9)
Finally, for each training example(ui, yi)∈ Db, we construct a new input pattern
exi =u i ⊗e ˆki , and learn a linear regression modelewfrom the training examples Dc ={(exi, yi), i= 1, . . . , N}. The following theorem bounds the recovery error
forew.
Theorem 6Assume
n≥mdlog N δ
Then, with a probability at least1−δ, we have
|ew−w| ≤O
 r
md
N log 1 δ
!
Comparing Theorem 3 to Theorem 1, we can see that the solution estimated the
synthetical datasetD c is significantly closer to the oraclewthan the one that is
learned from the clean datasetDa.
A.3 Proof of Theorem 3
Proof.First, sincex i =u i ⊗e ki, we have|Mkxi|>0if and only ifk=k i. Hence,
the expression forbµk in (7) computes the average ofui ∈R d fromD a that are

22 Y. Zhao et al.
sampled from thekth Gaussian distributionN(µ k, σ2Id). We denote bymk the
number of training examples inDa that are sampled fromN(µ k, σ2Id). Using
the chernoff bound, it is easy to show that, with a probability at least1−δ, for
anyk∈[m], we have

mk − n m

 ≤O  n m log m δ 
Thus, whenn≥Ω(mlog(m/δ)), we have
mk ≥Ω
 n
m

Then, using the concentration inequality for vectors, we have, with a probability
1−δ,
|bµk −µ k| ≤O

σd
mk
log m δ +σ
r
d
mk
log m δ
!
=O

σ
r
md
n log m δ
!
Since|u i −µ ki |2 ∼σ 2χ2 d, with a probability1−δ,
|ui −µ ki |2 =σ 2

d+O
 r
dlog N δ
!!
,∀i[N]
we have
max
i∈[N]
|ui −bµki | ≤max i∈[N] |µi −µ ki |+ max j∈[m] |µj −bµj|
≤σ
vuutd+O  r dlog N δ ! +O  σ r md n log m δ ! ≤O  σ √ d 
and
min
i∈[N],k̸=k i
|ui −bµk|= min j̸=k |µj −µ k| −max i∈[N] |ui −bµki |=Ω(
√
d)
As a result, whenσ=o(1), we have, with a probability1−δ,
ˆki =k i,∀i∈[N]
indicating that we obtain the correct indices of Gaussian distributions for all the
training examples inD b. Using the augmented training datasetDc, we learn a
linear regression modelew∈R md as
ew=

1
N
NX
i=1
exiex⊤ i
!−1
1
N
NX
i=1
exiyi
!
Since ˆki =k i for alli∈[N], we have
ew=

1
N
NX
i=1
xix⊤ i
!−1
1
N
NX
i=1
xiyi
!

High-Resolution Weather Forecasting via Data Scaling 23
wherex i =u i ⊗e ki. Following the same analysis, we have, with a probability at
least1−δ,
|ew−w| ≤O
 r
md
N log 1 δ
!
B Data and Evaluation Details
B.1 Dataset
As illustrated in Table 2, the dataset comprises real-time analysis data and
synthetic data generated through super-resolution applied to the ERA5 reanal-
ysis [16].
We select 13 standard vertical pressure levels (50, 100, 150, 200, 250, 300,
400, 500, 600, 700, 850, 925, and 1000 hPa) and include key atmospheric vari-
ables at these levels: geopotential, temperature, u component of wind, v com-
ponent of wind, and specific humidity. In addition to widely used surface level
variables, such as 2-meter temperature (T2M), 2-meter dewpoint temperature
(D2M), 10-meter wind components (U10, V10), and mean sea-level pressure
(MSL), we also incorporate several specialized surface variables that enhance
specific forecasting applications. These include surface pressure (SP), essential
for tracking synoptic-scale weather systems and mass conservation; 100-meter
wind components (U100, V100), which are valuable for wind power forecast-
ing; low cloud cover (LCC), total cloud cover (TCC), surface solar radiation
downwards (SSRD), and surface direct solar radiation (FDIR), which support
solar power forecasting; and sea surface temperature (SST), which is critical for
typhoon analysis and marine shipping applications. Furthermore, total column
water (TCW), total column vertically-integrated water vapour (TCWV), and
total precipitation (TP) are included to support precipitation forecasting.
Real-timeAnalysisDataReal-timeanalysisdatawithhighresolutionof0.1 ◦,
produced every 6 hours via 4D-Var data assimilation, serves as the initial con-
dition for IFS-HRES forecasts. This analysis is generated by assimilating a wide
range of observational sources, including satellite retrievals, radiosonde measure-
ments, and surface station reports, thereby providing a dynamically consistent
and physically coherent representation of the atmospheric state. Similarly, most
AI-based models use upscaled0.25◦ data as input for real-time forecasting. The
high-resolution analysis data has been provided by the European Centre for
Medium-Range Weather Forecasts (ECMWF) since mid-2016. For the accumu-
lated variables FDIR, SSRD, and TP, which are not available in the analysis
data, we use IFS-HRES forecasts as substitutes. Specifically, FDIR and SSRD
are taken as 1-hour accumulations over the past hour, while TP is provided
in two variants: TP1H, representing 1-hour accumulations over the past hour,
and TP6H, representing 6-hour accumulations over the past 6 hours. Note that
the baseline operational IFS-HRES data utilized for evaluation corresponding to
the year 2025 follows the active ECMWF operational cycles during that period
(primarily CY49R1, transitioning to subsequent updates as implemented).

24 Y. Zhao et al.
SyntheticDatabySuper-resolutionTheinputforsuper-resolutionisERA5,
a global atmospheric reanalysis dataset produced by the ECMWF. ERA5 pro-
vides detailed information on Earth’s climate and weather conditions from 1940
to the present. While it offers a spatial resolution of0.25◦, it significantly exceeds
real-time analysis data in volume. Therefore, to leverage this rich resource, we
feed ERA5 into the per-variable super-resolution model to generate synthetic
high-resolution data at0.1 ◦, matching the resolution of the real-time analysis.
The input variables are drawn from ERA5 and correspond to the same set of
variables listed in Table 2, ensuring consistency between the synthetic and real
training data.
Table 2:Variables used in the training. The "Type" column categorizes variables
as static (non-time-varying) properties, time-varying, single-level (surface) properties,
or time-varying atmospheric properties. The "Variable Name" and "Abbrev." columns
denotethelabelsassignedbyECMWF,whereasthe"ECMWFID"columnspecifiesthe
numerical identifier allocated by the organization. The "Input" and "Output" columns
indicate whether a variable functions as an input to or an output from BaguanHR.
Type Variable name Abbrev. Input Output ECMWF ID
Atmospheric Geopotential Z✓ ✓129
Atmospheric U wind component U✓ ✓131
Atmospheric V wind component V✓ ✓132
Atmospheric Temperature T✓ ✓130
Atmospheric Specific humidity Q✓ ✓133
Single 2-metre temperature T2M✓ ✓167
Single 2-metre dewpoint temperature D2M✓ ✓168
Single 10-metre U wind component U10✓ ✓165
Single 10-metre V wind component V10✓ ✓166
Single 100-metre U wind component U100✓ ✓228246
Single 100-metre V wind component V100✓ ✓228247
Single mean sea-level pressure MSL✓ ✓151
Single total cloud cover TCC✓ ✓164
Single low cloud cover LCC✓ ✓186
Single surface solar radiation downward SSRD✓ ✓169
Single total sky direct solar radiation at surface FDIR✓ ✓228021
Single sea surface temperature SST✓ ✓34
Single total column water TCW✓ ✓136
Single total column water vapor TCWV✓ ✓137
Single total precipitation TP×✓228
Static Land-sea mask LSM✓×172
Static geopotential at surface -✓×162051
Static angle of sub gridscale orography ANOR✓×162
Static anisotropy of sub gridscale orography ISOR✓×161
Static lake cover CL✓×26
Static soil type SOILTYP✓×500205

High-Resolution Weather Forecasting via Data Scaling 25
Data Partitioning StrategyTo ensure a robust evaluation and strictly pre-
vent temporal data leakage, we partition our dataset chronologically across dif-
ferent stages:
– Super-Resolution Training:The super-resolution model is trained using
paired ERA5 and real-time0.1◦ analysis data from 2018 to 2024.
– Synthetic Data Generation:Using the trained super-resolution model,
we synthesize 10 years of0.1◦ data from ERA5 covering 2007 to 2016. Due
to storage limitations, only 10 years of data are generated, although using
more data would likely yield greater benefits.
– Forecasting Model Training:The downstream BaguanHR forecasting
model is trained on a combination of the 10-year synthetic dataset (2007–
2016) and the real-time analysis data (2017–2024).
– Evaluation:Data from the entire year of 2025 is strictly reserved for model
evaluation on unseen future states.
B.2 Evaluation Metrics
We adopt the standard weather evaluation methodology outlined in Weather-
Bench [33], focusing on forecasts initialized at 00/12 UTC for the year 2025.
There are two metrics: latitude-weighted Root Mean Square Error (RMSE) and
latitude-weighted Anomaly Correlation Coefficient (ACC), which have also been
widely used in ML-based models [3,6,22,31].
Root mean square error (RMSE)RMSE is a commonly utilized statistical
metric in geospatial analysis and climate science to evaluate the precision of a
model’s predictions or estimates over various latitudinal ranges:
RM SE= 1 N ΣN t=1
r
1
H×W ΣH i=1ΣW j=1L(i)( ˜Xt,i,j −X t,i,j)2. (10)
The latitude weighting factorL(i)is used to account for the differences in surface
area represented by various latitudes on a spherical Earth. It is given by:
L(i) = cos(lat(i)) 1
H ΣH k=1cos(lat(k)) . (11)
Anomaly correlation coefficient (ACC)ACC measures the spatial correla-
tion between the prediction anomalies˜X ′ and ground truth anomaliesX′, both
computed relative to the historical climatology. The ACC is evaluated spatially
at each forecasting time steptand then averaged over allNvalid times in the
test set:
ACC= 1 N
NX
t=1
PH
i=1
PW
j=1 L(i) ˜X ′ t,i,jX ′ t,i,jrhPH
i=1
PW
j=1 L(i)( ˜X ′ t,i,j)2
i hPH
i=1
PW
j=1 L(i)(X ′ t,i,j)2
i , (12)

26 Y. Zhao et al.
where the anomalies are defined as:
˜X ′ t,i,j = ˜Xt,i,j −C t,i,j, X ′ t,i,j =X t,i,j −C t,i,j. (13)
Unliketakingasimpletemporalmeanovertheevaluatedtestset,theclimatology
Ct,i,j here denotes the historical day-of-year mean for the specific location(i, j)
corresponding to the validation timet, following the standard WeatherBench 2
guidelines [33].
C Model Architecture and Implementation Details
C.1 Problem Statement
BaguanHR is an advanced data-driven framework designed to generate accurate,
high-resolution global medium-range weather forecasts. BaguanHR takes the
atmospheric state at timetas input, represented asX t ∈R V×H×W , where
Vdenotes the number of atmospheric and surface variables considered in the
input, whileHandWrepresent the height (latitude) and width (longitude) of
the grid, respectively. In our high-resolution scenario with a spatial resolution of
0.1◦,H= 1801andW= 3600for the Earth. BaguanHR aims to establish the
mapping function ˜X t+∆t =BaguanHR(X t), where∆tdenotes the time interval
(6 hours). The model then produces 6-hourly forecasts into the future in an
auto-regressive manner.
System Overview.To achieve this goal under the severe scarcity of high-
resolution training data, our overall pipeline is decoupled into two critical com-
ponents: (1) aSuper-Resolution Data Generator, which first synthesizes
extensive0.1 ◦ pseudo-labels from decades of coarse historical data; and (2) the
BaguanHR Forecasting Model, which is subsequently trained from scratch
on this augmented dataset to perform the core auto-regressive forecasting task.
We detail both components below.
C.2 Super-Resolution Data Generator (Swin2SR)
Both data-driven models and numerical weather prediction systems fundamen-
tallytreatweatherforecastingasaninitialvalueproblemgovernedbytheNavier-
Stokesequationsandrelatedatmosphericdynamics.Incontrast,super-resolution
(SR) is a spatial reconstruction task. It does not require full adherence to the
temporalintegrationofphysicalequationsbutratherreliesheavilyonspatialpri-
ors and topographic information. As demonstrated by recent studies [1,15,35],
training a separate SR model for individual variables effectively avoids cross-
channel interference and yields significantly higher reconstruction quality. Thus,
we employ a tailored Swin2SR [8] architecture to perform variable-specific down-
scaling of the0.25◦ ERA5 data to0.1◦.
The architecture is specifically designed to leverage high-resolution static
topographies. The forward process features two key components:

High-Resolution Weather Forecasting via Data Scaling 27
– Topographic-Conditioned Embedding:The generator receives both the
0.25◦ coarse-grainedatmosphericvariablesandthe0.1 ◦ high-resolutionstatic
topographical constants (e.g., land-sea mask, orography). Through a dual-
branch convolutional stem with different strides, these two inputs are spa-
tially aligned and fused into a unified latent space. This ensures that the
generated atmospheric features are strictly conditioned on the underlying
physical geography.
– High-Frequency Residual Learning:Following deep feature extraction
by the Swin2SR backbone and PixelShuffle upsampling, the model avoids
generating the absolute target values directly. Instead, it outputs a residual
map∆X. The final0.1 ◦ pseudo-label is obtained by adding this learned
high-frequency residual to the bicubically interpolated low-resolution input:
ˆXhr = Interpolate(Xlr,mode=’bicubic’) +∆X (14)
This explicit residual connection forces the network to focus exclusively on
reconstructing missing fine-scale textures, yielding high physical fidelity.
C.3 The BaguanHR Forecasting Model
ThearchitectureoftheBaguanHRforecastingmodelfollowsanencoder-backbone-
decoder paradigm with a global residual connection. It effectively transforms
physical states into a latent space, simulates atmospheric dynamics over time
∆t, and projects the predicted increments back to the physical grid. Prior to pro-
cessing, all input variablesXt are standardized usingZ-score normalization
based on the historical climatological mean and standard deviation, ensuring
stable gradient propagation.
Encoder: Variable-Specific Tokenization and Hierarchical Embedding.The en-
coder is responsible for mapping the high-dimensional, multi-variable physical
inputs into a unified latent space. Given the input atmospheric stateX t ∈
RVin×H×W (whereV in = 86), each variable is first independently tokenized
via a patchify mechanism with a patch size ofp= 9. Subsequently, a learnable
variable-specific embedding is added to each variable’s token sequence to pre-
serve its physical identity. Unlike natural images, atmospheric states involve tens
of distinct physical variables. A naive cross-attention aggregation across allVin
variables would result in an excessive computational and memory bottleneck. To
address this, we propose aHierarchical Weather Embedding, which utilizes
a dual-stage cross-attention mechanism:
1.Group-Wise Aggregation:The 86 variables are partitioned into 12 phys-
ical groups. For the five 3D upper-air variables (z, u, v, t, q), we create an
overlapping splitbased on pressure levels to maintain vertical continuity:
levels between50∼600hPa form the “upper-level” groups, while levels
between400∼1000hPa form the “lower-level” groups. This yields 10 at-
mospheric groups. The time-varying surface variables (e.g., t2m, u10, sp)
and the static geographic variables (e.g., land-sea mask, orography) form

28 Y. Zhao et al.
the 11th and 12th groups. Within each group, a dedicated learnable channel
query aggregates information via cross-attention, producing a group-specific
summary vector.
2.Global Ensemble Aggregation:An ensemble query then performs a sec-
ondary cross-attention over the 12 group-specific summaries. The resulting
vectors are concatenated and projected to form the final multi-modal latent
token of dimensionC= 1536.
Furthermore, to provide the model with essential seasonal and diurnal context,
we inject aTime Embeddinginto the latent representation. The temporal fea-
tures—the day of the year (1–365) and the hour of the day (0–23)—are passed
through distinct learnable embedding dictionaries and added to the spatial to-
kens. An explicit full positional embedding is also applied to preserve global
geographic coordinates.
Swin Transformer Backbone.If the embedded tensor that the backbone receives
asinputcanbeviewedasalatentgridonwhichthesimulationisperformed,then
the backbone acts as a neural physics simulator. We opt for a Swin Transformer
V2 [?] backbone with cross-shaped windows. The embeddings are passed through
a deep stack of 24 Swin Transformer blocks to facilitate interactions among dif-
ferent patches. In contrast to the standard Vision Transformer (ViT), our choice
of Swin Transformer is critical for0.1◦ resolution. Each layer performs local self-
attention operations between tokens within20×40local windows. In alternating
layers, the windows are shifted, inherently enforcing locality and emulating the
message-passing computations performed by traditional numerical PDE solvers.
This mitigates the issue of attention maps spreading uniformly without local
structure, while strictly avoiding the quadratic complexity of vanilla Transform-
ers.
Decoder and Global Residual Connection.After latent-space evolution by the
backbone, the decoder projects the latent representation back to the original
spatial dimensions. Rather than directly predicting the absolute atmospheric
state at the next time step, the model predicts the dynamical increment over
∆t, which is added to the current input fields through a global skip connection.
Accumulated variables such as total precipitation are generated directly. This
residual design constrains the prediction trajectory and improves the stability of
auto-regressive forecasting. Finally, inverse Z-score normalization is applied to
recover the physical atmospheric variables.
C.4 Experimental Setups
The network architecture hyperparameters and computational complexity of
both the Super-Resolution model and the forecasting model are detailed in Ta-
ble 3.

High-Resolution Weather Forecasting via Data Scaling 29
Objective Loss Function.The super-resolution model and BaguanHR forecast-
ing model are both optimized using theLatitude-weighted Mean Absolute
Error (MAE)as the objective loss function. This ensures that the optimization
process accounts for the varying grid cell areas on the spherical Earth topology.
The lossLis defined as:
LM AE= 1 V×H×W
VX
v=1
HX
i=1
WX
j=1
L(i)

 ˜X t+∆t v,i,j −X t+∆t v,i,j

 (15)
whereL(i) = cos(lat(i)) 1
H
PH
k=1 cos(lat(k)) is the latitude weighting factor.
Training Stages and Configurations.The training pipeline encompasses the up-
stream data generation and the downstream forecasting model optimization. All
models are trained on a cluster of 32 NVIDIA A800 GPUs. To ensure stable
convergence and prevent error accumulation in the forecasting phase, the entire
process is conducted in four progressive stages:
– Stage 0: Super-Resolution Data Synthesis.Thanks to the lightweight
architectural design of the Swin2SR model and the localized nature of the
spatial reconstruction task, the per-variable SR models are highly efficient
to optimize. Training the SR model for a single variable takes only∼24
hours on 8 GPUs. Subsequently, synthesizing the entire 10-year (2007–2016)
0.1◦ global dataset requires approximately 2 days of inference time across
the cluster.
– Stage 1: Pretraining on Analysis Data.The BaguanHR forecasting
model is pretrained from scratch for a single-step forecast (∆t= 6h) us-
ing the EC analysis data (2017–2024) exclusively. This stage spans approxi-
mately 14 days (250,000 optimization steps). The learning rate is warmed up
linearly to5×10 −4 and then decays to1×10−8 following a cosine annealing
schedule.
– Stage 2: Synthetic Fine-Tuning.We extend the single-step training by
incorporating the additional 10 years of synthetic0.1 ◦ data generated in
Stage 0. This phase lasts approximately 4 days (70,000 steps) with a linearly
warmed-up learning rate peaking at2×10 −5.
– Stage 3: Rollout Training.Finally, to mitigate error accumulation over
long horizons, we perform 2 days of auto-regressive multi-step fine-tuning
using both the synthetic and real datasets. We employ a self-adaptive replay
buffer and store up to 40 historical states per GPU worker, with the buffer
size chosen according to strict CPU memory constraints. During this stage,
the learning rate is fixed at2×10−6.
Data Mixing and Sampling Strategy.During the Synthetic Fine-Tuning (Stage
2) and Rollout Training (Stage 3), the model learns from a combined dataset
comprising the 2017-2024 real EC analysis data and 10 years of synthetic SR
data. Prior to training, this mixed dataset is uniformly partitioned and sharded

30 Y. Zhao et al.
Table 3:Architectural hyperparameters of both the Super-Resolution Data Generator
(Swin2SR) and the BaguanHR forecasting model. Note that the original latitude di-
mension of 1801 is cropped to 1800 to ensure exact divisibility by the patch size (9×9).
Hyperparameter Super-Resolution (Swin2SR) BaguanHR Forecasting Model
Input Resolution (H×W)720×1440(0.25 ◦)1800×3600(0.1 ◦)
Output Resolution (H×W)1800×3600(0.1 ◦)1800×3600(0.1 ◦)
Input Channels (Vin) 82 (Atmospheric) + 6 (Constants) 80 (Atmospheric/Surface) + 6 (Constants)
Output Channels (Vout) 1 (Variable-specific) 82 (Including Precipitation)
Patch Size (p×p)1×1 9×9
Latent Embedding Dimension (C) 384 1536
Swin Transformer Blocks [6, 6, 6, 6](4 stages)24(Single deep stage)
Window Size12×12 20×40
Attention Heads [12, 12, 12, 12] 16
Total Parameters500.74 M 821.65 M
Table 4:Optimization configurations across the Super-Resolution (SR) generation
stage and the progressive training stages of the BaguanHR forecasting model.
Configuration SR Model (Data Gen.) BaguanHR Stage 1 BaguanHR Stage 2 BaguanHR Stage 3
Task Description Spatial downscaling Single-step forecast Single-step forecast Auto-regressive
Batch Size (Per GPU) 4 1 1 1
Optimizer AdamW AdamW AdamW AdamW
β1, β2 0.9,0.99 0.9,0.95 0.9,0.99 0.9,0.99
Weight Decay1×10 −5 0.05 1×10 −5 1×10 −5
Peak Learning Rate2×10 −4 5×10 −4 2×10 −5 2×10 −6 (Fixed)
LR Schedule Cosine Annealing Linear + Cosine Linear + Cosine Constant
Optimization Steps 50,000 250,000 70,000 5,000
across the local NVMe SSDs of the compute nodes. During optimization, each
GPU worker independently samples batches strictly from its local SSD shard.
Given the comparable volume of the two data sources, this decentralized sam-
pling strategy naturally yields a heterogeneous mini-batch composition where
the ratio of real to synthetic samples is continuously maintained at approxi-
mately1:1. A detailed exposition of this I/O-optimized data loading framework
is provided in Section D.
C.5 Self-Adaptive Rollout and Replay Buffer Strategy
In auto-regressive weather forecasting (Stage 3 rollout training), multi-step fine-
tuning is necessary to reduce error accumulation at long lead times. While main-
stream approaches often rely on simple unrolled backpropagation, recent models
such as Fengwu [14] and Aurora [4] have introduced replay-buffer-based designs
to improve long-range training stability. However, uniformly optimizing buffered
long-horizon states can bias training toward long-range error correction and de-
grade short-range predictive fidelity.
To address this trade-off under limited GPU and CPU memory, we propose
aSelf-Adaptive Rollout Strategywith two components:
Lead-Time-Aware Loss Weighting.Errors typically grow with lead time in an
unrolled trajectory, so treating all steps equally can cause long-range losses to

High-Resolution Weather Forecasting via Data Scaling 31
dominate optimization. We therefore apply a decaying weight based on the auto-
regressive step index. For thek-th prediction step (k= 1,2, . . . , K), the loss is
weighted by1/k, yielding
Lrollout =
KX
k=1
1
k LMAE( ˜X t0+k∆t, Xt0+k∆t). (16)
This harmonic decay emphasizes short-range accuracy while still providing su-
pervision for longer-horizon prediction.
Stochastic Buffer Replacement Schedule.Replay buffers in ML-based weather
models are often implemented as First-In-First-Out (FIFO) queues. For a high-
resolution model like BaguanHR, however, the large activation footprint limits
the local batch size to very small values (oftenN= 1per GPU). Under dis-
tributed training, a FIFO buffer can therefore make the global batch overly
concentrated on a narrow range of lead times, reducing trajectory diversity
and destabilizing optimization. To alleviate this issue, we replace FIFO with
aStochastic Buffer Update Strategy. When a trajectory in the 40-sample
CPU buffer reaches its maximum rollout horizon and is removed, we randomly
insert initialization states from different historical timestamps. As a result, each
optimization step draws a more heterogeneous mixture of atmospheric states and
lead-time stages across the 32 GPU workers. This reduces the tendency of the
global batch to be dominated by a single forecasting horizon and helps improve
optimization stability during distributed training.
D Large-Scale System Engineering and Computational
Cost
The transition from0.25◦ to0.1 ◦ global resolution poses unprecedented system-
level challenges. The intrinsic precision requirements of meteorological data ne-
cessitate 32-bit storage, as 16-bit quantization introduces non-negligible numer-
ical degradation across numerous thermodynamic variables. This high-precision
representation of a dense1801×3600grid results inexceptionally large in-
dividual data files—typically 4 to 5 GB each.
Consequently, training high-resolution weather forecasting models faces a se-
vere I/O bottleneck, a challenge rarely encountered in the standard training
pipelines of large language models or computer vision systems. The end-to-end
training throughput is strictly bottlenecked by the storage-to-CPU bandwidth
rather than the GPU’s theoretical floating-point operations per second (FLOPs).
To decouple GPU computation from disk latency and maximize hardware uti-
lization, we employ several complementary I/O strategies.
D.1 Hybrid I/O and Caching Strategies
Through the following three customized data-loading strategies, our pipeline
effectively masks the I/O latency and achievesa training speedup of over
4×compared to naive network storage access.

32 Y. Zhao et al.
Data Partitioning by Machine.Our storage infrastructure includes a large-scale
Network Attached Storage (NAS) system alongside approximately 12 TB of
high-speed NVMe SSD storage per 8-GPU machine. To leverage the significantly
faster read/write performance of local SSDs compared to the NAS, we partition
the entire training dataset intonshards—wheren= 4equals the number of
physical machines—and distribute one unique shard to each machine. During
distributed training, each machine loads only the data shard corresponding to
its assigned node rank, drastically minimizing cross-node network I/O overhead
and maximizing localized throughput.
Hybrid Storage Strategy Based on Time-ID Partitioning.Despite the data par-
titioning, the aggregate 12 TB of SSD storage per machine is still insufficient to
house the full historical dataset. To address this, we implement a time-based hy-
brid storage strategy: data initialized at UTC 00:00 and 12:00 (which constitute
the primary cycles for operational weather forecasting) is permanently cached
on the local SSDs for high-speed access. Meanwhile, data from the intermediate
UTC 06:00 and 18:00 cycles resides on the NAS and is fetched dynamically. This
specific allocation strategy guarantees a high cache hit rate on the SSDs while
remaining within hardware limits.
Efficient Replay of Cached Data.Our distributed training pipeline first transfers
data from storage (SSD/NAS) to CPU memory before moving it to the GPU
memory. Because the end-to-end throughput is bottlenecked by the sluggish
I/O bandwidth from storage to CPU, we mitigate this latency through an in-
memoryreplaymechanism.Weaggressivelyreusedatabatchescurrentlyresident
in the CPU memory queue to feed the GPUs, maintaining active compute cycles
whenever asynchronous I/O threads are still fetching new data from the storage
layer.
D.2 System-Level Profiling
To accurately profile the isolated impact of our I/O optimization strategies,
it is essential to decouple the storage-to-CPU bottleneck from inter-node net-
work communication overhead (e.g., NCCL gradient synchronization across ma-
chines). Therefore, we benchmarked the training throughput on a single compute
node (equipped with 8 NVIDIA A800 GPUs and local NVMe SSDs) representing
one functional shard of our full 32-GPU distributed pipeline.
As detailed in Table 5, the BaguanHR architecture exhibits exceptionally
high computational complexity, reaching approximately 364.7 TFLOPs per op-
timization step per GPU. However, a baseline data-loading strategy that reads
training samples directly from the network-attached storage (NAS) leads to se-
vere GPU under-utilization. The average I/O wait time reaches 28.7 seconds
per step, reducing the GPU active ratio to only 54.0%. In contrast, our hybrid
I/O and SSD partitioning strategy effectively mitigates this system bottleneck,
reducing the average I/O wait time to just 0.69 seconds per step and increasing
the GPU active ratio to 92.0%. These results indicate that, for0.1◦ training,

High-Resolution Weather Forecasting via Data Scaling 33
the dominant limitation is not raw computation itself, but the efficiency of the
storage and data delivery pipeline.
Table 5:System-level profiling of computational complexity and I/O efficiency un-
der different data-loading strategies. To isolate the storage bottleneck from cross-node
communication overhead, metrics were collected over 200 optimization steps on a single
operational 8×A800 GPU node.
Model Pipeline Theoretical Compute (TFLOPs / Step / GPU) Baseline: Direct NAS Read Ours: Hybrid I/O & Partitioning GPU Active Ratio I/O Wait / StepGPU Active Ratio I/O Wait / Step
BaguanHR (0.1◦) 364.7 54.0% 28,714 ms 92.0% 692 ms
E Extended Discussions
E.1 Experimental Protocol for Conditional Entropy and Task
Robustness
In the main text (Section 3.1), we posit that “Super-Resolution (SR) has prov-
ably lower conditional entropy than multi-step forecasting (FC)”, making it a
significantly more robust vehicle for data transfer than model fine-tuning. Due
to page constraints, the specific experimental procedures used to validate this
core insight were omitted. Here, we detail the lightweight inference protocols
designed to measure task difficulty and input perturbation sensitivity.
Experiment I: Task Difficulty ComparisonThe primary objective of this
experiment is to empirically demonstrate that SR is an intrinsically simpler task
than temporal forecasting by directly comparing their reconstruction errors.
– SR Task Protocol:The model takes the low-resolution stateX0.25◦ t as in-
put and outputs the high-resolution reconstructionˆX 0.1◦ t . The ground truth
is the exact same-time high-resolution analysisX0.1◦ t .
– Forecasting Task Protocol:The model takes the high-resolution state
X 0.1◦ t as input and predicts the future stateˆX 0.1◦ t+6h. The ground truth is the
actual future analysisX 0.1◦ t+6h.
As reported in the main text, the SR task yields significantly lower RMSE (e.g.,
13.8 vs. 23.6 for z500). From an information-theoretic perspective, the lower
error indicates that the conditional entropy of same-time spatial reconstruc-
tionH(X 0.1◦ t |X 0.25◦ t )is substantially lower than that of cross-time prediction
H(X 0.1◦ t+6h|X 0.1◦ t ).

34 Y. Zhao et al.
Experiment II: Input Perturbation SensitivityThe second experiment
aims to prove that forecasting, governed by chaotic atmospheric dynamics, am-
plifies input errors exponentially, whereas the SR mapping remains highly stable.
We apply isotropic Gaussian noiseε∼ N(0, σ2)at varying intensitiesσ∈
{0.01,0.05,0.10,0.20,0.25}to the input fields of both models. The sensitivity
is quantified by theAmplification Factor, defined as the ratio of the output
error change to the magnitude of the injected noise. For the SR model:
Y SR clean =Φ SR(Xt), Y SR noisy =Φ SR(Xt +ε) (17)
AmplificationSR = ||Y SR noisy −Y SR clean|| ||ε|| (18)
For the Forecasting (FC) model:
Y F C clean =Φ F C(Xt), Y F C noisy =Φ F C(Xt +ε) (19)
AmplificationF C= ||Y F C noisy −Y F C clean|| ||ε|| (20)
As illustrated in Figure 1 of the main text, the AmplificationSR curve re-
mains relatively flat and strictly below1.0(e.g.,0.6∼0.8×), indicating that
input information is transferred to the output with minimal and reversible loss.
In sharp contrast, the AmplificationF Ccurve exhibits an upward trend (>1.0×),
demonstrating that small input perturbations are irreversibly magnified due to
the chaotic nature of temporal evolution. This justifies our paradigm shift: gen-
erating pseudo-labels via SR is fundamentally more robust than attempting to
extract fine-scale structures from a pre-trained0.25◦ forecasting model.
E.2 Mathematical Formulation of the Data Scaling Law
In main text Section 5.2 (Fig. 4), we presented the empirical data scaling laws,
demonstratingthatmodelperformanceimprovesasthevolumeofhigh-resolution
training data increases, before eventually plateauing. To rigorously formalize this
observation, we fitted the empirical validation RMSE to a generalized power-law
function with an irreducible error term:
E(D) =αD −β +E ∞ (21)
whereE(D)is the forecast error given training data volumeD(in years),αis
a scaling constant,β >0is the characteristic scaling decay exponent, andE∞
represents the theoretical saturation bound (irreducible error). The precise fitted
parameters are detailed in Table 6.
The emergence of the saturation thresholdE∞ (evident as the curves flatten
around the 18-year mark in Fig. 4) suggests that while synthesizing additional
decades of data via SR improves the representation of rare meso-scale anomalies,

High-Resolution Weather Forecasting via Data Scaling 35
the deterministic predictive skill is ultimately bounded by the inherent chaotic
limits of atmospheric predictability and the parameter capacity of the current
architecture.
Crucially, it is important to note that the models evaluated in this scaling
analysis were trained exclusively for the6-hour single-step prediction task,
without undergoing the subsequent auto-regressive rollout fine-tuning. Conse-
quently, the 6-hour forecast metrics (whereR2 >0.95across all variables) pro-
vide the purest, most direct reflection of the underlying data scaling mechanism,
isolated from the complex error accumulation inherent in long-range unrolling.
Furthermore, as revealed in Table 6, the scaling exponentβexhibits a systematic
decay as the forecast lead time increases (e.g., for T2M,βdrops from 2.207 at
6h to 0.792 at 120h). This compelling quantitative finding indicates that while
short-term localized dynamics are highly data-hungry and benefit immensely
from high-resolution data scaling, extreme long-term forecasting becomes in-
creasingly dominated by systemic chaotic divergence, rendering pure data scal-
ing progressively less effective. This formulation provides a rigorous guideline for
balancing the computational cost of data synthesis against marginal performance
gains across different forecasting horizons.
Table 6:Fitted parameters of the empirical scaling lawE(D) =αD−β +E ∞ for rep-
resentative atmospheric variables across different lead times.R2 indicates the goodness
of fit.
Lead Time Variable Scaling Const (α) Exponent (β) Irreducible Error (E∞)R 2
6h T2M 0.817 2.207 0.682 0.968
6h U10 1.697 2.681 0.690 0.974
6h MSL 41.950 1.192 33.370 0.959
6h Z500 35.062 1.012 20.684 0.951
72h T2M 1.164 1.189 1.107 0.938
72h U10 1.192 0.745 1.549 0.795
72h MSL 268.332 1.126 144.224 0.802
72h Z500 236.864 0.879 122.599 0.785
120h T2M 1.146 0.792 1.488 0.870
120h U10 1.427 0.481 2.244 0.749
120h MSL 270.943 0.767 277.567 0.689
120h Z500 285.245 0.542 239.073 0.693
E.3 Extended Discussion on Physical Consistency of SR-Generated
Fields
The forecast improvements shown in Figs. 4–8 of the main paper demonstrate
that SR-generated pseudo-labels provide effective high-resolution training sig-
nals for downstream forecasting. However, these downstream gains alone do not
fully rule out the concern that SR may hallucinate physically inconsistent high-
frequency details. We therefore directly examine whether the SR-generated fields

36 Y. Zhao et al.
preserve key diagnostic relationships of the reference atmosphere, using three
complementary physical perspectives.
First, we evaluate themoisture structureusing relative humidity (RH)
diagnosed from temperature and specific humidity, which tests whether ther-
modynamic and moisture variables remain mutually coherent after SR. Second,
we evaluate thedynamical structureusing geostrophic wind speed|V g|di-
agnosed from geopotential heightZ, which reflects whether the reconstructed
pressure-level fields preserve large-scale balanced dynamics. Third, we evaluate
thethermodynamicstratificationusingpotentialtemperaturedifferences∆θ
between pressure levels, which measures whether the vertical thermal structure
remains consistent.
Table 7 reports latitude-weighted correlations between the SR-generated di-
agnostics and those computed from the 0.1◦ analysis. The consistently high
correlations indicate that the per-variable SR fields preserve key moisture, dy-
namical, and thermodynamic structures despite being generated independently
for each variable. In addition, the power spectral analysis in Fig. 9 shows that
the SR fields closely match the 0.1◦ analysis over most resolved wavelengths,
without introducing systematic spurious high-frequency energy.
Table 7:Physical consistency of per-variable SR fields. Values are latitude-weighted
correlations against EC 0.1◦ analysis.
Level (hPa) RH Level (hPa)|V g| Layer (hPa)∆θ
500 0.962 500 0.821 700–500 0.972
850 0.940 850 0.843 850–700 0.964
925 0.961 925 0.855 925–850 0.937
100101102
Wavelength ( E)
10 2
100
102
104
Power
msl
0.1  analysis
SR field
100101102
Wavelength ( E)
10 6
10 4
10 2
100
Power
t2m
0.1  analysis
SR field
Fig.9:Power spectra of SR-generated fields and EC 0.1◦ analysis fields, using 2-meter
temperature (t2m) and mean sea-level pressure (msl) as examples.

High-Resolution Weather Forecasting via Data Scaling 37
E.4 Extended Discussion on Baseline Selection and Forecasting
Dynamics
InSection5.3ofthemaintext,ourcomparisonincludesIFS-HRESandBaguan+swin2sr
overthefullforecastrange,andfurtherextendstoGraphCast+swin2sr,Pangu+swin2sr,
and Baguan+GHR within the short-term 3-day window. It is essential to clarify
that these “+swin2sr” configurations represent azero-shot post-processing
paradigm. In this setup, the respective0.25◦ pre-trained forecasting models are
executed entirely frozen, and their output states are subsequently upscaled to
0.1◦ during inference using our super-resolution model, without any end-to-end
fine-tuning on the high-resolution grid. The Pangu and GraphCast forecasts are
generated using ECMWF’sai-modelsframework and its public model plug-
ins [32].
This specific evaluation design is intentional, serving to expose the severe in-
formation bottleneck inherent to decoupled post-processing routes. At early fore-
casting lead times (short-range), the atmospheric state still contains rich high-
frequency spatial structures and sharp mesoscale gradients. Coarse-resolution
(0.25◦)modelsinherentlyfailtoresolvethesefeatures,resultinginoverlysmoothed
outputstates.Attemptingtoreconstructsuchlostfine-scaleinformationposthoc
via super-resolution is fundamentally ill-posed and tends to amplify forecast er-
rors. This information loss helps explain why our end-to-end BaguanHR model
achieves its largest advantages in the short-to-medium range, where fine-scale
structures are still most prominent.
Interestingly, as the auto-regressive rollout extends to longer lead times (e.g.,
10 days), the performance gap between BaguanHR and the post-processing base-
lines gradually narrows. This trend is closely related to the chaotic nature of at-
mospheric dynamics and the accumulated error growth in deterministic forecast-
ing. At extended lead times, all deterministic auto-regressive models, including
BaguanHR, tend to lose variance and produce progressively smoother forecast
states. As fine-scale structures become increasingly attenuated, the disadvantage
imposedbythe0.25 ◦ informationbottleneckbecomeslesspronounced,whichcan
make post-hoc upscaling appear relatively more competitive in the long range.
To ensure a fair comparison and to show that our gains are not simply due
to avoiding post-processing smoothing, we also includeBaguan+GHR(re-
produced following [14]) in our evaluation. This baseline represents a strong
coarse-to-fine transfer learning paradigm, in which the forecasting model is fur-
ther fine-tuned on the0.1 ◦ analysis grid. By consistently outperforming both
the zero-shot post-processing baselines and the fully fine-tuned Baguan+GHR
model within the critical 3-day operational window, our results indicate that the
proposed “synthetic-plus-real” data scaling strategy provides a more effective
route toward high-resolution AI weather forecasting.
E.5 Comparison Against Station Observation
While the grid-to-grid evaluations against EC analysis in the main text provide a
comprehensive global perspective, gridded analysis data may still contain model-
dependent diagnostic uncertainties. To further assess whether the0.1◦ resolution

38 Y. Zhao et al.
of BaguanHR translates into tangible improvements in real-world forecasting, we
extend the evaluation to direct ground station measurements through grid-to-
point verification.
For this evaluation, we construct a global ground-truth subset comprising
measurements from13,058weather stations worldwide. The raw station obser-
vations were accessed via theMeteostatAPI [23], which aggregates data from
public providers including NOAA and DWD. We use hourlywspd(wind speed,
corresponding to
√
u102 +v10 2) and hourlytemp(air temperature, correspond-
ing to T2M) from January 1, 2025 to December 20, 2025. To map gridded model
outputs to station coordinates, we apply standard bilinear interpolation from
the surrounding grid points before computing forecast errors.
Consistent with the grid-based evaluation, BaguanHR also performs strongly
in station-based verification. As shown in Fig. 10, BaguanHR achieves lower
RMSE than both IFS-HRES and Baguan+swin2sr for 2-meter temperature and
wind speed across most lead times. This result further supports the robustness
of BaguanHR in localized surface forecasting.
1 3 5 7 10
Lead time (days)
2.0
2.5
3.0
3.5
4.0RMSE (K)
2m T emperature at weather station, RMSE
IFS-HRES
BaguanHR
Baguan+swin2sr
1 3 5 7 10
Lead time (days)
1.6
1.8
2.0
2.2
2.4
2.6RMSE (m/s)
Wind Speed at weather station, RMSE
IFS-HRES
BaguanHR
Baguan+swin2sr
Fig.10:Station-based RMSE as a function of lead time for 2-meter temperature (left)
and wind speed (right). BaguanHR consistently achieves lower errors than both IFS-
HRES and Baguan+swin2sr across most lead times.
E.6 Visualization of High-Resolution Forecasts
To qualitatively demonstrate the structural fidelity and precision of our proposed
framework, Figures 11, 12, and 13 present comprehensive spatial visualizations
of the 2-meter temperature (T2M), the 10-meter U-component of wind (U10),
and specific humidity at 850 hPa (Q850), respectively. All forecast trajectories
are initialized at00:00 UTC on December 10, 2025.
Each figure compares the ground truth (ECMWF0.1 ◦ analysis) against
the predictions generated by three distinct systems: our end-to-end BaguanHR

High-Resolution Weather Forecasting via Data Scaling 39
model, the zero-shot post-processing baseline (Baguan+swin2sr), and the op-
erational physical baseline (IFS-HRES). Corresponding error distribution maps
(Predicted−Analysis) are also provided. These examples serve as qualitative
case studies, showing that BaguanHR generally produces predictions that are
visually closer to the analysis and exhibits lower overall error than the post-
processing baseline.
E.7 The Performance of BaguanHR in Tracking Tropical Cyclones
Building on the individual case study in Fig. 8(a) and (b) of the main text,
we further evaluate the robustness of our framework for tropical cyclone (TC)
tracking across a broader set of historical storms. Figure 14 shows tracking error
(km) as a function of forecast lead time for six representative storms, together
with basin-mean errors over the two major cyclogenesis regions: the Western
North Pacific and the North Atlantic. The ground-truth TC tracks used in both
the main text and this supplementary analysis are taken from the International
Best Track Archive for Climate Stewardship (IBTrACS) [11,20], which provides
the most comprehensive and globally unified archive of historical tropical cyclone
best-track data.
For a more statistically robust evaluation, the tracking error of each storm is
not computed from a single forecast only. Instead, we generate multiple forecast
trajectories initialized from different valid 00:00/12:00 UTC timestamps over
the storm lifetime, and report the mean tracking error across these initializa-
tion times at each lead time. As shown in Fig. 14, BaguanHR achieves consis-
tently strong TC tracking performance across both individual storms and basin-
mean statistics. In particular, over the North Atlantic and for several representa-
tive hurricanes, BaguanHR generally maintains lower tracking errors than both
Baguan+swin2sr and IFS-HRES throughout the 72-hour window. Although the
margin is smaller over the more challenging Western North Pacific, BaguanHR
remainscompetitiveoverall,indicatingthatsynthetic-data-basedhigh-resolution
scaling provides a reliable basis for TC trajectory prediction.
F Limitations and Broader Impact
This study relies entirely on public, gridded meteorological datasets and does
not involve human subjects, personal data, or sensitive individual information.
More broadly, our framework provides a practical data-centric route for improv-
ing high-resolution weather forecasting under limited compute and data avail-
ability. By converting long-term coarse-resolution reanalyses into synthetic 0.1°
training data, it may help widen access to stronger extreme-weather forecasting
systems for institutions and regions that cannot afford large operational model-
ing pipelines.
Nevertheless, several limitations remain. First, our synthetic high-resolution
data are generated by per-variable super-resolution models trained indepen-
dently for each field. While this design improves variable-specific fidelity, it may

40 Y. Zhao et al.
EC
analysis
Lead time: 1 day
 Lead time: 3 days
 Lead time: 7 days
BG-HR
BG-HR
- EC
Baguan
+ swin2sr
Baguan+swin2sr
- EC
IFS-HRES
IFS-HRES
- EC
260
280
300
320
K
260
280
300
320
K
5.0
2.5
0.0
2.5
5.0
K
260
280
300
320
K
5.0
2.5
0.0
2.5
5.0
K
260
280
300
320
K
5.0
2.5
0.0
2.5
5.0
K
Fig.11:Qualitative comparison of2-meter temperature (T2M)forecasts initial-
ized at 00:00 UTC, Dec 10, 2025.

High-Resolution Weather Forecasting via Data Scaling 41
EC
analysis
Lead time: 1 day
 Lead time: 3 days
 Lead time: 7 days
BG-HR
BG-HR
- EC
Baguan
+ swin2sr
Baguan+swin2sr
- EC
IFS-HRES
IFS-HRES
- EC
20
10
0
10
20
m s 1
20
10
0
10
20
m s 1
10
0
10
m s 1
20
10
0
10
20
m s 1
10
0
10
m s 1
20
10
0
10
20
m s 1
10
0
10
m s 1
Fig.12:Qualitative comparison of the10-meter U-component of wind (U10)
initialized at 00:00 UTC, Dec 10, 2025.

42 Y. Zhao et al.
EC
analysis
Lead time: 1 day
 Lead time: 3 days
 Lead time: 7 days
BG-HR
BG-HR
- EC
Baguan
+ swin2sr
Baguan+swin2sr
- EC
IFS-HRES
IFS-HRES
- EC
0.000
0.005
0.010
0.015
0.020
kg kg 1
0.000
0.005
0.010
0.015
0.020
kg kg 1
0.004
0.002
0.000
0.002
0.004
kg kg 1
0.000
0.005
0.010
0.015
0.020
kg kg 1
0.004
0.002
0.000
0.002
0.004
kg kg 1
0.000
0.005
0.010
0.015
0.020
kg kg 1
0.004
0.002
0.000
0.002
0.004
kg kg 1
Fig.13:Qualitative comparison ofspecific humidity at 850 hPa (Q850)initialized
at 00:00 UTC, Dec 10, 2025.

High-Resolution Weather Forecasting via Data Scaling 43
12 24 36 48 60 72
Lead time (hours)
40
60
80
100
120Tracking error (km)
T yphoon Bailu
IFS-HRES
BaguanHR
Baguan+swin2sr
12 24 36 48 60 72
Lead time (hours)
50
100
150
200
T yphoon Neoguri
IFS-HRES
BaguanHR
Baguan+swin2sr
12 24 36 48 60 72
Lead time (hours)
20
40
60
80
100
120
140
T yphoon Wutip
IFS-HRES
BaguanHR
Baguan+swin2sr
12 24 36 48 60 72
Lead time (hours)
50
100
150
200
250
300
350Tracking error (km)
Hurricane Erin
IFS-HRES
BaguanHR
Baguan+swin2sr
12 24 36 48 60 72
Lead time (hours)
100
200
300
400
Hurricane Jerry
IFS-HRES
BaguanHR
Baguan+swin2sr
12 24 36 48 60 72
Lead time (hours)
100
200
300
400
500
600
Hurricane Melissa
IFS-HRES
BaguanHR
Baguan+swin2sr
12 24 36 48 60 72
Lead time (hours)
100
200
300
400Tracking error (km)
Western North Pacific
IFS-HRES
BaguanHR
Baguan+swin2sr
12 24 36 48 60 72
Lead time (hours)
50
100
150
200
250
300
350
400
North Atlantic
IFS-HRES
BaguanHR
Baguan+swin2sr
Fig.14:Comparison of tropical cyclone tracking error versus lead time for six repre-
sentative storms and the corresponding basin-wide averages over the Western North
Pacific and North Atlantic. The ground truth tracks are derived from the IBTrACS
dataset. Errors for individual storms are averaged across multiple viable initialization
timestamps.
not fully preserve cross-variable coupling and multivariate physical consistency
at the finest scales. Second, although 0.1◦ resolution (roughly 9 km) is effective
formesoscaleforecasting,itisstillinsufficienttoexplicitlyresolvemicroscalecon-
vective extremes such as tornadoes, hail, or highly localized severe storms. Third,
forecast errors still accumulate with lead time under auto-regressive rollout. In
particular, BaguanHR brings limited additional gains at 10–15 day lead times,
consistent with the practical 10-day predictability limit of instantaneous midlati-
tude weather [39]; at such horizons, forecasts are mainly controlled by large-scale
atmospheric patterns and fine-scale details become weakly predictable. Future
work will explore ensemble forecasting to better characterize forecast uncertainty
and extend the model’s practical predictability.
