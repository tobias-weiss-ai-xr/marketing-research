---
title: How do World Models and Policies Compose in LLM Agents? A Joint Spectral and Behavioral Account
url: https://arxiv.org/abs/2608.30067
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Ruize Xu
- Xiao Yu
- Yujin Tang
- Chenming Shang
- Nikhil Singh
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.30067
pages: 21
chars: 82648
fetched_at: '2026-11-08T13:35:01+00:00'
kb_version: 1
---

# How do World Models and Policies Compose in LLM Agents? A Joint Spectral and Behavioral Account

How do World Models and Policies Compose in LLM Agents?
A Joint Spectral and Behavioral Account
Ruize Xu1, Xiao Yu2, Yujin Tang1, Chenming Shang1, Nikhil Singh1
1Dartmouth College 2Columbia University
{ruize.xu.gr,yujin.tang.gr,chenming.shang.gr,nikhil.u.singh}@dartmouth.edu
xy2437@columbia.edu
Abstract
How do LLM agents come to both understand
environments they act in and master tasks set
within them? Through controlled experiments
combining world-model training (next-state
prediction) and policy training (reward max-
imization), we investigate this question. We
dissect the resulting models through their addi-
tive parameter updates. Geometrically, we find
effective world-model updates are low-rank and
share aninput-feature subspace with policy up-
dates while writing to nearly orthogonalout-
putdirections, whether trained separately or se-
quentially. However, we find that, in projection
interventions, the sequential update induces
more robustness than separate policy RL when
removing the world model’s leading input direc-
tions, suggesting that it has learned alternative
input pathways. Behaviorally, we find the se-
quentially trained agent explores a wider range
of states and actions. Based on this, we ask:
does policy training preserve world knowledge
as well as itcould? We probe this with training-
free merging built on the geometrically moti-
vated input basis plus an online world-model
loss during policy RL, and show both improve
over the untreated baseline. Our findings sug-
gest world knowledge and task-directed ability
can be learned in geometrically complementary
forms, and that future post-training pipelines
should consider how best to engineer the inter-
face between them.
1 Introduction
We know things about the world, and we do things
in it. Language models too are increasingly stud-
ied through this dual lens (e.g., theirworld mod-
els(Li et al., 2023; Toshniwal et al., 2022; Guan
et al., 2023; Vafa et al., 2024)) and are even ex-
plicitly trained to internalize both these capaci-
ties. For example, post-training pipelines for LLM-
based agents increasingly adopt a two-stage for-
mula: aworld-modelstage that trains the model
Code:github.com/Rick-Xu315/WM_Spectral
to anticipate environment dynamics, followed by
apolicystage that optimizes end-task reward (Yu
et al., 2025b; Zhang et al., 2026; Yu et al., 2025a;
Chen et al., 2025; Yu et al., 2026). This sequential
pipeline consistently improves over policy training
from a base model, often by sizable margins.
What is the relationship between these two ob-
jects: knowledge and ability? Intuitively, knowing
your environment well helps you select better ac-
tions. Still, the two are not the same: by analogy,
radiologists don’t necessarily make good surgeons.
Despite the empirical success of world-model learn-
ing, the precise mechanism by which it benefits
downstream policies remains opaque. For example,
do world models act as a warm-up that places the
policy at a better initialization in a region of weight
space it would have reached on its own? Does it
identify a useful subspace the policy stage then re-
fines? Or does it leave behind a representational
structure on which the policy builds in meaning-
fullycomplementarydirections?
Getting good answers to these questions is po-
tentially consequential for both interpretation and
design. If world-model learning accelerates the
policy’s discovery of the same solution, the second
stage should in principle be able to absorb the first,
and the pipeline could be collapsed without loss. If
instead the two stages contribute structurally dif-
ferent things, then how to preserve, combine, and
schedule them is an important design lever for agen-
tic post-training. Prior work has documented the
benefit of the pipeline but rarely its mechanism.
Existing analyses either evaluate the composed
pipeline as a black box (Yu et al., 2026; Chen et al.,
2025) or characterize properties of post-training
updates in isolation (Aghajanyan et al., 2021; Hu
et al., 2022; Zhu et al., 2025), without directly con-
trasting world-model and policy stages. Perhaps
closest to the present work is Zhu et al. (2025),
which uses spectral structure to show how RLVR
largely preserves principal subspaces and updates
1
arXiv:2608.30067v1  [cs.LG]  30 Aug 2026

off-principal directions vs. SFT. Similarly, we ana-
lyze post-training updates through spectral geom-
etry and, consistent with their results, we find RL
and SFT updates differ sharply in the world model
regime. However, our primary focus is within the
RL regime, analyzing the input-feature vs. output
directions.
We take a first step toward understanding
how world-model and policy stages interact via
parameter-space dissection of a controlled family
of post-trained checkpoints. For each post-training
paradigm X, we form the additive parameter up-
date ∆X =θ X −θ 0 relative to the base model;
the policy stage’s incremental contribution on top
of the world model can then be analyzed sepa-
rately. We then conduct a series of spectral in-
terventions (subspace projection, rank truncation,
and magnitude-based pruning) and behavioral mea-
surements (held-out next-state prediction entropy,
state coverage, and patterns of success). Our results
show meaningful complementarity between world-
model and policy updates: the two stages share
an input-feature subspace but write to nearly or-
thogonal output directions, and sequential training
additionally equips the policy update with input-
pathway redundancy that base-initialized policy
training cannot acquire. We also show that the two-
stage agent exhibits useful behavioral capacities
(e.g., preserved world-model calibration, expanded
state coverage) over the policy-only version.
In all, this paper contributes an exploratory em-
pirical analysis of two-stage agentic post-training:
a parameter-space dissection that maps out the geo-
metric structure underlying the two-stage recipe’s
empirical success, across two benchmarks and two
models, in which we ask:
RQ1 Are there geometric and behavioral signatures
of effective world-model training?
RQ2 What is the relationship between parameter
updates produced by world-model and policy
training, independently vs. sequentially?
RQ3 Is the world-model preserved enough through
policy training, and can we improve this?
This work then contributes:
1. Empirical evidenceshowingspectral and
behavioral signatures of effective world-
model training(RQ1; §4, §6).
2. A ∆-decompositionand left/rightsubspace
projection methodology, using which we
findgeometric evidence of stage comple-
mentarity(RQ2; §5). We find that RL-trained
world models’ left singular subspaces (out-
put directions) are nearly orthogonal to the
downstream policy’s, while their right sin-
gular subspaces (input-feature directions) are
strongly aligned. Sequential training addition-
ally equips the policy update with redundant
input pathways unavailable from base-only.
3. Design implicationsforpreservingworld
models during policy training, realized via
merging and SFT experiments(RQ3; §7).
The complementarity finding predicts that the
two stages should compose constructively. We
test both a training-free KnOTS/TIES merge
and an online world model SFT auxiliary loss
during policy learning (similar to concurrent
work by Shrivastava et al. (2026)), both of
which improve over the untreated baseline.
2 Preliminaries
2.1 Problem Setup
We formulate multi-step task completion as a
Markov Decision Process ⟨S,A,T,R, γ⟩ (Sutton
and Barto, 2018). A ReAct-style (Yao et al., 2023)
LLM agent πθ interleaves reasoning and acting:
at step t, it receives an observation st ∈ Sto-
gether with up to H turns of interaction history
⟨st−H , at−H , . . . , st⟩, produces thought τt, and
emits an action at ∼π θ(· |st−H:t , at−H:t−1 ); the
environment returns the next observation st+1 ∼
T(· |s t, at). The loop terminates with a task-
success rewardr T .
World model.A world model Wϕ is a learned
surrogate for the transition T (Ha and Schmidhu-
ber, 2018; Hafner et al., 2023): it predicts the next
state ˆst+1 ∼ Wϕ(· |st−H:t , at−H:t ). We write ˆst
for predicted ands t for ground-truth states.
2.2 Two-stage Training
A growing line of work (Yu et al., 2025b; Zhang
et al., 2026; Yu et al., 2025a, 2026) adopts a two-
stage post-training pipeline for agentic LLMs: a
world-modelstage that grounds πθ in environment
dynamics, followed by apolicy RLstage that opti-
mizes task-success reward.
World-model SFT.The simplest instantiation
finetunes πθ on transition triplets to maximize
logπ θ(st+1 |s t−H:t , at) (Yu et al., 2025b; Zhang
2

et al., 2026; Yu et al., 2025a; Chen et al., 2025).
WMSFT inherits the pitfalls of imitation learning:
token-level rather than semantic supervision, sen-
sitivity to data quality, and model collapse / catas-
trophic forgetting (Yu et al., 2026).
World-model RL (WMRL).Yu et al. (2026) train
the world model with RL on a self-supervisedsim-
to-realreward, which we call WMRL. Given a pre-
diction(τ t,ˆst+1)∼π θ(· |st−H:t , at), the reward
rWM =1  sim  E(ˆst+1), E(st+1)  > η  (1)
scores embedding-space proximity to the realized
next state, where E(·) is a frozen embedding
model, sim(·,·) a similarity function, and η a
threshold. πθ is optimized with GRPO (Shao et al.,
2024) on its own rollouts using this reward, thereby
encouragingsemanticnext-state alignment. We
test η∈ {0.5,0.8,0.9}, and also test alternates in-
cluding LLM-as-judge evaluation (no-η) and world-
model transitions extracted from official ALFWorld
expert data.
Policy RL ( PRL).The second stage then opti-
mizesπ θ end-to-end for task success with GRPO:
LGRPO =−E πθold
h
min

ρθA,clip(ρ θ,1±ϵ)A

−β DKL

πθ ∥π θref
i
,
with ρθ =π θ(y|x)/π θold(y|x) and group-
relative advantageA= (r T −µ G)/σG.
2.3 Benchmarks and Models
Our primary benchmark isALFWorld(Shrid-
har et al., 2021), a text-based embodied environ-
ment in which the agent locates and interacts with
household objects to complete natural-language
tasks. It tests long-horizon planning and tracking
of action-conditioned state transitions. We use τ 2-
Bench(Barres et al., 2026) as a secondary test,
which is an interleaved tool-use environment in
which the agent alternates between tool calls and
dialogue with a simulated user.
Model preparation.We follow the training setup
of Yu et al. (2026): Qwen2.5-7B-Instruct (Qwen
Team, 2025a) for ALFWorld (Qwen3-8B (Qwen
Team, 2025b) forτ 2-Bench). The checkpoints stud-
ied throughout the paper are re-trained in this setup:
the base model, WMRL-only, PRL-only, and sequen-
tial WMRL→PRL . Full data, hyperparameter, and
prompting details are in Appendix A.1 and B.1.
Replicated performance.Table 1 reports ALF-
World results; our numbers track Yu et al. (2026).
See Appendix B.1 forτ 2-Bench replication.
Table 1: Replicated success rates on ALFWorld (%),
mean ± std over 3 seeds. Our numbers closely match Yu
et al. (2026).
Model ID OOD A VG
ReAct (base) 19.8±4.5 15.6±1.3 17.7±2.9
WMSFT5.0±1.0 2.1±1.5 3.5±1.2
WMRL33.6±3.4 31.8±5.3 32.7±3.3
PRL84.6±1.3 71.9±2.6 78.3±0.9
WMSFT→PRL66.4±1.3 55.2±2.0 60.8±1.5
WMRL→PRL87.0±0.4 81.8±0.7 84.4±0.3
3 Methodology
We first define several measures we use to study
the checkpoints mentioned.
∆-decomposition.Let θ0 denote the base-model
parameters. Following the task-vector formula-
tion of Ilharco et al. (2023), for each post-training
paradigm X∈ {WMSFT,WMRL,PRL,WMRL→
PRL} we obtain trained parameters θX and define
the additive update∆X =θ X −θ0. This yields four
primary deltas: ∆WMSFT, ∆WMRL, ∆PRL (PRL trained
directly from base), and ∆WMRL+PRL (the cumulative
update after sequential WMRL→PRL ). To isolate the
policy stage’s post-WMRL (conditional) contribution,
we further define
∆∆PRL = ∆WMRL+PRL −∆ WMRL (2)
so that (∆WMRL,∆∆ PRL) cleanly decomposes
the sequential pipeline. All deltas are com-
puted module-wise on the seven trainable lin-
ear projections of every transformer block
({q,k,v,o,up,gate,down}_proj ). Since all
checkpoints in our setting share the same archi-
tecture and pretrained initialization, their updates
also share a common coordinate system. This facil-
itates a more principled weight-space comparison
than for independently trained networks where pa-
rameter similarity can be distinct from functional
similarity. Additionally, prior work has shown that
for models fine-tuned from a common pretrained
base, linear operations on weights can correspond
predictably to linear changes in intermediate fea-
tures (Zhou et al., 2024), which offers further em-
pirical support for treating their parameter updates
as comparable objects.
3

