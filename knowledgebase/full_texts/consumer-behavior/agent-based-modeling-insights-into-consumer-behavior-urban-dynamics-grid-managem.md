---
title: 'Agent-based modeling: Insights into consumer behavior, urban dynamics, grid management, and market
  interactions'
url: https://doi.org/10.1016/j.esr.2024.101613
category: consumer-behavior
subcategory: framework
date: 2025-01
venue: Energy Strategy Reviews
authors:
- Sambeet Mishra
- Thiago Christiano Silva
- Lars Hellemo
source: openalex-oa
pdf_url: https://publikationen.bibliothek.kit.edu/1000178670/156822489
pages: 19
chars: 126852
fetched_at: '2026-11-08T17:20:08+00:00'
kb_version: 1
---

# Agent-based modeling: Insights into consumer behavior, urban dynamics, grid management, and market interactions

Contents lists available at ScienceDirect
Energy Strategy Reviews
journal homepage: www.elsevier.com/locate/esr
Review
Agent-based modeling: Insights into consumer behavior, urban dynamics,
grid management, and market interactions
Sambeet Mishra a,f
 ,∗, Thiago Lima Silva b, Lars Hellemo c, Stefan Jaehnert a, Lars Even Egner c,
Sobah Abbas Petersen c, Tim Signer d, Florian Zimmermann d, Chiara Bordin e
a SINTEF Energy Research, Norway
b SINTEF Industry, Norway
c Norwegian University of Science and Technology (NTNU), Norway
d Karlsruhe Institute of Technology (KIT), Germany
e UiT: The Arctic University of Norway, Norway
f University of South-Eastern Norway (USN), Norway
A R T I C L E I N F O
Keywords:
Agent based modeling
Energy system modeling
Energy transition
Energy strategy
Decision support system
A B S T R A C T
A future sustainable energy system is expected to be digital, de-central, de-carbonized, and democratized. As
the transition unfolds, new and diverse actors of various sizes will emerge in different segments. Thereby, the
future energy system could shift its attention to the actors’ behavior than finding an optimum based on the
physical system. Agent based modeling tools can reflect decisions from several actors in a decentralized and
digital market setting. Then, such tools can enable a sustainable energy transition.
This work sets out to investigate how agent-based models could tackle various challenges in energy
transition. This investigation covers four segments of the energy system — consumer, city, microgrid, and
market. It starts with the consumer where consumer behavior is modeled. From there, expands to a city level
where the dynamic characteristics of a city are simulated. The next step is distributed microgrids, particularly
how to optimally plan the grid expansions. The final step in the investigation is simulating an energy market
with national and international stakeholders. The selection of models presents how agent-based models can be
applied to decision-making processes in the aforementioned segments. Then a novel framework with metrics
for characterization is proposed and validated that addresses the challenge — which are the characteristics that
make an agent-based model a better fit to tackle a modeling objective? Additionally, the framework identifies
the existing knowledge gaps and the scope for further developments.
In summary, this work outlines how far agent-based models have come to tackle energy system challenges
to sustain the energy transition. This work specifically highlights the scope, advantages, challenges, and trends
of the agent-based models in energy sector applications. Moreover, this study finds that agent-based models
reflect what a solution could be more than the traditional modeling practice that focuses on what a solution
should be.
Contents
1. Introduction ...................................................................................................................................................................................................... 2
1.1. Working of an agent-based model............................................................................................................................................................ 3
1.2. Scope and objective................................................................................................................................................................................ 4
1.3. Methodology.......................................................................................................................................................................................... 4
1.4. Key contributions ................................................................................................................................................................................... 4
2. Portfolio of agent based models for energy transition ........................................................................................................................................... 5
2.1. ABM for household Energy Retrofit Behavior (HERB) ................................................................................................................................ 5
2.2. ABM for city dynamics simulation (CitySIM) ............................................................................................................................................ 8
2.3. ABM for distributed microgrid expansion planning.................................................................................................................................... 9
2.4. ABM for electricity market simulation (PowerACE) ................................................................................................................................... 11
∗ Corresponding author at: SINTEF Energy Research, Norway.
E-mail addresses: sambeets@gmail.com, sambeet.mishra@usn.no (S. Mishra).
https://doi.org/10.1016/j.esr.2024.101613
Received 29 December 2022; Received in revised form 11 November 2024; Accepted 12 December 2024
Energy Strategy Reviews 57 (2025) 101613
Available online 3 January 2025
2211-467X/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-
nc-nd/4.0/ ).

S. Mishra et al.
3. Discussions and characterization of ABM tools ..................................................................................................................................................... 13
3.1. Characterization of ABM for consumer behavior ...................................................................................................................................... 15
3.2. Characterization of ABM for city dynamics simulation............................................................................................................................... 15
3.3. Characterization of ABM for expansion planning of distributed microgrids .................................................................................................. 16
3.4. Characterization of ABM for electricity market simulation ......................................................................................................................... 16
4. Concluding remarks ........................................................................................................................................................................................... 17
4.1. Determinants of agent-based modeling approaches .................................................................................................................................... 17
Declaration of competing interest........................................................................................................................................................................ 17
Acknowledgments .............................................................................................................................................................................................. 17
Data availability ................................................................................................................................................................................................ 17
References......................................................................................................................................................................................................... 17
Nomenclature
𝐴𝐵 𝑀 Agent Based Model (s)
𝑀 𝐴𝑆 Multi Agent System
𝐶 𝐴𝑆 Complex Adaptive System
𝐶 𝑅𝑀 Capacity Remuneration Mechanism
𝐸 𝑉 Electric Vehicle
𝐿𝑂 𝐿𝐸 Loss of Load Expectation
𝑀 𝐺 Microgrid
𝑁 𝑃 𝑉 Net Present Value
𝑅𝐸 𝑆 Renewable Energy Sources
1. Introduction
In an era marked by rapidly evolving technology and increasing
sustainability awareness, energy systems are pivotal interfaces of hu-
man progress and environmental stewardship [1]. At their core, energy
systems are designed to serve a fundamental purpose: delivering criti-
cal energy services to end-users. However, these systems’ complexity
extends far beyond mere production and distribution [2,3]. As the
Intergovernmental Panel on Climate Change (IPCC) underscored [4],
energy systems envelop ‘‘all components related to the production,
conversion, delivery, and use of energy’’, accentuating their multi-
faceted nature [5]. Understanding the complexity of energy systems
requires a comprehensive view [6,7]. Beyond their intricate matrix
of components and technical facets, these systems are emblematic
of economic maneuvering, political decision-making [8], and social
dynamics [9,10]. While this convergence of elements provides rich
opportunities for innovation, it also introduces complexities that com-
plicate the understanding of the system and makes both its analysis
and subsequent optimization difficult [11]. Illustratively agent based
models are evidently finding new applications in the field of large lan-
guage models [12], real-time predictions [13], multi-level policies for
epidemic management [14], electrical vehicle demand simulation [15],
urban growth modeling in Africa [16].
When it comes to analyzing energy systems, the research objective
becomes paramount and influences the perspective from which the
energy system is viewed [17]. Based on this overarching view, critical
system elements can be identified and modeled depending on the
specific objective [18]. Given the complexity of energy systems, these
models serve as simplifications and essential abstractions that make
the system modelable and analyzable [19]. Within this framework,
tools like flow network algorithms, including minimal cost flow, find
applications [20]. System components can be conceptualized as individ-
ual dynamical entities, underscoring the significance of technological
modeling rooted in the engineering nuances of particular technologies.
As energy systems transform with new technologies and innovative
mechanisms, the need for sophisticated modeling grows more pro-
nounced, especially in supporting informed decisions for a sustainable
energy future [21]. In this evolving landscape, agent-based modeling
(ABM) has emerged as a potent tool, garnering significant attention
in recent years [22,23]. ABM is bottom-up approach distinguishes it,
allowing for detailed modeling of specific system components and
stakeholders. Such granularity offers invaluable insights, especially
when navigating novel mechanisms like peer-to-peer trading [23]. By
capturing the intricacies of these elements, ABM provides a compre-
hensive lens to view, analyze, and optimize the ever-adaptive energy
system landscape [24,25].
Agent-based modeling (ABM) has become a crucial tool in energy
research, enabling the simulation of complex systems with interact-
ing agents, such as consumers, firms, and policymakers. The use of
ABM in energy systems dates back to the 1990s, when early models
began to explore consumer behavior and market dynamics in elec-
tricity systems [26]. In the mid-1990s, ABM’s potential for modeling
decentralized systems and decision-making processes in energy markets
became more widely recognized, with studies such as Tesfatsion in [27]
demonstrating its capacity to simulate electricity markets and pricing
mechanisms. By the early 2000s, ABM expanded to incorporate more
complex scenarios, including renewable energy integration and envi-
ronmental policy impacts in [28]. In the 2010s, ABM became essential
for studying the dynamic transitions of energy systems, as it was
increasingly used to model energy transitions, renewable energy adop-
tion, and consumer behavior in response to climate policies [29]. More
recently, ABM has been leveraged to simulate the interactions between
diverse energy technologies, policy incentives, and societal behavior,
providing insights into how small-scale decisions can affect large-scale
system transformations [30]. These historical developments highlight
the growing sophistication and applicability of ABM in understanding
and managing energy systems.
One of the very first ABMs created showed that in a simulated
neighborhood where the inhabitants had a slight preference for similar
neighbors to oneself will generate total segregation [31]. Here, the
model showed that even though none of the individual agents had
a wish or desire for segregation, this was the macro-level outcome.
This is one of the main functions of ABMs; to model the behavior of
individual agents and observe macro-level outcomes. As ABM relies on
the codification of individual behavior, it is therefore deeply connected
to the behavioral sciences [32].
Generally, codifying agents’ behavior can be separated into two cat-
egories. In the first category, agents act according to rational decision-
making. Here, agents perform a certain action when they are financially
beneficial, or when the benefits outweigh the risks [33]. This type of
modeling gives better predictions, but the validity is often questioned,
as humans are not purely rational decision-makers. In the second
category, agents act according to existing behavioral research. Here,
agents do not typically act rationally, but in accordance with their val-
ues, motivations, barriers, mental shortcomings, and decision-making
strategies [34]. For the purpose of this paper, we dub it psychological-
behavioral systems. The aforementioned factors can be based on the
modeler’s own research or existing behavioral theory. This type of
modeling is less precise but could be argued to be more valid.
Although the knowledge gained from decision-making research is
starting to be integrated into energy system modeling, the process
is slow. Huckebrink and Bertsch Huckebrink and Bertsch [35] state
in their recent review of the literature that ‘‘developing more so-
phisticated ways for integrating behavioral aspects in energy system
Energy Strategy Reviews 57 (2025) 101613
2

