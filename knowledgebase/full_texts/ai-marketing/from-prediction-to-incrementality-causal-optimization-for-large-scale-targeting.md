---
title: 'From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation'
url: https://arxiv.org/abs/2608.10182
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Changshuai Wei
- John Bencina
- Phuc Nguyen
- Andre Assuncao Silva T Ribeiro
- Benjamin Zelditch
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.10182
pages: 10
chars: 55635
fetched_at: '2026-11-08T12:57:33+00:00'
kb_version: 1
---

# From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation

From Prediction to Incrementality: Causal Optimization for
Large-Scale Targeting and Recommendation
Changshuai Wei∗†
chawei@linkedin.com
LinkedIn
Seattle, USA
John Bencina∗
jbencina@linkedin.com
LinkedIn
Sunnyvale, USA
Phuc Nguyen∗
honnguyen@linkedin.com
LinkedIn
Sunnyvale, USA
Andre Assuncao Silva T
Ribeiro∗
aribeiro@linkedin.com
LinkedIn
Sunnyvale, USA
Benjamin Zelditch
bzelditch@linkedin.com
LinkedIn
Sunnyvale, USA
Abstract
Large-scale targeting and recommendation systems are typically
built around predictive scores fed into heuristic or local allocation.
When the business goal is incremental impact, as in marketing
campaigns, incentives, and notifications, this paradigm systemati-
cally misallocates resources toward users who would have acted
anyway. We present a decision-centric framework that instead
optimizes causal effects under global constraints, aligning three
components under a single objective: a causal neural network with
a Transformer backbone for individual treatment-effect estima-
tion, a Bayesian neural-bandit layer for uncertainty-aware explo-
ration, and a dual-based large-scale linear-programming layer for
constrained allocation. The framework also supports sequential
context and multi-outcome, attribute-conditioned scoring through
a Transformer encoder and outcome embeddings. We evaluate it
with offline simulations on a public bandit dataset, targeted architec-
tural ablations, and an online A/B test on LinkedIn Feed marketing
traffic. We also distill production lessons on causal training-data
construction and cost and delivery control, which were critical to
successful deployment. The end-to-end treatment policy delivered
a statistically significant+7.20%lift in the primary long-term-value
metric, demonstrating the feasibility of production-scale causal
optimization under business constraints.
CCS Concepts
•Mathematics of computing → Probability and statistics;•
Computing methodologies→ Machine learning;•Informa-
tion systems→Information retrieval.
Keywords
Causal ML, Transformer, Bandit, Linear Program
1 Introduction
Large-scale targeting and recommendation systems are a core com-
ponent of modern online platforms, supporting applications such as
advertising, marketing outreach, notifications, and content recom-
mendation. In practice, these systems are typically built by training
predictive models to estimate user response probabilities (such as
∗These authors contributed equally
†Corresponding Author
click-through or conversion likelihood) and then ranking or select-
ing items based on these predictions. This paradigm has proven
effective for optimizing engagement metrics at scale and has be-
come the dominant approach in both industrial deployments and
academic research.
However, predictive modeling alone is fundamentally misaligned
with the objectives of many real-world targeting problems. In mar-
keting and incentive-driven settings, the goal is not to predict out-
comes under historical policies, but to estimate theincremental
impactof an intervention relative to a counterfactual baseline. Ob-
served user responses are confounded by prior targeting decisions,
exposure mechanisms, and user self-selection, implying that high
predicted response does not necessarily correspond to high causal
value. Prior work has demonstrated that learning and evaluation
based on biased recommendation logs can systematically misesti-
mate the true effect of interventions when deployed for decision-
making [33, 42].
This challenge has motivated increasing interest incausal ma-
chine learningfor recommender and targeting systems. A line of
work reframes recommendations as treatments and user interac-
tions as potential outcomes, enabling principled correction for expo-
sure bias and confounding [5, 33]. More broadly, causal perspectives
on recommendation have been surveyed extensively, highlighting
the limitations of purely predictive approaches and emphasizing
the role of causal inference in reliable decision-making [17].
In marketing and targeting applications, uplift modeling and
treatment effect estimation explicitly target incrementality by esti-
mating individual-level causal effects rather than response proba-
bilities. Foundational work has studied the theoretical properties of
individual treatment effect estimation and proposed representation-
learning-based approaches to mitigate confounding bias [34]. More
recent neural architectures, such as DragonNet, jointly model poten-
tial outcomes and treatment assignment, demonstrating improved
stability and accuracy in treatment effect estimation [35].
Complementary to causal modeling, a rich literature studies
counterfactual evaluation and learning from logged bandit feed-
back. Off-policy evaluation methods enable unbiased estimation of
policy value without exhaustive online experimentation and have
been extended to large action spaces and slate recommendation
settings [24, 39]. While these approaches provide principled tools
arXiv:2608.10182v1  [cs.LG]  10 Aug 2026

