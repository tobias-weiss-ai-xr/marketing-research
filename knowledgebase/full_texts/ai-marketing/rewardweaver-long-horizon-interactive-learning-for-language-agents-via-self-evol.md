---
title: 'RewardWeaver: Long-Horizon Interactive Learning for Language Agents via Self-Evolving Reward Adaptation'
url: https://arxiv.org/abs/2610.10120
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Hengbo Xiao
- Boyao Zhang
- Purui Liu
- Yuxuan Zheng
- Haoran Yin
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.10120
pages: 23
chars: 78168
fetched_at: '2026-11-08T13:31:34+00:00'
kb_version: 1
---

# RewardWeaver: Long-Horizon Interactive Learning for Language Agents via Self-Evolving Reward Adaptation

REWARDWEAVER: LONG-HORIZONINTERACTIVELEARNING
FORLANGUAGEAGENTS
VIASELF-EVOLVINGREWARDADAPTATION
A PREPRINT
Hengbo Xiao∗♠
Yoolee.ai
Boyao Zhang∗
University of Science and Technology of China
Purui Liu∗
Peking University
Yuxuan Zheng
Peking University
Haoran Yin
Tianjin University
Haibo Liu
Yoolee.ai
Fan Zhang†
Yoolee.ai
fan.zhang@yoolee.ai
ABSTRACT
Reinforcement learning with verifiable rewards (RLVR) has driven substantial progress in domains
where task outcomes can be reliably evaluated, but long-horizon interaction remains challenging
due to sparse terminal feedback and difficult credit assignment. Process rewards provide denser
supervision, yet the capabilities most relevant for training can change as the policy evolves: a be-
havior that is easy to evaluate or frequently deficient need not be the bottleneck currently limiting
task success. We introduceRewardWeaver, a self-evolving reward adaptation framework for lan-
guage agents in long-horizon interaction. RewardWeaver maintains a validated capability space in
which the semantics of admitted Rubrics remain fixed, and closes the loop between policy opti-
mization, task evaluation, failure attribution, and reward adaptation. After each training stage, it
performs outcome-grounded backward attribution on low-outcome trajectories, aggregates recurrent
and policy-controlled capability bottlenecks, and dynamically selects the corresponding process re-
wards for the next stage. Recurrent failures not covered by the existing capability space trigger a
separate, controlled expansion procedure. We evaluate REWARDWEAVERon SOTOPIA, Amazon-
HistoryPrice, and a newly constructed Sales Benchmark. Across social interaction, bilateral bargain-
ing, and domain-specific sales, REWARDWEAVERestablishes new state-of-the-art (SOTA) results.
Ablations further demonstrate the importance of dynamic reward allocation, failure-grounded attri-
bution, and stable semantics for admitted capabilities.
1 Introduction
Reinforcement learning with verifiable rewards (RLVR) has enabled substantial progress in mathematics and code,
where task outcomes can be reliably checked by rules, tests, or execution (Shao et al., 2024; Le et al., 2022; Guo et al.,
2025). Long-horizon interaction, however, poses a fundamentally different optimization problem. In settings such as
negotiation, social coordination, and collaborative decision making (Zhou et al., 2024a; Wang et al., 2026; Liu et al.,
2025), each action changes the partner’s subsequent behavior and reshapes the interaction trajectory. Final outcomes
emerge from sequences of interdependent decisions across many turns, making rewards sparse, delayed, and difficult
to assign to specific behaviors (Arjona-Medina et al., 2019; Hung et al., 2019; Meulemans et al., 2023). A terminal
score indicates whether an interaction succeeded, but certifies failure without localizing its cause and cannot by itself
direct training.
Rubric-based rewards and evaluators provide denser supervision by assessing intermediate behaviors against explicit,
fine-grained criteria (Gunjal et al., 2026; Wei et al., 2026; Hashemi et al., 2024; Lee et al., 2025), and rubric con-
∗Equal contribution.♠Project leader.†Corresponding author.
arXiv:2610.10120v1  [cs.AI]  7 Oct 2026

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
FIXED TASK RUBRICS
Taskt
Human Expert
External LLM
Fixed Rubrics
Reward Policy Model
(a) Static Rubric Rewards
EVOLVING TASK RUBRICS
Taskt
Policy Modelπ k Current Policy Responses
External
Rubric LLM
FIXED
Candidate
Rubrics Filter
Task Rubric Buffer
B k→B k+1
Reward
Task-Specific Priors
Expert · Answer · Web
(b) External-LLM Rubric Adaptation
CO-EVOLVING TASK RUBRICS
Taskt
Shared Policy Modelπ θ
SHAREDθ· TRAINABLE
Reasoner
Role
Current Policy
Responses
Rubric Generator
Role
Verify & Filter
Evolving Task
Rubrics
B k→B k+1
Initial Task Rubrics
BEFORE RL
Reward
(c) Joint Policy-Rubric Co-Evolution
OUTCOME-GUIDED TRAINING PRIORITIES
Diverse Tasks
?
Policy Model
Low-Outcome Trajectories
⋯ ⋯
⋯ ⋯
⋯ ⋯
Failure Attribution
Large-Scale Interaction Data
Capability
Induction
Reusable Capability Rubric Pool
Open-ended · Reference-free · Multi-task
Clarity
Rubric
Conciseness
Rubric
Empathy
Rubric
Response
Relevance
Rubric
Constraint
Awareness
Rubric
Planning
Rubric
TRAINING PRIORITIES
Response
Relevance RUBRIC
Constraint
Awareness RUBRIC
Planning
RUBRIC
Adaptive
Reward
(d) RewardWeaver
Figure 1:Reward Adaptation under Policy Evolution. (a)Task-specific Rubrics remain fixed throughout training.
(b)External-LLM methods revise Rubrics as policy evolves.(c)Co-evolution methods jointly update Rubrics and
the policy.(d)RewardWeaver grounds reward adaptation in recurrent task failures and prioritizes capability Rubrics
according to current policy bottlenecks.
struction now scales from instance-specific generation to reusable repositories (He et al., 2025; Li et al., 2026). Recent
approaches further revise or evolve these criteria as the policy changes, tracking its current response distribution (Guan
et al., 2026). However, tracking the response distribution is not tracking the failure distribution: a behavior may be fre-
quent or easy to discriminate without being a recurrent cause of task failure, while a less frequent capability deficiency
may constitute the actual performance bottleneck. The key question is not only how evaluation criteria should adapt,
but what evidence should drive that adaptation. We argue that this evidence should be recurrent failures in low-outcome
trajectories, rather than response characteristics alone. Figure 1 contrasts these reward-adaptation paradigms.
The central challenge is not merely how to design better process rewards, but how to decide what the current policy
should optimize next. This introduces an outer-loop optimization problem complementary to standard RL: the inner-
loop optimizer determines how to improve the policy under a given reward, while the outer loop must determine which
capabilities deserve training credit. Diagnostic evidence must therefore satisfy three conditions: it must be outcome-
grounded, drawn from trajectories that failed rather than sampled uniformly; recurrent, reappearing across trajectories
rather than reflecting incidental variation; and policy-controlled, attributable to the agent’s own behavior (Zhang et al.,
2025a) rather than to the partner or the scenario. Isolated low scores satisfy none of these conditions. In this view, the
task-level objective should remain stable, while process-level training credit shifts toward the capabilities that currently
constrain performance.
We introduceRewardWeaver, a self-evolving reward adaptation framework for language agents in long-horizon
interaction. REWARDWEAVERcloses the loop between policy training, automatic evaluation, failure attribution, and
reward adaptation. At each stage, it identifies recurrent capability bottlenecks from on-policy interaction failures and
dynamically selects the corresponding Rubrics to construct the next process reward. Unlike prior self-evolving rubric
methods that evolvewhat is evaluated, REWARDWEAVERevolveswhat is optimized: it preserves stable semantics for
admitted capabilities while dynamically reallocating training credit across them. Recurrent failures that fall outside
the existing Rubric space are incorporated only through controlled validation, allowing the reward to evolve without
uncontrolled semantic drift.
We evaluate REWARDWEAVERon SOTOPIA (Zhou et al., 2024a) and related social intelligence benchmarks against
outcome-only reinforcement learning, static capability prioritization, and alternative attribution and rubric-design
strategies. REWARDWEAVERimproves the primary evaluation metrics and achieves new state-of-the-art (SOTA)
performance under matched training and evaluation protocols. Further ablation, sensitivity, and qualitative analyses
show that failure-grounded attribution, adaptive credit reallocation, and stable semantics for admitted capabilities are
2

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
A
B
C
1 Policy Optimization
Optimize policy using the current reward.
(πk,R k)→π k+1
πk
Rk
2 Task Interaction & Outcome
Execute tasks; collect outcomes and failures.
πk+1 →T k+1 →F k+1
Tk+1
Ro(τi)
!
Fk+1
3 Failure Attribution
Evidence→Retrieve→Evaluate→Aggregate
Fk+1 →G k+1
!
d1
d2
d3
Gk+1
4 Adaptive Reward Update
Prioritize→Select→Compile
(Gk+1,D k+1)→A k+1 →R k+1
Next stage:k←k+ 1
Illustrative
Example
Partner: “This is over
my budget.”
Policy: “Let me list
all the features.”
Low outcome
Policy: “Let me list
all the features.”
Evidence: ignores
the stated concern
Response
Relevance Clarity Conciseness
Recurrent
across
failures
Response
Relevance
Activate dimension Activate Rubric
Rubric LibraryD k
Human-
Likeness Empathy Information Clarity •••
Capability Dimensions
Rubric-Specific Evaluators{J d}
Rubricd ?
Initial Judge Prompt
Prompt Iteration
Test · Refine
Reliable
EvaluatorJ d
rubric definitions
attribution verdicts
Rubric ExpansionfromG k+1
!
Uncovered Define Deduplicate Validate
0
Dk+1
Library update(k→k+1)
Figure 2:The Overall Architecture of REWARDWEAVER. (a)The policy is optimized under the current reward;
its on-policy low-outcome trajectories reveal recurrent capability bottlenecks that determine the next-stage allocation
of training credit.(b)Failure attribution grounds bottleneck identification in concrete behavioral evidence.(c)A val-
idated capability space provides stable semantics for admitted capabilities, while recurrent uncovered failures trigger
controlled expansion.
key contributors to the gains. Our contributions are summarized as follows: (1) We formulate reward adaptation in
long-horizon interaction as an outer-loop optimization problem that determines which process capabilities should be
prioritized next. (2) We propose REWARDWEAVER, which dynamically reallocates training credit through failure-
driven capability-bottleneck identification while preserving stable task objectives and evaluation semantics. (3) We
conduct systematic experiments demonstrating the advantages of self-evolving reward adaptation over outcome-only
and static process-reward baselines, and isolate the contributions of REWARDWEAVER’s key components.
2 RewardWeaver Methodology
REWARDWEAVERseparatesreward semanticsfromreward relevance: a validated capability space determineswhat
can be rewarded, while a stage-wise outer loop determineswhat should be rewarded. Training priorities can evolve
with the policy without the semantics of admitted capabilities drifting, while the capability library itself expands only
through a separate validated procedure.
2.1 Task Formulation
At stagek, policyπ k interacts with partnerπ partner: given interaction historyh t, the two parties act alternately with
at ∼π k(· |ht)andb t ∼π partner(· |ht, at). A completed trajectoryτreceives a fixed task-level outcomeR o(τ)and
a stage-dependent process reward,
Rk(τ) =R o(τ) + 1 |Ak| X d∈Ak ¯Jd(τ),(1)
whereD k is the capability space available at stagek,A k ⊆ Dk the active subset, and ¯Jd(τ)the trajectory-level score
of capability evaluatorJ d; all active Rubrics enter with equal weight, so adaptation determineswhichcapabilities
receive credit rather than how much each receives. The terminal objective remains fixed; only process-level credit
changes: standard RL determineshowto optimize underR k, i.e.,(π k, Rk)→π k+1, whereas REWARDWEAVER
3

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
Algorithm 1 Validated Capability-Space Construction
Require:Raw interaction corpusT raw, induction modelsM, validity criteriaV, evaluator configurationκ, repeat countR, con-
struction budgetB
Ensure:Validated capability spaceD={(d, J d)}
Stage I: Capability Discovery and Consolidation
1:T ←NORMALIZEANDFILTER(T raw)
2:F ←OPENINDUCTIONWITHEVIDENCE(T,M)
3:forr= 1, . . . , Rdo
4:S r ←CONSOLIDATE(EMBEDDINGNEIGHBORS(F))
5:S r ←FILTER(S r;generality,operationality,distinctiveness)
6:end for
7:S ←ALIGNANDSELECT({S r}R r=1;recurrence,coverage,support)
8:S ←DEFINECANDIDATES(S,F)
Stage II: Operationalization and Admission
9:D ←∅
10:whileS ̸=∅and budgetBremainsdo
11: remove candidatedfromS
12:X d ←RETRIEVERELEVANTCASES(T, d)
13:L d ←ANNOTATEANDVERIFY(X d, d)
14:(L dev d ,L acc d )←SOURCEDISJOINTSPLIT(L d)
15:(L dev d ,L acc d )←ENSURECOVERAGE(L dev d ,L acc d , d)
16:p ⋆ d ←DEVELOPEVALUATOR(d,L dev d , κ)
17:J d ←FREEZEEVALUATOR(p ⋆ d, d, κ)
18:v d ←VALIDATECANDIDATE(d, J d,L acc d ,D;V)
19:ifv d =ACCEPTthen
20:D ← D ∪ {(FREEZEDEFINITION(d), J d)}
21:else ifv d =REVISEthen
22:d ′ ←REVISECANDIDATE(d, v d)
23:S ← S ∪ {d ′}
24:else
25: discardd
26:end if
27:end while
28:returnD
determineswhich capabilities should receive training credit next. Throughout,capabilitydenotes the behavioral
concept,Rubricits frozen operational definition, andevaluatorthe scoring functionJ d; theactive setis the subset
of capabilities currently receiving process-level training credit, and areward specificationcouples the active set with
how its evaluators are composed.
2.2 Validated Capability Space
Reward adaptation requires stable semantics for admitted capabilities. REWARDWEAVERoperates over a validated
spaceDof observable, policy-controllable behaviors, where eachd∈ Dcouples a frozen Rubric definition with an
evaluatorJ d(x) =M eval(pd, x), andpd operationalizes the definition over interaction contextx. Construction has
two stages: candidates are first induced from interaction evidence, consolidated across runs, and filtered for generality,
operationality, and semantic distinctiveness; each is then operationalized by a dedicated evaluator and subjected to
source-disjoint acceptance testing (Algorithm 1). Candidates may be revised before admission; only validated pairs are
admitted intoD, so discovery remains flexible while admitted semantics remain fixed. Admission testing certifies each
evaluator on its own source-disjoint acceptance set, so every admitted capability satisfies the same validity criteria. The
SOTOPIA capability space, representative entries, and their operationalization into executable criteria are provided in
Appendix A.
2.3 Outcome-Grounded Failure Attribution
Terminal outcomes identify low-outcome trajectories that warrant diagnosis, but do not by themselves establish an
agent-side failure or determine what should receive training credit. After stagek,π k+1 generates on-policy trajectories
Tk+1, from which the low-outcome cohortF k+1 ={τ i ∈ Tk+1 |q o(Ro(τi), xi) = 1}is selected, wherex i denotes
the task instance of trajectoryτ i. For eachτ i ∈ Fk+1, REWARDWEAVERlocalizes failure-relevant evidence, retrieves
candidate capabilitiesC i ⊆ Dk, and produces attribution recordsa i,d = (s i,d, ci,d, ei,d)ford∈C i, wheres i,d
4

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
Algorithm 2 Failure Attribution and Adaptive Credit Allocation
Require:On-policy trajectoriesT k+1, capability spaceD k, current reward specificationP k, adaptation historyS k, task-
performance summaryy k+1, calibration setH k+1, parametersΘwith active budgetKand calibration limitM
Ensure:Next-stage reward specificationP k+1, or calibration failure⊥
1:F k+1 ←LOWOUTCOMES(T k+1);Z k+1 ←∅
2:forτ∈ F k+1 do
3:e τ ←LOCALIZEEVIDENCE(τ)
4:C τ ←RETRIEVE(e τ ,D k)
5:Z τ ←ATTRIBUTE(e τ , Cτ )▷Abstention allowed
6:Z k+1 ← Zk+1 ∪ Zτ
7:end for
8:(G k+1,{r d, nd, cd, fd})←AGGREGATE(Z k+1)
9:p d ←αr d +βc d +γ(1−f d),d∈ D k
10:(B high,B weak)←ELIGIBLE(G k+1,S k; Θ)
11:A k+1 ←TOPK(B high, p, K)
12:if|A k+1|< KandALLOWWEAK(B high,S k; Θ)then
13:A k+1 ←A k+1 ∪TOPK(B weak \A k+1, p, K− |Ak+1|)
14:end if
15:(A k+1,S k+1)←SCHEDULE(A k+1, Gk+1,S k, yk+1; Θ)
16:λ k+1,d ←1/|A k+1|,d∈A k+1 ▷Equal weight over active Rubrics
17:Q k+1 ←COMPILERUBRICS(A k+1, Pk)▷Assemble a reward specification
18:form= 1, . . . , Mdo
19:(s, δ)←CALIBRATE(Q k+1,H k+1)
20:ifACCEPT(s)then▷Rubric-set publication gate
21:P k+1 ←COMPOSE(P k, Ak+1, λk+1, Qk+1, s, δ,Sk+1)
22: PUBLISH(P k+1)
23:returnP k+1
24:else ifm < Mthen
25:Q k+1 ←REVISE(Q k+1, s, δ)▷Revise composition; keep(d, J d)frozen
26:end if
27:end for
28:return⊥▷Calibration failure; no new reward is published
is the deficit judgment,c i,d its confidence, ande i,d the supporting evidence; unsupported assignments are rejected.
Trajectory-level records are aggregated intoG k+1 = Aggregate({a i,d}), which retains recurrent, supported, and
policy-controlled failure modes rather than isolated low scores.
2.4 Adaptive Credit Allocation
A capability can be valid yet irrelevant to the current policy; REWARDWEAVERtreats training relevance as stage-
dependent. GivenG k+1, it selects a budgeted active setA k+1 = Select(G k+1,D k)⊆ D k. All active Rubrics
contribute equally to the process reward, yieldingR k+1(τ) =R o(τ) + 1 |Ak+1| P d∈Ak+1 ¯Jd(τ). As a bottleneck
recedes, its Rubric may leave the active set and capacity is released for newly dominant failures, so the process reward
is selective and stage-dependent rather than cumulative. LettingP k denote the deployed process-reward specification
at stagek,S k its adaptation history, andy k+1 the stage-level task-performance summary, Algorithm 2 specifies the
complete attribution-to-reward update. Importantly, the update changes which Rubrics are active and how they are
composed into the next-stage reward, but never modifies the frozen semantics or evaluators of the capabilities admitted
toD k.
2.5 Controlled Capability Expansion
Adaptive credit allocation operates only over the capability space already validated at the beginning of the update, so
the transition from stagektok+ 1always satisfiesA k+1 ⊆ Dk. When recurrent failures cannot be represented by
Dk, REWARDWEAVERinvokes the same admission procedure as Algorithm 1: validated additions form the expanded
spaceD k+1, but newly admitted capabilities do not alter the reward update that triggered their discovery—they become
eligible only in the subsequent adaptation step, i.e.,A k+2 ⊆ Dk+1. The fast loop therefore reallocates training credit
within fixed semantics,
(πk, Rk)→π k+1 → Tk+1 → Fk+1 →G k+1 →A k+1 ⊆ Dk →R k+1,(2)
5

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
while the slower semantic loop updates(F k+1,D k)→ Dk+1, with any new dimensions becoming available only to
later reward updates. This separation defines the methodological boundary of REWARDWEAVER:training priorities
evolve rapidly; reward semantics evolve conservatively.
Table 1:Main results on SOTOPIA.The best result in each setting is shown inbold. In the Partner setting, the
counterpart is GPT-4o for literature results and Qwen2.5-72B for AMPO and REWARDWEAVERin our experiments.
Self-Play Partner
Method SOTOPIA Goal / Overall↑ SOTOPIA-Hard Goal / Overall↑ SOTOPIA Goal / Overall↑ SOTOPIA-Hard Goal / Overall↑
Proprietary LLMs
GPT-4o 8.19 / 3.76 6.97 / 3.46 8.19 / 3.76 6.97 / 3.46
Claude-3.5-Sonnet 8.29 / 3.71 6.33 / 3.09 8.42 / 3.77 6.64 / 3.30
DeepSeek-V3 8.15 / 3.62 6.34 / 3.09 8.14 / 3.72 6.69 / 3.31
Large Reasoning Models
OpenAI-o1 7.93 / 3.58 5.69 / 2.71 8.09 / 3.69 6.65 / 3.20
OpenAI-o3-mini 7.38 / 3.30 5.14 / 2.36 7.96 / 3.61 6.33 / 2.98
Gemini-2.5-Pro 7.85 / 3.43 5.67 / 2.55 8.12 / 3.59 6.70 / 3.09
DeepSeek-R1 7.97 / 3.40 5.86 / 2.73 7.92 / 3.49 6.20 / 2.95
QwQ-32B 7.70 / 3.30 5.35 / 2.41 7.80 / 3.47 6.19 / 2.91
Post-training on Qwen2.5-7B-Instruct
Qwen2.5-7B-Instruct 7.91 / 3.55 6.21 / 3.01 6.71 / 3.13 5.90 / 2.90
w/ PPDPP (Deng et al., 2024) 7.97 / 3.65 6.63 / 3.31 8.07 / 3.71 6.76 / 3.35
w/ EPO (Liu et al., 2025) 8.09 / 3.51 6.82 / 3.12 8.41 / 3.86 6.81 / 3.51
w/ DAT (Li et al., 2024) 7.97 / 3.59 6.39 / 3.10 8.11 / 3.70 6.78 / 3.36
w/ DSI (Zhang et al., 2025b) 8.35 / 3.75 7.31 / 3.51 8.15 / 3.70 6.87 / 3.42
AMPO (Wang et al., 2026) 8.45 / 4.20 7.67 / 3.94 8.30 / 4.09 7.30 / 3.80
REWARDWEAVER(ours) 8.72 / 4.47 7.90 / 4.38 8.49 / 4.47 7.66 / 4.22
3 Experiments
3.1 Experimental Settings
Benchmarks.We evaluate REWARDWEAVERon three long-horizon benchmarks that together span general social in-
teraction, bilateral bargaining, and domain-specific sales. SOTOPIA (Zhou et al., 2024a) contains 90 social scenarios;
we report on the full benchmark and SOTOPIA-Hard. AmazonHistoryPrice (Xia et al., 2024) contains 930 products
across 18 categories and evaluates bargaining under asymmetric information, with Mutual Interest (MI) instances ad-
mitting feasible agreements and Conflicting Interest (CI) instances admitting none. Following SOTOPIA-π(Wang
et al., 2024b), we construct a health-service Sales Benchmark of 400 tasks across 20 scenario families; evaluation uses
held-out instances within training families (see Appendix B).
Evaluation.SOTOPIA and the Sales Benchmark use the SOTOPIA-EV AL protocol (Zhou et al., 2024a), reporting
Goal Completion and Overall under Self-Play and fixed-Partner settings; SOTOPIA-Hard is the challenging subset,
and Sales-Hard the 50 constraint-conflict tasks. For AmazonHistoryPrice, we report MI Deal Rate, CI Correct No-Deal
Rate, Task Success Rate, Normalized Seller Utility, and Expected MI Seller Return. Task Success counts a legal MI
agreement or correct CI no-deal; Expected MI Seller Return combines agreement probability with the resulting seller
utility. For SOTOPIA, REWARDWEAVERuses a validated 40-dimensional capability space (Appendix A), activates at
mostB= 6Rubrics per stage, and updates allocation every 30 steps.
3.2 Experimental Results and Analysis
RQ1: Does RewardWeaver improve long-horizon interactive learning?Across the three benchmarks, REWARD-
WEAVERimproves most primary metrics, with particularly strong gains in the harder SOTOPIA settings. On SO-
TOPIA (Table 1), it outperforms AMPO, the strongest prior method, on every metric under the same partner protocol,
most pronounced on SOTOPIA-Hard (Goal/Overall: 7.67/3.94 to 7.90/4.38 Self-Play, 7.30/3.80 to 7.66/4.22 Partner),
suggesting adaptive reward allocation remains effective under harder scenarios and external partners. On AmazonHis-
toryPrice (Figure 3), REWARDWEAVERjointly improves MI Deal Rate and seller-side utility, reaching the upper-right
6

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
performance frontier; complete numerical results are reported in Appendix Table C1. On the Sales Benchmark (Ta-
ble C2), it achieves the best result on six of eight metrics.
Figure 3:Main results on AmazonHistoryPrice.Under the DeepSeek-V4-Pro buyer, REWARDWEAVERreaches
the upper-right frontier, achieving a 95.2% MI Deal Rate and the highest Normalized Seller Utility (0.9737) among all
evaluated methods.
RQ2: Does dynamic reward adaptation matter, and does it need to target the correct bottlenecks?Table 2 com-
pares REWARDWEAVERwith outcome-only GRPO, Static Top-K, and Random Active Set. Outcome-only GRPO
is weaker overall, supporting the usefulness of process-level supervision in this setting, while Static Top-Kremains
below REWARDWEAVER, suggesting that a fixed capability set becomes insufficient as training proceeds. Random
Active Set preserves stage-wise reward changes but breaks the mapping from diagnosed bottlenecks to rewarded ca-
pabilities, providing a controlled test of bottleneck alignment; it underperforms REWARDWEAVERacross all eight
metrics. This comparison supports the importance of aligning reward allocation with the diagnosed bottlenecks, be-
yond the benefit of reward changes alone.
Table 2:Ablation study on SOTOPIA.The counterpart is Qwen2.5-72B. The best result in each column isbold.
We isolate the effects of dynamic reward adaptation, failure-grounded bottleneck identification, and stable semantics
for admitted capabilities under matched training budgets.
Self-Play Partner
Method SOTOPIA Goal / Overall↑ SOTOPIA-Hard Goal / Overall↑ SOTOPIA Goal / Overall↑ SOTOPIA-Hard Goal / Overall↑
REWARDWEAVER(ours) 8.72/ 4.47 7.90 /4.38 8.49 / 4.477.66 /4.22
Dynamic Reward Adaptation
Outcome-only GRPO 8.43 / 4.31 7.53 / 4.05 8.35 / 4.26 7.71 / 4.12
Static Top-KDimensions 8.44 / 4.31 7.77 / 4.14 8.36 / 4.23 7.49 / 3.83
Random Active Set 8.47 / 4.41 7.56 / 4.18 8.33 / 4.27 7.31 / 3.97
Failure-Grounded Bottleneck Identification
Dynamic Top-Kby Failure Frequency 8.21 / 4.23 7.36 / 4.03 8.11 / 3.40 7.13 / 3.25
Random-Trajectory Attribution 8.38 / 4.37 7.67 / 4.25 8.24 / 4.31 7.60 / 4.17
Success–Failure Trajectory Attribution 8.55 /4.52 7.93/ 4.32 8.34 / 4.33 7.60 / 4.14
Stable Semantics for Admitted Capabilities
Open-V ocabulary Dimensions 8.50 / 4.37 7.69 / 4.19 8.35 / 4.18 7.44 / 3.95
Instance-Specific Rubrics 8.61 / 4.43 7.90 / 4.29 8.47 / 4.337.83/ 4.21
RQ3: Is failure-grounded attribution necessary for identifying policy bottlenecks?Table 2 separates failure attri-
bution from simpler deficiency-based selection. Dynamic Top-Kby Failure Frequency reselects capabilities each stage
by deficiency prevalence on low-outcome trajectories, but performs no backward attribution or evidence localization.
It underperforms REWARDWEAVERacross all eight metrics, suggesting deficiency frequency alone is insufficient to
reliably identify failure-relevant capabilities in these settings. Random-Trajectory Attribution degrades performance,
suggesting attribution needs to be grounded in outcome-relevant failures rather than generic behavior. Success–Failure
7

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
Trajectory Attribution remains competitive but does not consistently improve over REWARDWEAVER. These results
suggest training relevance is better identified by evidence-grounded failure attribution than by deficiency prevalence
or outcome-agnostic behavioral analysis. Appendix D provides trajectory-level cases of contrastive validation and
selective attribution.
Figure 4:Evolution of capability priorities on SOTOPIA.Normalized priorities of the 15 most prominent Rubrics
across training stages. Reward emphasis shifts as different capability bottlenecks become training-relevant, illustrating
stage-dependent reallocation of process-level credit in REWARDWEAVER.
RQ4: Does semantic stability of admitted capabilities matter?As shown in Table 2, relaxing semantic stability
also reduces performance. Open-V ocabulary Dimensions is consistently weaker than REWARDWEAVERacross all four
settings, suggesting an advantage of maintaining stable, validated capability definitions. Instance-Specific Rubrics is
competitive, but remains inconsistent across settings despite occasionally matching or exceeding individual metrics.
3.3 Reward Adaptation Analysis
Reward Evolution.Figure 4 shows reward emphasis shifting across training stages.Maintain Goal Commitment
dominates early but later recedes, whileSwitch Strategies,State Benefits, andRespond with Empathybecome more
prominent; other capabilities, such asConditional Concessions, re-emerge after decline. These patterns show RE-
WARDWEAVERreallocates process-level credit as training-relevant bottlenecks change, rather than accumulating re-
ward Rubrics.
Bottleneck Attribution and Subsequent Failure Reduction.Complementing the controlled RQ2 ablations, we
examine whether the attribution signal is prospectively associated with bottleneck reduction. We define bottleneck
importanceI k,d =F fail k,d −F succ k,d and next-stage failure reduction∆F k,d =F fail k,d −F fail k+1,d. Bottleneck importance
positively correlates with subsequent reduction (Spearmanρ= 0.28), remains positive after controlling for failure
rate (partialρ= 0.22), and strengthens within stage (ρ= 0.31), while current failure rate alone yieldsρ= 0.21. The
attribution ranking carries prospective information about which bottlenecks recede next. This analysis is not a causal
identification of capability-level improvement; causal evidence comes from the controlled ablations in RQ2 and RQ3.
Full results are reported in Appendix E.
Sensitivity Analysis.We vary both the active Rubric budgetBand the adaptation interval. Performance is non-
monotonic in both:B= 6achieves the strongest overall results among the tested budgets, while the 30-step interval
provides the most consistently strong performance across Self-Play and Partner evaluation. Effective reward adaptation
therefore depends on bothselective credit allocationand anappropriate adaptation timescale. Full results are reported
in Appendix F.
Capability Retention.We examine whether capabilities regress after leaving the active reward set, tracking semanti-
cally aligned capabilities with fixed evaluation criteria across stages. Across the six capabilities deactivated after the
8

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
initial stage, all 36 post-deactivation observations remain within 0.02 of or above their final active scores, with a mean
change of+0.10.Adapt to New Information, deactivated later, remains stable. On the fixed diagnostic set, we observe
no systematic regression in the tracked capabilities after deactivation, providing evidence that reward reallocation need
not immediately erase previously emphasized behaviors. Full results are reported in Appendix G.
4 Related Work
Outcome and Preference-Based Rewards.RLVR grounds rewards in verifiable task outcomes (Shao et al., 2024;
Le et al., 2022; Guo et al., 2025), and process verifiers extend it to intermediate solution steps (Wang et al., 2024a;
Lightman et al., 2024; Lu et al., 2024; Zeng et al., 2025; Setlur et al., 2025; Zheng et al., 2025). RLHF learns reward
models from human preference data (Christiano et al., 2017; Stiennon et al., 2020; Ouyang et al., 2022); subsequent
work diversifies feedback types (Wu et al., 2023; Yuan et al., 2024; Wang et al., 2024c), develops ranking objectives
that bypass explicit reward modeling (Yuan et al., 2023; Hwang et al., 2023; Rafailov et al., 2023), and automates
evaluation with AI feedback and pretrained LLM judges (Lee et al., 2023; Zheng et al., 2023; Liu et al., 2023; Kim
et al., 2024a,b; Ke et al., 2024). In many of these approaches, however, the reward specification is fixed or largely
determined before policy training; which capabilities the current policy should optimize next remains open.
Rubric-Based Process Rewards.Rubrics structure process quality: instance-specific rubrics are auto-generated
(Gunjal et al., 2026; Wei et al., 2026; He et al., 2025), multidimensional evaluators induced (Hashemi et al., 2024),
checklist scoring improves reliability (Lee et al., 2025), construction scales into reusable repositories (Li et al., 2026),
and EvoRubric adapts criteria to the response distribution (Guan et al., 2026). These methods sharpen response-
quality representation, yet discriminability does not determine training priority: a criterion may separate good from
bad responses yet bear weakly on success, whereas a rarely violated capability may bind. Which criteria recurrent
low-outcome failures implicate is underexplored.
Credit Assignment in Multi-Turn Interaction.Assigning feedback in long-horizon interaction is long-standing:
methods decompose delayed returns (Arjona-Medina et al., 2019), transport value across time (Hung et al., 2019),
or estimate counterfactuals (Meulemans et al., 2023). For language agents, feedback spans episode-level scoring
(Zhou et al., 2024a), utterance-level rewards from episode feedback or Shapley decomposition (Yu et al., 2025; Feng
et al., 2026), segment-level preferences (Kong et al., 2025), and process rewards over strategic reasoning (Liu et al.,
2025); hierarchical and retrospective agents optimize behavior (Zhou et al., 2024b; Yao et al., 2024), and automated
attribution localizes failures (Zhang et al., 2025a). Orthogonally, AMPO (Wang et al., 2026) adapts reasoning depth
to interaction modes, WebRL (Qi et al., 2025) evolves curricula, and PPDPP (Deng et al., 2024), DAT (Li et al.,
2024), and DSI (Zhang et al., 2025b) steer dialogue through planners or strategy-injected corpora. These methods
determinewherean objective applies within an interaction; reward adaptation askswhatthe process reward should
contain; REWARDWEAVERselects capability-level objectives from outcome-grounded failures.
5 Discussion
The results of REWARDWEAVERsuggest that reward relevance is stage-dependent and should be grounded in recurrent
failures linked to task outcomes. This casts reward adaptation as an outer-loop problem: standard RL determineshow
to optimize under a given reward, while the outer loop determineswhat should receive training credit next. Reward
adaptation should therefore trackwhat currently limits performance, not merelywhat can be evaluated well.
REWARDWEAVERnevertheless depends on LLM-based evaluators and informative terminal outcomes, so errors in
either can propagate into reward adaptation. Its active budget and adaptation interval may also require re-tuning across
domains.
AI Use Statement
In this work, we used generative AI tools to support discussions of research methodology and experimental de-
sign, qualitative analysis and interpretation of results, and the drafting, restructuring, and language polishing of the
manuscript. Generative AI was also used to improve the presentation and organization of selected algorithm descrip-
tions, tables, figure captions, and appendix materials.
All AI-assisted content was carefully reviewed by the authors. The research methodology, experimental settings,
data, and empirical results were verified against the actual implementation and experimental records, and the authors
independently determined whether to adopt any AI-generated suggestions. The authors take full responsibility for
9

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
the final content of this work, including any text, analysis, or other research artifacts generated or modified with the
assistance of generative AI.
References
Jose A. Arjona-Medina, Michael Gillhofer, Michael Widrich, Thomas Unterthiner, Johannes Brandstetter, and Sepp
Hochreiter. RUDDER: Return decomposition for delayed rewards. InAdvances in Neural Information Processing
Systems (NeurIPS), 2019.
Paul F. Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement
learning from human preferences. InAdvances in Neural Information Processing Systems (NeurIPS), 2017.
Yang Deng, Wenxuan Zhang, Wai Lam, See-Kiong Ng, and Tat-Seng Chua. Plug-and-play policy planner for large
language model powered dialogue agents. InInternational Conference on Learning Representations (ICLR), 2024.
Xiachong Feng, Yi Jiang, Xiaocheng Feng, Deyi Yin, Libo Qin, Yangfan Ye, Lei Huang, Weitao Ma, Yuxuan Gu,
Chonghan Qin, Bing Qin, and Lingpeng Kong. SA VOIR: Learning social savoir-faire via shapley-based reward
attribution.arXiv preprint arXiv:2604.18982, 2026.
Xin Guan, Xiaomeng Hu, Shen Huang, Zhenyi Wang, Bo Zhang, Zijian Li, Pengjun Xie, Bo Liu, and Jiuxin Cao.
EvoRubric: Self-evolving rubric-driven RL for open-ended generation.arXiv preprint arXiv:2605.29847, 2026.
Anisha Gunjal, Anthony Wang, Elaine Lau, Vaskar Nath, Yunzhong He, Bing Liu, and Sean M. Hendryx. Rubrics
as rewards: Reinforcement learning beyond verifiable domains. InThe Fourteenth International Conference on
Learning Representations, 2026.
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Runxin Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi
Wang, Xiao Bi, et al. DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning.Nature, 645:
633–638, 2025.
Helia Hashemi, Jason Eisner, Corby Rosset, Benjamin Van Durme, and Chris Kedzie. LLM-Rubric: A multidimen-
sional, calibrated approach to automated evaluation of natural language texts. InProceedings of ACL, 2024.
Yun He, Wenzhe Li, Hejia Zhang, Songlin Li, Karishma Mandyam, Sopan Khosla, Yuanhao Xiong, Nanshu Wang, Xi-
aoliang Peng, Beibin Li, Shengjie Bi, Shishir G. Patil, Qi Qi, Shengyu Feng, Julian Katz-Samuels, Richard Yuanzhe
Pang, Sujan Gonugondla, Hunter Lang, Yue Yu, Yundi Qian, Maryam Fazel-Zarandi, Licheng Yu, Amine Benhal-
loum, Hany Awadalla, and Manaal Faruqui. AdvancedIF: Rubric-based benchmarking and reinforcement learning
for advancing LLM instruction following.arXiv preprint arXiv:2511.10507, 2025.
Chia-Chun Hung, Timothy Lillicrap, Josh Abramson, Yan Wu, Mehdi Mirza, Federico Carnevale, Arun Ahuja, and
Greg Wayne. Optimizing agent behavior over long time scales by transporting value.Nature Communications,
2019.
Minyoung Hwang, Gunmin Lee, Hogun Kee, Chanwoo Kim, Kyungjae Lee, and Songhwai Oh. Sequential preference
ranking for efficient reinforcement learning from human feedback. InAdvances in Neural Information Processing
Systems (NeurIPS), 2023.
Pei Ke, Bosi Wen, Zhuoer Feng, Xiao Liu, Xuanyu Lei, Jiale Cheng, Shengyuan Wang, Aohan Zeng, Yuxiao Dong,
Hongning Wang, Jie Tang, and Minlie Huang. CritiqueLLM: Towards an informative critique generation model for
evaluation of large language model generation. InProceedings of ACL, 2024.
Seungone Kim, Jamin Shin, Yejin Cho, Joel Jang, Shayne Longpre, Hwaran Lee, Sangdoo Yun, Seongjin Shin, Sung-
dong Kim, James Thorne, and Minjoon Seo. Prometheus: Inducing fine-grained evaluation capability in language
models. InInternational Conference on Learning Representations (ICLR), 2024a.
Seungone Kim, Juyoung Suk, Shayne Longpre, Bill Yuchen Lin, Jamin Shin, Sean Welleck, Graham Neubig, Moontae
Lee, Kyungjae Lee, and Minjoon Seo. Prometheus 2: An open source language model specialized in evaluating
other language models. InProceedings of EMNLP, 2024b.
Aobo Kong, Wentao Ma, Shiwan Zhao, Yongbin Li, Yuchuan Wu, Ke Wang, Xiaoqian Liu, Qicheng Li, Yong Qin,
and Fei Huang. SDPO: Segment-level direct preference optimization for social agents. InProceedings of ACL, pp.
12409–12423, 2025.
Hung Le, Yuheng Wang, Shafiq Gotmare, Silvio Savarese, and Steven Hoi. CodeRL: Mastering code generation
through pretrained models and deep reinforcement learning. InAdvances in Neural Information Processing Systems
(NeurIPS), 2022.
Harrison Lee, Samrat Phatale, Hassan Mansoor, Kellie Lu, Thomas Mesnard, Colton Bishop, Ethan Ferret, and
Peter Riedel. RLAIF: Scaling reinforcement learning from human feedback with AI feedback.arXiv preprint
arXiv:2309.00267, 2023.
10

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
Yukyung Lee, Joonghoon Kim, Jaehee Kim, Hyowon Cho, Pilsung Kang, and Najoung Kim. CheckEval: A reliable
LLM-as-a-judge framework for evaluating text generation using checklists. InProceedings of EMNLP, 2025.
Kenneth Li, Yiming Wang, Fernanda Vi ´egas, and Martin Wattenberg. Dialogue action tokens: Steering language
models in goal-directed dialogue with a multi-turn planner.arXiv preprint arXiv:2406.11978, 2024.
Sunzhu Li, Jiale Zhao, Miteto Wei, Huimin Ren, Yang Zhou, Jingwen Yang, Shunyu Liu, Kaike Zhang, and Wei Chen.
RubricHub: A comprehensive and highly discriminative rubric dataset via automated coarse-to-fine generation.
arXiv preprint arXiv:2601.08430, 2026.
Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman,
Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. InInternational Conference on Learning Representations
(ICLR), 2024.
Xiaoqian Liu, Ke Wang, Yongbin Li, Yuchuan Wu, Wentao Ma, Aobo Kong, Fei Huang, Jianbin Jiao, and Junge
Zhang. EPO: Explicit policy optimization for strategic reasoning in LLMs via reinforcement learning. InProceed-
ings of ACL, pp. 15371–15396, 2025.
Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang, Ruochen Xu, and Chenguang Zhu. G-Eval: NLG evaluation using
GPT-4 with better human alignment. InProceedings of EMNLP, 2023.
Jianqiao Lu, Zhiyang Dou, Hongru Wang, Zeyu Cao, Jianbo Dai, Yingjia Wan, Yunlong Feng, and Zhijiang Guo. Au-
toPSV: Automated process-supervised verifier. InAdvances in Neural Information Processing Systems (NeurIPS),
2024.
Alexander Meulemans, Simon Schug, Seijin Kobayashi, Nathaniel D. Daw, and Gregory Wayne. Would I have got-
ten that reward? Long-Term credit assignment by counterfactual contribution analysis. InAdvances in Neural
Information Processing Systems (NeurIPS), 2023.
Long Ouyang, Jeffrey Wu, Xu Jiang, et al. Training language models to follow instructions with human feedback. In
Advances in Neural Information Processing Systems (NeurIPS), 2022.
Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Jiadai Sun, Xinyue Yang, Yu Yang, Shuntian Yao,
Wei Xu, Jie Tang, and Yuxiao Dong. WebRL: Training LLM web agents via self-evolving online curriculum
reinforcement learning. InInternational Conference on Learning Representations (ICLR), 2025.
Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and Chelsea Finn. Direct
preference optimization: Your language model is secretly a reward model. InAdvances in Neural Information
Processing Systems (NeurIPS), 2023.
Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal,
Jonathan Berant, and Aviral Kumar. Rewarding progress: Scaling automated process verifiers for LLM reasoning.
InInternational Conference on Learning Representations (ICLR), 2025.
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li,
Y Wu, et al. DeepSeekMath: Pushing the limits of mathematical reasoning in open language models.arXiv preprint
arXiv:2402.03300, 2024.
Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea V oss, Alec Radford, Dario
Amodei, and Paul F. Christiano. Learning to summarize from human feedback. InAdvances in Neural Information
Processing Systems (NeurIPS), 2020.
Minzheng Wang, Yongbin Li, Haobo Wang, Xinghua Zhang, Nan Xu, Bingli Wu, Fei Huang, Haiyang Yu, and Wenji
Mao. Adaptive social learning via mode policy optimization for language agents. InInternational Conference on
Learning Representations (ICLR), 2026.
Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-
shepherd: Verify and reinforce LLMs step-by-step without human annotations. InProceedings of ACL, 2024a.
Ruiyi Wang, Haofei Yu, Wenxin Zhang, Zhengyang Qi, Maarten Sap, Graham Neubig, Yonatan Bisk, and Hao Zhu.
SOTOPIA-π: Interactive Learning of Socially Intelligent Language Agents.arXiv preprint arXiv:2403.08715,
2024b.
Zhilin Wang, Yi Dong, Olivier Delalleau, Jiaqi Zeng, Gerald Shen, Daniel Egert, Jimmy J. Zhang, Makesh Narsimhan
Sreedhar, and Oleksii Kuchaiev. HelpSteer2: Open-source dataset for training top-performing reward models. In
Advances in Neural Information Processing Systems (NeurIPS), 2024c.
Xiyu Wei, Qingwei Zong, Xiaoguang Li, Eugene J. Yu, and Sujian Li. QuRL: Rubrics as judge for open-ended
question answering. InInternational Conference on Learning Representations (ICLR), 2026.
11

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
Zeqiu Wu, Yushi Hu, Weijia Shi, Nouha Dziri, Alane Suhr, Prithviraj Ammanabrolu, Noah A. Smith, Mari Ostendorf,
and Hannaneh Hajishirzi. Fine-grained human feedback gives better rewards for language model training. In
Advances in Neural Information Processing Systems (NeurIPS), 2023.
Tian Xia, Zhiwei He, Tong Ren, Yibo Miao, Zhuosheng Zhang, Yang Yang, and Rui Wang. Measuring bargaining abil-
ities of LLMs: A benchmark and a buyer-enhancement method. InFindings of the Association for Computational
Linguistics: ACL 2024, 2024.
Weiran Yao, Shelby Heinecke, Juan Carlos Niebles, Zhiwei Liu, Yihao Feng, Le Xue, Rithesh Murthy, Zeyuan Chen,
Jianguo Zhang, Devansh Arpit, Ran Xu, Phil Mui, Huan Wang, Caiming Xiong, and Silvio Savarese. Retroformer:
Retrospective large language agents with policy gradient optimization. InInternational Conference on Learning
Representations (ICLR), 2024.
Haofei Yu, Zhengyang Qi, Yining Zhao, Kolby Nottingham, Keyang Xuan, Bodhisattwa Prasad Majumder, Hao
Zhu, Paul Pu Liang, and Jiaxuan You. SOTOPIA-RL: Reward design for social intelligence.arXiv preprint
arXiv:2508.03905, 2025.
Hongyi Yuan, Zheng Yuan, Chuanqi Tan, Wei Wang, Songfang Huang, and Fei Huang. RRHF: Rank responses to
align language models with human feedback. InAdvances in Neural Information Processing Systems (NeurIPS),
2023.
Yifu Yuan, Jianye Hao, Yi Ma, Zibin Dong, Hebin Liang, Jinyi Liu, Zhixin Feng, Kai Zhao, and Yan Zheng. Uni-
RLHF: Universal platform and benchmark suite for reinforcement learning with diverse human feedback. InInter-
national Conference on Learning Representations (ICLR), 2024.
Thomas Zeng, Shuibai Zhang, Shutong Wu, Christian Classen, Daewon Chae, Ethan Ewer, Minjae Lee, Heeju Kim,
Wonjun Kang, Jackson Kunde, Ying Fan, Jungtaek Kim, Hyung Il Koo, Kannan Ramchandran, Dimitris Papail-
iopoulos, and Kangwook Lee. VersaPRM: Multi-domain process reward model via synthetic reasoning data. In
International Conference on Machine Learning (ICML), 2025.
Shaokun Zhang, Ming Yin, Jieyu Zhang, Jiale Liu, Zhiguang Han, Jingyang Zhang, Beibin Li, Chi Wang, Huazheng
Wang, Yiran Chen, and Qingyun Wu. Which agent causes task failures and when? On automated failure attribution
of LLM multi-agent systems. InInternational Conference on Machine Learning (ICML), 2025a.
Wenyuan Zhang, Tianyun Liu, Mengxiao Song, Xiaodong Li, and Tingwen Liu. SOTOPIA-Ω: Dynamic strategy
injection learning and social instruction following evaluation for social agents. InProceedings of ACL, pp. 24669–
24697, 2025b.
Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and
Junyang Lin. ProcessBench: Identifying process errors in mathematical reasoning. InProceedings of ACL, 2025.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li,
Dacheng Li, Eric Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. Judging LLM-as-a-judge with MT-Bench
and Chatbot Arena. InAdvances in Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks
Track, 2023.
Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong Zhang, Zhengyang Qi, Haofei Yu, Louis-Philippe Morency, Yonatan
Bisk, Daniel Fried, Graham Neubig, and Maarten Sap. SOTOPIA: Interactive evaluation for social intelligence in
language agents. InInternational Conference on Learning Representations (ICLR), 2024a.
Yifei Zhou, Andrea Zanette, Jiayi Pan, Sergey Levine, and Aviral Kumar. ArCHer: Training language model agents
via hierarchical multi-turn RL. InInternational Conference on Machine Learning (ICML), 2024b.
12

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
A Validated Capability-Space Construction for SOTOPIA in RewardWeaver
The SOTOPIA capability space contains 40 validated Rubrics organized into seven behavioral families. We first
summarize the structure of the space (Table A1), then present representative semantic entries (Table A2), and finally
show how a frozen Rubric is operationalized into an executable evaluator (Section A.3).
Table A1:Behavioral families in the SOTOPIA capability Rubric library.The validated space contains 40
individual Rubrics across seven families.
Family # Rubrics Behavioral Scope
Goal Expression and Persistence 5 Goal articulation and retention
Information Acquisition 8 Information elicitation and clarification
Information Use 5 Evidence use and adaptation
Concern Handling and Persuasion 6 Objection handling and negotiation
Goal Progression and Closure 7 Progress, strategy, and completion
Relationship Management 5 Empathy and interaction quality
Boundaries and Safety 4 Privacy, truthfulness, and social boundaries
Total 40
A.1 Capability-Space Overview
Table A1 summarizes the seven behavioral families spanned by the 40-dimensional SOTOPIA capability space. The
grouping is organizational: failure attribution and reward adaptation operate over individual Rubrics rather than family-
level scores.
A.2 Representative Capability Rubrics
Table A2 presents representative entries covering the major regions of the capability space. Definitions are condensed
for readability while preserving their operative behavioral distinctions. Positive and negative evidence illustrate the
intended semantic boundary of each Rubric.
A.3 Rubric-Specific Evaluator Operationalization
We use USE OFKEYINFORMATION, introduced in Table A2, as a concrete example of Rubric-Specific Evaluator
construction. The Rubric semantics are fixed before evaluator development; operationalization specifies when the
Rubric applies, how it is scored, and how uncertainty is handled.
Table A3 summarizes the resulting decision structure.
Table A3:Operationalization of USE OFKEYINFORMATION.Applicability is determined before scoring, and
insufficient evidence is distinguished from genuine non-applicability.
Field Operationalization
Rubric IDfixed-use-key-information-v1
Applicability The Rubric applies when at least one safe, directly relevant fact, preference, constraint, or con-
firmed arrangement is available in the visible context before the target response.
Score= 1The target response accurately uses at least one currently relevant item of known information to
explain, request, confirm, adapt, or respond.
Score= 0The Rubric applies, but the target response uses none of the relevant known information, or mis-
states a relevant fact, quantity, person, relation, or constraint.
Non-applicable (N) No safe and directly relevant information is available for the current response. Failure to use
available information is scored as0, notN.
Abstain (U) The visible evidence is insufficient to determine applicability or scoring without guessing.
Boundary / Exclusion Generic acknowledgment does not count as information use unless it clearly refers to a specific
fact established in context. Earlier use of a fact does not imply that the current response uses it,
and external knowledge is not introduced to supplement missing evidence.
13

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
Table A2:Representative entries from the 40-dimensional SOTOPIA capability Rubric library.The selected
entries span goal expression, information acquisition and use, adaptation, persuasion, goal progression, relationship
management, and behavioral boundaries. USE OFKEYINFORMATIONis further operationalized in Section A.3.
ID Capability Definition Positive Evidence Negative Evidence
explicit-goalExplicit Goal Expres-
sion
Explicitly state a task-required request,
position, information, feeling, bound-
ary, or correction that has not yet been
expressed.
Asks a phone-using companion to
put the phone away and engage
with the group.
Comments on the pleasant gather-
ing without stating the underlying
request.
elicit-key-infoTargeted Information
Elicitation
Directly ask for task-relevant informa-
tion that is required but not yet avail-
able.
Asks the landlord about the de-
posit policy for early lease termi-
nation.
Continues discussing property
maintenance without asking
about the needed policy.
use-key-
information
Use of Key Information Accurately use at least one known, rel-
evant, and safely usable fact to support
the current response.
Explains a fear of enclosed spaces
when declining an escape-room
proposal.
Argues only that the alternative is
more popular, leaving the relevant
constraint unused.
adapt-to-new-infoAdapt to New Informa-
tion
Adjust a request or plan when newly
disclosed information changes its feasi-
bility.
Suggests Thursday after learning
that the partner will be away on
Wednesday.
Repeats the Wednesday request
despite the disclosed trip.
address-concernAddress Concerns with
New Options
After the partner raises a specific con-
cern, propose an actionable adjustment
that directly reduces that concern.
Proposes a small low-sugar cake
with ventilation after concerns
about smell and diet.
Repeats that baking is enjoyable
without modifying the proposal.
strategy-pivotSwitch Strategies After repeated rejection or deferral, use
a new argument, angle, or plan rather
than repeating the same request.
Proposes a three-month hybrid-
work trial after repeated remote-
work rejections.
Repeats the same remote-work
request without changing the ar-
gument or plan.
empathic-
acknowledgment
Respond with Empathy Acknowledge the partner’s expressed
negative emotion or difficulty before
continuing the task interaction.
Recognizes a colleague’s exhaus-
tion before proposing how to di-
vide the remaining report work.
Ignores the exhaustion and imme-
diately demands additional over-
time.
secret-keepingConfidentiality Preser-
vation
Avoid disclosing information explicitly
marked as confidential when the related
topic arises.
Discusses an investment proposal
without revealing confidential fi-
nancial circumstances.
Explicitly reveals information
marked confidential in the task
context.
reject-improper-
request
Rejection of Improper
Requests
Explicitly reject a request that violates
social norms, law, or the agent’s stated
boundaries.
Refuses to make a false statement
to cover for a roommate.
Agrees to falsely take responsibil-
ity for the roommate’s rule viola-
tion.
privacy-boundaryPrivacy Boundary Re-
spect
Avoid probing task-irrelevant sensitive
personal information when such infor-
mation enters the conversation.
Offers to reschedule a contract
discussion after a family hospital-
ization is mentioned.
Presses for details about the ill-
ness, costs, and unrelated finan-
cial circumstances.
Evaluator Operationalization.Each candidate is operationalized by a dedicated evaluator and subjected to source-
disjoint acceptance testing: the evaluator is developed on a development partition, and admission is decided on source-
disjoint held-out cases. Rubric semantics remain fixed throughout evaluator development; prompt refinement only
clarifies applicability, scoring boundaries, and abstention behavior. Once admitted, both the Rubric definition and
evaluator are frozen across training stages. This separation between semantic definition and evaluator operationaliza-
tion ensures that reward adaptation changes which capabilities receive training credit rather than what those capabilities
mean.
14

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
B Sales Benchmark Construction and Evaluation
We construct the Sales Benchmark to evaluate long-horizon interaction under structured business rules, asymmetric
information, and conflicting objectives. The benchmark contains 400 health-service sales tasks across 20 scenario
families, with 20 profile-conditioned instances per family. Among them, 350 are standard tasks and 50 are constraint-
conflict tasks. This appendix details benchmark construction, quality control, data splits, evaluation, and representative
tasks.
B.1 Construction Protocol
Each scenario family is instantiated with 20 buyer profiles. The 13 retained families use a bank of 20 buyer profiles,
while the seven replacement families use a separate bank of 20 enterprise-buyer profiles, yielding 260 and 140 tasks,
respectively.
Model-assisted authoring.We used GPT-5.6 Sol via Codex to assist with task drafting and refinement, conditioned
on scenario specifications and buyer profiles. Construction includes explicit specification and revision of business
rules, role goals, and private constraints rather than surface-level paraphrasing. The resulting task specifications are
programmatically compiled into runtime views containing a shared scenario and role-specific information.
Prices, procedures, and service policies are fictional environment facts. The benchmark is entirely synthetic and is
intended to evaluate interactive decision making and constraint following, not medical reasoning, diagnosis, or real-
world healthcare recommendations; no real patient data are used. Each participant receives only its own role view; the
counterpart’s private information and internal authoring answer keys are excluded.
B.2 Authoring Template and Quality Control
The following compact template summarizes the constraints used to specify and revise tasks. It captures the construc-
tion protocol rather than reproducing every historical authoring request verbatim.
Construct or revise a health-service sales task from:
{scenario specification},{buyer profile},{business rules},
and{standard / constraint-conflict designation}.
Return: a shared scenario, seller goal and private information,
and buyer goal and private information.
Specify decision-relevant options, prices, timing, and authority.
Preserve supplied facts and intended goal conflicts; flag missing
or inconsistent constraints for revision. Keep private facts in
the appropriate role view and internal answer keys outside both
views. Define outcomes observable within the interaction, without
assuming future third-party consent or actions. Do not prescribe
an ideal dialogue or make unsupported medical claims.
Quality control and deduplication.Tasks are checked for schema completeness, sufficient decision-relevant in-
formation, internal consistency of business rules, appropriate role visibility, and observable completion conditions.
Underspecified or inconsistent drafts are revised while preserving intentional goal conflicts.
Automated validation additionally checks for internal answer-key fields in runtime inputs and exact matches of private-
information strings in unauthorized role views. Task-ID uniqueness and exact-match checks over serialized environ-
ment specifications verify that the final collection contains 400 distinct task records.
B.3 Scenario Families
Table B1 summarizes the 20 scenario families. The displayed names are abbreviated; complete task specifications and
identifiers will accompany the released benchmark.
15

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
Table B1:Scenario families in the Sales Benchmark.
Family Scenario
R01 Staged corporate procurement
R02 Data-use purpose separation
R03 Cross-city service-network due diligence
R04 Multi-site acceptance and objection terms
R05 Corporate lead qualification
R06 Sign-language and bilingual support
R07 Contract, payment, and invoice entities
S01 Budget-constrained add-ons
S02 Final price confirmation
S04 Retention against a cheaper competitor
S05 Package reduction
S06 Deposits and slot reservation
S10 Time-constrained service selection
S13 Paid report interpretation
S14 Package-tier selection
S15 Renewal timing
S16 Referral rewards
S17 Gift-package transfer
S19 Follow-up examination conversion
S20 Refund and replacement purchase
B.4 Split and Evaluation
Split and overlap checks.We use a fixed 320/80 train–evaluation split, assigning 16 training and four evaluation
tasks to each scenario family. The training split contains 287 standard and 33 constraint-conflict tasks; the evaluation
split contains 63 standard and 17 constraint-conflict tasks.
No task IDs or exact serialized environment specifications overlap across the two partitions. Scenario families and
profile banks are shared across the split, so the evaluation split measures generalization to unseen tasks within each
scenario family. The 80-task evaluation set is reserved for final reporting; it never participates in reward adaptation or
checkpoint selection.
Outcome evaluation.The outcome judge is Qwen2.5-72B. It receives the shared scenario, both participants’ back-
grounds and goals, and the complete dialogue, and applies the seven-dimensional SOTOPIA-EV AL rubric without
additional sales-specific authoring answer keys. The reported Overall score is the arithmetic mean of the seven raw
dimension scores.
This outcome evaluator is distinct from the process-reward evaluators used during training.
Release.We will release the benchmark alongside the paper, including the task specifications, fixed split manifest,
construction instructions, and evaluation materials containing the actual scoring prompt, parser, and aggregation code.
B.5 Representative Tasks
We provide two representative tasks below. These are condensed English renderings of the underlying task specifica-
tions rather than complete runtime exports; personality fields and secondary business details are omitted for brevity.
Standard: Refund and replacement purchase.sales-crafted-S20-P01. A buyer requests a refund for an
unused RMB 799 health-check package because an employer-provided examination duplicates several included items.
The seller may offer fixed RMB 599 alternatives with a RMB 200 difference refund, but must preserve the buyer’s
unconditional full-refund option. The buyer privately knows which items are already covered and remains interested
in a six-hormone panel. The interaction therefore requires eliciting existing coverage and preferences before seeking
a voluntary replacement purchase.
Constraint conflict: Gift-package transfer.sales-crafted-S17-P03. The seller seeks a voluntary RMB 180
upgrade, whereas the buyer wants to transfer the gifted package without additional payment. Free transfer requires
an independent recipient-confirmation link; the buyer cannot provide consent on the recipient’s behalf. The seller
must explain the free-transfer option and stop pressing the upgrade after an explicit refusal. Initiating a compliant
16

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
free transfer does not satisfy the seller’s paid-upgrade objective, and issuing the link does not by itself establish a
completed transfer.
17

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
C Additional Benchmark Results of RewardWeaver
Table C1 reports the full AmazonHistoryPrice results corresponding to Figure 3 in the main text. Table C2 presents
the full results on the Sales Benchmark under Self-Play and Partner evaluation.
Table C1:Main results on AmazonHistoryPrice.All sellers are evaluated withdeepseek-v4-proas the buyer.
The best result in each column is shown inbold.
Method MI Deal Rate↑ CI Correct No-Deal Rate↑ Task Success Rate↑ Normalized Seller Utility↑ Expected MI Seller Return↑
Proprietary LLMs
doubao-seed-2-0-pro94.40100.0094.50 0.85 0.80
glm-5.3-flash95.20 100.00 95.300.91 0.86
glm-5.292.00100.0092.20 0.93 0.86
qwen3.8-max80.80100.0081.30 0.95 0.76
qwen3.8-flash83.20100.0083.60 0.93 0.77
qwen3.7-plus51.20100.0052.30 0.92 0.47
deepseek-v4-pro83.20100.0083.60 0.87 0.73
Post-training on Qwen2.5-7B-Instruct
Qwen2.5-7B-Instruct w/ GRPO 84.00 66.70 83.60 0.56 0.47
REWARDWEAVER(ours) 95.20 100.00 95.30 0.97 0.93
Table C2:Main results on the Sales Benchmark.In the Partner setting, the counterpart is Qwen2.5-72B-Instruct.
The best result in each column is shown inbold.
Self-Play Partner
Method Sales Goal / Overall↑ Sales-Hard Goal / Overall↑ Sales Goal / Overall↑ Sales-Hard Goal / Overall↑
Proprietary LLMs
doubao-seed-2-1-pro8.55 / 4.36 7.29 / 3.99 8.81 / 4.43 7.47 / 4.10
qwen3.8-max8.65 / 4.38 7.76 / 4.09 8.76 / 4.43 7.76 / 4.17
gemini-3.1-pro-preview8.63 / 4.37 7.29 / 4.11 8.83 / 4.48 7.59 / 4.08
deepseek-v4-pro8.68 / 4.30 7.24 / 3.97 8.67 / 4.39 7.82 / 4.17
glm-5.28.38 / 4.30 7.59 / 4.12 8.73 / 4.407.88/ 4.19
Post-training on Qwen2.5-7B-Instruct
Qwen2.5-7B-Instruct 8.33 / 4.30 7.18 / 3.97 8.41 / 4.33 7.12 / 3.99
Qwen2.5-7B-Instruct w/ GRPO 8.38 / 4.41 7.71 / 4.28 8.59 / 4.47 7.65 /4.29
REWARDWEAVER(ours) 8.73/4.43 7.88/4.31 8.90/4.537.71 / 4.24
18

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
D Qualitative Case Studies of RewardWeaver
To complement the aggregate experiments, we examine how reward adaptation operates at the trajectory level through
three representative cases from a complete SOTOPIA training run. Together, they illustrate three properties of the
mechanism: stage-dependent bottleneck transition, contrastive validation of failure-derived Rubrics, and selective
attribution under uncertainty.
D.1 Bottleneck Transition
Multiple low-outcome trajectories exhibit a recurrent pattern of verbose, abstract, and difficult-to-interpret language.
In a representative right-of-way negotiation at a four-way stop, the agent receives Goal Completion2/10, and the task
evaluator explicitly attributes the failure to unclear communication. The same pattern recurs across other trajectories
in the cohort, indicating a stage-level bottleneck rather than an isolated error.
The subsequent attribution step identifiesClear Expressionas a candidate capability. Following rubric generation
and calibration, the next reward specification incorporates a criterion targeting the observed communication failures.
In the following stage, repeated rollouts of the same scenario exhibit improved behavior, reaching Goal Completion
scores of 7 and 9; the previous language degradation was not observed in the sampled follow-up rollouts. The failure
distribution then shifts again: the new low-outcome cohort exhibits a different recurrent pattern, and the next adaptation
step redirects emphasis towardConcrete Solutions.
The case illustrates the stage dependence of training relevance:
recurrent failure→bottleneck attribution→reward adaptation→new failure distribution.
A capability need not remain a training priority once its associated bottleneck recedes, and a capability that was previ-
ously non-limiting may become dominant as the policy and interaction distribution evolve. Thus, REWARDWEAVER
allocates process-level credit according to the current bottleneck rather than a fixed capability set.
As scorecards are regenerated between adaptation stages, the qualitative comparison is based on repeated evaluation
of the same scenario.
D.2 Contrastive Validation of Failure-Derived Rubrics
A Rubric proposed from failure-side evidence is not necessarily specific to failure. A candidate evaluator forEmpathic
Supportis calibrated on a matched set containing both high- and low-outcome trajectories. The evaluator is applicable
to 23 trajectories, yet all 23 pass, yielding zero observed failures and very low score variation. It is flagged as collapsed
and targeted for revision. The candidate rubric set fails the publication gate because its validity rate is below the
required threshold. Rubric-set acceptance conditions govern publication, while Rubric-level diagnostics guide local
revision.
This distinction is central:
failure-derived̸⇒failure-specific.
A Rubric may be motivated by failed trajectories yet fail to distinguish failure-relevant behavior on held-out contrastive
examples. Such a signal provides little useful discrimination for process supervision. REWARDWEAVERtherefore
separates bottleneck discovery from reward-rubric calibration: failure evidence proposes candidate capabilities, while
calibration determines whether the generated rubric set satisfies publication conditions and uses Rubric-level diagnos-
tics to guide revision.
This mechanism differs from the Success–Failure Trajectory Attribution variant studied in RQ3, which introduces suc-
cess trajectories during bottleneck attribution. Here, calibration occurs after rubric generation and governs publication
of the candidate reward specification. Success trajectories are not required for the failure-attribution step; calibration
remains required before publishing an updated reward specification.
D.3 Selective Attribution under Uncertainty
Failure-grounded attribution does not require every low-outcome trajectory to be mapped to an agent-side capability
deficit. In one representative trajectory, the agent fails to achieve its task goal because the partner’s private objective
is to decline the interaction. The task evaluator explicitly attributes the outcome to the partner’s preference, and no
agent-side capability is activated.
19

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
Similar cases occur elsewhere in the run, including trajectories with low terminal outcomes despite all currently active
capability checks being satisfied. These observations establish that terminal failure alone is insufficient evidence for
capability-level credit assignment.
The attribution pipeline therefore admits three outcomes:
supported capability bottleneck,interaction-driven failure,insufficient evidence.
Capability-level training credit is assigned only when the failure admits an evidence-supported, policy-controlled
bottleneck. This selectivity prevents partner behavior, scenario constraints, or ambiguous evidence from being silently
converted into agent-side learning objectives.
Accordingly, failure-grounded attribution is not forced attribution: low outcome determines which trajectories war-
rant diagnosis, whereas capability-level credit is assigned only when the failure is supported by observable, policy-
controlled evidence.
Summary.The three cases illustrate complementary aspects of adaptive process rewards. First, training relevance
is stage-dependent and should track the current failure bottleneck. Second, failure-derived Rubrics require calibration
before publication: rubric-set acceptance checks govern publication, while Rubric-level diagnostics guide revision.
Third, attribution remains selective under uncertainty: low outcome is a trigger for diagnosis, not a guarantee of
capability-level blame.
Together, the cases show that effective reward adaptation requires current relevance, discriminative criteria, and
evidence-supported attribution; REWARDWEAVERtherefore combines evidence-grounded candidate selection with
rubric-set calibration.
20

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
E Association Between Bottleneck Attribution and Subsequent Failure Reduction
We further analyze whether the bottleneck importance estimated by REWARDWEAVERis informative about subse-
quent changes in capability-level failure patterns.
E.1 Analysis Setup
For each capabilitydat training stagek, we define bottleneck importance as
Ik,d =F fail k,d −F succ k,d ,
whereF fail k,d is the fraction of low-outcome trajectories attributed to a deficiency in capabilityd, andF succ k,d is the
corresponding fraction among high-outcome trajectories. A largerIk,d therefore indicates that the capability deficiency
is more strongly associated with low-outcome trajectories.
This contrast is constructed for analysis: the attribution mechanism itself (Section 2.3) operates on low-outcome tra-
jectories only, and the success-side contrast is introduced here to characterize how informative the attribution ranking
is.
We quantify the subsequent reduction of this failure mode as
∆Fk,d =F fail k,d −F fail k+1,d,
such that a larger positive value corresponds to a larger decrease in the attributed failure rate in the following stage.
We evaluate this relationship over 240 capability–stage pairs spanning 40 capabilities and six adjacent training-stage
transitions. We use Spearman rank correlation because the attribution mechanism primarily operates through relative
capability priorities.
E.2 Results
Table E1 summarizes the results. Bottleneck importance exhibits a positive association with next-stage failure re-
duction, with Spearmanρ= 0.28. In comparison, the current failure rate alone shows a weaker association with
subsequent reduction (ρ= 0.21).
To determine whether the attribution signal provides information beyond the prevalence of the current failure mode,
we additionally control forF fail k,d . The association remains positive, with partial Spearmanρ= 0.22. We further
compare capabilities within the same training stage, obtaining a stronger association ofρ= 0.31.
Table E1:Association between bottleneck attribution and subsequent failure reduction.We measure the associ-
ation between capability-level signals at stagekand the reduction in attributed failures at stagek+ 1.
Analysis Spearmanρ
Bottleneck importanceI k,d vs.∆F k,d 0.28
Current failure rateF fail k,d vs.∆F k,d 0.21
Ik,d vs.∆F k,d, controlling forF fail k,d 0.22
Within-stage association 0.31
The comparison reveals two complementary properties of the attribution signal. First, its association is stronger than
that of current failure prevalence alone. Second, the association remains positive after accounting for current failure
prevalence and when capabilities are compared within the same training stage. Thus, the attribution signal provides
a stage-dependent ranking whose higher values are associated with larger subsequent reductions in capability-level
failure rates.
21

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
F Sensitivity Analysis of RewardWeaver
We examine two design choices governing reward adaptation in REWARDWEAVER: the number of capabilities that
receive concurrent training credit and the frequency with which this allocation is updated. Unless otherwise specified,
the main configuration uses an active Rubric budget ofB= 6and updates reward allocation every 30 optimization
steps.
F.1 Active Rubric Budget
Table F1 varies the number of concurrently active Rubrics under both Self-Play and Partner evaluation. Performance is
non-monotonic inB: neither reducing the active set nor activating more Rubrics consistently improves performance.
The main settingB= 6achieves the strongest results across all reported settings, suggesting that effective process
supervision depends on concentrating training credit on a selective set of current bottlenecks rather than accumulating
additional Rubrics.
Table F1:Sensitivity to the active Rubric budgetB.Results are reported as Goal Completion / Overall under both
Self-Play and Partner evaluation. The main configuration usesB= 6. Increasing the number of simultaneously active
Rubrics does not monotonically improve performance, supporting selective rather than cumulative credit allocation.
Self-Play Partner
BSOTOPIA SOTOPIA-Hard SOTOPIA SOTOPIA-Hard
2 8.46 / 4.32 7.50 / 3.97 8.38 / 4.17 7.46 / 3.92
4 8.31 / 4.29 7.79 / 4.16 8.21 / 4.19 7.37 / 4.03
6 8.72 / 4.47 7.90 / 4.38 8.49 / 4.47 7.66 / 4.22
8 8.49 / 4.44 7.67 / 4.25 8.31 / 4.25 7.59 / 4.15
10 8.50 / 4.46 7.63 / 4.36 8.34 / 4.37 7.57 / 4.21
F.2 Adaptation Interval
Table F2 varies the reward-adaptation interval under both Self-Play and Partner evaluation. Performance is again
non-monotonic. The 30-step configuration provides the most consistently strong results across interaction modes and
difficulty levels: it achieves the strongest Goal Completion scores under Self-Play and the strongest results across all
Partner settings, while the 20-step setting is marginally higher on selected Self-Play Overall scores.
These results indicate that reward adaptation is sensitive to its update timescale rather than benefiting monotonically
from either faster or slower updates.
Table F2:Sensitivity to the reward-adaptation interval.The main configuration updates reward allocation every
30 optimization steps. Results are reported as Goal Completion / Overall.
Self-Play Partner
Interval SOTOPIA SOTOPIA-Hard SOTOPIA SOTOPIA-Hard
10 8.28 / 4.41 7.73 / 4.36 8.32 / 4.33 7.59 / 4.20
20 8.50 /4.477.81 /4.398.27 / 4.19 7.47 / 4.03
30 8.72/4.47 7.90/ 4.388.49 / 4.47 7.66 / 4.22
60 8.21 / 4.26 7.44 / 3.95 8.34 / 4.28 7.49 / 4.04
Taken together, the two analyses highlight complementary requirements of adaptive process rewards: credit allocation
should remain selective in capability space and operate at an appropriate adaptation timescale.
22

