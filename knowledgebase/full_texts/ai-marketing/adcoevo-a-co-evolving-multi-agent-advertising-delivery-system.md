---
title: 'AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System'
url: https://arxiv.org/abs/2610.19454
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Tianzhu Hu
- Hang Yu
- Zeyuan Zhao
- Zeyu Pan
- Huan Luo
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.19454
pages: 20
chars: 69451
fetched_at: '2026-11-08T13:26:11+00:00'
kb_version: 1
---

# AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System

AdCoEvo: A Co-Evolving Multi-Agent Advertising
Delivery System
Tianzhu Hu 1,2,∗,‡,Hang Yu 3,∗,‡,Zeyuan Zhao 4,Zeyu Pan 4,Huan Luo 4,Chun Gan 4,†,
Mingzhe Cao 4,Liubin Wang 4,Mingming Li 1,†,Jiao Dai 1,Jizhong Han 1,Songlin Hu 1,2
1Institute of Information Engineering, Chinese Academy of Sciences
2School of Cyberspace Security, University of Chinese Academy of Sciences
3The University of Sydney 4JD.COM
hutianzhu@iie.ac.cn,hayu0853@uni.sydney.edu.au
{zhaozeyuan.6, panzeyu3, luohuan.12, ganchun1, caomingzhe1, wangliubin.ubi}@jd.com
{limingming, daijiao, hanjizhong, husonglin}@iie.ac.cn
∗Equal contribution, †Corresponding authors, ‡Work was done during internship.
Abstract
Digital advertising is an important means for platforms to reach potential users and drive business
growth. Advertising delivery is the core link between marketing objectives and actual returns.
Existing methods have achieved partial automation in individual tasks such as bidding and budget
allocation, but they still rely on human operators for overall coordination, making it difficult to
support large-scale operations. They also often fail to achieve optimal performance, and individual
experience remains difficult to turn into reusable operational capabilities. In addition, as advertising
markets change, advertising delivery systems need timely strategy updates to remain effective in
dynamic markets. To automate the entire advertising operations process and improve adaptability
to market changes, we propose AdCoEvo, a co-evolving multi-agent advertising delivery system.
Specifically, the system connects delivery decisions across different timescales and operational
granularities through role specialization. Diagnostic results guide account planning and strategy
adjustment in the next period. The multi-agent system updates its model parameters based on
actual delivery outcomes and continually improves delivery strategies through mutual feedback
among planning, adjustment, and diagnosis, thereby achieving co-evolution. Experiments show
that, relative to the rule-based operational baseline (Rule), AdCoEvo increases advertiser value by
14.02% while reducing cost per acquisition by 7.07%. Compared with a multi-agent system with
fixed parameters, AdCoEvo increases advertiser value by 3.96% and reduces cost per acquisition
by 1.24%, indicating that co-evolution can yield greater delivery returns.
Code:https://github.com/jd-opensource/AdCoEvo
1 Introduction
Digital advertising is an important channel for platforms to reach potential users and drive business growth.
Turning marketing objectives into returns requires continuous high-quality advertising delivery decisions under
budget constraints [1]. As shown on the left of Figure 1, existing delivery workflows still rely heavily on
1
arXiv:2610.19454v1  [cs.AI]  14 Oct 2026

(a) Human-Led Advertising Operations
Manual task-by-task decisions
(b) Co-Evolving Multi-Agent Advertising Delivery System
Role-specialized multi-agent coordination
Account-Level Planning
Unit-Level Actions tCPA
Review & Diagnosis
AdCoEvo
Multi-Agent System
Planner
Account-Level Planning
Optimizer
Unit-Level Actions
tCPA
Inspector
Review & Diagnosis
$
Budget Allocation
$
Budget Allocation
Labor Scales
with Operations
Heavy Reliance on
Individual Expertise
Limited Adaptability
to Dynamic Markets
Scalable Automated
Operations
Operational experience
can be accumulated
Enhanced Adaptability
to Dynamic Markets
Paradigm Shift
Figure 1From manual to multi-agent advertising delivery.
manual configuration and experience-based judgment by operators [2]. As operations grow, limited manpower
and responsiveness make this approach difficult to scale and often prevent optimal performance [2]. Operators’
accumulated experience is also hard to turn into reusable operational capabilities for later delivery.
Prior work has automated individual tasks, such as bidding [1, 3] and budget allocation [4–6], but overall
advertising operations still rely on human coordination. More recently, large language model agents have
begun to take on decisions across the entire advertising delivery process. AdPilot uses a Reflector–Actor
workflow: it first generates a diagnosis from current metrics and historical trends, then makes delivery decisions
based on that diagnosis, and improves agent capabilities through a series of post-training steps [2].
Training policies for the entire delivery process requires linking business feedback to specific decisions. Budget
planning and ad-unit adjustments continue to affect subsequent delivery, and their effects need to be evaluated
through cumulative returns; post-delivery diagnosis takes effect through planning and adjustment in the next
period. Organizing multi-agent collaboration by operational responsibility therefore also requires constructing
training signals according to each decision’s scope of influence and feedback timing, and scheduling role
updates after feedback settlement, enabling models to co-evolve during continuous delivery.
Meanwhile, the advertising delivery market is not static: a continually changing auction environment may
create a mismatch between historical strategies and current conditions, requiring timely updates to delivery
strategies [3, 7]. Beyond autonomous execution, we therefore need to study how multi-agent systems use
continuous business feedback to adjust strategies and jointly adapt to market changes through collaboration.
To automate the entire advertising delivery process and improve adaptability to market changes, we propose
AdCoEvo, a co-evolving multi-agent advertising delivery system. As shown on the right of Figure 1, the
system connects decisions across different timescales and operational granularities by assigning separate
responsibilities for account-level budget planning, ad-unit delivery strategy adjustment, and end-of-period
diagnosis. Diagnostic results guide account planning and strategy adjustment in the next period. After
offline training, the system updates one role per period in rotation using settled feedback, while keeping
other roles’ parameters fixed. The updated policy takes effect in the next period. Through joint execution, it
changes the delivery states and training feedback encountered by other roles, which adapt their policies in
later rotations. We call this mutual adaptation across periods co-evolution. Experiments show that AdCoEvo
improves advertiser value (ADV) and reduces cost per acquisition (CPA) in both environments.1 Compared
with a multi-agent system with fixed parameters, co-evolution can yield greater delivery returns.
Our main contributions are as follows:
1. We propose AdCoEvo, a co-evolving multi-agent advertising delivery system that connects account budget
planning, ad-unit delivery strategy adjustment, and post-delivery diagnosis through role specialization
across different timescales and operational granularities, enabling autonomous delivery across periods.
1ADV = P(tCPA×pCVR)over valid impressions [8];CPA =total spend/total conversions [9]. Here, tCPA is the target
cost per acquisition and pCVR is the predicted conversion probability.
2

2. We develop a co-evolution framework for continuous advertising delivery in which the multi-agent system
updates policies using settled business feedback and jointly adapts to changes in delivery as its decisions
influence one another.
3. We validate the system’s delivery performance across different market sequences and compare role com-
positions, training stages, and role-update schemes to analyze gains from role collaboration, operational
capability development, and co-evolution.
2 Related Work
2.1 Advertising Delivery
Research on advertising delivery has largely focused on automating individual tasks. Automated bidding has
progressed from optimizing bid functions under budget constraints [1] to using reinforcement learning [10, 11]
or generative modeling [12] for sequential decision-making. RTBAgent incorporates expert knowledge and
reflection on past experience into bidding decisions [13]. AdComB jointly optimizes budget allocation and
bidding [5], while HiBid uses a hierarchical mechanism to connect cross-channel budgets with within-channel
bidding [4]. AuctionNet evaluates automated bidding through traffic generation and auction interactions [14].
AdPilot supports end-to-end autonomous advertising delivery through a Reflector–Actor workflow informed
by current states and historical memory. Post-training further improves its delivery decisions [2]. AdCoEvo
organizes operational responsibilities into roles with separate policies. Period-end diagnosis guides account
planning and strategy adjustment in the next period, while settled feedback supports role-policy updates
during continuous delivery.
2.2 Multi-Agent Collaboration
The core advantage of multi-agent systems is decomposing complex processes into roles with clear responsi-
bilities. Roles address distinct objectives and contexts, then make collective decisions through interaction.
Studies have applied complementary roles and task decomposition to complex problem solving and workflow
automation, supporting multi-step tasks that are difficult for a single agent to complete independently [15–19].
Current research on multi-agent systems organizes role collaboration through standardized workflows, dynamic
task allocation, and runtime supervision [17, 20–23]. It also trains models using joint execution trajectories,
role evaluations, or interaction rewards to improve collaborative decision-making capabilities [24, 25]. Our
work focuses on the collaboration and continual evolution of multi-agent systems in advertising delivery tasks.
2.3 Agentic RL
Agentic RL uses feedback from environmental interactions to optimize multi-step decision-making and tool-use
policies [26–28]. For example, ReTool uses tool-call outcomes to improve when and how tools are called [29],
while AgentFlow uses multi-turn trajectories to improve planning policies [30]. MARTI uses multi-agent
interaction trajectories for distributed training updates [31].
We continually update role policies through alternating reinforcement learning, focusing on mutual adaptation
among roles during continuous delivery. Training signals reflect each role’s scope of influence and feedback
timing. Cross-period diagnosis and subsequent joint execution allow each role’s policy updates to shape
feedback for other roles’ subsequent decisions and learning.
3 Problem Formulation
We formulate continuous advertising delivery as sequential decision-making, with objectives for value generation
and conversion costs under budget and adjustment-count constraints.
3

