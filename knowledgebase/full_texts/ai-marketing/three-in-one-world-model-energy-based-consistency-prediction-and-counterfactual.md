---
title: 'Three-in-One World Model: Energy-Based Consistency, Prediction, and Counterfactual Inference for
  Marketing Intervention'
url: https://arxiv.org/abs/2605.07199
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Junichiro Niimi
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.07199
pages: 11
chars: 49887
fetched_at: '2026-11-08T12:57:55+00:00'
kb_version: 1
---

# Three-in-One World Model: Energy-Based Consistency, Prediction, and Counterfactual Inference for Marketing Intervention

THREE-IN-ONEWORLDMODEL: ENERGY-BASED
CONSISTENCY, PREDICTION,ANDCOUNTERFACTUAL
INFERENCE FORMARKETINGINTERVENTION
A PREPRINT
Junichiro Niimi* 1
1Meijo University
ABSTRACT
Marketing decisions reflect the interaction of latent consumer heterogeneity, time-varying internal
states, and explicit interventions, a structure that current prediction- and language-oriented mod-
els do not capture in a unified manner. We propose a Three-in-One world-model architecture in
which a Deep Boltzmann Machine (DBM) learns a frozen belief representation from demographics,
time, and lagged actions and outcomes, with lightweight task-specific adapters attached on top. The
same belief supports three tasks within a single framework: (i) energy-based consistency evaluation
through the DBM’s free energy, (ii) outcome prediction through adapters, and (iii) counterfactual
inference by holding the belief fixed and varying only the action input given to the adapter. Us-
ing a controlled simulation in which the latent price sensitivity, promotion responsiveness, and base
preference of each consumer are known, we show that the adapters match a strong MLP baseline
on visit- and purchase-AUC while recovering heterogeneous treatment effects substantially better
than S-, T-, X-, and DR-learner meta-learners and a Causal Forest baseline built on the same raw
features, with the largest gap on a confounded price-promotion intervention. Complementing this,
free-energy clamps systematically penalize counterfactual purchase trajectories that lack prior pro-
motional exposure, and the penalty itself depends on the latent base preference in the expected
direction. These results indicate that DBM beliefs disentangle latent traits in a form that survives
counterfactual queries, providing an integrated world-model substrate for marketing intervention.
Keywordsworld model·deep Boltzmann machine·energy-based model·counterfactual inference·marketing
intervention
1 Introduction
1.1 Background
Large language models (LLMs) have achieved remark-
able progress in recent years. Since the introduction of
the Transformer architecture [1], the field has witnessed
rapid scaling of autoregressive language models, such as
generative pretrained transformer (GPT) [2, 3, 4, 5], with
performance improving predictably as a function of model
and data size [6]. These models now demonstrate impres-
sive capabilities across a wide range of tasks, yet their suc-
cess relies fundamentally on next-token prediction over
text sequences, a paradigm that lacks explicit mechanisms
for causal reasoning or internal world representation [7].
In contrast to such token-level prediction, world models
i.e.,systems that learn an internal representation of en-
vironment dynamics to enable prediction, planning, and
reasoning, have attracted growing attention as a comple-
mentary paradigm [8, 7]. Recent theoretical proposals [7]
and empirical advances [8, 9, 10] have positioned world
models as a promising path beyond the limitations of au-
toregressive generation. This view is echoed in broader
discourse: for example, Yann LeCun has described au-
toregressive LLMs as “doomed” due to their inability to
model causality 1, and Demis Hassabis has emphasized
that artificial general intelligence (AGI) requires world
models capable of understanding physical reality2.
To date, world models have been explored predominantly
in the context of physical environments (e.g.,robotic con-
trol [8] and video generation [10, 11]) where the goal is
to simulate and anticipate interactions with the real world
[12]. Yet the core premise of world models, learning the
latent dynamics that govern sequential observations, ap-
plies equally to behavioral domains. In consumer behav-
ior, for instance, purchase decisions emerge from the in-
1Joint Mathematics Meetings, January 2025.
2Google DeepMind Podcast, December 2025.
arXiv:2605.07199v1  [cs.AI]  8 May 2026

