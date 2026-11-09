---
title: LLMs Are Not Good Strategists, Yet Memory-Enhanced Agency Boosts Reasoning
url: https://arxiv.org/abs/2608.12626
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Yi Wu
- Zhimin Hu
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.12626
pages: 14
chars: 48193
fetched_at: '2026-11-08T13:34:56+00:00'
kb_version: 1
---

# LLMs Are Not Good Strategists, Yet Memory-Enhanced Agency Boosts Reasoning

LLMSARENOTGOODSTRATEGISTS, YETMEMORY-
ENHANCEDAGENCYBOOSTSREASONING
Yi Wu ∗
University of Chicago
yiwu@uchicago.edu
Zhimin Hu ∗
University of Wisconsin-Madison
hu436@wisc.edu
ABSTRACT
Strategic reasoning in Large Language Models (LLMs) within long-horizon en-
vironments is often limited by inconsistent subgoals. In these settings, finite at-
tention resources prevent the model from maintaining strategic coherence over
thousands of steps. This limitation leads to strategic drift, where localized deci-
sions fail to sustain a coherent trajectory across reasoning. To address this, we
introduce EpicStar, a framework that enables agents to learn memory as policy to
tackle long-horizon reasoning. Specifically, the agent maintains a bank of success-
ful past episodes as a heuristic alongside a working memory to track short-term
environmental changes. During inference, a dynamic gating mechanism deter-
mines whether to execute a retrieved action directly or to perform new reasoning
through a contextual fusion of the retrieved episodes and current working mem-
ory. Utilizing StarCraft II as the testbed, we evaluated EpicStar against diverse
opponent styles. It significantly outperforms baseline methods, achieving higher
win rates while consuming an order of magnitude fewer tokens, and it maintains
this advantage consistently across difficulty levels and opponent strategies. Our
findings provide compelling evidence that structured cross-episode memory is es-
sential for enabling LLM agents to perform robust, long-term strategic execution
in dynamic, autonomous settings.
1 INTRODUCTION
Strategic reasoning in dynamic and partially observable environments represents a formidable chal-
lenge for Large Language Models (LLMs), where agents must maintain a coherent long-term tra-
jectory while simultaneously adapting to rapid environmental shifts. StarCraft II has long served as
a testbed for such capabilities because it demands the simultaneous coordination of resource man-
agement, technological expansion, and unit control over thousands of time steps. While LLMs have
already achieved human-level reasoning in short-horizon settings (Mondorf & Plank, 2024; Kabra
et al., 2025), their performance often degrades in long-range sequential reasoning tasks. We ar-
gue that the failures are mainly due to the fact that the agent tends to progressively overfit to local
observations and consequently loses sight of its global objectives.
Existing efforts to mitigate these issues either rely on more prompting loops to compress information
(Ma et al., 2024) or introduce more rules to stabilize the reasoning (Shao et al., 2024). In this paper,
we argue that robust strategic reasoning requires a transition from reactive prompting to structured
reuse of past experience (Klein, 2017). We introduce EpicStar, an agentic framework that integrates
episodic retrieval with situational modulation as a policy for reasoning. EpicStar continuously stores
successful gameplay episodes in a structured memory bank. During inference, the agent retrieves
relevant episodes, acting as a strategic heuristic to guide its reasoning. To remain responsive to
new situations, EpicStar maintains a working memory for tracking environmental changes and em-
ploys a dynamic gating mechanism to balance reusing past actions directly with new reasoning for
situational adaptation. Additionally, in situational adaptation, retrieved episodes are fused via a
context-aligned mechanism to provide high-level context and structure for ongoing reasoning.
∗Equal contribution. The author order follows the alphabetical order of first names, and each author reserves
the right to list their name first in their own records. It was published at the ICLR 2025 Workshop on Reasoning
and Planning for LLMs.
1
arXiv:2608.12626v1  [cs.CL]  12 Aug 2026

Memory Cache
• Current Observation
• Observation-Action in
past k steps
Episodic Memory
Gate
(Exploration or
Exploitation)
Contextual
Fusion
If win
Experiential Learning
Actions Observation
Actions
ObservationProposed Actions
Retrieved Actions Agent
EpicStar Agent
Figure 1: Overview of the EpicStar architecture. The agent is composed of distinct memory compo-
nents and their interactions. Episodic memory stores gameplay episodes for retrieval and long-term
learning. On the left blue panel, working memory consists of a short-term cache and gating mech-
anisms that manage exploration and exploitation, balancing coherent planning with dynamic adap-
tation. Contextual fusion enables bidirectional modulation between working memory and episodic
memory, facilitating the integration of immediate context with past strategic knowledge.
We evaluated EpicStar in StarCraft II using TextStarCraft II (Ma et al., 2024) and chose its Chain of
Summarization (CoS) method as our primary baseline, as it shares the most comparable assumptions
and design scope with our method. We focus on level 5 and 6 game difficulties, which roughly cor-
respond to entry-level and above-average human performance and mark the threshold at which CoS
begins to show signs of performance degradation. We found that EpicStar consistently outperforms
CoS across both levels, achieving higher win rates (Table 1) while consuming fewer tokens. Further,
it demonstrates notably improved adaptability under diverse strategic conditions (Figure 2).
In summary, our contributions are threefold: 1) we introduce EpicStar, an LLM-based agentic frame-
work that incorporates structured episodic memory to support long-horizon strategic reasoning.
EpicStar mitigates strategic drift by retrieving and adapting past trajectories to maintain coherence
over time; 2) we propose a situational modulation mechanism that balances prior experience with
real-time context. This includes a dynamic gating module that integrates episodic recall with work-
ing memory, and a contextual fusion step that translates retrieved episodes into strategic guidance;
3) we provide empirical evidence that both episodic and working memory are essential for strategic
performance. Even a small number of high-quality episodic memories leads to marked improve-
ments in win rate and adaptability. Code can be found at https://github.com/ethanyiwu/EpicStar.
2 RELATEDWORK
2.1 GAMEAGENT
The world of LLM-based game agents has been built on several fundamental ideas in agent design:
1) agents can learn from their action failures and reflect on their reasoning (Yao et al., 2022; Shinn
et al., 2024); agents can be equipped with external knowledge (Lewis et al., 2020); agents can learn
to use tools (Schick et al., 2023). These advancements have led to the bloom of developing LLM
agents in more complex game scenarios. To begin with, V oyager (Wang et al., 2023) autonomously
builds a toolkit of procedural skills through executable code in Minecraft. Conversely, PokeLLMon
(Hu et al., 2024) retrieves external knowledge and uses memory for in-game reflection to refine
high-level strategy in Pok´emon. Feng et al. (2023) and Huang et al. (2024) utilize external gameplay
datasets to train a language model to play Chess and Poker.
2