3.1 Modeling Delivery Decisions
During delivery, the system plans ad-unit budgets within each account and adjusts control tCPA based on
the current state. The fixed underlying bidder uses these settings to bid for individual traffic opportunities.
At the end of the period, the system generates diagnostic guidance from settled outcomes to inform account
planning and strategy adjustment in the next period.
Index decisions chronologically under system policyπ. Decisioniuses currently observable information:
ui ∼π(· |hi).(1)
• Decision information hi consists of the current decision type and its observable delivery state,
historical execution records, and settled feedback. Historical diagnostic guidance forms part of this
information and informs subsequent account planning and strategy adjustment.
• Decision output ui: an account’s ad-unit budget allocations, control tCPA, and diagnostic guidance.
3.2 Business Objectives and Constraints
The system measures the business outcomes of delivery decisions using ADV and CPA, which reflect value
generation and conversion costs, respectively. LetA denote the set of controlled accounts andUa the set of
ad units in accounta. The total ADV across all controlled accounts in periodeis
Fe =
X
a∈A
X
j∈Ua
da,jqe,a,j,(2)
Here, da,j is the environment-provided initial tCPA of the ad unit, andqe,a,j is the sum of predicted conversion
probabilities for its valid impressions within the period. ADV is always calculated using the initial tCPA.
Control tCPA changes affect ADV through delivery outcomes, while its valuation basis stays fixed.
Let ¯Fe = Fe/|A| denote average ADV per account, andCe, Ne denote total spend and conversions across
controlled accounts in periode. Aggregate CPA isCe/Ne. We optimize these two objectives subject to budget
and adjustment-count constraints:
maximize
π∈Π

Eπ[ ¯Fe],− Eπ[Ce] Eπ[Ne]  ,
subject to
X
j∈Ua
be,a,j =B e,a,∀e, a,
be,a,j ≥0, v e,a,j ≤K,∀e, a, j.
(3)
•Policy setΠ: policies use only information observable at decision time; CPA requiresEπ[Ne]>0.
• Budget constraint: Be,a is the budget of accounta in period e, and be,a,j is the total budget limit of
ad unitj. Reallocation among ad units preserves the account’s total budget.
• Adjustment-count constraint: ve,a,j counts valid tCPA adjustments executed for ad unitj in period
e;Kis the maximum count per ad unit per period.
4 Method
AdCoEvo organizes advertising delivery through role collaboration. As shown in the upper part of Figure 2,
Planner handles account budget planning, Optimizer adjusts ad-unit delivery strategies, and Inspector turns
settled period outcomes into diagnostic guidance for the next period. Together, planning, adjustment, and
diagnosis form a collaborative process across periods.
The system adopts two-stage training. The first stage develops operational decision-making capabilities
through supervised fine-tuning and offline reinforcement learning. The second stage, shown in the lower part
of Figure 2, updates role parameters using settled business feedback during continuous delivery, enabling
co-evolution. The offline reinforcement learning and co-evolution algorithms are given in Appendices B.2
and C.3, respectively.
4

Multi-Agent System
Advertising Environment
Planner
Account budget planning
 Once after
W
 steps
Optimizer
Ad-unit strategy adjustment
 Each remaining step
Inspector
Period-end diagnosis
Reward settled next period
Decision context
Budget · spend
State · history
Prior guidance
Within-account
budget allocation
b
1
b
2
…
tCPA actions
 HOLD |
κ
j

d
j
Adjustments ≤
K
Next-period guidance
g
e
Fixed bidder
 Per-traffic bids
Advertising market
 Auctions · settlement
Settled outcomes
ADV
Spend
Conversions · CPA
Budgets &
tCPA actions
Per-step
observations
Settled
outcomes
Co-Evolution during Continuous Delivery
 Role buffers
Settled P/O records
 Settled I records
Settled records
Value estimation
h
V
r
PrefixValueModel
Policy optimization
P
O
I
One role per period
Next-period policies
 P
O
I
Updated policies
Execution / guidance
Training / policy update
Figure 2Role collaboration and continuous co-evolution in AdCoEvo. The upper panel shows delivery execution,
and the lower panel shows role-policy updates.
4.1 Role Specialization and Collaborative Execution
Account budget planning, ad-unit delivery strategy adjustment, and end-of-period diagnosis differ in their
scope of influence and feedback timing. AdCoEvo accordingly assigns these responsibilities to Planner,
Optimizer, and Inspector and maintains a separate policyπθr for each role, wherer∈ {P, O, I}and θr denotes
the role’s model parameters. This organization associates execution records for different responsibilities with
their corresponding training feedback. Planner and Optimizer make decisions for one account and its ad units
at a time, whereas Inspector aggregates period outcomes across all controlled accounts.
After observing W time steps, Planner uses observed delivery performance to allocate the account’s remaining
budget, outputting a proportionαj for each ad unit. Unitjthen has total budget limit
bj =c pre j +Rα j,(4)
Here, cpre j is the cumulative spend of ad unitj before planning, R = B− P j∈U cpre j is the account’s remaining
budget, and B and U denote the account’s total budget and set of ad units, respectively. The allocation
proportions satisfyα j ≥0and P j∈U αj = 1.
After budget planning, Optimizer determines at every remaining time step whether each ad unit in the account
needs a delivery strategy adjustment. Ad-unit actions include HOLD and a multiplier adjustment relative to
the initial tCPA. If an adjustment is selected and the unit’s number of valid adjustments in the current period
has not reachedK, Optimizer selectsκj from the available multiplier setK and updates the control tCPA to
bdj =κ jdj,(5)
Here, dj is the environment-provided initial tCPA. The current control value is retained for HOLD or when
valid adjustments reachK.
After period settlement, Inspector aggregates delivery performance, budget utilization, and action records
across the controlled accounts to generate diagnostic guidancege as part of the decision inputs of Planner and
Optimizer in the next period.
4.2 Role Reward Construction
Training feedback for Planner and Optimizer accounts for both value generation and cost control. For ADV,
spend, and conversionsF, C, Nwithin the corresponding aggregation scope, we define the proxy return
Q(F, C, N) =F−η(C−ρN) s ,(6)
5

Here, ρ is the mean initial tCPA of ad units in the settlement window, weighted by conversion counts;η
weights the cost deviationC−ρN; andsscales the reward.
Role rewards reflect the scope of influence and feedback timing of each decision. Planner coordinates the
account’s period budget and evaluates resource allocation using outcomes from observation end to period end.
Optimizer continually adjusts ad-unit delivery strategies, computes stepwise returns from value generation
and the cost deviation, and accumulates subsequent returns during training to account for the lasting effects
of its actions. Both rewards combine the current account’s return with a weighted overall return. Inspector
provides diagnostic guidance to Planner and Optimizer in the next period. Its reward is computed from
changes in overall feedback between adjacent periods once the next period’s delivery outcomes are settled:
rP a =Q a +ωQ all, r O a,t =Q a,t +ωQ all,t, r I e−1 =w ⊤(ye −y e−1).(7)
Here, Qa, Qall aggregate outcomes from observation end to period end for the current account and all controlled
accounts, respectively; time-indexed terms use current-step increments. The parameterω weights the overall
reward. The period feedback vectorye combines standardized ADV, conversions, the CPA constraint margin,
and the forced-HOLD rate across all controlled accounts, with fixed weightsw. Unsettled diagnoses are
excluded from training. Calculations appear in Appendices A.1–A.2.
4.3 Offline Development of Operational Capabilities
We first apply supervised fine-tuning [32, 33] on role-specific demonstration trajectories to learn action
semantics and structured output specifications. Offline reinforcement learning then uses delivery outcomes as
training feedback aligned with each role’s responsibilities to improve operational decisions further.
To compare different decisions from the same delivery state, the system fixes the other roles’ policies, samples
G candidate responses for the target role, and executes them separately, withJ r g denoting the return of
candidate g. Planner and Optimizer construct leave-one-out advantages [34]; Inspector evaluates the delivery
improvement from guidance against the baseline returnJ0 of a branch in which neither Planner nor Optimizer
receives diagnostic guidance. The candidate advantages are
Ar g =