Changshuai Wei, John Bencina, Phuc Nguyen, Andre Assuncao Silva T Ribeiro, and Benjamin Zelditch
for evaluation and exploration, they typically focus on estimating or
comparing policies rather than optimizing decisions for incremental
outcomes.
At the same time, real-world targeting and recommendation
systems must operate under complex global constraints, includ-
ing budgets, capacity limits, frequency caps, and coverage or fair-
ness requirements. To address these challenges, many industrial
platforms rely on large-scale constrained optimization, often for-
mulated as linear or mixed-integer programs, to translate model
outputs into coordinated decisions. Theoretical foundations for
robust and constrained optimization are well established [3], and
industrial systems have demonstrated the effectiveness of combin-
ing learned utility models with constraint-aware optimization to
improve system-level objectives [1, 23, 43].
Despite their success, existing optimization-based systems al-
most universally rely onpredictivescores or locally estimated uplift
values as inputs. When incrementality matters, optimizing con-
strained decisions using non-causal or locally optimal signals can
systematically misallocate resources toward users who would have
acted regardless of intervention, thereby reducing true return on
investment. Conversely, causal effect estimates alone are insuffi-
cient without a principled optimization layer to enforce constraints
and optimize system-level objectives.
We present adecision-centricformulation in which incremen-
tality and constraints are addressed jointly: the system optimizes
causal effects under global constraints, replacing the more common
pattern of optimizing predictive or proxy signals under heuristic
allocation. This reframes targeting as choosing users with high
incremental impact and as globally coordinated allocation, rather
than as ranking high-response users. The three components fit
together naturally under this objective: causal modeling defines
what is optimized, uncertainty-aware exploration shapes the data
on which the causal estimates are learned, and constrained opti-
mization translates those estimates into feasible decisions under
shared resources. We instantiate the framework with a Transformer-
augmented DragonNet causal head, a Bayesian neural-bandit layer,
and a large-scale LP layer. While our primary motivation arises
from marketing, the formulation is not domain-specific and extends
to other settings that allocate limited intervention capacity under
constraints.
Our contributions are: (i) a decision-centric formulation that
aligns causal estimation, exploration, and constrained allocation
under a single objective; (ii) two DragonNet architectural exten-
sions, a Transformer encoder for marketing-touchpoint sequences
and a shared outcome-embedding head, for multi-outcome and
attribute-conditioned incremental scoring; and (iii) a production-
ized pipeline combining the causal head with neural-bandit explo-
ration and a dual-based large-scale LP solver, evaluated on a public
bandit dataset and as an end-to-end policy in a large online A/B
test on LinkedIn Feed marketing traffic that delivered a+7.20%lift
in the primary KPI (𝑝=0.041).
1.1 Related Work
Recent work has begun to incorporate treatment effect estimation
and uplift modeling directly into recommender systems, moving
beyond purely predictive objectives. Chen et al. [ 7] propose us-
ing individual treatment effect estimation to guide user interest
exploration, demonstrating that causal signals can improve explo-
ration efficiency compared to prediction-based uncertainty. Meng
et al. [25] introduce a coarse-to-fine dynamic uplift modeling frame-
work for real-time video recommendation, showing that explicit up-
lift estimation can improve ranking quality at scale. Sun et al. [37]
study incentive recommendation under budget constraints and
propose an end-to-end uplift-based framework to improve cost-
effectiveness.
While these approaches demonstrate the practical value of causal
and uplift modeling in recommender systems, they primarily focus
onlocal decision-making, such as improving ranking quality or
applying uplift-based heuristics under relatively simple constraints.
Exploration is typically handled implicitly or through heuristic
mechanisms, and optimization is performed at the level of individual
users or items rather than as a coordinated system-level problem.
In contrast, our work integratescausal effect estimation, princi-
pled exploration, and constrained optimizationinto a unified decision
framework. We combine DragonNet-style causal modeling with
Transformer-based sequential representations and a neural bandit
layer, enabling uncertainty-aware exploration guided by estimated
incremental effects. On the optimization side, we formulate target-
ing decisions as a large-scale constrained optimization problem and
solve it using a dual-based approach that scales to extreme problem
sizes. This allows us to coordinate decisions across users, items,
and campaigns while enforcing complex global constraints, going
beyond ranking-based or locally optimal uplift methods.
2 Incremental Optimization Framework
2.1 Incremental Modeling
Incremental optimization requires estimating user-level treatment
effects that quantify the expected lift from a targeting or recommen-
dation action. Under the potential outcomes framework, let𝑌( 1)
and𝑌( 0) denote the potential outcomes under treatment (𝑇= 1)
and control (𝑇= 0), and let 𝑋∈X denote observed covariates.
The Conditional Average Treatment Effect (CATE), or Individual
Treatment Effect (ITE) at the covariate level, is
𝜏(𝑋)=E[𝑌(1)−𝑌(0)|𝑋]=𝜇 1(𝑋)−𝜇 0(𝑋),(1)
where𝜇𝑡(𝑋)=E[𝑌(𝑡)|𝑋] . Two standard assumptions identify
𝜏(𝑋) from observational data:unconfoundedness, {𝑌( 0),𝑌( 1)}⊥
⊥𝑇|𝑋 , andoverlap,0 <𝑒(𝑋)< 1for all 𝑋 , where 𝑒(𝑋)=
𝑃(𝑇= 1|𝑋) is the propensity score. Under these,𝜇𝑡(𝑋)=E[𝑌|
𝑋,𝑇=𝑡] and𝜏(𝑋) becomes point-identified from the observed
data distribution.
Various estimators for𝜏(𝑋) have been proposed, including S-
Learner, T-Learner, X-Learner, and Double Machine Learning (DML)
[9, 21]. These approaches typically require multi-stage modeling
pipelines, which introduce operational complexity at our scale of
hundreds of millions of members. We instead adopt a modified ver-
sion of DragonNet [35], shown in Figure 1, which jointly estimates
𝜇1(𝑋),𝜇 0(𝑋), and𝑒(𝑋)in a single forward pass.
DragonNet extends TARNET [34] by adding a propensity head to
a shared-representation architecture: a shared encoder Φ feeds two

From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation
Figure 1: Incremental model architecture overview. The model extends DragonNet with a transformer for temporal modeling
and outcome embeddings for multi-product prediction. The core model utilizes member-level embeddings, dense features, and
the marketing interaction sequence. The auxiliary autoencoder model utilizes product-level embeddings corresponding to
each modeled outcome.
outcome heads estimating𝜇1 and𝜇0 (with observed-treatment gra-
dient routing), and a third head estimating𝑒(𝑋) . The motivation
is propensity sufficiency: under unconfoundedness, the propen-
sity score is a balancing score, so any representation Φ that pre-
serves𝑒(𝑋) retains all information needed for CATE estimation.
Outcome-only training tends to discard propensity signal in pursuit
of marginal-likelihood fit, biasing ˆ𝜏= ˆ𝜇1− ˆ𝜇0 toward the dominant
treatment arm. Jointly optimizing the propensity head therefore
acts as an architectural regularizer on Φ, and in practice yields
markedly more stable CATE estimates [35].
We extend DragonNet with three key enhancements for rec-
ommender systems. First, we feed sequential user-event features
through a transformer layer (Section 3) before they enter Φ, let-
ting the encoder absorb temporal context such as recency and
engagement cadence. Second, we extend the outcome heads to a
multi-outcome configuration using learned product embeddings,
so the model can score newly introduced products without adding
a product-specific output head. Third, and more importantly, we
couple this causal predictor with the neural bandit in Section 2.2,
forming aDragonBanditpolicy that explores over incremental ac-
tion values rather than predicted responses.
2.2 Neural Bandit Exploration
Reliance on logged data without any mechanism for exploration
reinforces feedback loops, leading to “rich-get-richer” dynamics
and suboptimal long-term performance [22, 27, 36, 38]. For causal
modeling, exploration is additionally important to improve overlap
and reduce dependence on the incumbent logging policy [19, 33],
supporting causal identification where the required assumptions
hold [26]. At each round, DragonBandit draws posterior incremen-
tal scores rather than passing deterministic point estimates to the
allocator in Section 2.3. The multi-turn simulation examines this
mechanism under feedback-loop bias.
Letℎ𝑡 denote the history and remaining constraint capacity
at round 𝑡,C𝑡(ℎ𝑡) the corresponding feasible set, and 𝑥∗ 𝑡( ˜𝜏𝑡) its
sampled-score solution. For nonzero exploration, the sampled log-
its have a nondegenerate Gaussian distribution; because the sig-
moid heads are monotone, every open score ordering has positive
probability. Therefore,
𝜋𝛼(𝑖|𝑢,ℎ 𝑡)=Pr

𝑥∗ 𝑢,𝑖,𝑡( ˜𝜏𝑡)=1|ℎ 𝑡  >0(2)
for every(𝑢,𝑖) contained in some𝑥𝑡∈C 𝑡(ℎ𝑡). Thus exploration
guarantees positivity conditional on the feasible action.
2.2.1 Neural Thompson sampling via Laplace approximation.We
approximate the posterior over network parameters by a Gauss-
ian centered at the MAP solution ˆ𝜃MAP via the linearized Laplace
approximation (LLA) [12, 15, 30, 36]. The LLA computes the Gauss–
Newton curvature of the log-likelihood at ˆ𝜃MAP and propagates
it through the network’s local linearization, yielding a closed-
form Gaussian on the logit𝑓𝜃(𝑥∗) with mean𝑓 ˆ𝜃(𝑥∗) and variance
𝜎 2 0+𝑔(𝑥 ∗)⊤Ω−1𝑔(𝑥∗), where 𝑔(𝑥∗) is the Jacobian and Ω is the
curvature matrix. Thompson sampling proceeds by drawing a logit
sample and applying𝜎(·) , so the same supervised checkpoint can be
deployed with or without exploration and no retraining is required.
Production scale is achieved through lightweight curvature approx-
imations (low-rank, diagonal, or last-layer variants [28, 31, 45]); we
use the last-layer variant for our pretrained DragonNet.
We also evaluated Bayes by Backprop (Appendix B.1) offline, but
use LLA in production because it adds uncertainty sampling to the
existing checkpoint with substantially lower training and serving
overhead.

