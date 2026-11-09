---
title: 'HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents'
url: https://arxiv.org/abs/2608.02650
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Zian Zhai
- Xingyu Tan
- Gaowang Zou
- Xiaoyang Wang
- Wenjie Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.02650
pages: 10
chars: 51306
fetched_at: '2026-11-08T13:34:32+00:00'
kb_version: 1
---

# HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents

HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use
LLM Agents
Zian Zhai1, Xingyu Tan1, Gaowang Zou1, Xiaoyang Wang1, Wenjie Zhang1
1University of New South Wales
zian.zhai@unsw.edu.au, xingyu.tan@unsw.edu.au, z5445224@ad.unsw.edu.au, xiaoyang.wang1@unsw.edu.au,
wenjie.zhang@unsw.edu.au
Abstract
Large language model (LLM) agents increasingly rely on ex-
ternal tools to complete complex real-world tasks. However,
reliable tool-use planning remains challenging due to the lim-
itations of implicit reasoning and the evolving nature of real-
world execution environments. Existing tool-use agents typ-
ically rely on LLMs to infer tool compositions from textual
descriptions, which can lead to inefficient exploration and un-
reliable execution in complex tasks. To address these chal-
lenges, we model tool relations at the schema level and con-
struct a directed Tool–Schema Hypergraph, in which tools are
represented as hyperedges from their required input-schema
nodes to their output-schema nodes. Furthermore, we propose
HyperAgent, a Tool–Schema Hypergraph-guided framework
for dynamic planning and execution. Given a task, Hyper-
Agent first extracts a task-relevant tool context graph and
uses it to guide the construction of a schema-aware Task
DAG. During execution, HyperAgent dynamically realizes
each subtask by constructing a state-conditioned tool support
graph through deficit-oriented expansion, which identifies un-
resolved requirements and retrieves supporting producer tools
according to the current agent state. Experiments on App-
World demonstrate that HyperAgent improves task comple-
tion performance while reducing redundant API calls, LLM
interactions, and token consumption compared with existing
agent baselines.
Introduction
With continued improvements in the reasoning capabili-
ties of large language models (LLMs) (OpenAI 2023; Yang
et al. 2024), LLM-based autonomous agents are increasingly
deployed to perform complex real-world tasks (Yao et al.
2022; Kim et al. 2025). Equipped with tool-use capabilities,
these agents can invoke external APIs, manipulate operat-
ing systems, and interact with software services to satisfy
user requests. Such capabilities extend LLMs beyond lan-
guage generation, allowing agents to take concrete actions
and affect their environments (Yang et al. 2023; Qin et al.
2023; Patil et al. 2023). In many practical scenarios, how-
ever, fulfilling a user request requires the agent to interpret
the task and determine several actions toward the intended
goal (Zhang et al. 2025; Yu, Ding, and Sato 2025). For
tool-using agents, this further entails selecting tools that are
aligned with the current objective and executable under the
available information, resources, and environment state (Liu
et al. 2024a; Lumer et al. 2025).
To enhance the task-solving capabilities of LLM agents,
numerous approaches have been proposed. Existing studies
have primarily advanced tool-using agents along two com-
plementary directions. The first focuses on online acting,
where the agent repeatedly selects tools, observes its exe-
cution result, and determines the next action from the up-
dated state (Yao et al. 2022; Kim et al. 2025). This interac-
tion loop enables the agent to incorporate runtime observa-
tions and adapt subsequent actions to execution outcomes.
The second focuses on task planning, where the LLM agent
decomposes a user request into intermediate goals or gen-
erates a sequence of intended actions before execution (Sun
et al. 2023; Erdogan et al. 2025). Such plans provide useful
global guidance and help alleviate the myopic behavior of
agents that select actions step by step.
Despite this progress, existing approaches have two main
limitations. First, relying on LLMs to infer executable tool
chains implicitly from textual tool descriptions is unreliable.
Specifically, for a target operation, the model must identify
not only a semantically relevant tool but also the upstream
tools required to produce its input parameters. This depen-
dency reasoning becomes particularly fragile when the agent
must process a large volume of tool documentation. Sec-
ond, although recent tool-retrieval methods preserve tools
directly related to the user request, they may exclude seman-
tically distant yet operationally indispensable prerequisites
for the target tools. Once omitted, these tools can only be
recognized during online execution when the chosen tool is
found to be non-executable.
These limitations have motivated a growing research
interest in graph-based approaches. For example, at the
tool level, ToolNet constrains each tool selection through
transitions in a directed tool graph (Liu et al. 2024a),
while Graph RAG–Tool Fusion expands semantically re-
trieved tools along dependency edges to recover prerequisite
tools (Lumer et al. 2025). At the task level, GNN4TaskPlan
employs graph neural networks to select structurally coher-
ent subtasks (Wu et al. 2024), and GTool encodes request-
specific tool dependencies to guide the generation of com-
plete tool trajectories (Chen et al. 2025b). These methods
explicitly model tool relations that need to be inferred im-
plicitly by LLMs, and allow the planner to recover prerequi-
site tools beyond semantic retrieval.
arXiv:2608.02650v1  [cs.AI]  31 Jul 2026

