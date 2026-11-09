---
title: 'HMAF: A Hierarchical Multi-Slot GD-RTB Allocation Framework'
url: https://arxiv.org/abs/2606.09896
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Tianxing Bu
- Zhaoqi Zhang
- Linyou Cai
- Miao Xie
- Shengri Xue
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.09896
pages: 10
chars: 49789
fetched_at: '2026-11-08T13:05:41+00:00'
kb_version: 1
---

# HMAF: A Hierarchical Multi-Slot GD-RTB Allocation Framework

HMAF: A Hierarchical Multi-Slot GD-RTB Allocation Framework
Tianxing Bu
Meituan
Beijing, China
butianxing@meituan.com
Zhaoqi Zhang∗
Nanyang Technological University
Singapore
zhaoqi001@e.ntu.edu.sg
Linyou Cai
Meituan
Beijing, China
cailinyou@meituan.com
Miao Xie
China Agricultural University
Beijing, China
xiemiao@cau.edu.cn
Shengri Xue
Meituan
Beijing, China
xueshengri@meituan.com
Tan Qu
Meituan
Beijing, China
qutan@meituan.com
Qianlong Xie
Meituan
Beijing, China
xieqianlong@meituan.com
Xingxing Wang
Meituan
Beijing, China
wangxingxing04@meituan.com
Siqiang Luo
Nanyang Technological University
Singapore
siqiang.luo@ntu.edu.sg
Gao Cong
Nanyang Technological University
Singapore
gaocong@ntu.edu.sg
Abstract
In modern online advertising platforms, Guaranteed Delivery (GD)
contracts coexist and bid with Real-Time Bidding (RTB) auctions.
Recent approaches either decouple GD and RTB optimization or rely
on heuristic priority rules, and thus fail to effectively balance short-
term revenue maximization with long-term contract delivery under
complex multi-slot delivery and impression constraints. To address
these challenges, we propose HMAF (Hierarchical Multi-Slot Al-
location Framework), a unified framework designed to optimize
impression allocation in GD-RTB advertising platforms. HMAF
employs thePlan–Calibrate–Executeparadigm as its core struc-
ture, and integrates offline constraint optimization with online
decision-making, balancing offline GD resource planning, dynami-
cally calibrating GD-RTB competitiveness, and making real-time
listwise rank decisions across multi-slot environments. HMAF has
been implemented in multiple marketing scenarios at Meituan, one
of the world’s largest online food delivery platforms, leading to
a 3.72% increase on GD delivery rate and 1.59% increase on total
advertisement revenue.
CCS Concepts
•Information systems→Computational advertising;
∗Corresponding author.
This work is licensed under a Creative Commons Attribution 4.0 International License.
KDD ’26, Jeju Island, Republic of Korea
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2259-2/2026/08
https://doi.org/10.1145/3770855.3818434
Keywords
Guaranteed Delivery, Real Time Bidding, Multi-Slot Allocation,
Dual Optimization
ACM Reference Format:
Tianxing Bu, Zhaoqi Zhang, Linyou Cai, Miao Xie, Shengri Xue, Tan Qu,
Qianlong Xie, Xingxing Wang, Siqiang Luo, and Gao Cong. 2026. HMAF: A
Hierarchical Multi-Slot GD-RTB Allocation Framework. InProceedings of
the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining
V.2 (KDD ’26), August 09–13, 2026, Jeju Island, Republic of Korea.ACM, New
York, NY, USA, 10 pages. https://doi.org/10.1145/3770855.3818434
1 Introduction
In large-scale online advertising ecosystems, especially multi-slot
environments such as Online-to-Offline content feeds, impression
allocation is governed by a hybrid marketplace where Guaranteed
Delivery (GD) contracts [1, 7, 9] coexist and bid with Real-Time
Bidding (RTB) auctions [15, 20, 24]. GD contracts ensure long-term
contract delivery by guaranteeing fixed impression volumes at
pre-negotiated prices, while RTB auctions dynamically monetize re-
maining inventory through competitive bidding. Although revenue
maximization is relatively straightforward in a pure RTB setting,
hybrid markets introduce an inherent conflict between short-term
eCPM-driven revenue efficiency and long-term delivery guarantees.
This conflict is further amplified in multi-slot page view setting.
Prior research has studied GD and RTB mechanisms largely in
isolation or through loosely coupled pipelines. Early works [ 2]
on GD allocation formulated delivery as a constrained optimiza-
tion problem, primarily focusing on offline planning to satisfy sup-
ply–demand balance. To cope with real-time traffic uncertainty,
subsequent studies introduced feedback and control-theoretic ap-
proaches, including PID-based controllers [3, 23], to dynamically
regulate bidding prices or sampling rates. Recent studies consider
arXiv:2606.09896v1  [cs.GT]  4 Jun 2026

KDD ’26, August 09–13, 2026, Jeju Island, Republic of Korea Tianxing Bu et al.
Figure 1: Flowchart of Meituan display advertising system
GD and RTB competing in shared auctions. CONFLUX [17] coor-
dinates GD and RTB via a primal–dual control mechanism under
delivery constraints, while LIBRA [16] embeds contract-aware sig-
nals into learning-based hybrid ranking. While existing systems
mark an important step toward unified GD–RTB competition, they
remain limited in their ability to address the full complexity of
large-scale, multi-slot hybrid allocation.
Despite recent progress in GD-RTB allocation and delivery con-
trol, three fundamental challenges persist:(1) NP-Hardness un-
der Fine-Grained Multi-Slot Constraints.The hybrid allocation
problem involves large-scale combinatorial optimization over mil-
lions of requests and thousands of contracts. Fine-grained supply-
side constraints, such as Page View limits to mitigate ad fatigue,
further complicate the problem and render global optimization
NP-hard.(2) eCPM-fulfillment Trade-off under Delivery Con-
straints.Pursuing higher eCPM can improve short-term momone-
tization but often risks under-delivery when delivery constraints
become binding, while overly aggressive fulfilment pacing may com-
promiseconomic efficiency. Effectively managing this constraint-
aware trade-off is crucial for sustaining both revenue efficiency
and delivery stability in large-scale hybrid advertising systems.(3)
Weak Supervision under Hybrid Ranking Objectives.Unlike
conventional CTR prediction tasks with explicit click labels, hybrid
ranking lacks ground-truth supervision, defining an optimal rank-
ing list that balances immediate revenue with long-term delivery
guarantees. As a result, the system must learn from implicit and
delayed feedback derived from aggregate delivery states rather than
direct labels.
To address the aforementioned challenges, we proposeHMAF, a
HierarchicalMulti-Slot andAllowcationFramework, which decom-
poses the intractable GD-RTB allocation problem into a hierarchical
Plan-Calibrate-Executeparadigm. As illustrated in Figure 1, HMAF
is positioned at the confluence of two parallel pipelines, aggre-
gating their outputs to construct a unified competitive stage for
GD and RTB ads. At theplanstage, we formulate aPage View-
Constrained Optimizationproblem and solve it offline to derive
optimal dual variables. These dual variables act as shadow prices
that encode the tightness of delivery constraints and the marginal
value of page-view resources for individual contracts and slots,
distilling long-horizon delivery pressure and supply-demand imbal-
ance into compact control signals for downstream decision-making.
At thecalibrationstage, we design aDual-Guided Unified Rank-
ingmechanism that injects offline dual variables into online scoring,
balancing eCPM maximization with long-term fulfillment require-
ments under delivery and slot constraints. At theexecutionstage,
we develop aGenerator-Evaluatornetwork for real-time GD-RTB
ranking, where the dual variables are incorporated as global state
features to guide listwise generation, allowing the model to trade
off instantaneous RTB revenue against the shadow cost of potential
GD violations and thereby transforming unsupervised ranking into
a reward-guided decision process.
TThe main contributions of this paper are summarized as fol-
lows:
• We propose HMAF, a unified GD-RTB allocation and ranking
framework, which tightly couples offline constraint optimization
with online neural decision making, providing a reliable architec-
tural foundation for GD-RTB allocation in multi-slot advertising
systems.
• We introduce three tightly coupled core components, a Page
View-Constrained Optimization module, which provides a prin-
cipled optimization backbone that captures fine-grained supply-
side constraints and global resource scarcity; a Dual-Guided Uni-
fied Ranking module, which calibrates online candidate scoring
using the offline dual variables, explicitly balancing eCPM maxi-
mization and contract fulfillment under delivery constraints; and
a Generator-Evaluator module, which enables listwise GD-RTB
ranking by jointly modeling candidate–position interactions and
selecting revenue-optimal ranking lists under global guidance.
• We conduct large-scale comparative experiments and online A/B
tests on Meituan’s advertising platform, HMAF achieved statisti-
cally significant improvements: 3.72% increase on GD delivery
rate and 1.59% increase on total advertisement revenue
2 Related Work
2.1 Guaranteed Delivery Allocation
Several approaches focus on the allocation of display ads within GD
contexts. Vee et al. [14] address online allocation using future ar-
rival forecasts, ensuring near-optimal solutions even in adversarial
settings. Bharadwaj et al. [2] propose SHALE, a scalable algorithm
for GD advertising, optimizing decisions with minimal state in-
formation and linear time complexity. Cheng et al. [4] introduce
an adaptive framework that balances contract fulfillment and user
interest optimization through real-time pacing adjustments. Fang et
al. [6] present Xshale, which models GD allocation at the individual
user level, incorporating real-time pacing strategies to improve
targeting. He et al. [8] propose a local search optimization method
to explore feasible allocations while respecting complex multilin-
ear constraints. Li et al. [11] introduce a bi-objective optimization
framework that balances impressions for new orders and inventory
allocation, reducing online delivery risks. More recently, Zhang
et al. [25] extend GD allocation from the conventional single-slot
setting to multi-slot joint optimization by considering page-view
constraints.

