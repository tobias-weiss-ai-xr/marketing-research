---
title: 'OptScientist: Automated Discovery of Optimization Laws'
url: https://arxiv.org/abs/2610.28562
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Ma ZhenYao
- Yue Liang
- Jian-Qiao Zhu
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.28562
pages: 42
chars: 140956
fetched_at: '2026-11-08T13:31:23+00:00'
kb_version: 1
---

# OptScientist: Automated Discovery of Optimization Laws

OptScientist:
Automated Discovery of Optimization Laws
Ma ZhenYao∗1,2 , Yue Liang1,3, and Jian-Qiao Zhu4
1Plokerm AI Lab
2Xiamen University
3University of Tübingen
4The University of Hong Kong
Abstract
Many scientific phenomena are best understood as outcomes of underlying op-
timization problems, yet automated scientific discovery has largely focused on
recovering equations that describe observed input–output patterns. We introduce
OptScientist, a novel automated framework for discovering compact symbolic
optimization laws directly from data. OptScientist comprises (i) a model that
infers symbolic optimization problems by first learning to represent data as an
optimization problem and then extracting its symbolic form, and (ii) an LLM agen-
tic system embedding the model in a discovery process that integrates theoretical
priors from scientific literature, discovers candidate laws, abstracts their underlying
mechanisms, and suggests new data to collect. We first evaluate OptScientist on
OptFeynman, a novel benchmark of 99 physics-derived optimization problems,
where OptScientist recovers ground-truth laws for over 80% of the problems and
remains robust to noisy contextual information, while substantially outperforming
machine-learning, symbolic, and LLM-based model-discovery baselines. On hu-
man risky choice and central-bank monetary policy, OptScientist discovers compact
symbolic optimization laws that achieve held-out predictive performance compet-
itive with leading baselines, while using few parameters and substantially fewer
tokens than LLM baselines. Overall, OptScientist extends automated scientific
discovery to uncovering optimization laws that generate observed phenomena,
enabling automated theory building across the physical, biological, behavioral, and
social sciences.
1 Introduction
Across the sciences, many influential theories characterize observed phenomena as solutions to
optimization problems. Examples include energy or free-energy minimization principles for charac-
terizing equilibrium states in statistical physics (Gibbs, 1902; Landau & Lifshitz, 2013), optimality
models for explaining how biological fitness shapes evolutionary outcomes (Wright et al., 1932;
Fisher, 1999), rational and resource-rational analyses of human behavior and cognition (Samuelson,
1948; Debreu, 1959; Anderson, 1991; Lieder & Griffiths, 2020), and intertemporal optimization for
modelling dynamic macroeconomic systems (Ramsey, 1928; Ljungqvist & Sargent, 2018). Devel-
oping such theories requires identifying objectives and relevant constraints that jointly account for
observed outcomes. However, these components are typically formulated by domain experts and
only subsequently evaluated against data, making optimization-based theory construction largely
manual and dependent on specialized insight. This reliance on expert formulation creates a substantial
bottleneck for theory discovery across scientific domains. A fundamental question therefore remains:
Can optimization laws be discovered automatically from observational data?
∗Corresponding author: zhenyaoma@163.com
arXiv:2610.28562v1  [cs.AI]  20 Oct 2026

The complexity of real-world scientific data further exacerbates this bottleneck, as observations
are often noisy, high-dimensional, and shaped by complex interactions. Hand-crafted interpretable
models may fail to capture complex patterns, whereas flexible data-driven approaches, particularly
machine-learning methods, have demonstrated strong predictive performance across physics (Baldi
et al., 2014; Carleo & Troyer, 2017), biology (Poplin et al., 2018; Jumper et al., 2021), and behavioral
and social sciences (Kosinski et al., 2013; Peterson et al., 2021; Zhu et al., 2025).
Recent advances in scientific machine learning have enabled data-driven discovery of symbolic laws
(Champion et al., 2019; Udrescu & Tegmark, 2020; Cranmer et al., 2020), embedded mathematical
structure into flexible ML models (Chen et al., 2018; Liu et al., 2025; Ma et al., 2026b), and integrated
scientific theories with machine learning (Raissi et al., 2019; Peterson et al., 2021). However, these
approaches have largely focused on recovering input–output equations or learning models without
explicit symbolic structure, while optimization-structured scientific ML models (Ma et al., 2026b) still
require human interpretation of optimization structures and lack an end-to-end process for automated
theory discovery. Consequently, automatically discovering compact symbolic optimization laws from
real-world data remains a fundamental challenge.
To address these challenges, we introduceOptScientist,a novel framework that uses AI methods to
automate the discovery of optimization laws.OptScientist has two components: a novel symbolic-
discovery model and an agentic research system. First, the symbolic-discovery model (OptScientist
Model) learns to represent observational data as an optimization problem using a hierarchical opti-
mization network with an optimization representation bottleneck, enabling denoising, information
compression, and automatic extraction of interpretable features. It then distills this learned opti-
mization representation into a compact symbolic optimization problem. The second component, the
OptScientist Agent, places this discovered symbolic model inside an automated scientific-discovery
loop. A Theory Prior Agent proposes scientific priors, candidate variables and mechanism hypotheses.
An Experiment Agent then uses the OptScientist Model to search for compact symbolic optimization
laws from data. Finally, a Scientific Critic and Theory Abstraction Agent evaluates and selects the
discovered laws, abstracts the selected laws into a general form and qualitative mechanisms, and
suggests new variables or data for the next round of discovery. Together, the model and agent form
an iterative system for proposing, discovering and refining optimization laws.
We conduct three experiments spanning physical systems, human behaviour, and macroeconomic
policy. First, to test whether the core OptScientist Model can recover ground-truth optimization laws
(Sec. 4.1), we introduceOptFeynman(Sec. 5.1), a novel synthetic benchmark of 99 optimization
problems derived from analytic physics equations, where observations are generated as noisy samples
from the induced optimization landscapes. On held-out contexts, OptScientist Model shows strong
recovery of the generating laws, achieving perfect exact-order recovery on 88 of 99 discrete problems
and 78 of 99 continuous problems, while substantially outperforming machine-learning, symbolic-
regression, and LLM model-discovery baselines. Our results also suggest that OptScientist remains
robust even when context variables are noisy. We then apply OptScientist to two autonomous
scientific-discovery tasks on real-world data for which the underlying laws are unknown. In human
decisions under risk and ambiguity (Sec. 4.2), OptScientist discovers an optimization law combining
expected reward, cognitive switching cost and counterfactual reward. In central-bank monetary
decisions (Sec. 4.3), it discovers a law in which observed policy tracks a latent subjective target
through squared-error minimization. Across both domains, the discovered laws remain competitive
with the strongest baselines while using near-minimal parameter counts and symbolic complexity,
and substantially fewer output tokens than LLM-based model-discovery methods.
Overall, our contributions are threefold. First, we introduce the OptScientist Model, which, to the
best of our knowledge, is the first scientific machine-learning framework for learning symbolic
optimization problems directly from observational data. Second, for science, we develop OptScientist,
a hybrid symbolic–LLM system that extends automated scientific discovery to optimization-law
discovery in domains associated with optimization models. Third, at the paradigm level, we contribute
to inverse optimization, revealed preference and related fields by moving beyond parameter estimation
for pre-specified optimization problems, providing a new methodology for directly recovering
optimization laws themselves from data.
2 Related Work
2

Symbolic discovery.Recent advances in symbolic regression have enabled symbolic law discovery
from data. Most existing approaches, however, recover input–output laws, such as y=f(x) (Koza,
1994; Schmidt & Lipson, 2009; Udrescu & Tegmark, 2020), or physical equations expressed through
differential relationships, such as dx dt =f(x, t) (Brunton et al., 2016; Rudy et al., 2017; Champion et al., 2019). They are less suited to settings where the scientific law is itself an optimization
problem. OptScientist learns symbolic optimization problems from observational data, providing a
new symbolic-discovery model for scientific domains associated with optimization models.
LLM-based automated scientific discovery.LLMs have been used to propose and refine symbolic
functional forms or governing equations (Merler et al., 2024; Du et al., 2024; Shojaee et al., 2025), and
to automate broader scientific workflows such as hypothesis generation, experimentation and iterative
refinement (Lu et al., 2026; Gottweis et al., 2026; Aygün et al., 2026). Recent LLM-based work also
searches for symbolic utility expressions to support group-level prediction (Zhao et al., 2026), but
rarely recovers parsimonious scientific laws. Despite their broad role in scientific automation, these
systems are not designed to discover compact symbolic optimization problems from data. OptScientist
does not remove LLMs entirely. Instead, it suggests that greater efficiency and performance can
be achieved by combining a symbolic discovery model with an auxiliary LLM agentic system to
improve and interpret the discovered laws and add semantic meaning to them.
Cognitive discovery.Some cognitive-discovery methods use black-box predictions or structured
neural architectures to recover interpretable mechanisms from behavioural data (Agrawal et al., 2020;
Peterson et al., 2021; Miller et al., 2023; Zhu et al., 2025; Ji-An et al., 2025; Ma et al., 2026b),
while others use LLMs to generate and revise executable models, diagnose theory failures and design
informative experiments (Binz et al., 2025; Rmus et al., 2026; Éltet˝o et al., 2026; Jagadish et al., 2026).
These approaches recover programs or reduced-form decision rules rather than compact symbolic
optimization laws. Moreover, human behaviour is often modelled through resource-rational analysis
(Debreu, 1959; Lieder & Griffiths, 2020; Zhu & Griffiths, 2026), which formulates behaviour using
hand-specified optimization models. As a general framework for automated discovery of optimization
laws, OptScientist can support automated resource-rational analysis.
Inverse optimization.Inverse optimization (Ahuja & Orlin, 2001; Aswani et al., 2018) and related
approaches, including revealed preference (Afriat, 1967; Varian, 1982), inverse reinforcement learning
(Ng et al., 2000; Ziebart et al., 2008), and optimization-based hierarchical network models (Ma et al.,
2026b), infer latent objectives or estimate the parameters of pre-specified optimization problems.
However, they generally assume the functional form of the optimization problems. OptScientist
provides a new methodology in which the optimization law itself can be recovered from data without
prespecifying its functional form.
3 The OptScientist
3.1 Formalizing Optimization-Law Discovery
Generally, a law expressed as optimization describes an outcome y as the solution to an objective
under constraints,
max
y∈Y
U(x,y)s.t.C(x,y)≤0,T(x,y) = 0.(1)
Here x denotes the observed context, U(·) is the objective, C(·) represents inequality constraints, and
T(·) represents equality constraints or target conditions. This form covers a broad class of scientific
laws in which observed outcomes arise from maximizing a quantity, possibly under constraints.
For learning, it is useful to express the same object as a single scalar landscape. Under standard local
regularity conditions, the constrained problem in Eq. (1) admits a locally exact penalty representation
(Han & Mangasarian, 1979),
max
y∈Y
λ0 ϕ

U(x,y)

−λ ⊤ 1 ρ  C(x,y)  −λ ⊤ 2 ψ  T(x,y)  ,(2)
Here ϕ is strictly increasing, ρ(z) = max{z,0} penalizes violated inequality constraints, and
ψ(z) =|z| penalizes deviations from equality constraints. This reformulation places objectives and
constraints inside one optimization score, making the law easier to analyse and learn.
The outcome generated by an optimization law can be represented in two ways. In the deterministic
case, the predicted outcome is by(x) = arg maxy∈Y S(x,y) , where S(x,y) is a scalar representation
3

of the underlying optimization problem. For example, under the exact-penalty reformulation in
Eq. (2), S is given by the objective together with penalties for violated constraints. In noisy systems,
the same score defines a probability distribution over possible outcomes,
p(y|x) = exp(S(x,y)/τ)/Z(x),(3)
where τ >0 controls the level of noise and Z(x) is the normalizing term. As τ decreases, the
distribution concentrates on the maximizers of S; for larger τ, it describes noisy realizations of the
same underlying optimization principle.
Therefore, we formulate the central question of optimization-law discovery as follows.
Question 1 (Optimization-Law Discovery) Given observational data D={(x i,y i)}N i=1 gener-
ated by an unknown optimization lawL ∗ of the form
max
y∈Y
U ∗(x,y)s.t.C ∗(x,y)≤0,T ∗(x,y) = 0,
where outcomes arise either as optimal solutions or as stochastic realizations of the induced opti-
mization landscape, can we recover a compact symbolic law
bL= ( bU ,bC, bT)
without pre-specifying the functional forms of its components, such that it reproduces the observable
implications ofL ∗?
3.2 OptScientist Model
To discover compact optimization laws from data directly, the OptScientist Model consists of two
stages: the Optimization Learner (OptLearner; see Figure 1a Left) and the Optimization Discoverer
(OptDiscover; see Figure 1a Right).
3.2.1 Optimization Learner
Observational data rarely reveal the optimization law directly. They may be noisy, high-dimensional,
redundant, or expressed in variables that are not yet suitable for symbolic modelling. The Optimiza-
tion Learner (OptLearner) addresses this challenge by learning to represent observational data as an
optimization problem through a hierarchical optimization network with an optimization represen-
tation bottleneck. This process enables denoising, information compression, and automatic feature
extraction, producing a learned optimization representation for subsequent symbolic discovery.
Behavior Learning backbone.OptLearner uses the Behavior Learning Network (BL) (Ma et al.,
2026b;a) as its backbone to learn a scalar landscape over context–outcome pairs. For each context
x and candidate outcome y, the network returns a score Sθ(x,y) that measures how strongly y is
preferred under the latent optimization problem. Under Eq. (3), observed outcomes are treated as
stochastic samples from the learned optimization landscape. Learning therefore reconstructs the
latent landscape on which observed outcomes arise as preferred solutions. This corresponds to the
representation-learning step in Figure 1 (a,b).
Optimization representation bottleneck.OptLearner builds on the BL backbone to represent
observational data as a single optimization problem. Its early layers denoise and compress the
observations, capturing interactions and latent features that may be difficult to express in the original
coordinates. The final layer consists of a single BL block, forming an optimization representation
bottleneck with learnable objective and optional constraint components, each potentially comprising
multiple branches,
max
y∈Y
U(x,y)| {z }
[λ0]
s.t.C(x,y)| {z }
[λ1]
≤0,T(x,y)| {z }
[λ2]
= 0.(4)
Here λ0 controls the scale of the objective, while λ1 and λ2 control the strengths of the inequality
and equality terms. This bottleneck provides a structured optimization representation for subsequent
symbolic discovery. When the input variables are already meaningful, OptLearner primarily denoises
the optimization landscape. For high-dimensional or unstructured inputs, it additionally extracts and
compresses relevant features before forming the learned optimization representation.
4

Data Space
 Latent Optimization Problem
Latent Optimization Network
Symbolic Form
Compression & Representation Symbolic Distillation

b
c
Real-world Observations Symbolic DiscoveryDenoised Representation
Optimization Learner
Optimization Discoverer
a
Figure 1:The OptScientist Model. a,The OptScientist Model consists of an Optimization Learner
and an Optimization Discoverer. The Optimization Learner learns to represent observational data as
an optimization problem using a hierarchical network with an optimization representation bottleneck.
The Optimization Discoverer then distills this learned optimization representation into a compact
symbolic optimization problem.b,The OptScientist Model represents the data manifold through a
latent optimization network. Raw observations are first compressed and represented by hierarchical
optimization blocks. The learned representations are then expressed as a single optimization problem
through the optimization representation bottleneck, from which a compact symbolic law is extracted.
c,The model follows the same logic in concrete discovery settings. Noisy real-world observations
are first transformed into denoised representations, and symbolic regression is then applied to the
learned optimization representation to recover symbolic laws.
Training objective.The training objective follows the same principle for discrete and continuous
outcomes. For a finite outcome set Y, OptLearner evaluates all candidates and trains the score by
cross-entropy,
Ldisc =− 1 N
NX
i=1
log exp(Sθ(xi,y i)/τ)P
y∈Y exp(Sθ(xi,y)/τ) .(5)
For continuous outcomes, enumerating Y is infeasible. OptLearner therefore compares the observed
outcome with sampled alternatives eyik using the same contrastive objective,
Lcont =− 1 N
NX
i=1
log exp(Sθ(xi,y i)/τ)
exp(Sθ(xi,y i)/τ) + PK k=1 exp(Sθ(xi, eyik)/τ) .(6)
5

