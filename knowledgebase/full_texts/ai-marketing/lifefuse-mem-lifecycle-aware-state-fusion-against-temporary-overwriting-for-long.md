---
title: 'LifeFuse-Mem: Lifecycle-Aware State Fusion Against Temporary Overwriting for Long-Term Memory'
url: https://arxiv.org/abs/2609.12436
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Hanyu Zhao
- Yuqian Feng
- Zhenyu Song
- Yuanchao Cheng
- Yance Jiao
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.12436
pages: 16
chars: 48934
fetched_at: '2026-11-08T13:34:43+00:00'
kb_version: 1
---

# LifeFuse-Mem: Lifecycle-Aware State Fusion Against Temporary Overwriting for Long-Term Memory

LifeFuse-Mem: Lifecycle-Aware State Fusion
Against Temporary Overwriting for Long-Term
Memory
Hanyu Zhao1,*, Yuqian Feng1,2,3,*, Zhenyu Song4,*, Yuanchao Cheng1, Yance Jiao1, Tengfei
Pan1,†, Li Du1,†
1Beijing Academy of Artificial Intelligence
2University of Chinese Academy of Sciences
3Institute of Software, Chinese Academy of Sciences
4National University of Defense Technology
Long-running LLM agents require memory mechanisms that maintain coherent internal states across
interactions. We study a lifecycle-labeled memory setting in which write episodes provide lifecycle
metadata during training, and phase-aware readout is used during evaluation. This setting reflects
the need to distinguish information that should remain influential across future interactions from
information that should affect only the current context. A mismatch between these lifecycles can cause
temporary information to overwrite durable knowledge, leading to behavioral drift in persistent agents.
Within this setting, we introduceLifeFuse-Mem, a lifecycle-aware neural memory framework that
separates information according to its temporal commitment. LifeFuse-Mem uses dedicated memory
components and lifecycle-aware updates to allow stable and transient knowledge to evolve locally
without converting temporary context into durable state. On the controlled anti-overwrite benchmark,
LifeFuse-Mem improves acquisition-controlled retention and reduces temporary overwrite; on two public
long-memory benchmarks, it remains broadly competitive. These results suggest that explicit lifecycle
signals can help diagnose and mitigate overwrite in compact online memory.
1. Introduction
Large language model (LLM)-based agents are evolving from short-lived assistants into persistent
systems that continuously interact with users, accumulate experience, and execute long-horizon tasks Ye
et al. [2026]; CHENG et al. [2026]. To support such persistent interactions, agents increasingly rely
on memory mechanisms to maintain a coherent state beyond the current context window, including
user preferences, behavioral policies, and accumulated knowledge Wu et al. [2024]; Hu et al. [2026].
However,unlikeconventionalinformationstoragesystems,agentmemorymustmanageinformationthat
differs fundamentally in temporal validity: some information should persist across future interactions,
while other information should only influence the current situation Ong et al. [2025].
Existing memory systems Xu et al. [2026]; Tan et al. [2025b] largely overlook this lifecycle dimension,
creating a fundamental failure mode in long-running agents. When information with different persis-
tence requirements is stored and updated through the same memory pathway, temporary context can
overwrite durable knowledge. For example, an agent may maintain a persistent policy requiring user
confirmation before external actions. During a specific debugging session, the user may temporarily
instruct the agent to skip confirmations because all operations occur in a sandbox. The agent should
adapt to this local assumption while preserving its original policy for future tasks. Without lifecycle-
1∗These authors contributed equally to this work. Emails: hyzhao@baai.ac.cn
2†Corresponding author.
arXiv:2609.12436v1  [cs.AI]  11 Sep 2026

Lifecycle-agnostic memory Lifecycle-aware memory
① Earlier permanent write
② Current temporary update Permanent write Temporary write
Shared low-rank state
Later turns Skip confirmation
 Later turns Ask for confirmation
Persistent policy
“confirm before external actions”
Earlier turns Current turn
Temporary instruction
“skip confirmation this time”
Later turns
Confirm?
Skip?
Shared low-rank state
Temporary overwrite
Permanent policy Temporary instruction
Lifecycle Router
long-term
short-term
Figure1: Temporary overwrite arises when a temporary assumption is written into the same compact
state as a permanent fact. LifeFuse-Mem separates information lifecycles at write time and uses
phase-aware readout to preserve long-term facts while still following local assumptions.
aware memory, however, the temporary instruction may be incorporated as a lasting update, causing
the agent to gradually drift from its intended behavior. We refer to this failure as temporary overwrite.
Such failures are particularly problematic for autonomous agents because they silently alter future
decisions, degrade behavioral consistency, and undermine user trust.
Therootcauseoftemporaryoverwriteisthelackoflifecycledisentanglementinmemoryrepresentations.
Existing neural memory mechanisms typically compress interaction histories into a shared latent state
and update this state using unified dynamics Behrouz et al. [2026]; Wang et al. [2025a]. Consequently,
transient assumptions and persistent knowledge compete for the same representational capacity: an
update intended for short-term adaptation can modify the latent components encoding long-term
information. Preventing temporary overwrite therefore requires more than increasing memory capacity
or improving retrieval; it requires a memory architecture that explicitly separates information according
to how long it should influence future agent behavior.
To address this challenge, we study a controlled but diagnostic lifecycle-labeled memory setting in
which write episodes specify whether incoming evidence should be treated as durable or temporary, and
phase-aware readout uses known phase boundaries and query lifecycles at evaluation time. This setting
is intended to isolate temporary overwrite under explicit lifecycle signals; it does not claim autonomous
lifecycle discovery from unlabeled interaction histories. Our contributions are threefold: first, we define
temporary overwrite as a lifecycle mismatch failure mode and evaluate it with an acquisition-controlled
protocol; second, we build Hard Attribution Anti-Overwrite as a diagnostic benchmark for measuring
whether permanent facts survive conflicting temporary writes; third, we propose LifeFuse-Mem, which
reduces overwrite in compact online memory states when lifecycle metadata and phase structure are
2

LLM Backbone
Wv Wk Wq
vt kt qt 0
Attention
Computation
at
+
output
qt m
Adapter
State
+
Wq m
Lifecycle-Aware
Subspace Partition
Rank-r = 8 Memory
Plastic(A = 4) Stable(B = 4)
... ...
Input 𝑥
 Permanent Routing