HMAF: A Hierarchical Multi-Slot GD-RTB Allocation Framework KDD ’26, August 09–13, 2026, Jeju Island, Republic of Korea
Figure 2: Overview of HMAF.
2.2 Guaranteed Delivery Optimization
In addition to allocation, several works focus on optimizing the ful-
fillment of guaranteed delivery ads. Wu et al. [19] explore auction-
based impression allocation, using multi-agent reinforcement learn-
ing to optimize allocation decisions and adapt to dynamic traffic
patterns. Zhang et al. [21] propose a control-based bidding approach
for mobile livestreaming ads, adjusting bidding parameters using
feedback control to meet exposure guarantees. Mao et al. [12] in-
troduce a unified end-to-end system for inventory prediction and
allocation, improving efficiency by integrating forecasting with al-
location. Dai et al. [5] incorporate fairness considerations into GD
allocation, balancing contract fulfillment and traffic costs. Wei et
al. [18] present RLTP, a reinforcement learning-based pacing agent
that optimizes both guaranteed impression counts and delivery
performance through an adaptive reward estimator.
2.3 GD-RTB Competition
Combining the GD and RTB models has become a promising ap-
proach for maximizing revenue across both streams. Wang et al. [17]
introduce CONFLUX, a unified framework for impression alloca-
tion that bridges the GD and RTB markets. By modeling impression
allocation at the individual request level, the framework maximizes
combined revenue and uses a cascaded learning process to guide a
deep model. This model is then transferred to a lightweight model
suitable for large-scale online serving. Zhang et al. [ 22] present
RAP, a request-level system for GD advertising that captures fine-
grained request attributes and jointly optimizes impression fore-
casting, sales planning, and supply allocation, ensuring that ads are
served effectively. Li et al. [11] address the challenge of balancing
the allocation of impressions for both new guaranteed contracts
and inventory distribution across supply nodes. Their bi-objective
optimization framework ensures that impressions are maximized
for incoming orders while maintaining a balanced distribution to
reduce risks in online serving.
3 Preliminary
3.1 Problem Formulation
We formulate a multi-slot GD-RTB allocation problem, where GD
contracts and RTB ads compete for exposure in a shared stream

