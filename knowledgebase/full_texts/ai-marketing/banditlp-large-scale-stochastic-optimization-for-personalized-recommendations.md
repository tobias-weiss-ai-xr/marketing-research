---
title: 'BanditLP: Large-Scale Stochastic Optimization for Personalized Recommendations'
url: https://arxiv.org/abs/2601.15552
category: ai-marketing
subcategory: empirical
date: 2026-01
venue: ''
authors:
- Phuc Nguyen
- Benjamin Zelditch
- Joyce Chen
- Rohit Patra
- Changshuai Wei
source: arxiv
pdf_url: https://arxiv.org/pdf/2601.15552
pages: 10
chars: 53444
fetched_at: '2026-11-08T13:17:56+00:00'
kb_version: 1
---

# BanditLP: Large-Scale Stochastic Optimization for Personalized Recommendations

BanditLP: Large-Scale Stochastic Optimization for Personalized
Recommendations
Phuc Nguyen
LinkedIn
San Francisco, USA
honnguyen@linkedin.com
Benjamin Zelditch
LinkedIn
New York, USA
bzelditch@linkedin.com
Joyce Chen
LinkedIn
Sunnyvale, USA
joychen@linkedin.com
Rohit Patra
LinkedIn
New York, USA
ropatra@linkedin.com
Changshuai Wei∗
LinkedIn
Seattle, USA
chawei@linkedin.com
Abstract
We present BanditLP, a scalable multi-stakeholder contextual bandit
framework that unifies neural Thompson Sampling (TS) for learning
objective-specific outcomes with a large-scale linear program (LP)
for constrained action selection at serving time. The methodology
is application-agnostic, compatible with arbitrary neural architec-
tures, and deployable at web scale—with an LP solver capable of
handling billions of variables. Experiments on public benchmarks
and synthetic data show consistent gains over strong baselines.
We apply this approach in LinkedIn’s email marketing system and
demonstrate business win, illustrating the value of integrated ex-
ploration and constrained optimization in production.
CCS Concepts
•Mathematics of computing → Probability and statistics;•
Computing methodologies→ Machine learning;•Informa-
tion systems→ Information retrieval;Web searching and infor-
mation discovery;Online advertising;•Applied computing →
Marketing.
Keywords
Contextual Bandit, Linear Program, Stochastic Optimization, Multi-
stakeholder Recommendation, Marketing
1 INTRODUCTION
Most contextual-bandit (CB) based recommender systems (RS) fo-
cus on optimizing a single objective, typically the utility of end
users, such as clicks or engagement metrics. However, in real-world
platform ecosystems, multiple stakeholders are involved. For exam-
ple, buyers and sellers on Amazon, artists and listeners on Spotify,
viewers and content creators on YouTube or TikTok, and users,
drivers, and restaurants on UberEats or DoorDash all form distinct
stakeholder groups. Within an organization, there may also be mul-
tiple stakeholders. We see within LinkedIn email marketing system
that the stakeholders include LinkedIn users, business lines within
∗Corresponding author
This work is licensed under a Creative Commons Attribution-NonCommercial-
NoDerivatives 4.0 International License.
LinkedIn (e.g. B2C vs. B2B), and the platform itself may have differ-
ent objectives and constraints. From the user-perspective, there are
conflicting objectives: maximizing conversions while maintaining
a low unsubscribe rate to preserve long-term reach. From the busi-
ness lines perspective, we need fair representation—for example, to
prevent the algorithm from over-promoting B2C products (which
often generate quicker, higher-volume conversions) at the expense
of B2B offerings. At the platform level, constraints such as maxi-
mum the number of emails sent to each member per week or the
total volume of emails must be enforced.
These systems require careful balancing utilities of all these
stakeholders, and call for multi-stakeholder contextual bandits that
balances exploration and exploitation while jointly managing poten-
tially conflicting objectives across these groups. We can frame this
multi-stakeholder problem as maximizing a primary cumulative
reward subject to multi-level constraints that safeguard stakehold-
ers’ interests in every round. This formulation is broadly applica-
ble in real-world systems that involves batch recommendations,
where operational constraints such as budget, capacity limits, and
latency targets coexist with fairness, minimum exposure, or safety
requirements. For instance, in e-commerce platforms like Amazon,
recommendation policies must balance user engagement against
seller exposure and inventory or delivery capacity limits. In con-
tent platforms such as TikTok or YouTube, models must allocate
impressions fairly across creators while optimizing viewer satis-
faction and respecting latency or throughput constraints [10, 33].
In LinkedIn’s email marketing system, recommendation policies
must satisfy user-level frequency caps, business-line-level repre-
sentation requirements, and platform-level performance guardrails
and volume limits simultaneously. These settings all share a com-
mon structure: optimizing a primary objective while satisfying
constraints across multiple stakeholders and system levels.
While prior research has advanced contextual bandits under
constraints or multiple objectives, none provides a solution suited
to large-scale applications with complex, multi-level stakeholder
constraints. Existing approaches based on linear or multi-armed
bandits [2, 17, 30] cannot capture complex, high-dimensional rela-
tionships between users, items, and contexts. Methods developed
for constrained or safe bandits typically handle only specific types
of constraints or a single constraint level [8, 12], making them diffi-
cult to apply in multi-level constraints settings. On the other hand,
large-scale recommender systems [21, 34] that combine predictive
arXiv:2601.15552v1  [cs.LG]  22 Jan 2026