Spectral interventions.For each module ∆∈
Rm×n we compute the SVD ∆ =UΣV ⊤ and then
compute derived quantities defined below.
Effective rank(Roy and Vetterli, 2007), how
broadly∆spreads across singular directions:
eRank(∆) = exp

−P i pi logp i  , pi =σ i  P j σj,
where σi are singular values of ∆ and pi is the
spectrum-normalized mass.
Truncated rank-k approximation.The Eckart–
Young best rank- k approximation (Eckart and
Young, 1936) ∆k =U :,1:k Σ1:k,1:k V ⊤ :,1:k gives a
coordinate-free notion of how much of an update’s
information lives in its top-k singular components.
Subspace projection.For two updates ∆A, ∆B
at the same module, let U (k) A and V (k) A denote the
leading k left and right singular vectors of ∆A.
Taking the left projection as an example, we con-
struct three projected variants of ∆B: parallel,
U (k) A U (k)⊤ A ∆B; orthogonal, (I−U (k) A U (k)⊤ A )∆B;
and random, R(k)R(k)⊤∆B, where R(k) is a ran-
dom orthonormalk-frame of matching dimension.
The reconstructed checkpoint θ0 + ∆ WMRL +
proj(∆∆PRL) (or +proj(∆PRL) in the independent
control) is then re-evaluated end-to-end.
Module-wise subspace overlap.For two leading-
k subspaces with orthonormal bases BA, BB, the
mean squared principal cosine 1 k P i σ2 i (B⊤ A BB)
measures alignment (random baseline ≈k/d ).
This is a standard principal-angle-based subspace
alignment measure (Björck and Golub, 1973).
Magnitude pruning of ∆.We also retain only
the top-P% of ∆ entries by absolute magnitude
(zeroing the rest), following task-vector merging
conventions (Yadav et al., 2023; Yu et al., 2024).
This complements the spectral analysis by operat-
ing in coordinate rather than singular-vector space.
Behavioral readouts.We complement the ge-
ometric analyses with per-token entropy of the
model’s distribution over theground-truthnext-
state tokens on a held-out WMRL evaluation set
(lower = better world-model calibration), and pair-
wise success-set overlap on the downstream task to
flag behavioral complementarity.
4 What makes a good world model?
Spectral signatures of effective
two-stage training (RQ1)
Figure 1 plots effective rank against success across
WM-stage checkpoints, observing thatwithin RL
0 10 20 30 40 50 60 70 80
AVG success rate (%)
1950
2000
2050
2100
2150
2200
2250
Average Effective Rank
WMRL (η = 0.8, anchor)
WMRL (η = 0.5)
WMRL (η = 0.9)
WMRL (expert data)
WMRL (multi-turn)
WMRL (LLM-judge reward)
WMSFT
PRL
WMRL→ PRL
WMSFT→ PRL
Effective rank vs AVG task success
WMRL variants
PRL variants
WMSFT
WMRL-only fit
(r = −0.81)
Figure 1: Effective rank vs. A VG success across WM-
stage checkpoints: a WMSFT baseline and a WMRL sweep
over reward threshold, judge type, data source, and pre-
diction format (Appendix A.2). Within WMRL, lower
effective rank tracks higher performance; WMSFT col-
lapses despite low rank.
regime, the strongest world model is low-rank.
However,WMSFToperates in a different regime.
WMSFT achieves lowest eRank of any checkpoint
yet performs catastrophically. WMSFT→PRL trails
WMRL→PRL by >20 A VG points. Thus, the two
regimes are not comparable spectrally; one pos-
sible explanation is that WMSFT concentrates up-
dates on surface textual patterns, vs. WMRL looking
for embedding-level semantic match and learning
dynamics-relevant directions. We defer testing this
hypothesis systematically to future work, but note
that this split echoes evidence that effective fine-
tuning updates concentrate in low-dimensional sub-
spaces (Aghajanyan et al., 2021; Hu et al., 2022)
and that RL post-training has a characteristic spec-
tral structure distinct from SFT (Zhu et al., 2025).
WMRL initialization broadens the directions
policy RL explores.Comparing ∆PRL against
∆WMRL+PRL, the WMRL-initialized pipeline shows sub-
stantially higher per-layer effective rank at every
depth, with the largest gap in the early-to-mid lay-
ers. We posit that the world-model stage opens
up directions in weight space that the policy stage
subsequently exploits—a geometric counterpart to
the behavioral claim that WMRL contributes comple-
mentary structure rather than redundant capacity.
The world-model update is functionally low-
rank.The low effective rank of strong WMRL
checkpoints has a functional counterpart: truncat-
ing ∆WMRL to its top singular components while
leaving ∆∆PRL intact incurs little performance cost.
4

Even a rank-1 truncation (a single outer product)
recovers within ≈10 points of the full sequential
pipeline, whereas the same truncation applied to
∆∆PRL or to ∆PRL collapses performance to near
the WMRL-only model at small k. The world-model
stage’s downstream value is therefore concentrated
in a handful of directions, while the policy update
spreads its task value more diffusely. We refer the
reader to Appendix A.5 for the full results.
5 Weight-space Relationship between
∆WMRL and the Policy Stage (RQ2)
Since WMRL and PRL leave deltas of different rank,
we ask whether the directions populated by the two
stages overlap or are disjoint. Is their relationship
more one ofcomplementarityor ofredundancy?
We identify two accounts that could explain the
observed two-stage WMRL→PRL performance gain:
Account A (shared / parallel).The policy stage refines,
compresses, or warm-starts from directions WMRL has al-
ready identified and thus its update sits largely within
∆WMRL’s subspace. If true, keeping only the ∆WMRL-aligned
component of∆∆ PRL should recover most of the gain.
Account B (orthogonal / complementary).The policy
stage complements WMRL, learning an update indifferent
directions of weight space. If true, most of ∆∆PRL’s task
value should lie in the orthogonal complement of ∆WMRL’s
leading directions.
We test both accounts through left/right subspace
projections of ∆∆PRL and ∆PRL (§5.1–5.2), and
module-wise principal-angle overlap (§5.4).
5.1 Left-space (Output-direction) Projection
We compute the SVD ∆WMRL =UΣV ⊤
and form Uk =U :,1:k. For each k∈
{1,25,50,150,250,500} , we replace ∆∆PRL with
one of three projected variants: projection
UkU ⊤ k ∆∆PRL, (I−U kU ⊤ k )∆∆PRL, RkR⊤ k ∆∆PRL
(parallel, orthogonal, random control). We then
re-evaluateθ 0 + ∆WMRL + proj(∆∆PRL).
Finding 1: Policy-stage output directions are
largely orthogonal to ∆WMRL.Removing ∆WMRL’s
top-k left-singular directions from ∆∆PRL has es-
sentially no cost on either split (Fig. 2, red hol-
low series): at k=500, ID 91.7 and OOD 84.9,
both at or slightly above the un-projected WMRL→
PRL baseline (ID 87.0, OOD 81.8). The bulk of
∆∆PRL’s task-relevant signal therefore lives out-
side∆ WMRL’s principaloutputsubspace.
Finding 2: ∆WMRL’s U directions carry only
marginal policy-relevant signal.Keeping only
∆WMRL’s top- k left-singular directions in ∆∆PRL
(red dashed series) recovers performance gradu-
ally, reaching ID 60.4 / OOD 56.8 at k=500. This
trails the orthogonal projection by ∼30 points on
bothsplits; a matched random projection (gray)
reaches ID 50.3 / OOD 49.5, only ∼8 points lower.
The output directions WMRL has populated are only
mildly enriched in policy-relevant information.
Finding 3: U-disjointness is likely intrinsic to
policy training, not only two-stage.The pattern
holds when we project ∆PRL (PRL trained directly
from base, never conditioned on ∆WMRL; blue se-
ries). Orthogonal projection preserves performance
(at k=500, ID 84.9 / OOD 77.6, vs. un-projected
PRL at ID 84.6 / OOD 71.9 – in fact slightlyabove
PRL on OOD). Parallel projection recovers only
ID 32.8 / OOD 32.3 at k=1 and ID 48.2 / OOD
55.2 at k=500. Because ∆PRL is computed inde-
pendently of ∆WMRL, the orthogonality cannot be a
consequence of sequential training; it likely reflects
an intrinsic difference between the preferredoutput
subspaces of policy and world-model learning. Per-
checkpoint numbers underlying Fig. 2 are reported
in Appendix A.4 (Tabs. 6 and 7).
5.2 Right-space (Input-feature) Projection
§5.1 only examinesoutputalignment. Two updates
can be orthogonal as matrices and still touch the
same input features, if the rotation between their
right bases happens to land on different columns
of U. We therefore repeat the analysis on the right
side, projecting onto ∆WMRL’s leadingrightsingular
vectors∆∆ PRL VkV ⊤ k and∆∆ PRL(I−V kV ⊤ k ).
Finding 4: In contrast, the two stagessharethe
right/V (input-feature) subspace.Parallelpro-
jection on the right (Fig. 3) is dramatically more
effective than on the left: ∆∆PRL projected onto
∆WMRL’s top right subspace gives ID 44.0 / OOD
40.6 at k=1 and climbs to ID 83.6 / OOD 79.7 at
k=500 – within a few points of the un-projected
WMRL→PRL baseline (ID 87.0 / OOD 81.8) on
both splits. The same operation on the left only
reached ID 60.4 / OOD 56.8 at k=500. The ran-
dom control stays near the WMRL baseline, ruling
out a generic rank- k effect. This suggests V∆WMRL
encodes task-relevant information.
Finding 5: Removing V from ∆PRL hurts
performance, but not for ∆∆PRL, suggesting
∆∆PRL learns robust V -redundant pathways.
For ∆∆PRL, removing ∆WMRL’s leading right singu-
5

1 5 25 50 100150 250 500
Projection rank k
0
20
40
60
80
100
ID success rate (%)
Left-space projection -- ID
1 5 25 50 100150 250 500
Projection rank k
0
20
40
60
80
100
OOD success rate (%)
Left-space projection -- OOD
WMRL→ PRL PRL ∆PRL
 ∆∆PRL
 ∆PRL
 ∆∆PRL
 ∆∆PRL rand.
