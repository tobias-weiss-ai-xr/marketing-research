---
title: Locating and Closing Information Gaps in Multi-Agent Systems
url: https://arxiv.org/abs/2610.40186
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Yaxin Gong
- Chongming Gao
- Gangyi Zhang
- Chenxiao Fan
- Leyang Shen
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.40186
pages: 12
chars: 76219
fetched_at: '2026-11-08T13:36:02+00:00'
kb_version: 1
---

# Locating and Closing Information Gaps in Multi-Agent Systems

Locating and Closing Information Gaps in Multi-Agent Systems
Yaxin Gong1,2, Chongming Gao1, Gangyi Zhang2, Chenxiao Fan1, Leyang Shen3,
Jiakai Wang2, Dong Wang2, Yang Liu2, Haoyan Liu1, Xinting Hu1
1 University of Science and Technology of China
2 Qwen Business Unit of Alibaba 3 National University of Singapore
gyx2022@mail.ustc.edu.cn
Abstract
Multi-step Web tasks often require several LLM agents to gather
and combine evidence. The communication graph of a fixed work-
flow restricts which agents can read each other’s outputs: evidence
retrieved by one agent may never reach the agent that needs it,
leaving aninformation gapand an incomplete or incorrect answer.
Adding a connection can deliver the missing evidence, but can also
lead the receiver to adopt an incorrect upstream conclusion that dis-
places a correct answer; the final output alone does not separate the
two. We proposeSelectiveProbing andLinkInsertion forClosing
information gaps in multi-agentExecution (SPLICE), which locates
information gaps per query and decides what to adopt after adding
an edge. After the original workflow runs, SPLICE uses the query
and node outputs to locate a possible gap, adds one directed edge
from a source to a receiver to deliver the relevant evidence, and
re-executes the receiver and affected downstream nodes, produc-
ing a candidate answer. The adoption decision reads both the final
answers of the two runs and the process changes the edit caused
inside the workflow: how far the receiver moved, where its new
content came from, and whether the change reached the final an-
swer. A selector trained on these process features chooses between
adopting the candidate answer and retaining the original. On five
benchmarks, SPLICE raises the task score on Web tool use by8.0%
and the mean score on four reasoning and planning benchmarks by
5.7%relative to the static skeleton, at1 .25to1 .44× the skeleton’s
cost, and transfers zero-shot to four unseen backbones.
CCS Concepts
•Computing methodologies → Multi-agent systems;•Infor-
mation systems→Information retrieval.
Keywords
Multi-Agent Systems, Agentic Search, Evidence Grounding, Large
Language Models
1 Introduction
A growing share of complex requests on the Web cannot be an-
swered from any single source, but require evidence gathered across
multiple services, interfaces, and pages[6, 15]. Such multi-step infor-
mation seeking is increasingly carried out by pipelines of specialised
LLM agents, each responsible for one stage of retrieval or tool
use [1, 32], which outperform single agents on many tasks [21, 43].
Together these stages form a harness that gathers and analyses Web
content. The pipeline’s communication graph determines which
agents can read each other’s outputs; the quality of the final answer
(a) Unlike fixed workflows that may omit key evidence, SPLICE selectively
adds a communication link to provide missing information where it is needed.
(b) Comparing final answers alone cannot tell whether a candidate reflects the
delivered evidence or an unrelated rewrite. SPLICE instead examines how
evidence from the added link is used to shape the receiver's reply and the final
answer, then decides whether to adopt the repair.
Key
evidence
Evidence missing Evidence added
e Key
evidence
False claim
Key omitted
False claim
e
e
e ee
e
Compare answers only Check evidence use
Adopt !
Reject !
Adopt ?
Adopt ?
Evidence lost
Useful
repair
Useless
change Evidence
Fixed workflows SPLICE
Figure 1: Comparison between existing fixed workflows (left)
and our proposed SPLICE (right).
therefore depends on whether the evidence gathered across these
stages is grounded in the agent that has to act on it.
Consider a request to plan a cross-border trip. One agent looks
up flights, another checks visa rules, and a third assembles the
itinerary. The flight agent retrieves a route with a stop in a third
country, but the visa agent never receives this detail and applies the
rules for a direct flight. The final itinerary omits a required transit
visa (Figure 1(a), left). In a fixed workflow, an agent reads only the
outputs of its direct predecessors [8], even though the evidence it
needs varies by query. The relevant evidence is already available
elsewhere in the workflow but absent from the context of the agent
that needs it. We call this aninformation gap(§3.2).
A natural fix is to add a communication edge, deliver the evidence
an upstream agent holds to the receiver, and re-execute the affected
downstream nodes [8, 12, 26, 43] (Figure 1(a), right). Adding an
edge, however, is not enough on its own. The inserted message can
supply the missing fact or lead the receiver to copy an incorrect
upstream conclusion and overwrite a correct answer [ 7, 37]; the
final output alone does not separate the two (Figure 1(b), left).
The answer produced by the edit and the re-execution—hereafter
thecandidate answer—therefore cannot be adopted automatically;
whether to adopt the candidate answer or retain the original must
be decided after observing what the edit did inside the workflow.
We draw inspiration from dendritic spine turnover: during learn-
ing, new synaptic connections form, and subsequent local activity
helps determine which are stabilised or retracted [10, 35]. Following
this “form, then select by observed activity” principle, this paper
arXiv:2610.40186v1  [cs.AI]  29 Oct 2026

Yaxin Gong et al.
proposesSelectiveProbing andLinkInsertion forClosing infor-
mation gaps in multi-agentExecution (SPLICE). After the original
workflow runs, SPLICE uses the query and node outputs to locate
an information gap, adds one directed edge from a source to a re-
ceiver, sends the relevant evidence, and re-executes the affected
downstream nodes, producing a candidate answer. The agents stay
unchanged; the original answer is retained, and SPLICE chooses
between the candidate answer and the original by reading how
outputs changed between the original run and the trial.
SPLICE decides where to add an edge through two levels of
diagnosis. At the query level, a regressor predicts the base score
each question would receive under the static skeleton, and the trial
budget goes to the questions with the largest predicted room for
improvement. At the edge level, SPLICE scores each candidate edge
by whether adding it will change the final output, and adds the
highest-scoring edge. The inserted message is not a relay of the
upstream answer; it grounds the Web evidence that the source agent
holds but the receiver’s context lacks, closing the information gap.
After the edit, SPLICE chooses between the candidate answer
and the original. The two final answers do not separate several
outcomes: the inserted message is never used by the receiver, it is
used but the revision owes nothing to it, or the revision is absorbed
downstream. SPLICE’sprocess-conditioned selectiontherefore reads
both the final answers and the process changes the edit caused
inside the workflow (Figure 1(b), right): how far the receiver moved,
where its new content came from (the message, the existing context,
or neither), and whether the change appears in the final answer. A
selector trained on these process features chooses between adopting
the candidate answer and retaining the original.
Our contributions are as follows.
• We identify and characterise theinformation gapin multi-agent
workflows, and propose SPLICE, a method that locates it per
query, closes it with one directed edge, and rolls back when
verification is unfavourable.
• We make the adoption decision from how outputs change inside
the workflow between the original run and the trial, which judges
what to keep more reliably than comparing final answers alone.
• On five benchmarks SPLICE raises Web tool use by8.0%and the
mean of four reasoning benchmarks by5.7%relative to the static
skeleton, composes with the workflows of two published systems
and a generic chain, and transfers zero-shot to four backbones.
2 Related Work
We review prior work along two lines that bear directly on this
paper: how the communication topology among agents is designed
and adjusted [34], and how, once a modification produces a candi-
date answer, a choice is made among candidates.
2.1 Multi-Agent Communication Topology
Early multi-agent systems adopted a variety of fixed topologies for
inter-agent collaboration: CAMEL [14] introduced communicative
agents that cooperate through role-playing, AutoGen [ 33] gen-
eralised this paradigm to multi-agent dialogues, LLM-Debate [5]
leveraged a multi-agent argumentation mechanism to correct hal-
lucinations, and Generative Agents [19] and AgentVerse [3] facili-
tated collaboration by simulating social environments or orches-
trating expert groups, with MetaGPT [11] and ChatDev [20] further
instantiating these fixed role divisions on software development
pipelines. As interaction patterns grew more complex, subsequent
work began to model agents explicitly as nodes in a graph and com-
munication channels as edges, optimising these graph structures
to improve collaboration [ 24]: GPTswarm [47], DyLAN [ 16], G-
Designer [43] and MACNET [21] each optimise the communication
topology from a different angle. Building on this graph-based view,
further work makes finer-grained edits to the graph structure—
MOC [8] uniformly expands the range of upstream outputs each
agent can read, AgentPrune [42] and AgentDropout [31] remove
edges judged redundant to improve efficiency, and G-Safeguard [29]
intervenes topologically to block malicious propagation. More re-
cently, DATS [12], AFlow [44], MaAS [41], MASS [46], Codebook
Agent [39] and Nexa [27] begin to decide the topology per query
rather than committing one graph for the entire dataset. None of
these methods, however, revisits the decision after observing what
the modified workflow produces: once an edge is added, its output
is used as the final answer. In this work we add an edge per query,
run a trial, and decide whether to adopt the candidate answer or
retain the original from how outputs change inside the workflow
between the base run and the trial.
2.2 Selecting Among Candidate Outputs
When a modification produces a candidate answer, deciding whether
to adopt it is a selection problem. The most basic approach places
the original answer in a candidate pool and picks the best: self-
consistency [30] takes a majority vote over multiple samples, Self-
Refine [18] and Reflexion [25] let the model reflect on and revise its
own answer, and multi-agent debate [5] converges through multi-
ple rounds of discussion. More refined selection mechanisms have
since been proposed: Oracle Gap [13] decomposes selector net gain
into recoverable headroom, verification signal quality, and harm to
already-correct answers; TrajSelector [38] scores each reasoning
step from the sampler’s own latent representations and aggregates
those scores to pick a trajectory, generative verifiers [45] score can-
didates at the token level, MAS-ProVe [28] studies how well process
verification actually works across multi-agent frameworks, and
Best-of-Evidence [40] keeps the candidate pool fixed while spend-
ing a limited budget on the evidence actions that could change the
choice; Consilience [2] calibrates a conformal guarantee on each
proposed communication action, and DoVer [17] verifies failure
hypotheses through active intervention. We compare against the
last four of these decision rules on a shared candidate pool in Ta-
ble 1. TrajSelector reads the sampler’s latent representations, which
the API backbones used here do not expose, so it is not among
the arms we run. A related line of work addresses harmful mes-
sages. G-Safeguard [29] targets harm from an external adversary
that constitutes a detectable distribution shift; in normal collab-
oration, however, a message can be fluent and well-reasoned yet
wrong, and this kind of harm from honest agents has never been
managed as an intrinsic property of collaboration. In all of the se-
lection methods above, candidates are produced by independent

