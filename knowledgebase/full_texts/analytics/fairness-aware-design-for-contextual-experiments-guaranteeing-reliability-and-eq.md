---
title: 'Fairness-Aware Design for Contextual Experiments: Guaranteeing Reliability and Equity in Heterogeneous
  Subgroups'
url: https://arxiv.org/abs/2611.01867
category: analytics
subcategory: measurement
date: 2026-11
venue: ''
authors:
- Guangyan Gan
- Ling Zhang
- Yanhua Cheng
- Yongxiang Tang
- Kaiyuan Li
source: arxiv
pdf_url: https://arxiv.org/pdf/2611.01867
pages: 8
chars: 38390
fetched_at: '2026-11-08T12:59:45+00:00'
kb_version: 1
---

# Fairness-Aware Design for Contextual Experiments: Guaranteeing Reliability and Equity in Heterogeneous Subgroups

Fairness-Aware Design for Contextual Experiments:
Guaranteeing Reliability and Equity in Heterogeneous Subgroups
Guangyan Gan * 1,2 , Ling Zhang 3, Yanhua Cheng 2, Yongxiang Tang2, Kaiyuan Li 2,
Xialong Liu2, Peng Jiang 2
1 School of Physical and Mathematical Sciences, Nanyang Technological Unviersity, Singapore
2 Kuaishou Technology, China
3School of Management, Beijing Institute of Technology, China
guangyan001@e.ntu.edu.sg, zhangling@bit.edu.cn, chengyanhua@kuaishou.com, tangyongxiang@kuaishou.com,
likaiyuan03@kuaishou.com, liuxialong2007@sina.com,jp2006@139.com
Abstract
Experimental design is critical for evidence-based decision-
making in healthcare, marketing, and public policy. How-
ever, designing efficient experiments across heterogeneous
subgroups presents significant challenges. Existing methods
often optimize for statistical power or overall sample ef-
ficiency, overlooking crucial fairness considerations across
these different subgroups. To address this gap, we intro-
duce a Fairness-Aware Contextual Track-and-Stop Design (F-
CTSD) algorithm. The proposed F-CTSD algorithm provides
statistical guarantees on subgroup fairness while minimiz-
ing required sample sizes. We quantify the fairness-efficiency
trade-off and derive the exact sample complexity for the pro-
posed F-CTSD algorithm under its fairness constraints. We
further theoretically prove that the proposed F-CTSD algo-
rithm consistently produces accurate treatment effect esti-
mates even under fairness requirements, enhancing statisti-
cal reliability. Numerical experiments show that the proposed
F-CTSD algorithm outperforms existing methods, achieving
higher sample efficiency while reducing subgroup fairness vi-
olations by 4.95%.
Introduction
Experimental design plays a pivotal role across various do-
mains, including public policy (Bond et al. 2012; Opper
2019; Viviano 2025), healthcare (Chick, Gans, and Yapar
2022; Alban, Chick, and Forster 2023), and digital platforms
(Johari et al. 2022; Bojinov, Simchi-Levi, and Zhao 2023).
In these settings, experimenters often leverage data-driven
algorithms to adaptively optimize interventions and improve
operational efficiency. Adaptive allocation has proven to be
more efficient than traditional random experiments, such
as classical randomized controlled trials (Lai and Robbins
1985). However, a substantial body of research in the social
sciences documents pronouncedheterogeneityin treatment
effects across different groups (Angrist 2004; Varadhan and
Seeger 2013; Wager and Athey 2018; K ¨unzel et al. 2019;
Simchi-Levi, Wang, and Xu 2024). This heterogeneity is
*Corresponding author
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
particularly consequential in areas like personalized health-
care and recommendation systems, where the effectiveness
of interventions varies significantly across subpopulations.
As a result, strategies that tailor treatments based on observ-
able characteristics have gained increasing attention.
Most existing methodologies in experimental design
focus primarily on statistical objectives, such as maximiz-
ing power, minimizing variance, and reducing bias, often
overlooking fairness considerations, especially when deci-
sions affect heterogeneous subgroups (Simchi-Levi, Wang,
and Xu 2024). This neglect can systematically disadvan-
tage certain groups, raising significant ethical and regula-
tory issues. Documented real-world examples, such as dis-
criminatory pricing in e-commerce (Cohen, Miao, and Wang
2025; Xu, Qiao, and Wang 2023) and biased treatment al-
locations in healthcare (Chien et al. 2022), highlight the
importance of integrating fairness into experimental design
to ensure equitable opportunities and outcomes. Recent ad-
vances, such as the non-parametric causal forest estimator
(Wager and Athey 2018), enable robust estimation of hetero-
geneous treatment effects. Additionally, Simchi-Levi, Wang,
and Xu (2024) optimize experimental design to efficiently
identify the best treatment per subgroup under minimal sam-
ple complexity, leveraging the Best Arm Identification (BAI)
framework while explicitly modeling subgroup heterogene-
ity. Despite these strides, a critical challenge remains under-
explored: fairness in experimental design, particularly in the
context of heterogeneous and distinct subgroups.
Fairness concerns are paramount when allocation poli-
cies induce disparities across sensitive attributes such as
age, gender, or race (Viviano and Bradic 2024). In practical
applications, including personalized pricing, clinical trials,
and public policy, experimental designs that optimize solely
for efficiency risk generating unfair treatment allocations
across subgroups. These disparities not only undermine eth-
ical standards but also raise concerns related to regulatory
compliance and the credibility of experimental outcomes.
Incorporating fairness into experimental design is driven by
both ethical imperatives and practical benefits. Ensuring eq-
uitable treatment allocation safeguards vulnerable popula-
tions and fulfills social responsibilities, while fairness-aware
arXiv:2611.01867v1  [cs.AI]  1 Nov 2026