Three-in-One World ModelA PREPRINT
teraction of latent individual traits, time-varying states,
and marketing interventions, a dynamic process that de-
mands the same kind of internal representation that world
models provide for physical systems.
This paper therefore proposes a world-model architec-
ture with multiple task-specific adapters that captures
the structure of consumer behavior and supports predic-
tion, consistency evaluation, and counterfactual inference
within a single framework. We evaluate the proposed
model using simulation data, where ground-truth coun-
terfactual outcomes are available for rigorous assessment
of causal effect recovery. The remainder of the paper is
organized as follows. Section 2 reviews the related study
to formulate the research gaps. Section 3 introduces the
architecture and algorithm of the proposed model. Sec-
tion 4 conducts the three simulation-based experiments
to demonstrate the performance of the proposed model.
Finally, Section 5 summarizes the findings, implications,
and limitations of the study.
1.2 Contributions
This study makes four contributions.
Marketing application of world models.We bring the
world-model paradigm [8, 7] into the marketing domain
by treating the consumer-and-environment dynamics—
demographics, time, lagged interventions, and lagged
outcomes—as the system whose latent structure is to be
learned. The resulting model captures time-varying con-
sumer states using only lagged features in the visible
layer, without recurrent connections, while preserving the
asymmetry between a heavy world model and lightweight
downstream modules that characterizes [8].
Energy-based consistency evaluation.By adopting a
DBM as the world model, the proposed framework can
score the consistency of an input pattern through its free
energy: low free energy indicates that the configuration
of demographics, history, and observed behavior is plau-
sible under the learned distribution, whereas high free en-
ergy flags an implausible scenario. Unlike the static co-
occurrence model of [13], the consistency check here ap-
plies to time-extended trajectories that include lagged ac-
tions and outcomes.
Prediction via belief representation.The belief vec-
tor formed by concatenating activations of all hidden lay-
ers serves as a frozen, task-agnostic substrate on which
compact MLP adapters are trained for each downstream
task. Empirically, this two-stage design matches the
test-set AUC of an MLP trained end-to-end on the raw
features, demonstrating that the dimensionality reduc-
tion performed by the DBM does not sacrifice predictive
power.
Counterfactual inference.Because the current-period
intervention vector is supplied only to the adapter and not
to the DBM, counterfactual outcomes can be obtained by
fixing the belief and toggling the action input. This yields
individual-level CATE estimates that, under the controlled
simulation studied here, recover the true heterogeneity in
price sensitivity and promotion responsiveness more ac-
curately than S-, T-, X-, and DR-learner meta-learners and
a Causal Forest baseline that operate on the same raw fea-
tures.
2 Related Study
2.1 Large Language Models
Building on the background in Section 1, we here review
LLMs with a focus on their real-world applications and
their relationship to world models. Through next-token
prediction on massive corpora, LLMs acquire broad lin-
guistic and reasoning capabilities that transfer to a wide
range of downstream tasks [4, 14, 15, 16].
In the real-world application, particularly in the field of
marketing, LLMs have been applied primarily to text-
centric tasks such as sentiment analysis [14], review gen-
eration [17, 18], and consumer simulation [19, 20]. While
these applications exploit the linguistic fluency of LLMs,
they do not address the structural modeling of consumer
dynamics—the latent heterogeneity, time-varying states,
and intervention effects—that is the focus of the present
study.
A central open question is whether LLMs implicitly ac-
quire world models through language modeling alone.
Some evidence suggests that LLMs can develop internal
representations of environment states. A representative
line of work on board games began with Othello-GPT
[21], demonstrating that world representations emerge in
a synthetic task without any prior knowledge about the
game rules [22, 23, 24].
Other studies have focused on LLM-driven agent sim-
ulations, demonstrating emergent social behaviors that
resemble aspects of world modeling [25, 26]. How-
ever, without additional architectural constraints, such
representations remain implicit, entangled with linguistic
knowledge, and do not readily support causal or counter-
factual reasoning [7].
More fundamentally, a growing body of criticism ques-
tions whether fluent generation equates to genuine under-
standing. Bender and Koller [27] argue that a system
trained solely on linguistic form cannot acquire mean-
ing, because the mapping from form to communicative
intent is underdetermined by text alone. Bender et al.
[28] further characterize LLMs as “stochastic parrots”
that reproduce statistical patterns in their training data
without grounded comprehension. These critiques sug-
gest that next-token prediction, however scaled, may be
insufficient for building models that truly represent how
the world works—motivating the development of explicit
world models.
2

Three-in-One World ModelA PREPRINT
2.2 World Models
2.2.1 Two Major Trends in World Models
World models have gained renewed attention as a com-
plementary paradigm to LLMs [12, 29]. The field en-
compasses two major streams: reinforcement-learning-
based approaches [8, 30] and representation-learning ap-
proaches [7, 10, 9]. In this study, we draw on ideas from
both streams.
First, Ha and Schmidhuber [8] introduced an RNN-based
world model that learns environmental dynamics through
state prediction, comprising Vision (V), Memory (M),
and Controller (C) modules.Mpredicts the latent state
at timet+ 1from the current latent state at timetand
action, whileCselects actions based on the resulting rep-
resentation. A key design principle is the asymmetry be-
tween components:C(867 parameters) is orders of mag-
nitude smaller thanV(4.3M) orM(0.4M), andCop-
erates only onz, an abstract representation produced by
V. This demonstrates that if a world model captures suf-
ficient structure, the downstream controller need not be
large.
Second, the Joint Embedding Predictive Architecture
(JEPA) line of work [9, 10] operationalizes LeCun’s vi-
sion [7] by learning world models in an abstract embed-
ding space, demonstrating that meaningful structure can
be captured without reconstructing pixel-level details as
in generative approaches. Central to this framework is
the use of Energy-Based Models (EBMs) [31], in which
an energy function distinguishes plausible from implau-
sible configurations, as a foundation for world models:
low energy indicates a plausible pattern, while high en-
ergy signals an implausible one. This property is par-
ticularly attractive for world models, because the energy
landscape provides a built-in mechanism for evaluating
input consistency—a capability that has been exploited
for anomaly detection [32] and, more recently, for cog-
nitively inspired world models [33].
2.2.2 Deep Boltzmann Machine
The Deep Boltzmann Machine (DBM) [34] is a represen-
tative EBM that stacks multiple layers of Restricted Boltz-
mann Machines (RBMs) [35, 36], each an undirected bi-
partite model whose intra-layer independence enables ef-
ficient inference. The DBM is trained via greedy layer-
wise pretraining of individual RBMs followed by joint
fine-tuning across all layers [37]. As a generative model,
the DBM assigns an energy to every configuration of vis-
ible and hidden units, and its free energy (FE) provides a
principled score of how well an input pattern conforms to
the learned distribution.
Niimi [13] adopted a DBM as a world model and com-
bined it with an adapter and GPT-2 [3] to build a con-
sumer review generation model. By separating the world
model from the language model, the study demonstrated
that (i) energy-based coherence can be evaluated by the
DBM alone, (ii) conditioning through the world model
enables a small language model to generate fluent and se-
mantically coherent text, and (iii) interventional genera-
tion is possible by clamping the input vector of the DBM.
However, that model was limited to static co-occurrence
among variables and could not capture time-varying dy-
namics within individual consumers.
Several studies have extended RBMs to handle time-series
data [38, 39, 40, 41, 42]. These extensions were de-
signed primarily for sequential generation tasks such as
music composition and motion capture, where modeling
the conditional distribution of the next observation given
the history is the natural objective. The Conditional RBM
(CRBM) [38] achieves this by using past observations to
modulate biases at each time step, while models with re-
current structures, such as Recurrent Temporal RBM (RT-
RBM) [40] and RNN-RBM [41], introduce hidden-to-
hidden connections trained via backpropagation through
time (BPTT) [43, 44, 45].
Our design goals differ. For counterfactual inference, we
require a world model whose parameters represent the sta-
ble structure of the environment, with temporal variation
captured in the agent’s internal state (belief) rather than
in time-varying model parameters. We therefore adopt
a standard DBM and incorporate temporal information
through lagged features in the visible layer. This sim-
pler design also enables the use of a multi-layer hierar-
chy, which can in principle provide a richer, hierarchically
summarized belief representation by concatenating the ac-
tivations of all hidden layers—an option not exploited by
the temporal RBM extensions above, which typically op-
erate with a single hidden layer.
2.3 Causal Inference
Causal inference aims to estimate the effect of an inter-
vention from observational or experimental data. Two
foundational frameworks underpin this field: the potential
outcomes framework [46], which defines causal effects
through the contrast of counterfactual outcomesYi(1)and
Yi(0)for each uniti, and the structural causal model
of Pearl [47], which formalizes interventions via thedo-
operator. A central challenge is that only one potential
outcome is ever observed for a given unit—the fundamen-
tal problem of causal inference.
When treatment effects vary across individuals, the quan-
tity of interest is the Conditional Average Treatment Ef-
fect (CATE):τ(x) =E[Y(1)−Y(0)|X=x].
K¨unzel et al. [48] systematize CATE estimation under
the meta-learner framework. The S-learner fits a single
model with treatment as a feature and estimates CATE as
ˆµ(x,1)−ˆµ(x,0); the T-learner trains separate models for
treated and control groups. The X-learner [48] extends
the T-learner by imputing individual treatment effects
on each arm and combining them through a propensity-
weighted average, which improves performance under
unbalanced treatment assignment. The DR-learner [49]
3

