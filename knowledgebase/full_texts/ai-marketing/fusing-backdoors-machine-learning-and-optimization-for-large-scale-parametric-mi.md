---
title: Fusing Backdoors, Machine Learning, and Optimization for Large-Scale Parametric Mixed-Integer Programs
url: https://arxiv.org/abs/2606.21440
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- El Mehdi Er Raqabi
- Pascal Van Hentenryck
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.21440
pages: 43
chars: 94252
fetched_at: '2026-11-08T13:28:49+00:00'
kb_version: 1
---

# Fusing Backdoors, Machine Learning, and Optimization for Large-Scale Parametric Mixed-Integer Programs

Fusing Backdoors, Machine Learning, and Optimization
for Large-Scale Parametric Mixed-Integer Programs
El Mehdi Er Raqabi, 1,2,∗ Pascal Van Hentenryck 2
1Department of Operations and Decision Systems, Université Laval, Québec, Canada
2H. Milton Stewart School of Industrial and Systems Engineering, Georgia Institute of Technology, Atlanta, USA
∗Corresponding Author: el-mehdi.er-raqabi@fsa.ulaval.ca
Abstract
Large-scale optimization problems are often solved repeatedly under similar structural con-
ditions, leading to substantial computational overhead. This occurs in applications such as
power systems, transportation, and supply chain networks, where the underlying structure is
fixed while parameters frequently vary under perturbations.
This paper proposes a Learning to Optimize (LTO) framework that accelerates the solution
of large-scale general mixed-integer problems by leveraging the concept of a backdoor, i.e., a
subset of variables that drive most of the computational complexity. The proposedBIPC
framework consists of three phases. Phase I is anidentificationprocedure that discovers a
backdoor for a set of instances in the distribution. Phase II uses supervised learning to develop
machine learning modelsthat, given an instance, predict values for bounded-domain backdoor
variables and intervals for wide-domain backdoor variables. These predictions define a reduced
optimization problem where the predictions constrain the backdoor variables, while the other
variables remain free. Phase III optimizes this reduced problem and, if necessary, applies a
correction stepto restore feasibility or the optimality guarantees.
Experiments on real-world, large-scale problems show substantial reductions in solution time
with only a limited loss in solution quality. The framework enables organizations to solve
large-scale optimization problems efficiently in the presence of frequent perturbations, such as
unexpected events, demand fluctuations, or operational changes. Because these changes affect
parameters rather than the problem structure,BIPCcan quickly provide high-quality, feasible
solutions, offeringapracticalapproachtointegratingmachinelearningintoexistingoptimization
pipelines.
Keywords: large-scale optimization, machine learning, mixed-integer programming, optimization
proxies, parametric optimization
1
arXiv:2606.21440v1  [cs.LG]  19 Jun 2026

1 Introduction
Large-scale optimization problems play a central role in many real-world applications, including
power systems, transportation, and supply chain networks. In practice, these problems are often
solved repeatedly under similar structural conditions. Still, parameters such as demand, resource
availability, or operational constraints change over time due to unexpected events or fluctuations.
Formally, these problems are often referred to as parametric optimization problems, i.e., problems
that share the same overall structure, e.g., the same generators in power systems (Er Raqabi et al.,
2025a), the same conveyors and quays in downstream coastal planning (Er Raqabi et al., 2025b),
the same facilities in package delivery (Mohan et al., 2025), the same machines in a manufacturing
layout Moinuddin et al. (2026), with only parameters changing, making numerous instances of data
typically related (Akhlaghi et al., 2025; Cai et al., 2025). These parametric problems are usually
modeled using general mixed integer programs (MIPs) of the form
ϕ(P) = argmin{c ⊤x|Ax≤b, x∈R n, xi ∈Z∀i∈ I},
whereP= (A,b,c)is the instance data,A∈R m×n,b∈R m,c∈R n, andI ⊆ {1, . . . , n}
denotes the index set of general integer variables. Solving each instance of this parametric problem
from scratch can be computationally expensive and time-consuming, thereby limiting the ability of
organizations to respond quickly to real-time operational changes, meet real-time constraints, and
implement interaction optimization tools exploring many scenarios.
This motivates the development of approaches that exploit the repetitive structure of these prob-
lems to accelerate computation while maintaining solution quality and feasibility. Large-scale op-
timization problems have traditionally been solved using exact methods such as MIP solvers and
decomposition algorithms, or using heuristic and metaheuristic approaches (Er Raqabi, 2024). To
acceleratecomputation, practitionersoftenemploywarm-starting, validinequalities, andfixingtech-
niques, as well as surrogate models that exploit problem structure (Er Raqabi et al., 2024). More
recently, learning-augmented methods have been proposed to guide optimization, for example, by
predicting feasible solutions, variable bounds, or partial assignments (Bengio et al., 2021; Akhlaghi
et al., 2025). These approaches have been applied across a range of domains, including transporta-
2

tion planning (Morabit et al., 2021), supply chain network design (Cai et al., 2025), and power
system operations (Chen et al., 2023), demonstrating their potential to reduce computational time
while maintaining solution quality in specific settings.
Despite these advances, existing methods face limitations when applied to large-scale parametric
optimization problems that are fundamentally different in nature: (1) they are expressed in terms
of integer variables that can take large values, as they represent multi-faceted decisions, including
procurement, production, and inventory decisions over a long time horizon; and (2) they typically
feature millions of integer variables. As a result, many existing techniques that fuse operations
research (OR) and machine learning (ML) are not directly applicable. Some approaches focus on
predicting only integer variables taking zero values at optimality, which may not always be sufficient
for real-world instances when some non-zero variables must be determined accurately to solve the
problem efficiently (Akhlaghi et al., 2025; Cai et al., 2025). The intuition in this research is that
predicting the values of all integer variablesxi ∈ Iis hard and costly and often yields infeasible
solutions, i.e., solutions that require repairs. Instead, this paper recognizes that, for various classes
of parametric MIPs, there exists a subsetB ⊆ Iof integer variables, called abackdoor, that, when
fixed, creates a lower-dimensional problem that is much easier to solve. To the best of the authors’
knowledge, there is no general framework that systematically identifies backdoors for parametric
optimization problems.
ThismotivatesthedevelopmentoftheBackdoorIdentification, Prediction, andCorrection(BIPC)
framework for parametric MIPs that combines backdoor identification, ML, and repair mechanisms
to obtain, in reasonable time, high-quality solutions to instances of parametric MIPs. This paper
is a detailed presentation ofBIPCand makes the following contributions:
1.TheBIPCFramework.The paper presents a novel 3-phase framework to obtain high-
quality solutions to parametric MIPs. Phase I identifies a backdoor that drives most of the
computational complexity for a class of instances. Phase II uses ML to predict values or
restricted domains for the backdoor variables. Phase III uses optimization to complete the
partial assignment and possibly corrects the predictions using repair mechanisms.
2.TheBIPCPredictions.Unlike existing methods for MIP models that often predict only
zeros for integer variables or focus on 0-1 MIPs,BIPCpredicts all backdoor variables. For
3

integer variables spanning a short range,BIPCpredicts a specific value. For integer variables
spanning a large range, it predicts 0 or restricted domains.BIPCthus generalizes existing
methods in the literature (Akhlaghi et al., 2025; Cai et al., 2025).
3.TheBIPCTaxonomy.The paper presents a taxonomy for designingBIPCfor a given
parametric optimization MIP. The taxonomy includes the problem size, variable types, and
feature types.
4.BIPCApplications and Computational Results.BIPCis tested on five real-world
large-scale problems: a middle-mile consolidation network design (MMCNP), a strategic loco-
motive assignment problem (SLAP), exam class scheduling (COURSE), a downstream supply
chain planning (OCP), and an order fulfillment problem (OFP). The results demonstrate
consistent and significant reductions in solution time while maintaining solution quality.
The remainder of the paper is structured as follows. Section 2 reviews the relevant literature on
learning-based methods and proxy approaches. Section 3 presents an overview ofBIPC. Section 4
introduces theBIPCtaxonomy and methodology. Sections 5–7 discuss the threeBIPCphases
in detail. Section 8 describes the experimental design and the real-world large-scale problems
considered. Section 9 reports computational results and analyzes the performance of theBIPC
framework. Finally, Section 10 concludes the paper and outlines directions for future research.
2 Literature Review
The use of ML for MIPs has attracted significant attention in recent years. It is increasingly
recognized as a promising direction to overcome some of the computational challenges (Bengio
et al., 2021; Kotary et al., 2021; Vesselinova et al., 2020), especially for problems that can only be
solved by fusing the powers of OR and ML (Van Hentenryck and Dalmeijer, 2024). Learning-based
approaches are well known for their ability to yield effective empirical algorithms that leverage
regularities in large real-world datasets and improve solution times (Cappart et al., 2021; Kotary
et al., 2021; Morabit et al., 2021; Khalil et al., 2022a).
The integration of optimization and ML recently led to the development of several distinct ap-
proaches, surveyed by Kotary et al. (2021). These methods, often referred to by various names in
4

the literature, can be categorized into three main categories, increasingly hybridized: 1) Decision-
focused learning, 2) Optimization proxies, and 3) Learning to optimize. Decision-focused learning,
also called smart-predict-then-optimize or predict-and-search, aims at training forecasting and op-
timization models in the same pipeline (see e.g., Elmachtoub and Grigas (2022); El Balghiti et al.
(2019); Ning and You (2019); Sahinidis (2004); Donti et al. (2017)). Optimization proxies aims at
learning the mapping between the input and an optimal solution of an optimization problem (see
e.g., Chen et al. (2023); Kotary et al. (2021, 2022); Donti et al. (2021); Huang and Chen (2021); Park
and Van Hentenryck (2023)). Learning to optimize focuses on techniques to improve the efficiency
and the solution quality of optimization algorithms and solvers (Tang and Yao, 2024; Maragno
et al., 2025). This paper is a hybridization of these three categories and is the first to leverage their
combined capabilities.
Decision-focused learning.In decision-focused learning, Park et al. (2023) introduce the Predict-
Repair-Optimize framework, which predicts an optimal solution, fixes a subset of variables with
confident predictions, and restores feasibility with a dedicated repair algorithm. A final optimization
step is applied to complete the partial assignment. Han et al. (2023) propose a novel predict-
and-search (PaS) framework that adopts the trust region method, which searches for near-optimal
solutions within a well-defined region. Their approach uses a trained graph neural network (GNN)
to predict marginal probabilities of binary variables in a given MIP instance. It then searches for
near-optimal solutions within the trust region using these predictions. Huang et al. (2024a) propose
the ConPaS framework that learns to predict solutions to MIPs with contrastive learning. ConPaS
collects both high-quality solutions as positive samples and low-quality or infeasible solutions as
negative samples, and learns to make discriminative predictions by contrasting these samples. It
then fixes the assignments for a subset of integer variables and solves the resulting reduced MIP to
obtain high-quality solutions. ConPaS was evaluated on four classes of binary MIPs. Most of these
approaches primarily evaluate their algorithms on binary problems. Cai et al. (2025) extend the
PaS framework to parametric MIPs and introduceID-PaS+, an identity-aware learning framework
that enables the ML model to handle heterogeneous variables more effectively. Experiments on
several real-world large-scale problems demonstrate thatID-PaS+consistently outperforms the
state-of-the-art solvers Gurobi and PaS.
5

