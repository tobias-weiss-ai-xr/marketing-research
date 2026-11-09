---
title: 'Carthago Delenda Est: Co-opetitive Indirect Information Diffusion Model for Influence Operations
  on Online Social Media'
url: https://arxiv.org/abs/2402.01905
category: social-media
subcategory: empirical
date: 2024-02
venue: ''
authors:
- Jwen Fai Low
- Benjamin C. M. Fung
- Farkhund Iqbal
- Claude Fachkha
source: arxiv
pdf_url: https://arxiv.org/pdf/2402.01905
pages: 60
chars: 288349
fetched_at: '2026-11-08T13:08:46+00:00'
kb_version: 1
---

# Carthago Delenda Est: Co-opetitive Indirect Information Diffusion Model for Influence Operations on Online Social Media

Carthago Delenda Est: Co-opetitive Indirect Information Diffusion
Model for Influence Operations on Online Social Media
Jwen Fai Low, Benjamin C. M. Fung, Farkhund Iqbal, and Claude Fachkha
Abstract
For a state or non-state actor whose credibility is bankrupt, relying on bots to conduct non-attributable,
non-accountable, and seemingly-grassroots-but-decentralized-in-actuality influence/information opera-
tions (info ops) on social media can help circumvent the issue of trust deficit while advancing its interests.
Planning and/or defending against decentralized info ops can be aided by computational simulations
in lieu of ethically-fraught live experiments on social media. In this study, we introduce Diluvsion, an
agent-based model for contested information propagation efforts on Twitter-like social media. The model
emphasizes a user’s belief in an opinion (stance) being impacted by the perception of potentially illusory
popular support from constant incoming floods of indirect information, floods that can be cooperatively
engineered in an uncoordinated manner by bots as they compete to spread their stances. Our model,
which has been validated against real-world data, is an advancement over previous models because we
account for engagement metrics in influencing stance adoption, non-social tie spreading of information,
neutrality as a stance that can be spread, and themes that are analogous to media’s framing effect and are
symbiotic with respect to stance propagation. The strengths of the Diluvsion model are demonstrated
in simulations of orthodox info ops, e.g., maximizing adoption of one stance; creating echo chambers; in-
ducing polarization; and unorthodox info ops, e.g., simultaneous support of multiple stances as a Trojan
horse tactic for the dissemination of a theme.
Keywords— agent-based modeling, information diffusion, information propagation, information operations, in-
fluence operations, psychological operations, rumor spreading, rumor management, social cybersecurity, persuasive
computing
1 Introduction
Artificial intelligence (AI), alternatively known as machine learning, has advanced on all fronts — behavioral, textual,
audio, visual, and video — to the point where comprehensive and convincing digital personas can be crafted from
mere lines of code (Section 2.2.5). As a result, the detection of information operations (defined in Section 2.2.1)
as a method for combating the spread of undesirable narratives by adversarial agents on online social networks,
while still important, becomes increasingly non-viable as the predominant means of achieving information security.
A 2021 review of research papers on countering influence operations that went as far back as 1972 noted that all
223 studies they found were on user-focused countermeasures (users being consumers of disinformation) [1]. The
authors concluded that “[b]eyond fact-checking, the research base is very thin”, and called for increased focus on key
areas such as “studying countermeasures that target the creators of disinformation content in addition to studying
consumer-facing policies”. In response to this call for action, we propose complementing existing detect-and-correct
methods that conduct struggles against undesirable information on a tactical, low-level per-message or per-user basis
with a method that facilitates waging war against disinformation from a high-level strategical perspective, where
users and messages are seen as a part of a synergistic whole meant to achieve a combined arms outcome.
To that end, we designed Diluvsion, an agent-based model for simulating how information operations can perturb
opinion evolution in an online social media platform. The model relies on parameters derived from publicly available
data on a social media platform to forecast the outcomes of info ops on similar platforms. As such, it can serve as a
tool to be used by planners in crafting campaigns to attack disinformation or defend against it without needing to
first test the interventions in the real world — tests that can have unsavory ethical and even geopolitical implications
[2, 3]. Like many other information diffusion models, Diluvsion is inspired by epidemiology but updated to consider
new insights on transmission dynamics from the COVID-19 pandemic (Section 2.1.2). But, unlike many models,
Diluvsion is developed with info ops and bots in mind, meaning that unconventional routes for expanding influence
are accounted for and that optimistic assumptions for information diffusion in other arguably marginally more benign
1
arXiv:2402.01905v2  [cs.SI]  6 Feb 2024

contexts are discarded, for example, the ability to select seed nodes to maximize propagation in product advertising
[4, 5].
While models are often designed to adhere closely to the real world, no model is meant to be a perfect recreation of
the real world; design choices reflect aspects that the modelers wish to emphasize. In our case, Diluvsion brings into
prominence the role played by indirect information, namely social cues [6] — engagement metrics and the perception
of mass adoption — in opinion propagation. Repetition is the key to the operation of our model. Much like Cato’s
brilliant tactic of incessantly playing up Carthage’s threat to Rome [7] and calling for Carthage’s destruction in the
Roman Senate led to the genocide [7] of Carthage, much like repeating a lie can let it take on the mantle of truth [8, 9],
so does the persistent saturation of an opinion in the media landscape can drive its adoption among the populace
[10, 11, 12, 13, 14, 15, 16].
The contributions of this paper are:
• An agent-based co-opetitive information diffusion model for information operations on social media that is
novel in its incorporation of concepts not considered by existing models: an infectious neutral stance; themes
that must piggyback on stances to infect users and have an enhancing or diminishing effect on the stance’s
infectivity; non-social tie-based transmission of information; parity in the treatment of bots backing different
stances; perception of mass support inferred through engagement metrics such as the number of retweets
influencing stance adoption; and agents with heterogeneous roles and activity levels populating the simulation.
• In-depth rationale behind the design/modeling choices, demonstrating the empirical evidence that our model
is predicated upon and consequently the real-world applicability of our model.
• Initial “validation” of the model by drawing simulation and graph structure generation parameter values from
distributions found in real-world data and further validation that succeeded in reproducing via simulations the
distributions from a different empirical dataset.
• Simulations that are in part ablation studies and in part experimentation with info ops tactics. The maneuvers
examined include bot-backed minority stances facing off against a non-bot-backed majority stance, polariza-
tion/depolarization, and maximizing theme diffusion. The emergent outcomes from implicit cooperation and
competition found in these simulations are examined and discussed in the context of their implications for
decentralized info ops.
2 Background
As our work occurs at the intersection of different domains, we split our discussion of relevant works into two major
sections: information diffusion and influence maximization (Section 2.1), and information operations (Section 2.2).
2.1 Information diffusion models
The study of information diffusion — the process by which information spreads from one entity to another — has a
long history. In the particular case of diffusion on online social networks, the history is sufficiently extensive to allow
for a survey [17] of existing work to be published in 2013. The closely related domains of influence maximization and
consensus formation have similarly rich histories, which can be seen in a 2021 survey [18]. Influence maximization
(IM) studies the problem of locating influential nodes that maximize the spread of information to the entire network.
Consensus formation is concerned with determining the manner in which a group of agents can all arrive at the same
opinion. For an in-depth discussion of these topics, we refer the readers to the aforementioned surveys. Here, we
restrict ourselves to discussing the most prominent and relevant models and the elements from those models that
influenced the development of our model, Diluvsion. The information presented is also meant to help situate Diluvsion
among the constellation of predecessor models.
2.1.1 Information
In the space of diffusion/propagation models, information goes by many different names, including information [19],
influence [18], rumor [20], opinion [21], memes [22], and news [23], depending on the context. While we will use these
terms interchangeably throughout this paper, we favor the term “opinion” due to the fact that the major component
of the information being spread in networks within our model, the stance, is polarized and homophilic. Together with
non-polarizable themes, they form a unit of information in our model (Section 3.1). That is not to say that other
forms of information are not present in the model. Engagement metrics, for instance, are exposed to agents and can
influence their decision to adopt a piece of information.
We are aware of works that have studied how real news and fake news spread differently on social media [24, 25].
The information of interest in this paper, i.e., the information being disseminated, is not generally regarded as “fact”
2

(e.g., quantum mechanics and general relativity applied within their respective restricted contexts and not outside)
but “opinion” (e.g., the dispute over the rarity of scale-free networks in the real-world [26]), which does not have
a clear delineation between true and false. In our model, “disinformation” is simply a term of convenience for
undesirable information; messages are indistinguishable in terms of veracity, so veracity cannot influence a message’s
spread. Only stances and themes have influence.
2.1.2 Uncontested information diffusion
Based on the typology introduced in [17], information diffusion models can be separated into two categories: explana-
tory and predictive. Explanatory models aim to “infer the underlying spreading cascade, given a complete activation
sequence.” Diluvsion belongs to the other category, predictive models, that aim to predict “how a specific diffusion
process would unfold in a given network, from temporal and/or spatial points of view by learning from past diffusion
traces.” Predictive models are further divided into graph- and non-graph-based approaches. Graph-based approaches
assume that information spreads along the edges in the graph. Non-graph-based approaches ignore network topology
and model information diffusion as a process represented by a system of differential equations, in emulation of similar
equations in epidemiology [27, 28].
The two most well-known graph-based models are the independent cascade (IC) [29] and linear threshold (LT) [30]
models, and they serve as the base models for most influence maximization research. IC models diffusion as a chain
reaction in which a node that has adopted a piece of information, designated as being activated, attempts to activate
inactive neighboring nodes in the graph with a certain probability. There are no retries and an activated node remains
activated forever. In LT, an inactive node becomes activated if the sum of influence from activated neighboring nodes
exceeds the node’s threshold. Influence takes the form of weighted directed edges between nodes and the threshold
is generally drawn from a uniform random distribution. An activated node remains forever activated in LT as well.
IC can be seen as sender-centric in contrast to the receiver-centric LT.
In non-graph-based models, the model names usually take after the sequence of state transitions permissible
within the model, where the states are susceptible (S), infected (I), and recovered (R), which are based on the earliest
epidemiological model, SIR [27]. The first explicit link between information and disease was established by Daley and
Kendall, who were inspired by the SIR model to create the Daley–Kendall (DK) model for rumor propagation [31].
Notable variants of DK include the Maki–Thompson model [32]. Rumor diffusion models have states such as ignorant
(I, susceptible), spreader (S, infected), and stifler (S/R, recovered) that mirror their epidemiological counterparts,
although these specific terms were not used in the initial work by Daley and Kendall. Later reviews [33, 34] showed
the cross-pollination of ideas between rumor-specific and biological epidemiological models. Subsequent studies on
epidemiological diffusion models also innovated upon the transition sequence, e.g., SIRS [35] or added additional
states, e.g., SIHR [36] rumor spreading model where H stands for hibernator and SHIR [19] model for competitive
information diffusion on online social media where H stands for hesitated. DK descendants innovated in a similar
fashion, e.g., ISCR [37] which added a counter-spreader (C) state.
In Diluvsion, network topology matters, as in IC and LT, and information generally travels based on the agents’
connections. The influence of epidemiological models, SIR, SIS, etc., are in inclusion of non-graph edge routes
(circumventing topology) for information diffusion to our model, as well as in the agents’ non-durable immunity
(SIS). However, agents are never in an uninfected state within our model, as they only ever transition between the
three mutually exclusive infected states (stances), negative, neutral, and positive, with infection by non-exclusive
themes providing an additional differentiating mechanism akin to viral variants (Section 3.1).
The SARS-CoV-2 pandemic has revealed the shortcomings of some graph-based models. In information diffusion,
the common assumption is that a link/edge exists between two people only if they have social ties (e.g., friends,
family, followers, and colleagues). However, in epidemiology, such an assumption is not always made because ties can
be formed with complete strangers in many situations. A passerby breathing, coughing, or sneezing in a crowded cafe
spreads aerosolizable infectious disease almost as effectively as staying under the same roof with a diseased family
member [38]. On social media, many posts are publicly viewable and lively discussions can occur in the replies section
of those posts, analagous to a forum or a cafe, and a user may be exposed to the opinions of strangers, i.e., people
who are neither followers nor followees, who replied to the post of the user’s followee (this idea will be explored in
Section 3.3.2). Another issue is the strong assumption inherent in designating the recovered/stifler state as an agent’s
end state in an information epidemic. SARS-CoV-2 immunity is transient. It is not permanent. Reinfection by the
same or different variants is a real possibility [39]. Non-permanent resistance to contagions that increases or decreases
depending on the infection type is a mechanic implemented in Diluvsion to offer an alternative perspective to the
strong assumptions of permanent immunity in the existing literature (Section 3.4).
3

2.1.3 Competitive information diffusion
Classical information diffusion does not account for information possessing polarity and existing in a contested
space. “Vaccines are safe” and “vaccines are dangerous” are contradictory opinions which a single entity is unlikely
to hold simultaneously. There are actors, such as healthcare authorities, with a vested interest in not just rapidly
disseminating the opinion that vaccines are safe and having people adopt that opinion but also stemming the adoption
of the opposing opinion and having the opposing opinion be dislodged from those who have adopted it. Competitive
information diffusion models, also known as opinion formation models, were developed to simulate such scenarios.
In biology, competition can be thought of as cross-immunity contagions [40], where developing immunity for one
decreases the likelihood of being infected by the other.
Two broad categories of competition exist based on the type of information being diffused: continuous or discrete.
Certain consensus formation mechanisms (e.g., taking the mean or median) are not possible for an information type
(e.g., selecting a material for constructing an object, although the problem can be reformulated such that selection is
based on continuous-valued attributes such as tensile strength). Elements of continuous and discrete models can be
made to work together, as demonstrated by the Biased Voter model [41] that combines DeGroot and voter models.
For continuous-valued information, the DeGroot/French–DeGroot [42, 43] model is widely used for competitive
diffusion. In the model, every incoming edge for a node/agent has a weight denoting another agent’s influence (a
weight of zero is equivalent to not having an edge). There is also a weighted self-loop for the extent to which an
agent values its own opinion. At every time-step, an agent updates its opinion by taking the weighted average
of all neighboring opinions, including its own. This process is repeated until the values (opinions) are stable. In
a strongly connected graph, perfect consensus (all agents share the same opinion) is guaranteed. The Bounded
Confidence model, alternatively known as the Hegselmann–Krause model [44], also updates an agent’s opinion by
averaging others’ opinions, except that instead of the opinions of all neighbors, the opinions are those who share
similar opinions, with similarity being bounded by some arbitrary value, hence the model’s name. Clustering (a form
of polarization), instead of perfect consensus, is the likely outcome of the Bounded Confidence model. A review of
continuous-valued models, which includes DeGroot, Weighted-Median, Bounded Confidence, and Quantum Game,
can be found in [45].
For discrete opinions, one popular model is the voter model, independently developed by Clifford and Sudbury
[46] and by Holley and Liggett [47]. At every step, the model first chooses an agent and its neighbor, both at random.
The agent then adopts the opinion of its neighbor. Another popular model is the social influence model by political
scientist Axelrod, designed to explain how global polarization arises due to local homophily. In this model, each
agent is defined by its cultural traits, which is a fixed-length string of discrete numbers. Similar to the voter model,
the Axelrod model randomly chooses an agent and its neighbor at every step. Then, with a probability equal to their
cultural similarity, the agent will update one of its traits that differs from its neighbor’s. The Axelrod model can be
considered an extension of the voter model.
One natural extension to voter models is to have an agent’s opinion updates be guided by the majority instead
of just any random neighbor. The majority rule model by Chen and Redner selects at random a flippable spin
(a changeable binary opinion) and have the spin adopt the majority state of its interaction neighborhood [49]. Fu
and Wang incorporated minority avoidance into the majority rule model by having agents occasionally sever ties
with those holding a minority opinion [50]. Other information diffusion models studied a different form of minority
avoidance [51, 52], specifically the “spiral of silence” [53], which theorizes that people are reluctant to disagree with the
majority, hence restricting themselves from expressing a non-conforming opinion, ultimately leading to the continued
domination of the majority voice. The majority voice can be illusory, created by a vocal minority.
There are many ways in which competition can be modeled using epidemiological models. For two competing
information contagions, a winner-takes-all situation emerges, where the stronger contagion dominates completely
instead of just gaining a majority across all graph types, given the conditions of no permanent immunity (SIS-like,
where S is susceptible and I is infected), mutually exclusive infections, and nodes that are homogeneous in their
resistance towards both contagions [54]. Non-graph-based epidemiological models can also account for competition.
Two of the proposed epidemiological models in [37] accounted for the presence of competing discrete information
differently: the ISCR model features an additional class of user, counter-spreaders (C), in addition to the classical
ignorant (I), spreader (S), and recovered (R), while the ISSRR model divides the spreader and recovered classes based
on the which side of the bipolar information they were infected by or recovered from.
Extensions to IC and LC (Section 2.1.2), which are discrete models, allow them to model competitive influence
maximization. The simplest modification is to start the diffusion of two different pieces of information from two
different origin/seed nodes. The different IC and LT derivatives distinguish themselves based on the restrictions or
conditions that the competing factions are subject to: selecting the most influential starting nodes for one faction
given that the competing faction’s starting nodes are known under IC [55]; best response and first mover strategies
under IC [56]; proving that being the first mover is not always an advantage under a special case of IC [20]; different
forms of competitive diffusion under LT, e.g., different tie-breaking rules [57]; and two competing cascades on a signed
4

network under the IC model [58].
The limitations and unrealistic assumptions of IC and LT have been recognized, with [59] highlighting three
misspecifications of classical IC and LT: not modeling assortativity of influence, ignoring non-uniformity of the joint
distribution of influence and susceptibility (due to peer effects, homophily, and social influence), and heterogeneity in
influence and susceptibility. However, [59] has misspecifications of its own. In the problem of IM, [59] defaults to seed
selection: a faction (representing a stance) has the opportunity to pick and choose seed nodes from which to begin its
diffusion. However, this seed selection assumption that non-competitive and competitive IM operate under is alien
to info ops (Section 2.2). Influencers on social media can be paid to promote a stance, but not all can be bought off.
Info ops are also often conducted in a decentralized manner to make them resilient against the decapitation strike
tactic of silencing/compromising influential nodes (Section 2.2.4), so info ops planners are unlikely to even consider
the problem of seed selection.
Traces of LT’s threshold mechanism combined with DeGroot’s weighted influence (despite our model being de-
signed for discrete instead of continuous opinion), and the voter/majority rule model are present in our model,
grounding it in the extant competitive diffusion literature. A threshold (resistance) must be crossed for opinion
adoption/infection events. Unlike classical majority rule models, in which an agent’s adoption of the majority opin-
ion is deterministic (the neighborhood’s majority opinion will definitely be adopted), ours is probabilistic, with each
opinion weighted by perceived popularity, as measured through the proxies of engagement metrics. While agents do
not have weighted self-loops as in DeGroot, they are influenced by how others judge the opinions that they express
(Section 3.3.2). The mechanics make it so that human agents in Diluvsion are more inclined to convert to a stance
that is perceived to be held by the majority in the quasi-global neighborhood (Section 3.3.2). Adopting an unpopular
opinion is possible, though unlikely. An agent’s discrimination against minority opinions is therefore encoded in the
probability distribution. This form of minority avoidance in our model, Diluvsion, despite sharing conceptual roots
with those encountered in the literature, is considerably different its technical implementation.
The design of our mechanics for themes can be considered a special restricted case of Axelrod’s cultural traits.
The example of traits given in Axelrod’s original paper allows for 10 5 possible states since there are five positions
filled with numbers ranging from zero to nine. The number of positions in Diluvsion is variable, from one to an
arbitrary maximum, and a theme can fill a position only once. If the maximum was five and there were 12 themes,P5
k=1
12!
k!(12−k)! = 1585. Peer effects, homophily, and social influence all affect an agent’s decisions in Diluvsion,
heightening realism (see Section 3.3.2). One manifestation of homophily is in opinions sharing similar stance and
themes as the agent itself possessing greater weights during an infection event, and this homophily is comparable to
Axelrod’s and Hegselmann-Krause’s homophily, though less extreme.
2.1.4 Cooperative and competitive information diffusion
Cooperation can also be an outcome of the interactions between multiple information contagions present in a system
[40]. Immunological dysfunctions caused by the infections of viruses such as HIV [60], Ebola virus [61], and SARS-
CoV-2 [62] that make the infected more susceptible to other viruses are examples of cooperative biological contagions.
Relative to competitive diffusion, the many forms of cooperative information diffusion have been less frequently
studied.
Cooperation can occur at the information/contagion level. The diffusion model in [63] learns from empirical data
the affinity between different contagions (URLs), finding that news stories of the same event boost the adoption of
each other’s URLs, implying cooperation. The spread of a highly infectious news story’s URL suppresses the spread of
URLs from other unrelated, less infectious news stories, implying competition. Different models [64, 65] have recreated
the synergistic (e.g., complimentary products such as iPhone and Apple Watch) and antagonistic relationships between
contagions propagating in heterogeneous and homogeneous multilayer networks where simultaneous infection by
multiple contagions (coinfection) is possible.
Cooperation can occur at the agent level. The implicit form of such cooperation is common in the study of
multi-agent systems in the context of robotics (vehicular information diffusion and consensus formation [66, 67],
drone swarms [68, 69], and search-and-rescue robots [70]). Ideas found in (not necessarily originating in) robotics can
be adapted to information diffusion, e.g., swarm intelligence algorithms for influence maximization under IC and LT
models [71, 72].
Finally, the cooperative effect can be found in the links/edges connecting nodes in a network; a node u being
infected by a contagion through another node v makes u more susceptible to future infection by a different contagion
via v [73], reminiscent of the effects of trust and affection in social relations.
The implicit cooperation for Diluvsion happens at the agent-level, where all bots targeting the most vulnerable
for stance propagation 3.5) and when bots’ independent actions unknowingly contribute towards a common objective
(Section 6.2). At the information level, stances and themes induce homophilic conversions, and engagement metrics
induce bandwagoning (Sections 3.1 and 3.3.2).
5

2.1.5 Agent-based models
Agent-based models (ABMs) aim to infer macro-level outcomes from micro-level interactions and can be viewed
as a further reduction of abstraction compared to models based on interconnected homogeneous nodes and models
constructed only from differential equations. Nothing stipulates that agent-based models have to incorporate a
network topology in modeling diffusion (e.g., agents can be placed on a grid and the diffusion can be governed
by spatial proximity), but in practice, agent-based models of information diffusion on social media invariably use
network topology, as networks are an effective approximation of social organization in human communities, online
and offline. Being freed from the constraints of stringently adhering to the precepts of classical IC and LT, and their
many extensions, enables more customized and accurate models to be built based on empirical data in sociological
and psychological studies, albeit costlier to run computationally. An example is the ABM for the highly specific
context of online anti-vaccination movements [74] which contained three different agent types: doctors (similar but
not equivalent to external authority/mass media in other models), patients (humans), and initiators (stubborns/bots).
A comprehensive review of the various design aspects of modeling information diffusion in social networks as multi-
agent systems (MAS) can be found in [75]. This review focuses on the trade-off between the simplistic assumptions
found in classical MAS and the complexity of real-world social networks. Thinking in terms of complexity versus
abstraction can help establish boundaries between classical and agent-based models of diffusion. This demarcation
is used by some ABMs, e.g., [52]. Thus, while agency is arguably present in some models discussed earlier due to
individualization/heterogeneity of nodes, e.g., DeGroot [42, 43], those models never fully embraced the possibilities of
agency and the resulting emergent behavior (e.g., John Conway’s Game of Life) in the interest of keeping the models
analytically tractable, which is why we do not discuss them in this section.
Diluvsion is an agent-based model. It borrows many concepts from existing models that are relevant to accurately
simulating the impact of info ops on information diffusion on social media.
One borrowed concept is that agents have a set amount of energy, with every action depleting their energy
reserves. In [76], agents have a fixed energy level and interactions do not cost energy; however, after some arbitrary
point in time, every interaction decreases the agent’s energy level. This setup enables the study of the correlation
between agent energy and rumor propagation intensity. In [77], the simulations were populated by different classes of
agents, each class with its own range for how frequently its members tweet and retweet. Our implementation of the
energy level is based on empirical data from Twitter that separated users into three tiers (Sections 3.4 and 3.8.1).
Our agents’ actions are additionally restricted by a diurnal cycle (Section 3.6).
Agents are also commonly constrained by having a memory and attention (also uncommonly, and perhaps con-
fusingly, called vigor [78]) limit placed upon them, e.g., [22, 78, 79, 80, 81], reflecting the non-omniscient nature of
humans. We discuss this mechanic in greater detail in Section 3.2.
Linked to the concept of memory is the concept of repetition driving information adoption. In the agent-based
SIR rumor diffusion model introduced in [82], agents can receive the same information multiple times, with agents
likelier to adopt information that has been seen more frequently, contributing to the spread of the information as
agents eventually share the information that they have adopted. In the information entropy-based rumor spreading
model in [79], a rumor’s information salience is measured by the frequency of the rumor’s occurrence in the agent’s
memory, with greater frequency linked to higher salience. The most salient rumor is selected for transmission during
the spreading phase of the model, and this selection mechanism constitutes the conformity effect put into practice
[79]. In an ABM for studying astroturfing by bots under the spiral of silence framework, conformity takes the form
of an opinion climate, which is composed of the opinions expressed by neighboring agents with silent agents excluded
[52]. Another model [80] of conformity by has an agent slowly revising its opinion to become more similar to its
neighbors’. Yet another model, AMID, features users who are likely to adopt opinions supported by the majority
of adjacent neighbors in [78]. Additionally, under AMID, trust between agents was modeled as the frequency with
which a truster shares the trustee’s messages, with users likelier to adopt messages from trusted sources [78].
Repetition’s influence similarly suffuses every part ofDiluvsion. A stance that occurs more frequently in an agent’s
memory has a greater chance of being adopted. But, we introduced additional complications into the mechanism.
Conformity effects are extended to account for the engagement metrics prominently displayed alongside every message
on social media, which serve as cues on how others perceive the credibility of the message (Section 3.3.2). Conformity
effects are also balanced against homophily for stances and themes, which is based on the real-world tendency for
people to prefer opinions that are similar to their own.
A divide exists among ABMs on the matter of opinions being exclusionary or capable of co-existing with oth-
ers. Exclusionary opinions, as conceptualized in [83], permit a user to only adopt one discrete opinion at any one
time. Models in which opinions are modeled as a point along a continuous spectrum, as is common in counter-
disinformation ABMs, e.g., [81, 82, 84], naturally feature exclusionary opinions as opinions cannot simultaneously
occupy two positions along the spectrum. Studies using the spiral of silence framework, e.g., [51, 52], require polar-
ized/exclusionary opinions by design; users would not be hesitant to voice opinions that ran counter to the perceived
majority opinion climate if an oppositional relationship did not exist. For non-exclusionary opinions, there is also a
6

myriad of conceptualizations. In SMSim, developed for studying non-polarized information diffusion [85], bit vectors
denote a message’s association with the set of possible topics in the simulation. For the rumor spreading model
introduced in [79], infection by an opinion means that the opinion goes into the agent’s memory bank. There is no
incompatibility mechanism that forces a stored opinion to be ejected from memory; removal is only due to insufficient
space in the bank. And with some models, the distinction between exclusionary and non-exclusionary is less clear,
e.g., [63] where agents can only adopt one contagion but the agent’s infection history continues to influence future
contagion adoption. In the AMID model [78], each message is associated with all possible topics in the simulation
with varying strengths (fuzzy sets) and there is an additional binary number for each topic denoting the message’s
positive or negative opinion towards the topic, a formulation reminiscent of Diluvsion’s stance and themes (Section
3.1). Users in AMID are capable of caring about multiple topics simultaneously, but the opinion (polarity) for each
topic is an exclusionary binary value.
On the matter of co-existing opinions,Diluvsion straddles the middle as there are exclusionary and non-exclusionary
components of an opinion within Diluvsion, corresponding to polarized stances and non-polarizable themes respec-
tively (Section 3.1).
A common feature of ABMs is the segregation of the agents into distinct classes. This practice is intuitive in
studies investigating the impact of bots on social media, e.g., [52, 77, 81, 84], as bots have to behave differently than
the rest of the users to distinguish themselves and for their influence to be measurable. In [77], both humans and
bots were further subdivided into additional categories, e.g., amplifier and commentator, based on extant research
on social media user behavior. Some works [81, 84] divided agents based on stance, with “truth” propagandists,
neutral/uninformed people, and “disinformation” peddlers exhibiting different behavioral patterns; bots are associated
solely with the undesirable stance, disinformation. While most models keep an agent’s role static throughout the
simulation, some allow agents to radically alter their behavior upon meeting certain conditions, e.g., radicalization
turning passive users into active disseminators [74, 84].
Under Diluvsion, three main attributes define an agent: its activity level, its action-role, and whether the agent is
a human or a bot. There are three activity levels, five action-roles (15 unique action distributions as the distributions
for the same role differ based on activity level), and a binary bot/human membership. As such, a total of 30 possible
classes of users exist in Diluvsion. Agents do not change roles. Our conception of bots (Section 3.5) hews closer to
[52, 77] in that their behavior is stance-agnostic for the reasons specified in Section 2.2.5, even though [52, 77] also
only associate bots with malicious behavior.
Models found in the literature that most closely resemble our Diluvsion are those developed for a purpose similar
to ours: the ones by Beskow and Carley and Averza et al. which dealt with information operations involving bots
shaping discourse on online social media platforms [81, 84]. Unlike [52] which also studied the impact of bots on online
discourse, [81, 84] did not integrate the spiral of silence into their models. And unlike [77] which was interested in the
descriptive statistics (e.g., tweets and retweets per day) that a mixed population of bots and humans would generate,
[81, 84] are concerned with competitive diffusion of three stances, just like our study. Although to be accurate, our
model allows all three stances to be propagated, but in [81, 84], only the two stances that are antithetical to each
other can be propagated while the neutral stance is a static default state. The crucial differences between our work
and [81, 84] are the stance-agnosticism of our bots (Section 3.5), neutrality being an infectious stance in our model, as
previously mentioned (Section 3.1), the inclusion of indirect influence mechanics (engagement metrics and non-edge
information transmission, Section 3.3.2), and heterogeneous activity levels and roles for agents (Section 3.8.1).
2.2 Information operations
2.2.1 T erminology
Within the existing literature, information operations (info ops), influence operations, and psychological operations
have been used interchangeably to describe “activities that target information bases of an adversary, protect one’s own
information assets and make efficient use of one’s own information”[86] even though each term has a specific meaning,
e.g., psychological operations are originally defined as falling under the umbrella of info ops [87]. In this paper, we
adhere to the loose usage of these terms as other researchers have, e.g., authors of [1, 88] switching between the terms
within the same document; Cambridge Analytica varyingly described as engaging in psychological operations [89],
information operations, [90], and influence operations [91].
Although info ops is “a military defined concept and doctrine” originating from the post-Cold War US and
NATO military establishments, it “interacts largely with society as the majority of the targets either attacked or to
be defended by Information Operations means are not military but civil targets” [86]. As pervasive computing has
become a reality in a world where interconnected mobile computing devices are increasingly commonplace among
civilians, there has never been a richer, more fertile ground for info ops [92], especially when the rise of social media
normalizes rapid information sharing.
7