Three-in-One World ModelA PREPRINT
regresses a doubly robust pseudo-outcome—constructed
from outcome-model and propensity-score nuisance es-
timates with cross-fitting—on covariates, providing opti-
mality guarantees under flexible nuisance estimation. Wa-
ger and Athey [50] propose the Causal Forest, a nonpara-
metric approach based on random forests that partitions
the covariate space to estimate heterogeneous effects di-
rectly. These methods serve as baselines in our experi-
ments.
In marketing, CATE estimation is operationalized as up-
lift modeling (i.e.,the task of identifying which cus-
tomers will respond positively to a specific intervention
such as a promotion or advertisement) [51, 52, 53]. Un-
like conventional predictive models that estimate the out-
come level, uplift models estimate the incremental ef-
fect of treatment, enabling targeted intervention strategies.
Our approach differs from existing uplift methods in that
CATE is derived from the counterfactual predictions of a
world model: by holding the belief representation fixed
and varying only the action input, the adapter produces
paired predictions whose difference yields an individual-
level treatment effect estimate.
2.4 Research Gaps
The related studies reviewed above reveal several open is-
sues that the present work aims to address.
World model for consumer behavior remains static.
Existing work on DBM-based world models for market-
ing [13] operates solely on static, non-time-varying vari-
ables. As a result, the model cannot represent how con-
sumer states evolve over time in response to past actions
and outcomes.
Coherence evaluation is limited to static co-
occurrence.Because the underlying world model
is static, energy-based coherence evaluation is restricted
to assessing co-occurrence among consumer demograph-
ics, product attributes, and behavioral logs at a single
point in time. It cannot evaluate the consistency of
temporal scenarios—for example, whether a sequence
of purchase behaviors is plausible given a consumer’s
history and the interventions they received.
Downstream tasks lack modularity.In most multi-
task learning approaches, accommodating a new down-
stream task requires updating the shared model weights,
risking catastrophic forgetting of previously learned tasks.
A world model whose internal representation is frozen af-
ter training would allow new task-specific adapters to be
added without disturbing the learned representation, but
this modular design has not been explored in the market-
ing context.
Standard predictive models are insufficient for CATE
recovery.Conventional predictive models such as
MLPs, when used as S-learners, estimate outcomes rather
than treatment effects directly. Without an explicit mech-
anism for counterfactual comparison—such as holding
a latent representation fixed while varying the treatment
input—these models struggle to recover heterogeneous
causal effects, particularly when treatment assignment is
correlated with latent consumer traits.
For these reasons, we adopt a standard DBM for the
world model and incorporate temporal information sim-
ply through lagged features in the visible layer, avoiding
the complexity and instability of recurrent extensions.
3 Proposed Model
We propose a world-model architecture that combines
a Deep Boltzmann Machine (DBM) with multiple task-
specific adapters, supporting three tasks within a single
framework: (i) energy-based consistency evaluation of
consumer trajectories, (ii) prediction of downstream out-
comes such as visit and purchase, and (iii) counterfac-
tual inference of intervention effects. The world model
and the adapters are trained in two stages, and the world
model’s parameters are frozen before any adapter is fit, so
that adding a new downstream task requires training only
a new adapter. Figure 1 summarizes the architecture.
3.1 Visible Layer and Lagged Features
For each consumeriand time indext, we construct a
binary visible vectorv i,t ∈ {0,1}Dv by concatenating
five blocks: (a) static consumer attributes (store, loy-
alty bin, age decade, income quintile), (b) calendar fea-
tures (day-of-week, month), (c) time-varying state sum-
maries derived from the consumer’s history (recent vis-
it/purchase recency dummies and cumulative visit/pur-
chase count thresholds), (d) lagged action indicators for
the pastwsperiods (coupon,campaign,push), and (e)
lagged outcome indicators (visit,purchase) over the
same window. All non-binary attributes are one-hot or
threshold-encoded. Withws= 4the total dimension is
Dv = 72; Table 1 gives the per-block breakdown.
The current-period action vectorz i,t ∈ {0,1}Dz (sale1,
sale2,campaign,coupon,push) is deliberatelynot
placed in the visible layer of the DBM. It is supplied di-
rectly to the adapter (Section 3.4). This separation has two
consequences. First, the DBM learns a representation of
the consumer state that is independent of the current in-
tervention, so the same belief can be reused across coun-
terfactual queries. Second, the adapter is forced to learn
the interaction between the consumer state and the action,
which is precisely the quantity targeted by counterfactual
prediction.
3.2 World Model: Deep Boltzmann Machine
The world model is a Bernoulli–Bernoulli DBM withL
stacked hidden layersh (1), . . . , h(L). Layer sizes are64–
4