Figure 2:Left-space (output-direction) projection on ALFWorld, reported separately on ID and OOD.The
two panels share a legend and overlay both projector variants on each policy update: parallel (dashed, filled
marker) keeps the ∆WMRL-aligned component; orthogonal (solid, hollow marker) keeps its complement. Blue series
correspond to ∆PRL, red to ∆∆PRL; gray is the random-subspace control for ∆∆PRL. Black dashed and dotted lines
denote WMRL→PRL and PRL baselines, respectively, with values taken from the same ID or OOD split as the panel.
lar directions barely hurts: ID 91.4→89.6 (nearly
flat) and OOD 82.8→77.6 (mild drop) from
k=1 to k=500. Taken with Finding 4, this sug-
gests that ∆∆PRL’s task value is redundant across
∆WMRL’s leading right directions and their comple-
ment rather than confined to either: removing one
side appears to leave a functioning input pathway
on the other. However, on∆PRL, removing the same
directions makes performance drop from ID 87.0 /
OOD 79.7 at k=1 to ID 65.9 / OOD 66.2 at k=500,
well below the un-projectedPRL baseline (ID 84.6 /
OOD 71.9) on both splits. Because ∆PRL is trained
directly from base with no exposure to ∆WMRL, we
infer that PRL-from-base independently discovers
a subspace that overlaps with ∆WMRL’s, to the point
that projecting ∆WMRL’s right directions out of ∆PRL
removes content the policy update needs to func-
tion. This adds evidence for Account A on the right
side. Per-checkpoint numbers underlying Fig. 3 are
in Appendix A.4 (Tabs. 8 and 9).
5.3 A Unified View of Two-stage Agentic
Post-Training Geometry
Together, these results point toward a coherent pic-
ture of how the two stages interact:∆ WMRL concen-
trates its update in a low-rank right subspace V
that also contains the policy stage’s task-relevant
input signal (Finding 4), policy training (even inde-
pendently) writes outputs in U-directions disjoint
from WMRL (Findings 1–3), andsequential training
composes the two components without geomet-
ric interference(Finding 5). In other words, the
geometrically identifiable value of sequential train-
ing is primarily V -redundancy in the downstream
policy ∆. Accounts A and B thus holdin tandem
on different sides. Though this establishes their
weight-space roles, it does not explain how these
differences manifest at deployment, or what com-
plementarity accomplishes behaviorally. We next
seek behavioral evidence to fill out this picture.
5.4 Module-wise Subspace Overlap
We show in Fig. 4 that the global picture also holds
at the module level. For every pair of corresponding
weight matrices in ∆PRL and ∆∆PRL, we compute
the principal-angle overlap ¯σ2 = 1 k P i σ2 i (B⊤ A BB)
between their leading- k left (or right) subspaces.
The top panel shows the left-side overlap ( k=1,
mean 0.04), nearly orthogonal, while the bottom
panel shows the right-side overlap ( k=1, mean
0.63), highly aligned at dominant input direction.
5.5 Cross-Benchmark Replication
On τ 2-Bench (with Qwen3-8B), the U-disjoint and
V -shared geometric pattern replicates. Rank-1 left-
subspace overlap remains near-zero, whereas the
right-subspace overlap appears even more strongly
than on ALFWorld. However, this is associated
more modestly with end-to-end projection per-
formance. The right-parallel projection recovers
71.8% of oracle improvement on ALFWorld vs.
46.9% on τ 2-Bench, and we thus interpret the geo-
metric replication as stronger than the behavioral
evidence (full results in Appendix B).
6

1 25 50 150 250 500
Projection rank k
0
20
40
60
80
100
ID success rate (%)
Right-space projection -- ID
1 25 50 150 250 500
Projection rank k
0
20
40
60
80
100
OOD success rate (%)
Right-space projection -- OOD
WMRL→ PRL PRL ∆PRL
 ∆∆PRL
 ∆PRL
 ∆∆PRL
 ∆∆PRL rand.
Figure 3:Right-space (input-feature) projection on ALFWorld, reported separately on ID and OOD.Same
plotting conventions as Fig. 2: the two panels share a legend; parallel projection is shown with dashed filled markers,
and orthogonal projection with solid hollow markers. Blue series correspond to ∆PRL, red to ∆∆PRL, and gray to
the random-subspace control. Black dashed and dotted lines denote WMRL→PRL and PRL baselines, respectively.
The picture is mirrored relative to the left: orthogonal removal hurts ∆PRL monotonically with k, while parallel
projection of∆∆ PRL recovers most of theWMRL→PRLbaseline byk=500on both splits.
q
k
v
o
up
gate
down
Left rank-1 subspace overlap
0 4 8 12 16 20 24
Layer
q
k
v
o
up
gate
down
Right rank-1 subspace overlap
0.0
0.5
1.0
Figure 4:Module-wise rank- 1 subspace overlapbe-
tween ∆PRL and ∆∆PRL on the left (output) vs. right
(input-feature) side.
6 How doesWMRLhelp in practice? A
rollout-time behavioral account (RQ1)
The geometric findings raise a behavioral question:
what does the WMRL-derived structure let the agent
do that PRL alone cannot? We probe this through
success-set overlap and rollout-time statistics.
Success-set overlap.For each pair of check-
points we compare tasks solved at pass@1 (Fig. 5).
The composite WMRL→PRL model doesnotsub-
sume either WMRL’s or PRL’s success set: each
solves a non-trivial number of tasks WMRL→PRL
fails on, while WMRL→PRL itself picks up new suc-
cesses that neither base achieves. This non-nesting
rules out the simplest reading, i.e. that WMRL→PRL
is simply a refined version of PRL, since refinement
would predict success-set containment. This sug-
Base WMRL PRL
WMRL→PRL
Base
WMRL
PRL
WMRL→ PRL
27
18 64
23 58 154
27 61 139 163
Pairwise success overlap @ pass@1 (N = 192)
Figure 5: Success-set overlap at pass@1 on ALFWorld.
Diagonal = #samples a model passes; off-diagonal =
#samples both pass.
gests that what the second stage is doing on top of
WMRL is not a near-copy of what PRL does on its
own and instead points to synergistic effects.
Exploration statistics.Table 2 reports per-task
averages of unique valid actions, unique observa-
tion states, and total turns across rollouts, with each
run capped at 30 turns. Uniqueness is computed by
exact string match, and an action is valid only if it
changes the environment state. We also report the
three-run union as a cross-check.
WMRL does not improve unique-action coverage
over the base model, but maintains broaderstate
exploration. PRL, in contrast, sharply contracts
both action and state coverage in exchange for
shorter, more focused trajectories. The compos-
ite WMRL→PRL inherits PRL’s efficiency (similar
turn count) while recovering some of WMRL’s state-
coverage advantage, suggesting that the exploration
benefit of WMRL is preservedbehaviorallythrough
7

Table 2: Exploration statistics on ALFWorld (ID+OOD,
N=192). We report per-task averages of unique valid
actions, unique states, and total turns.
Pass@1 Pass@3 Union
ModelN act Nstate TurnsN act Nstate Turns
Base 10.8 14.8 28.0 18.3 26.7 82.0
WMRL7.8 13.5 24.9 13.3 26.5 74.6
PRL7.1 8.1 12.6 8.8 10.3 37.7
WMRL→PRL8.4 9.7 12.4 11.6 13.9 37.5
the policy stage. This rules out WMRL→PRL being
simply a more efficient WMRL or a more reward-
optimized PRL since each of the baselines lacks
one of the two behavioral axes the composite has.
Base SFT WMRL PRL
WMRL→PRL SFT→PRL
0.0
0.5
1.0
1.5
Per-token entropy
WM prediction entropy
Figure 6: Per-token entropy of each checkpoint’s distri-
bution over theground-truthnext-state tokens, evaluated
on the WMRL held-out test set (N=512 single-turn tran-
sitions) and averaged per sample.
Next-state prediction entropy on held-out WM
set.Fig. 6 reports per-token entropy on a held-
out WMRL evaluation set, scored against theground-
truthnext-state tokens. The prompt is slightly re-
vised to directly predict the next state without think-
ing for fair comparison, same as WMSFT. Lower in-
dicates the models are better calibrated as a world
model. We observe (i) WMRL reduces next-state en-
tropy relative to base, i.e. WMRL training makes the
model a more calibrated next-state predictor, con-
sistent with its training objective (ii)PRL-from-base
degradesnext-state calibration, by itself actively
pushing the modelawayfrom accurate next-state
prediction, and (iii) WMRL→PRL preserves most
of WMRL’s improvement. Here, the second-stage
policy update doesnoterase the calibration that the
first-stageWMRLupdate put in place.
SummaryTaken together, the three behavioral
findings point in the same direction: WMRL→PRL
is an effective combination of two qualitatively dif-
ferent stages. The non-nested success sets show
this at thetasklevel (each baseline solves tasks the
composite misses, and vice versa). The exploration
statistics show it at thetrajectorylevel (the com-
posite combines WMRL’s state coverage with PRL’s
efficiency). Finally, the entropy results show it at
therepresentationallevel (the composite retains
the WM calibration that PRL-from-base implicitly
degrades). We hypothesize that these three patterns
areplausible(observational) behavioral correlates
of the §5 geometry, in which the two stages write
to disjoint output subspaces (Findings 1–3) while
sharing input subspaces (Finding 4), although we
cannot directly establish a causal relationship. This
connection is most direct for entropy preservation,
since orthogonal weight updates do not overwrite
each other’s columns by construction. Though
these properties are not uniquely predicted by the
geometric patterns, they point toward future causal
investigations to better characterize such effects.
7 Preserving the World Model (RQ3)
The asymmetric geometry of §5 predicts that gentle
preservation of ∆WMRL during policy training could
help performance, and that extra world-model sig-
nal should compose constructively with the policy
update. We test this assumption with two interven-
tions, one training-free and one training-time (for
full details, refer to Appendix C):
Training-free: KnOTS / TIES merging of
MWMRL and the policy model.We additively
merge MWMRL with either MPRL (PRL from base) or
MWMRL+PRL (sequential WMRL→PRL ) via TIES (Ya-
dav et al., 2023) and KnOTS (Stoica et al., 2025).
KnOTS factors out a singular basis shared across
tasks before applying the TIES mask; since our
geometry has V shared and U disjoint, we test both
the defaultU-sharing and aV-sharing variant.
Training-based: online WM-SFT during PRL.
During the second stage we additionally subsample
32 realized transitions from each step’s rollouts to
compute a next-state SFT loss on top of the policy
gradient, mirroring the ECHO recipe of concurrent
work by Shrivastava et al. (2026), which learns a
world model “for free” inside terminal-agent RL.
Interventions improve over the untreated
WMRL→PRL baseline.On (MWMRL, MPRL),
KnOTS-V beats KnOTS-U by +2.0 (+4.2 OOD),
matching the V -shared/U-disjoint prediction: fac-
toring out the basis that the two tasks actually share
(V ) preserves signal that the U basis variant loses.
8