Phuc et al.
models with LP solvers lack exploration, which amplifies selection
bias and leads to suboptimal long-term outcomes. To our knowl-
edge, no existing method jointly achieves i) the expressiveness to
model complex, high-dimensional relationships, ii) the flexibility
to satisfy interdependent multi-level stakeholder constraints, and
iii) the scalability required for web-scale deployment.
Our work addresses this gap by proposingBanditLP, an algo-
rithm which combines neural Thompson sampling (TS) for explo-
ration–exploitation and expressive modeling with a large-scale
linear program (LP) to balance multi-stakeholder objectives under
constraints. In our approach, rewards and costs are first estimated
and sampled via neural TS; then, at each decision round, an LP
sub-routine selects actions that satisfy multi-level constraints cor-
responding to different stakeholders.
In summary, the primary contributions of this paper are:
• Novel methodology: An algorithm, BanditLP, that cou-
ples neural TS with large-scale LP for multi-stakeholder sys-
tems. The method is highly generalizable: it applies across
applications, is compatible with arbitrary deep learning
architectures for modeling objectives, supports a rich set
of constraints, and scales to billions of recommendations.
We validate BanditLP on public benchmarks and synthetic
datasets, showing gains over established baselines.
• Large-scale application with real-world impacts: We
deploy BanditLP in LinkedIn’s large-scale email marketing
system. Online experiments show significant improvements
across multiple business objectives, leading to production
deployment. To our knowledge, this is the first large-scale
email marketing RS that combines contextual bandits with
constrained optimization and demonstrates business impact
via online A/B testing.
• Insights from deployment and A/B test: We describe
several modifications for large-scale deployment, including
speeding up and scaling neural TS, tuning and monitoring
the degree of exploration, calibrating Thompson-sampled
probabilities, and configuring the LP. We also detail an on-
line experiment design that avoids effect dilution and data
leakage, enabling a fair comparison between recommenders
with and without exploration.
2 RELATED WORK
Contextual bandit algorithms have emerged as a powerful frame-
work for personalized recommendation systems, with applica-
tions spanning healthcare, finance, and information retrieval. This
demonstrates the versatility of bandit-based approaches in solving
real-world recommendation challenges [6, 19, 24, 41]. Recent ad-
vances [1, 4, 42, 43] leverage the representational power of neural
networks, with some algorithms achieving provable regret guar-
antees [4, 42] and others showing strong empirical success [ 43].
However, traditional CB formulations optimize a single scalar re-
ward, which limits their applicability in multi-objective or multi-
stakeholder recommendation environments.
A rich body of work has studied constrained multi-armed ban-
dits, where costs are introduced alongside rewards, and the learner
aims to maximize cumulative reward while satisfying constraints.
One line of research focuses on knapsack-style constraints, where
interactions terminate once a constraint is violated [3, 20], or where
cumulative constraints must be respected across all rounds [ 14].
These differ from our setting, where constraints should be satis-
fied in every round. Another branch closely related to our problem
considers per-round constraints, often requiring the construction
of safe decision sets [ 2, 17], which can become computationally
expensive when constraints are complex. In [30], a global constraint
imposes a minimal level of performance in each round, and a lin-
ear bandit is combined with an LP sub-routine to select actions.
Our work shares similarities with [30] in combining a contextual
bandit method with linear programming (LP) to select arms that
balance constraints at each round. However, we extend this idea
to a richer contextual bandit setting with more complex reward
and cost functions and a larger set of constraints. Moreover, prior
work in constrained multi-arm or linear bandits primarily focuses
on regret analysis under simplified settings and on offline exper-
iments. In contrast, we aim to show how contextual bandits can
handle complex relationships between context and rewards, as well
as large-scale operational constraints in web applications.
The literature on contextual bandits for multi-objective and
multi-stakeholder settings is comparatively limited. Some ap-
proaches convert multiple objectives into a single scalar objective
through scalarization [7, 22, 36], but this is unsuitable when cer-
tain objectives (e.g., minimum selection or spend budgets) must
be treated as hard constraints. Other methods only accommodate
specific types of constraints. For instance, [8] constrains total per-
formance relative to a baseline level, while [12] solves the combina-
torial bandits for budget allocation in advertising using Bayesian
hierarchical models. These formulations are not directly applicable
to our problem, which involves potentially complex and multi-level
constraints. In [15], an algorithm combines general-purpose learn-
ing models with discrete constrained optimization to generate a
pool of safe solutions and employs inverse gap weighting to sam-
ple actions. However, in large-scale ecosystems with billions of
user–item combinations, maintaining such a pool becomes compu-
tationally prohibitive.
Our method is motivated by recent trends in recommender sys-
tems that increasingly integrate predictive models with scalable LP
solvers to enforce multi-objective trade-offs and operational con-
straints at decision time. For example, [34] uses base recommender
scores as LP inputs to balance buyer- and provider-side objectives,
and [21] addresses platform-level business constraints. Other ap-
plications employ LP to satisfy a variety of constraints, including
optimizing email volume [ 5], ensuring fairness in ranking [ 13],
promoting diversity in network growth [27], and managing mar-
ketplace budget allocations [27]. However, these approaches rely
solely on supervised models trained for predictive accuracy on
logged data, without any mechanism for exploration. This lack of
exploration often reinforces feedback loops—models repeatedly rec-
ommend items similar to those already popular, leading to “rich get
richer” dynamics—and ultimately results in suboptimal long-term
performance [19, 33, 35]. Furthermore, unlike bandit-based recom-
menders, such systems are prone to the cold-start problem [ 37].
A key distinction of our approach is the use of neural Thompson
sampling, which naturally balances exploration and exploitation
to mitigate selection bias, handle uncertainty, and adapt to new
information for improved long-term outcomes.

BanditLP: Large-Scale Stochastic Optimization for Personalized Recommendations
3 METHODOLOGY
3.1 BanditLP
For ease of exposition, similar to [ 34], we assume that there are
three stakeholders in the multi-stakeholder ecosystem: the platform,
the provider (i.e., cohorts of items, sellers, business lines) and the
user, although our result is generalizable to more stakeholders. In
each round, the RS selects a set of items for each user. Let 𝑢=
1,···,𝑈 index users, 𝑖= 1,···,𝐼 index items, and 𝐿 be a set of
providers such that for each𝑖∈I 𝑙 the item𝑖 belongs to provider𝑙.
In each round𝑡= 1,...,𝑇 , the RS observes a contextual feature𝑧user 𝑢,𝑡
for a user𝑢, and𝑧item 𝑖,𝑡 for an item𝑖. If the RS recommends item𝑖
for user𝑢, it receives a set of feedback drawn from an unknown
distribution, where𝑟𝑢,𝑖,𝑡 =𝑟 𝑡(𝑧𝑢,𝑖,𝑡) with𝑧𝑢,𝑖,𝑡 =[𝑧 user 𝑢,𝑡 ;𝑧item 𝑖,𝑡 ] is
the primary reward representing a true-north business metric, and
{𝑐(𝑘) 𝑢,𝑖,𝑡 =𝑐(𝑘) 𝑡 (𝑧𝑢,𝑖,𝑡)}𝐾 𝑘=1 are𝐾 costs and secondary feedback relevant
to all stakeholders in the ecosystem.
We frame this multi-stakeholders problem as maximizing the
cumulative primary reward as the main objective subject to con-
straints that safeguard stakeholders’ interests in every round. We
can characterize the constraints in a three-stakeholder ecosystem
as:
• Platform-level constraints: a constraint involves feedback
for all users and items.
• Provider-level constraints: a constraint is calculated over
items belonging to each provider. This can also generalize
to include constraints calculated over users belonging to a
cohort.
• User-level (or item-level) constraints: a constraint is for
each user.
Some examples of platform-level constraint are total daily ads bud-
get for an ads platform, maximum unsubscription rate for an email
service, or minimum platform-wide revenue performance. This con-
straint is often found in safe bandit works [8, 30]. Some examples
of provider-level constraint are minimum percentage of promoted
products from each seller in an online marketplace, or maximum
deviation from a provider’s budget, which are often found as fair-
ness constraints in fair bandit works [31]. User-level constraint can
be the maximum number of recommendations a user may get [39],
or item-level constraint may be minimum number of selection or a
budget [18].
The goal is to design a policy that:
maximize𝑥𝑢,𝑖,𝑡
𝑇∑︁
𝑡=1
𝑈∑︁
𝑢=1
𝐼∑︁
𝑖=1
𝑥𝑢,𝑖,𝑡𝑟𝑢,𝑖,𝑡
subject to
∑︁
𝑢
∑︁
𝑖
𝑥𝑢,𝑖,𝑡𝑐(1) 𝑢,𝑖,𝑡≤𝐶 1∀𝑡,(1a)
∑︁
𝑢
∑︁
𝑖∈I𝑙
𝑥𝑢,𝑖,𝑡𝑐(2) 𝑢,𝑖,𝑡≤𝐶 2𝑙∀𝑙, 𝑡,(1b)
∑︁
𝑖∈𝐼
𝑥𝑢,𝑖,𝑡𝑐(3) 𝑢,𝑖,𝑡≤𝐶 3 ∀𝑢, 𝑡,(1c)
0≤𝑥 𝑢,𝑖,𝑡≤1∀𝑢, 𝑖, 𝑡
where𝑥𝑢,𝑖,𝑡 denotes the probability of selecting item𝑖 for user𝑢 at
time𝑡.
Algorithm 1:BanditLP
Input : Time horizon𝑇 ; providers𝑙= 1,...,𝐿 with item
index sets{I 𝑙}𝐿 𝑙=1 partitioning{1,...,𝐼};
three-stakeholders constraint thresholds𝐶 1,
{𝐶2𝑙}𝑙∈𝐿 ,𝐶 3.
Initialize :Initialize Bayesian neural networkse𝑟0(𝑧)and
{e𝑐(𝑘) 0 (𝑧)} 3 𝑘=1.
1forround𝑡=1to𝑇do
2foreach user𝑢=1,...,𝑈and item𝑖=1,...,𝐼do
3Observe contexts𝑧 𝑢,𝑖,𝑡 . Draw Thompson samples
from neural posterior predictive distributions
based on Laplace approximation:
b𝑟𝑢,𝑖,𝑡∼P𝑟
·

