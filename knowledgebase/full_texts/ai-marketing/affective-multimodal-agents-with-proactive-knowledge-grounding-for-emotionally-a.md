---
title: Affective Multimodal Agents with Proactive Knowledge Grounding for Emotionally Aligned Marketing
  Dialogue
url: https://arxiv.org/abs/2511.21728
category: ai-marketing
subcategory: empirical
date: 2025-11
venue: ''
authors:
- Lin Yu
- Xiaofei Han
- Yifei Kang
- Chiung-Yi Tseng
- Danyang Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2511.21728
pages: 12
chars: 53507
fetched_at: '2026-11-08T13:13:16+00:00'
kb_version: 1
---

# Affective Multimodal Agents with Proactive Knowledge Grounding for Emotionally Aligned Marketing Dialogue

Affective Multimodal Agents with Proactive
Knowledge Grounding for Emotionally Aligned
Marketing Dialogue
1st Lin Yu∗, 2 nd Xiaofei Han †, 3 rd Yifei Kang‡, 4 th Chiung-Yi Tseng§, 5 th Danyang Zhang ¶,
6th Ziqian Bi ∥, 7 th Zhimo Han ∗∗
∗Hunan Police Academy, Department of Criminal Investigation, Changsha, China
Email: tanxiyu@hnpa.edu.cn
†Business College, California State University, Long Beach, California, USA
Email: fendyhanxiaofei@gmail.com
‡Northwestern University, Chicago, USA
Email: Sophiekang2024@u.northwestern.edu
§LuxMuse AI
Email: ctseng@luxmuse.ai
¶AI Agent Lab, V okram Group, United Kingdom
Email: danyang@vokram.com
∥Beijing University of Technology
Email: zbill2016@gmail.com
∗∗Zheng Zhou University of Light Industry
Email: 542313460107@zzuli.edu.cn
Abstract—Recent advances in large language models (LLMs)
have enabled fluent dialogue systems, but most remain reactive
and struggle in emotionally rich, goal-oriented settings such as
marketing conversations. To address this limitation, we propose
AffectMind, a multimodal affective dialogue agent that performs
proactive reasoning and dynamic knowledge grounding to sustain
emotionally aligned and persuasive interactions. AffectMind
combines three components: a Proactive Knowledge Grounding
Network (PKGN) that continuously updates factual and affective
context from text, vision, and prosody; an Emotion–Intent
Alignment Model (EIAM) that jointly models user emotion and
purchase intent to adapt persuasion strategies; and a Reinforced
Discourse Loop (RDL) that optimizes emotional coherence and
engagement via reinforcement signals from user responses. Ex-
periments on two newly curated marketing dialogue datasets,
MM-ConvMarket and AffectPromo, show that AffectMind out-
performs strong LLM-based baselines in emotional consistency
(+26%), persuasive success rate (+19%), and long-term user
engagement (+23%), highlighting emotion-grounded proactivity
as a key capability for commercial multimodal agents.
Index Terms—multimodal dialogue systems, affective comput-
ing, knowledge grounding, marketing dialogue, emotion recogni-
tion, reinforcement learning, persuasive AI
I. INTRODUCTION
The rapid advancement of Large Language Models (LLMs)
has revolutionised conversational AI, enabling dialogue sys-
tems to achieve an unprecedented level of linguistic fluency
and contextual understanding [1]–[3]. However, despite these
remarkable capabilities, most current dialogue agents remain
Corresponding Author: Zhimo Han. Email: 542313460107@zzuli.edu.cn.
fundamentally reactive, responding to user inputs without
proactively guiding conversations toward specific goals [4].
This limitation becomes particularly pronounced in goal-
oriented domains such as marketing, where successful inter-
actions require not only understanding user intent but also
recognizing emotional states, adapting persuasion strategies,
and maintaining long-term engagement [5].
Traditional marketing dialogue systems face several critical
challenges that limit their effectiveness in real-world applica-
tions. First, they often operate in a purely textual modality,
missing crucial emotional cues from voice intonation, facial
expressions, and body language that human sales representa-
tives naturally leverage [6]. Second, these systems typically
rely on static knowledge bases that cannot adapt to evolving
product information, user preferences, or market trends in
real-time [7]. Third, existing approaches lack sophisticated
emotional intelligence, failing to recognize, understand, and
appropriately respond to the complex emotional dynamics that
characterize successful sales interactions [8].
The importance of emotional alignment in marketing con-
versations cannot be overstated. Research in consumer psy-
chology has consistently shown that purchasing decisions
are heavily influenced by emotional factors, with emotional
connection to a brand or product often outweighing purely
rational considerations [9], [10]. Moreover, customers expect
increasingly personalized and empathetic interactions from
AI systems, particularly in high-involvement purchase scenar-
ios [11]. Current dialogue systems, however, struggle to main-
arXiv:2511.21728v2  [cs.CL]  20 Dec 2025

AffectMind — Emotionally Aligned, Proactive Marketing Dialogue
User Signals
Text
Voice & Prosody
Visual Cues
Sense
Ground & Align
Act (Empathetic, Persuasive
Reply)
Learn (Feedback →
Policy/Memory)
Continuous improvement
Proactive Knowledge
Emotion ↔  Intent
Alignment
Outcomes
Emotional Consistency ↑  (+26%)
Persuasive Success ↑  (+19%)
Long‑term Engagement ↑
(+23%)
User
Engagement, emotion, conversion
Data & Benchmark Context
MM‑ConvMarket (multimodal, 10k) 
AffectPromo (promo dialogues)
Beats strong LLM/reaction-only baselines on emotional alignment, persuasion, and
engagement
1. Sense
2. Ground & Align
3. Act
4. Learn
Fig. 1. AffectMind: A proactive marketing dialogue system that senses user signals, aligns with emotion and intent, and generates empathetic, persuasive
responses.
tain emotional coherence across extended conversations and
often produce responses that feel mechanical or emotionally
misaligned with user needs.
To address these fundamental limitations, we propose Af-
fectMind, a novel multimodal affective dialogue agent de-
signed specifically for emotionally intelligent marketing con-
versations. Our system introduces three key architectural in-
novations that work synergistically to achieve superior perfor-
mance in commercial dialogue scenarios:
•Proactive Knowledge Grounding Network (PKGN): A
dynamic knowledge integration system that continuously
updates both factual product information and emotional
context representations by processing multimodal inputs
including text, visual cues, and prosodic features. Unlike
traditional static knowledge bases, PKGN enables real-
time adaptation to new information and changing con-
versation dynamics.
•Emotion-Intent Alignment Model (EIAM): A joint mod-
eling framework that simultaneously processes user emo-
tional states and purchase intentions, enabling dynamic
adaptation of persuasion strategies. EIAM leverages ad-
vanced multimodal fusion techniques to create a unified
representation of user affective and cognitive states.
•Reinforced Discourse Loop (RDL): A reinforcement
learning framework that optimizes long-term conversation
outcomes by learning from user engagement signals,
emotional responses, and ultimate conversion metrics.
RDL enables the system to develop sophisticated con-
versation strategies that balance immediate emotional
alignment with long-term persuasive goals.
Our main contributions can be summarized as follows:
•In order to address the discrepancy between predomi-
nantly reactive language models and the requirement for
emotionally aligned, goal-directed marketing dialogue,
a comprehensive multimodal framework is proposed,
namely AffectMind. This integrates Proactive Knowledge
Grounding (PKGN), Emotion-Intent Alignment (EIAM),
and a Reinforced Discourse Loop (RDL) to support
sustained, persuasive interactions.
•In order to address the paucity of realistic multimodal
benchmarks for emotion-grounded marketing conversa-
tions, two large-scale datasets, MM-ConvMarket and Af-
fectPromo, have been constructed, with rich annotations
for emotional states, persuasion strategies, and conversion
outcomes. The results demonstrate the significant superi-
ority of AffectMind in comparison to strong LLM- and
multimodal-based baselines across a range of evaluation
metrics.
•In order to address the practical and ethical challenges
associated with the deployment of emotionally aware per-
suasive agents in commercial settings, a detailed analysis
of transparency, privacy, fairness, and user agency con-
siderations is provided. This analysis is then distilled into
concrete deployment guidelines for responsible marketing
dialogue systems.
The rest of this paper is organized as follows: Section II

