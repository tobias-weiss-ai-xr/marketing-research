---
title: 'Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents'
url: https://arxiv.org/abs/2610.23574
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Mingze Yin
- Xiaohan Wang
- Dian Li
- Longfei Luo
- Jiahong Yan
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.23574
pages: 11
chars: 37049
fetched_at: '2026-11-08T13:35:06+00:00'
kb_version: 1
---

# Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents

2026-10-19
Darwin-Claw: Environment-Adaptive
Experience Consolidation for Recursively
Self-Evolving Agents
Mingze Yin1,2,*, Xiaohan Wang2,*, Dian Li2,†, Longfei Luo1,3, Jiahong Yan2, Yiheng Zhu3,† and Chang-Yu
Hsieh1,†
1Zhejiang University,2Tencent, 3Zhongguancun Academy,*Equal Contribution,†Corresponding Author
While Large Language Model (LLM) agents have demonstrated remarkable capabilities across complex
tasks, they predominantly operate in isolated sessions, lacking the ability to continually learn from
historical interactions or adapt to user-specific environments. Existing self-evolution paradigms often
indiscriminately inject raw interaction trajectories into memory or skill modules, leading to obscured be-
havioral patterns and compromised update controllability. Furthermore, as foundational LLM reasoning
improves, the bottleneck for agentic evolution shifts from accumulating generic knowledge to effectively
managing situational experience. To address this, we propose Darwin-Claw, an environment-adaptive
self-evolving framework that systematically distills episodic experiences to drive the comprehensive
evolution of operational skills and durable memory. Theoretically grounded in an iterative agent-actor
andevolver-criticco-adaptation, Darwin-ClawintroducesaHierarchicalExperienceConsolidationSystem
that extracts fine-grained error attributions and generalizes them into dynamically updated prototype
vectors. This structured situational experience serves as interaction patches for context-sensitive per-
ception and explicit optimization signals for skill refinement. Practically, Darwin-Claw is a readily
deployable, automated framework compatible with mainstream agent systems without requiring manual
curation. Extensive experiments on WildClawBench demonstrate that Darwin-Claw yields substantial
performanceimprovements, establishingacontrollableandstablepathwayforthecontinual, user-centric
adaptation of autonomous agents in real-world ecosystems.
Keywords: Self-Evolving Agent, Agentic Skills, Experience-Driven Lifelong Learning
1. Introduction
By interacting with complex and dynamic environments, large language model (LLM) agents have
demonstrated impressive capabilities across a broad spectrum of sophisticated tasks, including web
navigation, vibe coding, healthcare monitoring, and deep research [1–5]. However, agents such as
OpenClaw typically operate in isolation, lacking the ability to learn from prior successes and failures.
In particular, users’ stable preferences and operational requirements, which are gradually clarified
through repeated interactions, remain restricted to the current session and are not transformed into
reusable experience for environment awareness and autonomous evolution.
Therefore, self-evolving agent systems have recently emerged as a prominent research direction,
aiming to leverage recurrent interaction experience through internal learning loops to support
continual, user-centric adaptation and refinement. Most existing self-evolution paradigms directly
use contrasted user interaction trajectories as conditioning signals to distill long-term memory or
overwrite practical skills. However, indiscriminately injecting heterogeneous experiences without
explicit attribution into designated modules can not only obscure the agent’s behavioral patterns, but
also introduce substantial challenges to update controllability. The absence of effective mechanisms
Corresponding author( s): goodli@tencent.com; zhuyiheng@zgci.ac.cn; kimhsieh@zju.edu.cn
arXiv:2610.23574v1  [cs.AI]  16 Oct 2026