e𝑟𝑡−1(𝑧𝑢,𝑖,𝑡),D 1:𝑡−1 
b𝑐(𝑘) 𝑢,𝑖,𝑡∼P𝑘 ·

e𝑐(𝑘) 𝑡−1(𝑧𝑢,𝑖,𝑡),D 1:𝑡−1 ,∀𝑘
4Solve the LP:
maximize𝑥𝑢,𝑖,𝑡
∑︁
𝑢
∑︁
𝑖
𝑥𝑢,𝑖,𝑡 b𝑟𝑢,𝑖,𝑡
subject to
∑︁
𝑢
∑︁
𝑖
𝑥𝑢,𝑖,𝑡 b𝑐(1) 𝑢,𝑖,𝑡≤𝐶 1,
∑︁
𝑢
∑︁
𝑖∈I𝑙
𝑥𝑢,𝑖,𝑡 b𝑐(2) 𝑢,𝑖,𝑡≤𝐶 2𝑙 ∀𝑙,
∑︁
𝑖
𝑥𝑢,𝑖,𝑡 b𝑐(3) 𝑢,𝑖,𝑡 ≤𝐶 3 ∀𝑢,
0≤𝑥 𝑢,𝑖,𝑡≤1∀𝑢, 𝑖.
foreach user𝑢=1,...,𝑈do
5 Choose a set of items𝐴𝑢,𝑡 , where an item𝑖 is chosen
based on𝑥𝑢,𝑖,𝑡 .
6Observe feedback𝑟 𝑢,𝑖,𝑡,{𝑐 (𝑘) 𝑢,𝑖,𝑡}3 𝑘=1 for𝑖∈𝐴 𝑢,𝑡 .
7Update the Bayesian neural networkse𝑟 𝑡(𝑧)and
{e𝑐(𝑘) 𝑡 (𝑧)} 3 𝑘=1 using the new observations.
We observe that a satisfactory policy can be obtained by solv-
ing a subroutine linear program (LP) in every round. Specifically,
in the LP formulation, in the current round 𝑡, the goal is to max-
imize a primary business objective ˝ 𝑢 ˝ 𝑖𝑥𝑢,𝑖,𝑡𝑟𝑡(𝑧𝑢,𝑡,𝑖) , subject
to platform-level, provider-level, and user-level constraints as in-
cluded in (1a), (1b), (1c) respectively. As long as the number of
providers in𝐿is small, the problem is computationally feasible.
In practice, since the true𝑟𝑢,𝑖,𝑡,𝑐 (𝑘) 𝑢,𝑖,𝑡 are unknown, we assume
that they can be estimated via Bayesian neural networks (see Sec-
tion 3.2) e𝑟𝑡(𝑧𝑢,𝑖,𝑡) for the primary reward and e𝑐(𝑘) 𝑡 (𝑧𝑢,𝑖,𝑡) for the
costs and secondary reward. Exploration can be achieved through
Thompson sampling given neural posterior predictive distributions.
A policy satisfying the objective and constraints above can be com-
puted based on solving the LP with the estimated rewards and
costs [5]. After serving those recommendations, we update the es-
timatorse𝑟𝑡(𝑧),e𝑐(𝑘) 𝑡 (𝑧) to obtain improved utility value estimates
before the next round. We summarize BanditLP in Algorithm 1.

Phuc et al.
The proposed BanditLP method offers both versatility and scala-
bility, making it suitable for a wide range of real-world applications.
The multi-level constraint formulation generalizes numerous con-
strained bandit settings, encompassing item-level and group-level
fairness, campaign-level budget control, and global minimum safety
requirements, as well as arbitrary combinations of these. The neu-
ral Thompson sampling component can be paired with any neural
network architecture, while the LP layer is fully decoupled from
the prediction model, enabling flexible customization for diverse
objectives and constraints. From a scalability perspective, the LP
solver can efficiently handle billions of decision variables, and the
neural network component can model complex, high-dimensional
relationships. This modular architecture also supports incremen-
tal testing and staged deployment in production environments,
facilitating reliable integration into large-scale systems.
3.2 Neural Thompson Sampling
In this section, we briefly summarize our large-scale implementa-
tion of Bayesian neural networks to estimate unknown rewards and
costs functions𝑟𝑡(𝑧),{𝑐 (𝑘) 𝑡 (𝑧)}𝐾 𝑘=1. We quantify the uncertainty in
our estimators by approximating their intractable posteriors by
multivariate Gaussian via the Laplace approximation. Laplace ap-
proximations are widely used for uncertainty quantification in
recommendation system [9, 11, 16, 25, 33].
Let us assume that for an input 𝑧, we have a neural network
𝑓𝜃(𝑧) to predict the probability of a binary reward𝑟. Then under
linearized Laplace approximation (LLA) of [9, 11, 25], the posterior
predictive distribution for a new observation(𝑧∗,𝑟∗) in the binary
classification setup will be𝑃(𝑟 ∗ =1|z∗,D𝑡𝑟𝑎𝑖𝑛)=𝜎(𝜇(𝑧 ∗)),with
𝜇(𝑧∗)∼𝑁  𝑓b𝜃𝑀𝐴𝑃 (𝑧∗),𝜏𝑉 
𝑉:=𝜎 2 0+𝑔(𝑧∗)𝑇 Ω−1𝑔(𝑧∗)
Ω:=
𝑁∑︁
𝑛=1
𝑔(z𝑛)

∇2 𝑓 𝑙𝑜𝑔𝑝(r 𝑛|𝑓)

 𝑓=𝑓 b𝜃𝑀𝐴𝑃 (z𝑛) ! 𝑔(z𝑛)𝑇
