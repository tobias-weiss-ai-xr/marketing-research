---
title: 'MenuNet: A Strategy-Proof Mechanism for Matching Markets'
url: https://arxiv.org/abs/2605.03216
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Zhaohong Sun
- Makoto Yokoo
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.03216
pages: 15
chars: 50737
fetched_at: '2026-11-08T13:09:57+00:00'
kb_version: 1
---

# MenuNet: A Strategy-Proof Mechanism for Matching Markets

MenuNet: A Strategy-Proof Mechanism for Matching Markets
Zhaohong Sun1,2 and Makoto Yokoo1
1Kyushu University, Japan
2CyberAgent, Japan
ABSTRACT
Strategy-proofness is a fundamental desideratum in mechanism design, ensuring truthful reporting
and robust participation. Stability is another central requirement in matching markets, widely
adopted in applications such as school choice and labor market clearing. In practice, however, these
markets are invariably governed by complex distributional constraints, ranging from diversity quotas
and regional balance to global capacity slacks, under which stable matchings often fail to exist.
This raises a fundamental question: how to distribute unavoidable instability across agents while
preserving strategy-proofness? To address this, we propose MenuNet, a strategy-proof mechanism
design framework based on a neural representation of menus. Rather than directly constructing
assignments, MenuNet learns to generate personalized probabilistic menus, from which assignments
are realized via a structured sequential choice rule that guarantees strategy-proofness by construction.
By decomposing stability into fairness (no envy) and non-wastefulness, our approach models these
properties as vector-valued quantities and optimizes their distribution through differentiable objectives,
providing a principled trade-off between competing axioms. Empirically, MenuNet navigates this
trade-off effectively: it consistently outperforms Random Serial Dictatorship (RSD) in terms of envy
and Deferred Acceptance (DA) in terms of waste, while maintaining scalability and computational
efficiency. These results suggest that learning-based menu mechanisms provide a flexible and scalable
paradigm for mechanism design in highly constrained, real-world environments.
1 Introduction
Strategy-proofness (SP) is a central desideratum in matching markets, ensuring that agents have no incentive to misreport
their preferences. By aligning incentives with truthful reporting, SP simplifies strategic behavior and enhances the
robustness of the mechanism. Its importance is well illustrated by major market design reforms, such as the National
Resident Matching Program (NRMP) in the U.S. [Roth, 1984] and the Boston school choice system [Abdulkadiro˘glu
et al., 2005a], where manipulable mechanisms were replaced by strategy-proof alternatives. These reforms are largely
based on the Deferred Acceptance (DA) mechanism [Gale and Shapley, 1962], which is strategy-proof for the proposing
side and produces stable outcomes. Stability is another fundamental requirement, ensuring that no pair of agents can
profitably deviate to form a blocking match. This property is widely adopted in practice, including medical residency
matching [Roth and Peranson, 1999, Roth, 2008], school choice systems in New York City [Abdulkadiro ˘glu et al.,
2005b] and Chile [Correa et al., 2022], centralized college admissions in India [Baswana et al., 2019], and daycare
matching in Japan [Kamada and Kojima, 2024, Sun et al., 2023, 2024].
In many real-world applications, however, matching markets are subject to distributional and institutional constraints
that extend beyond the classical framework of rigid capacities. For instance, lower quotas may require institutions to
enroll a minimum number of students to remain viable [Biró et al., 2010], while regional quotas impose aggregate
capacity limits across groups of institutions [Kamada and Kojima, 2015]. Diversity and affirmative action policies
introduce type-based priorities to enroll students from diverse backgrounds [Sönmez and Yenmez, 2022, Aygün and Bó,
2021], and complementarities arise in settings such as residency matching for couples [McDermid and Manlove, 2010,
Kojima et al., 2013]. More generally, multi-dimensional feasibility constraints encountered in refugee resettlement
further complicate the solution space [Delacrétaz et al., 2023, Aziz et al., 2018].
arXiv:2605.03216v1  [cs.GT]  4 May 2026

