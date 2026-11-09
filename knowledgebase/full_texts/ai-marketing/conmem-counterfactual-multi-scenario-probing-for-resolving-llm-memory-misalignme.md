---
title: 'ConMem: Counterfactual Multi-Scenario Probing for Resolving LLM Memory Misalignment'
url: https://arxiv.org/abs/2610.33432
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Shuning Zhang
- Tenghao Ji
- Jingruo Chen
- Eryue Xu
- Bohao Chu
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.33432
pages: 17
chars: 64727
fetched_at: '2026-11-08T13:35:40+00:00'
kb_version: 1
---

# ConMem: Counterfactual Multi-Scenario Probing for Resolving LLM Memory Misalignment

ConMem: Counterfactual Multi-Scenario Probing for Resolving LLM
Memory Misalignment
Shuning Zhang1,*, Tenghao Ji2,*, Jingruo Chen3,
Eryue Xu4, Bohao Chu5, Xin Yi1
1Tsinghua University
2Independent Researcher
3Cornell University
4University of Illinois Urbana-Champaign
5University of Duisburg-Essen
Abstract
Long-term memory is critical for autonomous
Large Language Model (LLM) agents execut-
ing multi-session, long-horizon tasks. How-
ever, existing memories often inappropriately
store, retain, or retrieve over-generalized, mis-
attributed, or privacy-sensitive information, a
problem we term memory misalignment. To
study this problem, we constructMemAlign, a
benchmark comprising 1,079 curated memory
cases grounded in synthetic, validated multi-
session conversational contexts covering di-
verse misalignment taxonomies. We then pro-
pose ConMem, an algorithm that reframes re-
tention decisions as prospective counterfac-
tual causal inference.ConMemsynthesizes
counterfactual interaction scenarios to prospec-
tively audit downstream intervention effects
across three aspects: relevant task execution,
irrelevant invariance checks, and risk-sensitive
boundary shifts. Experiments show that Con-
Mem outperforms other methods, achieving
75.16% accuracy, 64.15% balanced accuracy,
and a Macro-F1 of 65.31%, effectively miti-
gating over-retention biases without sacrificing
personalization utility.
1 Introduction
Long-term memory is important for autonomous
agentic systems, particularly as Large Language
Model (LLM) agents are increasingly deployed
for complex, multi-session, and long-horizon
tasks (Park et al., 2023; Packer et al., 2023). To
enable agents with persistent capabilities across
extended interactions, a variety of frameworks
emerged, ranging from hierarchical key-value
stores to dynamic context paging systems (Wang
et al., 2023; Modarressi et al., 2023; Zhong et al.,
2024a). Concurrently, extensive benchmarking
efforts scrutinized memory hallucinations (Dziri
et al., 2022), factual retrieval precision (Liu et al.,
2023), and long-context recall degradation (Liu
et al., 2024; Maharana et al., 2024). Despite these
My coworker
doesn’t eat meat. Candidate Memory
ConMem: Prospective Counterfactual Evaluation
vegetarian.
Got it. User is
Before storing: how would this memory change future responses?
Relevant Irrelevant Risk-sensitives
Any dinner ideas
for me?
Vegetarian
restaurants.
Here’s a revised
version.
Make this email
more polite.
Recommend a
steakhouse?
I’d avoid steak.
Harmful Neutral Harmful
Store? Do-Not-Store?
Figure 1: An illustration of memory misalignment.
advancements, agents deployed in open-ended life-
long interactions often exhibit memory behavior
that remains frustratingly misaligned with user ex-
pectations (Zhang et al., 2025b).
As seen in Figure 1, imagine a user casually
conversing with a personal assistant about plan-
ning a farewell dinner for a vegetarian colleague:
“can you suggest a fine-dining spot? My co-worker
doesn’t eat meat. ”A naive memory pipeline, eager
to extract personal attributes, commits to long-term
storage:“user is strictly vegetarian. ”In a sub-
sequent session three weeks later, when the user
requests recommendations of a steakhouse for their
own birthday, the agent filters out all beef dishes,
warns the user about dietary violations, and refuses
to provide relevant suggestions. In this scenario,
the stored information is a misattributed inference.
When later recalled, such inappropriate memories
pollute the agent’s future decision boundaries.
We frame this challenge as thememory mis-
alignmentproblem. Extending the taxonomy es-
tablished by Chen et al. (2026), memory misalign-
1
arXiv:2610.33432v1  [cs.AI]  24 Oct 2026

ment spans multiple failure classes across two op-
erational stages:memory generation(e.g., attribu-
tion confusion, over-inference, and granularity mis-
match) andmemory usage(e.g., context misappli-
cation, stale memory reliance, and privacy overuse).
Crucially, existing memory techniques evaluate
candidate memories in isolation, relying primar-
ily on extraction confidence, semantic relevance, or
surface-level factual heuristics (Salama et al., 2025;
Tan et al., 2025). Therefore, they fail to anticipate
how a candidate memory will affect downstream
agent behavior across future interactions, leading
either to over-retention or over-pruning.
To benchmark memory admission and usage
within multi-turn interaction, we constructMemA-
lign. Building upon Chen et al. (2026), we cu-
rate 1,079 candidate memories and augment each
record with a multi-session conversational history
generated via Qwen3.8-Max (Qwen Team, 2026).
All conversational contexts pass structural checks,
LLM-based semantic audits, and human review,
which improve fidelity to the source annotations
and reduce label-revealing shortcuts. These dia-
logues preserve the epistemic strength, entity attri-
bution, temporal evolution, and corrective feedback
of the source interaction while prohibiting the lexi-
calization of gold storage decisions.
To mitigate memory misalignment at the admis-
sion stage, we proposeConMem, a memory admis-
sion framework based on counterfactual probing of
future interactions. Instead of treating admission as
a static text-classification task, ConMem decides
whether to store a candidate memory by simulating
future interactions and comparing responses gener-
ated with and without access to the memory. These
comparisons are aggregated into the Counterfac-
tual Memory Treatment Effect (CMTE), a score
that reflects the net downstream effect of memory
access. Given a candidate memory and its historical
context, ConMem synthesizes three future probes:
(i) a relevant probe that tests whether the memory
provides useful personalization, (ii) an irrelevant
probe that checks whether the memory induces
unnecessary personalization where it should not
matter, and (iii) a risk-sensitive probe that intro-
duces entity, temporal, or scope shifts to expose
inappropriate memory carry-over. A blind quality
judge and a separate attribution auditor then deter-
mine whether each response change is beneficial
and whether it is attributable to the memory.
Extensive evaluations on MemAlign show that
ConMem outperforms state-of-the-art memory
mechanisms, including A-MAC (Zhang et al.,
2026) and SAGE (Peng et al., 2026). Specifi-
cally, ConMem achieves an accuracy of 75.16%,
a balanced accuracy of 64.15%, and a Macro-F1
of 65.31%, surpassing A-MAC by 15.40 percent-
age points in Macro-F1 while effectively breaking
the extreme retention biases of existing baselines.
Furthermore, granular error analyses provide em-
pirical insights into the delicate trade-off between
memory utility and safety, showing robust general-
ization across parameter spaces while highlighting
nuanced contextual scope boundaries as important
directions for future exploration.
Collectively, this paper contributes: (i) we for-
malize the agent memory misalignment problem
and introduce MemAlign, a benchmark of 1,079
candidate memories grounded in dual-validated
multi-session dialogues; (ii) we propose ConMem,
reframing memory admission as prospective coun-
terfactual evaluation across complementary future
scenarios; (iii) we show that CONMEMsubstan-
tially outperforms existing baselines by achieving
65.31% Macro-F1, while uncovering behavioral
trade-offs across distinct misalignment categories.
2 Related Work
2.1 Memory of Agentic System
Recent architectural advancements have estab-
lished structured and hierarchical memory frame-
works as core components for enabling dynamic
context management in LLM agents. Park et al.
(2023) pioneered agentic memory design by sim-
ulating human-like behavior through social con-
text interactions. To go beyond static prompts,
MemGPT (Packer et al., 2023) introduces an oper-
ating system-inspired virtual memory management
system that enables agents to dynamically page
and edit memory across storage tiers via function
calling. Complementary architectures like LONG-
MEM (Wang et al., 2023) leverage a decoupled
trainable side network to retrieve long-term tex-
tual contexts, while RET-LLM (Modarressi et al.,
2023) equips models with an external, read-write
memory unit via direct API interactions. Further-
more, TiM (Liu et al., 2023) improves reteieval ef-
ficiency by storing abstracted, structured “thoughts”
rather than unstructured conversation history, and
CoPS (Zhou et al., 2024) applies a tripartite human-
inspired memory system to organize search histo-
ries for personalized retrieval.
Beyond structural storage, agents increasingly
2