Three-in-One World ModelA PREPRINT
Figure 1:Three-in-One world-model architecture.The visible vectorventers a frozen Bernoulli–Bernoulli DBM
with hidden layers of size64–32–16. The beliefb, formed by concatenating mean-field activations of all three hidden
layers, supports three task interfaces on a single shared substrate:(i)the free energyF(v)scores the consistency of
the input trajectory;(ii)a small task-specific adapterg k takes[b;z]and outputs the predictive probabilityˆp k;(iii)
counterfactual outcomes are obtained by holdingbfixed and varying onlyz, since the action vector never enters the
DBM.
32–16in our experiments. The joint energy is
E(v, h) =−v ⊤W (1)h(1) −
L−1X
ℓ=1
h(ℓ)⊤W (ℓ+1)h(ℓ+1)
−b ⊤ v v−
LX
ℓ=1
b⊤ ℓ h(ℓ),(1)
whereW (ℓ) are inter-layer weight matrices andb v, bℓ are
biases. The free energy of a visible configuration,
F(v) =−log
X
h
exp

−E(v, h)

,(2)
is the principal scalar score used for consistency evalua-
tion.
Training follows the standard two-stage procedure for
DBMs [34, 37]: each pair of adjacent layers is greedily
pretrained as an RBM, after which the full network is fine-
tuned jointly using persistent contrastive divergence with
mean-field inference for the data-dependent term. We use
the Adam optimizer [54] for both phases.
3.3 Belief Representation
After training, the DBM is frozen and used as a feature ex-
tractor. For each visible vectorv i,t we run mean-field in-
ference to obtain layerwise activationsµ (ℓ) i,t ∈[0,1] dℓ and
define the belief vector as the concatenation of all hidden
activations,
bi,t =

µ(1) i,t ;µ (2) i,t ;µ (3) i,t  ∈[0,1] d1+d2+d3 .(3)
Including all layers rather than only the topmost layer pre-
serves information at multiple levels of abstraction, allow-
ing each adapter to draw on whichever scale is most infor-
mative for its task. With layer sizes64–32–16, the belief
has dimension112.
3.4 Adapters
For each downstream taskk(e.g., visit prediction, pur-
chase prediction) we train a task-specific adapterg k, in-
stantiated as a small MLP, that takes as input the concate-
nation of the frozen belief and the current-period action
vector,
ˆpk,i,t =σ

gk

[bi,t;z i,t]

.(4)
The world-model parameters are not updated during
adapter training, so adding a new task does not perturb
the belief representation or any previously trained adapter,
avoiding catastrophic forgetting across tasks.
3.5 Three Tasks on a Shared Belief
Consistency evaluation.The free energy in (2) is com-
puted analytically for the Bernoulli–Bernoulli DBM and
serves as a real-valued plausibility score for any visible
configurationv i,t. Becausev i,t contains lagged actions
5

Three-in-One World ModelA PREPRINT
Table 1: Visible-layer composition withws= 4(D v = 72). Variable names match the columns in the simulated panel
data.
Block Variable Dim Description
Static
store {0..9}10 One-hot of the consumer’s home store (10stores)
loyalty11if the consumer is enrolled in the loyalty program
age {20..60}s5 Decade one-hot of age
income q{1..5}5 Quintile one-hot of annual income
month {1..12}12 One-hot of calendar month
dow {0..6}7 One-hot of day-of-week (Monday= 0)
Time-varying
visited within {7,14,30}d31if any visit occurred within the last7/14/30days
purchased within {7,14,30}d31if any purchase occurred within the last7/14/30days
cum visits {5,10,30}plus31if cumulative visits to date≥5/10/30
cum purchases {5,10,30}plus31if cumulative purchases to date≥5/10/30
coupon lag{1..4}4 Coupon issued1–4days ago
campaign lag{1..4}4 Store-level campaign active1–4days ago
push lag{1..4}4 Push notification sent1–4days ago
visit lag{1..4}4 Visit observed1–4days ago
purchase lag{1..4}4 Purchase observed1–4days ago
Total 72
and outcomes, this score evaluates the consistency oftra-
jectoriesrather than static co-occurrence, addressing a
limitation of [13].
Prediction.The adapter outputs the predictive probabil-
ity of each downstream outcome given the current con-
sumer state and the current intervention. Because the be-
lief is frozen, the adapter only has to learn a task-specific
mapping on top of a representation that is already shaped
by the world model.
Counterfactual inference.For any unitiat timet,
individual-level treatment effects are obtained by fixing
the beliefb i,t and toggling a chosen component ofz i,t be-
tween0and1:
\CATEk(i, t;zj) =g k

[bi,t;z (j= 1) i,t ]  −g k  [bi,t;z (j= 0) i,t ]  ,
(5)
wherez (j=v) i,t denotes the action vector with component
jset tov. Because the belief is computed from features
that exclude the current action, this contrast is a counter-
factual in thedo-operator sense [47]: the consumer state
representation is held fixed across the two interventions.
4 Experiments
We evaluate the proposed model on a controlled simu-
lation in which each consumer’s latent traits are known
by construction, allowing direct comparison between esti-
mated CATE and the underlying ground-truth heterogene-
ity.
4.1 Simulation Setup
Each synthetic consumeriis endowed with three latent
parameters that govern their behavior:
•α i: price sensitivity, decreasing in income and age,
•γ i: promotion responsiveness, increasing in loyalty,
•β i: base preference, increasing in income, age, and
loyalty.
Through their shared dependence on demographics,α i
andβ i are negatively confounded via income and age,
whileγ i andβ i are positively confounded via loyalty;α i
andγ i have no direct confounding path. The visit utility
depends onβ i and onγ i multiplied by the active promo-
tional channels; the purchase utility depends onβ i and on
−αi ·price, where price is synthesized causally from the
action variables (price = 100−5·sale1−3·sale2−
5·campaign−r i ·coupon). Visit and purchase outcomes
are then drawn independently from a logistic-Gumbel re-
sponse with noise scale0.10.
We simulateN= 1,024consumers overT= 365
days, yielding312,320training samples after train/valida-
tion/test splitting at the consumer level (validation and test
sets contain30,720samples each). The visible-layer di-
mension isD v = 72with lag windowws= 4, and the ac-
tion vector hasD z = 5components. The DBM uses hid-
den dimensions64–32–16(belief dimension112), each
adapter is an MLP with hidden dimensions64–32–16
trained for up to100epochs with patience30, and the
baseline MLP shares the adapter architecture but con-
sumes raw features instead of the belief.
6

