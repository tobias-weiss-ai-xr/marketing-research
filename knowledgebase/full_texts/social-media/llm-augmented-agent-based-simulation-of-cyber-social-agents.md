---
title: LLM-Augmented Agent-Based Simulation of Cyber Social Agents
url: https://arxiv.org/abs/2610.32988
category: social-media
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Lynnette Hui Xian Ng
- Kathleen M. Carley
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.32988
pages: 9
chars: 25880
fetched_at: '2026-11-08T13:13:59+00:00'
kb_version: 1
---

# LLM-Augmented Agent-Based Simulation of Cyber Social Agents

LLM-Augmented Agent-Based Simulation of
Cyber Social Agents
Lynnette Hui Xian Ng1 Kathleen M. Carley1
1Carnegie Mellon University
lynnetteng@cmu.edu
Abstract
Social media bots are often portrayed as malicious automations to be detected and
removed, but automation on social media platforms encompasses a wide spectrum
of roles, behaviors, and rhetorical strategies that can shape online discourse in both
constructive and destructive ways. This work conceptualizes these automated ac-
tors asCyber Social Agentsthrough a taxonomy of archetypes characterized by
their operational tactics and rhetorical style. We integrate this taxonomy into an
LLM-driven social simulation, where agents communicate and coordinate in a
network environment. Using empirically grounded CSA personas, we simulate
heterogeneous online societies to study how agent diversity shapes information
diffusion and social influence. Our approach bridges the gap between rule-based
agent models and LLM-powered simulations with generated agents that are pa-
rameterized from empirical data.
1 Introduction
A social media bot is broadly understood to be an automated agent on social media, and much of
the current work has emphasized their detection strategies Ng and Carley [2023a], Hayawi et al.
[2023], Orabi et al. [2020]. This includes the creation and deployment of generic bot detection
algorithms with feature-based, graph-based or deep-learning approaches Orabi et al. [2020]. Most
of these studies treat bots as malicious creatures to be mitigated, because of their contribution to
spreading harmful information, causing ideological polarization and sometimes instigating offline
violence Himelein-Wachowiak et al. [2021], Shu et al. [2020], Ng and Taeihagh [2021].
However, the bot is not simply a static agent. The term “bot” by itself describes a generic automation
algorithm, treating all forms and behaviors of an automation as a homogeneous entity. Yet the
automated agent can express different behavioral archetypes and rhetorical styles rather than simply
a monolithic “bot” automation. Recent research highlights its diversity: amplifiers that boost chosen
principals and narratives Jia et al. [2024], cyborgs whose automation varies over time Ng et al.
[2024], bridging agents who connect multiple narratives and clusters of users together Ng and Carley
[2023b] and conversational agents that sustain dialogue and persona Wang et al. [2018]. This line
of work motivates taxonomies that classify automated agents by operational tactics and not simply
by binary “bot vs. human” labels.
Here, we expand the term “bot” into a “Cyber Social Agent” (CSA), framing automation in terms
of nuanced sets of archetypes rather than a monolithic category. Automated accounts are not merely
scripts, but they are a suite of agents that adopt specific roles, employ different strategies, and interact
uniquely with humans, other CSAs and platform infrastructures. These archetypes have agency, and
therefore can be either good or bad. Some CSAs serve constructive roles like news dissemination
and emotional support, while others spread misinformation and manipulate public discourse.
Preprint.
arXiv:2610.32988v2  [cs.MA]  31 Oct 2026