rely on experiential learning and domain-specific
state tracking to evolve dynamically without weight
updates. Reflexion (Shinn et al., 2023) optimizes
agent decision-making by storing natural language
self-reflections of past failures in episodic mem-
ory. Similarly, ExpeL (Zhao et al., 2024) ex-
tracts high-level insights from successful trajec-
tory memories in vector stores to enable cross-
task generalization. Incorporating cognitive mecha-
nisms, MemoryBank (Zhong et al., 2024a) applies
Ebbinghaus’s forgetting curve to guide memory
update and retention strategies. Expanding into
physical and multimodal environments, JARVIS-
1 (Wang et al., 2024b) uses a multimodal mem-
ory component for lifelong planning in open-world
tasks, MuRAG (Chen et al., 2022) lays the ground
for cross-modal retrieval-augmented reasoning,
and Fan et al. (2024) proposes a unified memory
mechanism tracking temporal segment descriptions
and object states for video understanding.
To rigorously evaluate long-term contextual re-
tainment and retrieval fidelity, several benchmark-
ing suits have been developed. LOCOMO (Ma-
harana et al., 2024) assesses how agents reflect on
and retrieve multi-session personalized information
over extensive temporal horizons. Similarly, Long-
MemEval (Wu et al., 2024) probes the memory
capacity of chat assistants and analyzes optimized
indexing and reading strategies. Extending these
evaluations across those criteria, MemBench (Tan
et al., 2025) benchmarks agentic memory mecha-
nisms using multi-scenario, multi-level, and multi-
metric dimensions. Addressing localized memory
extraction, MemInsight (Salama et al., 2025) eval-
uates autonomous memory augmentation by gener-
ating attribute-based representations.
Reviews provide formal taxonomies and con-
ceptual baselines for categorizing diverse agentic
memory mechanisms. Zhang et al. (2025b) present
a comprehensive review mapping out agentic mem-
ory implementations, evaluation methodologies,
and current boundaries. Similarly, Wang et al.
(2024a) classify autonomous agent memory mod-
ules through the tri-fold lens of memory structures,
formats, and core operations. From a holistic per-
spective, Xi et al. (2025) formulated a general agent
framework comprising brain, perception, and ac-
tion modules, situating long-term memory with
societal behavior and prospective challenges.
2.2 Alignment and Misalignment
Retrieval-augmented mechanisms inherently suffer
from contextual bottlenecks and factual halluci-
nations that undermine system reliability. Shuster
et al. (2021) showed that grounding dialogue in neu-
ral retrieval mitigates hallucination, though Dziri
et al. (2022) and Zhang et al. (2025a) highlight per-
sistent factual error patterns across the LLM lifecy-
cle. In terms of structural context limitations, Liu
et al. (2024) identify the “lost in the middle” phe-
nomenon, showing a U-shaped performance curve
where LLMs struggle to recall information posi-
tioned in the middle of long sequences. To evaluate
these boundaries, RGB (Chen et al., 2024a) intro-
duces a benchmark targeting RAG capabilities in
noise robustness and negative rejection.
Integrating persistent, updatable memory ex-
poses agents to novel adversarial vectors, privacy
leaks, and data manipulation attacks. AGENTPOI-
SON (Chen et al., 2024b) introduces a backdoor
attack that pollutes an agent’s memory to force
malicious actions, while Hubinger et al. (2024)
prove that backdoor behaviors can stubbornly
survive standard safety fine-tuning. Addressing
memory-specific threats, Sunil et al. (2026) evalu-
ate memory injection attacks (MINJA) on health-
care agents and propose trust-aware memory sani-
tization. Tool-calling vulnerabilities are analyzed
in InjecAgent (Zhan et al., 2024), Indirect Prompt
Injection (IPI) threats introduced by Greshake et al.
(2023), and stateful environmental security evalu-
ated via AgentDojo (Debenedetti et al., 2024). Fur-
thermore, MEXTRA (Wang et al., 2025) exposes
privacy risks by demonstrating black-box extrac-
tion of sensitive conversation history from agent
memory, complementing real-world empirical find-
ings by Jo et al. (2024) regarding memory-induced
user privacy concerns in public health chatbots.
Mitigating these safety risks requires robust
alignment frameworks, structural defense, and safe
design paradigms. InstructGPT (Ouyang et al.,
2022) establishes the foundation for aligning LLMs
with user intent via Reinforcement Learning from
Human Feedback (RLHF). Addressing explicit in-
struction safety, Wallace et al. (2024) propose an
instruction hierarchy framework to enforce system
instruction precedence over lower-privileged user
or tool inputs, thereby defending against prompt
injections. From a holistic architectural perspec-
tive, Li et al. (2024) review the intelligence levels,
capabilities, and security boundaries of personal
3

agents, while Amodei et al. (2016) categorize foun-
dational empirical machine learning safety risks to
guide trustworthy system deployment.
3 MemAlign
We buildMemAlignon the dataset introduced
by Chen et al. (2026). The task is a binary de-
cision of whether a candidate memory should be
stored for future personalization. Given a candi-
date memory and its historical interaction context,
a model predicts STOREor DONOTSTORE, with
the original user-annotated storage decision serv-
ing as the reference label (see Figure 2 for the
label and reason-type distributions). Each original
record contains a candidate memory, an accuracy
annotation, a storage decision, and brief user feed-
back on the memory. To provide the conversational
grounding absent in the source data, we synthesize
a multi-turn historical interaction context for each
instance while retaining all original annotations.
Context Generation.We employ Qwen3.8-Max
(Qwen Team, 2026) to synthesize conversational
histories conditioned on four pieces ofconstruction
supervision: the candidate memory, user feedback,
assigned reason type, and gold storage decision.
These inputs serve to reconstruct the latent eviden-
tiary relationship between the generated dialogue
and the candidate memory, not to reveal the gold
storage label to downstream admission models.
Specifically, the generated context must faith-
fully mirror the epistemic certainty, entity attribu-
tion, temporal status, and scope implied by the
evidence. For instance, over-inferred memories
are backed only by weak or indirect premises,
attribution-confusion cases maintain strict entity
ownership, stale memories incorporate explicit tem-
poral shifts, and inaccurate memories retain the
contradictions noted in user feedback.
To prevent label leakage and artificial artifacts,
the model is strictly constrained from lexicaliz-
ing metadata, such as storage labels, reason cate-
gories, or retention preferences, echoing the candi-
date memory verbatim, amplifying recurrence or
permanence, or fabricating personal details. The
synthesized dialogue therefore features natural in-
teractional cues, such as routine requests, correc-
tions, and follow-ups, rather than summary-level
persona profiles. Furthermore, generation prompts
enforce session parsimony, where dialogues use
one session by default, extending to two or three
only when modelling temporal updates or indepen-
dent interactions demands it. Session counts are
explicitly decoupled from the assigned reason type,
and the source memory’s language is preserved.
779 (72.2%) 300 (27.8%)
0 200 400 600 800
Number of cases
Directly relevant 780 (72.3%)
False memory use 108 (10.0%)
Over-inference 55 (5.1%)
Granularity mismatch 33 (3.1%)
Context misapplication 31 (2.9%)
Incomplete memory use 18 (1.7%)
Stale memory use 17 (1.6%)
Attribution confusion 15 (1.4%)
Identity mis-inference 11 (1.0%)
Privacy overuse 11 (1.0%)
(a) Storage decision N = 1,079
STORE DO NOT STORE
(b) Reason type
Figure 2: Distribution of (a) storage decisions and (b)
reason types in MEMALIGN( N= 1,079 ). Labels
indicate instance counts and percentages.
Validation.To assess and improve context qual-
ity, we combine two-stage automated validation
with human review. Structural checks require one
to three sequentially indexed sessions, each con-
taining two, four, or six non-empty messages with
alternating user and assistant roles. Each session
starts with a user utterance and ends with an assis-
tant response, and the total context contains at most
12 messages. Additional checks screen for near-
verbatim reproduction of the candidate memory
and explicit benchmark taxonomy leakage.
We then conduct semantic validation using GPT-
6 Astra. The audit assesses eight dimensions: evi-
dence fidelity, reason-type consistency, candidate-
memory mirroring, diagnostic shortcuts, annotation
lexicalization, retention leakage, reason-specific
templating, and conversational naturalness and con-
ciseness. Acceptance requires fidelity and consis-
tency with the available evidence, natural dialogue,
and the absence of the identified artifacts. Con-
texts requiring revision are refined using structural
error reports and semantic feedback. Across the
1,081 initial instances, generation involved one,
two, three, or four attempts for 898, 155, 16, and
12 instances, respectively. These counts include
two instances that received manual supplements
and were subsequently excluded.
Post-generation refinement included restoring
richer reference contexts for 139 instances and
manually rewriting seven additional contexts to ad-
4