& Subspace
Writing
Protected State Fusion and Lifecycle Readout
Phase A: Permanent writePhase B:Temporary overwrites
Protected state
construction
Learned Orthogonal Basis
𝑄!	=	𝑜𝑟𝑡ℎ(𝑅!)
Permanent Query
Score with 𝑆" Score with 𝑆#$%&!’
x 1
Plastic rows (always writable)
Stable rows (scaled by𝜌!)Token-level Permanent Router
𝝆𝒕∈[𝟎,𝟏]
𝒉𝒕
x 𝜌$
Permanent Token
Temporary Token
𝜌$≈1
𝜌$≈0
Temporary Query
𝑺𝑨 𝑺𝑨𝑩 𝑺𝒔𝒕𝒂𝒃𝒍𝒆
Fused Score
Score with 𝑆")
Write-then-
read training Answer
Answer Answer
Message
…
Memory update
Routing and writing
Fusion and readout
(Writing disabled)Query
Stable
subspace B
plastic
subspace A
Figure2: Overview of LifeFuse-Mem. The method separates plastic and stable subspaces, routes
permanent tokens toward stable writing, and uses phase-aware protected-state readout.
available.
We evaluate LifeFuse-Mem in two roles. The controlled Hard Attribution Anti-Overwrite benchmark
provides the direct anti-overwrite test, where LifeFuse-Mem improves acquisition-controlled retention
under explicit lifecycle supervision and phase-aware readout. LoCoMo and MemoryAgentBench do
not provide overwrite phases or query lifecycle labels, so we use them only as compatibility checks for
the trained memory adapter in standard online-memory mode; in this setting, LifeFuse-Mem remains
broadly competitive, with gains on LoCoMo and mixed category-level results on MemoryAgentBench.
2. Related Work
2.1. Memory-Augmented Language Models
Memory-augmented language models extend context through retrieval, replay, compression, or neural
state. Retrieval systems store passages or hidden states and fetch them at generation time, including
retrieval-augmented pre-training Zhao et al. [2025]; Jin et al. [2025], retrieve-and-read generation Gao
et al. [2025]; Cheng et al. [2025],kNN or datastore-based lookup Wang et al. [2025a]; Zanzotto et al.
[2025], and self-reflective retrieval Tan et al. [2025b]; Ong et al. [2025]. Long-context methods instead
compress, index, or manage history through compressive memory Behrouz et al. [2026]; He et al.
[2025], landmark access Gao et al. [2025]; Bai et al. [2025], gist tokens He et al. [2025]; Wu et al.
[2025]; Deng et al. [2025], or tiered memory management Kang et al. [2025]; Chhikara et al. [2025],
though longer replay alone does not ensure reliable use of all positions Bai et al. [2025]; Wu et al.
[2025]; Yen et al. [2024]; Modarressi et al. [2025]. LifeFuse-Mem is closest to parametric or adapter
memories that are read during the forward pass, including selective state-space memory He et al.
[2025], test-time-training states Behrouz et al. [2026], neural long-term memory modules Behrouz
3

et al. [2026]; Wang et al. [2025a], delta-rule associative states Lei et al. [2026], trainable memory
layers Zanzotto et al. [2025], external or latent neural memory modules Xu et al. [2026]; Wang et al.
[2025a], controllable key–value memory Liao et al. [2026], and decoupled side-networks Hu et al.
[2025]; Wang et al. [2025b]. In particular,δ-Mem stores interaction evidence in a compact online
associative state read as low-rank attention corrections Lei et al. [2026]. Such states are efficient and
tightly coupled to generation, but they also mix heterogeneous evidence in a shared representation.
LifeFuse-Mem addresses the resulting write interference by adding lifecycle-aware subspace isolation
and phase-aware readout to an existing parametric memory.
2.2. Continual Learning and Catastrophic Forgetting
Continual learning studies retention under sequential updates. Common solutions include replay and
episodic constraints Yang et al. [2025b]; Wang et al. [2025b], importance-based regularization Liao
et al. [2026]; Li et al. [2025], parameter isolation Hu et al. [2025]; Liao et al. [2026], and subspace or
gradient-projection methods Liao et al. [2026]; Feng et al. [2025]; recent LLM work adapts related
ideas through orthogonal low-rank adaptation Liao et al. [2026]; Yang et al. [2025b]. Surveys provide
broader taxonomies Yang et al. [2025a]. Temporary overwrite is related but has a different target
behavior: the later value may be locally valid without being a permanent replacement. LifeFuse-Mem
therefore uses isolation and routing to distinguish information lifecycles inside one online memory
state, rather than to retain old task behavior across discrete tasks.
2.3. Long-Term Memory Evaluation
Long-term memory benchmarks test whether models can use extended histories, including conversa-
tional and agent-oriented settings such as LoCoMo Maharana et al. [2024] and LongMemEval Wu et al.
[2024], multitask long-context suites Bai et al. [2025]; Hu et al. [2026]; Yen et al. [2024], bilingual
long-context understanding Bai et al. [2025], evaluation beyond 100K tokens Bai et al. [2025]; Wu et al.
[2025], and controlled retrieval or aggregation stress tests Wu et al. [2025]; Tan et al. [2025a]; Zhang
et al. [2025]; Modarressi et al. [2025]. These benchmarks are valuable for general memory ability, but
they typically do not separate permanent facts from temporary overwrites or condition retention on
successful initial acquisition. Our Hard Attribution Anti-Overwrite benchmark complements them with
an explicit Phase-A/Phase-B conflict structure and acquisition-controlled overwrite metrics.
3. Preliminaries and Problem Formulation
3.1. Memory-Conditioned Response Generation
Weconsideralong-runninglanguageagentthatreceivesaquery xandgeneratesaresponse yusingboth
the parametric model and accumulated memory. The relevant memory is not homogeneous. Permanent
facts P={(k i,v p i )}n i=1 encode stable user facts or durable task preferences whose values should remain
valid across future interactions. Temporary factsT={(k j,v t j)}m j=1 encode local assumptions, task-
specific conditions, or counterfactual instructions whose values should apply only within the current
context.
A response therefore depends on both semantic relevance and information lifecycle. A permanent
query should recovervp i even after later local context is written, whereas a temporary query should
follow the active temporary valuevt j. The hard case occurs when temporary and permanent facts share
the same semantic attribute but assign conflicting values. The model must use the temporary value for
the local response without making it authoritative for future permanent queries.
4

