---
title: Heterogeneous Multi-Agent Modeling for Measurement and Network Analysis of the Data Service Market
url: https://arxiv.org/abs/2605.27433
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Deyu Zhou
- Yuwei Guo
- Xudong Lu
- Linhao Zhang
- Wei Guo
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.27433
pages: 12
chars: 57785
fetched_at: '2026-11-08T12:58:09+00:00'
kb_version: 1
---

# Heterogeneous Multi-Agent Modeling for Measurement and Network Analysis of the Data Service Market

Heterogeneous Multi-Agent Modeling for
Measurement and Network Analysis of the Data
Service Market
Deyu Zhou1,2, Yuwei Guo 3, Xudong Lu 1,2, Linhao Zhang 1,2, Wei Guo 1,2, Lizhen Cui 1,2*
1 School of Software, Shandong University, Jinan, China
2 Joint SDU-NTU Centre for Artificial Intelligence Research (C-FAIR), Shandong University, Jinan, China
3 College of Intelligence and Computing, Tianjin University, Tianjin, China
Email: zhoudeyu@mail.sdu.edu.cn, 17860130125@163.com, dongxul@sdu.edu.cn,
linhaoz2022@163.com, guowei@sdu.edu.cn, clz@sdu.edu.cn
Abstract—With the increasing complexity of collaboration
among various social entities and user demands, the factors
affecting the stable development of the data service market
are also growing. These factors include the widespread dissem-
ination of information enhancing subjective consciousness, the
continuous improvement in intelligence, and the complexification
of structural relationships. To achieve effective governance and
regulation of the data service market, it is crucial to conduct
simulation experiments before making regulatory decisions. How-
ever, current research and analysis of the data service market
primarily focus on data-level performance, proving inadequate
when it comes to measurement and analysis of multiple hetero-
geneous entities and the integration of various social elements
within the data service market. Based on this, this paper
innovatively proposes a data service market measurement and
network analysis method based on heterogeneous multi-agent
modeling. By introducing the service ecosystem theory, we clarify
the participants and external factors of the data service market
and conduct utility measurements for three-level entities based on
value creation. Furthermore, an analytical methodology is devised
to precisely assess the influence of heterogeneous networks on
utility. Finally, the paper verifies the effectiveness of the proposed
method through the analysis of experimental results.
Index Terms—Data Service Market, Multi-agent System,
Agent-based Modeling (ABM), Network Analysis
I. INTRODUCTION
The data service market is a supply-demand matching
system in the modern service industry, which is driven by data
and provides digital customized services for market demands
through the division of labor and collaborative operation of
multiple individuals. As the social structure is redefined under
the logic of services [1], the data service market is gradually
transforming into a service ecosystem in which numerous
intelligent service entities (such as humans, institutions, soft-
ware robots, etc.) operate collaboratively [2]. It is no longer a
single market of the traditional data industry, but a multi-factor
integrated market that spans industries and meets various
demands [3].
* Corresponding author: Lizhen Cui; e-mail: clz@sdu.edu.cn;
The data service market includes the demand side, the
platform side, and the supply side. Their logical relationships
are shown in Fig.1. Customers on the demand side make ser-
vice requests through passive guidance or active exploration.
Model and data service providers on the service supply side
offer services [4]. The service platform side designs pricing
mechanisms and matches requests with supplies. Various intel-
ligent service entities have formed complex inter-relationships
through long-term competition and cooperation, and exhibit
adaptive behaviors to the environment.By measuring and op-
timizing service utility, the process of cooperation between
human agents and robot agents in the collective intelligence
space is regulated, and governance strategies are adjusted
accordingly, ultimately improving service quality and utility
[5], [6].
On one hand, the data service market is a bottom-up, self-
organizing, and self-growing complex system, where the over-
all state of the system depends on the spontaneous interactive
behaviors among different service entities [7]. On the other
hand, the data service market is also a product of top-down
planning, where managers can use patterns obtained from
various analytical methods to alter the design planning and
evolution path of the data service market [8]. Due to the
inherently low visibility of the service process, the visibility
of risks can easily be obscured at various stages, leading to
their accumulation until they eventually erupt. Therefore, how
to achieve effective monitoring and analysis of the data service
market has become a crucial issue for its sustainable and
healthy development [9].
As a complex and uncertain social system, the regulation
of the data service market exhibits dynamic and diversified
trends, which impose higher demands on research methods
[10]. Researchers mainly analyze service ecosystems through
data-driven statistical analysis method and agent-based model-
ing (ABM) [11], [12]. However, current research and analysis
of the data service market primarily focus on data-level per-
formance, proving inadequate when it comes to measure and
arXiv:2605.27433v1  [cs.MA]  22 May 2026

Fig. 1. The Operational Structure of Data Service Market
analyze of multiple heterogeneous entities and the integration
of various social elements within the data service market [13].
Based on this, in this paper, we innovatively propose
a measurement and network analysis method for the data
service market based on heterogeneous multi-agent modeling
from the perspective of service ecosystem. By modeling the
heterogeneous entities and their relationships, we define a
service utility measurement model for the data service market
[14]. Furthermore, a method for analyzing the impact of
heterogeneous networks on utility is established.
The rest of this paper is organized as follows: Section 1
presents the research background and motivation; Section 2
presents the measurement and network analysis methods for
data service market; Section 3 gives the construction and
design of experiments system about data service market, and
analyzes the experimental results; Section 4 concludes the
paper.
II. BACKGROUND ANDMOTIVATION
The influencing factors in the evolution process of the data
service market are complex and difficult to identify. They are
not only affected by human free will and subjective initiative
but can also change their evolutionary path due to occasional
events. Therefore, it is necessary to study its evolutionary
analysis methods. Currently, researchers commonly use the
following methods to analyze the data services market:
Data-driven Statistical Analysis: Big data lays more em-
phasis on application. It is a method of predicting phenomena
by collecting large amounts of data. Its drawback is that
although it can make predictions, it is difficult to explain the
predicted phenomena. This method continuously monitors sys-
tem operation data to detect potential faults or anomalies. For
example, statistical model-based anomaly detection techniques
construct a data model from all the data and identify outliers
as objects that do not fit the model perfectly. This method
is very challenging when studying complex systems that are
difficult to represent with mathematical models [15]. Based on
a systematic review of data market research literature, Abbas
et al. believe that the current understanding of the data service
market abroad is still unclear [16]. Technical research on the
data market mainly focuses on the construction of data trading
platforms, especially the application of blockchain. Mahajan
et al. proposed a blockchain-based data market development
method from the perspective of enhancing the capabilities of
data users [17].
Agent-based Modeling (ABM): Compared with data-
driven methods, ABM focuses more on theory. Its function
is to extract theories and put forward testable and falsi-
fiable hypotheses through computer simulation. It can not