Locating and Closing Information Gaps in Multi-Agent Systems
sampling or answer-level revision, and the original answer enters
the choice alongside the other candidates. Our candidates come
from a per-query edge addition and a trial; the original answer is
the default returned when the candidate is not adopted; and the
adoption decision reads how outputs change inside the workflow
between the base run and the trial, not only the final answers.
3 Preliminaries
This section sets up the notation used throughout the paper. We
cast a multi-agent workflow as a directed graph and then define
candidate edges, information gaps, and trials in turn.
3.1 Multi-Agent Workflows as Graphs
We adopt the graph formulation of multi-agent workflows used
in prior work [8, 42, 43]. A workflow is a directed acyclic graph
𝐺=(𝑉,𝐸) in which each node𝑣𝑖∈𝑉 is an LLM agent assigned a
subtask𝑥𝑖, and each edge(𝑣𝑖,𝑣 𝑗)∈𝐸 means that the output of𝑣𝑖 is
readable by𝑣𝑗 . Given a query𝑞 from a query setQ, nodes execute
in topological order: node𝑣𝑗 produces an answer𝑎𝑗 conditioned
on𝑞, on its own subtask𝑥𝑗 , and on the outputs of its in-neighbours
N−(𝑣𝑗)={𝑣 𝑖 :(𝑣𝑖,𝑣 𝑗)∈𝐸} . A designated terminal node emits the
final output ˆ𝑦𝑞, whose task score we write 𝑟𝑞 =Score( ˆ𝑦𝑞,𝑦 ★ 𝑞)∈
[0, 1], where𝑦★ 𝑞 is the reference answer. We call the collection of
all node answers in one execution itstrace,𝜏 𝑞 =(𝑎 1,...,𝑎 |𝑉|, ˆ𝑦𝑞).
Under this formulation, what𝑣𝑗 reads from upstream is exactly
the concatenation of the answers of the nodes inN−(𝑣𝑗), placed in
its prompt [8]. Two properties are worth stating explicitly, because
the problem we study follows from them. First, the query𝑞 is visible
to every node, while the intermediate products the nodes derive
from it travel only along𝐸; the visibility we refer to throughout is
therefore the visibility of these inter-node products, which is fixed
at design time and does not vary with the query. Second, a node
forwards its own answer𝑎𝑖 rather than the upstream material it
read; a piece of evidence that an upstream node derives therefore
either reaches 𝑣𝑗 in compressed form, having been rewritten at
every hop along the way, or does not reach it at all when the two
sit on branches that the skeleton never connects.
3.2 Communication Rewiring
Candidate edges.Index the nodes by a topological order of 𝐺, so
that𝑖<𝑗 implies𝑣𝑗 is not an ancestor of𝑣𝑖. Thecandidate edge set
C=

(𝑣𝑖→𝑣 𝑗):𝑖<𝑗, 𝑣 𝑖 ∉N −(𝑣𝑗) 	 (1)
collects the forward edges missing from the skeleton, each of which
would hand material from an upstream node𝑣𝑖 (thesource) directly
to𝑣𝑗 (thereceiver) without creating a cycle. Two kinds of source
qualify: nodes that already reach 𝑣𝑗 indirectly, and nodes on a
parallel branch that reach it not at all. C is determined by the
skeleton alone and is the same for every query; what varies across
queries is which of its edges is worth opening.
Information gaps.The candidate set collects every pathway that
could be opened, but only some of its edges correspond to a piece
of evidence that is actually missing. For a query𝑞 and a candidate
edge(𝑣𝑖→𝑣 𝑗)∈C , we say the pair constitutes aninformation
gapon 𝑞 when the source answer𝑎𝑖 carries evidence that𝑣𝑗 needs
to answer but that is absent from its upstream input — 𝑣𝑙∈N−(𝑣 𝑗)𝑎𝑙
and that𝑣𝑗 does not recover from𝑞 on its own. Since𝑞 is visible
to every node, the gap is the evidence that the source derived and
that the receiver can neither read nor reproduce; the definition
is structural, stating that this evidence exists at the source and is
missing at the receiver. The cross-border example in §1 belongs
to the second kind of source in (1), where source and receiver sit
on parallel branches. Membership is defined with reference to the
reference answer𝑦★ 𝑞 and is unobservable at deployment, where §4.1
supplies the ranking proxy used in its place.
Trials.Opening a candidate 𝑒=(𝑣 𝑖→𝑣 𝑗) and sending a message
𝑚 along it yields the rewired graph𝐺⊕(𝑒,𝑚)=(𝑉,𝐸∪{𝑒}) , in
which𝑣𝑗 reads𝑚 in addition to its original inputs. Only𝑣𝑗 and its
descendants need to be re-executed, producing a trial trace𝜏𝑞(𝑒,𝑚) ,
a candidate output ˆ𝑦𝑞(𝑒,𝑚)and its score𝑟 𝑞(𝑒,𝑚).
Gain.The score change of a trial relative to the base run is
𝑔𝑞(𝑒,𝑚)=𝑟 𝑞(𝑒,𝑚)−𝑟 𝑞. Because scores lie in[0,1],
−𝑟𝑞 ≤𝑔 𝑞(𝑒,𝑚) ≤1−𝑟 𝑞.(2)
We call a modificationbeneficial(B),neutral(S) orharmful(W)
according to whether𝑔>0,𝑔=0or𝑔<0.
Rewiring policies and blind commit.A rewiring policy makes
three choices on each query: whether to trial, 𝑡𝑞∈{ 0, 1}; which
edges to trial,𝑆𝑞⊆C , together with their messages; and, after the
trial, an adoption decision𝑑𝑞∈𝑆 𝑞∪{⊥} , where⊥ denotes retaining
the original answer ˆ𝑦𝑞. The policy space of rewiring strategies
introduced in §1 can now be formalised through two properties.
Definition 1(Selectivity, retractability, blind commit).A policy is
selectiveif (𝑡𝑞,𝑆𝑞) varies with𝑞, andretractableif 𝑑𝑞 is a function
of the trial trace𝜏𝑞(𝑒,𝑚) that can take the value⊥. A policy is a
blind commitif its decision does not depend on anything observed
after the trial, which takes one of two forms: ano-trial commitwith
𝑡𝑞 = 0that modifies the graph and returns the modified output as
the final answer (predicted topologies such as G-Designer, Nexa
and MaAS fall here), and apost-trial commitwith 𝑡𝑞 = 1but 𝑑𝑞 ≠⊥
for every query, which adopts unconditionally after every trial.
4 Method
SPLICE intervenes after the workflow has executed (Figure 2). For
each selected query, diagnosis picks one candidate edge and runs a
single trial; at most𝐵=𝑏|Q| queries are trialled, where𝑏∈( 0, 1]
is the budget fraction. The goal is to maximise the total score gain
across all trialled queries, counting retention of the original answer
as zero gain. All decisions before the trial rely only on the base
trace𝜏𝑞; only the adoption decision may use the trial trace. This
section is organised in two parts: diagnosis and targeted generation
decidewhereto intervene andwhatto send; process-conditioned
selection then decides, for each trialled query, whether to adopt the
candidate answer or retain the original ˆ𝑦𝑞.
4.1 Diagnosis and Targeted Generation
Query-level diagnosis: whether to repair.By Eq. (2), a trial can
win at most the headroom1−𝑟𝑞, which can be estimated before
the trial. We fit the base score with a regressor ˆ𝑟𝑞 =𝑓 𝜔(𝜓(𝜏𝑞))
whose features𝜓 read only the base trace: whether the base output
failed to parse, surface statistics of the answer, and the agreement

Yaxin Gong et al.
Diagnosis
Choose one link
Output-change likelihood
Process evidence
Source attributionPropagation & retentionStronger support
Base Aug.
Message
Context
Neither Retained
Better
Same
Worse
Weaker support
Base Aug. Neither Not retained
Weighted adoption
× =
Gain
× =
Risk
Δ > 0
Message
Context
++
++
Better
Same
Worse
rq
Outcome probabilities
× =
Gain
× =
Risk
Δ ≤0++
++
Δ=Gain -Risk
…
Queries
…
Choose queries to repair
Query
Step 1: Base execution Step 2: Choose one link
Basereply
Missing items
Step 4: Augmentedexecution
BaseAug.
Selector
Adopt repairΔ > 0
Keep base
Δ≤ 0
Candidate link
Rerun
Step 3: Targeted generation
Process
evidence
Step 5: Adopt or rollback
1-rq 1-rq
1-rq
rq
rq
selector
selector
m
Figure 2: Overview of SPLICE. The four sub-decisions are made in one timeline: diagnosis selects which queries are worth a
trial and which candidate edge to open, targeted generation writes the message that edge carries, and the trial is then executed.
Only afterwards does verification read the resulting execution and decide whether to adopt the candidate answer or retain the
original ˆ𝑦𝑞. The top half of the figure shows the core mechanism behind each step.
between the terminal node’s answer and the final output. None of
these touches gold, and𝑓𝜔 is fitted on the training split only (§5.1).
We then set𝑡𝑞 =1for the𝐵queries with the largest1− ˆ𝑟𝑞.
Edge-level diagnosis: where to rewire.Within a selected query we
pick one edge fromC by ranking edges with a gold-free estimate
of thepropagation probability
𝜌𝑞,𝑒 =𝑃  ˆ𝑦𝑞(𝑒,𝑚)≠ ˆ𝑦𝑞

