---
title: Relational Multi-Agent Reinforcement Learning for Dynamic Pricing in High-Speed Railway Markets
url: https://arxiv.org/abs/2607.05179
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Enrique Adrian Villarrubia-Martin
- David Muñoz-Valero
- Luis Rodriguez-Benitez
- Giovanni Montana
- Luis Jimenez-Linares
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.05179
pages: 46
chars: 91793
fetched_at: '2026-11-08T13:08:14+00:00'
kb_version: 1
---

# Relational Multi-Agent Reinforcement Learning for Dynamic Pricing in High-Speed Railway Markets

Relational Multi-Agent Reinforcement Learning for
Dynamic Pricing in High-Speed Railway Markets
Enrique Adrian Villarrubia-Martina, David Muñoz-Valerob,∗, Luis
Rodriguez-Beniteza, Giovanni Montanac, Luis Jimenez-Linaresa
aDepartment of Technologies and Information Systems, Universidad de Castilla-La
Mancha, Paseo de la Universidad 4, Ciudad Real, 13071, Spain
bDepartment of Technologies and Information Systems, Universidad de Castilla-La
Mancha, Avenida Carlos III, s/n, Toledo, 45071, Spain
cWarwick Manufacturing Group, University of Warwick, Gibbet Hill
Road, Coventry, CV4 7AL, UK
Abstract
Inliberalisedrailwaysystems, operatorsmustsetpricesdynamicallyinanen-
vironment with partial observability, as they retain private information about
their objectives and performance, where regulatory constraints prohibit com-
munication or direct information exchange between competitors to prevent
explicit collusion. Consequently, agents must learn to infer strategic interac-
tions only from observable market data which presents a significant challenge
for multi-agent reinforcement learning, where standard approaches typically
treat observations as unstructured vectors, ignoring the underlying market
topology that governs strategic interactions. To address this, an entity graph
modelling approach is proposed, which represents the environment as a graph
of operational units, rather than decision-making agents or static infrastruc-
ture, encoding competition, coordination, and connectivity relations between
entities. Then, an extension of the multi-agent twin delayed deep determin-
istic policy gradient algorithm with graph-based representation learning pro-
cesses the features of the entities through a multi-layer relational graph con-
volutional network and aggregates them via a learnt attention mechanism.
∗Corresponding author
Email addresses:enrique.villarrubia@uclm.es(Enrique Adrian
Villarrubia-Martin),david.munoz@uclm.es(David Muñoz-Valero),
luis.rodriguez@uclm.es(Luis Rodriguez-Benitez),g.montana@warwick.ac.uk
(Giovanni Montana),luis.jimenez@uclm.es(Luis Jimenez-Linares)
arXiv:2607.05179v1  [cs.LG]  6 Jul 2026

Experimental results in a rail pricing reinforcement learning environment
show that this novel framework achieves higher revenue and stability in two
different settings of increasing market complexity compared to a representa-
tive selection of relational and non-relational baselines. The code is publicly
available at:https://github.com/Kinrre/RelationalRailPricing-RL.
Keywords:
Dynamic Pricing, Multi-Agent Reinforcement Learning, Deep
Reinforcement Learning, Graph Neural Networks, Railway Systems
1. Introduction
The Multi-Agent Reinforcement Learning (MARL) community has in-
creasingly adopted graph-based approaches to model complex environments
[1, 2]. Graphs are a common and very powerful practice to naturally and ef-
ficiently capture the structural relations that are fundamental to multi-agent
interaction and reasoning [3]. The environments are characterised by a highly
dynamic nature, where agents are constantly moving and their neighbour-
hood relations evolve rapidly, which creates a need for architectures capable
of capturing abstract relational representations. Graph Neural Networks
(GNNs) are framed as the ideal solution, precisely because they operate na-
tively on graph structures, allowing the learning process to automatically
adapt to the changing topology of the environment [4]. As agents modify
their connections, GNNs maintain the ability to model interactions through
message passing operations, which transforms relational variability from a
limitation into an advantage, without the need to adapt the architecture of
the model.
Focusing on railway systems, the field of application selected for ex-
perimentation, graph-based representations have emerged as the standard
approach for modelling complex transportation networks. Station-based
graphs, where vertices encode physical stations and edges denote direct rail
connections, remain the predominant paradigm in recent railway optimisa-
tion literature [5]. This approach is widely used for network topology anal-
ysis, vulnerability assessment, and capacity planning [6]. However, these
models, where stations are encoded as nodes, are typically not designed to
capture operational aspects, such as service differentiation, multi-operator
dynamics, and market-level interactions in liberalised high-speed passenger
markets [7]. To bridge this gap, this work introduces an entity graph-based
2

modelling approach, where operational entities constitute the vertices, and
competitive, coordination, and connectivity relations are encoded as hetero-
geneous edges. With these relations encoded in the graph structure, GNN
layers propagate messages across the network while attention mechanisms
can selectively aggregate the most relevant features for each agent. This
produces learnable relational representations that can be used to support
strategic decision-making in multi-agent environments.
Based on the entity graph-based modelling framework [8, 9], the pro-
posed model learns a relational state representation for each agent through
a three-stage process. First, it individually encodes the characteristics of
all entities in the environment. Then, it enriches them by allowing enti-
ties to exchange contextual information with their neighbours through the
network of relations. Finally, it applies an attention mechanism that al-
lows each agent to selectively combine the most relevant information from
all entities, thus generating a compact and personalised state of the environ-
ment. These relational representations are subsequently integrated into an
actor-critic architecture augmented with graphs that operates under the Cen-
tralised Training with Decentralised Execution (CTDE) [10, 11] paradigm.
This architecture allows agents to access global information during training,
when graph-based embeddings are constructed and refined, while maintain-
ing decentralised policies that preserve privacy at runtime. The proposed
method extends the Multi-Agent Twin Delayed Deep Deterministic Policy
Gradient (MATD3) [12] algorithm with graph representation learning capa-
bilities, capturing the relational structure of the environment and addressing
the challenge of multi-agent strategic interaction under partial observability
with information asymmetry, which is typical of competitive market environ-
ments such as the liberalised passenger rail transport market.
1.1. Contributions
The contributions of this work can be summarised as follows:
•An entity graph modelling approach for MARL that encodes the en-
vironment as a graph of operational units rather than decision-making
agents or static infrastructure. This approach models competition,
coordination, and connectivity relations as heterogeneous edges be-
tween entities, providing a relational inductive bias [13] to capture fine-
grained strategic dependencies in partially observable environments.
3

•AnextensionoftheMATD3algorithmwithgraph-basedrepresentation
learning. The proposed method specifically incorporates a relational
state representation module that processes heterogeneous entity fea-
tures through a multi-layer Relational Graph Convolutional Network
(R-GCN) and aggregates them via a learnt attention mechanism to
learn policies that dynamically prioritise strategically relevant services.
In addition, it incorporates a gradient-stopping operation to decouple
representation learning from policy optimisation, which, although it
can come at the cost of a reduced total revenue, stabilises the training
dynamics of each agent individually.
•An experimental study of the framework in a railway pricing rein-
forcement learning environment [14] in two different scenarios, with
increased revenue and stability in both settings. The performance of
the method is compared against a representative selection of relational
and non-relational MARL baselines. Several ablation studies have been
conducted to measure the relative contribution of each edge type, the
impact of the network depth on agent performance, the importance
of the learnt attention mechanism, and the effect of decoupling the
representation learning from the actor. Furthermore, the learnt graph
embeddings are also explored.
The rest of this work is structured as follows: First, Section 2 reviews
related work. Then, Section 3 introduces the formal framework of partially
observable Markov Game (MG). Then, Section 4 presents the entity-graph
relational actor-critic framework. After that, Section 5 evaluates the effec-
tiveness of the framework, and finally, Section 6 outlines the conclusions and
future research directions.
2. Related work
First, Section 2.1 reviews MARL in the context of dynamic pricing. Sec-
ondly, Section 2.2 examines how graph-based representations can capture the
relational structure inherent in multi-agent environments. Lastly, Section 2.3
discusses the application of Deep Reinforcement Learning (DRL) to railway
systems.
4

2.1. Multi-agent reinforcement learning for dynamic pricing
MARL extends the single-agent reinforcement learning framework to sce-
narios in which multiple agents interact in a shared environment to achieve
individual or collective goals [15]. In contrast to single-agent settings, MARL
environments are inherently non-stationary, as each agent’s policy evolves
during training, thus altering the environment for other agents. This in-
teraction is formally modelled through game theory, and settings involving
both competitive and cooperative objectives are referred to as coopetition
[16]. A particularly influential paradigm for addressing non-stationarity that
maintains scalable, decentralised execution is CTDE [10, 11]. Under CTDE,
agents share global information during training to stabilise learning, while re-
taining independent policies at execution time. Within this paradigm, MAD-
DPG [11] adapts the deterministic policy gradient approach for continuous
action spaces in mixed cooperative-competitive environments, Multi-Agent
Proximal Policy Optimisation (MAPPO) [17] extends proximal policy opti-
misation to cooperative settings, and Multi-Actor Attention Critic (MAAC)
[18] incorporates attention mechanisms to dynamically weight the relevance
of other agents when computing centralised Q-values.
Dynamic pricing, also known as pricing intelligence, involves adjusting
prices in real time based on supply and demand to maximise profits and align
withmarketconditions. Withinthiscontext, forelectricvehiclecharging, [19]
proposed a MARL mechanism design framework to simultaneously determine
optimalchargingpricesacrossmultiplestations, modellingstation–userinter-
action as a mechanism design problem and station–station cooperation as an
MG solved via MADDPG. Similarly, for hydrogen fuel cell vehicle refuelling,
[20]employedaMulti-AgentSystem(MAS)tocoordinaterefuellingschedules
and determine prices, improving demand satisfaction and traffic flow in mi-
crogrids. Shifting to other domains, in telecommunications, [21] framed the
interaction between mobile virtual network operators and users as a Stack-
elberg game, solving it using a Multi-Agent Deep Q-Network (MADQN).
Moreover, in smart grids, [22] proposed a distributed multi-agent optimisa-
tion approach for resolving supply-demand imbalances while strengthening
privacy and autonomy.
Despite these advancements, dynamic pricing in high-speed railways in-
troduces complex relational dependencies, such as cooperative dynamics with
multi-operator services and overlapping market competition. Furthermore,
thepartialobservabilityandtheprohibitionofcommunicationbetweenagents
in this domain demand that agents infer strategic interactions only from ob-
5