only propose predictive hypotheses about phenomena but also
explain the phenomena and their causes through theory [18],
[19]. Agent-based modeling is very suitable for describing
the dynamic evolution process of complex systems. However,
there are some limitations in using ABM methods for service
ecosystem simulation modeling, such as the lack of research
on heterogeneous intelligent agent systems and the absence of
comprehensive metrics for system measurement during ABM
applications [20].
In the traditional industrial era, enterprises embedded value
into products during the production process and realized value
transfer and appreciation through market transactions [21],
[22]. Vargo et al. proposed the concept of service ecosystem,
believing that the service ecosystem is a self-regulating and
relatively independent system formed by loosely coupled
participants connected by institutions and value co-creation
mechanisms [23], [24]. Besides, with the development of
the internet technologies, social networks have become an
indispensable part of human daily life. People share infor-
mation, establish connections, and obtain services through
social networks. Researchers have begun to explore how to use
graph theory and complex network analysis methods to model
the relationships between service providers and customers in
social networks [25]. They describe entities as nodes and study
their interactions through edges in the social network [26].
These methods have revealed some characteristics and patterns
of complex adaptive systems in social networks.
Current research methods prioritize prediction over expla-
nation, making it difficult to reveal the underlying mechanisms
of the data service market’s evolution and lacking a systematic
characterization of heterogeneous intelligent agents within
the service ecosystem [27]–[29]. To address the limitations
of existing analysis methods in studying the data service
market, this paper proposes a data service market measurement
and network analysis method based on heterogeneous multi-
agent modeling. From the perspective of service ecosystem,
this method clarifies the participating entities, value creation
patterns, and external elements of the data service market.
On this basis, a service utility measurement model and a
heterogeneous agent collaboration model based on complex
networks are defined.
III. MEASUREMENT ANDNETWORKANALYSISMETHOD
FOR THEDATASERVICEMARKET
This section addresses the challenges of complexity repre-
sentation and system complexity assessment of heterogeneous
entities in the data service market by modeling and measuring
heterogeneous multi-level agents. Finally, a method for ana-
lyzing the impact of heterogeneous networks based on service
utility is designed [30], Table I summarizes the important
indicators.
TABLE I
KEY INDICATORS USED IN MEASUREMENT AND NETWORK ANALYSIS FOR
THE DATA SERVICE MARKET.
Indicator Explanation
N∆t(t)The number of order arrivals within the interval
[t, t+ ∆t].
U dem(∆t)The utility on the demand side at timet.
Dop(t)The platform’s decision objective.
U collab(o)The collaboration utility for an orderoexecuted by
an agent set.
Ur The individual utility of robotr.
Up The individual utility of business agentp.
UG The organizational utility ofG.
Usys The system utility at the platform level.
A. Structure-constrained Heterogeneous Agent Modeling in
Data Service Market
From the perspective of service ecosystems, the evolution
of the data service market is based on supply and demand
matching. The system includes the service demand side,
service supply side, and service operation side [7], [31], [32].
In the data service market, the purpose of measurement and
analysis is to better govern the service system on the supply
side. Therefore, the nodes on the demand side are regarded as
the external market environment and are represented by the
demand fluctuation sequence, while the agents in the service
system on the supply side are the focus of modeling. The
modeling of data service market from these three aspects is as
follows:
•Demand-side Modeling
Demands are manifested as a stream of user orders arriving
over time. To characterize demand uncertainty and hetero-
geneity, we consider the inter-arrival pattern of orders, the
order volume within a time window, and the composition
and complexity of orders, including order types, processing
difficulty, and the proportion of different categories.
We model order arrivals using queuing theory and assume
that the number of orders arriving within a short time window
follows a Poisson process. To regulate the workload injected
into the system, we introduce a user-adjustableorder arrival
ratethat controls the expected number of arrivals per unit time:
N∆t(t)∼Poisson (λ(t)∆t),(1)
where,λ(t)is the order arrival rate at timet, and∆tis
the window length. The functionλ(t)can be specified as a
constant (stationary demand) or a time-dependent profile (non-
stationary demand) to capture peak hours, bursts, or periodic
fluctuations.
Given the arrivals, we generate order attributes via Monte
Carlo sampling to reflect heterogeneity in order types and
processing requirements. Specifically, for each arriving order,
we sample its type, difficulty, and other features from pre-
defined distributions, and the proportions of different types
are controlled by scenario parameters. When historical order
data are available, we estimate the empirical distributions
(or fit parametric forms) from real observations and then
sample accordingly, enabling data-driven simulation of order

