---
title: Can Generative Agent-Based Modeling Replicate the Friendship Paradox in Social Media Simulations?
url: https://arxiv.org/abs/2502.05919
category: social-media
subcategory: empirical
date: 2025-02
venue: ''
authors:
- Gian Marco Orlando
- Valerio La Gatta
- Diego Russo
- Vincenzo Moscato
source: arxiv
pdf_url: https://arxiv.org/pdf/2502.05919
pages: 6
chars: 32916
fetched_at: '2026-11-08T13:08:00+00:00'
kb_version: 1
---

# Can Generative Agent-Based Modeling Replicate the Friendship Paradox in Social Media Simulations?

Can Generative Agent-Based Modeling Replicate the Friendship
Paradox in Social Media Simulations?
Gian Marco Orlando
University of Naples Federico II
gianmarco.orlando@unina.it
Valerio La Gatta
Northwestern University
valerio.lagatta@northwestern.edu
Diego Russo
University of Bergamo
diego.russo@unibg.it
Vincenzo Moscato
University of Naples Federico II
vincenzo.moscato@unina.it
Abstract
Generative Agent-Based Modeling (GABM) is an emerging simula-
tion paradigm that combines the reasoning abilities of Large Lan-
guage Models with traditional Agent-Based Modeling to replicate
complex social behaviors, including interactions on social media.
While prior work has focused on localized phenomena such as
opinion formation and information spread, its potential to capture
global network dynamics remains underexplored. This paper ad-
dresses this gap by analyzing GABM-based social media simulations
through the lens of the Friendship Paradox (FP), a counterintuitive
phenomenon where individuals, on average, have fewer friends
than their friends. We propose a GABM framework for social me-
dia simulations, featuring generative agents that emulate real users
with distinct personalities and interests. Using Twitter datasets on
the US 2020 Election and the QAnon conspiracy, we show that the
FP emerges naturally in GABM simulations. Consistent with real-
world observations, the simulations unveil a hierarchical structure,
where agents preferentially connect with others displaying higher
activity or influence. Additionally, we find that infrequent connec-
tions primarily drive the FP, reflecting patterns in real networks.
These findings validate GABM as a robust tool for modeling global
social media phenomena and highlight its potential for advancing
social science by enabling nuanced analysis of user behavior.
CCS Concepts
• Information systems→ Social networks; Language models; •
Computing methodologies→ Multi-agent systems.
Keywords
Generative Agents; Friendship Paradox; Agent-Based Modeling;
Social Media Simulation
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
WEBSCI ’25, May 20-24, 2025, New Brunswick, New Jersey, USA
© 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-1-4503-XXXX-X/18/06
https://doi.org/XXXXXXX.XXXXXXX
ACM Reference Format:
Gian Marco Orlando, Valerio La Gatta, Diego Russo, and Vincenzo Moscato.
2025. Can Generative Agent-Based Modeling Replicate the Friendship Para-
dox in Social Media Simulations?. In Proceedings of ACM Web Science Con-
ference (WEBSCI ’25). ACM, New York, NY, USA, 6 pages. https://doi.org/
XXXXXXX.XXXXXXX
1 Introduction
Large Language Models (LLMs) have enabled the development of
generative agents, autonomous computational entities capable of
reasoning, adapting, and interacting in ways resembling human be-
havior. Generative Agent-Based Modeling (GABM) leverages these
capabilities and integrates LLM with traditional Agent-Based Mod-
eling (ABM) to enhance simulations by enabling more sophisticated
and adaptive agent behavior [18]. Unlike traditional ABM, which
relies on probabilistic equations and oversimplifies the complex-
ities of human decision-making [ 19], GABM leverages LLMs to
enable generative agents whose behaviors arise naturally from their
interactions within the simulated environment, unconstrained by
predefined rules. This paradigm shift has demonstrated its potential
in simulating complex systems involving human decision-making
and social interactions [18, 22].
Recent studies in the social sciences have explored how GABM
can be applied to model human behaviors in order to investigate a
wide range of micro- and meso-level phenomena [20, 21], primarily
focusing on information propagation [ 9] and influence dynam-
ics [10]. Despite these advancements, the exploration of network
formation processes and global network-level phenomena within
the GABM framework remains underexplored. To our knowledge,
only [7] demonstrates that generative agents naturally form homo-
geneous ideological clusters, akin to real-world phenomenon of
echo chambers. This paper addresses this notable research gap by
focusing on the Friendship Paradox (FP), a phenomenon where
individuals, on average, have fewer friends than their friends do
[6], due to skewed degree distributions typical of social networks.
The Generalized Friendship Paradox (GFP) extends this concept to
other metrics, including (i) Activity Paradox, where individuals are,
on average, less active than their friends [12]; (ii) Virality Paradox,
where individuals are, on average, less influential than their friends
[12]; and (iii) Susceptibility Paradox, where individuals’ friends are,
on average, more susceptible to influence than the individuals them-
selves [15]. The FP and its variations have practical implications for
content virality, opinion formation, and information asymmetry
[16], as well as psychological ramifications, significantly affecting
individuals’ perceptions [13]. Given these implications, exploring
arXiv:2502.05919v1  [cs.SI]  9 Feb 2025