Historical context C Candidate memory M
Future probe construction
Three future probes:
Relevant
Memory can affect response
Irrelevant
Behavioral invariance
Risk-sensitive
Conflict or scope change
Probe auditor + validation
C used for evaluation
Controlled responses
For each validated qᵢ
Without M
Rᵢ⁰
f(qᵢ)
With M
Rᵢ¹
f(qᵢ, M)
Dual evaluation
Compare Rᵢ⁰ and Rᵢ¹
Blind response
quality attribution
Memory
Which R better
current
interaction?
serves the
Was M used?
How did it affect
the response?
Response effect E ᵢ
A ttribution Pᵢ
Agg re g ation &  admission
Probe contributions cᵢ
CMT E( M )  =  ⅓  Σ  cᵢ
A cross three probes
tie - brea k
S tore Do- N ot- S tore
Figure 3: Overview of ConMem. Given a historical context C and a candidate memory M, ConMem (1) constructs
and validates three future probes (relevant, irrelevant, and risk-sensitive); (2) generates a control responseR0 i without
M and a treatment response R1 i with M for each probe qi; (3) compares the two responses with a blind quality
judge and a memory-attribution auditor; and (4) aggregates the signed probe contributions ci into CMTE(M) to
decide STOREor DO-NOT-STORE, invoking a tie-break judge when the score is zero. C is withheld from response
generation and used only for evaluation.
dress unnatural compression, artificial diagnostic
cues, or unsupported details. Two researchers inde-
pendently reviewed the generated contexts against
the same quality criteria, resolving disagreements
through discussion. The review concerned the syn-
thesized contexts; the original accuracy and storage
annotations remained unchanged. The two manu-
ally supplemented instances were excluded because
the source feedback provided insufficient evidence
to ground their contexts, leaving 1,079 instances
in the final benchmark. The final dataset contains
779 STOREinstances (72.2%) and 300 DO-NOT-
STOREinstances (27.8%), spanning ten reason cat-
egories. Figure 2 presents storage decisions’ and
reason types’ distributions.
4 ConMem
4.1 Overview
ConMem determines whether a candidate memory
should be retained by estimating itsCounterfac-
tual Memory Treatment Effect (CMTE)on fu-
ture interactions. Given historical context C and
candidate memory M, ConMem constructs con-
trolled future scenarios and compares responses
generated with and without access to M. Rather
than predicting storage suitability directly from the
memory text, it evaluates whether access to the
memory produces useful, unnecessary, or risky be-
havioral changes.
The framework consists of four stages, as il-
lustrated in Figure 3: future probe construction,
controlled response generation, dual evaluation
of response quality and memory attribution, and
counterfactual aggregation for admission. Detailed
prompts are provided in Appendix B.
4.2 Future Probe Construction
Because memory utility is inherently context-
dependent, each candidate memory is evaluated
across a probe triplet Q={q rel, qirr, qrisk}. The
relevantprobe creates a realistic setting in which
M provides non-redundant user-specific informa-
tion that materially affect the response. Their-
relevantprobe represents a task whose response
quality should not depend on M. Theriskprobe
introduces an observable change (e.g., target entity
shifts, overrides, or scope transitions) designed to
expose inappropriate memory carry-over.
Probe Validation.An independent probe auditor
verifies that generated queries fulfill their desig-
nated semantic roles while ensuring no leakage of
candidate memories, gold storage labels, or bench-
mark artifacts. Invalid probes are revised before
evaluation. We first regenerate the probe set while
preserving valid probes, then repair individual in-
valid roles when necessary, and use a fresh recon-
struction only for cases that remain invalid. This
guarantees downstream treatment effects reflect
memory utility rather than flawed probes.
4.3 Controlled Counterfactual Responses
To isolate the marginal causal effect of candidate
memory M, control and treatment generations dif-
5

fer exclusively by memory access: R0 i =f(q i),
R1 i =f(q i, M). Both branches use identical model
configurations. The treatment condition receives
M as optional context alongside instructions to
apply it solely when relevant and appropriate. His-
torical context C is withheld from both generation
branches to isolate the direct causal impact of M,
and is reserved for downstream evaluation to as-
sess whether memory-induced personalization is
substantiated by prior interactions.
4.4 Dual Evaluation of Memory Effects
As generation variance can arise independently of
memory retrieval, ConMem decouples response
quality assessment from memory attribution.
Blind Response Quality.A blind pairwise judge
evaluates R0 i and R1 i against historical context C
and probe q. The judge is agnostic to M and
treatment-assignment conditions. Generations are
presented in deterministically randomized order
(positions A/B) to counter position bias, yielding a
preference ofA,BorTie.
Memory Attribution.An attribution auditor eval-
uates C, M, qi, R0 i , and R1 i to ascertain if M
was substantively invoked and materially altered
outputs, classifying behavioral effects into: Pi ∈
{utility,unnecessary,neutral,risk} whereUtility
signifies accurate, appropriately bounded personal-
ization;unnecessarydenotes benign yet irrelevant
incorporation,riskcaptures negative externalities
such as entity confusion or over-generalization, and
neutralindicates no material intervention.
Decoupling these two judgments prevents
generation quality variation from being inter-
preted as evidence of memory misalignment.
We define the response-level effect Ei ∈
{HELPFUL,NEUTRAL,HARMFUL}. If the mem-
ory is not substantively used or does not change the
treatment response, Ei is NEUTRAL. Otherwise,
it is HELPFULwhen the judge prefers treatment
response, HARMFULwhen preferring control re-
sponse, and NEUTRALfor a tie.
4.5 Counterfactual Scoring and Admission
Probe Contributions.Each probe contributes a
signed effect according to its semantic role, at-
tributed use, and observed response quality. For
a relevant probe, helpful utility contributes +1.0,
while attributed risk contributes −1.0. For an ir-
relevant probe, unnecessary personalization con-
tributes −0.5 and attributed risk contributes −1.0.
For a risk probe, helpful utility contributes +0.5,
unnecessary personalization contributes −0.5, and
attributed risk contributes −1.5. All other out-
comes contribute 0. Positive evidence therefore
requires both causal attribution of memory use
and response quality improvement. Negative evi-
dence requires explicit attribution of unnecessary
or risky use. The aggregate metric is computed as:
CMTE(M) = 1 K PK i=1 ci, K= 3.
Score-First Admission.A positive ConMem
score yields STORE, while a negative score yields
DO-NOT-STORE: When |CMTE(M)| ≤ϵ, ev-
idence is considered inconclusive. ConMem in-
vokes a parameter-independent tie-break judge that
evaluates C, M, and raw counterfactual logs. This
tie-breaker is shielded from predetermined numeric
weights and gold labels, preventing heuristic bias.
Reason Classification.Following admission,
ConMem executes a post-hoc classification
to assign a structured explanation, but does
not modify ˆyor CMTE(M). Accepted cases
(STORE) map to directly_relevant. For
rejected cases (DO-NOT-STORE), a classifier
takes C, M, ˆy, and the generation ratio-
nale to assign the primary failure category:
context_misapplication, memory_omission,
granularity_mismatch, over_inference,
stale_memory_use, privacy_refusal,
privacy_overuse, attribution_confusion,
identity_misinference, incomplete_memory_
use, or false_memory_use. These categorical
attributions are primarily used for downstream
interpretation and failure analysis.
5 Experiments
5.1 Methods
We compare the following methods:
•ConMem: as introduced in Sec. 4.
• SAGE: a multi-agent reasoning framework
(Challenger, Planner, Solver, Critic) tested here
for its deliberation capability in memory admis-
sion (Peng et al., 2026).
• A-MAC: an admission control method scoring
candidates by expected utility, factual confidence,
semantic novelty, recency, and content-type pri-
ors (Zhang et al., 2026).
• A-MEM (Xu et al., 2025): organizes dialogue
into attributed memories. Following Zhang et al.
(2026), candidates are scored via normalized im-
portance and semantic novelty.
6