Nevertheless, existing graph-based approaches remain
limited in two critical aspects. First, current graphs capture
only coarse tool dependencies and do not specify which up-
stream outputs satisfy the inputs of a downstream tool (Lee,
Kim, and Jo 2025). When multiple tools can produce the
same required parameter, this ambiguity makes it diffi-
cult to identify the necessary producers and avoid redun-
dant calls. Second, executable tool composition is state-
dependent rather than fixed. Some required inputs may al-
ready be available from the user request or previous ex-
ecutions, thereby changing which upstream tools are still
needed. A statically planned tool path may therefore become
redundant or incomplete during execution.
To this end, we first construct a directed Tool–Schema
Hypergraph (TSH) to model fine-grained parameter-level re-
lations among tools. Each tool is represented as a directed
hyperedge from its input schema nodes to its output schema
and effect nodes. We further annotate port links between out-
put and input schema nodes to capture schema-level data
flow across tools. Based on the constructed TSH, we propose
HyperAgent, a planning and execution framework operating
over the TSH. Before execution, HyperAgent retrieves a tool
context graph that contains potentially useful tools selected
according to semantic relevance and hypergraph structure,
and uses it to guide the decomposition of the task into a
Task DAG whose nodes are connected by identified schema-
level dependencies. During execution, HyperAgent realizes
each ready subtask with a Tool Support Subgraph selected
according to the current agent state. The resulting observa-
tions update the agent state and are used to refine the remain-
ing Task DAG, so that subsequent tool compositions adapt
to the evolving execution context.
In summary, our main contributions are summarized as
follows:
• We construct a directed Tool–Schema Hypergraph using
a real-world API dataset, which models tool relations as
fine-grained schema dependencies.
• We propose HyperAgent, a two-stage planning and execu-
tion framework that extracts a task-relevant Tool Context
Graph and uses it to construct a schema-level Task DAG
before execution.
• We introduce deficit-oriented support graph expansion to
construct state-conditioned Tool Support Subgraphs for
ready subtasks, enabling tool compositions to adapt to the
dynamical agent state.
• Extensive experiments on AppWorld show that HyperA-
gent improves task completion while reducing redundant
API calls, LLM interactions, and token consumption com-
pared with the selected baselines.
Related Work
Tool-Use Planning. Tool-use planning enables language
agents to select and compose tools into multi-step action se-
quences. Early methods rely on language-model reasoning
to guide tool use. ReAct (Yao et al. 2022) interleaves reason-
ing with actions, whereas ART (Paranjape et al. 2023) con-
structs reasoning programs from retrieved demonstrations.
However, direct trajectory generation provides limited ex-
ploration of alternative tool sequences. Search-based meth-
ods instead evaluate multiple candidates through depth-first
search in ToolLLM (Qin et al. 2023) and A*-style search in
ToolChain (Zhuang et al. 2024). Yet trajectory search still re-
lies on textual descriptions to infer tool dependencies, which
may lead to invalid tool selections or infeasible plans.
Graph-Augmented Agents. Graph-based methods make
tool dependencies explicit by organizing tool relations and
invocation paths into structured graphs (Bei et al. 2025).
ControlLLM (Liu et al. 2024b) searches tool graphs en-
coding parameter dependencies, while ToolNet (Liu et al.
2024a) organizes large tool collections through directed
transitions. However, tool graphs may be incomplete, irrel-
evant to a request, or insensitive to the evolving execution
trajectory (Chen et al. 2026; Patel et al. 2026). GTool (Chen
et al. 2026) reduces irrelevant relations through request-
specific construction and addresses incompleteness through
missing-edge prediction, while Dynamic Tool Dependency
Retrieval (Patel et al. 2026) updates retrieval using both the
query and current trajectory. Ordinary graphs represent de-
pendencies through pairwise edges, whereas hypergraphs
naturally capture higher-order relations involving multiple
entities (Antelmi et al. 2023). However, their use for ex-
ecutable tool-schema planning under different agent states
remains underexplored.
Preliminaries
Tool-Schema Hypergraph (TSH). LetH= (V,E,D)
denote a Tool-Schema Hypergraph, whereVrepresents
schema and effect nodes,Econtains tool hyperedges, and
Dcontains port-level schema-dependency links between
tool hyperedges. The node set contains input-schema nodes,
output-schema nodes, and tool-effect nodes, i.e.,V=V I ∪
VO ∪ VF . For simplicity, we useV O to denote both output
schemas and effect nodes. Each tool hyperedgee∈ Eis di-
rected from a set of input nodes to a set of output and effect
nodes, i.e.,E e(VI ) ={V O}.The TSH contains port-level
schema-dependency linksD ⊆ VO × VI ,where each de-
pendencyD(v o, vi) =windicates that the output schema
vo may support the input schemav i with weightw. A sub-
hypergraphH S = (V S,E S,D S)is induced by a subset of
tool hyperedgesE S ⊆ E, whereV S = S e∈ES V(e),and
DS ={D(v o, vi) =w∈ D |vo, vi ∈ VS}.
Definition 1(Neighbor Tools).Given two tool hyperedges
ei, ej ∈ E,e i is an upstream neighbor ofe j if at least
one of the output schemas ofe i can support at least one
of the input schemas ofe j through dependency edges, i.e.,
ei ∈Nbr −(ej)⇐ ⇒ ∃vo ∈O(e i),∃v i ∈I(e j),∃w >
0s.t.(v o, vi)∈ D.Symmetrically,ej is a downstream neigh-
bor ofe i, ande j ∈Nbr +(ei)⇐ ⇒ei ∈Nbr −(ej).
Method
HyperGraph Construction
Graph Conversion. We construct the TSH based on
In-N-Out (Lee, Kim, and Jo 2025), an expert-annotated
parameter-level API graph. In the original graph, API tools
and their input and output parameters are represented as
nodes. Directed intra-API links connect input parameters

to the corresponding API and the API to its output param-
eters. In addition, directed inter-API schema-dependency
links connect an output parameter of one API to an input
parameter of another when the returned value can serve as
a valid argument for the downstream API. These links are
constructed through LLM-based filtering and expert anno-
tation. Although their tool–schema graph captures schema-
level data dependencies across tools, it does not explicitly
represent the joint constraints of real-world tool invocation.
Specifically, an API is executable only when all of its re-
quired inputs are jointly available and its outputs are jointly
produced by the same invocation. To encode these con-
straints, we convert the original graph into a directed Tool–
Schema Hypergraph. For each API tool, we represent it as
a hyperedge and preserve the original schema nodesVand
inter-tool schema-dependency linksD.
Graph Refinement. Some tools do not return reusable pa-
rameters but primarily change the environment state, such
as sending a message and creating a transaction. Conversely,
the execution of a tool may depend on an environment pre-
condition, which is often described in its documentation but
is not explicitly presented by input parameters. For example,
a login tool may establish an authenticated session that is re-
quired before invoking a protected API. To represent such
precondition and effect dependencies, we extract additional
effect and condition nodes from API documentation. First,
we use GPT-4o to extract candidate state changes and ex-
ecution preconditions from each tool description and align
them with the existing input and output schemas. Expert an-
notators then validate the proposed alignments. State predi-
cates that are not represented by the original schema nodes
are introduced into the node set as additional effect or condi-
tion nodes. We preserve the original port–level schema de-
pendency links in In–N–Out. For the newly introduced ef-
fect and condition nodes, we enumerate candidate effect–
precondition pairs and remove pairs with incompatible do-
mains or entities. Then, we use GPT-4o to score the seman-
tic relevance of the remaining pairs and further filter the ir-
relevant pairs. Subsequently, human annotators verify the
filtered candidates and label valid links as strong or weak
state dependencies, while other pairs are discarded. The re-
tained effect–condition links are incorporated into the port–
level dependency link set. Due to space limitations, we pro-
vide implementation details for the refinement procedure
and graph statistics in Appendix A.
Task-Level Planning
Given a user request, HyperAgent first extracts a task-
relevant Tool Context Graph from the full TSH. The context
graph restricts the planning space to potentially useful tools
while retaining the schema-level connections among them.
Conditioned on this context graph, the agent is prompted
to decompose the request into a schema–level Task DAG,
where each node represents a subtask and each edge speci-
fies data, effect, or ordering dependencies between subtasks.
Task Interpretation. User requests are often expressed at
a high level, leaving the intended operations, relevant enti-
ties, constraints, and desired environment changes only im-
plicit. To help the agent locate the relevant region of the
TSH, we prompt it to produce a structured task interpreta-
tion. Formally, given a user requestt, the agent is asked to
output a structured representationd t =