J r g − 1 G−1 X k̸=g J r k , r∈ {P, O},
J I g −J 0, r=I.
(8)
Planner and Optimizer advantages are normalized by a scale, while Inspector retains the return difference
relative to the baseline without diagnostic guidance. We denote them bybAr g. Using the sequence-level clipping
approach of GSPO [35], we apply decision advantages to policy optimization over entire responses. For roler
with valid candidatesIr, we optimize
Lr off (θr) =− 1 |Ir| X g∈Ir min h ϱg bAr g,clip  ϱg,1−ε −,1 +ε + bAr g i +β bDKL.(9)
Here, ϱg is the length-normalized sequence importance ratio of the current policy to the sampling policy, and
bDKL measures the current policy’s deviation from a fixed reference policy. The parametersε−, ε+ and β
control the clipping range and KL penalty strength, respectively. The calculations for advantage processing,
the sequence ratio, and the KL term are detailed in Appendix B.1.
4.4 Co-Evolution during Continuous Delivery
Offline training compares candidate decisions while keeping the other roles’ policies fixed. During continuous
delivery, updated roles participate in joint execution again, changing subsequent delivery states and business
feedback, to which other roles must also adapt their decisions. AdCoEvo draws on SAO’s single-trajectory
asynchronous update idea [36] to construct training signals from settled execution trajectories.
6