Against this backdrop, our work formalizes a taxonomy ofCyber Social Agentsthat encodes the
personality, operational tactics and rhetorical style as parameters, explicitly typing linguistic behav-
ior to network tactics in a social simulation. We incorporate these dynamics into a social simulation
where we model these agents with Large Language Models (LLMs) and compare our work against
empirical data.
2 Related Work
Bot simulation and ModelingRecent social bot simulation studies have used the Agent-Based
Modeling (ABM) technique to examine how automated accounts influence opinion dynamics and
polarization in digital societies. For example, the X feed modeled as a discrete event simulation can
explore the emergent behavior of two bot-based disinformation maneuvers, bridging and backing,
which revealed that bots are only effective when correctly embedded in the network Beskow and
Carley [2019]. Further, Averza et al. [2022] evaluates how the beliefs of agents can be influenced
in an X network with malicious users that spread misinformation through an SIR-epidemiological
model setup.
However, these traditional agent-based models are linguistically static. The agents did not produce
or interpret languages, and therefore could not simulate conversational discourse. This gap moti-
vates the integration of LLMs into social simulations to endow agents with expressive, goal-directed
communication studies.
LLM-Based Social SimulationAdvances in LLM-based simulation have enabled realistic agent
communication and behavior synthesis. These social simulations range from dialog-driven (e.g.,
social interaction, question-answering, and game-based) to task driven (e.g., software develop-
ment) Mou et al. [2024]. Such simulations have crafted artificial societies with LLM-powered
agents that are capable of autonomous memory and planning, and demonstrate emergent social
behaviors Park et al. [2023]. OASIS is a social simulation that models the information propaga-
tion dynamics in X and the herd effect in Reddit with a total of one million agents Yang et al..
However, many existing LLM-based simulations lack the explicit modeling of social structure, role
differentiation and network-level interactions. Agents often operate in sandboxed contexts without
persistent relationships or inter-agent dependencies that mirror real-world social media dynamics.
Our work builds upon these foundations by introducing a framework of simulations of CSAs as
LLM-based agents embedded with personality traits and operational strategies that are situated in a
social network.
Persona-Driven Agent ModelingA growing thread integrates social personas with social simu-
lation, where the simulated agents are encoded with demographics, roles, goals and rhetorical style
so agents mimic reality. PersonaGym demonstrates this by assigning hundreds of distinct persona
profiles (e.g., age, occupation, cultural background) and prompting LLMs to act within the corre-
sponding role-based environments tailored to these personasSamuel et al. [2024]. In parallel, the
SOTOPIA environment operationalizes social scenarios like negotiation, exchange, persuasion and
so forth with a wide range of character profiles and relationshipsZhou et al. [2024]. Larger scale
work on generative agent simulations encoded over a thousand agents with data from qualitative
interviews enhanced with LLM-driven behavior modeling. We build on these strands of work to
create a heterogeneous social simulation with a diversity of cyber social agent archetypes.
3 Cyber Social Agent Personas
Our social simulation operationalizes sixteen empirically grounded Cyber Social Agent (CSA)
archetypes. The archetypes in this simulation express a nuanced categorization of behaviors and
rhetorical strategy, and reflect agent’s motivation and network effects. The personas are adapted
from [Ng and Carley, 2025a], and described briefly in Table 1.
2

Table 1: Cyber Social Agent Archetypes
Category Archetype Primary Function
General Executes broad, non-specialized automated
actions
Operational Tactic Amplifier Increases message reach through high fre-
quency shares
Repeater Replicates its existing content to reinforce nar-
ratives
Social Influencer Applies persuasive tactics (measured as influ-
ence maneuvers with Carley [2020])
Cyborgs Blends human input with automated posting
behavior
Bridger Connects distinct communities or network
clusters
Synchronized Coordinates with peer agents
Chaos Injects randomness or conflict to fragment dis-
course
Rhetorical Strategy Self-Declared Declares its automated status
Announcer Issues scheduled or periodic information re-
leases
Content Generator Creates original social media content
Information Corrector Detects and counter false information
Genre-Specific Focuses activity within a defined topical do-
main
Conversational Sustains dialogue or initiates discussion
Engagement Generator Evokes emotional responses and drive user en-
gagement
News Bot Delivers or aggregates timely news updates
4 Simulation Design
4.1 Simulation Setup
Persona ModelingThe persona modeling step creates the agents. A set of agents are created man-
ually. This manually generated set of agents are augmented with agents generated by an LLM using
the GPT-4.1-nano model. Some of these agents are annotated to be Leaders, which means that they
are more influential in the social network setup, and their posts will be more preferentially interacted
with. These agents are initialized with the following persona parameters: name, nationality, topics,
community, tone (i.e., authoritative, formal, casual, journalistic). Each agent is also initialized with
the following network parameters: leader flag (Li ∈0,1), action quotaN, action setsA, and posting
periods.
Network creationFrom the persona modeling step, each agentiis assigned a community label
gi ∈G(e.g., “Odrian fans”, “Ethalian fans”) and a leader flagL i ∈0,1. We generate the initial
undirected social network as a graph by sampling each potential edge(i, j), i̸=j, from a mixture of
three attachment mechanisms: (1)π com, linear preferential-attachment within community, (2)πlead,
attachment to community leaders, and (3)π rand, uniform random attachment to other agents in the
network. In our simulation, the mixture weights are:π com = 0.70, πlead = 0.30, πrand = 0.10.
The edge probability is then represented in Equation 1.
Pr(i→j) =π com
1{gj =g i}k jP
u̸=i 1{gu =g i}k u | {z }
within community (preferential by degree)
+π lead
1{Lj = 1}wjP
u̸=i 1{Lu = 1}wu | {z }
attach to leaders (by leader weight)
+π rand
1
N−1| {z }
uniform random
.
(1)
3