Changshuai Wei, John Bencina, Phuc Nguyen, Andre Assuncao Silva T Ribeiro, and Benjamin Zelditch
2.3 Large-scale Allocation with Constraints
The neural bandit improves decisions across rounds, but each round
must still coordinate assignments under a common set of business
constraints. Let𝑥𝑢,𝑖,𝑡 indicate whether item𝑖∈I is allocated to
user𝑢∈U at round𝑡= 1,...,𝑇 . Using the sampled incremental
objective ˜𝜏obj 𝑢,𝑖,𝑡 from DragonBandit, the horizon objective is
max
𝑥𝑢,𝑖,𝑡
𝑇∑︁
𝑡=1
∑︁
𝑢,𝑖
˜𝜏obj 𝑢,𝑖,𝑡𝑥𝑢,𝑖,𝑡,(3)
s.t.
∑︁
𝑢,𝑖
𝜏guardrail𝑘 𝑢,𝑖,𝑡 𝑥𝑢,𝑖,𝑡≤𝐶 guardrail𝑘,∀𝑡,𝑘,
∑︁
𝑖
𝑥𝑢,𝑖,𝑡≤𝐶 fcap,∀𝑢,𝑡,
𝑥𝑢,𝑖,𝑡∈{0,1},∀𝑢,𝑖,𝑡.
Here𝜏𝑦 𝑢,𝑖,𝑡 =𝑓 𝑦 𝑡 (𝑢,𝑖, 1)−𝑓 𝑦 𝑡 (𝑢,𝑖, 0) is the round-specific sampled
treatment effect on metric𝑦. We use a sequential policy that solves
one constrained optimization problem per round using the current
posterior sample from DragonBandit. After each round, DragonBan-
dit is updated using the observed feedback before producing the
posterior sample for the next round. In the absence of shared allo-
cation constraints, the resulting policy is equivalent to Thompson
sampling: for each user, it selects the feasible action that maximizes
the sampled incremental reward.
2.3.1 Scalability via Dual Decomposition.At production scale, each
round contains tens of millions of users and hundreds of items, so its
batch has|U|×|I| variables and is intractable for general-purpose
solvers. Suppressing the round index, we relax𝑥𝑢,𝑖,𝑡 to represent an
action probability and solve the resulting large-scale problem using
a smoothed dual-decomposition method [ 2]. The method adds a
small ridge perturbation 𝛾 2∥𝑥∥ 2 to the primal and dualizes the 𝐾
global constraints with multipliers𝜆≥ 0; by Danskin’s theorem,
the resulting dual 𝑔𝛾(𝜆) is differentiable with Lipschitz gradient
∇𝑔𝛾(𝜆)=𝐴𝑥 ∗ 𝛾(𝜆)−𝑏 , where the primal minimizer decomposes per
user:
𝑥∗ 𝛾,𝑢(𝜆)=Π C𝑢
h
− 1 𝛾 𝐴𝑇 𝑢𝜆+𝑐 𝑢 i ,(4)
with ΠC𝑢 an𝑂(|I|log|I|) projection onto the per-user frequency-
cap polytope. The solver then maximizes𝑔𝛾 over the𝐾-dimensional
dual with Nesterov-accelerated ascent, giving per-iteration cost
linear in|U|·|I| versus𝑂((|U||I|) 3.5) for interior-point methods.
The regularization 𝛾 is picked as the largest value satisfying
𝛾 ˆ𝑥𝑇 ˆ𝑥
2|𝑐 𝑇 ˆ𝑥| < 10−3, so the ridge perturbation contributes < 0.1%of the
objective and the perturbed optimum is practically indistinguish-
able from the true LP optimum; when𝐴 is ill-conditioned across
constraint scales, we apply Jacobi row preconditioning. In steady
state, we warm-start the dual from the previous period’s𝜆∗, which
under stable input distributions (KS-tested) achieves over 99% of
the current optimum and also serves as an SLA fallback when the
solver does not converge in time.
3 Incrementality Transformer Architecture
3.1 Temporal Features
We construct a touchpoint sequence𝑆=(𝑠 1,...,𝑠 𝐿) over a look-
back window, where each𝑠𝑖 encodes a (channel, action) interaction
such as (AD, IMPRESSION) or (EMAIL, OPEN); we also inject prior
conversion events into the sequence. Each token is mapped through
a learned embedding matrix𝐸𝑇∈R 𝑉×𝑑 , with𝑉 interaction types
plus a leading [CLS] token (BERT-style [13]) that summarizes the se-
quence even when empty. We use the temporal encoding described
below.
Temporal position.Member interactions occur on irregular sched-
ules, so each token combines its interaction embedding with a day-
since embedding𝐸𝐷𝐴𝑌𝑆 , day-of-week embedding𝐸𝐷𝑂𝑊 , and the
small-embedding-friendly sinusoidal positional encoding 𝑃𝐸𝑖 of
Foumani et al. [16]:
𝐸𝑖 =𝐸𝑇(𝑠𝑖)+𝐸 𝐷𝐴𝑌𝑆(𝑡𝑖)+𝐸 𝐷𝑂𝑊(dow𝑖)+𝑃𝐸 𝑖.(5)
This represents both sequence order and elapsed time without
expanding the interaction vocabulary. Appendix B.2 gives the sinu-
soidal parameterization.
Multi-head attention.We apply standard multi-head self-
attention [41] with𝑄=𝐾=𝑉=(𝐸 1,...,𝐸 𝐿), and pool by taking
only the [CLS] output as the shared representation𝐸𝑆∈R 𝑑, which
is concatenated with member embeddings and dense features before
Φ.
3.2 Multi-Outcome Extension
Marketing campaigns generate multiple outcomes (products) per
member, so we extend the single-outcome DragonNet to a multi-
label setting𝑌𝑘,𝑘∈{ 1,...,𝐾} . Because per-product conversion
rates are highly imbalanced, we use inverse-frequency weights𝑐𝑘
and combine the standard BCE loss (with sigmoid𝜎) into a per-head
outcome loss
L𝑌|𝑇=𝑡 = 1 𝐾
∑︁
𝑘
𝑐𝑘·BCE(𝑦 𝑘, ˆ𝑦𝑘),L 𝑌 =L𝑌|𝑇=1+L𝑌|𝑇=0,(6)
counting each head’s loss only when the corresponding 𝑇
is observed (as in DragonNet/TARNET). Treatment prediction
uses standard BCE on the propensity-head output ˆ𝑒(𝑋) ,L𝑇 =
E[BCE(𝑇, ˆ𝑒(𝑋))].
Following Shi et al. [35], we add targeted regularization based
on the efficient influence function (EIF) for the ATE under uncon-
foundedness [9]:
𝜙EIF = ˆ𝜏(𝑋)+ 𝑇 ˆ𝑒(𝑋)(𝑌− ˆ𝜇1)− 1−𝑇 1− ˆ𝑒(𝑋)(𝑌− ˆ𝜇0)−ATE.(7)
The EIF is Neyman-orthogonal. We use its one-step correction as a
training regularizer, not as a substitute for identification assump-
tions or as a stand-alone guarantee of unbiased CATE estimation:
Ltarreg =E
h𝑌−( ˆ𝑌+𝜖𝜓) 2i ,(8)
with𝜓=𝑇/ ˆ𝑒(𝑋)−( 1−𝑇)/( 1− ˆ𝑒(𝑋)) (the TMLEclever covari-
ate[ 40]), learnable scalar 𝜖, and ˆ𝑌 the prediction from the head
matching observed𝑇.
3.3 Outcome Embeddings
New-product launches create a cold-start problem: marketers want
to promote an offering before the model has seen examples for it.
Our use of “CLIP-inspired” refers narrowly to a normalized shared
embedding space with temperature-scaled similarity; it does not