2.2 STARCRAFTII AGENT
Among various games, StarCraft II has been unique in testing long-horizon strategic reasoning.
As a real-time strategic game in partially observable environments, it requires players to reason
under constraints from diverse sources of information and adapt strategies over extensive steps. The
complexity of this domain was first made accessible to agentic research through the PySC2 interface
(DeepMind, 2017), which provides low-level state information and control. This interface fueled the
development of reinforcement learning-based agents like AlphaStar (Vinyals et al., 2019), which
achieved superhuman performance via massive-scale self-play, albeit at a prohibitive computational
cost and with limited generalization. More recently, SwarmBrain (Shao et al., 2024) applied LLMs
to this low-level interface. While it attempted to learn from gameplay through a log of semantic
descriptions of strategies used, its learning is fundamentally oriented towards low-level control and
lacks contextual richness.
Afterwards, the TextStarCraft II interface (Ma et al., 2024) was introduced, moving away from
micro-management and re-framing the game as a high-level strategic challenge. Our work is sit-
uated within this paradigm. Its CoS method serves as a strong baseline, using its sliding-window
summary as a working memory to distill complex, high-dimensional state information into a concise,
actionable representation. However, a clear gap remains: no existing agent for high-level strategic
reasoning like StarCraft II learns from its own gameplay experience in a structured manner.
3 REASONING WITHMEMORY
3.1 TASKFORMULATION
Strategic reasoning within StarCraft II can be conceptualized as a sequential decision-making pro-
cess characterized by the tuple(S, A, T, R, Z, O).Srepresents the actual state space of the world,
whereS={s 1, s2, . . . , sN }is the set of all possible states the system can be in.Arepresents
the action space, andA={a 1, a2, . . . , aM }is the set of actions the agent can take. In partially
observable environments, the agent has access to an observation spaceO={o 1, o2, . . . , oK}.T
acts as the state transition functionT(s ′ |s, a) =P(s ′ |s, a)andZis the observation function,
Z(o|s ′, a), represents the probability of receiving observationoafter the agent takes actionaand
transitions to states ′. In this framework, the agent does not receive a direct rewardR(s, a)but rather
observes the outcome of the game - either a win or a loss. Unlike traditional reinforcement learning,
we do not directly estimate theTandZ, instead, we rely on LLM reasoning coupled with memory
mechanisms to maximize the expected accumulated reward.
Algorithm 1Working Memory Exploration and Exploitation -W(·)
Require:Exploration Cool Down Framed e, Queue Pop Cool Down Framed q, Action Sizen,
Current Game Timet, Last Time to Explorel e, Last Time to Pop Queuel q
1:(e 1, . . . , en)←Re EC (t, ot)▷Retrievenepisodes
2:a t ←ExtractAction((e 1, . . . , en))▷Select the first action
3:ift≥d e +l e then
4:l e ←t
5:o ′ t =o t ×Q o(t)
6:(a 1, . . . , an)←LLM(S,(o ′ t))▷Proposenexploration actions
7:Q a.push((a1, . . . , an))
8:end if
9:ifa t =EmptyActionandQ a.size()>0andt≥l q +d q then
10:l q =t
11:a t ←Q a.pop()▷Add the exploration action
12:end if
13:t←t+ 1
14:returna t
3

3.2 RETRIEVAL FROMEPISODICMEMORY
Given a set of gameplay data, we define a series of episodes{(t i, oi, ai)|i= 1,2, . . . , e}, where
ti represents the time in the game. The episodic memory, denoted asM EC (t, o, a), consists of
episodes corresponding to victory games.
For each moment(t, o)in a new game, we identify similar past moments by finding indices of
episodesD index that closely match the current scenario fromM EC . Initially, we searchM EC
aroundtto retrieve a subset:
M EC t = BinarySearch(MEC , t, t∆)(1)
wheret ∆ is a predefined parameter representing a time range aroundtfor the search (we sett ∆ = 0
for simplicity). Next, we compute the differences between the current observationot and all previous
observationsO ′ ∈M EC t, with each observationo t represented as a Python dictionary (with a unit
as the key and a scalar value). We calculate two metrics: (1) the number of items that changed,
denoted asD item; and (2) the number of values that changed, denoted asD value. We then obtain
the topnmemories based on the following criteria:
Dindex = Argsort(αMinMax(Ditem)
+βMinMax(D value)) (2)
where we perform min-max normalization on bothD item andD value, then sortDin ascending
order. We setn= 3, α= 0.5, β= 0.5
Thus, the retrieval function is defined as:
ReEC (t, o) =



n
EmptyAction
o
,if|M EC t|= 0n
M EC t(ti, oi, ai)|i∈D index[:n] o ,
otherwise
(3)
3.3 WORKINGMEMORY ANDGATINGMECHANISM
For every time stept, the observation queue,Q o, captures recentk max observations. Inspired by
frame skipping (Braylan et al., 2015), the working memory recalls the past observations by a frame
interval ofL:
Qo(t) ={(ot−k)|k=L,2L, . . . , kmaxL}(4)
whereo t−k represents observation at timet−k. Before reasoning, we map the observationo t to an
augmented observation space defined as:o ′ t =o t ×Q o(t). We setk max = 4andL= 24.
We define the combination of the vanilla system prompt and contextual fusion as semantic knowl-
edgeSand the querying of the LLM as the functionLLM(·). We then engage in the exploration
and exploitation process denoted asW(·)and initiate it with an exploration action queue,Q a, as
outlined in Algorithm 1.
InW(·),Q o(t)provides short-term historical information that allows the agent to analyze the state’s
tendency. In contrast,Q a stores actions for future interpolation into action sequences retrieved from
episodic memory, enabling adaptive planning.
3.4 CONTEXTUALFUSION
To make a fair comparison, we adapt the task instruction prompts from CoS methods (Ma et al.,
2024) as a backbone. Additionally, we incorporate contextual fusion to connect the information
between working memory and episodic memory to the prompts. Specifically: 1) We augment the
prompt with additional instructions that encourage the retrieved actions to be executable within the
current scenario. This serves as a modulation from working memory to episodic memory. 2) To
better align exploratory actions with episodic memory, we prompt the LLM to generate a high-level
description of the strategy underlying the retrieved episodic memory and concatenate this infor-
mation with the prompt. This serves as a modulation from episodic memory to working memory.
The prompts are provided in the Appendix B. The full reasoning loop of our agent is presented in
Algorithm 2.
4