dop t , dsch t  , where
dop t captures the intended operations, anddsch t identifies can-
didate schemas, values, constraints, and desired outcomes
expressed or implied by the request. We use the components
ofd t as retrieval signals to anchor relevant tool hyperedges
and schema nodes in the TSH.
Seed Hyperedge Anchoring. To identify initial task-
relevant tools, we retrieve tool hyperedges based on the
operation-level interpretationd op t . Specifically, for each hy-
peredgee∈ E, we use its functional description and com-
pute the semantic similarity withd op t , which is denoted as
sim(e, dop t ) = cos (z(e),z(dop t )),(1)
wherez(·)denotes the embedding function. We select the
Top-Khyperedges whose similarity scores exceed a thresh-
oldθ e to form the seed hyperedge setE seed.
Seed Node Anchoring. We distinguish input and precondi-
tion nodesV I from output and effect nodesVO. The schema-
level interpretationd sch t may contain entities, constraints,
required values, and desired outcomes that correspond di-
rectly to these schema nodes. We therefore used sch t to an-
chor relevant nodes in the TSH. For each nodev∈ V, we
compute the semantic similarity between its description and
dsch t using the same embedding-based similarity function in
Equation 1. We select the top-Kv input-side and output-side
nodes whose similarity scores exceedθ v, yieldingV I seed ⊆
VI andV O seed ⊆ VO, respectively. The final seed node set is
the union of both sides, i.e.,V seed =V I seed ∪ VO seed.
Context Graph Extraction. Starting from the seed hyper-
edges and nodes, we perform bounded backward search
over the TSH to construct a compact, task-relevant context
graph. The expansion reduces the global tool space while
retaining the schema–level dependencies connecting the re-
trieved tools. We first augment the seed hyperedge set with
tools directly associated with the anchored schema nodes.
For each output-side seed node, tools satisfyingv o ∈O(e)
are considered as its direct producer candidates. Similarly,
for each input-side seed node, tools satisfyingv i ∈I(e)
are considered direct consumer candidates. Among the pro-
ducer and consumer hyperedge candidates, we compute the
operation-level similarity defined in Equation 1 and add the
top-Kcandidates for each seed node to the seed hyper-
edge setE seed. We then initialize the backward frontier as
B0 =V I seed ∪{v i |v i ∈I(e), e∈ Eseed}. At each hoph, the
backward expansion follows dependency linksDin reverse
towards the output and effect nodes. Formally, ifv i ∈ Bh,
D(vo, vi) =w >0, andv o ∈O(e p), thene p is consid-
ered as a producer candidate forvi. We rank producer candi-
dates by jointly considering the strength of the schema-level
dependency and their semantic relevance to the operation–
level task interpretation:
sback(e, dop t ) =w(v o, vi)·cos  z(e),z(d op t )  .(2)
For each frontier node, we retain the top-Kproducer candi-
dates and add them to the retrieved hyperedge set. The input
nodes of the newly added producers form the next backward

Phase 1: Simplified Hypergraph
Construction (Offline)
Phase 2: Simplified Retrieval &
DAG Generation (Online)
Phase 3: Topological Execution & 
Online Refinement
Graph
Conversion
Graph
Conversion
Assistant Assistant
Tool-Schema Hypergraph (TSH)
Each tool is an N-to-N hyperedge; schema dependencies bridge tools
Supervisor Instruction Grounded Agent State
Assistant 1
Assistant 2
Assistant 3
Structured Task Interpretation
Tool Context Graph Extraction
Top-K bounded backward expansion from two anchor types
Task DAG Generation
Serialize tools + port-level dependency evidence
Task DAG Grounded Agent State
Grounded values
email · order_id ·
file_path
Topological Execution Loop
1. Select Ready Subgoal
e.g., s3: Download receipt
Assistant 3
Python
Executor
LLM Refiner
Grounded
Agent State
Supervisor
Task Submitted
TGC/SGC results
✅  Concpt iat goal criteria
✅  Goal criteria initants
✅  Renoneat goal criteria
▥
Gold Tool Recall
Done
Input-schema
nodes
Tool 
hyperedges
Output /
effect nodes
query
access_token
contact.email
contact.name
query
access_token
order_id
paid_amount
order_id
access_token
receipt.file_path
receipt_downloaded
email_addresses
attachment_file_paths
subject
body
sent_email_id
sent_thread_id
email_sent
■  input　■  output　■  effect　- - schema dependency
N-to-N incidence: each hyperedge consumes a set of schemas 
and jointly produces output/effect sets.
Port-level links: producer outputs support downstream inputs.
Operation view
find contact · find order ·
download · email
Schema view
contact.email · order_id ·
receipt.file_path
Seed hyperedge
Seed schema node
s1
s2
s3
D1-D3: output-schema →  input-schema links
Schema-Level Task DAG
q
s1: Find Alice's email
s2: Find latest order s3: Download receipt
s4: Send receipt
D2
D1
D3
D1: s1.contact_email →  s4.email_addresses
D2: s2.order_id →  s3.order_id
D3: s3.receipt.file_path →  s4.attachment_file_paths
Observation Δ:  values, effects, errors
2. Deficit-Oriented Support Graph Construction
Search candidate TSH and retain a complete task-conditioned subgraph
Candidate TSH Selected Support Graph→
phone.search_contacts
amazon.
download_order_receipt
gmail.send_email
amazon.show_orders
Retrieved context
phone.
search
amazon.
orders
amazon.
receipt
gmail.
send
D1 s4 D3
D2
s1: Find 
Alice's email
s2: Find
latest order
s3: Download
receipt
s4: Send 
receipt
D2
D1
D3
Only a few
values grounded
gmail.send_email
attachment_file_paths
✓
4. Verify Contract & Update State
newly grounded schemas · achieved effects · remaining deficits
phone.search
amazon.orders
amazon.receipt
gmail.send
email
order_id
file_path
email_sent
✕  Unresolved
update state or refine DAG /
support graph
✓  Contract Satisfied　
Graph
Conversion
Request: Email Alice the latest
Amazon order receipt
3. Execute Selected Support Graph (Python Runtime)
Generate multi-tool code · ground arguments · preserve variables
Amazon Spotify Venmo Gmail Phone
SimpleNote FileSystem local DBs
Expert-annotated
Tool Documentation
Roommate/Family
Global Tool Ecosystem
Splitsville
 Todo List
Figure 1: The framework of HyperAgent.
frontierB h+1. This expansion continues until the hop bud-
get is exhausted or no new producer is retrieved, inducing
the Tool Context Graph.
Definition 2(Tool Context Graph).A Tool Context Graph is
the task-relevant subgraphHs = (Vs,E s,D s)of the TSH in-
duced by the seed set, whereEs =E seed,V s = S e∈Es  I(e)∪
O(e)