where𝜏 is a temperature to scale the posterior covariance,𝑔(·) :=
∇𝜃𝑓𝜃(𝑧∗)|𝜃=b𝜃𝑀𝐴𝑃 ,∇2 𝑓 𝑙𝑜𝑔𝑝(𝑟 𝑛|𝑓) :=𝑒 𝑓/(1+𝑒𝑓)2,𝜎(·) is the sigmoid
function,Dtrain denotes the training data set, and𝜎2 0 is the variance
on the Gaussian prior on𝜃, and b𝜃𝑀𝐴𝑃 are network weights learned
from standard training with gradient descent.1
In our production scale settings, Ω is often too large to invert
directly, the literature focuses on lower dimensional approximation
such as top 𝑘 eigen-pairs of Ω[23], a diagonal matrix [ 40], sub-
network approximation that focuses on identifying a small subset
𝑆 of parameters [9] and use the sub matrix Ω𝑆,𝑆 to approximate Ω,
use thelast few layersof the network as the choice of 𝑆 [28, 32].
Our implementation adopts the last strategy.
For applications where a baseline supervised neural network
model exists, it may be desirable to be able to quickly deploy or
rollback on explore-exploit capability. Neural TS provides this ad-
vantage because we can apply LLA on a wide range of pre-trained
neural network [9]. We discuss practical tips to select the number
1For numeric reward or costs, we use Gaussian for posterior predictive distribution
and use the Gauss-Newton matrix for Hessian for regression task, see [11] for more
details.
of the last layers of the network, as well as tune and monitor degree
of exploration for web-scale applications in Section 3.4.2.
3.3 Large-scale Linear Program solver
To solve an LP with up to billions of variables, we turn toDuaLip[5,
26, 27], a large-scale LP solver developed here at LinkedIn. We
briefly outline the algorithm implemented in Dualip here. To begin,
for a given round 𝑡, observe that the LP in Section 3.1 in can be
written in the following form:
min
𝑥
𝑟⊤𝑥 𝑠.𝑡. 𝐷𝑥≤𝑏, 𝑥∈[0,1] 𝑈𝐼 ∀𝑢,𝑖,(3)
where𝑥=(𝑥 1,1,𝑡,···,𝑥 𝑈,𝐼,𝑡) ∈R|𝑈||𝐼| is the vector of decision
variables,𝑟=− 1 𝑟𝑡(𝑧1,𝑡,1)),·,𝑟 𝑡(𝑧𝑈,𝑡,𝐼) ∈R 𝑈𝐼 is the coefficient
vector for the decision variables in the objective,𝐷 is the design ma-
trix in the constraints,𝑏=(𝐶 1,𝐶 21,···,𝐶 2𝐿,𝐶 3)⊤ is the constraint
budget vector.
Instead of solving the LP in (3) directly, we solve a perturbed
version of the LP, which is a quadratic program (QP):
min
𝑥
𝑟⊤𝑥+ 𝛾 2𝑥⊤𝑥 𝑠.𝑡. 𝐷𝑥≤𝑏, 𝑥 𝑢,𝑖,𝑡∈[0,1] ∀𝑢,𝑖,
where𝛾> 0is a regularization hyperparameter. Dualizing just the
polytopal constraint𝐷𝑥≤𝑏leads to the partial Lagrangian dual
𝑔𝛾(𝜆)=min 𝑥
n
𝑟⊤𝑥+ 𝛾 2𝑥⊤𝑥+𝜆 ⊤(𝐷𝑥−𝑏) o ,
The problem is transformed to calculatemax𝜆𝑔𝛾(𝜆) such that𝜆≥ 0,
assuming strong duality holds. We can then solve the dual problem
efficiently using first-order methods, by using parallelizable projec-
tions. For sufficiently small𝛾, this yields the same solution as the
original LP. More details on DuaLip can be found in [5, 26, 27] and
tips for implementation can be found in [39].
3.4 Application in Email marketing at LinkedIn
3.4.1 Formulating the BanditLP problem.We now turn to a large-
scale application of BanditLP at LinkedIn: email marketing recom-
mendation. In email marketing at LinkedIn, we use batch inference
to make personalized, per-member send decisions at massive scale
across many campaigns, with decisions governed by eligibility and
frequency controls. The primary business objective is to maximize
total expected revenue subject to a global constraint on total mar-
keting unsubscriptions, as well as minimum business-line-level
selection and maximum member-level volume constraints each
week.
We apply the BanditLP formulation in Section 3.1 to this applica-
tion. Let𝑢= 1,···,𝑈 and𝑖= 1,···,𝐼 index users and campaigns
respectively. In any given week𝑡, conditional on context𝑧 𝑢,𝑖,𝑡 , we
estimate the primary reward for sending campaign𝑖 to member𝑢
as𝑦conv 𝑢,𝑖,𝑡·𝑦 LTV 𝑢,𝑖,𝑡 , where𝑦conv 𝑢,𝑖,𝑡 =𝑓 conv(𝑧𝑢,𝑖,𝑡) is an estimate for a short-
term reward measured by conversions, 𝑦LTV 𝑢,𝑖,𝑡 =𝑓 LTV(𝑧𝑢,𝑖,𝑡) is an
estimate for a long-term reward measured by life-time value (LTV)
associated with a conversion. We also estimate unsubscription as
𝑦unsub 𝑢,𝑖,𝑡 =𝑓 unsub(𝑧𝑢,𝑖,𝑡). Here𝑓 conv and𝑓 unsub are all estimated with
neural TS using LLA as described in Section 3.2, coupled with prob-
ability calibration. The 𝑓 LTV model is maintained by a separate
system and fitted by a supervised learning method.

BanditLP: Large-Scale Stochastic Optimization for Personalized Recommendations
Additionally, we have several constraints on the costs and send
decisions that must be satisfied weekly: i) the total unsubscrip-
tion should not be more than 𝐶unsub, ii) the minimum sends for
campaigns for B2B products must be𝐶⊭B, and the minimum sends
for campaigns for B2C products must be 𝐶2C, and iii) the maxi-
mum number of campaigns that can be sent to a user is𝐶 fcap. The
resulting BanditLP problem in each week is:
maximize𝑥𝑢,𝑖,𝑡
∑︁
𝑢
∑︁
𝑖
𝑥𝑢,𝑖,𝑡𝑦conv 𝑢,𝑖,𝑡 𝑦LTV 𝑢,𝑖,𝑡
subject to
∑︁
𝑢
∑︁
𝑖
𝑥𝑢,𝑖,𝑡𝑦unsub 𝑢,𝑖,𝑡 ≤𝐶 unsub,
∑︁
𝑢
∑︁
𝑖∈I 2B
−𝑥𝑢,𝑖,𝑡≤−𝐶 2B,
∑︁
𝑢
∑︁
𝑖∈I 2C
−𝑥𝑢,𝑖,𝑡≤−𝐶 2C,
∑︁
𝑖
𝑥𝑢,𝑖,𝑡≤𝐶 fcap ∀𝑢,
0≤𝑥 𝑢,𝑖,𝑡≤1∀𝑢, 𝑖
Notice that the action probability variable𝑥 has dimension𝑈𝐼 , the
product of the number of members and the number of campaigns,
which can result in tens of billions of variables. We useDuaLipto
solve for𝑥𝑢,𝑖,𝑡 , the probability of sending campaign𝑖 to user𝑢 in
week𝑡. The main parameter to tune is𝛾, which controls the trade-
off between speed and precision of the solver. Prior works [5, 39]
have discussed practical tips for implementing and tuning𝛾 that
also work well in our application. Figure 1 shows the overview of
the email marketing recommender based on BanditLP.
Member
features
Campaign
features Constraints
LPConversion model
Unsubscription
model
LTV model
Probability
calibration
Probability
calibration
Labels Environment
Batch decisions
Rewards, costs
Figure 1: Overview of email marketing recommender system
based on BanditLP at LinkedIn.
3.4.2 Tuning and monitoring the degree of exploration.We describe
practical tips for tuning neural TS when its outputs feed an LP. First,
the temperature parameter𝜏 controls the exploration–exploitation
trade-off. Because TS samples pass through an LP with complex
constraints, doubling𝜏 does not necessarily double the effective
exploration downstream. We therefore propose anoverlap-at- 𝐾
metric to measure the realized degree of exploration:
Overlap-at-𝐾= 1 𝑁 𝑁∑︁ 𝑛=1

𝑆TS 𝑛 (𝐾)∩𝑆 exploit 𝑛 (𝐾)

 𝐾 ,
where𝑁 is the number of observations, and𝑆TS 𝑛 (𝐾) and𝑆exploit 𝑛 (𝐾)
denote the top-𝐾 actions for observation 𝑛 under the neural-TS
policy and the same neural model without exploration, respectively.
The metric quantifies how often the 𝐾 actions chosen by the TS
policy agree with those from the exploit-only policy; values closer
to1indicate less exploration.
For our application, we set 𝐾=𝐶 fcap and choose a target
𝑝safe ∈ (0, 1). We then grid-search over 𝜏 to achieve overlap-at-
𝐾≥𝑝 safe prior to deployment. Second, during model update,
overlap-at-𝐾 also serves to monitor distribution shift in model
scores after refreshes, providing a safety check on exploration.
Finally, we select the largest suffix of layers used for posterior-
uncertainty approximation that still satisfies training and serving
latency requirements.
30
 20
 10
 0 10 20 30
logit(p)
0
500
1000
1500
2000
2500
3000Frequency
Original
NN
NNTS
30
 20
 10
 0 10 20 30
logit(p)
0
1000
2000
3000
4000
5000
Calibration with heuristic
calibrated NN
well-calibrated
NNTS
30
 20
 10
 0 10 20 30
