---
title: 'EconSimulacra: A Digital Twin Platform of Socio-Economic Systems Powered by LLM Agents'
url: https://arxiv.org/abs/2606.26883
category: consumer-behavior
subcategory: case-study
date: 2026-06
venue: arXiv (Cornell University)
authors:
- Ryuji Hashimoto
- Masahiro Kaneko
- Kentaro Ueda
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.26883
pages: 10
chars: 41055
fetched_at: '2026-11-08T12:57:29+00:00'
kb_version: 1
---

# EconSimulacra: A Digital Twin Platform of Socio-Economic Systems Powered by LLM Agents

EconSimulacra: A Digital Twin Platform of Socio-Economic Systems
Powered by LLM Agents
Ryuji Hashimoto1,2, Masahiro Kaneko1,3, Kentaro Ueda1, Takehiro Takayanagi1,2, Kiyoshi Izumi1,2
1Simulacra Inc., 2The University of Tokyo, 3MBZUAI.
Correspondence:r_hashimoto@simulacra.co.jp
Abstract
Real-world social behavior emerges from
tightly coupled domains: economic conditions
shape mobility and social interactions, while
online attention and offline activity feed back
into local popularity and consumer behavior.
Capturing these feedback loops requires arti-
ficial societies in which agents carry experi-
ences from one domain into decisions in an-
other. Large language models (LLMs) pro-
vide a promising foundation for such societies.
However, existing LLM-based simulators typ-
ically model domains in isolation or merely
place them side by side. To enable such cross-
domain interactions, we present EconSimu-
lacra, a multi-agent social simulator that cou-
ples consumer economy, mobility, and social
networks through a shared internal-state mech-
anism. In EconSimulacra, experiences accu-
mulated across different domains are stored
in memory and transformed into shared inter-
nal states (i.e., stress level) connecting hetero-
geneous domains through individual decision
making. This design allows agents to recon-
cile competing demands arising from multiple
domains and generate coherent cross-domain
behaviors. A case study shows that the shared
internal state mechanisms reproduce a nonlin-
ear relationship between online social attention
and offline local popularity, illustrating how
realistic cross-domain dynamics can emerge
within a unified artificial society. The source
code1, package2, documentation3, live demo4,
and instruction movie 5 are publicly available.
1 Introduction
Understanding socioeconomic systems can benefit
from considering the interactions among multiple
co-evolving social dynamics rather than treating
1https://github.com/SimulacraBusiness/econsimulacra
2https://pypi.org/project/econsimulacra/
3https://simulacrabusiness.github.io/econsimulacra/
4https://econsimulacra.onrender.com
5https://www.youtube.com/watch?v=tGTWAbAN5m8
each domain in isolation (Holling, 2001; Padgett
and Powell, 2012). Socioeconomic systems are
complex adaptive systems in which diverse do-
mains, such as economic activity, social networks,
and human mobility, evolve simultaneously and
influence one another (Epstein and Axtell, 1996).
To this end, large language models (LLMs) pro-
vide a promising foundation for building multi-
domain artificial societies. Conventional agent-
based models often rely on manually designed rules
tailored to each individual domain, making it dif-
ficult to coordinate multiple interacting domains
within a single framework (Chopra et al., 2025).
In contrast, LLMs can naturally integrate diverse
inputs through a shared natural-language represen-
tation and generate decisions that holistically ac-
count for these heterogeneous factors (Ma et al.,
2024; Gao et al., 2024). This capability offers a
flexible way to model and couple heterogeneous
social dynamics within a single artificial society.
However, existing LLM-based social simula-
tions either focus on a single domain (Mou et al.,
2024; Li et al., 2024) or merely place multiple do-
mains within a common environment (Park et al.,
2023; Zhang et al., 2025). The mere coexistence of
multiple domains does not necessarily imply inter-
action between them. For cross-domain dynamics
to emerge, experiences acquired in one domain
must influence behavior in another domain through
some shared decision-making process. In real soci-
eties, such cross-domain influences are often medi-
ated by internal states arising from physical and so-
cial constraints. For example, hunger accumulated
through consumption decisions can motivate mobil-
ity toward stores, while congestion experienced dur-
ing travel may subsequently influence social-media
activity. Individuals integrate experiences from dif-
ferent domains while balancing physical or social
constraints (Kruglanski et al., 2002; Hägerstrand,
1970). Although prior work (Bougie and Watanabe,
2025) has introduced memories and needs, these
arXiv:2606.26883v2  [cs.DL]  30 Jun 2026

