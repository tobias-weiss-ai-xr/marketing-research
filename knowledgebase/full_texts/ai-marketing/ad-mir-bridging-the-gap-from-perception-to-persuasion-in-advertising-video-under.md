---
title: 'AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via
  Structured Reasoning'
url: https://arxiv.org/abs/2602.07625
category: ai-marketing
subcategory: empirical
date: 2026-02
venue: ''
authors:
- Binxiao Xu
- Junyu Feng
- Xiaopeng Lin
- Haodong Li
- Zhiyuan Feng
source: arxiv
pdf_url: https://arxiv.org/pdf/2602.07625
pages: 18
chars: 64542
fetched_at: '2026-11-08T13:12:36+00:00'
kb_version: 1
---

# AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video
Understanding via Structured Reasoning
Binxiao Xu 1 2 * Junyu Feng 2 * Xiaopeng Lin 2 Haodong Li 3 Zhiyuan Feng 4 Bohan Zeng 1
Shaolin Lu 1 † Ming Lu 5 Qi She 6 Wentao Zhang 1†
Abstract
Multimodal understanding of advertising videos
is essential for interpreting the intricate relation-
ship between visual storytelling and abstract per-
suasion strategies. However, despite excelling
at general search, existing agents often struggle
to bridge the cognitive gap between pixel-level
perception and high-level marketing logic. To
address this challenge, we introduceAD-MIR,
a framework designed to decode advertising in-
tent via a two-stage architecture. First, in the
Structure-Aware Memory Constructionphase,
the system converts raw video into a structured
database by integrating semantic retrieval with ex-
act keyword matching. This approach prioritizes
fine-grained brand details (e.g., logos, on-screen
text) while dynamically filtering out irrelevant
background noise to isolate key protagonists. Sec-
ond, theStructured Reasoning Agentmimics
a marketing expert through an iterative inquiry
loop, decomposing the narrative to deduce im-
plicit persuasion tactics. Crucially, it employs an
evidence-based self-correction mechanism that
rigorously validates these insights against spe-
cific video frames, automatically backtracking
when visual support is lacking. Evaluation on the
AdsQA benchmark demonstrates that AD-MIR
achieves state-of-the-art performance, surpassing
the strongest general-purpose agent, DVD, by
1.8% in strict and 9.5% in relaxed accuracy. These
results underscore that effective advertising under-
standing demands explicitly grounding abstract
marketing strategies in pixel-level evidence. The
code is available at https://github.com/
Little-Fridge/AD-MIR.
*Equal contribution † Project leader † Corresponding author
1Peking University, Beijing, China 2Xi’an Jiaotong University,
Xi’an, China 3South China University of Technology, Guangzhou,
China 4Tsinghua University, Beijing, China 5Intel, Beijing, China
6ByteDance, Beijing, China. Correspondence to: Wentao Zhang
<wentao.zhang@pku.edu.cn>.
Preprint. February 10, 2026.
1. Introduction
The research paradigm for video understanding is shifting
from entity-centric perception to intent-oriented cognition,
as Lin et al. (2024); Zhang et al. (2025); Fu et al. (2025) pro-
gressively move from object-centric recognition to higher-
level reasoning over long-form video content. Despite the
success of Large Multimodal Models (LMMs) in general-
izing across objective physical descriptions, a substantial
cognitive disparity remains when processing subjective and
strategic content, even as Liu et al. (2023); Zhang et al.
(2024a) demonstrate strong generalization under instruction-
tuned and long-context settings. Advertising videos serve as
an adversarial benchmark for this limitation. Unlike objec-
tive recordings, ads are engineered semiotic systems (Hus-
sain et al., 2017). In such non-linear narratives, cinematic
techniques such as lighting manipulation and rhythmic edit-
ing function not merely as visual signals, but as vehicles for
abstract persuasion logic. Therefore, bridging this semantic
divide between low-level visual facts (e.g., a scene fading
to black) and high-level abstract intents (e.g., creating a
sense of suppression to trigger pain points) is essential for
effective advertising understanding.
Table 1.Feature comparison with existing paradigms.Unlike
general agents (e.g., DVD) limited to generic retrieval, or RL-
optimized baselines (ReAd-R) relying on implicit outcome fitting,
AD-MIR explicitly integrates expert modules to decode persuasion
strategies (”why”) and employs rigorous visual verification to
minimize hallucinations.
Perception Strategy Cognition Reliability
Method Visual Grounding Fine-grained Detail Causal Reasoning Persuasion Decoding Visual Verification
End-to-End LMMs✗ ✓ ✗ ✗ ✗
General Video Agents (DVD)✓ ✓ ✗ ✗ ✗
ReAd-R (AdsQA Baseline)✓ ✓ ✓ ✗ ✗
AD-MIR (Ours) ✓ ✓ ✓ ✓ ✓
Current video understanding models face significant hurdles
in the domain of advertising (Hussain et al., 2017). While
end-to-end LMMs excel at describing general visual content
(Liu et al., 2023; Lin et al., 2024), they struggle with two
main limitations: limited memory and logic hallucinations
(Zhang et al., 2024a; Guan et al., 2024; Fu et al., 2025). First,
constrained by context windows, these models often lose
track of details across long narratives. Second, and more
1
arXiv:2602.07625v1  [cs.CV]  7 Feb 2026

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
AIAgent
Thinking
“Need narrative
structure first.”
User Query: “How is
Technology integrated
with work?”
1.INPUT & PLANNING 2. EXPERT CAUSAL NARRATIVE
python
Call: frame_inspect_tool
Query: “close-up of phone
screen with Sprint button.”
3. VISUAL VERIFICATION
Verified at 00:04
OCRMatch
“Sprint my order”
00:0000:02
00:03
00:04
00:05
00:06
Expert Tool
Context:
Manual Labor
Tradesman in
low-tech setting.
Action:
Digital Trigger
Interacts with
“sprint” app.
Outcome:
Physical Speed
App bridges need
to rapid delivery.
CausalLogicSummary
The app acts as the direct causal mechanism.
Video Strip
Global Context
Clip-Level Events
Fine-Grained OCR
Verification Matrix
1
2
3
Narrative Claim Visual Confidence
Verified
Verified
Verified
Problem: Urgent Repair
Solution: Digital Order
Result: Fast Delivery
Final Output The ad shows professionals at a construction site placing orders with a single click through an app.
python
Call: communication_expert_tool
Args: query_focus=“integration
of technology.”
4. FINAL SYNTHESIS
Mode: “literal”
Figure 1.Illustrative walkthrough of AD-MIR’s reasoning pipeline on an AdsQA example.Unlike general agents that focus on
retrieval, AD-MIR bridges the cognitive gap by first constructing a high-level causal narrative via a communication expert (Phase 1-2), then
performing targeted frame inspection to verify precise visual details (Phase 3), and finally synthesizing a visually grounded explanation
that links the expert narrative to pixel-level evidence (Phase 4).
critically, lacking a mechanism to decode persuasive intent,
they tend to hallucinate when explaining strategic motiva-
tions, often fabricating reasons that defy basic advertising
logic (Hussain et al., 2017; Guan et al., 2024).
On the other hand, tool-augmented agents, represented by
the Deep Video Discovery (DVD) Agent (Zhang et al.,
2025), have successfully established a baseline forvisual
groundingby precisely locking onto the timestamps of
events. However, a critical distinction exists between re-
trieving”what happened”and reasoning”why it happened. ”
While DVD demonstrates acuity in locating visual content,
it lacks the cognitive capability to decode the underlying
marketing psychology(e.g., identifying rhetorical devices,
emotional appeals, and symbolic metaphors). Even the re-
cent ReAd-R framework (Long et al., 2025), which employs
reinforcement learning to enhance retrieval-QA alignment,
remains limited by implicit data fitting. Without explicit
structural constraints for persuasion analysis, such models
struggle to distinguish between superficial visual correla-
tions and deep strategic causation (e.g., recognizing a phone
not merely as an object, but as a solution to a labor prob-
lem). Consequently, when nuanced strategic inquiries arise,
standard video agents and RL-optimized baselines can only
draw shallow associations, resulting in a logical fracture
between visual perception and intent understanding. Ta-
ble 1 summarizes the capability gaps between these existing
paradigms and our proposed approach.
In response to these challenges, we proposeAD-MIR
(ADvertising Multimodal Intent Reasoning), a multimodal
agent framework tailored for advertising videos. Rather than
relying on single-shot retrieval or black-box inference, AD-
MIR is designed to close the cognitive gap via a two-stage
architecture that extends the standard reasoning-and-acting
paradigm (Yao et al., 2022). As illustrated in Figure 1,
the framework operates by mirroring how a human analyst
works: first, constructing a structured memory of the nar-
rative, and second, employing an iterative inquiry loop to
align high-level hypotheses with precise visual anchors.
The first phase isStructure-Aware Memory Construction,
where the system decouples raw video streams into visual,
textual, and audio modalities to construct a hierarchical in-
dex. This allows the model to anchor cues often missed
by general retrieval. The second phase involves theStruc-
tured Reasoning Agent, which employs an explicit iterative
inquiry-refinement mechanism. Instead of a generic loop,
this mechanism intelligently selects the most suitable tools
based on the query’s nature. For factual queries, it routes to
2

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
perception tools; for strategic queries, it invokes specialized
communication expert modules grounded in marketing psy-
chology (e.g., analyzing persuasion, rhetoric, and emotional
arcs). This hierarchical synergy enables AD-MIR to capture
implicit logical associations, such as linking “a plumber
under a sink” to “a speeding motorbike” by reconstructing
discrete visual symbols into a coherent marketing narrative.
Our main contributions are summarized as follows:
1. A Multimodal Reasoning Agent Framework Tai-
lored for Advertising.We present AD-MIR, a novel
agent designed to bridge the gap between visual percep-
tion and intent understanding. By employing an itera-
tive inquiry-refinement mechanism that aligns expert-
derived marketing insights with rigorous visual ver-
ification, it effectively decodes complex persuasion
tactics that general agents miss.
2. Hierarchical Perception-Inference Toolchain.We
introduce a query-driven architecture that selectively
routes inquiries between perception tools for factual
grounding and specialized expert modules grounded
in marketing psychology. This specialized design en-
ables the precise interpretation of symbolic imagery
and emotional cues, surpassing the literal description
capabilities of standard multimodal systems.
3. Visual Verification for Grounded Reasoning.We
introduce a mechanism that validates high-level rea-
soning against pixel-level evidence, ensuring interpre-
tations are derived strictly from video frames rather
than linguistic priors. This cross-modal alignment
bridges abstract marketing concepts with concrete vi-
sual signals, significantly enhancing the reliability and
interpretability of persuasion analysis.
2. Method
In this section, we present the AD-MIR framework. As
illustrated in Figure 2, AD-MIR utilizes an agentic reason-
ing architecture that couples a ReAct-style controller with
a shared multimodal database M and a suite of domain-
specific interaction tools. This design effectively bridges the
semantic gap between pixel-level perception and high-level
marketing intent. The workflow proceeds in two synergis-
tic stages: (1)Structure-Aware Memory Construction,
where raw video streams are decoupled into a discrete, in-
dexable multimodal database to isolate key narrative ele-
ments; and (2)Iterative Intent Reasoning, where a domain-
adaptive agent orchestrates perception primitives and intent
experts via a “Think-Act-Observe” loop, aligning visual
evidence with logically grounded marketing inference.
2.1. Problem Definition
We formalize the advertising video understanding task as a
Partially Observable Markov Decision Process (POMDP),
defined by the tuple (S,A,T,R,Ω,O) (Wu et al., 2019).
Due to the non-linear and metaphorical nature of advertising
narratives, the agent cannot perceive the full video V in a
single step, rendering the state space S partially observable.
Definition 2.1.The state st ∈ Sat time t is defined as the
union of the multimodal database M, the context-anchored
subject registryS reg, and the interaction historyH t−1.
Given a natural language query Q, the agent receives an
environmental observation ot ∈Ω . It then generates a
Chain-of-Thought (CoT) reasoning step zt by leveraging
the historyH t−1 ={o 0, a0, . . . , at−1, zt−1}.
Proposition 2.2.The agent selects the next action at ∈ A
according to a domain-adaptive policy π(at|Ht−1, ot; Θ),
where Θ represents the frozen parameters of a Large Multi-
modal Model. The policy is implemented via prompt-based
in-context learning rather than gradient-based updates.
The system aims to generate an answer A∗ that maximizes
semantic consistency and evidence-based grounding:
A∗ = arg max
A
P(A|V, Q,Sreg; Θ)(1)
2.2. Structure-Aware Memory Construction
To effectively mitigate the computational VRAM bottle-
necks inherent in long-video reasoning and simultaneously
ensure the granular precision of evidence backtracking, we
employ a dedicated offline pipeline to decouple the continu-
ous raw video stream into a structured multimodal database.
This systematic preprocessing workflow is primarily under-
pinned by two pivotal mechanisms:
2.2.1. HYBRIDSEMANTIC-LEXICALINDEXING
We discretize the raw video stream into a set of temporal
clips C={c i}N i=1. To construct a comprehensive seman-
tic index, for each clip ci, we utilize a VLM to generate
fine-grained visual narrative descriptions d(i) vis and integrate
the Whisper model to extract timestamped audio transcripts
d(i) aud. Addressing the precision loss inherent in single dense
vector retrieval when handling specific entities (e.g., brand
names, prices), we propose a hybrid semantic-lexical scor-
ing strategy. Given a query Q, the relevance score S(Q, ci)
for clip ci is formalized as a weighted linear combination of
dense semantic similarity and exact keyword matching:
S(Q, ci) = cos(ϕ(Q), ϕ(d(i) vis ⊕d (i) aud))| {z }
Semantic
+β· K(Q, d(i) vis ⊕d (i) aud)| {z }
Lexical
(2)
where ϕ(·) denotes the semantic text embedding function,
and ⊕ represents the concatenation operation of multimodal
3

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
Input & Contex
to ReAct
Controller
Iterative ReAct Loop withThought,
Action, Observation, History
Action
invoke toolReasoning
Observation
results from
tools
Raw ReAct
Answer
ReAct uses
memory of
previous steps
Preprocessing
into multimodal
assets
(A) Input & Context (B) The ReAct Controller (C) Toolset for Video Interaction
(D) Multimodal Data Base Layer
Unified multimodal data layer for all tools
Initial
context
Global Browse Tool
(Structural Sampling)
Communication Expert Tool
(Two-step Reasoning)
Hook
(Beginning)
Sparse
Samples(Middle)
Payoff/CTA
（End）
Global Story Understandina
Forced read of beginning and end;
sparse sampling in the middle
Action: use
Global Browse
Observation: global
narrative summary
Reason over facts using
marketing psychology
Step 2: Inference (Marketing Strategy)
Step 1: Perception (Objective Logging)
Observation: deep strategy explanatior
Clip Search Tool
(Dual-path Retrieval)
Frame Inspect Tool
(Multimodal Micro-Observation)
Long video
(E) Output: Refinement (Answer Distillation)
Raw ReAct Answer
Lightweight
LLM(GPT-4o-mini)
Refined Answer
(GPT-4o-mini)
Information-preserving compressionl
Compress length, keepntities,actions,
negations remove redundancy
Raw ReAct
Answer
Keyword
Matching
Query
“sad”
“Nike”
Vector
Search
 Selected