Both losses encode the same principle: under the observed context, the observed outcome should
receive the highest optimization score.
3.2.2 Optimization Discoverer
The Optimization Learner represents observational data as an optimization problem, but the learned
representation is not yet a compact symbolic law. The Optimization Discoverer (OptDiscover)
addresses this by extracting the symbolic form of the learned optimization problem, as illustrated
in Figure 1 (a,b). After OptLearner is trained, its parameters are frozen. OptDiscover then distills
the components of the optimization representation bottleneck into compact symbolic expressions.
This bottleneck consists of three types of components: objective terms Uθ, inequality-constraint
terms Cθ, and equality-constraint terms Tθ, with each type optionally comprising multiple branches.
OptDiscover searches for a compact symbolic expression for each active component,
bHj = arg min F∈F Ωj
1
M
MX
m=1
[F(x m,y m)−H θ,j (xm,y m)]2 , H θ,j ∈ {Uθ, Cθ, Tθ}.(7)
Here FΩj denotes the symbolic search space for the j-th term. The distilled expressions of the
active components are assembled according to the learned optimization structure, yielding a symbolic
optimization problem with explicit objectives, inequality constraints, and equality constraints.
Optional automatic feature extraction.OptDiscover can operate with or without automatic feature
extraction. When the observed variables already form a meaningful symbolic language, the law is
distilled directly from (x,y) . When the raw variables require transformation, interaction, or com-
pression, OptLearner first maps them into denoised intermediate representations. Technically, these
representations are the outputs of intermediate layers in OptLearner, taken before the optimization
representation bottleneck. These layer-level variables act as automatically extracted features, and
OptDiscover then extracts the symbolic law on this learned feature space. This allows the framework
to handle both meaningful scientific variables and raw observations whose symbolic structure is more
naturally expressed after representation learning.
Complexity penalty.Symbolic complexity is measured by expression-tree size, with each variable,
numerical constant and operator counted as one node. OptDiscover controls symbolic complexity in
two ways. First, it selects the simplest expression among candidates with near-minimal distillation
loss. This favours parsimonious laws while preserving the learned optimization structure. Second,
for the objective term, OptDiscover removes additive components that depend only on x. These
components are constant across candidate outcomesyand therefore do not affect the optimizer.
3.3 OptScientist Agent
Research Orchestrator
Coordinates tools, state,
and the iterative research loop.
1 Theory Prior Agent 2 Experiment Agent 3 Scientific Critic & Theory Abstraction Agent
Refine the next round
Scientific
priors1
OptScientist
run
2
Model
adjudication1
Theory
abstraction2
New-data
suggestions3Model evaluation 3
Agentic
Search
1
Variable
proposals2
Mechanism
hypotheses3
Figure 2:OptScientist Agent as an iterative research
framework.The framework embeds the OptScientist
Model in a scientific-discovery loop.
Symbolic discovery often requires scien-
tific decisions both before and after model
fitting: researchers construct meaningful
variables, impose search priors, interpret
candidate expressions, abstract qualitative
mechanisms and decide how subsequent
analysis should be revised. To automate
this research loop, OptScientist Agent em-
beds the OptScientist Model in an iterative
framework for optimization-law discovery
(Figure 2). The system comprises four in-
teracting modules: a Research Orchestra-
tor, a Theory Prior Agent, an Experiment
Agent and a Scientific Critic and Theory
Abstraction Agent. A detailed description
of the OptScientist Agent is provided in
Appendix A.2.
Research Orchestrator.The Research Orchestrator maintains the shared research state and coor-
dinates the discovery process. It integrates hypotheses, candidate variables, discovered laws and
scientific findings across agents and discovery rounds, while carrying unresolved questions forward.
6

It also determines whether the workflow should terminate or enter another round of refinement,
turning OptScientist runs into an iterative scientific-discovery process.
Theory Prior Agent.The Theory Prior Agent draws on the scientific literature to identify established
theories and mechanisms relevant to the research question, and translates them into explicit, testable
hypotheses. It then proposes scientifically meaningful variables or transformations that represent
these mechanisms, together with symbolic-search priors when scientifically justified. These priors
guide the search while keeping the final expression data-driven.
Experiment Agent.Guided by the priors from the Theory Prior Agent, the Experiment Agent
translates scientific hypotheses, candidate variables and search priors into executable OptScientist
configurations. It then uses the core OptScientist Model to search for candidate optimization laws
from observational data. The resulting laws and supporting empirical evidence are returned for
scientific critique and theory abstraction.
Scientific Critic and Theory Abstraction Agent.The Scientific Critic and Theory Abstraction
Agent evaluates candidate laws as scientific explanations and identifies the best-supported structures
across them. It synthesizes the supported laws into a more general theoretical form and summarizes
their qualitative mechanisms and main scientific findings. Remaining uncertainty is then translated
into new hypotheses, variables or data requirements for the next discovery round, moving OptScientist
Agent from symbolic law recovery towards iterative theory refinement.
Embedding the OptScientist Model in the discovery loop.The OptScientist Model forms the
empirical core of the agentic system. In each round, scientific hypotheses, candidate variables
and search priors are translated into executable configurations, through which the model discovers
candidate optimization laws from observational data. The resulting laws and empirical evidence are
then returned to the agents for evaluation, theory abstraction and refinement of the next round.
4 Experiments
We evaluate OptScientist Model onOptFeynman, a new benchmark for optimization-law discov-
ery, and the full framework on two real-world scientific-discovery tasks, with comparisons against
machine-learning models, symbolic regression, and LLM model-discovery methods. The LLM base-
lines include an LLM-only researcher, GeCCo (Rmus et al., 2026) as a code-assisted LLM approach,
and Model Discovery Agent (MDA; Murphy, 2026) as a Bayesian experiment-design approach. All
LLM methods use DeepSeek-V4-Flash, the same LLM used by the optional OptScientist Agent. Data
and evaluation are provided in Sec. 5, and comparison methods in Appendix B.1.
4.1 Recovering Ground-Truth Optimization Laws
Table 1:Examples of recovered OptFeynman
laws.Examples show that OptScientist perfectly
recovers effective ground-truth optimization ex-
pressions across diverse physical structures.
Decision vari-
able
Effective ground truth Effective recovered expres-
sion
y3 maxy3 x3y3 maxy3 x3y3
wmax w w2 maxw w2
Ef max Ef Ef cosθmax Ef Ef cosθ
Gmax
G
G
 1
r2
−
1
r1

max
G
G(r1 −r 2)
r1r2
dmax
d
T2 −T 1
d
max
d
T2 −T 1
d
rmax r
1
r2 maxr
1
r2
dmax
d
1
d
max
d
1
d
We first tested whether OptScientist Model can
recover ground-truth optimization laws from
observations. OptFeynman converts analytic
physics equations into latent optimization prob-
lems and generates observations via Gibbs sam-
pling. Because the generating objective is
known, recovery can be evaluated directly on un-
seen test contexts by comparing the preference
order and Gibbs distribution of the recovered
and ground-truth laws.Notably, this experiment
evaluates only the OptScientist Model, without
any LLM assistance.
Ground-truth recovery on OptFeynman.
OptScientist shows the strongest out-of-sample
ability to recover the true optimization law
across both discrete and continuous decision
variables (Figure 3). For discrete decision vari-
ables, it achieves perfect exact-order recovery on 88/99 problems, indicating that the recovered
symbolic laws induce preference orders approximately equivalent to the ground-truth laws. For con-
7

a b
OptFeynman
I. Physics → Optimization Form
II. Gibbs Sampling → Observations
c
d
e
Figure 3:Recovering ground-truth optimization laws on OptFeynman. a,OptFeynman converts
analytic physics equations into latent optimization problems and generates observations by Gibbs
sampling from the induced landscapes.b,c,For discrete decision variables, OptScientist shows
the strongest out-of-sample ability to recover the true optimization law on unseen test contexts,
outperforming baselines. It achieves perfect exact-order recovery on 88/99 tasks, indicating that
the recovered symbolic laws induce preference orders approximately equivalent to the ground-truth
laws.d,e,For continuous decision variables, the advantage persists on unseen test contexts across
increasingly dense candidate sets. OptScientist perfectly recovers the exact order on 78/99 tasks
at K= 10 , K= 50 and K= 100 , showing robust discovery of the underlying optimization law
beyond discrete-choice settings. Error bars denote standard errors across datasets where shown.
8

a
b
c
Figure 4:Robust recovery of optimization laws under noisy context variables.Gaussian noise is
added to the training context variables, while validation and test contexts remain clean.a,For discrete
decision variables, OptScientist remains the strongest method for out-of-sample recovery of the true
optimization law, achieving perfect exact-order recovery on 92/99 tasks and outperforming machine-
learning, symbolic-regression, optimization-structured, and LLM-based automated model-discovery
baselines.b,c,For continuous decision variables, OptScientist retains high recovery performance on
unseen test contexts across K= 10 , K= 50 and K= 100 , perfectly recovering the exact order on
76/99 tasks at each candidate-set size and continuing to outperform the evaluated baselines. These
results show that the model can recover approximately equivalent ground-truth optimization laws
even when the training observations are corrupted by context noise. Error bars denote standard errors
across datasets where shown.
tinuous decision variables, OptScientist achieves perfect exact-order recovery on 78/99 problems at
K= 10,50,and100 . In both settings, OptScientist substantially outperforms all evaluated baselines.
The stability of performance across increasingly dense candidate sets shows robust discovery of the
underlying law. The recovered symbolic laws also preserve the stochastic structure of the generating
landscape, yielding Gibbs distributions close to the ground truth.
Robustness to noisy context variables.We next evaluated whether recovery remains reliable when
the training observations are corrupted by context noise (Figure 4). Specifically, Gaussian noise is
added to the training context variables, while validation and test contexts remain clean. Under this
setting, OptScientist remains the strongest method for out-of-sample recovery of the true optimization
law. It achieves perfect exact-order recovery on 92/99 discrete problems and on 76/99 continuous
problems at K= 10 , K= 50 and K= 100 . These results show that OptScientist can recover
9

approximately equivalent ground-truth optimization laws even when the training observations are
corrupted by context noise.
Representative recovered laws.Table 1 shows representative examples of successful symbolic
recovery. The comparison focuses on the decision-relevant part of each optimization law after
pruning numerical constants and scale factors that do not affect the optimizer. OptScientist recovers
diverse physical structures, including linear interactions, quadratic energy terms, inverse-square laws,
heat-transfer terms and algebraically equivalent rational forms. These examples illustrate that the
recovered laws preserve the optimization law up to choice-equivalent symbolic transformations.
4.2 Human Choice under Risk and Ambiguity
b
c

a
 Discovered Optimization Law
Three Qualitative Findings
Ⅰ  Choice follows immediate reward.
Ⅱ  Departing from a previous choice carries a cognitive cost.
Ⅲ  Forgone rewards shape future decisions.
Figure 5:A compact law of human decision-making under risk and ambiguity. a,A preliminary
analysis of the CPC18 repeated-choice task shows that decision-history variables are particularly
informative relative to lottery, demographic and framing variables, consistent with the sequential
structure of the discovered optimization law.b,OptScientist recovers this sequential structure as a
compact symbolic law: people tend to follow immediate reward, resist switching from a previous
choice and remain sensitive to forgone outcomes.c,Across behavioural baselines, machine-learning
models and OptScientist variants, the recovered law achieves the near-best predictive performance
with a near-minimal number of parameters. The result shows that human choice can be compressed
into a simple optimization principle rather than explained by model scale alone. Error bars denote the
standard error of the mean across participant-level metrics.
We next applied OptScientist to human decisions under risk and ambiguity, where the underlying
optimization law is unknown and human choices are shaped by repeated feedback, individual
heterogeneity and noisy behavioural responses. The CPC18 dataset asks participants to repeatedly
choose between two monetary prospects (Plonsky et al., 2019). This setting tests how OptScientist
turns behavioural data into a compact symbolic optimization law.
Theory-guided generation of supplementary variables.Guided by scientific literature, the Theory
Prior Agent constructs theoretically motivated variables beyond those in the original data, including
expected value, forgone payoffs, gender and residence in wealthier regions. These variables are then
considered in symbolic discovery. See Appendix B.3.2 for details.
A compact law of repeated choice.OptScientist recovered a compact symbolic optimization law
(Figure 5b). In abstract form, the discovered law is
max
yt∈{A,B}

V(x t, yt)−λ1(y t ̸=y t−1) +η Rcf t−1(yt) 	 .(8)
Here, V(x t, yt) is the current reward value of the candidate option, 1(yt ̸=y t−1) captures the
cognitive cost of switching from the previous choice, andRcf t−1(yt) captures sensitivity to the forgone
reward from the previous round. This law summarizes three qualitative mechanisms: choice follows
10

immediate reward, departing from a previous choice carries a cognitive cost, and forgone rewards
shape future decisions. In this case, our approach can be viewed as performing an automated resource-
rational analysis of human risky choices. The concrete score-difference expression and its mapping
to this abstract law are given in Additional Experimental Details, Appendix B.3.3.
Automatic-feature symbolic discovery.Following the feature-mediated design introduced in the
OptScientist Model, we also evaluated an automatic-feature variant, denoted AutoF OptScientist. In
this variant, OptLearner first maps (xt, yt) into denoised intermediate representations from its inner
layers. These layer-level variables act as automatically extracted features, and OptDiscover then
distills the final optimization score as a symbolic function on the learned feature space. This provides
an additional compact symbolic description of the CPC18 dataset and allows representation learning
to support symbolic discovery when behavioural variables are noisy, redundant or weakly structured.
See Appendix B.3.4 for the recovered inner-feature expression.
Near-best performance with near-minimal complexity.Across behavioural baselines, machine-
learning models and OptScientist variants, the recovered law achieves a favourable accuracy–
complexity trade-off (Figure 5c). The direct OptScientist law reaches 82.9% accuracy with five
numerical constants, approaching the strongest high-capacity machine-learning baselines that use
thousands of parameters. Notably, predictive performance on CPC18 appears to saturate at ap-
proximately 83% held-out accuracy across strong predictive models. AutoF OptScientist achieves
comparable ranking and calibration performance with seven numerical constants, including an AUC
of 0.865, a probability MSE of 0.137, and an ECE of 0.116. Full predictive metrics and complexity
definitions are reported in Additional Experimental Details, Appendix B.3.5. These results show that
repeated human choice in CPC18 can be compressed into a simple optimization principle combining
immediate reward, cognitive switching cost and counterfactual reward.
4.3 Central-Bank Monetary Policy
a
Ⅰ. Policy tracks a latent target through squared-error minimization.
Ⅱ. Macro strength tightens; financial fragility loosens.
  Ⅲ. Policy momentum persists, but overshooting is restrained.
b
Discovered Central-Bank Policy Law
Qualitative Findings
Figure 6:Discovery of a central-bank policy law. a,OptScientist recovers a compact symbolic
rule for quarterly monetary-policy decisions. The five-class policy stance, ranging from large easing
to large tightening, is explained as tracking a latent policy target driven by macroeconomic strength,
financial fragility, inherited tightness and policy momentum.b,On a future-period out-of-time test set,
OptScientist attains the best policy-stance and policy-direction accuracy while using a near-minimal
parameter count. Error bars denote bootstrap standard errors from 10,000 quarter-level resamples
with replacement.
11

