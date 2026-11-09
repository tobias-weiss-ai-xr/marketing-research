---
title: 'SACO: Sequence-Aware Constrained Optimization Framework for Coupon Distribution in E-commerce'
url: https://arxiv.org/abs/2508.09198
category: ai-marketing
subcategory: empirical
date: 2025-08
venue: ''
authors:
- Li Kong
- Bingzhe Wang
- Zhou Chen
- Suhan Hu
- Yuchao Ma
source: arxiv
pdf_url: https://arxiv.org/pdf/2508.09198
pages: 9
chars: 41795
fetched_at: '2026-11-08T13:11:57+00:00'
kb_version: 1
---

# SACO: Sequence-Aware Constrained Optimization Framework for Coupon Distribution in E-commerce

SACO: Sequence-Aware Constrained Optimization Framework for Coupon
Distribution in E-commerce
Li Kong1*, Bingzhe Wang1*, Zhou Chen2, Suhan Hu1, Yuchao Ma1, Qi Qi1,4,5†, Suoyuan Song3,
Bicheng Jin3
1Gaoling School of Artificial Intelligence, Renmin University of China, China
2School of Economics and Management, Southeast University, China
3ByteDance, China
4Beijing Key Laboratory of Research on Large Models and Intelligent Governance
5Engineering Research Center of Next-Generation Intelligent Search and Recommendation, MOE
beverly kong@163.com,{wbz2022, 2023202249, yc.ma, qi.qi}@ruc.edu.cn,
chenzhou@seu.edu.cn,{songsuoyuan, jinbicheng}@bytedance.com
Abstract
Coupon distribution is a critical marketing strategy used by
online platforms to boost revenue and enhance user engage-
ment. Regrettably, existing coupon distribution strategies fall
far short of effectively leveraging the complex sequential in-
teractions between platforms and users. This critical over-
sight, despite the abundance of e-commerce log data, has pre-
cipitated a performance plateau. In this paper, we focus on the
scene that the platforms make sequential coupon distribution
decision multiple times for various users, with each user in-
teracting with the platform repeatedly. Based on this scenario,
we propose a novel marketing framework, namedSequence-
AwareConstrainedOptimization (SACO) framework, to di-
rectly devise coupon distribution policy for long-term rev-
enue boosting. SACO framework enables optimized online
decision-making in a variety of real-world marketing scenar-
ios. It achieves this by seamlessly integrating three key char-
acteristics, general scenarios, sequential modeling with more
comprehensive historical data, and efficient iterative updates
within a unified framework. Furthermore, empirical results on
real-world industrial dataset, alongside public and synthetic
datasets demonstrate the superiority of our framework.
Introduction
In the highly competitive online ecosystem, coupon distri-
bution has emerged as a central marketing strategy for on-
line platforms looking to amplify user engagement and opti-
mize revenue streams. Coupons take many forms (as shown
in Figure 1), from traditional discounts to service upgrades
and cash rewards, all designed to incentivize consumption
across diverse sectors. For instance, Booking’s promotional
activities can enhance user satisfaction (Goldenberg et al.
2020; Albert and Goldenberg 2022); Airbnb employs dy-
namic pricing (Ye et al. 2018); Uber’s promotions encourage
users to adopt new products (Du, Lee, and Ghaffarizadeh
2019); Taobao’s discounts increase user activity (Zhao et al.
*These authors contributed equally.
†Corresponding Author.
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
100 dollars
80 dollars!
Cash OFF
Discount Coupon
Guess what? You got
 upgraded!
Flight
Promotion
Upgraded to
the suite with
a Jacuzzi!
Services Upgrades
Cash Reward
Crack
Golden
Eggs
You cracked it!
You got the prize!
Figure 1: Complex and Meaningful Coupon Distribution.
2019; Zhang et al. 2021); Kuaishou offers cash rewards to
stimulate user retention (Ai et al. 2022); and Meituan uti-
lizes spend&save discounts to incentivize purchases (Zhou
et al. 2023; Huang et al. 2024; Zhou et al. 2024).
However, these marketing campaigns come with sig-
nificant costs. Typically, dedicated budgets are set to en-
sure campaign sustainability. Effective coupon distribution
within these finite budgets is therefore a critical challenge,
frequently formalized as a constrained optimization prob-
lem. Unlike traditional resource allocation, coupon distri-
bution under budget constraints faces two significant chal-
lenges. First, user responses are variable and the counter-
factual outcomes are fundamentally unobservable. Second,
user responses are sequential, which means past coupon de-
cisions affect users’ subsequent responses, making counter-
factual prediction challenging. As a result, it is impossible
to obtain a direct solution.
While prior research has explored counterfactual policy
optimization from logged bandit feedback (Swaminathan
and Joachims 2015b,a; Joachims, Swaminathan, and De Ri-
jke 2018), the bandit approach relies on online explo-
ration, rendering it unsuitable for coupon distribution in e-
commerce scenarios where decisions, once made, are dif-
ficult to reverse. In contrast, more recent studies acknowl-
arXiv:2508.09198v2  [cs.LG]  2 Feb 2026