3.2. Lifecycle Conflict in Compact Online Memory
A broad class of neural memory methods compresses interaction history into a compact online state. At
injected layerl, we write this state asS(l) t ∈R r×r. Given hidden stateht, the memory module produces
qm t =norm(W m q ht),
km t =norm(W m k ht),v m t =W m v ht.
The state is read aszt =S t−1qm t and injected back into the model computation. A token-level write
gateβ t =σ(W βht +b β)and keep coefficientλ t =1−β t define a common delta-style update:
St =diag(λ t)St−1 +diag(β t)(vm t −S t−1km t )(k m t )⊤.
This abstraction covers compact neural memory adapters that read and write a shared low-rank state,
includingδ-Mem.
The lifecycle conflict appears when the same state stores both lifecycles. After Phase A, stateSA should
contain permanent facts; after Phase B, stateSAB includes temporary overwrites. If both phases use the
same rows and write dynamics, Phase B can erase or re-rank evidence for the Phase-A value. We call
thistemporary overwrite: after writing a temporary value, the memory state answers a later permanent
query with that temporary value.
This failure differs from ordinary acquisition failure, where the permanent value may never have been
stored. We therefore evaluate retention only on facts acquired after Phase A. LetAi =1 if the model
answers thei-th permanent query correctly after Phase A, and letRi =1 if it still returns the permanent
value after Phase B. The acquisition-controlled retention is
Retacq =
∑︀
i 1[A i =1∧R i =1]∑︀
i 1[A i =1] .
The overwrite rate is computed on the same acquired subset, counting answers equal to the conflicting
temporary value. This protocol isolates the lifecycle question: once a permanent fact has been acquired,
does a temporary write incorrectly become authoritative?
4. LifeFuse-Mem
4.1. Framework Overview
LifeFuse-Mem adds a lifecycle boundary to compact neural memory. The framework has three parts,
shown in Figure 2. First, it learns a plastic/stable subspace partition inside each online memory state.
Second, a supervised permanent router controls how strongly write tokens can update the stable rows.
Third, phase-aware protected-state readout is used only in the controlled overwrite-attribution protocol,
where phase boundaries and query lifecycles are known in advance, to evaluate whether preserved
evidence can be recovered after conflicting temporary writes. Thus, lifecycle control is applied at
writing, training, and readout, without returning answers from an external key–value table.
4.2. Lifecycle-Aware Subspace Partition
A fixed split of raw rank dimensions is arbitrary, so LifeFuse-Mem learns an approximately orthogonal
basis for the memory coordinates in each injected attention module. LetRl ∈R r×r be a learned square
matrix and letQl =orth(R l) be the orthogonalized basis used in the forward pass, withQ⊤ l Ql =I
5

