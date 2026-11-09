---
title: 'On the post-hoc Evaluation of PDE Discovery: A Multifaceted Challenge of Scientific Advancement'
url: https://arxiv.org/abs/2607.23753
category: ai-marketing
subcategory: measurement
date: 2026-07
venue: ''
authors:
- Baptiste Mathevon
- Farah Cherfaoui
- Amaury Habrard
- Marc Sebban
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.23753
pages: 42
chars: 140649
fetched_at: '2026-11-08T13:28:38+00:00'
kb_version: 1
---

# On the post-hoc Evaluation of PDE Discovery: A Multifaceted Challenge of Scientific Advancement

On the post-hoc Evaluation of PDE Discovery:
A Multifaceted Challenge of Scientific Advancement
Baptiste Mathevon1, Farah Cherfaoui1, Amaury Habrard 1,2 and Marc Sebban 1
1Universit´ e Jean Monnet Saint-´Etienne, CNRS, Institut d’Optique Graduate School, Inria,
Laboratoire Hubert Curien UMR 5516, F-42023, SAINT- ´ETIENNE, France
2Institut Universitaire de France (IUF)
Abstract
Partial differential equation (PDE) discovery aims to identify from data the governing law of
a physical system. Constituting a cornerstone of scientific advancement, it has become during
the past decade a major line of research in the rapidly evolving field of Physics-informed Machine
Learning (PiML). Among the remaining open problems to address in this domain, the post-hoc
evaluation of discovered PDEs raises the particular difficulty of being multifaceted. Indeed, it
requires jointly considering predictive accuracy, physical consistency, interpretability, and out-of-
distribution generalization capacity. Given that some of these properties are conflicting, it is worth
noting that the wide range of existing evaluation metrics only partially address the overall problem,
potentially leading to overly interpreted conclusions about the validity of a presumed new physical
theory. From an abundant literature spanning machine learning, numerical analysis, information
theory or symbolic regression, we propose, to our knowledge, the first taxonomy of PDE evaluation
metrics, and discuss their advantages and limitations in depth. Based on the observation that
evaluation is often achieved on a case-by-case basis and that a universally accepted methodology
remains elusive, we further provide recommendations with the aim of promoting standardized and
reliable practices, before sketching promising future lines of research in this field. We argue that
this paper is intended both for ML experts who design new PDE discovery algorithms and for users
of these methods aiming, in real applications, to discover and validate well-founded scientific laws.
Contents
1 Introduction 2
2 PDE discovery setting, notations and experimental setup 5
3 Metrics requiring access to the governing PDE 7
3.1 Recovery of the PDE terms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.2 Recovery of the PDE coefficients . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4 Metrics independent from the ground truth analytical form 13
4.1 Prediction errors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
4.2 Sparsity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.3 Trade-off between prediction and sparsity . . . . . . . . . . . . . . . . . . . . . . . . . 18
4.4 Physical consistency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
4.5 Out-of-distribution generalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
5 Practical guidelines for evaluating PDEs and perspectives 28
1
arXiv:2607.23753v1  [cs.LG]  26 Jul 2026

1 Introduction
Alongsideforwardproblems such as learning fast neural surrogate solvers (e.g.PINNs [1] or FNOs [2]),
partial differential equation (PDE) discovery is one of the maininverseproblems studied in the active
field of Physics-informed Machine Learning (PiML) [3]. It consists in automatically identifying from
simulation or observation data the governing equation(s) of a physical system. This task becomes
especially critical when addressing real applications where there is no prior knowledge of the underlying
physics (or only a partial understanding of it), which may involve the complex interplay of several
physical phenomena. While a broad range of PDE discovery methods (see,e.g., [4, 5, 6, 7, 8]) has
flourished in the past few years, often envisioning the task from the perspective of sparse regression, it is
worth noting that a universally accepted methodology for the systematic evaluation of identified PDEs
remains unestablished [9]. The main reason is that post-hoc assessment, as commonly acknowledged
in the literature [10, 11, 12], is inherently multifaceted and difficult to capture with a single measure,
insofar as the fitness accuracy, physical consistency, parcimony and generalization capacity, have to
be considered jointly. More precisely, we argue that a discovered PDE is expected to meet several
objectives, some of which may be in conflict, that we propose to formulate in terms of the following
key questions (see Fig. 1 for an overview):Q1:Does the identified PDE allow to lead to accurate
solutions (up to numerical errors)?Q2:Is this equation physically consistent (i.e., is there any
violation of fundamental physical principles)?Q3:Is it simple enough so as to be interpreted as a
general scientific discovery?Q4:What is its ability to generalize out of distribution (long-horizon
prediction, adaptation to different initial/boundary conditions or changes in dynamical regimes)?Q5:
To what extent does it agree with the ground-truth (GT) governing PDE, when the latter is available?
These questions naturally relate to the classical statistical learning setting, notably with respect
to the bias–variance trade-off. In particular,Q1is directly connected to data fidelity, whileQ3refers
to model complexity. As in standard machine learning, increasing the latter may improve the former
and reduce bias, but comes at the cost of higher variance; conversely, reducing model complexity may
increase bias while lowering variance. However, beyond this similarity, the following distinction should
be noted: the notion of complexity is stronger in PDE discovery because it demands interpretability
and consistency at the level of a meaningful scientific law, thereby requiring going beyond mere sparsity.
Therefore, we argue that in PDE discovery, the ”simpler is better” paradigm is less straightforward
than in conventional machine learning. On the other hand, it is worth noticing thatQ4extends
the standard notion of generalization by explicitly targeting out-of-distribution extrapolation, which
becomes central in dynamical systems. Indeed, it is often necessary in real applications to simulate the
PDE under varying conditions, time horizons and regimes. Finally, while modern neural architectures
may incorporate symmetries or equivariances which partially draw inspiration from physics, PDE
discovery (viaQ2) requires adherence to actual fundamental physical principles (e.g.conservation
laws), making the discovery and evaluation tasks more theoretically grounded.
Evaluating a PDE solely through the lens of one of these questions can lead to drawing erroneous
conclusions and formulating inconsistent hypotheses about the governing physical theory. For instance,
it is well established that a small reconstruction error does not always reflect the symbolic correctness
of the discovered equation (e.g., spurious terms that cause small errors over a short time period
can lead, over a longer horizon, to a dramatic deterioration of the solutions). Moreover, despite the
realistic assumption that most physical systems are governed by PDEs composed of a few terms, it
is also widely known that the simplicity of an equation does not necessarily guarantee its physical
consistency (e.g.a sparse PDE may violate symmetry properties or conservation laws). On the
other hand, as theoretically studied for PINNs [13, 14, 15], observing small residuals, even on unseen
validation data, does not automatically mean that the discovered equation is correct and leads to
accurate solutions. Considering the diversity of metrics, which are hardly comparable since they
capture different properties of the PDE, one may feel at a loss when it comes to determining whether
a learned equation represents a valid physical law.
2

Figure 1: Overview of PDE discovery and metrics (in blue) devoted to address the multifaceted
challenge of post-hoc PDE evaluation in accordance with the five key principles to be met (in red). The
illustrations of dynamics correspond to a physical system leading to complex pattern formation and
chaotic behavior. They are simulated from either the ground truth Kuramoto-Sivashinsky equation
(P DEGT ) or a learnedP DEA, or they correspond to observation data (e.g.obtained by laser-matter
interaction and self-organization of matter for whichP DE GT is a good candidate for modeling the
phenomenon). Three sets are used in PDE discovery: a training setTis employed for learningP DE A
with some algorithmA; a validation setVis compared to a setEof estimated solutions, simulated
fromP DEA, for evaluating the discovered law from a pointwise or trajectory perspective.
Although PDE evaluation is intrinsically multi-criteria, we emphasize that this paper is not
positioned within a multi-objective optimization framework [16], where one typically seeks Pareto-
optimal solutions to identify trade-offs among conflicting criteria as done,e.g., in genetic algorithms,
decomposition-based methods, multi-objective gradient-based approaches, etc. Said differently, we
do not view the metrics considered in this study as means of guiding PDE discovery algorithms
(some of those criteria are non-separable functions and cannot even be optimized). Instead, they are
treated as post-training measures to evaluate an equation, during a downstream task, regardless of the
mechanism from which it originates. Nonetheless, certain metrics commonly used in multi-objective
optimization can be leveraged in post-hoc PDE evaluation. This applies to those employed in symbolic
regression [17]1, which will thus be studied below.
By decoupling the identified PDE from the discovery process, we shift the focus of the evaluation
task from the learning algorithm to the scientific discovery itself. Moreover, by doing so, we argue
that these metrics may thus be applied in scenarios that do not necessarily involve learning but still
require a valid evaluation procedure 2. This may hold, for instance, whenhuman experts formulate
1A substantial part of the PDE discovery literature can be cast, as a special case, within this framework, albeit more
challenging due to the presence of derivative terms.
2Note that for the sake of consistency in notation and terminology, we will remain within the scope of conventional
PDE discovery throughout this article, assuming that the equation has been learned from data, while not exploiting the
algorithm itself in the downstream evaluation task.
3

a new hypothesisfor a physical law based on their own theoretical knowledge and observations of a
physical system. It also applies in an attempt tosimplify a complex existing law, motivatede.g.by
the need (i) to reduce the computational cost, making large-scale simulations feasible, (ii) to isolate
the dominant physical mechanisms, thereby improving interpretability, or (iii) to facilitate theoretical
analysis (existence/uniqueness of solutions, asymptotic guarantees, etc.) that would be impossible
without sparsifying the equation. Thecomparison of competing conjecturesproposed in the literature
to model the same phenomenon constitutes another example of setting where post-hoc evaluation can
be highly beneficial. By focusing on the discovered knowledge, note that two properties frequently
studied in PDE discovery literature will not be considered in this article: the robustness (i) to the
presence of noise, and (ii) to scarcity in the training data. Both indeed characterize the performance
of the discovery algorithm itself.
With this clarification in mind, we can now outline the main contributions of this paper:
1. Drawing from a vast body of literature at the intersection of machine learning, information
theory, symbolic regression, but also by leveraging verification criteria from numerical analysis,
we establish ataxonomy of PDE evaluation metrics. We do not limit this classification
to a mere enumeration of formulae. Instead, we provide a comprehensive analysis, examining
for each of the metrics itsproperties, advantages, andlimitations. To the best of our
knowledge, this is the first study which conducts such an in-depth analysis and gathers the
state-of-the-art metrics previously dispersed across different scientific domains. To illustrate the
practical use of these criteria, we rely throughout this study on arunning example on the
non linear fourth-order Kuramoto-Sivashinsky equation(illustrated in Fig. 1), which
presents a chaotic behavior and allows to model complex pattern formation and instabilities
in various physical systems. The experiments performed with this non trivial equation (see
all paragraphs entitled “Running Example” which constitute milestones of this paper) enable a
better understanding of these metrics and sometimes revealpathological behaviorsexhibited
by some of them.
2. The classification proposed, together with the analysis of PDE evaluation metric behaviors on
the Kuramoto-Sivashinsky PDE, allows us toformulate general cautions and recommen-
dations. The goal is to address the pressing need forstandardizing PDE evaluation(as
recently stated in [18]) so as to avoid overstating the validity of identified laws. From this dis-
cussion, we outline aset of promising research directionsto meet: (i) the need to better
account for the functional propertiesof the discovered equation, unlike ML-conventional
pointwise metrics. We notably discuss the use of tools from functional analysis, as well as opti-
mal transport and gradient flows; (ii) the necessity ofconsidering the numerical solvability
of the model as an additional key criterion to allow large and small-scale simulations when ad-
dressing real-world applications. This aspect is strikingly underexplored in the PDE evaluation
literature, and (iii) the value of designing new measures specifically tailored to theevalua-
tion of fractional PDEs. Indeed, the ability of these equations to account for nonlocal effects
makes them particularly attractive for modeling certain complex, multiscale, and memory-driven
phenomena; however, the expressiveness and intrinsic complexity of fractional-order derivatives
reduce the relevance of classical metrics.
We argue that this paper could provide valuable insights for machine learning experts developing new
PDE discovery algorithms, and may also be of interest to scientists in other domains where modeling
dynamics through equations plays a crucial role,e.g., in physics, chemistry, or biology, seeking a
comprehensive understanding of PDE evaluation. To enable them to easily compute the metrics
presented throughout this survey on their own PDEs, we have developed the following user-friendly
GitHub repository: PDE-Evaluation.
4

Table 1: Capacity of the investigated metrics to answer the 5 key questions in PDE evaluation. The
last four rows of the table do not, strictly speaking, represent evaluation metrics, but rather physical
properties discussed in Sec. 4.4 that can be used to assess the physical consistency of the PDE.
Solution Physical Interpretation Generalization GT PDE
Accuracy Consistency Sparsity Capacity Recovery
Metrics Q1 Q2 Q3 Q4 Q5
T P R(α,ˆα) (4)J(α,ˆα) (7) ✘ ✘ ✔ ✘ ✔
P(α,ˆα) (5)R(α,ˆα) (6) ✘ ✘ ✔ ✘ ✔
LM M ✘ ✘ ✔ ✘ ✔
ϵp coef (α,ˆα) (8)-(10) ✘ ✘ ✘ ✘ ✔
wϵ2 coef (α,ˆα) (12)-(13) ✘ ✔ ✘ ✘ ✔
N DCG(α,ˆα) (14) ✘ ✔ ✘ ✘ ✔
TG(α,ˆα) (17) ✘ ✘ ✘ ✘ ✔
M SE/M AEonu(18)-(20) ✔ ✘ ✘ ✔ ✘
M SEonu t (21) ✘ ✔ ✘ ✔ ✘
f M SE(F(ˆu),F(u)) (23) ✔ ✔ ✘ ✔ ✘
ϵrollout(ˆu, u) (24) ✔ ✔ ✘ ✔ ✘
Sterms(ˆα) (25) ✘ ✘ ✔ ✘ ✘
C(ˆα⊤.Θ) (26) ✘ ✘ ✔ ✘ ✘
Score(ˆα) (27) ✔ ✘ ✔ ✘ ✘
Reward1,2(ˆα) (28) (29) ✘ ✔ ✔ ✘ ✘
AIC c (31),BIC(32) ✘ ✔ ✔ ✘ ✘
P IC(33) ✔ ✔ ✔ ✘ ✘
M DL(34) (35) ✔ ✘ ✔ ✘ ✘
ϵT ′ rollout(ˆu, u) (37) ✔ ✔ ✘ ✔ ✘
Conv x(ˆα) (38) ✘ ✔ ✘ ✔ ✘
Conv t(ˆα) (39) ✘ ✔ ✘ ✔ ✘
Physical properties 4.4: ✘ ✔ ✘ ✔ ✘
Symmetries, Conservation Laws
Residuals, Dimensional Consistency
Positivity Preservation, Convection
Energy Dissipation, etc.
The rest of this article is organized as follows: Section 2 introduces the PDE discovery setting,
the notations used, as well as the Kuramoto-Sivashinsky (KS) equation employed as running example
throughout our study. Section 3 is devoted to the presentation of metrics that require the access to
the governing equationP DEGT . Since this setting is more appropriate for evaluating an algorithm’s
capability to recoverP DEGT and less suited to scientific discovery, we relax this constraint in Section 4
and present metrics that can be applied even when the governing analytical form is not available. The
findings of our review are summarized in Table 1 reporting the metric capacity to answer the five
aforementioned questions. In Section 4, we also discuss various methods for evaluating the physical
consistency of a PDE through the verification of relevant physical properties. Finally, we outline
in Section 5 key recommendations along with the main pitfalls to be avoided when evaluating an
equation. We conclude this article by sketching several promising directions for PDE evaluation.
2 PDE discovery setting, notations and experimental setup
Let us consider equations of the following general form:u t =N[u],withu∈C n([0, T]×Ω;R d2),
ann-times continuously differentiable function modeling a vector field;u t is the time derivative, and
N[·] is a (possibly nonlinear) differential operator, witht∈[0, T] the temporal variable bounded by a
finite time horizonTandx∈Ω⊂R d the spatial coordinates belonging to a bounded input domain.
5