designs enhance the external validity and acceptance of ex-
perimental findings, particularly in high-stakes fields like
healthcare and public policy. However, enforcing fairness
constraints introduces inherent trade-offs: mitigating dispar-
ities often reduces statistical efficiency or restricts the adap-
tive allocation of participants to more effective treatments.
This tension calls for principled methods that explicitly bal-
ance efficiency and fairness in treatment allocation.
In this paper, we address experimental design under ex-
plicit fairness constraints within the contextual BAI frame-
work, focusing on a fixed-confidence setting. Our goal is to
develop principled algorithms that identify the optimal treat-
ment for each subgroup while rigorously enforcing fairness
constraints throughout the learning process.
We present the following contributions:
1.Sample Complexity Lower Bound.We derive an
instance-dependent lower bound on the sample complex-
ity for anyδ-weighted-Probably Approximately Correct
(PAC) algorithm that satisfies fairness constraints. This
bound quantifies the price of fairness, referring to the
additional samples required to identify the optimal arm
while adhering to fairness constraints, shading light on
the trade-off between sample complexity and fairness.
2.Algorithm Design.We propose the F-CTSD algorithm
under theδ-weighted PAC constraint. Our algorithm
asymptotically matches the sample complexity lower
bound and ensures that fairness constraints are satisfied
at each interaction round for pre-specified fairness val-
ues. Unlike the Fair Best Arm Identification (F-BAI) al-
gorithm (Russo and Vannella 2024), we introduce a novel
stopping rule tailored to theδ-weighted PAC constraint.
Additionally, our tracking procedure is probabilistic,
contrasting with the deterministic methods used in the
Contextual Track-and-Stop (CTSD) algorithm (Simchi-
Levi, Wang, and Xu 2024), which only identifies the op-
timal arm without fairness considerations.
3.Numerical Experiments.We evaluate F-CTSD on syn-
thetic datasets, showing that our algorithm outperforms
benchmark methods in both sample efficiency and mini-
mizing fairness violations.
By rigorously incorporating fairness into experimental
design, our work provides both methodological innovations
and practical insights for conducting equitable and efficient
experiments in heterogeneous populations.
Related Work
Our work intersects three primary research areas: adaptive
experimental design, best arm identification, and fairness.
We provide an overview of each in Appendix.
Fairness-Ware Experimental Design
This section formulates the adaptive experimental design
problem using a contextual bandit framework and studies a
fairness-ware experimental design problem.
Adaptive Experimental Design
We study an adaptive experimental design problem within
a contextual bandit framework. At each discrete time step
t, a single experimental unit arrives with contextual in-
formationx t from a discrete and finite contextual space
X:={1,2,...,M}. Eachx t corresponds to a subgroup
based on pre-treatment characteristics. For a given prob-
lem instanceν, we assumex t is independent and identi-
cally distributed (i.i.d.) generated from an unknown distri-
butionPν,x, whereP ν(xt =x) =p ν,x >0for allx∈X.
Upon observingx t, the experimenter assigns a treatment
at∈A:={1,2,...,K}. The environment generates poten-
tial outcomesr xt,a for each treatment optiona∈A, but
only reveals the rewardr xt,at associated with the selected
treatmenta t. At timet+ 1, the experimenter can only uti-
lize the observed information collected in the historyH t =
(x1,a1,rx1,a1,...,x t,at,rxt,at).This history forms a filtra-
tion{H t}t≥1 updated per treatment. For subgroupxand
treatmenta, letν x,a denote the distribution of rewardr x,a
with meanθ x,a. We formally define the instance for sub-
groupxasν x = (νx,1,...,ν x,K)and its mean reward vec-
tor asθx = (θx,1,...,θ x,K)⊤. Therefore, every problem in-
stance can be formally denoted byν= (P ν,x,(νx)x∈X ),
and all the possible instances forming the setS.
We adopt the standard identifiability condition in
adaptive experimental design (Simchi-Levi, Wang, and Xu
2024): for each subgroupx∈X, there exists a unique op-
timal treatmenta ∗ x(ν) := argmax a∈Aθx,a.This hetero-
geneity condition reflects empirical evidence that optimal
treatments systematically differ across subgroups (Ober-
meyer and Emanuel 2016; Lada et al. 2019; Imai and
Ratkovic 2013). The experimenter aims to output an opti-
mal treatmentˆax for each subgroupxsuch thatˆax =a∗(νx)
with high statistical confidence. Aligning with Simchi-Levi,
Wang, and Xu (2024), we formalize this guarantee through
aδ-weighted Probably Approximately Correct (PAC) con-
straint.
Definition 1(δ-weighted-PAC constraint (Simchi-Levi,
Wang, and Xu 2024)).For any instanceνinS,ˆa x satis-
fies ∑
x∈X
px,ν Pν (ˆax̸=a∗(νx))≤δ.(1)
The parameterδensures that statistical guarantees hold
with high confidence. This bound controls the decision er-
ror, where weighting by subgroup proportionsp x,ν im-
poses stricter accuracy requirements for larger subgroups.
To achieve this constraint, we minimize the expected exper-
imental budget quantified by the stopping timeτδ, the termi-
nal round where final decisionsˆax are implemented. Given
unit arrivals per round,τδ equivalently gives the total sample
size.
Fairness-Aware Experimental Design
Adaptive experimental design problems withδ-weighted-
PAC constraint aim to output an optimal treatment for each
subgroup with minimal sample complexity (i.e., minimiz-
ing the stopping timeτ δ). However, they overlook crucial