up to numerical precision. The memory read, key, and value vectors are rotated into this basis before
subspace-specific control:
˜qt =Q ⊤ l qm t , ˜kt =Q ⊤ l km t , ˜vt =Q ⊤ l vm t .
The first rA coordinates define the plastic subspaceA, and the remainingrB =r−r A coordinates
define the stable subspaceB. In the experiments,r=8 and the split isrA =r B =4 . The raw rotation
parameter is regularized by
Lorth = 1 Lr2 L∑︁ l=1 ∥R⊤ l Rl −I∥ 2 F,
where L is the number of injected memory modules. The1/r2 factor matches the elementwise mean
used in the implementation and does not change the minimizer. This regularizer keeps the subspaces
separable while allowing the model to learn a coordinate system more suitable than raw rank indices.
The underlying state is the same compact associative state used byδ-Mem. For a single memory module,
St ∈R r×r is read and updated online. Before tokentwrites, the memory read is
zt =S t−1 ˜qt.
With row-wise keep, erase, and write coefficientsκt,ϵ t,ω t ∈R r, the affine update is
St =κ t ⊙row St−1 −ϵ t ⊙row
[︁
(St−1 ˜kt)˜k⊤ t
]︁
+ω t ⊙row
[︁
˜vt ˜k⊤ t
]︁
.
The read vector is rotated back before it is projected into the active attention heads.
4.3. Permanent Routing and Subspace Writing
For each write token, LifeFuse-Mem predicts a permanent-route weight
ρt =σ(w ⊤ r ht +b r).
In the implemented training data, the route target comes from the episode metadata. If the target
lifecycle is permanent, valid write tokens in that example receiveyi =1 ; if it is temporary, they receive
yi =0; examples without a lifecycle type are masked. The route supervision loss is
Lroute =− 1 |Ω| ∑︁ (i,t)∈Ω [yi logρ i,t + (1−yi)log(1−ρ i,t)] ,
whereΩis the set of valid routed write tokens.
The router affects writing through row scaling. Plastic rows remain writable for all tokens. Stable rows
use an interpolation between a temporary scaleatmp and a permanent scaleaperm:
at,j =
{︃
1,j≤r A,
atmp +ρ t(aperm −a tmp),j>r A.
For the main LifeFuse-Mem runs, the implementation uses thepermanent_boostmode withatmp =0
and aperm =1 . Under the standard δ-Mem update this row scale turns the base coefficients into
κt,j =1−a t,j +a t,j λt,j and ϵt,j =ω t,j =a t,j βt,j. Thus tokens with highρt can update both plastic and
stable rows, while tokens with lowρt primarily update the plastic rows because stable-row erase and
write coefficients are suppressed. The implementation also applies subspace key isolation: during
ordinary online writing, stable key coordinates are attenuated (0.5 in the reproduced runs), so writes
prefer plastic coordinates on the key axis as well. This design does not hard-code a separate memory
module for each lifetime; instead, route labels, row scaling, key isolation, and downstream ranking
losses encourage lifecycle-aware separation under explicit route supervision.
6

4.4. Episodic Learning Objective
LifeFuse-Mem is trained with an episodic write-then-read objective. The model first consumes write
messages and updates memory toSwrite. It then answers the final assistant target with further writing
disabled, forcing the answer to depend on the stored state rather than updating memory during the
read. The full objective is
L=L CE +λ route Lroute +λ orth Lorth
+λhc(u)L hc +λ retLret +λ sp Lsp .
where u is training progress. The cross-entropy term trains the adapter state to support the target
answer after context writing.
The hard candidate loss improves candidate discrimination. Given the correct answery+ and a hard
negative y−, we compute their average answer cross-entropiesCE+ and CE−. The objective encourages
the negative candidate to have loss at leastmhc larger than the correct candidate:
Lhc =τ hc softplus
(︂ mhc −(CE − −CE +)
τhc
)︂
.
This loss is ramped in after early answer learning has stabilized. For permanent examples, a retention-
ranking loss with the same form uses its own marginmret and temperatureτret, giving extra pressure for
the permanent value to outrank the temporary or rejected candidate. Finally, a sparsity penalty keeps
the average write gate near a small targetβ0 (0.05 in the reproduced runs), discouraging unnecessary
memory updates on every token.
4.5. Protected State Fusion and Lifecycle Readout
This component is specific to the controlled overwrite-attribution protocol and should not be interpreted
as autonomous lifecycle discovery. In that setting, LifeFuse-Mem checkpoints the memory state after
Phase A asSA and also keeps the post-overwrite stateSAB. It then constructs a stable-row protected
stateS stable by taking plastic rows fromSAB and stable rows fromSA:
Sstable[..., :r A, :] =SAB[..., :r A, :],
Sstable[...,r A :, :] =SA[...,r A :, :].
Thus, Sstable preserves the part of memory intended to carry long-lived facts while retaining recent
plastic context.
For a permanent query, the model scores each candidatey∈ Cunder bothSA and Sstable. The candidate
score is the length-normalized token log probability
sS(y) = 1 |y|
|y|∑︁
τ=1
logp θ(yτ |x,y <τ,S).
The two component scores are
sA(y) =sSA (y),
sstable(y) =sSstable(y).
The final permanent-query score is
sfuse(y) =αs A(y) + (1−α)sstable(y),
7

and the selected answer is
ˆy=arg max
y∈C
sfuse(y).
For a temporary query, LifeFuse-Mem does not protect or fuse the state; it scores candidates with
the full post-overwrite stateSAB. The readout therefore matches the intended lifecycle of the query:
permanent queries consult protected evidence, whereas temporary queries follow the local overwrite.
5. Experiments
5.1. Experimental Setup
Experimental DesignWe evaluate LifeFuse-Mem from three angles. First, we use a targeted
temporary-overwrite benchmark to test whether permanent facts remain recoverable after conflicting
temporary writes. Second, we evaluate on public long-memory benchmarks to check whether the
proposed lifecycle boundary preserves general memory behavior outside the controlled overwrite
setting. Third, we ablate the main components on the targeted benchmark to identify the source of the
retention effect.
Evaluation ProtocolWe report results on Qwen3-4B and SmolLM3-3B. The controlled temporary-
overwrite benchmark is our main diagnostic experiment, while LoCoMo and MemoryAgentBench test
compatibility with standard long-memory evaluation. All comparisons are made within the same
backbone and use the same data split, prompting format, scoring protocol, and memory rank. Trained
adapters share the same 3,243-sample training set and optimization setup, with details provided in the
Appendix file. LifeFuse-Mem additionally uses episode-level lifecycle metadata for route supervision,
so we include a no-route-supervision ablation to isolate this signal.
Shared Memory ConfigurationAll comparison experiments use the same rank-8 LoRA configuration
for the corresponding backbone. LifeFuse-Mem changes only the lifecycle-aware components: it splits
therankintofourplasticandfourstabledimensions, learnsanorthogonalbasisforthispartition, enables
token-level permanent routing, and uses the losses defined in Section 4. The basis is orthonormalized
by QR decomposition at each forward pass; the orthogonal regularizer acts on the underlying parameter
and is not the source of exact orthogonality. On Hard Attribution Anti-Overwrite, where Phase-A/Phase-
B boundaries and query lifecycles are known, permanent queries use phase-aware fusion readout:
LifeFuse-Mem fuses the Phase-A state with a stable-row-protected post-overwrite state, where plastic
rows come from the post-overwrite state and stable rows are restored from Phase A. Temporary queries
use the full post-overwrite state. The main fusion weight isα=0.70 ; the Appendix file provides the
detailed sensitivity ablation. On LoCoMo and MemoryAgentBench, which do not provide overwrite
phases or query lifecycle labels, LifeFuse-Mem is evaluated in standard online-memory mode: the
model consumes the benchmark history with normal memory writes and answers from the resulting
memory state, without Phase-A checkpointing, stable-row restoration, or query-type-specific fusion.
5.2. Hard Attribution Anti-Overwrite
Benchmark and MetricsWe construct a 1,000-episode Hard Attribution Anti-Overwrite benchmark
to measure the target failure mode directly. Each episode writes permanent facts in Phase A and then
introduces conflicting temporary facts in Phase B. Permanent queries should recover the Phase-A value,
whereas temporary queries should follow the Phase-B value. This separates stable-fact retention from
local adaptation to temporary context.
8

Table 1: Results on Hard Attribution Anti-Overwrite. Scores are percentages. Ret. and Ovr. are
acquisition-controlled metrics computed only over conflict-permanent facts answered correctly after
Phase A; under this choice protocol, they are complementary. Temp. is an auxiliary sanity check on
temporary-query behavior. Higher is better except Ovr.
Model Permanent Query Temp. (aux.)
Perm. Ret. Ovr.↓Temp.
Qwen3-4B
+ LoRA-Mem 19.65 61.03 38.97 20.13
+ Titans 19.65 58.02 41.98 20.23
+δ-Mem 19.32 57.72 42.2820.27
+ LifeFuse-Mem20.12 63.71 36.2920.10
SmolLM3-3B
+ LoRA-Mem 19.68 61.14 38.86 19.95
+ Titans 19.82 61.71 38.29 19.88
+δ-Mem19.9560.27 39.73 20.18
+ LifeFuse-Mem 19.6569.39 30.61 20.35
Table 2: Results on public memory benchmarks. Scores are percentages. MAB denotes MemoryAgent-
Bench. Bold values indicate the best method under the same backbone and benchmark category.
Model MemoryAgentBench LoCoMo
Avg. AR TTL LRU SF Avg. Multi Temp. Open Single
Qwen3-4B
+ LoRA-Mem 31.46 38.80 23.93 46.37 16.50 39.95 28.57 28.05 15.19 51.14
+ Titans 30.56 40.00 18.86 46.25 17.13 34.33 26.60 21.64 13.26 44.17
+δ-Mem 31.8340.2021.0046.52 17.2541.24 29.78 29.57 14.57 52.57
+ LifeFuse-Mem32.24 40.20 24.0045.30 16.7542.41 33.62 30.71 16.17 52.81
SmolLM3-3B
+ LoRA-Mem 19.85 25.25 8.5737.2012.50 30.79 21.69 23.40 14.35 38.53
+ Titans 19.3927.854.79 37.17 7.75 23.82 20.82 16.95 12.82 28.70
+δ-Mem 20.13 25.55 8.50 37.1213.1330.65 22.38 23.19 14.99 38.06
+ LifeFuse-Mem20.2125.859.0536.55 12.3738.30 28.47 27.08 18.50 48.14
The benchmark is intentionally difficult. Queries use natural-language aliases rather than canonical
keys, some answers require cross-sentence attribution, both phases contain noise facts, conflicts may
be indirect, and queries are scored with hard-candidate choice sets. Each episode contains two entities,
four protected facts per entity, six conflict keys, four overwrite rounds, and noise facts in both phases.
Table 1 reports four metrics.Perm.is final accuracy on all permanent queries after Phase B, using the
Phase-A value as the target. Because this metric also depends on initial acquisition, we additionally
report acquisition-controlled metrics over conflict-permanent facts answered correctly after Phase A.
Ret.is the fraction of this acquired subset still answered with the permanent value after Phase B.Ovr.
is the fraction answered with the conflicting temporary value after Phase B; lower is better. In the
released hard-candidate choice evaluation, each acquired conflict-permanent query is ranked over
the Phase-A permanent answer and four temporary overwrite candidates. Under this protocol, Ret.
9

and Ovr. are complementary; this complementarity is not a general property of the metrics under
open-generation or mixed-distractor evaluations.Temp.is final accuracy on temporary queries, using
the Phase-B value as the target. We report Temp. as an auxiliary sanity check on Phase-B behavior, not
as the main criterion for overwrite. Ret. does not measure how many facts are acquired initially, so it
should be read together with Perm.
ResultsTable 1 shows the clearest gain on the acquisition-controlled metrics. Compared withδ-Mem,
LifeFuse-Mem raises Ret. from 57.72% to 63.71% on Qwen3-4B and from 60.27% to 69.39% on
SmolLM3-3B. Ovr. decreases in parallel, from 42.28% to 36.29% on Qwen3-4B and from 39.73% to
30.61% on SmolLM3-3B. Thus, among facts that were already acquired after Phase A, LifeFuse-Mem is
less likely to answer with the conflicting temporary value after Phase B.
End-to-endpermanent-queryaccuracychangesonlymarginally: itincreasesonQwen3-4B,from19.32%
to 20.12%, but changes from 19.95% to 19.65% on SmolLM3-3B. This indicates that LifeFuse-Mem
primarily improves overwrite resistance conditional on successful acquisition, rather than substantially
improving the overall probability of answering permanent queries correctly end to end. Temp. remains
similar across methods, which is consistent with the retention gain not coming from simply suppressing
Phase-B information. Accordingly, Ret. and Ovr. should be interpreted as diagnostic measures of
overwrite behavior, not as substitutes for end-to-end task accuracy.
Table 3: Component ablations on Hard Attribution Anti-Overwrite. Scores are percentages. Ret. and
Ovr. are acquisition-controlled and complementary under the released hard-candidate choice protocol;
Temp. is auxiliary; lower Ovr. is better.
Model Permanent Query Temp. (aux.)
Perm. Ret. Ovr.↓Temp.
Qwen3-4B
+ LifeFuse-Mem20.1263.71 36.29 20.10
w/o route sup. 19.88 58.68 41.32 19.98
w/o stable rows 19.93 62.79 37.21 20.10
w/o hard cand. 19.2864.09 35.91 20.55
w/o ret. loss 20.00 62.37 37.63 19.15
SmolLM3-3B
+ LifeFuse-Mem 19.6569.39 30.6120.35
w/o route sup. 19.62 59.45 40.5520.38
w/o stable rows 19.72 68.47 31.53 20.22
w/o hard cand. 19.98 69.04 30.96 20.35
w/o ret. loss20.1065.74 34.26 19.98
5.3. Long-Memory Benchmarks
Benchmark and MetricsWe next evaluate whether the lifecycle boundary remains compatible with
public long-memory tasks. This is a compatibility check rather than a direct anti-overwrite test: a
method could protect old facts on the targeted benchmark while degrading standard memory behavior.
We use LoCoMo and MemoryAgentBench. LoCoMo is evaluated with full-history replay on categories
1–4, covering 1,540 questions, and reports overall, multi-hop, temporal, open-domain, and single-hop
scores. MemoryAgentBench contains 3,671 questions from 14 datasets, grouped into Accurate Retrieval
(AR), Test-time Learning (TTL), Long Range Understanding (LRU), and Selective Forgetting (SF).
10

For MemoryAgentBench, we use a unified prompt template, temperature 0.4, top-p 0.9, top-k 10,
maximum generation length 4,096, maximum context length 120,000 characters, and evaluation batch
size 16. Its overall score is the sample-weighted category average. Since these public benchmarks do
not annotate information lifecycles or controlled overwrite phases, no protected-state fusion is used in
this evaluation. The learned router and subspace partition remain active as part of the memory adapter,
but no benchmark-specific lifecycle labels are supplied at inference time.
ResultsTable 2 reports compatibility results on public long-memory benchmarks. LifeFuse-Mem
remains broadly competitive: relative toδ-Mem on Qwen3-4B, LoCoMo improves from 41.24% to
42.41% and MemoryAgentBench increases slightly from 31.83% to 32.24%. Category-level results
vary: TTL improves from 21.00% to 24.00%, AR ties at 40.20%, while LRU and SF decrease from
46.52% to 45.30% and from 17.25% to 16.75%, respectively.
Relative toδ-Mem on SmolLM3-3B, LifeFuse-Mem also improves LoCoMo overall score, from 30.65% to
38.30%, with gains in all LoCoMo categories. On MemoryAgentBench, the overall score is again close
to δ-Mem, increasing slightly from 20.13% to 20.21%. AR and TTL improve from 25.55% to 25.85%
and from 8.50% to 9.05%, while LRU and SF decrease from 37.12% to 36.55% and from 13.13%
to 12.37%, respectively. This suggests that the lifecycle boundary improves some public-benchmark
categories while reducing others, so its benefits are not uniform across all MemoryAgentBench task
types.
Neither LoCoMo nor MemoryAgentBench instantiates the Phase-A/Phase-B overwrite structure or
separates permanent from temporary queries. They should therefore be interpreted as compatibility
checks for running the trained lifecycle-aware memory adapter under ordinary long-memory inference,
not as direct evidence for the phase-aware anti-overwrite readout. The targeted benchmark provides the
direct anti-overwrite evidence; the public benchmarks show how the same trained memory architecture
affects general long-memory behavior when explicit lifecycle boundaries are absent.
5.4. Ablation Studies
Component AblationsWe ablate four components on the 1,000-episode Hard Attribution benchmark:
routesupervision, stablerows, hardcandidateloss, andpermanentretentionloss. Eachablationremoves
one component and keeps the remaining training and inference settings unchanged. We report the same
metrics as in Section 5.2 to measure retention and overwrite under the same acquisition-controlled
protocol. The main fusion weight isα=0.70 ; the Appendix file reports the detailed weight-sensitivity
ablation.
Ablation ResultsTable 3 identifies route supervision as the most important component. Removing it
decreases retention from 63.71% to 58.68% on Qwen3-4B and from 69.39% to 59.45% on SmolLM3-
3B; overwrite rises to 41.32% and 40.55%, respectively. This indicates that rank partitioning alone is
insufficient: token-level permanent routing provides the signal that makes the subspaces lifecycle-aware.
The remaining components contribute in more model-dependent ways. Removing stable rows or
permanent retention loss consistently weakens acquisition-controlled retention relative to the full
model on both backbones. Removing hard candidate loss is not uniformly beneficial or harmful. On
Qwen3-4B, Ret. and Ovr. improve slightly, but end-to-end Perm. drops from 20.12% to 19.28%,
indicating a trade-off between the acquired subset and final permanent-query accuracy. On SmolLM3-
3B, its effect is small relative to route supervision and retention loss. Overall, the ablations identify
route supervision as the most reliable contributor to acquisition-controlled retention. Stable rows and
11

the retention loss provide additional but smaller gains, while the hard-candidate loss mainly affects
candidate calibration and does not uniformly improve Ret. or Ovr. Thus, the evidence supports the
role of route-conditioned isolation, but does not imply that every auxiliary objective is necessary for
every metric.
6. Conclusion
This work studies temporary overwrite as a lifecycle mismatch failure mode in compact online memory
and introduces LifeFuse-Mem as a targeted mitigation framework. By combining lifecycle-aware
routing, subspace isolation, and protected readout, LifeFuse-Mem reduces acquisition-conditioned
overwrite on the controlled Hard Attribution Anti-Overwrite benchmark. Results on LoCoMo and
MemoryAgentBench indicate that the trained adapter remains compatible with standard long-memory
evaluation when protected-state fusion is not available, although the gains vary across backbones and
task categories. Ablation studies identify route supervision as the most reliable source of the retention
gains, with stable rows, protected fusion, and auxiliary losses contributing more selectively. Overall,
the results support explicit lifecycle modeling as a useful diagnostic and architectural principle for
long-term memory, while leaving lifecycle inference from unlabeled interaction histories to future work.
References
Yushi Bai, Shangqing Tu, Jiajie Zhang, Hao Peng, Xiaozhi Wang, Xin Lv, Shulin Cao, Jiazheng Xu,
Lei Hou, Yuxiao Dong, Jie Tang, and Juanzi Li. LongBench v2: Towards deeper understanding
and reasoning on realistic long-context multitasks. In Wanxiang Che, Joyce Nabende, Ekaterina
Shutova, and Mohammad Taher Pilehvar, editors,Proceedings of the 63rd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), pages 3639–3664, Vienna, Austria,
July 2025. Association for Computational Linguistics. ISBN 979-8-89176-251-0. doi: 10.18653/v1/
2025.acl-long.183. URLhttps://aclanthology.org/2025.acl-long.183/.
Ali Behrouz, Peilin Zhong, and Vahab Mirrokni. Titans: Learning to memorize at test time.Advances in
Neural Information Processing Systems, 38:113506–113543, 2026.
Jiayang CHENG, Dongyu Ru, Lin Qiu, Yiyang Li, Xuezhi Cao, Yangqiu SONG, and Xunliang Cai.
Amemgym: Interactive memory benchmarking for assistants in long-horizon conversations. InPaper
presented at The 14th International Conference on Learning Representations (ICLR 2026), Rio de Janeiro,
Brazil, 2026.
Yiruo Cheng, Kelong Mao, Ziliang Zhao, Guanting Dong, Hongjin Qian, Yongkang Wu, Tetsuya Sakai, Ji-
Rong Wen, and Zhicheng Dou. CORAL: Benchmarking multi-turn conversational retrieval-augmented
generation. In Luis Chiruzzo, Alan Ritter, and Lu Wang, editors,Findings of the Association for
Computational Linguistics: NAACL 2025, pages 1308–1330, Albuquerque, New Mexico, April 2025.
Association for Computational Linguistics. ISBN 979-8-89176-195-7. doi: 10.18653/v1/2025.
findings-naacl.72. URLhttps://aclanthology.org/2025.findings-naacl.72/.
Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, and Deshraj Yadav. Mem0: Building
production-ready ai agents with scalable long-term memory.arXiv preprint arXiv:2504.19413, 2025.
Chenlong Deng, Zhisong Zhang, Kelong Mao, Shuaiyi Li, Xinting Huang, Dong Yu, and Zhicheng Dou.
A silver bullet or a compromise for full attention? a comprehensive study of gist token-based context
compression. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar,
editors,Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume
12