reviews related work in multimodal dialogue systems and af-
fective computing. Section III presents our AffectMind frame-
work in detail. Section IV describes our experimental setup
and comprehensive evaluation results. Section V discusses
implications, limitations, and future directions. Section VI
concludes the paper with broader impact considerations.
II. RELATEDWORK
A. Multimodal Dialogue Systems
Recent advances in multimodal dialogue systems have fo-
cused on integrating visual and textual information to create
more contextually aware conversational agents [3], [12], [13].
Early multimodal dialogue work primarily combined pre-
trained vision and language models through simple concatena-
tion or attention mechanisms [14], [15]. More sophisticated ap-
proaches have emerged with the development of transformer-
based architectures that can jointly process multiple modali-
ties [16], [17].
Recent work has explored various fusion strategies for
multimodal dialogue [18]. Early fusion approaches process
raw multimodal inputs simultaneously [19], while late fusion
methods combine modality-specific representations at higher
levels [20]. Intermediate fusion techniques, such as cross-
modal attention mechanisms, have shown promise in balancing
computational efficiency with representation quality.
However, the majority of extant multimodal dialogue sys-
tems concentrate chiefly on visual question answering or gen-
eral conversation scenarios, with limited consideration given
to emotion-aware applications. Moreover, these systems gen-
erally function in a reactive manner, responding to user queries
without proactively steering the conversation towards specific
objectives. The present work addresses these limitations by
introducing proactive reasoning capabilities specifically de-
signed for emotionally rich marketing interactions.
B. Affective Computing in Dialogue
Affective computing has emerged as a critical component of
human-computer interaction, with particular relevance to dia-
logue systems [8], [21]. Early emotion recognition approaches
focused on single modalities, such as text-based sentiment
analysis [22] or speech emotion recognition [23]. More recent
work has explored multimodal emotion recognition that com-
bines facial expressions, voice characteristics, and linguistic
content [24], [25].
In dialogue contexts, emotion recognition serves multi-
ple purposes: understanding user emotional states, generating
emotionally appropriate responses, and maintaining emotional
coherence across conversations [26]. Several recent works
have attempted to incorporate emotion awareness into dialogue
generation. For example, MIME [27] uses emotion recognition
to condition response generation, while EmpDialogue [28]
focuses on empathetic response generation.
However, the majority of extant affective dialogue systems
treat emotion as a secondary consideration rather than a pri-
mary driving force for conversation strategy. Prior studies also
show that although empathetic or emotion-aware responses
can improve user experience, they rarely integrate emotional
factors into persuasion-oriented dialogue planning [29], [30].
Existing systems tend to prioritise emotional appropriateness
over emotional persuasiveness, despite evidence that emotional
expression and affective framing significantly influence per-
suasive effectiveness [31]–[33]. This oversight neglects the
pivotal link between affective states and persuasive impact that
typifies effective marketing and decision-making interactions.
C. Knowledge Grounding and Proactive Dialogue
Knowledge grounding in dialogue systems involves inte-
grating external knowledge sources to provide informative and
factually accurate responses [7], [34]. Traditional approaches
rely on static knowledge bases or retrieval systems that provide
relevant facts based on conversation context [35], [36].
Recent work has explored dynamic knowledge integration
approaches that can update knowledge representations during
conversations [37], [38]. These systems typically use memory
networks or attention mechanisms to selectively incorporate
relevant knowledge while maintaining conversation coherence.
Proactive dialogue represents a significant departure from
traditional reactive systems. Instead of merely responding
to user inputs, proactive agents actively guide conversations
toward specific objectives [39]. This capability is particularly
important in task-oriented domains such as customer service,
sales, and education, where the agent must balance user needs
with organizational goals.
However, existing proactive dialogue systems often lack
sophisticated emotional modeling and struggle to maintain
natural conversation flow while pursuing specific objectives.
Our work addresses these limitations by introducing emotion-
ally intelligent proactive strategies specifically designed for
marketing contexts.
D. Marketing Dialogue and Persuasive AI
The intersection of AI and marketing has generated sig-
nificant research interest, particularly in the development of
conversational marketing systems [11], [40]. Early marketing
chatbots focused primarily on information provision and basic
customer service functions [41]. More sophisticated systems
have begun incorporating persuasion techniques derived from
social psychology and behavioral economics [42], [43].
Persuasive AI systems face unique challenges related to
user trust, transparency, and ethical considerations [44]. Recent
work has explored various persuasion strategies in AI systems,
including social proof, authority, scarcity, and reciprocity [45],
[46]. However, most existing persuasive AI systems operate
through simple rule-based approaches rather than sophisticated
emotional intelligence.
The ethical implications of persuasive AI have received
increasing attention from both researchers and policymak-
ers [47], [48]. Key concerns include user manipulation, privacy
protection, and the potential for AI systems to exploit vulner-
able populations. Our work addresses these concerns through
explicit ethical constraints and transparency mechanisms.