KDD ’26, August 09–13, 2026, Jeju Island, Republic of Korea Tianxing Bu et al.
of multi-slot page view requests. Let I denote the sequence of
incoming user requests (supply), and J=J 𝐺𝐷∪J𝑅𝑇𝐵 denote
the set of candidate ads (demand). Each request𝑖∈I may contain
multiple ad slots, but for modeling simplicity, we treat𝑖 as an atomic
supply unit with capacity𝑠𝑖 (e.g., expected impressions).
Our ultimate goal is to maximize the platform’s total revenue,
which consists of the realized value from RTB auctions and the
contractual value from GD fulfillment, subject to strict delivery
constraints. Let 𝑥𝑖𝑗 ∈ {0, 1} and𝑦𝑖𝑗 ∈ {0, 1} be binary decision
variables indicating whether request𝑖 is allocated to a GD contract
𝑗∈J 𝐺𝐷 or a RTB ad 𝑗∈J 𝑅𝑇𝐵 , respectively. The unified allocation
problem is formulated as follows:
max
x,y
∑︁
𝑖∈I
'›
«
∑︁
𝑗∈J𝐺𝐷
CPM𝑗·𝑥𝑖𝑗+
∑︁
𝑗∈J𝑅𝑇𝐵
BID𝑖𝑗·𝑦𝑖𝑗 “ﬁ
‹
(1)
s.t.𝜙𝐵 𝑗≤
∑︁
𝑖∈Γ(𝑗)
𝑠𝑖𝑥𝑖𝑗≤𝐵 𝑗,∀𝑗∈J 𝐺𝐷 (2)
∑︁
𝑗∈J𝐺𝐷
𝑥𝑖𝑗+
∑︁
𝑗∈J𝑅𝑇𝐵
𝑦𝑖𝑗≤1,∀𝑖∈I(3)
𝑠𝑖(𝑥𝑖𝑗+𝑦𝑖𝑗)≤𝑝𝑣 𝑖,∀𝑖,𝑗(4)
𝑥𝑖𝑗,𝑦𝑖𝑗 ∈{0,1},∀𝑖,𝑗(5)
Here, Equation 1 represents the total revenue. Constraint 2 enforces
the double-sided delivery guarantee for GD contracts, where𝐵𝑗 is
the total purchased quantity and𝜙∈[ 0, 1] is the minimum delivery
rate required to avoid penalties. Constraint 3 ensures that each
supply unit is allocated to at most one ad. Constraint 4 represents
the fine-grained Page View constraint, preventing over-exposure
at specific slot positions.
3.2 Computational Challenges
Directly solving the multi-slot GD-RTB allocation problem in an in-
dustrial online environment presents two fundamental challenges:
1. NP-Hardness of Combinatorial Allocation: The multi-slot
GD-RTB allocation problem is computationally intractable, even
in an offline setting where all requestsI are known in advance.
Specifically, the combination of the capacity constraint (3) and
the double-sided knapsack-like demand constraint (2) generalizes
the well-knownMultidimensional Knapsack Problem (MKP), both
of which are NP-hard [ 10]. The introduction of the Page View
constraint (4) further couples the decision variables across different
slots, increasing complexity.
To formally establish NP-hardness, we provide a polynomial-
time reduction from MKP to our problem (denoted as Π). Consider
an arbitrary MKP instance defined by:
• A set of items 𝑘∈K={ 1,...,𝑁} , each with weight 𝑤𝑘 and
value𝑣 𝑘.
• A set of knapsacks𝑚∈M={ 1,...,𝑀} , each with capacity𝐶𝑚.
• Objective: Maximize ˝ 𝑚,𝑘𝑣𝑘𝑧𝑚𝑘 subject to ˝ 𝑘𝑤𝑘𝑧𝑚𝑘≤𝐶𝑚 and˝
𝑚𝑧𝑚𝑘≤1, where𝑧 𝑚𝑘∈{0,1}.
We construct a specific instance of our problem Π (defined by
Eqs. (1)-(5)) using the following mapping𝑓:
Sets mapping:
• Let the set of impressionsI correspond to the set of itemsK (i.e.,
|I|=𝑁).
• Let the set of GD advertisersJ𝐺𝐷 correspond to the set of knap-
sacksM(i.e.,|J 𝐺𝐷|=𝑀).
•Let the set of RTB advertisers be empty:J 𝑅𝑇𝐵 =∅.
Parameter assignment (restriction):
•Set impression consumption𝑠 𝑖 =𝑤𝑖.
•Set advertiser budget𝐵 𝑗 =𝐶 𝑗 .
• Set advertiser value CPM𝑗 such that the gain matches𝑣𝑘 (a uni-
form value suffices because even the simplified MKP with item-
independent values is NP-hard).
• Set the lower bound parameter𝜙= 0(relaxing the lower bound
constraint).
•Set impression capacity𝑝𝑣 𝑖 =1(standard 0/1 constraint).
•SinceJ 𝑅𝑇𝐵 =∅, all BID𝑖𝑗 terms and variables𝑦𝑖𝑗 vanish.
Substituting these parameters into our formulation yields:
(1) Objective: maxx
˝
𝑖∈I
˝
𝑗∈J𝐺𝐷 CPM𝑗𝑥𝑖𝑗 — matches MKP objec-
tive.
(2) GD constraint: Upper bound˝ 𝑖𝑠𝑖𝑥𝑖𝑗≤𝐵 𝑗 (lower bound trivial).
(3) Supply constraint: ˝ 𝑗𝑥𝑖𝑗≤ 1— matches MKP item assignment
constraint.
(4) Binary constraint:𝑥 𝑖𝑗 ∈{0,1}.
Thus the constructed instance is mathematically identical to
MKP. The mapping𝑓 involves only constant-time assignments and
is clearly polynomial-time. Since MKP is known to be NP-hard [13],
it follows that our problem Π is NP-hard. Consequently, obtaining
an exact integer solution for millions of requests and contracts is
impossible within milliseconds.
2. Online Stochasticity:In practice, requests 𝑖 arrive sequentially,
and the RTB bids BID𝑖𝑗 are unknown until the auction occurs.
This stochastic nature precludes static optimization. While On-
line Primal-Dual methods can provide asymptotic guarantees, they
typically require convex relaxations and cannot directly handle
the complex combinatorial constraints (e.g., listwise layout effects)
inherent in deep rendering models.
4 Methodology
We propose HMAF, a unified multi-slot GD–RTB allocation frame-
work. As illustrated in Figure 2, HMAF consists of three tightly
integrated modules: (1) Plan stage: Page View–Constrained Allo-
cation Module, which formulates GD fulfillment as a page-level
constrained optimization problem and derives dual signals to explic-
itly regulate multi-slot exposure and long-term delivery pressure;
(2) Calibrate stage: Dual-Guided Pre-Ranking Module, which lever-
ages offline dual variables to perform unified candidate filtering and
coarse ranking across GD and RTB ads, significantly reducing the
decision space while preserving allocation quality; and (3) Execute
stage: Generator–Evaluator Module, which conducts listwise allo-
cation by jointly modeling cross-slot interactions and competitive
dependencies to produce the final impression assignment.
4.1 Page View-Constrained Allocation Module
To effectively coordinate ad delivery across multiple slots within
the same page view, we first formulate the allocation task as a
constrained optimization problem. This formulation captures not

HMAF: A Hierarchical Multi-Slot GD-RTB Allocation Framework KDD ’26, August 09–13, 2026, Jeju Island, Republic of Korea
only contract fulfillment and user engagement but also fine-grained
control over slot-level exposure. In particular, we introduce a novel
Page View constraint to limit the number of impressions each
slot can serve, thereby preventing over-exposure of high-traffic
positions and promoting a more balanced inventory allocation
across all ad slots. The detailed objective function and constraints
are defined as follows:
arg min
𝑥𝑖𝑗
1
2
∑︁
𝑗
∑︁
𝑖∈Γ(𝑗)
𝑠𝑖
𝑉𝑗
𝜃𝑗
(𝑥𝑖𝑗−𝜃 𝑗)2− ∑︁
𝑗
𝑤𝑗
∑︁
𝑖∈Γ(𝑗)
𝑠𝑖𝑥𝑖𝑗 (6)
−
∑︁
𝑗
𝜆𝑗
∑︁
𝑖∈Γ(𝑗)
𝑠𝑖𝑥𝑖𝑗𝑐𝑖𝑗
s.t.
∑︁
𝑖∈Γ(𝑗)
𝑠𝑖𝑥𝑖𝑗≤𝑑 𝑗,∀𝑗(7)
∑︁
𝑗∈Γ(𝑖)
𝑥𝑖𝑗≤1,∀𝑖(8)
𝑥𝑖𝑗≥0,∀𝑖,𝑗(9)
𝑠𝑖𝑥𝑖𝑗≤𝑝𝑣 𝑖,∀𝑖,𝑗(10)
where𝑥𝑖𝑗 denote the allocation probability from request𝑖 (i.e. sup-
ply) to contract 𝑗 (i.e. demand), the user interest between request𝑖
and contract 𝑗 is denoted by𝑐𝑖𝑗 , and𝜆𝑗 controls the relative impor-
tance of user interest for contract 𝑗 in the objective, each request𝑖
has a supply capacity𝑠𝑖, while each contract 𝑗 requires𝑑𝑗 impres-
sions in total. Distinct from prior work, we novelly introduce𝑝𝑣𝑖
to model page-view–level exposure limits for request𝑖, which con-
strains the maximum exposure volume that request𝑖 can contribute
across multiple ad slots on the same page. This constraint provides
a structural handle for capturing fine-grained supply-side scarcity
and enables principled interaction between offline optimization and
online learning. Let Γ(𝑗) denote the set of requests that can serve
contract 𝑗, and let Γ(𝑖) denote the set of contracts that request 𝑖
is eligible to serve. Each contract 𝑗 is further characterized by a
priority weight𝑤𝑗 , a smoothness parameter𝑉𝑗 , and a normalized
target delivery ratio𝜃𝑗 = 𝑑𝑗˝ 𝑖∈Γ(𝑗) 𝑠𝑖 , where𝑉𝑗 controls the strength
of the quadratic fairness regularization that penalizes deviations
from𝜃 𝑗 .
𝐿(𝛼,𝛽,𝛾,𝛿)= 1 2 ∑︁ 𝑗 ∑︁ 𝑖∈Γ(𝑗) 𝑠𝑖 𝑉𝑗 𝜃𝑗 (𝑥𝑖𝑗−𝜃 𝑗)2− ∑︁ 𝑗 𝑤𝑗 ∑︁ 𝑖∈Γ(𝑗) 𝑠𝑖𝑥𝑖𝑗
−
∑︁
𝑗
𝜆𝑗
∑︁
𝑖∈Γ(𝑗)
𝑠𝑖𝑥𝑖𝑗𝑐𝑖𝑗+
∑︁
𝑗
𝛼𝑗 '›
«
∑︁
𝑖∈Γ(𝑗)
𝑠𝑖𝑥𝑖𝑗−𝑑 𝑗 “ﬁ
‹
+
∑︁
𝑖
𝛽𝑖 '›
«
∑︁
𝑗∈Γ(𝑖)
𝑥𝑖𝑗−1 “ﬁ
‹
−
∑︁
𝑗
∑︁
𝑖∈Γ(𝑗)
𝛾𝑖𝑗𝑥𝑖𝑗
+
∑︁
𝑗
∑︁
𝑖∈Γ(𝑗)
𝛿𝑖𝑗
𝑠𝑖𝑥𝑖𝑗−𝑝𝑣 𝑖  (11)
KKT conditions:
𝑠𝑖
𝑉𝑗
𝜃𝑗
(𝑥𝑖𝑗−𝜃 𝑗)−𝑤 𝑗𝑠𝑖−𝜆 𝑗𝑠𝑖𝑐𝑖𝑗+𝛼 𝑗𝑠𝑖+𝛽𝑖𝑠𝑖−𝛾𝑖𝑗+𝛿𝑖𝑗𝑠𝑖 =0(12)
𝛼𝑗 '›
«
∑︁
𝑖∈Γ(𝑗)
𝑠𝑖𝑥𝑖𝑗−𝑑 𝑗 “ﬁ
‹
=0(13)
𝛽𝑖 '›
«
∑︁
𝑗∈Γ(𝑖)
𝑥𝑖𝑗−1 “ﬁ
‹
=0(14)
𝛾𝑖𝑗𝑥𝑖𝑗 =0(15)
𝛿𝑖𝑗
𝑠𝑖𝑥𝑖𝑗−𝑝𝑣 𝑖  =0(16)
𝛼𝑗≥0, 𝛽 𝑖≥0, 𝛾 𝑖𝑗≥0, 𝛿 𝑖𝑗≥0(17)
where𝛼𝑗 ,𝛽𝑖,𝛾𝑖𝑗 and𝛿𝑖𝑗 are the Lagrangian multipliers of constraints
Equation 13, 14, 15 and 16 respectively. According to the KKT
conditions, the optimal allocation probability𝑥𝑖𝑗 can be derived as:
𝑥𝑖𝑗 =max