2.2.2 Social media
Social media has always been a tool for information warfare. As early as 2003 [93] / 2006 [94], the cyberdissident
diplomacy (CDD) initiative from the US State Department reached out to “tech-savvy youth in the sixteen-to-thirty-
five age range with the aim of training them in particular forms of cyberdissidence and online campaigning”, leading
“young Muslims” to “serve as the proxies to the US” in a “war of ideas”, an “ideological war”— influence operations,
in other words — “to maintain its global hegemony” [93, 95]. As the provocative title of one journal paper neatly
summarized, “Facebook to Mobilize, Twitter to Coordinate Protests, and YouTube to Tell the World”: New Media,
Cyberactivism, and the Arab Spring [96]. In the 2009 protests in Iran, Twitter was deemed so crucial to the protesters
that the US State Department intervened in Twitter’s scheduled server upgrade to ensure that Iranian users did not
suffer from service interruption [97]. In Russia where the user base of native social media platforms VKontakte
and Odnoklassniki dwarfs that of the US-developed Facebook, it is Facebook that mobilized anti-regime forces in
2011 [98]. The clearest example of social media as an instrument of war is the USAID-backed ZunZuneo, which is a
Twitter-like service designed to run solely in Cuba through mobile text messaging for the express purpose of covertly
inciting regime change, according to the reporting done by the US news agency Associated Press [99, 100].
But as the flames of social unrest fanned in faraway “jungle” [101] countries escaped their confines and started
engulfing First World/developed “garden” countries, the dangerous potential of social media was finally recognized
by the research community and alarms were raised. In a review of academic publications on countermeasures against
influence operations, the authors found a “dramatic increase in the number of studies since 2016” which is “[i]n line
with other research trends in the broader field of influence operations and disinformation” [1]; 2016 was the year
when Russia was accused of meddling in the US presidential election in favor of Trump via social media campaigns
[102]. Threats can be homegrown too: Amazon, Apple, and Google suspended the US social media platform Parler
for its role in the 2021 Capitol Hill riot [103]. The panic in the research community has culminated in the birth of
a new field, social cybersecurity, which seeks to “characterize, understand, and forecast cyber-mediated changes in
human behavior and in social, cultural, and political outcomes” as one of its objectives [104].
Diluvsion is a tool that seeks to aid in the fulfillment of the aforementioned objective by enabling the character-
ization of Twitter-like services and the forecast of info ops on such services.
2.2.3 Twitter-like platforms
Likely because of the ease of collecting data from Twitter, many researchers have focused on modeling information
diffusion on Twitter such as [22, 41, 81, 84, 105]. This is one reason the simulation environment within Diluvsion
models itself after Twitter. A greater motivating factor is the profusion of Twitter-like social media platforms. Truth
Social, Parler, and Gab cater to users chafing at the politically restrictive policies of Twitter [106]. Mastodon lets
users escape the whims of a single central authority by dispersing regulatory power among multiple central authorities
[107]. Twitter-like platforms have also emerged to serve different regions and languages, such as China’s Sina Weibo.
Even social media platforms that have never sought to emulate Twitter have analogs to certain features of Twitter
(which may not have originated from Twitter), e.g., Facebook’s share and share with a comment being similar to
Twitter’s retweet and quote-tweet, respectively.
The mushrooming of Twitter alternatives also speaks to a credibility crisis, where users no longer trust that they
can express their views free of suppression from a central authority. Decentralization is a natural antidote to this
credibility crisis. Our conceptualization of decentralization within Diluvsion does not take after Mastodon, since their
federated instances still allow moderation power to rest in the hands of the few [107]. We speak of a decentralization
where power is much more diffuse — or at least appears so (Section 2.2.4).
2.2.4 Decentralization and radicalization
The most effective way to shut down conversation is the top-down approach of restricting free speech, as the Ukrainian
experience of banning Russian social media VKontakte from 2017 onwards has shown [108]. Yet at the same time, the
vast majority of both pro-Ukraine and pro-Russia Ukrainians circumventing the ban to continue accessing VKontakte
[108] shows that the desire to escape overt, centralized censorship can transcend political affiliations. In liberal
democracies, harsh speech policing measures are not well-tolerated by users, even if private corporations instead of
governments are the ones doing the policing [109], as evinced by the many alternatives to Twitter (Section 2.2.3).
And if governments instead of corporations enforce censorship, the governments risk being viewed as draconian,
tyrannical, totalitarian, authoritarian, etc., by liberty-minded people. A 2019 attitudinal survey of US internet users
found that “among political attitudes, opposition to censorship (β = −.231, p < .001) had a significant negative effect
on support for government regulation of platforms” [110]. Hence the rise of a decentralized approach to information
warfare: shaping discourse with an invisible hand, unbeknownst to the public.
Decentralization has proven effective on offline social networks. Decentralization allows for radicalization without
attribution and accountability. Absent clear chains of command, membership simply involves claiming affiliation.
8

Members can appear to be acting autonomously, when collectively those actions advance the interests of the movement
[111]. Should the members’ actions harm the movement, “they can simply disavow the act without disavowing the
ideology” [112] in the same vein as black ops and black sites [113]. Without central authority, a movement can resist
collapse from decapitation strikes [96, 114, 115]. Ivan Marovic, a leader in the successful Serbian regime change
organization, Otpor, which is funded by NED; IRI; USAID; Freedom House; and British Westminster Foundation,
explained to National Public Radio’s Bob Garfield that “[l]eaders could have been blackmailed or bribed or even
maybe killed. You can’t do that with brands or ideas” [116]. This is similar to how a perpetual struggle can be waged
against an idea, e.g., the Global War on Terrorism. Terrorist themselves from white supremacists [117] to al-Qaeda
and Hamas [111] also favored decentralized structures for their resilience and “tactical security”.
Success in the offline world has led to attempts to replicate decentralized movements online. The US cyberdis-
sidence program is one such attempt at growing an online decentralized movement (Section 2.2.2). Another is
CENTCOM’s Operation Earnest Voice (OEV), which empowered “one US serviceman or woman to control up to 10
separate identities based all over the world” so they can create “false consensus in online conversations” [118, 119].
Graphika and Stanford Internet Observatory (SIO) reported in 2022 that their joint investigation with Twitter and
Meta uncovered hundreds of accounts engaging in covert pro-Western info ops over the course of five years [120].
An Israeli company, Team Jorge, specializing in info ops that ran multiple campaigns influencing elections around
the world [121, 122], created Advanced Impact Media Solutions (AIMS), a one-click system for creating “fake digital
persona[s] built to mimic human behavior and avoid detection” which operate “on social media sites, disseminating
rumors, harassment, defamation or praise — whatever the client asked for” [123, 124]. Other Israeli info ops com-
panies Archimedes and Percepto also employed fictitious digital personas [125, 126]. White supremacists [112] and
international Islamists [127, 128] took advantage of social media for recruitment [112, 127, 128], to transition to decen-
tralized structures [112, 127], and to conduct info ops of their own [87]. The “IT cells” manipulating Indian elections
adopted a functionally leaderless structure, where the bottom layer “creating and trending narratives” maintains
“enough distance from the top to give leaders plausible deniability if the digital foot soldiers become too extreme”
[115]. Another example is NAFO (North Atlantic Fellas Organization), which Politico described as consisting of
“internet culture warriors taking on Russian disinformation and raising funds for Ukraine” by adopting the same
tactics as “the Islamic State” and “the American far-right boogaloo movement” [129]. According to one freelance
disinformation researcher and self-proclaimed member [130, 131], NAFO is a leaderless movement [132]. The Wall
Street Journal describes NAFO as having “no command structure” [133].
Owing to the achievements and prevalence of decentralized info ops, the simulations we chose to show running in
Diluvsion (Section 5) were developed with decentralized info ops in mind, with affecting change through uncoordinated
coordination. The change agents being unaware of each other (Section 3.5) in Diluvsion is also a deliberate design
choice grounded in decentralization — leaderless terrorist/freedom fighter cells [134].
To affect change and appear organic at the same time, a decentralized movement needs a large number of warm
bodies. But growing a movement is time consuming. Furthermore, each additional truly independent (human) agents
within a movement is an additional security risk. Humans can turn into whistleblowers. Financial trails from hiring
propagandists risk being traced back to the mastermind.
CENTCOM’s OEV, Archimedes, Percepto, and Team Jorge’s AIMS already hinted at a solution: autonomous
artificial personas (Section 2.2.5).
2.2.5 Digital personas and bots
Based on all the markers accessible via cyberspace — i.e., excluding anything that requires physical interaction in the
real world — bots can be made virtually indistinguishable from live human operatives. This is all thanks to progress
in the field of machine learning making it easier than ever to deceive human senses and cognition [135]. On the
behavioral and textual front, services such as Character.AI allow users to create chatbots with distinct personalities,
such as Elon Musk or Marvel movie characters, and these chatbots are capable of carrying conversations for hours
with humans [136]. Chatbots can exert influence over humans; interacting with chatbots has a positive impact on
people’s attitude towards vaccines and also their intention to get vaccinated [137]. Bot-run Twitter accounts are
perceived as credible sources of information [138]. On the audio front, text-to-speech audio generation [139] has led
to convincing audio clips of Biden and Trump chatting over gaming sessions [140]. On the video front, there are
talking head video generation neural networks producing realistic depictions of people saying things that they have
never said, e.g., [141]. A variety of techniques exist for transposing one person’s face onto the body of another person
in a video, e.g., [142]. High resolution videos can be created with only text prompts, e.g., [143]. A navigable 3D
scene can be created through neural radiance fields using just a few static images, e.g., [144, 145]. On the image
front, text-to-image synthesis networks can hallucinate scenes that never existed in the real world purely by relying
on text descriptions, e.g., [146]. For realistic faces, one does not need to steal the identity of a human, as faces of
non-existent people can be generated [147].
To tie it all together, AIs given an initial goal from humans can plan to accomplish the goal by giving itself a
9

list of tasks and setting about accomplishing the tasks by itself using various tools (including itself and other AIs) at
its disposal [148], currently best exemplified by Auto-GPT. Pretending to be a human employed in a job will not be
too difficult, as AIs can produce codes that run [149] and also play at the role of a knowledgeable analyst since vast
swaths of programming and data science work can be automated via ChatGPT [150].
While we are not aware of any entity that has made digital personas using a combination of all these bleeding
edge AI capabilities 1, there is a high likelihood of such hypothetical human-like bots being created and deployed
in service of info ops at present or in the near future. Relying on detection as the sole strategy to safeguard
against them might be a dead-end. A collaborative report by the Stanford Internet Observatory, OpenAI, and
Georgetown University’s Center for Security and Emerging Technology concluded that it was reasonable to assume
that “attributing short pieces of [textual] content as AI-generated will remain impossible” [151]. The same report
warned that, based on their deliberately limited scope of “generative language models” producing “persuasive text”,
AI is “likely to significantly impact the future of influence operation” [151]. The days in which bots are simplistic
and easily detectable automatons, such as those found by BotHunter to be influencing Singaporean elections to little
apparent success [152] or found by Botometer (which already often mistakenly classifies humans as bots [153]), are
drawing to a close with advancements in AI.
The promise of AI-enabled bots lies not just in rapidly raising an info ops army as Team Jorge did with its 39,000
avatars [121, 122], but also in reducing the cost of info ops. “The potential of language models to rival human-written
content at low cost suggests that these models—like any powerful technology—may provide distinct advantages to
propagandists who choose to use them” [151]. Accessibility to content generation capabilities, which is correlated
with cost, has also been widened with the advent of AI. Image generation via diffusion models such as Dall-E-2,
Midjourney, and Stable Diffusion are available as services “for free or for a low price” [154] to practically everyone.
Consequently, social media platforms have been flooded by “hyper-realistic fake images deceiving many online” such
as those of Trump resisting arrest in March 2023 [155].
Bots can solve the problem of credibility crisis by appearing independent. This is not the same credibility crisis
we spoke of earlier where social media platforms were not trusted to be non-interventional (Section 2.2.3). This is
a credibility crisis among entities pushing the message — usually users of the platform and not the platform itself.
Messages from US-linked organizations are distrusted even for the seemingly benign (or even beneficial) cause of
counter-terrorism [127]. Attempts at laundering their reputation by using proxies such as “community groups, non-
governmental organisations and private enterprise” may be unsuccessful because simply being affiliated with the US
in any way taints the proxies’ reputations [127]. However, by conducting info ops through a collective of artificial
online personas who cannot be linked back to any state or non-state actor, the info ops would not be subjected to any
long-held animosity that the targeted population may have towards an actor, thus encountering less resistance. A
scholar examining the US’s credibility problem on social media in the issue of counter-terrorism similarly noted that
“producing the appearance of independence by hiding behind fictitious online identities is one option” to address the
credibility deficit [127].
Our conception of bots being nigh undetectable, as expounded in this section, plays a critical role in the design
of information propagation within Diluvsion. In Diluvsion, we assume that bots are bound by many of the same
limitations that a human agent would be, e.g., their activity level, as they would seek to blend in with the human
population. We also assume that people would not be able to ascertain another social media user’s true nature and
affiliations, hence why a person’s judgment on the credibility of a message/tweet relies on external social cues. And
this human heuristic of assessing credibility by following the herd makes social media users uniquely vulnerable to
decentralized info ops that can be trivially signal-boosted by bots, as we will discuss in Section 3.3.2.
However, at the same time, there exists in Diluvsion a special class of agents separate from humans that are
called “bots” (Section 3.5); within Diluvsion, “bots” is a term of convenience for all forms of propagandists. If a
human takes on the role of a propagandist (calculatingly penning tweets to maximize engagement, using Photoshop
or a physical airbrush to alter images, etc.) on social media, they are rightly classified as “bots” since they are
indistinguishable from purely algorithmic bots engaging in info ops.
The reason we reject the terms “propagandists” or “operatives” in favor of “bots” is because we reject the current
erroneous framing within the agent-based simulation community of segmenting agent types based on stance (defined
in Section 3.1) on an issue. In twitter sim [81], there are “three types of users: normal users (ignorants), bots/trolls
(spreaders), and truth defenders (stiflers).” In the model introduced in [84], there are “three types of agents: Deceptive
agents, representing bots or malicious human users; neutral agents, representing most Twitter users; and news agents,
official sources who share accurate, verified information.” A pattern emerges: bots are invariably associated only
with the “bad guys”, which is categorically false since NAFO, OEV, and the pro-Western covert info ops documented
1OEV predates the AI/neural network revolution. Graphika and SIO noted that assets in the pro-Western covert info ops
they uncovered “created fake personas with GAN-generated faces”[120], but no details were provided on whether other content
are AI-generated. AIMS bots do not rely fully on AI: profile pictures were “stolen from a genuine profile”, although the “creation
of [textual] content” is “driven by AI” [121, 123].
10

by Graphika and SIO are examples of bots working for “good” causes by disseminating “truth”. Under Diluvsion,
all propagandists are bots regardless of their stance.
Reclaiming the term “bots” is necessary to ensure accuracy in analysis and simulation, and thus avoid errors in
strategic judgment. Propaganda work and counter-propaganda work are often broadly equivalent in tactics. Persisting
in the delusion that the “good guys” behave in a radically different manner in matters of war is detrimental to the
formulation of good policy. Researchers will chase after the wrong solutions due to that initial error in judgment.
Recall the example of the failure of US counter-terrorism info ops on social media [127]. Foreign policy analysis
and reporting, e.g., [156, 157, 158, 159], will fixate on attributing the success of Islamist or ISIS propaganda over
US counter-propaganda to their speed, sophistication, creativity, having a better narrative, etc., and rarely question
whether the failure of counter-propaganda lies in the counter-propagandists’ lack of credibility, in the message listeners’
fear and loathing of the US. The State Department’s Digital Outreach Team (DOT) accusing ISIS of terror tactics
via social media accounts clearly affiliated with the US [127] appears oblivious to the fact that the use of terror tactics
by the US itself 2 undermines such a message. The initial error in judgment in assuming that the US’s hands are
clean ensured US counter-propaganda efforts’ continued failure [127].
2.2.6 State and non-state actors
Other notions that we need to disabuse ourselves of for the sake of strategic clarity is that info ops originating from the
“good guys” — democratic states — are only sanctioned against so-called non-democratic states and that meaningful
distinction exists between state and non-state actors. Democratic states attack each other and themselves. State and
non-state actors lead a chimeric existence.
For social media platforms, the distinction between state and non-state actors is increasingly blurred due to the
vast reach that the platforms have in people’s lives, leading governments to constantly intervene in the platforms’
daily operations [163] or even prop up the platforms, e.g., the case of Twitter, Iran, and the US State Department [97]
and the case of USAID-funded ZunZuneo [99, 100]. So deeply and confoundingly intertwined is the public-private
relationship that in [109], the author explicitly set out to argue that it is simultaneously unlikely and likely that
courts will conclude that a social media company is a state actor.
Distinguishing between private and public entities among those engaged in info ops would be similarly difficult.
Former intelligence operatives naturally gravitate towards private info ops firms, e.g., [124, 126, 164, 165, 166], and
these operatives bring along their contacts in the government, skills, and knowledge into their new roles [166]. One
remaining difference may be the scale of resources that state-level actors can muster compared to non-state actors,
but even that disparity is vanishing as states outsource info ops to private entities, potentially as a form of legalized
corruption via awarding lucrative contracts [156, 167] and as a way to shield themselves from culpability (Section
2.2.4). According to Oxford Internet Institute’s 2020 Industrialized Disinformation report, despite the difficulty
in “tracking down contractual evidence of private contracting firms”, they found that “almost US $60 million was
spent on hiring firms for computational propaganda since 2009” [168]. Public-private joint efforts can be seen in
CENTCOM awarding a $2.76M contract to the private corporation Ntrepid to develop OEV’s persona management
software [118]; in the US State Department awarding a $500,000 contract to Cambridge Analytica’s parent company
SCL for “target audience research” [169]; in the many info ops companies manipulating democratic elections at the
behest of clients from democratic states [89, 90, 91, 115, 121, 122, 123, 124, 125, 126, 164, 166]; in Team Jorge running
info ops through “Demoman International, which is registered on a website run by the Israeli Ministry of Defense
to promote defence exports” [121, 122]; and in NAFO, which according to a Kyiv Post interview of its founder, is
“endorsed by U.S. Congressman Adam Kinzinger, as well as U.K. Minister of Defense Ben Wallace” [170].
Conducting info ops against other democracies is not beyond the pale for democracies. Many documented in-
stances exist. The campaigns conducted by the UK-based Cambridge Analytica in support of Trump and in col-
laboration [124, 165, 169] with the Israeli Team Jorge is a well-known example [89, 90, 91]. The actions of Israeli
info ops companies in meddling with non-US democracies — e.g., Team Jorge’s interference 3 in “33 presidential-level
election campaigns, 27 of which were successful” [121, 122]; Percepto’s info ops against a Burkina Faso election [126];
Archimedes targeting a Nigerian election [125] — are no less impactful simply because they received comparatively
little attention in mainstream media and scholarly circles. Israeli Prime Minister Netanyahu also attempted to influ-
ence the 2016 election in favor of Trump [166]. Info ops conducted by an outside actor may even be orchestrated by
paymasters situated within the targeted state. Trump campaign official Rick Gates sought proposals from an Israeli
2In recent years, it has come to light, through the reporting by outlets such as Current Affairs, The Guardian, and The Wire
[160, 161, 162], that indiscriminate bombing via drones has instilled terror in the hearts of the populace in many regions of the
Middle East. Children have come to fear clear blue skies because those are the perfect weather for flying drones.
3Veracity of Haaretz’s reporting: “Journalists from The Guardian, Der Spiegel, Die Zeit, Le Monde, the international
organization of investigative journalists OCCRP, Radio France, Haaretz, TheMarker and other media outlets worked in France,
Kenya, Israel, the United States, Indonesia, Germany, Tanzania and Spain to examine the veracity of Jorge’s claims about his
worldwide deeds. Shockingly, many of the allegations were corroborated.” [121]
11

company Psy Group to “to create fake online identities, to use social media manipulation and to gather intelligence
to help defeat Republican primary race opponents and Hillary Clinton”; the proposal, named Project Rome, was
ultimately never acted upon [171, 172]. The US under the Obama regime in turn has employed covert info ops against
Israel [173]: a US Senate inquiry found that “[i]n service of V15 [an anti-Netanyahu group], OneVoice deployed its
social media platform, which more than doubled during the State Department grant period; used its database of voter
contact information, including email addresses . . . and enlisted its network of trained activists, many of whom were
recruited or trained under the grant, to support and recruit for V15.” Even a seemingly innocuous “voter button”
displayed on Facebook to encourage turnout in UK elections can be construed as an attack because Facebook, as a
US company, should not be influencing UK politics in any way [3].
All these examples are in essence the use of non-state intermediaries in information warfare involving three
state-level actors widely considered to be democracies (according to the Economist Intelligence Unit’s 2016 and 2022
Democracy Index [174, 175], the US and Israel are flawed democracies and the UK is a full democracy), putting to
rest the idea that info ops are only ever employed in the stalwart defense of peace, freedom, and democracy against
states with autocratic, authoritarian, totalitarian, etc. tendencies 4.
Info ops’ use by democracies is not limited to state-to-state situations. Info ops can be used against a democracy’s
own populace. In India, the world’s largest democracy, “[t]he 2014 election of Narendra Modi catapulted the BJP
to power thanks, at least in part, to an expansive network of ‘IT cells’ aimed at spreading positive news about the
BJP and attacking its detractors” [115]. Cambridge Analytica is believed to have influenced the Brexit vote results
[124, 190], though its culpability is disputed by some [191].
Having established that info ops originating from state and non-state actors would have no appreciable difference
due to ever-present public-private entanglement, we can claim that incorporating the publicized details of info ops
conducted by non-state actors into our modeling will not bias the model towards the form of info ops conducted by
non-state actors and vice versa, and we can claim that findings from Diluvsion simulations are equally applicable to
info ops from or against either state or non-state actors.
In Diluvsion, we defaulted to bots starting out embedded in a social network prior to being activated, in contrast
to some preceding models that started bots out with only a single connection (edge) to the network, e.g., [81], or let
bots have lower degrees than humans, e.g., [52], as they assumed that communities have not been penetrated by bots
prior to an info ops. Our choice is based on reports of uncovered info ops. Team Jorge estimated that about 1,000
bots are needed to “postpone an election in Africa without good cause” with half being newly created bots and the
other half preexisting bots [123]; the “inventory of fictitious accounts” were categorized based on regions/identities
(e.g., Arabs, Russians, Asians, and Africans) and reused for different info ops [121] — segmentation by region and
recycling bots for multiple campaigns strongly suggest that Team Jorge would equip bots with social relations (if
the bots’ positions within a social network did not matter, swapping in a campaign-appropriate regional identity on
preexisting bots instead of maintaining an extensive inventory would have been more cost-effective). AIMS bots also
exhibit meticulous attention to detail, with some of the bots even having bank accounts [123]. Taking that fact into
consideration, Team Jorge are unlikely to neglect situating their bots inside a suitably believable network of social
relations at creation time. Percepto’s case adds further support to the likelihood of bots having relations. One of
Percepto’s bots was an entirely fictitious investigative reporter based in Paris that had a real news agency with actual
humans working under the bot [126]. Even the simplistic bots that apparently failed in manipulating Singaporean
elections “appear relatively ubiquitous throughout the social network” despite a “failure to amass network influence”
[152]. The strongest evidence comes from bots used in the covert pro-Western info ops studied by Graphika and
SIO [120], which exhibited “a typical long-tail distribution in the follower footprints, with a few influential accounts
followed by a descending list of accounts with progressively fewer followers”, showing that the distribution of node
degrees among bots mimic that of humans on social media (in most [192, 193] but not all cases [194] of human
networks). The probability of an info ops bot army starting out from the periphery of a network is low.
3 The Model — Diluvsion
In our information diffusion model for Twitter-like social media, Diluvsion, information is composed of two elements:
stance and themes. Stances are polarized and exclusionary. A message can have multiple but non-repeated themes.
The dissemination of stances through the network is of greater concern to us than themes. Details on stances and
4For purveyors of “No True Scotsman” and “Democratic Peace” [176]: Some academics have argued that Israel is an apartheid
state [177] and also a settler colonial state [178]. The US has been characterized as an oligarchy [179] and as a plutocracy
[180, 181], and some Americans prefer to define the US as a republic [182]. The UK may fit the definition of an “electoral
authoritarian” regime [183] due to a history of banning political parties [184], media censorship [185], and electoral fraud [186],
on top of inheriting a hereditary monarchical head of state and hereditary peers in the House of Lords who exercise indirect
political influence [187]. An argument can also be advanced that certain states within the triad, being client states, lack true
sovereignty [188, 189] so conducting inter-state info ops does not constitute warfare as no one’s sovereignty has been violated.
12

themes are found in Section 3.1.
There are two major classes of agents in our model, humans (Section 3.4) and bots (Section 3.5). While “humans”
are exclusively humans, “bots” can encompass artificial algorithmic entities and natural organic entities so long as
they play the role of propagandist. Our motives for using this terminology are explained in Section 2.2.5.
Section 3.2 explains the attention-memory mechanism that agents are subjected to. In brief, the mechanism
aims to mimic the impact that real humans’ limited information processing capability and retention capacity can
have on information diffusion. Section 3.3 lists the range of actions that agents can perform within the simulation
to propagate or boost the propagation of stance and themes. Section 3.3.1 describes statistical data — engagement
metrics — that agents are exposed to and affected by. Section 3.3.2 describes indirect influence mechanisms as well
as the rationale behind our model’s reliance on engagement metrics as proxy for indirect influence.
The chosen resolution for Diluvsion simulations, i.e., the length of real-world time that a single step in the model
is equivalent to, is justified in Section 3.6. The starting parameters of the simulation are detailed in Section 3.8.
An assumption under our model is that all agents are devoted to debating one topic. They may devote a differing
amount of time per day on social media and their forms of engagement may differ (e.g., spending most of their time
liking posts they agree with, primarily retweeting others, etc.). These additional traits of the agents are sufficiently
divergent that each combination constitutes a sub-class of bots and humans (Section 3.8.1).
Private accounts are excluded from our model primarily because they have a limited ability to engage in public
debates; a private account’s tweets can only be seen by the account’s followers. For instance, if a private account sees
an opinion they disagree with, refutations that the private account u posts in reply will not be seen by the author
v of the disagreeable tweet and the author’s, v’s, followers if the author v is not a follower of the private account
u. This limited reach of private accounts makes them inappropriate for inclusion in simulations of public info ops.
Additionally, private accounts constitute a small minority of Twitter users so their exclusion would not drastically
affect our results. According to a Pew Research Center survey on adult US Twitter users conducted in 2019, 13% of
Twitter accounts are private [195].
We also exclude the “silent majority”/“no activity” users (Section 3.8.1) from our model because their lack of
activity means that there is little data to collect on how they exert influence and how they, in turn, are influenced.
Their lack of activity also means that they would have no discernible impact on the evolution of a Twitter discourse.
Diluvsion is built on the Python agent-based modeling framework Mesa, which in turn uses the Python network
analysis package NetworkX as a backbone.
3.1 Stances and themes
Stances are opinions on an issue. To ease interpretability, we allow only three discrete stances in our model: two
located at the poles and one at the exact midpoint between the two. We let the distance from the midpoint to either
pole be one. The three stances are known as negative, neutral, and positive. Alternate names used throughout this
paper for the negative stance include “con”, “against”, and “opposition” and the positive stance is also known by
“pro”, “favor”, and “support”. While not all opinions can be modeled under this system, e.g., opinions on the actual
worth of a used car, many can be, e.g., opinions on voluntary abortion.
Our model differs from others in the literature, e.g., [80], in that we allow neutrality as a stance to be propagated.
Bipolar ideological battles have been consistently framed as drawing users to either pole, but not taking a stand can
be as principled a stance as taking a stand, at least in principle, although perhaps not always in practice (some may
argue that true equidistant neutrality in the strictest sense does not exist as everything exhibits a bias5). An example
of a manifestation of neutrality is the Non-Aligned Movement [199] in geopolitics.
Stances are different from sentiments. Sentiments are concerned with the emotive content of a message, whereas
stances are concerned with the message’s position with regards to an issue of interest. For example, both statements “I
hate wearing masks” and “I hate doctors not wearing masks around immunocompromised patients” show a negative
sentiment due to their negative tone and presence of words such as “hate” in them, but in terms of stances, the first
statement is against mask-wearing while the second is in favor.
Themes are the non-polarizable aspects of an opinion, and they are non-polarizable only with respect to the issue
of interest. We illustrate the concept with an example where the issue of interest is mask-wearing: a message decrying
5Academics, e.g., [10, 13], have argued that mass media always represent ruling class interests, making impartiality impossible.
To maintain a facade of impartiality, mass media “strictly limit the spectrum of acceptable opinion, but allow very lively
debate within that spectrum” [196]. Others have argued that journalism, “in its pretense of ideological neutrality”, created
“a particularly pernicious myth” as the presence of filters in both the news reporter and news consumer prevents neutrality
[197]. Spiral of silence [53] predicts that some people are unwilling to voice out an opinion to avoid contradicting what is
perceived to be a majority opinion. Such inaction can be interpreted as neutrality, yet it does not contribute to the emergence
of neutrality but instead contributes to the (potentially false) majority’s continued dominance. Central banks invoking market
neutrality to depoliticize corporate security purchase decisions are biased because “[a]s critical political economists, sociologists
and anthropologists have so frequently argued, markets embody a specific, political vision of society, which is not shared by
every member of the polity” [198].
13

a store for banning masked patrons for fear of criminal intentions and another message praising a store for banning
unmasked patrons out of health concerns, despite differences in stance (anti- vs. pro-mask) and sentiment (negative
in condemning vs. positive in complimenting), are united under the common theme of “non-medical authority” being
exercised. And although people may have opinions on authority (favor or against), those stances have no direct
bearing on the issue of concern, mask-wearing. Themes are comparable to the concept of frames in the field of
communications [200, 201, 202] but is not equivalent to frames 6. A frame is envisioned as a wrapper, a method
of carrying messages. Different perspectives (wrapper) on an issue (message) changes one’s perception on an issue.
For us, themes function as more than wrappers. They are capable of being transmitted to (infecting) a target, just
like stances. There can be multiple themes per message just as there can be multiple frames/wrappers per message.
Multiple themes are similar to opinions encoded as binary strings in the rumor spreading model introduced in [79]
and to a lesser degree the discrete-numbered cultures in the Axelrod model [48], SMSim’s single-topic bit vector [85],
and AMID’s fuzzy set multi-topic messages [78].
The usefulness of explicitly modeling themes and having multiple themes per tweet/user can be demonstrated
with an example involving an unpopular theme (adopted by a low percentage of agents). To make things easier to
understand, we name this theme “conspiracy”. By wrapping every message a bot army tweets out with a layer of
conspiracy and by having more popular themes accompany the conspiracy theme since multiple themes are allowed,
we can ensure that the conspiracy theme is more willingly adopted by others because of its constant presence and its
association with popular themes. This ultimately results in a conspiratorial mindset slowly taking over the targeted
human populace on social media. We indeed simulated such a scenario under Diluvsion (Sim 9, Section 6.4). A less
nefarious theme can always take the place of “conspiracy”, e.g, “affordability”.
Each message, i.e., tweet, in our model is composed of a single stance and one or more themes. Each agent has a
stance and a set of themes as well. Agents can switch stances and can adopt themes over time. To keep the agents’
themes from homogenizing as the simulation progresses because of the adoption mechanic, the maximum number of
themes that an agent can possess at any one time is always lower than the set of all available themes in a simulation.
This limitation also reflects that not all aspects (themes) of an issue can be the core interests of an agent; people
have a limited capacity to care. All tweets by an agent will have the same stance as the one held by the agent at
the time of tweeting. Themes, however, can differ between tweets (Sections 3.4 and 3.5), e.g., a human agent will
use the same themes as the tweet it is replying to, even if the themes are not part of the agent’s theme set. Under
Diluvsion, compatibility in both the stance and the themes is required to improve the persuasiveness of a message
to its recipient (Section 3.8.2). Once again using a mask-wearing example, a message that attempts to proselytize
mask-wearing through the themes of safety and medical authority will find no purchase on an agent whose themes
reflect a concern for comfort, e.g., masks being difficult to breathe through. Stance plus themes can also be thought
of as viral variants, except that the transmission of stance and themes is dependent on homophily, but viral variants
do not necessarily operate under this mechanic 7.
3.2 Memory and attention
Memory and attention mechanisms are common features in many models of information diffusion, e.g., [22, 78, 79,
80, 81] and the motivations behind incorporating such mechanisms are largely similar. Modeling agents as having
limited attention and limited memory is meant to reflect the reality where humans are incapable of digesting all
the information presented to them and retaining the digested information over the long term. Diluvsion features
an attention and memory mechanism. An attention-memory limit governs the number of tweets that an agent sees
per activation (when an agent wakes during a time-step and performs actions), the number of its own most recently
6To underscore the importance of themes/frames: Incidentally, the concept of framing introduced by Tversky and Kahneman
was first motivated by the “Asian disease problem” [203], where people were surveyed on their preferences to two solutions to an
“unusual Asian disease”, with one solution framed as saving lives and the other as causing deaths. Framing the disease as Asian
betrays a problematic inclination harbored by the authors in their supposition that a disease terrible enough to force people
to face a moral dilemma could have only originated from Asia or Asians, much like SARS and SARS-CoV-2 are exoticized and
racialized as Asian [204, 205]. But perhaps the framing of framing’s motivating problem can be excused as it dates from an era
when people have yet to learn to better hide their prejudices. In the own words of Kahneman, “[s]ome people have commented
that the ‘Asian’ label is unnecessary and pejorative . . . but the example was written in the 1970s, when sensitivity to group
labels was less developed than it is today” [206]. The term “Asian disease problem” remains in common usage in scholarly
circles today.
7There is some superficial similarity in how newer variants of SARS-CoV-2 such as Delta and Omicron evolve greater binding
affinity to ACE2 receptors in human cells than the ancestral wild type [207, 208]. Antibodies and some therapeutics either
aim to present a more attractive binding target for the virus or bind to ACE2 receptors first before the virus [209, 210, 211],
essentially outcompeting the virus. Themes are analogous to binding affinity, where a tweet exhibiting a greater number of
matching themes (homophily) with the targeted user increases the chance of the tweet’s stance being accepted by the targeted
user, just as a the strength of binding affinity can influence whether an antibody (a stance) or a virus (a different stance) binds
to a host cell.
14