Consumer Economy Social Network
Agent
Memory
Stress Level
Experiences from multiple domains
observations
action history
...
hunger
econ. state
...
•price change
•inventory
•economicstate
•sales promotion
•trends
•location
•travel cost
•crowd
Mobility
Balance multiple objectives
and generate actions
feel hungry...
need to save money...
head to
DairyMart!
Macroscopic phenomena emerge
from coupled interactions across domains
Macro Phenomena
Nonlinear relationship
viral trend
→ actual visits
→ crowd / sales
→ opinion disagreement
→ ...online attention
EconSimulacra
sales
Actions in Each Domain
consume
goods
place
an order
post /
(un) follow
move
sleep
Figure 1: Overview of EconSimulacra. Agents continuously accumulate heterogeneous experiences from the
consumer economy, social networks, and mobility domains. These experiences are stored in memory and transformed
into shared internal states (i.e., stress level), which guide decisions across domains. The resulting cross-domain
interactions generate emergent macroscopic phenomena, such as nonlinear online–offline coupling.
mechanisms have primarily been used to improve
realism within individual domains rather than to
generate interactions across domains.
We hypothesize that cross-domain dynamics in
LLM societies emerge when heterogeneous experi-
ences are integrated through a shared internal repre-
sentation. To enable the study of such cross-domain
interactions, we propose EconSimulacra, a multi-
domain social simulator that couples consumer
economy, mobility, and social networks through
stress level-based internal states. Agents accumu-
late experiences across domains in memory, from
which stress levels are computed and used as a
shared representation of competing demands.
Our experiments demonstrate that introducing
stress levels strengthens interactions among hetero-
geneous social domains and enables the emergence
of realistic cross-domain dynamics. In particular,
the proposed framework reproduces the nonlinear
relationship between online social media activity
and offline local popularity, a stylized fact observed
in real-world socioeconomic systems (Gong et al.,
2025). Ablation experiments further show that re-
moving the stress level-based coupling mechanism
weakens these emergent patterns. These findings
support the hypothesis that shared internal repre-
sentations can serve as coupling mechanisms for
multi-domain artificial societies.
Configuration Structure
{
"simulation": {...},
"environment": {...},
"<componentName>": {...},
...
}
Figure 2: Structure of the JSON-based configuration
file. The configuration specifies the overall simulation
settings and environment composition, followed by the
definitions of individual components such as agents,
spaces, social networks, items, events, and services.
2 EconSimulacra Architecture
EconSimulacra is an open-source framework for
building LLM-based multi-domain social simula-
tions. The framework can be installed via pip and
is designed to simplify the development of cou-
pled social simulations. As illustrated in Figure 1,
the system is organized into two primary layers:
(i) Multi-domain Environments, which model indi-
vidual domains such as consumer economy, social
networks, and mobility, and(ii) the Agent Layer,
where LLM-based agents maintain memories of
past observations and action histories, convert expe-
riences from multiple domains into a unified stress
level representation, and generate actions based on
these internal states.
Simulation scenarios are defined declaratively

EconSimulacra Simulation Loop
env = Environment(config)
env.reset(seed=42)
num_steps:int
for_in range(num_steps):
all_actions = {}
foragent_idinenv.agent_ids:
agent = env.agent_id2agent[agent_id]
obs = env.get_observations(agent_id )
action = agent.act(obs)
all_actions[agent_id ] = action
env.step(all_actions)
Figure 3: Simplified execution flow of a simulation. At
each step, agents receive observations from the envi-
ronments, generate actions, and the environments are
updated based on the joint actions of all agents.
through a JSON-based configuration file. Figure 2
shows the simplified structure of a configuration
file. The simulation and environment sec-
tions specify the global simulation settings and
the composition of the virtual world, while the re-
maining sections define the individual components
(e.g., spaces, social networks, agents, items, events,
and services such as LLM API clients and prompt
management modules). Since all components are
instantiated by name from the configuration, users
can seamlessly integrate newly implemented mod-
ules alongside the built-in ones without changing
the core implementation.
A simulation proceeds by repeatedly collecting
observations from the environments, querying each
agent for its actions, and updating the environment
states based on their actions. Figure 3 summa-
rizes the overall execution flow. In addition to the
Python API, EconSimulacra provides an interactive
demonstration interface that enables users to visual-
ize simulation dynamics and inspect the behaviors
of individual agents and macroscopic system states.
Multi-domain EnvironmentsEconSimulacra
models different aspects of social and economic
activities as independent environment modules.
Each environment maintains its own state transition
rules and provides domain-specific observations to
agents, while receiving agents’ actions to update
the underlying world state. This modular design
enables multiple domains to interact within a uni-
fied simulation while preserving the flexibility to
develop and extend each domain independently.
Figure 1 illustrates the three representative environ-
ments currently implemented in the framework.
• Consumer Economy:models purchasing ac-
tivities and retail markets, providing observa-
tions such as product prices, inventories, and
economic conditions.
• Social Network:represents online interactions
and information diffusion, including posts, trend-
ing topics, sales promotions, and follow/unfol-
low relationships.
• Mobility:captures physical movement and lo-
cation choices, exposing information such as
destinations, travel costs, and local crowd levels.
At each simulation step, environment modules ex-
pose their observations to agents, and subsequently
update their internal states according to the actions
returned by the agents. Since all environments
follow a common interface, new domains can be
incorporated by implementing the corresponding
observation and transition functions without modi-
fying the existing simulation framework.
Agent LayerLLM-based agents serve as the
decision-making entities in EconSimulacra by in-
tegrating observations from multiple domains and
generating actions accordingly. As illustrated in
Figure 1, each agent maintains two internal states:
MemoryandStress Levels. TheMemorymodule
stores a summarized representation of the agent’s
past experiences across domains, including obser-
vations and action histories. TheStress Levelmod-
ule provides a unified internal representation that
couples heterogeneous domains. Rather than di-
rectly exposing all environment-specific variables
to the decision-making process, observations and
action histories stored in memory are transformed
into a set of interpretable stress levels through rule-
based functions. The framework currently provides
several built-in stress level models:
• Hunger:computed from the gap between calo-
rie intake and a target nutritional requirement,
where each item can be associated with a calorie
value.
• Fatigue:computed from accumulated travel dis-
tance, with stress level alleviation when agents
remain at their designated home locations.
• Economic State:computed from both absolute
and relative shortages of available cash and from
decreases in owned assets.
• Sleep:computed from insufficient sleep dura-
tion and irregular sleep rhythms.
• Congestion:computed from the local popula-
tion density around the agent’s current location.
Since stress levels are derived from memories
through modular rule-based functions, the frame-
work can be easily extended with additional in-

