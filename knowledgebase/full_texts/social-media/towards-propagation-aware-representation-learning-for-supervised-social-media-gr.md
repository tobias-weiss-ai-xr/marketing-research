---
title: Towards Propagation-aware Representation Learning for Supervised Social Media Graph Analytics
url: https://arxiv.org/abs/2509.01124
category: social-media
subcategory: empirical
date: 2025-09
venue: ''
authors:
- Wei Jiang
- Tong Chen
- Wei Yuan
- Xiangyu Zhao
- Quoc Viet Hung Nguyen
source: arxiv
pdf_url: https://arxiv.org/pdf/2509.01124
pages: 11
chars: 58688
fetched_at: '2026-11-08T13:06:31+00:00'
kb_version: 1
---

# Towards Propagation-aware Representation Learning for Supervised Social Media Graph Analytics

Towards Propagation-aware Representation Learning
for Supervised Social Media Graph Analytics
Wei Jiang1, Tong Chen 1, Wei Yuan1, Xiangyu Zhao 2, Quoc Viet Hung Nguyen 3, Hongzhi Yin 1∗
1The University of Queensland, Australia
2City University of Hong Kong, Hong Kong
3Griffith University, Australia
{wei.jiang, tong.chen, w.yuan, h.yin1 }@uq.edu.au, xy.zhao@cityu.edu.hk, henry.nguyen@griffith.edu.au
Abstract—Social media platforms generate vast, complex
graph-structured data, facilitating diverse tasks such as rumor
detection, bot identification, and influence modeling. Real-world
applications like public opinion monitoring and stock trading –
which have a strong attachment to social media – demand models
that are performant across diverse tasks and datasets. However,
most existing solutions are purely data-driven, exhibiting vulner-
ability to the inherent noise within social media data. Moreover,
the reliance on task-specific model design challenges efficient
reuse of the same model architecture on different tasks, incurring
repetitive engineering efforts. To address these challenges in
social media graph analytics, we propose a general representation
learning framework that integrates a dual-encoder structure
with a kinetic-guided propagation module. In addition to jointly
modeling structural and contextual information with two en-
coders, our framework innovatively captures the information
propagation dynamics within social media graphs by integrat-
ing principled kinetic knowledge. By deriving a propagation-
aware encoder and corresponding optimization objective from
a Markov chain-based transmission model, the representation
learning pipeline receives a boost in its robustness to noisy data
and versatility in diverse tasks. Extensive experiments verify
that our approach achieves state-of-the-art performance with a
unified architecture on a variety of social media graph mining
tasks spanning graph classification, node classification, and link
prediction. Besides, our solution exhibits strong zero-shot and
few-shot transferability across datasets, demonstrating practical-
ity when handling data-scarce tasks. The code is available at
https://github.com/WeiJiang01/RPRL.
Index Terms—Represenation Learning; Social Media Analyt-
ics; Graph Learning
I. I NTRODUCTION
With the rapid expansion of the Internet, social media plat-
forms such as X, Facebook and Weibo have become the central
hub for information dissemination and public discourse [1],
[2]. To maximize the value of numerous interactions on these
platforms, there is an ongoing trend to model social media data
as graphs for a wide range of analyses [3]–[7]. Among them,
supervised predictive tasks have enjoyed prolonged popularity
[8], [9]. Based on the granularity of both graphs and labels,
supervised social media graph analytics can be categorized
into three core tasks: (1) graph classification, where one
example is rumor detection [10] that predicts the veracity of
the source information given its propagation graph; (2) node
∗Hongzhi Yin is the corresponding author.
classification, such as detecting anomalous users or social
bots [11] within a large user network; and (3) link prediction,
where a typical instance is information cascade prediction [12].
While significant progress has been made in each type of
these tasks, they are often studied independently, with task-
specific models designed around the structural characteris-
tics of their input graphs. For instance, graph classification
usually involves small-scale graphs representing information
dissemination in a short time period, where models focus
on capturing global structural patterns such as centrality and
depth [13]–[15]. In node classification, the input is typically
a single, large-scale social network, and models learn to
infer node labels using local neighborhood structures and
node attributes [16]–[19]. Link prediction, by contrast, often
requires reasoning over dynamic or higher-order structures
such as temporal graphs or hypergraphs, demanding more
sophisticated models like transformers or hypergraph neural
networks [20]–[22].
However, these specialized approaches face several critical
limitations. First, it is notoriously challenging to train effective
graph representation learning models with social media data,
which is commonly agreed to be rich-yet-noisy [14], [23], [24]
(e.g., incompleteness, temporal shifts, spurious edges, etc.).
This issue is further amplified considering that most existing
solutions bear a purely data-driven design [14]. Second, in
real-world applications where social media plays a central role,
the combined power of multiple graph tasks [25], [26] is in
high demand. For example, political consulting agencies need
the insight from diverse social media mining tasks to inform
campaign strategy during an election [27], while stock trading
firms also clearly benefit from various aforementioned tasks
to estimate the public’s confidence in certain industries [28].
When operated at scale, designing separate models for each
task not only incurs substantial engineering efforts, but also
risks a high opportunity cost from the repetitive trial-and-error
process in the search for optimal model designs. As such, both
factors highlight a critical utility gap between the outgoing,
task-specific solutions and practical deployment, and motivate
the pursuit of a generic model architecture capable of handling
all three task types when trained with corresponding datasets.
Nevertheless, achieving such structural unification remains
highly non-trivial. First, the substantial heterogeneity across
arXiv:2509.01124v1  [cs.SI]  1 Sep 2025