III. METHODOLOGY
A. Problem Formulation
LetU={u 1, u2, ..., uT }represent a sequence of user
inputs in a marketing dialogue session, where eachu t contains
multimodal information including textual contentu text t , visual
featuresu vision t (such as facial expressions and gestures), and
prosodic featuresu audio t (including tone, pitch, and speaking
rate). The goal is to generate a sequence of system responses
R={r 1, r2, ..., rT }that maximizes three key objectives:
max
R
α· E(U,R) +β· P(U,R) +γ· G(U,R)(1)
whereE(U,R)represents emotional alignment between user
states and system responses,P(U,R)measures persuasive
effectiveness toward marketing objectives, andG(U,R)quan-
tifies long-term user engagement. The weightsα,β, andγ
balance these competing objectives while ensuring ethical
constraints are maintained.
We formally define the emotional alignment objective as:
E(U,R) = 1 T
TX
t=1
sim(euser t , eresponse t )(2)
wheree user t ande response t represent the emotional states of
the user and the appropriateness of the system response at time
t, respectively, and sim(·,·)measures emotional compatibility.
B. AffectMind Architecture Overview
Figure 2 illustrates the overall architecture of AffectMind,
which consists of three main components working in synergy
to achieve emotionally aligned marketing dialogue. The system
processes multimodal user inputs through parallel feature
extraction pipelines, integrates this information through the
PKGN knowledge grounding network, performs joint emotion-
intent modeling via EIAM, and optimizes long-term conver-
sation strategy through RDL.
The data flow begins with multimodal input processing,
where textual content is encoded using a pre-trained language
model (RoBERTa-large), visual features are extracted using a
fine-tuned vision transformer, and audio features are processed
using Wav2Vec2.0. These modality-specific representations
are then fused through learned attention mechanisms and fed
into the core AffectMind components.
C. Proactive Knowledge Grounding Network (PKGN)
The PKGN module dynamically updates both factual and
affective knowledge representations by processing multimodal
inputs in real-time. Unlike traditional static knowledge bases,
PKGN maintains two complementary knowledge representa-
tions: factual knowledgeK f containing product information,
specifications, and objective features; and affective knowledge
Ka capturing emotional associations, user preferences, and
contextual mood indicators.
The knowledge update mechanism is formulated as:
Kt =Update(K t−1,Fuse(f text, fvision, faudio))(3)
whereK t = [Kt f ;K t a]represents the concatenated knowledge
state at timet, and Fuse(·)combines multimodal features
through a learned attention mechanism:
Fuse(ftext, fvision, faudio) =MHA([ftext;f vision;f audio])
(4)
The multimodal fusion employs multi-head attention
(MHA) to learn optimal combinations of modality-specific fea-
tures. Each modality contributes differently to factual versus
affective knowledge updates:
K t f =K t−1 f +α f ·FF f (Fuse(ftext, fvision, faudio))
K t a =K t−1 a +α a ·FF a(Fuse(ftext, fvision, faudio)) (5)
where FF f and FF a are modality-specific feed-forward net-
works, andα f ,α a are learnable update rates.
The proactive knowledge selection mechanism identifies
relevant knowledge based on predicted user needs and con-
versation trajectory:
Kselected =Attention(Q context, Kt, Vt)(6)
whereQ context represents the current conversation context,
and the attention mechanism selects the most relevant knowl-
edge for response generation.
D. Emotion-Intent Alignment Model (EIAM)
EIAM jointly models user emotional states and purchase
intentions to enable dynamic adaptation of persuasion strate-
gies. The model architecture consists of two parallel encod-
ing streams that process emotional and intentional signals,
followed by a fusion network that creates unified user state
representations.
The emotional encoding stream processes multimodal af-
fective cues:
Et =EmotionEncoder(Concat(f f acial, fprosodic, flinguistic))
(7)
wheref f acialrepresents facial expression features extracted
from video input,f prosodic captures voice emotion indicators,
andf linguistic encodes text-based sentiment and emotion
markers.
The intent encoding stream focuses on purchase-related
behavioral signals:
It =IntentEncoder(Concat(f query , fbehavior, fcontext))(8)
wheref query represents query intent features,f behavior cap-
tures user interaction patterns, andf context encodes conversa-
tion history and product context.
The emotion-intent fusion mechanism creates a unified
representation that captures the relationship between affective
states and purchase motivations:

🧑‍💻  Multimodal User Input at turn t ( )
🧠  Text Encoder (RoBERTa-large) →
🖼  Vision Transformer →
🎧  Wav2Vec2.0 →
🧪  Multi-head Attention Fusion MHA([ ; ; ])
→  fused features
🧭  Proactive Knowledge Grounding Network
📚  Prev. knowledge state
🧭  Update factual  and affective  via ,  and learnable rates
📚 ✨  New knowledge state
🧩  Conversation context 🔦  Attention( , , ) →
🤝  Emotion–Intent Alignment Model
🙂  Facial features
🎚  Prosodic features
🔤  Linguistic emotion features
🎭  EmotionEncoder(concat) →
🎯  Query / goal features
👣  Behavioral patterns
🗂  History & product context
🔀  FusionNetwork([ ; ;  ⊙  ]) →
user state
🕹  Policy network softmax(   + ) →
🧭  IntentEncoder(concat) →
🔄  Reinforced Discourse Loop (actor–critic RL)
🧍  User state  (from EIAM)
💬  Conversation context features
📚  Knowledge state  (from
PKGN)
🧩  State
🕹  Policy
⚡  Action  = (response
strategy, emotion tone, info
content)
🙋  User response (text,
emotion, behavior)
💎  Compute reward
🧺  Store  in
buffer B
🛠  Per-episode training loop (Algorithm 1)
⚖  Compute advantages  from
and value network
⬆  Update policy θ:
🔧  Update value φ:
🧑 💬  Text:
🎥 / 🙂  Video / Facial:
🔊  Audio / Prosody:
Fig. 2. Architecture of the AffectMind algorithm, showcasing multimodal fusion, proactive knowledge generation, emotion-intent alignment, and a reinforced
discourse loop for adaptive marketing dialogues.
St =FusionNetwork([E t;I t;E t ⊙I t])(9)
where⊙represents element-wise multiplication to capture
interaction effects between emotion and intent.
Dynamic strategy adaptation is achieved through a policy
network that selects appropriate persuasion techniques based
on the current user state:
πt =softmax(W πSt +b π)(10)
whereπ t represents the probability distribution over available
persuasion strategies (e.g., logical appeal, emotional appeal,
social proof, urgency creation).
E. Reinforced Discourse Loop (RDL)
The RDL component implements a reinforcement learning
framework that optimizes long-term conversation outcomes by
learning from user engagement signals, emotional responses,
and conversion metrics. The system treats each conversation
turn as an action in a partially observable Markov decision
process (POMDP), where the goal is to maximize expected
cumulative reward.
The state representation at timetcombines user state,
conversation context, and knowledge states:
st = [St;C t;K t](11)
whereS t is the EIAM user state,C t represents conversation
context features, andK t is the PKGN knowledge state.
The action space consists of discrete response strategies
combined with continuous response parameters:
at = [strategyt;emotion tonet;information contentt](12)
The reward function incorporates multiple feedback signals
with different time horizons:
Algorithm 1Reinforced Discourse Loop Training Algorithm
1:Initializepolicy networkπ θ and value networkV ϕ
2:Initializeexperience bufferB
3:foreach training episodedo
4:Reset conversation states 0
5:fort= 1toTdo
6:Sample actiona t ∼π θ(at|st)
7:Execute action and observe user response
8:Compute rewardR t from user feedback
9:Update states t+1
10:Store(s t, at, Rt, st+1)inB
11:end for
12:Compute advantage estimatesA t
13:Update policy using equation (12)
14:Update value function using equation (12)
15:end for
Rt =w 1Rimmediate +w 2Rengagement +w 3Rconversion (13)
whereR immediate provides immediate feedback based on
user emotional response,R engagement measures sustained
user interest, andR conversion represents ultimate marketing
success.
The policy optimization follows a actor-critic approach with
separate value and policy networks:
θpolicy ←θ policy +α∇ θpolicy logπ θpolicy (at|st)At
θvalue ←θ value +β∇ θvalue (Rt −V θvalue (st))2 (14)
whereA t =R t −V θvalue (st)is the advantage function.
Algorithm 1 presents the complete training procedure for
the Reinforced Discourse Loop component.