fluctuations and composition. When real data are unavailable,
we adopt synthetic yet controllable distributions by specifying
a fluctuation function forλ(t)(e.g., sinusoidal or piece-
wise functions) and selecting plausible priors for order-type
proportions and difficulty, which together produce scenario-
consistent demand streams for computational experiments.
The duration and quality of order completion can be used
to represent how well the system performs the task, while the
time and cost spent by the system to complete all incoming
orders can measure the overall capability. We define demand
side utility as a “quality–time–cost” trade-off:
U dem(∆t) =E[q(o)−λ T T(o)−λ CC(o)](2)
where,odenotes an incoming order during∆t;q(o)represents
the service quality obtained from completing ordero;T(o)is
the processing time of ordero;C(o)denotes the processing
cost;λ T andλ C are penalty coefficients associated with
time and cost, respectively;E[·]takes expectation over order
arrivals.
•Operation-side Modeling
The operation side refers to the system management plat-
form agent, which coordinates and controls the entire system,
receives orders from external sources, allocates orders to
different institutions for processing, and calculates total cost
and revenue to evaluate overall utility. The platform’s decision
objective is modeled as:
Dop(t) =R(t)−η 1 T(t)−η 2 Ω(t),(3)
where,R(t)is the total revenue (or value) obtained from
processed orders; T(t)denotes the average order processing
time;Ω(t)is a load imbalance term across institutions (e.g.,
variance of occupancy); andη 1, η2 are penalty coefficients.
The platform assigns orders to institutions by prioritizing
allocation according to institutional occupancy levels, while
jointly considering order complexity as well as robot and
business agent utilization. Accordingly, this decision logic is
formulated as a structure-constrained assignment problem:
xo,i = arg max i∈I (ˆuo,i −κ r ρr i (t)−κ e ρe i (t)),
s.t.
X
i∈I
xo,i = 1. (4)
where,Idenotes the set of institutions;x o,i ∈ {0,1}indicates
whether orderois assigned to institutioni;ˆu o,i represents the
estimated utility if institutioniprocesses ordero(reflecting
order difficulty, expected processing time, and cost);ρ r i (t)and
ρe i (t)denote the robot and business agent occupancy rates,
respectively; andκ r, κe are penalty weights.
•Supply-side Modeling
The supply side is the main body of the system, forming
a multi-organization and multi-agent system where different
organizations collaborate to fulfill orders. The supply side
includes secondary entities (organizations) and primary en-
tities within organizations (high intelligence business agents
and low-intelligence software robot agents). Organizational
agents receive orders allocated by the platform; orders can
be transferred between organizations. Within each organiza-
tion, intelligent agents collaborate to handle system orders.
High-intelligence agents handle higher-difficulty orders but
consume more cost and time, while low-intelligence agents
process quickly at lower cost but can only handle less difficult
orders [33]. Embeddingstructure-constrained collaboration,
we define the collaboration utility of orderoexecuted by an
agent setA o as:
U collab(o) = X
a∈Ao
ua(o)−ϕ|A o|,(5)
where,A o denotes the collaborating agent set;u a(o)is the
individual utility contribution of agenta;|A o|is the number of
collaborators; andϕis the coordination overhead coefficient,
capturing communication and coordination costs. The collabo-
ration must satisfy structural constraints induced by capability
thresholds and availability:
d(o)≤θ r ⇒a∈ A o ∩ Ris feasible,
d(o)> θr ⇒a∈ A o ∩ Bis required,
ρa(t)<1,∀a∈ A o,
(6)
where,d(o)denotes order difficulty;θ r is the robot capability
threshold;RandBdenote the robot-agent set and business-
agent set, respectively; andρ a(t)is the occupancy rate of agent
aat timet(which must be less than1for availability).
B. Utility Measurement Model of Data Service Market
Heterogeneous agents create value through order process-
ing. To quantitatively evaluate system utility, an effective-
value-based utility measurement model is introduced. Different
from coarse-grained evaluation limited to the organizational
or platform level, system utility is decomposed into primary-
entity utility, organizational utility, and platform-level utility,
forming a consistent multi-level measurement framework [34].
The value created by the agents is a major source of system
cost and revenue.
•Primary Entity: Individual Utility
Individual utility reflects the execution capability and effi-
ciency of an agent during order processing. A higher individual
utility indicates that collaborative orders can be completed in
a shorter time, thereby reducing the actual delivery time of
an order and improving order fulfillment quality and customer
satisfaction. Software robot agents create effective value by
completing orders while simultaneously incurring maintenance
costs [35]. Accordingly, the individual utility of a robot is
defined as:
Ur =
X
o∈Or
 RhP Ah ·O dv(o)  −C r,(7)
where,O r is the set of orders processed by robotr;R h
represents the workload completed by robotrin ordero;P Ah denotes the total workload completed by all agents
participating in ordero;O dv(o)represents the complexity or
value of ordero;C r denotes the maintenance cost incurred by

robotrwithin a service cycle. Business agents create effective
value through order processing. Accordingly, the individual
utilityU p of a business agents is defined as [36]:
Up =B+
X
o∈Op
 PhP Ah ·O dv(o)·O vr  ,(8)
where,Brepresents the base income of the business agent;O p
denotes the set of orders processed by business agentp;P h is
the workload completed by business agentpin ordero; P Ah
denotes the total workload of ordero;O dv(o)represents the
value or complexity of ordero;O vr denotes the conversion
coefficient that maps order value to income.
•Secondary Entity: Organizational Utility
Organizational utility characterizes the overall operational
performance of an organization over a service cycle [37]–
[39]. It is jointly determined by the total effective value
created by internal agents and the organizational operating
costs. The created value of organizationGis defined as the
total complexity-based value of the orders it processes:
CV G =
X
o∈OG
Odv(o),(9)
where,O G denotes orders set processed by organizationG.
The organizational cost consists of robot maintenance costs
and business agent compensation:
CG =
X
r∈RG
Cr +
X
p∈PG
Up,(10)
where,R G andP G denote the sets of robots and business
agents within organizationG, respectively;C r represents the
maintenance cost of robotr; andU p denotes the income
of business agentp, which is regarded as an organizational
expense [40]. The organizational utility of organizationGis
finally defined as:
UG =CV G ·G vr −C G,(11)
whereG vr is the organization value conversion coefficient.
•Tertiary Entity: System Utility
The platform is the operator of the service system, service’s
utility can help platform agent adjust system parameters. In
this work, system utility is evaluated at the platform level,
while agent-level and organizational-level utilities affect sys-
tem utility implicitly through delivery efficiency and opera-
tional cost. Under the above mechanism, system utilityU sys
at the platform level can be uniformly expressed as:
Usys =
X
o∈O
Odv(o) Te(o) Trly (o) − X G∈G CG(EG),(12)
where,Odenotes the set of all orders in the system;O dv(o)
represents the complexity or intrinsic value of ordero;T e(o)
denotes the average processing time of historical orders
with comparable complexity, serving as a reference baseline;
Trly (o)denotes the actual completion time of ordero, which
is a function of the individual utility set{U a}a∈Ao and the
organizational utility set{E G}G∈G, reflecting the combined
influence of individual execution efficiency and organizational
coordination on delivery performance;Gdenotes the set of
organizations in the system;C G(EG)denotes the operational
cost of organizationG, which is modeled as a function of
organizational utility, reflecting resource consumption, main-
tenance overhead, and collaboration costs.
In implementation, the realized completion timeT rly (o)
is computed by a workload–capacity–congestion mechanism,
where individual utility affects effective processing speed and
organizational utility affects the congestion multiplier. Specif-
ically, the order workload is mapped from order difficulty,
while the effective processing rate of each agent is determined
by its baseline capability and individual utility [41]–[43]. In
addition, collaboration size and average occupancy introduce
multiplicative delay factors that capture coordination overhead
and congestion effects.
Trly (o) = W(o)P
a∈Ao sa
·(1 +λ ρ ¯ρAo )·(1 +λ c (|Ao| −1)),
(13)
where,W(o) =ω 0 +ω 1 Odv(o)denotes the workload of order
o, which is mapped from its complexity.ω 0, ω1 >0are scaling
coefficients.A o is the set of agents collaborating on ordero,
ands a represents the effective processing rate of agenta.¯ρ Ao
denotes the average occupancy of the agents inA o, which
reflects the workload pressure or resource utilization level of
the collaborating agents when processing ordero. The effective
processing rate of agentais defined as:
sa =s 0 a ·  1 +λ u ˜Ua  ,(14)
wheres 0 a is the baseline processing rate of agenta(which
may differ between robots and human employees), andλ u ≥0
controls the influence of individual utility on processing speed.
The normalized individual utility ˜Ua in Formula 14 is given
by:
˜Ua = Ua −min(U) max(U)−min(U) +ϵ ,(15)
where,ϵis a small positive constant to avoid division by zero.
The average occupancy of the collaborating agent set¯ρ Ao in
Formula 13 is defined as:
¯ρAo = 1 |Ao| X a∈Ao ρa(t),(16)
whereρ a(t)∈[0,1]denotes the occupancy rate of agent
aat timet. The coefficientλ ρ ≥0captures congestion
amplification due to high resource utilization, whileλ c ≥0
represents the coordination overhead introduced by collabora-
tion, increasing with the number of agents.
C. A Structure-Constrained Network Analysis Method for Ser-
vice Utility Evaluation
This section develops a network-centric analysis method to
research how heterogeneous interaction structures influence
service utility in data service markets [44]. We model the
service ecosystem as an interaction network as follows:
W= (N,E),(17)