tweeted tweets that the agent remembers, and the number of users that the agents remember seeing. Memory observes
the first-in first-out (FIFO) queue, with the newest item displacing the oldest should the limit of a memory bin is
reached. Since it is a combination attention and memory limit, it is possible for items that have entered an agent’s
memory to be forgotten before the items have a chance to be seen by the agent. For instance, if there are 31 new
tweets directed to an agent whose memory is empty and has a limit of 30, the earliest/oldest 31 st tweet will be
“forgotten” before ever being read by the agent. The memory of seen users is duplicative and cumulative: a user
can appear more than once in an agent’s history and users that appear more frequently are given greater weight in
calculations (e.g., when deciding which user to follow).
While we keep track of the history of all users seen by an agent (this history is different and separate from the
limited memory seen user history) and the history of all influential users (users that infected/changed the stance of
the agent), they do not affect agent behavior and are only used by us to diagnose how influence spreads in the social
network (Section 5). These histories are also duplicative.
Bots are constrained by a memory limit though theirs is several times higher than that of the humans. Bots are
assumed to be more dedicated to spreading stances and/or themes than regular humans whose social media usage is
less singularly goal-driven. Therefore, bots would dedicate more resources, such as greater attention and memory, to
accomplish their goals.
3.3 Engagement
The ways in which a user can engage with the social media platform Twitter are referred to as actions in our model.
The set of actions available to an agent in our model — following, unfollowing, like, tweet, retweet, quote-tweet, and
reply— is different from the set of engagement metrics, which we will discuss in Section 3.3.1.
Following is a one-way relationship where the follower u indicates their interest in receiving updates on the
activities of the followee, v, e.g., when v tweets, retweets, etc. Unfollowing is the sundering of the follow relationship.
A follower following a followee indicates that the follower is receptive to information flowing out from the followee.
A loss of interest in the followee and/or the followee’s tweets losing their informativeness often leads to the demise of
the follow relationship [212, 213]. In our model, a potential followee having matching stance and themes with a user
increases the candidate’s chance of being followed by the user.
Liking (previously known as “favoriting”) is the most voluminous [214] action performed by Twitter users. Likes
on social media can be considered a “numeric representation of social acceptance” [215]. The bandwagon effect —
the heuristic of following the crowd used by humans when other signals of authenticity are weak or absent — can
guide a person’s decision to like, as people were found to be more likely to like photos with many likes over those
with few likes [216].
Tweeting is the act of composing and posting a message on the social media platform. Since our model excludes
private accounts, all tweets are assumed to be publicly viewable and searchable. While there are a number of factors
(Twitter’s algorithm, a human user’s own preferences, etc.) affecting whether these viewable tweets are actually seen
by users, our model assumes that an agent’s tweets are always seen by the agent’s followers so long as the tweet
remains in the memory (Section 3.2) of the followers. While not the most common action, the production of tweets
is the basis for all other actions, except for following and unfollowing, because liking, retweeting, etc., require tweets
to first exist.
Retweeting is the sharing of another’s tweet with one’s followers without any embellishment. According to [217],
retweets indicate interest, trust, and agreement with the message. As credibility and trust are important to having
a tweet retweeted, our model factored trust into an human agent’s decision on which tweet to retweet. Rather than
using a randomly generated number to quantify trust relationship between agents, we relied on indirect influence,
namely engagement metrics (like, retweet itself, and reply), as a proxy for trust (detailed in Section 3.3.1, justified
in Section 3.3.2).
Replying is responding to another’s tweet with one’s own tweet, not as an independent tweet but as a tweet that
will be added to the original tweet’s reply thread, easily accessible by others should they tap or click on the original
tweet. While not all replies challenge the stance of the parent/source tweet, replies are strongly weighted towards
being negatory in nature. The Stance in Replies and Quotes (SRQ) dataset [218] shows that 44.0% of the replies
are against the stance expressed in the tweet being replied to (parent/source tweet), and that approximately half,
22.9%, are supportive. The remaining 33.2% are comments and queries about the parent tweet’s stance, which can
be interpreted as being neutral in nature. In the problem of detecting contradiction for rumorous claims [219], there
is a special category for detecting disagreeing replies (as opposed to expressing disagreement in independent tweets),
highlighting replies as vehicles for disagreement. Our model adheres to the conception of replies being primarily,
though not exclusively, negatory in nature.
Quote-tweeting, alternatively known as quoting, is sharing another’s tweet with one’s followers while adding extra
content from the quote-tweeter. Quote-tweeting is relatively rare, even when compared against replies. In a dataset of
COVID-19 tweets that consisted of just retweets, quote-tweets, and replies, quote-tweets’ share is 3.82% while replies
15

have 4.91% [220]. A study on the roles assumed by Twitter users on the platform [214] showed that quote-tweeting is
seldom practiced, with Repliers as a role and replying as an action outnumbering Quoters and quoting across all roles
and user activity levels save for Quoters themselves. The motivation behind quoting appears equally divided between
refuting and affirming the original tweet. In the SRQ dataset [218], 46.8% of quote-tweets are negatory with respect
to the quoted tweet and 43.5% are affirmatory, with the remaining 10.7% being comments and queries regarding the
quoted tweet’s stance. Stance ambivalence in motivating quote-tweets, as evinced by the even split between negatory
and affirmatory, is modeled in Diluvsion as compatibility in stance having a lower weight than themes when an agent
picks which tweet to quote-tweet.
Ratios can also offer clues on whether agreement or disagreement drives an action (Section 3.3.1). Actions as
modeled in Diluvsion is generally in agreement with findings from ratiometrics.
In our model, an agent’s decision to like, retweet, or reply to a tweet is partially based on the agent’s agreement
with the tweet’s stance and themes, and partially on whether the tweet’s popularity merits bandwagoning. Whether
popularity or compatibility is the dominant factor depends on which action is being taken, as detailed in the explana-
tion of this mechanism in Section 3.8.2. The existence of a follower-followee (or inverse) relationship between agents
does not influence an agent’s action; the “text semantics and contents” of a tweet, “regardless of tweet author”,
are the most important factors in determining if a user engages with a tweet through liking, retweeting, replying or
quoting [221].
Agents who received replies to their tweets or have had their tweets quoted usually receive notifications, so we
assume that information from replies and quote-tweets diffuse to the targeted agents. Additionally, replies to a reply-
tweet are read by a fixed percentage of the followers of the author of the tweet being replied to, which is a form of
non-social tie information diffusion (Section 3.3.2).
Like Twitter and other real-world social media platforms, we only allow a user to like a tweet once and retweet
a tweet once. The practice of including a link to a tweet, a in a reply-tweet, which increases the retweet counter of a
and can be performed multiple times, is excluded from our model. And although it is possible to reply to the same
tweet multiple times on Twitter, we restrict the number of times an agent can reply to a tweet to just one. Any
information that a replier wishes to convey through multiple replies to a parent tweet can be thought of as having
been consolidated into one reply.
Tweeting is the action that all agents, bot and human, default to if the agent’s attention-memory contains no seen
tweets or if the chosen action for a particular time-step of the simulation is invalid. Many actions, e.g., liking and
retweeting, require tweets to be present before they can act on those tweets, so this default behavior helps populate
the simulation with tweets. Invalid actions are common around simulation start due to a confluence of three factors
(1) the lack of tweets, (2) limiting each tweet to one like, retweet, quote-tweet, and reply each per user, and (3) liking
and retweeting being common actions. A consequence of tweet scarcity is that the action distributions generated
from the simulation deviate slightly from empirical data, despite the model using parameters from empirical data, as
we shall discuss in Section 4.
3.3.1 Engagement metrics and ratioing
There are three prominent engagement metrics — likes, retweets, and replies — visible to Twitter users. While we
allow for quote-tweeting as an action in our model, its metrics are not visible to agents in our model and are therefore
incapable of influencing the agents (Section 3.3.2). In the context of stance conversion, likes are positive, retweets
are moderately positive, and replies are moderately negative.
Excluding the number of quote-tweets from engagement metrics is because of this metric being hidden throughout
much of Twitter’s existence. In 2020, quote-tweets were still semi-hidden, with Twitter forcing users to tap/click on
a tweet then on the tweet’s retweets before they could see the number of retweets broken down into retweets and
quote-tweets [222, 223]. Besides quote-tweets, we also exclude additional metrics that have been surfaced since Elon
Musk’s Twitter acquisition, such as the counts of views and bookmarks a tweet has received. This is because the
foundations of our model — engagement data we and others have collected (Section 3.8.1) and the vast majority of
scholarly literature on the impact of engagement — date from the era when these statistics were hidden. On Twitter’s
current timeline interface where users scroll through tweets, only viewcounts have been added alongside the counts of
likes, retweets, and replies. The newly surfaced engagement metrics are also rarely displayed on other platforms, e.g.,
Instagram and YouTube only show the number of likes and replies that a post has received while the Twitter-like
Mastodon shows retweets, replies, and likes.
The number of followers is an engagement metric that does not influence human agents. Although a user’s
follower count is publicly visible to anyone who visits the user’s profile page, it is not visible in the context of other
actions — liking, retweeting, replying, and quote-tweeting. Visiting a user’s profile page is an extra step from the
typical Twitter usage behavior of “infinite scrolling”, breaking from a user interface (UI) designed to entrap users in
perpetually consuming media [224, 225]. For following and unfollowing a user, these actions are available as part of
a dropdown menu accessible by clicking an icon on a tweet; visiting a user’s profile page and being made aware of
16

the user’s follower count are entirely avoidable. Bots, however, do use follower count as information for some of their
decisions, as they are motivated agents of stance/theme propagation.
Ratioing on Twitter is a phenomenon that best expresses the logic behind engagement when Twitter conversations
involve contested issues. When a user expresses an objectionable opinion, others may express their disagreement by
replying to the user’s tweet. Should the number of replies (regardless of whether they all express disagreement) or
the number of likes of any one of the disagreeeing tweets outnumber the likes of the parent tweet, a “ratio” has been
achieved, i.e., the ratioed user has been publicly and quantitatively mocked. A study on an info ops campaign waged
by social media users opposed to the fossil fuel industry used ratioing as a means to identify tweets targeted by
the operatives as the operatives employed the strategy of questioning fossil fuel organizations’ legitimacy with large
numbers of negative comments [226]. A broader definition of ratioing includes cases in which the number of replies
exceeds the number of retweets. This definition was employed in a study of the different ratios of engagement metrics
that tweets from Presidents Trump and Obama received [227], which found that Trump consistently achieve higher
reply-retweet — more controversial — ratios compared to Obama.
3.3.2 Indirect influence and trust
Our conceptualization of influence departs from some works in the literature that regard all influences as having
a positive impact. These works include [228], which posits that the high trustingness of an acting agent and the
high trustworthiness of the acted-upon agent are the determinants behind the acting agent’s decision to act (retweet,
reply). Another work is [229], which deemed one user as having influenced another if the user engaged with the tweet
in any way (retweet, like, reply, quote, and follow). From the perspective of stance diffusion, such conceptualizations
of influence clash with empirical observations of why people choose to respond to messages. As discussed earlier in
Section 3.3, replies and, to a lesser extent, quote-tweets are often used to make rebuttals. Ratioing (Section 3.3.1)
demonstrates that not all interactions constitute affirmative influence. The disconnect between the models [228, 229]
and the data is a result of ignoring polarity/stance. Zhang et al. explicitly stated that their method of finding
matching tokens between two tweets “identify whether their topics are similar”; nothing is said about the user’s
stance on the topic.
Direct influence comes from direct attempts at persuasion, which in our model consists of the contents of a tweet
— its stance and themes. Direct influence travels along the prescribed lines of influence, social ties, from followee
to follower. Indirect influence is information outside of a tweet’s content that can influence an agent’s adoption of
the contents. Indirect influence can either increase or decrease the persuasiveness of tweets. Indirect influence can
operate outside of observable follower-followee relationships.
One form of indirect influence modeled under Diluvsion is the ability for replies to circumvent social ties when
transmitting information, where a certain percentage of the followers of the parent tweets’ authors will read the
replies (Section 3.8.2). Tweets in most cases can be replied to by any user, not just followers or followees. More than
just transmitting information to the user targeted by the reply, replies can also transmit information to the targeted
user’s followers. A browse through Twitter will reveal that many replies to tweets that have gained a lot of attention
(high number of likes, retweets, etc.), colloquially known as “going viral”, are advertisements or posts about topics
tangential to those of the original tweets, e.g., fake BTC giveaway scams [230] and shilling for cryptocurrency. They
are attempts to take advantage of the tweets’ popularity. The hope is that some of the attention can be diverted to
profitable or persuasive ends.
Attempts have been made to model such indirect routes of information diffusion. The model proposed in [84]
allows for tweets that have crossed a certain threshold of engagement numbers to go viral, meaning that the tweet
will be “shown to all agents in the network that share the same topics with the sender agent, even if an edge does
not connect them”. From our perspective, the indirect propagation of information captured in their implementation
appears limited, as most information still travels along the network edges in their model. The sole exceptions were
viral tweets. In Diluvsion, virality would naturally emerge from the propensity for agents to favor sharing or otherwise
engaging with popular tweets over unpopular ones (bandwagoning) since engagement metrics, themselves a form of
indirect influence, factor into an agent’s decisions on which tweet to engage.
The engagement metrics discussed in Section 3.3.1 constitutes a form of indirect influence. The metrics serve as
both [6, 231, 232] social cues for the bandwagon effect [233, 234] and social cues for computing source trustworthiness
[78, 228, 231] and message credibility [232].
Engagement metrics taking the place of credibility is supported by the existing research literature. One study
found that “bandwagon heuristics—such as the number of likes, comments, and retweets—increased the credibility of
news” [232]. The automated activity of social probing by non-human-like bots with zero trust, i.e., strangers, which
in the case of [235] consists of visiting the profile page of others, can boost popularity. That popularity translated
successfully to influence, which was getting others to follow accounts recommended by the bots. The number of
retweets, despite its noisiness and bias, has a positive correlation with expert-assessed credibility of messages, and
it is effective at predicting ground-truth credibility when combined with credibility ratings from a different crowd,
17

Mechanical Turk annotators [236]. Cues in the form of retweets (information sharing) boosted the credibility of a
tweet’s author regardless of whether the tweet originated from a peer or a stranger, and even if the retweets were
performed by strangers [231]. Conversely, source credibility was found to play a major role in the information sharing
behavior of users on Twitter [237]. Credibility and influence are intertwined, feeding off each other and creating a
rich-get-richer effect, where the wealth is social capital.
The need to impute a separate trust value for a social tie shared between two agents is also obviated by engagement
metrics that can serve as proxies. We improve upon the trust mechanism found in [78, 228], where the proxy variables
for trust are the number of times a user has retweeted [78, 228] and replied [228] to another user, by factoring in the
relationship between engagement type, stance distance, and themes; weighing the different engagement metrics; and
counting indirect engagement actions instead of direct ones. The authors of [228] themselves noted that replies as a
proxy can be unreliable because replies may contain users expressing a stance different from the parent tweet, lending
support to our decision to account for stance when using engagement metrics. Whether an engagement type is driven
by heterophilia or homophilia in stances and themes (and consequently the metric generated for the engagement
type) under our model is explained in Section 3.3.
As for using indirect engagement numbers over direct ones as proxies for trust, indirect engagement can be more
reliable than direct engagement despite appearing counter-intuitive.
Traditional indicators of sources as being authoritative are less visible online [238] because of a flattening of
hierarchies. Surmounting the accessibility barrier (e.g., radiocommunication spectrum licensing, capital costs of print
media) and the expertise barrier (e.g., sufficiently credentialed to be invited onto mass media to comment on an
issue) denoted authoritativeness pre-social media, but under social media where such barriers towards broadcasting a
message has disappeared, so too has their function as indicators of trustworthiness. Distrust in authoritative sources
has also been on the rise, further weakening traditional signals of credibility. Distrust in authority being a widespread
phenomenon is evident in Twitter discourse on vaccine and climate change where “science” (science as a source of
authority, not science as practiced) is regarded with suspicion [239, 240, 241]. While an authoritative source can still
engender trust on social media, a stranger retweeting information from an authoritative source actually reduces the
trustworthiness of the source, whereas a stranger retweeting peers or other strangers increases trustworthiness [231].
The rising distrust in authorities was an impetus for the development of bot-augmented decentralized info ops (as
discussed in Sections 2.2.4 and 3.5). On social media, the audience has also been flattened through the phenomenon
of context collapse [242], where users cannot tailor messages to pander to specific subgroups because messages posted
on social media are viewable by all, making it easy to offend others, with the offense causing diminished trust in the
source [243].
With direct trust in a message’s source significantly dampened by flattened hierarchy and context, message
credibility and user trustworthiness online are strongly coupled. Social media users become only as trustworthy as
the credibility of their messages. People judge the credibility of information by engagement metrics attached to
that information [231, 232]. Consequently, crowdsourcing trust is an established practice, e.g., computation of a
Twitter user’s credibility based on the degree of agreement between the user’s tweets and their respective replies
[244]. Engagement-based source credibility indiscriminately boosts the credibility of peers and strangers [231]. These
engagement metrics are susceptible to the bandwagon effect, in which people base their opinion on what they perceive
to be the opinion of the collective herd [231, 232], e.g., liking what others liked and retweeting what other have
retweeted. Another factor at play is minority-avoidance and the spiral of silence, as discussed in Section 2.1.3. Trust
quantified by indirect engagement numbers is the overwhelmingly dominant form of trust online.
That is not to say that a message source under an indirect trust system, e.g., as implemented in Diluvsion, is
wholly incapable of affecting the message’s credibility, and by extension, the source’s trustworthiness. A source that
has amassed a large following of users sharing similar stances is likelier to receive more likes for its message than a
user with zero followers.
The pervasive indirect influence of engagement metrics extends beyond how one perceives others and into how
one perceives oneself. Every additional like or retweet that a user receives for their own tweets serves as a small
validation, affirmation, and acceptance of the online self [215, 245]. Under Diluvsion, an agent’s memory of its own
recently tweeted tweets also influences stance adoption, and the agent’s perception of those recently tweeted tweets
are shaped by their respective engagement metrics. Because an agent’s tweet’s stance is always the same as the
agent’s (unless they recently changed their stance) under our model, if an agent’s recent tweets have received a lot of
affirmation (e.g., a high number of likes), the agent will be more likely to retain their stance even when they encounter
a lot of opposition to their stance in their memory of seen tweets (memory of others’ tweets that they saw).
Figure 1 demonstrates how indirect influence operates to infect an agent. This example omits the influence of
stance and theme compatibility between the tweets and the agent in an infection event. For an example that does
include it, see Section 6.5.
18

H1
H2B1
H3
H4
B2 B3
H1
H2B1
H3
H4
B2 B3
H1
H2B1
H3
H4
B2 B3
Memory (H1)
Stance # L # RT # RP
Pro 0 0 0
A B
C D
Follow Action (reply-tweet, like) Bot Human Negative Neutral Positive
H1
H2B1
H3
H4
B2 B3
Self-Memory (H1)
Stance # L # RT # RP
Neu 0 0 1
Memory (H1)
Stance # L # RT # RP
Con 0 0 0
Pro 0 0 0
Self-Memory (H1)
Stance # L # RT # RP
Neu 0 0 2
Memory (H1)
Stance # L # RT # RP
Con 2 0 0
Con 0 0 0
Pro 0 0 1
Self-Memory (H1)
Stance # L # RT # RP
Neu 0 0 2
Memory (H1)
Stance # L # RT # RP
Pro 0 0 0
Con 2 0 0
Con 0 0 0
Self-Memory (H1)
Stance # L # RT # RP
Neu 0 0 3
Figure 1: At time-step 1, a neutral human agent (H1) makes a tweet (action not depicted in this figure)
expressing a neutral stance and themes of medical authority and individual liberty over collective good, e.g.,
“My doctor tells me wearing masks is a personal preference.” (A) While still at time-step 1, a second human
agent (H2), H1’s follower, concocts a reply-tweet with matching themes but a positive stance, e.g., “The
CDC said masks protect everyone, not just the wearer.” (B) A negative bot (B1) calls poll tweets, which
is equivalent to doing a search of existing tweets, finds H1’s neutral tweet, and replies with a negative tweet.
(C) A third human agent (H3) makes a reply-tweet with a negative stance to H2’s earlier reply to H1. Two
bots (B2 and B3) liked H3’s reply-tweet. H3’s reply happens to be seen by H1 because H1, as a follower
of H2, occasionally reads the replies to H2’s tweets. (D) A fourth human agent (H4) makes a tweet with a
positive stance that is seen by H1, which pushes the very first tweet seen out of H1’s limited memory. (E,
not shown) At the start of time-step 2, when read conversion is called, H1 observes one positive-stanced
tweet without any engagement, two negative-stanced tweets, one which received two likes, and finally its
own neutral-stanced tweet that received three replies. To determine if H1 will experience a stance conversion
after reading these tweets, we check if a generated uniform random number clears H1’s resistance threshold.
The number does. To see which stance from the seen tweets infect H1, a weight is calculated for each stance.
The negative stance has a heavier weight than neutral or positive because the negative tweets are greater
in number and have affirmative engagement instead of negatory (likes instead of replies). Weighted random
choice picks the negative stance, H1 changes its stance to negative.
19

3.4 Humans
An agent designated as “human” in our model is an idealized representation of a typical social media user. All
human agents follow the same heuristics, and they also have the same maximum memory size and maximum number
of concurrent themes. Human agents may differ in their starting stance and themes, starting infection resistance,
activity level, and roles. Over the course of the simulation, their stances and themes may change. Resistance evolves
with every infection (stance change). Their activity level and roles remain fixed. The heuristics and maximums
remain fixed as well.
The roles taken on by human agents, as well as their activity levels, are based on empirical Twitter data (Section
3.8.1). Roles are the five groups that users were placed into based on their favored engagement action on Twitter,
e.g., they were known as Likers if they exhibited a tendency to like others’ tweets rather than compose their own
tweets. Users were also separately placed into three activeness categories depending on the number of observable
actions taken per week. Each role, with respect to its activity level, will have the highest frequency for the engagement
action that the role is named for, e.g., moderately active Quoters will have the highest frequency of quote-tweeting
compared to other moderately active roles. However, the same role will have different action frequency distributions
between different activity levels, e.g., a highly active Quoter will be likelier to like tweets than they are to quote-tweet,
but a moderately active Quoter will quote-tweet more often than like.
At every time-step, a check is performed to determine whether a human agent wakes. If it wakes, it will read
tweets and potentially be infected by the tweets it has read. If it is awake, a second check is performed to determine
whether it has used up its allotted quota of weekly actions (this quota is based on its assigned activity level). If it
has not, the agent will definitely act during this time-step. If it has, the agent will have a very small fixed random
chance of acting. The actions that an agent can perform are discussed in Section 3.3.
For all actions, the part that involves broadcasting a stance — i.e.,writing a reply, a tweet, or a quote-tweet — the
broadcasted stance is always the same as the agent’s. Themes for replies and quote-tweets always match the themes
of the parent tweet; the assumption is that when responding to another, normal users would not go off-topic. Themes
for an independent tweet are drawn from the agent’s own pool of themes, with themes that have been recently used
by an agent having greater probability of being chosen. For the part of an action that does not explicitly broadcast
a stance, i.e., selecting a tweet to like, retweet, quote, or reply to, the agent will favor tweets with stance and themes
that align with its own, but the agent is also influenced by engagement metrics to pick tweets with different stances
and themes.
To be infected, a uniform random number must first exceed an agent’s resistance threshold. A high resistance
results in fewer infection events being triggered. If the threshold is cleared, one stance among the tweets an agent has
read will be selected as the infecting stance. The selection is random, but each stance is weighted by the engagement
metrics (Section 3.3.1) and by the compatibility of the tweets representing the stance. The compatibility calculation
factors in themes as well, e.g., for a neutral agent (equidistant from both poles), a group of tweets representing the
positive stance that has many matching themes will influence the agent more strongly than a similar-sized group of
negative tweets with non-matching themes, all else being equal. A successful infection results in the agent’s adoption
of not just the infecting stance but also a portion of the most popular themes found in the tweets representing the
infecting stance. Examples of the infection mechanism at work can be found in Figure 1 (the influence of stance and
theme compatibility is omitted in this example) and in Section 6.5.
Although we have called infection as stance “change” or “conversion” throughout this paper, an infection event
can end with an agent being infected by the same stance. This situation can be thought of as witnessing strong
arguments that affirms one’s faith in one’s stance.
Resistance is altered by infections. If the infecting stance is the same as the one held by an agent at the start of
an infection event, the infection will improve resistance. Infections by non-matching stances degrade resistance. This
mechanism is inspired by certain viruses such as the Hepatitis C virus (HCV) whose infection some people can clear,
whereas in certain other population segments they induce an impaired immune response thereby allowing reinfections
or chronic infections [246, 247]. More domain-appropriate inspirations are the observed instances of people slowly
doubting their worldview if some strongly held beliefs have been shattered (e.g., South Korean feminists “taking the
red pill”[248], spiral of mistrust/cynicism [249]).
3.5 Bots
Bots are propagandists, biological (Section 2.2.5) or electronic, dedicated to promoting a stance on a social network.
The key differences between bots and humans are: a bot’s stance is fixed, a bot never unfollows another user, a bot
constantly surveys the conversation landscape, and a bot has a greater memory capacity. The set of heuristics that a
bot follows also differ from that of humans as they are designed to spread their stance as widely as possible. None of
the differences should be interpreted as bots having superhuman abilities or access to tools on social media platforms
that regular users do not. The difference is purely a result of motivation and prioritization. Bots are just as limited
20

as humans in terms of their activity levels and roles.
A bot surveying the conversation landscape, poll tweet, at the start of every time-step is equivalent to running
a search or covertly reading tweets from accounts that it does not follow. A fixed number of the most recent tweets
are returned with each survey attempt and these tweets are saved into the bot’s memory of seen tweets. Surveying
allows bots to take note of tweets/conversations that may have escaped the attention of human agents. If necessary,
bots can jump into the conversations to influence other agents. This form of non-social tie information acquisition is
exclusive to bots. For human agents, non-social tie information is acquired if they happen to be randomly selected
as the followers who have read a reply to their followee’s tweet (see Section 3.3; the mechanism applies to bots too).
Bots do not unfollow so as to avoid triggering reciprocal unfollowing among their followers. Bots want as large
an audience as possible to maximize the reach of their messages. This desire for a large audience is also manifested
when choosing which tweets to quote, retweet, or reply to. Unlike humans who will only consider engagement and
compatibility, bots will additionally consider a tweet author’s follower count, favoring those who have large counts.
Bots not changing their stance is simply a result of them being bots, i.e., unyielding propagandists. Their greater
memory capacity (Section 3.2) is also due to them being motivated agents of change.
However, bots do adopt new themes. Since bots are conceptualized as being interested in altering only the
stances with regard to the issue of interest, theme adoption does not compromise the bots’ mission as themes are
non-polarizable with regard to the issue of interest (Section 3.1). It may even aid in the bots’ mission as bots can
better empathize with the rest of the agent population, e.g., composing tweets with themes that resonate with other
agents and are able to infect others more because of greater theme compatibility.
When bots have to choose which tweet to reply to, they have two tactics — targeting vulnerable users and
targeting high engagement tweets — that they alternate between. A probability distribution governs how often one
tactic is used over the other. To target vulnerable users is to target tweets from users who have a low number of
followees. The reasoning for this tactic is that such users have low number of information sources (followees) and are
therefore more easily swayed by a flood of information from non-followees. To target high engagement tweets is to
target tweets whose engagement metrics are the highest among those that a bot has witnessed in its memory and
are authored by users with high follower counts. This tactic maximizes the visibility of a tweet as high engagement
tweets are likelier (due to bandwagoning) to be targeted by agents for actions that trigger information sharing such
as replying, retweeting, and quote-tweeting. This tactic has real-world precedence, e.g., BTC scams [230].
Replies and quote-tweets authored by bots have the same stance as each bot’s respective stance, just like humans,
but the process of themes selection differs from humans. While humans would use the same themes as the parent
tweets, bots would only use half of the themes from parent tweets, while the other half is drawn randomly from
each bot’s pool of themes. In the case where a bot’s themes deviate significantly from the population, this tactic
serves to subtly inject the bot’s themes into the information environment to facilitate infection in the future, while
infection chances at present are improved by adopting half of the same themes as the parent tweet. Theme selection
for independent tweets also differs from humans, as a bot does not select based on a history of its own tweets. Instead,
following the same selfish/motivated reasoning as when replying and quote-tweeting, half of the themes are the most
common themes found in a bot’s seen tweet memory while the remaining half are randomly chosen from the bot’s
pool of themes.
Like humans, bots start out embedded in a network instead of starting out in the network’s periphery. Section
2.2.6 explains the reasoning behind this positioning. The bots in our simulation are bound by the same diurnal
activity schedule as the one humans follow. This is informed by the activity data of the covert pro-Western info ops’
assets, which have peaks and troughs [120] that mimic a human’s. Motivated by decentralization (Section 2.2.4), the
bots act independently (just like human agents) and are not conscious of the presence of other bots. Naturally, this
excludes explicit coordination between the bots.
Bots operate the same across stances within Diluvsion, unlike other works that split propagandists based on
stance. For instance, the “bad guys” bots/trolls class of agents in twitter sim actively spread disinformation while
the “good guys” stiflers in twitter sim [81] are reactionary by design, only countering disinformation that they see
and never proactively spreading truth.
3.6 Temporal resolution
Humans follow a diurnal cycle, and their inclination towards being active on social media follows a similar cycle [250].
Therefore, the human and bot agents in our model also observe this cycle. The mean number of tweets from a dataset
of mask-wearing conversations on Twitter, binned by the day of the week and the time of the day, gave us an action-
probability table. This table approximates the likelihood of an average Twitter user using the service at a particular
time-step. Within each time-step, the order in which the agents activate is random. A consequence of simulating
peaks and troughs in platform activity levels is that during periods of high activity, information dissemination and
actions to boost dissemination will reach the highest number of awake users. However, at the same time, the great
21

volume of information flowing during high activity periods means that disseminated information risks being pushed
out of the memory (Section 3.2) of agents with high numbers of incoming links.
The resolution of the simulation is 30 minutes. This resolution is sufficient and has empirical support: the
Graphika and SIO investigation found that the info ops “assets in the Afghanistan and Central Asia groups typically
posted at roughly 15-minute or 30-minute intervals in any given hour” [120]. Our decision was also influenced by the
mean weekly frequency (the number of actions taken by a user in a week) for the high-activity group in the study
by Antelmi et al., which was found to be 133.84 [214]. If we took 133.84 actions and divided them over seven days,
this leaves approximately 19 actions per day. At a resolution of 30 minutes, 19 actions will take 9.5 hours, including
the interval time between actions. This wakefulness period does not violate typical sleep-wake cycles within human
circadian rhythms [251].
As validation, when we generated 1,000,000 sets of 336 random numbers (2 periods per hour × 24 hours × 7 days)
with a 0.9 damping factor 8 and tested them against the activity-probability table (derived from our mask-wearing
dataset), the maximum number of periods/time-step in which an agent is awake was 153 .45 ± 8.46 per week, a range
which can accommodate the maximum number of actions the most active class of agents can take per week within
our model (we let this maximum be the rounded mean number of actions of high activity users, 134, from the dataset
in [214], which is different from the mask-wearing dataset used to generate the action-probability table). To allow for
variability, once an agent exhausts its allotted action quota, if a random number check against the action-probability
table says that the agent is awake and can therefore take an action, the agent has a fixed 1% chance of exceeding the
quota.
3.7 Graph structure
Directed scale-free graphs were used as the simulation environments. Specifically, we used the improved version [252]
of the algorithm first introduced in [253] by Schweimer et al. for generating random directed social network (SN)
graphs for use in information diffusion studies. The hyperparameters used for graph generation comes from the
hyperparameters file in the open-source code repository shared by the author 9 which themselves are derived from
crawling real-world social networks on Twitter. The set of hyperparameters used were named “Covid”, the largest
of the 14 networks crawled with 50,133 nodes and 4,832,226 edges.
Desirable network properties such as a high amount of clustering and reciprocity are reproduced by the SN
graph generation algorithm. Clustering describes users aggregating into homophilic clusters when interacting online
on Facebook and Twitter [254]. Reciprocity describes the small but still significant amount of reciprocal edges on
social media (22.1% found on Twitter [255]). If we used non-SN scale-free graph generation algorithms, e.g., the
one proposed in [256] by Bollob´ as et al. which improved upon the Barabasi-Albert method, certain properties of the
network deviate further from expectations than if an SN graph generation algorithm was used (Section 4).
A total of 20 graphs with 1,000 nodes and 20 graphs with 900 nodes were generated. Because of an inherent
flaw [253] of the graph generation algorithm itself, approximately 2.5% of the nodes for each graph are isolates, i.e.,
the nodes have no incoming or outgoing edges. The graphs were saved and reused for different scenarios to allow
for reproducible results and also because graph generation is time consuming. The graphs with 900 nodes were used
for the “peripheral”/“fringe” scenarios where bots (10% of the network population, equivalent to 100 agents) do not
start out embedded in the network but is added to the graph later and given only one outgoing edge to a random
node, i.e., a bot’s only social tie is being a follower of an existing human user.
3.8 Parameterization
The same set of parameters are used for validation (Section 4) and simulations (Section 5).
3.8.1 Empirical data
To ensure that agents populating the network mimic the behavior of those found in real-world social media, we
initialize the agents based on statistical data collected from Twitter users.
For the diurnal activity schedule, we took the mean number of tweets split by day of the week and into half-hour
intervals (the resolution of the simulation) from the two million tweets we collected on COVID-19 masking debate
between January 1–June 21, 2020 as a probability distribution for when an agent will be active.
The starting distributions of stances and themes, including the starting number of themes per agent, are taken
from the February 27–March 2, 2020 period of the COVID-19 masking debate, which we have identified as the starting
point for when the majority of the discussions occur within the appropriate context of masking as protection against
8When multiplied by probabilities in the action-probability table (Section 3.8.1), which can range from 0 to 1, the factor
shifts the graph down/reduces the amplitude, i.e., lowers the action probability.
9https://github.com/Buters147/Social_Network_Graph_Generator
22