1: Long Papers), pages 4861–4879, Vienna, Austria, July 2025. Association for Computational
Linguistics. ISBN 979-8-89176-251-0. doi: 10.18653/v1/2025.acl-long.241. URL https://
aclanthology.org/2025.acl-long.241/.
Yujie Feng, Xujia Wang, Zexin Lu, Shenghong Fu, Guangyuan Shi, Yongxin Xu, Yasha Wang, Philip S.
Yu, Xu Chu, and Xiao-Ming Wu. Recurrent knowledge identification and fusion for language model
continual learning. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher
Pilehvar, editors,Proceedings of the 63rd Annual Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 27396–27413, Vienna, Austria, July 2025. Association for
Computational Linguistics. ISBN 979-8-89176-251-0. doi: 10.18653/v1/2025.acl-long.1328. URL
https://aclanthology.org/2025.acl-long.1328/.
Tianyu Gao, Alexander Wettig, Howard Yen, and Danqi Chen. How to train long-context language
models (effectively). InProceedings of the 63rd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 7376–7399, 2025.
Zifan He, Yingqi Cao, Zongyue Qin, Neha Prakriya, Yizhou Sun, and Jason Cong. HMT: Hierarchical
memory transformer for efficient long context language processing. In Luis Chiruzzo, Alan Ritter,
and Lu Wang, editors,Proceedings of the 2025 Conference of the Nations of the Americas Chapter
of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long
Papers), pages 8068–8089, Albuquerque, New Mexico, April 2025. Association for Computational
Linguistics. ISBN 979-8-89176-189-6. doi: 10.18653/v1/2025.naacl-long.410. URL https:
//aclanthology.org/2025.naacl-long.410/.
Mengkang Hu, Tianxing Chen, Qiguang Chen, Yao Mu, Wenqi Shao, and Ping Luo. HiAgent: Hier-
archical working memory management for solving long-horizon agent tasks with large language
model. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar,
editors,Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 32779–32798, Vienna, Austria, July 2025. Association for Com-
putational Linguistics. ISBN 979-8-89176-251-0. doi: 10.18653/v1/2025.acl-long.1575. URL
https://aclanthology.org/2025.acl-long.1575/.
Yuanzhe Hu, Yu Wang, and Julian McAuley. Evaluating memory in LLM agents via incremental multi-
turn interactions. InThe Fourteenth International Conference on Learning Representations, 2026. URL
https://openreview.net/forum?id=DT7JyQC3MR.
Bowen Jin, Jinsung Yoon, Jiawei Han, and Sercan Arik. Long-context llms meet rag: Overcoming
challenges for long inputs in rag. InInternational Conference on Learning Representations, volume
2025, pages 37784–37822, 2025.
Jiazheng Kang, Mingming Ji, Zhe Zhao, and Ting Bai. Memory OS of AI agent. In Christos
Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng, editors,Proceedings of the
2025 Conference on Empirical Methods in Natural Language Processing, pages 25961–25970, Suzhou,
China, November 2025. Association for Computational Linguistics. ISBN 979-8-89176-332-6. doi:
10.18653/v1/2025.emnlp-main.1318. URL https://aclanthology.org/2025.emnlp-main.
1318/.
Jingdi Lei, Di Zhang, Junxian Li, Weida Wang, Kaixuan Fan, Xiang Liu, Qihan Liu, Xiaoteng Ma, Baian
Chen, and Soujanya Poria.δ-Mem: Efficient online memory for large language models.arXiv preprint
arXiv:2605.12357, 2026.
13