S. Mishra et al.
optimization or simulation models is of utmost importance in order to
allow for behavioral realism of the output from energy system models’’.
Translating behavioral research to model code is difficult, but vital to
the validity of energy system models.
Agent-based modeling is a modeling approach that has been devel-
oped that focuses on capturing the behaviors of real-world actors as
computational agents. It is a tool that ought to be considered when
working on the transition to sustainable energy [30].
The future energy system is decarbonized meaning low-emission
or, at best, carbon-neutral. The transition to a sustainable energy
future aims to achieve a better balance by adjusting both supply
and demand sides [36]. A better balance could be achieved by ac-
tively engaging stakeholders at various levels, essentially democratizing
the energy sector. Rapid digitalization is underway to accelerate the
process. As the transition unfolds the system is expected to be decentral-
ized where several pockets of distributed generations, consumers, and
prosumers will maintain the supply–demand balance. The European
Union in its ‘Fit for 55’ package seeks to increase the flexibility in
the energy system by active engagement of consumers [37]. NODES
in Norway aims to increase flexible power consumption through the
NorFlex project [38]. Through this project, a local flexibility market
is operated to achieve a better balance by deferring consumption, and
investments and securing network operations. This project illustrates
that the future energy system is expected to be decarbonized, digital,
decentral, and democratized [39–43].
The transition is then reflected in the policies and models that
drive the decision-making process. Existing policies are expected to be
revised to cater to a consumer-centric approach. In terms of models,
the attention is shifting towards behavioral-based predictions from an
often non-attainable theoretical global optimum from the technology
perspective. Reflecting the behavior of various actors in the system is
often a challenge due to the layers of complexity as opposed to rule-
based decision-making. Then it is paramount to better understand the
motivations and responses of the agents in the energy system.
An agent-based model (ABM) can be understood as a model with a
defined environment, an autonomous decision-making entity with feed-
back loops as the entity interacts with the environment [44]. Intelligent
agents have been described as software, hardware, or computer-based
entities that are autonomous, proactive in a goal-oriented manner,
react in a timely manner by perceiving their environment, and have
the ability to communicate and coordinate with other agents in the
environment or human beings [45]. A Multi-agent system (MAS) can
be understood as a collection of such agents, forming a hive that
could simulate real-world scenarios. ABM has the feature to integrate
various types of models or methods for decision-making. For instance,
mathematical functions, statistical models, machine learning, network
analysis, optimization models, and game theory. A MAS could link
one or more types of methods through utility functions or rule-based
mechanisms to approximate a system behavior with many hetero-
geneous agents. Rai and Henry [29] explain the fundamental and
applied aspects of ABM to model consumer energy choices. Melliger
and Chappin [46] used an ABM approach to investigate the invest-
ment preferences considering renewable energy support schemes. How
agent-based models can be used to simulate the occupant behaviors in
a building is proposed by Lee and Malkawi [47]. This illustrates that
ABM tools can be utilized to render decisions on investment planning
as long as consumer behaviors.
The energy transition towards a carbon-neutral future relies both on
the supply and demand side transitions. On the supply side, the transi-
tion is focused on switching to low-emission resources such as hydro,
wind, and solar. Resources can be further classified into dispatchable
and non-dispatchable types. Stored hydropower production is a mostly
dispatchable resource while wind and solar are non-dispatchable being
reliant on weather conditions; therefore, stochastic. Hydro, wind, and
solar resources often come with inherent uncertainties and variability.
Adding to that, as the policies and decisions are expected to rely
Fig. 1. Structure of an agent.
more on consumer behavior, uncertainties in behavior would become
a significant part of the decision-making process. For instance, how a
consumer responds to electricity prices balancing its desired comfort
levels. Such actions are stochastic in nature as their priorities differ
from one to another. ABM fits the context of modeling uncertainties
and simulates various production scenarios which are partly unpre-
dictable. Ma and Nakamori [44] presents a comparison between three
types of optimization models and agent-based models for planning in
the energy system. The authors concluded that optimization models can
describe ‘‘what should be’’(normative) and agent-based models explain
‘‘what could be’’ (explorative).
With the growing interest in applying ABMs for simulating and
studying the behavior of energy systems and the diversity of agent-
based tools that are available, there is a need to analyze and evaluate
the relevance of these models and tools. The need for a metric for the
classification and characterization of the models has been developed.
1.1. Working of an agent-based model
The fundamental working principle of an agent is presented in
Fig. 1. An agent is interacting with an environment with three functions
— action/re-action, reward, and state. With each time 𝑡, the state of the
environment 𝑆𝑡 is recorded. An agent performs an action 𝐴𝑡 seeking
reward 𝑅𝑡. Depending on the objective, an agent optimizes the expected
reward 𝑅𝑡 through action 𝐴𝑡. With each iteration, the agent receives
an adjusted reward 𝑅𝑡+1 and an updated state of the environment 𝑅𝑡+1.
The objective of the agent is to maximize its reward, with each time
step 𝑡, through adjusting the action 𝐴𝑡. The key challenge is to design an
adequate reward function such that maximum reward can be achieved
by the agent through adjusting its actions [48].
The traditional definition of ABM while covering a large part of ap-
plications, does not cover pseudo-random events, such as the behavior
of consumers. It is although important to be noted that ABM is one of
the tools that can still be used to simulate such a dynamic and complex
system. Such systems often have a pseudo-random state at their core as-
sumption or starting point. Often highly uncertain and variable systems
sit in this category. Instead of being goal-oriented, such models seek to
take any feasible state within the set boundary conditions. Consumer
behavior in terms of responding to price signals could be mentioned
as an example. When the rewards increase the number of random
states reduces. For instance, as the number of consumers increases who
respond to the signal then the behavior becomes more predictable.
ABM are versatile tools that can be used for various perspectives in the
context of an electric power system. For instance, ABM can be used to
model from the grid owner’s perspective to maximize profit or minimize
losses, at the same time ABM can be used from a system perspective
as in emulating dynamic city-transport dynamics. A reward therefore
could be a sufficient attribute but not necessary in the application of
ABM in the real world.
A multi-agent system could be understood as a collective of agents
through a functional relation to meet a common or central objective.
Energy Strategy Reviews 57 (2025) 101613
3

S. Mishra et al.
While ABM primarily focuses on an individual agent’s interaction with
an environment, a MAS typically emphasizes interactions within the
system. For instance, MAS involves the study of coordination mecha-
nisms and multi-criteria decision-making methods. Subsequently, ABM
tools are often employed in behavioral studies but MAS is used for in-
telligent systems with autonomous agents with individual objectives. In
terms of methodology, ABM tools utilize a simulation-based approach
and are used for observation of the system evolution. MAS covers a
broader range of methodologies such as distributed computing, game
theory, and coordination mechanisms by mathematical optimization
for decision-making. ABM models have been adopted in several recent
energy system decision-making challenges such as trading storage [49],
strategic bidding in day-ahead energy market [50], integrated energy
systems [51], food-energy-water nexus [52] and hybrid ABM-Machine
learning prediction of energy consumption [53]. Some relevant proto-
cols for describing ABM that have been proposed in the literature are
ODD, ODD+, Mr. Potatoehead [54–56].
1.2. Scope and objective
Several models for energy system modeling have been proposed in
the literature for the planning and operation of centralized electrical
power systems from the perspective of policymakers, regulators, and
producers [57–62]. Such tools are used to determine investments in
capacity expansion and optimal scheduling of generation units. As the
power system moves from a centralized to a more decentralized system
wherein the consumer has a possibility for more active participation,
new modeling tools are required. End-user or local flexibility is an
example of such a scenario where the consumer determines the level
of flexibility without sacrificing individual comfort.
Avoiding the YAAWN syndrome [63], the scope of this study is to
illustrate the ABM applications in four segments for sustainable energy
transition — consumers, cities, grids, and electricity markets. The study
also identifies the trends and patterns within each area of application.
Below is a short introduction to the four segments.
Energy market — Electricity, heat, and fuel products are all dealt
with in the energy market, a particular kind of commodities market.
Electricity and natural gas constitute significant commodities. Oil, coal,
carbon emissions (greenhouse gases), nuclear power, solar energy, and
wind energy are additional commodities traded in the energy market.
Current and upcoming energy prices are rarely correlated because of
the challenges associated with energy storage and transportation.
Decentralized microgrid — A decentralized microgrid is a small-
scale collection of various power sources, typically renewable sources,
that can function independently or in conjunction with a larger energy
grid. Grid-connected microgrids have the ability to disconnect from
the larger grid when needed to run independently in ‘‘island mode’’.
People can act as producer–consumers (also known as ‘‘prosumers’’) or
simply as consumers thanks to microgrids, which operate on the idea
of communal collaboration.
City dynamics — City dynamics refers to the city as a complex
adaptive system (CAS) with heterogeneous and autonomous agents.
With a focus on the transportation and electric grid, it includes sev-
eral agents representing cars, buses, humans, and other transportation
means. The simulation is conducted with the objective to understand
the evolution of the city with dynamic changes in the transportation
system. Moreover, the total power usage is observed in simulating the
dynamics of the city under several operational policies.
Consumer behavior — The study of people, groups, or organizations
and all the behaviors connected to the acquisition, consumption, and
disposal of products and services is known as consumer behavior.
Consumer behavior refers to how a person’s feelings, attitudes, and
preferences influence their purchasing decisions. Researchers in the
energy sector frequently discuss ‘‘energy consumer behavior’’, which
is frequently described as a collection of individual behaviors that
affect energy production and consumption. In this context, behavioral
economics plays a key role.
1.3. Methodology
The proposed framework is tested and validated with the 4 models
presented in this work. The proposed framework provides a complete
and holistic characteristic of an ABM that can be utilized to (a) identify
potential knowledge gaps and (b) compare similar tools for an informed
selection.
The metrics for the evaluation of ABMs that are proposed in this
paper could meet the current needs and is an innovative artifact that
could support the selection of an appropriate tool for modeling energy
systems using ABM. The Design Science Research Method (DSRM) [64]
from the field of Information Systems is an appropriate method for
designing new artifacts, based on the needs of the environmental
context (energy modeling in our case) and leveraging on the existing
body of knowledge, methods, and theory. Thus, we have adopted DSRM
as our methodology for the design of the metrics for evaluation. DSRM
includes three closely related cycles of activities, which are called the
relevance, rigor, and design cycles. The relevance cycle identifies the
environment in which the designed artifact will be applied and the
requirements for the designed artifact. The rigor cycle brings existing
knowledge, methods, and theories into the design cycle and adds the
new knowledge generated through the design process. The design cycle
is an iterative process that includes the design, development, and
evaluation of the design artifact until it has reached the desired quality
and expectations [65]. Our adoption of Hevner’s DSRM is illustrated in
Fig. 2.
Previous research shows that several methods have been applied to
studying the contextual environment, such as interviews and observa-
tions. Case studies [66] have been considered as one of the approaches
that could be applied for studying the environment and collecting data
before the design of the artifact [67]. The contextual environment in
this research includes several ABMs in the energy sector, developed
for a variety of purposes and ranging from single entities, such as
a household, to larger systems, such as a microgrid or a city. These
are presented as cases to illustrate a range of ABM approaches and
methods in diverse application contexts. We have used the case study
approach to describe some different ABM approaches for energy model-
ing. Each of these cases was a study by itself, conducted independently
of each other and by different research groups. The authors represent
researchers involved in each study. Hence, the main source of data for
each case is the researchers themselves and the models, experimental
data, and the relevant documents that relate to the specific studies.
Each case description includes the specific literature relevant to the
study, the specific research methods, and the modeling, design, sim-
ulation, and validation methodologies. The analyses of the case studies
provided input for the design cycle in DSRM. The metrics for evaluation
shown in Table 2, which is the new artifact that is developed, have been
developed by synthesizing the different studies reported in this paper
and by analyzing them to identify the main characteristics of these
models. This result has been further used to both evaluate and compare
the different ABM tools, which also serve as a validation of the metrics
for the evaluation itself. As one of the objectives of DSRM, the new
knowledge that is created through this research work is the analyses of
the ABM cases in the energy sector, the metrics for evaluation, and an
analysis of the ABM cases using the new artifact, described in Section 3.
1.4. Key contributions
This paper focuses on agent-based modeling for energy system
planning. One of the primary motivations for utilizing agent-based
modeling is its unique capability to model intricate energy systems
at a micro-level. Such granularity and high-level detail are exclusive
attributes of ABM, setting it apart from other modeling techniques.
Agent-based modeling’s emphasis on the micro-level permits a broad
spectrum of perspectives for analysis. It begins at the individual agent
level and extends to the system level when considering the interactions
Energy Strategy Reviews 57 (2025) 101613
4

S. Mishra et al.
Fig. 2. Design science research method and case studies.
and interplay of multiple agents. Furthermore, ABM allows for the
examination of different methodological and behavioral aspects. This
provides an avenue to mirror the heterogeneity of actors in the energy
system, capturing the vast diversity and individualistic behaviors.
The main contributions of this work can be summarized as follows:
• Systematic investigation of Agent-based models in four key en-
ergy transition areas — consumers, cities, electric grid, and elec-
tricity market
• Schematic description of a representative ABM use cases for each
area, illustrating the decision making process and the related
results.
• Outline the trends and patterns in terms of modeling, specifically
agent-based modeling, for each area.
• Introduction and validation of a novel framework to characterize
heterogeneous agent-based models to facilitate decision-making
in subsequent areas
• Derivation of determinants for the future development of agent-
based tools applied to energy system modeling
The rest of the paper is organized into three sections. Section 2
introduces the selection of agent-based models alongside a case study
to demonstrate the working of the model. Section 3 introduces a
framework to evaluate the agent-based model and applied it to the
selection of models. Finally, a conclusion is drawn based on the findings
and future outlook.
2. Portfolio of agent based models for energy transition
The inquiry first focuses on the energy transition from the perspec-
tive of the consumer and then moves on to the dynamics of the city,
particularly the transportation sector. The inquiry then moves to the
grid level, where the best growth planning choices are made using the
ABM approach. Lastly, a presentation on the use of ABM to electricity
market simulation is made. Presenting a fresh framework to character-
ize ABM technologies is the secondary goal. The suggested paradigm
accomplishes two goals: (a) determining the benefits, drawbacks, and
knowledge gaps of a specific ABM tool; (b) comparing tools of a similar
nature.
The portfolio of the ABM tools and subsequent four energy segments
are illustrated in Fig. 3.
The first case study investigates how the energy consumption-
oriented behavioral aspects of a consumer can be modeled using ABM.
The second case study expands to simulating the dynamics of a city
such as traffic and transportation. The third case study presents how a
multi-agent system can be applied to microgrid expansion planning un-
der resource uncertainty. Finally, the fourth case study delves into how
a multi-agent system can be unitized to simulate electricity markets.
Fig. 3. Selection of applications using agent-based modeling tools.
2.1. ABM for household Energy Retrofit Behavior (HERB)
The first case study focuses on households’ energy retrofitting be-
havior and energy heating consumption. For the analyses, we use an
agent-based model, the Household Energy Retrofit Behavior (HERB)
model [68]. Different policies can be assessed using the model to
observe their impact on energy consumption over time. This model
was primarily based on a series of research investigating households’
decisions to retrofit [69,70]. Their research found that households
typically go through 4 stages of decision-making and that different
factors influence the transition between different stages. In the first
stages, when the households are still considering upgrading the thermal
insulation of the house, the key variables are their self-efficacy, i.e. their
belief in their capability to execute behaviors necessary to produce
specific performance attainments (upgrading the thermal insulation of
the house), and how wasteful they perceive their energy standard.
In later stages, when the agent has already decided to perform the
thermal insulation upgrade but is still considering the available options,
financial factors are more important. How important each factor was to
each stage was quantified through interviews and surveys in [69,70],
and also based on other research studies [71].
In the HERB model, each agent, which represents a household, can
therefore transition between four stages of decision-making, based on
the four stages identified in this research. The main factors influencing
the transitions were translated into mathematical form after technical
discussions in a workshop with behavioral researchers. Still, a pseudo-
random generator with a stochastic behavior was introduced in all
stages of the decision-making algorithm in order to account for some
factors which are hard to describe mathematically, such as free will
Energy Strategy Reviews 57 (2025) 101613
5