Figure 1: Illustration of a section of the resultant simulated network, where Cyber Social Agents
interacted with a human agent.
wherek j is the current degree of nodej(usek j = 1at initialization),w j ≥1is the leader weight
(e.g.,w j =η >1ifL j = 1, otherwise0), andg i denotes the community label of agenti. Self-loops
are disallowed (i̸=j).
4.2 Simulation
Agent ActivationEach simulated actor follows a probabilistic behavioral rule that is either time-
defined or drawn from a geometric distribution, reflecting the stochastic posting rhythm of social
agents. This is reflected in Equation 2.
Ai(t)∼Bernoulli

pi(t)

, p i(t) =p(0) i ϕi(t)1{Ci(t)< Ni}.(2)
wherep (0) i ∈(0,1)is the baseline activation probability,ϕ i(t)∈[0,1]is a fatigue factor,C i(t) =P
s≤t Ai(s)is the cumulative number of activations up to timet,N i is the pre-defined action quota
for agenti. If the agent is a CSA,ϕ i(t) = 0, i.e. does not experience fatigue.
Two CSAs have special activation formula. First, Cyborgs use an alternating activation, reflected in
Equation 3, which means that they post like humans in some intervals, then post like a General CSA
in other intervals.
Ai(t) =1

(t−t i,0)≡0 (modT i)

1{Ci(t)< Ni}.(3)
wheret i,0 is the start time of activation,Ti >0is the posting period that defines the interval between
activations,C i(t) =P s≤t Ai(s),N i is the pre-defined action quota for agenti.
Announcers also have a special activation formula. Announcers have scheduled posting patterns,
reflected in Equation4.
Ai(t) =1
n
t∈

ti,0 +k Ti :k∈N 0
	 o
1{Ci(t)< Ni }.(4)
wheret i,0 is the start time,T i >0is the posting period at a fixed interval,C i(t) =P s≤t Ai(s),N i
is the pre-defined action quota for agenti.
4

