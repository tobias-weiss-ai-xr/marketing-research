---
title: Multitask Reinforcement Learning for Assisting Choice Model Specification
url: https://arxiv.org/abs/2609.18441
category: consumer-behavior
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Gabriel Nova
- Stephane Hess
- Sander Van Cranenburgh
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.18441
pages: 20
chars: 53947
fetched_at: '2026-11-08T13:16:39+00:00'
kb_version: 1
---

# Multitask Reinforcement Learning for Assisting Choice Model Specification

Multitask Reinforcement Learning for Assisting Choice Model Specification
Gabriel Nova*1, Stephane Hess 1,2, and Sander van Cranenburgh 1
1CityAI Lab, Transport and Logistics Group, Delft University of Technology, The Netherlands
2Institute for Transport Studies and Choice Modelling Centre, University of Leeds, UK
Discrete choice model specification is a time-consuming task in which modellers often
specify and estimate multiple models while balancing goodness-of-fit, parsimony, and be-
havioural plausibility. We present Delphos, a multitask reinforcement learning framework
that learns transferable specification strategies across transport choice datasets. Delphos
frames model specification as a sequential decision-making problem in which it applies
a sequence of modelling actions and receives feedback from an estimation environment
based on model performance and convergence. To transfer modelling decisions across
datasets with different sets of variables, Delphos represents utility specifications as sets
of modelling terms using a DeepSet-Q architecture, allowing a shared specification pol-
icy to learn across multiple datasets. Trained on nine transport choice datasets, Delphos
consistently outperforms independently trained single-task agents, indicating that sharing
modelling experience improves learning efficiency and helps identify promising sequences
of modelling decisions with fewer unsuccessful estimation attempts. When applied without
further training to the unseen Swissmetro and Decisions datasets, the same agent identifies
competitive specifications in less than 20 minutes on a standard CPU. It achieves a higher
log-likelihood per observation than the VNS metaheuristic on Swissmetro and performance
comparable to a published MNL specification developed by expert modellers on Decisions.
These findings show that accumulating and reusing modelling experience enables Delphos
to function as an intelligent assistant for discrete choice model specification. It reduces
manual trial-and-error while allowing modellers to retain control over model diagnosis, re-
finement, and final selection.
Keywords: Assisted choice model specification; Deep reinforcement learning; Artificial
intelligence
1
arXiv:2609.18441v1  [econ.GN]  16 Sep 2026

1 Introduction
Discrete choice models (DCMs) are econometric frameworks widely used to understand and
analyse individual choice behaviour, forecast demand, and evaluate policies across a wide
range of application domains Buckell et al. (2019); Mariel et al. (2021); Hess & Daly (2024);
de Vries et al. (2025). By representing the decision-making process underlying observed
choices, DCMs provide insights into individuals’ preferences and the trade-offs they make
between alternatives. These models can then be used to derive behavioural measures such
as marginal utilities, elasticities, willingness-to-pay, and values of travel time. To obtain
such behavioural insights, modellers typically specify competing choice models by making
various modelling decisions, such as selecting explanatory variables, defining functional
forms, and representing preference heterogeneity that reflect different behavioural assump-
tions (Van Cranenburgh et al., 2022). In practice, they estimate and evaluate specifications
by balancing goodness-of-fit, parsimony, and behavioural plausibility, and then refine them
through successive iterations (Nova et al., 2025). Consequently, specifying discrete choice
models remains an iterative, cognitively demanding, and time-consuming process.
This trial-and-error workflow has motivated the development of assisted specification meth-
ods, which seek to support, speed up, or partially automate the specification process.
Two broad classes of approaches can be distinguished. The first comprises metaheuristic
methods that formulate model specification as a combinatorial search problem and use
optimisation techniques to explore the space of possible models (Páez & Boisjoly, 2022;
Rodrigues et al., 2020; Ortelli et al., 2021). These approaches iteratively construct can-
didate specifications from previously explored models and evaluate them using objective
functions based on model fit and parsimony. Promising specifications are retained and
modified through predefined search operators to generate new candidates. More recent
approaches have incorporated behavioural constraints and grammar-based representations
to improve the behavioural plausibility of the resulting specifications (Beeramoole et al.,
2023; Haj-Yahia et al., n.d.; Ghorbani et al., 2025). Although these methods can efficiently
explore model spaces, they rely on predefined search operators and do not explicitly accu-
mulate knowledge about modelling decisions across specification problems.
The second class comprises machine-learning-based approaches that generate model spec-
ifications by learning from previous modelling exercises. Instead of relying on predefined
search operators, these methods learn patterns from previously estimated specifications
and use them to propose candidates that are likely to satisfy behavioural expectations and
provide a good fit. For instance, Sfeir et al. (2025) explore the use of pre-trained large
language models to generate utility specifications by drawing on knowledge and reason-
ing capabilities acquired from large text corpora. Similarly, Nova et al. (2025) formu-
late model specification as a sequential decision-making problem in which a reinforcement
learning agent learns specification strategies through repeated interaction with an esti-
mation environment. These approaches shift the focus from predefined search operators
to learning-based systems that can use accumulated knowledge to assist the specification
process.
However, existing assisted model specification methods struggle to reuse modelling expe-
rience across datasets. Human modellers, by contrast, rarely approach each specification
problem independently. They draw on experience from previous modelling exercises and
adapt it to new contexts. This is possible because many modelling decisions are informed
by behavioural principles that generalise across datasets and application domains. For
example, travel cost is expected to have a negative marginal utility, income interactions
are commonly used to capture heterogeneity in cost sensitivity, and total, in-vehicle, and
out-of-vehicle travel time can be treated as alternative representations of the same be-
havioural construct. Despite the transferability of this knowledge, metaheuristic methods
2