Table 3: Preservation interventions on ALFWorld. For
each base pair (PRL or WMRL→PRL as the second task)
we list the source checkpoints, plain TIES merging, and
KnOTS-TIES in both the default U-sharing and our V -
sharing variant. The bottom row is the training-based on-
line WMSFT auxiliary loss during PRL.Bold/ underlined
indicates the best/baseline results within each sub-block.
Method ID OOD A VG
base 19.8±4.5 15.6±1.3 17.7±2.9
WMRL33.6±3.4 31.8±5.3 32.7±3.3
PRL84.6±1.3 71.9±2.6 78.3±0.9
training free
TIES 85.0±1.7 72.6±1.2 78.8±0.5
KnOTS (U)88.0±0.774.5±3.2 81.2±1.7
KnOTS(V) 87.8±2.278.7±1.9 83.2±1.9
WMRL→PRL87.0±0.4 81.8±0.7 84.4±0.3
training free
TIES 87.5±1.3 82.0±0.4 84.8±1.0
KnOTS(U) 89.8±1.182.8±1.3 86.3±0.3
KnOTS(V) 90.1±1.0 81.8±1.9 85.9±0.7
training based
OnlineWMSFT90.4±0.479.5±0.7 85.0±0.5
On (MWMRL, MWMRL+PRL), the V /U gap flips but is
very close; because ∆WMRL+PRL = ∆WMRL + ∆∆PRL
already incorporates ∆WMRL, reducing the effect of
the basis choice. Both merge variants still sit ∼2
points above the untreated baseline on ALFWorld.
Finally, online WMSFT during PRL reaches the high-
est ID ( 90.4) but trails on OOD ( 79.5). The two
interventions therefore complement each other: a
training-free merger built on the right geometric
basis (V ) recovers most of the gain without any fur-
ther optimization, and a light training-time WMSFT
signal further improves ID performance.
8 Conclusion
The composition of world models and policies is
moving from an emergent property of large models
to an explicit training criterion. This shift opens
two questions. One isengineering: how should
the stages be combined to produce capable agents?
The other is scientific: how does a single network
meaningfully compose both kinds of knowledge,
and what structural properties does this produce?
We offer an initial pathway for investigating both.
In our experiments, we find that world-model and
policy training share input-feature directions and
write to largely distinct output directions, and also
that sequential training makes the resulting policy
less dependent on the world model’s leading input
directions. These findings suggest ways forward
for both investigating and engineering how these
two stages compose.
Limitations.Our analysis is empirical and con-
fined to two text-only agent benchmarks and two
Qwen2.5/Qwen3 models. This setting is less gen-
eral than more realistic web- or computer-use
agents, which often require vision-language per-
ception, grounding, and interaction. We thus view
our work as a first exploration of these phenomena.
However, world-model training and evaluation for
multimodal agents remain comparatively immature,
making text-only environments a useful controlled
setting for isolating the geometry of world-model
preservation. The left/right asymmetry we iden-
tify is robust across modules and depths within
these settings, but its mechanistic origin remains
open. One possible contributor is a difference be-
tween target distributions of world-model and pol-
icy training. However, this pattern also appears
on τ 2-Bench, where both of these stages contain
natural-language dialogue and tool-related content.
Still, our experiments cannot yet isolate the contri-
bution of target-distribution differences.
We also restrict our analysis to additive parame-
ter updates relative to a single base model; extend-
ing the framework to LoRA-style decomposed up-
dates (Hu et al., 2022) is a natural next step. Mean-
while, our interventions are module-wise but apply
the same intervention to all modules. Stronger
causal tests, such as cross-module analysis (Wang
et al., 2023), layer-local editing (Geva et al., 2021),
activation patching (Meng et al., 2022), or training-
time constraints on the U/V subspaces (Zou et al.,
2025), are left for future work.
Finally, our preservation experiments instantiate
only a small part of the design space suggested by
the geometry. We evaluate KnOTS/TIES merg-
ing and an online WM-SFT auxiliary loss, but
do not extensively tune merge hyperparameters;
on τ 2-Bench, we replicate only the training-free
merge experiments due to the cost of running on-
line WMSFT. More scalable preservation methods
and broader benchmark/model coverage remain im-
portant next steps. We hope this exploratory study
motivates more systematic investigations of world-
model preservation through geometry, especially in
multimodal agents, and inspires scalable methods
for boosting agentic post-training.
9

References
Armen Aghajanyan, Sonal Gupta, and Luke Zettle-
moyer. 2021. Intrinsic dimensionality explains the
effectiveness of language model fine-tuning. InAn-
nual Meeting of the Association for Computational
Linguistics (ACL).
Saleh Ashkboos, Maximilian L. Croci, Marcelo Gen-
nari do Nascimento, Torsten Hoefler, and James
Hensman. 2024. SliceGPT: Compress large lan-
guage models by deleting rows and columns. In
International Conference on Learning Representa-
tions (ICLR).
Victor Barres, Honghua Dong, Soham Ray, Xujie Si,
and Karthik R Narasimhan. 2026. τ 2-Bench: Eval-
uating conversational agents in a dual-control envi-
ronment. InForty-third International Conference on
Machine Learning.
Åke Björck and Gene H. Golub. 1973. Numerical meth-
ods for computing angles between linear subspaces.
Mathematics of Computation, 27(123):579–594.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming
Yuan, Henrique Ponde de Oliveira Pinto, Jared Ka-
plan, Harri Edwards, Yuri Burda, Nicholas Joseph,
Greg Brockman, et al. 2021. Evaluating large
language models trained on code.arXiv preprint
arXiv:2107.03374.
Shiqi Chen, Tongyao Zhu, Zian Wang, Jinghan Zhang,
Kangrui Wang, Siyang Gao, Teng Xiao, Yee Whye
Teh, Junxian He, and Manling Li. 2025. Internalizing
world models via self-play finetuning for agentic RL.
arXiv preprint arXiv:2510.15047.
Emily L. Denton, Wojciech Zaremba, Joan Bruna, Yann
LeCun, and Rob Fergus. 2014. Exploiting linear
structure within convolutional networks for efficient
evaluation. InAdvances in Neural Information Pro-
cessing Systems (NeurIPS).
Carl Eckart and Gale Young. 1936. The approximation
of one matrix by another of lower rank.Psychome-
trika, 1(3):211–218.
Lang Feng, Zhenghai Xue, Tingcong Liu, and Bo An.
2025. Group-in-group policy optimization for LLM
agent training. InThe Thirty-ninth Annual Confer-
ence on Neural Information Processing Systems.
Jonathan Frankle and Michael Carbin. 2019. The lottery
ticket hypothesis: Finding sparse, trainable neural
networks. InInternational Conference on Learning
Representations (ICLR).
Elias Frantar and Dan Alistarh. 2023. SparseGPT: Mas-
sive language models can be accurately pruned in
one-shot. InInternational Conference on Machine
Learning (ICML).
Mor Geva, Roei Schuster, Jonathan Berant, and Omer
Levy. 2021. Transformer feed-forward layers are key-
value memories. InProceedings of the 2021 Confer-
ence on Empirical Methods in Natural Language Pro-
cessing, pages 5484–5495, Online and Punta Cana,
Dominican Republic. Association for Computational
Linguistics.
Lin Guan, Karthik Valmeekam, Sarath Sreedharan,
and Subbarao Kambhampati. 2023. Leveraging pre-
trained large language models to construct and utilize
world models for model-based task planning.Ad-
vances in Neural Information Processing Systems,
36:79081–79094.
David Ha and Jürgen Schmidhuber. 2018. Recurrent
world models facilitate policy evolution. InAdvances
in Neural Information Processing Systems (NeurIPS).
Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, and
Timothy Lillicrap. 2023. Mastering diverse do-
mains through world models.arXiv preprint
arXiv:2301.04104.
Song Han, Jeff Pool, John Tran, and William J. Dally.
2015. Learning both weights and connections for
efficient neural networks. InAdvances in Neural
Information Processing Systems (NeurIPS).
Edward J Hu, yelong shen, Phillip Wallis, Zeyuan Allen-
Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu
Chen. 2022. LoRA: Low-rank adaptation of large
language models. InInternational Conference on
Learning Representations.
Gabriel Ilharco, Marco Tulio Ribeiro, Mitchell Worts-
man, Ludwig Schmidt, Hannaneh Hajishirzi, and Ali
Farhadi. 2023. Editing models with task arithmetic.
InThe Eleventh International Conference on Learn-
ing Representations.
Kenneth Li, Aspen K Hopkins, David Bau, Fernanda
Viégas, Hanspeter Pfister, and Martin Wattenberg.
2023. Emergent world representations: Exploring
a sequence model trained on a synthetic task. In
The Eleventh International Conference on Learning
Representations.
Xinyin Ma, Gongfan Fang, and Xinchao Wang. 2023.
LLM-Pruner: On the structural pruning of large lan-
guage models. InAdvances in Neural Information
Processing Systems (NeurIPS).
Kevin Meng, David Bau, Alex Andonian, and Yonatan
Belinkov. 2022. Locating and editing factual asso-
ciations in GPT.Advances in Neural Information
Processing Systems, 36. ArXiv:2202.05262.
Qwen Team. 2025a. Qwen2.5 technical report.arXiv
preprint arXiv:2412.15115.
Qwen Team. 2025b. Qwen3 technical report.arXiv
preprint arXiv:2505.09388.
Olivier Roy and Martin Vetterli. 2007. The effective
rank: A measure of effective dimensionality.Eu-
ropean Signal Processing Conference (EUSIPCO),
pages 606–610.
10

Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu,
Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan
Zhang, Y . K. Li, Yu Wu, and Daya Guo. 2024.
DeepSeekMath: Pushing the limits of mathematical
reasoning in open language models.arXiv preprint
arXiv:2402.03300.
Pratyusha Sharma, Jordan T. Ash, and Dipendra Misra.
2024. The truth is in there: Improving reasoning in
language models with layer-selective rank reduction.
InInternational Conference on Learning Representa-
tions (ICLR).
Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté,
Yonatan Bisk, Adam Trischler, and Matthew
Hausknecht. 2021. ALFWorld: Aligning text and
embodied environments for interactive learning. In
International Conference on Learning Representa-
tions (ICLR).
Vaishnavi Shrivastava, Piero Kauffmann, Ahmed
Awadallah, and Dimitris Papailiopoulos. 2026.
Echo: Terminal agents learn world models for free.
Preprint, arXiv:2605.24517.
George Stoica, Pratik Ramesh, Boglarka Ecsedi,
Leshem Choshen, and Judy Hoffman. 2025. Model
merging with SVD to tie the knots. InThe Thirteenth
International Conference on Learning Representa-
tions.
Mingjie Sun, Zhuang Liu, Anna Bair, and J. Zico Kolter.
2024. A simple and effective pruning approach for
large language models. InInternational Conference
on Learning Representations (ICLR).
Richard S. Sutton and Andrew G. Barto. 2018.Rein-
forcement Learning: An Introduction, 2nd edition.
MIT Press.
Shubham Toshniwal, Sam Wiseman, Karen Livescu,
and Kevin Gimpel. 2022. Chess as a testbed for
language model state tracking. InProceedings of
the AAAI Conference on Artificial Intelligence, vol-
ume 36, pages 11385–11393.
Keyon Vafa, Justin Y Chen, Ashesh Rambachan, Jon
Kleinberg, and Sendhil Mullainathan. 2024. Evaluat-
ing the world model implicit in a generative model.
Advances in Neural Information Processing Systems,
37:26941–26975.
Kevin Ro Wang, Alexandre Variengien, Arthur Conmy,
Buck Shlegeris, and Jacob Steinhardt. 2023. Inter-
pretability in the wild: a circuit for indirect object
identification in GPT-2 small. InThe Eleventh Inter-
national Conference on Learning Representations.
Prateek Yadav, Derek Tam, Leshem Choshen, Colin
Raffel, and Mohit Bansal. 2023. TIES-merging: Re-
solving interference when merging models. InAd-
vances in Neural Information Processing Systems
(NeurIPS).
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik Narasimhan, and Yuan Cao. 2023.
ReAct: Synergizing reasoning and acting in language
models. InInternational Conference on Learning
Representations (ICLR).
Le Yu, Bowen Yu, Haiyang Yu, Fei Huang, and Yongbin
Li. 2024. Language models are super Mario: Absorb-
ing abilities from homologous models as a free lunch.
InInternational Conference on Machine Learning
(ICML).
Xiao Yu, Baolin Peng, Michel Galley, Hao Cheng,
Qingyu Wu, Janardhan Kulkarni, Suman Nath, Zhou
Yu, and Jianfeng Gao. 2025a. Dyna-Mind: Learn-
ing to simulate from experience for better AI agents.
arXiv preprint arXiv:2510.09577.
Xiao Yu, Baolin Peng, Ruize Xu, Michel Galley, Hao
Cheng, Suman Nath, Jianfeng Gao, and Zhou Yu.
2025b. Dyna-Think: Synergizing reasoning, acting,
and world model simulation in AI agents.arXiv
preprint arXiv:2506.00320.
Xiao Yu, Baolin Peng, Ruize Xu, Yelong Shen,
Pengcheng He, Suman Nath, Nikhil Singh, Jian-
feng Gao, and Zhou Yu. 2026. Reinforcement
world model learning for LLM-based agents.arXiv
preprint arXiv:2602.05842.
Kai Zhang, Xiangchao Chen, Bo Liu, Tianci Xue,
Zeyi Liao, Zhihan Liu, Xiyao Wang, Yuting Ning,
Zhaorun Chen, Xiaohan Fu, Jian Xie, Yuxuan Sun,
Boyu Gou, Qi Qi, Zihang Meng, Jianwei Yang, Ning
Zhang, Xian Li, Ashish Shah, et al. 2026. Agent
learning via early experience. InForty-third Interna-
tional Conference on Machine Learning.
Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang,
Huan Lin, Baosong Yang, Pengjun Xie, An Yang,
Dayiheng Liu, Junyang Lin, Fei Huang, and Jingren
Zhou. 2025. Qwen3 embedding: Advancing text
embedding and reranking through foundation models.
arXiv preprint arXiv:2506.05176.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric Xing, et al. 2023.
Judging llm-as-a-judge with mt-bench and chatbot
arena.Advances in neural information processing
systems, 36:46595–46623.
Zhanpeng Zhou, Zijun Chen, Yilan Chen, Bo Zhang,
and Junchi Yan. 2024. On the emergence of cross-
task linearity in pretraining-finetuning paradigm.
InForty-first International Conference on Machine
Learning.
Hanqing Zhu, Zhenyu Zhang, Hanxian Huang, Dachuan
Su, Zhangyang Liu, Jiawei Zhao, Igor Fedorov,
Hamed Pirsiavash, Jinwoo Lee, David Z. Pan,
Zhangyang Wang, Yuandong Tian, and Kai Sheng
Tai. 2025. The path not taken: RLVR provably learns
off the principals. InNeurIPS Workshop on Efficient
Reasoning.
11

