---
title: 'HyMem: Hierarchical Context Management for Long-Horizon Agents via Information Isolation'
url: https://arxiv.org/abs/2608.15703
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- XinQi Wang
- Jinwei Xiao
- Sijia Cui
- Hongming Zhang
- Yanna Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.15703
pages: 16
chars: 59684
fetched_at: '2026-11-08T13:35:07+00:00'
kb_version: 1
---

# HyMem: Hierarchical Context Management for Long-Horizon Agents via Information Isolation

HyMem: Hierarchical Context Management for Long-Horizon Agents via
Information Isolation
XinQi Wang1,2,3,*, Jinwei Xiao1,2,*, Sijia Cui1,2, Hongming Zhang1, Yanna Wang1, Qingyang Zhang1, Bo Xu1,3
1National Key Laboratory of Cognition and Decision Intelligence for Complex Systems,
Institute of Automation, Chinese Academy of Sciences
2University of Chinese Academy of Sciences
3Nanjing Artificial Intelligence Research of IA
*Equal Contribution
wangxinqi2024@ia.ac.cn
Abstract
Large language model (LLM) agents often per-
form poorly on complex, long-horizon tasks be-
cause their context becomes increasingly clut-
tered over time. As interactions accumulate, de-
tailed execution traces and intermediate outputs
dominate the context, making it difficult for the
model to retain and use high-level planning
information. Most existing methods address
this issue through compression or retrieval ap-
plied to a single, flat context, which does not
clearly separate different types of context in-
formation and often leads to degraded reason-
ing. To address this challenge, we propose
HyMem, a hierarchical framework that explic-
itly separates the agent’s context into distinct
functional layers. HyMem organizes context by
function to separate high-level planning from
execution and complex analysis. Its isolated
reasoning module handles complex subtasks
without adding intermediate reasoning traces
to the persistent planning context, while its
memory management module preserves task
progress across context refreshes through struc-
tured summaries. These components reduce
redundant context accumulation, retain task-
critical information, and support coherent long-
horizon reasoning within a limited context win-
dow. Experiments on GAIA and Browsecomp-
plus show that, with DeepSeek-V4, HyMem
achieves average Pass@1 scores of 66.7% and
61.3%, outperforming the strongest baseline by
6.1 and 4.7 percentage points, respectively. Fur-
ther analysis indicates that HyMem effectively
controls the growth of the reasoning context,
allowing the model to maintain focus and accu-
racy across complex, long-horizon tasks.
1 Introduction
Large Language Model-based agents have demon-
strated remarkable capabilities in tackling intri-
cate, long-horizon tasks across scenarios requir-
ing extensive environmental interaction, such as
graphical user interface manipulation (Qin et al.,
3 6 9 12 15
Reasoning step
0.0
2.5
5.0
7.5Key-info density of context (%)
0 20k 40k 60k
1
5
10
14
19
24 step
1.6%
5.8%
0.8%
1.5%
1.7%
1.9%
ReAct  score=0
0 1k 2k 3k
Context position (tokens)
1
2
3
4
5 step
3.6%
9.2%
8.9%
12.0%
12.8%
HyMem  score=1
Key information is a smaller fraction
of context under ReAct One task: the same key fact across steps
key-info tokens other context tokens end of context
Figure 1:Changes in task-critical information within
the agent context.As the context length increases,
effective task signals are diluted by redundant historical
information, reducing the agent’s sensitivity to core
constraint information. The left panel shows changes in
task-critical information during task execution on GAIA
by agents using ReAct and HyMem, respectively. The
right panel illustrates the changes in the position and
density of ReAct and HyMem within the context in a
task example.
2025; Tang et al., 2025), in-depth research investi-
gation (Wei et al., 2025; Jin et al., 2025; Li et al.,
2025b; OpenAI, 2025; Google, 2025), and web-
based information retrieval (Zhou et al., 2023; Li
et al., 2025d; Qiao et al., 2025; Cui et al., 2025).
However, when facing scenarios that mirror the
complexity of real-world tasks—necessitating a
seamless integration of macro-strategic planning
and micro-tool manipulation—LLM-based agents
still encounter significant challenges. A critical
bottleneck emerges from the structural mismatch
between the agent’s cognitive processes and its con-
text management. Long-horizon and complex tasks
inherently involve different information streams:
high-level strategic planning which requires stabil-
ity and continuity, low-level execution traces which
are often noisy and transient (Zhao et al., 2024; Yu
et al., 2025; Yang et al., 2025b; Zhao et al., 2025;
Zhang et al., 2024). In standard flat context ar-
chitectures (e.g., ReAct (Yao et al., 2023)), these
1
arXiv:2608.15703v1  [cs.AI]  16 Aug 2026

distinct streams are interleaved into a single se-
quence. As shown in Figure 1, the redundancy
information from execution steps rapidly accumu-
lates, creating an "information flood" that dilutes
and eventually submerges the sparse but critical
signals of the strategic plan. This leads the agent
to lose track of its original goal amidst the details
of tool usage.
Prior approaches have attempted to mitigate con-
text constraints through techniques such as context
compression (Yan et al., 2025; Zhang et al., 2025;
Yang et al., 2024; Wang et al., 2025; Zhou et al.,
2025) or external memory retrieval (Yang et al.,
2026; Leng et al., 2024; Xu et al., 2025a; Li et al.,
2025c; Chhikara et al., 2025; Zhang et al., 2023).
However, these methods typically operate on a pre-
mixed flat sequence, making it difficult to distin-
guish the underlying reasoning signal from the exe-
cution noise. Specifically, compression often leads
to the loss of critical reasoning chains, and external
memory retrieval frequently fails to preserve tem-
poral logic and struggles to differentiate between
high-level strategic planning and discrete execution
steps. Ultimately, these strategies merely address
the symptom of context length rather than the root
cause: the way different types of information are
mixed together in a single sequence.
To address the challenges, we propose HyMem,
a framework that enforces hierarchical manage-
ment and isolation between reasoning layer and
execution layer. Instead of treating context as
a passive log of past interactions, HyMem man-
ages it deliberately to keep only what is useful for
decision-making. By decoupling high-level strate-
gic planning from low-level execution details, the
framework encapsulates noisy interaction loops
within a dedicated Action Layer, ensuring that
the Planner Layer context remains clean and fo-
cused on high-value strategic signals. This source-
level isolation fundamentally blocks the propaga-
tion of redundant execution information into the
decision-making space, allowing for sustained rea-
soning clarity. Complementing this, HyMem uses
a structured compression method to summarize
past interactions into concise representations, re-
ducing context size while preserving essential task
information. As a training-free solution for the
long-horizon reasoning task, HyMem offers seam-
less, plug-and-play convenience for complex, long-
horizon tasks.
To validate the effectiveness of the HyMem
framework, we conducted systematic evaluations
on two representative benchmark datasets, cover-
ing complex information retrieval tasks as well as
general-purpose agent reasoning tasks. HyMem
improves average Pass@1 over the strongest base-
line by 6.1 percentage points on GAIA and 4.7
percentage points on Browsecomp-plus (Wu et al.,
2025b; Lu et al., 2025; Zhou et al., 2025; Yu et al.,
2025). On hard Browsecomp-plus tasks, Pass@1
increases from 14.0% to 30.0%. Ablation stud-
ies show that isolated reasoning is important for
long-horizon tasks: removing this module consis-
tently lowers task success, indicating that complex
subtask analysis should remain separate from the
persistent planning context. Structured memory
serves a complementary role by preserving task
goals, completed milestones, and reusable tool ex-
perience across context refreshes. These findings
suggest that effective long-horizon context manage-
ment requires both selective information isolation
and continuity preservation, rather than context
compression alone. Furthermore, analysis of con-
text length trajectories reveals that the HyMem ar-
chitecture’s global specification inference capabil-
ity is less affected by redundant information during
execution, demonstrating its potential for sustained
reasoning and extensive exploration in complex,
long-threaded tasks.
In summary, our contributions are as follows:
(1) We formalize context dilution in long-horizon
agents as an information-density mismatch
between sparse planning signals and dense
execution traces, and introduce hierarchical
context isolation as the guiding principle.
(2) We instantiate this principle in HyMem, a
training-free framework that separates plan-
ner, executor, isolated subtask reasoning, and
structured memory management through ex-
plicit information boundaries.
(3) We evaluate HyMem on Browsecomp-plus
and GAIA against several methods. HyMem
achieves average Pass@1 scores of 61.3%
and 66.7%, outperforming the strongest base-
line by 4.7 and 6.1 percentage points, respec-
tively, while maintaining comparable token
consumption and tool-call counts.
2 Related Work
LLM-based Agent Frameworks.LLM-based
agents have been widely studied as systems that
combine language-model reasoning with tool use
2

