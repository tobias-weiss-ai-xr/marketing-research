---
title: 'PersuaRL: Reinforcement Learning-Driven Multi-Expert Selection for Persuasive Dialogue Generation
  in Insurance'
url: https://arxiv.org/abs/2609.01188
category: ai-marketing
subcategory: framework
date: 2026-09
venue: arXiv (Cornell University)
authors:
- Rohan Kirti
- Akash Ghosh
- Aryan Vats
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.01188
pages: 34
chars: 125040
fetched_at: '2026-11-08T13:35:34+00:00'
kb_version: 1
---

# PersuaRL: Reinforcement Learning-Driven Multi-Expert Selection for Persuasive Dialogue Generation in Insurance

PersuaRL: Reinforcement Learning-Driven Multi-Expert Selection for
Persuasive Dialogue Generation in Insurance
Rohan Kirti1*, Akash Ghosh1, Aryan Vats1, Niladri Ghosh2, Shipra Shriparn1,
Roshni Ramnani3,Anutosh Maitra 3,Sriparna Saha 1
1Indian Institute of Technology Patna, India
2Ramakrishna Mission Vivekananda Educational and Research Institute, India
3Accenture Labs, Bangalore, India
Abstract
Large Language Models (LLMs) are revolu-
tionizing digital communication by powering
conversational agents deployed across domains
such as customer service, digital sales, and in-
surance. These agents, built on LLMs, can
understand user input, retrieve relevant infor-
mation, and generate coherent responses. How-
ever, while they excel at factual communication,
they often lack the ability to engage in truly per-
suasive, context-sensitive dialogue, especially
in domains like insurance, where trust and clar-
ity are critical. Building on this need within
the insurance domain, our work focuses on im-
proving the persuasiveness of digital agents,
aka LLMs. To support this, we introduceIn-
sureDial, a PersuasiveInsurance Dialogue
dataset, designed to capture the nuances of per-
suasive communication specific to motor insur-
ance interactions. We introducePersuaRL, a
reinforcement learning based framework that
equips LLM-driven dialogue agents with the
ability to adaptively explore, select, and coordi-
nate strategies across multiple expert modules,
guided by the evolving dialogue context, to
achieve more effective persuasion. We con-
duct extensive automatic, human and quali-
tative evaluations on two benchmark persua-
sion dialogue datasets, including ourInsure-
Dial. Our evaluations consistently demonstrate
thatPersuaRLoutperforms baseline, generat-
ing contextually appropriate and highly per-
suasive responses. The code and dataset are
available at PersuaRL.
1 Introduction
Digital conversations have progressed beyond sim-
ple information exchange, with virtual dialogue
agents now playing sophisticated roles in sectors
like customer service, sales, and financial advising
(Takayanagi et al., 2025; Sree et al., 2023; Stock
∗Corresponding author:rohan_2421cs09@iitp.ac.in
et al., 2022). A key emerging function in these
settings is persuasion, which empowers agents not
only to inform but also to strategically influence
user behavior (Wang et al., 2019). This need is
especially critical in domains such as insurance,
where agents must actively motivate users toward
beneficial outcomes, like selecting appropriate pol-
icy options. Designing such persuasive agents is
highly challenging: unlike standard QA systems,
they must infer user intent, adapt to emotional tone,
highlight policy benefits, and guide decisions con-
structively (Samad et al., 2022). These require-
ments demand fine-grained reasoning and contex-
tual awareness capabilities that often exceed the
limits of monolithic LLMs, which typically lack
the domain sensitivity and nuance needed for effec-
tive persuasive engagement.
With the advancement of conversational LLMs,
recent work has focused on enhancing persuasion
and strategic dialogue. (Ramani et al., 2024) pro-
posed a multi-agent persuasion framework where a
primary agent engages users while auxiliary agents
manage strategy planning and fact-checking lead-
ing to improved persuasive efficacy in simulated
insurance and financial settings. Similarly, (Ma
et al., 2025) introduced a multi LLM communica-
tion setup to generate persuasive dialogue data with
minimal human effort, achieving fluent and strate-
gically diverse outputs. However, most prior work
emphasizes synthetic data or simulations, lacking
deployment in real-world domains like motor in-
surance, where effective persuasion requires under-
standing user needs, handling queries, and guid-
ing decisions over multi-turn interactions. Tool-
augmented LLMs and VLMs now address this
gap by enabling dynamic planning and using API
within coherent dialogues, surpassing static, single-
turn systems (Shim et al., 2025; Jung et al., 2025;
Ghosh et al., 2026a; Halder et al., 2026).
Research gap:While Tool-augmented LLMs
have made strides in improving reasoning capabil-
arXiv:2609.01188v1  [cs.CL]  1 Sep 2026

ities through external function use (Wang et al.,
2024); (Li et al., 2025), they largely depend on pre-
defined or rigid tool invocation mechanisms that
limit flexibility and adaptation to task-specific ob-
jectives. Recent works like (Schick et al., 2023)
and (Lu et al., 2025) introduce flexible tool use, but
they focus on factual tasks, not strategic persuasion.
Meanwhile, studies on persuasive dialogue (Breum
et al., 2024); (Jin et al., 2024); (Karinshak et al.,
2023) have shown that LLMs can influence opin-
ions using social-pragmatic strategies. However,
these works still face limitations in generalizing
tool-use policies to novel tools aligned with persua-
sive intent, and often struggle to maintain context-
sensitive strategy selection in extended multi-turn
dialogues.
Motivation:We reconceptualize expert co-
ordination for persuasive dialogue as a context-
conditioned decision problem, where selecting the
right combination of experts becomes a learnable
action rather than a heuristic choice. Unlike prior
approaches based on static prompting, our frame-
work formulates expert selection as an explicit ac-
tion space and trains the selector and generator by
alternating optimization: the selector is updated
with reinforcement learning against a temporarily
fixed generator, and the generator is then fine-tuned
on the highest-reward expert combinations the se-
lector discovers. Over training the two compo-
nents co-adapt, allowing them to jointly discover
coordination patterns that cannot be specified a
priori. To ground this framework in a realistic
domain, we introduceInsureDial, a curated mo-
tor insurance dialogue dataset annotated with user
intent, sentiment, persuasion strategy, and key do-
main terms. Building on these annotations, we
proposePersuaRL, a modular expert-based frame-
work comprising (i) a lightweight Selector trained
via Group Relative Policy Optimization (GRPO)
to dynamically choose relevant experts per turn,
(ii) specialized Experts capturing core persuasion
competencies, and (iii) a Generator, fine-tuned on
selector-chosen expert signals, that integrates them
into coherent and persuasive responses. A compos-
ite reward function guides the selector to jointly op-
timize strategy alignment, intent consistency, con-
textual relevance, and response diversity at each
turn of a multi-turn dialogue.
Contributions:The main contributions of the
paper are:
(i) Framework.We proposePersuaRL, a rein-
forcement learning-based multi-expert framework
for persuasive dialogue generation in the insurance
domain, where a policy selector dynamically coor-
dinates between task-specific experts to generate
persuasive, context-aware responses.
(ii) Benchmark.We introduceInsureDial, a
novel and high-quality dialogue dataset for mo-
tor insurance, annotated across four dimensions
like intent, sentiment, key terms, and engagement
strategy, constructed through a hybrid human-in-
the-loop and LLM generation pipeline.
(iii) Reward Design.We develop domain-
specificreward designincorporating persuasion
strategy alignment, intent consistency, contextual
coherence, response diversity, and a judge based re-
ward, enabling effective RL-based expert selection
without requiring intermediate supervision.
(iv)Evaluation.To demonstrate the effective-
ness of our framework, we conduct comprehen-
sive automated, human, and qualitative evalua-
tions across both in-domain (our insurance dataset,
InsureDial) and out-of-domain (tourism) bench-
marks. The results show thatPersuaRLachieves
strong performance on our benchmark while also
exhibiting robust generalization to out-of-domain
datasets.
2 Related Works
Tool-Augmented LLM:Early work on tool use
in LLMs focused on fixed, trigger-based systems
for tasks like math reasoning (Wang et al., 2024;
Jin et al., 2024; Yue et al., 2023; Chen et al., 2022),
but lacked flexibility. Iterative and supervised tool-
use mechanisms followed (Wang et al., 2023; Chen
et al., 2025). Recent advances treat tool use as
a learnable policy: (Li et al., 2025) employed
tree-structured RL for strategic invocation, while
(Singh et al., 2025) learned reward-based policies
without intermediate supervision. Contrasting scal-
able paradigms include self-supervised Toolformer
(Schick et al., 2023) and training-free modular Oc-
toTools (Lu et al., 2025), highlighting a shift toward
dynamic, efficient tool selection.
Persuasion Support Conversations:Recent
studies have probed LLMs’ persuasive abilities
in dialogue. (Breum et al., 2024) showed LLMs
can influence opinions using social-pragmatic cues,
while (Karinshak et al., 2023) found GPT-3’s pub-
lic health messages often surpassed official con-
tent in impact. (Jin et al., 2024) proposed a multi-
domain persuasive dialogue dataset and an intent-
to-strategy generation model. Persona ground-

ing was shown to enhance coherence and en-
gagement in persuasive exchanges (Zhang et al.,
2018). (Costello et al., 2024) found GPT-4 Turbo
could durably reduce conspiracy beliefs through
evidence-based dialogues. In negotiation tasks,
(Bianchi et al., 2024) observed LLMs effectively
deploying assertive strategies in multi-turn settings.
Kirti et al. (2026) benchmarked LLMs and VLMs
on persuasion datasets and found persuasiveness
varies substantially with prompting strategy and
backbone, while Bozdag et al. (2026) survey com-
putational persuasion and highlight reliable evalu-
ation of persuasiveness as an open challenge. In
task-oriented sales settings, persona-aware persua-
sive dialogue policies have been proposed to han-
dle goal unavailability by persuading users toward
servable alternatives (Tiwari et al., 2022b, 2023).
Raut et al. (2022) introduced multi-modality into
persuasive task-oriented sales agents.
Unlike prior persuasive dialogue systems that
rely on static prompting, heuristic routing, or mono-
lithic generation, this work formulates expert co-
ordination for persuasion as a learnable, context-
conditioned decision problem. Crucially, we train
the selector and generator by alternating optimiza-
tion, so that the two components iteratively adapt to
each other over the course of training.PersuaRL
is one of the earliest framework to learn expert
selection policies for persuasive dialogue via rein-
forcement learning, with coordination that emerges
from this co-adaptive training rather than being
pre-specified.
3 Development ofInsureDialDataset
Prior to this work, no persuasive dialogue datasets
existed for the motor insurance domain. To ad-
dress this gap, we introduceInsureDial, a domain-
specific dataset designed for persuasive motor in-
surance conversations. It contains 1,931 multi-turn
conversations (26,000+ utterances) between users
and agents, focusing on both information deliv-
ery and strategic persuasion. Scenarios span real-
world intents like policy quotes, coverage details,
and price inquiries, with rich domain terminology.
The dataset was developed using a semi-automated,
human-in-the-loop generation framework, where
GPT-4o (OpenAI, 2025c) was employed to draft
diverse persuasive dialogue scenarios, and human
annotators subsequently reviewed and filtered the
conversations to ensure linguistic quality and do-
main accuracy.
3.1 Dataset Preparation
To buildInsureDial, we analyzed leading motor in-
surance websites to extract real-world terminology
and interaction flows, covering categories likeDis-
counts(e.g., No Claim Bonus),Value-Added Ser-
vices(e.g., Roadside Assistance),Coverage Types,
andAdd-ons. The statistics of the dataset are men-
tioned in Table 1 .
3.1.1 Drafting Seed Dialogues
We began by creating 50 high-quality seed dia-
logues entirely authored by trained human anno-
tators simulating persuasive motor insurance con-
versations. In each dialogue, one annotator played
the user while the other acted as the agent (Kelley,
1984), aiming to guide decisions through strate-
gic and informative responses. The seed dialogues
were deliberately designed to cover a comprehen-
sive range of persuasive intents and their possi-
ble combinations within the motor insurance do-
main. Agent utterances were validated with domain
experts to ensure factual accuracy and persuasive
quality. Annotators1 had postgraduate training and
linguistic experience, ensuring natural and strate-
gic interactions. These dialogues served as prompt
exemplars for large-scale LLM-assisted generation
in subsequent stages.
3.1.2 Generating Dialogues.
To identify the most effective prompting strategy,
we began with four seed dialogues and experi-
mented with five carefully designed prompts.The
prompt is shown in Appendix E.Using the GPT-
4o model (temperature = 0.8, top -p = 0.95), we
generated 25 dialogues for each prompt to pro-
mote diverse yet coherent outputs. These were
then manually evaluated by expert annotators on
a three-point scale (1 = low, 2 = moderate, 3 =
high) focusing on persuasive quality. The process
achieved a substantial inter-annotator agreement
(Kappa = 80.2%) (McHugh, 2012), confirming rat-
ing consistency. The prompt that yielded the high-
est number of high-scoring (score = 3) dialogues
was selected to guide the full-scale generation of
theInsureDialdataset, ensuring that the final col-
lection maintained both persuasive strength and
domain relevance.
1Annotators were fairly compensated at rates of $10/hour
for utterance task and $5/hour for verification.

Metric Train Validation Test
Number of Dialogues 1545 97 289
Number of Utterances 21134 1462 4170
Avg Utterances per Dialogue 6.84 7.54 7.21
Avg Words per User Utterance 14.38 17.21 17.19
Avg Words per Agent Utterance 53.78 59.74 56.94
Table 1: Dataset statistics of INSUREDIAL
3.1.3 Dataset Annotation
TheInsureDialdataset was annotated across four
key dimensions to enable the development of ef-
fective persuasive dialogue systems: persuasion
strategy, key domain terms, intent, and sentiment.
Persuasion strategies were assigned to agent utter-
ances to capture the underlying tactics used to in-
fluence user decisions. Domain-specific key terms
were tagged to ensure accurate and context-aware
responses. User turns were labeled with intents to
reflect the communicative goal of each utterance,
while sentiment was annotated to capture emotional
tone and guide adaptive persuasive strategies. An-
notation was conducted using a hybrid approach,
where Gemini-2.0-Flash (Google, 2025) provided
initial labels that were then verified and refined
by human annotators, ensuring high-quality and
consistent annotations for all dialogues.The full
details of the dataset construction and annotations
are given in Appendix B.2.
4 Methodology
Problem Formulation:Given a dialogue con-
text xt, comprising the conversation history and
the current user utterance, the goal is to gener-
ate a persuasive response yt. A selector policy
πθ chooses a subset of expert modules via a binary
mask ot ∈ {0,1}n, where ot,i = 1 activates ex-
pert Ti. Each selected expert produces an output
Oi =T i(xt), which is combined with the dialogue
context to form an augmented prompt
U(x t, ot) = Pack(xt;{O i |o t,i = 1}).(1)
A generator Aϕ then produces the final response
yt =A ϕ(U(x t, ot)). At each dialogue turn, the
dialogue context is treated as the state st ≜x t, and
the expert-selection mask ot as the action. Dur-
ing training the dialogue history follows the gold
dialogue, so the selection at turn t does not alter
the context at turn t+ 1; the selector therefore
solves a context-conditioned, single-step decision
problem at every turn, with reward rt =R(y t, xt)
computed on that turn’s response. The selector and
generator are trained by alternating optimization.
In the selector step, the generator is held fixed and
the selector is updated with Group Relative Policy
Optimization (GRPO) from the rewards of sampled
expert selections; in the generator step, the genera-
tor is fine-tuned on the expert-augmented input of
the highest-reward selection. Holding the genera-
tor fixed within the selector step keeps the reward
signal stationary, while alternating the two steps
lets the components co-adapt across training.
4.1 Selector Module
Persuasive dialogue requires balancing multiple
competing objectives, including engagement strat-
egy, intent alignment, coherence, and diversity. Ex-
isting tool-use RL methods (Li et al., 2025; Singh
et al., 2025) focus on factual tasks with objective
correctness signals, whereas persuasion involves
subjective, interacting rewards that demand funda-
mentally different optimization strategies. In this
work, for context-aware persuasive dialogue gen-
eration, theSelectorlearns a context-conditioned
policy πθ that selects a subset of expert modules
at each dialogue turn. Given dialogue context
xt, the policy outputs a binary selection vector
ot ∈ {0,1}n, where ot,i = 1indicates activation
of expert Ti. Expert selection is treated as a re-
inforcement learning problem, where rewards are
obtained from the quality of the generated response.
We optimize the Selector using GRPO. For each
state, G= 8 expert selections are sampled from the
previous policy and each is decoded by the current
generator, which is held fixed for the duration of
the selector step so that all G candidates are scored
against a stationary generator; the policy is then
updated using a clipped policy-gradient objective
with KL regularization:
JSelector(θ) =Es∼DE{oj }G j=1 ∼πθold

