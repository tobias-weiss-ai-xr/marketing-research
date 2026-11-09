---
title: Multi-Agent Agentic Graph Learning via Structural Signatures
url: https://arxiv.org/abs/2609.09565
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Liang Qu
- Jianxin Li
- Hua Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.09565
pages: 13
chars: 69914
fetched_at: '2026-11-08T13:35:20+00:00'
kb_version: 1
---

# Multi-Agent Agentic Graph Learning via Structural Signatures

1
Multi-Agent Agentic Graph Learning via
Structural Signatures
Liang Qu 1 Member, IEEE, Jianxin Li 1∗ Senior Member, IEEE, Hua Wang 2 Fellow, IEEE
Abstract—Agentic graph learning (AGL) has recently achieved
promising results on graph reasoning tasks, where an agent
powered by a large language model (LLM) sequentially samples
the graph as evidence to support its final prediction. Existing
methods either employ a single agent or orchestrate multiple
role-based agents to reason and learn over the entire graph,
but both essentially rely on a shared reasoning policy across
different graph regions, which can be suboptimal for graphs
with heterogeneous structural and semantic patterns. Inspired by
the progress of multi-agent collaboration on complex reasoning
tasks, a natural remedy is to let multiple agents own different
memory and collaborate; however, applying this paradigm to
graphs directly faces two challenges. First, existing AGL meth-
ods typically verbalize graph structures into natural-language
descriptions for LLM agents, making the reasoning process
sensitive to the ordering of structural information and thereby
breaking the permutation-invariant nature of graphs. Second,
incorporating increasingly large sampled neighborhoods leads
to rapidly growing contexts, which not only increases inference
cost but also makes important structural evidence vulnerable
to the lost-in-the-middle problem. To address these challenges,
this paper introduces a multi-agent agentic graph learning (i.e.,
MAAGL) framework. MAAGL partitions the graph into com-
munities and assigns an independent agent to each community
for region-specific specialization. Unlike existing methods that
verbalize all sampled evidence into text, MAAGL represents
structural and semantic evidence separately. Structural evidence
is summarized by a dynamically updatedstructural signature
that is permutation-invariant and fixed in size, while semantic
evidence is filtered to the top-knodes ranked by relevance.
Based on historical trajectories with similar signatures, agents
estimate their confidence and trigger debate-style collaboration
when needed. MAAGL further learns reusable experience from
historical trajectories to guide subsequent reasoning. Extensive
experiments on four benchmark datasets show that MAAGL
outperforms state-of-the-art AGL methods under both in-domain
and zero-shot transfer settings while reducing token overhead.
Index Terms—Graph learning, Large Language Models, AI
Agents
I. INTRODUCTION
Text-attributed graphs (TAGs) are widely used to model
relational data in many real-world applications [1]–[3]. A TAG
consists of structural information and semantic information.
The structural information is represented by nodes and edges,
where nodes denote entities and edges describe the relations
between them. The semantic information is the text attached
to each node. For example, in social networks [4], nodes
represent users and edges represent their social connections,
1Edith Cowan University, Perth, Australia. Liang Qu:
leoqu94@outlook.com.
2The University of Queensland, Brisbane, Australia.
∗Corresponding author: Jianxin Li (jianxin.li@ecu.edu.au).
while user profiles provide the text of the nodes. In citation
networks [5], nodes represent papers and edges represent
citation relations between papers, while titles, abstracts, and
keywords provide the text of the papers. As a result, the core
objective of learning on TAGs is to learn from the structural
information and the semantic information jointly.
The traditional method to learn from both kinds of informa-
tion is graph neural networks (GNNs) [6]. A GNN starts from
the semantic information of each node, encoded as a feature
vector, and passes it along the edges. At each layer, a node
aggregates the representations of its neighbors and updates
its own. Thus, after several layers, a node representation
carries the semantics of its multi-hop neighborhood. Early
models such as GCN [7], GraphSAGE [8], and GAT [9]
mainly differ in how the neighbors are selected and how
their information are aggregated. Recently, graph transformers
such as Graphormer [10] and GraphGPS [11] are proposed to
add attention over the whole graph for capturing long-range
dependencies. Despite their success, these methods share a
fundamental limitation, i.e., the same neighborhood selection
and aggregation rule is applied uniformly across all nodes. But,
in fact, different nodes may require different neighborhood
contexts for downstream tasks.
Recently, agentic graph learning (AGL) [14] has emerged
as a new paradigm that leverages the planning and reasoning
capabilities of LLMs together with graph-specific tools to
adaptively identify and collect relevant structural and semantic
evidence for downstream graph tasks. Existing AGL methods
can be roughly divided into two categories. Single-agent
methods [3], [15] employ a single LLM agent to iteratively
retrieve graph evidence and reason toward the final prediction.
Orchestration-based methods [2], [16] instead decompose this
reasoning process across multiple role-specific agents and
coordinate them through a predefined workflow, with different
agents responsible for different stages of graph reasoning. De-
spite this architectural difference, both paradigms essentially
rely on a shared reasoning policy over the entire graph. How-
ever, as the graph becomes larger and more heterogeneous,
mixing diverse structural and semantic patterns into a shared
policy can be suboptimal.
To address the above issue, a natural solution is to in-
troduce multi-agent collaborative reasoning (e.g., multi-agent
debate [17]), which has shown strong effectiveness on com-
plex reasoning tasks by leveraging diverse perspectives from
agents with independent memories and reasoning experiences
[17], [18]. However, directly applying such methods to graph
reasoning tasks is non-trivial and faces two key challenges.
(1) Existing multi-agent collaboration is mainly developed
arXiv:2609.09565v2  [cs.AI]  19 Oct 2026

2
Which arXiv category does this paper belong to?
Title: Self-Supervised Contrastive ...
Abstract: Annotated medical images are ...
?
Agent Action: retrieve 1-hop neighbors
[1] Node P1, label cs.LG
Title: Momentum Contrast...
Abstract: We propose Momentum...
[2] Node P2, label cs.CV
Title: U-Net for Medical Image...
Abstract: U-Net is a widely used model...
[3] Node P3, label cs.CL
Title: A Simple Framework for...
Abstract: We present a simple framework...
....
The 1-hop neighbors information is: The 1-hop neighbors information is:
Degree = 3
Neighbor-label entropy = 0.92
Cross-community ratio = 0.33
Structural evidence:
Semantic evidence: (top-k)
1. P1 Title: Momentum Contrast...
2. P3 Title: A Simple Framework...
(a) Verbalized evidence (b) Structured evidence
ReAct MAAGL
(c) Effect of neighbor order
0
10
20
30
40
50
Answer changed (%)
41%
5%
1-hop 2-hop
(d) Token cost
1k
10k
100k
1M
Prompt tokens / query
3.2k
1.3k
541k
1.4k
0.40
0.45
0.50
0.55
Accuracy per ordering
11 pts
2 pts
ReAct (verbalized graph structure) MAAGL (structural signature)
Fig. 1. (a) Agents reasoning with verbalized graph evidence. (b) Agents reasoning with the proposed structural evidence. (c) Neighbor-order sensitivity of a
ReAct-based agent [12] on OGB-Arxiv [13] across five independent runs, where the retrieved neighbors are presented in different random orders. (d) Prompt
tokens per query on the same nodes.
for language-based reasoning tasks, where both the problem
context and reasoning process are naturally expressed in text,
making textual exchange between agents straightforward. In
graph reasoning, however, part of the evidence lies in the
graph structure, which must first be verbalized into a textual
sequence for agent communication, as illustrated in Figure 1
(a). This verbalization imposes an arbitrary order on inherently
unordered graph neighborhoods, breaking permutation invari-
ance and making the reasoning sensitive to neighbor ordering.
As evidenced by our preliminary results in Figure 1 (c),
different orderings of the same neighbors can lead to different
predictions. (2) Verbalizing graph structures also causes the
context to grow rapidly as the neighborhood expands. In TAGs,
each retrieved node brings not only structural information but
also its associated textual attributes, all of which need to
be included in the textual context. Due to the combinatorial
expansion of multi-hop neighborhoods, the resulting context
can therefore grow rapidly with each additional hop, leading
to substantial token costs, as evidenced by our preliminary
results in Figure 1(d).
In light of the above challenges, this work proposes a multi-
agent agentic graph learning MAAGL framework. Specifi-
cally, to enable agent specialization, MAAGL first partitions
the graph into communities and assigns one independent agent
to each community. Each agent then performs independent rea-
soning within its assigned community to build region-specific
reasoning experience. Unlike existing methods that verbalize
all sampled graph evidence into text, MAAGL represents the
evidence returned by each reasoning action in two parts: struc-
tural evidence and semantic evidence. For structural evidence,
we summarize the observed neighborhood using astructural
signaturecomposed of a small set of graph statistics (e.g.,
node degree and neighborhood label entropy). The signature
is dynamically updated over the sampled node set as new
evidence is collected, while remaining permutation-invariant
and fixed in size. For semantic evidence, MAAGL retains
the textual attributes of only the top-kretrieved nodes ranked
by their semantic relevance to the target node. In this way,
MAAGL preserves useful structural and semantic evidence
while avoiding arbitrary neighbor ordering and excessive token
costs. During subsequent reasoning, each agent estimates its
confidence using the success rate of past trajectories with simi-
lar structural signatures. If the confidence is below a threshold,
the same score is computed for the other agents, and the top-
Kagents are selected for debate-style collaborative reasoning.
Finally, MAAGL learns from historical reasoning trajectories
and stores the learned experiences in agent memory to guide
subsequent reasoning. The contributions of this work can be
summarized as follows:
•We identify a fundamental mismatch in applying existing
multi-agent collaborative reasoning to graph reasoning
tasks. Directly verbalizing sampled graph evidence for
agent reasoning can break permutation invariance and
incur high token costs.
•We propose MAAGL, a multi-agent agentic graph learn-
ing framework. MAAGL separates sampled graph ev-
idence into structural and semantic information, repre-
senting the former with a dynamically updatedstructural
signatureand filtering the latter by semantic relevance.
•We conduct extensive experiments on four benchmark
datasets, where MAAGL outperforms AGL methods un-
der both in-domain and zero-shot transfer settings while
reducing token overhead.
The rest of this paper is organized as follows. Section
2 reviews related work. We formally define the problem
of MAAGL in Section 3 and present its framework with
technical details in Section 4. Section 5 demonstrates the
experimental evaluation and Section 6 concludes the paper.
II. RELATEDWORK
A. GNN-based Graph Learning
Graph neural networks (GNNs) [6] are the dominant ap-
proach for learning from both structural and semantic informa-
tion on graphs. A GNN starts from the semantic information
of each node, encoded as a feature vector, and propagates
it along graph edges through message passing, so that each
node gradually aggregates information from its local structure.
Different GNN architectures mainly differ in how neighbors
are selected and how their information is aggregated. GCN [7]