,andD s ={(v o, vi)∈ D |vo ∈ Vs, vi ∈ Vs}.The
graphH s provides the LLM planner with a compact con-
text that preserves both task relevance and the schema-level
dependency topology among the retrieved tools.
Task Decomposition. After constructing the tool context
graphH s, we serialize it into a compact textual description,
where each hyperedge is represented by its API name and
description, and each schema node is described by its as-
sociated API tool, name, and concise description. Moreover,
the dependency links are serialized as directed links from the
output schemas of producer hyperedges to the input schemas
of consumer hyperedges. We provide the prompt illustra-
tion in Appendix B. Based on this serialized context, the
LLM planner is prompted to construct a Task DAG (Yang
et al. 2025; Dong et al. 2024), where each node represents a
subtask and each edge encodes the identified dependencies
among subtasks, including schema-level data and effect de-
pendencies from the Tool Context Graph. For each subtask,
the planner specifies its local goal, target output schemas or
effects, and a set of candidate terminal tools. For each de-
pendency between subtasks, the planner identifies relevant
schema-dependency links from the Tool Context Graph that
connect the output schemas or effects of the upstream sub-
task to the input schemas required by the downstream sub-
task.
Definition 3(Task DAG).Given the Tool Context Graph
Hs, a Task DAG is an LLM-generated directed acyclic graph
G= (Q,L). Each nodeq i ∈ Qrepresents a subtask and
is defined asq i = (g i, τi, bEi, ϕi),whereg i is the local
goal,τ i ⊆ VO denotes the target output schemas or ef-
fects, bEi ⊆ Es is a small set of candidate terminal tools, and
ϕi records the execution status of the subtask. Each edge
ℓij ∈ Lrepresents a data or effect dependency fromqi toq j.
Such a dependency is grounded in schema-level links from
Hs that connect outputs associated withqi to inputs required
byq j.
Task Execution
Topological Execution. Once the initial Task DAG is con-
structed, the agent executes subtasks following the depen-
dency topology. At execution stepℓ, the agent identifies the
frontier subtasks whose predecessors have been completed
and selects one for execution. Here, we formally define the
agent state.
Definition 4(Agent State).Given the current Task DAG
Gℓ = (Q ℓ,L ℓ)before theℓ-th execution iteration, the run-
time agent state is defined asS ℓ = (C ℓ,R ℓ,I ℓ),whereC ℓ
records the execution history,R ℓ records the execution sta-
tus of subtasks, andI ℓ stores the runtime schema–value
bindings and achieved effects accumulated during execu-
tion.
For the selected subtask, the agent retrieves a tool support
subgraph from the TSH for its concrete tool-level realiza-
tion, which is introduced in the following subsection. After
executing the selected subtask, the newly grounded schema–
value bindings∆I ℓ and achieved effects update the agent
state:S ℓ+1 =StateUpdate(S ℓ,∆I ℓ).The updated state is
then used either to execute the next subtask or to refine the
remaining Task DAG, yieldingG ℓ+1.
Subtask Verification. A successful tool call alone is insuf-
ficient to verify subtask completion. After executing the se-
lected tool support graph, HyperAgent determines whether

the execution results satisfy the expected outputs, effects,
and constraints of the current subtask. Specifically, it aligns
the execution trace with the selected support graph and ex-
amines the successful API calls, schema–value bindings, in-
termediate computation results, and achieved effects. A sub-
task is marked as completed only when its required outputs
are materialized with valid schema-level evidence or its tar-
get effects are supported by the execution trace. The verified
terminal outputs are then incorporated intoI ℓ+1, allowing
HyperAgent to determine the initial state of subsequent sub-
tasks. Otherwise, HyperAgent retains the observed outputs
and effects and refines the current Task DAG. Due to space
limitations, the prompt templates and detailed procedure are
provided in the Appendix B, C, respectively.
Tool–Level Planning
The Task DAG specifies the subtasks and candidate termi-
nal tools for each subtask. However, HyperAgent does not
determine an executable tool composition in advance, as the
agent state evolves with newly obtained values and effects
during execution, which may change the required tools. In-
stead, HyperAgent dynamically constructs a Tool Support
Subgraph for each subtask by identifying unresolved input
requirements of candidate terminal tools and expanding pro-
ducer tools according to the current state.
Tool–Schema Support. Before presenting the detailed ex-
pansion algorithm, we define Tool-Schema Support to quan-
tify the support strength between tools and input schemas.
Definition 5(Tool-Schema Support).Given a Tool-Schema
HypergraphH= (V,E,D), lete∈ Ebe a tool hyperedge
andr∈ VI be an input-schema node. The Tool-Schema Sup-
port frometormeasures the strongest support of the outputs
ofeto the input schemar, and is defined as
ρ(e, r) = max
o∈O(e)
W(o, r),(3)
where
W(o, r) =
w,(o, r)∈ D,
0,otherwise.
Ifρ(e, r)>0, thenecan serve as a producer tool for
schemar. For efficient lookup during online execution, we
precompute the support between each input-schema node
and each tool hyperedge and store the scores in a sparse pro-
ducer matrixA prod ∈R |VI |×|E| .Each row corresponds to
an input schemarand contains the support scores of its can-
didate producer tools, i.e.,A prod(r, e) =ρ(e, r).
Deficit–Oriented Expansion. For each candidate terminal
toole t ∈ bEi, Deficit–Oriented Expansion (DOE) performs
beam search over the TSH to construct a Tool Support Sub-
graph conditioned on the current agent stateS ℓ. Starting
from each proposed terminal tool, DOE maintains a deficit
set that records input-schema requirements not satisfied by
the current agent state or the selected producer tools. It it-
eratively expands candidate subgraphs by adding producer
hyperedges to satisfy the deficit set and terminates when a
complete support subgraph is found. For readability, we omit
the subtask superscriptq i in this subsection.
Definition 6(Deficit Set).Given an agent stateS ℓ =
(Cℓ,R ℓ,I ℓ)and a candidate support subgraphG h =
(Vh,E h,D h), the deficit setM Gh contains input-schema
nodes required by the selected tools that are neither avail-
able in the current agent state nor supported by the output-
schema nodes ofG h through the retained dependency links.
For the candidate terminal toole t, DOE initializes the
candidate subgraphG 0 = (V0,E 0,D 0)with the current agent
stateS ℓ, whereV 0 =I(e t),E 0 ={e t},andD 0 =∅.The
initial deficit setM G0 is determined by the input schemas of
et that are not grounded in the current agent state. We encode
the deficit set as a sparse binary vectorm Gh ∈ {0,1}|VI |×1,
where each dimension indicates whether the corresponding
input-schema node belongs to the current deficit set:
mGh (r) =
1, r∈M Gh ,
0, r /∈MGh , r∈ VI .(4)
At each expansion step, DOE selects producer hyperedges
that can resolve the current deficits. Since the output head
O(e)of a producer hyperedge may jointly support multi-
ple unresolved input-schema nodes, DOE prioritizes hyper-
edges whose outputs have greater overlap with the current
deficit setM Gh. This overlap is defined as
Ω(e, MGh ) =
X
r∈MGh
ρ(e, r),(5)
whereρ(e, r)denotes the Tool-Schema Support defined
above. The top-Kproducer hyperedges with positive sup-
port are selected as expansion directions. For each selected
producere p, DOE adds the hyperedge together with its input
and output schema nodes and retains the dependency links
through which its outputs support the nodes in the current
deficit set. The deficit set is then updated after expansion by
deleting the resolved deficits and introducing input schemas
required bye p that are not already grounded in the current
state or supported by the expanded subgraph. At each expan-
sion depth, the subgraph candidates are ranked according to
the number of unresolved schema nodes in the deficit set,
i.e.,|M G (ep ) h+1 |, and the top-Bcandidates with the smallest
deficit sets are retained for the next expansion. Candidates
with empty deficit sets are considered complete support sub-
graphs and are no longer expanded.
Support Graph Selection. Given a subtaskq i, letS qi ℓ de- note the set of complete support subgraphs returned by DOE
for the proposed candidate terminal tools in bEi. HyperA-
gent selects a support subgraphG qi ∈S qi ℓ as the schema- complete tool composition for realizingq i. If no feasible
support subgraph is available or the execution fails, the out-
come is incorporated into the agent state and the remaining
Task DAG is refined accordingly.
Experiments
Dataset
We evaluate HyperAgent on the AppWorld dataset (Trivedi
et al. 2024), a benchmark that evaluates an LLM agent’s
ability to complete user-directed tasks by interacting

