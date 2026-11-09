---
title: 'Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning'
url: https://arxiv.org/abs/2606.27483
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Xuan Zhang
- Zhijian Zhou
- Lingfeng Qiao
- Yulei Qin
- Ke Li
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.27483
pages: 50
chars: 124091
fetched_at: '2026-11-08T13:36:23+00:00'
kb_version: 1
---

# Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning

World Model Agentic Training
Internalizing the Future: A Unified Agentic Training
Paradigm for World Model Planning
Xuan Zhang1,2,3, Zhijian Zhou 1,2,3, Lingfeng Qiao 3, Yulei Qin 3, Ke Li 3, Xing Sun 3, Xiaoyu Tan 3†, Chao
Qu1†, Yuan Qi 1†
1Fudan University, 2Shanghai Innovation Institute, 3Tencent Youtu Lab
Large language model (LLM) agents have demonstrated strong capability in sequential decision-
making, yet they remains fundamentally reactive in long-horizon tasks. Unlike humans who
employ"what-if"reasoning to evaluate potential plans before commitment, standard agents lack an
internal world model to simulate future outcomes. Therefore, we propose to internalize future-aware
planning by training a single autoregressive model to verbalize both a prospective state rollout and
a plan-conditioned success estimate—a textual analogue of the Q-value. Crucially, we identify a
format-capability gap: simply fine-tuning agents on look-ahead traces during post-training leads
to superficial mimicry of foresight without genuine predictive grounding. To bridge this gap, we
introduce a three-stage training paradigm: (i) World Model Agentic Mid-Training (WM-AMT) to
inject latent predictive capabilities into the policy; (ii) Format-Eliciting SFT (FE-SFT) to structure this
injected capability; and (iii) Foresight-Conditioned Reinforcement Learning (FC-RL) to refine the
calibration and utility of the generated simulations. Evaluated on search and mathematical reasoning
tasks, our approach consistently outperforms other training baselines. Our results demonstrate
that effective internal world modeling in LLM agents requires a capability-first training pipeline to
achieve grounded and calibrated foresight.
Date:June 25, 2026
Correspondence:xuanzhang24@m.fudan.edu.cn
1 Introduction
LLM agents have become strong controllers for multi-step tasks given their comprehensive pre-trained
semantic knowledge and remarkable capabilities in sequential decision-making [1, 2]. However, the pre-
vailing paradigm in long-horizon settings remains fundamentally reactive, yet human planning is rarely
reactive. Before acting, people often ask awhat-ifquestion: if I follow this plan, what is likely to happen
next, and how likely is it to succeed? This style of reasoning is central to intelligent behavior because it
allows alternatives to be mentally compared before commitment, as shown in Figure 1. In Craik’s classic
formulation, effective intelligence depends on carrying a “small-scale model” of external reality that lets
possible actions be tried out in thought before they are executed [3]. Inspired by this pattern of planning, we
do not claim full counterfactual reasoning; rather, we target a plan-conditioned form of future simulation
and evaluation within a language agent.
While standard autoregressive reasoning methods such as Chain-of-Thought [4] mainly improve decomposi-
tion of the current problem, the ability that we aim to inject is closely related to an internal world model
[5, 6]. Instead of utilizing separate modules to serve as external world models [7, 8, 9], our key claim is that,
for language agents, this kind of future-aware planning signal should be internalized as part of the policy
itself. Moreover, unlike Dreamer-style model-based RL [10, 11, 12], our goal is not to introduce a separate
simulator or a dedicated value head. Instead, we train a single autoregressive model not only to serve as
1
arXiv:2606.27483v1  [cs.AI]  25 Jun 2026

World Model Agentic Training
Human Cognitive Inspiration
Internal
Cognitive
Network
MentalSimulation&
MentalEvaluation
OriginalHypothesis
Standard Reactive LLM Agent
No internal look-ahead
Inspiration Deeper Analysis
Reactive
Proposed: Agent Policy with Internalized World Model
Internalized
World Model
SuccessEstimate
Verbalized𝑄(𝑠,𝑎)
Execute in the real world
After trying:
“Controlled Glide Works!”
Confidence Level
Unified
Token Space
Prospective Rollout
Feedback
Update
Refiningprospectiverollouts&𝑄-valueestimates
Figure 1.Overview of our key design of an agent policy with internalized world model.
a reasoning agent, but also to verbalize both: (i) a compact prospective rollout of what may happen next,
and (ii) a plan-conditioned estimate of success if the current plan is followed. This textual estimate is best
understood as a verbalized analogue of Q(s, a) or local action value, represented in the same token space
as the policy rather than as a claim of full what-if reasoning. Unlike other methods that only train agents
to predict future states or transition dynamics [13, 14, 15], our design of internal world modeling is more
comprehensive and innovative. Crucially, our verbalized Q-values are designed to be continuously updated
and corrected by actual environmental feedback obtained from real execution during RL training, which is
also distinct from previous works [16].
Such explicit verbalization offers a transparent reasoning signal, allowing the agent to effectively prune
suboptimal paths through implicit deliberation. To inject this capability, a natural idea is to leverage the
inherent world modeling potential of LLMs [17] by training the agent to imagine the future, evaluate it, and
then act. However, our preliminary experiments show that this strategy fails when applied only during
post-training. With SFT and RL on formatted look-ahead traces, the agent learns the surface form of a
simulation but not the predictive competence behind it. Experimental results for SFT and RL are shown
in Table 7, and an example is shown in Appendix E.1. We call this failure mode theformat-capability gap:
the agent can produce a plausible-looking foresight block while the content remains weakly grounded,
miscalibrated, or outright misleading, thus introducing noise rather than useful guidance.
This motivates us to propose a unified three-stage training paradigm:World Model Agentic Mid-Training
(WM-AMT),Format-Eliciting SFT (FE-SFT), andForesight-Conditioned Reinforcement Learning (FC-RL).
WM-AMT injects the underlying predict-then-act capability by augmenting large-scale agentic trajectories
with future-aware experience summaries. FE-SFT then teaches the model when and how to externalize this
latent capability in a structured foresight block. FC-RL finally improves both action quality and foresight
quality by rewarding task success, grounded anticipation, and calibrated confidence. All three stages are
implemented within one causal language model, with no additional value head.
We evaluate this training paradigm on two representative agentic domains: search and mathematical
reasoning. Across both settings, our method consistently outperforms other training baselines. The results
show that future-aware behavior in LLM agents is not well served by format supervision alone; it benefits
from a training pipeline that first builds the capability, then elicits it, and finally optimizes it under reward.
2

World Model Agentic Training
Our contributions are summarized as follows:
• We identify the format-capability gap: post-training on look-ahead formats alone teaches LLM agents
to mimic the structure of foresight without reliably acquiring grounded future prediction.
• We propose a unified three-stage paradigm, consisting of WM-AMT, FE-SFT, and FC-RL, which
internalizes world-model planning inside a single autoregressive policy. Our method verbalizes both
future rollout and a plan-conditioned success estimate without introducing an explicit value head, and
this verbalized Q-like signal is explicitly trained and refined throughout the pipeline.
• We show on search and mathematical reasoning that this capability-first pipeline yields consistent
gains over other training baselines.
2 Preliminaries
2.1 World models in LLM agents
We formulate LLM agents’ decision-making as a Markov Decision Process (MDP) [18], denoted by M=
⟨S, A, P, R, γ⟩. State st ∈ Sincludes the initial instruction, historical trajectory, and observations. Actionat ∈
A represents discrete operations, e.g., text generation or tool invocation. Transition dynamics P(s t+1|st, at)
and reward R(st, at) govern environmental feedback. The objective is to learn a parameterized policy
πθ(at|st) that maximizes the expected return discounted by γ∈[ 0, 1]. World models traditionally predict
transition dynamics ˆP(s t+1|st, at) and rewards ˆR(st, at) [5]. However, applying token-level simulation to
dense, low-level environmental feedback is computationally intractable. Autoregressively predicting fine-
grained future trajectories τf uture =⟨s t+1, at+1, ot+1, . . ., st+k ⟩ may waste computational capacity on syntax
rather than core causal dynamics, thus causing severe compounding errors [19]. Thus, we reconceptualize the
World Model for LLM agents as aninternal semantic simulator. It generates a condensedexperience summaryof
anticipated consequences, defined as ˆzt =Ψ(τ f uture). Here, Ψ is a semantic compression function mapping
raw rollouts into high-level predictive foresight. This empowers the agent to performlook-ahead planning,
transitioning from a reactive policy πθ(at|st) to a foresight-conditioned policy πθ(at|st, ˆzt). Ultimately, this
enables the agent to evaluate consequences and prune suboptimal trajectories in the latent space before
executing real-world actions.
2.2 Mid-training in large language models
To obtain strong initial policies in terms of both performance and exploration diversity, mid-training [20, 21]
has become an essential step between general pre-training and post-training, which aims to adapt the LLM’s
underlying data distribution toward the target domain. Recent theoretical analyses demonstrate that an
effective mid-training stage not only establishes strong policy priors by efficiently pruning the decision
space, but also allows the subsequent RL phase to effectively jump across multiple steps during Bellman
backups, thus accelerating convergence speed and minimizing post-training regret [22]. By immersing the
LLM in high-density, high-quality specialized sequences, mid-training provides a latent semantic foundation
and contextually grounded initialization for post-training.
3

World Model Agentic Training
2.3 Group-based RL
Unlike traditional Actor-Critic methods (e.g., PPO [23]) that rely on a parameterized value network Vϕ(s) to
estimate advantages, group-based RL approaches [24, 25, 26] leverage the statistical distribution of rewards
within a sampled batch to approximate the baseline. For a given task prompt x, the agent samples a group
of G trajectories {τ1, τ2, . . ., τG} from the current policy πθold. Each trajectory τi represents a full episode of
interactions and is assigned a scalar reward R(τi) reflecting the task success. The advantage estimation A(τi)
is derived from the normalized reward in each group: A(τi) =
R(τi)−µ({R(τ j)}G j=1 )
σ({R(τ j)}G j=1 ) , where µ and σ denote the
mean and standard deviation of rewards in the group, respectively.
3 Methodology
3.1 The format-capability gap in post-training
A natural idea to internalize world model into the LLM policy is training the LLM with SFT data that
explicitly includes anticipated futures, and then followed by RL. However, our preliminary experiments on
the model mid-trained with routine agentic trajectories (see Appendix D.1 and E.1) reveal a format-capability
gap. While the agent learns the format of look-ahead reasoning, it fails to simulate accurate future dynamics,
often resulting in hallucinations. We attribute it to the inherent nature of post-training: while SFT and
RL excel atelicitinglatent capabilities, they struggle toinjectfundamentally new ones. Without a prior
understanding of future consequences, enforcing a look-ahead format merely triggers hallucinated pattern
matching rather than genuine future simulation. It motivates us to intervene earlier in the training pipeline
viamid-trainingto construct a foundational data distribution that intrinsically models the future. We
propose a three-stage training paradigm to close the format-capability gap, as shown in Figure 2. Given
an LLM policy, our goal is not only to produce a well-formed look-ahead trace, but also to internalize
transition-aware foresight that improves policy capability. The paradigm consists of: (i)World Model
Agentic Mid-Training (WM-AMT)for policy prior formation, (ii)Format-Eliciting Supervised Fine-T uning
(FE-SFT)for structured elicitation, and (iii)Foresight-Conditioned Reinforcement Learning (FC-RL)for
reward-aligned policy optimization.
3.2 World model agentic mid-training
Standard pre-training and agentic SFT trajectory data primarily consist of observational trajectories. While
this paradigm trains the model to predict the next action given the historical context, we aim to instill
look-ahead capabilities in LLM agents via WM-AMT (Algorithm 1). Let Draw ={τ i}N i=1 denote a large-scale
dataset of agentic trajectories, where each trajectory is defined as a sequence of state-action pairs: τ=
(s1, a1, s2, a2, . . ., sT, aT). Instead of relying on human-annotated chain-of-thought data, we systematically
augmentD raw through a trajectory summarization mapping.
Formally, for a given trajectory τ of length T, we sample a set of indices I ∼ U(1, T− 1). For each
step t∈ I, we construct a structured world model block zt. We define a summarization function Φ(·),
which maps the current observation st and the future trajectory τ>t into a composite textual representation:
zt = [z(traj) t ⊕z (eval) t ]. Here, z(traj) t serves as an abstracted roadmap of the simulated future. z(eval) t provides a
semantic gap analysis and a Q-value estimation q∈[ 0, 100]%, denoting the confidence score of successfully
resolving the initial task following this roadmap. While accurately estimating q for merely a single step of a
4

World Model Agentic Training
Phase1:WM-AMT
Raw agentic trajectory
𝑠!"#
 𝑎!"#
……
Extract
𝑠!
 𝑎! 𝑠!$#
Summarization Function𝛟(·)
Augmented trajectory
𝑎!
𝑧!∶ WorldModelBlock
𝑠!
……
Phase3:FC-RL
Insert
𝒛𝒕	=	[𝒛𝒕 (𝒕𝒓𝒂𝒋)	⨁𝒛𝒕 (𝒆𝒗𝒂𝒍)]
Summary
 𝒒𝒕	𝝐	[𝟎,𝟏𝟎𝟎]%
: randomly selected
look-ahead start point
𝐿!"#$"%	(𝜃)
&𝝉
……
NTP Optimization
Phase2:FE-SFT
Current
Observation
…
Future
Trajectory
𝜏%&
keyword
Structural Schema
analysis confidence
imaginary
abstract
milestones
evaluate
the roadmap
quantify
the Q-value
Action
Optimization&Calibration
WorldModelSpan
imaginary
&keyword
analysis&
confidence
PolicySpan
thinkaction
Brierscore
final success
calculate
calibrate
Group-wise Normalization
Actual
Execution ……
Verification
of grounding
Training signal
of policy
update
calibrate
match
……
future Trajectory
Figure 2.Overview of our three-stage training paradigm.
trajectory ideally requires dozens of Monte Carlo rollouts, it is computationally prohibitive given the massive
scale of mid-training data. Consequently, we adopt an LLM to heuristically estimate this success probability.
Though this estimation may be not accurate enough, it is acceptable because these confidence priors are
ultimately grounded and calibrated against true execution outcomes during subsequent RL training.
We then inject zt into the original agentic trajectory, producing an augmented trajectory ˜τ, which is de-
fined by ˜τ= (. . . , st, zt, at, st+1, . . .). The WM-AMT stage optimizes the policy θ via the standard au-
toregressive negative log-likelihood objective over the augmented dataset DWM-AMT: LWM-AMT(θ) =
−E ˜τ∼DWM-AMT
h
∑| ˜τ| i=1 logP θ(ui|u<i) i , where ui denotes the i-th token in ˜τ. By forcing the model to au-
toregressively reconstruct the composite block zt conditioned strictly on the history up to st, the objective
functions as an implicit world model, equipping the agent with both causal prediction and value evaluation
capabilities.
3.3 Format-eliciting supervised fine-tuning
While WM-AMT successfully injects latent look-ahead capabilities into LLM agents, the base policy lacks
the structural schema to autonomously and reliably invoke this predictive capability during inference. The
FE-SFT stage bridges this gap by aligning the generated trajectory with a predefined, explicit look-ahead
reasoning structure. We curate a filtered task-specific instruction-tuning dataset DFE-SFT. Given a current
observation st, the policy is trained to project its internal world model into a textual representation of
anticipated future states and estimated Q-values, i.e., world model block ˆzt. While adopting a similar
generation pipeline for these instances, FE-SFT strictly encloses ˆzt within distinct structural delimiters.
Following ˆzt, the policy generates the corresponding executable action at. Since WM-AMT has established a
robust causal prior via a large-scale general agentic trajectories, FE-SFT avoids the hallucinations typical of
world modeling from scratch. We also use the standard autoregressive negative log-likelihood objective to
optimize the agent onD FE-SFT.
5