S. Mishra et al.
Fig. 4. HERB model schematic.
or intuition, e.g. ‘‘the right time has not yet come’’. To complete the
model, a system for households to pick what energy standard they
considered upgrading to had to be implemented. No research on this
could be identified, so a general modeling approach was selected.
The model-based itself on research regarding the availability heuristic,
which refers to the phenomenon that humans make decisions based
on readily available information [72]. The more readily available the
information is, the more impact it has over the decision being made, re-
gardless of its objective relevancy. Naturally, the most readily available
energy standard of households was that of their neighbors and friends.
Thus, households mostly considered upgrading to the energy standards
they were exposed to through their neighbors and friends.
A schematic describing the model is depicted in Fig. 4. In the
initialization phase, the neighborhood of study is instantiated with
the corresponding physical and psychological variables of each house-
hold. In the sequence, a randomized algorithm selects the household
friends including close neighbors and also other households residing
a bit further within a certain radius from the household address. The
household friends will influence their psychological variables in the
decision-making process. In the simulation phase, prior to the decision-
making, the model accounts for natural phenomena, such as a decay in
the household energy standard, a continuous increase in the household
investment potential, and also the possibility of agents moving to
another neighborhood. The simulation transforms the physical vari-
ables of a household, e.g. their property size, income, and investment
potential, into psychological variables, e.g. self-efficacy and financial
worry. Then, it calculates a final score indicating the probability of the
household transitioning between stages. Different scores are required
to transition between different stages. The agent typically transitions
from the first stage, where it is not considering a decision yet, to the
second stage where it is deciding what to do, before reaching stage 3
where is deciding how to do the retrofit. After stage 3, the household
performs retrofit if it is affordable or goes back to stage 1 and picks a
new ambition.
Case study 1 investigates the energy retrofitting decision-making
process of private households using the HERB model. First, the HERB
model aims to evaluate how well psychological decision-making, rather
than economical, fits real-world data regarding the overall retrofitting
rate, mean energy standard, consecutive retrofitting, and free-riding on
subsidies. Secondly, it can enable investigation of the effect of current
and proposed energy retrofit policies on overall energy consumption.
The neighborhood of study consists of 430 households spread over
an area of 1 square km split into grid cells. Each Household lies on a
grid cell of this simulated area and the model is simulated for 50 years
with a 1-week tick. Each household has a set of state variables, such
as property size, annual technical energy standard, current ambition
the household aims to retrofit, an income docile to which the house-
hold belongs, some investment potential representing the amount of
money available for retrofitting, and also some personal multipliers
moderating the importance of the psychological variables.
An assumption was made that each household has also a social net-
work consisting of 10 peers, being 5 neighbors and 5 closest friends who
can live further away. Another assumption concerns the retrofitting ac-
tions that are performed by the households. In the current HERB model,
retrofit actions are modeled as relative improvements in the energy
standard, so there is no representation of specific retrofit measures as
the focus of the ABM is on modeling the behavior of energy retrofitting.
Still, differently from other ABMs available in the literature repre-
senting energy-oriented behavioral decisions [68], the HERB model
represents the energy standard of buildings using energy efficiency
metrics such as average energy consumption per household in total
energy per square meter (kWh/m2). Extensions to the HERB model to
consider a more accurate representation of different energy efficiency
measures such as wall insulation, roof insulation, new windows and
doors and better heat recovery ventilation that is feasible for each
building is part of ongoing research activities in the Behavior project.
The HERB model uses input data from two surveys conducted by
Enova SF in 2014 and 2019 with the aim to investigate the trends in
private housing retrofitting in Norway. The surveys had 2605 and 3797
respondents, respectively. After removing answers with missing data
and performing 5 imputations to the original data, a larger dataset with
28,000 entries was produced. The dataset and more details about the
input data can be found at [68]. In the simulation results presented
hereafter, we considered 430 households uniformly distributed across
the 10 income deciles established by SSB (Statistics Norway) [73].
Fig. 5(a) depicts the average energy standard for all the build-
ings considered in the simulated neighborhood which is a measure
of annual energy performance of the buildings based on their con-
struction type, year, thermal insulation and installed equipment. On
the right-hand side, Fig. 5(b) shows the number of retrofits (with the
associated moving average for a 3-year period) performed over 50 years
or 2600 weeks. As it is shown in Fig. 5(a), a continuous decrease in
the mean annual energy standard is observed in the first 2000 weeks
of simulation. After that, the mean energy standard starts to increase
again until the end of the simulation. There are two opposing forces
influencing the mean annual energy standard: a natural decay in the
energy standard of the building due to aging, and the energy efficiency
improvements achieved with the retrofits. The energy standard of the
buildings in the simulations ranged within 190–235 kWh/m2 which
is within the reference standard for Norway between the years 1995–
2012 according to Statistics Norway (SSB) [74]. These results are show
a potential realization of the future for the simulated neighborhood
Energy Strategy Reviews 57 (2025) 101613
6

S. Mishra et al.
Fig. 5. Simulation results depicting the mean energy standard and retrofits performed in the 430 private houses.
Fig. 6. Total cost of retrofits and subsidies distributed.
where subsidies remain the same as today and there are two opposing
forces in action, the building depreciation impacting negatively and
retrofitting actions impacting positively the energy standard.
As it can be seen in Fig. 5(b), the weekly number of retrofits
performed initially is quite high mainly due to model initialization. It
settles at relatively low retrofit rates, between 0.5% and 1.1% (for a ref-
erence, the Norwegian energy retrofit rate is at a standstill compared to
4 years ago, with a yearly energy retrofitting rate of about 3.4%) [75],
which explains the increase in the mean annual energy standard over
time.
Figs. 6(a) and 6(b) depict the total weekly cost with retrofits and the
corresponding distributed subsidies. The retrofit costs depend on the
desired improvement, e.g., the difference between the actual energy
standard and the household’s ambition, the energy price, and the
house size. The retrofit costs are based on the relative improvement
in the energy efficiency of the building following the cost estimates
proposed in [71]. As can be seen by looking at both the total costs
with retrofits and total amount of subsidies distributed, there is a strong
correlation between the number of retrofits being performed and the
available subsidies. This means that more households are willing to
perform retrofits if they are eligible for subsidies. The total amount of
subsidies distributed in the simulations is a good measure of the impact
of policies to foster retrofitting and its impact on the mean energy
standard.
Fig. 7 shows the weekly distribution of households in the four
decision stages. In this graph, it is possible to observe the number of
agents in the different decision stages, namely from 1 to 4, and how
they transition between the stages for a period of 50 years. After an
initialization phase, the share per decision stage becomes relatively
stable. Many factors influence the transitions between the decision
stages, such as financial concerns related to the investment potentials
and retrofit costs, but also social influence exerted by neighbors and
friends in the households’ social network. Although considering some
financial concerns and randomness in such transitions, they are mostly
Fig. 7. Retrofit intention — decision stages.
driven by psychological variables rather than economic ones.
Fig. 8 depicts the final mean energy standard for different policies
regarding the distribution of subsidies. The value on the 𝑥-axis indicates
the minimum energy standard required for households to be eligible
for the most accessible subsidy when retrofitting. As can be seen in
the plot, this relation is fairly non-linear but its initial trend shows
a relative improvement in the final mean energy standard when the
requirement on the minimum energy standard is increased. This result
is logical as more households would be eligible for subsidies with a
higher threshold on the minimum energy standard. The second trend
showing an increase in the final mean energy standard could indicate
that less ambitious retrofits occur initially (and not subsequently) and
this affected negatively the final mean energy standard temporarily. As
it was seen in Fig. 5(a), an improvement in the energy standard in a
shorter horizon is not enough to ensure the best performance in the
Energy Strategy Reviews 57 (2025) 101613
7

S. Mishra et al.
Fig. 8. Effect of subsidy policies on mean energy standard.
long term. Sensitivity analysis on key criteria for policy enforcement
can be used as input by decision-makers to evaluate the performance
and select the best policies for a given horizon of interest.
The main aim of this case study is to investigate households’ en-
ergy retrofitting behavior and their influence on energy heating con-
sumption in city districts or neighborhoods. Rather than traditional
mathematical and financial-driven models, an ABM model focused on
household energy retrofit behavior was adopted for the analyses. This
model was selected based on previous behavioral research on energy
retrofit which found that psychological variables, such as i.e. self-
efficacy and how wasteful they perceive their energy standard are more
important than economic variables, especially in the initial decision
stages. The model allows to simulate of energy retrofitting behavior
for different policies and neighborhoods, which has the potential to
support policymakers to assess the impact of subsidies and other types
of incentives impacting energy heating consumption.
The HERB simulation model has the potential to simulate the fre-
quency and distribution of energy retrofits across city districts for
many decades. Given the current energy situation in Europe and the
significant share of energy consumption used for heating, this is an
important aspect for decision-makers searching for the main energy
consumption trends and favorable policies to foster energy savings.
Further, the model can also provide insights on the unrealized po-
tential and regional energy demand, which can provide insights to
energy providers for prioritization of investments and deployment of
the necessary energy infrastructure in a cost-effective manner.
2.2. ABM for city dynamics simulation (CitySIM)
In this case study, CitySIM, we have focused on the city as a
whole and how the city and the entities within it evolve due to their
interactions. The motivation for this study was to understand how
individual citizens’ decisions can affect the city. In particular, we have
examined how an individual person’s decision on their transport mode
could affect the traffic picture and the evolution of the traffic condition
in the city during the day. The main aim of this study was to explore the
uses of an agent-based, modular micro simulator of a city as a Complex
System. This study was conducted as a part of a Masters’s thesis and
the details of the implementation and simulation results are available
from [76].
Cities have been described as Complex Systems, where the overall
behavior emerges due to the behavior of its components [77]. Hence,
we apply ideas from Complex Adaptive Systems (CAS) in combination
with ABM. CAS is composed of interacting, autonomous agents [78].
To understand the behavior of such a system, the interconnections
or the ‘‘interwovenness’’ of the entities as well as the behaviors of
the individual entities are essential [79]. The overall behavior of such
an entity, in this case, a city, thus emerges as a consequence of the
interactions between the entities within the city, and this is called
emergent behavior. Another way of explaining emergent behavior is
that the whole is greater than the sum of the individual parts. One of the
advantages of CAS modeling is the ease of modeling simple, individual
entities bottom up, and the possibility to conduct population-level
simulations [80]. The energy consumption and indeed the distribution
of energy consumption across a city or the energy flow is linked to
where people are and what they do.
The entities within a CAS can be modeled as agents using the ABM
approach [81]. In the CitySIM case, the aspects of a city that were
included in the model are traffic (cars and buses) and the electric grid.
These agents interact through the traffic system and make decisions
based on past experiences, which are measured in the costs of choices
they make. The ABM model and the simulations were implemented
using the Repast Simphony 2.6, released on 20 November 2018, which
is a tightly integrated, richly interactive, cross-platform Java-based
modeling system that runs under Microsoft Windows, Apple Mac OS
X, and Linux. It supports the development of extremely flexible models
of interacting agents for use on workstations and computing clusters.
An ABM is developed for the environment (the roads in a few blocks
of the city of Trondheim, Norway) and for the entities that use the
environment, and the agents we have identified, which are cars, buses,
and persons. These are shown in Fig. 9(CitySIM case: Agents and
Environment).
The agent ‘‘Persons’’ choose travel methods, which are by the agent
types ‘‘Bus’’ or ‘‘Car’’. The population of people is a parameter, i.e. the
no. of agents of type Persons, (e.g. 75 % of people go to work, 2 %
do not go anywhere, 23 % go shopping). A Person chooses to use her
own car or take the bus, e.g. depending on the bus fare or weather.
The agent ‘‘Vehicles’’ use the road network, i.e. the ‘‘Environment’’ to
move on. ‘‘Spawn’’ points are where vehicles enter the model, i.e. the
road or the environment respectively, and ‘‘Despawn’’ points are where
vehicles exit the model. Simple ‘‘Rules’’ are applied to vehicles to avoid
collisions and to calculate their paths. For example, each vehicle has a
destination to calculate their paths, and they avoid collision with the
vehicles next to them (in front, behind, and to their sides).
The scenario that is modeled is that every person decides in the
morning if they will stay at home or leave their homes to go to work or
shopping. If they go to work or shopping, they will choose a transport
vehicle. If the bus fare is low enough for them, they will take the
bus. Otherwise, they will drive their own cars. The city area that is
modeled has several entry points and depending on the locations of the
population, each person will choose an entry point into the city. People
who go shopping enter and leave the city at random times during the
day, whereas people who go to work have set times for work and,
during working hours, they will reside in the buildings in the city.
Depending on where people are in the city, they will choose a parking
space. If they have electric vehicles, they will charge their vehicles in
the buildings with parking spaces.
In addition, for the implementation of the model in Repast Sym-
phony, there is a structures package, which contains data structures
that are used in different parts of the project. A Utils package contains
the utilities and tools needed by other classes, such as algorithms and
look-up functions. In addition, the CitySIM-Builder class is where all
the initialization and setup for the simulation are done. Finally, the
Reporter class keeps track of the measures, calculates the averages
when new data comes in, and reports it to the GUI for display.
The simulation is designed to show how the traffic evolves during
the day, depending on an individual person’s decision to leave their
homes and their mode of transport. By varying several parameters, such
as the total population of the people, the percentage of the population
that chooses the bus or the car as their transport mode, closing, and
opening entry and exit points in and out of the city, moving the location
of parking spaces, which also include electric vehicle charging stations,
we are able to obtain an overview of how it can affect the traffic
Energy Strategy Reviews 57 (2025) 101613
8