(b) Executor Layer
PLANNING
(a) Planner Layer
task subtask subtask
Tools
Quality Assessment
complex
subtask
easy
subtask
Result
complete Result
Execute
task
Executor
Result
(c) Isolated reasoning module
previous Planner context
complex
subtask
ToolsReasoning
×m
(d) Memory Management module
Planner & Executor
layer history
Auxiliary LLM
Auxiliary LLM
episode memory
task_description:....
event_1:....
event_2:....
working memory
goal&challenge:....
action_1:....
action_2:....
tool memory
tool_name:....
turn_1:....
turn_2:....
compress
Planner Layer context
Planner context Executor context
Memory
update
Redundant
process information
Result&Evidence
Reasoning
Info.
Query:
between 1990 and 1994 inclusive,
what teams played in a soccer
match with   ........and four
substitutions, one of which was for
an injury in the first 25 minutes of
the match.
HyMem
Answer:
Ireland v Romania
END
Figure 2: Overview of the HyMem framework. Upon query arrival, the PLanner Layer (a) performs task de-
composition and iterative planning. Sub-tasks are routed to the Executor Layer (b) for execution within isolated
reasoning spaces (c) based on complexity, returning refined results for strategic synthesis. Simultaneously, the
framework maintains context efficiency by compressing historical trajectories into structured episode, working, and
tool memories in (d), which are re-injected to ensure long-horizon task continuity and reasoning focus.
and environmental interaction (Wang et al., 2023a;
Team, 2025; Jin et al., 2022). Representative
frameworks such as ReAct (Yao et al., 2023),
Plan-and-Solve (Wang et al., 2023b), and Re-
flexion (Shinn et al., 2023) improve task solving
by making intermediate reasoning, action selec-
tion, planning, or self-reflection explicit. Recent
agent systems further extend this paradigm to web
search, GUI control, and long-horizon information-
seeking tasks (Yang et al., 2025b; Wu et al., 2025a;
Li et al., 2025a). Closely related to our work,
THREAD (Schroeder et al., 2025) explores recur-
sive child threads for deeper subtask reasoning.
These methods demonstrate the value of structured
reasoning workflows, but they mainly focus on
how agents decompose, execute, or reflect on tasks.
HyMem instead focuses on how information should
be separated during execution: high-level planner,
tool interaction, and deep subtask reasoning are
placed in different context spaces, and only syn-
thesized results are returned to the main decision
context.
Agent Memory and Context Management.An-
other line of work improves long-horizon agents
through memory construction, retrieval, summa-
rization, or learned context management (Mei
et al., 2025). External memory systems such as
A-MEM (Xu et al., 2025a), Mem0 (Chhikara et al.,
2025), and MemOS (Li et al., 2025e) organize
reusable information outside the immediate con-
text and retrieve relevant memories when needed.
Intra-task context management methods such as
ReSum (Wu et al., 2025b), MemAgent (Yu et al.,
2025), MEM1 (Zhou et al., 2025), AgentFold (Ye
et al., 2025), and context-folding approaches (Sun
et al., 2025) compress or learn to retain useful tra-
jectory information during long tasks. These ap-
proaches reduce context pressure, but they usually
operate on trajectories where planning signals and
execution traces have already been mixed, or re-
quire additional training to learn memory opera-
tions. HyMem is complementary to these meth-
ods: it uses structured memory to preserve task
continuity, but its central mechanism is architec-
tural context isolation, which reduces the amount of
low-level execution noise that reaches the planner
context in the first place.
3 Methodology
As illustrated in Figure 2, HyMem is a training-free
inference-time controller for long-horizon LLM
agents. Its central design principle is typed con-
text isolation: planning, tool execution, isolated
sub-task reasoning, and memory consolidation are
maintained in separate context spaces, and only
schema-constrained messages are allowed to cross
3

their boundaries. This design prevents raw exe-
cution traces and intermediate deliberation tokens
from being directly appended to the main planning
context, while preserving task continuity through
structured memory.
3.1 Problem Formulation
We consider an LLM-based agent that solves a user
query q through iterative interaction with an envi-
ronment E. At step t, the agent emits an action
or reasoning output at and receives an observation
ot ∈ O. A conventional ReAct-style agent main-
tains a flat context:
Ct =

P, q,(a1, o1), . . . ,(at, ot)

,(1)
where P is the system prompt and all items are
concatenated as tokens.
The information in Ct is heterogeneous. We use
two functional projections to describe this struc-
ture:
Zt =π Z(Ct),
Xt =π X (Ct). (2)
where πZ(·) denotes a conceptual selector that
extracts planning-relevant information from the
context, πX (·) denotes a selector for execution-
level traces. Zt contains planning-relevant informa-
tion such as goals, verified facts, constraints, and
unresolved sub-goals, while Xt contains execution-
level traces such as raw tool outputs, browsing logs,
retries, formatting artifacts, and failed attempts.
In long-horizon tasks, |Xt| typically grows faster
than |Zt|, reducing the relative density of planning-
relevant information:
ρt = |Zt| |Ct| .(3)
We refer to this reduction ascontext dilution. Fig-
ure 1 empirically measures this phenomenon by
tracking task-critical information across reasoning
steps.
HyMem aims to update the planner only through
distilled typed messages. Let Rt denote the struc-
tured return from a lower-level context space. The
intended information boundary is:
C(p) t+1 =U(C (p) t , Rt),
I(C (p) t+1;X t |R t)≈0. (4)
U(·) is the planner-state update function, and
I(A;B|C) denotes conditional mutual informa-
tion. Eq. 4 is not optimized as a differentiable
objective. It is enforced by the interface design:
raw execution traces are kept inside lower-level
contexts and only schema-constrained returns are
appended to the planner.
3.2 HyMem Framework
HyMem contains two context spaces: Planner, Ex-
ecutor, and two modules: isolated reasoning mod-
ule, and Memory Management module. Only the
planner persists across the whole task. Another
spaces are instantiated on demand, return a typed
message, and discard their private context.
Planner.The planner maintains the main deci-
sion context:
C(p) t =  P (p), q,Mepi t ,M wm t ,M tool t , H(p) t  ,
(5)
where Mepi is episode memory, Mwm is work-
ing memory, Mtool is compact tool memory, and
H (p) t stores only typed returns from previous sub-
sessions. The planner emits exactly one action
from:
A={⟨TASK⟩(d),⟨ISOREASON⟩(d),
⟨FOLD⟩,⟨ANSWER⟩(ˆy)}. (6)
Executor.Given a tool-use directive d, HyMem
creates a fresh executor context:
C(e) t,0 = (P (e), d,Mtool t ).(7)
The executor performs a bounded tool-call loop
and obtains raw observations ot,1, . . . , ot,k. These
observations are not returned directly. HyMem first
applies a relevance-conditioned distillation opera-
tor:
˜ot,j =ϕ(o t,j |d),(8)
where ϕ removes navigation text, duplicated pas-
sages, formatting artifacts, irrelevant snippets, and
tool-error boilerplate while preserving named en-
tities, dates, numerical values, source identifiers,
evidence snippets, and answer candidates. The
distilled observations are then synthesized into:
R(e) t =⟨RESULTS⟩
[findings,evidence,sources,
status,gaps]
⟨/RESULTS⟩.
(9)
Only R(e) t is appended to the planner history. The
executor context and raw observations are dis-
carded after return.
4