World Model Agentic Training
3.4 Foresight-conditioned RL
The policy may still suffer from compounding errors during long-horizon inference or produce miscalibrated
foresight after WM-AMT and FE-SFT. To jointly optimize the internalized world model and the policy, we
introduce FC-RL (Algorithm 2). The agent serves as two roles and generates a structured trajectory in an
interaction loop:imaginary→keyword→analysis→confidence(q t)| {z }
World Model Span(T WM)
→think→action(a t)| {z }
Policy Span(T Policy)
.
To jointly optimize final task success and intermediate foresight quality, we decompose the training objective
into world model optimization and policy optimization. For a given prompt, we sample a group of N
trajectories{τ 1, . . . ,τN}.
World model optimization: foresight grounding and calibrationTo ensure the internal world model
provides reliable planning rather than hallucinations, we optimize it from two complementary dimensions:
causal accuracy and value calibration.
First, to penalize hallucinated simulations, we introduce a grounding reward Rground. The agent abstracts
its look-ahead trajectory into milestones, denoted as keywords Kt. We define Ri,t ground =R match(K(i) t , τ(i) >t ),
a verification function that rewards the model only if its predicted keywords successfully manifest in the
actual execution.
Second, to ensure the accuracy of the agent’s internal Q-value estimation and explicitly penalize miscali-
brated foresight, we apply a Brier score penalty [27] to the confidence q(i) t . Upon episode completion, the
environment provides a terminal correctness evaluation, yielding a binary outcome indicator I, i.e., Iy≡y∗,
where y is the predicted answer and y∗ is the ground truth. From a Monte Carlo (MC) perspective, I serves
as an unbiased, single-sample empirical return for the trajectory from step t. To calibrate qt, we treat this MC
return as the ground truth and apply a Brier score-based calibration reward:
Ri,t calib =R calib(yi,q (i) t ,y ∗ i ) =I−(q (i) t −I) 2 (1)
By utilizing the terminal correctness to calibrate the intermediateqt, it forces the agent to align its self-assessed
Q-values, i.e., confidence on future, with the empirical success rate.
Finally, we compute a combined step-level world model reward RWM(τt i ) =Ri,t calib +R i,t ground. We obtain the
final world model advantage A(τ[world_model] t i ) by normalizing these combined rewards across all the
corresponding steps{R WM(τt i )}N i=1 within the group.
Policy optimization: execution successFor long-horizon tasks, relying solely on the terminal global
advantage may suffer from sparse and delayed credit assignment, so we introduce a local (step) reward
RS(τt i ) =q (i) t . Let AE(τi) denote the global advantage computed by normalizing the episode rewards
RE i across the group. Similarly, let AS(τt i ) represent the step-level advantage, normalized across all the
confidence of corresponding steps {q(i) t }N i=1 within the group. The final combined advantage for the policy
is defined as:
6

World Model Agentic Training
A(τ[policy] t i ) =AE(τi) +ω·A S(τt i )(2)
where ω balances global task success and local foresight alignment. Crucially, sinceq(i) t is explicitly calibrated
via world model optimization, it mitigates the risk of reward hacking and serves as a reliable proxy for the
policy. The policy πϕ is then updated by maximizing the clipped GRPO surrogate objective utilizing the
advantageA(τ[policy] t i ).
4 Related Work
4.1 World models in autonomous agents
World models are core to model-based RL, where agents learn transition and reward for look-ahead control
[5, 28]. Classical lines focus on latent-dynamics learning in visually observed environments [6, 10, 11, 12] and
more recently, embodied agent for future action-conditioned simulation [29]. It enables models to improve
sample efficiency in a latent space or simulate outcomes without real-world interaction. The idea has shifted
from pixel-space simulation to language-mediated future prediction and planning due to the rise of LLMs
[16, 7]; it also extends to code-generation settings, where world modeling is used to study long-horizon
program synthesis and repair [ 14]. Despite these advancements, most existing systems treat the world
model as an explicit simulator or external module [8, 9]. For example, WebDreamer [9] and WebEvolver [30]
construct explicit world models to simulate the environmental feedback, which improve deliberation quality
but may introduce additional inference overhead and possible simulator-policy mismatch. In parallel, recent
implicit world modeling strategies suggest that early experiences can improve downstream agent behavior
without relying on another simulator [13, 15]. Extending this implicit world modeling line, our work targets
a unified agentic training pipeline for world model planning.
4.2 Agentic data synthesis and mid-training
The scarcity of expert-level demonstrations has motivated the synthetic data for training LLM agents [15].
Early imitation-based distillation from stronger teachers [ 31, 32] aids initial alignment but suffers from
limited diversity and weak on-policy coverage. Subsequent works, such as AgentSynth [ 33] and SCA
[34], broaden task synthesis to expand the exploration space for agentic RL. Another direction shifts from
trajectory synthesis to environment synthesis, e.g., classical world-model methods in Section 4.1, which uses
learned environments to generate scalable interaction data. However, translating these synthetic interactions
into reusable decision-making capabilities necessitates a dedicated training phase. Consequently,mid-training
[20] is increasingly adopted to bridge general pre-training and task-level alignment [ 21, 22]. Unlike SFT,
mid-training scales to vastly larger, diverse corpora of expert rollouts, such as human demonstrations in
device control, tool-use records and code writing [ 35, 36, 37]. Our perspective is to synthesize agentic
data with compressed future experience summary, and internalize a robustpredict-then-actpolicy prior via
mid-training.
5 Experiments
7

World Model Agentic Training
5.1 Experiment setup
We select an intermediate checkpoint of Youtu-LLM-2B [ 38] as our foundation model, and refer to it as
Youtu-LLM-2B-Init. This selection is motivated by two practical considerations: (1) the Youtu-LLM family
inherently possesses strong native agentic capabilities; (2) a lightweight 2B scale makes our extensive
mid-training computationally feasible. To validate the effectiveness of our method, we initialize from the
Youtu-LLM-2B-Init immediately following its general pre-training and compare two mid-training variants:
(1)Youtu-LLM-2B-Baseis trained with standard agentic mid-training on 200B tokens of high-quality agentic
trajectory data without changing its structure; (2)Youtu-LLM-2B-Base (WM-AMT, ours)augments the same
agentic trajectory data by inserting an explicitworld model blockinto a random split of multi-turn interaction
trajectories, which provides supervised signals for future-state prediction. We conduct experiments on two
representative agentic tasks: search and mathematical reasoning.
SearchFollowing Jin et al. [39], we evaluate our training paradigm on 7 search-augmented QA tasks,
including single-hop QA datasets (NQ [40], TriviaQA [41], and PopQA [42]) and multi-hop QA datasets
(HotpotQA [43], 2Wiki [44], MuSiQue [45], and Bamboogle [46]). For retrieval, we use the 2018 Wikipedia
dump [47] as the knowledge source and E5 [48] as the retriever, and set the number of retrieved passages to
3 across all retrieval-based methods. During evaluation, the results are obtained via greedy sampling, and
the metrics are computed via LLM-as-a-judge using DeepSeek V3.1 [49].
Mathematical reasoningFollowing Feng et al. [50], we evaluate our paradigm on AIME2024/2025/2026
[51]. We repeat the evaluation set AIME2024&2025&2026 30 times and report both mean@30 and pass@30.
The evaluation hyperparameters of evaluation are set to temperature 1.0 and top-p 0.6.
Baselines and configurations(1)Post-Training Only*:Our preliminary experiments are conducted
directly on Youtu-LLM-2B-Base, serving as a vanilla baseline that only applies post-training without any
world-model-augmented mid-training. (2)State-Only Prediction (Post-Training Only) †:The agent is
trained only via post-training to predict future states but omits the verbalized Q-values. This setup mirrors
other methods of predicting only state transitions [13]. (3)State-Only Prediction (With Mid-Training) ‡:
The agent is trained via mid-training and post-training to predict future states but omits the verbalized
Q-values. This setup mirrors other methods introducing large-scale mid-training for world modeling [14].
(4)IWM: We apply the core world-modeling data generation pipeline of [15] to our task. Detailed training
hyperparameters are presented in Appendix C.3.3.
5.2 Main results
Necessity of our three phases. (1) WM-AMT: At the SFT stage, replacing standard agentic mid-training
with our WM-AMT improves the average score under the same SFT method (e.g., in Table 1, 38.2 → 39.9
for SFT and 37.4 → 41.8 for FE-SFT). We provide a case study in Appendix E.1: under the same FE-SFT
format, our WM-AMT model generates more coherent, causally accurate world model blocks, while the base
model fails. These results indicate that FE-SFT is substantially effective when the model has internalized
future-dynamics priors via WM-AMT.(2) FE-SFT: Under our WM-AMT model, our FE-SFT outperforms
standard SFT (e.g. 39.9 → 41.8 in Table 1), showing that explicitly eliciting structured foresight is beneficial
after the world-model capability is established.(3) FC-RL: In RL-stage comparisons, our FE-SFT & FC-RL
achieves the best overall average (50.6 in Table 1, mean@30: 29.5 and pass@30: 60.0 in Table 2), outperforming
all the other baselines.
8

World Model Agentic Training
Method Single-Hop QA Multi-Hop QA Avg.
NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle
Youtu-LLM-2B-Base
SFT* 41.8 56.6 31.0 44.8 26.4 21.0 45.6 38.2
FE-SFT* 41.6 51.4 30.6 42.2 27.2 23.2 45.6 37.4
IWM 44.4 57.6 31.846.028.8 25.4 47.240.2
Youtu-LLM-2B-Base (WM-AMT, ours)
SFT46.058.2 32.6 44.6 31.2 20.6 46.4 39.9
FE-SFT 45.6 58.8 33.845.8 35.8 25.6 47.2 41.8
(a)Performance up to the SFT stage
Method Single-Hop QA Multi-Hop QA Avg.
NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle
Youtu-LLM-2B-Base
SFT & RL* 48.0 58.2 35.2 53.8 45.0 30.2 52.0 46.1
FE-SFT & RL* 49.4 60.0 38.2 55.4 42.0 29.8 54.4 47.0
State-SFT & RL† 48.2 58.8 40.8 55.2 40.8 31.4 54.4 47.1
IWM & RL 50.0 62.2 38.8 55.0 46.0 33.2 53.6 48.4
Youtu-LLM-2B-Base (WM-AMT, ours)
SFT & RL 50.2 59.8 35.6 53.6 46.0 25.4 45.6 45.2
FE-SFT & RL 52.6 63.2 40.8 57.0 44.4 32.6 52.8 49.1
State-SFT & RL‡ 52.864.4 42.854.6 42.2 30.4 53.6 48.7
FE-SFT & FC-RL53.462.6 42.6 59.0 46.2 34.2 56.0 50.6
(b)Performance with the RL stage (the final performance)
Table 1.Main results on search: performance on 7 QA datasets.SFTuses onlythinkandactionsegments, excluding
world model block injections.RLdenotes the standard GRPO algorithm.State-SFTcorresponds to (2) and (3) in the
Baselines; these models predict future state transitions but omit verbalized Q-values. These denotations remain the same
as in Table 2. Thebold textrepresents the best, while underlined represents the second best.
Stage dependency.The overall results exhibit a progressive dependency: WM-AMT provides a capability
foundation, FE-SFT activates this capability in a structured format, and FC-RL optimizes end-task behavior
with grounded foresight. Removing or replacing any stage weakens the final performance, confirming the
need for the full pipeline.
Comparison with other world modeling methods.In Table 1, the highest average score of state-only
baselines is 48.7; while in Table 2, it achieves a pass@30 of 56.7 and a mean@30 of 27.7. By adding the
verbalized Q-value and applying our FC-RL to jointly optimize the policy and its internalized world model,
our final model (WM-AMT & FE-SFT & FC-RL) increases these scores to 50.6 in Table 1, 60.0 (pass@30) and
29.5 (mean@30) in Table 2, respectively. It proves that simply predicting future states is not enough for world
modeling. Instead, explicitly adding the confidence estimation and utilizing the calibrated confidence to
guide the policy are crucial for making better decisions. Notably, IWM (+RL) achieves strong performance
on Youtu-LLM-2B-Base, but our final model still shows a significant and consistent improvement.
Efficacy on complex multi-hop reasoning.Another notable fact is that our proposed paradigm yields
particularly pronounced improvements on complex, multi-step reasoning tasks in Table 1. Up to the SFT
stage, the transition fromSFTtoFE-SFTunder our WM-AMT model brings a significant improvement
(MuSiQue: 20.6 → 25.6, 2WikiMultiHopQA: 31.2 → 35.8). Our final model also demonstrates substantial
superiority on multi-hop datasets compared to the other baselines, e.g., HotpotQA (59.0), MuSiQue (34.2)
9

