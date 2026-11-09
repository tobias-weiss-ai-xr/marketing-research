---
title: 'Learning When to Update: A Near-Optimal Timing Bandit Approach'
url: https://arxiv.org/abs/2609.37932
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Qiulin Lin
- Junyan Su
- Liyuan Wang
- Minghua Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.37932
pages: 17
chars: 89191
fetched_at: '2026-11-08T13:26:02+00:00'
kb_version: 1
---

# Learning When to Update: A Near-Optimal Timing Bandit Approach

Learning When to Update: A Near-Optimal Timing Bandit
Approach
Qiulin Lin, Junyan Su, Liyuan Wang
City University of Hong Kong,, Hong Kong, China
Minghua Chen
The Chinese University of Hong Kong (Shenzhen), China
City University of Hong Kong, Hong Kong, China
Abstract
Systems operating in dynamic environments require timely up-
dates to sustain performance. For resource-intensive systems such
as machine learning models and digital twins, strategically tim-
ing updates is essential. Updating too frequently wastes resources,
while updating too infrequently leads to costly performance degra-
dation. The problem is particularly challenging when the system’s
degradation pattern is unknown a priori, as is common in new oper-
ating environments. We formalize this challenge as a noveltiming
banditproblem, where each arm represents a candidate update
interval with a fixed update cost and an unknown, stochastic degra-
dation cost. Three structural properties distinguish this setting from
standard multi-armed bandits: selecting an interval commits the
learner to multiple time slots before the next update; arm costs are
composed of per-step degradation costs and a fixed update cost; and
selecting a longer interval naturally reveals degradation at every in-
termediate step, providing consecutive feedback relevant to shorter
intervals. By exploiting these structures, we develop Balanced Con-
secutive Arm Elimination (BCAE).BCAEachieves ˜𝑂( √ 𝑇) regret,
improving upon the ˜Ω(𝐾 √ 𝑇) regret of standard bandit algorithms
in this setting, where𝐾 is the number of candidate update intervals.
We further propose an Optimism-Enhanced variant (OE-BCAE) that
integrates lower-confidence-bound principles to improve empirical
adaptivity while preserving the same regret order. Moreover, the
regret bound achieved by our algorithms matches the theoretical
lower bound up to logarithmic factors. Simulation results demon-
strate that our algorithms achieve low regret and remain stable as
both the number of arms and the update cost vary.
ACM Reference Format:
Qiulin Lin, Junyan Su, Liyuan Wang and Minghua Chen. 2026. Learning
When to Update: A Near-Optimal Timing Bandit Approach. InThe Twenty-
seventh International Symposium on Theory, Algorithmic Foundations, and
Protocol Design for Mobile Networks and Mobile Computing (MobiHoc ’26),
November 23-26, 2026, Tokyo, Japan.ACM, New York, NY, USA, 17 pages.
https://doi.org/10.1145/3842721.3849669
1 Introduction
Timely updates are crucial for systems operating in dynamic envi-
ronments to sustain performance. For instance, machine learning
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
MobiHoc ’26, Tokyo, Japan
©2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-2975-1/2026/11
https://doi.org/10.1145/3842721.3849669
models need to be retrained or fine-tuned to counteract model
drift [23], a phenomenon in which the statistical properties of input
data change over time since original training, leading to a gradual
degradation in predictive performance [ 20, 35]. Digital twins of
physical assets need frequent synchronization with the real-world
state they mirror. Otherwise, the fidelity of simulation-based deci-
sions degrades [15, 31].
However, performing an update is seldom free. Retraining a
large-scale machine learning model may consume substantial com-
putational resources and energy. Synchronizing a digital twin can
require expensive sensor readings or communication bandwidth.
More specifically, in networked and edge deployments, these costs
are often dominated by communication overhead. Triggering an
update may require waking up a radio transceiver or transmit-
ting a large volume of data over a bandwidth-limited link, each of
which drains the limited battery budget of an IoT device or edge
node [3, 36]. Consequently, a system designer faces a fundamental
trade-off: updating too frequently wastes resources on unnecessary
refreshes, while updating too infrequently allows performance to
degrade, potentially incurring costs that far exceed the savings from
skipping an update.
Striking the right balance is further complicated by the fact that
degradation patterns are oftenunknown a priori. The rate at which
a model’s accuracy declines, or a digital twin’s fidelity erodes, de-
pends on the volatility of the underlying environment—a quantity
that is itself uncertain and may change across deployments. When
the degradation cost associated with each possible update interval
is known or can be modeled parametrically, the optimal update
schedule can be computed offline. In practice, however, such prior
information is rarely available, especially when a system is deployed
in a new environment. This renders the problem inherently an on-
line learning problem: the system must discover an effective update
policy through its own operational experience. The Age of Infor-
mation (AoI) literature has extensively studied update scheduling
under various application scenarios [30, 37], but it predominantly
assumes known degradation functions (or age penalty functions)
and optimizes a closed-form objective. In contrast, the setting in
which the degradation dynamics are stochastic and must belearned
online remains largely open; existing studies either assume full
knowledge of the degradation model [1, 3, 30] or adopt fully adver-
sarial formulations [22, 32, 33] that do not exploit the stochastic
structure; see a detailed discussion of related work in Section 2.
In this paper, we investigate the update scheduling problem
(USP), which involves strategically determining the timing of up-
dates under realistic conditions where future performance degra-
dation patterns are stochastic and unknown. We aim to minimize
the average total expected degradation cost and update expenses
over a time horizon. The fundamental challenge lies in learning the
arXiv:2609.37932v1  [cs.LG]  29 Sep 2026

MobiHoc ’26, November 23-26, 2026, Tokyo, Japan Lin et al.
unknown degradation costs while making real-time update deci-
sions, without prior knowledge of the degradation cost patterns
or their distributions. We frame this challenge as a novel variant
of the multi-armed bandit (MAB) problem, namedTiming Bandit,
where each arm corresponds to a candidate update interval. We
reveal three structural properties of Timing Bandit. First,timing de-
cisions: selecting arm𝑘 commits the learner to operate for the next
𝑘 time steps before performing an update, so a single decision occu-
pies a variable number of rounds rather than a single slot. Second,
arm cost composition: the cost of an arm comprises the stochastic
degradation cost that accumulates as the system ages during the
interval and a fixed update cost incurred at the end. Third,con-
secutive feedback: pulling an arm traverses every intermediate age
in sequence, revealing degradation information relevant to every
shorter interval. These structures distinguish our problem from
existing variants of MAB problems (cf. Table 1) and necessitate
novel algorithm design and analysis. To this end, we develop online
algorithms that achieve provably near-optimal, sublinear regret
bounds, where regret is defined as the performance gap relative to
an optimal strategy with known degradation cost distributions. We
summarize ourcontributionsas follows.
▷ In Sec. 3, we introduce the update scheduling problem (USP),
whose objective is to minimize the total cost comprising both sto-
chastic degradation and update expenses by optimizing the timing
of updates. We show that the optimal policy for minimizing the
asymptotic time-average total cost reduces to a periodic one, i.e.,
updating at a fixed interval.
▷ Motivated by the optimality of periodic updates, in Sec. 4, we
frame the online setting, where the stochastic degradation costs
are unknown a priori, as a novelTiming Banditproblem. Here,
each arm corresponds to a candidate update interval whose fixed
update cost is known but whose degradation costs must be learned
through interaction. We further identify three structural properties
ofTiming Bandit, including timing decisions, arm cost composition,
and consecutive feedback.
▷ In Sec. 5, we demonstrate that, resulting from the timing de-
cision structure, a direct application of standard MAB algorithms,
i.e., treating each of the𝐾 candidate intervals as an independent
arm, yields a regret of ˜𝑂(𝐾 √ 𝑇) rather than the usual ˜𝑂( √ 𝐾𝑇) . We
then propose an efficient online algorithm, namely Balanced Con-
secutive Arm Elimination (BCAE), for the timing bandit. Built on
arm elimination, our algorithm further leverages a novel idea of
balancing the confidence gaps across all arms, enabling joint use
of the specific arm cost composition and the consecutive feedback
structures. We prove that our algorithm achieves sublinear regret
bounds of ˜𝑂( √ 𝑇) for sufficiently large𝑇 , removing the 𝐾 multi-
plicative overhead found in applying standard MAB algorithms. We
show that the achieved regret matches the regret lower bound for
the problem up to logarithmic factors. While analytically conve-
nient, the elimination paradigm adapts only at infrequent, discrete
elimination events, limiting empirical responsiveness. To address
this, we further propose an Optimism-Enhanced variant (OE-BCAE)
that integrates Lower Confidence Bound (LCB) principles into the
elimination framework, enabling continuous adaptation while pre-
serving the same order regret.
Table 1: Comparison with related stochastic multi-armed
bandit (MAB) problems.
MAB
Problems
Timing
Decisions
Consecutive
Feedback
Arm Cost
Composition Regret
Standard, e.g., [19]✗ ✗ ✗ ˜𝑂( √ 𝐾𝑇) ★
One-Sided, e.g., [5, 21, 38]✗ ✓ ✗ ˜𝑂( √ 𝑇) ★
Side Info. [7]✗ ✓ ✗ ˜𝑂( √ 𝐾𝑇)†
Batch, e.g., [6, 14, 25] ✓ ✓ ✗ ˜𝑂(ℎ(·))‡★
Timing Bandit
(this work) ✓ ✓ ✓ ˜𝑂( √ 𝑇) ★
★ Denotes the regret bound matches its lower bound up to logarithmic factors.
† Result when applied to the consecutive or one-sided feedback case.
‡ℎ(·)= √ 𝐾𝑇 1/(2−2 1−𝑁) , where𝑁represents the number of batches.
▷ We validate our theoretical findings through numerical evalu-
ation in Sec. 6 and evaluate the empirical performance on a remote
monitoring instance using real-world traces in Sec. 7. The experi-
ments demonstrate that our approaches, in particularOE-BCAE,
achieve lower regret and remain robust to changes in both the
number of arms and the update cost.
2 Related Work
Multi-armed Bandit.We considerTiming bandit, a novel variant
of the classical multi-armed bandit (MAB) framework [ 28] with
structural properties tailored to our setting. This variant differs from
traditional MAB problems in decision-making, feedback mecha-
nisms, and arm cost composition, which require new algorithm
design and analysis, as we will elaborate in Sec. 4 and Sec. 5. We
summarize the comparison of the most-related variants of bandit
problems in Table 1. While some properties of our problem can be
considered individually as special cases of other MAB paradigms,
there is no direct generalization from these paradigms that accounts
for all of our problem’s properties. In particular, in [ 5, 7, 21, 38],
the authors consider bandits in which pulling an arm also provides
samples of arms with smaller (or larger) indexes, similar to our
consecutive feedback structure. Also, the timing decision structure
that pulling an arm, say𝑘, occupies𝑘 slots and reveals feedback
of the first𝑘 arms, can be viewed as pulling a batch of the first𝑘
arms in the batched multi-armed bandit problem [6, 14, 25]. How-
ever, we note that, rather than the learner choosing a subset of
arms to observe, it is the temporal physics of the timing bandit
that determines the timing of observations, and we cannot choose
arbitrary batches. Other examples include that the way the arm
cost is composed in our problem can be connected to the combina-
torial multi-armed bandit problem [10–12], The paper in [8], which
focuses on the control of a renewal reward process, exhibits the
property of consecutive feedback, where choosing a longer inter-
rupt time also reveals feedback of a shorter one. Here, we exploit
all three properties of the problem with novel algorithmic design
and achieve a provable, improved sublinear regret, which matches
the lower bound regret within logarithmic factors.
Age-of-Information Optimization.Our problem is also re-
lated to the Age-of-Information (AoI) optimization in communica-
tion networks [18, 37]. AoI captures the freshness of information
received at the destination, and the general goal for AoI optimiza-
tion is to maintain a low AoI by optimizing the update process.