Andy Zou, Long Phan, Sarah Chen, James Campbell,
Phillip Guo, Richard Ren, Alexander Pan, Xuwang
Yin, Mantas Mazeika, Ann-Kathrin Dombrowski,
Shashwat Goel, Nathaniel Li, Michael J. Byun, Zifan
Wang, Alex Mallen, Steven Basart, Sanmi Koyejo,
Dawn Song, Matt Fredrikson, et al. 2025. Repre-
sentation engineering: A top-down approach to ai
transparency.Preprint, arXiv:2310.01405.
A ALFWorld: Implementation Details
and Extended Results
This appendix collects (i) implementation details
and hyperparameters for the ALFWorld experi-
ments, (ii) the WMRL configuration sweep that pro-
duced the cluster of checkpoints in Fig. 1, (iii)
the module-level effective-rank breakdown, (iv)
magnitude-pruning controls referenced in §A.5,
and (v) the full per-checkpoint performance tables
behind the projection and pruning figures in the
main text. Throughout we follow the experimen-
tal setup of Yu et al. (2026) as closely as possible:
all checkpoints are trained from publicly released
base models with GRPO for both theWMRL and PRL
stages.
A.1 Training and Reproduction Setup
Base model and data.We start from Qwen2.5-
7B-Instruct (Qwen Team, 2025a). The WMRL train-
ing corpus is collected by rolling out the base
model on the official ALFWorld training split
(N=3 trajectories per task, temperature 1.0, max
30 steps), converting trajectories into per-step tran-
sition triplets ⟨st−H:t , at, st+1⟩, and discarding
samples with invalid actions. Following Yu et al.
(2026), we fix H= 2 for training efficiency and
perform SFT with a held-out split to get a filter
model, which we then use to subsample “too-easy”
triplets retaining ∼30% of the original. The data
size is∼16K.
Sim-to-real reward.We use Qwen3-Embedding-
8B (Zhang et al., 2025) as the frozen encoder E(·)
with cosine-similarity thresholdη= 0.8.
WMRL stage. 2 epochs, learning rate 1e−6, effec-
tive batch size 32, GRPO group size 8. Each check-
point is trained on two NVIDIA H200 GPUs for
around 8 hours.
PRL stage.GRPO with terminal task-success re-
ward, discount γ= 1.0 , maximum 15 steps per
episode during training, 300 update steps, group
size 8. We use the official repo of Verl-Agent (Feng
et al., 2025) for the multi-turn training 1. Each
checkpoint is trained on two NVIDIA H200 GPUs
for around 30 hours.
A.2WMRLSetting Sweep
To probe how sensitive WMRL is to its training-time
choices—and to assemble the cluster of WMRL con-
figurations plotted in Fig. 1—we sweep along four
axes with anchor values ( η= 0.8 , self-rollouts,
single-turn prediction, binarized embedding score):
• Reward threshold η∈ {0.5,0.8,0.9}, control-
ling how strict the similarity criterion is.
• Data source: self-rollouts vs. expert demon-
strations from ALFWorld official data.
• Prediction format: single-turn vs. three con-
secutive steps’ predictions with averaged re-
ward (multi-state predictions with multiple cor-
responding actions provided)
• Judge category: LLM-as-judge (Zheng et al.,
2023) with Qwen3-235B-A22B-Instruct vs.
Qwen3-8B embedding score.
Table 4: WMRL setting sweep on ALFWorld (%, A VG).
Each row reports the standalone WMRL checkpoint and
the downstreamWMRL→PRLpipeline.
SettingWMRL WMRL→PRL
Anchor
- 32.7±3.3 84.4±0.3
Reward threshold
η= 0.510.2±3.4 71.9±2.0
η= 0.918.2±2.6 76.1±0.8
Data source
Expert demonstrations 16.4±3.4 74.0±1.3
Prediction format
Multi-turn 21.5±1.2 75.6±3.1
Judge Category
LLM-as-a-Judge 17.2±2.8 78.7±1.9
A.3 Per-layer Spectral Picture of the Pipeline
At every layer, the post-training updates show a
clear spectral separation: ∆WMRL above ∆WMRL+PRL
above ∆PRL, with ∆WMSFT far below all three
(Fig. 7). We use this layer-wise ordering primar-
ily for descriptive context since many plausible
accounts (e.g., shared gradient dynamics across
modules) would predict module-wise consistency.
1https://github.com/langfengq/verl-agent
12

0 5 10 15 20 25
Layer
1850
1900
1950
2000
2050
2100
2150
Average Effective Rank
WMRL
PolicyRL
WMSFT
WMSFT+PolicyRL
WMRL+PolicyRL
Effective Rank per Layer
Figure 7: Per-layer effective rank of the parameter up-
dates produced by each post-training paradigm, aver-
aged across modules. The ordering of paradigms is
preserved across depth.
A.4 Full Performance Tables for the
Projection
The main text reports ID and OOD success rates
separately for the projection (§5) and pruning
(§A.5, Appendix A.6) experiments. For complete-
ness, this appendix collects the full ID, OOD, and
A VG (= Unweighted mean over ID and OOD) num-
bers for every checkpoint used in those analyses,
shown as the mean± standard deviation over3 roll-
out repeats. Baselines from Tab. 1 are reproduced
in Tab. 5 for convenience.
Table 5: ALFWorld baseline reference checkpoints (re-
produced from Tab. 1 for cross-reference).
ckpt ID OOD A VG
ReAct(base) 19.8±4.5 15.6±1.3 17.7±2.9
WMSFT5.0±1.0 2.1±1.5 3.5±1.2
WMRL33.6±3.4 31.8±5.3 32.7±3.3
PRL84.6±1.3 71.9±2.6 78.3±0.9
WMSFT+PRL66.4±1.3 55.2±2.0 60.8±1.5
WMRL+PRL87.0±0.4 81.8±0.7 84.4±0.3
Left-space projection (§5.1).Tab. 6 reports
∆PRL projected onto ∆WMRL’s top-k left singular sub-
space; Tab. 7 reports ∆∆PRL projected onto the
same.
Right-space projection (§5.2).Tab. 8 reports
∆PRL projected onto ∆WMRL’s top-k right singular
subspace; Tab. 9 reports the same for∆∆ PRL.
1 25 50 250 500
Projection rank k
0
20
40
60
80
100
AVG success rate (%)
Truncated rank-k pruning
WMRL→ PRL
PRL
WkP
WPk
WkPk
Pk
Figure 8:Rank- k truncation pruning of ∆s.Across
k∈ {1,25,50,250,500} , pruning ∆WMRL is nearly
harmless, whereas pruning ∆∆PRL or ∆PRL causes a
sharp small-rank drop.
A.5 Robustness Check: rank-kPruning
Experiments
The geometric picture of §5 –∆WMRL suggests a low-
rank, input-aligned scaffold that the policy stage
builds on through output-orthogonal directions –
makes a prediction about each stage’s update in iso-
lation: ∆WMRL should be highly truncation-tolerant,
while ∆PRL – a from-base update that has to redis-
cover the same hypothetical scaffold – should not
be. We test these predictions through rank-k trun-
cation, following prior work on low-rank approxi-
mations of neural network weights for compression
and adaptation (Denton et al., 2014; Aghajanyan
et al., 2021; Hu et al., 2022) and on rank-based com-
pression of LLM weights (Ashkboos et al., 2024;
Sharma et al., 2024).
Concretely, for each k and each ∆∈
{∆WMRL,∆∆ PRL,∆ PRL} we form the truncated
rank-k approximation ∆k and evaluate four vari-
ants: WkP, which prunes ∆WMRL only; WPk, which
prunes ∆∆PRL only; WkPk, which prunes both up-
dates; and Pk, which directly prunes the from-base
update ∆PRL. Tab. 10 reports the per-k ID, OOD,
and A VG numbers for the four rank-truncation
regimes and Fig. 8 displays the trend.
∆WMRL is highly compressible. WkP is almost flat
across ranks (Fig. 8): even replacing ∆WMRL by
its rank-1 truncation while keeping ∆∆PRL intact
yields ID 77.6 / OOD 79.7, within ∼10 points of
the full WMRL→PRL model (ID 87.0, OOD 81.8).
Thus, most of the downstream utility of the WM
stage is concentrated in very few directions.
13