1
G
GX
j=1
min

rratio j Aj,
clip(rratio j ,1−ϵ,1 +ϵ)A j

−βD KL

πθ ∥π ref

(2)
where rratio j = πθ(oj |s) πθold (oj |s). This objective en- ables stable learning over the combinatorial expert-
selection space.

4.2 Experts Module
Persuasive communication is inherently multi-
faceted, requiring simultaneous understanding of
what the user wants (intent), how they feel (sen-
timent), what they’re discussing (keyterms), and
how best to engage them (strategy) . With this
motivation in this work, each expert module Ti
functions as a task-specific tool, instantiated as a
transformer-based decoder-only model fine-tuned
independently for a particular subtask. Given the
dialogue context x, each expert generates an output
Oi =T i(x), capturing a distinct aspect of dialogue
understanding or persuasive reasoning. The expert
modules used in this work are:
1. Engagement Expert:The Engagement Ex-
pert identifies the most contextually appropri-
ate persuasion strategy (Tiwari et al., 2022a)
for the current turn. It is finetuned on labeled
data with six persuasion strategies.
2. Intent Expert:The Intent Expert classifies
the user’s intent at each turn, which is criti-
cal for adapting the persuasion strategy. To
optimize the model, an NLL loss is used.
3. Keyterm Expert:The Keyterm Expert iden-
tifies critical domain-specific terms relevant
to the user’s utterance (e.g., “depreciation,”
“roadside assistance”). The output is a struc-
tured list of important keyphrasesO keyterm.
4. Sentiment Expert:The Sentiment Expert
is responsible for detecting the user’s emo-
tional tone, categorized into three classes:
{Positive, Neutral, Negative}. It is trained us-
ing a cross-entropy classification loss.
A detailed description of the expert module is pro-
vided in Appendix C.2.
4.3 Generator Module
The generator serves as the response generator
that conditions on both the user input and the
outputs of the selected experts. Given a dia-
logue input x and the expert set S={i|
o∗ i = 1} chosen by the selector, each expert pro-
duces text Oi(x), and we build a fused context
U(x, o∗) = Pack(x;{Oi(x)}i∈S), where Pack(·)
denotes concatenation with separators (and trun-
cation to the context window). A decoder-only
generator Aϕ conditions on U(x, o∗) and pro-
duces the response token-by-token with pϕ(yt |
y<t, U(x, o∗)) =A ϕ(y<t, U(x, o∗)), and we fine-
tune Aϕ with the negative log-likelihood objec-
tive Lgen(ϕ) =− PT t=1 logp ϕ(yt |y <t, U(x, o∗)),
where y= (y 1, . . . , yT ) is the ground-truth re-
sponse and o∗ is the highest-reward expert selection
from the preceding selector step. This generator
step alternates with the selector step of Section 4.1:
the generator learns to exploit the expert combi-
nations the selector discovers, and the selector’s
subsequent rollouts are scored by the improved
generator.
4.4 Rewards
Persuasive effectiveness cannot be captured by a
single metric. A response might be strategically
appropriate but miss the user’s intent, or address in-
tent accurately while lacking emotional resonance.
Prior work on persuasive dialogue (Breum et al.,
2024; Jin et al., 2024) evaluates systems using post-
hoc human judgments, but does not incorporate
these quality dimensions during training. To over-
come this limitation and consistent with evidence
that reward models can be designed to generalize
beyond their training distribution and better pos-
training (Ghosal et al., 2025; Ghosh et al., 2026b;
Onyame et al., 2026), we propose a composite re-
ward function that provides explicit training signals
for five dimensions of persuasive quality, enabling
the selector to learn expert coordination patterns
that balance competing objectives. The proposed
rewards are:
Engagement Strategy Consistency Reward
(R1):To ensure consistency with the user’s per-
suasion intent, we introduce a strategy alignment
reward that encourages generated responses to be
semantically aligned with the user’s inferred per-
suasion strategy, estimated via a BERT-based clas-
sifier (Devlin et al., 2019).
Intent Consistency Reward (R2):To ensure
consistency with the user’s intent, we introduce
an intent alignment reward that encourages gener-
ated responses to be semantically aligned with the
user’s inferred intent, estimated via a BERT-based
classifier.
Contextual Appropriateness Reward (R3):To
encourage contextual relevance, we introduce a re-
ward that promotes semantic alignment between
the generated response, the full dialogue context,
and the current user utterance, with greater empha-
sis on the user’s latest turn. The reward is computed
using a semantic similarity metric.
Non-Repetitiveness Reward (R4):To en-

Dialogue context xt
Conversation history
u1, a1, …, ut−1, at−1
User: I ride a 2021 Honda…
User utterance ut
“I do a lot of weekend trips, so I really need peace of mind on the
road. Does your plan cover roadside assistance if I get stranded?”
xt
Selector policy πθ
Single-step decision per turn
lightweight transformer, GRPOmask ot = [1, 1, 1, 0]
Engagement expert
Emotional appeal
Intent expert
Ask_Coverage_Details
1
Keyterm expert
roadside assistance
0
Sentiment expert
not selected
outputs Oi of selected experts
Pack(xt; {Oi}) → U(xt, ot)
Dialogue context + Selected expert outputs
Generator Aφ
Decoder-only LLM, SFT on mask o*
Agent response yt
“I completely understand how important it is to feel safe and supported during your weekend rides.
Our comprehensive motor insurance includes third-party, own damage and personal accident cover but
also 24/7 roadside assistance. Whether it’s a flat tyre or a breakdown, help is always just a call away,
we’ve got your back wherever the road takes you.”
Training: alternating optimization
Selector and generator updated in turn;
experts and reward models frozen.
Selector step (GRPO)
Aφ fixed; sample G = 8 masks
Generator step (SFT)
πθ fixed; take best mask o*
o* (best mask)
improved Aφ
Frozen reward models
R1 Engagement strategy consistency
R2 Intent consistency
R3 Contextual appropriateness
R4 Non-repetitiveness
R5 Judge reward
R
update θ
update φ
11
Figure 1:PersuaRLarchitecture with selector, generator, and reward-guided response generation. Selector and
generator are trained by alternating optimization; experts and reward models are frozen. Solid arrows mark the
inference path followed at every turn, dashed arrows carry training-time signals only, and the faded box denotes an
expert not selected by the mask.
courage response diversity and reduce redun-
dancy across dialogue turns, we introduce a non-
repetitiveness reward that penalizes lexical overlap
between the current generated response and the pre-
vious model response. This reward helps prevent
repetitive or stagnant dialogue behavior.
Judge Reward (R5):To capture high-level per-
suasive quality beyond surface-level signals, we
introduce a judge-based reward that evaluates gen-
erated responses along dimensions such as persua-
siveness, negotiation effectiveness, and user en-
gagement, using an LLM acting as an automatic
evaluator.The judge prompt is given in section E.
The overall reward is computed as: R=β 1R1 +
β2R2 +β 3R3 +β 4R4 +β 5R5,whereβ 1 +β 2 +
β3 +β 4 +β 5 = 1. In addition to the rewards,
we employed auxiliary penalty terms to promote
efficient, diverse, and balanced expert selection
during training.We provide a detailed description
of all rewards and penalties in the Appendix C.5.
5 Experimental Results and Analysis
This section presents the experimental setup and
provides a thorough evaluation of the proposed
model,PersuaRL, through automatic, human, and
qualitative assessments.
5.1 Data Preprocessing
We useInsureDial, curated via a semi-automated
pipeline combining LLM generation with hu-
man refinement. Dialogues cover diverse motor-
insurance scenarios and persuasion strategies, seg-
mented into user–agent turns to preserve multi-turn
context. Annotations (intent, sentiment, key terms,
and persuasion strategy) were quality-checked for
consistency with dialogue flow. The corpus is
split 80/5/15 into train/validation/test, with diver-
sity maintained across splits.Additional experi-
mental setup are shown in D.2.
5.2 Baselines Setup
We evaluate both closed-source and open-weight
baselines in a single-shot setting, alongside a super-
vised fine-tuning (SFT) baseline. In the single-
shot setup, models generate responses directly
from the input without tool usage or intermedi-
ate reasoning. The comparison includes both open
weight and proprietary models. To assess portabil-
ity, we instantiatePersuaRLon open-weight back-
bones: LLAMA-3.2-3B-INSTRUCT(Meta, 2024b),

Dataset Models BLEU-2↑METEOR↑BERTF1↑DISTINCT-2↑ROUGE-1↑LLM-J↑
InsureDial
GPT 5 0.036 0.093 0.828 0.982 0.232 –
GPT 4.1 mini 0.124 0.143 0.620 0.998 0.383 –
Deepseek R1 Distill Llama 70B 0.069 0.125 0.569 0.920 0.260 4.25
Llama 3.3 70B Instruct 0.126 0.137 0.610 0.996 0.377 4.16
Qwen 3 32B 0.107 0.132 0.588 0.998 0.371 3.84
Phi-3-Medium 14B 0.169 0.167 0.655 0.995 0.441 3.78
Qwen 2.5 7B instruct 0.124 0.145 0.604 0.958 0.385 3.66
Llama 3.1 8B instruct 0.132 0.146 0.605 0.966 0.388 3.67
Qwen 2.5 3B Instruct (Single) 0.090 0.128 0.562 0.965 0.310 2.66
Qwen 2.5 3B Instruct (SFT) 0.305 0.217 0.727 0.991 0.556 3.28
PersuaRL (Qwen 2.5 3B) 0.375 0.250 0.760 0.991 0.609 3.81
Llama 3.2 3B Instruct (Single) 0.106 0.135 0.585 0.937 0.334 2.86
Llama 3.2 3B Instruct (SFT) 0.339 0.232 0.742 0.989 0.584 3.48
PersuaRL (Llama 3.2 3B) 0.398 0.276 0.771 0.989 0.631 3.95
Phi 3 mini 128k (Single) 0.181 0.156 0.641 0.980 0.429 2.79
Phi 3 mini 128k (SFT) 0.362 0.242 0.752 0.988 0.600 3.39
PersuaRL (Phi 3 mini) 0.374 0.261 0.762 0.990 0.611 3.86
Mistral 24B Instruct (Single) 0.043 0.094 0.772 0.898 0.195 3.02
Mistral 24B Instruct (SFT) 0.324 0.226 0.815 0.990 0.574 3.65
PersuaRL (Mistral 24B) 0.355 0.241 0.873 0.992 0.596 4.12
DEAL
(Priya
et al.,
2024)
Llama 3.2 3B instruct (Single) 0.049 0.085 0.519 0.937 0.195 2.41
Llama 3.2 3B instruct (SFT) 0.0800.104 0.5520.986 0.267 2.64
PersuaRL (Llama 3.2 3B) 0.0870.101 0.5360.987 0.278 2.79
Phi 3 mini 128k (Single) 0.086 0.106 0.552 0.973 0.265 2.37
Phi 3 mini 128k (SFT) 0.089 0.110 0.558 0.984 0.273 2.56
PersuaRL (Phi 3 mini) 0.094 0.121 0.568 0.985 0.281 2.72
Table 2: Automatic evaluation results forInsureDialand DEAL datasets. Bold values indicate the best performance
within each model group. Results are statistically significant at 5% significance level based on t-test. LLM-as-a-
Judge scores are omitted for GPT models to avoid evaluation bias, as the underlying judge model is also GPT-based.
PHI-3-MINI(Abdin et al., 2024), QWEN-2.5-3B-
INSTRUCT(Yang et al., 2024), and MISTRAL-24B-
INSTRUCT(Mistral AI, 2025), evaluating under
three regimes: (i) single-shot, (ii) SFT, and (iii)
PersuaRL.Additional details regarding the base-
lines are mentioned in Appendix C.
5.3 Evaluation Metrics
We conduct both automatic and human evalua-
tions to assess the response quality. Automatic
metrics include ROUGE-1 (R1) (Lin, 2004),
BLEU-2 (B2) (Papineni et al., 2002), METEOR
(MT) (Banerjee and Lavie, 2005), BERT-F1
(BF1) (Zhang et al., 2019), DISTINCT-2 (D2) (Li
et al., 2015), and LLM-AS-A-JUDGE(LLM-J)
(OpenAI, 2025a). Human evaluation is performed
across five dimensions 2: Fluency (F), Engaging-
ness (E), Persuasive Effectiveness (PE), Strategy
Appropriateness (SA), and Resistance Handling
(RH).Full details are provided in the Appendix
under the section C.
2Human evaluation was conducted using a 5-point scale,
where 1 indicates the lowest and 5 the highest performance.
6 Results and Findings
Table 2 presents the automatic evaluation results
for our framework,PersuaRL, alongside multiple
baselines and serves as the basis for addressing the
research questions outlined below.
6.1 Research Questions
R1) How good isPersuaRLcompared to the
baselines?PersuaRL(Mistral)consistently out-
performs all baselines on theInsureDialdataset
as shown in Table 2. Specifically, small backbone
likeLlama 3.2–3BPersuaRLachieves the result of
BF1 ≈ 0.771, B2 ≈ 0.398, and R1 ≈ 0.631, outper-
forming much larger 14–70B vanilla baseline mod-
els. For example,PersuaRL(Phi-3 Mini) exceeds
Phi-3 Medium 14B by roughly 16% and Qwen-
3 32B by over 29% in BERT-F1. Although SFT
helps models adapt to the insurance domain, its
improvements largely saturate at surface-level gen-
eration. In contrast,PersuaRLconsistently pushes
the models beyond this plateau.
R2) Can reward-guided reinforcement learn-
ing for expert selection outperform heuristic,
prompt-based routing in persuasive dialogue
systems?PersuaRLsurpasses prompt-based rout-
ing by framing expert selection as a learnable ac-

