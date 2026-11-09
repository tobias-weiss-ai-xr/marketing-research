---
title: 'SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized
  Energy Markets'
url: https://arxiv.org/abs/2607.08681
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Shilin Ou
- Yifan Xu
- Luyao Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.08681
pages: 14
chars: 62484
fetched_at: '2026-11-08T13:02:59+00:00'
kb_version: 1
---

# SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets

SolarChain-Eval: A Physics-Constrained Benchmark for
Trustworthy Economic Agents in Decentralized Energy Markets
Shilin Ou†
Duke Kunshan University
Kunshan, Jiangsu, China
Yifan Xu†
Duke Kunshan University
Kunshan, Jiangsu, China
Luyao Zhang∗
Duke Kunshan University
Kunshan, Jiangsu, China
1. Solar-Market Inputs 2. Physics-Constrained Benchmark MDP 3. Agentic AI 4. Evaluation
☀
Solar Nodes
irradiance, temp, P_max
⚡
P2P Market
demand, liquidity, price
🔎
Trust Labels
FDIA flags, rejected reports, excess generation
📁
Benchmark Tables
nodes | generation | trades | liquidity
🕑
City-Hour Aggregation
verified, reported, rejected
MWh
📈
Market Features
supply gap, slippage, volume
BenchmarkData
shared data object for training and
evaluation
🔧
State Encoder
time, supply, demand, risk
🗺
Observation
, previous action, market state
🛡
Physics Gate
P_max, FDIA, unsafe supply
⚖
Market Transition
clearing, price, drawdown
🎯
Reward Accounting
utility, stability, safety, fairness
🔃
Step Output
, , info_t
Benchmark Environment
Gymnasium-compatible MDP
🤖
Policy Candidate
Static, Random, Myopic, RL
🎲
Governance Action
🧠
LLM Planner
episode bounds, audit policy
🛡
LLM Auditor
trigger, approve, revise
📐
Action Sanitizer
bounds, allocation budget
📋
Agentic Trace
plan validity, audits, revisions
Final Executed Action
policy action after planner/auditor
constraints
🔄
Controlled Rollouts
policy x episode x seed
📊
Trust Metrics
reward, risk, drawdown, fairness
🔬
Penalty Ablation
unsafe supply still logged
📝
Agentic Metrics
audit rate, revision rate, delta
📄
Run Artifacts
metrics.csv, actions.csv,
summary.json
🖼
Paper Figures
curves, frontier, city-hour
heatmap
Benchmark Evidence Bundle
utility, safety, stability, fairness, auditability
Action space
: reward allocation; : liquidity support; : token burn.
Constraint signals
P_max, FDIA labels, unsafe-backed MWh, and physics-penalty ablation.
Reported Matrix
Learning curves, safety-utility frontier, city heatmap, and agentic logs.
hourly records
labels
verified supply
risk terms
reward
observation
proposal
bounds
triggerclip
revision
logs
final action
trajectories
counterfactual
agent logs CSV/JSON
Figure 1: OverallSolarChain-Evalbenchmark pipeline. The figure summarizes the end-to-end workflow from data loading, RL
training, policy evaluation, output generation, and trustworthiness evidence for decentralized energy-market governance.
Abstract
As agentic AI systems are increasingly applied to cyber-physical
environments, their evaluation requires assessment of both task
performance and trustworthiness. In decentralized energy markets,
autonomous agents may improve market utility, but may also ex-
ploit invalid physical data, create artificial liquidity, and produce
unstable governance decisions. Therefore, we proposeSolarChain-
Eval, a physics-constrained benchmark for evaluating trustworthy
economic agents. It formulates market governance as a Gymnasium-
compatible Markov Decision Process, where agents make hourly
decisions.SolarChain-Evalevaluates each policy across multiple di-
mensions, including market utility, physical safety, slippage, action
smoothness, spatial fairness, and auditability.
To support agentic evaluation,SolarChain-Evalincorporates an
LLM-based Planner/Auditor layer. The Planner defines episode-
level action bounds and audit rules, while the Auditor reviews and
revises high-risk actions. All interventions are recorded through
structured logs, including trigger signals, proposed actions, revised
actions, and audit rationales. Experiments with static, random, my-
opic, RL, and RL+LLM policies reveal a clear utility-safety trade-off.
†Equal contribution.
∗The Corresponding author: Email: lz183@duke.edu, Digital Innovation Research
Center and Social Science Division, Duke Kunshan University, Address: Duke Avenue
No.8, Kunshan, Suzhou, Jiangsu, China, 215316.Acknowledgments: Shilin Ou is
grateful for the support from the Summer Research Scholar Program at Duke Kunshan
University, supervised by Prof. Luyao Zhang.
RL agents improve market utility but can still produce unsafe be-
havior. When the physics penalty is removed, reward-maximizing
agents exploit invalid generation and increase artificial liquidity.
The LLM Planner/Auditor improves auditability and mitigates se-
lected risks, but it cannot fully compensate for a misspecified re-
ward function. These results indicate that trustworthy agentic AI
evaluation requires both physical constraints and transparent inter-
vention traces. We release data and code as open access on GitHub
for replicability.
Keywords
Agentic AI, reinforcement learning, trustworthiness evaluation,
tokenomics, decentralized energy markets
1 Introduction
Agentic AI is increasingly used to support autonomous decision-
making in cyber-physical and economic systems[30]. Such agents
not only optimize digital objectives, their actions may also affect
physical resources, market incentives, and systems safety[29]. This
shift raises an evaluation challenge that agent performance cannot
be judged by scalar reward alone. Trustworthy agents should there-
fore make decisions that are physically grounded, constraint-aware,
and auditable under real-world operating conditions [7, 20, 22].
In decentralized energy markets, reinforcement learning (RL) has
been used to manage market liquidity, token issuance, and incentive
distribution [21, 27]. However, unlike purely digital environments,
arXiv:2607.08681v1  [cs.AI]  9 Jul 2026

Ou et al.
Table 1: Comparison of Prevailing Bi-Level Architectures Integrating RL and LLM Agents
Framework Domain Synergy Mechanism (LLM + RL) Limitations & Challenges
RE-GoT[34] Robotic Control &
Manipulation
Upper-level LLM uses Graph-of-Thoughts
to evolve reward functions; Vision models
analyze RL rollouts for semantic feedback.
High latency due to LLM/VLM in-
ference bottlenecks in real-time con-
trol loops.
RL2 [33] Active Distribution
Networks
LLM translates operator safety intents into
mathematical penalties; adapts parameters
via DRL feedback.
Sensitive to LLM hallucination dur-
ing algebraic adjustments.
ADMM-LLM[32] Microgrid Heat-
Electricity
LLM acts as an optimizer that observes op-
timization residuals to predict and adjust
decentralized ADMM penalty parameters.
Heuristic trial-and-error lacks strict
mathematical convergence guaran-
tees.
energy markets are bounded by physical laws, such as localized so-
lar irradiance and photovoltaic panel capacities [18, 36]. Deploying
reward-maximizing agents in such environments therefore creates
important trustworthiness risks. Without explicit physical con-
straints, RL models can learn to exploit weaknesses in the market
mechanism [1].
To address this, we proposeSolarChain-Eval, a physics-constrained
benchmark for evaluating trustworthy agentic AI in decentral-
izedenergy markets.SolarChain-Evalcombines solar signals with
controlled market and risk scenarios, and formulates market gov-
ernance as a Gymnasium-compatible Markov Decision Process.
To further examine agentic oversight,SolarChain-Evalincorpo-
rates an evaluation-time LLM-based Planner/Auditor layer, which
is inserted between the trained RL policy and the benchmark en-
vironment without being used during RL training. The Planner
defines episode-level action bounds and audit rules, while the Au-
ditor reviews and revises high-risk actions. This design enables
SolarChain-Evalto assess both the operational performance of an
RL policy, and the extent to which its decision-making behavior
remains governable and interpretable.
Specifically, we concentrate on the following research questions:
• RQ1:How do autonomous market policies trade off eco-
nomic utility, physical safety, stability, and fairness com-
pared with static and heuristic baselines?
• RQ2:To what extent do reward-maximizing agents ex-
ploit invalid generation and create artificial liquidity when
physics penalties are removed?
• RQ3:How does an LLM-based Planner/Auditor contribute
to auditable risk mitigation for trained RL policies, and
what are its limitations under reward misspecification?
Data and Code Availabilty Statements: We release data and
code as open access on GitHub1 for replicability.
2 Literature Review
2.1 Reinforcement Learning in Tokenomics
Traditional economic mechanisms struggle when applied to decen-
tralized energy markets due to the restrictive assumptions of station-
ary environments [37]. Distributed Energy Resources (DERs) are
1https://github.com/yxu-dev/SolarChain-Eval
governed by intermittent generation constraints and Peer-to-Peer
(P2P) network topologies [5]. However, tokenomic mechanisms are
subject to extreme volatility driven by liquidity depth, speculative
token price trajectories, and adoption rates [6, 17]. RL provides a
flexible modeling approach by formulating market governance as
a Markov Decision Process [37]. It can adapt to high-dimensional
state spaces, optimizing long-term objectives that balance physical
utility with economic stability[37].
In current decentralized market governance literature[23, 31],
macroeconomic control is typically abstracted into continuous gov-
ernance levers, such as the reward ratio ( 𝑟𝑡 ), liquidity ratio (𝑙𝑡 ),
and token burn rate (𝑏𝑡 ). In simulated environments, the normal-
ized action vector𝑎𝑡 is decoded into specific economic parameters.
To evaluate system trustworthiness, researchers widely rely on
standardized frameworks likeStable-Baselines3[ 24] to benchmark
distinct RL algorithmic paradigms:
Proximal Policy Optimization (PPO) is an on-policy actor-critic
algorithm widely applied to continuous action space governance
tasks. To prevent excessively large policy updates, PPO utilizes a
clipped surrogate objective [26]:
𝐿𝐶𝐿𝐼𝑃(𝜃)= ˆE𝑡  min(𝑝𝑡(𝜃) ˆ𝐴𝑡,clip(𝑝 𝑡(𝜃),1−𝜖,1+𝜖) ˆ𝐴𝑡)  (1)
where𝜃 denotes the policy network parameters, 𝑝𝑡(𝜃) is the prob-
ability ratio, ˆ𝐴𝑡 represents the estimated advantage function, and 𝜖 is
the clipping hyperparameter.
In tokenomic governance, this high training stability translates
to practical advantages by effectively suppressing action jitter and
ensuring smoother adjustments of macroeconomic parameters.
Also supporting continuous control, Soft Actor-Critic (SAC) is an
off-policy algorithm. By incorporating a maximum entropy mecha-
nism into its objective function [11], SAC proactively encourages
the agent to explore diverse tokenomic strategies:
𝐽(𝜋)=
𝑇∑︁
𝑡=0
E(𝑠𝑡,𝑎𝑡)∼𝜌 𝜋[𝑟(𝑠𝑡,𝑎𝑡)+𝛼H(𝜋(·|𝑠 𝑡))] (2)
where𝑟(𝑠𝑡,𝑎𝑡) denotes the immediate reward,𝛼 is the temperature
parameter, andH(𝜋(·|𝑠 𝑡)) represents the entropy of the policy 𝜋 at
state𝑠𝑡 .

SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets
Existing research demonstrates that this mechanism not only
improves sample efficiency but also prevents the policy from prema-
turely converging to suboptimal local minima in highly nonlinear
market environments[3].
As a robust value-based baseline algorithm, Deep Q-Network
(DQN) is applied to discrete action spaces. In multidimensional
control tasks, continuous levers are typically discretized. Despite
inherent quantization errors, DQN excels at accurately estimating
the action-value function𝑄(𝑠,𝑎)[19, 28].
2.2 RL & LLM Agent Integration
RL has shown strong performance in high-dimensional continuous
control tasks. However, its black-box nature limits its reliability in
infrastructure [2]. In practice, human auditors may find it difficult
to explain why an RL policy makes adjustments [25]. Furthermore,
while post-hoc AI methods offer retrospective insights, they cannot
proactively prevent unsafe actions[10].
Recent studies address this by integrating Large Language Mod-
els (LLMs) with RL systems. LLMs could act as high-level reasoners
to process task context and operator instructions [ 35]. This abil-
ity allows them to translate operator intents into mathematical
penalties that can support lower-level decision making [8].
Consequently, current research is shifting toward a bi-level RL-
LLM architecture [4]. The lower layer uses RL policies to make
frequent control decisions based on value estimates such as𝑉(𝑠)
or𝑄(𝑠,𝑎) . The upper layer uses LLMs for slower and more abstract
reasoning tasks. Prior work has used LLMs to convert operator
intent into reward penalties [13], revise reward functions, and tune
optimization parameters [16]. Table 1 summarizes representative
examples of this design.
Recent advances in RL have improved agent-based optimization
in Cyber-Physical Systems, especially in decentralized energy mar-
kets [12, 15]. As the focus shifts toward real-world deployment [9],
there is a growing need to complement traditional reward-centric
benchmarks with evaluations of trustworthiness. Specifically, en-
suring safe operation requires assessing an agent’s adherence to
physical constraints and its resilience in adversarial scenarios [14].
Following this view, our benchmark couples economic dynamics
with physical ground truths and evaluates agentic trustworthiness
across multiple dimensions.
3 Methodology
Instead of merely maximizing short-term trading volume, our bench-
mark evaluates the overall trustworthiness of an autonomous eco-
nomic agent. It assesses whether the agent can maintain market
utility while respecting physical limits, ensuring market stability,
reducing action jitter, and preserving spatial fairness. Each episode
represents a 24 hour market cycle, sampled from a 720-hour dataset
from April 2026. Episodes are constrained to start at the beginning
of the day. This temporal design ensures a consistent daily decision
horizon for the agent while preserving real-world weather patterns.
3.1 RL Formulation
Figure 2 summarizes the RL loop. Energy generation, market de-
mand, and physics labels are aggregated into an hourly benchmark
state. Based on this state, a policy proposes a governance action.
The state𝑠𝑡 and action𝑎𝑡 are defined as:
𝑠𝑡 =[sin𝜏 𝑡,cos𝜏 𝑡,𝐺𝑣 𝑡,𝐺𝑟 𝑡,𝑃 max 𝑡 ,Δ𝑡,𝐿𝑡,𝑝𝑡,𝜈𝑡,𝜎𝑡,𝛼𝑡−1,ℓ𝑡−1],
𝑎𝑡 =(𝛼 𝑡,ℓ𝑡,𝑏𝑡), 𝛼 𝑡+ℓ𝑡≤0.98. (3)
Here,𝜏𝑡 is the time angle, 𝐺𝑣 𝑡 is verified generation, 𝐺𝑟 𝑡 is reported
generation,𝑃 max 𝑡 is the physical PV upper bound, Δ𝑡 is the supply-
demand gap, 𝐿𝑡 is market liquidity, 𝑝𝑡 is token price, 𝜈𝑡 is the raw
risk signal, and𝜎 𝑡 is the static slippage.
The action𝑎𝑡 comprises the reward allocation ratio𝛼𝑡 , liquidity
injection ratioℓ𝑡 , and token burn rate𝑏𝑡 . Standard algorithms like
PPO and SAC operate on the continuous action space, while DQN
utilizes a discretized5 3 = 125action grid over the same parameters.
All trained policies are evaluated under the uniform benchmark
setting detailed in Table 2.
Table 2: Main benchmark configuration.
Item Value
Cities Beijing, Shanghai, Chengdu, Shenzhen, Hangzhou
Energy nodes 50
Main period 2026-04-01 to 2026-04-30
Hourly market states 720
Generation records 36,000
P2P trade records 1,185
Episode length 24 hours
Evaluated Policies Static, Random, Myopic, PPO, SAC, DQN
3.2 Physics Limit and Market Transition
SolarChain-Evalimplements a physics constraint module, which
verifies whether reported generation is physically feasible and FDIA
labels. Let𝑋𝑡 denote suspicious or invalid supply. The benchmark
not only records this anomaly but quantifies the extent to which
the policy economically backs it:
𝑉𝑡 = 𝛽𝑡𝑋𝑡 max(𝐺𝑣 𝑡+𝛽𝑡𝑋𝑡,𝜖) , 𝛽 𝑡 = min(𝛼𝑡+ℓ𝑡,0.98) 0.98 .(4)
In Eq. (4),𝑉𝑡 is the action-dependent physics violation term. A
policy incurs higher risk when it heavily backs invalid supply. This
formulation directly addresses RQ2: through a no-physics-penalty
ablation, we can observe whether a purely reward-driven agent
exploits invalid generation to inflate artificial liquidity.
Additionally, the market module processes the backed supply,
consisting of verified supply and the action-backed suspicious sup-
ply. It updates the matched energy𝑀𝑡 and computes the residual
liquidity𝐿𝑡+1 for the next hour:
𝑀𝑡 =min(𝐿 𝑡+ℓ𝑡(𝐺𝑣 𝑡+𝛽𝑡𝑋𝑡), e𝑄𝑡),
𝐿𝑡+1 =max(𝐿 𝑡+ℓ𝑡(𝐺𝑣 𝑡+𝛽𝑡𝑋𝑡)−𝑀 𝑡,0). (5)
Here, e𝑄𝑡 represents the effective demand after token burning, com-
puted as
e𝑄𝑡 =𝑄𝑑 𝑡 max(0.75,1−0.80𝑏 𝑡),
where𝑄𝑑 𝑡 is the raw market demand. This mechanism explicitly
links the agent’s governance decisions to both trading volume and
market liquidity depth.

Ou et al.
1. Physics-Constrained Reinforcement Learning Loop
2. Policy Optimization 3. Trustworthiness Evaluation
4. Reported Artifacts
State Encoder
city-hour features
MDP State
: market and risk
Policy / Q Function
 or