The equations may also be accompanied by initial and boundary conditions (denoted by IC and BC,
respectively) that must be satisfied at the initial time or on the boundaries of the domain. In the
following, the notationu x denotes the partial derivative with respect to the input spatial domain,u xx
corresponds to the second order derivative, etc.
The PDE discovery paradigm is based on the realistic assumption that in most physical laws only
a few important terms govern the underlying dynamics, that encourages promoting sparsity. For this
reason, many algorithms address the problem from a sparse regression perspective by approximating
the differential operator into the form of a parsimonious linear combination of preselected terms from
a finite dictionary, typically composed of partial space derivatives (i.e.u x1,u x1x1,u x1x2,u x1ux2,
etc.), polynomials (e.g.u 3) and constants. Since the success of such strategy is closely tied to the
completeness of the dictionary, the design of the latter remains a challenge. This is why free-form
strategies are used in symbolic regression (e.g., resorting to genetic programming, tree-based search
algorithms, transformers, etc.) to adapt the expression being searched for to the task at hand.
Nevertheless, without loss of generality, we can assume here that PDE discovery can be reduced to
producing a linear combination of terms in the form of an estimate ˆu t =ˆα⊤.Θ where Θ is a vector
of size|Θ|whose components are evaluations of linear and non linear functions at (t,x) andˆαis a
|Θ| ×d2 matrix containing the learned coefficients associated with each term of Θ for thed 2 governing
equations. Let us assume thatˆαhas been learned with some PDE discovery algorithm from a
training setT={u(t i,x i)}nT i=1 composed ofn T simulation datain the scenario where the ground
truth equationP DEGT is known, orobservation datawhen the theory governing the dynamical
system is not yet identified. Moreover, we also assume we have at our disposal a validation set
V={u(t j,x j)}nV j=1 that will be used, depending on the type of metrics, for evaluating the identified
PDEs. Note thatVmight be obtained from different IC and BC and beyond the training time
horizon to evaluate the capacity of the learned PDEs to adapt to out-of-distribution tasks.
For the sake of simplifying the notations, we will assume in the following thatd 2 = 1, meaning that
uis a scalar field. In this scenario,ˆα ⊤ = (ˆα1, . . . ,ˆαi, . . . ,ˆα|Θ|) becomes a vector of size|Θ|. Note
that most of the metrics presented in this paper can be readily applied to anyd2-dimensional dynamics.
Running Example: As mentioned above, we consider the following fourth-order non linear 1D
Kuramoto-Sivashinsky (KS) PDE, which will serve as running example throughout the paper:
P DEGT :u t =−1.0uu x −1.0u xx −1.0u xxxx.(1)
This equation will be solved using periodic BC and the following IC: cos(2πx/L)+0.5 cos(4πx/L+0.3).
Let us assume that an algorithmAdiscovered fromTthe following equation:
P DEA : ˆut =−0.99uu x −0.98u xx −0.985u xxxx.(2)
Let us further assume that another algorithmBidentified a second equation defined as:
P DEB : ˆut =−0.89uu x −0.9u xx −0.85u xxxx + 0.0004u−0.0008u xuxx.(3)
Note that we intentionally use asP DE B an equation that is “farther” 3 fromP DEGT thanP DEA
leading to larger differences between solutions, especially as time progresses (see simulations in Fig. 2),
thereby allowing us to assess the ability of the metrics to distinguish the quality of the two equations.
Using our notations, the true vector of coefficientsα ⊤ = (0,−1,−1,−1,0), while the vectors learned
byAandBareˆα ⊤ A = (0,−0.99,−0.98,−0.985,0) andˆα ⊤ B = (0.0004,−0.89,−0.9,−0.85,−0.0008)
respectively, all of them associated with Θ ⊤ = (u, uux, uxx, uxxxx, uxuxx).
3Although this term remains ambiguous at this stage of the paper, it refers quite objectively to deviations in both
the coefficients and the functions involved.
6

Figure 2: Simulated solutions of the Kuramoto-Sivashinsky equationP DE GT (left) and 2 learned
equations,P DEA (center) andP DEB (right). For the purpose of this running example,P DE A is by
construction much more similar to the ground truth thanP DEB. Indeed, we can observe thatP DEB
gradually diverges over time from the true physical dynamics modeled byP DE GT .
Experimental setup:For the experiments requiring validation dataVsimulated fromP DE GT and
estimated solutionsEobtained fromP DE A andP DEB (this concerns all metrics discussed in Sec. 4),
we will use the numerical method ETD1 (Exponential Time Differencing, 1st order) and solve the
equations over a timeT= 50 with a time stepδ t = 0.05 yielding a temporal discretization with
Nt = 1000 steps. We use a spatial meshN x = 1024 over a periodic domain of lengthL= 22, which
yields a spatial spacingδ x =L/N x ≈0.0215. This way, we collect datasetsVandEconsisting of
nV =N x ×N t = 1,024,000 data, defined as solutions evaluated at the same (t,x) coordinates allowing
pointwise comparisons. Depending on the setting (in-distribution or out-of-distribution), the setsV
andEwill be simulated using either the same or different IC and BC asT.
3 Metrics requiring access to the governing PDE
We begin this review with criteria that require access to the analytical expression of the governing law
P DEGT . Although this category of PDE evaluation metrics may appear somewhat contradictory at
first sight (why allow the use ofP DEGT when the goal is to discover it?), it is worth noticing that most
papers presenting a new PDE discovery algorithm assume in their experimental setup that the target
equation is known; and they directly use the latter in the evaluation. This way, rather than focusing
on assessing adiscovered PDEas a new physical theory, these works primarily aim to evaluate
the algorithm’s ability torecover a known equationused for proof-of-concept purposes. Under
this scenario, several metrics can be employed to check the accuracy of either the learned symbolic
expression (Sec. 3.1) or the coefficients associated with its terms (Sec. 3.2).
3.1 Recovery of the PDE terms
Using our notations, let us recall that PDE discovery looks for equations of the form ˆu t =ˆα⊤.Θ.
Metrics discussed in this section are based on the functions involved in this symbolic expression,i.e.
those associated with coefficientsα i ̸= 0. They primarily help answer QuestionQ5(which concerns
the recovery ofP DEGT ). Additionally, they indirectly provide insights on QuestionQ3(dealing with
the sparsity).
Support recovery: In [19], directly inspired by the well-knownF 1-score, the authors leverage the
followingtrue positive ratio(T P R):
T P R(α,ˆα) = T P(α,ˆα) T P(α,ˆα) +F N(α,ˆα) +F P(α,ˆα)∈[0,1],(4)
7

Table 2: Application of the term recovery metrics (Sec. 3.1) to compareP DE A versusP DEB using
the KS ground truthP DE GT as reference. A green point • (resp. •) corresponds to a better
(resp. worse) evaluation score w.r.t.P DE GT . By construction of the equations,P DE A is expected
to achieve better scores. An • point corresponds to a tie situation, where the metric is unable to
distinguish between the two PDEs.
P DEA P DEB
ˆut =−0.99uu x ˆut =−0.89uu x −0.9u xx
−0.98uxx −0.985u xxxx −0.85uxxxx + 0.0004u−0.0008u xuxx
T P R(α,ˆα) (4) 1 • 3/5 •
P(α,ˆα) (5) 1 • 3/5 •
R(α,ˆα) (6) 1 • 1 •
LLM(α,ˆα)
“They are approximately
equivalent, differing only
by small numerical esti-
mation errors.”
•
“They are structurally similar, the two
extra terms are small and likely spu-
rious, but there is no set of constant
parameter values that makes the two
equivalent.”
•
whereT P(True Positives) denotes the number of correctly-identified nonzero coefficients, andF N
(False Negatives) - resp.F P(False Positives), stands for the number of coefficients that are incorrectly
specified as zero (resp. nonzero). This metric has been used in several PDE discovery methods,
including the Mechanistic PDE Networks [20], or Adjoint-PDE-FIND [21]. Rather than usingT P Ras
a measure of overall structural similarity, one can rather exploit the so-called PrecisionPand RecallR.
This is the post-hoc evaluation strategy used in PhysPDE [9], an algorithm guiding and constraining
the discovery of PDE expressions with prior physical hypotheses.PandRare respectively defined in
the classical way as follows:
P(α,ˆα) = T P(α,ˆα) T P(α,ˆα) +F P(α,ˆα)∈[0,1],(5)
R(α,ˆα) = T P(α,ˆα) T P(α,ˆα) +F N(α,ˆα)∈[0,1].(6)
In PDE evaluation, combiningPandRinstead of a singleT P R-like measure provides a more balanced
assessment by jointly capturing how well the discovered derivatives match the true underlying terms
while penalizing both missing relevant differential terms and introducing spurious ones.
Note thatT P Ris also referred in the literature to as Jaccard indexJ(see [22] and MIO-
SINDY [23]) or as Tanimoto coefficientT[24], both defined as the following function on sets:
J(α,ˆα) =T(α,ˆα) =|S(α)∩ S(ˆα)| |S(α)∪ S(ˆα)|∈[0,1],(7)
whereS(α) ={Θ i :α i ̸= 0}andS(ˆα) ={Θ i :ˆαi ̸= 0}.
AlthoughT P R(and henceJandT) are not specifically designed to evaluate the sparsity of
the learned model, values close to 1 indicate that the structure ofP DE GT has been successfully
recovered. As it is generally accepted that most physical laws can be expressed with a small number
of terms, aT P Rclose to 1 means that the equation is therefore also likely to be parsimonious. These
metric can therefore also be considered as providing a partial answer to QuestionQ3regarding sparsity
Symbolic accuracy with LLMs: Based on a paradigm that differs significantly from other
classical methods, Foundation Models and in particular Large Language Models (LLMs) have
8

recently gained interest for equation discovery (see,e.g.NeuroSymBO [25], Data-Driven Discovery
(D3) framework [26] or [27]). In LLM-SRBench [28], beyond building many challenging problems
across various scientific domains, the authors employ GPT-4o as an automated post-hoc evaluator
to measure asymbolic accuracybetweenP DE GT and a discovered expression, after replacing
constants with placeholders. The LLM is prompted to decide if the two equations are symbolically
equivalent (with a request for algebraic justification) under a tolerance of small numerical mismatches
in the coefficients. A prompt similar to the following is used:“Given theP DE GT expression and the
hypothesisP DEA, determine if there exist any constant parameter values that would makeP DE GT
equivalent toP DE A”. Note that LLMs, as used in LLM-SRBench to prune the search space in
the context of symbolic regression, are combined in [29] with a utility measure for each termθ i of
the equation and its associated coefficientsα i (while holding the others fixed) to refine the list of
candidate functions.
Running Example: Let us experiment with the metrics presented in this section on the KS
equationP DEGT and the learned equationsP DE A andP DEB. The values of the metrics are
reported in Table 2. ForP DE A, fromT P(α,ˆαA) = 3,F N(α,ˆαA) = 0 andF P(α,ˆαA) = 0, we get
T P R(α,ˆαA) = 1,P(α,ˆα A) = 1 andR(α,ˆα A) = 1, reflecting that the structure has been perfectly
recovered. On the other hand, fromT P(α,ˆαB) = 3,F N(α,ˆαB) = 0 andF P(α,ˆαB) = 2 we get, as
expected, a lowerT P R(α,ˆαB) equal to 3/5 withP(α,ˆα B) = 3/5 andR(α,ˆαB) = 1. Different from
1,T P RandPcapture well the presence of the spurious terms. Using LLMs as in LLM-SRBench, we
get a better evaluation forP DEA thanP DEB. The model further indicates that with the presence of
the two additional termsuandu xuxx, there is no set of coefficientsˆαB that makes the two equations
P DEB andP DEGT equivalent.
PROS✔vsCONS✘
✔T P R, PandRdirectly measure success of structural recovery. Moreover, they are invariant to the
number of terms of the equations and their interpretation is intuitive (the higher the better). Although
they do not directly measure the sparsity of the discovered PDEs, a value close to 1 indicates that the
parsimony ofP DEGT is recovered. For its part, LLMs have the benefit of justifying the decision and
provide a binary final answer.
✘These metrics requireP DE GT to be known. Moreover,T P R, PandRonly assess the form of the
PDE (i.e.the terms involved in the equation) without evaluating the associated coefficients which
have an impact on the shape of the dynamics. The symbolic accuracy provided by a LLM is not
a reliable quantitative measure. Moreover, two close but different textual descriptions can make it
difficult to compare competing PDEs.
✔ ✘
3.2 Recovery of the PDE coefficients
This section provides an overview of the main existing metrics built upon the magnitude of the
learned coefficientsˆα. It ends with a presentation of some metrics that also consider information
about the recovery of the terms. All of them primarily help answer QuestionQ5.
Unweighted error on coefficients: Most PDE discovery papers quantify the deviationϵp coef between
the learned PDE andP DE GT in terms oferror on coefficients. Often defined as an unweighted
error,ϵ p coef can take different forms depending on the normℓ p used for the comparison betweenαand
ˆα.
For instance, one can leverage the classic normalized squared errorϵ 2 coef (α,ˆα) (as used in Weak
SINDy [30], Ensemble-SINDY [31] or MIO-SINDY [23]) which gives insights regarding the magnitudes
9

of spurious coefficients:
ϵ2 coef (α,ˆα) =||α−ˆα||2 2 ||α||2 2 ∈R ≥0.(8)
Note that the following normalized absolute errorϵ 1 coef is preferred overϵ 2 coef (which may over-penalize
an error on only one coefficient) in several articles on PDE discovery (see,e.g.SINDY [4], PDE-
NET [5], PDE-LEARN [7], EqGPT [32], Adjoint-PDE-FIND [21] or ABL-PDE [33]).
ϵ1 coef (α,ˆα) =||α−ˆα||1 ||α||1 ∈R ≥0.(9)
Based on the physical observation that a single misidentified coefficient can completely alter the law,
Weak SINDy [30], and Mechanistic PDE Networks [20] resort to the more severeℓ ∞-based error on
the true nonzero coefficients:
ϵ∞ coef (α,ˆα) = max i:αi̸=0 |αi −ˆαi| |αi| ∈R ≥0.(10)
Finally, in iNeural-SINDy [6], the absolute values are applied on each coefficientα i separately in order
to take into account the fact that their respective order might be different, describing dynamics of
varying scales:
ϵ1 coef(i) (αi,ˆαi) =|α i −ˆαi| ∈R≥0, i= 1..|Θ|.(11)
Considering that, depending on the PDE term it is associated with, a small variation in a
coefficient may have a more or less significant impact on the overall dynamics, we discuss below
metrics built upon weighted errors.
W eighted error based on sensitivity analysis: Metrics presented above do not distinguish
between coefficients that are numerically close but dynamically different, and those that are numeri-
cally different but have negligible effect on the solution behavior, stability properties, and long-term
evolution. One way to overcome this issue consists in assigning a weightw i to each coefficientα i
according to the impact of the associated functionθ i on the induced dynamics. Note that this
strategy requires simulation data fromP DE GT to allow the calculation of partial derivatives, as
explained in the following.
A first approach to definew i on the basis of a local sensitivity analysis of the solution with respect
to the parametersα i is inspired by the Learning Gradient Flow (LGF) optimizer [34] as follows:
wi ∝
 ∂u ∂αi  2 2 ,
leading to the following weighted error reflecting how perturbations in each coefficient propagate
through the dynamics (note that this can be also applied to theℓ 1-based variant):
wϵ2 coef (α,ˆα) =
P|Θ|
i=1 wi(αi −ˆαi)2
P|Θ|
i=1 wi
∈R ≥0.(12)
A second complementary approach accounts for the exponential amplification of perturbations along
unstable dynamical directions. Letλ >0 denote a dominant Lyapunov exponent [35] associated with
the underlying dynamical system. One can define a time-dependent weighted sensitivity of the solution
with respect to each parameterα i, as follows:
wi(t)∝exp(λt)
 ∂u ∂αi  2 2 .
10

This leads to a Lyapunov-informed metric of the form
wLyapϵ2 coef (α,ˆα) =
|θ|X
i=1
 Z T
0
exp(λt)
 ∂u(t) ∂αi  2 2 dt ! (αi −ˆαi)2 ∈R ≥0.(13)