ternal drives and domain-specific objectives. The
resulting stress level representation enables hetero-
geneous information from different domains to be
handled in a common format, facilitating cross-
domain interactions within the agent.
At every simulation step, the LLM receives the
summarized memories, current stress levels, and
the latest environmental observations, and performs
natural-language reasoning to balance multiple
objectives, such as satisfying hunger, conserving
money, reducing travel costs, or avoiding conges-
tion. The output is a set of executable actions that
can be directly applied to the corresponding en-
vironments, including consuming goods, placing
orders, posting or following users on social net-
works, moving between locations, and sleeping.
Interactive DemoEconSimulacra provides an
interactive demonstration interface for visualizing
and exploring simulation dynamics. As shown in
Figure 4, the interface allows users to inspect the
states of individual domains, such as the grid-based
environment, the social network, and macroeco-
nomic indicators, while simultaneously monitoring
the internal states and decision-making processes
of individual agents. Users can interactively ex-
amine agent attributes, memories, stress levels, in-
ventories, and action histories, enabling a detailed
understanding of how micro-level decisions emerge
from multi-domain experiences. The interface also
supports step-by-step playback of simulations, fa-
cilitating the analysis and debugging of complex
cross-domain interactions.
3 Experiment
To demonstrate the ability of EconSimulacra to
capture cross-domain interactions, we examine
whether coupling among the social network, mo-
bility, and consumer economy domains reproduces
the nonlinear relationship between online social
attention and offline consumer activity reported in
empirical studies (Gong et al., 2025). We test the
following hypotheses:
• H1:The interaction between online attention
and offline consumer activity exhibits a nonlin-
ear relationship.
• H2:This relationship emerges fromstress level-
couplingacross the three domains.
To validate the underlying mechanism, we per-
form an ablation study by comparing two simu-
lation settings: (i) the full EconSimulacra model,
(a) Grid space
(b) Social network
Figure 4: Representative views of the interactive demon-
stration interface showing (a) agents and physical inter-
actions in grid space, and (b) online communication and
information diffusion in the social network.
where agents accumulate stress levels through expe-
riences across multiple domains and use it for sub-
sequent decision making, and (ii) a stress-disabled
variant, where domain-specific experiences do not
influence future behaviors through the internal
stress levels. By comparing these two conditions,
we evaluate whether stress level-coupling is nec-
essary for reproducing the nonlinear coupling be-
tween virtual and real spaces.
Simulation SetupsWe construct a simplified ar-
tificial society consisting of household agents, a
rule-based restaurant, and a retailer. The simula-
tion takes place in a grid world, where household
agents repeatedly make decisions. As an exoge-
nous intervention, the restaurant launches a pre-
defined discount campaign during a fixed period.
Table 1 summarizes the key simulation parame-
ters. The complete experimental configuration, in-
cluding simulation settings and execution scripts,
is publicly available in the EconSimulacra reposi-
tory.6 The experiments reported in this paper can
be reproduced using the provided configuration
files and scripts. The hardware and software con-
figurations used in the experiment are summarized
6https://github.com/SimulacraBusiness/econsimulacra/tree/
main/examples/vllm