Table 6: Left-space projection of ∆PRL onto ∆WMRL. Composition: θ0 + projL(∆PRL). We report performance for
the parallel component (U U⊤∆PRL) and the orthogonal component ((I−U U ⊤)∆PRL).
parallel orthogonal
kID OOD A VG ID OOD A VG
1 32.8±1.1 32.3±4.5 32.5±2.7 86.5±1.3 78.7±3.2 82.5±2.2
25 38.0±2.6 39.6±0.7 38.8±1.5 86.5±0.7 78.1±2.2 82.3±0.7
50 40.4±4.5 35.4±1.9 37.9±1.7 86.2±0.4 77.1±1.9 81.6±0.8
150 42.7±1.3 42.7±5.9 42.7±3.2 86.7±0.6 78.1±1.3 82.4±1.0
250 45.0±2.6 42.7±6.4 43.9±3.1 87.0±2.0 81.8±3.2 84.4±2.6
500 48.2±1.0 55.2±5.2 51.7±2.7 84.9±0.7 77.6±0.7 81.2±0.6
Table 7: Left-space projection of ∆∆PRL onto ∆WMRL. Composition: θ0 + ∆WMRL + proj L(∆∆PRL). Columns
report the parallel component (U U⊤∆∆PRL), orthogonal component ((I−U U ⊤)∆∆PRL), and random projection
(QQ⊤∆∆PRL withQrandom orthonormal).
parallel orthogonal random
kID OOD A VG ID OOD A VG ID OOD A VG
1 33.5±1.2 30.4±2.3 32.0±0.8 88.5±2.2 83.8±2.7 86.2±1.0 34.9±3.2 31.8±4.1 33.3±1.5
5 34.6±1.9 31.2±5.6 32.9±3.5 87.5±1.1 83.3±1.5 85.4±1.1 29.9±1.6 34.9±1.9 32.4±1.7
25 34.6±1.0 33.3±6.5 34.0±3.4 87.0±2.0 81.8±3.2 84.4±1.7 28.9±1.9 34.4±7.8 31.6±3.9
50 38.3±2.8 36.5±5.8 37.4±4.2 89.8±1.7 83.3±1.5 86.6±0.7 34.4±3.4 30.2±3.9 32.3±1.0
100 44.3±1.5 38.5±3.9 41.4±2.2 90.6±2.2 83.8±1.9 87.2±2.0 34.6±1.3 33.3±4.8 34.0±2.2
150 49.5±2.4 40.6±3.8 45.0±1.2 91.2±1.0 83.3±3.2 87.2±2.1 35.4±2.2 34.9±3.9 35.2±2.6
250 51.0±3.0 46.9±5.8 49.0±3.3 91.9±0.7 85.4±0.7 88.7±0.6 41.4±2.2 41.1±5.2 41.3±3.7
500 60.4±2.4 56.8±1.9 58.6±1.8 91.7±1.6 84.9±0.7 88.3±1.1 50.3±0.4 49.5±5.8 49.9±2.7
∆∆PRL and ∆PRL require higher rank.In con-
trast, WPk drops to ID 43.8 / OOD 46.4 at k=1
and recovers only by moderate ranks, showing that
∆∆PRL spreads its task value across many singular
components. WkPk closely tracks WPk, indicating
that ∆∆PRL, rather than ∆WMRL, is the bottleneck.
The direct from-base update is densest: Pk is worst
at every k, with rank-1 performance near the WMRL-
only model and rank 500 only matching unpruned
PRL.
Robustness with respect to the geometric pic-
ture.These trends match the geometry in §5:
∆WMRL provides a low-rank scaffold that the pol-
icy stage can reuse, whereas PRL from base must
construct that scaffold and the task-specific cor-
rection jointly. The similar pattern appears under
magnitude pruning: top-p pruning recovers ∆∆PRL
to the WMRL→PRL baseline best with only 10%
of entries retained, while pruning ∆PRL yields best
performance with50%(Appendix A.6).
A.6 Magnitude Pruning of∆s
As a coordinate-space complement to the spec-
tral analyses, we apply classical magnitude prun-
ing (Han et al., 2015; Frankle and Carbin, 2019)
– also a central primitive in recent LLM weight
pruning methods such as SparseGPT (Frantar and
Alistarh, 2023), Wanda (Sun et al., 2024) and LLM-
Pruner (Ma et al., 2023) – to ∆PRL and ∆∆PRL, re-
taining only a p fraction of the ∆ entries (zeroing
the rest) chosen by three different selection rules
and re-evaluating task success: (i)top- p, keeping
the entries with the largest absolute magnitude; (ii)
bottom-p, keeping the entries with the smallest ab-
solute magnitude (i.e. the lowest-magnitude tail);
(iii)random- p, keeping a random p fraction. The
latter two serve as baselines that isolate, respec-
tively, the effect of discarding the high-magnitude
head and the effect of total mass alone. Per- p ID,
OOD, and A VG numbers for all three selection
rules are in Tab. 11. The sign_only row keeps
only the sign of every entry and rescales magni-
tudes to a fixed constant. The curves are also shown
in Fig. 9 to better track the trend.
Three patterns are consistent with the spectral
story: (i) top-p on ∆∆PRL reaches the best perfor-
mance with p= 0.1 , while the curve for ∆PRL
still goes up before p= 0.5 , indicating that the
update of ∆∆PRL is more compact. This is con-
sistent with ∆∆PRL’s smaller, output-orthogonal
spectral role on top of ∆WMRL. (ii) Bottom- p col-
lapses both ∆PRL and ∆∆PRL sharply for every p –
the high-magnitude entries discarded by bottom-p
are precisely the ones that carry the task signal,
14

Table 8: Right-space projection of ∆PRL onto ∆WMRL. Composition: θ0 + projR(∆PRL). Columns report the parallel
component (∆PRLV V⊤), orthogonal component ( ∆PRL(I−V V ⊤)), and random projection ( ∆PRLQQ⊤ with Q
random orthonormal).
parallel orthogonal random
kID OOD A VG ID OOD A VG ID OOD A VG
1 39.3±1.3 45.3±2.5 42.3±1.8 87.0±1.6 79.7±2.2 83.3±1.8 31.8±0.4 28.6±1.9 30.2±1.0
25 54.4±1.9 57.3±0.7 55.9±0.6 82.3±0.7 81.2±5.1 81.8±2.6 32.5±1.6 32.3±1.5 32.4±0.3
50 60.2±1.3 59.4±1.3 59.8±1.1 78.9±1.1 71.9±4.4 75.4±2.0 29.4±5.1 29.2±2.7 29.3±2.5
150 69.3±2.6 66.2±2.7 67.7±0.8 72.4±1.6 66.7±1.9 69.5±1.0 34.1±1.3 32.8±1.3 33.5±1.2
250 68.8±1.3 62.5±0.0 65.6±0.6 69.0±2.0 65.6±2.2 67.3±1.9 37.5±1.3 35.9±0.0 36.7±0.6
500 73.7±1.3 70.8±2.7 72.3±2.0 65.9±1.6 66.2±3.2 66.0±1.4 41.7±2.6 37.5±2.2 39.6±1.8
Table 9: Right-space projection of∆∆ PRL onto∆ WMRL. Composition:θ 0 + ∆WMRL + projR(∆∆PRL).
parallel orthogonal random
kID OOD A VG ID OOD A VG ID OOD A VG
1 44.0±2.2 40.6±3.8 42.3±1.6 91.4±0.6 82.8±1.3 87.1±0.8 33.3±2.0 28.6±1.9 31.0±1.8
25 59.1±1.8 63.0±5.2 61.1±2.3 92.5±1.0 85.4±1.5 88.9±1.2 33.3±1.5 30.2±3.9 31.8±1.5
50 65.6±3.4 70.8±4.5 68.2±1.3 93.0±1.7 82.8±2.2 87.9±0.3 30.7±3.5 33.9±1.9 32.3±1.9
150 78.7±1.8 77.6±1.5 78.1±1.7 92.2±0.0 82.8±1.3 87.5±0.6 34.4±1.9 30.7±3.9 32.5±1.0
250 82.0±2.5 79.7±2.5 80.9±1.3 90.4±0.7 81.2±1.3 85.8±0.4 37.0±1.8 34.4±2.2 35.7±1.8
500 83.6±1.1 79.7±2.2 81.6±1.5 89.6±0.7 77.6±1.9 83.6±0.6 42.7±2.6 39.6±4.8 41.1±1.4
Table 10: Truncated rank-k pruning of ∆s (§A.5). WkP:
θ0 + (∆WMRL)k + ∆∆PRL; WPk: θ0 + ∆WMRL + (∆∆PRL)k;
WkPk:θ 0 + (∆WMRL)k + (∆∆PRL)k;P k:θ 0 + (∆PRL)k.
MethodkID OOD A VG
WkP
1 77.6±1.0 79.7±2.2 78.7±1.3
25 82.0±0.6 82.3±1.9 82.2±1.3
50 85.7±1.6 83.8±3.0 84.8±2.2
250 86.5±1.8 79.2±2.7 82.8±2.2
500 86.5±1.0 82.8±2.2 84.6±0.8
WPk
1 43.8±2.9 46.4±0.7 45.0±1.4
25 85.7±2.2 78.7±1.5 82.2±0.7
50 88.3±1.1 82.3±0.7 85.3±0.9
250 88.0±1.0 81.2±2.2 84.6±0.8
500 88.3±1.9 82.3±1.5 85.3±1.6
WkPk
1 40.4±2.4 43.8±3.4 42.1±2.7
25 81.2±3.2 79.2±3.9 80.2±3.2
50 85.7±2.9 81.8±1.5 83.7±2.1
250 85.2±1.9 80.7±3.2 82.9±2.6
500 88.0±1.0 84.9±1.9 86.5±0.5
Pk
1 34.1±5.0 34.9±0.7 34.5±2.1
25 77.3±1.7 65.1±1.5 71.2±0.7
50 81.8±3.1 72.4±4.1 77.1±0.5
250 84.6±2.2 71.9±1.3 78.3±0.9
500 84.1±1.5 74.0±5.8 79.0±2.2
complementing the top-p result. (iii) Random-p re-
covers performance roughly in proportion to mass:
∆∆PRL random-p matches top-p only as p→0.5 ,
while ∆PRL random-p trails top-p by a wide margin
at small p. So the gain of top- p over random-p,
at any given p, gives a coordinate-level analogue
of the spectral concentration story – ∆∆PRL’s top-
0.02 0.05 0.1 0.3 0.5
p (mass fraction kept)
0
20
40
60
80
100
AVG success rate (%)
Magnitude pruning
WMRL→ PRL
PRL
top-p ∆P
bot-p ∆P
rand-p ∆P
top-p ∆∆P
bot-p ∆∆P
rand-p ∆∆P
Figure 9: Magnitude pruning on ∆PRL (blue) and ∆∆PRL
(red), comparing thetop- p selection rule (solid) against
bottom-p (dashed) andrandom- p (dotted) baselines.
Top-p keeps the entries of ∆ with the largest absolute
magnitude; bottom-p keeps the smallest; random- p is
a random subset of the same mass. Top- p on ∆∆PRL
performs best at p= 0.1 ; top-p on ∆PRL needs p≥0.3
to reach the maxima; bottom-p is near-baseline for all
p; random-psaturates only asp→0.5.
magnitude entries dominate downstream perfor-
mance much more than∆ PRL’s.
Bτ 2-Bench: Cross-task Replication
This appendix reports a partial replication of the
ALFWorld findings on τ 2-Bench with a different
base model (Qwen3-8B). §B.1 describes the train-
ing setup and end-to-end performance numbers,
15