Learning When to Update: A Near-Optimal Timing Bandit Approach MobiHoc ’26, November 23-26, 2026, Tokyo, Japan
Our approach extends to AoI optimization scenarios where the age-
dependent penalty follows some unknown random distribution, in
contrast to prior studies that typically consider known, determinis-
tic penalties [3, 32], known, random age-dependent rewards [9], or
unknown adversarial penalties [33, 34]. In addition, our problem
generalizes to age-dependent update cost, whereas constant update
cost is commonly considered in the literature, [33, 34]. Our work
is closely related to the single-source, bandit-feedback framework
explored in [34], where online decision-making is studied under ad-
versarial penalty functions for information aging, using algorithms
such as Follow the Perturbed Leader (FTPL) and EXP3. Another line
of work studies AoI bandits, e.g., [13], where the arms are channels
with unknown success probabilities and the age penalty is determin-
istic. In contrast, our study considers model degradation with an
unknown, age-dependent distribution and further investigates how
incorporating the specific problem structures can yield improved,
near-optimal regret bounds.
3 Model and Problem Formulation
We consider a general scenario where a system operator maintains
a deployed model in a dynamic environment, such as operating
a machine learning inference model, a digital twin, or a remote
monitoring system in volatile edge and IoT environments. As the
underlying physical environment or data distribution evolves, the
deployed model becomes stale, and the operator must determine
the optimal schedule for retraining or synchronizing it. Our goal is
to minimize the total cost, which comprises deterministic update
costs (e.g., data acquisition and computation) and the stochastic
performance degradation costs due to model staleness. We discuss
the optimal solution with known degradation patterns and the
performance metrics.
3.1 System Model
We consider a slotted time horizon with 𝑇 slots. The deployed
model is implemented at the beginning of the first slot. Similarly,
we consider that updates of the model (if any) are conducted at the
end of the slot and become available at the beginning of the next
slot. An illustration of our system model is provided in Fig. 1.
System Age and Freshness.To quantify staleness, we denote
the age of the model at slot𝑡 as𝑎𝑡 . The age evolves as follows. It is
initialized to one at slot1. At any subsequent slot𝑡, if no update was
performed at the end of the previous slot, the age increments by one.
If an update was performed, the age resets to one. 1 Consequently,
the age evolution is given by,
𝑎𝑡 =
(
1,if𝑡=1or the model is updated at𝑡−1;
𝑎𝑡−1+1,otherwise. (1)
We note that a smaller𝑎𝑡 indicates a fresher model. In our problem,
we consider that there is a minimum requirement on the model
update, i.e., the model cannot stay un-updated for more than 𝐾
slots to guarantee a minimum level of freshness. In such a case, we
have𝑎𝑡≤𝐾,∀𝑡∈[𝑇] . We note that our definition of model age is
similar to the Age of Information (AoI) concept in communication
networks [18, 37]; see more discussion in Sec. 2.
1Note that setting the model age to start from one is for the convenience of presentation.
Our results remain valid when the age is initialized to zero.
⋯
Age
Update Update
Slot
𝟏 𝟐 𝟑 𝟒 𝟓 𝟔 𝟕 ⋯ 𝑻
𝟑
𝟐
𝟏
Degradation cost
Probability density
Random Degradation
Figure 1: An illustration of the evolution of model age and
the associated degradation cost. At each slot, the model age
increments by one if no update is performed and resets to
one upon an update. It incurs a random degradation cost
following the probability distribution𝑓 𝑎 at age𝑎.
Degradation Cost.Let M𝜏 denote the version of the deployed
model updated at slot 𝜏. At slot 𝑡, if the model’s age is 𝑎𝑡 , the
model being used at slot 𝑡 is the one updated at 𝑡−𝑎 𝑡+ 1, i.e.,
M𝑡−𝑎𝑡+1. We define the model degradation cost as the performance
loss of applyingM𝑡−𝑎𝑡+1 at slot𝑡 and denote it as𝑔𝑡(M𝑡−𝑎𝑡+1). In
practice, performance degradation is driven by volatile and often
unpredictable factors, such as sudden shifts in user behavior, envi-
ronmental noise, or random state transitions in a physical system.
To capture this inherent uncertainty, we model the degradation
cost as a random variable. For ease of presentation, we simplify the
notation to𝑔𝑡(𝑎𝑡). We assume that the degradation costs at differ-
ent slots are independent and their distributions depend strictly on
the model’s age. We let𝑓𝑎 denote the probability density function
(PDF) of the degradation cost for a given age 𝑎. Thus, 𝑔𝑡(𝑎𝑡) is
randomly generated from the distribution𝑓𝑎. We assume that the
degradation cost is upper bounded by a maximum constant𝑀, i.e.,
𝑔𝑡(𝑎𝑡)≤𝑀,∀𝑡,𝑎 𝑡 . We denote the expected value of𝑔𝑡(𝑎𝑡) as ˜𝑔(𝑎𝑡).
Remark1.Our model assumes i.i.d. degradation costs for a given
age and independent costs across slots. While these assumptions
may not capture all non-stationary drift, they provide a tractable
and non-trivial foundation for algorithm design. Here, we discuss
the applicability of the model and where it is an approximation.
The independence assumption is plausible in systems serving in-
dependent requests, where the degradation noise stems primarily
from the variance of individual request feedback. Moreover, the
update interval materially affects performance in such systems [20],
which supports modeling the degradation cost as a function of age.
The age-based cost structure is also natural in remote monitoring
of temporally correlated processes, where independence does not
hold exactly; examples include remote estimation of a Wiener pro-
cess [29] and the power-grid frequency trace of our empirical study
(Sec. 7), on which the algorithms remain effective. The model is an
approximation when the degradation is driven by observed con-
text (e.g., ML retraining, digital twins) or the feasible action set by
resource availability, rather than by age alone. These cases would
require extensions, including a contextual-bandit formulation with
observable context features and a constrained formulation with
resource-dependent action sets. Further, time-varying degradation
distributions could be handled by building on non-stationary [4]
or rising-bandit [24] methods. We leave this for future work.

MobiHoc ’26, November 23-26, 2026, Tokyo, Japan Lin et al.
System Updating Cost.Updating the deployed model incurs
an explicit system cost, which may encompass data acquisition,
computational overhead, and network transmission. We define𝐶(𝑎)
as the cost to update an asset that currently has an age of𝑎. Because
updates occur at the end of a slot, an update at slot𝑡 operates on an
asset of age𝑎𝑡 , incurring a cost of𝐶(𝑎𝑡). Formulating the cost as a
function of age accommodates practical scenarios where updating a
heavily degraded system requires more extensive data collection or
longer retraining times, meaning𝐶(𝑎) may increase with𝑎. It also
generalizes from existing studies that consider a constant update
cost, e.g., [32, 33].
Remark2.Unlike the degradation cost, which must be learned
online, we assume the update cost𝐶(𝑎) is knowna priori: update
expenses are dominated by deterministic system-level resources
(radio energy, bandwidth tariffs, cloud fees) that a designer can
profile offline.
3.2 Problem Formulation
We aim to find an optimal update policy that minimizes the ex-
pected total cost, encompassing both the update cost and the degra-
dation cost. At the beginning of slot 𝑡∈ [𝑇] , the system oper-
ates with a model of age𝑎𝑡 and incurs a realized degradation cost
𝑔𝑡(𝑎𝑡). At the end of slot 𝑡, the decision-maker observes the his-
toryH𝑡 ={𝑎 1,...,𝑎 𝑡,𝑥 1,...,𝑥 𝑡−1,𝑔 1,...,𝑔 𝑡} and makes an update
decision𝑥𝑡∈X(𝑎 𝑡)⊆{ 0, 1}, where𝑥𝑡 = 1denotes triggering an
update and𝑥𝑡 = 0denotes no update. To meet the minimum re-
quirement on the model update, we ensure the age does not exceed
the maximum limit,𝐾. Then, the available action space depends
on the current age:X(𝑎𝑡)={ 0, 1} if𝑎𝑡 <𝐾 , and{1} if𝑎𝑡 =𝐾 . A
policy𝜋=(𝜇 1,...,𝜇 𝑇) is a sequence of decision rules where 𝜇𝑡
maps the historyH𝑡 to a valid action𝑥𝑡∈X(𝑎 𝑡). Let Π denote the
set of all such non-anticipatory (causal) policies. The optimization
problem is formulated as follows:
USP: min
𝜋∈Π
E𝜋
" 𝑇∑︁
𝑡=1
(𝑔𝑡(𝑎𝑡)+𝐶(𝑎 𝑡)·𝑥 𝑡)
#
(2)
s.t.𝑎 𝑡+1 =
(
1,if𝑥 𝑡 =1,
𝑎𝑡+1,if𝑥 𝑡 =0, ∀𝑡∈[𝑇−1],(3)
𝑎1 =1.(4)
We consider that our problem starts from a freshly updated model
(𝑎1 = 1). If the underlying distributions of the degradation costs
were knowna priori, the Update Scheduling Problem (USP) could be
solved optimally via standard dynamic programming. Under such
known dynamics, we can also characterize the optimal policy for the
asymptotic average cost objective, which exhibits a clear and highly
interpretable structure. In practice, however, the operator rarely
has access to these true degradation distributions beforehand. This
motivates the core focus of our work: a challengingonline scenario
where the decision-maker must simultaneously learn the unknown
degradation profile while making real-time, cost-efficient update
decisions.
3.3 Optimal Solution and Performance Metrics
Optimal Solution.We consider minimizing the asymptotic aver-
age total cost defined as
lim sup
𝑇→∞
1
𝑇 E𝜋
" 𝑇∑︁
𝑡=1

𝑔𝑡(𝑎𝑡)+𝐶(𝑎 𝑡)𝑥𝑡
#
(5)
We derive the optimal solution when the information of the
expected degradation cost ˜𝑔(𝑎𝑡),∀𝑎𝑡≤𝐾, is available.
Proposition 1.Given the expected degradation cost ˜𝑔(𝑎𝑡),∀𝑎𝑡≤
𝐾, the optimal solution to the problem in (5) is to update the learning
model periodically with the optimal period𝑘 ∗:
𝑘∗ =arg min
𝑘∈[𝐾]
˝𝑘
𝑗=1 ˜𝑔(𝑗)+𝐶(𝑘)
𝑘 .(6)
And the optimal average cost is given by
˝𝑘∗
𝑗=1 ˜𝑔(𝑗)+𝐶(𝑘 ∗)
𝑘∗ .
Because the degradation cost is independent across slots and does
not affect system dynamics, the optimal policy depends only on age;
the system reduces to a Renewal Reward process, and the Renewal
Reward Theorem gives (6). It also suggests that an efficient online
algorithm should aim to find the optimal update period. Please refer
to Appendix A. We note that Proposition 1 relates to Theorem 4
in [27], which optimizes over policies that decide based on the
age alone: under our independence assumptions, the degradation
history is decision-irrelevant, so our age-based optimum agrees
with theirs once we take the per-slot penalty as˜𝑔(𝑎)+𝐶(𝑎)−𝐶(𝑎− 1).
Regret Minimization.We use regret as a performance metric
for evaluating the performance of an online policy. We denote the
total cost of the optimal solution in Proposition 1 as 𝑂𝑃𝑇(𝑇) for
a given period length𝑇 . Given an online algorithm, we denote its
expected total cost as 𝐴𝐿𝐺(𝑇) . We define the regret 𝑅(𝑇) as the
difference between these two total costs,
𝑅(𝑇)=𝐴𝐿𝐺(𝑇)−𝑂𝑃𝑇(𝑇).(7)
In regret analysis, our goal is to develop online algorithms with
low regret. Specifically, a sublinear regret ensures that the long-
term average cost of the online algorithm converges to the same
value as the optimal solution; see e.g., [19].
4 A Novel Multi-Armed Bandit Variant
In this section, we first show that our problem can be viewed as a
new variant of the multi-armed bandit (MAB) problem; we call it
timing bandit. We then discuss its problem structures.
4.1 ConnectingUSPwith Multi-armed Bandit
Following the optimal offline solution in Proposition 1, to achieve
a lower regret in the online scenario, one should find the optimal
update interval𝑘∗ (the time between two successive updates) effi-
ciently using the observed degradation costs from online update
decisions. This follows a similar spirit to the multi-armed bandit
problem, where we aim to learn the optimal arm with low regret.
We connect theUSPproblem to MAB by treating each update in-
terval𝑘∈[𝐾] as an arm. We define the average cost of arm𝑘 as
the average cost of choosing an update interval𝑘as

Learning When to Update: A Near-Optimal Timing Bandit Approach MobiHoc ’26, November 23-26, 2026, Tokyo, Japan
Time Slot
Decision
Degradation
Total Cost
Feedback
Pull Arm

Pull Arm

+ Update +
Figure 2: An illustrative example of timing bandit. Suppose
we first pull arm2. We will observe the degradation cost of
age1and age2in the following two slots, from which we can
derive feedback on arm1and arm2. The cost of such a pull
includes the degradation cost and the update cost (at age2),
the expectation of which equals2·𝜇 2 (according to(8)).
𝜇𝑘 ≜
˝𝑘
𝑡=1 ˜𝑔(𝑖)+𝐶(𝑘)
𝑘 .(8)
With the above definition, suppose we choose an update interval
𝑘, the average degradation cost and the update cost during these
𝑘 slots will be 𝑘·𝜇 𝑘. Further, we denote 𝑛𝑘(𝑇) as the expected
number of times that the update interval 𝑘 occurs in running an
online algorithm. Then, we can show the following approximation
of the regret, which is easy to interpret under the multi-armed
bandit paradigm:
˜𝑅(𝑇)≜
𝐾∑︁
𝑘=1
𝑘·𝜇 𝑘·𝑛𝑘(𝑇)−𝑇·𝜇 𝑘∗.(9)
We give the bounds of this approximation in the following
Lemma, which is due to the rounding issue of a finite𝑇.
Lemma 2 (Approximation of regret).The difference between
the regret𝑅(𝑇)and ˜𝑅(𝑇)is given by

𝑅(𝑇)− ˜𝑅(𝑇)

≤𝐾·𝑀.(10)
Lemma 2 implies that an online algorithm achieves the same
order of regret bounds under 𝑅(𝑇) and ˜𝑅(𝑇) . We thus focus on
minimizing ˜𝑅(𝑇)in the following discussion.
4.2 Timing Bandit and Problem Structures
We are now ready to relate our problem to the multi-armed ban-
dit paradigm with specific structures; we call itTiming Bandit,
referring to making timing update decisions. We consider each
update interval𝑘∈[𝐾] as an arm in a𝐾-arm multi-armed bandit
problem. Each arm𝑘 is associated with a random cost defined by
(˝𝑘 𝑖=1𝑔(𝑖)+𝐶(𝑘))/𝑘 , where𝑔(𝑖)∼𝑓 𝑖, and the mean cost of the
arm is𝜇𝑘 (defined in (8)) for all𝑘∈[𝐾] . We provide an illustrative
example in Fig. 2. Thetiming banditparadigm differs from the
standard MAB problem in its decision-making, feedback structure,
and specific arm cost composition, as detailed below:
(1) Timing decision-making: in standard MAB, the decision is
made at each time slot 𝑡 and incurs a single random cost
associated with the chosen arm. In contrast, in the timing
bandit, pulling arm𝑘 would occupy the next𝑘 time slots and
would incur𝑘·𝜇 𝑘, i.e.,𝑘 times the expected cost of the arm.
(2) Arm cost composition: In timing bandit, the cost of arm 𝑘
is defined as the sum of two components: the average of
𝑘 random degradation costs,𝑔(𝑖) from age1to age 𝑘, and
a fraction of the update cost, 𝐶(𝑘)/𝑘 . This contrasts with
standard MAB, where the cost of an arm is given by a single
random variable associated with it.
(3) Consecutive feedback: in standard MAB, we receive feed-
back immediately after pulling an arm, which is a sample
of the random cost associated with the arm. In the timing
bandit, pulling arm𝑘 yields feedback from arm1to arm 𝑘
consecutively over the next𝑘rounds.
Intuitively, the timing decision-making property makes the tim-
ing bandit problem more challenging, since pulling one arm would
occupy more time slots and incur more cost, while only giving one
sample of the pulled arm. In contrast, the second property turns
out to allow a tighter confidence bound for estimating the arm cost
that facilitates the learning, as we will discuss in Lemma 4. The
third property can facilitate learning by providing richer feedback
from a single pulling.
In the following, we characterize the challenge due to the timing
decision-making structure, which also reveals the regret bound
of directly applying the standard MAB algorithm to our problem
without utilizing the latter two properties.
Proposition 3.Consider a multi-armed bandit problem with 𝐾
arms and random costs with unknown means 𝜇𝑘,∀𝑘∈[𝐾] , where
pulling an arm (say arm 𝑘) will occupy𝑘 slots, incur𝑘 times its cost,
and receive one sample on its cost. Then, any online algorithm for the
problem will incur an expected regret of at leastΩ(𝐾
√
𝑇/log𝐾).
The proof follows the lower bound proof for the standard MAB
(see Theorem 5.1 in [2]) but with careful refinement to fit our case.
Proposition 3 shows that the timing decision property increases
the regret lower bound by a multiplicative factor of
√
𝐾/log𝐾 com-
pared to the standard MAB setting. This indicates that maintaining
low regret is fundamentally more challenging for any online al-
gorithm under this property. However, as we will show, the other
two properties can help mitigate this difficulty through appropriate
algorithmic design.
Remark3.Our mathematical formulation is related to the time-
varying cost of AoI optimization studied in [34] (specifically, the
single-sourcing case with bandit feedback, which is shown in the
long version at arXiv [ 33]). The authors consider the adversary
cost setting and apply the standard EXP3 algorithm. We note that
directly applying their result to our setting will incur a regret of
˜𝑂(𝐾 √ 𝑇) , which is consistent with our finding in Proposition 3; see
more discussion in Appendix B. We will show an improved regret
by exploring the problem structures next.
5 Algorithm and Regret Analysis
In this section, we introduce an online algorithm,BCAE, that lever-
ages the structures of the timing bandit. We establish thatBCAE
achieves a regret of ˜𝑂( √ 𝑇) . Additionally, we present a matching
regret lower bound of Ω(
√
𝑇) . We further propose an Optimism-
Enhanced variant,OE-BCAE, that integrates lower confidence bound
principles to improve empirical adaptivity while preserving the
same regret order.

MobiHoc ’26, November 23-26, 2026, Tokyo, Japan Lin et al.
5.1 Our Proposed Algorithm:BCAE
Our algorithm, namely Balanced Consecutive Arm Elimination
(BCAE), integrates the arm elimination strategy from the standard
stochastic MAB literature (see e.g., a book of MAB [ 28]) while
exploring the special structures of the timing bandit. Specifically,
our algorithm introduces a tighter confidence bound by the arm cost
composition and a balanced consecutive feedback idea to efficiently
explore the consecutive feedback and the tighter confidence bound.
We provide a pseudocode of the algorithm in Algorithm 1.
In ourBCAEalgorithm, we maintain a set A of candidate arms
that includes the optimal arm𝑘∗ with high probability. After making
the last update, we check our cost estimation of the arms in the
candidate setA. If the cost of an arm is far away from the optimal
one we observed so far, we eliminate such an arm fromA. We note
that we use𝑛𝑘(𝑡) to denote the number of times arm 𝑘 is pulled
before slot𝑡. We use𝑚𝑘(𝑡) to denote the number of samples for arm
𝑘 before slot𝑡. For ease of the presentation, we simplify them to be
𝑛𝑘 and𝑚𝑘 in Algorithm 1, which represent the latest value of𝑛𝑘(𝑡)
and𝑚𝑘(𝑡) . Similarly, we use ¯𝜇𝑘 to denote the latest estimation of
𝜇𝑘. Our algorithm introduces the following new designs.
Tighter Confidence Bound.Following the arm cost composi-
tion property in Sec. 4.2, with𝑚𝑘(𝑡) samples of𝜇𝑘 (each including
samples of𝑔(𝑎),∀𝑎∈[𝑘] ), ¯𝜇𝑘 becomes that average of 𝑘·𝑚 𝑖(𝑡)
bounded, independent random variables. According to Hoeffding
Inequality, it allows us to derive a tighter confidence bound for the
estimation of𝜇𝑘, i.e.,|𝜇𝑘− ¯𝜇𝑘|≤
√︂
𝑀2 log( √ 𝐾𝑇)
𝑘·𝑚𝑘 with high probabil-
ity, compared with the standard bound (which replaces𝑘·𝑚 𝑘 by
𝑚𝑘). We formalize it in Lemma 4 in the regret analysis. It leads to a
refined condition for arm elimination, Line 26 in Algorithm 1.
Balanced Confidence Gaps with Consecutive Feedback.To
explore the consecutive feedback, existing literature, e.g., [5, 21, 38],
proposed the idea to pull the arm with the maximum index in the
candidate setA, thereby efficiently collecting samples for all arms
inA with a single pull. While it seems natural to combine this
maximum-index-pulling idea with the tighter confidence bounds,
this direct combination is insufficient to significantly reduce regret.
This is because in arm elimination, the elimination condition (see
Line 26 in Algorithm 1) relies on shrinking both confidence bounds
of the compared arm pairs. The maximum-index-pulling method
only ensures the same number of samples,𝑚𝑖,∀𝑖∈A . The arms
with smaller indices have looser confidence bounds, compared with
larger ones (due to the 𝑖·𝑚 𝑖 term in the denominator), and will
dominate the number of samples needed to shrink the confidence
bounds to a certain level, leading to a limited utilization of the
tighter confidence bound.
Instead, we introduce the idea of strategically balancing the con-
fidence gaps,
√︃
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚𝑖 , for all arms, while efficiently utilizing
the consecutive feedback. We provide an illustration in Fig. 3. We
introduce the concept of super-round, which includes a number of
consecutive arm pullings. It corresponds to the period of running
Line 10 to Line 29 for one iteration. Our design is to balance the
confidence gaps of all arms at the end of each super-round, i.e.,
ensuring that𝑖·𝑚 𝑖,∀𝑖∈A are close to each other. Specifically, at a
super-round, we identify arms with index2 ˆ𝑗− ˜𝑗,∀ ˜𝑗∈{ 0, 1,··· ˆ𝑗− 1},
where ˆ𝑗=⌈log 2 ˆ𝑘⌉ and ˆ𝑘 is the maximum index inA. We call these
Values of          after each pull:
Arm
1 2 13 4 5 6 7 8
2 4 16 8
3 6
4 8
Arm 8 → Arm 4 → Arm 2 → Arm 2

Arm pulls in a super round:
5 6 7 8
16 8 5 6 7 8
5 6 7 816 8
Figure 3: An illustrative example ofBCAEin a super-round.
Suppose there are 8 arms. Then, the anchor arms are {2, 4, 8}.
Each square shape represents an observed sample; e.g.,
pulling arm 8, we have samples from all arms. The num-
bers represent the values of 𝑖·𝑚 𝑖 of the arms after each pull.
We see that at the end of the super-round, the values of 𝑖·𝑚 𝑖
are within a factor of two of each other, which leads to a
balanced confidence interval among all the arms.
arms anchors. For each anchor arm2 ˆ𝑗− ˜𝑗, ˜𝑗∈{ 0, 1,··· ˆ𝑗− 1}, we
pull it ˆ𝑧= 2 ˜𝑗− 2 ˜𝑗−1 times (or one time when ˜𝑗= 0). In case the
anchor arm has been eliminated, we delegate the updates to the
closest arm to it from the left, ˜𝑖:=max 𝑖{𝑖∈A|𝑖≤2 ˆ𝑗− ˜𝑗}.
For illustrative purposes, we assume that all anchor arms remain
inA. For each anchor arm2 ˆ𝑗− ˜𝑗 , we obtain1+˝ ˜𝑗 𝑗=1(2𝑗− 2𝑗−1)= 2 ˜𝑗
samples, either by pulling it or anchor arms with larger index
(exploring the consecutive feedback). It ensures the increment of
𝑖·𝑚 𝑖 for all anchor arms 𝑖 are similar, i.e.,2 ˆ𝑗− ˜𝑗· 2 ˜𝑗 = 2 ˆ𝑗≃ ˆ𝑘,∀ ˜𝑗.
For each other arm, it obtains the same number of samples in the
super-round as the anchor arm with the smallest index greater than
its own, due to the consecutive feedback structure. And as its index
is at least half of such an anchor arm, its increment in𝑖·𝑚 𝑖 is also
at least half of such an anchor arm. We provide a formal statement
of this property in Lemma 5 within our regret analysis.
For the rest of the algorithm, after each arm pull, we update
our estimates for arms with indices smaller than ˜𝑖. We count the
number of times the arm is pulled,𝑛 ˜𝑖, and the number of samples
we obtained for the arms, 𝑚𝑖,∀𝑖≤ ˜𝑖and𝑖∈ A . We apply the
arm elimination condition to eliminate non-optimal arms. These
correspond to Line 16 to Line 27 in Algorithm 1. We repeat the
process until the end of the horizon𝑇.
5.2 Regret Analysis
Here, we illustrate the key properties of our proposedBCAEal-
gorithm. We provide a theoretical analysis of its performance on
regret minimization. Furthermore, we establish a corresponding
regret lower bound for theUSPproblem, demonstrating the near-
optimality of our approach.
We first formally describe the tighter confidence bound we ap-
plied in our algorithmBCAEand the balanced confidence gaps
guaranteed by our designs in the algorithm.
Lemma 4 (Tighter Confidence Bound).
P'›
«
| ¯𝜇𝑘(𝑡)−𝜇 𝑘|≥
√︄
𝑀2 log( √ 𝐾𝑇)
𝑘·𝑚 𝑘(𝑡)
“ﬁ
‹
≤2·𝐾 −1𝑇−2.(11)

Learning When to Update: A Near-Optimal Timing Bandit Approach MobiHoc ’26, November 23-26, 2026, Tokyo, Japan
Algorithm 1: Balanced Consecutive Arm Elimination(BCAE)
1:Keep the model for𝐾slots, receive degradation cost𝑔 𝑡(𝑎𝑡)
with𝑎𝑡 =𝑡 ,∀𝑡∈[𝐾] . Perform an update at the end of slot𝐾.
2:Initialize ¯𝜇𝑘 = 1 𝑘

𝐶(𝑘)+ ˝𝑘 𝑖=1𝑔𝑖(𝑖)  .
3:InitializeA={1,2,···,𝐾}.
4:𝑡=𝐾and𝑚 𝑘 =1,∀𝑘∈[𝐾].
5:𝑗 ∗ =arg min𝑖∈A ¯𝜇𝑖+
√︃
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚𝑖 .
6:for𝑖∈Ado
7:If ¯𝜇𝑖−
√︃
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚𝑖 > ¯𝜇𝑗∗+
√︂
𝑀2 log( √ 𝐾𝑇)
𝑗∗·𝑚𝑗∗ ,A=A−{𝑖}.
8:end for
9:while𝑡<𝑇do
10:Let ˆ𝑘=max 𝑘{𝑘∈A}, and ˆ𝑗=⌈log 2 ˆ𝑘⌉.
11:If ˆ𝑗=0, Update the model at the end of the slot;𝑡=𝑡+1;
Continuous.
12:for ˜𝑗=0 : 1 : ˆ𝑗−1do
13:Let ˜𝑖=max 𝑖{𝑖∈A|𝑖≤2 ˆ𝑗− ˜𝑗}. If no such ˜𝑖, BREAK.
14:Let ˆ𝑧=1if ˜𝑗=0; otherwise, ˆ𝑧=2 ˜𝑗−2 ˜𝑗−1 .
15:for𝑧=1 : 1 : ˆ𝑧do
16:Let ˜𝑖=max 𝑖{𝑖∈A|𝑖≤2 ˆ𝑗− ˜𝑗}. If no such ˜𝑖, BREAK.
17:If𝑡+ ˜𝑖>𝑇, Keep the model till𝑇and EXIT.
18:Pull arm ˜𝑖, i.e., Keep the model for ˜𝑖slots, observe
𝑔𝑡+1(1),𝑔𝑡+2(2)···𝑔 𝑡+ ˜𝑖(˜𝑖), and update the model.
19:Update𝑡=𝑡+ ˜𝑖; Update𝑛 ˜𝑖 =𝑛 ˜𝑖+1.
20:for𝑖∈Aand𝑖≤ ˜𝑖do
21:Obtain a sample of𝜇 𝑖, i.e., let
ˆ𝜇𝑖 = 1 𝑖 𝐶(𝑖)+ ˝𝑖 𝑘=1𝑔𝑡+𝑘(𝑘);
22:Update ¯𝜇𝑖 = 𝑚𝑖· ¯𝜇𝑖+ ˆ𝜇𝑖 𝑚𝑖+1 ; Update𝑚𝑖 =𝑚𝑖+1.
23:end for
24:𝑗 ∗ =arg min𝑖∈A ¯𝜇𝑖+
√︃
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚𝑖 .
25:for𝑖∈Ado
26:If ¯𝜇𝑖−
√︃
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚𝑖 > ¯𝜇𝑗∗+
√︂
𝑀2 log( √ 𝐾𝑇)
𝑗∗·𝑚𝑗∗ ,
A=A−{𝑖}.
27:end for
28:end for
29:end for
30:end while
The details of the proof are in Appendix D. The proof is based on
the Hoeffding Inequality [17] and the specific arm-cost composition
of our problem. In analysis of the standard MAB, e.g., [ 19], the
confidence gap, usually defined as
√︂
𝑀2 log( √ 𝐾𝑇)
𝑚𝑘(𝑡) , shrinks with the
number of samples𝑚𝑘(𝑡) . Our result introduces a tighter confidence
bound, which shrinks faster in the arm index.
We denote𝑡𝑠 as the beginning slot of the𝑠-th super-round.
Lemma 5.After the previous super-round, we have that
𝑖·𝑚 𝑖(𝑡𝑠)
𝑗·𝑚 𝑗(𝑡𝑠)≤2,∀𝑖,𝑗∈A(𝑡 𝑠).(12)
The lemma implies that, for all arms inA(𝑡𝑠), their confidence
gaps,
√︂
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚𝑖(𝑡𝑠) ,∀𝑖∈A , are tightly clustered, differing by no
more than a multiplicative factor of
√
2. The lemma is due to our
dedicated algorithmic design for balancing confidence gaps, which
ensures that the increments of𝑖·𝑚 𝑖 in each super-round are close
for all arms in the candidate set. The details of the proof are in
Appendix E.
Suppose that the optimal arm is with index𝑘∗, and we denote
the difference between the expected cost of arm𝑘 and arm𝑘∗ as
Δ𝑘 =𝜇 𝑘−𝜇𝑘∗. We consider a clean eventE:
E≜
 
 | ¯𝜇𝑘(𝑡)−𝜇 𝑘|≤
√︄
𝑀2 log( √ 𝐾𝑇)
𝑘·𝑚 𝑘(𝑡) ,∀𝑡∈[𝑇],𝑘∈[𝐾]
 
 ,(13)
We can show that eventE happens with high probability based
on Lemma 4 and the union bound. It would be sufficient to show
that our algorithm can obtain the desired regret bound under the
clean event. We note that under eventE, the optimal arm𝑘∗ will
always be inA, by observing that the condition in the algorithm
BCAEto eliminate an arm fromAwill never hold for arm𝑘 ∗.
We show that, under the clean eventE, algorithmBCAEonly
requires a bounded number of samples to eliminate an arm𝑖 with
optimality gapΔ𝑖.
Lemma 6.We have𝑚 𝑖(𝑇)≤ 36𝑀2 log( √ 𝐾𝑇) 𝑖·Δ 2 𝑖 +2·𝐾,∀𝑖≠𝑘 ∗.
The details of the proof are in Appendix F. Unlike the standard
bound, ours scales inversely with the arm index 𝑖 as well as Δ2 𝑖 ,
thanks to the tighter confidence bound (Lemma 4) and the balanced
confidence gaps (Lemma 5). The idea of the proof is that after the
required number of samples has been collected, our balancing idea
ensures that the confidence bounds for the suboptimal arm𝑖 and
the optimal arm𝑘∗ become sufficiently and consistently narrow,
which triggers the elimination condition once the optimality gap
Δ𝑖 can be reliably distinguished.
Our algorithm will pull arms with a smaller index to ensure bal-
anced confidence gaps. Such behavior deviates from the maximum-
index-pulling idea in the literature [5, 21, 38] and may not optimally
utilize the consecutive feedback structure. For example, under the
maximum-index-pulling idea, arms whose index values fall below
that of the optimal arm are almost unlikely to be pulled since the
optimal arm remains in the candidate set with high probability
and will dominate the index comparison. As a comparison, our
algorithm sometimes pulls these arms. Nevertheless, our novelty
in the analysis is that we show that our algorithm is able to uti-
lize the consecutive feedback efficiently (incurring a low regret)
in each subset of a partition of the total 𝐾 arms. Specifically, the
partition, induced by the anchor arms, consists of⌈log2𝐾⌉ subsets,
which is denoted as {K𝑗|𝑗∈ ⌈log 2𝐾⌉} , whereK1 ={ 1, 2} and
K𝑗 ={ 2𝑗−1+ 1,···,min{𝐾, 2𝑗}}, for 𝑗∈ {2,···,⌈log 2𝐾⌉} . We
obtain the following upper bound on the regret incurred by pulling
the arms in each subset.
Lemma 7.We have that, for any𝑗∈{1,···,⌈log 2𝐾⌉},
∑︁
𝑖∈K𝑗
𝑖·𝑛 𝑖(𝑇)·Δ 𝑖≤
√︃
36𝑇𝑀 2 log( √ 𝐾𝑇)·𝐿 1+2𝐾 2( ¯𝐶+𝑀),(14)
where𝐿 1 ≜

2+log 2𝐾( ¯𝐶+𝑀) √ 𝑇√
36𝑀2 log( √ 𝐾𝑇)

and ¯𝐶≜max 𝑘𝐶(𝑘).

MobiHoc ’26, November 23-26, 2026, Tokyo, Japan Lin et al.
The details of the proof are in Appendix G. Essentially, the lemma
implies that the regret incurred by pulling suboptimal arms in each
subsetK𝑗 is bounded by ˜𝑂( √ 𝑇) . Together with the fact that the
number of subsets in our partition is bounded bylog2𝐾+ 1, we can
conclude the regret upper bound of our algorithm, which will be
shown in Theorem 8.
The lemma is based on the tighter bounds on the required number
of samples shown in Lemma 6. We further show that in each subset,
an arm will not be pulled before all arms with larger indices (in the
subset) are eliminated. It ensures the following inequality under
the clean eventE,∀𝑘∈K 𝑗 ,
𝑛𝑘(𝑇)=0or ˝min{𝐾,2𝑗} 𝑖=𝑘 𝑛𝑖(𝑇)≤ 36𝑀2 log( √ 𝐾𝑇) 𝑘·Δ 2 𝑘 +2𝐾.(15)
That is, either that an arm𝑘 will never be pulled (it is eliminated
due to sufficient samples from pulling arms with larger indices) or
that its sample bound provides an upper bound to the total number
of pulls of all arms with no smaller indices (in the subset). The
bound is tighter than the one in the standard MAB, where the
number of pulls of each arm is bounded by its required sample
size individually. The proof of the lemma is based on solving the
optimization problem of maximizing the incurred regret subject to
the constraints on the number of pulls of the arms (including (15)).
We now show the regret guarantee of our proposed algorithm
in the following theorem, which is obtained by summing up the
regret incurred by all the⌈log 2𝐾⌉subsets and Lemma 7.
Theorem 8.The regret of ourBCAEalgorithm is upper bounded
by
√︃
36𝑇𝑀 2 log( √ 𝐾𝑇)·(log 2𝐾+ 1)·𝐿 1+ 2𝐾2(log2𝐾+ 1)( ¯𝐶+𝑀),
where𝐿 1 and ¯𝐶are as those defined in Lemma 7.
Theorem 8 shows that ourBCAEalgorithm achieves a sublinear
regret upper bound of ˜𝑂( √ 𝑇) for sufficiently large𝑇 . Here, the ˜𝑂 no-
tation suppresses logarithmic factors. We note that sublinear regret
implies that the long-term average cost of our proposed algorithm
converges to the same value as the optimal solution. Our approach
could effectively learn to make optimal update decisions. In addi-
tion, it improves over simply applying standard MAB algorithms
(achieving ˜𝑂(𝐾 √ 𝑇) , Proposition 3). Finally, with the lower bound
identified in the following Proposition 9, our algorithm achieves a
regret bound close to the lower bound by up to logarithmic factors.
Proposition 9.The regret for any online algorithm forUSPis
lower bounded byΩ(
√
𝑇).
We prove the lower bound following the proof of the lower bound
for stochastic multi-armed bandit with two arms; see Theorem 2.10
with𝐾= 2in [ 28] for an illustration. We construct two instances
ofUSP, where 𝑔1 follows a Bernoulli distribution with mean1/4,
𝐶( 1)=𝐶( 2)= 1/4, and𝑔2 follows a Bernoulli distribution with
mean1/2−𝜖 in the first instance and with mean1 /2+𝜖 in the
second case. Under both instances, we can check that playing a
suboptimal arm will incur a loss of1/2·𝜖 per round. Following the
information-theoretic argument in [28], it requires Ω(1/𝜖2) rounds
to determine the optimal arms in both instances. It will incur a
regret of Ω(𝜖·min{ 1/𝜖2,𝑇}) , which by tuning𝜖=Θ( 1/ √ 𝑇) , leads
to a regret lower bound ofΩ(
√
𝑇).
5.3 Optimism-Enhanced Balanced Consecutive
Arm Elimination (OE-BCAE)
Our proposedBCAEalgorithm follows the arm elimination par-
adigm. It permanently discards an arm only when there is high
confidence that the arm is suboptimal. Because mistaken elimina-
tion is irrecoverable, the criterion is necessarily conservative, so the
algorithm adapts only at infrequent elimination events. In contrast,
the Lower Confidence Bound (LCB) paradigm reselects the arm
with the smallest LCB every round, making it more responsive to
incoming feedback. Such a behavior of arm elimination may not be
preferable from an empirical evaluation perspective, as observed
in the literature, e.g., [ 5, 38]. In this section, we incorporate the
optimism idea in the lower confidence bound paradigm and pro-
pose Optimism-Enhanced Balanced Consecutive Arm Elimination
(OE-BCAE). We show thatOE-BCAEmaintains the near-optimal
regret bound. We will discuss numerical performance in Sec. 6.2
OurOE-BCAEalgorithm makes the following modification to
BCAE. At Step 16 of Algorithm 1, instead of simply pulling the arm
with the maximum index no larger than2 ˆ𝑗− ˜𝑗 , we apply the lower
confidence bound algorithm in a forward window from the arm.
More specifically, for each ˜𝑖, we consider the forward window,
W˜𝑖 ≜{ ˜𝑖}∪ (A∩[𝑙+1,𝑙+𝑤]∩[𝑙,2·𝑙] ),(16)
where𝑙≜ 2⌈log2 ˜𝑖⌉ and𝑤 is an upper bound on the window size
that can be designed. And, we pull the arm
ˆ𝑖=arg min 𝑖∈W ˜𝑖 ¯𝜇𝑖−
√︄
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚 𝑖
.(17)
The use of the forward window (ˆ𝑖 is no smaller than ˜𝑖) allows us
to efficiently utilize consecutive feedback, similar to pulling ˜𝑖: we
receive all the feedback from arm one to arm ˜𝑖 at once. Restricting
the arm indexes in the window to2 ·𝑙 can keep the confidence
bounds among arms balanced. These two maintain the two prop-
erties ofBCAEthat are important for achieving the near-optimal
regret guarantee. Further, by limiting the number of arms in the for-
ward window,𝑤, we can limit the additional regret or risk incurred
compared with directly pulling arm ˜𝑖. All together, these allow us to
show thatOE-BCAEalso achieves the near-optimal regret ˜𝑂( √ 𝑇) .
Theorem 10.The regret of ourOE-BCAEalgorithm is upper
bounded by ˜𝑂( √ 𝑇)when𝑤is a constant or𝑂(log𝐾).
The details of the proof are in Appendix I. Our idea to prove the
theorem is twofold. First, we decompose the regret into two parts,
where the first part is induced as if we play ˜𝑖, and the second part
is the additional regret from actually pulling ˆ𝑖 according to (17).
Second, we show the first part incurs a regret bounded by ˜𝑂( √ 𝑇)
following a similar analysis as that of theBCAEalgorithm, and the
second part functions analogously to LCB with a constant number
of arms, contributes an additional regret term bounded by ˜𝑂( √ 𝑇).
6 Simulation Results
In this section, we evaluate the performance of our proposed online
learning algorithms through numerical simulations. Our evaluation
2A direct LCB-based design remains open (seeSA-LCBin Sec. 6), as it is unclear how
LCB variants can efficiently utilize the consecutive feedback structure; see e.g. [5, 38].

Learning When to Update: A Near-Optimal Timing Bandit Approach MobiHoc ’26, November 23-26, 2026, Tokyo, Japan
0.0 0.2 0.4 0.6 0.8 1.0
Time horizon 1e6
0.0
0.2
0.4
0.6
0.8
1.0
Average cumulative regret
×107
LCB
ELMI
SA-LCB
BCAE
OE-BCAE
(a) Performance across the horizon𝑇
100 200 300 400 500 600 700
Maximum interval K
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
Average final regret
×107
LCB
ELMI
SA-LCB
BCAE
OE-BCAE (b) Performance under different𝐾
20 40 60 80 100 120
Base update cost C0
0.0
0.2
0.4
0.6
0.8
1.0
Average final regret
×107
LCB
ELMI
SA-LCB
BCAE
OE-BCAE (c) Performance under different𝐶 0
Figure 4: The performance of comparing algorithms under different parameters.
aims to demonstrate the efficiency of our proposed algorithms
and compare them with the alternatives. An additional empirical
evaluation on a remote monitoring instance using real-world traces
is provided in Sec. 7.
6.1 Simulation Setup
Baselines for Comparison:We compare our proposed algorithms
against the following baselines:
•LCB:The standard Lower Confidence Bound algorithm.
• ELMI, e.g., [5, 21, 38]: An arm-elimination variant that al-
ways pulls the maximum-index arm in the candidate set.
• SA-LCB, Structure-Aware LCB: An LCB variant we adapt re-
garding the problem structures, i.e., replacing the confidence
bound used in LCB with the one we develop in Lemma 4.
• BCAE:Our proposed Balanced Consecutive Arm Elimination
algorithm in Algorithm 1.
• OE-BCAE:Our Optimism-Enhanced variant, which inte-
grates LCB principles intoBCAE, discussed in Sec. 5.3.
Environment and Cost Models:We simulate a dynamic sys-
tem where an operator maintains a deployed model over a time
horizon𝑇 . The decision space consists of 𝐾 candidate update in-
tervals (arms). The expected degradation cost is modeled as an in-
creasing function of the model age𝑎, specifically ˜𝑔(𝑎)= 50·(𝑎/𝐾) 2.
The realized degradation cost at slot𝑡 is sampled from a truncated
normal distribution with mean ˜𝑔(𝑎𝑡) and a random standard devia-
tion𝜎=𝛼· ˜𝑔(𝑎) where𝛼 is chosen as0.2. The deterministic system
update cost is set to be𝐶(𝑎)=𝐶 0+ 50
√︁
𝑎/𝐾. The sublinear square
root function captures diminishing marginal overhead for updating.
We set the degradation and update costs to be parameterized by
the normalized age𝑎/𝐾. It ensures that increasing𝐾 increases the
number of available arms without proportionally enlarging the
cost range, capturing a setting with more candidate intervals but
comparable cost scale.
By default, we set the time horizon to𝑇= 106 slots, the maximum
candidate interval to 𝐾= 100, and the base update cost 𝐶0 = 20.
Results are averaged over 30 independent simulation runs to ensure
statistical confidence.
6.2 Results and Discussion
Fig. 4a illustrates the cumulative regret of the evaluated algorithms
under the default settings. In Fig. 4b, we demonstrate the regret of
Table 2: Average regret ofOE-BCAEversus the autocorrela-
tion coefficient𝜌.
𝜌0 0.3 0.5 0.7 0.9
OE-BCAE(×10 5) 8.62 8.63 8.62 8.62 8.62
the algorithms under different maximum intervals𝐾. Fig. 4c shows
the regret of the algorithms under different base update costs𝐶 0.
The results show thatBCAEandOE-BCAEclearly improve over
LCBandELMI, which do not or only partially exploit the favorable
problem structures, and remain robust across varying maximum
intervals and base update costs, highlighting their scalability and
adaptability. Compared withSA-LCB, a baseline we adapt from
the standard LCB by incorporating the problem structures,SA-
LCBachieves the lowest regret when the number of arms is small,
whereas our algorithms, particularlyOE-BCAE, are superior in
larger search spaces. AlthoughSA-LCB’s competitive performance
underscores the value of the structural insights in this paper, its
theoretical regret analysis remains an open challenge.
The plots also highlight the empirical advantage ofOE-BCAE
overBCAE: by integrating LCB-style optimism,OE-BCAEavoids
the delayed adaptation inherent to pure elimination paradigms,
resulting in a lower-regret curve.
Robustness to temporal correlation.We relax the independence
assumption (Remark 1) by making the degradation noise AR(1):
𝑔𝑡(𝑎𝑡)=max( 0, ˜𝑔(𝑎𝑡)+𝜎(𝑎 𝑡)𝑧𝑡) with 𝑧𝑡 =𝜌𝑧 𝑡−1+
√︁
1−𝜌 2𝜂𝑡
(𝜂𝑡 i.i.d. standard normal), leaving the per-age mean and variance
unchanged, so𝜌= 0recovers the i.i.d. model. Table 2 showsOE-
BCAE’s mean regret is flat across𝜌∈{ 0,..., 0.9}. Other baselines
behave likewise, but details are omitted due to space limit. Intu-
itively, correlation inflates the variance of the estimates without
shifting their means, while the confidence bounds of Lemma 4 are
variance-free and far larger than the estimation noise. Hence, the
arm-selection decisions and the mean regret barely change. We
note that under correlation, the realized degradation predicts fu-
ture degradation, so an optimal policy should adapt to the realized
degradation. Designing such policies is left to future work.

MobiHoc ’26, November 23-26, 2026, Tokyo, Japan Lin et al.
0.0 0.2 0.4 0.6 0.8 1.0
Time horizon ×106
0
2
4
6
8
Cumulative regret
×103
LCB
ELMI
SA-LCB
BCAE
OE-BCAE
(a) Performance across the horizon𝑇
100 200 300 400 500 600 700 800 900
Maximum interval K
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Final regret
×104
LCB
ELMI
SA-LCB
BCAE
OE-BCAE (b) Performance under different𝐾
0.005 0.01 0.015 0.02 0.025
Constant update cost C
2
4
6
8
Final regret
×103
LCB
ELMI
SA-LCB
BCAE
OE-BCAE (c) Performance under different𝐶
Figure 5: Empirical Evaluation on Real Frequency Trace.
OE-BCAE SA-LCB
Periodic (0.2K)Periodic (0.5K)Periodic (0.8K)
0.0
0.2
0.4
0.6
0.8
1.0
1.2
T otal cost
×104
Figure 6: Total-cost comparison ofOE-BCAE,SA-LCB, and
periodic baselines on the real frequency trace.
7 Empirical Evaluation
In this section, we evaluate the performance of our proposed on-
line learning algorithms through an empirical study on a remote
monitoring problem using real-world traces.
7.1 Simulation Setup
We consider a remote monitoring problem in which a monitor
maintains a cached view of an evolving physical process. The re-
mote source decides when to refresh that view under a constant
update cost. As the underlying process, we use the public historical
frequency dataset released by Fingrid for the Nordic synchronous
power system, 3 which records frequency measurements from sub-
stations at multiple locations in Finland. We regularize the mea-
surements onto a 1-second grid. Letting𝑦𝑡 denote the regularized
frequency value, we define the degradation cost of using a sample
of age𝜏 at time𝑡+𝜏 as|𝑦𝑡+𝜏−𝑦𝑡|, which captures the monitoring
error induced by outdated information. We then compare with the
algorithms listed in Sec. 6.1 and heuristic periodic algorithms on
chronological traces under a constant-cost update model. Our main
results use horizon𝑇= 106, maximum update interval 𝐾= 100,
and update cost 𝐶= 0.01, and we further report sensitivity to
𝐾∈{ 100, 300, 500, 700, 900} and𝐶∈{ 0.005, 0.01, 0.015, 0.02, 0.025}.
We choose the update cost to be comparable in magnitude to the
degradation cost, so that the objective reflects a genuine trade-off
3https://data.fingrid.fi/en/datasets/339.
between communication overhead and information staleness across
the range of update intervals. Regret is measured relative to the
empirically optimal static update interval computed on the realized
trace. We demonstrate the results in Fig. 5 and Fig. 6.
7.2 Results and Discussion
The regret results in Fig. 5 on the real frequency trace are broadly
consistent with the trends observed in the numerical evaluation
in Sec. 6. First, our structure-aware methodsBCAEandOE-BCAE,
as well asSA-LCB, substantially outperform the unstructured or
only partially structured baselinesLCBandELMI. This provides
further empirical evidence that exploiting problem structure is criti-
cal for achieving low regret. Second, when compared withSA-LCB,
we find thatOE-BCAEbecomes increasingly competitive as the
search space grows, and eventually overtakesSA-LCBin the larger-
𝐾 regime considered here. Third,OE-BCAEconsistently improves
uponBCAE, indicating that the addition of LCB-style optimism
helps the elimination-based strategy adapt more effectively in prac-
tice.
Fig. 6 compares the total cost of our adaptive methods with
heuristic periodic baselines under the default setting 𝐾= 100,
𝐶= 0.01, and𝑇= 106. We set the update interval for the periodic
baselines as0 .2, 0.5, 0.8of 𝐾 respectively. Both adaptive policies,
SA-LCBand ourOE-BCAE, outperform all three tested periodic
rules by a clear margin. Specifically, ourOE-BCAEachieves at least
13% reduction in total cost compared to heuristic periodic baselines.
This indicates that when there is no prior knowledge about the
degradation cost, setting a fixed update schedule heuristically may
not be efficient. Instead, adaptive policies that exploit problem
structures can efficiently adjust their decisions online based on
observed costs and gain an empirical advantage in this setting.
Finally, we note that our empirical evaluation using real-world
traces demonstrates that, while our designs rely on the assumptions
that the degradation costs are i.i.d. given age and independent
across ages, they remain effective in practical scenarios where these
assumptions may not hold perfectly.
8 Conclusion
In this paper, we study the problem of jointly optimizing degrada-
tion costs and update expenses by strategically timing the updates,
without prior information on the distribution of the degradation

Learning When to Update: A Near-Optimal Timing Bandit Approach MobiHoc ’26, November 23-26, 2026, Tokyo, Japan
cost. We have formulated this problem as a novel timing multi-
armed bandit problem. We identify the challenges of the problem
by providing the lower bound of an ablated timing bandit problem.
We then explore the problem-specific structures of timing feed-
back and develop two efficient online algorithms with sublinear,
near-optimal regret for it. Our online algorithms derive an update
strategy that achieves the sublinear regret bounds relative to the
optimal policy with complete knowledge of the degradation cost
distribution. As for future work, it would be interesting to general-
ize our approach under less restrictive assumptions. For example,
we may incorporate techniques from rising bandits [24] to model
scenarios where the degradation costs at a given age decrease in
time due to technological advancements. More generally, we may
adapt techniques from non-stationary bandits, e.g., [4], to handle
environments without the i.i.d. assumption. Another interesting
direction is to apply our algorithm and ideas to broader scenarios,
including the age-of-information optimization in communication
networks, product age optimization in business, etc.
Acknowledgments
This work is supported in part by a General Research Fund from Re-
search Grants Council, Hong Kong (Project No. 11200223), a Collab-
orative Research Fund from Research Grants Council, Hong Kong
(Project No. C1049-24G), and a Start-up Research Grant from The
Chinese University of Hong Kong, Shenzhen (Project No. UDF01004086).
The authors would also like to thank the anonymous reviewers for
their helpful comments.
References
[1] Ahmed Arafa, Jing Yang, Sennur Ulukus, and H Vincent Poor. 2019. Age-minimal
transmission for energy harvesting sensors with finite batteries: Online policies.
IEEE Transactions on Information Theory66, 1 (2019), 534–556.
[2] Peter Auer, Nicolo Cesa-Bianchi, Yoav Freund, and Robert E Schapire. 2002. The
nonstochastic multiarmed bandit problem.SIAM journal on computing32, 1
(2002), 48–77.
[3] Baran Tan Bacinoglu, Yin Sun, Elif Uysal, and Volkan Mutlu. 2019. Optimal status
updating with a finite-battery energy harvesting source.Journal of Communica-
tions and Networks21, 3 (2019), 280–294.
[4] Omar Besbes, Yonatan Gur, and Assaf Zeevi. 2014. Stochastic multi-armed-bandit
problem with non-stationary rewards.Advances in neural information processing
systems27 (2014).
[5] Swapna Buccapatnam, Fang Liu, Atilla Eryilmaz, and Ness B. Shroff. 2018. Reward
Maximization Under Uncertainty: Leveraging Side-Observations on Networks.
Journal of Machine Learning Research18, 216 (2018), 1–34.
[6] Shengyu Cao, Simai He, Ruoqing Jiang, Jin Xu, and Hongsong Yuan. 2023. Best
Arm Identification in Batched Multi-armed Bandit Problems. arXiv:2312.13875
[7] Stéphane Caron, Branislav Kveton, Marc Lelarge, and Smriti Bhagat. 2012. Lever-
aging side observations in stochastic bandits.arXiv:1210.4839(2012).
[8] Semih Cayci, Atilla Eryilmaz, and R. Srikant. 2019. Learning to Control Renewal
Processes with Bandit Feedback.Proc. ACM Meas. Anal. Comput. Syst.3, 2, Article
43 (June 2019), 32 pages. https://doi.org/10.1145/3341617.3326158
[9] Sirin Chakraborty and Yin Sun. 2025. Send Pilot or Data? Leveraging Age of Chan-
nel State Information for Throughput Maximization. arXiv:2503.13866 [eess.SP]
[10] Wei Chen, Wei Hu, Fu Li, Jian Li, Yu Liu, and Pinyan Lu. 2016. Combinatorial
Multi-Armed Bandit with General Reward Functions. InAdvances in Neural
Information Processing Systems, Vol. 29. Curran Associates, Inc.
[11] Wei Chen, Yajun Wang, and Yang Yuan. 2013. Combinatorial Multi-Armed Bandit:
General Framework and Applications. InProceedings of the 30th International
Conference on Machine Learning, Vol. 28. PMLR, Atlanta, Georgia, USA, 151–159.
[12] Wei Chen, Yajun Wang, Yang Yuan, and Qinshi Wang. 2016. Combinatorial
multi-armed bandit and its extension to probabilistically triggered arms.Journal
of Machine Learning Research17, 50 (2016), 1–33.
[13] Santosh Fatale, Kavya Bhandari, Urvidh Narula, Sharayu Moharir, and Manjesh K.
Hanawal. 2022. Regret of Age-of-Information Bandits.IEEE Transactions on
Communications70, 1 (2022), 87–100.
[14] Zijun Gao, Yanjun Han, Zhimei Ren, and Zhengqing Zhou. 2019. Batched Multi-
armed Bandits Problem. InAdvances in Neural Information Processing Systems,
Vol. 32. Curran Associates, Inc.
[15] Michael Grieves and John Vickers. 2016. Digital twin: Mitigating unpredictable,
undesirable emergent behavior in complex systems. InTransdisciplinary perspec-
tives on complex systems: New findings and approaches. Springer, 85–113.
[16] Onésimo Hernández-Lerma and Jean B Lasserre. 1996.Discrete-Time Markov
Control Processes: Basic Optimality Criteria. Springer-Verlag, Chapter 5.
[17] Wassily Hoeffding. 1963. Probability Inequalities for Sums of Bounded Random
Variables.J. Amer. Statist. Assoc.58, 301 (1963), 13–30.
[18] Sanjit Kaul, Roy Yates, and Marco Gruteser. 2012. Real-time status: How often
should one update?. InProceedings IEEE INFOCOM. 2731–2735.
[19] Tor Lattimore and Csaba Szepesvári. 2020.Bandit algorithms. Cambridge Univer-
sity Press.
[20] Hyunsung Lee, Sungwook Yoo, Dongjun Lee, and Jaekwang Kim. 2023. How
Important is Periodic Model update in Recommender System?. InProceedings of
ACM SIGIR(Taipei, Taiwan). 2661–2668.
[21] Fengjiao Li, Yu Sang, Zhongdong Liu, Bin Li, Huasen Wu, and Bo Ji. 2021. Wait-
ing But Not Aging: Optimizing Information Freshness Under the Pull Model.
IEEE/ACM Transactions on Networking29, 1 (2021), 465–478.
[22] Qiulin Lin, Junyan Su, and Minghua Chen. 2025. Optimal Algorithms for Online
Age-of-Information Optimization in Energy Harvesting Systems.IEEE Transac-
tions on Networking33, 6 (2025), 3146–3161.
[23] Jie Lu, Anjin Liu, Fan Dong, Feng Gu, Joao Gama, and Guangquan Zhang. 2018.
Learning under concept drift: A review.IEEE transactions on knowledge and data
engineering31, 12 (2018), 2346–2363.
[24] Alberto Maria Metelli, Francesco Trovò, Matteo Pirola, and Marcello Restelli.
2022. Stochastic Rising Bandits. InProceedings of the 39th International Conference
on Machine Learning, Vol. 162. PMLR, 15421–15457.
[25] Vianney Perchet, Philippe Rigollet, Sylvain Chassang, and Erik Snowberg. 2016.
Batched Bandit Problems.The Annals of Statistics44, 2 (2016), 660–681.
[26] Sheldon M Ross. 2014.Introduction to probability models. Academic press.
[27] Md Kamran Chowdhury Shisher, Yin Sun, and I-Hong Hou. 2024. Timely Com-
munications for Remote Inference.IEEE/ACM Transactions on Networking32, 5
(2024), 3824–3839.
[28] Aleksandrs Slivkins. 2019. Introduction to multi-armed bandits.Foundations and
Trends®in Machine Learning12, 1-2 (2019), 1–286.
[29] Yin Sun, Yury Polyanskiy, and Elif Uysal. 2019. Sampling of the Wiener process
for remote estimation over a channel with random delay.IEEE Transactions on
Information Theory66, 2 (2019), 1118–1135.
[30] Yin Sun, Elif Uysal-Biyikoglu, Roy D Yates, C Emre Koksal, and Ness B Shroff. 2017.
Update or wait: How to keep your data fresh.IEEE Transactions on Information
Theory63, 11 (2017), 7492–7508.
[31] Fei Tao, He Zhang, Ang Liu, and Andrew YC Nee. 2018. Digital twin in industry:
State-of-the-art.IEEE Transactions on industrial informatics15, 4 (2018), 2405–
2415.
[32] Vishrant Tripathi and Eytan Modiano. 2019. A whittle index approach to mini-
mizing functions of age of information. In2019 57th Annual Allerton Conference
on Communication, Control, and Computing (Allerton). IEEE, 1160–1167.
[33] Vishrant Tripathi and Eytan Modiano. 2021. An Online Learning Approach to
Optimizing Time-Varying Costs of AoI. arXiv:2105.13383 [cs.NI]
[34] Vishrant Tripathi and Eytan Modiano. 2021. An Online Learning Approach
to Optimizing Time-Varying Costs of AoI. InProceedings of ACM Mobihoc ’21
(Shanghai, China). 241–250.
[35] Daniel Vela, Andrew Sharp, Richard Zhang, Trang Nguyen, An Hoang, and Oleg S
Pianykh. 2022. Temporal quality degradation in AI models.Scientific Reports12,
1 (2022), 11654.
[36] Shiqiang Wang, Tiffany Tuor, Theodoros Salonidis, Kin K. Leung, Christian
Makaya, Ting He, and Kevin Chan. 2019. Adaptive Federated Learning in Re-
source Constrained Edge Computing Systems.IEEE Journal on Selected Areas in
Communications37, 6 (2019), 1205–1221.
[37] Roy D Yates, Yin Sun, D Richard Brown, Sanjit K Kaul, Eytan Modiano, and
Sennur Ulukus. 2021. Age of information: An introduction and survey.IEEE
Journal on Selected Areas in Communications39, 5 (2021), 1183–1210.
[38] H. Zhao and W. Chen. 2019. Stochastic one-sided full-information bandit. InJoint
European Conference on Machine Learning and Knowledge Discovery in Databases.
Springer International Publishing, Cham, 150–166.
A Proof of Proposition 1
Proof. We first show that the problem can be framed as a
Markov Decision Process (MDP). In such an MDP, it suffices to
consider a stationary, deterministic policy that only depends on
the current age. Second, we show that such a policy reduces to
updating periodically and derive the optimal period.
First, we model the problem as a Markov Decision Process (MDP)
defined by the tuple(S,U,𝑃,𝑐) , 1) State Space,S=A×G , where

MobiHoc ’26, November 23-26, 2026, Tokyo, Japan Lin et al.
A={ 1, 2,...,𝐾} is the finite set of possible ages, andG⊆R ≥0 is
the Borel space of possible degradation costs. A state at time𝑡 is𝑠𝑡 =
(𝐴𝑡,𝐺𝑡); 2) Action Space:U={ 0, 1}, representing "keep" (0) and
"update" (1); 3) Cost Function, the immediate cost is𝑐((𝑎,𝑔),𝑢)=𝑔+
𝐶(𝑎)𝑢 , where𝐶(𝑎)≥ 0is the cost of updating at age𝑎; 4) Transition
Kernel, Let𝑃(·|(𝑎,𝑔),𝑢) denote the probability measure of the next
state(𝐴𝑡+1,𝐺𝑡+1). The age transitions deterministically:𝐴𝑡+1 = 1if
𝑢= 1, and𝐴𝑡+1 =min(𝑎+ 1,𝐾) if𝑢= 0. The next degradation cost
𝐺𝑡+1 is drawn from a probability measure𝐹𝐴𝑡+1(·) which depends
only on the new age𝐴𝑡+1 . Note that we include the degradation cost
into the state to make the cost function deterministic over the state
and the action, which matches the standard MDP in the literature.
Later, we will see that, because the degradation cost depends only
on the current age and is independent of future degradation costs,
it is sufficient to consider optimal policies that only depend on the
age but not the realized degradation cost.
Follwoing [16], we establish the Average Cost Optimality Equa-
tion (ACOE). Let𝐽∗ be the optimal long-run average cost, andℎ(𝑎,𝑔)
be the relative value function [16]. The ACOE is given by:
𝐽∗+ℎ(𝑎,𝑔)(18)
=min
𝑢∈{0,1}