3
performs normalized neighborhood aggregation, GraphSAGE
[8] samples neighbors and applies a learnable aggregator, GAT
[9] assigns attention weights to different neighbors, and JK-
Net [19] combines representations from multiple layers to
capture neighborhoods at different ranges. Later work extends
message passing to heterogeneous graphs with different node
and edge types [20], [21], while graph transformers [11], [22]
introduce global attention to capture long-range dependencies.
Another line of work improves their training with graph
augmentation. DropEdge [23] randomly removes edges during
training, which reduces over-fitting and over-smoothing in
deep GNNs. GraphCL [24] perturbs the graph into several
contrastive views and learns representations that agree across
the views. NodeAug [25] and local augmentation [26] enrich
the surroundings of each node, the former by changing its
nearby attributes and edges under consistency training, the
latter by generating extra neighbor features conditioned on the
node.
However, GNN-based graph learning methods generally rely
on neighborhood selection and aggregation rules determined
by the model architecture and applied uniformly across nodes,
which can be suboptimal when different nodes require differ-
ent graph contexts for downstream tasks.
B. Agent-based Graph Learning
Large language model (LLM)-powered agents have recently
emerged as a promising paradigm for solving complex tasks
by integrating planning, reasoning, and tool use within an
autonomous loop [12], [27]. This paradigm has also been
extended to graph learning, giving rise to agentic graph
learning (AGL) [14]. Existing AGL methods mainly follow
two lines. Single-agent methods use one LLM agent to interact
with the graph and iteratively collect evidence for reasoning.
ReaGAN [15] equips an agent with graph sampling tools for
retrieving structural and semantic evidence such as neighbor
labels, while Graph-CoT [28] lets an agent iteratively invoke
graph functions and reason over the returned information.
AgentGL [3] further organizes graph reasoning into a thought-
action-observation loop [12] and optimizes the reasoning
policy from collected trajectories, and GraphReAct [29] per-
forms multi-step reasoning and acting for graph inference.
Orchestration-based methods instead coordinate multiple role-
specific agents through a predefined workflow. GraphAgent [2]
assigns different agents to planning, graph retrieval, and pre-
diction, GraphTeam [30] coordinates role-specialized agents
to collaboratively solve graph analysis tasks, GraphCogent
[16] decomposes complex graph understanding across multiple
collaborating agents, while GraphMaster [31] adopts a similar
division of labor for graph data synthesis.
Despite their architectural differences, both single-agent
and orchestration-based methods essentially rely on a shared
reasoning policy over the entire graph. Although the policy can
adaptively collect evidence for individual instances, different
graph regions may exhibit distinct structural and semantic pat-
terns. As the graph becomes larger and more heterogeneous,
mixing these diverse patterns into a shared policy can therefore
be suboptimal.
C. Multi-agent Collaborative Reasoning
Multi-agent collaborative reasoning has shown promising
performance on complex reasoning tasks by combining diverse
perspectives from agents with independent memories and
reasoning experiences [17], [18]. Existing methods mainly
differ in how agents collaborate. Debate-style methods [17]
involve multiple agents in the same task and iteratively refine
their decisions by exchanging reasoning results: each agent
reads the answers and rationales of the others, revises its
own over several rounds, and the final decision is reached
by consensus or voting. Routing-based methods select only a
subset of agents according to their expertise for each task;
AgentRouter [32] embeds the incoming task and retrieves
the agents whose recorded expertise is semantically closest,
and follow-up work studies how to select the best set of
collaborators under a cost budget [33]. Other methods enable
agents to share past experience through a common memory
without direct interaction [34]. An agent writes what it has
learned into a shared pool, from which other agents retrieve
when they meet similar tasks. These methods are mainly
developed for language-based reasoning tasks, where both
the task information and reasoning process can be naturally
represented and exchanged in text.
Directly applying such collaboration to graph reasoning,
however, is non-trivial. Graph reasoning additionally relies
on structural evidence, which must be verbalized into text
before it can be exchanged between agents. This verbalization
imposes an arbitrary order on inherently unordered graph
neighborhoods, breaking permutation invariance and making
the reasoning sensitive to neighbor ordering. Moreover, as
multi-hop neighborhoods expand, verbalizing the sampled
nodes together with their textual attributes can quickly increase
the context length, leading to high token costs.
III. PROBLEMFORMULATION
Text-attributed Graph (TAG):We define a TAG [2], [3]
asG= (V, E,X,Y), whereVdenotes the set of nodes and
E⊆V×Vdenotes the set of edges. Each nodev∈Vis
associated with a textual attribute (e.g., the title and abstract of
a paper node in academic citation graphs)x v ∈ X, whereX
denotes the textual attribute space. A subset of nodesV L ⊆V
is labeled, and each labeled nodev∈V L is associated with a
class labely v ∈ Y, whereYdenotes the label space.
Multi-Agent Agentic Graph Learning:Given a TAGG
and a target nodev, multi-agent agentic graph learning em-
ploys a set ofMLLM-powered agentsA={A 1, . . . , AM },
where each agentA i maintains its own reasoning policyπ i and
private memoryM i. We formulate the reasoning of each agent
as a sequential decision process. At stept, agentA i observes
the evidence collected so far, denoted bys t v, and selects an
actiona t v =π i(st v,M i)fromA evi ∪ {apred}, whereA evi is
a set of evidence-collection actions that sample structural and
semantic evidence fromG, anda pred terminates the process
with a predictionˆy v. Agents may further collaborate on the
same target node, and every reasoning process is recorded
as a trajectory in the memory of the corresponding agent.
Given the labeled node setV L, the goal is to enrich the