From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation
use CLIP’s large-scale contrastive pretraining. Instead of align-
ing images and text, we align a member’s outcome state with an
attribute-derived product representation, allowing the same mem-
ber encoder to produce scores for products whose attributes can be
embedded, including products unseen during training.
Concretely, each outcome tower (a two-dense-block MLP with
linear projection) drops the final sigmoid and returns hidden logits
ℎ𝑡(𝑋),ℎ 𝑛𝑡(𝑋) ∈R𝑑𝑜 representing the member’s expected state
under𝑇= 1and 𝑇= 0. A single shared outcome embedding matrix
𝐸𝑂 ∈R 𝐾×𝑑 𝑜 encodes the 𝐾 products and is consumed by both
towers, reflecting the fact that the product’s intrinsic semantics are
invariant to treatment.
3.3.1 Outcome Autoencoder. 𝐸𝑂 is the bottleneck of a lightweight
autoencoder𝐸𝑂 =Encoder(𝐸 input 𝑂 ) over outcome attribute repre-
sentations.𝐸input 𝑂 is constructed by mapping each product attribute
through a learned embedding and concatenating; attributes can be
either structured (one-hot product taxonomy, business-line, format)
or unstructured (LLM-derived embeddings of product descriptions).
The autoencoder is trained jointly with the main task using MSE
reconstruction
Lrecon = 1 𝐾
∑︁
𝑘
𝐸input 𝑂,𝑘 −Decoder(𝐸 𝑂,𝑘) 2.(9)
This serves as semantic regularization: compared with a directly
trained, task-specific𝐸𝑂, the reconstruction objective encourages
𝐸𝑂 to retain the geometry of the input attribute space. The same
setup enables large-scale embedding-space simulation, since pre-
computedℎ𝑡(𝑋) andℎ𝑛𝑡(𝑋) can be paired with arbitrary𝐸𝑂 sam-
ples without re-running the full model.
3.3.2 Outcome Matrix Layer.The final outcome logits are L2-
normalized dot products with learnable log-inverse-temperatures
𝜈𝑡,𝜈𝑛𝑡 (initialized tolog 14.0following CLIP):
ˆ𝑦𝑡 = ℎ𝑡(𝑋) ∥ℎ𝑡(𝑋)∥ · 𝐸𝑇 𝑂 ∥𝐸𝑂∥·exp(𝜈 𝑡), ˆ𝑦𝑛𝑡 = ℎ𝑛𝑡(𝑋) ∥ℎ𝑛𝑡(𝑋)∥ · 𝐸𝑇 𝑂 ∥𝐸𝑂∥·exp(𝜈 𝑛𝑡).
(10)
Each row of𝐸𝑂 is L2-normalized so that similarity depends purely
on the angle between member-state and product representations,
keeping logits on a consistent scale across products and treatment
arms.
3.4 Complete Loss Function
The complete training objective sums the outcome, treatment,
targeted-regularization, and reconstruction losses,
L=L 𝑌|𝑇=1+L𝑌|𝑇=0+L𝑇+L tarreg+𝜆 reconLrecon,(11)
where𝜆recon weights the reconstruction loss;Lrecon is included only
when outcome attribute encodings are provided.
Although the complete research architecture contains several
losses and optional modules, the serving path is modular rather than
a jointly tuned monolith: outcome embeddings are used only for
multi-product scoring, LLA is applied after supervised training to
the last layer, and the LP consumes exported scores independently
of model training. This separation lets each module be disabled or
validated without retraining the rest of the decision pipeline, while
the remaining tuning burden and feature sensitivity are limitations
of the current shared-representation model.
4 Offline Simulations
In order to showcase the strengths of our proposed methodology,
we perform an offline simulation study with a publicly available
dataset. We focus on comparing the following approaches to tar-
geting recommendations.
• Incremental Modeling + Constrained Optimization (ours):
integrates uplift modeling with constrained optimization
for system-level incremental targeting; uses dual decompo-
sition [2] at production scale and OR-Tools for simulation
studies.
• Bandit Incremental Modeling + Constrained Optimization:
extends our method with BNN-based exploration to address
feedback-loop bias [27]; same solver setup as above.
• Propensity Modeling + Constrained Optimization: opti-
mizes predicted scores under constraints [ 1, 23] without
modeling organic outcomes.
• Incremental Modeling + Ranking: ranks by estimated up-
lift [6, 25, 37] but ignores global constraints.
• Propensity Modeling + Ranking: ranks by predicted re-
sponse probability [8, 10, 22, 44].
4.1 Dataset
We use the Open Bandit Dataset (OBD) [32], a real-world logged
bandit dataset. We utilize the random-policy subset, synthetically
mapping the original 34 products that were recommended to >
400K users to 5 distinct actions that are relevant to the production
incrementality use case: recommendation to one of four business
lines or no-recommendation. The no-recommendation action is a
key difference between incremental and non-incremental targeting.
We consider the logged reward within the OBD dataset as indicative
of a conversion event to one of the four business lines. We augment
that reward by coupling it with the average product price of the
four business lines and apply per-business-line LP volume bounds,
as shown in Table 1.
Table 1: Average product price and LP constraint bounds (as
% of audience) for each business line.
Business Line Avg. Price Min. Vol. Max. Vol.
A $5 5% 10%
B $10 5% 30%
C $10 5% 30%
D $200 30% 50%
We also constructed a treatment variable that indicates whether
a member was exposed to a marketing campaign showcasing one
of the four business lines. This setup mirrors the production ecosys-
tem and allows us to demonstrate the importance of incremental
modeling. Finally, we assign a cost of $0.1 to each recommenda-
tion/targeting action to capture operational and bidding costs.
4.2 Setup
We performed an 80/20 split of the full dataset into training and
prediction sets. We trained the predictive models (incremental and
propensity) on the training set, generating incremental/propensity
scores for the prediction set. We applied constrained optimization