Table 11: Magnitude pruning of ∆s on ALFWorld. p is the fraction of entries retained. Left block prunes ∆PRL;
right block prunes∆∆ PRL. Each section corresponds to one selection rule, followed by the sign-only baseline.
∆PRL pruned∆∆ PRL pruned
pID OOD A VG ID OOD A VG
top-p
0.02 75.5±0.4 74.5±1.5 75.0±0.8 82.0±5.7 75.0±2.2 78.5±2.2
0.05 74.5±1.3 75.5±0.7 75.0±0.3 82.0±3.5 75.0±2.5 78.5±1.4
0.10 82.8±2.2 73.4±3.4 78.1±1.3 88.3±1.3 81.2±2.2 84.8±1.7
0.30 85.7±1.0 74.5±0.7 80.1±0.3 88.8±0.4 80.7±1.5 84.8±0.6
0.50 85.4±1.9 74.5±0.7 80.0±1.0 87.0±1.8 77.1±3.9 82.0±1.4
bottom-p
0.02 24.0±1.0 23.4±1.3 23.7±1.1 32.3±3.2 27.6±3.2 29.9±0.4
0.05 23.7±0.7 20.8±1.9 22.3±1.1 31.8±3.0 29.7±4.6 30.7±2.7
0.10 23.4±2.3 19.3±2.7 21.4±1.3 34.1±2.7 32.8±3.4 33.5±2.9
0.30 23.7±4.2 23.4±3.4 23.6±3.8 34.9±3.7 30.2±3.9 32.5±2.4
0.50 23.4±1.1 24.5±1.9 24.0±1.4 34.6±3.0 28.1±2.5 31.4±0.7
random-p
0.02 25.5±2.0 29.7±2.2 27.6±1.2 39.3±1.5 32.3±2.7 35.8±1.0
0.05 29.7±1.9 33.3±1.9 31.5±1.8 43.0±2.2 38.5±1.9 40.8±0.4
0.10 36.2±1.9 39.6±0.7 37.9±0.6 52.9±2.9 46.9±3.4 49.9±2.1
0.30 66.9±2.7 64.1±2.5 65.5±0.4 74.2±0.6 72.9±3.9 73.6±2.3
0.50 80.0±0.7 73.4±0.0 76.7±0.4 87.2±2.0 81.2±2.5 84.2±2.2
sign_only85.2±1.7 74.5±3.7 79.8±1.4 83.8±1.3 80.2±1.9 82.0±1.1
and §B.3 replicates the subspace asymmetry of §5
on this model/task pair.
B.1 Training and Reproduction Setup
Base model and data.We start from Qwen3-
8B (Qwen Team, 2025b). Following Yu et al.
(2026), we fix the history lengthH= 5 to deal with
more complex scenarios. As τ 2-Bench provides
only 178 training tasks, we roll out 6 trajectories
per task – three with GPT-4.1 as the user simula-
tor and three with Qwen3-235B-A22B-Instruct –
and convert trajectories into transition triplets. To
prevent the model from memorizing database con-
tents, we replace tool-response values with their
OpenAPI schemas.
Sim-to-real reward.Following Yu et al. (2026):
embedding-based binary similarity for natural-
language user responses (Qwen3-Embedding-8B,
η= 0.6 ), and a discretised ROUGE-L score for
structured tool responses.
WMRL stage. 2 epochs, learning rate 1e−6, effec-
tive batch size 32, GRPO group size 16. We use
similar filtering pipeline as Yu et al. (2026). Each
checkpoint is trained on two NVIDIA H200 GPUs
for around 10 hours. The data size is∼6K.
PRL stage.GRPO with terminal task-success re-
ward, γ= 1.0 , max 30 steps per episode, 200
update steps, group size 8. We use Qwen3-235B-
A22B-Instruct as the user simulator throughout.
We also use the modified Verl-Agent GitHub repo
for training and each checkpoint is trained on four
NVIDIA H200 GPUs for around 100 hours.
Table 12: Replicated τ 2-Bench performance. A VG@3
is mean ± std success rate over 3 seeds across retail,
telecom, and airline; pass@k (Chen et al., 2021) is the
probability that at least one ofkrollouts succeeds.
Model A VG@3 pass@1 pass@3
ReAct (base)33.7±2.5 37.0 49.0
WMSFT26.0±4.3 30.0 46.0
WMRL36.3±0.5 36.0 52.0
PRL39.3±2.6 38.0 58.0
WMSFT→PRL38.3±4.5 41.0 59.0
WMRL→PRL45.0±1.6 43.0 64.0
B.2 Per-layer Effective Rank
We reproduce the main-text per-layer effective-rank
plot (Fig. 7) on Qwen3-8B +τ 2-Bench checkpoints
in Fig. 10, using the same plot format (one line per
checkpoint, averaged across all target modules).
The qualitative ordering is preserved across all 36
layers: WMRL sits visibly above the RL-stage check-
points (PRL, WMRL→PRL , WMSFT→PRL , clustered
in the middle), and WMSFT trails them in the deeper
layers – matching the Qwen2.5/ALFWorld pattern
on a different model and benchmark.
16

0 5 10 15 20 25 30 35
Layer
2400
2500
2600
2700
Effective Rank (avg over all modules)
WMRL
PolicyRL
WMSFT
WMSFT+PolicyRL
WMRL+PolicyRL
Effective Rank per Layer
Figure 10:Per-layer eRank(∆) of post-training on
Qwen3-8B + τ 2-Bench, averaged across all target mod-
ules. Same plot format as the main-text Fig. 7: WMRL
(red) keeps the highest per-layer rank; the RL-after-WM
variants (WMRL→PRL , WMSFT→PRL ) and PRL cluster
closely in the middle; WMSFT (green) is comparable in
the early layers but drifts below the RL-trained check-
points in the deeper layers.
B.3 Cross-model Replication of the Subspace
Asymmetry
The main-text geometric analyses in §5 are con-
ducted on Qwen2.5-7B-Instruct fine-tuned on ALF-
World. To check that the U-disjoint / V-shared
asymmetry is not an artefact of a single model
or task, we replicate the module-wise subspace
overlap measurement on a different model and
benchmark: Qwen3-8B fine-tuned on τ 2-Bench.
The fine-tuning recipe follows the same two-stage
pipeline (WMRL followed by PRL), so we can form
the same ∆PRL and ∆∆PRL updates and compute
their leading-k left and right subspace overlap mod-
ule by module, exactly as in §5.4.
Headline numbers (Tab. 13).The asymmetry
holds, and is in fact slightly sharper on Qwen3.
Mean rank- 1 leftoverlap is 0.04 on both mod-
els (essentially identical), while mean rank-1 right
overlap is 0.81 on Qwen3 versus 0.63 on Qwen2.5.
The Frobenius cosine between ∆PRL and ∆∆PRL is
0.015 on Qwen3 (vs. 0.028 on Qwen2.5), confirm-
ing that the two updates are close to orthogonal as
matrices on both models.
Module-wise heatmaps.Fig. 11 reproduces the
rank-1 left/right overlap heatmaps of §5.4 on
Qwen3. Visually the pattern is the same as on
Qwen2.5 (cf. Fig. 4): the left heatmap is uniformly
dark (near-zero overlap on output directions) while
the right heatmap is uniformly bright (high overlap
on input-feature directions). A small handful of
early-FFN modules (up_proj/gate_proj in layers
Table 13: Cross-model replication of the module-wise
subspace overlap (∆PRL vs. ∆∆PRL) and Frobenius co-
sine, averaged over all target modules in each model.
metric Qwen2.5-7B Qwen3-8B
(ALFWorld) (τ 2-Bench)
n_modules 196 252
Frobenius cosine, mean 0.028 0.015
Left subspace overlap
k=1, mean 0.036 0.043
k=50, mean 0.158 0.157
k=250, mean 0.239 0.238
Right subspace overlap
k=1, mean 0.6350.811
k=50, mean 0.411 0.508
k=250, mean 0.393 0.416
1–4) show the reverse pattern – shared on the left,
disjoint on the right – which we note but do not
interpret further here; outside this small block, the
U-disjoint / V-shared geometry holds module-wise
across all36layers.
q
k
v
o
up
gate
down
Left rank-1 subspace overlap
0 4 8 12 16 20 24 28 32
Layer
q
k
v
o
up
gate
down
Right rank-1 subspace overlap
0.0
0.5
1.0
Figure 11:Module-wise rank- 1 subspace overlap be-
tween ∆PRL and ∆∆PRL on Qwen3-8B + τ 2-Bench.
The top panel shows the left-side overlap (k=1, mean
0.04), nearly orthogonal, while the bottom panel
shows the right-side overlap (k=1, mean 0.81), highly
aligned at the dominant input direction – matching the
Qwen2.5/ALFWorld pattern.
Does the geometric asymmetry translate to a
behavioral asymmetry?To check whether the
U-disjoint / V-shared geometry reproducesbehav-
iorallyon Qwen3, we run the same parallel/orthog-
onal projection sweep that produced the main-text
left/right curves on the Qwen3 + τ 2-Bench check-
points, and then we compare the k=1 and k=250
rows against the Qwen2.5/ALFWorld numbers in
Tab. 14.
Geometry replicatesThe qualitative direction is
preserved: on Qwen3, orthogonal-to-∆WMRL projec-
17

0 8 16 24 32
Layer
q_proj
k_proj
v_proj
o_proj
up_proj
gate_proj
down_proj Module
Qwen3: ∆PRL vs. ∆∆PRL
0.2
0.1
0.0
0.1
0.2
Frob. cos.
Figure 12: Per-module Frobenius cosine similarity be-
tween ∆PRL and ∆∆PRL on Qwen3-8B + τ 2-Bench. The
vast majority of modules are at or near zero; only a small
subset of attention projections in the last three layers
shows mild positive similarity (≲0.10 ). Module-wise
mean is0.015.
tions of ∆PRL at k=1 are still higher than parallel
ones ( 40.3 vs. 34.0, gap +6.3), and the parallel
projection sits at the base+∆WMRL level rather than
near the oracle – the sign of the asymmetry matches
Qwen2.5. What is different is themagnitude: on
Qwen2.5 the k=1 orth−par gap is +50 points, on
Qwen3 it is +6. Three factors might explain most
of this attenuation:
• Smaller dynamic range for ∆PRL.On
Qwen2.5, ∆PRL buys +60.6 points over base
(17.7→78.3 ); on Qwen3 it buys only +5.6
(33.7→39.3 ). The behavioral signal that any
projection of ∆PRL can corrupt or preserve is
proportionally smaller.
• Smaller two-stage gain over ∆PRL.The
∆WMRL+∆∆PRL oracle is only +5.7 above
∆PRL alone on Qwen3 (vs. +6.1 on Qwen2.5
in absolute, but starting from a far higher base)
– and as a fraction of headroom this is much
thinner. Recovering even 80% of that gain is
a ∼4.6 point swing that competes with per-
repeat noise of±1–4points.
• Lower absolute success rates and a harder
task. τ 2-Bench operates in the 30–45% band
where multi-tool long-horizon failures domi-
nate; small per-direction perturbations do not
change which tasks succeed in nearly as many
cases as on ALFWorld’s17–88%range.
Table 14: Cross-model behavioral projection results.
Numbers are end-to-end success rate (%) averaged over
3 repeats. Same projection sweep as Tabs. 6 and 8, re-
stricted to k=1 and k=250. Geometric asymmetry repli-
cates cleanly on Qwen3 (Tab. 13), but the behavioral
separation between parallel and orthogonal projections
is much smaller, for reasons we discuss below.
Qwen2.5-7B Qwen3-8B
(ALFWorld) (τ 2-Bench)
base 17.7 33.7
∆WMRL alone 32.7 36.3
∆PRL alone 78.3 39.3
∆WMRL+∆∆PRL (oracle) 84.4 45.0
Left-space proj. of∆ PRL onto∆ WMRL
parallel,k=132.5 34.0
parallel,k=25043.9 35.0
orthogonal,k=182.5 40.3
orthogonal,k=25084.4 40.7
Right-space proj. of∆ PRL onto∆ WMRL
parallel,k=142.3 35.3
parallel,k=25065.6 39.0
orthogonal,k=183.3 39.7
orthogonal,k=25067.3 40.7
The right-side picture is the weakest: on Qwen2.5,
the parallel-on-right projection at k=250 recov-
ered 71.8% of the oracle gain over base, evidence
that ∆PRL’s input-feature scope is largely shared
with ∆WMRL. On Qwen3, the analogous parallel-on-
right projection recovers only 46.9% of the (much
smaller) oracle gain – consistent with the above
noise/dynamic-range argument rather than with a
failure of the geometric claim, since the underly-
ing right-overlap mean is in fact higher on Qwen3
(0.81vs0.63).
Takeaway.The U-disjoint / V-shared subspace
asymmetry between ∆PRL and ∆∆PRL, and the near-
zero Frobenius cosine, are reproduced on a differ-
ent base model (Qwen3-8B vs Qwen2.5-7B), a
different post-training corpus (τ 2-Bench vs ALF-
World), and a different model depth (36 vs 28 lay-
ers), with essentially identical left numbers and
an even sharper right alignment. The behavioral
projection sweep on Qwen3 carries the same qual-
itative sign (orth > par on the left at low k, no
collapse under either projection), but its margins
are compressed into the noise band by the smaller
absolute ∆PRL contribution and the harder bench-
mark. Read together, these two appendices indicate
that the geometric complementarity diagnosed in
§5 may be a property of the two-stage post-training
recipe rather than of a particular model/task, while
the strength with which it shows up in end-to-end
18