Optimization Proxies.Optimization proxies have accumulated great success for continuous opti-
mization problems. Tanneau and Van Hentenryck (2024) present dual Lagrangian learning (DLL),
a principled learning methodology for dual conic optimization proxies. The proposed methodology
significantly outperforms a state-of-the-art learning-based method and achieves 1000×speedups
over commercial interior-point solvers with optimality gaps under 0.5% on average. However, they
encounter feasibility and training challenges when discrete variables are present (Tran et al., 2021;
Fioretto et al., 2020; Detassis et al., 2021; Guan et al., 2026). Learning models for discrete opti-
mization problems lack useful gradients because the arg-max operator is piecewise constant, which
complicates backpropagation. One way to address this is to construct effective approximations of
the gradients, e.g., by generating continuous surrogates of the MIP to facilitate effective training
(Ferber et al., 2020; Kotary et al., 2021; Donti et al., 2017; Wilder et al., 2019). This paper combines
a partial proxy with a correction phase to handle the discrete context. The focus is on the backdoor
variablesx i, i∈ B, which drive complexity. Then, the solution is completed. The correction phase
restores feasibility in case the obtained solution is infeasible.
Learning to Optimize.Learning to optimize encompasses a wealth of approaches, many of which
are reviewed in Lodi and Zarpellon (2017), Bengio et al. (2021), and Kotary et al. (2021). They
include techniques to guide search decisions in branch-and-bound/cut solvers (Zarpellon et al., 2021;
Gasse et al., 2019; Gupta et al., 2020; Tang et al., 2020) and direct the application of primal heuris-
tics within branch-and-bound (Khalil et al. (2017); Chmiela et al. (2021); Bengio et al. (2020); Song
et al. (2020); Ye et al. (2026)). Khalil et al. (2016) highlight that, beyond the supervised learning
approaches prevalent in this context, reinforcement learning formulations are worth exploring due
to the sequential nature of the variable selection task. Aligned with this observation, Akhlaghi et al.
(2025) implement a novel approach that combines the benefits of supervised learning and deep re-
inforcement learning. They proposePROPEL, a new framework that integrates optimization with
both supervised and deep reinforcement learning (DRL) to reduce the search space significantly.
Although it differs from these studies,PROPELshares some similarities with those focusing on
variable selection strategies (Khalil et al. (2016); Alvarez et al. (2017); Balcan et al. (2018)).PRO-
PELuses supervised learning not to predict the values of all integer variables, but to identify the
variables fixed to zero in the optimal solution.PROPELdrew inspiration from Park et al. (2023),
6

but differs in two key aspects. First, it fixes only the variables to zero, leaving the nonzero integer
variables free. Second, it uses deep reinforcement learning to determine which variables to unfix to
obtain the desired optimality target.
Paper Positioning.This work lies at the intersection of learning-based MIP acceleration and the
backdoor literature in combinatorial optimization. The first stream learns solution information or
solver decisions for MIPs. ThePROPELframework is the closest to this research: 1) it is the first
framework that fuses OR and ML for industrial supply chain planning, 2) it considers problems with
arbitrary integers, and 3) it is not restricted to graph-based problems and applies to standard MIP
formulations. However, it focuses only on predicting variables that take the value 0 amongxi ∈ I
and does not consider the concept ofbackdoor. Furthermore,PROPELhas been evaluated in a
single case study of industrial supply chain planning. The authors highlight the need to consider
other classes of applications beyond supply chain planning and other solution techniques for both
stages in thePROPELframework, and the potential for even larger problems than the supply
chain planning instances (Akhlaghi et al., 2025).
The second stream studies backdoors as structural explanations for solver performance. Back-
doors were originally introduced in the Boolean satisfiability problem (SAT) and the constraint
satisfaction problem (CSP) as sets of variables whose instantiation makes the remaining problem
tractable (Gomes et al., 2000; Williams et al., 2003). This idea was later extended to optimization,
where different notions of feasibility and optimality backdoors were proposed for combinatorial op-
timization and mixed-integer programming (Dilkina et al., 2007, 2009). More recent work learns
effective MILP backdoors using ranking or contrastive learning, but these methods use the predicted
backdoor to guide branching decisions inside branch-and-bound rather than to predict variable as-
signments or domains (Khalil et al., 2022b; Cai et al., 2024).
BIPCdiffers from both streams. It identifies a stable computational backdoor at the level of
a parametric MIP family, learns values or intervals for the backdoor variables, and uses these
predictions to construct a reduced optimization problem that is then completed and corrected.
Thus, the backdoor inBIPCis not merely a branching guide. It is the interface between learning
and optimization.
BIPCextendsPROPEL along six axes: 1)Backdoor Variables.BIPCis organized around
7

the concept of backdoor: it identifies a backdoor for a parametric MIP and organizes the prediction
phase around this backdoor. 2)Prediction.BIPCpredicts not only zero-valued variables; it also
predicts the values or restricted domains for non-zero variables, 3)Real Case Studies.BIPCis
evaluated with five different large-scale real-world applications, 4)Scalability.This paper tackles
problems with millions of variables and constraints, addressing problem sizes that are significantly
larger than those considered in the existing literature, 5)Transferability.This research broadens
the class of MIPs and applications that can benefit the fusion of OR and ML to five applications,
and 6)Feasible and High-Quality Solutions.This research reduces the size of the search space
by focusing on the backdoor variables and uses correction mechanisms to decide which variables to
relax, potentially enhancing feasibility and near-optimality.
To the best of the authors’ knowledge,BIPCis the first framework to combine backdoor identi-
fication, value or interval prediction, and optimization-based completion for large-scale parametric
MIPs with general integer variables.
3 Overview of theBIPCFramework
Consider the parametric mixed-integer optimization problem
ϕ(P) = argmin{c ⊤x|Ax≤b, x∈R n, xi ∈Z∀i∈ I},
where multiple instances share the same structural formulation but differ in the instance data
P= (A,b,c)withA∈R m×n,b∈R m,c∈R n, andI ⊆ {1, . . . , n}denotes the index set of general
integer variables. The instance data is taken from a distributionD, learned from historical data
and/or forecasts.
TheBIPCframework assumes that a subsetB ⊆ Iof variables drives most of the complexity in
solving instances ofϕ. These variables are often called abackdoorin the artificial intelligence (AI)
literature, and this article adopts this terminology. Informally speaking,BIPCfirst identifies this
backdoor using a reference instance and then develops ML models to predict their values.BIPC
then solves an optimization problem to complete this partial solution.
More precisely,BIPCconsists of three phases: (I) backdoor identification, (II) prediction, and
8

Figure 1: TheBIPCFramework.
(III) completion and correction. The identification phase tries to discover the backdoorB, which is
partitioned into two sets:Bf andB b. The prediction phase builds ML models that predict, for an
instanceP, the values of the variables fromBf in the optimal solutionϕ(P)and intervals for the
variables fromBb which contain the optimal solution. The completion and correction phase uses the
ML models and solves a reduced optimization problem where the variables inBf are fixed to their
predicted values and the variables inBb are constrained to be within their predicted intervals. This
reduced problem can be infeasible and suboptimal, in which this phase applies corrections to the
predictions until the problem becomes feasible and satisfies the optimality tolerance. Importantly,
phases I and II are performed offline using the distributionD(training time), while phase III is
executed online for new instances (inference time). The rest of this section goes into more details
of each of these phases. A visual description ofBIPCis given in Figure 1.
9

Backdoor Identification.The identification phase aims at finding the backdoorB.BIPCas-
sumes the availability of a reference instancePr and that the backdoor remains essentially the same
for all instances of distributionD. This assumption is motivated by many practical optimization set-
tings in which the same class of strategic decisions repeatedly drives computational complexity, even
as the instance data changes over time. For example, in facility-location problems, facility-opening
variables often determine the overall structure of the solution. In production planning, production
quantities across products and periods typically drive most operational decisions. In network design
problems, arc activation or flow variables frequently dominate the combinatorial complexity. As a
result, while parameter values may vary from one instance to another, the variable family acting as
the backdoor often remains unchanged. Under this assumption, the backdoor identified from the
reference instance can be used throughout the learning and optimization phases.
The identification phase first partitions the set of variablesIinto{I 1, . . . ,Im}based on the
structure ofϕ. It then solves the reference instanceϕ(P r)to obtain a reference solutionx r. The
goal of the identification phase is to determine which subsetIk is a potential backdoor. To identify
this subset,BIPCsolvesmreduced optimization problems, one for each subset. The optimization
problem associated with subsetIk (1≤k≤m)is the instanceϕ(P r)where each variablex j inI k
is fixed to its value in the reference solutionxr, i.e.,x j =x r j. Since the objective ofBIPCis to
accelerate optimization, the subset for which an optimal solution is found the fastest is considered
the backdoor. The pseudo-code of the backdoor identification is given in Algorithm 1. It uses a
functionϕ(P, S)which returns a pair(x ∗, t∗)wherex ∗ is an optimal solution to instancePwith
additional constraintsSandt ∗ is the computation time of the optimization.
The Learning Phase.Given a backdoorB, the learning phase starts by partitioning its variables
intoB f andB b. It then learns two ML modelsMf andM b forB f andB b respectively.M f learns
the mappingϕbut only for the variables inBf.M b learns to predict intervals for the variables in
Bb which contain the optimal solutions for a given instance.Mb is a classification problem where
the domains of the variables inBb have been partitioned into a set of intervals.
Completion and Correction.At inference time, given a new instanceP,BIPCusesM f and
Mb to predict the values and intervals forBf andB b in the optimal solutionϕ(P). For instanceP,
10

Algorithm 1:Phase I: The Backdoor Identification Procedure.
Input:ϕ,P r,{I 1, ...,Im}
1t ∗ =∞
2x r =ϕ(P r)
3fori∈ {1, ..., m}do
4S={x k =x r k |k∈ Ii}
5(x i, ti)=ϕ(P r, S)
6ift i < t∗ then
7t ∗ =t i
8i ∗ =i
9end
10end
11returnI i∗
BIPCthen solves the reduced optimization problem
ϕ(P,{x k = ˆxk(P)|k∈ B f } ∪ {xk ∈ ˆDk(P)|k∈ Bb})
which fixes each variablexk inB f to its predicted valueˆxk(P)and constrains each variablexk inB b
to be in its predicted intervalsˆDk(P). This reduced problem may be infeasible or suboptimal, in
which case a correction phase is applied. The correction selectively relaxes a subset of variables in
B, restoring feasibility while preserving as much of the predictions as possible. Variables inBf are
relaxed by removing their assigned values. Variables inBb are relaxed by enlarging their intervals.
Since the design of the ML models and correction mechanisms is problem-dependent, the next
section focuses on the taxonomy and methodology used in theBIPCframework to specify the
modeling choices, feature design, and algorithmic strategies used for the three phases across different
problem classes.
4 Taxonomy and Methodology
Before detailing the methodology for predicting and correcting the backdoor, this section introduces
a conceptual taxonomy that organizes model and strategy types. The taxonomy highlights the key
factors underlying the design space of Phases II and III, providing a systematic basis for selecting
appropriate ML models and correction mechanisms within theBIPCframework. The section
presents the taxonomy first before outlining the methodology for designing the ML models and
11