Jeffrey Li, Mohammadreza Armandpour, Seyed Iman Mirzadeh, Sachin Mehta, Vaishaal Shankar,
Raviteja Vemulapalli, Samy Bengio, Oncel Tuzel, Mehrdad Farajtabar, Hadi Pouransari, and Fartash
Faghri. TiC-LM: A web-scale benchmark for time-continual LLM pretraining. In Wanxiang Che, Joyce
Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors,Proceedings of the 63rd Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 32231–32273,
Vienna, Austria, July 2025. Association for Computational Linguistics. ISBN 979-8-89176-251-0. doi:
10.18653/v1/2025.acl-long.1551. URL https://aclanthology.org/2025.acl-long.1551/.
Huanxuan Liao, Shizhu He, Yupu Hao, Yequan Wang, Wenhao Teng, Xiangwen Liao, Jun Zhao,
and Kang Liu. Spectral disentanglement: Rank-aware task adaptation for rehearsal-free continual
learning in LLMs. In Maria Liakata, Viviane P. Moreira, Jiajun Zhang, and David Jurgens, editors,
Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1:
Long Papers), pages 7360–7376, San Diego, California, United States, July 2026. Association for
Computational Linguistics. ISBN 979-8-89176-390-6. doi: 10.18653/v1/2026.acl-long.334. URL
https://aclanthology.org/2026.acl-long.334/.
Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov, Mohit Bansal, Francesco Barbieri, and Yuwei
Fang. Evaluating very long-term conversational memory of LLM agents. In Lun-Wei Ku, Andre
Martins, and Vivek Srikumar, editors,Proceedings of the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), pages 13851–13870, Bangkok, Thailand,
August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-long.747. URL
https://aclanthology.org/2024.acl-long.747/.
Ali Modarressi, Hanieh Deilamsalehy, Franck Dernoncourt, Trung Bui, Ryan A. Rossi, Seunghyun Yoon,
and Hinrich Schuetze. NoLiMa: Long-context evaluation beyond literal matching. In Aarti Singh,
Maryam Fazel, Daniel Hsu, Simon Lacoste-Julien, Felix Berkenkamp, Tegan Maharaj, Kiri Wagstaff,
and Jerry Zhu, editors,Proceedings of the 42nd International Conference on Machine Learning, volume
267 ofProceedings of Machine Learning Research, pages 44554–44570. PMLR, 13–19 Jul 2025. URL
https://proceedings.mlr.press/v267/modarressi25a.html.
Kai Tzu-iunn Ong, Namyoung Kim, Minju Gwak, Hyungjoo Chae, Taeyoon Kwon, Yohan Jo, Seung-won
Hwang, Dongha Lee, and Jinyoung Yeo. Towards lifelong dialogue agents via timeline-based memory
management. InProceedings of the 2025 Conference of the Nations of the Americas Chapter of the
Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers),
pages 8631–8661, 2025.
Haoran Tan, Zeyu Zhang, Chen Ma, Xu Chen, Quanyu Dai, and Zhenhua Dong. MemBench: Towards
more comprehensive evaluation on the memory of LLM-based agents. In Wanxiang Che, Joyce
Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors,Findings of the Association for
Computational Linguistics: ACL 2025, pages 19336–19352, Vienna, Austria, July 2025a. Association
for Computational Linguistics. ISBN 979-8-89176-256-5. doi: 10.18653/v1/2025.findings-acl.989.
URLhttps://aclanthology.org/2025.findings-acl.989/.
Zhen Tan, Jun Yan, I-Hung Hsu, Rujun Han, Zifeng Wang, Long Le, Yiwen Song, Yanfei Chen, Hamid
Palangi, George Lee, Anand Rajan Iyer, Tianlong Chen, Huan Liu, Chen-Yu Lee, and Tomas Pfister.
In prospect and retrospect: Reflective memory management for long-term personalized dialogue
agents. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors,
Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), pages 8416–8439, Vienna, Austria, July 2025b. Association for Computational Linguistics.
ISBN 979-8-89176-251-0. doi: 10.18653/v1/2025.acl-long.413. URLhttps://aclanthology.
14