In the presence of such constraints, stable matchings are no longer guaranteed to exist. The existing literature has
largely addressed this challenge by decomposing stability into fairness (absence of justified envy) and non-wastefulness,
subsequently relaxing these properties to restore feasibility under specific constraints. However, these approaches
typically focus on aggregate objectives, offering limited control over the distributional consequences of the resulting
instability. In practice, this can lead to systemic imbalance, where a small subset of agents bear the brunt of the
violations, resulting in extreme individual dissatisfaction. Since some degree of instability is unavoidable in constrained
environments, the key design question is no longer how to eliminate instability, but how to distribute it. Our goal is
to design strategy-proof mechanisms that not only balance fairness and non-wastefulness, but also equitably partition
unavoidable instability across agents to preclude disproportionate individual loss.
To address this challenge, we introduce MenuNet, a neural mechanism design framework built upon personalized
probabilistic menus. Rather than directly optimizing discrete assignments, MenuNet generates an admission probability
menu for each agent, from which final allocations are induced via a structured choice rule that ensures strategy-
proofness by construction (Theorem 1). The framework is modular and versatile, modeling both envy and waste as
vector-valued quantities. This formulation allows MenuNet to optimize differentiable objectives with fine-grained
control, facilitating a principled trade-off between fairness and efficiency while preventing the concentration of instability
from disproportionately affecting a small subset of agents. Moreover, the architecture naturally accommodates a broad
spectrum of distributional constraints, and is computationally efficient and scales to large markets.
To demonstrate the effectiveness of our approach, we focus on a representative constraint, global capacity slack, where
capacity constraints are treated as flexible and allow for controlled and bounded violations. Such settings commonly
arise in practice: universities may over-admit to hedge against yield uncertainty; research labs may temporarily exceed
supervision limits at a marginal cost; and course allocation systems often expand high-demand sections to better satisfy
preferences. These requirements introduce interdependent constraints across institutions, leading to environments in
which capacity is sufficient in aggregate but remains locally scarce.
Through extensive experiments across diverse market scales, we demonstrate thatMenuNet achieves a superior trade-off
between fairness and non-wastefulness compared to classical baselines such as Random Serial Dictatorship (RSD) and
Deferred Acceptance (DA). Specifically, MenuNet consistently attains lower envy than RSD and lower waste than DA,
while crucially distributing unavoidable dissatisfaction more equitably across the agent population. Furthermore, the
framework exhibits robust scalability, maintaining computational efficiency as it scales to large-scale markets.
2 Related Work
Recent advances in neural mechanism design have demonstrated the potential of deep learning for optimal auction
design [Feng et al., 2018, Rahme et al., 2021, Duan et al., 2022, Ivanov et al., 2022, Dütting et al., 2024]. In contrast,
comparatively little work has applied neural approaches to matching problems. A notable exception is [Ravindranath
et al., 2021], which studies neural mechanisms for classical two-sided matching. Our work differs from this paper
in several important respects. First, while it focuses on classical matching environments with rigid capacities, our
framework is designed for settings with flexible quotas and more general distributional constraints commonly arising in
institutional applications. Second, rather than directly learning assignments through regret-based objectives, MenuNet
adopts a menu-based representation that guarantees strategy-proofness by construction, providing a structural alternative
to empirical regularization. Third,MenuNetis designed for scalability, achieving efficient training and inference even
in large markets.
A separate line of work studies matching under uncertainty through bandit-based frameworks, where agent preferences
must be learned online [Das and Kamenica, 2005, Liu et al., 2020, 2021, Basu, 2025]. These works address preference
elicitation and exploration-exploitation trade-offs, whereas our focus is on mechanism design under known preferences
but complex feasibility constraints.
3 Model
In this section, we formalize the school choice model with global capacity flexibility, a specific form of distributional
constraints. While our proposed MenuNet framework applies to a broad class of matching markets, we focus on this
setting for illustrative purposes.
An instance is defined by the tuple I= (S, C,q, k, V, U), where S={s 1, . . . , sn} and C={c 0, c1, . . . , cm} denote
the sets of students and schools, respectively. Each school c∈C\ {c 0} is associated with asoft capacity target
qc ∈Z ≥0, representing its preferred maximum enrollment. We include an outside option c0 ∈C , representing the
option of being unassigned, and assume c0 has sufficient capacity to accommodate all students (i.e., qc0 ≥n ). To
2

capture flexibility in the system, we introduce aglobal slackparameter k∈Z ≥0, which bounds the total allowable
over-enrollment across all schools.
To enable gradient-based optimization, we adopt a cardinal representation of preferences and priorities. Let V=
[vs,c]∈R n×(m+1) and U= [u s,c]∈R n×(m+1) denote the student utility matrix and the school priority matrix,
respectively, where vs,c represents the utility of student s for school c, and us,c represents the priority assigned to s by
school c. All scores for acceptable assignments are normalized to lie in [0,1] , with higher values indicating stronger
preferences or higher priorities. We allow vs,c <0 to indicate that school c is unacceptable to student s. The outside
option is normalized tov s,c0 = 0, ensuring that all unacceptable schools are strictly dominated.1
A matching µ assigns each student to exactly one element of C, i.e., µ(s)∈C for all s∈S . For each school c∈C , let
µ(c) ={s∈S|µ(s) =c} denote the set of students assigned to c. A matching isfeasibleif the aggregate capacity
violation satisfies: X
c∈C\{c 0}
max{|µ(c)| −qc,0} ≤k.(1)
Stability is a central concept in matching markets, defined as the combination ofindividual rationalityand the absence
ofblocking pairs[Roth, 1985]. Individual rationality requires that no student is assigned to an unacceptable school,
while a pair (s, c)blocks a matching if both sides prefer to be matched with each other over their current assignments.
In our setting, blocking pairs can be decomposed into two distinct types: either a student can displace a lower-priority
student at a school, or can be assigned to a school with available capacity without violating feasibility. These two cases
correspond, respectively, to violations offairnessandnon-wastefulness, standard notions in the literature on matching
with distributional constraints [Kamada and Kojima, 2024].
Definition 1(Fairness).A matching µ isfairif there does not exist a pair (s, c)such that (i) s strictly prefers c to µ(s),
and (ii) there exists a students ′ ∈µ(c)with lower priority thansatc.
Definition 2(Non-wastefulness).A matching µ isnon-wastefulif there does not exist a pair (s, c)such that (i) s strictly
prefers c to µ(s), and (ii) the matching µ′, obtained by reassigning s to c and leaving all other students’ assignments
unchanged, is feasible.
The inherent tension between fairness and non-wastefulness under global capacity constraints can be illustrated by the
following example.
Example 1.Consider an instance with two students S={s 1, s2} and two schools C={c 1, c2}. The system is subject
to a global quota k= 1 , so that at most one student can be assigned in any feasible matching. Preferences and priorities
are perfectly misaligned: student s1 prefers c2 over c1, and s2 prefers c1 over c2, while school c1 ranks s1 above s2,
and c2 ranks s2 above s1. We claim that no deterministic matching satisfies both fairness and non-wastefulness. If we
assign s1 to c1, the matching is wasteful because s1 prefers c2 and reassigning s1 to c2 remains feasible (k= 1 ). If we
instead assign s1 to c2, fairness is violated because s2 has higher priority at c2 and prefers c2 to being unmatched.
By symmetry, assigning s2 to c2 is wasteful, while assigning s2 to c1 violates fairness. Therefore, every non-empty
deterministic matching either violates fairness or is wasteful.
The impossibility result in Example 1 reveals a fundamental limitation of deterministic mechanisms under global
constraints. This motivates the introduction of randomization as a relaxation of deterministic assignments. To
illustrate, let µ(1) be the matching with µ(1)(s1) =c 2, and let µ(2) be the matching with µ(2)(s2) =c 1. The lottery
P= 1 2 µ(1) + 1 2 µ(2) assigns each student to their top choice with probability 1/2. While such randomization does not eliminate instability ex post, it redistributes instability more evenly across agents, thereby mitigating systematic
disadvantage and yielding a more balanced notion of ex-ante fairness.
A random assignment is represented by a marginal probability matrix P∈[0,1] |S|×|C| , where each entry Ps,c denotes
the probability that student s is assigned to school c. Let F denote the set of feasible random assignments if it satisfies
the following two conditions: each student is assigned to exactly one option (including the outside optionc 0), and the
global capacity constraint is satisfied in expectation up to slackk. Formally,
F=