typically discard information about previously explored specifications once the search ter-
minates, offering little scope for cumulative learning. Machine-learning-based approaches
retain knowledge from previous modelling tasks, but usually encode it in dataset-specific
representations. Consequently, the specification process must effectively be repeated for
each new dataset, even when relevant modelling knowledge could be transferred from re-
lated contexts.
To leverage modelling experience across datasets, we propose a multitask reinforcement
learning framework for assisting choice model specification. By extending Delphos (Nova
et al. (2025)) to a multitask setting, we enable a single agent to learn a transferable spec-
ification policy from multiple choice datasets. To support transfer across datasets with
different attributes and socio-demographic variables, Delphos represents modelling deci-
sions independently of the dataset-specific variables and contexts in which they are applied.
Specifically, we extend Delphos with a DeepSet-Q network (Hügle et al., 2020) that encodes
utility specifications as sets of modelling terms and learns a shared latent representation.
Conditioned on the current modelling context, this representation enables the agent to
select decisions that generalise across related datasets. Through training across datasets,
the agent learns which modelling decisions tend to produce high-performing specifications
in similar contexts and reuses this knowledge when specifying models for new datasets.
The main aim of the framework is to support modellers by using experience acquired
across datasets to provide automated, data-driven suggestions for utility specifications.
By directing the search towards high-performing and behaviourally plausible candidates,
Delphos can reduce the cognitive and computational burden of manual trial-and-error
and reduce the risk of misspecification. In practice, the modeller defines a catalogue of
attributes, socio-demographic characteristics, non-linear transformations, and taste struc-
tures. Delphos then proposes and estimates candidate specifications and presents the
successfully estimated models on the Pareto front. The modeller can compare, refine, and
validate these candidates while retaining control over their behavioural interpretation and
final selection. Overall, Delphos functions as an intelligent assistant that automates part
of the specification workflow. It supports the development of utility functions from which
willingness-to-pay measures, such as values of travel time savings used in cost–benefit anal-
ysis, can be derived.
The remainder of the paper is organised as follows. Section 2 introduces the reinforcement
learning concepts used in the paper. Section 3 presents our framework for assisted choice
model specification across multiple datasets. Section 3.1 formulates the specification task
as a Markov decision process, Section 3.2 describes the multitask extension for sharing
modelling decisions across datasets, and Section 3.3 presents the training and evaluation
protocol. Section 4 describes the experimental design and evaluation studies. Finally,
Section 5 presents the main results, and Section 6 concludes the paper.
2 Background
2.1 Markov decision process
A Markov decision process (MDP) represents a sequential decision-making problem in
which an agent interacts with an environment over time. The agent repeatedly observes
the current state, selects an action, receives feedback from the environment, and transitions
toanewstate. Formally, anMDPisdefinedasthetuple(S,A,P,R, γ), whereSrepresents
the possible states of the environment andArepresents the actions available to the agent.
The transition functionP(s ′ |s, a)defines the probability of moving from statesto
a subsequent states ′ after taking actiona. The reward functionR(s, a)evaluates the
3

outcome of taking actionain states. Finally, the discount factorγdetermines the relative
importance of future and immediate rewards.
Vπ(s) =Eπ
" ∞X
t=0
γtrt+1

 s0 =s # (1)
The agent aims to maximise the cumulative reward obtained through its interactions with
the environment. It follows a policyπ(a|s;θ)that defines the probability of selecting action
awhen the environment is in states. The state-value function represents the expected
cumulative reward obtained when starting from statesand following policyπ, as shown
in Eq. (1). The optimal value function, denoted byV∗(s), represents the maximum return
achievable from states.
2.2 Reinforcement learning
While an MDP formulates a sequential decision-making problem, reinforcement learning
(RL) addresses that problem by learning a policy that maximises expected long-term re-
wards (Sutton & Barto, 2018). Through repeated interaction with the environment, the
agent balances exploration and exploitation. Exploration provides additional knowledge
about the environment, whereas exploitation uses that knowledge to select actions with
high expected returns. At each decision step, the agent stores a transition containing the
current state, selected action, received reward, and next state. These transitions are then
used to refine the policy towards actions that are expected to yield higher returns.
Q-learning is commonly used to learn such a policy (Watkins & Dayan, 1992). The agent
estimates an action-value function,Q(s, a), which represents the expected cumulative re-
ward after taking actionain states, as shown in Eq. (2). These action values define
a policy that selects the feasible action with the highest expected return in each state.
Formally, the optimal policy maximises the action-value function over the set of feasible
actionsA(s), as shown in Eq. (3).
Q(s, a) =E

r+γmax
a′
Q(s′, a′)|s, a

(2)
π∗(s) = arg max
a∈A(s)
Q∗(s, a)(3)
In practice, the action-value function cannot be represented explicitly when the state space
is large. Deep Q-networks (DQNs; Mnih et al., 2015) address this limitation by approxi-
matingQ(s, a;θ)with a neural network parameterised byθ. Rather than storing a value for
every state–action pair, the network predicts action values directly from the state represen-
tation. To improve training stability, a DQN also maintains a target networkQ(s, a;θ−),
whose parameters are periodically updated from the policy network and used to compute
stable learning targets. This approach enables RL agents to operate in complex decision
spaces where traditional tabular methods are infeasible (Plaat, 2022).
3 Methodological framework
This section introduces the proposed multitask reinforcement learning framework for as-
sisting the choice model specification process across multiple datasets. We first formulate
the specification process as a Markov decision process. We then extend the formulation
to multiple datasets through a shared representation of utility specifications that enables
transferable modelling decisions. Finally, we present the training and evaluation protocol
used to assess learning and transferability.
4