𝑐((𝑎,𝑔),𝑢)+
E[ℎ(𝐴𝑡+1,𝐺𝑡+1)|𝐴 𝑡 =𝑎,𝐺 𝑡 =𝑔,𝑈 𝑡 =𝑢]
 (19)
=min
𝑢∈{0,1}

𝑔+𝐶(𝑎)𝑢+
∫
G
ℎ(𝑎′ 𝑢,𝑔′)𝑑𝐹 𝑎′𝑢(𝑔′)

,(20)
where𝑎′ 0 =min(𝑎+ 1,𝐾) and𝑎′ 1 = 1. The last equation is obtained
by substituting the explicit cost and transition dynamics, noting
that𝐴𝑡+1 only depends on𝑎 and𝑢, and𝐺𝑡=1 only depends on𝐴𝑡+1 .
The optimal action is given by:
𝜋∗(𝑎,𝑔)∈arg min
𝑢∈{0,1}

𝑔+𝐶(𝑎)𝑢+
∫
G
ℎ(𝑎′ 𝑢,𝑔′)𝑑𝐹 𝑎′𝑢(𝑔′)

Notice that the current degradation𝑔 appears as an additive con-
stant independent of the action 𝑢 and we let 𝑄(𝑎,𝑢)=𝐶(𝑎)𝑢+∫
Gℎ(𝑎′ 𝑢,𝑔′)𝑑𝐹 𝑎′𝑢(𝑔′). We have that the optimal action is given by:
𝜋∗(𝑎,𝑔)∈arg min
𝑢∈{0,1}
𝑄(𝑎,𝑢)
Because𝑄(𝑎,𝑢)is strictly a function of𝑎and𝑢, and is completely
independent of 𝑔, the minimizing action 𝑢∗ depends only on 𝑎.
Therefore,𝜋∗(𝑎,𝑔)=𝜋 ∗(𝑎).
We can then focus on stationary, deterministic policy𝜋∗(𝑎) that
maps the current age 𝑎𝑡 ∈{ 1, 2,...,𝐾} to an action 𝑢𝑡 ∈{ 0, 1}.
Under such a policy, the system will always update exactly when
the age reaches some𝑘∈{ 1, 2,...,𝐾} , which can be modeled as a
renewal reward process. By the Elementary Renewal Reward Theo-
rem [26], the long-run expected average cost of a periodic policy
with period𝑘, is almost surely equal to the expected cost of one
cycle divided by the expected length of one cycle, i.e.,
˝𝑘
𝑗=1 ˜𝑔(𝑗)+𝐶(𝑘)
𝑘 .
Then, the optimal average cost is the minimum one over all pos-
sible choices of𝑘. And the optimal period𝑘∗ is the argument that
achieves this minimum. This completes the proof.
□
B Comparison with the Adversarial
Setting [32, 33]
The authors in [34] introduce an epoch-based formulation, where a
strategy fixes one update interval in an epoch and receives feedback
on its cost, and consider the adversarial online setting where the
degradation cost or the penalty on age is chosen adversarially. In
more detail, they show that the EXP3 algorithm achieves a regret of
𝑂(
√︁
𝑇′𝑀′ log𝑀′), where𝑇′ is the number of epochs and𝑀′ is the
length of the epochs (and also the maximum update interval). They
consider that the total cost in an epoch is normalized to be within
[0, 1]. However, when𝑀′ is large, such a normalization implies that
the cost at each slot approaches zero, which may not be practical.
Mapping to our case, the cost in an epoch will be in the order of𝑀′.
Taking it into account, their regret becomes𝑂(𝑀′√︁ 𝑇′𝑀′ log𝑀′).
Noting the total number of slots𝑇=𝑇 ′·𝑀′ and𝐾=𝑀 ′, applying
their result to our case achieves a regret ˜𝑂(𝐾 √ 𝑇).
This is consistent with our finding in Proposition 3 that online
algorithms not exploiting the consecutive feedback structure of
the timing bandit could not achieve an expected regret smaller
than Ω(𝐾
√
𝑇/log𝐾) . As a comparison, our online algorithm that
explores the feedback structure of the timing bandit paradigm
achieves a regret of ˜𝑂( √ 𝑇), as shown in Theorem 8
C Proof of Proposition 3
Proof. We now discuss the proof of Proposition 3. Our proof is
adapted from [2] by further considering that in our case, pulling an
arm𝑘 will take𝑘 slots and𝑘 times of cost to receive one feedback.
We consider the following𝐾+ 1problem instances and we will
show that at least one of them will have a large regret given any
online algorithm. Let 𝜇(𝑖)∈R 𝐾 be the vector of the means of the
arms in the𝑖-th instance,∀𝑖∈{ 0, 1,···𝐾} , and𝜇(𝑖) 𝑗 = 1/2+ 1/2(1−
1 𝑖=𝑗)Δ,∀𝑖,𝑗∈[𝑘] , and 𝜇(0) 𝑗 = 1/2+ 1/2Δ,∀𝑗∈[𝐾] . Here, Δ is a
parameter to be determined later.
We consider that the cost of arm 𝑗 under instance𝑖 follows a
Bernoulli distribution with mean 𝜇(𝑖) 𝑗 . We let E𝑖[·]=E 𝜇𝑖[·]. We
define𝑅𝑖 as the expected regard of an online algorithm under in-
stance𝑖. We define𝑛𝑘(𝑇) as the number of arm𝑘 is pulled. We note
that the optimal arm in instance𝑖 is arm𝑖, and the optimality gaps
of other arms are Δ/2. Therefore, the regret of the algorithm can
be written as
𝑅𝑖 =
𝐾∑︁
𝑘=1,𝑘≠𝑖
𝑘·E 𝑖[𝑛𝑘(𝑇)]Δ,(21)
Also, we have that (which is adapted from Lemma A.1 from [2],
noting that𝑛𝑖[𝑇] is a random variable bounded by𝑇/𝑖 and the KL
divergence between Bernoulli(𝜇(0) 𝑖 ) and Bernoulli(𝜇(𝑖) 𝑖 ) is bounded
by2Δ 2.)
E𝑖[𝑛𝑖(𝑇)]]≤E 0[𝑛𝑖(𝑇)]+ 𝑇 𝑖 √︁ E0[𝑛𝑖(𝑇)]Δ 2,(22)
Then, by the identity that˝𝐾 𝑖=1𝑖·E0[𝑛𝑖(𝑇)]=𝑇 and Cauchy–Schwarz
inequality, we have
𝐾∑︁
𝑖=1
𝑖·E 𝑖[𝑛𝑖(𝑇)](23)