org/2025.acl-long.413/.
Yu Wang, Dmitry Krotov, Yuanzhe Hu, Yifan Gao, Wangchunshu Zhou, Julian Mcauley, Dan Gutfreund,
Rogerio Feris, and Zexue He. M+: Extending MemoryLLM with scalable long-term memory. In
Aarti Singh, Maryam Fazel, Daniel Hsu, Simon Lacoste-Julien, Felix Berkenkamp, Tegan Maharaj,
Kiri Wagstaff, and Jerry Zhu, editors,Proceedings of the 42nd International Conference on Machine
Learning, volume 267 ofProceedings of Machine Learning Research, pages 63308–63323. PMLR,
13–19 Jul 2025a. URLhttps://proceedings.mlr.press/v267/wang25au.html.
Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, and Graham Neubig. Agent workflow memory. In
Aarti Singh, Maryam Fazel, Daniel Hsu, Simon Lacoste-Julien, Felix Berkenkamp, Tegan Maharaj,
Kiri Wagstaff, and Jerry Zhu, editors,Proceedings of the 42nd International Conference on Machine
Learning, volume 267 ofProceedings of Machine Learning Research, pages 63897–63911. PMLR,
13–19 Jul 2025b. URLhttps://proceedings.mlr.press/v267/wang25bx.html.
Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, and Dong Yu. Longmemeval:
Benchmarking chat assistants on long-term interactive memory. 2024. URLhttps://arxiv.org/
abs/2410.10813.
Xiaodong Wu, Minhao Wang, Yichen Liu, Xiaoming Shi, He Yan, Lu Xiangju, Junmin Zhu, and
Wei Zhang. LIFBench: Evaluating the instruction following performance and stability of large
language models in long-context scenarios. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova,
and Mohammad Taher Pilehvar, editors,Proceedings of the 63rd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), pages 16445–16468, Vienna, Austria, July
2025. Association for Computational Linguistics. ISBN 979-8-89176-251-0. doi: 10.18653/v1/2025.
acl-long.803. URLhttps://aclanthology.org/2025.acl-long.803/.
Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, and Yongfeng Zhang. A-mem: Agentic
memory for llm agents.Advances in Neural Information Processing Systems, 38:17577–17604, 2026.
Yutao Yang, Jie Zhou, Xuanwen Ding, Tianyu Huai, Shunyu Liu, Qin Chen, Yuan Xie, and Liang He.
Recent advances of foundation language models-based continual learning: A survey.ACM Computing
Surveys, 57(5):1–38, 2025a.
Zeyuan Yang, Fangzhou Xiong, Peng Li, and Yang Liu. Rethinking long context generation from the
continuallearningperspective. InOwenRambow, LeoWanner, MariannaApidianaki, HendAl-Khalifa,
Barbara Di Eugenio, and Steven Schockaert, editors,Proceedings of the 31st International Conference
on Computational Linguistics, pages 1922–1933, Abu Dhabi, UAE, January 2025b. Association for
Computational Linguistics. URLhttps://aclanthology.org/2025.coling-main.131/.
Rui Ye, Zhongwang Zhang, Kuan Li, Huifeng Yin, Zhengwei Tao, Yida Zhao, Liangcai Su, Liwen Zhang,
Zile Qiao, Xinyu Wang, et al. Agentfold: Long-horizon web agents with proactive context folding. In
The Fourteenth International Conference on Learning Representations, 2026.
Howard Yen, Tianyu Gao, Minmin Hou, Ke Ding, Daniel Fleischer, Peter Izsak, Moshe Wasserblat, and
Danqi Chen. Helmet: How to evaluate long-context language models effectively and thoroughly.
2024.
Fabio Massimo Zanzotto, Elena Sofia Ruzzetti, Giancarlo A. Xompero, Leonardo Ranaldi, Davide
Venditti, Federico Ranaldi, Cristina Giannone, Andrea Favalli, and Raniero Romagnoli. Position
paper: MeMo: Towards language models with associative memory mechanisms. In Wanxiang Che,
JoyceNabende, EkaterinaShutova, andMohammadTaherPilehvar, editors,Findings of the Association
15