Category Configuration
Simulation period 216 steps (1 hour per step)
Grid space10×10grid world
Social network Follow cap = 5
Date time Dec. 19 09:00 – Dec. 28 09:00
Household agents 30
Restaurant 1 (Pizza Place, rule-based)
Retailer 1 (Daily Mart, LLM)
Restaurant products Pizza, Soda
Retailer products Rice, Bread, Salad, Soup
Event 40% pizza discount (Dec. 23–25)
Social campaign Restaurant promotional posts
Table 1: Simulation setup.
in Appendix A.
In the experiment, we conduct 10 indepen-
dent simulation runs with different random seeds
for each of the following LLMs: GPT-OSS-
20B (OpenAI, 2025), GPT-OSS-120B (OpenAI,
2025), Llama 3.1 70B Instruct (Meta, 2024), and
Qwen3.6-35B-A3B (Team, 2025).
Stress Level-Coupling AblationTo investigate
the mechanism underlying the emergence of non-
linear online–offline dynamics, we conduct an ab-
lation study by comparing the following two simu-
lation settings. Both settings share the same simu-
lation environment and differ only in whether past
experiences are accumulated as internal stress lev-
els that influence future decision making.
• EconSimulacra (full).Agents accumulate expe-
riences across multiple domains as internal stress
variables, which subsequently influence future
decision making. Consequently, experiences in
one domain can indirectly affect behaviors in
other domains through the shared internal state.
• EconSimulacra (w/o stress level).Agents inter-
act with the same environment and perform the
same actions as in the full model, but the stress-
level abstraction is removed. Instead of main-
taining integrated internal stress states, agents di-
rectly receive the raw experience histories from
each domain. The aggregation and prioritization
of these heterogeneous experiences are therefore
left entirely to the LLM during decision making.
By comparing these two conditions, we evaluate
whether stress-mediated memory is necessary for
reproducing the nonlinear coupling between online
attention and offline consumer activity.
Evaluation MetricsWe quantify the coupling be-
tween online attention and offline consumer activity
for the restaurant (Pizza Place) using the notions
ofonline heatandoffline heat(Gong et al., 2025).
In our setting, the offline heat Hoffline ∈R ≥0, is
defined as the daily sales of Pizza Place, while the
online heat Honline ∈R ≥0, is defined as the daily
number of social media posts containing the key-
word “pizza.” To evaluate whether the simulation
reproduces the nonlinear relationship observed in
real-world online–offline interactions, we fit the
following quadratic regression model:
Hoffline =aH 2 online +bH online +c.(1)
Here, a∈R represents the strength of thesatura-
tion effect, capturing the decrease in offline activity
due to factors such as congestion, while b∈R rep-
resents the strength of theonline attention effect,
reflecting the positive impact of social attention on
consumer visits. Based on empirical findings, we
expect the simulation to exhibita <0andb >0.
In addition, we examine the relationship between
the volume and diversity of online opinions by com-
puting the Pearson correlation coefficient between
the daily number of “pizza”-related posts and the
standard deviation of their sentiment scores. The
sentiment score of each post is estimated using
the RoBERTa-based sentiment classifier (Barbieri
et al., 2020). We hypothesize that periods of height-
ened online attention are accompanied by a greater
diversity of consumer experiences and opinions,
resulting in a positive correlation between online
heat and sentiment dispersion.
4 Results and Discussion
Table 2 provides quantitative evidence supporting
H1. Across all tested LLM backbones, the full
model consistently exhibits a negative quadratic
coefficient (a <0 ), a positive linear coefficient
(b >0 ), and a positive correlation between the
volume of online discussions and the diversity of
sentiment. The comparison between the full model
and the ablated variant further supportsH2. When
the stress-level mechanism is removed, the negative
quadratic coefficient becomes substantially weaker,
and the correlation between online discussions and
sentiment diversity is also greatly reduced. These
findings indicate that the nonlinear relationship
does not emerge merely because multiple domains
coexist, but because information from the social
network, mobility, and consumer economy is cou-
pled through the shared internal representation.
A representative cross-domain feedback loop ob-
served in our simulation illustrates the mechanism