3.5 LEARNINGEPISODICMEMORY FROMGAMEPLAY
Episodic memory typically encompasses both learning and retrieval processes. To efficiently boot-
strap the episodic memory, we use a rule-based agent to collect successful trajectories. Specifically,
we gather game episodes as the agent competes against built-in opponents at Levels 6 and 7 for 20
rounds, and retain episodes from five winning games, yielding a total of 4,592 episodes. To ensure
generalization and avoid overfitting to the data collection regime, we evaluate EpicStar on maps
disjoint from those used during memory collection.
3.6 GAMEINTERFACE
Given the actiona t returned from Algorithm 2, the game interface translates this action into specific
procedures within StarCraft II. We adapt the game interface from Ma et al. (2024), keeping the same
action spaces for fair comparison. To improve generality, we removed overly specific operational
routines hardcoded into theattackanddef endactions, allowing them to be invoked more flexibly
in different contexts.
4 EXPERIMENTS
We evaluated EpicStar by comparing it against built-in agent opponents across varying difficulty
levels, attack styles, and game maps in StarCraft II.
4.1 EXPERIMENTALSETUP
Our evaluation was carried out in two phases: (1) a comparative analysis against baseline methods
and (2) an ablation study to assess the impact of individual components.
We used four closed-source OpenAI models spanning two generations, gpt-3.5-turbo, gpt-4-turbo,
gpt-4o-mini, and gpt-4o (Hurst et al., 2024), to assess whether the benefits of EpicStar are consistent
across backbones of varying capability. We conducted our experiments primarily at difficulty levels
5 and 6. To ensure consistency, we adopted the results from Ma et al. (2024) to mitigate potential
performance degradation due to reproduction. Also, we only usedgpt-4-turboin Level 5 to
match the results from CoS. Additional details on the experimental setup and metrics can be found
in the Appendix A.
4.2 EVALUATIONMETRICS
We used the win rate as the primary indicator of agent performance. To further assess the efficiency
of resource management and technological advancement within the game, we employed additional
metrics detailed in Results5 and the Appendix A.
4.3 FIRSTPHASE: BASELINECOMPARISON
In the first phase of our experiments, we compared EpicStar against the CoS baseline. The agent was
evaluated against built-in agents at difficulty levels 5 and 6, with 40 evaluation rounds conducted at
Algorithm 2EpicStar Agent
Require:StarCraft II Game Environmentenv, Working MemoryW(·)
1:env.initialize(),
2:Q a ← ∅,le ←0,t←0,l q ←0
3:o t ←env.observation()▷Initial observation
4:whileenvis not terminateddo
5:a t ←W(t, Qa, ot, Qo(t), le, lq)
6:t←t+ 1
7:o t =env.step(a t)▷Next frame’s observation
8:end while
9:returnenv.game result()
5

Difficulty Agent Type Win Rate PBR RUR APU TR
Level 5
CoS(GPT-3.5-Turbo) 0.550 0.0781 7875 0.7608 0.4476
CoS(GPT-4-Turbo) 0.600 0.0337 8306 0.7194 0.3452
EpicStar(GPT-3.5-Turbo) 0.575 0.1123 11363 0.7991 0.2500
EpicStar(GPT-4-Turbo)0.7500.1385 11483 0.8449 0.2524
EpicStar(GPT-4o-mini) 0.675 0.1211 9864 0.8123 0.2536
EpicStar(GPT-4o) 0.650 0.1175 11020 0.8107 0.2524
Level 6
CoS(GPT-3.5-Turbo) 0.0833 - - - -
EpicStar(GPT-3.5-Turbo) 0.150 0.1043 11191 0.7378 0.2375
EpicStar(GPT-4o-mini)0.3000.1089 10931 0.7865 0.2304
EpicStar(GPT-4o) 0.275 0.1176 10449 0.7404 0.2220
Table 1: Overall comparison of EpicStar with CoS baseline across different model backends against
Level 5 and Level 6 built-in agents. Bold values indicate the highest win rates within each difficulty
level.
each level (exceptgpt-4-turbois tested with 20 rounds due to its high cost). Specifically, we
tested the agent against various built-in game strategies—timing,rush,power,macro, and
air—as outlined in Appendix A. These tests were conducted on two newly introduced maps for
the 2024 Season,Abyssal Reef LEandEver Dream LE. Each combination of strategy and
map was tested four times, resulting in a total of 40 rounds.
4.4 SECONDPHASE: ABLATIONSTUDY
To evaluate the contribution of individual components within EpicStar, we selectively removed key
elements while keeping other experimental conditions consistent with Phase 1 ongpt-4o-mini.
The first ablation, denoted w/o exploration in the tables and figures below, disables the exploration
step using information from working memory, so that the agent relies solely on retrieved episodes
for reasoning. This allowed us to isolate and assess the role of exploration via LLMs within the
framework. In a subsequent ablation, we removed the contextual fusion to examine the influence
of bidirectional modulation between memory components on the agent’s reasoning and planning
abilities. In EpicStar, ablating episodic memory reduces the agent to a configuration functionally
similar to CoS. Therefore, we omit the ablation of the episodic memory component.
5 RESULTS
5.1 EPICSTAR V.S. BASELINE
We present a comprehensive analysis of EpicStar’s performance with CoS against the built-in agents,
as shown in Table 1. At Level 5, EpicStar achieves a win rate of 67.5% ongpt-4o-miniand
75.0% ongpt-4-turbo, while at Level 6, it secures 30.0% withgpt-4o-mini. In contrast, the
strongest baseline, CoS (gpt-4-turbo), achieves a win rate of 60.0% at Level 5. CoS, however,
struggles considerably at Level 6, with a win rate of just 8.3% (gpt-3.5-Turbo), and EpicStar
nearly doubled the win rate to 15% with the same model. Our method achieves a significant win
rate gain compared to the baseline. Beyond the increase in win rate, our token consumption is only
14.5% of CoS when using the same models (see more details in Appendix C)
Beyond the win rate and token consumption, we observe additional metrics that validate Epic-
Star’s enhanced performance. The Average Population Utilization (APU), which measures the
efficiency of utilizing the population cap, reveals that EpicStar outperforms both baselines with
values of 0.7991(gpt-3.5-turbo) and 0.8449(gpt-4-turbo), compared to 0.7608 for CoS
(gpt-3.5-turbo) and 0.7194 for CoS (gpt-4-turbo). A higher APU indicates more effec-
tive macro management to facilitate units in the game. We note occasional discrepancies among the
Population Block Ratio (PBR; the lower the better), the Tech Rate (TR; a neutral indicator), and the
Win Rate. These discrepancies occur because when EpicStar defeats the built-in agents, our agent
6