• MemoryBank: Zhong et al. (2024b) models
retention via recency, relevance, and importance. It
followed Zhang et al. (2026) by scoring candidates
via semantic relevance and estimated utility.
5.2 Parameters and Settings
All ConMem components and baseline LLM back-
bones use Qwen3.8-Max with temperature 0, seed
42, and default API decoding parameters. Out-
put token limits are capped at 2,048 for probing,
validation, auditing, and tie-breaking stages, and
8,192 for control and treatment response gener-
ation. We employ medium reasoning effort for
probe, response, and quality generation, and high
effort for validation, auditing, and tie-breaking.
Each candidate is evaluated across three scenario
probes with a zero-score tolerance of ϵ= 10 −12,
requiring 14 standard model calls plus an optional
tie-break call, with detailed efficiency metrics ap-
pear in Appendix C. For baselines evaluated on
the same 1,079 candidates, A-MAC (Zhang et al.,
2026) adopts its published five-feature policy with
weights (0.1, 0.1, 0.1, 0.1, 0.6), and a 0.55 thresh-
old. A-MEM (Xu et al., 2025) computes admis-
sion scores as 0.7Inorm+0.3N (threshold 0.5) from
extracted attributes. MemoryBank (Zhong et al.,
2024a) uses 0.3R + 0.4L + 0.3I, adapting recency
to benchmark constraints. SAGE (Peng et al., 2026)
evaluates decisions from its multi-agent reasoning.
5.3 Results
5.3.1 Overall Performance
Table 1 compares ConMem with MemoryBank, A-
MEM, A-MAC, and SAGE on the 1,079 candidate
memories. ConMem achieves 75.16% accuracy,
64.15% balanced accuracy, and 65.13% Macro-F1,
outperforming all baselines on accuracy and Macro-
F1. Relative to the strongest accuracy baseline, A-
MAC, ConMem yields gains of 5.83, 12.23 and
15.40 percentage points across accuracy, balanced
accuracy and Macro-F1, respectively. Compared to
MemoryBank, the leading baseline in balanced ac-
curacy, ConMem improves accuracy by 3.97 points
and Macro-F1 by 1.01 points.
Class-wise performance highlights contrasting
admission behaviors. A-Mem and A-MAC exhibit
an over-retention bias, attaining highStorerecall
(88.83% and 91.12%) at the expense ofDo-Not-
Storerecall (11.67% and 12.71%). Conversely,
MemoryBank offers a more balanced trade-off
(69.67%Do-Not-Storeand 66.24%Storerecall),
while SAGE excessively rejects candidates, captur-
ing only 34.15% of validStorememories. Con-
Mem achieves the best overall trade-off, sustaining
a highStorerecall of 88.96% while increasingDo-
Not-Storerecall to 39.33%, thereby securing the
highest balanced accuracy and Macro-F1.
Table 1: Performance comparison across techniques.
Method Acc. BAcc. Macro-F1 Store R. DNS R.
MemoryBank 67.19 67.95 64.30 66.2469.67
A-MEM 67.38 50.25 48.16 88.83 11.67
A-MAC 69.33 51.91 49.9191.1212.71
SAGE 40.96 46.41 40.55 34.15 58.67
ConMem75.1664.1565.3188.96 39.33
5.3.2 Cross-Dataset Generalization
LoCoMo.We evaluated all methods on LoCoMo,
where ConMem achieves the highest precision of
41.8%, outperforming competitors such as A-MAC
(41.7%) and A-MEM (37.1%). While methods like
A-MEM and A-MAC yield higher recall (100.0%
and 97.2%, respectively), ConMem maintains a
balanced trade-off with 75.7% recall and a 53.9%
F1 score. This substantially outperforms retrieval
baselines like MemGPT (32.4% F1) and Memory-
Bank (45.2% F1), rivaling dedicated frameworks
and confirming its strong generalizability across
memory management benchmarks.
HaluMem.We further evaluate ConMem on
HaluMem, which separates valid reference mem-
ories from interfering ones. On a randomly se-
lected balanced 400-case subset, ConMem achieves
66.00% accuracy, 66.00% balanced accuracy, and
63.22% Macro-F1, retaining 93.50% of valid mem-
ories while rejecting 38.50% of distractor memo-
ries. These results show ConMem’s efficacy un-
der distinct criteria targeting memory interference,
while the lowerDo-Not-Storerecall reflects an
ongoing inclination toward over-retention.
5.3.3 Error Analysis
ConMem achieves 881/1,079 accuracy, with errors
heavily skewed toward over-retention: 182 false
positives (60.67% ofDo-Not-Store) versus 86 false
negatives (11.04% ofStore). This disparity reflects
asymmetric counterfactual scoring. False Positives
stem from unpenalized utility, where strong rel-
evance signals (mean +0.852) overshadow unde-
tected risks (risk mean +0.107). Conversely, FNs
result from disproportionate risk penalties (mean
-1.052), which override valid relevance signals
(mean +0.360) and lead to erroneous discards.
7

Rejection efficacy varies substantially across er-
ror types (Table 2). ConMem effectively flags
factual inconsistencies (e.g.,state_memory_use
at 58.82% recall andfalse_memory_useat
57.41%), but underperforms on fine-grained
contextual and scoping boundaries, including
context_misapplication(12.90%) andincom-
plete_memory_use(16.67%). Notably, tie-
breaking is not the primary error source, where
the admission judge achieves 81.91% accuracy on
the 199 tie-break cases. Misclassifications primar-
ily stem from upstream counterfactual evidence
generation and aggregation than final arbitration.
Table 2: ConMem performance across rejection cate-
gories.
Reason typeNRecall (%)
context_misapplication 31 12.90
incomplete_memory_use 18 16.67
granularity_mismatch 33 21.21
identity_mis_inference 11 27.27
privacy_overuse 11 27.27
attribution_confusion 15 33.33
over_inference 55 38.18
false_memory_use 108 57.41
stale_memory_use 17 58.82
5.3.4 Parameter Sensitivity
We evaluate ConMem over 27 pre-specified com-
binations of its three scoring parameters, with the
setting fixed before evaluation. Across these set-
tings, accuracy spans 75.16%–78.13%, balanced
accuracy 64.15%–65.69%, and Macro-F1 65.31%–
67.50%. STORErecall varies from 88.96% to
93.71%, while DO-NOT-STORErecall remains be-
tween 37.33% and 39.67%. Overall, ConMem ex-
hibits strong parameter stability, with the default
configuration achieving 75.16% accuracy, 64.15%
balanced accuracy, and 65.31% Macro-F1. Com-
plete results are detailed in Appendix A.
5.3.5 Backbone Robustness
We evaluate ConMem with three backbones,
Qwen3.8-Max, GPT-5.6-sol, and DeepSeek-V4-
Flash, on the same 1,079 cases under identical
prompts, evaluation protocols, scoring weights, and
admission rules. GPT-5.6-sol achieves the highest
accuracy (77.85%), balanced accuracy (70.93%),
and Macro-F1 (71.54%), followed by DeepSeek-
V4-Flash (76.83%, 67.76%, and 68.89%) and
Qwen3.8-Max (75.16%, 64.15%, and 65.31%).
For DeepSeek, sensitivity analyses over 27 pre-
defined cost configurations yields stable accuracies
(76.65%–77.94%), confirming robustness to coeffi-
cient variations. Full results appear in Appendix D.
5.3.6 Ablation Study
To assess ConMem’s validation and decision mod-
ules, we evaluate four variants on the 1,079 cases
using original probe sets and weights: (1)w/o Qual-
ity Judge, which directly uses the attribution audi-
tor’s utility assessment without blind quality confir-
mation; (2)w/o Attribution Auditor, which derives
utility scores solely from pairwise preferences with-
out causal attribution verification; and (3–4)Zero
→ STOREandZero → DO_NOT_STORE, replac-
ing zero-score tie-breaker with fixed defaults.
Table 3: Ablation results for ConMem’s validation and
decision components (%).
Variant Acc. BAcc. Macro-F1
Full ConMem75.16 64.15 65.31
w/o Quality Judge 72.57 59.28 59.87
w/o Attribution Auditor 55.05 55.55 52.41
Zero→STORE 71.73 56.85 56.83
Zero→DO_NOT_STORE 66.82 60.93 60.38
As shown in Table 3, removing the quality judge
reduces Macro-F1 from 65.31% to 59.87%, while
removing the attribution auditor degrades it fur-
ther to 52.41%, showing the synergy between qual-
ity confirmation and causal attribution. More-
over, replacing adaptive tie-breaking with fixed
decisions degrades performance, where a default
SCORE inflates false-positive retention, and a de-
fault DO_NOT_STORE leads to under-admission.
These results highlight the need to couple evidence
verification with adaptive thresholding.
6 Conclusion
This paper tackles memory misalignment in LLM
chatbots, where conventional memory admission
fails to discern whether candidate memories are
appropriate. To address this, we introduceMemA-
lign, a benchmark of 1,079 memories grounded
in verified multi-session dialogues, alongsideCon-
Mem. grounded in counterfactual memory treat-
ment effects,ConMemevaluates candidates by
simulating causal interventions across diverse fu-
ture probes spanning utility, invariance, and risk,
while decoupling blind quality assessment from
attribution auditing. Empirical results show that
ConMemconsistently outperforms competitive
baselines, achieving 75.16% accuracy, 64.15% bal-
anced accuracy, and 65.31% Macro-F1.
8

