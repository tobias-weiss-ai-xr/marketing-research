---
title: Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination
url: https://arxiv.org/abs/2609.31963
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Ben Rachmut
- Ning Zhang
- Yevgeniy Vorobeychik
- William Yeoh
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.31963
pages: 19
chars: 49311
fetched_at: '2026-11-08T13:34:29+00:00'
kb_version: 1
---

# Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination

Symbolic Guidance for LLM Agents in
Distributed Multiagent Coordination ⋆
Ben Rachmut, Ning Zhang, Yevgeniy Vorobeychik, and William Yeoh
Washington University in St. Louis, Saint Louis, MO, United States
{benr, zhang.ning, yvorobeychik, wyeoh}@wustl.edu
Abstract.Large language models (LLMs) are increasingly deployed as
autonomous agents within multi-agent systems. Yet, their capacity to
execute distributed coordination protocols remains poorly understood.
Recently, researchers introduced AgentsNet, a framework that enables
LLM agents to coordinate in a distributed manner to solve a range
of multi-agent coordination problems. However, because this approach
grants agents full flexibility in reasoning about their coordination strate-
gies,itoftenyieldsinconsistentorpoorperformance,particularlyinmore
complex domains.
In this paper, we hypothesize that LLM agents can achieve better coordi-
nation when provided with symbolic guidance derived from established
symbolic algorithms. To test this hypothesis, we systematically evalu-
ate how different forms of guidance influence performance across three
canonical distributed graph-based problems – graph coloring, matching,
and vertex cover. For each problem, we examine two variants: A sim-
pler one where feasible solutions can be found using local, agent-based
heuristics,andamorecomplexonewhereoptimalsolutionsrequireglobal
coordination.
To structure this investigation, we introduce theSymbolic Guidance Tax-
onomy (SGT), which defines a spectrum of guidance ranging from the
AgentsNet baseline – using only freeform natural-language task descrip-
tions with no explicit guidance – at one end, to complete algorithmic
specifications at the other, with intermediate levels incorporating par-
tial pseudocode. Our results reveal that intermediate guidance levels are
most effective: Partial pseudocode guidance consistently outperforms the
unguided AgentsNet baseline. Moreover, both the choice of model and
source of symbolic guidance play important roles. Gemini agents gen-
erally achieve the best overall performance; Llama agents often benefit
from guidance; whereas Qwen agents tend to be largely insensitive to it.
Similarly,guidancederivedfromlocalheuristicalgorithmsprovesbroadly
robust, while guidance from complex global search algorithms tends to
be less effective. Collectively, these findings offer design principles for
balancing symbolic structure and LLM adaptability in distributed multi-
agent coordination.
Keywords:Large Language Models·Multiagent Systems·Distributed
Coordination·Symbolic Guidance·Adjustable Autonomy
⋆ A preliminary version of this work was published as an extended abstract at AAMAS
2026 [28].
arXiv:2609.31963v2  [cs.AI]  22 Oct 2026

2 B. Rachmut et al.
1 Introduction
Coordinating multiple autonomous agents to achieve a common objective is a
long-standing and fundamental challenge in AI. Whether in scheduling meet-
ings [19], deploying multi-robot teams [27], managing smart homes and smart
grids [21,10,29], or controlling satellite constellations [36], the core difficulty lies
in ensuring that coherent global behavior emerges from local decisions made un-
der limited information and communication. Such multiagent coordination prob-
lems are inherently complex and computationally demanding, requiring agents to
reason about both their own actions and those of others in dynamic, distributed
environments.
Over the past several decades, symbolic approaches have provided elegant
solutions to these problems. Distributed algorithms, many of which were pro-
posed by the AAMAS community [23,4,22,7], have enabled agents to coordinate
through rigorously defined message-passing and optimization procedures, often
with formal guarantees of correctness and convergence. However, these symbolic
solvers depend on complete and well-specified problem formulations, making
them fragile when the environment or objectives are uncertain, underspecified,
or expressed informally.
In parallel, the recent emergence of agentic AI systems, that is, large language
models (LLMs) acting as autonomous agents, has opened a new frontier for
multiagent coordination [24,32,11]. LLM agents can interpret instructions and
interact in natural language, making them robust to incomplete, ambiguous,
or imprecise specifications. Yet, when deployed off the shelf, they struggle to
coordinate reliably, particularly in domains where global coherence must arise
from local interactions [11]. In contrast to symbolic algorithms, LLM agents lack
built-in mechanisms to ensure consistency, convergence, or optimality.
This contrast exposes a core tradeoff between the two paradigms. Symbolic
solvers offer theoretical rigor and reliability but limited flexibility, whereas LLM
agents provide linguistic adaptability and robustness but lack structure for con-
sistent coordination. Bridging this gap requires combining the complementary
strengths of both.
To this end, we propose integrating symbolic guidance into LLM-based mul-
tiagent systems and systematically studying its effects. Specifically, we introduce
theSymbolic Guidance Taxonomy (SGT): A principled framework that charac-
terizes different levels and forms of symbolic scaffolding for LLM agents. Inspired
by ideas from adjustable autonomy [31,30], SGT positions LLM agents along an
autonomy spectrum: From fully open-ended reasoning (maximal autonomy), to
strict algorithmic adherence (minimal autonomy). This taxonomy provides a
unified lens for understanding how symbolic structure can guide agentic reason-
ing, revealing when and how symbolic scaffolding enhances coordination perfor-
mance.
Building on this analogy, we use SGT not only as a conceptual lens but also as
the basis for our evaluation methodology. Specifically, we instantiate benchmark
graph-based coordination problems – graph coloring, matching, and vertex cover
– each encompassing both local and global objectives. Local objectives (e.g., col-

Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination 3
oring with∆+ 1colors, where∆is the graph’s maximum degree; maximal
matching; minimal vertex cover) capture feasible but suboptimal coordination
under partial information, whereas global objectives (e.g., 3-coloring, maximum
matching, minimum vertex cover) impose stronger optimality requirements. Our
experimental setup systematically factors both algorithmic structure (e.g., local
agent-based heuristics versus global distributed search procedures) and symbolic
guidance levels as defined by SGT, enabling direct comparison across LLM fam-
ilies, task types, and autonomy regimes.
Our results show that symbolic guidance profoundly shapes coordination out-
comes: Structured scaffolding significantly improves coherence and stability on
harder global objectives, while excessive prescriptiveness can reduce adaptability
in simpler tasks. These findings highlight that the balance between symbolic con-
trol and LLM autonomy is neither binary nor monotonic, but context-dependent,
mirroring the broader principle of adjustable autonomy in human-agent collab-
oration.
In summary, our key contributions are as follows:
1.The Symbolic Guidance Taxonomy (SGT):A principled framework for
structuring guidance strategies in multi-agent LLMs, inspired by adjustable
autonomy and formalized in terms of algorithmic selections and representa-
tional encodings.
2.A unified evaluation frameworkthat systematically combines bench-
mark distributed graph problems, controllable difficulty levels (local vs.
global objectives), and structured variation in symbolic guidance.
3.Ananalysisofalgorithm-guidanceinteractionsthatdisentangleswhen
LLMs benefit from symbolic structure versus when open-ended reasoning
yields superior adaptability.
4.Empirical design principlesfor balancing symbolic control and LLM flex-
ibility, providing actionable insights for deploying multiagent LLM systems
in real-world distributed environments.
2 Background
Distributed coordination problems are naturally formalized as graphs, where
each agent corresponds to a vertex and communicates through message exchange
with its neighboring vertices. The central challenge lies in ensuring that these
locally informed decisions collectively produce a globally consistent outcome.
To systematically examine this challenge, we first describe the three canonical
benchmarkdomainsthatisthefocusofthispaper:Graph coloring,matching,and
vertex cover. We then contrast two classical algorithmic paradigms:Local agent-
based heuristics, which emphasize scalability and decentralized decision-making,
andglobal distributed search procedures, which provide stronger guarantees of
optimality but demand greater coordination and communication overhead. We
describe a representative algorithm from each of the two paradigms that we use
in this paper.