full w/o stress level
Modela b R 2 Corra b R 2 Corr
GPT-OSS-120B−0.337 ∗∗ 1.120∗∗ 0.433 0.214 ∗ 0.240 0.475 0.400 0.034
GPT-OSS-20B−0.337 ∗∗ 0.451∗∗ 0.349 0.201 ∗ 0.003 0.911 ∗∗ 0.712−0.323
Llama 3.1 70B Instruct−0.416 ∗∗ 0.573∗∗ 0.589 0.470 ∗∗ 0.129 0.496 ∗ 0.235−0.010
Qwen3.6-35B-A3B−0.085 ∗ 0.621∗∗ 0.374 0.377 ∗∗ 0.042 0.625 ∗∗ 0.428 0.190 ∗
Table 2: Comparison between the EconSimulacra (full) and an ablated variant without stress-level mechanism (w/o
stress level).Note.* p<0.05, ** p<0.01,
underlying this result. Promotional information
disseminated through the social network attracts
customers to a restaurant, changing real-world pur-
chasing and mobility patterns. The resulting experi-
ences, including both positive experiences (e.g., dis-
counted purchases) and negative ones (e.g., conges-
tion), are reflected in agents’ stress levels and subse-
quently influence future online discussions. These
updated discussions further amplify or suppress
later visits, creating intertwined positive and neg-
ative feedback loops spanning the social-network,
mobility, and consumer-economy domains. Quali-
tative examples of these processes are provided in
Appendix B. Together, these quantitative and qual-
itative findings suggest that stress-level coupling
serves as an effective mechanism for integrating
heterogeneous domain-specific constraints, provid-
ing a practical design principle for constructing
coupled multi-domain social simulations.
5 Related Work
LLM-based Social SimulationsRecent stud-
ies (Ma et al., 2024; Gao et al., 2024; Önder Gür-
can, 2024; Mou et al., 2026) demonstrate that
LLMs provide a foundation for social simulation.
Building on these capabilities, LLM-based social
simulations have rapidly expanded across a wide
range of domains. Existing studies have applied
LLM agents to simulate everyday human activi-
ties (Park et al., 2023), urban and city-scale dynam-
ics (Bougie and Watanabe, 2025), the emergence
of social norms (Ren et al., 2024), information dif-
fusion on social media (Mou et al., 2024; Zheng
and Tang, 2025), opinion formation (Chuang et al.,
2024; Hashimoto et al., 2026a), macroeconomic
behavior (Li et al., 2024), and financial market dy-
namics (Hashimoto et al., 2026b; Hirano, 2026).
Collectively, these studies highlight the versatility
of LLM agents as a common computational sub-
strate for modeling and integrating heterogeneous
social and economic domains.
A number of software frameworks have also
been developed to support LLM-based social simu-
lations in specific application domains. Representa-
tive examples include SmallVille for daily life and
social activities (Park et al., 2023), CAMEL (Li
et al., 2023), AgentSims (Lin et al., 2023), and So-
topia (Zhou et al., 2024) for conversational scenar-
ios, Agent Trading Arena for financial markets (Ma
et al., 2025), and OASIS (Yang et al., 2025) and
MOSAIC (Liu et al., 2025) for social media dy-
namics. More general-purpose platforms such as
Concordia (Vezhnevets et al., 2023) and AgentSoci-
ety (Zhang et al., 2025) provide reusable infrastruc-
tures for constructing LLM agent societies across
multiple tasks. However, these frameworks pri-
marily focus on modeling a single domain or inter-
action modality, and largely overlook the explicit
coupling of multiple social domains within a uni-
fied simulation environment.
6 Conclusion
We presented EconSimulacra, an open-source plat-
form for constructing LLM-based artificial so-
cieties with coupled consumer economy, mobil-
ity, and social-network dynamics. The platform
provides a unified framework in which domain-
specific observations are integrated into shared in-
ternal states and subsequently influence agents’ fu-
ture decisions. Through a case study of online–
offline interactions around restaurant promotions,
we demonstrated how localized events can propa-
gate across multiple domains and reproduce emer-
gent social phenomena. Our results suggest that
reproducing real-world social phenomena requires
not only modeling multiple domains, but also pro-
viding a mechanism that integrates heterogeneous
experiences and constraints into coherent cross-
domain feedback loops. We envision EconSimu-
lacra as a step toward a new paradigm in computa-
tional social science: moving beyond the isolated
analysis of individual domains toward the gener-
ative understanding of how interactions between
domains give rise to complex social dynamics.