WEBSCI ’25, May 20-24, 2025, New Brunswick, New Jersey, USA Orlando et al.
the reproduction of the FP and GFP within GABM offers valuable
insights into its ability to model complex network-level phenomena,
highlighting its potential as a powerful tool for studying online
human behavior.
We propose a GABM-based social media simulation framework
featuring generative agents powered by LLaMa 3 [5], integrating
realistic personalities, dynamic connections, memory mechanisms,
and standard social media actions, alongside a recommender system
to guide interactions. Our study investigates two research questions:
RQ1: Do the FP and GFP manifest in GABM-based social media
simulations?
RQ2: Which social connections most contribute to experiencing the
FP and GFP?
Given that FP and GFP have been extensively studied in real-
world social networks, our primary contribution is to explore whether
these network-level phenomena naturally emerge in GABM-based
social media simulations. Using Twitter datasets on the US 2020
Election [3] and the QAnon conspiracy [11], we confirm the consis-
tent emergence of the FP and its variations across simulations, with
agents preferentially following those with superior attributes like
higher activity or influence. Notably, in line with real social media
[2, 16], the FP is predominantly driven by less frequent interactions,
rather than more frequent connections with closer followers. These
findings not only validate the applicability of GABM in replicating
complex social phenomena but also provide a new lens for under-
standing the mechanisms underlying the FP and GFP. This study
offers valuable implications for social science research, particu-
larly in exploring the hierarchical and asymmetric nature of social
relationships in digital environments.
2 Methodology
Our framework simulates social media dynamics through genera-
tive agents, advanced LLM-powered entities designed to simulate
realistic user behavior on social media. Each agent is modeled with
a profile, a memory unit, and a reasoning module that enables
decision-making. Over multiple iterations, agents engage in typ-
ical social media actions such as following users, creating posts,
or re-sharing content. The simulation workflow, as illustrated in
Figure 2, consists of three phases which collectively simulate the
dynamics of the social network. We detail generative agents and
each phase of the simulation workflow in the following sections.
2.1 Generative Agents
Agent Profile. The agent’s profile replicates a social media user’s
identity, including inferred personality traits and dynamic social
connections. Personality traits are generated from real user posts
using a prompt-based strategy with LLMs, identifying attributes
such as ideological alignment and engagement style (e.g., being
outspoken, critical, or supportive of specific political figures), as
illustrated in Figure 1. In addition to personality profiling, each
agent maintains a dynamic list of social connections in a social
media graphG =(V,E), whereV ={𝑎1, 𝑎2, . . . , 𝑎𝑛} represents
the set of agents, and E = {(𝑎𝑖, 𝑎𝑗) |𝑎𝑖, 𝑎𝑗 ∈ V}denotes the
directed edges capturing follower-followee relationships. While
personality traits remain static, connections evolve as agents decide
to follow others during the simulation.
Memory Unit. The agent’s activity history is managed through
a memory unit with two components: Short-Term Memory (STM)
and Long-Term Memory (LTM), designed to balance recent and
significant interactions. The STM stores recently published content
along with engagement metadata (e.g., the number of re-shares,
likes, dislikes and comments). To prevent the STM from becoming
overloaded or dominated by outdated content, a decay mechanism
removes less relevant items over time. The probability of removing
an item is defined as 𝑝(𝑀𝑎𝑖 𝑗 ) = 1− 𝑝 𝑗+𝑟 𝑗 2 , where 𝑝 𝑗 represents
engagement popularity and 𝑟 𝑗 measures recency.
The LTM preserves high-impact content identified from STM
through periodic evaluations. Items with engagement scores ex-
ceeding a threshold 𝜏 (set to 0.5 in experiments) are transferred to
LTM, ensuring the retention of only the most influential contents.
Both memory components initialize empty, allowing agents’
memories to evolve dynamically through the simulation, providing
an unbiased foundation for analyzing phenomena like the Friend-
ship Paradox.
Reasoning Module. The Reasoning Module drives the agent’s
decision-making by leveraging LLMs to emulate user behavior
using a prompt-based approach. The module outputs a Choice-
Reason-Content triplet, where Choice specifies the selected action,
Reason details the contextual rationale, and Content defines the
associated material, such as a new post or an interaction with
another agent’s post. If no action is taken, theContent field remains
empty.
2.2 Simulation Workflow
Initialization Phase. The Initialization Phase configures gener-
ative agents to emulate real users by assigning distinct personality
profiles, identifying key interests and traits as outlined in the Agent
Profile section. This approach avoids the extensive parameter cali-
bration of traditional ABM [14] and improves on GABM methods
relying solely on demographic attributes to characterize agents
[21, 22].
Operational Phase. During each simulation iteration, agents
are immersed in an environment resembling a social media platform,
with theOperational Phase executing the core dynamics of the agent-
based model. This phase focuses on constructing the input prompt
for the agent’s Reasoning Module, enabling decision-making for
subsequent actions by incorporating information a real user would
likely consider before taking action. This prompt incorporates three
key elements: (i) feedback on the agent’s previously published
content, (ii) a personalized feed of recommended posts, and (iii) a
list of available actions the agent can perform.
Specifically, the feedback section provides the agent with insights
into how its previously published content was received by others.
This feedback is retrieved from the agent’s memory unit and in-
cludes raw posts along with their engagement metrics (e.g., the
number of re-shares, likes, dislikes, and comments received). The
recommended posts section simulates a social media feed, presenting
posts from other agents for potential interaction, such as liking,
disliking, sharing, or commenting, guided by a recommendation
algorithm that mimics existing social media recommender systems.
The actions’ list section outlines available actions: (i) publishing a