Limitations
We acknowledge several limitations of this paper.
First, although verified, the memory context is syn-
thetic, which may differ from realistic chat histo-
ries. We made this choice because users can hardly
memorize their histories, and those histories also
pose privacy concerns. Future work could build
upon our work to build such traces. Second, we
primarily target the memories for LLM-based chat-
bots that face Chinese users, noting that memories
in other agentic systems may be different and war-
rant future examination.
Ethics Statement
This work complies with the ACL Ethics Pol-
icy. The multi-session conversational histories con-
structed for MemAlign are entirely synthetic and
contain no personally identifiable information (PII).
All user attributes, preference profiles, and inter-
action trajectories represent simulated scenarios
designed strictly for probing memory misalign-
ment taxonomies. No private personal logs, propri-
etary user communications, or real-world sensitive
records were collected, crawled, or utilized during
benchmark construction or evaluation.
From a broad societal perspective, deploying per-
sistent memory mechanisms in autonomous agents
introduces systemic risks regarding privacy leak-
age, unwarranted personalization, and the perpet-
uation of misattributed user traits. Rather than ex-
acerbating these hazards, ConMem is intentionally
architected as an alignment and safety mechanism.
By enforcing behavioral invariance across irrele-
vant inquiries and explicitly penalizing inappro-
priate memory carry-over under contextual bound-
ary shifts, the framework actively prevents privacy
overuse and over-retention, fostering trustworthy
and boundary-aware conversational agent deploy-
ments.
References
Dario Amodei, Chris Olah, Jacob Steinhardt, Paul
Christiano, John Schulman, and Dan Mané. 2016.
Concrete problems in ai safety.arXiv preprint
arXiv:1606.06565.
Jiawei Chen, Hongyu Lin, Xianpei Han, and Le Sun.
2024a. Benchmarking large language models in
retrieval-augmented generation. InProceedings of
the AAAI conference on artificial intelligence, vol-
ume 38, pages 17754–17762.
Jingruo Chen, Shuning Zhang, Eryue Xu, Jianing Li,
and Xin Yi. 2026. Characterizing memory misalign-
ment in human-llm interaction from user perspectives.
Preprint, arXiv:2609.33623.
Wenhu Chen, Hexiang Hu, Xi Chen, Pat Verga, and
William Cohen. 2022. Murag: Multimodal retrieval-
augmented generator for open question answering
over images and text. InProceedings of the 2022
Conference on Empirical Methods in Natural Lan-
guage Processing, pages 5558–5570.
Zhaorun Chen, Zhen Xiang, Chaowei Xiao, Dawn Song,
and Bo Li. 2024b. Agentpoison: Red-teaming llm
agents via poisoning memory or knowledge bases.
Advances in Neural Information Processing Systems,
37:130185–130213.
Edoardo Debenedetti, Jie Zhang, Mislav Balunovic,
Luca Beurer-Kellner, Marc Fischer, and Florian
Tramèr. 2024. Agentdojo: A dynamic environment
to evaluate prompt injection attacks and defenses for
llm agents.Advances in neural information process-
ing systems, 37:82895–82920.
Nouha Dziri, Sivan Milton, Mo Yu, Osmar R Zaiane,
and Siva Reddy. 2022. On the origin of hallucinations
in conversational models: Is it the datasets or the
models? InProceedings of the 2022 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, pages 5271–5285.
Yue Fan, Xiaojian Ma, Rujie Wu, Yuntao Du, Jiaqi
Li, Zhi Gao, and Qing Li. 2024. Videoagent: A
memory-augmented multimodal agent for video un-
derstanding. InEuropean Conference on Computer
Vision, pages 75–92. Springer.
Kai Greshake, Sahar Abdelnabi, Shailesh Mishra,
Christoph Endres, Thorsten Holz, and Mario Fritz.
2023. Not what you’ve signed up for: Compromis-
ing real-world llm-integrated applications with indi-
rect prompt injection. InProceedings of the 16th
ACM workshop on artificial intelligence and security,
pages 79–90.
Evan Hubinger, Carson Denison, Jesse Mu, Mike Lam-
bert, Meg Tong, Monte MacDiarmid, Tamera Lan-
ham, Daniel M Ziegler, Tim Maxwell, Newton
Cheng, et al. 2024. Sleeper agents: Training decep-
tive llms that persist through safety training.arXiv
preprint arXiv:2401.05566.
Eunkyung Jo, Yuin Jeong, SoHyun Park, Daniel A Ep-
stein, and Young-Ho Kim. 2024. Understanding
the impact of long-term memory on self-disclosure
with large language model-driven chatbots for pub-
lic health intervention. InProceedings of the 2024
CHI Conference on Human Factors in Computing
Systems, pages 1–21.
Yuanchun Li, Hao Wen, Weijun Wang, Xiangyu Li,
Yizhen Yuan, Guohong Liu, Jiacheng Liu, Wenx-
ing Xu, Xiang Wang, Yi Sun, et al. 2024. Per-
sonal llm agents: Insights and survey about the
9