TABLE I
DATASETSTATISTICS ANDCHARACTERISTICS
Dataset Sessions Avg. Product Emotion Conversion
Turns Categories Classes Rate
MM-ConvMarket 10,000 15.3 12 6 34.2%
AffectPromo 5,000 22.1 8 6 28.7%
IV. EXPERIMENTS ANDRESULTS
A. Experimental Setup
1) Implementation Details:Our implementation uses Py-
Torch 1.12 with CUDA 11.7 for GPU acceleration. Training
was conducted on 8 HGX H100 node GPUs with 80GB mem-
ory each. The language model component uses RoBERTa-
large (355M parameters) for text encoding, Vision Transformer
(ViT-B/16) for visual feature extraction, and Wav2Vec2.0-large
for audio processing. The total model contains approximately
1.2B parameters across all components.
Hyperparameter optimization was performed using Optuna
with 100 trials. Key hyperparameters include: learning rate
lr= 2×10 −5 with cosine annealing, batch size of 16
conversations, maximum sequence length of 512 tokens, and
dropout rate of 0.1. The reinforcement learning component
uses discount factorγ= 0.95and GAE parameterλ= 0.95.
2) Datasets:We evaluate AffectMind on two newly curated
marketing dialogue datasets:
a) MM-ConvMarket:: A comprehensive multimodal
marketing conversation dataset containing 10,000 dialogue
sessions with text, video, and audio recordings from real
customer interactions across various product categories in-
cluding electronics, fashion, home goods, and services. Each
session contains an average of 15.3 turns and includes detailed
annotations for emotional states, persuasion attempts, and con-
version outcomes. The dataset was collected from volunteer
participants interacting with human sales representatives, then
post-processed to extract multimodal features and ground-truth
labels.
b) AffectPromo:: A specialized dataset focusing on
emotional dynamics in promotional conversations, featuring
5,000 annotated sessions with detailed emotion labels (using
a 6-class emotion model: Positive, Neutral, Negative, Angry,
Confused, Excited) and persuasion success indicators. This
dataset emphasizes high-emotion scenarios such as limited-
time offers, premium product sales, and customer retention
conversations. Sessions average 22.1 turns and include rich
contextual information about customer demographics, pur-
chase history, and interaction preferences.
Data preprocessing included conversation segmentation,
multimodal feature alignment, and quality filtering to remove
incomplete or corrupted sessions. Emotion annotations were
validated through inter-annotator agreement studies achieving
Cohen’s(kappa >0.75). Conversion labels were determined
based on actual purchase decisions within 7 days of conver-
sations.
3) Baseline Methods:We compare AffectMind against
several state-of-the-art baseline methods:
a) GPT-3.5 Baseline:: Fine-tuned GPT-3.5-turbo on
marketing dialogue data with standard conversation prompting.
This represents current industry practice for conversational AI
in sales contexts.
b) GPT-4 Enhanced:: GPT-4 with carefully crafted
prompts including emotion awareness instructions and sales
methodology guidelines. This baseline tests whether sophisti-
cated prompting can achieve comparable results to our spe-
cialized architecture.
c) MultiModal-BERT:: A BERT-based dialogue model
enhanced with visual and audio feature fusion through con-
catenation and cross-modal attention mechanisms [17].
d) BLIP-2 Dialogue:: A recent vision-language model
adapted for dialogue generation through fine-tuning on con-
versational data [13].
e) EmpDialogue++:: An enhanced version of the em-
pathetic dialogue system with additional marketing-specific
training and multimodal capabilities [28].
f) PersuaBot:: A specialized persuasive dialogue system
implementing rule-based persuasion techniques from social
psychology literature [5].
4) Evaluation Metrics:Our evaluation encompasses both
objective computational metrics and subjective human assess-
ments:
a) Emotional Consistency Score:: Measures alignment
between predicted and actual user emotional responses using
cosine similarity between emotion embeddings. Calculated as
the average similarity across all conversation turns.
b) Persuasive Success Rate:: Percentage of conversa-
tions that result in successful conversions (purchases) within
the evaluation period. This represents the primary business
objective for marketing dialogue systems.
c) User Engagement Score:: Composite metric combin-
ing conversation length, user response rate, and interaction
quality indicators such as follow-up questions and positive
feedback signals.
d) Emotional Intelligence Quotient (EIQ):: Novel met-
ric measuring the system’s ability to recognize, understand,
and appropriately respond to user emotions across different
emotional states and transition scenarios.
e) Knowledge Integration Accuracy:: Measures how
effectively the system incorporates relevant factual information
while maintaining conversational flow and emotional appropri-
ateness.
f) Response Quality:: Human-evaluated metric assess-
ing naturalness, helpfulness, and appropriateness of system
responses on a 5-point Likert scale.
B. Main Results
Performance Comparison on Marketing Dialogue Tasks
Table II presents the comprehensive performance com-
parison between AffectMind and baseline methods across
all evaluation metrics. Our approach demonstrates significant