Can Generative Agent-Based Modeling Replicate the Friendship Paradox in Social Media Simulations? WEBSCI ’25, May 20-24, 2025, New Brunswick, New Jersey, USA
Post #1: @JoeBiden, We already know
@realdonaldtrump has no plan to protect
Americans from Covid-19 [...] that prove Trump's
incompetence
Post #2: @JoeBiden, At your first State of the
Union address, please consider inviting the families
of George Floyd. […] #BlackLivesMatter
Post #3: @realDonaldTrump has FAILED us. […]
#DumpTrump2020
Real User’s Contents
You have shared a variety of opinions on various topics related to
politics and current events. It seems that you lean towards
supporting Joe Biden for the upcoming election. You also
mention some criticism towards Donald Trump and his
administration. Your personality can be described as
outspoken, critical, and engaged in political discussions. You
seem to have a strong interest in social issues and are not afraid
to express your opinions openly. You appear to be passionate
about these topics. You are not afraid of engaging with others
who may hold different views.
Extracted Personality
Large Language
Model
Figure 1: Example of personality inference. LLMs analyze user’s generated content to extract personality traits.
Figure 2: The simulation workflow begins with the Initialization Phase, setting up agents with distinct personalities. In the
Operational Phase, agents autonomously decide their actions, such as posting or interacting with content. The Interaction
Phase updates the simulation environment. The process repeats iteratively until the stop condition is met.
new content, (ii) re-share, (iii) like, (iv) dislike or (v) comment posts
published by other agents, (vi) refraining from interaction.
The Operational Phase ends when the agent’s Reasoning Module
outputs the Choice-Reason-Content triplet for each agent.
Interaction Phase. The Interaction Phase enables agent inter-
actions, simulating a dynamic social network by updating three key
elements: (i) the follower-followee network, (ii) feedback on agents’
published content, and (iii) recommended content for potential
interactions.
First, the follower-followee network, represented as a global social
media graphG =(V,E), evolves dynamically through a "who to
follow" mechanism. In this process, agents are prompted to evaluate
potential new connections. To manage the limited context window
of LLMs, candidate suggestions are restricted to a subset of agents
identified via semantic similarity. Specifically, for a target agent
𝑎𝑖, the system calculates the average cosine similarity between the
semantic embeddings of 𝑎𝑖’s posts and those of other agents, select-
ing the top-10 agents with the highest similarity scores. Semantic
embeddings are computed using BERT [4].
Second, the Interaction Phase provides agents with feedback
on their previously published content, including metrics like re-
shares, likes, dislikes, and comments. This information is stored in
the agent’s memory unit, forming the basis for informed decision-
making in subsequent actions. By reflecting content engagement
and virality, this mechanism realistically simulates the influence of
community reactions on social media users.
Finally, recommended content is generated using a Retrieval-
Augmented Generation (RAG) strategy [7], which dynamically sug-
gests posts aligned with agents’ preferences. The retriever queries
an external vector database, updated continuously with all con-
tent published by agents in the simulation, ensuring relevant and
up-to-date recommendations. By decoupling retrieval from genera-
tion, the RAG approach maintains a stable prompt size, ensuring
scalability and consistent performance throughout the simulation.
Stop Condition. The iterative process betweenOperational Phase
and Interaction Phase continues until a predefined stop condition
is met. To mitigate the decline in content diversity observed in
LLM-empowered agents during repeated interactions [17], we de-
fine a saturation point determined by monitoring post similarity
across iterations, marking the point where agents cease generating
novel content. The simulation halts when 𝐿 original posts — cor-
responding to the number of agents — exhibit a cosine similarity
greater than 0.99 with prior content. This threshold ensures the
system stops only when redundancy dominates, signaling a lack of
substantive new contributions.
3 Experiments
Datasets. We assess our framework using two publicly available
Twitter datasets: (i) the US 2020 Election dataset [3], which captures
polarized discussions between liberals and conservatives during the
final months of the 2020 presidential campaign and its aftermath,
reflecting a broad and polarized discourse involving more than 1
million users; (ii) the QAnon dataset [11], which focuses on interac-
tions within the ideologically cohesive QAnon community leading
up to the January 6th Capitol riot [ 1], highlighting interactions
within a smaller, tightly-knit network of approximately 175,000
users. This diversity enables the examination of interactions within
individual communities as well as across polarized groups, demon-
strating the generalizability of our framework across varied online
environments.
Experimental setup . The experiments were conducted on a
computing system featuring an 11th Gen Intel Core i7-11800H
processor, 16 GB of RAM, and an NVIDIA GeForce RTX 3060 Lap-
top GPU. Agents were instantiated by annotating the political or
ideological affiliations of 100 users per dataset, categorized as Re-
publican or Democratic for the US election dataset and QAnon
promoters or non-promoters for the QAnon dataset. Simulations
concluded upon generating 100 repeated original contents, corre-
sponding to the number of agents, indicating a saturation point

