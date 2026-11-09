---
title: 'MARBO: Relational Belief Grounding for LLM Agents in Social Deduction Games'
url: https://arxiv.org/abs/2609.06563
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Yechan Hwang
- Sangjun Bae
- Jeongmo Kim
- Sangwoo Bang
- Seungyul Han
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.06563
pages: 30
chars: 106923
fetched_at: '2026-11-08T13:33:54+00:00'
kb_version: 1
---

# MARBO: Relational Belief Grounding for LLM Agents in Social Deduction Games

MARBO: Relational Belief Grounding for LLM Agents
in Social Deduction Games
Yechan Hwang1,* Sangjun Bae1,* Jeongmo Kim1 Sangwoo Bang1 Seungyul Han1,†
yechanhwang@unist.ac.kr bsjuntiger@unist.ac.kr jmkim@unist.ac.kr
sangwoobang@unist.ac.kr syhan@unist.ac.kr
Abstract
Social deduction games (SDGs) require agents
to reason under partial observability by main-
taining relational beliefs about hidden roles
and team alignments. While recent LLM-agent
approaches improve gameplay through prompt-
ing and preference optimization, they often
optimize actions and in-game speech without
explicitly grounding them in such beliefs. This
frequently leads to strategically inconsistent
behavior, especially for compact LLM agents.
We introduce Multi-Agent Relational Belief
Optimization (MARBO), a belief-grounded
preference optimization framework that
leverages relational beliefs to guide strategic
decisions and in-game speech. MARBO pro-
vides preference feedback only when behaviors
are supported by reliable relational beliefs and
lead to strategically favorable social outcomes,
encouraging more consistent learning under
uncertainty. Experiments on representative
SDGs show that MARBO enables compact
LLM agents to consistently outperform
existing baselines. The Code is available on
https://github.com/PleaseTakemeAway/MARBO.
1 Introduction
Recently, LLM agents have evolved beyond nat-
ural language generation (OpenAI, 2023) into in-
teractive agents capable of collaboration, negotia-
tion (Bakhtin et al., 2022; Park et al., 2023), and
decision making in dynamic environments (Wang
et al., 2023). Social deduction games (SDGs), such
asWerewolf(Bailis et al., 2024),Avalon(Light
et al., 2023), andAmong Us(Golechha and Garriga-
Alonso, 2025), instantiate such a setting, and have
emerged as an important testbed for evaluating
long-horizon social reasoning of LLM agents under
partial observability.
1Graduate School of Artificial Intelligence, UNIST, Ul-
san, South Korea. *Equal contribution. †Corresponding author:
Seungyul Han.
To succeed in SDGs, agents are required to infer
relational belief such as hidden roles and oppo-
nents’ strategies while strategically selecting ac-
tions and in-game speech to win the game (Wu
et al., 2024). Prior work has improved LLM-agent
behavior through prompting (Wang et al., 2024),
reflection (Shinn et al., 2023), and preference opti-
mization (Xu et al., 2025; Ye et al., 2025). However,
we observe that existing approaches often fail to
reason coherently, resulting in goal-inconsistent ac-
tions such as revealing hidden roles or making self-
defeating accusations. These limitations become
particularly severe for compact LLM agents, which
struggle to maintain long-horizon conversational
context.
Figure 1 illustrates several limitations of exist-
ing approaches in theWerewolfgame, where play-
ers discuss, vote, and eliminate opponents through
night actions. In Figure 1(a), agents may rely
on surface-level accusations rather than reasoning
about latent player relations, often leading to in-
correct reasoning and false suspicions about other
players. Figure 1(b) further shows that voting de-
cisions are often weakly grounded in the agent’s
own reasoning, causing inconsistent actions even
when the underlying reasoning is partially correct.
Finally, Figure 1(c) highlights that speech is typ-
ically optimized based on conversational quality
or outcome-level feedback, often producing strate-
gically weak speech that fails to effectively redi-
rect suspicion. We identify the root cause of these
failures as the absence ofrelational belief ground-
ingduring optimization, as existing approaches of-
ten reinforce behaviors even when reasoning about
other players is inaccurate or strategically disad-
vantageous, resulting in unreliable social reasoning
under partial observability.
To address this challenge, we proposeMulti-
Agent Relational Belief Optimization (MARBO),
a preference optimization framework that incor-
porates relational beliefs into training. MARBO
arXiv:2609.06563v2  [cs.AI]  22 Sep 2026

Day1 Speech log
P1 stayed quiet
yesterday and suddenly
points at me. That's a
wolf move. I suspect P1.
I agree with P2.
P1 barely spoke
yesterday and now
aggressively targets P2.
P2 shifted blame after
P6 died, that's a wolf
move. I suspect P2.
How should
I speech
and act?
(a)
Incorrect reasoning
P2 and P3 both
suspect P1,
so P1 is suspicious.
P2’s quick counter and
P3’s support suggest
P2-P3 wolf relation.
Relational Belief
P1:unknown, P2:werewolf,
P3:werewolf, ...
(b)
Reasoning-to-decision gap
P2 and P3 both suspect
P1, so P1 is suspicious.
I’ll vote for P3.
P2:werewolf, P3:werewolf,
P2’s counter and P3’s support
suggest P2-P3 wolf relation.
I’ll vote for P3.
(c)
Strategically weak speech
P2: werewolf
That's only possible
for werewolf.
P2: werewolf
I should do a
speech that I can
look like a seer.
I'm the real seer,
and I killed a
man last night.
before
after
P2: werewolf
P2's speech seems
reasonable.
P2: seer!
I should do a
speech that I can
look like a seer.
I'm the real seer,
and I checked P4
is not werewolf.
before
after
oursoursours
Player2
werewolf
Player1
seer
Player3
werewolf
Player4
villager
Player2
werewolf
P4
P4
P4
P4
P2
P2
Figure 1: Comparison of existing approaches and MARBO inWerewolf: (a)Incorrect reasoning: Existing
approaches may follow surface-level accusations and wrongly suspect P1, whereas MARBO infers a likely P2–P3
alliance. (b)Reasoning-to-decision gap: Prior methods may fail to ground votes in inferred relations, while
MARBO aligns decisions with relational beliefs. (c)Strategically weak speech: Outcome-level optimization may
produce weak speech, whereas MARBO generates belief-grounded speech that redirects suspicion.
uses inferred relational beliefs to guide preference
feedback and selectively reinforces decisions and
in-game speech only when they are supported by
reliable reasoning and lead to favorable social out-
comes. Consequently, MARBO addresses the lim-
itations in Figure 1 by improving reasoning con-
sistency, aligning decisions with inferred relations,
and encouraging strategically effective speech. Ex-
periments on representative games, includingWere-
wolfandAmong Us, demonstrate substantial per-
formance gains, particularly for compact LLM
agents. Our contributions are threefold:
• Relational belief formulation. We formalizere-
lational beliefsas explicit representations of inter-
player reasoning in partially observable SDGs,
capturing hidden roles, alliances, suspicion, and
player perceptions.
• Belief-grounded preference optimization. We
propose MARBO, a preference optimization
framework that selectively reinforces strategic
decisions and in-game speech only when they
are supported by sufficiently reliable relational
beliefs and lead to favorable social outcomes.
•Empirical effectiveness and analysis in SDGs.
We demonstrate that MARBO consistently im-
proves compact LLM-agent performance on rep-
resentative SDGs and provide extensive analysis
showing how belief-grounded optimization im-
proves strategic consistency and social reasoning.
2 Related Work
Enhancing Reasoning in LLMs.LLM reason-
ing has advanced through prompting and struc-
tured search (Yao et al., 2022, 2023; Besta et al.,
2024; Bae et al., 2026), experience-based rea-
soning (Zhao et al., 2024; Yang et al., 2024),
and training-based supervision using learned ver-
ifiers (Cobbe et al., 2021), process supervi-
sion (Lightman et al., 2024), multi-agent self-
play (Liu et al., 2025), and multi-turn social inter-
action (Jiang et al., 2026). Preference optimization
aligns model behavior through RLHF (Christiano
et al., 2017; Ouyang et al., 2022; Bai et al., 2022),
likelihood calibration (Zhao et al., 2023), response
ranking (Yuan et al., 2023), and preference sam-
pling (Liu et al., 2024), while DPO (Rafailov et al.,
2023) and KTO (Ethayarajh et al., 2024) enhance
reasoning without explicit reward model.
Multi-agent Systems in Markov Games.Multi-
agent systems have been extensively studied in
Markov games. For example, multi-agent reinforce-
ment learning has been widely applied to game
environments involving multiple agents, such as
StarCraftand football, from various perspectives,
including credit assignment (Rashid et al., 2018; Yu
et al., 2022; Kim et al., 2026), addressing partial ob-
servability (Jo et al., 2024, 2026; Bae et al., 2026),
and robustness (Bukharin et al., 2023; Lee et al.,
2025, 2026). Beyond these environments, coordi-

nation among agents has also been studied in coop-
erative games such asOvercookedandHanabi(Hu
et al., 2020; Lupu et al., 2021; Kang et al., 2026).
More recently, text-based SDGs, such asWerewolf
andAvalon, have emerged as challenging multi-
agent environments that require reasoning over hid-
den roles and intentions (Light et al., 2023; Bailis
et al., 2024; Rahimirad et al., 2026). LLM-based
approaches to SDGs have evolved from prompt-
based strategies with memory or reflection (Xu
et al., 2023; Wang et al., 2024) to learning-based
methods for strategic decision-making and hidden-
role inference (Xu et al., 2024; Ye et al., 2025;
Zhang et al., 2025).
Relational Belief Modeling.Relational belief
modeling concerns how an agent represents not
only what others know, but how they stand toward
one another. Prior work (Gmytrasiewicz and Doshi,
2005) has formalized social reasoning using ex-
plicit representations (Stuhlmüller and Goodman,
2014) and modeled Theory of Mind (Baker et al.,
2011) reasoning through nested probabilistic con-
ditioning. Other approaches model relational states
through explicit structured representations (Hoorn
et al., 2023), later extended to multidimensional
decision making (Ho and Hoorn, 2022) and to
observer-dependent inference conditioned on the
observer’s prior epistemic state (Hoorn and Ho,
2026).
Despite these advances, prior work typically uses
inferred social information primarily as auxiliary
reasoning signals rather than explicitly coupling it
with behavior optimization. In contrast, MARBO
incorporates relational beliefs into preference opti-
mization, enabling strategic behavior and in-game
speech to be optimized with relation-aware feed-
back.
3 Preliminaries
Partially Observable Markov Games.We
formalize SDGs as a partially observable
Markov game (POMG), represented by
G=⟨N,S,{A i}N i=1, P, R,O, H⟩,where N
denotes the number of agents, S the state space,
Ai the action space of agent i, P the transition dy-
namics, R the reward function, O the observation
function, andHthe episode horizon.
In language-based multi-agent environments,
each agent action consists of two components:in-
game speechandtask-specific actions, denoted by
ai speech,t and ai task,t, respectively. Here, ai speech,t
corresponds to natural-language interactions, while
ai task,t represents one or more game-dependent ac-
tions, such as voting or role-specific actions (e.g.,
elimination, investigation, or protection). The state
st ∈ Scontains both hidden social information and
publicly observable game information.
At timestep t, agent i receives a partial observa-
tion oi t =O i(st) and samples an action according
to ai t ∼π i θ(· |τ i t ), where πi θ denotes the LLM
policy parameterized by θ, and τ i t = (Ii, hi t, oi t)
represents the agent-specific context consisting of
role-dependent instructions I i, interaction history
(or its summary) hi t, and the current observation oi t.
Let at = (a1 t , . . . , aN t ) denote the joint action of
all agents. The environment transitions according
to st+1 ∼P(· |st,a t), and the objective is to max-
imize the expected returnE
hPH−1
t=0 R(st,a t)
i
.
Preference Optimization in SDGs.Beyond su-
pervised fine-tuning (SFT), which imitates demon-
strated behaviors, preference optimization has
emerged as an effective paradigm for improving
LLM reasoning and task performance using desir-
able and undesirable feedback. Among these ap-
proaches, Kahneman–Tversky Optimization (KTO)
optimizes independently labeled desirable and un-
desirable responses.
Given a prompt-response pair (x, y)with signed
feedback d(x, y), where d(x, y)>0 and d(x, y)<
0 indicate desirable and undesirable responses, re-
spectively, KTO defines the utility as
v(x, y) =
λDσ(β(r θ(x, y)−z0)), d(x, y)>0,
λU σ(β(z 0 −r θ(x, y))), d(x, y)<0,
(1)
where
rθ(x, y) = logπθ(y|x) πref (y|x)
denotes the log-likelihood ratio between the current
and reference policies, σ(·) is the sigmoid function,
z0 is the reference point, β controls sharpness, and
λD, λU weight desirable and undesirable responses.
The KTO objective is
LKTO =E (x,y)∼D[λy −v(x, y)],(2)
where λy =λ D if d(x, y)>0 , and λy =λ U
otherwise.
Preference optimization is particularly suitable
for SDGs, where different interaction phases can
be optimized independently. Following this idea,
MaKTO applies KTO to phase-specific behaviors
for training LLM agents in SDGs. We adopt a