Isolated reasoning.For sub-tasks requiring
multi-hop analysis, hypothesis checking, or recon-
ciliation of conflicting evidence, the planner emits
⟨ISOREASON⟩(d). HyMem then creates:
C(iso) t,0 =  P (iso), d,M epi t ,M wm t ,
Mtool t , τ(H(p) t )  . (10)
where τ(·) selects the recent planner state needed
to ground the sub-task. The isolated session may
call the executor for additional evidence, but its
intermediate reasoning trace remains private. It
returns:
R(iso) t =⟨RETURN⟩
[conclusion,supporting facts,sources,
confidenceκ,assumptions]
⟨/RETURN⟩.
(11)
where κ∈[0,1] is the self-estimated confidence.
After return, the isolated context is discarded.
Structured memories.HyMem maintains three
rewritable memories:
Mt ={M epi t ,M wm t ,M tool t }.(12)
Episode memory records completed milestones,
verified facts, and important decisions. Working
memory records the current objective, unresolved
gaps, and next-step plan. Tool memory records
effective tool-use patterns, failed queries, and tool-
specific caveats. The fold operator rewrites all
memories jointly:
Mt+1 = Φ(H (p) t , H(e) ≤t , H(iso) ≤t ,M t).(13)
HyMem uses asymmetric memory injection:
C(p) ←(M epi,M wm,M tool),
C(iso) ←(M epi,M wm,M tool),
C(e) ← Mtool.
(14)
The tool memory injected into the planner is a com-
pact procedural summary, not raw tool logs. This
preserves reusable tool experience while keeping
raw execution traces outside the planner.
3.3 Inference Procedure and Context
Boundary
HyMem wraps a frozen base LLM πθ at inference
time. At planner stept:
at ∼π θ(· |C(p) t ), at ∈ A.(15)
The transition is:
at =⟨TASK⟩(d)⇒C (p) t+1 ←U  C (p) t , R(e) t  ,
at =⟨ISOREASON⟩(d)⇒C (p) t+1 ←U  C (p) t , R(iso) t  ,
at =⟨FOLD⟩or Trigger(s t)⇒ Mt+1 ←Φ(·),
at =⟨ANSWER⟩(ˆy)⇒return ˆy.
(16)
A fold is invoked when the planner explicitly
emits ⟨FOLD⟩ , or when one of the following deter-
ministic conditions is met:
Trigger(st) = [rctx t >0.99]∨[n exec t ≥5]
∨[n fail t ≥3]∨[n turn t ≥8]
∨[n tool t ≥10].
(17)
Here, rctx t is planner-context token utilization,
nexec t counts executor invocations since the last
fold, nfail t counts consecutive executor failures,
nturn t counts planner turns since the last fold, and
ntool t counts tool calls since the last fold.
The context boundary follows from the transition
rules. Raw observations enter only the executor
and are deleted after R(e) t is returned. Intermediate
reasoning tokens enter only the isolated reason-
ing context and are deleted after R(iso) t is returned.
The planner grows through bounded typed returns
and rewritten memories, rather than through the
full length of tool traces or sub-task deliberations.
Therefore, HyMem does not merely summarize
a flat trajectory after it becomes long; it restricts
which information can enter the decision context
throughout execution. This mechanism underlies
the lower context-dilution behavior measured in
Figure 1.
4 Experiments
Benchmark.We evaluate HyMem using two
benchmark datasets including GAIA (Mialon et al.,
2024), and Browsecomp-plus (Chen et al., 2025).
Browsecomp-plus focuses on reasoning-intensive
queries derived from OpenAI’s Browsecomp (Wei
et al., 2025) and provides a comprehensive offline
corpus to ensure evaluation consistency without
real-time web dependency. GAIA is employed to
assess the agent’s proficiency in general reasoning,
retrieval, and tool utilization. Due to constraints in
retrieval API resources and computational time, we
randomly sampled 150 questions with a balanced
difficulty distribution from Browsecomp-plus (Sun
et al., 2025). For GAIA, the evaluation is restricted
to text-based queries.
5

Backbone Framework GAIA Browsecomp-plus
Level 1 Level 2 Level 3Avg. P@1 Easy Medium HardAvg. P@1
No Agency
Qwen3-32B Base 23.8 6.0 5.3 18.9 - - - -
DeepSeek-V4 Base 35.7 27.2 15.8 28.3 14.0 10.0 0.0 8.0
Agentic Frameworks
Qwen3-32B ReAct 19.0 10.6 0.0 11.8 70.0 24.0 2.0 32.0 Summary 30.9 21.2 5.3 22.0 20.6 46.0 14.0 2.0
DeepSeek-v4 ReAct 66.6 56.1 36.8 56.6 94.062.0 14.0 56.6 Summary 69.1 45.5 31.6 51.2 78.0 42.0 6.0 42.0
ReSum 76.2 54.5 47.4 60.6 78.0 46.0 6.0 43.3
AMEM 61.9 48.5 26.3 49.6 70.0 34.0 6.0 36.7
THREAD 42.9 34.8 26.3 35.4 42.0 30.0 8.0 26.7
Our Framework
Qwen3-32B HyMem 45.2 30.3 15.8 33.0 48.0 24.0 4.0 25.3
DeepSeek-V4 HyMem 77.0 65.2 49.1 66.7 90.064.0 30.0 61.3
Table 1: Experimental results on GAIA and Browsecomp-plus benchmarks. P@1 denotes Pass@1. The bolded
numbers represent the top performers in their respective categories. (1) HyMem improves the reasoning capabilities
of different backbone models. (2) HyMem delivers the largest overall performance improvement among the
compared agent frameworks.
Baseline and Implementation.HyMem is com-
pared against several representative methodologies:
theReActframework (Yao et al., 2023), which fa-
cilitates explicit reasoning via a continuous reason-
act-observe cycle;Summarization-basedwork-
flows (Yu et al., 2025), which condense historical
interaction trajectories into information-dense sum-
maries to guide subsequent reasoning;ReSum(Wu
et al., 2025b), which periodically summarizes long
interaction histories into compact reasoning states
to support continued long-horizon exploration;A-
MEM(Xu et al., 2025b), which constructs an agen-
tic memory system by organizing experiences into
dynamically linked and evolving memory notes;
andTHREAD(Schroeder et al., 2025), which de-
composes complex tasks through recursive thread
spawning, enabling isolated subtask reasoning and
subsequent aggregation. We evaluate two back-
bone models, Qwen3-32B (Yang et al., 2025a) and
DeepSeek-V4 (DeepSeek-AI et al., 2025). Unless
otherwise specified, the same backbone is used for
the compared framework under the same bench-
mark setting. Detailed prompts, turn budgets, and
hyperparameters are provided in the Appendix A.
4.1 Results and Analysis
Table 1 shows that HyMem achieves the strongest
overall performance when paired with the stronger
DeepSeek-V4 backbone. On GAIA, DeepSeek-V4
with HyMem reaches an average Pass@1 of 66.7,
improving over ReAct by 10.1 percentage points
and over ReSum by 6.1 percentage points. The gain
is consistent across all three GAIA difficulty levels,
with the largest margin over ReAct appearing on
Level 3 questions. On Browsecomp-plus, HyMem
reaches an average Pass@1 of 61.3, outperforming
ReAct by 4.7 percentage points and substantially
exceeding memory-oriented or modular baselines
such as ReSum, A-MEM, and THREAD.
The difficulty-wise results further clarify where
HyMem is most useful. On Browsecomp-plus
with DeepSeek-V4, HyMem is slightly lower
than ReAct on easy questions, but improves on
medium and hard questions, especially hard ques-
tions where Pass@1 increases from 14.0 to 30.0.
This pattern is consistent with the design motiva-
tion of HyMem: typed context isolation is most
beneficial when solving the task requires sustained
planning, evidence accumulation, and multi-step
verification rather than short tool-use trajectories.
The Qwen3-32B results show a more nuanced
picture. On GAIA, HyMem improves the average
Pass@1 from 11.8 under ReAct and 22.0 under the
summarization workflow to 33.0, indicating that
context isolation can help a smaller backbone sus-
tain reasoning over multi-step tasks. However, on
Browsecomp-plus, Qwen3-32B with HyMem does
not outperform the ReAct baseline. This suggests
that HyMem’s gains depend not only on context
structure but also on the underlying model’s ability
6