S. Mishra et al.
Fig. 9. CitySIM case – CitySIM case – Agents and environment overview.
situation in the city. In particular, how the traffic situation evolves in
specific areas of the city.
An overview of the simulation environment is shown in Fig. 9
(CitySIM case — Agents and Environment simulation overview). Sev-
eral elements, such as parking spaces, roundabouts, bus stops, and entry
and exit points into this specific area of the city are modeled (see
Fig. 10).
CAS simulations show the emergent behavior in a city and in this
case, it is how the traffic evolves during the day. As the model illus-
trates, there are several entities that are in movement and interacting
with one another, e.g. each vehicle is moving on the roads and avoiding
collisions, some are looking for parking spaces, etc. It is impossible to
show the emergence in 2-dimensional views or graphs. In addition, we
have created a video of the simulation, available at [82]. Unlike several
types of simulations, ABM simulations based on the CAS approach
provide an opportunity to have a qualitative analysis of the situation
as can be seen from the figures and the video.
The main aim of this case study is to illustrate how a city could be
modeled as a CAS. In fact, a city could be considered a system consisting
of several CAS or sub-systems, the traffic is one of them. Hence, this
case study illustrates how several parameters that use the roads and
other entities in a city affect the traffic in the city. The decisions and
choices that lead to the total no. of people and vehicles in cities are
dependent on several factors, such as working hours, no. of people
working in the area, shops in the area (which affect the percentage
of the population that come to the city to shop and at random times),
social and economic factors, such as the ability to pay for higher bus
fares. The CAS model provides an opportunity to vary such parameters
and run simulations.
The model has the potential to simulate the flow and distribution
of energy consumption across the city and throughout the day and
night. Given the high market penetration of electric vehicles in Norway,
this is an important aspect in the design and implementation of smart
grids and the development of the charging infrastructure. The CitySIM
simulation model is aimed at providing a broader insight into the
parameters that could benefit the planning of energy-related issues,
e.g. where people are located, where they park and charge their cars,
how much time they spend driving, which also has an energy cost.
The complexity of energy transitions in a city and the diverse in-
teractions that lead to de-centralized, emergent behaviors in cities that
affect the energy picture can be challenging to capture through linear
modeling approaches. CAS and ABM provide an appropriate means of
representing such scenarios and highlighting the implications of small
local-level changes that affect the overall behavior of the system; in the
case of CitySIM, the decisions of individual citizens’ decisions about
their daily transportation mode, or closing off a road in a city, and
how such individual decisions could affect the overall traffic picture of
certain areas in the city. CAS enables modeling of diverse entities and
how they relate to one another and these can be important in making
decisions at the city level.
2.3. ABM for distributed microgrid expansion planning
Multi-agent system perspectives have been discussed in [83] where
authors proposed a coordinated planning approach for electrical mi-
crogrid (MG) expansion under uncertainty, called CoMG. The main
objective of the work was to propose new approaches to address
the expansion planning problem of MGs, by integrating traditional
optimization models within multi-agent frameworks, and developing
a coordination and communications strategy between MGs. The main
motivation behind the CoMG multi-agent framework is the need to
address the transition between the traditional centralized power grid
towards the current decentralized and distribute grid where peer-
to-peer communication between consumers and prosumers becomes
crucial. Because of the integration of renewable energy sources, such
as wind and solar, into modern power grids, electricity generation is
increasingly occurring in a distributed manner, with MGs representing
the primary distributed power generation sources. MGs cover a tiny
geographic region and provide novel optimization problems to the func-
tioning of the electric power grid. MGs, in contrast to centralized power
generation sources, frequently have a variety of sources of electricity
generation. Power is sent in both directions. As a result, it becomes
more difficult to maintain a balance between demand and supply,
maintain an appropriate power reserve, and maximize resource use.
New approaches for coordinated MG expansion planning are required
in order to meet these issues. The CoMG framework is one of them.
While mathematical optimization has been widely used for decision-
making within both electrical and thermal energy systems, its applica-
tion to more modern problems coupled with multi-agent approaches is
relatively new. The CoMG framework utilizes multi-agent approaches
for MG expansion through optimization and math heuristics. It is a
novel application of computer science to an energy and power systems-
related problem, and it, therefore, falls within the so-called Energy
Informatics domain where smart energy and power systems modeling
is a core sub-field [6].
A summary of the overall concept that underpins the CoMG model
with a focus on the agent configuration is shown in Fig. 11.
Three levels of the agent, each with its own set of strategies and
functions, are depicted. It is allocated for internal operations, such as
scheduling dispatchable generation, maximizing the use of renewable
resources, and controlling storage units to their optimum performance
in the primary layer. The secondary layer provides accurate optimiza-
tion in terms of the most cost-effective investments in generation and
transmission expansion. The third layer is dedicated to information
organization, and it is responsible for coordinating information sharing
and exchange. It will collect information on the marginal cost of genera-
tion for each MG, the energy needs of each MG, and the excess energy
produced in each MG from conventional plants and energy produced
from renewable resources. As part of this process, the tertiary layer will
collect and distribute information, making it available to the MG so that
they can make informed decisions. The third layer keeps track of the
Energy Strategy Reviews 57 (2025) 101613
9

S. Mishra et al.
Fig. 10. CitySIM case — Agents and Environment simulation overview.
Fig. 11. Graphical representation of the main actions performed by an agent within
the CoMG optimization framework.
Fig. 12. Graphical representation of an agent within the CoMG optimization frame-
work.
grid’s status and receives updates from other agents. An agent’s level
of coordination in decision-making is depicted in Fig. 12.
At level t-2, each MG is responsible for solving its own optimization
problem, which we shall refer to as ‘‘self-contained optimization’’. It is
at this level that the necessity for energy transactions is determined
since each MG will calculate energy requirements that exceed energy
availability. At level t-1, each MG will exchange information with
the rest of the neighborhood (during the information sharing stage,
information is broadcasted and received). After then, at level t, each
Fig. 13. Communication strategy, enumeration versus evolutionary sequencing algo-
rithm EVS [83].
MG will solve its optimization problem by taking into consideration
the information obtained from the other MG, along with the possibility
to develop connections and conduct transactions.
The reader will note that each action depicted in Fig. 12 is contained
in circles of different sizes. This refers to the time required for each
action to be finalized. Self-contained optimization takes a long time to
solve (for big instances it can take hours or even days), while informa-
tion sharing takes less time, (in the form of seconds), and transaction
decisions are even faster since the availability of information provided
by the previous actions allows a fast response at the final stage. For the
sake of communication, MGs are categorized by their size, the capacity
of their generation units, and the capacity of their transmission lines.
There are three different capacities: high, medium, and low, as well
as three different sizes: big, medium, and small. Following that, several
communication tactics might be implemented. The authors present an
evolutionary sequencing (EVS) methodology that lowers the number of
permutations that must be performed. An example is shown in Fig. 13.
Here a, b, c refer to different types of MGs obtained from different
combinations of capacities and sizes. Two MG will solve their self-
contained optimization problem simultaneously, lock their decisions,
and then send their output to the third MG, who will make the final
decision based on the information they have received.
The experiments that were performed in [83] showed that, when an
MG receives information from neighboring MGs, they are able to make
informed decisions and they are encouraged to establish new connec-
tions between them, resulting in fewer new generation infrastructure
installations compared to the basic self-contained optimization. Indeed,
MGs can receive electricity from the neighbors as a result of recently
Energy Strategy Reviews 57 (2025) 101613
10

S. Mishra et al.
constructed connections. More often than not, the cost of establishing a
new connection with a peer is less expensive than the cost of installing
a new generation infrastructure. The experiments showed how capacity
constraints, market, and competitive pricing can all affect peer-to-peer
communication decision-making.
The models were tested with data from three islands off the coast of
Norway, and they were commissioned to provide answers to problems
that were of interest to the local system operator at the time. Especially
with the emergence of intelligent technology, such as smart metering
and thermostats, this strategy is now easily adaptable to other types of
MGs. The coordinated MG is intended to make it easier for diverse MG
agents (in this case, functional entities that share information) to collab-
orate in decision-making for both operational planning and investment
decisions. MGs can collaborate in order to ensure that existing resources
are utilized to their full potential. They can also determine whether or
not the installation of new resources in a neighboring MG region is a
wise investment. When evaluating these options in isolation, there are
numerous downsides to be aware of. In the case of fresh investments
in an MG, a neighboring MG may choose to join in those investments
rather than pursue its own investments in the future. The findings of
the models demonstrate that significant improvements in both planning
efficiency and resource usage can be achieved. In six out of nine
situations, the coordinated decision-making technique outperformed
self-contained hierarchical decision-making, and the strategy resulted
in cost savings that were possible for all MGs. In some cases, the
expected profit growth can reach as high as 13 percent of the total
revenue.
In a nutshell, the advantages can be summarized as follows:
• MG planning that is more efficient
• Profit increases of up to 13 percent have been observed.
• The development of a new approach for coordinated MG planning
The results of the experiments led to the conclusion that the value
of coordination resides in the additional profit earned by a single MG as
a result of coordination or synchronization with peers. In comparison
to a self-contained hierarchical decision-making approach, the coordi-
nated decision-making strategy outperforms it. On the methodological
side, the sequence in which MGs are organized has an impact on the
potential profit, and as a result, there is a need for additional research
in this area to better understand the impact of different communication
strategies. On the application side, the proposed methodology should
be further tested and shaped for other problems, such as network re-
structuring and reconfiguration that have been first introduced in [84],
while a more advanced multi-horizon version was proposed in [3].
Indeed peer-to-peer communication between MGs has the potential to
minimize and/or delay costly investments in network restructuring and
reconfiguration that arise within the power systems as a consequence of
the increasing energy demand and the increasing maintenance costs of
power lines. In addition, a multi-agent approach would be beneficial
to analyze long-term investment decision-making of novel technolo-
gies, such as pumped thermal electricity storage [85]. By coupling
it with machine learning algorithms, the multiagent approach can
become a powerful methodology to apply within the cyberspace of
cyber–physical energy systems as outlined in [86].
The proposed CoMG approach is a multi-agent system MAS and as
such, it is a type of ABM. The results of the experiments demonstrate
the value of an agent-based approach to enhance decision-making for
optimal investment decisions within power systems. An approach based
on peer-to-peer transactions is more realistic in the current decen-
tralized scenario. In addition, solving subproblems within each MG
and establishing communication protocols between them have positive
effects on the computational time required to reach a solution.
2.4. ABM for electricity market simulation (PowerACE)
PowerACE is an agent-based simulation model for the analysis of
liberalized electricity markets. The initial development of PowerACE
only considered the German market. However, over the past years
the scope of the model has been extended by adding major European
market areas [87]. The focus of PowerACE lies on the simulation of
European liberalized electricity markets considering model-endogenous
yearly investment decisions. The model enables the investigation of a
wide range of different scientific research questions, which allows, for
example, the evaluation of different market designs and technologies
on the European electricity markets [25,88].
As shown in Fig. 14 a central role in PowerACE is taken by different
agents that represent market participants, such as various traders,
regulators, and consumers [89]. Agents can interact with their environ-
ment dynamically by choosing appropriate actions. For the selection
of suitable actions, decision-making algorithms are implemented for
each agent. A decision-making algorithm can be based on a variety
of different methodological approaches and consequently offer high
flexibility.
Supply agents refer to big European utility companies that bring
their dispatchable power plants to the market. Renewable agents create
bids for priority feed-in of RES and offer these bids in the market.
The hourly inelastic demand is marketed by demand agents. Further
agents for electricity storage technologies, e.g., pumped hydro or bat-
tery, schedule the operation and submit the corresponding bids to the
markets [90]. Additional agents dispatch flexibilities from sector cou-
pling technologies, such as hydrogen electrolyzers [91] and controlled
chargeable electric vehicles [92]. The operating strategies of respective
sector coupling technologies can be varied with respect to different
objectives, such as CO2 minimization, dispatch cost minimization, or
load smoothing. Lastly, operator agents manage the market framework,
wherein bids can be submitted and the market outcome by market area
is calculated.
Decisions within a PowerACE electricity market simulation can be
characterized by short-term and long-term decision levels. For the
short-term simulation, PowerACE assumes the day-ahead spot market
as the best estimate for all electricity markets. However, further market
segments i.e., the control reserve markets, are at least rudimentarily
included. In each simulation, multiple demand and supply agents per
market area participate. On each simulation day, the following four
steps are performed:
(1) Forecasting: At the beginning of each spot market simulation
step, the agents create an hourly price forecast for the following day.
The forecast gives the agents information about the market environ-
ment. (2) Bidding: Agents prepare hourly demand or supply bids to
buy or sell electricity on the spot market. Hereby, each trader agent
can submit multiple bids for each hour of the subsequent day. The
bidding strategy of each agent depends on the predefined settings. (3)
Market clearing: After the submission of all bids, the operator agent
is called and the market clearing algorithm is executed. Here, a linear
optimization model is used to determine the market outcome (dispatch,
cross-border flows, and wholesale market price) with the objective of
maximizing the total welfare of all considered market areas subject
to limited cross-border transmission capacities, balanced energy flows,
and fulfilling the demand. (4) Dispatch: Subsequently, each supply
agent aggregates its accepted bids and thus determines its individual
load curve. Based on this demand to be met, each supply trading agent
determines its daily power plant dispatch. For the spot market, the bids
submitted by the agents for the individual market areas are collected
by the market coupling operator.
In the long term, agents decide annually on the construction of
new power plants based on the expected profitability of potential
investment options, e.g., dispatchable power plants, battery storage
facilities [88,90,93,94]. The underlying investment planning scheme is
Energy Strategy Reviews 57 (2025) 101613
11