Timeline
E-commerce Platform
Figure 2: Single-Round Scenarios in Existing Research.
edge the importance of pre-training models with logged data
before deployment, representing a significant improvement.
However, they typically focus on scenarios where the plat-
form makes a single-round coupon allocation decision for
each user interaction according to the current state. The
prevailing two-stage approach dominates coupon allocation
research (Hansotia and Rukstales 2002; Zhao et al. 2019;
Goldenberg et al. 2020), comprising: (1) machine learning
(ML) prediction of user response to different coupons, and
(2) optimization research (OR) for revenue maximization.
However, decoupling the process into two stages leads to er-
ror accumulation, and the two-stage goals cannot be fully
aligned. Recent end-to-end frameworks, including decision-
focused learning (DFL) (Zhou et al. 2023, 2024) and re-
inforcement learning (RL) (Xiao et al. 2019; Zhang et al.
2021), attempt to address this limitation. However, these ap-
proaches face inherent performance limitations when con-
strained to this single-round interaction paradigm, as illus-
trated in Figure 2. The top part visualizes the RL methods
modeling the interactions with single user as Markov pro-
cesses. In contrast, the bottom part shows Two-stage and
DFL methods making decisions based on current state alone.
In these settings, the potential for leveraging the richer se-
quential dependencies in user behavior is significantly cur-
tailed, leading to a performance plateau.
Unlike these single-round paradigms, our work, while
inheriting the benefits of an end-to-end framework, em-
braces the sequential nature of user engagement within e-
commerce platforms. We propose an efficient framework
namedSequence-AwareConstrainedOptimization (SACO)
framework to directly devise coupon distribution policy for
long-term revenue boosting. Critically, while demonstrated
here for coupon distribution, SACO’s general framework
empowers exploration of constrained optimization scenarios
across many applications. Our contributions are threefold:
Generalized and Practical Problem Setting.We ad-
dress more complex scenarios where: (1) multiple users ar-
rive simultaneously per round (e.g., group-buying scenar-
ios), requiring parallel coupon allocation; and (2) users may
revisit the platform across multiple rounds, creating sequen-
tial dependencies.
Efficient Framework.SACO framework offers two key
advantages: (1) by explicitly modeling the series of user in-
teractions and utilizing historical e-commerce data, SACO
captures valuable temporal dynamics overlooked by single-
round approaches; and (2) by reformulating sequential
decision-making as an auto-regressive prediction task, we
leverage causal-Transformer structure to effectively captur-
ing multi-round causal relationships. Meanwhile, this struc-
ture reduces the framework’s reliance on the statistical
premise of unbiased data, which serves as the training set
foundation for two-stage methods and DFL based on uplift
models. This allows for efficient, timely, and cost-effective
iterative updates, contributing to sustained optimal perfor-
mance in dynamic online environments.
Extensive Experiments on Public, Synthetic and In-
dustrial Datasets.We validate our approach through com-
prehensive experiments on diverse datasets. Comparisons
against state-of-the-art baselines demonstrate an average
revenue improvement of3.60%. Supporting experiments in-
clude ablation studies and inference speed analysis.
Further Related Work
Coupon distribution requires estimating user responses to
different coupon strategies, a task known as counterfactual
evaluation. A key metric is the conditional average treatment
effect (CATE), which quantifies the impact of a specific
coupon on outcomes like conversion rates, considering indi-
vidual user characteristics (Devriendt, Moldovan, and Ver-
beke 2018). Uplift modeling, a field dedicated to CATE esti-
mation, has produced various machine learning techniques,
often trained on randomized controlled trial (RCT) data
(Athey and Imbens 2015). The trained models then predict
individual-level causal effects for arbitrary interventions.
Notable CATE estimation techniques include meta-learners
(Hansotia and Rukstales 2002; Athey and Imbens 2015;
K¨unzel et al. 2019; Nie and Wager 2021), ranking-based
methods (Kuusisto et al. 2014; Betlei, Diemert, and Amini
2021), representation learning (Johansson, Shalit, and Son-
tag 2016; Shi, Blei, and Veitch 2019; Yao et al. 2018), and
causal forests (Ai et al. 2022; ATHEY , TIBSHIRANI, and
W AGER 2019; Wager and Athey 2018; Zhao, Fang, and
Simchi-Levi 2017). However, existing CATE formulations
primarily address single-treatment effects. In contrast, our
problem requires modelingtemporal treatment dependen-
cies, where user responses depend not only on the current
coupon but also on historical coupon exposures. This in-
troduces complex sequential counterfactual estimation chal-
lenges that traditional uplift models cannot address.
To tackle this challenge, we leverage the Transformer ar-
chitecture (Vaswani 2017), which has demonstrated remark-
able capabilities in sequential modeling across diverse do-
mains including natural language processing (Keskar et al.
2019; Dai et al. 2019), computer vision (Parvaiz et al. 2023),
and reinforcement learning (RL) (Chen et al. 2021; Zheng,
Zhang, and Grover 2022; Wu, Wang, and Hamaya 2023).
While prior RL applications focus on unconstrained op-
timization of cumulative rewards, we adapt the Decision
Transformer (DT) framework (Chen et al. 2021) for con-
strained optimization problems. Our modification enables
handling of budget constraints while preserving DT’s abil-
ity to model sequential dependencies in decision-making.