tasks poses a major challenge, necessitating a generalizable
encoder that can effectively model diverse graph structures and
feature spaces. Second, learning the dynamics of information
propagation is essential for most social media graph mining
tasks, yet current methods lack a principled mechanism to
describe and quantify these patterns in a consistent and trans-
ferable manner across datasets and tasks. In contrast, other do-
mains have demonstrated the potential of integrating physics-
informed or first-principle knowledge to guide learning. For
instance, traffic forecasting and air quality prediction have
successfully incorporated energy-based formulations to model
spatiotemporal dynamics through physical laws of energy
transfer. These successes further motivate us to explore the use
of first principle knowledge to guide representation learning of
information propagation in social media networks [29], [30],
which can potentially serve as a unifying principle for social
media graph learning.
To this end, we design a general architecture that inte-
grates data-driven modeling with principled propagation mech-
anisms. Concretely, we propose a parallel encoding module
that jointly captures graph topology and global context. It
consists of two complementary encoders: a structure-aware
graph encoder that models local dependencies based on actual
connectivity, and a structure-agnostic context encoder that
captures global interactions across all nodes regardless of edge
information. This design enables flexible adaptation to graphs
of varying sizes and structures across different tasks. Beyond
architectural flexibility, we incorporate domain knowledge
of information propagation to guide representation learning.
Specifically, we define an information propagation graph char-
acterized by binary node states that reflect activation patterns
over time. These state transitions are modeled using a kinetic
model based on microscopic dynamics [31]–[33]. To integrate
this mechanism into training, we further introduce a kinetic-
guided objective that aligns the predicted state evolution with
the derivatives defined by an ordinary differential equation.
This provides physically grounded supervision without requir-
ing labeled states and enhances the ability of our method to
learn propagation-aware representations that generalize across
heterogeneous graph tasks. Moreover, with the introduction of
the kinetic model, the previously mentioned vulnerability to
inherent data noise can also be addressed. As a result, the
proposed framework is robust and applicable across diverse
tasks in a task-specific manner, while also exhibiting strong
cross-dataset generalization, making it well-suited for practical
use in real-world social media analytics.
Our main contributions are summarized as follows:
• We identify a general underlying mechanism across di-
verse graph-based tasks in social media graph analytics
and formalize it as the information propagation graph.
This abstraction provides a task-agnostic supervisory
signal that enhances representation learning beyond ob-
served features and topologies.
• We propose a general architecture that integrates data-
driven representation learning with kinetic model-guided
supervision. It employs a dual-encoder architecture to
capture both structural and contextual semantics, and
incorporates a kinetic-guided loss to align learned node
state dynamics with physical propagation principles, en-
abling versatility across heterogeneous graph structures.
• We conduct extensive experiments across graph classifi-
cation, node classification, and link prediction on multiple
real-world social media datasets. Our method achieves
state-of-the-art performance on each task and demon-
strates strong zero- and few-shot transfer capabilities
across datasets and task settings.
II. R ELATED WORK
Below we present related work for three supervised learning
tasks in social media network analysis, i.e., graph classifica-
tion, node classification, and link prediction along with their
primary applications.
Graph Classification. The goal of graph classification in
social media network is to assign a single label to an entire
graph structure. One prominent application is rumor detection,
where each instance is represented as a propagation tree
or network, and the model must decide if that propagation
graph conveys misinformation or factual content. For example,
BiGCN treats a rumor propagation tree as a graph and learns
bidirectional propagation patterns (top-down and bottom-up)
to produce a graph-level embedding for classification [34].
Recent methods further refine the graph-level representation
by incorporating structural priors such as node centrality mea-
sures or epidemiological diffusion patterns into the embedding
process [13], [14].
Node Classification. In node classification task, each user
(node) in a social network graph is labeled independently,
e.g., as “bot” or “human.” BotRGCN applies a relational
graph convolutional network (RGCN) over a multi-relation
user graph (retweets, mentions, follows, etc.) to learn per-node
features that capture heterogeneous neighborhood signals, then
classifies each node based on its aggregated embedding [16].
RGT augments this by adding a self-attention mechanism
over the same multi-relational graph, allowing the model to
weigh information from different relation types dynamically
and focus on the most informative neighbors during node
embedding construction [35].
Link Prediction. In link prediction, the model receives partial
information about an evolving graph (e.g., nodes and edges
observed so far in a cascade) and must predict which new
user–user or cascade–user edge will form next. DyHGCN
tackles this by jointly encoding the static social network and
the dynamic diffusion cascade graph with temporal encod-
ings and multi-head attention; it then scores candidate edges
between users and the cascade to forecast the next spread
step [36]. MS-HGAT extends this by constructing a sequen-
tial hypergraph over user interactions within each cascade
and applying hypergraph attention layers, supplemented by a
memory-enhanced embedding lookup that captures each user’s
evolving preference in the diffusion process [20]. RotDiff
departs from Euclidean embeddings altogether by mapping
2

users and cascades into a hyperbolic space: rotation transfor-
mations in hyperbolic geometry encode hierarchical influence
and asymmetric spread patterns, and edge likelihoods are
computed via hyperbolic distance metrics [21].
Although each family of methods excels within its desig-
nated task, they are required significant re-engineering of data
representations or architectural components for other tasks.
This siloed design incurs heavy modeling overhead when
extending to new social media analysis tasks. In contrast, our
method unifies all three problem settings under a single back-
bone with task-specific heads, enabling end-to-end learning
for rumor detection, social-bot identification, and diffusion
forecasting without rebuilding separate models for each.
III. P RELIMINARIES
A. Problem Definition
In this paper, we aim to design a cross-task architecture that
can achieve advantageous performance when trained for each
task. As per our discussions earlier, we focus on three key tasks
within the domain of supervised social media graph analytics:
graph classification, node classification, and link prediction.
Note that although the training process is task-specific due
to the use of different objectives and hyperparameters, the
same model architecture can be directly reused across tasks to
minimize engineering costs. Below, we formally define each
of these tasks.
Graph Classification: Graph classification task in the con-
text of social media graph analytics can be formulated as
classifying the type of root post using the whole information
of a small scale propagation tree. Given a propagation tree
GR,i = (Vi, Ei, X i), where Vi = {v(i) 0 , v(i) 1 , . . . , v(i) n } denotes
the set of nodes corresponding to posts within an event with
the root post v0, Ei denotes the set of edges capturing the reply
or retweet structure, and X i = [x0, x1, . . . , xn]T denotes the
node feature matrix. The objective of this task is to map each
root post v(i) 0 , along with its associated graph GR,i and textual
features X i, to a binary label yi ∈ {0, 1}.
Node Classification: Node classification is formulated as a su-
pervised binary classification of nodes on a multi-relational so-
cial network. The social network is defined as GS = (V, E, X),
where V = {vi | i = 1 , 2, . . . , n} denotes the set of nodes,
E = ∪R r=1Er is the set of edges under R relation types (e.g.
following, follower and reply), and X is the feature matrix,
with each row X i representing the feature vector of node vi.
The objective of this task is to use G and the labels of training
nodes Y train to predict the labels of unseen nodes Y test.
Link Prediction: We formulate the link prediction task in the
context of social network and its information diffusion cascade
sequences, where the goal is to predict the next user likely to
be linked in an ongoing diffusion cascade sequence Cc =
{(uc 1, tc 1), . . . ,(uc n, tc n)}. Given a dataset D containing a set of
historical cascades C = {C1, · · ·, C|C|} and a social network
GD = (V, E) encompassing all users in D, the task is to predict
the next link from the current cascade to a potential target user.
Specifically, given a query sequence q = {uq 1, · · ·, uq m}, the
objective is to predict the next user uq m+1 who will be linked,
by leveraging the historical cascade patterns and the structural
information in GD.
B. Information Propagation Graph
All three tasks in social media networks rely on graph-
structured data constructed from user-generated content and
interactions. Since both information propagation tree and
social networks reflect how information spreads among users
[37], [38], the underlying propagation structure in these tasks
can be regarded as information propagation graph, which is
denoted as GIP = (V, E, S) and shown in Figure 1. Here, V
and E represent the sets of nodes and edges, respectively, and
S = {U, I1, I2} defines the possible states of each node: an
initial unknown state U, and two binary informative states, I1
and I2, which abstract states as positive or negative.
Graph Classification
Propagation Tree Social Network
Link Prediction
Social Network
Interaction Path
Node Classification
𝑡
𝑡1 𝑡2 𝑡3𝑡0
Information Propagation Graph
root
Positive State Negative State
ego
root
Unknown State
Fig. 1: Information Propagation Graph. This graph is an
abstraction derived from the propagation tree or the social
networks. All the nodes remain in the initial unknown state at
time t0. Gradually, nodes at hop-i transition from the unknown
state to either a positive or negative state at time step ti.
In GIP, nodes transition from the unknown state U to either
I1 or I2 as information propagates through the network,
typically emanating from an ego (or root) node. Specifically,
at time t0, all nodes are initialized in state U, and at each
subsequent time step ti, hop- i neighbors of the ego node
may transition to either I1 or I2, depending on the dynamics
of propagation. The specific semantics of the binary states
depend on the task: they represent supporting and denying
comments based on the stances of users, or interacted and
non-interacted users (e.g., following, follower, and reply), or
active and inactive users in an information cascade session.
IV. P ROPOSED FRAMEWORK
In this section, we present the proposed Robust Propagation-
aware Representation Learning (RPRL) framework, a cross-
task architecture designed to address graph classification,
node classification, and link prediction in social media an-
alytics. As illustrated in Figure 2, RPRL consists of three
key components: (1) a data-driven dual-encoder module, (2)
a propagation-aware representation learning module, and (3)
3