S. Mishra et al.
Fig. 14. Schematic overview of the main parts of the electricity market simulation model PowerACE [89].
Fig. 15. Simplified schematic process overview of investment planning in PowerACE [89].
illustrated in Fig. 15. Capacity remuneration mechanisms that incen-
tives large-scale investments in order to ensure long-term generation
adequacy have been introduced in many European countries over the
past decade. These mechanisms have a significant effect on investment
planning and consequently the generation portfolio. Therefore, various
capacity remuneration mechanisms have been implemented in Power-
ACE, i.e., capacity payments [95], a central buyer [96], decentralized
obligations [97], and a strategic reserve [98].
Key outputs in PowerACE are hourly, i.e., spot market prices,
facility-level dispatch decisions, flexibility operation decisions, CO2
emissions, cross-border flows, long-term capacity developments, under-
lying investment decisions and decommissions, and ex-post profitability
analyses. This has enabled numerous studies to be carried out with
PowerACE in the past, only some of which are listed here. First,
research was conducted by [25] on the possible market power be-
havior of large power generation utilities in Germany. This work was
followed by further investigations. Generation security and welfare
in the Central Western Europe-area was researched by the authors
in [87]. The potential future impact of the introduction of capacity
remuneration mechanisms in Germany was considered in [96]. The
Energy Strategy Reviews 57 (2025) 101613
12

S. Mishra et al.
authors in [99] analyzed the different price drivers on the German
spot electricity prices, such as commodity prices of gas, coal, or carbon
certificates. Ensslen et al. [92] investigated the market impact of
smart charging control of EVs on the German and French electricity
markets, while [100] examined the impact of storage systems under
capacity remuneration mechanisms. A study on cross-border effects
on the Swiss electricity market due to market design changes in
neighboring countries was provided by the autors in [94]. But also on a
methodological level, regarding differences in modeling, a comparison
of PowerACE with two optimizing models was addressed in [101]. This
small selection of studies illustrates the flexible applicability of the
PowerACE agent-based electricity market simulation model.
To give a better understanding of PowerACE’s field of applications
we present some exemplary results of previous studies subsequently.
The boxplots in Fig. 16 show the electricity spot market prices that
were determined in a study regarding state-based or market-based
investments in new French nuclear power plants in the upcoming years.
More specifically, the market impact of new nuclear power plants in
the context of increasingly interconnected European electricity markets
with high RES share was investigated. Typically, when working with
PowerACE, several scenarios with different parameterizations are cal-
culated. Thus, for the study about French nuclear power plants prices in
two scenarios (state-based investments and market-based investments)
are considered with a long-term horizon until the year 2050. In addi-
tion to France, the electricity markets of neighboring countries were
highlighted in the study. This illustrates the large geographic scope of
PowerACE.
When looking at the values that are displayed in the boxplots, the
average prices in the different market areas appear to be synchronized
in large parts. This can be attributed to the market coupling and the
expansion of trans-border trading capacities. The endogenous-driven
(state-based) investment results in the overall lowest average prices.
In conclusion, the prices indicate a large impact of the French market
on the prices in the neighboring market areas.
The major challenge in the power system is the temporal mis-
match between financial and physical fulfillment. PowerACE was one
of the first agent-based models to enable the tradeoff between modeling
deregulated electricity markets, taking into account numerous technical
details, multiple market areas, and a wide variety of actors active
in the market. These four dimensions often cannot be represented
jointly from other model classes. In particular, PowerACE’s ability
to model imperfect markets provides an excellent analytical tool, es-
pecially when investigating market designs to identify and eliminate
misaligned incentives early on.
In summary, PowerACE is a comprehensive model that can serve as
a sustainable and powerful tool for analyzing electricity markets and
their effects due to the various methodological extension possibilities.
3. Discussions and characterization of ABM tools
The previous section illustrated how an agent-based model can
facilitate simulation and decision-making in four key segments of the
energy transition. In [102] authors have listed a comprehensive enu-
meration of ABM tools. The authors compared the tools using a list
of specifications. However, there is a knowledge gap in comparing
or characterizing the ABM tools for the energy sector. Moreover, a
framework is required to characterize ABM tools. The following state-
ments before the table of framework explain the reasoning behind
it from the experience of the Authors who developed several tools.
Typically, a framework is a real or conceptual structure that is meant
to act as a support or guide for the construction of something that
develops the structure into something useful. A framework’s objective
is to aid in development by providing standard, low-level functionality
so that developers may concentrate their efforts on the components
that distinguish the project. Using high-quality, pre-tested functionality
improves software stability, reduces development time, and simplifies
testing. The goal of frameworks is to provide a common structure so
that developers do not have to reinvent the wheel and may reuse the
code given. In this way, frameworks enable us to eliminate much of the
labor and save a significant amount of time.
In this section, a novel framework to characterize such tools is
developed and presented. The framework has 12 metrics ranging from
methodology, agent variety, decision level, data variety, data horizon,
model horizon, granularity, efficiency, uncertainty, randomness, model
complexity, and availability. Together the metrics reflect how a certain
ABM tool fairs in a specific decision-making objective — such as, how
CoMG reflects the power system expansion planning problem. The
framework is then validated by applying it to the models included in
the study. Specifically, the framework explains how a specific ABM tool
aids in decision-making for a set objective. In Table 1 the developed and
proposed metrics are elaborated with descriptions.
Models are often data-dependent. Specifically, the variety and ve-
locity of the data set impact the model and simulations. For instance,
character-type data typically leads to a qualitative decision as opposed
to a quantitative one from the numerical one. Simulations are depen-
dent on both the volume and velocity of data. Digitalization of the
energy sector has increased the volume of data that is available. The
implementation of the Internet of Things results in more and more
near-real and real-time data sets. ABM tools are typically dynamic that
enable the introduction of high velocity and volume of the dataset
in the simulation. However, the threshold to which the integration is
possible varies among different models.
Efficiency is a typical metric that applies to most modeling tools.
Efficiency could be expressed temporally through a time of conver-
gence and iterations per minute. The programming language used to
write the model is a determinant of further development operations,
maintainability, and adaptation. There are several ABM packages in
practice, such as Java agent-based modeling toolkit [103], MESA in
python [104], and Agents in Julia language [105] and NetLogo [106].
Uncertainty and variability in the physical world have remained
a challenge in physics-oriented modelings, such as non-dispatchable
RES. Adding to that, human behavioral aspects bring forwards some
predictable actions while increasing the complexity of modeling. Agent-
based modeling fits well in such context as presented in the previous
section. ABM tools are effective in simulating complex and dynamic
environments that adapt well to physics-informed energy modeling.
How uncertainty is addressed in ABM is an important distinction be-
tween various ABM tools. For instance, if variability is considered, and
if spatial or temporal uncertainties are handled. Complexity can be
understood as a result of uncertainty and variability. Complexity can be
a part of the model, such as designing the reward function. It could also
be a part of the decision-making process. Thereby complexity could be
a metric to classify ABM tools. One method to reduce complexity could
be flexibility. Flexibility in ABM tools could be assessed through the
methodology behind the model. For instance, a rule-based method has
little to no flexibility at all and the rules for application must be unam-
biguous. The availability of a model, for instance, if it is open-source
and commercial solvers to solve a model are also factors to consider.
Beyond that, model sizes also vary depending on various factors, such
as the programming language and the method of modeling.
As highlighted in earlier sections, agent-based modeling offers sig-
nificant advantages for analyzing energy systems. However, it is still
an emerging approach in energy system modeling with limited com-
prehensive reviews available. Given ABM’s bottom-up approach, it
paves the way for numerous research opportunities. Considering the
scarcity of publications, our newly developed metric becomes especially
valuable for energy system planning. This metric empowers researchers
to grasp a clearer understanding of ABM’s impact on energy system
modeling.
To validate the proposed framework, the metrics are applied to each
ABM in this study. The Table 2 lists the metrics and corresponding
values for each ABM. The selections and reasoning for them are further
elaborated in the following subsections.
Energy Strategy Reviews 57 (2025) 101613
13

S. Mishra et al.
Fig. 16. Box plots of spot market prices between 2030 and 2050 for all market areas surrounding France with a comparably high CO2 emission allowance price path; outliers are
removed. The average is indicated as a diamond. None of the prices take into account levies for Gid, RES, or CRM [89].
Table 1
Framework with metrics for evaluation of agent-based models.
Metric Description
Methodology What is the method used for modeling? Rule-based/optimization/ etc.
Agent variety How different are the agents from one another (if it is a multi-agent model) and how the agents are linked
Decision level Are the decision(s) made at an individual agent or at the system level?
Data variety Varieties of data processed, High = mixed (alphanumerical, spatial) inputs, Low = only numerical
Data horizon When/How is the input data measured/generated? (Historical/ near-real-time/ future predictions)
Model horizon Planning horizon of the specific tool, Short (near real-time)/medium (weeks-year)/long-term (more than 5 years)
Model granularity What is the time step of the simulation?
Efficiency Typical computational time to reach a solution. (Expressed in minutes)
Uncertainty If and how the uncertainty is handled in the model? (Stochastic/sensitivity analysis/iterative/stochastic dynamic/etc. If not handled, then
N.A.)
Randomness If there is randomness involved in the model or in data generation?
Model complexity Lines of code/number of processes/steps to reach the final solution/number of agents/amount of equation/size of
formulation/computational time per agent
Availability Tool freely available but code as a black box/tool freely available and code available/only data available/Partially available data/private
only
Energy Strategy Reviews 57 (2025) 101613
14

S. Mishra et al.
Table 2
Evaluation of ABM characteristics based on the proposed framework.
Behavior City dynamics Microgrids Energy market
Methodology Rule based Complex adaptive system Stochastic optimization Combination
Agent variety Heterogeneous, non-linear
dependence
Heterogeneous Homogeneous agents, linear
dependence
Heterogeneous and non-linear
dependency
Decision level Agent System System Agent (short-term) and System
(long-term)
Data variety High High Low Very high
Data horizon Historical surveys Historical Future predictions Combination
Model horizon Long term Medium Medium Combination
Model granularity Weeks Minutes Hours Hourly
Efficiency 1–2 min 12 h 5760 min 4000 to 8000 min
Uncertainty Sensitivity analysis Iterative Exact Sensitivity analysis
Randomness Yes No No No
Model complexity 430 agents, 2600 steps (1 step
per week for 50 years)
10 types of agents, agent
population >100
3 types pf agents, exact
solution
25–50 agents per Market
Area, 16 Market areas
Availability Open source Private Dataset available Private
3.1. Characterization of ABM for consumer behavior
As mentioned in the introduction, behavioral ABMs can be roughly
divided into financial-rational and psychological-behavioral systems.
While the latter has historically received less attention [35], its role
in energy system models is growing. In order for energy system models
to encompass end users, the behavioral perspective must be included.
The HERB model is an example of an ABM based on a psychological-
behavioral perspective focused on household energy retrofitting and
subsequent energy use for heating. Here, agents are based on previous
behavioral research regarding private household energy retrofitting
[69,70].
As the agent’s behavior is based on previous behavioral research,
it could be said to be rule-based. All agents are parameterized on
an individual real-life survey respondent, making each agent unique.
The agent is linked through a small world [107] system that does not
change. All decisions regarding behaviors are made on an agent level.
As both ‘hard’ factors, such as building energy standard, retrofitting
costs, and neighborhood retrofitting rate, as well as ‘soft’ factors, such
as worry, social desirability, self-efficacy, comfort, and personality,
are simulated, the data variety is high. As the agents are based on
survey responses, the data horizon is historical. Although the model can
simulate shorter time periods (1–2 years), it is best suited for long-term
simulations and thus has a long-term model horizon (20+ years). As
retrofitting decisions do not happen frequently, the model granularity
is one week. Although the model can under most circumstances reach
a single solution rather quickly (2.5 m), one solution is rarely enough
to answer a research question the model is fit for investigating, and
hundreds or thousands of simulations are usually needed. The uncer-
tainty caused by the lack of research on the behavior is handled by
sensitivity analysis. Randomness exists in the model to account for
unknown factors, true randomness in behavior, or free will. The model
is fully available to download at [108].
As the model reflects behavioral research regarding household en-
ergy retrofitting, its strengths lie in a valid representation of human
behavior. The model agent’s rules are as representative of human
behavior as the research allows. Thus, the methodology of the model
can be said to be its strength. Simultaneously, relying on behavioral
research leaves a lot of uncertainty in the model. Firstly, ‘‘translating’’
psychological parameters into code is a highly subjective undertaking,
as there is no way to objectively represent variables, such as expected
comfort in code. Secondly, no behavioral science can explain 100%
of a behavior. Therefore, random variability due to unknown factors
must be included in the model, further raising the uncertainty of the
model. Thus, the model’s uncertainty and randomness can be seen as
its weaknesses. As soon as more behavioral research emerges regarding
household energy retrofitting behavior, this will improve the model and
should be implemented. To alleviate these weaknesses, the simulation
is run numerous times. This way, a mean effect, and distribution can
be presented in the results. From there, the researcher can present
the ‘‘most likely’’ change in energy consumption as a result of the
implemented policy. Note that this distribution of results is somewhat
different from ‘‘scenarios’’ presented in other models [109]. The dis-
tribution of results in the HERB model represents true uncertainty
as a consequence of unpredictable human behavior, not variation in
circumstances. In the end, models based on behavioral research trade
accuracy for validity, creating inaccurate but well-founded models. If
the research question the researcher is addressing allows him or her to
be roughly right rather than precisely wrong, behavioral modeling can
be a solid option.
3.2. Characterization of ABM for city dynamics simulation
Cities have been described as Complex Systems, where the overall
behavior emerges due to the behavior of its components [77]. However,
the application of ABM and particularly CAS at the city level are
limited. In [81], Batty explored the emerging properties on a city
scale. The CAS approach has also been applied at the regional level to
understand innovation systems, the competitive environment, and how
the behaviors of the agents adapt to the environmental changes [110].
The CAS is a MAS, where there are multiple types of autonomous
agents that represent the different types of entities within a city and
the relationships among them. Each agent makes decentralized au-
tonomous decisions, based on very simple rules and the current state of
their environment. A single agent does not process such data. However,
the system itself calculates a new set of values that reflect the behavior
of the whole system frequently, which makes the system computation-
ally resource-intensive and is, thus, the main factor affecting efficiency
due to the long processing time. In fact, the simulation of the behav-
ior of each agent and their collective behavior, which represents the
emergent nature of the whole system, can provide a more complete
and complex view of the system at the expense of efficiency.
CitySIM model and simulations can be of benefit to several stake-
holders. For example, urban designers may find it useful to experiment
with such a model to determine the various elements and their locations
and distributions within a physical area. A municipality or a city
planner or a service provider, such as parking services or electrical
charging stations, can benefit from such a model. Given the wide
spectra of parameters, opportunities, and stakeholders for such a model,
the focus is on the emergence arising from the interactions of the
different entities and to support qualitative assessments and support
decision-making. The visualizations of emergence and how the city
evolves as the parameters are varied, provide a medium for discussions
among stakeholder groups.
One of the main limitations of CAS and ABM models is, as with
any form of modeling, the accuracy of the models and the assumptions
Energy Strategy Reviews 57 (2025) 101613
15