where, nodesNrepresent service agents (human employees or
robots), and edgesEdenote collaboration relationships estab-
lished during service execution. The network structure serves
as a structural constraint space, shaping feasible interaction
patterns, coordination costs, and information flow efficiency.
LetN=|N |be the total number of agents. The interaction
structure at timetis characterized by an adjacency matrix
At =

aij(t)

∈ {0,1}N×N ,(18)
where,a ij(t) = 1indicates an active collaboration between
Agentiand Agentj. The degree of an agentk i(t)measures
collaboration capacity, reflecting ability to share workload, ex-
change information, and participate in joint service execution.
ki(t) =
NX
j=1
aij(t),(19)
At the system level, structural statistics such as average
degree ¯k, clustering coefficient, and path length collectively
determine the interaction efficiency and coordination overhead
of the service network. For the data service market, collabora-
tion is inherently dynamic and history-dependent. We quantify
the cooperation intensityP ij between agentsiandjas
Pij = Nij 1
T
PT
t=1 N (t) ij ,(20)
where,N ij denotes the number of completed service interac-
tions between the agent pair, andTis the total number of
repeated runs. This formulation captures long-term collabo-
ration stability, serving as a weighted interpretation of edges
inG, and bridges the network structure with realized service
outcomes.
Under structural constraints imposed by the interaction
networkW, the platform allocates a task setTto agents and
produces a collaboration outcome
x=A(T,W),x={x it},(21)
wherex it denotes the assignment outcome of agention task
t. For each agenti, the effective service capability is not a
constant, but is modulated by the network:
˜si =s i ·ϕ i(W), ϕ i(W) =
X
j
aijPij,(22)
wheres i is the baseline capability,ϕ i(W)is a network-
induced collaboration amplification factor,a ij indicates
whetherican interact withjinW, andP ij denotes the
interaction (or collaboration) strength/probability. Thus,W
directly shapes “who can do what” and “to what extent” in
the mechanism.
IV. EXPERIMENTALSYSTEM OF THEDATASERVICE
MARKET
We conducted extensive experiments to address a series of
research questions regarding the method proposed in this paper
[29]: It is mainly used to address a series of research questions:
•RQ1:Can the proposed service utility measurement method
evaluate the data service market more stably and effectively?
•RQ2:How do collaboration patterns under different net-
work structures influence the service utility of the data
service market?
A. Experimental System Construction
The data service market is focused on the digital government
system in our work, primarily describing the interaction behav-
iors and processes between service entities and the relationship
between service entities and public demands. Citizens can use
digital platforms to query government information, apply for
administrative permits, or submit feedback. The government
community processes and responds to these requests via the
digital platform and provides corresponding services based on
rules and processes. By modeling the operational mechanisms,
processes, and relationships among participants in the digital
government system, guidance can be provided for designing
and improving digital government systems to enhance citizen
engagement, service quality, and government utility.
Fig. 2. The Experimental Architecture of Data Service Market
As shown in Fig.2, the system involves five major compo-
nents: “Orders”, “Platform”, “Government Agencies”, “Sales-
man Agents”, and “Robots”. Each component needs to be
designed as a distinct entity class. The system currently
includes 8 government Agencies (i.e.,Institutions), each insti-
tution builds a collaborative structure corresponding to each
network model, labeled A through H. Agency A can only pro-
cess orders of type A, and so on. These institutions collaborate
to complete customer orders. Each institution initially has 12
agents: 4 salesman agents (i.e., P1,P2,P3 and P4) and 8 robots.
They work together to process system orders. Salesman agents
can handle more difficult orders but incur costs and have
slower processing speeds, while robots process orders quickly
but can only handle less difficult orders. Orders originate from
outside the system and come in eight basic types: A, B, C,
D, E, F, G, and H, as well as their random combinations. For

example, BA type orders are equivalent to AB type orders, and
so forth. Additionally, each order type has different levels of
complexity. The complexity of an order indirectly represents
its value.
Different organizational and market conditions give rise to
heterogeneous interaction topologies, which are modeled as
structural priors:Isolated Network:Agents operate indepen-
dently (k i = 0), minimizing coordination cost but severely
limiting collaborative capacity.Globally Coupled Network:
Fully connected structure enabling maximal collaboration, at
the expense of high communication and coordination over-
head.Star Network:A centralized topology where a hub
agent mediates interactions, introducing structural asymmetry
and potential bottlenecks.One-Dimensional Ring:Agents
form a ring network, where each Agent can only form co-
operative relationships with its two adjacent Agents.G(N,L)
Random Network:There areNagent nodes are connected
by randomly placed links. Where,0≤L≤ N(N−1) 2 ,
initiallyLis set toN(N−1)/8.WS Small-World Network:
Consider a nearest-neighbor coupled network withNnodes
arranged in a ring, where each node is connected toK/2
nodes on its left and right (K is even). The parameters satisfy
N≫K≫lnN≫1. Then, with probabilityp, each edge
in the network is randomly reconnected, i.e., one endpoint
of the edge remains unchanged while the other endpoint is
replaced with a randomly selected node in the network. The
small-world network specifies that there should be no multiple
edges or self-loops.NW Small-World Network:Similarly,
in a K-nearest neighbor network, an edge is added between
a randomly selected pair of agent nodes with probabilityp.
This addition of edges also ensures that there are no multiple
edges or self-loops in the network.BA Scale-Free Network:
Starting from a network withm 0 nodes, each time a new
node is introduced, it connects tomexisting nodes, where
m≤m 0. The probabilityΠ i that the new node connects to
an existing nodev i is proportional to the degreek i of node
vi , i.e.,Π i = kiP
j kj . Aftertsteps, this algorithm produces a network withN=t+m 0 nodes andm t edges. Initially,
the network is set to have two nodes, and each new node is
connected to two existing nodes according to the preferential
attachment mechanism.
B. Parameter Settings
By fitting the order distribution pattern on zbj.com, a digital
service platform in reality, we take it as the order fluctuation
data on the demand side of the data service market. Based on
this, parameters about environment that can be designed for
the system environment include [45]:1)Order Generation:
The order quantity distribution based on real data is shown in
Fig. 3.2)Order Type: It is generated evenly corresponding to
8 types of institutions.3)Order Complexity: Using numeric
Input Box, it allows input of positive integers only, with a
minimum value of 1 and a maximum value of 3.4)Order
Arrival Rate: It represents the average number of orders
arriving per unit of time. Set between 0.5 and 10, allowing
both integers and decimals.5)Cycle Duration: It allows
input of positive integers only, with a minimum value of 60
and a maximum value of 240 (The default setting is 120).
These parameters can be adjusted appropriately according to
experimental requirements.
Fig. 3. The Order Arrival Distribution
ForRQ1, we compare the proposedsystem utility-based
measurement (U sys) with representative alternatives that are
commonly adopted in service evaluation and information
systems assessment. Specifically, we consider the following
baselines: (i)DeLone & McLean (D&M)[46]: a system-
success proxy constructed from observable variables (e.g.,
service quality, usage/intention, and net benefits) to approx-
imate the classic information systems success model; (ii)QoS
Utility (QoS)[47]: a traditional service-computing baseline
that maps QoS attributes into a utility function and aggregates
them with fixed weights, emphasizing performance-driven
evaluation; (iii)Serv-qual proxy (SaL)[48]: a service-quality
baseline inspired by the expectation and perception gap, used
to approximate perceived service quality in a measurable way.
We report a unified set of outcome factors derived from the
same simulation logs and standardize them to a common[0,1]
scale with consistenthigher-is-bettersemantics. For cost-type
metrics we further reverse the normalized value so that larger
scores indicate better performance. (i)IL(Inverse Latency),
a standardized delay score derived from the mean realized
latency T rly ; (ii)T rly(Inverse Delay Std), a stability score
obtained by reversing the standard deviationstd(T rly ); (iii)
SuS(Success Rate), the proportion of orders successfully
completed (or satisfying the speedup constraint), reflecting
reliability; (iv)Sp(Speedup), the average acceleration ra-
tio (e.g.,T e/Trly), reflecting efficiency improvement over
the baseline processing time; (v)LG(Load Gini Score),
a reversed Gini-based score computed from institution-level
processed value, where higher scores indicate lower load
imbalance; (vi)F air(Fairness Gini Score), a reversed Gini-
based score computed from individual utilities, where higher
scores indicate better fairness among participants. Finally, we
compute anOverallscore by averaging the above normal-
ized factors, yielding a composite measure for cross-method
ranking.