fairness considerations across these subgroups. Widely de-
ployed healthcare algorithms exhibit racial bias: Black pa-
tients assigned identical risk scores as white patients show
greater illness severity due to cost-based proxies, making
them 28.8% less likely to qualify for additional care (Ober-
meyer et al. 2019). This arises when experimental designs
prioritize cost prediction over equitable outcomes
To address systemic disparities, we formulate fair-
ness constraints ensuring minimum selection rates for each
treatment within every subgroup. These constraints pre-
vent systematic under-selection and maintain equitable treat-
ment allocation throughout the experiment. LetN x,a(t) =∑t
s=1 1{xs=x,as=a} denote the number of times arma∈A has been selected under subgroupx∈Xup to timet, and
Nx(t) =∑t s=1 1{xs=x} be the total number of observations with subgroupx. We denote theq-fairness constraints in ex-
perimental design problems.
Definition 2(q-fairness constraints).Theq-fairness con-
straint requires that the expected allocation proportion of
each arma∈Awithin every subgroupx∈Xexceeds a pre-
determined thresholdqx,a∈[0,1], i.e.,
Eν[Nx,a(τδ)]
Eν[Nx(τδ)] ≥qx,a,∀a∈A, x∈X.(2)
Whenq x,a = 0, Eq. (2) holds trivially, allowing opti-
mal strategies to select each subgroup’s best treatment with-
out fairness considerations. Conversely,qx,a>0forces full
treatment exploration, explicitly trading fairness for sample
efficiency: Lower values weaken fairness guarantees, while
higher values enforce stricter assignment equity (i.e., guar-
anteed minimum allocation proportions).
Our fairness framework generalizes and strengthens
prior work in three main aspects. First, whereas Russo and
Vannella (2024) introduce single-groupδ-PAC fairness con-
straints requiring minimum treatment probabilities, we ex-
plicitly incorporate subgroup structure and define fairness
at the subgroup level. This enables modeling heterogeneous
treatment effects while enforcing equity across subgroups,
making our approach strictly more expressive for stratified
settings. Second, while Wei, Ma, and Wang (2024) address
envy-freeness in adaptive designs, their focus on statisti-
cal power fundamentally neglects experimental cost control.
Third, our formulation directly minimizes the expected sam-
ple size—quantified by the stopping timeτ δ—under joint
fairness andδ-weighted-PAC constraint.
Integrating theδ-weighted PAC constraint withq-
fairness constraints, we define aq-fairδ-weighted-PAC al-
gorithm as follows:
Definition 3(q-fairδ-weighted-PAC algorithm).An algo-
rithm isq-fairδ-weighted-PAC if for allν∈Sandδ∈
(0,1/2), it satisfies:
(1)δ-weighted-PAC constraint(Definition 1),
(2)q-fairness constraints(Definition 2), and
(3)finite stopping:P ν(τδ<∞) = 1.
This definition formalizes fairness-aware experimen-
tal design. The fairness constraints prevent allocation dis-
parities by ensuring minimum exposureq x,a for each arm-
subgroup pair. Theδ-weighted-PAC constraint ensures sta-
tistical reliability of the selected treatments. That is, with
probability at least1−δ, the algorithm correctly identifies
the best treatment for each subgroup, with subgroup-level
errors weighted by their importancep x,ν. The finite stop-
ping condition ensures termination. Together, these yield ef-
ficient, equitable algorithms that generalize theδ-weighted-
PAC framework (Simchi-Levi, Wang, and Xu 2024) with
subgroup fairness.
The experimenter seeks aq-Fairδ-weighted-PAC algo-
rithm that minimizes the expected sample sizeEν[τδ]while
satisfying:
minE ν[τδ]
s. t.
∑
x∈X
px,ν Pν(ˆax̸=a∗ x(ν))≤δ,
Eν[Nx,a(τδ)]
Eν[Nx(τδ)] ≥qx,a,∀a∈A,x∈X.
Theδ-weighted-PAC constraint guarantees reliable iden-
tification of optimal treatmentsa ∗ x(ν)across subgroups,
while theq-fairness constraints enforce minimum allocation
thresholdsq x,a per subgroup-treatment pair—preventing
systematic neglect of therapeutic options within any sub-
group.
Fairness-Aware Contextual Track-and-Stop
Design Algorithm
This section proposes a Fairness-Aware Contextual Track-
and-Stop Design (F-CTSD) algorithm, extending recent ad-
vances in fairness-aware best arm identification (Russo and
Vannella 2024) to contextual settings. Our framework inte-
gratesq-fairness constraints into contextual best arm iden-
tification under fixed-confidence regimes. We theoretically
prove that the proposed F-CTSD algorithm is aq-Fairδ-
weighted-PAC algorithm, belonging to the Track-and-Stop
(TaS) family (Garivier and Kaufmann 2016).
The proposed F-CTSD algorithm comprises three core
components: sampling rule, stopping rule, and selection
rule. We detail each component below and give the pseudo-
code in the Appendix.
Sampling Rule
We define the sampling ruleπ={π t}t≥1 as a policy map-
ping historyH t−1∪{xt}to treatmenta t, governing exper-
imental unit allocation. The core insight is that sampling
proportional toω ⋆ x,q (θx)simultaneously minimizes sample
complexity while satisfying fairness constraints. Since the
mean reward vectorθx is unknown, we implement this via:
(1)Parameter estimation: Incrementally update reward es-
timates
ˆθx,a(t) :=
∑t
s=1rxs,as·1[xs =x,a s =a]
Nx,a(t) ,
ˆθx(t) =
(
ˆθx,1(t),..., ˆθx,K(t)
)⊤
,
with strong consistency ˆθx(t) a.s.−−→θx (Lemma 1 in Ap-
pendix).