Limitations
Limited Domain CoverageThe current imple-
mentation of EconSimulacra focuses on the inter-
actions among three domains: consumer economy,
mobility, and social networks. While these do-
mains already capture a variety of online–offline
feedback loops, many important components of
real-world societies remain outside the scope of
the present platform. In particular, labor markets
and financial markets represent natural extensions
that could introduce additional channels of inter-
action. Because the platform is designed around
modular environments and a shared coupling mech-
anism, we believe that incorporating such domains
can be achieved without fundamentally changing
the underlying architecture. Expanding the range
of modeled domains is therefore an important di-
rection for building more comprehensive artificial
societies.
Open Challenges in Cross-Domain Coupling
In the current implementation, cross-domain in-
teractions are mediated through a stress level-based
internal representation that aggregates heteroge-
neous experiences and constraints. While our re-
sults demonstrate that this mechanism is effective
for reproducing coupled online–offline dynamics,
stress level should be regarded as only one possi-
ble design choice rather than a universal solution.
More generally, identifying what kinds of shared
internal representations are most suitable for cou-
pling heterogeneous social domains remains an
open research question. We therefore view Econ-
Simulacra not only as a simulation platform but
also as a testbed for exploring and comparing gen-
eral mechanisms for cross-domain coupling in arti-
ficial societies.
Limited Scope of Empirical StudyThe case
study presented in this paper focuses on a specific
example of online–offline coupling around restau-
rant promotions, and therefore represents only a
small subset of the social phenomena that the plat-
form may support. Establishing the generality of
the proposed framework will require applying it
to a broader range of domains and validating the
resulting dynamics against diverse empirical ob-
servations. More fundamentally, we do not view
EconSimulacra as a complete model of society,
but rather as an experimental infrastructure for
studying how interactions among heterogeneous
domains generate complex social phenomena. We
hope that such LLM-based artificial societies will
complement conventional data-driven analyses by
enabling researchers to formulate, simulate, and
test generative hypotheses about cross-domain so-
cial dynamics.
References
Francesco Barbieri, Jose Camacho-Collados, Luis
Espinosa-Anke, and Leonardo Neves. 2020. TweetE-
val: Unified benchmark and comparative evaluation
for tweet classification. InFindings of the Associa-
tion for Computational Linguistics: EMNLP 2020,
pages 1644–1650.
Nicolas Bougie and Narimawa Watanabe. 2025.
CitySim: Modeling urban behaviors and city dynam-
ics with large-scale LLM-driven agent simulation. In
Proceedings of the 2025 Conference on Empirical
Methods in Natural Language Processing: Industry
Track, pages 215–229.
Ayush Chopra, Shashank Kumar, Nurullah Giray Kuru,
Ramesh Raskar, and Arnau Quera-Bofarull. 2025.
On the limits of agency in agent-based models. In
Proceedings of the 24th International Conference on
Autonomous Agents and Multiagent Systems, pages
500–509.
Yun-Shiuan Chuang, Agam Goyal, Nikunj Harlalka,
Siddharth Suresh, Robert Hawkins, Sijia Yang, Dha-
van Shah, Junjie Hu, and Timothy Rogers. 2024.
Simulating opinion dynamics with networks of LLM-
based agents. InFindings of the Association for Com-
putational Linguistics: NAACL 2024, pages 3326–
3346.
Joshua M. Epstein and Robert L. Axtell. 1996.Growing
artificial societies: Social science from the bottom
up. The MIT Press.
Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao
Ding, Zhilun Zhou, Fengli Xu, and Yong Li. 2024.
Large language models empowered agent-based mod-
eling and simulation: A survey and perspectives.
Humanities and Social Sciences Communications,
11(1):1259.
Yilu Gong, Sijia Han, and Jun Yang. 2025. Study on the
coupling and coordination degree of virtual and real
space heat in coastal internet celebrity streets.ISPRS
International Journal of Geo-Information, 14(10).
Maarten Grootendorst. 2022. BERTopic: Neural topic
modeling with a class-based TF-IDF procedure.
Preprint, arXiv:2203.05794.
Torsten Hägerstrand. 1970. What about people in re-
gional science?Papers of the Regional Science Asso-
ciation, 24(1):6–21.
Ryuji Hashimoto, Masahiro Kaneko, Ryosuke Takata,
Takehiro Takayanagi, and Kiyoshi Izumi. 2026a.
From heard to lived opinions: Simulating opinion