Fig. 3. Performance Comparison on Marketing Dialogue Tasks
improvements across all measured dimensions, with particu-
larly strong performance in emotional consistency and user
engagement. Results can be shown in Figure 3.
Statistical significance testing using paired t-tests confirms
that all improvements are statistically significant. The emo-
tional consistency improvement of 26% represents a substan-
tial advancement in the system’s ability to maintain appropri-
ate emotional tone throughout conversations. The persuasive
success rate improvement of 19% translates to significant
business value in real-world deployment scenarios.
Beyond the absolute numbers in Table II, we assess both
statistical and practical significance. For statistical validity,
we report means across multiple random seeds and conversa-
tion resamplings, and compute non-parametric bootstrap 95%
confidence intervals; paired tests across identical conversation
sets indicate consistent gains (Holm–Bonferroni corrected).
For practical significance, two observations stand out. First,
Emotional Consistency improvements translate into measur-
ably smoother state transitions: the model is less likely to os-
cillate between contradictory tones within a 3–5 turn window,
which directly stabilizes downstream persuasion strategies.
Second, the Persuasive Success Rate gains are accompanied by
higher user-initiated follow-ups, indicating that AffectMind’s
improvements are not merely cosmetic.
We further examine calibration by comparing predicted
emotion distributions to human labels via reliability curves.
AffectMind exhibits lower Expected Calibration Error than
baselines, suggesting better confidence–accuracy alignment.
This matters in deployment since over-confident yet mis-
aligned affect predictions tend to trigger inappropriate strate-
gies.
A mediation analysis across sessions shows that improve-
ments in EIQ partly mediate gains in User Engagement, which
in turn mediate Persuasive Success. Qualitatively, AffectMind
de-escalates negative states faster and sustains positive mo-
mentum longer; quantitatively, we observe that sessions with
stable affect trajectories (low variance of turn-level affect
deltas) are those with the highest conversion likelihood. This
supports our design choice to optimize emotion–intent align-
ment before strategy selection.
C. Ablation Studies
We conducted comprehensive ablation studies to understand
the contribution of each component and design choice. Ta-
ble IV presents results for different component combinations,
which was also depicted in Figure 4.
The ablation study reveals that each component contributes
significantly to overall performance. The PKGN component
shows the largest individual contribution to persuasive success,
while EIAM most strongly impacts emotional consistency. The
RDL component primarily improves user engagement through
better long-term strategy optimization.
Multimodal input processing provides substantial benefits
over text-only approaches, with visual emotion recognition
contributing most significantly to emotional consistency im-
provements. Audio features, while less impactful individually,
provide crucial disambiguation in emotionally ambiguous sce-
narios.
Table IV indicates that each module contributes materi-
ally. Removing the Proactive Knowledge Grounding Network
(PKGN) most strongly hurts Persuasive Success, consistent
with our hypothesis that timely and context-appropriate facts

TABLE II
PERFORMANCECOMPARISON ONMARKETINGDIALOGUETASKS
Method Emotional Persuasive User EIQ Response
Consistency Success (%) Engagement Score Quality
GPT-3.5 Baseline 72.3 64.1 58.7 3.2 3.1
GPT-4 Enhanced 76.8 67.3 62.4 3.6 3.5
MultiModal-BERT 75.8 67.3 61.2 3.4 3.3
BLIP-2 Dialogue 78.1 69.8 63.4 3.7 3.6
EmpDialogue++ 79.2 70.1 65.3 3.8 3.7
PersuaBot 74.6 71.2 59.8 3.3 3.4
AffectMind 91.1 76.3 72.1 4.3 4.2
Improvement +26% +19% +23% +13% +14%
TABLE III
LONGCONVERSATIONSESSIONPERFORMANCESTABILITYANALYSIS
Dialogue Turns Emotional Consistency Knowledge Consistency Response Relevance User Engagement Memory Retention Strategy Effectiveness
1-10 91.5 93.2 94.1 88.7 95.3 89.6
11-20 90.8 91.7 92.8 86.4 91.8 87.3
21-30 89.3 89.5 90.2 83.1 87.4 84.9
31-40 87.6 86.8 87.9 79.8 82.7 81.2
41-50 85.2 83.4 84.6 75.3 77.9 77.8
51+ 82.7 79.1 80.3 70.6 72.5 73.4
Performance Degradation 9.6% 15.1% 14.7% 20.4% 23.9% 18.1%
TABLE IV
ABLATIONSTUDYRESULTS
System Configuration Emotional Persuasive User
Consistency Success (%) Engagement
AffectMind (Full) 91.1 76.3 72.1
- w/o PKGN 85.7 72.1 67.8
- w/o EIAM 83.2 69.4 65.2
- w/o RDL 88.3 71.9 68.5
- w/o Multimodal 79.4 68.7 61.3
- Static Knowledge 82.6 70.2 64.7
- Text Only 76.2 65.8 58.9
are the backbone of credible marketing dialogue. Removing
the Emotion–Intent Alignment Module (EIAM) primarily de-
grades Emotional Consistency, confirming that accurate affect
recognition and regulation are prerequisites for strategy selec-
tion. Disabling the Reinforcement Dialogue Learner (RDL)
reduces User Engagement—the RL policy appears to learn
when to pivot among strategies rather than merely which
strategy to use.
We also examine interaction effects. PKGN+EIAM yields
super-additive improvements relative to either alone: accu-
rate affect tracking increases the marginal utility of freshly
grounded knowledge, and the availability of precise, relevant
facts reduces the cognitive dissonance users feel when tone
and content diverge. These observations are consistent with
the cross-attention fusion results in Table V, where richer
inter-modal conditioning benefits both affect tracking and
knowledge selection.
D. Qualitative Analysis
We qualitatively probe how AffectMind attains its quan-
titative gains by analyzing four axes: (i) multimodal fusion
TABLE V
MULTIMODALFUSIONSTRATEGYPERFORMANCECOMPARISON
Performance Metrics Computational Metrics
Fusion Strategy Emot. Pers. User Infer. Params Fusion
Cons. Succ. Eng. Time (M) Eff.
Early Fusion 84.2 70.1 66.3 45 890 0.78
Late Fusion 82.7 68.9 64.8 38 875 0.82
Cross-Attention91.1 76.3 72.152 920 0.75
Dynamic Gating 89.6 74.8 70.5 49 905 0.76
behavior, (ii) proactive knowledge grounding dynamics, (iii)
emotion-intent alignment effects across affective states, and
(iv) long-session stability.
Table V shows a consistent pattern: cross-attention
yields the strongest peak performance across Emot. Cons.,
Pers. Succ., and User Eng., while dynamic gating approaches
this ceiling with lower average inference time. In human in-
spection, cross-attention produces turns that more tightly cou-
ple wording and nonverbal cues. Dynamic gating, in contrast,
learns to defer multimodal reasoning when text and PKGN
already provide high-confidence evidence, which explains its
favorable efficiency without large quality loss.
Table III shows performance decay with length, dominated
bymemory retention(–23.9%) andengagement(–20.4%).
Affect-aware compression that preserves (i) objections, (ii) ex-
plicit commitments, and (iii) affect-trend descriptors recovers a
large share of the drop by keeping strategy selection grounded
in what the user last cared about. Peaks align with objection
and price-sensitivity turns; the model pivots from spec sheets
to social proof (reviews) and logistics (return/warranty) before
escalating to scarcity cues, mirroring the quantitative gains in
Tables VI and VII. In a high-end electronics vignette, Affect-