4
(a) Agent Assignment
Policy
Action
Memory
Policy
Action
Memory
Policy
Action
Memory
(b) Agent Specification
Structural evidence
Semantic evidence
Degree CC ...
Global Top- 𝑘  Semantic
Neighborhood Search
Local 𝑟  -hop Structural
Neighborhood Search
Observation Action
y
Predicted Label
conf(y)
Confidence
Prediction
Degree y
Reasoning trajectory
Insights
[degree > 3, 1-hop neighbor]
Memory
Reasoning, y Reasoning, y
Reasoning, y Reasoning, y
Exchange reasoning trajectory
Round 1
Round 2
(c) Collaborative reasoning Trigger: conf(y) < δ
Collaborator
routing
(d) Experience learning
Reasoning trajectory
from agents
Insights update
Experience
learning
Fig. 2. The overall architecture of MAAGL.
agent memories{M i}M i=1 by reasoning onV L, such that the
agents, individually or collaboratively, correctly predict the
labels of unlabeled nodes without updating any parameter of
the underlying LLM.
IV. THEMAAGLFRAMEWORK
As shown in Figure 2, MAAGL consists of four stages:
(a) Agent Assignment (Section IV-A), where the graph is
partitioned and one agent is assigned to each region; (b) Agent
Specialization (Section IV-B), where each agent independently
builds region-specific reasoning experience; (c) Collaborative
Reasoning (Section IV-C), where low-confidence cases trig-
ger collaboration among selected agents; and (d) Experience
Learning (Section IV-D), where historical trajectories are used
to learn reusable reasoning experience.
A. Agent Assignment
Existing AGL methods, including single-agent methods [3],
[15] and orchestration-based methods [2], [16], typically use a
shared reasoning policy and memory across the entire graph.
As a result, reasoning experience collected from different
graph regions is mixed together, even though these regions
may exhibit different structural and semantic patterns. To
enable agent specialization, we instead maintain multiple
independent agents, each with its own policy and memory,
and assign each agent to a specific graph region.
A straightforward approach is to randomly split the nodes
among agents. However, such a split ignores graph connec-
tivity and may place closely connected nodes into different
regions. We therefore use community detection to group
densely connected nodes and assign each community to one
agent. Formally,
{c1, c2, . . . , cM }= Partition(G),(1)
wherePartition(·)partitions the node set intoMdisjoint
communities, and agentA i is assigned to communityc i. In
this work, we adopt the Leiden algorithm [35] and further
study the effect of different partitioning methods in Section
V-F .
B. Agent Specialization
1) Observation:After agent assignment, each agent first
reasons independently within its assigned community to de-
velop region-specific expertise. We formulate this reasoning
process as a sequential decision process, where the agent
repeatedly takes graph sampling actions and uses the returned
evidence to determine its subsequent actions.
A key issue is how the sampled graph evidence is repre-
sented to the LLM agent. Existing AGL methods typically
verbalize all returned evidence into natural language. For
example, after retrieving the 1-hop neighbors of a target
node, the node identities, labels, and textual attributes of the
sampled neighbors are listed one by one in the prompt. As
more graph evidence is sampled, this verbalized context grows
accordingly. Example 1 illustrates such a representation.
Example 1 (verbalized evidence).
“The 1-hop neighbors information is:
[1] Nodeu 1, labely u1, title and abstract ...
[2] Nodeu 2, labely u2, title and abstract ...
. . .
[200] Nodeu 200, labely u200, title and abstract ...”
This representation is problematic for graph reasoning.
First, graph neighborhoods are inherently unordered, whereas
verbalization necessarily places the sampled neighbors into a
sequence. The resulting arbitrary order can therefore affect
the LLM’s reasoning. Second, multi-hop neighborhoods can
expand rapidly, and verbalizing every sampled node together
with its textual attribute introduces substantial token overhead.
To address this issue, unlike existing methods that uniformly
verbalize all sampled graph evidence, MAAGL separates
the returned evidence intostructural evidenceandsemantic
evidenceand represents them differently. Structural evidence is
summarized by a compactstructural signature, while semantic
evidence is filtered according to its relevance to the target
node. We first introduce the structural signature.
Definition 1 (Structural Signature):The structural signature
of a nodevat reasoning steptis a vector ofdstructural
statistics,
zt v = [g1(v, Ot v), g2(v, Ot v), . . . , gd(v, Ot v)],(2)
whereO t v denotes the set of sampled nodes observed up to
stept, and eachg j(·)is a deterministic graph statistic.

5
In this work, we use six statistics and divide them into static
and dynamic dimensions. The four static dimensions describe
the structural position ofvand remain unchanged during
reasoning.Degreemeasures its local connectivity.PageRank
measures its global importance under random walks. Theclus-
tering coefficientmeasures the connectivity among its 1-hop
neighbors. Thecross-community fractionmeasures the fraction
of 1-hop neighbors that belong to communities different from
that ofvin Eq. (1). The remaining two dimensions are updated
as the agent samples new evidence.Label entropymeasures
the diversity of labels among the sampled labeled nodes, while
themajority-label fractionmeasures the proportion of the most
frequent label. Both are computed over the labeled nodes in
the sampled node setO t v of Definition 1. Whenever a graph
action returns new labeled nodes, the dynamic dimensions
are recomputed while the static dimensions keep their initial
values,
zt v[j] =
(
gj(v, Ot v)ifg j is dynamic,
z0 v[j]otherwise. (3)
Therefore, the signature evolves with the sampled evidence
while remaining fixed in dimensionality.
For interaction with the LLM, the numeric signature is
rendered into a short textual form that reports the name and
value of each statistic,
text(zt v) =  name(gj), gj(v, Ot v) d j=1.(4)
In addition to the signature, the observed label counts over the
labeled nodes inO t v, from which the two dynamic dimensions
are computed, are also reported to the agent.
For semantic evidence, MAAGL does not retain the textual
attributes of all sampled nodes. Instead, the sampled nodes
are ranked by their semantic relevance to the target node,
measured by the cosine similarity between their text embed-
dings. Only the top-ktextual attributes are retained. Unlike the
arbitrary ordering of graph neighbors, this order is meaningful
because it directly reflects semantic relevance. Accordingly,
the observation of agentA i for target nodev∈c i at steptis
represented as
st v =  v,x v,text(z t v),X t,k v  ,(5)
wherex v is the textual attribute of the target node andX t,k v
denotes the textual attributes of the top-ksemantically relevant
nodes among the evidence sampled up to stept. Example 2
illustrates the resulting representation.
Example 2 (MAAGL evidence representation).
Structural evidence:
Degree= 3
Neighbor-label entropy= 0.92
Observed label counts: Label 5: 1, Label 9: 1, Label 23:
1
Cross-community fraction= 0.33
Semantic evidence (top-k):
1. Nodeu 1: title and abstract ...
2. Nodeu 3: title and abstract ...
The structural signature avoids imposing an arbitrary order
on the sampled neighborhood. Since every dimension is com-
puted from the sampled node set rather than its enumeration,
it satisfies permutation invariance.
Property 1 (Permutation Invariance):For any nodevand
sampled node setO t v, the structural signaturez t v is invariant
to any permutation of the nodes inO t v.
Proof:LetO t v ={u 1, . . . , um}be the sampled node
set at stept, and letσbe any permutation of its elements.
For the dynamic dimensions, define the label proportion of
classy∈ Yasp y(Ot v) =|{u∈O t v :y u =y}|/|O t v|.
Since permutation does not change the label counts,p y(Ot v) =
py(σ(Ot v))for every classy. Hence, both the label entropy
H(O t v) =− P y∈Y py(Ot v) logp y(Ot v)and the majority-label
fractionF(O t v) = max y∈Y py(Ot v)are invariant to node
ordering. For the static dimensions, degree depends only on
|N1(v)|, clustering coefficient on the edges amongN 1(v),
cross-community fraction on the number of neighbors outside
the community ofv, and PageRank on the graph topology.
None of these quantities depends on how the neighbors are
enumerated. Therefore,g j(v, Ot v) =g j(v, σ(Ot v))for every
j= 1, . . . , d, so thatzt v takes the same value forO t v and
σ(Ot v). Thus, the structural signature is permutation-invariant.
At the same time, the dimensionality ofz t v remains fixed
regardless of how many nodes have been sampled. Together
with top-kfiltering of semantic evidence, this representation
avoids arbitrary neighbor ordering while preventing the obser-
vation from growing directly with the sampled neighborhood
size.
2) Action:Given the current observation, the agent selects
an evidence-collection action to acquire additional information
from the graph. Consistent with the two types of evidence
defined above, we consider structural evidence obtained from
local graph neighborhoods and semantic evidence obtained
from text similarity. Accordingly, the evidence-collection ac-
tion space is
Aevi ={a 1-hop, a2-hop}| {z }
structural search
∪ {asem}| {z }
semantic search
.(6)
Each action returns a set of sampled nodes together with
their available labels and textual attributes. As described in
the previous subsection, the returned evidence is not directly
verbalized. Instead, its structural information is incorporated
into the structural signature, while its semantic information is
filtered by relevance before being presented to the agent.
Definition 2 (Localr-hop Structural Neighborhood Search):
Given a target nodevand a radiusr∈ {1,2}, the actiona r-hop
samples ther-hop neighborhood
Nr(v) ={u∈V|d G(u, v) =r},(7)
whered G(·,·)denotes the shortest-path distance onG. The
sampled nodes provide structural evidence for updating the
signaturez t v. Their textual attributes are further ranked by
semantic relevance to the target node, and only the top-kare
retained as semantic evidence in the observation.
Definition 3 (Global Top-kSemantic Neighborhood Search):
Given a target nodev, the actiona sem retrieves theknodes
whose textual attributes are most semantically similar tox v:
N k sem(v) = TopKu∈V\{v} cos(Enc(xv),Enc(x u)),(8)