Agent ActionAn active agent contributes content on social media, through constructing an origi-
nal post, retweeting or replying to a post. The agents personas have pre-defined their action setsA.
For example, for the Announcer,A={retweet}, for the Repeater,A={original post}. Further,
given an overall activity rateλthat is set for the simulation, human agents will perform1×λactions
while CSAs will perform2×λactions.
Topic SelectionEach agent’s probability of responding to a topic is determined by both its intrinsic
preferences and the topic’s popularity. The intrinsic preferenceκ i(j, t)combines the agent’s seeded
narrative, its memory of recent interactions, and any genre-specific bias. This preference is then
modulated by a popularity term(pop j(t) +δ)γ, producing a preferential attachment effect where
popular topics attract more attention. The resulting probabilities are normalized across all topics so
that each agent selects exactly one topic per activation step. The probabilityP i(j|t)that agenti
responds to or engages with topicjat timetis represented in Equation 5.
Pi(j|t) =π seed
πnar i,jP
k∈T πnar i,k| {z }
seeded narrative preference
+π mem
Mi,j(t)P
k∈T Mi,k(t)| {z }
memory of recent interactions
+π pop
(popj(t) +δ)γ P
k∈T (popk(t) +δ)γ | {z }
topic popularity
.
(5)
whereπ seed, πmem, πpop ≥0are coefficients of the relative importance of the seeded narrative,
recency-based memory, and topic popularity components. In our simulation runs, .π seed +π mem +
πpop = 1.π nar i,j represents the narrative prior describing how strongly agentiwas seeded with topic
j;M i,j(t)is a decaying memory term capturing how recently agentiinteracted with topicj; and
popj(t)denotes the overall popularity of topicjat timet, modulated by(pop j(t) +δ)γ to produce
a preferential-attachment effect. Here,δ >0is a smoothing constant that avoids zero probabilities,
andγ >0controls the sensitivity of agents to topic popularity.
There are Cyber Social Agents that only tweet on a single topic. The Genre-Specific agent focuses
its activity on a single topic domain, and only interacts with posts on its seeded topics, as represented
in Equation 6.
Pi(j|t) = 1{j∈ Gi}P i(j|t)X
k∈T
1{k∈ Gi}P i(k|t)
.(6)
whereG i⊆ Tis agentitopic setT.
Post text generationWhen an agent performs an action that requires text generation (i.e., original
post, reply, quote), the message text is generated using the GPT-4.1-nano LLM. The LLM is condi-
tioned on the agent’s persona, the topic selected and other persona parameters. An example of the
prompt used is:
You are a bot on X, with a persona of (persona description).
You will be posting on the following narrative (narrative
description). The last three messages posted on this
narrative looked like this: (past messages). In keeping
with your persona, please make your post sound like (tone).
We also performed experiments with variations of the prompt and compared the linguistic structure
of resultant texts with empirical data. We found that providing examples to the LLM produces more
realistic posts Ng and Carley [2025c].
5 Case Study
We based our simulation on the AuraSight scenario. The AuraSight scenario depicts the online
conflict between the online fans and detractors of the winner of a song-writing contest, Oliver. In
this work, we simulate the discourse in X. We urge the reader to read the full scenario and setup of
5

Figure 2: All-Communication social network at Day 1 and Day 30 of the simulation. Day 30 has
more clusters of users. Red nodes represent Cyber Social Agents, grey nodes represent humans.
communities in [Ng et al., 2025]. We manually constructed 110 human agents and 107 Cyber Social
Agents, then generated 219,854 human agents and 94,173 Cyber Social Agents. We ran the social
simulation process for 30 days.
5.1 Results
As preliminary results, we plot the all-communication network at Day 1 and at Day 30, and per-
formed face validation of the simulated network.
All-Communication NetworkLet the agents in the network beV={1, ..., N}. Let the interac-
tion actions be the setA={retweet,quote,reply}.
Then, the undirected, time-aggregated All-Communication network of a social graph over a time
window[t 0, t1]as the total number of interaction events is defined in Equation 7.
wij =
X
a∈A
αa

 X
t∈[t0,t1]

E a i→j(t)

 +

E a j→i(t)


 ,(7)
whereE a i→j(t)denotes events of typeafrom agentito agentjat timet. Links between agents
vi andv j represent interactions and are weighted through min-max scaling normalizationα a =
fa −min(f)
max(f)−min(f) .
Figure 2 shows the All-Communication network at Day 1 and Day 30 of the simulation. There are
clusters of users and a larger diversity of topics in Day 30.
ValidationWe mainly performed face validation of the output from the simulation against styl-
ized facts calculated from a year-long dataset of tweets obtained from the discussion on X on the
coronavirus pandemic from 2020-2021Ng and Carley [2025b].
6 Discussion and Conclusions
This work models and simulates persona-driven Cyber Social Agents using an LLM-Augmented
Agent-Based Modeling approach. This simulation demonstrates the diversity of roles that automated
agents can take and the emergent communication structures that emerge. Over the 30-day time
simulation period, the network emerge to have larger clusters of users and more diverse topics.
Many of the simulated behavioral metrics align closely with empirical stylized facts from large-scale
social media datasets, providing face validation for the model’s realism. This findings highlight the
importance of modeling automated agents as heterogeneous, personality-driven actors, and the use
of LLM-augmented social simulation bridges linguistic expressiveness with network realism.
6