S. Mishra et al.
the model is based upon. The case of CitySIM, which is our starting
point for the development of a CAS model for a city has focused on the
interactions among the entities to gain experience with the modeling
and simulation. The models have been presented to CAS modeling
experts, energy experts, and city planners who have all expressed their
interest and provided positive feedback. CitySIM has paid less attention
to making accurate models based on data and evidence, which will be
a part of our future work. A technical challenge with CAS simulations
is the computational resource demands and the time it can take to run
simulations with several parameters.
3.3. Characterization of ABM for expansion planning of distributed micro-
grids
The model ComG is based on a math-heuristic formulation that
combines a unique heuristic multi-agent approach together with an
embedded mathematical optimization model based on exact methods.
The embedded mathematical optimization model tackles investment
decisions and operational decisions, with the latter handled through a
stochastic formulation that accounts for uncertainty in demand, prices,
and renewable production.
The data variety is low since only numerical data are involved.
The dataset is based on predictions achieved through ARIMA-based
formulations. Data are partially available upon request. The time hori-
zon is one year, with a capital recovery factor that accounts for the
forecast lifetime of each investment, and a granularity of one hour for
the operational decisions. The computational time increases with the
size of the problem, and with the size of the stochastic tree that directly
depends on the number of scenarios included.
The combination of math-heuristic multi-agent formulations and
exact mathematical optimization methods is the main strength and
novelty of the CoMG model. The decision-making approach is based
on microgrid communication in the form of agents. This represents a
novel paradigm within energy and power systems modeling, based on
peer-to-peer communication. The decentralized approach adopted by
the model, the unique ABM approach, and the focus on renewable en-
ergy investment and operational decisions with stochastic approaches,
make CoMG an appealing decision support tool for a variety of anal-
yses within the ongoing energy transition towards low carbon energy
systems.
Nevertheless, the CoMG approach has some weaknesses that will be
improved with further research. The one-year horizon is a limitation
in the context of the energy transition since multi-horizon approaches,
such as those proposed in [111] could be developed and tested, in
order to tackle future projections in demand development and invest-
ments of resources. In addition, the hourly granularity of the model
may be improved and smaller granularity could be implemented for
the operational decisions that are optimized behind the investment
decisions. The partial data availability is another aspect that could be
enhanced. Data could be normalized and anonymized to make them
openly available and facilitate analyses for researchers involved in
the energy transition. Finally, the computational time due to the use
of exact methods for the optimal decisions within microgrids could
represent a challenge when analyzing bigger instances, when many
agents are involved, when a smaller granularity is needed, and when
more complex forms of communication are implemented. Advanced
decomposition techniques should be developed and tested to address
such issues.
As highlighted in [11], human energy behavior is nowadays a very
important trend of decision-making within the energy transition. How-
ever, it is often neglected and oversimplified when optimization-based
decision support systems tools are developed. Even though some works
like [11,112–114] kick-started the discussion, modeling the social and
human aspects of energy transition and energy use in ways suitable for
inclusion within mathematical optimization models is still a challenge
and open field of research. Therefore future trends and directions for
multi-agent approaches like CoMG should also consider the inclusion of
human energy behavior variables to achieve more realistic modeling of
the studied systems.
3.4. Characterization of ABM for electricity market simulation
Modeling complex electricity markets with a sufficient level of
detail requires comprehensive and efficient simulation models. Over
the course of the past decades, ABM has been deployed in an increasing
number of applications and is to date among the most commonly used
approaches in modeling electricity markets [115]. This development
was facilitated as the behavioral level of market participants became
increasingly important with the liberalization of European electricity
markets [115]. Due to its explorative nature, ABM allows the re-
flection of non-optimal but real-world behavioral patterns of market
participants when analyzing electricity markets. Notable agent-based
simulation tools for analyzing one or multiple European electricity
markets include AMIRIS [116], EMLab [117], and PowerACE.
Agents in PowerACE have very diverse roles, objectives, and action
sets. The concrete method and (agent or system decision) level depend,
among others, on the decision horizon. Price time series for fuels and
carbon allowances, profiles of RE generation, demand time series, or
behavioral studies in mostly hourly or daily resolution are just some
of the comprehensive and varied input data of PowerACE. In addition,
block-level power plant data with techno-economic parameters are fur-
ther included. This input data is based on historical and scenario values
that will typically be needed until 2050. PowerACE simulates annually
in hourly resolution until 2050. The model efficiency, indicated by the
run time, largely depends on the scenarios to be investigated and ranges
between 4000 to 8000 min. The complexity of PowerACE is high and
can only partially be derived by the number of agents. The complexity
can only be partly derived from the number of agents since, for each
large utility, there may also be different power plants whose individual
hourly bids have to be determined. In addition, other technologies
are aggregated but still needed for each market area. PowerACE is
deterministic and only handles uncertainties by modeling different sce-
narios/sensitivities. The model code is currently not publicly available
but is expected to be published in 2023.
The close-to-reality representation of European electricity markets
and relevant stakeholders is a strength of PowerACE. In contrast to
optimization models, imperfect markets and decisions can be depicted.
The high level of detail combined with a large geographical scope
allows the analysis of a wide range of multinational aspects with
PowerACE, e.g. investment and dispatch decisions, electricity price
developments, market designs, cross-border effects, or business models
of the stakeholders.
PowerACE, like all other models, simplifies reality, which brings
certain limitations. Particularly the representation of renewable ener-
gies in PowerACE can be improved. At present, renewable energies are
aggregated in feed-in profiles and bid in the electricity market with
priority at zero marginal cost. However, as the share of renewables
increases, new bidding strategies are necessary to cover their invest-
ments. Introducing other bid types, e.g., linked block bids could ease
the integration of flexibilities and storage facilities. Extensions that
address these limitations are planned and implemented in the future.
Another major challenge is the complexity of the execution (long
run times) and the interpretation of the broad results. They require
a detailed understanding of the model, which can lead to incorrect
conclusions without knowledge.
The future of ABM is strongly linked to the future of markets. As
long as energy, and particularly electricity, is traded in markets, ABM
has a justification for existence. Optimization models, however, may
be easier to operate and interpret, but market rules, as well as the
behavior of all participating agents, are never perfect, so adjustments
must be made constantly, and impacts on the target (e.g., efficient
dispatch, climate neutrality) must be investigated. One obstacle may
be the complexity of models with many actors and markets, which the
modeler must always take into account and make simplifications where
necessary.
Energy Strategy Reviews 57 (2025) 101613
16

S. Mishra et al.
4. Concluding remarks
The sustainable energy transition will require changes in four in-
vestigated segments of the existing energy system — consumer en-
gagement, city dynamics, distribution or micro-level grid structure,
and the energy markets. The challenges in policymaking will expand
as the characteristics of decision-making change. The 5-Ds act as a
driver of this change — decentralization, distribution, decarbonization,
digitalization, and democratization. To enable such a transition in the
decision-making process the existing modeling tools are to be revised
and new tools are to be developed.
Engaging different stakeholders at various levels is claimed to ‘de-
mocratize’ the energy sector. Challenges for future research can be
summarized as follows.
• Different stakeholders even at the same level, can have very
different preferences, and finding solutions that satisfy all, or even
a majority is a difficult task, often involving compromises
• multi-stakeholder analyses should in general be conducted using
multi-criteria methods in general and multi-objective optimiza-
tion in particular.
• Omitting the multi-criteria element in ABM modeling will easily
lead to ‘segregation’ effects
This work identified, described, and characterized agent-based mod-
eling tools for a sustainable energy transition. A framework is required
to characterize and compare several tools for a particular application.
Note that, it is hard to develop and verify such characteristics as ABM
are fine-tuned for a particular application. Therefore, such a framework
to evaluate an agent based model is developed, proposed, and vali-
dated. This framework has 12 metrics to characterize an agent-based
model. The proposed framework is tested by applying it to the selection
of agent based models. In validation, the framework accurately and
holistically elucidates — how does an agent based model perform in
terms of data, method, variety, decision, efficiency, and availability?
From there emerge the patterns and trends of agent-based models
outlining challenges, functionalities, and a way forward.
4.1. Determinants of agent-based modeling approaches
• Traditionally analysis in the power sector is based on optimization
models that focus on what solutions should be (normative).
• ABM has become a modeling approach to assess phenomena with
a tight connection to behavioral and social sciences. Thereby,
ABM reflects what solutions could be (explorative).
• Problems can increase in complexity, so more realistic reflections
can be achieved.
• A versatile tool to assess a variety of problems from small to
large-sized systems
Agent-based simulations are becoming more popular in electricity
market modeling to model strategic behavior and provide additional
insight, and future work should focus on reducing the complexity of
such models [118] and developing suitable learning algorithms [119,
120]. The review further showed that the greatest potential contribu-
tion of ABM to energy transition studies lies in its practical applica-
tion to decision-making in policy and planning. More interdisciplinary
collaboration in model development is recommended to address the
discrepancy between the relevance of social factors to modeling energy
transitions and the ability of the social sciences to make effective use
of ABM [121]. Over the years, these models have increased in size
and complexity. Current ABMs can simulate thousands of individuals
in realistic environments and with highly detailed internal physiology,
perception, and ability to process the perceptions and make deci-
sions based on those and their internal states. The implementation of
decision-making in ABMs ranges from fairly simple to highly complex;
the process of an individual deciding on action can occur through the
use of logical and simple (if-then) rules to more sophisticated neural
networks and genetic algorithms [122].
The investigation demonstrates that agent-based models can be an
important part of the modeling suites for the energy transition. It
has key advantages in terms of adaptability, representation of actors,
and digitalization. It also has challenges specifically on a sub-optimal
solution. The way to a holistic transition requires the engagement of
actors at different levels, accelerated by digitalization, an agent-based
model presents an optimal match to find a fitting solution to enable
a sustainable energy transition. Moreover, a shift in decision-making
strategies from a normative to an explorative approach fits well with
agent-based modeling that is both explorative and reflective. While the
agent-based models reviewed in this paper have a granularity of an
hour or more, future research directions could aim at a finer granularity
(like seconds or minutes) to better represent the system dynamics. In
addition to that, multi-criteria decision-making considering stakehold-
ers’ preferences could also be studied to improve the reward functions
of the agents in a multi-agent environment.
Declaration of competing interest
The authors declare the following financial interests/personal rela-
tionships which may be considered as potential competing interests:
Sambeet Mishra reports financial support was provided by Research
Council of Norway.
Acknowledgments
This research work is partly supported by funding from the Norwe-
gian center for energy transition strategies (FME NTRANS), Research
Centre on Zero Emission Neighborhoods in Smart Cities (FME ZEN), the
KPN project the Role of energy behavior in the low-carbon transition
(BEHAVIOUR) under grant agreement 308772 and, H2020 grant agree-
ment 824260. The authors would also like to thank the MSc student
Andre Fosvold for implementing the CitySIM CAS simulation model.
The authors would like to credit flaticon.com as the source of icons in
some of the figures.
Data availability
The authors do not have permission to share data.
References
[1] S. Mishra, C. Bordin, M. Leinakse, F. Wen, R.J. Howlett, I. Palu, Virtual power
plants and integrated energy system: current status and future prospects, in:
Handbook of Smart Energy Systems, Springer, 2023, pp. 115–145.
[2] S. Mishra, E. Ören, C. Bordin, F. Wen, I. Palu, Features extraction of wind ramp
events from a virtual wind park, Energy Rep. 6 (2020) 237–249.
[3] C. Bordin, S. Mishra, I. Palu, A multihorizon approach for the reliability oriented
network restructuring problem, considering learning effects, construction time,
and cables maintenance costs, Renew. Energy 168 (2021) 878–895.
[4] R.P. Allan, P.A. Arias, S. Berger, J.G. Canadell, C. Cassou, D. Chen, A.
Cherchi, S.L. Connors, E. Coppola, F.A. Cruz, et al., Intergovernmental panel
on climate change (IPCC). Summary for policymakers, in: Climate Change
2021: The Physical Science Basis. Contribution of Working Group I To the
Sixth Assessment Report of the Intergovernmental Panel on Climate Change,
Cambridge University Press, 2023, pp. 3–32.
[5] S. Mishra, P.P. Singh, I. Kiitam, M. Shafiq, I. Palu, C. Bordin, Diagnostics
analysis of partial discharge events of the power cables at various voltage levels
using ramping behavior analysis method, Electr. Power Syst. Res. 227 (2024)
109988.
[6] C. Bordin, A. Håkansson, S. Mishra, Smart energy and power systems mod-
elling: an iot and cyber-physical systems perspective, in the context of energy
informatics, Procedia Comput. Sci. 176 (2020) 2254–2263.
[7] C. Bordin, S. Mishra, A. Safari, F. Eliassen, Educating the energy informatics
specialist: opportunities and challenges in light of research and industrial trends,
SN Appl. Sci. 3 (2021) 1–17.
Energy Strategy Reviews 57 (2025) 101613
17