P∈[0,1] |S|×|C|

 X c∈C Ps,c = 1,∀s∈S; X c∈C\{c 0} max  0, X s∈S Ps,c −q c ! ≤k    .(2)
We next introduce differentiable notions of ex-ante envy and ex-ante waste, which respectively extend fairness and
non-wastefulness to probabilistic assignments. For any students s, s′ ∈S and school c∈C , we define theex-ante envy
1We assume all students are acceptable to all schools from the schools’ perspective, as is standard in the school choice literature;
this assumption does not affect the design of our algorithm.
3

intensityofstowards ′ at schoolcunder assignment matrixPas:
es,s′,c(P) =P s′,c ·max  vs,c − ¯Vs(P),0 	 ·I(u s,c > us′,c),(3)
where ¯Vs(P) = P d∈C Ps,dvs,d denotes the expected utility of student s under the probabilistic assignment P , and I(·) is the indicator function. This intensity captures three critical factors: (i) the probability mass Ps′,c allocated to student
s′, (ii) the potential marginal gain in expected utility if s were assigned to c instead, and (iii) the priority condition
I(us,c > us′,c)which ensures that envy is onlyjustifiedwhenshas a strictly higher priority thans ′ at schoolc.
Aggregating over all students s′ ∈S and all schools c∈C , we define the total ex-ante envy experienced by student s
as the normalized intensity across the population:
Es(P) = 1 |S| X s′∈S X c∈C es,s′,c(P).(4)
Let E(P) = (E s(P)) s∈S ∈R |S| + denote the resulting envy vector. This construction captures how ex-ante envy is
distributed across students under random assignments. Unlike discrete notions of justified envy, the continuity of
E(P) allows the mechanism to minimize not only the aggregate magnitude of justified envy but also to penalize its
distribution, ensuring that no single agent suffers disproportionately, especially when global constraints render perfect
fairness unattainable.
We extend non-wastefulness to random assignments through a slack-modulated intensity formulation. Let ℓc(P) =P
s∈S Ps,c denote the expected load at school c. Define the total overflow as Ω(P) = P c∈C max{ℓc(P)−q c,0} .
Slack arises from two complementary sources. Thelocal slackat school c is given by sloc c (P) = max{q c −ℓ c(P),0} ,
capturing unused target capacity. Theglobal slackis given by sglob(P) = max{k−Ω(P),0} , capturing the remaining
allowable over-enrollment under the global slack. The ex-ante waste intensity for student s at school c is then defined as
ws,c(P) = max

vs,c − ¯Vs(P),0 	 ·min  1, sloc c (P) +s glob(P) 	 (5)
where ¯Vs(P) is the expected utility as defined previously. The waste intensity captures the potential utility gain for
student s from being assigned to school c, scaled by the extent to which such an assignment is feasible under the
available slack. By averaging over all schools, we define the total ex-ante waste for studentsas
Ws(P) = 1 |C| X c∈C ws,c(P)(6)
Let W(P) = (W s(P)) s∈S ∈R |S| + denote the resultingwaste vector. Together, E(P) and W(P) provide a unified,
differentiable representation of ex-ante instability, characterizing how fairness and non -wastefulness violations are
distributed across agents.
Given an instance I, let M:V 7→∆(X) denote a mechanism that maps reported preference profiles to a probability
distribution over feasible matchings X . A mechanism M isstrategyproof(SP) if, for every student s∈S , any true
preference profileV, and any possible misreportV ′ s , it holds that:
Eµ∼M(Vs,V−s)

vs,µ(s)

≥E µ∼M(V ′s ,V−s)

vs,µ(s)

,(7)
where V−s denotes the reported preferences of all students other than s, and the expectation is taken over the internal
randomness of the mechanism. Under this definition, truthful reporting is a dominant strategy for all students, ensuring
that no agent can gain a higher expected utility by misrepresenting their preferences.
4 MenuNet Mechanism
We begin by introducing a straightforward deterministic menu mechanism, which serves as the basis of our neural
approach. Instead of directly producing assignments, the mechanism decouples the allocation process into two stages:
menu designandindividual choice. For each student, the mechanism specifies a menu of available schools, from
which the student selects their most preferred option. To ensure strategy-proofness, the menu must be constructed
independently of each student’s own reported preferences, although it may depend on the reports of other students.
However, the mechanism does not guarantee feasibility, as multiple students may select the same popular schools,
potentially resulting in assignments that violate the capacity constraints.
4