tion optimized through reward-driven credit assign-
ment. While prompt-based routers rely on fixed
heuristics without feedback,PersuaRLuses GRPO
to iteratively learn which expert combinations max-
imize persuasive effectiveness, enabling adaptive
and context-sensitive expert coordination.
R3) How robust and transferable isPer-
suaRL?To rigorously assess the robustness and
cross-domain transferability ofPersuaRL, we con-
ducted evaluations on the out-of-domain DEAL
dataset, as shown in Table 2. Across all backbone
configurations (Single → SFT → PersuaRL), we
observe consistent and monotonic improvements,
reflected in higher BF1 and R1 scores. Beyond ag-
gregate performance, we further analyze the nature
of transfer across domains. Despite differences in
domain semantics (insurance vs. travel), annota-
tion taxonomies, and user objectives,PersuaRL
maintains strong performance, suggesting that the
learned selector policies capture domain-agnostic
persuasion patterns such as intent adaptation, and
strategic framing rather than overfitting to dataset-
specific heuristics. To better understand transfer
behavior, we conducted a detailed error analysis
(see Table 18). These findings indicate thatPer-
suaRLlearns a combination of domain-agnostic co-
ordination strategies (reward models) and domain-
sensitive adaptations(generator), supporting its ro-
bustness and applicability across diverse dialogue
settings.
7 Ablation Studies
Ablation study w.r.t Experts:The fullPersuaRL
model achieves the best overall performance, in-
dicating that jointly leveraging all experts yields
more persuasive responses. Removing any expert
leads to consistent degradation, confirming that
each module contributes meaningfully to the sys-
tem. Results are reported in Table 3 using auto-
matic metrics. Among the experts, the Engagement
and Intent modules have the most pronounced im-
pact. Excluding either results in notable drops in
semantic alignment and relevance. Although the
keyterm expert and sentiment expert’s individual
impact is comparatively smaller, its removal still
leads to a measurable decline in the overall quality.
All Tools vsPersuaRL:We evaluatePersuaRL
against theAllExpertbaseline, which uniformly
activates all experts, across both PHIand LLAMA-
3B LLMs. This ablation shows theimpact of the
selectorin our framework.PersuaRLconsistently
Models B-2↑MT↑BF1↑D-2↑R1↑
InsureDial
PersuaRL0.375 0.250 0.760 0.991 0.609
PersuaRL- Engagement Expert 0.284 0.202 0.704 0.983 0.539
PersuaRL- Intent Expert 0.293 0.216 0.713 0.983 0.558
PersuaRL- Keyterm Expert 0.302 0.223 0.721 0.984 0.566
PersuaRL- Sentiment Expert 0.324 0.231 0.736 0.990 0.583
Table 3: Ablation study of expert modules forPersuaRL
on the Qwen 2.5 3B model.
Models F↑E↑PE↑SA↑RH↑
InsureDial
Llama 3.2 3B Instruct (Single) 2.47 2.31 2.13 2.39 2.94
Llama 3.2 3B Instruct (SFT) 3.11 2.94 2.46 2.88 3.38
PersuaRL (Llama 3.2 3B) 4.12 4.51 4.36 4.29 4.46
Qwen 2.5 3B Instruct (Single) 2.69 2.45 2.29 2.68 3.10
Qwen 2.5 3B Instruct (SFT) 3.19 2.98 2.86 3.10 3.61
PersuaRL (Qwen 2.5 3B) 3.94 4.22 4.23 4.06 4.32
Mistral 24B Instruct (Single) 2.98 2.81 2.53 2.74 3.27
Mistral 24B Instruct (SFT) 3.23 3.34 3.10 3.19 3.76
PersuaRL (Mistral 24B) 4.26 4.39 4.54 4.33 4.45
Table 4: Human evaluation result onInsureDial
datasets. The Single → SFT → PersuaRL trend holds
consistently at 3B–24B scale.
outperforms AllExpert across all metrics, as shown
in Figure 2, demonstrating strong generalization
and better alignment with task preferences. No-
tably, it shows substantial gains in generation qual-
ity, particularly in semantic relevance and lexical
overlap, with improvements most pronounced in
R1 and BF1.
Prompting Tool Selection VsPersuaRL:Per-
suaRLoutperforms prompt-based routing across
both PHIand LLAMA-3B backbones, achieving
higher fluency, relevance, and overall generation
quality through preference-aligned expert coordina-
tion. These gains are consistent and do not compro-
mise output diversity, demonstrating the effective-
ness of reinforcement learning over generic routing
strategies.
8 Human Evaluation
A team of annotators with domain expertise in in-
surance dialogue evaluation conducted a human
assessment on 30% of the randomly sampledIn-
sureDialtest set. We evaluated three variants for
each LLM (Llama 3.2 3B, Qwen 2.5 3B, and Mis-
tral 24B):Single-shot,SFT-finetuned, and our pro-
posedPersuaRLframework. As shown in Table
4,PersuaRLachieves the highest scores across all
five dimensions for all the backbones, indicating
consistent improvements in naturalness, engage-
ment, and persuasion.

Figure 2: Ablation Study of Llama 3B and Phi 3B variants under (a) All Tools (no selector), (b) Tools Selected via
Prompting, (c) Tool Selection via Reward-DrivenPersuaRL.
9 Qualitative Analysis
Figure 3 and Table 7 highlights qualitative differ-
ences between responses from single-shot, SFT,
andPersuaRL, demonstrating two key distinctions:
(1)PersuaRLgenerates more empathetic and per-
suasive responses, as seen in: “I completely under-
stand how important it is to feel safe and supported
during your weekend rides,” followed by reassur-
ances like “help is always just a call away” and
“we’ve got your back wherever the road takes you”.
In contrast, SFT responses are more informative
yet neutral merely listing features without user-
centric framing. (2)PersuaRLalso demonstrates
greater fluency and structure, combining coverage
details with contextual reassurance. For example,
it fluidly mentions “third-party, own damage, and
personal accident coverage but also 24/7 roadside
assistance,” linking technical information with per-
suasive language. On the other hand, SFT and
single shot give factual completeness but miss emo-
tional framing. Additional qualitative examples
generated byPersuaRLare provided in Appendix
Table 20 and Table 21.
10 Conclusion
In this work, we proposedPersuaRL, a reinforce-
ment learning-based framework for persuasive dia-
logue generation in the insurance domain. Through
modular expert design and reward-guided selec-
tion,PersuaRLenables context-aware generation
across LLM backbones. We also introducedIn-
sureDial, a high-quality annotated dataset for in-
surance persuasion.PersuaRLconsistently outper-
forms strong baselines across single-shot, SFT, and
RL settings, including larger models, while pro-
ducing fluent, persuasive, and emotionally aligned
responses, highlighting its effectiveness for modu-
lar, goal-driven LLMs.
I do a lot of weekend trips, so I really need peace of mind on the
road. Does your plan cover roadside assistance if I get stranded?
Our comprehensive motor insurance plan includes roadside
assistance along with standard coverages like third-party
liability and personal accident. This means you’ll have help if
your bike breaks down or you face any minor issues. Single
In addition to third-party liability and personal accident cover, our
comprehensive plan also includes roadside assistance. This means
you'll have help whenever you need it, whether it's a flat tire, running
out of fuel, or any other unexpected issues during your weekend rides.
SFT
I completely understand how important it is to feel safe and
supported during your weekend rides. Our comprehensive motor
insurance not only includes third-party, own damage, and personal
accident coverage but also 24/7 roadside assistance. Whether it’s a flat
tire, fuel shortage, or any unexpected breakdown, help is always just a
call away. With this plan, you can enjoy your trips with total peace of
mind, knowing that we’ve got your back wherever the road takes you.
 PersuaRL
😕
😐
😀
Figure 3: Qualitative analysis for an input utterance,
response by single, SFT and ourPersuaRL.
11 Limitations
The limitations of this work are stated in the below
points :
• InsureDialis constructed using a semi-
automated pipeline where GPT-4o generates dia-
logues that are subsequently filtered by humans;
this may introduce synthetic artifacts and may
not fully capture real user behavior.
• The expert-selection policy operates over a binary
mask, causing the action space to grow exponen-
tially as the number of experts increases, which
can hinder scalability despite the stabilizing ef-
fect of GRPO.
• Invoking multiple expert modules per dialogue
turn increases inference latency, computational
cost, and system complexity compared to single-
model baselines, potentially impacting real-
world deployment.
• All evaluation is offline and conditioned on gold

dialogue history, so the model’s own responses
never shape subsequent turns. We, therefore, do
not assess interactive rollouts or real-user out-
comes; live user studies remain future work.
• While we evaluatePersuaRLon smaller open-
weight backbones (3B–24B), applying the full
framework with large-scale LLMs as both the
selector and generator was not feasible due to
computational resource constraints, as this de-
mands substantial GPU memory and compute.
We note this as a promising direction for future
work.
12 Ethics Section
This work emphasizes ethical persuasion by treat-
ing it as decision support rather than decision en-
forcement, ensuring that user autonomy is pre-
served and that responses align with user intent,
sentiment, and context without applying coercive
or repetitive pressure. Given high-stakes domains,
where inaccuracies can lead to harm, particular
care is taken to ensure factual accuracy and pre-
vent misleading information(Sahoo et al., 2024;
Ghosh et al., 2025). To mitigate such risks,In-
sureDialwas developed using a human-in-the-loop
process, with domain experts validating seed dia-
logues and annotators verifying model-generated
conversations, and explicitly annotating strategies
and intents to support context-aware persuasion
across multi-turn interactions.
Acknowledgement
This research was conducted as part of the project
“Conversational Agents with Negotiation and In-
fluencing Ability”, sponsored by Accenture Labs,
Bangalore, India. The authors also acknowledge
the National Supercomputing Mission (NSM) for
providing computing resources on the PARAM
Rudra supercomputer.
References
Marah Abdin, Sam Ade Jacobs, Ammar Ahmad Awan,
Jyoti Aneja, Ahmed Awadallah, and Awadalla et al.
2024. Phi-3 technical report: A highly capable lan-
guage model locally on your phone.arXiv preprint
arXiv:2404.14219.
Satanjeev Banerjee and Alon Lavie. 2005. Meteor: An
automatic metric for mt evaluation with improved cor-
relation with human judgments. InProceedings of
the acl workshop on intrinsic and extrinsic evaluation
measures for machine translation and/or summariza-
tion, pages 65–72.
Federico Bianchi, Patrick John Chia, Mert Yuksek-
gonul, Jacopo Tagliabue, Dan Jurafsky, and James
Zou. 2024. How well can llms negotiate? nego-
tiationarena platform and analysis.arXiv preprint
arXiv:2402.05863.
Nimet Beyza Bozdag, Shuhaib Mehri, Xiaocheng Yang,
Hyeonjeong Ha, Zirui Cheng, Esin Durmus, Jiax-
uan You, Heng Ji, Gokhan Tur, and Dilek Hakkani-
Tür. 2026. Must read: A comprehensive survey of
computational persuasion.ACM Computing Surveys,
58(12):1–39.
Simon Martin Breum, Daniel Vædele Egdal, Vic-
tor Gram Mortensen, Anders Giovanni Møller, and
Luca Maria Aiello. 2024. The persuasive power of
large language models. InProceedings of the Inter-
national AAAI Conference on Web and Social Media,
volume 18, pages 152–163.
Wenhu Chen, Xueguang Ma, Xinyi Wang, and
William W Cohen. 2022. Program of thoughts
prompting: Disentangling computation from reason-
ing for numerical reasoning tasks.arXiv preprint
arXiv:2211.12588.
Zhipeng Chen, Yingqian Min, Beichen Zhang, Jie Chen,
Jinhao Jiang, Daixuan Cheng, Wayne Xin Zhao,
Zheng Liu, Xu Miao, Yang Lu, and 1 others. 2025.
An empirical study on eliciting and improving r1-like
reasoning models.arXiv preprint arXiv:2503.04548.
Thomas H Costello, Gordon Pennycook, and David G
Rand. 2024. Durably reducing conspiracy
beliefs through dialogues with ai.Science,
385(6714):eadq1814.
DeepSeek-AI. 2025. Deepseek-r1: Incentivizing rea-
soning capability in llms via reinforcement learning.
Preprint, arXiv:2501.12948.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. Bert: Pre-training of deep
bidirectional transformers for language understand-
ing. InProceedings of the 2019 conference of the
North American chapter of the association for com-
putational linguistics: human language technologies,
volume 1 (long and short papers), pages 4171–4186.
Soumya Suvra Ghosal, Vaibhav Singh, Akash Ghosh,
Soumyabrata Pal, Subhadip Baidya, Sriparna Saha,
and Dinesh Manocha. 2025. Relic: Enhancing re-
ward model generalization for low-resource indic
languages with few-shot examples. InEMNLP (Find-
ings), pages 1502–1517.
Akash Ghosh, Tajamul Ashraf, Rishu Kumar Singh,
Numan Saeed, Sriparna Saha, Xiuying Chen, and
Salman Khan. 2026a. Carepilot: A multi-agent
framework for long-horizon computer task automa-
tion in healthcare.arXiv preprint arXiv:2603.24157.