𝜏𝑞,𝑒 ,(3)
the probability that the trial changes the final output. It is estimated
by a light classifierℎ𝜂 whose features include the receiver’s distance
to the terminal node, the agreement between the terminal answer
and the final output, and surface statistics of the receiver’s answer.
Its training label is whether the final output changed, observable
directly after a trial without gold;ℎ𝜂 is fitted on the training split
only. At deployment every feature ofℎ𝜂 is computed from the base
trace𝜏𝑞 available before the trial.
𝑆𝑞 takes the single edge with the largest𝜌 𝑞,𝑒.
Targeted generation: what to send.Instead of forwarding the
source’s answer𝑎𝑖 verbatim, we have the source organise its content
against the receiver’s gap. Let Items(·) be a deterministic extractor
returning the entities and numbers in a text; the gap of receiver𝑣𝑗 ,
𝑀𝑞,𝑗 =Items(𝑥 𝑗)\
Ø
𝑣𝑙∈N−(𝑣 𝑗)
Items(𝑎𝑙),(4)
contains the items its subtask mentions but none of its parents’
outputs cover.𝑀𝑞,𝑗 tells the generator which items to foreground.
The message is then
𝑚=Gen 𝑎𝑖,𝑀𝑞,𝑗 .(5)
4.2 Process-Conditioned Selection
An inserted message can be present in the receiver’s input yet un-
used, can be used without producing a revision that owes anything
to it, or can move the receiver only to have the change absorbed
downstream. At the level of the final answer all three can look alike,
yet they mean very different things. The adoption decision there-
fore reads the change the edit caused inside the workflow between
the base run and the trial.
Process evidence.After a trial, the base trace 𝜏𝑞 and the trial trace
𝜏𝑞(𝑒,𝑚) form a pair, from which we read three groups of measure-
ments. The first ishow far the receiver moved: what its revision
added, dropped, and how large it was. The second iswhere the
revision came from: added content attributed to what the message
supplied, to what the receiver already had, or to neither. The third
iswhether it survived: how far the change travelled toward the
terminal node and whether the message’s content is still in the final
answer. We write these as theprocess evidence𝜙𝑞,𝑒 =𝜙(𝜏 𝑞,𝜏𝑞(𝑒,𝑚)) ;
the full list of fields is given in Appendix A.4.
Selector.We implement the adoption decision as a three-class
language-model selector 𝜋𝜃(𝑐|𝑧 𝑞,𝑒), 𝑐∈ { B, S, W}, whose in-
put𝑧𝑞,𝑒 =(𝑞,𝑥 𝑗,𝐺, ˆ𝑟𝑞, ˆ𝑦𝑞, ˆ𝑦𝑞(𝑒,𝑚),𝜙 𝑞,𝑒) contains the query, the re-
ceiver’s subtask, the workflow structure, the predicted base score,
the base and candidate outputs, and the process evidence. Train-
ing labels𝑐★ =sign(𝑔 𝑞(𝑒,𝑚)) are derived from reference answers;
no gold is used at inference. The selector is initialised by super-
vised fine-tuning, which gives the reference policy𝜋ref, and then
refined by direct preference optimisation [23] on pairs(𝑐★,𝑐−) with
𝑐− ≠𝑐 ★:
L(𝜃)=−E
h
log𝜎

𝛽log 𝜋𝜃(𝑐★|𝑧) 𝜋ref(𝑐★|𝑧) −𝛽log 𝜋𝜃(𝑐−|𝑧) 𝜋ref(𝑐−|𝑧) i .(6)
Weighted adoption.The selector scores three outcomes; the de-
ployment action is binary, adopt the candidate answer or retain
the original ˆ𝑦𝑞. At deployment the selector yields ˆ𝑝b =𝜋𝜃(B|𝑧 𝑞,𝑒)
and ˆ𝑝h =𝜋𝜃(W|𝑧 𝑞,𝑒) for each trialled edge. The adoption margin
is Δ𝑞,𝑒 = ˆ𝑝b(1− ˆ𝑟𝑞)− ˆ𝑝h ˆ𝑟𝑞, weighting a potential gain against the
headroom1− ˆ𝑟𝑞 and a potential loss against the score ˆ𝑟𝑞 already
in hand. The better the original answer, the stronger the evidence
needed to adopt the candidate. Neutral outcomes carry no weight