logit(p)
0
1000
2000
3000
4000
5000
6000
7000
Naive calibration
calibrated NN
badly-calibrated
NNTS
Figure 2: Calibration heuristic preserves exploration.
3.4.3 Calibrating neural Thompson sampled probabilities.In our
application, conversions and unsubscriptions are extremely rare,
and negative labels are down-sampled for training. Thus, probabil-
ity calibration is critical when predicted probabilities are used as
inputs to an LP: the solver interprets these probabilities as quantita-
tive values that directly constrain and guide optimization. We use
an off-the-shelf isotonic regression, a non-parametric calibration
technique that fits a monotone stepwise function mapping raw
model scores to calibrated probabilities.
Because uncertainty from the neural network cannot be directly
propagated through isotonic regression, we adopt a practical heuris-
tic. First, we fit a calibration model𝑔 using predicted probabilities
without exploration b𝑝and observed binary rewards𝑟:
𝑔=arg min
𝑔∈M
𝑁∑︁
𝑖=1
𝑟𝑖−𝑔( b𝑝𝑖)2,
whereM denotes the space of monotone stepwise functions. At
serving time, we obtain calibrated TS probabilities by applying𝑔 to
the Thompson-sampled predictions: e𝑝 TS =𝑔 b𝑝 TS, where b𝑝 TS are
the model’s TS probabilities prior to calibration.
If we instead fit isotonic regression directly on TS probabilities,
we observe a counterintuitive effect: increasing the temperature
𝜏 yields amoreconcentrated distribution of calibrated probabili-
ties. This arises because isotonic regression shrinks noisy TS draws
toward a monotone mean function, effectively dampening explo-
ration. Figure 2 illustrates this anti-exploration behavior for naive
TS calibration and the improvement under the proposed heuristic.
4 EXPERIMENTS
4.1 Offline experiment
4.1.1 Baseline methods.We compare BanditLP against standard
contextual bandit methods and multi-objective recommender sys-
tem without exploration. To our knowledge, there is no other work

Phuc et al.
the combines a contextual bandit with an LP sub-routine for multi-
stakeholders setting:
• NNTS: a contextual bandit with strong predictive power
using neural Thompson sampling but does not enforce con-
straints.
• LinUCB-LP: an extension of LinUCB, a classical contextual
bandit, by enforcing constraints during action selection by
solving the LP in (3), thereby satisfying constraints in each
round. However, LinUCB is limited in modeling complex
(nonlinear) reward and cost functions.
• NN-LP: a supervised baseline that uses neural networks for
deterministic predictions and solves the LP in (3) during
action selection (no exploration).
4.1.2 Datasets.We evaluate BanditLP on both a public benchmark
and a synthetic dataset. The synthetic dataset allows us to select the
number of constraints affecting the LP, the number of providers, and
other characteristics of the recommendation problem. We generate
random user and item features, assign items to mutually exclusive
sets (providers), and define reward and costs as functions of user
and item features. Appendix A.1 details the data-generation process.
For the public benchmark, we use the Open Bandit Dataset
(OBD) [ 29], a real-world logged bandit dataset. We utilize the
random-policy subset, where 34 products were randomly recom-
mended to > 400K users with binary click feedback. While OBD
natively supports off-policy evaluation via the replay method, to
enable efficient optimization of the LP sub-routine we construct an
imputed reward matrix. Specifically, we randomly sample 10K users
and fill unobserved user–item rewards using𝐾-Nearest Neighbors
(𝐾=10): for each unseen item, we identify the 10 most similar users
who interacted with it, compute their average CTR, and draw a
Bernoulli sample accordingly. The resulting dense reward matrix
serves as a controlled proxy for simulation studies and makes the
LP tractable. We use the imputed clicks as the reward. We define
synthetic costs similarly to the synthetic dataset. We also assign
products evenly to disjoint sets (providers).
4.1.3 Evaluation setup.All models are initialized using training
data collected by abiased logging policythat selects items from a
restricted region of the feature space. This reflects selection bias
common in real-world RS (e.g., “rich-get-richer”) and cold-start
effects for new items. Details for the synthetic setup appear in
Appendix A.1. For the OBD benchmark, the biased logging policy
only recommends the top30%items uniformly at random.
To set constraints, we run a random policy and record its global
and per-set costs, then set constraint targets as multipliers of these
baselines. Intuitively, global costs may be targeted below a random
policy (e.g.,70%), while per-set costs (e.g., fairness exposure) may be
bounded relative to a perfectly balanced random policy (e.g., within
20%). For𝑇 rounds, each model interacts with the environment by
selecting actions for a set of users and items, observing rewards and
costs, and updating via incremental training on its own feedback.
We repeat the simulation for𝑆 runs and report mean global reward,
global-constraint violation, and per-set constraint violation with
95%confidence intervals over all rounds. For the synthetic dataset,
we set𝑇=30, 𝑆=50, and for the OBD benchmark, we set𝑇=50, 𝑆=20.
Figure 3: Synthetic experiments. Top: cumulative reward over
rounds. Middle: global constraint violation (no violation if
≤ 0). Bottom: provider-level constraint violations across item
sets (no violation if≤ 0). Shaded regions show 95% CIs over
50 runs.
4.1.4 Results.BanditLP method combines predictive accuracy
with exploration and constraint satisfaction. Across both datasets,
it achieves the bestreward–feasibilitytrade-off, maintaining viola-
tions near or below zero while delivering high reward (see Figure 3
and Figure 4). When the logged data to initialize the reward and
costs models have selection bias, NNLP policy plateaus early as de-
terministic exploitation cannot escape selection-bias traps, yielding
lower reward in the long-run. As expected, NNTS policy, which
does not have an LP sub-routine, attains the highest reward but con-
sistently violates global and per-set constraints. LinUCB-LP policy
underperforms in reward while at the same time shows global con-
straint violation. Because the LP is solved using estimated rewards
and costs, LinUCB’s limited expressiveness to model non-linear
cost functions leads to constraint misspecification and violations.
4.2 Online experiment
4.2.1 Design.We design an online A/B test to compare the perfor-
mance of the BanditLP email marketing RS described in Section 3.4
against a fully exploitative baseline. The control is a RS that only
utilizes the same supervised learning models for 𝑓 conv,𝑓 unsub,𝑓 LTV
but without Thompson sampling, and an LP to optimize for business
constraints. The experiment therefore isolates BanditLP’s ability to
induce exploration in the LP solutionsby injecting uncertainty into
the estimated rewards and costs that enter the LP.