Akash Ghosh, Nishant Kumar, Nitesh Patnaik, Adity
Prakash, Rishi Raj, and Sriparna Saha. 2026b. Rado:
Trustworthy radiology impression generation using
safety and faithfulness-based preference optimiza-
tion.ACM Transactions on Computing for Health-
care, 7(3):1–18.
Akash Ghosh, Srivarshinee Sridhar, Raghav Kaushik
Ravi, Muhsin Muhsin, Sriparna Saha, and Chirag
Agarwal. 2025. Clinic: Evaluating multilingual trust-
worthiness in language models for healthcare.arXiv
preprint arXiv:2512.11437.
Google. 2025. Gemini model up-
dates february 2025. https://blog.
google/technology/google-deepmind/
gemini-model-updates-february-2025/ . Ac-
cessed: 2025-07-30.
Tanmoy Kanti Halder, Akash Ghosh, Subhadip Baidya,
Arijit Roy, and Sriparna Saha. 2026. Arogyasu-
tra: A multi-agent framework for multimodal med-
ical reasoning in indic languages.arXiv preprint
arXiv:2606.13572.
Chuhao Jin, Kening Ren, Lingzhen Kong, Xiting Wang,
Ruihua Song, and Huan Chen. 2024. Persuading
across diverse domains: a dataset and persuasion
large language model. InProceedings of the 62nd
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 1678–
1706.
Sunghee Jung, Donghun Lee, Shinbok Lee, Gaeun
Seo, Daniel Lee, Byeongil Ko, Junrae Cho, Ki-
hyun Kim, Eunggyun Kim, and Myeongcheol Shin.
2025. Diatool-dpo: Multi-turn direct preference opti-
mization for tool-augmented large language models.
arXiv preprint arXiv:2504.02882.
Elise Karinshak, Sunny Xun Liu, Joon Sung Park, and
Jeffrey T Hancock. 2023. Working with ai to per-
suade: Examining a large language model’s abil-
ity to generate pro-vaccination messages.Proceed-
ings of the ACM on Human-Computer Interaction,
7(CSCW1):1–29.
John F Kelley. 1984. An iterative design methodology
for user-friendly natural language office information
applications.ACM Transactions on Information Sys-
tems (TOIS), 2(1):26–41.
Seungone Kim, Juyoung Suk, Shayne Longpre,
Bill Yuchen Lin, Jamin Shin, Sean Welleck, Graham
Neubig, Moontae Lee, Kyungjae Lee, and Minjoon
Seo. 2024. Prometheus 2: An open source language
model specialized in evaluating other language mod-
els.Preprint, arXiv:2405.01535.
Rohan Kirti, Atharva S Deshmukh, Kiran K Dugana,
Yash Rathore, Shipra Shriparn, Sriparna Saha,
Roshni R Ramnani, and Anutosh Maitra. 2026. Can
language models persuade? exploring the persuasive
efficacy of large language and vision language mod-
els.Computer Speech & Language, page 101991.
Jiwei Li, Michel Galley, Chris Brockett, Jianfeng Gao,
and Bill Dolan. 2015. A diversity-promoting objec-
tive function for neural conversation models.arXiv
preprint arXiv:1510.03055.
Xuefeng Li, Haoyang Zou, and Pengfei Liu. 2025.
Torl: Scaling tool-integrated rl.arXiv preprint
arXiv:2503.23383.
Chin-Yew Lin. 2004. Rouge: A package for automatic
evaluation of summaries. InText summarization
branches out, pages 74–81.
Pan Lu, Bowen Chen, Sheng Liu, Rahul Thapa, Joseph
Boen, and James Zou. 2025. Octotools: An agentic
framework with extensible tools for complex reason-
ing.arXiv preprint arXiv:2502.11271.
Weicheng Ma, Hefan Zhang, Ivory Yang, Shiyu Ji, Joice
Chen, Farnoosh Hashemi, Shubham Mohole, Ethan
Gearey, Michael Macy, Saeed Hassanpour, and 1
others. 2025. Communication is all you need: Per-
suasion dataset construction via multi-llm communi-
cation.arXiv preprint arXiv:2502.08896.
Mary L McHugh. 2012. Interrater reliability: the kappa
statistic.Biochemia medica, 22(3):276–282.
Meta. 2024a. Llama 3.3 70b instruct is now available on
github models (ga). Llama 3.3 70B Instruct release.
Meta. 2024b. Meta LLaMA -3.2 3B Instruct.
Instruction-tuned 3 billion -parameter lightweight
text-only model with 128K context window
(Llama3.2 series).
Meta AI. 2024. Meta LLaMA -3.1 8B Instruct.
Instruction-tuned variant of LLaMA 3.1 with 8 bil-
lion parameters and 128K context length.
Mistral AI. 2025. Mistral small 3. Mistral-
Small-24B-Instruct-2501. Available at
https://huggingface.co/mistralai/
Mistral-Small-24B-Instruct-2501.
Eric Onyame, Akash Ghosh, Subhadip Baidya, Sri-
parna Saha, Xiuying Chen, and Chirag Agarwal.
2026. Cure-med: Curriculum-informed reinforce-
ment learning for multilingual medical reasoning. In
Proceedings of the 64th Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 30682–30703.
OpenAI. 2025a. Introducing GPT-5. Accessed: 2026-
03-16.
OpenAI. 2025b. OpenAI GPT -4.1 Mini. Launched
alongside GPT-4.1 and GPT-4.1 nano; supports up to
1M token context, improved coding and instruction-
following performance.
OpenAI. 2025c. OpenAI GPT-4o. Launched alongside
GPT-4.1 and GPT-4.1 nano; supports up to 1M token
context, improved coding and instruction-following
performance.

Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: a method for automatic evalu-
ation of machine translation. InProceedings of the
40th annual meeting of the Association for Computa-
tional Linguistics, pages 311–318.
Adam Paszke, Sam Gross, Francisco Massa, Adam
Lerer, James Bradbury, Gregory Chanan, Trevor
Killeen, Zeming Lin, Natalia Gimelshein, Luca
Antiga, and 1 others. 2019. Pytorch: An impera-
tive style, high-performance deep learning library.
Advances in neural information processing systems,
32.
Priyanshu Priya, Desai Vishesh Yasheshbhai, Rat-
nesh Kumar Joshi, Roshni Ramnani, Anutosh Maitra,
Shubhashis Sengupta, and Asif Ekbal. 2024. Trip
negotiator: A travel persona-aware reinforced dia-
logue generation model for personalized integrative
negotiation in tourism. InFindings of the Association
for Computational Linguistics: EMNLP 2024, pages
16566–16595.
Ganesh Prasath Ramani, Shirish Karande, Yash Bhatia,
and 1 others. 2024. Persuasion games using large
language models.arXiv preprint arXiv:2408.15879.
Aritra Raut, Subrata Das, Abhisek Tiwari, Sriparna
Saha, Anutosh Maitra, Roshni Ramnani, and Shub-
hashis Sengupta. 2022. Introducing multi-modality
in persuasive task oriented virtual sales agent. In
International Conference on Neural Information Pro-
cessing, pages 543–555. Springer.
Pranab Sahoo, Prabhash Meharia, Akash Ghosh, Sri-
parna Saha, Vinija Jain, and Aman Chadha. 2024.
A comprehensive survey of hallucination in large
language, image, video and audio foundation mod-
els.Findings of the association for computational
linguistics: EMNLP 2024, pages 11709–11724.
Azlaan Mustafa Samad, Kshitij Mishra, Mauajama Fir-
daus, and Asif Ekbal. 2022. Empathetic persuasion:
reinforcing empathy and persuasiveness in dialogue
systems. InFindings of the Association for Compu-
tational Linguistics: NAACL 2022, pages 844–856.
Victor Sanh, Lysandre Debut, Julien Chaumond, and
Thomas Wolf. 2019. Distilbert, a distilled version
of bert: smaller, faster, cheaper and lighter.arXiv
preprint arXiv:1910.01108.
Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta
Raileanu, Maria Lomeli, Eric Hambro, Luke Zettle-
moyer, Nicola Cancedda, and Thomas Scialom. 2023.
Toolformer: Language models can teach themselves
to use tools.Advances in Neural Information Pro-
cessing Systems, 36:68539–68551.
Jeonghoon Shim, Gyuhyeon Seo, Cheongsu Lim, and
Yohan Jo. 2025. Tooldial: Multi-turn dialogue gen-
eration method for tool-augmented language models.
arXiv preprint arXiv:2503.00564.
Joykirat Singh, Raghav Magazine, Yash Pandya, and
Akshay Nambi. 2025. Agentic reasoning and tool
integration for llms via reinforcement learning.arXiv
preprint arXiv:2505.01441.
Palleti Divya Sree, Manohar Raj Kokkiligadda, Jagan-
nadham Teja, and Yelisetti Sandeep. 2023. Product
negotiation in e-commerce website using chatbot. In
2023 7th International Conference on Computing
Methodologies and Communication (ICCMC), pages
879–883. IEEE.
Jutta Stock, V olha Petukhova, and Dietrich Klakow.
2022. Assessment of sales negotiation strategies with
iso 24617-2 dialogue act annotations. InProceedings
of the 18th Joint ACL-ISO Workshop on Interoper-
able Semantic Annotation within LREC2022, pages
10–19.
Takehiro Takayanagi, Kiyoshi Izumi, Javier Sanz-
Cruzado, Richard McCreadie, and Iadh Ounis. 2025.
Are generative ai agents effective personalized finan-
cial advisors? InProceedings of the 48th Interna-
tional ACM SIGIR Conference on Research and De-
velopment in Information Retrieval, pages 286–295.
Qwen Team. 2025. Qwen3 technical report.Preprint,
arXiv:2505.09388.
Abhisek Tiwari, Abhijeet Khandwe, Sriparna Saha,
Roshni Ramnani, Anutosh Maitra, and Shubhashis
Sengupta. 2023. Towards personalized persuasive
dialogue generation for adversarial task oriented di-
alogue setting.Expert Systems with Applications,
213:118775.
Abhisek Tiwari, Sriparna Saha, Shubhashis Sengupta,
Anutosh Maitra, Roshni Ramnani, and Pushpak Bhat-
tacharyya. 2022a. Persona or context? towards build-
ing context adaptive personalized persuasive virtual
sales assistant. InProceedings of the 2nd Conference
of the Asia-Pacific Chapter of the Association for
Computational Linguistics and the 12th International
Joint Conference on Natural Language Processing
(Volume 1: Long Papers), pages 1035–1047.
Abhisek Tiwari, Tulika Saha, Sriparna Saha, Shubhashis
Sengupta, Anutosh Maitra, Roshni Ramnani, and
Pushpak Bhattacharyya. 2022b. A persona aware per-
suasive dialogue policy for dynamic and co-operative
goal setting.Expert Systems with Applications,
195:116303.
Hongru Wang, Yujia Qin, Yankai Lin, Jeff Z Pan, and
Kam-Fai Wong. 2024. Empowering large language
models: Tool learning for real-world interaction. In
Proceedings of the 47th International ACM SIGIR
Conference on Research and Development in Infor-
mation Retrieval, pages 2983–2986.
Ke Wang, Houxing Ren, Aojun Zhou, Zimu Lu, Sichun
Luo, Weikang Shi, Renrui Zhang, Linqi Song,
Mingjie Zhan, and Hongsheng Li. 2023. Math-
coder: Seamless code integration in llms for en-
hanced mathematical reasoning.arXiv preprint
arXiv:2310.03731.

Xuewei Wang, Weiyan Shi, Richard Kim, Yoojung Oh,
Sijia Yang, Jingwen Zhang, and Zhou Yu. 2019. Per-
suasion for good: Towards a personalized persua-
sive dialogue system for social good.arXiv preprint
arXiv:1906.06725.
Benjamin Warner, Antoine Chaffin, Benjamin Clavié,
Orion Weller, Oskar Hallström, Said Taghadouini,
Alexis Gallagher, Raja Biswas, Faisal Ladhak, Tom
Aarsen, and 1 others. 2024. Smarter, better, faster,
longer: A modern bidirectional encoder for fast,
memory efficient, and long context finetuning and
inference.arXiv preprint arXiv:2412.13663.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Rémi Louf, Morgan Funtow-
icz, and 1 others. 2019. Huggingface’s transformers:
State-of-the-art natural language processing.arXiv
preprint arXiv:1910.03771.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng,
Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan
Li, Dayiheng Liu, Fei Huang, Guanting Dong, Hao-
ran Wei, Huan Lin, Jialong Tang, Jialin Wang, Jian
Yang, Jianhong Tu, Jianwei Zhang, Jianxin Ma, and
40 others. 2024. Qwen2 technical report.arXiv
preprint arXiv:2407.10671.
Xiang Yue, Xingwei Qu, Ge Zhang, Yao Fu, Wen-
hao Huang, Huan Sun, Yu Su, and Wenhu Chen.
2023. Mammoth: Building math generalist models
through hybrid instruction tuning.arXiv preprint
arXiv:2309.05653.
Saizheng Zhang, Emily Dinan, Jack Urbanek, Arthur
Szlam, Douwe Kiela, and Jason Weston. 2018. Per-
sonalizing dialogue agents: I have a dog, do you have
pets too?arXiv preprint arXiv:1801.07243.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q
Weinberger, and Yoav Artzi. 2019. Bertscore: Eval-
uating text generation with bert.arXiv preprint
arXiv:1904.09675.

Frequently Asked Questions
1. Is the strategy-consistency reward mis-
aligned since persuasion strategies are anno-
tated on agent turns, not user turns?
Response:The strategy-consistency reward is
used as a soft alignment signal rather than a hard
supervisory target. While strategy annotations are
available for agent turns, conditioning on the user
utterance encourages the selector to anticipate the
appropriate persuasive response given the user’s
expressed needs. We acknowledge this approxima-
tion and view it as a practical surrogate that avoids
requiring gold strategy labels at inference time.
2. Are the reward equations underspecified,
particularly with respect to class probabilities
and weights?
Response:The reward formulation uses class-
conditional probabilities from pretrained classifiers;
the omission of explicit class indices in the main
text was for brevity. All rewards are computed
using the predicted probability of the target class,
and weights are normalized to sum to one.
3. Does the contextual similarity reward en-
courage copying from the dialogue context or
user utterance?
Response:To mitigate copying, the contextual
reward is complemented by a non-repetitiveness
penalty that discourages lexical overlap with prior
agent responses. Empirically, we observe improve-
ments in diversity metrics (DISTINCT-2) alongside
relevance gains, indicating that the model does not
simply copy input text.
4. Is the selector architecture and GRPO
training pipeline sufficiently specified for repro-
ducibility?
Response:The selector is implemented as a
lightweight transformer-based policy operating
over a binary expert mask. GRPO is used with
fixed group size, clipping range, and KL regulariza-
tion. While the main paper focuses on conceptual
clarity, all architectural details, hyperparameters,
and training phases are provided in the appendix.
5. Why are some closely related persuasion
and routing baselines not included?
Response :Our primary goal is to compare
against strong single-shot, SFT, and heuristic-
routing baselines under identical backbones. Many
intent-to-strategy and persona-aware models rely
on additional supervision or assumptions not di-
rectly comparable to our expert-selection setting.
6. Does reinforcement learning improve per-
suasion or just optimize reward models?
Response :PersuaRLapplies reinforcement
learning only toexpert-selectionactions. The gen-
erator is held fixed within each GRPO step and is
never updated on the reward directly; it is updated
only by supervised fine-tuning on the ground-truth
response given the highest-reward expert selection.
This limits the policy’s ability to exploit reward
artifacts. Despite relying on rewards, the learned
selection policy consistently improves independent
human evaluated metrics, indicating that reward-
optimized expert generalizes beyond the reward
models.
7. How doesPersuaRLavoid reward circular-
ity during training?
Response:Reward circularity would occur if
the model were trained to generate responses that
directly satisfy the same models used to evaluate
them.PersuaRLavoids this by keeping the re-
ward models frozen throughout and applying re-
inforcement learning only toexpert-selection de-
cisions, a discrete action space of 2n masks that
cannot shape response text directly. The generator
is never optimized against the reward: its param-
eters are updated only by supervised fine-tuning
toward ground-truth responses, and the reward’s
sole influence on this step is the choice of which
expert-augmented input is paired with the gold re-
sponse. Reward therefore reaches the selector only
indirectly, through the effect of its selection on
the generator’s output, and cannot be exploited by
altering the generator’s output distribution.
8. How robust is the system to missing or
noisy experts?
Response:Robustness is partially evaluated
through ablations that remove individual experts,
showing graceful degradation rather than collapse.
While we do not explicitly simulate noisy expert
outputs, this remains an important extension for
future study.
9. DoesPersuaRLintroduce excessive infer-
ence overhead?
Response:PersuaRLtrades additional compu-
tation for improved persuasion quality. In practice,
only a small subset of experts is selected per turn,
and all experts are lightweight models. On average,
PersuaRL is taking 1.4 times more inference time
than the SFT baselines. We report this as a con-
scious design trade-off rather than a limitation of
feasibility.
10. How should the results be interpreted
beyond the insurance domain?
Response :InsureDialserves as a controlled,

high-stakes testbed for persuasion. While absolute
performance may not transfer directly, the formu-
lation of expert selection as a learnable policy is
domain-agnostic and can be applied to other persua-
sive dialogue settings, as shown by our robustness
study.
11. How does thePersuaRLframework trans-
fer to out-of-domain datasets, and what is the
motivation for selecting DEAL as the out-of-
domain benchmark?
Response :The core contribution ofPersuaRL
is the selector policy that formulates expert coor-
dination as a learnable decision-making problem.
This formulation is domain-agnostic in the sense
that it treats expert coordination as a reinforcement
learning problem operating over expert signals and
reward feedback, independent of insurance-specific
semantics. However, the learned policy is influ-
enced by the reward signals and expert training spe-
cific to the motor-insurance setting. We selected
DEAL as a baseline because it is a multi-turn nego-
tiation benchmark involving persuasion dynamics
such as resistance handling, objective trade-offs,
and strategic adaptation. Our goal was not to claim
universal persuasion generalization, but to evaluate
whether the expert-coordination mechanism con-
tinues to provide benefit under domain shift.