4 B. Rachmut et al.
2.1 Benchmark Domains and Variants
We now describe the three canonical benchmark domains that we use in this
paper: Graph coloring, matching, and vertex cover. For each of these domains,
we describe alocal variant, where neighborhood information is sufficient to solve
the problem, and aglobal variant, where consistency must be enforced across
the entire network [26].
Graph Coloring:In graph coloring, each agent must choose a color distinct
from its neighbors. If the palette has(∆+ 1)colors, where∆is the maximum
degree, every agent can resolve conflicts locally [17]. This is thelocalvariant. But
with only three colors, local choices no longer suffice: Agents must coordinate
globallyto avoid contradictions [5].
Matching:In matching, each agent must decide whether to form a pair with
one of its neighbors. Stopping once no more pairs can be added yields amaximal
matching,whichcanbeobtainedthroughonlylocalagreements[13].Bycontrast,
findingamaximum matching,thatis,pairingasmanyagentsaspossible,requires
globalcoordination across the whole network [2].
Vertex Cover:In vertex cover, agents must decide who takes responsibility for
covering their incident edges. A cover isminimalif every selected agent is essen-
tial, that is, removing any one of them would leave some edge uncovered [17].
This corresponds to thelocalvariant. In contrast, finding aminimumcover,
where the number of selected agents is as small as possible, requires balancing
responsibilitiesgloballyacross the network [25].
2.2 Algorithmic Approaches
We now describe a representative algorithm from the two contrasting algorith-
mic paradigms for distributed problems:Local agent-based heuristicsandglobal
distributed search procedures.
Local Agent-based Heuristics:We use theMaximal Independent Set (MIS)
heuristic, a cornerstone of distributed graph algorithms [18,1,17,15], as a rep-
resentative approach from this category. An MIS is a set of vertices with no two
adjacent, such that no additional vertex can be added without breaking inde-
pendence. It can be computed using only local neighborhood information: Each
vertex joins the set if none of its higher-priority neighbors has already done so.
This simple ordering principle extends naturally across our three domains: In
graph coloring, vertices commit to colors once higher-priority neighbors have
chosen; in matching, two vertices form a pair only if neither has already com-
mitted to another neighbor; and in vertex cover, priorities resolve redundancy so
that higher-priority vertices remain in the cover, ensuring every edge is covered.
These MIS-based rules admit efficient distributed algorithms running inO(logn)
rounds, wherenis the number of nodes in the graph [17,1].

Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination 5
Global Distributed Search Procedures:We useDistributed Depth-First
Search (DFS)as a representative algorithm from this category. Distributed DFS
enforces a strict global order: Agents are considered sequentially, and tentative
choices are undone whenever conflicts arise. This guarantees optimality: Color-
ings are extended until a consistent assignment is found, matchings are branched
on until the maximum is recovered, and vertex covers are explored until a min-
imum set is identified. The same approach is also referred to asbacktracking
searchin the literature on distributed constraint satisfaction problems, where
agents cooperatively assign values to variables subject to global satisfaction con-
straints [34]. However, such exhaustive search requires a runtime ofO(bn), where
bis the branching factor for each agent (e.g., number of possible colors in graph
coloring) andnis the number of agents in the problem. Due to the exponen-
tial complexity, such approaches may be impractical for large-scale distributed
coordination.
3 Related Work
Researchers have recently explore whether LLMs can coordinate effectively when
deployed as interacting agents.AgentsNetintroduced the first systematic bench-
mark for LLM-based multi-agent coordination, evaluating problems such as
(∆+ 1)-coloring, maximal matching, minimal vertex cover, leader election, and
consensus under synchronous message passing [11]. The framework spans a wide
range of models, network topologies, and scales, and highlights clear variation in
task difficulty: While some problems like consensus and leader election are solved
reliably, others such as coloring and vertex cover remain challenging. Crucially,
AgentsNet leaves the design of solution strategies entirely to the LLMs, provid-
ing only the problem description and communication channel. This makes it a
solid foundation for benchmarking open-ended coordination. Our work builds
on this platform, but shifts the focus to controlled analysis by systematically
varying the form of symbolic guidance and extending the tasks to harder global
variants (e.g., 3-coloring, maximum matching, minimum vertex cover).
Another recent development is the introduction ofVL-DCOPs, which ex-
tend Distributed Constraint Optimization Problems (DCOPs) to a spectrum of
agent types that integrate symbolic and neural components [20]. A DCOP [22]
models coordination as a set of agents, each controlling one or more variables
whose value assignments jointly determine the costs of shared constraints. The
objective is for the agents to coordinate their assignments so as to minimize the
total constraint cost across the network. In the VL-DCOP framework, this co-
ordination spectrum ranges from fully symbolic agents, which execute classical
distributed algorithms, to fully neural agents, which rely entirely on LLM-based
reasoning. Hybrid variants position LLMs in supporting roles, such as interpret-
ing human instructions, generating constraint models, or resolving uncertainty,
while symbolic solvers retain decision-making authority. This notion of hybrid-
ity differs from ours: in VL-DCOPs, hybridity arises from combining humans,