correction mechanisms.
4.1 Taxonomy of Models and Strategies
To systematically address the diversity of problem instances and guide the design of Phases II and
III, theBIPCtaxonomy classifies instances along three dimensions:problem size,variable type, and
feature type(see Figure 2).
Problem Size.This captures the scale of the problems which are divided into two classes:
•Medium-Scale (P 1): Problems with a moderate number of variables, i.e., problems that can
be handled effectively by a single predictive model.
•Large-Scale (P 2): Problems with a very large number of variables, i.e., problems whose scale
motivates variable-wise prediction to improve scalability.
Variable Type.This captures the nature of backdoor variables, which are divided into two classes:
•Bounded-Range (V 1): binary and integer variables with a limited domain.
•Wide-Range (V 2): Integer variables with large domains.
Feature Type.This captures the choice of input features, which are divided into two classes:
•Without Domain-Specific Features (F1): Models only rely on generic instance data, such as
the constraint matrix, objective coefficients, relaxation objective, etc.
•With Domain-Specific Features (F2): Models augment generic instance features with addi-
tional features informed by domain knowledge.
This taxonomy provides a structured framework for mapping problem characteristics to ML models
and correction strategies, allowing for systematic design choices in Phases II and III. The next
subsection discusses the methodology for constructing, training, and applying the ML models, as
well as the associated correction mechanisms, based on this taxonomy.
4.2 Methodology for Phases II and III
Building on the taxonomy above, the methodology for constructing and applying the ML model
(Phase II) and the correction mechanism (Phase III) is guided by problem size, variable type, and
12

V1
V2
P1
P2
F1
F2
Variable TypeProblem Size
Feature Type
Figure 2: Visualization of theBIPCframework taxonomy across three dimensions: variable type
(V1,V 2), problem size (P1,P 2), and feature type (F1,F 2). Each colored cube corresponds to a
distinct configuration of the taxonomy.
ID Color Code Architecture Type Feature Correction
1 OrangeP1V1F1G V P GF SR
2 GrayP1V1F2G V P CF SR
3 YellowP1V2F1G V P&IP GF SR&BA
4 PinkP1V2F2G V P&IP CF SR&BA
5 BlueP2V1F1V W V P GF SR
6 GreenP2V1F2V W V P CF SR
7 RedP2V2F1V W V P&IP GF SR&BA
8 PurpleP2V2F2V W V P&IP CF SR&BA
Table 4.1: Mapping of colored cubes in Figure 2 to Phases II and III settings. Phase II includes
ML model architecture, type, and features. Phase III indicates the correction strategy.
feature type. The following summary outlines the general approach, highlighting how these three
dimensions influence the choice of the strategies. The choices are summarized in Table 4.1.
ML Architecture.The design of the ML models depends on the problem size:
•Global Model (G): For medium-scale problems (P 1), a single model predicts all variables
simultaneously, ensuring consistency across variable interactions.
•Variable-wise Model (V W): For large-scale problems (P 2), a separate model per variable
captures individual variable behaviors, allowing scalability and specialized architectures at
the cost of losing variable interactions.
Model Type.The treatment of backdoor variables depends on whether they are small or large
13

domains:
•Value Prediction (V P): For problems of typeV1, predicting values is the selected method.
Predicted values are fixed in the reduced problem, and Phase III handles any resulting feasi-
bility issues.
•Interval Prediction (IP): For problems of typeV2, in addition to classifying whether a variable
is zero versus non-zero, the ML model predicts an interval for the value of each variable when
it is non-zero. Rather than estimating exact values, the method learns data-driven bounds that
restrict the domain of non-zero variables in the reduced problem. Phase III then selectively
relaxes these intervals, if needed, to restore feasibility and maintain solution quality.
ML Model Features.Input features influence model accuracy and robustness:
•Generic-Feature Model (GF): Models use only standard instance data, such as constraint
matrices or objective coefficients.
•Customized-Feature Model (CF): Models combine generic features with additional problem-
specific information, such as structural properties, aggregated metrics, or historical solution
patterns.
Correction Mechanism.Phase III ensures robustness regardless of ML model design using the
following strategies:
•Selective Relaxation (SR): Only the subset of predicted variables causing infeasibility or large
optimality gaps is relaxed, preserving the learning model structure as much as possible.
•Bound Adjustment (BA): For wide-range integer variables, the predicted intervals may be
progressively adjusted by expanding their lower and upper bounds, e.g., by incorporating
adjacent intervals, to restore feasibility while keeping predictions informative.
Phase III ofBIPCfocuses only on corrections that act on variable values and their bounds, as
these are the only objects predicted in Phase II. This design ensures methodological alignment and
preserves a clear interpretation of the ML model as defining a reduced optimization problem.
Many real-world large-scale optimization problems are sparse, with most backdoors equal to zero
at optimality. In such cases, the primary challenge is correctly identifying the non-zero variables,
14

as wrong predictions on zero-valued variables typically have limited impact. Accordingly, Phase III
corrections focus on wrongly predicted non-zeros, i.e., either by relaxing incorrectly fixed variables
or adjusting their bounds, while largely preserving the ML structure for zero-valued variables.
The proposed methodology enablesBIPCto efficiently predict and correct backdoor variables
across diverse parametric mixed-integer optimization problems. The taxonomy in Section 4.1 guides
these design decisions and maps them to the colored cubes in Figure 2, providing a clear reference
for Phases II and III.
5 The ML Models
This section discusses the learning task, supervised learning, and the reduced MIP problem. The
ML models use a set of labeled instances{(Pk, ϕ(Pk))}K k=1 drawn from distributionD.
5.1 Variables with Bounded Domains
BIPCuses supervised learning with a cross-entropy loss to predict the values of variables inBf.
Given a domainD i for variablex i and an instanceP, modelM f returns a (softmax) probability
distributionM f (P, xi)overD i. The loss function for variablexi and instancePis given by
Lf i (P) =− X
v∈Di
1{ϕ(P) i =v}log(M f (P, xi)v)
5.2 Variables with Large Domains
For variables inBb with large domains,BIPCuses two ML models:M 0 b andM I b. ModelM 0 b is a
binary classifier that determines whether a variable inBb is zero. ModelM0 b also uses a cross-entropy
loss for each variablexi, i.e.,
Lb i (P) =− X
v∈{0,1}
1{ψ(P) i =v}log(M 0 b (P, xi)v)
where
ψ(P) i :=



0,ifϕ(P) i = 0,
1,otherwise.
15

ModelM I b predicts an interval (or domain) for each of the variables inBb that are not predicted
to be zero in the optimal solution of an instance.BIPCpartitions the domainDi of each variable
xi ∈ Bb into a set of intervals, i.e.,Ii ={[l 1 i , u1 i ], . . . ,[lp i , up i ]}.Given a domainD i for variablexi and
an instanceP, modelM I b returns a (softmax) probability distribution overIi, whereM I b (P, xi)j
denotes the probability that optimal solutionϕ(P)i lies in[l j i , uj i ]. Again, modelMI b is trained with
a cross-entropy loss, i.e.,
LI i (P) =−
pX
j=1
1{ϕ(P) i ∈[l j i , uj i ]}log(M I b (P, xi)j)
5.3 Architecture
The deep neural net (DNN) architectures used for both classification and interval prediction are
designed with problem size in mind. For medium-scale problems (P1) with a moderate number of
backdoor variables, a single global model predicts all variables simultaneously, capturing dependen-
cies and interactions across variables, while remaining computationally efficient. In contrast, for
large-scale problems (P2) with many backdoor variables, a separate model is trained for each vari-
able. This approach enables scalability and the use of specialized architectures or hyperparameters
for each variable, which is particularly useful when variables differ in sparsity patterns or range.
In addition to problem size, the choice of input features influences model design. All DNNs can
be trained using only generic instance-level data, such as the constraint matrixAand objective
coefficientsc. When available, domain-specific features can be incorporated to improve predictive
accuracy, reducing dependencies on Phase III corrections. This design ensures that the architecture
is flexible and consistent across value and interval prediction tasks in Phase II.
These predictions, whether obtained from global or variable-wise DNNs and based on generic
or customized features, define the reduced optimization problem solved in Phase III and therefore
constitute the interface between learning and optimization in theBIPCframework.
16

6 The Reduced MIP Model and the Completion Phase
At inference time,BIPCpredicts the valueˆxi(P)of variablex i inB f for an instancePby selecting
the most likely value, i.e.,
ˆxi(P)∈argmax
v∈Di
Mf (P, xi)v.
BIPCfixesthesevariablestotheirpredictedvalueinthereducedoptimizationproblem. Forvariable
xi inB b and instanceP,BIPCfirst predicts whether the variable is zero in the optimal solution of
P, i.e.,
ˆzi(P)∈argmax
v∈{0,1}
M0 b (P, xi)v.
Ifˆzi(P) = 0, variablex i is fixed to zero in the reduced optimization problem. Otherwise,BIPC
selects the most likely interval for variablexi, i.e.,
bdi(P)∈argmax
j∈{1,...,p}
MI b (P, xi)j.
Variablex i is constrained to be in[lj i , uj i ], withj= bdi(P)in the reduced optimization problem.
The initial reduced optimization problem ofBIPCis depicted in Figure 3: it uses the predictions
listed above to constrain the backdoor variables. All other variables remain free and constrained
within their initial domains. Solvingϕr(P)yields a completed solution¯x, which may subsequently
be corrected in case of infeasibility or significant sub-optimality. The reduced optimization problem
is the core mechanism through whichBIPCcombines learning and optimization: the ML models
restrict the search space through backdoor predictions, while optimization completes the remaining
decisions and preserves feasibility.
7 The Correction Phase
Phase II typically yields reduced MIP problems whose solutions are feasible and near-optimal
(Akhlaghi et al., 2025). Nevertheless, in some instances, fixing or bounding the backdoor variables
can produce infeasible solutions or larger-than-desired optimality gaps. To address this, Phase III
introduces a correction mechanism that selectively relaxes or adjusts variable bounds. This ensures
17

ϕr(P) = argmin
x
c⊤x
s.t.Ax≤b,
xi = ˆxi(P),∀i∈ B f ,
xi = 0∀i∈ B b : ˆzi(P) = 0
lj i ≤x i ≤u j i ,∀i∈ B b, j= bdi(P)
xi ∈Z,∀i∈ I,
xi ∈R,∀i /∈ I,
Figure 3: The Core Reduced Optimization Problem ofBIPC.
feasibility and improves solution quality, while preserving the structural guidance provided by Phase
II. This section discusses how to relax subsets of fixed variables and adjust their intervals.
7.1 Selective Relaxation
Selective relaxation targets a subset of variables initially fixed by the ML model, but they are likely
causing infeasibility or suboptimality. DefineUf (P)⊆ Bas the subset selected for relaxation. The
selectively relaxed problem is then
ϕsr(P) = argmin
x
c⊤x
s.t.Ax≤b,
xi = ˆxi(P),∀i∈ B f \ Uf (P),
xi = 0∀i∈ B b \ Uf (P) : ˆzi(P) = 0
lj i ≤x i ≤u j i ,∀i∈ B b, j= bdi(P)
xi ∈Z,∀i∈ I,
xi ∈R,∀i /∈ I,
Techniques for selectingUf (P)include greedy heuristics based on infeasibility or constraint viola-
tions, solver sensitivity analysis using dual or reduced-cost information, and ML models predicting
which fixed variables are likely problematic.
18