4.1 MenuNet: A Neural Menu Mechanism
We next introduce MenuNet, a neural mechanism that generates personalized probabilistic menus and optimizes
system-level objectives via differentiable loss functions. This framework preserves strategy-proofness by construction
while enabling the mechanism to internalize complex feasibility and stability constraints through end-to-end training.
At a high level, MenuNetconsists of two stages: (i)menu generation, where each student is assigned a personalized
probability distribution over schools, and (ii)assignment, where the final allocation is realized based on the student’s
preferences and the generated menu.
Menu Generation:For each student s∈S , we construct a personalizedprobabilistic menuusing a shared neural
network Fθ parameterized by θ. The input to the network captures the global market state, including the priority
matrix U, the capacity vector q, and the student preferences. To satisfy strategy-proofness, we adopt a leave-one-out
construction for the preference input: for each student s, the network only observes the preferences of all other agents,
denoted byV −s. The personalized menu for studentsis thus given by
ps =F θ(V−s, U, q)∈[0,1]m,
where each component ps,c represents the probability that school c is available to student s. We fix the availability of
the outside option top s,c0 = 1, ensuring that every student has at least one guaranteed feasible selection.
Assignment:Given the probabilistic menu ps, the final assignment probability is realized through a sequential
choice rule that reflects the student’s preference ranking. For each student s, let the schools be indexed such that
c1 ≻s c2 ≻s · · · ≻s cm according to their reported utilities. The marginal probability Ps,cj of student s being assigned
to their j-th preferred school cj is defined as the joint probability that cj is available and all more preferred schools
{ck}k<j are unavailable:
Ps,cj =p s,cj
Y
k<j
(1−p s,ck ).(8)
By this construction, the total assigned probability satisfies P c∈C Ps,c ≤1 , with any residual mass implicitly allocated to the outside option. To ensure numerical stability during the backward pass and avoid vanishing gradients in long
preference chains, we compute the assignment probabilities in the log-domain:
logP s,cj = logp s,cj +
X
k<j
log(1−p s,ck ).(9)
The resulting assignment matrix P is a continuous and differentiable function of the menu parameters ps, enabling the
use of gradient-based optimization to minimize the envy and waste losses defined previously.
Theorem 1.The MenuNet mechanism is strategyproof for students.
Proof. To prove that the MenuNet mechanism M is strategyproof, we must show that for any student s∈S , reporting
true preferencesV s maximizes their expected utility, satisfying the condition:
Eµ∼M(Vs,V−s)

vs,µ(s)

≥E µ∼M(V ′s ,V−s)

vs,µ(s)

,∀V ′ s .(10)
The mechanism M decouples the allocation into two stages. First, a probabilistic menu ps is generated via the neural
network Fθ(V−s, U, q). By theleave-one-outarchitecture, ps is functionally independent of student s’s own report.
Thus, for any misreportV ′ s , the generated menu remains constant:p s(Vs, V−s) =p s(V ′ s , V−s) =p s.
Second, given a fixed ps, student s is assigned to schools based on their reported ranking. Let the reported ranking be
c1 ≻s c2 ≻s · · · ≻s cm. The expected utility of studentsis given by:
Us(Vs |p s) =
mX
j=1

ps,cj
Y
k<j
(1−p s,ck )

 vs,cj .(11)
This assignment rule can be viewed as a sequential application process where the student applies to schools in the
reported order, and each school c admits the student independently with probability ps,c if reached. We show that Us is
maximized if and only if the student reports the true descending order of utilities.
Consider any two schools c and c′ that are adjacent in the reported ranking, appearing at positions j and j+ 1 . Let
α= Q k<j (1−p s,ck ) be the probability that the student is not admitted by any school ranked higher than j. If c is
ranked beforec ′, the contribution of these two positions to the expected utility is:
∆ =α[p s,cvs,c + (1−p s,c)ps,c′vs,c′].(12)
5

If the student swaps the order ofcandc ′, the new contribution becomes:
∆′ =α[p s,c′vs,c′ + (1−p s,c′)ps,cvs,c].(13)
The difference between the two cases is:
∆−∆ ′ =α ps,cps,c′ (vs,c −v s,c′).(14)
Since α, ps,c, ps,c′ ∈[0,1] , the sign of the difference is determined solely by (vs,c −v s,c′). Specifically, if vs,c ≥v s,c′,
placingcbeforec ′ weakly increases the expected utility.
Any misreport V ′ s that induces an ordering different from the true utility ranking can be transformed back to the truthful
ranking through a finite sequence of such adjacent swaps. Since each swap toward the true order non-decreasingly
improves the expected utility, the truthful report Vs must be an optimal strategy. Because the menu ps is invariant to Vs,
studentshas no incentive to misreport, completing the proof.
4.2 Optimization Objectives and Training
In our framework, market instances are characterized by the tuple (V, U), where student preferences and school
priorities are sampled from a distribution representative of the target market. The network Fθ is trained offline to
minimize a composite objective over a large set of sampled instances. A key advantage of this approach is that after
training, the mechanism requires no instance-specific optimization; for any newly encountered market, the assignment
matrix P is obtained via a single forward pass of the network. This ensures that the mechanism is computationally
efficient and scalable to real-time allocation problems.
We train MenuNet by optimizing a loss function L(P) that reflects the core desiderata of market design. For a given
assignmentP, the total loss is defined as:
L(P) =λ wLwelf(P) +λ cLcapa(P) +λ sLstab(P),(15)
where the coefficients λ control the trade-offs between competing objectives. Specifically, Lwelf represents the negative
social welfare, Lcapa penalizes violations of the global capacity constraint k, and Lstab captures the magnitude and
distribution of instability through the ex-ante envy and waste vectors defined previously.
Welfare Loss.To encourage assignments that align with student preferences and promote social efficiency, we
incorporate an aggregate welfare metric into the learning objective. Minimizing Lwelf pushes the mechanism toward
allocations where students receive higher-ranked schools in expectation. We define the welfare loss as the negative
average expected utility across all students:
Lwelf(P) =− 1 |S| X s∈S ¯Vs(P) =− 1 |S| X s∈S X c∈C Ps,c vs,c.(16)
Feasibility Loss: The K-Barrier Penalty.To integrate the global capacity constraint into a gradient-based framework,
we employ a smooth penalty based on the total expected overflow. Let ℓc(P) = P s∈S Ps,c denote the expected load at schoolc, and define the total overflow as
Ω(P) =
X
c∈C
max{ℓc(P)−q c,0}.
Given the permissible slackk, we define theK-barrier penaltyas a piecewise function:
Lcapa(P) =
αΩ(P),ifΩ(P)≤k,
αk+β(Ω(P)−k) 2 +γ(Ω(P)−k),ifΩ(P)> k, (17)
where α, β, γ >0are hyperparameters controlling the penalty strength. When the overflow remains within the allowable
slack, the penalty is linear, encouraging the mechanism to efficiently utilize the flexible capacity. Once the overflow
exceeds the threshold k, the penalty transitions to asuper-linear regime, combining quadratic and linear terms to sharply
penalize further violations. In our implementation, we set γ= 10 to ensure a sufficient gradient signal at the transition
boundary.
Stability Loss.Under global feasibility constraints, it is generally impossible to eliminate all blocking pairs, as
illustrated by the non-existence result in Example 1. We therefore shift our focus from total elimination to regulating
thedistributional profileof instability. We characterize instability via two metrics: the envy vector E(P)∈R |S| + and
the waste vector W(P)∈R |S| + , which capture ex-ante violations of fairness and efficiency, respectively. For each
6