6 B. Rachmut et al.
symbolic solvers, and LLMs, whereas in our work, it emerges from varying the
degree of symbolic guidance provided to LLM agents themselves.
More broadly, both VL-DCOPs and our approach touch on a long-standing
question in multi-agent systems: How much decision-making power should re-
side with individual agents versus external controllers? The field ofadjustable
autonomy (AA)emerged to address precisely this issue, proposing that agents
dynamically shift control depending on context [8,14,31]. For example, in a
scheduling domain, an agent might act autonomously under routine conditions,
but transfer control to a human when uncertainty is high or when coordination
failures would be costly [9,12].
Early approaches often treated autonomy as binary: Either the agent acted
independently or it fully delegated to another entity. Recognizing these short-
comings, researchers introduced the notion oftransfer-of-control strategies[30,
31]. These strategies consist of conditional sequences: Agents may attempt an
autonomous decision, fall back to external input if needed, and adjust coor-
dination constraints to reduce miscoordination costs. This work demonstrated
thatintermediate strategies, rather than rigid extremes, best preserve both lo-
cal decision quality and global team coherence. In the next section, we adapt
the principle of adjustable autonomy into a taxonomy of guidance strategies for
LLM-based agents, treating different forms of symbolic instruction as varying
degrees of autonomy.
4 Symbolic Guidance Taxonomy
LLMs can be guided in different ways when solving distributed coordination
problems: From being left entirely to their own devices to being constrained by
precisesymbolicinstructions.TheSymbolic Guidance Taxonomy (SGT)provides
a unified framework for describing this design space. It specifies how much of a
reference algorithmAis revealed to agents and in what representational form,
thereby defining different points along a spectrum of autonomy. In what follows,
we introduce the formal definition of SGT, describe the resulting agent types
that instantiate different autonomy levels, and illustrate the taxonomy through
a working example.
4.1 Formal Definition
TheSymbolic Guidance Taxonomy (SGT)is a framework for varying which
components of a symbolic algorithm are revealed to agents and how they are ex-
pressed. AgentsNet [11] provided all agents with the sametask descriptionand
output requirement, leaving the solution strategy entirely to the LLM agents.
Building on this foundation, SGT extends the design space by systematically
varying the symbolic structure provided to agents while keeping the task descrip-
tion and output requirement fixed. Specifically, SGT parameterizes the output
guidance based on two components: (1) Which parts of an algorithmic descrip-
tion are made available to agents, and (2) The form in which these elements are
conveyed.

Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination 7
Formally, letAdenote a symbolic algorithm for solving a given distributed
multiagent coordination problem. A guidance strategy is defined as a mapping:
G(S, E;A)7→ I, whereS⊆ AandEtogether determine the additional
guidanceIprovided to each agent. In more detail:
–S(selection) specifies which parts of the algorithm are supplied, such as a
step sequence, a function set, or tie-breaking rules.
–E(encoding) specifies how the selected parts are represented, for example as
pseudocode, or natural-language descriptions. The encoding is chosen from:
E∈ {main-pseudocode,function-pseudocode,
function-description,full-pseudocode},
–Idenotes the resultingguidance blockreceived by the agent.
4.2 Autonomy Spectrum of Agent Types
This framing connects directly to the principle ofadjustable autonomy[30,31].
At one extreme, autonomy is maximized: The LLM agent must devise its own
procedure without any symbolic guidance. At the other, autonomy is minimized:
The LLM agent is asked to execute a fixed protocol with no freedom to deviate.
Beyondtheseboundsliesapurelyalgorithmicbaseline,whereautonomyvanishes
entirely as the symbolic procedure is executed directly without involving an
LLM. Between these extremes, the different guidance strategies are analogous
totransfer-of-control mechanismsin adjustable autonomy: Different levels of
symbolicscaffoldingareintroducedtoreducemiscoordinationwhilestillallowing
the LLM flexibility to fill in missing details.
The agent types we define in SGT instantiate this spectrum, ranging from
Freeform agents at the high-autonomy end to the Code agent baseline at the no-
autonomy end. Each corresponds to a specific(S, E)combination, as illustrated
in Figure 1. The five agent types in SGT, corresponding to the five encodingE
options, as well as two additional baselines are as follows:
– (Baseline) AgentsNet agent.No guidance is supplied or, equivalently,
G(∅,∅;A) =∅. Agents see only the task description and output require-
ment, and must devise their own procedure. This corresponds to the baseline
setup of AgentsNet [11].
– Function-description agent.Sis the set of all auxiliary helper functions
of the algorithmA.1 Functions are described in natural language, specifying
their desired behavior, but not their implementation. Thus, the LLM agents
have full flexibility on how to implement them.
– Function-pseudocode agent.Like Function-description agents,Sis the
set of all auxiliary helper functions of the algorithmA. However, instead of
natural language descriptions, agents receive pseudocode of the functions,
effectively suggesting an implementation strategy for those functions. How-
ever, note that the LLM agents are not told how those functions should be
used to solve the problem.
1 All functions of the algorithm except for the main function.