ForRQ2, we investigate how differentcollaboration net-
work structuresaffect the service utility of the data service
market under thesameorder stream and identical entity set-
tings. We treat each network topology as a structural baseline
and compare the resulting performance at theindividual,
organizational, andsystemlevels. Specifically, we consider
eight representative collaboration topologies deployed within
each institution (i.e.,GovA: Isolated Node Network;GovB:
Globally Coupled Network;GovC: Star Network;GovD: One-
Dimensional Ring;GovE: G(N,L) Random Network;GovF:
WS Small-World Network;GovG: NW Small-World Network;
GovH: BA Scale-Free Network). These topologies provide
a controlled spectrum from no collaboration links to fully
connected collaboration, as well as structured and stochastic
networks with shortcuts or hubs. All other factors (order
arrivals, agent costs and capabilities, and the time-generation
mechanism) are fixed so that any observed differences can
be attributed to network structure rather than environmental
variation. Following the multi-layer measurement framework,
we evaluate the impact of network structure using quantitative
metrics at three levels. At theindividual level, we report the
mean individual utility U ind and its dispersionσ(U ind)to
capture both effectiveness and stability of participants’ out-
comes; we further compute the inequality of individual utility
via the Gini coefficientGini i. At theorganizational level,
we report the mean organizational utility U org and the relative
improvement Gains(%) with respect to the reference topology,
reflecting the organization-level value creation under different
collaboration patterns. At thesystem level, we report the
overall system utility U sys together with its dispersionσ(U sys)
to assess market-level efficiency and robustness. Finally, we
provide aRankover topologies based on the system-level
outcomes (with higher U sys and lowerσ(U sys)preferred),
enabling a direct comparison of how structural choices shape
service utility under the same experimental conditions.
C. Analysis of Experimental Results
1) Analysis of Service Utility Measurement Method (RQ1)
:RQ1 investigates whether the proposed system utility mea-
surementU sys can evaluate the data service market morestably
andeffectivelythan representative alternatives. To this end, we
compareU sys with three widely adopted baselines, including
the DeLone & McLean proxy (D&M), the QoS-utility baseline
(QoS), and the Serv-qual proxy (SaL). All methods are eval-
uated underidenticalorder streams, identical entity settings,
and the same time-generation mechanism; only themeasure-
ment criterionis changed. This protocol guarantees that any
performance differences are attributable to the measurement
method rather than environmental variation. The key novelty
ofU sys lies in itscross-layer consistency: it unifies individual-,
organizational-, and system-level contributions into a coherent
platform-level objective, thereby producing a measurement
that is simultaneously performance-sensitive, cost-aware, and
stability-oriented.
Table II reports the normalized comparison results with
consistenthigher-is-bettersemantics. Among all compared
methods,U sys achieves the highest Overall score (0.83), out-
performing both D&M and QoS (each0.80) and substantially
exceeding SaL (0.69). This indicates thatU sys provides the best
balanced assessment across reliability, efficiency, and equity-
related dimensions, rather than optimizing a single aspect at
the expense of others. Fig. 4 further evaluates the stability
of each measurement method under different collaboration
network environments. Across these heterogeneous topologies,
Usys maintains consistently competitive stability scores without
the pronounced drops observed for the baselines in certain net-
work settings. Such robustness is crucial for data service mar-
kets where collaboration patterns and interaction constraints
can vary significantly. The stability advantage aligns with our
structure-aware modeling and multi-layer utility design: by
embedding realized delivery time and coordination effects into
utility accounting,U sys remains reliable even when network-
induced coordination and occupancy change.
TABLE II
COMPARISON OFMEASUREMENTMETHODS.
Method IL Trly SuS Sp LG Fair Overall
D&M 0.97 0.95 0.81 0.98 0.910.97 0.80
QoS 0.97 0.95 0.81 0.98 0.90 1.000.80
SaL 0.76 0.571.000.900.910.58 0.69
Usys 0.99 1.000.94 1.000.86 0.98 0.83
Note.Best in each column is inboldand second is underlined .
Fig. 4. The Stability Comparison of Various Measurement Methods under
Different Network Environments
A closer inspection of the factor-wise results in Table II
explains whyU sys dominates the composite score. First, on
latency-related dimensions,U sys attains the best performance
on bothIL(0.99) andT rly(1.00), implying lower mean
latency and higher delivery stability. This is becauseU sys
explicitly internalizes realized delivery time into the platform-
level value, discouraging inefficient collaboration patterns that
incur excessive coordination overhead or congestion-amplified
delays. Second, on reliability and efficiency,U sys achieves
the best success rateSuS(0.94) and speedupSp(1.00). In