100 200 300 400 500
Token consumption (k)
20
30
40
50
60
70
80
Pass@1 (%)
GAIA
BrowseComp+
HyMem
ReSum
Thread
A-MEM
ReAct
Summary
(a) Token Consumption vs. Performance
101 102
Number of tool calls (log)
20
30
40
50
60
70
80
Pass@1 (%)
GAIA
BrowseComp+
HyMem
ReSum
Thread
A-MEM
ReAct
Summary (b) Tool Calls vs. Performance
Figure 3:Resource Consumption and Task Performance across Different Methods.We compare the re-
source consumption and task performance of ReAct, ReSum, A-MEM, THREAD, and HyMem on the GAIA
and BrowseComp-Plus tasks. HyMem achieves better task performance while maintaining acceptable resource
utilization.
0 20 40 60 80 100
Task progress (%)
101
102
103
104
105
Context growth from start (tokens, log)
HyMem-Planner
HyMem-Total
ReSum
A-MEM
ReAct
Figure 4:Relationship between Context Changes
and Task Progress across Different Methods.We
record the relationship between context growth trends
and task progress for ReAct, A-MEM, ReSum, and
HyMem. HyMem-Total denotes the overall context of
HyMem, while HyMem refers to the context of the
planner module.
to follow typed control instructions and produce
reliable structured returns. We therefore treat cross-
backbone robustness as promising but not uniform
across all benchmark settings.
4.2 Efficiency and Context Behavior
Figure 3 compares task performance against token
consumption and tool-call count. HyMem occu-
pies a favorable region of the performance-resource
trade-off: it achieves higher task performance than
ReAct, ReSum, A-MEM, and THREAD while
keeping resource usage within a comparable range.
This is important because HyMem introduces addi-
tional control structure, including isolated reason-
ing and memory folding. The analysis indicates
that the performance gain is not simply obtained
by unbounded context growth or excessive tool
use; rather, structured context isolation directs addi-
tional computation toward task-relevant reasoning
and evidence synthesis.
Figure 4 shows that HyMem’s advantage lies
in how context is allocated rather than in reduc-
ing total context usage. HyMem-Total continues
to grow as the Executor and Isolated Reasoning
modules perform tool interaction and multi-step
analysis, whereas the persistent Planner context
grows much more slowly. The separation between
the two curves indicates that most execution de-
tails and intermediate analysis remain within tem-
porary contexts, while only structured returns and
rewritten memories update the Planner. Compared
with methods whose persistent reasoning contexts
grow with accumulated interaction traces, HyMem
supports extensive exploration while keeping the
Planner context focused on task-relevant informa-
tion and preventing transient execution details from
accumulating throughout the task.
4.3 Ablation Study
Table 2 evaluates the contribution of the two main
components of HyMem: the Isolated Reasoning
Module and Memory Management. Removing
7

Framework Browsecomp-plus (DeepSeek-V4) GAIA (Qwen3-32B)
Pass@1 Plan. Conf. Pass@1 Plan. Conf.
HyMem (Full) 0.630012.98 0.77 0.320014.20 0.82
w/o Isolated Reasoning 0.5800(-5.00pp)10.26(-2.72)0.68(-0.09) 0.1340(-18.60pp)11.50(-2.70)0.71(-0.11)
w/o Memory Management 0.5400(-9.00pp)9.68(-3.30)0.69(-0.08) 0.1340(-18.60pp)10.12(-4.08)0.70(-0.12)
Table 2: Ablation study of HyMem. Red values(-)indicate the performance drop compared to the full framework.
isolated reasoning causes the large performance
drop, reducing Pass@1 by 5.0 percentage points on
Browsecomp-plus and 18.6 percentage points on
GAIA. This confirms that isolating deep sub-task
reasoning is crucial for long-horizon agent tasks,
especially when the main planner would otherwise
accumulate long intermediate deliberations.
Removing memory management also substan-
tially degrades performance, reducing Pass@1 by
9.0 percentage points on Browsecomp-plus and
18.6 percentage points on GAIA. This result shows
that typed isolation alone is insufficient: the agent
also needs structured memories to preserve mile-
stones, current goals, and reusable tool experience
across context refreshes. Together, the ablation
results support the two-part design of HyMem. Iso-
lated reasoning protects the planner from sub-task
deliberation noise, while memory management pre-
serves task continuity after histories are folded.
Finally, the auxiliary metrics in Table 2 help
interpret the failure modes. Without isolated rea-
soning, Pass@1 decreases on both benchmarks, in-
dicating that the agent is less effective at resolving
complex subtasks when their analysis is handled di-
rectly within the persistent planning context. With-
out memory management, confidence also drops,
indicating that losing structured task state makes
the agent less certain even when it can still execute
tools. These trends align with the proposed mecha-
nism: HyMem improves long-horizon performance
by coordinating where reasoning happens and how
task state is retained.
5 Conclusion
This paper addresses context dilution in long-
horizon LLM agents, where sparse planning-
relevant signals are gradually obscured by dense
execution traces. We proposed HyMem, a training-
free inference-time framework based on typed con-
text isolation. By separating planning, tool exe-
cution, isolated sub-task reasoning, and memory
consolidation into distinct context spaces, HyMem
restricts raw observations and intermediate delib-
eration traces from directly entering the main plan-
ning context. Structured returns and asymmetric
memory injection allow the agent to preserve task
continuity while keeping the planner focused on
verified facts, current goals, and unresolved gaps.
Experiments on GAIA and Browsecomp-plus
show that HyMem improves long-horizon agent
performance most consistently with a stronger
instruction-following backbone. With DeepSeek-
V4, HyMem achieves the best average Pass@1 on
both benchmarks and shows clear gains on harder
Browsecomp-plus questions. The resource analy-
sis further suggests that these gains are not simply
obtained by using more tokens or more tool calls,
while the context-growth analysis supports the in-
tended mechanism: HyMem allows execution and
isolated reasoning contexts to expand without pro-
portionally expanding the persistent planner con-
text. Ablation results confirm that both isolated
reasoning and structured memory management are
necessary for the full framework.
HyMem also has clear boundaries. Its effective-
ness depends on the model’s ability to follow typed
control instructions and produce reliable structured
returns, and the gains are not uniform across all
backbone and benchmark combinations. Future
work should study adaptive routing and memory-
folding policies, reduce the cost of auxiliary distil-
lation, and extend context isolation to interactive
settings where user intent may change during multi-
turn task execution.
Limitations
LLM-based agents are increasingly used for long-
horizon tasks that require iterative planning, tool
use, and information gathering. However, their per-
formance is often limited by context dilution: as
interaction histories grow, dense execution traces
such as raw tool outputs, retries, and intermedi-
ate deliberations can obscure the sparse planning
signals needed for global task control. Existing
compression and retrieval methods reduce context
length, but they usually operate after planning and
8