0, 𝜃𝑗

1+ 𝑤𝑗+𝜆 𝑗𝑐𝑖𝑗−𝛼 𝑗−𝛽𝑖−𝛿𝑖𝑗
𝑉𝑗

(18)
To efficiently optimize the PV-constrained allocation problem,
we adopt an online distributed strategy that updates the dual vari-
ables𝛼 𝑗 ,𝛽 𝑖, and𝛿𝑖𝑗 based on the KKT conditions. These dual vari-
ables correspond to the contract demand, request capacity, and
slot-level page view constraints, respectively. Instead of solving
the primal problem directly, which is computationally expensive in
large-scale settings, we leverage the closed-form expression of𝑥𝑖𝑗
derived from the KKT optimality condition and iteratively adjust
the dual variables using projected gradient steps.
At each iteration,𝛼𝑗 is increased if the total allocated impressions
to contract𝑗 exceed its demand𝑑𝑗 , while𝛽𝑖 is updated to ensure the
total allocation from request𝑖 remains within its capacity. Similarly,
𝛿𝑖𝑗 is adjusted to enforce the fine-grained page view constraint for
each ad slot. These updates can be performed in parallel across all𝑖
and 𝑗, making the solution highly scalable and amenable to online
deployment. This formulation ensures that the allocation respects
all practical delivery constraints while optimizing for efficiency and
relevance. The detailed procedure is summarized in Algorithm 1.
Algorithm 1:PV Constrained Allocation Algorithm
Input:𝑠𝑖,𝑑𝑗,𝜆𝑗,𝑉𝑗,𝑤𝑗,𝑐𝑖𝑗
Output:𝛼 𝑗,𝛽𝑖,𝛿𝑖𝑗,𝑥𝑖𝑗
1Step 1: Initialize. Set𝛼 𝑗 =𝑤 𝑗+𝜆 𝑗𝑐𝑖𝑗,𝜃 𝑗 , calculate𝑥𝑖𝑗 , and
gradient𝑔𝑟𝑎𝑑 𝑗
2Step 2:
3foriteration = 1 to ndo
4update𝛼 𝑗 with Equation:𝛼 𝑡+1 𝑗 =𝛼 𝑡 𝑗−𝑉𝑗(1− 𝑑𝑗(𝛼𝑡) 𝑑𝑗 )
5solve𝛽 𝑖:𝛽 𝑖←max

0,𝛽𝑖+𝜂𝛽
˝
𝑗∈Γ(𝑖) 𝑥𝑖𝑗−1

6calculate𝛿 𝑖𝑗 :𝛿𝑖𝑗←max 0,𝛿𝑖𝑗+𝜂𝛿 𝑠𝑖𝑥𝑖𝑗−𝑝𝑣 𝑖 
7calculate𝑥 𝑖𝑗 :𝑥𝑖𝑗 =max
n
0, 𝜃𝑗

1+ 𝑤𝑗+𝜆𝑗𝑐𝑖𝑗−𝛼𝑗−𝛽𝑖−𝛿𝑖𝑗 𝑉𝑗
o
8update𝑔𝑟𝑎𝑑 𝑗 :𝑔𝑟𝑎𝑑 𝑗 = ˝ 𝑖∈Γ(𝑗) 𝑠𝑖𝑥𝑖𝑗−𝑑 𝑗
9end

KDD ’26, August 09–13, 2026, Jeju Island, Republic of Korea Tianxing Bu et al.
4.2 Dual-Guided Pre-Ranking Module
We consider a dual-guided pre-ranking module that jointly serves
GD ads and RTB ads within the same ranking list. Let 𝑗 index
candidate ads and𝑖 index page view-level requests. For each ad𝑗,
the online ranking score𝑟𝑠 𝑗 is defined as:
𝑟𝑠𝑗 =
 

𝑐𝑡𝑟𝑖𝑗·𝐶𝑃𝐶𝑏𝑖𝑑 𝑖𝑗+𝑔𝑚𝑣 𝑗, 𝑗∈{RTB},
𝐶𝑃𝑀𝑗·(1+𝑥 𝑖𝑗·𝑃𝐼𝐷 𝐸𝑟𝑟𝑜𝑟)+𝑔𝑚𝑣 𝑗, 𝑗∈{GD},
(19)
Here, we innovatively introduces a dual-guided modulation term,
𝑥𝑖𝑗·𝑃𝐼𝐷 𝐸𝑟𝑟𝑜𝑟 , where𝑥𝑖𝑗 is an allocation confidence score derived
from offline optimization described in Algorithm 1, reflecting the
competitiveness of contract𝑗 to request𝑖 within the GD channel
under allocation constraints. Unlike traditional PID approaches that
apply uniform regulation pressure across all traffic, our method
dynamically adjusts the allocation based on context-specific con-
fidence scores, enabling more tailored and responsive ad delivery.
The term 𝑃𝐼𝐷𝐸𝑟𝑟𝑜𝑟 represents the real-time delivery pressure of
guaranteed ad𝑗, which is calculated as follows:
𝑃𝐼𝐷𝐸𝑟𝑟𝑜𝑟 =
 