At period end, the system settles current P/O rewards and constructs period feedbackye. Inspector generates
diagnostic guidance ge for the next period from the delivery outcomes. The system then settles the reward for
the previous diagnosisge−1, adds settled records to role buffers, and updates one role in rotation(P, O, I).
Other role parameters remain fixed, and the new policy takes effect in the next period.
Value Estimation and Policy Optimization.During continuous delivery, the system executes one response
at each decision point. Each role therefore maintains a separate lightweight value model, PrefixValueModel
Vϕr (h), which predicts a scalar return from the input before response generation. The model is continually
trained on settled feedback to provide a baseline for policy updates.
Let V − i denote the value prediction for nodei before the current round of updates. Planner and Inspector
subtract this baseline from their settled rewards. Optimizer combines current-step rewards and subsequent
value estimates through GAE [37]:
bAr i =
(
rr i −V − i , r∈ {P, I},
GAEi({rO k , V− k }), r=O. (10)
Optimizer successor nodes follow decision time within the same account and period.
Advantages remain fixed during the current round of policy optimization. The value model is trained
independently by regression, without propagating its gradients into the role language model. The entire
response corresponding to a decision shares the same action advantage. For a responsez of length L, input h,
and action advantage bA, we optimize
Lco−evo(θr) =−
bA
Z
LX
ℓ=1
mℓ ¯ϱℓ logπ θr (zℓ |h, z<ℓ),(11)
Here, mℓ is a token-selection mask based on the probability ratio between the current and behavior policies,
¯ϱℓ is a clipped importance weight with its gradient stopped, andZ = P ℓ mℓ > 0is the number of valid tokens.
KL is used only for monitoring and triggering rollback. Implementation details of advantage estimation, value
regression, and update control are provided in Appendices C.1–C.2.
Through subsequent joint execution, updated policies change the delivery states and feedback encountered by
other roles. These roles adjust their policies accordingly in later rotations, enabling the system to continually
evolve through collaboration.
4.5 Inference Time Complexity Analysis
AdCoEvo’s per-period inference overhead depends on both the number of model calls and the cost of each call.
Let n denote the number of decision points per period and|A| the number of controlled accounts. Planner is
called once per account after observation, Optimizer is called once per account at each decision point after
observation, and Inspector is called once globally at the end of the period. The number of model calls per
period is thereforeO(|A|n).
Let L denote the combined input and output length per call, which is affected by the number of ad units per
account and the length of historical records. For a fixed model size with KV caching, the computational cost
of Transformer self-attention isO(L2)per call, yielding the following per-period inference complexity
Cinfer =O

|A|nL2 .(12)
5 Experiments
We compare AdCoEvo with operational baselines and foundation models in delivery performance and overhead
across continuous market sequences. Ablations examine the roles of collaboration, operational capability
development, and diagnostic guidance. Role-update comparisons and market-switch experiments further assess
whether co-evolution continually improves delivery, while budget and parameter experiments test whether
these gains persist under different settings.
7

5.1 Experimental Setup
Experimental environment:Experiments use the AuctionNet simulator [14] with its official period length
and traffic volume. The environment contains 48 ad units that can purchase traffic. We control 12 units
organized into 3 accounts, each containing 4 units, all using Abid as the fixed underlying bidder. We use
two environments, AuctionNet (Sparse) and AuctionNet (General). The former uses the public simulation
environment, where each controlled account’s initial budget is1/12of the total budget of all units. For
AuctionNet (General), we calibrate the pValue generation scale, ad-unit budgets, and CPA constraints using
the public General dataset, while keeping the other auction mechanisms unchanged. Detailed configurations
are provided in Appendix D.
Evaluation metrics:Delivery performance is measured using ADV, CPA, and a composite score. For ADV,
which uses tCPA-weighted predicted conversion values [8], we report the per-period average of total ADV
across all controlled accounts within the evaluation scope. CPA is total spend divided by total conversions
over the same evaluation scope [9]. The invalid output rateIR is the fraction of responses that violate the
required format or action specifications, such as parsing failures, incorrect ad-unit decision counts, or tCPA
multipliers outside the allowed set. Each invalid response is counted once. With No Operation under the
same environment and budget as the reference, methodm’s composite score is
Scorem = ADVm ADV0 · CPA0 CPAm −IR m.(13)
Here, subscript0denotes No Operation, whose score is 1. Invalid output rates are reported as percentages in
tables and used as decimal fractions in the formula.
Comparison methods:We use No Operation, Rule, and AdPilot * as advertising delivery baselines to
compare delivery performance across different approaches to operational decision-making. No Operation
makes no operational adjustments, while Rule adjusts budgets and tCPA using hand-crafted CPA-based rules.
AdPilot* follows AdPilot’s Reflector–Actor workflow [2], where a single agent generates actions informed by
delivery diagnosis. AdCoEvo (Fixed) retains all roles and the diagnostic workflow, with model parameters fixed
at the offline GSPO checkpoint during evaluation. We also evaluate representative closed- and open-source
foundation models [38–41]2 that directly perform advertising delivery tasks, comparing delivery performance,
output validity, and operational overhead.
Implementation and evaluation:AdCoEvo uses Qwen3-8B [42] with separate LoRA parameters [43] for
each role. AdPilot* uses the same backbone and follows AdPilot’s post-training procedure [2], with SFT
followed by GRPO. Its model parameters remain fixed during formal evaluation. We set the observation
length toW= 12, with at mostK= 8tCPA adjustments per ad unit per period.
Each experimental group uses five independent market sequences of 50 consecutive delivery periods, matched
across methods. These sequences were not used for SFT, offline reinforcement learning, or selecting the
default parameters. AdCoEvo independently starts each sequence from the same offline GSPO checkpoint.
AuctionNet regenerates market conditions, including traffic and predicted conversion probabilities, each period,
while role policies and diagnostic guidance carry over within the sequence.
5.2 Overall Delivery Performance
We first examine whether AdCoEvo can achieve better delivery outcomes than fixed operational rules derived
from human experience. As shown in Table 1, relative to Rule, AdCoEvo increases ADV by 14.02% and reduces
CPA by 7.07% in the Sparse environment, while also improving both metrics in the General environment.
Human-designed rules can trigger adjustments based on delivery states, but their decision logic is specified in
advance. AdCoEvo instead uses delivery feedback for policy learning and continuous updates, allowing the
models to accumulate experience throughout delivery.
The comparison with AdPilot* further examines how end-to-end delivery decisions are organized. Both use
the same backbone model. With both systems’ parameters fixed during evaluation, AdCoEvo (Fixed) achieves
2Closed-source model documentation: GPT-5.6-Terra, Claude-Sonnet-5, and Gemini-3.1-Flash-Lite.
8

Table 1Delivery performance across market sequences. Overall aggregates results from five 50-period sequences.
Method Sequence 1 Sequence 2 Sequence 3 Sequence 4 Sequence 5 Overall
ADV↑CPA↓ADV↑CPA↓ADV↑CPA↓ADV↑CPA↓ADV↑CPA↓ADV↑CPA↓Score↑
AuctionNet (Sparse)
No Operation 26,440.6 115.575 26,372.9 115.676 26,175.7 117.539 26,598.1 116.739 26,286.4 115.531 26,374.7 116.207 1.0000
Rule 28,680.3 104.124 28,333.9 103.629 28,376.6 105.553 28,537.4 104.623 28,195.3 103.658 28,424.7 104.315 1.2006
AdPilot* 28,090.3 118.479 27,012.3 118.847 27,103.3 120.397 27,046.0 119.133 26,876.5 118.358 27,225.7 119.040 1.0077
AdCoEvo (Fixed) 31,720.6 98.368 30,709.7 98.583 30,615.4 100.112 31,675.0 99.104 31,154.9 97.600 31,175.1 98.150 1.3995
AdCoEvo 32,125.4 96.807 32,350.1 96.217 32,725.4 98.087 32,341.5 98.220 32,500.9 96.361 32,408.7 96.936 1.4731
AuctionNet (General)
No Operation 27,612.0 8.864 28,094.9 8.685 27,782.8 8.875 28,306.5 8.738 28,203.9 8.677 28,000.0 8.767 1.0000
Rule 29,917.9 7.199 30,282.6 7.084 30,244.9 7.266 30,513.2 7.143 30,147.7 7.077 30,221.3 7.153 1.3229
AdPilot* 28,688.2 9.122 28,604.6 8.879 28,223.2 9.147 28,762.7 8.979 28,336.0 8.806 28,522.9 8.985 0.9940
AdCoEvo (Fixed) 31,965.4 7.112 31,375.8 7.025 30,914.1 7.139 32,294.7 7.258 31,541.2 7.203 31,618.2 7.147 1.3852
AdCoEvo 33,164.4 7.069 33,009.5 6.892 32,507.9 7.068 33,744.4 6.944 32,334.3 6.975 32,952.1 6.989 1.4763
Table 2Delivery performance, API costs, and inference latency of AdCoEvo and foundation models in Sparse. Bold
values indicate the best results.
Business Performance Estimated API Cost Latency
Model ADV↑CPA↓IR (%)↓Score↑CNY/Period↓CNY/10K ADV↓P50(s)↓P95(s)↓Period(s)↓
Closed-Source
GPT-5.6-Terra 31,243.6 100.1760.001.3742 5.733 1.8348 3.84 5.27 710.8
Claude-Sonnet-5 31,024.5 100.027 3.22 1.3344 8.152 2.6275 9.18 15.30 1,340.0
Gemini-3.1-Flash-Lite 30,291.8 101.393 8.16 1.2348 0.683 0.2255 1.40 2.23 470.8
Open-Source
DeepSeek-V4-Pro 30,890.9 100.1470.001.3591 0.830 0.2688 3.96 6.62 724.4
Kimi-K3 29,055.5 102.191 8.98 1.1630 13.441 4.6258 15.33 82.97 3,346.1
GLM-5.2 28,056.8 109.419 8.74 1.0423 1.427 0.5084 17.86 34.19 2,170.3
Qwen3.5-397B-A17B 27,152.6 117.737 11.58 0.9003 2.334 0.8597 14.49 26.98 1,709.7
AdCoEvo
AdCoEvo 32,408.7 96.936 0.00 1.4731 0.235 0.0725 1.20 2.19 397.1
14.51% higher ADV and 17.55% lower CPA in Sparse. Compared with a single agent that handles delivery
decisions, AdCoEvo assigns operational responsibilities to roles that learn separately and provide feedback to
one another, enabling them to collaborate and co-evolve toward a shared business objective.
Across all five market sequences in both environments, AdCoEvo achieves the highest ADV and lowest CPA
among the compared methods. These results indicate its adaptability to changing markets.
5.3 Comparison with Foundation Models
We compare with foundation models to assess advertising-specific operational capabilities. As shown in
Table 2, AdCoEvo achieves the highest ADV, lowest CPA, and highest composite score. Compared with
GPT-5.6-Terra, the best-performing foundation model overall, it increases ADV by 3.73% and reduces CPA
by 3.23%. With a smaller model, domain-specific training and co-evolution can build operational capabilities
aligned with delivery objectives, improving value generation and cost efficiency.
In addition to delivery performance, AdCoEvo also has lower API costs. Based on actual API usage across all
roles and the corresponding listed prices,3 its average API cost is CNY 0.235 per period, 65.59% lower than
that of Gemini-3.1-Flash-Lite, the least expensive foundation model, and its cost per 10,000 ADV is CNY
0.0725. Lower API costs help scale advertising delivery.
Qwen3.5-397B-A17B, a larger model from the same Qwen family, does not achieve better delivery results,
further indicating that operational capability cannot be assessed by model size alone. Organizing decisions and
3Cost estimates use the OpenRouter prices recorded on September 1, 2026.
9

Table 3ADV and CPA of different role combinations
in Sparse without domain-specific post-training.
Table 4Training-stage ablation in Sparse.
Method ADV↑CPA↓
No Operation 26,374.7 116.207
Planner 26,682.1 125.751
Optimizer 25,004.8 113.410
P+O 26,243.8 121.240
P+O+I27,543.2 109.641
Method ADV↑CPA↓
No Operation 26,374.7 116.207
w/o Training 27,543.2 109.641
SFT 30,892.4 100.016
GSPO 31,175.1 98.150
AdCoEvo32,408.7 96.936
learning around the advertising delivery task provides another effective way to balance business performance
and operational cost, beyond simply increasing the size of the backbone model.
5.4 Ablation Analysis
5.4.1 Role Composition Ablation
To examine collaboration among specialized roles, we construct combinations of Planner, Optimizer, and
Inspector without domain-specific post-training. As shown in Table 3, using Planner alone increases ADV but
also raises CPA; using Optimizer alone reduces CPA but decreases ADV. Combining the two still does not
improve both metrics simultaneously. Adding Inspector increases ADV by 4.95% and reduces CPA by 9.57%
relative to the Planner–Optimizer combination. The full system outperforms No Operation on both metrics.
This change indicates that local improvements from individual roles do not simply add up to overall gains
when more agents are introduced. Budget planning and ad-unit adjustment influence one another and require
collaboration around a shared delivery objective. Inspector turns execution outcomes into diagnostic guidance
for Planner and Optimizer, enabling both roles to revise subsequent decisions using prior delivery feedback.
5.4.2 Policy Learning Stage Ablation
With all roles present, we compare four settings: before domain-specific post-training (w/o Training), SFT
alone, subsequent GSPO offline reinforcement learning, and co-evolution. As shown in Table 4, SFT increases
ADV and reduces CPA; subsequent GSPO further improves both metrics. Business performance improves with
training even when the division of roles remains unchanged, indicating that the collaborative structure alone
does not guarantee high-quality decisions; the corresponding operational capabilities also need to be developed.
Supervised demonstrations provide initial decision-making capabilities, while reinforcement learning further
optimizes delivery strategies using execution outcomes, making multi-agent collaboration more effective in
supporting value generation and cost control.
Compared with AdCoEvo (Fixed), AdCoEvo increases ADV by 3.96% and reduces CPA by 1.24% in Sparse. In
General, ADV increases by 4.22% and CPA decreases by 2.21%. This improvement shows that the operational
capabilities established through offline training still have room to improve. In a changing advertising market,
co-evolution enables the multi-agent system to continually improve its policies using new settled feedback,
yielding greater delivery returns on top of its existing collaboration and operational capabilities.
5.4.3 Co-Evolution Ablation
To study role participation and rotation, we retain all roles and compare Optimizer-only updates, Planner–
Optimizer updates, and AdCoEvo against AdCoEvo (Fixed). To equalize role-update counts, the first setting
updates Optimizer every period; the second alternates Planner and Optimizer across periods.
As shown in Table 5, full co-evolution achieves higher ADV and composite scores than updating Planner and
Optimizer across all five market sequences. Overall, ADV further increases by 2.88% and the composite score
by 2.78%, while CPA increases by only approximately 0.10%. This shows that, while retaining diagnostic
guidance, allowing Inspector to participate in co-evolution can further increase advertiser value at a similar
cost per acquisition, yielding higher delivery returns.
10

Table 5ADV and Score gains (%) over AdCoEvo (Fixed) under different role-update settings in Sparse. All settings
retain the complete role composition.
O gains P+O gains AdCoEvo gains
Seq. ADV↑Score↑ADV↑Score↑ADV↑Score↑
1 0.62 2.25 0.93 2.561.28 2.91
2 0.74 3.30 1.03 3.585.34 7.93
3 0.64 2.84 1.01 3.116.89 9.10
4 0.56 1.67 0.94 1.982.10 3.02
5 0.59 2.11 1.33 2.174.32 5.66
Overall 0.63 2.08 1.05 2.413.96 5.26
General (1-15)
Sparse (16-35)
General (36-50)
(a) ADV uplift (%)
-4
0
4
8
12
1
10
20
30
40
50
Delivery period
General (1-15)
Sparse (16-35)
General (36-50)
(b)
DCPA (%)
-12
-8
-4
0
4
1
10
20
30
40
50
Delivery period
AdCoEvo
Fixed GSPO (0%)
Figure 3ADV uplift and CPA change relative to AdCoEvo (Fixed) under market switches, averaged across five
market sequences using five-period windows.
To examine how co-evolution adapts to market changes, we switch from General to Sparse at period 16 and
back to General at period 36, comparing AdCoEvo with AdCoEvo (Fixed). We report results averaged over
five market sequences using five-period windows. As shown in Figure 3, AdCoEvo retains an ADV advantage
after the market switches and gradually recovers its CPA improvement after the return to General, showing
that co-evolution can improve adaptation to market changes.
5.4.4 Diagnostic Guidance Ablation
To examine the role of diagnostic guidance, we replace Inspector-generated diagnoses with fixed statistical
summaries and compare delivery performance under the two feedback settings. Relative to fixed statistical
summaries, Inspector-generated diagnoses increase ADV by 1.61% and reduce CPA by 1.55% in Sparse, with
corresponding improvements of 1.64% and 1.34% in General. This shows that converting delivery outcomes
into diagnostic guidance better supports subsequent account planning and strategy adjustment than providing
statistical information alone.
5.5 Budget Constraints and Parameter Sensitivity
To examine whether AdCoEvo’s delivery gains depend on a particular resource setting, we compare business
performance under different initial budgets. As shown in Figure 4, AdCoEvo achieves the highest ADV and
lowest CPA at 60%, 80%, and 100% of the original budget. Even when the budget is reduced to 60%, it
increases ADV by 7.17% and reduces CPA by 0.78% relative to AdCoEvo (Fixed). Tighter budgets require
the system to coordinate account planning and ad-unit adjustment with more limited resources, yet AdCoEvo
still improves both value generation and cost efficiency. Thus, co-evolution retains its gains over the fixed
offline policy at lower budgets.
In addition to budget, we examine the observation lengthW and the maximum number of tCPA adjustments
11

(a) 60%
ADV
CPA
0
0
10k
40
20k
80
30k
120
(b) 80%
ADV
CPA
0
0
10k
40
20k
80
30k
120
(c) 100%
ADV
CPA
0
0
10k
40
20k
80
30k
120
No Operation
Rule
AdPilot*
SFT
GSPO
AdCoEvo
Figure 4ADV (solid bars, left axis) and CPA (hatched bars, right axis) under different initial budgets in Sparse.
Table 6Effects of observation lengthWand adjustment limitKon delivery performance.
Parameter ADV↑CP A↓Score↑
Observation length
W= 629,547.0 97.742 1.3319
W= 12(default)32,408.7 96.936 1.4731
W= 1830,649.6 107.914 1.2514
Adjustment limit
K= 431,992.6 97.240 1.4496
K= 8(default)32,408.7 96.936 1.4731
K= 1231,268.6 99.510 1.3845
per ad unit per periodK. As shown in Table 6, the default setting ofW = 12and K = 8achieves the
highest ADV and lowest CPA among the configurations compared. ExtendingW from 6 to 12 improves both
metrics, whereas extending it further to 18 reduces performance. A longer observation period provides more
information before decisions are made but shortens the time during which planning and adjustment can affect
subsequent delivery, requiring a balance between observation and execution.
Reducing K from 8 to 4 decreases ADV by 1.28% and raises CPA by 0.31%, while performance remains close
to the default configuration under the tighter adjustment constraint. Relaxing the limit to 12 lowers ADV
and raises CPA, so more adjustment opportunities do not necessarily improve performance.
6 Discussion and Conclusion
We present AdCoEvo, a multi-agent system for advertising delivery that organizes delivery decisions through
role specialization across different timescales and operational granularities, and improves delivery policies
through offline development of operational capabilities and co-evolution. Experiments show that operational-
level decisions, role collaboration, and post-training all help improve delivery performance, while co-evolution
provides further gains beyond offline reinforcement learning.
However, gains vary across environments, and the effectiveness of co-evolution still needs evaluation in specific
delivery scenarios. How operational roles’ decision frequencies and scopes of influence affect co-evolution, and
how advantage estimation and update mechanisms can be improved accordingly, warrant further study to
help multi-agent systems use actual delivery feedback more effectively.
References
[1] Weinan Zhang, Shuai Yuan, and Jun Wang. Optimal real-time bidding for display advertising. InProceedings of
the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pages 1077–1086.
Association for Computing Machinery, 2014. doi: 10.1145/2623330.2623633. URLhttps://doi.org/10.1145/
2623330.2623633.
[2] Shuoshuo Sun, Qi He, Xiaoting Li, et al. AdPilot: Towards fully autonomous advertising delivery via agentic
reinforcement learning. InProceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data
12

Mining V.2, pages 8021–8031, 2026. doi: 10.1145/3770855.3818315. URLhttps://doi.org/10.1145/3770855.
3818315.
[3] Zhiyu Mou et al. Sustainable online reinforcement learning for auto-bidding. InAdvances
in Neural Information Processing Systems, volume 35, pages 2651–2663. Curran Associates, Inc.,
2022. doi: 10.52202/068431-0192. URL https://proceedings.neurips.cc/paper_files/paper/2022/file/
11faf17bf7e5412d9cded369f97db23d-Paper-Conference.pdf.
[4] Hao Wang et al. HiBid: A cross-channel constrained bidding system with budget allocation by hierarchical offline
deep reinforcement learning.IEEE Transactions on Computers, 73(3):815–828, 2024. doi: 10.1109/tc.2023.3343111.
URLhttps://doi.org/10.1109/tc.2023.3343111.
[5] Alessandro Nuara, Francesco Trovò, Nicola Gatti, and Marcello Restelli. A combinatorial-bandit algorithm for the
online joint bid/budget optimization of pay-per-click advertising campaigns.Proceedings of the AAAI Conference
on Artificial Intelligence, 32(1):2379–2386, 2018. doi: 10.1609/aaai.v32i1.11888. URLhttps://ojs.aaai.org/
index.php/AAAI/article/view/11888.
[6] Mingxuan Song, Yusen Huo, Bohan Zhou, Shenglin Yin, Zhen Xiao, Jieyi Long, Zhilin Zhang, and Chuan Yu.
DARA: Few-shot budget allocation in online advertising via in-context decision making with RL-finetuned LLMs.
InProceedings of the ACM Web Conference 2026, pages 40–50. Association for Computing Machinery, 2026. doi:
10.1145/3774904.3792129. URLhttps://doi.org/10.1145/3774904.3792129.
[7] Lorenzo Croissant, Marc Abeille, and Clement Calauzenes. Real-time optimisation for online learning in auctions.
InProceedings of the 37th International Conference on Machine Learning, volume 119 ofProceedings of Machine
Learning Research, pages 2217–2226. PMLR, 2020. URLhttps://proceedings.mlr.press/v119/croissant20a.
html.
[8] Ashwinkumar Badanidiyuru. Model monotonicity in autobidding auctions: When do better predictions lead
to better outcomes? InProceedings of the 43rd International Conference on Machine Learning, volume 306 of
Proceedings of Machine Learning Research, pages 4802–4819. PMLR, 2026. URLhttps://proceedings.mlr.
press/v306/badanidiyuru26a.html.
[9] Google Ads. Average CPA: Definition. Google Ads Help, n.d. URLhttps://support.google.com/google-ads/
answer/6396841?hl=en. Accessed: 2026-10-11.
[10] Di Wu, Xiujun Chen, Xun Yang, Hao Wang, Qing Tan, Xiaoxun Zhang, Jian Xu, and Kun Gai. Budget constrained
bidding by model-free reinforcement learning in display advertising. InProceedings of the 27th ACM International
Conference on Information and Knowledge Management, pages 1443–1451. Association for Computing Machinery,
2018. doi: 10.1145/3269206.3271748. URLhttps://doi.org/10.1145/3269206.3271748.
[11] Han Cai, Kan Ren, Weinan Zhang, Kleanthis Malialis, Jun Wang, Yong Yu, and Defeng Guo. Real-time
bidding by reinforcement learning in display advertising. InProceedings of the Tenth ACM International
Conference on Web Search and Data Mining, pages 661–670. Association for Computing Machinery, 2017. doi:
10.1145/3018661.3018702. URLhttps://doi.org/10.1145/3018661.3018702.
[12] Jiayan Guo et al. Generative auto-bidding via conditional diffusion modeling. InProceedings of the 30th ACM
SIGKDD Conference on Knowledge Discovery and Data Mining, pages 5038–5049, 2024. doi: 10.1145/3637528.
3671526. URLhttps://doi.org/10.1145/3637528.3671526.
[13] Leng Cai et al. RTBAgent: A LLM-based agent system for real-time bidding. InCompanion Proceedings
of the ACM on Web Conference 2025, pages 104–113, 2025. doi: 10.1145/3701716.3715259. URL https:
//doi.org/10.1145/3701716.3715259.
[14] Kefan Su, Yusen Huo, Zhilin Zhang, et al. AuctionNet: A novel benchmark for decision-making in large-scale
games. InAdvances in Neural Information Processing Systems, volume 37, pages 94428–94452. Curran Associates,
Inc., 2024. doi: 10.52202/079017-2993. URL https://proceedings.neurips.cc/paper_files/paper/2024/
file/ab9b7c23edfea0011507f7e1eae82cd2-Paper-Datasets_and_Benchmarks_Track.pdf.
[15] Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, et al. CAMEL: Communicative agents for “mind”
exploration of large language model society. InAdvances in Neural Information Processing Systems, volume 36,
pages 51991–52008, 2023. doi: 10.52202/075280-2264. URLhttps://proceedings.neurips.cc/paper_files/
paper/2023/hash/a3621ee907def47c1b952ade25c67698-Abstract-Conference.html.
[16] Qingyun Wu, Gagan Bansal, Jieyu Zhang, et al. AutoGen: Enabling next-gen LLM applications via multi-agent
conversations. InFirst Conference on Language Modeling, 2024. URL https://openreview.net/forum?id=
BAakY1hNKS.
13

[17] Sirui Hong, Mingchen Zhuge, Jonathan Chen, et al. MetaGPT: Meta programming for a multi-
agent collaborative framework. InThe Twelfth International Conference on Learning Representa-
tions, pages 23247–23275, 2024. URL https://proceedings.iclr.cc/paper_files/paper/2024/hash/
6507b115562bb0a305f1958ccc87355a-Abstract-Conference.html.
[18] Chen Qian, Wei Liu, Hongzhang Liu, et al. ChatDev: Communicative agents for software development. In
Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), pages 15174–15186, Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi:
10.18653/v1/2024.acl-long.810. URLhttps://aclanthology.org/2024.acl-long.810/.
[19] Wei Tao, Yucheng Zhou, Yanlin Wang, Wenqiang Zhang, Hongyu Zhang, and Yu Cheng. MAGIS: LLM-based
multi-agent framework for GitHub issue resolution. InAdvances in Neural Information Processing Systems,
volume 37, pages 51963–51993, 2024. doi: 10.52202/079017-1647. URL https://proceedings.neurips.cc/
paper_files/paper/2024/hash/5d1f02132ef51602adf07000ca5b6138-Abstract-Conference.html.
[20] Boye Niu, Yiliao Song, Kai Lian, Yifan Shen, Yu Yao, Kun Zhang, and Tongliang Liu. Flow:
Modularized Agentic Workflow Automation. InInternational Conference on Learning Representa-
tions, pages 74949–74977, 2025. URL https://proceedings.iclr.cc/paper_files/paper/2025/hash/
ba84da6921f3040b74ee163aa7451f53-Abstract-Conference.html.
[21] Han Zhou, Xingchen Wan, Ruoxi Sun, Hamid Palangi, Shariq Iqbal, Ivan Vulić, Anna Korhonen, and Sercan Arik.
Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies. InInternational Conference on
Learning Representations, pages 15844–15872, 2026. URLhttps://proceedings.iclr.cc/paper_files/paper/
2026/hash/1ab4e0e8f35078109bc78d7b465d306f-Abstract-Conference.html.
[22] Fulin Lin, Shaowen Chen, Ruishan Fang, Hongwei Wang, and Tao Lin. Stop Wasting Your Tokens:
Towards Efficient Runtime Multi-Agent Systems. InInternational Conference on Learning Representa-
tions, pages 113497–113528, 2026. URL https://proceedings.iclr.cc/paper_files/paper/2026/hash/
b86a195e70f27017c514fa0e5f80595f-Abstract-Conference.html.
[23] Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chi-Min Chan, Heyang Yu, Yaxi Lu,
Yi-Hsin Hung, Chen Qian, Yujia Qin, Xin Cong, Ruobing Xie, Zhiyuan Liu, Maosong Sun, and Jie Zhou.
AgentVerse: Facilitating multi-agent collaboration and exploring emergent behaviors. InInternational Conference
on Learning Representations, pages 20094–20136, 2024. URL https://proceedings.iclr.cc/paper_files/
paper/2024/hash/578e65cdee35d00c708d4c64bce32971-Abstract-Conference.html.
[24] Sumeet Ramesh Motwani, Chandler Smith, Rocktim Jyoti Das, et al. MALT: Improving reasoning with multi-agent
LLM training. InSecond Conference on Language Modeling, 2025. URLhttps://openreview.net/forum?id=
jXP9bgFack.
[25] Xiangyuan Xue, Yifan Zhou, Guibin Zhang, Zaibin Zhang, Yijiang Li, Chen Zhang, Zhenfei Yin, Philip Torr,
Wanli Ouyang, and Lei Bai. CoMAS: Co-Evolving Multi-Agent Systems via Interaction Rewards. InInternational
Conference on Learning Representations, pages 32373–32394, 2026. URLhttps://proceedings.iclr.cc/paper_
files/paper/2026/hash/372593bd318ad8b34b3a8da77e20272b-Abstract-Conference.html.
[26] Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon, Sercan Ö. Arık, Dong Wang, Hamed Zamani, and Jiawei
Han. Search-R1: Training LLMs to reason and leverage search engines with reinforcement learning. InSecond
Conference on Language Modeling, 2025. URLhttps://openreview.net/forum?id=Rwhi91ideu.
[27] Weihua Du, Hailei Gong, Zhan Ling, Kang Liu, Lingfeng Shen, Xuesong Yao, Yufei Xu, Dingyuan Shi, Yiming
Yang, and Jiecao Chen. Generalizable End-to-End Tool-Use RL with Synthetic CodeGym. InInternational
Conference on Learning Representations, pages 17733–17756, 2026. URLhttps://proceedings.iclr.cc/paper_
files/paper/2026/hash/1e4322fddd833f83c855660ac65e428d-Abstract-Conference.html.
[28] Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Jiadai Sun, Xinyue Yang, Yu Yang,
Shuntian Yao, Wei Xu, Jie Tang, and Yuxiao Dong. WebRL: Training LLM web agents via self-
evolving online curriculum reinforcement learning. InInternational Conference on Learning Represen-
tations, pages 79791–79821, 2025. URL https://proceedings.iclr.cc/paper_files/paper/2025/hash/
c66e1fcc9691aae706250638f36f681b-Abstract-Conference.html.
[29] Jiazhan Feng, Shijue Huang, Xingwei Qu, Ge Zhang, Yujia Qin, Baoquan Zhong, Chengquan Jiang, Jinxin
Chi, and Wanjun Zhong. ReTool: Reinforcement Learning for Strategic Tool Use in LLMs. InInternational
Conference on Learning Representations, pages 37909–37926, 2026. URLhttps://proceedings.iclr.cc/paper_
files/paper/2026/hash/4038c9208dfc22644c60ad39c24e5c53-Abstract-Conference.html.
14