with APIs from simulated consumer applications, includ-
ing email, payment, music, shopping, phone, and file-
management services. The agent operates through a state-
ful Python interpreter and performs tasks of varying diffi-
culty. Task correctness is determined by unit tests that verify
whether the requested changes were successfully applied,
whether any unintended modifications were introduced, and
whether the final answer matches the reference answer when
applicable. The benchmark contains 250 task scenarios, each
instantiated with three variants, resulting in 750 tasks in to-
tal. These tasks are divided into a training set of 35 scenarios
(105 tasks), a development set of 20 scenarios (60 tasks), a
normal test set (TEST-N) of 56 scenarios (168 tasks), and
a challenge test set (TEST-C) of 139 scenarios (417 tasks).
Compared with TEST-N, TEST-C requires longer and more
complex interaction sequences and may involve applications
that are unseen during training. Performance is measured us-
ing Task Goal Completion (TGC), which reports the pro-
portion of successfully completed tasks, and Scenario Goal
Completion (SGC), which counts a scenario as solved only
when all of its task variants are completed successfully.
Baselines
Supervised Fine-Tuning (SFT). We include three super-
vised baselines that learn from successful agent trajectories.
SFT-GT transforms gold AppWorld traces into ReAct-style
interaction trajectories for supervised training. RFT (Yuan
et al. 2023) samples trajectories from the base agent and
fine-tunes the model only on successful rollouts. EI (An-
thony, Tian, and Barber 2017) performs RFT iteratively, us-
ing the improved policy from each round to collect training
trajectories for the next round.
Direct Preference Optimization (DPO). We also com-
pare HyperAgent with preference-based methods. DPO-
MCTS (Putta et al. 2024) uses Monte Carlo tree search to
discover alternative action trajectories and constructs pref-
erence pairs from their estimated returns. DMPO (Shi et al.
2024) extends preference optimization to multi-turn interac-
tion by jointly modeling the decisions within preferred and
rejected trajectories.
Reinforcement Learning (RL). We include policy-gradient
methods that optimize agents directly from environment re-
wards. PPO (Schulman et al. 2017) trains policies using a
learned value model for advantage estimation. RLOO (Ah-
madian et al. 2024) estimates trajectory-level advantages
by comparing multiple rollouts sampled for the same task.
GRPO (Shao et al. 2024) performs clipped group-relative
updates using normalized rewards among rollouts of the
same task, while LOOP reuses old sampled trajectories
through clipped policy updates and assigns credit at trajec-
tory (bandit), turn, or token-level (Chen et al. 2025a).
Non-Fine-Tuning Methods (NFT). For NFT methods, we
perform four agent scaffolds. ReAct (Yao et al. 2022) solves
tasks through iterative reasoning, execution, and observa-
tion. Plan and Execution (PlanExec) (Erdogan et al. 2025)
generates a plan which consists subtasks before ReAct exe-
cution, whereas Reflexion (FullCodeRefl) (Kim et al. 2025)
explicitly writes and revises execution feedback after each
execution. Traj (SetBSR+Snippet) (Gupta et al. 2025) aug-
Table 1: Performance comparison with different paradigms
on AppWorld.
Model Prompting
AppWorld
Test-N Test-C
TGC SGC TGC SGC
GPT-4o
ReAct 48.8 32.1 30.2 13.0
PlanExec 44.6 23.2 19.7 7.9
FullCodeRefl 33.9 26.8 19.2 12.2
HyperAgent 63.1 52.6 35.7 18.9
GPT-4turbo
ReAct 26.8 12.5 17.5 5.8
PlanExec 32.7 16.1 11.0 3.6
FullCodeRefl 25.6 19.3 12.5 7.2
HyperAgent 45.3 28.6 23.1 10.1
Llama-3-70B-Instruct
ReAct 20.8 8.9 3.4 0
PlanExec 8.9 1.8 2.4 0.7
FullCodeRefl 24.4 17.9 7.0 4.3
HyperAgent 30.1 19.7 8.9 6.4
Table 2: Performance comparison on AppWorld under dif-
ferent agent optimization methods.
Approach Test-N Test-C
TGC SGC TGC SGC
SFT
SFT-GT 6.2 1.8 0.8 0.1
RFT 47.9 26.4 26.4 11.4
EI 58.3 36.8 32.8 17.6
DPO DPO-MCTS 57.0 31.8 31.8 13.7 DMPO 59.0 36.6 36.3 13.7
RL
PPO (critic, token) 50.8 28.9 26.4 10.5
RLOO (traj) 57.2 35.7 36.7 17.4
GRPO (token) 58.0 36.8 39.5 22.4
LOOP (bandit) 53.3 33.6 27.7 13.0
LOOP (turn) 64.1 43.5 40.8 26.5
LOOP (token)71.3 53.6 45.7 26.6
NFT
ReAct 48.8 32.1 30.2 13.0
PlanExec 63.1 52.6 35.7 18.9
Traj(SsetBSR+Snippet) 65.8 53.6 38.7 24.8
HyperAgent 67.1 55.9 40.2 26.1
ments the agent with few-shot trajectory demonstrations be-
fore the test task and inserts a state-matched snippet into the
context before each action decision.
Agent Implementation
We use GPT-4o as the backbone for all LLM-based com-
ponents in the main experiments, including hypergraph con-
struction, task interpretation, semantic DAG planning and
refinement, support-graph selection, and ReAct-Code exe-
cution. Tool context extraction, Deficit-Oriented Expansion,
and runtime binding validation are implemented as deter-
ministic modules and do not invoke the LLM unless seman-
tic ambiguity remains. Each task is executed in a freshly ini-
tialized AppWorld environment with a persistent restricted
Python REPL, allowing intermediate variables and tool out-
puts to be reused across subgoals. The prompt templates for
the Planner, Refiner, and Executor, together with their de-
coding configurations, are provided in Appendix A. We also
vary the LLM backbone, using GPT-4–Turbo and Llama-