Info-Propagation Graph Task-specific Embeddings
Structure-agnostic
Context Encoder
Graph Encoder
Propagation-aware
Encoder
Fusion
Task-specific Adapter
Structure-agnostic
Embeddings
Kinetic-guided
Loss Function
St
a
Pr
ob
Pr
ob
State
Prob
𝑇
Data-driven Dual-Encoder
Linear Layers
𝑇
Predicted Probabilities
Numerical Results
𝛽
ℒ𝑝ℒ
Projection
𝑡𝑡3𝑡0 𝑡2𝑡1
Masked Node
Propagation-aware
Embeddings
Node Embedding Masking
Fig. 2: Overview of Robust Propagation-aware Representation Learning Framework
task-specific adapter and optimization. The details of each
module are described below.
A. Data-driven Dual-Encoder
The variation in graph structures and scales across tasks
leads to multifaceted modeling priorities. For instance, propa-
gation trees in graph classification task are typically small in
scale, whereas the social networks in node classification and
link prediction are significantly larger. Therefore, the emphasis
on capturing local structure versus global contextual informa-
tion varies across tasks, depending on the nature and scale
of the underlying graphs. To ensure social graph information
is captured at different granularities, we design a parallel
architecture that captures both graph topology semantics and
global contextual representations for data-driven representa-
tion learning. The architecture consists of two key encoders:
a Structure-agnostic Context Encoder, which models global
contextual relationships by enabling interactions between any
pair of nodes regardless of graph connectivity; and a Graph
Encoder, which captures local structural dependencies by
leveraging the actual graph topology. We first pass the node
feature xi of node i through a task-specific projection layer:
˜xi = projection(xi), (1)
where the projection layer is implemented as a linear trans-
formation for both graph and node classification tasks, and
as an embedding initialization method following the setup in
[20] for the link prediction task. Given the transformed ˜xi and
the information propagation graph GIP, the Structure-agnostic
Context Encoder and Graph Encoder can be formulated as:
hi = Encodercontext(˜xi),
ei = Encodergraph(GIP, ˜xi), (2)
where hi is the output embedding from Structure-agnostic
Context Encoder and ei is the output embedding from Graph
Encoder. In this work, we adopt multi-head transformer blocks
as the Structure-agnostic Context Encoder and a graph neural
network with residual layers based on the setting of [39] as
the Graph Encoder.
B. Propagation-aware Representation Learning
Most existing solutions on social media graph analytics
primarily focus on node-level content features, local neigh-
borhood aggregation, or the temporal dynamics of the data
itself. However, they often overlook the structured dynamics
of information propagation within the network when guided
by kinetic knowledge. As defined in Section III-B, the infor-
mation propagation graph includes binary propagation states,
namely positive and negative, which provide additional seman-
tic signals beyond the observed data. These node-level states
enrich the modeling of the propagation process by offering
interpretable supervision over how information spreads. The
objective of this module is to learn the probability distribu-
tion over these binary states from task-specific data, and to
incorporate this information into the optimization process.
Propagation-aware Encoder. We first introduce a
Propagation-aware Encoder that models the simulated
propagation process across the graph, enabling the learning
of richer representations that better align with real-world
propagation behavior. We begin by applying a Node
Embedding Masking to simulate the progressive activation of
nodes in the propagation process, the implementation is shown
in Algorithm 1. At time step t, only nodes that are within a
t-hop distance from the ego node vego are considered active.
These nodes are assumed to have received the propagated
information and are allowed to contribute their embeddings
to downstream attention computation. In contrast, nodes that
lie beyond the t-hop boundary are considered inactive at this
stage. Instead of directly removing them, we apply zeroing
masking to their embeddings, allowing the model to retain a
4