Learning When to Update: A Near-Optimal Timing Bandit Approach MobiHoc ’26, November 23-26, 2026, Tokyo, Japan
≤
𝐾∑︁
𝑖=1
𝑖·

E0[𝑛𝑖(𝑇)]+ 𝑇 𝑖 √︁ E0[𝑛𝑖(𝑇)]Δ 2  (24)
=𝑇+
𝐾∑︁
𝑖=1
𝑇
√︁
E0[𝑛𝑖(𝑇)]Δ 2 (25)
=𝑇+𝑇Δ
𝐾∑︁
𝑖=1
√︂
1
𝑖𝑖E0[𝑛𝑖(𝑇)](26)
≤𝑇+𝑇Δ
vut 𝐾∑︁
𝑖=1
 √︂
1
𝑖
!2 vut 𝐾∑︁
𝑖=1
√︁
𝑖E0[𝑛𝑖(𝑇)]
2
(27)
≤𝑇+𝑇Δ
√
𝑇
√︁
log𝐾(28)
Then we have that
𝐾∑︁
𝑖=1
𝑅𝑖 =Δ
𝐾∑︁
𝑖=1
(𝑇−𝑖·E 𝑖[𝑛𝑖(𝑇)]) (29)
≥Δ·(𝐾·𝑇−𝑇−𝑇Δ
√
𝑇
√︁
log𝐾)(30)
≥ 𝐾2
16
√︄
𝑇
log𝐾 (31)
where the last equality is achieved by taken Δ= 1 4 𝐾√ 𝑇log𝐾 and
noting that 𝐾≥ 2. We conclude that exist an 𝑖∈[𝐾] such that
𝑅𝑖≥ 1 16𝐾 √︁ 𝑇/log𝐾.□
D Proof of Lemma 4
Proof of Lemma 4. We first define some notations. Not that
there are𝑚𝑘(𝑡) feedback of the cost of arm 𝑘 at slot𝑡. For each
arm𝑘, we useℎ𝑖(𝑗) to denote the random variable of𝑔(𝑗) (or the
distribution𝑓𝑗 ) at its𝑖-th update. And we use𝜇𝑘,𝑖 as the𝑖-th sample
of𝜇 𝑘; that is
𝜇𝑘,𝑖 = 1 𝑘

