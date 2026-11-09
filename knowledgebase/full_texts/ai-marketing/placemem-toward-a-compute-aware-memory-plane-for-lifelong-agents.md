---
title: 'PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents'
url: https://arxiv.org/abs/2607.04089
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Sukanta Ganguly
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.04089
pages: 6
chars: 19154
fetched_at: '2026-11-08T13:36:22+00:00'
kb_version: 1
---

# PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents

Preprint. Under review.
PLACEMEM: Toward a Compute-Aware Memory Plane for
Lifelong Agents
Sukanta Ganguly, Ph.D
sukantag@netapp.com
Abstract
Lifelong agents need more than larger context windows and better retrieval.
They need memories that can persist, evolve, and be corrected without
forcing the serving stack to recompute the same history on every turn or
silently reuse stale runtime state. We present PLACEMEMas a systems posi-
tion on lifelong-agent memory, instantiated by an executable control-plane
prototype. The central claim is that agent memory should be represented as
versionedcapsulesthat unify semantics, provenance, validity, and reusable
runtime state under one correction-aware identity. In the current prototype,
capsules drive prompt-level text retrieval, KV-aware routing, and cascading
invalidation over live streamed backends; prospective layer-frontier replay
is intentionally framed as a deeper integration agenda rather than a claimed
engine feature. We describe a vLLM-first prototype with persistent capsule
state, concurrency-safe invalidation, an OpenAI-compatible routing sidecar,
a typed metadata contract, and a benchmark harness that measures live
first-token latency, reuse, and post-correction behavior. The result is both
an executable artifact that demonstrates correction-aware control-plane be-
havior today and a concrete roadmap for replay-aware serving integration
in future lifelong-agent systems.
1 Introduction
Lifelong agents are emerging as a unifying target for language-model systems: they must
remember users, refine beliefs, revise plans, accumulate tool experience, and stay responsive
under repeated interaction. Recent systems have shown that memory improves planning,
reflection, and multi-session behavior for language agents (Park et al., 2023; Shinn et al.,
2023; Packer et al., 2024). In parallel, serving systems such as vLLM have substantially
improved the runtime efficiency of large language model (LLM) inference through better
KV management and batching (Kwon et al., 2023). However, these two lines of work still
optimize disjoint layers of the stack, which makes it difficult to evaluate memory quality
and systems efficiency within one coherent architecture.
The first layer issemantic memory: facts, summaries, tool traces, episodic reflections, and
user-specific context retrieved for the next turn. The second isruntime memory: prefix
caches, KV tensors, offloaded blocks, and placement hints used by the serving system.
Lifelong-agent research usually treats the second layer as an opaque backend. Serving
research usually treats the first as unstructured prompt text. As a result, repeated multi-turn
agent workloads suffer from two avoidable failures: they recompute expensive prefills even
when semantically relevant reusable state exists, and they continue to expose stale compute
artifacts after a fact, summary, or plan has been corrected. We believe this memory–inference
boundary is becoming a first-order bottleneck for the next generation of agent systems.
This paper introduces PLACEMEMas a systems position on lifelong-agent memory, backed
by an executable control-plane prototype. Its core abstraction is amemory capsule, a ver-
sioned object that binds semantic content and reusable compute artifacts under a single
identity. Capsules drive replay selection, reuse eligibility, and cascading invalidation across
distributed inference nodes. More broadly, PLACEMEMis intended as a proposal for
how lifelong-agent memory should be operationalized when inference itself is distributed,
1
arXiv:2607.04089v1  [cs.AI]  5 Jul 2026