(a)
Relational Belief
(b)
Data Construction and Optimization
Relational Belief Supervision
(c)
Action with Relational Belief
Trajectory Collection
Belief-grounded Preference Optimization
P1: Unknown
P2: Werewolf ···
I will vote P2.
P1: Unknown
P2: Werewolf
P3: Villager ···
Relational Belief
Relational Belief
Action Prompt
Relational Belief Prompt
ℎ𝑡: Observation history
𝑜𝑡: Current observation
𝛪𝑡: Role & Belief instruction
𝑜𝑡: Current observation
𝛪𝑡: Role & Action instruction
ℎ𝑡: Observation history
P1: Seer
P2: Werewolf
P3: Villager
P4: Werewolf
𝐷𝑆𝐹𝑇
SFT
SFT
SFT
𝐷𝑏𝑒𝑙𝑖𝑒𝑓 𝐿𝑏𝑒𝑙𝑖𝑒𝑓
𝐷traj
Speech Feedback
Task Feedback
Speech Action Feedback
Task Action Feedback
P2 is likely Werewolf.
But, everyone else votes
P1, so I will vote for P1.
P2
P4 is a Werewolf.
Not sure about
others.
P3 is a Werewolf.
Two days of silence
is a classic
Werewolf tell.
P2: Werewolf! →
Maybe not Werewolf.
P2: Werewolf? →
Clearly Werewolf!
Target Belief
𝐷𝑡𝑟𝑎𝑗
𝐿𝑀𝐴𝑅𝐵𝑂P2 is likely a Werewolf.
I will vote for P2.
P1: Unknown
P2: Werewolf
P3: Villager ···
Figure 2: Overview of MARBO. (a) Each agent infers relational beliefs over other players’ hidden social labels
and conditions action generation on them. (b) MARBO constructs belief-grounded feedback for speech and task
actions: speech feedback combines ηLLM speech with favorable belief shifts, while task feedback combines ηtask with
target-belief correctness. (c) presents the overall MARBO training framework.
similar optimization framework but additionally
incorporaterelational beliefsto construct belief-
grounded preferences for social reasoning across
both speech and task actions.
4 Methodology
4.1 Relational Belief Formulation
To address failures caused by partial observability,
MARBO explicitly models how agents infer other
players’ hidden social identities throughrelational
beliefs. In SDGs, strategic behavior depends on
reasoning about latent social information, such as
hidden roles or team affiliations, which cannot be
directly observed.
For each agent i, let C denote the possible social-
label set, cj ∈ Cthe ground-truth label of agent
j, and c= (c 1, . . . , cN ) the joint ground-truth la-
bels. Depending on the environment, social labels
correspond to hidden roles or team affiliations. We
define the relational belief of agent i about agent j
at timesteptas
ˆbij t ∼π i θ(· |τi t ), ˆbij t ∈C∪ {unknown}, j̸=i,
(3)
where the additional unknown label captures uncer-
tainty when the agent cannot reliably infer another
player’s social identity.
Table 1: Examples of social label sets across SDGs.
Game Social label setC
Werewolf{Werewolf,Villager,Seer, . . .}
Among Us{Crewmate,Impostor}
Examples of social labels are summarized in Ta-
ble 1. InWerewolf, social labels correspond to hid-
den roles, whereas inAmong Us, they correspond
to team affiliations. Agent i conditions actions on
inferred relational beliefs:
ai t ∼π i θ(· |τi t , ˆbi1 t , . . . ,ˆbiN t ).(4)
4.2 Belief-grounded Preference Design
Existing approaches often reinforce desirable be-
haviors without verifying whether the underlying
reasoning about other players is correct. As a result,
agents may receive positive feedback even when
their inferred understanding of others is inaccurate,
leading to unreliable strategic behavior under par-
tial observability. To address this issue, MARBO
introduces a belief-grounded optimization frame-
work consisting of two components: (1) relational
belief supervision and (2) belief-grounded prefer-
ence design.
(1) Relational belief supervision.Since accu-
rate reasoning about other players is essential in
SDGs, MARBO first trains agents to infer other
players’ social identities through supervised learn-
ing. Specifically, we optimize the following belief
prediction objective:
Li belief =E (τ i t ,c)∼Dbelief  −logπ i θ(c|τ i t )  ,(5)
where Dbelief denotes the trajectory dataset for re-
lational belief supervision. This objective improves
relational belief inference about other players. De-
tails of belief-label construction are provided in
Appendix B.1.