[30] Zhuofeng Li, Haoxiang Zhang, Seungju Han, Sheng Liu, Jianwen Xie, Yu Zhang, Yejin Choi, James Y Zou,
and Pan Lu. In-the-Flow Agentic System Optimization for Effective Planning and Tool Use. InInternational
Conference on Learning Representations, pages 50524–50570, 2026. URLhttps://proceedings.iclr.cc/paper_
files/paper/2026/hash/52c4a736cd63b3c7bf52011a1f66f3f6-Abstract-Conference.html.
[31] Kaiyan Zhang, Kai Tian, Runze Liu, Sihang Zeng, Xuekai Zhu, Guoli Jia, Yuchen Fan, Xingtai Lv,
Yuxin Zuo, Che Jiang, Yuru Wang, Jianyu Wang, Ermo Hua, Xinwei Long, Junqi Gao, Youbang Sun,
Zhiyuan Ma, Ganqu Cui, Ning Ding, Biqing Qi, and Bowen Zhou. MARTI: A Framework for Multi-
Agent LLM Systems Reinforced Training and Inference. InInternational Conference on Learning Repre-
sentations, pages 138790–138813, 2026. URLhttps://proceedings.iclr.cc/paper_files/paper/2026/hash/
e045c55a71fb4fc04d9a20579415247d-Abstract-Conference.html.
[32] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini
Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens,
Amanda Askell, Peter Welinder, Paul F. Christiano, Jan Leike, and Ryan Lowe. Training language models to
follow instructions with human feedback. InAdvances in Neural Information Processing Systems, volume 35, pages
27730–27744. Curran Associates, Inc., 2022. doi: 10.52202/068431-2011. URLhttps://proceedings.neurips.
cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html.
[33] Aohan Zeng, Mingdao Liu, Rui Lu, Bowen Wang, Xiao Liu, Yuxiao Dong, and Jie Tang. AgentTuning: Enabling
generalized agent abilities for LLMs. InFindings of the Association for Computational Linguistics: ACL 2024,
pages 3053–3077. Association for Computational Linguistics, 2024. doi: 10.18653/v1/2024.findings-acl.181. URL
https://aclanthology.org/2024.findings-acl.181/.
[34] Arash Ahmadian, Chris Cremer, Matthias Gallé, Marzieh Fadaee, Julia Kreutzer, Olivier Pietquin, Ahmet Üstün,
and Sara Hooker. Back to basics: Revisiting REINFORCE-style optimization for learning from human feedback in
LLMs. InProceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), pages 12248–12267. Association for Computational Linguistics, 2024. doi: 10.18653/v1/2024.acl-long.662.
URLhttps://aclanthology.org/2024.acl-long.662/.
[35] Chujie Zheng et al. Group sequence policy optimization. arXiv preprint, 2025. URLhttps://arxiv.org/abs/
2507.18071.
[36] Zhenyu Hou et al. Single-rollout asynchronous optimization for agentic reinforcement learning. arXiv preprint,
2026. URLhttps://arxiv.org/abs/2607.07508.
[37] John Schulman, Philipp Moritz, Sergey Levine, Michael I. Jordan, and Pieter Abbeel. High-dimensional continuous
control using generalized advantage estimation. InInternational Conference on Learning Representations, 2016.
URLhttps://arxiv.org/abs/1506.02438.
[38] DeepSeek-AI. DeepSeek-V4: Towards highly efficient million-token context intelligence. Technical report, 2026.
URLhttps://arxiv.org/abs/2606.19348.
[39] Kimi Team. Kimi K3: Open frontier intelligence. arXiv preprint, 2026. URLhttps://arxiv.org/abs/2607.24653.
[40] Z.AI. GLM-5.2: Built for long-horizon tasks, June 2026. URL https://huggingface.co/blog/zai-org/
glm-52-blog.
[41] Qwen Team. Qwen3.5: Towards native multimodal agents, February 2026. URLhttps://qwen.ai/blog?id=
qwen3.5.
[42] An Yang, Anfeng Li, Baosong Yang, et al. Qwen3 technical report. arXiv preprint, 2025. URL https:
//arxiv.org/abs/2505.09388.
[43] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and
Weizhu Chen. LoRA: Low-rank adaptation of large language models. InInternational Conference on Learning
Representations, 2022. URLhttps://openreview.net/forum?id=nZeVKeeFYf9.
15