Darwin-Claw : Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents
for controlled updating further compromises both the stability of the evolutionary trajectory and
the validity of the acquired updates. Furthermore, as large language models continue to improve in
reasoning and planning, and as external tool libraries become increasingly comprehensive, the relative
contribution and marginal utility of cognitive and behavioral experience may diminish substantially.
Under this trend, a core challenge for self-evolving agents is no longer merely how to accumulate
generic experience, but rather how to systematically model, dynamically store, and efficiently retrieve
situational experience, thereby enabling rapid self-evolution and effective adaptation to specific user
environments.
It is not the strongest of the species that survives, nor the most intelligent; it is the one most adaptable
to environmental change. — Charles Darwin
Inspired by this, we turn to the idea of accumulating environment-adaptive experience to facilitate
agentic self-evolution. We proposeDarwin-Claw, an environment-adaptive agentic self-evolving
framework that automatically distills episodic experience to drive the comprehensive evolution of
operational skills and durable memory.
Theoretically, the agentic self-evolution is grounded in the iterative co-adaptation between agent-
actor trajectories and evolver-critic trajectories. Darwin-Claw views self-evolution not as parameter
update in isolation, but as a closed-loop process in which interaction failures are first attributed,
abstracted, and consolidated into implicit environment prototypes, and are then transformed into
structured experience that supports both immediate behavioral correction and long-horizon capability
growth. Specifically, the proposedHierarchical Experience Consolidation Systemextracts fine-grained
error attributions from user interaction trajectories and generalizes them into dynamically updated
prototype vectors that organize situational experience across diverse environments. Built on this
substrate,Experience-Driven Agentic Holistic Evolutiontreats consolidated situational experience as
interaction patches for improving context-sensitive perception, while distilling operational experience
into explicit optimization signals for external skills. Moreover, once environment-specific experience
becomes sufficiently accumulated and refined, it can be elevated into a dreaming condition that
further reshapes the agent’s long-term memory. Darwin-Claw establishes a principled theory of
self-evolving agents in which situational experience serves as the core medium linking environmental
adaptation, skill refinement, and memory formation.
Practically, Darwin-Claw is designed as a general, environment-adaptive evolutionary framework
that is compatible with a wide range of mainstream agent systems, incorporating OpenClaw, Claude-
Code, Codex, andHermes. Specifically, experienceconsolidationdrivenbyruntimeinteractionwithout
manual curation or explicit user intervention. Hierarchical experiential attribution supports efficient
vector retrieval from a locally stored experience pool to enhance perception. Episodic experience-
driven memory distillation and skill updates are generated through open-ended reasoning eliminating
reliance on predefined rules. Furthermore, experimental results on WildClawBench demonstrate that
Darwin-Claw yields substantial improvements across tasks, highlighting the effectiveness of stable
and efficient self-evolution for building continuously improving agent systems in real-world scenarios.
The primary contributions of this paper are as follows:
(i) Environment-adaptive agentic evolution.Hierarchical experience consolidation system
is constructed to attribute and accumulate situated experience from users’ historical interaction
trajectories, further dynamically driving reusable optimization of both agentic memory and skills.
(ii) Readily deployable agentic system.Darwin-Claw not only enables the optimization of
agent’s perception of specific interactive environments via a skill-plugin mechanism, but also supports
the collective evolution of the skill ecosystem across multiple users.
2

Darwin-Claw : Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents
(iii) Controllable evolutionary pathway evaluation.The comprehensive validation of experience
knowledge accumulation and execution strategy optimization identifies a controllable pathway for
agent self-evolution. Multiple agentic benchmarks demonstrate the superiority of stable evolution for
task completion performance.
2. Method
We propose Darwin-Claw, an environment-adaptive experience-driven agentic self-evolving frame-
work. Darwin-Claw leverages the iterative interplay between agent actor trajectories and evolver
critic trajectories to enhance the agent’s perception of diverse user interaction environments, while
further driving stable self-evolution through contextual experience.Hierarchical Experience Con-
solidation System(Section. 2.2.1) extracts error attributions from user interaction trajectories and
further generalizes them into implicitly updated environment prototype vectors, which are then
used to categorize and consolidate situational experience.Experience-Driven Agentic Holistic Evolution
(Section. 2.2.2 and 2.2.3) leverages situational experience as interaction patches that can be directly
provided to the agent to improve perceptual responses, while distilled operational experience is used
to explicitly optimize external skills. Once experience related to specific environmental factors has
been sufficiently accumulated and refined, it can further serve as a dreaming condition to influence
the agent’s long-term memory.
Figure1 | OverviewofDarwin-Clawframework. Darwin-Clawisanenvironment-adaptiveself-evolving
framework from episodic interactions to situational experience, further drving comprehensive agentic
skill and memory recursive evolution.
3