(2)Instance mapping: Convert to exponential family in-
stance
ˆνx(t)← ˆθx(t)(via canonical parameterization).
(3)Proportion optimization: Solve the fairness-
constrained lower bound by
ω⋆ x,q(t) = argmax
ωx∈Σq
inf
ν′x∈Alt(ˆνx)
∑
a∈A
ωx,a KL(ˆνx,a,ν′ x,a).
(4)Best arm identification:
a⋆ x,t = argmax a∈A ˆθx,a(t).
The sampling rule then allocates arms to trackω⋆ x,q(t)while
respecting fairness constraints.
To enforce that the parametric uncertainty asymptoti-
cally goes to0(i.e., ˆθx(t)→θ x almost surely), we employ
a probabilistic tracking mechanism, inspired by the method
proposed in Russo and Vannella (2024). Specifically, we mix
the estimated optimal allocationω ⋆ x,q(t)with a fixed policy
πx,c via a decaying coefficientϵt = 1 2t2 , yielding:
πx(t) = (1−ϵt)·ω ⋆ x,q(t) +ϵt·πx,c.
The constant policyπ x,c guarantees every arm is sampled
infinitely often and is defined by:
πx,c,a =



qx,a,ifq x,a>0, K x0̸= 0,
1−qsum x
Kx0 ,ifq x,a = 0, K x0̸= 0,
qx,a + 1−qsum x K ,ifK x0 = 0,
whereKx0 =|{a∈[K] :q x,a = 0}|. Unlike traditional TaS
algorithms that rely on deterministic tracking (Garivier and
Kaufmann 2016; Simchi-Levi, Wang, and Xu 2024), our ap-
proach samples actions probabilistically fromπ x(t). This
probabilistic nature simplifies implementation and naturally
aligns with fairness constraints, eliminating the need for ex-
ternal exploration mechanisms. Lemma 1 and Theorem 7 in
Appendix establish the strong consistency of our parameter
estimates.
Stopping Rule
In this subsection, we introduce a novel stopping rule specif-
ically designed to align with the structure of the fairness-
aware contextual best arm identification setting. The stop-
ping rule determines when sufficient statistical evidence has
been gathered to satisfy theq-fairδ-weighted-PAC con-
straint, thereby signaling the end of the experiment. For-
mally, we define a stopping timeτδ with respect to the filtra-
tion{H t}t≥1, which governs the evolution of observations
over time.
We first define the set of alternative instances:
Alt(νx) :=
{
ν′∈Sx ⏐⏐a∗(νx)̸=a ∗(ν′) } ,
which includes all instances with a different optimal arm.
We also define a complexity measure that captures the dis-
tinguishability of the current instance from alternative ones
under fairness constraints:
T∗ q (νx) := max ωx∈Σq inf ν′x∈Alt(νx) ∑ a∈A ωx,aKL(νx,a,ν′ x,a),
(3)
where
Σq :=
{
ωx∈[0,1] K
⏐⏐⏐⏐⏐ K∑ a=1 ωx,a = 1, ωx,a≥qx,a,∀a∈X } ,
andKL(ν x,a,ν′ x,a)denotes the Kullback-Leibler di-
vergence between distributionsν x,a andν ′ x,a. We
also define, for any feasible allocationω x ∈Σ K :={
ωx∈[0,1] K|∑K a=1ωx,a = 1 } ,
T(νx,ωx) := inf ν′x∈Alt(νx)
∑
a∈A
ωx,aKL(νx,a,ν′ x,a),
and denote byω∗ x(νx)the optimizer of the maximization in
(3), which satisfies
T∗ q (νx) =T(ν x,ω∗ x(νx)).
At the population level, we define the overall complexity as
the weighted sum over all groups:
T∗ q :=
M∑
x=1
pν,xT∗ q (νx),(4)
wherepν,x is the probability of groupxunder the instance
ν. We slightly abuse notation by usingω∗ x(θx)andω ∗ x(νx)
interchangeably, as the one-parameter canonical exponential
family induces a bijection between the natural parameterθx
and the distributionν x.
To ensure valid termination, any admissible stopping
rule must satisfy the following weighted-PAC inequality
∀x,ν′ x∈Alt(ν x):
M∑
x=1
pν,x exp
{
−
K∑
a=1
Eν [Nx,a (τδ)]KL
(
νx,ν′ x )
}
≤4δ.
This expression motivates the use of an empirical analogue
as a practical and implementable stopping criterion. Inspired
from (Simchi-Levi, Wang, and Xu 2024) we define the stop-
ping time as the first roundtsuch that:
M∑
x=1
ˆp′ x(t)exp
{
−inf
ν′x∈Alt(ˆνx)
K∑
a=1
Nx,a(t)KL
(
ˆνx,a,ν′ x,a )
}
(5)
≤ϕ(t,δ),
whereˆp′ x(t) := Nx(t) t + 4 √ loglog(t) t is an optimistic esti-
mate of the true group weightp ν,x, andϕ(t,δ) = δ t3K is a time- and confidence-dependent threshold function. We
show that this rule ensures satisfaction of theq-fairδ-
weighted-PAC constraint in Theorem 3.
Importantly, our stopping rule operates jointly across
all groups, rather than applying a separate rule to each indi-
vidual group. This group-wise aggregation ensures that the
stopping condition is met globally, thereby promoting sta-
tistical parity across contexts and preserving the algorithm’s
fairness guarantees at termination.