𝐶(𝑘)+
𝑘∑︁
𝑗=1
ℎ𝑖(𝑗)
!
(32)
Then, we have that
¯𝜇𝑘(𝑡)= 1 𝑚𝑘(𝑡)
𝑚𝑘(𝑡)∑︁
𝑖=1
𝜇𝑘,𝑖 (33)
= 1 𝑘·𝑚 𝑘(𝑡)
𝑚𝑘(𝑡)∑︁
𝑖=1
𝑘∑︁
𝑗=1
ℎ𝑖(𝑗)+ 𝐶(𝑘) 𝑘 .(34)
Noting that
𝜇𝑘 = 1 𝑘·𝑚 𝑘(𝑡)
𝑚𝑘(𝑡)∑︁
𝑖=1
𝑘∑︁
𝑗=1
˜𝑔(𝑗)+ 𝐶(𝑘) 𝑘 (35)
= 1 𝑘·𝑚 𝑘(𝑡)
𝑚𝑘(𝑡)∑︁
𝑖=1
𝑘∑︁
𝑗=1
E[ℎ𝑖(𝑗)]+ 𝐶(𝑘) 𝑘 (36)
=E
"
1
𝑘·𝑚 𝑘(𝑡)
𝑚𝑘(𝑡)∑︁
𝑖=1
𝑘∑︁
𝑗=1
ℎ𝑖(𝑗)+ 𝐶(𝑘) 𝑘
#
.(37)
We have that
P(| ¯𝜇𝑘(𝑡)−𝜇 𝑘|≥𝑟 𝑘(𝑡)) (38)
=P