BanditLP: Large-Scale Stochastic Optimization for Personalized Recommendations
Figure 4: Open Bandit Dataset (imputed matrix) experiments.
Top: cumulative reward over rounds. Middle: global con-
straint violation (no violation if≤ 0). Bottom: provider-level
constraint violations across item sets (no violation if ≤ 0).
Shaded regions show 95% CIs over 20 runs.
Because the email marketing system only covers a small per-
centage of all LinkedIn users, we carefully define the experiment
population to reduce effect dilution. Rather than include all mem-
bers, we restrict the population to the union of users who are
eligible for weekly email recommendations during the test period.
Concretely, we first assign all users to treatment or control, with
assignments fixed for the duration of the experiment. Each week,
when the set of eligible users is produced, those users are routed to
their preassigned policy. For analysis, we include only users who
were actually served by either the control or BanditLP RS during
the experiment window.
Additionally, to avoid data leakage when A/B-testing a RS with-
out exploration against one with exploration, we use a data-diverted
experiment setup similar to [33]. Specifically, users random treat-
ment assignments are enforced in both training and serving. Be-
fore launching the experiment, we train both RSs only on pre-
experiment logs. During the experiment period, each RS may up-
date using only data collected from its own cohort. This ensures
there is no cross-learning and leaking the benefit of exploration
from the treatment to the control policy. Figure 5 illustrates the
data-diverted experiment setup. We run the experiment for seven
weeks, during which both the control and BanditLP RSs update
on a weekly cadence with new interactions and feedback from the
environment. This ensures the experiment can measure the effect
of exploration on model learning.
Users Policies
Data Collection Policy Evaluation
Control cohort
Treatment
cohort
Baseline
policy
BanditLP
policy
Policy quality
comparison
Figure 5: Data-diverted experiment setup to measure benefits
of exploration.
We track revenue as the long-term, true north business metric,
conversion rate as a short-term signal for reward, and unsubscrip-
tion rate as our guardrail metric. In terms of statistical analysis, it is
worth noting that the long-term revenue metric has zero inflation
and heavy tail [39]. Thus, we use the two-sample𝑡-tests (Welch’s) as
well as consider nonparametric zero-truncated tests [38] to robustly
detect changes in this metric.
Table 1: Result of Online A/B Test
Metric Relative improvement (95%CI)
Revenue+3.08%(+0.17%,+5.99%)
Conversion rate−0.01%(−0.26%,+0.23%)
Unsubscription rate−1.51%(−2.25%,−0.72%)
4.2.2 Results.The A/B test results using two-sample 𝑡-tests (Ta-
ble 1) show BanditLP produces statistically significant positive lift
in long-term revenue metric (+3.08%), and statistically significant
reduction in unsubscription rate (−1.51%). The short-term reward
metric, conversion rate, shows a very small and not statistically
significant change (−0.01%). This is interesting because it suggests a
trade-off between short-term and long-term gains: exploration may
not immediately increase conversions, but it leads to higher sus-
tained revenue over time. Additionally, the results show, by adding
exploration to the estimates of rewards and costs using neural TS,
BanditLP can effectively induce exploration in the LP solutions
4.3 Ablation analysis
Beyond demonstrating BanditLP’s effectiveness in production via
an online A/B test, we conduct ablation studies to measure its
sensitivity to the quality of the rewards and costs estimators and
levels of exploration. We seek to address the broad question: How
will the LP behave given different estimators quality? In these
analyses, we use our email marketing formulation for illustration.
We simulate BanditLP in a single round across varying levels of
exploration𝜏 and prediction model quality𝑞. We generate realistic
ground truth data and then model the data using varying degrees
of model quality and exploration levels. For each pair (𝑞,𝜏) of
model quality and exploration level, we solve the LP, obtaining an
allocation decision and associated downstream quantities. Precise
details of the simulation setup are provided in Appendix B.
We seek to answer the following research questions:

Phuc et al.
RQ1: What risks are introduced to constraints satisfaction due to
exploration and model quality?
RQ2: How does exploration affect the stability of the LP’s alloca-
tion decision?
Figure 6: Relative unsubscription change under increasing
degrees of exploration.
RQ1 (Constraint Satisfaction).Figure 6 shows relative unsub-
scription change RUC(𝑞,𝜏)=
¯U(𝑞,𝜏)− ¯U(𝑞,0)
¯U(𝑞,0) · 100%. Unsubscriptions
remain stable (within±2% of baseline) across all configurations,
indicating the constraint remains effectively binding despite explo-
ration noise.
Figure 7: Total allocation variance change under increasing
degrees of exploration.
RQ2 (Allocation Stability).Figure 7 shows allocation vari-
ance AV(𝑞,𝜏)= 1 |U||I| ˝ 𝑢,𝑖 Var𝑋𝑢,𝑖 . Variance increases with ex-
ploration, with high-quality models showing greater sensitivity.
This occurs because low-quality models already contain substantial
baseline instability, making exploration’s marginal contribution
relatively small.
5 CONCLUSION AND FUTURE WORK
This work introduces a general algorithm for multi-stakeholder con-
textual bandits that combines neural Thompson Sampling with a
large-scale linear program to maximizing a primary reward subject
to constraints that safeguard stakeholders’ interests in every round.
All objectives are first estimated and sampled via neural TS, and
the final recommendations are chosen by a decoupled LP that en-
forces stakeholders’ constraints at scale. The system is application-
agnostic, compatible with arbitrary deep learning architecture to
estimate rewards and costs, supports a rich set of constraints, and
scales to billions of recommendations. We validate the approach
on public benchmarks and synthetic data against established base-
lines. In production, we demonstrate BanditLP’s strengths in an
application to LinkedIn email marketing system, balancing users,
business lines, and platform goals under real constraints. The ap-
plication delivers business impact through online A/B test. We
describe deployment lessons such as probability calibration, tuning
and scaling neural TS, improving LP convergence, and setting up
bandit experiment to avoid data leakage.
The current formulation assumes no interaction effects across
marketing units, and performance relies on accurately calibrated
predictions feeding the LP. Moreover, end-to-end behavior depends
on solver throughput and feasibility under tight constraints. Future
work includes real-time inference and online learning to close the
loop continuously in production, further automation of calibration
and diagnostics for stability at scale, and extending the method
to broader recommender settings and constraint families while
preserving the separation between learning and optimization.
Acknowledgments
We thank Licurgo Benemann De Almeida, Kenneth Tay, John
Bencina, Shruti Sharma, Rajni Sharma, Sumukh Sagar Manjunath,
Curtis Seaton, Shawn Bianchi, and Alyssa Falk for their support
and collaboration on the email application and A/B test.
References
[1] Robin Allesiardo, Raphaël Féraud, and Djallel Bouneffouf. 2014. A neural net-
works committee for the contextual bandit problem. InInternational Conference
on Neural Information Processing. Springer, 374–381.
[2] Sanae Amani, Mahnoosh Alizadeh, and Christos Thrampoulidis. 2019. Linear
stochastic bandits under safety constraints.Advances in Neural Information
Processing Systems32 (2019).
[3] Ashwinkumar Badanidiyuru, Robert Kleinberg, and Aleksandrs Slivkins. 2018.
Bandits with knapsacks.Journal of the ACM (JACM)65, 3 (2018), 1–55.
[4] Yikun Ban, Yuchen Yan, Arindam Banerjee, and Jingrui He. 2022. Ee-net:
Exploitation-exploration neural networks in contextual bandits.10th Inter-
national Conference on Learning Representations(2022).
[5] Kinjal Basu, Amol Ghoting, Rahul Mazumder, and Yao Pan. 2020. ECLIPSE:
An extreme-scale linear program solver for web-applications. InInternational
Conference on Machine Learning. PMLR, 704–714.
[6] Djallel Bouneffouf, Irina Rish, and Charu Aggarwal. 2020. Survey on applications
of multi-armed and contextual bandits. In2020 IEEE congress on evolutionary
computation (CEC). IEEE, 1–8.
[7] Róbert Busa-Fekete, Balázs Szörényi, Paul Weng, and Shie Mannor. 2017. Multi-
objective bandits: Optimizing the generalized gini index. InInternational Confer-
ence on Machine Learning. PMLR, 625–634.
[8] Samuel Daulton, Shaun Singh, Vashist Avadhanula, Drew Dimmery, and Eytan
Bakshy. 2019. Thompson sampling for contextual bandit problems with auxiliary
safety constraints.arXiv preprint arXiv:1911.00638(2019).
[9] Erik Daxberger, Agustinus Kristiadi, Alexander Immer, Runa Eschenhagen,
Matthias Bauer, and Philipp Hennig. 2021. Laplace redux-effortless bayesian
deep learning.Advances in neural information processing systems34 (2021),
20089–20103.
[10] Yulong Dong, Kun Jin, Xinghai Hu, and Yang Liu. 2024. Measuring fairness
in large-scale recommendation systems with missing labels.arXiv preprint
arXiv:2406.05247(2024).
[11] Andrew YK Foong, Yingzhen Li, José Miguel Hernández-Lobato, and Richard E
Turner. 2019. ’In-Between’Uncertainty in Bayesian Neural Networks.arXiv
preprint arXiv:1906.11537(2019).
[12] Lin Ge, Yang Xu, Jianing Chu, David Cramer, Fuhong Li, Kelly Paulson, and Rui
Song. 2025. Multi-task combinatorial bandits for budget allocation. InProceedings