7.2 Bound Adjustment
For wide-range backdoor variables predicted as active (non-zero), the predicted intervals may be too
restrictive. The bound adjustment procedure expands the intervals for a subsetUb(P)of variables,
while leaving the remaining variables unchanged. Let[˜lj i ,˜uj i ]denote the adjusted bounds fori∈ Ub.
The bound-adjusted problem is then
ϕba(P) = argmin
x
c⊤x
s.t.Ax≤b,
xi = ˆxi(P),∀i∈ B f ,
xi = 0∀i∈ B b : ˆzi(P) = 0
lj i ≤x i ≤u j i ,∀i∈ B b \ Ub(P), j= bdi(P)
˜lj i ≤x i ≤˜uj i ,∀i∈ U b(P), j= bdi(P)
xi ∈Z,∀i∈ I,
xi ∈R,∀i /∈ I,
Common strategies for selectingU b(P)and adjusting bounds include threshold-based relaxation
using historical solution statistics, solver-guided iterative expansion until feasibility is achieved, and
learning-based methods that predict effective bound expansions.
If both selective relaxation and bound adjustment are applied, the resulting reduced problem
incorporates both modifications simultaneously, with variables inUf (P)relaxed and variables in
Ub(P)having their bounds updated, yielding a combined correction model that preserves feasibility
while leveraging the ML predictions.
8 Experimental Design
This section describes the general characteristics of the test instances, the computational setting,
and implementation details.
19

8.1 Case Studies
Thefirstcasestudyisdrawnfromthemiddle-mileconsolidationnetworkdesignproblem(MMCNP).
The MMCNP focuses on planning transportation capacity from vendors to fulfillment centers (FCs)
and last-mile delivery (LMDs) centers, within required lead times. Shipments must be routed and
consolidated into scheduled loads to ensure efficient delivery. The planner must decide which con-
nections to operate, how much capacity to allocate, and how to group shipments so all demand is
delivered on time. The hard setting includes 50 facilities, 2,000 paths, 400 arcs, and 300 commodi-
ties, and the very-hard problem setting includes 200 facilities, 24,000 paths, 1,000 arcs, and 6,000
commodities. In the hard setting, instances are solved on average within 18 hours. In the very-hard
setting, instances do not converge and exhibit an average gap of 5.12% after 24 hours, underscor-
ing the difficulty of these models. Domain-specific features for the MMCNP case include: number
of facilities (vendors, FCs, and LMDs), number of commodities to be transported, total demand
volume aggregated over all commodities, number of direct transportation paths in the network,
and the demand-to-capacity ratio defined as total demand divided by total available transportation
capacity. Phase I reveals that the backdoor variables in the MMCNP case are the integer vari-
ables that capture the number of trucks flowing on each arc. These variables span a small range.
The reader is referred to the original paper for a detailed description of the model and industrial
context (Greening et al., 2023; Huang et al., 2024b).
The second case is drawn from the strategic locomotive assignment problem (SLAP). The SLAP
determines a weekly, repeatable plan for assigning locomotives to a fixed train schedule. The prob-
lem specifies the required inputs, operational constraints, and cost components governing locomotive
movements and work events such as pickups and set-outs. Its main outputs are the weekly loco-
motive flows across the network and the event locations. These strategic decisions, including fleet
sizing and event placement, provide the foundation for subsequent tactical and operational planning.
The hard problem setting includes 1,000 nodes and 40,000 arcs, and the very-hard problem setting
includes 8,000 nodes and 50,000 arcs. In the hard setting, instances reach optimality on average in
five hours. In the very-hard setting, instances are more demanding and do not close the gap even
after 24 hours, with an average gap of 0.03%. Domain-specific features for the SLAP include: the
number of locomotives, the number of arcs, the number of trains, the length of the planning horizon
20

(number of periods), the total initial locomotive inventory, and the average number of locomotives
per train. Phase I reveals that the backdoor variables in the SLAP case are the integer variables that
capture the number of locomotives on each arc. These variables span a small range. The reader is
referred to the original paper for a detailed description of the industrial context (Kim et al., 2025).
The third case is drawn from a course scheduling problem (COURSE) at Cornell University. The
COURSE determines an optimal assignment of university courses to discrete time blocks. The
problem specifies the required inputs and operational constraints, such as block capacities and
penalty components governing scheduling conflicts between co-enrolled courses. Its main outputs
are the exact placements of courses into time slots. The hard problem setting includes 200 courses
and 12 time slots, and the very-hard problem setting includes 400 courses and 14 time slots. As
the number of courses increases, the density of conflict constraints grows significantly, making the
resulting MIPs substantially more challenging to solve. Domain-specific features for the COURSE
caseinclude: numberofcourses, numberoftimeslots, totalnumberofconflictpairs(co-enrollments),
average conflict degree per course, maximum conflict degree, total penalty weight aggregated over all
conflicts, average penalty per conflict, and conflict density (ratio of realized conflicts to all possible
course pairs). Phase I reveals that the backdoor variables are the binary variables indicating the
assignment of each course to a specific time slot. Since each course must be placed into exactly
one time slot out of all available options, all remaining assignment variables for that course are
strictly zero. The reader is referred to the original paper for a detailed description of the industrial
context (Ye et al., 2025a).
The fourth case study (OCP) is the downstream supply chain of the OCP Group at the Jorf site
in Morocco, one of the world’s largest phosphate-processing and export facilities. OCP is a large-
scale mixed-integer linear programming model that integrates production, storage, and distribution
decisions over a monthly planning horizon with daily resolution. The model captures the physical
flow of materials across a highly interconnected network of conveyors, pipelines, storage units,
and quays, while accounting for a rapidly expanding product portfolio and a demand-driven order
fulfillment process. Key decisions include selecting shipments and loading schedules, developing
daily production plans across multiple processing units, and determining implied inventory and
changeover trajectories. Thehardsetting includes 61 vessels, a 32-day horizon (summer), and a
21

demand of around 1,066,290 tonnes, and thevery-hardsetting includes 58 vessels, a 30-day horizon
(winter), and a demand of around 1,797,910 tonnes. In the hard setting, instances are solved
on average within 1000 seconds. In the very-hard setting, instances do not converge and exhibit
an average gap of 2% after 3 hours, underscoring the difficulty of these models. Domain-specific
features for the OCP case include: number of vessels in the planning horizon, total demand volume
(in tonnes) aggregated over all products and vessels, number of products considered in the instance,
total available storage capacity across all storage units, average production capacity utilization
(ratio of demand to nominal production capacity), and seasonal indicator (e.g., month or quarter
of the year). Phase I reveals that the backdoor variables for the OCP case are the binary variables
assigning the vessels to quays for loading over a specific period. A detailed description of the model
and industrial context is available in (Er Raqabi et al., 2025b).
The fifth case study considers a multi-period, multi-product order fulfillment problem (OFP)
arising in distribution and warehousing operations. The planner must decide which customer orders
to fulfill, how much to ship from each warehouse in each period, and when to activate warehouse
facilities to maximize total profit, defined as revenues minus handling, transportation, and setup
costs. The model incorporates inventory balance constraints, warehouse capacity limits, and order-
specific delivery time windows, resulting in a large-scale mixed-integer linear program. The hard
problem setting includes 80 periods, 100 orders, 6 locations, and 6 products, and the very-hard
problem setting includes 100 periods, 200 orders, 10 locations, and 10 products. In the hard setting,
instances are solved on average within 60 minutes. In the very-hard setting, instances are solved
on average within 3 hours. Domain-specific features for the OFP include: the number of customer
orders, the number of warehouse locations, the number of products, the length of the planning hori-
zon (number of periods), the total initial inventory aggregated across all products and warehouses,
and the average order time-window width measuring delivery flexibility. Phase I reveals that the
backdoors for the OFP case are the integer variables that capture the quantities to produce for each
product in each period and each facility. These variables span a large range. The reader is referred
to the original paper for a detailed description of the model and industrial context (Ye et al., 2025b).
Table 8.1 overviews instances in each setting for each case study and reports the number of
constraints, the number of continuous variables, the number of binary variables, the number of
22

Problem Constraints Continuous Binary Integer Avg. Zeros
MMCNP Hard 643 - 2,540 357 87%
MMCNP Very-Hard 4,361 - 23,984 1,135 85%
SLAP Hard 80,982 - 8 77,946 98%
SLAP Very-Hard 82,996 - 20 77,032 95%
COURSE Hard 30,173 - 43,488 173 95%
COURSE Very-Hard 53,205 - 79,968 229 90%
OCP Hard 772,383 925,502 11,155 - 96%
OCP Very-Hard 370,827 435,536 15,237 - 92%
OFP Hard 143,892 2,880 580 288,580 90%
OFP Very-Hard 1,012,900 10,000 1,200 2,001,200 91%
Table 8.1: Instances
Taxonomy MMCNP SLAP COURSE OCP OFP Hard Very-Hard Hard Very-Hard Hard Very-Hard Hard Very-Hard Hard Very-Hard
Problem Size P1 P1 P1 P1 P1 P1 P2 P2 P2 P2
Variable Type V1 V1 V1 V1 V1 V1 V1 V1 V2 V2
Feature Type F1 /F 2 F1 /F 2 F1 /F 2 F1 /F 2 F1 /F 2 F1 /F 2 F1 /F 2 F1 /F 2 F1 /F 2 F1 /F 2
Table 8.2: Case Studies Classification based on the Taxonomy
integer variables, and the average percentage of zero-valued backdoor variables in the optimal so-
lution. These case studies are well-suited to evaluating the proposedBIPCframework, as they
represent various cases discussed in the taxonomy as summarized in Table 8.2. Throughout this
paper, problems with fewer than 100,000 backdoor variables are classified as medium-scale (P1),
whereas problems with at least 100,000 backdoor variables are classified as large-scale (P2). This
threshold was selected empirically based on the scalability of the learning models and serves as a
guideline for choosing between global and variable-wise prediction architectures.
8.2 Experimental Setting
Data Generation.For each case study, training and test instances are constructed from two
reference problem instances that represent different levels of difficulty, referred to ashardandvery-
hard. These reference instances are obtained from realistic operational data settings and serve as
representative baselines for the underlying optimization problems.
Throughout the experiments, all generated instances preserve the structural formulation of the
reference problem, while demand parameters are perturbed to create diverse operational scenarios
followingaprocedureinspiredbyAkhlaghietal.(2025). Demanduncertaintyinreal-worldoptimiza-
23