WEBSCI ’25, May 20-24, 2025, New Brunswick, New Jersey, USA Orlando et al.
where all agents had, on average, contributed to content repetition.
The framework, implemented using PyAutogen [23], incorporates
ChromaDB∗ as the vector database for the agents’ memory unit
and the RAG technique, and employs the open-source Llama 3 8B
model†.
Measuring the Friendship Paradox . To examine the Friend-
ship Paradox and its generalizations, we analyze multiple metrics
reflecting social connectivity and influence dynamics. Specifically,
In-Degree (number of followers) and Out-Degree (number of fol-
lowees) quantify the agent’s social connections and enable the
verification of the Friendship Paradox as a property of the network
in its classical form: "on average, your friends have more friends than
you do" [6]. Metrics such as the Number of Tweets (NT), represent-
ing the number of posts generated by the agent (including both
original posts and re-shares), and Number of Original Tweets (NOT),
reflecting authored posts, measure activity and enable analysis of
the Activity Paradox. Then, Total Times Retweeted (TTR), which cap-
tures the total retweets received by the agent, andRetweets per Tweet
(RPT), the ratio of re-shares to original posts, quantify the agent’s
influence and address theVirality Paradox [12]. Lastly, theInfluence-
driven Adoption Rate (IAR), defined as the ratio of content shared
by the agent to the total content exposure, examines theSusceptibil-
ity Paradox, where an agent’s friends exhibit greater susceptibility
to influence than the agent itself [15]. We measured the Pearson
correlation coefficients among the above-mentioned attributes. The
correlations are generally low in magnitude, confirming that these
metrics capture distinct aspects of nodal characteristics.
The analysis of the Friendship Paradox and its generalizations
can be operationalized using the concept of neighbor superiority [8].
In a social media graphG =(V,E), whereV ={𝑎1, 𝑎2,··· , 𝑎𝑛} is
the set of agents andE ={(𝑎𝑖, 𝑎𝑗)|𝑎𝑖, 𝑎𝑗∈V} is the set of edges
representing follower-followee relationships, let𝑎𝑝 𝑖 denote the 𝑝-th
attribute of agent 𝑎𝑖, and 𝜂(𝑎𝑖) (resp. 𝛾(𝑎𝑖)) represent its followees
(resp. followers). For a fixed attribute 𝑝, agent 𝑎𝑖 experiences neigh-
bor superiority if 𝑎𝑝 𝑖 < E[𝜂(𝑎𝑝 𝑖)] (resp. 𝑎𝑝 𝑖 < E[𝛾(𝑎𝑝 𝑖)]), meaning
its followees (resp. followers) have higher average 𝑝 values. To
mitigate outlier effects, the comparison can be also compared to the
median of the neighbors’ values, offering a more robust measure of
neighbor superiority [16].
3.1 RQ1: Do the FP and GFP manifest in
GABM-based social media simulations?
We assess the prevalence of the Friendship Paradox and its gen-
eralizations by evaluating the percentage of agents experiencing
neighbor superiority . Table 1 presents the mean percentages of
agents experiencing neighbor superiority for each attribute across
all datasets, averaged over three independent simulation runs, with
standard deviations reported. For instance, in the US Election dataset,
an average of 86.33% of agents experiencemean followee superiority
for the in-degree attribute, indicating that for these agents 𝑎𝑖∈V ,
the inequality 𝑎in-degree 𝑖 < E[𝜂(𝑎in-degree 𝑖 )] holds. In contrast, only
41.33% of agents experience mean follower superiority for the same
attribute, i.e., 𝑎𝑖𝑛-𝑑𝑒𝑔𝑟𝑒𝑒 𝑖 < E[𝛾(𝑎𝑖𝑛−𝑑𝑒𝑔𝑟𝑒𝑒 𝑖 )]. Across all datasets
∗https://www.trychroma.com/
†https://ai.meta.com/blog/meta-llama-3/
Table 1: Percentage of agents experiencing mean neighbor
superiority. The results are averaged across three simulation
runs, standard deviation is in parenthesis. Bold indicates
cases where the proportion of agents experiencing mean fol-
lowee superiority exceeds that of agents experiencing mean
follower superiority.
US Election Dataset QAnon Dataset
Mean
Follower
(%)
Mean
Followee
(%)
Mean
Follower
(%)
Mean
Followee
(%)
In-Degree 41.33 (± 6.79) 86.33 (± 2.49) 19.33 (± 6.12) 82.33 (± 2.62)
Out-Degree 26.66 (± 5.43) 32.00 (± 6.97) 21.33 (± 5.43) 34.00 (± 0.81)
NT 48.33 (± 2.35) 35.33 ( ± 4.49) 32.00 (± 1.41) 52.66 (± 2.86)
NOT 48.66 (± 2.86) 44.00 ( ± 2.16) 30.00 (± 4.54) 60.33 (± 4.11)
TTR 48.00 (± 12.19) 78.33 (± 4.11) 31.66 (± 5.24) 81.66 (± 2.05)
RPT 50.00 (± 12.19) 81.66 (± 4.98) 29.66 (± 5.43) 81.33 (± 2.62)
IAR 41.33 (± 4.18) 75.66 (± 1.88) 33.00 (± 2.16) 62.33 (± 5.43)
and attributes, followee superiority consistently surpasses follower
superiority, a pattern observed in 12 of the 14 cases in Table 1. While
the analysis also holds when considering median neighbor supe-
riority, these results are omitted here for brevity. These findings
align with empirical results from real-world social networks [16],
indicating agents tend to follow others with higher nodal attributes.
This asymmetry suggests an implicit social hierarchy, reflecting
the tendency of agents to follow those with higher popularity and
activity.
3.2 RQ2: Which social connections most
contribute to experiencing the FP and GFP?
We now investigate which connections primarily drive the Friend-
ship Paradox and its generalizations for a generic agent.
To operationalize this concept, we restrict the sets of followers
and followees based on interaction frequency. Formally, let 𝜂(𝑎𝑖)| 𝑘
represent the top-𝑘 followers with whom agent 𝑎𝑖 has the high-
est interaction frequency, measured by re-shares, likes, dislikes
and comments. Similarly, 𝛾(𝑎𝑖)| 𝑘 denotes the top-𝑘 followees with
whom 𝑎𝑖 engages most frequently. We then analyze neighbor supe-
riority across three cases: (i) 𝜂(𝑎𝑖)| 𝑘=1 and 𝛾(𝑎𝑖)| 𝑘=1, considering
only the single most interactive follower or followee; (ii) 𝜂(𝑎𝑖)| 𝑘=3
and 𝛾(𝑎𝑖)| 𝑘=3, focusing on the top-3 most interactive connections;
and (iii) 𝜂(𝑎𝑖) and 𝛾(𝑎𝑖), examining the complete sets of followers
and followees. This approach evaluates the role of closest connec-
tions in driving the paradoxes.
Figure 3 shows the percentages of agents experiencing mean
follower superiority (Figures 3a–3b) and mean followee superiority
(Figures 3c–3d) for each attribute and restriction condition. For
example, in the US Election dataset, Figure 3c reveals an increasing
trend in followee superiority for the in-degree attribute (blue line).
Specifically, the paradox affects 72.33% of agents under 𝜂(𝑎𝑖)| 𝑘=1,
82.66% under 𝜂(𝑎𝑖)| 𝑘=3, and 86.33% for the full set 𝜂(𝑎𝑖). Similarly,
follower superiority (Figure 3a) rises from 37.33% under 𝛾(𝑎𝑖)| 𝑘=1,
increasing to 39.66% for 𝛾(𝑎𝑖)| 𝑘=3 and peaking at 41.33% when the