𝜇0+(1−𝜇 0)𝑑𝑟∗−𝑑𝑟𝑗(𝑡) 𝑑𝑟∗ , 𝑑𝑟 𝑗(𝑡)≤𝑑𝑟 ∗,
𝜇0, 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒,
(20)
where𝑑𝑟𝑗(𝑡)= N𝑗(𝑡) B𝑗(𝑡) is the delivery rate at time 𝑡,N𝑗(𝑡) is the
accumulated impressions achieved up to time𝑡, andB𝑗(𝑡) denotes
the expected number of impressions at time𝑡 based on the historical
traffic curve.𝑑𝑟∗ and𝜇0 are hyperparameters, serving as the target
minimum delivery rate and the baseline competitiveness coefficient,
respectively. The parameter𝜇0 ensures that the contract retains a
minimum boost to prevent abrupt on-off switching, which could
destabilize the delivery curve and negatively affect user experience.
4.3 Generator-Evaluator Listwise Allocation
Module
While the allocation module ensures feasibility, it does not explicitly
optimize the relative ordering of candidates across multiple slots.
In multi-slot scenarios, ranking decisions are inherently listwise
and position-dependent, which motivates a Generator–Evaluator
network that jointly models candidate–position interactions and
evaluates ranking lists at the page-view level.
4.3.1 Dual-Augmented Feature Space.To bridge the gap between
offline page view-constrained allocation in GD channel and online
mixed ranking, we explicitly inject the optimization results from
Section 4.2 into the Generator-Evaluator network as GD state sig-
nals. Unlike traditional user-item features, these signals provide
the model with "foresight" regarding system-wide constraints:
GD Guidance Signal (𝑥𝑖𝑗 ): We feed the offline optimal probability
𝑥𝑖𝑗 directly into the network. This serves as a strong prior, guiding
the model to align its listwise generation with the macro-resource
plan, ensuring that the final execution does not deviate significantly
from the global optimum.
Urgency Signal (𝛼𝑗 ): The demand shadow price𝛼𝑗 informs the
network about fulfillment difficulty. The model implicitly learns
to prioritize contracts with lower 𝛼𝑗 (indicating high scarcity or
under-delivery) and yield traffic for those with high𝛼𝑗 (saturated
demand), thereby dynamically balancing pacing.
Competition Anchor (𝛽𝑗 ): The scarcity price𝛽𝑗 acts as a valuation
baseline for the current slot. It helps the evaluator network gauge
whether a candidate ad’s utility justifies occupying a premium slot,
effectively filtering out low-quality allocations in high-contention
contexts.
Topology Constraint Signal (𝛿𝑖𝑗 ): By incorporating the position
cost𝛿𝑖𝑗 , the model acquires layout-awareness. This signal discour-
ages the generator from placing an ad in a specific position where
it has already reached its exposure limit (i.e., high𝛿𝑖𝑗 ), promoting
diverse and compliant ad placements across the list.
4.3.2 Generator.The Generator models the page-view level as-
signment between candidate adsX ={𝑥 1,...,𝑥 𝑛} and positions
P ={𝑝 1,...,𝑝 𝑚} jointly. Leveraging a Transformer-based encoder
to capture candidate–position interactions in a shared latent space,
it outputs a probability matrix ˆ𝑃={ ˆ𝑝𝑖𝑗}, where ˆ𝑝𝑖𝑗 represents the
normalized probability of assigning candidate𝑥 𝑗 to position𝑝 𝑖:
ˆ𝑝𝑖𝑗 =
exp

𝑥⊤ 𝑗 𝑝𝑖

˝𝑛
𝑘=1 exp

𝑥⊤ 𝑘𝑝𝑖
 (21)
Based on ˆ𝑃, a candidate ranking list𝑆𝑔 is sampled. To enhance
exploration, we further generate a set of perturbed ranking lists
{𝑆1,...,𝑆 𝑙} using heuristic rules based on historical bidding pat-
terns.
4.3.3 Evaluator.The Evaluator serves as a listwise supervisor
that identifies the optimal ranking structure from the set 𝑆=
{𝑆𝑔,𝑆 1,...,𝑆 𝑙}. It estimates a reward𝑅(𝑆𝑘) for each list by aggregat-
ing predicted metrics and delivery constraints to compute the list-
level eCPM. The optimal list is selected as𝑆★ =arg max𝑆𝑘∈𝑆𝑅(𝑆𝑘)
and converted into a binary label matrixY ∈ {0, 1}𝑚×𝑛 , where
𝑌𝑖𝑗 = 1indicates the assignment of 𝑥𝑗 to𝑝𝑖 in𝑆★. This provides a
unified supervision signal balancing revenue efficiency and system
stability.
4.3.4 Training Objective.The model is optimized via a loss func-
tion that combines supervised alignment and reward-aware ex-
ploration. Specifically,L𝑐𝑒 aligns the predicted probability ˆ𝑃 with
the evaluator-selected optimal assignmentY, whileL 𝑟𝑒 addresses
the discrepancy between the model’s predicted eCPM ( ˆ𝑒𝑖𝑗 ) and the
realized eCPM observed in online logs (𝑒𝑖𝑗 ).
L=𝜓 1·

−
∑︁
𝑖,𝑗
𝑌𝑖𝑗 log ˆ𝑝𝑖𝑗
!
|                {z                }
L𝑐𝑒
−𝜓2·
∑︁
(𝑖,𝑗)∈O
 ˆ𝑒𝑖𝑗−𝑒𝑖𝑗 
|               {z               }
L𝑟𝑒
(22)
whereO represents the set of observed exposure events. By directly
penalizing the signed deviation ˆ𝑒𝑖𝑗 −𝑒 𝑖𝑗 , the model is forced to
correct systematic over-estimation or under-estimation biases, en-
suring that the predicted utility strictly aligns with the real-world
settlement data.𝜓1 and𝜓2 are hyperparameters balancing structural
correctness and value calibration.