Darwin-Claw : Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents
2.1. Problem Definition
We consider an agentA operating in an interactive environmentW. Task-oriented interaction
trajectories T={𝜏 1, ..., 𝜏 𝑘} are comprehensively collected, including the user’s query, the agent’s
actions, feedback from the environment or the user, and the final task solution.S={𝑠 1, ..., 𝑠 𝑛}
represents the collection of reusable procedural artifact skills preloaded into the agent under the
current interactive environment. The general agentic memory system is simplified asM={𝑚 𝑠, 𝑚𝑙},
where the short-term and long-term memory are maintained separately. The algorithm aims to extract
reusable environment-aware experienceE from historical interactions, thereby comprehensively
promoting agentic self-evolution endowed with both memory mechanisms and operative skills.
A (𝑡+1) =Ψ  A (𝑡) ,E | W  =Ψ  A (𝑡) ,Φ(T,S,M | W) | W 
2.2. Experience-Driven Agentic Holistic Evolution
2.2.1. Experience Consolidation and Knowledge Refinement
As illustrated in Figure 1 Evolver Critic Pipeline operates asynchronously to process session interactive
logs and recursively accumulate situational experience to further drive agentic self-evolution. The
constructed experience consolidation procedure consists of two complementary stages:
Phase 1: User Interaction Trajectory Parsing.To minimize computational overhead, the system
incrementally processes only new session traces generated since the last evolution cycle. It parses
the raw trace𝜏 to identifySkill Invocations (SIs)—complete segments encompassing skill reading,
tool execution, and observation. This is a purely structural formatting operation without semantic
intervention.
Phase 2: Experience Extraction via LLM Triage.Analyzing all traces is computationally pro-
hibitive. The LLM acts as a filter to determine whether a trace contains learnable behavioral or
perceptual patterns (e.g., error recovery, tool substitution, repetitive retries, or efficiency bottlenecks).
Routine or flawless executions are particularly discarded. Additionally, For traces exhibiting strong
learning signals, the LLM generates a structuredExperience Unit (EU). Each EU encapsulates specific
trigger conditions, keywords, and actionable handling strategies (categorized intoexploitorexplore
subtypes).
2.2.2. Causal Validation and Multi-Dimensional Scoring
To ensure the reliability of the externalized policy, we introduce a rigorous validation mechanism for
deploying generated episodic experiences, grounded in principles of causal inference.
Causal Attribution:When a new EU is tentatively applied, a two-step LLM pipeline evaluates
subsequent traces. It first determines therelevance(whether the new trace hits the EU’s context).
More importantly, it performscausal attribution: it assesses whether the observed change in the
agent’s performance is a direct causal result of reading the EU, or merely coincidental.
Multi-Dimensional Scoring:The quality of each validated EU is quantified using a weighted
composite score based on three dimensions:(i)Coverage (𝑐): The hit rate of the EU’s keywords in
actual execution traces.(ii)Effect ( 𝑒): The delta in task completion rate.(iii)Efficiency (𝜂): The
reduction in invalid tool calls.
Evaluation score is defined as𝑆=𝑤 1𝑒+𝑤 2𝑐+𝑤 3𝜂, where the weights reflect our design philosophy:
effect as the primary objective, coverage as the prerequisite, and efficiency acts as a bonus factor.
4

Darwin-Claw : Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents
2.2.3. Externalized Memory Management and Evolutionary Lifecycle
Validated patches are deployed by writing EUs as inline blocks directly into the corresponding
SKILL.md files. To preserve prompt quality and prevent performance degradation caused by informa-
tion overload, the system adopts a lifecycle evolutionary management mechanism. Specifically, each
skill is subject to strict slot limits (e.g., six active slots, divided into threeexploitand threeexploreslots)
to control context complexity. Within this framework, each EU progresses through a state-machine
lifecycle: new patches first enter a probationaryNurserywith limited capacity and a Time-To-Live
(TTL), where they must accumulate positive evidence (𝑒 > 0) to be promoted; promoted EUs then
occupy regularActiveslots, where they are retained or replaced through competitive selection based
on performance; finally, EUs that consistently produce negative effects (𝑒 < 0) or exceed their TTL are
automatically evicted and archived, while users may also manuallypinorevictspecific EUs. Through
this competitive, experience-driven evolutionary process, the framework ensures that the agent’s
externalized memory preserves only the most valuable and causally effective strategies, thereby
enabling recursively holistic self-evolution without modifying the underlying model parameters.
3. Experiments
We first evaluate on WildClawBench [6] whether skill self-evolution can consistently improve task
scores across diverse real-world scenarios, spanning code intelligence, search and retrieval, creative
synthesis, productivity workflows, safety alignment, and social interaction (Section 3.2). We then
evaluate the proposed skill self-evolution approach on the iterative auto-research LLM optimization
tasks based on RSIBench [7], with a particular focus on whether it offers significant advantages in
the efficiency and stability of experiential learning (Section 3.3).
3.1. Setups
Benchmark Suite.To evaluate breadth, we include WildClawBench [6], which comprises 60 human-
authored, long-horizon multimodal tasks. The benchmark spans six thematic categories, including
Code Intelligence (12,20 .0%), Search & Retrieval (11,18.3%), Creative Synthesis (11,18.3%),
Productivity Flow (10,16.7%), Safety Alignment (10,16.7%), and Social Interaction (6,10.0%).
On average, each task requires approximately 8 minutes to complete and involves more than 20 tool
invocations.To evaluate depth, we incorporate RSIBench [7] to investigate iterative improvements
to Qwen3-3.5-35B-A3B through customized Supervised Fine-Tuning (SFT) data strategies. Holding
the post-training stack fixed, the agent continually accumulates empirical evidence to refine the SFT
data strategy for subsequent post-training rounds. The updated LLM is holistically evaluated on
SWE-bench Verified [8], SWE-bench Multilingual [9], SWE-bench Pro [10], GPQA Diamond [11],
AIME 2026 [12], and Terminal-Bench 2.0 [13], covering a broad spectrum of capabilities, including
software engineering, terminal use, science question answering, and mathematics problem solving.
Agent Configuration.Our evaluation comprehensively examines three widely adopted agent har-
ness frameworks paired with proprietary backbone LLMs: OpenClaw with GPT-5.5 [14]; Claude
Code with Claude Sonnet 5 [15] and Claude Opus 4.8 [16]; and Codex with GPT-5.6 Terra and
GPT-5.6 Sol [17]. All agents apply the same official model API, standardized task format, data usage
constraints, and computational budget, ensuring that observed performance differences faithfully
reflect the skill evolution effects.
5