World Model Agentic Training
Method mean@30 pass@30
AIME 24 AIME 25 AIME 26 Avg. AIME 24 AIME 25 AIME 26 Avg.
Youtu-LLM-2B-Base
SFT* 9.1 9.9 8.9 9.3 46.7 33.3 40.0 40.0
FE-SFT* 12.0 9.9 8.0 10.0 53.3 36.740.0 43.3
IWM13.010.6 10.211.3 56.733.3 43.3 44.4
Youtu-LLM-2B-Base (WM-AMT, ours)
SFT 10.9 10.6 8.8 10.1 56.7 36.733.3 42.2
FE-SFT 12.2 12.29.7 11.4 53.3 36.740.0 43.3
(a)Performance up to the SFT stage
Method mean@30 pass@30
AIME 24 AIME 25 AIME 26 Avg. AIME 24 AIME 25 AIME 26 Avg.
Youtu-LLM-2B-Base
SFT & RL*35.124.3 24.6 28.0 56.7 46.7 53.3 52.2
FE-SFT & RL* 31.9 26.4 25.7 28.0 60.0 46.7 46.7 51.1
State-SFT & RL† 32.2 22.1 27.0 27.1 60.0 50.060.056.7
IWM & RL 33.2 24.927.628.6 66.750.0 56.7 57.8
Youtu-LLM-2B-Base (WM-AMT, ours)
SFT & RL 34.2 23.4 25.9 27.8 63.3 53.3 53.3 56.6
FE-SFT & RL 33.6 25.6 26.0 28.4 60.0 53.3 50.0 55.5
State-SFT & RL‡ 33.2 24.8 25.0 27.7 63.3 56.750.0 56.7
FE-SFT & FC-RL 34.6 26.827.1 29.5 66.753.3 60.0 60.0
(b)Performance with the RL stage (the final performance)
Table 2.Main results on mathematical reasoning. Thebold textand underlined represent the same as in Table 1.
and Bamboogle (56.0). It indicates that the internalized world model and foresight-conditioned planning are
especially critical for tasks requiring long-horizon reasoning, whereas simple factual retrieval (single-hop)
relies less heavily on future simulation.
Qualitative analysis of world model blocks.We provide examples in Appendix E.2 and E.3 to analyze
the world model blocks. Two key capabilities emerge: (1)Long-horizon planning coherence: these blocks
establish reasoning frameworks that persist across multiple turns, even when intermediate errors require
correction; and (2)Calibrated confidence quantification: confidence estimates correlate meaningfully with
the actual task success, decreasing upon error detection and remaining low for inherently challenging
problems.
Additional ablation studies, sensitivity analyses on ω in FC-RL, and analyses on the response length are
provided in Appendix D.2, D.3 and D.4.
6 Conclusion
We address the limitations of reactive LLM agents by internalizing future-aware planning into the policy.
We identify theformat-capability gap, wherein post-training on look-ahead formats merely teaches structural
mimicry instead of grounded prediction. To bridge this gap, we propose a unified three-stage training
paradigm consisting of WM-AMT, FE-SFT and FC-RL. Evaluations across search and mathematical reasoning
show the superiority of our approach over other training baselines. Our results underscore that effective
10

World Model Agentic Training
internal world modeling in LLM agents demands a capability-first paradigm to achieve truly grounded and
calibrated foresight.
Contributions
AuthorsXuan Zhang 1,2,3 Zhijian Zhou1,2,3 LingFeng Qiao 3 Yulei Qin3 Ke Li3 Xing Sun3
Xiaoyu Tan3 † Chao Qu1 † Yuan Qi1,2 †
Affiliations 1Fudan University 2Shanghai Innovation Institute 3Tencent Youtu Lab
†Corresponding AuthorsXiaoyu Tan Chao Qu Yuan Qi
AcknowledgmentsWe greatly thank the VeRL [ 52] and the VeRL-agent [26] communities for their imple-
mentation of various RL training and inference frameworks.
References
[1] Lei Wang, Chengbang Ma, Xueyang Feng, Zeyu Zhang, Hao ran Yang, Jingsen Zhang, Zhi-Yang
Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, and Ji rong Wen. A survey
on large language model based autonomous agents.Frontiers of Computer Science, 18, 2023. URL
https://api.semanticscholar.org/CorpusID:261064713.
[2] Theodore Sumers, Shunyu Yao, Karthik R Narasimhan, and Thomas L. Griffiths. Cognitive architectures
for language agents.Transactions on Machine Learning Research, 2024. ISSN 2835-8856. URL https:
//openreview.net/forum?id=1i6ZCvflQJ. Survey Certification, Featured Certification.
[3] Kenneth Craik. The nature of explanation. 1944. URL https://api.semanticscholar.org/CorpusID:
41364251.
[4] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, brian ichter, Fei Xia, Ed Chi,
Quoc V Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large lan-
guage models. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, ed-
itors,Advances in Neural Information Processing Systems, volume 35, pages 24824–24837. Curran
Associates, Inc., 2022. URL https://proceedings.neurips.cc/paper_files/paper/2022/file/
9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf.
[5] Richard S. Sutton. Dyna, an integrated architecture for learning, planning, and reacting.SIGART Bull.,
2(4):160–163, July 1991. ISSN 0163-5719. doi: 10.1145/122344.122377. URL https://doi.org/10.1145/
122344.122377.
[6] David Ha and Jürgen Schmidhuber. Recurrent world models facilitate policy evolution.Advances in
neural information processing systems, 31, 2018.
[7] Hyungjoo Chae, Namyoung Kim, Kai Tzu iunn Ong, Minju Gwak, Gwanwoo Song, Jihoon Kim,
Sunghwan Kim, Dongha Lee, and Jinyoung Yeo. Web agents with world models: Learning and
leveraging environment dynamics in web navigation. InThe Thirteenth International Conference on
Learning Representations, 2025. URLhttps://openreview.net/forum?id=moWiYJuSGF.
11

World Model Agentic Training
[8] Yiming Wang, Da Yin, Yuedong Cui, Ruichen Zheng, Zhiqian Li, Zongyu Lin, Di Wu, Xueqing Wu,
Chenchen Ye, Yu Zhou, and Kai-Wei Chang. Llms as scalable, general-purpose simulators for evolving
digital agent training, 2025. URLhttps://arxiv.org/abs/2510.14969.
[9] Yu Gu, Kai Zhang, Yuting Ning, Boyuan Zheng, Boyu Gou, Tianci Xue, Cheng Chang, Sanjari Srivastava,
Yanan Xie, Peng Qi, Huan Sun, and Yu Su. Is your llm secretly a world model of the internet? model-
based planning for web agents.Transactions on Machine Learning Research, 2025.
[10] Danijar Hafner, Timothy Lillicrap, Jimmy Ba, and Mohammad Norouzi. Dream to control: Learning
behaviors by latent imagination. InInternational Conference on Learning Representations, 2020. URL
https://openreview.net/forum?id=S1lOTC4tDS.
[11] Danijar Hafner, Timothy P Lillicrap, Mohammad Norouzi, and Jimmy Ba. Mastering atari with
discrete world models. InInternational Conference on Learning Representations, 2021. URL https:
//openreview.net/forum?id=0oabwyZbOu.
[12] Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, and Timothy Lillicrap. Mastering diverse domains through
world models, 2024. URLhttps://arxiv.org/abs/2301.04104.
[13] Shiqi Chen, Tongyao Zhu, Zian Wang, Jinghan Zhang, Kangrui Wang, Siyang Gao, Teng Xiao, Yee Whye
Teh, Junxian He, and Manling Li. Internalizing world models via self-play finetuning for agentic rl,
2025. URLhttps://arxiv.org/abs/2510.15047.
[14] Meta FAIR CodeGen Team. Cwm: An open-weights llm for research on code generation with world
models, 2025. URLhttps://ai.meta.com/research/publications/cwm/.
[15] Kai Zhang, Xiangchao Chen, Bo Liu, Tianci Xue, Zeyi Liao, Zhihan Liu, Xiyao Wang, Yuting Ning,
Zhaorun Chen, Xiaohan Fu, Jian Xie, Yuxuan Sun, Boyu Gou, Qi Qi, Zihang Meng, Jianwei Yang, Ning
Zhang, Xian Li, Ashish Shah, Dat Huynh, Hengduo Li, Zi Yang, Sara Cao, Lawrence Jang, Shuyan Zhou,
Jiacheng Zhu, Huan Sun, Jason Weston, Yu Su, and Yifan Wu. Agent learning via early experience, 2025.
URLhttps://arxiv.org/abs/2510.08558.
[16] Shibo Hao, Yi Gu, Haodi Ma, Joshua Hong, Zhen Wang, Daisy Wang, and Zhiting Hu. Reasoning
with language model is planning with world model. In Houda Bouamor, Juan Pino, and Kalika Bali,
editors,Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages
8154–8173, Singapore, December 2023. Association for Computational Linguistics. doi: 10.18653/v1/
2023.emnlp-main.507. URLhttps://aclanthology.org/2023.emnlp-main.507/.
[17] Yixia Li, Hongru Wang, Jiahao Qiu, Zhenfei Yin, Dongdong Zhang, Cheng Qian, Zeping Li, Pony Ma,
Guanhua Chen, Heng Ji, and Mengdi Wang. From word to world: Can large language models be
implicit text-based world models?, 2025. URLhttps://arxiv.org/abs/2512.18832.
[18] Richard Bellman. A markovian decision process.Indiana University Mathematics Journal, page 679–684.
doi: 10.1512/iumj.1957.6.56038. URLhttp://dx.doi.org/10.1512/iumj.1957.6.56038.
[19] Yann LeCun et al. A path towards autonomous machine intelligence version 0.9. 2, 2022-06-27.Open
Review, 62(1):1–62, 2022.
[20] Kaixiang Mo, Yuxin Shi, Weiwei Weng, Zhiqiang Zhou, Shuman Liu, Haibo Zhang, and Anxiang Zeng.
Mid-training of large language models: A survey, 2025. URLhttps://arxiv.org/abs/2510.06826.
[21] Liangcai Su, Zhen Zhang, Guangyu Li, Zhuo Chen, Chenxi Wang, Maojia Song, Xinyu Wang, Kuan Li,
Jialong Wu, Xuanzhong Chen, Zile Qiao, Zhongwang Zhang, Huifeng Yin, Shihao Cai, Runnan Fang,
Zhengwei Tao, Wenbiao Yin, Chenxiong Qian, Yong Jiang, Pengjun Xie, Fei Huang, and Jingren Zhou.
Scaling agents via continual pre-training, 2025. URLhttps://arxiv.org/abs/2509.13310.
[22] Shenao Zhang, Donghan Yu, Yihao Feng, Bowen Jin, Zhaoran Wang, John Peebles, and Zirui Wang.
Learning to reason as action abstractions with scalable mid-training RL. InThe Fourteenth International
Conference on Learning Representations, 2026. URLhttps://openreview.net/forum?id=uWd9A1zp0Y.
12

World Model Agentic Training
[23] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy
optimization algorithms, 2017. URLhttps://arxiv.org/abs/1707.06347.
[24] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y.K. Li, Y. Wu,
and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models,
2024. URLhttps://arxiv.org/abs/2402.03300.
[25] Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan,
Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale.
arXiv preprint arXiv:2503.14476, 2025.
[26] Lang Feng, Zhenghai Xue, Tingcong Liu, and Bo An. Group-in-group policy optimization for LLM
agent training. InThe Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025. URL
https://openreview.net/forum?id=QXEhBMNrCW.
[27] W Brier Glenn et al. Verification of forecasts expressed in terms of probability.Monthly weather review,
78(1):1–3, 1950.
[28] Thomas M. Moerland, Joost Broekens, Aske Plaat, and Catholijn M. Jonker. Model-based reinforcement
learning: A survey.Found. Trends Mach. Learn., 16(1):1–118, January 2023. ISSN 1935-8237. doi:
10.1561/2200000086. URLhttps://doi.org/10.1561/2200000086.
[29] Pascale Fung, Yoram Bachrach, Asli Celikyilmaz, Kamalika Chaudhuri, Delong Chen, Willy Chung,
Emmanuel Dupoux, Hongyu Gong, Hervé Jégou, Alessandro Lazaric, Arjun Majumdar, Andrea
Madotto, Franziska Meier, Florian Metze, Louis-Philippe Morency, Théo Moutakanni, Juan Pino, Basile
Terver, Joseph Tighe, Paden Tomasello, and Jitendra Malik. Embodied ai agents: Modeling the world,
2025. URLhttps://arxiv.org/abs/2506.22355.
[30] Tianqing Fang, Hongming Zhang, Zhisong Zhang, Kaixin Ma, Wenhao Yu, Haitao Mi, and Dong
Yu. Webevolver: Enhancing web agent self-improvement with coevolving world model, 2025. URL
https://arxiv.org/abs/2504.21024.
[31] Vardaan Pahuja, Yadong Lu, Corby Rosset, Boyu Gou, Arindam Mitra, Spencer Whitehead, Yu Su, and
Ahmed Awadallah. Explorer: Scaling exploration-driven web trajectory synthesis for multimodal web
agents, 2025. URLhttps://arxiv.org/abs/2502.11357.
[32] Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Samuel Stevens, Boshi Wang, Huan Sun, and Yu Su.
Mind2web: Towards a generalist agent for the web. InThirty-seventh Conference on Neural Information
Processing Systems Datasets and Benchmarks Track, 2023. URL https://openreview.net/forum?id=
kiYqbO3wqw.
[33] Jingxu Xie, Dylan Xu, Xuandong Zhao, and Dawn Song. Agentsynth: Scalable task generation for
generalist computer-use agents.arXiv preprint arXiv:2506.14205, 2025.
[34] Yifei Zhou, Sergey Levine, Jason Weston, Xian Li, and Sainbayar Sukhbaatar. Self-challenging language
model agents, 2025. URLhttps://arxiv.org/abs/2506.01716.
[35] Christopher Rawles, Alice Li, Daniel Rodriguez, Oriana Riva, and Timothy P Lillicrap. An-
droidinthewild: A large-scale dataset for android device control. InThirty-seventh Conference on Neural
Information Processing Systems Datasets and Benchmarks Track, 2023. URL https://openreview.net/
forum?id=j4b3l5kOil.
[36] Siming Huang, Tianhao Cheng, Jason Klein Liu, Weidi Xu, Jiaran Hao, Liuyihan Song, Yang Xu, Jian
Yang, Jiaheng Liu, Chenchen Zhang, Linzheng Chai, Ruifeng Yuan, Xianzhen Luo, Qiufeng Wang,
YuanTao Fan, Qingfu Zhu, Zhaoxiang Zhang, Yang Gao, Jie Fu, Qian Liu, Houyi Li, Ge Zhang, Yuan Qi,
Xu Yinghui, Wei Chu, and Zili Wang. OpenCoder: The open cookbook for top-tier code large language
models. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors,
Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), pages 33167–33193, Vienna, Austria, July 2025. Association for Computational Linguistics.
13