(a) Interaction and token efficiency
0.00 0.25 0.50 0.75 1.00
LLM turns
(Test-N)
14.6
7.2
Executable
API calls (Test-N)
75.1
48.0
Total tokens
(Test-N)
140k
46k
LLM turns
(Test-C)
22.0
10.5
Executable
API calls (Test-C)
123.1
57.0
Total tokens
(Test-C)
180k
68k
Relative resource use (ReAct = 1.0, lower is better)
ReAct HyperAgent
(b) Representative rollout
Task: Send a Venmo reminder for payment requests to my roommates
that have been pending for at least 30 days.
ReAct HyperAgent
CALL supervisor.show_profile;
show_account_passwords
DOC api_docs.search_api_docs x 3;
show_api_descriptions
CALL supervisor.show_account_passwords;
show_profile
CALL venmo.login; api_docs.show_api_doc x 3
CALL supervisor.show_profile;
show_account_passwords
CALL venmo.login; api_docs.show_api_doc x 2
CALL venmo.show_sent_payment_requests x 2
BAD venmo.remind_payment_request x 15 (all old
requests)
FAIL supervisor.complete_task (partial)
CALL supervisor.show_profile
CALL supervisor.show_account_passwords
CALL venmo.login
CALL venmo.show_sent_payment_requests
CALL phone.login
CALL phone.search_contacts
CALL venmo.remind_payment_request x 7 (matched
roommates)
DONE supervisor.complete_task (success)
Figure 2: Tool call and token usage for HyperAgent.
3–70B–Instruct, to evaluate HyperAgent against other agent
frameworks.
Main Results
RQ1: Does HyperAgent improve end-to-end task perfor-
mance. First, we compare HyperAgent with methods from
the SFT, DPO, RL, and NFT paradigms. All SFT, DPO, and
RL baselines are trained with the Qwen-2.5-32B LLM back-
bone, whereas the NFT methods are based on GPT-4o. As
shown in Table 2, by using a more comprehensive plan-
ning context and detailed schema-level Tool Support Sub-
graphs, HyperAgent outperforms the other NFT methods
and is competitive with trained agents. Second, we compare
HyperAgent with different agent scaffolds. From Table 1,
we observe that, with schema-level dependencies, HyperA-
gent consistently outperforms ReAct, PlanExec, and Full-
CodeRefl across the evaluated LLM backbones.
RQ2: Does HyperAgent reduce tool-document and to-
tal costs. We compare HyperAgent with ReAct in terms
of LLM interaction turns, API calls, and total token con-
sumption on Test-Normal and Test-Challenge. As shown in
Fig. 2, HyperAgent consistently reduces costs on both types
of tasks. We further present a representative execution roll-
out (with additional examples in the Appendix D), from
which we observe that ReAct repeatedly explores API doc-
umentation and retries actions before resolving the neces-
sary constraints, whereas HyperAgent follows dependency-
grounded tool sequences to accomplish planned subgoals,
such as retrieving roommates’ contact information, identify-
ing matching payment requests, and issuing reminders. With
the TSH, HyperAgent constructs prerequisite-complete sup-
port paths for individual subgoals, reducing costly online ex-
ploration over the action space.
Ablation Study
RQ3: Are the main components of HyperAgent essen-
tial and effective. First, we compare HyperAgent with two
variants. InVariant 1, we remove the retrieved graph con-
text, including tool-schema dependencies, and retain only
simplified tool descriptions during DAG planning and re-
finement. InVariant 2, we remove the Tool Support Sub-
graphs for each subtask and use the top-Ktools with the
highest semantic similarity to the subgoal. As shown in Fig-
ure 3, HyperAgent achieves higher task performance while
using fewer tokens and API calls. Removing either com-
ponent consistently degrades end-to-end task performance
on both Test-N and Test-C. This trend suggests that graph
context and tool support graphs reduce redundant tool ex-
ploration by exposing schema-level relations across tools.
Moreover, HyperAgent can construct more complete execu-
tion paths and avoid semantically related but operationally
unsuitable tools, leading to fewer API invocations and less
exploration. Second, we study the impact of the hop count
in the Tool Context Graph and the top-Ksupport parame-
ter used in support-graph expansion, as shown in Figure 4.
Increasing the hop count from 1 to 2 and the top-Kvalue
from 1 to 3 improves both TGC and SGC by recovering
more valid prerequisite paths. However, further expansion
provides negligible gains while substantially increasing to-
ken consumption due to additional irrelevant tools and de-
pendencies.
More Experiments
RQ4: Does HyperAgent construct a compact tool con-
text that preserves the gold tools. To evaluate the effec-
tiveness of the proposed Tool Context Graphs, we extract
task-level gold tool sets from the official AppWorld solu-
tions and compare HyperAgent with semantic top-Ktool
retrieval and In-N-Out graph retrieval under the same con-
text budget of 20 tools. Based on the results in Figure 5,
HyperAgent significantly outperforms In-N-Out and seman-
tic retrieval. This result indicates that, with schema-node
anchoring and dependency-guided expansion, the extracted
tool context recovers implicit prerequisite tools that are not
directly aligned with the task semantics, thereby providing a