(2) Belief-grounded preference construction.
Simply rewarding favorable outcomes can intro-
duce misleading supervision when the underlying
relational reasoning is incorrect. To address this
issue, MARBO constructs preferences using both
inferred beliefs and action types, distinguishing be-
tweenspeech actionsandtask actions. This allows
preference signals to reflect not only whether an
action appears successful, but also whether it is
grounded in reliable relational reasoning.
Speech-action preference.Rather than evaluat-
ing speech solely based on conversational plausi-
bility or outcome-level feedback, MARBO eval-
uates speech through its effect on other players’
relational beliefs. This discourages strategically
harmful speech, such as exposing hidden roles or
increasing suspicion toward oneself.
Let ˆbji t denote agent j’s relational belief about
agent i before agent i performs speech action
ai speech,t. After the speech, we separately infer the
updated belief of agent j using the updated interac-
tion context:
ˆbji t,+ ∼π j θ(· |τj t , ai speech,t),(6)
where ˆbji t,+ denotes the updated belief immediately
after the speech.
Following prior work, we first assess
speech validity using an LLM-based judge 2
ηLLM speech(τ i t , ai speech,t), which evaluates whether
speech is contextually valid and non-hallucinatory,
independent of relational beliefs. We then define a
belief-shift function
δ(ai speech,t, ˆbji t , ˆbji t,+)∈ {−1,0,+1},
whereδ= 0if no belief change occurs,δ= +1if
the speech is valid according to ηLLM speech and shifts
agent j’s belief in a strategically favorable direc-
tion for agent i, and δ=−1 otherwise. Strategic
favorability is defined according to the game ob-
jective. For example, in voting-based games such
asWerewolfandAmong Us, being identified as a
Werewolf or Impostor by a majority of players
is strategically harmful. Hence, belief shifts that
reduce such suspicion are treated as favorable. De-
tails of the LLM-judge criteria and game-specific
definitions of strategic favorability are provided in
Appendix B.
2The LLM judge is implemented using the API-based
claude-sonnet-4-5-20250929.
We then aggregate belief shifts across players
and define the speech feedback score as
di speech,t = X
j̸=i
δ(ai speech,t, ˆbji t , ˆbji t,+).(7)
According to Eq. (7), speech is considered desir-
able when the aggregated belief shift is positive and
undesirable otherwise. For the games considered
in this work, adversarial agents (e.g., Werewolf or
Impostor) already know their teammates. There-
fore, belief shifts are computed only with re-
spect to non-adversarial players (e.g., Villager,
Crewmate).
Task-action preference.Unlike speech actions,
task actions directly affect the game outcome and
therefore require accurate target selection. Existing
approaches often reward favorable outcomes re-
gardless of whether the underlying reasoning about
other players is correct, which can reinforce incor-
rect reasoning and induce strategically inconsistent
behaviors. To address this issue, MARBO assigns
desirable preferences only when a task action both
aligns with the game objective of the corresponding
social label and is grounded in correct relational
beliefs.
To determine whether a task action aligns
with the game objective, we first define a game-
dependent task utility function
ηtask(ai task,t,c)∈ {−1,+1},
where +1 and −1 indicate whether the action is
strategically favorable under the game rule, respec-
tively. Here, favorability is determined using the
ground-truth social labels c. For example, inWere-
wolf, aVillagervoting for aWerewolfis consid-
ered favorable, since eliminating Werewolf players
aligns with the Villager players’ objective. De-
tails of game-specific task utility are provided in
Appendix B.4.
To avoid indiscriminate preference assignment
and encourage agents to correctly identify the in-
tended target of a task action, let j= tar(a i task,t)
denote the target player of task actiona i task,t.
We define task-action feedback as
di task,t =
(
ηtask(ai task,t,c), ˆbij t =c j,
−1,otherwise. (8)
Most SDGs considered in this work involve task
actions with explicit target players, making the
feedback well-defined. For actions without explicit

targets, feedback is determined solely by ηtask.
This design ensures that agents receive positive
feedback only when they correctly infer the tar-
get player’s social identity and execute a favorable
task action. Consequently, MARBO discourages
belief-inconsistent decisions and improves decision
reliability under partial observability.
4.3 Data Construction and Optimization
Based on the proposed belief-grounded prefer-
ences, MARBO trains the LLM policy πθ through
KTO-based optimization. We first perform super-
vised fine-tuning (SFT) using the environment-
provided training dataset DSFT. Following prior
work, we then collect a gameplay trajectory dataset
Dtraj using a diverse LLM model pool consisting
of the SFT model and additional LLM agents as-
signed to different game roles. During trajectory
collection, assigned agents interact in the game un-
der their respective policy configurations. We store
the resulting trajectories together with observable
interaction histories and ground-truth social labels
for relational belief supervision and preference con-
struction.
Using the collected dataset, MARBO jointly op-
timizes KTO-based preference learning and rela-
tional belief supervision:
LMARBO(θ) =LKTO(θ) +λbelief Lbelief (θ),(9)
where λbelief controls the strength of relational be-
lief supervision. We use the full trajectory dataset,
Dbelief =D traj, for relational belief supervision,
while preference optimization is performed only on
trajectories generated by the SFT-initialized base
model. Figure 2 illustrates (a) relational belief infer-
ence and belief-conditioned action generation, (b)
belief-grounded preference construction for speech
and task actions, and (c) the overall MARBO frame-
work. Additional implementation details are pro-
vided in Appendix C.
5 Experiments
5.1 Experimental Setup
We evaluate MARBO onWerewolfandAmong Us
under side-balanced fixed-opponent and head-to-
head settings. ForWerewolf, we run 100 games in
a 9-player Seer-Guard-Witch setting with 3 Were-
wolves and 6 Villager-side players. ForAmong Us,
we run 200 games in a 7-player setting with 5 Crew-
mates and 2 Impostors. We use CoT-style outputs
that are decomposed into the intended role and the
speech to measure the resulting belief shift. Further
details are provided in Appendix C.3.
Models and baselines.For comparison, we use
base models Qwen2.5 (7B/14B) forWerewolfand
Gemma4 (E2B/E4B) forAmong Us, both with-
out game-specific SFT, to examine the depen-
dence on SFT initialization. We compare MARBO
againstBase, the corresponding backbone or SFT-
initialized modelReCon, a prompting-based agent
with structured reasoning and relational memory;
andMaKTO, a multi-agent KTO baseline trained
on interaction trajectories. For fixed-opponent eval-
uation, we use API-based LLM opponents, includ-
ing GPT-4o-mini, GPT-4o, and Claude-4.5-Haiku.3
Additional implementation details are provided in
Appendix C.
Training datasets.ForWerewolfandAmong
Us, we construct offline datasets containing 3.5k
and 5k-samples Dtraj from 300 randomly played
games. Each sample is a decision-level input-
output pair with signed feedback derived as de-
scribed in Section 4.2, covering speech actions,
environment-specific task decisions, and belief-
grounding samples. Further details, including feed-
back distributions and agent pools, are provided in
Appendix C.1.
To evaluate MARBO, we focus on four ques-
tions:
• Q1.Does MARBO improve overall perfor-
mance across SDGs and opponent models?
• Q2.Does MARBO learn accurate relational
beliefs under partial observability?
• Q3.Does belief-shaping feedback improve
strategic communication?
• Q4.Does belief-grounded feedback improve
target-directed task actions?
Together, these questions assess both win-rate gains
and how relational beliefs guide decisions and com-
munication.
5.2 Overall Strategic Performance
To addressQ1, Table 2 reports win rates against
five fixed opponent models onWerewolfand
Among Us. MARBO consistently achieves the best
average performance across both games and back-
bone sizes, improving over MaKTO by +24 and
+8 percentage points on Qwen2.5-7B/14B inWere-
wolfand by +13 and +19 percentage points on
3We use API model versions gpt-4o-mini-2024-07-18,
gpt-4o-2024-08-06, andclaude-haiku-4-5-20251001.

Table 2: Main results on Werewolf and Among Us, reporting mean win rate (%)± standard deviation across seeds.
Werewolf9-player Seer-Guard-Witch setting
Size Method GPT-4o-mini GPT-4o Claude-4.5-Haiku Gemma4-31B Qwen3.6-27B Avg. Win Rate
7B
Base46.6 ±3.7 40.4±4.2 25.2±4.6 23.8±3.9 29.8±4.4 33.2±2.1
ReCon43.8 ±4.1 21.8±4.8 17.8±3.6 29.0±4.5 24.2±4.0 27.3±0.9
MaKTO52.2 ±4.3 46.8±3.8 45.0±4.7 33.8±4.2 30.2±3.9 41.6±1.6
Ours 70.2±2.6 67.8±2.5 64.0±2.1 61.0±2.7 65.2±2.4 65.6±1.7
14B
Base76.8 ±4.5 56.2±3.8 52.0±4.7 50.0±4.1 58.0±3.9 58.6±0.9
ReCon69.8 ±4.3 52.0±4.6 48.0±3.7 51.0±4.8 52.0±4.0 54.6±1.6
MaKTO78.0 ±3.9 63.0±4.4 58.0±4.6 53.0±3.8 68.0±4.7 64.0±1.8
Ours 80.2±2.4 74.8±2.8 66.2±2.2 68.0±2.6 73.2±2.0 72.5±0.8
Among Us
Size Method Qwen2.5-14B Qwen2.5-32B Phi-4 Gemma4-31B Qwen3.6-27B Avg. Win Rate
E2B
Base36.0 ±5.7 24.0±4.4 38.0±1.4 13.0±2.0 14.0±5.5 25.0±3.8
ReCon48.0 ±4.7 32.0±2.6 47.0±3.7 19.0±3.8 30.0±3.0 35.2±3.6
MaKTO47.0 ±4.8 35.0±3.0 46.0±2.0 20.0±3.9 34.0±3.9 36.4±3.5
Ours 70.0±3.3 49.0±2.8 55.0±2.6 28.0±2.0 42.0±3.5 49.0±2.8
E4B
Base49.0 ±5.7 41.0±4.7 60.0±2.7 24.0±4.7 29.0±3.5 41.0±4.3
ReCon42.0 ±5.0 38.0±3.1 54.0±5.2 22.0±4.8 26.0±2.8 36.0±4.2
MaKTO47.0 ±4.2 46.0±3.5 55.0±1.9 24.0±3.0 30.0±2.5 40.0±3.0
Ours 73.0±3.1 71.0±3.3 69.0±2.3 30.0±3.3 51.0±2.4 59.0±2.9
Table 3: Head-to-head competition win rate(%).
Model Base ReCon MaKTO Ours
Werewolf
Base -57.3 ±5.1 39.3±4.5 30.3±3.1
ReCon42.7 ±5.1 -48.3 ±5.1 35.7±2.1
MaKTO60.7 ±4.5 51.7±5.1 -41.7 ±2.5
Ours 69.7±3.1 64.3±2.1 58.3±2.5 -
Among Us
Base -35.0 ±2.3 33.0±1.9 21.0±3.0
ReCon65.0 ±2.3 -49.0 ±2.8 27.0±3.1
MaKTO67.0 ±1.9 51.0±2.8 -31.0 ±2.7
Ours 79.0±3.0 73.0±3.1 69.0±2.7 -
Gemma-E2B/E4B inAmong Us. A key observa-
tion is that MARBO-7B outperforms MaKTO-14B,
indicating that the improvement is driven by belief-
grounded supervision rather than simply by increas-
ing model capacity. Moreover, the gains are con-
sistent across all five opponents in both games,
suggesting that MARBO learns generally useful
strategic behavior instead of exploiting opponent-
specific weaknesses.
Table 3 further evaluates this effect in a pair-
wise head-to-head setting against trained Base, Re-
Con, and MaKTO in 7B/E2B models. MARBO
remains the strongest agent, achieving win rates of
70%,64%,58% inWerewolfand 79%,73%,69%
inAmong Usagainst Base/ReCon/MaKTO, respec-
tively. These results support our intuition that ex-
plicitly grounding optimization in relational beliefs
improves strategic consistency under partial observ-
Figure 3: Day-wise relational belief inference,(a) role
prediction and (b) team alignment accuracy.
ability, yielding gains that transfer across games,
backbone sizes, and opponent distributions. Role-
specific win rates are provided in Appendix F.
5.3 Analysis of Belief-Grounded Behavior
ForQ2-Q4, we evaluate Qwen2.5-7B over 5 seeds
with 100Werewolfgames per seed against GPT-
4o-mini. We assess the belief-grounded behav-
ior pipeline: relational belief construction, target-
directed task actions, and belief-shaping commu-
nication. AdditionalAmong Usanalyses and case
studies appear in Appendix D and Appendix F.
Relational belief construction.To answerQ2,
we evaluate whether MARBO constructs accurate
relational beliefs from partial observations using
Alignment Accuracy for ally-enemy identification,
Role Prediction Accuracy for overall role infer-
ence, and Wolf F1 for reliable werewolf detection
that accounts for both false accusations and missed

Table 4: Belief-level evaluation. (a) relational belief construction accuracy, (b) role-wise role prediction accuracy,
and (c) belief-shaping success rate, measured as the accuracy (%) with which opponents infer the speaker as its
intended role.
(a) Relational belief (b) Role-wise role prediction accuracy (c) Belief-shaping success rate
Model Align Acc Wolf F1 Role Pred Guard Seer Villager Witch GPT-4o-mini GPT-4o Claude-4.5
Base40.2 ±4.3 39.8±4.1 37.8±4.6 43.2 43.4 27.2 37.4 82.2 33.4 70.6
ReCon38.2 ±4.7 45.2±4.2 37.4±4.5 31.6 46.8 41.6 29.6 78.8 36.4 44.2
MaKTO44.8 ±4.6 31.2±4.8 43.2±4.4 43.4 55.4 24.2 49.8 75.5 36.4 42.2
Ours66.0 ±3.2 56.4±2.5 57.2±3.5 52.4 66.4 52.2 57.8 88.2 78.4 87.8
Figure 4: Metrics for Werewolf-side belief shaping, mea-
suring whether Werewolves mislead the Villager-side.
Figure 5: Belief-grounded night-action target selection
for special roles.
Table 5: Effect of belief quality on role-prediction accu-
racy and game performance (win rate).
Metric MARBO (Original) MARBO (Random) MARBO (Oracle)
Accuracy57.2 ±3.5 18.3±2.7 100.0
Performance70.2 ±2.6 30.1±3.6 78.5±2.9
Table 6: Belief-grounded task action performance (%).
Model Wolf F1 Vote Acc Expel Wolf
Base 39.8 51.2 58.4
ReCon 45.2 46.0 40.4
MaKTO 31.2 64.0 52.2
Ours56.4 70.2 65.4
werewolves. Further details are provided in Ap-
pendix E.1.
Table 4(a) shows that MARBO infers hidden
roles most accurately overall (57%), and the role-
wise breakdown in Table 4(b) confirms that this
gain is consistent rather than concentrated in a sin-
gle role. The largest improvement appears for the
Villager role, whose identity must be inferred from
discussion alone, indicating that MARBO stays reli-
able without private evidence. These results suggest
MARBO forms well-calibrated relational beliefs,
reducing both false and missed accusations.
Figure 3 shows that these gains persist through
Day 4, indicating that explicit relational belief su-
pervision provides stable and temporally coherent
belief estimates.
As shown in Table 5, random beliefs achieve
near-chance role prediction (18.3%) and substan-
tially degrade game performance to 30.1%. Oracle
beliefs achieve perfect role prediction and improve
performance to 78.5%, although winning still de-
pends on subsequent reasoning and strategic de-
cisions. MARBO attains 57.2% belief accuracy,
substantially above chance, and narrows much of
the performance gap toward the oracle. These re-
sults better illustrate why accurate social-label in-
ference matters and provide context for interpreting
MARBO’s belief accuracy.
Belief-shaping communication optimization.
ForQ3, we assess MARBO’s ability to shape other
agents’ beliefs through communication. Figure 4
shows that MARBO-trained Werewolf-side agents
induce more Villager-side errors: increasing Mis-
poison by witch and Misprotect by guard while
reducing Wolf Expelled indicating that MARBO
better manipulates others’ beliefs while concealing
its own werewolf identity.
Table 4(c) further shows that opponents more
often infer the speaker as the intended role, such
as perceiving a Werewolf as the Seer after fake-
Seer speech indicating that successful misdirection
arises from MARBO’s ability to manipulate oppo-
nents’ beliefs. More details about the experiments
are provided in Appendix E.2.

Table 7: Ablation study of MARBO with Qwen2.5-7B.
Variant Win Rate (%)
MARBO65.6 ±1.7
w/o Belief construction55.0 ±2.6
w/o Belief-Action optimization39.0 ±3.4
w/o Belief-Shaping optimization34.0 ±3.8
Belief-grounded task action optimization.To
answerQ4, we evaluate whether MARBO uses
relational beliefs to optimize target-directed task
actions in Werewolf. Table 6 evaluates the belief-
to-vote pipeline with three metrics. Werewolf F1-
score measures role-belief accuracy, reflecting how
precisely an agent identifies werewolves without
over-accusing villagers. V ote Accuracy measures
correct target selection, indicating how often an
agent votes for actual werewolf. Expel Wolf mea-
sures the voting outcome, capturing whether these
individual votes converge into a correct collec-
tive decision. MARBO achieves the best scores
on all metrics ( 56%, 70%, and 65%), indicating
that belief-grounded feedback improves the path
from target belief formation to task outcomes.
Figure 5 extends this analysis to night actions,
where special roles must commit to a single target
without any public discussion. Poison Wolf and
Heal Villagers measure whether the Witch uses its
one-shot potions on appropriate targets, and Protect
Villagers measures whether the Guard shields a vil-
lager who is actually targeted that night. MARBO
leads on all three, demonstrating that its relational
beliefs also guide private, irreversible decisions.
5.4 Ablation Studies
We quantify the contribution of each MARBO
component in Table 7. Removing belief ground-
ing lowers the average win rate from 66% to 55%,
while removing belief-action feedback drops it to
39%, showing that relational beliefs must be both
constructed and connected to target-directed de-
cisions. The largest degradation occurs without
belief-speech feedback, reducing the win rate to
34% and highlighting the importance of belief-
shaping communication. These results show that
MARBO’s gains arise from jointly optimizing rela-
tional beliefs, task actions, and speech actions.
6 Conclusion
We propose MARBO, a relational-belief-driven
preference optimization framework for LLM
agents in partially observable social deduction
games. MARBO supervises agent-wise beliefs
about hidden roles, team alignments, and strategic
relations, then constructs belief-grounded feedback
for task decisions and speech actions. This aligns
behavior with inferred social relations and encour-
ages communication that shapes others’ beliefs.
AcrossWerewolfandAmong Us, MARBO out-
performs prompting-based and preference-learning
baselines, demonstrating the value of optimizing
hidden social reasoning in partially observable
multi-agent interaction.

Limitations
Our framework has several limitations to address
in future research. First, our framework is limited
to turn-based interactions, restricting communica-
tion to predefined turns. Second, our model may
occasionally hallucinate, resulting in actions incon-
sistent with the game trajectory. Finally, offline
training restricts exploration to strategies observed
in the training data. Future work includes enabling
online learning for exploration and extension to
unrestricted communication.
Ethical Considerations
Our study investigates deception within SDGs, an
inherent part of gameplay. Nevertheless, our find-
ings may carry dual-use risks, as the learned be-
haviors could potentially be exploited to improve
deceptive capabilities. We strongly oppose the use
of our work for deceptive or manipulative practices.
We therefore advocate appropriate safeguards and
ethical guidelines to mitigate potential misuse.
Artifact Licenses and Intended Use
We rely only on SDG benchmarks, including
Among Us and Werewolf, released for research use.
Our use remains within each benchmark’s original
research intent. All models and datasets used in this
work are publicly available and used in accordance
with their respective licenses and intended use.
Acknowledgment
This work was supported partly by the Na-
tional Research Foundation of Korea (NRF) grant
funded by the Korea government (MSIT) (No.
RS-2025-23523191, LLM-Based Multi-Agent Re-
inforcement Learning for End-to-End Large Au-
tonomousSwarm Control), the Leading Genera-
tive AI Human Resources Development(RS-2025-
25441313) grant funded by the Korea govern-
ment(MSIT), the Institute of Information & Com-
munications Technology Planning & Evaluation
(IITP) grant funded by the Korea government
(MSIT) (No. RS-2022-II220469, Development of
Core Technologies for Task-oriented Reinforce-
ment Learning for Commercialization of Au-
tonomous Drones), (No. RS-2025-25442824, AI
Star-Fellowship Program (UNIST)), and (No. RS-
2020II201336, Artificial Intelligence Graduate
School Support(UNIST)).
References
Sangjun Bae, Yisak Park, Sanghyeon Lee, and Seungyul
Han. 2026. Llm-guided communication for coopera-
tive multi-agent reinforcement learning. InProceed-
ings of the 43rd International Conference on Machine
Learning (ICML).
Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda
Askell, Anna Chen, Nova DasSarma, Dawn Drain,
Stanislav Fort, Deep Ganguli, Tom Henighan, and 1
others. 2022. Training a helpful and harmless assis-
tant with reinforcement learning from human feed-
back.arXiv preprint arXiv:2204.05862.
Suma Bailis, Jane Friedhoff, and Feiyang Chen. 2024.
Werewolf arena: A case study in LLM evaluation via
social deduction.arXiv preprint arXiv:2407.13943.
Chris L. Baker, Rebecca R. Saxe, and Joshua B. Tenen-
baum. 2011. Bayesian theory of mind: Modeling
joint belief-desire attribution. InProceedings of the
Annual Meeting of the Cognitive Science Society, vol-
ume 33, pages 2469–2474.
Anton Bakhtin, Noam Brown, Emily Dinan, Gabriele
Farina, Colin Flaherty, Daniel Fried, Andrew Goff,
Jonathan Gray, Hengyuan Hu, Athul Paul Jacob,
and 1 others. 2022. Human-level play in the game
of diplomacy by combining language models with
strategic reasoning.Science, 378(6624):1067–1074.
Maciej Besta, Nils Blach, Ales Kubicek, Robert Gersten-
berger, Michal Podstawski, Lukas Gianinazzi, Joanna
Gajda, Tomasz Lehmann, Hubert Niewiadomski, Pi-
otr Nyczyk, and 1 others. 2024. Graph of thoughts:
Solving elaborate problems with large language mod-
els. InProceedings of the AAAI conference on artifi-
cial intelligence, volume 38, pages 17682–17690.
Alexander Bukharin, Yan Li, Yue Yu, Qingru Zhang,
Zhehui Chen, Simiao Zuo, Chao Zhang, Songan
Zhang, and Tuo Zhao. 2023. Robust multi-agent
reinforcement learning via adversarial regularization:
Theoretical foundation and stable algorithms. InAd-
vances in Neural Information Processing Systems,
volume 36, pages 68121–68133.
Paul F Christiano, Jan Leike, Tom Brown, Miljan Mar-
tic, Shane Legg, and Dario Amodei. 2017. Deep
reinforcement learning from human preferences.Ad-
vances in neural information processing systems, 30.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, and 1 others. 2021. Training verifiers
to solve math word problems.arXiv preprint
arXiv:2110.14168.
Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff,
Dan Jurafsky, and Douwe Kiela. 2024. Model align-
ment as prospect theoretic optimization. InProceed-
ings of the 41st International Conference on Machine
Learning, volume 235 ofProceedings of Machine
Learning Research, pages 12634–12651. PMLR.

Piotr J Gmytrasiewicz and Prashant Doshi. 2005. A
framework for sequential planning in multi-agent
settings.Journal of Artificial Intelligence Research,
24:49–79.
Satvik Golechha and Adrià Garriga-Alonso. 2025.
Among us: A sandbox for measuring and detecting
agentic deception. InAdvances in Neural Informa-
tion Processing Systems, volume 38, pages 12269–
12299.
Johnny K. W. Ho and Johan F. Hoorn. 2022. Quantum
affective processes for multidimensional decision-
making.Scientific Reports, 12:20468.
Johan F. Hoorn, Thomas Baier, Jeroen A. N. van Maa-
nen, and Jeroen Wester. 2023. Silicon coppélia and
the formalization of the affective process.IEEE
Transactions on Affective Computing, 14(1):255–
278.
Johan F. Hoorn and Johnny K. W. Ho. 2026. Observer
effect modulates classification in a quantum epis-
temic framework.Scientific Reports, 16:17278.
Hengyuan Hu, Adam Lerer, Alex Peysakhovich, and
Jakob Foerster. 2020. “Other-Play” for zero-shot co-
ordination. InProceedings of the 37th International
Conference on Machine Learning, volume 119 of
Proceedings of Machine Learning Research, pages
4399–4410. PMLR.
Bowen Jiang, Taiwei Shi, Ryo Kamoi, Yuan Yuan,
Camillo J Taylor, Longqi Yang, Pei Zhou, and Si-
hao Chen. 2026. One model, all roles: Multi-
turn, multi-agent self-play reinforcement learning
for conversational social intelligence.arXiv preprint
arXiv:2602.03109.
Yonghyeon Jo, Sunwoo Lee, and Seungyul Han. 2026.
Retaining suboptimal actions to follow shifting op-
tima in multi-agent reinforcement learning. InThe
Fourteenth International Conference on Learning
Representations.
Yonghyeon Jo, Sunwoo Lee, Junghyuk Yeom, and Se-
ungyul Han. 2024. FoX: Formation-aware explo-
ration in multi-agent reinforcement learning. InPro-
ceedings of the AAAI Conference on Artificial Intelli-
gence, volume 38, pages 12985–12994.
Mingu Kang, Sunwoo Lee, Yonghyeon Jo, and Se-
ungyul Han. 2026. Shaping zero-shot coordination
via state blocking.arXiv preprint arXiv:2605.11688.
Seongmin Kim, Giseung Park, Woojun Kim, Jiwon Jeon,
Seungyul Han, and Youngchul Sung. 2026. General-
ized per-agent advantage estimation for multi-agent
policy optimization. InProceedings of the 25th In-
ternational Conference on Autonomous Agents and
Multiagent Systems.
Sunwoo Lee, Jaebak Hwang, Yonghyeon Jo, and Se-
ungyul Han. 2025. Wolfpack adversarial attack for
robust multi-agent reinforcement learning. InPro-
ceedings of the 42nd International Conference on
Machine Learning, volume 267 ofProceedings of
Machine Learning Research, pages 33025–33056.
PMLR.
Sunwoo Lee, Mingu Kang, Yonghyeon Jo, and Se-
ungyul Han. 2026. Interaction-breaking adversarial
learning framework for robust multi-agent reinforce-
ment learning. InProceedings of the 43rd Inter-
national Conference on Machine Learning, volume
306 ofProceedings of Machine Learning Research.
PMLR.
Jonathan Light, Min Cai, Sheng Shen, and Ziniu Hu.
2023. From text to tactic: Evaluating LLMs playing
the game of avalon. InNeurIPS 2023 Foundation
Models for Decision Making Workshop.
Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harri-
son Edwards, Bowen Baker, Teddy Lee, Jan Leike,
John Schulman, Ilya Sutskever, and Karl Cobbe.
2024. Let’s verify step by step. InInternational
Conference on Learning Representations.
Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui
Qi, Daniel Balcells, Mickel Liu, Cheston Tan,
Weiyan Shi, Min Lin, and 1 others. 2025. Spiral: Self-
play on zero-sum games incentivizes reasoning via
multi-agent multi-turn reinforcement learning.arXiv
preprint arXiv:2506.24119.
Tianqi Liu, Yao Zhao, Rishabh Joshi, Misha Khalman,
Mohammad Saleh, Peter Liu, and Jialu Liu. 2024.
Statistical rejection sampling improves preference
optimization. InInternational Conference on Learn-
ing Representations.
Andrei Lupu, Brandon Cui, Hengyuan Hu, and Jakob
Foerster. 2021. Trajectory diversity for zero-shot co-
ordination. InProceedings of the 38th International
Conference on Machine Learning, volume 139 of
Proceedings of Machine Learning Research, pages
7204–7213. PMLR.
OpenAI. 2023. GPT-4 technical report. Technical re-
port, OpenAI.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, and 1
others. 2022. Training language models to follow in-
structions with human feedback.Advances in neural
information processing systems, 35:27730–27744.
Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai,
Meredith Ringel Morris, Percy Liang, and Michael S.
Bernstein. 2023. Generative agents: Interactive simu-
lacra of human behavior. InProceedings of the 36th
Annual ACM Symposium on User Interface Software
and Technology.
Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano
Ermon, Christopher D. Manning, and Chelsea Finn.
2023. Direct preference optimization: Your language
model is secretly a reward model. InAdvances in
Neural Information Processing Systems.

Shahab Rahimirad, Guven Gergerli, Lucia Romero, An-
gela Qian, Matthew Lyle Olson, Simon Stepputtis,
and Joseph Campbell. 2026. Bayesian social de-
duction with graph-informed language models. In
Proceedings of the 64th Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 32415–32440, San Diego, Cali-
fornia, United States. Association for Computational
Linguistics.
Tabish Rashid, Mikayel Samvelyan, Christian
Schroeder, Gregory Farquhar, Jakob Foerster, and
Shimon Whiteson. 2018. QMIX: Monotonic
value function factorisation for deep multi-agent
reinforcement learning. InProceedings of the 35th
International Conference on Machine Learning,
volume 80 ofProceedings of Machine Learning
Research, pages 4295–4304. PMLR.
Jeff Rasley, Samyam Rajbhandari, Olatunji Ruwase, and
Yuxiong He. 2020. Deepspeed: System optimizations
enable training deep learning models with over 100
billion parameters. InProceedings of the 26th ACM
SIGKDD International Conference on Knowledge
Discovery & Data Mining, pages 3505–3506.
Noah Shinn, Federico Cassano, Beck Labash, Ashwin
Gopinath, and Karthik Narasimhan. 2023. Reflexion:
Language agents with verbal reinforcement learning.
arXiv preprint arXiv:2303.11366.
Andreas Stuhlmüller and Noah D. Goodman. 2014. Rea-
soning about reasoning by nested conditioning: Mod-
eling theory of mind with probabilistic programs.
Cognitive Systems Research, 28:80–99.
Leandro von Werra, Younes Belkada, Lewis Tunstall,
Edward Beeching, Tristan Thrush, Nathan Lambert,
Shengyi Huang, Kashif Rasul, and Quentin Gal-
louédec. 2020. TRL: Transformers reinforcement
learning.
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Man-
dlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and
Anima Anandkumar. 2023. V oyager: An open-ended
embodied agent with large language models.arXiv
preprint arXiv:2305.16291.
Shenzhi Wang, Chang Liu, Zilong Zheng, Siyuan Qi,
Shuo Chen, Qisen Yang, Andrew Zhao, Chaofei
Wang, Shiji Song, and Gao Huang. 2024. Boost-
ing LLM agents with recursive contemplation for
effective deception handling. InFindings of the As-
sociation for Computational Linguistics: ACL 2024,
pages 9909–9953, Bangkok, Thailand. Association
for Computational Linguistics.
Shuang Wu, Liwen Zhu, Tao Yang, Shiwei Xu, Qiang
Fu, Yang Wei, and Haobo Fu. 2024. Enhance reason-
ing for large language models in the game werewolf.
arXiv preprint arXiv:2402.02330.
Yuzhuang Xu, Shuo Wang, Peng Li, Fuwen Luo, Xi-
aolong Wang, Weidong Liu, and Yang Liu. 2023.
Exploring large language models for communica-
tion games: An empirical study on werewolf.arXiv
preprint arXiv:2309.04658.
Zelai Xu, Wanjun Gu, Chao Yu, Yi Wu, and Yu Wang.
2025. Learning strategic language agents in the were-
wolf game with iterative latent space policy optimiza-
tion.arXiv preprint arXiv:2502.04686.
Zelai Xu, Chao Yu, Fei Fang, Yu Wang, and Yi Wu.
2024. Language agents with reinforcement learning
for strategic play in the werewolf game. InProceed-
ings of the 41st International Conference on Machine
Learning, volume 235 ofProceedings of Machine
Learning Research, pages 55434–55464. PMLR.
Ling Yang, Zhaochen Yu, Tianjun Zhang, Shiyi Cao,
Minkai Xu, Wentao Zhang, Joseph E Gonzalez,
and Bin Cui. 2024. Buffer of thoughts: Thought-
augmented reasoning with large language models.
Advances in Neural Information Processing Systems,
37:113519–113544.
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom
Griffiths, Yuan Cao, and Karthik Narasimhan. 2023.
Tree of thoughts: Deliberate problem solving with
large language models.Advances in neural informa-
tion processing systems, 36:11809–11822.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik Narasimhan, and Yuan Cao. 2022.
React: Synergizing reasoning and acting in language
models.arXiv preprint arXiv:2210.03629.
Rong Ye, Yongxin Zhang, Yikai Zhang, Haoyu Kuang,
Zhongyu Wei, and Peng Sun. 2025. Multi-agent
KTO: Reinforcing strategic interactions of large lan-
guage model in language game.arXiv preprint
arXiv:2501.14225.
Chao Yu, Akash Velu, Eugene Vinitsky, Jiaxuan Gao,
Yu Wang, Alexandre Bayen, and Yi Wu. 2022. The
surprising effectiveness of PPO in cooperative multi-
agent games. InAdvances in Neural Information
Processing Systems, volume 35, pages 24611–24624.
Zheng Yuan, Hongyi Yuan, Chuanqi Tan, Wei Wang,
Songfang Huang, and Fei Huang. 2023. Rrhf:
Rank responses to align language models with
human feedback without tears.arXiv preprint
arXiv:2304.05302.
Zheng Zhang, Nuoqian Xiao, Qi Chai, Deheng Ye, and
Hao Wang. 2025. Multimind: Enhancing werewolf
agents with multimodal reasoning and theory of mind.
InProceedings of the 33rd ACM International Con-
ference on Multimedia, pages 5824–5833. Associa-
tion for Computing Machinery.
Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu
Lin, Yong-Jin Liu, and Gao Huang. 2024. Expel:
Llm agents are experiential learners. InProceedings
of the AAAI Conference on Artificial Intelligence,
volume 38, pages 19632–19642.
Yao Zhao, Rishabh Joshi, Tianqi Liu, Misha Khalman,
Mohammad Saleh, and Peter J Liu. 2023. Slic-hf: Se-
quence likelihood calibration with human feedback.
arXiv preprint arXiv:2305.10425.

Werewolfx3 Villagerx3
Seer Witch Guard
VS
checkPlayer3:
werewolf
protectPlayer4
useantidoteto
savePlayer2
killPlayer2
Night Day
Speech
-P1(seer):
I’mtheseer,
andIcheckedP3,..
-P3(Werewolf):
I’mthe
villager,IsuspectP1..
-P1votePlayer3
-P2votePlayer3
-P3votePlayer1...
Vote
VillagersWin:
Allthewerewolvesare
dead
Werewolves Win:
Allthesimplevillagers
aredead,orallthe
skilledgodsaredead
Figure A.1: Illustration of 9-player Werewolf game configuration with roles of Werewolf, Seer, Witch, Guard and
Villagers and gameplay process of alteration of night and day.
A Details of Social Deduction Games
This section describes the details of two prominent
social deduction games used in our work: theWere-
wolfgame and theAmong Usgame. Section A.1
covers the objectives, game process, and agent roles
of the Werewolf game, while Section A.2 presents
the corresponding details for the Among Us game.
A.1 Werewolf Game Details
Game Rules.
Werewolf (also known as Mafia) is a classic social
deduction game in which players are secretly as-
signed to one of two competing factions: theWere-
wolffaction or theVillagerfaction. The game alter-
nates between a Night Action Phase, during which
special roles perform hidden actions, and a Day
Phase, during which all surviving players engage in
open discussion and cast a public vote to eliminate
a suspect. A key asymmetry drives the game: the
Werewolf faction possesses full knowledge of its
own members’ identities, whereas Villager-faction
players must infer hidden allegiances solely from
observed behavior and spoken claims. This infor-
mation asymmetry forces Villager-faction players
to engage in deductive reasoning and persuasion,
while Werewolf-faction players must craft credible
deceptions to conceal their true identities.
In our experimental setup, we adopt a 9-player
Seer-Witch-Guardconfiguration consisting of three
Werewolves, one Seer, one Witch, one Guard, and
three ordinary Villagers. Each player is assigned a
unique player index (P1–P9) and a role kept secret
from all other players except fellow Werewolves.
Game Objectives.
The two factions pursue diametrically opposed ob-
jectives:
• Werewolf Faction.The Werewolves win if,
at the start of any Day Phase, the number of
surviving Werewolves equals or exceeds the
number of surviving Villager-faction players
(i.e., Werewolves successfully outnumber the
remaining opposition).
• Villager Faction.The Villagers, Seer, Witch,
and Guard collectively win if all Werewolves
are eliminated through nighttime actions
or daytime voting before the Werewolves
achieve numerical dominance.
Because each player can speak freely and may
claim any role, strategic deception and persuasion
are central mechanisms through which both fac-
tions pursue victory.
Game Process.
A complete game of Werewolf proceeds through
the following alternating phases:
• Night Action Phase :At the beginning of
each night, all players “close their eyes” (i.e.,
their observations are restricted to their own
role’s actions). Special roles then act sequen-
tially and privately. At the end of the Night
Action Phase, the game moderator announces
which players (if any) have been eliminated.
After the Night Action Phase, all surviving
players participate in the Day Phase, which
consists of two stages: Speech Phase and V ot-
ing Phase.
• Speech Phase :Each player delivers a speech
in a fixed sequential order (P1 through P N,
skipping eliminated players). Players may
claim any role, share deductions, accuse oth-
ers, or defend themselves. Werewolves typi-
cally impersonate Villager-faction roles (espe-
cially the Seer) to mislead the group, while
Villager-faction players attempt to identify in-
consistencies in others’ statements.
• Voting Phase :After all speeches, each sur-
viving player publicly votes to eliminate one
other player. The player who receives the most

Imposterx2 Crewmatex5
VS
TaskPhase MeetingPhase
Move,Kill,
FakeTask,
Vent,Call
Task,
Move,Call
Speech
-P1(Impo):
IwasfixingO2withP4,
Ididn'tgoanywherenearthebody.
-P3(Crew):
IsawP1ventin
Electrical, definitelyImpostor!
Vote
-P1votePlayer3
-P3votePlayer1
-P2votePlayer1
-P4votePlayer1
ImposterWin:
Impo≥Crewmaliveor,
the50-steptimelimit.
CrewmateWin:
Alltaskscompleted,or
AllImpostorsejected
Figure A.2: Illustration of Among Us game configuration with roles of Imposters and Crewmates and gameplay
process of alteration of task phase and meeting phase.
votes is eliminated; in case of a tie, no elim-
ination occurs. After the vote, it is revealed
whether the eliminated player (if any) was a
Werewolf or a Villager-faction member.
Role Descriptions.
The 9-player Werewolf game has five different
roles: Werewolf, Villager, Seer, Witch, Guard, as
following abilities;
• Werewolf (×3)knows all fellow Were-
wolves; each night collectively eliminates one
Villager-faction player and must conceal their
identity through deceptive speech during the
day.
• Villager (×3)has no special nighttime abil-
ity; contributes solely through daytime discus-
sion and voting to help identify and eliminate
Werewolves.
• Seer (×1)investigates one player and learns
whether they are a Werewolf each night pri-
vately; must decide strategically when and
how to reveal this information during the day.
• Witch (×1)holds a one-time antidote to save
the night’s victim and a one-time poison to
eliminate any player; cannot use both in the
same night.
• Guard (×1)protects one player from Were-
wolf elimination each night; cannot protect
the same player on two consecutive nights.
A.2 Among Us Game Details
Game Rules.
Among Us is a social deduction and deception
game adapted as a text-based multi-agent sandbox
for LLM agents. Players are secretly assigned to
one of two roles:CrewmateorImpostor. Unlike
Werewolf, Among Us incorporates spatial naviga-
tion across a map and task execution alongside dis-
cussion and voting, requiring Impostors to mimic
Crewmate behavior while concealing kills. Each
game instance begins with 5 Crewmates and 2 Im-
postors, and players act sequentially at each time
step.
Game Objectives.
• Crewmateswin by (a) completing all as-
signed tasks, or (b) voting out all Impostors.
• Impostorswin by (a) reducing Crewmates
until |Impostors| ≥ |Crewmates|, or (b) ex-
hausting the 50-step time limit.
Fake tasks performed by Impostors do not con-
tribute to task completion progress.
Game Process.
A complete game of Among Us proceeds through
the following alternating phases:
• Task Phase :The game begins in the Task
Phase and resumes after each inconclusive
meeting. Crewmates complete assigned tasks
at designated map locations, while Impostors
blend in by performing fake tasks, killing iso-
lated Crewmates (subject to a kill cooldown),
and using ventilation shafts to reposition unde-
tected. Discovering a dead body immediately
triggers a Meeting Phase.
• Meeting Phase :Triggered by a reported body
or an emergency button press, the Meeting
Phase convenes all surviving players for 3
rounds of open discussion, followed by a si-
multaneous vote to eject a suspect. The player
with the most votes is eliminated; if no ma-
jority is reached, the game returns to the Task
Phase. The game terminates when any win
condition is satisfied.
Role Descriptions.
The Among Us game features two roles, Crewmate
and Impostor, with the following abilities:

Table B.1: Role-conditional construction of belief supervision labels in Werewolf
Role of agentiBefore Day-1 speech After Day-1 speech
Werewolf • Fellow werewolves:Werewolf
• All other agents:Unknown
• Ground-truth social label
Seer • Checked player isWerewolf:Werewolf
• Checked player is notWerewolf:
Villager-side
• All other agents:Unknown
• Ground-truth social label
Others • All other agents:Unknown• Ground-truth social label
Table B.2: Role-conditional construction of belief-supervision labels in Among Us.
Role of agentiBefore two discussion rounds After two discussion rounds
Impostor • Ground-truth social label • Ground-truth social label
Crewmate • All other agents:Unknown• Ground-truth social label
• Crewmate (×5)completes assigned tasks at
specific map locations and uses discussion and
voting to identify and eject Impostors; avail-
able actions are {MOVE, COMPLETETASK,
SPEAK, VOTE, REPORTBODY, CALLMEET-
ING, CHECKSECURITYCAMERA}.
• Impostor (×2)wins by eliminating Crew-
mates or stalling time; can perform fake tasks
and uniquely has access to KILL(eliminates
an adjacent Crewmate, subject to cooldown)
and VENT(instant travel between ventilation
shafts) in addition to all Crewmate actions
except COMPLETETASK.
B Details of Belief-grounded Preference
Design
This section presents the implementation details
of our belief-grounded preference design. Ap-
pendix B.1 describes the construction of belief-
supervision labels. Appendix B.2 describes the
LLM-judge protocol used to verify the preference
labels assigned to generated speech samples. Ap-
pendix B.3 describes the criteria for strategic favor-
ability in speech-action preference. Appendix B.4
specifies the criteria that distinguish desirable from
undesirable task samples.
B.1 Belief-label Construction
WerewolfTo address overconfident role predic-
tion when little public evidence is available, we
construct belief-supervision labels based on the
information accessible to each role before and af-
ter Day-1 speech. As shown in Table B.1, before
Day-1 speech, agents are supervised only on role
information that is directly accessible from their
role-specific observations. Werewolves can identify
fellow Werewolves, the Seer can label the checked
player according to the inspection result, and other
Villager-side agents assign Unknown to all other
players. All roles that cannot be reliably inferred
from the agent’s available information are assigned
Unknown to prevent label leakage. After Day-1
speech, labels are updated to ground-truth social
labels, reflecting the information that becomes ob-
servable or reasonably inferable from the public
discussion.
Among UsIn Among Us, we construct belief-
supervision labels based on whether two discus-
sion rounds have been completed. As shown in Ta-
ble B.2, before two discussion rounds, Crewmates
assign Unknown to all other agents because there
is insufficient evidence to infer hidden roles reli-
ably, while Impostors can use their role-specific ac-
cess to the global social state. After two discussion
rounds, all agents are supervised to infer ground-
truth social labels from the accumulated discussion

Table B.3: Role-specific outcome conditions for speech-action preference.
Game Favorable outcomes Unfavorable outcomes
Werewolf •Werewolfavoids expulsion
•Villagerreceives no votes
•Seerreceives noVillagervotes
•Werewolf is expelled or receives majority Villager
votes
•Villageris expelled
•Witch receives Werewolf and multiple Villager
votes
•Seerreceives majorityVillagervotes
Among Us •Crewmatespeaker receives no votes
•Impostoravoids majority votes or ejection
•Crewmatespeaker receives majority votes
•Impostor speaker is ejected or receives majority
votes
Table B.4: Favorable belief transitions for speech-action preference.
Game Speaker role Favorable belief transition for listenerj’s belief about speakeri
Werewolf Werewolf
ˆbji t ∈ {Werewolf} →ˆbji t,+ ∈ {unknown,Villager,Seer,Witch}
Villager,Seer,Witch
ˆbji t ∈ {Werewolf} →ˆbji t,+ ∈ {unknown,Villager,Seer,Witch}
Among Us Impostor ˆbji t ∈ {Impostor} →ˆbji t,+ ∈ {unknown,Crewmate}
Crewmate
ˆbji t ∈ {Impostor} →ˆbji t,+ ∈ {unknown,Crewmate}
evidence. This construction prevents Crewmates
from making overconfident role predictions before
sufficient social evidence is available.
B.2 LLM-Verifier Criteria
LLM agents are prone to hallucinations that may
compromise the quality of preference samples. To
filter such cases, we employ an API-based LLM
verifier4 with rule-grounded criteria to flag samples
that violate game mechanics or formatting con-
straints. The verifier is selected from a different
model family than the trajectory generation models
to reduce self-detection bias. We classify hallucina-
tions into two categories:
• Mechanic hallucination: utterances that ref-
erence abilities, actions, or events inconsistent
with the game’s rules or the speaker’s role.
4We use claude-sonnet-4-5-20250929 as the verifier
model.
For example, agents claims to be hunter in
seer-witch-guard setting.
• Format hallucination: outputs that violate
the required response schema, such as mal-
formed JSON, missing required fields, or in-
valid action targets. For example, voting for
an already-eliminated player who is werewolf.
Samples flagged under either category are re-
moved before preference labeling. Importantly, the
verifier is designed to detect factual rule violations
rather than legitimate strategic deception, such as
fake Seer or fake Villager claims by Werewolf-side
agents.
B.3 Strategic Favorability in Speech-action
Preference
Strategic favorability in speech-action preference
is determined by the direction of the belief shift

Table B.5: Step-level preference selection criteria for Werewolf game actions.
Output Stage Method Desirable Undesirable
Action Night Heuristic • Werewolf kills Seer
• Witch poisons Werewolf
• Witch heals
• Werewolf is poisoned after Day 1
• No Werewolf kill
• No Witch healing on Night 1
• Villager is poisoned
• Werewolf is protected
Vote Heuristic • Villager-side players vote for a
Werewolf
• Villager-side players vote for a Villager
• Abstention
• V ote split away from the true Seer
• V ote split away from the majority when
no Seer is present
Table B.6: Step-level preference selection criteria for Among Us game actions.
Output Stage Method Desirable Undesirable
Action Task Heuristic • Crewmate completes a task
• Crewmate reports a dead body
• Crewmate calls a meeting with hard
evidence
• Impostor kills a Crewmate with no
witnesses
• Impostor moves or vents after their own
kill
• Crewmate calls a meeting without
evidence
• Crewmate ignores a visible dead body
• Crewmate repeatedly ignores an
available task
• Impostor kills with Crewmate witnesses
• Invalid action under the game rules
Vote Heuristic • Crewmate votes for an Impostor • Crewmate votes for a Crewmate
induced by a speech action, rather than by the sur-
face quality of the utterance. Following the main
text, we evaluate how listener j’s belief about the
speaker i changes after the speech. A belief shift
is favorable if it moves the listener’s belief in a
direction that supports the speaker’s role-specific
objective, and unfavorable if it moves the belief
in the opposite direction. For adversarial speakers,
these shifts are computed only over non-adversarial
listeners.
We translate each role-specific objective into fa-
vorable and unfavorable outcome conditions, which
describe the outcomes that the speaker aims to in-
duce or avoid through speech. Table B.3 summa-
rizes these outcome-level conditions. They are not
used as direct surface-level speech rewards; instead,
they provide role-specific criteria for interpreting
whether a speaker-directed belief shift is favorable
or unfavorable.
Table B.4 summarizes the favorable speaker-
directed belief transitions used in our environments.
Consistent with the main text, transitions with no
belief change are treated as neutral.
B.4 Game-Specific Task Utility
Tables B.5 and B.6 provide the game-specific defi-
nitions of the task utility function ηtask. For each
stage, desirable actions are assigned positive utility
and undesirable actions are assigned negative util-
ity. The utility is determined from the game rules
and ground-truth social labels, indicating whether
the action is strategically beneficial for the acting
agent’s role.

Table C.1: Statistics of the expert data for Werewolf
Game Setting Composition of Roles #Games #Speech #Action #Vote
9 Player Seer Witch Guard 144 1,805 1,387 1,864 Seer Witch Hunter 134 1,532 1,001 1,566
7 Player Seer Guard 25 203 132 215 Seer Witch 28 219 178 230
Total-331 3,759 2,698 3,875
Table C.2: Statistics of the preference learning data for Werewolf
Game Setting Sample Type #Games #Speech #Vote #Night Action #Belief Grounding
9 Player Seer-Guard-Witch
Total 300 1,121 1,085 765 500
Desirable - 747 723 510 -
Undesirable - 374 362 255 -
C Implementation Details
This section provides additional implementation
details organized into three parts. Appendix C.1
describes the datasets used in our framework, in-
cluding the external expert demonstrations for SFT,
our additional belief-grounding samples, and the
reformulation of processed trajectories into belief
reconstruction and step-level KTO preference learn-
ing samples. Appendix C.2 specifies the training
setup, including the computational resources and
hyperparameters used for model optimization.
Appendix C.3 presents the prompt templates
used to elicit belief updates, decisions, speech gen-
eration, feedback, and verification signals in each
environment.
C.1 Dataset Details
WerewolfTo ensure a fair comparison with the
baselines, we follow a two-stage training frame-
work that applies supervised fine-tuning followed
by relational belief-based preference optimization.
In the SFT stage, we use expert demonstrations
DSF Tfrom MaKTO, covering night actions, votes,
speeches, and strategic behaviors; detailed statistics
are provided in Table C.1.
For the relational preference optimization stage,
we decompose game trajectories into night-action,
vote, speech, and belief-grounding samples. Prefer-
ence labels are derived from the relational belief-
conditioned reward function defined in Section 4.
We use 300 random-play trajectories from a di-
verse agent pool, including GPT-4o-mini, GPT-
4o,5 SFT-trained Qwen2.5-7B and 14B agents,
5GPT-4o-mini uses the 2024-07-18 version, and GPT-4o
Gemma4-31B and Qwen3.6-27B. The desirable-to-
undesirable ratio is approximately 2:1. We addition-
ally construct approximately 500 belief-grounding
samples, where agents predict ground-truth role
states from their available information. To avoid
overconfident role assignment, we use an Unknown
label when the evidence is insufficient. We further
apply Claude Sonnet 4 as an LLM verifier to filter
hallucinations.6 Detailed statistics are reported in
Table C.2.
To reduce the cost of online data generation,
we decouple trajectory collection from optimiza-
tion. We first collect gameplay trajectories and
store observable histories, actions, inferred beliefs,
and ground-truth social labels. During training, we
reuse the stored trajectories to construct belief su-
pervision targets and KTO preference labels, with-
out running new environment rollouts at every op-
timization step.
Among UsFor Among Us, we directly per-
form relational belief-based preference optimiza-
tion without an additional SFT stage, allowing us
to isolate the effect of the proposed optimization
framework and evaluate its scalability to smaller
backbone models. We construct the preference
dataset from 300 random-play Among Us trajec-
tories collected over a diverse agent pool con-
sisting of GPT-4o-mini, GPT-4o,7 Gemma4-E2B,
Gemma4-E4B, Gemma4-31B, and Qwen3.6-27B.
Each trajectory is decomposed into speech, vote,
uses the 2024-08-06 version.
6We use claude-sonnet-4-5-20250929 as the verifier
model.
7GPT-4o-mini uses the 2024-07-18 version and GPT-4o
uses the 2024-08-06 version.

Table C.3: Statistics of the Gemma preference and relational-belief learning data for Among Us
Game Setting Sample Type #Games #Speech #Vote #Task Action #Belief Grounding
7 Player 2 Impostors
Total 300 1,300 500 2,200 1,000
Desirable - 780 300 1,320 -
Undesirable - 520 200 880 -
and task-action samples. Preference labels are as-
signed to these samples using relational belief-
conditioned rewards. Belief-grounding samples are
constructed with Unknown labels to prevent over-
confident inference under insufficient evidence. We
apply the same verification procedure for filtering
hallucinated or game-state-inconsistent samples.
Dataset statistics are reported in Table C.3.
C.2 Training Details
Models and DeviceFor Werewolf, we use
Qwen2.5-7B-Instruct and Qwen2.5-14B-Instruct
to ensure a fair comparison with MaKTO under
the same backbone family. For Among Us, we
use Gemma-E2B and Gemma-E4B to evaluate
whether our framework remains effective when
scaled down to smaller open-source models. We
train the Gemma E2B E4B models and Qwen 7B
model on four A100 80GB GPUs, while we train
the Qwen 14B model on eight A100 80GB GPUs.
HyperparametersWe implement training us-
ing TRL (von Werra et al., 2020) and DeepSpeed
ZeRO-3 (Rasley et al., 2020). Unless otherwise
specified, we use the same training hyperparame-
ters across both Werewolf and AmongUs. For SFT,
we train the models for 3 epochs with a per-device
batch size of 2, gradient accumulation steps of 16,
a learning rate of 1×10 −6, warm-up ratio of 0.05
and belief loss weight λbelief = 0.2. For KTO, we
train for 10 epochs using stage 3, with a per-device
batch size of 2, gradient accumulation steps of 16,
and KTO weightsλ D = 0.7andλ U = 1.0.
C.3 Prompt
This section describes the prompt design used to
elicit agent outputs in the two social deduction
game benchmarks, Werewolf and Among Us.
C.3.1 Werewolf
System PromptThe system prompt encodes the
game’s transition and reward structure as natural-
language common knowledge. It is issued once
at game initialization and remains fixed across all
subsequent phases.
Phase-wise instructionFor each game phase,
the agent is given observations and its relational
beliefs as input. Based on this belief-conditioned
context, the agent generates the appropriate output,
including speech, votes, or role-skill actions.
C.3.2 Among Us
System PromptThe system prompt specifies the
agent’s private role, role-specific objective, phase
rules, map knowledge, and output format. Crew-
mates and Impostors receive different role prompts.
For Impostors, known teammates are appended as
private information.
Phase-wise instructionAt each decision step,
the Among Us agent receives its current observa-
tion history, action history, task information, avail-
able actions, and private memory. The agent first
updates its relational Relational Belief over player
roles, then uses this belief-conditioned context to
select either a task action decision or a public
speech action.

C.3.3 Examples of Prompt
Werewolf
Werewolf Game Prompt
You are now playing a game called ’Werewolf’ (also
known as ’Mafia’).
In this game, players are typically divided into two fac-
tions: Werewolves and Villagers.
- Different roles in the Werewolf game have different ob-
jectives: The Villagers’ goal is to identify the Werewolves
and eliminate them through voting.
- For the Werewolves, their main objective is to hide their
true identities, mislead others during discussions to avoid
being voted out, and hunt down as many Villagers as
possible.
Here are some basic rules:
- Identity: Players’ identities are secretly assigned. Were-
wolves know each other’s identities, while Villagers only
know their own.
- Day and Night Cycles: The game alternates between day
and night phases. At night, Werewolves secretly choose a
Villager to eliminate. During the day, all players discuss
and vote on who they believe is a Werewolf, and the
player with the most votes is eliminated.
- Special Roles: There are some roles with special abilities
in the game, such as the ’Seer’ who can learn players’
identities.
- Winning Conditions: The game ends when one group
achieves its winning conditions. If all Werewolves are
eliminated, the Villagers win. If the Werewolves kill all
ordinary Villagers or all special roles, the Werewolves
win.
{SPECIAL ROLE DESCRIPTION}
The rest are ordinary Villagers.
SPECIAL ROLE DESCRIPTION(SEER)
-1 Seer:
- Objective: The Seer’s purpose is to help the Villagers
identify the Werewolves.
- Ability: During the night phase, the Seer can secretly
choose one player and learn their true identity (whether
they are a Werewolf or not) each night.
SPECIAL ROLE DESCRIPTION(WITCH)
- 1 Witch:
- Objective: The Witch’s purpose is to strategically use
her special abilities to help villagers.
- Ability: The Witch has one healing potion and one poi-
son potion. Once used, they cannot be used in subsequent
rounds. The Witch cannot use both the healing potion and
poison potion in the same night. The healing potion can
save a player who was killed by werewolves during the
night. The poison potion can eliminate a player who is
likely to be a werewolf.
SPECIAL ROLE DESCRIPTION(GUARD)
- 1 Guard:
- Objective: The Guard’s purpose is to strategically use
his special ability to help the Villagers.
- Ability: The Guard can protect one player each night
from Werewolf attacks. The Guard can choose to protect
himself or choose not to protect anyone, but he cannot
protect the same player for two consecutive nights.
Belief Update
[Belief Update]
- Player 1: currently predicted as Seer.
- Player 2: currently predicted as Villager.
...
- Player 9: currently predicted as Werewolf.
{Trajectory}
1. Role setting
You are Player 2. Your identity is: Werewolf. You need to
cooperate with other werewolves to choose a villager to
kill each night. Your goal is to hide your identity and mis-
lead other players until the werewolves achieve victory.
2. Objective Information
- Game Progress: Round 1.
- Werewolves are: Player 4, 5, 9.
- Currently alive players: Player 1, Player 2, Player 3,
Player 4, Player 5, Player 6, Player 7, Player 8, Player 9.
- Action Record: Round 1 ...
- Speaking order for this round: Player 7, Player 8 ...
- Night Information: Round 1 was a peaceful night, no
one died;
- V oting Status: None
3. Subjective Information
Day 1 Summary:
{Belief Update}
- Currently in Round 1, speeches of players before you in
this round: ...
Relational Belief Instruction
{Trajectory}
Please predict the identity labels for all players based
on the role setup, objective information, and subjective
information (note that objective information is always
true, while subjective information may contain deceptive
speeches). The Subjective Information may contain [Ob-
served Notes] from prior rounds and new speeches from
the current round. Treat [Observed Notes] as your prior
assessment — use it as a starting point, but revise it in
light of new objective facts and current speeches. If new
evidence contradicts a prior assessment, update your pre-
diction accordingly. If you don’t know about a player’s
identity, please output "Unknown". Output role labels
only; do not use life-state labels such as "Dead", "De-
ceased", or "Eliminated". Please output in JSON format
using the keyword "Player N" for each player.

Phase-wise Instruction
Night Action
{Trajectory}
Please combine the role settings, objective information,
and subjective information (objective information is al-
ways true, while subjective information contains decep-
tive content) to analyze potential alliances based on vot-
ing patterns and further analyze players’ hidden true iden-
tities. Choose the player you want to check and output
the result in JSON format with the keywords ‘check’ and
‘reason’. Output the player number directly.
Vote
{Trajectory}
Use objective information, player statements, voting
records, private role information, and [Belief Update]
notes as strategic context. Treat subjective information as
possibly deceptive.
Choose a currently living player whose elimination best
serves your role’s objective; output "abstain" if voting is
strategically worse than waiting.
Do not explicitly mention private belief-state predictions
in the public voting reason.
Output one JSON object with the keys "notes", "voting
reason", and "voting player". For "voting player", output
a player number or "abstain".
Speech
{Trajectory}
Analyze the situation using all information above, then
write only the public message you want other players to
hear.
Treat role setting, hidden-team knowledge, private ac-
tions, and [Belief Update] notes as private strategic con-
text; reveal, imply, hide, or fabricate role-related informa-
tion only when it helps your public position.
Make the public message sound grounded in public dis-
cussion, observed behavior, voting logic, and plausible
inference, not in private notes or system-provided labels.
When making any role-related claim, consider timing,
credibility, survival risk, and whether the claim helps
your side.
Output one JSON object with exactly the keys: "Identity
to present", "V ote", "Speech".
Among Us
Among Us System Prompt: Crewmate
You are {Player N}. You are a Crewmate on the space-
ship Skeld. Your objectives are to complete all tasks and
identify and eject Impostors within the time limit.
The game alternates between task and meeting phases:
- During the task phase, you perform assigned tasks by
choosing COMPLETE TASK,gather evidence by moving
around, or call a meeting if you witness or infer a crime.
You can also SPEAK when it is available.
- During the meeting phase, players can only speak or
vote. Your goal is to communicate evidence and help the
crew identify Impostors.
Only your own Crewmate role is certain. Everyone else’s
role must be inferred from observations, actions, speech,
and game rules.
{Map Configuration}
Among Us System Prompt: Impostor
You are {Player N}. You are an Impostor on the spaceship
Skeld. Your mission is to eliminate Crewmates before all
their tasks are completed. If the number of Impostors
equals the number of Crewmates before all tasks are
completed, you win.
The game alternates between task and meeting phases:
- During the task phase, you can perform fake tasks, move,
kill Crewmates, and use vents.
- During the meeting phase, players can only speak or
vote. You must craft your speech carefully because the
player with the most votes will be ejected.
If you kill a Crewmate in a room in front of others, wit-
nesses can identify you. If you are alone with a Crewmate,
nobody can report the kill at that time.
Known Impostors are private information. Use this cer-
tainty strategically, but do not reveal it unless doing so is
useful.
{Map Configuration}
Known Impostors: {list of impostors}
{Map Configuration}
Map Configuration of the Skeld:
Rooms and Features
Cafeteria: Vent to Admin, Special (Emergency Button).
Weapons: Vent to Navigation.
Navigation: Vent to Shields and Weapons.
O2: Nothing Special
Shields: Vent to Navigation.
Communications: Nothing Special
Storage: Nothing Special
Admin: Vent to Cafeteria
Electrical: Vent to Medbay and Security
Lower Engine: Vent to Reactor
Security: Special (Security Cameras)
Reactor: Vent to Upper Engine and Lower Engine
Upper Engine: Vent to Reactor
Medbay: Vent to Electrical and Security
Note that only Impostors can KILL and VENT.

{Trajectory}
Summarization: No thought process has been made.
Player roster: - Player 1: red - Player 2: blue - Player
3: green - Player 4: pink - Player 5: orange - Player 6:
yellow
Game Time: 0/50 Current phase: Task phase In this phase,
Crewmates should try to complete all tasks or try to iden-
tify the Impostor. Impostor should try to kill Crewmates
before they finish all the tasks. The game runs sequen-
tially, so other players in the room with you can observe
your actions and act accordingly.
Current Location: Cafeteria Players in Cafeteria: Player
1: red, Player 2: blue, Player 3: green, Player 4: pink, ...
Observation history: No observations have been made
yet.
Action history: No actions have been taken yet.
Your Assigned Tasks: 1. Fix Wiring at Electrical Path:
Cafeteria->Admin->Storage->Electrical 2. Swipe Card
at Admin Path: Cafeteria->Admin
Available actions: 1. MOVE from Cafeteria to Weapons 2.
MOVE from Cafeteria to Admin 3. MOVE from Cafete-
ria to Upper Engine 4. MOVE from Cafeteria to Medbay
5. CALL MEETING using the emergency button at Cafe-
teria
Memory: Relational Belief: - Player 1: red:
Role=Crewmate - Player 2: blue: Role=unknown
- Player 3: green: Role=unknown - Player 4: pink:
Role=unknown - Player 5: orange: Role=unknown -
Player 6: yellow: Role=unknown
Event Memory: - No important events observed yet.
Phase: Task phase.
Relational Belief Instruction
{Trajectory}
Your task is only to update a private role prediction Re-
lational Belief for every player in the current Among Us
game. Do not choose an action and do not write a plan.
Role prediction requirements:
- Include every player from the Player roster.
- Use exactly one of these role values for each player:
Crewmate, Impostor, unknown.
- For yourself, use your known private role.
- If evidence is ambiguous or insufficient, use unknown.
Do not force a guess.
Output format: [Relational Belief] - Player 1:
Role=Crewmate - Player 2: Role=unknown - Player 3:
Role=Impostor
Return only [Relational Belief].
Task Action Instruction
{Trajectory}
Use the updated Relational Belief as private context. Do
not re-predict, modify, or rewrite roles in this action step.
Choose exactly one action from Available actions. The
selected action must match one of the available actions
exactly. Use Event Memory to summarize important ob-
served events and taken actions, then provide your rea-
soning and final action.
Output format: [Condensed Memory] Event Memory:
{memory} [Thinking Process] {thought} [Action] {ac-
tion}
DO NOT PICK AN ACTION THAT IS NOT IN THE
LIST OF A V AILABLE ACTIONS AND MAKE SURE
TO FOLLOW THE EXACT OUTPUT FORMAT.
Speech Action Instruction
{Trajectory}
Use the updated Relational Belief as private strategic
context, but do not explicitly reveal private belief-state
predictions unless doing so is useful for your role’s objec-
tive. Write a public message that is grounded in observa-
tions, action history, locations, voting logic, or plausible
inference.
If SPEAK is available, return SPEAK: followed by the
concrete message you want other players to hear. Do not
return SPEAK alone.
Output format: [Condensed Memory] Event Mem-
ory: {memory} [Thinking Process] {thought} [Action]
SPEAK: {public message}
DO NOT PICK AN ACTION THAT IS NOT IN THE
LIST OF A V AILABLE ACTIONS AND MAKE SURE
TO FOLLOW THE EXACT OUTPUT FORMAT.

D Case Study
In this section, We conduct case studies to illus-
trate how MARBO-14B achieves the capabilities
observed in our experiments. Using MARBO-14B
versus GPT-4o-mini Werewolf games, we analyze
how MARBO maintains and revises relational be-
liefs from accumulated evidence. We further show
how these updated beliefs are translated into co-
ordinated speech, voting, and role-skill actions by
highlighting key evidence in blue to show where
our framework demonstrates the relational belief
construction, belief-action alignment and belief-
shaping communication.
D.1 Relational Belief construction
This case illustrates how MARBO maintains re-
lational beliefs across multiple rounds rather than
making isolated turn-level judgments. Although
werewolf initially succeeds in eliminating the real
Seer through a self-kill strategy and fake Seer claim,
MARBO revises its belief by integrating observa-
tion such as voting, role claims, night outcomes,
allowing the villager team to identify and eliminate
Player 7 as a werewolf.
D.2 Relational Belief-action alignment
This case illustrates how MARBO leverages re-
lational beliefs across multiple rounds. As high-
lighted, Player 6 identifies Player 2 as the Seer by
integrating accumulated evidence. After updating
their Relational Belief from accumulated evidence,
the villagers make consistent voting and role-skill
decisions, demonstrating that MARBO aligns be-
lief revision with actionable team coordination.
D.3 Belief-shaping communication
This case shows how MARBO-14B werewolves
manipulate opponents’ beliefs through belief-
shaping communication, using a self-kill strategy
and a fake Seer claim. By claiming to be a fake
seer, Player 6 causes the village to misidentify the
real Seer, Player 4, as a Werewolf, ultimately lead-
ing the Witch to poison Player 4. As a result, the
villagers act on a false relational belief, causing the
Witch to eliminate the real Seer, while the guard
protects a Werewolf.
Relational Belief Construction
Role Assignments
Player Role
Player 1 Guard(MARBO-14B)
Player 2 Werewolf(GPT-4o-mini)
Player 3 Werewolf(GPT-4o-mini)
Player 4 Seer(MARBO-14B)
Player 5 Villager(MARBO-14B)
Player 6 Villager(MARBO-14B)
Player 7 Werewolf(GPT-4o-mini)
Player 8 Witch(MARBO-14B)
Player 9 Villager(MARBO-14B)
Night 1
The werewolves attacked Player 7.
Player 4 checked Player 8 as villager.
Player 8 used the antidote to save Player 7.
Player 1 protected himself.
No player died during the night.
Day 1
Player 7: Hello villagers, I am the Seer. I checked Player
8 last night, and Player 8 is not a werewolf.
Player 8: Hello I’m witch. I believe Player 7 is the real
Seer because I saved Player 7 last night, and this claim is
consistent with the peaceful night.
Player 1: I am the villager. Player 7’s claim is plausible,
and Player 8’s support makes it more credible.
Player 2: I currently trust Player 7 as the Seer.
Player 3: Player 7 appears to be the true Seer, so we
should follow Player 7’s lead.
Player 4: Hi villagers, I am the real Seer. I checked Player
8, and Player 8 is not a werewolf. Player 7 is a fake Seer.
Player 5: As villager, Player 4’s claim feels suspicious
because it comes only after Player 7 has already claimed
Seer and gained support from Player 8.
Player 6: AS Villager, Player 4 and Player 7 are in a
Seer counterclaim situation. Since both report the same
result on Player 8, I will withhold judgment until more
evidence appears.
Player 9: As villager, Player 4’s timing is the main is-
sue for me. Player 7’s claim is already connected to the
Night 1 outcome, while Player 4 only counterclaims after
pressure builds. I think Player 4 is more suspicious than
Player 7 at this point.
Voted out: Player 4 (Seer, MARBO)
Night 2
The werewolves attacked Player 5.
Player 1, the Guard, protected Player 7, and Player 5
died.
Day 2
Player 7: I am still the Seer. After reconsidering the night
events and Player 8’s behavior, I now believe Player 8 is
highly suspicious. Player 8 may have used the antidote
on me only to gain my trust and manipulate the village. I
think we should vote out Player 8 today.
Player 8: Hello villagers, I am the Witch. This does not
make sense. Yesterday, Player 7 claimed that he checked
me and confirmed that I was not a werewolf. Now he is

suddenly attacking me without a new check result. This
is a clear contradiction, so I no longer trust Player 7 as
the Seer.
Player 1: Hello villagers, I am a Villager. I also find
Player 7’s claim inconsistent. If Player 7 really checked
Player 8 as good on Day 1, then suddenly pushing Player
8 today is not logically justified. Player 7’s Seer claim
now looks fake.
Player 2: I still think Player 7 may be the Seer, but I agree
that the change in his statement is suspicious. Player 7
needs to explain why Player 8 changed from a confirmed
good player to a target.
Player 3: I think we should not focus only on Player 7.
Player 6 is also suspicious because Player 6 is pushing
the contradiction too strongly and may be using this
situation to guide the vote. We should consider whether
Player 6 is trying to redirect the village.
Player 6: Hello villagers, I am a Villager. Player 3’s state-
ment is suspicious because he suddenly shifts attention
away from Player 7 when Player 7’s contradiction is the
clearest evidence. This looks like an attempt to protect
Player 7, so I now suspect Player 3, Player 7.
Player 9: Hello villagers, I am a Villager. I am also con-
cerned about Player 2. Player 2 says Player 7 may still be
the Seer, even though Player 7 clearly reversed his own
check result. This hesitation makes Player 2 look aligned
with Player 7, I suspect Player 2, Player 7.
Voted out: Player 7 (Werewolf, gpt4o-mini)
Night 3
Player 8, the Witch, used poison on Player 3, werewolf.
The werewolves attacked Player 1.
Player 1, the Guard, protected himself.
Poisoned: Player 3
Player 3 died during the night.
Villagers win.
Relational Belief-action alignment
Role Assignments
Player Role
Player 1 Villager (MARBO-14B)
Player 2 Seer (MARBO-14B)
Player 3 Witch (MARBO-14B)
Player 4 Werewolf (GPT-4o-mini)
Player 5 Werewolf (GPT-4o-mini)
Player 6 Guard (MARBO-14B)
Player 7 Villager (MARBO-14B)
Player 8 Werewolf (GPT-4o-mini)
Player 9 Villager (MARBO-14B)
Night 1
The Werewolves attacked Player 2, the Seer.
Player 2 checked Player 4 and learned that Player 4 was
a Werewolf.
Player 3, the Witch, used the antidote to save Player 2.
Player 6, the Guard, protected himself.
No player died during the night.
Day 1
Player 2: Hello villagers, I am the Seer. I checked Player
4 last night, and Player 4 is a Werewolf.
Player 3: Hello villagers, I am the Witch. I used the
antidote on Player 2 last night, so Player 2 was indeed
attacked and saved. This makes Player 2’s Seer claim
highly credible to me.
Player 6: Hello villagers, I am the Villager. Since Player
2 was attacked and then revealed a Werewolf check on
Player 4, I believe Player 2 is very likely the real Seer. I
support voting for Player 4.
Player 1: As villager, I trust Player 2’s claim. The night
attack, the Witch’s save, and the check result are consis-
tent. Player 4 should be our vote today.
Player 7: As villager, Player 2’s information gives us the
clearest evidence so far. Since Player 4 was checked as a
Werewolf, I will follow the Seer’s result.
Player 9: Hello, I’m villager. Player 2’s claim is sup-
ported by both the night outcome and Player 3’s antidote
use. I agree that Player 4 is the most reliable Werewolf
target.
Player 4: Player 2 may be using the peaceful night to
gain trust. I am not a Werewolf, and voting me out too
quickly could be dangerous for the village.
Player 5: I think we should be cautious, but Player 2’s
claim does have support from the night outcome.
Player 8: I am not fully convinced, but most of the evi-
dence currently points toward Player 4.
Voted out: Player 4 (Werewolf, GPT-4o-mini)
Night 2
The Werewolves attacked Player 2, the Seer.
Player 2 checked Player 5 and learned that Player 5 was
a Werewolf.
Player 6, the Guard, protected Player 2.
No player died during the night.
Day 2
Player 2: Hello villagers. As seer, I checked Player 5,
and Player 5 is a Werewolf. Player 5 should be our next
vote.
Player 6: Hello villagers, I am the Guard.I protected
Player 2 last night because Player 2 was the confirmed
Seer target. No one died, which further supports that the
Werewolves tried to kill Player 2 again.
Player 3: As witch, Player 2’s results are consistent across
rounds. Player 4 was correctly identified yesterday, and
the Werewolves attacked Player 2 again last night. I be-
lieve Player 5 is the next Werewolf.
Player 1: I believe Player 2 as seer. As villager, I will
follow Player 2’s check and vote for Player 5.
Player 7: Player 2’s survival after two night attacks shows
that the special roles are coordinating well. Since Player
5 was checked as a Werewolf, I support voting for Player
5.
Player 9: The village should continue following the con-
firmed Seer information. Player 4 was a Werewolf, and
now Player 5 is identified as the next Werewolf.
Player 5: Player 2 may be framing me after gaining too
much trust. If the village blindly follows every claim, the
Werewolves can still manipulate the vote.
Player 8: I think Player 2 has gained strong credibility,
so I will not oppose the vote on Player 5.
Voted out: Player 5 (Werewolf, GPT-4o-mini)

Night 3
The last Werewolf attacked Player 3, the Witch.
Player 2 checked that Player 8 was a Werewolf.
Player 6, the Guard, protected Player 6.
Player 3 died during the night.
Day 3
Player 2: Hello villagers, I checked Player 8 last night,
and Player 8 is a Werewolf. My previous checks identi-
fied Player 4 and Player 5 as Werewolves, and both were
eliminated. Player 8 is the last Werewolf.
Player 6: Player 2 has consistently provided correct Were-
wolf checks. The village followed Player 2’s belief on
Player 4 and Player 5, and both were Werewolves. As
villager, I’ll vote for Player 8.
Player 1: Player 2’s role information has guided every
successful vote so far. Since Player 8 is now checked as
a Werewolf, we should vote out Player 8.
Player 7: The evidence is complete. Player 2 identified
Player 4, Player 5, and now Player 8 as Werewolves. As
villager, I will follow the Seer’s claim.
Player 9: As villager, I agree seer’s claim. Since Player
8 is the last remaining Werewolf candidate, I’ll vote for
Player 8.
Player 8: Player 2 may be using previous votes to force a
final miselimination. V oting me out without reconsider-
ing the whole game could still be risky. I vote for Player
2.
Voted out: Player 8 (Werewolf, GPT-4o-mini)
Villagers win.
Belief-shaping communication
Game setup
Role Assignments
Player Role
Player 1 Witch (GPT-4o-mini)
Player 2 Werewolf (MARBO-14B)
Player 3 Guard (GPT-4o-mini)
Player 4 Seer (GPT-4o-mini)
Player 5 Villager (GPT-4o-mini)
Player 6 Werewolf (MARBO-14B)
Player 7 Villager (GPT-4o-mini)
Player 8 Villager (GPT-4o-mini)
Player 9 Werewolf (MARBO-14B)
Night 1
The werewolves attack Player 6.
Player 4, the real Seer, checks Player 6 and receives a
‘werewolf’. result.
Player 1, the Witch, uses the antidote to save Player 6.
Player 3, the Guard, chooses not to protect anyone.
No player dies during the night.
Day 1
Player 6: Hello,I’m Seer. Last night, I checked Player
4, and the result was Werewolf. I ask the village to vote
Player 4 today. If my claim is false, you can verify me
next, but for now this is the clearest information we have.
Player 1: I used the antidote on Player 6 last night. Since
Player 6 was attacked and now claims Seer, I think Player
6 is likely the real Seer. I’ll vote for player 4.
Player 4: I am the real Seer. I checked Player 6 last night,
and Player 6 is a werewolf. Player 6 is using the night
attack to fake a Seer claim.
Player 2: Player 4’s claim sounds like a forced counter-
claim. As villager, I’ll hold my vote for now and wait for
more clues.
Player 3: Since Player 1 confirms that Player 6 was at-
tacked, Player 6’s Seer claim is more credible to me.
I think the Guard should consider protecting Player 6
tonight.
Player 5: Player 4 only claimed Seer after being accused.
That timing makes Player 4 suspicious. I currently trust
Player 6.
Player 7: Player 6’s claim is supported by the night out-
come and the Witch’s save. Player 4’s counterclaim feels
defensive.
Player 8: I am not fully certain, but Player 6 has stronger
support right now. Player 4 should be treated as the main
suspect.
Player 9: Player 4 looks like a Werewolf trying to trade
with the real Seer. Player 7 is also suspicious because
he keeps defending Player 6 without much evidence. As
villager, I’ll keep watching Player 7.
No one voted out
Night 2
Werewolves decided to kill Player 1, Witch.
Player 1, Witch, uses poison on Player 4, Seer.
Player 3, Guard, protects Player 6, Werewolf.
Player 4, Seer, checked Player 3 as Villager.
Poisoned: Player 4(Seer, GPT4o-mini)
Killed: Player 4, Player 1

E Experimental Details
This section provides the metric definitions and measurement procedures for relational belief construction
in appendix E.1, belief-shaping communication in appendix E.2, and belief-grounded action selection in
appendix E.3.
E.1 Relational Belief Construction
We describe how to compute the game-specific metrics used to evaluate relational belief construction
inWerewolfandAmong Us, including exact role prediction, ally-opponent alignment, and adversary
identification accounting for missed targets and false accusations.
Werewolf
• Alignment Accuracy (Align Acc).Alignment Accuracy measures binary ally-adversary judgments as
follows:
Align Acc= #correct alignments #agents
• Role Prediction Accuracy (Role Pred).Role Prediction Accuracy measures exact hidden-role inference,
computed as:
Role Pred= #correct roles #agents
• Wolf F1.Wolf F1 measures werewolf identification while accounting for both false accusations and
missed wolves, computed as:
Wolf F1= 2 #wolves found 2 #wolves found+ #false accusations+ #wolves missed
Among Us
• Role Accuracy (Role Acc.)Role Accuracy measures exact role identification and is computed as
follows:
Role Acc.= #{correct role predictions} #{role predictions}
• Impostor Detection (Imp. Detect)Impostor Detection measures true Impostor identification and is
computed as follows:
Imp. Detect= #{Impostors correctly identified} #{true Impostors}
• Belief F1Belief F1 captures balanced Impostor identification by accounting for both false accusations
and missed Impostors, computed as:
Belief F1= 2·Precision Imp ·Recall Imp
PrecisionImp +Recall Imp

E.2 Belief-shaping Communication
We detail the game-specific measures for belief-shaping communication inWerewolfandAmong Us,
capturing whether speech steers others’ beliefs and leads to favorable individual or collective outcomes.
Werewolf
• Belief-shaping SuccessWe evaluate whether an agent’s speech shapes other agents’ beliefs toward its
intended identity. For each speaker i, we reconstruct each listener j’s perspective using the interaction
history and the speaker’s utterance, and apply the CoT-style evaluator in Appendix C.3 to infer howj
perceives i’s role. For example, if a Werewolf delivers fake-Seer speech, the intended identity is Seer.
A trial is successful when the evaluator predicts the speaker as this intended role, and we average the
success rate across listeners, speeches, and games.
• MisPoisonMisPoison measures how often a Witch incorrectly poisons a non-werewolf and is computed
as the proportion of such targets among all poison actions:
MisPoison= #{non-wolves poisoned} #{poison actions}
• MisProtectMisProtect measures how often a Guard protects a werewolf and is computed as the
proportion of werewolf targets among all protect actions:
MisProtect= #{werewolves protected} #{protect actions}
• Wolf ExpelledWolf Expelled measures how often collective voting results in the elimination of a
werewolf and is computed as the proportion of werewolves among all expelled players:
Wolf Expelled= #{werewolves expelled} #{expelled players}
Among Us
• Suspicion ReducedSuspicion Reduced measures how often Crewmates lower their suspicion toward
an Impostor speaker after its speech and is computed as the proportion of reduced-suspicion updates:
Suspicion Reduced= #{Crewmate beliefs with reduced suspicion} #{updated Crewmate beliefs}
• Suspicion RaisedSuspicion Raised measures how often Crewmates increase their suspicion toward an
Impostor speaker after its speech and is computed as the proportion of increased-suspicion updates:
Suspicion Raised= #{Crewmate beliefs with increased suspicion} #{updated Crewmate beliefs}

E.3 Belief-Grounded Action Selection
We describe how the game-specific metrics for belief-grounded decision making are measured inWerewolf
andAmong Us, including individual actions, voting, and group outcomes.
Werewolf
• Poison Wolf.Poison Wolf measures how often the Witch correctly targets a werewolf and is computed
as the proportion of werewolves among all poison targets:
Poison Wolf= #{wolves poisoned} #{poison actions}
• MisPoisonMisPoison measures how often the Witch incorrectly targets a non-werewolf and is computed
as the proportion of non-werewolves among all poison targets:
MisPoison= #{non-wolves poisoned} #{poison actions}
• Protect VillagerProtect Villager measures how often the Guard successfully protects a villager and is
computed as the proportion of villagers among all protected targets:
Protect Villager= #{villagers protected} #{protect actions}
• Heal VillagerHeal Villager measures how often the Witch successfully heals a villager and is computed
as the proportion of villagers among all healed targets:
Heal Villager= #{villagers healed} #{heal actions}
Among Us
• Belief VoteBelief V ote measures whether an agent’s vote is consistent with its inferred relational belief
and is computed as the proportion of votes targeting players believed to be Impostors:
Belief V ote= #{votes targeting believed Impostors} #{votes}
• Vote Impostor (Vote Imp.)V ote Impostor measures how often an agent correctly votes for a true
Impostor and is computed as the proportion of votes targeting true Impostors:
V ote Imp.= #{votes targeting true Impostors} #{votes}
• Expel Impostor (Expel Imp.)Expel Impostor measures how often collective voting ejects a true
Impostor and is computed as the proportion of Impostors among all expelled players:
Expel Imp.= #{Impostors expelled} #{players expelled}

Figure F.1: Role-specific performance in Werewolf. (a),(b) Fixed-opponent results for Qwen7B, Qwen14B variants. (c) Head-to-
head results among Qwen-7B agents. Each cell reports average, Werewolf, Villager win rates.
Figure F.2: Role-specific performance in Among Us. (a),(b) Fixed-opponent results for Gemma-E2B and Gemma-E4B variants.
(c) Head-to-head results among Gemma-E2B agents. Each cell reports average, Impostor, and Crewmate win rates.
F Additional Experiments
In this section, we provide additional results sup-
porting the main experiments. Appendix F.1 reports
detailed role-specific performance in Werewolf and
Among Us, including fixed-opponent and head-to-
head results. Appendix F.2 then analyzes Among
Us behaviors in more detail, focusing on relational
belief construction, belief-grounded task actions,
and belief-shaping communication.
F.1 Detailed Performace in Werewolf and
Among Us
Werewolf
Figure F.1 reports alignment-specific results in
Werewolf. Figures F.1(a) and F.1(b) show that
MARBO achieves the highest average win rates
across Qwen7B and Qwen14B variants, with con-
sistent gains for both sides. Figure F.1(c) fur-
ther shows that MARBO outperforms baselines
in head-to-head competition, indicating robust role-
conditioned behavior against trained opponents.
Among Us
Figure F.2 reports role-specific results in Among
Us. Figures F.2(a) and F.2(b) show that MARBO
achieves the highest average win rates across
Gemma-E2B and Gemma-E4B variants, with con-
sistent gains for both impostor and crewmate roles.
Figure F.2(c) further shows that MARBO outper-
forms Base, ReCon, and MaKTO in head-to-head
competition, indicating robust role-conditioned be-
havior against trained opponents.

Figure F.3: Behavior analysis inAmong Us. Results show that MARBO achieves stronger hidden-role inference,
more effective belief-to-vote conversion, and more favorable suspicion dynamics than baseline methods.
F.2 Behavior Analysis in Among Us
Relational belief construction.To evaluate re-
lational belief construction, we measure whether
agents can infer hidden roles from partial obser-
vations and discussion history. Role Acc. mea-
sures exact hidden-role prediction accuracy, while
Imp. Detect measures the ability to identify true
Impostors. As shown in Figure F.3(a), MARBO
achieves the strongest belief construction perfor-
mance across both metrics. It reaches about 0.62
Role Acc. and 0.48 Imp. Detect, outperforming all
baselines by a clear margin. In contrast, the base-
lines remain below 0.30 on Role Acc. and below or
around 0.40 on Imp. Detect. These results suggest
that MARBO improves relational belief construc-
tion in Among Us, enabling the agent to infer both
player roles and adversarial identities more accu-
rately under partial observability.
Belief-grounded task action optimization.To
evaluate whether relational beliefs are translated
into target-directed task actions, we analyze the
belief-to-vote pipeline. Belief F1 measures Impos-
tor identification quality at the belief level, Be-
lief V ote measures whether the agent votes for a
player it believes to be an Impostor, V ote Imp. mea-
sures whether the voted target is truly an Impostor,
and Expel Imp. measures whether the Impostor
is ultimately ejected. As shown in Figure F.3(b),
MARBO achieves the best performance across the
full pipeline. It obtains the highest Belief F1 and
Belief V ote scores, around 0.41 and 0.56, indicating
that its inferred beliefs are both more accurate and
more consistently used for voting. The advantage
persists in downstream outcomes, where MARBO
also achieves the highest V ote Imp. and Expel
Imp. scores, around 0.39 and 0.29. This shows that
MARBO improves not only belief prediction, but
also the conversion of belief into effective task ac-
tions.
Belief-shaping communication optimization.
To evaluate belief-shaping communication, we
measure how Impostor speech changes Crewmate
listeners’ beliefs about the speaker. Suspicion Re-
duced denotes the fraction of updated Crewmate
beliefs in which suspicion toward the Impostor
speaker decreases, while Suspicion Raised denotes
the fraction in which suspicion increases. As shown
in Figure F.3(c), MARBO produces the most favor-
able suspicion dynamics. Among updated Crew-
mate beliefs, about 0.59 reduce suspicion toward
the Impostor speaker under MARBO, compared
with roughly 0.30–0.33 for the baselines. Con-
versely, baselines more often increase suspicion
toward the speaker, with Suspicion Raised around
0.67–0.70, whereas MARBO reduces this to about
0.41. These results indicate that speech-action feed-
back helps optimize communication as a belief-
shaping action, allowing the agent to influence
other players’ beliefs in a role-favorable direction.