tion problems typically exhibits both positive correlations, driven by factors such as seasonality and
market trends, and negative correlations arising from substitution effects or resource competition.
The data generation process aims at capturing these characteristics while maintaining consistency
with observed operational patterns. The perturbed datasets reflect realistic operational variability
and produce integer variables with diverse activation patterns and wide value ranges, making them
well-suited for evaluating the learning and correction components of theBIPCframework.
Computational Setting.For each case study, a total of 600 MIP instances were generated
following the procedure described above. These instances were split into 400 training instances,
100 validation instances, and 100 testing instances. The training set was used to fit the supervised
learning models during Phase II, the validation set was used for hyperparameter tuning and model
selection, and the testing set was reserved exclusively for performance evaluation.
The DNNs used for both classification and interval prediction in Phase II are fully connected
multilayer perceptrons with ReLU activation functions. Hyperparameters were selected via grid
searchoverlearningrates{0.001,0.005}, numberofhiddenlayers{3,4}, andhiddenlayerdimensions
{32,64,128}. The number of instance-level and variable-level features used determines the input
dimension of each network. All models were trained for 100 epochs with a batch size of 32 using the
Adam optimizer. Model selection was performed based on validation performance, and final results
are reported on held-out test sets.
Classification models were evaluated using standard metrics such as F1 score and confusion matri-
ces, while interval prediction models were assessed using classification accuracy over the predicted
buckets. For medium-scale problems (P1), a single global model was trained for both classifica-
tion and interval prediction tasks. In contrast, for large-scale problems (P2), separate variable-wise
models were trained for each backdoor variable.
All learning models were implemented in Python using PyTorch. Experiments were conducted
using Gurobi Optimizer version 13.0.0. All optimization runs were executed on a machine equipped
with an Intel® CoreTM i7–8700 processor operating at 3.20GHz, with 64GiB of system memory,
running Oracle Linux Server release 7.7.
The reduced and corrected MIP models were solved using 32 CPU threads. The termination
24

criterion was defined by setting the Gurobi parameterMIPGapto 0.5%, andMIPFocuswas set to 1
to encourage rapid identification of high-quality feasible solutions. All reported runtimes correspond
to real (wall-clock) time. Unless otherwise stated, all reported objective values correspond to the
best feasible solution returned by the solver within the allotted time limit.
Metrics.It is worth highlighting that strong predictive accuracy does not necessarily translate into
high-quality optimization decisions (Elmachtoub et al., 2020). Accordingly, the evaluation focuses
exclusively on the quality of solutions obtained by solving the reduced and corrected MIP models
produced by theBIPCframework, rather than on standalone ML performance metrics.
Solution quality is measured using two standard optimization metrics. Theprimal gap(PG) is
defined as the relative difference between the objective value of the best feasible solution found by a
method and the best known bound, evaluated at termination. This metric captures the final solution
quality achieved within the computational budget. Formally, letzprimal(t)denote the objective value
of the best feasible solution found up to timet, and letz bound(t)denote the best available dual
bound at timet. At termination timeT, theprimal gapis defined as
PrimalGap(T) :=

zprimal(T)−z bound(T)

max{|zprimal(T)|, ϵ} ,
whereϵ >0is a small constant introduced to avoid division by zero.
In addition, the results report theprimal integral(PI), which measures the time-integrated primal
gap over the entire solve horizon, thereby accounting for both solution quality and the speed at
which high-quality feasible solutions are identified. Together, these metrics provide a comprehensive
assessment of the decision-making effectiveness of theBIPCframework, capturing not only the
quality of final solutions but also the temporal behavior of the optimization process relative to the
baseline. Formally:
PrimalIntegral(T) :=
Z T
0

zprimal(t)−z bound(t)

max{|zprimal(t)|, ϵ} dt.
Comparison.TheBIPCframework is benchmarked against state-of-the-art solution approaches
to assess its ability to deliver high-quality solutions under limited computational budgets. This com-
parison highlights the trade-off between solution quality and runtime and illustrates how learning-
25

augmented optimization can outperform conventional solvers on large-scale and computationally
challenging instances. The considered methods are:
•MIP:Directly solving the full model using a state-of-the-art MIP solver, i.e., Gurobi with
default parameter settings.
•PROPEL:The learning-augmented optimization framework proposed in Akhlaghi et al.
(2025).
•ID-P aS+:The identity aware predict-and-search introduced in Cai et al. (2025).
Allmethodsareevaluatedunderaruntimelimitof600secondsoverthefivecases: OCP,MMCNP,
OFP, SLAP, and COURSE. For each time budget, solution quality is assessed using the PG at
termination and the PI over the entire solve horizon, thereby jointly evaluating final solution quality
and the speed at which high-quality feasible solutions are obtained. ID-PaS+ does not apply to
OFP because its methodology is restricted to bounded-domain variables and does not support the
wide-range integer variables present in OFP.
9 Computational Results
This section evaluates the computational effectiveness of the proposedBIPCframework through an
extensive experimental study. First, theBIPCperformance is assessed relative to state-of-the-art
approaches. Then, the computational performance of eachBIPCphase is quantified. Last, several
managerial insights relevant to large-scale decision-making contexts are highlighted. The detailed
backdoor identification (Phase 1) is provided in Appendix A.
9.1 Comparison with State-of-Art
Table 9.1 shows the PG and PI averaged over 100 test instances for each benchmark, and reports
the mean, standard deviation, and the number of instances each method wins. The best-performing
entries are highlighted in bold for clarity.
Across all problem families and difficulty levels,BIPCconsistently achieves the lowest mean PG
and PI, often by a substantial margin. In the very-hard settings, the improvement is particularly
pronounced. For example, in OCP Very-Hard,BIPCreduces the mean PG from 1.72 and 1.98
26

Problem Method PG (%)↓ PI↓ Mean Std Dev Wins Mean Std Dev Wins
MMCNP Hard
MIP 0.16 0.25 10 3.30 3.28 0
PROPEL 0.09 0.15 12 2.12 2.22 6
ID-PaS+ 0.07 0.17 18 1.94 1.99 10
BIPC 0.05 0.10 60 0.51 1.45 84
MMCNP Very-Hard
MIP 1.05 0.49 2 35.11 5.91 0
PROPEL 0.15 0.27 14 12.33 2.45 9
ID-PaS+ 0.12 0.23 14 11.27 2.67 9
BIPC 0.04 0.08 70 2.70 0.67 82
SLAP Hard
MIP 0.049 0.054 9 1.36 0.59 0
PROPEL 0.028 0.041 10 1.07 0.25 8
ID-PaS+ 0.024 0.032 13 1.16 0.43 7
BIPC 0.011 0.014 68 0.42 0.16 85
SLAP Very-Hard
MIP 0.18 0.21 7 7.85 2.12 0
PROPEL 0.15 0.33 6 6.12 1.18 10
ID-PaS+ 0.13 0.15 11 5.36 1.55 10
BIPC 0.08 0.07 76 1.24 0.44 80
COURSE Hard
MIP 0.023 0.010 2 1.97 1.78 1
PROPEL 0.013 0.008 18 1.90 1.59 3
ID-PaS+ 0.004 0.003 25 1.75 1.71 5
BIPC 0.004 0.002 55 1.43 1.55 91
COURSE Very-Hard
MIP 0.26 0.44 3 9.87 6.35 0
PROPEL 0.13 0.31 6 9.14 5.03 3
ID-PaS+ 0.07 0.23 31 7.61 4.56 10
BIPC 0.05 0.11 60 6.76 4.22 87
OCP Hard
MIP 0.09 0.42 0 44.53 8.33 0
PROPEL 0.08 0.13 15 11.72 2.97 7
ID-PaS+ 0.08 0.08 20 11.13 3.11 8
BIPC 0.07 0.05 65 3.21 1.56 85
OCP Very-Hard
MIP 2.61 0.78 3 41.78 6.41 2
PROPEL 1.72 0.23 16 9.94 3.42 10
ID-PaS+ 1.98 0.15 10 9.28 3.55 8
BIPC 0.80 0.03 71 3.79 1.22 80
OFP Hard
MIP 0.30 0.41 4 4.71 1.32 0
PROPEL 0.20 0.31 15 3.12 0.75 5
ID-PaS+ - - - - - -
BIPC 0.09 0.05 81 0.79 0.27 95
OFP Very-Hard
MIP 1.14 0.25 3 8.11 1.12 0
PROPEL 0.78 0.45 18 4.44 1.02 12
ID-PaS+ - - - - - -
BIPC 0.13 0.08 79 1.16 0.25 88
Table 9.1: Performance comparison of baseline and proposed methods across benchmark instances
in terms of PG and PI. Results are reported as mean, standard deviation, and number of best-
performing instances (Wins) over 100 instances per benchmark. Lower values indicate better per-
formance.
27

forPROPELandID-PaS+, and 2.61 for MIP, to 0.80, while simultaneously decreasing the PI to
3.79 compared to values between 9 and 42 for competing methods. This demonstrates thatBIPC
improves both final solution quality and the speed at which high-quality incumbents are identified.
In hard settings, all learning-based methods remain competitive, yetBIPCstill achieves the smallest
PG and PI, and exhibits lower variability. This indicates not only improved solution quality but
also greater stability across instances. The reduction in PI is especially notable, showing thatBIPC
consistently identifies strong feasible solutions early in the search process. A Wilcoxon signed-rank
test (p <0.01) (Woolson, 2007) confirms that all reported performance differences betweenBIPC
and the baselines are statistically significant, validating the robustness of the observed improvements
across the various cases.
From an algorithmic perspective, the distinction between predicting zeros among all integer vari-
ables and predicting both zeros and non-zeros on a selected subset of backdoor variables reflects two
fundamentally different mechanisms for reducing combinatorial complexity. Predicting zeros across
the full set of integer variables, as done inPROPELandID-PaS+, follows a conservative pruning
strategy. By identifying likely inactive variables, this strategy reduces the search space while pre-
serving flexibility. The solver determines the remaining assignments. This strategy exploits sparsity,
which is common in many integer programs, and can substantially reduce the feasible region when
zero predictions are accurate. However, it provides limited structural guidance, since the solver
must still determine which of the remaining variables should take positive values.
In contrast, predicting both zeros and non-zeros on a targeted subset of backdoor variables, as in
BIPC, directly addresses the structural drivers of difficulty. Rather than distributing predictions
across the entire integer space, this strategy concentrates on variables that encode the core combi-
natorial decisions. By fixing both inactive and active assignments within this subset, the method
not only prunes the search space but also shapes it, thereby reducing the effective combinatorial
burden faced by the solver.
The performance trends in Table 9.1 align with this intuition. As instance difficulty increases,
the advantage ofBIPCbecomes more pronounced in both PG and PI. This pattern suggests that
when complexity is driven by a relatively small number of structural decisions, accurately predicting
their values yields stronger simplification than broadly predicting zeros across all integer variables.
28