We then applied OptScientist to quarterly central-bank monetary-policy decisions, where the observed
action is a five-class policy stance ranging from large easing to large tightening. The task is to
discover a compact optimization law linking macro-financial conditions to policy actions. This setting
tests how OptScientist recovers a symbolic policy rule from small, noisy and temporally structured
macroeconomic data.
Discovery of a central-bank optimization law.OptScientist recovers a compact symbolic optimiza-
tion law for monetary-policy decisions. For scientific interpretation, the selected law is abstracted
into a policy-target tracking form (see Figure 6a),
min
yt∈Y
(
yt − Nt 2κ 2 +ε t(yt) ) ,(9)
where yt is the policy stance, εt(yt) is a residual decision term and Nt/(2κ) is the latent subjective
target policy. The recovered net policy pressure isNt =m(g t +τt)−m(f t +qc t)−ρr t−1 +(s+ρ)∆ t.
The first term captures macroeconomic strength, the second captures financial fragility, the third
captures inherited policy tightness and the fourth captures policy momentum. The law therefore
explains quarterly policy as tracking a latent target: macroeconomic strength tightens policy, financial
fragility loosens policy, inherited tightness restrains further tightening, and policy momentum carries
previous adjustments forward. The full symbolic expression and the algebraic rewriting into the
target-tracking form are given in Additional Experimental Details, Appendix B.4.2 and B.4.3.
Constrained policy-law decomposition.OptScientist also recovers a constrained symbolic law
with explicit U, C and T components, decomposing the policy score into policy pressure, a one-
sided constraint and a quadratic risk or target-deviation term while retaining competitive predictive
performance. The full expression and branch-level complexities are reported in Appendix B.4.4.
Near-best performance with near-minimal complexity.Across baselines and OptScientist variants,
the single-U law achieves the best point estimates for exact and direction accuracy (Figure 6b),
reaching 78.6% and 85.7%, respectively, on the out-of-time test set with only 11 numerical parameters.
The constrained variant remains competitive at 71.4% and 78.6%, respectively, with the same
parameter count. Full metrics and complexity details are reported in Appendix B.4.5.
4.4 Token-Efficient Model Discovery
Figure 7:Token-efficient automated model discovery.We further compare the token efficiency
of OptScientist with three LLM-based automated model-discovery methods on the two real-world
discovery tasks: LLM-only discovery, GeCCo (code-assisted LLM), and MDA (Bayesian experiment
design). All LLM components use DeepSeek-V4-Flash.Left,On the central-bank monetary-
policy task (Sec. 4.3), OptScientist attains higher held-out policy-stance accuracy with substantially
lower output-token consumption.Right,On human decisions under risk and ambiguity (Sec. 4.2),
OptScientist reaches competitive held-out predictive accuracy with substantially fewer output tokens.
Across both domains, OptScientist achieves a favourable accuracy–token-efficiency trade-off.
We finally compared the token efficiency of OptScientist with three LLM baselines on the two
real-world discovery tasks in Secs. 4.2 and 4.3. All methods received the same research description,
12

variable information, and training data; for the LLM baselines, we evaluated four maximum output-
token settings and recorded held-out accuracy and cumulative output-token consumption.
Token efficiency.OptScientist achieves near-best held-out predictive performance with substantially
fewer LLM output tokens (Figure 7). On central-bank monetary-policy decisions, OptScientist
achieves 78.6% held-out policy-stance accuracy using 5,976 output tokens, exceeding the strongest
LLM-based baseline result of 70.5%, while the baselines consume approximately 16,700–29,600
tokens. On human decisions under risk and ambiguity, OptScientist approaches the apparent predictive
ceiling of approximately 83% held-out accuracy while using only 6,396 output tokens, compared
with approximately 15,800–45,800 tokens for the LLM baselines.
5 Data and Evaluation
5.1 The OptFeynman
Benchmark design.To evaluate whether OptScientist can recover symbolic optimization laws, we
constructOptFeynman, a benchmark derived from the AI Feynman equation collection (Udrescu
& Tegmark, 2020). The original benchmark asks whether a method can recover an input–output
equation. OptFeynman poses a different question: whether a method can recover the symbolic
optimization problem that generates observed outcomes. Each analytic equation is therefore treated as
a latent objective landscape, and the observed data are sampled as noisy outcomes of this landscape.
Optimization construction.For each multivariate Feynman equation, we separate its variables into
a contextxand a decision variabley. The original equation defines the ground-truth objective,
U(x, y) =f(x, y).
Single-variable equations are excluded because they do not define a context-dependent decision
problem, leaving 99 OptFeynman tasks. Context variables are sampled uniformly from the ranges
specified in the original Feynman benchmark. For each task, we generate a set of unique contexts and
partition them at the context level into training, validation and test sets. All stochastic outcomes gen-
erated from a given context are assigned to the same split. Thus, performance reflects generalization
across unseen x-contexts, with stochastic outcomes from each context kept entirely within one split.
Gibbs sampling.Observed outcomes are generated from the optimization landscape through Gibbs
sampling. In the discrete version, the decision variable is first discretized into five candidate actions
within its original range,
yk =y min +k ymax −y min K−1 , k= 0, . . . , K−1, K= 5.
For each context xi, the ground-truth objective is evaluated on these candidates. The resulting scores
are scaled by the standard deviation of the training objective values, estimated only from training
contexts, and converted into a Gibbs choice distribution,
P(y=k|x i) = exp(U(x i, yk)/(cT))PK−1
ℓ=0 exp(U(x i, yℓ)/(cT))
.
Observed labels are then sampled from this categorical distribution, with multiple labels drawn for
each context.
The continuous version follows the same principle, while keeping y continuous on its original
interval [ymin, ymax]. For each context, the target conditional density is defined by the exponentiated
objective,
p(y|x i)∝exp (U(x i, y)/(cT)), y∈[y min, ymax].
Because this density is not analytically tractable for arbitrary Feynman equations, it is approximated
on a dense grid over the decision interval. Grid points are assigned normalized Gibbs weights, a
grid point is sampled as the outcome, and the sampled value is optionally perturbed within its local
grid cell and clipped back to the valid interval. The continuous setting uses the same context-level
construction as the discrete setting, but draws a larger set of continuous outcomes from each context.
Thus, the same symbolic objective is instantiated either over a finite action set or over a continuous
decision interval.
13

Noisy-context version.We also construct a noisy-context version of OptFeynman. Starting from the
clean dataset, Gaussian noise is added only to the training contexts,
exij =x ij +ϵ ij, ϵ ij ∼ N(0, σ2 j ).
The default noise scale is one percent of the sampling range of each context variable. The validation
and test contexts remain clean, and the ground-truth objective, sampled outcomes, true scores, and
evaluation files are unchanged. This setting tests whether OptScientist can recover a stable underlying
law when the observations used for learning are corrupted by measurement noise.
Evaluation.Evaluation is based on the utility-representation view of optimization. By Debreu’s
continuous utility representation theorem, preferences can be represented by a utility function when
the preference relation is complete, transitive, and continuous (Debreu et al., 1953).
Theorem 5.1 (Continuous utility representation, Debreu) Let Z ⊆Rn, and let ⪰ be a complete,
transitive, and continuous preference relation on Z. Then there exists a continuous function u:Z →
Rsuch that, for allz 1, z2 ∈ Z,
z1 ⪰z 2 ⇐ ⇒u(z 1)≥u(z 2).
This result motivates our evaluation: an equivalent optimization problem should preserve the prefer-
ence structure induced by the latent objective, while also explaining its stochastic realizations. Since
OptFeynman provides the generating objective U(x, y), we evaluate whether the learned score and
the distilled symbolic score recover the same ordinal and probabilistic structure.
For each context xi, let Yi ={y i1, . . . , yiK} be the candidate outcome set. In discrete tasks, Yi
contains the five candidate actions; in continuous tasks, it contains sampled continuous candidates.
The ground-truth objective induces an ordered listπ i = (j1, . . . , jK),
U(x i, yij1 )≥U(x i, yij2 )≥ · · · ≥U(xi, yijK ),
with bπi defined analogously by the recovered score bS. Exact preference-order accuracy measures
whether bπi =π i, and pairwise accuracy measures whether each pairwise comparison has the same
direction under U and bS. These metrics test whether the recovered score represents the same
optimization problem up to order-preserving transformations.
Because the observations are generated by Gibbs sampling, we also evaluate the induced stochastic
landscape. For discrete tasks, the Gibbs distribution is computed over the five candidate actions. For
continuous tasks, it is approximated on a dense grid over the decision interval. We compare the true
and predicted distributions using KL divergence:
DKL(P∥ bP) = 1 N X i X y∈Yi P(y|x i) log P(y|x i) bP(y|x i) .
Together, preference recovery evaluates whether the discovered expression captures the equivalent
optimization law, while distribution recovery evaluates whether it also captures the stochastic strength
of the generating landscape.
5.2 Real-world Datasets
Synthetic benchmarks test recovery when the generating optimization law is known. Real-world
data test discovery under noise, redundancy and incomplete theoretical specification. We evaluate
OptScientist on two domains: human risky choice and central-bank monetary decisions.
Human decisions under risk and ambiguity.The first dataset is the Choice Prediction Competition
2018 (CPC18), a large-scale dataset of repeated human choices between monetary prospects under
risk and ambiguity (Plonsky et al., 2019). In each problem, a participant repeatedly chooses between
two options, A and B. The target variable is the observed binary choice, indicating whether option
B is selected. CPC18 contains several groups of variables. The main lottery variables describe the
objective choice environment, including outcomes, probabilities, ambiguity and correlation between
the two options. Identifier variables, such as participant and game identifiers, organize repeated
decisions across participants and problems. Framing variables describe how the choice problem and
feedback are presented. Demographic variables provide participant-level covariates. Because each
14

participant faces repeated decisions with feedback, we also construct history variables indicating
whether a previous round exists and which option was chosen in the previous round. This dataset tests
whether OptScientist can recover the optimization law behind human decisions under risk, ambiguity
and sequential feedback.
Central-bank monetary decisions.The second dataset studies central-bank monetary decisions from
quarterly macroeconomic and financial conditions. The outcome y is a five-class quarterly policy
stance, ranging from large easing to large tightening. We construct y from the quarter-to-quarter
change in the average federal funds target rate. Before 2008, the daily target rate is taken from the
single federal funds target-rate series. After 2008, it is computed as the midpoint of the target-rate
corridor. The daily target rate is averaged within each quarter, and the quarterly change is measured
in basis points. A decrease of at least 50 basis points is coded as −2, a decrease between 25 and 50
basis points as −1, a change within 25 basis points as 0, an increase between 25 and 50 basis points
as1, and an increase of at least 50 basis points as2.
The context x contains twelve quarterly macro-financial variables. These include PCE inflation,
core PCE inflation, unemployment and real GDP growth; two policy-inertia variables, given by the
previous average target rate and the previous quarterly target-rate change; three financial-market
variables, given by the Baa–Treasury credit spread, the 10-year–3-month term spread and the CBOE
V olatility Index (VIX); and three financial-stress measures, given by the St. Louis Fed Financial
Stress Index, the Chicago Fed National Financial Conditions Index and the Adjusted National
Financial Conditions Index. The period variable is retained for temporal indexing and data splitting.
This dataset tests whether OptScientist can recover a compact symbolic optimization law behind
macroeconomic policy decisions.
All policy-rate, macroeconomic and financial variables are obtained from Federal Reserve Economic
Data (FRED), maintained by the Federal Reserve Bank of St. Louis. The federal funds target-rate
series and target-range bounds are used to construct the policy outcome, while the macroeconomic,
financial-market and financial-stress variables are taken from their corresponding FRED series.
6 Conclusion and Limitations
We introduced OptScientist, a framework for automatically discovering compact symbolic optimiza-
tion laws from observational data. OptScientist combines a model that learns and distills latent
optimization structure with an agentic scientific-discovery system that incorporates theoretical priors,
searches for candidate laws, evaluates empirical evidence, and abstracts supported mechanisms.
On OptFeynman, OptScientist recovers ground-truth optimization laws across a broad range of
physics-derived problems, substantially outperforms all evaluated baselines, and remains robust to
noisy contextual information. Applied to human risky choice and central-bank monetary policy, it
discovers interpretable optimization laws with competitive or stronger held-out predictive perfor-
mance and compact symbolic representations. On the two real-world tasks, OptScientist also uses
substantially fewer output tokens than LLM-based automated model-discovery approaches. These
results establish symbolic optimization-law discovery as a new direction for automated scientific
discovery and provide a general framework for learning compact optimization principles underlying
observed phenomena.
Limitations and Future Research.When the structure of ground-truth models deviates substantially
from an optimization formulation, our approach is likely to fail. Although, mathematically, a broad
class of laws not originally formulated as optimization problems can be represented in optimization
form, the OptFeynman results show that OptScientist can recover the original laws from such
representations. Future research is needed to characterize the limits of the optimization assumption
and identify the classes of models that remain discoverable within a feasible computational budget.
15

References
Sydney N Afriat. The construction of utility functions from expenditure data.International economic
review, 8(1):67–77, 1967.
Mayank Agrawal, Joshua C Peterson, and Thomas L Griffiths. Scaling up psychology via scientific
regret minimization.Proceedings of the National Academy of Sciences, 117(16):8825–8835, 2020.
Ravindra K Ahuja and James B Orlin. Inverse optimization.Operations research, 49(5):771–783,
2001.
John R Anderson. The adaptive nature of human categorization.Psychological Review, 98(3):409,
1991.
Anil Aswani, Zuo-Jun Shen, and Auyon Siddiq. Inverse optimization with noisy data.Operations
Research, 66(3):870–892, 2018.
Eser Aygün, Anastasiya Belyaeva, Gheorghe Comanici, Marc Coram, Hao Cui, Jake Garrison, Renee
Johnston, Anton Kast, Cory Y McLean, Peter Norgaard, et al. An ai system to help scientists write
expert-level empirical software.Nature, pp. 1–3, 2026.
Pierre Baldi, Peter Sadowski, and Daniel Whiteson. Searching for exotic particles in high-energy
physics with deep learning.Nature communications, 5(1):4308, 2014.
Marcel Binz, Akshay Kumar Jagadish, Milena Rmus, and Eric Schulz. Automated scientific mini-
mization of regret for cognitive modeling. InNeurIPS 2025 AI for Science Workshop, 2025.
Leo Breiman. Random forests.Machine learning, 45(1):5–32, 2001.
Steven L Brunton, Joshua L Proctor, and J Nathan Kutz. Discovering governing equations from data
by sparse identification of nonlinear dynamical systems.Proceedings of the national academy of
sciences, 113(15):3932–3937, 2016.
Giuseppe Carleo and Matthias Troyer. Solving the quantum many-body problem with artificial neural
networks.Science, 355(6325):602–606, 2017.
Kathleen Champion, Bethany Lusch, J Nathan Kutz, and Steven L Brunton. Data-driven discovery of
coordinates and governing equations.Proceedings of the National Academy of Sciences, 116(45):
22445–22451, 2019.
Ricky TQ Chen, Yulia Rubanova, Jesse Bettencourt, and David K Duvenaud. Neural ordinary
differential equations.Advances in neural information processing systems, 31, 2018.
Tianqi Chen and Carlos Guestrin. Xgboost: A scalable tree boosting system. InProceedings of the
22nd acm sigkdd international conference on knowledge discovery and data mining, pp. 785–794,
2016.
David R Cox. The regression analysis of binary sequences.Journal of the Royal Statistical Society
Series B: Statistical Methodology, 20(2):215–232, 1958.
Miles Cranmer. Interpretable machine learning for science with pysr and symbolicregression. jl.
arXiv preprint arXiv:2305.01582, 2023.
Miles Cranmer, Alvaro Sanchez Gonzalez, Peter Battaglia, Rui Xu, Kyle Cranmer, David Spergel,
and Shirley Ho. Discovering symbolic models from deep learning with inductive biases.Advances
in neural information processing systems, 33:17429–17442, 2020.
Gerard Debreu.Theory of value: An axiomatic analysis of economic equilibrium, volume 17. Yale
University Press, 1959.
Gerard Debreu et al.Representation of a preference ordering by a numerical function. Yale University,
1953.
Mengge Du, Yuntian Chen, Zhongzheng Wang, Longfeng Nie, and Dongxiao Zhang. Llm4ed: Large
language models for automatic equation discovery.arXiv preprint arXiv:2405.07761, 2024.
16