Can Generative Agent-Based Modeling Replicate the Friendship Paradox in Social Media Simulations? WEBSCI ’25, May 20-24, 2025, New Brunswick, New Jersey, USA
Mean Follower Superiority
(ai)|k = 1
 (ai)|k = 3
 (ai)
25
30
35
40
45
50Percentage of Agents
(a) US Election Dataset
(ai)|k = 1
 (ai)|k = 3
 (ai)
17.5
20.0
22.5
25.0
27.5
30.0
32.5Percentage of Agents
 (b) QAnon Dataset
Mean Followee Superiority
(ai)|k = 1
 (ai)|k = 3
 (ai)
30
40
50
60
70
80Percentage of Agents
(c) US Election Dataset
(ai)|k = 1
 (ai)|k = 3
 (ai)
30
40
50
60
70
80Percentage of Agents
 (d) QAnon Dataset
Figure 3: Proportion of agents experiencing mean follower
superiority and mean followee superiority for each attribute
across different restriction conditions.
full set 𝛾(𝑎𝑖) is considered. These increasing trends are consistent
across most attributes for mean follower values, being observed
in 17 out of 21 cases. In contrast, mean followee values exhibit
this trend in approximately half of the cases (10 out of 21). These
findings suggest that the Friendship Paradox and its variations are
not driven by an agent’s strongest connections (i.e., those with
the highest interaction frequencies). Instead, the connections that
contribute to the Friendship Paradox for a given agent primarily
involve agents with whom the target agent has less interactions.
This aligns with real-world findings [ 2], demonstrating that the
paradox in GABM simulations emerges through infrequent yet
impactful connections with highly influential agents.
4 Conclusion & Future Work
This paper introduces a GABM framework for simulating social me-
dia dynamics. The proposed generative agents, powered by modern
LLMs, emulate real-world users by integrating distinct personalities,
interests, dynamic social connections, and memory-based mecha-
nisms. The simulation workflow enables agents to perform typical
social media activities such as following, posting, re-sharing, liking,
disliking, and commenting. Using this framework, we investigated
the emergence of the Friendship Paradox and its generalizations,
including the Activity, Virality, and Susceptibility Paradoxes, in
GABM-based simulations. Experiments demonstrated that these
paradoxes naturally arise in these simulations, consistent with prior
findings in real-world social networks [2, 16]. Key findings include:
(i) agents exhibit hierarchical, preferential attachment behaviors,
connecting more frequently with individuals possessing superior at-
tributes such as higher activity or influence (RQ1), and (ii) the para-
doxes are primarily driven by infrequent connections rather than
the most frequently interacted connections (RQ2). These findings
validate GABM’s ability to replicate complex global phenomena
observed in real-world social networks.
Future work will focus on extending our study by addressing
two specific areas derived from our current findings. First, we aim
to investigate the temporal evolution of the FP and its variations
within simulations. Analyzing these temporal trends will provide a
deeper understanding of the conditions under which the paradox
emerges and stabilizes. Additionally, we plan to explore which
types of agents are most affected by the paradox. By pursuing these
directions, we aim to further establish GABM as a novel analysis
technique for social network analysis, enhancing its utility for
studying online behaviors and addressing critical challenges such
as misinformation and network polarization.
Acknowledgments
References
[1] Amarnath Amarasingam and Marc-André Argentino. 2020. The QAnon conspir-
acy theory: A security threat in the making. CTC Sentinel 13, 7 (2020), 37–44.
[2] James Bagrow, Christopher Danforth, and Lewis Mitchell. 2017. Which friends
are more popular than you? Contact strength and the friendship paradox in social
networks. (03 2017). https://doi.org/10.48550/arXiv.1703.06361
[3] E. Chen, A. Deb, and E. Ferrara. 2022. #Election2020: the first public Twitter
dataset on the 2020 US Presidential election. J. Comput. Soc. Sci. 5, 1 (2022), 1–18.
https://doi.org/10.1007/S42001-021-00117-9
[4] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT:
Pre-training of Deep Bidirectional Transformers for Language Understanding. In
Proceedings of the 2019 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, Volume 1 (Long and
Short Papers). 4171–4186.
[5] Abhimanyu Dubey et al . 2024. The llama 3 herd of models. arXiv preprint
arXiv:2407.21783 (2024).
[6] Scott L Feld. 1991. Why your friends have more friends than you do. American
journal of sociology 96, 6 (1991), 1464–1477.
[7] Antonino Ferraro, Antonio Galli, Valerio La Gatta, Marco Postiglione, Gian Marco
Orlando, Diego Russo, Giuseppe Riccio, Antonio Romano, and Vincenzo Moscato.
2024. Agent-Based Modelling Meets Generative AI in Social Network Simulations.
arXiv:2411.16031 [cs.SI] https://arxiv.org/abs/2411.16031
[8] Babak Fotouhi. 2014. Complex networks: dynamism of connectivity and opinion.
(2014).
[9] C. Gao, X. Lan, Z. Lu, J. Mao, J. Piao, H. Wang, D. Jin, and Yong Li. 2023. S3: Social-
network Simulation System with Large Language Model-Empowered Agents.
arXiv:2307.14984 (2023).
[10] Navid Ghaffarzadegan, Aritra Majumdar, Ross Williams, and Niyousha Hos-
seinichimeh. 2023. Generative agent-based modeling: Unveiling social system
dynamics through coupling mechanistic models with generative artificial intelli-
gence. arXiv preprint arXiv:2309.11456 (2023).
[11] Matthew N. Hannah. 2022. Collection of tweets related to QAnon hashtags.
https://doi.org/doi:/10.4231/32MD-DB04
[12] Nathan Hodas, Farshad Kooti, and Kristina Lerman. 2013. Friendship paradox re-
dux: Your friends are more interesting than you. InProceedings of the International
AAAI Conference on Web and Social Media , Vol. 7. 225–233.
[13] Matthew O. Jackson. 2019. The Friendship Paradox and Systematic Biases in
Perceptions and Social Norms. Journal of Political Economy 127, 2 (2019), 777–818.
https://doi.org/10.1086/701031 arXiv:https://doi.org/10.1086/701031
[14] Tse Yang Lim, Erin J Stringfellow, Celia A Stafford, Catherine DiGennaro, Jack B
Homer, Wayne Wakeland, Sara L Eggers, Reza Kazemi, Lukas Glos, Emily G
Ewing, et al. 2022. Modeling the evolution of the US opioid crisis for national
policy development. Proceedings of the National Academy of Sciences 119, 23
(2022), e2115714119.
[15] Luca Luceri, Jinyi Ye, Julie Jiang, and Emilio Ferrara. 2024. The Susceptibility
Paradox in Online Social Influence. arXiv preprint arXiv:2406.11553 (2024).
[16] Naghmeh Momeni and Michael Rabbat. 2016. Qualities and inequalities in online
social networks through the lens of the generalized friendship paradox. PloS one
11, 2 (2016), e0143633.
[17] Vishakh Padmakumar and He He. 2023. Does Writing with Language Models
Reduce Content Diversity? arXiv preprint arXiv:2309.05196 (2023).