Selection Rule
The selection rule is a measurable mapping from the ob-
served history at stopping time,Hτδ, to the set of armsAM , yielding a final decisionˆax for each context groupx∈X.
Once the stopping criterion is satisfied, the F-CSTD algo-
rithm proceeds by selecting the arm with the highest empiri-
cal mean reward for each context. Formally, for everyx∈X,
the selected arm is given by:
ˆax = argmax a∈A ˆθx,a (τδ).(6)
This rule ensures that the algorithm outputs the empirically
best arm at the stopping time, reflecting the accumulated ev-
idence under the fairness-aware and context-sensitive sam-
pling process.
Theoretical Analysis
In this section, we first establish an instance-dependent
lower bound on the sample complexity that holds for any
q-fairδ-weighted-PAC design. These bounds characterize
the minimal number of samples necessary to ensure fair and
probably approximately correct outcomes across heteroge-
neous groups. We then quantify the price of fairness in Sec-
tion , which reflects the increase in sample complexity in-
duced by fairness constraints. We next show that our pro-
posed F-CSTD isq-fairδ-weighted-PAC in Section . Then,
we establish the sample complexity guarantees of F-CSTD
in Section , and finally analyze the inference accuracy of
treatment effects in Section .
Sample Complexity Lower Bound
The following theorem states a lower bound on the sam-
ple complexity of anyq-fairδ-weighted-PAC algorithm. The
key quantity driving the lower bound is thecharacteristic
timeT∗ q in (4).
Theorem 1(Instance-dependent Lower Bound).Letδ∈
(0,1). For anyq-fairδ-weighted-PAC algorithm and any in-
stanceν∈S, the expected stopping time satisfies:
Eν[τδ]≥ log
( 1
4δ
)
T∗q .
Remark 1.Whenq= (0,...,0), the fairness constraint is
inactive and the result recovers the lower bound of (Simchi-
Levi, Wang, and Xu 2024). In the special case whereM= 1,
Theorem 1 reduces to the fairness-aware lower bound of
(Russo and Vannella 2024). ForM= 1andq= (0,...,0),
the result recovers the classical lower bound for Best-Arm
Identification (see, e.g., Garivier and Kaufmann (2016);
Kaufmann, Capp´e, and Garivier (2016)).
The Price of Fairness
We now quantify the cost incurred by enforcing fairness con-
straints through the following result, which bounds the rel-
ative increase in sample complexity. Specifically, we upper-
bound the ratio
T∗ q0
T∗q ,which measures the additional cost
(in terms of sample complexity) of imposing fairness con-
straints compared to the unconstrained setting.
Theorem 2(Price of Fairness).Letq= (q x,a)x∈X,a∈X ∈
[0,1]M×K be a nontrivial fairness constraint, and define
q0 := (0,...,0) M×K to denote the unconstrained case. Let
qmin := minx,aqx,a. Then,
1≤ T∗ q0
T∗q ≤ 1 qmin .(7)
Remark 2.Theorem 2 confirms that fairness constraints in-
evitably increase the sample complexity: for anyq̸=q 0, it
holds thatT∗ q≤T∗ q0. This highlights a fundamental trade-off between fairness and efficiency. Moreover, the upper bound
1
qmin implies that the price of fairness remains finite, even in the worst case. Stricter fairness requirements (i.e., larger
values ofq min) result in a larger increase in sample com-
plexity, reflecting a higher cost for more equitable treatment.
Fairness Guarantees
We first present the following main result, which establishes
that F-CTSD satisfies theq-fairδ-weighted-PAC property.
Theorem 3(q-fairδ-weighted-PAC Constraint).Let F-
CTSD be run withϕ(t,δ) = δ t3K . Then, F-CTSD isq-fair δ-weighted-PAC. In particular:
•Fairness:For allt≥1,x∈X, anda∈X,
E[Nx,a(t)]
Nx(t) ≥qx,a.
•δ-weighted-PAC :For every instanceν∈S,
∑
x∈X
pν,x Pν (τδ<∞,ˆax̸=a∗(νx))≤δ.
Theorem 3 confirms that F-CTSD guarantees fairness
at every round and satisfies the desiredδ-weighted-PAC con-
straints.
Sample Complexity Guarantees
We now analyze the efficiency of F-CTSD. Specifically, we
show that it achieves the optimal sample complexity asymp-
totically asδ→0, matching the lower bound in Theorem 1.
Theorem 4(Asymptotic Optimality in Expectation).Let F-
CTSD be run withϕ(t,δ) = δ t3K . Then, for allδ∈(0,1/2),
the expected sample complexity is finite, i.e.,E ν[τδ]<∞.
Furthermore, for every instanceν∈S, the following asymp-
totic guarantee holds:limδ→0 Eν[τδ]≤
log( 1 4δ )
T∗q .
Theorem 4 shows that for sufficiently smallδ, the
expected stopping time of F-CTSD closely matches the
lower bound. This suggests that approximately
log( 1 4δ )
T∗q sam-
ples are nearly necessary and sufficient to ensureq-fair
δ-weighted-PAC in expectation. In other words, the ex-
pected duration of the experiment scales proportionally with
log(1/δ), and the constant of proportionality is precisely
governed by the inverse ofT∗ q , which encodes the problem’s
inherent difficulty under fairness constraints. The detailed
proof is deferred to the Appendix.