In easier instances, where sparsity alone may already provide sufficient reduction, the PG between
strategies is smaller, consistent with the more moderate differences observed in the table. Overall,
the relative gains ofBIPCincrease with problem hardness, indicating that ML and structured
parameter selection provide increasingly effective guidance in large and complex search spaces.
9.2 Computational Performance ofBIPC
BIPCPerformance on Instances solved to a PG below 0.05%.Figure 4 shows the PG
over time, averaged over 100 test instances on each benchmark for each of the four methods. The
figure reports the evolution of the PG (in %) over time (0–1000 seconds) on a logarithmic scale for
eight instances across five problem classes (MMCNP, SLAP, COURSE, OCP, and OFP), each in
Hard and Very-Hard variants. Each subfigure compares the four methods by tracking the rate and
magnitude of reduction in the PG.
Acrossalmostallinstances,BIPCexhibitsamarkedlyfasterinitialreductioninthePG.Inseveral
cases (e.g., OCP Hard, MMCNP Hard, SLAP Hard),BIPCreaches sub-1% PGs within the first
100–200 seconds and often stabilizes near 0.01–0.1% well before 600 seconds. This early dominance
indicates thatBIPCis particularly effective at rapidly constructing high-quality feasible solutions.
In contrast, MIP (Gurobi) typically reduces the PG more gradually, with a noticeable delay before
reaching the same low-PG regime.PROPELandID-PaS+consistently outperform the vanilla
MIP baseline in the intermediate time window (roughly 100–400 seconds), often reducing the PG
substantially earlier and sometimes matchingBIPCin final solution quality, though typically not
in early speed.
The performance differences become more pronounced on the Very-Hard instances. For OCP
Very-Hard and OFP Very-Hard, MIP and evenPROPELandID-PaS+tend to plateau at non-
negligible PGs. At the same time,BIPCcontinues to significantly reduce the PG, particularly in
the mid-to-late runtime regime. A similar pattern is observed in MMCNP and SLAP instances,
wherePROPELandID-PaS+consistently improve upon MIP but are slightly less aggressive
in early convergence thanBIPC. Overall, the graphs suggest a clear hierarchy:BIPCdominates
in early feasible-solution quality and often in final PG,PROPELandID-PaS+provide stable
improvements over MIP, and the baseline MIP solver exhibits the slowest PG closure, particularly
29

Problem Instances MIP Completion Correction 1 Correction 2 Correction 3 Correction 4
MMCNP Hard 21 0.41 0.15 0.11 0.07 0.07 0.07
MMCNP Very-Hard 19 1.54 0.12 0.08 0.06 0.06 0.06
SLAP Hard - 0.10 0.03 - - - -
SLAP Very-Hard 16 0.39 0.15 0.11 0.07 0.07 0.07
COURSE Hard - 0.10 0.03 - - - -
COURSE Very-Hard 16 0.39 0.15 0.11 0.07 0.07 0.07
OCP Hard 15 0.51 0.12 0.07 0.07 0.07 0.07
OCP Very-Hard 17 3.39 0.93 0.80 0.80 0.80 0.80
OFP Hard 24 0.71 0.14 0.10 0.07 0.07 -
OFP Very-Hard 26 1.39 0.21 0.15 0.10 0.07 0.07
Table 9.2: Evolution of PG across the proposedBIPCframework, including completion and cor-
rections. Results are averaged over instances not solved within the desired threshold.
as instance difficulty increases.
BIPCPerformance on Instances solved with PG higher than 0.05% or infeasible.
Table 9.2 reports the decomposition of the method into its successive phases: the baseline MIP
configuration, completion, and up to four Correction iterations (Phase III). For each problem class
and difficulty level, the table shows the final PG after a fixed runtime budget, allowing a clear
attribution of performance gains to each stage. The instances range from moderately difficult Hard
cases to substantially more challenging Very-Hard cases, providing a consistent view of how the
refinement mechanism behaves as complexity increases.
The completion accounts for the majority of the improvement, while corrections primarily serve
as a robustness mechanism that recovers from occasional prediction errors and further refines solu-
tion quality. Across all problem classes, the PG decreases substantially from the baseline MIP to
completion. For example, in OCP Very-Hard, the PG decreases from 3.39 to 0.93, and in MMCNP
Very-Hard from 1.54 to 0.12. Similar patterns appear in OFP Very-Hard (1.39 to 0.21) and OCP
Hard (0.51 to 0.12). This shows that most of the performance improvement is already captured by
the completion, which is highly effective at identifying strong regions of the parameter space before
any iterative correction is applied.
The corrections then deliver systematic but diminishing improvements. The first one or two
corrections typically produce the largest additional reductions, while later iterations provide finer
30

Problem
F1 F2
PG (%)↓ PI↓ PG (%)↓ PI↓
Mean Std Dev Mean Std Dev Mean Std Dev Mean Std Dev
MMCNP Hard 0.07 0.14 0.61 1.74 0.05 0.10 0.51 1.45
MMCNP Very-Hard 0.056 0.112 3.24 0.80 0.04 0.08 2.70 0.67
SLAP Hard 0.0154 0.0196 0.50 0.19 0.011 0.014 0.42 0.16
SLAP Very-Hard 0.112 0.098 1.49 0.53 0.08 0.07 1.24 0.44
COURSE Hard 0.008 0.002 1.77 2.01 0.004 0.002 1.43 1.55
COURSE Very-Hard 0.07 0.23 7.12 4.63 0.05 0.11 6.76 4.22
OCP Hard 0.098 0.07 3.85 1.87 0.07 0.05 3.21 1.56
OCP Very-Hard 0.88 0.042 4.55 1.46 0.80 0.03 3.79 1.22
OFP Hard 0.126 0.07 0.95 0.32 0.09 0.05 0.79 0.27
OFP Very-Hard 0.182 0.112 1.39 0.30 0.13 0.08 1.16 0.25
Table 9.3: Impact of feature engineering on ML model performance. Comparison between the
generic feature setF1 and the enriched feature setF2 in terms of PG and PI, reported as mean and
standard deviation across instances.
refinements. In OFP Very-Hard, the PG decreases from 0.21 to 0.07 over three corrections. In
MMCNP Hard, the PG decreases from 0.15 to 0.07 within two corrections. In easier cases, such
as SLAP Hard, the completion alone already yields a very small PG (0.03), making further cor-
rections unnecessary. Overall, the table highlights a two-stage effect: the completion delivers the
dominant improvement, while the correction iterations act as a controlled polishing mechanism that
incrementally consolidates solution quality, especially on the most difficult instances.
By progressively enabling the completion and correction mechanisms, supervised learning and
targeted corrections jointly improve feasibility, optimality, and robustness across problem classes.
Impact of Domain-specific Features.Table 9.3 evaluates the impact of the feature design used
in the ML model. Two feature sets are compared:F1, which includes only generic instance features,
andF 2, which augmentsF 1 with domain-specific features. For each problem class and difficulty
level, the table reports the mean and standard deviation of two performance indicators: the PG
and the PI. This allows assessment not only of average solution quality but also of robustness across
instances.
Across all problem classes and difficulty levels,F2 consistently outperformsF 1 in terms of mean
PG. The improvement is particularly pronounced on Very-Hard instances. For example, in OCP
31

Very-Hard, the mean PG decreases from 0.88 (F1) to 0.80 (F2), and in OFP Very-Hard from
0.182 to 0.13. Similar reductions are observed for MMCNP and SLAP variants. These results
indicate that incorporating domain-specific structure enables the ML model to capture instance
heterogeneity better and select more appropriate parameter configurations. The performance gains
aresystematicratherthanisolated, asF 2 dominatesF 1 ineveryrowofthetable. AWilcoxonsigned-
rank test (p <0.01) (Woolson, 2007) confirms that all reported performance differences between
domain-generic and domain-specific features inBIPCare statistically significant, validating the
robustness of the observed improvements across the five case studies. The benefits of domain-
specific features are more pronounced on the very-hard instances, suggesting that instance-specific
structural information becomes increasingly valuable as combinatorial complexity grows.
9.3 Managerial Insights
The computational study reveals three consistent findings across all five application domains. First,
each parametric MIP family exhibits a small computational backdoor whose fixation dramatically
reduces solution effort, providing empirical evidence that a limited subset of variables drives most
of the optimization complexity. Second, these backdoors are highly sparse, with the vast majority
of backdoor variables taking value zero at optimality and only a small fraction of non-zero variables
determining the key decisions. Third, fixing only the non-zero backdoor variables recovers most
of the computational benefit obtained by fixing the entire backdoor, while fixing only the zero-
valued variables yields substantially weaker improvements. These results suggest that the primary
challenge in large-scale parametric mixed-integer optimization is not predicting all integer variables,
but accurately identifying and predicting the small subset of non-zero backdoor variables that govern
solution quality and computational performance. Collectively, these findings provide the empirical
foundation for theBIPCframework and motivate its predict-complete-correct paradigm.
These computational findings translate into actionable managerial insights. This section discusses
howBIPCsupports faster and more reliable decision-making, identifies critical variables driving
complexity, and enables scalable planning in high-dimensional operational settings.
Faster and more reliable decision support.Across all problem classes,BIPCconsistently re-
duces both the primal gap and the primal integral, indicating not only higher final solution quality
32

but also substantially faster convergence to high-quality feasible plans. From a managerial per-
spective, this means that decision-makers can obtain strong, implementable solutions earlier within
limited planning windows. In time-sensitive operational environments such as port operations, pro-
duction planning, or logistics coordination, earlier access to high-quality plans directly translates
into improved responsiveness, reduced operational risk, and greater confidence in execution.
Focusing on what truly drives complexity.A central insight ofBIPCis that not all decision
variables contribute equally to computational difficulty. Rather than attempting to simplify the
entire model uniformly,BIPCconcentrates on a backdoor, i.e., a subset of structurally critical
variables that drive combinatorial complexity. By accurately predicting both active and inactive
values for backdoor variables,BIPCreshapes the search space around its most influential decisions.
Managerially, this provides a clear message: complexity in large-scale planning problems is often
concentrated in a small number of pivotal choices, such as assignment, sequencing, or allocation
decisions. Identifying and structuring these key drivers enables disproportionate gains in solvability
and performance.
Scalable planning through feature-driven tuning.The effectiveness ofBIPCrelies on inter-
pretable, domain-specific features that summarize instance characteristics such as demand intensity,
resource capacity, structural size, and seasonality. These features serve as a compact representation
of the operational environment and enable the model to adapt its parameter selection to the in-
stance’s difficulty. Importantly, the framework is modular: if additional domain knowledge becomes
available, new features can be incorporated without redesigning the optimization model itself. This
flexibility enables organizations to refine performance as more operational data is collected over
time.
The Elephant and the Bee analogy.Conceptually,BIPCembodies a divide-and-focus phi-
losophy. The large-scale optimization model is like an elephant: powerful, with generic features,
but computationally intensive. The learning component with the domain-specific features acts as
the bee: lightweight, adaptive, and capable of quickly identifying where attention should be di-
rected. By guiding the solver toward structurally critical decisions rather than uniformly reducing
the model, the approach balances robustness with efficiency. This synergy enables organizations to
maintain rich, high-fidelity models while achieving tractable solution times, even as problem size
33