RewardWeaver: Self-Evolving Reward AdaptationA PREPRINT
G Capability Retention under Reward Reallocation
We further examine whether reallocating process-level credit causes previously emphasized capabilities to deteriorate
once they leave the active reward set.
G.1 Evaluation Protocol
We evaluate the policy at each stage on the same fixed diagnostic scenarios and score each tracked capability using
a fixed evaluation criterion across all stages. For capabilitydat stagek, we denote the resulting diagnostic score by
Sk,d, computed as the mean normalized process score over applicable episodes.
Six capabilities receive process-level credit in the initial stage and are subsequently deactivated:Address Concerns
with New Options,State Benefits,Conditional Concessions,Maintain Goal Commitment,Regulate Pressure, and
Switch Strategies.Adapt to New Informationis deactivated at a later stage. We additionally report three continuously
active capability families, namelyRespond with Empathy,Early Disclosure, andConcrete Next Step, as reference
trajectories.
For a capability deactivated after stagek, we measure retention by its subsequent change∆S t,d =S k+t,d −S k,d
relative to the final active stage.
G.2 Retention Results
Table G1 reports the capability trajectories. The six capabilities deactivated after the initial stage show no systematic
regression: across 36 post-deactivation capability–stage observations, the mean change is+0.10, the median change
is+0.06, and the minimum change is−0.01. No observation decreases by more than 0.02 from its final active score.
Adapt to New Information, which is deactivated later, remains at 1.00 throughout all subsequent stages.
Table G1:Capability retention across training stages.†denotes capabilities deactivated after the initial stage,‡
denotes a capability deactivated later, and unmarked dimensions remain active during the evaluated period.
Capability Stage 1 Stage 2 Stage 3 Stage 4 Stage 5 Stage 6 Stage 7
Address Concerns with New Options†0.80 0.85 0.92 0.95 0.86 0.89 0.90
State Benefits†0.84 0.88 0.97 0.98 0.95 0.94 0.98
Conditional Concessions†0.85 0.90 0.98 0.93 0.86 0.90 0.96
Maintain Goal Commitment†0.96 0.95 1.00 0.98 0.96 1.00 1.00
Regulate Pressure†1.00 1.00 1.00 1.00 1.00 1.00 1.00
Switch Strategies†0.62 0.91 1.00 1.00 0.88 1.00 1.00
Adapt to New Information‡1.00 0.99 1.00 1.00 1.00 1.00 1.00
Respond with Empathy 0.99 1.00 1.00 1.00 1.00 1.00 1.00
Early Disclosure 0.92 0.90 0.94 0.94 0.91 0.92 0.99
Concrete Next Step 0.99 1.00 1.00 1.00 0.99 0.99 0.99
The event-aligned trajectories make the retention pattern particularly clear. Among the six early-deactivated dimen-
sions, every post-deactivation observation remains close to or above its final active score. Several capabilities continue
to improve despite receiving no further direct process-level credit:Switch Strategiesrises from 0.62 to 1.00,State
Benefitsfrom 0.84 to 0.98, andAddress Concerns with New Optionsfrom 0.80 to 0.90. The later-deactivatedAdapt to
New Informationis similarly stable.
These results show that, on the fixed diagnostic set, shifting reward emphasis toward newly relevant capabilities
does not systematically erase capabilities emphasized at earlier stages. The adaptive reward therefore behaves as a
reallocation of training credit rather than requiring previously learned capabilities to be continually reinforced.
23