8 B. Rachmut et al.
Fig.1: The Symbolic Guidance Taxonomy (SGT) autonomy spectrum, ranging
from maximized autonomy (AgentsNet agents) to no autonomy (Code agents).
– Main-pseudocode agent.Here,Sis the main function of the algorithmA
and the agents receive that information in the form of the pseudocode for the
function. Note that the main function may call auxiliary helper functions,
which are not provided to the LLM agents. Thus, the agents are free to
interpret and implement the auxiliary helper functions as they wish.
– Full-pseudocode agent.Sis the complete algorithmA. Agents are pro-
vided the complete pseudocode of the algorithm with all steps, function
bodies and tie-breaking rules.
– (OracleBaseline)Codeagent.Asanoraclebaselineontheotherextreme
of this spectrum, we implemented algorithmAin Python and is executed
directly by the agents without any LLM involvement.
4.3 Illustrative Example
We now illustrate the SGT using a concrete working example. ConsiderAas
a maximal independent set (MIS) variant for distributed graph coloring (see
Section 2). At a high level, the MIS-based algorithm proceeds in rounds where
agentstentativelyproposecolors,resolveconflictswithneighborsviatie-breaking
rules, and then commit to successful choices. In this example, we focus on the
proposal stepof the algorithm, during which each agent must propose a tentative
group assignment. The SGT framework highlights how this same step can take
different representational forms depending on the guidance configuration(S, E).
Here, the guidanceIprovides minimal scaffolding since it conveys a behav-
ioral intuition without specifying how to operationalize it in code or reasoning.
At the high-autonomy end, theFunction-description agentis provided with
natural language descriptions of all auxiliary helper functions that support the
algorithm. For example:“propose_group: If options remain, choose one at ran-
dom; otherwise, select the group least frequent among neighbors’ commitments.”
This guidance introduces modular decomposition while preserving linguistic am-
biguity.
In contrast, theFunction-pseudocode agentreceives the same set of aux-
iliary helper functions but encoded as explicit pseudocode. For instance:
function propose_group():
if P(me) not empty:

Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination 9
tentative <- random choice from P(me)
else:
tentative <- least frequent group among neighbors
The pseudocode uses descriptive identifiers and clear structure to minimize am-
biguity while retaining readability for LLMs.
Progressing further, theMain-pseudocode agentis given a global outline
of the main coordination procedure. Within this outline, the proposal stage ap-
pears only as a high-level directive:“Step 4: Propose a tentative group (if uncom-
mitted); if none available, select to the least frequent choice among neighbors.”
This provides the agent with global context but omits detailed implementation.
At the low-autonomy extreme, theFull-pseudocode agentreceives the
complete algorithm in pseudocode, including both the global structure and all
supporting functions. In this setting, the proposal step appears twice: Once
in the overall outline (“Step 4...”) and again in the detailed helper function
(propose_group()). The resulting specification leaves minimal room for inter-
pretation, effectively guiding the agent toward deterministic execution.
5 Experimental Design
Our experiments evaluate how different levels of symbolic guidance affect LLM
agents on distributed coordination tasks. We structure the design around five
components: The experimental simulator, the graph topologies, the algorithm
choices, the LLM models, and the evaluation metrics.
Experimental Simulator:We build on theAgentsNetbenchmark [11], us-
ing their public implementation2 for message passing and network generation.
We provide our own extended implementation,3 which adds harder global vari-
ants (3-coloring, maximum matching, minimum vertex cover) and systematically
varies symbolic guidance through the Symbolic Guidance Taxonomy (SGT).
Graph Topologies:Agents operate on three graph families generated with the
original benchmark code using NetworkX:4
–Smallworld[33]: Strong local clustering with a few random shortcuts.
–Scalefree[3]: Hub-dominated networks with power-law degree distributions.
–Delaunay[16]: Planar graphs emphasizing spatial locality.
For each topology, we generate5graphs of sizen= 16, yielding15networks.
All experiments run for2D+1synchronous message-passing rounds (whereDis
the graph diameter), ensuring each agent can indirectly reach all other agents.
We evaluate all agent types from SGT, as described in Section 4.2. Each exper-
iment uses the same number of message-passing rounds, isolating the effect of
symbolic guidance.
2 https://github.com/floriangroetschla/AgentsNet
3 https://github.com/YODA-Lab/Symbolic-Guidance-Taxonomy
4 https://networkx.org/