3.1 Problem formulation
We formulate discrete choice model specification as a Markov decision process in which
an agent learns to build utility specifications through interaction with an estimation en-
vironment (Figure 1). Delphos is the reinforcement learning agent that learns a policy
for specifying high-performing choice models (Nova et al. (2025)). At the start of each
episode, Delphos uses a linear additive specification in which the available attributes enter
linearly with generic coefficients and no covariate interactions. It then applies a sequence
of modelling actions to modify these terms and propose a final candidate. The episode
ends when the agent selects theterminateaction. The environment then estimates the
candidate and returns modelling outcomes used to compute a reward based on goodness-
of-fit, convergence, and behavioural expectations.
Figure 1: Delphos: a multitask reinforcement learning framework for assisting choice model
specification across datasets. The agent learns to take a sequence of modelling actions to
propose utility specifications, while the environment returns feedback based on model fit,
complexity, and behavioural plausibility.
The previous formulation considers a single specification problem, whereas our objective
is to learn modelling strategies that transfer across related datasets. We therefore treat
each choice dataset as a separate multinomial logit utility specification taskτsampled
from a domain, such thatτ∼P(τ)(McFadden, 1978). The domain is represented by a
catalogue of modelling components that can be shared across tasks, including attributes,
transformations, taste structures, and covariates. Each datasetτuses a task-specific subset
that is compatible with its available variables and feasible modelling terms. Consequently,
each dataset induces its own MDP, with a task-specific state spaceSτ, action spaceA τ,
transition functionP(s τ,e+1 |s τ,e, aτ,e), and reward functionRτ.
To describe modelling decisions across specification problems, we define adomain cata-
loguecontainingallmodellingcomponentsthatmayappearacrosstheconsidereddatasets.
Formally, the domain catalogue is defined as
C={K,T,G,V},
whereKis the set of available attributes that may enter the utility functions, such as travel
time and travel cost.Tis the set of transformations that can be applied to these attributes,
includinglinear, logarithmic, andBox–Cox transformations.Gis theset oftaste structures,
which determine whether a parameter is generic across alternatives or alternative-specific.
Vis the set of covariates used to capture observed heterogeneity. Each dataset uses a
subsetC τ and induces an MDP with a dataset-specific state spaceSτ, action spaceA τ,
transition functionP τ, and reward functionRτ.
5

i)State space (Sτ).The state space comprises all feasible utility specifications that can
be constructed from the dataset-specific catalogueC τ. Each specification is represented
as a set of modelling terms. Each term encodes a decision about how a variable enters
the utility function. Specifically, a modelling term combines an attributekl ∈ Kτ with its
transformationt l ∈ Tτ, taste structuregl ∈ Gτ, and covariate interactionvl ∈ Vτ. Formally,
the state at interactioneis
sτ e ={x l}Le l=1, x l = (kl, tl, gl, vl),(4)
whereL e denotes the number of modelling terms in the specification. Attributes that are
not included in the current specification are encoded astl =g l =v l = 0.
To illustrate this representation, consider the following utility specification for the bus al-
ternative. It contains four modelling terms: an alternative-specific constant; travel time
with a logarithmic transformation and an alternative-specific coefficient; travel cost enter-
ing linearly with a generic coefficient that interacts with the two levels of the covariate
cov1; and headway, which is excluded from the specification.
V[["bus"]]= asc_bus #(1, linear, specific, none)
+ b_tt_bus * log(TT_bus) #(2, log, specific, none)
+ b_tc_female * Female * TC_bus #(3, linear, generic, female)
+ b_tc_male * (1-Female) * TC_bus #(3, linear, generic, male)
Using the catalogue indices (e.g., attributes: 0=None, 1=ASC, 2=TT, 3=TC, 4=HE;
transformations: 0=None, 1=Linear, 2=Log, 3=Box–Cox; taste structures: 0=None,
1=Generic, 2=Alternative-specific; covariates: 0=None, 1=COV1), the corresponding
state is
sτ e ={(1,1,2,0),(2,2,2,0),(3,1,1,1),(4,0,0,0)}(5)
This representation preserves the behavioural decisions that define a utility specification
while separating them from dataset-specific variable labels and availability. Consequently,
variables that capture the same behavioural construct can be encoded consistently across
datasets. Examples include total and in-vehicle travel time, or fare and travel cost. This
shared representation provides the basis for transferring modelling experience from one
specification problem to related tasks.
ii)Action space (A τ).The action space defines the feasible operations that the agent
can use to modify the current utility specification. Because each state is represented as
a set of modelling terms, the agent operates directly on these terms. It can add a term,
modify an existing term, or terminate the specification process. Formally, the action space
is
a∈ {add(k, t, g, v),change(k, t, g, v),terminate},(6)
whereaddintroduces a new modelling term,changeupdates the transformation, taste
structure, or covariate interaction of an existing term, andterminateends the specifica-
tion process and triggers model estimation.
Continuing the example, suppose that the agent first selectsadd(HE, linear, generic, none),
which introduces headway as a new modelling term. The updated specification is
6

s0 e →add(HE, linear, generic, none)→s 1 e
V[["bus"]]= asc_bus #(1, linear, specific, none)
+ b_tt_bus * log(TT_bus) #(2, log, specific, none)
+ b_tc_female * Female * TC_bus #(3, linear, generic, female)
+ b_tc_male * (1-Female) * TC_bus #(3, linear, generic, male)
+ b_he * HE_bus #(4, linear, generic, none)
The agent may then choosechange(TT, Box-Cox, specific, none). This action replaces the
logarithmic transformation of travel time with a Box–Cox transformation while preserving
the remaining modelling decisions. The resulting specification is
s1 e →change(TT, box-cox, specific, none)→s 2 e
V[["bus"]]= asc_bus #(1, linear, specific, none)
+ b_tt_bus * BoxCox(TT_bus) #(2, box-cox, specific, none)
+ b_tc_female * Female * TC_bus #(3, linear, generic, female)
+ b_tc_male * (1-Female) * TC_bus #(3, linear, generic, male)
+ b_he * HE_bus #(4, linear, generic, none)
This formulation decomposes utility specification into a sequence of modelling decisions,
whereby the agent progressively constructs a utility specification by adding and modifying
modelling terms until it selects theterminateaction. The previous example thus corre-
sponds to a trajectory of state transitions, in which the agent progressively updates the
specification through successive modelling actions before submitting the final candidate for
estimation.
s0
,→add(HE, linear, generic, none)→s 1
,→change(TT, box–cox, specific, none)→s 2
,→terminate→s 3
,→environment estimatess 3 →reward
To ensure that each decision contributes meaningfully to the specification process, the
available actions are dynamically restricted. The agent cannot select modelling compo-
nents that are unavailable in the dataset, actions that immediately reverse previous modi-
fications, or actions already selected in the current episode. An action-masking mechanism
implements these restrictions and ensures that the agent explores only feasible and non-
redundant specification trajectories (Huang & Ontañón, 2020).
iii)Reward signal (R τ).The reward signal evaluates the quality of the utility spec-
ification at the end of an episode. Through delayed credit assignment, this feedback is
propagated to the preceding sequence of modelling decisions. The agent can therefore
learn which decisions improve model performance over repeated trials. In a multitask
setting, however, goodness-of-fit measures such as log-likelihood cannot be used directly
because their magnitude depends on the sample size, model complexity, and baseline fit
of each dataset. Similar modelling decisions may therefore produce substantially different
rewards across datasets. This could bias learning towards datasets with larger absolute
improvements in log-likelihood. To provide a stable signal across heterogeneous datasets,
we define the reward as the per-observation improvement in log-likelihood relative to a
baseline model:
r= tanh
 LL ˆβ −LL baseline