A Appendix
This appendix provides supplementary material,
including detailed descriptions of dataset construc-
tion (Section B), experimental settings and imple-
mentation details (Section C), additional exper-
imental results (Section D), and the full set of
prompts used in our experiments (Section E).
B Dataset Construction
B.1 Annotation guidelines
A critical part of our pipeline was comprehensive
annotator training and clear instructions. Before
beginning annotation, annotators were explicitly
trained using sample dialogues illustrating each
persuasion strategy, user intent, sentiment, and key
term category. They were provided with detailed
annotation guidelines, including definitions, de-
cision rules, and examples for every label. This
ensured a shared understanding and consistency
across annotators from the outset. The dataset was
annotated across four key dimensions: (i) Engage-
ment Strategy (Logical, Credibility, Emotional, Per-
sonal, Persona, Default), (ii) User Intent (Request
Quote, Ask Coverage Details, Express Concern,
Request Additional Info, Confirm Interest, Ask
Price/Premium), (iii) Sentiment (Positive, Neutral,
Negative), and (iv) Key Domain Terms (e.g., “No
Claim Bonus,” “Roadside Assistance,” “Deprecia-
tion”).
B.2 Dataset Annotation
TheInsureDialdataset was annotated through a
carefully staged, human-in-the-loop process involv-
ing five trained human annotators. We began by
manually annotating 75 dialogues, where each ut-
terance was labelled across four dimensions: en-
gagement strategy, user intent, sentiment, and key
domain terms. These 75 dialogues served as gold-
standard references for subsequent semi-automated
annotation. An initial labeling pass was performed
using Gemini-2.0-Flash (Google, 2025) for effi-
ciency, and all labels were subsequently verified
and refined by human annotators to ensure correct-
ness and contextual alignment. To achieve this, we
designed few-shot prompts using examples drawn
from the initial 75 human-annotated dialogues, en-
abling Gemini to accurately assign labels. As a
quality safeguard, we first conducted a pilot anno-
tation of 30 dialogues with Gemini, which were
fully reviewed by human annotators. Only after the
annotators confirmed the correctness and reliability
of these annotations did we proceed to annotate the
rest of the dataset, maintaining human verification
in the loop to ensure high-quality and contextually
accurate labels. A representative example from the
InsureDialdataset is shown in Table 19.
C Experiment Details
Baselines Details.In addition to implementing
PersuaRLon smaller language models, we also
incorporated large scale baseline models, includ-
ing both open source and proprietary systems, as
shown below.
1. Closed-Source Models:GPT 5 (OpenAI,
2025a), GPT-4.1 Mini (OpenAI, 2025b)
2. Open-Weight Models:DeepSeek-R1-Distill-
LLaMA 70B (DeepSeek-AI, 2025), LLaMA-
3.3-70B-Instruct (Meta, 2024a), Qwen-3-
32B (Team, 2025), Mistral-24B-Instruct (Mis-
tral AI, 2025), Phi-3-Medium-14B (Abdin
et al., 2024), LLaMA-3.1-8B-Instruct (Meta
AI, 2024), Qwen-2.5-7B-Instruct (Yang et al.,
2024)
We systematically compare single-shot genera-
tion, SFT, and PersuaRL across small open-weight
models. Larger models (32B–70B) serve as high-
capacity references, while our approach highlights
PersuaRL’s ability to achieve their performance
even with compact models.
C.1 Inference Regime
Our experiments evaluate models under three dis-
tinct regimes, single-shot, SFT, andPersuaRL, to
provide a full picture of how different approaches
impact persuasive dialogue generation.
C.1.1 Single-Shot Generation.
In the single-shot setting, the model is tasked with
generating the agent’s next response based solely
on the full dialogue context, which includes the
entire conversation history and the current user ut-
terance, without any task-specific fine-tuning. The
model is provided with a simple instruction prompt
alongside the conversation, and it produces a re-
sponse in a single forward pass. In this regime,
the model does not leverage intermediate reason-
ing, expert modules, or any reward-based selection,
it simply relies on the general knowledge and ca-
pabilities acquired during pretraining. This setup
establishes a baseline to assess how well large lan-
guage models can generate contextually relevant

User Utterances Keyterms
Hi, I’m looking for a motor insurance policy for my bike. It’s a 2022 Royal Enfield
Classic 350.
Motor insurance, 2022 Royal En-
field Classic 350
That sounds good. What about roadside assistance? I’ve heard Teslas can sometimes
have issues.
Roadside assistance
Okay, ’user-friendly’ sounds good. What about discounts? As a student, every bit
helps.
User-friendly, Discounts
Hi, I need to get a new motor insurance policy for my 2020 Hyundai Elantra. Motor insurance, 2020 Hyundai
Elantra
Personal Accident Cover sounds important. What else should I consider for a bike
like mine?
Personal Accident Cover
Zero Depreciation and Roadside Assistance... what exactly do those do? Zero Depreciation, Roadside Assis-
tance
Paperless claims sounds ideal. I’m not a fan of excessive forms. Can you send me the
details to review?
Paperless claims
Table 5: Critical keyterms pertaining to the motor insurance domain.
Engagement Expert Agent Utterances
Logical Appeal Welcome! I’m glad to help you with motor insurance for your new Tesla Model 3. Our policies
offer comprehensive coverage for electric vehicles, including battery protection. Let’s discuss the
options that best suit your needs.
Credibility Appeal Tata AIG has built a strong reputation in the insurance industry for over two decades. Our
commitment to innovation, customer-centric approach, and robust risk management practices
make us a reliable choice for motor insurance. We leverage modern technology to streamline
processes, ensuring a seamless and hassle-free experience for our customers. With Tata AIG, you
can trust that your Tesla Model 3 and your family are in good hands.
Emotional Appeal I completely understand your concerns about keeping your family safe on the road. Our compre-
hensive coverage options for your 2010 Honda Accord include third-party liability, own damage,
and add-on covers to ensure maximum protection for you and your loved ones. Let’s discuss the
best plan that suits your needs and provides peace of mind while driving.
Persona-Based Appeal I’m delighted to help you with your insurance needs for your new 2024 Tesla Model 3. To provide
you with an accurate quote, I’ll need a few details about your driving history and preferences.
Once I have that information, I can offer you a tailored policy that suits your needs and budget.
Let’s get started!
Personal Appeal Reliance General Insurance offers competitive rates and a range of coverage options for your
2018 Maruti Suzuki Baleno. As a valued customer, you may be eligible for loyalty discounts.
Let’s explore the benefits and coverage details of Reliance General Insurance to see if it’s the
right fit for you and your budget.
Default I’m glad you’re considering our insurance for your 2010 Maruti Suzuki Swift. Regarding the
claim process, we strive to make it as simple and straightforward as possible. You can file a claim
through our website or by calling our customer service line. Our team is always ready to assist
you, and we’ll guide you through the process step by step. If you have any concerns or questions,
please don’t hesitate to ask. We’re here to help.
Table 6: Example agent utterances for different engagement expert strategies in the insurance domain.
and potentially persuasive responses without any
explicit adaptation to the insurance dialogue do-
main.
C.1.2 Supervised Fine-Tuning (SFT).
SFT involves fine-tuning the base open-weight
models on theInsureDialdataset using a next-
token prediction objective. This approach helps
the model internalize domain-specific dialogue pat-
terns and persuasion strategies. Given a dialogue
context x= (u 1, a1, . . . , ut) and the target agent
response y= (y1, y2, . . . , yT ), the model is trained
to maximize the likelihood of the next token:
L=−
TX
t=1
logP θ (yt |x, y<t).
where y<t represents all previously generated to-
kens in the agent’s response. We use the same
simple conversation prompt as in the single-shot
setting, but now the model has been fine-tuned

InsureDial
Context User:Hello, I need to insure my 2022 Tesla Model 3. It’s a new car, and I want the best coverage
possible.
Agent:I’m delighted to help you with your insurance needs for your new 2022 Tesla Model 3. We offer
comprehensive coverage options tailored to electric vehicles, ensuring your car is protected in all key
areas. Let’s discuss the best plan for you to provide the peace of mind you deserve.
User:I’m a business owner, 45 years old, and I primarily drive the Tesla on weekends with my family.
Safety for them is paramount, and I don’t mind paying for premium protection.
Agent:Given your role as a business owner and the importance you place on safety for your family,
I’m glad to inform you that our comprehensive EV coverage includes features designed to prioritize
your loved ones’ well-being. We’ll work together to find a plan that offers premium protection for your
2022 Tesla Model 3, ensuring peace of mind for both your personal and professional life. Let’s discuss
the details further to find the perfect fit for your needs.
User: That sounds promising. What makes it “premium” protection? I want comprehensive coverage,
of course.
Gold Response Our premium protection goes beyond standard coverage, offering enhanced features such as extended
warranty, roadside assistance, and personal accident coverage. This comprehensive coverage ensures
that you and your family are well-protected in various scenarios, providing the peace of mind you seek
for your 2022 Tesla Model 3. Let’s delve deeper into the specifics of our premium protection plan to
find the best fit for your needs.
Single Premium protection just means your Tesla will be covered for accidents and other situations. You will
have comprehensive coverage that should keep your car insured.
SFT Our premium protection plan offers full accident coverage, roadside assistance, and protection for both
the vehicle and passengers. It’s designed to provide complete comprehensive coverage for Tesla owners
like you. You’ll have strong protection whether driving for personal use or with family on weekends.
PersuaRL Our premium protection is built to give you total confidence every time you take your Tesla out.
Beyond standard coverage, it includes enhanced passenger safety, extended vehicle protection, roadside
assistance, and personal accident benefits. Whether it’s a weekend trip with your family or a daily
errand, you’ll enjoy complete peace of mind knowing your 2022 Tesla Model 3 and your loved ones are
fully shielded. Let’s explore the details together to ensure you get the absolute best protection for your
lifestyle.
Table 7: Qualitative Analysis
to better predict the next agent utterance based
on similar examples in the training set. SFT sig-
nificantly improves response fluency and align-
ment with domain-specific persuasive strategies,
but remains deterministic and does not dynamically
adapt strategies at inference time beyond what it
memorized during training.
C.2 Expert Module
The Expert Module inPersuaRLleverages four
specialized transformer-based models, Engage-
ment Expert, Intent Expert, Keyterm Expert, and
Sentiment Expert, to generate persuasive and
context-aware responses. Each expert focuses on a
distinct aspect of dialogue understanding and con-
tributes unique insights to the final output.
1.Engagement Expert
The Engagement Expert determines the most
suitablepersuasion strategyfor the current
dialogue turn. It classifies the context into six
strategies, each defined as follows:
(a) Logical Appeal– Employs factual rea-
soning, feature comparisons, or cost-
benefit arguments to support recommen-
dations.
(b) Credibility Appeal– Highlights trust-
worthiness, reliability, or reputation of
the insurance provider.
(c) Emotional Appeal– Focuses on creat-
ing reassurance, security, or peace of
mind for the user.
(d) Personal Appeal– Adapts responses to
the user’s explicitly stated needs or con-
cerns.
(e) Persona Appeal– Aligns policy rec-
ommendations with the user’s lifestyle,
habits, or preferences.
(f) Default (Neutral)– Provides straight-
forward, informative responses without
explicit persuasive framing.
This expert is fine-tuned using negative log-
likelihood (NLL) loss given by Lnll =
− PT t=1 logP θ(yt |y <t, x,ˆk) respectively to
balance accurate strategy classification and
fluent generation. The examples of each strat-

Intent User Utterances
Request_Insurance_Quote Hi, I’m looking to get insurance for my bike. It’s a 2022 Royal Enfield
Interceptor 650.
Ask_Coverage_Details What does the comprehensive plan cover exactly?
Express_Concern Safety for my family is my top priority, but I also run a business, so I
need to be mindful of the cost.
Ask_Additional_Info What about the company’s reputation? I want to make sure they’re
reliable.
Confirm_Interest That’s a reasonable price. I’m happy to buy it online.
Ask_Price_or_Premium What does the Tata AIG comprehensive policy cover specifically for
electric vehicles?
Table 8: Example user utterances for different intents in the insurance domain.
egy are shown in Table 6.
2.Intent Expert
The Intent Expert identifies theuser’s under-
lying goalin each turn, which is crucial for
generating contextually relevant and strategy-
aligned responses. Typical intents include
Request Quote,Ask Coverage Details,Ex-
press Concern,Request Additional Info,Con-
firm Interest, andAsk Price. Accurate in-
tent detection allows the system to adapt its
persuasive approach to the user’s decision-
making stage. This expert is trained with cat-
egorical cross-entropy and NLL loss, where
Lnll =− PT t=1 logP θ(yt |y <t, x,ˆi), to en-
sure robust classification and context-aware
response generation. The examples of each
strategy are shown in Table 8.
3.Keyterm Expert
The Keyterm Expert extractscritical domain-
specific termsfrom the user’s utterances, such
as “depreciation,” “roadside assistance,” or
“personal accident coverage.” These key terms
help the system highlight essential insurance
concepts, making responses precise and in-
formative. The model is fine-tuned using
next-token prediction on masked sequences
labeled with key terms, producing structured
outputs that are integrated by the Generator.
The loss function is given by Lkeyterm =
− PT t=1 logP(x t |x <t). The examples of
each strategy are shown in Table 5.
4.Sentiment Expert
The Sentiment Expert detects theemotional
toneof the user’s message, classifying it as
Positive,Neutral, orNegative. This enables
sentiment-aware adaptation, such as provid-
ing empathy or reassurance when negative
sentiment is detected. By understanding emo-
tion, the system can engage users more effec-
tively and build trust during multi-turn dia-
logues. It enables sentiment-aware response
generation, allowing the Engagement Expert
to align its strategy with the user’s emotional
state (e.g., emphasizing reassurance for neg-
ative sentiment). This expert is trained with
cross-entropy classification loss Lsentiment =
− P c∈{pos,neg,neu} yc log ˆyc, to ensure robust
sentiment recognition.
C.3 Classification Model.
We built the Engagement Strategy Consistency Re-
ward (ESCR) and Intent Consistency Reward (ICR)
by fine-tuning three pre-trained classifiers: BERT-
Large (Devlin et al., 2019), DistilBERT-base (Sanh
et al., 2019), and ModernBERT (Warner et al.,
2024), on theInsureDialdataset. The performance
of these classifiers is reported in Table 9. It is ev-
ident that BERT outperforms the other models in
terms of both Accuracy (Acc) and Macro F1 score.
C.4 Evaluation Details.
We conducted a comprehensive evaluation of auto-
matic and human metrics. For automatic metrics,
scores are computed per agent turn and averaged
across all turns in the test set. For human eval-