Clips
Exact kerd and
text match
understand
abstract concepts
person holding
Natural language question
about the ad
Video
Ad Video File
Pre-computed
Summary
(Global Browse)
LLM
(GPT-4o)
Thought
“I need to checkthe
text onscreen first..”
User Query
History
past Thoughts,Actions,
Observations
on-screen text
Smile
mobile phone
Lifetyle marketing
Fear appeal
Social Proof
Shared data
access
Visual Assets
Extracted video
frames for VLM
Textual Assets
ASR transcripts and
subtitles for LLM
Semantic Index
Vector embeddinos
of text and images
Final
concise
answer
to user
Time
Range
High-frequency
dense sampling
Sparse
keyframe sampling
Visual
Evidence
Figure 2.The overall architecture of AD-MIR.The framework comprises five synergistic components: (A) Input & Context construction
for multi-modal preprocessing; (B) a ReAct Controller for iterative reasoning; (C) a Hierarchical Toolset featuring global browsing,
communication experts, and fine-grained inspection; (D) a Unified Multimodal Database serving as shared memory; and (E) an Answer
Refinement stage to ensure concise, evidence-based output.
text streams. K(·) is a lexical scoring function based on
keyword hit rate and exact match enhancement, and β is a
hyperparameter regulating the relative lexical weight. This
formulation ensures that the agent possesses dual perception
capabilities: the dense vector component captures abstract
visual concepts (e.g., “a warm dinner”), while the sparse
retrieval component precisely localizes specific explicit mar-
keting clues (e.g., “Nike” or “50% OFF”).
2.2.2. CONTEXT-ANCHOREDSUBJECTREGISTRY
In complex advertising scenarios, the frame is often crowded
with background characters, which distracts the agent from
the main protagonists. To mitigate this noise, we implement
a two-step register-and-filter mechanism.
First, during the offline memory construction, we utilize
GPT-4o to extract a static subject registry Sreg ={s j}M j=1.
Unlike simple object detection, the model generates a rich
semantic profile dj for each distinct character (e.g., “A
middle-aged doctor wearing a stethoscope and looking anx-
ious”), rather than just a bounding box label.
Second, during inference, we apply a dynamic activation
strategy to decide which characters are relevant. User
queries often suffer from referential ambiguity (e.g., “What
isheholding?”), where the pronoun’s target is unclear
without context. To resolve this, we construct an en-
hanced semantic anchor Aanchor—a composite represen-
tation that fuses the raw query Q with the global narra-
tive summary Cglob obtained from the global browse tool
(Aanchor =Q⊕C glob). This anchor serves as a contextual-
ized reference point in the vector space, ensuring the search
is driven by the full narrative intent rather than ambiguous
keywords. We then compute the relevance scoreρj between
this anchor and each character’s profile:
Sactive =TopK({s j ∈ Sreg |ρ j = cos(ϕ(dj), ϕ(Aanchor))}, k) (3)
By filtering based on semantic similarityρj, this mechanism
acts as a cognitive spotlight: it activates relevant characters
(e.g., the ”doctor”) while suppressing background noise,
ensuring the reasoning chain focuses solely on evidence
pertinent to the narrative intent.
4

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
Table 2.Action Spaces for Intent Reasoning.The framework
stratifies the action space into perceptual grounding tools and intent
analysis experts to bridge the semantic gap. Specific implementa-
tion parameters (e.g., sampling rates) are detailed in Appendix B.2.
Action Function & Parameters
GLOBALBROWSEInput:DatabaseM, QueryQ init
Retrieves pre-computed narrative logs
to synthesize a structured global
summaryC glob.
CLIPSEARCHInput:DatabaseM, Query ˆQ
Performs hybrid retrieval with Temporal
Fusion to merge continuous event
segments.
FRAMEINSPECTInput:QueryQ vis, Range[t s, te],
Modem
Variable-density visual inspection: mlit
(dense) for factual details;m sem
(sparse) for stylistic elements.
COMM. EXPERTInput:Focus ˆQf oc, Range[t s, te]
Executes high-density grid inference to
resolve long-term dependencies and
decode persuasion logic.
FINISHInput:ResponseA, EvidenceE
Triggers VERIFYGROUNDING; returns
A∗ if verified, otherwise initiates a
forced backtrack.
2.3. Structured Reasoning Agent
At the core of AD-MIR lies a controller designed to emulate
the cognitive processes of marketing experts by dynamically
orchestrating action primitives.
2.3.1. PROMPT-GUIDEDREACTCONTROLLER.
We instantiate the LMM as the central controller πΘ. Dis-
tinct from fine-tuned video agents, our system utilizes frozen
parameters Θ (e.g., GPT-4o) governed by structured in-
context learning. Instead of relying on implicit priors, the
system prompt injects explicit behavioral constraints, man-
dating that the agent prioritizes retrieved visual evidence
over internal parametric knowledge when interpreting ab-
stract concepts. The execution logic follows the ”Think-Act-
Observe” cycle formalized in Algorithm 1.
At each stept, the agent generates a thoughtzt and selects an
action at conditioned on the interaction history Ht−1. The
controller is equipped with a self-correction mechanism: if
the generated answer fails the visual grounding verification
check (as detailed in Section 2.4), the system triggers a
forced trajectory backtrack, appending a “Weak Evidence”
constraint toH t to guide the policy toward re-retrieval.
Algorithm 1AD-MIR Inference Process
Input:Video StreamV, QueryQ
Output:Refined answerA ∗
Stage I: Structure-Aware Memory Construction
M,S reg ←BUILDDB(V){1 FPS, Whisper, GPT-4o}
Stage II: Iterative Intent Reasoning
Cglob,ASR←GLOBALBROWSE(M, Q)
H0 ← {Q, Cglob,S reg}
t←0
whilet < Tmax do
zt, at ←π Θ(Ht−1)
ifa t =FINISH(A,E)then
Wanchors ←EXTRACTENTITIES(E)
ifVERIFYGROUNDING(A,E,W anchors)then
returnVISUALANCHORREFINE(A)
end if
Ht ← Ht−1 ∪ {”Reject: Weak Evidence”}
t←t+ 1
continue
end if
ifa t ∈ Apercept then
ot ←EXECUTE(a t,M)
else
ifa t =COMMEXPERT( ˆQf oc,[t s, te])then
Lvis ←GRIDSAMPLE(M,[t s, te])
ot ←REASON(L vis,ASR, Cglob, ˆQf oc)
end if
end if
Ht ← Ht−1 ∪ {(zt, at, ot)}
t←t+ 1
end while
returnFAILURE
2.3.2. SEARCH-CENTRICTOOLSETCONSTRUCTION.
Building upon the structured database M, we categorize
the action space A into two distinct groups:information
retrieval toolsfor locating visual evidence andreasoning
modulesfor decoding narrative logic. To ensure determinis-
tic interaction between the agent and the environment, we
define explicit functional interfaces for each tool, as com-
prehensively formalized in Table 2. The implementation
details of these tools are elaborated below.
Tool: Global Browse.Serving as the strategic initializer
for the reasoning trajectory, this tool constructs a holistic
narrative framework Cglob to ground subsequent actions. In
contrast to conventional methods relying on stochastic frame
sampling that frequently fractures temporal continuity, this
module exploits the pre-computed textual modalities within
M. Specifically, it aggregates the complete chronological
sequence of visual captions and ASR transcripts into a uni-
fied context window. By processing this high-density textual
stream, the LMM synthesizes a structured summary that not
5

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
only classifies the macro-genre (e.g., emotional narrative
vs. direct promotion) but also extracts pivotal entities. This
global prior effectively prunes the search space by imposing
essential semantic constraints, thereby preventing the agent
from hallucinating in unrelated contexts.
Tool: Clip Search.To secure narrative continuity at the
event level, this tool facilitates medium-granularity retrieval,
addressing the issue of temporal fragmentation common
in standard top-k retrieval. By executing a synthetic query
ˆQ against the hybrid index, it identifies candidate intervals
which are subsequently refined via a Temporal Fusion Al-
gorithm. Specifically, disjointed clips exhibiting minimal
temporal gaps (less than 3 seconds) or high semantic affinity
(>0.8 ) are coalesced into unified event blocks. This mech-
anism effectively reconstructs fragmented retrieval results
into continuous event units, ensuring that the agent perceives
complete long-duration actions rather than isolated snippets.
Tool: Frame Inspect.Functioning as the system’s visual
microscope, this tool bridges the granularity gap between
abstract semantics and raw pixel data by modulating its
sampling strategy according to the analysis modem. Specif-
ically, the literal mode (mlit) enforces high-frequency dense
sampling to rigorously extract observable axioms, such as
OCR text and object counts, which are essential for factual
verification. In contrast, the semantic mode (msem) adopts
a sparse keyframe strategy to interpret stylistic elements like
lighting, color temperature, and metaphorical imagery. This
dual-path architecture allows the agent to dynamically alter-
nate between forensic precision and aesthetic appreciation
based on the specific requirements of the query.
Tool: Communication Expert.Designed to bridge the gap
between concrete visual signals and abstract persuasive in-
tent, this tool introduces a Spatio-Temporal Grid Projection
mechanism. Unlike conventional sequential processing that
suffers from context forgetting in long videos, this module
transforms the temporal dimension into a unified spatial
representation by arranging N= 64 sampled frames into
a high-resolution composite visual grid. This projection
enables the LMM to perform parallel visual reasoning over
the entire narrative arc simultaneously. Furthermore, to mit-
igate the hallucinations common in abstract deduction, we
implement a Text-Constrained Symbolic Mapping proto-
col. By fusing the visual grid with aligned ASR and global
summaries, the agent is forced to ground its high-level inter-
pretations (e.g., mapping “soaring eagle” to “freedom”) in
verifiable textual facts, thereby achieving robust persuasion
analysis without exceeding token limits.
2.4. Reasoning Reliability Mechanisms
We embed two control mechanisms within the execution
loop to enforce a robust and coherent reasoning trajectory.
Macro-to-Micro Evidence Zooming.We enforce a
hypothesis-driven cascading strategy:
Cglob
Init
− − →Intent
Search
− − − → Trel
Verify
− − − → Lvis.(4)
The agent first pre-emptively acquires the narrative con-
tour via GLOBALBROWSEto initialize the semantic con-
text. Subsequently, within the ReAct loop, it prioritizes
the COMM. EXPERTto formulate high-level persuasion
hypotheses (e.g., identifying a specific marketing strategy).
These hypotheses guide the CLIPSEARCHto narrow down
relevant temporal intervals Trel, and finally, the agent locks
onto pixel-level evidence through FRAMEINSPECTfor rig-
orous verification. This zooming mechanism prevents disori-
entation by ensuring that low-level visual search is always
directed by high-level semantic intent.
Visual Grounding Verification.To mitigate hallucinations,
we introduce a rigorous answer verification protocol. Upon
generating a candidate answer Acand, the system triggers a
grounding functionΨ:
State= Ψ(A cand,E,W anchors)(5)
where E denotes the accumulated evidence chain, and
Wanchors represents the set of visual entities extracted from
the retrieving history. The function Ψ checks whether the
key claims in Acand are supported by specific frames in
Wanchors. If visual grounding is insufficient (i.e., State=
Reject), the system mandates a forced trajectory backtrack,
appending a negative constraint to the history to guide the
agent toward alternative retrieval paths.
3. Experiments
In this section, we evaluate AD-MIR on the AdsQA bench-
mark (Long et al., 2025). Our experimental design aims to:
(1) benchmark the framework against end-to-end LMMs and
general-purpose video agents; (2) isolate the contributions
of specific architectural components via ablation studies;
and (3) analyze hyperparameter sensitivity to verify system
robustness and reproducibility.
3.1. Experimental Setup
Dataset.We evaluate AD-MIR on AdsQA, a benchmark
that focuses on deep persuasion logic and marketing intent
understanding in advertising videos. AdsQA covers 38
diverse categories and includes questions that range from
concrete factual retrieval to abstract rhetorical and audience
modelling analysis. This setting precisely matches our goal
of testing whether an agent can connect pixel-level evidence
to complex high-level persuasion intents.
Evaluation Metrics.Following the official AdsQA proto-
col, we employ an LLM-as-a-Judge framework to evaluate
6

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
Table 3.Performance comparison on the AdsQA benchmark. We report both strict and relaxed accuracy (%) across all five dimensions
(VU, ER, TE, PS, AM) and the overall average. AD-MIR, built upon Qwen2.5-VL-7B and o1, is evaluated against commercial LMMs
(o1), open-source video LVLMs, and reasoning-oriented video agents.
Model
Strict Accuracy Relaxed Accuracy
VU ER TE PS AM Overall VU ER TE PS AM Overall
Commercial Large Multimodal Model
o1(Jaech et al., 2024) 31.8 32.0 34.9 31.0 32.0 33.1 50.9 52.8 54.8 50.0 51.2 52.4
Open-sourced Video-LLMs
VideoLLaMA2-7B(Cheng et al., 2024) 4.56 7.75 7.28 6.06 7.38 6.48 21.6 29.0 28.4 22.6 27.2 25.2
LLaV A-OneVision-7B(Li et al., 2024) 11.8 11.6 16.2 13.7 15.1 14.0 35.8 39.5 43.2 36.8 41.7 39.1
LLaV A-Video-7B(Zhang et al., 2024b) 14.0 14.4 18.7 15.2 17.3 16.1 37.8 41.6 45.1 38.1 43.6 41.0
Qwen2.5-VL-7B(Bai et al., 2025) 27.6 27.1 25.7 26.3 25.0 26.2 49.8 51.6 48.8 48.5 47.2 49.0
Reasoning Agent/Models
ReAd-R(Qwen2.5-VL-7B)(Long et al., 2025) 20.4 27.9 27.2 22.1 25.5 25.0 46.2 56.2 54.6 48.2 52.6 51.5
DVD(o1)(Zhang et al., 2025) 31.1 34.0 39.8 35.9 36.6 36.3 45.0 50.9 54.8 48.5 51.5 50.5
AD-MIR(Qwen2.5-VL-7B) 31.6 34.0 31.0 29.5 27.4 30.7 52.5 55.9 53.0 50.2 50.1 52.1
AD-MIR(o1) 32.8 36.1 41.6 37.9 38.1 38.1↑1.8 56.0 59.9 63.2 58.8 60.6 60.0↑7.6
semantic alignment. The judge receives the video meta-data,
query, ground truth, and model prediction, assigning a score
s∈ {0,0.5,1.0} based on a standardized rubric (detailed
in Appendix C.4). We reportstrict accuracy(fraction of
samples with s= 1.0 ) andrelaxed accuracy( s≥0.5 )
across five task-specific dimensions: Visual Concept Un-
derstanding (VU), Emotion Recognition (ER), Theme and
Core Message Extraction (TE), Persuasion Strategy Mining
(PS), and Potential Audience Modeling (AM). These met-
rics allow for a fine-grained diagnosis of different cognitive
abilities. Crucially, to mitigate the well-known length bias
of LLM judges and ensure a fair evaluation, we integrate a
Refinement Module that strictly constrains our model’s out-
put to fewer than 30 tokens, thereby prioritizing information
density and precision over verbosity.
Baselines.We compare AD-MIR against three families of
systems, as summarized in Table 3: (i) a strong commercial
LMM (o1) used as an end-to-end zero-shot reference, (ii) re-
cent open-source video LVLMs based on LLaV A-style and
Qwen2.5-VL backbones, and (iii) reasoning-oriented video
agents, including the AdsQA-specific ReAd-R and the long-
video agent DVD. AD-MIR is instantiated on both an open-
source backbone (Qwen2.5-VL-7B) and a commercial rea-
soning model (o1), which we denote as AD-MIR(Qwen2.5-
VL-7B) and AD-MIR(o1). Further implementation details
for all baselines are provided in Appendix B.1.
3.2. Main Results
We present the comprehensive performance comparison in
Table 3. As evidenced by the data, AD-MIR establishes new
state-of-the-art benchmarks across both strict and relaxed
accuracy metrics, yielding three critical insights into the
efficacy of structured reasoning agents.
Unlocking Latent Reasoning Capabilities.Our results
demonstrate substantial performance gains over base mod-
els across both metrics. Equipped with the o1 backbone,
AD-MIR achieves a strict accuracy of38.1%(+5.0%) and
a relaxed accuracy of60.0%(+7.6%). Similarly, AD-MIR
(Qwen2.5-VL-7B) improves upon its base model by+4.5%
(strict) and+3.1%(relaxed). These consistent improve-
ments indicate that the bottleneck in complex video un-
derstanding lies less in inherent parametric knowledge and
more in the orchestration of long-horizon reasoning. By en-
forcing an explicit “Think-Act-Observe” loop, AD-MIR ef-
fectively unlocks latent deductive capabilities, bridging the
gap between raw knowledge and precise decision-making.
Bridging the Proprietary-Open Source Gap.Crucially,
our framework enables smaller open-source models to com-
pete with larger commercial systems. AD-MIR (Qwen2.5-
VL-7B) attains a relaxed accuracy of52.1%, comparable
to the commercial o1 baseline (52.4%). This suggests that
a structured agentic architecture augmented with domain-
specific tools (e.g., theCommunication Expert) can mitigate
parameter disparity, providing a resource-efficient alterna-
tive for high-level video reasoning.
Superiority Over Reasoning-Enhanced Models.AD-
MIR also surpasses reasoning-centric baselines like ReAd-
R. While ReAd-R shows strong latent reasoning (51.5%
relaxed), its strict accuracy collapses to 25.0%, highlight-
ing the difficulty of aligning reasoning with rigid output
constraints through standard optimization. Conversely,
AD-MIR (Qwen2.5-VL-7B) achieves a favorable balance
(+5.7% strict, +0.6% relaxed) without parameter updates.
This validates our training-free paradigm: instead of relying
on potentially unstable fine-tuning, AD-MIR leverages struc-
tured tool usage to guide the frozen backbone, proving that
architectural scaffolding offers a more robust mechanism
for enforcing verifiable decision-making.
7

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
(a) LexicalWeight Sensitivity  (b) Max IterationSensitivity  (c) Component Ablation
Figure 3.Ablation and sensitivity analysis ofAD-MIRon AdsQA. Subfigures (a) and (b) report strict (top) and relaxed (bottom) accuracy
on all five dimensions under different lexical weights β and maximum reasoning steps Tmax, respectively, showing that performance
is stable in a broad range and peaks around the default setting. Subfigure (c) presents component-level ablations for Hybrid Indexing,
Subject Registry, Communication Expert, and Visual Anchor, where “w/” and “w/o” denote whether the corresponding module is enabled;
the results highlight the complementary gains of structured indexing, domain expert reasoning, and visual anchor self-correction.
3.3. Ablation Study and Sensitivity Analysis
We conduct ablation and sensitivity analyses using Qwen2.5-
VL-7B to isolate component contributions and evaluate sys-
tem robustness, as summarized in Figure 3. The results
validate our architectural choices.
Sensitivity to Hyperparameters.Figure 3(a) examines
the impact of the lexical weight β in our hybrid indexing
mechanism. Performance improves significantly as β in-
creases and stabilizes across a broad range of higher values.
This trend underscores the critical role of precise lexical
matching for AdsQA, where intent often hinges on fine-
grained OCR clues (e.g., disclaimers, prices) that semantic-
only retrieval might overlook. Figure 3(b) investigates the
maximum reasoning steps Tmax. Accuracy improves with
increased reasoning budgets up to Tmax = 8, confirming
the necessity of multi-hop evidence collection for complex
narratives. Beyond this point, performance saturates and
even slightly declines, suggesting that excessive reasoning
steps yield diminishing returns and may introduce noise.
Component-wise Ablation.Figure 3(c) validates the effi-
cacy of our architectural modules by removing them one
at a time: (1)w/o Hybrid Indexing: Removing lexical
signals leads to a notable performance drop, reaffirming
that semantic retrieval alone is insufficient for capturing
exact visual text details. (2)w/o Subject Registry: The
exclusion of subject tracking degrades performance, par-
ticularly in questions involving social interactions, due to
increased interference from irrelevant background charac-
ters. (3)w/o Communication Expert: We observe the
sharpest decline in persuasion-centric dimensions (e.g., PS)
when this module is disabled, supporting our hypothesis that
explicit marketing priors are essential for decoding advertis-
ing strategies. (4)w/o Visual Anchor: The absence of the
visual anchor consistently hurts strict accuracy, indicating
that the verification mechanism is crucial for suppressing
plausible but hallucinated reasoning.
4. Conclusion
In this paper, we presented AD-MIR, a multimodal frame-
work designed to bridge the cognitive gap between pixel-
level perception and high-level persuasive intent. By syner-
gizing structure-aware memory construction with iterative
structured reasoning, AD-MIR effectively decodes complex
marketing strategies within non-linear narratives. Exten-
sive evaluations on the AdsQA benchmark demonstrate that
our approach achieves state-of-the-art performance, signifi-
cantly outperforming both end-to-end LMMs and general
video agents. These findings highlight the necessity of ex-
plicit reasoning for advertising understanding and pave the
way for next-generation agents capable of strategic analysis.
8

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
Impact Statement
This paper presents work aimed at advancing multimodal
video understanding, specifically in the domain of advertis-
ing and persuasion analysis. A primary societal benefit of
our framework, AD-MIR, is its potential to assist in con-
tent moderation and regulatory compliance by automatically
decoding implicit marketing intents and detecting mislead-
ing or non-compliant persuasive tactics. This capability
contributes to greater transparency in digital media.
References
Bai, S., Chen, K., Liu, X., Wang, J., Ge, W., Song, S., Dang,
K., Wang, P., Wang, S., Tang, J., et al. Qwen2. 5-vl
technical report.arXiv preprint arXiv:2502.13923, 2025.
Cheng, Z., Leng, S., Zhang, H., Xin, Y ., Li, X., Chen, G.,
Zhu, Y ., Zhang, W., Luo, Z., Zhao, D., et al. Videollama
2: Advancing spatial-temporal modeling and audio under-
standing in video-llms.arXiv preprint arXiv:2406.07476,
2024.
Fan, Y ., Ma, X., Wu, R., Du, Y ., Li, J., Gao, Z., and Li,
Q. Videoagent: A memory-augmented multimodal agent
for video understanding. InEuropean Conference on
Computer Vision, pp. 75–92. Springer, 2024.
Fang, X., Mao, K., Duan, H., Zhao, X., Li, Y ., Lin, D.,
and Chen, K. Mmbench-video: A long-form multi-shot
benchmark for holistic video understanding.Advances
in Neural Information Processing Systems, 37:89098–
89124, 2024.
Fu, C., Dai, Y ., Luo, Y ., Li, L., Ren, S., Zhang, R., Wang,
Z., Zhou, C., Shen, Y ., Zhang, M., et al. Video-mme:
The first-ever comprehensive evaluation benchmark of
multi-modal llms in video analysis. InProceedings of the
Computer Vision and Pattern Recognition Conference, pp.
24108–24118, 2025.
Guan, T., Liu, F., Wu, X., Xian, R., Li, Z., Liu, X., Wang, X.,
Chen, L., Huang, F., Yacoob, Y ., et al. Hallusionbench:
an advanced diagnostic suite for entangled language hal-
lucination and visual illusion in large vision-language
models. InProceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pp. 14375–
14385, 2024.
Guo, Z., Chen, X., Zhang, R., An, R., Qi, Y ., Jiang, D., Li,
X., Zhang, M., Li, H., and Heng, P.-A. Are video models
ready as zero-shot reasoners? an empirical study with the
mme-cof benchmark.arXiv preprint arXiv:2510.26802,
2025.
He, B., Li, H., Jang, Y . K., Jia, M., Cao, X., Shah, A.,
Shrivastava, A., and Lim, S.-N. Ma-lmm: Memory-
augmented large multimodal model for long-term video
understanding. InProceedings of the IEEE/CVF Confer-
ence on Computer Vision and Pattern Recognition, pp.
13504–13514, 2024.
Hussain, Z., Zhang, M., Zhang, X., Ye, K., Thomas, C.,
Agha, Z., Ong, N., and Kovashka, A. Automatic un-
derstanding of image and video advertisements. InPro-
ceedings of the IEEE conference on computer vision and
pattern recognition, pp. 1705–1715, 2017.
Jaech, A., Kalai, A., Lerer, A., Richardson, A., El-Kishky,
A., Low, A., Helyar, A., Madry, A., Beutel, A., Car-
ney, A., et al. Openai o1 system card.arXiv preprint
arXiv:2412.16720, 2024.
Jin, D., Xu, R., Zeng, J., Lan, R., Bai, Y ., Sun, L., and Chu,
X. Semantic context matters: Improving conditioning for
autoregressive models.arXiv preprint arXiv:2511.14063,
2025.
Lan, R., Bai, Y ., Duan, X., Li, M., Jin, D., Xu, R., Sun, L.,
and Chu, X. Flux-text: A simple and advanced diffusion
transformer baseline for scene text editing.arXiv preprint
arXiv:2505.03329, 2025.
Li, B., Zhang, Y ., Guo, D., Zhang, R., Li, F., Zhang, H.,
Zhang, K., Zhang, P., Li, Y ., Liu, Z., et al. Llava-
onevision: Easy visual task transfer.arXiv preprint
arXiv:2408.03326, 2024.
Li, Y ., Du, Y ., Zhou, K., Wang, J., Zhao, W. X., and Wen,
J.-R. Evaluating object hallucination in large vision-
language models.arXiv preprint arXiv:2305.10355,
2023.
Lin, B., Ye, Y ., Zhu, B., Cui, J., Ning, M., Jin, P., and Yuan,
L. Video-llava: Learning united visual representation by
alignment before projection. InProceedings of the 2024
conference on empirical methods in natural language
processing, pp. 5971–5984, 2024.
Lin, W., Wei, X., An, R., Ren, T., Chen, T., Zhang, R., Guo,
Z., Zhang, W., Zhang, L., and Li, H. Perceive anything:
Recognize, explain, caption, and segment anything in
images and videos.arXiv preprint arXiv:2506.05302,
2025.
Liu, H., Li, C., Wu, Q., and Lee, Y . J. Visual instruction tun-
ing.Advances in neural information processing systems,
36:34892–34916, 2023.
Long, X., Tian, K., Xu, P., Jia, G., Li, J., Yang, S., Shao,
Y ., Zhang, K., Jiang, C., Xu, H., et al. Adsqa: Towards
advertisement video understanding. InProceedings of the
IEEE/CVF International Conference on Computer Vision,
pp. 23396–23407, 2025.
9

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
Schick, T., Dwivedi-Yu, J., Dess`ı, R., Raileanu, R., Lomeli,
M., Hambro, E., Zettlemoyer, L., Cancedda, N., and
Scialom, T. Toolformer: Language models can teach
themselves to use tools.Advances in Neural Information
Processing Systems, 36:68539–68551, 2023.
Tan, X., Luo, Y ., Ye, Y ., Liu, F., and Cai, Z. Allvb: All-in-
one long video understanding benchmark. InProceed-
ings of the AAAI Conference on Artificial Intelligence,
volume 39, pp. 7211–7219, 2025.
Wang, W., He, Z., Hong, W., Cheng, Y ., Zhang, X., Qi, J.,
Ding, M., Gu, X., Huang, S., Xu, B., et al. Lvbench:
An extreme long video understanding benchmark. In
Proceedings of the IEEE/CVF International Conference
on Computer Vision, pp. 22958–22967, 2025.
Wu, B., Zou, C., Li, C., Huang, D., Yang, F., Tan, H., Peng,
J., Wu, J., Xiong, J., Jiang, J., et al. Hunyuanvideo 1.5
technical report.arXiv preprint arXiv:2511.18870, 2025.
Wu, J., Liu, Q., Wang, D., Zhang, J., Wu, S., Wang, L.,
and Tan, T. Logical closed loop: Uncovering object
hallucinations in large vision-language models.arXiv
preprint arXiv:2402.11622, 2024.
Wu, Z., Xiong, C., Ma, C.-Y ., Socher, R., and Davis, L. S.
Adaframe: Adaptive frame selection for fast video recog-
nition. InProceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pp. 1278–
1287, 2019.
Xu, R., Jin, D., Bai, Y ., Lan, R., Duan, X., Sun, L., and Chu,
X. Scalar: Scale-wise controllable visual autoregressive
learning.arXiv preprint arXiv:2507.19946, 2025.
Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan,
K. R., and Cao, Y . React: Synergizing reasoning and
acting in language models. InThe eleventh international
conference on learning representations, 2022.
Zeng, J., Bai, Y ., Chen, R., Zhang, X., Sun, L., Jin, D., Xu,
R., Zhang, N., Song, D., and Chu, X. Eevee: Towards
close-up high-resolution video-based virtual try-on.arXiv
preprint arXiv:2511.18957, 2025.
Zhang, P., Zhang, K., Li, B., Zeng, G., Yang, J., Zhang,
Y ., Wang, Z., Tan, H., Li, C., and Liu, Z. Long con-
text transfer from language to vision.arXiv preprint
arXiv:2406.16852, 2024a.
Zhang, X., Jia, Z., Guo, Z., Li, J., Li, B., Li, H., and
Lu, Y . Deep video discovery: Agentic search with tool
use for long-form video understanding.arXiv preprint
arXiv:2505.18079, 2025.
Zhang, Y ., Wu, J., Li, W., Li, B., Ma, Z., Liu, Z., and Li,
C. Video instruction tuning with synthetic data.arXiv
preprint arXiv:2410.02713, 2024b.
10

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
A. Related Works
Advertising UnderstandingComputational advertisement understanding has long recognized that ads are deliberately
engineered persuasive artifacts rather than objective records, making the key challenge to infer persuasive intent beyond
literal content. Hussain et al. (2017) formalize this view by connecting observable cues (objects, scenes, edits) to symbolic
references and persuasive strategies in large-scale image and video ad datasets. Building on this semiotic framing, our work
focuses on modern long-form, information-dense advertising videos and emphasizes intent reasoning that leverages domain
knowledge (marketing psychology, rhetoric) together with stricter evidence grounding to avoid plausible-but-unsupported
narratives.
Long-Form Video Understanding with Multimodal LLMs and BenchmarksWhile the field of visual generation has
witnessed rapid advancements in controllable autoregressive learning (Xu et al., 2025; Jin et al., 2025), precise scene
text editing (Lan et al., 2025), and high-fidelity video synthesis applications (Wu et al., 2025; Zeng et al., 2025), the
domain ofunderstandinglong-form narratives faces distinct challenges. Despite rapid progress in multimodal LLMs for
video description and QA, long-form understanding remains bottlenecked by limited context, temporal fragmentation,
and imperfect multimodal integration. Representative advances include unified frameworks like Video-LLaV A (Lin et al.,
2024) and memory-augmented models such as MA-LMM (He et al., 2024) and PAM (Lin et al., 2025). However, recent
benchmarks, including Video-MME, LVBench, ALLVB, MMBench-Video and MME-CoF (Fu et al., 2025; Wang et al.,
2025; Tan et al., 2025; Fang et al., 2024; Guo et al., 2025), collectively reveal that current systems still degrade markedly
on multi-hour videos and require explicit long-term memory. Motivated by these findings, our approach treats advertising
videos as high-density long-form narratives, incorporating structured memory, temporal indexing, and iterative evidence
collection tailored to intent-centric reasoning.
Tool-Augmented Agents and Hallucination-Aware Multimodal ReasoningA promising solution to long-context con-
straints is tool-augmented, agentic reasoning that iteratively gathers evidence and revises hypotheses. On the language
side, Yao et al. (2022); Schick et al. (2023) show that LLMs can interleave reasoning with external tool calls and even
self-supervise tool-use policies, while in the video domain Zhang et al. (2025); Fan et al. (2024) develop agentic frame-
works such as DVD and VideoAgent for multi-granular retrieval and memory-augmented long-horizon understanding, and
hallucination analyses including HallusionBench and object-centric evaluations like POPE and Logical Closed Loop by
Guan et al. (2024); Li et al. (2023); Wu et al. (2024) demonstrate that LVLMs frequently produce confident yet weakly
supported explanations. Building on this line of work, our method instantiates an advertising-specific tool-augmented agent
with domain-adaptive inductive biases and hallucination-aware self-correction, explicitly enforcing evidence-first reasoning
when mapping pixel-level anchors to persuasion-level intents.
B. Implementation Details
In this section, we provide a detailed overview of the experimental setup, including the testing protocols for baseline models
and the specific hyperparameter configurations for our proposed ADMIRagent.
B.1. Baseline Testing Protocol
Following the benchmarking standards established in AdsQA, we evaluate baseline Multimodal Large Language Models
(MLLMs) using a standardized zero-shot setting to ensure fair comparison.
Frame Sampling Strategy.For end-to-end MLLM baselines, we adopt a uniform sampling strategy. Given the high
temporal redundancy in advertisement videos, we sample N= 16 frames uniformly distributed across the video duration.
For models that support high-resolution inputs or dynamic resolution (e.g., o1), frames are resized while maintaining the
aspect ratio, with the longest side not exceeding 1024 pixels.
Prompting Strategy.We utilize the standard prompts provided by the AdsQA benchmark. The prompt structure consists
of a system instruction defining the task (Video QA), followed by the visual inputs (interleaved frames) and the specific
question. For open-ended generation, we employ a greedy decoding strategy to ensure reproducibility.
B.2. Admir Agent Configuration
The implementation details for the data preprocessing and agent hyperparameters are strictly aligned with the provided logic.
11

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
Video Database Construction.We preprocess the AdsQA video corpus to build a structured retrieval database:
•Frame Extraction: Videos are decoded at a frame rate of 1 FPS (‘VIDEO FPS=1‘).
• Captioning: We generate dense captions for video clips with a duration of 5 seconds (‘CLIPSECS=5‘). The captioning
model isgpt-4o.
• Subject Registry: A dynamic subject registry is maintained and merged across clips to track character identities and
key objects.
•Embeddings: We utilizeBAAI/bge-m3(dimension 1024) for local vector storage.
Agent Hyperparameters.The ADMIRagent is orchestrated by gpt-4o, while the specialized COMMUNICATIONEXPERT
tool utilizes the reasoning-intensiveo1model.
• Maximum Iterations: The ReAct loop is capped at Tmax = 8 steps to prevent infinite loops, though most queries are
resolved within 4–6 steps.
• Global Browse: The top K= 40 semantic captions (‘GLOBAL BROWSE TOPK‘) are retrieved during the pre-
emptive global browse phase to construct the initial narrative context.
• Clip Search: A hybrid search mechanism (Vector + Keyword) retrieves the top K= 5 to 8 relevant clips for
fine-grained inspection.
• Expert Analysis: The COMMUNICATIONEXPERTprocesses up to 64 frames stitched into 2×2 grid images to analyze
visual rhetoric and persuasion strategies.
• Answer Refinement: The final output is refined by gpt-4o-mini to strictly adhere to the token limit (under 30
words) while preserving critical entities and attributes.
Retry Mechanism.To handle API instability and potential hallucinations in tool calls, we implement an exponential backoff
retry mechanism with a maximum of 8 retries for critical API failures.
B.3. Algorithm Robustness Details
To prevent the ReAct agent from falling into infinite loops or overwriting high-confidence expert insights with low-level
hallucinations, we implement three specific algorithmic safeguards within the inference controller.
1. Temporal Stagnation Detection & Redirection.In long-horizon reasoning, agents often become fixated on a specific
time segment, repeatedly searching the same interval despite finding no new evidence. To mitigate this, we implement a
Temporal Stagnation Check. Let Htime ={(t (i) start, t(i) end)} be the history of time ranges queried by the agent. For a new
query range[t s, te]with durationd=t e −t s, we calculate the overlap ratio with history:
Overlap(i) = intersection([ts, te],[t (i) start, t(i) end]) d (6)
If Overlap(i)>0.6 for more than N= 2 distinct historical queries, the system triggers aForced Redirection Intervention.
The agent’s query is overridden, and the focus is mechanically shifted to the video boundaries (First 15s or Last 15s) to
break the cognitive deadlock.
2. Anti-Verification Protocol (The ”Golden Source” Rule).A common failure mode in hierarchical agents is ”over-
verification,” where the agent uses a low-capacity tool (e.g., frame inspect) to verify a high-capacity tool (e.g.,
communication expert), leading to false negatives due to sparse sampling. We enforce anAnti-Verification Protocol
via the system prompt:
”IF the Communication Expert returns a specific Proper Name, Metaphor, or Strategy, YOU MUST ACCEPT IT
AS FACT. DO NOT use frameinspect tool to ’double check’ what the Expert Tool has already found. ”
12

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
This ensures that high-level semantic findings (e.g., ”The ad uses a fear appeal strategy”) are not discarded simply because a
literal frame inspection failed to OCR the word ”fear”.
3. Visual Anchor Repair.For questions explicitly demanding visual grounding (e.g., ”What specific object...”), the agent’s
draft answer is passed through a lightweight verification module (using GPT-4o-mini). If the answer lacks concrete visual
nouns (anchors) found in the retrieval evidence, a repair loop is triggered to inject specific observable details (e.g., changing
”a vehicle” to ”a red Ferrari”) before final output.
B.4. Expert Model Input Strategy
To bridge the gap between token limits and the need for high temporal resolution in advertising analysis, we employ a
Spatio-Temporal Grid Projectionstrategy for thecommunication expert tool.
High-Density Sampling.Unlike standard approaches that sample 8-16 frames, our expert module samples N= 64 frames
uniformly distributed across the video duration (or the queried segment). This high density is crucial for capturing fleeting
subliminal cues typical in commercials (e.g., split-second micro-expressions or flash cuts).
2x2 Grid Stitching.Directly feeding 64 images exceeds the file count limits of most VLM APIs. We therefore stitch
consecutive frames into2×2grid images.
•Batching: The 64 frames are divided into 16 batches of 4 frames each.
• Composition: Each batch is stitched into a single high-resolution image (Hgrid = 2×H f rame, Wgrid = 2×W f rame).
•Resolution: The resulting grids are encoded withdetail: "high"to preserve OCR-readability in sub-frames.
Temporal Serialization.The VLM receives a sequence of 16 grid images. To ensure correct temporal reasoning, the system
prompt explicitly defines the reading order:
Order: Top-Left− →Top-Right− →Bottom-Left− →Bottom-Right (7)
This projection allows the model to process 64 frames of visual information while only consuming the request overhead of
16 images, effectively quadrupling the temporal context window.
C. Core Prompts of AD-MIR
In this section, we present the comprehensive system prompts used in the AD-MIR framework. These prompts are
meticulously designed to guide the neuro-symbolic agent through the distinct stages of perception, reasoning, and answer
refinement.
C.1. Perception & Context Construction Prompts
The following prompts drive the offline perception layer, transforming raw video signals into structured semantic indices
through narrative reconstruction and dynamic inspection.
Global Browse: Text-Based Forensic Reconstruction
Role Media Forensics Expert
Goal Reconstruct the narrative and ground truth from multimodal logs (Visual Captions + Audio) without direct pixel
access.
Key Mechanisms
• A/V Cross-Referencing: Combining visual descriptions with audio transcripts to infer specific entities (e.g.,
”Product shown” + ”Audio mentions Pepsi”→”Pepsi”).
•Text Hunting: Specifically scanning logs for[POTENTIAL TEXT]tags to extract explicit on-screen text.
System Prompt
13

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
You are a Media Forensics Expert specialized in solving AdsQA cases.
**YOUR CONSTRAINT **: You cannot see the video. You only have access to:
1. **Visual Logs **: Text descriptions of what happens.
2. **Audio Transcript **: What was said.
**STRATEGY FOR TEXT-ONLY ANALYSIS **:
1. **Cross-Referencing**: If Visual Log says "[SCENE]: A product is shown" and Audio says "Try the new
Pepsi", you must infer the product is "Pepsi".
2. **Text Hunting **: Look specifically for the ‘[POTENTIAL_TEXT]‘ tags in the logs.
3. **Implicit Clues **: Identify brands/objects from specific descriptions (e.g., red car + horse logo $\
to$ Ferrari).
**OUTPUT FORMAT (JSON) **:
{
"narrative_reconstruction": "Story flow (Hook $\to$ Middle $\to$ End).",
"inferred_objects": ["List of objects implied by combining visual + audio"],
"explicit_text_found": ["Text explicitly quoted in visual logs"],
"audio_visual_mismatch": "Contradictions between seen and heard?",
"final_answer": "Direct answer to the USER QUERY."
}
Frame Inspect: Dynamic Mode Switching
Function ‘frame inspect tool‘
Strategy The tool dynamically selects an analysis mode based on the query type (Factual vs. Abstract).
Mode A: Literal Inspection (OCR & Factual)
[MODE: LITERAL INSPECTION & OCR]
1. **VISUAL LOG **: Create a chronological log of events.
2. **TEXT**: Transcribe any visible text/logos verbatim.
3. **DETAILS**: List objects and specific physical interactions.
Mode B: Semantic Analysis (Narrative & Symbolism)
[MODE: SEMANTIC & NARRATIVE]
1. **STORY**: Describe the setup -> action -> outcome.
2. **TWIST**: Note if the environment changes artificially (e.g., reveal of a set).
3. **MEANING**: Identify key symbols and subject relationships.
Clip Search: Semantic Query Rewrite
Function ‘clip search tool‘
Goal Generalize specific user queries into broader visual concepts for better retrieval recall.
Rewrite Prompt
Rewrite ’{original_query}’ into 3 simple, comma-separated keywords/phrases for video retrieval.
Rules: Keep it generic. Do NOT invent specific visual details (e.g. do NOT change ’luxury’ to ’gold’).
Input: ’sad man’ -> Output: crying person, unhappy face, depressed mood
14

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
C.2. Structured Agent Reasoning Prompts
These prompts control the online inference engine, managing the interaction between the ReAct controller and domain-
specific experts.
Communication Expert: Visual Semiotics Analysis
Input 2x2 Grid Images (High-Density Temporal Sampling)
Core Analysis Protocols
•2x2 Grid Reading: Explicit instruction on reading order (TL→TR→BL→BR).
•Grounding: Strict prohibition against hallucinating objects not present in the grid.
System Prompt
You are an Elite Advertising Forensics Expert & Visual Semiotics Analyst.
**YOUR MISSION **: Decode the provided video content to uncover the narrative structure, character
relationships, and persuasive strategy.
**INPUT FORMAT (CRITICAL) **:
- The visual input consists of **2x2 Grid Images **.
- Each image contains **4 chronological video frames **.
- **Reading Order **: Analyze each grid from **Top-Left -> Top-Right -> Bottom-Left -> Bottom-Right **.
**CORE ANALYSIS PROTOCOLS: **
1. **OCR & BRAND TRUTH (HIGHEST PRIORITY) **: Any text on screen is fact. Identify Logos.
2. **UNIVERSAL CHARACTER DYNAMICS **: Analyze Transactional, Conflict, or Affectionate interactions.
3. **NARRATIVE ARC **: Hook -> Problem -> Product -> CTA.
4. **GROUNDING**: Do not invent objects not present in the grids.
ReAct Controller: System Instructions
Role Advanced Video Analysis Agent
Philosophy ”Trust Y our Expert & Be Decisive”
System Prompt
You are an advanced Video Analysis Agent. Your goal is to answer the user’s question precisely using the
provided tools.
**CORE PHILOSOPHY: TRUST YOUR EXPERT & BE DECISIVE **
1. **THE "GOLDEN SOURCE" RULE **: The ‘communication_expert_tool‘ is your PRIMARY SOURCE OF TRUTH. If it
returns specific Proper Names or Metaphors, YOU MUST ACCEPT IT AS FACT.
2. **ANTI-VERIFICATION PROTOCOL **: DO NOT use ‘frame_inspect_tool‘ to "double check" the Expert Tool.
Only use it as a fallback.
3. **SINGLE-SHOT VICTORY **: If the Expert Tool answers fully, FINISH IMMEDIATELY.
**OUTPUT PROCESS **:
1. **THOUGHT**: First, write a brief thought analysis in plain text explaining your reasoning.
2. **ACTION**: Then, call the appropriate tool using the native function calling capability.
15

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
Answer Refinement & Repair
Stage Post-Processing
Task Compress output to<30 tokens and repair visual grounding errors.
Refinement Prompt
You are compressing an answer for a visual QA benchmark.
Rewrite the answer to be <= 25 words, but DO NOT lose any core information.
[HARD CONSTRAINTS]
- Preserve ALL essential facts: names/entities, key attributes (color, number, time), and negation.
- DO NOT add new facts or hallucinations.
- If original is entity identification, output a compact noun phrase.
[EDITING RULES]
1) Remove meta phrases: "the video shows", "the answer is".
2) Keep specificity: numbers, brand names, proper nouns.
Visual Grounding Repair Prompt
Rewrite the answer so it names ONE specific, observable scene/object/action from the evidence.
Hard constraints:
- Mention a concrete visual element (what is shown), not abstract traits.
- Use at least 1 anchor word if possible.
- Under 30 tokens.
C.3. Data Preprocessing Prompts
The following prompts drive the offline perception layer, transforming raw video signals into structured semantic indices
through narrative reconstruction, entity tracking, and fine-grained text extraction.
Visual Captioning & Subject Registry Extraction
Input Consecutive Video Frames (Clip Level)
Core Analysis Protocols
•Structured Output: Strict JSON format enforcement for database indexing.
•Subject Profiling: Extract detailed appearance and identity for the context-anchored registry.
System Prompt
16

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
Here are consecutive frames from a video clip. Please visually analyze the video clip and output JSON in
the template below.
Output template:
\{
"clip\_start\_time": CLIP\_START\_TIME,
"clip\_end\_time": CLIP\_END\_TIME,
"subject\_registry": \{
"<subject\_i>": \{
"name": "<fill with short identity if name is unknown, e.g. ’man in red’>",
"appearance": "<list of visual appearance descriptions>",
"identity": "<list of inferred identity descriptions>",
"first\_seen": "<timestamp>"
\},
...
\},
"clip\_description": "<smooth and detailed visual narration of the video clip>"
\}
Subject Registry Merging
Input List of Partial Subject Registries (from multiple clips)
Core Analysis Protocols
•De-duplication: Merge subjects referring to the same visual entity across time.
•Union: Combine attribute fields while preserving the earliest timestamp.
System Prompt
You are given several partial ‘new\_subject\_registry‘ JSON objects extracted from different clips of
the *same* video.
Task:
1. Merge these partial registries into one coherent ‘subject\_registry‘.
2. Preserve all unique subjects.
3. If two subjects visually refer to the same person/object, merge them (keep earliest ‘first\_seen‘
time and union all fields).
Input (list of JSON objects):
REGISTRIES\_PLACEHOLDER
Return *only* the merged ‘subject\_registry‘ JSON object.
Fine-Grained OCR Extraction
Input Single Video Frame (High Resolution)
Core Analysis Protocols
•Exhaustive Extraction: Capture all visible text including logos, brand names, and background signs.
•Format: One item per line, strictly no visual descriptions.
System Prompt
17

AD-MIR: Bridging the Gap from Perception to Persuasion in Advertising Video Understanding via Structured Reasoning
Extract ALL visible text from this image.
Include: titles, labels, captions, signs, logos, brand names, slogans, any written content.
Return ONLY the extracted text, one item per line.
If no text is visible, return "NO\_TEXT".
Do not describe the image, only extract text.
C.4. Evaluation Prompts
The prompt utilized by the LLM-as-a-Judge mechanism to benchmark performance against ground truth annotations.
AdsQA Evaluation Judge
Role Advertising Expert Judge
Goal Evaluate semantic alignment between prediction and golden answer.
Judge Prompt
You are an advertising expert specializing in evaluating whether a respondent’s answer after watching a
video matches the golden answer.
### The meta-information (Ground Truth):
{meta_info}
### Question:
{question}
### Golden Answer:
{golden_answer}
### Rule:
1. If response contains ALL key info OR expresses same meaning -> Output 1.
2. If response does NOT contain key info -> Output 0.
3. If response is contradictory/unreasonable given meta-info -> Output 0.
4. If response contains MOST key info and NO contradictions -> Output 0.5.
### Response to be judged:
{response}
### Instructions:
Follow the format below and do not give any extra outputs:
Answer: 0 / 0.5 / 1
18