component, we adopt a structured aggregation combining three principles:egalitarian(reducing total magnitude),
Rawlsian(protecting the worst-off agent), andbalanced(discouraging concentration). The resulting lossesL envy and
Lwaste are defined as weighted combinations of these terms, enabling control over both the magnitude and distribution
of instability.
Egalitarian Principle:This objective aims to reduce the aggregate magnitude of dissatisfaction across the population.
We employ the mean squared error (MSE) of the vectors to penalize larger individual violations more heavily than
smaller ones:
LE egal(P) = 1 |S| X s∈S  Es(P) 2 ,L W egal(P) = 1 |S| X s∈S  Ws(P) 2 .(18)
Rawlsian Principle:This principle prioritizes the worst-off agents by minimizing the maximum dissatisfaction
experienced by any single student. Since the max operator is non-differentiable and unsuitable for gradient-based
optimization, we approximate theL ∞ norm (the maximum operator) using a smoothlog-sum-expoperator:
LE rawl(P) =τ E log X
s∈S
exp
 Es(P)
τE

,L W rawl(P) =τ W log X
s∈S
exp
 Ws(P)
τW

,(19)
where τ >0 is a temperature parameter. As τ→0 , this objective converges to the classical minimax criterion,
effectively shielding individuals from extreme instability.
Balanced Principle:To prevent certain agents from bearing a disproportionate share of instability, we define the
balanced objectives as the variance of the dissatisfaction vectors:
LE bal(P) = Var(E(P)),L W bal(P) = Var(W(P)).(20)
By penalizing the variance, we encourage the mechanism to distribute unavoidable envy and waste more uniformly
across the student body.
The overall stability loss Lstab(P) is the weighted sum of these components, allowing for flexible control over the
trade-offs between magnitude and fairness:
Lenvy(P) =λ E 1 LE egal +λ E 2 LE rawl +λ E 3 LE bal,(21)
Lwaste(P) =λ W 1 LW egal +λ W 2 LW rawl +λ W 3 LW bal.(22)
The final objective is given by Lstab(P) =L envy(P) +L waste(P) , providing a comprehensive, differentiable measure
of ex-ante instability for end-to-end training.
5 Experiments
We evaluate the performance of MenuNet through extensive simulations across diverse market scales. To benchmark
its efficacy, we compare it against two foundational strategy-proof mechanisms: Random Serial Dictatorship (RSD),
which prioritizes non-wastefulness, and Deferred Acceptance (DA), which prioritizes fairness under global constraints.
The results indicate that MenuNet achieves a consistent trade-off between ex-ante envy and waste. In addition, it
yields allocations in which instability is more evenly distributed across agents, avoiding the concentration of violations
observed in the baseline mechanisms. From a computational perspective, the proposed approach is efficient and scalable.
Training remains tractable on a CPU, requiring approximately 10 minutes for markets with 1,000 students.
5.1 Experimental Setup: Data Generation
We evaluate the mechanism across a range of market scales, with the student population varying from100 to 2,000 in
increments of 100, while fixing the number of schools at 10. For each configuration, we generate 1,000 training, 200
validation, and100test instances.
Student preferences are generated using the Mallows model [Lu and Boutilier, 2011], which characterizes preference
profiles as noisy perturbations centered around a reference ranking ≻ref s . The dispersion parameter ϕstudent ∈(0,1]
dictates the degree of heterogeneity; smaller values signify stronger correlation among student preferences, while
ϕstudent = 1 corresponds to uniform randomness. We refer to Appendix A for a formal description of the model and the
sampling procedure. To reflect realistic constraints on student choices, we implement truncated preferences where each
student identifies only their top-k schools as acceptable. Preference utilities V are assigned as a decreasing function of
rank for acceptable schools, supplemented by small random perturbations to facilitate tie-breaking. The outside option
c0 is consistently assigned zero utility.
7