Changshuai Wei, John Bencina, Phuc Nguyen, Andre Assuncao Silva T Ribeiro, and Benjamin Zelditch
or ranking to arrive at the final recommendations for the prediction
set (one of the five actions described above), with the objective
function constructed by coupling the incremental/propensity scores
for conversion to each business line with the corresponding average
product price.
We solve the offline simulation LP with Google OR-Tools, which
is tractable at this scale (∼400K members, 5 actions) and conve-
nient for reproduction; at full production scale we use the dual-
decomposition method described in Section 2.3 instead. We apply
the volume bounds from Table 1. The ranking baseline assigns each
member to the action with the highest predictive score, disregarding
global business constraints.
We consider two simulation regimes: asingle-turn(static) eval-
uation and amulti-turn(online) evaluation. For the single-turn
setting, we construct the training log from a random logging policy
in which all actions are approximately equally represented, and we
evaluate each method once on the full prediction set using fixed
model scores. For the multi-turn setting, we intentionally bias the
training log by severely under-sampling a subset of actions, so
that their estimated uplifts become high-variance and can even
exhibit sign errors relative to the OBD ground-truth uplifts. We
then simulate deployment over𝑇= 200rounds using the predic-
tion set as the environment: at each round, each method selects
actions for the current batch, observes the realized rewards from
its own recommendations, updates its training data accordingly,
and incrementally updates the model before the next round.
4.3 Results
4.3.1 Single-turn evaluation.We evaluated the different methods
by calculating the corresponding average rewards with Doubly
Robust Policy Evaluation. As shown in Table 2, incremental scores
lead to higher rewards compared to propensity scores. We also
provide the corresponding send volumes in Table 3, where it can
be seen that incremental targeting leads to a higher percentage
of no-recommendations as the engine is able to identify members
likely to convert organically.
Table 2: Average Rewards, Costs, and Net Returns
ML Model Optim. Avg Reward Avg Cost Avg Net Return
Incremental Constr. Opt.$0.55±0.14 $0.091±0.001 $0.46±0.13
Propensity Constr. Opt.$0.49±0.18 $0.1±0 $0.39±0.18
Incremental Ranking$0.46±0.15 $0.090±0.001 $0.37±0.15
Propensity Ranking$0.41±0.20 $0.1±0 $0.31±0.20
The send volumes also highlight the difference between Con-
strained Optimization and Ranking. As expected, Ranking provides
solutions that deviate significantly from the desired business con-
straints.
We show the average costs in Table 2, where it can be seen that
incremental modeling leads to reduced cost due to the reduced send
volumes described above. The corresponding net returns are shown
in Table 2, where Incremental Modeling coupled with Constrained
Optimization provides the highest overall performance.
Table 3: Send Volumes
Method
Bus.
Line
A
Bus.
Line
B
Bus.
Line
C
Bus.
Line
D
No
Rec.
Incremental +
Constr. Opt. 5% 30% 26% 30% 9%
Propensity +
Constr. Opt. 5% 18% 27% 50% 0%
Incremental +
Ranking 0% 46% 44% 0% 10%
Propensity +
Ranking 0% 0% 0% 100% 0%
4.3.2 Multi-turn evaluation.The previous single-turn evaluation
shows that only approaches with Constrained Optimization can
adequately satisfy the volume constraint bounds induced by busi-
ness constraints, so we restrict attention to these approaches in the
multi-turn evaluation. This multi-turn evaluation demonstrates the
advantage of having an explicit mechanism to balance exploration
and exploitation at the system level. The initial training-data bias
we inject is designed to mirror common challenges in industry ap-
plications, such as cold-start, low representation for certain actions,
and non-stationarity where the true reward function evolves over
time (e.g., an initially low-performing action later becomes high-
performing). Figure 2a shows that the Bandit Incremental Model
is able to overcome this bias and ultimately outperform the other
approaches after learning from the outcomes of its own actions,
even though it may underperform its greedy counterpart in the first
few steps of online learning. This reflects the short-term cost of
exploration in exchange for long-term gains: after roughly 50 model
updates, the Bandit Incremental Model begins to outperform both
greedy variants. Finally, we show that the benefit of exploration is
more pronounced when the initial training-data bias is larger, as
illustrated in Figure 2b.
(a) Small bias setting.
 (b) Large bias setting.
Figure 2: Average cumulative reward and 95% confidence in-
tervals after 200 rounds of feedback. The confidence intervals
are calculated from 30 simulation runs.
4.4 Ablation Study
We tested 8 configurations on a fixed train/validation snapshot,
each repeated 5 times with common hyperparameters. Figure 3a
summarizes outcome, treatment, and uplift performance. Adding
outcome embeddings preserves outcome AUROC and produces

From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation
the highest uplift AUUC point estimate. Removing dense features
reduces outcome AUROC, while its uplift effect depends on the
configuration: AUUC increases for the base model but decreases
slightly when bandit exploration is enabled. This is consistent with
the dense features being prognostic rather than treatment-effect
modifiers. Appendix A provides the full methodology, results, and
outcome-embedding diagnostic.
5 Production Deployment and Experimentation
We now turn from modeling toproduction. Deploying causal target-
ing at scale taught us that a handful of pragmatic enhancements be-
yond the core model and optimizer are what make the system work
in practice. The most important are the construction of training
data and the control of spend and delivery. These enhancements are
largely invisible to offline simulations and ablation studies, which
hold the data-generating process and delivery pipeline fixed, yet
in our experience they are important for real-world success. We
describe these enhancements first, followed by the serving archi-
tecture, agentic experimentation setup, and online results.
5.1 Training-Data Construction for Causal
Estimation
Production logs allow us to build sequences of marketing touches
and conversions, but causal estimation requires careful construc-
tion of the context sequence𝑋 , treatment action𝑇 , and conversion
label𝑌 . The context must contain only information available be-
fore treatment, while treatment and outcome are assigned from
subsequent non-overlapping windows.
Let 𝑅 denote the snapshot run date. For each member, pro-
duction samples 𝐷=𝑅−(𝑊 𝐶+𝑊𝑇 +𝑊𝐷)+𝑈 , where 𝑈∼
Uniform{0,...,𝑊 𝐷− 1},𝑊𝐷 = 90days, 𝑊𝑇 = 7days, and 𝑊𝐶 = 30
days. Thus𝐷∈[𝑅− 127,𝑅− 38]. The model input contains market-
ing interactions and prior conversions in[𝐷− 60,𝐷) ; post-𝐷 events
are excluded. We set𝑇= 1when at least one qualifying email send,
on-platform impression, or video view occurs in [𝐷,𝐷+ 7). We
set𝑌= 1when the corresponding business-line or product-family
conversion occurs in[𝐷+ 7,𝑅] , and𝑌= 0otherwise. This reserves
at least 30 days of follow-up while earlier dates have longer out-
come windows. Randomizing𝐷 avoids a last-touch label, captures
long-term action effects, and preserves variable-length histories.
5.2 Cost and Delivery Control
Controlling how much the causal policy spends and delivers matters
for two reasons: a standingbusinessrequirement to pace committed
budgets over the fiscal quarter, and anexperimentationrequirement
to compare arms at matched delivery. Both stem from the same
underlying gap between an assignment and its realized delivery.
At a given round, with 𝑡 suppressed, the LP in (3) chooses as-
signments𝑥𝑢,𝑖, but an assignment is not a guaranteed delivery in
an auction-mediated, activity-gated channel. A member may not
return during the campaign window, or the send may lose the down-
stream auction. We therefore estimate the probability of delivery,
𝑝𝑢,𝑖 =𝑃(delivered within window|𝑢,𝑖),(12)
using a classifier with isotonic calibration per member-lifecycle seg-
ment. The estimate enters the LP through the expected-impression
constraint ˝ 𝑢,𝑖𝑝𝑢,𝑖𝑥𝑢,𝑖 ∈[𝐶 𝑙 imp,𝐶𝑢 imp] and the expected-cost con-
straint ˝ 𝑢,𝑖 ˆ𝑐𝑢,𝑖𝑥𝑢,𝑖∈[𝐶 𝑙 cost,𝐶𝑢 cost]. Their bounds are calibrated to
the observed BAU delivery envelope. This prevents the optimizer
from concentrating assignments on members who appear incre-
mental but are difficult or expensive to reach.
Across multiple rounds, such as in quarterly budget pacing or
cumulative spend matching in an experiment, realized delivery and
cost may differ from their LP predictions. We therefore introduce
a feedback controller that adjusts the round-level cost target. Let
𝐵 be the committed budget,𝑆𝑡 the cumulative realized spend, and
𝑞(𝑡/𝐻) the desired cumulative pacing curve over a horizon𝐻, with
𝑞(0)=0and𝑞(1)=1. The outer loop computes
𝑆★ 𝑡 =𝐵𝑞(𝑡/𝐻), 𝑒 𝑡 =𝑆 ★ 𝑡 −𝑆𝑡.(13)
Let𝐷𝑡 denote the realized spend during interval 𝑡, and let 𝐴𝑡 =˝
𝑢,𝑖 ˆ𝑐𝑢,𝑖,𝑡𝑥𝑢,𝑖,𝑡 denote the LP-predicted spend of the selected as-
signments. The inner loop estimates the spend-realization ratio
as𝑟𝑡 =𝐷 𝑡/𝐴𝑡 and smooths it using ˆ𝑟𝑡 =𝛼𝑟 𝑡+( 1−𝛼) ˆ𝑟𝑡−1 , where
𝛼∈( 0, 1] weights the newest observation. It then updates the LP
cost target:
𝐶cost,𝑡+1 =Π[𝐶min,𝐶max]