COVID-19 instead of masking in other contexts, e.g., masks to protect against volcanic ashfall. A total of 12 themes
are identified from the dataset. Examples of the themes are “encourage” (encouraging people to mask or to not
mask) and “appraisal-critize” (praising others for wearing or for not wearing masks).
Although the proportions of stances and themes at the population level are maintained, the stance and the themes
chosen for an individual human agent are entirely random, unaffected by the agent’s neighbor’s stance and themes.
Some may take issue with our choice since homophily would predict that users sharing similar outlooks, political
or otherwise, are more likely to be connected, so there should be homogeneous stance and theme clusters in the
network. For emerging issues where strong narratives have not been established, the situation is not so clear-cut.
Republicans are more anti-mask during the COVID-19-pandemic than Democrats [257, 258], but the Twitter data on
mask-wearing that we collected showed that right before the pandemic, many fans of Trump supporter Scott Presler
were urging him to wear a mask to avoid catching disease from homeless people.
The counts of users found in the high, medium, and low activity categories are taken from [214]. For the range
of actions available to the agents (Section 3.3) except for following and unfollowing, the frequency distribution is
based on the tables and figures in [214]. In [214], the authors categorized users into five roles — Tweeters, Quoters,
Retweeters, Repliers, and Likers — with a corresponding action frequency distribution. Each role is further sub-
divided into high, medium, low, and no activity. Although almost 50% of users belong to the no activity cluster
(no visible activity but have done at least one hidden activity such as changing their screen name), we exclude this
category because they would have no appreciable impact on the simulation dynamics owing to their inactivity. This
leaves us with 5 × 3 = 15 human agent categories.
Statistics on following and unfollowing are not found in [214]. We relied on the descriptions provided in [212, 259].
According to Kwak et al., the “average of unfollows is 15.4” and “average number of followees increases from 59.7 to
75.7” in 51 days with “about 30% of users [having] unfollowed at least once” [212]. According to Myers and Leskovec,
“[i]n a given month a user of degree 100 tends to gain 10 and loose [sic] 3 followers” [259]). Their descriptions
showed that while following and unfollowing are pervasive over a scale of multiple months, they are rare when one
factors in all the possible actions that a user can take (tweeting, retweeting, etc.) at the scale of half-hour steps
which our simulation runs at. Modeling the actions of following and unfollowing as suitably rare events translates to
having follow and unfollow constituting 0 .6% and 0 .3% of all of an agent’s actions, respectively. This applies to all
15 agent categories. Given that highly active and moderately active agents form 10.4% and 22.2% of the population
(totaling ∼ 30%) and their actions per week are 134 and 66, respectively, we expect highly active agents to follow
134 × 0.66% × 4 = 3 .5 users and unfollow 1 .8 users over 28 days while moderately active users would attempt 1 .7
follows and 0.9 unfollows, which is slightly lower than the frequency observed in [212].
The parameterization of activity levels and roles used statistics from [214] because it cannot be done using the
mask-wearing dataset. Only tweet-level data were collected for the mask-wearing dataset; user-level data were absent.
However, this does provide us an opportunity to validate a simulation using parameters from the dataset in [214]
against an “unobserved” dataset (the mask-wearing dataset), as we shall see in Section 4, which is a more informative
validation process than using the same dataset from which the parameters are drawn.
3.8.2 Best approximations
Certain parameters in our model require information that the existing literature does not provide and that we were
unable to collect. The resistance to stance conversion is one such parameter. We opt to model the resistance as a
truncated normal distribution with a low of 0.5, a mean of 0.75, a high of 1.0, and a standard deviation of 0.25. The
size of a human agent’s memory is fixed at m = 30, and this upper limit is used for three separate memory bins,
which are the agent’s own recent tweets, tweets by others that an agent has seen, and the author of those seen tweets.
Bots have a memory of 120 and poll tweet returns 30 tweets each time. The number of themes that every human
and bot agent can hold at once is five while the maximum percentage of new themes that an agent will adopt is
40% for humans and bots. Humans adopt themes upon a successful infection, whereas bots adopt themes at every
time-step. All of a user’s tweets are assumed to propagate to all of the user’s followers, although not all tweets are
guaranteed to be seen as older tweets risk being pushed out of a follower’s limited memory by newer tweets. The
proportion of a user u’s followers who see a reply from another user v to a tweet from u, which is the primary method
of non-social tie information propagation in our model (there are other methods such as u retweeting a seen tweet
from a non-followee user), is set at 10%, with u’s followers being chosen at random.
Every infection event by a stance matching a human agent’s own increases the agent’s resistance by 1% while
an infection by a non-matching stance decreases the agent’s resistance, with the decrease being proportional to the
distance between the stances, −0.5% for the closest neighboring stance and −1% for the stance on the opposite pole.
Stance compatibility is simply the distance between two stances divided by 2, cs = |suser − stweet|/2. Division by
the maximum distance between stances, 2, ensures that the maximum value of cs is 1. Themes compatibility is the
number of matching themes divided by the number of unique themes, ct = |tuser ∩ ttweet|/|tuser ∪ ttweet|. Compatibility,
c = csws + ctwt where ws is the weight for stance compatibility and wt is the weight for themes compatibility.
23

The default values for {ws, wt} are {1, 0.8} so having matching stances is more important than matching themes.
Note that since incompatibility, not compatibility, in stances increases the chance of replying, the compatibility score
when replying is calculated slightly differently, c = ((1 − cs) × ws) + ctwt. Weights are also modified when replying,
{ws, wt} are {0.8, 1} to mildly de-emphasize stance compatibility, thus preventing replies from being exclusively an
act of disagreement with a tweet’s stance.
When deciding on which tweet to reply to, a human agent will prefer to reply to tweets that have the same themes
but a different stance, giving less consideration to the amount of engagement that a tweet has received. When deciding
which tweet to retweet, human agents will prefer tweets with matching stance and themes, with a tweet’s engagement
having slightly less weight on the decision. Quote-tweets emphasize theme compatibility over stance compatibility
when choosing a target tweet to quote, and a slight importance is placed on compatibility over engagement just like
when retweeting. The probability score of a tweet being liked, retweeted, quoted, or replied to, p = gwg + cwc where
w stands for weight, g for engagement, and c for stance and theme compatibility. The weights {wg, wc} are {0.5, 1}
when replying, {0.8, 1} when retweeting and quote-tweeting, and {1, 1} when liking. Engagement is a weighted sum
of metric counts, g = Nlikewlike + NR TwR T+ Nreplywreply. The weights used differ based on the action taken (e.g., in
deciding whether one should like a tweet, the bandwagon heuristic would more pay more attention to the number of
likes the tweet has instead of the number of replies). The weights for the engagement metrics, {wlike, wR T, wreply},
for the engagement actions of liking, retweeting, quoting, and replying are {1, 0.2, 0.2}, {0.2, 1, 0.2}, {0.2, 1, 0.2}, and
{0.2, 1, 0.2} respectively. Quote-tweeting and retweeting have the same weights as both actions expose one’s followers
to another’s tweet. Both g and c are normalized by dividing over the values summed over all candidate tweets, e.g.,
for a tweet x, gx = gx/ PNcandidate n=1 gn.
Bots differ from humans in that their probability for choosing a target,p = g+c+f , meaning that the probabilities
are unweighted and an additional term f has been added for the follower counts of the tweet authors. Like g and
c, f is normalized. And instead of the probabilities being used in weighted random choice, they are used to sort
the candidate tweets and the tweet with the highest probability is always selected. Bots also weigh each metric in
engagement g and the weights, {wlike, wR T, wreply}, for liking, retweeting, quoting, and replying are the same as those
of humans.
Within the sub-component of the read conversion algorithm for computing a human agent’s stance changes,
the compatibility score, rc, for each stance (e.g., rc-pro) is the sum of the individual compatibility scores for the
subset of an agent’s seen tweets that exhibit the stance. The same applies to the engagement metrics’ scores,
rg. The compatibility scores are normalized by dividing over the total score for messages of all stances. The
engagement scores are normalized on a per-engagement type basis by dividing over the total of the frequencies for
an engagement type. Prior to summation, the engagement metrics are weighted, {wlike, wR T, wreply} = {1, 0.5, −0.5}.
The weighting reflects whether an engagement action is affirmatory or negatory in the context of stances. The
summed compatibility scores and engagement metrics’ scores are also weighted to avoid stance conversion from
being entirely dominated by engagement metrics. The weight for compatibility is an agent’s memory, m, while the
weight for engagement is the reciprocal, 1/m. As such, the final conversion score for a stance, e.g., pro, wr−pro =
m−1rg-pro + mrc-pro where rg-pro = PNpro x=1 gx and rc-pro = ( PNpro x=1 cx)/ P c. The engagement score for a tweet
x is gx = wlikeNlike-x/ P Nlike + wR TNR T-x/ P NR T+ wreplyNreply-x/ P Nreply. The conversion scores are used as
probabilities for selecting the stance which a human agent would convert to if its resistance threshold has been
exceeded.
4 Validation
Validating information diffusion models can take the form of showing that the model is able to generate statistical
distributions similar to those in the real world, e.g., recreating the percentages of tweets that receive zero engagement
and tweets that go viral by adjusting parameters [84], and matching curve shapes for message volume [85]. Another
method is confirming that the parameters used in the model match those found in the real world, e.g., Twitter usage
inter-arrival time in the twitter sim model [81] by Beskow and Carley.
As explained in Section 3.8.1, a large number of key parameters in our model such as the distribution of a user’s
actions, a user’s degree of activity (cognate to inter-arrival time), and the distribution of user roles are taken directly
from real-world data. The underlying graph structure on which the simulation is run on (Section 3.7) and the user’s
dirunal schedule (Section 3.6) are also based on real-world data. Our model would naturally reproduce inter-arrival
time, action distribution, etc., that are close (though not perfect matches) to empirical observations. Therefore, we
have “validated” our model in the same sense that Beskow and Carley have.
For additional validation, we compared the engagement statistics obtained from simulations with those obtained
from real-world data, namely the Twitter on mask-wearing conversations pertaining to the COVID-19 pandemic
(Section 3.8.1). Differences and similarities between statistics collected empirically and from the simulation are
shown in Figure 2. The simulations are run for a period equivalent to 28 days and data was aggregated from 20
24

runs. Parameters for the agents are the same as those described in Section 3.8. The configuration for the human-only
simulation scenario is equivalent to the Sim 11 scenario described in Section 5.
There are two sets of real-world distributions from the mask-wearing dataset in Figure 2 as we intend to illustrate
how distributions can differ depending on how hotly a topic is contested. Each set of distributions is from the complete
month-long period of the named month. The January 2020 data are from a less popular and less contentious period as
it is composed of tweets that have been classified as out-of-topic/containing no stances, i.e., they are not offering any
opinion on mask-wearing as it relates to COVID-19, but they are discussing masks in other contexts (e.g., protection
against volcanic ash, fictional characters). In contrast, the March 2020 distribution is a subset of only tweets that
have stances. March is also the period we have identified as when the mask-wearing conversation occured almost
exclusively in the context of COVID-19.
The January distributions, from a subset where masks are a less contentious and less discussed topic, all contain
lower values than the March distributions, i.e., shifted left. The distributions from the simulation in Figure 2 nearly
overlap the empirical January distribution for likes and replies. The simulation distribution is visibly shifted right
compared to the January distribution when comparing retweets, although it is still bound to the right by the March
distribution. For simulations, the within-dataset ratios Nlike : NR Tand Nlike : Nreply are on average 2.0 and 8.4
respectively, close to the numbers calculated directly from the data from which the simulation parameters are drawn
(sans simulation), which are 2.1 and 8.5. If we had instead used a non-social network-specific graph generation
algorithm (Section 3.7), the discrepancy between the simulation and empirical ratios would have been starker, as
the simulation ratios obtained would have been 1.7 and 5.2, validating our choice in the graph generation algorithm.
January mask-wearing data shows ratios of 3.8 and 22.5, while March’s ratios are 3.3 and 13.2. Retweets and especially
replies are intensified when a topic is contentious (March), hence the lower ratios.
One factor involved in the discrepancy in distributions and ratios is the insufficient number of tweets at simulation
start for agents to like, retweet, etc. We alleviated tweet scarcity by having an agent default to tweeting as an action
if there are no incoming tweets in its memory and whenever a chosen action for a time-step is invalid. A consequence
of this design choice is that the observed action distribution of agents would differ from the parameters they were
given, as they tweeted more often than they should. However, the alternative of doing nothing if a chosen action for
a time-step is invalid would have caused a similar issue of mismatch between parameters and observed distribution of
actions taken, in addition to causing an agent to appear less active (due to skipped actions) and causing the starting
phase of the simulation to last longer (due to tweet scarcity). We had considered seeding the simulation with a set
of initial tweets but decided against it as the assumptions and ramifications — heuristic for distributing the initial
tweets to the nodes, the tweets causing stance changes in agents immediately at simulation start, etc. — would
complicate the analysis of the simulation results.
Another partial explanation for this difference is the size and structure of the networks. Simulations relied on
a synthetic scale-free network as the graph structure in terms of the follower-followee network of the mask-wearing
dataset is unknown to us. When compared with the January dataset, the across-dataaset ratio for the counts of likes,
Nlike-Sim : Nlike-Jan, is 2.7, that of retweets, NR T-Sim: NR T-Jan, is 1.4, and that of replies, Nreply-Sim : Nreply-Jan, is
1.0. When compared with March, the respective ratios are 30.3, 18.0, and 19.2. If we infer the hidden size of the
network through the engagement counts (hidden size because users in the mask-wearing dataset cannot represent the
totality of network; metrics for a tweet can originate from a user outside the collected dataset), the number of users
in January could be at least 2 .7× larger than in the simulation and for March, 20 .3× larger.
The across-dataset ratio of replies as well as the within-dataset ratios indicate that the simulations show a greater
affinity to March than January data. For all engagement types, a constant multiplier of ∼ 1.5× reproduces March’s
ratios for within-dataset ratios, whereas while the across-dataset ratios for March’s ratios are a constant ∼ 20×
of the simulations except for Nlike-Sim : Nlike-Mar. January’s multipliers differs depending on engagement type for
across-dataset (∼ 2× and ∼ 3×) and within-dataset ( ∼ 3×, ∼ 1.5×, and ∼ 1×) cases. This makes the simulation a
closer approximation of conditions where a topic is heavily debated, i.e., March’s conditions.
Overall, the distributions for the engagement actions strongly resemble real-world data, owing to the real-world
statistics used to initialize simulation parameters and the robust SN-graph generation algorithm that also relied on
empirical data. As the indirect influence from engagement actions and the metrics resulting from those actions are
central to Diluvsion, the findings in this section supports the model’s validity.
5 Simulations
We present a number of simulations, starting from the baseline scenario of bots representing two disadvantaged stances
engaged in a co-opetitive influence operation and continuing with simulations where certain key functionalities of the
bots are progressively altered/degraded, which can be thought of as ablation studies. Other scenarios tested the effect
of varying the mixture of bot-backed stances. The results from the simulations are shown in Table 1 and we grouped
our discussion of the results in Section 6 based on their implications for conducting real-world info ops. All scenarios
25

100 101 102 103
100
101
102
103
104
Frequency
# likes
100 101 102 103
100
101
102
103
104 # RTs
100 101 102 103
100
101
102
103
104 # Replies
Sim, humans only
Empirical, Jan,
no stance
Empirical, Mar,
has stances
Figure 2: Engagement metrics: real-world data vs simulations with 1,000 agents.
featured 1,000 agents in scale-free networks and the results were averaged over 20 runs, with each run lasting 1344
steps (includes step 0, equivalent to 28 days). A bot’s role determines its action distribution, i.e., the probabilities for
liking, retweeting, etc. at each time-step. A role is named after the most frequent action the role takes, e.g., Likers
like liking. Bot frequency is the number of times a bot is permitted to act per week. The definitions for both roles
and frequencies (activity levels) are based on the Twitter data reported in [214], and the definitions apply to bots
and humans.
In classical influence maximization (Section 2.1.3), information that we wish to see widely propagated is injected
via nodes that have been algorithmically identified as influential, i.e., positioned to maximize spread, but the bots
in our simulations have no such advantage as their positions in the network are entirely random. Starting from the
periphery of a network is the most disadvantaged position our bots are subjected to (Sims 6 and 7).
Inter- and intra-stance awareness of the presence of other bots is absent as the info ops is conducted in a decen-
tralized fashion (Section 2.2.4). Competition is implied as each agent can only belong to one stance so an agent’s
conversion from one stance to another directly results in losing an agent to the other stance group; bots from one
stance are not forbidden from converting agents belonging to a different bot-backed stance. Cooperation amongst
agents arise naturally because agents gravitate towards performing affirmative actions, e.g., liking, for other agents
that share similar a stance. Cooperation among two bot groups, each backing a different stance, can be implicit in that
their uncoordinated and even competitive actions can accomplish a common goal better than they can individually,
e.g., reducing support for a third non-bot-backed stance.
A high bot percentage, 10%, is used in all scenarios so that the impact from bots is more easily apparent, not
because this percentage is reflective of the actual bot population in the real world. Estimates of bot percentages on
Twitter vary widely depending on the source, with Twitter’s own analysis claiming 5.3% in 2022, a 2016 Securities
and Exchange Commission filing by Twitter claiming 8.5%, Cyabra claiming 11% in 2022, and a study on the 2020
Singaporean election claiming 26.99% [152, 260, 261]. Bots defaulting to a high activity level also makes their influence
more easily observable. Additionally, evidence exists that bots are prolific content creators on Twitter, with the Israeli
web analytics company Similarweb finding that “20%–29% of content in the US on Twitter is generated by bots”
[262].
To ensure that the overall stance ratio at simulation start matches the one at the start of March 2020 in the
mask-wearing dataset, the stance ratio for humans is rebalanced to account for the bots’ stance distribution. In other
words, the number of human agents assigned to a particular stance is reduced if bots are assigned to that stance.
As Sim 1 is the baseline, Sim 1 is referenced by all other scenarios for comparison in the scenario descriptions
below:
1. Sim 1: Bots belonging to two minority stances, neutral and opposition, attempt to maximize the spread of their
respective stances. The bot population is evenly split between neutral and opposition, and there are no bots
in the camp of supporters, making the bot population’s stance ratio 1 : 1 : 0 (pro : neutral : con). This stance
distribution enables us to observe synergistic and antagonistic effects between the two bot sub-populations.
For all agent types, the number of themes an agent has as well as the distribution of the 12 themes are the
same as in the March mask-wearing dataset. Bots start out embedded in the network, i.e., they have organic
follower-followee relationships just as human agents do for reasons we have argued in Section 2.2.6. All the
bots take on the role of a Replier to better demonstrate non-social tie spreading of information (Section 3.3.2).
Bots are as active as highly active humans are. In choosing whose tweets to reply to, bots will favor those
designated as vulnerable, which are people with a low number of information sources, i.e., low followee count.
26

Bots will adopt commonly encountered themes to help the tweets they compose appeal to a wider audience.
2. Sim 2: Bots will prioritize tweets that have high engagement metrics and that happen to also be authored
by people with high follower counts when deciding whose tweet to reply to instead of targeting tweets from
vulnerable agents as in Sim 1.
3. Sim 3: Bots are as active as moderately active humans rather than matching highly active humans’ frequency.
4. Sim 4: Instead of being Repliers, bots are Likers.
5. Sim 5: Instead of being Repliers, bots are Retweeters.
6. Sim 6: Instead of being embedded in the network, each bot starts out isolated in the fringes of the network
with only one followee relationship with a random human agent in the network (meaning that any tweet by the
bot that is not a reply or quote-tweet will not be read by anyone in the network). This replicates the difficult
starting condition that bots face at the start of an info-ops, as presumed by other researchers [81] but which
we have argued against in Section 2.2.6.
7. Sim 7: In addition to starting out in the fringes of the network as in Sim 6, bots take on the role of Likers
instead of Repliers.
8. Sim 8: Instead of being highly active Repliers, bots take on a variety of roles (Likers, Retweeters, etc.) with
variable activity levels: low, medium, and high, just like human agents. The role and activity level distributions
of the bots follow the distributions in [214].
9. Sim 9: Bots conserve a theme, Theme 7, instead of following the usual theme adoption process. Conservation
involves a set of conserved themes that always have priority whenever the bot updates its list of themes to
adopt and whenever the bot needs to decide which themes its tweet should be accompanied by.
10. Sim 10: Just as in Sim 8, bots mimic human agents’ roles and activity levels. Furthermore, the distribution of
the bots’ stances are the same as the humans’ stance distribution from the March 2020 mask-wearing dataset.
11. Sim 11: All agents in this scenario are humans, unlike other scenarios that contain 10% bots.
12. Sim 12: Bots are evenly distributed between supporters and detractors instead of being evenly distributed
between neutrals and detractors, 1 : 0 : 1 (negative : neutral : positive).
13. Sim 13: Bot distribution follows a 1 : 0 : 0 (negative : neutral : positive) ratio.
14. Sim 14: Bot distribution follows a 1 : 1 : 1 (negative : neutral : positive) ratio.
15. Sim 15: Bot distribution follows a 2 : 2 : 1 (negative : neutral : positive) ratio.
16. Sim 16: Bot distribution follows a 4 : 0 : 1 (negative : neutral : positive) ratio.
6 Results and discussion
The simulation results are shown in Table 1. Figure 3 shows the temporal evolution of the stances for the simulations
in Table 1 while Figure 4 shows the temporal evolution for follower and followee counts, split by stances. Figures
5, 6, 7, 8, and 9 are for our discussion on the consequences of bots starting out embedded in the network versus its
periphery (Section 6.5).
A note on the presentation of the results: not all models of information diffusion are strongly deterministic, which
is why some authors, e.g., [52], opted to instead show the number of simulations in which the bot-backed stance
becomes dominant instead of showing the average number of agents per stance at the conclusion of a simulation as
we have done in this paper. However, because our simulations all have a biased start where one stance is a clear
majority that outnumbers the combined total of the minority stances by a factor of 2.7 to 1 (human agents’ stances
are evenly split in [52]) and bots can back more than one stance per scenario (bots all back the negative opinion in
[52]), reporting our results as percentages of runs in which the bot-backed stance dominates is not viable.
When we speak of a “majority” or a “minority” stance, we are referring a stance’s share among the agent
population at the beginning of the simulation.
Since Diluvsion is designed to support studies on info ops, discussion of simulation results will be interwoven with
discussion of their relevance to info ops.
6.1 Polarization
Winner-takes-all, i.e., no polarization/unipolar polarization, is the natural trend of a network where a stance has a
numerical advantage over the combined total from minority stances, as witnessed in Sim 11 and Sim 10. This trend is
not meaningfully altered whether the network is populated entirely by human agents (Sim 11) or the network contains
27

Sim 1 Sim 2 Sim 3 Sim 4 Sim 5 Sim 6 Sim 7 Sim 8
Stance ratio (bot) 1 : 1 : 0 1 : 1 : 0 1 : 1 : 0 1 : 1 : 0 1 : 1 : 0 1 : 1 : 0 1 : 1 : 0 1 : 1 : 0
Bot start Embed Embed Embed Embed Embed F ringe F ringe Embed
Bot roles Replier Replier Replier Liker R T er Replier Liker Human
Bot frequency Hi-hum. Hi-hum. Md-hum. Hi-hum. Hi-hum. Hi-hum. Hi-hum. Human
Bot reply Vuln. Engage Vuln. Vuln. Vuln. Vuln. Vuln. Vuln.
Bot adopts themes Yes Yes Yes Yes Yes Yes Yes Yes
Start/End N (Con) 139 305 345 133* 212 101* 70* 64* 109*
Start/End N (Neu.) 129 568 551 400* 391* 159* 74* 67* 124*
Start/End N (Pro) 732 127 105 468* 397* 740* 856* 870* 767*
Start/End N (T1) 158 232 223 277 246 236 224 404* 248
Start/End N (T2) 240 240 230 259 270 310* 374* 264 303*
Start/End N (T3) 549 288 317 329 360* 430* 592* 589* 439*
Start/End N (T4) 188 244 236 263 261 271 306 246 311
Start/End N (T5) 34 204 195 189 184 181 126* 155 180
Start/End N (T6) 69 220 237 219 223 203 190 142* 172*
Start/End N (T7) 1 60 56 87 36 34 20* 15* 54
Start/End N (T8) 52 218 195 194 224 191 144* 196 206
Start/End N (T9) 26 193 221 186 176 172 126* 101* 151
Start/End N (T10) 35 187 177 193 198 157 131* 137 132*
Start/End N (T11) 26 194 207 184 185 180 108* 125* 144*
Start/End N (T12) 26 200 178* 191 190 159* 142* 105* 151*
Sim 9 Sim 10 Sim 11 Sim 12 Sim 13 Sim 14 Sim 15 Sim 16
Stance ratio (bot) 1 : 1 : 0 March - 1 : 0 : 1 1 : 0 : 0 1 : 1 : 1 2 : 2 : 1 4 : 0 : 1
Bot start Embed Embed - Embed Embed Embed Embed Embed
Bot roles Replier Human - Replier Replier Replier Replier Replier
Bot frequency Hi-hum. Human - Hi-hum. Hi-hum. Hi-hum. Hi-hum. Hi-hum.
Bot reply Vuln. Vuln. - Vuln. Vuln. Vuln. Vuln. Vuln.
Bot adopts themes Consv. Yes - Yes Yes Yes Yes Yes
Start/End N (Con) 139 320 25* 12* 196* 760* 115* 213 540*
Start/End N (Neu.) 129 536 63* 61* 8* 6* 228* 372* 7*
Start/End N (Pro) 732 143 912* 926* 796* 234* 658* 415* 452*
Start/End N (T1) 158 197* 231 312 220 219 236 243 243
Start/End N (T2) 240 218 347* 367* 246 237 248 229 241
Start/End N (T3) 549 266 427* 571* 305 303 298 290 301
Start/End N (T4) 188 214 283 355* 220 232 218 238 231
Start/End N (T5) 34 139* 190 61* 180 204 202 210 188
Start/End N (T6) 69 181* 182 151* 198 205 214 221 200
Start/End N (T7) 1 519* 29 4* 69 38 40 51 23
Start/End N (T8) 52 175* 184 138 196 190 204 206 194
Start/End N (T9) 26 160* 140* 66* 171 189 187 207 192
Start/End N (T10) 35 152* 153 56* 195 181 182 212* 194
Start/End N (T11) 26 174 124* 38* 179 190 206 193 178
Start/End N (T12) 26 157* 144* 81* 175 191 192 173* 188
Table 1: The number of agents holding a stance and theme(s) at simulation end averaged over 20 runs for
16 scenarios with 1,000 agents. Agents can adopt a maximum of five themes. Stance ratio is negative :
neutral : positive. An asterisk (*) indicates significant difference ( p < 0.05) compared to Sim 1. Starting
number of agents for a stance or a theme is listed on the unnamed column on the left, between the column
of row names and the named columns.
28

0
500
1000 Sim 1 Sim 2 Sim 3 Sim 4
0
500
1000 Sim 5 Sim 6 Sim 7 Sim 8
0
500
1000 Sim 9 Sim 10 Sim 11 Sim 12
0 4 8 12 16 20 24 28
Days
0
500
1000 Sim 13
0 4 8 12 16 20 24 28
Days
Sim 14
0 4 8 12 16 20 24 28
Days
Sim 15
0 4 8 12 16 20 24 28
Days
Sim 16
Against Neutral Favor
Figure 3: Temporal evolution of stance distribution among 1,000 agents. Values are from 20-run averages of
different scenarios/simulations. Values at simulation end corresponds to the mean values reported in Table
1. Descriptions of the scenarios are found in Table 1 and in Section 5.
10% bots which are allocated similarly as the human population’s stance distribution (Sim 10). The slightly higher
number of agents belonging to the minority stances in Sim 10 is likely a consequence of the bots’ presence, whose
stances can never be changed, slowing but not halting the network from reaching a consensus around the majority
opinion. These are only trends, and not necessarily the final outcomes, as the simulations need to be run longer to
observe whether all agents converge to a single opinion. And in the case where bots populate the simulation, Sim 10,
the network will never fully converge as bots will never change their stance.
A winner-takes-all result [54] has been found for networks with competing viruses where one virus is stronger
than the other, and the strength of the virus is quantified by a single numerical parameter (derived from attack and
recovery rates). While the viruses (opinions) in our model are equal in that they do not have an explicit parameter
that offers one virus an advantage over others, a combination of factors enable the dominant stance in our work
to replicate a similar advantage over competitors. The dominant stance in Diluvsion is the stronger virus because
homophily dictates that the stance has a more receptive audience, and their greater number means that their opinions
are broadcasted and boosted more often, making others more susceptible to succumbing to peer pressure and adopting
the majority stance.
Polarization can be induced if bots are present, and the stance distribution of bots differs from that of the humans.
When half of the entire bot population holds a negative stance and the other half a neutral stance while the bots
are restricted to human-like role and activity level distributions (Sim 8), the encroachment of the majority opinion
is mostly halted. In Sims 12 and 16, where bots are only distributed between negative and positive stances with
none for neutral, assigned a role more suitable for stance propagation (Replier), and are all as active as highly active
humans, neutrals virtually disappear and agents congregate around the two polar opinions. In the case of Sim 13
where all agents start out belonging to only one minority stance, specifically the polar minority stance, a similar
depopulation of neutral agents is observed. More time-steps are needed to determine whether Sim 12 ends with this
polarized distribution or if all agents are eventually converted to the bot-backed negative stances.
In existing studies on binary opinion dynamics, consensus cannot be reached if stubborn agents are present in
the network [263, 264]. When the problem is extended to account for committed/stubborn agents and for multiple
opinions (greater than binary), only opinions that are backed by committed people survive under the voter model
[83]. The results from our simulations serve to further confirm the role played by stubborn agents, bots in our case,
in driving polarization in a network.
29

40
50# Agents
Sim 1
40
50
Sim 2
40
50
Sim 3
40
60 Sim 4
50
60# Agents
Sim 5
0
50
Sim 6
0
50 Sim 7
45
50
Sim 8
40
60# Agents
Sim 9
40
50
Sim 10
25
50
Sim 11
20
40
Sim 12
0 4 8 12 16 20 24 28
Days
30
40
50# Agents
Sim 13
0 4 8 12 16 20 24 28
Days
45
50
55
Sim 14
0 4 8 12 16 20 24 28
Days
50
60 Sim 15
0 4 8 12 16 20 24 28
Days
25
50
Sim 16
Followers-Against
Sources-Against
Followers-Neutral
Sources-Neutral
Followers-Favor
Sources-Favor
Figure 4: Temporal evolution of mean follower and followee (source) counts split by an agent’s stance for
20-run averages of different scenarios/simulations. When an agent converts to a stance at a time-step, its
follower and source counts are included in the average for the new stance and excluded for the old stance.
Subplots do not share a common range for the y-axis due to significant variance across scenarios. Descriptions
of the scenarios are found in Table 1 and in Section 5.
30

Figure 5: Embedded bots scenario. Each edge arrow represents the direction of information flow, i.e., the
inverse of a directed follower-followee relationship, for a simulation with 100 agents in conditions equivalent
to Sim 13 (Table 1). In standard graph notation for an edge/link ( u, v), u is a follower of v, so the follower-
followee relationship is u → v but the information flow is reversed, u ← v. The image on the left shows
the network at simulation start and has nodes sized according to the ratio of followers to followees. The
image on the right shows the graph at simulation end and nodes are sized according to the average ratio
of likes to replies received by the agent’s tweets 1 N Pi=1 N #likesi #repliesi , with higher values indicating that the agent’s tweets tend to have a perception of being well-received. As likes and replies are accumulated over the
course of a simulation, sizing the nodes based on engagement metrics is only possible post-simulation. The
edge/link widths for the image on the left has a fixed value, while those on the right are based on stance and
themes compatibility between two agents. Stance is indicated by each node’s color. Agency is indicated in
the edge/link color and the node’s border color. Blue nodes are the opposition, yellow nodes are neutral,
and green nodes are supporters. A red border indicates a bot while a white/invisible border indicates a
human.
31

Figure 6: Embedded bots scenario. From the same simulation run as Figure 5. The image on the left
shows whose tweets a node has seen at the end of the simulation. The image on the right shows whose
tweets contributed to a node’s stance switching at the end of the simulation. For both images, the edge
widths correspond to the frequency of the seen agent’s (left)/the contributor’s (right) appearance. Not all
seen tweets led to stance conversion, hence the difference. The color of each node indicates its stance while
the color of the node’s edges indicates agency. Blue nodes are the opposition, yellow nodes are neutral,
and green nodes are supporters. A red border indicates a bot while a white/invisible border indicates
a human. The edge/link colors distinguish between influence originating from bots, indicated in red, and
from humans, in black.
32