servable market data. This motivates the use of graph-based representations,
where interacting entities and their relationships are naturally encoded as
nodes and edges in a graph structure.
2.2. Graph neural networks in multi-agent reinforcement learning
Multi-agentenvironmentsfrequentlyinvolverelationalinformation, where
agents interact with each other through dependencies such as competition or
coordination. However, traditional deep MARL approaches encode a state
as a flat vector, a representation that discards the structural relations be-
tween agents, forcing neural networks to implicitly discover patterns that
could be encoded explicitly. GNNs can be used as an alternative that pre-
serves this relational structure [23]. By modelling the environment as a
graph, where vertices denote decision-making entities and edges encode their
relationships, agents are able to reason explicitly about their interdependen-
cies. For instance, [1] introduced graph convolutional reinforcement learn-
ing, which constructs a graph where each agent corresponds to a vertex and
edges connect agents that influence each other’s outcomes. Rather than using
fixed rules to determine these connections, the method employs multi-head
attention mechanisms as relation kernels, learning how agents interact with
their neighbours, with temporal relation regularisation further encouraging
cooperative behaviours over time. Similarly, [24] developed G2ANet, which
introduces a two-stage attention network combining hard attention, to iden-
tify and eliminate irrelevant agent connections, and soft attention, to weigh
the importance of remaining interactions.
Other approaches have explored richer graph structures that incorporate
additional context from the environment. In [9], they proposed InforMARL,
which constructs an agent-entity graph connecting agents not only to other
agents but also to surrounding entities such as obstacles and goals. At each
time step, the framework builds a graph linking each agent to nearby entities
within its local neighbourhood, employing a GNN with multi-head attention
to aggregate this information into fixed-size representations for actor-critic
networks. This local aggregation is more sample-efficient than concatenating
global information, as it allows agents to focus on locally relevant context
while maintaining a scalable representation. Additionally, [2] developed a
GNN-based MARL method for resilient distributed coordination of multi-
robot systems operating under challenging real-world conditions. The ap-
proach employs MAPPO using a Multilayer Perceptron (MLP) critic for
training and a GNN actor that incorporates both node and edge features
6

through a modified GraphSAGE [25] architecture with multi-layer message
passing. A key innovation is a neighbour scoring mechanism which eval-
uates and selects the graph edges that agents should traverse for discrete
wayfinding.
Several successful applications can be found across multiple domains.
In traffic signal control, [26] introduced a graph state representation, and
in a similar way, [27] proposed the HG-M2I algorithm, which combines a
hierarchical graph representation learning module with a multi-agent mu-
tual information framework. In a related line of work on traffic manage-
ment, [5] applied DRL with graphs for the extension planning of metro net-
works, improving the resilience of urban critical infrastructures. Beyond
transportation, [28] proposed Multi-Relational Graph Reinforcement Learn-
ing (MRGRL) for dynamic flexible job-shop scheduling, explicitly modelling
multi-type dependencies and competition patterns through heterogeneous
graphs, demonstrating strong generalisation under unstable manufacturing
conditions.
Although these graph-based approaches are effective for reasoning about
relational structure, they predominantly model agents themselves as graph
nodes or static physical infrastructure, which limits their ability to capture
the fine-grained operational dependencies that drive strategic interactions,
as is the case of dynamic pricing in liberalised railway systems.
2.3. Deep reinforcement learning for railway systems
The application of DRL to railway systems has grown considerably in
recent years, with a potential for optimising operations and improving ef-
ficiency. In the context of traffic management, DRL has been applied to
real-time trajectory generation for trains to ensure punctuality and energy
efficiency [29], as well as to Train Timetable Rescheduling (TTR) and the
VehicleReschedulingProblem(VRSP),whereagentsmustrestorenormalop-
erations rapidly following disruptions [30, 31]. Further applications include
predictive maintenance scheduling [32, 33], autonomous train control [34, 35],
and interval control under safety constraints using constrained Markov deci-
sion processes [36]. Simulation environments such as Flatland-RL [31] have
played an important role in supporting the safe development and benchmark-
ing of these approaches [37].
However, existing DRL applications in railways are predominantly con-
cerned with operational problems rather than market-driven strategies. Dy-
namic pricing introduces additional challenges where agents must model the
7

distinct passenger behaviours, account for interdependencies arising from
multi-operator itineraries, as well as the inherent tension between compe-
tition and cooperation in a partially observable market. To address this gap,
[14] introduced RailPricing-RL, a parameterisable MARL environment de-
signed specifically for dynamic pricing in high-speed railway markets where
operators must balance competition and cooperation with connecting ser-
vices, incorporating microscopic passenger decision-making via Random Util-
ity Models (RUM). The current study extends this approach by introducing a
novel relational state representation that explicitly captures these structural
dependencies.
3. Preliminaries
This section introduces a partially observable MG [38], a stochastic game
that satisfies the Markov property, with mixed incentives in which agents
have both aligned and competing objectives. In an MG, a multi-agent exten-
sion of an MDP, multiple agents act as independent decision-makers, each
with their own set of actions and reward functions, as shown in Figure 1.
Environment
Agent 1
reward
action
Agent 2
action
obs
reward
obs
Figure 1: MARL interaction in a partially observable MG.
A key property is that both state transitions and individual rewards de-
pend on the joint actions of all agents, creating a complex interdependence
of strategies and outcomes in which no single agent fully controls the envi-
ronment dynamics. Formally, it is defined by the tuple:
8

M=⟨S, U, P, r, Z, O, A, γ⟩
whereSis the set of possible states, withs∈Sdenoting the current state
of the environment. The setA={1, . . . , n}represents thenagents, where
each agenta∈Aselects actionsu a ∈Uat each time step. These actions
collectively form a joint actionu∈U≡U n, which induces a transition
to a new states ′ according to the state transition functionP(s ′ |s,u) :
S×U×S→[0,1].
In contrast to Decentralised Partially Observable Markov Decision Pro-
cesses (DPOMDP) [39], typically used in fully cooperative settings where all
agents share a common reward function, stochastic games allow competitive,
cooperative, or mixed forms of interaction, the latter often referred to as
coopetition [16]. Consequently, each agent is assigned an individual reward
function, defined asr a(s,u) :S×U→R, which depends on the global
state and the joint action. Partial observability is intrinsic to realistic multi-
agent settings, contrasting with perfect information games, where the full
state is observable. This is the case in railway market environments, where
operators retain private information about their objectives, behaviour, per-
formance, etc. Formally, each agent receives an observationza ∈Z a, which
provides partial information about the global state. It is determined by the
agent-specific observation functionO(s, a) :S×A→Z a, whereZ a denotes
the observation space for agenta. Furthermore, agents operate under strict
information asymmetry without explicit communication, where each agenta
can observe only its own reward signalra and local observationza, whereas
the rewards, policies, and value functions of other agents remain hidden.
While traditional approaches treat the observations as unstructured vec-
tors, real-world MAS often exhibit a rich relational structure with entities
connected by specific relations that influence strategic interactions. To cap-
ture the structural relations inherent in multi-agent environments, the state
is augmented with a graphGt = (V, E, X), whereVdenotes the set of ver-
tices,E⊆V×Vare the edges encoding relations between vertices, and
X={x v}v∈V comprises node features. The graph evolves with the environ-
ment state at each time stept, yieldingGt =G(s t), and provides a structured
representation that enables reasoning about relational dependencies beyond
flat feature vectors. This is a separate augmentation of the state rather than
an additional element of the tupleM. Finally, the goal of each agentais to
learn a stochastic policyπa(ua |z a) :Z a ×U→[0,1], which maps observa-
9

tions to a probability distribution over actions. The collection of policies for
all agents,π= (π 1, . . . , πn), forms the joint policy. Thus, the objective of
each agent is to maximise its expected discounted return, defined as:
J(π a) =Eu∼π,s∼P
" ∞X
t=0
γtra t (s,u t)
#
,
whereγ∈[0,1]is the discount factor that determines the relative impor-
tance of immediate versus long-term rewards.
4. Methods
This section proposes an entity graph-based relational actor-critic frame-
work for MARL in environments with rich relational structure. First, Sec-
tion 4.1 introduces the entity-based graph modelling approach, then Sec-
tion 4.2 details the semantic embedding architecture, and finally Section 4.3
presents the graph-augmented actor-critic architecture that integrates these
representations.
4.1. Entity-based graph modelling
The first goal is to encode the environment as a heterogeneous graph to
provide a relational inductive bias [13, 40, 41] overcoming the limitations of
unstructured state representations common in MARL [17]. Typically, nodes
in these graphs are the agents themselves [1, 24] or the static physical infras-
tructure [5, 26]. As a novel contribution, the entity graph, instead of focusing
on decision-making agents such as railway companies, focuses on the opera-
tional nodes they control, referred to as entities. This paradigm shift moves
beyond modelling decision-makers or passive infrastructure, towards encod-
ing the strategic units of control themselves. The approach treats entities as
the primary vertices in the graph, modelling the different relations between
operational units within the MAS. It captures how strategic decisions affect
and are affected by the broader ecosystem of interactions, rather than forc-
ing neural networks to implicitly discover these patterns from flat feature
vectors.
These entities in the railway domain take the form of specific train ser-
vices, which constitute the resources and functional units on which agents
operate. A service is defined as a scheduled journey between stations at a
specific time with allocated capacity. The value of this entity approach lies
10

in the explicit modelling of the relational dynamics that arise between these
entities. Thus, competitive dependencies are captured, where services from
different agents compete for the same market; coordination relations, that
forms the agent’s internal service portfolio; and connectivity dependencies,
where one entity requires another to operate, so that passengers can transfer
between services to form multi-operator routes. As a consequence, the frame-
work can reason about how pricing decisions propagate through the service
network.
To formalise this, at each time stept, the railway market is modelled
as a directed graphGt = (V, E, X)where vertices correspond to individual
railway services and edges encode these market relations. Here, each vertex
v∈Vcorresponds to a unique service operated within the railway network
by an agentagent(v)∈A. A service is a scheduled, multi-stop journey along
a line of consecutive stations and serves a set of origin–destination markets
W(v), where each market(w o, wd)is specified by its origin stationw o and
destination stationw d, defining an origin-destination pair where passengers
seek transportation. The edge set is formed through three specific relation
types described as follows, wherevi, vj are any two distinct vertices inV:
•E comp ={(v i, vj) :W(v i)∩W(v j)̸=∅, date(v i) =date(vj), agent(vi)̸=
agent(vj)}denotes competition edges connecting services scheduled on
the same date that operate in at least one common marketwbut are
managed by different agents.
•E coord ={(v i, vj) :date(v i) =date(v j), agent(vi) =agent(v j)}repre-
sents coordination edges that link services operated by the same agent
on the same date.
•E conn ={(v i, vj) :W d(vi)∩W o(vj)̸=∅, date(v i) =date(v j)}defines
connectivity edges as potential passenger connections between services
scheduled on the same date, whereWo(v) ={w o : (wo, wd)∈W(v)}
andW d(v) ={w d : (wo, wd)∈W(v)}are the sets of origin and desti-
nation stations of the markets served byv.
Competition and coordination edges are symmetric, so the reverse edge
(vj, vi)is also added, whereas the connectivity relation is naturally directed
from the arriving service to the departing service. Thus, the edge setEis:
E=E comp ∪E coord ∪E conn.
11