𝐶cost,𝑡+𝜅 𝑒𝑡 max( ˆ𝑟𝑡,𝜖)  ,(14)
where𝜅> 0is the controller gain. The target 𝐶cost,𝑡 can be con-
verted into a two-sided LP constraint using a predefined tolerance
around the target.
When realized spend falls behind the pacing curve, the controller
raises the assignment cap in proportion to the gap and estimated
deliverability; when spend runs ahead, it lowers the cap. The pro-
jection preserves operational bounds.
An early A/B test runwithoutthe above controls showed the
treatment arm under-delivering: the causal policy withholds and re-
allocates sends, lowering treatment impressions relative to control.
A raw total-bookings comparison then penalizes the treatment for
deliveringlessrather than for choosing worse, confounding policy
quality with delivery volume. Constraining treatment to the BAU
impression and cost envelope equalizes delivery across arms and
restores a clean, like-for-like read.
5.3 Serving Architecture
The system is served as a batch pipeline. DragonBandit scores
𝜇1,𝜇0, and𝑒 for the eligible population and samples incremental
objectives via last-layer linearized Laplace Thompson sampling
(Section 2.2); a dual-decomposition solver [ 2] computes the con-
strained allocation (3) under global guardrails, warm-started from
the previous period’s dual 𝜆★; and the feedback controller (Sec-
tion 5.2) adjusts budget caps from realized deliverability before
assignments are materialized to the campaign-management system.
Because scoring and allocation are decoupled from serving, the
same supervised checkpoint is deployed with or without explo-
ration, and non-convergence solver falls back to the warm-started
dual, which recovers over 99% of the current optimum under stable
input distributions within the SLA.

Changshuai Wei, John Bencina, Phuc Nguyen, Andre Assuncao Silva T Ribeiro, and Benjamin Zelditch
(a) Outcome prediction AUROC.
 (b) Treatment prediction AUROC.
 (c) Uplift AUUC.
Figure 3: Ablation results. Error bars denote 95% confidence intervals from 5 training runs.
5.4 Agentic Experimentation
We evaluated the end-to-end framework with an eight-week on-
line A/B test on LinkedIn Feed marketing traffic, against the de-
ployed business-as-usual (BAU) targeting stack. BAU is a stan-
dard two-tier recommender: the retrieval tier pre-selects each cam-
paign’s audience using a propensity-based scoring model together
with marketer-defined criteria, and the ranking tier is a second
propensity-based model that estimates engagement probability
and is followed by ranking heuristics for final assignment. The
treatment arm keeps the marketer-defined criteria in retrieval and
replaces both propensity layers with a single decision layer that
scores members by predicted causal uplift across all campaigns and
assigns them via the LP under global constraints. A meaningful
policy difference is that the treatment arm canwithholda send
whenever the predicted incremental value is negative or no feasi-
ble positive-incremental option exists. Members were randomly
assigned 50/50 to the two experiment arms.
Standing up arepresentativeBAU control and a matched treat-
ment arm at scale requires configuring hundreds of live campaigns
across products, segments, and budgets. Manual configuration is
infeasible and, we found, subject to two subtle failure modes that
bias measurement yet are invisible offline. First, when out-of-scope
campaigns are suppressed via an exclusion segment defined by
dynamiccriteria (company, locale, activity), members drift across
arms in a way correlated with platform activity, contaminating the
intent-to-treat contrast. Second, when arms are assembled from
shared segment definitions, a control audience can silently inherit
atreatmentsend decision through a reused sub-segment. We there-
fore built an agentic campaign-setup tool that duplicates campaigns
into hundreds of budget-split variants,freezeseach audience to a
static snapshot for the experiment’s duration, audits segment lin-
eage so that no control segment depends on a treatment-derived
decision, and materializes campaigns as drafts promoted by a single
activation toggle with symmetric rollback. This provides identi-
cal scaffolding across arms, so the only systematic difference is
the decision layer. It also improves operational safety. Budget par-
ity is enforced by setting caps proportional to audience sizes and
recalibrating as arm sizes drift.
5.5 Results
Measured against long-term-value metrics over an eight-week pe-
riod, the treatment arm achieved a statistically significant+7.20%
lift (𝑝= 0.041, 95% CI:[0.31%, 14.09%]). The experiment evaluates
the end-to-end policy as deployed. Its components satisfy coupled
system requirements rather than representing independent product
features: causal scoring defines the incremental objective, the explo-
ration policy provides stochastic treatment variation that improves
positivity (overlap), the LP enforces global business constraints, and
the withhold rule prevents assignments with negative incremental
value. Removing any of these components changes the operating
requirements or the data-generating policy. The online result there-
fore measures the system-level impact of the complete production
policy, while the offline studies examine individual mechanisms
under controlled settings.
A Detailed Ablation Study
A.1 Protocol
We ran targeted ablation simulations on a static train/validation
snapshot, holding hyperparameters (learning rate, epochs, batch
size, hidden sizes) constant across configurations and varying only
the indicated change. We tested 8 configurations, each repeated 5
times. The base model is the architecture from Section 3 on top
of the DragonNet causal head, without bandit sampling or out-
come embeddings (OE); we then added bandit and OE separately,
and additionally removed three input categories: dense features,
entity embeddings, and sequential interactions. These are not ex-
haustive component ablations: in particular, they do not separately
isolate the Transformer operator from its sequence input, targeted
regularization, or every interaction among loss terms.
A.2 Outcome and Treatment Metrics
Outcome ROC-AUC is computed against the common validation
dataset using the observed treatment for masking, ˆ𝑦=𝑇 ˆ𝑦𝑡+( 1−
𝑇) ˆ𝑦𝑛𝑡 , and macro-averaged across labels. Treatment AUROC eval-
uates the propensity head against the observed treatment assign-
ment.
A.3 Uplift Results
Following CausalML [6], we rank observations by predicted uplift
and compute
CumLift(𝑘)=
˝𝑘
𝑖=1𝑌𝑖𝑇𝑖 ˝𝑘
𝑖=1𝑇𝑖+𝜖−
˝𝑘
𝑖=1𝑌𝑖(1−𝑇𝑖) ˝𝑘
𝑖=1(1−𝑇𝑖)+𝜖,(15)