Nobs

,(7)
Normalising by the number of observations makes the reward comparable across datasets
7

of different sizes. Thetanhtransformation bounds the reward within(−1,1)and improves
numerical stability in a similar way to reward clipping (Mnih et al., 2015; Hessel et al.,
2019). We use the null model as the baseline because it provides a lower bound for theo-
retically valid maximum-likelihood specifications (Mokhtarian, 2016). Specifications that
fail to converge receive a fixed penalty of−1. The reward can also accommodate richer
modelling objectives through penalties or incentives based on behavioural expectations.
For example, it could discourage specifications with implausible parameter signs, such as
positive travel-time or travel-cost sensitivities, statistically insignificant parameters, or es-
timation issues (Nova et al. (2025)).
iv)Environment.The environment provides the interface between the reinforcement
learning agent and the choice model estimation framework. After the agent selects the
terminateaction, the environment translates the final state into a complete utility speci-
fication and estimates it on the corresponding dataset using Apollo (Hess & Palma, 2019).
The resulting outcomes, including goodness-of-fit measures, convergence diagnostics, and
parameter estimates, are used to compute the reward in Eq. (7).
3.2 Learning transferable modelling decisions
To enable a single agent to learn and reuse modelling experience across choice datasets,
we extend Delphos to a multitask reinforcement learning framework. Instead of training a
separate agent for each specification problem, Delphos learns jointly across related prob-
lems. It learns both which modelling decisions tend to produce high-performing utility
specifications and the contexts in which those decisions are appropriate. A single policy,
however, requires a common representation of utility specifications despite differences in
the number and composition of their modelling terms.
To address this heterogeneity, we implement Delphos as a DeepSet-Q network (Hügle et
al., 2020). DeepSets encode unordered sets with varying numbers of elements as fixed-
length latent representations (Zaheer et al., 2017). They are therefore well suited to utility
specifications, whose modelling terms have no intrinsic order and may differ in number
and composition. In the single-task framework of Nova, Hess, & van Cranenburgh (2025),
each specification is represented as a fixed-length vector. By contrast, we represent utility
specifications as sets of modelling terms. Specifications from different datasets can there-
fore be represented consistently and processed by a single policy.
Figure 2: DeepSet-Q network (adapted from Hügle et al. (2020)). It combines a specifica-
tion encoder with a context-dependent Q-network. Each modelling term is embedded by
a shared networkϕ(·)and then aggregated through poolingρ(·)to obtain a latent repre-
sentation of the specification.
Figure 2 shows the proposed architecture, which combines a specification encoder with a
context-dependent Q-network. The architecture separates the representation of a utility
specification from the modelling context in which it is applied. The first component is the
DeepSet encoder (Zaheer et al., 2017), which maps the set of modelling termssτ e ={x l}Le l=1
8

to a fixed-length latent representation. Each termxl is embedded using a shared neural
networkϕ(·)and then aggregated through a permutation-invariant pooling operation,
Z(s τ e ) =ρ
 LeX
l=1
ϕ(xl)
!
,(8)
whereZ(s τ e )is the latent representation of the utility specification. Because the aggrega-
tion is invariant to the order and number of modelling terms, specifications from different
datasets are mapped to a common latent space.
The specification embedding alone does not identify which modelling terms are available
for the current dataset. Delphos therefore uses a task-specific context vectorxτ, which
encodes the availability of attributes, transformations, taste structures, and covariates in
the dataset-specific catalogueC τ. The specification embeddingZ(s τ e )and context vector
xτ are concatenated and provided as input to a deep Q-network (Mnih et al., 2015),
q=Q(Z(s τ e )||x τ ),(9)
which estimates the value of each feasible modelling decision in the current state. By
combining a shared specification representation with a task-specific context, Delphos learns
a single policy that can be applied across related datasets.
3.3 Multitask training and evaluation
Delphos is trained jointly across all specification tasks using a single DeepSet-Q network
whose parameters are shared across datasets. During each episode, a datasetτis sampled
at random, and the agent selects modelling actions until it reaches theterminateaction.
The environment estimates the resulting utility specification and assigns a reward accord-
ing to Eq. (7). Each interaction generates a transition(sτ e , aτ e , rτ e , sτ e+1), which is stored in
a shared experience replay buffer. The buffer therefore contains modelling experience from
all training datasets and is used to update the network.
The network parameters are updated following the deep Q-learning framework (Mnih et
al., 2015). At each optimisation step, a mini-batchBof transitions is sampled from the
buffer, and the temporal-difference loss is minimised,
L(θ) = 1 |B|
|B|X
b=1

Qtarget(s′, a′;θ −)−Q(s, a;θ) 2 ,(10)
whereθandθ − denote the parameters of the policy and target networks, respectively. The
loss compares the estimated value of a modelling decision with a target that combines the
observed reward and expected value of subsequent decisions. By minimising this error,
Delphos learns to favour decisions that improve the current utility specification and lead
to more promising sequences of decisions over time.
To prevent datasets with longer specification trajectories from dominating optimisation, we
sample balanced mini-batches from the replay buffer so that each task contributes similarly
to the parameter updates (Sutton & Barto, 2018). During training,ϵ-greedy exploration
is gradually reduced, shifting the agent from exploration towards decisions associated with
high-performing specifications. This design follows the purpose of experience replay in
deep reinforcement learning (Schaul et al., 2015) and provides balanced (Sodhani et al.,
2021) and diverse (Ross & Bagnell, 2010) exposure across tasks.
During inference, the trained agent is applied directly to unseen datasets without further
training. Given the task-specific catalogueC τ, Delphos selects a sequence of modelling
9