A Role Reward Computation
We detail aggregation scopes and parameters for offline and co-evolution rewards (Section 4.2).
A.1 Rewards for Planner and Optimizer
Equations (6)–(7) combine separate returns for the current account and all controlled accounts. Planner uses
results from observation end to period end; Optimizer uses current-step increments. Each term aggregates
ADV, spend, and conversionsF, C, Nin its scope to compute the scaled proxy return.
The CPA target averages initial tCPA across all units, weighted by conversions. For settlement windowW,
letd u be unitu’s initial tCPA andNu,W its conversions. The target cost allowanceMW = P u duNu,W and
total conversionsN W = P u Nu,W giveρ=M W /NW; whenN W = 0, we setρ= 0.
Both Sparse and General use this computation. Training setsη = 1, s = 10000, and ω = 0.2to control the
cost-deviation weight, reward scaling, and overall reward weight, respectively. Planner’s reward settles at
period end; Optimizer’s current-step reward is used in the advantage recursion in Appendix C.1.
A.2 Period-Level Feedback for Inspector
Period feedback aggregates value generation, conversions, cost control, and adjustment execution across all
controlled accounts. LetFe, Ce, Ne denote aggregate ADV, spend, and conversions in periode. The feedback
vector and fixed weights in Eq. (7) are
ye =
 eFe, eNe, mCPA e ,−r forced e ⊤ ,