Archetype Stylized Facts Simulated Values
GeneralCSAs perform2×λactions General CSA:Human tweet ra-
tio=2.01
Mann-Whitney U test p-value =
0.003<0.05
AmplifierA={retweet}Median number of retweets = 2
RepeaterA={original post}
A few tweets of each agent have
same content
Repeaters:human tweet ratio =
48.74
Mann Whitney U test p-value=
6.40E−262<0.001
Avg number of similar messages
per agent = 3
Social Influencer Uses 4 times influence maneu-
vers compared to humans
Avg influence maneuvers used
by Social Influencer:Human =
1.59
CyborgsAlternate between human and
General CSA behavior everyn
hours
Alternates behavior every 0.7
hours
BridgerA{original post, quote, reply}
Tags people from multiple com-
munities
Avg number of retweets = 0.60
Avg number of mentions = 25.0
% that tag people from multiple
communities = 100
Synchronized
Chaos Uses 4 times influence maneu-
vers compared to humans
Erratic posting schedule
Avg influence maneuvers used
by Social Influencer:Human =
1.59
Self-DeclaredIndicates automation in use
metadata
For uses with word “bot” in
metadata, Self-Declared:human
tweet ratio = 41.06
AnnouncerPost only everynhours Periodic posting checked by
variation in time difference in in-
tervals of posting
Content Generator
Information Corrector References fact-checking URL
websites
% that reference fact-checking
URL websites and corrects facts
= 0.30
Genre-SpecificConsistent topic selected for
posting
Avg number of topics by seman-
tic similarity = 1.4
ConversationalA=
{original post, quote, reply}
Avg number of topics by seman-
tic similarity = 4.0
Engagement Generator High use of emotional cues Avg number of words related to
emotions = 1.3
News Bot Posts new headlines
References news URLs
% of tweets that reference news
websites = 20
Table 2: Validation of Behavior of Cyber Social Agents against empirical data.Boldmeans that the
simulated values matches the stylized facts.
Modeling AssumptionsThere are several assumptions made in this work during the modeling of
agents. Agent activation are approximated by probabilistic rules likes Bernoulli processes and fixed
intervals, and while these abstractions estimate the online rhythm of posting activities, they omit
micro-level cognitive factors like attention, fatigue recovery or feedback adaptation. Second, the
agents operate in a closed system with a fixed topology, and link decay and exogenous events are
not modeled. These assumptions balance computational tractability with interpretability, but future
work should relax them to simulate more open-ended and evolving environments.
7

Future Work and ApplicationsThis persona simulation offers a foundation for studying infor-
mation diffusion, influence operations and intervention design in digital societies. By embedding
rhetorical realism into agent-based networks, this system can be used to explore how CSAs am-
plifies or mitigates misinformation campaigns, test countermeasures such as injecting information
correction bots or simulate narrative evolution.
ConclusionBy modeling the nuances of persona-driven Cyber Social Agents, our work combines
theoretical and empirical understanding of digital actors into a scalable and realistic social simula-
tion. This provides a foundation for the analysis of information diffusion on platforms, the design
and testing of interventions, and the formulation of policies for digital governance research.
AcknowledgementsThis material is based upon work supported by the Scalable Technologies
for Social Cybersecurity, U.S. Army (W911NF20D0002), the Threat Assessment, Office of Naval
Research (N000142412414), and Community Assessment Techniques for Digital Data, Office of
Naval Research (N000142412568), and ACTAINS, Office of Naval Research (N000142612511).
The views and conclusions contained in this document are those of the authors and should not
be interpreted as representing official policies, either expressed or implied by the Office of Naval
Research, U.S. Army or the U.S. government.
References
Aldo Averza, Khaled Slhoub, and Siddhartha Bhattacharyya. Evaluating the influence of twitter bots
via agent-based social simulation.IEEE Access, 10:129394–129407, 2022.
David M Beskow and Kathleen M Carley. Agent based simulation of bot disinformation maneuvers
in twitter. In2019 Winter simulation conference (WSC), pages 750–761. IEEE, 2019.
Kathleen M Carley. Social cybersecurity: an emerging science.Computational and mathematical
organization theory, 26(4):365–381, 2020.
Kadhim Hayawi, Susmita Saha, Mohammad Mehedy Masud, Sujith Samuel Mathew, and Mo-
hammed Kaosar. Social media bot detection with deep learning methods: a systematic review.
Neural Computing and Applications, 35(12):8903–8918, 2023.
McKenzie Himelein-Wachowiak, Salvatore Giorgi, Amanda Devoto, Muhammad Rahman, Lyle
Ungar, H Andrew Schwartz, David H Epstein, Lorenzo Leggio, and Brenda Curtis. Bots and
misinformation spread on social media: implications for covid-19.Journal of medical Internet
research, 23(5):e26933, 2021.
Quanxin Jia, Wujiong Ren, et al. Social bots as information amplifier: Influence of social bots on
information dissemination regarding bucha event. SSRN Working Paper, 2024.
Xinyi Mou, Xuanwen Ding, Qi He, Liang Wang, Jingcong Liang, Xinnong Zhang, Libo Sun, Jiayu
Lin, Jie Zhou, Xuanjing Huang, et al. From individual to society: A survey on social simulation
driven by large language model-based agents.arXiv preprint arXiv:2412.03563, 2024.
Lynnette Hui Xian Ng and Kathleen M Carley. Botbuster: Multi-platform bot detection using a
mixture of experts. InProceedings of the international AAAI conference on web and social media,
volume 17, pages 686–697, 2023a.
Lynnette Hui Xian Ng and Kathleen M Carley. Deflating the chinese balloon: types of twitter bots
in us-china balloon incident.EPJ Data Science, 12(1):63, 2023b.
Lynnette Hui Xian Ng and Kathleen M Carley. The dual personas of social media bots.arXiv
preprint arXiv:2504.12498, 2025a.
Lynnette Hui Xian Ng and Kathleen M Carley. A global comparison of social media bot and human
characteristics.Scientific Reports, 15(1):10973, 2025b.
Lynnette Hui Xian Ng and Kathleen M Carley. Are llm-powered social media bots realistic? In
International Conference on Social Computing, Behavioral-Cultural Modeling and Prediction
and Behavior Representation in Modeling and Simulation, pages 14–23. Springer, 2025c.
8