decisions before submitting a utility specification for estimation. By repeating this process,
Delphos proposes and estimates a set of high-performing candidates. Modellers can then
inspect and compare the resulting models using criteria such as goodness-of-fit, behavioural
plausibility, and parameter significance. Delphos thus acts as a specification assistant that
reuses experience from related problems while adapting its decisions to previously unseen
datasets.
4 Experiments
This section evaluates the proposed multitask reinforcement learning framework. We first
introduce the choice datasets used for training and inference (Subsection 4.1). We then
describe the metrics used to assess learning and transferability (Subsection 4.2). Finally,
we present the studies used to evaluate whether modelling experience transfers across
specification problems and whether the specifications generated for unseen datasets are
behaviourally plausible (Subsection 4.3).
4.1 Datasets
Table 1 summarises the transport choice datasets used in this paper. The first nine are
used for training, while Decisions and Swissmetro are held out for inference. Each dataset
defines a different specification problem, with its own choice context, alternatives, available
attributes, socio-demographic variables, and sample size. Although the datasets differ in
their observed variables and experimental settings, they share behavioural concepts such
as travel time and travel cost, among others.
4.2 Evaluation metrics
The experiments evaluate two aspects of the proposed framework: (i) its ability to learn
sequences of modelling decisions that produce high-performing utility specifications during
multitask training and (ii) its ability to transfer these strategies to unseen specification
problems during inference.
During training, Delphos sequentially proposes utility specifications and receives feedback
from the estimation environment. We evaluate learning performance using the average
reward, maximum reward, and area under the learning curve. These metrics measure the
average quality of the modelling trajectories, the quality of the best specification found,
and overall learning efficiency, respectively. To characterise exploration, we also report
the convergence rate, defined as the proportion of estimated specifications that converge
successfully, and the proportion of novel specifications explored during training.
During inference, the trained agent is applied to unseen datasets without further training.
We use the same metrics to evaluate the generated specifications and the transferability of
the learnt policy. We also derive the Pareto front to examine the trade-off between model
fit and complexity and to characterise the models that Delphos tends to propose.
4.3 Evaluation studies
To evaluate Delphos’ ability to learn transferable modelling strategies, we examine whether
it can use experience across datasets to improve sample efficiency and whether the gener-
ated specifications balance model fit, parsimony, and behavioural plausibility.
First, we evaluate whether the proposed multitask framework improves Delphos’ ability
to learn and transfer modelling experience across specification problems. We compare the
10

Table 1: Choice modelling tasks used for multitask training and inference.
T askτ τ 1 τ2 τ3 τ4 τ5 τ6 τ7 τ8 τ9 τ10 τ11
T raining datasets✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
Choice attributes
Travel time✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
Travel cost✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
Out-of-vehicle time✓ ✓ ✓ ✓ ✓ ✓ ✓
Transfers✓ ✓ ✓ ✓ ✓
Service quality✓ ✓ ✓
Reliability✓ ✓
Socio-demographic variables
Gender✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
Income✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
Age✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
Purpose✓ ✓ ✓ ✓ ✓ ✓ ✓
Car access✓ ✓ ✓ ✓
Business✓ ✓ ✓
Education✓ ✓ ✓ ✓
Dataset characteristics
Panel data✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
Alternatives 4 2 2 2 3 3 4 2 3 6 3
Sample size 7000 3492 1511 52488 6570 1576 81086 1521 850 9356 5409
LL0 -8196 -2420 -1047 -36381 -5885 -1731 -112409 -1054 -966 -11233 -5548
LLlinear -5761 -1665 -732 -33026 -4734 -1121 -71099 -812 -924 -4294 -4346
Hess & Palma (2019)
Axhausen et al. (2008)
Bierlaire (2018)
Ramjerdi et al. (2010)
Arentze & Molin (2013)
Ibeas et al. (2014)
Hillel et al. (2018)
Bierlaire (2018)
Van Cranenburgh et al. (2019)
Calastri et al. (2020)
Bierlaire et al. (2001)
proposed DeepSet-Q architecture with the single-task DQN framework introduced by Nova
et al. (2025). All agents are trained for 10,000 episodes using the hyperparameter config-
uration reported in Appendix 5. The multitask agent is trained jointly across all training
datasets, whereas each single-task agent is trained independently on its corresponding
dataset. We evaluate learning and transfer using the metrics introduced in Subsection 4.2.
Second, we assess the quality of the utility specifications generated by Delphos for unseen
datasets. We compare the Pareto-optimal specifications identified by Delphos with bench-
mark models from the original studies and with other assisted specification approaches. We
consider model performance, parsimony, and behavioural plausibility to determine whether
the transferred policy produces competitive models that are consistent with established
choice modelling practice.
5 Resul ts
This section presents the results of the two evaluation studies. We first examine learning
during multitask training and then assess the utility specifications generated for unseen
datasets.
11