Noémi Éltet˝o, Nathaniel D Daw, Kimberly L Stachenfeld, and Kevin J Miller. Atlas: Active theory
learning for automated science.arXiv preprint arXiv:2606.12386, 2026.
Ronald Aylmer Fisher.The genetical theory of natural selection: a complete variorum edition.
Oxford University Press, 1999.
Jerome H Friedman. Greedy function approximation: a gradient boosting machine.Annals of
statistics, pp. 1189–1232, 2001.
Josiah Willard Gibbs.Elementary principles in statistical mechanics: developed with especial
reference to the rational foundations of thermodynamics. C. Scribner’s sons, 1902.
Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Petar Sirkovic, Artiom Myaskovsky,
Grzegorz Glowaty, Felix Weissenberger, Alessio Orlandi, Dan Popovici, et al. Accelerating
scientific discovery with co-scientist.Nature, pp. 1–3, 2026.
S-P Han and Olvi L Mangasarian. Exact penalty functions in nonlinear programming.Mathematical
programming, 17(1):251–269, 1979.
Akshay K Jagadish, Younes Strittmatter, Nori Jacoby, George Kachergis, Eric Schulz, Nathaniel
Daw, Suyog H Chandramouli, and Thomas L Griffiths. Closing the loop to discover psychological
theories with an automated cognitive scientist.arXiv preprint arXiv:2606.26448, 2026.
Li Ji-An, Marcus K Benna, and Marcelo G Mattar. Discovering cognitive strategies with tiny recurrent
neural networks.Nature, 644(8078):993–1001, 2025.
John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger,
Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko, et al. Highly accurate
protein structure prediction with alphafold.nature, 596(7873):583–589, 2021.
Michal Kosinski, David Stillwell, and Thore Graepel. Private traits and attributes are predictable
from digital records of human behavior.Proceedings of the national academy of sciences, 110(15):
5802–5805, 2013.
John R Koza. Genetic programming as a means for programming computers by natural selection.
Statistics and computing, 4(2):87–112, 1994.
Lev Davidovich Landau and Evgenii Mikhailovich Lifshitz.Course of theoretical physics. Elsevier,
2013.
Yann LeCun, Sumit Chopra, Raia Hadsell, M Ranzato, Fujie Huang, et al. A tutorial on energy-based
learning.Predicting structured data, 1(0), 2006.
Falk Lieder and Thomas L Griffiths. Resource-rational analysis: Understanding human cognition as
the optimal use of limited computational resources.Behavioral and brain sciences, 43:e1, 2020.
Ziming Liu, Yixuan Wang, Sachin Vaidya, Fabian Ruehle, James Halverson, Marin Soljacic, Thomas
Hou, and Max Tegmark. Kan: Kolmogorov–arnold networks. InInternational conference on
learning representations, volume 2025, pp. 70367–70413, 2025.
Lars Ljungqvist and Thomas J Sargent.Recursive macroeconomic theory. MIT press, 2018.
Chris Lu, Cong Lu, Robert Tjarko Lange, Yutaro Yamada, Shengran Hu, Jakob Foerster, David Ha,
and Jeff Clune. Towards end-to-end automation of ai research.Nature, 651(8107):914–919, 2026.
Zhenyao Ma, Yue Liang, and Dongxu Li. Behavior learning (bl): Learning hierarchical optimization
structures from data.arXiv preprint arXiv:2602.20152, 2026a.
Zhenyao Ma, Yue Liang, and Dongxu Li. Behavior learning (BL). InInternational Conference on
Learning Representations, volume 2026, pp. 115378–115425, 2026b.
Matteo Merler, Katsiaryna Haitsiukevich, Nicola Dainese, and Pekka Marttinen. In-context symbolic
regression: Leveraging large language models for function discovery. InProceedings of the 62nd
Annual Meeting of the Association for Computational Linguistics (V olume 4: Student Research
Workshop), pp. 427–444, 2024.
17

Kevin Miller, Maria Eckstein, Matt Botvinick, and Zeb Kurth-Nelson. Cognitive model discovery via
disentangled rnns.Advances in Neural Information Processing Systems, 36:61377–61394, 2023.
Kevin Murphy. Model discovery agent: Llm-assisted bayesian experiment design for data-efficient
discovery of mechanistic world models.arXiv preprint arXiv:2608.09696, 2026.
Andrew Y Ng, Stuart Russell, et al. Algorithms for inverse reinforcement learning. InIcml, volume 1,
pp. 2, 2000.
Joshua C Peterson, David D Bourgin, Mayank Agrawal, Daniel Reichman, and Thomas L Griffiths.
Using large-scale experiments and machine learning to discover theories of human decision-making.
Science, 372(6547):1209–1214, 2021.
Ori Plonsky, Ido Erev, and Eyal Ert. All raw data for cpc18: Choice prediction competition 2018.
Zenodo, 2019. Dataset.
Ryan Poplin, Pi-Chuan Chang, David Alexander, Scott Schwartz, Thomas Colthurst, Alexander
Ku, Dan Newburger, Jojo Dijamco, Nam Nguyen, Pegah T Afshar, et al. A universal snp and
small-indel variant caller using deep neural networks.Nature biotechnology, 36(10):983–987,
2018.
Maziar Raissi, Paris Perdikaris, and George E Karniadakis. Physics-informed neural networks: A
deep learning framework for solving forward and inverse problems involving nonlinear partial
differential equations.Journal of Computational physics, 378:686–707, 2019.
Frank Plumpton Ramsey. A mathematical theory of saving.The economic journal, 38(152):543–559,
1928.
Milena Rmus, Akshay Kumar Jagadish, Marvin Mathony, Tobias Ludwig, and Eric Schulz. Generat-
ing computational cognitive models using large language models.Advances in Neural Information
Processing Systems, 38:87796–87833, 2026.
Samuel H Rudy, Steven L Brunton, Joshua L Proctor, and J Nathan Kutz. Data-driven discovery of
partial differential equations.Science advances, 3(4):e1602614, 2017.
David E Rumelhart, Geoffrey E Hinton, and Ronald J Williams. Learning representations by
back-propagating errors.nature, 323(6088):533–536, 1986.
Paul Anthony Samuelson. Foundations of economic analysis.Science and Society, 13(1), 1948.
Michael Schmidt and Hod Lipson. Distilling free-form natural laws from experimental data.science,
324(5923):81–85, 2009.
Parshin Shojaee, Kazem Meidani, Shashank Gupta, Amir Barati Farimani, and Chandan Reddy. Llm-
sr: Scientific equation discovery via programming with large language models. InInternational
Conference on Learning Representations, volume 2025, pp. 16054–16085, 2025.
Silviu-Marian Udrescu and Max Tegmark. Ai feynman: A physics-inspired method for symbolic
regression.Science advances, 6(16):eaay2631, 2020.
Hal R Varian. The nonparametric approach to demand analysis.Econometrica: Journal of the
Econometric Society, pp. 945–973, 1982.
Sewall Wright et al. The roles of mutation, inbreeding, crossbreeding, and selection in evolution.
1932.
Anyi Xu, Bangcai Lin, Bing Xue, Bingxuan Wang, Bingzheng Xu, Bochao Wu, Bowei Zhang,
Chaofan Lin, Chen Dong, Chenchen Ling, et al. Deepseek-v4: Towards highly efficient million-
token context intelligence.arXiv preprint arXiv:2606.19348, 2026.
Yibo Zhao, Yang Zhao, Hongru Du, and Hao Frank Yang. Personalized decision modeling: Utility
optimization or textualized-symbolic reasoning.Advances in Neural Information Processing
Systems, 38:89317–89364, 2026.
18

Jian-Qiao Zhu and Thomas L Griffiths. Computation-limited Bayesian updating: A resource-rational
analysis of approximate bayesian inference.Psychological Review, 133(3):619, 2026.
Jian-Qiao Zhu, Joshua C Peterson, Benjamin Enke, and Thomas L Griffiths. Capturing the complexity
of human strategic decision-making with machine learning.Nature Human Behaviour, 9(10):
2114–2120, 2025.
Brian D Ziebart, Andrew L Maas, J Andrew Bagnell, Anind K Dey, et al. Maximum entropy inverse
reinforcement learning. InAaai, volume 8, pp. 1433–1438. Chicago, IL, USA, 2008.
19

Appendix Contents
A Additional Architecture Details 21
A.1 OptScientist Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
A.2 OptScientist Agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
B Additional Experimental Details 30
B.1 Baselines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
B.2 OptFeynman Ground-Truth Recovery . . . . . . . . . . . . . . . . . . . . . . . . 30
B.3 Human Choice under Risk and Ambiguity . . . . . . . . . . . . . . . . . . . . . . 36
B.3.1 Dataset and evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
B.3.2 Theory Prior Agent and variable discovery . . . . . . . . . . . . . . . . . 36
B.3.3 Direct symbolic law . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
B.3.4 Automatic-feature symbolic law . . . . . . . . . . . . . . . . . . . . . . . 37
B.3.5 Predictive performance and complexity . . . . . . . . . . . . . . . . . . . 37
B.4 Central-Bank Monetary Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
B.4.1 Dataset and evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
B.4.2 Single-Usymbolic law . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
B.4.3 Rewriting the symbolic law into target-tracking form . . . . . . . . . . . . 38
B.4.4 ConstrainedU/C/Tsymbolic law . . . . . . . . . . . . . . . . . . . . . . 39
B.4.5 Predictive performance and complexity . . . . . . . . . . . . . . . . . . . 40
B.5 Token-Efficient Model Discovery . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
20

A Additional Architecture Details
A.1 OptScientist Model
The OptScientist Model implements the two-stage discovery procedure introduced in Sec. 3.2. The
Optimization Learner (OptLearner) first learns to represent observational data as an optimization
problem, and the Optimization Discoverer (OptDiscover) subsequently extracts its symbolic form.
The discrete- and continuous-outcome implementations share the same model architecture, optimiza-
tion procedure, validation protocol, and symbolic-distillation pipeline. They differ primarily in how
candidate decisions are constructed for the OptLearner training objective.
Algorithm 1OptScientist Model
Require: Training data Dtrain, validation data Dval, decision domain Y, outcome type r∈
{discrete,continuous}, OptLearner configurationM, symbolic search spacesΩ
Ensure:Symbolic optimization law bL
1:Initialize OptLearnerS θ(x, y)fromM
2:Initialize best validation lossℓ ∗ ← ∞
3:fore= 1, . . . , Emax do
4:forminibatchB ⊂ D train do
5:foreach(x i, yi)∈ Bdo
6:ifr= discretethen
7:A i ← Y▷enumerate all feasible decisions
8:else
9:Sampleey i1, . . . ,eyiK ∼Unif(Y)
10:A i ← {yi,eyi1, . . . ,eyiK}
11:end if
12:end for
13:Compute
L=− 1 |B| X i∈B log exp(Sθ(xi, yi)/τ)P y∈Ai exp(Sθ(xi, y)/τ)
14:Updateθusing AdamW
15:end for
16:Evaluate validation lossℓ val
17:ifℓ val < ℓ∗ then
18:Save OptLearner checkpoint
19:ℓ ∗ ←ℓ val
20:Reset early-stopping counter
21:else
22:Increment early-stopping counter
23:end if
24:ifearly-stopping patience is reachedthen
25:break
26:end if
27:end for
28:Restore the checkpoint with lowest validation loss
29:Freeze OptLearner
30:Construct symbolic-distillation samplesD distill
31:foreach active componentH θ,j ∈ {Uθ, Cθ, Tθ}do
32:EvaluateH θ,j onD distill
33:SearchF Ωj for symbolic approximations ofH θ,j
34:Retain the simplest expression with near-minimal distillation loss
35:end for
36:Remove additivex-only terms from the distilled objective
37:Assemble the retained components according to the learned optimization structure
38:return bL
21

OptLearner architecture.OptLearner uses the Behavior Learning Network (BL) as its backbone
to learn a scalar optimization landscape over context–outcome pairs. For each contextx and candidate
outcome y, the network returns a score Sθ(x, y)that measures how strongly y is preferred under the
latent optimization problem.
Building on the BL backbone, OptLearner represents observational data as a single optimization
problem. Its early layers denoise and compress observations, capturing interactions and latent
features that may be difficult to express in the original coordinates. The final layer consists of a single
BL block, forming an optimization representation bottleneck with learnable objective and optional
constraint components, each potentially comprising multiple branches,
max
y∈Y
Uθ(x, y)| {z }
[λ0]
s.t. C θ(x, y)| {z }
[λ1]
≤0, T θ(x, y)| {z }
[λ2]
= 0.(10)
Here λ0 controls the scale of the objective, while λ1 and λ2 control the strengths of the inequality
and equality terms. This bottleneck provides a structured optimization representation for subsequent
symbolic discovery. When the input variables are already meaningful, OptLearner primarily denoises
the optimization landscape. For high-dimensional or weakly structured inputs, it additionally extracts
and compresses relevant features before forming the learned optimization representation.
In the default implementation, OptLearner contains two BL layers with widths[128,1] . The first layer
uses one U branch and one C branch, and the default final block contains a single U branch. This
configuration provides the default single-objective form used in the main OptFeynman experiments.
Task-specific configurations can additionally activate C and T in the final block, as in the constrained
OptScientist variants used in our experiments.
Unified learning objective.The discrete and continuous implementations can be written using
the same candidate-ranking objective. For observation (xi, yi), let Ai denote the set of candidate
decisions considered during that training step. OptLearner minimizes
LOptLearner =− 1 N
NX
i=1
log exp(Sθ(xi, yi)/τ)P
y∈Ai exp(Sθ(xi, y)/τ).(11)
For discrete outcomes, Ai =Y and the model evaluates the complete finite decision set, giving
the cross-entropy objective in Eq. (11). For continuous outcomes, OptLearner constructs a sampled
candidate set,
Ai ={y i,eyi1, . . . ,eyiK},ey ik ∼Unif(Y),(12)
where the observed outcome is compared with K alternatives sampled uniformly from the feasible
decision range. This gives the sampled contrastive Gibbs objective in Eq. (6). Both settings therefore
train the same latent optimization score by assigning higher scores to observed outcomes than to
feasible alternatives under the same context.
OptLearner is optimized on the training split and selected using validation loss. The best checkpoint
is updated whenever validation loss improves. Training terminates after the specified number of
consecutive epochs without validation improvement or when the maximum number of epochs is
reached. The checkpoint with the lowest validation loss is then restored and frozen before symbolic
discovery.
OptDiscover implementation.After OptLearner is trained, its parameters are frozen. OptDiscover
extracts the symbolic form of the learned optimization problem by distilling the components of the
optimization representation bottleneck. For each active component
Hθ,j ∈ {Uθ, Cθ, Tθ},
the model generates a distillation dataset over context–decision pairs and records the corresponding
learned component values. Symbolic regression then searches for an expression
bHj = arg min F∈F Ωj
1
M
MX
m=1
[F(x m, ym)−H θ,j (xm, ym)]2 ,(13)
whereF Ωj denotes the symbolic search space for thej-th component.
22

Table 2:Default OptScientist Model hyperparameters.The discrete and continuous imple-
mentations use the same OptLearner architecture and training procedure, with different candidate
construction for the learning objective. Symbolic operators are task-dependent; the table reports the
default base language, and additional binary or unary operators can be introduced when required
by the discovery problem. The default final block contains a single objective component U, while
task-specific configurations can additionally activateCandTcomponents.
Hyperparameter Discrete Continuous
OptLearner architecture
Number of BL layers 2 2
BL layer widths[128,1] [128,1]
Hidden-layer(U, C, T)branches(1,1,0) (1,1,0)
Default final-layer(U, C, T)branches(1,0,0) (1,0,0)
Uactivation Identity Identity
Cactivation ReLU ReLU
Output-head bias Yes Yes
Decision encoding Scalar Scalar
OptLearner training
Learning objective Cross-entropy Sampled contrastive Gibbs
Contrastive alternativesK– 32
Temperatureτ1.0 1.0
Alternative-decision sampling – Uniform over feasible range
Optimizer AdamW AdamW
Learning rate2×10 −3 2×10 −3
Weight decay10 −5 10−5
Batch size 128 128
Maximum epochs 480 480
Early-stopping patience 25 25
Random seed 42 42
Model-selection criterion Validation loss Validation loss
OptDiscover symbolic distillation
Active final components Task-dependent; defaultUTask-dependent; defaultU
Distillation target Activated component output Activated component output
Binary operators Task-dependent; default{+,−,×}Task-dependent; default{+,−,×}
Unary operators Task-dependent Task-dependent
Symbolic-search iterations 200 200
Maximum expression size 24 24
Distillation samples 1,000 800
Simplicity tolerance 0.042 0.05
Model-selection rule Best Best
The symbolic language Ωj is task-dependent. We use a compact base operator set by default, and
additional binary or unary operators can be introduced when required by the scientific problem or by
explicit search priors. This design allows the symbolic hypothesis space to reflect the mathematical
structure of each discovery task.
Symbolic search is performed separately for the active components of the optimization representation
bottleneck. The resulting expressions are assembled according to the learned optimization structure,
yielding a compact symbolic optimization problem with an explicit objective and optional constraints.
Among expressions with near-minimal distillation loss, OptDiscover selects the expression with
the lowest effective symbolic complexity. For the objective component, additive terms that depend
only on x are subsequently removed because they remain constant across candidate decisions and
therefore do not affect the optimizer. The retained symbolic components define the final discovered
optimization law.
Algorithm 1 summarizes the common implementation for discrete and continuous outcomes.
Implementation and hyperparameters.Table 2 reports the default implementation settings used
in our experiments. These values specify the base OptLearner and OptDiscover configuration. The
active U/C/T structure and symbolic operator language can vary across task-specific configurations.
The operator entries in the table report the default symbolic search language.
23