Figure 7: Peripheral bots scenario. Information flow for a simulation with 100 agents with all bots backing
the negative stance (no equivalent in Table 1, closest is Sim 6). This scenario differs from Sim 13 in Figures 5
and 6 only in that each bot starts out in the periphery/fringes with a single outgoing edge (follower-followee)
to a random human node instead of being embedded naturally in the network. This more challenging
starting condition resulted in the non-bot-backed dominant opinion maintaining its dominance, although
bots managed to convert two nodes in the fringes. Legend is the same as Figure 5.
33

Figure 8: Peripheral bots scenario. From the same simulation run as Figure 7. Left image shows how often
a different user’s tweets were seen by an agent while right image shows how often a different user’s tweets
converted an agent’s stance. Legend is the same as Figure 6.
Figure 9: Each box in the heatmap represents the stance of an agent at a particular time-step. The evolution
of an agent’s stance can be tracked by following a column from top to bottom. Agents are sorted by their
initial stances, leftmost are negative agents and rightmost are positive, with neutrals in between. Rapid
conversion at the early stage in the embedded scenario has rapidly eliminated neutral agents, hence their
seeming absence. Data are from the same simulation runs as Figures 5–8.
34

6.2 Impact of bots and bot ratios
Given that the distribution of roles and action frequencies among bots do not differ between the stances (i.e., bots all
have the same role and frequency regardless of the stance that they back), the ratio of bots between the stances has a
drastic impact on the temporal evolution of the stances, which can be seen in their impact on polarization in (Section
6.1). If the stance ratio of bots follows that of humans, then the bots backing the majority stance would suppress the
bots backing the minority stances, reproducing a dynamic very similar to the scenario where only humans presents
while bots are absent. The bots’ stance ratio must deviate from that of the humans to cause disequilibrium.
The co-opetitive relationship between the bots backing a minority polar stance (negative) and those backing a
minority midpoint stance (neutral) benefits the midpoint stance the most. Across all scenarios in which the two
minority stances are backed by an equal number of bots (Sims 1–9, 14, and 15), the number of neutral agents is
always greater than that of negative agents. We suspect that this is due to the neutral agents’ stance distance being
the shortest for both polar stances (except for the distance between a polar stance and itself). Once neutral agents
gain a critical mass through conversion, they have the numbers to peer pressure other agents in the network to adopt
their opinion. But the strength of neutral agents is also their greatest vulnerability. Without agents immune to stance
conversion, i.e., bots, in their midst, the group of neutral agents collapses quickly as they are the easiest targets to be
converted by the majority stance (which does not need to be bot-backed) and the bot-backed minority stance. This
phenomenon is evident in Sims 12, 13, and 16.
Depending on the info ops goal of the bots’ operators, one mixture of bots can be more optimal than the other.
If the goal is to maximize the number of agents holding a stance that is the polar opposite of the majority, all bot
resources should be devoted to backing that stance, as shown by the results of Sim 13. The cost of not having neutral
bots is a slight inefficiency in reducing the number of people holding the majority stance as seen in the greater number
of agents being positive at simulation end in Sim 13 compared to Sim 1. However, if one intends to purely reduce
the share of the majority stance, Sims 1 and 2 show that having an equal number of negative and neutral bots is the
most effective. The neutral agents’ smaller stance distance with positive agents makes them more persuasive. A side
effect of a bot operator employing the tactic of mixed neutral and negative bots is that the population of negative
agents is “cannibalized”, a consequence of the bots in our simulations acting independently to avoid being seen as
a centrally-directed, coordinated info ops. In cases where the positive stance is also backed by bots, using a mix of
neutral and negative bots to counter the positive bots (a pro : neutral : con ratio of 2 : 2 : 1 in Sim 15) still appears
marginally better than relying purely on negative bots (4 : 0 : 1 in Sim 16).
If the goal is to drive polarization, bots can be assigned to both ends of the pole at equal ratios (Sim 12) or
with a ratio that favors the minority polar stance (Sim 16). Without unwavering advocacy for neutrality, neutral
agents quickly dwindle to nothing, as polar opinions compete to attract users to their stance. In situations where
there are motivated neutral agents, they must be outnumbered to be overpowered. As Sim 10 shows, if the bots’
starting stance distribution matches that of the humans from the March mask-wearing dataset, which implies that
the numbers of bots representing the pro and neutral camps are roughly equivalent in most runs, the polar minority
stance, negative, diminishes in size far more rapidly than the midpoint minority stance, neutral.
For stances starting out from a disadvantaged position (negative and neutral at 13.9% and 12.9% of the pop-
ulation), Sims 15 and 16 show that the combined number of bots backing the non-majority stances requires an
approximate 4-to-1 numerical advantage over the bots backing the majority stance in order to reach influence parity,
assuming bots for all stances are similarly capable (same roles and activity levels). Should bots only back the polar
stances in equal numbers while neutral bots are absent, the majority stance maintains and extends its dominance,
nearly eliminating neutrals but is unable to penetrate the enclave of the non-neutral minority stance (Sim 12). The
source of the negative agents’ resilience against conversion can potentially be explained by Figure 4, where the follower
and followee counts for the bot-backed negative stance in Sim 12 remained steady as the simulation progresses (so did
the counts for the bot-backed positive stance). The neutral stance which lacked bot backing showed greater volatility
and trended downwards. Bots backing only one minority stance against the onslaught of the majority stance, which
can be seen in Sim 13, also stabilizes the follower and followee counts of the minority stance. Bot-backing may be
capable of creating echo chambers for minority stances.
Although echo chambers/filter bubbles are terrible for the purpose of gaining new recruits as the Islamic State’s
experience has shown (Section 6.3), echo chambers are excellent for the reinforcement and consolidation of opinions
[128]. A bot’s broadcasted messages can reach people sharing the same stance, allowing bots to drive stance retention,
i.e., keeping users with the same stance from being lost to other stances because those users are exposed to messages
containing alternative stances. Bots play much of the same role as stubborn users in other information diffusion
models; their unchanging stance making them ideal as the resilient core of a movement. Some have attributed
Trump’s electoral success to the presence of botnets “spreading pro-Trump content in overwhelming numbers” and
“digital echo chambers where users see content and posts that agree only with their preexisting beliefs” [265]. Using
bots to create echo chambers may even escape alerting social media monitors as certain platforms are already inclined
towards echo chamber formation, with researchers finding that “information diffusion is biased towards individuals
35

who share a similar leaning in some social media, namely Twitter and Facebook” compared to Reddit and Gab [254].
When great political orators across the entire American political spectrum, e.g., Hillary Clinton [266] and George
W. Bush, expressed sentiments along the lines of “you are either with us, or against us”, that there is no middle
ground, their words contain a kernel of truth. From the perspective of eroding the support base of a polar opinion
(e.g., pro-war), the actions taken by neutrals and the opposition (e.g., situationally pro-war/war-ambivalent and
anti-war) to draw people into supporting their respective stances have the same effect — erosion. All our simulations
featuring a pro : neutral : con stance ratio at 1 : 1 : 0 for bots provide evidence that support for the positive stance is
inevitably eroded (Sims 6 and 7 are not exceptions as they are just examples of bots being ineffectual, as discussed
in Section 6.5). In other words, if a predominant force supports one pole of a polarized issue, appealing to others
not to pick either side can make one a collaborator for the “enemy” (supporters of the opposite pole). The slightest
deviation from full, enthusiastic support of a stance is indeed “treachery”.
6.3 Stance conversion and retention strategies
Repetition is the key to success for info ops. Repetition in this case means being extremely active in disseminating
and boosting content. If the action frequency of the bots is cut in half, from 134 actions per week to 66, as seen in
Sim 1 vs. Sim 3, then bots are substantially less effective at promoting minority stances against a non-bot-backed
majority stance. This reduction in influence is also evident in other scenarios where bots went from being highly
active to adopting activity levels that mimic the human distribution (low activity and medium activity users make
up 67.4% and 22.2% of the human population respectively) which can be seen in Sim 1 vs. Sims 8 and 10. Our
observation that repetition is important has support, e.g., simulations in [76] which showed that high energy agents
contributed towards the prevalence of extreme opinions (polarization). Another study demonstrated that repetition
can turn into influence: a bot in a social media experiment that had gained popularity simply by periodically visiting
others’ profile pages later recommended accounts for users to follow and succeeded in convincing a majority of them
to take its recommendation [235].
Not all forms of repetitive action elicit the same responses from the network. Sims 4 and 5 show that bots
who favored liking or favored retweeting over all other actions are unable to convert as many users to their stance
compared to bots which favored replying (Sim 1) despite having the same high activity level. In the case of Sim 5,
the bots were only able to stop the majority opinion from gaining ground. There are several factors behind these
outcomes. In a situation where the bots represent the minority stance, there are a greater number of tweets that
express the majority stance and consequently more targets for negatory replies. On the other hand, bots that favor
liking and retweeting, which are affirmatory actions, are likely to have run out of minority stance tweets to boost.
As a small percentage of the population, bots are unlikely to occupy a majority of high-degree nodes, limiting the
reach of their messages. Replier bots can sidestep the lack of an audience by borrowing the audience of others as a
small portion of replies is seen by the followers of the parent tweet. Retweets, however, are only seen by the author
of the parent tweet (and the bot’s own followers). Liker bots do not have to find an audience as they are liking other
users’ tweets that already have audiences, namely those other users’ followers, but the reach of liker bots is largely
confined to these audiences as they seldom invade the conversations of other users compared to Replier bots. Since
minority stances are minorities population-wise and Liker bots who back a minority stance will favor liking tweets
advocating the minority stance, the audience of tweets liked by Liker bots are small too, although not as small as
that of Retweeter bots.
Targeting vulnerable users — friendless people, i.e., having a low number of followees — for replies can result in a
similar number of stance conversions as the alternative tactic of finding the largest platform to shout from (replying
to tweets with high engagement), as demonstrated by Sim 1 vs. Sim 2. Also, in terms of decreasing the number of
people holding the majority stance, both Sim 1 and Sim 2 are the most effective of all the tested tactics (Sim 9 will
be discussed in Section 6.4). Our results are in accord with real-world observations. Bots finding success by targeting
vulnerable users bears some similarities to how “extremist” groups have historically targeted loners, marginalized
and ostracized groups, and other societal outcasts for recruitment/radicalization owing to these people’s greater
receptiveness towards extremist messaging [267, 268]. The tactic of maximizing audience reach is also favored by
extremist groups, as seen in the Islamic State (IS) “fighting for its propaganda to appear on search indexes and
continued to launch ‘media invasion raids’ to gain an even short-lived visibility on mainstream social media” due
to IS’s favored social media platform, Telegram, having “limited audience reach and echo-chamber effect, with the
IS message being shared mostly among like-minded individuals” [269]. Another example are BTC scam bots [230],
which are known to raid the replies sections of other tweets to maximize visibility.
6.4 Themes conservation and propagation
Themes are unique within our model in that agents do not guard against them unlike stances that have polarity,
but their transmission is entirely dependent on the successful adoption of polarizable stances. Themes can improve
36

the transmission probability of the stance that they are attached to if the targeted agent shares the same themes.
Themes can therefore be thought of as having a symbiotic relationship with stances.
We tested a naive tactic for improving the propagation of themes — saturation. By making all the bots conserve
a particular theme (Theme 7), we aim to see if themes can spread beyond the bots themselves and into the human
population. Conservation involves attaching the conserved theme(s) to every outgoing message from bots and also
giving the conserved theme(s) a permanent place in a bot’s set of themes. The results from Sim 9 show that not
only are bots capable of making half the population of the simulation be infected by Theme 7, they were able to
accomplish it without causing any appreciable change in the final distribution of the stances when compared to Sim
1, i.e., the bots still experienced similar success in stance propagation while conserving a theme. Because the number
of agents holding the conserved stance, Theme 7, exceeds the bot population and an agent cannot hold duplicates in
its theme set, we can conclude that the bots have succeeded in pushing the conserved theme onto human agents.
Even without an explicit theme conservation tactic, the bots’ greedy strategy of keeping half of their own themes
whenever they survey tweets for themes to adopt ensures that minority themes are given a boost whenever bots are
involved in a simulation (Sims 1–16, except the humans-only Sim 11). In cases where bots failed to propagate their
backed stances because the bots’ starting positions are in the periphery of the network (Sims 6 and 7), the bots are
still capable of elevating the presence of the initially obscure Theme 7. Bots can also suppress the growth of popular
themes or even cause their decline, which can be observed by tracking the counts for the first and second highest
frequency themes, Themes 3 and 2 across the simulations. The exceptions are when bots are exiled to the fringes,
as in Sims 6 and 7, when bot activity levels are low, as in Sims 8 and 10, or when bots are completely absent, as in
Sim 11, where a normative rich-gets-richer effect is at play where themes that were already popular mostly grew in
popularity as the simulation progresses.
Prior to obtaining our simulation results, our concern was that themes not matching fully will hamper stance
adoption and therefore theme adoption; theme compatibility is ct = |tuser ∩ ttweet|/|tuser ∪ ttweet|, so deliberately in-
cluding a theme that is virtually absent in the entire population would ensure that during the early phase of the
simulation, the denominator of the theme compatibility equation will almost always be increased by one even in cases
where all the non-conserved themes in a tweet matches with a user’s theme. However, as the results from Sim 9
demonstrate, this is not a factor, at least not when the number of themes to be conserved is just one. The outcome
might be different if more than one theme has to be conserved, as the reduced presence of compatible themes may
be insufficient to compensate for the incompatibility arising from multiple conserved themes.
We theorize that engagement metrics, a high volume of replies representing a stance, and other effects that are
within the ability of the bots in the simulation to manipulate are sufficient to overcome incompatibility in themes
during stance adoption. Once a critical mass of agents are infected with the conserved theme, a synergistic effect
begins to take hold. Human agents who have yet to be infected by the conserved theme find that their tweets are
less effective at changing the stances of those who are infected with the conserved theme. This enables the number
of agents with the conserved theme to grow without much interruption. These agents are also likely to share the
same stance(s) as the bots because the conserved theme is almost exclusively possessed by the bots at simulation
start, so acquiring that theme implies that the bots’ stance(s) has infected the agent, at least in the early phase
of the simulation. Once agents with the conserved theme become the majority, they can peer pressure others into
accepting their stance. A theme can be viewed as performing a function similar to “investments” (sunk costs) that
makes “betraying”/leaving “extremist” groups [270, 271], armed forces [272], religions [273], and currency standards
[274, 275] difficult.
Bots being able to push a single theme without sacrificing progress on stance conversion, as results from Sim 9
demonstrated, is a non-trivial finding. There are implications for actors intending to conduct separate info ops on
more than one issue. Such actors would ideally wish to succeed on all fronts without having to decide which info ops
are the most important ones while making trade-offs and compromises for the rest. Our results show that not only
can balancing acts be avoided, the actors can design an info ops in ways that can improve the outcomes of other
related info ops. We illustrate this with an example concerning the issue of mask-wearing.
Under the guise of facilitating debate between the supporting, neutral, and opposing factions of mask-wearing,
a motivated actor participating in more than one side of the debate via bots that always frame their messages with
a theme of liberty (personal/individual freedom versus communal responsibilities and interests) is ensuring that the
theme over time becomes the basis around which the issue is discussed as an increasing number of agents are infected
by the theme. This mindset caused by the theme-infection can potentially be carried over into other issues, e.g.,
seatbelts, drunk driving, and climate change, causing the infected agents to frame those issues in terms of liberty.
This is similar to the belief in the field of pedagogy that thinking habits can be taught and can be carried over across
different situations (e.g., critical thinking [276], thinking like an engineer [277], fostering creativity in children [278]),
exposing people who think in a certain way to cognitive blind spots [279] due to “belief bias and the magnitude
of framing effects” [280]. When others attempt to persuade these theme-infected agents to, for instance, not drink
and drive by presenting arguments framed only in authoritarian terms (e.g., driving under the influence is against
the law) or safety terms (e.g., drinking and driving often kills the driver), they would have difficulty dislodging the
37

agent’s stance.
6.5 Embedded vs. peripheral bots
Figures 5, 6, 7, and 8 are visual illustrations of the differences between bots starting out embedded naturally within
a network and bots starting out as outsiders with only one outgoing follower-followee link (i.e., the bots’ tweets that
are not replies will not be seen by anyone in the network). This challenging start is meant to mimic the “time zero
on the periphery” with “a single link to a random node” start for bot disinformation maneuvers in [81]. Two other
scenarios featuring bots in the periphery are Sims 6 and 7 in Table 1. Although only 100 agents are used for plotting
these graphs, the embedded scenario is representative of the 1,000 agent simulation results in Table 1 for Sim 13.
The isolated/fringe scenario with 100 agents has no equivalent in Table 1, but it can be considered a variant of Sim
6 where the stance ratio for bots is 1 : 0 : 0 instead of 1 : 1 : 0. The influence of bots is easier to see visually if the
bots all belonged to one stance, hence the chosen configurations.
Embedded bots (Sim 13 and Figures 5 and 6) succeeded in converting a majority of the network population to its
stance but the bots that started out in the network’s fringes (Sims 6 and 7, and Figures 7 and 8) could only convert
other users who also exist on the fringes. Cut off from the influence of negative bots existing on the periphery,
the positive human agents in the central clusters rapidly converted the few neutral and negative human agents into
positive agents (Figures 7 and 8, and Sims 6 and 7). Although bots did not actively initiate the severing of links
— they start the simulation already isolated from the central clusters — the peripheral bots scenarios serve as an
in situ demonstration of the effects of a community (central clusters) shielding itself from outside influence (bots).
The results from these simulations of ours are in accord with the model in [281] which produced predictions of social
influence (homophily in opinion) and unfollowing being drivers behind the emergence of echo chambers, consistent
with the empirical Twitter data they collected.
The fierceness of ideological competition is evident from comparing both halves of Figure 6, which represents the
embedded bots scenario. While a large share of outgoing messages were read by users in the network, as indicated by
the thick lines of the edges in the graph on the left, the messages that convinced another user to switch their stances
are a smaller proportion of those that have been read, indicated by the thinner influence lines connecting nodes on
the right. The same observation applies even more so to the peripheral bots scenario in Figure 8. Bot messages lack
the consistent persuasiveness of more centrally located humans, as the bots’ red influence lines are comparatively
thin next to the thick black influence lines emanating from humans. One shared trait of the winning sides in both
the embedded and fringe cases is that their tweets receive a lot of affirmation, i.e., likes received outnumbered the
replies, indicated by their greater node size in the right halves of Figure 5 (blue negative agents) and Figure 7 (green
positive agents).
Figure 9 shows that stance conversion happens early in both the embedded and fringe scenarios. While there
are occasional bouts of rapid stance switches, most agents tend to hold a consistent stance for long periods of time.
In the fringe scenario, there is a greater occurrence of positive agents converting to neutrality for short stretches of
time in the early phase of the simulation. We speculate that this is because of negative bots having numbers that
are sufficient to dampen positive tweets with their actions but are insufficient to boost negative tweets past the point
where their stance incompatibility with positive agents is minimal, leaving neutrality to benefit from the struggle 10.
The outcomes for Sim 6 and Sim 7 in Table 1 provide support for this observation in Figure 9. Despite the absolute
counts at simulation end dropping for both negative and neutral, neutral has a higher count relative to negative
despite starting with a comparatively lower count.
The peripheral bots’ tactic of targeting low-followee accounts for replying and quote-tweeting is unlikely to be
the cause of the bots’ failure in combating the majority stance, because replying and quote-tweeting retweeting is
limited to once each per tweet, so bots would switch to other targets once they have hit their interaction quota with
10An example with a positive agent undergoing stance conversion after having read a tweet each from negative, neutral, and
positive stances: Recall that a stance’s conversion score wr is made up of two components, engagement rg and compatibility
rc, wr = m−1rg + mrc. The m−1 and m terms are weights used to de-emphasize engagement and emphasize compatibility,
respectively. Let themes be ignored in the compatibility calculation and assume that the two components will not be weighted
when summed. Assume that in the absence of bot-backing, the three tweets receive zero engagement. Assume that in the
presence of bot-backing for the negative stance, the backing involves only actions that impact the engagement component of
the conversion weight — the positive tweet receiving one reply (assume that the reply was not seen by the agent experiencing
this conversion event). For the non-bot backed case, rg-con = rg-neu = rg-pro = 0 and rc-con = 0, rc-neu = 0.33, rc-pro = 0.66.
For the bot-backed case, rc remains the same but rg-pos = −0.5 due to receiving a reply. Engagement components for negative
and neutral remain the same, rg-con = rg-neu = 0, because they received no engagement. The conversion weights without
bot-backing are wr-neg = 0, wr-neu = 0.5, wr-pro = 1 and with bot-backing, they are wr-neg = 0, wr-neu = 0.5, wr-pro = 0.16.
In percentages, the chances of a stance being selected, from negative to neutral to positive, are 0%, 33%, and 66% for the case
without bot-backing, and are 0%, 76%, and 24% with bot-backing. By “attacking” positive tweets, the bots’ actions ended up
making neutrality a more attractive option. In the actual simulations, the m−1 and m weights are meant to ensure that the
influence from engagement metrics does not easily overpower homophily for stance and themes.
38

agents on the fringes. For liking and retweeting, bots target tweets with high engagement written by agents with high
follower counts. Incidentally, bots frequently liking other tweets to boost their infectivity appears to be a slightly
inferior tactic compared to frequently replying to messages (Sim 6 vs. Sim 7). This difference between the Liker and
Replier bots are less pronounced compared to the embedded scenarios (Sim 1 vs. Sim 4).
The difficulty faced by bots under the fringe scenario in overturning the predominant stance can perhaps be
attributed to the follow and unfollow mechanism in Diluvsion. The probability for an agent to follow and unfollow
accounts are based on data of user behavior on social media (Section 3.8.1) that likely was collected under “peacetime”,
i.e., when a community is not vigorously debating a topic. Therefore, they may not reflect a greater tendency to
cluster into echo chambers/hives during “wartime” by rapidly establishing social ties with like-minded users and
severing ties with non-believers. However, as we aim to ground our model in as much empirical data as possible and
we did not encounter data of heightened follow/unfollow behavior on “war footing”, we opted to keep probabilities
low. The model in [81], twitter sim, strongly incentivizes the creation of new links, which explains the difference
between their simulation results and ours, where they demonstrated that bots are successful in backing a stance and in
bridging two separate communities despite bots starting in the fringes. Under twitter sim, link creation probability
for humans is low at 5% but is higher than our model’s 0 .6%, the check for link creation is triggered every time a
user wakes instead of being a separate event that consumes a user’s action budget under our model (compounding
the higher link creation probability), and links in twitter sim are never broken.
Figure 4 shows the crippling effect of being deprived of an audience. Unlike other scenarios where the minority
stances’ mean follower and followee counts are at parity with the majority stance’s at simulation start, they are
only about three-fourths of the majority’s in Sims 6 and 7. Once agents begin renouncing a minority stance for the
majority stance, the minority stance’s follower and followee counts begin experiencing a precipitous decline that they
never recover from.
Our results here are corroborated by the details of real info ops on social media that have emerged (Section 2.2.6),
showing that great effort is invested in equipping many bots with extensive social ties, going as far as having real
humans work under a bot. No matter how persuasive a bot is constructed to be, its effect is limited if it does not have
a ready audience that is always exposed to the messages that the bot broadcasts. Bombarding the replies section
of other users to persuade them and their neighbors into changing their stances cannot succeed if the bots are just
10% of the population, as our simulations have shown. Resorting to other tactics to improve the performance of bots
without increasing the number of bots, e.g., explicitly coordinating with other bots and increasing the frequency of
activity, runs the risk of the info ops being discovered.
7 Limitations and future work
At the outset of this paper, we have stated that no model is perfect and that they are all reflections of some aspect
of real life that the modelers wish to bring to attention. There is room for future work because we made several
simplifying assumptions in our model. For instance, we accounted for the bandwagon effect but did not implement
a mechanism for the spiral of silence. Our simulations start out with one dominant and two minority stances, which
do not cover scenarios where the distributions are balanced. Some other assumptions involved picking one side of an
ongoing debate (e.g., whether resistance increases with repeat infections) and not having the opportunity to explore
the alternative side in-depth in this paper.
One promising route for future investigation is to allow a reinforcement agent to control the bots. The reinforce-
ment learning agent AlphaStar has been demonstrated to perform at the Grandmaster level for the real-time strategy
(RTS) game StarCraft II [282]; an info ops problem bears strong resemblance to an RTS game. Just as playing an RTS
game involves controlling groups of hundreds of units with specific roles (attackers, defenders, healers, etc.), so too can
the managing of an info ops on social media involve controlling hundreds of bots with specific roles (Repliers, Likers,
etc.). However, a central controller dictating the actions of multiple bots does violate the emergent/uncoordinated
coordination condition that this paper is predicated upon and could potentially make this proposed form of bot-driven
info ops easier to detect, so an alternative scenario where there are multiple reinforcement agents that each control
one bot should also be explored.
Greater heterogeneity in terms of bots should also be investigated. While we have varied the distribution of roles
and activity levels, we have kept other aspects homogeneous throughout a simulation run, such as the process by which
a bot chooses a tweet to like. And when deciding how bots should act, e.g., the per-week frequency of actions such as
retweeting, we have relied on pre-defined roles derived from empirical observations of Twitter user behavior. All this
was done to facilitate comparison between scenarios. There may be more optimal action distributions for maximizing
stance propagation. Heterogeneity would also enable us to explore more complicated info ops scenarios. An example
would be explicit cooperation between neutral and opposition bots, where neutral bots would only target agents who
are supporters for conversion to neutrality while opposition bots would target both neutral and supporter agents. In
this example, opposition bots would effectively function as a conversion pipeline for opposition bots. Compared to
39

opposition bots attempting to convert supporters into detractors, the lesser difference in stance between supporters
and neutrals means that neutral bots would have an easier time converting supporters to neutrality. Once converted
to neutrality, opposition bots can more easily convert the former supporters into agents of the opposition.
Agent heterogeneity should include class and role transitions, e.g., deepening radicalization turning human agents
into bots and de-radicalization turning bots to humans. Bots switching roles as the info ops situation demands
should also be included. Role transition in an ABM for information diffusion has been explored before in [74] where
radicalized patients become staunch anti-vaccine propagandists. Our model’s radicalization and de-radicalization
involved only an agent switching stances. In addition, human and bot users entering and exiting the network should
be accounted for. The dynamics of a social network in which the ratio between bots and humans is ever shifting may
provide additional info ops insights.
8 Conclusion
In this paper, we developed and empirically validated an agent-based information diffusion model for bot-driven
information operations on social media, Diluvsion, that incorporated crucial but oft-neglected real-world aspects of
diffusion. Chief among them is indirect influence, consisting of two forms, the exposure to a message’s engagement
metrics inducing bandwagon/conformity effects within a user and the ability to transmit information to another node
in the absence of a social tie linking two nodes together. Other key innovations of the model are the designation of
neutrality as an independent infection-capable stance instead of a transition point between the two discrete polar
stances (opinions) and the introduction of the non-polarizable, homophily-inducing, infection-capable, and stance-
symbiotic themes as a counterpart to stances.
Through simulations, we demonstrated the different routes by which motivated agents, i.e., bots, can exploit
these aspects of information diffusion to manipulate the information environment. The simulations showed that
highly active Replier bots representing minority stances are capable of overturning the dominance of a non-bot-
backed majority stance, and that a naive saturation tactic can not only keep a minority theme, e.g., “conspiracy”,
alive but also further its adoption over time without compromising stance propagation. Neutrality is also shown to be
non-neutral in its threat to the continued dominance of the majority stance. Overall, our model shows that info ops
originating from agents embedded in the network who are not counterbalanced by a similarly motivated oppositional
force can easily pollute the information environment and induce different outcomes, such as increased polarization.
Although much of our paper has been steeped in the language of war, the model we introduced here can be
used towards beneficial, pacific ends. Reducing polarization on social media through the introduction of bots that
stubbornly advocate a neutral stance, for instance, can be studied through Diluvsion, in the tradition of the numerous
works that have been published on depolarization, e.g., [283, 284, 285, 286]. The assumption here is that polarization
reduction is prosocial, an assumption that some may not agree with as they may believe that there is no peaceful
coexistence with certain opinions or ideas, e.g., Nazism. On the other hand, there are real-life examples — the US, for
one — of comfortable coexistence being possible between “extreme” ideologies and the ideals of liberal democracy, the
best governing system ever and which Churchill, the widely venerated British prime minister who presided over the
Bengal famine [287, 288, 289], wryly described as “the worst form of Government except for all those other forms that
have been tried from time to time”. The US never lost its global status (global as in encompassing only the “garden”
[101]) as the shining beacon of democracy despite being the direct progenitor of Nazism via cherished American ideals
such as Manifest Destiny [290, 291] and despite fascism resurging in modern-day America [292, 293, 294, 295].
Or, perhaps, certain states, systems, ideas, etc., maintaining an untarnished reputation as a force for good are not
due to their inherent merits but due to having waged successful info ops campaigns, and maintaining that reputation
in the age of social media requires active effort in maintaining an edge in tools for wargaming info ops on social
media, in tools such as Diluvsion.
9 Acknowledgments
This research is supported by NSERC Discovery Grants (RGPIN-2018-03872), NSERC CREATE Grants (CREATE-
554764-2021) and Canada Research Chairs Program (CRC-2019-00041).
References
[1] Laura Courchesne, Julia Ilhardt, and Jacob N. Shapiro. Review of social science research on the im-
pact of countermeasures against influence operations. Harvard Kennedy School Misinformation Review ,
September 2021. doi: 10.37016/mr-2020-79. URL https://misinforeview.hks.harvard.edu/article/
review-of-social-science-research-on-the-impact-of-countermeasures-against-influence-operations/ .
40

[2] Vindu Goel. Facebook Tinkers With Users’ Emotions in News Feed Experiment, Stirri. . . .
New York Times , September 2014. URL http://www.nytimes.com/2014/06/30/technology/
facebook-tinkers-with-users-emotions-in-news-feed-experiment-stirring-outcry.html?_r=0 .
[3] Hannes Grassegger. Facebook says its ‘voter button’ is good for turnout. But
should the tech giant be nudging us at all? The Guardian , April 2018.
ISSN 0029-7712. URL https://www.theguardian.com/technology/2018/apr/15/
facebook-says-it-voter-button-is-good-for-turn-but-should-the-tech-giant-be-nudging-us-at-all .
[4] Yuchen Li, Dongxiang Zhang, and Kian-Lee Tan. Real-time Targeted Influence Maximization for Online
Advertisements. Proc. VLDB Endow. , 8(10):1070–1081, June 2015. ISSN 2150-8097. doi: 10.14778/2794367.
2794376. URL https://doi.org/10.14778/2794367.2794376.
[5] H. T. Nguyen, T. N. Dinh, and M. T. Thai ±. Cost-aware Targeted Viral Marketing in billion-scale networks.
In IEEE INFOCOM 2016 - The 35th Annual IEEE International Conference on Computer Communications ,
pages 1–9, April 2016. doi: 10.1109/INFOCOM.2016.7524377.
[6] Ziv Epstein, Hause Lin, Gordon Pennycook, and David Rand. How many others have shared this? Experi-
mentally investigating the effects of social cues on engagement, misinformation, and unpredictability on social
media, July 2022. URL http://arxiv.org/abs/2207.07562.
[7] Ben Kiernan. The First Genocide: Carthage, 146 BC. Diogenes, 51(3):27–39, August 2004. ISSN
0392-1921, 1467-7695. doi: 10.1177/0392192104043648. URL http://journals.sagepub.com/doi/10.1177/
0392192104043648.
[8] Aumyo Hassan and Sarah J. Barber. The effects of repetition frequency on the illusory truth effect. Cognitive
Research: Principles and Implications , 6(1):38, May 2021. ISSN 2365-7464. doi: 10.1186/s41235-021-00301-5.
URL https://doi.org/10.1186/s41235-021-00301-5 .
[9] Lisa K. Fazio, Nadia M. Brashier, B. Keith Payne, and Elizabeth J. Marsh. Knowledge does not protect
against illusory truth. Journal of Experimental Psychology: General , 144:993–1002, 2015. ISSN 1939-2222. doi:
10.1037/xge0000098.
[10] Florian Zollmann. Bringing Propaganda Back into News Media Studies. Critical Sociology, 45(3):329–345, May
2019. ISSN 0896-9205, 1569-1632. doi: 10.1177/0896920517731134. URL http://journals.sagepub.com/doi/
10.1177/0896920517731134.
[11] Alan MacLeod. Manufacturing Consent in Venezuela: Media Misreporting of a Country, 1998–2014 - Alan
MacLeod, 2020. Critical Sociology, December 2018. URL https://journals-sagepub-com.proxy3.library.
mcgill.ca/doi/10.1177/0896920518820934.
[12] Christian Fuchs. Propaganda 2.0: Herman and Chomsky’s Propaganda Model in the Age of the Internet, Big
Data and Social Media in the Age of the Internet, Big Data and Social Media , pages 71–92. University of
Westminster Press, October 2018. ISBN 978-1-912656-16-5. doi: 10.16997/book27.f. URL https://www.
uwestminsterpress.co.uk/site/chapters/10.16997/book27.f/.
[13] Andrew Mullen and Jeffery Klaehn. The Herman–Chomsky Propaganda Model: A Critical Approach
to Analysing Mass Media Behaviour. Sociology Compass , 4(4):215–229, 2010. ISSN 1751-9020. doi:
10.1111/j.1751-9020.2010.00275.x. URL https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1751-9020.
2010.00275.x.
[14] Edward S. Herman and Noam Chomsky. Manufacturing Consent: The Political Economy of the Mass Media .
Random House, 2010.
[15] Edward S. Herman. The Propaganda Model: A retrospective. Journalism Studies, 1(1):101–112, January 2000.
ISSN 1461-670X, 1469-9699. doi: 10.1080/146167000361195. URL http://www.tandfonline.com/doi/abs/
10.1080/146167000361195.
[16] Michael 1933 Parenti. Inventing Reality : The Politics of News Media . St. Martin’s Press, New York, 2nd ed.
edition, 1993. ISBN 0-312-02013-9 978-0-312-02013-2 0-312-08629-6 978-0-312-08629-9.
[17] Adrien Guille, Hakim Hacid, Cecile Favre, and Djamel A. Zighed. Information Diffusion in Online Social
Networks: A Survey. SIGMOD Rec., 42(2):17–28, July 2013. ISSN 0163-5808. doi: 10.1145/2503792.2503797.
URL http://doi.acm.org/10.1145/2503792.2503797.
41