Figure 2 illustrates a concrete example of this entity graph, visualising the
dense network of relations for a market comprising 15 services operated by
three competing agents, where each node corresponds to a service, labelled by
its controlling agent. Notably, the coordination edges densely interconnect
within each agent’s portfolio, competition edges link services in overlapping
markets, and connectivity edges weave between services to form potential
multi-operator routes.
1
1
1
11
2
2
2
2
2
3
3 3
3
3
Competition
Coordination
Connectivity
Figure 2: Entity graph representation for a railway network with 15 services scheduled
on the same date by three agents. Red edges indicate competition, services in the same
market by different operators, orange edges denote coordination, services operated by the
same agent, and green edges represent connectivity, potential transfers between services.
4.2. Relational state representation learning
This framework learns a relational state representation for each agent
through a three-stage process (see Figure 3): heterogeneous entity feature en-
coding, which processes categorical and continuous entity attributes through
separate pathways (Section 4.2.1), relational context propagation, which per-
forms message passing to create context-aware entity embeddings (Section
4.2.2), and agent-level state aggregation, which produces a fixed-size state
vector for each agent, computed from the set of entity embeddings (Section
4.2.3).
12

Multi-Layer
PerceptronEmbedding
Linear
Multi-Layer
GNN
Attention
pooling
Softmax
MLP
(Score function)
Weighted
Sum
+
R-GCN
R-GCN
ReLU
Layer Norm
Dropout
Layer Norm
Intermediate
layer
Final layer
3
2
1
1 1
1
2
3
Figure 3: Architecture of the relational state representation module. For each agent,
the entity features are first encoded, with categorical attributes through embeddings and
continuous ones through an MLP, and then concatenated and projected by a linear trans-
formation. A multi-layer R-GCN refines them by using message passing over the entity
graph. Finally, a learnt attention pooling aggregates them into a fixed-size state vector.
4.2.1. Encoding of heterogeneous entity features
The initial stage transforms the raw, heterogeneous features of each entity
node into a unified dense representation, which serves as the input to an
individual GNN. For each agenta, this transformation is achieved through
parallelpathwaysdesignedtohandlethedistinctpropertiesofcategoricaland
continuous data before fusing them into a common latent space. Each entity
vis characterised by a heterogeneous feature vector comprising categorical
attributes, such as origin and destination stations, seat class, operator, line,
corridor, time slot and rolling stock type, and continuous market indicators
used in dynamic railway pricing models. Each categorical attribute typekis
transformed through a learnable embedding function:
E a k :N→R de
which maps discrete category indices to dense embedding vectors of di-
mensiond e. This enables learning continuous semantic representations of
13

the respective categorical attributes, which are subsequently concatenated
to form a unified categorical feature vector:
ha cat(v) =∥
k∈K
E a k (vk)
whereKis the set of all categorical attributes for entityv, and∥denotes
the concatenation operation.
The dynamic market data associated with servicev, comprising pricesps,c
and sales volumenw,c for each service-seat combination and the total service
profitr w,c are flattened into a single vectorxa cont(v). To enforce partial ob-
servability, agentaobserves complete information for its own services, but
for competitor services the private ticket-sales information, that is, sales vol-
ume per service-seat and total service profit, is masked with zeros. Although
zero sales is a valid observation, it cannot be confused with a masked one,
as masking is applied only to competitor services which can be identified by
the operator feature. This vector is then processed by an MLP to capture
complex, nonlinear interactions and dependencies within the market signals,
such as price elasticity effects:
ha cont(v) = MLPa(xa cont(v))
Finally, the categorical and continuous vectors are concatenated and pro-
jected into the target hidden dimensiondh by a linear transformation:
ha,(0) v =W a proj[ha cat(v)∥h a cont(v)] +ba proj.
This projection yields the initial node embeddingha,(0) v ∈R dh for each en-
tity, a unified embedding that captures the intrinsic properties independently
of the graph structure, without incorporating any relational information from
neighbouring entities. These entity-level representations then serve as input
for the relational context propagation stage, where message passing over the
graph enriches them with information from the entity’s neighbourhood.
4.2.2. Relational context propagation through a multi-layer GNN
The initial entity embeddingsha,(0) v capture intrinsic properties but lack
awareness of the broader market structure. To incorporate this relational
context, a multi-layer GNN that performs message passing across the het-
erogeneous entity graph, is used. Specifically, a stack of R-GCN [42] layers
is employed to iteratively aggregate information from neighbouring entities.
14

At each layerℓ∈ {1,2, . . . , L}, the hidden representationha,(ℓ) v of entityvis
updated through message passing over the graph structureGt:
ha,(ℓ) v =f (ℓ)

X
r∈R
X
u∈Nr(v)
1
|Nr(v)| W (ℓ) r ha,(ℓ−1) u +W (ℓ) 0 ha,(ℓ−1) v +b (ℓ)

 , v∈V
whereN r(v)denotes the neighbourhood of nodevunder relationrcon-
nected through competition, coordination, or connectivity edges. Each re-
lation weight matrixW (ℓ) r transforms the aggregated neighbour representa-
tions, whereasW (ℓ) 0 corresponds to a self-loop that introduces a special rela-
tion type to each node, to ensure that the node at layerℓis also informed by
the corresponding representation at the previous layerℓ−1. In addition,b(ℓ)
is a learnable bias vector and the activation functionf(ℓ) introduces nonlin-
earity. The normalisation constant|Nr(v)|implements a mean aggregation,
ensuring that nodes with many connections do not dominate the aggregation.
To stabilise training and facilitate gradient flow through deep architec-
tures, each intermediate layerℓ < Lincorporates several architectural mech-
anisms. More specifically, residual connections [43] are added to mitigate the
vanishing gradient problem through additive information flow across layers.
In addition, layer normalisation [44] is employed to stabilise the distribution
of representations as they evolve over the network during training. Further-
more, dropout regularisation prevents overfitting by randomly deactivating
neurons during training. In contrast, the final layerLdiffers from intermedi-
ate layers, applying only layer normalisation without an activation function
or residual connection.
This produces the final context-aware entity embeddingha,(L) v ∈R demb,
whered emb is the embedding dimension. These learnt embeddings encode
both intrinsic entity properties, derived from the initial feature encoding,
and relational context, acquired through iterative message passing across the
graph structure. Consequently, each embeddingh a,(L) v captures the strate-
gic position of entityvwithin the market ecosystem, reflecting competitive
pressures from rival services, portfolio synergies with services under the same
agent’s control, and network effects arising from connectivity relations.
4.2.3. Attention-based agent-level state aggregation
Each agent GNN yields a set of context-aware embeddings{ha,(L) v }v∈V
for all entities in the environment. However, for decision-making, each agent
15

requires a single, fixed-size state vector that aggregates information from
the set of entities relevant to its decision-making. Since the number of en-
tities can vary, a simple concatenation or flattening of embeddings is not
feasible. While fixed pooling operations, such as mean or max aggregation,
can produce a fixed-size vector, they treat all entities as equally important,
regardless of their strategic relevance.
To overcome this, an attention mechanism is introduced that learns to
dynamically weigh the importance of each entity in the environment. This
allows the agent to focus on the most strategically relevant entities when
constructing its state representation. For instance, the attention weights can
learn to prioritise services in highly competitive markets during price wars,
while directing focus towards capacity-constrained services when demand
increases, or emphasising services that form multi-operator journeys when
coordination opportunities arise. For each agenta, attention weights are
computed by applying a learnt scoring function to each entity embedding,
followed by softmax normalisation:
αa v = exp

score(ha,(L) v )  P
u∈V exp

score(ha,(L) u )  , v∈V,(1)
wherescore(·)is a learnable function that maps entity embeddings to
scalar importance scores. In particular, a two-layer MLP with a ReLU acti-
vation function is used for thescorefunction. The agent-level observation˜za
is then computed as a weighted sum:
˜za = X
v∈V
αa vha,(L) v ,(2)
yielding ˜za ∈R demb, a permutation-invariant representation [45] that dy-
namically weights entities according to learnt strategic relevance. Moreover,
the learnt attention weights are useful diagnostics, offering insight into which
entities the agent considers most relevant to make a decision at each time
step.
4.3. Relational actor-critic with heterogeneous graph embeddings
The attention mechanism produces a context-aware state vector˜za for
each agent. Next, to enable strategic decision-making with these represen-
tations in mixed competitive-cooperative multi-agent settings under partial
observability and information asymmetry, the framework employs the CTDE
16

paradigm [10, 11]. This framework gives agents access to global information
during training while maintaining decentralised, privacy-preserving policies
at execution time, making it well-suited for competitive market environments
where operators must act independently based on local observations. Based
on the MATD3 algorithm [12], the proposed method extends the standard
actor-critic architecture with graph-based representation learning to capture
relational environmental structure. Each agentamaintains two distinct com-
ponents, a decentralised actorπa θ that maps local aggregated observations˜za
to actions, and two centralised criticsQa ϕ1,Q a ϕ2 that estimate action-value
functions using global state information, with the minimum taken to miti-
gate overestimation bias.
Additionally, each agentamaintains its own independent GNN (GNNψa)
that processes the entity graphGt, with agent-specific masked features, to
produce entity embeddings{ha,(L) v }v∈V. This design reflects the information
asymmetry inherent in competitive markets where each agent observes only
public information about competitors’ entities while maintaining complete
visibility of its own operations. In particular, the actor networkπ a θ pro-
cesses the agent’s aggregated observation˜za derived from attention-weighted
pooling of entity embeddings to produce a continuous actionua. The ac-
tor maximises expected returns through policy gradients, whereas the critic
minimises temporal difference error. Therefore, using both to update the
GNN representations can lead to conflicting gradient signals. To address
this, when computing actions for environment interaction and actor updates,
the aggregated observation˜za, along with the representation module, is de-
tached from the computational graph. Thus, the GNN is trained exclusively
through the critic loss, which provides richer signals from the global value
function, decoupling policy learning from representation learning.
The centralised criticsQa ϕ1(˜Z,u), Qa ϕ2(˜Z,u)take as input the joint aggre-
gated observations ˜Z= ( ˜z1, . . . ,˜zn)and joint actionsu= (u 1, . . . , un)of
all agents. The critics operate on the same abstracted state space as the
actors, taking as input the joint aggregated observation˜Zto learn a global
value function conditioned on the agents’ summarised local views. During
critic updates, the GNN parametersψa are optimised only with respect to
the current agent, although the critics receive the joint embedding˜Zj, which
also contains the embeddings produced by the GNNs of other agents. The
GNN parametersψ a are jointly optimised with the critics parametersϕa 1, ϕa 2
to minimise the temporal difference error as the expected value over samples
17

drawn from the replay bufferD:
L(ϕa 1, ϕa 2, ψa) =Ej∼D
" 2X
i=1