contrast, D&M and QoS reach the same moderateSuSlevel
(0.81), while SaL achieves the highestSuS(1.00) but does
not translate this into a balanced advantage in other dimen-
sions. This highlights that reliability alone is insufficient; an
effective market-level measurement must also reward efficient
and stable fulfillment. Third, on equity-related dimensions,
Usys maintains strong fairness withF air= 0.98while
keeping a high load-balance scoreLG= 0.86. Notably, SaL
performs well onLG(0.91) but poorly onF air(0.58), sug-
gesting that perceived-quality-oriented proxies may encourage
allocations that appear balanced at the institution level but still
yield inequitable outcomes among individuals. QoS attains the
best fairness score (F air= 1.00) but does not dominate in
stability and latency-related metrics, reflecting the limitation
of purely QoS-driven aggregation when coordination and
congestion effects are present.
In summary, the results confirm that the proposedU sys
provides a more stable and effective evaluation for the data
service market than representative baselines. In particular,
Usys achieves the highest composite score and exhibits strong
robustness across heterogeneous collaboration networks, vali-
dating that our multi-layer utility decomposition and structure-
aware modeling yield a faithful and actionable measurement
method under realistic network variability.
2) Analysis of Network Structure Impact on Service Util-
ity (RQ2):This subsection investigates how collaboration
topologies structurally constrain coordination processes and
consequently shape service utilities at the individual, organi-
zational, and system levels. Table III reports the key statistics
(mean, dispersion, Gini, and rank), while Fig. 5-Fig. 8 further
visualize individual utility distributions, organizational utility
accumulation, temporal system dynamics, and robustness.
Individual-level utility: centralization inflates the mean but
harms fairness; WS small-world is best in stability and equity.
At the individual level, GovC (Star) attains the largest mean
individual utility ¯Uind = 492.595, yet it exhibits severe
inequality (Gini= 0.496) and extremely high dispersion
(σ(Uind) = 648.359), reflecting a hub-dominance “rich-get-
richer” effect. Fig. 5 shows clear polarization under the star
structure, implying that a high mean may be driven by a
few beneficiaries rather than broad improvement. By contrast,
GovF (WS Small-World) is best in both stability and fairness,
achieving the smallestσ(U ind) = 10.263and the smallest Gini
= 0.024. GovB (Globally Coupled) is second-best in fairness
(Gini= 0.040) and keeps dispersion low (σ= 24.680),
highlighting how dense connectivity promotes opportunity
equalization and risk diversification. These findings align with
our structure-constrained collaboration modeling: topology
governs not only average payoffs but also the distribution and
propagation of volatility.
Organizational-level utility: globally coupled yields the
highest institutional utility, followed by small-world. Fig. 6
and Table III show that GovB (Globally Coupled) remains
the best at the organizational level with ¯Uorg = 4555.205,
corresponding to the upper envelope of the accumulation
trajectories. GovF (WS Small-World) is second-best ( ¯Uorg =
Fig. 5. The Individual Utility of Salesman Agents in Different Government
Agencies
Fig. 6. The Organizational Utility of Institutions in Data Service Market
4240.275), and the Gains(%) values (7.4 for GovB and 1.2 for
GovF) further support the ranking. This suggests that multi-
path reachability and load balancing enhance order matching
and collaboration efficiency, thus accumulating higher insti-
tutional value. Conversely, GovA (Isolated) is substantially
worse ( ¯Uorg = 2179.753), confirming that missing collabora-
tive links prevent institutions from benefiting from scale effects
and complementary division of labor.
System-level utility: global coupling dominates; small-
world is a robust near-optimal alternative. As shown in Ta-
ble III and Fig. 8, GovB (Globally Coupled) achieves the high-

est mean system utility, ¯Usys = 75083.970(Rank 1), consistent
with the top “global” distribution in the boxplot. This indicates
that dense connectivity maximizes reachability and cross-
agent resource sharing, lifting the upper bound of system-wide
matching efficiency. GovF (WS Small-World) and GovG (NW
Small-World) form the second tier with ¯Usys = 55456.279
(Rank 2) and54472.563(Rank 3), respectively. By combining
local clustering with a small number of long-range shortcuts,
small-world structures shorten functional paths and mitigate
localized congestion without requiring full connectivity, yield-
ing a favorable efficiency–cost trade-off. In contrast, GovA
(Isolated) is the worst ( ¯Usys = 20528.649, Rank 8) and
GovC (Star) is also low (22574.292, Rank 7), suggesting that
insufficient connectivity (isolated) or hub bottlenecks (star)
fundamentally limit throughput and collaboration gains.
Fig. 7. The System Performance Over Time
Regarding system variabilityσ(U sys), GovC (Star) is the
smallest (1047.402) and GovA (Isolated) is second (1123.526),
yet both have low mean system utilities (Rank 7/8). This
shows that low variance does not necessarily imply high
effectiveness: star networks may operate stably at a low
throughput due to centralized scheduling bottlenecks, while
isolated structures cap collaboration gains by design. As shown
in Fig. 7, although transient perturbations occur frequently
with order arrivals, the system utility fluctuates within a
bounded range and quickly reverts to its mean level, indicating
short-lived shocks rather than persistent drift across network
structures.Fig. 8 further indicates temporal responses under
workload fluctuations; globally coupled and small-world net-
works better absorb localized congestion thanks to alternative
paths, maintaining higher-utility regimes more robustly.
In Summary, we observe consistent structure–collaboration–
performance regularities: (i) Globally Coupled is best at the
system and organizational levels; (ii) Small-World provides
a robust near-optimal alternative; (iii) Star inflates individual
mean utility but severely harms fairness and stability; and
(iv) Isolated suffers from limited collaboration gains. These
results validate the proposed multi-level utility decomposition
and structure-constrained collaboration modeling, enabling
Fig. 8. The System Utility with Different Networks
topology comparison together with explainable diagnosis of
fairness, volatility, and bottleneck mechanisms for governance-
oriented network design.
V. CONCLUSION
The research presented in this paper introduces an inno-
vative approach to understanding and analyzing the complex
dynamics of data service markets through the lens of service
ecosystems. By developing a comprehensive modeling, mea-
surement and network analysis method, this study addresses
the challenges about measurement posed by the intricate
interactions nature of agents within these markets. In the
future, the process of researching collaboration models in the
data service market needs to further consider the collaboration
costs of three-level entities. In addition, based on the research
results of this article, further explore the impact of other factors
in the data service market on the collaboration process and
incorporate more complex behaviors of agents.
ACKNOWLEDGMENT
This work was supported by the National Natural Science
Foundation of China (No.92367202).
REFERENCES
[1] C. Gr ¨onroos and J. Gummerus, “The service revolution and its marketing
implications: service logic vs service-dominant logic,”Managing service
quality, vol. 24, no. 3, pp. 206–229, 2014.
[2] S. W. Driessen, G. Monsieur, and W.-J. Van den Heuvel, “Data market
design: A systematic literature review,”Ieee access, vol. 10, pp. 33 123–
33 153, 2022.
[3] F. Liang, W. Yu, D. An, Q. Yang, X. Fu, and W. Zhao, “A survey on
big data market: Pricing, trading and protection,”Ieee Access, vol. 6,
pp. 15 132–15 154, 2018.
[4] M. Lu, S. Chen, X. Xue, X. Wang, Y . Zhang, Y . Zhang, and F.-Y .
Wang, “Computational experiments for complex social systems—part
ii: The evaluation of computational models,”IEEE Transactions on
Computational Social Systems, vol. 9, no. 4, pp. 1224–1236, 2021.
[5] D. Centola, “The network science of collective intelligence,”Trends in
Cognitive Sciences, vol. 26, no. 11, pp. 923–941, 2022.
[6] H. Cui and T. Yasseri, “Ai-enhanced collective intelligence,”Patterns,
vol. 5, no. 11, 2024.