Three-in-One World ModelA PREPRINT
4.2 Energy-Based Consistency Evaluation
We probe whether the DBM’s free energy in (2) re-
sponds to a counterfactually clamped trajectory in a man-
ner that reflects latent consumer heterogeneity. From
each split we keep samples whose visible vector origi-
nally records no recent purchase (purchase lag1:4 = 0),
and clamp the visible layer to a “purchasing without re-
cent promotion” configuration:purchase lag1:4 = 1,
purchased within 7d= 1, andcampaign lag1:4 =
push lag1:4 = 0. All other visible units are left at their
observed values. The free energy change
∆F(v) =F(v clamped)−F(v original)(6)
quantifies how much less plausible the DBM judges the
clamped trajectory than the original. Figure 2 visualizes
the resulting distributions on the test split, and Table 2
reports the corresponding statistics across all three splits.
Table 2(a) shows that∆Fis systematically positive on ev-
ery split: the DBM treats “the consumer purchased on ev-
ery recent day but received neither campaigns nor pushes”
as substantially less plausible than the corresponding ob-
served trajectory, with overwhelming significance under
both a pairedt-test and a Wilcoxon signed-rank test.
Because the clamp targets lagged actions and outcomes
rather than a single-period co-occurrence pattern, this is a
property the static DBM of [13] cannot exhibit: the con-
sistency check here operates on time-extended trajecto-
ries.
Table 2(b) further shows that the penalty is heterogeneous
in the latent base preference. Splitting the eligible samples
at the median of the ground-truthβi yields a smaller mean
∆Ffor the high-βgroup than for the low-βgroup on ev-
ery split, with the gap significant under both Welch’st-test
and the Mann–WhitneyUtest. “Purchasing without pro-
motion” is therefore less surprising to the DBM precisely
when the consumer’s observed covariates already predict
a high intrinsic preference. The DBM is trained without
access toβ i, so this dependence emerges purely through
the demographic-to-belief mapping that the world model
learns. This is the energy-side counterpart of the disentan-
glement signal observed in CATE recovery (Section 4.4):
the same belief that supports counterfactual contrasts in
the adapter also shapes the energy landscape in aβ-aware
direction.
4.3 Prediction Performance
We first verify that compressing the72-dimensional in-
put into a112-dimensional frozen belief does not dam-
age predictive power. Table 3 compares the test-set AUC
of the baseline MLP, which consumes the raw features
and the current action, against the adapter that consumes
the frozen belief and the current action. The two are
within0.001–0.002AUC of each other on both tasks. The
adapter even matches or slightly exceeds the baseline on
visit prediction. We conclude that the DBM’s representa-
tion retains the predictive content of the input.
4.4 CATE Recovery
We next evaluate whether the adapter, when used for
counterfactual prediction, recovers the true heterogeneity
of treatment effects across consumers. We consider two
interventions whose causal structure differs:
•push→visit, whose effect in the data-generating pro-
cess is governed by the promotion-responsiveness pa-
rameterγ i and which is unconfounded withα i;
•sale1→purchase, whose effect operates through the
price channel and is governed by the price-sensitivity
parameterα i, withα i andβ i confounded through in-
come and age.
For each intervention, we compute estimated CATE on the
test set under six models—S-learner, T-learner, X-learner,
DR-learner, Causal Forest [50, 48, 49], and the proposed
Belief Adapter—all using the same raw features for the
meta-learners and the frozen belief for the adapter. The X-
learner and DR-learner use random-forest base learners,
with the DR-learner additionally relying on2-fold cross-
fitting for its nuisance estimates. As the principal metric,
we report the Spearman rank correlationρbetween the es-
timated CATE and each true latent parameter on the logit
scale, which removes the sigmoid compression that dis-
torts probability-scale CATE.
Table 4 summarizes the results. On both interventions,
the adapter attains the highest rank correlation between
estimated CATE and the target latent parameter. For the
unconfoundedpush→visit intervention, the gap is mod-
erate (ρ γ = +0.625vs.+0.579for the strongest meta-
learner baseline). For the confoundedsale1→purchase
intervention, the gap widens substantially: the adapter re-
coversρ α = +0.548, whereas the T-learner and Causal
Forest, which are well known to be sensitive to limited
overlap and confounded treatment assignment [48, 50],
drop to+0.161and+0.040, respectively. The X-learner
and DR-learner, despite being explicitly designed to mit-
igate the limitations of T-learner and to deliver dou-
bly robust pseudo-outcome regression, only reachρ α =
+0.123and−0.016in this setting, plausibly because their
random-forest base learners and cross-fitting introduce
additional variance on top of an already noisy treated/con-
trol split. The S-learner remains competitive at+0.406
but is still outperformed by the adapter by more than0.14
inρ.
A second observation concerns leakage to nuisance pa-
rameters. Although the X-learner, DR-learner, and Causal
Forest record relatively low absolute correlations with the
target, they also exhibit small magnitudes on the irrele-
vant parameters: onpush→visit,|ρ α|stays below0.08
for all three, and onsale1→purchase,|ρ γ|stays be-
low0.07. The S-learner and T-learner show larger spu-
rious correlations with the confound parameter, reflecting
their reliance on a single outcome model whose treatment-
feature interactions can absorb confounded variation. The
adapter, by contrast, achieves both the strongest target-
parameter recovery and a sizable confound correlation
7