ya j −Q a ϕi(˜Zj,u j) 2
#
,(3)
wherey a j is the target value computed using target networks as follows:
ya j =r a j + (1−d j)γmin i=1,2 Qa ϕ′ i (˜Zj+1, π1 θ′(˜z1 j+1) +ϵ, . . . , πn θ′(˜zn j+1) +ϵ),(4)
andϵ∼clip(N(0, σ),−c, c)introduces a small amount of random noise
to the target policy as a regularisation term, clipped to keep the target close
to the original action. The termdj indicates a terminal transition, for tran-
sitions where the episode terminates, the targetya j is equal to the immediate
rewardr a j. The next-state embeddings are produced by the online represen-
tation module, as only target networks are used for the actors and critics,
which already provide a stable objective in the learning process. Then, the
actor is updated using the deterministic policy gradient:
∇θaJ(π a) =Ej∼D
h
∇θaπa(˜za j )∇uaQϕa 1 (˜Zj,u j)|ua=πa(˜za j )
i
(5)
with gradient detachment on the aggregated observations to preserve the
separation between policy and representation learning. In addition, the actor
target network is updated with a reduced frequencydcompared to the critic,
which has been shown to reduce overestimation bias and improve sample ef-
ficiency in continuous control tasks [46]. Finally, to further stabilise learning,
target networks are updated using soft updates with interpolation parame-
terτ. The complete training procedure of the framework called RACHE is
detailed in Algorithm 1.
5. Experimental settings and results
This section evaluates the effectiveness of the proposal in learning strate-
gic pricing policies in two different scenarios. First, Section 5.1 describes the
simulation environment, and Section 5.2 the experimental scenarios. Subse-
quently, Section 5.3 presents the algorithms selected for evaluation. Then,
Section 5.4 details the implementation settings. Later, Section 5.5 analyses
the comparative performance of the evaluated algorithms and finally, Section
5.6 examines key architectural components of RACHE.
18

Algorithm 1Relational Actor-Critic with Heterogeneous Graph Embed-
dings (RACHE)
1:Initialise networks{π θa, Qϕa 1 , Qϕa 2 ,GNN ψa}n a=1 with random parameters
2:Initialise target networksθ ′a ←θ a, ϕ′a 1 ←ϕ a 1, ϕ′a 2 ←ϕ a 2
3:Initialise replay bufferD
4:forepisode =1, . . . , Mdo
5:fort= 1, . . . , Tdo
6:foreach agenta= 1, . . . , ndo
7:Compute service embeddings:{h a,(L) v }v∈V =GNN ψa(Gt)▷With
masked features
8:Compute aggregated observation ˜za t via attention using Eq. 1-2
9:Select action:u a t =π θa(˜za t ) +ϵ,ϵ∼ N(0, σ)▷Stop gradient
10:end for
11:Execute joint actionu t, observe rewards{ra t }n a=1 and next observation
Zt+1
12:Store transition(Z t,u t,{r a t }n a=1,Z t+1, dt)inD▷Raw entity features
13:if|D| ≥batch sizethen
14:foreach agenta= 1, . . . , ndo
15:Sample minibatch(Z j,u j,{r a j }n a=1,Z j+1, dt)fromD
16:Compute aggregated observation ˜za j+1 for all agents▷See Lines
7-8
17:Compute target as shown in Eq. 4
18:Update critic and GNN using Eq. 3
19:Update actor using the sampled policy gradient as in Eq. 5
▷Stop gradient
20:end for
21:Update critic target network:ϕ ′a i ←τ ϕa i + (1−τ)ϕ ′a i , i∈ {1,2}
22:iftmodd= 0then
23:Update actor target network:θ ′a ←τ θa + (1−τ)θ ′a
24:end if
25:end if
26:end for
27:end for
5.1. Simulation environment
All experiments are conducted using the simulator RailPricing-RL [14], a
parameterisable reinforcement learning environment designed to model high-
speed railway networks featuring dynamic pricing, multi-operator itineraries,
and diverse passenger behaviour. The environment employs microscopic
19

modelling of passenger decision-making using RUM, where passengers can
choose not to travel if no itinerary meets their utility threshold, resulting in
a non-zero sum game. It supports MARL algorithms through compatibility
with standard RL interfaces. In this environment, each service is scheduled
for a specific date. However, the simulation operates over a booking horizon
that begins when the first passenger attempts to buy a ticket. This horizon is
divided into discrete time steps, each representing a single day. During these
steps, agents set prices, and passengers, each arriving on a specific day sam-
pled from their segment’s booking distribution, make purchasing decisions.
Now, the observation space, action space, and reward function are described.
Observation space.Each agent observes all services in the network. For
each service the observation includes static attributes which are the train
service provider, the corridor (a set of stations within a region), the line (a
sequence of stations in the corridor), the time slot, and the rolling stock,
encoded as indices, as well as dynamic pricing data containing the prices per
service-seat combination, the ticket sales and the cumulative service revenue.
Nevertheless, the ticket sales and the cumulative service revenue are private,
so agentaobserves them only for its own services, while the corresponding
features of competitor services are masked with zeros to preserve partial
observability.
Action space.The action space defines the set of decisions available to
agents for modifying ticket prices in their respective services. Each agent
selects a continuous actionαc v,t ∈[−1,1]per service-seat combination, rep-
resenting a normalised percentage price adjustment applied to the current
price:
pc v,t+1 =p c v,t ·

1 +αc v,t · β 100  ,
whereβ= 25is the default scaling factor and prices are clipped to[0,∞)
to prevent negative values.
Reward.At each time stept, agentareceives a reward equal to the incre-
mental daily revenue across its operated services:
ra t = X
v∈V a
ρv t −ρ v t−1,
20

whereρ v t denotes the cumulative revenue of servicevup to time stept
andV a ⊆Vis the set of services operated by agenta. This formulation
assumes no associated costs for providing services, so the reward captures
revenue changes only. Thus, the objective is to maximise its expected total
revenue over the course of an episode.
5.2. Scenarios
The experiments evaluate the performance of the algorithms in two sce-
narios of increasing market complexity. These scenarios employ distinct sup-
ply configurations and a common demand pattern to assess algorithm be-
haviour under varying levels of market structure. The supply configuration
of the first scenario features 18 services scheduled on the same date, oper-
ated by three agents, each one with six services, illustrated in Figure 4a. The
second scenario expands it to 63 services, consisting of a daily schedule of
21 services repeated on three consecutive days. In addition, it introduces an
additional agent as shown in Figure 4b. In both scenarios, agents compete
directly in overlapping markets and can cooperate through multi-operator
connecting itineraries. Agents are heterogeneous, controlling different sets
of services with distinct action spaces. The specific characteristics of each
scenario are described below.
1
1
1
1
1
1
2
2
2
2
2
2
3
3
3
33
3
Competition
Coordination
Connectivity
(a) Base.
1 2
3
4
2
1
3
214 2
1
3
2
3
2
1
3
1
1
4
1 2
3
4
2
1
3
214 2
1
3
2
3
2
1
3
1
1
4
1 2
3
4
2
1
3
214 2
1
3
2
3
2
1
3
1
1
4
Competition
Coordination
Connectivity (b) Large.
Figure 4: Entity graph representations for the experimental scenarios. Each node corre-
sponds to a train service labelled by its operating agent, and edges encode competition,
coordination, and connectivity relations.
21

Base.This scenario introduces a varied passenger market across five sta-
tions and seven origin-destination markets, operated by three agents, each
controlling six services on a single day with a total of 18 services. Four
passenger segments named business, commuter, student and leisure coexist
with distinct utility functions and temporal preferences. On the one hand,
business travellers are a user group characterised by inelastic demand, with
strong preferences for convenient morning arrival and departure times, and
commuters exhibit high penalties for travel time and transfers. On the other
hand, students show high price sensitivity with flexible timing preferences
and book tickets close to the departure, whereas leisure passengers tend to
book earlier and over a wider window with greater diversity in the arrival
time. Episodes last seven days and generate an average of 980 potential
passengers across all markets. Moreover, all services offer two seat types,
basic and premium, with a capacity of 32 and eight seats per service respec-
tively, forming a joint action space of 36 dimensions. Finite seat availability
introduces capacity management constraints requiring agents to adapt their
pricing strategies in response to competition and inventory levels.
Large.This scenario expands market complexity by introducing a fourth
competing agent, resulting in a total of 63 services, 21 per day over three
consecutive days, across six origin-destination markets with an increased
number of passengers. The four agents are asymmetric in portfolio size,
with the largest controlling a total of 21 services, and the smallest operating
only nine. The same four passenger segments coexist with the same utility
functions and temporal preferences described above. Episodes span ten days
and generate an average of approximately 1,420 potential passengers across
all markets. As in the first scenario, all services offer basic and premium
seat types, with a capacity of 13 and four seats per service respectively, and
a joint action space of 126 dimensions, to account for capacity management
constraints.
Finally, Table 1 reports the statistics of the entity graph for each scenario.
In both, the coordination relation is the densest one, as it connects every
service scheduled on the same date provided by the same agent. However,
the other relations in the Large scenario, competition and connectivity, are
more represented with the addition of a fourth agent.
22

Table 1: Statistics of the entity graph for each scenario. Competition and coordination
edges are symmetric and counted in both directions, whereas connectivity edges are di-
rected.
Statistic Base Large
Agents 3 4
Nodes (services) 18 63
Competition edges 30 (21%) 162 (26%)
Coordination edges 90 (61%) 294 (47%)
Connectivity edges 27 (18%) 168 (27%)
Total edges 147 624
5.3. Benchmark algorithms and baselines
To evaluate the approach and its contribution of entity-based graph mod-
elling, RACHE is compared against a representative selection of MARL al-
gorithms covering deterministic and stochastic policies, with and without
relational structure. The evaluated algorithms are described below:
•Random:A non-learning baseline that selects pricing actions uni-
formly at random from the action space, establishing a lower bound on
performance.
•Static pricing:A revenue management strategy in which fixed pricing
is used to assess whether dynamic pricing policies are valuable.
•MADDPG [11]:A deterministic actor-critic algorithm extending
DDPG [47] to multi-agent settings via CTDE, included as a baseline
for deterministic policy methods in mixed cooperative-competitive en-
vironments.
•MATD3 [12]:A deterministic actor-critic that extends MADDPG
with twin critics, delayed policy updates, and target policy smoothing
to mitigate overestimation bias. This is the algorithm the framework
is based on.
•MAAC [18]:A stochastic multi-agent extension of SAC [48] incor-
porating attention to dynamically weight the relevance of other agents
when computing centralised Q-values to assess agent-level attention
without explicit graph structure.
23