capability, efficiency and security.arXiv preprint
arXiv:2401.05459.
Lei Liu, Xiaoyan Yang, Yue Shen, Binbin Hu, Zhiqiang
Zhang, Jinjie Gu, and Guannan Zhang. 2023. Think-
in-memory: Recalling and post-thinking enable
llms with long-term memory.arXiv preprint
arXiv:2311.08719.
Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paran-
jape, Michele Bevilacqua, Fabio Petroni, and Percy
Liang. 2024. Lost in the middle: How language mod-
els use long contexts.Transactions of the association
for computational linguistics, 12:157–173.
Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov,
Mohit Bansal, Francesco Barbieri, and Yuwei Fang.
2024. Evaluating very long-term conversational
memory of llm agents. InProceedings of the 62nd
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 13851–
13870.
Ali Modarressi, Ayyoob Imani, Mohsen Fayyaz, and
Hinrich Schütze. 2023. Ret-llm: Towards a general
read-write memory for large language models.arXiv
preprint arXiv:2305.14322.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow instruc-
tions with human feedback.Advances in neural in-
formation processing systems, 35:27730–27744.
Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang,
Shishir G Patil, Ion Stoica, and Joseph E Gonzalez.
2023. Memgpt: Towards llms as operating systems.
arXiv preprint arXiv:2310.08560.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Mered-
ith Ringel Morris, Percy Liang, and Michael S Bern-
stein. 2023. Generative agents: Interactive simulacra
of human behavior. InProceedings of the 36th an-
nual acm symposium on user interface software and
technology, pages 1–22.
Yulin Peng, Xinxin Zhu, Chenxing Wei, Nianbo Zeng,
Leilei Wang, Ying Tiffany He, and F. Richard Yu.
2026. Sage: Multi-agent self-evolution for llm rea-
soning.Preprint, arXiv:2603.15255.
Qwen Team. 2026. Qwen3.8: A new bar for coding and
cowork.
Rana Salama, Jason Cai, Michelle Yuan, Anna Currey,
Monica Sunkara, Yi Zhang, and Yassine Benajiba.
2025. Meminsight: Autonomous memory augmen-
tation for llm agents. InProceedings of the 2025
Conference on Empirical Methods in Natural Lan-
guage Processing, pages 33124–33140.
Noah Shinn, Federico Cassano, Ashwin Gopinath,
Karthik Narasimhan, and Shunyu Yao. 2023. Re-
flexion: Language agents with verbal reinforcement
learning.Advances in neural information processing
systems, 36:8634–8652.
Kurt Shuster, Spencer Poff, Moya Chen, Douwe Kiela,
and Jason Weston. 2021. Retrieval augmentation
reduces hallucination in conversation. InFindings
of the Association for Computational Linguistics:
EMNLP 2021, pages 3784–3803.
Balachandra Devarangadi Sunil, Isheeta Sinha, Piyush
Maheshwari, Shantanu Todmal, Shreyan Mallik, and
Shuchi Mishra. 2026. Memory poisoning attack and
defense on memory based llm-agents.arXiv preprint
arXiv:2601.05504.
Haoran Tan, Zeyu Zhang, Chen Ma, Xu Chen, Quanyu
Dai, and Zhenhua Dong. 2025. Membench: Towards
more comprehensive evaluation on the memory of
llm-based agents. InFindings of the Association for
Computational Linguistics: ACL 2025, pages 19336–
19352.
Eric Wallace, Kai Xiao, Reimar Leike, Lilian Weng,
Johannes Heidecke, and Alex Beutel. 2024. The in-
struction hierarchy: Training llms to prioritize privi-
leged instructions.arXiv preprint arXiv:2404.13208.
Bo Wang, Weiyi He, Shenglai Zeng, Zhen Xiang, Yue
Xing, Jiliang Tang, and Pengfei He. 2025. Unveiling
privacy risks in llm agent memory. InProceedings
of the 63rd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 25241–25260.
Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao
Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang,
Xu Chen, Yankai Lin, et al. 2024a. A survey on large
language model based autonomous agents.Frontiers
of computer science, 18(6):186345.
Weizhi Wang, Li Dong, Hao Cheng, Xiaodong Liu,
Xifeng Yan, Jianfeng Gao, and Furu Wei. 2023. Aug-
menting language models with long-term memory.
Advances in neural information processing systems,
36:74530–74543.
Zihao Wang, Shaofei Cai, Anji Liu, Yonggang Jin, Jin-
bing Hou, Bowei Zhang, Haowei Lin, Zhaofeng
He, Zilong Zheng, Yaodong Yang, et al. 2024b.
Jarvis-1: Open-world multi-task agents with memory-
augmented multimodal language models.IEEE
Transactions on Pattern Analysis and Machine In-
telligence, 47(3):1894–1907.
Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang,
Kai-Wei Chang, and Dong Yu. 2024. Longmemeval:
Benchmarking chat assistants on long-term interac-
tive memory.arXiv preprint arXiv:2410.10813.
Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen
Ding, Boyang Hong, Ming Zhang, Junzhe Wang, Sen-
jie Jin, Enyu Zhou, et al. 2025. The rise and potential
of large language model based agents: A survey.Sci-
ence China information sciences, 68(2):121101.
Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Jun-
tao Tan, and Yongfeng Zhang. 2025. A-mem:
Agentic memory for llm agents.arXiv preprint
arXiv:2502.12110.
10

Qiusi Zhan, Zhixiang Liang, Zifan Ying, and Daniel
Kang. 2024. Injecagent: Benchmarking indirect
prompt injections in tool-integrated large language
model agents. InFindings of the Association for
Computational Linguistics: ACL 2024, pages 10471–
10506.
Guilin Zhang, Wei Jiang, Xiejiashan Wang, Aisha Behr,
Kai Zhao, Jeffrey Friedman, Xu Chu, and Amine
Anoun. 2026. Adaptive memory admission control
for llm agents.arXiv preprint arXiv:2603.04549.
Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao Liu,
Tingchen Fu, Xinting Huang, Enbo Zhao, Yu Zhang,
Yulong Chen, et al. 2025a. Siren’s song in the ai
ocean: A survey on hallucination in large language
models.Computational Linguistics, 51(4):1373–
1418.
Zeyu Zhang, Quanyu Dai, Xiaohe Bo, Chen Ma, Rui Li,
Xu Chen, Jieming Zhu, Zhenhua Dong, and Ji-Rong
Wen. 2025b. A survey on the memory mechanism of
large language model-based agents.ACM Transac-
tions on Information Systems, 43(6):1–47.
Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu
Lin, Yong-Jin Liu, and Gao Huang. 2024. Expel:
Llm agents are experiential learners. InProceedings
of the AAAI Conference on Artificial Intelligence,
volume 38, pages 19632–19642.
Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and
Yanlin Wang. 2024a. Memorybank: Enhancing large
language models with long-term memory. InPro-
ceedings of the AAAI conference on artificial intelli-
gence, volume 38, pages 19724–19731.
Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and
Yanlin Wang. 2024b. Memorybank: enhancing large
language models with long-term memory. InPro-
ceedings of the Thirty-Eighth AAAI Conference on
Artificial Intelligence and Thirty-Sixth Conference on
Innovative Applications of Artificial Intelligence and
Fourteenth Symposium on Educational Advances in
Artificial Intelligence, AAAI’24/IAAI’24/EAAI’24.
AAAI Press.
Yujia Zhou, Qiannan Zhu, Jiajie Jin, and Zhicheng Dou.
2024. Cognitive personalized search integrating large
language models with an efficient memory mecha-
nism. InProceedings of the ACM Web Conference
2024, pages 1464–1473.
11

Appendix
A Parameter Sensitivity Details
Table 4: Sensitivity results for the nine distinct combinations of the risk-safe reward and explicit-risk penalty.
Results are identical for irrelevant-personalization costs of 0.25, 0.50, and 0.75 when the other parameters are fixed.
Safe Reward Risk Penalty Acc. BAcc. Macro-F1 Store R. DNS R.
0.00 1.0 78.13 65.69 67.50 93.71 37.67
0.00 1.5 75.25 64.31 65.49 88.96 39.67
0.00 2.0 75.25 64.31 65.49 88.96 39.67
0.25 1.0 78.04 65.52 67.31 93.71 37.33
0.25 1.5 75.16 64.15 65.31 88.96 39.33
0.25 2.0 75.16 64.15 65.31 88.96 39.33
0.50 1.0 78.04 65.52 67.31 93.71 37.33
0.50 1.575.16 64.15 65.31 88.96 39.33
0.50 2.0 75.16 64.15 65.31 88.96 39.33
Table 5: Overall sensitivity of ConMem to the scoring parameters.
Metric Main setting Range
Accuracy 75.16 75.16–78.13
Balanced Accuracy 64.15 64.15–65.69
Macro-F1 65.31 65.31–67.50
STORERecall 88.96 88.96–93.71
DNS Recall 39.33 37.33–39.67
Zero-score Rate 18.44 18.44–25.58
We perform a sensitivity analysis over 27 pre-
specified combinations of three scoring parameters:
the cost of unnecessary personalization on an irrele-
vant probe, the reward for safe and helpful memory
use on a risk-sensitive probe, and the penalty for
explicit risk on a risk-sensitive probe. Their tested
values are {0.25,0.50,0.75} , {0,0.25,0.50} , and
{1.0,1.5,2.0} , respectively. The main configura-
tion uses 0.50, 0.50, and 1.50. All settings are
evaluated using the same counterfactual evidence,
and the parameter-independent tie-break procedure
is applied whenever the resulting ConMem score
is zero.
The irrelevant-personalization cost has no effect
on the final admission predictions within the tested
range: changing it from 0.25 to 0.75 produces iden-
tical classification metrics when the other two pa-
rameters are fixed. The reward for safe memory
use has only a small effect. Increasing it from 0
to 0.25 slightly changes the predictions, whereas
increasing it further from 0.25 to 0.50 leaves the
final classification metrics unchanged.
The largest variation is caused by the explicit-
risk penalty on the risk-sensitive probe. With the
other parameters fixed, reducing this penalty from
1.5 to 1.0 increases STORErecall from 88.96% to
93.71%, while DO-NOT-STORErecall decreases
from approximately 39–40% to 37–38%. Con-
sequently, overall accuracy increases to approxi-
mately 78%, largely because STOREcases are more
frequent in the primary benchmark. Increasing the
penalty from 1.5 to 2.0, in contrast, does not alter
the final admission predictions. These results indi-
cate that the observed variation primarily reflects
the expected trade-off between preserving poten-
tially useful memories and penalizing future misuse
than broad instability of the scoring scheme.
Because the irrelevant-personalization cost does
not affect the final predictions, Table 4 collapses the
full 27-setting grid over this dimension and reports
the nine distinct combinations of the remaining two
parameters.
B Prompt Design
This appendix summarizes the prompts used by
ConMem. The prompts follow the functional mod-
ules described in Sec. 4. Benchmark labels are
never provided to the probe generator, response
agents, quality judge, or attribution auditor. Histori-
cal context, candidate memories, generated queries,
and model responses are explicitly delimited and
12