6
whereEnc(·)denotes a text encoder. The textual attributes of
these nodes form the semantic evidence, while their available
labels are also incorporated into the sampled node set used to
update the dynamic dimensions of the structural signature.
3) Prediction:With the observation and evidence-
collection actions defined above, each agent independently
decides whether to collect more evidence or terminate the
reasoning process with a prediction. At stept, agentA i
selects an action according to its policy,
at v =π i(st v,M i),(9)
wheres t v is the current observation andM i is the private
memory of agentA i. The action is selected fromA evi ∪
{apred}, whereA evi contains the evidence-collection actions
defined above.
If an evidence-collection action is selected, the returned
nodes are added to the sampled node set. The structural
signature is then updated by Eq. (3), while the semantic
evidence is re-ranked and filtered to retain the top-krelevant
textual attributes. The next observation becomes
st+1 v =  v,x v,text(z t+1 v ),X t+1,k v  .(10)
The agent then continues reasoning based on the updated
evidence. Whena pred is selected, the reasoning process ter-
minates and agentA i produces
ˆyv =A i

st v,M i  .(11)
We allow at mostTreasoning steps. If the budget is exhausted
beforea pred is selected, the final step is used for prediction.
We setT= 3in our experiments. Fig. 3 shows the prompt
template used at each reasoning step, which presents the
structural signature, the filtered semantic evidence, the search
history, and the available experiences to the agent.
Adaptive Search Termination.Different instances may re-
quire different amounts of graph evidence. Some nodes can be
resolved from their own attributes or a small local neighbor-
hood, whereas others require additional structural or semantic
evidence. Requiring every instance to perform the same num-
ber of searches can therefore introduce redundant evidence
collection. Besides increasing token cost, unnecessary searches
may bring irrelevant nodes into the reasoning context and
interfere with the final prediction.
Inspired by the Search-Constrained Thinking strategy of
AgentGL [3], we encourage each agent to stop searching
once the collected evidence is sufficient. Rather than learning
this behavior through reinforcement learning, we implement
it directly through prompting. After every evidence-collection
action, the agent is instructed to review the updated evidence
and determine whether another search is necessary before
selecting its next action.
4) Memory:After reasoning on a labeled training node ter-
minates, the agent stores the resulting trajectory in its private
memory. Since the ground-truth label is available during this
stage, we assign a binary reward according to whether the
prediction is correct,
rv =⊮[ˆyv =y v].(12)
You are an agent responsible for one community of
a{graph kind}. Your task is to classify the
target{item}into one of the candidate
categories.
Target{item}: "{node text}"
Structural signature of the target node, computed
by the system and updated as evidence is sampled:
{for each dimensionj: name(g j ) =g j (v, Ot v)
(description); an updated dimension also shows its
previous value}
- observed label counts:{label: count, ...}
Semantic evidence, the sampled nodes most relevant
to the target (best match first):
{top-ksampled texts, each with its label}
Search history:
{one line per earlier action, with the newly
observed label counts}
Experiences available to you:
{for each experience: IF{metric}>{threshold}
THEN take the{action}action}
Candidate categories: [{label list}]
Choose exactly one action:
1-hop: sample the 1-hop neighbors of the target
node.
2-hop: sample the 2-hop neighborhood; newly
observed labels update the signature.
semantic: retrieve the most semantically similar
labeled nodes in the whole graph.
predict: output the final label based on the
current context.
Respond strictly in JSON:{"thought": "...",
"action": "1-hop|2-hop|semantic|predict", "label":
"one candidate category, required only when action
is predict"}
Fig. 3. Prompt template for one reasoning step of an agent. Curly braces
denote placeholders filled by the system at runtime.
The complete reasoning process is recorded as
τv =

z0 v, s0 v, a0 v, . . . , sTv v , aTv v ,ˆyv, yv, rv  ,(13)
whereT v ≤T−1denotes the step at whicha pred is selected.
We explicitly store the initial structural signaturez 0 v with each
trajectory, which will later be used to retrieve past cases with
similar structural patterns during collaborative reasoning.
After all labeled nodes in communityc i have been pro-
cessed, agentA i obtains its trajectory memory
Mtraj i ={τ v |v∈V L ∩c i},(14)
whereV L denotes the set of labeled training nodes. The private
memory of agentA i is written asM i = (Mtraj i ,M exp i ). This
stage only populatesM traj i , whileM exp i stores the learned
experiences produced by the experience learning stage in
Section IV-D. Since agents reason only over their assigned
communities and do not communicate in this stage, their spe-
cialization processes can be performed in parallel. Algorithm 1
summarizes the complete agent specialization process.
C. Collaborative Reasoning
After agent specialization, each agent has developed its
own reasoning experience within the assigned community and
stored historical trajectories in its trajectory memory. We next

7
Algorithm 1Agent Specialization
Require:communities{c i}M i=1; agents{A i}M i=1; labeled node
setV L; step budgetT
Ensure:trajectory memories{M traj i }M i=1
1:foreach agentA i,i= 1, . . . , M,in parallel do
2:M traj i ← ∅
3:M exp i ← ∅
4:foreach nodev∈V L ∩c i do
5:initialize sampled node setO 0 v and compute struc-
tural signaturez 0 v
6:X 0,k v ← ∅
7:s 0 v ←(v,x v,text(z 0 v),X 0,k v )
8:fort= 0,1, . . . , T−1do
9:selecta t v =π i(st v,M i)by Eq. (9)▷force
apred whent=T−1
10:ifa t v =a pred then
11:outputˆy v by Eq. (11)
12:T v ←t
13:break
14:end if
15:executea t v to sample additional nodes by Def-
initions 2 and 3
16:updateO t+1 v with the newly sampled nodes
17:update structural signaturez t+1 v by Eq. (3)
18:rank sampled textual evidence and retain
X t+1,k v
19:update observations t+1 v by Eq. (10)
20:review the current evidence before deciding
whether another search is needed
21:end for
22:r v ←⊮[ˆyv =y v]
23:constructτ v by Eq. (13)
24:M traj i ← Mtraj i ∪ {τv}
25:end for
26:end for
27:return{M traj i }M i=1
describe how these specialized agents collaborate on cases that
are difficult for a single agent.
Collaboration Trigger.After agentA i produces a prediction
for nodev, we estimate how reliable the prediction is from
its performance on structurally similar cases. Specifically, we
retrieve themtrajectories inM traj i whose stored structural
signatures are most similar to the initial signaturez 0 v. The
confidence of agentA i is defined as their similarity-weighted
success rate,
conf i(v) =
P
τ∈Q m i (v) sim(z0 v, zτ )r τ P
τ∈Q m i (v) sim(z0v, zτ ) ,(15)
whereQ m i (v)⊆ Mtraj i denotes the retrieved trajectories,z τ
is the initial structural signature stored with trajectoryτ, and
rτ is its reward. We use cosine similarity forsim(·,·). A
high value indicates that agentA i has frequently succeeded
on nodes with similar structural signatures. Collaboration
is triggered whenconf i(v)< δ, whereδis a predefined
threshold.
You are agent{id}, one of several agents
classifying the same{item}in a{graph kind}. In
the previous round every agent reasoned
independently. First review the other agents’
opinions below, then give your own updated
prediction independently. You may keep or revise
your previous answer; do not follow the majority
blindly, follow the evidence.
Target{item}: "{node text}"
Structural signature of the target node:
{signature dimensions and observed label counts,
as in the reasoning prompt}
Previous-round opinions:
{for each participant: agent id; predicted label;
brief rationale}
Candidate categories: [{label list}]
Respond strictly in JSON:{"thought": "...",
"label": "one candidate category"}
Fig. 4. Prompt template for debate rounds after the first round. Each
participant reads the previous-round opinions and independently updates its
prediction.
Collaborator Selection.When collaboration is triggered, we
compute the same confidence score for every other agent using
its own trajectory memory. Agents that have performed well
on structurally similar cases are preferred as collaborators.
Specifically, we select
K(v) = arg top-K
j̸=i
conf j(v),(16)
whereconf j(v)is computed fromM traj j using Eq. (15). In
this way, collaborator selection directly reuses the region-
specific experience accumulated during agent specialization
and requires no additional training.
Collaborative Prediction.The owning agentA i and the
selected agents inK(v)then perform debate-style collaborative
reasoning [17]. In the first round, each collaborator receives the
target node(v,x v)together with its initial structural signature
z0 v and independently runs the reasoning process described in
Section IV-B. Each agent instead collects and represents its
own structural and semantic evidence using its private policy
and memory, thereby preserving the specialization learned
from its assigned community.
After the first round, each participant outputs a prediction
together with a short rationale. In the following rounds, the
participants read the previous-round predictions and rationales
and independently reconsider their own decisions without
collecting additional graph evidence. Letˆy (j,ℓ) v denote the
prediction of agentA j at debate roundℓ. AfterDrounds,
the final prediction is obtained by majority vote,
ˆyv = arg max y∈Y

 n j∈ {i} ∪ K(v) : ˆy(j,D) v =y o

 .(17)
If multiple labels receive the same number of votes, we
choose the prediction from the tied participant with the highest
confidence score. Algorithm 2 summarizes the complete col-
laborative reasoning process. Fig. 4 shows the prompt template
used in the debate rounds.
Communication Cost.A direct transfer of conventional multi-
agent collaboration to graphs would require agents to exchange

8
Algorithm 2Collaborative Reasoning
Require:target nodev; owning agentA i; agents{A j}M j=1;
trajectory memories{M traj j }M j=1; thresholdδ; collabora-
tor numberK; reasoning budgetT; debate roundsD
Ensure:final predictionˆy v
1:initializez 0 v and observations 0 v
2:A i independently reasons onvusing Algorithm 1 and
outputsˆy(i,1) v
3:computeconf i(v)fromM traj i by Eq. (15)
4:ifconf i(v)≥δthen
5:returnˆy (i,1) v
6:end if
7:foreach agentA j,j̸=ido
8:computeconf j(v)fromM traj j by Eq. (15)
9:end for
10:select collaboratorsK(v)by Eq. (16)
11:foreachA j ∈ K(v)in parallel do
12:initializes 0 v,j using(v,x v, z0 v)
13:A j independently collects and represents its own graph
evidence
14:outputˆy (j,1) v with a short rationale
15:end for
16:forℓ= 2, . . . , Ddo
17:foreach participantA j,j∈ {i} ∪ K(v),in parallel
do
18:read the round-(ℓ−1)predictions and rationales
19:output revised predictionˆy (j,ℓ) v with a short ratio-
nale
20:end for
21:end for
22:obtainˆy v by majority vote using Eq. (17)
23:returnˆy v
the sampled graph evidence in textual form. For anh-hop
neighborhood, this context grows with the number of sampled
nodes and their textual attributes, which can lead to substantial
token costs. In MAAGL, structural evidence is communicated
through the fixed-dimensional signaturez 0 v, while sampled
semantic evidence remains local to each agent. During debate,
agents exchange only their predictions and length-bounded
rationales. Therefore, the communication cost does not grow
with the size of the sampled graph neighborhood.
D. Experience Learning
After agent specialization and collaborative reasoning, each
agent has accumulated trajectories that record the sampled
evidence, reasoning actions, predictions, and corresponding
rewards. These trajectories provide more than individual suc-
cessful or failed cases: they can reveal recurring relations
between graph characteristics and effective reasoning strate-
gies. We therefore further extract reusable experience from the
trajectory memories and use it to guide subsequent reasoning.
Existing experience-learning methods for LLM agents typi-
cally store experience as free-form natural language. For graph
reasoning, however, such descriptions can be ambiguous. For
example, an experience such as “search for semantic evidence
when nearby labels disagree” does not specify how disagree-
ment is measured or when the recommendation should be
applied. Since MAAGL already represents structural evidence
through explicitly defined signature metrics, we instead ex-
press each experience as a quantitative condition together with
a reasoning recommendation.
Experience Generation.Each agent first learns experience
independently from its own trajectory memory. Following
the contrastive learning principle of ExpeL [36], agentA i is
provided with successful and failed trajectories fromM traj i ,
together with the names and descriptions of the structural sig-
nature metrics. The agent compares these trajectories and iden-
tifies structural conditions that are associated with different
reasoning outcomes. Each generated experience is represented
as
ϵ= (g, θ, ρ)(18)
wheregis one of the signature metrics,θspecifies a threshold
on that metric, andρis a recommended reasoning strategy
when the conditiong > θholds. The generated experiences
are stored in the private experience memoryM exp i of agent
Ai. Together with the trajectory memory, the complete private
memory is thereforeM i = (M traj i ,M exp i ). The trajectory
memory provides concrete past cases, whereas the experience
memory provides reusable reasoning guidance distilled from
these cases.
Cross-Agent Experience Validation.An experience learned
from one community may reflect only its local graph patterns
and may not generalize to other regions. We therefore validate
each generated experience using the trajectories of the other
agents before making it globally available. Importantly, this
validation operates directly on stored trajectories and does not
require additional LLM calls.
Consider an experienceϵ= (g, θ, ρ)generated by agentA i.
For another agentA j, letT + j (ϵ)denote the trajectories whose
initial structural signatures satisfyg(z τ )> θand which take
the recommended actionρat some step, and letT − j (ϵ)contain
trajectories satisfying the same structural condition but never
takingρ. We measure the effectiveness of the recommendation
on agentA j as
∆j(ϵ) = ˆpj(r= 1| T + j (ϵ))−ˆpj(r= 1| T − j (ϵ))(19)
whereˆpj(·)denotes the empirical success rate over the cor-
responding trajectories. A positive∆ j(ϵ)indicates that, for
nodes satisfying the structural condition, trajectories following
ρachieve a higher success rate.
We admit an experience to the shared experience setSwhen
it is supported by sufficiently many other agents,
|{j̸=i: ∆ j(ϵ)≥γ}| ≥κ(20)
whereγcontrols the minimum improvement required from the
recommended strategy andκspecifies the minimum number
of supporting agents. Experiences that pass this validation are
added toSand can be used by all agents in subsequent
reasoning, while agent-specific experiences remain in their
corresponding private experience memories. Example 3 illus-
trates the validation process, and Algorithm 3 summarizes the
complete experience learning process.

9
Example 3 (cross-agent validation).Suppose agentA 1 generates
the experienceϵ= (label entropy,0.8,semantic search). For the
trajectories of agentA 2 with label entropy above0.8, those that
performed semantic search achieve a higher success rate than those
that did not, giving∆ 2(ϵ) = 0.27. Similarly,∆ 3(ϵ) = 0.23. If
γ= 0.2andκ= 2, the experience is supported by two other
agents and is therefore added to the shared experience setS.
Algorithm 3Experience Learning
Require:trajectory memories{M traj i }M i=1; experience mem-
ories{M exp i }M i=1; signature metrics{g 1, . . . , gd}; shared
experience setS; thresholdsγandκ
Ensure:updated{M exp i }M i=1 andS
1:foreach agentA i,i= 1, . . . , M,in parallel do
2:sample successful and failed trajectories fromM traj i
3:generate candidate experiencesI i ={ϵ= (g, θ, ρ)}
from the sampled trajectories
4:M exp i ← Mexp i ∪I i
5:end for
6:foreach experienceϵ∈I i generated by agentA i do
7:foreach agentA j,j̸=ido
8:compute∆ j(ϵ)fromM traj j by Eq. (19)
9:end for
10:ifEq. (20) holdsthen
11:S ← S ∪ {ϵ}
12:end if
13:end for
14:return{M exp i }M i=1 andS
Computation Cost.The structural signature introduces only
limited additional computation. The four static dimensions are
computed once before reasoning and cached for subsequent
episodes. During reasoning, only the two dynamic dimen-
sions need to be updated as new labeled nodes are sampled.
Since these dimensions depend on label counts, they can
be updated incrementally from the newly collected evidence
without recomputing the entire sampled neighborhood. Con-
fidence estimation in Eq. (15) requires comparing the current
initial signature with stored trajectory signatures, with a direct
cost ofO(|M traj i |d)for agentA i. Cross-agent collaborator
selection and experience validation reuse the same cached
signatures and stored trajectory outcomes and therefore require
no additional graph sampling or LLM calls.
V. EXPERIMENTS
We conduct extensive experiments to answer the following
research questions (RQs):
•RQ1:How does MAAGL compare with existing state-
of-the-art AGL methods?
•RQ2:How does each core component contribute to the
overall performance?
•RQ3:How sensitive is MAAGL to key hyperparameters?
•RQ4:How efficient is MAAGL in terms of reasoning
cost?
A. Datasets
We evaluate MAAGL on four TAGs spanning two domains.
For each domain, we use one dataset forin-domaintraining
TABLE I
STATISTICS OF THE DATASETS.
Domain Dataset #Nodes #Edges #Classes Setting
Academic OGB-Arxiv 169,343 1,166,243 40 In-Domain Cora-full 19,793 126,842 70 Zero-shot
E-commerce OGB-Products 54,025 74,420 47 In-Domain Amazon-Computers 87,229 1,256,548 10 Zero-shot
and evaluation, and a second, disjoint dataset from thesame
domain to assesszero-shot transfer. In the academic cita-
tion domain, nodes represent papers, edges represent citation
relations, and the node text is the title and abstract of the
paper; we train on OGB-Arxiv [13] and transfer to Cora-
full [37], [38]. In the e-commerce domain, nodes represent
products, edges connect products that are frequently bought
together, and the node text is the title and description of the
product in OGB-Products and a user review of the product in
Amazon-Computers; we train on the OGB-Products subset of
TAPE [13], [39] and transfer to Amazon-Computers [40]. The
statistics of all datasets are summarized in Table I.
B. Baselines
We compare MAAGL against three categories of baselines:
•GNN methodslearn node representations by message
passing or graph transformers and are trained on each
dataset separately.
– GCN[7] aggregates the normalized features of the
1-hop neighbors in every layer.
– GraphSAGE[8] aggregates sampled neighbors with
a learnable function.
– GraphGPS[11] combines local message passing
with global attention in a modular graph transformer.
•Single-agent methodsuse a single LLM-powered agent
to adaptively collect graph evidence and reason.
– Graph-CoT[28] lets the LLM iteratively invoke
graph functions to collect graph information.
– ReaGAN[15] equips an agent with neighbor-
expansion and semantic retrieval tools, and predicts
using the retrieved evidence.
– AgentGL[3] structures graph reasoning into
thought-action-observation trajectories and optimizes
the agent policy through reinforcement learning.
– GraphReAct[29] performs multi-step reasoning and
acting for graph inference.
•Orchestration-based methodscoordinate multiple role-
specific agents through a predefined workflow for graph
reasoning.
– GraphTeam[30] coordinates role-specialized agents
to collaboratively solve graph reasoning tasks.
– GraphAgent[2] organizes multiple role-specific
agents into a predefined workflow for graph reason-
ing.
C. Experimental Setup
Following AgentGL [3], on the two in-domain training
datasets (OGB-Arxiv and OGB-Products) we sample 3,000

10
TABLE II
OVERALL NODE CLASSIFICATION PERFORMANCE(ACCURACY ANDMACRO-F1)UNDER THE IN-DOMAIN AND ZERO-SHOT TRANSFER SETTINGS.
Settings In-Domain Zero-shot Transfer
Datasets OGB-Arxiv OGB-Products Cora-full Amazon-Comp.
Category Methods Acc Ma-F1 Acc Ma-F1 Acc Ma-F1 Acc Ma-F1
GNN
Methods
GCN [7] 0.6460 0.3521 0.6710 0.4014 – – – –
GraphSAGE [8] 0.6210 0.3766 0.6610 0.4151 – – – –
GraphGPS [11] 0.5530 0.2044 0.5170 0.2635 – – – –
Single-Agent
Methods
Graph-CoT [28] 0.6240 0.4165 0.3690 0.2902 0.5780 0.5399 0.8340 0.8657
ReaGAN [15] 0.6390 0.4764 0.7210 0.5074 0.6447 0.5974 0.7830 0.8306
AgentGL [3] 0.65500.48510.6860 0.5011 0.6320 0.5850 0.7100 0.6495
GraphReAct [29] 0.6320 0.4389 0.6650 0.4821 0.6260 0.5624 0.8110 0.8179
Orchestration-based
Methods
GraphTeam [30] 0.6200 0.4487 0.5990 0.3909 0.5950 0.5457 0.6180 0.5500
GraphAgent [2] 0.6531 0.4652 0.6730 0.4768 0.6170 0.5762 0.7110 0.6856
OursMAAGL 0.66900.48320.7650 0.5588 0.6590 0.6035 0.8670 0.8902
training nodes each for optimization, and for each dataset we
sample 1,000 nodes from the original test split for evaluation.
The supervised baselines (GCN, GraphSAGE, and GraphGPS)
are trained on the same 3,000 training nodes, using the node
features shipped with each dataset, with model selection on
the official validation split; since their label space is tied to
the training graph, they have no zero-shot transfer results.
For the zero-shot transfer datasets (Cora-full and Amazon-
Computers), no training is performed on the target graph and
we directly evaluate on 1,000 sampled test nodes: MAAGL
reuses the shared experiences and the trajectory memories
learned on the in-domain dataset of the same domain, which
transfer unchanged because they contain structural signatures,
reasoning actions, and correctness outcomes but no label
names. MAAGL adopts GPT-4o-mini as the backbone of
every agent and is fully training-free: it relies solely on the
accumulated trajectories and the learned experiences, with-
out updating any model parameter. Unless stated otherwise,
MAAGL partitions the graph with Leiden intoM= 10
communities and usesK= 2collaborators,D= 2debate
rounds,R= 2learning rounds, and a confidence thresholdδ
set to the 25th percentile of the training confidences.
D. Overall Performance (RQ1)
We first evaluate the overall performance of MAAGL
against all baselines on node classification, under both the
in-domain and the zero-shot transfer settings. The results are
reported in Table II, where baselines are grouped by category
and our method is listed at the bottom. We summarize the key
observations below.
•MAAGL achieves the best Accuracy on all four datasets.
For Macro-F1, it achieves the best results on OGB-
Products and Amazon-Comp., while remaining compet-
itive with the best baselines on OGB-Arxiv and Cora-
full. These results demonstrate the overall effectiveness
of MAAGL. A possible reason is that region-specific
specialization allows each agent to learn from structurally
and semantically similar cases, while selective collabora-
tion further introduces complementary reasoning when
the owning agent is less reliable.
•Agent-based methods generally outperform conventional
GNN methods, particularly in terms of Macro-F1. This
advantage is also reflected in the zero-shot transfer set-
ting, where trained GNN models cannot be directly trans-
ferred to unseen graphs, whereas agent-based methods
remain applicable without retraining. This observation
supports the motivation of agentic graph learning, where
LLM agents can adaptively collect graph evidence and
exploit textual semantics for different instances, providing
stronger generalization across graphs.
•Existing orchestration-based methods do not consistently
outperform single-agent methods. For example, GraphA-
gent performs competitively on OGB-Arxiv but falls
behind strong single-agent methods on the other datasets.
This observation is consistent with our motivation that
simply organizing multiple agents does not fundamentally
address the limitation of applying a shared reasoning pol-
icy across different graph regions. In contrast, MAAGL
consistently improves upon both categories by allowing
agents to specialize in different regions and collaborate
selectively when complementary experience is needed.
E. Ablation Study (RQ2)
To understand the contribution of each core component, we
compare MAAGL with four ablated variants on OGB-Arxiv,
each removing or replacing exactly one design choice: (i)w/o
structural signature, which verbalizes the retrieved neighbors
as raw text in the ReaGAN style and removes the structural
signature from the observation, while the numeric signature
is still used for the collaboration trigger and collaborator
selection so that only the representation effect is isolated; (ii)
w/ free-text experience, which replaces the structured experi-
ences with free-text experiences in natural language kept in
each agent’s private experience memory, without cross-agent
validation; (iii)w/o collaboration, where the owning agent
always answers alone; and (iv)w/ max-confidence merge,
which keeps collaboration but replaces the debate and the vote
with the single prediction of the most confident participant.
Figure 5 reports Accuracy on node classification.

11
0.56 0.58 0.60 0.62 0.64 0.66
Accuracy
w/o metric-based repr.
w/ free-text experience
w/o collaboration
w/ max-conf merge
MAAGL (full)
Fig. 5. Ablation study on node classification on OGB-Arxiv.
•Removing the structural signature causes the largest per-
formance degradation. This confirms the importance of
separating structural and semantic evidence instead of
directly verbalizing sampled neighborhoods, supporting
our motivation that raw textual serialization is unsuitable
for graph reasoning.
•Replacing the structured experience with free-text expe-
rience consistently weakens performance. This suggests
that expressing experience through explicit structural
conditions and recommendations provides more reliable
guidance than unconstrained natural-language lessons.
•Removing collaboration also degrades performance,
showing that independently specialized agents are not
sufficient for all instances. Selective collaboration allows
agents to incorporate complementary experience from
other regions when their own reasoning is less reliable.
•Replacing debate-based collaboration with max-
confidence merging leads to a smaller performance drop.
This indicates that simply selecting the most confident
prediction cannot fully exploit the complementary
reasoning of multiple agents, while iterative exchange
and refinement provides additional benefit.
F . Hyperparameter Sensitivity (RQ3)
We study the sensitivity of MAAGL to four key hyper-
parameters: (a) the choice of community detection algorithm
including Leiden, Louvain, and random partition. (b) the
number of communitiesM∈ {5,10,20}). (c) the number
of debate rounds (D∈ {1,2,3}). (d) the confidence threshold
that triggers collaboration (δset to the 10th, 25th, or 40th
percentile of the training confidences). Figure 6 reports node
classification Accuracy as each hyperparameter varies while
the others are fixed at their default values. We also study the
effect of the number of learning rounds (from the warm-up
only up toR= 4), in which collaborative reasoning and
experience learning alternate. Figure 7 reports the accuracy
on the training set of OGB-Arxiv as more learning rounds are
performed.
•MAAGL is relatively insensitive to the choice of com-
munity detection algorithm. Leiden, Louvain, and ran-
dom partition all achieve comparable performance, while
community-based partitioning provides a small advan-
tage. This suggests that the benefit mainly comes from
Leiden Louvain Random
0.62
0.64
0.66
0.68
0.70
Accuracy
0.669 0.666 0.664
(a) Community detection al-
gorithm
5 10 20
Number of communities M
0.650
0.655
0.660
0.665
0.670
Accuracy
(b) Number of communities
1 2 3
Debate rounds D
0.650
0.655
0.660
0.665
Accuracy
(c) Number of debate
rounds
10 25 40
Threshold percentile of δ
0.65
0.66
0.67
Accuracy
(d) Confidence threshold
Fig. 6. Hyperparameter sensitivity of MAAGL on OGB-Arxiv.
warm-up round 1 round 2 round 3 round 4
0.72
0.74
0.76
0.78
0.80
Training-set accuracy
0.720
0.759
0.773
0.776
0.782
Fig. 7. Accuracy on the learning set of OGB-Arxiv across learning rounds.
assigning different graph regions to independent agents
rather than relying on a particular partitioning algorithm.
•The number of communities has a clear effect on perfor-
mance. Too few communities limit agent specialization,
while too many communities divide the graph into overly
small regions and reduce the experience available to each
agent. A moderate number of communities provides a
better balance between specialization and sufficient local
experience.
•A small number of debate rounds is sufficient for effective
collaboration. Increasing the number of rounds initially
improves performance by allowing agents to reconsider
their predictions using complementary opinions, whereas
further debate provides little additional benefit and may
introduce unnecessary reconsideration.
•A moderate confidence threshold achieves the best per-
formance. A low threshold triggers collaboration for too
few cases, while a high threshold invokes collaboration