and dimensionality increase.
Overall, the results suggest that data-informed variable prioritization can substantially enhance
thescalabilityofadvancedplanningmodels. Formanagers, thismeansthatcomplex, high-dimensional
decision problems need not be simplified at the modeling stage to remain solvable. Instead, in-
telligent guidance layered on top of detailed optimization models can deliver both realism and
computational performance.
10 Conclusion
This paper introduced theBIPCframework for efficiently solving parametric mixed-integer op-
timization problems by identifying backdoor variables that drive computational complexity and
exploiting this structure through targeted prediction and correction. The framework consists of
three phases: backdoor identification, which analyzes the impact of variable fixing to identify a
backdoor; supervised learning, which predicts values or narrower domains for backdoor variables to
produce a reduced problem that can be solved efficiently; and completion and correction, which re-
store feasibility and improve solution quality when predictions are imperfect. To guide the design of
Phases II and III, a taxonomy was proposed based on problem size, backdoor variable type, and fea-
ture type, providing a systematic map for selecting appropriate modeling and correction strategies.
The methodology leverages this taxonomy to handle binary and general integer variables, sparse
and dense structures, and domain-specific features, thereby balancing computational efficiency with
solution quality.
Computationalexperimentsonfivelarge-scaleapplicationsdemonstratedthattheproposedframe-
work consistently identifies meaningful and stable backdoors corresponding to the primary opera-
tional decisions of each problem. The results show that combining prediction, completion, and
correction can significantly improve solution quality relative to both classical optimization and ex-
isting learning-augmented optimization approaches. In particular, the experiments highlight that
much of the computational complexity of large-scale parametric MIPs is concentrated in a small
subset of strategic variables, and that accurately predicting these variables can dramatically reduce
the effective search space while preserving high-quality solutions.
34

More broadly, the results suggest that learning and optimization are particularly complemen-
tary in repetitive decision-making environments where large numbers of related instances must be
solved over time. By leveraging historical solutions to identify and predict the most influential
decisions,BIPCtransforms optimization from solving each instance independently to exploiting
recurring structural patterns across instances. This perspective provides a scalable pathway for in-
tegrating machine learning into mathematical optimization and establishes a foundation for future
research on adaptive backdoor discovery, richer prediction models, and learning-enhanced optimiza-
tion frameworks for large-scale industrial applications. The present work assumes that instances
share a common structural formulation and differ primarily through parameter perturbations. Ex-
tendingBIPCto variable-size instances, where nodes, arcs, products, or constraints may be added
or removed over time, constitutes an important direction for future research. Such extensions would
require learning representations that generalize across varying optimization structures and could
further broaden the applicability of learning-enhanced optimization in industrial settings.
Acknowledgments
This research was partly supported by the NSF AI Institute for Advances in Optimization (Award
2112533).
References
Akhlaghi, V. E., Zandehshahvar, R., and Van Hentenryck, P. (2025). Propel: Supervised and
reinforcement learning for large-scale supply chain planning.arXiv preprint arXiv:2504.07383.
Alvarez, A. M., Louveaux, Q., and Wehenkel, L. (2017). A machine learning-based approximation
of strong branching.INFORMS Journal on Computing, 29:185–195.
Balcan, M.-F., Dick, T., Sandholm, T., and Vitercik, E. (2018). Learning to branch. In Dy, J.
and Krause, A., editors,Proceedings of the 35th International Conference on Machine Learning,
volume 80 ofProceedings of Machine Learning Research, pages 344–353. PMLR.
Bengio, Y., Frejinger, E., Lodi, A., Patel, R., and Sankaranarayanan, S. (2020). A learning-based
algorithm to quickly compute good primal solutions for stochastic integer programs. InInterna-
tional conference on integration of constraint programming, artificial intelligence, and operations
research, pages 99–111. Springer.
Bengio, Y., Lodi, A., and Prouvost, A. (2021). Machine learning for combinatorial optimization: a
methodological tour d’horizon.European Journal of Operational Research, 290:405–421.
Cai, J., Er Raqabi, E. M., Van Hentenryck, P., and Dilkina, B. (2025). ID-PaS: Identity-aware
predict-and-search for general mixed-integer linear programs.arXiv preprint arXiv:2512.10211.
35

Cai, J., Huang, T., and Dilkina, B. (2024). Learning backdoors for mixed integer linear programs
with contrastive learning.arXiv preprint arXiv:2401.10467.
Cappart, Q., Moisan, T., Rousseau, L.-M., Prémont-Schwarz, I., and Cire, A. A. (2021). Combining
reinforcementlearningandconstraintprogrammingforcombinatorialoptimization. InProceedings
of the AAAI conference on artificial intelligence, volume 35, pages 3677–3687.
Chen, W., Tanneau, M., and Van Hentenryck, P. (2023). End-to-end feasible optimization proxies
for large-scale economic dispatch.IEEE Transactions on Power Systems, 39:4723–4734.
Chmiela, A., Khalil, E., Gleixner, A., Lodi, A., and Pokutta, S. (2021). Learning to schedule
heuristics in branch and bound.Advances in Neural Information Processing Systems, 34:24235–
24246.
Detassis, F., Lombardi, M., and Milano, M. (2021). Teaching the old dog new tricks: Supervised
learning with constraints. InProceedings of the AAAI Conference on Artificial Intelligence, vol-
ume 35, pages 3742–3749.
Dilkina, B., Gomes, C. P., Malitsky, Y., Sabharwal, A., and Sellmann, M. (2009). Backdoors to
combinatorial optimization: Feasibility and optimality. InInternational Conference on Integra-
tion of Constraint Programming, Artificial Intelligence, and Operations Research, pages 56–70.
Springer.
Dilkina, B., Gomes, C. P., and Sabharwal, A. (2007). Tradeoffs in the complexity of backdoor
detection. InInternational Conference on Principles and Practice of Constraint Programming,
pages 256–270. Springer.
Donti, P., Amos, B., and Kolter, J. Z. (2017). Task-based end-to-end model learning in stochastic
optimization.Advances in neural information processing systems, 30.
Donti, P. L., Rolnick, D., and Kolter, J. Z. (2021). Dc3: A learning method for optimization with
hard constraints.arXiv preprint arXiv:2104.12225.
El Balghiti, O., Elmachtoub, A. N., Grigas, P., and Tewari, A. (2019). Generalization bounds in
the predict-then-optimize framework.Advances in neural information processing systems, 32.
Elmachtoub, A. N. and Grigas, P. (2022). Smart “predict, then optimize”.Management Science,
68:9–26.
Elmachtoub, A. N., Liang, J. C. N., and McNellis, R. (2020). Decision trees for decision-making
under the predict-then-optimize framework. InInternational conference on machine learning,
pages 2858–2867. PMLR.
Er Raqabi, E. M. (2024).Primal Methods for Very Large-Scale Optimization. PhD thesis, Poly-
technique Montréal.
Er Raqabi, E. M., Bani, A., Morabit, M., Massé, A. B., Besner, A., Fournier, J., and El Hallaoui, I.
(2025a). A decomposition matheuristic for the transient stability constrained unit commitment
at Hydro-Quebec.IEEE Transactions on Power Systems.
Er Raqabi, E. M., Beljadid, A., Bennouna, M. A., Bennouna, R., Boussaadi, L., El Hachemi, N.,
El Hallaoui, I., Fender, M., Jamali, M. A., Si Hammou, N., and Soumis, F. (2025b). OCP
optimizes its supply chain for Africa.INFORMS Journal on Applied Analytics, 55(6):437–456.
36

Er Raqabi, E. M., Wu, Y., El Hallaoui, I., Soumis, F., et al. (2024). Towards resilience: Primal
large-scale re-optimization.Transportation Research Part E: Logistics and Transportation Review,
192:103819.
Ferber, A., Wilder, B., Dilkina, B., and Tambe, M. (2020). Mipaal: Mixed integer program as a
layer. InProceedings of the AAAI conference on artificial intelligence, volume 34, pages 1504–
1511.
Fioretto, F., Mak, T. W., and Van Hentenryck, P. (2020). Predicting ac optimal power flows:
Combining deep learning and lagrangian dual methods. InProceedings of the AAAI conference
on artificial intelligence, volume 34, pages 630–637.
Gasse, M., Chételat, D., Ferroni, N., Charlin, L., and Lodi, A. (2019). Exact combinatorial opti-
mization with graph convolutional neural networks.Advances in neural information processing
systems, 32.
Gomes, C. P., Selman, B., Crato, N., and Kautz, H. (2000). Heavy-tailed phenomena in satisfiability
and constraint satisfaction problems.Journal of automated reasoning, 24(1):67–100.
Greening, L. M., Dahan, M., and Erera, A. L. (2023). Lead-time-constrained middle-mile con-
solidation network design with fixed origins and destinations.Transportation Research Part B:
Methodological, 174:102782.
Guan, C., Er Raqabi, E. M., Tanneau, M., and Van Hentenryck, P. (2026). The proxy benders
decomposition.arXiv preprint arXiv:2606.07403.
Gupta, P., Gasse, M., Khalil, E., Mudigonda, P., Lodi, A., and Bengio, Y. (2020). Hybrid models
for learning to branch.Advances in neural information processing systems, 33:18087–18097.
Han, Q., Yang, L., Chen, Q., Zhou, X., Zhang, D., Wang, A., Sun, R., and Luo, X. (2023). A
gnn-guided predict-and-search framework for mixed-integer linear programming.arXiv preprint
arXiv:2302.05636.
Huang, T., Ferber, A. M., Zharmagambetov, A., Tian, Y., and Dilkina, B. (2024a). Contrastive
predict-and-search for mixed integer linear programs. InForty-first International Conference on
Machine Learning.
Huang, W. and Chen, M. (2021). Deepopf-ngt: Fast no ground truth deep learning-based approach
for ac-opf problems. InICML 2021 Workshop Tackling Climate Change with Machine Learning.
Huang, W., Huang, T., Ferber, A. M., and Dilkina, B. (2024b). Distributional MIPLIB: a multi-
domain library for advancing ml-guided milp methods.arXiv preprint arXiv:2406.06954.
Khalil, E., Le Bodic, P., Song, L., Nemhauser, G., and Dilkina, B. (2016). Learning to branch
in mixed integer programming. InProceedings of the AAAI conference on artificial intelligence,
volume 30.
Khalil, E. B., Dilkina, B., Nemhauser, G. L., Ahmed, S., and Shao, Y. (2017). Learning to run
heuristics in tree search. InIjcai, volume 2017, pages 659–666.
Khalil, E. B., Morris, C., and Lodi, A. (2022a). Mip-gnn: A data-driven framework for guiding
combinatorialsolvers. InProceedings of the AAAI Conference on Artificial Intelligence, volume36,
pages 10219–10227.
37

