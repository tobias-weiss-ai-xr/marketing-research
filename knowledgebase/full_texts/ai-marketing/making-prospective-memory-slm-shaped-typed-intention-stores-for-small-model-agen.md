---
title: 'Making Prospective Memory SLM-Shaped: Typed Intention Stores for Small-Model Agents'
url: https://arxiv.org/abs/2609.01272
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Jinqing Zhao
- Chengcan Wu
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.01272
pages: 8
chars: 27178
fetched_at: '2026-11-08T13:39:01+00:00'
kb_version: 1
---

# Making Prospective Memory SLM-Shaped: Typed Intention Stores for Small-Model Agents

Making Prospective Memory SLM-Shaped:
Typed Intention Stores for Small-Model Agents
Jinqing Zhao
Peking University
Chengcan Wu
Peking University
wuchengcan@stu.pku.edu.cn
Abstract
Prospective memory means carrying out a deferred intention at the right future
cue while other work continues. Benchmarks now isolate it as an agent skill, yet
frontier LLMs still struggle: the best published PM-Bench scaffold reaches only
65.1% Set-F1. We argue that this loop is schema-constrained state tracking rather
than open-ended reasoning, and that small models can execute it when the action
space is typed. We propose the Prospective Intention Store (PIS) that puts lifecycle
logic in code and scoped language work on the model. The scaffold is agentic and
training-free: no selector fine-tuning and no trajectory distillation. On PM-Bench,
DeepSeek-Chat with PIS reaches 82.9% Set-F1. On Gemma-E2B, Set-F1 is only
4.2% without a store and at most 6.6% under seven retrospective memories, while
PIS reaches 66.2%. PIS further reaches 70.1% Set-F1, where retrospective memory
methods stay at most 54.4%. PIS sets a new state of the art on this benchmark and
enables small models to surpass the published large-model scaffold.
1 Introduction
As language agents move from single-turn answering to long-horizon assistance—planning, tool use,
and multi-session interaction—memory becomes indispensable [Yao et al., 2023, Packer et al., 2023,
Sumers et al., 2024]. Without an external store, models forget user constraints, lose intermediate
state, and cannot reuse experience across steps [Liu et al., 2024, Maharana et al., 2024, Wu et al.,
2024]. A large share of today’s agent memory is retrospective: write notes from interaction, update
or merge entries, and later retrieve what is relevant to a query [Chhikara et al., 2025, Xu et al.,
2025, Zhong et al., 2024]. In practice, that write–update–retrieve loop is dominated bynarrow,
repetitivecalls—structured extraction, short summaries, similarity lookup, light JSON edits—rather
than open-ended reasoning [Belcak et al., 2025, Fang et al., 2025]. Such scoped invocations are
a natural fit for small language models (SLMs): they are cheaper, lower-latency, and deployable
on-device, while large models remain a fallback for hard open-domain work [Belcak et al., 2025,
Sharma and Mehta, 2025, Erdogan et al., 2024, Chen et al., 2024]. Schema-constrained tool use
already shows that 1B–7B models can match or exceed cloud-scale APIs when the action space is
typed [Erdogan et al., 2024, Chen et al., 2024, Patil et al., 2023].
Recent Memory×SLM systems report strong results: SLMs can run online controller/selector/writer
pipelines [Zhang et al., 2026a], and dual-space distillation lets a 4B on-device agent approach a
larger teacher when procedural memories are provided [Hosseini et al., 2026]. Those gains typically
require training-time cost—selector LoRA, teacher trajectories, or student adapters—before the small
model operates memory well. Despite this progress, the memories those systems operate remain
retrospective: they retrieve or cache the past rather than maintain deferred commitments until a
future cue fires. Prospective memory (PM)—maintaining a deferred intention and executing it at a
future cue or time while other activities continue—is ubiquitous in everyday assistance (“remind
me when the portal opens,” “take the medicine at 21:00”) and has long been distinguished from
retrospective recall in cognitive science [Einstein and McDaniel, 1990, Rendell and Craik, 2000]. In
agent-memory work, PM remains sparsely studied: most benchmarks and stores optimize sim(e, q)
rather than whether a trigger is satisfied and which set of actions is due [Maharana et al., 2024,
Submitted to 40th Conference on Neural Information Processing Systems (NeurIPS 2026). Do not distribute.
arXiv:2609.01272v1  [cs.AI]  1 Sep 2026

Typed Intention： =  (, , ) ∈
 trigger
  action
pending
done
canceled
 status
Intention expiration conditions Action executed when φ is satisfied current status of the Intention
Stage 4：Decide
input
......
Structurer
Intention 1
Intention 2
Intention n
Intention k
SLM
Disassembler
reschedule
cancel
override
New Intention
Stage 1：Form Stage 2&3：Revise & Filter
History
Intention

SLM
Eligible(, )
Intention 1
Intention 2
Intention m
......
Intention 3
Updated Intention
New Intention
Filtered
Intention Bt Channel Judge
Channel 1
Channel 2
Channel K
......
Channel 3

 ∪ {, }
∀  = (, , ) ∈
 =  ∪ ;  =
SLM Decide = True
Final decision
Updated intention set +
Figure 1: Overview of the prospective intention store (PIS). A deferred commitment is typed as
I=(φ, α, σ); each step runs Form →Revise→Filter→Decide (with optional channel enrichment
before Decide) and emits a due set.
Wu et al., 2024, Xu et al., 2025, Fang et al., 2025]. Evaluations that isolate PM find that even
frontier LLMs are unreliable—PM-Bench’s best reported scaffold reaches only 65.1% Set-F1 [Liu
and Gabriel, 2026], and TriggerBench shows near-ceiling retrospective accuracy where proactive
intervention collapses [Zhang et al., 2026b]—and, to our knowledge, prior work has not studied SLMs
for prospective memory. Existing Memory ×SLM pipelines retrieve the past or cache procedural
scripts; they do not maintain revisable due sets [Hosseini et al., 2026, Zhang et al., 2026a]. We argue
that this gap is architectural as well as a scale gap: PM is schema-constrained state tracking of the
same family as the repetitive memory operations SLMs already handle retrospectively [Belcak et al.,
2025, Sharma and Mehta, 2025].
Conditioned delayed memory requires three loops that similarity RAG does not provide: Update
(rewrite cancellations and overrides), Decision (emit a due set), and Observation (expand clocks
and channels into evidence) [Liu and Gabriel, 2026, Liu et al., 2024]. Once intentions are typed as
(φ, α, σ), those loops are schema-scoped—the regime where TinyAgent-style interfaces succeed [Er-
dogan et al., 2024]—but overload a small model if packed into one open JSON state machine. We
therefore propose the Prospective Intention Store (PIS; Figure 1): an agentic scaffold that external-
izes intentions as typed records, implements lifecycle and board logic in code, and leaves scoped
grounding to the model, usable at inference without PEFT [Belcak et al., 2025]. On PM-Bench, PIS
sets a new state of the art and lets small models exceed the published large-model scaffold.
Contributions.
1. We provide, to our knowledge, the first systematic formalization of prospective-memory operations
for language agents, casting deferred commitments as typed records and due-set decisions as
operators over an external store.
2. We propose an agent system, PIS, that executes those operations as a training-free Form–Decide
loop and show empirically that it yields strong PM-Bench results across large and small backbones.
3. We are the first to study SLMs for prospective memory: PIS not only surpasses large-model
scaffolds in Set-F1, but also uses far fewer tokens and less wall-clock time than heavy large-model
memory stacks, offering an efficient and low-cost solution for this skill [Belcak et al., 2025].
We will release the method and code upon acceptance.
2 Related Work
SLMs for scoped agent work.Belcak et al. argue that most agent traffic is narrow and repetitive,
so SLMs should be the default with selective LLM fallback [Belcak et al., 2025, Sharma and Mehta,
2025]. TinyAgent and Octopus show 1B–7B models matching larger APIs when tool interfaces are
typed [Erdogan et al., 2024, Chen et al., 2024]; we treat prospective memory as another such scoped
subroutine.
2