12
OGB-Arxiv OGB-Products Cora-full Amazon-Comp.
102
103
104
105
106
Tokens per message (log)
serialized 1-hop serialized 2-hop structural signature
Fig. 8. Tokens per cross-agent message on the four datasets.
OGB-Arxiv OGB-Products Cora-full Amazon-Comp.
0.0
0.5
1.0
1.5
2.0Avg. searches per episode
w/o termination w/ termination
Fig. 9. Average number of search actions per episode on each dataset, with
and without the Adaptive Search Termination.
even when the owning agent is already reliable. This sup-
ports selectively introducing collaboration for uncertain
instances.
•Performance improves consistently over successive learn-
ing rounds and gradually approaches saturation. This
indicates that agents can progressively accumulate useful
experience from historical reasoning trajectories, while
the diminishing improvement in later rounds suggests
convergence of the learning process.
G. Efficiency Analysis (RQ4)
We analyze the two efficiency designs of MAAGL on all
four datasets. Figure 8 compares the number of tokens one
cross-agent message carries, when the message serializes the
1-hop or 2-hop neighborhood and when it carries only the
structural signature, measured on the 1,000 test nodes of each
dataset with 200 tokens per node text. Figure 9 reports the
average number of search actions per episode on each dataset,
with and without adaptive search termination.
•The structural signature substantially reduces the token
cost of cross-agent communication across all datasets.
Unlike serialized neighborhoods, whose size grows
rapidly with the number of retrieved nodes and neigh-
borhood depth, the signature remains compact and fixed
in size. This confirms that separating structural evidence
from raw textual content provides a more efficient repre-
sentation for multi-agent communication.
•Adaptive search termination consistently reduces the
number of search actions across all datasets. This in-
dicates that many instances can be resolved without
exhausting the full search budget, and allowing the agent
to stop once sufficient evidence has been collected avoids
unnecessary graph exploration and improves reasoning
efficiency.
VI. CONCLUSION
In this work, we revisited multi-agent collaboration for
agentic graph learning and identified two key limitations in
directly transferring existing collaborative reasoning methods
to graphs. First, existing AGL methods generally rely on a
shared reasoning policy across different graph regions, which
can be suboptimal when these regions exhibit different struc-
tural and semantic patterns. Second, communicating graph
evidence through natural-language serialization introduces ar-
bitrary neighbor ordering and rapidly increasing token costs.
To address these issues, we proposed MAAGL, which assigns
independent agents to different graph communities for region-
specific specialization and represents sampled structural and
semantic evidence separately. Structural evidence is summa-
rized by a permutation-invariant structural signature, while
semantic evidence is filtered according to relevance. Historical
trajectories are further used to estimate agent confidence, select
complementary collaborators, and learn reusable reasoning
experience. Extensive experiments on four benchmark datasets
demonstrate that MAAGL consistently improves over existing
AGL methods.
One limitation of the current framework is that the dimen-
sions of the structural signature are manually specified based
on commonly used graph statistics. An important direction
for future work is therefore to automatically discover or select
task-specific structural signature dimensions from graph data
and reasoning trajectories.
ACKNOWLEDGMENT
This work is supported by the Australian Research Council
under the Discovery Project scheme (No.DP240101591).
REFERENCES
[1] F. Xia, C. Peng, J. Ren, F. G. Febrinanto, R. Luo, V . Saikrishna, S. Yu,
and X. Kong, “Graph learning,”Foundations and Trends® in Signal
Processing, vol. 19, no. 4, pp. 362–519, 2026.
[2] Y . Yang, J. Tang, L. Xia, X. Zou, Y . Liang, and C. Huang, “Graphagent:
Agentic graph language assistant,” inProceedings of the 2025 Confer-
ence on Empirical Methods in Natural Language Processing, 2025, pp.
26 360–26 379.
[3] Y . Sun, K. Li, D. Fan, J. Liu, and Q. Tan, “Agentgl: Towards agentic
graph learning with llms via reinforcement learning,”arXiv preprint
arXiv:2604.05846, 2026.
[4] Q. Tan, N. Liu, and X. Hu, “Deep representation learning for social
network analysis,”Frontiers in big Data, vol. 2, p. 2, 2019.
[5] J. Gao, J. Wu, and J. Ding, “Heterogeneous graph condensation,”IEEE
Transactions on Knowledge and Data Engineering, vol. 36, no. 7, pp.
3126–3138, 2024.
[6] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and P. S. Yu, “A
comprehensive survey on graph neural networks,”IEEE transactions on
neural networks and learning systems, vol. 32, no. 1, pp. 4–24, 2020.
[7] T. N. Kipf and M. Welling, “Semi-supervised classification with graph
convolutional networks,”arXiv preprint arXiv:1609.02907, 2016.
[8] W. Hamilton, Z. Ying, and J. Leskovec, “Inductive representation
learning on large graphs,”Advances in neural information processing
systems, vol. 30, 2017.
[9] P. Veli ˇckovi´c, G. Cucurull, A. Casanova, A. Romero, P. Lio, and Y . Ben-
gio, “Graph attention networks,”arXiv preprint arXiv:1710.10903, 2017.