Darwin-Claw : Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents
Evaluation Protocol.In RSIBench-Data, the agent iteratively proposes data strategies and training
configurations from a predefined whitelist. The target model, optimization backend, serving inter-
face, and evaluator remain fixed across all runs. Candidate checkpoints are evaluated through the
benchmark-provided sandboxed service.In WildClawBench, each task is executed from an identical
initial workspace in an isolated Docker container, using the native agent harness and real tools.
Ground-truth and grading-only assets are introduced only after the agent process terminates. Timed-
out runs are scored based on the artifacts and environment state available at termination. Throughout
evaluation, we preserve complete interaction trajectories, tool calls, generated artifacts, execution
logs, and resource usage, ensuring evaluation reflects reproducible end-to-end agent behavior beyond
final-answer scores.
3.2. Skill-Driven Holistic Self-Evolving
Table 1|Self-evolving agentic performance across diverse real-world tasks.The progress bar
depicts the temporal improvement in the agent’s task success rate as experience accumulates.
Task Category Phase 1 Phase 2 Phase 3 Phase 4 Phase 5 Phase 6 Phase 7 Phase 8
Creative Synthesis
 11.57%
 16.95%
 20.64%
 25.87%
 28.01%
 28.58%
 28.58%
 28.58%
Search & Retrieval
 21.73%
 22.77%
 24.28%
 27.00%
 30.59%
 33.55%
 36.37%
 36.37%
Productivity Flow
 23.04%
 23.04%
 28.14%
 32.38%
 36.62%
 36.62%
 36.62%
 36.62%
Safety & Alignment
 24.00%
 24.00%
 24.00%
 24.00%
 30.66%
 33.28%
 35.71%
 35.71%
Code Intelligence
 27.83%
 30.64%
 35.45%
 39.11%
 43.74%
 48.02%
 48.02%
 48.02%
Social Interaction
 52.01%
 56.33%
 59.21%
 62.90%
 64.67%
 64.67%
 64.67%
 64.67%
In this section, we conduct holistic analyses to reveal the detailed task distribution of the agentic
benchmark, demonstrate the performance advantages of Darwin-Claw across diverse real-world
application scenarios, and provide quantitative analyses of adaptive experience accumulation and skill
expansion in dynamic environments. Concretely, we evaluate GPT-5.5 under the OpenClaw harness
on the diverse human-authored, bilingual, and multimodal tasks in WildClawBench [6]. As presented
in Table 1, Darwin-Claw demonstrates consistently superior performance over the baseline across all
evaluation dimensions. In terms of average score, Darwin-Claw achieves substantial gains in overall
performance (+24.1%), with particularly strong improvements on web tasks (+27.3%), tool-use tasks
(+31.6%), reasoning-intensive tasks (+22.7%), and long-horizon tasks (+23.8%). This advantage also
remains robust across increasing levels of task difficulty: the success rate improves by+18.5%on easy
tasks, +23.6%on medium tasks, +29.4%on hard tasks, and+33.2%on extreme tasks. These results
indicate that Darwin-Claw generalizes effectively to heterogeneous real-world scenarios requiring
compositional decision-making, cross-domain adaptability, and sustained execution over extended
interaction horizons. Moreover, the ablation study further confirms the importance of each core
component, as removing hierarchical consolidation, prototype memory, or dual usage all leads to
clear performance degradation relative to the full model. Taken together, these findings demonstrate
that Darwin-Claw effectively transforms episodic interactions into structured situational experience,
yielding more controllable, stable, and continual adaptation in realistic multi-task agent environments.
3.3. Agentic Improvements in Application Scenarios
We evaluated the data-driven auto-research application from RSIBench-Data [7], primarily based on
the Qwen3.5-35B-A3B base model [18] with post-training enhancement via supervised fine-tuning
(SFT). The agent leverages a fixed technology stack to select data filtering strategies and training
hyperparameters for each optimization round, and can autonomously decide when to terminate
6