Coupon Distribution Problem
Model on Coupon Distribution
We formulate the coupon distribution problem as a budget
allocation problem with multiple treatments, which was also
introduced in many existing works. Different from them, we
consider a comprehensive scenario with sequential coupon
distribution decisions for diverse users who continuously in-
teract with the e-commerce platform.
An e-commerce platform hasNusers. Given the require-
ment that all users register on the platform before purchas-
ing,Nis a known parameter. Over a finite time horizon,
users interact with the platform for up toTtimes, referred
to asTrounds. Upon receiving a user interaction request, the
platform must make a real-time decision regarding coupon
issuance. Critically, once a coupon is granted, it cannot be
revoked. Over theTrounds, the platform has a marketing
budgetB, which is the total amount it is willing to spend on
issuing coupons to all users. The platform offersKtypes of
coupons, such as{2,5,10}dollar coupons forK= 3, and
so forth. Let[N],[T],[K]denote the sets of users, rounds,
and coupons, respectively.
We definex itk as the platform’s coupon issuance deci-
sion, wherex itk = 1indicates that in roundt, the platform
issues couponkto useri, withi∈[N], t∈[T], k∈[K].
Following coupon issuance, a user generates consumption
ritk, while the platform incurs a corresponding cost ofc itk
as a subsidy. The platform’s objective is to maximize rev-
enue from marketing within the limited budgetB. Formally,
we perform a linear relaxation onx itk and express the plat-
form’s online marketing problem as the following online op-
timization problem:
max
X
i∈[N],t∈[T],k∈[K]
ritkxitk (1)
s.t.
X
i∈[N],t∈[T],k∈[K]
citkxitk ≤B,(2)
0≤x itk ≤1,∀i∈[N], t∈[T], k∈[K].(3)
In previous research, the platform receives a request from
only one user per round. In this paper, we generalize this
constraint by allowing the platform to receive requests from
multiple users per round. For instance, in group-buying
scenarios, the platform needs to make coupon issuance
decisions for multiple users simultaneously. Furthermore,
by leveraging Transformer architectures to process multi-
dimensional action space, we allow the platform to issue a
bundle of coupons (e.g. the combination of 5-dollar coupon
and 10% discount) to each user per time, which aligns more
closely with real-world complex scenarios.
Dual Problem Formulation
Letxrepresent the coupon distribution strategy,R(x)de-
note the total revenue obtained by the platform under this
strategy, andC(x)represent the total amount of coupons
subsidized by the platform under this strategy. To obtain the
optimal distribution strategy within the budget constraint,
we first introduceλas the dual variable for the constraint
P
i∈[N],t∈[T],k∈[K] citkxitk ≤B. Next, we define the La-
grangian functionL(x, λ)and the objective function of the
dual problem is the maximum value of the Lagrangian func-
tion with respect tox, i.e.,
min
λ≥0
max
0≤xitk≤1
L(x, λ)(4)
= min
λ≥0
max
0≤xitk≤1
(R(x)−λ(C(x)−B))(5)
Problem (1) is formulated as a linear program. Therefore,
strong duality holds, implying that the we can find the op-
timal primal solution by solving the dual problem. Given
optimal dual variableλ ∗ and known parameterB, the opti-
mization objective simplifies to
max
0≤xitk≤1
(R(x)−λ ∗C(x)).(6)
Assuming all responses are known, the problem simplifies
to a classical multiple choice knapsack problem, yielding an
approximation ratio near 1(Zhou et al. 2023, 2024). How-
ever, the platform can only observe the actual revenue or
cost after a specific coupon decision and the counterfactual
data is inherently unattainable. Furthermore, user responses
are sequential. Previous coupon distribution decisions influ-
ence subsequent users’ coupon responses, making counter-
factual prediction challenging. Therefore, the online linear
programming problem cannot be directly solved.
Our Framework
To address the above challenge, we propose our frame-
work namedSequence-AwareConstrainedOptimization
(SACO) framework, a direct policy learning approach in-
volving training a model to determine the optimal sequential
policyx i for each userigivenλ, then leveraging aλopti-
mization algorithm and model-parallel inference to derive
the optimal overall strategyx.
Trajectory Representation
In the e-commerce platform, learning policies through direct
interaction with the online environment is infeasible. How-
ever, by organizing historical online logs into structured tra-
jectories, we unlock a feasible strategy for effective model
training. We model the sequential decision-making problem
for single-user and propose the trajectory representation as
the training dateset format.
The sequential decision-making problem is represented
by the tuple<S,A,P,R,C, γ >. Specifically,
•S: The state space, which describes the user context,
including user features and other relevant information.
st ∈ Srepresents the user context for all users in round
t, wheres t = (s1t, . . . , sit, . . . , sN t).
•A: The coupon distribution action space, which encom-
passes the choices of treatments for users.a t ∈ Arepre-
sents the coupon distribution strategy in roundt, where
at = (x1t1, . . . , xN t1, . . . , xitk, . . . , xN tK).
•P: The state transition function,P:S × A → S. The
transition dynamicsP(s t+1|st, at)describe the dynamic
transition from the current states t to the next states t+1
after taking an actiona t.