execution information has already been mixed into
a flat trajectory. We propose HyMem, a training-
free inference-time framework based on typed con-
text isolation. HyMem separates planning, tool ex-
ecution, isolated sub-task reasoning, and memory
consolidation into distinct context spaces, allow-
ing only schema-constrained results and structured
memories to enter the main planner context. Exper-
iments on GAIA and Browsecomp-plus show that
HyMem improves performance over ReAct, Re-
Sum, and other agent baselines while maintaining
an acceptable resource-performance trade-off.
References
Zijian Chen, Xueguang Ma, Shengyao Zhuang, Ping
Nie, Kai Zou, Andrew Liu, Joshua Green, Kshama
Patel, Ruoxi Meng, Mingyi Su, Sahel Shari-
fymoghaddam, Yanxi Li, Haoran Hong, Xinyu
Shi, Xuye Liu, Nandan Thakur, Crystina Zhang,
Luyu Gao, Wenhu Chen, and Jimmy Lin. 2025.
Browsecomp-plus: A more fair and transparent eval-
uation benchmark of deep-research agent.arXiv
preprint arXiv:2508.06600.
Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet
Singh, and Deshraj Yadav. 2025. Mem0: Building
production-ready ai agents with scalable long-term
memory.Preprint, arXiv:2504.19413.
Sijia Cui, Aiyao He, Shuai Xu, Hongming Zhang, Yanna
Wang, Qingyang Zhang, Yajing Wang, and Bo Xu.
2025. Self-guided function calling in large language
models via stepwise experience recall. InFindings
of the Association for Computational Linguistics:
EMNLP 2025, pages 10842–10854, Suzhou, China.
Association for Computational Linguistics.
DeepSeek-AI, Aixin Liu, Aoxue Mei, Bangcai Lin,
Bing Xue, Bingxuan Wang, Bingzheng Xu, Bochao
Wu, Bowei Zhang, Chaofan Lin, Chen Dong,
Chengda Lu, Chenggang Zhao, Chengqi Deng, Chen-
hao Xu, Chong Ruan, Damai Dai, Daya Guo, Dejian
Yang, and 245 others. 2025. Deepseek-v3.2: Pushing
the frontier of open large language models.Preprint,
arXiv:2512.02556.
Google. 2025. Deep research is now available on gemini
2.5 pro experimental. Technical report, Google.
Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon,
Sercan Arik, Dong Wang, Hamed Zamani, and Jiawei
Han. 2025. Search-r1: Training llms to reason and
leverage search engines with reinforcement learning.
Preprint, arXiv:2503.09516.
Jun Jin, Hongming Zhang, and Jun Luo. 2022. Build
generally reusable agent-environment interaction
models.Preprint, arXiv:2211.08234.
Quinn Leng, Jacob Portes, Sam Havens, Matei Za-
haria, and Michael Carbin. 2024. Long context rag
performance of large language models.Preprint,
arXiv:2411.03538.
Kuan Li, Zhongwang Zhang, Huifeng Yin, Rui Ye,
Yida Zhao, Liwen Zhang, Litu Ou, Dingchu Zhang,
Xixi Wu, Jialong Wu, Xinyu Wang, Zile Qiao, Zhen
Zhang, Yong Jiang, Pengjun Xie, Fei Huang, and Jin-
gren Zhou. 2025a. Websailor-v2: Bridging the chasm
to proprietary agents via synthetic data and scalable
reinforcement learning.Preprint, arXiv:2509.13305.
Xiaoxi Li, Guanting Dong, Jiajie Jin, Yuyao Zhang,
Yujia Zhou, Yutao Zhu, Peitian Zhang, and Zhicheng
Dou. 2025b. Search-o1: Agentic search-enhanced
large reasoning models.CoRR, abs/2501.05366.
Xiaoxi Li, Wenxiang Jiao, Jiarui Jin, Guanting Dong,
Jiajie Jin, Yinuo Wang, Hao Wang, Yutao Zhu, Ji-
Rong Wen, Yuan Lu, and Zhicheng Dou. 2025c.
Deepagent: A general reasoning agent with scalable
toolsets.Preprint, arXiv:2510.21618.
Xiaoxi Li, Jiajie Jin, Guanting Dong, Hongjin Qian, Yu-
tao Zhu, Yongkang Wu, Ji-Rong Wen, and Zhicheng
Dou. 2025d. Webthinker: Empowering large rea-
soning models with deep research capability.CoRR,
abs/2504.21776.
Zhiyu Li, Shichao Song, Hanyu Wang, Simin Niu, Ding
Chen, Jiawei Yang, Chenyang Xi, Huayi Lai, Ji-
hao Zhao, Yezhaohui Wang, Junpeng Ren, Zehao
Lin, Jiahao Huo, Tianyi Chen, Kai Chen, Kehang Li,
Zhiqiang Yin, Qingchen Yu, Bo Tang, and 3 others.
2025e. Memos: An operating system for memory-
augmented generation (mag) in large language mod-
els.Preprint, arXiv:2505.22101.
Miao Lu, Weiwei Sun, Weihua Du, Zhan Ling, Xuesong
Yao, Kang Liu, and Jiecao Chen. 2025. Scaling llm
multi-turn rl with end-to-end summarization-based
context management.Preprint, arXiv:2510.06727.
Lingrui Mei, Jiayu Yao, Yuyao Ge, Yiwei Wang, Bao-
long Bi, Yujun Cai, Jiazhi Liu, Mingyu Li, Zhong-Zhi
Li, Duzhen Zhang, Chenlin Zhou, Jiayi Mao, Tianze
Xia, Jiafeng Guo, and Shenghua Liu. 2025. A sur-
vey of context engineering for large language models.
Preprint, arXiv:2507.13334.
Grégoire Mialon, Clémentine Fourrier, Thomas Wolf,
Yann LeCun, and Thomas Scialom. 2024. GAIA: a
benchmark for general AI assistants. InThe Twelfth
International Conference on Learning Representa-
tions.
OpenAI. 2025. Deep research system card. Technical
report, OpenAI.
Zile Qiao, Guoxin Chen, Xuanzhong Chen, Donglei Yu,
Wenbiao Yin, Xinyu Wang, Zhen Zhang, Baixuan
Li, Huifeng Yin, Kuan Li, Rui Min, Minpeng Liao,
Yong Jiang, Pengjun Xie, Fei Huang, and Jingren
Zhou. 2025. Webresearcher: Unleashing unbounded
reasoning capability in long-horizon agents.Preprint,
arXiv:2509.13309.
9

Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang,
Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao Li,
Yunxin Li, Shijue Huang, and 1 others. 2025. Ui-
tars: Pioneering automated gui interaction with native
agents.arXiv preprint arXiv:2501.12326.
Philip Schroeder, Nathaniel W. Morgan, Hongyin Luo,
and James R. Glass. 2025. THREAD: Thinking
deeper with recursive spawning. InProceedings of
the 2025 Conference of the Nations of the Americas
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies (Volume 1:
Long Papers), pages 8418–8442, Albuquerque, New
Mexico. Association for Computational Linguistics.
Noah Shinn, Federico Cassano, Ashwin Gopinath,
Karthik Narasimhan, and Shunyu Yao. 2023. Re-
flexion: language agents with verbal reinforcement
learning. InAdvances in Neural Information Process-
ing Systems, volume 36, pages 8634–8652. Curran
Associates, Inc.
Weiwei Sun, Miao Lu, Zhan Ling, Kang Liu, Xuesong
Yao, Yiming Yang, and Jiecao Chen. 2025. Scaling
long-horizon llm agent via context-folding.Preprint,
arXiv:2510.11967.
Xiangru Tang, Tianrui Qin, Tianhao Peng, Ziyang Zhou,
Daniel Shao, Tingting Du, Xinming Wei, Peng Xia,
Fang Wu, He Zhu, Ge Zhang, Jiaheng Liu, Xingyao
Wang, Sirui Hong, Chenglin Wu, Hao Cheng, Chi
Wang, and Wangchunshu Zhou. 2025. Agent kb:
Leveraging cross-domain experience for agentic prob-
lem solving.Preprint, arXiv:2507.06229.
Gemini Team. 2025. Gemini 2.5: Pushing the fron-
tier with advanced reasoning, multimodality, long
context, and next generation agentic capabilities.
Preprint, arXiv:2507.06261.
Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao
Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang,
Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei,
and Ji-Rong Wen. 2023a. A survey on large lan-
guage model based autonomous agents.Preprint,
arXiv:2308.11432.
Lei Wang, Wanyu Xu, Yihuai Lan, Zhiqiang Hu,
Yunshi Lan, Roy Ka-Wei Lee, and Ee-Peng Lim.
2023b. Plan-and-solve prompting: Improving zero-
shot chain-of-thought reasoning by large language
models. InProceedings of the 61st Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 2609–2634, Toronto,
Canada. Association for Computational Linguistics.
Yu Wang, Ryuichi Takanobu, Zhiqi Liang, Yuzhen Mao,
Yuanzhe Hu, Julian McAuley, and Xiaojian Wu. 2025.
Mem-α: Learning memory construction via rein-
forcement learning.Preprint, arXiv:2509.25911.
Jason Wei, Zhiqing Sun, Spencer Papay, Scott McK-
inney, Jeffrey Han, Isa Fulford, Hyung Won Chung,
Alex Tachard Passos, William Fedus, and Amelia
Glaese. 2025. Browsecomp: A simple yet chal-
lenging benchmark for browsing agents.Preprint,
arXiv:2504.12516.
Jialong Wu, Baixuan Li, Runnan Fang, Wenbiao Yin,
Liwen Zhang, Zhengwei Tao, Dingchu Zhang, Zekun
Xi, Gang Fu, Yong Jiang, Pengjun Xie, Fei Huang,
and Jingren Zhou. 2025a. Webdancer: Towards au-
tonomous information seeking agency.Preprint,
arXiv:2505.22648.
Xixi Wu, Kuan Li, Yida Zhao, Liwen Zhang, Litu
Ou, Huifeng Yin, Zhongwang Zhang, Xinmiao Yu,
Dingchu Zhang, Yong Jiang, Pengjun Xie, Fei Huang,
Minhao Cheng, Shuai Wang, Hong Cheng, and
Jingren Zhou. 2025b. Resum: Unlocking long-
horizon search intelligence via context summariza-
tion.Preprint, arXiv:2509.13313.
Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Jun-
tao Tan, and Yongfeng Zhang. 2025a. A-mem:
Agentic memory for llm agents.arXiv preprint
arXiv:2502.12110.
Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao
Tan, and Yongfeng Zhang. 2025b. A-mem: Agentic
memory for llm agents.Preprint, arXiv:2502.12110.
Sikuan Yan, Xiufeng Yang, Zuchao Huang, Ercong
Nie, Zifeng Ding, Zonggen Li, Xiaowen Ma, Kris-
tian Kersting, Jeff Z. Pan, Hinrich Schütze, V olker
Tresp, and Yunpu Ma. 2025. Memory-r1: Enhanc-
ing large language model agents to manage and uti-
lize memories via reinforcement learning.Preprint,
arXiv:2508.19828.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
iheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41
others. 2025a. Qwen3 technical report.Preprint,
arXiv:2505.09388.
Cheng Yang, Xuemeng Yang, Licheng Wen, Daocheng
Fu, Jianbiao Mei, Rong Wu, Pinlong Cai, Yufan Shen,
Nianchen Deng, Botian Shi, Yu Qiao, and Haifeng Li.
2025b. Learning on the job: An experience-driven
self-evolving agent for long-horizon tasks.Preprint,
arXiv:2510.08002.
Hongkang Yang, Zehao Lin, Wenjin Wang, Hao Wu,
Zhiyu Li, Bo Tang, Wenqiang Wei, Jinbo Wang,
Zeyun Tang, Shichao Song, Chenyang Xi, Yu Yu,
Kai Chen, Feiyu Xiong, Linpeng Tang, and Weinan
E. 2024. Memory 3: Language modeling with
explicit memory.Journal of Machine Learning,
3(3):300–346.
Wei Yang, Jinwei Xiao, Hongming Zhang, Qingyang
Zhang, Yanna Wang, and Bo Xu. 2026. Coarse-
to-fine grounded memory for llm agent planning.
Preprint, arXiv:2508.15305.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik Narasimhan, and Yuan Cao. 2023.
ReAct: Synergizing reasoning and acting in language
models. InInternational Conference on Learning
Representations (ICLR).
10