Three-in-One World ModelA PREPRINT
Figure 2:Energy-based consistency under the “purchasing without recent promotion” clamp(test split, eligible
n= 12,432).(a)Free energy distributions before (observedF(v)) and after (clampedF(v ′)) the clamp; the clamp
shifts the mean rightward by ∆F= +1.07.(b)Distributions of∆F=F(v clamped)−F(v original)split at the median
of the ground-truth base preferenceβ i; the high-βgroup (orange) receives a uniformly smaller penalty than the low-β
group (teal), although within-group dispersion remains substantial. All reported test statistics are highly significant
(p <0.001); cross-split numerical values are in Table 2.
that, by construction of the simulator, is in the direction
implied by the latent confounding path.
The adapter also exhibits stronger negative correlation
with the confound (β) onsale1→purchase (ρ β =
−0.597). Becauseα i andβ i are negatively confounded
by construction, this is consistent with the adapter relying
onα-aligned information rather than onβ-aligned short-
cuts; we caution, however, that with a single confounding
path the two interpretations cannot be fully distinguished
from this experiment alone. The cleanerpush→visit re-
sult, in whichγis recovered whileαremains near zero,
supports the view that the belief carries identifiable, sepa-
rable information about distinct latent traits.
Taken together, Table 3 and Table 4 indicate that the
DBM’s belief representation does not merely match raw-
feature predictors on outcome accuracy but provides a
substrate on which counterfactual contrasts recover het-
erogeneous effects more faithfully than standard meta-
learners (S-, T-, X-, and DR-learner) and Causal Forest
applied to the same features.
5 Conclusion
We have proposed a Three-in-One world-model architec-
ture for marketing intervention in which a frozen DBM
provides a belief representation that simultaneously sup-
ports energy-based consistency evaluation, outcome pre-
diction, and counterfactual inference. The design sepa-
rates a heavyweight world model from lightweight task-
specific adapters, mirroring the asymmetry between envi-
ronment models and controllers in [8], and incorporates
time-varying information through lagged features in the
visible layer instead of recurrent connections.
In a controlled simulation with known latent traits, pre-
diction adapters matched a strong MLP baseline on test-
set AUC for visit and purchase while recovering hetero-
geneous treatment effects substantially better than S-, T-
, X-, and DR-learner meta-learners and a Causal Forest
baseline. The advantage was largest for a confounded
price-promotion intervention, where the price-sensitivity
parameter is easily masked by the negatively confounded
base preference. Free-energy clamps further showed that
the DBM penalizes counterfactual purchase trajectories
without prior promotional exposure, with the penalty
itself heterogeneous in the latent base preference—an
energy-side counterpart to the disentanglement signal ob-
served in CATE recovery. These findings suggest that
DBM-based world models can provide a unified substrate
for prediction, consistency evaluation, and causal-effect
estimation in marketing settings where latent heterogene-
ity drives intervention response.
Several limitations remain. All experiments rely on a
single simulation seed and a single data-generating pro-
cess; replication across seeds and across alternative DGPs
is needed to characterize the variance and the condi-
tions under which the advantages of the world-model
adapter and of the energy-based consistency signal per-
sist. The energy-based analysis additionally examines a
single clamp specification (purchasing without recent pro-
motion) and reports a population-level effect: although
the high-versus-low-βgap in ∆Fis highly significant,
within-group dispersion is large enough that∆Falone
is not a sample-level classifier of latent type. Sensitivity
to alternative counterfactual configurations—for example,
implausible promotional bursts on consumers whose his-
tory shows no engagement—remains to be characterized.
We also restrict attention to a single product category
and binary outcomes; extension to multiple products via
8

Three-in-One World ModelA PREPRINT
Table 2: Energy-based consistency across data splits. Panel (a):∆Ftested against zero. Panel (b):∆Fsplit at the
median of the ground-truth base-preference parameterβ i. Eligiblencounts samples whose visible vector originally
haspurchase lag1:4 = 0. Within-group standard deviations of∆Fare reported in parentheses.
Train Val Test
Eligiblen129,568 12,694 12,432
(a) Penalty against zero
Pairedt198.25 24.68 26.69
p(pairedt)<0.001<0.001<0.001
p(Wilcoxon)<0.001<0.001<0.001
(b) Median split onβ i
nhigh/nlow 64,792/64,776 6,352/6,342 6,229/6,203
∆Fhigh-β1.85 (3.84) 0.65 (4.18) 0.77 (4.11)
∆Flow-β3.09 (4.97) 1.36 (4.93) 1.38 (4.79)
Welcht−50.27−8.64−7.66
p(Welch)<0.001<0.001<0.001
p(Mann–Whitney)<0.001<0.001<0.001
Table 3: Test-set AUC for visit and purchase prediction.
Baseline MLPconsumes raw features and the current ac-
tion;Belief Adapterconsumes the frozen belief and the
current action.
Task MLP Belief Adapter Gap
visit0.7119 0.7130 +0.0011
purchase0.6777 0.6772−0.0005
choice models, to continuous outcomes such as session
length and basket value, and to real A/B-test data are natu-
ral next steps. Finally, learning optimal intervention poli-
cies on top of the world model—closing the loop between
belief, adapter, and controller in the sense of [8]—remains
for future work.
References
[1] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
Kaiser, and Illia Polosukhin. Attention is all you
need.Advances in neural information processing
systems, 30, 2017.
[2] Alec Radford, Karthik Narasimhan, Tim Salimans,
Ilya Sutskever, et al. Improving language under-
standing by generative pre-training. 2018.
[3] Alec Radford, Jeffrey Wu, Rewon Child, David
Luan, Dario Amodei, Ilya Sutskever, et al. Language
models are unsupervised multitask learners.OpenAI
blog, 1(8):9, 2019.
[4] Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. Language models are few-shot learn-
ers.Advances in neural information processing sys-
tems, 33:1877–1901, 2020.
[5] OpenAI. Gpt-4 technical report.arXiv preprint
arXiv:2303.08774, 2023.
[6] Jared Kaplan, Sam McCandlish, Tom Henighan,
Tom B Brown, Benjamin Chess, Rewon Child, Scott
Gray, Alec Radford, Jeffrey Wu, and Dario Amodei.
Scaling laws for neural language models.arXiv
preprint arXiv:2001.08361, 2020.
[7] Yann LeCun. A path towards autonomous machine
intelligence version 0.9. 2, 2022-06-27.Open Re-
view, 62(1):1–62, 2022.
[8] David Ha and J ¨urgen Schmidhuber. World models.
arXiv preprint arXiv:1803.10122, 2(3), 2018.
[9] Mahmoud Assran, Quentin Duval, Ishan Misra,
Piotr Bojanowski, Pascal Vincent, Michael Rab-
bat, Yann LeCun, and Nicolas Ballas. Self-
supervised learning from images with a joint-
embedding predictive architecture. InProceedings
of the IEEE/CVF Conference on Computer Vision
and Pattern Recognition, pages 15619–15629, 2023.
[10] Adrien Bardes, Quentin Garrido, Jean Ponce, Xinlei
Chen, Michael Rabbat, Yann LeCun, Mido Assran,
and Nicolas Ballas. V-jepa: Latent video prediction
for visual representation learning. 2023.
[11] Quentin Garrido, Mahmoud Assran, Nicolas Bal-
las, Adrien Bardes, Laurent Najman, and Yann
LeCun. Learning and leveraging world models
in visual representation learning.arXiv preprint
arXiv:2403.00504, 2024.
[12] Jingtao Ding, Yunke Zhang, Yu Shang, Yuheng
Zhang, Zefang Zong, Jie Feng, Yuan Yuan,
Hongyuan Su, Nian Li, Nicholas Sukiennik, et al.
Understanding world or predicting future? a com-
prehensive survey of world models.ACM Comput-
ing Surveys, 58(3):1–38, 2025.
[13] Junichiro Niimi. the mouth is not the brain: Bridg-
ing energy-based world models and language gen-
9