School priorities are sampled using an analogous Mallows structure, where a reference ranking ≻ref c over students is
perturbed by a dispersion parameter ϕschool. Priority scores are derived from the resulting ranks, with identical priority
assigned to students for the outside option c0 given its unlimited capacity. The total capacity is set proportional to
the number of students, with ratio 0.6 in all experiments. Individual school capacities are sampled from a Gaussian
distribution with mean equal to the average capacity per school and a specified standard deviation, and then discretely
adjusted to ensure that the total capacity exactly matches the target level. We allow limited violations of capacity
constraints via a global slack parameter K, which bounds the total overflow. In all experiments, we set K= 0.05· |S|,
allowing up to5%of the number of students as aggregate over-enrollment.
5.2 Implementation Details
The neural mechanism Fθ is parameterized as a three-layer multilayer perceptron (MLP) with256 hidden units per layer.
To enhance training stability in large-scale matching environments, each hidden layer incorporates Layer Normalization
and ReLU activation. The model is trained using the Adam optimizer with a learning rate of 1×10 −4, a batch size of
16, and a total of 30 epochs. To prevent gradient explosion and ensure numerical stability, we apply gradient clipping
with a maximum norm of 1.0. During training, the sequential survival-based construction uses a temperature parameter
τprio = 100.0 for differentiable priority comparisons, while the final evaluation is performed under a fixed scale to
ensure exactness.
All experiments are implemented using the PyTorch framework.The computational cost of the proposed approach scales
approximately linearly with the market size, and this trend is consistent across both CPU and GPU implementations. For
instance, for a market with 1,000 students, the training procedure completes in approximately 10 minutes on an Apple
M4 Max CPU, and is further accelerated to approximately 1 minute on an NVIDIA RTX 5090 GPU. The feasibility of
CPU execution is a significant practical advantage, as it demonstrates that the mechanism is computationally tractable
without the need for specialized hardware. This positioning suggests that GPU acceleration is an optional speedup
rather than a fundamental requirement for scalability, making the approach accessible for a wide range of institutional
matching applications. Detailed scaling curves for both CPU and GPU performance are provided in the appendix.
5.3 Experimental Results
We benchmark the performance of MenuNet against two foundational strategy-proof mechanisms: Random Serial
Dictatorship (RSD) and Deferred Acceptance (DA). To ensure a fair comparison, both baselines are augmented to
accommodate the global slack constraints as detailed in Appendix B.
We evaluate envy and waste across multiple aggregation criteria, including the population mean, egalitarian (MSE),
Rawlsian (maximum), and variance-based measures. Across all metrics, MenuNet consistently achieves a superior
trade-off between fairness and efficiency. Crucially, the mechanism distributes instability more evenly across the student
population, effectively mitigating the concentration of violations observed in DA and RSD. This shift toward a more
balanced profile of dissatisfaction is quantitatively depicted in Figure 2 of the Appendix.
Regarding feasibility, MenuNet respects the global flexibility budget K with high precision. As shown in Figure 3
of the Appendix, the total expected overflow remains closely aligned with the prescribed limit, with only negligible
deviations across a small subset of instances. Notably, we employ a consistent set of hyperparameters across all market
sizes. While further tuning of the penalty weights for each specific market scale could potentially eliminate these minor
slack violations entirely, our results demonstrate that a unified parameter configuration already provides robust and
reliable performance.
In terms of social welfare, MenuNet exhibits a slight performance gap compared to RSD and DA. This outcome is
anticipated, as the mechanism explicitly internalizes the costs of stability and global feasibility within its objective.
These findings underscore the inherent tension between welfare maximization and distributional stability, reinforcing
the value of a multi-objective approach that prioritizes system-wide fairness.
Overall, our experiments validate MenuNet as a principled framework for balancing competing desiderata in market
design. It achieves substantial improvements in distributional stability while maintaining computational tractability and
preserving the fundamental property of strategy-proofness.
6 Conclusion
We study mechanism design under complex distributional constraints, where stable matchings may fail to exist.
We propose MenuNet, a neural framework that shifts the objective from feasibility to the principled distribution of
unavoidable instability. By ensuring strategy-proofness by construction and optimizing vector-valued fairness objectives,
8

MenuNet enables fine-grained control over the distribution of dissatisfaction. Experiments under global capacity slack
show that it effectively balances fairness and non-wastefulness, outperforming classical benchmarks while remaining
computationally efficient at scale. These results highlight the potential of learning-based menu mechanisms as a
practical paradigm for constrained matching.
Several directions remain for future work. First, beyond standard baselines, it would be valuable to compare against
specialized strategy-proof mechanisms tailored to structured constraints, such as those based on M♮-convexity [Kojima
et al., 2018]. Second, designing more expressive and symmetry-aware neural architectures may further improve
performance and generalization. Finally, extending the framework to richer classes of multi-dimensional distributional
constraints is an important step toward broader applicability.
9

References
A. E. Roth. The evolution of the labor market for medical interns and residents: a case study in game theory.Journal of
Political Economy, 92(6):991–1016, 1984.
A. Abdulkadiro˘glu, P. A. Pathak, A. E. Roth, and T. Sönmez. The boston public school match.American Economic
Review, 95(2):368–371, 2005a.
D. Gale and L. S. Shapley. College admissions and the stability of marriage.The American Mathematical Monthly, 69
(1):9–15, 1962.
A. E. Roth and E. Peranson. The redesign of the matching market for american physicians: Some engineering aspects
of economic design.American Economic Review, 89(4):748–780, 1999.
A. E. Roth. Deferred acceptance algorithms: History, theory, practice, and open questions.International Journal of
Game Theory, 36(3):537–569, 2008.
A. Abdulkadiro˘glu, P. A. Pathak, and A. E. Roth. The New York City high school match.American Economic Review,
95(2):364–367, 2005b.
J. Correa, N. Epstein, R. Epstein, J. Escobar, I. Rios, N. Aramayo, B. Bahamondes, C. Bonet, M. Castillo, A. Cristi,
B. Epstein, and F. Subiabre. School choice in chile.Operations Research, 70(2):1066–1087, 2022.
S. Baswana, P. P. Chakrabarti, S. Chandran, Y . Kanoria, and U. Patange. Centralized admissions for engineering
colleges in India.INFORMS J. Appl. Anal., 49(5):338–354, 2019.
Yuichiro Kamada and Fuhito Kojima. Fair matching under constraints: Theory and applications.The Review of
Economic Studies, 91(2):1162–1199, 03 2024. ISSN 0034-6527. doi: 10.1093/restud/rdad046. URL https:
//doi.org/10.1093/restud/rdad046.
Z. Sun, Y . Takenami, D. Moriwaki, Y . Tomita, and M. Yokoo. Daycare matching in Japan: Transfers and siblings. In
Proceedings of the 37th AAAI Conference on Artificial Intelligence, AAAI 2023, pages 14487–14495, 2023.
Z. Sun, N. Yamada, Y . Takenami, D. Moriwaki, and M. Yokoo. Stable matchings in practice: A constraint programming
approach. InProceedings of the 38th AAAI Conference on Artificial Intelligence, AAAI 2024, pages 22377–22384,
2024.
P. Biró, T. Fleiner, R. W. Irving, and D. F. Manlove. The college admissions problem with lower and common quotas.
Theoretical Computer Science, 411(34):3136 – 3153, 2010. ISSN 0304-3975.
Y . Kamada and F. Kojima. Efficient matching under distributional constraints: Theory and applications.The American
Economic Review, 105(1):67–99, 2015.
T. Sönmez and M. B. Yenmez. Affirmative action in India via vertical and horizontal reservations.Econometrica, 90(3):
1143–1176, 2022.
O. Aygün and I. Bó. College admission with multidimensional privileges: The Brazilian affirmative action case.
American Economic Journal: Microeconomics, 13(3):1–28, 2021.
E. J. McDermid and D. F. Manlove. Keeping partners together: algorithmic results for the hospitals/residents problem
with couples.Journal of Combinatorial Optimization, 19(3):279–303, 2010.
F. Kojima, P. A. Pathak, and A. E. Roth. Matching with couples: Stability and incentives in large markets.The Quarterly
Journal of Economics, 128(4):1585–1632, 2013.
D. Delacrétaz, S. Kominers, and A. Teytelboym. Matching mechanisms for refugee settlement.American Economic
Review, 113(10):2689–2717, 2023.
H. Aziz, J. Chen, S. Gaspers, and Z. Sun. Stability and Pareto optimality in refugee allocation matchings. In
International Conference on Autonomous Agents and Multiagent Systems, pages 964–972, 2018.
Z. Feng, H. Narasimhan, and D. C. Parkes. Deep learning for revenue-optimal auctions with budgets. In Elisabeth
André, Sven Koenig, Mehdi Dastani, and Gita Sukthankar, editors,Proceedings of the 17th International Conference
on Autonomous Agents and MultiAgent Systems, AAMAS 2018, Stockholm, Sweden, July 10-15, 2018, pages 354–362.
International Foundation for Autonomous Agents and Multiagent Systems Richland, SC, USA / ACM, 2018. URL
http://dl.acm.org/citation.cfm?id=3237439.
J. Rahme, S. Jelassi, J. Bruna, and S. M. Weinberg. A permutation-equivariant neural network architecture for
auction design. InThirty-Fifth AAAI Conference on Artificial Intelligence, AAAI 2021, Thirty-Third Conference on
Innovative Applications of Artificial Intelligence, IAAI 2021, The Eleventh Symposium on Educational Advances in
Artificial Intelligence, EAAI 2021, Virtual Event, February 2-9, 2021, pages 5664–5672. AAAI Press, 2021. doi:
10.1609/AAAI.V35I6.16711. URLhttps://doi.org/10.1609/aaai.v35i6.16711.
10