13
[10] C. Ying, T. Cai, S. Luo, S. Zheng, G. Ke, D. He, Y . Shen, and T.-Y .
Liu, “Do transformers really perform badly for graph representation?”
Advances in neural information processing systems, vol. 34, pp. 28 877–
28 888, 2021.
[11] L. Ramp ´aˇsek, M. Galkin, V . P. Dwivedi, A. T. Luu, G. Wolf, and
D. Beaini, “Recipe for a general, powerful, scalable graph transformer,”
Advances in Neural Information Processing Systems, vol. 35, pp.
14 501–14 515, 2022.
[12] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y . Cao,
“React: Synergizing reasoning and acting in language models,”arXiv
preprint arXiv:2210.03629, 2022.
[13] W. Hu, M. Fey, M. Zitnik, Y . Dong, H. Ren, B. Liu, M. Catasta, and
J. Leskovec, “Open graph benchmark: Datasets for machine learning on
graphs,”Advances in neural information processing systems, vol. 33,
pp. 22 118–22 133, 2020.
[14] Y . Bei, W. Zhang, S. Wang, W. Chen, S. Zhou, H. Chen, Y . Li, J. Bu,
S. Pan, Y . Yuet al., “Graphs meet ai agents: Taxonomy, progress, and
future opportunities,”arXiv preprint arXiv:2506.18019, 2025.
[15] M. Guo, X. Zhu, H. Xue, C. Zhang, S. Lin, J. Huang, Z. Ye, and
Y . Zhang, “Reagan: Node-as-agent-reasoning graph agentic network,”
arXiv preprint arXiv:2508.00429, 2025.
[16] R. Wang, S. Liang, Q. Chen, Y . Huang, M. Li, Y . Ma, D. Zhang,
K. Qin, and M.-F. Leung, “Graphcogent: Mitigating llms’ working
memory constraints via multi-agent collaboration in complex graph
understanding,” inProceedings of the ACM Web Conference 2026, 2026,
pp. 3811–3822.
[17] Y . Du, S. Li, A. Torralba, J. B. Tenenbaum, and I. Mordatch, “Improving
factuality and reasoning in language models through multiagent debate,
2023,”URL https://arxiv. org/abs/2305.14325, vol. 3, 2023.
[18] G. Hao, Y . Long, and Z. Zhao, “Self-evolving multi-agent systems via
decentralized memory,”arXiv preprint arXiv:2605.22721, 2026.
[19] K. Xu, C. Li, Y . Tian, T. Sonobe, K.-i. Kawarabayashi, and S. Jegelka,
“Representation learning on graphs with jumping knowledge networks,”
inInternational conference on machine learning. pmlr, 2018, pp. 5453–
5462.
[20] X. Wang, H. Ji, C. Shi, B. Wang, Y . Ye, P. Cui, and P. S. Yu, “Hetero-
geneous graph attention network,” inThe world wide web conference,
2019, pp. 2022–2032.
[21] X. Fu, J. Zhang, Z. Meng, and I. King, “Magnn: Metapath aggregated
graph neural network for heterogeneous graph embedding,” inProceed-
ings of the web conference 2020, 2020, pp. 2331–2341.
[22] S. Yun, M. Jeong, R. Kim, J. Kang, and H. J. Kim, “Graph transformer
networks,”Advances in neural information processing systems, vol. 32,
2019.
[23] Y . Rong, W. Huang, T. Xu, and J. Huang, “Dropedge: Towards deep
graph convolutional networks on node classification,”arXiv preprint
arXiv:1907.10903, 2019.
[24] Y . You, T. Chen, Y . Sui, T. Chen, Z. Wang, and Y . Shen, “Graph con-
trastive learning with augmentations,”Advances in neural information
processing systems, vol. 33, pp. 5812–5823, 2020.
[25] Y . Wang, W. Wang, Y . Liang, Y . Cai, J. Liu, and B. Hooi, “Nodeaug:
Semi-supervised node classification with data augmentation,” inPro-
ceedings of the 26th ACM SIGKDD international conference on knowl-
edge discovery & data mining, 2020, pp. 207–217.
[26] S. Liu, R. Ying, H. Dong, L. Li, T. Xu, Y . Rong, P. Zhao, J. Huang, and
D. Wu, “Local augmentation for graph neural networks,” inInternational
conference on machine learning. PMLR, 2022, pp. 14 054–14 072.
[27] A. Yehudai, L. Eden, A. Li, G. Uziel, Y . Zhao, R. Bar-Haim, A. Cohan,
and M. Shmueli-Scheuer, “Survey on evaluation of llm-based agents,”
arXiv preprint arXiv:2503.16416, 2025.
[28] B. Jin, C. Xie, J. Zhang, K. K. Roy, Y . Zhang, Z. Li, R. Li, X. Tang,
S. Wang, Y . Menget al., “Graph chain-of-thought: Augmenting large
language models by reasoning on graphs,” inFindings of the Association
for Computational Linguistics: ACL 2024, 2024, pp. 163–184.
[29] X. Yu, Z. Kuai, C. Zhou, X. Xie, R. Jiang, X. Zhang, H. Cheng,
X. Zhang, and Y . Fang, “Graphreact: Reasoning and acting for multi-step
graph inference,”arXiv preprint arXiv:2605.07357, 2026.
[30] X. Li, Q. Chu, Y . Chen, Y . Liu, Y . Liu, Z. Yu, W. Chen, C. Qian,
C. Shi, and C. Yang, “Graphteam: Facilitating large language model-
based graph analysis via multi-agent collaboration,”arXiv preprint
arXiv:2410.18032, 2024.
[31] E. Du, X. Li, T. Jin, Z. Zhang, R.-H. Li, and G. Wang, “Graphmaster:
Automated graph synthesis via llm agents in data-limited environments,”
arXiv preprint arXiv:2504.00711, 2025.
[32] Z. Zhang, K. Shi, Z. Yuan, Z. Wang, T. Ma, K. Murugesan, V . Galassi,
C. Zhang, and Y . Ye, “Agentrouter: A knowledge-graph-guided llm
router for collaborative multi-agent question answering,”arXiv preprint
arXiv:2510.05445, 2025.
[33] J. Wang, S. Zhao, H. Wang, Y . Fan, L. Zhang, Y . Liu, and T. Liu,
“Optimal-agent-selection: State-aware routing framework for efficient
multi-agent collaboration,”arXiv preprint arXiv:2511.02200, 2025.
[34] H. Gao and Y . Zhang, “Memory sharing for large language model based
agents,”arXiv preprint arXiv:2404.09982, 2024.
[35] V . A. Traag, L. Waltman, and N. J. Van Eck, “From louvain to leiden:
guaranteeing well-connected communities,”Scientific reports, vol. 9,
no. 1, p. 5233, 2019.
[36] A. Zhao, D. Huang, Q. Xu, M. Lin, Y .-J. Liu, and G. Huang, “Expel: Llm
agents are experiential learners,” inProceedings of the AAAI Conference
on Artificial Intelligence, vol. 38, no. 17, 2024, pp. 19 632–19 642.
[37] A. Bojchevski and S. G ¨unnemann, “Deep gaussian embedding of
graphs: Unsupervised inductive learning via ranking,”arXiv preprint
arXiv:1707.03815, 2017.
[38] O. Shchur, M. Mumme, A. Bojchevski, and S. G ¨unnemann, “Pit-
falls of graph neural network evaluation, 2018,”arXiv preprint
arXiv:1811.05868, 1811.
[39] X. He, X. Bresson, T. Laurent, A. Perold, Y . LeCun, and B. Hooi, “Har-
nessing explanations: Llm-to-lm interpreter for enhanced text-attributed
graph representation learning,” inInternational conference on learning
representations, vol. 2024, 2024, pp. 5711–5732.
[40] H. Yan, C. Li, R. Long, C. Yan, J. Zhao, W. Zhuang, J. Yin, P. Zhang,
W. Han, H. Sunet al., “A comprehensive study on text-attributed
graphs: Benchmarking and rethinking,”Advances in Neural Information
Processing Systems, vol. 36, pp. 17 238–17 264, 2023.