S. Mishra et al.
[8] A.A. Yusuf, H.F. Kesselly, A. Nippae, C. Asumana, M.O. Kakulu, I.S. Sinneh, S.Z.
Gono, R.B. Mayango, A comprehensive review of Liberia’s energy scenario: Ad-
vancing energy access, sustainability, and policy implications, Energy Strategy
Rev. 51 (2024) 101295.
[9] A.Z. Ahwazi, C. Bordin, S. Mishra, A. Horsch, P.H. Ha, Sustainable and
decarbonized data-center facilities: A socio-techno-economic discussion, in:
2021 IEEE PES Innovative Smart Grid Technologies-Asia, ISGT Asia, IEEE, 2021,
pp. 1–5.
[10] C. Bordin, A. Tomasgard, Behavioural change in green transportation: Micro-
economics perspectives and optimization strategies, Energies 14 (13) (2021)
3728.
[11] M. Fodstad, P.C. del Granado, L. Hellemo, B.R. Knudsen, P. Pisciella, A. Silvast,
C. Bordin, S. Schmidt, J. Straus, Next frontiers in energy system modelling: A
review on challenges and the state of the art, Renew. Sustain. Energy Rev. 160
(2022) 112246.
[12] C. Gao, X. Lan, N. Li, Y. Yuan, J. Ding, Z. Zhou, F. Xu, Y. Li, Large
language models empowered agent-based modeling and simulation: A survey
and perspectives, Hum. Soc. Sci. Commun. 11 (1) (2024) 1–24.
[13] M. Kieu, H. Nguyen, J.A. Ward, N. Malleson, Towards real-time predictions
using emulators of agent-based models, J. Simul. 18 (1) (2024) 29–46.
[14] J.-H. Niemann, S. Uram, S. Wolf, N.D. Conrad, M. Weiser, Multilevel optimiza-
tion for policy design with agent-based epidemic models, J. Comput. Sci. 77
(2024) 102242.
[15] Y.S. Liu, M. Tayarani, F. You, H.O. Gao, Bayesian optimization for battery
electric vehicle charging station placement by agent-based demand simulation,
Appl. Energy 375 (2024) 123975.
[16] A. Korah, J.A. Koch, M.C. Wimberly, Understanding urban growth modeling in
Africa: Dynamics, drivers, and challenges, Cities 146 (2024) 104734.
[17] M. Thirunavukkarasu, Y. Sawle, H. Lala, A comprehensive review on optimiza-
tion of hybrid renewable energy systems using various optimization techniques,
Renew. Sustain. Energy Rev. 176 (2023) 113192.
[18] C. Bordin, S. Mishra, F.E. Benth, Pedagogical perspectives of interdisciplinary
teaching and research: An energy system modelling outlook in relation to
energy informatics, Energies 16 (15) (2023) 5757.
[19] R. Akpahou, L.D. Mensah, D.A. Quansah, F. Kemausuor, Energy planning and
modeling tools for sustainable development: A systematic literature review,
Energy Rep. 11 (2024) 830–845.
[20] S. Mishra, C. Bordin, Q. Wu, H. Manninen, Resilient expansion planning of
virtual power plant with an integrated energy system considering reliability
criteria of lines and towers, Int. J. Energy Res. 46 (10) (2022) 13726–13751.
[21] M. Khalid, Smart grids and renewable energy systems: Perspectives and grid
integration challenges, Energy Strategy Rev. 51 (2024) 101299.
[22] M.I.A. Shah, A. Wahid, E. Barrett, K. Mason, Multi-agent systems in peer-to-peer
energy trading: A comprehensive survey, Eng. Appl. Artif. Intell. 132 (2024)
107847.
[23] Y. Zhou, P.D. Lund, Peer-to-peer energy sharing and trading of renewable
energy in smart communities trading pricing models, decision-making and
agent-based collaboration, Renew. Energy 207 (2023) 177–193.
[24] W. Tushar, C. Yuen, T.K. Saha, T. Morstyn, A.C. Chapman, M.J.E. Alam, S.
Hanif, H.V. Poor, Peer-to-peer energy systems for connected communities: A
review of recent advances and emerging challenges, Appl. Energy 282 (2021)
116131.
[25] M. Genoese, Energiewirtschaftliche Analysen des Deutschen Strommarkts Mit
Agentenbasierter Simulation, Nomos Verlagsgesellschaft mbH & Co. KG, 2010.
[26] R. Axelrod, The Complexity of Cooperation: Agent-Based Models of Competition
and Collaboration: Agent-Based Models of Competition and Collaboration,
Princeton University Press, 1997.
[27] L. Tesfatsion, Agent-based computational economics: A constructive approach
to economic theory, Handb. Comput. Econom. 2 (2006) 831–880.
[28] F. Schweitzer, Self-Organization of Complex Structures: From Individual to
Collective Dynamics, CRC Press, 1997.
[29] V. Rai, A.D. Henry, Agent-based modelling of consumer energy choices, Nature
Clim. Change 6 (6) (2016) 556–562.
[30] P. Ringler, D. Keles, W. Fichtner, Agent-based modelling and simulation of
smart electricity grids and markets–a literature review, Renew. Sustain. Energy
Rev. 57 (2016) 205–215.
[31] T.C. Schelling, Models of segregation, Am. Econ. Rev. 59 (2) (1969) 488–493.
[32] M. Hallsworth, A manifesto for applying behavioural science, Nat. Hum. Behav.
7 (3) (2023) 310–322.
[33] X. Liang, T. Yu, J. Hong, G.Q. Shen, Making incentive policies more effective:
An agent-based model for energy-efficiency retrofit in China, Energy Policy 126
(2019) 177–189.
[34] B.M. Sopha, C.A. Klöckner, E.G. Hertwich, Exploring policy options for a tran-
sition to sustainable heating system diffusion using an agent-based simulation,
Energy Policy 39 (5) (2011) 2722–2729.
[35] D. Huckebrink, V. Bertsch, Integrating behavioural aspects in energy system
modelling—A review, Energies 14 (15) (2021) 4579.
[36] Net-zero 2050 - European climate foundation, 2022, URL: . [Online; Accessed
5 December 2022].
[37] S. Schlacke, H. Wentzien, E.-M. Thierjung, M. Köster, Implementing the EU
climate law via the ‘fit for 55’ package, Oxford Open Energy 1 (2022) oiab002.
[38] P. NODES, NODES local electricity market, 2022, URL: https://nodesmarket.
com//publications.
[39] M.L. Di Silvestre, S. Favuzza, E.R. Sanseverino, G. Zizzo, How decarbonization,
digitalization and decentralization are changing key power infrastructures,
Renew. Sustain. Energy Rev. 93 (2018) 483–498.
[40] A. Idries, J. Krogstie, J. Rajasekharan, Challenges in platforming and digitizing
decentralized energy services, Energy Inform. 5 (1) (2022) 1–29.
[41] M.P. Moghaddam, S. Nasiri, M. Yousefian, 5D giga trends in future power
systems, in: Decentralized Frameworks for Future Power Systems, Elsevier,
2022, pp. 19–50.
[42] P. Calver, N. Simcock, Demand response and energy justice: A critical overview
of ethical risks and opportunities within digital, decentralised, and decarbonised
futures, Energy Policy 151 (2021) 112198.
[43] E. Judson, O. Fitch-Roy, I. Soutar, Energy democracy: A digital future? Energy
Res. Soc. Sci. 91 (2022) 102732.
[44] T. Ma, Y. Nakamori, Modeling technological change in energy systems–from
optimization to agent-based modeling, Energy 34 (7) (2009) 873–879.
[45] M.J. Wooldridge, N.R. Jennings, Intelligent agents: Theory and practice, Knowl.
Eng. Rev. 10 (2) (1995) 115–152.
[46] M. Melliger, E. Chappin, Phasing out support schemes for renewables in
neighbouring countries: An agent-based model with investment preferences,
Appl. Energy 305 (2022) 117959.
[47] Y.S. Lee, A.M. Malkawi, Simulating multiple occupant behaviors in buildings:
An agent-based modeling approach, Energy Build. 69 (2014) 407–416.
[48] C.M. Macal, Everything you need to know about agent-based modelling and
simulation, J. Simul. 10 (2) (2016) 144–156.
[49] Y. Wei, X. Liang, L. Xu, G. Kou, J. Chevallier, Trading, storage, or penalty?
Uncovering firms’ decision-making behavior in the Shanghai emissions trading
scheme: Insights from agent-based modeling, Energy Econ. 117 (2023) 106463.
[50] P. Jain, A. Saxena, A multi-agent based simulator for strategic bidding in
day-ahead energy market, Sustain. Energy Grids Netw. 33 (2023) 100979.
[51] L. Chi, H. Su, E. Zio, M. Qadrdan, J. Zhou, L. Zhang, L. Fan, Z. Yang, F. Xie,
L. Zuo, et al., A systematic framework for the assessment of the reliability of
energy supply in integrated energy systems based on a quasi-steady-state model,
Energy 263 (2023) 125740.
[52] M. Elkamel, A. Valencia, W. Zhang, Q.P. Zheng, N.-B. Chang, Multi-agent
modeling for linking a green transportation system with an urban agriculture
network in a food-energy-water nexus, Sustainable Cities Soc. 89 (2023)
104354.
[53] Q. Qiao, A. Yunusa-Kaltungo, A hybrid agent-based machine learning method
for human-centred energy consumption prediction, Energy Build. (2023)
112797.
[54] V. Grimm, U. Berger, D.L. DeAngelis, J.G. Polhill, J. Giske, S.F. Railsback,
The ODD protocol: a review and first update, Ecol. Model. 221 (23) (2010)
2760–2768.
[55] B. Müller, F. Bohn, G. Dreßler, J. Groeneveld, C. Klassert, R. Martin, M.
Schlüter, J. Schulze, H. Weise, N. Schwarz, Describing human decisions in
agent-based models–ODD+ D, an extension of the ODD protocol, Environ.
Model. Softw. 48 (2013) 37–48.
[56] D.C. Parker, D.G. Brown, J.G. Polhill, P.J. Deadman, S.M. Manson, Illustrating
a New’conceptual Design Pattern’for Agent-Based Models of Land Use Via Five
Case Studies—The MR POTATOHEAD Framework, Universidad de Valladolid,
2008.
[57] H.-K. Ringkjøb, P.M. Haugan, A. Nybø, Transitioning remote arctic settlements
to renewable energy systems–A modelling study of Longyearbyen, Svalbard,
Appl. Energy 258 (2020) 114079.
[58] J. Sachs, Y. Meng, S. Giarola, A. Hawkes, An agent-based model for energy
investment decisions in the residential sector, Energy 172 (2019) 752–768.
[59] T. Wittmann, Agent-Based Models of Energy Investment Decisions, Springer
Science & Business Media, 2008.
[60] A. Krumm, D. Süsser, P. Blechinger, Modelling social aspects of the energy
transition: What is the current representation of social factors in energy
models? Energy 239 (2022) 121706.
[61] M.B. Anwar, G. Stephen, S. Dalvi, B. Frew, S. Ericson, M. Brown, M. O’Malley,
Modeling investment decisions from heterogeneous firms under imperfect
information and risk in wholesale electricity markets, Appl. Energy 306 (2022)
117908.
[62] H. Algarvio, F. Lopes, Agent-based retail competition and portfolio optimization
in liberalized electricity markets: A study involving real-world consumers, Int.
J. Electr. Power Energy Syst. 137 (2022) 107687.
[63] D. O’Sullivan, T. Evans, S. Manson, S. Metcalf, A. Ligmann-Zielinska, C. Bone,
Strategic directions for agent-based modeling: avoiding the YAAWN syndrome,
J. Land Use Sci. 11 (2) (2016) 177–187.
[64] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems
research, MIS Q. 28 (1) (2004) 75–105.
[65] A.R. Hevner, A three cycle view of design science research, Scand. J. Inf. Syst.
19 (2) (2007) 87–92.
[66] R.K. Yin, Case Study Research: Design and Methods, SAGE Publications, 2014.
Energy Strategy Reviews 57 (2025) 101613
18