Algorithm 1 Node Embedding Masking
Input: Propagation graph G = (V, E), node features {hj}j∈V,
ego node vego, current time step t
Output: Masked node embeddings {˜h(t) j }j∈V
1: for each node j ∈ Vdo
2: Compute dj ← dist(vego, j)
3: if dj ≤ t then
4: m(t) j ← 1
5: else
6: m(t) j ← 0
7: end if
8: ˜h(t) j ← m(t) j · hj
9: end for
10: return {˜h(t) j }j∈V
consistent dynamic structure while suppressing their semantic
contribution.
Formally, let dj = dist(vego, j) denote the shortest path
distance (in number of hops) from the ego node to node j.
We define a binary mask m(t) j ∈ {0, 1} for each node j at
time step t as:
m(t) j =
(
1, if dj ≤ t
0, otherwise. (3)
The masked node feature is then computed as:
˜h (t) j = m(t) j · hj (4)
where hj is the structure-agnostic embedding of node j, and
˜h (t) j is its masked embedding at time t.
This masking operation is applied prior to the propagation-
aware encoder. At each time step, the model processes the
masked embeddings of all nodes using shared transformer
blocks without graph structure:
z(t) i = Encoderprop({˜h (t) j }(j,t′)∈Ct i ), (5)
where
Ct i = {(j, t′)|j ∈ V, 0 ≤ t′ ≤ t}. (6)
Finally, we derive the probabilities of the shared state s for
each node:
p

y(t) i = s

 n h(t) j o (j,t′)∈C(t) i  = softmax  W shout(t) i + bs  ,
for s ∈ S= {U, l1, l2}
(7)
where W s and bs are learnable parameter and bias, s is
the possible state of node i. However, relying solely on
propagation-aware embedding to enhance data-driven repre-
sentations is insufficient, as these embeddings are inherently
learned through dynamic transformations of the input data.
Consequently, their quality remains sensitive to data noise and
imperfections, which can lead to suboptimal model perfor-
mance.
Markov Chain-based Kinetic Model. To address this chal-
lenge, we incorporate domain knowledge to guide the learning
of propagation-aware embeddings. The micro-dynamic tran-
sitions of node states driven by information propagation in
complex networks can be described using a Markov chain-
based kinetic model. This model has been widely applied
in fields such as epidemiology, information diffusion, and
circuit power systems, etc [31]–[33]. Based on the information
propagation graph defined in Section III-B, we adapt a binary-
state kinetic model that reflects the spread of rumors or infor-
mation in social networks based on [32]. This model captures
the fine-grained dynamics by which node states transition
from the unknown state to either a positive or negative state
during the propagation process. Given the state probabilities
{Uv(t), I1,v(t), I2,v(t)} of node i at time t, the kinetic model
is denoted as:



dUv(t)
dt =
X
k
−Uv(t)βk
X
j∈N
av,j Ik,v(t)
dIk,v(t)
dt = Uv(t)βk
X
j∈N
av,j Ik,v(t),
s.t. Uv(t) +
X
k
Ik,v(t) = 1,
(8)
where av,j is the element of adjacency matrix in the informa-
tion propagation graph, av,j = 1 if node v and j are connected,
otherwise it is 0, βk is the transition coefficient from unknown
state U to Ik.
Kinetic-guided Loss Function. To ensure that the predictions
of state probabilities from Equation (7) respect these physical
constraints, we define a kinetic-guided loss by minimizing
the residuals between the predicted state dynamics and the
ODE-defined derivatives, enabling physical supervision in the
propagation-aware encoder without requiring labeled states.
We first denote the predicted probabilities as:
ˆUi(t) = p

y(t) i = U

 n ˜h (t) j o (j,t′)∈C(t) i  ,
ˆIk,i(t) = p

y(t) i = Ik

 n ˜h (t) j o (j,t′)∈C(t) i  . (9)
Given these predictions of probabilities, we then compute
the kinetic-guided loss by minimizing the residuals defined by
the kinetic model:
Lp =
X
i

 d ˆUi(t)
dt −

X
k
− ˆUi(t) ˆβk
X
j∈N
ai,j ˆIk,i(t)




2
+
X
i
X
k

 d ˆIk,i(t)
dt − ˆUi(t) ˆβk
X
j∈N
ai,j ˆIk,i(t)


2
,
(10)
where ˆβk can be learned by a linear layer with propagation-
aware embedding zout(t) i . We approximate the time derivative
d ˆXi(t)
dt using a discretized forward difference quotient. Specifi-
5

cally, given the predicted variable ˆXi(t) at discrete time steps,
the derivative is approximated as:
d ˆXi(t)
dt ≈
ˆXi(t + ∆t) − ˆXi(t)
∆t . (11)
In our setting, each time step t corresponds to a discrete
hop in the information propagation process, where nodes
progressively become activated based on their hop distance
from the ego node. Since the propagation steps are uniformly
defined over hop distances, we assume a unit time interval
(∆t = 1) between consecutive steps. The forward difference
quotient provides a first-order estimate of the temporal change
in predicted state probabilities, aligned with the discrete nature
of the propagation-aware encoding process.
C. Task-specific Adapters and Model Optimization
The propagation-aware embedding z(t) i optimized by the
kinetic-guided loss not only captures the dynamic patterns
of simulated information propagation, but also benefits from
the guidance and constraints provided by domain knowledge.
This results in an enhanced structure-agnostic embedding ˆhi
that can be effectively integrated with the structure-agnostic
embedding hi as follows:
ˆhi = hi + σ(z(t) i ), (12)
where σ is an activation function. Since the graph structures
and node features vary significantly across tasks, and each task
may emphasize different aspects of the data, it is necessary to
fuse the enhanced structure-agnostic embedding with the graph
embedding. This fusion allows the model to simultaneously
capture information from both global and structural perspec-
tives, thereby improving the overall representation capacity
and robustness of our method. We then input the graph
embedding ei and enhanced structure-agnostic embedding ˆhi
to a fusion layer:
oi = γ · ei + (1 − γ) · ˆhi, (13)
where γ is the coefficient that controls the contribution of
graph structural information during learning. The output em-
bedding oi is passed through a task-specific adapter to produce
the final prediction.
Graph Classification. For graph classification, each input
sample consists of a small-scale propagation tree GR along
with its corresponding node features X i. We input X i to
Equation (1) and obtain the output embeddings oi through
the above learning process, the graph classification adapter
first applies a graph pooling operation, followed by a linear
transformation layer to produce the final prediction pg:
og = Pooling(O),
pg = softmax(W gog + bg), (14)
where O is the combination of all nodes’ output embeddings,
W g and bg are the parameters of graph-level output layer.
Node Classification. For node classification, the input consists
of a large-scale social network GS along with node features X,
where each node serves as an individual classification target.
We input X to Equation (1) and learn the output embedding oi
of each node through the preceding steps, the final prediction
for each node is obtained by applying a linear transformation:
pi = softmax(W ooi + bo), (15)
where W o and bo are the parameters of node-level output
layer.
Link Prediction. For link prediction, each input sample
consists of a cascade sequence Cc and a large-scale social
network GD. We input the concatenated feature Xall =
concatenate(x1, . . . ,xN ) to Equation (1), and derive the out-
put embedding Oall from the previous steps, to predict which
node is most likely to be linked to Cc. A linear output layer
is applied to perform this prediction:
P = softmax(W pOall + Maskp), (16)
where W p is the parameter matrix of link prediction output
layer. P is the matrix of activation probabilities for all users.
Maskp is using for masking the users who have been in the
cascade. Mask i,p = −∞ if user i is already in the cascade,
else Mask i,p = 0.
Model Optimization. Finally, we derive three types of pre-
dictions corresponding to different tasks: (1) the graph-level
prediction pg for graph classification, where the goal is to
predict the category of the root post in a propagation tree;
(2) the node-level prediction pi for node classification, which
assigns category labels to each node in a social network;
and (3) the link-level prediction P for link prediction, which
predicts the likelihood of each node in the social network being
linked to a given cascade sequence Cc. For all the tasks, a
softmax function is applied to the model outputs to obtain
probability distributions. The resulting predictions are then
supervised using a cross-entropy loss, denoted as Ls, and the
final optimization objective function of RPRL is:
L = Ls + λLp, (17)
where Lp is the kinetic-guided loss function, λ controls the
contribution of the kinetic-guided loss in the overall objective.
V. E XPERIMENTS
A. Experimental Settings
In our experiments, we evaluate the effectiveness of the
proposed RPRL on three real-world applications: rumor de-
tection, social-bot detection, and information diffusion. These
applications correspond to the tasks of graph classification,
node classification, and link prediction, respectively.
Datasets: We evaluate RPRL on six datasets covering all
three tasks. For rumor detection, we use DRWeibo [13] and
Weibo [40]; for social-bot detection, we use Twibot-22 [41]
and MGTAB [42]; and for information diffusion prediction, we
use the Christianity [43] and Twitter [44] datasets. In the rumor
detection setting, following [13], [14], we represent node-level
textual content using Word2Vec embeddings. For social-bot
detection, we follow the setting of [45], sampling 10,000
nodes from Twibot-22 while preserving the original label
6

distribution. For information diffusion prediction, we adopt
the initialization strategy from [20], where node embeddings
are initialized using graph convolutional operations. To ensure
fair comparison, we follow the evaluation protocols used by
the baselines in each task [14], [35], [46], and split each dataset
into training, validation, and test sets using a 6:2:2 ratio for
rumor detection, 7:1:2 for social-bot detection, and 8:1:1 for
information diffusion prediction.
Baselines: We compare RPRL with 6 widely used and state-
of-the-art baselines for each of the three tasks, respectively.
• Rumor Detection: Our baselines include graph-based
rumor detection methods ResGCN [39], KAGIN [47],
GACL [48], GARD [49], RAGCL [13], EIN [14].
• Social-bot Detection: Our baselines include GAT,
BotRGCN [16], SHGN [50], RGT [35], BotMoE [17],
SEBot [18], which are state-of-the-art methods based on
graph neural networks.
• Information Diffusion Prediction: Our baselines include
both dynamic and hypergraph methods like FOREST
[51], DyHGCN [36], MSHGAT [20], RotDiff [21],
MINDS [22], GODEN [46].
Evaluation Metrics and Implementation Details: We adopt
standard evaluation metrics tailored to each task. For the rumor
detection task, we use Accuracy (Acc.), ROC-AUC (AUC),
and F1-score (F1). For social-bot detection, the evaluation
metrics include Accuracy (Acc.), Balanced Accuracy (B-Acc.),
and F1-score (F1). For the information diffusion prediction
task, we report Hit@K and Mean Average Precision at K
(MAP@K), where K ∈ {10, 100}.
We implement the proposed RPRL framework using Py-
Torch and conduct all experiments on an NVIDIA RTX 4090
GPU. Detailed parameter settings for RPRL across all tasks
are available in the released code repository. In addition, we
provide an analysis of the impact of the hyperparameters γ
and λ in Section V-E.
TABLE I: Overall comparison results for the graph-based
rumor detection task (%).
Dataset Model Acc. AUC F1
ResGCN 87.79 ±1.29 87.73 ±1.14 86.98 ±1.09
KAGIN 86.75 ±0.29 86.54 ±0.64 85.61 ±1.42
GACL 83.14 ±3.17 83.51 ±3.01 84.15 ±2.38
GARD 88.58 ±0.76 88.55 ±0.77 87.95 ±0.66
DRWeibo RAGCL 88.50 ±0.53 88.37 ±0.62 87.57 ±0.72
EIN 89.04 ±0.47 88.95 ±0.53 88.28 ±0.53
RPRL w/o pt 89.49 ±0.29 89.47±0.13 88.86±0.07
RAGCL-pt 88.83 ±0.53 88.63 ±0.54 87.77 ±0.59
EIN-pt 88.54 ±0.47 88.57 ±0.34 88.02 ±0.37
RPRL (ours) 89.53±0.59 89.61 ±0.49 89.18 ±0.59
ResGCN 93.89 ±1.67 93.92 ±1.63 93.82 ±1.85
KAGIN 92.44 ±0.68 92.46 ±0.70 92.28 ±0.86
GACL 94.37 ±0.83 94.39 ±0.82 94.36 ±0.90
GARD 94.43 ±0.45 94.41 ±0.43 94.56 ±0.56
Weibo RAGCL 93.94 ±0.68 93.95 ±0.69 93.87 ±0.82
EIN 95.39 ±0.61 95.38 ±0.59 95.45 ±0.69
RPRL w/o pt 95.57 ±0.15 95.71 ±0.15 95.75 ±0.12
RAGCL-pt 94.59 ±0.23 94.59 ±0.24 94.58 ±0.26
EIN-pt 95.66 ±0.38 95.66±0.38 95.70±0.32
RPRL (ours) 96.20±0.99 96.19 ±0.98 96.25 ±0.98
TABLE II: Overall comparison results for the social-bot de-
tection task (%).
Dataset Model Acc. B-Acc. F1
BotRGCN 86.93 ±0.37 69.46 ±0.14 50.12 ±0.22
GAT 87.20 ±0.21 67.30 ±0.24 47.30 ±0.60
SHGN 87.23 ±0.43 67.49 ±2.77 47.48 ±4.68
Twibot-22 RGT 87.32 ±0.33 69.13 ±2.17 49.99 ±2.65
BotMoE 87.10 ±0.23 48.14 ±5.83 49.58 ±0.40
RPRL w/o pt 86.87 ±0.48 71.44 ±0.28 52.57±0.24
BotRGCN-pt 86.97 ±0.14 66.32 ±3.88 45.14 ±6.17
RGT-pt 87.43±0.14 66.53±1.40 46.28 ±2.43
RPRL (ours) 87.42 ±0.07 72.61±0.36 54.64 ±0.32
BotRGCN 89.13 ±2.35 83.60 ±5.58 77.86 ±6.88
GAT 87.66 ±1.25 84.70 ±0.05 77.57 ±1.02
SHGN 87.66 ±3.74 86.46 ±2.31 78.88 ±5.09
RGT 89.88 ±0.94 86.29 ±2.09 80.69 ±2.45
MGTAB BotMoE 88.69 ±0.64 86.71 ±1.17 80.29 ±0.69
SEBot 89.41 ±1.86 86.95 ±0.99 80.64±2.28
RPRL w/o pt 90.21 ±1.25 86.17±2.24 81.59 ±2.89
BotRGCN-pt 89.72 ±0.28 86.46 ±0.36 80.77 ±0.67
RGT-pt 88.10 ±0.21 82.59 ±0.12 76.34 ±0.45
RPRL (ours) 90.45±1.04 87.35 ±2.39 82.07 ±2.71
TABLE III: Overall comparison results for the information
diffusion prediction task (%).
Dataset Model Hits@10 MAP@10 Hits@100 MAP@100
FOREST 23.88 ±1.90 16.26 ±0.47 56.80 ±2.37 17.33 ±0.42
DyHGCN 30.13 ±0.01 18.69 ±0.39 60.72 ±0.63 19.74 ±0.41
MSHGAT 30.47 ±1.74 17.24 ±0.86 61.05 ±0.79 18.34 ±0.72
RotDiff 30.92 ±0.16 19.14 ±0.70 63.72±0.47 20.33±0.81
Chris. MINDS 27.79 ±1.10 17.88 ±0.30 57.59 ±1.58 18.94 ±0.44
GODEN 30.25 ±2.57 19.88 ±0.75 58.93±2.68 20.84 ±0.69
RPRL w/o pt 32.03 ±0.16 18.66±0.19 62.16 ±0.16 19.76 ±0.15
RotDiff-pt 30.81 ±0.32 19.20 ±0.60 62.16 ±3.01 20.24 ±0.69
GODEN-pt 28.79 ±0.22 18.99 ±0.26 57.48 ±0.33 19.95 ±0.25
RPRL (ours) 33.70±1.27 20.30 ±0.13 62.95±0.63 21.32±0.06
FOREST 23.33 ±0.04 16.47 ±0.28 42.55 ±0.44 17.05 ±0.26
DyHGCN 33.79 ±0.03 22.80 ±0.15 57.28 ±0.16 23.61 ±0.16
MSHGAT 30.61 ±0.37 19.76 ±0.11 56.41 ±0.49 20.63 ±0.14
RotDiff 35.77 ±0.16 23.07 ±0.20 62.22 ±0.23 23.95 ±0.21
Twitter MINDS 28.67 ±1.44 15.89 ±1.13 53.50 ±1.22 16.73 ±1.13
GODEN 37.78 ±0.04 24.45±0.09 64.80±0.25 25.40±0.08
RPRL w/o pt 37.43 ±0.35 24.94 ±0.21 63.89±0.06 25.86±0.19
RotDiff-pt 34.92 ±0.48 22.56 ±0.70 62.10 ±0.59 23.49 ±0.69
GODEN-pt 34.31 ±0.44 21.22 ±0.48 62.65 ±1.77 22.19 ±0.43
RPRL (ours) 38.05±0.14 25.29 ±0.07 63.60±0.21 26.18±0.08
B. Overall Comparison
Setup: For all baseline models across all tasks, we adopt
end-to-end training. The proposed RPRL framework follows a
cross-dataset pre-training and fine-tuning setting. For instance,
in the rumor detection task, if Weibo is the target dataset,
RPRL is first pre-trained on the DRWeibo dataset, and then
fine-tuned and evaluated on Weibo. To ensure a fair compar-
ison, we apply the same cross-dataset pre-training strategy
to the top two best-performing baseline models, which are
denoted with the suffix “-pt”. We also compare the version
of RPRL without pre-training with other baselines, which is
denoted as RPRL w/o pt.
7

Result: We compare the proposed RPRL framework against
baseline models across all three tasks, with the results summa-
rized in Tables I to III. The best results are highlighted in bold,
and the second-best results are underlined. Based on these
results, we make the following observations: (1) Our method
achieves state-of-the-art performance across all three tasks.
Even without pre-training, the RPRL model outperforms most
baseline methods in the majority of cases. This demonstrates
that our approach not only supports cross-task generalization
under the same architecture, but also exhibits strong cross-
dataset transferability and robustness to data variations. (2) For
those baseline models that are also pre-trained across datasets,
their performance is unstable and sometimes even worse
than their non-pretrained counterparts (e.g., RAGCL and EIN
on DRWeibo). This phenomenon suggests that these models
have limited knowledge transfer capability and struggle to
generalize to unseen data distributions. In contrast, RPRL
consistently maintains high performance even under domain
shift, highlighting its superior adaptability and robustness.
C. Zero- and Few-shot Capability of RPRL
Setup: To further evaluate the cross-dataset generalization
and data efficiency of RPRL, we conduct zero- and few-shot
experiments across all three tasks. We adopt the cross-dataset
pre-train and fine-tune setting in Section V-B to pre-train all
the methods and fine-tune on the target dataset. For the few-
shot experiments, we randomly select 1% and 5% of the target
dataset for the one-shot and five-shot settings, respectively. In
the zero-shot setting, we directly evaluate performance on the
target dataset without any fine-tuning.
Result: As shown in Figure 3, RPRL demonstrates strong
cross-dataset generalization, consistently outperforming all
baseline methods in zero-shot settings in most cases. This
trend is especially evident in the rumor detection and social-
bot detection tasks, where RPRL achieves superior perfor-
mance without access to any labeled samples from the target
domain. Notably, in the rumor detection task, RPRL’s zero-
shot performance even surpasses the five-shot results of the
baseline models, underscoring its exceptional cross-domain
transferability.
As more supervision becomes available, RPRL continues to
show clear performance gains. In both one-shot and five-shot
scenarios, its advantages remain consistent across all tasks and
evaluation metrics: accuracy and F1-score for rumor detection,
balanced accuracy and F1-score for social-bot detection, and
MAP@10 and Hit@10 for information diffusion prediction.
These results highlight RPRL’s strong data efficiency and
adaptability in low-resource settings.
An exception arises in the information diffusion prediction
task (Christianity and Twitter datasets), where all methods,
including our RPRL, exhibit relatively poor performance in
the zero-shot setting. This outcome is expected, as the task
is framed as a retrieval-based link prediction problem that
involves selecting the next user to be activated from a large
candidate pool. Without any labeled data in the target domain,
models struggle to transfer the retrieval objective, making
zero-shot prediction particularly challenging. Nevertheless,
RPRL quickly outperforms all baselines once minimal su-
pervision (e.g., one-shot) is introduced, reaffirming its strong
adaptability even in complex task formulations.
D. Ablation Study
To investigate the contributions of different components in
RPRL, we conduct an ablation study across all three tasks,
as shown in Table IV. We compare the full model with
three variants: (1) RPRL w/o pt, which removes cross-dataset
pre-training; (2) RPRL w/o pe, which disables propagation-
aware embedding learning by removing the propagation-aware
encoder and kinetic-guided loss; and (3) RPRL-rg, which
replaces the Markov chain-based kinetic model with a simpler
regular kinetic model for computing the kinetic-guided loss.
The results demonstrate several key findings. Above all,
removing the propagation-aware embedding module (RPRL
w/o pe) leads to a consistent and notable performance drop
across all datasets and tasks. This highlights the importance
of modeling propagation dynamics via the propagation-aware
encoder and kinetic-guided supervision. Besides, the RPRL
w/o pt variant generally performs worse than the fully pre-
trained version, indicating that cross-dataset pre-training im-
proves generalization and boosts performance. The RPRL-rg
variant, which replaces the kinetic-guided loss function with
a regular kinetic model, also underperforms compared to the
full model, indicating the advantage of our modified Markov
chain-based kinetic formulation for guiding information prop-
agation modeling.
TABLE IV: Performance comparison of RPRL variants across
three tasks (%). Best results are in bold.
Task Dataset Model Acc. F1
RD
DRWeibo RPRL w/o pt 89.24 ±0.18 88.73 ±0.11
RPRL w/o pe 89.58±0.65 88.98±0.48
RPRL-rg 88.41 ±0.41 87.57 ±0.76
RPRL 89.53 ±0.47 89.18±0.59
Weibo RPRL w/o pt 95.55 ±0.83 95.62 ±0.87
RPRL w/o pe 94.86 ±1.36 94.90 ±1.46
RPRL-rg 95.39 ±1.36 95.45 ±1.65
RPRL 96.20±0.99 96.25 ±0.98
Task Dataset Model B-Acc. F1
SBD
TwiBot-22 RPRL w/o pt 71.44 ±0.28 52.57 ±0.24
RPRL w/o pe 68.85 ±1.14 49.97 ±1.65
RPRL-rg 70.52 ±0.92 51.36 ±1.34
RPRL 72.61±0.36 54.64 ±0.32
MGTAB RPRL w/o pt 86.17 ±2.24 81.09 ±2.96
RPRL w/o pe 86.93 ±2.64 81.59 ±2.89
RPRL-rg 86.18 ±2.25 80.92 ±2.72
RPRL 87.35±2.39 82.07 ±2.71
Task Dataset Model Hits@10 MAP@10
IDP
Christianity RPRL w/o pt 32.03 ±0.16 18.66 ±0.19
RPRL w/o pe 31.92 ±0.01 19.31 ±0.16
RPRL-rg 31.92 ±1.27 19.62 ±0.72
RPRL 33.70±1.27 20.30 ±0.13
Twitter RPRL w/o pt 37.43 ±0.35 24.94 ±0.21
RPRL w/o pe 37.74 ±0.12 24.62 ±0.54
RPRL-rg 37.28 ±0.11 24.90 ±0.16
RPRL 38.05±0.14 25.29 ±0.07
8

0 1 5
Shot
0.7
0.8
0.9Accuracy
RAGCL
EIN
RPRL
0 1 5
Shot
0.7
0.8
0.9F1-Score
RAGCL
EIN
RPRL
(a) DRWeibo
0 1 5
Shot
0.4
0.5
0.6
0.7Balance-acc
BotRGCN
RGT
RPRL
0 1 5
Shot
0.0
0.2
0.4F1-Score
BotRGCN
RGT
RPRL (b) Twibot-22
0 1 5
Shot
0.00
0.05
0.10
0.15Map@10
RotDiff
GODEN
RPRL
0 1 5
Shot
0.0
0.1
0.2Hit@10
RotDiff
GODEN
RPRL (c) Christianity
0 1 5
Shot
0.7
0.8
0.9Accuracy
RAGCL
EIN
RPRL
0 1 5
Shot
0.7
0.8
0.9F1-Score
RAGCL
EIN
RPRL
(d) Weibo
0 1 5
Shot
0.4
0.5
0.6
0.7
0.8Balance-acc
BotRGCN
RGT
RPRL
0 1 5
Shot
0.0
0.2
0.4
0.6F1-Score
BotRGCN
RGT
RPRL (e) MGTAB
0 1 5
Shot
0.00
0.05
0.10Map@10
RotDiff
GODEN
RPRL
0 1 5
Shot
0.00
0.05
0.10
0.15Hit@10
RotDiff
GODEN
RPRL (f) Twitter
Fig. 3: Performance of RPRL and baselines across three tasks under different zero- and few-shot settings.
E. Hyperparameter Analysis
To analyze the sensitivity of our model to key hyper-
parameters, we conduct experiments on three representative
datasets from each task: DRWeibo (rumor detection), MGTAB
(social bot detection), and Christianity (information diffusion
prediction). We analyze the influences of two hyperparameters:
γ, which controls the contribution of graph encoder, and λ,
which controls the contribution of the kinetic-guided loss in
the overall optimization process.
0.1 0.3 0.5 0.7 0.9
0.860
0.865
0.870
0.875
0.880
0.885
0.890Accuracy
(a) γ on DRWeibo.
0.1 0.3 0.5 0.7 0.9
0.866
0.868
0.870
0.872B-Acc
 (b) γ on MGTAB.
0.1 0.3 0.5 0.7 0.9
0.24
0.26
0.28
0.30
0.32
0.34Hit@10
 (c) γ on Christianity.
0.1 0.3 0.5 0.7 0.9
0.870
0.875
0.880
0.885
0.890Accuracy
(d) λ on DRWeibo.
0.0010.01 0.1 0.5 1.0
0.8724
0.8726
0.8728
0.8730
0.8732
0.8734B-Acc
 (e) λ on MGTAB.
0.0010.01 0.1 0.5 1.0
0.3175
0.3200
0.3225
0.3250
0.3275
0.3300
0.3325
0.3350
0.3375Hit@10
 (f) λ on Christianity.
Fig. 4: Hyperparameter sensitivity analysis: The influences of
γ and λ on DRweibo, MGTAB and Christianity datasets.
In Figure 4, the results show that the impact of γ varies no-
tably across tasks, reflecting their different levels of reliance on
structural information. In DRWeibo (rumor detection), model
performance peaks around γ = 0.5 and declines beyond that,
suggesting that while graph learning helps, overemphasizing
it may suppress the structure-agnostic patterns critical for
classifying the root post. In MGTAB (social bot detection), the
model benefits from relatively higher values of γ (up to 0.7),
which aligns with the nature of node classification within large
social networks, where local graph structural context is more
informative. In contrast, on Christianity (information diffu-
sion prediction), increasing γ leads to consistent performance
degradation, indicating that graph learning plays a limited
role in retrieval-based link prediction, where structure-agnostic
patterns in cascade sequences are more dominant.
In addition, we observe that λ on DRWeibo and MGTAB,
where performance peaks around λ = 0 .5 and drops there-
after. This confirms that over-weighting the kinetic-guided
loss interferes with task-specific objectives, and highlights
the importance of balancing domain knowledge with data-
driven learning. Moreover, in the Christianity dataset, perfor-
mance improves steadily with increasing λ, suggesting that the
kinetic-guided loss is more beneficial in link prediction, where
learning structured dynamics is particularly challenging.
VI. C ONCLUSION
In this paper, we proposed a robust propagation-aware
representation learning (RPRL) framework that incorporates
domain knowledge through kinetic modeling to enhance data-
driven representations. The proposed method adopts a gen-
eral architecture capable of addressing graph classification,
node classification, and link prediction. Extensive experiments
demonstrate that RPRL achieves state-of-the-art performance
across all three tasks. Moreover, the model exhibits strong
cross-dataset generalization, significantly outperforming exist-
ing baselines in zero-shot and few-shot transfer settings. These
results highlight the effectiveness and robustness of our ap-
proach, and point toward a promising direction for developing
foundation models for social media graph analytics.
ACKNOWLEDGMENT
The Australian Research Council partially supports
this work under the streams of Future Fellowship (No.
FT210100624), Discovery Early Career Researcher Award
(No. DE230101033), Discovery Project (No. DP240101108
and No. DP240101814), and Linkage Project (Grant No.
LP230200892 and LP240200546).
9

REFERENCES
[1] H. Kwak, C. Lee, H. Park, and S. Moon, “What is twitter, a social
network or a news media?” in Proceedings of the 19th international
conference on World wide web , 2010, pp. 591–600.
[2] S. Chen, H. Zhang, M. Lin, and S. Lv, “Comparision of microblogging
service between sina weibo and twitter,” in Proceedings of 2011 In-
ternational Conference on Computer Science and Network Technology ,
vol. 4. IEEE, 2011, pp. 2259–2263.
[3] W. Jiang, X. Gao, G. Xu, T. Chen, and H. Yin, “Challenging low
homophily in social recommendation,” in Proceedings of the ACM Web
Conference 2024, 2024, pp. 3476–3484.
[4] H. Yin, Q. Wang, K. Zheng, Z. Li, J. Yang, and X. Zhou, “Social
influence-based group representation learning for group recommenda-
tion,” in 2019 IEEE 35th International Conference on Data Engineering
(ICDE). IEEE, 2019, pp. 566–577.
[5] N. Q. V . Hung, H. H. Viet, N. T. Tam, M. Weidlich, H. Yin, and
X. Zhou, “Computing crowd consensus with partial agreement,” IEEE
Transactions on Knowledge and Data Engineering , vol. 30, no. 1, pp.
1–14, 2017.
[6] X. Sun, H. Cheng, B. Liu, J. Li, H. Chen, G. Xu, and H. Yin, “Self-
supervised hypergraph representation learning for sociological analysis,”
IEEE Transactions on Knowledge and Data Engineering, vol. 35, no. 11,
pp. 11 860–11 871, 2023.
[7] T. Chen, D. Wang, X. Liang, M. Risius, G. Demartini, and H. Yin,
“Hate speech detection with generalizable target-aware fairness,” in
Proceedings of the 30th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining , 2024, pp. 365–375.
[8] J. Liu, M. He, X. Shang, J. Shi, B. Cui, and H. Yin, “Bourne: Boot-
strapped self-supervised learning framework for unified graph anomaly
detection,” in 2024 IEEE 40th International Conference on Data Engi-
neering (ICDE). IEEE, 2024, pp. 2820–2833.
[9] X. Gao, W. Zhang, J. Yu, Y . Shao, Q. V . H. Nguyen, B. Cui, and
H. Yin, “Accelerating scalable graph neural network inference with
node-adaptive propagation,” in2024 IEEE 40th International Conference
on Data Engineering (ICDE) . IEEE, 2024, pp. 3042–3055.
[10] A. Bondielli and F. Marcelloni, “A survey on fake news and rumour
detection techniques,” Information sciences, vol. 497, pp. 38–55, 2019.
[11] S. Cresci, “A decade of social bot detection,” Communications of the
ACM, vol. 63, no. 10, pp. 72–83, 2020.
[12] M. Li, X. Wang, K. Gao, and S. Zhang, “A survey on information
diffusion in online social networks: Models and methods,” Information,
vol. 8, no. 4, p. 118, 2017.
[13] C. Cui and C. Jia, “Propagation tree is not deep: Adaptive graph
contrastive learning approach for rumor detection,” in Proceedings of
the AAAI Conference on Artificial Intelligence , vol. 38, no. 1, 2024, pp.
73–81.
[14] W. Jiang, T. Chen, X. Gao, W. Zhang, L. Cui, and H. Yin,
“Epidemiology-informed network for robust rumor detection,” in Pro-
ceedings of the ACM on Web Conference 2025 , 2025, pp. 3618–3627.
[15] X. Sun, H. Yin, B. Liu, H. Chen, J. Cao, Y . Shao, and N. Q. Viet Hung,
“Heterogeneous hypergraph embedding for graph classification,” in
Proceedings of the 14th ACM international conference on web search
and data mining , 2021, pp. 725–733.
[16] S. Feng, H. Wan, N. Wang, and M. Luo, “Botrgcn: Twitter bot de-
tection with relational graph convolutional networks,” in Proceedings
of the 2021 IEEE/ACM international conference on advances in social
networks analysis and mining , 2021, pp. 236–239.
[17] Y . Liu, Z. Tan, H. Wang, S. Feng, Q. Zheng, and M. Luo, “Botmoe:
Twitter bot detection with community-aware mixtures of modal-specific
experts,” in Proceedings of the 46th International ACM SIGIR Confer-
ence on Research and Development in Information Retrieval , 2023, pp.
485–495.
[18] Y . Yang, Q. Wu, B. He, H. Peng, R. Yang, Z. Hao, and Y . Liao, “Sebot:
Structural entropy guided multi-view contrastive learning for social bot
detection,” in Proceedings of the 30th ACM SIGKDD Conference on
Knowledge Discovery and Data Mining , 2024, pp. 3841–3852.
[19] J. Liu, M. He, G. Wang, N. Q. V . Hung, X. Shang, and H. Yin,
“Imbalanced node classification beyond homophilic assumption,” arXiv
preprint arXiv:2304.14635, 2023.
[20] L. Sun, Y . Rao, X. Zhang, Y . Lan, and S. Yu, “Ms-hgat: memory-
enhanced sequential hypergraph attention network for information dif-
fusion prediction,” in Proceedings of the AAAI Conference on Artificial
Intelligence, vol. 36, no. 4, 2022, pp. 4156–4164.
[21] H. Qiao, S. Feng, X. Li, H. Lin, H. Hu, W. Wei, and Y . Ye, “Rotdiff:
A hyperbolic rotation representation model for information diffusion
prediction,” in Proceedings of the 32nd ACM International Conference
on Information and Knowledge Management , 2023, pp. 2065–2074.
[22] P. Jiao, H. Chen, Q. Bao, W. Zhang, and H. Wu, “Enhancing multi-scale
diffusion prediction via sequential hypergraphs and adversarial learning,”
in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 38,
no. 8, 2024, pp. 8571–8581.
[23] T. Zimmerman, “Social noise: the influence of observers on social media
information behavior,” Journal of Documentation , vol. 78, no. 6, pp.
1228–1248, 2022.
[24] S. L. Buglass, J. F. Binder, L. R. Betts, and J. D. Underwood, “When
‘friends’ collide: Social heterogeneity and user vulnerability on social
network sites,” Computers in Human Behavior, vol. 54, pp. 62–72, 2016.
[25] R. Levinson-Waldman, “Government access to and manipulation of
social media: Legal and policy challenges,” Howard LJ, vol. 61, p. 523,
2017.
[26] A. Kavanaugh, E. A. Fox, S. Sheetz, S. Yang, L. T. Li, T. Whalen,
D. Shoemaker, P. Natsev, and L. Xie, “Social media use by government:
From the routine to the critical,” in Proceedings of the 12th annual in-
ternational digital government research conference: digital government
innovation in challenging times , 2011, pp. 121–130.
[27] P. Chauhan, N. Sharma, and G. Sikka, “The emergence of social media
data and sentiment analysis in election prediction,” Journal of Ambient
Intelligence and Humanized Computing , vol. 12, pp. 2601–2627, 2021.
[28] J. Bukovina, “Social media big data and capital markets—an overview,”
Journal of Behavioral and Experimental Finance , vol. 11, pp. 18–26,
2016.
[29] W. Jiang, T. Chen, G. Ye, W. Zhang, L. Cui, Z. Huang, and H. Yin,
“Physics-guided active sample reweighting for urban flow prediction,”
arXiv preprint arXiv:2407.13605 , 2024.
[30] K. H. Hettige, J. Ji, S. Xiang, C. Long, G. Cong, and J. Wang,
“Airphynet: Harnessing physics-guided neural networks for air quality
prediction,” arXiv preprint arXiv:2402.03784 , 2024.
[31] P. Van Mieghem, J. Omic, and R. Kooij, “Virus spread in networks,”
IEEE/ACM Transactions On Networking, vol. 17, no. 1, pp. 1–14, 2008.
[32] Z.-K. Zhang, C. Liu, X.-X. Zhan, X. Lu, C.-X. Zhang, and Y .-C. Zhang,
“Dynamics of information diffusion and its applications on complex
networks,” Physics Reports, vol. 651, pp. 1–34, 2016.
[33] M. Youssef and C. Scoglio, “An individual-based approach to sir
epidemics in contact networks,” Journal of theoretical biology, vol. 283,
no. 1, pp. 136–144, 2011.
[34] T. Bian, X. Xiao, T. Xu, P. Zhao, W. Huang, Y . Rong, and J. Huang,
“Rumor detection on social media with bi-directional graph convolu-
tional networks,” in Proceedings of the AAAI conference on artificial
intelligence, vol. 34, no. 01, 2020, pp. 549–556.
[35] S. Feng, Z. Tan, R. Li, and M. Luo, “Heterogeneity-aware twitter bot
detection with relational graph transformers,” inProceedings of the AAAI
Conference on Artificial Intelligence , vol. 36, no. 4, 2022, pp. 3977–
3985.
[36] C. Yuan, J. Li, W. Zhou, Y . Lu, X. Zhang, and S. Hu, “Dyhgcn: A
dynamic heterogeneous graph convolutional network to learn users’
dynamic preferences for information diffusion prediction,” in Machine
Learning and Knowledge Discovery in Databases: European Confer-
ence, ECML PKDD 2020, Ghent, Belgium, September 14–18, 2020,
Proceedings, Part III. Springer, 2021, pp. 347–363.
[37] N. Hajli, U. Saeed, M. Tajvidi, and F. Shirazi, “Social bots and the
spread of disinformation in social media: the challenges of artificial
intelligence,” British Journal of Management , vol. 33, no. 3, pp. 1238–
1253, 2022.
[38] M. Himelein-Wachowiak, S. Giorgi, A. Devoto, M. Rahman, L. Ungar,
H. A. Schwartz, D. H. Epstein, L. Leggio, and B. Curtis, “Bots and
misinformation spread on social media: implications for covid-19,”
Journal of medical Internet research , vol. 23, no. 5, p. e26933, 2021.
[39] Y . You, T. Chen, Y . Sui, T. Chen, Z. Wang, and Y . Shen, “Graph con-
trastive learning with augmentations,” Advances in neural information
processing systems, vol. 33, pp. 5812–5823, 2020.
[40] J. Ma, W. Gao, P. Mitra, S. Kwon, B. J. Jansen, K.-F. Wong, and M. Cha,
“Detecting rumors from microblogs with recurrent neural networks,”
2016.
[41] S. Feng, Z. Tan, H. Wan, N. Wang, Z. Chen, B. Zhang, Q. Zheng,
W. Zhang, Z. Lei, S. Yang et al. , “Twibot-22: Towards graph-based
twitter bot detection,” Advances in Neural Information Processing
Systems, vol. 35, pp. 35 254–35 269, 2022.
10

[42] S. Shi, K. Qiao, J. Chen, S. Yang, J. Yang, B. Song, L. Wang, and
B. Yan, “Mgtab: A multi-relational graph-based twitter account detection
benchmark,” arXiv preprint arXiv:2301.01123 , 2023.
[43] A. Sankar, X. Zhang, A. Krishnan, and J. Han, “Inf-vae: A variational
autoencoder framework to integrate homophily and influence in diffusion
prediction,” in Proceedings of the 13th international conference on web
search and data mining , 2020, pp. 510–518.
[44] N. O. Hodas and K. Lerman, “The simple rules of social contagion,”
Scientific reports, vol. 4, no. 1, p. 4343, 2014.
[45] M. Zhou, D. Zhang, Y . Wang, Y .-A. Geng, and J. Tang, “Detecting
social bot on the fly using contrastive learning,” in Proceedings of the
32nd ACM International Conference on Information and Knowledge
Management, 2023, pp. 4995–5001.
[46] D. Wang, W. Zhou, and S. Hu, “Information diffusion prediction with
graph neural ordinary differential equation network,” in Proceedings of
the 32nd ACM International Conference on Multimedia, 2024, pp. 9699–
9708.
[47] R. Bresson, G. Nikolentzos, G. Panagopoulos, M. Chatzianastasis,
J. Pang, and M. Vazirgiannis, “Kagnns: Kolmogorov-arnold networks
meet graph learning,” arXiv preprint arXiv:2406.18380 , 2024.
[48] T. Sun, Z. Qian, S. Dong, P. Li, and Q. Zhu, “Rumor detection on social
media with graph adversarial contrastive learning,” in Proceedings of the
ACM Web Conference 2022 , 2022, pp. 2789–2797.
[49] X. Tao, L. Wang, Q. Liu, S. Wu, and L. Wang, “Semantic evolvement
enhanced graph autoencoder for rumor detection,” in Proceedings of the
ACM on Web Conference 2024 , 2024, pp. 4150–4159.
[50] Q. Lv, M. Ding, Q. Liu, Y . Chen, W. Feng, S. He, C. Zhou, J. Jiang,
Y . Dong, and J. Tang, “Are we really making much progress? revisiting,
benchmarking and refining heterogeneous graph neural networks,” in
Proceedings of the 27th ACM SIGKDD conference on knowledge
discovery & data mining , 2021, pp. 1150–1160.
[51] C. Yang, H. Wang, J. Tang, C. Shi, M. Sun, G. Cui, and Z. Liu,
“Full-scale information diffusion prediction with reinforced recurrent
networks,” IEEE Transactions on Neural Networks and Learning Sys-
tems, vol. 34, no. 5, pp. 2271–2283, 2021.
11