Theorem 5(Almost Sure Asymptotic Optimality).For any
instanceν∈S, F-CTSD satisfies:
Pν
(
lim
δ→0
τδ≤ log
( 1
4δ
)
T∗q
)
= 1.
Theorem 5 is stronger than Theorem 4, as it guaran-
tees the same sample complexity bound almost surely, not
merely in expectation. Specifically, it asserts that the stop-
ping timeτ δ of F-CTSD satisfiesτ δ≤
log( 1 4δ )
T∗q with proba-
bility 1 asδ→0. This result implies that F-CTSD achieves
the optimal sample complexity almost surely in the asymp-
totic regime. Consequently, the algorithm not only performs
well in expectation but also offers robust guarantees on indi-
vidual realizations, even under fairness constraints. The de-
tailed proof is provided in the Appendix.
Inference
A central objective in experimentation is conducting reli-
able statistical inference, particularly estimating the mean
outcome of each treatment arm. Accurate mean estimation
further enables valid inference on treatment effects. This
section analyzes the concentration of the empirical mean
ˆθx,a(t)around the true meanθ x,a, thereby establishing the
inferential reliability of F-CTSD. We show that F-CTSD
guarantees high-probability confidence bounds for mean es-
timates under fairness constraints. The detailed proof is de-
ferred to the Appendix.
Theorem 6(Mean Estimation Guarantee).Letx∈X,a∈
X, andα∈(0,1). Then, with probability at least1−α, the
empirical mean ˆθx,a(t)satisfies:
P

d
(
ˆθx,a(t),θx,a
)
≤
3log
( log(Nx(t)qx,a+1)+1
α
)
Nx(t)qx,a

≥1−α,
whered(·,·)denotes a suitable divergence function, and
Nx(t)denotes the number of samples collected under con-
textxby timet.
Theorem 6 implies that the confidence interval for the
mean narrows asN x(t)andq x,a increase. We observe that
a largerq x,a (i.e., stricter fairness constraints) leads to a
smaller error bound, and hence tighter confidence intervals.
This highlights an additional benefit of fairness constraints:
although they increase the overall sample complexity and
hence the experimental cost, they also promote uniform ex-
ploration across arms. This uniformity results in more bal-
anced data and, consequently, more accurate and reliable in-
ference of treatment effects.
Numerical Experiments
In this section, we empirically evaluate the performance of
our proposed F-CSTD algorithm on both synthetic and real-
world datasets. The objective is to assess the algorithm’s
effectiveness in balancing fairness and sample efficiency
across diverse contexts.
10 20
K
0
1000
5 10 15
M
0
200
400
0.00 0.02 0.04
δ
0
500
1000
0.02 0.04
q′
75
100
0.000
0.005
0.010
0.0075
0.0100
0.00
0.01
0.02
0.04
Sample Complexity Fairness Violation
Figure 1: Impact of hyperparameters on synthetic data.
Experimental Setup
Synthetic data.We considerKarms andMcontexts.
The expected rewards(θ x,a)a∈X are linearly spaced in
[0,5], and the fairness vector is set asq=q ′[1,...,1],
withq′∈[0,1/K]. We vary the number of contextsM∈
{1,5,10,15,20}and consider multiple confidence levelsδ∈
{10−5,10−4,10−3,10−2,10−1}. Each configuration is re-
peated overN= 50independent runs.
Real-world data.We use the COVID-19 Clinical Trials
dataset (Larson et al. 2022). Contexts are defined by study
Gender, Age, and Phase, resulting inM= 29unique con-
texts. Interventions are encoded intoK= 11categories. The
reward is whether study results are posted (1) or not (0). The
sequential learning setup mirrors that of synthetic experi-
ments, with real-time updates of estimated success proba-
bilities and fairness constraints.
Baseline Algorithms
We compare F-CSTD against three baselines:
•Contextual Track-and-Stop Design (CTSD)(Simchi-
Levi, Wang, and Xu 2024): Adapts to subgroup hetero-
geneity but does not enforce fairness.
•Fair Best-Arm Identification (F-BAI)(Russo and Van-
nella 2024): Enforces fairness at the population level, as-
suming a single context (M= 1).
•UniformFair: Allocates sampling probability uniformly
while satisfying minimal fairness thresholds:
πx,a(t) =qx,a + 1−q sum x K , q sum x = K∑ a=1 qx,a.
This design guarantees that the expected sampling fre-
quency satisfiesEν
[Nx,a(t)
Nx(t)
]
≥qx,a for allt≥1.
Evaluation Metrics
We evaluate algorithms along two dimensions:
1.Sample Complexity:The expected number of samples
Eν[τδ]required to meet the confidence thresholdδ.
2.Fairness Violation:Defined at stopping timeτ δ as:
Fairness Violation=E ν [ρ(τδ)],