TABLE III
QUANTITATIVECOMPARISON ACROSSCOLLABORATIONTOPOLOGIES.
Topology Individual-level Organizational-level System-level
¯Uind ↑σ(U ind)↓Gini↓ ¯Uorg(U G)↑Gains(%)↑ ¯Usys ↑σ(U sys)↓Rank
GovA (Isolated) 192.788 33.331 0.047 2179.753 -48.6 20528.649 1123.526 8
GovB (Globally Coupled) 289.183 24.680 0.040 4555.205 7.4 75083.9703322.7301
GovC (Star)492.595648.359 0.496 2883.712 -32.0 22574.2921047.4027
GovD (Ring) 278.502 75.366 0.126 3593.746 -15.2 46121.258 1988.327 5
GovE (RandomG(N, L)) 258.352 77.427 0.133 3460.193 -18.4 50115.238 2935.542 4
GovF (WS Small-World) 283.68110.263 0.0244240.275 1.2 55456.279 2655.588 2
GovG (NW Small-World) 227.573 39.401 0.072 4211.262 -0.7 54472.563 2489.793 3
GovH (BA Scale-Free) 387.233 176.142 0.207 3665.261 -13.6 44595.925 2791.403 6
Note.Best in each column is inboldand second is underlined .
[7] X. Xue, S. Wang, B. Gui, and Z. Hou, “A computational experiment-
based evaluation method for context-aware services in complicated
environment,”Information Sciences, vol. 373, pp. 269–286, 2016.
[8] I. Graef, “Market definition and market power in data: The case of online
platforms,”World Competition, vol. 38, no. 4, 2015.
[9] V . Kumar, V . Chattaraman, C. Neghina, B. Skiera, L. Aksoy, A. Buoye,
and J. Henseler, “Data-driven services marketing in a connected world,”
Journal of Service Management, vol. 24, no. 3, pp. 330–352, 2013.
[10] Z. Feng, Y . Xu, X. Xue, and S. Chen, “Review on the development of
microservice architecture,”journal of computer research and develop-
ment, vol. 57, no. 5, pp. 1103–1122, 2020.
[11] X. Xue, X. Yu, and F.-Y . Wang, “Chatgpt chats on computational
experiments: From interactive intelligence to imaginative intelligence for
design of artificial societies and optimization of foundational models,”
IEEE/CAA Journal of Automatica Sinica, vol. 10, no. 6, pp. 1357–1360,
2023.
[12] S. F. Railsback and V . Grimm,Agent-based and individual-based
modeling: a practical introduction. Princeton university press, 2019.
[13] I. Visnjic, A. Neely, and M. Jovanovic, “The path to outcome deliv-
ery: Interplay of service market strategy and open business models,”
Technovation, vol. 72, pp. 46–59, 2018.
[14] X. Xue, X. Yu, D. Zhou, C. Peng, X. Wang, D. Liu, and F.-Y .
Wang, “Computational experiments for complex social systems—part iii:
the docking of domain models,”IEEE Transactions on Computational
Social Systems, vol. 11, no. 2, pp. 1766–1780, 2023.
[15] I. Markovsky and F. D ¨orfler, “Behavioral systems theory in data-driven
analysis, signal processing, and control,”Annual Reviews in Control,
vol. 52, pp. 42–64, 2021.
[16] A. E. Abbas, W. Agahari, M. Van de Ven, A. Zuiderwijk, and
M. De Reuver, “Business data sharing through data marketplaces:
A systematic literature review,”Journal of Theoretical and Applied
Electronic Commerce Research, vol. 16, no. 7, pp. 3321–3339, 2021.
[17] S. Mahajan, “Data marketplaces: A solution for personal data control
and ownership?”Sustainability, vol. 14, no. 24, p. 16884, 2022.
[18] C. Peng, X. Yu, W. Ma, H. Kaneko, L. Meng, Y . Zhao, and X. Xue,
“Computational experiments: Virtual production and governance tool for
metaverse,”International Journal of Crowd Science, vol. 7, no. 4, pp.
158–167, 2023.
[19] D.-Y . Zhou, X. Xue, Q. Ma, C. Guo, L.-Z. Cui, Y .-L. Tian, J. Yang,
and F.-Y . Wang, “Federated experiments: Generative causal inference
powered by llm-based agents simulation and rag-based domain docking,”
IEEE/CAA Journal of Automatica Sinica, vol. 12, no. 7, pp. 1301–1304,
2025.
[20] X. Xue, G. Li, D. Zhou, Y . Zhang, L. Zhang, Y . Zhao, Z. Feng, L. Cui,
Z. Zhou, X. Sunet al., “Research roadmap of service ecosystems: A
crowd intelligence perspective,”International Journal of Crowd Science,
vol. 6, no. 4, pp. 195–222, 2022.
[21] W.-B. Huang, J. Liu, H. Bai, and P. Zhang, “Value assessment of
companies by using an enterprise value assessment system based on their
public transfer specification,”Information Processing & Management,
vol. 57, no. 5, p. 102254, 2020.
[22] D. Sj ¨odin, V . Parida, M. Jovanovic, and I. Visnjic, “Value creation
and value capture alignment in business model innovation: A process
view on outcome-based business models,”Journal of Product Innovation
Management, vol. 37, no. 2, pp. 158–183, 2020.
[23] S. L. Vargo and R. F. Lusch, “From repeat patronage to value co-creation
in service ecosystems: a transcending conceptualization of relationship,”
Journal of Business Market Management, vol. 4, pp. 169–179, 2010.
[24] X. Xue, X. Yu, D. Zhou, X. Wang, C. Bi, S. Wang, and F.-Y . Wang,
“Computational experiments for complex social systems: Integrated
design of experiment system,”IEEE/CAA Journal of Automatica Sinica,
vol. 11, no. 5, pp. 1175–1189, 2024.
[25] L. Milroy and C. Llamas, “Social networks,”The handbook of language
variation and change, pp. 407–427, 2013.
[26] D. Zhou, X. Xue, X. Lu, Y . Guo, P. Ji, H. Lv, W. He, Y . Xu, Q. Li,
and L. Cui, “A hierarchical model for complex adaptive system: From
adaptive agent to ai society,”ACM Transactions on Autonomous and
Adaptive Systems, 2024.
[27] D. Brunner, C. Legat, and U. Seebacher, “Towards next generation data-
driven management: Leveraging predictive swarm intelligence to reason
and predict market dynamics,” inCollective intelligence. CRC Press,
2024, pp. 152–203.
[28] V . Kumar, A. Dixit, R. R. G. Javalgi, and M. Dass, “Research framework,
strategies, and applications of intelligent agent technologies (iats) in
marketing,”Journal of the Academy of Marketing Science, vol. 44, no. 1,
pp. 24–45, 2016.
[29] X. Xue, D. Zhou, X. Yu, G. Wang, J. Li, X. Xie, L. Cui, and F.-Y . Wang,
“Computational experiments for complex social systems: Experiment
design and generative explanation,”IEEE/CAA Journal of Automatica
Sinica, vol. 11, no. 4, pp. 1022–1038, 2024.
[30] X. Xue, Y . Guo, S. Chen, and S. Wang, “Analysis and controlling
of manufacturing service ecosystem: A research framework based on
the parallel system theory,”IEEE Transactions on Services Computing,
vol. 14, no. 6, pp. 1598–1611, 2019.
[31] R.-U. Syrbe and K. Grunewald, “Ecosystem service supply and demand–
the challenge to balance spatial mismatches,”International Journal of
Biodiversity Science, Ecosystem Services & Management, vol. 13, no. 2,
pp. 148–161, 2017.
[32] H. Wei, W. Fan, X. Wang, N. Lu, X. Dong, Y . Zhao, X. Ya, and Y . Zhao,
“Integrating supply and social demand in ecosystem services assessment:
A review,”Ecosystem services, vol. 25, pp. 15–27, 2017.
[33] X. Xue, F. Chen, D. Zhou, X. Wang, M. Lu, and F.-Y . Wang, “Compu-
tational experiments for complex social systems—part i: The customiza-
tion of computational model,”IEEE Transactions on Computational
Social Systems, vol. 9, no. 5, pp. 1330–1344, 2021.
[34] J. Byrne and J. Taminiau, “A review of sustainable energy utility and
energy service utility concepts and applications: realizing ecological and
social sustainability with a community utility,”Wiley Interdisciplinary
Reviews: Energy and Environment, vol. 5, no. 2, pp. 136–154, 2016.
[35] X. Xue, D. Zhou, F. Chen, X. Yu, Z. Feng, Y . Duan, L. Meng, and
M. Zhang, “From soa to voa: a shift in understanding the operation
and evolution of service ecosystem,”IEEE Transactions on Services
Computing, vol. 16, no. 1, pp. 315–329, 2021.
[36] X. Yu, X. Xue, D. Zhou, G. Wang, and Z. Feng, “Unlocking complexity:
Harnessing value entropy for advanced multidimensional utility evalua-
tion in service ecosystems,”IEEE Transactions on Services Computing,
2025.