[18] Mehdi Azaouzi, Wassim Mnasri, and Lotfi Ben Romdhane. New trends in influence maximization models.
Computer Science Review , 40:100393, May 2021. ISSN 1574-0137. doi: 10.1016/j.cosrev.2021.100393. URL
https://www.sciencedirect.com/science/article/pii/S1574013721000332.
[19] Yun Liu, Su-Meng Diao, Yi-Xiang Zhu, and Qing Liu. SHIR competitive information diffusion model for
online social media. Physica A: Statistical Mechanics and its Applications , 461:543–553, November 2016. ISSN
0378-4371. doi: 10.1016/j.physa.2016.06.080. URL http://www.sciencedirect.com/science/article/pii/
S037843711630348X.
[20] Jan Kostka, Yvonne Anne Oswald, and Roger Wattenhofer. Word of Mouth: Rumor Dissemination in Social
Networks. In Alexander A. Shvartsman and Pascal Felber, editors, Structural Information and Communication
Complexity, Lecture Notes in Computer Science, pages 185–196, Berlin, Heidelberg, 2008. Springer. ISBN
978-3-540-69355-0. doi: 10.1007/978-3-540-69355-0 16.
[21] Walter Quattrociocchi, Guido Caldarelli, and Antonio Scala. Opinion dynamics on interacting networks: Media
competition and social influence. Scientific Reports, 4:4938, May 2014. ISSN 2045-2322. doi: 10.1038/srep04938.
URL http://www.nature.com/articles/srep04938.
[22] L. Weng, A. Flammini, A. Vespignani, and F. Menczer. Competition among memes in a world with limited
attention. Scientific Reports , 2:335, March 2012. ISSN 2045-2322. doi: 10.1038/srep00335. URL http:
//www.nature.com/articles/srep00335.
[23] Jos´ e R.C. Piqueira, Mauro Zilbovicius, and Cristiane M. Batistela. Daley–Kendal models in fake-news scenario.
Physica A: Statistical Mechanics and its Applications , 548:123406, June 2020. ISSN 03784371. doi: 10.1016/j.
physa.2019.123406. URL https://linkinghub.elsevier.com/retrieve/pii/S0378437119319028.
[24] Soroush Vosoughi, Deb Roy, and Sinan Aral. The spread of true and false news online. Science, 359(6380):
1146–1151, March 2018. ISSN 0036-8075, 1095-9203. doi: 10.1126/science.aap9559. URL https://science.
sciencemag.org/content/359/6380/1146.
[25] Zilong Zhao, Jichang Zhao, Yukie Sano, Orr Levy, Hideki Takayasu, Misako Takayasu, Daqing Li, Junjie
Wu, and Shlomo Havlin. Fake news propagates differently from real news even at early stages of spreading.
EPJ Data Science , 9(1):7, December 2020. ISSN 2193-1127. doi: 10.1140/epjds/s13688-020-00224-z. URL
https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-020-00224-z .
[26] Petter Holme. Rare and everywhere: Perspectives on scale-free networks. Nature Communications, 10(1):1016,
March 2019. ISSN 2041-1723. doi: 10.1038/s41467-019-09038-8. URL https://www.nature.com/articles/
s41467-019-09038-8 .
[27] W. O. Kermack and A. G. McKendrick. A Contribution to the Mathematical Theory of Epidemics. Proceedings
of the Royal Society of London. Series A, Containing Papers of a Mathematical and Physical Character , 115
(772):700–721, 1927. ISSN 0950-1207. URL http://www.jstor.org/stable/94815.
[28] William Ogilvy Kermack, A. G. McKendrick, and Gilbert Thomas Walker. Contributions to the mathematical
theory of epidemics. II. —The problem of endemicity. Proceedings of the Royal Society of London. Series A,
Containing Papers of a Mathematical and Physical Character , 138(834):55–83, October 1932. doi: 10.1098/
rspa.1932.0171. URL https://royalsocietypublishing.org/doi/abs/10.1098/rspa.1932.0171.
[29] Jacob Goldenberg, Barak Libai, and Eitan Muller. Talk of the Network: A Complex Systems Look at the
Underlying Process of Word-of-Mouth. Marketing Letters, 12(3):211–223, August 2001. ISSN 1573-059X. doi:
10.1023/A:1011122126881. URL https://doi.org/10.1023/A:1011122126881.
[30] Mark Granovetter. Threshold Models of Collective Behavior. American Journal of Sociology, 83(6):1420–1443,
1978. ISSN 0002-9602. URL https://www.jstor.org/stable/2778111.
[31] D. J. Daley and D. G. Kendall. Epidemics and Rumours. Nature, 204(4963):1118–1118, December 1964. ISSN
1476-4687. doi: 10.1038/2041118a0. URL https://www.nature.com/articles/2041118a0.
[32] Daniel P. Maki and Maynard Thompson. Mathematical Models and Applications : With Emphasis on the
Social, Life, and Management Sciences . Prentice-Hall, Englewood Cliffs, N.J., 1973. ISBN 0-13-561670-0
978-0-13-561670-3. URL http://www.gbv.de/dms/hbz/toc/ht004611076.PDF.
42

[33] Herbert W. Hethcote. The Mathematics of Infectious Diseases. SIAM Review , 42(4):599–653, January
2000. ISSN 0036-1445. doi: 10.1137/S0036144500371907. URL https://epubs.siam.org/doi/abs/10.1137/
s0036144500371907.
[34] M. E. J. Newman. The Structure and Function of Complex Networks. SIAM Review, 45(2):167–256, January
2003. ISSN 0036-1445. doi: 10.1137/S003614450342480. URL https://epubs.siam.org/doi/abs/10.1137/
s003614450342480.
[35] Albin Shaji, R. V. Belfin, and E. Grace Mary Kanaga. An Innovated SIRS Model for Information Spreading.
In Elijah Blessing Rajsingh, Jey Veerasamy, Amir H. Alavi, and J. Dinesh Peter, editors, Advances in Big
Data and Cloud Computing , Advances in Intelligent Systems and Computing, pages 405–413, Singapore, 2018.
Springer. ISBN 978-981-10-7200-0. doi: 10.1007/978-981-10-7200-0 37.
[36] Laijun Zhao, Jiajia Wang, Yucheng Chen, Qin Wang, Jingjing Cheng, and Hongxin Cui. SIHR rumor spreading
model in social networks. Physica A: Statistical Mechanics and its Applications , 391(7):2444–2453, April 2012.
ISSN 0378-4371. doi: 10.1016/j.physa.2011.12.008. URL https://www.sciencedirect.com/science/article/
pii/S0378437111009058.
[37] Michael Muhlmeyer, Shaurya Agarwal, and Archie J. Huang. Modeling Social Contagion and Information
Diffusion in Complex Socio-Technical Systems. IEEE Systems Journal , 14(4):5187–5198, December 2020. ISSN
1937-9234. doi: 10.1109/JSYST.2020.2993542.
[38] Cho Ryok Kang and Sae Kyung Joo. Internet cafe and karaoke could be a hotbed for explosive spreading
of COVID-19 into community. Public Health Affairs , 4(1), December 2020. ISSN 2586-2901, 2586-5609. doi:
10.29339/pha.20.10. URL http://www.pha.or.kr/journal/view.php?number=74.
[39] Juliet R. C. Pulliam, Cari van Schalkwyk, Nevashan Govender, Anne von Gottberg, Cheryl Cohen, Michelle J.
Groome, Jonathan Dushoff, Koleka Mlisana, and Harry Moultrie. Increased risk of SARS-CoV-2 reinfection
associated with emergence of Omicron in South Africa. Science, 376(6593):eabn4947, March 2022. doi: 10.
1126/science.abn4947. URL https://www.science.org/doi/full/10.1126/science.abn4947.
[40] Wei Wang, Quan-Hui Liu, Junhao Liang, Yanqing Hu, and Tao Zhou. Coevolution spreading in complex
networks. Physics Reports , July 2019. ISSN 0370-1573. doi: 10.1016/j.physrep.2019.07.001. URL http:
//www.sciencedirect.com/science/article/pii/S0370157319302583.
[41] Abhimanyu Das, Sreenivas Gollapudi, and Kamesh Munagala. Modeling opinion dynamics in social networks.
In Proceedings of the 7th ACM International Conference on Web Search and Data Mining , WSDM ’14, pages
403–412, New York, NY, USA, February 2014. Association for Computing Machinery. ISBN 978-1-4503-2351-2.
doi: 10.1145/2556195.2559896. URL https://doi.org/10.1145/2556195.2559896.
[42] John R. P. French Jr. A formal theory of social power. Psychological Review, 63:181–194, 1956. ISSN 1939-
1471(Electronic),0033-295X(Print). doi: 10.1037/h0046123.
[43] Morris H. DeGroot. Reaching a Consensus. Journal of the American Statistical Association , 69(345):118–121,
March 1974. ISSN 0162-1459. doi: 10.1080/01621459.1974.10480137. URL https://www.tandfonline.com/
doi/abs/10.1080/01621459.1974.10480137.
[44] Rainer Hegselmann and Ulrich Krause. Opinion dynamics and bounded confidence: Models, analysis and
simulation. Journal of Artificial Societies and Social Simulation , 5(3), 2002.
[45] Carlos Andres Devia and Giulia Giordano. A framework to analyze opinion formation models. Scientific
Reports, 12(1):13441, August 2022. ISSN 2045-2322. doi: 10.1038/s41598-022-17348-z. URL https://www.
nature.com/articles/s41598-022-17348-z .
[46] Peter Clifford and Aidan Sudbury. A Model for Spatial Conflict. Biometrika, 60(3):581–588, 1973. ISSN
0006-3444. doi: 10.2307/2335008. URL https://www.jstor.org/stable/2335008.
[47] Richard A. Holley and Thomas M. Liggett. Ergodic Theorems for Weakly Interacting Infinite Systems and
the Voter Model. The Annals of Probability , 3(4):643–663, August 1975. ISSN 0091-1798, 2168-894X. doi:
10.1214/aop/1176996306. URL https://projecteuclid.org/journals/annals-of-probability/volume-3/
issue-4/Ergodic-Theorems-for-Weakly-Interacting-Infinite-Systems-and-the-Voter/10.1214/aop/
1176996306.full.
43

[48] Robert Axelrod. The Dissemination of Culture: A Model with Local Convergence and Global Polarization.
Journal of Conflict Resolution, 41(2):203–226, April 1997. ISSN 0022-0027. doi: 10.1177/0022002797041002001.
URL https://doi.org/10.1177/0022002797041002001.
[49] P. Chen and S. Redner. Majority rule dynamics in finite dimensions. Physical Review E , 71(3):036101, March
2005. doi: 10.1103/PhysRevE.71.036101. URL https://link.aps.org/doi/10.1103/PhysRevE.71.036101.
[50] Feng Fu and Long Wang. Coevolutionary dynamics of opinions and networks: From diversity to uniformity.
Physical Review E, 78(1):016104, July 2008. doi: 10.1103/PhysRevE.78.016104. URL https://link.aps.org/
doi/10.1103/PhysRevE.78.016104.
[51] Daiki Takeuchi, Gouhei Tanaka, Ryo Fujie, and Hideyuki Suzuki. Public opinion formation with the spiral of
silence on complex social networks. Nonlinear Theory and Its Applications, IEICE, 6(1):15–25, 2015. ISSN 2185-
4106. doi: 10.1587/nolta.6.15. URL https://www.jstage.jst.go.jp/article/nolta/6/1/6_15/_article.
[52] Bj¨ orn Ross, Laura Pilz, Benjamin Cabrera, Florian Brachten, German Neubaum, and Stefan Stieglitz. Are
social bots a real threat? An agent-based model of the spiral of silence to analyse the impact of manipulative
actors in social networks. European Journal of Information Systems , 28(4):394–412, July 2019. ISSN 0960-
085X, 1476-9344. doi: 10.1080/0960085X.2018.1560920. URL https://www.tandfonline.com/doi/full/10.
1080/0960085X.2018.1560920.
[53] Elisabeth Noelle-Neumann. The Spiral of Silence A Theory of Public Opinion. Journal of Communication ,
24(2):43–51, 1974. ISSN 1460-2466. doi: 10.1111/j.1460-2466.1974.tb00367.x. URL https://onlinelibrary.
wiley.com/doi/abs/10.1111/j.1460-2466.1974.tb00367.x.
[54] B. Aditya Prakash, Alex Beutel, Roni Rosenfeld, and Christos Faloutsos. Winner takes all: Competing viruses
or ideas on fair-play networks. In Proceedings of the 21st International Conference on World Wide Web , pages
1037–1046, Lyon France, April 2012. ACM. ISBN 978-1-4503-1229-5. doi: 10.1145/2187836.2187975. URL
https://dl.acm.org/doi/10.1145/2187836.2187975.
[55] Tim Carnes, Chandrashekhar Nagarajan, Stefan M. Wild, and Anke van Zuylen. Maximizing influence in a
competitive social network: A follower’s perspective. In Proceedings of the Ninth International Conference on
Electronic Commerce, ICEC ’07, pages 351–360, New York, NY, USA, August 2007. Association for Computing
Machinery. ISBN 978-1-59593-700-1. doi: 10.1145/1282100.1282167. URL https://dl.acm.org/doi/10.1145/
1282100.1282167.
[56] Shishir Bharathi, David Kempe, and Mahyar Salek. Competitive Influence Maximization in Social Net-
works. In Xiaotie Deng and Fan Chung Graham, editors, Internet and Network Economics , Lecture Notes
in Computer Science, pages 306–311, Berlin, Heidelberg, 2007. Springer. ISBN 978-3-540-77105-0. doi:
10.1007/978-3-540-77105-0 31.
[57] Allan Borodin, Yuval Filmus, and Joel Oren. Threshold Models for Competitive Influence in Social Networks.
In Amin Saberi, editor, Internet and Network Economics , Lecture Notes in Computer Science, pages 539–550,
Berlin, Heidelberg, 2010. Springer. ISBN 978-3-642-17572-5. doi: 10.1007/978-3-642-17572-5 48.
[58] A. Srivastava, C. Chelmis, and V. K. Prasanna. Social influence computation and maximization in signed net-
works with competing cascades. In 2015 IEEE/ACM International Conference on Advances in Social Networks
Analysis and Mining (ASONAM) , pages 41–48, August 2015. doi: 10.1145/2808797.2809304.
[59] Sinan Aral and Paramveer S. Dhillon. Social influence maximization under empirical influence models. Nature
Human Behaviour , 2(6):375–382, June 2018. ISSN 2397-3374. doi: 10.1038/s41562-018-0346-z. URL http:
//www.nature.com/articles/s41562-018-0346-z .
[60] Jean Claude Ameisen and Andre Capron. Cell dysfunction and depletion in AIDS: The programmed cell
death hypothesis. Immunology Today, 12(4):102–105, April 1991. ISSN 0167-5699. doi: 10.1016/0167-5699(91)
90092-8. URL https://www.sciencedirect.com/science/article/pii/0167569991900928.
[61] Aur´ elie Wiedemann, Emile Foucat, Hakim Hocini, C´ ecile Lefebvre, Boris P. Hejblum, M´ elany Durand, Miriam
Kr¨ uger, Alpha Kabinet Keita, Ahidjo Ayouba, St´ ephane M´ ely, Jos´ e-Carlos Fernandez, Abdoulaye Tour´ e, Slim
Fourati, Claire L´ evy-Marchal, Herv´ e Raoul, Eric Delaporte, Lamine Koivogui, Rodolphe Thi´ ebaut, Christine
Lacabaratz, and Yves L´ evy. Long-lasting severe immune dysfunction in Ebola virus disease survivors. Nature
Communications, 11(1):3730, July 2020. ISSN 2041-1723. doi: 10.1038/s41467-020-17489-7. URL https:
//www.nature.com/articles/s41467-020-17489-7 .
44

[62] Chansavath Phetsouphanh, David R. Darley, Daniel B. Wilson, Annett Howe, C. Mee Ling Munier, Sheila K.
Patel, Jennifer A. Juno, Louise M. Burrell, Stephen J. Kent, Gregory J. Dore, Anthony D. Kelleher, and Gail V.
Matthews. Immunological dysfunction persists for 8 months following initial mild-to-moderate SARS-CoV-2 in-
fection. Nature Immunology, 23(2):210–216, February 2022. ISSN 1529-2916. doi: 10.1038/s41590-021-01113-x.
URL https://www.nature.com/articles/s41590-021-01113-x .
[63] S. A. Myers and J. Leskovec. Clash of the Contagions: Cooperation and Competition in Information Diffusion.
In 2012 IEEE 12th International Conference on Data Mining , pages 539–548, December 2012. doi: 10.1109/
ICDM.2012.159.
[64] Ho-Chun Herbert Chang and Feng Fu. Co-diffusion of social contagions. New Journal of Physics , 20(9):
095001, September 2018. ISSN 1367-2630. doi: 10.1088/1367-2630/aadce7. URL https://iopscience.iop.
org/article/10.1088/1367-2630/aadce7.
[65] Hegui Zhang, Xiaolong Chen, Yi Peng, Gang Kou, and Ruijie Wang. The interaction of multiple information
on multiplex social networks. Information Sciences, 605:366–380, August 2022. ISSN 00200255. doi: 10.1016/
j.ins.2022.05.036. URL https://linkinghub.elsevier.com/retrieve/pii/S002002552200456X.
[66] Christian Adler, Stephan Eichler, Timo Kosch, Christoph Schroth, and Markus Strassberger. Self-organized and
Context-Adaptive Information Diffusion in Vehicular Ad Hoc Networks. In 2006 3rd International Symposium
on Wireless Communication Systems , pages 307–311, September 2006. doi: 10.1109/ISWCS.2006.4362309.
[67] David Salda˜ na, Amanda Prorok, Shreyas Sundaram, Mario F. M. Campos, and Vijay Kumar. Resilient consen-
sus for time-varying networks of dynamic agents. In 2017 American Control Conference (ACC), pages 252–258,
May 2017. doi: 10.23919/ACC.2017.7962962.
[68] Ross Arnold, Kevin Carey, Benjamin Abruzzo, and Christopher Korpela. What is A Robot Swarm: A Definition
for Swarming Robotics. In 2019 IEEE 10th Annual Ubiquitous Computing, Electronics & Mobile Communication
Conference (UEMCON), pages 0074–0081, October 2019. doi: 10.1109/UEMCON47517.2019.8993024.
[69] Xiaohan Wang, Fakui Wang, Zisen Nie, Yuhui Ai, and Tianjiang Hu. optiSwarm: Optical Swarm Robots
Using Implicit Cooperation. IEEE Sensors Journal , 22(24):24380–24394, December 2022. ISSN 1558-1748. doi:
10.1109/JSEN.2022.3216445.
[70] Monica Anderson and Nikolaos Papanikolopoulos. Implicit Cooperation Strategies for Multi-robot Search of
Unknown Areas. Journal of Intelligent and Robotic Systems , 53(4):381–397, December 2008. ISSN 0921-0296,
1573-0409. doi: 10.1007/s10846-008-9242-5. URL http://link.springer.com/10.1007/s10846-008-9242-5 .
[71] Aybike S ¸im¸ sek and Resul Kara. Using swarm intelligence algorithms to detect influential individuals for influ-
ence maximization in social networks. Expert Systems with Applications , 114:224–236, December 2018. ISSN
0957-4174. doi: 10.1016/j.eswa.2018.07.038. URL https://www.sciencedirect.com/science/article/pii/
S0957417418304561.
[72] Rodrigo Olivares, Francisco Mu˜ noz, and Fabi´ an Riquelme. A multi-objective linear threshold influence spread
model solved by swarm intelligence-based methods. Knowledge-Based Systems, 212:106623, January 2021. ISSN
0950-7051. doi: 10.1016/j.knosys.2020.106623. URL https://www.sciencedirect.com/science/article/pii/
S0950705120307528.
[73] Jun Wang, Shimin Cai, Wei Wang, and Tao Zhou. Link cooperation effect of cooperative epidemics on complex
networks. Applied Mathematics and Computation , 437:127537, January 2023. ISSN 00963003. doi: 10.1016/j.
amc.2022.127537. URL https://linkinghub.elsevier.com/retrieve/pii/S0096300322006117.
[74] Pawel Sobkowicz and Antoni Sobkowicz. Agent Based Model of Anti-Vaccination Movements: Simu-
lations and Comparison with Empirical Data. Vaccines, 9(8):809, July 2021. ISSN 2076-393X. doi:
10.3390/vaccines9080809. URL https://www.mdpi.com/2076-393X/9/8/809.
[75] Yichuan Jiang and J. C. Jiang. Diffusion in Social Networks: A Multiagent Perspective. IEEE Transactions
on Systems, Man, and Cybernetics: Systems , 45(2):198–213, February 2015. ISSN 2168-2232. doi: 10.1109/
TSMC.2014.2339198.
[76] Chaitanya Kaligotla, Enver Y¨ ucesan, and Stephen E. Chick. Diffusion of competing rumours on social media.
Journal of Simulation , 0(0):1–21, August 2020. ISSN 1747-7778. doi: 10.1080/17477778.2020.1785345. URL
https://doi.org/10.1080/17477778.2020.1785345.
45

[77] Agnieszka Onuchowska and Donald J Berndt. Using Agent-Based Modelling to Address Malicious Behavior on
Social Media. In ICIS 2019 Proceedings, Munich, 2019.
[78] Weihua Li, Quan Bai, Minjie Zhang, and Tung Doan Nguyen. Modelling Multiple Influences Diffusion in On-line
Social Networks. In Proceedings of the 17th International Conference on Autonomous Agents and MultiAgent
Systems, AAMAS ’18, pages 1053–1061, Richland, SC, 2018. International Foundation for Autonomous Agents
and Multiagent Systems. URL http://dl.acm.org/citation.cfm?id=3237383.3237854.
[79] Chao Wang, Zong Xuan Tan, Ye Ye, Lu Wang, Kang Hao Cheong, and Neng-gang Xie. A rumor spreading
model based on information entropy. Scientific Reports, 7(1):9615, August 2017. ISSN 2045-2322. doi: 10.
1038/s41598-017-09171-8. URL https://www.nature.com/articles/s41598-017-09171-8 .
[80] Weihua Li, Quan Bai, and Minjie Zhang. A Multi-agent System for Modelling Preference-Based Complex
Influence Diffusion in Social Networks. The Computer Journal , 62(3):430–447, March 2019. ISSN 0010-4620.
doi: 10.1093/comjnl/bxy078. URL http://academic.oup.com/comjnl/article/62/3/430/5067534.
[81] David M. Beskow and Kathleen M. Carley. Agent Based Simulation of Bot Disinformation Maneuvers in Twit-
ter. In 2019 Winter Simulation Conference (WSC) , pages 750–761, December 2019. doi: 10.1109/WSC40007.
2019.9004942.
[82] Keisuke Ikeda, Yoshiyuki Okada, Fujio Toriumi, Takeshi Sakaki, Kazuhiro Kazama, Itsuki Noda, Kosuke
Shinoda, Hirohiko Suwa, and Satoshi Kurihara. Multi-agent Information Diffusion Model for Twitter. In
2014 IEEE/WIC/ACM International Joint Conferences on Web Intelligence (WI) and Intelligent Agent
Technologies (IAT), pages 21–26, Warsaw, Poland, August 2014. IEEE. ISBN 978-1-4799-4143-8. doi:
10.1109/WI-IAT.2014.12. URL http://ieeexplore.ieee.org/document/6927521/.
[83] Haibo Hu. Competing opinion diffusion on social networks. Royal Society Open Science , 4(11), Novem-
ber 2017. ISSN 2054-5703. doi: 10.1098/rsos.171160. URL https://www.ncbi.nlm.nih.gov/pmc/articles/
PMC5717675/.
[84] Aldo Averza, Khaled Slhoub, and Siddhartha Bhattacharyya. Evaluating the Influence of Twitter Bots via
Agent-Based Social Simulation. IEEE Access, 10:129394–129407, 2022. ISSN 2169-3536. doi: 10.1109/ACCESS.
2022.3228258.
[85] Maira A de C Gatti, Ana Paula Appel, Cicero Nogueira dos Santos, Claudio Santos Pinhanez, Paulo Ro-
drigo Cavalin, and Samuel Barbosa Neto. A simulation-based approach to analyze the information diffusion
in Microblogging Online Social Network. In 2013 Winter Simulations Conference (WSC) , pages 1685–1696,
December 2013. doi: 10.1109/WSC.2013.6721550.
[86] Eric A. M. Luiijf. Information assurance and the information Society. In Urs E. Gattiker, Pia Pedersen, and
Karsten Petersen, editors, EICAR Best Paper Proceedings, 1999.
[87] Norman E. Emery, Robert S. Earl, and Raymond Buettner. Terrorist Use of Information Operations. Journal of
Information Warfare, 13(2):14, 2014. ISSN 14453312. URL https://www.proquest.com/docview/2164442205/
abstract/B4766C3DE2FE464FPQ/2.
[88] Duncan Hollis. The Influence of War; the War for Influence. Temple International & Comparative Law Journal,
32(1):31–46, 2018.
[89] Vian Bakir. Psychological Operations in Digital Political Campaigns: Assessing Cambridge Analytica’s
Psychographic Profiling and Targeting. Frontiers in Communication , 5, 2020. ISSN 2297-900X. URL
https://www.frontiersin.org/articles/10.3389/fcomm.2020.00067.
[90] Melissa-Ellen Dowling. Cyber information operations: Cambridge Analytica’s challenge to democratic legiti-
macy. Journal of Cyber Policy , 7(2):230–248, May 2022. ISSN 2373-8871. doi: 10.1080/23738871.2022.2081089.
URL https://doi.org/10.1080/23738871.2022.2081089.
[91] Richard Wilson. Cambridge Analytica, Facebook, and Influence Operations: A Case Study and Anticipatory
Ethical Analysis. In European Conference on Cyber Warfare and Security, pages 587–595,XX, Reading, United
Kingdom, July 2019. Academic Conferences International Limited. URLhttps://www.proquest.com/docview/
2261006731/abstract/7535B9A14F504BB7PQ/1.
46

[92] Roy Campbell, Jalal Al-Muhtadi, Prasad Naldurg, Geetanjali Sampemane, and M. Dennis Mickunas. Towards
Security and Privacy for Pervasive Computing. In Gerhard Goos, Juris Hartmanis, Jan van Leeuwen, Mitsuhiro
Okada, Benjamin C. Pierce, Andre Scedrov, Hideyuki Tokuda, and Akinori Yonezawa, editors,Software Security
— Theories and Systems , volume 2609, pages 1–15. Springer Berlin Heidelberg, Berlin, Heidelberg, 2003. ISBN
978-3-540-00708-1 978-3-540-36532-7. doi: 10.1007/3-540-36532-X 1. URL http://link.springer.com/10.
1007/3-540-36532-X_1 .
[93] Linda Herrera. Revolution in the Age of Social Media : The Egyptian Popular Insurrection and the Inter-
net. Verso, London, 2014. ISBN 978-1-78168-275-3 1-78168-275-5 978-1-78168-276-0 1-78168-276-3. URL
9781781682753.jpg.
[94] Asef Bayat. Revolution without Revolutionaries : Making Sense of the Arab Spring . Stanford Studies in Middle
Eastern and Islamic Societies and Cultures. Stanford University Press, Stanford, CA, 2020. ISBN 978-1-5036-
0307-3 1-5036-0307-5. doi: 10.1515/9781503603073. URL https://doi.org/10.1515/9781503603073.
[95] Linda Herrera. Youth and Citizenship in the Digital Age: A View from Egypt. Har-
vard Educational Review , 82(3):333–352, September 2012. ISSN 0017-8055, 1943-5045. doi: 10.
17763/haer.82.3.88267r117u710300. URL https://meridian.allenpress.com/her/article/82/3/333/32085/
Youth-and-Citizenship-in-the-Digital-Age-A-View .
[96] Mohamed Arafa and Crystal Armstrong. ”Facebook to Mobilize, Twitter to Coordinate Protests, and YouTube
to Tell the World”: New Media, Cyberactivism, and the Arab Spring. Journal of Global Initiatives: Policy,
Pedagogy, Perspective, 10(1), January 2016. ISSN 1930-3009. URL https://digitalcommons.kennesaw.edu/
jgi/vol10/iss1/6.
[97] Alex Burns and Ben Eltham. Twitter free Iran: An evaluation of Twitter’s role in public diplomacy and
information operations in Iran’s 2009 election crisis. In Record of the Communications Policy and Research
Forum 2009, Sydney, Australia, November 2009.
[98] Stephen White and Ian McAllister. Did Russia (Nearly) have a Facebook Revolution in 2011? Social Media’s
Challenge to Authoritarianism. Politics, 34(1):72–84, February 2014. ISSN 0263-3957, 1467-9256. doi: 10.
1111/1467-9256.12037. URL http://journals.sagepub.com/doi/10.1111/1467-9256.12037.
[99] Desmond Butler, Jack Gillum, and Alberto Arce. US secretly built ’Cuban Twit-
ter’ to stir unrest. Associated Press , April 2014. URL https://apnews.com/article/
technology-cuba-united-states-government-904a9a6a1bcd46cebfc14bea2ee30fdf .
[100] AP. US secretly created ’Cuban Twitter’ to stir unrest and undermine government. The
Guardian, April 2014. ISSN 0261-3077. URL https://www.theguardian.com/world/2014/apr/03/
us-cuban-twitter-zunzuneo-stir-unrest .
[101] Roshni Majumdar. EU top diplomat denies ’jungle’ remark was racist. Deutsche Welle , October 2022. URL
https://www.dw.com/en/eu-top-diplomat-denies-jungle-remark-was-racist/a-63484246 .
[102] AJ. Russia used all major social media platforms to aid Trump: Report.
Al Jazeera , December 2018. URL https://www.aljazeera.com/news/2018/12/17/
russia-used-all-major-social-media-platforms-to-aid-trump-report .
[103] AJ. Amazon to suspend Parler after deadly Capitol Hill riot. Al Jazeera, January 2021. URL https://www.
aljazeera.com/news/2021/1/10/amazon-to-suspend-parler-after-deadly-capitol-hill-riot .
[104] Kathleen M. Carley. Social cybersecurity: An emerging science. Computational and Mathematical Organization
Theory, 26(4):365–381, December 2020. ISSN 1572-9346. doi: 10.1007/s10588-020-09322-9. URL https:
//doi.org/10.1007/s10588-020-09322-9 .
[105] Ma ´ ıra Gatti, Paulo Cavalin, Samuel Barbosa Neto, Claudio Pinhanez, C ´ ıcero dos Santos, Daniel Gribel, and
Ana Paula Appel. Large-Scale Multi-agent-Based Modeling and Simulation of Microblogging-Based Online
Social Network. In Shah Jamal Alam and H. Van Dyke Parunak, editors, Multi-Agent-Based Simulation XIV ,
Lecture Notes in Computer Science, pages 17–33, Berlin, Heidelberg, 2014. Springer. ISBN 978-3-642-54783-6.
doi: 10.1007/978-3-642-54783-6 2.
47