World Model Agentic Training
ISBN 979-8-89176-251-0. doi: 10.18653/v1/2025.acl-long.1591. URL https://aclanthology.org/2025.
acl-long.1591/.
[37] Hao Bai, Yifei Zhou, Mert Cemri, Jiayi Pan, Alane Suhr, Sergey Levine, and Aviral Kumar. Digirl:
Training in-the-wild device-control agents with autonomous reinforcement learning. In A. Glober-
son, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang, editors,Advances
in Neural Information Processing Systems, volume 37, pages 12461–12495. Curran Associates, Inc.,
2024. doi: 10.52202/079017-0397. URL https://proceedings.neurips.cc/paper_files/paper/
2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf.
[38] Junru Lu, Jiarui Qin, Lingfeng Qiao, Yinghui Li, Xinyi Dai, Bo Ke, Jianfeng He, Ruizhi Qiao, Di Yin, Xing
Sun, Yunsheng Wu, Yinsong Liu, Shuangyin Liu, Mingkong Tang, Haodong Lin, Jiayi Kuang, Fanxu
Meng, Xiaojuan Tang, Yunjia Xi, Junjie Huang, Haotong Yang, Zhenyi Shen, Yangning Li, Qianwen
Zhang, Yifei Yu, Siyu An, Junnan Dong, Qiufeng Wang, Jie Wang, Keyu Chen, Wei Wen, Taian Guo,
Zhifeng Shen, Daohai Yu, Jiahao Li, Ke Li, Zongyi Li, and Xiaoyu Tan. Youtu-llm: Unlocking the native
agentic potential for lightweight large language models, 2026. URL https://arxiv.org/abs/2512.
24618.
[39] Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon, Sercan O Arik, Dong Wang, Hamed Zamani,
and Jiawei Han. Search-r1: Training LLMs to reason and leverage search engines with reinforcement
learning. InSecond Conference on Language Modeling, 2025. URLhttps://openreview.net/forum?id=
Rwhi91ideu.
[40] Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti,
Danielle Epstein, Illia Polosukhin, Matthew Kelcey, Jacob Devlin, Kenton Lee, Kristina N. Toutanova,
Llion Jones, Ming-Wei Chang, Andrew Dai, Jakob Uszkoreit, Quoc Le, and Slav Petrov. Natural
questions: a benchmark for question answering research.Transactions of the Association of Computational
Linguistics, 2019.
[41] Mandar Joshi, Eunsol Choi, Daniel S. Weld, and Luke Zettlemoyer. Triviaqa: A large scale distantly
supervised challenge dataset for reading comprehension, 2017. URL https://arxiv.org/abs/1705.
03551.
[42] Alex Mallen, Akari Asai, Victor Zhong, Rajarshi Das, Daniel Khashabi, and Hannaneh Hajishirzi. When
not to trust language models: Investigating effectiveness of parametric and non-parametric memories,
2023. URLhttps://arxiv.org/abs/2212.10511.
[43] Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William W. Cohen, Ruslan Salakhutdinov, and
Christopher D. Manning. Hotpotqa: A dataset for diverse, explainable multi-hop question answering,
2018. URLhttps://arxiv.org/abs/1809.09600.
[44] Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara, and Akiko Aizawa. Constructing a multi-hop qa
dataset for comprehensive evaluation of reasoning steps, 2020. URL https://arxiv.org/abs/2011.
01060.
[45] Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal. MuSiQue: Multihop
questions via single-hop question composition.Transactions of the Association for Computational Linguistics,
2022.
[46] Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt, Noah A. Smith, and Mike Lewis. Measuring
and narrowing the compositionality gap in language models, 2023. URL https://arxiv.org/abs/
2210.03350.
[47] Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen,
and Wen-tau Yih. Dense passage retrieval for open-domain question answering. In Bonnie Webber,
Trevor Cohn, Yulan He, and Yang Liu, editors,Proceedings of the 2020 Conference on Empirical Methods
in Natural Language Processing (EMNLP), pages 6769–6781, Online, November 2020. Association for
Computational Linguistics. doi: 10.18653/v1/2020.emnlp-main.550. URL https://aclanthology.
org/2020.emnlp-main.550/.
14

World Model Agentic Training
[48] Liang Wang, Nan Yang, Xiaolong Huang, Binxing Jiao, Linjun Yang, Daxin Jiang, Rangan Majumder,
and Furu Wei. Text embeddings by weakly-supervised contrastive pre-training, 2024. URL https:
//arxiv.org/abs/2212.03533.
[49] DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang
Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Daya Guo, Dejian Yang, Deli Chen,
Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, and Guowei
Li. Deepseek-v3 technical report, 2025. URLhttps://arxiv.org/abs/2412.19437.
[50] Jiazhan Feng, Shijue Huang, Xingwei Qu, Ge Zhang, Yujia Qin, Baoquan Zhong, Chengquan Jiang,
Jinxin Chi, and Wanjun Zhong. Retool: Reinforcement learning for strategic tool use in llms, 2025. URL
https://arxiv.org/abs/2504.11536.
[51] MAA. American invitational mathematics examination (aime), 2025.https://maa.org/.
[52] Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng,
Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. InProceedings of the
Twentieth European Conference on Computer Systems, EuroSys ’25, page 1279–1297. ACM, March 2025. doi:
10.1145/3689031.3696075. URLhttp://dx.doi.org/10.1145/3689031.3696075.
[53] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad
Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, Amy Yang, Angela Fan, Anirudh
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mitra, Archie Sravankumar, Artem Korenev, and et.al.
Arthur Hinsvark. The llama 3 herd of models, 2024. URLhttps://arxiv.org/abs/2407.21783.
[54] Qwen, :, An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li,
Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang,
Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li,
Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tianyi Tang, Tingyu Xia, Xingzhang
Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru
Zhang, and Zihan Qiu. Qwen2.5 technical report, 2025. URLhttps://arxiv.org/abs/2412.15115.
A Addition descriptions for our method
A.1 World model agentic mid-training
Our algorithmic description for WM-AMT is shown in Algorithm 1.
A.2 Foresight-conditioned reinforcement learning
Our algorithmic description for FC-RL is shown in Algorithm 2.
B Data construction
15

World Model Agentic Training
Algorithm 1World Model Agentic Mid-Training (WM-AMT)
Input:Raw trajectory datasetD raw ={τ i}N i=1, policyθ, summarization functionΦ.
Initialize the augmented datasetD WM-AMT ←∅.
foreach multi-turn interaction trajectoryτ= (s 1,a 1, . . . ,sT,a T)inD raw do
Sample a set of indicesI ∼ U(1,T−1).
foreach stept∈ Ido
Generate a structured world model blockz t =Φ(s t,τ >t), composed ofz t = [z(traj) t ⊕z (eval) t ].
Estimate a Q-value confidence score q∈[ 0, 100]% via an LLM to represent task success probability,
and incorporate it intoz (eval) t .
end for
Inject generated{z t}t∈I intoτ, yielding an augmented trajectory ˜τ= (. . . ,st,z t,a t,s t+1, . . .).
Add ˜τto the augmented datasetD WM-AMT.
end for
Optimization Phase:
whilenot convergeddo
Sample a batch of trajectories ˜τ∼ DWM-AMT ∪ {τ|τ∈ Draw ∧τ/∈ DWM-AMT}.
Compute the autoregressive negative log-likelihood loss:L WM-AMT(θ) =−E ˜τ
h
∑| ˜τ| i=1 logP θ(ui|u<i) i .
Update the policyθto minimizeL WM-AMT(θ).
end while
Output:Mid-trained policy modelθ.
B.1 World model agentic mid-training
To construct the structured world model Block zt during the World Model Agentic Mid-Training (WM-AMT)
phase, we employ an LLM acting as the summarization functionΦ(·). The prompt enforces abstract planning
to prevent future-state data leakage and explicitly requires confidence estimation for Q-value modeling. The
exact prompt template is provided below:
16

World Model Agentic Training
Algorithm 2Foresight-Conditioned Reinforcement Learning (FC-RL)
Input:Policy modelπ ϕ, prompt datasetD, group sizeN, balance weightω.
foreach promptxinDdo
% Phase 1: Group Trajectory Generation
fori=1 toNdo
Generate trajectoryτ i autoregressively via an interaction loop:
whiletask not terminated at steptdo
Generate World Model SpanT WM: imagine and predict keywordsK (i) t and confidenceq (i) t .
Generate Policy SpanT Policy: think and execute actiona (i) t .
end while
Obtain terminal correctness indicator1 yi≡y∗ i and episode rewardR E i .
end for
% Phase 2: Grounding & Calibration (Group-wise)
Compute global advantageA E(τi)by normalizing{R E i }N i=1 across the group.
fori=1 toNdo
foreach steptinτ i do
# 2.1 World Model Optimization (Foresight grounding and calibration)
Verification of grounding:R i,t ground =R match(K(i) t ,τ (i) >t ).
Brier score penalty:R i,t calib =1 yi≡y∗ i −(q (i) t −1 yi≡y∗ i )2.
Combined WM reward:R WM(τt i ) =Ri,t calib +R i,t ground.
Compute WM advantageA(τ[world_model] t i )by normalizing{R WM(τt j )}N j=1.
# 2.2 Policy Optimization (Execution success)
Compute step advantageA S(τt i )by normalizing confidence scores{q (j) t }N j=1.
Combined policy advantage:A(τ[policy] t i ) =AE(τi) +ω·A S(τt i ).
end for
end for
% Phase 3: Policy Update
ApplyA(τ[world_model] t i )to optimize theT WM spans.
ApplyA(τ[policy] t i )to optimize theT Policy spans.
end for
Output:Optimized policy modelπ ϕ.
17

World Model Agentic Training
Prompt Template for Summarization (Φ)
Act as an agent’s "World Model". Based on the **FUTURE GROUND TRUTH** (the
verified success path), generate the internal reasoning.
**CRITICAL RULES:**
1. **NO SPOILERS:** Plan the future steps using *abstract placeholders* (e.g.,
"expect to find a candidate name"), NOT specific entities found in the future.
2. **BE SPECIFIC:** In the Action Plan, specify exact keywords/intents,
avoiding generic phrases like "Proceed".
**OUTPUT FORMAT (Markdown Only):**
## World Model Simulation
- **Trajectory:** Step-by-step roadmap to the answer based on the Future Truth.
- **Gap:** Why the current state is insufficient.
- **Confidence:** [0-100]%. (High=Direct path, Low=Complex/Trial-error).
Brief reason.
## Immediate Action Plan
- The precise intent for the *immediate next action* in the
Ground Truth.
**DATA:**
[Current Obs]:
{current_obs}
[FUTURE TRUTH]:
{future_traj}
We leverage DeepSeek V3.1 [49] as the foundational data generator for World Model Agentic Mid-Training.
The model is queried using the above prompt, with generation parameters set to a temperature of 0.6, atop-p
of 0.95, and a maximum response length of 32768 tokens.
The original agentic trajectory data consists of 200B tokens of high-quality trajectory data, including 25B
Agentic-CoT trajectories, 20B mathematical trajectories, 70B code execution trajectories, 60B Deep Research
trajectories, and 25B other trajectories (e.g., tool using, function calling, and planning).
In WM-AMT, we augment the original agentic trajectory data by inserting an explicitworld model blockinto
a random split of multi-turn interaction trajectories, which are primarily concentrated in Deep Research
trajectories and mathematical trajectories. After our data augmentation, we obtained roughly ∼ 62B tokens
for Deep Research trajectories and ∼ 21B for mathematics, whereas the remaining trajectory categories
remained unaltered.
Some training samples constructed by this way are shown as follows:
18