whereρ(t) = max
(
maxx,a
{
qx,a−Nx,a(t) Nx(t) } ,0 ) .This
measures the average maximum deviation from the pre-
scribed allocationq x,a across all groups at the stopping
timeτδ.
Algorithm Fairness Violation Sample Complexity
CTSD 0.0081 114.81
F-BAI 0.0083 34.09
UniformFair 0.0047 178.50
F-CSTD 0.0048 169.66
Table 1: Performance Comparison on Synthetic Data (q′ =
0.01,δ= 0.05,K=M= 10).
Results on Synthetic Data
Table 1 summarizes the empirical comparison of fairness vi-
olation and sample complexity on synthetic data. Our pro-
posed F-CSTD algorithm maintains a strong balance be-
tween fairness and efficiency. It achieves a fairness violation
of 0.0048, nearly matching the best baseline (UniformFair:
0.0047), while reducing sample complexity from 178.50 to
169.66. Compared to CSTD, F-CSTD reduces fairness vio-
lation by over 40% with only a moderate increase in sam-
ple complexity, demonstrating the benefit of fairness-aware
adaptive learning. Although F-BAI yields the lowest sample
complexity (34.09), it exhibits the highest fairness violation
(0.0083), exceeding F-CSTD by more than 70%. This sug-
gests that fairness enforced only at the population level may
fail to protect subgroups in heterogeneous environments.
We further analyze the impact of hyperparameters in
Figure 1. Fairness violation increases with the number of
armsK, with higher confidence levelsδ, and with looser
fairness constraints. Conversely, it decreases as the number
of contexts increases. For sample complexity, it decreases
with largerKand largerδ, but increases with more contexts
and stricter fairness constraints.
Results on COVID-19 Clinical Trials Data
Comparison with benchmarksWe compared FCTSD
with several benchmarks: CTSD, FBAI, UniformFair. Ta-
ble 2 reports the mean fairness violations and sample com-
plexity across 50 repeated experiments. FCTSD achieved an
better tradeoff between fairness and sample efficiency.
Sensitivity analysis.We performed a sensitivity analysis
on key algorithmic parameters, including the fairness con-
straint thresholdq′ and the confidence parameterδ. In Fig-
ure 2, the trends observed in real-world data were consistent
with those obtained from synthetic datasets, demonstrating
that the algorithm’s behavior is robust to parameter varia-
tions.
Discussion.F-CSTD consistently balances fairness and
sample efficiency in both synthetic and real-world datasets.
Sensitivity analyses confirm that algorithmic behavior is ro-
bust to variations in key hyperparameters (q′ andδ). These
results demonstrate the practical applicability of F-CSTD for
Algorithm Fairness Violation Sample Complexity
CTSD 0.0124 256.73
F-BAI 0.0118 102.44
UniformFair 0.0079 341.55
F-CSTD 0.0082 301.19
Table 2: Performance Comparison on Real Data (q′ = 0.01,
δ= 0.05,K= 11,M= 29).
0.000 0.025 0.050 0.075 0.100
δ
400
500
600
700
800
 Sample Complexity
Fairness Violation
0.0 0.1 0.2 0.3
q′
400
450
500
550
Sample Complexity
Fairness Violation
0.096
0.098
0.100
0.102
0.104
0.0
0.1
0.2
0.3
Figure 2: Impact of hyperparameters on clinical trials data..
adaptive decision-making scenarios where fairness across
heterogeneous contexts is critical.
Conclusion
In this work, we address the challenge of fair experimen-
tal design for heterogeneous subgroups by introducing the
F-CTSD algorithm, which enforces explicit fairness con-
straints in treatment allocation. Our theoretical analysis es-
tablishes instance-specific lower bounds on sample com-
plexity and quantifies the trade-off between fairness and ef-
ficiency. We further develop the F-CTSD algorithm, which
provably achieves these lower bounds while ensuring fair-
ness constraints are met throughout the experimental pro-
cess. Extensive experiments on synthetic data confirm that
our approach delivers a strong balance between fairness and
sample efficiency, outperforming existing methods on both
fronts.
While our framework advances the integration of fair-
ness into adaptive experimental design, it primarily focuses
on statistical objectives related to treatment identification.
Future research could explore further aligning experimental
objectives with the welfare and preferences of participants,
as well as extending the framework to more complex or real-
world settings.
Acknowledgments
The authors gratefully acknowledge Hanzhang Qin and
Zhenzhen Yan for their valuable comments and insights, as
well as the fruitful discussions that greatly contributed to this
work.
References
Alban, A.; Chick, S. E.; and Forster, M. 2023. Value-based
clinical trials: selecting recruitment rates and trial lengths in