AffectMind (Full) w/o PKGN w/o EIAM w/o RDL w/o Multimodal Static Knowledge Text Only
Model Configuration
0
20
40
60
80
100Score (%)
91.1
85.7
83.2
88.3
79.4
82.6
76.276.3
72.1
69.4
71.9
68.7 70.2
65.8
72.1
67.8
65.2
68.5
61.3
64.7
58.9
Ablation Study Results
Emotional Consistency
Persuasive Success
User Engagement
Fig. 4. Ablation study results showing the impact of removing individual components (PKGN, EIAM, RDL) and design choices (multimodal input, dynamic
knowledge) on emotional consistency, persuasive success, and user engagement.
TABLE VI
PKGN KNOWLEDGEUPDATEMECHANISMEFFECTIVENESSANALYSIS
Knowledge Update Strategy Knowledge Relevance Response Accuracy Dialogue Coherence Information Timeliness User Satisfaction
Static Knowledge Base 0.72 0.68 0.75 0.61 3.2
Periodic Updates 0.81 0.74 0.79 0.73 3.6
Attention-based 0.85 0.79 0.82 0.78 3.9
PKGN (Dynamic)0.93 0.87 0.91 0.89 4.3
Fig. 5. Performance Degradation Across Dialogue Turns
TABLE VII
EMOTION-INTENTALIGNMENTEFFECTIVENESSANALYSIS
Emotional State Intent Recognition Strategy Conversion Positive Emotional
Accuracy (%) Matching (%) Rate (%) Response Rate (%)
Positive 92.3 94.1 42.7 88.5
Neutral 87.6 85.3 31.2 76.8
Negative 83.4 79.8 18.9 65.3
Angry 78.1 72.6 12.4 58.7
Confused 85.9 83.2 25.7 71.4
Excited 90.8 91.5 38.9 85.2
Average 86.4 84.4 28.3 74.3
EIAM Enhanced91.2 93.7 36.8 87.9
Mind de-escalates frustration by reframing ”spec overload”
into lifestyle outcomes, then grounds claims with verified
review snippets; baselines persist with technical detail and lose
the user.

V. DISCUSSION
A. Implications for Marketing AI
The results demonstrate that emotion-grounded proactive
dialogue represents a significant advancement in marketing AI
capabilities. The 19% improvement in persuasive success rate
could translate to substantial business impact in real-world
deployments. For a typical e-commerce platform processing
millions of customer interactions, this improvement could
result in significant revenue increases.
The multimodal capabilities of AffectMind enable more
natural and effective customer interactions compared to text-
only systems. The ability to process visual and audio cues
allows the system to detect emotional states that might not be
explicitly expressed in text, leading to more appropriate and
effective responses.
The proactive knowledge grounding capability addresses a
critical limitation of current marketing chatbots. By dynami-
cally updating knowledge representations based on conversa-
tion context and user behavior, the system can provide more
relevant and timely information, leading to improved customer
satisfaction and conversion rates.
B. Ethical Considerations
The development of emotionally intelligent persuasive AI
systems raises important ethical considerations that must be
carefully addressed:
a) Transparency and User Awareness:: Users should be
clearly informed when interacting with AI systems, particu-
larly those designed to influence behavior. Our system includes
explicit disclosure mechanisms and allows users to request
information about the AI’s emotional and persuasive strategies.
b) Manipulation vs. Assistance:: There is a fine line
between helpful persuasion and manipulative coercion. We
implement explicit constraints to prevent the system from
exploiting vulnerable emotional states or using deceptive prac-
tices. The system is designed to provide genuine value to users
while achieving business objectives.
c) Privacy Protection:: The collection and processing
of emotional data raises significant privacy concerns. Our sys-
tem implements differential privacy mechanisms and provides
users with control over their emotional data usage and storage.
d) Bias and Fairness:: Emotional AI systems may
inadvertently discriminate against certain demographic groups
or emotional expression styles. We conducted extensive bias
testing and implemented fairness constraints to ensure equi-
table treatment across diverse user populations.
C. Limitations and Future Work
Several limitations of the current work provide opportunities
for future research:
a) Computational Efficiency:: The current implemen-
tation requires significant computational resources, limiting
deployment scalability. Future work will explore more effi-
cient architectures and optimization techniques for real-time
deployment.
b) Cross-Cultural Generalization:: Emotional expres-
sion and persuasion effectiveness vary significantly across
cultures. Current datasets primarily represent Western cultural
contexts, and future work should explore cross-cultural adap-
tation mechanisms.
c) Long-Term Relationship Modeling:: Current eval-
uation focuses on individual conversation sessions. Future
research should explore how emotionally intelligent systems
can build and maintain long-term customer relationships across
multiple interactions.
d) Multi-Party Conversations:: Real-world marketing
scenarios often involve multiple participants. Future work
should extend the framework to handle complex multi-party
dynamics and group decision-making processes.
e) Adversarial Robustness:: The system’s vulnerabil-
ity to adversarial attacks and manipulation attempts requires
further investigation. Future research should develop robust
defense mechanisms against potential misuse.
f) Dataset Availability:: The MM-ConvMarket and Af-
fectPromo datasets were collected in collaboration with retail
industry partners under standard commercial agreements. Due
to the inclusion of real customer interactions and business-
sensitive conversion data, the raw datasets are subject to
privacy and confidentiality requirements that prevent public
release. Interested researchers may contact the corresponding
author to explore potential collaboration opportunities.
g) Reproducibility Constraints:: Reproducing our re-
sults requires considerable computational resources. Training
was conducted on an HGX H100 GPU (8×H100 SXM5
GPUs, 80GB each) over approximately 4 weeks. The multi-
modal feature extraction pipeline relies on licensed third-party
components. Additionally, the reinforcement learning module
exhibits sensitivity to random initialization, with performance
variance of up to 12% observed across different runs. We hope
future work can explore more resource-efficient alternatives.
VI. CONCLUSION ANDFUTUREWORK
In this paper, we presented AffectMind, a novel multimodal
affective dialogue agent designed for emotionally aligned
marketing conversations. Our approach introduces three key
architectural innovations: the Proactive Knowledge Grounding
Network (PKGN) for dynamic knowledge integration, the
Emotion-Intent Alignment Model (EIAM) for joint emotional
and intentional reasoning, and the Reinforced Discourse Loop
(RDL) for sustained engagement optimization.
The comprehensive experimental evaluation demonstrates
significant improvements over state-of-the-art baselines across
multiple metrics: emotional consistency (+26%), persuasive
success rate (+19%), and user engagement (+23%). These
results establish emotion-grounded proactivity as a crucial
capability for next-generation conversational AI systems in
commercial applications.
Our contributions extend beyond technical improvements to
include important considerations for ethical AI deployment in
persuasive contexts. The explicit attention to transparency, user