Z. Duan, J. Tang, Y . Yin, Z. Feng, X. Yan, M. Zaheer, and X. Deng. A context-integrated transformer-based neural
network for auction design. InProceedings of the 39th International Conference on Machine Learning, volume 162
ofProceedings of Machine Learning Research, pages 5609–5626. PMLR, 17–23 Jul 2022.
D. Ivanov, I. Safiulin, I. Filippov, and K. Balabaeva. Optimal-er auctions through attention. InAdvances in Neural
Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022, NeurIPS
2022, New Orleans, LA, USA, November 28 - December 9, 2022, 2022.
P. Dütting, Z. Feng, H. Narasimhan, D. C. Parkes, and S. S. Ravindranath. Optimal auctions through deep learning:
Advances in differentiable economics.J. ACM, 71(1):5:1–5:53, 2024. doi: 10.1145/3630749. URL https:
//doi.org/10.1145/3630749.
S. Ravindranath, Z. Feng, S. Li, J. Ma, S. Kominers, and D. C. Parkes. Deep learning for two-sided matching.CoRR,
abs/2107.03427, 2021. URLhttps://arxiv.org/abs/2107.03427.
S. Das and E. Kamenica. Two-sided bandits and the dating market. InProceedings of the Nineteenth International
Joint Conference on Artificial Intelligence, Edinburgh, Scotland, UK, July 30 - August 5, 2005, pages 947–952, 2005.
L. T. Liu, H. Mania, and M. I. Jordan. Competing bandits in matching markets. InThe 23rd International Conference
on Artificial Intelligence and Statistics, AISTATS 2020, 26-28 August 2020, Online [Palermo, Sicily, Italy], volume
108 ofProceedings of Machine Learning Research, pages 1618–1628, 2020.
L. T. Liu, F. Ruan, H. Mania, and M. I. Jordan. Bandit learning in decentralized matching markets.J. Mach. Learn.
Res., 22:211:1–211:34, 2021.
Soumya Basu. Competing bandits in matching markets via super stability. InForty-second International Conference
on Machine Learning, ICML 2025, Vancouver, BC, Canada, July 13-19, 2025, Proceedings of Machine Learning
Research. PMLR / OpenReview.net, 2025. URLhttps://proceedings.mlr.press/v267/basu25a.html.
A. E. Roth. The college admissions problem is not equivalent to the marriage problem.Journal of Economic Theory,
36(2):277–288, 1985.
T. Lu and C. Boutilier. Learning mallows models with pairwise preferences. InProceedings of the 28th International
Conference on Machine Learning (ICML-11), pages 145–152, 2011.
F. Kojima, A. Tamura, and M. Yokoo. Designing matching mechanisms under constraints: An approach from discrete
convex analysis.J. Econ. Theory, 176:803–833, 2018.
E. Budish, Y . Che, F. Kojima, and P. Milgrom. Designing random allocation mechanisms: Theory and applications.
American Economic Review, 103(2):585–623, April 2013. doi: 10.1257/aer.103.2.585. URL https://www.aeaweb.
org/articles?id=10.1257/aer.103.2.585.
11