Difficulty Agent Type Win Rate PBR RUR APU TR
Level 5
w/o exploration 0.600 0.0598 11778 0.7628 0.2577
w/o fusion 0.650 0.1292 11339 0.8179 0.2619
EpicStar0.6750.1211 9864 0.8123 0.2536
Level 6
w/o exploration 0.175 0.0522 10020 0.6828 0.2393
w/o fusion 0.125 0.0992 13744 0.7497 0.2161
EpicStar0.3000.1089 10931 0.7865 0.2304
Table 2: Overall comparison of EpicStar and two ablation agents against Level 5 and Level 6 built-
in agents. We found that ablating either exploration using working memory or contextual fusion
degrades the performance.
Air
Macro
PowerRush
Timing 0.2
0.4
0.6
0.8
1.0 Air
Macro
PowerRush
Timing 0.2
0.4
0.6
0.8
1.0
EpicStar
w/o Exploration
w/o Fusion
Figure 2: Detailed win rate across built-in strategies on EpicStar and two ablation agent types:
agents without exploration and agents without contextual fusion.
does not accept their surrender. Thus, the game is extended until EpicStar reaches the population
cap, which may result in lower PBR values even after a win.
5.2 ABLATIONSTUDY
To understand the improved performance of EpicStar, we investigated the impacts of the exploration
and contextual fusion components separately. As shown in Table 2, at Level 5, removing exploration
decreases the win rate from 67.5% (EpicStar) to 60.0%, while removing contextual fusion slightly
reduces it to 65.0%. Thus, both components contribute positively, with exploration playing a slightly
more critical role. At Level 6, this impact intensifies: the win rate significantly drops to 17.5%
without exploration and to 12.5% without contextual fusion, compared to EpicStar’s 30.0%. These
findings highlight that strategy coherence becomes increasingly important at higher difficulty levels,
where misaligned exploration significantly impairs performance. It is also worth noting that other
metrics are very close to each other; this is due to the similarities among the three agents.
Furthermore, as shown in Figure 2, at Level 5 (left), the three agents exhibit comparable perfor-
mance profiles across most strategies, indicating that the marginal benefit of exploration and con-
textual fusion is limited at this difficulty. At Level 6 (right), however, the gap widens substantially,
particularly in thePower,Rush, andTimingstrategies, where the ablated agents’ win rates drop
close to zero while EpicStar retains a modest but non-trivial win rate (e.g., 37.5% inPower, 12.5%
inRushandTiming). It is worth noting that absolute win rates remain relatively low for all agents
at this difficulty, suggesting that Level 6 continues to pose a substantial challenge even for the full
EpicStar agent; the results should therefore be interpreted as evidence of relative robustness rather
than mastery of the task. This pattern suggests that the benefits of exploration and contextual fusion
become more pronounced as task difficulty increases.
7

Figure 3: Expansion condition on1,5,8,11minutes for EpicStar (first row) and EpicStar without
exploration (second row). The green dots represent the occupied bases, and EpicStar expands faster
than EpicStar without exploration.
5.3 CASESTUDY
Besides the quantitative results showing the improved performance of EpicStar compared to the
baseline, we conducted a case study on the effect of working memory. Specifically, we compare
EpicStar with and without exploration using working memory. We select a victory case against
Level 6 air style built-in AI from each agent, and we find that EpicStar wins the game faster and
achieves faster expansion, as illustrated(shown time 1:00, 5:00, 8:00, and 11:00, respectively), as
shown in Figure 3. This indicates that EpicStar reasons about its current strategic situation in the
game and utilizes the limited resources more efficiently, and achieves better occupation, which leads
to faster victory against the same opponent.
6 DISCUSSION& FUTUREWORK
Memory mechanisms have been explored in various short-horizon complex tasks. These studies pri-
marily focus on utilizing memory as a storage for intermediate steps in multi-step reasoning (Wang
et al., 2024) or as a means of grounding LLM inference with external knowledge (Wu et al., 2025).
While Hatalis et al. (2023) argue that LLM agents should possess long-term memory, the abundance
of domain knowledge available online has led researchers to prioritize the efficient retrieval of exist-
ing knowledge over developing agents capable of autonomous learning and experiential integration.
We argue that while enabling agents to learn from experience presents significant challenges, it is
essential for the long-term advancement of autonomous intelligence. Our results suggest that even
a small, curated bank of past trajectories can act as an effective substitute for costly exploration
at inference time, echoing findings in case-based reasoning (Klein, 2017) that a handful of well-
chosen precedents can carry more decision-relevant signal than exhaustive search. This reframes
episodic memory not merely as a storage mechanism but as an implicit, non-parametric policy that
complements the LLM’s own reasoning.
However, our work is not without limitations. First, although we observed that incorporating
exploration yields better performance than relying solely on episodic retrieval-a clear sign of
improvement-there is currently limited empirical evidence to determine the extent to which this
performance ceiling depends on the base model’s capabilities. Meanwhile, our episodic memory
8