Three-in-One World ModelA PREPRINT
Table 4: CATE recovery: Spearmanρbetween estimated CATE (logit scale) and true latent parameters on the test
set.Boldindicates the best recovery of the target parameter for each intervention.S: S-learner.T: T-learner.XL:
X-learner with random-forest base learners [48].DR: DR-learner [49] with random-forest nuisance models and 2-fold
cross-fitting.CF: Causal Forest.Adapter: belief adapter (proposed). XL, DR, and CF report risk-difference uplift, so
the logit-scale and probability-scale columns coincide for these estimators.
Intervention Param S T XL DR CF Adapter
push→visit
α(irrelevant)+0.004−0.284 +0.043−0.008 +0.071−0.148
β(confound)+0.204 +0.441 +0.067 +0.079 +0.063 +0.377
γ(target)+0.579 +0.558 +0.318 +0.194 +0.350 +0.625
sale1→purchase
α(target)+0.406 +0.161 +0.123−0.016 +0.040 +0.548
β(confound)−0.394−0.154−0.154−0.004−0.044−0.597
γ(irrelevant)−0.043−0.027−0.060−0.042−0.006−0.306
eration. InThe 2nd Workshop for World Models in
The Fourteenth International Conference on Learn-
ing Representations (ICLR 2026), 2026.
[14] Jan Ole Krugmann and Jochen Hartmann. Sentiment
analysis in the age of generative ai.Customer Needs
and Solutions, 11(1):3, 2024.
[15] Yaxuan Kong, Yuqi Nie, Xiaowen Dong, John M
Mulvey, H Vincent Poor, Qingsong Wen, and Stefan
Zohren. Large language models for financial and
investment management: Applications and bench-
marks.Journal of Portfolio Management, 51(2),
2024.
[16] Enkelejda Kasneci, Kathrin Seßler, Stefan
K¨uchemann, Maria Bannert, Daryna Demen-
tieva, Frank Fischer, Urs Gasser, Georg Groh,
Stephan G ¨unnemann, Eyke H ¨ullermeier, et al.
Chatgpt for good? on opportunities and challenges
of large language models for education.Learning
and individual differences, 103:102274, 2023.
[17] Qiyao Peng, Hongtao Liu, Hongyan Xu, Qing Yang,
Minglai Shao, and Wenjun Wang. Llm: Harnessing
large language models for personalized review gen-
eration.arXiv preprint arXiv:2407.07487, 2024.
[18] Konstantinos I Roumeliotis, Nikolaos D Tselikas,
and Dimitrios K Nasiopoulos. Llms in e-commerce:
a comparative analysis of gpt and llama models in
product review evaluation.Natural Language Pro-
cessing Journal, 6:100056, 2024.
[19] Ang Li, Haozhe Chen, Hongseok Namkoong, and
Tianyi Peng. LLM generated persona is a promise
with a catch. InThe Thirty-Ninth Annual Conference
on Neural Information Processing Systems Position
Paper Track, 2025.
[20] Yu-Min Tseng, Yu-Chao Huang, Teng-Yun Hsiao,
Wei-Lin Chen, Chao-Wei Huang, Yu Meng, and
Yun-Nung Chen. Two tales of persona in llms: A
survey of role-playing and personalization. InFind-
ings of the Association for Computational Linguis-
tics: EMNLP 2024, pages 16612–16631, 2024.
[21] Kenneth Li, Aspen K Hopkins, David Bau, Fer-
nanda Vi ´egas, Hanspeter Pfister, and Martin Wat-
tenberg. Emergent world representations: Explor-
ing a sequence model trained on a synthetic task. In
The Eleventh International Conference on Learning
Representations.
[22] Neel Nanda, Andrew Lee, and Martin Wattenberg.
Emergent linear representations in world models of
self-supervised sequence models. InProceedings of
the 6th BlackboxNLP Workshop: Analyzing and In-
terpreting Neural Networks for NLP, pages 16–30,
2023.
[23] Adam Karvonen. Emergent world models and la-
tent variable estimation in chess-playing language
models. InFirst Conference on Language Model-
ing, 2024.
[24] Alexander F Spies, William Edwards, Michael Ivan-
itskiy, Adrians Skapars, Tilman R ¨auker, Katsumi
Inoue, Alessandra Russo, and Murray Shanahan.
Transformers use causal world models in maze-
solving tasks. InICLR 2025 Workshop on World
Models: Understanding, Modelling and Scaling,
2025.
[25] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai,
Meredith Ringel Morris, Percy Liang, and Michael S
Bernstein. Generative agents: Interactive simulacra
of human behavior. InProceedings of the 36th an-
nual acm symposium on user interface software and
technology, pages 1–22, 2023.
[26] Yuwei Yan, Qingbin Zeng, Zhiheng Zheng, Jingzhe
Yuan, Jie Feng, Jun Zhang, Fengli Xu, and Yong
Li. Opencity: A scalable platform to simulate urban
activities with massive llm agents.arXiv preprint
arXiv:2410.21286, 2024.
[27] Emily M Bender and Alexander Koller. Climbing
towards nlu: On meaning, form, and understanding
in the age of data. InProceedings of the 58th an-
nual meeting of the association for computational
linguistics, pages 5185–5198, 2020.
[28] Emily M Bender, Timnit Gebru, Angelina
McMillan-Major, and Shmargaret Shmitchell.
On the dangers of stochastic parrots: Can language
models be too big? InProceedings of the 2021
10