•GA-AC [24]:A graph-based stochastic actor-critic in which decision-
making agents are graph nodes and interactions are modelled by the
G2ANet two-stage attention mechanism, combining hard gating with
soft scaled dot-product attention. It contrasts the agent-based graph
paradigm with the entity-graph approach of RACHE.
These algorithms are evaluated in the scenarios described previously to
assess whether explicit relational reasoning provides benefits compared to
flat observation encoders, whether modelling operational entities in an entity
graph is preferable to modelling decision-making agents as graph nodes, and
how deterministic policy methods compare with stochastic alternatives in
this setting. All baseline implementations, except for the MAAC algorithm
for which the original repository has been used, are publicly available at:
https://github.com/Kinrre/RelationalRailPricing-RL.
5.4. Implementation details
For a standardised comparison, the default hyperparameters of each algo-
rithm were adopted without additional tuning. A complete list of the hyper-
parameters is provided in Appendix A, and all experiments were conducted
on an Intel i7-13700KF CPU and an NVIDIA GeForce RTX 4080 16GB
GPU. To encourage initial exploration and diversify the state-action space,
each algorithm was first trained with a random policy for 1,000 episodes. The
models were trained for one million steps with a replay buffer of the same size.
Furthermore, policy updates were performed every two Q-network updates
in the case of the MATD3 and RACHE algorithms. Finally, it is worth not-
ing that the RACHE framework employs a two-layer R-GCN for relational
context propagation across the entity graph.
In theexperiments, to facilitatestable training, normalisation was applied
tocontinuousfeaturesoftheobservationspace, suchasprices, ticketsalesand
cumulative service revenue. In particular, it was performed after masking the
private data of each agent, which can still be identified through the operator
feature. The normalised observation featureˆzt at time steptwas computed
as follows:
ˆzt = zt −µ tp σ2 t +ϵ ,
wherez t is the raw observation at timet,µt is the running mean of each
individual continuous feature up to timet,σ2 t is the running variance of each
24

individual feature up to timet, andϵis a small constant used for numerical
stability. Fortherewardsignal, representingthedailyrevenue, rewardscaling
was employed instead of standard normalisation. Rewards were divided by
a constant factor of 1,000 in both scenarios to account for high revenue
magnitudes. This approach preserves the direct relationship between revenue
and the reward signal, maintaining positive signs and relative magnitudes
while preventing numerical instability from large gradient updates. As a
result, the value function receives a more consistent learning signal with a
clearer distinction between more profitable and less profitable actions.
5.5. Performance comparisons and analysis
This section analyses the performance of the evaluated algorithms in both
scenarios. Table 2 summarises the total revenue obtained during the eval-
uation at the end of training using the last checkpoint of the models, and
Figure 5 illustrates the training dynamics across all scenarios.
Table 2: Total revenue obtained in the evaluation using the last checkpoint for the dif-
ferent scenarios. The mean and the stratified bootstrap confidence intervals at 95% were
computed over three independent runs.
Algorithm Base Large
Random30961 [30832,31092] 40031 [39937,40115]
Static pricing31309 [31284,31335] 40950 [40908,40992]
MADDPG32688 [31641,33675] 43902 [43427,44402]
MATD337028 [36312,37739] 48206 [46930,49425]
MAAC31254 [30445,32093] 41220 [40755,41675]
GA-AC34446 [34285,34596] 40479 [40388,40566]
RACHE (Ours)41036[40596,41509]53831[53113,54604]
The highest values are indicated in bold.
First, with respect to the non-learning baselines, static pricing, that keeps
a fixed pricing by not modifying the initial price point for each service spec-
ified by the scenarios, performs better than the random baseline, indicating
that modifying prices randomly from the action space is a worse strategy.
Among the learning-based algorithms, the RACHE framework achieves the
highest revenue in both scenarios, followed by MATD3, which presents a
substantially higher variance. This supports that the relational state repre-
sentation learnt over the entity graph provides a meaningful inductive bias.
25

As expected, regarding the deterministic baselines, MATD3 surpasses MAD-
DPG, since the combination of twin critics, delayed policy updates, and
target policy smoothing helps to achieve a higher revenue.
In the case of the stochastic alternatives, MAAC fails to learn an effective
pricing policy, performing comparably to or even worse than the random
baseline during training in the first scenario. Finally, regarding GA-AC,
the agent-based graph baseline learns a meaningful policy that surpasses
MADDPG in the Base scenario, with a very low variance. However, in the
large one, its performance fails to improve over the course of training. This
is due to the fact that, by abstracting each operator as a single node, GA-
AC cannot capture the fine-grained service-level relations. The entity graph
addresses precisely this limitation by treating services rather than operators
as the primary vertices, whose granularity scales with the market structure.
0.0 0.2 0.4 0.6 0.8 1.0
Time steps 1e6
28000
30000
32000
34000
36000
38000
40000
42000
44000Average Total Revenue (95% CIs)
Base
0.0 0.2 0.4 0.6 0.8 1.0
Time steps 1e6
40000
42500
45000
47500
50000
52500
55000
57500
Large
MADDPG
GA-AC
MATD3
Random
RACHE
Static
MAAC
Figure 5: Average total revenue obtained at training for the two scenarios.
To account for which agent the total revenue comes from, Figure 6 shows
the distribution of the total revenue of each individual agent in both scenar-
ios. Foremost, it can be observed in the Base scenario that the total revenue
is more evenly distributed among the agents, whereas in the Large scenario,
it is imbalanced because of the asymmetric portfolio sizes. In both cases,
the RACHE framework increases the revenue of every agent with respect
to almost all baselines, except, for instance, the first agent of the MATD3
algorithm in the former. More precisely, the increase of total revenue in the
first scenario can be attributed mainly to the third agent, although, in the
second, the improvement is more uniformly distributed across all agents.
In addition, as suggested by [49], Figure 7 presents a pairwise matrix
26

Random Static MADDPGMATD3 MAAC GA-AC RACHE
Algorithm
0
2500
5000
7500
10000
12500
15000
17500Average Revenue (95% CIs)
Base
Random Static MADDPGMATD3 MAAC GA-AC RACHE
Algorithm
0
2500
5000
7500
10000
12500
15000
17500
Large
Agent 1 Agent 2 Agent 3 Agent 4
Figure 6: Average revenue obtained at evaluation using the last checkpoint for each agent.
with the probability of improvement, that is, the probability that algorithm
Xobtains a higher total reward than algorithmY. This is calculated from
the Mann–WhitneyUstatistic collected across the three seeds for a scenario
mgivenNandKevaluation episodes respectively, defined as:
P(X m > Ym) = 1 N K
NX
i=1
KX
j=1
S(xm,i, ym,j)whereS(x, y) =



1,ify < x,
1
2 ,ify=x,
0,ify > x.
The results indicate that the RACHE framework obtains a higher total
reward than the rest of the considered baselines.
RandomStatic MADDPGMATD3MAACGA-ACRACHE
Random
Static
MADDPG
MATD3
MAAC
GA-AC
RACHE
0.17 0.33 0.00 0.52 0.00 0.00
0.83 0.33 0.00 0.65 0.00 0.00
0.67 0.67 0.06 0.70 0.29 0.00
1.00 1.00 0.94 1.00 0.94 0.00
0.48 0.35 0.30 0.00 0.03 0.00
1.00 1.00 0.71 0.06 0.97 0.00
1.00 1.00 1.00 1.00 1.00 1.00
Base
RandomStatic MADDPGMATD3MAACGA-ACRACHE
Random
Static
MADDPG
MATD3
MAAC
GA-AC
RACHE
0.00 0.00 0.00 0.22 0.10 0.00
1.00 0.00 0.00 0.33 0.97 0.00
1.00 1.00 0.10 0.98 1.00 0.00
1.00 1.00 0.90 1.00 1.00 0.02
0.78 0.67 0.02 0.00 0.67 0.00
0.90 0.03 0.00 0.00 0.33 0.00
1.00 1.00 1.00 0.98 1.00 1.00
Large
0.0
0.2
0.4
0.6
0.8
1.0
P(row > col)
0.0
0.2
0.4
0.6
0.8
1.0
P(row > col)
Figure 7: Probability of improvement matrix using the Mann–WhitneyUstatistic.
Next, the effect of the learnt policies on the final prices at the end of the
27

episode, relative to the initial fares, is analysed together with its impact on
the percentage of passengers travelling. Figure 8 shows the distribution of
the final price change per seat type, and Table 3 details the corresponding
percentages. As shown, the deterministic algorithms increase prices more
than the stochastic ones. In fact, in the Base scenario, GA-AC obtains a
higher revenue than MADDPG with smaller price increments, as well as
RACHE compared to MATD3 in both scenarios, indicating that larger price
increases do not necessarily translate into higher revenue. In contrast, the
deterministic algorithms reduce the percentage of passengers travelling more
than the stochastic ones, as a consequence of their larger price increases, but
still RACHE obtains a higher revenue while retaining a larger number of
passengers travelling compared to MATD3.
MADDPG MATD3 MAAC GA-AC RACHE
Algorithm
100
0
100
200
300
Final Price Change (%)
Base
MADDPG MATD3 MAAC GA-AC RACHE
Algorithm
0
200
400
600
800
Large
Basic Premium
Figure 8: Distribution of the final price change per seat type relative to the initial fare.
Lastly, Table 4 reports the number of parameters for each model and the
totaltrainingtimeincludingalltheseedsofeachalgorithminhours. Notably,
the scalability of the proposed framework can be attributed to two points:
first, the processing of a compact fixed-size embedding of each agent, which
decreases the input size of the centralised critics, and second, to the message
passing paradigm whose parameter weights are shared across all nodes and,
therefore, independent of the number of services in the graph.
5.6. Further studies
This section examines key architectural components in more depth. First,
Section 5.6.1 analyses the importance of each relation type in the entity
28

Table 3: Percentage of passengers travelling in the evaluation using the last checkpoint
for the different scenarios. The mean and the stratified bootstrap confidence intervals at
95% were computed over three independent runs.
Algorithm Base Large
Random70.15 [69.96,70.34] 63.07 [62.99,63.16]
Static pricing70.67[70.50,70.84]63.22[63.12,63.31]
MADDPG63.16 [62.91,63.42] 52.77 [52.27,53.29]
MATD361.09 [59.94,62.18] 52.08 [51.35,52.78]
MAAC69.53 [69.23,69.82] 62.15 [61.88,62.45]
GA-AC69.48 [69.28,69.68] 63.10 [62.99,63.20]
RACHE (Ours)63.46 [62.03,64.81] 53.55 [53.04,54.04]
The highest values are indicated in bold.
Table 4: Parameter count of each algorithm and total wall training time using three
independent runs for the different scenarios.
Base Large
Parameter Count Wall time Parameter Count Wall time
MADDPG1,318,6956.2hours5,851,778 9.0hours
MATD32,208,810 6.2hours10,374,790 9.1hours
MAAC1,759,000 7.0hours5,152,212 10.0hours
GA-AC4,287,825 6.3hours10,094,856 9.1hours
RACHE (Ours)1,887,7295.8hours2,983,466 7.4hours
The lowest values are indicated in bold.
graph. Subsequently, Section 5.6.2 examines how the depth of message pass-
ing affects agent performance. Then, Section 5.6.3 evaluates the attention-
based pooling contribution. Next, Section 5.6.4 investigates the effect of
decoupling representation learning from the actor in the training dynamics.
Finally, Section 5.6.5 analyses the information encoded by the learnt graph
embeddings.
5.6.1. What is the contribution of each relation type in the entity graph?
An evaluation of the importance of each relation was carried out, in which
each relation type was removed from the entity graph in order to assess
its relative contribution. To this end, three variants of the framework are
compared versus the default configuration, in which all three relation types
29