The symbolic-search settings provide a base configuration that can be adapted to the scientific structure
of each task. In particular, Ω can be expanded with task-relevant operators before OptDiscover is
executed. This allows the OptLearner architecture to remain common across tasks while the symbolic
hypothesis space adapts to each scientific domain.








/RVVUHODWLYHWRLQLWLDOL]DWLRQ
&RQWLQXRXV2SW)H\QPDQ









&RQWLQXRXV1RLV\FRQWH[W2SW)H\QPDQ
     
1RUPDOL]HGWUDLQLQJSURJUHVV




/RVVUHODWLYHWRLQLWLDOL]DWLRQ
'LVFUHWH2SW)H\QPDQ
     
1RUPDOL]HGWUDLQLQJSURJUHVV









'LVFUHWH1RLV\FRQWH[W2SW)H\QPDQ
7UDLQLQJORVV 7UDLQLQJ,45 9 DOLGDWLRQORVV 9 DOLGDWLRQ,45
Figure 8:OptLearner learning curves on OptFeynman.Training and validation losses for
continuous and discrete OptFeynman tasks, with and without noisy context variables. Loss is the
OptLearner objective defined in the main text: Lcont for continuous outcomes and Ldisc for discrete
outcomes. For each task, losses are normalized by their values at the first epoch, and training progress
is normalized from the first epoch to the epoch selected by validation-based early stopping. Curves
show the median across tasks and shaded regions show the interquartile range.
A.2 OptScientist Agent
The OptScientist Agent implements the iterative scientific-discovery process introduced in Sec. 3.3.
A Research Orchestrator maintains the research state and coordinates three specialized agents: a
Theory Prior Agent, an Experiment Agent, and a Scientific Critic and Theory Abstraction Agent.
Together, these components connect scientific reasoning with model training, symbolic discovery
and empirical evaluation, allowing candidate optimization laws to be progressively proposed, tested,
adjudicated and abstracted.
The architecture is organized around a shared research state that accumulates information across dis-
covery rounds. This state contains the research question, variable definitions, theoretical hypotheses,
fixed data split, search configurations, discovered symbolic laws, evaluation results and unresolved
scientific questions. Maintaining these elements in a common state allows later stages to trace each
candidate law back to the assumptions, variables and empirical evidence that produced it. It also
enables the system to preserve informative failures: unstable symbolic structures, weakly supported
mechanisms and missing explanatory variables can directly shape the next round of discovery.
Each specialized agent operates on a role-specific view of this state and returns structured outputs
to the Research Orchestrator. Scientific priors therefore enter the workflow as explicit hypotheses
and search constraints; empirical results enter through executed OptScientist runs; and scientific
interpretations are formed from the accumulated evidence across candidate laws.
Embedding the OptScientist Model in the discovery loop.The OptScientist Model forms the
empirical core of the agentic discovery system. In each discovery round, the Theory Prior Agent
converts scientific knowledge into a structured set of candidate hypotheses, variables and search
priors. These outputs can include newly constructed variables, transformations of observed variables,
24

Scientific
proposal
hypotheses
variables
transformations
symbolic priors
− →
Experiment Agent
Vk: variables
Mk: model
Θk: parameters
Ωk: symbolic space
− →
OptScientist
Model
OptLearner
↓
OptDiscover
Scientific
refinement
revise variables, priors,
configurations or data
← −
Scientific Critic
adjudication
theory abstraction
mechanism findings
← −
Evidence package
candidate law
validation, complexity,
fidelity and stability
Figure 9:Embedding the OptScientist Model in the agentic discovery loop.The Theory Prior
Agent produces scientific hypotheses, candidate variables and symbolic priors. The Experiment
Agent combines these proposals with model and search parameters into executable configurationsQk.
Each configuration is passed through OptLearner and OptDiscover to produce candidate symbolic
optimization laws and associated empirical evidence. The Scientific Critic evaluates this evidence,
abstracts the supported laws into a more general theoretical form and qualitative mechanisms, and
returns refinements that can modify the variables, priors, model configurations or data used in the
next discovery round.
candidate mechanisms, preferred symbolic operators and restrictions on admissible functional forms.
The Experiment Agent combines these proposals with model and training parameters to construct a
bounded set of executable OptScientist runs.
Concretely, each run is represented by a configuration
Qk = (Vk,M k,Θ k,Ω k),
where Vk denotes the observed and theory-derived variables supplied to the model, Mk specifies
the OptScientist representation to be fitted, Θk contains the corresponding model, training and
search parameters, and Ωk defines the symbolic language used for distillation. For example, a prior
analysis of the data informed by the scientific literature may suggest an expected-reward variable or a
particular interaction between observed quantities. The Experiment Agent adds these variables to the
corresponding model input, assigns an OptLearner architecture and training configuration, specifies
the operators available to OptDiscover, and submits the resulting configuration as an OptScientist run.
Different hypotheses, variable sets or parameter settings can therefore generate complementary runs
within the same discovery round.
Figure 9 summarizes this interface. Scientific proposals are first converted into executable config-
urations. These configurations are passed to the OptScientist Model, which learns an optimization
representation and distills it into symbolic laws. The resulting laws and their empirical evidence are
then returned to the research state for scientific adjudication and refinement.
Each configuration is evaluated using the two-stage OptScientist Model introduced in Sec. 3.2. Given
the training data restricted to the variables inV k, OptLearner fits a scalar optimization landscape,
Sθk =OPTLEARNER(D train[Vk],M k,Θ k).
The learned hierarchy can denoise observations, compress redundant information, or construct in-
termediate representations, which are then expressed as a single optimization problem through the
optimization representation bottleneck. The fitted model therefore provides a data-driven representa-
tion of how candidate outcomes are ranked under the observed contexts.
After training, the OptLearner parameters are frozen. OptDiscover receives the learned optimization
representation together with the symbolic specification Ωk and distills its components into compact
symbolic expressions,
Lk =OPTDISCOVER(S θk ,Ω k).
For a single-objective configuration, this procedure distills the learned objective directly. For a
constrained configuration, the objective, inequality-constraint and equality-constraint components
are distilled separately and then assembled according to the learned optimization structure. The
25

symbolic-search specification controls the admissible operators and functional forms, while the
distillation loss and complexity criterion determine which candidate expressions are retained.
The Experiment Agent collects the output of every successful run as an evidence package,
Ek =

validation performance,symbolic complexity,
distillation fidelity,run stability,execution record

.
The pair (Lk,E k) is written back to the shared research state. Repeated symbolic searches can
contribute several low-complexity expressions with near-optimal distillation loss, allowing alternative
structures to remain available when the data do not identify a unique symbolic form. The resulting
candidate set therefore records both the discovered mathematical expressions and the evidence
supporting each expression.
The Scientific Critic and Theory Abstraction Agent receives these candidate laws together with their
evidence records and the hypotheses that generated the corresponding runs. It compares candidates
using predictive performance, symbolic complexity, fidelity to the learned optimization landscape
and stability across repeated searches, and identifies the laws and mathematical structures that receive
the strongest empirical support. It then abstracts these supported structures into a more general
theoretical form and summarizes the corresponding qualitative mechanisms and scientific findings.
The exact candidate expressions are retained alongside this abstraction, preserving the connection
between the empirical laws and the higher-level theory derived from them.
Remaining uncertainty is translated into concrete modifications of the next discovery round. These
may include introducing a new theoretically motivated variable, removing a redundant representation,
changing the symbolic operator set, evaluating an alternative OptScientist configuration or request-
ing additional observations. The resulting theory abstraction, mechanism findings and refinement
proposals are written back to the shared research state and used to define the subsequent round of
discovery.
This interface creates a direct path from scientific reasoning to model execution and back to scientific
interpretation. Theory-guided variables, hypotheses and search priors are compiled by the Experiment
Agent into explicit OptScientist configurations; OptLearner and OptDiscover recover candidate
optimization laws from the data; and the resulting evidence is evaluated by the Scientific Critic
and Theory Abstraction Agent. The supported laws are then adjudicated, abstracted into a more
general theoretical form and summarized as qualitative mechanisms and scientific findings. These
conclusions, together with the remaining uncertainties, determine how the subsequent discovery
round is refined.
Algorithm 2 makes this interface explicit.
Research Orchestrator.The Research Orchestrator provides the control layer of the discovery pro-
cess. It maintains the shared research state, coordinates information transfer among agents, manages
the search budget and determines whether another discovery round is needed. The state records
theoretical hypotheses, accepted variables, model configurations, discovered symbolic expressions,
their empirical evaluations, theory abstractions and qualitative findings, creating a persistent scientific
record across successive rounds.
This persistent state also provides continuity between scientific reasoning and empirical search. A
hypothesis proposed early in the workflow remains associated with the variables introduced to test
it, the model configurations used during discovery and the evidence obtained from the resulting
symbolic laws. Similarly, unresolved mechanisms identified by the Scientific Critic can be translated
into explicit requests for additional variables, alternative transformations or further model searches.
The Orchestrator therefore allows the discovery process to accumulate evidence over time while
preserving the provenance of intermediate scientific decisions.
Importantly, the Orchestrator also preserves the boundary between scientific reasoning and model
execution. Agent outputs that define hypotheses, variables or search priors are converted into
explicit OptScientist configurations before model fitting. Conversely, outputs from OptLearner
and OptDiscover enter subsequent agent reasoning only through recorded candidate laws and their
associated empirical evidence. This separation makes it possible to distinguish structures proposed
as theoretical priors from structures that are subsequently supported by model fitting and symbolic
discovery.
26

Algorithm 2OptScientist Agent
Require:Observational dataD, research questionq, decision variabley, search budgetB
Ensure: Supported symbolic optimization laws L∗ and scientific abstraction with qualitative mecha-
nismsA ∗
1:Initialize shared research stateS
2:Fix training and validation splitsD train,D val
3:whilediscovery continuesdo
4:(H,V,Ω)←THEORYPRIORAGENT(S)▷hypotheses, variables, and search priors
5:Validate proposed variablesV
6:UpdateSwith accepted hypotheses and variables
7:Q ←EXPERIMENTAGENT(S,H,V,Ω,B)▷executable OptScientist configurations
8:Initialize candidate-evidence setC ←∅
9:foreach configurationQ∈ Qdo
10:S θQ ←OPTLEARNER(D train, Q)▷learn latent optimization landscape
11:FreezeS θQ
12:L Q ←OPTDISCOVER(S θQ , Q)▷distill candidate symbolic laws
13:E Q ←EVALUATE(L Q, SθQ ,D val)▷predictive, structural, and symbolic evidence
14:C ← C ∪ {(L Q,E Q, Q)}
15:end for
16:Record candidate laws, evidence, and execution traces inS
17:(L ∗,A ∗,R)←SCIENTIFICCRITICANDTHEORYABSTRACTION(S,H,C)▷adjudication,
theory abstraction, mechanisms, and refinement
18: Update S with supported laws L∗, theory abstraction and mechanism findings A∗, associated
evidence, and refinementsR
19:ifadditional hypotheses, variables, or data are requiredthen
20:Initialize the next discovery round fromS
21:else
22:break
23:end if
24:end while
25:returnL ∗,A ∗
Agent instructions.Each specialized agent is assigned a defined scientific role, information scope
and output structure. The prompts emphasize testable hypotheses, executable empirical search and
evidence-grounded scientific abstraction. Their principal instructions are summarized below.
Theory Prior Agent
Role.Act as a scientific theorist preparing an optimization-law discovery problem.
Input.Research question, decision variable, available variables, compact training-side data structure and
allowed variable transformations.
Instructions.Identify established scientific theories and mechanisms relevant to the research question and
connect them to observed variables without treating theoretical priors as empirical conclusions. Formulate
a small set of explicit and testable mechanism hypotheses. Identify scientifically meaningful, target-
independent variables or derived variables that provide observable representations of these mechanisms,
and propose sparse symbolic-search priors over operators and functional structures when scientifically
justified. Exclude variable constructions that depend on the observed target or validation and test
information, and examine identifiability, redundancy and other theoretical risks. Express each proposal in
a form that can be evaluated through subsequent model fitting and symbolic discovery.
Output.Background theory, mechanism hypotheses, candidate variables, theoretical rationale, symbolic-
search priors, potential risks and unresolved scientific questions.
The Theory Prior Agent provides the scientific entry point to the discovery loop. Its role is particularly
important when raw observations admit many possible representations. Domain concepts can suggest
target-independent transformations that expose latent mechanisms, such as temporal differences,
relative quantities, interaction terms or state variables. These proposals constrain the effective
hypothesis space presented to symbolic discovery and provide an interpretable correspondence
between discovered mathematical terms and candidate scientific mechanisms. Because the proposals
27

remain explicit in the shared state, later stages can evaluate whether the resulting evidence supports,
weakens or leaves each hypothesis unresolved.
The Theory Prior Agent does not determine the functional form of the final law. Its proposals
define the scientific search space presented to OptScientist: which observed or derived variables may
represent a mechanism, and which symbolic structures are scientifically plausible enough to prioritize
during discovery. Whether those variables enter the final optimization law, and in what mathematical
form, is determined subsequently by OptLearner and OptDiscover from the observational data.
Experiment Agent
Role.Translate scientific priors into an empirical search for symbolic optimization laws.
Input.Theory priors, validated variables, task type, available OptScientist configurations, symbolic
operators, fixed validation protocol and compute budget.
Instructions.Organize the theoretical mechanisms, proposed variables and symbolic-search priors into a
bounded set of complementary OptScientist configurations. For each configuration, invoke OptLearner to
fit the latent optimization landscape on the fixed training data and then invoke OptDiscover to distil the
trained optimization representation into compact symbolic laws. Evaluate the resulting laws under the
fixed validation protocol. Repeat symbolic discovery where useful for assessing structural stability, and
preserve low-complexity, near-optimal complete expressions from each successful symbolic-search run
rather than retaining only a single run-level expression. When variable construction fails, repair only the
implementation while preserving its scientific meaning and target independence. Record the resulting
candidate expressions, predictive performance, symbolic complexity, distillation evidence, repeated-run
evidence and execution records. Preserve alternative high-performing structures for subsequent scientific
adjudication rather than selecting the final scientific law.
Output.OptScientist configurations, candidate symbolic optimization laws, predictive metrics, symbolic
complexity, distillation and repeated-run evidence, execution records and runtime issues.
The Experiment Agent provides the empirical interface between scientific reasoning and the OptSci-
entist Model. Candidate hypotheses are not evaluated by asking the language model to directly write a
final equation. Instead, the agent converts each hypothesis into an executable discovery configuration
specifying the candidate variables, model structure, symbolic operators and relevant search settings.
This produces a small set of scientifically differentiated model runs that can be compared under the
same training and validation protocol.
Each run then follows the fixed internal logic of the OptScientist Model. OptLearner receives the
observational variables selected for that configuration and learns a scalar optimization landscape
Sθ(x,y) . Depending on the structure of the observations, OptLearner may primarily denoise mean-
ingful scientific variables or additionally extract and compress features from high-dimensional or
weakly structured inputs. Its final layer consists of a single BL block, forming an optimization
representation bottleneck that represents the data as a single optimization problem. OptDiscover then
extracts the symbolic form of the learned optimization problem.
After OptLearner has been trained, its parameters are frozen and OptDiscover operates on the learned
representation rather than directly fitting the observed target. For a constrained representation, the
learned objective, inequality-constraint and equality-constraint components are distilled separately
and then assembled into a symbolic optimization problem. For a single-objective representation,
the corresponding learned objective is distilled directly. The symbolic operators and structural
priors proposed earlier in the discovery round determine the candidate symbolic language, while the
distillation objective and complexity control determine which expressions are retained. This division
of labour is important: the agent specifies the scientific search problem, whereas OptScientist learns
and distills the optimization structure supported by the data.
The resulting evidence extends beyond predictive performance. Each symbolic-search run can
contribute several low-complexity expressions with near-optimal distillation loss, allowing alternative
structures to remain available when the symbolic evidence does not identify a unique expression.
Candidate laws are therefore compared using their validation performance, symbolic complexity,
fidelity to the learned optimization representation and stability across repeated searches. Recording
these dimensions provides the Scientific Critic with evidence about both empirical adequacy and
structural reliability, while preserving multiple competitive expressions when the available data do
not clearly distinguish among them.
This explicit model interface also separates model discovery from scientific adjudication. The
Experiment Agent records successful and unsuccessful runs but does not choose which expression
28