Preprint. Under review.
Approach Semantics Reuse
Cascade
invalidate
Placement
aware
Prompt or vector memory Yes No Rarely No
Runtime prefix or KV cache No Yes No Local only
PLACEMEMcapsules Yes Yes Yes Yes
Table 1: A qualitative comparison of text-centric memory, runtime caches, and PLACEMEM.
latency-sensitive, and continuously reused. The current paper does not claim a finished
replay engine; instead, it demonstrates correction-aware control-plane behavior today and
uses deeper replay integration as the agenda that follows from that result.
Contributions.We make three contributions.
• We argue for a compute-aware memory plane as a missing systems abstraction for
lifelong agents, and define memory capsules as its correction-aware core unit.
• We present an executable vLLM-first prototype that already demonstrates
correction-aware control-plane behavior through persistent capsule state,
concurrency-safe invalidation, an OpenAI-compatible sidecar, a typed serving
contract, and a live benchmark harness.
• We define a replay-and-placement policy, together with an explicit systems agenda
for deeper integration, that trades off semantic value, latency, staleness risk, and
locality across text retrieval and KV replay while leaving layer replay as future
engine work rather than a claimed implementation result.
2 Why lifelong-agent memory needs a systems layer
The central systems problem is not onlywhatan agent should remember, but alsowherethat
memory should live andhowit should be invalidated once the world changes. Consider
a customer-support agent that first stores an outdated refund policy, then later receives a
corrected policy. A text-only memory system can replace the sentence that will be retrieved
next time, but it usually does not know about derivative summaries, graph edges, prefix
caches, or remote KV artifacts that were created from the stale policy. Conversely, a serv-
ing stack may reuse runtime state efficiently, but lacks a principled view of whether the
underlying semantics remain valid.
Lifelong agents therefore need a missing middle layer with four properties:
• Unified identity.The same object should name both memory semantics and com-
pute artifacts derived from them.
• Freshness-aware reuse.Reuse should be blocked when validity windows, prove-
nance, or contradiction signals indicate elevated risk.
• Locality-aware execution.Requests should move toward reusable artifacts when
that is better than fetching them remotely or recomputing them.
• Cascading forgetting.Corrections and deletions should invalidate derived sum-
maries, indexes, and runtime artifacts rather than merely updating a text row.
Table 1 summarizes the distinction. PLACEMEMdoes not replace retrieval or runtime
caching. Instead, it makes them interoperable and auditable for lifelong agents.
3 The PLACEMEMarchitecture
Figure 1 shows the control path. The architecture is organized around a capsule catalog,
a dependency graph, and a scheduler that reasons jointly about semantic relevance and
runtime reuse.
2

Preprint. Under review.
Request → Temporal retriever → Capsule catalog → Replay policy → Placement sidecar →
vLLM backend
Hot-path writeback → Capsule update → Dependency graph → Invalidation engine →
Benchmark and tracing signals
Figure 1: PLACEMEMinserts a control plane between agent memory and distributed
inference.
3.1 Memory capsules
A memory capsule is a versioned record with required semantic fields such as tenant identity,
surface text, timestamps, and validity windows, together with optional enrichment such as
summaries, provenance, entities, facts, dependencies, and artifact locators. The crucial step
is that a capsule can also name reusable runtime artifacts such as embeddings, KV cache
segments, and optional layer-frontier checkpoints.
This design gives one identifier for meaning and compute. A retriever can therefore answer
not onlywhich memory is relevant, but alsowhich reusable state is compatible and cheap to consume
on a specific node. In the current prototype, text and KV-aware routing are fully wired end to
end, while layer-frontier replay remains an explicit contract for future engine extensions.
3.2 Replay policy and placement
For each request, PLACEMEMranks replay options across prompt-level text retrieval, KV
replay, and prospective layer replay. The policy evaluates a capsule c on target t under
replay moderwith a utility function of the form
U(c,t,r) =w 1Preuse +w 2Csaved +w 3Vsem −w 4Rstale −w 5Bremote −w 6Ltarget. (1)
Here, Preuse estimates near-term reuse, Csaved measures avoided prefill work, Vsem captures
task relevance, Rstale captures freshness risk, Bremote estimates transfer cost, and Ltarget
penalizes latency-sensitive targets. The selected decision is then turned into backend
metadata for the serving layer.
This differs from a local prefix cache in two ways. First, the decision is made in a control
plane rather than inside a single worker. Second, the decision is conditioned on semantic
validity and locality, not only on byte reuse. In other words, PLACEMEMtreats memory
reuse as a policy question, not merely a storage optimization. In the current prototype, the
scheduler exercises this policy over a configurable node topology; multi-node heterogeneous
placement evaluation is a forward agenda item.
3.3 Invalidation as a correctness primitive
For lifelong agents, forgetting is not a convenience feature; it is part of staying behaviorally
current after corrections. When a fact is corrected, or a plan is superseded, the agent should
not continue to reuse runtime state that was derived from the stale information. PLACEMEM
therefore maintains dependency edges between capsules and derived artifacts, allowing
an invalidation event to cascade through summaries, indexes, graph facts, and reusable
compute state.
This mechanism turns memory correction into a first-class operational event. In practice,
it creates an auditable answer to a question that many agent stacks leave implicit: after a
correction, which downstream artifacts are no longer safe to reuse?
4 A vLLM-first prototype
We implement PLACEMEMas a concrete control-plane prototype anchored on vLLM, in-
tended as executable evidence for the systems position above rather than a claim that all
3