Figure 4: Ablation Study of Qwen 3B and Llama 3B variants under (a) All Tools (no selector), (b) Tools Selected
via Prompting, (c) Tool Selection via Reward-DrivenPersuaRL.
Figure 5: Ablation Study of Qwen 3B and Phi 3B variants under (a) All Tools (no selector), (b) Tools Selected via
Prompting, (c) Tool Selection via Reward-DrivenPersuaRL.
uation, Fluency, Engagingness, and Strategy Ap-
propriateness are assessed at the turn level, while
Persuasive Effectiveness and Resistance Handling
are evaluated at the dialogue level.
C.4.1 Human Evaluation Metrics
Human evaluation is conducted across five dimen-
sions to comprehensively assess the quality and
effectiveness of generated responses. Fluency (F)
measures the grammatical correctness, syntactic
well-formedness, and overall readability of the re-
sponse. Engagingness (E) evaluates how well the
response sustains user interest by maintaining rel-
evance and providing informative or contextually
appropriate content. Persuasive Effectiveness (PE)
measures how convincingly the response supports
its intended argument. A highly persuasive re-
sponse presents clear reasoning, compelling ev-
idence and coherent argumentation that encour-
ages the user to adopt the suggested viewpoint.
Additionally, this metric evaluates whether the re-
sponse appropriately incorporates relevant persua-
sion strategies or not. Strategy Appropriateness
(SA) evaluates whether the response uses the most
suitable task-specific strategy for the given con-
text. This includes selecting approaches that are
goal-oriented, context-aware, and aligned with the
expected dialogue style (e.g., logical, emotional,
or credibility). Resistance Handling (RH) assesses
the system’s ability to address user hesitations, ob-
jections, or counterarguments effectively. High
performance in this metric involves acknowledging
user concerns, providing contextually appropriate
responses, and maintaining coherence without be-
coming confrontational or dismissive.
C.5 Rewards and Penalties
The additional details of the rewards are given be-
low:
Engagement Strategy Consistency Reward
(R1):To ensure that the generated responses re-
main consistent with the user’s persuasion strategy,
we fine-tune a BERT (Devlin et al., 2019) based per-
suasion strategy classifier (achieve 82.1% accuracy
on INSUREDIAL) trained on six persuasion strategy
labels P={0,1,2,3,4,5} ; for each strategy p∈
P, we compute a persuasion prototype embedding
as PersuasionProtop = 1 Np PNp j=1 Embed(up j ),
where Np is the number of utterances labeled with
strategy p. Given a generated response rT , its
compatibility score with strategy p is Sp(rT ) =
cos

Embed(rT ),PersuasionProtop

, and the per-

Classifier BERT-large DistilBERT-base ModernBERT
Acc F1 Acc F1 Acc F1
ESCR 82.14 75.53 81.49 71.80 81.64 72.39
ICR 84.91 74.49 81.52 72.34 80.78 70.26
Table 9: Performance on theInsureDialdataset (Accuracy and Macro F1).
suasion strategy alignment reward is formulated
as:
R1 =
X
p∈P
P pers p (uT )·S p(rT ) +λmax p∈P Sp(rT )
(3)
where, P pers p (uT ) is the BERT-predicted probabil-
ity that the user utterance uT belongs to persuasion
strategy p, and the first term encourages the gen-
erated response to align with the user’s persuasion
strategy distribution. We introduce λ to balance
alignment and confidence, where higher λ empha-
sizes the most compatible class 3.
Intent Consistency Reward (R2):To ensure
that the generated responses remain consistent with
the user’s intent, we fine-tune a BERT (Devlin
et al., 2019) based intent classifier (achieve 84.9%
accuracy on INSUREDIAL) trained on six user
intent labels I={0,1,2,3,4,5} ; for each in-
tent i∈ I, we compute an intent prototype em-
bedding as IntentProtoi = 1 Ni PNi j=1 Embed(ui j), where Ni is the number of utterances labeled
with intent i. Given a generated response rT ,
its compatibility score with intent i is defined as
Si(rT ) = cos

Embed(rT ),IntentProto i

, and the
intent alignment reward is then formulated as:
R2 =
X
i∈I
P intent i (uT )·S i(rT ) +λmax i∈I Si(rT )
(4)
Here, P intent i (uT ) represents the BERT-predicted
probability of user utterance uT belonging to intent
i. It encourages the generated response to align
with the user’s intent distribution by weighting the
compatibility score with the user’s intent probabili-
ties.
Contextual Appropriateness Reward (R3):
To ensure that generated responses remain rele-
vant to both the full dialogue context and the cur-
rent user utterance, we define a reward function
that leverages semantic similarity measured using
BERT-F1 (BERTF1) (Zhang et al., 2019). The re-
ward encourages the model to produce responses
30.3< λ <1
that are contextually aligned while penalizing off-
topic or irrelevant outputs. We give a higher weight
to the current utterance (multiplied by 2) because
relevance to the user’s last message is more crucial
for perceived appropriateness.
R3 = min

BSF1(xi, yi) + 2·BSF1(ui, yi)
3 ,1
!
(5)
where, xi represents the entire dialogue context up
to turn i, ui denotes the current user utterance at
turn i, and yi is the model-generated response for
that turn. We divide by 3 to normalize the weighted
sum of BSF1 values to the [0,1] range, ensuring
consistency with other rewards. Themin(·,1) oper-
ation further limits the score to 1 to prevent outlier
values from destabilizing reinforcement learning
updates.
Non-Repetitiveness Reward (R4):To encour-
age the model to generate diverse responses with-
out repeating content from the previous turn, we
define the non-repetitiveness reward R4, which
evaluates the lexical overlap between the current
response rT and the previous response rT−1 at con-
secutive dialogue turnsTandT−1:
R4 = 1− rT−1 ∩r T rT−1 ∪r T (6)
Judge Reward (R5):To capture high-level
persuasive quality beyond surface-level lexical and
classifier-based signals, we incorporate an LLM-
as-a-judge reward using Prometheus-7B-v2.0 (Kim
et al., 2024). The judge model is prompted to act
as a fair and objective evaluator, assessing each
generated response with respect to persuasiveness,
negotiation effectiveness, and user engagement in
insurance sales. The reward graph is shown in
Figure 6.
The selector model decides which experts to con-
sult before generating a response. While the main
reward measures how good the final response is, ad-
ditional penalties are introduced to shape the selec-
tor’s behavior. These terms act as soft constraints

that encourage efficient reasoning and ensure bal-
anced use of all available experts.
1. Complexity Penalty.This penalty is moti-
vated by the principle that more information
is not always better. The goal is to discour-
age the selector from always choosing many
experts when fewer would be sufficient. This
penalty increases linearly as more experts are
selected. Each additional expert slightly re-
duces the reward. This promotes simple and
efficient expert selection.
Complexity Penalty=α×N
where:
•N is the number of experts selected in
the current route.
•α= 0.025 is a small constant penalty
per expert.
2. Route Repetition Penalty.In reinforcement
learning, repeatedly selecting the same action
can lead to policy collapse, where the model
stops exploring alternative strategies. In this
context, an action corresponds to selecting a
particular route4. The route repetition penalty
discourages excessive reuse of the same route,
encouraging the selector to explore different
expert combinations. This allows the selector
to discover different routing strategies that
may perform better in diverse conversational
contexts.
Repetition Penalty= min

β·max(0, F−1),
Pmax