BanditLP: Large-Scale Stochastic Optimization for Personalized Recommendations
of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.
1. 2247–2258.
[13] Sahin Cem Geyik, Stuart Ambler, and Krishnaram Kenthapadi. 2019. Fairness-
aware ranking in search & recommendation systems with application to linkedin
talent search. InProceedings of the 25th acm sigkdd international conference on
knowledge discovery & data mining. 2221–2231.
[14] Hengquan Guo, Lingkai Zu, and Xin Liu. 2025. Triple-Optimistic Learning
for Stochastic Contextual Bandits with General Constraints. InForty-second
International Conference on Machine Learning.
[15] Pavithra Harsha, Chitra Subramanian, Naoki Abe, Shivaram Subramanian,
Amadou Ba, Kevin Arturo Fernández Román, Mauricio Longinos Garrido, and
Chandrasekhar Narayanaswami. 2025. Practical Contextual Bandits for Large-
Scale Structured Discrete Constrained Optimization Problems. InProceedings of
the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2.
850–859.
[16] Thorsten Joachims, Adith Swaminathan, and Maarten De Rijke. 2018. Deep
learning with logged bandit feedback. InInternational Conference on Learning
Representations.
[17] Kia Khezeli and Eilyan Bitar. 2020. Safe linear stochastic bandits. InProceedings
of the AAAI Conference on Artificial Intelligence, Vol. 34. 10202–10209.
[18] Fengjiao Li, Jia Liu, and Bo Ji. 2019. Combinatorial sleeping bandits with fairness
constraints.IEEE Transactions on Network Science and Engineering7, 3 (2019),
1799–1813.
[19] Lihong Li, Wei Chu, John Langford, and Robert E Schapire. 2010. A contextual-
bandit approach to personalized news article recommendation. InProceedings of
the 19th international conference on World wide web. 661–670.
[20] Shang Liu, Jiashuo Jiang, and Xiaocheng Li. 2022. Non-stationary bandits with
knapsacks.Advances in Neural Information Processing Systems35 (2022), 16522–
16532.
[21] Haihao Lu, Duncan Simester, and Yuting Zhu. 2025. Optimizing scalable targeted
marketing policies with constraints.Marketing Science(2025).
[22] Rishabh Mehrotra, Niannan Xue, and Mounia Lalmas. 2020. Bandit based opti-
mization of multiple objectives on a music streaming platform. InProceedings of
the 26th ACM SIGKDD international conference on knowledge discovery & data
mining. 3224–3233.
[23] Geir K Nilsen, Antonella Z Munthe-Kaas, Hans J Skaug, and Morten Brun. 2022.
Epistemic uncertainty quantification in deep learning classification by the Delta
method.Neural networks145 (2022), 164–176.
[24] Lijing Qin, Shouyuan Chen, and Xiaoyan Zhu. 2014. Contextual combinatorial
bandit and its application on diversified online recommendation. InProceedings
of the 2014 SIAM International Conference on Data Mining. SIAM, 461–469.
[25] Swarnali Raha, Kshitij Khare, and Rohit K Patra. [n. d.]. Computationally Efficient
Laplace Approximations for Neural Networks. InNeurIPS 2024 Workshop on
Bayesian Decision-making and Uncertainty.
[26] Rohan Ramanath, Sathiya S Keerthi, Kinjal Basu, Konstantin Salomatin, Pan
Yao, Amol Ghoting, and Miao Cheng. 2022. DuaLip: Dual Decomposition based
Linear Program Solver, version 2.0.0. https://github.com/linkedin/dualip
[27] Rohan Ramanath, S Sathiya Keerthi, Yao Pan, Konstantin Salomatin, and Kinjal
Basu. 2022. Efficient vertex-oriented polytopic projection for web-scale appli-
cations. InProceedings of the AAAI Conference on Artificial Intelligence, Vol. 36.
3821–3829.
[28] Carlos Riquelme, George Tucker, and Jasper Snoek. 2018. Deep bayesian bandits
showdown. InInternational conference on learning representations, Vol. 9.
[29] Yuta Saito, Shunsuke Aihara, Megumi Matsutani, and Yusuke Narita. 2020. Open
bandit dataset and pipeline: Towards realistic and reproducible off-policy evalu-
ation.arXiv preprint arXiv:2008.07146(2020).
[30] Vidit Saxena, Joakim Jalden, and Joseph Gonzalez. 2020. Thompson sampling for
linearly constrained bandits. InInternational Conference on Artificial Intelligence
and Statistics. PMLR, 1999–2009.
[31] Akruti Sinha, Devika Sapra, Deepak Sinwar, Vijander Singh, and Ghanshyam
Raghuwanshi. 2024. Assessing and mitigating bias in artificial intelligence: a
review.Recent Advances in Computer Science and Communications (Formerly:
Recent Patents on Computer Science)17, 1 (2024), 1–10.
[32] Jasper Snoek, Oren Rippel, Kevin Swersky, Ryan Kiros, Nadathur Satish,
Narayanan Sundaram, Mostofa Patwary, Mr Prabhat, and Ryan Adams. 2015.
Scalable bayesian optimization using deep neural networks. InInternational
conference on machine learning. PMLR, 2171–2180.
[33] Yi Su, Xiangyu Wang, Elaine Ya Le, Liang Liu, Yuening Li, Haokai Lu, Benjamin
Lipshitz, Sriraj Badam, Lukasz Heldt, Shuchao Bi, et al. 2024. Long-term value of
exploration: measurements, findings and algorithms. InProceedings of the 17th
ACM International Conference on Web Search and Data Mining. 636–644.
[34] Özge Sürer, Robin Burke, and Edward C Malthouse. 2018. Multistakeholder
recommendation with provider constraints. InProceedings of the 12th ACM
Conference on Recommender Systems. 54–62.
[35] Adith Swaminathan and Thorsten Joachims. 2015. Batch learning from logged
bandit feedback through counterfactual risk minimization.The Journal of Ma-
chine Learning Research16, 1 (2015), 1731–1755.
[36] Cem Tekin and Eralp Turğay. 2018. Multi-objective contextual multi-armed
bandit with a dominant objective.IEEE Transactions on Signal Processing66, 14
(2018), 3799–3813.
[37] Lu Wang, Chengyu Wang, Keqiang Wang, and Xiaofeng He. 2017. Biucb: A
contextual bandit algorithm for cold-start and diversified recommendation. In
2017 IEEE international conference on big knowledge (ICBK). IEEE, 248–253.
[38] Changshuai Wei, Phuc Nguyen, Benjamin Zelditch, and Joyce Chen. 2025. Beyond
Basic A/B testing: Improving Statistical Efficiency for Business Growth.arXiv
preprint arXiv:2505.08128(2025).
[39] Changshuai Wei, Benjamin Zelditch, Joyce Chen, Andre Assuncao Silva T Ribeiro,
Jingyi Kenneth Tay, Borja Ocejo Elizondo, Sathiya Keerthi Selvaraj, Aman Gupta,
and Licurgo Benemann De Almeida. 2024. Neural optimization with adaptive
heuristics for intelligent marketing system. InProceedings of the 30th ACM
SIGKDD Conference on Knowledge Discovery and Data Mining. 5938–5949.
[40] Weitong Zhang, Dongruo Zhou, Lihong Li, and Quanquan Gu. 2020. Neural
thompson sampling.arXiv preprint arXiv:2010.00827(2020).
[41] Xiaoying Zhang, Hong Xie, Hang Li, and John CS Lui. 2020. Conversational
contextual bandit: Algorithm and application. InProceedings of the web conference
2020. 662–672.
[42] Dongruo Zhou, Lihong Li, and Quanquan Gu. 2020. Neural contextual bandits
with ucb-based exploration. InInternational conference on machine learning.
PMLR, 11492–11502.
[43] Zheqing Zhu and Benjamin Van Roy. 2023. Scalable neural contextual bandit for
recommender systems. InProceedings of the 32nd ACM International Conference
on Information and Knowledge Management. 3636–3646.
A Offline experiment
A.1 Synthetic experiment setup
Here we describe in detail the synthetic data generation setup for
offline experiments in Section 4.1. We set number of user each
round to𝑈= 500, and number of items (fixed) to 𝐼= 100, with
items assigned to 𝐿= 5disjoint sets of items. To generate a
multi-stakeholder contextual bandit problem, at each round, we
sample user features 𝑧𝑢 ∼𝑁( 0,𝐼), 𝑧𝑢 ∈R 𝑑𝑢 and item features
𝑧𝑖 ∼𝑁( 0,𝐼), 𝑧𝑖 ∈R 𝑑𝑖 , with 𝑑𝑢 =𝑑 𝑖 = 10. The true dominant
reward and cost functions are:
𝑟𝑢,𝑖∼𝑁(𝜇 𝑟(𝑧⊤ 𝑢𝛽𝑢+𝑧⊤ 𝑖 𝛽𝑖), 𝜎2 𝑟),
𝑐(1) 𝑢,𝑖 ∼𝑁(𝜇 𝑐(𝑧⊤ 𝑢𝛽(1) 𝑢 +𝑧⊤ 𝑖 𝛽(1) 𝑖 ), 𝜎2 𝑐),
𝑐(2) 𝑢,𝑖 ∼𝑁(𝜇 𝑐(𝑧⊤ 𝑢𝛽(2) 𝑢 +𝑧⊤ 𝑖 𝛽(2) 𝑖 ), 𝜎2 𝑐)
where the reward is centered around a sum of sigmoids of linear
transformations of the features 𝜇𝑟(𝑣) :=𝜎(− 4𝑣+ 5)+ 5𝜎( 5𝑣+
5)+ 0.1 sin(2𝑣),, and the costs are centered around 𝜇𝑐(𝑣) := 1+
0.1 tanh(𝑣/ 2). We set 𝜎2 𝑟 =𝜎 2 𝑐 = 0.1, and sample linear weights
𝛽𝑢,𝛽𝑖,𝛽(1) 𝑢 ,𝛽(2) 𝑢 ,𝛽(1) 𝑖 ,𝛽(2) 𝑖 ∼𝑁(0,0.6 2).
We implement the biased logging initial policy as selecting ac-
tions with𝑧⊤ 𝑢𝛽𝑢+𝑧⊤ 𝑖 𝛽𝑖 < 0uniformly at random. We set user-level
constraint to be2. We simulate the global and per-set constraints by
first running a random policy that selects up to two item for 5000
users, producing a set𝐴𝑟𝑎𝑛𝑑𝑜𝑚 . We then calculate the global con-
straint as𝐶1 = 0.8˝5000 𝑢=1 ˝ 𝑖𝑐(1) 𝑢,𝑖 1𝑢,𝑖∈𝐴𝑟𝑎𝑛𝑑𝑜𝑚 and per-set constraints
as𝐶 2𝑙 =1.5 ˝5000 𝑢=1 ˝ 𝑖𝑐(2) 𝑢 1𝑢,𝑖∈𝐴𝑟𝑎𝑛𝑑𝑜𝑚 .
B Ablation and sensitivity analysis
Here we describe in detail the ablation simulation and analysis. We
first simulate how different levels of exploration affect LP allocation
decisions in a single period, across varying levels of prediction
model quality𝑞. We generate synthetic data under the following