Governance Action Constraint Gate
bounds and budget
Environment Kernel
physics and clearing
Reward Model
utility, safety, fairnessTransition Record
: time; : verified/reported generation; : physical limit; : supply gap; :
liquidity/price; : risk/stability.
 : matched energy; : drawdown and jitter; :
unsafe supply, violation, fairness loss.
Trajectory Buffer
rollout or replay
PPO
on-policy
SAC
entropy-regularized
DQN
value-based
: policy ratio; : advantage; : entropy temperature; :
discount factor; : target network.
Trained Policy
benchmark candidate
Policy Set
baselines and RL
Controlled Rollouts
episode and seed
Trust Metrics
utility and risk
Utility | Safety | Stability | Fairness | Auditability
Benchmark Outputs
hourly trajectories and reproducibility metadata
 Figures
safety-utility tradeoff and city-hour allocation patterns
Trust Evidence
physics-penalty ablation and unsafe-liquidity monitoring for
agentic AI evaluation
observation proposal projection
market outcomenext state
samples
objective update
parameter update
reported evidence
Energy Data
generation and trades
Market Data
liquidity and price
Physics Labels
P_max and FDIA
Figure 2: Reinforcement learning evaluation framework for SolarChain-Eval. The diagram connects market and physical
inputs to policy actions, environment feedback, PPO/SAC/DQN updates, and trustworthiness-oriented evaluation across utility,
safety, stability, smoothness, and fairness.
3.3 Reward Design and RL Optimization
To optimize for both utility and market trustworthiness, the step
reward implements a series of penalties (Figure 2):
𝑅𝑡 =𝑀𝑡−𝜆𝑑𝐷𝑡−𝜆 𝑗𝐽𝑡−𝜆𝑢𝑈𝑡−𝜆𝑝 Φ𝑡−𝜆 𝑓𝐹𝑡,
Φ𝑡 =𝑉𝑡+𝐴𝑡, 𝐴 𝑡 =𝛽 𝑡𝑋𝑡. (6)
The positive term𝑀𝑡 rewards successful market clearing. The cor-
responding penalties address liquidity drawdown (𝐷𝑡 ), action jitter
(𝐽𝑡 ), unmet demand (𝑈𝑡 ), composite physics risk (Φ𝑡 ), and spatial
unfairness across cities (𝐹𝑡 ). Here, Φ𝑡 combines the normalized
physics violation rate𝑉𝑡 and the action-backed suspicious supply
amount𝐴𝑡 .
The RL policies are trained using Stable-Baselines3. The bench-
mark incorporates three learned controllers with distinct optimiza-
tion biases: PPO for stable on-policy updates, SAC for entropy-
guided continuous exploration, and DQN for discrete Q-value learn-
ing. For instance, DQN optimizes the following target over the
discretized action grid:
𝑦𝑡 =𝑅𝑡+𝛾max 𝑎′ 𝑄 ¯𝜃(𝑠𝑡+1,𝑎′).(7)
Static, random, and myopic controllers are also evaluated as non-
learning baselines to provide a comparison.
3.4 LLM Planner/Auditor Layer
To evaluate whether agentic oversight improves deployment-time
safety, we introduce an AI-agent governance layer powered by
LLMs, as shown in Figure 3. We insert this layer between the trained
RL policy (e.g., PPO, SAC, DQN) and the market environment. This
layer is active only during evaluation and is never used during RL
training. This separation ensures that any observed safety improve-
ment stems from deployment-time guardrails rather than from
reward shaping, policy retraining, or parameter updates.
The governance layer consists of two components: a Planner
and an Auditor.
The Planner operates at the episode level. At the start of each
24-hour episode, it reviews episode-level context, including supply-
demand adequacy, physics-risk statistics, static-market slippage,
and benchmark action constraints. Based on this context, the Plan-
ner establishes admissible bounds for the RL action components,
namely the reward ratio𝛼𝑡 , liquidity ratioℓ𝑡 , and burn rate𝑏𝑡 . It also
outputs an episode-specific audit policy, including risk thresholds,
a maximum audit budget𝐵𝑒, a target audit rate, and a minimum
cooldown length𝑐𝑒. At each hourly step, the RL policy’s proposed
action is first decoded into market variables and clipped by the
Planner-defined bounds and benchmark constraints, yielding a
bounded action ¯𝑎𝑡 .
The Auditor provides sparse step-level oversight. Instead of re-
viewing every action, it is invoked only when risk signals indicate
possible safety or market-integrity failures. To avoid notational
conflict with the reward terms in Eq. (6), we denote the audit-side
action-instability signal by 𝜅𝑡 . It is computed as the ℓ1 distance
between the current bounded action and the previous executed
action:
𝜅𝑡 =∥ ¯𝑎𝑡−𝑎𝑡−1∥1.(8)
We further define the audit-side normalized supply-demand gap as
Δ𝑎𝑢𝑑𝑖𝑡 𝑡 = 𝐺𝑣 𝑡−𝑄𝑑 𝑡 max(𝑄𝑑 𝑡,𝜖) ,(9)

SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets
Reinforcement Learning Layer
Rollout Buffer
o, a, r
Observation
state vector
Policy Network
PPO / SAC / DQN
State Encoder
features
obs
RL Update
training only
parameter update
Action Decode
r, l, b
raw action
AI Agentic Governance Layer
Episode Context
risk summary
Planner Prompt
task rules
LLM Planner
episode policy
Schema Check
clip to config
Plan
bounds + audit rules
Action Composer
final action
Agentic Log
plan, audit, delta
action delta
LLM Auditor
approve / revise revision
Bounds Gate
constrain action
bounds
Risk Detector
gap, violation
audit rules
bounded action
Audit Scheduler
budget + cooldown
budget policy
risk flags
no audit
Audit Prompt
step contextaudit call
Feedback Signals
reward, next obs, safety metrics
Interaction Evidence
action changes + audit metrics
action proposal
final action
next obs
reward + info
episode summary
agentic metrics
interaction metrics
Figure 3: Interaction between the reinforcement learning layer and the AI-agent governance layer. The RL policy proposes
market actions, which are bounded by the Planner and conditionally revised by the Auditor under high-risk scenarios.
where𝐺𝑣 𝑡 denotes verified energy supply,𝑄𝑑 𝑡 denotes market de-
mand/load, and𝜖> 0avoids division by zero. Negative values of
Δ𝑎𝑢𝑑𝑖𝑡 𝑡 indicate supply shortfall.
Audit triggers are divided into hard and soft categories. Hard
triggers respond to immediate safety or market-integrity threats, in-
cluding excessive physical violation rate𝜈𝑡 , supply shortfall Δ𝑎𝑢𝑑𝑖𝑡 𝑡 ,
and high static-market slippage𝜎𝑡 :
𝐻𝑡 =I

𝜈𝑡 >𝜏 𝜈 ∨Δ 𝑎𝑢𝑑𝑖𝑡 𝑡 <𝜏 Δ ∨𝜎 𝑡 >𝜏 𝜎  .(10)
Soft triggers capture erratic controller behavior through action
instability:
𝑆𝑡 =I[𝜅𝑡 >𝜏𝜅].(11)
An action becomes audit-eligible when either trigger fires:
𝐸𝑡 =𝐻𝑡∨𝑆𝑡.(12)
To prevent excessive LLM intervention, soft-triggered audits are
rate-limited by the episode budget and cooldown. In contrast, hard
triggers bypass these limits due to their severity. Let𝑁𝑎𝑢𝑑𝑖𝑡 𝑒,𝑡 denote
the number of audits already used in episode𝑒 before step𝑡, and let
𝑡𝑙𝑎𝑠𝑡 𝑒 denote the most recent audited step. The final audit decision is
I𝑎𝑢𝑑𝑖𝑡 𝑡 =𝐸𝑡∧ h 𝐻𝑡 ∨  𝑁𝑎𝑢𝑑𝑖𝑡 𝑒,𝑡 <𝐵 𝑒 ∧𝑡−𝑡 𝑙𝑎𝑠𝑡 𝑒 >𝑐 𝑒 i .(13)
Thus, severe physics or market failures can trigger immediate
review, while softer instability signals are subject to sparse inter-
vention limits.
If I𝑎𝑢𝑑𝑖𝑡 𝑡 = 0, the market directly executes the bounded action
¯𝑎𝑡 . If I𝑎𝑢𝑑𝑖𝑡 𝑡 = 1, the Auditor receives the current observation, the
bounded proposed action, the previous action, the Planner policy,
and recent market diagnostics. It then returns a decision: approve,
which keeps ¯𝑎𝑡 , or revise, which replaces it with a conservative
corrected action. The wrapper deterministically applies this deci-
sion before calling the environment step.
Finally, to make the governance layer auditable and economically
valid, all LLM outputs must follow structured schemas and numeri-
cal validation(Appendix B: Table 9). Planner outputs are clipped to
valid benchmark action ranges and audit-policy ranges. Auditor out-
puts are sanitized against market constraints, including individual
bounds on𝛼𝑡 ,ℓ𝑡 , and𝑏𝑡 , as well as the global allocation constraint
𝛼𝑡+ℓ𝑡≤ 0.98. This schema-enforced interface prevents free-form
text from directly controlling market execution and ensures that ev-
ery agentic intervention remains traceable and reproducible during
evaluation.
3.5 Evaluation Metrics
SolarChain-Evalevaluates each policy from two perspectives: mar-
ket utility and system trustworthiness. We compare six baselines:
Static, Random, Myopic, PPO, SAC, and DQN. Static uses fixed
governance parameters, Random samples actions uniformly, and
Myopic follows a greedy rule based on current supply, demand, and
risk signals. PPO and SAC operate in the continuous action space,
while DQN uses the discretized action grid.
We use three evaluation settings:
• Main Benchmark:evaluates all baselines using the full
reward in Eq. (6). This setting tests whether RL policies can
improve utility while maintaining safety, stability, smooth-
ness, and fairness.
• Reward Ablation:removes the physics penalty from Eq.(6),
while still logging physical violations. This setting tests
whether agents exploit unsafe generation when physical
risk is not penalized.
• Agentic Evaluation:adds the AI-agent governance layer
to trained RL policies during evaluation. This setting tests
whether LLM-based oversight can revise unsafe actions
without retraining the RL controller.