success requires a task and model where ∆PRL it-
self has substantial headroom to begin with. How-
ever, we caution against over-interpreting these re-
sults: these experiments cannot establish generality
across models and agent types.
C Preservation Method Details
We study two ways to preserve the world-modeling
ability acquired during WMRL while adapting the
policy with PRL. The first istraining-free: merge
two fine-tuned checkpoints in weight space. The
second istraining-based: add an online world-
modeling SFT loss during PRL. In all cases, the
preservation method produces a single deployable
policy checkpoint.
Training-free checkpoint merging.The merg-
ing methods take the base model M0 and two
task checkpoints as input: always MWMRL for task
A, and either MPRL or the sequential checkpoint
MWMRL+PRL (WMRL→PRL ) for task B. For each
target weight matrixW (k), we form task vectors
τ (k) i =W (k) i −W (k) 0 , i∈ {A, B}.
We merge only the seven projection matrices in
each transformer layer,
q,k,v,o,up,gate,down,
and leave embeddings, layer norms, and the lm-
head at their base-model values.
Plain TIES.Plain TIES operates directly on the
raw task vectors τA, τB flattened from the entire
model’s parameters. For each pair of models, we
stack the two task vectors, keep the top-K% entries
by magnitude (K=40), resolve sign conflicts with
sum_of_values, and average the surviving entries
using a disjoint mean, i.e. each coordinate is di-
vided by the number of non-zero contributors rather
than by the total number of tasks. The merged
checkpoint is
Wmerged =W 0 + TIES(τA, τB).
KnOTS.KnOTS first represents the two module-
wise task vectors in a shared low-rank SVD frame,
then applies the same TIES masking and aggrega-
tion in that frame. In the default U-sharing version,
the two task matrices are concatenated along the
input dimension:

τ (k) A |τ (k) B  =U (k)Σ(k)V (k)⊤.
Algorithm 1OnlineWMSFTduringPRL
Require: Policy πθ, downsampling ratio ρ= 0.2 ,
WM-SFT weightλ= 1.0
1:foreachPRLupdate stepdo
2:Collect on-policy rollouts withπ θ
3: Extract real WM-SFT pairs DWM =
{((st−H:t , at), st+1)}
4: Downsample no-op transitions (st+1 =s t)
to at most ρ times the number of changed-
observation transitions
5:Randomly keep32samples each step
6:ComputeL GRPO on the rollout batch
7: Compute LWM-SFT by predicting st+1 from
(st−H:t , at)
8:UpdateθusingL GRPO +λL WM-SFT
9:end for
10:returnUpdated policyπ θ
This gives a shared left basis U (k), corresponding
to a shared output subspace. The per-task right
factors are split from ΣV ⊤, TIES is applied to
those factors, and the merged delta is reconstructed
as
∆(k) =U (k)V (k) merged.
We also evaluate a V -sharing variant, motivated
by the stronger right-subspace overlap observed
in §5. This variant transposes each task matrix
before the joint SVD, so that the shared basis lies
on the input side rather than the output side. After
merging in this transposed frame, the reconstructed
matrix is transposed back to the original (out,in)
shape. We modify KnOTS’s official repository 2 to
enable full parameter update merging.
For both KnOTS variants, we use the same
TIES hyperparameters as plain TIES: K=40,
sum_of_values sign resolution, disjoint-mean ag-
gregation, scaling coefficient 1.0, and no DARE
pre-processing. Singular directions with negligible
singular values are discarded.
Training-based: online WM-SFT during PRL.
We follow the PRL GRPO training setup of Yu
et al. (2026), but add an auxiliary online world-
modeling SFT update. At each training step, we
reuse the same on-policy rollouts collected for
GRPO and convert each realized transition into
a next-observation prediction example: given the
recent observation history st−H:t and the executed
action at, the model predicts the environment’s
2https://github.com/gstoica27/knots
19

next observation st+1. Hence, the WM signal is
“free” in the sense of the concurrent ECHO recipe of
Shrivastava et al. (2026): it requires no additional
environment interaction. The training objective is
L=L GRPO +λL WM-SFT, λ= 1.0
with all otherPRLhyperparameters unchanged.
Table 15: KnOTS-TIES preservation interventions on
Qwen3-8B + τ 2-Bench. We compare the source check-
points with training-free KnOTS-TIES merges at top-
K=40, using either the default shared U basis or our
shared V -basis variant. The two merge blocks differ
in the second task arm: PRL from base, or the trained
sequential WMRL→PRL checkpoint.Bold= best within
each sub-block.
Method A VG@3 pass@1 pass@3
PRL39.3±2.6 38.0 58.0
WMRL→PRL45.0±1.6 43.0 64.0
training free:WMRL+PRL
KnOTS-TIES (U)38.0±0.8 37.0 54.0
KnOTS-TIES (V)40.7±2.937.058.0
training free:WMRL+ (WMRL→PRL)
KnOTS-TIES (U)38.0±3.6 35.0 56.0
KnOTS-TIES (V)39.3±4.241.057.0
KnOTS replication on τ 2-Bench.We repli-
cate the training-free KnOTS-TIES merges from
§C on Qwen3-8B + τ 2-Bench, using the same
top-K=40, sum_of_values sign resolution, and
merging_type=mean as in the ALFWorld exper-
iments (Table 15). The results broadly favor the
shared right/input singular basis (V -sharing) over
the default U-sharing variant, consistent with the
input-side geometry suggested by §5. In both
merge settings, the V -sharing variant attains the
best A VG@3 within the training-free block, and
in the WMRL+ (WMRL→PRL) setting it also im-
proves pass@1 and pass@3. However, the best
training-free merge still remains below the trained
WMRL→PRL sequential baseline, suggesting that
simple checkpoint merging is not sufficient to re-
cover the full benefit of staged training on this more
complex benchmark. For cost reasons, we do not
replicate the online WMSFT auxiliary-loss baseline
onτ 2-Bench.
D WMRL Data Example
We show one representative training example from
ALFWorld and one from τ 2-Bench. Each example
consists of the model prompt, and the ground-truth
next observation used as the supervision target. Part
of the content is omitted for display.
For WMSFT and entropy probing in Figure 6, we
revise the final instruction to disable thinking.
ALFWorld example
Prompt
You are an expert agent operating in the
ALFRED Embodied Environment.
Your task is to: look at pillow under the
desklamp.
Prior to this step, you have already taken 7
step(s). Below are the
most recent 2 observations and the
corresponding actions you took:
[Observation 6:'You arrive at shelf 1. On
the shelf 1, you see a
pencil 2, and a pencil 1.', Action 6:
'[<action>go to desk 1</action>']
[Observation 7:'Nothing happens.', Action 7:
'<action>go to desk 1
</action>']']
You are now at step 8 and your current
observation is: Nothing
happens.
Your admissible actions of the current
situation are:
['examine shelf 1' 'go to bed 1' 'go to desk
1' 'go to desk 2'
'go to garbagecan 1' 'go to shelf 2' 'go to
shelf 3' 'go to shelf 4'
'go to shelf 5' 'inventory' 'look' 'take
pencil 1 from shelf 1'
'take pencil 2 from shelf 1'].
Potential action: <action>go to desk
1</action>
Now, your task is to predict the immediate
next observation after executing the
potential action above.
You should first *briefly* reflect on the
previous steps and current situation. Then
think about what the next observation will
look like after taking this action, and also
whether the task is completed after taking
this action. This reflection and reasoning
process MUST be enclosed within <think>
</think> tags.
Once you've finished your reasoning, present
both your final prediction of the next
observation (use the past and current
observations as examples!) and task
completion status within <next_state>
</next_state> tags.
Ground-truth next observation
You arrive at desk 1. On the desk 1, you see
a creditcard 1, and a
keychain 1. Task is not yet completed.
20

ALFWorld Non-thinking Prompt
...
Now, your task is to predict the immediate
next observation after executing the
potential action above.
Directly present your final prediction of the
next observation. DO NOT generate anything
else.
τ 2-Bench example
Prompt, abbreviated
<instructions>
You are a customer service agent that helps
the user according to
the <policy> provided below.
...
</instructions>
<policy>
# Retail agent policy
[... full retail policy elided: ~6k chars
covering cancel/modify
pending orders, return/exchange delivered
orders, identity
authentication rules, payment-method rules,
etc. ...]
</policy>
<tools>
[... ~30 tool schemas elided:
find_user_id_by_email,
find_user_id_by_name_zip, get_user_details,
get_order_details,
return_delivered_order_items,
exchange_delivered_order_items,
cancel_pending_order,
modify_pending_order_items,
transfer_to_human,
...]
</tools>
# Dialogue so far
user: Hi! I need to return two tablets I
bought recently. Can you
help me with that?
assistant: I can help you with that. To
process your return, I'll
need to verify your identity first.
...
potential assistant response: I've located
your account, Chen Silva
(user ID: chen_silva_7485). To process your
return, I'll need the
order ID of the tablets you purchased.
Once you've finished your thinking, format
both your final prediction of the next
user/tool response and task completion status
within <next_state> </next_state> tags.
Ground-truth next observation
Hmm, I don't have the order ID on me right
now -- everything's kind of scattered. Is
there another way we can find it? Maybe by
the date I ordered or the tablet model? I
think it was within the last two weeks.
Task is not yet completed.
Tau2-Bench Non-thinking Prompt
...
DO NOT perform any thinking. Directly present
your final prediction of the next user/tool
response and task completion status.
E WM-SFT Prompt Format
We use a lightweight next-observation prediction
template for online WMSFT to mitigate the collapse
in the separate training stage. The prompt contains
the previous raw environment observation and the
agent’s extracted action; the supervision target is
only the next environment observation.
Template
Given the previous observation and the action,
predict the next observation.
Previous observation:
{prev_obs}
Action:
{action}
Next observation:
Concrete instance
<|im_start|>user
Given the previous observation and the action,
predict the next observation.
Previous observation:
Nothing happens.
Action:
go to desk 1
Next observation:<|im_end|>
<|im_start|>assistant
Only these target tokens haveloss_mask=1
Supervision target
You arrive at desk 1. On the desk 1, you see
a creditcard 1, and a
keychain 1.<|im_end|>
21