10 B. Rachmut et al.
Algorithm Choices:The algorithmA, whose components are provided as
guidance to the LLM agents, depend on the variant of the problem domain. For
local variants (i.e., (∆+ 1)-coloring, maximal matching, and minimal vertex
cover), we use theMaximal Independent Set (MIS) heuristic. For the global
variants (i.e., 3-coloring, maximum matching, and minimum vertex cover), we
use the MIS heuristic as well as theDistributed DFS algorithm. See Section 2.2
for more information of the two algorithms.
LLM Models:We evaluate three representative LLM models, covering both
free open-source options and a more expensive commercial system:
–Llama-3.1-8B Instruct(Meta), served locally via Ollama.
–Qwen-2.5-7B Instruct(Alibaba), also via Ollama.
–Gemini-2.5 Flash(Google DeepMind), accessed via OpenRouter. Identified
byAgentsNetas Pareto-optimal in accuracy-cost trade-offs [11].
Evaluation Metrics:We adopt a unified error metric, theSum of Squared
Error (SSE), which captures deviations from correctness or optimality. We define
them below for each of our three domains:
–Graph coloring: For a solutionx, an edge isvalidif its vertices have different
colors in the solution, andinvalidotherwise. LetV(x)andI(x)denote the
sets of valid and invalid edges in the solution, respectively, and|OP T(G)|
denote the maximum number of edges that can be properly colored in the
input graphG. Using these definitions, the SSE is defined as follows for the
two local and global variants of this problem:
•(∆+ 1)-Coloring:SSE local coloring(x) =|I(x)| 2.
•3-Coloring:SSE global coloring(x) =  |OP T(G)| − |V(x)| 2 .
–Matching: For a solutionx, letM(x) ={{u, v} ∈E|x(u) =v∧x(v) =u}
define the set of matches in the solution. An edge isvalidif it belongs to
M(x)or if at least one of its vertices is already matched via another edge
inM(x)(so the edge is indirectly covered). Otherwise it isinvalid. LetI(x)
denotes the set of invalid edges in the solution and|OP T(G)|denote the
number of a matches in an optimal solution of the problem.
•Maximal Matching:SSE local matching(x) =|I(x)| 2.
•Maximum Matching:SSE global matching(x) =  |OP T(G)| − |M(x)| 2 .
–Vertex cover: For a solutionx, a vertex isvalidif it is in the selected set and
is required to cover at least one uncovered edge (i.e., none of its neighbors are
already in the cover), andinvalidotherwise. LetV(x)andI(x)denote the
sets of valid and invalid vertices in the solution, respectively, and|OP T(G)|
denote the minimum number of vertices needed to optimally cover all edges
in the problem.
•Minimal Vertex Cover:SSE local cover(x) =|I(x)| 2.
•Minimum Vertex Cover:SSE global cover (x) =  |OP T(G)| − |V(x)| 2 +|I(x)| 2.

Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination 11
Llama-3.1 Qwen-2.5 Gemini-2.50
1
2
3
4
5
6
7
( +1)-Coloring
Llama-3.1 Qwen-2.5 Gemini-2.50
1
2
3
4
5
6
7
Maximal Matching
Llama-3.1 Qwen-2.5 Gemini-2.50
1
2
3
4
5
6
7
Minimal Vertex Cover
Mean ln(1 + SSE)
AgentsNet Function- Description Function- Pseudocode Main- Pseudocode Full- Pseudocode Code
Fig.2: Local coordination domains with MIS as algorithmA. Showing mean
ln(1 + SSE)by model. Bar colors denote agent types sorted by autonomy level;
error bars show SEM.
( +1)-Coloring
 Maximal Matching Minimal Vertex Cover
0.0
0.2
0.4
0.6
0.8
1.0Success rate
AgentsNet Function- Description Function- Pseudocode Main- Pseudocode Full- Pseudocode Code
Fig.3:LocalcoordinationdomainswithMISasalgorithmA.Showingthesuccess
rate of feasible solutions for Gemini. Bar colors denote agent types sorted by
autonomy level; error bars show SEM.
6 Experimental Results
We now describe our experimental results on the performance of the different
agent types across the SGT autonomy spectrum (see Section 4.2) and different
domain variants (see Section 2.1).
6.1 Local Coordination Problems
We first focus on the local variants of the three domains, where MIS is the
algorithmAwhose components are provided as guidance to the LLM agents.
Figure 2 shows the average error of all the five SGT agent types as well as the
two AgentsNet and Code baselines with all three LLM models across the three
domains. We make the following observations:
–In general, the Gemini agents perform better than their Llama and Qwen
counterparts, highlighting that Gemini is a better LLM for distributed graph
coordination problems. This observation is consistent with similar findings in