treated as data rather than instructions.
B.1 Future Probe Generation
The probe generator receives the historical context
and candidate memory and produces exactly one
relevant, oneirrelevant, and oneriskprobe. The
candidate memory is not assumed to be correct,
stable, or suitable for storage.
For the relevant probe, the prompt asks for a re-
alistic future query in which the candidate memory
provides non-redundant user-specific information
that could materially affect the response. The query
itself must not reveal or paraphrase that informa-
tion. For the irrelevant probe, the substantive task
outcome should remain independent of the candi-
date memory. For the risk probe, the query must
contain an observable condition—such as a differ-
ent person, an updated fact, an explicit override, or
a scope change—under which inappropriate carry-
over can be detected. Hypothetical staleness alone
is not sufficient.
The prompt further requires all probes to be
natural user requests and prohibits references to
benchmarks, storage decisions, treatment/control
conditions, or hidden memory information.
Historical Context:
<<<HISTORICAL_CONTEXT>>>
{historical_context}
<<<END_HISTORICAL_CONTEXT>>>
Candidate Memory:
<<<CANDIDATE_MEMORY>>>
{candidate_memory}
<<<END_CANDIDATE_MEMORY>>>
Generate exactly three plausible future user
queries:,→
one relevant, one irrelevant, and one risk
probe.,→
B.2 Probe Validation and Repair
A separate probe auditor checks the generated
queries without making an admission decision. It
verifies whether the relevant probe provides a non-
redundant opportunity for memory use, whether
the irrelevant probe is substantively memory-
independent, whether the risk probe contains an
observable conflict or scope change, and whether
the probe set is free of memory or benchmark leak-
age.
When validation fails, the semantic audit is re-
turned to the generator. Already valid probes are
preserved when possible, while invalid roles are
regenerated. If full-set regeneration remains unsuc-
cessful, ConMem repairs the failed probe individu-
ally.
Historical Context:
<<<HISTORICAL_CONTEXT>>>
{historical_context}
<<<END_HISTORICAL_CONTEXT>>>
Candidate Memory:
<<<CANDIDATE_MEMORY>>>
{candidate_memory}
<<<END_CANDIDATE_MEMORY>>>
Role to repair:
{probe_type}
Current probe set:
<<<CURRENT_PROBES>>>
{current_probes}
<<<END_CURRENT_PROBES>>>
Semantic audit:
<<<SEMANTIC_AUDIT>>>
{semantic_audit}
<<<END_SEMANTIC_AUDIT>>>
Generate a replacement only for the requested
role.,→
The replacement should correct the semantic
failure,→
rather than merely paraphrase the previous
query.,→
If targeted repair still fails, the generator recon-
structs a fresh three-probe set using the same role
definitions.
B.3 Counterfactual Response Generation
The control and treatment branches use the same
response instruction. The assistant is asked to an-
swer the current request naturally and accurately,
to use optional user-specific information only when
relevant, and to prioritize the current request over
historical information.
The control branch receives only the future
query:
Current User Query:
<<<CURRENT_QUERY>>>
{query}
<<<END_CURRENT_QUERY>>>
Answer the current request.
The treatment branch additionally receives the
candidate memory:
Optional User-Specific Information:
<<<USER_INFORMATION>>>
{candidate_memory}
<<<END_USER_INFORMATION>>>
13

Current User Query:
<<<CURRENT_QUERY>>>
{query}
<<<END_CURRENT_QUERY>>>
Answer the current request.
Thus, the two response-generation conditions
differ only in whether the candidate memory is
available.
B.4 Blind Response-Quality Evaluation
The blind quality judge receives the historical con-
text, future query, and two responses, but does not
observe the candidate memory or know which re-
sponse corresponds to the treatment condition. It
evaluates correctness, relevance, appropriateness,
and helpfulness, while treating the current query
as the strongest evidence of present intent and con-
straints.
Historical Context:
<<<HISTORICAL_CONTEXT>>>
{historical_context}
<<<END_HISTORICAL_CONTEXT>>>
Future User Query:
<<<CURRENT_QUERY>>>
{query}
<<<END_CURRENT_QUERY>>>
Response A:
<<<RESPONSE_A>>>
{response_a}
<<<END_RESPONSE_A>>>
Response B:
<<<RESPONSE_B>>>
{response_b}
<<<END_RESPONSE_B>>>
Which response better serves this future
interaction?,→
Return A, B, or TIE with a concise
explanation.,→
B.5 Memory-Attribution Audit
The attribution auditor observes the historical con-
text, candidate memory, future query, control re-
sponse, and treatment response. It does not com-
pare response quality. Instead, it determines
whether the candidate memory was substantively
used, whether it materially changed the treatment
response, and whether the resulting personalization
isutility,unnecessary,neutral, orrisk.
The auditor labels a change asutilitywhen it is
relevant, supported by the historical context, and
appropriately scoped.Unnecessarydenotes mild
but irrelevant personalization.Riskcovers unsup-
ported, misattributed, over-generalized, privacy-
invasive, or conflicting memory use. If the memory
is not materially used or does not change the re-
sponse, the effect isneutral.
Historical Context:
<<<HISTORICAL_CONTEXT>>>
{historical_context}
<<<END_HISTORICAL_CONTEXT>>>
Candidate Memory:
<<<CANDIDATE_MEMORY>>>
{candidate_memory}
<<<END_CANDIDATE_MEMORY>>>
Future User Query:
<<<CURRENT_QUERY>>>
{query}
<<<END_CURRENT_QUERY>>>
Control Response:
<<<CONTROL_RESPONSE>>>
{control_response}
<<<END_CONTROL_RESPONSE>>>
Treatment Response:
<<<TREATMENT_RESPONSE>>>
{treatment_response}
<<<END_TREATMENT_RESPONSE>>>
Determine whether the Candidate Memory was
used,,→
whether it materially changed the treatment
response,,→
and whether the resulting personalization is
utility, unnecessary, neutral, or risk.
The auditor is explicitly instructed not to infer
staleness merely because information could have
changed. A risk judgment requires observable con-
tradictory, updated, superseding, or otherwise inap-
propriate use.
B.6 Zero-Score Admission Tie-Break
The tie-break judge is invoked only when the aggre-
gate CMTE score is zero. It receives the candidate
memory, historical context, and raw counterfactual
evidence, but does not receive the hand-specified
CMTE weights or benchmark labels.
Candidate Memory:
<<<CANDIDATE_MEMORY>>>
{candidate_memory}
<<<END_CANDIDATE_MEMORY>>>
Historical Context:
<<<HISTORICAL_CONTEXT>>>
{historical_context}
<<<END_HISTORICAL_CONTEXT>>>
Raw Counterfactual Evidence:
<<<COUNTERFACTUAL_EVIDENCE>>>
{counterfactual_evidence}
14