Figure 3: Constrained-Optimization Decision Transformer
•R: The reward space,R:S × A → R ∈R, which de-
scribes the platform revenue generated by coupon distri-
bution.r t ∈ Rrepresents the platform revenue in round
t, wherer t = P i∈[N] rit andr it = P k∈[K] ritk.
•C: The cost space,C:S × A → C ∈R, which describes
the marketing budget expenditure incurred by coupon
distribution actions.c t ∈ Crepresents the marketing bud-
get expenditure in roundt, wherec t = P i∈[N] cit and
cit = P k∈[K] citk.
•γ: The discount factor for future rewards, indicating the
importance of future rewards relative to the present. In
this paper, we setγ= 1.
Given a dataset in the format (user-id, user-features as
state, treatment as action, cost, reward, time) and additional
λrandomized in the interval(0,1), we aggregate the dataset
by user-id and then sort the data with each user’s group in
chronological order. We defineRT Git = PT t′=t γrit (Chen
et al. 2021) andCT Git = PT t′=t cit. The training dataset is
pre-processed into trajectory data of sizeN:
τi∈[N] =[(si0 , ai0 , CT Gi0 , RT Gi0 , λi), . . . ,
[(sit , ait , CT Git , RT Git , λi), . . . ,
(siT , aiT , CT GiT , RT GiT , λi)]
As mentioned above, the dual variableλreflects the con-
straint on the budgetB. To improve the model’s ability to
generalize across diverse budget levels, we randomizeλten
times for each trajectory sample. This expands our training
dataset tenfold, promoting more robust learning.
Constrained-Optimization Decision Transformer
Having established the training dataset, we adapt the Deci-
sion Transformer model and align it for direct policy learn-
ing, as summarized in Figure 3 and Algorithm 1.
Our model leverages two key advantages of the causal
transformer structure, the ability to handle sequential data
effectively via its transformer architecture and the capability
to evaluate counterfactual outcomes through its causal struc-
ture(Nichani, Damian, and Lee 2024).
To integrate constraint information, we augment the in-
put space with the parametersctg, representing constraint
Algorithm 1: Model Training
Input:State dimensiond s, action dimensiond a
Maximum episode lengthT, sequence lengthK
Parameter: Learning ratesη, weight decayβ
Output: Trained modelθ
1:Initialize:θ, AdamW(θ, η, β)
2:forepoch= 1toN epochs do
3:Sample batchB={(s t, at,rtg t,ctg t, t, λ)}j+K t=j
4:Normalize states:s t ←(s t −µ s)/σs
5:Compute embeddings:
6:e s ←Embed(s t) +Embed(t) +Embed(λt)
7:e a ←Embed(a t) +Embed(t) +Embed(λt)
8:e dRT G←Embed( dRT Gt) +Embed(t) +Embed(λt)
9:e dCT G←Embed( dCT Gt) +Embed(t) +Embed(λt)
10:Stack embeddings:x←Stack(e s, ea, edRT G, edCT G)
11:Apply layer norm:x←LayerNorm(x)
12:for each transformer blockBlock i do
13:x←Block i(x)
14:end for
15:Predict:ˆa t
16:Compute task losses:L a
17:BackpropagateL a and updateθusing optimizers
18:end for
19:returnTrained modelθ
types. Furthermore, we enhance the original time embed-
dingEmbed(t)by incorporating the dual variable embed-
dingEmbed(λ), as shown in line 6-9 of Algorithm 1.
This enhancement effectively encoded constraint informa-
tion alongside temporal signals for each parameter. Subse-
quently, these augmented inputs are processed through the
Causal Transformer blocks, with the internal details visual-
ized in the left panel of Figure 3.
As shown in line 16 of Algorithm 1, we employed a cross-
entropy loss calculated on the action predictions:
La(θ) =− 1 N T
NX
i=1
TX
t=1
KX
j=1
yitj log(pθ(ait =j ′|sit))(7)
only whenj=j ′, theny itj = 1, meaning that thej ′ type
of coupon is distributed to the user in the dataset and the

Algorithm 2: Overall Algorithm of SACO
Input: N, user statess, budgetB
Parameter: max iterations, noise, learning ratelr
Output:λ ∗,R ∗
1:Initialize:λ←Uniform(0,1)
2:Define Function OBJECTIVE(λ):
3:Simulate all users withλthrough trained model
4:Compute total costCand total revenueR
5:penalty←λ·max(C(x)−B,0)
6:returnpenalty−R(x)
7:whileC > BorC < B−ϵdo
8:Reset the offline simulation environment
9:init←λ+Uniform(−noise,noise)
10:init←Clip(init,0,1)
11:Optimizeλusing SLSQP:
12:result←minimize(OBJECTIVE,init,SLSQP,bounds)
13:λ←result.x[0]{Updateλ}
14:R,C←(user states, λ)
15:ifR>R*andC≤Bthen
16:R*←R,λ ∗ ←λ
17:end if
18:λ←λ+lr·(C−B){Dynamic adjustment}
19:end while
20:returnλ ∗,R ∗
response is recorded and observable. This design choice en-
ables the model to learn optimal policies tailored to specific
optimization objectives and constraints.
Following training, we obtained the model capable of
making optimal sequential decisions for individual users,
conditioned on the dual variables.
Overall Strategy
Based on the trained model to determine the optimal se-
quential policyx i for each userigivenλ, we combine
it with theλoptimization algorithm, obtaining the SACO
framework to derive the optimal overall strategyx, as sum-
marized in Algorithm 2.
We adopt the SLSQP algorithm to optimize Lagrangian
multiplierλ, as it is versatile and robust. SLSQP eliminates
the need for fine-tuning while delivering reliable solutions
for practical engineering applications.
We set the objective of SLSQP algorithm as
λ·(C(x)−B)−R(x).(8)
Considering the limitation that the SLSQP algorithm may
fall into the local optimum, we will perform multiple rounds
of iterative optimization in our framework. In each new
round of iterative optimization process, we will add some
noise disturbance and penalty onλto appropriately guide
the update direction, shown in line 9 and 18 of Algorithm 2.
Assumption 1WhenC(x)> C(x ′), thenR(x)> R(x ′).
We operate under the assumption of a direct correlation
between reward magnitude and associated cost, an obser-
vation validated by typical marketing and advertising prac-
tices. Hence, we define the convergence criterion for itera-
tion asB−ϵ < C < B.
Finally, we obtain the overall framework to directly devise
coupon distribution policy for long-term revenue boosting.
Unlike prior single-round approaches, SACO, as a se-
quential modeling framework, unlocks the potential to ex-
tract complex user-platform interaction patterns from rich
datasets. Critically, while demonstrated here for coupon dis-
tribution, SACO’s general framework empowers exploration
of constrained optimization scenarios across a spectrum of
applications. Furthermore, its significant scalability allows
for straightforward integration of external components.
Experiment
In this section, we conduct experiments to evaluate the per-
formance of our proposed framework. Specifically, we com-
pare it with baseline algorithms, perform an ablation study
to assess the contribution of each component, and conduct
an inference speed analysis. Since both our framework and
the baselines may generate actions˜athat are not present
in the dataset trajectories, the corresponding revenue˜rand
cost˜cfor these actions are missing. To address this issue of
missing data, we follow the approach outlined in (Guo et al.
2024) and create an offline simulation environment based
on the tuples(s, a, r, c)within the existing trajectories. This
environment enables us to obtain the tuples(s,˜a,˜r,˜c)for
actions that are not included in the original trajectories.
Experimental Settings
DatasetTo demonstrate the robustness of our framework,
we leverage a diverse set of datasets including public bench-
marks, real-world industrial data, and synthetic simulations.
CRITEO-UPLIFT v2 (CU).The dataset is provided by
Criteo AI Labs at the AdKDD’18 workshop (Diemert et al.
2018) and comprises 13.9 million samples collected from
Randomized Controlled Trial (RCT). Each sample contains
12 features, a binary treatment indicator, and two response
labels, namely visit and conversion. We follow the approach
in (Zhou et al. 2023), extracting user feature columns ‘f0-
f11’ as states, ‘treatment’ as actions, ‘visit’ label as costs
and ‘conversion’ label as generated revenue.
MT-LIFT (MT).Collected from two months of coupon
marketing scenarios for food delivery(Huang et al. 2024),
the dataset contains nearly 5.5 million samples, which in-
clude 99 features, 5 types of treatment, and two response
labels: click and conversion. Similar to the CU dataset, we
process user feature columns ‘f0-f98’ as states, ‘treatment’
as actions, ‘click’ as costs and ‘conversion’ as revenue.
Synthetic Dataset (SY).We have developed a synthetic
dataset generation pipeline inspired by (Yan et al. 2023).
The dataset consists of 10,000 simulated users. Each user
interaction spans 10 timesteps, with an action space of four
treatments applied randomly with equal probabilities at each
timestep. The cost and reward is generated when the user
responds to the coupon with the response probability. Gaus-
sian noise is used to simulate state transitions.
Business Dataset (BD).To realistically evaluate the per-
formance of our model in real-world industrial scenar-
ios, we incorporate a recent business dataset originating
from ByteDance, a global leading technology company with

0.6 0.7 0.8 0.9 1.0
Budget
0.1
0.0
0.1
0.2
0.3
0.4
0.5
Revenue Difference
Low Medium High
Forest
SACO
DFCL
Bandit
CMDP25
CMDP50
CMDP75
(a) CU
0.6 0.7 0.8 0.9 1.0
Budget
0.2
0.1
0.0
0.1
0.2
0.3
0.4
0.5
Revenue Difference
Low Medium High
Forest
SACO
DFCL
Bandit
CMDP25
CMDP50
CMDP75 (b) MT
0.6 0.7 0.8 0.9 1.0
Budget
0.1
0.0
0.1
0.2
0.3
0.4
0.5
Revenue Difference
Low Medium High
Forest
SACO
DFCL
Bandit
CMDP25
CMDP50
CMDP75 (c) SY
0.6 0.7 0.8 0.9 1.0
Budget
0.1
0.0
0.1
0.2
0.3
0.4
0.5
Revenue Difference
Low Medium High
Forest
SACO
DFCL
Bandit
CMDP25
CMDP50
CMDP75 (d) BD
Figure 4: Evaluation Results
Dataset Metric SACO DFCL Bandit CMDP25 CMDP50 CMDP75 Forest
CU ROI1.11 1.052 1.072 1.053 1.053 1.052 1.087 BARate0.997 0.986 0.966 0.987 0.991 0.984 0.968
MT ROI1.105 1.106 1.06 1.053 1.054 1.059 1.088 BARate1.0 0.926 0.988 0.989 0.984 0.984 0.952
SY ROI1.109 1.073 1.066 1.053 1.053 1.057 1.101 BARate0.999 0.977 0.978 0.983 0.986 0.98 0.934
BD ROI1.126 1.069 1.067 1.05 1.057 1.052 1.101 BARate0.996 0.981 0.983 0.979 0.984 0.985 0.919
Table 1: Performance Comparison Across Datasets and Baselines
a range of popular platforms. User features included are
anonymized to ensure data privacy and compliance. The
marketing dataset consists of millions of samples, includ-
ing anonymized user features as states, treatments as actions,
‘cost’ label as costs and ‘is paid’ label as revenue.
For all datasets, we randomly split them separately, using
80% of the samples for training and 20% for testing. After
initial data cleaning to remove anomalies, we aggregate the
data by user ID or relatively stable user feature. Within each
aggregated group, we subsequently sort the data chronolog-
ically to generate trajectory samples.
Evaluation Metrics
• Revenue (R(x)): A crucial factor in measuring market-
ing effectiveness is the platform revenue generated by the
marketing efforts.
• Return on Investment (ROI) ( R(x) C(x) ): The emphasis on the
ROI indicator is paramount. Without proper considera-
tion of cost, the strategy risks favoring marketing activ-
ities targeting users with both high returns and high as-
sociated expenditures. It leads to a suboptimal outcome
and inefficient resource allocation.
• Budget Allocation Rate (BARate) ( C(x) B ): Effective coupon distribution requires assessing user sensitivity
beforehand. Successful strategies will exhibit high bud-
get utilization, implying that coupons are effectively tar-
geted at highly sensitive users.
Evaluation Experiments
Baseline Algorithms
• CausalForest(Athey and Wager 2021): This baseline
model, commonly used in marketing scenarios, is trained
on historical data to predict individual treatment effects
(ITE). At each decision point, the model estimates the
treatment effect of offering a coupon and allocates it only
if the predicted effect is positive.
•Bandit(Chapelle and Li 2011): We employ a multi-arm
bandit algorithm based on Thompson Sampling (TS).
This algorithm leverages Bayesian methods to construct
a belief over the reward distribution of actions.
• Constrained Markov Decision Process (CMDP) (Xiao
et al. 2019): For differentλvalues, the CMDP model
needs to be retrained. Hence, we established three CMDP
baselines,CMDP25,CMDP50andCMDP75, by re-
training the core policy network withλvalues of 0.25,
0.5, and 0.75, respectively.
• Decision Focused Causal Learning (DFCL) (Zhou et al.
2024): The DCFL baseline is a state-of-the-art method
that claims to achieve breakthrough performance by
building upon two-stage approaches. It is an end-to-end
framework, aiming to align the prediction objective with
the ultimate decision-making goal.
Experimental ResultsTo establish a clear baseline, we
select the Forest algorithm as our benchmark model. Figure
4 presents the revenue difference between evaluated models
and the causal forest benchmark. We choose Forest due to its
widespread adoption in marketing platforms, known for its
robust causal learning capabilities. It is an appropriate and
meaningful point of comparison.
To assess budget constraint robustness, we defined three
budget levels: Low, Medium, and High, representing strict
to loose constraints. Within each level, we specify three dis-
tinct budget amounts. All budget values are normalized to
avoid dependence on specific numerical scales and ensure

0.5
 0.0 0.5 1.0
Ours
No-constraint
No-RTG
1.17
0.00
0.00
Budget = 0.5625
0.5
 0.0 0.5 1.0 1.5
1.57
0.00
0.00
Budget = 0.75
1
 0 1 2
2.06
1.80
1.74
Budget = 1.0
Cost Revenue Budget Limit
Figure 5: Ablation Study on MT Dataset.
generalizability across different scenarios.
The experimental results in Figure 4 demonstrate that our
proposed SACO framework gains higher revenue compared
to baselines across all datasets and budget levels, with two
exception: the medium budget level in the SY dataset and
MT dataset. SACO achieves an average revenue improve-
ment of3.60%. Furthermore, Table 1 highlights SACO’s
superior performance in terms of both average ROI and
BARate across the tested budget range. This overall supe-
rior performance emphasizes SACO’s strong strategy learn-
ing capabilities, robust causal reasoning, and adaptability to
diverse dataset characteristics.
We hypothesize that SACO’s slightly lower revenue than
DFCL at the medium budget level in MT is because DFCL,
developed by Meituan, may be particularly suited to the
Meituan dataset. Regarding the slightly lower revenue com-
pared to Forest at the medium budget level in the SY dataset,
this is attributed to the uniform distribution of actions within
that specific synthetic dataset. It is worth noting that for-
est and uplift models often benefit from training on unbi-
ased RCT data, which features a uniform distribution of ac-
tions. However, online deployment would typically utilize
an optimized strategy like DFCL algorithm, rather than a
random coupon distribution, which means the newly sam-
pled data inherently introduces selection bias. While some
existing methods don’t detail how their models would be it-
eratively updated under these biased conditions, our SACO’s
implicit causal learning approach offers a distinct advan-
tage. By reducing its reliance on the statistical premise of
unbiased data, SACO allows for efficient, timely, and cost-
effective iterative updates, contributing to sustained optimal
performance in dynamic online environments.
Ablation Study
Ablation Design
• No-constraint: We omit the parameterλand dRT Cfrom
our model, assessing their significance on learning and
respecting budget constraints.
• No- dRT G: We utilize the original Transformer model
(Vaswani 2017) without the dRT Gparameter to evaluate
its impact on the model’s capacity to pursue long-term
revenue, as opposed to immediate rewards.
Experimental ResultsWe conduct ablation studies in the
MT-LIFT public dataset. The experimental results are pre-
sented in Figure 5. The horizontal axis depicts revenue (pos-
itive values) and costs (negative values), while the vertical
axis lists the ablated algorithms. The dashed vertical line de-
notes the budget constraint.
Comparing our framework with No-constraint model re-
veals that removing constraint-related variables leads to a
diminished awareness of budgetary limitations. The model
fails to adequately respond to budgetary changes. Compar-
ing SACO to model withoutRT Gshows that, when the bud-
get is not sufficiently generous, the absence ofRT Gcauses
the model to marginally exceed the budget in pursuit of im-
mediate revenue gains. Furthermore, when budget is ample,
the absence of RTG guidance restricts overall revenue gen-
eration, rendering its performance inferior to SACO.
Inference Speed Analysis
Motivated by the demands of real-world applications, we
conduct inference efficiency experiments to validate the run-
time performance of SACO. The results are presented below.
Scenarios Time (ms) Hardware
Single-user 24.6243 CPU-only
Single-user 3.8128 NVIDIA RTX 4090
128 users 48.5075 NVIDIA RTX 4090
Table 2: Model Inference Time
Based on the results, SACO framework achieves an infer-
ence speed suitable for industrial applications. In addition,
we use 16 parallel models in the multi-user scenario, lim-
ited by CUDA memory. We anticipate that deployment in
industrial environments, equipped with superior computing
resources (e.g., larger GPU memory, parallel GPUs), will ef-
fectively mitigate this memory bottleneck.
Conclusion
In this paper, we propose SACO framework, sequentially
formulating coupon distribution strategies to enhance long-
term revenue. Our unified framework combines general sce-
narios, sequential modeling and efficient iterative updates.
Extensive experiments have been conducted to demonstrate
the superiority of our framework.
Future directions includes integrating SACO with exter-
nalities, such as incorporating user-to-user impact evalua-
tion as input features. Also, we plan to encode coupons to
prevent action space drift. This is in case we need to dynam-
ically adapt coupon types (e.g., larger discounts) based on
observed coupon performance.

Acknowledgments
This work was supported by National Natural Science Foun-
dation of China (No.62472428), Public Computing Cloud,
Renmin University of China, the fund for building world-
class universities (disciplines) of Renmin University of
China and ByteDance.
References
Ai, M.; Li, B.; Gong, H.; Yu, Q.; Xue, S.; Zhang, Y .;
Zhang, Y .; and Jiang, P. 2022. Lbcf: A large-scale budget-
constrained causal forest algorithm. InProceedings of the
ACM Web Conference 2022, 2310–2319.
Albert, J.; and Goldenberg, D. 2022. E-commerce promo-
tions personalization via online multiple-choice knapsack
with uplift modeling. InProceedings of the 31st ACM In-
ternational Conference on Information & Knowledge Man-
agement, 2863–2872.
Athey, S.; and Imbens, G. W. 2015. Machine learning
methods for estimating heterogeneous causal effects.stat,
1050(5): 1–26.
ATHEY , S.; TIBSHIRANI, J.; and W AGER, S. 2019. GEN-
ERALIZED RANDOM FORESTS.The Annals of Statis-
tics, 47(2): 1148–1178.
Athey, S.; and Wager, S. 2021. Policy learning with obser-
vational data.Econometrica, 89(1): 133–161.
Betlei, A.; Diemert, E.; and Amini, M.-R. 2021. Uplift mod-
eling with generalization guarantees. InProceedings of the
27th ACM SIGKDD Conference on Knowledge Discovery &
Data Mining, 55–65.
Chapelle, O.; and Li, L. 2011. An empirical evaluation of
thompson sampling.Advances in neural information pro-
cessing systems, 24.
Chen, L.; Lu, K.; Rajeswaran, A.; Lee, K.; Grover, A.;
Laskin, M.; Abbeel, P.; Srinivas, A.; and Mordatch, I. 2021.
Decision transformer: Reinforcement learning via sequence
modeling.Advances in neural information processing sys-
tems, 34: 15084–15097.
Dai, Z.; Yang, Z.; Yang, Y .; Carbonell, J.; Le, Q. V .; and
Salakhutdinov, R. 2019. Transformer-xl: Attentive lan-
guage models beyond a fixed-length context.arXiv preprint
arXiv:1901.02860.
Devriendt, F.; Moldovan, D.; and Verbeke, W. 2018. A liter-
ature survey and experimental evaluation of the state-of-the-
art in uplift modeling: A stepping stone toward the develop-
ment of prescriptive analytics.Big data, 6(1): 13–41.
Diemert, E.; Betlei, A.; Renaudin, C.; and Amini, M.-R.
2018. A large scale benchmark for uplift modeling. InKDD.
Du, S.; Lee, J.; and Ghaffarizadeh, F. 2019. Improve user
retention with causal learning. InThe 2019 ACM SIGKDD
Workshop on Causal Discovery, 34–49. PMLR.
Goldenberg, D.; Albert, J.; Bernardi, L.; and Estevez, P.
2020. Free lunch! retrospective uplift modeling for dynamic
promotions recommendation within roi constraints. InPro-
ceedings of the 14th ACM Conference on Recommender Sys-
tems, 486–491.
Guo, J.; Huo, Y .; Zhang, Z.; Wang, T.; Yu, C.; Xu, J.; Zheng,
B.; and Zhang, Y . 2024. Generative Auto-bidding via Con-
ditional Diffusion Modeling. InProceedings of the 30th
ACM SIGKDD Conference on Knowledge Discovery and
Data Mining, 5038–5049.
Hansotia, B. J.; and Rukstales, B. 2002. Direct marketing
for multichannel retailers: Issues, challenges and solutions.
Journal of Database Marketing & Customer Strategy Man-
agement, 9: 259–266.
Huang, Y .; Wang, S.; Gao, M.; Wei, X.; Li, C.; Luo, C.; Zhu,
Y .; Xiao, X.; and Luo, Y . 2024. Entire Chain Uplift Model-
ing with Context-Enhanced Learning for Intelligent Market-
ing. InCompanion Proceedings of the ACM on Web Confer-
ence 2024, 226–234.
Joachims, T.; Swaminathan, A.; and De Rijke, M. 2018.
Deep learning with logged bandit feedback. InInternational
Conference on Learning Representations.
Johansson, F.; Shalit, U.; and Sontag, D. 2016. Learning rep-
resentations for counterfactual inference. InInternational
conference on machine learning, 3020–3029. PMLR.
Keskar, N. S.; McCann, B.; Varshney, L. R.; Xiong, C.;
and Socher, R. 2019. Ctrl: A conditional transformer lan-
guage model for controllable generation.arXiv preprint
arXiv:1909.05858.
K¨unzel, S. R.; Sekhon, J. S.; Bickel, P. J.; and Yu, B.
2019. Metalearners for estimating heterogeneous treatment
effects using machine learning.Proceedings of the national
academy of sciences, 116(10): 4156–4165.
Kuusisto, F.; Costa, V . S.; Nassif, H.; Burnside, E.; Page, D.;
and Shavlik, J. 2014. Support vector machines for differen-
tial prediction. InMachine Learning and Knowledge Dis-
covery in Databases: European Conference, ECML PKDD
2014, Nancy, France, September 15-19, 2014. Proceedings,
Part II 14, 50–65. Springer.
Nichani, E.; Damian, A.; and Lee, J. D. 2024. How trans-
formers learn causal structure with gradient descent.arXiv
preprint arXiv:2402.14735.
Nie, X.; and Wager, S. 2021. Quasi-oracle estimation of
heterogeneous treatment effects.Biometrika, 108(2): 299–
319.
Parvaiz, A.; Khalid, M. A.; Zafar, R.; Ameer, H.; Ali, M.;
and Fraz, M. M. 2023. Vision Transformers in medical com-
puter vision—A contemplative retrospection.Engineering
Applications of Artificial Intelligence, 122: 106126.
Shi, C.; Blei, D.; and Veitch, V . 2019. Adapting neural net-
works for the estimation of treatment effects.Advances in
neural information processing systems, 32.
Swaminathan, A.; and Joachims, T. 2015a. Batch learn-
ing from logged bandit feedback through counterfactual risk
minimization.The Journal of Machine Learning Research,
16(1): 1731–1755.
Swaminathan, A.; and Joachims, T. 2015b. Counterfac-
tual risk minimization: Learning from logged bandit feed-
back. InInternational Conference on Machine Learning,
814–823. PMLR.

Vaswani, A. 2017. Attention is all you need.Advances in
Neural Information Processing Systems.
Wager, S.; and Athey, S. 2018. Estimation and inference of
heterogeneous treatment effects using random forests.Jour-
nal of the American Statistical Association, 113(523): 1228–
1242.
Wu, Y .-H.; Wang, X.; and Hamaya, M. 2023. Elastic deci-
sion transformer.Advances in neural information processing
systems, 36: 18532–18550.
Xiao, S.; Guo, L.; Jiang, Z.; Lv, L.; Chen, Y .; Zhu, J.; and
Yang, S. 2019. Model-based constrained MDP for budget
allocation in sequential incentive marketing. InProceedings
of the 28th ACM International Conference on Information
and Knowledge Management, 971–980.
Yan, Z.; Wang, S.; Zhou, G.; Lin, J.; and Jiang, P.
2023. An end-to-end framework for marketing effective-
ness optimization under budget constraint.arXiv preprint
arXiv:2302.04477.
Yao, L.; Li, S.; Li, Y .; Huai, M.; Gao, J.; and Zhang, A. 2018.
Representation learning for treatment effect estimation from
observational data.Advances in neural information process-
ing systems, 31.
Ye, P.; Qian, J.; Chen, J.; Wu, C.-h.; Zhou, Y .; De Mars, S.;
Yang, F.; and Zhang, L. 2018. Customized regression model
for airbnb dynamic pricing. InProceedings of the 24th ACM
SIGKDD international conference on knowledge discovery
& data mining, 932–940.
Zhang, Y .; Tang, B.; Yang, Q.; An, D.; Tang, H.; Xi, C.;
Li, X.; and Xiong, F. 2021. BCORLE (lambda): An Of-
fline Reinforcement Learning and Evaluation Framework
for Coupons Allocation in E-commerce Market.Advances in
Neural Information Processing Systems, 34: 20410–20422.
Zhao, K.; Hua, J.; Yan, L.; Zhang, Q.; Xu, H.; and Yang,
C. 2019. A unified framework for marketing budget allo-
cation. InProceedings of the 25th ACM SIGKDD Interna-
tional Conference on Knowledge Discovery & Data Mining,
1820–1830.
Zhao, Y .; Fang, X.; and Simchi-Levi, D. 2017. Uplift mod-
eling with multiple treatments and general response types.
InProceedings of the 2017 SIAM International Conference
on Data Mining, 588–596. SIAM.
Zheng, Q.; Zhang, A.; and Grover, A. 2022. Online decision
transformer. Ininternational conference on machine learn-
ing, 27042–27059. PMLR.
Zhou, H.; Huang, R.; Li, S.; Jiang, G.; Zheng, J.; Cheng, B.;
and Lin, W. 2024. Decision focused causal learning for di-
rect counterfactual marketing optimization. InProceedings
of the 30th ACM SIGKDD Conference on Knowledge Dis-
covery and Data Mining, 6368–6379.
Zhou, H.; Li, S.; Jiang, G.; Zheng, J.; and Wang, D. 2023.
Direct heterogeneous causal learning for resource allocation
problems in marketing. InProceedings of the AAAI Confer-
ence on Artificial Intelligence, volume 37, 5446–5454.