w= [1.0,0.2,0.5,0.1] ⊤. (A.1)
To obtain eFe and eNe, we subtract training-set meansµF , µN from ADV and conversions, divide by the
corresponding standard deviationsσF , σN plus a numerical stabilizerϵ >0, and clip to[−3, 3]. The means
and standard deviations remain frozen during training.
The CPA constraint margin compares actual spending with the target cost allowanceMe = P u duNe,u, where
uranges over all controlled units andNe,u counts unitu’s conversions in periode:
mCPA e = clip
 Me −C e
max(Me, ϵ),−3,3

.(A.2)
This component is positive below the target cost allowance and negative above it.
The forced-HOLD rate reflects adjustment requests made after the adjustment limit has been reached. LetHe
count SET requests converted to HOLD because the limit has been reached, andSe count all SET requests:
rforced e = clip
 He
max(Se,1) ,0,3

.(A.3)
This component enters the feedback vector negatively. Once periode’s feedback is settled, the system computes
the previous diagnosis’s reward as the weighted change between adjacent periods,rI e−1 =w ⊤(ye −y e−1).
B Offline Optimization Details and Algorithm
B.1 Candidate Advantages and Sequence-Level Optimization
At the same decision snapshot, the system fixes the policies of the other roles, samples candidate responses
for the target role using behavior policyπr b, and computes returns according to the reward definitions in
Appendix A. Optimizer’s candidate return is the undiscounted sum of stepwise rewards for the same account
16

from the step when the candidate action takes effect through the end of the period; each stepwise reward
retains both the account-level and global feedback terms.
Planner and Optimizer construct leave-one-out advantages using Eq.(8), normalizing with an exponential
moving average of within-group return standard deviations; candidate groups with overly small return variance
receive zero advantages. Inspector uses each candidate branch’s return minus that of the branch without a
diagnosis. Both share the previous period’s feedback, so their difference depends only on next-period outcomes.
These advantages stay fixed throughout offline optimization.
Policy optimization uses the sequence-level objective in Eq.(9). For candidateg, let Lg denote the response
length, and letpgℓ(θ)and pb gℓ denote the conditional probabilities of tokenℓ under the current and behavior
policies, respectively. The length-normalized sequence importance ratio is
ϱg(θ) = exp

 1
Lg
LgX
ℓ=1
log pgℓ(θ) pb gℓ

 .(B.1)
The KL penalty uses reference policyπref, with token probabilitypref gℓ . Define ξgℓ = log[pref gℓ /pgℓ(θ)]. The k3
estimate averages exp(ξgℓ) −ξ gℓ − 1over valid response tokens. Behavior and reference policies stay fixed
throughout offline optimization. Appendix D.2 gives the clipping range and KL coefficient.
B.2 Offline Reinforcement Learning Algorithm
In Algorithm B.1,Sr denotes the set of decision snapshots for roler∈ R= {P, O, I}, andΓ r maps responses
to executable actions or diagnostic guidance.Bvalid r stores the inputs, responses, returns, fixed advantages,
and behavior policy probabilities and versions of valid candidates, andBdenotes a training batch.
Algorithm B.1:Offline Reinforcement Learning
Input:SFT parameters{θ SFT r }, decision snapshots{Sr}, delivery environmentE.
Output:Offline parameters{θ off r }.
1θ r ←θ SFT r ; fixπ r b ←π θr;D off r ←∅,∀r;
2forr∈ R, σ∈ Sr do
3Readh r fromσ;{z r g }G g=1 ∼π r b (· |hr);
4u r g ←Γ r(zr g , hr); execute candidates separately fromσ; compute{Jr g }G g=1 as specified in Appendix B.1;
5ifr=Ithen
6Run the branch without a diagnosis; computeJ 0 using Eq. (7);
7end
8Compute and fix{ bAr g}using Eq. (8) and its normalization rules;
9D off r ← Doff r ∪ Bvalid r ;
10end
11forr∈ Rdo
12Fixπ r ref;
13forB ⊂ D off r do
14Computeϱ r g andL r off using Eqs. (B.1) and (9), and updateθr;
15end
16θ off r ←θ r;
17end
18return{θ off r }r∈R;
C Co-Evolution Update Details and Algorithm
Co-evolution uses settled feedback from actual execution trajectories. Trajectoryτe records inputs, responses,
behavior policy versions, generation probabilities, and feedback. Settled records formDe at period end, with
role r’s records inDr e. The new diagnosis awaits next-period settlement; scheduleke cycles through( P, O, I).
Each role adds newly settled records to its bufferCr and, when scheduled, selects valid records to form the
current round’s training setBr e. Used records are removed from the buffer and excluded from later rounds;
the remaining records are retained. Updated role policies take effect in the next period.
17