12 B. Rachmut et al.
Llama-3.1 Qwen-2.5 Gemini-2.50
1
2
3
4
5
6
3-Coloring
Llama-3.1 Qwen-2.5 Gemini-2.50
1
2
3
4
5
6
Maximum Matching
Llama-3.1 Qwen-2.5 Gemini-2.50
1
2
3
4
5
6
Minimum Vertex Cover
Mean ln(1 + SSE)
AgentsNet Function- Description Function- Pseudocode Main- Pseudocode Full- Pseudocode Code
Fig.4: Global coordination domains with MIS as algorithmA. Showing mean
ln(1 + SSE)by model. Bar colors denote agent types sorted by autonomy level;
error bars show SEM.
Llama-3.1 Qwen-2.5 Gemini-2.50
1
2
3
4
5
6
3-Coloring
Llama-3.1 Qwen-2.5 Gemini-2.50
1
2
3
4
5
6
Maximum Matching
Llama-3.1 Qwen-2.5 Gemini-2.50
1
2
3
4
5
6
Minimum Vertex Cover
Mean ln(1 + SSE)
AgentsNet Function- Description Function- Pseudocode Main- Pseudocode Full- Pseudocode Code
Fig.5:GlobalcoordinationdomainswithDistributedDFSasalgorithmA.Show-
ingmeanln(1+SSE)bymodel.Barcolorsdenoteagenttypessortedbyautonomy
level; error bars show SEM.
the literature for other problem types, such as open-ended natural-language
dialogue (e.g., explaining code, summarizing text, or answering creative
prompts) and multimodal academic reasoning (e.g., college-level question
answering that integrates text with images such as diagrams, charts, and
tables across multiple disciplines) [6,35].
–On whether symbolic guidance improves on the AgentsNet baseline, there
are mixed results. Specifically,
•When the agents use Llama models, all forms of guidance help with
little statistical significance differences between the different agent types.
However, they are all statistically significantly better than AgentsNet.
•When the agents use Qwen models, there is mostly no statistical differ-
ences between AgentsNet and all the different SGT agent types.
•When the agents use Gemini models, all forms of guidance help in (∆
+ 1)-coloring problems. In the maximal matching and minimal vertex
cover problems, the function-description scaffold yields a slight addi-
tional improvement. Interestingly, some agent types perform worse than

Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination 13
AgentsNet in some settings (e.g., Main- and full-pseudocode agents in
maximal matching problems), highlighting that the guidance provided
can some times do more harm than good.
Figure 3 shows the success rates5 of all the agent types with the Gemini
model only. We omitted results for the Llama and Qwen as all variants except
for the oracle Code baseline failed to solve all instances in these domains. We
make the following observations:
–As expected, the oracle Code agent achieves perfect success rates across all
three domains.
–For (∆+ 1)-coloring problems, consistent with results from Figure 2, all
forms of guidance improve the success rate of AgentsNet with function-
based guidance (i.e., function-pseudocode and function-description agents)
performing the best.
–For maximal matching problem, function-based guidance also perform the
best.
–Finally, for minimal vertex cover problems, guidance did not appear to pro-
duce meaningful differences in the number of feasible instances.
6.2 Global Coordination Problems
We now present results on the global variants of the three domains, where either
MIS or Distributed DFS is the algorithmAwhose components are provided
as guidance to the LLM agents. For these experiments, we constraint the oracle
Code agent to use the same number of communication rounds as the LLM agents
to allow for fair comparisons between the different agent types.
Figure 4 shows the results when the algorithm employed is MIS. In general,
the trends here are mostly consistent with the trends from the local variants
shown in Figure 2:
–Gemini agents perform better than Llama and Qwen agents across all three
problem domains.
–Among Llama agents, in general, all forms of guidance improve upon
AgentsNet with statistical significance.
–Among Qwen agents, in general, there is no statistical difference between
AgntsNet and the SGT agent types.
–Among Gemini agents, Function-pseudocode agents perform best in 3-
coloring and maximum matching, while Function-description agents perform
best in minimum vertex cover.
The key difference with the results from the local variants is that the oracle Code
agent now has a non-zero error. The main reason is the following: While MIS is
guaranteed to find a feasible solution in the simpler local variant problems, it is
not guaranteed to find optimal solutions in these problems that require global
coordination.
5 Defined as the fraction of instances that were successfully solved.

14 B. Rachmut et al.
Figure 5 shows the results when the algorithm employed is Distributed DFS.
Most of the trends from earlier still apply here as well. However, there are several
key differences:
–Some of the Gemini agent types perform better than the oracle Code agent!
While one expects that oracle Code agents find optimal solutions because
they are running Distributed DFS, which has optimality guarantees, that is
under the assumption that it has enough runtime to run till convergence. As
we limit the number of communication rounds to be the same as that of the
LLM agents, this guarantee no longer applies, and the reported results are
not necessarily optimal.6
–When using Gemini models, none of the guidance forms help in 3-
coloring problems. However function-description guidance helped in max-
imum matching and full-pseudocode guidance helped in minimum vertex
cover problems.
As Gemini consistently achieves the lowest errors across all domain variants
andalgorithms(Figures2–5)amongthethreeLLMmodels,wefocusourdetailed
quantitative analysis on this model. Table 1 consolidates these results across all
tasks and algorithms, showing that, in most cases,the most effective agents
are those with function-based guidance(i.e., function description and function
pseudocode)exhibiting intermediate autonomy.
6.3 Discussion
Across all domains, the results reveal that both the form of symbolic guidance
and the underlying algorithm jointly shape agents’ ability to reason and coordi-
nate effectively.
Among the tested models, Gemini consistently demonstrates the strongest
capacity to leverage symbolic structure, achieving lower errors and more stable
performance across guidance levels. This trend suggests that more capable mod-
elsarebetterabletointernalizeandoperationalizesymbolicscaffolds,translating
external structure into coherent multiagent reasoning.
Notably, function description agents often achieve the best or near-best re-
sults across domains. This suggests that LLMs perform best when symbolic
guidance captures algorithmic intent at a conceptual level rather than prescrib-
ing every procedural detail. In contrast, both unguided AgentsNet agents and
fully specified pseudocode agents tend to underperform, indicating that excessive
autonomy or over-specification can each disrupt coherent coordination.
For local agent-based MIS heuristics, lightweight scaffolds (e.g., function
pseudocode) further illustrate this pattern, providing enough structure to sup-
port coordination while preserving reasoning flexibility. In contrast, overly de-
tailed guidance (e.g., full pseudocode specifications) often leads to degraded per-
6 While the same constraint is imposed on Code agents when it is running MIS, that
limitation did not prevent it from finding the best solutions across the different agent
types.

Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination 15
Local (MIS)
(∆+1)- Maximal Minimal
Coloring Matching V ertex Cover
AgentsNet 1.99±0.43 1.03±0.34 2.74±0.44
Function-Description 0.55±0.260.78±0.31 2.21±0.34
Function-Pseudocode0.34±0.120.80±0.30 3.03±0.40
Main-Pseudocode 1.05±0.33 1.85±0.46 2.34±0.38
Full-Pseudocode 0.76±0.25 2.61±0.49 3.48±0.25
Global (MIS)
3-Coloring Maximum Minimum
Matching V ertex Cover
AgentsNet 2.35±0.33 1.24±0.11 2.90±0.31
Function-Description 1.92±0.30 1.11±0.202.35±0.32
Function-Pseudocode1.56±0.24 1.01±0.173.29±0.39
Main-Pseudocode 2.49±0.33 1.37±0.26 2.83±0.26
Full-Pseudocode 1.89±0.36 1.85±0.25 3.68±0.26
Global (Distributed DFS)
3-Coloring Maximum Minimum
Matching V ertex Cover
AgentsNet 2.35±0.33 1.24±0.11 2.90±0.31
Function-Description 3.15±0.361.02±0.164.23±0.27
Function-Pseudocode2.02±0.361.96±0.32 2.77±0.44
Main-Pseudocode 3.47±0.42 1.72±0.23 3.97±0.29
Full-Pseudocode 2.38±0.34 2.37±0.251.54±0.31
Table 1: Gemini-2.5: meanln(1 + SSE)±SEMacross different experimental
settings (best per column inbold). Each section header indicates the domain
variant and, in parentheses, the algorithm used.
formance, implying that symbolic scaffolds are most effective when they com-
plement rather than constrain the model’s reasoning process.
For the global search-based Distributed DFS algorithm, results are more
mixed: Performance differences across SGT agent types are often not statistically
significant. In some cases, detailed guidance helps (e.g., full-pseudocode agents
with Gemini on minimum vertex cover problems), while in others, it hinders
performance (e.g., function-description and main-pseudocode agents on the same
task).Overall,thesefindingssuggestthatLLM agents benefit most from symbolic
scaffolds that align with simpler, local heuristics, whose algorithmic structure can
be more readily absorbed and integrated by language models, unlike complex
global search procedures that impose rigid control flows and exceed the model’s
representational strengths.