was bootstrapped from a relatively small set of victories; we have not yet characterized how perfor-
mance scales as the memory grows substantially larger, nor how the agent behaves when the bank
contains noisy, redundant, or contradictory episodes.
Looking forward, several directions could extend this work. To enable more scalable memory use
when reasoning, future work could investigate agentic frameworks that use specialized tokens to rep-
resent memory information, avoiding the growing prompt overhead of appending retrieved episodes
in natural language as the memory bank scales. Additionally, one could explore methods to integrate
parameterized memory in such experiential learning (Jun et al., 2025), which remains a promising
direction. Beyond StarCraft II, testing whether episodic-memory-as-policy transfers to other long-
horizon, partially observable domains would help establish whether strategic drift and its mitigation
via structured memory are general phenomena rather than artifacts of this particular testbed. Finally,
an important safety consideration for any system that reuses past successful behavior is the risk of
overfitting to opponent styles seen during memory collection; developing principled ways to detect
when a retrieved episode no longer applies, rather than relying solely on the gating heuristic used
here, would make such agents more robust when deployed against genuinely novel adversaries.
7 CONCLUSION
In this paper, we introduce a novel perspective on the design of reasoning agents for long-horizon
tasks. By integrating episodic and working memory systems, we enable agents to maintain coherent
strategic trajectories and adapt dynamically to evolving game scenarios. Empirical results demon-
strate that our approach not only outperforms base methods in terms of performance but also has
much lower token consumption, indicating that episodic memory can serve as an implicit mecha-
nism for policy optimization, which enables more efficient reasoning. We show that even limited
high-quality past experience can be maximized for significant performance gains when paired with
a dynamic memory framework. This research also underscores the importance of human cogni-
tive mechanisms in developing AI that can navigate and excel in complex strategic environments,
bridging the gap between artificial intelligence and cognitive science.
REFERENCES
Alexander Braylan, Mark Hollenbeck, Elliot Meyerson, and Risto Miikkulainen. Frame skip is a
powerful parameter for learning to play atari. InAAAI Workshop: Learning for General Compe-
tency in Video Games, 2015.
Google DeepMind. Pysc2 - starcraft ii learning environment, 2017. URLhttps://github.
com/google-deepmind/pysc2. Accessed: 2024-12-27.
Xidong Feng, Yicheng Luo, Ziyan Wang, Hongrui Tang, Mengyue Yang, Kun Shao, David Mguni,
Yali Du, and Jun Wang. Chessgpt: Bridging policy learning and language modeling.Advances in
Neural Information Processing Systems, 36:7216–7262, 2023.
Kostas Hatalis, Despina Christou, Joshua Myers, Steven Jones, Keith Lambert, Adam Amos-Binks,
Zohreh Dannenhauer, and Dustin Dannenhauer. Memory matters: The need to improve long-term
memory in llm-agents. InProceedings of the AAAI Symposium Series, volume 2, pp. 277–280,
2023.
Sihao Hu, Tiansheng Huang, and Ling Liu. Pokellmon: A human-parity agent for pokemon battles
with large language models.arXiv preprint arXiv:2402.01118, 2024.
Chenghao Huang, Yanbo Cao, Yinlong Wen, Tao Zhou, and Yanru Zhang. Pokergpt: An end-to-
end lightweight solver for multi-player texas hold’em via large language model.arXiv preprint
arXiv:2401.06781, 2024.
Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Os-
trow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card.arXiv preprint
arXiv:2410.21276, 2024.
9