should be interpreted as the final scientific law. Candidate-law adjudication, theory abstraction
and mechanism-level interpretation occur only after the candidate expressions and their associated
evidence have been returned to the shared research state.
Scientific Critic and Theory Abstraction Agent
Role.Evaluate discovered optimization laws as candidate scientific explanations and abstract their best-
supported scientific structure.
Input.Theory hypotheses, candidate symbolic laws, validation evidence, symbolic complexity, distillation
evidence, repeated-run stability and available robustness evidence.
Instructions.Compare candidate laws using their empirical evidence and characterize the level of support
for each proposed mechanism. Adjudicate among candidate laws by jointly considering predictive perfor-
mance, symbolic complexity, structural stability and consistency with plausible theoretical mechanisms,
while treating theory as a prior rather than a substitute for empirical support. Preserve the exact selected
candidate expressions and identify structures and qualitative mechanisms that recur across supported
laws. Synthesize the supported candidates into a general-to-specific theory abstraction, progressing from
a general optimization form to supported functional structure, exact parameterized laws and qualitative
findings. Assess explicit research hypotheses, identify competing explanations, limitations and remaining
failure modes, and propose additional variables, observations or targeted analyses that could resolve the
remaining scientific uncertainty.
Output.Candidate-law adjudication, supported symbolic laws, general-to-specific theory abstraction,
qualitative mechanisms, hypothesis assessment, limitations and targeted suggestions for subsequent
discovery.
The Scientific Critic connects symbolic recovery to theory formation. Symbolic regression can
produce several expressions with similar predictive performance, including algebraically related
forms and model-specific residual terms. The Critic evaluates these expressions collectively and
identifies structures that remain stable across supported candidates. Recurring structures provide
evidence for mechanism-level conclusions, whereas unstable or weakly identified terms are retained
as sources of uncertainty.
The Critic receives the output of OptScientist as empirical evidence rather than as a finished theory.
This distinction allows it to compare not only the symbolic expressions themselves but also how
faithfully they reproduce the learned optimization landscape, how well they generalize under the
fixed validation protocol, and whether similar structures reappear across repeated discovery runs.
Scientific interpretation is therefore conditioned on the evidence produced by the model rather than
on the plausibility of an expression in isolation.
Theory abstraction is performed hierarchically. At the highest level, the Critic identifies the general
optimization principle expressed by the supported laws, such as reward maximization, target tracking
or minimization of a deviation cost. It then constructs a parameter-tied general form where common
parameter structure is empirically supported, followed by the specific functional structure associated
with interpretable mechanisms. The exact parameterized candidate laws are retained at the next
level, preserving their empirical expressions, and the final level summarizes the supported qualitative
findings. This hierarchy allows OptScientist to synthesize candidate laws into a more general form
and qualitative mechanisms while preserving the detailed mathematical structure from which those
conclusions were derived.
The Critic also converts unresolved evidence into new scientific questions. A missing mechanism may
motivate a new derived variable; competing symbolic structures may motivate additional observations
capable of distinguishing their predictions; and systematic prediction failures may indicate omitted
context or an insufficient symbolic language. These outputs are returned to the shared research state
and provide structured inputs for a subsequent discovery round. In the next round, the Theory Prior
and Experiment Agents translate these unresolved questions into revised variables, hypotheses or
OptScientist configurations, so that scientific critique produces a concrete change in the subsequent
model search rather than remaining a purely textual assessment.
Overall, the architecture organizes OptScientist into an iterative sequence of theory formation, model-
based empirical discovery, evidence evaluation and theory abstraction. The Theory Prior Agent
establishes candidate mechanisms, scientifically meaningful representations and symbolic-search
priors. The Experiment Agent converts these proposals into executable configurations and invokes
the OptScientist Model. Within each run, OptLearner learns to represent observational data as an
optimization problem through an optimization representation bottleneck, and OptDiscover then
29

distills the learned representation into a compact symbolic optimization law. The Scientific Critic
then adjudicates among the resulting candidates and synthesizes their supported structure into more
general optimization forms and qualitative mechanisms. The Research Orchestrator preserves the
connection between these stages and carries unresolved scientific questions across iterations. This
division of labour places a specialized symbolic-discovery model at the empirical centre of the agentic
workflow, allowing language-model agents to guide and interpret discovery without substituting
linguistic generation for model-based evidence.
B Additional Experimental Details
B.1 Baselines
We compare OptScientist with standard machine-learning models, symbolic regression, optimization-
structured models, domain-specific models, and three LLM-based automated model-discovery meth-
ods. The general baselines include Multilayer Perceptron (MLP) (Rumelhart et al., 1986), Logistic
Regression (LR) (Cox, 1958), Random Forest (RF) (Breiman, 2001), eXtreme Gradient Boosting
(XGBoost) (Chen & Guestrin, 2016), Gradient-Boosted Decision Trees (GBDT) (Friedman, 2001),
Symbolic Regression (SR) (Cranmer, 2023), Neural Energy-Based Models (Neural EBM) (LeCun
et al., 2006), and Behavior Learning (BL) (Ma et al., 2026b). The LLM-based baselines are an
LLM-only researcher, GeCCo (Rmus et al., 2026) as a code-assisted LLM approach, and Model
Discovery Agent (MDA; Murphy, 2026) as a Bayesian experiment-design approach.
OptFeynman.For OptFeynman, we compare against MLP, LR, RF, XGBoost, and GBDT as standard
machine-learning baselines, SR as a direct symbolic-discovery baseline, Neural EBM and BL as
optimization-structured baselines, and the three LLM-based baselines.
Human decisions under risk and ambiguity.For CPC18, we compare against established be-
havioural models, including expected-value logit, expected-utility logit, prospect-theory logit with
fixed or fitted parameters, and mean–variance logit. We additionally include GBDT, MLP, RF, and
XGBoost as machine-learning baselines, together with the three LLM-based baselines.
Central-bank monetary decisions.For monetary-policy decisions, we compare against MLP, RF,
XGBoost, and GBDT as machine-learning baselines, Neural EBM as an optimization-structured
baseline, SR as a direct symbolic-discovery baseline, and the three LLM-based baselines.
B.2 OptFeynman Ground-Truth Recovery
Statistical analysis.We report additional statistics for the OptFeynman experiments in Figures 3
and 4. The analysis uses results from the OptLearner score and the final OptScientist symbolic law
produced by OptDiscover for 99 OptFeynman problems under each combination of decision type
(discrete or continuous) and training condition. Throughout this section,OptLearner scorerefers to
the learned optimization score before symbolic distillation, andOptScientist lawrefers to the final
symbolic optimization law produced by OptDiscover. We useCleanfor the original OptFeynman
setting andNoisy-contextfor the noisy-context version defined in Sec. 5.1, in which Gaussian noise
is added only to the training contexts. Each problem is treated as one observation when computing
statistics across the benchmark. One duplicated record in the continuous Clean setting contained
identical metrics and was counted once.
Recovery is evaluated using exact-order accuracy, pairwise preference accuracy, and the Gibbs
distribution induced by the recovered score. Exact-order accuracy measures agreement between the
complete preference order produced by the recovered and ground-truth objectives. Pairwise accuracy
measures agreement across individual pairs of candidate outcomes. For continuous tasks, preference
recovery is evaluated at K= 10 , 50, and 100 candidate outcomes, and distribution recovery is
evaluated on a dense grid over the decision interval.
Unless stated otherwise, reported uncertainty is the standard error across the 99 OptFeynman prob-
lems,
SE = s√n , n= 99,
30

where s is the sample standard deviation across problems. Error bars in Figures 3 and 4 use mean ±1
SE. Medians and interquartile ranges are also reported for metrics with uneven distributions across
problems. Perfect exact-order recovery denotes a task with exact-order accuracy equal to one.
Perfect exact-order recovery.Table 3 summarizes perfect ground-truth recovery. For discrete
outcomes, OptScientist recovers the complete ground-truth preference order on88/99 Clean problems
and 92/99 Noisy-context problems. For continuous outcomes, it achieves perfect recovery on 78/99
Clean problems and 76/99 Noisy-context problems at K= 10 , 50, and 100. The stability of these
counts as K increases shows that the recovered laws from OptScientist continue to preserve the full
ordering over increasingly dense sets of candidate outcomes.
The learned OptLearner score has substantially fewer perfectly recovered problems. In the continuous
Clean setting, the count decreases from 30/99 at K= 10 to 14/99 at K= 100 . This difference
is also visible in the discrete setting, where OptLearner achieves perfect recovery on 31/99 Clean
problems and27/99Noisy-context problems.
Table 3:Perfect exact-order recovery on OptFeynman.Entries report the number and percentage
of the 99 tasks with exact-order accuracy equal to one. OptScientist law denotes the final symbolic
optimization law produced by OptDiscover.
Decision type Representation Candidate set Clean Noisy-context
Discrete OptScientist lawK= 5 88/99 (88.89%) 92/99 (92.93%)
Discrete OptLearner scoreK= 5 31/99 (31.31%) 27/99 (27.27%)
Continuous OptScientist lawK= 10 78/99 (78.79%) 76/99 (76.77%)
Continuous OptLearner scoreK= 10 30/99 (30.30%) 30/99 (30.30%)
Continuous OptScientist lawK= 50 78/99 (78.79%) 76/99 (76.77%)
Continuous OptLearner scoreK= 50 20/99 (20.20%) 23/99 (23.23%)
Continuous OptScientist lawK= 100 78/99 (78.79%) 76/99 (76.77%)
Continuous OptLearner scoreK= 100 14/99 (14.14%) 15/99 (15.15%)
Continuous outcomes.Table 4 reports continuous preference recovery. Under the Clean condition,
mean OptScientist exact-order accuracy is0.900 at K= 10 , 0.871 at K= 50 , and 0.866 at K= 100 .
The corresponding values under Noisy-context are0.902,0.874, and0.869.
Table 4:Preference recovery for continuous OptFeynman problems.Values are mean ± SE across
99 OptFeynman problems. Median and interquartile range refer to exact-order accuracy. Higher
values indicate better recovery.
ConditionKRepresentation Exact order Median [Q1,Q3] Pairwise
Clean 10 OptScientist law0.900±0.027 1.000 [1.000,1.000] 0.963±0.015
Clean 10 OptLearner score0.825±0.026 0.940 [0.800,1.000] 0.960±0.007
Clean 50 OptScientist law0.871±0.032 1.000 [1.000,1.000] 0.963±0.015
Clean 50 OptLearner score0.743±0.035 0.900 [0.695,0.990] 0.960±0.008
Clean 100 OptScientist law0.866±0.033 1.000 [1.000,1.000] 0.963±0.015
Clean 100 OptLearner score0.719±0.035 0.880 [0.665,0.970] 0.960±0.008
Noisy-context 10 OptScientist law0.902±0.026 1.000 [1.000,1.000] 0.959±0.014
Noisy-context 10 OptLearner score0.826±0.026 0.950 [0.805,1.000] 0.960±0.008
Noisy-context 50 OptScientist law0.874±0.030 1.000 [1.000,1.000] 0.959±0.014
Noisy-context 50 OptLearner score0.743±0.035 0.910 [0.695,0.990] 0.960±0.008
Noisy-context 100 OptScientist law0.869±0.031 1.000 [1.000,1.000] 0.958±0.014
Noisy-context 100 OptLearner score0.722±0.035 0.880 [0.665,0.980] 0.960±0.008
For every value of K, the median and both quartiles of OptScientist exact-order accuracy are equal
to one. Most problems therefore retain perfect ordering even when the candidate set becomes
substantially denser. Pairwise recovery is similarly stable. Mean OptScientist pairwise accuracy
remains approximately 0.96 across all candidate-set sizes and both training conditions, with a median
of one.
31

Table 5:Distribution recovery for continuous OptFeynman problems.KL divergence is computed
between the ground-truth and recovered Gibbs distributions on the dense test grid. Values are mean
±SE across 99 OptFeynman problems. Lower values indicate closer distribution recovery.
Condition Representation KL Median [Q1,Q3]
Clean OptScientist law0.0461±0.0111 0.0080 [0.0013,0.0358]
Clean OptLearner score0.0078±0.0032 0.0015 [0.0010,0.0030]
Noisy-context OptScientist law0.0460±0.0163 0.0071 [0.0012,0.0382]
Noisy-context OptLearner score0.0082±0.0036 0.0014 [0.0009,0.0031]
OptLearner also achieves high pairwise accuracy, while its exact-order accuracy decreases more
strongly with K. Under the Clean condition, mean OptLearner exact-order accuracy decreases from
0.825atK= 10to0.719atK= 100.
The recovered continuous laws from OptScientist also preserve the Gibbs distributions generated by
the ground-truth objectives. Mean dense-grid KL divergence is 0.0461 under Clean and 0.0460 under
Noisy-context. The corresponding medians are 0.0080 and 0.0071, showing low distributional error
for most tasks. OptLearner achieves mean KL values of 0.0078 and 0.0082, consistent with its direct
fit to the stochastic optimization landscape.
Discrete outcomes.The discrete results show a similar pattern. Under the Clean condition, the
recovered OptScientist laws achieve mean exact-order accuracy 0.971 and pairwise accuracy 0.984.
Under Noisy-context, these values are0.974 and 0.984. The median and both quartiles of OptScientist
exact-order accuracy are equal to one in both conditions.
Table 6:Preference recovery for discrete OptFeynman problems.Values are mean ± SE across
99 problems. Median and interquartile range refer to exact-order accuracy.
Condition Representation Exact order Median [Q1,Q3] Pairwise Exact= 1
Clean OptScientist law0.971±0.014 1.000 [1.000,1.000] 0.984±0.011 88/99
Clean OptLearner score0.805±0.025 0.920 [0.675,1.000] 0.947±0.009 31/99
Noisy-context OptScientist law0.974±0.015 1.000 [1.000,1.000] 0.984±0.011 92/99
Noisy-context OptLearner score0.805±0.024 0.890 [0.705,1.000] 0.948±0.009 27/99
Training-context noise produces little change in the overall recovery statistics. Mean OptScientist
exact-order accuracy changes from 0.971 to 0.974, while mean pairwise accuracy remains approxi-
mately 0.984. The number of perfectly recovered tasks changes from 88/99 to 92/99. These results
are consistent with the robustness observed in Figure 4.
Table 7:Distribution recovery for discrete OptFeynman problems.The ground-truth Gibbs
distribution over five candidate actions is compared with the distribution induced by the recovered
score. Probability MAE is the mean absolute error between ground-truth and recovered Gibbs
probabilities. Values are mean±SE across 99 problems. Lower values indicate closer recovery.
Condition Representation Prob. MAE MAE median [Q1,Q3] KL KL median [Q1,Q3]
Clean OptScientist law0.0182±0.0025 0.0115 [0.0061,0.0201] 0.0217±0.0092 0.0036 [0.0008,0.0109]
Clean OptLearner score0.0161±0.0032 0.0112 [0.0083,0.0154] 0.1932±0.1873 0.0032 [0.0016,0.0059]
Noisy-context OptScientist law0.0208±0.0036 0.0117 [0.0062,0.0238] 0.2005±0.1852 0.0036 [0.0010,0.0132]
Noisy-context OptLearner score0.0161±0.0032 0.0110 [0.0080,0.0146] 0.2025±0.1964 0.0033 [0.0016,0.0052]
For the Gibbs distributions over the five candidate actions, we additionally report probability MAE,
defined as the mean absolute error between the ground-truth and recovered Gibbs probabilities across
candidate actions. The OptScientist laws achieve mean probability MAE 0.0182 and mean KL
divergence 0.0217 under the Clean condition. Their medians are 0.0115 and 0.0036, respectively.
Under Noisy-context, mean probability MAE remains low at 0.0208, with a median of 0.0117. Mean
OptScientist KL increases to 0.2005, while the median remains 0.0036 and the third quartile is
32