[106] Galen Stocking, Amy Mitchell, Katerina Eva Matsa, Regina Widjaya, Mark Jurkowitz, Shree-
nita Ghosh, Aaron Smith, Sarah Naseer, and Christopher St. Aubin. The Role of Alter-
native Social Media in the News and Information Environment. Technical report, Pew Re-
search Center, October 2022. URL https://www.pewresearch.org/journalism/2022/10/06/
the-role-of-alternative-social-media-in-the-news-and-information-environment/ .
[107] Diana Zulli, Miao Liu, and Robert Gehl. Rethinking the “social” in “social media”: Insights into topology,
abstraction, and scale on the Mastodon social network. New Media & Society , 22(7):1188–1205, July 2020.
ISSN 1461-4448, 1461-7315. doi: 10.1177/1461444820912533. URL http://journals.sagepub.com/doi/10.
1177/1461444820912533.
[108] Yevgeniy Golovchenko. Fighting Propaganda with Censorship: A Study of the Ukrainian Ban on Russian Social
Media. The Journal of Politics , 84(2):639–654, April 2022. ISSN 0022-3816, 1468-2508. doi: 10.1086/716949.
URL https://www.journals.uchicago.edu/doi/10.1086/716949.
[109] Michael Patty. Social Media and Censorship: Rethinking State Action Once Again. Mitchell Hamline Law
Journal of Public Policy and Practice , 40:99–136, 2019.
[110] Martin J. Riedl, Kelsey N. Whipple, and Ryan Wallace. Antecedents of support for social media content
moderation and platform regulation: The role of presumed effects on self and others. Information, Commu-
nication & Society , 25(11):1632–1649, August 2022. ISSN 1369-118X. doi: 10.1080/1369118X.2021.1874040.
URL https://doi.org/10.1080/1369118X.2021.1874040.
[111] Richard Medina and George Hepner. Geospatial Analysis of Dynamic Terrorist Networks. In Ibrahim A.
Karawan, Wayne McCormack, and Stephen E. Reynolds, editors, Values and Violence , volume 4, pages
151–167. Springer Netherlands, Dordrecht, 2009. ISBN 978-1-4020-8659-5 978-1-4020-8660-1. doi: 10.1007/
978-1-4020-8660-1 10. URL http://link.springer.com/10.1007/978-1-4020-8660-1_10 .
[112] A. O’Neil. Right wing terrorism in the west: Radicalization and decentralization. Pathways to Peace and
Security, (1):125–137, 2017. ISSN 23071494, 23115238. doi: 10.20542/2307-1494-2017-1-125-137. URL http:
//www.imemo.ru/files/File/magazines/puty_miru/2017/01/08ONeil.pdf.
[113] Travis Linnemann and Corina Medley. Black sites, “dark sides”: War power, police power, and the violence
of the (un)known. Crime, Media, Culture: An International Journal , 15(2):341–358, August 2019. ISSN
1741-6590, 1741-6604. doi: 10.1177/1741659018777779. URL http://journals.sagepub.com/doi/10.1177/
1741659018777779.
[114] Gerald Sussman and Sascha Krader. Template Revolutions: Marketing U.S. Regime Change in Eastern Europe.
Westminster Papers in Communication and Culture , 5(3):91, August 2008. ISSN 1744-6716, 1744-6708. doi:
10.16997/wpcc.95. URL http://www.westminsterpapers.org/article/10.16997/wpcc.95/.
[115] Phineas Rueckert. How a Journalist’s Murder Led to a Global Investigation Into the Mercenar-
ies Who Sell Disinformation and Destroy Democracies. Haaretz, February 2023. URL https:
//www.haaretz.com/israel-news/security-aviation/2023-02-14/ty-article-magazine/.premium/
how-a-journalists-murder-led-to-the-pursuit-of-cybermercenaries-who-destroy-democracies/
00000186-4b01-da6c-a3f6-cb0bb4c60000 .
[116] Bob Garfield. Revolution, Inc. — On the Media, November 2005. URL https://www.wnycstudios.org/
podcasts/otm/segments/129044-revolution-inc .
[117] David J. Caspi, Joshua D. Freilich, and Steven M. Chermak. Worst of the bad: Violent white supremacist
groups and lethality. Dynamics of Asymmetric Conflict , 5(1):1–17, March 2012. ISSN 1746-7586. doi: 10.1080/
17467586.2012.679664. URL https://doi.org/10.1080/17467586.2012.679664.
[118] Ian Cobain and Nick Fielding. Revealed: US spy operation that manipulates social media. The
Guardian, March 2011. ISSN 0261-3077. URL https://www.theguardian.com/technology/2011/mar/17/
us-spy-operation-social-networks .
[119] Daniel Bennett. Exploring the impact of an evolving war and terror blogosphere on traditional media
coverage of conflict. Media, War & Conflict , 6(1):37–53, April 2013. ISSN 1750-6352, 1750-6360. doi:
10.1177/1750635212469907. URL http://journals.sagepub.com/doi/10.1177/1750635212469907.
[120] Graphika and SIO. Unheard Voice: Evaluating five years of pro-Western covert influence operations. Technical
report, Graphika, Stanford Internet Observatory, August 2022.
48

[121] Gur Megiddo and Omer Benjakob. The Israelis Destabilizing Democracy and
Disrupting Elections Worldwide. Haaretz, November 2022. URL https://
www.haaretz.com/israel-news/security-aviation/2022-11-16/ty-article-static-ext/
the-israelis-destabilizing-democracy-and-disrupting-elections-worldwide/
00000186-461e-d80f-abff-6e9e08b10000 .
[122] Stephanie Kirchgaessner, Manisha Ganguly, David Pegg, and Jason Burke. Revealed: The
hacking and disinformation team meddling in elections — Technology — The Guardian. The
Guardian, 15 Feb 2023 04.00 GMT. URL https://www.theguardian.com/world/2023/feb/15/
revealed-disinformation-team-jorge-claim-meddling-elections-tal-hanan .
[123] Omer Benjakob and Gur Megiddo. Hacking, Extortion, Election Interference: These Are the
Tools Used by Israel’s Agents of Chaos and Manipulation. Haaretz, February 2023. URL
https://www.haaretz.com/israel-news/security-aviation/2023-02-15/ty-article-magazine/
.premium/hacking-extortion-election-interference-the-toolkit-of-israels-agents-of-chaos/
00000186-4aa6-d933-af9e-cbe7aa9c0000 .
[124] Gur Megiddo and Omer Benjakob. Cambridge Analytica’s Israeli Black Ops Team – Exposed at Last.
Haaretz, February 2023. URL https://www.haaretz.com/israel-news/security-aviation/2023-02-15/
ty-article-magazine/.premium/cambridge-analyticas-israeli-black-ops-team-exposed-at-last/
00000186-4b78-da04-a186-7bfa41fe0000 .
[125] Isabel Debre. Israeli company targeted Nigerian election in Facebook disinformation cam-
paign. Times of Israel , 18 May 2019, 4:16am. URL https://www.timesofisrael.com/
israeli-company-targeted-nigerian-election-in-facebook-disinformation-campaign/ .
[126] Gur Megiddo and Omer Benjakob. Antisemitic Influencers, Fake Journalists: Inside
an Israeli Factory for Online Deception. Haaretz, February 2023. URL https://www.
haaretz.com/israel-news/security-aviation/2023-02-16/ty-article-magazine/.premium/
antisemitic-influencers-fake-journalists-inside-an-israeli-factory-for-online-deception/
00000186-4b7c-da6c-a3f6-cb7f03cf0000 .
[127] Tim Aistrope. Social media and counterterrorism strategy. Australian Journal of International Affairs , 70
(2):121–138, March 2016. ISSN 1035-7718. doi: 10.1080/10357718.2015.1113230. URL https://doi.org/10.
1080/10357718.2015.1113230.
[128] Imran Awan. Cyber-Extremism: Isis and the Power of Social Media. Society, 54(2):138–149, April 2017. ISSN
1936-4725. doi: 10.1007/s12115-017-0114-0. URL https://doi.org/10.1007/s12115-017-0114-0 .
[129] Mark Scott. Digital Bridge: NAFO fellas — Aussie encryption vs. safety — UK lessons for Cal-
ifornia. POLITICO, September 2022. URL https://www.politico.eu/newsletter/digital-bridge/
nafo-fellas-aussie-encryption-vs-safety-uk-lessons-for-california/ .
[130] Joohn Choe. Joohn Choe - Disinformation & extremism researcher and consultant - Freelance — LinkedIn,
April 2023. URL https://www.linkedin.com/in/joohnchoe.
[131] Joohn Choe. JChoe (@JoohnChoe) / Twitter, January 2023. URL https://twitter.com/JoohnChoe.
[132] Joohn Choe. Let me explain something about NAFO as simply as I can: NAFO is a LEADERLESS MOVE-
MENT that does only two things: 1. fights disinfo 2. fundraise for Ukraine #1 means we ratio people like this
guy. That’s low for us. It’ll hit probably 1.5 - 2:1 when all is said and done. 1/3 https://t.co/d4m1ydqCvp,
October 2022. URL https://twitter.com/JoohnChoe/status/1585099669851746304.
[133] Daniel Michaels. Ukraine’s Internet Army of ‘NAFO Fellas’ Fights Russian Trolls and
Re. . . . Wall Street Journal , September 2022. URL https://www.wsj.com/amp/articles/
ukraines-internet-army-of-nafo-fellas-fights-russian-trolls-and-rewards-donors-with-dogs-11664271002 .
[134] Jeffrey Kaplan. ‘Leaderless resistance’. Terrorism and Political Violence , 9(3):80–95, September 1997. ISSN
0954-6553, 1556-1836. doi: 10.1080/09546559708427417. URL http://www.tandfonline.com/doi/abs/10.
1080/09546559708427417.
[135] Jan Kietzmann, Linda W. Lee, Ian P. McCarthy, and Tim C. Kietzmann. Deepfakes: Trick or treat? Business
Horizons, 63(2):135–146, March 2020. ISSN 0007-6813. doi: 10.1016/j.bushor.2019.11.006. URL https:
//www.sciencedirect.com/science/article/pii/S0007681319301600.
49

[136] Allegra Rosenberg. Custom AI chatbots are quietly becoming the next big thing
in fandom. The Verge , March 2023. URL https://www.theverge.com/23627402/
character-ai-fandom-chat-bots-fanfiction-role-playing .
[137] Sacha Altay, Anne-Sophie Hacquin, Coralie Chevallier, and Hugo Mercier. Information delivered by a chatbot
has a positive impact on COVID-19 vaccines attitudes and intentions. Journal of Experimental Psychology:
Applied, 29:52–62, 2023. ISSN 1939-2192. doi: 10.1037/xap0000400.
[138] Chad Edwards, Autumn Edwards, Patric R. Spence, and Ashleigh K. Shelton. Is that a bot running the social
media feed? Testing the differences in perceptions of communication quality for a human agent and a bot agent
on Twitter. Computers in Human Behavior , 33:372–376, April 2014. ISSN 07475632. doi: 10.1016/j.chb.2013.
08.013. URL https://linkinghub.elsevier.com/retrieve/pii/S0747563213003129.
[139] Zahra Khanjani, Gabrielle Watson, and Vandana P. Janeja. Audio deepfakes: A survey. Frontiers in Big Data ,
5:1001063, January 2023. ISSN 2624-909X. doi: 10.3389/fdata.2022.1001063. URL https://www.ncbi.nlm.
nih.gov/pmc/articles/PMC9869423/.
[140] Allegra Rosenberg. AI-generated audio of Joe Biden and Donald Trump trashtalking while gaming is tak-
ing over TikTok. Business Insider , Mar 1, 2023, 2:06 PM. URL https://www.businessinsider.com/
voice-ai-audio-joe-biden-donald-trump-tiktok-2023-3 .
[141] Suzhen Wang, Lincheng Li, Yu Ding, and Xin Yu. One-Shot Talking Face Generation from Single-Speaker
Audio-Visual Correlation Learning. Proceedings of the AAAI Conference on Artificial Intelligence , 36(3):2531–
2539, June 2022. ISSN 2374-3468, 2159-5399. doi: 10.1609/aaai.v36i3.20154. URL https://ojs.aaai.org/
index.php/AAAI/article/view/20154.
[142] Zhiliang Xu, Zhibin Hong, Changxing Ding, Zhen Zhu, Junyu Han, Jingtuo Liu, and Errui Ding. Mobile-
FaceSwap: A Lightweight Framework for Video Face Swapping. Proceedings of the AAAI Conference on
Artificial Intelligence, 36(3):2973–2981, June 2022. ISSN 2374-3468, 2159-5399. doi: 10.1609/aaai.v36i3.20203.
URL https://ojs.aaai.org/index.php/AAAI/article/view/20203.
[143] Andreas Blattmann, Robin Rombach, Huan Ling, Tim Dockhorn, Seung Wook Kim, Sanja Fidler, and Karsten
Kreis. Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models, April 2023. URL
http://arxiv.org/abs/2304.08818.
[144] Alex Yu, Vickie Ye, Matthew Tancik, and Angjoo Kanazawa. pixelNeRF: Neural Radiance Fields from One
or Few Images. In 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , pages
4576–4585, June 2021. doi: 10.1109/CVPR46437.2021.00455.
[145] Jonathan T. Barron, Ben Mildenhall, Dor Verbin, Pratul P. Srinivasan, and Peter Hedman. Mip-NeRF 360:
Unbounded Anti-Aliased Neural Radiance Fields. In 2022 IEEE/CVF Conference on Computer Vision and
Pattern Recognition (CVPR), pages 5460–5469, New Orleans, LA, USA, June 2022. IEEE. ISBN 978-1-66546-
946-3. doi: 10.1109/CVPR52688.2022.00539. URL https://ieeexplore.ieee.org/document/9878829/.
[146] Minfeng Zhu, Pingbo Pan, Wei Chen, and Yi Yang. DM-GAN: Dynamic Memory Generative Adversarial
Networks for Text-To-Image Synthesis. In 2019 IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), pages 5795–5803, Long Beach, CA, USA, June 2019. IEEE. ISBN 978-1-72813-293-8.
doi: 10.1109/CVPR.2019.00595. URL https://ieeexplore.ieee.org/document/8954283/.
[147] Amina Kammoun, Rim Slama, Hedi Tabia, Tarek Ouni, and Mohmed Abid. Generative Adversarial Networks
for Face Generation: A Survey. ACM Computing Surveys , 55(5):94:1–94:37, December 2022. ISSN 0360-0300.
doi: 10.1145/3527850. URL https://dl.acm.org/doi/10.1145/3527850.
[148] Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang, Chaojun
Xiao, Chi Han, Yi Ren Fung, Yusheng Su, Huadong Wang, Cheng Qian, Runchu Tian, Kunlun Zhu, Shihao
Liang, Xingyu Shen, Bokai Xu, Zhen Zhang, Yining Ye, Bowen Li, Ziwei Tang, Jing Yi, Yuzhang Zhu, Zhenning
Dai, Lan Yan, Xin Cong, Yaxi Lu, Weilin Zhao, Yuxiang Huang, Junxi Yan, Xu Han, Xian Sun, Dahai Li,
Jason Phang, Cheng Yang, Tongshuang Wu, Heng Ji, Zhiyuan Liu, and Maosong Sun. Tool Learning with
Foundation Models, April 2023. URL http://arxiv.org/abs/2304.08354.
[149] Ali Kashefi and Tapan Mukerji. ChatGPT for Programming Numerical Methods, April 2023. URL http:
//arxiv.org/abs/2303.12093.
50

[150] Hossein Hassani and Emmanuel Sirmal Silva. The Role of ChatGPT in Data Science: How AI-Assisted Con-
versational Interfaces Are Revolutionizing the Field. Big Data and Cognitive Computing , 7(2):62, June 2023.
ISSN 2504-2289. doi: 10.3390/bdcc7020062. URL https://www.mdpi.com/2504-2289/7/2/62.
[151] Josh A Goldstein, Girish Sastry, Micah Musser, Ren´ ee DiResta, Matthew Gentzel, and Katerina Sedova. Gen-
erative Language Models and Automated Influence Operations: Emerging Threats and Potential Mitigations.
Technical report, Stanford Internet Observatory, OpenAI, and Georgetown University’s Center for Security and
Emerging Technology, January 2023.
[152] Joshua Uyheng, Lynnette Hui Xian Ng, and Kathleen M. Carley. Active, aggressive, but to little avail:
Characterizing bot activity during the 2020 Singaporean elections. Computational and Mathematical Orga-
nization Theory , 27(3):324–342, September 2021. ISSN 1572-9346. doi: 10.1007/s10588-021-09332-1. URL
https://doi.org/10.1007/s10588-021-09332-1 .
[153] Adrian Rauchfleisch and Jonas Kaiser. The False positive problem of automatic bot detection in social science
research. PLOS ONE , 15(10):e0241045, October 2020. ISSN 1932-6203. doi: 10.1371/journal.pone.0241045.
URL https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0241045.
[154] Mark Hachman. The best AI art generators: Bring your wildest dreams to life. PC-
World, Apr 4, 2023 3:45 am PDT. URL https://www.pcworld.com/article/1672975/
the-best-ai-art-generators-for-you-midjourney-bing-and-more.html .
[155] Emmanuelle Saliba. ’A real worry’: How AI is making it harder to spot fake images, April 7, 2023, 6:08 AM.
URL https://abcnews.go.com/US/real-worry-ai-making-harder-spot-fake-images/story?id=98188795 .
[156] Andrew Garfield. The U.S. Counter-propaganda Failure in Iraq. Middle East Quarterly , 14(4):23–32, September
2007. URL https://www.meforum.org/1753/the-us-counter-propaganda-failure-in-iraq .
[157] Jenna McLaughlin. Why the US government’s counter-terrorism tweeters are finding it tough
to fight ISIS Online, September 2014. URL https://www.motherjones.com/politics/2014/09/
isis-social-media-state-department/ .
[158] Bernd Debusmann. United States lags in propaganda war against ISIS — Bernd Debusmann. The Arab Weekly,
June 2015. URL https://thearabweekly.com/united-states-lags-propaganda-war-against-isis .
[159] Dylan Gerstel. ISIS and Innovative Propaganda: Confronting Extremism in the Digital Age. Swarthmore
International Relations Journal , (1):1–9, 2016. ISSN 25740113. doi: 10.24968/2574-0113.1.5. URL http:
//works.swarthmore.edu/swarthmoreirjournal/vol1/iss1/5/.
[160] Alexander Abad-Santos. This 13-Year-Old Is Scared When the Sky Is Blue Because of Our
Drones. The Atlantic , October 2013. URL https://www.theatlantic.com/politics/archive/2013/10/
saddest-words-congresss-briefing-drone-strikes/354548/ .
[161] Karen McVeigh. Drone strikes: Tears in Congress as Pakistani family tells of mother’s death. The
Guardian, October 2013. ISSN 0261-3077. URL https://www.theguardian.com/world/2013/oct/29/
pakistan-family-drone-victim-testimony-congress .
[162] Matthew Byrne. Drone Skies. Current Affairs , (March/April 2022), June 2022. ISSN 2471-2647. URL
https://www.currentaffairs.org/2022/06/drone-skies.
[163] L. DeNardis and A.M. Hackl. Internet governance by social media platforms. Telecommunications Policy, 39
(9):761–770, October 2015. ISSN 03085961. doi: 10.1016/j.telpol.2015.04.003. URL https://linkinghub.
elsevier.com/retrieve/pii/S0308596115000592.
[164] TOI Staff and AP. Trump campaign mined Facebook user data using Israeli ‘intelligence gath-
ering’. Times of Israel , 20 March 2018, 3:42 am. URL https://www.timesofisrael.com/
trump-campaign-mined-facebook-user-data-using-israeli-intelligence-gathering/ .
[165] Haaretz. Israeli Hackers Reportedly Offered Trump-linked Firm Cambridge Analytica Private Info
on Two Heads of State. Haaretz, March 2018. URL https://www.haaretz.com/israel-news/
2018-03-21/ty-article/israeli-hackers-offered-trump-linked-firm-info-on-2-heads-of-state/
0000017f-dbc2-d3a5-af7f-fbee1a830000 .
51

[166] James Bamford. The Trump Campaign’s Collusion With Israel. The Nation , March 2023. ISSN 0027-8378.
URL https://www.thenation.com/article/world/trump-israel-collusion/ .
[167] Sarah Chayes. The Strategies Are Foreign, but the Corruption Is American: A Response
to ”The Rise of Strategic Corruption”. Foreign Affairs , 99(6):167–170, November/December
2020. ISSN 0015-7120. URL https://www.foreignaffairs.com/articles/united-states/2020-10-13/
strategies-are-foreign-corruption-american .
[168] Samantha Bradshaw, Hannah Bailey, and Philip N. Howard. Industrialized Disinformation: 2020 Global
Inventory of Organized Social Media Manipulation. Working Paper 2021.1, Oxford Internet Insti-
tute, Oxford, UK, 2021. URL https://demtech.oii.ox.ac.uk/wp-content/uploads/sites/12/2021/02/
CyberTroop-Report20-Draft9.pdf .
[169] Byron Tau and Rebecca Ballhaus. Israeli Intelligence Company Formed Venture With Trump Campaign Firm
Cambridge Analytica. Wall Street Journal, May 2018. ISSN 0099-9660. URL https://www.wsj.com/articles/
israeli-intelligence-company-formed-venture-with-trump-campaign-firm-cambridge-analytica-1527030765 .
[170] Jason Jay Smart. Founder of NAFO Reveals Identity, Discusses Raison D’ˆ etre. Kyiv Post , November 2022.
URL https://www.kyivpost.com/post/204.
[171] Psy Group. Project ”Rome”: Campaign Intelligence & Influence Services Proposal. Technical re-
port, Psy Group, April 2016. URL https://int.nyt.com/data/documenthelper/360-trump-project-rome/
574d679d1ff58a30836c/optimized/full.pdf.
[172] Mark Mazzetti, Ronen Bergman, David D. Kirkpatrick, and Maggie Haberman. Rick Gates Sought Online
Manipulation Plans From Israeli Intelligence Firm for Trump Campaign. The New York Times , October 2018.
ISSN 0362-4331. URL https://www.nytimes.com/2018/10/08/us/politics/rick-gates-psy-group-trump.
html.
[173] Raphael Ahren. US funds aided 2015 campaign to oust Netanyahu, Senate probe
finds. Times of Israel , 12 July 2016, 10:26 pm. URL http://www.timesofisrael.com/
us-funds-aided-2015-campaign-to-oust-netanyahu-senate-probe-finds/ .
[174] EIU. The Economist Intelligence Unit’s Democracy Index 2016. Technical report, The Economist Intelli-
gence Unit, 2017. URL https://impact.economist.com/perspectives/sites/default/files/The%20EIU%
27s%202016%20Democracy%20Index_0.pdf.
[175] EIU. The Economist Intelligence Unit’s Democracy Index 2022. Technical report, The Economist Intelligence
Unit, 2023. URL https://www.eiu.com/n/campaigns/democracy-index-2022/ .
[176] Jaechun Kim. Democratic Peace and Covert War: A Case Study of the U.S. Covert War in Chile. Journal of
International and Area Studies , 12(1):25–47, June 2005.
[177] Richard Falk and Virginia Tilley. Israeli Practices towards the Palestinian People and the Question of Apartheid,
Executive Summary. Middle East Policy , 24(2):33–40, 2017. ISSN 1475-4967. doi: 10.1111/mepo.12265. URL
https://onlinelibrary.wiley.com/doi/abs/10.1111/mepo.12265.
[178] David Lloyd. Settler Colonialism and the State of Exception: The Example of Palestine/Israel. Settler Colonial
Studies, 2(1):59–80, January 2012. ISSN 2201-473X. doi: 10.1080/2201473X.2012.10648826. URL https:
//doi.org/10.1080/2201473X.2012.10648826.
[179] Martin Gilens and Benjamin I. Page. Testing Theories of American Politics: Elites, Interest Groups, and Av-
erage Citizens. Perspectives on Politics , 12(3):564–581, September 2014. ISSN 1537-5927, 1541-0986. doi: 10.
1017/S1537592714001595. URL https://www.cambridge.org/core/journals/perspectives-on-politics/
article/testing-theories-ofamerican-politics-elites-interest-groups-and-averagecitizens/
62327F513959D0A304D4893B382B992B.
[180] Martin Gilens. Inequality and Democratic Responsiveness. Public Opinion Quarterly , 69(5):778–796, January
2005. ISSN 0033-362X. doi: 10.1093/poq/nfi058. URL https://doi.org/10.1093/poq/nfi058.
[181] Larry M. Bartels. Unequal Democracy: The Political Economy of the New Gilded Age - Second Edition .
Princeton University Press, September 2016. ISBN 978-1-4008-8336-3. doi: 10.1515/9781400883363. URL
https://www.degruyter.com/document/doi/10.1515/9781400883363/html.
52

[182] Glen E. Holt. Democracy or Republic: Answering a Frequent Reference Question. Public Library Quarterly ,
35(3):243–253, July 2016. ISSN 0161-6846. doi: 10.1080/01616846.2016.1210454. URL https://doi.org/10.
1080/01616846.2016.1210454.
[183] Andreas Schedler. Electoral Authoritarianism. In Emerging Trends in the Social and Behavioral Sciences, pages
1–16. John Wiley & Sons, Ltd, 2015. ISBN 978-1-118-90077-2. doi: 10.1002/9781118900772.etrds0098. URL
https://onlinelibrary.wiley.com/doi/abs/10.1002/9781118900772.etrds0098.
[184] Angela K. Bourne and Fernando Casal B´ ertoa. Mapping ‘Militant Democracy’: Variation in Party Ban Practices
in European Democracies (1945-2015). European Constitutional Law Review, 13(2):221–247, June 2017. ISSN
1574-0196, 1744-5515. doi: 10.1017/S1574019617000098. URL https://www.cambridge.org/core/product/
identifier/S1574019617000098/type/journal_article.
[185] Constance Bitso, Ina Fourie, and Theo J. D. Bothma. Trends in transition from classical censorship to Internet
censorship : Selected country overviews. Innovation : journal of appropriate librarianship and information
work in Southern Africa , 2013(46):166–191, June 2013. doi: 10.10520/EJC148135. URL https://journals.
co.za/doi/abs/10.10520/EJC148135.
[186] Stephen Farrall, Stuart Wilks-Heeg, Robert Struthers, and Emily Gray. Who are the victims of electoral
fraud in Great Britain? Evidence from survey research. British Politics , 17(3):333–352, September 2022.
ISSN 1746918X. doi: 10.1057/s41293-021-00189-1. URL https://www.proquest.com/docview/2701342210/
24F35A44DDA34416PQ/1.
[187] Andr´ e Kaiser. House of Lords and Monarchy: British Majoritarian Democracy and the Current Reform
Debate about its Pre-Democratic Institutions. In Peter Catterall, Wolfram Kaiser, and Ulrike Walton-Jordan,
editors, Reforming the Constitution, pages 97–128. Routledge, first edition, May 2014. ISBN 978-1-315-03978-7.
doi: 10.4324/9781315039787-4. URL https://www.taylorfrancis.com/books/9781135305628/chapters/10.
4324/9781315039787-4.
[188] David Sylvan and Stephen Majeski. An Agent-Based Model of the Acquisition of U.S. Client States. In Paper
Prepared for Presentation at the 44th Annual Convention of the International Studies Association , Portland,
OR, 2003.
[189] Chas W. Freeman. A Diplomatic Taxonomy for the New World Disorder. In Paul Webster Hare, Juan Luis
Manfredi-S´ anchez, and Kenneth Weisbrode, editors, The Palgrave Handbook of Diplomatic Reform and In-
novation, Studies in Diplomacy and International Relations, pages 41–58. Springer International Publishing,
Cham, 2023. ISBN 978-3-031-10971-3. doi: 10.1007/978-3-031-10971-3 3. URL https://doi.org/10.1007/
978-3-031-10971-3_3 .
[190] Reuters Staff. What are the links between Cambridge Analytica and a Brexit cam-
paign group? Reuters, March 2018. URL https://www.reuters.com/article/
us-facebook-cambridge-analytica-leave-eu-idUSKBN1GX2IO .
[191] BBC. Cambridge Analytica ’not involved’ in Brexit referendum, says watchdog. BBC News , October 2020.
URL https://www.bbc.com/news/uk-politics-54457407 .
[192] Albert-L´ aszl´ o Barab´ asi and R´ eka Albert. Emergence of Scaling in Random Networks.Science, 286(5439):
509–512, October 1999. doi: 10.1126/science.286.5439.509. URL https://www.science.org/doi/10.1126/
science.286.5439.509.
[193] VenkataSwamy Martha, Weizhong Zhao, and Xiaowei Xu. A study on Twitter user-follower network: A
network based analysis. In Proceedings of the 2013 IEEE/ACM International Conference on Advances in
Social Networks Analysis and Mining , ASONAM ’13, pages 1405–1409, New York, NY, USA, August 2013.
Association for Computing Machinery. ISBN 978-1-4503-2240-9. doi: 10.1145/2492517.2500298. URL https:
//dl.acm.org/doi/10.1145/2492517.2500298.
[194] Anna D. Broido and Aaron Clauset. Scale-free networks are rare. Nature Communications , 10(1):1017,
March 2019. ISSN 2041-1723. doi: 10.1038/s41467-019-08746-5. URL https://www.nature.com/articles/
s41467-019-08746-5 .
[195] Emma Remy. How public and private Twitter users in the U.S. compare — and why it might
matter for your research, July 2019. URL https://www.pewresearch.org/decoded/2019/07/15/
how-public-and-private-twitter-users-in-the-u-s-compare-and-why-it-might-matter-for-your-research/ .
53

[196] Jorge Bahamonde, Johan Bollen, Erick Elejalde, Leo Ferres, and Barbara Poblete. Power structure in Chilean
news media. PLOS ONE , 13(6):e0197150, June 2018. ISSN 1932-6203. doi: 10.1371/journal.pone.0197150.
URL https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0197150.
[197] Christopher Meyers. Partisan News, the Myth of Objectivity, and the Standards of Responsible Journalism.
Journal of Media Ethics , 35(3):180–194, July 2020. ISSN 2373-6992, 2373-700X. doi: 10.1080/23736992.2020.
1780131. URL https://www.tandfonline.com/doi/full/10.1080/23736992.2020.1780131.
[198] Jens van ’t Klooster and Cl´ ement Fontan. The Myth of Market Neutrality: A Comparative Study of the
European Central Bank’s and the Swiss National Bank’s Corporate Security Purchases.New Political Economy,
25(6):865–879, September 2020. ISSN 1356-3467. doi: 10.1080/13563467.2019.1657077. URL https://doi.
org/10.1080/13563467.2019.1657077.
[199] Marco A. Vieira. Understanding Resilience in International Relations: The Non-Aligned Movement and
Ontological Security. International Studies Review , 18(2):290–311, June 2016. ISSN 1521-9488. doi:
10.1093/isr/viw002. URL https://doi.org/10.1093/isr/viw002.
[200] Irwin P. Levin, Sandra L. Schneider, and Gary J. Gaeth. All Frames Are Not Created Equal: A Typology and
Critical Analysis of Framing Effects. Organizational Behavior and Human Decision Processes , 76(2):149–188,
November 1998. ISSN 07495978. doi: 10.1006/obhd.1998.2804. URL https://linkinghub.elsevier.com/
retrieve/pii/S0749597898928047.
[201] Claes H. Vreese. News framing: Theory and typology. Information Design Journal , 13(1):51–62, April 2005.
ISSN 0142-5471, 1569-979X. doi: 10.1075/idjdd.13.1.06vre. URL http://www.jbe-platform.com/content/
journals/10.1075/idjdd.13.1.06vre.
[202] Dennis Chong and James N. Druckman. Framing Theory. Annual Review of Political Science , 10(1):103–
126, June 2007. ISSN 1094-2939, 1545-1577. doi: 10.1146/annurev.polisci.10.072805.103054. URL https:
//www.annualreviews.org/doi/10.1146/annurev.polisci.10.072805.103054.
[203] Amos Tversky and Daniel Kahneman. The Framing of Decisions and the Psychology of Choice. Science, 211
(4481):453–458, January 1981. doi: 10.1126/science.7455683. URL https://www.science.org/doi/abs/10.
1126/science.7455683.
[204] Yanqiu Rachel Zhou and William D. Coleman. Accelerated Contagion and Response: Understanding the
Relationships among Globalization, Time, and Disease. Globalizations, 13(3):285–299, May 2016. ISSN 1474-
7731. doi: 10.1080/14747731.2015.1056498. URL https://doi.org/10.1080/14747731.2015.1056498.
[205] Julia R. DeCook and Mi Hyun Yoon. Kung Flu and Roof Koreans: Asian/Americans as the Hated Other
and Proxies of Hating in the White Imaginary. Journal of Hate Studies , 17(1):119–132, October 2021. ISSN
2169-7442. doi: 10.33972/jhs.199. URL https://jhs.press.gonzaga.edu/articles/10.33972/jhs.199?utm_
source=TrendMD&utm_medium=cpc&utm_campaign=Journal_of_Hate_Studies_TrendMD_1.
[206] Daniel Kahneman. Thinking, Fast and Slow . Doubleday Canada, November 2011. ISBN 978-0-385-67652-6.
[207] Masaud Shah and Hyun Goo Woo. Omicron: A Heavily Mutated SARS-CoV-2 Variant Exhibits Stronger
Binding to ACE2 and Potently Escapes Approved COVID-19 Therapeutic Antibodies.Frontiers in Immunology,
12:830527, 2021. ISSN 1664-3224. doi: 10.3389/fimmu.2021.830527.
[208] Leyun Wu, Liping Zhou, Mengxia Mo, Tingting Liu, Chengkun Wu, Chunye Gong, Kai Lu, Likun Gong, Weil-
iang Zhu, and Zhijian Xu. SARS-CoV-2 Omicron RBD shows weaker binding affinity than the currently domi-
nant Delta variant to human ACE2. Signal Transduction and Targeted Therapy, 7(1):1–3, January 2022. ISSN
2059-3635. doi: 10.1038/s41392-021-00863-2. URL https://www.nature.com/articles/s41392-021-00863-2 .
[209] Milena Sokolowska. Outsmarting SARS-CoV-2 by empowering a decoy ACE2.Signal Transduction and Targeted
Therapy, 5(1):1–3, November 2020. ISSN 2059-3635. doi: 10.1038/s41392-020-00370-w. URL https://www.
nature.com/articles/s41392-020-00370-w .
[210] Sebastian Fiedler, Monika A. Piziorska, Viola Denninger, Alexey S. Morgunov, Alison Ilsley, Anisa Y. Malik,
Matthias M. Schneider, Sean R. A. Devenish, Georg Meisl, Vasilis Kosmoliaptsis, Adriano Aguzzi, Heike Fiegler,
and Tuomas P. J. Knowles. Antibody Affinity Governs the Inhibition of SARS-CoV-2 Spike/ACE2 Binding in
Patient Serum. ACS Infectious Diseases, 7(8):2362–2369, August 2021. doi: 10.1021/acsinfecdis.1c00047. URL
https://doi.org/10.1021/acsinfecdis.1c00047.
54