Rui Ye, Zhongwang Zhang, Kuan Li, Huifeng Yin,
Zhengwei Tao, Yida Zhao, Liangcai Su, Liwen
Zhang, Zile Qiao, Xinyu Wang, Pengjun Xie, Fei
Huang, Siheng Chen, Jingren Zhou, and Yong
Jiang. 2025. Agentfold: Long-horizon web agents
with proactive context management.Preprint,
arXiv:2510.24699.
Hongli Yu, Tinghong Chen, Jiangtao Feng, Jiangjie
Chen, Weinan Dai, Qiying Yu, Ya-Qin Zhang, Wei-
Ying Ma, Jingjing Liu, Mingxuan Wang, and Hao
Zhou. 2025. Memagent: Reshaping long-context llm
with multi-conv rl-based memory agent.Preprint,
arXiv:2507.02259.
Guibin Zhang, Muxin Fu, and Shuicheng Yan. 2025.
Memgen: Weaving generative latent memory for self-
evolving agents.Preprint, arXiv:2509.24704.
Hongming Zhang, Ke Sun, bo xu, Linglong Kong, and
Martin Müller. 2024. A distance-based anomaly de-
tection framework for deep reinforcement learning.
Transactions on Machine Learning Research.
Hongming Zhang, Chenjun Xiao, Han Wang, Jun Jin,
bo xu, and Martin Müller. 2023. Replay memory
as an empirical MDP: Combining conservative es-
timation with experience replay. InThe Eleventh
International Conference on Learning Representa-
tions.
Bingxi Zhao, Lin Geng Foo, Ping Hu, Christian
Theobalt, Hossein Rahmani, and Jun Liu. 2025. Llm-
based agentic reasoning frameworks: A survey from
methods to scenarios.Preprint, arXiv:2508.17692.
Jun Zhao, Can Zu, Hao Xu, Yi Lu, Wei He, Yiwen
Ding, Tao Gui, Qi Zhang, and Xuanjing Huang.
2024. Longagent: Scaling language models to 128k
context through multi-agent collaboration.Preprint,
arXiv:2402.11550.
Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou,
Robert Lo, Abishek Sridhar, Xianyi Cheng, Yonatan
Bisk, Daniel Fried, Uri Alon, and 1 others. 2023. We-
barena: A realistic web environment for building au-
tonomous agents.arXiv preprint arXiv:2307.13854.
Zijian Zhou, Ao Qu, Zhaoxuan Wu, Sunghwan Kim,
Alok Prakash, Daniela Rus, Jinhua Zhao, Bryan
Kian Hsiang Low, and Paul Pu Liang. 2025. Mem1:
Learning to synergize memory and reasoning for effi-
cient long-horizon agents.
A Experiment setup
A.1 Benchmarks and Data Selection
For the primary evaluation, we utilized a curated
subset of 150 tasks from the BrowseComp-Plus
benchmark, maintaining a balanced 1:1:1 ratio
across easy, medium, and hard difficulty levels. For
the GAIA benchmark, we focused on the validation
set (165 tasks), specifically filtering for and evalu-
ating all text-only instances. In ablation studies, we
maintained the same 150 tasks for BrowseComp-
Plus and the text-only GAIA subset for testing. All
experimental results are reported as the mean value
derived from at least three independent trials to
ensure statistical reliability and consistency.
A.2 Model Configurations &
Hyperparameters
The agent frameworks were evaluated using
Qwen3-32B and DeepSeek-V4 as the primary back-
bone models. To ensure procedural consistency and
experimental stability, all auxiliary language mod-
eling tasks across all frameworks were uniformly
handled by DeepSeek-V4.
To regulate task progression and optimize com-
putational efficiency, the HyMem framework em-
ploys a specific set of hyperparameter constraints:
•Planner_turns=12 : The maximum number
of interaction turns permitted within theplan-
ner Layerfor high-level strategic planning.
•execute_turns=10 : The maximum allow-
able turns for theActor Layerduring discrete
task execution and tool manipulation.
•max_iso_reasoning=5 : The upper limit on
the total number ofisolated reasoning ses-
sionsinvoked throughout the duration of a
task.
•max_iso_reasoning_turn=3 : The maxi-
mum number of reasoning steps allowed
within each individualisolated reasoning ses-
sion.
This configuration was selected to ensure the agent
has sufficient latitude for environmental explo-
ration and complex decision-making while prevent-
ing excessive task duration or inefficient resource
consumption. We compared HyMem against two
standard baselines. ReAct maximum turn budget
was set to 100. Summarization-based Agent: When
the context length reached a predefined threshold,
the agent performed recursive summarization by
distilling the most recent three interaction turns
and concatenating them with the preceding history.
This baseline was also capped at 100 turns.
A.3 Context Analysis
To evaluate global context management efficiency,
we collected historical trajectories from identical
tasks for both HyMem, ReAct, ReSum and A-
MEM. Figure 4 plots task progress on the horizon-
tal axis and context volume on the vertical axis. To
11