agency, and fairness provides a framework for responsible de-
velopment of emotionally intelligent commercial AI systems.
The proprietary datasets (MM-ConvMarket and Affect-
Promo) developed through industry partnerships demonstrate
the potential of emotion-grounded dialogue systems in com-
mercial contexts.
Future research directions include extending AffectMind
to other goal-oriented dialogue domains, improving com-
putational efficiency for large-scale deployment, developing
more sophisticated ethical safeguards, and exploring cross-
cultural adaptation mechanisms. Additionally, investigation of
long-term relationship building and multi-party conversation
dynamics represents promising areas for advancement.
The broader impact of this work extends to the transforma-
tion of customer-business interactions through more natural,
empathetic, and effective AI-mediated conversations. As AI
systems become increasingly integrated into commercial con-
texts, the principles and techniques developed in this work will
be crucial for creating beneficial outcomes for both businesses
and customers.
REFERENCES
[1] T. Brownet al., “Language models are few-shot learners,” inAdvances in
Neural Information Processing Systems, vol. 33, 2020, pp. 1877–1901.
[2] M. Zhang, Z. Fang, T. Wang, S. Lu, X. Wang, and T. Shi, “CCMA:
A framework for cascading cooperative multi-agent in autonomous
driving merging using large language models,”Expert Systems with
Applications, vol. 282, p. 127717, 2025.
[3] C. X. Liang, P. Tian, C. H. Yin, Y . Yua, W. An-Hou, L. Ming,
T. Wang, Z. Bi, and M. Liu, “A comprehensive survey and guide
to multimodal large language models in vision-language tasks,”arXiv
preprint arXiv:2411.06284, 2024.
[4] Y . Zhang, S. Sun, M. Galley, Y .-C. Chen, C. Brockett, X. Gao, J. Gao,
J. Liu, and B. Dolan, “DialoGPT: Large-scale generative pre-training for
conversational response generation,” inProceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, 2020, pp.
270–278.
[5] X. Wang, Z. Chen, K. Yang, H. Zhou, and L. Zhao, “Persuasive dialogue
generation with persona-based reinforcement learning,” inProceedings
of the 2022 Conference on Empirical Methods in Natural Language
Processing, 2022, pp. 3542–3555.
[6] S. Poria, E. Cambria, R. Bajpai, and A. Hussain, “A review of affective
computing: From unimodal analysis to multimodal fusion,”Information
Fusion, vol. 37, pp. 98–125, 2017.
[7] E. Dinanet al., “Wizard of wikipedia: Knowledge-powered conver-
sational agents,” inProceedings of the International Conference on
Learning Representations, 2019.
[8] R. W. Picard,Affective Computing. MIT Press, 2000.
[9] A. Damasio,Descartes’ Error: Emotion, Reason, and the Human Brain.
Putnam Publishing, 1994.
[10] A. Bechara, “The role of emotion in decision-making: Evidence from
neurological patients with orbitofrontal damage,”Brain and Cognition,
vol. 55, no. 1, pp. 30–40, 2005.
[11] V . Kumaret al., “Artificial intelligence in marketing: Consequences for
the retail industry,”California Management Review, vol. 61, no. 4, pp.
5–25, 2019.
[12] P. P. Liang, A. Zadeh, and L.-P. Morency, “Foundations and recent
trends in multimodal machine learning: Principles, challenges, and open
questions,”ACM Computing Surveys, vol. 55, no. 10, pp. 1–38, 2022.
[13] J. Li, D. Li, S. Savarese, and S. Hoi, “BLIP-2: Bootstrapping vision-
language pre-training with frozen image encoders and large language
models,” inProceedings of the International Conference on Machine
Learning, 2023, pp. 19 730–19 742.
[14] S. Antolet al., “VQA: Visual question answering,” inProceedings of
the IEEE International Conference on Computer Vision, 2015, pp. 2425–
2433.
[15] A. Daset al., “Visual dialog,” inProceedings of the IEEE Conference
on Computer Vision and Pattern Recognition, 2017, pp. 326–335.
[16] L. H. Li, M. Yatskar, D. Yin, C.-J. Hsieh, and K.-W. Chang, “Visu-
alBERT: A simple and performant baseline for vision and language,”
arXiv preprint arXiv:1908.03557, 2019.
[17] J. Lu, D. Batra, D. Parikh, and S. Lee, “ViLBERT: Pretraining task-
agnostic visiolinguistic representations for vision-and-language tasks,”
inAdvances in Neural Information Processing Systems, 2019, pp. 13–
23.
[18] T. Zeng, T. Wang, M. Zhang, J. Yin, Z. Zeng, F. Zhang, Y . Wang, J. Jiao,
Y . Wang, Y . He, J. Tan, C. Claudel, and X. Wang, “TCSTNet: A text-
driven color style transfer network for low-light image enhancement,”
Expert Systems with Applications, vol. 299, p. 130012, 2025.
[19] T. Baltru ˇsaitis, C. Ahuja, and L.-P. Morency, “Multimodal machine
learning: A survey and taxonomy,”IEEE Transactions on Pattern
Analysis and Machine Intelligence, vol. 41, no. 2, pp. 423–443, 2019.
[20] A. Zadeh, M. Chen, S. Poria, E. Cambria, and L.-P. Morency, “Tensor
fusion network for multimodal sentiment analysis,” inProceedings
of the 2017 Conference on Empirical Methods in Natural Language
Processing, 2017, pp. 1103–1114.
[21] R. A. Calvo and S. D’Mello, “Affect detection: An interdisciplinary
review of models, methods, and their applications,”IEEE Transactions
on Affective Computing, vol. 1, no. 1, pp. 18–37, 2010.
[22] B. Liu,Sentiment Analysis and Opinion Mining. Morgan & Claypool
Publishers, 2012.
[23] H. A. El Ayadi, M. S. Kamel, and F. Karray, “Survey on speech emotion
recognition: Features, classification schemes, and databases,”Pattern
Recognition, vol. 44, no. 3, pp. 572–587, 2011.
[24] T. Baltru ˇsaitis, P. Robinson, and L.-P. Morency, “OpenFace: An open
source facial behavior analysis toolkit,” inProceedings of the IEEE
Winter Conference on Applications of Computer Vision, 2016, pp. 1–
10.
[25] A. Zadehet al., “Multimodal language analysis in the wild: CMU-
MOSEI dataset and interpretable dynamic fusion graph,” inProceedings
of the 56th Annual Meeting of the Association for Computational
Linguistics, 2018, pp. 2236–2246.
[26] H. Zhou, M. Huang, T. Zhang, X. Zhu, and B. Liu, “Emotional
chatting machine: Emotional conversation generation with internal and
external memory,” inProceedings of the AAAI Conference on Artificial
Intelligence, vol. 32, no. 1, 2018.
[27] N. Majumder, P. Hong, S. Peng, J. Lu, D. Ghosal, A. Gelbukh,
R. Mihalcea, and S. Poria, “MIME: MIMicking emotions for empa-
thetic response generation,” inProceedings of the 2020 Conference on
Empirical Methods in Natural Language Processing, 2020, pp. 8968–
8979.
[28] H. Rashkin, E. M. Smith, M. Li, and Y .-L. Boureau, “Towards em-
pathetic open-domain conversation models: A new benchmark and
dataset,” inProceedings of the 57th Annual Meeting of the Association
for Computational Linguistics, 2019, pp. 5370–5381.
[29] A. M. Samad, K. Mishra, M. Firdaus, and A. Ekbal, “Empathetic per-
suasion: Reinforcing empathy and persuasiveness in dialogue systems,”
inFindings of the Association for Computational Linguistics: NAACL
2022, 2022, pp. 844–856.
[30] W. Shi, Y . Li, S. Sahay, and Y . Zhou, “Refine and imitate: Reducing
repetition and inconsistency in persuasion dialogues via reinforcement
learning and human demonstration,” inFindings of the Association for
Computational Linguistics: EMNLP 2021, 2021, pp. 3478–3492.
[31] K. Yoshino, Y . Ishikawa, M. Mizukami, Y . Suzuki, S. Sakti, and
S. Nakamura, “Dialogue scenario collection of persuasive dialogue
with emotional expressions via crowdsourcing,” inProceedings of the
Eleventh International Conference on Language Resources and Evalu-
ation (LREC 2018), 2018.
[32] H. U. Genc ¸, S. Chandrasegaran, T. Dingler, and H. Verma, “Persuasion
in pixels and prose: The effects of emotional language and visuals in
agent conversations on decision-making,” inProceedings of the 2025
CHI Conference on Human Factors in Computing Systems, 2025, pp.
1–27.
[33] C. Carrasco-Farr ´e, “Large language models are as persuasive as humans,
but how? about the cognitive effort and moral-emotional language of
LLM arguments,”arXiv preprint arXiv:2404.09329, 2024.
[34] M. Ghazvininejad, C. Brockett, M.-W. Chang, B. Dolan, J. Gao, W.-t.
Yih, and M. Galley, “A knowledge-grounded neural conversation model,”
inProceedings of the AAAI Conference on Artificial Intelligence, vol. 32,
no. 1, 2018.