Locating and Closing Information Gaps in Multi-Agent Systems
Table 1: End-to-end results on five benchmarks. Net is the per-question fix−harm rate (%). Best values per column are bolded.
ToolBench(𝑛=230) Four benchmarks(𝑛=2,142) Total
Method Micro Served Net % Cost MuSiQue DROP 2Wiki PlanCraft Mean Net % Cost
Static 0.6347 0.3957 – 1.00×0.4257 0.6734 0.7614 0.6988 0.6654 – 1.00×
Always 0.6514↑.0167 0.3435↓.0522 +2.6 1.75× 0.4184↓.0073 0.7015↑.0281 0.7649↑.0035 0.6842↓.0146 0.6725↑.0071 +2.0 1.71×
Random 0.6384↑.00370.3870↓.0087+0.91.67×0.4343↑.00860.7004↑.02700.7607↓.00070.6491↓.04970.6678↑.0024+1.91.71×
Self-cons. 0.6282↓.0065 0.3609↓.0348 −1.7 3.00× 0.4346↑.0089 0.6874↑.0140 0.7627↑.0013 0.6813↓.0175 0.6692↑.0038 −0.1 3.00×
Judge 0.6624↑.02770.4304↑.0348+6.12.67×0.4418↑.01610.6985↑.02510.7717↑.01030.6871↓.01170.6781↑.0127+3.11.88×
Regressor 0.6572↑.0225 0.4304↑.0348 +4.3 2.35× 0.4322↑.0065 0.7011↑.0277 0.7624↑.0010 0.7281↑.0292 0.6808↑.0154 +4.4 1.75×
MOC 0.6598↑.02510.4304↑.0348+5.21.75×0.4475↑.02180.7218↑.04840.7602↓.00120.6871↓.01170.6831↑.0177+4.71.71×
Nexa 0.6514↑.0167 0.3435↓.0522 +2.6 1.09× 0.4314↑.0057 0.6954↑.0220 0.7643↑.0029 0.7105↑.0117 0.6766↑.0112 +2.5 1.42×
Nexa+rb. 0.6613↑.02660.4130↑.0174+5.21.09×0.4388↑.01310.7006↑.02720.7666↑.00520.7193↑.02050.6818↑.0164+3.81.45×
MAS-ProVe 0.6580↑.0233 0.4391↑.0435 +4.3 2.71× 0.4363↑.0106 0.7170↑.0436 0.7569↓.0045 0.7485↑.0497 0.6883↑.0229 +5.0 1.81×
Best-of-Evid. 0.6419↑.00720.4043↑.0087+1.71.85×0.4276↑.00190.7132↑.03980.7634↑.00200.7047↑.00580.6807↑.0153+3.11.41×
DoVer 0.6419↑.0072 0.4130↑.0174 +0.9 1.33× 0.4384↑.0127 0.6843↑.0109 0.7689↑.0075 0.6988 0.6737↑.0083 +0.8 1.03×
Consilience 0.6401↑.00540.3957+0.92.71×0.4337↑.00800.7125↑.03910.7638↑.00240.7368↑.03800.6868↑.0214+4.41.81×
SPLICE (𝑏=0.3) 0.6769↑.0422 0.4304↑.0348 +7.0 1.27× 0.4575↑.0318 0.6858↑.0124 0.7633↑.0019 0.7632↑.0643 0.6858↑.0204 +4.7 1.11×
SPLICE (𝑏=0.5)0.6856↑.05090.4478↑.0522+8.71.44×0.4612↑.03550.7158↑.04240.7760↑.01460.7778↑.07890.7031↑.0377+5.31.25×
SPLICE (full) 0.6813↑.0466 0.4391↑.0435 +7.8 1.90× 0.4662↑.0405 0.7272↑.0538 0.7799↑.0185 0.7836↑.0848 0.7101↑.0446 +7.5 1.50×
on either end. The decision is
𝑑𝑞 =
(
arg max𝑒∈𝑆 𝑞 Δ𝑞,𝑒 ifmax 𝑒∈𝑆 𝑞 Δ𝑞,𝑒 >0,
⊥otherwise. (7)
5 Experiments
We organise our evaluation around four research questions.
• RQ1:Does the full method beat the static skeleton and baselines?
•RQ2:What does each component contribute?
• RQ3:Does SPLICE locate the information gap it sets out to close?
• RQ4:Does it generalise across host workflows, backbones and
skeleton scales?
5.1 Experimental Setup
Datasets and evaluation.ToolBench [ 22] is the primary workload
(Table 2) and matches the Web-tool-use track adopted by broader
agent-evaluation suites: agents issue tool calls through the Stable-
ToolBench [9] virtual API server, which replays archived responses
so the same request yields the same result on any day, and paired
differences therefore reflect the communication repair rather than
service availability. PlanCraft is scored by executing the crafting
sequence against the benchmark’s recipe library. Rollback is scoped
Table 2: Datasets and evaluation. Micro grades each required
API by call and content; Served is the fraction of fully-scored
requests; Token F1 and Plan success score the other four
benchmarks against reference answers.
Dataset Task Metric Train Test
ToolBench Web tool use Micro (Served) 535 230
MuSiQue Multi-hop QA Token F1 1,680 360
DROP Discrete reasoning Token F1 3,360 720
2WikiMultihopQA Multi-hop QA Token F1 3,360 720
PlanCraft Embodied planning Plan success 1,596 342
to the output layer and does not undo executed tool calls. Each
dataset is split at the question level; all learned components are
fitted on the training split only, and every reported number comes
from a single evaluation on the test split. The mean over the four
reasoning and planning benchmarks is weighted by test-set size,
and the individual benchmark scores show how improvements
vary across question answering and planning. Appendix A.1 gives
skeleton structures and split details.
Baselines.We compare against five generic controls: Always,
which adds all candidate edges at once; Random, which opens one
at random; Self-consistency [30]; a tuned LLM Judge; and a gain
Regressor. We also compare against the published systems MOC [8]
and Nexa [27], together with Nexa+ rollback, which attaches our
rollback step to the graph Nexa predicts, and against four pub-
lished selection rules—MAS-ProVe [28], Best-of-Evidence [40], Con-
silience [2] and DoVer [17]—all on the same skeletons, questions and
splits, each running its own procedure (details in Appendix A.5).
Implementation.All workflow nodes run on gpt-4o-mini; the
adoption selector is a local Qwen2.5-7B-Instruct [36] trained with
DPO. We report three budget fractions𝑏∈{ 0.3, 0.5, 1.0}. Intervals
are95%question-paired bootstrap CIs; cost is a dollar multiple over
the static skeleton, with the selector charged at its public hosted
rate (4.9%of the total). Appendices A.3 and A give full details.
5.2 End-to-End Performance (RQ1)
The full method is ahead on both workloads. At 𝑏=0.5it reaches
0.6856Micro on ToolBench and a weighted mean of0 .7031on the
four benchmarks,+0.0509and+0.0377over the static skeleton, and
its paired difference against every competitor (Table 14) stays above
zero. The half budget is a favourable operating point: it buys most
of the gain at1.44× the cost on ToolBench and1.25× on the four
benchmarks, trading a small amount of score for a lower cost than
the full budget. Opening edges without selection gives a different
picture: Always and Random fix about as many questions as they

Yaxin Gong et al.
Table 3: Query-level diagnosis calibration on ToolBench
(𝑛=230). Bins are quintiles of predicted base score ˆ𝑟𝑞.
Q1 (low) Q2 Q3 Q4 Q5 (high) All
Predicted 0.392 0.548 0.651 0.736 0.847 0.635
Actual 0.388 0.542 0.648 0.740 0.856 0.635
Trialled 100% 100% 50% 0% 0% 50%
harm, a net rate of only+2.0%and+1.9%on the four benchmarks,
so the gain comes from where to intervene.
The two calibers diverge in a way that is itself informative. Al-
ways and Nexa raise Micro by0 .0167yet lose0 .0522on Served:
opening an edge unconditionally displaces answers that were al-
ready complete. The same effect appears between our own budget
settings. The half budget both serves more requests (0.4478against
0.4391) and scores higher on Micro (0.6856against0 .6813) than the
full budget, so the extra trials the full budget buys crowd out some
responses that needed no repair at all.
Attaching rollback to an existing method captures part of the gain
but does not close it: Nexa+ rollback reaches0.6613on ToolBench,
still0.0243below the full method, and trails it by0 .0213on the four
benchmarks. Targeted diagnosis and process-conditioned selection
add value beyond attaching rollback to a predicted graph.
The gains hold under a different family of scoring rules from
ToolBench’s Micro. MuSiQue, DROP and 2WikiMultihopQA are
scored by standard token F1, and PlanCraft by an executable verifier
that steps through the recipe inventory, and the weighted mean
gain across them is+0.0377at 𝑏=0.5. The same method that helps
on the Micro metric also helps under these separate rules, so the
improvement comes from the communication repair rather than
from a fit to one scoring signal. On ToolBench, §5.4 audits the same
questions against the API responses the workflow received.
5.3 Component Contribution (RQ2)
We verify each component along the four layers of locating.
Layer 1: Query-level locating.Table 3 bins the230test questions
into quintiles by predicted base score ˆ𝑟𝑞 and reports the mean
predicted score, the mean actual score and the fraction trialled at
budget𝑏=0.5. Predicted and actual scores track closely. The budget
concentrates entirely on the two lowest quintiles, which are trialled
at 100%, while the two highest quintiles are skipped entirely. Table 4
corroborates this: removing diagnosis altogether raises cost without
raising the score, and replacing the predicted score with a constant,
a parse-failure flag or answer length all fall significantly below the
full diagnosis.
Layer 2: Edge-level locating.On the same535training queries, the
edge selected by𝜌, which is the edge the full method uses, produces
an output change on115questions, of which70improve and45
worsen, a fix ratio of0 .61. A randomly chosen edge produces a
change on96questions,44improving and52worsening, a fix ratio
of0.46. The edge diagnosis thus selects edges that are not merely
more likely to change the output but more likely to change it for
the better. In the ablation table, random edge selection falls−0.0202
behind the full method, and ranking edges by a predicted-gain head
falls−0.0185behind it: 𝜌 selects better edges than a direct gain
Table 4: Component ablation on ToolBench with the four
locating layers varied in turn. Δ is relative to Full (𝑏=0.5); the
intervals are 95% paired bootstrap CIs over questions.
Configuration Score Δ Net % Cost
Static skeleton 0.6347 – – 1.00×
w/o diagnosis 0.6813−.0043+.0073 −.0162 +7.8 1.90×
ˆ𝑟= constant 0.6718−.0138 −.0054 −.0296 +6.11.44×
ˆ𝑟= parse failure 0.6648−.0208−.0146 −.0401 +3.5 1.44×
ˆ𝑟= length 0.6642−.0214 −.0147 −.0410 +3.51.44×
edge=random 0.6654−.0202−.0137 −.0392 +4.3 1.44×
edge=predicted gain 0.6671−.0185 −.0021 −.0372 +4.31.44×
w/ verbatim forward 0.6732−.0124−.0050 −.0285 +5.2 1.44×
w/ untargeted msg 0.6749−.0107 −.0038 −.0258 +6.11.44×
w/ key fact removed 0.6745−.0111−.0052 −.0246 +5.2 1.44×
w/ length-matched filler 0.6697−.0159 −.0082 −.0351 +5.21.44×
w/o message (re-run) 0.6665−.0191−.0112 −.0375 +4.3 1.44×
w/ self-revision (matched budget) 0.6689−.0167 −.0012 −.0349 +4.31.44×
w/o rollback 0.6727−.0129−.0052 −.0307 +6.1 1.44×
adopt by ˆ𝑝b− ˆ𝑝h 0.6738−.0118 −.0041 −.0290 +6.11.44×
adopt by predicted gain 0.6789−.0067−.0005 −.0160 +7.0 1.44×
w/ benefit head only 0.6634−.0222 −.0157 −.0427 +3.51.44×
w/o process evidence 0.6709−.0147−.0071 −.0334 +5.2 1.44×
w/ shuffled process 0.6699−.0157 −.0081 −.0351 +5.21.44×
w/ raw-trace selector 0.6772−.0084−.0019 −.0221 +6.1 1.44×
w/o attribution 0.6780−.0076 −.0012 −.0210 +6.11.44×
attribution only 0.6760−.0096−.0028 −.0238 +5.2 1.44×
w/ SFT selector 0.6818−.0038 +.0081 −.0160 +7.81.44×
Full(𝑏=0.5) 0.6856 – +8.7 1.44×
forecast, since the gain depends on what the receiver does with the
message and is only measurable after the trial.
Layer 3: Message-level locating.The message ablations form a
ladder that holds the edge and the re-execution fixed and varies
only what is sent. At the bottom, re-running the same nodes with
no edge and no message at the same1 .44× budget scores0.6665.
Opening the edge with length-matched filler adds0.0032. Removing
only the key factual statement while keeping the rest of the message
intact gives0.6745, and the complete message gives0.6856. Of the
0.0159separating filler from the full method, roughly seven tenths is
carried by that single factual statement, confirming that the message
locates a specific piece of missing evidence. On the same queries,
115answers change when a targeted message is delivered against
68without one, so the adoption rule has69%more candidates to
choose among. Spending the same1.44× budget on receiver self-
revision with the same selector, rather than on a targeted message,
reaches0.6689, so at matched cost the gain comes from delivering
the located evidence rather than from the extra computation alone.
Appendix A.8 reproduces two archived edges, one a ToolBench
edge carrying an API payload downstream.
Layer 4: Process-evidence verification.Removing process evidence
entirely costs−0.0147, and shuffling it costs−0.0157, confirming
that the features carry a real signal. The attribution group isolates

Locating and Closing Information Gaps in Multi-Agent Systems
Table 5: Gap-hit precision@1 on the held-out ToolBench test
set, with two judges supplying the gap labels and 𝜌 compared
against three heuristic edge-selection rules.
Edge selection rule Precision@1 95%CI
Random reachable edge0.41[.34, .48]
Terminal-distance (nearest) 0.49 [.42, .56]
Content coverage0.55[.48, .62]
𝜌(SPLICE) 0.67 [.60, .74]
Table 6: Gap-localisation audit on𝑛=120adopted repairs, inde-
pendently scored by two judges across four conditions whose
joint rate is reported in the bold row.
Condition DeepSeek-v4-pro Claude-opus-4-6
Source holds the fact0.88[.82,.93]0.86[.79,.91]
Receiver lacked the fact 0.91[.85,.95] 0.89[.83,.94]
Message delivered the fact0.85[.78,.90]0.83[.76,.89]
Revision used the fact 0.82[.75,.88] 0.80[.72,.86]
All four hold0.74[.66,.81]0.71[.63,.79]
the most diagnostic layer: removing it alone costs−0.0076, so know-
ing whether new content originated from the message or from the
receiver’s own resampling has independent value for the adoption
decision. A selector reading the same base and trial traces as raw
text, with the same model, training data, and candidate pool but
without the hand-computed attribution features, reaches0.6772and
trails the full method by−0.0084, so the explicit process-attribution
features add adoption value on top of access to the same trace.
Adopting by the unweighted difference ˆ𝑝𝑏− ˆ𝑝ℎ falls behind the
asymmetric default by −0.0118(CI clear of zero), showing that
weighting a candidate against the headroom on one side and the
score already in hand on the other is doing work. Replacing the se-
lector altogether with a predicted-gain regressor costs−0.0067(CI
[−.0160,−. 0005]), so the three-class process-conditioned selector
improves adoption beyond a direct gain forecast on top of the same
adoption rule. These results support combining process evidence
with the predicted base score when deciding whether to adopt a
repair. The process features help distinguish beneficial from harm-
ful changes, while the base score determines their relative weights:
a higher predicted score increases the penalty for potential harm
and reduces the weight assigned to potential improvement.
5.4 Gap Localisation (RQ3)
Pre-trial gap-hit precision.We first test whether the edge selector
locates real gaps before any trial. On the held-out test set, two
judges label for each question which candidate edges correspond to
a true information gap, a source-held fact absent from the receiver’s
upstream context and not recovered from𝑞; we take this as ground
truth and measure how often each rule’s top-ranked edge is a true
gap (Table 5). Ranking by𝜌 reaches a precision@1 of0.67, above
random reachable edges (0.41), the terminal-distance heuristic (0.49)
and content coverage (0.55): the pre-trial selector favours real gaps
over edges that merely change the output.
Table 7: Evidence support on the held-out ToolBench test
set (𝑛=230); the first three rows sum to one, and the judging
protocol is detailed in Appendix A.10.
Measure Static SPLICE
Fact-support rate0.71[.65,.77]0.83[.78,.88]
Partially-supported rate 0.11[.07,.15] 0.08[.05,.12]
Unsupported-claim rate0.18[.13,.23]0.09[.06,.13]
Task completion rate 0.63[.57,.70] 0.74[.68,.80]
Table 8: A held-out ToolBench case where SPLICE closes an
API-payload gap: the UUID returned at node 0 reaches the
terminal only after the added edge delivers it. Full archived
exchange in Appendix A.8.
Checkpoint Archived observation
Node 0 return API payload:𝑢 ∗ + captcha PNG.
Terminal input Parents (nodes 1–2): no payload and no𝑢∗.
Repair Open0→3: deliver payload to terminal.
Answer Static: “no API results”; SPLICE:𝑢∗ + image.
Post-adoption gap audit.We then audit whether an adopted edge
closes a real gap. Two judges unrelated to the workflow back-
bone and the selector independently label a random sample of
120adopted repairs against four conditions: the source holds the
fact, the receiver lacked it, the message delivered it, and the revision
used it (Table 6). All four conditions hold on0.74and0 .71of the
sample under the two judges, with substantial agreement (Cohen’s
𝜅=0.77). The audit separates an output change from a closed gap:
the majority of adopted repairs carry a fact the source already held
and the receiver lacked, deliver it, and use it in the corrected answer.
Across the28 ,560edges of the offline probe pool,613(2 .1%)
satisfy all four conditions, split almost evenly between sources on
a parallel branch the skeleton never connects (315) and distant-
ancestor sources whose content was rewritten away hop by hop
(298); both are gaps a fixed topology cannot cover. Appendix A.8
reproduces one closed gap of each kind verbatim.
Evidence support.The audit so far reads the workflow trace; we
close RQ3 at the answer level by checking whether the content a
closed gap introduces is itself grounded in an API response. On
the230held-out test questions, two judges read the API responses
the workflow actually received and verify each concrete claim, a
number, name, date or URL, against them, labelling each as sup-
ported, partially supported or unsupported (three rates summing
to one; Table 7). SPLICE raises the fact-support rate from0.71to
0.83and the task completion rate from0 .63to0 .74, and lowers the
unsupported-claim rate from0.18to0 .09. The gain therefore lands
on claims that an API response backs rather than on answer speci-
ficity alone, so the improvement reflects evidence support rather
than longer or more detailed answers.
Table 8 makes the answer-level audit concrete: the repaired
answer reuses the value returned at node 0, while the static terminal
had no access to any API result.

Yaxin Gong et al.
Table 9: Composability on three host workflows; 𝑝 compares
SPLICE against each host’s own static output.
Host Bench Static Always SPLICE 𝑝
Chain ToolBench 0.4222 0.4604↑.03820.4832↑.06100.0003
AgentPrune [42] ToolBench 0.4180 0.4428↑.0248 0.4713↑.0533 0.0003
G-Designer [43] ToolBench 0.3995 0.4212↑.02170.4433↑.04380.0008
Chain 2Wiki 0.6009 0.5942↓.0067 0.6242↑.0233 0.0828
AgentPrune 2Wiki 0.5616 0.5728↑.01120.6076↑.04600.0276
G-Designer 2Wiki 0.6625 0.6689↑.0064 0.6833↑.0208 0.0100
Table 10: Backbone transfer on DROP, 2Wiki and PlanCraft,
with the selector fitted once on gpt-4o-mini and reused on
four unseen backbones with no retraining.
Backbone Static Always SPLICE 95%CI 𝑝
Kimi-K2.6 0.7150 0.7436 0.7652↑.0502[.026, .076]1.3×10 −4
DeepSeek-V3.2 [4] 0.7245 0.7167 0.7758↑.0513 [.030, .076] 1.2×10−5
Qwen3.7-Max 0.8355 0.8406 0.8673↑.0317[.014, .052]1.2×10 −3
Qwen3.6-Plus 0.7636 0.7714 0.7921↑.0284 [.012, .047] 1.7×10−3
4 8 12
0.44
0.47
0.50
0.53Task score ↑
Chain
Static Ours
4 8 12
Tree
4 8 12
Dense
4 8 12
Agents
1.0
1.4
1.8
2.2Token cost ↓ Token cost (× static)
4 8 12
Agents
4 8 12
Agents
Figure 3: Skeleton scan on DROP across three topology fami-
lies (Chain, Tree, Dense) and three agent scales (4, 8, 12).
5.5 Generalisation and Boundaries (RQ4)
Composability.SPLICE adds value on top of existing workflows
(Table 9). Across six host-by-benchmark cells it improves on each
host’s own output: by+0.044to +0.061on the three ToolBench
hosts (𝑝≤ 0.0008) and by+0.021to+0.046on the three 2Wiki hosts.
The 2Wiki-Chain cell is the informative one: its candidate pool is
net negative, so opening every edge (Always) loses0.0067, while
SPLICE still gains+0.0233because rollback keeps the harmful edits
out. Per-query diagnosis and rollback thus act as a layer on top of
an existing orchestration rather than a replacement for its topology.
Backbone, scale and budget.The method holds as the setting
changes. The selector is fitted once on gpt-4o-mini and never re-
trained, yet transfers to four unseen backbones with gains of+0.028
to+0.051(Table 10, all 𝑝≤ 2× 10−3), so the gain does not fade as
the backbone grows stronger. Across nine topologies and scales
the direction is positive throughout (Figure 3), as the number of
candidate edges|C| ranges from2to55and the gains run from
+0.0154to+0.0383. The budget sweep separates the two workloads:
ToolBench Micro rises monotonically with𝑏 up to a peak at𝑏=0.5
0.1 0.3 0.5 0.7 1.0
Budget fraction b
0.650
0.675
0.700ToolBench Micro
static skeleton
b = 0.5
ToolBench
0.1 0.3 0.5 0.7 1.0
Budget fraction b
0.675
0.700Weighted mean static skeleton
b = 0.5
Four benchmarks
Score
Cost
1
2
3
Cost multiple
1.0
1.5
2.0
Cost multiple
Figure 4: Score and cost against the trial-budget fraction 𝑏 on
ToolBench and the four reasoning and planning benchmarks.
and declines at𝑏=1.0, while the four reasoning and planning bench-
marks rise and then saturate for𝑏≥ 0.5(Figure 4), so the operating
point𝑏=0.5sits on the knee for both workloads at matched cost.
The gain is positive across all nine topologies and scales, and its
size follows how much the terminal structure lets a local edit move.
The candidate count does not determine the gain monotonically:
the smallest pool (|C|= 2) and the largest one (|C|= 55) both improve,
while the nine gains interleave between+0.0154and+0.0383rather
than rising with|C| . SPLICE therefore buys better gap localisation
rather than a larger candidate pool or additional trials per query.
The size of each gain tracks the room the terminal structure leaves
for a single rewritten edge to move the final answer, as the per-cell
counts in Figure 3 show across chain and tree families alike.
6 Conclusion and Future Work
When multiple LLM agents collaborate on Web content, the quality
of the final answer depends on whether each cross-agent transfer
of evidence reaches the party that needs it. We proposed SPLICE,
which after the original workflow has executed locates an informa-
tion gap per query, closes it with one directed edge, re-executes the
affected downstream nodes, and chooses between the candidate an-
swer and the original from how outputs change inside the workflow
between the base run and the trial. Across five benchmarks SPLICE
raises the task score on Web tool use by8.0%and the mean on four
reasoning and planning benchmarks by5.7%relative to the static
skeleton at1.25to1.44×its cost, composes with the workflows of
two published systems and a generic chain, and transfers zero-shot
to four unseen backbones. Intervention analysis and ablations to-
gether show that the final answer alone cannot say what should
be kept; the adoption decision has to read the process trace an edit
leaves inside the workflow between the original run and the trial.
As Web agent pipelines scale to more sources and longer tool-use
chains, cross-agent evidence transfer becomes the reliability pivot
of collaborative systems. The present work operates with a single
gap and one real trial per query. Pushing process evidence from
agent replies down to pages, documents, and entities, and extending
the method from read-only Web to writing and transactional APIs,
are natural next steps: in these settings cross-source corroboration
can tighten gap identification, and single-edge repair can grow into
multi-step repair in which process features replace a real trial as
a cheaper adoption criterion. We plan to pursue these directions
toward Web multi-agent systems in which diagnosis, repair, and
verification run through the full collaboration lifecycle, providing
a more reliable foundation for increasingly complex Web mining
and information integration tasks.

Locating and Closing Information Gaps in Multi-Agent Systems
References
[1] Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, and Hannaneh Hajishirzi. 2024.
Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection.
InThe Twelfth International Conference on Learning Representations.
[2] Abhijith Babu, Ramneet Kaur, Vishal Pramanik, Olivera Kotevska, Nathaniel D.
Bastian, Susmit Jha, Sunny Raj, Yanzhao Wu, Sumit Kumar Jha, and Anirban
Roy. 2026. Consilience: Conformally Calibrated Communication Control for
Hidden-Profile Multi-Agent Reasoning. arXiv:2608.20564
[3] Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chi-Min Chan,
Heyang Yu, Yaxi Lu, Yi-Hsin Hung, Chen Qian, Yujia Qin, Xin Cong, Ruobing
Xie, Zhiyuan Liu, Maosong Sun, and Jie Zhou. 2024. AgentVerse: Facilitating
Multi-Agent Collaboration and Exploring Emergent Behaviors. InInternational
Conference on Learning Representations.
[4] DeepSeek-AI, Aixin Liu, Aoxue Mei, Bangcai Lin, Bing Xue, et al. 2025. DeepSeek-
V3.2: Pushing the Frontier of Open Large Language Models. arXiv:2512.02556
[5] Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mor-
datch. 2024. Improving Factuality and Reasoning in Language Models through
Multiagent Debate. InProceedings of the 41st International Conference on Machine
Learning.
[6] Yaxin Gong, Chongming Gao, Chenxiao Fan, Haoyan Liu, et al. 2026. Breaking
User-Centric Agency: A Tri-Party Framework for Agent-Based Recommendation.
arXiv:2603.10673
[7] Yaxin Gong, Gangyi Zhang, Chongming Gao, Leyang Shen, Chenxiao Fan, Jiakai
Wang, Dong Wang, Yang Liu, Wenjie Wang, and Xiangnan He. 2026. When
Upstream Messages Override Correct Answers: A Controlled Study of Multi-
Agent LLM Collaboration. arXiv:2609.36855
[8] Yao Guan, Lin Wang, Zhihui Lu, Ziyi Wang, Wenzhu Yan, and Qiang Duan.
2026. MOC: Multi-Order Communication in LLM-based Multi-Agent Systems.
InProceedings of the 43rd International Conference on Machine Learning.
[9] Zhicheng Guo, Sijie Cheng, Hao Wang, Shihao Liang, Yujia Qin, Peng Li, Zhiyuan
Liu, Maosong Sun, and Yang Liu. 2024. StableToolBench: Towards Stable Large-
Scale Benchmarking on Tool Learning of Large Language Models. InFindings of
the Association for Computational Linguistics: ACL 2024.
[10] Travis C. Hill and Karen Zito. 2013. LTP-induced long-term stabilization of
individual nascent dendritic spines.The Journal of Neuroscience33, 2 (2013),
678–686.
[11] Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, et al.
2024. MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework.
InThe Twelfth International Conference on Learning Representations.
[12] Yunsong Hong. 2026. Learning How Much to Collaborate: Difficulty-Aware
Topology Selection for Multi-Agent Code Generation. arXiv:2609.13890
[13] Jie Hu. 2026. Oracle Gap and Signal Fidelity: A Fixed-Pool Diagnostic for Test-
Time Collaboration. arXiv:2607.17531
[14] Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard
Ghanem. 2023. CAMEL: Communicative Agents for "Mind" Exploration of
Large Language Model Society. InAdvances in Neural Information Processing
Systems.
[15] Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, et al. 2024. AgentBench:
Evaluating LLMs as Agents. InThe Twelfth International Conference on Learning
Representations.
[16] Zijun Liu, Yanzhe Zhang, Peng Li, Yang Liu, and Diyi Yang. 2024. A Dynamic
LLM-Powered Agent Network for Task-Oriented Agent Collaboration. InFirst
Conference on Language Modeling.
[17] Ming Ma, Jue Zhang, Fangkai Yang, Yu Kang, Qingwei Lin, Saravan Rajmohan,
and Dongmei Zhang. 2026. DoVer: Intervention-Driven Auto Debugging for LLM
Multi-Agent Systems. InInternational Conference on Learning Representations.
[18] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah
Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank
Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir
Yazdanbakhsh, and Peter Clark. 2023. Self-Refine: Iterative Refinement with
Self-Feedback. InAdvances in Neural Information Processing Systems.
[19] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy
Liang, and Michael S. Bernstein. 2023. Generative Agents: Interactive Simulacra
of Human Behavior. InProceedings of the 36th Annual ACM Symposium on User
Interface Software and Technology.
[20] Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, et al. 2024. ChatDev:
Communicative Agents for Software Development. Association for Computa-
tional Linguistics, Bangkok, Thailand.
[21] Chen Qian, Zihao Xie, YiFei Wang, Wei Liu, Kunlun Zhu, Hanchen Xia, Yu-
fan Dang, Zhuoyun Du, Weize Chen, Cheng Yang, Zhiyuan Liu, and Maosong
Sun. 2025. Scaling Large Language Model-based Multi-Agent Collaboration. In
International Conference on Learning Representations.
[22] Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, et al. 2024. ToolLLM:
Facilitating Large Language Models to Master 16000+ Real-world APIs. InThe
Twelfth International Conference on Learning Representations.
[23] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano
Ermon, and Chelsea Finn. 2023. Direct Preference Optimization: Your Language
Model is Secretly a Reward Model. InAdvances in Neural Information Processing
Systems.
[24] Xu Shen, Yixin Liu, Yiwei Dai, Yili Wang, Rui Miao, Yue Tan, Shirui Pan, and
Xin Wang. 2025. Understanding the Information Propagation Effects of Commu-
nication Topologies in LLM-based Multi-Agent Systems. InProceedings of the
2025 Conference on Empirical Methods in Natural Language Processing.
[25] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and
Shunyu Yao. 2023. Reflexion: language agents with verbal reinforcement learning.
InAdvances in Neural Information Processing Systems.
[26] Jinwei Su, Qizhen Lan, Yinghui Xia, Lifan Sun, Weiyou Tian, Tianyu Shi, and
Lewei He. 2026. Difficulty-Aware Agentic Orchestration for Query-Specific
Multi-Agent Workflows. InProceedings of the ACM Web Conference 2026.
[27] Nurbek Tastan, Alex Iacob, Lorenzo Sani, Meghdad Kurmanji, Nicholas D. Lane,
Samuel Horvath, and Karthik Nandakumar. 2026. Response-Conditioned Parallel-
to-Sequential Orchestration for Multi-Agent Systems. arXiv:2605.15573
[28] Vishal Venkataramani, Haizhou Shi, Zixuan Ke, Austin Xu, Xiaoxiao He, Yingbo
Zhou, Semih Yavuz, Hao Wang, and Shafiq Joty. 2026. MAS-ProVe: Understand-
ing the Process Verification of Multi-Agent Systems. InProceedings of the 43rd
International Conference on Machine Learning.
[29] Shilong Wang, Guibin Zhang, Miao Yu, Guancheng Wan, Fanci Meng, Chongye
Guo, Kun Wang, and Yang Wang. 2025. G-Safeguard: A Topology-Guided Security
Lens and Treatment on LLM-based Multi-agent Systems. InProceedings of the
63rd Annual Meeting of the Association for Computational Linguistics (Volume 1:
Long Papers).
[30] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H. Chi, Sharan Narang,
Aakanksha Chowdhery, and Denny Zhou. 2023. Self-Consistency Improves
Chain of Thought Reasoning in Language Models. InThe Eleventh International
Conference on Learning Representations.
[31] Zhexuan Wang, Yutong Wang, Xuebo Liu, Liang Ding, Miao Zhang, Jie Liu, and
Min Zhang. 2025. AgentDropout: Dynamic Agent Elimination for Token-Efficient
and High-Performance LLM-Based Multi-Agent Collaboration. InProceedings of
the 63rd Annual Meeting of the Association for Computational Linguistics (Volume
1: Long Papers).
[32] Jialong Wu, Wenbiao Yin, Yong Jiang, Zhenglin Wang, Zekun Xi, Runnan Fang,
Linhai Zhang, Yulan He, Deyu Zhou, Pengjun Xie, and Fei Huang. 2025. Web-
Walker: Benchmarking LLMs in Web Traversal. InProceedings of the 63rd Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).
[33] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li
Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, Ahmed Hassan Awadallah,
Ryen W White, Doug Burger, and Chi Wang. 2024. AutoGen: Enabling Next-
Gen LLM Applications via Multi-Agent Conversations. InFirst Conference on
Language Modeling.
[34] Tongtong Wu, Yanming Li, Ziye Tang, Chen Jiang, Linhao Luo, Guilin Qi, Shirui
Pan, and Gholamreza Haffari. 2026. CARD: Towards Conditional Design of
Multi-agent Topological Structures. InInternational Conference on Learning Rep-
resentations.
[35] T. Xu, X. Yu, A. J. Perlik, W. F. Tobin, J. A. Zweig, K. Tennant, T. Jones, and Y.
Zuo. 2009. Rapid formation and selective stabilization of synapses for enduring
motor memories.Nature462, 7275 (2009), 915–919.
[36] An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu,
et al. 2025. Qwen2.5 Technical Report. arXiv:2412.15115
[37] Chih-Hsuan Yang, Anjir Ahmed Chowdhury, Cheng-Hau Yang, Weijian Zheng,
Fernando Llorente, Xiaolong Ma, Xinyang Li, Eliu A. Huerta, Ian T. Foster, and
Rajeev Thakur. 2026. Wrong but Useful: Trajectory Value Beyond Answer
Correctness in Multi-Agent Messages. arXiv:2608.14375
[38] Bin Yu, Xinming Wang, Shijie Lian, Haotian Li, Changti Wu, Ruina Hu, Bail-
ing Wang, Yuliang Wei, and Kai Chen. 2025. TrajSelector: Harnessing Latent
Representations for Efficient and Effective Best-of-N in Large Reasoning Model.
arXiv:2510.16449
[39] Jinxi Yu, Yubei Li, Eric Hanchen Jiang, Zhi Zhang, Dong Liu, Wenxiao Zhao,
Levina Li, Kai-Wei Chang, and Ying Nian Wu. 2026. Codebook Agent: Amortized
Topology Design for LLM Multi-Agent Systems. arXiv:2609.02264
[40] Cenwei Zhang, Teng Fang, Yuxia Wang, Derek Li, Bryan Dai, and Lei
You. 2026. Best-of-Evidence: Best-of-N Selection under Partial Verification.
arXiv:2607.20950
[41] Guibin Zhang, Luyang Niu, Junfeng Fang, Kun Wang, Lei Bai, and Xiang Wang.
2025. Multi-agent Architecture Search via Agentic Supernet. InProceedings of
the 42nd International Conference on Machine Learning.
[42] Guibin Zhang, Yanwei Yue, Zhixun Li, Sukwon Yun, Guancheng Wan, Kun Wang,
Dawei Cheng, Jeffrey Yu, and Tianlong Chen. 2025. Cut the Crap: An Economical
Communication Pipeline for LLM-based Multi-Agent Systems. InInternational
Conference on Learning Representations.
[43] Guibin Zhang, Yanwei Yue, Xiangguo Sun, Guancheng Wan, Miao Yu, Junfeng
Fang, Kun Wang, Tianlong Chen, and Dawei Cheng. 2025. G-Designer: Archi-
tecting Multi-agent Communication Topologies via Graph Neural Networks. In
Proceedings of the 42nd International Conference on Machine Learning.
[44] Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, XiongHui Chen, Jiaqi
Chen, Mingchen Zhuge, Xin Cheng, Sirui Hong, Jinlin Wang, Bingnan Zheng,
Bang Liu, Yuyu Luo, and Chenglin Wu. 2025. AFlow: Automating Agentic