C.1 Value Baselines and Advantage Estimation
Each role’s independent PrefixValueModelVϕr (h)maps the last input token’sD-dimensional hidden represen-
tation before response generation through LayerNorm(D), Linear(D, 256), Tanh, and Linear(256, 1) to a
scalar return. Detached input features block value-model gradients to the role language model.
Before each training round, the system computes value predictionsV − i , then advantages and return targets.
Planner and Inspector userr i −V − i as the advantage in Eq.(10), with regression targetsbRr i = rr i. Optimizer
applies GAE within each account and period, including HOLD decisions.
Fixing one period, letta,i denote the i-th decision step of accounta, rO a,i its reward,∆ a,i = ta,i+1 −t a,i the
number of environment steps to the next node of the same account, andba,i ∈ {0, 1} the sequence termination
indicator. The recursion is
δa,i =r O a,i +γ ∆a,i (1−b a,i)V − a,i+1 −V − a,i,
bAO a,i =δ a,i +γ ∆a,i λ(1−b a,i) bAO a,i+1,
bRO a,i = bAO a,i +V − a,i.
(C.1)
The discount factor isγ = 1and the GAE parameter isλ = 0.95. Each account’s final node in a period has
ba,i = 1and∆ a,i = 0, with zero terminal bootstrap value and boundary advantage. Recursion never crosses
accounts or periods, even though rewards include all-account feedback. Advantages and return targets are
computed over complete account-period sequences before batching and remain fixed throughout the round.
C.2 Value Regression and Policy Updates
The value model performs SmoothL1 regression against fixed, detached return targetsbRi, averaging the
per-node regression losses over the settled batchB. Each role’s first scheduled round updates only its value
model. Later rounds update the value model first, then the role policy using the previously fixed action
advantages. The two models maintain separate optimizers and optimizer states.
Policy updates follow Eq.(11), with an entire response sharing the same action advantage. Letpℓ(θ)and pb ℓ
denote the conditional probabilities of tokenℓ under the current policy and the behavior policy that collected
the response. Their ratio isϱℓ =p ℓ(θ)/pb ℓ. The selection mask and importance weight are
mℓ =1

1−ε − ≤ϱ ℓ ≤1 +ε + ,
¯ϱℓ = sg

clip(ϱℓ,1−ε −,1 +ε +)  . (C.2)
Here,ε − =ε + = 0.2,sgstops the gradient, andZ= PL ℓ=1 mℓ is the number of valid tokens.
Each actor update recomputes probability ratios and masks; advantages and importance weights stay fixed
during backpropagation. Responses withZ = 0are skipped for that update. Thek3KL to the behavior policy
is used only for monitoring and rollback, not in the actor objective. If KL exceeds 0.01 or the retained-token
fraction falls below 0.4, the system restores the parameters and optimizer state from before that update and
stops actor updates for the round. Completed value-model updates are retained.
C.3 Continuous Co-Evolution Algorithm
In Algorithm C.1, letΘr e denote role r’s policy parameters, value parameters, and optimizer states,νr its
number of completed training rounds, andeΘr its state at the end of the current round.
18

Algorithm C.1:Continuous Co-Evolution
Input:Offline parameters{θ off r }, delivery environmentE, role schedule{ke}E e=1.
Output:Final training states{Θ r E+1}.
1Initialize{Θ r 1}using{θ off r };ν r ←0,C r ←∅,∀r;g 0 ←∅;
2fore= 1, . . . , Edo
3 Execute and record P/O delivery withge−1 in τe; compute P/O rewards using Eqs.(6)–(7) and construct
ye;
4z I e ∼π θI (· |hI e);g e ←Γ I (zI e , hI e);
5Append the current diagnosis toτ e as pending;
6InitializeD e with settled P/O records; if a previous diagnosis is pending, settle its reward using Eq. (7)
and add its record;
7C r′ ← Cr′ ∪ Dr′ e ,∀r ′ ∈ R;
8r←k e; formB r e from valid records inCr;
9Compute and fixV − i , bAr i , bRr i forB r e using Eq. (10) and Appendix C.1;
10DivideB r e into batches; updateϕr by value regression in Appendix C.2;
11ifν r >0then
12Updateθ r batch by batch using Eq. (11) with filtering and rollback in Appendix C.2;
13end
14C r ← Cr \ Br e;
15ν r ←ν r + 1;Θ r e+1 ← eΘr;Θ r′ e+1 ←Θ r′ e , r′ ̸=r;
16end
17return{Θ r E+1}r∈R;
D Experimental Implementation Settings
D.1 Environment Configuration
Delivery periods use 48 time steps and a traffic generation setting of 500,000 opportunities, following
AuctionNet’s official defaults [14]. General is calibrated from the General dataset in AuctionNet’s open-source
repository: the generation baseline for predicted conversion probabilities (pValue) is 0.005, and budgets and
CPA constraints use the full 48-dimensional configurations. Other auction mechanisms remain unchanged.
For each environment configuration, the total traffic volume, initial budgets and CPA constraints, competitor-
type composition, and pValue generation baseline remain fixed across periods. Each period uses the episode
index to resample predicted conversion probabilities and their variability and within-period traffic curves,
and to initialize native competitors’ random states, producing different market conditions. Both Sparse and
General split episodes 71–320 consecutively into five market sequences, each with 50 delivery periods.
D.2 Training Configuration
For SFT, each role uses 3,290 demonstration trajectories generated by DeepSeek V4 Flash. Training uses a
learning rate of10−4, microbatch size 8, gradient accumulation of 2, and maximum total sequence length of
2,560 tokens. Planner, Optimizer, and Inspector are trained for 4, 3, and 3 epochs, respectively.
Offline GSPO uses a learning rate of10−5 for 5 epochs, 4 candidates per decision, sequence-ratio clipping to
[0.8,1.2], and a KL penalty coefficient of 0.1. Both stages use LoRA with rank 16 and alpha 32.
Co-evolution uses AdamW at actor and value-model learning rates of10−6 and5 × 10−4, respectively. Batches
hold valid settled decision nodes for the scheduled role. Rounds with valid nodes update the value model once
and the actor at most four times; Appendix C.2 covers the first scheduled round and rollback.
D.3 Inference and Action Handling
During continuous delivery, responses are sampled at a temperature of 0.7 with thinking disabled. The context
and response limits are 8,192 and 512 tokens, respectively. Top-p is not explicitly specified. Optimizer selects
HOLD or a tCPA multiplier of 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, or 1.3.
19

Foundation models and AdCoEvo use the same role workflow, prompts, output format, and action-parsing
rules. We specify the required output format in prompts for foundation models, without enforcing constrained
JSON generation. If Planner parsing or format validation fails, the remaining budget is allocated in proportion
to the ad units’ initial budgets. For Optimizer, parsing failure or an incorrect decision count produces four
HOLDs; each invalid multiplier is replaced by HOLD. During evaluation, each invalid response is counted
once, regardless of how many errors it contains. Format errors do not trigger resampling.
D.4 Baseline and Ablation Configurations
AdPilot* combines reflection and action generation in a single model call. Its SFT demonstrations are
generated by DeepSeek V4 Flash, and its SFT and GRPO training use the same training markets as AdCoEvo.
Rule multiplies an ad unit’s budget by 1.1 when its CPA does not exceed the target, and by 0.9 otherwise,
then normalizes budgets within the account to preserve its total budget. For tCPA, it uses 0.7 if CPA exceeds
1.10 times the target, 1.3 if CPA is below 0.90 times the target, and HOLD otherwise. No conversions or an
exhausted adjustment limit yield HOLD. The rules do not use within-period timing or spending progress to
determine when to adjust.
Role-composition ablations omit the excluded roles at inference. Without Optimizer, the execution layer
applies HOLD throughout delivery and keeps control tCPA at its initial value; without Planner, each ad unit
retains its initial budget limit. Without Inspector, the remaining Planner and Optimizer roles receive the
current-period delivery state but no cross-period diagnostic guidance or fixed statistical summaries.
20