Ou et al.
(a) Rollout-level cumulative reward.
 (b) Utility–safety frontier. Each point is one
rollout; larger markers indicate higher artifi-
cial liquidity.
(c) Episode-wise reward trajectory with 95%
confidence bands across seeds.
Figure 4: Main benchmark performance under the physics-constrained reward.
(a) Physics violation rate.
 (b) Artificial liquidity.
 (c) Mean slippage.
Figure 5: Trustworthiness metrics in the main benchmark. Translucent points are individual rollouts.
Table 3: Trustworthiness-oriented evaluation dimensions
and reported evidence.
Dimension Reported Evidence
Utility Cumulative reward, episode trading volume
Physics Safety Physics violation rate, artificial liquidity
Market Stability Liquidity drawdown, token drawdown, slippage
Action Smoothness Action jitter across hourly decisions
Spatial Fairness City-level reward allocation imbalance
Auditability (Agentic) Plan validity, audit rate, revision rate, action delta
4 Evaluation
Our empirical evaluation addresses the research questions using
data aggregated across three independent seeds. We benchmark
three agentic policies (PPO+LLM, SAC+LLM, DQN+LLM) against
six non-agentic baselines (PPO, SAC, DQN, Static, Random, Myopic).
The evaluation dataset (Appendix B) comprises 1,620 episode-level
records, 38,880 hourly actions, 194,400 hourly state records, and
12,960 LLM governance log entries.
4.1 Benchmark Performance
We first evaluate the RL policies against three baseline models(Static,
Random, Myopic) for market governance. To assess trustworthi-
ness comprehensively, Table 4 reports utility, physical consistency,
and market-execution metrics simultaneously. Results indicate that
learned RL control provides a clear advantage over non-RL baselines.
Across 90 rollouts per policy, the RL policies achieve a higher mean
cumulative reward than the static, random, and myopic baselines
(−22.61vs.−23.97; Welch’s𝑡-test,𝑝< 10−28). This improvement is
primarily driven by continuous-control methods, as both PPO and
SAC outperform all baselines (𝑝< 10−6 for all pairwise tests). No-
tably, these non-RL baselines are non-trivial: they represent stable
governance rules (static), pure action-space exploration (random),
and local rationality (myopic). Their underperformance suggests
that effective market governance requires adaptive RL rather than
rigid or one-step heuristics.
However, trustworthiness metrics reveal a complex utility-safety
tradeoff. While SAC achieves the highest cumulative reward and
trading volume alongside the lowest physics violation rate, it suffers
from the highest mean slippage among the RL policies. Conversely,

SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets
Table 4: Main benchmark performance under the physics-constrained reward. Values are mean ± standard deviation over
all three seeds and 90 rollouts per policy. Higher cumulative reward and trading volume are better; lower physics violation,
slippage, and artificial liquidity indicate safer market governance.
Policy Cumulative Reward Trading Volume Physics Violation Rate Mean Slippage Artificial Liquidity
Static -23.38±0.80 0.514±0.099 0.4874±0.0166 0.0140±0.0020 0.1803±0.0419
Random -25.46±0.91 0.480±0.093 0.4771±0.0172 0.0148±0.0023 0.1137±0.0297
Myopic -23.08±0.80 0.456±0.088 0.4779±0.0168 0.0144±0.0023 0.1009±0.0235
PPO -22.35±1.02 0.470±0.097 0.4520±0.0219 0.0134±0.0023 0.1453±0.0840
SAC -22.26±0.94 0.521±0.100 0.4461±0.0196 0.0178±0.0032 0.0686±0.0328
DQN -23.23±0.91 0.491±0.096 0.4688±0.0182 0.0148±0.0023 0.1298±0.0397
Table 5: Paired without-constraints deltas with and without the LLM governance layer. Each row uses 90 paired rollouts across
three seeds. Positive Δ reward indicates that removing the physics penalty increases scalar utility; positive Δ violation or
artificial liquidity indicates increased safety risk.
Governance PolicyΔRewardΔPhysics ViolationΔArtificial LiquidityΔSlippage
RL PPO 22.61±1.10 0.0311±0.0084 0.0785±0.0678 -0.0012±0.0010
RL SAC 22.52±1.01 0.0412±0.0095 0.1238±0.0386 -0.0041±0.0017
RL DQN 23.55±0.91 0.0182±0.0101 0.0576±0.0317 -0.0018±0.0014
RL+LLM PPO 22.67±1.17 0.0225±0.0107 0.0598±0.0631 -0.0011±0.0016
RL+LLM SAC 22.62±0.96 0.0344±0.0102 0.1149±0.0388 -0.0038±0.0017
RL+LLM DQN 23.78±0.88 0.0081±0.0079 0.0413±0.0317 -0.0015±0.0018
(a) Paired without-constraints artificial-
liquidity deltas for RL and RL+LLM.
(b) Artificial liquidity across RL, RL+LLM, and
their without-constraints ablations.
(c) Episode-wise artificial-liquidity trajecto-
ries for all four learned-agent settings.
Figure 6: Ablation experiment of physics constraints. Translucent points are rollout-level or paired-rollout observations.
PPO offers the lowest slippage but generates more artificial liquid-
ity. DQN improves upon random control but fails to consistently
outperform the myopic baseline, illustrating that RL architecture
choice is critical for fine-grained control tasks. Consequently, these
patterns expose an evaluation frontier. For rigorous trustworthiness
evaluation, maximizing reward does not guarantee a safe policy
if the gain introduces market friction or lacks physical backing.
Figure 4 illustrates this frontier, showing the distinct operational
trade-offs and residual variability within each policy type.
The metric decomposition in Figure 5 further unpacks this fron-
tier. Although RL policies reduce overall physics violations com-
pared to non-RL baselines, the underlying risk is redistributed
across artificial liquidity and slippage. SAC excels at physical credi-
bility, whereas PPO prioritizes slippage control.
4.2 Ablation Experiment of Physics Constraints
The ablation study investigates the necessity of adding physical
constraints to our RL and AI agent models. We examine four con-
figurations: standard RL, RL without physics constraints, RL with
LLM governance, and RL with LLM governance but lacking physics
constraints. In the unconstrained settings, we remove the physics
penalty from the reward function(Eq.6) while continuing to track
physical violations and artificial liquidity. This design decouples
the agent’s optimization objective from the benchmark’s safety