Yaxin Gong et al.
Workflow Generation. InInternational Conference on Learning Representations.
[45] Lunjun Zhang, Arian Hosseini, Hritik Bansal, Mehran Kazemi, Aviral Kumar, and
Rishabh Agarwal. 2025. Generative Verifiers: Reward Modeling as Next-Token
Prediction. InThe Thirteenth International Conference on Learning Representa-
tions.
[46] Han Zhou, Xingchen Wan, Ruoxi Sun, Hamid Palangi, Shariq Iqbal, Ivan Vulić,
Anna Korhonen, and Sercan Arik. 2026. Multi-Agent Design: Optimizing Agents
with Better Prompts and Topologies. InInternational Conference on Learning
Representations.
[47] Mingchen Zhuge, Wenyi Wang, Louis Kirsch, Francesco Faccio, Dmitrii
Khizbullin, and Jürgen Schmidhuber. 2024. GPTSwarm: Language Agents as Op-
timizable Graphs. InProceedings of the 41st International Conference on Machine
Learning.
A Reproducibility and Supplementary Tables
A.1 Data and splits
Table 2 in the main text lists the datasets and splits. Splits are
taken over questions rather than edges so that the candidates of a
question never straddle a boundary. ToolBench had no split field in
the archive, so we added one with the same70/15/15ratio under
a fixed seed and froze it before any evaluation; its validation and
test portions are then evaluated as a single held-out split of230
requests, and every quantity that the other benchmarks select on
validation is selected within the ToolBench training split instead.
Plan execution on PlanCraft.The inventory is parsed from the
item–count lines of the prompt, and the crafting sequence is read
from the workflow’s final answer as a list of item names. The
checker executes that sequence one step at a time against the bench-
mark’s own recipe library: for each item it reads the recipe, counting
required quantities from the occurrences of each key in the pat-
tern for shaped recipes and from the ingredient list for shapeless
ones, then consumes the ingredients and adds the product when
the inventory holds enough. A plan scores1when every step is
executed this way and the target item ends up in the inventory. For
the infeasible instances a reachability search over the same library
establishes that no sequence produces the target, and the workflow
must report the task as impossible. A final answer from which no
crafting sequence can be parsed scores0, the same convention the
other benchmarks use for unparsable output.
ToolBench contributes all765solvable requests in the six subsets
of StableToolBench. Both skeletons are four-node workflows, three
sub-task nodes and one aggregator, and the candidate edges are
the forward edges missing from the skeleton. Tool-enabled nodes
first issue tool calls and then generate their outputs from the re-
turned API content. Table 11 lists every skeleton as an adjacency
list (receiver:{sources}; nodes with no incoming edge omitted), with
the|C| column counting the candidate edges Eq. (1) admits on that
skeleton. The scan families name the generator rather than the
shape of each instance: the parallel-spine generator (Chain) degen-
erates to a diamond at𝑁=4and becomes parallel chains that merge
at the terminal for𝑁∈{ 8, 12}, and the density-sampled generator
(Dense) degenerates to a linear chain at𝑁=4and acquires multiple
ancestors per node as𝑁grows.
On the four reasoning benchmarks the skeletons admit three
candidate edges (two on PlanCraft). At deployment the method
selects and executes one edge per question; the edge is chosen
by𝜌 before any candidate is executed, so no candidate-execution
information leaks into the selection. The offline probe pool executes
two edges per question across all14,280questions—the two ranked
first by the receiver’s distance to the terminal—giving14 ,280×
2 = 28,560executed edges; the learned components are fit on
the training split alone. Always opens all candidate edges of each
question in one execution.
Table 11: Skeletons as adjacency lists.
Skeleton Adjacency list |C|
Main experiments
MuSiQue (most frequent) 1:{0}; 2:{1}; 3:{2} 3
DROP, 2Wiki 1:{0}; 3:{1,2} 3
PlanCraft, ToolBench 1:{0}; 2:{0}; 3:{1,2} 2
Skeleton scan(Figure 3)
Chain-4 1:{0}; 2:{0}; 3:{1,2} 2
Chain-8 1:{0}; 2:{0}; 3:{0}; 4:{1}; 5:{2}; 6:{3}; 7:{4,5,6} 19
Chain-12 1:{0}; 2:{0}; 3:{0}; 4:{1}; 5:{2}; 6:{3}; 7:{4}; 8:{5}; 9:{6}; 10:{7}; 11:{8,9,10} 53
Tree-4 3:{0,1,2} 3
Tree-8 4:{0}; 5:{1,2}; 6:{3,4,5}; 7:{6} 21
Tree-12 7:{0,1}; 8:{2,3}; 9:{4,5}; 10:{6,7}; 11:{8,9,10} 55
Dense-4 1:{0}; 2:{1}; 3:{2} 3
Dense-8 1:{0}; 2:{1}; 3:{2}; 4:{3}; 5:{4}; 6:{5}; 7:{5,6} 20
Dense-12 1:{0}; 2:{1}; 3:{0,2}; 4:{3}; 5:{4}; 6:{5}; 7:{1,5,6}; 8:{0,1,7}; 9:{0,8}; 10:{0,1,6,9}; 11:{10} 46
A.2 Decisive-edge filter
This filter is defined on the offline probe pool (§A.1), which executes
two candidate edges per question on all14,280questions of the four
benchmarks, train, validation and test, giving28,560executed edges.
Learned components are fit on the training split alone; the pool
carries no end-to-end score. Of the28 ,560edges,20 ,106produce
a final answer that is byte-identical to the baseline: adopting and
rolling back score the same, an identity transformation under any
policy. The remaining8 ,454are thedecisiveedges and form the
training and evaluation unit for the selector. End-to-end task scores
are reported on the test split (Table 2) and are unaffected by this fil-
ter; only the adopt, fix and harm counts are restricted, and those are
absolute counts over the5,143questions of the pool whose output
can change. Including the non-decisive edges in selector accuracy
would only dilute differences between arms with samples that carry
no decision, and the filter is the same identity transformation for
every strategy we compare.
Table 12: Token-level cost decomposition on the four reason-
ing and planning benchmarks (per-question token counts
and multiples relative to the static skeleton).
Configuration Tokens / question Multiple
Static skeleton4,509 1.00×
Diag.+Sel.,𝑏=0.3 5,059 1.12×
Diag.+Sel.,𝑏=0.5 5,426 1.20×
Nexa 6,718 1.49×
Ours,𝑏=0.5 5,652 1.25×
Always / random / no selector 7,998 1.77×
Selector only / gain regressor8,174 1.81×
Tuned LLM judge 8,928 1.98×
Ours,𝑏=1.0 6,795 1.51×
self-consistency 13,527 3.00×