Preprint. Under review.
replay paths are native to the serving engine. The implementation includes: a capsule
schema, a catalog, a dependency graph, persistent state snapshots, concurrency-safe invali-
dation, a placement RPC contract, an HTTP control plane, a vLLM-facing admission shim, a
multi-node OpenAI-compatible sidecar, and a benchmark harness with repeated-run JSON
and CSV exports.
The sidecar provides an immediately deployable integration surface with existing vLLM-
compatible endpoints and establishes a stable typed-header contract for deeper engine
integration, keeping the control-plane behavior deployable today while exposing the exact
seam where replay-aware integration can be added later.
The present implementation is deliberately control-plane heavy. It directly supports text and
KV-aware routing over live streamed backends, while exposing layer-checkpoint artifacts
and replay mode selection as a forward-compatible contract. This gives a practical eval-
uation surface for correction-aware reuse and invalidation without requiring an invasive
engine fork.
5 Pilot evaluation on lifelong-agent workloads
We evaluate on three workload families that stress distinct failure modes of lifelong memory:
customer-support history, coding-agent repository loops, and research-agent fact revision.
The goal of this section is intentionally narrow: validate correction-aware control-plane
behavior on repeated lifelong-agent traces, not claim that replay-aware serving integration
is already complete.
We compare four baselines on the same 48-turn pilot trace: prompt-only execution, text-only
retrieval that prepends a retrieved capsule summary without exposing reusable KV artifacts,
runtime reuse without semantic invalidation, and full PLACEMEM.
The text-only baseline is intentionally prompt-layer, because that is how current agent-
memory stacks typically consume retrieved text when no reusable compute artifact is
available. The pilot preserves the real control-plane, admission, and sidecar path, but
replaces the final token generator with a replay-mode-sensitive streaming mock (a fixed
SSE payload with a configurable inter-token delay, so TTFT reflects only control-plane
capsule lookup and sidecar routing overhead) to isolate cross-layer reuse and invalidation
behavior before full cluster-scale vLLM evaluation. We therefore use this pilot to test the
correction-aware control-plane thesis directly, while treating deeper replay-aware engine
integration as subsequent work.
In the current pilot, we report mean time-to-first-token, replay reuse rate, post-correction
stale-hit counts, and invalidation overhead, because those are fully executable end to
end today and directly test whether correction-aware control-plane behavior changes the
correctness–latency trade-off of reuse.
Baseline Mean TTFT∆TTFT Reuse Stale hits
Prompt-only 18.25 — 0.00 0
Text-only 18.31 +0.3% 0.00 0
Runtime-only 6.72 -63.2% 1.00 17
Full PLACEMEM7.17 -60.7% 1.00 0
Table 2: Aggregate pilot comparison over 48 turns spanning support, coding, and fact-
revision traces using the live control plane, routing sidecar, and a replay-mode-sensitive
mock backend.
Table 2 sharpens the main systems claim. Relative to prompt-only execution, both runtime-
only reuse and full PLACEMEMreduce mean time-to-first-token by about 61–63% on this
controlled backend. The crucial distinction is correction handling: disabling invalidation
preserves the latency win but yields 17 stale post-correction reuses, whereas full PLACEMEM
retains the latency benefit while eliminating stale hits entirely. Mean invalidation overhead
in the full system is 1.09 ms over three correction events.Note: TTFT here measures control-
4