Three-in-One World ModelA PREPRINT
ACM conference on fairness, accountability, and
transparency, pages 610–623, 2021.
[29] Xinji Mai, Zeng Tao, Junxiong Lin, Haoran Wang,
Yang Chang, Yanlan Kang, Yan Wang, and Wen-
qiang Zhang. From efficient multimodal mod-
els to world models: A survey.arXiv preprint
arXiv:2407.00118, 2024.
[30] J ¨urgen Schmidhuber. On learning to think: Algorith-
mic information theory for novel combinations of re-
inforcement learning controllers and recurrent neu-
ral world models.arXiv preprint arXiv:1511.09249,
2015.
[31] Yann LeCun, Sumit Chopra, Raia Hadsell, M Ran-
zato, Fujie Huang, et al. A tutorial on energy-based
learning.Predicting structured data, 1(0), 2006.
[32] Shuangfei Zhai, Yu Cheng, Weining Lu, and
Zhongfei Zhang. Deep structured energy based
models for anomaly detection. InInternational
conference on machine learning, pages 1100–1109.
PMLR, 2016.
[33] Alexi Gladstone, Ganesh Nanduru, Md Mofijul Is-
lam, Aman Chadha, Jundong Li, and Tariq Iqbal.
Cognitively inspired energy-based world models.
arXiv preprint arXiv:2406.08862, 2024.
[34] Ruslan Salakhutdinov and Geoffrey Hinton. Deep
boltzmann machines. InArtificial intelligence and
statistics, pages 448–455. PMLR, 2009.
[35] Paul Smolensky. Information processing in dynami-
cal systems: Foundations of harmony theory. Tech-
nical report, 1986.
[36] Geoffrey E Hinton. A practical guide to training re-
stricted boltzmann machines. InNeural Networks:
Tricks of the Trade: Second Edition, pages 599–619.
Springer, 2012.
[37] David H Ackley, Geoffrey E Hinton, and Terrence J
Sejnowski. A learning algorithm for boltzmann ma-
chines.Cognitive science, 9(1):147–169, 1985.
[38] Graham W Taylor, Geoffrey E Hinton, and Sam
Roweis. Modeling human motion using binary la-
tent variables.Advances in neural information pro-
cessing systems, 19, 2006.
[39] Graham W Taylor and Geoffrey E Hinton. Factored
conditional restricted boltzmann machines for mod-
eling motion style. InProceedings of the 26th an-
nual international conference on machine learning,
pages 1025–1032, 2009.
[40] Ilya Sutskever, Geoffrey E Hinton, and Graham W
Taylor. The recurrent temporal restricted boltzmann
machine.Advances in neural information process-
ing systems, 21, 2008.
[41] Nicolas Boulanger-Lewandowski, Yoshua Bengio,
and Pascal Vincent. Modeling temporal depen-
dencies in high-dimensional sequences: Application
to polyphonic music generation and transcription.
2012.
[42] Roni Mittelman, Benjamin Kuipers, Silvio Savarese,
and Honglak Lee. Structured recurrent temporal re-
stricted boltzmann machines. InInternational Con-
ference on Machine Learning, pages 1647–1655.
PMLR, 2014.
[43] David E Rumelhart, Geoffrey E Hinton, and
Ronald J Williams. Learning representations by
back-propagating errors.nature, 323(6088):533–
536, 1986.
[44] Paul J Werbos. Backpropagation through time: what
it does and how to do it.Proceedings of the IEEE,
78(10):1550–1560, 2002.
[45] Ronald J Williams and David Zipser. Gradient-
based learning algorithms for recurrent networks
and their computational complexity. InBackprop-
agation, pages 433–486. Psychology Press, 2013.
[46] Donald B Rubin. Causal inference using potential
outcomes: Design, modeling, decisions.Journal of
the American statistical Association, 100(469):322–
331, 2005.
[47] Judea Pearl.Causality. Cambridge university press,
2009.
[48] S ¨oren R K ¨unzel, Jasjeet S Sekhon, Peter J Bickel,
and Bin Yu. Metalearners for estimating hetero-
geneous treatment effects using machine learning.
Proceedings of the national academy of sciences,
116(10):4156–4165, 2019.
[49] Edward H Kennedy. Towards optimal doubly robust
estimation of heterogeneous causal effects.Elec-
tronic Journal of Statistics, 17(2):3008–3049, 2023.
[50] Stefan Wager and Susan Athey. Estimation and
inference of heterogeneous treatment effects using
random forests.Journal of the American Statistical
Association, 113(523):1228–1242, 2018.
[51] Nicholas Radcliffe. Using control groups to tar-
get on predicted lift: Building and assessing uplift
model. 2007.
[52] Eustache Diemert, Artem Betlei, Christophe Re-
naudin, and Massih-Reza Amini. A large scale
benchmark for uplift modeling. InKDD, 2018.
[53] Piotr Rzepakowski and Szymon Jaroszewicz. Deci-
sion trees for uplift modeling with single and multi-
ple treatments.Knowledge and Information Systems,
32(2):303–327, 2012.
[54] Diederik P. Kingma and Jimmy Ba. Adam: A
method for stochastic optimization. In Yoshua Ben-
gio and Yann LeCun, editors,3rd International Con-
ference on Learning Representations, ICLR 2015,
San Diego, CA, USA, May 7-9, 2015, Conference
Track Proceedings, 2015.
11