Locating and Closing Information Gaps in Multi-Agent Systems
Table 13: The process-evidence block𝜙 𝑞,𝑒.
Field Definition Range
Paired text
Message content delivered along edge text
Receiver before receiver answer in𝜏𝑞 text
Receiver after receiver answer in𝜏 𝑞(𝑒,𝑚)text
How far the receiver moved
Revised receiver’s answer changed {0, 1}
Addedmin(|𝐴|,60)/60[0,1]
Dropped min(|𝐷|,60)/60 [0,1]
Churn|𝐴∪𝐷|over the union of both answers[0,1]
Where the revision came from
From message |𝐴∩(𝑀\𝑃)|/|𝐴| [0,1]
From prior context|𝐴∩𝑃|/|𝐴| [0,1]
From neither |𝐴\(𝑀∪𝑃)|/|𝐴| [0,1]
Numbers from message|𝐴 𝑛∩𝑀𝑛|/|𝐴 𝑛| [0,1]
Numbers from neither |𝐴𝑛\(𝑀 𝑛∪𝑃𝑛)|/|𝐴 𝑛| [0,1]
Number conflict𝐴 𝑛,𝑀𝑛 ≠∅and𝐴 𝑛∩𝑀𝑛 =∅{0, 1}
Displaced prior |𝐷∩𝑃|/|𝐷| [0,1]
Message novelty|𝑀\𝑃|/|𝑀| [0,1]
Whether the revision survived
Propagation reach share of downstream nodes whose output moved [0,1]
Survived to output|𝐴∩(𝑀\𝑃)|in final answer /|𝐴| [0,1]
Final carries message (𝑀\𝑃)present in final answer {0, 1}
Final changed final outputs differ {0, 1}
A.3 Selector implementation
The adoption selector is a 7B model trained with DPO on preference
pairs (training labels are derived from reference answers). Its input
contains the question, the original answer, the candidate answer
produced by the trial, and the process-evidence block recorded
during that trial. It scores three outcomes, beneficial, neutral and
harmful, and the action taken at deployment is binary, to adopt the
candidate answer or to retain the original. It is trained on the train-
ing split only, with the validation split used for checkpoint selection.
Both stages train a LoRA adapter with the backbone weights frozen,
at rank16, 𝛼= 32and dropout0 .08, applied to the seven attention
and feed-forward projections; preference optimisation continues
on the same adapter weights, and the reference policy is the frozen
supervised one. At inference, no reference answer is used: head-
room enters as ˆ𝑟, never as the true𝑟, and the selector input contains
no gold. Inference runs locally rather than through an external API,
taking roughly0.3s per question on a single GPU and is already
priced into the cost column reported in §5.1.
A.4 Process-evidence fields
Table 13 lists the evidence block in full, in the three groups of §4.2.
Write𝐴 for the content words the receiver added and𝐷 for those it
dropped,𝑀 for the content words of the delivered message, and𝑃
for those of the receiver’s pre-existing context, that is, the outputs
of its parents in the original graph; content words are normalised
tokens longer than three characters, and numbers are extracted sep-
arately as their own sets, with a subscript𝑛 marking the quantities
read over numbers alone and the three paired texts truncated to
300characters. Every quantity is computed from the two archived
traces, none reads a reference answer, and the rendering is identical
at training and inference time. The ablations in §5.3 remove the
block entirely inw/o process evidenceand, inw/ shuffled process, pair
each query with another query’s block while leaving the block itself
intact, keeping format and length statistics of the input unchanged.
A.5 Baselines
All methods are deployed on the same workflow skeletons and face
the same questions and the same splits, and each published method
runs its own decision procedure as described in its paper.
Always adds all of a question’s candidate edges at once and
re-executes the receivers and their descendants once, rather than
trialling single edges separately and selecting among the results;
Random opens one at random; Self-consistency spends the budget
on re-running the workflow and voting; Judge is a tuned gpt-4o-
mini that compares the base and candidate final answers for each
candidate edge and decides whether to adopt; Regressor regresses
the gain from the same features and adopts the candidate with the
highest positive predicted gain. MOC widens the receptive field
uniformly, with no per-question decision and no rollback. Nexa
predicts a sparse communication graph per question after the base
execution, with its threshold tuned on the validation split, and
cannot withdraw it; Nexa+ rollback attaches our adoption step
to the same predicted graph. MAS-ProVe is a study across verifier
types, verification granularities and context scopes rather than a
single rule; we instantiate the configuration it reports as strongest
on multi-agent reasoning, a learned process verifier at agent-level
granularity taking the terminal agent’s context as input. Consilience
calibrates an acceptance threshold on the validation split and falls
back to no intervention below it. DoVer localises failed base runs
without gold and intervenes only there, keeping a change only
when the trace shows it reached the final output. Best-of-Evidence
votes over the pool at zero budget and spends its budget on the
questions whose vote is closest.
A.6 Evaluation protocol
The splits are disjoint at the question level, and no ground-truth𝑟
ever enters a prompt. The training split fits every learned compo-
nent, the validation split is used only for checkpoint selection, and
the test split is evaluated exactly once. On ToolBench, which has no
separate validation split, checkpoint selection is performed within
the training split. Hyperparameters were fixed once in advance
(SFT:3epochs at lr2 ×10−5; DPO:3epochs at lr5 ×10−6, 𝛽=0.1;
a rank-16LoRA adapter in both stages) and were never revisited
against the test split; the adoption threshold is fixed at zero and
needs no tuning. The split seed is fixed and a leak audit confirms
no overlap between test and training files. The test splits contain
2,142questions on the four benchmarks and230on ToolBench,
with1,225decisive edges in the former (5,950for fitting and1 ,279
for validation). We exclude the base-versus-candidate similarity
of the final outputs from the propagation classifierℎ𝜂, since that
quantity encodes the label it is meant to predict.
A.7 Paired differences against every competitor
Table 14 reports the paired difference between SPLICE and every
competitor on both workloads under95%paired-bootstrap confi-
dence intervals computed over questions.