dynamics with grounded llm agents in economic en-
vironments.Preprint, arXiv:2603.26701.
Ryuji Hashimoto, Takehiro Takayanagi, Masahiro
Suzuki, and Kiyoshi Izumi. 2026b. Agent-based
simulation of a financial market with large language
models. InThe International Conference on Princi-
ples and Practice of Multi-Agent Systems (PRIMA
2025), pages 20–28.
Masanori Hirano. 2026. Building LLM-based artificial
market simulations: Can LLMs function as agents
in multi-agent simulations for finance? InThe Inter-
national Conference on Principles and Practice of
Multi-Agent Systems (PRIMA 2025), pages 56–71.
C. S. Holling. 2001. Understanding the complexity of
economic, ecological, and social systems.Ecosys-
tems, 4(5):390–405.
Arie W. Kruglanski, James Y . Shah, Ayelet Fishbach,
Ron Friedman, Woo Young Chun, and David Sleeth-
Keppler. 2002. A theory of goal systems. vol-
ume 34 ofAdvances in Experimental Social Psychol-
ogy, pages 331–378. Academic Press.
Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii
Khizbullin, and Bernard Ghanem. 2023. CAMEL:
Communicative agents for "Mind" exploration of
large language model society. InAdvances in Neural
Information Processing Systems, volume 36, pages
51991–52008.
Nian Li, Chen Gao, Mingyu Li, Yong Li, and Qing-
min Liao. 2024. EconAgent: Large language model-
empowered agents for simulating macroeconomic
activities. InProceedings of the 62nd Annual Meet-
ing of the Association for Computational Linguistics,
pages 15523–15536.
Jiaju Lin, Haoran Zhao, Aochi Zhang, Yiting Wu, Huqi-
uyue Ping, and Qin Chen. 2023. AgentSims: An
open-source sandbox for large language model evalu-
ation.Preprint, arXiv:2308.04026.
Genglin Liu, Vivian T. Le, Salman Rahman, Elisa
Kreiss, Marzyeh Ghassemi, and Saadia Gabriel. 2025.
Mosaic: Modeling social ai for content dissemination
and regulation in multi-agent simulations. InPro-
ceedings of the 2025 Conference on Empirical Meth-
ods in Natural Language Processing, pages 6390–
6417.
Qun Ma, Xiao Xue, Deyu Zhou, Xiangning Yu,
Donghua Liu, Xuwen Zhang, Zihan Zhao, Yifan
Shen, Peilin Ji, Juanjuan Li, Gang Wang, and Wan-
peng Ma. 2024. Computational experiments meet
large language model based agents: A survey and
perspective.Preprint, arXiv:2402.00262.
Tianmi Ma, Jiawei Du, Wenxin Huang, Wenjie Wang,
Liang Xie, Xian Zhong, and Joey Tianyi Zhou. 2025.
Agent trading arena: A study on numerical under-
standing in LLM-based agents. InFindings of the
Association for Computational Linguistics: EMNLP
2025, pages 5496–5514.
Meta. 2024. The Llama 3 herd of models.Preprint,
arXiv:2407.21783.
Xinyi Mou, Xuanwen Ding, Qi He, Liang Wang, Jing-
cong Liang, Xinnong Zhang, Libo Sun, Jiayu Lin,
Jie Zhou, Huang Xuanjing, and Zhongyu Wei. 2026.
From individual to society: A survey on social simu-
lation driven by large language model-based agents.
ACM Computing Surveys, 58(11).
Xinyi Mou, Zhongyu Wei, and Xuanjing Huang. 2024.
Unveiling the truth and facilitating change: Towards
agent-based large-scale social movement simulation.
InFindings of the Association for Computational
Linguistics: ACL 2024, pages 4789–4809.
Önder Gürcan. 2024. LLM-augmented agent-based
modelling for social simulations: Challenges and op-
portunities. InHybrid Human AI Systems for the
Social Good (HHAI 2024), Frontiers in Artificial In-
telligence and Applications. IOS Press.
OpenAI. 2025. gpt-oss-120b & gpt-oss-20b model card.
Preprint, arXiv:2508.10925.
John F. Padgett and Walter W. Powell. 2012.The emer-
gence of organizations and markets. Princeton Uni-
versity Press.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Mered-
ith Ringel Morris, Percy Liang, and Michael S. Bern-
stein. 2023. Generative agents: Interactive simulacra
of human behavior. InProceedings of the 36th An-
nual ACM Symposium on User Interface Software
and Technology.
Siyue Ren, Zhiyao Cui, Ruiqi Song, Zhen Wang, and
Shuyue Hu. 2024. Emergence of social norms in gen-
erative agent societies: Principles and architecture.
InProceedings of the 33nd International Joint Con-
ference on Artificial Intelligence, pages 7895–7903.
Qwen Team. 2025. Qwen3 technical report.Preprint,
arXiv:2505.09388.
Alexander Sasha Vezhnevets, John P. Agapiou, Avia
Aharon, Ron Ziv, Jayd Matyas, Edgar A. Duéñez-
Guzmán, William A. Cunningham, Simon Osindero,
Danny Karmon, and Joel Z. Leibo. 2023. Gener-
ative agent-based modeling with actions grounded
in physical, social, or digital space using Concordia.
Preprint, arXiv:2312.03664.
Ziyi Yang, Zaibin Zhang, Zirui Zheng, Yuxian Jiang,
Ziyue Gan, Zhiyu Wang, Zijian Ling, Jinsong Chen,
Martz Ma, Bowen Dong, Prateek Gupta, Shuyue
Hu, Zhenfei Yin, Guohao Li, Xu Jia, Lijun Wang,
Bernard Ghanem, Huchuan Lu, Chaochao Lu, and
4 others. 2025. OASIS: Open agent social interac-
tion simulations with one million agents.Preprint,
arXiv:2411.11581.
Jun Zhang, Yuwei Yan, Junbo Yan, Zhiheng Zheng,
Jinghua Piao, Depeng Jin, and Yong Li. 2025. A
parallelized framework for simulating large-scale llm
agents with realistic environments and interactions.