[35] S. Moon, P. Shah, A. Kumar, and R. Subba, “OpenDialKG: Explainable
conversational reasoning with attention-based walks over knowledge
graphs,” inProceedings of the 57th Annual Meeting of the Association
for Computational Linguistics, 2019, pp. 845–854.
[36] H. Zhouet al., “Commonsense knowledge aware conversation gener-
ation with graph attention,” inProceedings of the International Joint
Conference on Artificial Intelligence, 2018, pp. 4623–4629.
[37] A. Madotto, C.-S. Wu, and P. Fung, “Mem2Seq: Effectively incorpo-
rating knowledge bases into end-to-end task-oriented dialog systems,”
inProceedings of the 56th Annual Meeting of the Association for
Computational Linguistics, 2018, pp. 1468–1478.
[38] W. Wu, Z. Guo, X. Zhou, H. Wu, X. Zhang, R. Lian, and H. Wang,
“Proactive human-machine conversation with explicit conversation
goal,” inProceedings of the 57th Annual Meeting of the Association
for Computational Linguistics, 2019, pp. 3794–3804.
[39] J. Tang, T. Zhao, C. Xiong, X. Liang, E. Xing, and Z. Hu, “Target-guided
open-domain conversation,” inProceedings of the 57th Annual Meeting
of the Association for Computational Linguistics, 2019, pp. 5624–5634.
[40] M. Chung, E. Ko, H. Joung, and S. J. Kim, “Chatbot e-service and
customer satisfaction regarding luxury brands,”Journal of Business
Research, vol. 117, pp. 587–595, 2020.
[41] A. Følstad and P. B. Brandtzæg, “Chatbots and the new world of HCI,”
Interactions, vol. 24, no. 4, pp. 38–42, 2017.
[42] B. J. Fogg,Persuasive Technology: Using Computers to Change What
We Think and Do. Morgan Kaufmann, 2002.
[43] K. Torning and H. Oinas-Kukkonen, “Persuasive system design: State
of the art and future directions,” inProceedings of the 4th International
Conference on Persuasive Technology, 2009, pp. 1–8.
[44] D. Berdichevsky and E. Neuenschwander, “Toward an ethics of per-
suasive technology,”Communications of the ACM, vol. 42, no. 5, pp.
51–58, 1999.
[45] J. Ham, A. Spahn, and H. Oinas-Kukkonen, “Can persuasive technology
help reduce obesity? an exploration of moral and ethical issues,” inPro-
ceedings of the 10th International Conference on Persuasive Technology,
2015, pp. 112–123.
[46] A. Stibe and H. Oinas-Kukkonen, “Advancing social influence systems
research and practice: Seven C’s framework,” inProceedings of the 10th
International Conference on Persuasive Technology, 2015, pp. 73–84.
[47] M. Ryan, “In AI we trust: Ethics, artificial intelligence, and reliability,”
Science and Engineering Ethics, vol. 26, no. 5, pp. 2749–2767, 2020.
[48] C. Metz and A. Satariano, “An AI chatbot convinced a belgian man to
kill himself,”The New York Times, March 2023.