visualize the aggregate effect, we concatenated the
context-change data from all evaluated tasks into
a continuous curve, providing a holistic compari-
son of how each framework manages information
density over time.
B Case Study
To demonstrate the effectiveness of the HyMem
framework in leveraging hierarchical isolation for
context management to enhance reasoning capa-
bilities in complex, long-horizon tasks, Table 3
provides a detailed case study. This instance illus-
trates how the Planner and Executor layers utilize
architectural decoupling to filter redundant informa-
tion while facilitating the exchange of high-value
strategic signals. Furthermore, it highlights how
the isolated reasoning module and memory man-
agement mechanism synergistically enhance ex-
ploratory steps and distill essential information to
maintain reasoning integrity, ultimately enabling
the resolution of intricate multi-hop tasks. For the
sake of clarity, the content in the table has been
selectively curated and condensed to emphasize the
specific roles of these core components and pro-
vide a transparent illustration of the framework’s
operational mechanics.
C Prompt Engineering
The primary prompt templates for the HyMem
framework are detailed in Tables 4 – 7, represent-
ing the Planner Layer, Executor Layer, isolated
reasoning sessions, and memory management com-
ponents, respectively (Sun et al., 2025; Li et al.,
2025e).
User Query:Born in 1970s, 3x World Half-
Marathon champ... retired 2021.Goal:Date (DD/M-
M/YYYY) of 10,000m PB?
Turn 1: Entity Identification
<think> Break down constraints: "Born 1970s", "3x
Champion". First, identify the athlete.(. . . )</think>
<task> Search "three-time World Half-Marathon
champion born 1970s" </task> <result> Target
matchesTegla Loroupe(Kenyan). Born May 9, 1973.
Won titles 1997, 1998, 1999. (...)</result>
Turn 2-4: Constraint Verification
<think> Candidate found. Before searching for PB, ver-
ify detailed clues (weight, UN honor, retirement) in par-
allel.</think>
<isoReason> Verify: (1) First win age 21 (NYC
Marathon ’94?); (2) UN Person of Year; (3) Weight 40kg.
</isoReason> <result> [Success]Confirmed: Won
NYC Marathon at 21; UN Person of Year (Kenya, 2016);
Weight approx 40kg.</result>
Turn 5: Attribute Retrieval
<think> Identity verified. Now search specifically for
the 10,000m personal best date.</think>
<task> Search "T egla Loroupe 10,000 meters per-
sonal best date" </task> <result> Found PB time:
30:32.03.[Failure]Specific date missing in snippets.
Source only lists time.</result>
Turn 6: Refinement Strategy
<think> Direct search for date failed. Strategy shift:
Search using the exact time "30:32.03" to find the spe-
cific event record.</think>
<task> Search "T egla Loroupe 30:32.03 10,000m"
</task> <result> Event Identified:1999 World
Championships (Sevilla). Date confirmed:26 August
1999.</result>
/compressMemory Compression: Detailed traces (Turns
1-6) folded intoAssignment, Moving & Tool
Memory.
Updated Memory:"Tegla Loroupe, PB 30:32.03 on
26 Aug 1999 (Needs Final Verify)".
Turn 7-8: Final Answer
<think> Memory confirms date. Evidence is consistent
across sources (Sporting-heroes, Wikipedia). </think>
Answer:Tegla Loroupe achieved her personal best for
the 10,000-meter race on26 August 1999.
Table 3: Execution trace of HyMem on a multi-hop
reasoning task. The flow demonstrates the interaction
between the Planner Layer (reasoning/task generation),
Executor Layer (tool use), and the Isolated Reasoning
mechanism for verification. Note the Memory Com-
pression event which consolidates the context before the
final answer.
12

Prompt 1: HyMem Planner Layer
You are an expert research planner with memory-augmented reasoning capabilities. Your task is to analyze complex questions and devise effective search
strategies. You work with a specialized searchactorand can create reasoning isoReasons. Your goal is to reach the best final answer by combining structured
analysis, targeted retrieval, delegated reasoning, and memory-guided iteration.
## Role & Responsibilities
Your role is to:
- Analyze the problem and identify key information needs.
- Decompose complex questions into concrete search tasks and reasoning sub-problems.
- Assign search tasks to theactoror delegate complex reasoning to isoReasons.
- Synthesize results and reason towards the final answer.
## Workflow
Follow this process iteratively:
(a) Problem Analysis: Identify core entities, constraints, and relationships.
(b) Search Strategy: Design strategies that narrow the search space and reduce ambiguity.
(c) Task Delegation: You havetwodelegation options:
-Option A – Search Task (for actor):
<task> [Describe the specific search task for the actor.] </task>
-Option B – isoReason Task (independent reasoning):
<isoReason>
<description> [3-5 word identifier] </description>
<prompt> [Clear reasoning objective] </prompt>
</isoReason>
(d) Result Integration: When theactororisoReasonreturns results:
- Evaluate whether results satisfy the criteria.
- Identify remaining gaps and decide whether to continue exploration or conclude.
(e) Memory-Guided Reasoning: Use memory from previous sessions to:
- Avoid repeating failed strategies.
- Build upon prior discoveries.
- Maintain reasoning continuity across iterations.
## Output Format
Your response must include step-by-step reasoning and a final answer:
<think>
Step-by-step reasoning, including problem analysis, strategy design,
delegation choices, and integration decisions.
If reasoning becomes too lengthy, output <to_memory> to trigger memory compression.
</think>
<answer> [Your final answer] </answer>
<confidence> [Score 0-1] </confidence>
## Important Guidelines
1. Think step-by-step within<think>...</think>tags.
2. UseisoReasonwhen a sub-problem needs independent analysis.
3. Use<task>for straightforward information retrieval.
4. If reasoning becomes too lengthy, output<to_memory>to trigger memory compression.
5. Do not stop reasoning until you can provide a final answer.
6. If stuck, reanalyze the problem from different angles and revise the search plan.
Table 4: Full prompt template for HyMem Planner Layer.
13