(a)Daily Mart
(a)Pizza Place
Figure 5: Time series of sales amounts for Pizza Place
and Daily Mart in a representative simulation run with
GPT-OSS-120B. A promotional campaign was con-
ducted at Pizza Place during December 23–25.
InProceedings of the 63rd Annual Meeting of the
Association for Computational Linguistics (Volume
6: Industry Track), pages 1339–1349.
Wenzhen Zheng and Xijin Tang. 2025. Simulating so-
cial network with LLM agents: An analysis of infor-
mation propagation and echo chambers. InKnowl-
edge and Systems Sciences, pages 63–77.
Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong Zhang,
Haofei Yu, Zhengyang Qi, Louis-Philippe Morency,
Yonatan Bisk, Daniel Fried, Graham Neubig, and
Maarten Sap. 2024. SOTOPIA: Interactive evalua-
tion for social intelligence in language agents. In
Proceedings of The Twelfth International Conference
on Learning Representations.
A Computing Infrastructure
The experiment is conducted on a workstation
equipped with the following hardware and software
configurations:
• CPU: AMD Ryzen 9 3950X 16-Core Pro-
cessor (32 threads, base clock 3.5 GHz, max
boost 4.76 GHz)
• GPU: 2 × NVIDIA RTX 6000 Ada Genera-
tion (48 GB VRAM each)
• Operating System: Ubuntu 22.04.5 LTS
(Jammy Jellyfish)
B Qualitative Analysis of an Emergent
Online–Offline Coupling
To complement the quantitative analysis in the
main text, we provide a qualitative case study of
a single representative simulation run using GPT-
OSS-120B. We focus on the three-day promotional
event held at Pizza Place during December 23–25
and examine how changes in agent behaviors and
online discussions jointly give rise to the observed
online–offline coupling.
Promotional Event and Aggregate Sales Dynam-
icsFigure 5 shows the resulting sales amount tra-
jectories of the two stores. During the promotional
period (December 23–25), Pizza Place exhibits
a pronounced increase in sales activity, whereas
Daily Mart remains within its ordinary range of
fluctuations. This contrast confirms that the promo-
tional campaign acts as a localized exogenous per-
turbation to the consumer economy domain. In the
following analysis, we trace how this local offline
event is reflected in the collective behaviors and
online discussions of household agents, providing a
qualitative illustration of the feedback loop across
consumer activities, mobility, and social interac-
tions that underlies the nonlinear online–offline
relationship reported in the main text.
Behavioral Adaptation of Household Agents
To characterize the collective adaptation of house-
hold behaviors, we cluster agents according to
their normalized daytime consumption-item vec-
tors.7 Figure 6 shows the resulting representa-
tive consumption patterns and the temporal evo-
lution of the number of agents assigned to each
cluster. The identified clusters capture distinct
consumption tendencies, including a pizza- and
soda-oriented dining pattern (cluster 1), rice- and
bread-centered routine shopping patterns (cluster
7Specifically, for each agent and each day, we construct
a consumption vector by counting purchases of each item
category during daytime activities. For example, a daily
consumption record of (Bread: 5, Pizza: 2, Rice: 0, Salad:
5, Soda: 1, Soup: 0) is represented as the six-dimensional
vector (5,2,0,5,1,0) , which is then normalized to unit
lengh before clustering. We conduct KMeans clustering with
K= 2,4,6,8, and 10, and report the result with the highest
adjusted Rand index (ARI) of0.681.

(a) Representative consumption vectors for the clusters.
 (b) Time series of the number of agents assigned to each cluster.
Figure 6: Behavioral clusters derived from normalized daytime consumption vectors and their temporal evolution in
the representative GPT-OSS-120B simulation run.
0: festive / discounted / christmaseve
2: escaping / jam /crowd
1: crowded / packed / leaving
3: piece / ate / last
4: sale / tommorows / pizza
5: finished / homebound / homeward
6: christmas / eve / grateful
7: exhausted / bed / sleep
8: friendly / chat / hello
9: staples / cheap / budget
10: restock / pantry / deals
11: mart / snag / budgethunt
12: soda / fizzy / festive
13: sleep / no / plan
14: lonely / bump / home
Figure 7: Time series of the topic composition of online
discussions in the representative GPT-OSS-120B simu-
lation run. Topics are obtained by applying BERTopic
to all posts generated during the simulation, and the
figure shows the proportion of each topic over time.
0 and 2), and a salad-oriented light-meal pattern
(cluster 3). During the promotional period, the
population of the pizza-oriented cluster (cluster 1)
increases markedly, while the relative sizes of the
routine shopping clusters decrease. These observa-
tions suggest that the promotional event reshapes
the distribution of consumption behaviors across
the population.
Emergence of Online DiscussionsTo investi-
gate how changes in offline activities are reflected
in the social network domain, we extract discus-
sion topics from the corpus of all generated posts
using BERTopic (Grootendorst, 2022). Figure 7
shows the temporal evolution of the resulting topic
shares throughout the simulation. During the pro-
motional period, topics directly related to the cam-
paign, such as“festive / discounted / christmaseve”
(topic 0), become prominent, indicating that in-
formation about the sale is actively propagated
through online interactions. At the same time, top-
ics associated with the consequences of increased
offline activity, including“crowded / packed /
leaving”(topic 1) and“escaping / jam / crowd”
(topic 2), also emerge and spread among agents.
These observations suggest that online discussions
reflect not only the promotional event itself but also
the collective experiences generated by the result-
ing changes in purchasing and mobility behaviors.
In this way, the social network domain contains
both positive feedback, where information about
the sale attracts additional consumers, and nega-
tive feedback, where reports of congestion discour-
age further visits. This coexistence of reinforcing
and balancing feedback qualitatively illustrates the
cross-domain interaction mechanism underlying
the nonlinear online–offline relationship reported
in the main text.