16 B. Rachmut et al.
7 Conclusions
This paper introduced the Symbolic Guidance Taxonomy (SGT) – a principled
framework for analyzing how symbolic structure shapes intelligence and coor-
dination in LLM-based multiagent systems. SGT conceptualizes agent behavior
as a continuum of autonomy, identifying symbolic guidance as a controllable
mechanism that modulates this autonomy in distributed multiagent coordina-
tion settings.
Empirically, we evaluated the SGT framework across multiple coordination
domains (graph coloring, matching, and vertex cover). We examined six LLM
agent types positioned along the SGT autonomy spectrum and contrasted two
algorithmic paradigms: Local heuristic-based coordination and global exhaustive
distributed search. Together, these experiments provide a systematic view of how
symbolic representation and autonomy interact to influence coordination quality.
Our results show that coordination performance does not improve monoton-
ically with either increased guidance or greater autonomy; rather, it depends on
how the two are balanced.The strongest gains occur at intermediate autonomy
levels, where symbolic structure provides a useful scaffold for reasoning while
maintaining flexibility. These benefits, however, arise primarily when the guid-
ance derives from heuristic algorithms, whose simpler and more interpretable
structures align well with the reasoning capabilities of LLM agents. In contrast,
guidance based on global search algorithms typically yields little to no improve-
ment, likely because such information is overly detailed and complex, making it
difficult for LLM agents to distill and effectively exploit during coordination.
These findings demonstrate that symbolic guidance serves as a principled
lever for regulating autonomy in LLM agents. Rather than treating autonomy
as fixed, SGT enables it to be tuned through the form and representation of
symbolic information, allowing system designers to balance reliability and adapt-
ability in multiagent coordination. This connection bridges classical distributed
algorithm design with emergent language-based reasoning, showing that formal
symbolic control and generative flexibility can coexist within a unified multia-
gent framework. Future work will extend SGT to mixed-autonomy teams, where
agents within the same graph may operate at different levels of autonomy de-
pending on their role or local context. We aim to develop adaptive guidance
mechanisms that allow agents to adjust their autonomy dynamically as tasks
unfold and coordination demands shift.
Acknowledgements.This work was partially supported by the Office of Naval
Research (N00014-24-1-2663).
References
1. Alon, N., Babai, L., Itai, A.: A fast and simple randomized parallel algorithm for
the maximal independent set problem. Journal of Algorithms7(4), 567–583 (1986)

Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination 17
2. Bar-Yehuda, R., Censor-Hillel, K., Ghaffari, M., Schwartzman, G.: Distributed ap-
proximation of maximum independent set and maximum matching. In: Proceed-
ings of the ACM Symposium on Principles of Distributed Computing (PODC). pp.
165–174 (2017)
3. Barabási, A.L., Albert, R.: Emergence of scaling in random networks. Science
286(5439), 509–512 (1999)
4. Barde, P., Foerster, J., Nowrouzezahrai, D., Zhang, A.: A model-based solution to
the offline multi-agent coordination problem. In: Proceedings of the International
Conference on Autonomous Agents and Multiagent Systems (AAMAS). pp. 141–
150 (2024)
5. Blum, A.: New approximation algorithms for graph coloring. Journal of the ACM
(JACM)41(3), 470–516 (1994)
6. Chiang, W.L., Zheng, L., Sheng, Y., Angelopoulos, A.N., Li, T., Li, D., Zhu, B.,
Zhang, H., Jordan, M., Gonzalez, J.E., et al.: Chatbot arena: An open platform
for evaluating llms by human preference. In: Proceedings of the International Con-
ference on Machine Learning (ICML). pp. 7027–7046 (2024)
7. Cohen, L., Zivan, R.: Max-sum revisited: The real power of damping. In: Pro-
ceedings of the International Conference on Autonomous Agents and Multiagent
Systems (AAMAS). pp. 111–124 (2017)
8. Dorais, G., Bonasso, R.P., Kortenkamp, D., Pell, B., Schreckenghost, D.: Ad-
justable autonomy for human-centered autonomous systems on mars. In: Proceed-
ings of the Mars Society Conference. pp. 98–044 (1998)
9. Ferguson, G., Allen, J., Miller, B.: Trains-95: Towards a mixed-initiative planning
assistant. In: Proceedings of the International Conference on Artificial Intelligence
Planning Systems (AIPS). pp. 70–77 (1996)
10. Fioretto, F., Yeoh, W., Pontelli, E.: A multiagent system approach to schedul-
ing devices in smart homes. In: Proceedings of the International Conference on
Autonomous Agents and Multiagent Systems (AAMAS). pp. 981–989 (2017)
11. Grötschla, F., Müller, L., Tönshoff, J., Galkin, M., Perozzi, B.: Agentsnet:
Coordination and collaborative reasoning in multi-agent llms. arXiv preprint
arXiv:2507.08616 (2025)
12. Gunderson, J., Martin, W.: Effects of uncertainty on variable autonomy in mainte-
nance robots. In: Agents’99 Workshop on Autonomy Control Software. pp. 26–34
(1999)
13. Hanckowiak, M., Karonski, M., Panconesi, A.: On the distributed complexity of
computing maximal matchings. SIAM Journal on Discrete Mathematics15(1),
41–57 (2001)
14. Horvitz, E.: Principles of mixed-initiative user interfaces. In: Proceedings of the
SIGCHI Conference on Human Factors in Computing Systems (CHI). pp. 159–166
(1999)
15. Johansson, Ö.: Simple distributedδ+ 1-coloring of graphs. Information Processing
Letters70(5), 229–232 (1999)
16. Lee, D.T., Schachter, B.J.: Two algorithms for constructing a delaunay triangu-
lation. International Journal of Computer & Information Sciences9(3), 219–242
(1980)
17. Linial, N.: Locality in distributed graph algorithms. SIAM Journal on Computing
21(1), 193–201 (1992)
18. Luby, M.: A simple parallel algorithm for the maximal independent set problem.
In: Proceedings of the Annual ACM Symposium on Theory of Computing (STOC).
pp. 1–10 (1985)