(a) CPU runtime scaling on markets up to 2,000 students (M4 Max).
(b) GPU runtime scaling on larger markets up to 2,000 students (RTX 5090).
Figure 1: Training time scaling with market size.
A Mallows Model and RIM Sampling
The Mallows model [Lu and Boutilier, 2011] is a distance-based exponential family distribution over the space of
permutations. Let Sm denote the set of all permutations over m items. Given a reference ranking ≻ref ∈ Sm and a
dispersion parameterϕ∈(0,1], the probability of observing a ranking≻∈ S m is defined as:
P(≻|ϕ,≻ ref ) = 1 Z(ϕ) ϕdτ (≻,≻ref ),(23)
where dτ (·,·) denotes the Kendall tau distance, which counts the number of pairwise adjacent swaps required to
transform one ranking into another. The normalization constant (partition function) Z(ϕ) is independent of ≻ref and
admits a convenient closed-form expression:
Z(ϕ) =
mY
i=1
i−1X
j=0
ϕj =
mY
i=1
1−ϕ i
1−ϕ .(24)
12

Figure 2: Ex ante fairness and non-wastefulness metrics.
Figure 3: Capacity usage under flexible quotas.
As ϕ→0 , the distribution concentrates its mass entirely on the reference ranking ≻ref, whereas ϕ= 1 recovers the
uniform distribution overS m.
To perform efficient and exact sampling from this distribution, we employ theRepeated Insertion Model(RIM). Suppose
the reference ranking is fixed as (c1, . . . , cm). The sampled ranking is constructed incrementally by inserting each item
ci at positionk∈ {1, . . . , i}with probability:
P(itemc i is at positionk) = ϕi−k Pi
j=1 ϕi−j
.(25)
13

Starting from c1, each subsequent item ci is inserted into the existing permutation of {c1, . . . , ci−1}. This procedure
generates exact samples from the Mallows distribution under the Kendall tau distance in O(m2) time, which is highly
efficient for the market sizes considered in our experiments.
B Two Strategy-Proof Baseline Mechanisms
To benchmark the performance of MenuNet, we consider two classical mechanisms that preserve strategy-proofness
while exhibiting complementary trade-offs between fairness and efficiency under global capacity constraints.
Random Serial Dictatorship (RSD).We consider a variant ofRandom Serial Dictatorshipadapted to the flexible
capacity setting. The mechanism first samples a random permutation (master list) over students σ∈ SN with uniform
probability. Students are processed sequentially according to σ. When student s is processed, they are assigned to their
most preferred school c that is stillglobally feasible. In this context, a school c remains feasible if the current total
enrollment across all schools does not exceed the aggregate capacity P j∈C qj +K.
By construction, this mechanism is strategy-proof, as each student faces a serial decision over a fixed set of available
options. Moreover, RSD isnon-wasteful: if a student can be assigned to a more preferred school without violating the
global constraint K, the algorithm will prioritize that assignment. However, RSD does not account for school priorities,
which typically leads to significant justified envy as earlier students in the ordering can displace those with higher
priority. Consequently, while efficient, the mechanism is generallyunfair.
Deferred Acceptance (DA).As a complementary baseline, we employ theStudent-Proposing Deferred Acceptance
algorithm. To incorporate flexibility while preserving strategy-proofness, we must distribute the global slack K across
schoolsindependentlyof the students’ reported preferences. Specifically, we augment each school c’s nominal capacity
qc by a proportional share of the global slack, defined asq′ c =q c +⌊K/|C|⌋ , and distribute the remainder K(mod|C|)
randomly among the schools.
The standard DA algorithm is then executed using these adjusted capacitiesq′. This approach ensures that the mechanism
remains strategy-proof and eliminates justified envy with respect to the augmented capacities. However, this ex ante
allocation of slack is inherentlywasteful: since the flexibility is distributed uniformly rather than being directed by
realized demand, some schools may end up with unused slack while students desiring those seats are rejected elsewhere.
This mismatch highlights the inefficiency of rigid slack allocation compared to the adaptive, differentiable approach
used inMenuNet.
C Implementation Details
The definitions of envy and waste intensity involve discontinuous indicator functions and are therefore not directly
amenable to gradient-based optimization. To address this, we replace them with differentiable surrogates during training.
Specifically, the priority condition 1[s≻ c s′] is approximated by a sigmoid function σ(τprio ·(r s,c −r s′,c)), where
rs,c denotes the priority score of student s at school c and τprio >0 controls the sharpness of the approximation.
Furthermore, we define theutility gapas ∆s,c(P) = max{0, vs,c −¯us(P)} , representing student s’s desire for school
cabove their current expected utility¯us(P).
For waste calculation, we model the availability of seats at schoolcvia a continuous gate:
Gc(P) = min{1,[q c −ℓ c(P)] + + [K−Ω(P)] +},(26)
where [x]+ = max(0, x), ℓc(P) is the current load, and Ω(P) is the total system-wide overflow. This gate provides a
continuous interpolation between available and saturated regimes. The surrogate waste for student s at school c is then
computed as the product of the utility gap and the availability gate:w s,c(P) = ∆ s,c(P)·G c(P).
These approximations define piecewise differentiable surrogates that preserve the economic intuition of the original
definitions while enabling efficient optimization via backpropagation.
D Ex post Feasibility and Decomposition Challenges
Unlike standard capacity constraints that operate independently for each institution, theglobal slackconstraint introduces
complex interdependencies across the entire market. According to the framework established by Budish et al. [2013],
such a structure where a global constraint overlaps with local capacity limits, is generally notuniversally implementable.
14

Specifically, a probabilistic assignment matrix P that satisfies the global slack K in expectation may not admit a
Birkhoff–von Neumann decomposition into a convex combination of pure matchings that each strictly respect the
aggregate bound.
This fundamental theoretical gap presents a significant challenge for traditional combinatorial mechanisms, which
typically require a structured hierarchy of constraints to ensure feasible implementation. Our learning-based approach,
MenuNet, addresses this limitation by explicitly internalizing these non-linear dependencies through a differentiable
K-barrier penalty during training. By penalizing the expected violation, MenuNet identifies assignment distributions
that are biased toward "near-feasible" regions of the polytope. While the theoretical non-implementability remains,
our experiments (see Figure 3) demonstrate that this approach yields ex post realizations where deviations from the
global budget are negligible, effectively navigating a constraint space where exact deterministic implementation is not
mathematically guaranteed.
15