Prompt 2: HyMem Executor Layer
You are a searching agent equipped with multiple search tools and file parsing capabilities. Your task is to locate, extract, and synthesize information that satisfies
a given search target, using careful query design and iterative reasoning.
## Role & Objective
Your goal is to efficiently find accurate and relevant information by:
- Designing precise search queries.
- Selecting appropriate tools for retrieval or parsing.
- Extracting structured evidence from web pages or files.
- Synthesizing findings into clear results aligned with the search target.
## Available Tools
You may use the following tools at any step:
•web_search(keywords): Perform keyword-based web searches.
•web_parse(link, query): Fetch a specific web page and extract information relevant to a query.
•batch_search_and_filter(keyword): Run integrated searches with built-in filtering.
•parse_file(file_path): Parse and extract text from files (PDF, CSV , XLSX, DOCX, TXT, HTML).
## Workflow
Follow this structured process:
(a) Target Analysis: Clearly understand the search target and define information requirements.
(b) Query Design: Craft focused keywords; avoid overly broad searches.
(c) Tool Selection: Choose the most suitable tool for each subtask (web search, page parsing, or file parsing).
(d) Iterative Exploration: Refine queries or parse deeper sources based on intermediate findings.
(e) Result Synthesis: Aggregate extracted evidence into concise, relevant findings.
## Example Usage
<code>
# Web search
result = await web_search("machine learning papers 2023")
for item in result["tool_result"]["organic"][:5]:
print(f"- {item['title']}: {item['snippet'][:100]}")
# File parsing
file_result = await parse_file("/path/to/document.pdf")
content = file_result["tool_result"]["content"]
print(f"File content: {content[:500]}")
</code>
## Output FormatYour response must include reasoning and final findings:
<think>
Step-by-step reasoning about query selection, tool usage,
evidence evaluation, and refinement decisions.
</think>
<results>
[Structured list or summary of findings that satisfy the search target.]
</results>
## Guidelines
1. Always reason explicitly within<think>...</think>tags.
2. Avoid unnecessary or overly broad searches.
3. Useweb_parsefor detailed extraction from promising sources.
4. Useparse_filewhen handling provided documents.
5. Iterate until the search target is sufficiently satisfied, then report results clearly.
Table 5: Full prompt template for HyMem Executor Layer.
14

Prompt 3: HyMem Isolated Reasoning Module
You are a reasoning branch of the main planner. You inherit the full context and memory fromMAIN. Your role is to focus exclusively on the assigned reasoning
task, execute systematic analysis, optionally gather information, and return immediately after completing the objective. You must not perform any actions beyond
the specified scope.
## Role & Scope
Your responsibilities are strictly limited to:
- Concentrating on the assigned reasoning objective only.
- Applying structured, step-by-step analysis.
- Returning comprehensive findings toMAINwithout attempting to solve the overall problem.
## Critical Instructions
You must follow these rules precisely:
1.Understand the Task: Carefully read and internalize the assigned objective.
2.Execute Analysis:
• Perform step-by-step reasoning within<think>...</think>tags.
• Use<task>...</task>to delegate searches to the executor if external information is required.
• Analyze all evidence systematically and critically.
3.Return Findings: Once the objective is complete, immediately report results using the required return format.
## Return Format Requirements
Because your internal reasoning is invisible toMAIN, your return must be explicit, structured, and self-contained. Include all of the following components:
•CONCLUSION: A direct answer to the assigned question, with concise justification.
•KEY EVIDENCE: Supporting facts, observations, or data points (include sources or doc IDs if available).
•CONFIDENCE: Your confidence in the conclusion (scale 0–1).
•NOTES: Caveats, limitations, assumptions, or recommendations forMAIN.
## Operational Constraint
- Focusexclusivelyon the assigned task.
- DoNOTprovide a final answer to the main problem.
- DoNOTperform actions outside your designated reasoning scope.
## Output Format
When you have completed your assigned reasoning task, wrap everything strictly in the following structure:
<think>
Step-by-step reasoning specific to the assigned task.
</think>
<return>
CONCLUSION: ...
KEY EVIDENCE: ...
CONFIDENCE: ...
NOTES: ...
</return>
Table 6: Full prompt template for the HyMem Isolated Reasoning Module, responsible for recursive sub-problem
decomposition and independent analysis.
15

Prompt 4: HyMem Memory Management Module
You are a memory management assistant responsible for compressing, structuring, and recording different forms of agent memory. Your objective is to distill
complex interaction histories into concise, machine-readable memory representations that support long-term reasoning, short-term planning, and tool-use
optimization.
## Memory Modules Overview
You operate three distinct memory modules, each with a clearly defined role, input scope, and output schema. You must strictly follow the instructions for each
module and outputonlythe specified JSON format.
## Module 1: episode Memory
Role: You are a memory compression assistant. Summarize the key events in the planner’s reasoning process.
Task:{question}
Inputs:{planner_history},{executor_summary}
Instructions:
1. Identify major milestones, strategic decisions, and key discoveries.
2. Extract only critical events that inform long-term progress.
3. Outputonlythe JSON format specified below.
Output Schema (JSON)
{
"task_description": "Summary of the task and overall goals",
"key_events": [
{ "step": "N", "description": "What was done", "outcome": "learned" }
],
"current_progress": "Summary of progress and remaining work"
}
## Module 2: working Memory
Role: You are a working memory manager. Create a snapshot of the current research state.
Inputs:{recent_history},{hypothesis_section}
Instructions:
1. Extractonlyimmediate goals, current challenges, and planned next steps.
2. Focus on actionable information and ignore completed work.
3. Outputonlythe JSON format specified below.
Output Schema (JSON)
{
"immediate_goal": "What the planner is currently determining",
"current_challenges": "Main obstacles or gaps in information",
"active_hypotheses": ["hypothesis1", "hypothesis2"],
"next_actions": [
{ "type": "search", "description": "Action" }
]
}
## Module 3: Tool Memory
Role: You are a tool experience recorder. Synthesize tool usage patterns across interactions.
Input:{history_str}
Instructions:
1. Analyze which tool calls succeeded versus failed.
2. Identify effective search strategies and parameter patterns.
3. Outputonlythe JSON format specified below.
Output Schema (JSON)
{
"tools_used": [
{
"tool_name": "str",
"call_count": N,
"effective_queries": []
}
],
"derived_rules": ["Rule learned from experience"],
"useful_sources": ["URLs or docids"]
}
## Global Constraints
• Donotinclude any text outside the required JSON schemas.
• Donotmix content across memory modules.
• Ensure outputs are concise, structured, and suitable for long-term agent memory storage.
Table 7: The suite of prompts used in the Memory Management Module, including episode memory, working
memory, and Tool memory.
16