HMAF: A Hierarchical Multi-Slot GD-RTB Allocation Framework KDD ’26, August 09–13, 2026, Jeju Island, Republic of Korea
5 Experiments
5.1 Setup
5.1.1 Datasets.We collected a large-scale industrial dataset from
the Meituan platform’s production logs, spanning 32 consecutive
days, from 1st January to 1st February, 2026. The dataset contains
123,546,485 impression samples associated with 193,797 advertise-
ments, of which 9.73% correspond to GD ads, while the remaining
impressions are served through RTB.
5.1.2 Offline Baselines.We evaluate the performance of HMAF
against a diverse set of representative baselines, including GD-
focused models, CF, PID, and AUAF [4], and GD-RTB models, CON-
FLUX [17] and LIBRA [16]:
• Contract First (CF): A heuristic baseline that prioritizes ful-
filling GD contracts and allocates residual impressions to RTB,
typically optimized via the primal-dual SHALE algorithm [2].
• PID: A feedback-based method that applies proportional-integral-
derivative control to dynamically regulate GD contract delivery
and reduce under- or over-delivery.
• AUAF[ 4]: An adaptive unified allocation framework that dy-
namically balances multiple GD contracts under heterogeneous
demand and supply conditions.
• CONFLUX[ 17]: A request-level fusion framework that unifies
GD and RTB allocation via cascaded distillation.
• LIBRA[ 16]: A unified impression allocation approach that en-
forces fairness across contracts using adversarial reward guid-
ance.
To adapt our baselines to our multi-slot setting, we decompose each
page view into sequential single-slot decisions, greedily selecting
the highest-ranked eligible ad per position.
5.1.3 Evaluation Metrics.We consider the following metrics:
• Group AUC (GA): Measures the ranking accuracy of the model
within each user session. It serves as a standard metric for ver-
ifying that the injection of auxiliary features does not degrade
the core CTR estimation capability.
• Delivery Rate (DR): This metric serves as the central measure
of GD contract performance and quantifies the fulfillment rate.
Since there are multiple contracts in the system, we calculate
the weighted delivery rate,˝ 𝑗∈J 𝑤𝑒𝑖𝑔ℎ𝑡𝑗 ˝ 𝑖𝑥𝑖𝑗 𝑑𝑗 , where𝑤𝑒𝑖𝑔ℎ𝑡𝑗 =
𝑑𝑗˝
𝑗∈J 𝑑𝑗 .
• GD Quality (GQ): This metric assesses the fulfillment rate of
impression quality constraints, specifically in terms of clicks, for
GD contracts. We calculate the weighted fullfillment rate as GD
quality,˝ 𝑗∈J 𝑤𝑒𝑖𝑔ℎ𝑡𝑗 ˝ 𝑖𝑥𝑖𝑗·𝑝𝐶𝑇𝑅𝑖𝑗 𝑐𝑙𝑖𝑐𝑘𝑗 , where𝑤𝑒𝑖𝑔ℎ𝑡 𝑗 = 𝑐𝑙𝑖𝑐𝑘𝑗˝ 𝑗∈J 𝑐𝑙𝑖𝑐𝑘𝑗 .
• RTB eCPM (RE): As the unified allocation framework releases
more high-quality impressions to the RTB market, we calculate
the average eCPM (effective cost per mille) of the RTB market.
For privacy concerns related to business data, we normalize this
metric using the highest eCPM among the compared methods.
• Utility Rate (UR): This metric represents the total utility return
from both GD and RTB markets. It considers the sum of GD and
RTB incomes while accounting for under delivery penalties. As
user traffic and bid landscape evolve over time, we normalize
it by the theoretically optimal utility solved using evaluator in
Section 4.3. This normalization provides an intuitive and effective
metric to evaluate the method’s impact on revenue lift.
5.1.4 Experomental Settings.During training, the first 31 days of
the dataset are used for training, while the last day is reserved for
testing, ensuring a robust evaluation of the model’s performance on
unseen online traffic conditions.All the experiments involving deep
learning frameworks are executed on two NVIDIA A100 GPUs. For
more detailed hyperparameters, please refer to Table 1.
Table 1: The detailed hyperparameters of HMAF
Hyperparameters Value
Batch size 512
Learning rate 3e-4
Optimizer LazyAdam
Embedding dim 8
Activation function Swish
𝑑𝑟∗0.9
𝜇𝑜 0.1
𝜙1 1
𝜙2 -0.2
5.2 Performance Analysis
The experimental results in Table 2 demonstrate that HMAF con-
sistently outperforms all baseline methods across most evaluation
metrics, achieving the highest scores in Group AUC (GA), GD Qual-
ity (GQ), RTB eCPM (RE), and Utility Rate (UR).
Among GD-focused methods, CF achieves the highest Deliv-
ery Rate (DR), which is expected given its heuristic strategy that
strictly prioritizes GD contracts before allocating remaining traffic
to RTB ads. However, this prioritization comes at the cost of re-
duced flexibility in revenue optimization. Notably, HMAF attains a
highly competitive DR with only a marginal gap from CF, despite
not enforcing explicit GD-first rules. This indicates that HMAF
can effectively satisfy GD delivery requirements while preserving
allocation flexibility for revenue-aware decision-making. PID and
AUAF improve GD delivery stability by introducing feedback con-
trol or adaptive heuristics, yet they remain primarily optimized
for GD contracts and rely on decoupled or rule-based mechanisms
when handling RTB ads. As a result, these methods struggle to
achieve a balanced trade-off between long-term contract delivery
and short-term revenue maximization in a unified allocation setting.
Among GD–RTB baselines, CONFLUX attempts to bridge the
two markets through request-level unification, but is designed for
single-slot allocation, which limits its ability to capture cross-slot
interactions and page-level coordination in multi-slot traffic. LIBRA
represents the strongest GD-RTB baseline by incorporating adver-
sarial reward guidance for unified impression allocation. Neverthe-
less, its decision process lacks explicit mechanisms to dynamically
integrate offline constraint signals with online allocation decisions.
In contrast, HMAF emphasizes page-level constraint modeling
and coordinated listwise allocation, which jointly enable effective
multi-slot decision-making across GD and RTB ads. These design
choices allow HMAF to achieve superior overall performance with-
out relying on rigid prioritization rules or heavy online control,

KDD ’26, August 09–13, 2026, Jeju Island, Republic of Korea Tianxing Bu et al.
Table 2: Offline performance comparison, categorized by
model type as either GD-focused models ( ✗) or GD-RTB mod-
els (✓). The highest score is highlighted in bold, while the
second-best result among the baselines is underlined. To en-
sure robustness, all metrics are reported as the mean and
standard deviation over ten independent runs.
Type Model GA DR GQ RE UR
✗CF 0.7203
(±0.0032)
0.9680
(±0.0000)
0.8351
(±0.0041)
0.7333
(±0.0050)
0.8273
(±0.0043)
✗PID 0.7839
(±0.0027)
0.9273
(±0.0025)
0.8604
(±0.0033)
0.7734
(±0.0038)
0.9379
(±0.0029)
✗AUAF 0.8026
(±0.0024)
0.9408
(±0.0022)
0.8948
(±0.0028)
0.8023
(±0.0032)
0.8953
(±0.0030)
✓CONFLUX 0.8274
(±0.0025)
0.9493
(±0.0021)
0.9264
(±0.0029)
0.8673
(±0.0035)
0.9308
(±0.0028)
✓LIBRA 0.8538
(±0.0031)
0.9554
(±0.0024)
0.9450
(±0.0035)
0.9132
(±0.0042)
0.9513
(±0.0033)
✓HMAF 0.8984
(±0.0021)
0.9638
(±0.0018)
0.9751
(±0.0019)
1.0000
(±0.0000)
0.9812
(±0.0017)
leading to consistent gains across both delivery and revenue met-
rics. To verify that these improvements are statistically reliable,
we further conduct significance testing against the strongest base-
lines. The results show that HMAF achieves significant gains on
all major metrics, while the reported standard deviations and confi-
dence intervals over multiple runs demonstrate the stability of its
performance.
5.3 Ablation Study
TTable 3 summarizes the ablation results of HMAF. Overall, remov-
ing any component results in noticeable performance degradation.
In particular, excluding the PV module leads to a significant drop
in allocation accuracy. This decline occurs because the PV module
explicitly captures page-level exposure constraints and propagates
the corresponding dual information to the online decision stage.
Without this guidance, the model tends to make slot-wise decisions
independently, which weakens its ability to coordinate impressions
across multiple slots on the same page. Removing the GE module
also hurts all metrics, showing that listwise allocation is necessary
for balancing GD delivery and RTB revenue in the multi-slot setting.
In contrast, removing the PR module yields slightly higher DR and
UR scores. This effect can be attributed to PR module’s candidate
pruning mechanism, which trades off a small amount of allocation
flexibility for efficiency by reducing the candidate space. Notably,
PR reduces the end-to-end optimization time from approximately
two days to 15 minutes, while introducing only marginal differ-
ences in allocation performance. These results demonstrate that PR
provides an effective accuracy–efficiency trade-off and is essential
for enabling scalable deployment in large-scale production systems.
5.4 Parameters Analysis
We evaluated the impact of four key hyperparameters: 𝑑𝑟∗ sets
the target minimum delivery rate for GD contracts, ensuring that
the system meets the required delivery levels;𝜇0 acts as a baseline
Table 3: Ablation study performances by removing Page
View-Constrained Allocation Module (PV), Dual-Guided Pre-
Ranking Module (PR) and Generator-Evaluator Listwise Al-
location Module (GE)
Model GA DR GQ RE UR
w/o PV 0.8419 0.9458 0.9503 0.9496 0.9647
w/o PR 0.7943 0.9647 0.9604 0.9672 0.9810
w/o GE 0.8294 0.9583 0.9382 0.9252 0.9458
HMAF 0.8984 0.9638 0.9751 1.0000 0.9812
(a) Parameter analysis on𝑑𝑟 ∗.
 (b) Parameter analysis on𝜇 0.