for Computational Linguistics: ACL 2025, pages 15169–15180, Vienna, Austria, July 2025. Association
for Computational Linguistics. ISBN 979-8-89176-256-5. doi: 10.18653/v1/2025.findings-acl.785.
URLhttps://aclanthology.org/2025.findings-acl.785/.
Zeyu Zhang, Quanyu Dai, Luyu Chen, Zeren Jiang, Rui Li, Jieming Zhu, Xu Chen, Yi Xie, Zhenhua
Dong, and Ji-Rong Wen. Memsim: A bayesian simulator for evaluating memory of llm-based personal
assistants. In D. Belgrave, C. Zhang, H. Lin, R. Pascanu, P. Koniusz, M. Ghassemi, and N. Chen,
editors,Advances in Neural Information Processing Systems, volume 38, pages 90475–90511. Curran
Associates, Inc., 2025. URLhttps://proceedings.neurips.cc/paper_files/paper/2025/
file/826aea2253363fe04e8c4991b2a8869e-Paper-Conference.pdf.
Xinping Zhao, Yan Zhong, Zetian Sun, Xinshuo Hu, Zhenyu Liu, Dongfang Li, Baotian Hu, and Min
Zhang. Funnelrag: A coarse-to-fine progressive retrieval paradigm for rag. InFindings of the
Association for Computational Linguistics: NAACL 2025, pages 3029–3046, 2025.
16