different regulatory contexts.Management Science, 69(6):
3516–3535.
Angrist, J. D. 2004. Treatment effect heterogeneity in theory
and practice.The economic journal, 114(494): C52–C83.
Bojinov, I.; Simchi-Levi, D.; and Zhao, J. 2023. Design and
analysis of switchback experiments.Management Science,
69(7): 3759–3777.
Bond, R. M.; Fariss, C. J.; Jones, J. J.; Kramer, A. D.; Mar-
low, C.; Settle, J. E.; and Fowler, J. H. 2012. A 61-million-
person experiment in social influence and political mobiliza-
tion.Nature, 489(7415): 295–298.
Chick, S. E.; Gans, N.; and Yapar, ¨O. 2022. Bayesian se-
quential learning for clinical trials of multiple correlated
medical interventions.Management science, 68(7): 4919–
4938.
Chien, I.; Deliu, N.; Turner, R.; Weller, A.; Villar, S.; and
Kilbertus, N. 2022. Multi-disciplinary fairness considera-
tions in machine learning for clinical trials. InProceedings
of the 2022 ACM Conference on Fairness, Accountability,
and Transparency, 906–924.
Cohen, M. C.; Miao, S.; and Wang, Y . 2025. Dynamic pric-
ing with fairness constraints.Operations Research.
Garivier, A.; and Kaufmann, E. 2016. Optimal best arm
identification with fixed confidence. InConference on
Learning Theory, 998–1027. PMLR.
Imai, K.; and Ratkovic, M. 2013. Estimating treatment ef-
fect heterogeneity in randomized program evaluation.The
Annals of Applied Statistics, 443–470.
Johari, R.; Li, H.; Liskovich, I.; and Weintraub, G. Y . 2022.
Experimental design in two-sided platforms: An analysis of
bias.Management Science, 68(10): 7069–7089.
Kaufmann, E.; Capp ´e, O.; and Garivier, A. 2016. On the
complexity of best arm identification in multi-armed bandit
models. InJMLR.
K¨unzel, S. R.; Sekhon, J. S.; Bickel, P. J.; and Yu, B.
2019. Metalearners for estimating heterogeneous treatment
effects using machine learning.Proceedings of the national
academy of sciences, 116(10): 4156–4165.
Lada, A.; Peysakhovich, A.; Aparicio, D.; and Bailey, M.
2019. Observational data for heterogeneous treatment ef-
fects with application to recommender systems. InProceed-
ings of the 2019 ACM Conference on Economics and Com-
putation, 199–213.
Lai, T. L.; and Robbins, H. 1985. Asymptotically efficient
adaptive allocation rules.Advances in applied mathematics,
6(1): 4–22.
Larson, K.; Sim, I.; von Isenburg, M.; Levenstein, M.; Rock-
hold, F.; Neumann, S.; D’Arcy, C.; Graham, E.; Zuckerman,
D.; and Li, R. 2022. COVID-19 interventional trials: anal-
ysis of data sharing intentions during a time of pandemic.
Contemporary Clinical Trials, 115: 106709.
Obermeyer, Z.; and Emanuel, E. J. 2016. Predicting the
future—big data, machine learning, and clinical medicine.
New England Journal of Medicine, 375(13): 1216–1219.
Obermeyer, Z.; Powers, B.; V ogeli, C.; and Mullainathan, S.
2019. Dissecting racial bias in an algorithm used to manage
the health of populations.Science, 366(6464): 447–453.
Opper, I. M. 2019. Does helping John help Sue? Evidence of
spillovers in education.American Economic Review, 109(3):
1080–1115.
Russo, A.; and Vannella, F. 2024. Fair best arm identification
with fixed confidence.arXiv preprint arXiv:2408.17313.
Simchi-Levi, D.; Wang, C.; and Xu, J. 2024. On Experimen-
tation With Heterogeneous Subgroups: An Asymptotic Op-
timalδ-Weighted-PAC Design.Available at SSRN 4721755.
Varadhan, R.; and Seeger, J. D. 2013. Estimation and re-
porting of heterogeneity of treatment effects. InDeveloping
a protocol for observational comparative effectiveness re-
search: A user’s guide. Agency for Healthcare Research and
Quality (US).
Viviano, D. 2025. Policy targeting under network interfer-
ence.Review of Economic Studies, 92(2): 1257–1292.
Viviano, D.; and Bradic, J. 2024. Fair policy targeting.Jour-
nal of the American Statistical Association, 119(545): 730–
743.
Wager, S.; and Athey, S. 2018. Estimation and inference of
heterogeneous treatment effects using random forests.Jour-
nal of the American Statistical Association, 113(523): 1228–
1242.
Wei, W.; Ma, X.; and Wang, J. 2024. Fair adaptive experi-
ments.Advances in Neural Information Processing Systems,
36.
Xu, J.; Qiao, D.; and Wang, Y .-X. 2023. Doubly fair dy-
namic pricing. InInternational Conference on Artificial In-
telligence and Statistics, 9941–9975. PMLR.