From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation
with CumGain(𝑘)=𝑘CumLift(𝑘) and normalized area under the
gain curve as AUUC. Implementations of AUUC and Qini differ [14,
18, 29]; we use the CausalML implementation.
Removing dense features is neutral or beneficial for uplift AUUC
despite reducing outcome AUROC from 0.857 to 0.826 and mini-
mally affecting treatment AUROC. A plausible explanation is that
these features are prognostic and predict outcomes regardless of
treatment, rather than serving as treatment-effect modifiers. They
may therefore add variance when the shared DragonNet representa-
tion must serve both propensity and outcome losses. This remains a
hypothesis rather than an automated feature-selection mechanism;
architectures such as FlexTENet [11] could explicitly separate the
two subspaces.
A.4 Outcome-Embedding Diagnostic
We train on 9 of 10 outcomes, draw 5,000 hypothetical products
from the learned embedding space, and score each against the held-
out 10th product across the validation members. Figure 4 shows
that samples near semantically similar trained products have higher
AUROC against the held-out target, indicating that the geometry re-
tains outcome-relevant structure. Because this diagnostic uses one
held-out product and sampled embeddings rather than prospective
real launches, it does not establish zero-shot production effective-
ness.
Figure 4: Outcome-embedding PCA. Each sampled hypotheti-
cal product is colored by AUROC z-score against the held-out
product.
B Additional Architectural Details
B.1 Bayes by Backprop
Bayes by Backprop [4, 20] learns a Gaussian variational posterior
𝑞𝜙(𝜃) by maximizing the evidence lower bound. Predictive proba-
bilities are approximated by Monte Carlo sampling,
𝑃(𝑦∗ =1|𝑥 ∗)≈ 1 𝑀 𝑀∑︁ 𝑚=1 𝜎(𝑓𝜃(𝑚)(𝑥∗)), 𝜃 (𝑚)∼𝑞𝜙.(16)
Compared with LLA, it captures non-local posterior uncertainty
but adds stochastic training and repeated inference-time sampling.
For a minibatch variant, an additional𝛽L𝐾𝐿 term regularizes the
posterior toward the prior;𝛽= 1gives the standard ELBO objective.
We did not explore alternative KL-weight schedules in the reported
experiments.
B.2 Temporal Position Encoding
For sequence position𝑝𝑜𝑠 and embedding coordinate𝑖, we use the
small-embedding-friendly sinusoidal variant
𝑃𝐸(𝑝𝑜𝑠,2𝑖) =sin(𝑝𝑜𝑠𝜔 new 𝑖 ), 𝑃𝐸 (𝑝𝑜𝑠,2𝑖+1) =cos(𝑝𝑜𝑠𝜔 new 𝑖 ),
(17)
where𝜔 new 𝑖 =𝜔𝑖𝑑/𝐿 and𝜔𝑖 = 10000−2𝑖/𝑑 . The scaling adapts the
standard sinusoid to the short interaction vocabulary and sequence
length used in our setting.
Ethical Considerations
We identify no ethical implications specific to the proposed opti-
mization method beyond the standard privacy, fairness, and experi-
mentation considerations of large-scale recommendation systems;
deployments should follow applicable data-governance and review
processes.
References
[1] Deepak Agarwal, Shaunak Chatterjee, Yang Yang, and Liang Zhang. 2015. Con-
strained optimization for homepage relevance. InProceedings of the 24th Interna-
tional Conference on World Wide Web. 375–384.
[2] Kinjal Basu, Amol Ghoting, Rahul Mazumder, and Yao Pan. 2020.
ECLIPSE: An Extreme-Scale Linear Program Solver for Web-Applications.
arXiv:2007.15936 [math.OC] https://arxiv.org/abs/2007.15936
[3] Dimitris Bertsimas, David B. Brown, and Constantine Caramanis. 2011. The
Theory of Robust Optimization.SIAM Rev.(2011).
[4] Charles Blundell, Julien Cornebise, Koray Kavukcuoglu, and Daan Wierstra.
2015. Weight Uncertainty in Neural Networks. arXiv:1505.05424 [stat.ML]
https://arxiv.org/abs/1505.05424
[5] Stephen Bonner and Flavian Vasile. 2018. Causal Embeddings for Recommenda-
tion. InProceedings of the 12th ACM Conference on Recommender Systems.
[6] Huigang Chen, Totte Harinen, Jeong-Yoon Lee, Mike Yung, and Zhenyu
Zhao. 2020. CausalML: Python Package for Causal Machine Learning.
arXiv:2002.11631 [cs.CY]
[7] Jiaju Chen, Wang Wenjie, Chongming Gao, Peng Wu, Jianxiong Wei, and Qing-
song Hua. 2024. Treatment Effect Estimation for User Interest Exploration
on Recommender Systems. InProceedings of the 47th International ACM SIGIR
Conference on Research and Development in Information Retrieval. 1861–1871.
[8] Heng-Tze Cheng, Levent Koc, Jeremiah Harmsen, Tal Shaked, Tushar Chandra,
Hrishi Aradhye, Glen Anderson, Greg Corrado, Wei Chai, Mustafa Ispir, Rohan
Anil, Zakaria Haque, Lichan Hong, Vihan Jain, Xiaobing Liu, and Hemal Shah.
2016. Wide & Deep Learning for Recommender Systems. InProceedings of the
1st Workshop on Deep Learning for Recommender Systems (DLRS 2016). 7–10.
[9] Victor Chernozhukov, Denis Chetverikov, Mert Demirer, Esther Duflo, Christian
Hansen, Whitney Newey, and James Robins. 2018. Double/debiased machine
learning for treatment and structural parameters.The Econometrics Journal21, 1
(01 2018), C1–C68. doi:10.1111/ectj.12097
[10] Paul Covington, Jay Adams, and Emre Sargin. 2016. Deep Neural Networks
for YouTube Recommendations. InProceedings of the 10th ACM Conference on
Recommender Systems (RecSys ’16). 191–198.
[11] Alicia Curth and Mihaela van der Schaar. 2021. On Inductive Biases for Het-
erogeneous Treatment Effect Estimation. arXiv:2106.03765 [stat.ML] https:
//arxiv.org/abs/2106.03765
[12] Erik Daxberger, Agustinus Kristiadi, Alexander Immer, Runa Eschenhagen,
Matthias Bauer, and Philipp Hennig. 2021. Laplace redux-effortless bayesian
deep learning.Advances in neural information processing systems34 (2021),
20089–20103.
[13] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT:
Pre-training of Deep Bidirectional Transformers for Language Understanding.
arXiv:1810.04805 [cs.CL] https://arxiv.org/abs/1810.04805
[14] Floris Devriendt, Tias Guns, and Wouter Verbeke. 2020. Learning to rank for
uplift modeling.CoRRabs/2002.05897 (2020). arXiv:2002.05897 https://arxiv.
org/abs/2002.05897