1
𝑘·𝑚 𝑘(𝑡)

 𝑚𝑘(𝑡)∑︁ 𝑖=1 𝑘∑︁ 𝑗=1 ℎ𝑖(𝑗)− 𝑚𝑘(𝑡)∑︁ 𝑖=1 𝑘∑︁ 𝑗=1 E[ℎ𝑖(𝑗)]

 (39)
≥𝑟 𝑘(𝑡)
!
(40)
≤2 exp(−2·𝑘·𝑚 𝑘(𝑡)·𝑟 2 𝑘(𝑡))(41)
where the final step follows Hoeffding’s inequality by noting that
ℎ𝑖(𝑗),∀𝑖∈[𝑚 𝑘(𝑡)],𝑗∈[𝑘] are independent and bounded random
variables in[0,𝑀] . And we show the lemma by putting the value
of𝑟𝑘(𝑡)in the last step, which leads to
P(| ¯𝜇𝑘(𝑡)−𝜇 𝑘|≥𝑟 𝑘(𝑡))≤2·𝐾 −1·𝑇−2 (42)
□
E Proof of Lemma 5
Proof of Lemma 5. We prove it by showing that if arm𝑖 and 𝑗
remain inAat the end of a super-round, we have
𝑖·𝛿 𝑚𝑖
𝑗·𝛿 𝑚𝑗
≤2,(43)
where𝛿𝑚𝑖 represents the increment in the number of samples for
arm𝑖 that are obtained during the super-round. We do not specify
the super-round in the notation for ease of presentation.
In Algorithm 1, we have that, for each arm𝑖 inA (which remains
inA after the super-round), we will obtain one sample if we pull an
arm with index larger than𝑖. In a super-round, we have that ˜𝑖 (the
arm we pull) will be no smaller than𝑖, when𝑖≤ 2 ˆ𝑗− ˜𝑗−1 , according
to Line 13. And for each ˜𝑗, we have ˆ𝑧= 2 ˜𝑗− 2 ˜𝑗−1 number of arm
pulling. We have that,
𝛿𝑚𝑖 =1+
⌊ ˆ𝑗−log 2𝑖⌋∑︁
˜𝑗=1