WEBSCI ’25, May 20-24, 2025, New Brunswick, New Jersey, USA Orlando et al.
[18] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy
Liang, and Michael S Bernstein. 2023. Generative agents: Interactive simulacra
of human behavior. In Proceedings of the 36th annual acm symposium on user
interface software and technology . 1–22.
[19] Javier Pastor-Galindo, Pantaleone Nespoli, and José A Ruipérez-Valiente. 2024.
Large-Language-Model-Powered Agent-Based Framework for Misinformation
and Disinformation Research: Opportunities and Open Challenges. IEEE Security
& Privacy (2024).
[20] Petter Törnberg, Diliara Valeeva, Justus Uitermark, and Christopher Bail. 2023.
Simulating social media using large language models to evaluate alternative news
feed algorithms. arXiv preprint arXiv:2310.05984 (2023).
[21] Lei Wang, Jingsen Zhang, Hao Yang, Zhiyuan Chen, Jiakai Tang, Zeyu Zhang, Xu
Chen, Yankai Lin, Ruihua Song, Wayne Xin Zhao, et al. 2023. User behavior sim-
ulation with large language model based agents. arXiv preprint arXiv:2306.02552
(2023).
[22] Ross Williams, Niyousha Hosseinichimeh, Aritra Majumdar, and Navid Ghaf-
farzadegan. 2023. Epidemic modeling with generative agents. arXiv preprint
arXiv:2307.04986 (2023).
[23] Q. Wu, G. Bansal, J. Zhang, Y. Wu, B. Li, E. Zhu, L. Jiang, X. Zhang, S. Zhang, J. Liu,
A. H. Awadallah, R. W. White, D. Burger, and C. Wang. 2023. AutoGen: Enabling
Next-Gen LLM Applications via Multi-Agent Conversation. arXiv:2308.08155
(2023).