Changshuai Wei, John Bencina, Phuc Nguyen, Andre Assuncao Silva T Ribeiro, and Benjamin Zelditch
[15] Andrew YK Foong, Yingzhen Li, José Miguel Hernández-Lobato, and Richard E
Turner. 2019. ’In-Between’Uncertainty in Bayesian Neural Networks.arXiv
preprint arXiv:1906.11537(2019).
[16] Navid Mohammadi Foumani, Chang Wei Tan, Geoffrey I. Webb, and Mahsa
Salehi. 2023. Improving position encoding of transformers for multivariate time
series classification.Data Mining and Knowledge Discovery38, 1 (Sept. 2023),
22–48. doi:10.1007/s10618-023-00948-2
[17] Chen Gao, Yu Zheng, Wenjie Wang, Fuli Feng, Xiangnan He, and Yong Li. 2024.
Causal inference in recommender systems: A survey and future directions.ACM
Transactions on Information Systems42, 4 (2024), 1–32.
[18] Pierre Gutierrez and Jean-Yves Gérardy. 2017. Causal Inference and Uplift
Modelling: A Review of the Literature. InProceedings of The 3rd International
Conference on Predictive Applications and APIs (Proceedings of Machine Learning
Research, Vol. 67), Claire Hardgrove, Louis Dorard, Keiran Thompson, and Florian
Douetteau (Eds.). PMLR, 1–13. https://proceedings.mlr.press/v67/gutierrez17a.
html
[19] Maximilian Kasy and Anja Sautmann. 2021. Adaptive treatment assignment in
experiments for policy choice.Econometrica89, 1 (2021), 113–132.
[20] Durk P Kingma, Tim Salimans, and Max Welling. 2015. Variational dropout and
the local reparameterization trick.Advances in neural information processing
systems28 (2015).
[21] Sören R. Künzel, Jasjeet S. Sekhon, Peter J. Bickel, and Bin Yu. 2019. Metalearners
for estimating heterogeneous treatment effects using machine learning.Pro-
ceedings of the National Academy of Sciences116, 10 (Feb. 2019), 4156–4165.
doi:10.1073/pnas.1804597116
[22] Lihong Li, Wei Chu, John Langford, and Robert E Schapire. 2010. A contextual-
bandit approach to personalized news article recommendation. InProceedings of
the 19th international conference on World wide web. 661–670.
[23] Rahul Makhijani, Shreya Chakrabarti, Dale Struble, and Yi Liu. 2019. LORE: a
large-scale offer recommendation engine with eligibility and capacity constraints.
InProceedings of the 13th ACM Conference on Recommender Systems. 160–168.
[24] James McInerney, Brian Brost, Praveen Chandar, Rishabh Mehrotra, and Ben-
jamin Carterette. 2020. Counterfactual evaluation of slate recommendations
with sequential reward interactions. InProceedings of the 26th ACM SIGKDD
International Conference on Knowledge Discovery & Data Mining. 1779–1788.
[25] Chang Meng, Chenhao Zhai, Xueliang Wang, Shuchang Liu, Xiaoqiang Feng,
Lantao Hu, Xiu Li, Han Li, and Kun Gai. 2025. Enhancing Online Video Rec-
ommendation via a Coarse-to-fine Dynamic Uplift Modeling Framework. In
Proceedings of the 19th ACM Conference on Recommender Systems. 82–92.
[26] Brady Neal. 2020. Introduction to causal inference.Course lecture notes (draft)
132 (2020).
[27] Phuc Nguyen, Benjamin Zelditch, Joyce Chen, Rohit Patra, and Changshuai Wei.
2026. BanditLP: Large-Scale Stochastic Optimization for Personalized Recom-
mendations.arXiv preprint arXiv:2601.15552(2026).
[28] Geir K Nilsen, Antonella Z Munthe-Kaas, Hans J Skaug, and Morten Brun. 2022.
Epistemic uncertainty quantification in deep learning classification by the Delta
method.Neural networks145 (2022), 164–176.
[29] Nicholas Radcliffe. 2007. Using control groups to target on predicted lift: Building
and assessing uplift model.Direct Marketing Analytics Journal(2007), 14–21.
[30] Swarnali Raha, Kshitij Khare, and Rohit K Patra. [n. d.]. Computationally Efficient
Laplace Approximations for Neural Networks. InNeurIPS 2024 Workshop on
Bayesian Decision-making and Uncertainty.
[31] Carlos Riquelme, George Tucker, and Jasper Snoek. 2018. Deep bayesian bandits
showdown. InInternational conference on learning representations, Vol. 9.
[32] Yuta Saito, Shunsuke Aihara, Megumi Matsutani, and Yusuke Narita. 2020. Open
bandit dataset and pipeline: Towards realistic and reproducible off-policy evalu-
ation.arXiv preprint arXiv:2008.07146(2020).
[33] Tobias Schnabel, Adith Swaminathan, Ashudeep Singh, Navin Chandak, and
Thorsten Joachims. 2016. Recommendations as Treatments: Debiasing Learning
and Evaluation. InProceedings of the 33rd International Conference on Machine
Learning.
[34] Uri Shalit, Fredrik D. Johansson, and David Sontag. 2017. Estimating Individual
Treatment Effect: Generalization Bounds and Algorithms. InProceedings of the
34th International Conference on Machine Learning.
[35] Claudia Shi, David Blei, and Victor Veitch. 2019. Adapting Neural Networks for
the Estimation of Treatment Effects. InAdvances in Neural Information Processing
Systems.
[36] Yi Su, Xiangyu Wang, Elaine Ya Le, Liang Liu, Yuening Li, Haokai Lu, Benjamin
Lipshitz, Sriraj Badam, Lukasz Heldt, Shuchao Bi, et al. 2024. Long-term value of
exploration: measurements, findings and algorithms. InProceedings of the 17th
ACM International Conference on Web Search and Data Mining. 636–644.
[37] Zexu Sun, Hao Yang, Dugang Liu, Yunpeng Weng, Xing Tang, and Xiuqiang
He. 2024. End-to-end cost-effective incentive recommendation under budget
constraint with uplift modeling. InProceedings of the 18th ACM Conference on
Recommender Systems. 560–569.
[38] Adith Swaminathan and Thorsten Joachims. 2015. Batch learning from logged
bandit feedback through counterfactual risk minimization.The Journal of Ma-
chine Learning Research16, 1 (2015), 1731–1755.
[39] Adith Swaminathan and Thorsten Joachims. 2017. Off-Policy Evaluation for
Slate Recommendation. InAdvances in Neural Information Processing Systems.
[40] Mark J. van der Laan and Daniel Rubin. 2006. Targeted Maximum Likelihood
Learning.The International Journal of Biostatistics2, 1 (2006). doi:10.2202/1557-
4679.1043
[41] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all
you need.Advances in Neural Information Processing Systems(2017).
[42] Yixin Wang, Dawen Liang, Laurent Charlin, and David M Blei. 2018. The decon-
founded recommender: A causal inference approach to recommendation.arXiv
preprint arXiv:1808.06581.
[43] Changshuai Wei, Benjamin Zelditch, Joyce Chen, Andre Assuncao Silva T Ribeiro,
Jingyi Kenneth Tay, Borja Ocejo Elizondo, Sathiya Keerthi Selvaraj, Aman Gupta,
and Licurgo Benemann De Almeida. 2024. Neural optimization with adaptive
heuristics for intelligent marketing system. InProceedings of the 30th ACM
SIGKDD Conference on Knowledge Discovery and Data Mining. 5938–5949.
[44] Rex Ying, Ruining He, Kaifeng Chen, Pong Eksombatchai, William L. Hamilton,
and Jure Leskovec. 2018. Graph Convolutional Neural Networks for Web-Scale
Recommender Systems. InProceedings of the 24th ACM SIGKDD International
Conference on Knowledge Discovery & Data Mining (KDD ’18). 974–983.
[45] Weitong Zhang, Dongruo Zhou, Lihong Li, and Quanquan Gu. 2020. Neural
thompson sampling.arXiv preprint arXiv:2010.00827(2020).