S. Mishra et al.
[67] E. Costa, A. Soares, J. Pinho de Sousa, Situating case studies within the design
science research paradigm: An instantiation for collaborative networks, in:
Collaboration in a Hyperconnected World, Springer, 2016, pp. 531–544.
[68] L.E. Egner, C. Klöckner, Effect of policy implementation on energy retrofit
behavior and energy consumption in a simulated neighborhood, J. Artif. Soc.
Soc. Simul. (ISSN: 1460-7425) 25 (4) (2022) 7, http://dx.doi.org/10.18564/
jasss.4936, URL: http://jasss.soc.surrey.ac.uk/25/4/7.html.
[69] C.A. Klöckner, Psychological determinants of intentions to upgrade the energy
standards of privately-owned buildings: results from a Norwegian survey, Int.
J. Sustain. Build. Technol. Urban Dev. 5 (3) (2014) 222–229.
[70] C.A. Klöckner, A. Nayum, Specific barriers and drivers in different stages of
decision-making about energy efficiency upgrades in private homes, Front.
Psychol. 7 (2016) 1362.
[71] R. Galvin, Thermal upgrades of existing homes in Germany: The building code,
subsidies, and economic efficiency, Energy Build. 42 (6) (2010) 834–844.
[72] A. Tversky, D. Kahneman, Availability: A heuristic for judging frequency and
probability, Cogn. Psychol. 5 (2) (1973) 207–232.
[73] S.N. (SSB), Income and wealth statistics for households, 2018, URL: https:
//www.ssb.no/en/statbank/table/12558/.
[74] S.N. (SSB), Energy consumption in households, 2018, URL: https://www.ssb.
no/en/statbank/table/10575/.
[75] L.E. Egner, C.A. Klöckner, G. Pellegrini-Masini, Low free-riding at the cost
of subsidizing the rich. Replicating swiss energy retrofit subsidy findings
in Norway, Energy Build. (ISSN: 0378-7788) 253 (2021) 111542, http://dx.
doi.org/10.1016/j.enbuild.2021.111542, URL: https://www.sciencedirect.com/
science/article/pii/S0378778821008264.
[76] A. Fosvold, CitySim: A modular Agent-Based simulation system for Modeling
Cities as Complex Systems (Master’s thesis), Norwegian University of Science
and Technology, 2019.
[77] M. Batty, Cities and Complexity, Understanding Cities with Cellular Automata,
Agent-Based Models, and Fractals, MIT Press, 2005.
[78] J.H. Holland, Studying complex adaptive systems, J. Syst. Sci. Complex. 19 (1)
(2006) 207–232.
[79] Y. Bay-Yam, Agent-Based Modeling: Methods and Techniques for Simulating
Human Systems, Addison-Wesley, 1997.
[80] M. Weisberg, Understanding the emergence of population behavior in
individual-based models, Philos. Sci. 81 (5) (2014).
[81] M. Batty, Complexity and emergence in city systems: Implications for urban
planning, Malays. J. Environ. Manage. 10 (1) (2009).
[82] A. Fosvold, City as complex system, traffic, 2019, URL: https://youtu.be/
Azb7dZai46E.
[83] S. Mishra, C. Bordin, A. Tomasgard, I. Palu, A multi-agent system approach for
optimal microgrid expansion planning under uncertainty, Int. J. Electr. Power
Energy Syst. 109 (2019) 696–709.
[84] S. Mishra, C. Bordin, I. Palu, Rnr: reliability oriented network restructuring,
in: 2018 IEEE 59th International Scientific Conference on Power and Electrical
Engineering of Riga Technical University-RTUCON, IEEE, 2019.
[85] A.A. Ibrahim, B. Kazemtabrizi, C. Bordin, C.J. Dent, J.D. McTigue, A.J. White,
Pumped thermal electricity storage for active distribution network applications,
in: 2017 IEEE Manchester PowerTech, IEEE, 2017, pp. 1–6.
[86] C. Bordin, H.I. Skjelbred, J. Kong, Z. Yang, Machine learning for hydropower
scheduling: State of the art and future research directions, Procedia Comput.
Sci. 176 (2020) 1659–1668.
[87] P. Ringler, D. Keles, W. Fichtner, How to benefit from a common European
electricity market design, Energy Policy 101 (2017) 629–643.
[88] C. Fraunholz, Market design for the transition to renewable electricity systems,
2021.
[89] F. Zimmermann, D. Keles, State or Market: Investments in New Nuclear Power
Plants in France and Their Domestic and Cross-Border Effects, Technical Report,
Working Paper Series in Production and Energy, 2022.
[90] C. Fraunholz, F. Zimmermann, D. Keles, W. Fichtner, Price-based versus
load-smoothing pumped storage operation: Long-term impacts on generation
adequacy, in: 2017 14th International Conference on the European Energy
Market, EEM, IEEE, 2017, pp. 1–6.
[91] F. Zimmermann, E. Kraft, W. Fichtner, Modeling the dispatch of electrolyzers us-
ing agent-based electricity market simulation, in: 18th International Conference
on the European Energy Market, EEM, Institute of Electrical and Electronics
Engineers (IEEE), ISBN: 978-1-66540-896-7, 2022, pp. 1–10, http://dx.doi.org/
10.1109/EEM54602.2022.9921118, 37.12.01; LK 01.
[92] A. Ensslen, P. Ringler, L. Dörr, P. Jochem, F. Zimmermann, W. Fichtner,
Incentivizing smart charging: Modeling charging tariffs for electric vehicles
in German and French electricity markets, Energy Res. Soc. Sci. 42 (2018)
112–126.
[93] C. Fraunholz, D. Hladik, D. Keles, D. Möst, W. Fichtner, On the long-term
efficiency of market splitting in Germany, Energy Policy 149 (2021) 111833.
[94] F. Zimmermann, A. Bublitz, D. Keles, W. Fichtner, Cross-border effects of
capacity remuneration mechanisms: The Swiss case, Energy J. 42 (2) (2021).
[95] M. Genoese, F. Genoese, W. Fichtner, Model-based analysis of the impact of
capacity markets on electricity markets, in: 2012 9th International Conference
on the European Energy Market, IEEE, 2012, pp. 1–6.
[96] D. Keles, L. Renz, A. Bublitz, F. Zimmermann, M. Genoese, W. Ficht-
ner, H. Höfling, F. Sensfuß, J. Winkler, Zukunftsfähige Designoptionen
für den Deutschen Strommarkt: ein Vergleich des Energy-only-Marktes mit
Kapazitätsmärkten, vol. 10, KIT Scientific Publishing, 2016.
[97] E. Kraft, Analysis and Modelling of the French Capacity Mechanism, Springer,
2017.
[98] A. Bublitz, L. Renz, D. Keles, M. Genoese, W. Fichtner, An assessment of
the newly proposed strategic reserve in Germany, in: 2015 12th International
Conference on the European Energy Market, EEM, IEEE, 2015, pp. 1–5.
[99] A. Bublitz, D. Keles, W. Fichtner, An analysis of the decline of electricity spot
prices in Europe: Who is to blame? Energy Policy 107 (2017) 323–336.
[100] C. Fraunholz, D. Keles, W. Fichtner, On the role of electricity storage in capacity
remuneration mechanisms, Energy Policy 149 (2021) 112014.
[101] S. Misconel, R. Leisen, J. Mikurda, F. Zimmermann, C. Fraunholz, W. Ficht-
ner, D. Möst, C. Weber, Systematic comparison of high-resolution electricity
system modeling approaches focusing on investment, dispatch and generation
adequacy, Renew. Sustain. Energy Rev. 153 (2022) 111785.
[102] Simulating multiple occupant behaviors in buildings: An agent-based modeling
approach, Energy Build. (ISSN: 0378-7788) 69 (2014) 407–416, http://dx.doi.
org/10.1016/j.enbuild.2013.11.020.
[103] S. Phelps, Applying Dependency Injection to Agent-Based Modeling: The JABM
Toolkit, WP056-12, Tech. Rep., Centre for Computational Finance and Economic
Agents (CCFEA), 2012.
[104] V. Grimm, E. Revilla, U. Berger, F. Jeltsch, W.M. Mooij, S.F. Railsback, H.-H.
Thulke, J. Weiner, T. Wiegand, D.L. DeAngelis, Pattern-oriented modeling of
agent-based complex systems: lessons from ecology, Science 310 (5750) (2005)
987–991.
[105] G. Datseris, A.R. Vahdati, T.C. DuBois, Agents.jl: a performant and feature-full
agent-based modeling software of minimal code complexity, Simulation (2021)
00375497211068820.
[106] S. Tisue, U. Wilensky, Netlogo: A simple environment for modeling complexity,
in: International Conference on Complex Systems, vol. 21, Boston, MA, 2004,
pp. 16–21.
[107] D.J. Watts, S.H. Strogatz, Collective dynamics of ‘small-world’ networks, Nature
393 (6684) (1998) 440–442.
[108] L.E. Egner, Household energy retrofit behavior (HERB) ABM v1.0.0,
2008, https://www.comses.net/codebases/72d1d19f-1fd5-463f-8cf3-
ba13f26d4fa6/releases/1.0.0. [Online; Accessed 18 November 2022].
[109] M. Abdel-Aal, I. Haltas, L. Varga, Modelling the diffusion and operation of
anaerobic digestions in Great Britain under future scenarios within the scope
of water-energy-food nexus, J. Clean. Prod. 253 (2020) 119897.
[110] C. Ponsiglione, I. Quinto, G. Zollo, Regional innovation systems as complex
adaptive systems: The case of lagging European regions, Sustainability 10 (8)
(2018) 2862.
[111] C. Bordin, A. Tomasgard, SMACS MODEL, a stochastic multihorizon approach
for charging sites management, operations, design, and expansion under limited
capacity conditions, J. Energy Storage 26 (2019) 100824.
[112] C.D. Korkas, S. Baldi, E.B. Kosmatopoulos, Grid-connected microgrids: Demand
management via distributed control and human-in-the-loop optimization, in:
Advances in Renewable Energies and Power Technologies, Elsevier, 2018, pp.
315–344.
[113] L. Dias, S. Simões, J. Gouveia, J. Seixas, City energy modelling-optimising local
low carbon transitions with household budget constraints, Energy Strategy Rev.
26 (2019) 100387.
[114] J. Xu, K. Li, M. Abusara, Preference based multi-objective reinforcement
learning for multi-microgrid system optimization problem in smart grid, Mem.
Comput. 14 (2) (2022) 225–235.
[115] A. Bublitz, Capacity remuneration mechanisms for electricity markets in
transition, 2019.
[116] M. Deissenroth, M. Klein, K. Nienhaus, M. Reeg, Assessing the plurality of actors
and policy interactions: agent-based modelling of renewable energy market
integration, Complexity 2017 (2017).
[117] E.J. Chappin, L.J. de Vries, J.C. Richstein, P. Bhagwat, K. Iychettira, S. Khan,
Simulating climate and energy policy with agent-based modelling: The energy
modelling laboratory (EMLab), Environ. Model. Softw. 96 (2017) 421–431.
[118] Z. Zhou, W.K.V. Chan, J.H. Chow, Agent-based simulation of electricity markets:
a survey of tools, Artif. Intell. Rev. 28 (4) (2007) 305–342.
[119] F. Sensfuß, M. Ragwitz, M. Genoese, D. Möst, Agent-based simulation of
electricity markets. A literature review, 2007.
[120] P. Shinde, M. Amelin, Agent-based models in electricity markets: A literature
review, in: 2019 IEEE Innovative Smart Grid Technologies - Asia, ISGT Asia,
2019, pp. 3026–3031, http://dx.doi.org/10.1109/ISGT-Asia.2019.8880889.
[121] P. Hansen, X. Liu, G.M. Morrison, Agent-based modeling and socio-technical
energy transitions: A systematic literature review, Energy Res. Soc. Sci. 49
(2019) 41–52.
[122] D.L. DeAngelis, S.G. Diaz, Decision-making in agent-based modeling: A current
review and future prospectus, Front. Ecol. Evol. 6 (2019) 237.
Energy Strategy Reviews 57 (2025) 101613
19