Khalil, E. B., Vaezipoor, P., and Dilkina, B. (2022b). Finding backdoors to integer programs: a
monte carlo tree search framework. InProceedings of the AAAI Conference on Artificial Intelli-
gence, volume 36, pages 3786–3795.
Kim, Y., Hijazi, A., Dalmeijer, K., and Van Hentenryck, P. (2025). Practice-based optimization for
the strategic locomotive assignment problem.arXiv preprint arXiv:2507.22235.
Kotary, J., Fioretto, F., andVanHentenryck, P.(2022). Fastapproximationsforjobshopscheduling:
A lagrangian dual deep learning method. InProceedings of the AAAI Conference on Artificial
Intelligence, volume 36, pages 7239–7246.
Kotary, J., Fioretto, F., Van Hentenryck, P., and Wilder, B. (2021). End-to-end constrained opti-
mization learning: A survey.arXiv preprint arXiv:2103.16378.
Lodi, A. and Zarpellon, G. (2017). On learning and branching: a survey.Top, 25:207–236.
Maragno, D., Wiberg, H., Bertsimas, D., Birbil, Ş. İ., den Hertog, D., and Fajemisin, A. O. (2025).
Mixed-integer optimization with constraint learning.Operations Research, 73(2):1011–1028.
Mohan, V., Er Raqabi, E. M., and Van Hentenryck, P. (2025). A fair or-ml framework for resource
substitution in large-scale networks.arXiv preprint arXiv:2511.18269.
Moinuddin, A., Er Raqabi, E. M., and Van Hentenryck, P. (2026). Scheduling and routing in the
flexible job shop with heterogeneous transbots and zoning: A constraint programming approach.
arXiv preprint arXiv:2604.24483.
Morabit, M., Desaulniers, G., and Lodi, A. (2021). Machine-learning–based column selection for
column generation.Transportation Science, 55(4):815–831.
Ning, C. and You, F. (2019). Optimization under uncertainty in the era of big data and deep
learning: When machine learning meets mathematical programming.Computers & Chemical
Engineering, 125:434–448.
Park, S., Chen, W., Han, D., Tanneau, M., and Van Hentenryck, P. (2023). Confidence-aware graph
neural networks for learning reliability assessment commitments.IEEE Transactions on Power
Systems, 39:3839–3850.
Park, S. and Van Hentenryck, P. (2023). Self-supervised primal-dual learning for constrained op-
timization. InProceedings of the AAAI Conference on Artificial Intelligence, volume 37, pages
4052–4060.
Sahinidis, N. V. (2004). Optimization under uncertainty: state-of-the-art and opportunities.Com-
puters & chemical engineering, 28:971–983.
Song, J., Yue, Y., Dilkina, B., et al. (2020). A general large neighborhood search framework for
solving integer linear programs.Advances in Neural Information Processing Systems, 33:20012–
20023.
Tang, K. and Yao, X. (2024). Learn to optimize—a brief overview.National Science Review,
11(8):nwae132.
Tang, Y., Agrawal, S., and Faenza, Y. (2020). Reinforcement learning for integer programming:
Learning to cut. InInternational conference on machine learning, pages 9367–9376. PMLR.
38

Tanneau, M. and Van Hentenryck, P. (2024). Dual lagrangian learning for conic optimization.
Advances in Neural Information Processing Systems, 37:55538–55561.
Tran, C., Fioretto, F., and Van Hentenryck, P. (2021). Differentially private and fair deep learning:
A lagrangian dual approach. InProceedings of the AAAI conference on artificial intelligence,
volume 35, pages 9932–9939.
Van Hentenryck, P. and Dalmeijer, K. (2024). AI4OPT: AI institute for advances in optimization.
AI Magazine, 45(1):42–47.
Vesselinova, N., Steinert, R., Perez-Ramirez, D. F., and Boman, M. (2020). Learning combinatorial
optimization on graphs: A survey with applications to networking.IEEE Access, 8:120388–
120416.
Wilder, B., Dilkina, B., and Tambe, M. (2019). Melding the data-decisions pipeline: Decision-
focused learning for combinatorial optimization. InProceedings of the AAAI conference on arti-
ficial intelligence, volume 33, pages 1658–1665.
Williams, R., Gomes, C. P., and Selman, B. (2003). Backdoors to typical case complexity. InIJCAI,
volume 3, pages 1173–1178.
Woolson, R. F. (2007). Wilcoxon signed-rank test.Wiley encyclopedia of clinical trials, pages 1–3.
Ye, T., Deza, A., Mohan, V., Er Raqabi, E. M., and Van Hentenryck, P. (2026). Democratizing
large-scale re-optimization with llm-guided model patches.arXiv preprint arXiv:2605.18692.
Ye, T., Jovine, A. S., Van Osselaer, W., Zhu, Q., and Shmoys, D. B. (2025a). Cornell University uses
integer programming to optimize final exam scheduling.INFORMS Journal on Applied Analytics.
Ye, T., Tong, S., Guan, C., Basciftci, B., and Van Hentenryck, P. (2025b). Deep learning-
driven contextual stochastic optimization for real-time order fulfillment. InNeurIPS 2025 Work-
shop MLxOR: Mathematical Foundations and Operational Integration of Machine Learning for
Uncertainty-Aware Decision-Making.
Zarpellon, G., Jo, J., Lodi, A., and Bengio, Y. (2021). Parameterizing branch-and-bound search
trees to learn branching policies. InProceedings of the aaai conference on artificial intelligence,
volume 35, pages 3931–3939.
Appendix A Backdoor Identification
Tables A.1 and A.2 report the Phase I exploratory analysis used to identify candidate backdoors for
the hard and very-hard settings, respectively. For each application, several semantically meaningful
variable families were fixed to their values in a reference optimal solution, and the resulting reduced
MIP was solved. Consistent with the backdoor identification procedure described in Section 3,
the family yielding the shortest runtime was selected as the backdoor. Interestingly, the selected
39

Problem Variable Family # Var Runtime (s) Gap (%) Selected
MMCNDP x(flow variables) 2,1830.0010.000✓ y(facility variables) 357 0.004 0.163
SLAP
x(assignment variables) 39,1690.0200.000✓
u(inventory variables) 38,769 0.039 0.466
y(fleet variables) 8 50.744 0.410
COURSE
x(course assignment variables) 20,7360.0310.000✓
y(scheduling variables) 1,728 0.050 0.000
z(auxiliary variables) 20,736 1.477 0.000
w(block variables) 300 0.061 0.000
v(slot variables) 12 0.064 0.000
o(three variables) 1 1.671 0.000
r(B2B variables) 2 9.581 0.000
l(triple variables) 2 100.021 3.681
OCP
x(vessel assignment) 9,6906.6090.213✓
y(order fulfillment) 61 100.044 –
v(selected variables) 1,404 16.416 0.034
OFP
x(allocation variables) 288,0000.1310.000✓
s(setup variables) 480 0.962 0.216
a(activation variables) 100 1.820 0.360
Table A.1: Phase I backdoor identification results for the Hard setting. For each application,
candidatevariablefamilieswerefixedtotheirvaluesinareferenceoptimalsolution, andtheresulting
reduced MIP was solved. Following the backdoor identification procedure ofBIPC, the variable
family yielding the shortest runtime was selected as the backdoor.
backdoors correspond to the principal operational decision variables of each application (transporta-
tion flows in MMCNDP, locomotive assignments in SLAP, course assignments in COURSE, vessel
assignment in OCP, and order-allocation variables in OFP), providing empirical evidence that a
relatively small subset of strategic decisions drives most of the computational complexity. Notably,
the selected backdoor variables are also those with the largest cardinality in four of the five appli-
cations, indicating that the most expressive operational decisions tend to capture the majority of
the combinatorial structure of the problem.
The results reveal substantial differences in the computational impact of the candidate variable
families. In all five applications, the selected backdoor yields the smallest solution time, often by
several orders of magnitude. These findings suggest that the computational complexity of the con-
sidered parametric MIPs is concentrated in a relatively small subset of strategic decision variables,
40

Problem Variable Family # Var Runtime (s) Gap (%) Selected
MMCNDP x(flow variables) 23,9840.0100.000✓ y(facility variables) 1,135 100.010 –
SLAP
x(assignment variables) 39,9160.0220.000✓
u(inventory variables) 37,116 0.094 0.000
y(fleet variables) 20 100.037 0.537
COURSE
x(course assignment variables) 38,4160.0500.000✓
y(scheduling variables) 2,744 0.092 0.000
z(auxiliary variables) 38,416 3.723 0.499
w(block variables) 406 0.116 0.000
v(slot variables) 14 0.121 0.000
o(three variables) 1 4.034 0.000
r(B2B variables) 2 21.685 0.000
l(triple variables) 2 100.017 6.455
OCP
x(vessel assignment) 5,68220.7250.000✓
y(order fulfillment) 38 55.202 0.000
v(selected variables) 1,179 92.761 0.000
w(production variables) 4,154 60.009 0.000
o(changeover variables) 5,239 100.021 16.161
OFP
x(allocation variables) 2,000,0001.1530.000✓
a(activation variables) 200 11.706 0.454
s(setup variables) 1,000 64.206 0.487
Table A.2: Phase I backdoor identification results for the Very-Hard setting. For each application,
candidatevariablefamilieswerefixedtotheirvaluesinareferenceoptimalsolution, andtheresulting
reduced MIP was solved. Following the backdoor identification procedure ofBIPC, the variable
family yielding the shortest runtime was selected as the backdoor.
which motivates the prediction, completion, and correction mechanisms developed in Phases II and
III.
The results indicate that the same variable family is consistently identified as the backdoor across
both Hard and Very-Hard instances for all five applications. This empirical observation provides
strong support for the assumption made in Section 3 that the backdoor remains essentially stable
across instances drawn from the same distribution. Moreover, the selected backdoors consistently
correspond to the primary operational decision variables of each application, suggesting that the
computational complexity of these parametric MIPs is concentrated in a small set of strategic
decisions.
Although the selected backdoor variables often correspond to the largest variable family in the
41

formulation, the exploratory analysis shows that cardinality alone is insufficient to explain compu-
tational impact, as several large variable families produce significantly weaker reductions in solution
time.
42

0 200 400 600 800 1,000
10−1
101
Runtime (s)
PG (%)
Gurobi PROPEL
ID-PaS+ BIPC
(a) MMCNP Hard
0 200 400 600 800 1,000
10−1
101
Runtime (s)
PG (%)
Gurobi PROPEL
ID-PaS+ BIPC
(b) MMCNP Very-Hard
0 200 400 600 800 1,000
10−1
101
Runtime (s)
PG (%)
Gurobi PROPEL
ID-PaS+ BIPC
(c) SLAP Hard
0 200 400 600 800 1,000
10−1
101
Runtime (s)
PG (%)
Gurobi PROPEL
ID-PaS+ BIPC
(d) SLAP Very-Hard
0 200 400 600 800 1,000
10−2
100
102
Runtime (s)
PG (%)
Gurobi PROPEL
ID-PaS+ BIPC
(e) COURSE Hard
0 200 400 600 800 1,000
10−1
101
Runtime (s)
PG (%)
Gurobi PROPEL
ID-PaS+ BIPC
(f) COURSE Very-Hard
0 200 400 600 800 1,000
10−1
101
Runtime (s)
PG (%)
MIP PROPEL
ID-PaS+ BIPC
(g) OCP Hard
0 200 400 600 800 1,00010−1
100
101
102
Runtime (s)
PG (%)
Gurobi PROPEL
ID-PaS+ BIPC
(h) OCP Very-Hard
0 200 400 600 800 1,000
10−1
101
Runtime (s)
PG (%)
Gurobi PROPEL
BIPC
(i) OFP Hard
0 200 400 600 800 1,000
10−1
101
Runtime (s)
PG (%)
Gurobi PROPEL
BIPC
(j) OFP Very-Hard
Figure 4: Average PG Evolution across Methods and Problem Instances.
43