Retrospective memory.MemGPT/Letta, Mem0, A-Mem, MemoryOS, LightMem and related
stacks store and retrieve episodic or semantic notes [Packer et al., 2023, Chhikara et al., 2025, Xu et al.,
2025, Kang et al., 2025, Fang et al., 2025]. Memory×SLM systems (LightMem-SLM, DuoMem)
operate those pipelines with small models, typically after selector LoRA or teacher distillation [Zhang
et al., 2026a, Hosseini et al., 2026]. Success metrics remain answer quality or environment reward
rather than cue-triggered due-set Set-F1, and the stored object remains a note optimized for sim(e, q),
not a revisable intention (φ, α, σ)with satisfaction sat(φ, Vt). Overall, retrospective memory for
agents is extensively studied, whereas work that targets prospective memory remains scarce.
Prospective memory.Cognitive work distinguishes event- and time-based deferred intentions [Ein-
stein and McDaniel, 1990, Rendell and Craik, 2000]. PM-Bench isolates the skill for tool-using
agents (best scaffold 65.1% Set-F1); residuals concentrate on monitoring, cross-day obligations, and
updates, consistent with missing structure rather than insufficient model scale [Liu and Gabriel, 2026].
TriggerBench shows prospective performance far below matched retrospective probes [Zhang et al.,
2026b]. PIS complements this landscape with a typed prospective object and Form–Decide operators
on a frozen backbone, without selector LoRA or teacher distillation.
3 Method
We cast conditioned delayed memory as operations over a typed prospective intention store (PIS;
Figure 1). Lifecycle over fields is deterministic and structural; the language model performs only
scoped semantic grounding. This factorization is usable at inference without PEFT [Belcak et al.,
2025].
3.1 Problem formulation
At discrete step t, the agent observes evidence Vt (vignette text, tool replies, clocks) and a
menu Xt of candidate actions. It maintains an external store Pt of intentions. Each inten-
tion is a triple I= (φ, α, σ), where φ is the trigger condition, α is the intended action, and
σ∈ {pending,done,canceled} is status. Beyond clocks and in-scene events, many real triggers de-
pend onhidden state channels—portals, dashboards, inboxes, sensors—whose contents are invisible
until the agent proactively queries them. We write Ct for the set of channels referenced by pending
intentions in Pt; a query on channel c∈ Ct returns a reply that is merged into evidence,Vt ←V t ∪ {c}.
Without such Observation, Vt |=φ cannot be evaluated for channel-conditioned pledges, so Decide
must be allowed to request queries before emitting a due set. Satisfaction Vt |=φ is checked by rules
for clocks and by a language judge for event and channel cues once evidence is present. The ideal
due set is D⋆ t ={α|I∈ P t, σ= pending, Vt |=φ} ; the agent emits a predicted set ˆDt ⊆X t,
scored by trajectory Set-F1 against ground-truth Dt [Liu and Gabriel, 2026]. We write the decision
and store update as ˆDt =π(P t, Vt) and Pt+1 =F(P t, Vt, ˆDt). Operationally, each step factors
into four operators—Form, Revise, Filter, and Decide—with an eligibility board Bt ⊆ Pt as the
intermediate view on which Decide conditions, including which channels still need to be queried.
3.2 Store and decision interface
The interface contracts are
ˆDt =π(P t, Vt),P t+1 =F(P t, Vt, ˆDt),(1)
with ideal due set D⋆ t ={α|I∈ P t, σ= pending, Vt |=φ}.(2)
Clock predicates are rule-checked; event and channel predicates use a language judge after any
needed channel replies enterV t.
3.3 Operators
Done-marking after execution is folded into Decide.
Form.Narrative is converted into typed rows once. Disassemble(Vt) extracts commitment spans;
Structure(s) = (φ, α,pending)fills trigger, action, and status:
∆form t = Form(Vt) ={Structure(s)|s∈Disassemble(V t)},P t ← Pt ∪∆ form t .(3)
In the SLM realization, Structure is a slot-filling call assembled in code into I=(φ, α, σ); Disassem-ble and Structure may share one model invocation. Form is the only stage where open text enters the
store schema.
3