0.0132. The difference between the mean and median reflects a small number of tasks with large KL
values.
Table 8:Examples of recovered OptFeynman laws.Ground-truth and recovered laws are shown
in optimization form after removing numerical constants and scale factors that do not affect the
optimizer.
Decision variable Effective ground truth Effective recovered expression
y3 max y3 x3y3 max y3 x3y3
wmax
w
w2 max
w
w2
χmax
χ
Bχmax
χ
Bχ
Ef max Ef Ef cosθmax Ef Ef cosθ
θmax
θ
sinθmax
θ
sinθ
Gmax
G
G
 1
r2
− 1 r1

max
G
G(r1 −r 2)
r1r2
xmax
x
x2 max
x
x2
dmax
d
T2 −T 1
d max d
T2 −T 1
d
rmax
r
1
r2 max r
1
r2
dmax
d
1
d max d
1
d
Effect of OptDiscover complexity control.Here we evaluate the expression-level reduction used
within the symbolic complexity control of OptDiscover described in Sec. 3.2.2. In Table 9,Initial
denotes the recovered symbolic expression before this reduction, andFinaldenotes the compact
symbolic expression after it. We additionally compare exact-order recovery before and after this
reduction. Discrete recovery is unchanged: mean exact-order accuracy remains 0.971 under Clean
and0.974under Noisy-context, with88and92perfectly recovered problems, respectively.
For continuous outcomes, complexity control gives small improvements in exact-order recovery.
Under Clean, mean accuracy increases by 0.010, 0.011, and 0.013 at K= 10 , 50, and 100. At
K= 100 , the number of perfectly recovered problems increases from 67 to 78. Under Noisy-context,
changes in mean accuracy range from −0.001 to +0.005, and perfect recovery at K= 100 increases
from70to76problems.
Held-out baseline comparison.Tables 10 and 11 report ground-truth recovery for the baseline
models on unseen test contexts. The largest separation appears in exact-order recovery, which requires
the recovered score to preserve the complete preference order induced by the ground-truth objective.
In the discrete Clean setting, the two strongest baselines by mean exact-order accuracy are BL and
logistic regression. BL achieves mean exact-order accuracy 0.805 with perfect recovery on 31.3% of
tasks, and logistic regression achieves 0.716 with perfect recovery on 17.2%. OptScientist reaches
0.971 exact-order accuracy and perfectly recovers 88/99 tasks. The separation becomes larger for
continuous outcomes as the candidate set grows. At K= 100 , the two strongest baselines by mean
exact-order accuracy, BL and Neural EBM, achieve exact-order accuracies of 0.719 and 0.294, with
perfect recovery on 14.1% and 10.1% of tasks, respectively. OptScientist retains exact-order accuracy
0.866and perfectly recovers78/99tasks.
Pairwise and distributional metrics provide complementary views of recovery. Several baselines
preserve a substantial fraction of pairwise comparisons or closely approximate the Gibbs distribution
while showing considerably weaker recovery of the complete ordering. For example, Neural EBM
33

Table 9:Exact-order recovery before and after OptDiscover complexity control.Mean accuracy
is computed across matched OptFeynman problems. Initial denotes the recovered symbolic expression
before expression-level reduction, and Final denotes the compact symbolic expression after it. The
final column reports the number of problems with perfect exact-order recovery before and after this
reduction.
Decision type Condition Initial Final∆Perfect recovery
Continuous Clean,K= 10 0.890 0.900 +0.010 77→78
Continuous Clean,K= 50 0.860 0.871 +0.011 72→78
Continuous Clean,K= 100 0.852 0.866 +0.013 67→78
Continuous Noisy-context,K= 10 0.902 0.902−0.001 76→76
Continuous Noisy-context,K= 50 0.872 0.874 +0.002 75→76
Continuous Noisy-context,K= 100 0.864 0.869 +0.005 70→76
Discrete Clean0.971 0.971 0.000 88→88
Discrete Noisy-context0.974 0.974 0.000 92→92
Table 10:Held-out baseline recovery for discrete OptFeynman problems.Exact-order and
pairwise preference accuracy are evaluated on unseen test contexts. Exact = 1 reports the percentage
of tasks with perfect exact-order recovery. KL divergence compares the ground-truth and recovered
Gibbs distributions over the five candidate actions; lower values indicate closer distribution recovery.
For discrete decisions, a standard multiclass MLP can be written in the same finite-action softmax
form as a conditional Neural EBM, so we use the multiclass MLP directly rather than introducing a
separate Neural EBM baseline.
Condition MethodnExact order Exact= 1Pairwise KL
Clean GBDT 99 0.327 0.0% 0.844 0.1679
Clean LR 99 0.716 17.2% 0.919 0.0859
Clean MLP 99 0.420 6.1% 0.859 0.1580
Clean RF 99 0.206 0.0% 0.794 0.5992
Clean XGBoost 99 0.337 0.0% 0.847 0.0833
Clean SR 99 0.076 0.0% 0.743 0.8855
Clean LLM-only 99 0.588 5.1% 0.911 0.0125
Clean GeCCo 99 0.715 20.2% 0.928 0.2025
Clean MDA 99 0.700 21.2% 0.926 0.1579
Clean BL 99 0.805 31.3% 0.947 0.1932
Clean OptScientist 99 0.971 88.9% 0.984 0.0217
Noisy-context GBDT 99 0.371 0.0% 0.854 0.1744
Noisy-context LR 99 0.717 17.2% 0.919 0.0860
Noisy-context MLP 99 0.418 6.1% 0.860 0.1635
Noisy-context RF 99 0.104 0.0% 0.701 1.1334
Noisy-context XGBoost 99 0.331 0.0% 0.842 0.0636
Noisy-context SR 99 0.076 1.0% 0.743 0.8816
Noisy-context LLM-only 99 0.593 8.1% 0.911 0.1214
Noisy-context GeCCo 99 0.721 20.2% 0.930 0.1592
Noisy-context MDA 99 0.703 18.2% 0.930 0.1417
Noisy-context BL 99 0.805 27.3% 0.948 0.2025
Noisy-context OptScientist 99 0.974 92.9% 0.984 0.2005
reaches pairwise accuracy 0.888 and dense-grid KL divergence 0.0098 at K= 100 in the continuous
Clean setting, while its exact-order accuracy is 0.294. BL achieves a dense-grid KL divergence of
0.0078, lower than that achieved by OptScientist, while its exact-order accuracy decreases to 0.719
at K= 100 . A similar pattern appears for the LLM-only baseline in the discrete Clean setting,
which reaches KL divergence 0.0125 but exact-order accuracy 0.588, with perfect recovery on only
5.1% of tasks. These results show that accurate approximation of local pairwise relations or the
stochastic landscape can coexist with substantial errors in the complete preference order. Because
all preference metrics are evaluated on held-out contexts, exact-order recovery places a stronger
34

Table 11:Held-out baseline recovery for continuous OptFeynman problems.Within the exact-
order, perfect-recovery and pairwise columns, entries correspond to K= 10/50/100 , respectively.
Exact = 1 reports the percentage of tasks with perfect exact-order recovery. KL divergence compares
the ground-truth and recovered Gibbs distributions on the dense held-out test grid; lower values
indicate closer distribution recovery.
Condition MethodnExact order 10/50/100 Exact= 1 (%) 10/50/100 Pairwise10/50/100 KL
Clean GBDT 990.063/0.003/0.002 0.0/0.0/0.0 0.704/0.704/0.7040.6362
Clean Neural EBM 990.482/0.314/0.294 12.1/10.1/10.1 0.888/0.887/0.8880.0098
Clean MLP 990.061/0.003/0.001 0.0/0.0/0.0 0.703/0.703/0.7030.6349
Clean RF 990.064/0.003/0.001 0.0/0.0/0.0 0.703/0.702/0.7030.6408
Clean XGBoost 990.061/0.003/0.001 0.0/0.0/0.0 0.704/0.704/0.7040.6399
Clean SR 990.060/0.002/0.001 0.0/0.0/0.0 0.710/0.710/0.7110.6414
Clean LLM-only 990.061/0.003/0.002 0.0/0.0/0.0 0.701/0.702/0.7020.6422
Clean GeCCo 990.062/0.003/0.002 0.0/0.0/0.0 0.703/0.704/0.7040.6353
Clean MDA 990.062/0.002/0.002 0.0/0.0/0.0 0.704/0.704/0.7040.6355
Clean BL 990.825/0.743/0.719 30.3/20.2/14.1 0.960/0.960/0.9600.0078
Clean OptScientist 990.900/0.871/0.866 78.8/78.8/78.8 0.963/0.963/0.9630.0461
Noisy-context GBDT 990.063/0.003/0.001 0.0/0.0/0.0 0.704/0.704/0.7050.6372
Noisy-context Neural EBM 990.473/0.307/0.290 10.1/6.1/6.1 0.887/0.887/0.8880.0101
Noisy-context MLP 990.061/0.003/0.001 0.0/0.0/0.0 0.703/0.703/0.7030.6351
Noisy-context RF 990.081/0.006/0.002 0.0/0.0/0.0 0.675/0.674/0.6740.8009
Noisy-context XGBoost 990.062/0.003/0.002 0.0/0.0/0.0 0.704/0.704/0.7040.6399
Noisy-context SR 990.061/0.002/0.001 0.0/0.0/0.0 0.710/0.710/0.7100.6437
Noisy-context LLM-only 990.062/0.003/0.002 0.0/0.0/0.0 0.704/0.704/0.7040.6388
Noisy-context GeCCo 990.062/0.003/0.002 0.0/0.0/0.0 0.704/0.704/0.7040.6353
Noisy-context MDA 990.062/0.003/0.002 0.0/0.0/0.0 0.703/0.704/0.7040.6358
Noisy-context BL 990.826/0.743/0.722 30.3/23.2/15.2 0.960/0.960/0.9600.0082
Noisy-context OptScientist 990.902/0.874/0.869 76.8/76.8/76.8 0.959/0.959/0.9580.0460
requirement on the learned model: the recovered mechanism must preserve the full ordering generated
by the ground-truth objective across unseen contexts.
The LLM-based model-discovery baselines show particularly limited recovery in the continuous
setting. On discrete Clean OptFeynman, GeCCo and MDA achieve exact-order accuracies of 0.715
and 0.700, respectively, remaining below BL and substantially below OptScientist. On continuous
Clean OptFeynman, their performance decreases sharply as the candidate set becomes denser. At
K= 100 , LLM-only, GeCCo and MDA achieve exact-order accuracies of 0.0018, 0.0021, and
0.0017, respectively, with no perfectly recovered tasks; their pairwise accuracies remain around
0.70, and their dense-grid KL divergences remain around 0.64. A plausible interpretation is that
LLM-based discovery depends strongly on the scientific and functional-form priors available in
language. When such priors provide limited information about the generating mechanism, identifying
a transferable law directly from observations becomes substantially more difficult. Strong textual
priors may also favour familiar or plausible functional forms, creating a risk that the discovered
expression reflects prior knowledge more strongly than the mechanism that generated the observations.
The OptFeynman results therefore highlight the value of learning the optimization landscape from
data before symbolic distillation, particularly when informative domain priors are unavailable or
incomplete.
LLM baseline protocol.For the LLM-based baselines on OptFeynman, model generation, revision,
and selection use only the training and validation splits. All methods use the same DeepSeek-V4-
Flash model and follow their original discovery procedures with a unified budget of eight discovery
rounds. To prevent semantic leakage from physics-specific notation, all OptFeynman variable names
are replaced with neutral identifiers before being provided to the LLMs. The held-out test set is
never exposed during model discovery or model selection. After the final model is selected, its
predictive model is evaluated directly on the test set using the common OptFeynman metrics; this
final evaluation is fully deterministic and involves no further LLM interaction.
Overall, the detailed statistics support the ground-truth recovery results reported in the main text.
OptScientist recovers the complete preference order on most OptFeynman problems, with high
pairwise agreement across the benchmark. It substantially outperforms the baseline methods in
exact-order recovery, particularly in the fraction of problems for which the complete ground-truth
35

preference order is perfectly recovered. Continuous recovery remains stable as the candidate set
increases from K= 10 to K= 100 , and recovery remains strong when Gaussian noise is added to
the training contexts. The problem-level medians and quartiles show that these results hold across
most of the benchmark optimization problems.
B.3 Human Choice under Risk and Ambiguity
B.3.1 Dataset and evaluation
The CPC18 experiment studies repeated binary choices between two monetary prospects under
risk and ambiguity (Plonsky et al., 2019). We use a random split with 408,600, 51,060 and 51,090
observations for training, validation and testing, respectively. For Figure 5, test metrics are first
computed at the participant level and then averaged across the 686 test participants. Error bars denote
the standard error of the mean across participant-level metrics.
B.3.2 Theory Prior Agent and variable discovery
Before symbolic discovery, the Theory Prior Agent used scientific theories of decision-making under
risk, ambiguity and repeated feedback to construct theoretically motivated variables beyond those
directly available in the CPC18 data. These variables were specified independently of validation and
test performance and were subsequently considered as candidate inputs for symbolic discovery.
Let option j∈ {A, B}have high payoff Hj, low payoff Lj, and probability pH,j of the high payoff.
The agent constructed expected-value representations
EVA =p H,AHA + (1−p H,A)LA,EV B =p H,BHB + (1−p H,B)LB,
together with relative probability and payoff-dispersion measures,
∆pH =p H,B −p H,A,∆Spread = (H B −L B)−(H A −L A).
It also introduced an ambiguity–correlation interaction,
AmbNegCorr = Amb1{Corr<0},
and an indicator for the feedback framing condition,
ByFB =1{Condition =ByFB}.
Participant-level variables included gender,
Male =1{Gender = M},
and an indicator for residence in wealthier regions,
WealthyRegion =1{Region∈ W},
whereWdenotes the corresponding region classification used in preprocessing.
Because CPC18 contains repeated choices with feedback, the Theory Prior Agent also proposed
lagged obtained and forgone payoff variables. Let RA t and RB t denote the payoff feedback associated
with options A and B, and let yt ∈ {0,1}indicate whether option B was chosen. The obtained and
forgone payoffs are
Robt t = (1−y t)RA t +y tRB t , R forgone t =y tRA t + (1−y t)RB t .
For prediction at round t, only lagged quantities from preceding rounds were used. During sym-
bolic discovery, OptScientist Model subsequently identified decision-relevant combinations of these
variables, including the counterfactual payoff difference
∆Rcf t =R forgone t −R obt t .
Together, the Theory Prior Agent provides candidate representations of expected reward, probability
sensitivity, risk, ambiguity, framing, demographic heterogeneity and feedback, while the OptScientist
Model determines how these variables enter the discovered symbolic law.
36