[37] J. R. Matthews, “Assessing organizational effectiveness: the role of
performance measures,”The Library Quarterly, vol. 81, no. 1, pp. 83–
110, 2011.
[38] R. McAdam, S.-A. Hazlett, and B. Galbraith, “The role of performance
measurement models in multi level alignment: an exploratory case
analysis in the utilities sector,”International Journal of Operations &
Production Management, vol. 34, no. 9, pp. 1153–1183, 2014.
[39] X. Xue, Z. Chen, S. Wang, Z. Feng, Y . Duan, and Z. Zhou, “Value
entropy: A systematic evaluation model of service ecosystem evolution,”
IEEE Transactions on Services Computing, vol. 15, no. 4, pp. 1760–
1773, 2020.
[40] D. Zhou, X. Xue, and Z. Zhou, “Sle2: The improved social learning
evolution model of cloud manufacturing service ecosystem,”IEEE
Transactions on Industrial Informatics, vol. 18, no. 12, pp. 9017–9026,
2022.
[41] K. van de Merwe, S. Mallam, and S. Nazir, “Agent transparency,
situation awareness, mental workload, and operator performance: A
systematic literature review,”Human Factors, vol. 66, no. 1, pp. 180–
208, 2024.
[42] W. Shen, L. Wang, and Q. Hao, “Agent-based distributed manufactur-
ing process planning and scheduling: a state-of-the-art survey,”IEEE
Transactions on Systems, Man, and Cybernetics, Part C (Applications
and Reviews), vol. 36, no. 4, pp. 563–577, 2006.
[43] X. Xue, S. Wang, L. Zhang, Z. Feng, and Y . Guo, “Social learning
evolution (sle): Computational experiment-based modeling framework
of social manufacturing,”IEEE Transactions on Industrial Informatics,
vol. 15, no. 6, pp. 3343–3355, 2018.
[44] N. Kapucu and V . Garayev, “Designing, managing, and sustaining func-
tionally collaborative emergency management networks,”The American
Review of Public Administration, vol. 43, no. 3, pp. 312–330, 2013.
[45] T. Yigitcanlar, S. Senadheera, R. Marasinghe, S. E. Bibri, T. Sanchez,
F. Cugurullo, and R. Sieber, “Artificial intelligence and the local gov-
ernment: A five-decade scientometric analysis on the evolution, state-
of-the-art, and emerging trends,”Cities, vol. 152, p. 105151, 2024.
[46] M. Al-Okaily and A. Al-Okaily, “An empirical assessment of enterprise
information systems success in a developing country: the jordanian
experience,”The TQM Journal, vol. 34, no. 6, pp. 1958–1975, 2022.
[47] B. Mefgouda, H. Idoudi, M. Al-Quraan, O. Waqar, A. Zoha, M. A.
Imran, and L. Mohjazi, “A qos-aware service-driven network selection
for hwns based on marcos and utility functions,”IEEE Open Journal of
the Communications Society, vol. 5, pp. 3658–3677, 2024.
[48] Y .-J. Seo and K.-H. Um, “The role of service quality in fostering differ-
ent types of perceived value for student blended learning satisfaction,”
Journal of Computing in Higher Education, vol. 35, no. 3, pp. 521–549,
2023.