(c) Joint parameter analysis on(𝜓 1,𝜓 2).
Figure 3: Parameter sensitivity analysis of HMAF.
competitiveness coefficient, influencing the allocation of resources
between GD and RTB ads;𝜓1 and𝜓2 control the relative importance
of the loss terms, with 𝜓1 balancing the importance of the page-
view constrained allocation and𝜓2 managing the trade-off between
real-time revenue and long-term contract fulfillment.
As shown in Figure 3, the selected parameter configuration
achieves the best overall performance. If𝑑𝑟∗ is too low, the model
may prioritize contract fulfillment at the expense of maximizing
revenue, leading to suboptimal performance in the RTB market. On
the other hand, if𝑑𝑟∗ is set too high, the system might overempha-
size fulfillment, which could result in missed revenue opportunities.
Similarly,𝜇0 influences the trade-off between ensuring delivery and
maximizing RTB revenue. A𝜇0 that is too low reduces the system’s
ability to prioritize GD contracts, leading to potential delivery is-
sues. Conversely, an excessively high𝜇0 results in an overemphasis
on GD contracts, reducing flexibility in RTB allocation and limiting
the overall revenue potential. In our joint analysis of𝜓1 and𝜓2, we
observe that when these parameters are set too low, the system

HMAF: A Hierarchical Multi-Slot GD-RTB Allocation Framework KDD ’26, August 09–13, 2026, Jeju Island, Republic of Korea
struggles to effectively balance the dual objectives of contract fulfill-
ment and revenue maximization. On the other hand, setting them
too high results in overfitting, where the system either excessively
prioritizes GD contracts or diminishes RTB revenue generation.
The optimal performance is achieved when these parameters are
appropriately balanced, enabling the model to dynamically adapt to
varying traffic conditions while ensuring efficient allocation across
multiple slots.
6 Online A/B Testing
6.1 Setup
The experiments were conducted on the Meituan advertising plat-
form with live traffic. We employed a rigorous A/B testing frame-
work:
• Control Group:The legacy system using a standard PID-based
pacing algorithm with a greedy ranking strategy (RTB-first).
• Treatment Group:Our proposed HMAF framework, including
the Offline Primal-Dual Solver, Pacing-Adaptive Pre-Ranking,
and Dual-Augmented GE Reranking.
• Traffic Split:Traffic was randomly split by user ID buckets (50%
vs. 50%) to ensure fair comparison. The experiment lasted for
2 months, which is reasonably representative as it covers two
complete business cycles with both weekday and weekend traffic
patterns.
6.2 System Efficiency and Stability
In production, the offline stage runs on 20 machines, each equipped
with 32-core Intel Xeon Gold 6130 CPUs, and processes approxi-
mately 100 million SKUs in around two hours. The online serving
stage is lightweight, pre-ranking takes less than 5 ms per ad, and
GE inference remains within 50 ms per page view. The daily infras-
tructure cost is approximately $150.
To improve robustness under traffic shifts, HMAF adopts two
daily update mechanisms: (1)Daily Re-planning, the offline KKT
optimization is re-run every day using the latest traffic forecasts,
and (2)Strict Gating, the GE network is retrained daily and deployed
only when its offline Group-AUC fluctuation is within 5% of the
serving model.
For newly created GD contracts with insufficient real-time de-
livery data, HMAF uses a cold-start strategy based on historical
[City]× [Category] averages to initialize the dual variables. This
provides a reasonable exposure baseline before enough online data
is accumulated, after which the PID controller performs minor
adjustments around the globally coordinated allocation.
6.3 Online A/B Test Results
We adopt a comprehensive set of metrics covering three dimensions:
• Platform Revenue:Measured byRevenue Per Mille (RPM), eCPM
and total advertising revenue (TR).
• Contract Delivery:Measured byDelivery Rate (DR)—the ratio
of delivered impressions to the guaranteed quantity.
• Merchant Efficiency:Measured byROI (Return on Investment),
ensuring that increased revenue does not come at the cost of
advertiser satisfaction.
Our framework achieves a significantPareto Improvement. The
delivery rate increased by3.72%, effectively eliminating under-
delivery issues. Simultaneously, total advertisement revenue in-
creased by1.59%. This counter-intuitive result (usually better ful-
fillment hurts revenue) is attributed to the fine-grained optimiza-
tion of our GE model: by utilizing the𝛿𝑖𝑗 (slot constraint) and𝛽𝑖
(scarcity) signals, the model intelligently shifts GD impressions to
non-premium slots or low-competition traffic, releasing high-value
inventory for RTB ads. We further verify that this joint improve-
ment is statistically reliable. Over the two-month online experiment,
we performed a paired t-test on the daily delivery-rate differences
between the treatment and control groups, yielding a p-value of
0.018 (<0.05). The 95% confidence interval for the delivery-rate lift is
[3.04%, 4.27%]. For total advertisement revenue, the p-value is 0.024,
with a 95% confidence interval of [1.23%, 2.15%] for the revenue lift.
7 Conclusion
In this paper, we propose HMAF, a hierarchical multi-slot GD-RTB
allocation framework that effectively balances long-term contract
fulfillment with short-term revenue maximization in GD-RTB adver-
tising systems. HMAF introduces a novelPlan–Calibrate–Execute
paradigm, which tightly integrates offline constraint optimization
with online neural allocation, enabling systematic coordination
across the allocation process. This paradigm ensures both precise
global planning and dynamic real-time adjustments, making it well-
suited for the complex challenges of GD–RTB systems. By intro-
ducing page view constraints and deriving dual signals that capture
global scarcity and delivery pressure, HMAF enhances coordination
across GD and RTB ads in multi-slot environments. Experimental
results demonstrate that HMAF significantly outperforms baseline
models, achieving higher revenue and improved contract delivery
rates. HMAF has also been deployed in Meituan’s production adver-
tising system, where it brings measurable gains under large-scale
live traffic. Since its core formulation only relies on guaranteed de-
livery requirements, real-time bidding values, and multi-slot expo-
sure constraints, the framework can be adapted to other advertising
platforms with similar GD–RTB allocation settings.
References
[1] Anand Bhalgat, Jon Feldman, and Vahab Mirrokni. 2012. Online allocation
of display ads with smooth delivery. InProceedings of the 18th ACM SIGKDD
international conference on Knowledge discovery and data mining. 1213–1221.
[2] Vijay Bharadwaj, Peiji Chen, Wenjing Ma, Chandrashekhar Nagarajan, John
Tomlin, Sergei Vassilvitskii, Erik Vee, and Jian Yang. 2012. Shale: an efficient
algorithm for allocation of guaranteed display advertising. InProceedings of the
18th ACM SIGKDD international conference on Knowledge discovery and data
mining. 1195–1203.
[3] Ye Chen, Pavel Berkhin, Bo Anderson, and Nikhil R Devanur. 2011. Real-time
bidding algorithms for performance-based display ad allocation. InProceedings
of the 17th ACM SIGKDD international conference on Knowledge discovery and
data mining. 1307–1315.
[4] Xiao Cheng, Chuanren Liu, Liang Dai, Peng Zhang, Zhen Fang, and Zhonglin
Zu. 2022. An adaptive unified allocation framework for guaranteed display
advertising. InProceedings of the Fifteenth ACM International Conference on Web
Search and Data Mining. 132–140.
[5] Liang Dai, Zhonglin Zu, Hao Wu, Liang Wang, and Bo Zheng. 2023. Fairness-
aware guaranteed display advertising allocation under traffic cost constraint. In
Proceedings of the ACM Web Conference 2023. 3572–3580.
[6] Zhen Fang, Yang Li, Chuanren Liu, Wenxiang Zhu, Yu Zheng, and Wenjun Zhou.
2019. Large-scale personalized delivery for guaranteed display advertising with
real-time pacing. In2019 IEEE International Conference on Data Mining (ICDM).
IEEE, 190–199.