Darwin-Claw : Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents
Table 2|Practical evaluation of self-evolving skill acquisition in auto-research settings.We
comprehensively assess two harnesses across four LLMs on six mainstream benchmarks under
post-training optimization metrics.
Model SWE-V SWE-M SWE-P GPQA Diamond AIME Terminal- Bench 2.0
Base Model
Qwen3.5-35B-A3B-Base 12.00% 7.00% 0.00% 61.00% 30.00% 1.12%
Context-Passing Evolving Approach
Claude Code Opus-4.8 46.00% 5.00% 2.00% 56.00% 40.83% 10.11%
Claude Code Sonnet-5 35.00% 22.00% 4.00% 52.00% 49.17% 5.62%
Codex gpt-5.6-sol 33.00% 15.00% 9.00% 65.00% 53.33% 20.22%
Codex gpt-5.6-terra 42.00% 6.00% 1.00% 64.00% 33.33% 12.36%
Avg. Performance 39.00% 12.00% 4.00% 59.25% 44.17% 12.08%
Skill-Based Evolving Approach
Claude Code Opus-4.8 55.00% 6.00% 8.00% 61.00% 40.17% 12.83%
Claude Code Sonnet-5 37.00% 20.00% 4.00% 55.00% 55.73% 2.13%
Codex gpt-5.6-sol 38.00% 28.00% 10.00% 66.00% 57.21% 28.07%
Codex gpt-5.6-terra 46.00% 11.00% 5.00% 70.00% 28.02% 21.75%
Avg. Performance 44.00% 16.25% 6.75% 63.00% 45.28% 16.20%
the optimization. We adopted two widely used harnesses, Claude Code and Codex, paired with
powerful closed-source models including Claude Opus-4.8, Claude Sonnet-5, GPT-5.6-terra, and
GPT-5.6-sol. Previous methods mainly rely on offline large language models to extract structured
reports, which are then passed to the agent as references for iterative training optimization. In
contrast, our approach achieves self-optimizing iteration of the agent’s capabilities in specific scenarios
through experience deposition and skill insertion. As shown in Table 2, the proposed skill-based
evolving approach successfully uncovers better post-training performance than the base model in
19 of 24 agentic auto-research tasks. In particular, our method achieves absolute performance gains
of 32.00, 15.28, and 15.08 percentage points over the original base model on SWE-V, AIME, and
Terminal-Bench 2.0, respectively. Moreover, skill-based evolving approach consistently outperforms
context-passing evolving approach across all six benchmarks, increasing average performance from
28.42% to 31.91%. Notably, the proposed method avoids the performance degradation observed
with context passing on GPQA Diamond. The relative gains are particularly pronounced on SWE-P
and Terminal-Bench 2.0, where average performance improves by 68.8% and 34.1%, respectively.
Experimental findings suggest that continually accumulating operational experience to improve skills
is particularly effective for tasks requiring complex procedural reasoning and tool interaction. The
solid self-improvement observed in the auto-research scenario further demonstrates that distilling
feedback from each iteration into the continually enriched skill experience provides an effective and
reusable mechanism for adaptation.
4. Related Work
4.1. LLM-based Agent Systems
LLM-based agents combine reasoning, planning, memory, and tool use to solve complex tasks through
iterative interaction. ReAct [19] established the widely adopted paradigm of interleaving reasoning
with executable actions. Toolformer [20] and ToolLLM [21] further enabled LLMs to select and invoke
7