James Jun, Vijay Marupudi, Raj Sanjay Shah, and Sashank Varma. A neural network model of
complementary learning systems: Pattern separation and completion for continual learning. In
Proceedings of the Annual Meeting of the Cognitive Science Society, volume 47, 2025.
Keshav Kabra, Kalit Inani, Vijay Marupudi, and Sashank Varma. Modeling understanding of story-
based analogies using large language models. InProceedings of the Annual Meeting of the Cog-
nitive Science Society, volume 47, 2025.
Gary A Klein.Sources of power: How people make decisions. MIT press, 2017.
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal,
Heinrich K¨uttler, Mike Lewis, Wen-tau Yih, Tim Rockt¨aschel, et al. Retrieval-augmented gener-
ation for knowledge-intensive nlp tasks.Advances in neural information processing systems, 33:
9459–9474, 2020.
Weiyu Ma, Qirui Mi, Yongcheng Zeng, Xue Yan, Runji Lin, Yuqiao Wu, Jun Wang, and Haifeng
Zhang. Large language models play starcraft II:benchmarks and a chain of summarization ap-
proach. InThe Thirty-eighth Annual Conference on Neural Information Processing Systems,
2024.
Philipp Mondorf and Barbara Plank. Comparing inferential strategies of humans and large language
models in deductive reasoning. InProceedings of the 62nd Annual Meeting of the Association for
Computational Linguistics (V olume 1: Long Papers), pp. 9370–9402, 2024.
Timo Schick, Jane Dwivedi-Yu, Roberto Dess `ı, Roberta Raileanu, Maria Lomeli, Eric Hambro,
Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can
teach themselves to use tools.Advances in neural information processing systems, 36:68539–
68551, 2023.
Xiao Shao, Weifu Jiang, Fei Zuo, and Mengqing Liu. Swarmbrain: Embodied agent for real-time
strategy game starcraft ii via large language models.arXiv preprint arXiv:2401.17749, 2024.
Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion:
Language agents with verbal reinforcement learning.Advances in Neural Information Processing
Systems, 36, 2024.
Oriol Vinyals, Igor Babuschkin, Wojciech M. Czarnecki, Micha¨el Mathieu, Andrew Dudzik, Juny-
oung Chung, David Choi, Richard Powell, et al. Grandmaster level in starcraft ii using multi-agent
reinforcement learning.Nature, 575:350 – 354, 2019.
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan,
and Anima Anandkumar. V oyager: An open-ended embodied agent with large language models.
Transactions on Machine Learning Research, 2023.
Siyuan Wang, Zhongyu Wei, Yejin Choi, and Xiang Ren. Symbolic working memory enhances lan-
guage models for complex rule application. InProceedings of the 2024 Conference on Empirical
Methods in Natural Language Processing, pp. 17583–17604, 2024.
Jibang Wu, Chenghao Yang, Yi Wu, Simon Mahns, Chaoqi Wang, Hao Zhu, Fei Fang, and Haifeng
Xu. Ai realtor: Towards grounded persuasive language generation for automated copywriting.
arXiv preprint arXiv:2502.16810, 2025.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R Narasimhan, and Yuan
Cao. React: Synergizing reasoning and acting in language models. InThe eleventh international
conference on learning representations, 2022.
10

A EXPERIMENTALSETUP ANDMETRICSDESCRIPTION
A.1 EXPERIMENTALSETUP
Agent and Opponent Configuration:To maintain a consistent and controlled testing environment,
LLM agents are set to play as Protoss against built-in agent-controlled Zerg opponents. This ar-
rangement enables a systematic evaluation of strategic performance across varying difficulty levels.
The difficulty settings are listed below.
Level BLZ Difficulty Approximate League Equivalent
1 Very Easy Bronze (Low)
2 Easy Bronze (Mid)
3 Medium Bronze (High)
4 Hard Silver (Low)
5 Harder Silver (Mid)
6 Very Hard Silver (High)
7 Elite Gold (Low)
8 Cheat Vision Gold (Mid)
9 Cheat Money Gold (High)
10 Cheat Insane Platinum (Low)
Table 3: StarCraft II Built-in Agent Levels and Approximate League Equivalents
Parameter Configuration:The temperature parameter is set to 0.1 to prioritize strategic decision-
making over random actions.
Game Version:All experiments were conducted using the latest Patch5.0.14.93333of Star-
Craft II.
A.2 EVALUATIONMETRICS
Our evaluation framework for TextStarCraft II Ma et al. (2024) builds upon StarCraft II’s established
player performance analytics, incorporating tailored modifications to comprehensively assess LLM
agent gameplay strategies.
Win Rate:This is the primary performance indicator for the agent in the game. It is calculated as
the percentage of victories relative to the total games played.
Population Block Ratio (PBR):PBR assesses the agent’s macro-management skills, specifically
its ability to allocate resources efficiently and sustain population growth. It is defined as:
PBR= Time at Population Cap Game Duration (5)
This metric represents the proportion of time the agent spends at maximum population capacity
relative to the total game duration until it reaches the 200/200 supply cap for the first time. A high
PBR suggests ineffective macro-strategic planning and suboptimal decision-making.
Resource Utilization Ratio (RUR):RUR measures how efficiently the agent manages in-game
resources over time. It is computed as:
RUR= Total Minerals + Total Gas Used Game Duration (6)
This metric evaluates the total resources expended relative to the game’s duration until the agent
first reaches the maximum supply. A high RUR may indicate poor resource utilization, reflecting
suboptimal macro-strategic decisions.
Average Population Utilization (APU):APU quantifies how effectively the agent utilizes its avail-
able population capacity. It is calculated as:
11

APU= 1 N
NX
i=1
Used Population ati th step
Population Cap ati th step

(7)
This metric averages the ratio of the population used to total capacity across all time steps until the
agent reaches full supply. A higher APU indicates more efficient population management and better
macro-strategic execution.
Technology Rate (TR):TR evaluates the agent’s inclination toward technological advancement by
measuring its exploration of the technology tree. It is defined as:
TR= Completed Technologies Total Technologies Available (8)
This metric calculates the fraction of completed technologies and structures relative to the total
available from start to finish of the game. TR reflects the agent’s tendency to pursue technological
upgrades, although it does not necessarily correlate with overall performance.
A.3 STARCRAFTII BUILT-INAGENTSTYLES
1.Timing: Executes attacks at specific moments when a strategic advantage is perceived.
2.Rush: Aims to overwhelm the opponent early by rapidly producing offensive units and
launching swift attacks.
3.Power: Focuses on building a strong economy and technological foundation before engag-
ing in significant combat.
4.Macro: Prioritizes long-term economic growth and infrastructure development.
5.Air: Prioritizes the development and deployment of air units.
B PROMPT
We present the prompt used in the EpicStar and CoS baseline (Ma et al., 2024). Prompt 1 (in
Figure 4) serves as the backbone prompt of EpicStar. In this prompt, the LLM will generate the
strategy description based on the episodic memory retrieved. Here we present the example of the
Warpgate strategy description generated bygpt-4o. Prompt 2 (in Figure 5) is the CoS prompt and
is used in our ablation study.
C TOKENCONSUMPTION OFEPICSTAR ANDCOS
By checking the token usage data from the API (gpt-4o-mini):
On January21,2025, we conducted a total of five test experiments using the CoS baseline, consum-
ing2,592,427tokens, with an average of2,592,427/5 = 518485.4tokens per game.
On February14,2025, we ran 37 experiments with EpicStar, utilizing2,776,468tokens, with an
average of2,776,468/37 = 75039.7tokens per game.
From this data, it is evident that our token consumption for EpicStar is nearly an order of magnitude
lower than that for the CoS baseline.
12

Prompt 1: System prompt with contextual fusion from episodic memory (e.g. Warpgate strategy).
You are an AI trained in analyzing and summarizing StarCraft II games. You understand the nuances and
strategies of the Protoss race.Specifically, you are playing the WarpGate Strategy in StarCraft II,
which is a core tactic for the Protoss race, leveraging their ability to instantly warp in units anywhere
on the map using Pylons or Warp Prisms. By converting Gateways into Warp Gates, Protoss players can
quickly reinforce their army or apply pressure without needing to rally units across the map. This
strategy emphasizes map control, timing attacks, and flexibility, often paired with strong early-game
units like Zealots or Stalkers. Proper use of Warp Gates can overwhelm opponents with rapid unit
production and strategic positioning.
Based on the summaries of multiple rounds in a game, we want you to analyze the game progression in a
structured way. Your analysis should include the following aspects:
1. Game Overview: Provide a brief overview of the current situation based on all the rounds.
2. Current Game Stage: Determine the stage of the game based on the information of all rounds. Is it
the early game, mid-game, or late game?
3. Our Situation: Describe our current status in terms of:
3.1 Units and Buildings: Analyze the state of our units and buildings.
3.2 Economy: Evaluate our economic condition, including resource collection and usage.
3.3 Technology: Describe the status of our technological research and what technologies we have unlocked
so far. Analyze our technology tree, indicating the available and potential upgrades or units.
4. Our Strategy: Infer our potential strategy based on our current situation and the information of all
rounds.
5. Enemy’s Strategy: Infer the enemy’s potential strategy, based on the available information.
6. Key Information: Highlight the most important aspects from all rounds that have significantly
influenced the game.
For Protoss, keep an eye on Nexus’s energy to Chrono Boost important structures, and keep an eye on
training units and building pylons.
Based on the game situation and strategies used by both sides, provide specific suggestions for the
following areas:
1. Our Strategy: Propose adjustments to our current strategy to counter the enemy’s moves and
capitalize on our strengths.
2. Units and Buildings: Offer ways to enhance our unit composition and improve our building layout,
suited to the current stage of the game.
3. Economy: Recommend better practices for resource gathering and usage, in line with our strategic
needs.
4. Technology: Suggest focused research paths to gain technological advantages, considering our current
research status and technology tree.
5. Feasibility: Based on current resources like mineral, gas, buildings, supplies, workers, use your
knowledge in StarCraft II to brainstorm 3 coarse decisions that can be successfully executed and think
and explain why.
5. Decisions: Lastly, consider the current situation and the suggestions provided, make 3 actionable
and specific decisions from the action dictionary{TRAIN UNIT:{0: TRAIN PROBE, 1: TRAIN ZEALOT,
2: TRAIN ADEPT, 3: TRAIN STALKER, 4: TRAIN SENTRY, 5: TRAIN HIGHTEMPLAR, 6: TRAIN DARKTEMPLAR,
7: TRAIN VOIDRAY, 8: TRAIN CARRIER, 9: TRAIN TEMPEST, 10: TRAIN ORACLE, 11: TRAIN PHOENIX,
12: TRAIN MOTHERSHIP, 13: TRAIN OBSERVER, 14: TRAIN IMMORTAL, 15: TRAIN WARPPRISM, 16: TRAIN
COLOSSUS, 17: TRAIN DISRUPTOR, 18: MORPH ARCHON}, BUILD STRUCTURE:{19: BUILD PYLON, 20:
BUILD ASSIMILATOR, 21: BUILD NEXUS, 22: BUILD GATEWAY, 23: BUILD CYBERNETICSCORE, 24: BUILD
FORGE, 25: BUILD TWILIGHTCOUNCIL, 26: BUILD ROBOTICSFACILITY, 27: BUILD STARGATE, 28: BUILD
TEMPLARARCHIVE, 29: BUILD DARKSHRINE, 30: BUILD ROBOTICSBAY, 31: BUILD FLEETBEACON, 32: BUILD
PHOTONCANNON, 33: BUILD SHIELDBATTERY}, RESEARCH TECHNIQUE:{34: RESEARCH WARPGATERESEARCH,
35: RESEARCH PROTOSSAIRWEAPONSLEVEL1, 36: RESEARCH PROTOSSAIRWEAPONSLEVEL2, 37: RESEARCH
PROTOSSAIRWEAPONSLEVEL3, 38: RESEARCH PROTOSSAIRARMORSLEVEL1, 39: RESEARCH PROTOSSAIRARMORSLEVEL2,
40: RESEARCH PROTOSSAIRARMORSLEVEL3, 41: RESEARCH ADEPTPIERCINGATTACK, 42: RESEARCH BLINKTECH, 43:
RESEARCH CHARGE, 44: RESEARCH PROTOSSGROUNDWEAPONSLEVEL1, 45: RESEARCH PROTOSSGROUNDWEAPONSLEVEL2,
46: RESEARCH PROTOSSGROUNDWEAPONSLEVEL3, 47: RESEARCH PROTOSSGROUNDARMORSLEVEL1, 48:
RESEARCH PROTOSSGROUNDARMORSLEVEL2, 49: RESEARCH PROTOSSGROUNDARMORSLEVEL3, 50: RESEARCH
PROTOSSSHIELDSLEVEL1, 51: RESEARCH PROTOSSSHIELDSLEVEL2, 52: RESEARCH PROTOSSSHIELDSLEVEL3, 53:
RESEARCH EXTENDEDTHERMALLANCE, 54: RESEARCH GRAVITICDRIVE, 55: RESEARCH OBSERVERGRAVITICBOOSTER,
56: RESEARCH PSISTORMTECH, 57: RESEARCH VOIDRAYSPEEDUPGRADE, 58: RESEARCH PHOENIXRANGEUPGRADE, 59:
RESEARCH TEMPESTGROUNDATTACKUPGRADE}, OTHER ACTION:{60: SCOUTING PROBE, 61: SCOUTING OBSERVER, 62:
SCOUTING ZEALOT, 63: SCOUTING PHOENIX, 64: MULTI-ATTACK, 65: MULTI-RETREAT, 66: CHRONOBOOST NEXUS,
67: CHRONOBOOST CYBERNETICSCORE, 68: CHRONOBOOST TWILIGHTCOUNCIL, 69: CHRONOBOOST STARGATE, 70:
CHRONOBOOST FORGE, 71: EMPTY ACTION}}. This dictionary comprises four categories of actions: unit
production, building construction, technology research, and other actions. Remember to align these
decisions with the current stage and WarpGate strategy of the game, and avoid proposing actions that are
not currently feasible, such as actions requiring more resources than we have now, actions that are not
in correct condition, etc. Remember to outline each action with<ACTION NAME>, surrounded by<and>.
Figure 4: System prompt with contextual fusion from episodes where Warpgate strategy was used.
Description is generated usinggpt-4owhen summarizing the strategy used in retrieved episodic
memory (in bold)
13

Prompt 2: System prompt of Chain of Summarization (CoS)
You are an AI trained in analyzing and summarizing StarCraft II games. You understand the nuances and
strategies of the Protoss race.
Based on the summaries of multiple rounds in a game, we want you to analyze the game progression in a
structured way. Your analysis should include the following aspects:
1. Game Overview: Provide a brief overview of the current situation based on all the rounds.
2. Current Game Stage: Determine the stage of the game based on the information of all rounds. Is it
the early game, mid-game, or late game?
3. Our Situation: Describe our current status in terms of:
3.1 Units and Buildings: Analyze the state of our units and buildings.
3.2 Economy: Evaluate our economic condition, including resource collection and usage.
3.3 Technology: Describe the status of our technological research and what technologies we have unlocked
so far. Analyze our technology tree, indicating the available and potential upgrades or units.
4. Our Strategy: Infer our potential strategy based on our current situation and the information of all
rounds.
5. Enemy’s Strategy: Infer the enemy’s potential strategy, based on the available information.
6. Key Information: Highlight the most important aspects from all rounds that have significantly
influenced the game.
For Protoss, keep an eye on Nexus’s energy to Chrono Boost important structures, and keep an eye on
training units and building pylons.
Based on the game situation and strategies used by both sides, provide specific suggestions for the
following areas:
1. Our Strategy: Propose adjustments to our current strategy to counter the enemy’s moves and
capitalize on our strengths.
2. Units and Buildings: Offer ways to enhance our unit composition and improve our building layout,
suited to the current stage of the game.
3. Economy: Recommend better practices for resource gathering and usage, in line with our strategic
needs.
4. Technology: Suggest focused research paths to gain technological advantages, considering our current
research status and technology tree.
5. Feasibility: Based on current resources like mineral, gas, buildings, supplies, workers, use your
knowledge in StarCraft II to brainstorm 3 coarse decisions that can be successfully executed and think
and explain why.
5. Decisions: Lastly, consider the current situation and the suggestions provided, make 3 actionable
and specific decisions from the action dictionary{TRAIN UNIT:{0: TRAIN PROBE, 1: TRAIN ZEALOT,
2: TRAIN ADEPT, 3: TRAIN STALKER, 4: TRAIN SENTRY, 5: TRAIN HIGHTEMPLAR, 6: TRAIN DARKTEMPLAR,
7: TRAIN VOIDRAY, 8: TRAIN CARRIER, 9: TRAIN TEMPEST, 10: TRAIN ORACLE, 11: TRAIN PHOENIX,
12: TRAIN MOTHERSHIP, 13: TRAIN OBSERVER, 14: TRAIN IMMORTAL, 15: TRAIN WARPPRISM, 16: TRAIN
COLOSSUS, 17: TRAIN DISRUPTOR, 18: MORPH ARCHON}, BUILD STRUCTURE:{19: BUILD PYLON, 20:
BUILD ASSIMILATOR, 21: BUILD NEXUS, 22: BUILD GATEWAY, 23: BUILD CYBERNETICSCORE, 24: BUILD
FORGE, 25: BUILD TWILIGHTCOUNCIL, 26: BUILD ROBOTICSFACILITY, 27: BUILD STARGATE, 28: BUILD
TEMPLARARCHIVE, 29: BUILD DARKSHRINE, 30: BUILD ROBOTICSBAY, 31: BUILD FLEETBEACON, 32: BUILD
PHOTONCANNON, 33: BUILD SHIELDBATTERY}, RESEARCH TECHNIQUE:{34: RESEARCH WARPGATERESEARCH,
35: RESEARCH PROTOSSAIRWEAPONSLEVEL1, 36: RESEARCH PROTOSSAIRWEAPONSLEVEL2, 37: RESEARCH
PROTOSSAIRWEAPONSLEVEL3, 38: RESEARCH PROTOSSAIRARMORSLEVEL1, 39: RESEARCH PROTOSSAIRARMORSLEVEL2,
40: RESEARCH PROTOSSAIRARMORSLEVEL3, 41: RESEARCH ADEPTPIERCINGATTACK, 42: RESEARCH BLINKTECH, 43:
RESEARCH CHARGE, 44: RESEARCH PROTOSSGROUNDWEAPONSLEVEL1, 45: RESEARCH PROTOSSGROUNDWEAPONSLEVEL2,
46: RESEARCH PROTOSSGROUNDWEAPONSLEVEL3, 47: RESEARCH PROTOSSGROUNDARMORSLEVEL1, 48:
RESEARCH PROTOSSGROUNDARMORSLEVEL2, 49: RESEARCH PROTOSSGROUNDARMORSLEVEL3, 50: RESEARCH
PROTOSSSHIELDSLEVEL1, 51: RESEARCH PROTOSSSHIELDSLEVEL2, 52: RESEARCH PROTOSSSHIELDSLEVEL3, 53:
RESEARCH EXTENDEDTHERMALLANCE, 54: RESEARCH GRAVITICDRIVE, 55: RESEARCH OBSERVERGRAVITICBOOSTER,
56: RESEARCH PSISTORMTECH, 57: RESEARCH VOIDRAYSPEEDUPGRADE, 58: RESEARCH PHOENIXRANGEUPGRADE, 59:
RESEARCH TEMPESTGROUNDATTACKUPGRADE}, OTHER ACTION:{60: SCOUTING PROBE, 61: SCOUTING OBSERVER, 62:
SCOUTING ZEALOT, 63: SCOUTING PHOENIX, 64: MULTI-ATTACK, 65: MULTI-RETREAT, 66: CHRONOBOOST NEXUS,
67: CHRONOBOOST CYBERNETICSCORE, 68: CHRONOBOOST TWILIGHTCOUNCIL, 69: CHRONOBOOST STARGATE, 70:
CHRONOBOOST FORGE, 71: EMPTY ACTION}}. This dictionary comprises four categories of actions: unit
production, building construction, technology research, and other actions. Remember to align these
decisions with the current stage and WarpGate strategy of the game, and avoid proposing actions that are
not currently feasible, such as actions requiring more resources than we have now, actions that are not
in correct condition, etc. Remember to outline each action with<ACTION NAME>, surrounded by<and>.
Figure 5: System prompt of CoS, which is used in the ablation study.
14