Phuc et al.
mechanism:
pConv𝑢,𝑖∼Beta(2,18)·10 −2,
pUnsub𝑢,𝑖∼Beta(1,9)·10 −1,
LTV𝑢,𝑖∼Gamma(2,150).
We think of these as the true, unknown values that we estimate via
prediction models.
Second, we generate model predictions for these ground truth
values, which are noisy estimates of them. We introduce four model
qualities𝑞, each of which has an associated noise parameter 𝜎𝑞
(higher quality models have lower noise parameter values). The
model predictions are given by:
logit( pConv 𝑞 𝑢,𝑖)=logit(pConv 𝑢,𝑖)+𝜖 𝑞, 𝜖 𝑞∼N(0,𝜎 2 𝑞)
And similarly for pUnsub 𝑞 𝑢,𝑖.
Third, given the model predictions, we compute the prediction
uncertainties:𝑈𝑞 Conv𝑢,𝑖 =𝜏𝛾| pConv 𝑞 𝑢,𝑖−pConv𝑢,𝑖|+𝛾 0. In practice
we would need to estimate these uncertainties as well. Given them,
we obtain the explored/perturbed predictions:
pConv𝑢,𝑖∼Beta 𝛼𝑞 Conv,𝛽𝑞 Conv ,
where𝛼𝑞 Conv = pConv·𝑛 Conv,𝛽𝑞 Conv =( 1− pConv)·𝑛 Conv, and
𝑛Conv =
pConv(1− pConv)
(𝑈𝑞 Conv𝑢,𝑖)2 − 1. These choices ensure E
h
pConv𝑢,𝑖
i
=
pConv and Var

pConv𝑢,𝑖

≈ (𝑈𝑞 Conv𝑢,𝑖)2. Here 𝜏 is a parameter
which controls the degree of exploration (higher𝜏 leads to more
exploration). And similarly for unsubscription probabilities.
The LP we solve is:
maximize𝑥𝑢,𝑖
∑︁
𝑢∈U
∑︁
𝑖∈I
𝑥𝑢,𝑖 pConv 𝑞 𝑢,𝑖 LTV𝑢,𝑖
subject to
∑︁
𝑢∈U
∑︁
𝑖∈I
𝑥𝑢,𝑖 pUnsub 𝑞 𝑢,𝑖≤ e𝐶,
∑︁
𝑖∈I
𝑥𝑢,𝑖≤1∀𝑢,
𝑥𝑢,𝑖≥0∀𝑢,𝑖
The solution of this LP is an allocation decision D(𝑞,𝜏)=
{𝑥D(𝑞,𝜏) 𝑢,𝑖 } that is a function of both the model quality 𝑞 and the
degree of exploration𝜏. The allocation decisionD(𝑞, 0) is the solu-
tion we obtain under no exploration and serves as a baseline. As
we vary the two parameters, we explore the behavior ofD(𝑞,𝜏)
and key downstream quantities:
R(𝑞,𝜏)=
∑︁
𝑢∈U
∑︁
𝑖∈I
pConv𝑢,𝑖 LTV𝑢,𝑖𝑥D(𝑞,𝜏) 𝑢,𝑖 ,
U(𝑞,𝜏)=
∑︁
𝑢∈U
∑︁
𝑖∈I
pUnsub𝑢,𝑖𝑥D(𝑞,𝜏) 𝑢,𝑖 .
These are total expected revenue and total expected unsubscrip-
tions, respectively. Across multiple simulation runs, we also explore
stability quantities such as:
AV(𝑞,𝜏)= 1 |U||I| ∑︁ 𝑢∈U ∑︁ 𝑖∈I Var  𝑥D(𝑞,𝜏) 𝑢,𝑖  This is the total average allocation variance of D(𝑞,𝜏) across
multiple runs.