Yaxin Gong et al.
Table 14: Paired differences against every competitor.
ToolBench(𝑛=230) Four bench.(𝑛=2,142)
vs. 𝑏=0.5 Full 𝑏=0.5 Full
Static+.0509 +.0758 +.0280 +.0466+.0725 +.0227 +.0377+.0452 +.0304 +.0447+.0524 +.0369
Always +.0342+.0554 +.0135 +.0299+.0499 +.0101 +.0307+.0377 +.0238 +.0376+.0457 +.0297
Random+.0472 +.0719 +.0215 +.0429+.0678 +.0174 +.0354+.0422 +.0290 +.0423+.0489 +.0354
Self-cons. +.0574+.0849 +.0308 +.0531+.0810 +.0265 +.0339+.0414 +.0266 +.0408+.0485 +.0332
Judge+.0232 +.0394 +.0074 +.0189+.0346 +.0062 +.0250+.0308 +.0189 +.0319+.0384 +.0253
Regressor +.0284+.0466 +.0104 +.0241+.0418 +.0077 +.0223+.0279 +.0164 +.0292+.0354 +.0227
MOC+.0258 +.0437 +.0089 +.0215+.0382 +.0069 +.0201+.0262 +.0139 +.0270+.0342 +.0198
Nexa +.0342+.0554 +.0135 +.0299+.0499 +.0101 +.0265+.0324 +.0205 +.0335+.0400 +.0269
Nexa+rb.+.0243 +.0455 +.0036 +.0200+.0400 +.0002 +.0213+.0272 +.0153 +.0283+.0348 +.0217
MAS-ProVe +.0276+.0456 +.0094 +.0233+.0408 +.0075 +.0149+.0198 +.0100 +.0218+.0270 +.0165
Best-of-Evid.+.0437 +.0674 +.0198 +.0394+.0633 +.0157 +.0224+.0281 +.0167 +.0293+.0357 +.0229
DoVer +.0437+.0674 +.0198 +.0394+.0633 +.0157 +.0294+.0360 +.0228 +.0363+.0432 +.0292
Consilience+.0455 +.0700 +.0210 +.0412+.0659 +.0169 +.0164+.0219 +.0109 +.0233+.0290 +.0176
A.8 Verifiable instances of a closed gap
We illustrate two gap types with archived cases from PlanCraft and
ToolBench. Each case identifies a source-held fact missing from the
receiver’s upstream context and shows how delivering it changes
the receiver’s reply and the final answer. The PlanCraft case con-
nects parallel branches; the ToolBench case bypasses intermediate
nodes that omitted an API payload.
A recipe one branch away (PlanCraft,1 → 2).The skeleton
is0 → {1, 2} →3: node 1 expands the recipe tree and node 2
analyses the inventory gap, with no edge between them. For
the target cracked_stone_bricks, node 1 produced the recipe,
“cracked_stone_bricks (craftable intermediate) ⌞ stone_bricks (raw
material)”. Node 2, reconstructing the recipe on its own, added
a requirement that the recipe does not contain: “known crafting
recipe: cracked_stone_bricks are obtained by smelting stone_bricks
in a furnace . . . stone_bricks: 1 (enough)”, then failed the furnace
check, and the workflow answered IMPOSSIBLE. With the edge
opened, node 2 reads the recipe and writes “required direct ingredi-
ent: stone_bricks . . . stone_bricks: 1 (available, count sufficient)”; the
final answer becomes “Craft cracked_stone_bricks from stone_bricks
in inventory”. The single fact that moved along the edge is which
ingredients the recipe actually requires.
An API payload that never reached the synthesiser (ToolBench,
0→ 3).This instance is from the test split, and it shows how the
gap takes the form of a retrieved Web payload rather than a derived
fact. The ToolBench workflow runs in two stages: the execution
node first issues the tool calls and receives the live API responses,
and the terminal node then synthesises a reply from those responses.
Asked to generate a captcha image and a UUID and then verify the
captcha, node 0 called the captcha service and recorded its return,
including the server-generated identifier “2961c533-b254-4d48-8a0a-
234ca85ef250” and the base64 PNG of the captcha image. The termi-
nal node’s upstream input is the concatenation of nodes 1 and 2’s
answers and does not include node 0’s retrieved payload; since the
identifier is minted by the service and cannot be reproduced from
𝑞, the terminal answered “I currently don’t have access to any API
results to generate a captcha image or UUID”. With0 → 3opened,
the terminal reads the payload and answers “I generated a captcha
image and UUID for your friend: the UUID is “2961c533-b254-4d48-
8a0a-234ca85ef250” and the captcha image is provided as a base64
PNG data URL”. The fact that moved along the edge is the API re-
turn itself: a value the source node retrieved from the Web service
and the synthesiser had no other way to obtain.
A.9 A trial the selector rejected
This test-split instance illustrates a trial whose candidate answer
reads as more polished but which the selector correctly rejects.
The task asks for short-URL creation through two tools ( bitly
and URL Link Shortener ). In the static workflow, node 0 reports
two upstream issues verbatim: a missing access token for bitly
and incomplete URL arguments for URL Link Shortener , and
the terminal answers “. . . for creating short URLs for your social
media posts using the bitly tool, the requests failed due to a miss-
ing access token. To proceed with Bitly, you will need to provide a
valid access token for authentication.” With0 → 3opened, the mes-
sage from node 0 conveys API failure information to the terminal.
The terminal, however, omits this failure information and rewrites
the response into a smooth tutorial that no longer mentions the
failures: “you can use the bitly tool to generate short URLs for each
post . . . use bitly to create short URLs for your social media posts to
track engagement effectively.” The process evidence records that the
corrective content in the message does not survive to the final an-
swer (prov_msg_reached_final=0), that76%of the new content
is traceable neither to the message nor to the receiver’s prior con-
text (prov_added_invented=0.76), and that the receiver rewrote
roughly69%of its answer ( prov_receiver_churn=0.69). Against
a predicted base score ˆ𝑟𝑞=0.94, the selector returns ˆ𝑝𝑏 =0.37and
ˆ𝑝ℎ=0.06, giving Δ= 0.37(1−0.94)− 0.06· 0.94 =− 0.0342 < 0;
SPLICE therefore retains the original answer. Against the reference
labels this trial would have cost−1.00in task score, and the three-
class process evidence shows the receiver rewrote without using
the message.
A.10 Evidence-support protocol
On the230held-out ToolBench questions, two independent judges
(DeepSeek-v4-pro and Claude-opus-4-6), distinct from the work-
flow backbone and selector, receive the question, one candidate
answer, and the API response bodies replayed by StableToolBench
during that execution. Each concrete claim (a number, name, date,
or URL) is labelled supported if a response matches it, partially
supported if a response is related but does not fully match, and
unsupported if no response backs it. The three rates are computed
over all claims and sum to one; task completion separately mea-
sures whether each answer fulfils the request. Judges are blind to
method identity. Reported results average the two judges, with95%
bootstrap intervals. A manual re-check of a random subsample
yields0.90per-claim agreement between human and judge labels.