KDD ’26, August 09–13, 2026, Jeju Island, Republic of Korea Tianxing Bu et al.
[7] Arpita Ghosh, Preston McAfee, Kishore Papineni, and Sergei Vassilvitskii. 2009.
Bidding for representative allocations for display advertising. InInternational
workshop on internet and network economics. Springer, 208–219.
[8] Xiang He, Wuyang Mao, Zhenghang Xu, Yuanzhe Gu, Yundu Huang, Zhonglin
Zu, Liang Wang, Mengyu Zhao, and Mengchuan Zou. 2024. An Efficient Local
Search Algorithm for Large GD Advertising Inventory Allocation with Multilinear
Constraints. InProceedings of the 30th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining. 1040–1049.
[9] Ali Hojjat, John Turner, Suleyman Cetintas, and Jian Yang. 2014. Delivering
guaranteed display ads under reach and frequency requirements. InProceedings
of the AAAI Conference on Artificial Intelligence, Vol. 28.
[10] Hans Kellerer, Ulrich Pferschy, and David Pisinger. 2004.Knapsack Problems.
Springer, Berlin, Heidelberg.
[11] Yan Li, Yundu Huang, Wuyang Mao, Furong Ye, Xiang He, Zhonglin Zu, and
Shaowei Cai. 2024. Bi-Objective Contract Allocation for Guaranteed Delivery
Advertising. InProceedings of the 30th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining. 1691–1700.
[12] Wuyang Mao, Chuanren Liu, Yundu Huang, Zhonglin Zu, M Harshvardhan,
Liang Wang, and Bo Zheng. 2023. End-to-end inventory prediction and contract
allocation for guaranteed delivery advertising. InProceedings of the 29th ACM
SIGKDD Conference on Knowledge Discovery and Data Mining. 1677–1686.
[13] Silvano Martello and Paolo Toth. 1990.Knapsack problems: algorithms and com-
puter implementations. John Wiley & Sons, Inc.
[14] Erik Vee, Sergei Vassilvitskii, and Jayavel Shanmugasundaram. 2010. Optimal
online assignment with forecasts. InProceedings of the 11th ACM conference on
Electronic commerce. 109–118.
[15] Jun Wang and Shuai Yuan. 2015. Real-time bidding: A new frontier of com-
putational advertising research. InProceedings of the Eighth ACM International
Conference on Web Search and Data Mining. 415–416.
[16] Xiaoyu Wang, Yonghui Guo, Bin Tan, Tao Yang, Dongbo Huang, Lan Xu, Hao
Zhou, and Xiangyang Li. 2024. Follow the libra: guiding fair policy for unified
impression allocation via adversarial rewarding. InProceedings of the 17th ACM
International Conference on Web Search and Data Mining. 750–759.
[17] XiaoYu Wang, Bin Tan, Yonghui Guo, Tao Yang, Dongbo Huang, Lan Xu, Niko-
laos M Freris, Hao Zhou, and Xiang-Yang Li. 2022. CONFLUX: A Request-level
Fusion Framework for Impression Allocation via Cascade Distillation. InPro-
ceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data
Mining. 4070–4078.
[18] Penghui Wei, Yongqiang Chen, Shaoguo Liu, Liang Wang, and Bo Zheng. 2023.
RLTP: Reinforcement Learning to Pace for Delayed Impression Modeling in
Preloaded Ads. InProceedings of the 29th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining. 5204–5214.
[19] Di Wu, Cheng Chen, Xiujun Chen, Junwei Pan, Xun Yang, Qing Tan, Jian Xu,
and Kuang-Chih Lee. 2021. Impression allocation and policy search in display
advertising. In2021 IEEE International Conference on Data Mining (ICDM). IEEE,
749–756.
[20] Shuai Yuan, Jun Wang, and Xiaoxue Zhao. 2013. Real-time bidding for online
advertising: measurement and analysis. InProceedings of the seventh international
workshop on data mining for online advertising. 1–8.
[21] Haoqi Zhang, Junqi Jin, Zhenzhe Zheng, Fan Wu, Haiyang Xu, and Jian Xu. 2022.
Control-based Bidding for Mobile Livestreaming Ads with Exposure Guarantee. In
Proceedings of the 31st ACM International Conference on Information & Knowledge
Management. 2539–2548.
[22] Hong Zhang, Lan Zhang, Lan Xu, Xiaoyang Ma, Zhengtao Wu, Cong Tang,
Wei Xu, and Yiguo Yang. 2020. A request-level guaranteed delivery advertising
planning: Forecasting and allocation. InProceedings of the 26th ACM SIGKDD
International Conference on Knowledge Discovery & Data Mining. 2980–2988.
[23] Weinan Zhang, Yifei Rong, Jun Wang, Tianchi Zhu, and Xiaofan Wang. 2016.
Feedback control of real-time display advertising. InProceedings of the Ninth
ACM International Conference on Web Search and Data Mining. 407–416.
[24] Weinan Zhang, Shuai Yuan, and Jun Wang. 2014. Optimal real-time bidding
for display advertising. InProceedings of the 20th ACM SIGKDD international
conference on Knowledge discovery and data mining. 1077–1086.
[25] Zhaoqi Zhang, Jiaming Deng, Miao Xie, Linyou Cai, Qianlong Xie, Xingxing
Wang, Siqiang Luo, and Gao Cong. 2026. Beyond Single Slot: Joint Optimization
for Multi-Slot Guaranteed Display Advertising.arXiv preprint arXiv:2605.21556
(2026).