Ou et al.
Table 6: Paired effects of adding the LLM Planner/Auditor layer under the physics-constrained reward. Δ columns are RL+LLM
minus RL over 90 matched rollouts across three seeds; audit and revision rates are computed from 2,160 governance log steps
per policy.
PolicyΔRewardΔAction JitterΔArtificial LiquidityΔSpatial Fairness Audit Rate Revision Rate
PPO -0.094±0.293 0.0223±0.0154 -0.0074±0.0216 0.0004±0.0008 0.344 0.961
SAC -0.062±0.268 -0.0290±0.0198 0.0073±0.0110 0.0003±0.0006 0.342 0.966
DQN -0.277±0.503 -0.0179±0.0274 0.0109±0.0252 -0.0002±0.0021 0.372 0.958
(a) Action stability: RL+LLM reduces action
jitter for SAC and DQN,
(b) Paired RL+LLM-minus-RL changes in ac-
tion jitter and artificial liquidity.
(c) Step-level relationship between pre-audit
action jitter and Auditor action delta.
Figure 7: Agentic governance diagnostics for the LLM Planner/Auditor layer. The panels combine summary auditability statistics,
paired episode-level governance effects, and step-level audit traces.
diagnostics. Consequently, scalar reward maximization does not
inherently equate to a better market outcome. If an agent boosts its
reward by backing invalid supply and inflating apparent liquidity,
the benchmark can explicitly expose it.
The empirical results in Table 5 demonstrate that removing the
physics penalty inflates scalar rewards, but at the cost of severe
safety risks. Under raw RL deployment, artificial liquidity surges
by 0.0785, 0.1238, and 0.0576 MWh for PPO, SAC, and DQN, respec-
tively. This failure mode persists even under RL+LLM deployment,
where artificial liquidity still increases by 0.0598, 0.1149, and 0.0413
MWh. This illustrates a consistent shift toward higher artificial liq-
uidity when constraints are ablated across both governance regimes
(Figure 6a). Although the LLM layer mitigates the magnitude of
these violations, it cannot eliminate the misalignment caused by a
misspecified reward.
This comparison highlights the complementary roles of physical
constraints and AI agent governance. While LLM governance au-
dits actions post-hoc, physics-constrained RL embeds safety during
optimization to prevent the exploitation of unviable liquidity. Ag-
gregated across learned policies, mean artificial liquidity remains
low in constrained environments (0.1146 MWh for RL; 0.1181 MWh
for RL+LLM) but spikes in unconstrained settings (0.2012 MWh
for RL; 0.1901 MWh for RL+LLM) (Figure 6b). Furthermore, this
risk inflation is not an artifact of isolated rollouts, but a persistent
behavioral trajectory woven throughout the evaluation episodes
(Figure 6c). This confirms that unconstrained optimization remains
riskier, even with active agentic oversight.
4.3 Evaluation of Agentic Layer
Having proven the function of physics constraints, we now evaluate
the AI agent layer’s capacity for verifiable oversight. By analyz-
ing transparent audit traces from market execution, we assess the
system’s effectiveness as an auditable risk-control interface. This
evaluation specifically quantifies intervention triggers, the mag-
nitude of action modifications, and the underlying rationales for
these corrections.
To investigate the reliability of the AI agent mechanism, Ta-
ble 6 presents metrics derived from 12,960 step-level governance
logs (encompassing three seeds, two constraint settings, and three
learned policies). The system demonstrates exceptional reliability,
with a Planner validity of 1.0 across all configurations. Notably,
the evaluation reveals that effective oversight is highly selective
rather than continuous. Under the physics-constrained setting, the
Auditor intervenes in 34.2%–37.2% of steps, whereas in the uncon-
strained setting, the intervention rate is 27.3%–29.7%. The Auditor
revises proposed actions in over 95% of cases under constraints,
and over 83% without constraints.
The empirical results suggest that agentic governance functions
as an auditable risk-control interface rather than a universal perfor-
mance optimizer. Its impact is highly dependent on the behavioral
characteristics of the base RL policy. For instance(Figure7a), the
LLM layer successfully suppresses action jitter for SAC and DQN by
0.0290 and 0.0179, respectively. Conversely, it marginally increases
PPO jitter by 0.0223, primarily due to more frequent clipping and tar-
geted revisions of PPO’s proposed actions. Similar policy-dependent
trade-offs emerge in artificial liquidity: oversight reduces it for PPO

SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets
Table 7: Representative LLM audit trace selected from
agentic_logs.jsonl. The row records the market context,
proposed RL action, audited final action, and action delta.
Field Value
policy / setting PPO / LLM No-physics
Episode and step Episode 6, step 15, hour 15
Trigger context raw violation 0.14; gap 1.97; static slippage 0.72
RL proposed action r=0.049, l=0.931, b=0.200
Audited final action r=0.050, l=0.200, b=0.000
Action delta 0.932
Auditor rationale Violation rate exceeds audit threshold; tighten
allocation to limit exposure to unsafe backed sup-
ply.
(a) Selected action revision.
 (b) Context of audited PPO steps.
Figure 8: Case-study audit trace for PPO under the LLM gov-
ernance setting.
(−0.0074MWh) but slightly increases it for SAC (+0.0073MWh)
and DQN (+0.0109MWh). Spatial fairness remains largely stable,
with minimal deltas across all policies(Figure 7b).
These mixed outcomes reveal that researchers should not assume
that deploying an LLM governance layer automatically resolves
all safety risks. Instead, it must rigorously define the boundaries
of such oversight. Within the decentralized energy market setting,
SolarChain-Evaldemonstrates that while the AI agent successfully
intercepts unstable decisions, as evidenced by the positive corre-
lation between pre-audit action jitter and the corrective delta in
Figure 7c, it cannot fully compensate for a misspecified RL reward.
Ultimately, our findings advocate for a complementary approach
to trustworthy autonomous systems. While agentic governance
guarantees post-deployment transparency and event-driven risk
mitigation, physically constrained RL optimization remains neces-
sary to prevent reward-driven exploitation.
4.4 Case Study: Transparent LLM Audit Trace
To illustrate the transparency of our evaluation, we analyze a rep-
resentative audit trace (Table 7). We select a scenario where the
PPO agent operates without physical constraints, a setting where
reward misspecification inherently encourages risky market behav-
ior. At the evaluated step, environmental risk signals are elevated,
including a raw physics violation rate of 0.14 and a supply gap of
1.97.
Driven by economic utility, the RL policy proposes an aggressive,
high-liquidity action(𝑟= 0.049,𝑙= 0.931,𝑏= 0.200). Recogniz-
ing the safety breach, the LLM Auditor intervenes and revises the
action to a conservative bound (𝑟= 0.050,𝑙= 0.200,𝑏= 0.000),
resulting in a substantial action delta of 0.932 (Figure 8b). Beyond
the numerical correction, the physical violation rate exceeded the
safety threshold, necessitating a tighter liquidity allocation to limit
exposure to unsafe supply.
This case validates the contribution of the agentic layer to trust-
worthy evaluation.SolarChain-Evalrecords the entire decision-
making process. It explicitly documents the activating risk signals,
the resulting action adjustments, and the auditor’s natural language
rationale. By providing this transparency,SolarChain-Evalguar-
antees that autonomous interventions remain accountable after
deployment.
5 Conclusion
In conclusion, we proposedSolarChain-Eval, a physics-constrained
benchmark designed to evaluate the trustworthiness of economic
agents in decentralized energy markets. Our empirical evaluations
reveal a clear trade-off inherent in autonomous market governance.
While RL policies improve economic utility relative to static and
heuristic rules, they may compromise safety for market efficiency.
This vulnerability is starkly exposed when physical constraints
are removed: driven purely by reward maximization, an RL policy
may exploit false data injection attacks to artificially inflate market
liquidity. To counter this flaw, combining physical constraints with
an AI-agent governance layer provides a structured and auditable
safety interface. By evaluating context and intercepting high-risk
decisions, the AI-agent layer creates transparent intervention traces
and can mitigate instability patterns, although its corrective im-
pact remains policy-dependent and bounded by the underlying RL
controller.
The deployment of autonomous agents in cyber-physical systems
requires evaluation paradigms that look beyond standard reward
maximization.SolarChain-Evaladdresses this gap by logging the
complete decision loop, including environmental risk signals, action
corrections, and natural language explanations. Consequently, our
benchmark supports deployment-oriented stress tests in which
agent behaviors remain economically viable, verifiable, accountable,
and physically grounded.
Future work will makeSolarChain-Evalbroader and more diag-
nostic. We will test whether the utility–safety–stability–fairness–
auditability template transfers to autonomous trading and supply-
chain allocation by replacing the PV physics oracle with domain-
specific feasibility or risk checks. We will also calibrate the simulator
with broader meteorological and market traces and run sensitivity
analyses over reward weights, FDIA frequency and severity, node
scale, and market-clearing assumptions. For the Planner/Auditor,
we will measure selectivity with safe-action holdouts, approval-only
controls, false-positive and false-negative rates, and trigger-level
ablations, separating meaningful risk detection from overly con-
servative defaults. Finally, we will compareSolarChain-Evalwith
constrained-RL and agentic-benchmark baselines to clarify when
post-hoc governance helps and when reward misspecification must
be addressed during training.