5.1 Learning transferable specification strategies
Figure 3 compares the learning curves of the proposed multitask DeepSet-Q agent with
those of the single-task DQN agents across the training datasets. For most datasets, both
approaches achieve progressively higher rewards during training. However, the multitask
agent generally learns faster and reaches higher reward levels. This suggests that updating
a single policy with experience from multiple specification problems improves its ability to
generalise across datasets.
Figure 3: Learning curves of the single-task DQN agents and the proposed multitask
DeepSet-Q agent across the training datasets.
Learning performance varies across datasets. The gains are larger for LondonModeChoice,
SpainParkingChoice, and ApolloModeChoice, and the differences are smaller for Nor-
wayVTT and VanCranenburghVOT. One possible explanation is the complexity of the
underlying specification problem. Datasets with more attributes and feasible covariate
interactions define larger specification spaces and require longer sequences of modelling
decisions. In these settings, experience from related datasets provides greater guidance
during specification. By contrast, NorwayVTT and VanCranenburghVOT contain only
two attributes: travel time and travel cost. Their smaller specification and action spaces
make transferred modelling experience less beneficial.
Table 2 summarises the performance of the single-task DQN agents and the proposed
multitask DeepSet-Q agent across the training datasets. The multitask agent generally
achieves higher mean rewards, maximum rewards, and areas under the learning curve.
These improvements indicate that sharing modelling experience across specification prob-
lems enables Delphos to learn more effective policies. The main exception is VanCranen-
burghVOT, for which the two approaches perform similarly. This result is consistent with
its smaller specification space.
From a reinforcement learning perspective, the higher rewards are accompanied by larger
areas under the learning curve, which suggests that Delphos reaches high-performing speci-
12

Table 2: Learning performance on the training datasets.
Dataset Agent Mean Reward Max Reward AUC Novel Specs (%) Estimable Specs (%)
ApolloModeChoice DQN 0.151 0.334 146693.6682.74
DeepSet-Q 0.187 0.434 183991.7585.56
SwissmetroRouteChoice DQN 0.033 0.219 29195.8684.62
DeepSet-Q 0.082 0.220 76192.8788.52
NLModeChoice DQN -0.1110.216-116196.2772.80
DeepSet-Q -0.0420.205-49789.5478.61
NorwayVTT DQN 0.130 0.168 130026.24 99.84
DeepSet-Q 0.140 0.173 139422.6699.84
Arentze2013 DQN -0.273 0.008 -282577.9062.01
DeepSet-Q -0.199 0.111 -209663.3268.35
SpainParkingChoice DQN -0.237 0.176 -247317.9954.91
DeepSet-Q -0.058 0.270 -69813.6468.21
LondonModeChoice DQN -0.1960.518-208696.7452.62
DeepSet-Q -0.0560.497-71691.8161.22
Optima DQN -0.297 0.181 -306096.4757.61
DeepSet-Q -0.228 0.183 -237689.2763.83
VanCranenburghVOTDQN 0.0640.086635 27.77 99.73
DeepSet-Q 0.0600.089597 25.20 99.72
fications earlier during training. Notably, these improvements are obtained while exploring
a slightly smaller proportion of novel specifications. This suggests that modelling experi-
ence acquired from related datasets makes the search more sample-efficient, which allows
the agent to identify promising sequences of modelling decisions with fewer unsuccessful
specification trials.
This behaviour is also reflected from a choice modelling perspective. Although the multi-
task agent explores fewer unique specifications, it consistently produces a larger proportion
of successfully estimated models across almost all datasets. This suggests that the trans-
ferred modelling experience not only improves model fit but also guides the search towards
specifications that are more likely to be successful estimated.
5.2 Application to unseen datasets
Swissmetro
When applied to the unseen Swissmetro dataset (τ11; (Bierlaire et al., 2001)), Delphos
proposes 283 candidate models within a computational budget of 20 minutes on a laptop
CPU. Figure 4 shows all converged candidates and the resulting Pareto front, whose non-
dominated models balance model performance and parsimony. Thirteen of the converged
specifications are non-dominated. Within the computational budget, Delphos identifies a
best specification with a log-likelihood of−0.681per observation. This result improves
on both the linear baseline (LLlinear =−1.029) and the value of−0.72per observation
reported for the VNS assisted specification method by Ortelli et al. (2021).
13

Figure 4: Pareto front of Delphos candidates on the Swissmetro dataset. Grey dots show
all converged specifications proposed during inference. Stars indicate the non-dominated
candidates, and circles show the specifications with the best AIC and log-likelihood values.
Table 3: Best specification identified by Delphos on Swissmetro.
Modelling term Included Taste Transformation Interaction
ASC✓Specific –
Travel time✓Specific Log Age
Travel cost✓Specific Log Gender
Headway✓Generic Linear Gender
Seat type✓Generic Linear Income
LL(0) -6,964.66
LL(final) -4,603.96
AIC 9,265.92
BIC 9,463.70
Rho-squared 0.34
Adj. Rho-squared 0.34
Observations 6,768
Number of parameters 29
LL/N– Delphos -0.68
LL/N– VNS Ortelli et al. (2021) -0.72
14

Table 3 reports the specification identified by Delphos and its fit statistics. The model
includes constants specific to each alternative and relevant attributes with either generic
parameters or parameters that vary across alternatives. It also introduces non-linear trans-
formations and meaningful covariate interactions. These results suggest that Delphos can
transfer modelling decisions to an unseen dataset and identify a competitive, behaviourally
plausible specification within a limited computational budget. Inference runs on a standard
laptop CPU, making the approach practical for analysts seeking to reduce specification ef-
fort and for researchers studying reusable modelling strategies.
Decisions
We apply the same trained multitask agent to the unseen Decisions dataset (τ10; (Calastri
et al., 2020)) using the same 20-minute computational budget. Figure 5 shows all converged
specifications and the resulting Pareto front. Without further training, Delphos identifies
a set of non-dominated models. This result suggests that the learnt policy continues to
select effective modelling actions for a different and unseen specification problem. The
specification with the best AIC has a log-likelihood of−0.37per observation, improving
on the linear additive model (LLlinear =−0.46). Its performance is also comparable to
the value of−0.36reported for the MNL specification developed by expert modellers in
Tsoleridis et al. (2022), as shown in Table 4. The Delphos specification includes alternative-
specific constants, non-linear transformations, and interactions with socio-demographic
variables.
Figure 5: Pareto front of Delphos candidates on the Decisions dataset. Grey dots show
all converged specifications proposed during inference. Stars indicate the non-dominated
candidates, and circles show the specifications with the best AIC and log-likelihood values.
Although the two datasets differ substantially in sample size, choice-set structure, and
available variables, the same transferred policy identifies competitive specifications for
both. Delphos achieves a higher log-likelihood per observation than the VNS benchmark
on Swissmetro and performance comparable to a published MNL specification developed
by expert modellers on Decisions.
15