Algorithm 1One PIS step: realizing(π, F)
Require:storeP t, evidenceV t, menuX t
Ensure:action set ˆDt, updated storeP t+1
1:P t ← Pt ∪Form(V t)▷Eq. (3)
2:P t ←Revise(P t, Vt)▷Eq. (4)
3:B t ←Filter(P t, Vt)▷Eq. (5)
4:whilechannel judge onB t requestsc∈ Ct do
5:V t ←V t ∪ {c}▷query hidden channel
6:end while
7:( ˆDt,P t+1)←Decide(B t, Vt, Xt)▷Eqs. (6)–(7)
8:return ˆDt,P t+1
Revise.Revise performs belief update over the existing store rather than retrieval. For each pending
I, a language judge may apply one typed patch:reschedulerewrites φ,overridereplaces α, or
cancelsets σ←canceled . Cue appearance alone is not cancellation; it is evidence for Vt |=φ and is
handled by Filter and Decide.
ρt(I;V t) =



(φ′, α,pending),reschedule(I;V t),
(φ, α′,pending),override(I;V t),
(φ, α,canceled),cancel(I;V t),
I,no revision,
Revise(Pt, Vt) ={ρ t(I;V t)}I∈P t .(4)
Implementation shortlists candidates Ct ⊆ Pt, then one indexed judge emits a sparse patch setapplied in code (no update span implies an empty patch).
Filter.Pending rows are reduced to an eligibility board by structural rules (day/horizon, exact clock
matches, discrete event/channel labels). Channel-conditioned intentions whose watched channel has
not yet been queried remain on the board as check targets rather than being dropped—a filtered view
ofP, not embedding neighbors ofV t:
Bt = Filter(Pt, Vt) ={I∈ Pt |σ= pending,eligible(I;V t)}.(5)
Decide.Because many pledges depend on hidden channels, a channel judge first inspects Bt and
may request one or more queries c∈ Ct; replies enrich evidence, Vt ←V t ∪ {c}, before due-set
selection. This Observation step mirrors everyday assistance, where the agent must open a portal or
check a sensor rather than wait for the cue to appear in the dialogue. Decide then maps(B t, Vt, Xt)
to a due set and an updated store:
( ˆDt,P t+1) = Decide(Bt, Vt, Xt),(6)
where ˆDt ⊆X t and fulfilled pending rows are markeddone:
κ(I; ˆDt) =
(φ, α,done), α∈ ˆDt, σ= pending,guards allow,
I,otherwise, Pt+1 ={κ(I; ˆDt)|I∈ P t}.
(7)
Filter and κ are structural; Form, Revise, the channel judge, and Decide require language ground-ing [Belcak et al., 2025].
3.4 One-step algorithm
Equivalently, π comprises Filter, proactive channel Observation overCt, and Decide; F comprises
Form, Revise, and theκcommit inside Decide. Errors are attributable at operator boundaries (§4).
4 Experiments
4.1 Setup
We evaluate on the released PM-Bench synthetic week [Liu and Gabriel, 2026]: seven simulated
days of activity choice interleaved with anonymous prospective menus, lure actions, and hidden
state channels. The primary metric is microSet-F1between predicted and ground-truth due sets; we
also report update miss, cross-day miss, and false alarms per step (Table 1). All backbones remain
frozen: no selector LoRA, no teacher-trajectory distillation, and no PEFT, so gains are attributable to
the memory scaffold. Table 1 compares training-free retrospective memories (Naive RAG; Mem0;
4

Table 1: PM-Bench main comparison (DeepSeek-Chat left, Gemma-E2B right).Set-F1: micro F1
over predicted vs. ground-truth due sets (higher is better).Update miss: miss rate on the update-
sensitive slice (reschedule/cancel/override; lower is better).Cross-day miss: miss rate on intentions
planted on an earlier day (lower is better).FA/step: false alarms per decision step (lower is better).
DeepSeek-Chat Gemma-E2B
Setup Set-F1 Update miss Cross-day miss FA/step Set-F1 Update miss Cross-day miss FA/step
single 67.7 55.6 57.1 6.3 4.2 100.0 85.7 13.8
+ Naive RAG 46.5 88.9 100.0 57.5 6.6 88.9 100.0 43.8
+ Mem0 48.7 100.0 57.1 6.3 4.9 88.9 100.0 45.0
+ A-Mem 54.1 100.0 42.9 8.8 0.0 100.0 100.0 10.0
+ Letta 52.2 66.7 71.4 25.0 4.5 88.9 100.0 55.0
+ LightMem-style 51.5 66.7 57.1 38.8 6.6 88.9 100.0 41.3
+ MemoryOS-style 58.3 66.7 42.9 8.8 3.3 88.9 100.0 42.5
+ PIS82.922.2 0.0 8.866.277.8 28.6 15.0
A-Mem; Letta/MemGPT; LightMem-style; MemoryOS-style) [Chhikara et al., 2025, Xu et al., 2025,
Packer et al., 2023, Fang et al., 2025, Kang et al., 2025] against PIS on DeepSeek-Chat [DeepSeek-AI,
2024] and a local Gemma-E2B SLM [Gemma Team et al., 2024]. Table 2 uses the same layout on
Qwen3.5-4B and Qwen3-8B [Qwen Team, 2025], with Gemma+PIS as a size reference. Table 3
reports wall-clock duration and estimated main-prompt tokens. LightMem/MemoryOS rows are
pattern adapters of the corresponding retrieval designs rather than full upstream servers [Fang et al.,
2025, Kang et al., 2025]. The single row is a no-store baseline that reasons only from dialogue
context.
4.2 Main results
DeepSeek-Chat.PIS attains the highest Set-F1 at 82.9%, above every retrospective memory and
the no-store single ( 67.7%). On the three secondary metrics it also leads: update miss drops to
22.2% (vs. 55.6%–100% for the others), cross-day miss reaches 0.0%, and FA/step stays moderate at
8.8%—unlike Naive RAG or LightMem-style, which inflate false alarms with temporally obsolete
notes. Notably, single outperforms all retrospective memories ( 46.5%–58.3%). Single relies on
in-context reasoning over the ongoing dialogue rather than retrieved notes; the gap indicates that
existing retrospective stores do not beat this PM-Bench baseline, whereas PIS does.
Gemma-E2B.Gemma-E2B is a short-context on-device-class SLM: when injected memory or
long prompts exceed what it can use reliably, Set-F1 and the secondary metrics collapse. All seven
retrospective setups stay near floor (0.0–6.6% Set-F1), with update miss at least 88.9%, cross-day
miss typically 100%, and often high FA/step under noisy retrieves. We use this backbone deliberately
to stress-test methods at the small-model extreme. The same frozen PIS reaches 66.2%, about 10×
the best retrospective row, with cross-day miss falling to28.6% (update miss 77.8% remains the main
residual).
4.3 Scaling to other SLMs
Table 2 repeats the layout on Qwen3.5-4B and Qwen3-8B, with Gemma-E2B+PIS (66.2%) as a size
reference. The two Qwen backbones tell a similar story: PIS is best on both (70.1% on 4B; 57.2% on
8B), with lower update and cross-day misses than most retrieval rows, while retrospective memories
again fail to provide a reliable gain over the no-store baseline (on 4B they all fall below single; on
8B a weak single leaves some retrieval rows above it, but none approach PIS). Absolute scores are
higher on Qwen3.5-4B than on Qwen3-8B because the 3.5-4B checkpoint is designed for agentic
workloads, so it follows the typed board more reliably than the larger 8B chat model on this week.
4.4 Computation analysis
SLM-agent deployments care about latency and token load as well as accuracy [Belcak et al., 2025,
Sharma and Mehta, 2025]. Table 3 reports wall-clockDurand estimated main-prompt input tokens
Tok(millions) from logged EST_INPUT_TOKENS on choose/query calls. Side calls (intention judges,
embedders, external memory servers) are excluded, so Tok is a lower bound; Dur includes side effects
on the critical path.
Efficiency without competence.On Gemma and both Qwen SLMs, most retrospective scaffolds
finish in a few minutes at most about 1M estimated main tokens, yet remain near floor Set-F1. That
5