18 B. Rachmut et al.
19. Maheswaran, R., Tambe, M., Bowring, E., Pearce, J., Varakantham, P.: Taking
DCOP to the real world: Efficient complete solutions for distributed event schedul-
ing. In: Proceedings of the International Conference on Autonomous Agents and
Multiagent Systems (AAMAS). pp. 310–317 (2004)
20. Mahmud, S., Goldfajn, D.B., Zilberstein, S.: Distributed multi-agent coordination
using multi-modal foundation models. arXiv preprint arXiv:2501.14189 (2025)
21. Miller, S., Ramchurn, S., Rogers, A.: Optimal decentralised dispatch of embedded
generation in the smart grid. In: Proceedings of the International Conference on
Autonomous Agents and Multiagent Systems (AAMAS). pp. 281–288 (2012)
22. Modi, P.J., Shen, W.M., Tambe, M., Yokoo, M.: Adopt: Asynchronous distributed
constraint optimization with quality guarantees. Artificial Intelligence161(1-2),
149–180 (2005)
23. Nguyen, D.T., Yeoh, W., Lau, H.C., Zivan, R.: Distributed gibbs: A linear-space
sampling-based DCOP algorithm. Journal of Artificial Intelligence Research64,
705–748 (2019)
24. Park, J.S., O’Brien, J., Cai, C.J., Morris, M.R., Liang, P., Bernstein, M.S.: Gen-
erative agents: Interactive simulacra of human behavior. In: Proceedings of the
Annual ACM Symposium on User Interface Software and Technology (UIST). pp.
1–22 (2023)
25. Parnas, M., Ron, D.: Approximating the minimum vertex cover in sublinear time
and a connection to distributed algorithms. Theoretical Computer Science381(1-
3), 183–196 (2007)
26. Peleg, D.: Distributed computing: A locality-sensitive approach. In: SIAM Mono-
graphs on Discrete Mathematics and Applications (2000)
27. Pertzovskiy, A., Zivan, R., Agmon, N.: CAMS: Collision avoiding max-sum for mo-
bile sensor teams. In: Proceedings of the International Conference on Autonomous
Agents and Multiagent Systems (AAMAS). pp. 104–112 (2023)
28. Rachmut, B., Zhang, N., Vorobeychik, Y., Yeoh, W.: Symbolic guidance for LLM
agents in distributed multiagent coordination. In: Proceedings of the International
Conference on Autonomous Agents and Multiagent Systems (AAMAS). pp. 3356–
3358 (2026)
29. Rust, P., Picard, G., Ramparany, F.: Resilient distributed constraint reasoning
to autonomously configure and adapt iot environments. ACM Transactions on
Internet Technology22(4), 1–31 (2022)
30. Scerri, P., Pynadath, D., Tambe, M.: Adjustable autonomy in real-world multi-
agent environments. In: Proceedings of the International Conference on Au-
tonomous Agents (AGENTS). pp. 300–307 (2001)
31. Scerri, P., Pynadath, D., Tambe, M.: Towards adjustable autonomy for the real
world. Journal of Artificial Intelligence Research17, 171–228 (2002)
32. Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J.,
Chen, X., Lin, Y., et al.: A survey on large language model based autonomous
agents. Frontiers of Computer Science18(6), 186345 (2024)
33. Watts, D.J., Strogatz, S.H.: Collective dynamics of ‘small-world’ networks. Nature
393(6684), 440–442 (1998)
34. Yokoo, M., Durfee, E.H., Ishida, T., Kuwabara, K.: The distributed constraint sat-
isfaction problem: Formalization and algorithms. IEEE Transactions on knowledge
and data engineering10(5), 673–685 (2002)
35. Yue, X., Ni, Y., Zhang, K., Zheng, T., Liu, R., Zhang, G., Stevens, S., Jiang,
D., Ren, W., Sun, Y., et al.: Mmmu: A massive multi-discipline multimodal
understanding and reasoning benchmark for expert agi. In: Proceedings of the

Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination 19
IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).
pp. 9556–9567 (2024)
36. Zilberstein, I., Rao, A., Salis, M., Chien, S.A.: Decentralized, decomposition-based
observation scheduling for a large-scale satellite constellation. In: Proceedings of
the International Conference on Automated Planning and Scheduling (ICAPS).
pp. 716–724 (2024)