Compared to Eq. 12, this formulation explicitly accounts for the fact that perturbations in chaotic
or weakly stable regimes may remain negligible in the short term but grow exponentially over time.
Rank on the coefficients: Another category of metrics consists in evaluating the discovered PDE
using the rank of the terms, as used in [36]. The absolute values of the coefficients are sorted in
decreasing order; then, the ranking vector of the learned PDE is compared with that ofP DEGT . This
way, the metric assesses the ability of the method to correctly prioritize from a coefficient perspective
the key terms within the PDE. To compare the ranking vectorsrank(α) andrank(ˆα), one can resort,
e.g., to the normalized Discounted Cumulative GainN DCG:
N DCG(α,ˆα) =DCG(rank(ˆα)) DCG(rank(α)) ∈R ≥0.(14)
whereDCGis defined in [37] as follows:
DCG(rank(α)) =
|Θ|X
i=1
rank(α)i
log2(i+ 1) ∈R ≥0.(15)
The closerN DCGis to 1, the better the recovery of the GT coefficients. Even though, when equal
to 1, this metric does not guarantee thatP DE GT has been recovered, it nevertheless ensures that
the most important local terms at the origin of the physical dynamics are correct, and therefore
N DCGpartially also answers QuestionQ2about the physical consistency in the sense that the main
coefficients governing the PDE are correctly recovered.
T owards jointly considering terms and coefficients:Although a combination of the two may
appear natural, it is worth noticing that there is no adopted metric in the related works that explicitly
merges the support recoveryandcoefficient error into a single canonical formulation. We hypothesize
that one reason could be that, since these metrics cannot be used during training (becauseP DE GT is
assumed to be unknown and, moreover,T P Ris non-separable, thus not optimizable), they are instead
employed independently in a post-hoc manner, without the need to tune an additional hyperparameter
to combine them. However, note that two criteria attempt to establish a link between the two and
therefore deserve to be mentioned here.
The first one corresponds to a normalized version of Eq.(11), as used in [38], as well as in PDE-
READ [39], ABL-PDE [33] and ANN-PYSR [40]. This variant, which comes with the benefit that
errors in large coefficients do not dominate, is defined as follows:
ifT P R(α,ˆα) = 1 thenN ϵ1 coef(i) (αi,ˆαi) =
( |αi−ˆαi|
|αi| ∈R ≥0,∀i= 1..|Θ|s.t.α i ̸= 0,
0 otherwise.
(16)
The important point in Eq. 16 is that it is conditioned on first matching the GT structural terms.
Second, the Tanimoto coefficientT, which originally deals with sets (as already defined in Eq.(7)),
and is often used in chemical compound discovery based on molecular fingerprints [41, 42], has been
extended to handle real-valued vectors. Using our notations, this generalized versionT G is defined as
follows:
TG(α,ˆα) = α⊤ ˆα ||α||2 2 +||ˆα||2 2 −α ⊤ ˆα∈[0,1].(17)
11

Table 3: Application of the coefficient recovery metrics (Sec. 3.2) to compareP DE A versusP DEB
using the KS ground truth equationP DE GT as reference.
P DEA P DEB
ˆut =−0.99uu x ˆut =−0.89uu x −0.9u xx
−0.98uxx −0.985u xxxx −0.85uxxxx + 0.0004u−0.0008u xuxx
ϵ2 coef (α,ˆα) (8) 0.0002 • 0.0149 •
ϵ1 coef (α,ˆα) (9) 0.0150 • 0.1204 •
ϵ∞ coef (α,ˆα) (10) 0.0200 • 0.1500 •
wϵ2 coef (α,ˆα) (12) 0.0002 • 0.0014 •
N DCG(α,ˆα) (14) 0.9862 • 0.8855 •
TG(α,ˆα) (17) 0.9998 • 0.9834 •
Note that ifαandˆαare binary vectors (presence/absence of terms), the original expressionT
(Eq.(7)) andT G are equivalent. By comparing the coefficient vectors in this way, the extended
Tanimoto metric accounts for both the PDE structure, through the presence or absence of candidate
terms, and the magnitude of the associated coefficients.
Running Example: Reconsider the KS equationP DE GT and the learned equationsP DE A and
P DEB. The values computed from the different metrics discussed in this section are reported in
Table 3. They all indicate thatP DE A is much closer to the ground truth thanP DE B. Except for
theℓ 2-based errorϵ 2 coef (α,ˆα), which heavily over-penalizes local errors, all theϵ p coef metrics behave
similarly by yielding a ratio of approximately 1:7 to 1:8 in favor ofP DE A. It is worth noticing that,
in this example, the weighted errorwϵ 2 coef (α,ˆα) accounting for local sensitivity does not reveal a more
pronounced difference betweenP DE A andP DEB. Note that we did not computew Lyapϵ2 coef (α,ˆα)
because calculating the Lyapunov exponent is known to be NP-hard in general (as is the Kolmogorov
complexity [43]). Even though it can be estimated, it remains exponentially expensive for PDEs such
as KS. Finally, theN DCGmetric appears to better capture the difference between the two learned
PDEs than the Tanimoto coefficient, for which the two spurious terms have only a limited impact
because of their small associated coefficients.
PROS✔vsCONS✘
✔These metrics directly measure the success of coefficient recovery. Aside fromwϵ 2 coef andw Lyapϵ2 coef
which require evaluating partial derivatives w.r.t. to eachα i, they are simple to compute and easy to
interpret. Tanimoto coefficientT G indirectly considers both the structure and the coefficient involved.
N ϵ1 coefi is the only metric that guarantees the recovery of the structure while evaluating the coefficient
errors. By leveraging a local sensitivity analysis, the weighted errors convey more information because
they take into account the impact of each term on the induced dynamics.
✘They all require knowledge ofP DE GT . Coefficient errorsϵ p coef are relevant when the structure of
the identified PDE is correct otherwise there is no distinction between the coefficients of the correct
terms and those of the missing or wrongly identified functions. Tanimoto coefficientT G is not able
to strongly penalize PDEs containing spurious terms with small coefficients, yet likely to violate
physical properties and induce large solution errors in the long term.N ϵ 1 coefi can be used only if
the identified structure is correct. The weighted errors have an additional complexity burden due to
the computation of derivatives w.r.t.α i. Moreover, estimating the largest Lyapunov exponent in
wLyapϵ2 coef (α,ˆα) typically requires long trajectory integrations, making it computationally expensive.
Finally, a smallϵ p coef or a largeN DCGdo not necessarily imply sparsity.
✔ ✘
12

4 Metrics independent from the ground truth analytical form
Discovering a new physical law from data, rather than recovering a ground truth equation, corresponds
to the very essence of scientific progress. This task becomes especially crucial when dealing with
complex real-world phenomena which may rely on several interacting physical components making
it difficult, even for experts, to derive an appropriate mathematical model. Through their expertise,
scientists are sometimes able to formulate hypotheses about the presence of certain terms in the
equation, without however being able to provide its complete analytical form. This kind of scenario
arises in many fields, such as complex materials, biological systems, physical flows, or socio-economic
dynamics. This raises the key question of how to evaluate a discovered equation when there is no GT
theory or only a partial knowledge of its expression. This question still holds whenP DE GT is not
intended to be used in a metric directly through its symbolic form. In both cases, the direct analytical
comparison between the discovered and GT equations is not possible anymore. In this more realistic
setting, it is generally assumed that, in addition to the training setT, avalidation setVis available,
composed ofn V observation or simulation data. A standard way consists in numerically solving the
PDE identified fromT(provided that initial and boundary conditions are known, as well as
the time stepδ t) and in collecting a setEofn V estimated solutionsˆu(t,x). Then, it is possible
to compare, most of the time from a pointwise perspective, the underlying dynamics of the latter with
that of the validation datau(t,x) ofV.
We start this large overview with metrics based onprediction errors(Sec. 4.1), followed by a few
criteria focusing solely onsparsity(Sec. 4.2). The joint evaluationprediction+sparsityis addressed
in several metrics discussed in Sec. 4.3 before showing how to check thephysical consistencyof the
learned equation in Sec 4.4, when physical properties are available. Finally, Sec. 4.5 is devoted to the
assessment of theout-of-distribution generalizationcapability of the discovered PDE,i.e.whenVand
Eare not supposed to be i.i.d. according the same distribution asT.
4.1 Prediction errors
Metrics presented in this section primarily address QuestionQ1(which concerns the prediction
accuracy), and for some of them QuestionQ2(which deals with the physical consistency).
Solution error onu: Thesolution-mean squared errorM SE(ˆu, u) is arguably the most widely used
metric for assessing the ability of the identified equation to accurately predict the underlying physical
dynamics (see,e.g.[10, 36, 44]).M SE(ˆu, u) evaluates how well the estimated solutionsEfitin-
distributionvalidation dataV 4 when bothVandEhave been collected at the same (t,x) coordinates
allowing pointwise comparisons:
M SE(ˆu, u) =1 nV
nVX
i=1

ˆu(ti,x i)−u(t i,x i)
2 ∈R ≥0.(18)
As suggested in PDE-BENCH [45] where the authors compare several PiML models (PINN [1],
FNO [2], U-Net, etc.), it may be relevant to consider the scale-independent normalized version of
M SE(ˆu, u) defined as follows (also used,e.g., in ANN-PYSR [40], PITA [46] and in [47]):
nM SE(ˆu, u) =
PnV
i=1

ˆu(ti,x i)−u(t i,x i)
2
PnV
i=1 u(ti,x i)2 ∈R ≥0,(19)
4We assume here that the sets of validation dataVand estimated solutionsEare generated under the same physical
conditions and parameter distributions as those used for generating the training dataT. Out-of-distribution dynamics
will be discussed later when we will address the extrapolation ability of the discovered PDE.
13

or the normalized mean absolute error (nM AE):
nM AE(ˆu, u) =
PnV
i=1 |ˆu(ti,x i)−u(t i,x i)|PnV
i=1 |u(ti,x i)| ∈R ≥0.(20)
Note that in a couple of PDE discovery methods,e.g., PDE-NET [5], LLM-SRBench [28] or
KeplerAgent [48], a slight modification of Eq.(19) is used by subtracting from each term of the
denominator the spatial mean ¯uofu. This allows to remove the constant spatial mode and en-
sure that the metric primarily reflects the reconstruction accuracy of the non-trivial spatial structures.
Residual error fromu t: Instead of checking the prediction accuracy of the vector field solution ˆu, the
time derivatives ˆut can be considered and compared withu t. This amounts to evaluating the capacity
of the PDE to accurately capture the local dynamics of the system, as done,e.g., in PhysPDE [9],
SINDY-PI [10], MDBENCH [12], or MIO-SINDY [23]. Theresidual-mean squared error is defined as
follows:
nM SE(ˆut, ut) =
PnV
i=1

ˆut(xi)−u t(xi)
2
PnV
i=1 ut(xi)2 ∈R ≥0.(21)
Spectral error onF(u): In order to evaluate the learned PDE from a signal processing perspective,
the prediction error in the Fourier spacef M SEis computed in PDE-BENCH [45], constrained to low,
middle, and high-frequency regions. This allows to quantify how well the equation reproduces the
solution across different spatial scales, providing insight into whether both large-scale structures and
fine-scale dynamics are accurately captured.f M SEis defined from the estimated solutions ˆu(t,x) and
validation datau(t,x) as follows:
fM SE

F(ˆu(t, .)),F(u(t, .))

=
Pkmax
kmin |F(ˆu(t, .))− F(u(t, .))|2
kmax −k min + 1 ∈R ≥0,(22)
whereFis a discrete Fourier transformation, andk min,k max are the minimum and maximum indices
in Fourier coordinates. From Eq. 22, one can compute the overall error along the trajectory as follows:
f M SE

F(ˆu),F(u)

= 1 NT
NTX
i=1
fM SE

F(ˆu(i∗δt, .)),F(u(i∗δ t, .))

∈R ≥0,(23)
where, as a reminder,N T corresponds to the number of discrete temporal evaluations in [0, T] andδ t
is the time step. Note that at timet= 0,u(0,x) = ˆu(0,x) by construction.
Pointwise error heatmaps:Beyond the previous metrics which synthesize with one scalar the
prediction error of the discovered equation, most PDE discovery papers also assess visually the quality
of the equation by reporting in a heatmap, at each spatio-temporal coordinate (t,x), the corresponding
pointwise solution reconstruction absolute error|ˆu(t,x)−u(t,x)| ∈R ≥0, or|ˆu t −u t| ∈R≥0 if the
residual error is considered. This visualization is particularly well adapted for (1d+t) PDEs (see
Figure 3, first two panels, for the KS PDE).
Another heatmap can provide valuable physical insights by reporting the pointwise MSE or MAE
between the spatial Fourier transforms of the predicted and GT solutions as a function of time and
spatial wavenumber. This kind of representation (as illustrated in Fig. 3, last two panels) reveals how
the prediction error is distributed across spatial scales over time, indicating whether the discovered
PDE accurately captures both large-scale (low-wavenumber) and fine-scale (high-wavenumber)
dynamics.
14

Figure 3: Pointwise prediction absolute error between ˆu(t,x) andu(t,x) forP DE A (1st subfigure)
andP DEB (2nd), and the normalized mean absolute errornM AE, as defined in Eq.(20). On both
figures is also reported the rollout errorϵ t rollout(ˆu, u) (Eq.24) over time (dashed-lines). The 3d and 4th
panels represent the pointwiseM SEforP DE A andP DEB respectively, between the spatial Fourier
transforms of the predicted and GT solutions as a function of time and spatial wavenumber (up to 5).
The globalf M SEis also reported on the two figures.
Rollout error over timet: Even if, at first glance, two equations may appear similar (as observed
withP DEA andP DEB in Fig. 2) yielding lowM SEorM AEvalues over a limited temporal domain,
it should be kept in mind that the models recursively propagate their own predictions. Initially, if the
predicted trajectory may remain close to the GT, over longer rollout horizons, small initial inaccuracies
accumulate and eventually may lead to significant deviations. This error accumulation cannot be well
captured by pointwise metrics. To assess the stability and dynamical fidelity of the learned PDE, the
rollout errorϵ rollout is often used. This trajectory discrepancy involves a spatial integral at each time
step leading in the discrete case to the following expression:
ϵrollout(ˆu, u) =1 NT
NTX
i=1
ϵi rollout(ˆu, u) =1 NT
NTX
i=1
||ˆu(i∗δt, .)−u(i∗δ t, .)||2 L2(Ω) ∈R ≥0.(24)
As we will discuss later when addressing the question of generalization (see Section 4.5),ϵ rollout is
particularly well suited for evaluating the long-term extrapolation ability of the learned equation.
Instead of summarizing this error with one scalar as defined in Eq.(24), it may be worthwhile to plot
the curve representing the rollout errorϵ t rollout(ˆu, u) over time (see Figure 3). Note that this curve is
not monotonically increasing, as it represents the average error over all time steps between 0 andt.
This metric has been widely studied in recent PiML articles addressing the accumulation of
prediction errors when neural solvers are used as surrogate models for numerical schemes (see,e.g.,
PDE-Refiner [49], DiffusionRollout [50] or [51], to cite some of them).
Running Example: Back to the Kuramoto-Sivashinsky equation. Table 4 summarizes the evaluation
ofP DEA andP DEB according to the prediction metrics discussed in this section. For both the
solutionsuand the temporal derivativesu t, all evaluation metrics consistently demonstrate that
P DEA provides substantially more accurate estimated predictions ˆuand ˆu t thanP DEB. This is
visually confirmed by the the first two heatmaps presenting the pointwise errors on Fig. 3 which further
allow to identify which parts of the dynamics lead to the the largest errors. ForP DE B, interestingly,
we can notice that the error pattern is strongly correlated with the shock regions of the ground
truth (Fig. 2, left): whileP DE B captures the overall dynamics, it exhibits larger deviations near
propagating discontinuities and steep fronts, where the solution is more challenging to approximate
with this erroneous equation. The heatmaps on the Fourier transforms (two last panels of Fig. 3) show
that for bothP DEA andP DEB, the prediction error is mainly concentrated in the lowest wavenumber
modes (up to 4 for the latter), indicating that the largest discrepancies between the predicted and
ground-truth spectral components occur at large spatial scales. However, the f M SE(F(ˆu),F(u)) error
is approximately one order of magnitude smaller forP DE A than forP DE B, confirming the lower
quality of the latter. Finally, the curves of rollout errorϵ t rollout(ˆu, u), reported on Fig. 3 (dashed-lines),
15

Table 4: Application of the prediction error metrics (Sec. 4.1) to compareP DE A versusP DEB using
estimated solutions ˆufrom both of them and validation datausimulated from the KS ground truth
equationP DEGT as reference.
P DEA P DEB
ˆut =−0.99uu x ˆut =−0.89uu x −0.9u xx
−0.98uxx −0.985u xxxx −0.85uxxxx + 0.0004u−0.0008u xuxx
M SE(ˆu, u) (18) 0.0371 • 0.7557 •
nM SE(ˆu, u) (19) 0.0308 • 0.6277 •
nM AE(ˆu, u) (20) 0.1281 • 0.6605 •
nM SE(ˆut, ut) (21) 0.0003 • 0.0507 •
f M SE(F(ˆu),F(u)) (23) 1081.7 • 22011.1 •
ϵrollout(ˆu, u) (24) 0.8170 • 16.6252 •
show that the small initial error incurred byP DE B diverges dramatically as time passes while the
error associated withP DEA remains small. This is also reflected in the overall rollout error computed
att= 50, which is twenty times larger forP DE B (0.08170 versus 16.6252).
This running example clearly demonstrates that the graphical representations (heatmaps and
rollout error curves) provide a valuable complement to quantitative metrics such asM SE,M AE,
ϵrollout(ˆu, u) andf M SE(F(ˆu),F(u)). In particular, we must acknowledge that it is rather difficult to
interpret the value of the latter on its own and to determine whether 1081.7 can be considered small
without considering it in light of the Fourier heatmap.
PROS✔vsCONS✘
✔nM SEandnM AE-based metrics are scale invariant;f M SEprovides insight into the capacity of the
PDE to reproduce the solution across different spatial scales. Unlike the other metrics,ϵ rollout(ˆu, u)
allows to evaluate the stability of the PDE over time. The pointwise error heatmap enables the
identification of regions of the domain with the largest prediction errors (often in shock regions). The
heatmap on the Fourier transforms reveals how errors are distributed across spatial scales over time.
✘Small prediction errors do not ensure sparse PDEs and physical consistency. Therefore, the sole
use of these metrics does not guarantee the correct PDE has been discovered. The heatmaps cannot
be used directly for multi-dimensional PDEs.
✔ ✘
4.2 Sparsity
Based on the realistic assumption that most physical dynamics are governed by PDEs involving
only a few terms [52], the metrics presented in this section focus exclusively on QuestionQ3, which
concerns the simplicity and, hopefully, interpretability of the identified equations. The numerous
metrics which aim, more interestingly, at jointly considering the simplicity and the precision will be
discussed in Section 4.3
Nonzero coefficients in ˆα:A natural metric for evaluating the PDE sparsity simply consists
in counting the number of nonzero coefficients involved in the learned equation ˆu t =ˆα⊤.Θ, while
assigning an infinite score to an expression with no terms. This leads to the following scoreS terms(ˆα),
used,e.g., in [36]:
Sterms(ˆα) =
(
∞ifˆαis a zero vector,
1− |{ˆαi|ˆαi=0}| |Θ| ∈[0,1] otherwise. (25)
16

Table 5: Application of the sparsity metrics (Sec. 4.2) to compareP DE A versusP DEB.
P DEA P DEB
ˆut =−0.99uu x ˆut =−0.89uu x −0.9u xx
−0.98uxx −0.985u xxxx −0.85uxxxx + 0.0004u−0.0008u xuxx
Sterms(ˆα) (25) 3/5 • 1 •
C(ˆα⊤.Θ) (26) 11 • 18 •
The closerS terms is to 0, the sparser the PDE. It is worth noting that this score strongly depends
on the size of the dictionary considered. Consequently, the same PDE may yield different scores
depending on the number of functions available in Θ. For this reason,S terms is more useful when
comparing competing PDEs learned from the same set of terms.
Complexity of the expression tree of ˆα ⊤.Θ:Since the notion of model complexity is often
directly associated with the level of sparsity, the number of nodes, constant terms, and operations in
the expression tree representing the equation is frequently employed in symbolic regression during the
exploration of the search space. This measure of complexity can be defined as follows:
C(ˆα⊤.Θ) =size  ExpT ree(ˆα⊤.Θ)  ∈R >0,(26)
wheresize(.) outputs the number of elements involved in the expression treeExpT reeof the learned
equation. As done in [12], this metric can be easily computed by using theSymPyPython library.
The number of nodes in the expression tree is also used as a complexity measure for evaluating
equations in README [53], a framework for rapid equation discovery. AlthoughC(ˆα ⊤.Θ) allows
for a valid assessment of the complexity of certain functions through the expression tree (as is
the case, for example, for polynomials), note that it may be misleading if differential terms are
treated as atomic symbols, as this fails to account for their differential order. Therefore, particular
attention should be paid to properly representing the expressiveness associated with differential terms.
Running Example: Table 5 shows the values obtained fromP DE A andP DEB forS terms(ˆα) and
C(ˆα⊤.Θ). Both capture the fact thatP DE A is simpler thanP DE B. On the other hand, since we
have restricted the dictionary Θ, for the sake of simplicity, to a set containing only five functions,
P DEB is considered, according toS terms(ˆα), as not being sparse at all. EvenP DEA, which consists
of only three terms, is not considered to be that sparse.
PROS✔vsCONS✘
✔BothS terms(ˆα) andC(ˆα⊤.Θ) directly measure the sparsity, and thus, evaluate the potential inter-
pretability of the learned PDE. They are simple to compute and easy to interpret.
✘A high sparsity score (i.e.smallS terms(ˆα) orC(ˆα⊤.Θ)) does not guarantee a valid PDE has been
discovered. Two PDEs that are equivalent up to an analytical reformulation can lead to different spar-
sity scoresS terms(ˆα) or complexitiesC(ˆα⊤.Θ), depending for the latter on how they are represented
by the expression tree.S terms(ˆα) depends on the size of the dictionary Θ and thus can be overly
optimistic when a lot of functions are available, or overly pessimistic otherwise, as is the case in our
KS PDE illustration. If partial derivatives are considered atomic terms, neither criterion accurately
reflects the actual complexity of the expression.
✔ ✘
The limitations and risks associated with evaluating the quality of a PDE solely based on the
number of its constituent parts have led researchers to consider the ability of the equation to accurately
17

predict the observed dynamics alongside the sparsity. This strategy has resulted in the proposal of
numerous metrics based on a trade-off between the two characteristics, which are presented in the
following section.
4.3 Trade-off between prediction and sparsity
The metrics examined in Sec. 4.1 and 4.2 were intended to capture only one aspect of the PDE
evaluation. In this section, we review measures that deal with the task from a joint perspective, most
of them addressing both theprediction accuracy(QuestionQ1) andsparsityissues (QuestionQ3).
These different metrics differ from one another in the way they define and combine the two concepts.
Solution error–sparsity trade-off:In [54], considering the close relationship between the expres-
siveness of a PDE containing many terms and the risk of overfitting, the authors present a method for
symbolic representation distillation. They suggest to select, between competing PDEs, the one which
maximizes the fractional drop innM AEon the solutionsu(as defined in Eq. (20)) over the increase
∆Cin complexity. The latter is evaluated as a function of the atomic elements used in the equation,
e.g., the size of its expression tree as in Eq. (26). To this end, given two competing equationsP DE A
andP DEB, the followingScore(ˆαB|ˆαA) is computed (the larger the value, the better the evaluation
in favor ofP DEB):
Score(ˆαB|ˆαA) = −∆ log(nM AE(ˆuA,ˆuB)) ∆C(ˆαB|ˆαA) ∈R.(27)
In [55], the authors also leverage this metric in the context of PDE discovery for modeling Alzheimer’s
disease. They useScore(ˆα B|ˆαA) for selecting the equation governing the best the underlying
reaction-diffusion system.
Residual error–sparsity trade-off:In [32], the following reward function is defined to assess the
identified PDE, as a multiplicative trade-off between a sparsity term and the coefficient of determina-
tionR 2 on the residuals of the equation:
Reward1(ˆα) = (1−c0 log10 |S(ˆα)|)| {z }
Sparsity
×

1−
PnV
i=1

ut(xi)−Θ ⊤ i .ˆα 2 PnV
i=1 (ut(xi)−¯ut)2
!
| {z }
1−Residual error≈R 2
∈R >0,(28)
where|S(ˆα)|=|{Θ i :ˆαi ̸= 0}|corresponds to the number of nonzero coefficients involved in the
PDE, andc 0 is a constant that governs the trade-off between simplicity and accuracy; the second
term considers the residuals of the PDE that can be computed from the validation setV. The higher
Reward1(ˆα) is, the better is the evaluation of the identified equation ˆut =ˆα⊤.Θ.
In the same vein, a reward functionReward 2(ˆα) is presented in [56] to evaluate the PDE from a
sparsity and residuals perspective. This metric is defined as follows:
Reward2(ˆα) =1−ξ 1 × |S(ˆα)| −ξ2 ×depth

ExpT ree(ˆα⊤.Θ) 
1 +Err(ˆα⊤.Θ) ∈R,(29)
whereErr(ˆα⊤.Θ) is defined as the error on residuals||u t −ˆα⊤.Θ||2 2,depth  ExpT ree(ˆα⊤.Θ)  is
the depth of the PDE expression tree, andξ 1 andξ 2 are two constants that control the trade-off.
In NeuroSymBO [25], the authors leverage a criterion similar to Eq.(29), withξ 2 = 0 and using
Err(ˆα⊤.Θ) =nM SE(ˆu, u) as defined in Eq.(19).
18

Likelihood–sparsity trade-off:Information-theoretic criteria such as Akaike Information Criterion
(AIC) [57], Bayesian Information Criterion (BIC) [58], and their variants, are used to evaluate PDEs
according to an accuracy/complexity trade-off. Their difference with the previously discussed metrics
lies in the use of the likelihood of the dataset as a probabilistic measure of fitness that can be fur-
ther employed for uncertainty estimation. For all of them, a smaller value indicates a better evaluation.
Akaike Information Criterion (AIC) [57] is a statistical metric defined as follows:
AIC(ˆα) = 2|S(ˆα)| −2 log(L(T,ˆα))∈R,(30)
where, as a reminder,|S(ˆα)|corresponds to the number of nonzero coefficients involved in the expres-
sion, andL(T,ˆα) is the log-likelihood of the data, given the considered PDE. A common likelihood
function in PDE discovery is based on the residual sum of squares which amounts to calculating
||ut −Θ ⊤.ˆα||2 2, yielding the following correctedAIC c(ˆα) for the training setTof sizen T :
AIC c(ˆα) =nT log ||ut −Θ ⊤.ˆα||2 2 nT + 2|S(ˆα)| ∈R.(31)
In MIO-SINDY [23] and also in [59], the authors employAIC c as model selection criterion
for SINDY, especially to rank the candidate models with respect to the regularization parameter
associated with the sparsity-inducing norm. Note that Eq. (31) can be employed in the same way by
using the field valuesuinstead of the time derivatives. In this case, it is necessary to consider the
squared differences between the ground truthu(t,x) and simulation data ˆu(t,x) from the identified
PDE.
Also an established metric, theBIC(Bayesian Information Criterion) [58], known as the Schwarz
information criterion, has experienced renewed interest in model selection, particularly through recent
symbolic regression models for comparing learned analytical expressions. It differs fromAICin the
way it defines model complexity. WhileAICsolely considers the number of functions in Eq. (31), the
complexity is heavier inBICin the sense that it takes into account the sizen T of the datasetT, so
penalizing more and more complex models as the dataset grows. More formally,BICis defined in
our PDE evaluation setting as follows:
BIC(ˆα) =log(nT )|S(ˆα)| −2log(L(T,ˆα))∈R,(32)
whereL(T,ˆα) can be defined in the same way as forAIC.
While it is argued in [59] thatBICcan be efficiently used to select the best equation inferred by
SINDY, it is demonstrated in [38] that the minimization ofBICcould lead to overfitted equations
with unnecessary hypotheses, especially when the model is learned from an overcomplete candidate
library Θ. To overcome this issue, the authors present an uncertainty-penalized Bayesian Information
Criterion (U BIC) which penalizes the identified PDE both in terms of complexity and quantified
uncertainty. The latter is estimated by using Bayesian regression to compute the coefficient of
variation of the posterior PDE coefficients.
Finally, a Physics-informed Information Criterion (P IC) is used in [11] to evaluate the quality of
a learned PDE.P ICtakes the following form:
P IC(ˆα) =Lr(ˆα)×Lp(ˆα)∈R,(33)
whereL r is a redundancy loss measuring the parsimony of the PDE andL p is a physical loss
evaluating its precision. Using a moving horizon technique,L r represents the coefficient of variation
19

CVof the learned parameters over different moving horizons, under the realistic assumption that
correct dominant terms are stable with smallCV.L p measures the errors of a PINN optimized
using the learned PDE as a ground truth. The authors show evidence thatP ICperforms better
thanBICandAICin the presence of high noise. However, this improvement should be consid-
ered in light of the additional computational burden associated with training (i) a neural surrogate
to generate smoothed meta-data and calculate derivatives and (ii) a PINN to evaluate the physical loss.
Kolmogorov complexity ofΘ ⊤ ˆα:Minimum Description Length principle [60] (M DL) is closely
related toAICandBIC, but it is based on a distinct information-theoretic principle.M DLposits
that the best representation of a datasetTis the one that compressesTmost (leading to the so-called
Kolmogorov complexity), using symbols from a finite alphabet. In this context, the presence of any
regularity inT, as is often observed in physical dynamical systems, can be leveraged to compress the
data through derivative terms. A model is preferred over another if it leads to the shortest description
length, achieving the best trade-off between simplicity and predictive accuracy.
As far as we know,MDL, used as a criterion for discovering mathematical expressions, has been
applied in symbolic regression primarily on equations without spatial derivative terms. The main
reason is that its direct application to PDEs is non-trivial due to the additional complexity induced
by differential operators, which cannot be properly assessed simply by counting the number of terms
in the equation or the number of nodes in its expression tree. Nevertheless, allowing accuracy and
complexity to be directly traded-off,MDLprinciple has been leveraged in [61] for selecting ODE
candidate representations lying on the Pareto front. Since the Kolmogorov complexity associated to
MDLhas been shown to be incomputable [62], inMDLformer[63], the authors suggest to learn
a neural network which enables a robust estimation. InAI-Feynman[64],MDLis also employed
for selecting the winning function among symbolic regression candidates. Recast in our setting, this
criterion is defined as follows:
M DLF ey(ˆα) = log2 N(ˆα) +λlog2

max

1, ϵrr(ˆα) ϵd

∈R,(34)
whereϵrr(ˆα) is a fitting error of Θ ⊤ ˆα(e.g.M SE,M AE),ϵd is a normalization constant, andN(ˆα)
is the rank of the equation size on the list of all candidates compared.
InSymLang[65], aMDL-regularized Bayesian model selection is presented based on the following
MDLscore:
M DLSym (ˆα) =−logp

T |e(Θ⊤ ˆα)  +λlen  ExpT ree(Θ⊤ ˆα)  ∈R,(35)
whereλis a trade-off hyperparameter, and the description lengthlen

ExpT ree(Θ⊤ ˆα)  counts the
cost of encoding the expression treeExpT ree(Θ ⊤ ˆα) of the equation and its constants. This function
is defined as follows:len

ExpT ree(Θ⊤ ˆα)  = P v∈nodes(e) log2 |Ov|+|Θ|.log 2(cmax/ϵ),where|O v|is
the local branching factor at nodev, andc max andϵare constant range and precision. The authors
point out that this criterion is related toBIC(32) andAIC(30) but, unlike them, they stress the
fact that the structural complexity is better measured inM DL Sym (ˆα) by tree description length
than parameter count alone.
Running Example: Table 6 presents the results obtained fromP DE A andP DEB on our running
example with the metrics that consider the trade-off between accuracy and sparsity. Since several
of them require specifying hyperparameter values, we used the ones reported in the original papers
introducing these metrics. Following their experimental setups, we used:c 0 = 0.2 inReward 1(ˆα)
[32];ξ 1 = 0.01 andξ 2 = 0.0001 inReward 2(ˆα) [56];ϵrris defined as theM SE,N= 1,ϵ d = 10−15,
λ=n 1/2 V inM DLF ey(ˆα) [64];c max = 10,ϵ= 10 −6,λ= 0.1 inM DL Sym (ˆα) [65]. As visually
20

Table 6: Application of the accuracy-sparsity metrics (Sec. 4.3) to compareP DE A versusP DEB
using validation dataVsimulated from the KS ground truthP DE GT as reference. Note that N/A
means “Not Applicable” becauseScoreis conditional on the increase in complexity (in our case from
P DEA toP DEB) and not the other way around.
P DEA P DEB
ˆut =−0.99uu x ˆut =−0.89uu x −0.9u xx
−0.98uxx −0.985u xxxx −0.85uxxxx + 0.0004u−0.0008u xuxx
Score(ˆαB|ˆαA) (27) N/A -0.2343
Reward1(ˆα) (28) 0.9043 • 0.8166 •
Reward2(ˆα) (29) 0.0306 • 0.0002 •
AIC c(ˆα) (31) −1.1E+07 • −5.4E+06 •
BIC(ˆα) (32) −1.1E+07 • −5.4E+06 •
M DLF ey(ˆα) (34) 35234.7 • 42738.1 •
M DLSym (ˆα) (35) −5.3E-06 • −2.7E-06 •
highlighted by the green dots in the table, all metrics are able to identifyP DE A as the best
equation. Nevertheless, some differences can be observed in the gap between the two PDEs. In
particular,Reward 2(ˆα) andM DLSym (ˆα) seem to better capture the expected large difference in
quality betweenP DE A andP DEB, thanks to the presence of the size of the expression tree in
the complexity formulae. The other metrics tend to smooth out this difference due to the use of
the number of functions involved in the equations. RegardingAICandBIC, the experiments on
the Kuramoto-Sivashinsky data reveal a particular behavior of these two information criteria. By
construction, the likelihood term in both metrics rapidly outweighs the complexity penalty as the
number of data points increases. Because this experiment comprises 1,064,000 data points, theAIC
andBICvalues forP DE A andP DEB mainly reflect the predictive performance of the equations
rather than their sparsity. The latter is hidden behind the massive numbers obtained from the
likelihood.
PROS✔vsCONS✘
✔All these metrics have the advantage of combining two desirable properties of a good PDE: accuracy
and simplicity. They reduce equation evaluation to a single number, making it easy to rank competing
equations. The size of the expression tree seems to be more relevant for measuring complexity than
simply counting the number of terms in the equation.P ICfurther takes into account information
about the residuals of the learned equation.
✘Tuning hyperparameters is required for the evaluation ofReward 1, Reward2, M DLF ey and
M DLSym .Reward 1,AIC,BIC, andPICuse the number of terms in the equation as a measure
of simplicity. This is valid for PDEs composed of functions with similar structural complexity. By
construction, the likelihood term in bothAICandBICquickly overwhelms the effect of the com-
plexity penalty as the sample size increases. Finally,P ICcomes with an additional computational
burden (learning of two neural networks).
✔ ✘
4.4 Physical consistency
Although difficult to implement due to its dependence on prior knowledge that is not always available,
verifying that the discovered equation does not violate important physical properties is crucial in
PDE evaluation. In particular, checking physical consistency makes it possible to avoid overstating
21

the validity of a supposedly new law. Indeed, a low reconstruction error associated with a sparse
expression does not guarantee that the identified PDE represents a plausible physical theory. In this
section, we discuss various ways of verifying that certain physical constraints are satisfied, thereby
addressing QuestionQ2.
Consistency checking through small residuals:A widely used strategy in PiML to assess the
physical consistency of a model consists in verifying the PDE residuals are low. For instance, in
PINNs [1], this means that the dynamics optimized during training isconsistent with the physics
modeled by the known PDE. The situation is substantially different in post-hoc evaluation. In
particular, observing small residuals offersweaker physical guarantees when the analytical
expressionP DEGT is either unavailable or intentionally not used. In this case, a small
residual error (as defined in Eq. (21)) on validation dataVonly indicates the absence of overfitting
through a compatibility with the learned differential operator ˆN[u]. But it does not ensure that the
discovered PDE is the true governing law of the system. To illustrate the risk of over-interpreting low
residuals, Fig. 4 reports in 3D the solutions of both the Kuramoto-Sivashinski equation (P DE GT on
the left) and of a PDE that would satisfy the initial/boundary conditions and return 0 everywhere else
(right). Although such a hypothetical PDE does not satisfy then-times differentiability requirement
of a validn-order PDE, it can still be learned by a PiML algorithm, if no precautions are taken. We
can see that this PDE leads to zero residuals while completely missing the true physical dynamics.
Note that this problem has been addressed from both optimization and statistical generalization
perspectives in [15] when dealing with PINNs.
Consistency checking through explicit physical properties:Beyond analyzing the residuals,
one can also leverage different types of physical properties for evaluating the validity of a PDE. As
discussed later in Sec. 5, depending on the domain of study and the level of expertise available,
these properties can be either(i) a priori known, (ii) assumed to hold or (iii) learned from
data. They can be expressed through various types of constraints to be satisfied, such assymmetries,
conservation laws, dimensional consistency, etc.
Among them,symmetriesplay a key role as they correspond to a fundamental principle in physical
systems, defining their invariance under transformations such as translations, rotations, and scaling.
For this reason, symmetries, which are present in many datasets, have become an important algo-
rithmic and theoretical object of study in the machine learning community (see,e.g.[66, 67]). Their
incorporation into PiML processes has concerned the optimization of neural PDE surrogate solvers
[68, 69, 70], as well as the discovery of equations from data [44, 64, 65, 71]. Regarding this last research
direction, the use of symmetries in symbolic regression allowed to drastically reduce the number of
candidate expression trees by pruning the hypothesis space before search. This can therefore prevent
the discovery of inconsistent PDEs that may appear relevant at first glance if one considers only
prediction errors and sparsity criteria.
Respectingconservation lawsis also crucial in PDE discovery, as it improves the physical plausi-
bility of the identified equation. InProbConserv[72], a general framework is presented for satisfying
conservation laws in equation discovery from the finite volume perspective. The authors address this
task by combining the integral form (rather than its differential form) of the conservation laws with
a Bayesian update. In [73], the authors presentPINN-Proj, a PINN-based model which leverages a
new projection method to satisfy conservation laws. Experimental results are reported showing that
PINN-Projoutperforms a classic PINN thanks to this physical consistency requirement.
Additionally, checking thedimensional consistencycan be also of great help to filter out invalid
models. This strategy has been efficiently used in the DHC-GEP method [74] for discovering gov-
erning equations in gene expression programming. In [75], the authors use attribute grammars to
ensure the dimensional consistency of the discovered equations and demonstrate their effectiveness on
Feynman benchmarks. Note that, although dimensional consistency is generally considered as a hard
22

Figure 4: Possible pitfall of over-interpreting small residuals: 3D solutions of the Kuramoto-
Sivashinsky equationP DEGT (left) and solutions simulated from a learned equation that would satisfy
the initial/boundary conditions and return 0 everywhere else (right), leading thus to zero residuals.
(binary) constraint, some equation discovery algorithms employ it through a regularization term, only
penalizing candidates that do not satisfy it. This is the case for NEXUS [76], built on graph-based
equation representation, evolutionary optimization, and adaptive reinforcement learning and where
the dimensional consistency for a candidate equation ˆu t = Θ ⊤ ˆαis defined, using our notations, as
follows:
D

Θ⊤ ˆα  = X
t∈T(Θ⊤ ˆα)
log
 [t]
[ut]

,(36)
where [t] denotes the dimension of sub-expressiont, [u t] is the target dimension andT

Θ⊤ ˆα  is the
set of all sub-expressions in Θ ⊤ ˆα.
It is important to emphasize that the approaches described above primarily fall within the PDE
discovery setting. They therefore focus on enforcing physical constraints embedded in the optimization
process or used, as in symbolic regression, to select the most consistent models along the Pareto
front. Nevertheless, we argue that these very same physical properties (symmetries, conservation
laws, dimensional consistency, etc.) can also be exploited to evaluate a posteriori learned PDEs,
although they are surprisingly often overlooked in the post-hoc evaluation literature. In this setting,
they will complement certain physical properties that may be assumed to hold for the physical system
under study (e.g.convection, diffusion, advection, etc.) or other consistency-based metrics that
are derived from numerical analysis, such asforward–backward verification, mesh refinement study,
temporal convergence, as presented in the following. Below we attempt to categorize the main physical
properties that can be checked post-hoc according to the difficulty of their assessment.
1.Inspection of the structural form of the PDE: Some structural properties can be evaluated
by examining the symbolic expression of the equation. Here are a few simple examples intended
to facilitate non-specialist reader’s understanding: (i) if the underlying physical process is known
to bedissipative(as in heat conduction, viscous fluid flows, damped mechanical systems, etc.),
one would therefore expect the term−∇ ·(c∇u) to appear in the PDE; (ii) if we are studying
systems related to atmospheric circulation, ocean currents, or heat transport in fluids, thecon-
vectionterm∇ ·(cu) should be present; (iii) as a third illustration,self-advection, which occurs
when a field transports itself, as in fluid dynamics, implies that the term (u· ∇)ushould appear
in the symbolic expression. Even though identifying diffusion, convection, or advection mecha-
nisms solely from the structure of a PDE can provide useful physical insights, note that it does
23

not guarantee that the corresponding physical properties are actually satisfied by the model.
The verification generally requires more advanced analytical manipulations, such as deriving
conservation laws or energy estimates (see next point2.). Other properties can be assessed by
inspecting the form of the PDE. This is the case ofspatial and temporal symmetriesthat can be
verified if there is no term of the formxF(u) ortF(u). On the other hand, while often difficult
to enforce during the identification process,dimensional consistencyis much easier to check a
posteriori by simply inspecting each term of the equation.
2.Analytical derivation from the PDE:Many properties, includingconservation laws, posi-
tivity preservation, energy dissipation, and certaininvariancesrequire symbolic manipulation of
the equation. For instance, checking forconservation lawsconsists in determining whether the
PDE can be rewritten in conservative form,u t +∇ ·F=S, by identifying a flux functionF,
and a source termS. As an example, for reaction–diffusion PDEs, the mass conservation law is
not generally expected to hold, while this is required for Navier–Stokes PDEs which describe the
motion of viscous fluids. On the other hand,positivity preservationis generally harder to assess
than conservation laws, as it is not solely determined by the structure of the PDE but depends
on the global properties of the associated evolution operator. One possibility is to resort to the
maximum principle[77] according to which if the solution of the PDE were to become nega-
tive, it would attain a first negative minimum, contradicting the maximum principle. Hence,
any solution associated with non-negative initial data remains non-negative for all times in its
interval of existence. Note that this analytical verification is limited to elliptic and parabolic
PDEs. Verifyingenergy dissipationis also a non-trivial task in general: it requires deriving an
appropriate energy law and proving analytically that the associated energy decreases over time,
which may be difficult for complex nonlinear models.
3.Simulation-based verification:Because a PDE is meant to model dynamics leading to a
solutionu(t,x),well-posednessanduniquenessare also desirable properties when assessing the
quality of a learned PDE. However, these structural properties, which generally require advanced
mathematical analysis, are often difficult to establish rigorously. A practical solution is to
leverage simulations (provided the initial/boundary conditions are known) and manipulating
data instead of analytical equations to evaluate a property. For instance, by performing a
convergence study,i.e.by refining the spatial mesh or time step, and checking if the solution
u(x, t) converges, we can evaluate the risk of instability or ill-posedness of the learned PDE (see
Sec. 4.5 for more details). When priors are available about thereversibility[78] of the physical
phenomenon, an inverse reconstruction procedure can be performed consisting of simulating
the learned PDE forward in time and then integrating backward from the predicted final state
u(T,x) to assess whether the initial conditions are recovered or not. For example, if the model
is assumed to describe a dissipative system (e.g.reaction-diffusion, Navier–Stokes PDEs), the
reconstruction of the initial conditions is not expected to hold. On the other hand, to verify some
physicalinvariance, it suffices to apply the considered transformation to the PDE, then solve the
equation (provided that it is numerically possible) and compare the resulting solutions with the
original ones. The validation of the invariance can then be done (up to numerical errors and the
choice of a decision threshold) using standard metrics such as those discussed so far (e.g.,M SE,
M AE, etc.). Note that other properties such as the preservation ofpattern formation, can also
be assessed visually from simulations (this is the case of the Kuramoto-Sivashinsky equation),
particularly in the case of (1d+t) PDEs.
Let us conclude this section with a real-world illustration of how physical properties can be used
for evaluating a PDE. The considered applied setting is surface engineering, and more specifically
self-organization of matter induced by laser–matter interaction, for which the Kuramoto–Sivashinsky
PDE is a candidate to (partially) model this complex phenomenon. Therefore, through this example,
24

Figure 5: Subset of Scanning Electron Microscopy (SEM) images of surfaces irradiated by a femto-
second laser with cross-polarized double pulses, varying the number of double pulses between 0 and
50, when the laser fluence= 0.25 J/cm2 and the delay is 36ps (between the two laser pulses) [79]. Even
without expertise, the visual inspection reveals that spatial invariance and the growth of structures
should be reflected in the discovered PDE.
we remain within the scope of our running example.
Running Example: In laser–matter interaction, a femtosecond laser is typically employed to texture
the surface of a matter and endow it with specific physical features (e.g., wettability, hydrophobicity,
antibacterial properties, etc.). The observed dynamics (see,e.g., SEM images on Fig. 5 used in [79]),
together with the prior knowledge that this type of physical system leads to pattern formation, makes
it possible to establish a number of properties that a learned PDE should satisfy.Without assuming
that the KS equation is a possible candidatefor modeling this phenomenon, one may reasonably
expect the discovered PDE to be spatially symmetric under translations, to possess both linear (for
diffusion or anti-diffusion) and nonlinear terms (saturation of instabilities, generation of chaos), and
to be dissipative. These properties can thus be checked post-hoc to assess the physical consistency of
the learned PDE.
As a toy example, let us consider the following discovered equation: ˆu t =−1.0uu x −1.0u xx −
1.0uxxxx + 1.0xuwhich is very close toP DEGT . We can observe that: (i)uu x seems relevant because
it represents the self-advection of the field and is responsible for nonlinear distortion (non linear
patterns); (ii) similarly,u xx plays the role of a destabilizing term that allows the growth of structures;
(iii)u xxxx makes sense because it confirms the dissipative nature of the system and prevents blow-up
by stabilizing small scales which is key in pattern formation; (iv) Finally,xuassumes that pattern
formation is spatially dependent which is not consistent with the observed dynamics. In conclusion,
without additional calculations or simulations, provided some background expertise, we can state
by simply inspecting its structural form that this learned equation is not a physically plausible law
because of the spurious last term.
PROS✔vsCONS✘
✔Well-founded physics-informed approach to PDE evaluation. Help detect physical inconsistency
even when prediction errors are small and the PDE is sparse.
✘Require prior knowledge of the physical properties to be verified. Some properties may be difficult
or impossible to formally verify.
✔ ✘
4.5 Out-of-distribution generalization
As in classic statistical learning, the ability of a PDE, optimized from a set of dataT, to accurately
predict unseen states within the training conditions does not imply that this equation is the governing
one. Indeed, even an incorrect PDE may accurately predict the system’s evolution over short time
horizons, while failing to capture the true governing dynamics. As a result, reconstruction errors
25

remain small, and the evaluation metrics discussed so far and computed on anin-distributionvalidation
setVmay lead to an overly optimistic assessment of the model’s quality. This is why QuestionQ4
concerns the capacity of a discovered PDE to generalizeout-of-distribution(OOD).
OOD generalization can be evaluated through several experimental settings that probe the
robustness and stability of an equation beyond the conditions used for its identification. Common
scenarios encountered in PDE discovery include the generalization tounseen initial conditions (IC),
unseen boundary conditions (BC)orlonger prediction horizons. Other settings, such thatparameter
values outside the training rangeorvarying dynamical regimescan be considered but they are less
applicable when dealing with post-hoc evaluation. Indeed, regarding the former, it is less meaningful
to modify a posteriori a learned coefficient associated with a derivative term.
V arying initial and boundary conditions:Performing experiments under changing IC and BC
provides insight into whether the discovered PDE captures the underlying physical law rather than
merely fitting the observed data distribution. In real world situations, where the governingP DE GT
is unknown or only partially characterized, assessing the OOD generalization capacity is generally
more difficult because it requires either additional observation data obtained from varying conditions
or a learned (neural) operator allowing the generation of OOD trajectories from different IC and BC
(see Sec. 5 for a more in-depth discussion). WhenP DE GT is known, evaluating OOD generalization
capabilities is relatively straightforward, since the governing law can be used at will to generate
simulation data under changing IC and BC. The following evaluation protocol can then be applied.
Let us consider an equationP DE T learned from the training setTgenerated with the following IC
and BC respectively:
u(0,x)∼ Dic T ,∀x∈Ω
u(t,0), u(t, L)∼ Dbc T ,∀t∈[0, T]
where the spatial domain is supposed to be: Ω = [0, L].
1. Generation of two sets ofn V OODvalidation datafromP DE GT :
•Simulate a setV ic withu(0,x)∼ D ic OOD , whereD ic OOD ̸=D ic T (e.g.Gaussian, Sinusoidal,
random Fourier modes, parametric, etc.).
•Simulate a setV bc withu(t,0) andu(t, L)∼ Dbc OOD by selecting one of the following bound-
ary condition distributions (different fromD bc T ):
–Dirichlet: solutions are directly imposed at the boundary;
–Neumann: values of the derivative are imposed;
–Robin: combination of both;
–Periodic: derivatives must match at opposite boundaries;
–others.
2. Generation of two sets ofn V OODestimated solutionsfromP DE T : :
•Simulate a setE ic withu(0,x)∼ D ic OOD .
•Simulate a setE bc withu(t,0) andu(t, L)∼ Dbc OOD .
It is important to note that to allow pointwise or trajectory comparisons,V ic (resp.V bc) andE ic
(resp.E bc) are simulated at the same (t,x) coordinates.
3. CompareV ic (resp.V bc) withE ic (resp.E bc) and evaluate whetherP DE T still accurately
captures the underlying governing lawP DE GT under varying conditions. This evaluation can
be performed using primarily metrics presented in Sec. 4.1.
26

Figure 6: Simulation data obtained from the GT KS equationP DE GT ,P DEA andP DEB with
two initial conditions different from those used in the running example: (left)IC 2 = sin(2πx/L) +
0.3 sin(6πx/L+ 0.5); (right):IC 3 = cos(6πx/L) + 0.2 cos(10πx/L+ 0.7). We can note that changing
the IC while keeping the same analytical expression leads to very different pattern formations.
Note that the previously described protocol is similar to the one used in PhysPDE [9] where the
authors change the boundary conditions and evaluate their model’s OOD generalization capacity
through the mean squared residuals.
Long-horizon prediction:Thetemporal generalizationis also widely employed as an OOD scenario.
Instead of evaluating the learned PDE on unseen IC and BC,P DE T is simply assessed over longer
horizons than those used during the discovery process. In this case, one can resort to the rollout error
ϵrollout(ˆu, u) (already defined in Eq. 24) which is particularly well suited for evaluating the long-term
stability ofP DET (as used,e.g., in AutoSINDy [80]). We remind below its definition:
ϵT ′ rollout(ˆu, u) =1 N ′ T
N ′ TX
i=1
ϵi rollout(ˆu, u) =1 N ′ T
N ′ TX
i=1
||ˆu(i∗δt, .)−u(i∗δ t, .)||2 L2(Ω) ∈R ≥0,(37)
whereN ′ T is supposed here much higher than the number of temporal stepsN T used for learning
P DET .
Numerical OOD generalization:To conclude this section, we mention in the following an approach
borrowed from numerical analysis [81] to investigate the generalization ability of the discovered PDE
through the lens of a convergence study, which can be viewed as a form ofnumerical distribution
shiftevaluation. The principle consists in assessing the mesh convergence by numerically solving the
equation at different spatial resolutions. More formally, the following property is expected to hold:
Conv x(ˆα) = 0,(38)
whereConv x(ˆα) = limδx→0 ||ˆu−ˆuδx||. Eq. (38) means that as the spatial discretization is progres-
sively refined, the numerical solution converges to a stable limit. This approach can therefore reveal
pathological behaviors and help identify PDEs exhibiting low numerical robustness and potential ill-
posedness. Note that the convergence analysis can be equally applied to the temporal discretization,
leading to:
Conv t(ˆα) = lim δt→0 ||ˆu−ˆuδt||.(39)
Running Example: The OOD generalization capacity ofP DE A andP DEB in different scenarios
is reported in Table 7. Through the different changes of initial conditions, we can note thatP DE B,
because of its erroneous form, is not always able to accurately extrapolate. The most striking
illustration is given byIC3 for which theM AEincreases significantly (0.898). This deteriorated
behavior is confirmed by the simulation data presented in Fig. 6 (last panel). We can see thatIC3
prevents the pattern formation process withP DEB. By evaluating the individual terms of this PDE,
we noticed thatu xxxx becomes too small to play the expected role in the formation of non linear
27

Table 7: Capacity of out-of-distribution generalization ofP DE A andP DEB in three scenarios: (i)
varying initial conditions IC. TheM AEis used as evaluation metric. Note thatIC 1 corresponds to
the conditions of the running example; (ii) longer horizons at different timesT≥50. The rollout error
is evaluated at time 50,100,200 and 300; (iii) mesh and time convergence.
P DEA P DEB
OOD scenarios ˆut =−0.99uu x ˆut =−0.89uu x −0.9u xx
−0.98uxx −0.985u xxxx −0.85uxxxx + 0.0004u−0.0008u xuxx
IC 1 = cos(2πx/L) + 0.5 cos(4πx/L+ 0.3) 0.128 • 0.661 •
IC 2 = sin(2πx/L) + 0.3 sin(6πx/L+ 0.5) 0.126 • 0.572 •
IC 3 = cos(6πx/L) + 0.2 cos(10πx/L+ 0.7) 0.052 • 0.898 •
ϵT ′=50 rollout(ˆu, u) 0.817 • 16.6 •
ϵT ′=100 rollout (ˆu, u) 14.1 • 38.8 •
ϵT ′=200 rollout (ˆu, u) 36.8 • 55.4 •
ϵT ′=300 rollout (ˆu, u) 48.3 • 61.1 •
Conv x(ˆα) 0 • 0 •
Conv t(ˆα) 0 • 0 •
patterns. The analysis of the rollout-errors is also very informative. While we already noted that
P DEA leads to a much smallerϵ rollout(ˆu, u) in the training time interval [0, T] (Fig. 3), the gap
between the two PDEs tends to narrow as the time horizon is extended (shifting from a ratio of
20-to-1 to 1.3-to-1). This is confirmed by the simulations ofP DE GT ,P DEA andP DEB between
[0,300] presented in Fig. 7. AlthoughP DE A appears to be visually much closer toP DE GT than
P DEB, with similar patterns still clearly visible aftert= 50, the rollout error (dashed line) reveals
thatP DEA also deteriorates rapidly, eventually reaching nearly the same error level asP DE B
atT= 300. This example clearly illustrates how even small discrepancies in the analytical form
of a PDE can lead to dramatic errors in extrapolation. In particular, althoughP DE A contains
the correct terms and its coefficients are very close to those ofP DE GT , these seemingly minor
differences are sufficient to cause a substantial degradation in long-term predictions. We can
therefore conclude that the rollout error should play a crucial role in PDE evaluation, which is
far from being the case in papers on the subject. Finally, regardingConv x(ˆα) andConvt(ˆα), the
numerical convergence of bothP DE A andP DEB (in time and space) is satisfied, which is a good
point from an evaluation perspective, but it does not allow us to distinguish between the two equations.
PROS✔vsCONS✘
✔Simulating the learned PDE with varying IC and over longer time horizons is very informative
about the robustness of the equation to OOD.
✘Performing OOD experiments requires either the ground truthP DE GT to be known or access to
additional OOD observation data which is not always possible in real-applications.
✔ ✘
5 Practical guidelines for evaluating PDEs and perspectives
The in-depth analysis conducted in this paper from the extensive literature on equation evaluation,
spanning machine learning, information theory, symbolic regression, and numerical analysis, reveals
that a universally accepted methodology for a systematic evaluation remains elusive. To help
the research community working on this topic move toward a standardized process, and avoid
28

Figure 7: Long-horizon simulations (T∈[0,300]) of the Kuramoto-Sivashinsk GTP DE GT (left),
P DEA (center) andP DE B (right). The rollout errorϵ t rollout(ˆu, u) over time (dashed-lines) is also
reported.
overstatements regarding the validity of a discovered PDE, we formulate in this section practical
guidelines based on the findings presented in this survey. We finish the paper by proposing some
promising research directions in this area, which we consider to be still in its early stages.
Discover or Recover? That’s the question:If one aims at evaluating a novel PDE learning
algorithm rather than discovering genuinely a new theory, it is recommended, as widely done in the
literature, to employ benchmark equations for which the complete ground truth is known, including
the analytical formP DE GT , the parameter values as well as the associated initial and boundary
conditions. In this setting, assuming access to this prior makes it possible, as a proof-of-concept, to
assess the algorithm’s ability toaccurately recover the governing lawP DE GT . Evaluation can
then be carried out using the different metrics described in Section 3. In light of our analysis and the
results obtained on the Kuramoto-Sivanshinsky PDE, we particularly recommend usingT P R(α,ˆα)
(4),wϵ 2 coef (α,ˆα) (12) andN DCG(α,ˆα) 14.
WhenP DEGT is not perfectly recovered, it becomes crucial to assess the impact of a spurious term
or a coefficient deviation. Claiming that the PDE is “well recovered” on the basis of its similarity
toP DEGT , without measuring the consequences of even small differences cannot be considered a
scientifically valid approach. However, based solely on metrics of Section 3, a number of papers
conclude their experiments by typically stating: “Our novel algorithm A outperforms method B because
the symbolic shape and coefficients of the PDE identified with A are more similar toP DE GT than that
of competitor B.”” We have emphasized in our study that the presence of small errors in the coefficients
associated with certain terms, or the erroneous inclusion of an irrelevant function, can have dramatic
consequences on the modeled dynamics. The Kuramoto–Sivashinsky PDE provides a good illustration
of this behavior, with terms that have a nonlinear effect and slight changes in their coefficients can drive
the system from a quasi-stationary regime to a chaotic one. To address this issue, a common strategy
is to employ in-distribution validation data simulated fromP DEGT , and compare them with solutions
simulated from the identified PDE by resorting to trajectory or pointwise errors-based metrics such
asM SE(19),M AE(20) and their variants (see Sec. 4.1). Leveraging these metrics often makes it
possible to capture this type of pathological behaviors by checking thelocal consistencyof the learned
equation.
While this protocol based on so-calledinterpolationis appropriate when the goal is torecover
a GT law, we argue that such in-distribution generalization is necessary but not sufficient when it
comes to evaluating a PDE as a new scientific discovery. This more realistic situation arises when
P DEGT is assumed to be unknown and the goal isto discover it as a new knowledgefrom
observation data. To understand the specificity of this setting, it is essential to recall the distinction
betweeninterpolationandextrapolation, two well-known concepts in machine learning that play a key
role in this knowledge discovery framework.
29

Interpolation or Extrapolation? Get the best of both worlds!In PDE discovery, to avoid
overstating the validity of a discovered PDE, as a general new physical law, on the sole basis of
low errors on in-distribution data, it becomes crucial to also evaluate itsextrapolationcapability on
out-of-distribution examples. As seen in Sec. 4.5, extrapolation provides a more stringent criterion
by testing whether the learned equation captures the underlying dynamics beyond the regime seen
during its identification. Thus, interpolation and extrapolation play complementary roles in post-hoc
evaluation, each yielding different insights into the quality of the discovered PDE.Interpolation
ensures local consistency, verifying that the inferred dynamics is coherent in observed regimes.
On the other hand,extrapolationprovides a stronger indicator of whether the PDEcaptures true
physical structure rather than statistical regularities5. In this context, we discussed in Sec. 4.5
different scenarios for evaluating the OOD generalization capacity of a discovered PDE. Based on our
analysis and the experiments conducted, we strongly advocate the use of varying initial and boundary
conditions and the rollout-error 37 to evaluate the stability of the equation. The running example
withP DEA clearly illustrated that, despite having an equation very close toP DE GT , errors can
accumulate over the long term and lead to substantial divergence in the predictions.
Paradoxically, while real-world applications have a pressing need for extrapolation to validate sci-
entific discovery, they often suffer from a lack of observation data (compared to the unlimited number
of simulations available whenP DE GT is known), preventing the straightforward implementation of
the experimental setup described in Sec. 4.5. To overcome this issue, different solutions exist, one of
them consisting in learning a surrogate model allowing to generate data under new conditions. For
instance, Fourier Neural Operator [2], which models mappings between function spaces, can be used
as a surrogate numerical solver. Once trained on in-distribution data, it can generalize by outputting
solution trajectories for new conditions, thereby providing a practical way to construct controlled
OOD scenarios. However, it should be noted that, in addition to numerical errors associated with
trajectories simulated from the learned PDE, extrapolation may also be impacted by approximation
and generalization errors of the FNO, which are respectively related to the model architecture and
the amount of data available for training.
T o know or not to know a priori?In Section 4.4, we showed how physical properties can
be leveraged to complement, when validating the physical consistency of a PDE, metrics based on
pointwise/trajectory errors and sparsity criteria. However, such strategy raises the key question of
theaccess to physical priorsabout the characteristics that the discovered equation is expected
to satisfy, such as conserved quantities or symmetries. The review of the PDE discovery literature
reveals that a number of papers that employ inductive bias derived from physical laws often rely on the
assumption that these properties are known in advance. This is the case,e.g., in [44] where symmetry
is enforced by using differential invariants of the symmetry group as the variable set, hypothesizing
this group is already given. In [71], the authors incorporate a priori known Lie symmetries to enhance
Gaussian Processes-based models both in the context of forward and inverse problems (for learning
unknown PDE parameters). In the same vein, in [82], Lie symmetries are supposed to be known and
are embedded into the loss function of PINNs to solve inverse problems.
Assuming that such physical characteristics are given remains reasonable provided that one
has some background knowledge on the class of physical dynamical systems for which the PDE
discovery is being performed. In [44], the authors argue that physicists themselves often operate
in this manner, hypothesizing the symmetries of a system before seeking governing equations
allowed by those invariances. We illustrated this way of proceeding using the case of laser–matter
interaction in the “Running Example” paragraph of Section 4.4. However, for many real-world
situations, this postulate becomes less tenable because of a lack of reliable prior knowledge about
5Note that when the objective is merely to recover a known PDE, extrapolation can still serve as a robustness check,
but it is not strictly necessary for confirming correctness, sinceP DE GT is already fully specified.
30

the underlying physical structure, making it difficult to impose physical constraints on a learned
PDE. This can happen,e.g., in socio-economic systems, where interactions are heterogeneous,
in biology, where mechanisms are only partially understood and vary across scales, or in surface
engineering involving the complex intertwining of several phenomena. To circumvent this limitation,
recent works aimed to automatically discover physical properties from data and leverage them
for PDE discovery/evaluation. For example, in [83], the authors proposeLaLiGAN, a novel
generative model which can discover symmetries of nonlinear group actions. They show that their
method can be applied to downstream tasks such as equation discovery. On the other hand, in
[84] and [85], to avoid hard-coding symmetries in neural networks, the authors aim to discover
Lie group symmetry transformations present in the training dataset. The reader interested in
learning more about symmetry discovery may also refer to [64, 67, 86, 87, 88]. Similarly, note that
several recent papers have investigated the discovery of conservation laws from data (see,e.g., [89, 90]).
And what next?While some of the metrics discussed in this paper possess more desirable
characteristics than others, notably by providing better coverage of the key requirements that a
discovered PDE is expected to satisfy (see Table 1), it is worthwhile mentioning that the most
relevant ones are strongly grounded in a pointwise perspective. This applies to all metrics based on
prediction errors, residuals, and trajectory-based evaluations of Sec. 4. A common consequence of
these measures is that they provide only a partial assessment of the PDE quality, as they do not
capture higher-level functional properties beyond local discrepancies and trajectory matching. We
argue that more holistic evaluation metrics are therefore needed to assess PDE fidelity by accounting
not only for local approximation errors but also for the structural, geometric, and regularity properties
of the solution. We sketch below two perspectives, among other potential ones, which are likely to
address this need. They rely on the use of (i) the Sobolev semi-norm and (ii) the optimal transport
and gradient flows. On the other hand, leveraging [18], we also analyze the necessity to develop new
metrics related to the solvability of the identified PDE. Indeed, an equation, even if correct, has
little utility if no solver is available, or if the simulation time is not reasonable. Finally, we present
a last promising line of research on the evaluation of fractional PDEs, which, although richer than
classic equations, raise numerical challenges and require a specific assessment to be of practical interest.
▶F unctional analysis of PDEs:The Sobolev semi-norm of a function takes into account not
only the values of the function itself but also its derivatives up to a given orderk, providing insights
into its regularity and smoothness. Fundamentally rooted in functional analysis, it is defined as follows:
|u|H k(Ω) =

 X
|β|≤k
∥Dβu∥2 L2(Ω)


1/2
(40)
whereD βu= ∂|β| u
∂xβ1 1 ···∂x βd d , withβ= (β 1, β2, . . . , βd)∈N d is a multi-index and|β|=β 1 +· · ·+βd. This norm has been used for a long time in numerical analysis, notably to analyze the convergence,
stability and approximation quality of numerical solutions to PDES [81], and more recently in PiML
models for regularizing PINNs [15] allowing to theoretically maintain consistency with the underlying
physics. Surprisingly, while it enables better capture of local structures and helps avoid learning
overly smooth solutions, it is worth noting that the Sobolev norm has scarcely been leveraged in
the literature concerned with PDE discovery. One reason is that askincreases, obtaining and
differentiating through these higher-order terms becomes progressively more costly and can make
gradient-based training unstable. Moreover, using the Sobolev norm in its most general form as
defined in Eq. 40,e.g.as a regularization term, makes it difficult to derive generalization guarantees.
This is why, in [15], the authors restrict their convergence analysis of PINNs to affine differential
operators,i.e.limiting the approach to linear PDEs. However, in post-hoc PDE evaluation, we argue
31

that these constraints can be more readily relaxed, paving the way for the design of new metrics
based on this norm. Note that in MDBENCH [12], the authors share the observation that there is no
established metric for quantifying equation fidelity, and they claim that there is an urgent need for
a“robust metric that captures functional equivalence, e.g., using a discretized version of the Sobolev
semi-norm for PDE systems”.
▶PDEs viewed as gradient flows: Another promising direction in post-hoc evaluation is to
consider PDEs as evolving probability measures, and compare the ground truth data with the solutions
of the discovered equation through the lens of Optimal Transport (OT) [91] and Gradient Flows (GF)
[92]. Although OT is a longstanding theory [93], it has only attracted renewed interest from the
machine learning community over the past decade following (i) the design of efficient algorithms for
Wasserstein distance computation (e.g.Sinkhorn algorithm [94]), (ii) the development of Wasserstein
GANNs [95], and the use of GF in generative AI [32].
On the other hand, OT and GF offer significant advantages for capturing the functional properties
of dynamical systems. Indeed, many PDEs, such as Fokker-Planck, Keller-Segel or diffusion, advection
and aggregation equations in general, with many related real-world applications, have been shown to
be interpreted as GF [96, 97, 98]. This provides an original way to understand the evolution of an
equation as the steepest descent of an energy functional in a (typically) Wasserstein metric space,
offering the possibility to leverage the PDE’ underlying variational structure. Under this viewpoint,
OT and GF provide new mathematical tools for studying stability and long time behavior of PDEs.
They notably enabled the design of a new class of numerical methods (seee.g.[99, 100, 101]) endowed
with better stability and convergence guarantees.
In this context, a few papers have exploited the Wasserstein distance to evaluate the quality of
a learned PDE. For instance, in [102], the authors deal with learning systems of interacting particles
and compare GT and discovered solutions by leveraging the behavior of the Wasserstein distance. We
recall that the latter measures the discrepancy between two probability distributions by computing
the minimum transportation cost required to transform one distribution into the other. Under this
definition, it enables the characterization of properties that are not accessible through metrics relying
on pointwise errors or trajectory-based evaluation. For instance, two otherwise identical PDE solutions
with a slight spatial or temporal shift will be considered significantly different under pointwise metrics,
despite exhibiting nearly identical dynamics. By contrast, the Wasserstein distance will capture this
geometric displacement and therefore identifies the solutions as highly similar. Moreover, unlike most
of other alternative metrics, the Wasserstein distance is characterized by remaining informative over
longer horizons, even with non-overlapping support.
Some recent works have leveraged the Wasserstein distance from a theoretical standpoint to
establish new stability estimates in equation discovery. This is the case, for example, in [103] where
the authors deal with sparse identification of interaction kernels. Focusing on PDEs with interaction
potentials (which arises in many applications) that can be formulated as GF, they control the
Wasserstein distance between solutions generated using the true and learned interaction potentials.
In [104], discovery is envisioned under the assumption that the dataset is not governed by the same
dynamics. In this parametric PDE learning setting, they comnbine the Wasserstein distance with
diffusion maps, to discover conserved quantities that vary across trajectories.
Despite these few references, it is important to note that works exploiting OT and GF for
PDE evaluation (during learning or as downstream task) are still at an early stage. Beyond the
straightforward use of the Wasserstein distance between solution distributions (as seen above), no
well-established methodology has yet emerged. On the other hand, the numerous recent advances in
OT and GF are likely to pave the way for new evaluation frameworks capable of efficiently capturing
the functional properties of a learned PDE and measuring jointly its accuracy, simplicity, physical
consistency and long-time stability.
32

▶Discovered PDEs must also be numerically solvable to be useful:As discussed
throughout this survey, PDE evaluation metrics aim to deal with the requirements associated with
QuestionsQ1toQ5. Nevertheless, as recently highlighted in [18], even an equation that leads to
accurate solutions, which is sparse, physically consistent, and generalizes well, may still be of limited
practical value. For instance, a supposedly good PDE according to these criteria may also (i) exhibit
non-standard terms which significantly complicate its numerical solution, (ii) describe an ill-posed
problem (as discussed earlier in Sec. 4.4), (iii) lead to an unstable numerical discretization due,e.g.,
to excessively stiff dynamics, or more generally (iv) entail a prohibitive computational cost, making
large-scale simulations or uncertainty quantification impractical. Numerical tractability is therefore
not motivated by mathematical aesthetics, but because in most real-world applications, a PDE is
only useful if it can actually be practically deployable, that is, simulated reliably, repeatedly, and at
scale. As stated by [18], this issue has largely been overlooked in the literature, thereby justifying
the need for a new class of dedicated metrics. Note that low robustness and ill-posedness can be
partially identified through numerical criteria such as the mesh convergence (see Eq.(38)). On the
other hand, recent works have started to consider simulation time as a PDE quality criterion. This
is the case in PhysPDE [9] where the efficiency is measured by the totalsimulation wall-time. The
wall-clock timing is also employed in AutoSINDy [80] allowing,e.g.to detect stiff PDEs that require
finer time-stepping, leading to substantially longer integration times. Despite these few papers (see
also SciGym [105]), further investigation is still required to develop metrics that can detect and assess
solvability issues.
▶T owards evaluation metrics for fractional PDEs: Fractional PDEs generalize PDEs by
allowing derivatives of arbitrary, thus possibly non-integer, order. They arise in various physical
phenomena where non-locality plays a crucial role [106], such as in anomalous diffusion [107], transport
in porous media [108], viscoelastic materials [109], geophysical modelling [110], or in biological systems
[111]. Although the discovery of such PDEs has been investigated in a few papers [112, 113, 114, 115,
116], these equations pose several challenges lying in their nonlocal operators, which introduce long-
range spatial or temporal interactions and significantly complicate their numerical processing [117].
Due to this nonlocal nature of the fractional operator, conventional evaluation metrics discussed in
our study may become misleading. For instance, the sparsity/complexity of a fractional law is more
difficult to capture since a single fractional derivative can encode substantially richer dynamics than
a integer order-based term. By way of example, in [116], the authors show in their experiments that
one fractional derivative with the same approximation quality can be used as an interpolation of
two integer-order operators. This example shows that, although the resulting model is objectively
sparser, it would be questionable to claim that the use of a fractional derivative, which is inherently
more expressive and therefore more complex in a certain sense, leads to a simpler governing law.
This illustrates that, in the context of non-integer-order PDEs, it becomes necessary to distinguish
more carefully between the notions of sparsity and simplicity/interpretability through more refined
evaluation metrics. On the other hand, the numerical evaluation of residuals is more sensitive to
the choice of fractional derivative definition (e.g., Caputo, Riemann–Liouville, or Riesz) depending
on the property one primarily aims to preserve, which are not taken into account by classic metrics.
Moreover, the fractional orders themselves constitute continuous model parameters whose correctness
should be evaluated alongside the PDE coefficients and the presence/absence of terms, adding an extra
dimension to the evaluation procedure. These distinctive characteristics introduced by non-integer-
order derivatives call for the development of a new generation of post-hoc evaluation metrics. We
argue that this is essential to fairly assess future fractional PDE discovery methods, whose emergence
is expected to accelerate in light of the significant progress made in the numerical computation or
neural approximation of these derivatives, and the growing interest in fractional models due to their
ability to describe complex nonlocal phenomena.
33

Acknowledgments
This research was funded by the French National Research Agency (ANR) under the project
MELISSA ”Methodological contributions in statistical Learning InSpired by SurfAce engineering” -
ANR-24-CE23-7140-01.
The authors gratefully acknowledge Eduardo Brandao for his careful reading of the manuscript and
for his valuable and insightful comments, which contributed to its improvement.
References
[1] Maziar Raissi, Paris Perdikaris, and George E Karniadakis. Physics-informed neural networks:
A deep learning framework for solving forward and inverse problems involving nonlinear partial
differential equations.Journal of Computational physics, 2019.
[2] Zongyi Li, Nikola Borislavov Kovachki, Kamyar Azizzadenesheli, Burigede Liu, Kaushik Bhat-
tacharya, Andrew M. Stuart, and Anima Anandkumar. Fourier neural operator for parametric
partial differential equations. InICLR 2021, Austria, May 3-7, 2021. OpenReview.net, 2021.
[3] George Em Karniadakis, Ioannis G. Kevrekidis, Lu Lu, Paris Perdikaris, Sifan Wang, and Liu
Yang. Physics-informed machine learning.Nature Reviews Physics, 3(6), 5 2021.
[4] Steven L. Brunton, Joshua L. Proctor, and J. Nathan Kutz. Discovering governing equations
from data by sparse identification of nonlinear dynamical systems.Proceedings of the National
Academy of Science, 113(15):3932–3937, April 2016.
[5] Zichao Long, Yiping Lu, Xianzhong Ma, and Bin Dong. PDE-net: Learning PDEs from data. In
Jennifer Dy and Andreas Krause, editors,Proceedings of the 35th International Conference on
Machine Learning, volume 80 ofProceedings of Machine Learning Research, pages 3208–3216.
PMLR, 10–15 Jul 2018.
[6] Ali Forootani, Pawan Goyal, and Peter Benner. A robust sindy approach by combining neural
networks and an integral form.arXiv, abs/2309.07193, 2023.
[7] Robert Stephany and Christopher Earls. Pde-learn: Using deep learning to discover partial
differential equations from noisy, limited data.Neural Networks, 174:106242, 2024.
[8] Fayad Ali Banna, Antoine Caradot, Eduardo Brandao, Jean-Philippe Colombier, R´ emi Emonet,
and Marc Sebban. Unrolled-sindy: A stable explicit method for non linear pde discovery from
sparsely sampled data. InECML 2026, 2026.
[9] Mingquan Feng, Yixin Huang, Yizhou Liu, Bofang Jiang, and Junchi Yan. PhysPDE: Rethinking
PDE discovery and a physical HYpothesis selection benchmark. InThe Thirteenth International
Conference on Learning Representations, 2025.
[10] Kadierdan Kaheman, J. Nathan Kutz, and Steven L. Brunton. Sindy-pi: a robust algorithm for
parallel implicit sparse identification of nonlinear dynamics.Proceedings of the Royal Society A:
Mathematical, Physical and Engineering Sciences, 476(2242), October 2020.
[11] Hao Xu, Junsheng Zeng, and Dongxiao Zhang. Discovery of partial differential equations from
highly noisy and sparse data with physics-informed information criterion.Research, 6, January
2023.
34

[12] Amirmohammad Ziaei Bideh, Aleksandra Georgievska, and Jonathan Gryak. Mdbench: Bench-
marking data-driven methods for model discovery. InProc. Conf. AAAI Artif. Intell., 2026.
[13] Benjamin Girault, R´ emi Emonet, Amaury Habrard, Jordan Patracone, and Marc Sebban. Ap-
proximation Error of Sobolev Regular Functions with tanh Neural Networks: Theoretical Impact
on PINNs. ECML 2024, March 2024.
[14] Tim De Ryck, Ameya D Jagtap, and Siddhartha Mishra. Error estimates for physics-informed
neural networks approximating the navier–stokes equations.IMA Journal of Numerical Analysis,
44(1):83–119, 02 2024.
[15] Nathan Doum` eche, G´ erard Biau, and Claire Boyer. On the convergence of PINNs.Bernoulli,
31(3):2127 – 2151, 2025.
[16] K. Miettinen.Nonlinear multiobjective optimization. Kluwer, Boston, USA, 1999.
[17] Beatriz Regina Brum, Luiza Lober, Isolde Terezinha Santos Previdelli, and Francisco A. Ro-
drigues. Discovering equations from data: symbolic regression in dynamical systems.Journal
of Physics: Complexity, 7, 2025.
[18] Siyu Lou, Hao Xu, Wenguan Wang, Lu Lu, Hao Sun, Yang Liu, Linfeng Zhang, Dongxiao
Zhang, and Yuntian Chen. Data-driven discovery of governing differential equations across
physical systems.arXiv, abs/2606.09638, 2026.
[19] John H. Lagergren, John T. Nardini, G. Michael Lavigne, Erica M. Rutter, and Kevin B. Flores.
Learning partial differential equations for biological transport models from noisy spatio-temporal
data.Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences,
476(2234):20190800, February 2020.
[20] Adeel Pervez, Efstratios Gavves, and Francesco Locatello. Mechanistic PDE networks for dis-
covery of governing equations. InForty-second International Conference on Machine Learning,
2025.
[21] Mohsen Sadr, Tony Tohme, and Kamal Youcef-Toumi. Data-driven discovery of PDEs via the
adjoint method.Transactions on Machine Learning Research, 2025.
[22] Sarah Nogueira, Konstantinos Sechidis, and Gavin Brown. On the stability of feature selection
algorithms.Journal of Machine Learning Research, 18(174):1–54, 2018.
[23] Dimitris Bertsimas and Wes Gurnee. Learning sparse nonlinear dynamics via mixed-integer
optimization.Nonlinear Dynamics, 7(11), 2022.
[24] Austin Tripp, Sergio Bacallado, Sukriti Singh, and Jos´ e Miguel Hern´ andez-Lobato. Tanimoto
random features for scalable molecular machine learning. InThirty-seventh Conference on Neural
Information Processing Systems, 2023.
[25] Junqi Qu, Yan Zhang, Shangqian Gao, and Shibo Li. Dynamic bayesian optimization framework
for instruction tuning in partial differential equation discovery. InSubmitted to ACL Rolling
Review - January 2026, 2026. under review.
[26] Samuel Holt, Zhaozhi Qian, Tennison Liu, James Weatherall, and Mihaela van der Schaar.
Data-driven discovery of dynamical systems in pharmacology using large language models. In
A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang, editors,
Advances in Neural Information Processing Systems, volume 37, pages 96325–96366. Curran
Associates, Inc., 2024.
35

[27] Manuel Morales-Alvarado. Foundation models for equation discovery in high energy physics.
arXiv, 2510.03397, 10 2025.
[28] Parshin Shojaee, Ngoc-Hieu Nguyen, Kazem Meidani, Amir Barati Farimani, Khoa D Doan, and
Chandan K. Reddy. LLM-SRBench: A new benchmark for scientific equation discovery with
large language models. InForty-second International Conference on Machine Learning, 2025.
[29] Evgeny S. Saveliev, Samuel Holt, Nabeel Seedat, David L. Bentley, Jim Weatherall, and Mihaela
van der Schaar. Influence-guided symbolic regression: Scientific discovery via llm-driven equation
search with granular feedback.arXiv, abs/2605.29184, 2026.
[30] Daniel A. Messenger and David M. Bortz. Weak sindy for partial differential equations.Journal
of Computational Physics, 443:110525, October 2021.
[31] U. Fasel, J. N. Kutz, B. W. Brunton, and S. L. Brunton. Ensemble-sindy: Robust sparse model
discovery in the low-data, high-noise limit, with active learning and control.Proceedings of the
Royal Society A: Mathematical, Physical and Engineering Sciences, 478(2260), April 2022.
[32] Hao Xu, Yuntian Chen, Rui Cao, Tianning Tang, Mengge Du, Jian Li, Adrian H. Callaghan,
and Dongxiao Zhang. Generative discovery of partial differential equations by learning from
math handbooks.Nat Commun., 16(1), 2025.
[33] En-Hao Gao, Cunjing Ge, Yuan Jiang, and Zhi-Hua Zhou. Discovering symbolic partial differ-
ential equation by abductive learning. InAdvances in Neural Information Processing Systems
39 (NeurIPS’25), 2025.
[34] Grant Norman, Conor Rowan, Kurt Maute, and Alireza Doostan. Learning gradient flow:
Using equation discovery to accelerate engineering optimization.Computer Methods in Applied
Mechanics and Engineering, 460:119099, 2026.
[35] Amie Wilkinson. What are lyapunov exponents, and why are they interesting?Bulletinof the
American Mathematical Society, 54(1):79–105, 2017.
[36] Andr´ ea Ducos, Audrey Denizot, Thomas Guyet, and Hugues Berry. Evaluating PDE discovery
methods for multiscale modeling of biological signals. InSpringer LNBI, volume 15959, Lyon,
France, September 2025. Fran¸ cois Fages and Sabine P´ er` es.
[37] K. J¨ arvelin and J. Kek¨ al¨ ainen. Cumulated gain-based evaluation of IR techniques.ACM Trans-
actions on Information Systems (TOIS), 20(4):422–446, 2002.
[38] Pongpisit Thanasutives and Ken ichi Fukui. On uncertainty-penalized bayesian information
criterion.arXiv, abs/2404.16881, 2024.
[39] Robert Stephany and Christopher J. Earls. PDE-READ: human-readable partial differential
equation discovery using deep learning.Neural Networks, 154:360–382, 2022.
[40] Shilin Zhang, Yunqing Huang, Nianyu Yi, and shihan Zhang. Robust pde discovery under sparse
and highly noisy conditions via attention neural networks.ArXiv, abs/2506.17908, 2025.
[41] Weida Wang, Benteng Chen, Di Zhang, Wanhao Liu, Shuchen Pu, Ben Gao, Jin Zeng, Xiaoyong
Wei, Tianshu Yu, Shuzhou Sun, Tianfan Fu, Wanli Ouyang, Lei Bai, Jiatong Li, Zifu Wang,
Yuqiang Li, and Shufei Zhang. Chem-r: Learning to reason as a chemist.arXiv, abs/2510.16880,
2025.
[42] Fang Lim, Jinbo Pan, and Shixuan Du. Discovery of interpretable t c descriptors in conventional
superconductors guided by symbolic regression.Physical Review Materials, 10, 05 2026.
36

[43] Yizhi Huang, Rahul Ilango, and Hanlin Ren. Np-hardness of approximating meta-complexity:
A cryptographic approach.SIAM Journal on Computing, 54(4):819–886, 2025.
[44] Jianke Yang, Manu Bhat, Bryan Hu, Yadi Cao, Nima Dehmamy, Robin Walters, and Rose Yu.
Discovering symbolic differential equations with symmetry invariants.Transactions on Machine
Learning Research, 2026. Featured Certification, J2C Certification.
[45] Makoto Takamoto, Timothy Praditia, Raphael Leiteritz, Daniel MacKinlay, Francesco Alesiani,
Dirk Pfl¨ uger, and Mathias Niepert. Pdebench: An extensive benchmark for scientific machine
learning. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors,
Advances in Neural Information Processing Systems, volume 35, pages 1596–1611. Curran As-
sociates, Inc., 2022.
[46] Congcong Zhu, Xiaoyan Xu, Jiayue Han, and Jingrun Chen. Physics-informed temporal align-
ment for auto-regressive PDE foundation models. InForty-second International Conference on
Machine Learning, 2025.
[47] Zhao Chen, Yang Liu, and Hao Sun. Physics-informed learning of governing equations from
scarce data.Nature Communications, 12(1), October 2021.
[48] Jianwei Yang, Ohm Rishabh Venkatachalam, Mohammad Kianezhad, Sharvaree P. Vadgama,
and Rose Yu. Think like a scientist: Physics-guided llm agent for equation discovery.ArXiv,
abs/2602.12259, 2026.
[49] Phillip Lippe, Bastiaan S. Veeling, Paris Perdikaris, Richard E Turner, and Johannes Brandstet-
ter. PDE-refiner: Achieving accurate long rollouts with neural PDE solvers. InThirty-seventh
Conference on Neural Information Processing Systems, 2023.
[50] Seungwoo Yoo, Juil Koo, Daehyeon Choi, and Minhyuk Sung. Diffusionrollout: Uncertainty-
aware rollout planning in long-horizon PDE solving.Transactions on Machine Learning Re-
search, 2026.
[51] Xiaoxiao Lu, Ye Yuan, and Jiahao Shi. Stable long-horizon pde forecasting via latent structured
spectral propagators.arXiv, abs/2605.10154, 2026.
[52] Richard P. Feynman.The Character of Physical Law. MIT Press, Cambridge, MA, 1965.
[53] Gregory Kang Ruey Lau, Yue Ran Kang, Zi-Yu Khoo, Apivich Hemachandra, Ruth Wan Theng
Chew, and Bryan Kian Hsiang Low. README: Rapid equation discovery with multimodel
encoders. InNeurIPS 2025 AI for Science Workshop, 2025.
[54] Miles Cranmer, Alvaro Sanchez Gonzalez, Peter Battaglia, Rui Xu, Kyle Cranmer, David
Spergel, and Shirley Ho. Discovering symbolic models from deep learning with inductive bi-
ases. In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin, editors,Advances
in Neural Information Processing Systems, volume 33, pages 17429–17442. Curran Associates,
Inc., 2020.
[55] Zhen Zhang, Zongren Zou, Ellen Kuhl, and George Em Karniadakis. Discovering a reac-
tion–diffusion model for alzheimer’s disease by combining pinns with symbolic regression.Com-
puter Methods in Applied Mechanics and Engineering, 419:116647, 2024.
[56] Mengge Du, Yuntian Chen, and Dongxiao Zhang. Discover: Deep identification of symbolically
concise open-form partial differential equations via enhanced reinforcement learning.Phys. Rev.
Res., 6:013182, Feb 2024.
37

[57] H. Akaike.Information Theory and an Extension of the Maximum Likelihood Principle, pages
267–281. Akademiai Kiad´ o, Budapest, 1973.
[58] Gideon Schwarz. Estimating the dimension of a model.The Annals of Statistics, 6(2):461–464,
March 1978.
[59] N. M. Mangan, J. N. Kutz, S. L. Brunton, and J. L. Proctor. Model selection for dynamical
systems via sparse regression and information criteria.Proceedings of the Royal Society A:
Mathematical, Physical and Engineering Sciences, 473(2204):20170009, August 2017.
[60] A.N. Kolmogorov. On tables of random numbers.Theoretical Computer Science, 207(2):387–395,
1998.
[61] Deaglan J. Bartlett, Harry Desmond, and Pedro G. Ferreira. Exhaustive symbolic regression.
IEEE Transactions on Evolutionary Computation, 28(4):950–964, 2024.
[62] Paul M.B. Vit´ anyi. How incomputable is kolmogorov complexity?Entropy, 22(4):408, April
2020.
[63] Zihan Yu, Jingtao Ding, Yong Li, and Depeng Jin. Symbolic regression via MDLformer-guided
search: from minimizing prediction error to minimizing description length. InThe Thirteenth
International Conference on Learning Representations, 2025.
[64] Silviu-Marian Udrescu and Max Tegmark. Ai feynman: A physics-inspired method for symbolic
regression.Science Advances, 6(16), 2020.
[65] Mirza Baig and Syeda Gillani. Symmetry-constrained language-guided program synthesis for
discovering governing equations from noisy and partial observations.ArXiv, abs/2601.00088, 03
2026.
[66] Andrea Perin and St´ ephane Deny. On the ability of deep networks to learn symmetries from
data: A neural kernel theory.J. Mach. Learn. Res., 26:145:1–145:70, 2024.
[67] Samuel E. Otto, Nicholas Zolman, J. Nathan Kutz, and Steven L. Brunton. A unified framework
to enforce, discover, and promote symmetry in machine learning.Journal of Machine Learning
Research, 26(248):1–83, 2025.
[68] Tara Akhound-Sadegh, Laurence Perreault-Levasseur, Johannes Brandstetter, Max Welling, and
Siamak Ravanbakhsh. Lie point symmetry and physics-informed networks. InThirty-seventh
Conference on Neural Information Processing Systems, 2023.
[69] Yunfei Huang and David S. Greenberg. Geometric and physical constraints synergistically en-
hance neural PDE surrogates. InForty-second International Conference on Machine Learning,
2025.
[70] Johannes Brandstetter, Max Welling, and Daniel E Worrall. Lie point symmetry data aug-
mentation for neural PDE solvers. In Kamalika Chaudhuri, Stefanie Jegelka, Le Song, Csaba
Szepesvari, Gang Niu, and Sivan Sabato, editors,Proceedings of the 39th International Con-
ference on Machine Learning, volume 162 ofProceedings of Machine Learning Research, pages
2241–2256. PMLR, 17–23 Jul 2022.
[71] David Dalton, Dirk Husmeier, and Hao Gao. Physics and lie symmetry informed Gaussian pro-
cesses. In Ruslan Salakhutdinov, Zico Kolter, Katherine Heller, Adrian Weller, Nuria Oliver,
Jonathan Scarlett, and Felix Berkenkamp, editors,Proceedings of the 41st International Con-
ference on Machine Learning, volume 235 ofProceedings of Machine Learning Research, pages
9953–9975. PMLR, 21–27 Jul 2024.
38

[72] Derek Hansen, Danielle C. Maddix, Shima Alizadeh, Gaurav Gupta, and Michael W. Mahoney.
Learning physical models that can respect conservation laws.Physica D: Nonlinear Phenomena,
457:133952, January 2024.
[73] Anthony Baez, Wang Zhang, Ziwen Ma, Subhro Das, Lam M. Nguyen, and Luca Daniel. Guar-
anteeing conservation laws with projection in physics-informed neural networks. InNeurIPS
2024 Workshop on Data-driven and Differentiable Simulations, Surrogates, and Solvers, 2024.
[74] Wenjun Ma, Jun Zhang, Kaikai Feng, Haoyun Xing, and Dongsheng Wen. Dimensional homo-
geneity constrained gene expression programming for discovering governing equations.arXiv,
abs/2211.09679, 2024.
[75] Jure Brence, Saˇ so Dˇ zeroski, and Ljupˇ co Todorovski. Dimensionally-consistent equation discovery
through probabilistic attribute grammars.Information Sciences, 632:742–756, 2023.
[76] Mehardeep Singh. Nexus: A revolutionary framework for autonomous equation discovery. Au-
gust 2025.
[77] H. Holden and N. Risebro.Front Tracking for Hyperbolic Conservation Laws. Springer-Verlag,
New York City, NY, USA, 2002.
[78] E. Hairer, C. Lubich, and G. Wanner.Geometric numerical integration, Structure-preserving
algorithms for ordinary differential equations, volume 31. Springer-Verlag Berlin, 2006.
[79] Fayad Ali Banna, Eduardo Brand˜ ao, Anthony Nakhoul, R´ emi Emonet, Marc Sebban, and Jean-
Philippe Colombier. Photonic Learning in Ultrafast Laser-Induced Complexity.Ultrafast Sci-
ence, March 2026.
[80] Mohammad Amin Basiri and Charles Nicholson. Discovery of nonlinear dynamics with auto-
mated basis function generation.arXiv, abs/2605.09696, 2026.
[81] Susanne C. Brenner and Larkin R. Scott.The Mathematical Theory of Finite Element Methods,
volume 15 ofTexts in Applied Mathematics. Springer, 2008.
[82] Zhi-Yong Zhang, Hui Zhang, Li-Sheng Zhang, and Lei-Lei Guo. Enforcing continuous symmetries
in physics-informed neural network for solving forward and inverse problems of partial differential
equations.Journal of Computational Physics, 492:112415, 2023.
[83] Jianke Yang, Nima Dehmamy, Robin Walters, and Rose Yu. Latent space symmetry discovery.
InForty-first International Conference on Machine Learning, 2024.
[84] Alex Gabel, Victoria Klein, Riccardo Valperga, Jeroen S. W. Lamb, Kevin Webster, Rick Quax,
and Efstratios Gavves. Learning lie group symmetry transformations with neural networks.
In Timothy Doster, Tegan Emerson, Henry Kvinge, Nina Miolane, Mathilde Papillon, Bastian
Rieck, and Sophia Sanborn, editors,Proceedings of 2nd Annual Workshop on Topology, Algebra,
and Geometry in Machine Learning (TAG-ML), volume 221 ofProceedings of Machine Learning
Research, pages 50–59. PMLR, 28 Jul 2023.
[85] Artem Moskalev, Anna Sepliarskaia, Ivan Sosnovik, and Arnold W.M. Smeulders. LieGG:
Studying learned lie group generators. In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and
Kyunghyun Cho, editors,Advances in Neural Information Processing Systems, 2022.
[86] Shurui Gui, Xiner Li, and Shuiwang Ji. Discovering physics laws of dynamical systems via
invariant function learning. InForty-second International Conference on Machine Learning,
2025.
39

[87] Jianke Yang, Wang Rao, Nima Dehmamy, Robin Walters, and Rose Yu. Symmetry-informed
governing equation discovery. InThe Thirty-eighth Annual Conference on Neural Information
Processing Systems, 2024.
[88] Nima Dehmamy, Robin Walters, Yanchen Liu, Dashun Wang, and Rose Yu. Automatic symme-
try discovery with lie algebra convolutional network. In A. Beygelzimer, Y. Dauphin, P. Liang,
and J. Wortman Vaughan, editors,Advances in Neural Information Processing Systems, 2021.
[89] Vivan Doshi. Automated discovery of conservation laws via hybrid neural ode-transformers.
arXiv, abs/2511.00102, 2025.
[90] Shaoxuan Chen, Panayotis G. Kevrekidis, Hong-Kun Zhang, and Wei Zhu. Data-driven discovery
of conservation laws from trajectories via neural deflation.arXiv, abs/2410.05445, 2024.
[91] C´ edric Villani.Optimal transport – Old and new, volume 338, pages xxii+973. 01 2008.
[92] Anne Gagneux, S´ egol` ene Tiffany Martin, R´ emi Emonet, Quentin Bertrand, and Mathurin Mas-
sias. A visual dive into conditional flow matching. InThe Fourth Blogpost Track at ICLR 2025,
2025.
[93] Gaspard Monge. M´ emoire sur la th´ eorie des d´ eblais et de remblais.Histoire de l’Acad´ emie
Royale des Sciences de Paris, page 666–704, 1781.
[94] Marco Cuturi. Sinkhorn distances: Lightspeed computation of optimal transport. In C.J.
Burges, L. Bottou, M. Welling, Z. Ghahramani, and K. Weinberger, editors,Advances in Neural
Information Processing Systems, volume 26. Curran Associates, Inc., 2013.
[95] Martin Arjovsky, Soumith Chintala, and L´ eon Bottou. Wasserstein generative adversarial net-
works. In Doina Precup and Yee Whye Teh, editors,Proceedings of the 34th International Con-
ference on Machine Learning, volume 70 ofProceedings of Machine Learning Research, pages
214–223. PMLR, 06–11 Aug 2017.
[96] Filippo Santambrogio. Euclidean, Metric, and Wasserstein gradient flows: an overview.Math.
Sci., 7:87–154, 2017.
[97] Steffen Arnrich, Alexander Mielke, Mark A. Peletier, Giuseppe Savar´ e, and Marco Veneroni.
Passing to the limit in a wasserstein gradient flow: from diffusion to reaction.Calculus of
Variations and Partial Differential Equations, 44(3-4):419–454, August 2011.
[98] Lucas C. F. Ferreira and Julio C. Valencia-Guevara. Gradient flows of time-dependent functionals
in metric spaces and applications for pdes.Monatshefte f¨ ur Mathematik, 185(2):231–268, 2018.
[99] Quentin M´ erigot. A multiscale approach to optimal transport.Computer Graphics Forum,
30:1583 – 1592, 2011 2011.
[100] Jean-David Benamou and Guillaume Carlier. Augmented Lagrangian methods for transport
optimization, mean field games and degenerate elliptic equations.J. Optim. Theory Appl.,
167(1):1–26, 2015.
[101] Jose A. Carrillo, Katy Craig, Li Wang, and Chaozhen Wei. Primal dual methods for wasserstein
gradient flows.Foundations of Computational Mathematics, 22(2):389–443, 2022.
[102] Quanjun Lang and Fei Lu. Learning interaction kernels in mean-field equations of first-order
systems of interacting particles.SIAM Journal on Scientific Computing, 44(1):A260–A285, 2022.
40

[103] Jose A. Carrillo, Gissell Estrada-Rodriguez, Laszlo Mikolas, and Sui Tang. Sparse identifica-
tion of nonlocal interaction kernels in nonlinear gradient flow equations via partial inversion.
Mathematical Models and Methods in Applied Sciences, 35(5):1073–1131, 2026.
[104] Peter Yucheng Lu. Interpretable physics-informed machine learning methods for scientific mod-
eling and data analysis.Massachusetts Institute of Technology, September 2022.
[105] Haonan Duan, Stephen Zhewen Lu, Caitlin Fiona Harrigan, Nishkrit Desai, Jiarui Lu, Micha l
Koziarski, Leonardo Cotta, and Chris J. Maddison. Measuring scientific capabilities of language
models with a systems biology dry lab. InThe Thirty-ninth Annual Conference on Neural
Information Processing Systems Datasets and Benchmarks Track, 2026.
[106] HongGuang Sun, Yong Zhang, Dumitru Baleanu, Wen Chen, and YangQuan Chen. A new collec-
tion of real world applications of fractional calculus in science and engineering.Communications
in Nonlinear Science and Numerical Simulation, 64:213–231, 2018.
[107] Richard L. Magin, Osama Abdullah, Dumitru Baleanu, and Xiaohong Joe Zhou. Anomalous
diffusion expressed through fractional order differential operators in the bloch–torrey equation.
Journal of Magnetic Resonance, 190(2):255–270, 2008.
[108]  Lukasz P lociniczak. Analytical studies of a time-fractional porous medium equation. deriva-
tion, approximation and applications.Communications in Nonlinear Science and Numerical
Simulation, 24(1):169–183, 2015.
[109] Meihua Zhang, Yajuan Hao, Yiming Chen, Gang Cheng, Thierry Barri` ere, and Jingguo Qu.
Modeling and dynamic analysis of fractional order nonlinear viscoelastic rod.International
Journal of Non-Linear Mechanics, 162:104699, 2024.
[110] Jos´ e Humberto De Prates and Davidson Moreira. Fractional derivatives in geophysical modelling:
Approaches using the modified adomian decomposition method.Pure and Applied Geophysics,
177, 09 2020.
[111] Ishtiaq Ali. Dynamical analysis of two-dimensional fractional-order-in-time biological population
model using chebyshev spectral method.Fractal and Fractional, 8(6):325, May 2024.
[112] Xiangnan Yu, Hao Xu, Zhiping Mao, HongGuang Sun, Yong Zhang, Dongxiao Zhang, and Yun-
tian Chen. A data-driven framework for discovering fractional differential equations in complex
systems.arXiv, abs/2412.03970, 2024.
[113] Abhishek Kumar Singh, Mani Mehra, and Anatoly A. Alikhanov.Data-Driven Discovery of
Time Fractional Differential Equations, page 56–63. Springer International Publishing, 2022.
[114] Yash Vats, Mani Mehra, Dietmar Oelz, and Abhishek Kumar Singh. A new perspective for
scientific modelling: Sparse reconstruction-based approach for learning time-space fractional
differential equations.Journal of Computational and Nonlinear Dynamics, 19(12):121003, 09
2024.
[115] Abhishek Kumar Singh, Mani Mehra, and Samarth Gulyani. Learning parameters of a system
of variable order fractional differential equations.Numerical Methods for Partial Differential
Equations, 39(3):1962–1976, April 2021.
[116] Mamikon Gulian, Maziar Raissi, Paris Perdikaris, and George Karniadakis. Machine learning of
space-fractional differential equations.arXiv, abs/1808.00931, 2019.
41

[117] Anjali Chaudhary, Vikram Singh, and Sumit Malik. Approximate solutions for fractional partial
differential equations using new operational matrices and collocation technique.Physica Scripta,
101(7):075208, feb 2026.
42