Table 4: Best specification identified by Delphos on Decisions.
Modelling term Included Taste Transformation Interaction
ASC✓Specific – Purpose
Travel time✓Specific Linear N. Car
Travel cost✓Generic Box-Cox N. Car
Headway✓Specific Log Gender
LL(0) -11,233.44
LL(final) -3,481.79
AIC 7,055.59
BIC 7,384.20
Rho-squared 0.69
Adj. Rho-squared 0.69
Observations 9,356
Number of parameters 46
LL/N– Delphos -0.37
LL/N– Tsoleridis et al. (2022) -0.36
6 Conclusions
This paper extends Delphos to a multitask reinforcement learning setting for assisted dis-
crete choice model specification across related transport datasets. We formulate speci-
fication as a sequential decision problem in which an agent builds a candidate through
modelling actions and submits it to an estimation environment. A DeepSet-Q architecture
represents each candidate as a set of modelling terms and combines this representation
with dataset-specific context. This design allows the same decision rule to be applied
across datasets with different variables.
Our results show that Delphos learns reusable modelling strategies that transfer across
specification problems. During training, the multitask agent consistently outperforms inde-
pendently trained single-task agents. It achieves higher rewards, greater sample efficiency,
and a larger proportion of successfully estimated specifications while exploring fewer can-
didates. These results suggest that shared modelling experience guides the search towards
promising specification trajectories rather than simply encouraging broader exploration.
When applied without further training to the unseen Swissmetro and Decisions datasets,
the same agent identifies competitive and behaviourally meaningful specifications in less
than 20 minutes on a standard CPU. It achieves a higher log-likelihood per observation
than the VNS benchmark on Swissmetro and performance comparable to a published MNL
specification developed by expert modellers on Decisions. Overall, these findings highlight
the potential of reinforcement learning to accumulate and reuse experience for assisted
choice model specification.
Beyond these results, the framework can reduce the cognitive and computational burden
of manual trial and error and provide suggestions for behaviourally sound utility specifica-
tions. This support may help reduce the risk of misspecification, which can bias parameter
estimates, weaken forecasts, and lead to misleading welfare conclusions. Delphos may
therefore help choice modellers build utility functions that can be used to derive marginal
effects and willingness-to-pay measures, including values of travel time savings for cost-
benefit analysis.
The multitask training setup has several limitations. First, Delphos is trained on only
nine datasets and evaluated on two unseen datasets. Although these datasets have distinct
catalogues, broader validation across additional problems is needed to assess the generality
of the learnt policy. Second, the reward function is based mainly on goodness-of-fit and
convergence. It could be extended to include explicit behavioural constraints, as in (Nova,
16

Hess, & van Cranenburgh, 2025). Finally, the current framework transfers a fixed policy
without adapting it to new datasets during inference.
Delphos can be then used as a software package for assisted choice model specification
and estimation. The modeller first defines a catalogue of attributes, socio-demographic
characteristics, non-linear transformations, and taste structures. The agent then proposes
and returns successfully estimated utility specifications on the Pareto front. The modeller
can compare these models and select promising candidates for further diagnosis, refine-
ment, and validation. This workflow automates part of the search while retaining modeller
control over interpretation and final selection.
Future work will extend the experimental setup to a larger set of datasets to assess trans-
ferability across a broader range of modelling contexts. We will also investigate context
representations that describe each problem using dataset statistics and behavioural fea-
tures, rather than only the availability of catalogue components. These representations
may enable more informed decisions across heterogeneous datasets. Finally, we will eval-
uate few-shot adaptation strategies to determine when a shared policy can be efficiently
specialised to a new dataset using only a small number of additional training episodes.
Acknowledgements
Stephane Hess acknowledges support from the European Research Council through the
Advanced Grant 101020940-SYNERGY.
17

Appendix
Table 5: Hyperparameter configuration used for DeepSet-Q.
Domain catalogue
Attributes(|K|)7
Transformations(|T |)3
Taste structures(|G|)2
Covariates(|V|)7
Training datasets 9
DeepSet encoder
Input modelling term(k, t, g, v)
Embedding dimensions(16,8,8,16)
Hidden layer 1 128
Hidden layer 2 64
Modelling term (dterm) 64
Pooling Mean
Specification embedding (Z(s)) 64
Activation ReLU
Weight initialisation Kaiming uniform
Trainable parameters 27,384
Deep Q-network
Specification embedding 64
Context vector 19
Input dimension 83
Hidden layer 1 256
Hidden layer 2 256
Output actions 297
Activation ReLU
Weight initialisation Kaiming uniform
Trainable parameters 158,761
T raining V alue
Episodes per task 10,000
Learning updates 10,000
Replay buffer sampling 10,000
Mini-batch size 64
Discount factor (γ) 0.90
Learning rate1×10 −3
Target update (τ) 0.005
ϵ-greedy exploration Linear decay
18