are present.
Figure 9 shows the average total revenue during training when each re-
lation type is removed in both scenarios. The default configuration with
all relations results in the highest total revenue, confirming that the three
relations contribute to the agent’s decision-making. More specifically, re-
moving the competition relation produces the largest drop in performance,
followed by the connectivity relation, which is expected, since they capture
direct competition and potential cooperation between agents. In contrast,
removing the coordination relation, inspired by agent-based graphs, which
only encodes whether two services are operated by the same agent, leads
to the smallest performance gap. This indicates that the strategic value of
connecting two services derives from their market relationship rather than
shared ownership.
0.0 0.2 0.4 0.6 0.8 1.0
Time steps 1e6
25000
27500
30000
32500
35000
37500
40000
42500Average Total Revenue (95% CIs)
Base
0.0 0.2 0.4 0.6 0.8 1.0
Time steps 1e6
40000
42500
45000
47500
50000
52500
55000
57500
Large
Default No Competition No Coordination No Connectivity
Figure9: Ablationstudycomparingaveragetotalrevenuewitheachrelationtyperemoved.
5.6.2. How does message passing depth affect agent performance?
To evaluate the impact of network depth on agent performance, an ab-
lation study was conducted comparing variants with one, two, and three
R-GCN layers. The depth of the GNN determines how information is ag-
gregated for each service: a single-layer GNN aggregates information only
from adjacent services, whereas a two-layer or three-layer GNN expands it
to two-hop or three-hop neighbourhoods, respectively.
Figure 10 illustrates the average total revenue during training for each
depth setting. The two-layer configuration achieves the best performance
in both scenarios, followed by the one-layer and three-layer variants. This
30

can be attributed to the fact that it captures both, direct and connecting
services with one transfer, in contrast to the one-layer variant, which only
captures direct services, as price-sensitive passengers are willing to accept
longer journeys or transfers if the total fare is lower. In addition, the three-
layer variant exhibits the worst performance, which can suggest a smoothing
effect on the features of vertices, making them harder to distinguish and less
meaningful for decision-making [50].
0.0 0.2 0.4 0.6 0.8 1.0
Time steps 1e6
30000
32000
34000
36000
38000
40000
42000
44000Average Total Revenue (95% CIs)
Base
0.0 0.2 0.4 0.6 0.8 1.0
Time steps 1e6
37500
40000
42500
45000
47500
50000
52500
55000
57500
Large
One Layer Two Layers Three Layers
Figure 10: Ablation study comparing average total revenue for one, two, and three layers.
5.6.3. How does attention-based pooling compare to uniform aggregation?
The attention mechanism serves as a dynamic weighting function that
aggregates service-level embeddings into agent-level observations. To assess
the contribution of the learnt attention mechanism to agent performance,
the framework with learnt attention weights was compared against a variant
employing uniform attention weights. In the uniform attention variant, all
services receive an equal weight during the aggregation process, resulting
in the computation of a mean service embedding, rather than a weighted
combination.
Figure 11 presents the average total revenue during training for both
approaches. The results show that the uniform attention variant leads to a
slower learning process and, hence, to a worse sample efficiency compared to
the learnt attention method. Moreover, an interesting finding is that, once
enough experience has been collected, both variants converge to a similar
asymptotic performance. As a result, the multi-layer R-GCN compensates
for the lack of dynamic weighting by encoding later the relevant relational
context directly into the entity embeddings.
31

0.0 0.2 0.4 0.6 0.8 1.0
Time steps 1e6
30000
32000
34000
36000
38000
40000
42000
44000Average Total Revenue (95% CIs)
Base
0.0 0.2 0.4 0.6 0.8 1.0
Time steps 1e6
40000
42500
45000
47500
50000
52500
55000
57500
Large
Learnt Attention Uniform Attention
Figure 11: Ablation study comparing average total revenue of learnt attention weights
against uniform attention weights.
In addition, a visual representation of the cross-attention is shown in Fig-
ure 12, where the coordinate(i, j)represents the normalised mean attention
weight that agentiassigns to services operated by agentj. To analyse the
attention pattern, during the period in which the learnt mechanism provides
the advantage of the greater sample efficiency, the weights are aggregated
at training step 200K. Notably, the attention does not follow a uniform dis-
tribution, as there are weights concentrated along the main diagonal. This
behaviour is consistent with the partial observability of the environment,
since agents are only able to fully observe the services they control, so their
own entities provide a richer and more informative signal. Nevertheless, at-
tention is still assigned to competitor services, indicating that the visible
public attributes of rival entities are also informative.
5.6.4. How does decoupling representation learning from the actor affect the
training dynamics?
The framework detaches the aggregated observation from the computa-
tional graph when computing the actor update, so that the GNN parameters
are optimised only through the critics loss. The motivation behind this de-
sign choice is that, since they optimise different objectives, using both can
lead to a more unstable training of the agents. To evaluate its impact, the
default configuration is compared with a variant in which the representation
module is jointly updated by the critic and the actor losses.
Figure 13 shows the average total revenue during training for both vari-
ants. In particular, in the first scenario, the detached configuration results in
32

A1 A2 A3
Target Agent
A1
A2
A3 Source Agent
0.675 0.168 0.157
0.180 0.770 0.050
0.204 0.120 0.676
Base
A1 A2 A3 A4
Target Agent
A1
A2
A3
A4
0.578 0.156 0.138 0.129
0.065 0.764 0.094 0.077
0.055 0.049 0.855 0.041
0.040 0.043 0.047 0.870
Large
0.0
0.2
0.4
0.6
0.8
1.0
Attention
Figure 12: Normalised mean cross-attention weights between agents at training step 200K.
a policy with better performance and less variability across runs compared
to the other approach, whereas in the second scenario, it is the no detach
variant that achieves the higher revenue at the end of training. However, this
figure only reflects the revenue obtained by the agents in total.
0.0 0.2 0.4 0.6 0.8 1.0
Time steps 1e6
28000
30000
32000
34000
36000
38000
40000
42000
44000Average Total Revenue (95% CIs)
Base
0.0 0.2 0.4 0.6 0.8 1.0
Time steps 1e6
40000
42500
45000
47500
50000
52500
55000
57500
Large
Detach No Detach
Figure 13: Ablation study comparing average total revenue of detach and no detach vari-
ants.
To quantify the stability difference at agent level, for each run, a stability
metric is calculated as the standard deviation of the consecutive differences of
theindividualrevenue(Table5). Intuitively, thismetricisadiscreteanalogue
33

of the variability of the learning curve derivative, so smaller values indicate
that revenue increments from one step to the next are more consistent. More
specifically, the detached variant achieves the lowest value for every agent
in both scenarios, with this difference being more pronounced in the second
case. This implies that decoupling representation learning from the actor
stabilises the training dynamics of each agent individually, although there is
a trade-off with a reduced total revenue.
Table 5: Training stability per agent measured as the standard deviation of consecutive
differences of the individual revenue. The mean and the standard deviation were computed
over three independent runs.
Base Large
Detach No Detach Detach No Detach
Agent 1455.7±70.7498.9±144.0666.4±114.0846.1±195.3
Agent 2363.9±215.5441.2±13.6622.4±61.8943.7±17.3
Agent 3521.7±39.2537.1±100.9450.7±50.6649.3±61.2
Agent 4 - -356.2±37.7535.9±106.1
The lowest values are indicated in bold.
5.6.5. What do the learnt graph embeddings capture about agent strategies?
To understand the information encoded by the learnt embeddings, t-SNE
[51] visualisation was applied to the attention-weighted observations of the
trained agents. Specifically, these visualisations project the aggregated obser-
vation vectors˜za that serve as input to each agent’s actor and critic networks.
For each scenario, the three experimental runs with different random seeds
during the evaluation at the end of training are presented, with each point
representing an agent’s aggregated observation at a single time step. Each
observation point is coloured in two ways: first, by its controlling agent, to
reveal structural patterns in how different agents perceive the market, and
second, by its associated revenue, to uncover strategic value distributions.
Figure 14 illustrates the projections of the aggregated observations for
both scenarios. On the one hand, the agent-coloured projections show that
the aggregated observations of different agents are mapped to distinct, con-
tiguous regions of the latent space, with little overlap between them. This
can be attributed to the fact that each agent learns its own representation,
as each of them has its own GNN. Moreover, the partial observability of
34

the environment that hides private ticket-sales data of competitor services
encourages the same service to be encoded differently in each agent’s view
of the graph. On the other hand, the reward-coloured projections present a
similar pattern with high and low revenue points clustered together, rather
than being uniformly distributed. Therefore, this suggests that the learnt
embeddings appear to encode who is acting and how profitable the market
state is.
6. Conclusions and future work
This work introduces an entity relational actor-critic framework for par-
tially observable MARL with mixed competitive-cooperative settings. It
encodes the environment as graph of operational units with heterogeneous
edges, rather than decision-making agents or static infrastructure, connected
by competition, coordination, and connectivity relations. Each agent learns
a relational state representation through a multi-layer R-GCN, which is then
aggregated into an agent-level observation via a learnt attention mechanism,
and trains its policy under the CTDE paradigm by extending MATD3. The
framework has been evaluated in a railway pricing reinforcement learning en-
vironment in two different scenarios of increasing market complexity, where
it obtained a higher total revenue compared to the other MARL baselines
considered. Moreover, it achieved this with smaller price increments and a
higher percentage of passengers travelling compared to MATD3.
One potential benefit of the approach is the scalability with respect to the
market structure, due to the compact fixed-size agent embeddings and the
message passing paradigm that keep the model size independent of the num-
ber of services. This contrasts with the agent-based graph baseline GA-AC,
in which each operator is encoded into a single node and whose effectiveness
collapses in the larger scenario. According to the further studies, the compe-
tition and connectivity relations contribute the most to performance, while
the coordination relation, which is the closest to the agent-based modelling,
has the smallest impact. In addition, regarding the depth of the message
passing, the two-layer configuration achieves the highest revenue, since it
captures direct and connecting services with one transfer. Furthermore, the
attention mechanism improves sample efficiency in the early stages of train-
ing, and detaching the representation module from the actor gradients has
been shown to stabilise the individual agent training dynamics, even though
it can reduce the total revenue.
35

200
 100
 0 100 200