Table 2: PM-Bench on other SLMs (same metrics and layout as Table 1). Gemma-E2B+PIS is a size
reference; columns areQwen3.5-4B(left) andQwen3-8B(right).
Qwen3.5-4B Qwen3-8B
Setup Set-F1 Update miss Cross-day miss FA/step Set-F1 Update miss Cross-day miss FA/step
Gemma-E2B + PIS (ref.) 66.2 77.8 28.6 15.0 66.2 77.8 28.6 15.0
single 57.4 88.9 85.7 18.8 39.8 55.6 100.0 60.0
+ Naive RAG 48.8 88.9 85.7 57.5 41.5 77.8 100.0 58.8
+ Mem0 54.4 88.9 100.0 50.0 52.5 88.9 42.9 67.5
+ A-Mem 50.3 66.7 100.0 47.5 45.7 55.6 71.4 45.0
+ Letta 43.9 44.4 100.0 86.3 40.6 100.0 85.7 71.3
+ LightMem-style 46.9 66.7 100.0 86.3 42.8 88.9 71.4 88.8
+ MemoryOS-style 50.3 77.8 85.7 67.5 45.4 55.6 85.7 73.8
+ PIS70.133.3 28.6 38.857.255.6 57.1 47.5
Table 3: Computation on the PM-Bench week.Dur: wall-clock time for one full week.Tok:
estimated main-prompt input tokens in millions (sum of logged EST_INPUT_TOKENS; excludes
judge/embed side calls).
DeepSeek Gemma-E2B Qwen3.5-4B Qwen3-8B
Setup Dur Tok Dur Tok Dur Tok Dur Tok
single 1.3m 0.82 1.7m 0.90 1.7m 0.73 2.1m 1.04
+ Naive RAG 1.8m 0.82 1.5m 0.78 2.3m 0.72 3.3m 0.99
+ Mem0 7.4m 2.50 1.2m 0.79 2.1m 0.75 2.5m 0.87
+ A-Mem 22.0m 7.84 18.4m 3.37 35.4m 8.78 27.6m 4.89
+ Letta 23.9m 8.11 20.7m 7.79 14.8m 5.23 15.2m 6.23
+ LightMem-style 6.3m 1.43 2.9m 0.85 3.5m 0.75 5.5m 1.42
+ MemoryOS-style 5.4m 1.65 2.2m 0.79 3.5m 0.72 6.1m 1.47
+ PIS 16.4m 2.08 4.7m 1.23 6.5m 1.48 5.6m 1.39
apparent efficiency largely reflects missing Observation traffic: few check_time/query_state
loops shorten trajectories without improving PM. A-Mem and Letta are expensive exceptions (tens of
minutes; several million tokens) because linking and server-side LLM work dominate Dur.
PIS cost profile.PIS spends more on the main agent than a quiet single baseline (DeepSeek
16.4 min / 2.08M; Gemma 4.7 min / 1.23M; Qwen3.5-4B 6.5 min / 1.48M; Qwen3-8B 5.6 min /
1.39M) because channel enrichment and longer boards increase choose/query volume. Relative to
A-Mem and Letta, PIS is often cheaper in Dur while attaining the best Set-F1 on every backbone
in Tables 1–2. For SLM stacks, a typed Form–Decide loop is preferable to heavy retrospective
infrastructure that does not improve due-set F1.
5 Conclusion
Prospective memory is a newly isolated agent skill that frontier LLMs still struggle with, and that
retrospective Memory×SLM systems do not address. We framed PM as schema-constrained state
tracking and instantiated a typed intention store whose Form–Decide operators realize (π, F)as
agentic scaffolding without training a selector or distilling a student. That training-free stance
attributes competence to the typed object and the operator factorization rather than to PEFT as a
prerequisite. Large backbones with this store exceed published PM-Bench scaffolds (82.9% Set-F1 on
DeepSeek-Chat); Gemma-E2B rises from at most 6.6% under seven retrospective baselines to 66.2%
with the same frozen store; Qwen3.5-4B+PIS reaches 70.1% while seven retrospective memories
stay at most 54.4%. Wall-clock and estimated token costs (§4.4) indicate that the quality gain comes
from scaffolding rather than merely longer prompts.
Limitations.Public prospective-memory benchmarks for agents remain scarce; to our knowledge
PM-Bench is the main openly available suite, so our evaluation is necessarily concentrated on this
dataset. Although PIS needs no model training, fine-tuning is not explored here and may further
improve performance.
Future work.We plan to (i) fine-tune models on the Form–Decide interfaces, (ii) run evaluation
studies that isolate the contribution of each operator, and (iii) build additional prospective-memory
benchmarks to complement the currently limited open supply beyond PM-Bench. We release this as
non-archival work in progress toward SLM-native prospective agents.
6