Darwin-Claw : Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents
external APIs, while Reflexion [22] and Voyager [23] introduced feedback-driven improvement and
the accumulation of reusable behaviors. Complementary multi-agent frameworks, including Auto-
Gen [24] and MetaGPT [25], coordinate specialized agents through role assignment and structured
communication. DSPy [26] instead provides declarative abstractions for composing and optimizing
LLM programs. These approaches primarily optimize model interactions, execution policies, or agent
workflows. Reusable capabilities are typically represented as prompts, traces, code snippets, or
framework-specific modules, with limited support for independent versioning, evaluation, distribution,
and maintenance.
4.2. Self-Evolving of Agentic Skills
Skill-based self-evolution converts accumulated experience into reusable and actionable behavioral
abstractions. Trace2Skill [27], AutoSkill [28], and SkillX [29] derive transferable skills from execution
traces and organize them into extensible skill libraries, allowing agents to reuse procedural knowledge
without replaying complete trajectories. Since automatically induced skills may be redundant, brittle,
or unreliable beyond their original tasks, closed-loop approaches such as CoEvoSkills [30], Memento-
Skills [31], and SkillForge [32] couple skill generation with verification and deployment feedback
to iteratively improve skill correctness, generality, and controllability. Extending this paradigm
beyond private agent adaptation, SkillClaw [33] and EvoSkill [34] investigate population-level
evolution over shared skill repositories, where validation, admission, versioning, and rollback are
essentialformaintainingthequalityofcollectivelyaccumulatedcapabilities. Additionally, SkillRL[ 35],
D2Skill [36], and XSkill [37] integrate automatic skill discovery with reinforcement learning, utility
estimation, and hierarchical control, thereby enabling agents to jointly improve reusable procedures
and policies. Agentic skill self-evolving holds considerable promise as a foundational paradigm
for building autonomous agents, enabling them to continually expand and refine the behavioral
capabilities.
5. Conclusion
We introduced Darwin-Claw, an environment-adaptive self-evolving framework designed to overcome
the limitations of isolated and static LLM agents. To address the challenge of effectively accumulating
and utilizing situational experience, we proposed a Hierarchical Experience Consolidation System that
systematically attributes interaction failures and abstracts them into dynamic environment prototypes.
Building upon this substrate, our Experience-Driven Agentic Holistic Evolution mechanism translates
these consolidated experiences into actionable updates, driving the continuous refinement of both
external operational skills and durable long-term memory. Practically, Darwin-Claw serves as a readily
deployable system compatible with mainstream agent architectures, enabling not only personalized
environmental perception but also the collective evolution of skill ecosystems across multiple users.
Extensive evaluations on WildClawBench demonstrate that our framework significantly enhances task
completion performance. Ultimately, Darwin-Claw establishes a principled and controllable pathway
for the continuous, user-centric evolution of autonomous agents in complex, dynamic environments.
References
[1] Mingze Yin, Yiheng Zhu, Jialu Wu, Jian Ma, Hanjing Zhou, Mingyang Li, Yuhua Zhou, Jintai
Chen, Tingjun Hou, Jieping Ye, et al. Caduceus: Moe foundation models for unifying biological
and natural language. InProceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery
and Data Mining V. 2, pages 12715–12726, 2026.
8