[211] Eric Wang. Prediction of antibody binding to SARS-CoV-2 RBDs. Bioinformatics Advances, 3(1):vbac103,
January 2023. ISSN 2635-0041. doi: 10.1093/bioadv/vbac103. URL https://doi.org/10.1093/bioadv/
vbac103.
[212] Haewoon Kwak, Hyunwoo Chun, and Sue Moon. Fragile online relationship: A first look at unfollow dynamics
in twitter. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems , CHI ’11, pages
1091–1100, New York, NY, USA, May 2011. Association for Computing Machinery. ISBN 978-1-4503-0228-9.
doi: 10.1145/1978942.1979104. URL https://dl.acm.org/doi/10.1145/1978942.1979104.
[213] Bo Xu, Yun Huang, Haewoon Kwak, and Noshir Contractor. Structures of broken ties: Exploring unfollow
behavior on twitter. In Proceedings of the 2013 Conference on Computer Supported Cooperative Work , pages
871–876, San Antonio Texas USA, February 2013. ACM. ISBN 978-1-4503-1331-5. doi: 10.1145/2441776.
2441875. URL https://dl.acm.org/doi/10.1145/2441776.2441875.
[214] Alessia Antelmi, Delfina Malandrino, and Vittorio Scarano. Characterizing the Behavioral Evolution of Twitter
Users and The Truth Behind the 90-9-1 Rule. In Companion Proceedings of The 2019 World Wide Web Con-
ference, WWW ’19, pages 1035–1038, New York, NY, USA, May 2019. Association for Computing Machinery.
ISBN 978-1-4503-6675-5. doi: 10.1145/3308560.3316705. URL https://doi.org/10.1145/3308560.3316705.
[215] Astrid M. Rosenthal-von der P¨ utten, Matthias R. Hastall, S¨ oren K¨ ocher, Christian Meske, Timo Heinrich,
Franziska Labrenz, and Sebastian Ocklenburg. “Likes” as social rewards: Their role in online social comparison
and decisions to like other People’s selfies. Computers in Human Behavior , 92:76–86, March 2019. ISSN
0747-5632. doi: 10.1016/j.chb.2018.10.017. URL https://www.sciencedirect.com/science/article/pii/
S0747563218305016.
[216] Lauren E. Sherman, Ashley A. Payton, Leanna M. Hernandez, Patricia M. Greenfield, and Mirella Dapretto.
The Power of the Like in Adolescence: Effects of Peer Influence on Neural and Behavioral Responses to Social
Media. Psychological Science, 27(7):1027–1035, July 2016. ISSN 0956-7976. doi: 10.1177/0956797616645673.
URL https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5387999/.
[217] Panagiotis Metaxas, Eni Mustafaraj, Kily Wong, Laura Zeng, Megan O’Keefe, and Samantha Finn. What
Do Retweets Indicate? Results from User Survey and Meta-Review of Research. Proceedings of the Ninth
International AAAI Conference on Web and Social Media , 9(1):658–661, 2015. ISSN 2334-0770, 2162-3449.
doi: 10.1609/icwsm.v9i1.14661. URL https://ojs.aaai.org/index.php/ICWSM/article/view/14661.
[218] Ramon Villa-Cox, Sumeet Kumar, Matthew Babcock, and Kathleen M. Carley. Stance in Replies and Quotes
(SRQ): A New Dataset For Learning Stance in Twitter Conversations, June 2020. URL http://arxiv.org/
abs/2006.00691.
[219] Piroska Lendvai and Uwe Reichel. Contradiction Detection for Rumorous Claims. In Proceedings of the Work-
shop on Extra-Propositional Aspects of Meaning in Computational Linguistics (ExProM) , pages 31–40, Osaka,
Japan, December 2016. The COLING 2016 Organizing Committee.
[220] Ly Dinh and Nikolaus Parulian. COVID-19 pandemic and information diffusion analysis on Twitter.Proceedings
of the Association for Information Science and Technology , 57(1):e252, 2020. ISSN 2373-9231. doi: 10.1002/
pra2.252. URL https://onlinelibrary.wiley.com/doi/abs/10.1002/pra2.252.
[221] Cagri Toraman, Furkan S ¸ahinu¸ c, Eyup Halit Yilmaz, and Ibrahim Batuhan Akkaya. Understanding social
engagements: A comparative analysis of user and text features in Twitter. Social Network Analysis and
Mining, 12(1):47, March 2022. ISSN 1869-5469. doi: 10.1007/s13278-022-00872-1. URL https://doi.org/10.
1007/s13278-022-00872-1 .
[222] Twitter. Don’t miss the Tweets about your Tweet. Now on iOS, you can see Retweets with com-
ments all in one place. https://t.co/oanjZfzC6y, May 2020. URL https://twitter.com/Twitter/status/
1260294888811347969.
[223] Jay Peters. Twitter will now make it easier to see quote tweets on iOS, May 2020. URLhttps://www.theverge.
com/2020/5/12/21256586/twitter-ios-quote-tweets-retweets-with-comments .
[224] Beryl No¨ e, Liam D. Turner, David E. J. Linden, Stuart M. Allen, Bjorn Winkens, and Roger M. Whitaker.
Identifying Indicators of Smartphone Addiction Through User-App Interaction.Computers in Human Behavior,
99:56–65, October 2019. ISSN 0747-5632. doi: 10.1016/j.chb.2019.04.023. URL https://www.sciencedirect.
com/science/article/pii/S0747563219301712.
55

[225] Dorian Lyons, Ceyda Kiyak, Deniz Cetinkaya, Sarah Hodge, and John McAlaney. Design and Development
of a Mobile Application to Combat Digital Addiction and Dissociative States During Phone Usage. In 2022
IEEE International Conference on E-Business Engineering (ICEBE) , pages 204–209, Bournemouth, United
Kingdom, October 2022. IEEE. ISBN 978-1-66549-244-7. doi: 10.1109/ICEBE55470.2022.00043. URL https:
//ieeexplore.ieee.org/document/10035050/.
[226] Cassandra Lynn-Collins Troy. Get Ratioed: Questioning the Fossil Fuel Industry’s Social License to Operate on
Twitter. The Journal of Public Interest Communications , 6(1):4, June 2022. ISSN 2573-4342. doi: 10.32473/
jpic.v6.i1.p4. URL https://journals.flvc.org/jpic/article/view/129248.
[227] Joshua R. Minot, Michael V. Arnold, Thayer Alshaabi, Christopher M. Danforth, and Peter Sheridan Dodds.
Ratioing the President: An exploration of public engagement with Obama and Trump on Twitter. PLOS ONE,
16(4):e0248880, April 2021. ISSN 1932-6203. doi: 10.1371/journal.pone.0248880. URL https://journals.
plos.org/plosone/article?id=10.1371/journal.pone.0248880.
[228] Bhavtosh Rath, Wei Gao, Jing Ma, and Jaideep Srivastava. Utilizing computational trust to identify rumor
spreaders on Twitter. Social Network Analysis and Mining, 8(1):64, December 2018. ISSN 1869-5450, 1869-5469.
doi: 10.1007/s13278-018-0540-z. URL http://link.springer.com/10.1007/s13278-018-0540-z .
[229] Zizhu Zhang, Weiliang Zhao, Jian Yang, Cecile Paris, and Surya Nepal. Learning Influence Probabilities and
Modelling Influence Diffusion in Twitter. In Companion Proceedings of The 2019 World Wide Web Conference,
pages 1087–1094, San Francisco USA, May 2019. ACM. ISBN 978-1-4503-6675-5. doi: 10.1145/3308560.3316701.
URL https://dl.acm.org/doi/10.1145/3308560.3316701.
[230] Michele Mazza, Guglielmo Cola, and Maurizio Tesconi. Ready-to-(ab)use: From fake account trafficking to
coordinated inauthentic behavior on Twitter. Online Social Networks and Media , 31:100224, September 2022.
ISSN 24686964. doi: 10.1016/j.osnem.2022.100224. URL https://linkinghub.elsevier.com/retrieve/pii/
S2468696422000271.
[231] Xialing Lin, Patric R. Spence, and Kenneth A. Lachlan. Social media and credibility indicators: The effect of
influence cues. Computers in Human Behavior , 63:264–271, October 2016. ISSN 07475632. doi: 10.1016/j.chb.
2016.05.002. URL https://linkinghub.elsevier.com/retrieve/pii/S074756321630320X.
[232] Inyoung Shin, Luxuan Wang, and Yi-Ta Lu. Twitter and Endorsed (Fake) News: The Influence of Endorsement
by Strong Ties, Celebrities, and a User Majority on Credibility of Fake News During the COVID-19 Pandemic.
International Journal of Communication , 16(0):23, April 2022. ISSN 1932-8036. URL https://ijoc.org/
index.php/ijoc/article/view/18187.
[233] Richard Nadeau, Edouard Cloutier, and J.-H. Guay. New Evidence About the Existence of a Bandwagon
Effect in the Opinion Formation Process. International Political Science Review , 14(2):203–213, April 1993.
ISSN 0192-5121, 1460-373X. doi: 10.1177/019251219301400204. URL http://journals.sagepub.com/doi/
10.1177/019251219301400204.
[234] Matthew Barnfield. Think Twice before Jumping on the Bandwagon: Clarifying Concepts in Research on the
Bandwagon Effect. Political Studies Review , 18(4):553–574, November 2020. ISSN 1478-9299, 1478-9302. doi:
10.1177/1478929919870691. URL http://journals.sagepub.com/doi/10.1177/1478929919870691.
[235] Luca Maria Aiello, Martina Deplano, Rossano Schifanella, and Giancarlo Ruffo. People Are Strange When
You’re a Stranger: Impact and Influence of Bots on Social Networks. Proceedings of the International AAAI
Conference on Web and Social Media , 6(1):10–17, 2012. ISSN 2334-0770. doi: 10.1609/icwsm.v6i1.14236. URL
https://ojs.aaai.org/index.php/ICWSM/article/view/14236.
[236] Sujoy Sikdar, Byungkyu Kang, John ODonovan, Tobias H¨ ollerer, and Sibel Adah. Understanding Information
Credibility on Twitter. In 2013 International Conference on Social Computing , pages 19–24, September 2013.
doi: 10.1109/SocialCom.2013.9.
[237] Sangwook Ha and JoongHo Ahn. Why Are You Sharing Others’ Tweets?: The Impact of Argument Quality
and Source Credibility on Information Sharing Behavior. ICIS 2011 Proceedings, December 2011. URL https:
//aisel.aisnet.org/icis2011/proceedings/humanbehavior/4.
[238] Miriam J. Metzger and Andrew J. Flanagin. Credibility and trust of information in online environments: The
use of cognitive heuristics. Journal of Pragmatics , 59:210–220, December 2013. ISSN 0378-2166. doi: 10.1016/
j.pragma.2013.07.012. URL https://www.sciencedirect.com/science/article/pii/S0378216613001768.
56

[239] Peter J. Jacques and Claire Connolly Knox. Hurricanes and hegemony: A qualitative analysis of micro-level
climate change denial discourses. Environmental Politics , 25(5):831–852, September 2016. ISSN 0964-4016.
doi: 10.1080/09644016.2016.1189233. URL https://doi.org/10.1080/09644016.2016.1189233.
[240] Kristin Haltinner, Dilshani Sarathchandra, and Thomas Ptak. How Believing That Climate Change Is a
Conspiracy Affects Skeptics’ Environmental Attitudes. Environment: Science and Policy for Sustainable De-
velopment, 63(3):25–33, May 2021. ISSN 0013-9157, 1939-9154. doi: 10.1080/00139157.2021.1898900. URL
https://www.tandfonline.com/doi/full/10.1080/00139157.2021.1898900.
[241] Ignacio Ojea Quintana, Ritsaart Reimann, Marc Cheong, Mark Alfano, and Colin Klein. Polarization and
trust in the evolution of vaccine discourse on Twitter during COVID-19. PLOS ONE, 17(12):e0277292, Decem-
ber 2022. ISSN 1932-6203. doi: 10.1371/journal.pone.0277292. URL https://journals.plos.org/plosone/
article?id=10.1371/journal.pone.0277292.
[242] Alice E. Marwick and Danah Boyd. I tweet honestly, I tweet passionately: Twitter users, context collapse, and
the imagined audience. New Media & Society , 13(1):114–133, February 2011. ISSN 1461-4448, 1461-7315. doi:
10.1177/1461444810365313. URL http://journals.sagepub.com/doi/10.1177/1461444810365313.
[243] Leonor Fern´ andez, Alan Fossa, Zhiyong Dong, Tom Delbanco, Joann Elmore, Patricia Fitzgerald, Kendall Har-
court, Jocelyn Perez, Jan Walker, and Catherine DesRoches. Words Matter: What Do Patients Find Judgmental
or Offensive in Outpatient Notes? Journal of General Internal Medicine , 36(9):2571–2578, September 2021.
ISSN 1525-1497. doi: 10.1007/s11606-020-06432-7. URL https://doi.org/10.1007/s11606-020-06432-7 .
[244] Malith Wijesekara and Gamage Upeksha Ganegoda. Source credibility analysis on Twitter users. In 2020 Inter-
national Research Conference on Smart Computing and Systems Engineering (SCSE), pages 96–102, September
2020. doi: 10.1109/SCSE49731.2020.9313064.
[245] Rogers Brubaker. Digital hyperconnectivity and the self. Theory and Society , 49(5-6):771–801, October 2020.
ISSN 0304-2421, 1573-7853. doi: 10.1007/s11186-020-09405-1. URL https://link.springer.com/10.1007/
s11186-020-09405-1 .
[246] Kelly P. Burke and Andrea L. Cox. Hepatitis C virus evasion of adaptive immune responses: A model for viral
persistence. Immunologic Research, 47(1):216–227, July 2010. ISSN 1559-0755. doi: 10.1007/s12026-009-8152-3.
URL https://doi.org/10.1007/s12026-009-8152-3 .
[247] Patrizia Farci, Harvey J. Alter, Sugantha Govindarajan, Doris C. Wong, Ronald Engle, Richard R. Lesniewski,
Isa K. Mushahwar, Suresh M. Desai, Roger H. Miller, Norio Ogata, and Robert H. Purcell. Lack of Protective
Immunity Against Reinfection with Hepatitis C Virus. Science, 258(5079):135–140, October 1992. doi: 10.
1126/science.1279801. URL https://www.science.org/doi/abs/10.1126/science.1279801.
[248] Euisol Jeong and Jieun Lee. We take the red pill, we confront the DickTrix: Online feminist activism and the
augmentation of gendered realities in South Korea. Feminist Media Studies , 18(4):705–717, July 2018. ISSN
1468-0777. doi: 10.1080/14680777.2018.1447354. URL https://doi.org/10.1080/14680777.2018.1447354.
[249] Ruth Garland. The Surrender to the 24/7 News Cycle. In Ruth Garland, editor, Government Communications
and the Crisis of Trust: From Political Spin to Post-truth , pages 107–121. Springer International Publishing,
Cham, 2021. ISBN 978-3-030-77576-6. doi: 10.1007/978-3-030-77576-6 7. URL https://doi.org/10.1007/
978-3-030-77576-6_7 .
[250] Nir Grinberg, Mor Naaman, Blake Shaw, and Gilad Lotan. Extracting Diurnal Patterns of Real World Activity
from Social Media. Proceedings of the Seventh International AAAI Conference on Weblogs and Social Media , 7
(1):205–214, 2013. ISSN 2334-0770, 2162-3449. doi: 10.1609/icwsm.v7i1.14409. URL https://ojs.aaai.org/
index.php/ICWSM/article/view/14409.
[251] Alceu Ferraz Costa, Yuto Yamaguchi, Agma Juci Machado Traina, Caetano Traina, and Christos Faloutsos.
RSC: Mining and Modeling Temporal Activity in Social Media. In Proceedings of the 21th ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining , KDD ’15, pages 269–278, New York, NY,
USA, August 2015. Association for Computing Machinery. ISBN 978-1-4503-3664-2. doi: 10.1145/2783258.
2783294. URL https://dl.acm.org/doi/10.1145/2783258.2783294.
[252] Christoph Schweimer. Fast generation of simple directed social network graphs with reciprocal edges and high
clustering. Social Network Analysis and Mining , 12(1):127, December 2022. ISSN 1869-5450, 1869-5469. doi:
10.1007/s13278-022-00963-z. URL https://link.springer.com/10.1007/s13278-022-00963-z .
57

[253] Christoph Schweimer, Christine Gfrerer, Florian Lugstein, David Pape, Jan A. Velimsky, Robert Els¨ asser,
and Bernhard C. Geiger. Generating Simple Directed Social Network Graphs for Information Spreading. In
Proceedings of the ACM Web Conference 2022 , pages 1475–1485, April 2022. doi: 10.1145/3485447.3512194.
URL http://arxiv.org/abs/2205.02485.
[254] Matteo Cinelli, Gianmarco De Francisci Morales, Alessandro Galeazzi, Walter Quattrociocchi, and Michele
Starnini. The echo chamber effect on social media. Proceedings of the National Academy of Sciences , 118(9):
e2023301118, March 2021. doi: 10.1073/pnas.2023301118. URL https://www.pnas.org/doi/abs/10.1073/
pnas.2023301118.
[255] Haewoon Kwak, Changhyun Lee, Hosung Park, and Sue Moon. What is Twitter, a social network or a news
media? In Proceedings of the 19th International Conference on World Wide Web , pages 591–600, Raleigh
North Carolina USA, April 2010. ACM. ISBN 978-1-60558-799-8. doi: 10.1145/1772690.1772751. URL https:
//dl.acm.org/doi/10.1145/1772690.1772751.
[256] B´ ela Bollob´ as, Christian Borgs, Jennifer Chayes, and Oliver Riordan. Directed scale-free graphs. InProceedings
of the Fourteenth Annual ACM-SIAM Symposium on Discrete Algorithms , SODA ’03, pages 132–139, USA,
January 2003. Society for Industrial and Applied Mathematics. ISBN 978-0-89871-538-5.
[257] Stephanie Kramer. More Americans say they are regularly wearing masks in stores and
other businesses, August 2020. URL https://www.pewresearch.org/short-reads/2020/08/27/
more-americans-say-they-are-regularly-wearing-masks-in-stores-and-other-businesses/ .
[258] Kathy Frankovic. How Trump and Biden supporters differ on face masks — YouGov, October 03,
2020, 9:00 AM GMT-4. URL https://today.yougov.com/topics/politics/articles-reports/2020/10/03/
how-trump-and-biden-supporters-differ-face-masks .
[259] Seth A. Myers and Jure Leskovec. The bursty dynamics of the Twitter information network. In Proceedings
of the 23rd International Conference on World Wide Web , WWW ’14, pages 913–924, New York, NY, USA,
April 2014. Association for Computing Machinery. ISBN 978-1-4503-2744-2. doi: 10.1145/2566486.2568043.
URL https://doi.org/10.1145/2566486.2568043.
[260] V.S. Subrahmanian, Amos Azaria, Skylar Durst, Vadim Kagan, Aram Galstyan, Kristina Lerman, Linhong Zhu,
Emilio Ferrara, Alessandro Flammini, and Filippo Menczer. The DARPA Twitter Bot Challenge. Computer,
49(6):38–46, June 2016. ISSN 1558-0814. doi: 10.1109/MC.2016.183.
[261] Clare Duffy and Brian Fung. Elon Musk commissioned this bot analysis in his fight with Twitter. Now
it shows what he could face if he takes over the platform — CNN Business. CNN, October 2022. URL
https://www.cnn.com/2022/10/10/tech/elon-musk-twitter-bot-analysis-cyabra/index.html .
[262] Lakshmi Varanasi. Twitter bots appear to be be in line with the company’s estimate of below 5% — but you
wouldn’t know it from how much they tweet, researchers say. Business Insider , Sep 8, 2022, 7:48 PM EDT.
URL https://www.businessinsider.com/twitter-bots-comprise-less-than-5-but-tweet-more-2022-9 .
[263] Daron Acemo˘ glu, Giacomo Como, Fabio Fagnani, and Asuman Ozdaglar. Opinion Fluctuations and Dis-
agreement in Social Networks. Mathematics of Operations Research , 38(1):1–27, November 2012. ISSN 0364-
765X. doi: 10.1287/moor.1120.0570. URL https://pubsonline-informs-org.proxy3.library.mcgill.ca/
doi/abs/10.1287/moor.1120.0570.
[264] Ercan Yildiz, Asuman Ozdaglar, Daron Acemoglu, Amin Saberi, and Anna Scaglione. Binary Opinion Dynamics
with Stubborn Agents. ACM Trans. Econ. Comput. , 1(4):19:1–19:30, December 2013. ISSN 2167-8375. doi:
10.1145/2538508. URL http://doi.acm.org/10.1145/2538508.
[265] Dominic DiFranzo and Kristine Gloria-Garcia. Filter Bubbles and Fake News. XRDS: Crossroads, The ACM
Magazine for Students , 23(3):32–35, April 2017. ISSN 1528-4972. doi: 10.1145/3055153. URL http://doi.
acm.org/10.1145/3055153.
[266] Min Jung Lee and Dan Merica. Hillary Clinton: US should ’take out’ Assad’s air fields — CNN Politics. CNN,
April 2017. URL https://www.cnn.com/2017/04/06/politics/hillary-clinton-syria-assad/index.html .
[267] Robyn Torok. Developing an explanatory model for the process of online radicalisation and terrorism. Security
Informatics, 2(1):6, February 2013. ISSN 2190-8532. doi: 10.1186/2190-8532-2-6. URL https://doi.org/10.
1186/2190-8532-2-6 .
58

[268] Andrew H. Hales and Kipling D. Williams. Marginalized Individuals and Extremism: The Role of Ostracism
in Openness to Extreme Groups. Journal of Social Issues , 74(1):75–92, 2018. ISSN 1540-4560. doi: 10.1111/
josi.12257. URL https://onlinelibrary.wiley.com/doi/abs/10.1111/josi.12257.
[269] Gunnar Weimann, Beatrice Berton, and Antonios Samouris. IS’s global digital arenas: Strategy and platforms.
In Salafi-Jihadism and Digital Media . Routledge, 2022. ISBN 978-1-00-326131-5.
[270] Mary Beth Altier, Christian N Thoroughgood, and John G Horgan. Turning away from terrorism: Lessons
from psychology, sociology, and criminology. Journal of Peace Research, 51(5):647–661, September 2014. ISSN
0022-3433, 1460-3578. doi: 10.1177/0022343314535946. URL http://journals.sagepub.com/doi/10.1177/
0022343314535946.
[271] Hanna Paalgard Munden. Extremist group exits: What autobiographies by male right-wing formers reveal about
identity transformation. Behavioral Sciences of Terrorism and Political Aggression, 0(0):1–22, April 2023. ISSN
1943-4472. doi: 10.1080/19434472.2023.2192771. URL https://doi.org/10.1080/19434472.2023.2192771.
[272] Donna Winslow. Rites of Passage and Group Bonding in the Canadian Airborne. Armed Forces & Society, 25
(3):429–457, 1999. ISSN 0095-327X. URL https://www.jstor.org/stable/45346316.
[273] Lynn Davidman and Arthur L. Greil. Characters in Search of a Script: The Exit Narratives of Formerly
Ultra-Orthodox Jews. Journal for the Scientific Study of Religion , 46(2):201–216, 2007. ISSN 1468-5906. doi:
10.1111/j.1468-5906.2007.00351.x. URL https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-5906.
2007.00351.x.
[274] William R. Clark. Petrodollar Warfare : Oil, Iraq and the Future of the Dollar . NSP: New Society Publish-
ers, 2005. ISBN 978-1-55092-335-3 978-0-86571-514-1. URL https://canadacommons.ca/artifacts/1870198/
petrodollar-warfare/2619327/.
[275] Michael Mastanduno. System Maker and Privilege Taker: U.S. Power and the International Political Economy.
World Politics , 61(1):121–154, January 2009. ISSN 0043-8871, 1086-3338. doi: 10.1017/S0043887109000057.
URL https://muse.jhu.edu/article/260515.
[276] Susan A. Seibert. Problem-based learning: A strategy to foster generation Z’s critical thinking and perseverance.
Teaching and Learning in Nursing, 16(1):85–88, January 2021. ISSN 1557-3087. doi: 10.1016/j.teln.2020.09.002.
URL https://www.sciencedirect.com/science/article/pii/S1557308720301049.
[277] Bill Lucas and Janet Hanson. Thinking Like an Engineer: Using Engineering Habits of Mind and Signature
Pedagogies to Redesign Engineering Education. International Journal of Engineering Pedagogy (iJEP) , 6(2):
4–13, May 2016. URL https://doi.org/10.3991/ijep.v6i2.5366.
[278] Safinah Ali, Tyler Moroso, and Cynthia Breazeal. Can Children Learn Creativity from a Social Robot? In
Proceedings of the 2019 on Creativity and Cognition, pages 359–368, San Diego CA USA, June 2019. ACM. ISBN
978-1-4503-5917-7. doi: 10.1145/3325480.3325499. URL https://dl.acm.org/doi/10.1145/3325480.3325499.
[279] Daniela Oliveira, Marissa Rosenthal, Nicole Morin, Kuo-Chuan Yeh, Justin Cappos, and Yanyan Zhuang.
It’s the psychology stupid: How heuristics explain software vulnerabilities and how priming can illuminate
developer’s blind spots. In Proceedings of the 30th Annual Computer Security Applications Conference , pages
296–305, New Orleans Louisiana USA, December 2014. ACM. ISBN 978-1-4503-3005-3. doi: 10.1145/2664243.
2664254. URL https://dl.acm.org/doi/10.1145/2664243.2664254.
[280] Richard F. West, Russell J. Meserve, and Keith E. Stanovich. Cognitive sophistication does not attenuate the
bias blind spot. Journal of Personality and Social Psychology, 103(3):506–519, September 2012. ISSN 1939-1315,
0022-3514. doi: 10.1037/a0028857. URL http://doi.apa.org/getdoi.cfm?doi=10.1037/a0028857.
[281] Kazutoshi Sasahara, Wen Chen, Hao Peng, Giovanni Luca Ciampaglia, Alessandro Flammini, and Filippo
Menczer. Social influence and unfollowing accelerate the emergence of echo chambers.Journal of Computational
Social Science , 4(1):381–402, May 2021. ISSN 2432-2725. doi: 10.1007/s42001-020-00084-7. URL https:
//doi.org/10.1007/s42001-020-00084-7 .
[282] Oriol Vinyals, Igor Babuschkin, Wojciech M. Czarnecki, Micha¨ el Mathieu, Andrew Dudzik, Junyoung Chung,
David H. Choi, Richard Powell, Timo Ewalds, Petko Georgiev, Junhyuk Oh, Dan Horgan, Manuel Kroiss, Ivo
Danihelka, Aja Huang, Laurent Sifre, Trevor Cai, John P. Agapiou, Max Jaderberg, Alexander S. Vezhnevets,
R´ emi Leblond, Tobias Pohlen, Valentin Dalibard, David Budden, Yury Sulsky, James Molloy, Tom L. Paine,
59

Caglar Gulcehre, Ziyu Wang, Tobias Pfaff, Yuhuai Wu, Roman Ring, Dani Yogatama, Dario W¨ unsch, Katrina
McKinney, Oliver Smith, Tom Schaul, Timothy Lillicrap, Koray Kavukcuoglu, Demis Hassabis, Chris Apps,
and David Silver. Grandmaster level in StarCraft II using multi-agent reinforcement learning. Nature, 575
(7782):350–354, November 2019. ISSN 0028-0836, 1476-4687. doi: 10.1038/s41586-019-1724-z. URL http:
//www.nature.com/articles/s41586-019-1724-z .
[283] Amiram Vinokur and Eugene Burnstein. Depolarization of attitudes in groups. Journal of Personality and
Social Psychology , 36(8):872–885, 1978. ISSN 1939-1315. doi: 10.1037/0022-3514.36.8.872. URL https:
//psycnet.apa.org/fulltext/1980-00965-001.pdf .
[284] Samantha L. Moore-Berg, Jacob M. Parelman, Yphtach Lelkes, and Emily B. Falk. Neural polarization and
routes to depolarization. Proceedings of the National Academy of Sciences , 117(46):28552–28554, November
2020. doi: 10.1073/pnas.2020107117. URL https://www.pnas.org/doi/full/10.1073/pnas.2020107117.
[285] Christopher Brian Currin, Sebasti´ an Vallejo Vera, and Ali Khaledi-Nasab. Depolarization of echo chambers
by random dynamical nudge. Scientific Reports , 12(1):9234, June 2022. ISSN 2045-2322. doi: 10.1038/
s41598-022-12494-w. URL https://www.nature.com/articles/s41598-022-12494-w .
[286] Pawe l Sobkowicz. Social Depolarization and Diversity of Opinions—Unified ABM Framework. Entropy, 25(4):
568, April 2023. ISSN 1099-4300. doi: 10.3390/e25040568. URL https://www.mdpi.com/1099-4300/25/4/568.
[287] Vimal Mishra, Amar Deep Tiwari, Saran Aadhar, Reepal Shah, Mu Xiao, D. S. Pai, and Dennis Lettenmaier.
Drought and Famine in India, 1870–2016.Geophysical Research Letters, 46(4):2075–2083, 2019. ISSN 1944-8007.
doi: 10.1029/2018GL081477. URL https://onlinelibrary.wiley.com/doi/abs/10.1029/2018GL081477.
[288] Michael Safi. Churchill’s policies contributed to 1943 Bengal famine – study. The Guardian ,
March 2019. ISSN 0261-3077. URL https://www.theguardian.com/world/2019/mar/29/
winston-churchill-policies-contributed-to-1943-bengal-famine-study .
[289] Bilal Kuchay. Churchill’s policies to blame for 1943 Bengal famine: Study. Al Jazeera, April 2019. URL https:
//www.aljazeera.com/news/2019/4/1/churchills-policies-to-blame-for-1943-bengal-famine-study .
[290] James Q. Whitman. Hitler’s American Model: The United States and the Making of Nazi Race Law. In
Hitler’s American Model . Princeton University Press, February 2017. ISBN 978-1-4008-8463-6. doi: 10.1515/
9781400884636. URL https://www.degruyter.com/document/doi/10.1515/9781400884636/html.
[291] Robert J. Miller. Nazi Germany’s Race Laws, the United States, and American Indians. St. John ’s Law Review,
94(3):751–818, 2020. URL https://heinonline.org/HOL/P?h=hein.journals/stjohn94&i=769.
[292] Carl Davidson and Jerry Harris. Globalisation, theocracy and the new fascism: The US Right’s rise to power.
Race & Class , 47(3):47–67, January 2006. ISSN 0306-3968, 1741-3125. doi: 10.1177/0306396806061086. URL
http://journals.sagepub.com/doi/10.1177/0306396806061086.
[293] William I. Robinson and Mario Barrera. Global capitalism and twenty-first century fascism: A US case
study. Race & Class , 53(3):4–29, January 2012. ISSN 0306-3968. doi: 10.1177/0306396811425983. URL
https://doi.org/10.1177/0306396811425983.
[294] Chetan Bhatt. White Extinction: Metaphysical Elements of Contemporary Western Fascism. Theory, Culture
& Society , 38(1):27–52, January 2021. ISSN 0263-2764, 1460-3616. doi: 10.1177/0263276420925523. URL
http://journals.sagepub.com/doi/10.1177/0263276420925523.
[295] Imogen Richards, Callum Jones, and Gear´ oid Brinn. Eco-Fascism Online: Conceptualizing Far-Right Actors’
Response to Climate Change on Stormfront. Studies in Conflict & Terrorism , 0(0):1–27, December 2022. ISSN
1057-610X. doi: 10.1080/1057610X.2022.2156036. URL https://doi.org/10.1080/1057610X.2022.2156036.
60