References
Arentze, T. A., & Molin, E. J. (2013). Travelers’ preferences in multimodal networks: Design and
results of a comprehensive series of choice experiments.Transportation Research Part A: Policy
and Practice,58, 15–28.
Axhausen, K. W., Hess, S., König, A., Abay, G., Bates, J. J., & Bierlaire, M. (2008). Income and
distance elasticities of values of travel time savings: New swiss results.Transport Policy,15(3),
173–185.
Beeramoole, P. B., Arteaga, C., Pinz, A., Haque, M. M., & Paz, A. (2023). Extensive hypothesis
testing for estimation of mixed-logit models.Journal of choice modelling,47, 100409.
Bierlaire, M. (2018).Description of the netherlands mode choice dataset.Transport
and Mobility Laboratory, EPFL. Retrieved fromhttps://transp-or.epfl.ch/documents/
technicalReports/CS_ParkingDescription.pdff(Biogeme example dataset)
Bierlaire, M., Axhausen, K., & Abay, G. (2001). The acceptance of modal innovation: The case
of swissmetro. InSwiss transport research conference.
Buckell, J., Marti, J., & Sindelar, J. L. (2019). Should flavours be banned in cigarettes and e-
cigarettes? evidence on adult smokers and recent quitters from a discrete choice experiment.
Tobacco control,28(2), 168–175.
Calastri, C., Crastes dit Sourd, R., & Hess, S. (2020). We want it all: experiences from a survey
seeking to capture social network structures, lifetime events and short-term travel and activity
planning.Transportation,47, 175–201.
de Vries, M. O., Hernández, J. I., & Mouter, N. (2025). The value of accessibility, health, safety,
inclusion and sustainability: a public willingness to pay experiment.Research in Transportation
Economics,113, 101605.
Ghorbani, A., Nassir, N., Lavieri, P. S., Beeramoole, P. B., & Paz, A. (2025). Enhanced utility
estimation algorithm for discrete choice models in travel demand forecasting.Transportation,
1–28.
Haj-Yahia, S., Mansour, O., & Toledo, T. (n.d.). Grammar-based approach to data-driven utility
specification for discrete choice models.Available at SSRN 5195530.
Hess, S., & Daly, A. (2024).Handbook of choice modelling. Edward Elgar Publishing.
Hess, S., & Palma, D. (2019). Apollo: A flexible, powerful and customisable freeware package for
choice model estimation and application.Journal of choice modelling,32, 100170.
Hessel, M., Soyer, H., Espeholt, L., Czarnecki, W., Schmitt, S., & Van Hasselt, H. (2019). Multi-
task deep reinforcement learning with popart. InProceedings of the aaai conference on artificial
intelligence(Vol. 33, pp. 3796–3803).
Hillel, T., Elshafie, M. Z., & Jin, Y. (2018). Recreating passenger mode choice-sets for transport
simulation: A case study of london, uk.Proceedings of the Institution of Civil Engineers-Smart
Infrastructure and Construction,171(1), 29–42.
Huang, S., & Ontañón, S. (2020). A closer look at invalid action masking in policy gradient
algorithms.arXiv preprint arXiv:2006.14171.
Hügle, M., Kalweit, G., Werling, M., & Boedecker, J. (2020). Dynamic interaction-aware scene
understanding for reinforcement learning in autonomous driving. In2020 ieee international
conference on robotics and automation (icra)(pp. 4329–4335).
Ibeas, A., Dell’Olio, L., Bordagaray, M., & Ortúzar, J. d. D. (2014). Modelling parking choices
considering user heterogeneity.Transportation Research Part A: Policy and Practice,70, 41–49.
Mariel, P., Hoyos, D., Meyerhoff, J., Czajkowski, M., Dekker, T., Glenk, K., ... others (2021).
Environmental valuation with discrete choice experiments: Guidance on design, implementation
and data analysis. Springer Nature.
19

McFadden, D. (1978). Modelling the choice of residential location. InSpatial interaction theory
and planning models(pp. 75–96). North-Holland.
Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Veness, J., Bellemare, M. G., ... others
(2015). Human-level control through deep reinforcement learning.nature,518(7540), 529–533.
Mokhtarian, P. L. (2016). Discrete choice models’ρ2: A reintroduction to an old friend.Journal
of choice modelling,21, 60–65.
Nova, G., Hess, S., & van Cranenburgh, S. (2025). Delphos: A reinforcement learning framework
for assisting discrete choice model specification.arXiv preprint arXiv:2506.06410.
Nova, G., van Cranenburgh, S., & Hess, S. (2025). Understanding the decision-making process of
choice modellers.Journal of choice modelling,56, 100562.
Ortelli, N., Hillel, T., Pereira, F.C., deLapparent, M.,&Bierlaire, M. (2021). Assistedspecification
of discrete choice models.Journal of choice modelling,39, 100285.
Páez, A., & Boisjoly, G. (2022).Discrete choice analysis with r. Springer.
Plaat, A. (2022).Deep reinforcement learning(Vol. 10). Springer.
Ramjerdi, F., Flügel, S., Samstad, H., & Killi, M. (2010). Value of time, safety and environment
in passenger transport–time.TØI report B,1053.
Rodrigues, F., Ortelli, N., Bierlaire, M., & Pereira, F. C. (2020). Bayesian automatic relevance
determination for utility function specification in discrete choice models.IEEE Transactions on
Intelligent Transportation Systems,23(4), 3126–3136.
Ross, S., & Bagnell, D. (2010). Efficient reductions for imitation learning. InProceedings of the
thirteenth international conference on artificial intelligence and statistics(pp. 661–668).
Schaul, T., Quan, J., Antonoglou, I., & Silver, D. (2015). Prioritized experience replay.arXiv
preprint arXiv:1511.05952.
Sfeir, G., Nova, G., Hess, S., & van Cranenburgh, S. (2025). Can large language models assist
choice modelling? insights into prompting strategies and current models capabilities.arXiv
preprint arXiv:2507.21790.
Sodhani, S., Zhang, A., & Pineau, J. (2021). Multi-task reinforcement learning with context-based
representations. InInternational conference on machine learning(pp. 9767–9779).
Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction.A Bradford Book.
Tsoleridis, P., Choudhury, C. F., & Hess, S. (2022). Deriving transport appraisal values from
emerging revealed preference data.Transportation Research Part A: Policy and Practice,165,
225–245.
Van Cranenburgh, S., & Alwosheel, A. (2019). An artificial neural network based approach to
investigate travellers’ decision rules.Transportation Research Part C: Emerging Technologies,
98, 152–166.
Van Cranenburgh, S., Wang, S., Vij, A., Pereira, F., & Walker, J. (2022). Choice modelling in the
age of machine learning-discussion paper.Journal of choice modelling,42, 100340.
Watkins, C. J., & Dayan, P. (1992). Q-learning.Machine learning,8, 279–292.
Zaheer, M., Kottur, S., Ravanbakhsh, S., Poczos, B., Salakhutdinov, R. R., & Smola, A. J. (2017).
Deep sets.Advances in neural information processing systems,30.
20