2 ˜𝑗−2 ˜𝑗−1  =2⌊ ˆ𝑗−log 2𝑖⌋ =2 ˆ𝑗−⌈log 2𝑖⌉.(44)
And, we have that,
𝑖·𝛿 𝑚𝑖
𝑗·𝛿 𝑚𝑗
= 2 ˆ𝑗−⌈log 2𝑖⌉+log 2𝑖
2 ˆ𝑗−⌈log 2𝑗⌉+log 2𝑗 ≤2.(45)
And, we conclude the lemma.□
F Proof of Lemma 6
Proof of Lemma 6. For clarity, we denoteA(𝑡) as the setA at
the beginning of slot𝑡. Recall that𝑡𝑠 represents the beginning slot
of the𝑠-th super-round. According to Lemma 5, we have that
𝑖·𝑚 𝑖(𝑡𝑠)
𝑗·𝑚 𝑗(𝑡𝑠)≥ 1 2,∀𝑖,𝑗∈A(𝑡 𝑠).(46)
If an arm, say 𝑗, is eliminated during or before the super-round,
𝑚𝑗 will not increase afterward. We can easily see that
𝑖·𝑚 𝑖(𝑡𝑠)
𝑗·𝑚 𝑗(𝑡𝑠)≥ 1 2,∀𝑖∈A(𝑡 𝑠),∀𝑗∈[𝐾].(47)
We first show the following inequality for the number of samples
of an arm𝑖≠𝑘 ∗ at slot𝑡𝑠.
𝑚𝑖(𝑡𝑠)≤ 36𝑀2 log( √ 𝐾𝑇) 𝑖·Δ 2 𝑖 +𝐾.(48)