Lynnette Hui Xian Ng, Dawn C Robertson, and Kathleen M Carley. Cyborgs for strategic commu-
nication on social media.Big Data & Society, 11(1):20539517241231275, 2024.
Lynnette Hui Xian Ng, Bianca NY Kang, and Kathleen M Carley. Aurasight: generating realistic
social media data.arXiv preprint arXiv:2509.08927, 2025.
Lynnette HX Ng and Araz Taeihagh. How does fake news spread? understanding pathways of
disinformation spread through apis.Policy & Internet, 13(4):560–585, 2021.
Mariam Orabi, Djedjiga Mouheb, Zaher Al Aghbari, and Ibrahim Kamel. Detection of bots in social
media: a systematic review.Information Processing & Management, 57(4):102250, 2020.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and
Michael S Bernstein. Generative agents: Interactive simulacra of human behavior. InProceedings
of the 36th annual acm symposium on user interface software and technology, pages 1–22, 2023.
Vinay Samuel, Henry Peng Zou, Yue Zhou, Shreyas Chaudhari, Ashwin Kalyan, Tanmay Rajpuro-
hit, Ameet Deshpande, Karthik Narasimhan, and Vishvak Murahari. Personagym: Evaluating
persona agents and llms.arXiv preprint arXiv:2407.18416, 2024.
Kai Shu, Amrita Bhattacharjee, Faisal Alatawi, Tahora H Nazer, Kaize Ding, Mansooreh Karami,
and Huan Liu. Combating disinformation in a social media age.Wiley Interdisciplinary Reviews:
Data Mining and Knowledge Discovery, 10(6):e1385, 2020.
Haolin Wang, Qingpeng Zhang, Mary Ip, and Joseph Tak Fai Lau. Social media–based conversa-
tional agents for health management and interventions.Computer, 51(8):26–33, 2018.
Ziyi Yang, Zaibin Zhang, Zirui Zheng, Yuxian Jiang, Ziyue Gan, Zhiyu Wang, Zijian Ling, Martin
Ma, Bowen Dong, Prateek Gupta, et al. Oasis: Open agents social interaction simulations on one
million agents. InNeurIPS 2024 Workshop on Open-World Agents.
Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong Zhang, Haofei Yu, Zhengyang Qi, Louis-Philippe
Morency, Yonatan Bisk, Daniel Fried, Graham Neubig, and Maarten Sap. SOTOPIA: Interactive
evaluation for social intelligence in language agents. InThe Twelfth International Conference on
Learning Representations, 2024. URLhttps://openreview.net/forum?id=mM7VurbA4r.
9