Preprint. Under review.
plane and sidecar routing latency against the streaming mock; values do not reflect real prefill savings
on a production GPU.
Condition Mean TTFT (ms) KV reuse Post-corr. acc. Stale sel.
Text-summary baseline 36.08 0.00 1.00 —
Reuse w/o invalidation 20.73 1.00 0.00 1.00
Full PLACEMEM20.54 1.00 1.00 0.00
Deployment throughput (340-turn batch, 3 repeats)
FullPLACEMEM22.42 1.00 — —
Table 3: Real-backend comparison on LiquidAI/LFM2.5-230M. Top three rows: live
correction-follow probe (9 post-correction queries per condition × 3 workload families
= 27 post-correction turns per condition). Bottom row: deployment-throughput validation
across 3 repeats of the full 340-turn benchmark. Post-correction accuracy measures whether
the live model returns the corrected answer; stale selection measures whether the control
plane selects an invalidated capsule.
Table 3 integrates both the latency and behavioral stories on the real vLLM backend. The
correction-follow probe uses a controlled task: each scenario has a structured canonical
identifier injected into the active capsule summary, and accuracy measures whether the live
model’s response contains the post-correction identifier rather than the stale one, isolating
whether the control plane forwards the right summary rather than testing open-ended gen-
eration quality. The three-condition comparison shows why invalidation matters: without it
the control plane selects the stale capsule after a correction event, the model receives the
outdated summary, and post-correction accuracy drops to zero. Full PLACEMEMeliminates
stale selection while matching the TTFT of the reuse-without-invalidation condition (20.54
ms versus 20.73 ms), confirming that correction-aware control adds faithfulness at no la-
tency cost. The text-summary baseline reaches full accuracy but at 36.08 ms mean TTFT, a
75% overhead relative to full PLACEMEM. The deployment-throughput row confirms the
prototype runs end to end on a real vLLM deployment.
6 Related work
Agent-memory systems (Generative Agents, Reflexion, MemGPT) model what to remember
and retrieve, but leave runtime reuse and invalidation to the serving layer (Park et al.,
2023; Shinn et al., 2023; Packer et al., 2024). Serving systems such as vLLM optimize
KV memory, batching, and placement, but do not make semantic freshness or correction
first-class control-plane inputs (Kwon et al., 2023).
Semantic- and context-caching systems are the closest neighbors (Bang, 2023; Li et al.,
2024; Gao et al., 2025). GPTCache and SCALM match on similarity but carry no validity
windows or dependency edges; Online Context Caching optimizes prefix-block locality but
treats blocks as opaque artifacts with no correction semantics. Neither exposes a versioned
object jointly carrying meaning, validity, reusable artifacts, and edges for correction-driven
invalidation.
PLACEMEM’s cross-layer claim is that a single capsule identity coordinates retrieval, reuse
eligibility, and correction-driven invalidation.
Conclusion.Lifelong agents will not be reliable if semantic memory and runtime reuse
remain weakly synchronized. PLACEMEMcloses this gap with a versioned capsule design
backed by a working prototype, giving future researchers a direct surface for validating KV
replay gains, multi-node placement, and correction-aware invalidation at scale.
Ethics Statement.Persistent agent memory raises privacy and misuse concerns. We treat
provenance, tenant scoping, and explicit invalidation as mandatory metadata to make
retention and correction observable.
5

Preprint. Under review.
References
Fu Bang. GPTCache: An open-source semantic cache for LLM applications enabling
faster answers and cost savings. InProceedings of the 3rd Workshop for Natural Language
Processing Open Source Software (NLP-OSS 2023), pp. 212–218. Empirical Methods in
Natural Language Processing, 2023. doi: 10.18653/v1/2023.nlposs-1.24. URL http:
//dx.doi.org/10.18653/v1/2023.nlposs-1.24.
Bin Gao, Zhuomin He, Yizhen Yao, Zhanzhi Lou Lou, Zhi Zhou, and Weng-Fai Wong.
Online context caching for distributed large language models serving. InIEEE INFOCOM
2025 – IEEE Conference on Computer Communications, pp. 1–10. IEEE, May 2025. doi:
10.1109/infocom55648.2025.11044599. URL http://dx.doi.org/10.1109/infocom55648.
2025.11044599.
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu,
Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large
language model serving with PagedAttention.arXiv preprint arXiv:2309.06180, 2023.
Jiaxing Li, Chi Xu, Feng Wang, Isaac M von Riedemann, Cong Zhang, and Jiangchuan
Liu. SCALM: Towards semantic caching for automated chat services with large language
models. In2024 IEEE/ACM 32nd International Symposium on Quality of Service (IWQoS), pp.
1–10. IEEE, June 2024. doi: 10.1109/iwqos61813.2024.10682957. URL http://dx.doi.org/
10.1109/iwqos61813.2024.10682957.
Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, and
Joseph E. Gonzalez. MemGPT: Towards LLMs as operating systems.arXiv preprint
arXiv:2310.08560, 2024.
Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and
Michael S. Bernstein. Generative agents: Interactive simulacra of human behavior.arXiv
preprint arXiv:2304.03442, 2023.
Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan,
and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning.arXiv
preprint arXiv:2303.11366, 2023.
6