t-SNE Dimension 1
200
150
100
50
0
50
100
150
200
t-SNE Dimension 2
Colored by Agent (Reward/Ep: 40511.32)
Agent 1
Agent 2
Agent 3
200
 100
 0 100 200
t-SNE Dimension 1
200
150
100
50
0
50
100
150
200
t-SNE Dimension 2
Colored by Agent (Reward/Ep: 40160.62)
Agent 1
Agent 2
Agent 3
200
 100
 0 100 200
t-SNE Dimension 1
200
150
100
50
0
50
100
150
200
t-SNE Dimension 2
Colored by Agent (Reward/Ep: 42350.51)
Agent 1
Agent 2
Agent 3
200
 100
 0 100 200
t-SNE Dimension 1
200
150
100
50
0
50
100
150
200
t-SNE Dimension 2
Colored by Reward (Reward/Ep: 40511.32)
200
 100
 0 100 200
t-SNE Dimension 1
200
150
100
50
0
50
100
150
200
t-SNE Dimension 2
Colored by Reward (Reward/Ep: 40160.62)
200
 100
 0 100 200
t-SNE Dimension 1
200
150
100
50
0
50
100
150
200
t-SNE Dimension 2
Colored by Reward (Reward/Ep: 42350.51)
0
2000
4000
6000
8000
Reward (Profit)
(a) Base.
200
 100
 0 100 200
t-SNE Dimension 1
200
150
100
50
0
50
100
150
200
t-SNE Dimension 2
Colored by Agent (Reward/Ep: 56263.26)
Agent 1
Agent 2
Agent 3
Agent 4
200
 100
 0 100 200
t-SNE Dimension 1
200
150
100
50
0
50
100
150
200
t-SNE Dimension 2
Colored by Agent (Reward/Ep: 53274.74)
Agent 1
Agent 2
Agent 3
Agent 4
200
 100
 0 100 200
t-SNE Dimension 1
200
150
100
50
0
50
100
150
200
t-SNE Dimension 2
Colored by Agent (Reward/Ep: 52100.12)
Agent 1
Agent 2
Agent 3
Agent 4
200
 100
 0 100 200
t-SNE Dimension 1
200
150
100
50
0
50
100
150
200
t-SNE Dimension 2
Colored by Reward (Reward/Ep: 56263.26)
200
 100
 0 100 200
t-SNE Dimension 1
200
150
100
50
0
50
100
150
200
t-SNE Dimension 2
Colored by Reward (Reward/Ep: 53274.74)
200
 100
 0 100 200
t-SNE Dimension 1
200
150
100
50
0
50
100
150
200
t-SNE Dimension 2
Colored by Reward (Reward/Ep: 52100.12)
0
1000
2000
3000
4000
5000
6000
7000
8000
Reward (Profit)
(b) Large.
Figure 14: t-SNE visualisation of learnt agent observations coloured by agent and reward.
The clustering patterns suggest that the embeddings capture aspects of agent identity and
market profitability.
36

As future work, it is suggested to explore methods where agents could
directly discover which entities are connected to each other, rather than re-
lying on predefined edge types. For instance, this could be achieved by using
attention mechanisms that dynamically learn a relational structure based on
observed state transitions and rewards. The framework would also benefit
from modelling the temporal aspect within the graph structure itself. Cur-
rently, the entity graph is reconstructed at each time step based on static
rules, but many real-world systems present relations that evolve over time.
To this end, temporal graph networks [52] could be incorporated into the
model to capture relational changes as the environment evolves. Finally, only
off-policy methods are considered in this work, so future directions could ex-
tend the framework to on-policy algorithms in order to assess their potential
advantages in this setting.
CRediT authorship contribution statement
Enrique Adrian Villarrubia-Martin:Writing – original draft, Visu-
alisation, Validation, Software, Methodology, Data curation, Conceptualisa-
tion.David Muñoz-Valero:Writing – review & editing, Data curation,
Software.Luis Rodriguez-Benitez:Writing – original draft, Resources,
Methodology, Formal analysis.Giovanni Montana:Writing – review &
editing, Supervision, Methodology, Conceptualisation, Formal analysis.Luis
Jimenez-Linares:Supervision, Project administration, Methodology, Con-
ceptualisation, Funding acquisition.
Declaration of competing interest
The authors declare that they have no known competing financial inter-
ests or personal relationships that could have appeared to influence the work
reported in this paper.
Data availability
Data will be made available upon request.
Acknowledgments
This work was supported by grant PID2020-112967GB-C32 funded by
MCIN/AEI/10.13039/501100011033 and by the ERDF A Way of Making
37

Europe. It was completed when Enrique Adrian Villarrubia-Martin was a
predoctoral fellow at the Universidad de Castilla-La Mancha funded by the
European Social Fund Plus (ESF+) and in a visiting research stay at the
University of Warwick funded by a mobility grant from the Universidad de
Castilla-La Mancha for predoctoral students. Giovanni Montana acknowl-
edges support from a UKRI AI Turing Acceleration Fellowship (EPSRC
EP/V024868/1).
Appendix A. Hyperparameters
This section provides a comprehensive overview of the hyperparameters
used to train the algorithms. For a standardised comparison, the default hy-
perparametersofeachalgorithmwereusedwithoutadditionaltuning. Shared
hyperparametersarepresentedinTableA.1andareusedunlessanalgorithm-
specific table assigns a different value. Algorithm-specific configurations are
detailed in: Table A.2 for RACHE, Table A.3 for MADDPG, Table A.4 for
MATD3, Table A.5 for MAAC, and Table A.6 for GA-AC.
38

Table A.1: Shared hyperparameters between algorithms.
Hyperparameter Value
Number of environments 16
Optimiser Adam [53]
Buffer size 1,000,000
Training steps 1,000,000
Random policy episodes 1,000
Evaluation episodes 10,000
Number of hidden layers 2
Hidden units per layer 256
Non-linear activation function ReLU
Batch size 1024
Discount factor (γ) 0.99
Policy learning rate 0.001
Critic learning rate 0.001
Target smoothing coefficient (τ) 0.005
Steps per update 100
Seeds 0, 41, 73
Training environment seed{seed+r·1000|r∈ {0,1, . . . ,15}}
Evaluation environment seed{seed+r·100000|r∈ {0,1, . . . ,15}}
Observation normalisation Yes
Reward scaling 1000
Table A.2: RACHE hyperparameters.
Hyperparameter Value
Categorical embedding dim 4
Continuous embedding dim 128
R-GCN learning rate 0.001
R-GCN hidden dim 128
Number of R-GCN layers 2
Dropout 0.1
Attention score function MLP
39

Table A.3: MADDPG hyperparameters.
Hyperparameter Value
Discount factor (γ) 0.95
Policy learning rate 0.01
Critic learning rate 0.01
Exploration noise Ornstein-Uhlenbeck [54] θ= 0.15σ= 0.2
Table A.4: MATD3 hyperparameters.
Hyperparameter Value
Exploration noiseN(0,0.1)
Policy noiseN(0,0.2)
Policy noise clip 0.5
Frequency delayed policy updates 2
Table A.5: MAAC hyperparameters.
Hyperparameter Value
Non-linear activation function LeakyReLU
Number of attention heads 4
Number of updates per update cycle 4
Table A.6: GA-AC hyperparameters.
Hyperparameter Value
Entropy regularisation coefficient (α) 0.2
References
[1] J. Jiang, C. Dun, T. Huang, Z. Lu, Graph Convolutional Reinforcement
Learning, in: 8th International Conference on Learning Representations,
ICLR 2020, 2020.
[2] A. Goeckner, Y. Sui, N. Martinet, X. Li, Q. Zhu, Graph neural network-
based multi-agent reinforcement learning for resilient distributed co-
ordination of multi-robot systems, in: 2024 IEEE/RSJ International
40

Conference on Intelligent Robots and Systems (IROS), IEEE, 2024, pp.
5732–5739.
[3] S. Utke, J. Houssineau, G. Montana, Investigating relational state ab-
straction in collaborative marl, in: Proceedings of the AAAI Conference
on Artificial Intelligence, Vol. 39, 2025, pp. 20947–20955.
[4] E. Ardjmand, E. Izadi, A. Tavasoli, B. Moradi-Jamei, H. Shakeri,
Graph-embedded reinforcement learning for dynamic pricing and ad-
vertising under network effects, Applied Soft Computing 186 (2026).
doi:10.1016/j.asoc.2025.114056.
[5] Q. Liu, L. Zhang, M. J. Skibniewski, Network extension plan-
ning towards resilient urban critical infrastructures using deep
reinforcement learning, Applied Soft Computing 176 (2025).
doi:10.1016/j.asoc.2025.113163.
[6] T. Li, Y. Qin, M. Xu, Y. Zhou, L. Rong, Spatio-temporal vulnerability
ofhigh-speedraillinenetworkin china, TransportationResearchPart D:
Transport and Environment 134 (2024). doi:10.1016/j.trd.2024.104338.
[7] C. Gutiérrez-Hita, O. de la Cruz, R. Ramos-Melero, Infrastructure ac-
cess charges, service differentiation, and strategic competition in the eu
railway passenger market., Transportation Research Part B: Method-
ological 164 (2022). doi:10.1016/j.trb.2022.08.004.
[8] A. Agarwal, S. Kumar, K. Sycara, M. Lewis, Learning transferable co-
operative behavior in multi-agent team, in: Proceedings of the Interna-
tionalJointConferenceonAutonomousAgentsandMultiagentSystems,
AAMAS, Vol. 2020-May, 2020. doi:10.65109/edcb3795.
[9] S. Nayak, K. Choi, W. Ding, S. Dolan, K. Gopalakrishnan, H. Balakr-
ishnan, Scalable multi-agent reinforcement learning through intelligent
information aggregation, in: International conference on machine learn-
ing, PMLR, 2023, pp. 25817–25833.
[10] J. N. Foerster, G. Farquhar, T. Afouras, N. Nardelli, S. Whiteson, Coun-
terfactual multi-agent policy gradients, in: 32nd AAAI Conference on
Artificial Intelligence, AAAI 2018, 2018. doi:10.1609/aaai.v32i1.11794.
41