Ou et al.
References
[1] Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel. 2017. Constrained
policy optimization. InInternational conference on machine learning. PMLR, 22–
31.
[2] Mohammad Hossein Nejati Amiri, Fawaz Annaz, Mario De Oliveira, and Flo-
rimond Gueniat. 2025. Deep Reinforcement Learning with Local Interpretabil-
ity for Transparent Microgrid Resilience Energy Management.arXiv preprint
arXiv:2508.08132(2025).
[3] Gustavo Campos, Nael H El-Farra, and Ahmet Palazoglu. 2022. Soft actor-critic
deep reinforcement learning with hybrid mixed-integer actions for demand
responsive scheduling of energy systems.Industrial & Engineering Chemistry
Research61, 24 (2022), 8443–8461.
[4] Thomas Carta, Clément Romac, Thomas Wolf, Sylvain Lamprier, Olivier Sigaud,
and Pierre-Yves Oudeyer. 2023. Grounding large language models in interactive
environments with online reinforcement learning. InInternational Conference on
Machine Learning. PMLR, 3676–3713.
[5] T. Chen, S. Bu, X. Liu, J. Kang, F. R. Yu, and Z. Han. 2022. Peer-to-peer energy
trading and energy conversion in interconnected multi-energy microgrids using
multi-agent deep reinforcement learning.IEEE Transactions on Smart Grid13, 1
(2022), 715–727.
[6] Lin William Cong, Ye Li, and Neng Wang. 2021. Tokenomics: Dynamic adoption
and valuation.The Review of Financial Studies34, 3 (2021), 1105–1155.
[7] Jan Drgona, Truong X. Nghiem, Thomas Beckers, Mahyar Fazlyab, Enrique
Mallada, Colin Jones, Draguna Vrabie, Steven L. Brunton, and Rolf Findeisen.
2025. Safe Physics-informed Machine Learning for Dynamics and Control. In
Proceedings of the American Control Conference.
[8] Yuqing Du, Olivia Watkins, Zihan Wang, Cédric Colas, Trevor Darrell, Pieter
Abbeel, Abhishek Gupta, and Jacob Andreas. 2023. Guiding pretraining in
reinforcement learning with large language models. InInternational Conference
on Machine Learning. PMLR, 8657–8677.
[9] Gabriel Dulac-Arnold, Nir Levine, Daniel J Mankowitz, Jerry Li, Cosmin Padu-
raru, Todd Hester, et al. 2021. Challenges of real-world reinforcement learning:
definitions, benchmarks and analysis.Machine Learning110, 9 (2021), 2419–2468.
[10] Shangding Gu et al. 2024. A Review of Safe Reinforcement Learning: Methods,
Theory and Applications.IEEE Transactions on Pattern Analysis and Machine
Intelligence(2024).
[11] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. 2018. Soft
actor-critic: Off-policy maximum entropy deep reinforcement learning with a
stochastic actor. InInternational conference on machine learning. PMLR, 1861–
1870.
[12] Adrian Kelly, Aidan O’Sullivan, Patrick de Mars, and Antoine Marot. 2020. Rein-
forcement learning for electricity network operation. InElectric Power Systems
Research, Vol. 189. Elsevier, 106740.
[13] Minae Kwon, Sang Michael Xie, Kalesha Bullard, and Dorsa Sadigh. 2023. Re-
ward design with language models. InThe Eleventh International Conference on
Learning Representations.
[14] Yao Liu, Peng Ning, and Michael K Reiter. 2011. False data injection attacks
against state estimation in electric power grids.ACM Transactions on Information
and System Security (TISSEC)14, 1 (2011), 1–33.
[15] Daniela Rojas Lozano and Yuanyuan Shi. 2025. Democratizing microgrid opti-
mization: An llm agent for dispatching mobile chargers to construction electric
vehicles. InNeurIPS 2025 Workshop on Bridging Language, Agent, and World
Models for Reasoning and Planning.
[16] Yecheng Jason Ma, William Liang, Guanzhi Wang, De-An Huang, Osbert Bastani,
Dinesh Jayaraman, Yuke Zhu, Linxi Fan, and Anima Anandkumar. 2023. Eureka:
Human-level reward design via coding large language models. InThe Twelfth
International Conference on Learning Representations.
[17] Katya Malinova and Andreas Park. 2023. Tokenomics: When Tokens Beat Equity.
Management Science69, 11 (2023), 6568–6583.
[18] Esther Mengelkamp, Johannes Gärttner, Kerstin Rock, Scott Kessler, Lawrence
Orsini, and Christof Weinhardt. 2018. Designing microgrid energy markets: A
case study: The Brooklyn Microgrid.Applied Energy210 (2018), 870–880.
[19] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Veness,
Marc G Bellemare, Alex Graves, Martin Riedmiller, Andreas K Fidjeland, Georg
Ostrovski, et al. 2015. Human-level control through deep reinforcement learning.
nature518, 7540 (2015), 529–533.
[20] National Institute of Standards and Technology. 2023.Artificial Intelligence Risk
Management Framework (AI RMF 1.0). Technical Report NIST AI 100-1. National
Institute of Standards and Technology. doi:10.6028/NIST.AI.100-1
[21] Shilin Ou, Yifan Xu, Zhenshan Zhang, Luyao Zhang, and Ming-Chun Huang.
2026. SolarChain: Bridging Physical Law, Verifiable Trust, and Sustainable
Markets for Urban Energy Resilience.arXiv preprint arXiv:2605.23162(2026).
[22] Charles Chimwemwe Phiri. 2025. Creating Characteristically Auditable Agentic
AI Systems. InProceedings of the Intelligent Robotics FAIR 2025. ACM. doi:10.
1145/3759355.3759356
[23] Hanxiao Qu, Krzysztof M Gogol, Florian Grötschla, and Claudio J Tessone. 2025.
From Rules to Rewards: Reinforcement Learning for Interest Rate Adjustment
in DeFi Lending. InThe International Conference on Mathematical Research for
Blockchain Economy. Springer, 85–120.
[24] Antonin Raffin, Ashley Hill, Adam Gleave, Anssi Kanervisto, Maximilian Ernes-
tus, and Noah Dormann. 2021. Stable-Baselines3: Reliable Reinforcement Learn-
ing Implementations.Journal of Machine Learning Research22, 268 (2021), 1–8.
[25] Cynthia Rudin. 2019. Stop explaining black box machine learning models for
high stakes decisions and use interpretable models instead.Nature machine
intelligence1, 5 (2019), 206–215.
[26] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.
2017. Proximal policy optimization algorithms.arXiv preprint arXiv:1707.06347
(2017).
[27] Wayes Tushar, Chau Yuen, Hamed Mohsenian-Rad, Tapan Saha, H Vincent
Poor, and Kristin L Wood. 2018. Transforming energy networks via peer-to-
peer energy trading: The potential of game-theoretic approaches.IEEE Signal
Processing Magazine35, 4 (2018), 90–111.
[28] Hado Van Hasselt, Arthur Guez, and David Silver. 2016. Deep reinforcement
learning with double q-learning. InProceedings of the AAAI conference on artificial
intelligence, Vol. 30.
[29] Javal Vyas and Mehmet Mercangöz. 2025. Autonomous industrial control using
an agentic framework with large language models.IFAC-PapersOnLine59, 6
(2025), 349–354.
[30] Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming
Zhang, Junzhe Wang, Senjie Jin, Enyu Zhou, et al. 2025. The rise and potential of
large language model based agents: A survey.Science China Information Sciences
68, 2 (2025), 121101.
[31] Jiahua Xu, Yebo Feng, Daniel Perez, and Benjamin Livshits. 2025. Auto. gov:
learning-based governance for decentralized finance (DeFi).IEEE Transactions
on Services Computing(2025).
[32] Haolan Yang, Zhengbo Li, Youbo Liu, Yue Xiang, Lingtao Li, Jianping Yang, Ling
Tan, Shiqian Wang, Huangqi Ma, Zirui Xi, et al. 2025. LLM-powered distributed
optimal scheduling for industrial heat-electricity micro-grids.IEEE Transactions
on Industry Applications(2025).
[33] Xu Yang, Chenhui Lin, Haotian Liu, and Wenchuan Wu. 2025. RL2: Reinforce
Large Language Model to Assist Safe Reinforcement Learning for Energy Man-
agement of Active Distribution Networks.IEEE Transactions on Smart Grid
(2025).
[34] Changwei Yao, Xinzi Liu, Chen Li, and Marios Savvides. 2025. Reward Evo-
lution with Graph-of-Thoughts: A Bi-Level Language Model Framework for
Reinforcement Learning.arXiv preprint arXiv:2509.16136(2025).
[35] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan,
and Yuan Cao. 2022. React: Synergizing reasoning and acting in language models.
arXiv preprint arXiv:2210.03629(2022).
[36] Dongxia Zhang, Xiaoqing Han, and Chunyu Deng. 2018. Review on the research
and practice of deep learning and reinforcement learning in smart grids.CSEE
Journal of Power and Energy Systems4, 3 (2018), 362–370.
[37] Stephan Zheng, Alexander Trott, Sunil Srinivasa, David C Parkes, and Richard
Socher. 2022. The AI Economist: Taxation policy design via two-level deep
multiagent reinforcement learning.Science advances8, 18 (2022), eabk2607.

SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets
A Formulas Implementation
This appendix lists some important equations used by the released
SolarChain-Evalcode but not separately expanded in the methodol-
ogy section.
PV capacity and trust labels.The data generator converts weather
into a physical PV upper bound and the loader derives the trust
labels used by the benchmark:
𝐼𝑐,𝑡 =I[𝑧 𝑐,𝑡 <90◦]min{max(𝑆 𝑐,𝑡,0),1.08 max(𝐶 𝑐,𝑡,0)},
𝜂𝑡𝑒𝑚𝑝 𝑖,𝑡 =clip{1+𝛾 𝑖(𝑇𝑐,𝑡−25),0.78,1.08},
𝑃𝑚𝑎𝑥 𝑖,𝑡 =max{0,𝐼 𝑐,𝑡𝐴𝑖𝜂𝑖𝜂𝑡𝑒𝑚𝑝 𝑖,𝑡 },
𝐺𝑣 𝑖,𝑡 =I[status 𝑖,𝑡 =verified]𝑃 𝑟𝑒𝑝𝑜𝑟𝑡𝑒𝑑 𝑖,𝑡 ,
𝑋𝑒𝑥𝑐𝑒𝑠𝑠 𝑖,𝑡 =max(𝑃 𝑟𝑒𝑝𝑜𝑟𝑡𝑒𝑑 𝑖,𝑡 −𝑃 𝑚𝑎𝑥 𝑖,𝑡 ,0),
viol𝑖,𝑡 =I[𝑋 𝑒𝑥𝑐𝑒𝑠𝑠 𝑖,𝑡 >10−6∨FDIA𝑖,𝑡],
𝑅𝑟𝑒𝑗𝑒𝑐𝑡𝑒𝑑 𝑖,𝑡 =viol𝑖,𝑡𝑃𝑟𝑒𝑝𝑜𝑟𝑡𝑒𝑑 𝑖,𝑡 .
(14)
Action decoding and allocation budget.Continuous policy outputs
are decoded into governance ratios and then sanitized against the
global allocation budget:
𝛼𝑡 =𝛼 min+𝑢𝑡,1(𝛼max−𝛼 min),
ℓ𝑡 =ℓ min+𝑢𝑡,2(ℓmax−ℓ min),
𝑏𝑡 =𝑢𝑡,3𝑏max,
𝑠𝑡 =min

1, 0.98 𝛼𝑡+ℓ𝑡

,
(𝛼𝑡,ℓ𝑡)←(𝑠 𝑡𝛼𝑡,𝑠𝑡ℓ𝑡).
(15)
DQN uses the same decoder after selecting one point from a5 3 =
125normalized action grid.
Unsafe supply, artificial liquidity, and market clearing.The im-
plementation records how much invalid supply is economically
backed and how much liquidity it creates:
𝑋𝑡 =max
(∑︁
𝑖
𝑅𝑟𝑒𝑗𝑒𝑐𝑡𝑒𝑑 𝑖,𝑡 , ∑︁
𝑖
𝑋𝑒𝑥𝑐𝑒𝑠𝑠 𝑖,𝑡 ,
max
∑︁
𝑖
𝑃𝑟𝑒𝑝𝑜𝑟𝑡𝑒𝑑 𝑖,𝑡 − ∑︁
𝑖
𝑃𝑚𝑎𝑥 𝑖,𝑡 ,0 ) ,
𝛽𝑡 = min(𝛼𝑡+ℓ𝑡,0.98) 0.98 ,
𝐴𝑢𝑛𝑠𝑎𝑓𝑒 𝑡 =𝛽 𝑡𝑋𝑡,
𝐺𝑏𝑎𝑐𝑘𝑒𝑑 𝑡 =𝐺 𝑣 𝑡+𝐴𝑢𝑛𝑠𝑎𝑓𝑒 𝑡 ,
𝐴𝑎𝑟𝑡𝑖𝑓𝑖𝑐𝑖𝑎𝑙 𝑡 =ℓ𝑡𝐴𝑢𝑛𝑠𝑎𝑓𝑒 𝑡 .
(16)
The executed market transition is then
e𝑄𝑡 =𝑄𝑑 𝑡 max(0.75,1−0.80𝑏 𝑡),
𝐿𝑎𝑣𝑎𝑖𝑙 𝑡 =𝐿𝑡+ℓ𝑡𝐺𝑏𝑎𝑐𝑘𝑒𝑑 𝑡 ,
𝑀𝑡 =min(𝐿 𝑎𝑣𝑎𝑖𝑙 𝑡 , e𝑄𝑡),
𝐿𝑡+1 =max(𝐿 𝑎𝑣𝑎𝑖𝑙 𝑡 −𝑀𝑡,0),
𝜎𝑒𝑥𝑒𝑐 𝑡 = e𝑄𝑡 max(𝐿𝑎𝑣𝑎𝑖𝑙 𝑡 +0.05,0.05) .
(17)
Episode, fairness, and audit metrics.The evaluation code aggre-
gates step records into rollout-level metrics:
𝑅𝑒 =
∑︁
𝑡∈𝑒
𝑅𝑡,
𝑉𝑒 = 1 24 ∑︁ 𝑡∈𝑒 𝑉𝑡,
𝐽𝑒 = 1 23 24∑︁ 𝑡=2 ∥𝑎𝑡−𝑎𝑡−1∥1,
¯𝜎𝑒 = 1 24 ∑︁ 𝑡∈𝑒 𝜎𝑒𝑥𝑒𝑐 𝑡 ,
𝐴𝑎𝑟𝑡𝑖𝑓𝑖𝑐𝑖𝑎𝑙 𝑒 = ∑︁
𝑡∈𝑒
𝐴𝑎𝑟𝑡𝑖𝑓𝑖𝑐𝑖𝑎𝑙 𝑡 .
(18)
City-level reward imbalance and agentic intervention strength are
reported as
𝐹𝑒 =
Var𝑐
˝
𝑡∈𝑒 𝑟𝑐𝑖𝑡𝑦 𝑐,𝑡 
max

1
|𝐶|
˝
𝑐

˝ 𝑡∈𝑒 𝑟𝑐𝑖𝑡𝑦 𝑐,𝑡

,10−9 ,
𝛿𝑡 =∥𝑎 𝑓𝑖𝑛𝑎𝑙 𝑡 −𝑎𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙 𝑡 ∥1,
audit_rate= 𝑁𝑎𝑢𝑑𝑖𝑡
24 ,
revision_rate= 𝑁𝑟𝑒𝑣𝑖𝑠𝑒
max(𝑁𝑎𝑢𝑑𝑖𝑡,1) .
(19)
B Data Provenance and Evaluation Matrix
Table 8 summarizes the benchmark input data used in this pa-
per and documents the provenance of each raw file before policy
evaluation. The primary dataset is a benchmark instance cover-
ing Beijing, Shanghai, Chengdu, Shenzhen, and Hangzhou from
2026-04-01 to 2026-05-01. It contains 720 hourly timestamps and
integrates cached city-level weather, node-level PV parameters, re-
ported generation records, FDIA and verification labels, aggregate
market-liquidity states, and generated P2P transaction traces.
The evaluation artifacts reported in the paper are derived from
these raw inputs through a fixed evaluation pipeline. The stored evi-
dence records outcomes at multiple granularities, including episode-
level metrics for rollout rewards and safety outcomes, hourly action
rows for executed policy decisions, city-hour policy rows for spa-
tial market states, violation, and fairness calculations, and LLM
governance logs for Planner/Auditor decisions. Overall, the evalua-
tion matrix contains 1,620 episode-level metric rows, 38,880 hourly
action rows, 194,400 city-hour policy rows, and 12,960 LLM gover-
nance log rows.

Ou et al.
Table 8: Raw benchmark data files and collection or generation methods. Row counts exclude CSV headers.
File Rows Key fields Collection or generation method
open_meteo_weather.json5 city payloads hourly time, temperature, short-
wave radiation, latitude, longi-
tude, timezone
Retrieved by generate_monthly_datasets.py
from the Open-Meteo Historical Weather API
for Beijing, Shanghai, Chengdu, Shenzhen, and
Hangzhou; cached locally and reused on later
runs.
urban_energy_nodes.csv50 node id, city, latitude, longitude,
panel area, efficiency, temperature
coefficient, install date
Generated with seed 20260511: 10 nodes per
city, coordinates jittered around city centers,
panel areas sampled from 18–64 m 2, efficien-
cies from 0.176–0.226, temperature coefficients
from -0.0046 to -0.0032, and install dates from
2020-01-01 to 2024-05-31.
spatiotemporal_generation.csv36,000 timestamp, node id, city, irradi-
ance, air temperature, 𝑃𝑚𝑎𝑥 , re-
ported power, FDIA flag, verifica-
tion status
Generated hourly for 50 nodes over 720 hours
from cached weather, pvlib clear-sky and solar-
position calculations, node-specific PV param-
eters, inverter derate, and noise. Exactly 1,800
rows are FDIA-injected and marked rejected.
market_liquidity.csv720 timestamp, total verified MW, So-
larChain liquidity, baseline liquid-
ity, SolarChain slippage, baseline
slippage
Aggregated from verified generation. The imple-
mentation uses𝐿𝑆𝐶 = 0.92𝐺𝑣+ 0.018,𝐿𝑏𝑎𝑠𝑒 =
0.61𝐺𝑣+ 0.008,𝜎𝑆𝐶 = 0.18/(𝐿𝑆𝐶+ 0.045), and
𝜎𝑏𝑎𝑠𝑒 =0.31/(𝐿 𝑏𝑎𝑠𝑒+0.028).
p2p_trades.csv1,185 trade id, timestamp, factory id,
city, energy purchased, tokens
burned, exergy dissipated
Generated for daylight hours with positive ver-
ified supply. Each active hour can create up to
three factory purchases; purchase size is the
minimum of a SolarChain-liquidity share and a
verified-generation share, with token burn and
exergy fields sampled from configured multipli-
ers.
Table 9: Reproducibility protocol for the LLM Planner/Auditor layer.
Component Specification
LLM configuration Both Planner and Auditor use a fixed model,ChatGPT 5.5 mini , specified before evaluation and held constant across
seeds, policies, episodes, and steps. The LLM is used only at evaluation time and is not involved in RL training.
Prompting Planner and Auditor use fixed system/user prompt templates released with the code. The templates are unchanged
across runs; only the episode-level or step-level context is substituted into the prompt.
Planner output schema The Planner is called once per episode and must return governance_mode, action_bounds, audit_policy, and
rationale. Bounds cover𝛼𝑡 ,ℓ𝑡 , and𝑏𝑡 ; the audit policy specifies trigger thresholds, budget, target audit rate, and
cooldown.
Auditor output schema The Auditor is called only for scheduler-eligible steps and must return decision, final_action, risk_assessment,
andreason. The decision is restricted toapproveorrevise.
Decoding and validation Structured-output parsing is used first; the chat JSON-schema fallback usestemperature=0. All outputs are parsed by
strict schemas with extra fields forbidden. Valid numerical outputs are clipped and sanitized to benchmark constraints,
including𝛼 𝑡+ℓ 𝑡≤0.98.
Failure handling Missing, unparsable, or schema-invalid LLM outputs fail the LLM evaluation run rather than being silently executed
or replaced by free-form text.
Execution and logging Execution depends only on validated structured fields: approve keeps the bounded RL action, while revise executes
the validated final_action. Natural-language rationales are logged for audit evidence but do not control execution.
Determinism and baseline RL and environment seeds are fixed, but hosted LLM calls are not assumed to be bitwise deterministic. All accepted
Planner/Auditor outputs are logged. A rule-based Planner/Auditor baseline uses the same scheduler, sanitizer, budget,
cooldown, and logging interface.

SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets
Table 10: Detailed main-setting episode summaries. Reward, volume, violation, artificial liquidity, slippage, and action jitter are
aggregated over 90 rollouts per policy.
Policy Rollouts Reward Mean Reward Min Reward Max Volume Violation Mean Violation Range Artificial Liquidity
DQN 90 -23.23 -24.97 -21.00 0.491 0.4688 0.4270–0.5048 0.1298
Myopic 90 -23.08 -24.60 -21.39 0.456 0.4779 0.4434–0.5136 0.1009
PPO 90 -22.35 -24.20 -20.14 0.470 0.4520 0.4060–0.4912 0.1453
Random 90 -25.46 -27.34 -23.28 0.480 0.4771 0.4395–0.5147 0.1137
SAC 90 -22.26 -24.28 -20.15 0.521 0.4461 0.4083–0.4879 0.0686
Static 90 -23.38 -24.86 -21.65 0.514 0.4874 0.4527–0.5218 0.1803
Table 11: Four-setting summaries for learned policies. Each row aggregates 90 rollouts across three seeds. These values support
the paired physics-removal deltas and show how the LLM governance layer changes the setting-level risk profile.
Setting Policy Rollouts Reward Violation Artificial Liquidity Slippage Jitter Fairness
RL PPO 90 -22.35 0.4520 0.1453 0.0134 0.0607 0.0041
RL SAC 90 -22.26 0.4461 0.0686 0.0178 0.1435 0.0048
RL DQN 90 -23.23 0.4688 0.1298 0.0148 0.1118 0.0159
RL+LLM PPO 90 -22.44 0.4571 0.1379 0.0141 0.0829 0.0045
RL+LLM SAC 90 -22.32 0.4527 0.0759 0.0175 0.1145 0.0051
RL+LLM DQN 90 -23.51 0.4780 0.1406 0.0146 0.0939 0.0157
RL no-physics PPO 90 0.27 0.4831 0.2238 0.0122 0.0135 0.0053
RL no-physics SAC 90 0.26 0.4874 0.1925 0.0137 0.0432 0.0109
RL no-physics DQN 90 0.32 0.4869 0.1874 0.0129 0.0259 0.0119
RL+LLM no-physics PPO 90 0.22 0.4796 0.1977 0.0130 0.0366 0.0055
RL+LLM no-physics SAC 90 0.30 0.4870 0.1908 0.0137 0.0362 0.0109
RL+LLM no-physics DQN 90 0.27 0.4862 0.1820 0.0132 0.0342 0.0119
Table 12: Aggregate learned-policy means by setting. Each row averages PPO, SAC, and DQN over the same 270 rollouts. The
no-physics settings remain substantially higher in artificial liquidity even when LLM governance is active.
Setting Reward Violation Artificial Liquidity Slippage Jitter Fairness
RL -22.61 0.4557 0.1146 0.0153 0.1053 0.0083
RL+LLM -22.76 0.4626 0.1181 0.0154 0.0971 0.0084
RL no-physics 0.28 0.4858 0.2012 0.0129 0.0275 0.0094
RL+LLM no-physics 0.26 0.4843 0.1901 0.0133 0.0357 0.0094
Table 13: Detailed LLM governance operation rates. Each row aggregates 2,160 agentic log steps from three seeds. The LLM
failure count is zero for every row and is therefore not shown.
Setting Policy Steps Audit Rate Revision Given Audit Modification Rate Mean ActionΔNot Triggered
Main DQN 2160 0.372 0.958 0.518 0.084 0.488
Main PPO 2160 0.344 0.961 0.987 0.164 0.550
Main SAC 2160 0.342 0.966 0.524 0.059 0.509
No-physics DQN 2160 0.297 0.892 0.490 0.042 0.683
No-physics PPO 2160 0.273 0.832 0.991 0.111 0.691
No-physics SAC 2160 0.274 0.876 0.294 0.021 0.698

Ou et al.
Table 14: Detailed LLM post-hoc trigger diagnostics and mean Planner thresholds. Trigger columns report the fraction of logged
steps satisfying each trigger condition.
Setting Policy Physics Trig. Gap Trig. Slippage Trig. Jitter Trig. Viol. Thr. Gap Thr. Jitter Thr. Slip Thr.
Main DQN 0.120 0.440 0.168 0.230 0.141 -0.108 0.177 2.960
Main PPO 0.121 0.440 0.171 0.171 0.142 -0.112 0.174 2.961
Main SAC 0.120 0.441 0.137 0.211 0.142 -0.102 0.175 3.061
No-physics DQN 0.116 0.441 0.170 0.049 0.143 -0.099 0.170 3.028
No-physics PPO 0.113 0.441 0.126 0.078 0.144 -0.103 0.185 3.140
No-physics SAC 0.105 0.441 0.145 0.048 0.146 -0.102 0.181 3.111
Table 15: Paired episode-level effects of adding the LLM Planner/Auditor layer. Deltas are computed as RL+LLM minus raw RL
under matched seed, policy, and episode.
Comparison PolicyΔRewardΔAction JitterΔSpatial FairnessΔArtificial LiquidityΔSlippage
Main DQN -0.277±0.503 -0.0179±0.0274 -0.0002 0.0109 -0.0001
Main PPO -0.094±0.293 0.0223±0.0154 0.0004 -0.0074 0.0007
Main SAC -0.062±0.268 -0.0290±0.0198 0.0003 0.0073 -0.0003
No-physics DQN -0.045±0.065 0.0083±0.0110 0.0000 -0.0054 0.0002
No-physics PPO -0.043±0.097 0.0231±0.0166 0.0002 -0.0261 0.0008
No-physics SAC 0.038±0.089 -0.0070±0.0154 0.0000 -0.0017 0.0000
Table 16: Step-level action distributions for learned policies. Each cell reports mean with 5th–95th percentile range in parenthe-
ses.
Setting Policy Reward Ratio Liquidity Ratio Burn Rate
Main DQN 0.320 (0.050–0.500) 0.517 (0.200–0.762) 0.081 (0.000–0.150)
Main PPO 0.050 (0.049–0.050) 0.401 (0.200–0.931) 0.104 (0.000–0.200)
Main SAC 0.169 (0.058–0.432) 0.433 (0.212–0.738) 0.008 (0.001–0.028)
No-physics DQN 0.216 (0.049–0.308) 0.759 (0.672–0.931) 0.080 (0.000–0.200)
No-physics PPO 0.049 (0.049–0.050) 0.850 (0.200–0.931) 0.045 (0.000–0.200)
No-physics SAC 0.215 (0.079–0.363) 0.764 (0.617–0.898) 0.011 (0.002–0.025)
LLM Main DQN 0.321 (0.050–0.500) 0.575 (0.250–0.762) 0.070 (0.000–0.150)
LLM Main PPO 0.065 (0.050–0.124) 0.480 (0.250–0.900) 0.071 (0.000–0.150)
LLM Main SAC 0.166 (0.060–0.402) 0.470 (0.250–0.747) 0.009 (0.001–0.027)
LLM No-physics DQN 0.217 (0.050–0.350) 0.746 (0.500–0.900) 0.069 (0.000–0.150)
LLM No-physics PPO 0.062 (0.050–0.100) 0.799 (0.250–0.900) 0.028 (0.000–0.150)
LLM No-physics SAC 0.212 (0.083–0.343) 0.764 (0.634–0.888) 0.011 (0.002–0.025)
