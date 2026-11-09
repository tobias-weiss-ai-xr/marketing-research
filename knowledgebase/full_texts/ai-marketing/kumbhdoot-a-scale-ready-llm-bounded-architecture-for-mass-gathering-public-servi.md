---
title: 'KumbhDoot: A Scale-Ready, LLM-Bounded Architecture for Mass-Gathering Public-Service Assistants'
url: https://arxiv.org/abs/2608.07520
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Saurabh Sakalkar
- Abhishek Singh
- Ramesh Raskar
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.07520
pages: 14
chars: 39607
fetched_at: '2026-11-08T13:36:36+00:00'
kb_version: 1
---

# KumbhDoot: A Scale-Ready, LLM-Bounded Architecture for Mass-Gathering Public-Service Assistants

KumbhDoot: A Scale-Ready, LLM-Bounded Architecture
for Mass-Gathering Public-Service Assistants
Saurabh Sakalkar1 Abhishek Singh1 Ramesh Raskar2
1Project Nanda 2Massachusetts Institute of Technology
abstract
Mass religious gatherings such as the Kumbh Mela bring tens of millions of people to a
single region within a few weeks and create heavy, repetitive, multilingual demand for
information, part of which concerns personal safety. Conversational assistants are usually
built by sending every query to a large language model (LLM). In this setting that design is
expensive at scale, slow on emergency paths, liable to hallucinate facts on which physical
safety depends, and unavailable when the network fails. We describe KumbhDoot, a pilgrim
assistant for the Nashik Simhastha Kumbh Mela, in which semantic similarity over approved
content is the default mechanism and an LLM is called only when retrieval cannot produce
a correct answer. A single embedding-indexed store, which we call the semantic cache,
serves as the system’s retrieval primitive for intent routing, answer caching, offline lookup,
and agent retrieval. A hand-written three-tier orchestrator operates on this store, so that
each call to a model is the outcome of an explicit gate rather than a framework default. We
present the architecture, an analysis of its per-query cost in terms of how traffic divides
betweenretrieval-onlyandgenerativepaths,andastatementofwhichquerytypessimilarity
can and cannot serve. We argue that, for bounded, safety-critical domains with unreliable
connectivity, a similarity-first design with gated LLM use is a better fit than the conventional
LLM-centric pattern. We do not yet report a controlled evaluation; Section 7 sets out the
measurements that the claims require.
Keywords:semantic cache; retrieval-augmented generation; intent routing; offline-first
systems; public-service AI; mass gatherings
1 Introduction
An information service for a Kumbh-scale event must work under conditions that seldom coincide.
Millions of people use it at once, mostly on inexpensive phones and over congested mobile
networks. They ask questions in several languages, often mixing them within a sentence and
often by voice. Most questions are routine, such as bathing dates, the nearest ghat, or a helpline
number, but some report a lost child, a medical problem, or a dangerous crowd. For the latter, a
slow or wrong answer is a safety failure.
The usual way to build a conversational assistant today is to pass each utterance to an LLM
for both understanding and generation. We call this theLLM-defaultpattern. It is convenient
for prototyping, but at event scale it has four problems that compound one another. Repeated
questions are regenerated, and are paid for, every time they are asked. Generation adds latency
to paths that must be immediate. Free-form generation over facts such as ghat access, medical
contacts, and ritual schedules can produce plausible but false statements in precisely the cases
where they cause harm. And a cloud-hosted model is unavailable exactly when crowds saturate
the network.
Our starting point is that most of the work in such a service is retrieval rather than generation.
Representing text as vectors and ranking candidates by cosine similarity is an old problem in
1
arXiv:2608.07520v2  [cs.CY]  29 Oct 2026

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
information retrieval; the operation is inexpensive, deterministic, and easy to audit. KumbhDoot
uses it as the default path for the large majority of queries and reserves the LLM for requests
that require composition, that fall below a retrieval-confidence threshold, or that depend on live
external data.
The techniques we use (dense sentence embeddings, hybrid lexical and dense retrieval, cross-
encoder reranking, and nearest-neighbor classification over embeddings) are established. Our
contribution lies in how they are combined and constrained for a public-service setting:
(i) a design in which one retrieval primitive, cosine similarity over partitions of a single
embedding-indexed store, provides the knowledge base, intent classifier, response cache,
offline bundle, and per-agent memory (Section 4.3);
(ii) an escalation policy that orders methods by cost, calls an LLM only when an explicit gate fires,
andvalidatesthecitationsinanygeneratedansweragainsttheretrievedrecords(Section4.5),
together with a hand-written three-tier orchestrator built on the same primitive (Section 4.6);
(iii) an analysis that expresses expected per-query cost in terms of the share of traffic that must
escalate to generation (Section 5); and
(iv) an explicit account of the query classes that similarity can and cannot serve, with an evalua-
tion plan for the claims that remain unmeasured (Sections 6 and 7).
Section 2 states the deployment setting and the requirements it imposes. Section 3 reviews
related work. Section 4 describes the system, Section 5 analyzes its cost, and Section 6 discusses
the limits of similarity. Section 7 lists limitations and planned evaluation, and Section 8 concludes.
2 Setting and Requirements
KumbhDoot is designed for the Nashik Simhastha Kumbh Mela. Its users are pilgrims, who arrive
over several weeks, speak mainly Marathi, Hindi, or English, and rely on phones with limited
compute and intermittent connectivity. Its content is supplied by the event administration: official
advisories, facility locations, maps, ritual schedules, and emergency contacts. From this setting
we derive six requirements, numberedR1–R6for reference in later sections; Table 1 pairs each
with the mechanism that addresses it.
The volume of traffic is the most immediate constraint. Because the same questions recur
across millions of users, an assistant that regenerates every answer turns a largely cacheable
workload into a recurring per-query expense. Cost should instead grow with the number of
questions that are new in substance, as opposed to new in wording (R1). Within that traffic,
a small fraction of messages report a lost child or ask for an ambulance. Such messages must
receive deterministic guidance at once, without waiting on multi-step generation (R2).
A second group of requirements concerns what the system may say and under what conditions
it can say it. Statements about routes, medical facilities, and ritual schedules must be drawn from
approvedrecords;inthisdomaingroundingisasafetycontrolasmuchasaqualitycontrol(Shuster
et al., 2021), and we therefore require it of every answer (R3). Dense crowds also degrade mobile
networks, often at the moments when information is most needed, so the core of the service has
to function on the device without a connection (R4). A design whose every answer depends on a
cloud-hosted model cannot satisfy this requirement.
Thelasttworequirementsconcerndata.Apilgrim’slocation,healthstatus,familycomposition,
and stage of journey are sensitive, and routing every utterance to a remote model would expose
2

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
Table 1.Requirements of the deployment setting and the mechanisms that address them.
Requirement Principal mechanism Section
R1Cost proportional to novelty Paraphrase-aware response cache; answers
formatted from records without an LLM
4.3, 4.5
R2Immediate emergency handling Keyword-triggered, rule-based fast path
ahead of intent routing
4.4
R3Grounding in approved content InfoBins with source and validity metadata;
coded formatters; citation validation
4.2, 4.5
R4Offline operation On-device SQLite bundle with FTS5 and
pre-computed embeddings
4.7
R5Data minimization Local-first storage, coarse and consented
location, bucketed attributes
7
R6Aggregate operational insight Observability across LLM and non-LLM
paths; aggregate dashboards
4.1
precisely the information that ought to remain on the device or be coarsened before it leaves
(R5). The event administration, for its part, needs aggregate signals, such as where crowds are
concentrating and which concerns are emerging, and has no need for individual conversations or
per-user tracking (R6).
3 Related Work
Lexical and dense retrieval.Lexical scoring rests on the vector space model (Salton et al., 1975)
and on term weighting (Spärck Jones, 1972); latent semantic analysis (Deerwester et al., 1990)
introduced low-dimensional dense representations; Manning et al. (2008) give a standard treat-
ment. Word embeddings (Mikolov et al., 2013) and, later, sentence encoders trained with siamese
or contrastive objectives (Reimers and Gurevych, 2019; Gao et al., 2021) made it practical to
compare whole queries by cosine similarity, which is the granularity at which KumbhDoot oper-
ates. Cross-encoders improve precision by rescoring a candidate set produced by a cheaper first
stage (Nogueira and Cho, 2019; Cheng et al., 2026), and reciprocal rank fusion offers a simple,
robust way to combine lexical and dense rankings (Cormack et al., 2009). Throughout this line of
work the representations have improved while the comparison operation has remained essentially
the same.
Retrieval-augmented generation.Retrieval-augmented generation conditions a language model
on retrieved passages to improve factuality on knowledge-intensive tasks (Lewis et al., 2020;
Guu et al., 2020), typically with a dense retriever (Karpukhin et al., 2020), and retrieval has
been shown to reduce hallucination in dialogue (Shuster et al., 2021). In these systems a model
generates every answer and retrieval supplies its context. KumbhDoot reverses the default: most
answers are assembled from retrieved records without a model, and generation is the exception.
LLM agents.Agent frameworks interleave model reasoning with tool calls (Yao et al., 2022).
They are flexible, but control flow, including intent classification and task decomposition, is
usually delegated to the model, so that each step incurs a call and its decision is difficult to audit.
KumbhDoot keeps orchestration in code and reaches a model only through explicit gates.
Caching,offlineoperation,andon-devicemodels.Practitionersystemscachepromptsandresponses
to avoid repeated model calls, keep application data in offline-first mobile stores that synchronize
3

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
on reconnection, and trace LLM calls for latency and cost. KumbhDoot applies each of these
ideas more broadly: its cache matches paraphrases rather than exact strings, its offline tier
performs intent routing and retrieval as well as storage, and its observability covers non-LLM
paths. Work on distillation (Hinton et al., 2015), compression (Han et al., 2015), and on-device
learning (McMahan et al., 2016) has made small models practical on handsets; KumbhDoot
uses such components where they are available but does not assume them. Large language
models (Brown et al., 2020) provide the generative capability that KumbhDoot uses for the
residual class of queries described in Section 6.
What distinguishes KumbhDoot from these lines of work is scope rather than any single technique.
It is an event-specific assistant with bounded knowledge, strict fallbacks, and an offline tier, and
that scope is what makes a similarity-first design viable.
4 System Design
4.1 Overview
The runtime is a stack of layers, each of which answers what it can before passing the query
upward (Figure 1). From the bottom, a curated content layer holds official advisories, facility
details, maps, schedules, and emergency contacts. An InfoBin layer turns this content into
versioned, searchable records (Section 4.2), and a compact partition of those records is shipped
to the device as a local semantic cache (Section 4.7). An intent router combines rules, light
normalization, and nearest-neighbor matching with confidence scores (Section 4.4). Bounded
domain agents serve food, travel, safety, accommodation, health, emergency, ritual, profile, and
crowd queries (Section 4.6). A response composer formats answers from approved records and
calls a small model or an LLM only when the escalation policy requires it (Section 4.5). An
observability layer spans the stack and records latency, cost, cache hits, model use, sources, safety
flags, and fallback paths for every request, including those that never reach a model.
4.2 InfoBins
Informational apps usually present curated content as static cards. An agent needs the same
content in a form that can be matched against natural-language queries, checked for currency,
and withdrawn when it becomes wrong. We call such a record anInfoBinand write it as
𝑏=(𝑐, 𝜇,v, 𝜎),(1)
where 𝑐 is the approved content;𝜇 is metadata comprising domain, language, source authority,
zone, validity interval, and time of last update;v∈ℝ 𝑑 is a unit-normalized embedding of the
content; and𝜎 holds safety attributes, namely the source label, freshness status, revocation status,
and escalation rule. The first question the runtime asks of any query is whether an approved
InfoBin already answers it; escalation follows only when none does.
4.3 The semantic cache
Let 𝜙 denote a sentence encoder whose outputs are unit-normalized, so that cosine similarity
reduces to an inner product. The semantic cache is a collection of partitionsS={𝑃 1,...,𝑃 𝐾},
where each partition𝑃𝑘 ={( v𝑗,𝜋 𝑗)} pairs key embeddings with payloads. All retrieval in the
system is an instance of one operation,
Retrieve(𝑞,𝑃 𝑘)=top-k (v,𝜋)∈𝑃 𝑘⟨𝜙(𝑞),v⟩,(2)
4

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
Curated content layer
Official advisories, facilities, maps, schedules, emergency contacts
InfoBin layer
Versioned, searchable knowledge units: metadata, semantics, safety rules
Local semantic cache (on device)
Compact InfoBin bundle for fast lookup and offline behavior
Intent router
Rules, lightweight NLP , cosine matching, confidence scoring, escalation
Bounded domain agents
Food, travel, safety, accommodation, health, emergency, ritual, profile, crowd
Response composer
Formats from approved content; small model or LLM only when required
Observability layer
latency·cost·cache hits·model use·sources·fallbacks
escalate only if needed
zero generative LLM tokens deterministic; no LLM by default may invoke a model
Figure 1.Layered runtime. A query is answered by the lowest layer able to answer it reliably and moves
upward only when that layer cannot. Observability spans all layers and covers both LLM and non-LLM
paths.
Table 2.Five functions expressed as retrieval against different partitions of the semantic cache.
Function Keys Payload
Knowledge base Embeddings of InfoBin content InfoBin records
Intent classifier Embeddings of labeled exemplar queries Intent and domain labels
Response cache Embeddings of previously answered
queries
Approved answers
Offline bundle Device-resident subset of InfoBin
embeddings, with an FTS5 index
InfoBin records
Per-agent memory Embeddings of records in an agent’s
domain partition
Records scoped to that agent
optionally fused with a lexical ranking and reranked (Section 4.5). Five functions that are usually
built as separate components differ only in the partition queried (Table 2 and Figure 2).
The semantic cache is a logical layer rather than a single database, and it is realized differently
onthe server andon thedevice(Table3). On theserver, domainpartitionsare heldin memory and
in cache-backed stores, including a Redis store for paraphrase-aware query-to-answer caching,
with higher-dimensional embeddings that are updated as content changes. On the device, a
curated partition is shipped as a SQLite bundle of approximately 700KB that combines a full-text
(FTS5) index with lower-dimensional embeddings stored as binary blobs, so that hybrid retrieval
requires no network call. Both tiers expose the abstraction of Equation (2). The tiers do not share
a physical store, and live synchronization from the server indexes to the device bundle is not yet
implemented: the bundle is built at release time.
5

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
Conventional design: five separate systems
Knowledge base (structured records)
Intent classifier (ML model or LLM)
Response cache (key–value)
Offline data bundle (static files)
Per-agent memory and state
Semantic cache
embedding-indexed records + metadata
record embeddings intent exemplars
cached Q→A pairs POIs and facilities
all queried by cosine similarity
collapse into
cosine_scores(query_vec, partition)
one operation; the partition determines the function
Figure 2.One retrieval primitive in place of five components. Each function is cosine similarity against a
different partition of one embedding-indexed store; the variety lies in the partition, not the algorithm.
Table 3.Realization of the semantic cache on the two tiers.
Server Device
Storage In-memory partitions; Redis for
query-to-answer pairs
SQLite bundle (≈700KB)
Embeddings Higher-dimensional; updated with live
content
Lower-dimensional; pre-computed,
stored as blobs
Lexical index — SQLite FTS5
Retrieval Dense retrieval, fusion, reranking FTS5 and dense scores combined by
rank fusion
Query embedding Server-side encoder Quantized on-device encoder if present;
otherwise word-overlap matching
against pre-computed query embeddings
Content updates Continuous At build time (live synchronization not
yet implemented)
4.4 Intent routing
Many agent frameworks classify intent by prompting a model (e.g., Yao et al., 2022), which adds
a call, latency, and an opaque decision to every request. KumbhDoot treats intent classification as
nearest-neighbor search. LetE={( e𝑖,𝑦 𝑖)}𝑛 𝑖=1 be a set of𝑛≈ 520exemplar queries labeled with
one of 26 intents, written in English, Hindi, and Marathi and embedded once at start-up. For a
query𝑞, the router computes
ˆ𝚤=arg max
𝑖
⟨𝜙(𝑞),e 𝑖⟩,ˆ𝑦=𝑦 ˆ𝚤, 𝑠=⟨𝜙(𝑞),e ˆ𝚤⟩,(3)
which for all exemplars is a single matrix–vector product. The predicted intentˆ𝑦determines
the domain, and the score𝑠 is retained as an auditable confidence. The step uses no generative
model, although the encoder still runs.
Two components surround this step. Before it, the router normalizes transliteration and
common speech-recognition errors and checks the query against a list of emergency phrases; a
match routes the query to a rule-based fast path. After it, a separate heuristic estimates query
complexity from the number of domain keywords, the presence of conjunctions in any of the
6

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
Algorithm 1Escalation policy for a single query. Thresholds𝜏c and 𝜏r govern the cache and
retrieval gates.
Input:query𝑞; semantic cacheS; exemplarsE
Output:an answer with its sources and freshness status
1z←𝜙(𝑞)
2(𝑎,𝑠 c)←Retrieve 1(z,𝑃 cache)
3if𝑠 c≥𝜏 c then returnFormat(𝑎)⊲no LLM
4𝑞 ′←Normalize(𝑞)⊲transliteration, ASR errors
5ifEmergencyMatch(𝑞 ′)then returnEmergencyResponse(𝑞 ′)
6(ˆ𝑦,𝑠)←RouteIntent(𝑞 ′,E)
7𝑅←HybridRetrieve(𝑞 ′,𝑃 dom(ˆ𝑦))⊲lexical + dense, fused, reranked
8if¬Complex(𝑞 ′)∧conf(𝑅)≥𝜏 r∧¬NeedsLive(𝑞 ′)then
9returnFormatFromRecords(𝑅)⊲no LLM
10𝐴←BoundedLLM(𝑞 ′,𝑅)⊲generation restricted to𝑅
11returnValidateCitations(𝐴,𝑅)⊲drop citations not in𝑅
three languages, and query length. Complexity, not intent, decides whether the orchestrator of
Section 4.6 is engaged.
4.5 Escalation policy
Algorithm 1 and Figure 3 give the order in which the runtime tries its methods. A query is first
matched against the response cache; a confident hit is returned through a coded formatter. On a
miss, the router assigns a domain, and hybrid retrieval over that domain’s partition produces
a candidate set. When retrieval is confident and the request is single-domain, the records are
formatted into a cited answer without a model. An LLM is called only when an escalation gate
fires: the request needs multi-part synthesis, retrieval confidence falls below threshold, or the
answer depends on live or external data. Generation is then restricted to the retrieved records,
and a validation step removes any citation that does not correspond to a record the retriever
returned, so that identifiers invented by the model do not reach the user.
4.6 Orchestration
Requests that span domains are handled by three tiers of agents that share the retrieval primitive
(Figure 4). Anorchestratordecomposes the request into sub-needs with dependency edges and
schedules them in waves: independent sub-needs run concurrently, and dependent ones wait
for, and receive, the results of their prerequisites.Domain agents, one each for health, travel,
commerce, crowd, identity, governance, curated Kumbh content, and other domains, retrieve
from their own partitions.Record-level sub-agentsturn retrieved items into structured answers,
annotating each with whether it is actionable, its card type, whether it concerns an emergency,
and whether it matches a name in the query.
The orchestration logic is written by hand for this domain rather than delegated to a general-
purpose agent framework. Because every agent consults the semantic cache before anything
else, a model is reached only under the conditions of Algorithm 1, and the path by which each
answer was produced can be read from the trace. A further consequence is that adding a domain
is mostly a matter of data: curated records are loaded into a new partition and the domain is
7

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
User query
1·Q&A cache lookup (cosine)
paraphrase-aware, multilingual
2·Intent routing (cosine𝑘-NN)
≈520 exemplars·26 intents·emergency fast path
3·Domain retrieval (hybrid)
FTS5 + cosine + rank fusion + rerank
Confidence
high or medium?
format_from_records
grounded, cited·0 LLM calls
Escalation gate
complex multi-part synthesis·low-confidence retrieval
·live or external data
LLM (bounded fallback)
constrained to retrieved records
Grounding validation: drop unsupported citations
Grounded answer
with source + status
miss
yes
no / low
hit·0 LLM calls
cache and cheap paths return here
Figure 3.Escalation ladder. Methods are tried in order of cost. Paths drawn in the dark accent return
without a generative model; the warm-colored path is the only one that calls an LLM.
registered. New orchestration code is needed only when the shared schema or routing rules do
not already accommodate the domain.
4.7 Offline operation
The device tier is designed to remain useful without a connection. Emergency contacts, key
facilities, the user’s saved itinerary, basic maps, frequently asked questions, phrasebooks, and
previously synchronized InfoBins are stored locally. When the network is unavailable, voice input
falls back to text, agentic answers fall back to approved static guidance, and live data is shown
with the time it was last updated. Non-critical requests are queued until the connection returns,
and emergency updates are synchronized first. Every answer is labeled asavailable offline,last
updated, orpending refresh, so that users can judge how current it is. Retrieval on the device fuses
FTS5 results with dense scores by rank fusion, as summarized in Table 3.
5 Cost Analysis
In a pipeline where every stage is an LLM call, cost accrues at intent classification, complex-
ity assessment, decomposition, per-domain reasoning, and synthesis. A conventional retrieval-
augmented pipeline removes the model from retrieval but still generates every answer. In Kumbh-
8

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
TIER 1
TIER 2
TIER 3
Orchestrator
decompose into sub-needs·dependency-wave scheduling
Health agent
InfoCard
sub-agent
Travel agent
InfoCard
sub-agent
Commerce agent
InfoCard
sub-agent
Crowd agent
InfoCard
sub-agent
Shared semantic cache (embedding-indexed, partitioned by domain)
health partition travel partition commerce partition crowd partition more partitions . . .
Figure 4.Three-tier orchestration. All tiers retrieve through the same primitive, each over its own partition;
only four of the domain agents are shown. Sub-agents annotate retrieved items with the fields_actionable,
_card_type,_is_emergency, and_name_match.
Table 4.Where a generative model is invoked in three pipeline designs.
Stage LLM-default Conventional RAG KumbhDoot
Intent classification LLM — Nearest-neighbor over
exemplars
Complexity assessment LLM — Keyword and length
heuristic
Decomposition LLM — Hand-written
orchestrator
Retrieval LLM-directed tools Dense retriever Hybrid retrieval with
reranking
Answer synthesis LLM LLM Coded formatter; LLM
only when a gate fires
Doot each stage has a deterministic implementation, and the model is a fallback for synthesis
(Table 4).
The deterministic stages are inexpensive. Routing against a fixed exemplar set is one matrix–
vector product; a response-cache lookup is a nearest-neighbor query; hybrid retrieval combines
vector arithmetic, a lexical index, and a small local reranker. None of these consumes generative
tokens. The query embedding does consume compute, so the accurate statement is that common
paths use no generative tokens, not that they are free. On the device, where content vectors are
pre-computed, even the content-side embedding is avoided.
Let 𝑝𝐴, 𝑝𝐵, and𝑝𝐶 be the fractions of traffic answered in Bands A, B, and C (Section 6), with
𝑝𝐴+𝑝 𝐵+𝑝 𝐶 = 1, and let𝑐𝐴, 𝑐𝐵, and𝑐𝐶 be the corresponding per-query costs excluding the query
embedding, whose cost𝑐emb is paid on every server-side path. The expected cost of a query is
𝔼[𝐶]=𝑐 emb+𝑝 𝐴𝑐𝐴+𝑝 𝐵𝑐𝐵+𝑝 𝐶𝑐𝐶, 𝑐 𝐴≤𝑐 𝐵≪𝑐 𝐶,(4)
9

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
where the ordering holds because Bands A and B use no generative model. In an LLM-default
design every query costs on the order of𝑐𝐶. The advantage of the similarity-first design therefore
depends chiefly on𝑝𝐶, the share of traffic that must escalate.
That share should fall as the response cache fills. The first occurrence of a question costs one
embedding and one retrieval; later paraphrases, in any supported language, are answered from
the cache whenever they fall within its similarity threshold. If pilgrimage queries are concentrated
on a relatively small set of recurring needs, as we expect, the fraction answerable without a
model grows with use, and the marginal cost of a common query approaches that of a similarity
computation. Generation is then paidfor onlyon the tail of novel, multi-step, or externally sourced
requests. This is an argument about the structure of the cost, not a measurement; Section 7
describes how𝑝𝐶 and the band costs will be estimated.
6 What Similarity Can and Cannot Do
In a bounded, curated domain, similarity search with coded formatting suffices for a large class
of needs: intent classification over a fixed label set, retrieval that tolerates paraphrase, FAQ-style
answers, and structured factual responses drawn from approved records. For these needs a
generative model adds latency, cost, and risk of error without adding correctness.
Several needs lie outside this class. A query about something absent from the corpus produces
low-confidence retrieval and must be deflected or escalated; retrieval cannot return information
thatthecorpusdoesnotcontain.Theclosestrecordisnotnecessarilytheintendedone,particularly
near intent boundaries. Planning under constraints that span domains requires orchestration
and, often, generated prose. Coded formatters produce accurate structured output but not
fluent narrative. Transactions such as booking or identity verification require tool-using agents.
Multilingual encoders reduce, but do not remove, degradation from code-mixing, dialect, and
speech-recognition errors.
These observations divide the workload into three bands (Figure 5). In Band A, a query is
answered from the response cache or by direct retrieval, as when a user asks where a ghat is
or when the bathing dates fall. In Band B, coded orchestration combines several records into
a structured answer, as when a user asks for hospitals with emergency care near a locality. In
Band C, the system escalates to LLM-backed synthesis, as when an elderly traveler asks for a
personalized plan for the day of arrival. The aim is to answer each query in the cheapest band
that can answer it correctly and to make every escalation to Band C the result of an explicit
decision.
The same reasoning bounds what can be claimed about hallucination. Because most answers
are assembled by coded formatters from curated records, the opportunities for unconstrained
generation are fewer than in a design that calls a model at every step. They are not zero: Band C
still calls a model, and retrieval can surface a record that is itself wrong. Citation validation
removes one class of fabrication but does not guarantee correctness.
7 Limitations and Planned Evaluation
This paper describes an architecture and argues for it analytically; it does not report a controlled
evaluation. Table 5 summarizes the measurements the claims require, and the paragraphs below
discuss the limitations of the current design.
10

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
lower cost, deterministic higher cost, generative
Band A
Similarity alone
Q→ A cache +
direct retrieval
0 LLM calls
Example
“Where is Ramkund ghat?”
“What are the snan dates?”
Band B
Similarity + coded
orchestration
multi-record retrieval
+ structured format
0 LLM calls
Example
“List hospitals near Panchavati
with emergency care”
Band C
LLM-backed synthesis
and dialogue
multi-step planning,
open-ended generation
1 or more LLM calls
Example
“I’m 72, diabetic, arriving
Friday; plan everything for me”
Outside the reach of Bands A and B: content absent from the corpus, multi-step reasoning, novel synthesis, and transactions that require tools
Figure 5.Three workload bands. Each query should be answered in the cheapest band that can answer it
correctly. Hallucination is reduced rather than eliminated, because Band C still calls a model.
Table 5.Claims that remain to be measured and the planned protocol for each.
Claim Planned measurement
Most traffic needs no
generative model
Share of queries answered in Bands A and B on a representative query
distribution, with full per-step tracing
Cost and latency by band Tokens, cost, and latency per step on a tiered benchmark of simple,
multi-record, and multi-domain queries, each paired with paraphrases
Advantage over alternatives Comparison against both an LLM-at-every-step pipeline and a
conventional RAG pipeline that uses a model only for synthesis
Multilingual routing
accuracy
Accuracy and threshold calibration on a labeled test set in English, Hindi,
Marathi, and code-mixed input, including speech-recognition noise
Offline usefulness Minimum useful bundle size and on-device hit rate, measured by
replaying representative traffic
The choice of baselines matters for the comparison in the third row of Table 5. A pipeline
that forces a model through every stage represents a worst case, and an advantage over it alone
would overstate the contribution. The comparison must therefore also include a conventional
retrieval-augmented baseline, which generates every answer but uses no model for routing or
decomposition.
Theemergencypathisthemostseriouslimitationofthecurrentdesign.Keywordmatchingcan
miss indirect phrasing, speech-recognition errors, and code-mixed expressions, and it can raise
false alarms, so it cannot serve as the principal safeguard. A production system would need, at a
minimum, a permanent one-tap emergency control, emergency numbers and instructions stored
on the device, explicit confirmation of the location and nature of the emergency, direct telephone
and SMS paths, escalation to a human operator, and a safe default whenever classification
confidence is low. For official one-to-many alerts, cell broadcast is preferable to any application-
level channel, since it is designed to remain effective under network congestion (3rd Generation
Partnership Project, 2024).
11

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
Several properties on which the design relies have yet to be measured. The accuracy of nearest-
neighbor routing on English, Hindi, Marathi, and code-mixed input is unknown; encoder quality
degrades with dialect and speech-recognition noise, and the thresholds that separate answering,
clarifying, deflecting, and escalating must be tuned and reported on a labeled multilingual set. It
is likewise an open question how small an InfoBin bundle can be while still giving useful offline
behavior, and what hit rate it then achieves. The cost argument of Section 5 further assumes a
query distribution concentrated enough for the response cache to warm quickly, an assumption
that only real traffic can test.
Content currency poses a related problem. The device bundle is built at release time (Sec-
tion 4.3), and until signed incremental updates and revocation of stale or corrected guidance are
implemented, the offline tier cannot be relied on for advisories that change quickly. On the server,
guidance can become stale during road closures, shifts in crowd conditions, or emergencies. The
design provides last-updated labels, tiered refresh intervals, and revocation lists, but the opera-
tional practice of keeping safety-critical InfoBins current, and the audit standards appropriate to
a public-sector deployment, remain to be established in the field.
Finally, the privacy posture described in Section 2 (bucketed rather than exact attributes, local-
first storage, coarse and consented location, aggregate dashboards by default, and audit logs) is
at present a design commitment. Whether it holds in deployment, and how much personalization
is worth its privacy cost, are questions for the field study.
8 Conclusion
Public information services at mass gatherings must serve very large, multilingual populations
over unreliable networks, under tight cost constraints, with some questions bearing directly on
physical safety. We have described KumbhDoot, an assistant for the Nashik Simhastha Kumbh
Mela that treats retrieval as the default and generation as a gated exception. A single retrieval
primitive,cosinesimilarityoverpartitionsofanembedding-indexedstore,providestheknowledge
base, intent classifier, response cache, offline bundle, and per-agent memory, and a hand-written
orchestrator built on it calls a model only when an explicit condition is met.
Our cost analysis shows that the advantage of this design over an LLM-default one is governed
by the share of traffic that must escalate to generation, a quantity we have argued is small for this
domain but have not yet measured. Measuring it, together with multilingual routing accuracy,
offline coverage, and the behavior of the emergency path, is the subject of our next phase of
work. We expect the general point to hold beyond this event: in bounded, safety-critical domains,
generative models are most useful when reserved for the queries that retrieval cannot answer.
References
3rdGenerationPartnershipProject. Technicalrealizationofcellbroadcastservice(CBS). Technical
Specification TS 23.041, 3GPP, 2024. Release 18.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D. Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models
are few-shot learners. InAdvances in Neural Information Processing Systems, volume 33, pages
1877–1901, 2020.
12

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
Zhiyuan Cheng, Longying Lai, Yue Liu, Kai Cheng, and Xiaoxi Qi. Enhancing financial report
question-answering: A retrieval-augmented generation system with reranking analysis. arXiv
preprint arXiv:2603.16877, 2026.
Gordon V. Cormack, Charles L. A. Clarke, and Stefan Büttcher. Reciprocal rank fusion outperforms
Condorcet and individual rank learning methods. InProceedings of the 32nd International ACM
SIGIR Conference on Research and Development in Information Retrieval, pages 758–759, 2009.
doi: 10.1145/1571941.1572114.
Scott Deerwester, Susan T. Dumais, George W. Furnas, Thomas K. Landauer, and Richard Harsh-
man. Indexing by latent semantic analysis.Journal of the American Society for Informa-
tion Science, 41(6):391–407, 1990. doi: 10.1002/(SICI)1097-4571(199009)41:6<391::
AID-ASI1>3.0.CO;2-9.
Tianyu Gao, Xingcheng Yao, and Danqi Chen. SimCSE: Simple contrastive learning of sentence
embeddings. InProceedings of the 2021 Conference on Empirical Methods in Natural Language
Processing, pages 6894–6910, 2021. doi: 10.18653/v1/2021.emnlp-main.552.
Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, and Mingwei Chang. Retrieval augmented
language model pre-training. InProceedings of the 37th International Conference on Machine
Learning, volume 119 ofProceedings of Machine Learning Research, pages 3929–3938. PMLR,
2020.
SongHan,HuiziMao,andWilliamJ.Dally. Deepcompression:Compressingdeepneuralnetworks
with pruning, trained quantization and Huffman coding. arXiv preprint arXiv:1510.00149,
2015.
Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the knowledge in a neural network.
arXiv preprint arXiv:1503.02531, 2015.
Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi
Chen, and Wen-tau Yih. Dense passage retrieval for open-domain question answering. InPro-
ceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP),
pages 6769–6781, 2020. doi: 10.18653/v1/2020.emnlp-main.550.
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal,
Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, and Douwe
Kiela. Retrieval-augmented generation for knowledge-intensive NLP tasks. InAdvances in
Neural Information Processing Systems, volume 33, pages 9459–9474, 2020.
Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze.Introduction to Information
Retrieval. Cambridge University Press, Cambridge, UK, 2008. doi: 10.1017/CBO97805118090
71.
H. Brendan McMahan, Eider Moore, Daniel Ramage, Seth Hampson, and Blaise Agüera y Arcas.
Communication-efficient learning of deep networks from decentralized data. arXiv preprint
arXiv:1602.05629, 2016.
Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean. Efficient estimation of word represen-
tations in vector space. arXiv preprint arXiv:1301.3781, 2013.
Rodrigo Nogueira and Kyunghyun Cho. Passage re-ranking with BERT. arXiv preprint
arXiv:1901.04085, 2019.
Nils Reimers and Iryna Gurevych. Sentence-BERT: Sentence embeddings using Siamese BERT-
networks. InProceedings of the 2019 Conference on Empirical Methods in Natural Language
13

KumbhDoot: an llm-bounded architecture sakalkar, singh, and raskar
Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-
IJCNLP), pages 3982–3992, 2019. doi: 10.18653/v1/D19-1410.
Gerard Salton, Anita Wong, and Chung-Shu Yang. A vector space model for automatic indexing.
Communications of the ACM, 18(11):613–620, 1975. doi: 10.1145/361219.361220.
Kurt Shuster, Spencer Poff, Moya Chen, Douwe Kiela, and Jason Weston. Retrieval augmentation
reduceshallucinationinconversation. InFindingsoftheAssociationforComputationalLinguistics:
EMNLP 2021, pages 3784–3803, 2021. doi: 10.18653/v1/2021.findings-emnlp.320.
Karen Spärck Jones. A statistical interpretation of term specificity and its application in retrieval.
Journal of Documentation, 28(1):11–21, 1972. doi: 10.1108/eb026526.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.
ReAct: Synergizing reasoning and acting in language models. arXiv preprint arXiv:2210.03629,
2022.
14