w/o Graph Context
w/o Tool Support Graph
HyperAgent
0
15
30
45
60
75
Score (%)
56.0 54.6
67.1
Test-N
TGC
44.2
41.8
55.9
Test-N
SGC
28.5 26.9
40.2
Test-C
TGC
11.6 9.9
26.1
Test-C
SGC
(a) Task Performance.
w/o Graph Context
w/o Tool Support Graph
HyperAgent
0
30
60
90
120
Tokens per task (K)
61.8K
68.4K
46.0K
Test-N
89.7K
101.2K
68.0K
Test-C (b) Token Usage.
w/o Graph Context
w/o Tool Support Graph
HyperAgent
0
20
40
60
80
100
Calls per task 56.5
63.1
48.0
Test-N
75.8
84.7
57.0
Test-C (c) API Calls.
Figure 3: Ablation study with two variants.
(a) Task performance
0
10
20
30
40
50
Task score (%)
1-hop 2-hop 3-hop
Expansion depth H
Top-1 Top-3 Top-5
Frontier Top-K
36.3
40.2 39.4 37.1 40.2 40.4
21.8
26.1 25.0 22.6 26.1 25.9
Test-C TGC Test-C SGC
(a) Task Performance.
(b) Token cost
0
20
40
60
80
100
Tokens per task (K)
1-hop 2-hop 3-hop
Expansion depth H
Top-1 Top-3 Top-5
Frontier Top-K
56.3K
68.0K
87.5K
60.2K
68.0K
78.6K
Test-C tokens
(b) Token Usage.
Figure 4: Key hyperparameter analysis in HyperAgent.
reliable planning and execution space for task completion.
RQ5: Can HyperAgent Propose Better Tool-Use Se-
quences under Dynamical States. We evaluate the con-
structed tool support graphs by examining whether they im-
prove subgoal completion while reducing LLM calls. We
compare HyperAgent with ReAct using semantic Top–K re-
trieval under the same tool budget. For a fair comparison,
both methods operate on the same frozen set of subgoals.
Before executing either method, we manually annotate com-
pletion contracts for a predefined subset of subgoals, spec-
ifying their expected effects and outputs. A subgoal is con-
sidered completed only when its contract is supported by
runtime observations or verified changes to the environ-
ment. Based on the results in Figure 6, HyperAgent achieves
a higher subgoal completion rate while reducing the aver-
age number of LLM calls per subgoal. This result suggests
that the state-conditioned support graphs expose prerequisite
tools and intermediate schemas before execution, thereby
reducing trial-and-error tool selection and repeated explo-
ration relative to the baseline.
Gold tool
recall
Full-coverage
rate
0.0
0.2
0.4
0.6
0.8
1.0Rate
90
70
Semantic Retrieval In-N-Out HyperAgent
Figure 5: Quality evaluation of HyperAgent.
2 3 4 5
Average LLM calls per subgoal  ↓
60
65
70
75
80
Subgoal completion rate (%)  ↑
+10 pp completion
-2.7 LLM calls
ReAct
64%  |  5.2 calls
HyperAgent
74%  |  2.5 calls
Figure 6: Subgoal completion rate under dynamic states.
Conclusion
In this paper, we present HyperAgent, a Tool-Schema
Hypergraph-guided framework for dynamic tool-use plan-
ning with LLM agents. We extract schema-level dependen-
cies among tools and represent the available tool space as
a directed Tool-Schema Hypergraph. Given a task, HyperA-
gent retrieves a task-relevant Tool Context Graph that pre-
serves schema-level dependencies and guides the decom-
position of the task into a fine-grained Task DAG. During
execution, we further introduce deficit-based support graph
expansion to construct a state-conditioned and structurally
grounded tool composition for each subtask. Experiments
on AppWorld demonstrate that HyperAgent improves task
completion while reducing redundant API calls, LLM inter-
actions, and token consumption compared with the selected
baselines. These findings suggest that explicitly modeling
tool dependencies can complement the semantic reasoning
capabilities of LLMs, enabling more reliable and efficient
tool-use planning under dynamically changing agent states.