<<<END_COUNTERFACTUAL_EVIDENCE>>>
The aggregate CMTE score is exactly zero and
is therefore inconclusive. Make the STORE
or DO_NOT_STORE judgment from the evidence
above only.
,→
,→
,→
The judge favors STOREwhen the candidate
is sufficiently supported, appropriately attributed,
and potentially reusable. It favors DO-NOT-STORE
when the candidate is unsupported, misattributed,
materially over-generalized, contradicted by con-
text, or otherwise inappropriate to retain.
B.7 Reason Classification
After the admission outcome is fixed, ConMem
assigns a structured reason type for interpretation
and error analysis. This stage is post-hoc and does
not modify either the CMTE score or the admission
prediction.
For a STOREdecision, the reason type is
directly_relevant. For a DO-NOT-STOREdeci-
sion, the classifier receives the candidate memory,
historical context, finalized admission prediction,
and admission explanation:
You classify why this memory should NOT be
stored.,→
Candidate Memory:
{candidate_memory}
Historical Context:
{historical_context}
CMTE Admission Prediction:
{prediction}
Admission Explanation:
{admission_reason}
Return:
- reason_type
- confidence
- a short explanation
Do not change the admission decision.
The allowed rejection reasons are
context_misapplication, memory_omission,
granularity_mismatch, over_inference,
stale_memory_use, privacy_refusal,
privacy_overuse, attribution_confusion,
identity_mis_inference,
incomplete_memory_use, and
false_memory_use.
C Efficiency Analysis
We analyze the computational efficiency of Con-
Mem on the 1,079 instances of the primary bench-
mark. Unless otherwise stated, the reported latency
corresponds to the elapsed time of successful API
requests. Failed attempts and retry backoff time
are not included in the recorded latency. We report
only the calls required by the primary ConMem set-
ting and exclude additional calls performed solely
for parameter-sensitivity analysis.
API Calls.The standard execution path requires
14 model calls per candidate memory: one call
for future-probe generation, one for probe vali-
dation, six for generating the control and treat-
ment responses to the three probes, three for blind
response-quality evaluation, and three for memory-
attribution auditing. A zero CMTE score intro-
duces one additional tie-break call. In the primary
evaluation, 199 of 1,079 cases (18.44%) invoke this
tie-break.
Probe validation can introduce additional calls
when an initially generated probe set fails semantic
validation. Across the full benchmark, ConMem
performs 15,430 model-stage calls, corresponding
to an average of 14.30 calls per case. Of these, 125
calls are additional probe-generation, validation, or
repair calls beyond the standard execution path.
Latency.Table 6 reports latency statistics for
each component. Response generation takes ap-
proximately 21 seconds per call on average for
both the control and treatment branches. The at-
tribution auditor is the most expensive repeatedly
invoked component, with a mean latency of 26.85
seconds and a 95th-percentile latency of 85.76 sec-
onds. Probe validation also exhibits a relatively
long tail, with a 95th-percentile latency of 104.52
seconds.
The mean summed API latency is 347.64 sec-
onds per case, with a median of 325.44 seconds
and a 95th percentile of 577.46 seconds. These val-
ues represent the sum of component-level request
latencies rather than the wall-clock duration of the
complete experiment. In our implementation, up
to 16 cases are processed concurrently; therefore,
summed per-case latency should not be interpreted
as total experimental runtime.
Probe-Generation Overhead.Probe generation
is stable for most cases. A total of 1,044 cases
(96.76%) pass probe generation and semantic val-
idation in the first round. Overall, 1,074 cases
15

Table 6: Latency statistics of ConMem on the primary
benchmark. All latency values are in seconds. “Per-case”
denotes the sum of recorded API latencies required to
evaluate one candidate memory.
Stage Calls Mean Median P95
Probe generation 1,129 26.76 25.19 41.63
Probe audit 1,139 40.94 31.93 104.52
Probe repair 15 17.00 15.96 23.49
Control response 3,237 21.14 15.63 54.46
Treatment response 3,237 21.72 16.88 53.95
Quality judge 3,237 20.31 18.72 36.87
Attribution auditor 3,237 26.85 15.94 85.76
Tie-break judge 199 33.29 22.43 94.43
Per-case aggregate 1,079 347.64 325.44 577.46
(99.54%) are resolved through ordinary full-set gen-
eration or regeneration without entering targeted
repair. Only four cases require targeted role repair,
and one case requires fresh rescue synthesis.
Retry Behavior.Among the 15,430 model-stage
calls, 15,334 (99.38%) succeed on the first API
attempt. Only 96 calls require at least one retry.
The mean number of API attempts per model-stage
call is 1.009, and the maximum observed number
of attempts is five. Thus, transient API failures
contribute little additional invocation overhead in
the reported experiment.
These measurements reflect the API environ-
ment used in our experiments and should therefore
be interpreted as implementation-level efficiency
measurements rather than hardware-normalized in-
ference benchmarks. Token usage was not logged
during the original experiment and is consequently
not reported.
D Backbone Robustness
We further evaluate ConMem using DeepSeek-V4-
Flash and compare it with GPT-5.6-sol on the same
1,079 candidate memories. Both backbones use
three future-probe types, identical ConMem scor-
ing coefficients, and the same score-first admission
rule. Each backbone independently generates and
evaluates its probes, allowing us to examine the
end-to-end sensitivity to model selection.
Admission Performance.Table 7 reports ad-
mission performance across the two backbones.
GPT-5.6-sol achieves higher accuracy (77.85% vs.
76.83%), balanced accuracy (70.93% vs. 67.76%),
and Macro-F1 (71.54% vs. 68.89%). The dif-
ference is mainly reflected in Do-Not-Store re-
call (55.33% vs. 47.33%), whereas DeepSeek-V4-
Flash achieves slightly higher Store recall (88.19%
vs. 86.52%).
Table 7: ConMem admission performance across LLM
backbones. All values are percentages except counts.
Metric GPT-5.6 DeepSeek-V4-Flash
Accuracy 77.85 76.83
Balanced Acc. 70.93 67.76
Macro-F1 71.54 68.89
Store Precision 83.42 81.30
Store Recall 86.52 88.19
Store F1 84.94 84.61
DNS Precision 61.25 60.68
DNS Recall 55.33 47.33
DNS F1 58.14 53.18
Zero-score cases 458 193
Zero-score rate 42.45 17.89
The frequency of zero-score cases also dif-
fers substantially: 42.45% for GPT-5.6-sol versus
17.89% for DeepSeek-V4-Flash. Thus, the fre-
quency of inconclusive counterfactual scores de-
pends on the backbone, although fewer zero-score
cases do not necessarily imply better admission
performance.
Parameter Sensitivity.We examine 27 pre-
specified combinations of three CMTE coef-
ficients: the irrelevant-probe mild-use penalty
{0.25,0.5,0.75} , the risk-probe safe-utility gain
{0,0.25,0.5} , and the risk-probe harm penalty
{1.0,1.5,2.0} . The primary setting remains fixed
at(0.5,0.5,1.5).
As shown in Table 8, GPT-5.6-sol achieves
77.85–79.43% accuracy and 71.54–72.98% Macro-
F1 across these settings, compared with 76.65–
77.94% accuracy and 68.72–69.77% Macro-F1 for
DeepSeek-V4-Flash. Both backbones exhibit rela-
tively limited variation within the tested coefficient
ranges. These results characterize parameter sensi-
tivity rather than select an alternative configuration.
16

Table 8: Performance ranges across 27 CMTE scoring
settings. All values are percentages.
Metric GPT-5.6 DeepSeek-V4-Flash
Accuracy 77.85–79.43 76.65–77.94
Balanced Acc. 70.93–71.92 67.63–68.33
Macro-F1 71.54–72.98 68.72–69.77
Store Recall 86.52–88.83 87.93–89.99
DNS Recall 54.67–55.67 46.67–47.33
Zero-score Rate 42.45–45.41 17.79–20.67
17