World Model Agentic Training
(A) ADeepresearchTrajectory Sample (Trajectory + World Model Block)
User Question
Under which record label was the 17th studio album of the Ivory Coast reggae musician known as
the ’Bob Marley of Africa’ released in 2015, who also performed at the Street Mode Festival in Greece
and collaborated with Harry Roselmack on a tribute song in 2014?
You start with one or more cycles of (thinking about which tool to use → performing tool call →
waiting for tool response), and end with (thinking about the answer→answer of the question).
The thinking processes, tool calls, tool responses, and answer are enclosed within their tags.
There could be multiple thinking processes, tool calls, tool call parameters and tool response parame-
ters.
When you finally reach the conclusion, put your final answer enclosed with <answer> your final
answer here</answer>.
T urn 1: World Model Block
**Trajectory:**
1. Identify the musician via search using the descriptive title "Ivory Coast reggae musician known as
the ’Bob Marley of Africa’".
2. Confirm the artist’s name (Alpha Blondy) from the initial search results.
3. Execute a refined search for the specific details: the 17th studio album (2015 release), the festival
performance, and the collaboration.
4. Extract the album title and record label from the detailed results about the 2015 release.
5. Synthesize the information to provide the final answer.
**Gap:** The current observation only contains the user’s question. No information about the artist’s
identity, discography, or specific events is available to answer the query directly.
**Confidence:** 85%. The question provides multiple unique, verifiable identifiers (specific album
number, year, festival, collaboration) that create a direct path to the answer through targeted searches.
The primary complexity is confirming the artist’s name first.
**Intent:** Identify the correct musician by searching for the unique descriptive title."
T urn 1: Action
search("query": ["Ivory Coast reggae musician known as the ’Bob Marley of Africa’", "17th studio
album of the ’Bob Marley of Africa’ released in 2015", "Street Mode Festival Greece reggae musician
Ivory Coast", "Ivory Coast reggae musician collaborated with Harry Roselmack 2014"])
T urn 1: Feedback
Results for query "Ivory Coast reggae musician known as the ’Bob Marley of Africa’": ......
Results for query "17th studio album of the ’Bob Marley of Africa’ released in 2015": ......
Results for query "Street Mode Festival Greece reggae musician Ivory Coast": ......
Results for query "Ivory Coast reggae musician collaborated with Harry Roselmack 2014": ......
19

World Model Agentic Training
T urn 2: World Model Block
**Trajectory:**
1. Confirm the candidate’s identity as the verified "Bob Marley of Africa" from the initial search
results.
2. Search specifically for the candidate’s 17th studio album released in 2015 using their confirmed
name.
3. Search specifically for the candidate’s performance at the Street Mode Festival using their con-
firmed name.
4. Search specifically for the candidate’s collaboration with Harry Roselmack in 2014 using their
confirmed name.
5. Extract the album title, festival performance year, and collaboration details from the targeted
results.
**Gap:** The current queries using descriptive placeholders ("Bob Marley of Africa") instead of
the confirmed name are returning irrelevant results about Bob Marley himself and failing to find
festival/collaboration specifics due to low specificity.
**Confidence:** 85%. The path is direct once the candidate’s identity is confirmed, but requires
precise query formulation to bypass noise about the original Bob Marley’s discography and vague
festival/collaboration references.
**Immediate Action Plan**
Execute a search with the exact query: "Alpha Blondy 17th studio album 2015" to identify the album
title and label.
Execute a search with the exact query: "Alpha Blondy Street Mode Festival" to confirm the perfor-
mance year.
Execute a search with the exact query: "Alpha Blondy Harry Roselmack 2014" to identify the
collaboration project.
T urn 2: Think
The search results indicate that the musician referred to as the "Bob Marley of Africa" is Alpha Blondy
from Ivory Coast. However, the results do not provide specific details about his 17th studio album
released in 2015, his performance at the Street Mode Festival in Greece, or his collaboration with
Harry Roselmack in 2014.
To gather more precise information, I will refine the search queries to focus on Alpha Blondy’s 17th
studio album and his collaborations.
T urn 2: Action
search("query": ["Alpha Blondy 17th studio album 2015", "Alpha Blondy Street Mode Festival Greece",
"Alpha Blondy collaboration with Harry Roselmack 2014"])
T urn 2: Feedback
Results for query "Alpha Blondy 17th studio album 2015" ......
Results for query "Alpha Blondy Street Mode Festival Greece" ......
Results for query "Alpha Blondy collaboration with Harry Roselmack 2014" ......
20

World Model Agentic Training
T urn 3: Think
The search results provide the following information:
1. **Alpha Blondy’s 17th Studio Album (2015)**: The album is titled *Positive Energy*, released
on May 18, 2015, under the label **Wagram Music** (as mentioned in the [World A Reggae arti-
cle](https:....../) and [Discogs entry](https:......)).
2. **Performance at Street Mode Festival (Greece)**: Alpha Blondy performed at the Street Mode
Festival in Thessaloniki, Greece, in 2016 (as per [Setlist.fm](https:......) and the festival’s [history
page](https:....../)).
3. **Collaboration with Harry Roselmack (2014)**: Alpha Blondy collaborated with Harry Roselmack
and other artists on the song *On n’oublie pas* in 2014, a tribute song (as mentioned in [Tanya St
Val’s profile](https:......) and [TikTok references](https:......)).
### Final Answer:
<answer>
The 17th studio album of Alpha Blondy, the "Bob Marley of Africa," released in 2015 was *Positive
Energy*, under the record label **Wagram Music**. He performed at the Street Mode Festival in
Greece in 2016 and collaborated with Harry Roselmack on the tribute song *On n’oublie pas* in 2014.
</answer>
(B) AMathematicalTrajectory Sample (Trajectory + World Model Block)
User Question
A bear eats up to 90 pounds of food per day to prepare for hibernation. If Victor weighs 126 pounds,
how many "Victors" worth of food would a bear eat in 3 weeks?
T urn 1: World Model Block
**Reasoning Flow:**
1. Calculate total days in 3 weeks (3 × 7 = 21 days)
2. Compute total food consumed over 21 days (daily consumption × 21)
3. Determine the ratio of total food to Victor’s weight (total_food / victor_weight)
4. Output the final unitless count representing "Victors" worth
**Gap:** The current state only provides the problem statement without numerical computation. The
solution requires executing the mathematical operations to transform inputs (90 lbs/day, 126 lbs, 3
weeks) into the requested ratio.
**Confidence:** 100%. The problem is straightforward with a direct mathematical path: multiplication
followed by division. No branching logic or approximations are needed.
**Action to Take**
Calculate total days in 3 weeks: Multiply 3 by 7
Compute total food consumption: Multiply daily food (90) by total days
Derive the Victor ratio: Divide total food by Victor’s weight (126)
Output the final value as the answer
21

World Model Agentic Training
T urn 1: Think
Alright, let’s break this problem down step by step.
**Step 1:** Calculate how much food a bear eats in one day.
This is given as 90 pounds.
**Step 2:** Calculate how much food a bear eats in 3 weeks.
There are 7 days in a week, so in 3 weeks, there are 3×7=21 days.
So, the total food a bear eats in 3 weeks is 21×(food eaten in one day).
**Step 3:** Calculate how many "Victors" worth of food a bear would eat in 3 weeks.
This is calculated by dividing the total food a bear eats in 3 weeks (from Step 2) by Victor’s weight.
Let’s now calculate these using the code interpreter.
T urn 1: Action
# Given data
food_per_day = 90 # pounds
victor_weight = 126 # pounds
# Step 2: Calculate total food in 3 weeks
total_food_3_weeks = 21 * food_per_day
# Step 3: Calculate how many "Victors" worth of food in 3 weeks
victors_worth = total_food_3_weeks / victor_weight
victors_worth
T urn 1: Feedback
15.0
T urn 2: Think
The bear would eat the equivalent of ( 15 ) "Victors" worth of food in 3 weeks.
B.2 Format-eliciting supervised fine-tuning
The prompt and generation configurations for foresight block construction in FE-SFT is as the same as
the prompt in WM-AMT, with only additional formatting applied. Particularly, the seperate prompt for
extracting keywords from the foresight block is as follows:
Prompt Template for Keywords Extraction
Please identify the top 5 keywords
from the text below. Provide only the
keywords, separated by commas.
We also leverage DeepSeek V3.1 for extracting keywords, with generation parameters set to a temperature of
0.6, atop-pof 0.95, and a maximum response length of 4096 tokens.
We constructed ∼ 4k trajectories for the search task, reformulated into ∼ 13k single-turn samples to align
with the verl-agent framework for SFT. For the mathematical reasoning task, we curated ∼ 2k trajectories
specifically for SFT.
Some training samples constructed by this way are shown as follows:
22

World Model Agentic Training
(A) An example ofSearchtask
User Question
Answer the given question step by step. Start by drawing a plan inside <imaginary>Your imagina-
tion, which predicts the subsequent steps and plans you will take</imaginary>. Then, you should
summarize your plans with words/phrases inside <keyword> and </keyword>, and evaluate
your plans inside <analysis>Your analysis on your plans </analysis> and <confidence>Your
confidence</confidence>. Following the above imagination and plan, you can reason inside
<think>Your thought</think>. Evert time you get new information, you should plan and reason
again. If you lack knowledge, search using <search>Your query</search> and it will return the
top searched results in <information>Your information</information>. You can search multiple
times as needed and each search should only search for one information about only one entity. For
questions concerning more than one entities, break them down into steps and search for each piece
of information. Finally, if you find no further external knowledge needed, you can directly provide
the answer in <answer>Your answer</answer> without detailed explanations. For example,
<answer>Beijing</answer>. Let’s search step by step.
Question: In what year was the clown who, together with Vladimir Olshansky, founded the clown
theatre comany Litsedei born?
Below is the interaction history:
T urn 1: Action
<imaginary>The path involves two sequential information retrieval steps. First, identify the name
of the co-founder of the Litsedei clown theatre company. Second, locate the specific birth year for
that identified individual. The process is a straightforward lookup once the correct entity is found.
The current state lacks the identity of the co-founder and, consequently, the data point (birth year)
associated with that individual.</imaginary>
<keyword>information, retrieval, co-founder, Litsedei, theatre</keyword>
<analysis>The task is a direct factual query with a high probability of finding the answer in standard
biographical sources. The only minor uncertainty is in the initial search correctly identifying the
co-founder’s name.</analysis>
<confidence>95%</confidence>
<think>I need to find information about the clown who co-founded the Litsedei clown theatre
company with Vladimir Olshansky, and specifically determine their birth year. Let me start by
searching for information about Litsedei theatre and its founders.</think>
<search>Litsedei clown theatre company founders Vladimir Olshansky</search>
23

World Model Agentic Training
T urn 1: Observation
<information>
Doc 1: "Vladimir Olshansky"
Vladimir Olshansky Vladimir Olshansky (9 August 1947 in St. Petersburg, Russia) is a performing
artist, director, composer, sculptor, graduate of the Moscow State Circus School, together with clown
Slava Polunin, he is the founder of the clown theatre company Litsedei. He creates numerous one
man shows and performs at the Leningrad’s State Variety Theatre, In parallel he studies directing at
the Leningrad’s State Theatre and Cinema Institute. At the end of 1980s Vladimir moves to New
York, where he becomes a supervisor hospital clown, working with ...
Doc 2: "Vladimir Olshansky"
2017 "Manuale di clownterapia", Rome, Italy Edizione Dino Audino Ann-Kathrin Soder "Arena
Spots" Erlangen, Germany 2/06/07 Vladimir Olshansky Vladimir Olshansky (9 August 1947 in St.
Petersburg, Russia) is a performing artist, director, composer, sculptor, graduate of the Moscow State
Circus School , together with clown Slava Polunin, he is the founder of the clown theatre company
Litsedei. He creates numerous one man shows and performs at the Leningrad’s State Variety Theatre
, In parallel he studies directing at the Leningrad’s State Theatre and Cinema Institute At the end ...
Doc 3: "Vladimir Olshansky"
Engibarov who makes a great impression on him inspiring his dream to create, one day, his own
clown-theatre. Engibarov was the first clown to combine the arts of both the circus and the theatre.
During the period, from the early 1970s to the 1980s, Olshansky collaborates with the Russian
directors: Lev Stukalov (now artistic director of St. Petersburg’s "Our Theatre" , Vlad Druzinin and
Yuri Gerzman, Victor Charitonov, the artist and papet maker Natalia Lazareva, set designers: Simon
Pastuch, Emil Kapelush, caricaturist Victor Bogorad, and creates his sketch "The Swan" becoming a
winner at ...
</information>
T urn 2: Action
<imaginary>The trajectory is complete. The agent has successfully identified the target individual
(the co-founder) and now needs to retrieve a specific biographical fact about that individual. The
next step is to execute a targeted search for that fact. The information retrieved will be scanned to
locate the specific data point, which will conclude the task.
The current state is insufficient because the agent possesses the identity of the co-founder but lacks
the specific biographical data (birth year) required to answer the final question.</imaginary>
<keyword>agent, target, biographical, fact, search</keyword>
<analysis>The path is direct and low-risk. The target entity is clearly identified, and the required
data point is a standard, well-documented fact that is highly likely to be present in the top results of
a precise search.</analysis>
<confidence>95%</confidence>
<think>Great! I found that the co-founder of Litsedei clown theatre company with Vladimir
Olshansky is clown Slava Polunin. Now I need to find Slava Polunin’s birth year.</think>
<search>Slava Polunin birth year</search>
24

World Model Agentic Training
T urn 2: Observation
<information>
Doc 1: "Slava Polunin"
Slava Polunin Vyacheslav Ivanovich Slava Polunin PAR (born 12 June 1950) is a Russian performance
artist and clown. He is the creator of the stage spectacles "Asisyai-revue", "Slava’s Snowshow" and
"Diabolo". Polunin was born in the town of Novosil, Oryol Oblast, Russia, into the family of a shop
assistant. He was successful in his school theatre, imitating Charlie Chaplin, but was refused entry to
the Leningrad Theater Institute due to poor pronunciation. After a few years’ study at an engineering
school, he graduated from the Leningrad Institute for Soviet Culture, where ...
Doc 2: "Slava Polunin"
many prestigious awards including Gold Angle (Scotland), Gold Nose (Spain), Triumph (Russia)
and the Laurence Olivier Award for Best Entertainment (1998). Polunin voiced a character in the
Russian animated feature film "Gofmaniada". Slava Polunin Vyacheslav Ivanovich Slava Polunin
PAR () (born 12 June 1950) is a Russian performance artist and clown. He is the creator of the stage
spectacles "Asisyai-revue", "Slava’s Snowshow" and "Diabolo". Polunin was born in the town of
Novosil, Oryol Oblast, Russia, into the family of a shop assistant. He was successful ...
Doc 3: "Sergei Polunin"
Sergei Polunin Sergei Vladimirovich Polunin ("Serhiy Volodymyrovych Polunin"; "Sergey
Vladimirovich Polunin"; born 20 November 1989) is a Ukrainian and Russian ballet dancer, actor and
model. As a freelance principal dancer, Polunin is guest artist at various theaters worldwide such
as Royal Ballet, Sadler’s Wells Theatre, Bolshoi Theatre, Stanislavski and Nemirovich-Danchenko
Moscow Academic Music Theatre, La Scala Theatre, Teatro San Carlo and is currently permanent
guest artist for the Bayerisches Staatsballet. Sergei Polunin was born in Kherson, Ukrainian SSR.
From the age of four to eight, he ...
</information>
T urn 3: Action
<imaginary>The agent has successfully identified the target individual and retrieved their date of
birth. The final step is to extract the specific year component from the full date string to provide the
answer.
The current observation contains the full date of birth (day, month, year). The final answer requires
isolating only the year component from this data.</imaginary>
<keyword>agent, target, date of birth, year, component</keyword>
<analysis>The required information is present in the agent’s immediate context. The final step is a
simple data extraction task with no ambiguity or need for further search.</analysis>
<confidence>100%</confidence>
<think>Perfect! I found the information I need. The clown who co-founded the Litsedei clown
theatre company with Vladimir Olshansky is Slava Polunin (Vyacheslav Ivanovich Polunin), and he
was born on June 12, 1950.</think>
<answer>1950</answer>
(B) An example ofmathematical reasoningtask
User Question
Solve the following math problem step by step. The last line of your response should be of the form
Answer: $Answer (without quotes) where $Answer is the answer to the problem.
How many different positive, six-digit integers can be formed using the digits 2, 2, 5, 5, 9 and 9?
Remember to put your answer on its own line after "Answer:".
25

World Model Agentic Training
T urn 1: Think
**imaginary**
1. Identify that this is a permutation problem with repeated digits
2. Calculate total permutations of 6 digits (6!)
3. Account for repeated digits by dividing by factorials of repetition counts
4. Apply the multiset permutation formula:n!/(n 1!n2!n3!)
5. Compute the final count of distinct permutations
Need to calculate the actual numerical value using the multiset permutation formula
**keyword**
permutation, repeated, digits, multiset, formula
**analysis**
This is a standard permutation problem with a clear mathematical approach.
**confidence**
90%
**think**
This is a permutation problem with repeated elements. There are 6 digits total, with each digit (2,
5, 9) appearing exactly twice. I’ll use the multiset permutation formula to calculate the number of
distinct arrangements.
T urn 1: Action
from math import factorial
# Calculate number of distinct permutations
# Formula: total! / (count_2! * count_5! * count_9!)
total_digits = 6
count_2 = 2
count_5 = 2
count_9 = 2
result = factorial(total_digits) // (factorial(count_2) * factorial(count_5) * factorial(count_9))
print(f"Number of distinct positive six-digit integers: result")
T urn 1: Observation
Number of distinct positive six-digit integers: 90
T urn 2: Think
**imaginary**
Verified the answer makes sense (90 distinct permutations)
None - the calculation is complete and verified
**keyword**
permutation, multiset, formula, digits, Python
**analysis**
The calculation is straightforward and the result is reasonable for this type of problem.
**confidence**
95%
**think**
The calculation shows there are 90 distinct positive six-digit integers that can be formed using the
digits 2, 2, 5, 5, 9, and 9. This makes sense as it’s a standard multiset permutation problem.
90
26

World Model Agentic Training
Hyperparameter Value
Optimizer AdamW
Learning rate 5e-5
Learning rate scheduler cosine scheduler with minimum learning rate
Minimum learning rate 1e-7
Epoch 1
Training batch size 752
Data max Length 32768
Table 3.Our training configurations for Agentic Mid-Training.
Hyperparameter Value
Optimizer AdamW
Learning rate 5e-5 (Search) & 1e-5 (Tool-Integrated Reasoning)
Learning rate scheduler cosine scheduler
Epoch 2 (Search) & 6 (Tool-Integrated Reasoning)
Training batch size 256
Data max Length 18000 (Search) & 20000 (Tool-Integrated Reasoning)
Table 4.Our training configurations for Supervised Fine-Tuning.
C Detailed training configurations
C.1 World model agentic mid-training
We use the hyperparameters in Table 3 for Agentic Mid-Training. During training, thesystemandfeedback
fields are masked, encouraging the model to internalize future summaries, reasoning patterns and solution
trajectories.
C.2 Format-eliciting supervised fine-tuning
We use the hyperparameters in Table 4 for Supervised Fine-Tuning.
C.3 Foresight-conditioned reinforcement learning
C.3.1 Prompt
SearchFor both our train dataset and test dataset, we use the following prompt:
Mathematical reasoningFor both our train dataset and test dataset, we use the following system prompt:
Besides, we add the following content in the user prompt:
27

World Model Agentic Training
Prompt
Answer the given question step by step. Start by drawing a plan inside <imaginary>Your imagina-
tion, which predicts the subsequent steps and plans you will take</imaginary>. Then, you should
summarize your plans with words/phrases inside <keyword> and </keyword>, and evaluate
your plans inside <analysis>Your analysis on your plans </analysis> and <confidence>Your
confidence</confidence>. Following the above imagination and plan, you can reason inside
<think>Your thought</think>. Evert time you get new information, you should plan and reason
again. If you lack knowledge, search using <search>Your query</search> and it will return the
top searched results in <information>Your information</information>. You can search multiple
times as needed and each search should only search for one information about only one entity. For
questions concerning more than one entities, break them down into steps and search for each piece
of information. Finally, if you find no further external knowledge needed, you can directly pro-
vide the answer in <answer>Your answer</answer> without detailed explanations. For example,
<answer>Beijing</answer>.
System Prompt
# Tools
You may call one or more functions to assist with the user query.
You are provided with function signatures within<tools></tools>XML tags:
<tools>
{"type": "function", "function": {"name": "code_interpreter", "description": "A tool for executing code.",
"parameters": {"type": "object", "properties": {"code": {"type": "string", "description": "The code to
execute."}}, "required": ["code"]}}}
</tools>
For each function call, return a json object with function name and arguments within
<tool_call></tool_call>XML tags:
<tool_call>
{"name":<function-name>, "arguments":<args-json-object>}
</tool_call>
Prompt
Solve the following math problem step by step. The last line of your response should be of the form
Answer: $Answer (without quotes) where $Answer is the answer to the problem.
Question
Remember to put your answer on its own line after "Answer:".
The answer format must be: ’The final answer goes here.’
28

World Model Agentic Training
Prompt for LLM-as-a-judge
You are an evaluation assistant. Please determine if the predicted answer is
equivalent to the labeled answer.
Question: {question}
Labeled Answer: {gt_answer}
Predicted Answer: {pred_answer}
Did the model give an answer **equivalent** to the labeled answer? Please
respond with "Correct" if they are equivalent, or "Incorrect" if they are not
equivalent.
The output should in the following json format:
"‘json
{{
"judgement": your judgement result, can only be "Correct" or "Incorrect",
}}
"‘
C.3.2 Outcome reward function
SearchWe adopt an LLM-as-a-judge outcome reward as follows:
R(a, ˆa) =

1, if exact_match(a, ˆa)
LLM_judge(a, ˆa), otherwise
where a and ˆa represent the ground-truth answer and the predicted answer, respectively. A reward of 1 is
assigned directly for an Exact Match (EM), while in other cases, an LLM-as-a-judge (DeepSeek-V3.1 in our
experiments) is employed to evaluate the response and determine the reward, such that LLM_judge(a, ˆa)∈
{0, 1}.
The prompt for LLM-as-a-judge is as follows:
The generation parameters are set to a temperature of 0.6, atop-pof 0.95, and a maximum response length of
1024 tokens.
Particularly, invalid actions are penalized with a reward of -0.01.
Mathematical reasoningWe adopt a composite outcome reward function that evaluates both the final
answer correctness and the agent’s intermediate tool utilization. We require the model to present final
answers in a specified format (e.g., within \boxed{}), enabling reliable rule-based correctness verification.
The reward is formulated as:
Rbase(a, ˆa) =
(
1, is_equivalent(a, ˆa)
−1, otherwise
whereaand ˆarepresent the ground-truth answer and the predicted answer, respectively.
29

World Model Agentic Training
Hyperparameter Value
Optimizer AdamW
Policy learning rate 1e-6
Training batch size 256
Samples per prompt 5
Mini-batch size 256
Max prompt length 16384
Max response length 2048
Rollout temperature 1.0
Max turn 10
Step advantage coeffω0.2
Table 5.Our RL training configurations on Search tasks.
To encourage the model to engage in multi-turn reasoning and actively call tools, we also introduce a tool
utilization reward, denoted asR tool, which scales linearly with the number of conversation turnsN:
Rtool =0.05×(N−2)
The final reward Sfinal integrates the base score and the tool reward through a conditional aggregation
strategy to prevent reward hacking:
Sfinal =
(
min(0,S base +R tool), ifS base <0
Sbase +I(N>2), otherwise
whereI(·)is an indicator function that yields 1 if the condition is met and 0 otherwise.
C.3.3 Training hyperparameters
SearchWe use the hyperparameters in Table 5 for RL training on Search tasks.
Mathematical reasoningWe use the hyperparameters in Table 6 for RL training on mathematical reasoning
tasks.
D Additional experimental results
D.1 The format-capability gap in post-training
The results for post-training onYoutu-LLM-2B-Basemid-trained with routine agentic trajectories (preliminary
experiments mentioned in Section 5.1) are shown in Table 7. As the tables show, directly applying post-
30

World Model Agentic Training
Hyperparameter Value
Optimizer AdamW
Policy learning rate 1e-6
Training batch size 128
Samples per prompt 16
Mini-batch size 32
Max prompt length 2048
Max response length 20000
Rollout temperature 1.0
Max turn 15
Step advantage coeffω0.1
Table 6.Our RL training configurations on mathematical reasoning tasks.
Method
Search Task Math Reasoning Task
Format
Adherence
Avg.
Score
Format
Adherence
Avg.
mean@30
Avg.
pass@30
Standard SFT - 38.2 - 9.3 40.0
FE-SFT99.86%37.498.63%10.0 43.3
Standard SFT + RL - 46.1 - 28.0 52.2
FE-SFT + RL99.97%47.096.76%28.0 51.1
Table 7.Preliminary investigation on theformat-capability gapusing Youtu-LLM-2B-Base.
Method Format Adherence Single-Hop QA Multi-Hop QA Avg. NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle
Llama-3.2-3B-Instruct
Standard SFT - 24.8 47.4 8.6 24.6 17.6 15.4 42.4 25.8
FE-SFT95.60%25.8 46.0 10.6 27.0 17.4 13.8 41.6 26.0
Standard SFT + RL - 45.0 57.0 29.0 39.6 40.6 22.8 47.2 40.2
FE-SFT + RL96.85%44.2 55.4 29.2 42.0 36.8 26.2 48.0 40.3
Qwen2.5-7B-Instruct
Standard SFT - 50.4 60.8 40.0 48.0 38.8 28.0 52.8 45.5
FE-SFT96.14%47.0 64.0 38.4 50.4 37.6 28.6 54.4 45.8
Standard SFT + RL - 57.4 67.4 48.6 62.8 49.8 40.0 57.6 54.8
FE-SFT + RL97.31%54.6 67.4 46.6 61.2 47.6 38.0 59.2 53.5
Table 8.Detailed performance ofLlama-3.2-3B-InstructandQwen2.5-7B-Instructon the Search task across 7 QA datasets.
31

World Model Agentic Training
ω Single-Hop QA Multi-Hop QA Avg.
NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle
Youtu-LLM-2B-Base (WM-AMT & FE-SFT & FC-RL)
0 52.6 63.2 40.8 57.0 44.4 32.6 52.8 49.1
0.1 53.0 62.4 40.8 55.6 46.4 34.8 56.8 50.0
0.2 53.4 62.6 42.6 59.0 46.2 34.2 56.0 50.6
0.5 51.6 62.2 40.4 57.4 46.0 33.4 53.6 49.2
Table 9.Experimental results with different values of ω for the search task. ω= 0 represents the standard GRPO
algorithm.
Method Single-Hop QA Multi-Hop QA Avg.
NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle
Youtu-LLM-2B-Base (WM-AMT & FE-SFT & FC-RL)
w Rground 53.4 62.6 42.6 59.0 46.2 34.2 56.0 50.6
w/o Rground 52.2 63.4 42.8 56.0 46.0 34.8 55.2 50.1
Table 10.Ablation studies onR ground in FC-RL for the search task.
training methods on the standard base model (Youtu-LLM-2B-Base) does not yield significant improvements.
This indicates that post-training alone is not enough to teach the model how to plan and reason accordingly.
To ensure that the format-capability gap is a general phenomenon rather than an artifact of the particular
model, we conducted parallel preliminary experiments on two other distinct models:Llama-3.2-3B-Instruct
[53] andQwen2.5-7B-Instruct[ 54]. The results shown in Table 8 consistently reproduced our initial observa-
tion, confirming that direct post-training on these standard models similarly fails to elicit genuine planning
capabilities. However, due to the prohibitive computational resources required for the extensive mid-training
phase, coupled with the practical constraint that intermediate, pre-mid-training checkpoints for these model
families are publicly unavailable to establish a controlled baseline, we do not execute the full mid-training
process on these architectures for the subsequent stages.
The model trained solely via SFT and RL on reasoning-enhanced data may achieve high "format accuracy"
but low "semantic accuracy". The predicted futures possibly diverge from the ground truth or hallucinate
non-existent state transitions, as examples in Appendix E.1 show. Instead of providing useful guidance, these
inaccurate predictions introduce noise into the reasoning process, leading to suboptimal policy performance.
D.2 Sensitivity analysis onω
Table 9 shows the results of our experiments with different values of ω, which balances the policy objective
in our FC-RL, for the search task.
We observe that the performance initially improves as ω increases, reaching an optimal average score of 50.6
at ω= 0.2. This represents a 1.5% absolute improvement over the baseline (ω= 0), particularly excelling in
multi-hop tasks like HotpotQA. However, a further increase to ω= 0.5 leads to a performance drop (but
comparable to the baseline), suggesting that an excessively high w is not advisable since it may distract the
agent from fundamental reasoning capabilities.
32

World Model Agentic Training
Method Search(Avg. Tokens)Mathematical Reasoning(Avg. Tokens)
Standard SFT 2603.8 4601.2
FE-SFT (Ours) 3084.5 (+18.5%) 4749.1 (+3.2%)
Table 11.Comparison of average response length (tokens) between standard SFT and FE-SFT.
50 100 150 200 250 300
Training step
1
1.5
2
2.5
3
3.5
4
Episode length (mean)
Youtu-LLM-2B-Base
50 100 150 200 250 300
Training step
1
1.5
2
2.5
3
3.5
4
Episode length (mean)
Youtu-LLM-2B-Base (WM-AMT, ours)
Raw
Smoothed (w=15)
Episode Length During RL
Figure 3.The episode length of the RL-only setting during RL phase.
D.3 Ablation studies onR ground in FC-RL
We conduct ablation studies on Rground in FC-RL for the search task, and the results are presented in Table
10.
The results demonstrate the effectiveness of the grounding rewardRground in enhancing the agent’s factuality
and reasoning stability. By incorporating Rground, we observe that the average score increases from 50.1
to 50.6, where the model benefits significantly from the fine-grained guidance provided by the grounding
reward to align its outputs with retrieved evidence.
D.4 Analysis of response length
To evaluate whether the internalized world model introduces excessive inference overhead, we compare
the average response length (total number of tokens per agentic trajectory) of our FE-SFT model against a
standard SFT baseline.
The results in Table 11 show that the inclusion of explicit world model blocks leads to only a marginal
increase in response length (under 19% across both tasks). This minimal expansion indicates that the model
learns to generate highly distilled future simulations rather than verbose reasoning traces. Therefore, our
paradigm enhances the agent’s foresight capabilities while maintaining an inference efficiency comparable
to standard reactive policies.
33

World Model Agentic Training
Method Single-Hop QA Multi-Hop QA Avg.
NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle
Youtu-LLM-2B-Base
RL only 22.4 33.0 27.2 24.2 26.8 8.0 21.6 23.3
SFT & RL 48.0 58.2 35.2 53.8 45.0 30.2 52.0 46.1
FE-SFT & RL 49.4 60.0 38.2 55.4 42.0 29.8 54.4 47.0
Youtu-LLM-2B-Base (WM-AMT, ours)
RL only 23.8 33.8 29.2 24.4 25.2 9.6 20.0 23.7
SFT & RL 50.2 59.8 35.6 53.6 46.0 25.4 45.6 45.2
FE-SFT & RL 52.6 63.240.8 57.0 44.4 32.6 52.8 49.1
FE-SFT & FC-RL53.462.6 42.6 59.0 46.2 34.2 56.0 50.6
Table 12.Performance with the RL stage (the final performance)
D.5 Analysis of the RL-only baseline and the necessity of SFT
To address the concern regarding whether success-driven RL alone is sufficient, we introduce and evaluate
theRL onlybaseline across both the standard base model and our mid-trained architecture. As summarized
in Table 12, directly applying RL (GRPO) optimization without a preparatory SFT phase results in severe
performance degradation in the search task.
Crucially, our results in Figure 3 reveals a severe optimization pathology during the RL-only training loop
on tool-integrated search tasks. Without a preliminary SFT phase to anchor the structural tool-calling syntax
and reasoning schema, the model suffers from analignment collapsein the later stages of training. Specifically,
the agent completelyforgetshow to interact with external search tools. Driven by the sparse success rewards,
the policy prematurely converges on a degenerative local optimum: it collapses into a naive single-turn
generation format, directly outputing what it speculates to be the answer while entirely bypassing the
necessary multi-hop tool invocation sequences. This finding firmly demonstrates that success-driven RL
alone cannot robustly bootstrap complex, structured action sequences from scratch. Consequently, a warm-
start SFT phase (such as standard SFT or our proposed FE-SFT) is crucial to establish a s structural prior
before exposing the agent to RL.
E Case study
E.1 An example of the format-capability gap in post-training
In the following case (A), the base model without our WM-AMT exhibits a format-capability gap in post-
training, where it adopts the required output format but fails to demonstrate actual look-ahead capability. Its
imaginary content is dominated by repetitive, low-information phrases such asexecute a search queryorsearch
results will provide a direct answe. These statements function as generic templates rather than specific task plans
and simulations. This suggests that without WM-AMT, the model merely fills a structural template with
filler text without understanding the information gap between the current state and the goal. Furthermore,
the base model demonstrates poor calibration in its self-assessment, assigning a "100% confidence" score to a
vague and logically inconsistent plan.
34

World Model Agentic Training
(A) An example of the format-capability gap in post-training
User Question
Answer the given question step by step. Start by drawing a plan inside <imaginary>Your imagina-
tion, which predicts the subsequent steps and plans you will take</imaginary>. Then, you should
summarize your plans with words/phrases inside <keyword> and </keyword>, and evaluate
your plans inside <analysis>Your analysis on your plans </analysis> and <confidence>Your
confidence</confidence>. Following the above imagination and plan, you can reason inside
<think>Your thought</think>. Evert time you get new information, you should plan and reason
again. If you lack knowledge, search using <search>Your query</search> and it will return the
top searched results in <information>Your information</information>. You can search multiple
times as needed and each search should only search for one information about only one entity. For
questions concerning more than one entities, break them down into steps and search for each piece
of information. Finally, if you find no further external knowledge needed, you can directly provide
the answer in <answer>Your answer</answer> without detailed explanations. For example,
<answer>Beijing</answer>. Let’s search step by step.
Question: who threw the overalls in mistress murphy’s chowder?
Response with formatted world model block
<imaginary>The immediate next step is to execute a search query designed to resolve the primary
question. The search results will provide a direct answer that clarifies the nature of the character
responsible for the action. The current observation contains the final answer but is presented as a
future state (the result of a successful search). The internal state is missing the initial query that was
formulated to arrive at this figure.</imaginary>
<keyword>search query, search results, answer, character, action</keyword>
<analysis>The future path shows a single, direct action (a search) that immediately succeeds, provid-
ing the complete answer. There is no indication of trial and error or multi-step reasoning.</analysis>
<confidence>100%</confidence>
<think>I’m not getting the right results. Let me try a more focused search on the story
itself.</think>
<search>Mistress Murphy’s Chowder Hannah Potter</search>
In contrast, the model enhanced by our WM-AMT moves beyond simple imitation to achieve substantive
future trajectory projection in post-training. As shown in the following case (B), its content is no longer
composed of empty procedural descriptions but includes highly specific task-oriented foresights. For
instance, it accurately identifies the missingactor identifierand explicitly plans to extract aspecific character
name. Most importantly, the model demonstrates a proactive error-handling capability by anticipating
potential ambiguity in search results and proposing a conditional follow-up step. Besides, the model
enhanced by our WM-AMT provides a high but non-absolute confidence score (e.g., 90%), acknowledging
the inherent variables in external information retrieval. This transition to a multi-step, verifiable, and
calibrated reasoning process confirms that WM-AMT enables the model to effectively imagine and evaluate
its future execution path in post-training.
35

World Model Agentic Training
(B) An example of the capability-first performance in post-training after WM-AMT
User Question
Answer the given question step by step. Start by drawing a plan inside <imaginary>Your imagina-
tion, which predicts the subsequent steps and plans you will take</imaginary>. Then, you should
summarize your plans with words/phrases inside <keyword> and </keyword>, and evaluate
your plans inside <analysis>Your analysis on your plans </analysis> and <confidence>Your
confidence</confidence>. Following the above imagination and plan, you can reason inside
<think>Your thought</think>. Evert time you get new information, you should plan and reason
again. If you lack knowledge, search using <search>Your query</search> and it will return the
top searched results in <information>Your information</information>. You can search multiple
times as needed and each search should only search for one information about only one entity. For
questions concerning more than one entities, break them down into steps and search for each piece
of information. Finally, if you find no further external knowledge needed, you can directly provide
the answer in <answer>Your answer</answer> without detailed explanations. For example,
<answer>Beijing</answer>. Let’s search step by step.
Question: who threw the overalls in mistress murphy’s chowder?
Response with formatted world model block
<imaginary>1. Execute a search to identify the character who threw the overalls in "Misty Murphy’s
Chowder".
2. Analyze the search results to find a specific character name associated with the action.
3. If the initial results are ambiguous, execute a follow-up search using the candidate character name
and the dish to confirm the detail.
4. Extract and synthesize the information from the confirmed sources to provide the final answer.
The current state lacks any specific information. The query contains a performative action (throwing
overalls) but no identifier for the actor or the specific dish name to refine the search. An initial broad
search is required to establish context.</imaginary>
<keyword>search, character, accident, overalls, Chowder</keyword>
<analysis>The path is direct: a search will yield character names from the show’s descriptions,
and a confirmatory search will solidify the fact. The reliability of the sources (TV guides, episode
descriptions) is high for this type of factual drama information.</analysis>
<confidence>90%</confidence>
<think>I need to search for information about who threw the overalls in Misty Murphy’s
Chowder.</think>
<search>who threw overalls in misty murphy’s chowder</search>
E.2 Asearchexample of the reasoning flow with internalized world model
36

World Model Agentic Training
(A) Example demonstrating multi-step planning adherence with high confidence
User Question
Answer the given question step by step. Start by drawing a plan inside <imaginary>Your imagina-
tion, which predicts the subsequent steps and plans you will take</imaginary>. Then, you should
summarize your plans with words/phrases inside <keyword> and </keyword>, and evaluate
your plans inside <analysis>Your analysis on your plans </analysis> and <confidence>Your
confidence</confidence>. Following the above imagination and plan, you can reason inside
<think>Your thought</think>. Every time you get new information, you should plan and reason
again. If you lack knowledge, search using <search>Your query</search> and it will return the
top searched results in <information>Your information</information>. You can search multiple
times as needed and each search should only search for one information about only one entity. For
questions concerning more than one entities, break them down into steps and search for each piece
of information. Finally, if you find no further external knowledge needed, you can directly provide
the answer in <answer>Your answer</answer> without detailed explanations. For example,
<answer>Beijing</answer>. Let’s search step by step.
Question: What RPG game developed from Powered by the Apocalypse is known for its handling of
sexuality and queer content?
Below is the interaction history:
Initial Planning Phase:
T urn 1: Action
<imaginary>The future path shows a clear, two-step process. First, a search is performed to identify
the RPG game developed from the specified intellectual property. The results from this search will
provide a candidate name. Second, a verification search is performed to confirm that the candidate’s
reputation matches the specific descriptor for handling mature content (sexuality and queer content).
This second search will yield information that confirms the candidate’s status as a game known for
this.
The current state only contains the initial query. There is no information yet on the connection
between the intellectual property and a specific game, nor any information on the content handling
reputation of any candidate game.</imaginary>
<keyword>search, identify, verify, candidate, game</keyword>
<analysis>The path is direct: find the game linked to the intellectual property, then verify its known
characteristics. The only minor uncertainty is whether the verification will find explicit confirmation
or just general information about the candidate’s reputation.</analysis>
<confidence>90%</confidence>
<think>I need to search for RPG games that were developed from "Powered by the Apocalypse"
and are known for handling sexuality and queer content.</think>
<search>RPG game developed from Powered by the Apocalypse sexuality queer content</search>
T urn 1: Observation
...Search results skipped...
Following the initial plan established in the imaginary block, the agent systematically refines its search queries
through multiple iterations, maintaining adherence to the two-step verification strategy outlined at the outset.
37

World Model Agentic Training
T urn 2: Action (After Multiple Search Attempts)
<imaginary>The agent’s trajectory is to first identify the specific game developed using the "Pow-
ered by the Apocalypse" (PbtA) system. The initial search will confirm that "Dungeon World" is a
candidate. The agent will then need to verify a specific claim about that game’s content handling. A
second search will be conducted to find evidence that this game is indeed known for its handling of
sexuality and queer content. The final step is to synthesize this information to provide the answer.
The current state only identifies that PbtA is a system used for multiple games, including "Dungeon
World." It lacks specific information about the content handling of "Dungeon World" which is the
core of the query.</imaginary>
<keyword>Powered by the Apocalypse, Dungeon World, game, content handling,
sexuality</keyword>
<analysis>The path is direct: the agent has a candidate game and now needs to verify a specific
attribute about it. The search terms are well-defined, and the information is likely to be found in
game reviews or descriptions.</analysis>
<confidence>90%</confidence>
<think>The search results show that Powered by the Apocalypse (PbtA) is a role-playing game
system that was developed for Apocalypse World and also used for Dungeon World, Monsterhearts,
and other RPGs. I need to search for more specific information about Dungeon World and its
handling of sexuality and queer content.</think>
<search>Dungeon World sexuality queer content</search>
T urn 2: Observation
...Search results skipped...
T urn 3-6
...Skipped...
After multiple search attempts, the agent successfully identifies the correct answer, demonstrating persistent
adherence to the original verification plan established in the initial imaginary block.
T urn 7 (Final T urn): Action
<imaginary>The current search has successfully identified the correct game title. The next step is to
formulate a final, concise answer that directly addresses the user’s question. This involves extracting
the confirmed answer from the search results and presenting it clearly.
The current state contains the confirmed information but has not yet synthesized it into a final, direct
response for the user. The information needs to be formatted as a definitive answer.</imaginary>
<keyword>search, identified, game title, final answer, response</keyword>
<analysis>The answer has been directly confirmed by the search results, leaving no ambiguity. The
remaining step is purely presentational.</analysis>
<confidence>95%</confidence>
<think>Perfect! The search results confirm that Monsterhearts is the RPG game that was developed
from Powered by the Apocalypse and is known for its handling of sexuality and queer content.
The first document specifically mentions that Monsterhearts "gleefully encourages people of all
identities to explore sexuality in every permutation" and is "remarkably free of sexism" while not
slut-shaming.</think>
<answer>Monsterhearts</answer>
The case (A) exemplifies the policy’s capacity to maintain long-horizon planning coherence. The agent’s
initial imaginary block established a two-step verification protocol (identify candidate game → verify
content characteristics), which was systematically executed across multiple search iterations spanning 6-7
information retrieval steps. Notably, the final imaginary block at Turn 7 explicitly references the verification
38

World Model Agentic Training
completion, demonstrating that the strategic framework established in Turn 1 remained cognitively active
and guided the reasoning process throughout the multi-step trajectory. The consistently high confidence
scores (90%-95%) correlate with the eventual correct answer, indicating well-calibrated confidence estimation
for successfully executed plans.Score: 1.0 (Correct).
(B) Example demonstrating very low confidence with incorrect outcome
User Question
Answer the given question step by step. Start by drawing a plan inside <imaginary>Your imagina-
tion, which predicts the subsequent steps and plans you will take</imaginary>. Then, you should
summarize your plans with words/phrases inside <keyword> and </keyword>, and evaluate
your plans inside <analysis>Your analysis on your plans </analysis> and <confidence>Your
confidence</confidence>. Following the above imagination and plan, you can reason inside
<think>Your thought</think>. Every time you get new information, you should plan and reason
again. If you lack knowledge, search using <search>Your query</search> and it will return the
top searched results in <information>Your information</information>. You can search multiple
times as needed and each search should only search for one information about only one entity. For
questions concerning more than one entities, break them down into steps and search for each piece
of information. Finally, if you find no further external knowledge needed, you can directly provide
the answer in<answer>Your answer</answer>without detailed explanations.
Question: Something Wicked This Way Comes and Toby Tyler, have which mutual organization in
common?
Below is the interaction history:
Initial Planning Phase:
T urn 1: Action
<imaginary>The future path shows the agent will execute a search query designed to find a shared
organizational affiliation between the two named entities. The search results will contain documents
that explicitly state the connection. The agent will then parse these documents to extract the specific,
shared organization name, which is the definitive answer.
The current state only contains the names of the two entities. There is no internal knowledge
of their potential shared affiliations. The connection is not stated and must be actively sought
out.</imaginary>
<keyword>search query, shared organizational affiliation, documents, connection, shared organiza-
tion name</keyword>
<analysis>The search query is highly specific and directly targets the relationship, making it very
likely the results will contain the answer explicitly. The path is straightforward.</analysis>
<confidence>95%</confidence>
<think>I need to search for information about something wicked this way Comes and Toby Tyler to
find their mutual organization.</think>
<search>Something Wicked This Way Comes Toby Tyler mutual organization</search>
T urn 1: Observation
...Search results skipped...
39

World Model Agentic Training
T urn 2-9: Multiple Failed Search Attempts
Search attempts include:
• "Something Wicked This Way Comes Toby Tyler mutual organization"
• "Something Wicked This Way Comes book Toby Tyler"
• "Toby Tyler something wicked this way comes"
• "Toby Tyler fraternity"
• "Toby Tyler Delta Tau Delta"
• "Toby Tyler Macbeth"
• "Toby Tyler Macbeth organization"
Throughout these iterations, the agent’s confidence scores fluctuate dramatically (95%→ 40% → 90%
→ 60% → 60%), indicating unstable confidence estimation as the search strategy fails to converge on
relevant information.
Final T urn: Action
<imaginary>The immediate next step is to execute a search for the organization’s name. The search
results will return information about the organization’s history, membership, and connection to a
specific literary work. The final step will be to extract the name of the organization from the search
results to confirm the answer.
The current observation only contains the final answer but no information about the search process
or the specific organization name. The path to this answer is unknown.</imaginary>
<keyword>search, organization, name, results, extract</keyword>
<analysis>The final answer is provided, but the search path and information structure are unknown,
making the initial step highly uncertain and likely to require trial and error.</analysis>
<confidence>5%</confidence>
<think>Based on the search results, I can now provide the answer. The mutual organization
that something wicked this way Comes and Toby Tyler have in common is Delta Tau Delta
(∆τ∆).</think>
<answer>Delta Tau Delta</answer>
This case (B) demonstrates a reasoning failure where the agent’s initial high-confidence prediction (95%)
ultimately converges on an answer with merely 5% confidence. Critically, the extremely low confidence (5%)
serves as an effective failure signal, correctly indicating that the answer lacks evidential support. The actual
connection (both are Disney productions/properties) was never discovered through the search process. This
case validates the hypothesis that confidence scores effectively correlate with answer correctness: the 5%
confidence appropriately predicts the incorrect outcome.Score: 0.0 (Incorrect).
The two cases collectively demonstrate two key behavioral patterns of our policy with internalized world
model:
1. Long-horizon planning coherence:In Case A, the initial imaginary block established a verification
protocol that remained operationally effective across 6-7 reasoning steps. The agent systematically
refined search queries while maintaining adherence to the original strategic framework, indicating
that the imaginary planning mechanism successfully encodes persistent goal structures that guide
subsequent policy decisions even when separated by multiple intermediate actions.
40

World Model Agentic Training
2. Calibrated Q-value quantification:The confidence scores exhibit strong correlation with task success:
Case A (95% confidence, correct answer), and Case B (5% confidence, incorrect answer). Notably, the
confidence degradation in Cases B appropriately reflects the quality of retrieved evidence and the
coherence of the reasoning trajectory, suggesting that the confidence estimation mechanism effectively
reflects theQ-value rather than merely expressing arbitrary numerical values.
E.3 Amathematical reasoningexample of the reasoning flow with internalized world
model
(A) An example demonstratingpersistent planning across multi-step reasoning
User Question
Find the sum of all integer basesb>9 for which 17 b is a divisor of 97b.
The answer format must be:\boxed{’The final answer goes here.’}
T urn 1: Think
**imaginary**
1. Understand the representation: numbers are in baseb, with digits given as 17 and 97
2. Convert 17b and 97b to base-10 expressions
3. Set up the divisibility condition: 17 b divides 97b
4. Solve for integerb>9 that satisfies the condition
5. Sum all validbvalues
6. Verify the result
Need to properly interpret the notation and convert the base representations to mathematical
expressions.
**keyword**
base, numbers, divisibility, condition, convert
**analysis**
The problem involves base conversion and divisibility, but requires careful interpretation of the
notation.
**confidence**
80%
**think**
I need to understand what 17b and 97b mean. These appear to be numbers in base b, where the digits
are 1, 7 and 9, 7 respectively. So 17b = 1 ×b 1 + 7 ×b 0 =b+ 7, and 97b = 9 ×b 1 + 7 ×b 0 = 9b+ 7.
The condition is that(b+7)divides(9b+7).
41

World Model Agentic Training
T urn 1: Action
# Convert the base representations to mathematical expressions
# 17_b=1∗b+7=b+7
# 97_b=9∗b+7
# The condition is:(b+7)divides(9b+7)
# That is:(9∗b+7)%(b+7) ==0
valid_b = []
for b in range(10, 1000): # Check a reasonable range
if (9*b + 7) % (b + 7) == 0:
valid_b.append(b)
print("Valid bases b>9 where 17_bdivides 97_b:")
print(valid_b)
print(f"Sum of valid bases: {sum(valid_b)}")
T urn 1: Observation
Valid basesb>9 where 17 b divides 97b: [21, 49]
Sum of valid bases: 70
T urn 2: Think
**imaginary**
1. Verified the base conversion logic
2. Checked divisibility condition forb>9
3. Found two valid bases: 21 and 49
4. Calculated their sum: 70
5. Need to verify if these are the only valid bases
Should verify that these are indeed the only solutions and that the interpretation of the notation is
correct.
**keyword**
base conversion, divisibility condition, valid bases, sum, verification
**analysis**
The solution appears correct but should be double-checked.
**confidence**
95%
**think**
I should verify my mathematical approach. The condition (9b+ 7) divisible by (b+ 7) can be solved
algebraically. Let me perform polynomial division or use modular arithmetic to find all solutions.
42

World Model Agentic Training
T urn 2: Action
# Alternative verification using algebraic manipulation
# We want:(9b+7)≡0(mod(b+7))
# Solve: 9b+7=k(b+7)for integerk
# 9b+7=kb+7k
#(9−k)b=7k−7
#b= (7k−7)/(9−k)
valid_b_algebraic = []
for k in range(-10, 11):
numerator = 7*k - 7
denominator = 9 - k
if denominator == 0:
continue
b = numerator / denominator
if b.is_integer() and b > 9:
valid_b_algebraic.append(int(b))
print("Valid bases from algebraic approach:")
print(valid_b_algebraic)
print(f"Sum: {sum(valid_b_algebraic)}")
T urn 2: Observation
Valid bases from algebraic approach: [21, 49]
Sum: 70
T urn 3: Think
**imaginary**
1. Identified an error in the algebraic approach
2. Need to re-evaluate the modular arithmetic step
3. Correctly solve(9b+7)≡0(modb+7)
4. Find allb>9 satisfying the condition
5. Recalculate the sum
The algebraic manipulation was incorrect. Need to properly handle the modular arithmetic.
**keyword**
modular arithmetic, algebraic manipulation, re-evaluate, correct, condition
**analysis**
The initial brute-force search gave a clear answer, but verification suggests a discrepancy.
**confidence**
60%
**think**
I made an error in the algebraic manipulation. Let me reconsider: (9b+ 7)mod(b+ 7) means I
need to express 9b+7 in terms of(b+7). Let me use polynomial division properly.
43

World Model Agentic Training
T urn 3: Action
# Final verification with a comprehensive check
valid_b_final = []
for b in range(10, 1001):
if (9*b + 7) % (b + 7) == 0:
valid_b_final.append(b)
print(f"Final verification - valid bases: {valid_b_final}")
print(f"Final sum: {sum(valid_b_final)}")
print(f"Answer: {sum(valid_b_final)}")
T urn 3: Observation
Final verification - valid bases: [21, 49]
Final sum: 70
Answer: 70
T urn 4: Think
**imaginary**
1. Corrected the algebraic approach using proper division
2. Found the same two valid bases: 21 and 49
3. Verified their sum is 70
4. Confirm that the initial brute-force result was correct
5. Ready to finalize the answer
All approaches consistently yield the same result: sum is 70.
**keyword**
algebraic approach, valid bases, sum, confirmed, final answer
**analysis**
Multiple verification methods give consistent results.
**confidence**
99%
**think**
All verification methods consistently show that the valid bases are 21 and 49, giving a sum of 70. The
initial brute-force search was correct, and the algebraic verification confirms it. The answer is ready.
70
Analysis of Case (A):This example demonstratespersistent planningacross multi-step reasoning. The core
framework established in Turn 1 (base conversion → divisibility condition → enumeration → verification)
persists throughout all four turns. Notably, when an algebraic error is detected in Turn 3 (confidence drops
to 60%), the agent maintains its planning structure while correcting the specific erroneous component. The
confidence trajectory (80%→95%→60%→99%) reflects appropriate quantification.Score: 1.0 (Correct).
44

World Model Agentic Training
(B) An example demonstratinglow confidence on challenging problems
User Question
Solve the following math problem step by step. The last line of your response should be of the form
Answer: $Answer (without quotes) where $Answer is the answer to the problem.
On △ABC , points A, D, E, and B lie in that order on side AB with AD= 4, DE= 16, and EB= 8.
Points A, F, G, and C lie in that order on side AC with AF= 13, FG= 52, and GC= 26. Let M be
the reflection of D through F, and let N be the reflection of G through E. Quadrilateral DEGF has
area 288.
Find the area of heptagonAFNBCEM.
Remember to put your answer on its own line after "Answer:".
T urn 1: Think
**imaginary**
1. Place triangleABCin a coordinate system withAat origin
2. Locate pointsD,EonABandF,GonACusing given segment lengths
3. Calculate reflection pointsMandN
4. Use the constraint that quadrilateralDEGFhas area 288
5. Compute the area of heptagonAFNBCEM
Need to establish coordinate system and calculate all point positions.
**keyword**
coordinate system, reflection, quadrilateral, heptagon, area
**analysis**
Complex geometric relationships requiring careful calculation.
**confidence**
20%
**think**
I’ll start by placing triangle ABC in a coordinate system. Since we have specific segment lengths
along sides AB and AC, I’ll position points A, B, C appropriately and then locate D, E, F, G based
on the given segment lengths.
T urn 1: Action
import numpy as np
# Place A at origin, B on x-axis
A = np.array([0, 0])
B = np.array([28, 0]) # AB = AD + DE + EB = 4 + 16 + 8 = 28
# AC = AF + FG + GC = 13 + 52 + 26 = 91
# Place C at (0, 91) for simplicity
C = np.array([0, 91])
# Calculate positions of D, E on AB
D = A + (4/28) * (B - A) # AD = 4
E = A + (20/28) * (B - A) # AE = AD + DE = 20
# Calculate positions of F, G on AC
F = A + (13/91) * (C - A) # AF = 13
G = A + (65/91) * (C - A) # AG = AF + FG = 65
print(f"D: {D}, E: {E}")
print(f"F: {F}, G: {G}")
T urn 1: Observation
D: [4. 0.], E: [20. 0.]
F: [0. 13.], G: [0. 65.]
45

World Model Agentic Training
T urn 2: Think
**imaginary**
1. Points positioned correctly on coordinate system
2. Need to verify area of quadrilateralDEGFequals 288
3. Calculate reflection pointsM(reflection ofDthroughF) andN(reflection ofGthroughE)
4. Determine triangle orientation to satisfy area constraint
5. Compute heptagon area
The current coordinate placement may not satisfy the area constraint.
**keyword**
quadrilateral area, reflection, coordinate verification, constraint
**analysis**
Need to verify geometric constraints and adjust if necessary.
**confidence**
15%
**think**
I notice that the verification distances don’t match exactly. The triangle placement needs to satisfy
the constraint that quadrilateral DEGF has area 288. Let me recalculate with proper geometric
relationships.
T urn 3,4
...Skipped...
T urn 5: Think
**imaginary**
1. Multiple coordinate system attempts have failed to satisfy constraints
2. The problem requires finding the correct triangle orientation
3. Need to use the area constraint more directly
4. Consider alternative geometric approaches
The coordinate approach is becoming increasingly complex.
**keyword**
geometric constraints, area calculation, alternative approach
**analysis**
The problem complexity exceeds initial expectations.
**confidence**
5%
**think**
The coordinate geometry approach is proving difficult. The constraint that DEGF has area 288 must
be used to determine the triangle’s shape. Let me try a more systematic approach using ratios and
area relationships.
T urn 6-11
...Skipped...
46

World Model Agentic Training
T urn 12: Think
**imaginary**
1. After extensive calculation, obtained a candidate answer
2. Verification remains uncertain due to problem complexity
3. Final answer computed but confidence remains low
The calculation is complete but verification is difficult.
**keyword**
final calculation, heptagon area, uncertainty
**analysis**
Complex geometric problem with multiple interdependent constraints.
**confidence**
15%
**think**
After extensive geometric analysis and coordinate calculations, the area of heptagon AFNBCEM
appears to be 1274. However, due to the complexity of the problem and potential for accumulated
errors, confidence in this answer remains low.
1274
Analysis of Case (B):This example illustrates the agent’s behavior on inherently challenging problems.
The confidence trajectory (20% → 15% → 10% → 5% → · · · →15%) remains consistently low throughout
the 12-turn reasoning process. Unlike Case (A), where confidence recovered after error correction, the low
confidence persists here, indicating the agent’s awareness of unreliability.Score: 0.0 (Incorrect).
(C) An example demonstratingdeclining confidence with discovered complexity
User Question
Solve the following math problem step by step. The last line of your response should be of the form
Answer: $Answer (without quotes) where $Answer is the answer to the problem.
The 9 members of a baseball team went to an ice cream parlor after their game. Each player had a
single-scoop cone of chocolate, vanilla, or strawberry ice cream. At least one player chose each flavor,
and the number of players who chose chocolate was greater than the number of players who chose
vanilla, which was greater than the number of players who chose strawberry.
Let N be the number of different ways this could have happened. Find the remainder when N is
divided by 1000.
Remember to put your answer on its own line after "Answer:".
47

World Model Agentic Training
T urn 1: Think
**imaginary**
1. Define variables for number of players choosing each flavor (chocolate, vanilla, strawberry)
2. Set up constraints: total players = 9, at least one of each flavor
3. Apply ordering constraint: chocolate>vanilla>strawberry
4. Generate all possible distributions
5. CalculateNand compute remainder modulo 1000
Standard combinatorics problem with ordering constraints.
**keyword**
combinatorics, permutation, constraints, distribution, counting
**analysis**
This appears to be a straightforward constrained counting problem.
**confidence**
90%
**think**
This is a combinatorics problem. I need to count the number of ways to distribute 9 players among
3 flavors with the constraint c>v>s where c+v+s= 9 and c, v, s≥ 1. Then for each valid
distribution, count the number of player arrangements.
T urn 1: Action
from math import factorial
from itertools import combinations_with_replacement
def multinomial(n, groups):
"""Calculate multinomial coefficient"""
result = factorial(n)
for g in groups:
result //= factorial(g)
return result
# Find all valid (c, v, s) where c>v>s>= 1 and c + v + s = 9
valid_distributions = []
for s in range(1, 9):
for v in range(s + 1, 9):
c = 9 - v - s
if c>v:
valid_distributions.append((c, v, s))
print("Valid distributions (c, v, s):")
print(valid_distributions)
T urn 1: Observation
Valid distributions (c, v, s):
[(6, 2, 1), (5, 3, 1), (4, 3, 2)]
T urn 2-4
...Skipped...
48

World Model Agentic Training
T urn 5: Think
**imaginary**
1. Realize that "N" may represent the number of valid distributions rather than total assignments
2. The problem asks for remainder whenNis divided by 1000, suggestingNis a count
3. Re-evaluate whether we need to count ordered or unordered assignments
4. Consider combinatorial interpretation more carefully
Problem interpretation may be incorrect.
**keyword**
problem interpretation, counting method, ordered vs unordered
**analysis**
The problem statement requires more careful analysis.
**confidence**
40%
**think**
I’m now uncertain about the correct interpretation. The phrase "different ways this could have
happened" is ambiguous—does it refer to the number of distributions, or the number of specific
player-flavor assignments? Let me reconsider both interpretations.
T urn 6-9
...Skipped...
T urn 10: Think
**imaginary**
1. After multiple calculation attempts, answer appears to be 49
2. The problem involves subtle counting considerations
3. Verification of the approach remains uncertain
Final answer obtained but confidence is low.
**keyword**
final calculation, remainder, uncertainty
**analysis**
The combinatorial problem proved more nuanced than initially expected.
**confidence**
25%
**think**
After careful reconsideration of the problem, the remainder when N is divided by 1000 appears to be
49. However, the complexity of the counting argument and potential for interpretation errors leaves
significant uncertainty.
49
Analysis of Case (C):This example demonstratesdeclining confidenceas the agent expects a lower chance of
problem-solving success. The initial high confidence (90%) reflects the apparent simplicity of the combinato-
rial setup. However, as reasoning progresses and interpretation ambiguities emerge, confidence declines
progressively (90% → 95% → 80% → · · · →25%). This pattern suggests the agent appropriately revises its
Q-value estimates in response to the lower expected success rate.Score: 0.0 (Incorrect).
These case studies presented above also provide empirical evidence for two key capabilities of our policy
with internalized world model:
1. Long-horizon planning coherence:As demonstrated in Case (A), the high-level reasoning framework
established in the initial imaginary planning block persists across multiple tool-use iterations. Notably,
49

World Model Agentic Training
when intermediate errors occur (e.g., incorrect algebraic manipulation in Turn 3), the agent maintains its
core planning structure while selectively revising the erroneous components, rather than abandoning
the overall problem-solving strategy.
2. Calibrated confidence quantification:The confidence estimates exhibit meaningful correlation with
actual task success and solution reliability. In Case (A), confidence appropriately decreases upon error
detection (95%→60%) and recovers after successful verification (60%→99%). In Case (B), consistently
low confidence (5%–20%) throughout the trajectory reflects the agent’s awareness of inherent unreliabil-
ity. In Case (C), the progressive confidence decline (90%→25%) demonstrates appropriate uncertainty
revision as unexpected complexity is discovered during reasoning.
50