References
Peter Belcak, Greg Heinrich, Shizhe Diao, Yonggan Fu, Xin Dong, Saurav Muralidharan, Yingyan Celine Lin,
and Pavlo Molchanov. Small language models are the future of agentic AI.arXiv preprint arXiv:2506.02153,
2025.
Wei Chen, Zhiyuan Li, and Mingyuan Ma. Octopus v2: On-device language model for super agent.arXiv
preprint arXiv:2404.01744, 2024.
Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, and Deshraj Yadav. Mem0: Building production-
ready AI agents with scalable long-term memory.arXiv preprint arXiv:2504.19413, 2025.
DeepSeek-AI. DeepSeek-V3 technical report.arXiv preprint arXiv:2412.19437, 2024.
Gilles O. Einstein and Mark A. McDaniel. Normal aging and prospective memory.Journal of Experimental
Psychology: Learning, Memory, and Cognition, 16(4):717–726, 1990.
Lutfi Eren Erdogan, Nicholas Lee, Siddharth Jha, Sehoon Kim, Ryan Tabrizi, Suhong Moon, Coleman Hooper,
Gopala Anumanchipalli, Kurt Keutzer, and Amir Gholami. TinyAgent: Function calling at the edge.arXiv
preprint arXiv:2409.00608, 2024.
Jizhan Fang, Xinle Deng, Haoming Xu, Ziyan Jiang, Yuqi Tang, Ziwen Xu, Shumin Deng, Yunzhi Yao,
Mengru Wang, Shuofei Qiao, Huajun Chen, and Ningyu Zhang. LightMem: Lightweight and efficient
memory-augmented generation.arXiv preprint arXiv:2510.18866, 2025.
Gemma Team et al. Gemma 2: Improving open language models at a practical size.arXiv preprint
arXiv:2408.00118, 2024.
Peyman Hosseini, Ondrej Bohdal, Ahmed Alajrami, Andrea Maracani, Ignacio Castro, Matthew Purver, Mete
Ozay, Savas Ozkan, and Taha Ceritli. DuoMem: Towards capable on-device memory agents via dual-space
distillation.arXiv preprint arXiv:2606.29961, 2026.
Jiazheng Kang, Mingming Ji, Taize Zhao, and Fei Li. Memory OS of AI agent.arXiv preprint arXiv:2506.06326,
2025.
Genglin Liu and Saadia Gabriel. PM-Bench: Evaluating prospective memory in LLM agents.arXiv preprint
arXiv:2607.12385, 2026.
Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy
Liang. Lost in the middle: How language models use long contexts.Transactions of the Association for
Computational Linguistics, 12:157–173, 2024.
Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov, Mohit Bansal, Francesco Barbieri, and Yuwei Fang.
Evaluating very long-term conversational memory of LLM agents.arXiv preprint arXiv:2402.17753, 2024.
Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, and Joseph E. Gonzalez.
MemGPT: Towards LLMs as operating systems.arXiv preprint arXiv:2310.08560, 2023.
Shishir G. Patil, Tianjun Zhang, Xin Wang, and Joseph E. Gonzalez. Gorilla: Large language model connected
with massive APIs.arXiv preprint arXiv:2305.15334, 2023.
Qwen Team. Qwen3 technical report.arXiv preprint arXiv:2505.09388, 2025.
Peter G. Rendell and Fergus I. M. Craik. Virtual week and actual week: Ageing and context dependent
prospective memory.Aging, Neuropsychology, and Cognition, 7(4):209–226, 2000.
Raghav Sharma and Manan Mehta. Small language models for agentic systems: A survey of architectures,
capabilities, and deployment trade offs.arXiv preprint arXiv:2510.03847, 2025.
Theodore Sumers, Shunyu Yao, Karthik Narasimhan, and Thomas Griffiths. Cognitive architectures for language
agents.Transactions on Machine Learning Research, 2024.
Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, and Dong Yu. LongMemEval: Benchmark-
ing chat assistants on long-term interactive memory.arXiv preprint arXiv:2410.10813, 2024.
Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, and Yongfeng Zhang. A-Mem: Agentic memory for
LLM agents.arXiv preprint arXiv:2502.12110, 2025.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. ReAct: Syner-
gizing reasoning and acting in language models. InInternational Conference on Learning Representations,
2023.
7

Jiaquan Zhang, Chaoning Zhang, Shuxu Chen, Zhenzhen Huang, Pengcheng Zheng, Zhicheng Wang, Ping Guo,
Fan Mo, Sung-Ho Bae, Jie Zou, Jiwei Wei, and Yang Yang. Lightweight LLM agent memory with small
language models.arXiv preprint arXiv:2604.07798, 2026a.
Tianhua Zhang, Xinjiang Wang, Q. Zhang, Qi Chen, Kun Li, Yaoqi Chen, Dingdong Wang, Helen Meng,
and Yan Lu. TriggerBench: Investigating prospective memory for large language models.arXiv preprint
arXiv:2606.23459, 2026b.
Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and Yanlin Wang. MemoryBank: Enhancing large language
models with long-term memory.Proceedings of the AAAI Conference on Artificial Intelligence, 38, 2024.
8