References
Ahmadian, A.; Cremer, C.; Gall´e, M.; Fadaee, M.; Kreutzer,
J.; Pietquin, O.; ¨Ust¨un, A.; and Hooker, S. 2024. Back to Ba-
sics: Revisiting REINFORCE Style Optimization for Learn-
ing from Human Feedback in LLMs. arXiv:2402.14740.
Antelmi, A.; Cordasco, G.; Polato, M.; Scarano, V .; Spag-
nuolo, C.; and Yang, D. 2023. A Survey on Hypergraph
Representation Learning.ACM Comput. Surv., 56(1).
Anthony, T. W.; Tian, Z.; and Barber, D. 2017. Thinking Fast
and Slow with Deep Learning and Tree Search. InNeural
Information Processing Systems.
Bei, Y .; Zhang, W.; Wang, S.; Chen, W.; Zhou, S.; Chen, H.;
Li, Y .; Bu, J.; Pan, S.; Yu, Y .; King, I.; Karray, F.; and Yu,
P. S. 2025. Graphs Meet AI Agents: Taxonomy, Progress,
and Future Opportunities. arXiv:2506.18019.
Chen, K.; Cusumano-Towner, M.; Huval, B.; Petrenko, A.;
Hamburger, J.; Koltun, V .; and Krahenbuhl, P. 2025a. Re-
inforcement Learning for Long-Horizon Interactive LLM
Agents.ArXiv, abs/2502.01600.
Chen, W.; Li, W.; Yao, D.; Meng, X.; Gong, C.; and Bi, J.
2025b. GTool: Graph Enhanced Tool Planning with Large
Language Model.ArXiv, abs/2508.12725.
Chen, W.; Yao, D.; Li, W.; Meng, X.; Gong, C.; and Bi, J.
2026. GTool: Graph Enhanced Tool Planning with Large
Language Model. InThe Fourteenth International Confer-
ence on Learning Representations.
Dong, Y .; Zhu, X.; Pan, Z.; Zhu, L.; and Yang, Y . 2024.
VillagerAgent: A Graph-Based Multi-Agent Framework for
Coordinating Complex Task Dependencies in Minecraft. In
Annual Meeting of the Association for Computational Lin-
guistics.
Erdogan, L. E.; Furuta, H.; Kim, S.; Lee, N.; Moon, S.; Anu-
manchipalli, G.; Keutzer, K.; and Gholami, A. 2025. Plan-
and-Act: Improving Planning of Agents for Long-Horizon
Tasks. InForty-second International Conference on Ma-
chine Learning.
Gupta, S.; Singh, S.; Sabharwal, A.; Khot, T.; and Bogin, B.
2025. Leveraging In-Context Learning for Language Model
Agents.ArXiv, abs/2506.13109.
Kim, J.; Rhee, S.; Kim, M.; Kim, D.; Lee, S.; Sung, Y .; and
Jung, K. 2025. ReflAct: World-Grounded Decision Making
in LLM Agents via Goal-State Reflection. InConference on
Empirical Methods in Natural Language Processing.
Lee, S.; Kim, N.; and Jo, Y . 2025. In-N-Out: A Parameter-
Level API Graph Dataset for Tool Agents.ArXiv,
abs/2509.01560.
Liu, X.; Peng, Z.; Yi, X.; Xie, X.; Xiang, L.; Liu, Y .; and
Xu, D. 2024a. ToolNet: Connecting Large Language Models
with Massive Tools via Tool Graph. arXiv:2403.00839.
Liu, Z.; Lai, Z.; Gao, Z.; Cui, E.; Li, Z.; Zhu, X.; Lu, L.;
Chen, Q.; Qiao, Y .; Dai, J.; and Wang, W. 2024b. Con-
trolLLM: Augment Language Models with Tools by Search-
ing on Graphs. InComputer Vision – ECCV 2024, 89–105.
Springer.
Lumer, E.; Basavaraju, P. H.; Mason, M.; Burke, J. A.; and
Subbiah, V . K. 2025. Graph RAG-Tool Fusion.ArXiv,
abs/2502.07223.
OpenAI. 2023. GPT-4 Technical Report.
Paranjape, B.; Lundberg, S.; Singh, S.; Hajishirzi, H.; Zettle-
moyer, L.; and Ribeiro, M. T. 2023. ART: Automatic
multi-step reasoning and tool-use for large language mod-
els. arXiv:2303.09014.
Patel, B.; Belli, D.; Jalalirad, A.; Arnold, M.; Ermolov, A.;
and Major, B. 2026. Dynamic Tool Dependency Retrieval
for Lightweight Function Calling. In Liakata, M.; Moreira,
V . P.; Zhang, J.; and Jurgens, D., eds.,Findings of the As-
sociation for Computational Linguistics: ACL 2026, 33649–
33672. San Diego, California, United States: Association for
Computational Linguistics. ISBN 979-8-89176-395-1.
Patil, S. G.; Zhang, T.; Wang, X.; and Gonzalez, J. E. 2023.
Gorilla: Large Language Model Connected with Massive
APIs.ArXiv, abs/2305.15334.
Putta, P.; Mills, E.; Garg, N.; Motwani, S. R.; Finn, C.;
Garg, D.; and Rafailov, R. 2024. Agent Q: Advanced Rea-
soning and Learning for Autonomous AI Agents.ArXiv,
abs/2408.07199.
Qin, Y .; Liang, S.; Ye, Y .; Zhu, K.; Yan, L.; Lu, Y .-T.; Lin,
Y .; Cong, X.; Tang, X.; Qian, B.; Zhao, S.; Tian, R.; Xie, R.;
Zhou, J.; Gerstein, M. H.; Li, D.; Liu, Z.; and Sun, M. 2023.
ToolLLM: Facilitating Large Language Models to Master
16000+ Real-world APIs.ArXiv, abs/2307.16789.
Schulman, J.; Wolski, F.; Dhariwal, P.; Radford, A.; and
Klimov, O. 2017. Proximal Policy Optimization Algorithms.
ArXiv, abs/1707.06347.
Shao, Z.; Wang, P.; Zhu, Q.; Xu, R.; Song, J.-M.; Zhang, M.;
Li, Y . K.; Wu, Y .; and Guo, D. 2024. DeepSeekMath: Push-
ing the Limits of Mathematical Reasoning in Open Lan-
guage Models.ArXiv, abs/2402.03300.
Shi, W.; Yuan, M.; Wu, J.; Wang, Q.; and Feng, F. 2024.
Direct Multi-Turn Preference Optimization for Language
Agents.ArXiv, abs/2406.14868.
Sun, S.; Liu, Y .; Wang, S.; Zhu, C.; and Iyyer, M.
2023. PEARL: Prompting Large Language Models to
Plan and Execute Actions Over Long Documents.ArXiv,
abs/2305.14564.
Trivedi, H.; Khot, T.; Hartmann, M.; Manku, R. R.; Dong,
V .; Li, E.; Gupta, S.; Sabharwal, A.; and Balasubramanian,
N. 2024. AppWorld: A Controllable World of Apps and Peo-
ple for Benchmarking Interactive Coding Agents.ArXiv,
abs/2407.18901.
Wu, X.; Shen, Y .; Shan, C.; Song, K.; Wang, S.; Zhang,
B.; Feng, J.; Cheng, H.; Chen, W.; Xiong, Y .; and Li, D.
2024. Can Graph Learning Improve Planning in LLM-based
Agents?Advances in Neural Information Processing Sys-
tems 37.
Yang, Q. A.; Yang, B.; Zhang, B.; Hui, B.; Zheng, B.; Yu,
B.; Li, C.; Liu, D.; Huang, F.; Dong, G.; Wei, H.; Lin, H.;
Yang, J.; Tu, J.; Zhang, J.; Yang, J.; Yang, J.; Zhou, J.; Lin,
J.; Dang, K.; Lu, K.; Bao, K.; Yang, K.; Yu, L.; Li, M.; Xue,
M.; Zhang, P.; Zhu, Q.; Men, R.; Lin, R.; Li, T.; Xia, T.; Ren,

X.; Ren, X.; Fan, Y .; Su, Y .; Zhang, Y .-C.; Wan, Y .; Liu, Y .;
Cui, Z.; Zhang, Z.; Qiu, Z.; Quan, S.; and Wang, Z. 2024.
Qwen2.5 Technical Report.ArXiv, abs/2412.15115.
Yang, Y .; Chai, H.; Shao, S.; Song, Y .; Qi, S.; Rui, R.; and
Zhang, W. 2025. AgentNet: Decentralized Evolutionary Co-
ordination for LLM-based Multi-Agent Systems.ArXiv,
abs/2504.00587.
Yang, Z.; Li, L.; Wang, J.; Lin, K.; Azarnasab, E.; Ahmed,
F.; Liu, Z.; Liu, C.; Zeng, M.; and Wang, L. 2023. MM-
REACT: Prompting ChatGPT for Multimodal Reasoning
and Action.ArXiv, abs/2303.11381.
Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan,
K.; and Cao, Y . 2022. ReAct: Synergizing Reasoning and
Acting in Language Models.ArXiv, abs/2210.03629.
Yu, J.; Ding, Y .; and Sato, H. 2025. DynTaskMAS: A
Dynamic Task Graph-driven Framework for Asynchronous
and Parallel LLM-based Multi-Agent Systems.ArXiv,
abs/2503.07675.
Yuan, Z.; Yuan, H.; Li, C.; Dong, G.; Tan, C.; and Zhou,
C. 2023. Scaling Relationship on Learning Mathemat-
ical Reasoning with Large Language Models.ArXiv,
abs/2308.01825.
Zhang, S.; Ma, X.; Cao, Z.; Zhang, Z.; and Zhao, H. 2025.
Plan-over-Graph: Towards Parallelable LLM Agent Sched-
ule.ArXiv, abs/2502.14563.
Zhuang, Y .; Chen, X.; Yu, T.; Mitra, S.; Bursztyn, V .; Rossi,
R. A.; Sarkhel, S.; and Zhang, C. 2024. ToolChain*: Effi-
cient Action Space Navigation in Large Language Models
with A* Search. InThe Twelfth International Conference on
Learning Representations.