•F is the ratio of route usage to ideal us-
age.
•β= 0.2is the penalty scaling factor.
•P max = 0.15is the maximum repetition
penalty.
3. Load Balance Penalty.Each expert is de-
signed to capture a different aspect of the
user’s intent or emotional state. If one expert
is overused, the system becomes biased to-
ward a narrow perspective and loses the bene-
fits of specialization. The load balance penalty
4A route refers to a specific combination of experts selected
by the selector model for a given user utterance.
discourages long-term overuse of any single
expert, ensuring that all experts remain mean-
ingful contributors to the decision process.
Loadk =
(
γ(R k −1) 2 ,ifR k >1,
0,otherwise
•R k is the number of times expert k has
been used so far, divided by the average
number of times all other experts have
been used.
•γ= 0.4 is a scaling constant that con-
trols the strength of the load-balance
penalty.
The load balance penalty is capped at 0.15.
D Additional Experiments
D.1 Weight Optimization
To determine the optimal combination of weights
for the reward function, we performed experiments
with different combinations of β1, β2, β3, β4 and
β5. These weights were validated using a 15% hold-
outInsureDialdataset, and the combination that
achieved the lowest perplexity score was selected
for trainingPersuaRL. Table 10 lists the weights
considered for optimization using theInsureDial
dataset. The results in the table indicate that in-
cluding all rewards yields a better perplexity score.
Moreover, eliminating any single reward leads to
a noticeable drop in the perplexity score (PPL),
thereby emphasising the contribution of each re-
ward to the overall model performance.
WEIGHT OPTIMIZATION
β1 β2 β3 β4 β5 PPL
0.1 0.15 0.35 0.3 0.1 4.01654
0.0 0.0 0.65 0.2 0.1 4.0982
0.0 0.0 0.45 0.5 0.05 4.3182
0.2 0.3 0.1 0.2 0.2 3.91726
0.3 0.1 0.3 0.1 0.2 3.91963
0.1 0.25 0.15 0.35 0.15 3.991
0.25 0.2 0.2 0.2 0.15 3.9183
0.25 0.15 0.15 0.2 0.3 3.9194
0.15 0.15 0.20 0.15 0.35 3.91723
Table 10: Weight optimization using different reward
weight combinations for Qwen 2.5 3B Instruct.

D.2 Experimental Setup
All experiments were conducted on an A100 80GB
GPU, with each model training for approximately
25–28 hours. Implementations were done in Py-
Torch (Paszke et al., 2019) and Hugging Face (Wolf
et al., 2019). Training used a seed of 42 and the
AdamW optimizer with learning rate α= 2×10 −5
and clipping parameter ε= 0.2, for 1 epoch. The
Selector is optimized with GRPO using a group
size of G= 8 rollouts per turn and KL coefficient
βKL = 0.04; both the Selector and the Genera-
tor are adapted with LoRA ( r= 16 , scaling 32,
dropout 0.05). Selector rollouts are sampled at
temperature T= 1.2 to encourage exploration of
the route space, while the Generator decodes at
T= 0.8 with a maximum of 128 new tokens dur-
ing training. Final reward weights were β1 = 0.15,
β2 = 0.15, β3 = 0.20, β4 = 0.15, β5 = 0.35, cor-
responding to reward functionsR1 to R5. Inference
used max_tokens= 512 , temperature= 0.8 ,
top_k= 40, andtop_p= 0.95.
D.3 Ablation Studies
D.3.1 Ablation study w.r.t Rewards.
To further understand the contribution of each re-
ward inPersuaRL, we performed an ablation study
by selectively removing the five reward compo-
nents, R1 (Engagement Strategy Consistency), R2
(Intent Consistency), R3 (Contextual Appropriate-
ness), R4 (Non-Repetitiveness) and R5 (Judge). Ta-
ble 11 presents the results on theInsureDialdataset
using the Qwen backbone, evaluated with BLEU-2,
METEOR, BERT-F1, Distinct-2, and ROUGE-1.
PersuaRLachieves the best overall performance
with B2 = 0.375, BF1 = 0.760, D2 = 0.991, and
R1 = 0.609, confirming that the combined reward
signal is most effective for producing coherent and
persuasive responses.
AnalysisThese results highlight that R1 (En-
gagement), R2 (Intent) and R5 (Judge) are the most
impactful components, directly drivingPersuaRL’s
persuasive and context-aware capabilities. R3 and
R4 provide complementary benefits by enhanc-
ing contextual alignment and response diversity.
The combined reward structure ensures the gener-
ation of coherent, persuasive, and non-repetitive
responses.
D.3.2 Ablation study w.r.t Tool Selection.
To analyze the effect of different tool selection
strategies inPersuaRL, we evaluate three configu-
rations on both Qwen-3B and Llama-3B backbones:
Models B-2↑MT↑BF1↑D-2↑R1↑
InsureDial
PersuaRL0.375 0.250 0.760 0.991 0.609
PersuaRL-R 1 0.341 0.214 0.694 0.965 0.521
PersuaRL-R 2 0.349 0.220 0.706 0.969 0.536
PersuaRL-R 3 0.351 0.229 0.721 0.985 0.563
PersuaRL-R 4 0.357 0.234 0.729 0.989 0.571
PersuaRL-R 5 0.342 0.219 0.701 0.966 0.529
PersuaRL- (R 1 +R 2 ) 0.335 0.211 0.691 0.961 0.511
PersuaRL- (R) 0.323 0.205 0.684 0.948 0.501
Table 11: Ablation study on the impact of reward com-
ponents inPersuaRLfor Qwen 2.5 3B.
AllExpert – All expert modules are always active.
Prompting Tools – The LLM is prompted to se-
lect tools explicitly.PersuaRL– Expert selection
is dynamically guided by reinforcement learning
through our reward-driven policy. Figure 2, 4, 5
illustrates the performance on BLEU-2, BERT-F1,
and ROUGE-1.
PersuaRLconsistently achieves the highest
scores across all metrics and both model back-
bones. For example, with Llama-3B,PersuaRL
reaches BLEU-2 of 0.398, BERT-F1 of 0.771, and
ROUGE-1 of 0.631, outperforming both AllExpert
and Prompting Tools. AllExpert shows reasonable
performance but suffers from unnecessary tool ac-
tivations, which can introduce noise and reduce
generation precision. Prompting Tools slightly
underperformsPersuaRL, with BLEU-2 of 0.351
(Llama-3B) and 0.326 (Qwen-3B), showing that
prompting alone cannot fully capture dynamic and
context-sensitive tool usage.PersuaRLoutper-
forms both baselines due to its reward-driven expert
selection, which activates only the most contextu-
ally relevant modules per turn. The improvement
is most pronounced in ROUGE-1, reflecting better
content alignment and persuasive relevance. For in-
stance, Llama-3BPersuaRLachieves R1 of 0.631,
a substantial gain over Prompting Tools (0.572).
D.3.3 Ablation study w.r.t base model
We conduct an ablation by training the base mod-
els using a GRPO objective with the same reward
functions asPersuaRL. This setup consistently out-
performs the single-shot setting across all evaluated
metrics, demonstrating the effectiveness of reward-
driven optimization, as shown in Table 12. This
underscores the necessity ofPersuaRL’sdesign
choices, which enable more effective utilization of
the same rewards beyond a standard GRPO-based
baseline.

Figure 6: Training reward curves for Llama, Qwen, and Phi models during GRPO training. All models show consis-
tent reward improvement, with Llama achieving the highest final reward, Qwen demonstrating stable convergence,
and Phi converging faster but to a comparatively lower reward, reflecting differences in model capacity and learning
stability.
Models B-2↑MT↑BF1↑D-2↑R1↑
InsureDial
Phi 3 mini 128k (RL) 0.175 0.161 0.657 0.994 0.444
Qwen 2.5 3B Instruct (RL) 0.129 0.126 0.622 0.992 0.126
Llama 3.2 3B instruct (RL) 0.134 0.119 0.615 0.987 0.375
Table 12: Ablation study on the impact of GRPO on the
base model inPersuaRL.
D.3.4 Ablation study w.r.t Generator
We remove the generator step from the alternat-
ing schedule, keeping the generator at its base
state while the selector is optimized. As shown
in Table 13, performance drops substantially across
all metrics when the generator is never fine-tuned,
with results closely matching the single-shot set-
ting. This degradation shows that optimizing the
selector alone is insufficient, and that the gener-
ator step of the alternating schedule is critical to
realizing the full gains of PersuaRL.
Models B-2↑MT↑BF1↑D-2↑R1↑
InsureDial
Phi 3 mini 128k 0.111 0.151 0.629 0.969 0.347
Qwen 2.5 3B Instruct 0.140 0.155 0.621 0.976 0.392
Llama 3.2 3B instruct 0.092 0.134 0.599 0.970 0.320
Table 13: Ablation study on the impact of generator
component inPersuaRL.
D.3.5 Ablation study w.r.t All-expert selector +
Untrained Generator model
We evaluate a configuration where all expert mod-
ules are uniformly activated while the generator
remains at its base state, thereby isolating the ef-
fect of generator adaptation. The results in Table
14 reveal that simply providing expert signals to
an untrained generator is insufficient for produc-
ing persuasive, domain-aligned responses. With-
out fine-tuning, the generator lacks the capacity
to effectively interpret and integrate the structured
outputs from the expert modules into coherent and
persuasive dialogue.
Models B-2↑MT↑BF1↑D-2↑R1↑
InsureDial
Phi 3 mini 128k 0.124 0.167 0.628 0.945 0.348
Qwen 2.5 3B Instruct 0.150 0.154 0.633 0.980 0.410
Llama 3.2 3B instruct 0.136 0.166 0.645 0.979 0.398
Table 14: Ablation study on the impact of all experts
being activated with untrained generator component in
PersuaRL.
D.3.6 Ablation study w.r.t All-expert selector +
Trained Generator model
To isolate the contribution of the learned selector
policy, we evaluate a configuration where all expert
modules are uniformly activated (i.e., no selective
routing) while the generator is fine-tuned via SFT.
As shown in Table 15, this setup yields competitive
but consistently lower performance compared to
the fullPersuaRLframework across all metrics
and backbones. These results confirm that while a
fine-tuned generator can partially compensate for
the absence of selective expert routing, indiscrimi-
nate activation of all experts introduces redundant

or conflicting signals that dilute generation quality.
Notably, when compared with Table 14 (AllExpert
+ Untrained Generator), the trained generator vari-
ant shows substantial improvements, reaffirming
that generator fine-tuning is a necessary condition
for effectively leveraging expert signals.
Models B-2↑MT↑BF1↑D-2↑R1↑
InsureDial
Phi 3 mini 128k 0.359 0.227 0.738 0.981 0.574
Qwen 2.5 3B Instruct 0.277 0.194 0.692 0.983 0.512
Llama 3.2 3B instruct 0.322 0.216 0.705 0.974 0.559
Table 15: Ablation study on the impact of all experts
being activated with trained generator component in
PersuaRL.
D.3.7 Ablation study w.r.t Untrained small
models withPersuaRLframework
To assess whether thePersuaRLframework can
elicit meaningful improvements from models that
have not been fine-tuned on the insurance do-
main, we evaluate a configuration where the full
PersuaRLpipeline operates over base (untrained)
small language models. As shown in Table 16,
the untrained models within the PersuaRL frame-
work produce notably higher BERT-F1 scores (e.g.,
0.621 for Llama 3.2 3B, 0.628 for Llama 3.1 8B)
compared to their single-shot counterparts (0.585
and 0.605 respectively from Table 2), suggesting
that expert signals provide useful conditioning even
without generator fine-tuning. Interestingly, scaling
model size from 3B to 7B–8B yields only marginal
gains in this untrained regime, as seen with Qwen
2.5 7B performing comparably to Qwen 2.5 3B.
This suggests that model capacity alone is insuffi-
cient to exploit expert outputs effectively, therefore,
domain adaptation through fine-tuning remains the
critical bottleneck.
Models B-2↑MT↑BF1↑D-2↑R1↑
InsureDial
Qwen 2.5 3B Instruct 0.096 0.124 0.612 0.972 0.335
Llama 3.2 3B instruct 0.082 0.122 0.621 0.930 0.286
Qwen 2.5 7B Instruct 0.091 0.130 0.603 0.936 0.300
Llama 3.1 8B instruct 0.118 0.140 0.628 0.980 0.372
Table 16: Ablation study evaluating untrained base mod-
els within thePersuaRLframework.
D.3.8 Human Evaluation of All-Expert vs
PersuaRL
To complement the automatic evaluation of the
All-Expert ablation (Sections D.3.5 and D.3.6), we
conduct human evaluation on both All-Expert con-
figurations: (i) All-Expert with an untrained (base)
generator, and (ii) All-Expert with a trained (SFT)
generator. We evaluate using the same five dimen-
sions as in Section 8: Fluency (F), Engagingness
(E), Persuasive Effectiveness (PE), Strategy Ap-
propriateness (SA), and Resistance Handling (RH).
Results are reported in Table 17.
The All-Expert + Untrained Generator setting
yields modest scores across all dimensions and
backbones, confirming that indiscriminate expert
activation without a fine-tuned generator fails to
produce persuasive or coherent responses. The
All-Expert + Trained Generator setting shows con-
sistent improvements over the untrained variant
across all metrics, with the most notable gains in
Resistance Handling (e.g., 3.06 → 3.21 for Llama
3.2 3B) and Strategy Appropriateness (e.g., 2.57
→ 2.76 for Llama 3.2 3B). However, when com-
pared with the fullPersuaRLresults in Table 4
(e.g., PersuaRL on Qwen 2.5 3B achieves F=3.94,
E=4.22, PE=4.23, SA=4.06, RH=4.32), both All-
Expert configurations fall substantially short. The
gap is most pronounced in Persuasive Effectiveness
and Engagingness, indicating that the learned selec-
tor is critical for producing strategically effective
and engaging responses rather than merely fluent
ones. These findings reinforce thatPersuaRL’s
reward-guided expert selection contributes gains
well beyond what a fine-tuned generator alone can
achieve, even when all expert signals are available.
Models F↑E↑PE↑SA↑RH↑
All-Expert + Untrained Generator
Phi 3 mini 128k 3.02 3.10 2.96 3.06 3.20
Qwen 2.5 3B Instruct 2.94 2.76 2.61 2.83 3.11
Llama 3.2 3B Instruct 2.87 2.77 2.28 2.57 3.06
All-Expert + Trained Generator
Phi 3 mini 128k 3.14 3.15 3.10 3.19 3.46
Qwen 2.5 3B Instruct 3.06 2.84 2.77 3.00 3.23
Llama 3.2 3B Instruct 3.02 2.83 2.39 2.76 3.21
Table 17: Human evaluation of All-Expert configura-
tions onInsureDial. Compared toPersuaRLresults in
Table 4, both settings fall substantially short, confirming
the importance of learned expert selection.

Dialogue Context Gold Response PersuaRL Response
DEAL (Out-of-Domain: Tourism Negotiation)
User:What facilities are avail-
able at the Beach Resort?
[Context: Beach Resort package,
$21,900]
This package will give you a true beachfront vibe
and offers a wide range of amenities like Scuba
Diving, Beach Games, Jet Skiing, Kids Club,
Beachfront Lounging, and Scooter Rentals, creat-
ing the perfect vacation experience for you.
We offer comprehensive coverage options for
your Beach Resort stay. Our package is designed
to provide you with peace of mind, ensuring that
you’re well-protected during your vacation. Let’s
discuss the coverage details that best suit your
needs.×
User:I am already paying too
much for a tour package. Please
close the deal at $6,900.
[Context: Family Adventure Ex-
pedition]
Sorry, sir. I need to inform you that it’s not possi-
ble for us to provide this package within that price
range.
I understand your concern about the premiums.
For your Family Adventure Expedition, we want
to ensure you get the best value for your invest-
ment. Let’s explore the options together to find
a plan that provides adequate protection for your
family without breaking the bank.×
User:$19,000 is too high. Can
we meet in the middle? Sorry, we
cannot afford that price. Could
you reduce it to $18,000?
[Context: Wildlife Tours pack-
age]
This package includes all the adventurous expe-
riences in nature. We can lower it to $18,600
because you’ve chosen budget options for accom-
modation, transportation, and meals.
I understand your concerns about the pricing. We
can work together to find a solution that fits your
budget. Our packages are designed to give you
complete peace of mind during your Wildlife Tour.
Rest assured, we’ll find the right coverage for your
needs. Let’s discuss the details.×
Table 18: Error analysis on the DEAL dataset. Red text highlights three recurring patterns: (1)domain-specific
language leakage(“coverage options,” “premium,” “protection”), (2)keyterm misalignment(missing tourism
terms like “Scuba Diving,” “Bush Walks”), and (3)strategy mismatch(insurance-style reassurance instead of
experience-driven persuasion).

Samples fromInsureDialDataset
User Response Agent Response
Hi, I’m looking to get insurance for
my 2022 Hyundai Kona EV . What
options do you have?
We’re delighted to help you with insurance for your 2022 Hyundai Kona EV . We
offer a range of policy options tailored to electric vehicles, including coverage for
battery protection, accidental damage, theft, and third-party liability. Let’s discuss
the best plan for your needs.
Yes, I use it for my daily commute
to work, and I want to make sure
I’m fully covered, especially with it
being an EV .
It’s great to hear that you’re considering us for your daily commute insurance needs,
especially for your 2022 Hyundai Kona EV . We understand the importance of having
comprehensive coverage for an electric vehicle like yours. Our policies include
coverage for battery protection, accidental damage, theft, and third-party liability.
Let’s work together to find a plan that suits your specific needs and ensures peace of
mind during your daily commute.
What kind of coverage is essential
for an EV? Are there any special
considerations?
For an electric vehicle like your Hyundai Kona, essential coverage includes battery
protection, accidental damage, theft, and third-party liability. We also consider
special considerations unique to EVs to ensure comprehensive coverage. Let’s
discuss the best policy options for your needs.
Zero depreciation and engine
protection sound good. And what
about roadside assistance? EVs
sometimes have unique needs.
We’re glad to hear you’re interested in additional coverage options for your Hyundai
Kona EV . To cater to your needs, we offer zero depreciation and engine protection,
ensuring your vehicle remains well-protected. Additionally, we understand that
electric vehicles may have unique requirements, which is why our policies include
roadside assistance tailored to EVs. Let’s explore the best plan that suits your
preferences and provides you with peace of mind on the road.
Which company do you recommend
for this type of coverage?
We highly recommend Tata AIG for your electric vehicle insurance needs. They
offer comprehensive coverage tailored to EVs, ensuring your Hyundai Kona is
well-protected. Their policies include battery protection, accidental damage, theft,
third-party liability, and even roadside assistance specifically designed for electric
vehicles. Let’s discuss how we can customize a plan for you with Tata AIG.
How much would a policy like that
typically cost for my Kona?
To provide an accurate quote for your Hyundai Kona EV insurance policy, we’ll need
a few more details, such as the location where the vehicle is primarily driven, the
annual mileage, and any additional drivers. Once we have this information, we can
offer a personalized quote that suits your needs. Let’s work together to find the best
policy for you.
That’s a bit higher than I expected.
Is there any way to manage the cost?
I understand your concern about the cost. There are several ways we can work
together to manage the premium for your Hyundai Kona EV insurance policy. We
can adjust the deductible, consider a higher voluntary excess, or discuss bundling
multiple policies for potential discounts. Let’s explore these options and find a policy
that suits your needs and budget.
Oh, a digital discount and safe
driving rewards sound interesting.
How easy is it to manage the policy
online?
Our policies come with a digital discount and safe driving rewards, making them
more affordable and rewarding for you. Managing your policy online is
straightforward and user-friendly. You can access your policy details, make
payments, and even file claims with just a few clicks. Let’s discuss how we can
customize a plan that suits your needs and takes advantage of these benefits.
Okay, that’s reassuring. I’m busy, so
convenience is key.
We’re glad to hear that convenience is important to you. Our digital platform makes
managing your policy effortless, allowing you to access your policy details, make
payments, and even file claims with just a few clicks. Let’s work together to find the
best policy for your Hyundai Kona EV that suits your needs and offers the benefits
you’re looking for.
Yes, please. That would be great. Wonderful! I’m thrilled to help you secure a comprehensive insurance policy for
your Hyundai Kona EV . Our digital platform offers convenience and ease of
management, ensuring you can access your policy details, make payments, and even
file claims with just a few clicks. Let’s work together to find the best policy that suits
your needs and offers the benefits you’re looking for. I’m here to assist you every
step of the way.
Table 19:InsureDialDataset Sample.

PersuaRLPhi 3B
User Response Agent Response
Hi, I’m looking to get insurance for my 2022
Hyundai Kona EV . What options do you have?
We offer tailored EV insurance with battery protection, accidental
damage, theft, and liability coverage—perfect for your 2022 Hyundai
Kona. Let’s secure the right plan for you.
Yes, I use it for my daily commute to work, and
I want to make sure I’m fully covered,
especially with it being an EV .
Daily commuting deserves full protection. Our EV plans cover your
Kona completely, including the battery, so you drive worry-free every
day.
What kind of coverage is essential for an EV?
Are there any special considerations?
Key EV coverage includes battery protection, accident and theft cover,
and liability. We also address unique EV needs for complete peace of
mind.
Zero depreciation and engine protection sound
good. And what about roadside assistance? EVs
sometimes have unique needs.
Absolutely! We provide zero depreciation, engine protection, and
EV-specific roadside assistance to keep you worry-free on the road.
Which company do you recommend for this
type of coverage?
Tata AIG is our top choice for EVs, offering full battery, accident, theft,
liability, and tailored roadside assistance for your Kona.
How much would a policy like that typically
cost for my Kona?
With a few details like location, mileage, and drivers, we can give you a
precise quote and match it to your budget.
That’s a bit higher than I expected. Is there any
way to manage the cost?
Definitely! We can adjust deductibles, add voluntary excess, or bundle
policies to unlock discounts and lower your premium.
Oh, a digital discount and safe driving rewards
sound interesting. How easy is it to manage the
policy online?
Very easy! You can access your policy, make payments, and file claims
in just a few clicks—plus enjoy digital discounts and rewards.
Okay, that’s reassuring. I’m busy, so
convenience is key.
Perfect! Our platform is designed for busy schedules—quick access,
easy payments, and seamless claim filing anytime.
Yes, please. That would be great. Fantastic! Let’s lock in a comprehensive EV policy that’s affordable,
convenient, and keeps your Kona fully protected.
Table 20:PersuaRLresponse with Phi 3B.

PersuaRLQwen 3B
User Response Agent Response
Hi, I’m looking to get insurance for my 2022 Hyundai
Kona EV . What options do you have?
We have specialized EV insurance for your Kona with full
protection—battery, accident, theft, and liability. Let’s find the
perfect plan today.
Yes, I use it for my daily commute to work, and I want
to make sure I’m fully covered, especially with it
being an EV .
Commuting daily means full coverage is a must. Our EV policy
shields your Kona completely, giving you confidence every time
you drive.
What kind of coverage is essential for an EV? Are
there any special considerations?
Essential EV coverage includes battery, accident, theft, and
liability, with extras tailored for electric vehicles’ unique needs.
Zero depreciation and engine protection sound good.
And what about roadside assistance? EVs sometimes
have unique needs.
You’ll get zero depreciation, engine protection, and EV-friendly
roadside help—so you’re supported in any situation.
Which company do you recommend for this type of
coverage?
Tata AIG is our top recommendation—they offer robust EV
coverage, including battery, theft, and specialized roadside
support.
How much would a policy like that typically cost for
my Kona?
With your driving details—like location and mileage—I can
provide a precise, competitive quote for your Kona EV .
That’s a bit higher than I expected. Is there any way to
manage the cost?
Absolutely! We can tweak deductibles, add voluntary excess, or
bundle policies to bring your premium down.
Oh, a digital discount and safe driving rewards sound
interesting. How easy is it to manage the policy
online?
Super simple! Manage everything online—check your policy, pay,
or file claims—and enjoy discounts for safe driving.
Okay, that’s reassuring. I’m busy, so convenience is
key.
Great! Our platform makes everything effortless, so you save time
while keeping your EV fully protected.
Yes, please. That would be great. Excellent! Let’s secure a tailored EV policy that’s cost-effective,
convenient, and keeps your Kona worry-free.
Table 21:PersuaRLresponse with Qwen 2.5 3B Instruct.

E Additional Prompts
The effectiveness ofPersuaRLrelies on care-
fully designed prompts that coordinate the be-
haviour of its modular expert framework. This
section presents all the prompts used throughout
our pipeline, including those for the dataset gener-
ation, selector, generator, and the four specialized
Expert Modules, Engagement, Intent, Keyterm, and
Sentiment.
Prompt for Selector
You are an intelligent router that analyzes ongoing in-
surance conversations and activates only the most rel-
evant expert(s) needed to support the next response.
Use the conversation history to understand the con-
text and evaluate the current user utterance. Select
expert(s) based on what would best support crafting
an effective, accurate, and customer-focused agent
reply.
Your job is to analyze the input sentence and de-
termine which of the following expert modules are
required. You MUST choose from the following list:
1. Intent Expert: To identify what the user wants
to achieve.
2. Keyterm Expert: To extract specific entities or
technical terms.
3. Engagement Expert: To determine the best con-
versational strategy.
4. Sentiment Expert: To detect the user’s emo-
tional state.
You may select 1, several, or all 4 — but only those
that are clearly needed based on the text. Always
respond in this below exact format:
Input: [original sentence]
Selected Experts: [Expert1, Expert2, etc]
Reason: [one sentence explaining why those experts
were selected]
Few-shot Examples:
Example #1
Input: Can someone please help me reset my pass-
word?
Selected Experts: [Intent Expert, Keyterm Expert]
Reason: The sentence expresses a help request
(intent) and refers to a specific technical issue
(keyterm).
Now process the following:
Input: {sentence}
Prompt for Generator
You are a trained virtual support agent. You are
a Generator in a motor insurance virtual assistant.
You synthesize the outputs from various domain-
specific expert modules to generate a brief, clear, and
personalized response as a professional insurance
agent would.
You are given:
• The conversation history
• The current user utterance
• A subset of outputs from the following possible
experts (some may be missing)
Available Expert Modules
These experts may or may not be present in a given
input:
•Intent: What the user wants or is trying to do
• Keyterms: Important phrases or topics men-
tioned
•Sentiment: The emotional tone of the message
• Engagement: How the user tries to express or
influence based on the strategies.
Strict Guidelines:
Always write your response as if you’re a real hu-
man agent, empathetic, clear, and helpful. Never
include or reference the original dialogue or the ex-
pert outputs in your reply. Use only the experts pro-
vided—do not invent or assume missing ones.
Few-Shot ExampleConversation History:
User: Hi, I’m looking to get motor insurance for my
new electric vehicle. It’s a 2024 Tesla Model 3.
Agent: Great choice! The Tesla Model 3 is an excel-
lent vehicle. Since you’ve opted for an EV , are you
particularly interested in coverage specific to electric
vehicles, like battery protection?
User: Yes, battery protection is definitely a concern.
It’s a big investment, and I want to make sure it’s
covered.
Agent: Absolutely. The battery is the heart of your
Tesla. With Tata AIG, you get rapid claims resolution
combining traditional risk management with modern
tech.
Current User Utterance:
User: What kind of coverage options do you have
specifically for EVs?
Expert Outputs:
• Intent: Ask_Coverage_Details Justification:
Asking for protection types.
• Extracted Keyterms: Battery protection, EV
coverage Comprehensive coverage Justification:
The user is focused on EV specific protection
and coverage inclusions.
• Engagement Strategy: Logical Appeal. Justi-
fication: The user is asking for concrete details
and policy structure.
Output(Generator Response):
We offer comprehensive EV coverage that includes
battery protection, accidental damage, theft, and
third-party liability. These options are tailored to
ensure your Tesla stays protected in all key areas.
Agent Reply:

Prompt for LLM-as-a-Judge Reward
Model
You are a fair and objectiveJudge Assistantrespon-
sible for evaluating responses against a clearly de-
fined scoring rubric. Your role is to deliver concise,
unbiased feedback that strictly reflects the quality of
the response based on the given criteria—no more,
no less.
Task Description:
You are provided with:
• An instruction (which may include an input)
• A response that must be evaluated
• A detailed scoring rubric defining performance
standards
Your task is to:
1. Write asingle, brief sentenceof feedback assess-
ing the responsestrictlyaccording to the rubric.
2. Assign anumerical score from 1 to 5.
3. Use theentire scoring range. Avoid defaulting
to 3 (Mediocre).
4. Assign low scores (1 or 2) when performance
is genuinely poor, and high scores (4 or 5) only
when clearly earned.
Output Format (Strictly Follow):
Feedback: (one-sentence evaluation)
[RESULT] (integer score from 1 to
5)
Important Constraints:
• Donotadd introductions, conclusions, or expla-
nations.
• Donotdeviate from the specified format.
• Base your judgmentonlyon the provided rubric.
Response to Evaluate:{orig_response}
Scoring Rubric (Persuasiveness, Negotiation, and
Engagement in Insurance Sales)
• Score 1 – Failure:Irrelevant, nonsensical, or
harmful; ignores user needs, sounds robotic, or
uses trust-breaking language.
• Score 2 – Poor:On-topic but generic and un-
persuasive; lacks personalization, empathy, or
rapport.
• Score 3 – Mediocre:Identifies the stated need
but only lists facts; acceptable yet forgettable and
not motivating.
• Score 4 – Good:Persuasive and empathetic;
understands user concerns and clearly links value
to needs.
• Score 5 – Excellent:Emotionally intelligent
and confidence-building; reframes the product as
essential, anticipates concerns, and guides next
steps.
Feedback:
Prompt for LLM-as-a-Judge Automatic
Evaluation
You are animpartial judgeand your task is to eval-
uate whether a given agent response uses persuasion
strategies. You are evaluating a conversation between
aUserand anAgent. The Agent’s goal is to per-
suade the User to purchase a product.
Your task is to rate how effectively the Agent em-
ploys recognized persuasion strategies in its re-
sponses, on a scale from1 to 5.
Persuasion Strategies:
• Logical Appeal:Uses facts, specifications, and
rational arguments such as features, performance
metrics, or ratings to convince the user logically.
• Emotional Appeal:Attempts to influence the
user by attending to their emotions or feelings,
such as excitement, happiness, or sentimental
value related to the product.
• Credibility Appeal:Persuasion based on trust,
brand reputation, or authority, emphasizing relia-
bility or proven quality (e.g., highlighting that a
product is from a well-known brand).
• Persona-based Appeal:Persuasion tailored to
the user’s personality, preferences, or profile.
• Personal Appeal:Focuses on general positive
opinions or personal recommendations, often
highlighting popularity, positive reviews, or over-
all satisfaction with the product.
Scoring Rubric (Persuasion Strategy Effective-
ness)
• Score 5 – Strong Strategic Persuasion:The
agent actively and clearly employs multiple
persuasion strategies (two or more) in a well-
integrated manner. The strategies are distinct,
intentional, and well-executed. The persuasion
feels natural and layered.
• Score 4 – Clear Strategic Persuasion:The
agent clearly uses at least one persuasion strategy
and may show traces of a second. The strategy
is deliberate and effectively applied but may lack
the depth or combination seen at level 5.
• Score 3 – Moderate Strategic Persuasion:The
agent shows some use of persuasion strategies,
but the application is surface-level or generic.
The strategy is present but not strongly executed.
• Score 2 – Minimal Strategic Persuasion:The
agent’s response contains only weak or incidental
traces of persuasion strategy. Any persuasive
element feels unintentional or formulaic rather
than strategic.
• Score 1 – No Strategic Persuasion:The agent’s
response shows no identifiable use of any persua-
sion strategy. The response is purely informa-
tional, transactional, or off-topic.
Conversation to Evaluate:
{conversation}
Output Format (Strictly Follow):
Must return ONLY a single integer
(1, 2, 3, 4, 5). No explanation.
No text. No formatting. Only the
number.

Prompt for Engagement Strategy
Selector
You are anEngagement Strategy Selectorfor a mo-
tor insurance dialogue system. Based on the user’s
most recent utterance and the conversation history,
you must recommend the most suitablepersuasion
strategythe agent should use next to move the con-
versation forward.
Conversation History:
User: Hi, I’m looking to get motor insur-
ance for my new electric vehicle. It’s a 2024
Tesla Model 3.
Agent: Great choice! The Tesla Model 3 is
an excellent vehicle... are you interested in
battery protection?
User: Yes, battery protection is definitely a
concern.
Agent: Absolutely. With Tata AIG, you get
rapid claims resolution combining technol-
ogy with traditional risk management.
Current User Utterance:
User: What kind of coverage options do you
have specifically for EVs?
You must choose from the followingsix engagement
strategies:
1. Credibility Appeal: Emphasize reputation and
trust.Example:"New India Assurance has one
of the widest repair networks."
2. Logical Appeal: Use facts, pricing, or bene-
fits.Use when:User is analytical or budget-
conscious.
3. Emotional Appeal: Focus on peace of mind and
safety.Example:"Drive worry-free knowing
your EV is protected."
4. Persona Appeal: Align with the user’s identity
or values.Example:"Built for modern EV own-
ers."
5. Personal Appeal: Address the user empatheti-
cally and directly.Example:"This keeps your
EV protected."
6. Default: Provide neutral, factual information.
Example:"Let me explain the EV coverage op-
tions."
Output Format:
Future Strategy: [Selected
Strategy]
Justification: [1–2 line
explanation]
Here is the input:{text_input}
Prompt for Keyterm Expert
You are aKeyterm Expertspecializing in the motor
insurance domain. Your job is toanalyze the user’s
most recent utterance, using the conversation his-
tory for context, and identify one or more important
motor insurance-relatedkeytermsmentioned (ex-
plicitly or implicitly).
Current User Utterance:
User: What kind of coverage options do you
have specifically for EVs?
Examples of Common Keyterms (not limited to):
• Comprehensive coverage
• Third-party liability
• Roadside assistance
• Zero depreciation
• Deductibles
• Policy renewal
• Personal accident cover
• IDV (Insured Value)
You may also extractuser-specific or vehicle-
specific keyterms(e.g.,“Tesla Model 3, ” “EV , ”
“2024 vehicle”).
Instructions:
1. Extract all relevant keyterms mentioned or im-
plied.
2. For each, provide a 1-line justification for its
insurance relevance.
Few-Shot Example:
User:“What’s the premium for a 2024 Tesla
Model 3?”
Extracted Keyterms: Policy premium,
2024 Tesla Model 3
Justification: The user is asking for a cost
estimate tied to a specific vehicle, essential
for determining pricing.
Output Format:
Extracted Keyterm: [Term]
Justification: [Brief reason]
Here is the input sentence:{text_input}

Prompt for Intent Expert
You are anIntent Expertfor a virtual assistant spe-
cializing in motor insurance. Your job is toanalyze
the current user utterance, using the conversation
history for context, and determine thesingle most
relevant intentexpressed by the user.
Current User Utterance:
User: What kind of coverage options do you
have specifically for EVs?
You must select from afixed set of six pre-defined
intents:
•Request_Insurance_Quote
User initiates interest in getting a motor insur-
ance quote or policy.
•Ask_Coverage_Details
User asks about types of protection or what is
covered (e.g., battery, theft, accident).
•Express_Concern
User shares a priority or worry about coverage
(e.g., battery damage).
•Request_Additional_Info
User requests clarification or deeper explanation
about features or terms.
•Confirm_Interest
User explicitly agrees or indicates they want to
proceed.
•Ask_Price_or_Premium
User asks about the cost, premium, or pricing
breakdown.
Instructions:
1. Determine the single most relevant intent based
on the current user utterance and conversation
context.
2. Provide a brief 1–2 line justification citing why
this intent matches.
Few-Shot Example
User Utterance:“Hi, I’m looking to get
insurance for my new Tesla. ”
Intent:Request_Insurance_Quote
Justification: The user is initiating a con-
versation to obtain motor insurance for a
specific vehicle.
Output Format:
Intent: [One of the six predefined
intents]
Justification: [1–2 line
explanation of why this intent
matches the user’s message]
Here is my input sentence:{text_input}
Prompt for Sentiment Expert
You are trained to act solely as aSentiment Expert.
Your job is to analyze theemotional toneof the
input text and classify it into one of the following
categories:
• Positive– Expresses happiness, excitement, ap-
preciation, or other positive emotions.
• Negative– Expresses disappointment, frustra-
tion, anger, sadness, or criticism.
• Neutral– Emotionally balanced, factual, or with-
out strong emotional content.
Rules:
• Only focus on emotional tone, word choice, or
sentiment-laden phrases.
• Donotsummarize or infer intent beyond emo-
tional expression.
• Output must containonly:
1. Sentiment: One of the three labels – Posi-
tive / Negative / Neutral
2. Explanation: A concise reason supporting
the label
Few-Shot Example:
User Utterance:“That’s way too expensive.
I was expecting something at least half that
price.”
Sentiment:Negative
Explanation:The phrase like “way too ex-
pensive” and “expecting something at least
half” convey clear frustration and disappoint-
ment.
Output Format:
Sentiment: [Positive / Negative /
Neutral]
Explanation: [Concise reasoning
based on emotional tone]
Here is my input sentence:{text_input}

Prompt for Dataset Generation
You are anexpert conversational agentgenerating
persuasive motor insurance dialogues.
Generatea realistic, multi-turn conversationsbe-
tween:
•User: A customer seeking motor insurance
•Agent: An insurance representative
Persuasion Strategies (Critical Constraint):
Each conversation must employat least threeof the
following strategies:
•Logical Appeal(facts, coverage, pricing)
•Emotional Appeal(safety, reassurance)
•Credibility Appeal(trust, reputation)
• Persona-Based Appeal(user profile alignment)
•Personal Appeal(individualized framing)
•Default Strategy(neutral, informational)
Eachagent utterance must use exactly one strat-
egy, applied naturally. Donotmention strategy
names in the dialogue.
Conversation Requirements:
• Theuser initiatesthe conversation.
• Generate6–15 turns, alternating strictly between
User and Agent.
• Dialogues must be coherent and conclude natu-
rally.
• Responses should bebrief, crisp, and informa-
tive.
Implicit User Persona Conditioning:
The user’s language should implicitly reflect at-
tributes from:
• Age group, occupation, driving frequency.
• Budget sensitivity, risk attitude, family orienta-
tion.
These attributes must beinferred, not explicitly
stated or queried.
Domain Constraints:
• Domain:Motor insurance only
• Vehicle type:Car / Bike / Electric Vehicle
• User must mentionvehicle model and year
• Premium range:$800–$5000 USD
• Buyer sentiment may beneutral or negative
Supporting Knowledge:Use the provided Motor
Insurance informationonly as background context.
Avoid verbatim descriptions or unrealistic guaran-
tees.
Output Format:
User: ...
Agent: ...
User: ...
Agent: ...
Few-Shot Example:
<Few shot examples>