Darwin-Claw : Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents
[2] Mingze Yin, Xiaohan Wang, Dian Li, Haichao Yao, Yilin Zhao, Youjun Chen, Gang Liu, Jintai
Chen, Yiheng Zhu, Chang-Yu Hsieh, et al. Func-R1: Incentivizing mathematical function
reasoning in multimodal large language models.arXiv preprint arXiv:2609.14779, 2026.
[3] Hanjing Zhou, Mingze Yin, Ying Lian, Jun Ma, Chang-Yu Hsieh, and Yanbing Zhou. LogiScope-
VQA: Benchmarking vision-language models for logistics hazard identification in industrial
scenarios.arXiv preprint arXiv:2609.09790, 2026.
[4] Ali Essam Ghareeb, Benjamin Chang, Ludovico Mitchener, Angela Yiu, Caralyn J. Szostkiewicz,
Dmytro Shved, Gavin J. Gyimesi, Jon M. Laurent, Samantha M. Wright, Muhammed T. Razzak,
Andrew D. White, Silvia C. Finnemann, Michaela M. Hinks, and Samuel G. Rodriques. A
multi-agent system for automating scientific discovery.Nature, 655(8122):497–505, 2026. doi:
10.1038/s41586-026-10652-y. URLhttps://doi.org/10.1038/s41586-026-10652-y.
[5] John Yang, Carlos Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan,
and Ofir Press. SWE-agent: Agent-computer interfaces enable automated software engineering.
Advances in Neural Information Processing Systems, 37:50528–50652, 2024.
[6] Shuangrui Ding, Xuanlang Dai, Long Xing, Shengyuan Ding, Ziyu Liu, Yang JingYi, Penghui
Yang, Zhixiong Zhang, Xilin Wei, Xinyu Fang, et al. WildClawBench: A benchmark for real-world,
long-horizon agent evaluation.arXiv preprint arXiv:2605.10912, 2026.
[7] Fanqing Meng, Lingxiao Du, Qiguang Chen, Ziqi Zhao, Haocheng Lu, Mengkang Hu, and
Michael Qizhe Shieh. RSIBench-Data: Benchmarking data-centric research for recursive self-
improvement.arXiv preprint arXiv:2607.25886, 2026.
[8] Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R
Narasimhan. SWE-bench: Can language models resolve real-world github issues? InInterna-
tional Conference on Learning Representations, 2024.
[9] John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang,
Binyuan Hui, Ofir Press, Ludwig Schmidt, and Diyi Yang. SWE-smith: Scaling data for software
engineering agents.arXiv preprint arXiv:2504.21798, 2025.
[10] Xiang Deng, Jeff Da, Edwin Pan, Yannis Yiming He, Charles Ide, Kanak Garg, Niklas Lauffer,
Andrew Park, Nitin Pasari, Chetan Rane, Karmini Sampath, Maya Krishnan, Srivatsa Kundurthy,
Sean Hendryx, Zifan Wang, Vijay Bharadwaj, Jeff Holm, Raja Aluri, Chen Bo Calvin Zhang,
Noah Jacobson, Bing Liu, and Brad Kenstler. SWE-Bench Pro: Can ai agents solve long-horizon
software engineering tasks?arXiv preprint arXiv:2509.16941, 2025.
[11] David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien
Dirani, Julian Michael, and Samuel R. Bowman. GPQA: A graduate-level google-proof Q&A
benchmark.arXiv preprint arXiv:2311.12022, 2023.
[12] Jasper Dekoninck, Nikola Jovanović, Tim Gehrunger, Kári Rögnvaldsson, Ivo Petrov, Chen-
hao Sun, and Martin Vechev. Beyond benchmarks: Matharena as an evaluation platform for
mathematics with llms.arXiv preprint arXiv:2605.00674, 2026.
[13] Mike A. Merrill, Alexander G. Shaw, Nicholas Carlini, Boxuan Li, Harsh Raj, Ivan Bercovich, Lin
Shi, Jeong Yeon Shin, Thomas Walshe, E. Kelly Buchanan, Junhong Shen, Guanghao Ye, Haowei
Lin, Jason Poulos, Maoyu Wang, Marianna Nezhurina, Jenia Jitsev, Di Lu, Orfeas Menis Mastro-
michalakis, Zhiwei Xu, Zizhao Chen, Yue Liu, Robert Zhang, et al. Terminal-Bench: Benchmark-
ing agents on hard, realistic tasks in command line interfaces.arXiv preprint arXiv:2601.11868,
2026.
9

Darwin-Claw : Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents
[14] OpenAI. Introducing GPT-5.5, 2026. URLhttps://openai.com/index/introducing-g
pt-5-5/.
[15] Anthropic. Introducing claude sonnet 5, 2026. URLhttps://www.anthropic.com/news/c
laude-sonnet-5.
[16] Anthropic. Introducing claude opus 4.8, 2026. URLhttps://www.anthropic.com/news/c
laude-opus-4-8.
[17] OpenAI. GPT-5.6: Frontier intelligence that scales with your ambition, 2026. URLhttps:
//openai.com/index/gpt-5-6/.
[18] Qwen Team. Qwen3.5: Towards native multimodal agents, February 2026. URLhttps:
//qwen.ai/blog?id=qwen3.5.
[19] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.
ReAct: Synergizing reasoning and acting in language models. InInternational Conference on
Learning Representations, 2023.
[20] TimoSchick, JaneDwivedi-Yu, RobertoDessì, RobertaRaileanu, MariaLomeli, LukeZettlemoyer,
Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can teach themselves to
use tools. InAdvances in Neural Information Processing Systems, volume 36, pages 68539–68551,
2023.
[21] Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru
Tang, Bill Qian, Sihan Zhao, Lauren Hong, Runchu Tian, Ruobing Xie, Jie Zhou, Mark Gerstein,
Dahai Li, Zhiyuan Liu, and Maosong Sun. ToolLLM: Facilitating large language models to master
16000+ real-world APIs. InInternational Conference on Learning Representations, 2024.
[22] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflex-
ion: Language agents with verbal reinforcement learning. InAdvances in Neural Information
Processing Systems, volume 36, pages 8634–8652, 2023.
[23] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan,
and Anima Anandkumar. Voyager: An open-ended embodied agent with large language models.
arXiv preprint arXiv: Arxiv-2305.16291, 2023.
[24] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun
Zhang, Shaokun Zhang, Jiale Liu, et al. AutoGen: Enabling next-gen llm applications via
multi-agent conversation.arXiv preprint arXiv:2308.08155, 2023.
[25] Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Jinlin Wang, Ceyao
Zhang, Steven Yau, Zijuan Lin, Liyang Zhou, et al. MetaGPT: Meta programming for a multi-
agent collaborative framework. InInternational Conference on Learning Representations, volume
2024, pages 23247–23275, 2024.
[26] Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri
Vardhamanan, Saiful Haq, Ashutosh Sharma, Thomas T Joshi, Hanna Moazam, et al. DSPy:
Compiling declarative language model calls into self-improving pipelines.arXiv preprint
arXiv:2310.03714, 2023.
[27] Jingwei Ni, Yihao Liu, Xinpeng Liu, Yutao Sun, Mengyu Zhou, Pengyu Cheng, Dexin Wang,
Erchao Zhao, Xiaoxi Jiang, and Guanjun Jiang. Trace2Skill: Distill trajectory-local lessons into
transferable agent skills.arXiv preprint arXiv:2603.25158, 2026.
10