[11] R.Lowe, Y.Wu, A.Tamar, J.Harb, P.Abbeel, I.Mordatch, Multi-agent
actor-critic for mixed cooperative-competitive environments, in: Ad-
vances in Neural Information Processing Systems, Vol. 2017-December,
2017.
[12] J. Ackermann, V. Gabler, T. Osa, M. Sugiyama, Reducing overestima-
tion bias in multi-agent domains using double centralized critics, arXiv
preprint arXiv:1910.01465 (2019).
[13] V. Zambaldi, D. Raposo, A. Santoro, V. Bapst, Y. Li, I. Babuschkin,
K. Tuyls, D. Reichert, T. Lillicrap, E. Lockhart, M. Shanahan,
V. Langston, R. Pascanu, M. Botvinick, O. Vinyals, P. Battaglia, Deep
reinforcement learning with relational inductive biases, in: 7th Interna-
tional Conference on Learning Representations, ICLR 2019, 2019.
[14] E. A. Villarrubia-Martin, L. Rodriguez-Benitez, D. Muñoz-Valero,
G. Montana, L. Jimenez-Linares, Dynamic Pricing in High-Speed
Railways Using Multi-Agent Reinforcement Learning, arXiv preprint
arXiv:2501.08234 (2025).
[15] S. V. Albrecht, F. Christianos, L. Schäfer, Multi-Agent Reinforcement
Learning: Foundations and Modern Approaches, MIT Press, 2024.
URLhttps://www.marl-book.com
[16] D. Pang, J. Zhu, H. Meng, J. Cao, S. Liu, Data-driven optimal bipartite
containment control for heterogeneous multi-agent systems over coopeti-
tion networks, Journal of the Franklin Institute 362 (16) (2025) 108057.
doi:10.1016/J.JFRANKLIN.2025.108057.
[17] C. Yu, A. Velu, E. Vinitsky, J. Gao, Y. Wang, A. Bayen, Y. Wu, The
Surprising Effectiveness of PPO in Cooperative Multi-Agent Games, in:
Advances in Neural Information Processing Systems, Vol. 35, 2022.
[18] S. Iqbal, F. Sha, Actor-attention-critic for multi-agent reinforcement
learning, in: 36th International Conference on Machine Learning, ICML
2019, Vol. 2019-June, 2019, pp. 5261–5270.
[19] L. Hou, Y. Li, J. Yan, C. Wang, L. Wang, B. Wang, Multi-agent re-
inforcement mechanism design for dynamic pricing-based demand re-
sponse in charging network, International Journal of Electrical Power
and Energy Systems 147 (2023). doi:10.1016/j.ijepes.2022.108843.
42

[20] A. Fraija, N. Henao, K. Agbossou, S. Kelouwani, M. Fournier, S. Na-
garsheth, Deep reinforcement learning based dynamic pricing for de-
mand response considering market and supply constraints, Smart En-
ergy 14 (2024). doi:10.1016/j.segy.2024.100139.
[21] G. Sun, G. Boateng, L. Luo, H. Chen, D. Mensah, G. Liu, Competitive
Pricing for Resource Trading in Sliced Mobile Networks: A Multi-Agent
Reinforcement Learning Approach, IEEE Transactions on Mobile Com-
puting (2023). doi:10.1109/TMC.2023.3281203.
[22] H. Ma, H. Zhang, D. Tian, D. Yue, G. P. Hancke, Optimal
demand response based dynamic pricing strategy via Multi-Agent
Federated Twin Delayed Deep Deterministic policy gradient algo-
rithm, Engineering Applications of Artificial Intelligence 133 (2024).
doi:10.1016/j.engappai.2024.108012.
[23] T. N. Kipf, M. Welling, Semi-supervised classification with graph con-
volutional networks, in: 5th International Conference on Learning Rep-
resentations, ICLR 2017 - Conference Track Proceedings, 2017.
[24] Y. Liu, W. Wang, Y. Hu, J. Hao, X. Chen, Y. Gao, Multi-
Agent game abstraction via graph attention neural network, in:
AAAI 2020 - 34th AAAI Conference on Artificial Intelligence, 2020.
doi:10.1609/aaai.v34i05.6211.
[25] W. Hamilton, Z. Ying, J. Leskovec, Inductive representation learning
on large graphs, in: Advances in neural information processing systems,
Vol. 30, 2017.
[26] J. Yoon, K. Ahn, J. Park, H. Yeo, Transferable traffic signal con-
trol: Reinforcement learning with graph centric state representation,
Transportation Research Part C: Emerging Technologies 130 (2021).
doi:10.1016/j.trc.2021.103321.
[27] S.Yang, Hierarchicalgraphmulti-agentreinforcementlearningfortraffic
signal control, Information Sciences 634 (2023) 55–72.
[28] Z. Pang, X. Li, L. Gao, X. Zhang, J. Wu, Multi-relational
graph reinforcement learning for dynamic flexible job-shop schedul-
ing under machine breakdowns, Applied Soft Computing 190 (2026).
doi:10.1016/j.asoc.2026.114587.
43

[29] L. Ning, M. Zhou, Z. Hou, R. Goverde, F.-Y. Wang, H. Dong, Deep De-
terministic Policy Gradient for High-Speed Train Trajectory Optimiza-
tion, IEEE Transactions on Intelligent Transportation Systems 23 (8)
(2022) 11562–11574. doi:10.1109/TITS.2021.3105380.
[30] P. Yue, Y. Jin, X. Dai, Z. Feng, D. Cui, Reinforcement Learning
for Scalable Train Timetable Rescheduling With Graph Representa-
tion, IEEE Transactions on Intelligent Transportation Systems (2024).
doi:10.1109/TITS.2023.3344468.
[31] S. Mohanty, E. Nygren, F. Laurent, M. Schneider, C. Scheller, N. Bhat-
tacharya, J. Watson, A. Egli, C. Eichenberger, C. Baumberger, others,
Flatland-rl: Multi-agentreinforcementlearningontrains, arXivpreprint
arXiv:2012.05893 (2020).
[32] R. Mohammadi, Q. He, A deep reinforcement learning approach for rail
renewal and maintenance planning, Reliability Engineering and System
Safety 225 (2022). doi:10.1016/j.ress.2022.108615.
[33] G. Arcieri, C. Hoelzl, O. Schwery, D. Straub, K. Papakonstantinou,
E. Chatzi, POMDP inference and robust solution via deep reinforce-
ment learning: an application to railway optimal maintenance, Machine
Learning (2024). doi:10.1007/s10994-024-06559-2.
[34] W. Feng, W. Dong, S. Zhai, G. Zhang, X. Sun, Y. Ji, A deep reinforce-
ment learning method for freight train driving based on domain knowl-
edge and mass estimation network, in: ACM International Conference
Proceeding Series, 2021, pp. 41–46. doi:10.1145/3468891.3468898.
[35] Y. Cui, G. Zhang, W. Dong, X. Sun, W. Yang, Knowledge-based Deep
Reinforcement Learning for Train Automatic Stop Control of High-
Speed Railway, in: ACM International Conference Proceeding Series,
2020, pp. 31–36. doi:10.1145/3426826.3426833.
[36] J.Lin, X.Qiu, M.Li, Trackingintervalcontrolforurbanrailtrainsbased
on safe reinforcement learning, Engineering Applications of Artificial
Intelligence 137 (2024). doi:10.1016/j.engappai.2024.109226.
[37] J. Li, Z. Chen, Y. Zheng, S. H. Chan, D. Harabor, P. J. Stuckey, H. Ma,
S. Koenig, Scalable Rail Planning and Replanning: Winning the 2020
44

FlatlandChallenge, in: 14thInternationalSymposiumonCombinatorial
Search, SoCS 2021, 2021, pp. 477–485. doi:10.1609/socs.v12i1.18576.
[38] M. Littman, Markov games as a framework for multi-agent reinforce-
ment learning, in: Proceedings of the 11th International Conference on
Machine Learning, ICML 1994, 1994, pp. 157–163. doi:10.1016/B978-1-
55860-335-6.50027-1.
[39] F. A. Oliehoek, C. Amato, A Concise Introduction to Decentralized
POMDPs, 1st Edition, Springer Publishing Company, Incorporated,
2016.
[40] P.W.Battaglia, J.B.Hamrick, V.Bapst, A.Sanchez-Gonzalez, V.Zam-
baldi, M. Malinowski, A. Tacchetti, D. Raposo, A. Santoro, R. Faulkner,
others, Relational inductive biases, deep learning, and graph networks,
arXiv preprint arXiv:1806.01261 (2018).
[41] L. Ugadiarov, V. Vorobyov, A. Panov, Relational Object-Centric Actor-
Critic, in: Proceedings of Machine Learning Research, Vol. 275, 2025,
p. 1450 – 1476.
[42] M. Schlichtkrull, T. N. Kipf, P. Bloem, R. Van Den Berg, I. Titov,
M.Welling, Modelingrelationaldatawithgraphconvolutionalnetworks,
in: European semantic web conference, Springer, 2018, pp. 593–607.
[43] K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image recog-
nition, in: Proceedings of the IEEE Computer Society Conference on
Computer Vision and Pattern Recognition, Vol. 2016-December, 2016.
doi:10.1109/CVPR.2016.90.
[44] J. L. Ba, J. R. Kiros, G. E. Hinton, Layer normalization, arXiv preprint
arXiv:1607.06450 (2016).
[45] M. Zaheer, S. Kottur, S. Ravanbhakhsh, B. Póczos, R. Salakhutdinov,
A. J. Smola, Deep sets, in: Advances in Neural Information Processing
Systems, Vol. 2017-December, 2017.
[46] S. Fujimoto, H. Van Hoof, D. Meger, Addressing Function Approxima-
tion Error in Actor-Critic Methods, in: 35th International Conference
on Machine Learning, ICML 2018, Vol. 4, 2018, pp. 1587–1596.
45

[47] T. P. Lillicrap, J. J. Hunt, A. Pritzel, N. Heess, T. Erez, Y. Tassa, D. Sil-
ver, D. Wierstra, Continuous control with deep reinforcement learning,
in: 4th International Conference on Learning Representations, ICLR
2016 - Conference Track Proceedings, 2016.
[48] T. Haarnoja, A. Zhou, P. Abbeel, S. Levine, Soft actor-critic: Off-policy
maximum entropy deep reinforcement learning with a stochastic actor,
in: 35th International Conference on Machine Learning, ICML 2018,
Vol. 5, 2018, pp. 2976–2989.
[49] R. Agarwal, M. Schwarzer, P. S. Castro, A. Courville, M. G. Bellemare,
Deep reinforcement learning at the edge of the statistical precipice, in:
Advances in Neural Information Processing Systems, Vol. 35, 2021.
[50] Q. Li, Z. Han, X. M. Wu, Deeper insights into graph convolutional
networks for semi-supervised learning, in: 32nd AAAI Conference on
Artificial Intelligence, AAAI 2018, 2018. doi:10.1609/aaai.v32i1.11604.
[51] L. Van Der Maaten, G. Hinton, Visualizing data using t-SNE, Journal
of Machine Learning Research 9 (2008).
[52] E.Rossi, B.Chamberlain, F.Frasca, D.Eynard, F.Monti, M.Bronstein,
Temporal graph networks for deep learning on dynamic graphs, arXiv
preprint arXiv:2006.10637 (2020).
[53] D. Kingma, J. Ba, Adam: A method for stochastic optimization, in:
3rd International Conference on Learning Representations, ICLR 2015
- Conference Track Proceedings, 2015.
[54] G. E. Uhlenbeck, L. S. Ornstein, On the theory of the Brownian motion,
Physical Review 36 (5) (1930). doi:10.1103/PhysRev.36.823.
46