B.3.3 Direct symbolic law
For the binary-choice task presented in the CPC18 dataset, let yt = 1 denote choosing option B and
yt = 0denote choosing option A. The direct OptScientist law can be written as
bU(x t, yt) =y tD(xt),by t = arg max yt∈{0,1} bU(x t, yt),(14)
where D(xt) is the recovered score difference between choosing B and choosing A. The selected
expression is
D(xt) =−0.8173EV A + 0.5701EV B + 0.3393L B −0.0709 PrevForgone
−0.8173 PrevExp + 1.6541 PrevChoiceB + 0.0709 PrevPayoff.(15)
The model predicts that people would choose option B when D(xt)>0 . Continuous variables are
standardized using the training split. The expression has symbolic complexity 23 and contains five
distinct numerical constants.
Equation (15) supports the abstract law shown in Figure 5b. The current lottery terms form the
immediate reward component V(x t, yt). The previous-choice term captures persistence in the last
action, corresponding to the switching-cost component. The previous payoff and forgone-payoff
terms capture sequential feedback from the previous round.
B.3.4 Automatic-feature symbolic law
AutoF OptScientist follows the automatic-feature extraction route introduced in the OptScientist
Model. It first maps(x t, yt)into an intermediate representation,
h(xt, yt) = (h1, . . . , h8),(16)
taken from an OptLearner inner layer. OptDiscover then distills the final score as a symbolic function
of these learned features:
s(h) = 0.04345h 1 + 0.00976h 2 + 0.11970h 3 + 0.04345h 6 + 0.15760h 7
+ 0.04345|h 6|+ 0.11970|0.1819h 3 −0.1819h 4 + 0.3752h 7| −1.3408.(17)
The induced binary score difference is
DFM(xt) =s(h(x t,1))−s(h(x t,0)).(18)
The model predicts that people would choose option B when DFM(xt)>0 . This expression has
outer symbolic complexity 33 and contains seven distinct numerical constants. This automatic-feature
route allows OptLearner to compress weakly structured behavioural information before symbolic
extraction.
B.3.5 Predictive performance and complexity
Table 12:Predictive performance and complexity on CPC18.Metrics are reported as participant-
level mean ± standard error across test participants. Parameter count denotes the number of distinct
numerical constants in the recovered symbolic law.
Variant Parameters Accuracy↑AUC↑Prob. MSE↓NLL↓KL↓ECE↓
Direct OptScientist 50.829±0.004 0.863±0.004 0.149±0.002 0.476±0.004 0.011±0.001 0.172±0.002
AutoF OptScientist 70.798±0.004 0.865±0.004 0.137±0.002 0.422±0.006 0.006±0.000 0.116±0.001
Table 12 reports participant-level predictive performance and parameter counts for the two OptScien-
tist variants. Direct OptScientist achieves higher choice accuracy with fewer parameters, whereas
AutoF OptScientist yields slightly higher AUC and better probabilistic calibration, with lower prob-
ability MSE, NLL, KL divergence and ECE. Thus, direct symbolic discovery provides the more
parsimonious decision rule, while automatic feature extraction improves the fidelity of predicted
choice probabilities.
Notably, the MLP baseline achieves approximately 84% held-out accuracy. Together with the
clustering of the strongest predictive models around 82–84%, this suggests that predictive performance
on CPC18 is already close to saturation.
37

B.4 Central-Bank Monetary Policy
B.4.1 Dataset and evaluation
The central-bank experiment studies quarterly monetary-policy decisions from macro-financial
conditions. The dataset contains 127 quarterly observations. We use 90, 23 and 14 observations for
training, validation and out-of-time testing, respectively. The outcome is a five-class monetary policy
stancey t ∈ {−2,−1,0,1,2}, ranging from large easing to large tightening.
Continuous model predictions are mapped to the observed five policy classes before computing exact
policy-stance accuracy. Policy-direction accuracy compares the sign of the mapped policy class,
distinguishing easing, no change and tightening. Error bars in Figure 6 are bootstrap standard errors
from10,000resamples of the14test quarters with replacement.
B.4.2 Single-Usymbolic law
The single-U OptScientist Model distills the learned policy landscape into one symbolic objective
over the candidate policy stancey t. The concrete distilled symbolic branch is
Ut(y) =y

0.01812a trt−1 −0.01812a t∆t + 0.01812a tℓt + 0.01812a ty
−0.33822c t + 0.19520g t −0.04029r t−1∆t + 0.01812r t−1ℓt + 0.01812r t−1ut
+ 0.04029r t−1y−0.27460r t−1 + 0.04029 ∆2 t −0.05841 ∆ tℓt −0.01812 ∆ tut
−0.08058 ∆ ty+ 0.93769 ∆ t + 0.01812ℓ 2 t + 0.01812ℓ tut + 0.05841ℓ ty
−0.46980ℓ t + 0.19520τ t + 0.01812u ty+ 0.04029y 2 −0.93769y  ,(19)
with final score
St(y) = 0.58028U t(y) + 0.72030.(20)
Here at denotes the adjusted national financial conditions index, rt−1 the previous average target rate,
∆t the previous quarterly change in the target rate, ℓt the St. Louis financial stress index, ct the credit
spread, gt real GDP growth, ut unemployment and τt the term spread. All continuous variables are
standardized using the training split. The single-U expression has final effective symbolic complexity
131under the decision-relevant complexity accounting used in the experiment.
B.4.3 Rewriting the symbolic law into target-tracking form
The target-tracking form in Figure 6a is obtained by grouping the decision-relevant terms of the
discovered score. Since 0.58028>0 , the positive head scale in Eq.(20) preserves the maximizer over
y. The head bias is constant across candidate policy actions and is removed from the decision-relevant
expression. After this normalization, Eq. (19) can be collected as a polynomial in the candidate policy
action:
St(y)∼A ty+B ty2 +dy 3,(21)
where ∼ denotes equivalence up to positive scaling and additive context-only constants. The linear
policy-pressure term is
At = 0.01812a trt−1 −0.01812a t∆t + 0.01812a tℓt −0.33822c t + 0.19520g t
−0.04029r t−1∆t + 0.01812r t−1ℓt + 0.01812r t−1ut −0.27460r t−1
+ 0.04029 ∆2 t −0.05841 ∆ tℓt −0.01812 ∆ tut + 0.93769 ∆t
+ 0.01812ℓ 2 t + 0.01812ℓ tut −0.46980ℓ t + 0.19520τ t.(22)
The quadratic and cubic decision-residual terms are
Bt = 0.01812a t + 0.04029r t−1 −0.08058 ∆ t + 0.05841ℓ t + 0.01812u t −0.93769,(23)
d= 0.04029.(24)
For better interpretability, the Scientific Critic Agent abstracts the leading linear term At into four
macro-policy pressures,
At ⇝N t =m(g t +τ t)−m(f t +qc t)−ρr t−1 + (s+ρ)∆ t.(25)
38

Here gt +τ t groups real activity and the term spread as macroeconomic strength; ft +qc t groups
financial stress and credit conditions as financial fragility; rt−1 summarizes inherited policy tightness;
and ∆t summarizes policy momentum. Remaining interaction terms, state-dependent curvature and
higher-order terms are retained in the residual decision term below.
WritingB t =−κ+δ t withκ >0, the decision-relevant score of Eq. 21 can be rewritten as
St(y)∼N ty−κy 2 +δ ty2 +dy 3.(26)
Maximizing this score is equivalent to minimizing its negative:
max
y∈Y
St(y)≡min y∈Y

κy2 −N ty−δ ty2 −dy 3	 .(27)
Completing the square for the leading quadratic part gives
κy2 −N ty=κ

y− Nt
2κ
2
− N 2 t
4κ .(28)
The last term depends only on the context and does not affect the minimizing policy action. Dividing
by the positive constantκyields the displayed latent-target form:
min
yt∈Y
(
yt − Nt 2κ 2 +ε t(yt) ) ,(29)
where
εt(yt) =− δt κ y2 t − d κ y3 t (30)
collects residual decision-relevant deviations from the leading target-tracking structure. Thus, the
abstract law used in Figure 6a is a mechanism-level rewriting of the discovered symbolic score:
policy follows a latent target Nt/(2κ), with residual terms capturing state-dependent curvature and
higher-order deviations.
B.4.4 ConstrainedU/C/Tsymbolic law
We further considered a constrained OptScientist Model whose optimization representation bottleneck
contains three active components: an objective branch U, an inequality-constraint branch C, and a
target-deviation or risk branch T . OptDiscover distills these components into symbolic form, yielding
the final score
St(y) = 1.39737U t(y)−1.39737C t(y)−1.39737T t(y).(31)
The three branches are
Ut(y) =y

0.02035a t + 0.02035π core t + 0.04071 ∆t −0.02035y−0.51405  ,(32)
Ct(y) = 0.88835 max

0,0.4289a t −0.4289c t + 0.4289g t + ∆t
−0.4289ℓ t + 0.4289v t −1.4289y−0.92033

,(33)
and
Tt(y) = 0.11839

−0.55185a t + 0.55185c t −0.55185 ∆ t +ℓ t
−0.55185τ t + 0.55185v t + 2y
2
.(34)
Here πcore t is core PCE inflation and vt is VIX. The U branch captures policy pressure from financial
conditions, core inflation and policy momentum; the C branch captures a one-sided constraint
involving financial stress, growth and market volatility; and the T branch captures a quadratic
deviation penalty. The branch activations are identity for U, ReLU for C and square for T . The final
effective complexities are19,31and29, respectively, giving total effective complexity79.
39

Table 13:Predictive performance on central-bank monetary-policy decisions.Exact accuracy
is computed after mapping continuous predictions to the five policy classes. Direction accuracy
compares easing, no-change and tightening directions. Values are mean ± bootstrap standard error
over 10,000 quarter-level resamples. OptScientist-C denotes OptScientist with constraints.
Model Params. MSE↓MAE↓R 2↑Exact acc.↑Direction acc.↑
MLP 5,0571.6093±0.6026 0.9453±0.2250−0.1554±0.5005 0.3571±0.1268 0.4286±0.1313
Random forest 134,0001.0960±0.3639 0.8340±0.1693 0.2132±0.1663 0.3571±0.1277 0.5714±0.1323
XGBoost 6,6000.8501±0.2630 0.7616±0.1387 0.3897±0.1634 0.3571±0.1284 0.6429±0.1270
Neural EBM 5,1211.0276±0.4118 0.6343±0.2132 0.2622±0.3688 0.5714±0.1327 0.7143±0.1213
GBDT 6,6000.7595±0.2643 0.6884±0.1430 0.4547±0.1301 0.5714±0.1314 0.7857±0.1094
Symbolic regression 60.6788±0.34280.5636±0.16160.5126±0.2009 0.5714±0.1322 0.7143±0.1204
OptScientist 110.6513±0.30800.5750±0.15210.5324±0.1655 0.7857±0.1097 0.8571±0.0943
OptScientist-C 110.6792±0.3239 0.5700±0.1605 0.5124±0.2265 0.7143±0.1217 0.7857±0.1109
B.4.5 Predictive performance and complexity
Table 13 reports held-out test performance. All uncertainty values are bootstrapped standard errors
from 10,000 quarter-level resamples with replacement. Parameter count follows the plotting conven-
tion: for neural and tree models it counts model parameters or tree capacity, whereas for symbolic
models it counts distinct numerical constants in the final expression. Symbolic structural complexity
is reported separately.
OptScientist shows the strongest overall out-of-time predictive performance. It attains the lowest
MSE and highest R2, exact policy-stance accuracy and direction accuracy, while symbolic regression
achieves a slightly lower MAE. OptScientist-C also remains competitive, with exact and direction
accuracies of0.7143and0.7857, respectively.
Under decision-relevant structural-complexity accounting, the single-U OptScientist law has effective
complexity 131, the constrained U/C/T law has total effective complexity 79, and the symbolic-
regression baseline has complexity 21. Thus, OptScientist-C yields a more compact and explicitly
structured law, whereas the single-U formulation achieves stronger out-of-time performance on most
metrics. This difference may arise because the single-U formulation retains richer state-dependent
interactions and higher-order decision structure, whereas the constrained U/C/T decomposition
imposes stronger structural restrictions. These restrictions improve parsimony and interpretability,
but may omit variation that remains predictive in unseen periods.
B.5 Token-Efficient Model Discovery
We provide additional details for the token-efficient model-discovery experiment in Sec. 4.4. OptSci-
entist is compared with three LLM-based model-discovery baselines: (i) LLM-only discovery, which
directly proposes and iteratively revises candidate models; (ii) GeCCo, a code-assisted LLM approach
(Rmus et al., 2026); and (iii) MDA, a Bayesian experiment-design approach (Murphy, 2026). All
methods use the same DeepSeek-V4-Flash (Xu et al., 2026) as the underlying language model and
receive the same research description, variable information, and training data. The comparison is
conducted on the CPC18 dataset and the central-bank monetary-policy dataset described in Secs. 4.2
and 4.3. For each LLM-based baseline, we evaluate maximum generation settings of8,192,12,000,
16,384and24,000tokens per LLM call.
Evaluation protocol.Model generation, revision and selection use only the training and validation
data. The held-out test set is not exposed during the discovery process and is evaluated after the
final model has been selected. We record the held-out predictive accuracy of each discovered model
together with cumulative LLM output-token consumption across the complete discovery run. The
maximum-token setting denotes the generation limit for each individual LLM call and therefore
differs from the cumulative number of generated tokens reported below.
Token accounting.We use cumulative output-token consumption as the primary measure of language-
model budget. The discovery methods differ in their input representations, prompting structures
and intermediate context, making input-token counts less directly comparable across approaches.
Generated output tokens provide a common measure of the model-generation budget and are also
the more expensive component under the API pricing used in these experiments. We additionally
40

Table 14:Token-efficient model discovery on the CPC18 dataset.Held-out predictive accuracy and
cumulative LLM output-token consumption are reported for each discovery setting. The maximum-
token column gives the generation limit per LLM call. OptScientist achieves held-out accuracy near
the apparent CPC18 predictive ceiling with substantially lower output-token consumption.
Model Max tokens Output tokens Held-out acc.↑Acc./token(×10 −5)↑
LLM-only 8,192 17,981 83.354% 4.636
12,000 15,771 82.956% 5.260
16,384 16,048 83.173% 5.183
24,000 16,124 83.259% 5.164
GeCCo (Rmus et al., 2026) 8,192 35,947 83.777% 2.331
12,000 37,317 83.487% 2.237
16,384 35,873 83.667% 2.332
24,000 35,760 83.540% 2.336
MDA (Murphy, 2026) 8,192 45,761 83.114% 1.816
12,000 44,807 83.346% 1.860
16,384 41,550 83.395% 2.007
24,000 44,516 83.172% 1.868
OptScientist–6,39682.900%12.961
report held-out accuracy per output token as a descriptive summary of the accuracy–token trade-off.
The analysis concerns LLM-token efficiency; training and symbolic-search computation outside the
language model are not included in this measure.
Table 15:Token-efficient model discovery on central-bank monetary-policy decisions.Held-
out policy-stance accuracy and cumulative LLM output-token consumption are reported for each
discovery setting. OptScientist achieves the highest held-out point estimate while using substantially
fewer output tokens than the LLM-based discovery baselines.
Model Max tokens Output tokens Held-out acc.↑Acc./token(×10 −5)↑
LLM-only 8,192 18,381 44.318% 2.411
12,000 16,691 49.432% 2.962
16,384 17,361 47.727% 2.749
24,000 18,142 40.341% 2.224
GeCCo (Rmus et al., 2026) 8,192 23,188 64.205% 2.769
12,000 26,350 56.818% 2.156
16,384 25,447 56.250% 2.210
24,000 26,677 53.409% 2.002
MDA (Murphy, 2026) 8,192 29,611 68.182% 2.303
12,000 27,687 64.205% 2.319
16,384 25,576 70.455% 2.755
24,000 29,373 64.773% 2.205
OptScientist–5,976 78.600% 13.153
Token-efficiency results.On human decisions under risk and ambiguity, the LLM-based baselines
achieve closely clustered held-out accuracies while consuming between 15,771 and 45,761 output
tokens. Notably, the strongest predictive models cluster around 82–84% held-out accuracy. Perfor-
mance on the CPC18 dataset appears to saturate across all methods at approximately 83% held-out
accuracy, suggesting that CPC18 poses a relatively less challenging model-discovery problem. Never-
theless, OptScientist reaches competitive held-out accuracy using 6,396 output tokens, corresponding
to 59.4% fewer tokens than the lowest-token baseline. Its accuracy per output token is12.961×10 −5,
compared with a maximum of5.260×10 −5 among the LLM-based baselines.
On central-bank monetary-policy decisions, OptScientist achieves the highest held-out policy-stance
accuracy, reaching 78.6% with 5,976 output tokens. The strongest LLM-based baseline reaches
70.455% accuracy with 25,576 output tokens, while output-token consumption across the baseline
settings ranges from 16,691 to 29,611. Compared with the CPC18 dataset, modeling monetary-
policy decisions appears more challenging for the LLM-based baselines, as the discovered models
exhibit greater variability in performance. OptScientist also reaches an accuracy-per-token value of
41

13.153×10 −5, compared with a maximum of 2.962×10 −5 among the baselines. Together, the two
tasks show that OptScientist reaches competitive or stronger held-out predictive performance with
substantially less LLM generation, supporting the accuracy–token-efficiency trade-off reported in
Figure 7.
42