MobiHoc ’26, November 23-26, 2026, Tokyo, Japan Lin et al.
Suppose not, we consider the first𝑡𝑠′ such that,
𝑚𝑖(𝑡𝑠′)> 36𝑀2 log( √ 𝐾𝑇) 𝑖·Δ 2 𝑖 .(49)
We have that
Δ𝑖 >6·
√︄
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚 𝑖(𝑡𝑠′) (50)
(𝑎)
≥2·
√︄
𝑀2 log( √ 𝐾𝑇)
𝑘∗·𝑚𝑘∗(𝑡𝑠′) +2·
√︄
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚 𝑖(𝑡𝑠′) ,(51)
where (a) is by (47) noting that arm𝑘∗ is always inA under the
clean eventE.
Then, we can show that
¯𝜇𝑖−
√︄
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚 𝑖(𝑡) (52)
≥𝜇𝑖−2·
√︄
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚 𝑖(𝑡) (53)
=𝜇𝑘∗+Δ𝑖−2·
√︄
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚 𝑖(𝑡) (54)
≥¯𝜇𝑘∗+
√︄
𝑀2 log( √ 𝐾𝑇)
𝑘∗·𝑚𝑘∗(𝑡) −2·
√︄
𝑀2 log( √ 𝐾𝑇)
𝑘∗·𝑚𝑘∗(𝑡) (55)
+Δ𝑖−2·
√︄
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚 𝑖(𝑡) (56)
(51)
> ¯𝜇𝑘∗+
√︄
𝑀2 log( √ 𝐾𝑇)
𝑘∗·𝑚𝑘∗(𝑡) .(57)
We will have the elimination condition (Line 26 in Algorithm 1)
holds, and arm𝑖 will be eliminated, and𝑚𝑖 will remain unchanged
afterward. Noting that we at most obtained𝐾 samples of arm𝑖 and
due to the definition of𝑠′ we choose, we have that,
𝑚𝑖(𝑡𝑠′)≤𝑚 𝑖(𝑡𝑠′−1)+𝐾≤ 36𝑀2 log( √ 𝐾𝑇) 𝑖·Δ 2 𝑖 +𝐾.(58)
And we have that𝑚𝑖(𝑇) is bounded by𝑚𝑖(𝑡𝑠) at the complete last
super-round, plus the samples obtained from that to𝑇 (which are
bounded by𝐾). We conclude the lemma.□
G Proof of Lemma 7
Proof of Lemma 7. We consider the subset of arms K𝑗 . We
denote 𝐾′ =min{𝐾, 2𝑗}, which is the maximum index of the
arms in{K𝑗 . Note that, according to Line 16 in Algorithm 1, an
arm 𝑘 inK𝑗 will only be pulled when all arms with larger in-
dexes have been eliminated. If arm 𝑘 has never been pulled in
the total horizon, we have 𝑛𝑘(𝑇)= 0. Otherwise, suppose the
𝑡′ is the slot arm 𝑘 is eliminated; otherwise, we set 𝑡′ =𝑇 . We
have that the total number of pulling arms𝑘 in the whole period,
𝑛𝑘(𝑇)=𝑛 𝑘(𝑡′), as arm 𝑘 will not be pulled afterward. Also, all
arms inK𝑗 with index larger than𝑖 have been eliminated, and thus,
𝑛𝑖(𝑇)=𝑛 𝑖(𝑡′),∀𝑖∈{𝑖>𝑘|𝑖∈K 𝑗}. Also, we will not obtain sample
of arm 𝑘 afterward; thus,𝑚𝑖(𝑇)=𝑚 𝑖(𝑡′)= ˝𝐾 𝑖=𝑘𝑛𝑖(𝑡′), as each
pulling of arms with indexed larger than𝑘 will provide a sample
for arm𝑘if arm𝑘haven’t been eliminated. We have that
𝐾′∑︁
𝑖=𝑘
𝑛𝑖(𝑇)≤
𝐾′∑︁
𝑖=𝑘
𝑛𝑖(𝑇)+
𝐾∑︁
𝑖=𝐾′
𝑛𝑖(𝑡′)=𝑚 𝑖(𝑇).(59)
We then apply Lemma 6 to the above inequality.
In summary, we have the following inequality.
𝑛𝑘(𝑇)=0or
𝐾′∑︁
𝑖=𝑘
𝑛𝑖(𝑇)≤ 36𝑀2 log( √ 𝐾𝑇) 𝑘·Δ 2 𝑘 +2·𝐾,∀𝑘∈K 𝑗.(60)
In addition, it is not hard to see that
∑︁
𝑖∈K𝑗
𝑖·𝑛 𝑖(𝑇)≤𝑇.(61)
To derive an upper bound to ˝ 𝑖∈K𝑗𝑖·𝑛 𝑖(𝑇)·Δ 𝑖, the left-hand
side of (14), we consider an optimization problem to maximize it
by optimizing𝑛𝑖(𝑇),∀𝑖∈K 𝑗 while subject to constraint (60) and
constraint (61).
We separately consider arms with large cost differences where
condition (60) tends to dominate and those with small cost dif-
ferences where condition (61) will likely dominate. With such a
consideration, we separate arms inK𝑗 into the following two sets:
I1 :=
(
𝑖∈K 𝑗

 1 Δ𝑖 ≤ √︄ 𝑇 36𝑀2 log( √ 𝐾𝑇) ) ,(62)
and
I2 :=
 
 𝑖∈K 𝑗

 Δ𝑖 < √︄ 36𝑀2 log( √ 𝐾𝑇) 𝑇    .(63)
We consider two relaxed constraints to (60) and condition (61),
𝑛𝑘(𝑇)=0or
𝐾′∑︁
𝑖≥𝑘,𝑖∈I 1
𝑛𝑖(𝑇)≤ 36𝑀2 log( √ 𝐾𝑇) Δ2 𝑘 +2𝐾,∀𝑘∈I 1.(64)
and ∑︁
𝑘∈I2
𝑘·𝑛 𝑘(𝑇)≤𝑇.(65)
We can see that optimizing ˝ 𝑖∈K𝑗𝑖·𝑛 𝑖(𝑇)·Δ 𝑖 under the re-
laxed constraints will provide a greater objective value, and we can
separate optimizing the𝑛𝑖(𝑇)inI 1 andI2 in the relaxed problem.
We first considers optimizing𝑛𝑖(𝑇) inI1 subject to (64) to maxi-
mizing
ˆ𝑅1(𝑇):= ∑︁
𝑘∈I1
𝑘·𝑛 𝑘(𝑇)·Δ 𝑘.(66)
We denote such an optimization problem asP1. To find its optimal
solution, we identify a special structure for the optimal solution,
which is shown in Lemma 11. We consider one optimal solution
toP1 that satisfies the property stated in Lemma 11, i.e., 𝑗·Δ 𝑗 and
𝑗·Δ 2 𝑗 is a strictly increasing sequence in the index of the arms
inG=

𝑗∈I 1|𝑛𝑗(𝑇)>0

. We note that fixing G, the problem
becomes to maximizing
ˆ𝑅1(𝑇):= ∑︁
𝑘∈G
𝑘·𝑛 𝑘(𝑇)·Δ 𝑘,(67)

Learning When to Update: A Near-Optimal Timing Bandit Approach MobiHoc ’26, November 23-26, 2026, Tokyo, Japan
subject to
∑︁
𝑖≥𝑘,𝑖∈G
𝑛𝑖(𝑇)≤ 36𝑀2 log( √ 𝐾𝑇) 𝑘·Δ 2 𝑘 +2𝐾,∀𝑘∈G.(68)
with decision variables𝑛 𝑗(𝑇)>0,∀𝑗∈G. Moreover, according to
Lemma 11, we have that𝑖·Δ 𝑖 <𝑘·Δ 𝑘 and𝑖·Δ 2 𝑖 <𝑘·Δ 2 𝑘 if𝑖<𝑘 . We
list the elements inG (note that 𝑗∈G if and only if𝑛𝑗(𝑇)> 0) in
increasing order, i.e.,𝑘1≤𝑘 2···≤𝑘 |G| . Noting that fixingG,P1 is
an LP with increasing weight in𝑛𝑘(𝑇) and tightening budget limits
in𝑘, and the optimal solution is to allocate as most the budget as
possible to larger𝑘. We can easily show that the optimal solution
to theP 1 is by setting,
𝑛∗ 𝑘𝑖(𝑇)=36𝑀 2 log( √ 𝐾𝑇)·

1
𝑘𝑖·Δ 2 𝑘𝑖 − 1 𝑘𝑖+1·Δ 2 𝑘𝑖+1
!
,∀𝑖<|G|,
(69)
and
𝑛∗ 𝑘|G| (𝑇)= 36𝑀2 log( √ 𝐾𝑇) Δ2 𝑘|G| +2𝐾.(70)
We have the following argument,
ˆ𝑅1(𝑇)(71)
≤
|G|∑︁
𝑖=1
𝑘𝑖·𝑛∗ 𝑘𝑖(𝑇)·Δ 𝑘𝑖 (72)
≤
|G|−1∑︁
𝑖=1
𝑘𝑖·Δ𝑘𝑖·36𝑀 2 log( √ 𝐾𝑇)·

1
𝑘𝑖·Δ 2 𝑘𝑖 − 1 𝑘𝑖+1·Δ 2 𝑘𝑖+1
!
+𝑘|G| ·Δ𝑘|G|· '›
«
36𝑀2 log( √ 𝐾𝑇)· 1 𝑘|G| ·Δ 2 𝑘|G| +𝐾 “ﬁ ‹ (73)
=36𝑀 2 log( √ 𝐾𝑇)·

1
Δ𝑘1
+
|G|∑︁
𝑖=2
𝑘𝑖·Δ𝑘𝑖−𝑘𝑖−1·Δ𝑘𝑖−1
𝑘𝑖·Δ 2 𝑘𝑖
!
+𝐾·𝑘 |G| ·Δ𝑘|G| (74)
(62)
≤36𝑀 2 log( √ 𝐾𝑇)·
 √︄
𝑇
36𝑀2 log( √ 𝐾𝑇)
+
|G|∑︁
𝑖=2
√︄
𝑇
36𝑀2 log( √ 𝐾𝑇) 1 𝑘𝑖 Δ𝑘𝑖 (𝑘𝑖 Δ𝑘𝑖−𝑘𝑖−1 Δ𝑘𝑖−1)
!
+2𝐾·𝑘 |G| ·Δ𝑘|G| (75)
≤
√︃
36𝑇𝑀 2 log( √ 𝐾𝑇)·

1+log
𝑘|G| ·Δ𝑘|G|
𝑘1·Δ𝑘1
!
+2𝐾 2( ¯𝐶+𝑀)(76)
≤
√︃
36𝑇𝑀 2 log( √ 𝐾𝑇) '››
«
1+log 2𝐾( ¯𝐶+𝑀) √ 𝑇√︃
36𝑀2 log( √ 𝐾𝑇)
“ﬁﬁ
‹
+2𝐾 2( ¯𝐶+𝑀)(77)
where the last equality is by noting that 𝑘1 ≥ 1,𝑘|G| ≤𝐾 and
Δ𝑘|G|≤ ¯𝐶+𝑀(following the definition of𝜇 𝑘).
As for the arms inI2, we can have that
ˆ𝑅2(𝑇):= ∑︁
𝑘∈I2
𝑘·𝑛 𝑘(𝑇)·Δ 𝑘 (78)
≤
∑︁
𝑘∈I2
𝑘·𝑛 𝑘(𝑇)·
√︄
36𝑀2 log( √ 𝐾𝑇)
𝑇 (79)
≤
√︃
36𝑇𝑀 2 log( √ 𝐾𝑇).(80)
where the first inequality is by that all arms inI2,
Δ𝑘≤
√︃
36𝑀2 log( √ 𝐾𝑇)/𝑇 , and the last inequality is due to˝ 𝑘∈I2𝑘·
𝑛𝑘(𝑇)≤𝑇.
As we discussed earlier in this proof, combiningˆ𝑅1(𝑇) and ˆ𝑅2(𝑇)
will provide an upper bound to˝ 𝑖∈K𝑗𝑖·𝑛 𝑖(𝑇)·Δ 𝑖, and we conclude
the lemma.
□
H An optimal structure toP 1
Lemma 11.There exists an optimal solution {𝑛𝑖(𝑇)}𝑖∈K 1 toP1
such that𝑖·Δ 2 𝑖 is a strictly increasing sequence in the index of the
arms inG= {𝑖|𝑛𝑖(𝑇)>0 }. Further,𝑖·Δ 𝑖 is also a strictly increasing
sequence in the index of the arms inG.
Proof of Lemma 11. We prove it by showing that eliminating
the diminishing sequence in

Δ𝑗

𝑗∈G will not decrease the objective
value. We consider an optimal solution

𝑛𝑗(𝑇)

𝑗∈K 1 . Suppose that
𝑗·Δ 2 𝑗 is not a non-decreasing sequence in the index of the arms
{𝑗|𝑗∈G} . Then we can find two adjacent arms inG, denoted as
𝑗1 <𝑗 2, such that 𝑗1Δ2 𝑗1≥𝑗 2Δ2 𝑗2, which is called aninversion pair.
Also, according to condition (60), we have
𝐾∑︁
𝑖≥𝑗 1,𝑖∈G
𝑛𝑖(𝑇)≤ 36𝑀2 log( √ 𝐾𝑇) 𝑗1·Δ 2 𝑗1 +2𝐾,(81)
and
𝐾∑︁
𝑖≥𝑗 2,𝑖∈G
𝑛𝑖(𝑇)≤ 36𝑀2 log( √ 𝐾𝑇) 𝑗2·Δ 2 𝑗2 +2𝐾.(82)
Clearly, (81) implies (82). Next, we will show that under such a case,
we have
𝑗1·Δ 𝑗1≤𝑗 2·Δ 𝑗2,(83)
and we can, therefore, eliminate this inversion pair by constructing
a new optimal solution.
We prove it by contradiction. Suppose that𝑗1·Δ 𝑗1 >𝑗 2·Δ 𝑗2. We
construct an alternative solution where ˜𝑛𝑗1(𝑇)=𝑛 𝑗1(𝑇)+𝑛 𝑗2(𝑇) ,
˜𝑛𝑗2(𝑇)= 0and we keep all other 𝑛𝑗(𝑇) . It is not hard to check that
the constructed solution is also feasible toP1 with a strictly larger
objective than the previous one. It contradicts that the original
solution is optimal toP 1. We therefore have (83).
We consider an alternative solution that ˜𝑛𝑗1(𝑇)= 0, ˜𝑛𝑗2(𝑇)=
𝑛𝑗1(𝑇)+𝑛 𝑗2(𝑇) and we keep all other𝑛𝑗(𝑇) . We can easily check
that the constructed solution is also feasible toP1 with an objective
no smaller than the previous one. Thus, the newly constructed
solution is also optimal. Moreover,𝑗1 is no longer in the index set
with non-zero𝑛 𝑗(𝑇). We eliminate at least one inversion pair.
By continuously applying the same way to the optimal solution
until there does not exist𝑗1 <𝑗 2, such that𝑗1Δ2 𝑗1≥𝑗 2Δ2 𝑗2, we obtain
one optimal solution that achieves the desired property.

MobiHoc ’26, November 23-26, 2026, Tokyo, Japan Lin et al.
Further, we show that𝑖·Δ 𝑖 is also a strictly increasing sequence
in the index of the arms inG. We prove it by contradiction. Sup-
pose that 𝑗1·Δ 𝑗1 >𝑗 2·Δ 𝑗2. We construct an alternative solution
where ˜𝑛𝑗1(𝑇)=𝑛 𝑗1(𝑇)+𝑛 𝑗2(𝑇) , ˜𝑛𝑗2(𝑇)= 0and we keep all other
𝑛𝑗(𝑇) . It is not hard to check that the constructed solution is also
feasible toP1 with a strictly larger objective than the previous one.
It contradicts that the original solution is optimal toP 1.
□
I Proof of Theorem 10
Proof of Theorem 10. We denote the𝑛𝑖(𝑡) as the number of
times that arm𝑖 is selected as ˜𝑖 at Step 16 of Algorithm 1 up to time
𝑡. We denote𝑛𝑖,𝑘(𝑡) as the number of times that arm𝑘 is actually
pulled following the LCB algorithm in the forward window of𝑖, i.e.,
(17). Clearly, we have that
∑︁
𝑘∈W𝑖
𝑛𝑖,𝑘(𝑡)=𝑛 𝑖(𝑡),(84)
and
𝐾∑︁
𝑖=1
∑︁
𝑘∈W𝑖
𝑛𝑖,𝑘(𝑇)·𝑘=𝑇.(85)
We decompose the regret of the algorithm into two parts,
𝑅𝑂𝐶(𝑇)=
𝐾∑︁
𝑖=1
∑︁
𝑘∈W𝑖
𝑛𝑖,𝑘(𝑇)·𝑘·Δ 𝑘 (86)
=
𝐾∑︁
𝑖=1
∑︁
𝑘∈W𝑖
𝑛𝑖,𝑘(𝑇)·𝑘·Δ 𝑘−4·
𝐾∑︁
𝑖=1
𝑛𝑖(𝑇)·𝑖·Δ 𝑖
|                                                       {z                                                       }
Part I:𝑅𝐼
+4·
𝐾∑︁
𝑖=1
𝑛𝑖(𝑇)·𝑖·Δ 𝑖
|                  {z                  }
Part II:𝑅𝐼𝐼
.(87)
We first handle part I. For part I, we note that, following LCB, if
Δ𝑘 >Δ 𝑖.
𝑛𝑖,𝑘(𝑇)≤ 4𝑀2 log( √ 𝐾𝑇) 𝑘·(Δ 𝑘−Δ𝑖)2 .(88)
We can show it by contradiction. Suppose no, we would have that
at some𝑡
𝑚𝑘(𝑡)≥𝑛 𝑖,𝑘(𝑇)> 4𝑀2 log( √ 𝐾𝑇) 𝑘·(Δ 𝑘−Δ𝑖)2 ,(89)
and we have that
¯𝜇𝑖−
√︄
𝑀2 log( √ 𝐾𝑇)
𝑖·𝑚 𝑖(𝑡) (90)
≤𝜇 𝑖 (91)
=𝜇 𝑘−Δ𝑖+Δ𝑘 (92)
≤ ¯𝜇𝑘+
√︄
𝑀2 log( √ 𝐾𝑇)
𝑘·𝑚 𝑘(𝑡) −Δ𝑖+Δ𝑘 (93)
< ¯𝜇𝑘−
√︄
𝑀2 log( √ 𝐾𝑇)
𝑘·𝑚 𝑘(𝑡) (94)
where the last equality follows (89), and thus arm 𝑘 will not be
chosen following LCB defined in (17).
For ease of presentation, we denote
𝑅𝐼,𝑖 ≜
∑︁
𝑘∈W𝑖
𝑛𝑖,𝑘(𝑇)·𝑘·Δ 𝑘−4·𝑛 𝑖(𝑇)·𝑖·Δ 𝑖 (95)
We have that
𝑅𝐼 =
𝐾∑︁
𝑖=1
𝑅𝐼,𝑖.(96)
We have that
𝑅𝐼,𝑖
(𝑎)
≤4·𝑖· '›
«
∑︁
𝑘∈W𝑖
𝑛𝑖,𝑘(𝑇)·Δ 𝑘−𝑛𝑖(𝑇)·Δ 𝑖 “ﬁ
‹
(97)
(84)
=4·𝑖·
∑︁
𝑘∈W𝑖
𝑛𝑖,𝑘(𝑇)· (Δ𝑘−Δ𝑖) (98)
≤4·𝑖·
∑︁
𝑘∈W𝑖,Δ𝑘 >Δ𝑖
𝑛𝑖,𝑘(𝑇)· (Δ𝑘−Δ𝑖) (99)
where (a) is by noting that the arm indexes in the forward window
W𝑖 are bounded by4·𝑖.
We separately consider arms inW𝑖 where Δ𝑘 >Δ 𝑖, depending
on whether Δ𝑘−Δ𝑖≥
√︂
𝑤·4𝑀 2 log( √ 𝐾𝑇)
𝑖·𝑛𝑖(𝑇) . For the "smaller" ones, we
have that
∑︁
𝑘:Δ𝑘−Δ𝑖≤
√︂
𝑤·4𝑀 2 log( √ 𝐾𝑇)
𝑖·𝑛𝑖(𝑇)
𝑛𝑖,𝑘(𝑇)· (Δ𝑘−Δ𝑖) (100)
≤
∑︁
𝑘:Δ𝑘−Δ𝑖≤
√︂
𝑤⁄4𝑀2 log( √ 𝐾𝑇)
𝑖·𝑛𝑖(𝑇)
𝑛𝑖,𝑘(𝑇)·
√︄
𝑤·4𝑀 2 log( √ 𝐾𝑇)
𝑖·𝑛 𝑖(𝑇) (101)
≤𝑛𝑖(𝑇)·
√︄
𝑤·4𝑀 2 log( √ 𝐾𝑇)
𝑖·𝑛 𝑖(𝑇) (102)
=
√︃
𝑛𝑖(𝑇)·𝑤·4𝑀 2 log( √ 𝐾𝑇)/𝑖.(103)
For the "larger" ones, we have that
∑︁
𝑘:Δ𝑘−Δ𝑖≥
√︂
𝑤·4𝑀 2 log( √ 𝐾𝑇)
𝑖·𝑛𝑖(𝑇)
𝑛𝑖,𝑘(𝑇)· (Δ𝑘−Δ𝑖) (104)
(88)
≤
∑︁
𝑘:Δ𝑘−Δ𝑖≥
√︂
𝑤·4𝑀 2 log( √ 𝐾𝑇)
𝑖·𝑛𝑖(𝑇)
𝑤·4𝑀 2 log( √ 𝐾𝑇)
𝑘·(Δ 𝑘−Δ𝑖) (105)
≤𝑤·
√︄
𝑛𝑖(𝑇)· 4𝑀2 log( √ 𝐾𝑇) 𝑤·𝑖 (106)
=
√︃
𝑛𝑖(𝑇)·𝑤·4𝑀 2 log( √ 𝐾𝑇)/𝑖.(107)
Then, for part I, we have that
𝑅𝐼 =
𝐾∑︁
𝑖=1
𝑅𝐼,𝑖 (108)

Learning When to Update: A Near-Optimal Timing Bandit Approach MobiHoc ’26, November 23-26, 2026, Tokyo, Japan
≤
𝐾∑︁
𝑖=1
√︃
𝑛𝑖(𝑇)·𝑤·4𝑀 2 log( √ 𝐾𝑇)/𝑖(109)
(𝑎)
≤
√︃
𝑇·𝑤·4𝑀 2 log( √ 𝐾𝑇)·
vut 𝐾∑︁
𝑖=1
1/𝑖2 (110)
≤4·
√︃
𝑇·𝑤·𝑀 2 log( √ 𝐾𝑇)(111)
, where (a) is by noting that ˝ 𝑖𝑛𝑖(𝑇)·𝑖≤𝑇 and applying the
Cauchy–Schwarz inequality, and the last equation is by noting that˝𝐾
𝑖=1 1/𝑖2≤2.
We then move on to part II.
𝑅𝐼𝐼 =4·
𝐾∑︁
𝑖=1
𝑛𝑖(𝑇)·𝑖·Δ 𝑖.(112)
Recall that𝑛𝑖(𝑡) is the number of times that arm 𝑖 is selected as
˜𝑖 at Step 16 of Algorithm 1 up to time 𝑡. We actually pull an arm
following the LCB algorithm in the forward window of𝑖, i.e., (17).
We note that𝑅𝐼𝐼 is similar to the regret that we have analyzed for
theBCAEalgorithm. But there is a major difference: at each time to
select ˜𝑖 at Step 16, we are based on the past pulling decisions that
further involve the LCB component (17), instead of those selected
at previous rounds of Step 16. Nevertheless, we can show that key
properties for demonstrating the regret forBCAEstill hold in the
analysis of𝑅𝐼𝐼 (with only differences in some constant factors).
The first property is the balanced confidence bound among all
arms, i.e., analogous to Lemma 5. Specifically, we can show that
𝑖·𝑚 𝑖(𝑡𝑠)
𝑗·𝑚 𝑗(𝑡𝑠)≤4,∀𝑖,𝑗∈A(𝑡 𝑠).(113)
The constant increases for two to four, compared to Lemma 5.
Nevertheless, this will only incur a larger constant factor in all our
later analyses. As we showed in Appendix E, the critical step is to
show that at the end of a super-round, we have
𝑖·𝛿 𝑚𝑖
𝑗·𝛿 𝑚𝑗
≤4,(114)
where𝛿𝑚𝑖 represents the increment in the number of samples for
arm𝑖 that are obtained during the super-round. As the arm we
actually pull is not smaller (in index) than that in theBCAE, we
have that𝛿𝑚𝑖 is at least that in theBCAE(in (44)), i.e.,
𝛿𝑚𝑖≥2 ˆ𝑗−⌈log 2𝑖⌉.(115)
In addition, we get more samples of arm𝑖 if we actually pull the
larger arm. This only happens when ˜𝑖 at Step 16 of Algorithm 1
is within[2⌈log2𝑖⌉−2+ 1, 2⌈log2𝑖⌉−1] following the definition of the
forward window in (16) and2 ˆ𝑗− ˜𝑗 = 2⌈log2𝑖⌉−1].4 The number of
such pulling is at most2 ˜𝑗− 2 ˜𝑗−1 when ˜𝑗= ˆ𝑗−⌈log 2𝑖⌉+ 1. We have
that
𝛿𝑚𝑖≤2 ˆ𝑗−⌈log 2𝑖⌉+2 ˆ𝑗−⌈log 2𝑖⌉.(116)
With the lower bound and upper bound above, we can easily con-
clude (114) (similar to (45) and (113). Further, with (113), we can
prove the version of Lemma 6 for the analysis of𝑅𝐼𝐼 (with a larger
constant factor).
4According to Step 16 of Algorithm 1, if ˜𝑗 is larger, such an ˜𝑖 is too larger to be chosen.
If ˜𝑗is smaller, ˜𝑖is chosen only when arm𝑖has been eliminated.
The second property is the specific bound on𝑛𝑖(𝑇) , analogous
to (15), due to the feedback structure. We note that 𝑛𝑖(𝑡) is the
number of times that arm𝑖 is selected as ˜𝑖 at Step 16 of Algorithm 1
up to time𝑡. 5 Thus,𝑛𝑖(𝑡) is similar to that underBCAE, we will
never choose𝑖 at Step 16 unless all the arms in the corresponding
subset with larger indexes are eliminated, which results in (15)
(with a larger constant factor under the analysis of𝑅𝐼𝐼 ).
With the above two key properties, we can follow the proof of
Lemma 7 and Theorem 8 to show that𝑅𝐼𝐼 is in ˜𝑂( √ 𝑇) . We omit the
details for simplicity. Together with(111) and (87), we conclude the
theorem.
□
5We note that while inOE-BCAE, arm 𝑖 may also be pulled when chosen by the
introduced LCB, these are not counted in𝑛𝑖(𝑡).