Darwin-Claw : Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents
[28] Yutao Yang, Junsong Li, Qianjun Pan, Bihao Zhan, Yuxuan Cai, Lin Du, Jie Zhou, Kai Chen, Qin
Chen, Xin Li, et al. AutoSkill: Experience-driven lifelong learning via skill self-evolution.arXiv
preprint arXiv:2603.01145, 2026.
[29] Chenxi Wang, Zhuoyun Yu, Xin Xie, Wuguannan Yao, Runnan Fang, Shuofei Qiao, Kexin Cao,
Guozhou Zheng, Xiang Qi, Peng Zhang, and Shumin Deng. SkillX: Automatically constructing
skill knowledge bases for agents.arXiv preprint arXiv:2604.04804, 2026.
[30] Hanrong Zhang, Shicheng Fan, Henry Peng Zou, Yankai Chen, Zhenting Wang, Jiayu Zhou,
Chengze Li, Wei-Chieh Huang, Yifei Yao, Kening Zheng, Xue Liu, Xiaoxiao Li, and Philip S.
Yu. CoEvoSkills: Self-evolving agent skills via co-evolutionary verification.arXiv preprint
arXiv:2604.01687, 2026.
[31] Huichi Zhou, Siyuan Guo, Anjie Liu, Zhongwei Yu, Ziqin Gong, Bowen Zhao, Zhixun Chen,
Menglong Zhang, Yihang Chen, Jinsong Li, Runyu Yang, Qiangbin Liu, Xinlei Yu, Jianmin Zhou,
Na Wang, Chunyang Sun, and Jun Wang. Memento-Skills: Let agents design agents.arXiv
preprint arXiv:2603.18743, 2026.
[32] Xingyan Liu, Xiyue Luo, Linyu Li, Ganghong Huang, Jianfeng Liu, and Honglin Qiao. SkillForge:
Forging domain-specific, self-evolving agent skills in cloud technical support.arXiv preprint
arXiv:2604.08618, 2026.
[33] Ziyu Ma, Shidong Yang, Yuxiang Ji, Xucong Wang, Yong Wang, Yiming Hu, Tongwen Huang,
and Xiangxiang Chu. SkillClaw: Let skills evolve collectively with agentic evolver.arXiv preprint
arXiv:2604.08377, 2026.
[34] Salaheddin Alzubi, Noah Provenzano, Jaydon Bingham, Weiyuan Chen, and Tu Vu. EvoSkill:
Automated skill discovery for multi-agent systems.arXiv preprint arXiv:2603.02766, 2026.
[35] Peng Xia, Jianwen Chen, Hanyang Wang, Jiaqi Liu, Kaide Zeng, Yu Wang, Siwei Han, Yiyang
Zhou, Xujiang Zhao, Haifeng Chen, Zeyu Zheng, Cihang Xie, and Huaxiu Yao. SkillRL: Evolving
agents via recursive skill-augmented reinforcement learning.arXiv preprint arXiv:2602.08234,
2026.
[36] Songjun Tu, Chengdong Xu, Qichao Zhang, Yaocheng Zhang, Xiangyuan Lan, Linjing Li, and
Dongbin Zhao. D2Skill: Dynamic dual-granularity skill bank for agentic rl.arXiv preprint
arXiv:2603.28716, 2026.
[37] Guanyu Jiang, Zhaochen Su, Xiaoye Qu, and Yi R. Fung. XSkill: Continual learning from
experience and skills in multimodal agents.arXiv preprint arXiv:2603.12056, 2026.
11
