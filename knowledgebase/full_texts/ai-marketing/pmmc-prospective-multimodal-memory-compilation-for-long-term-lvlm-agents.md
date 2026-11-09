---
title: 'PMMC: Prospective Multimodal Memory Compilation for Long-Term LVLM Agents'
url: https://arxiv.org/abs/2608.00962
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Jingyu Sun
- Yan Lin
- Yuyang Xue
- Yifan Wang
- Zhengtao Yao
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.00962
pages: 9
chars: 36110
fetched_at: '2026-11-08T13:32:46+00:00'
kb_version: 1
---

# PMMC: Prospective Multimodal Memory Compilation for Long-Term LVLM Agents

PMMC: Prospective Multimodal Memory Compilation for Long-Term LVLM
Agents
Jingyu Sun1,2, Yan Lin3, Yuyang Xue4, Yifan Wang1, Zhengtao Yao5,
Rui Qian6, Zefeng Xu1, Jiachen Li7, Xianyang Liu8, Jiancheng Pan9,
Jingyuan Sun1, Syed Murtuza Baker1, Hongpeng Zhou1∗
1The University of Manchester 2The University of Melbourne 3The University of Newcastle
4The University of Edinburgh 5The University of Southern California 6Fudan University
7The University of Texas at Austin8Independent Researcher 9Ant Group
Abstract
Long-term memory is essential for LVLM agents to maintain
consistency and integrate information across extended multi-
modalinteractions.Existingagentmemorysystems,however,
often reduce visual experiences into textual summaries or
rely on static retrieve-then-reason pipelines, which are ineffi-
cient at query time and brittle when questions require image-
text binding, temporal updates, or visual details. We propose
Prospective Multimodal Memory Compilation, a framework
that shifts part of the memory reasoning process from query
timetomemoryconsolidationtime.Givenaccumulatedmulti-
modalinteractions,aQuestionerpredictsfuturequestioncan-
didates,aPlannercompilesquestion-conditionedmultimodal
memoryprograms,andaDoubterverifieswhethertheplanned
evidence path can support the predicted answer. The verified
question-program pairs form a structured question bank for
efficient query-time routing and evidence retrieval. Experi-
ments on multimodal long-term memory benchmarks show
that our method improves answer quality and visual evidence
recallwhilereducingquery-timetokenandlatencycosts.Ex-
tensiveablationsanalyzetheeffectsofself-feedback,dynamic
planning, raw-image access, and question bank coverage.
Introduction
Long-term memory is essential for large vision-language
model (LVLM) agents operating over extended multimodal
interactions.Unlikeconventionalvisualquestionanswering,
agent experiences arrive incrementally across sessions, so
evidenceforafuturequerymaybedistributedacrossdistant
turns, images, and later corrections. A capable agent must
therefore recall earlier information, bind visual entities to
linguistic references, combine evidence across events, and
update stale beliefs. Recent benchmarks show that current
systems remain challenged by long-range multimodal rea-
soning,temporalupdates,conflicts,andunsupportedqueries
(Maharana et al. 2024; Ren et al. 2026; Bei et al. 2026).
Existing approaches broadly rely on either long-context
LVLMs or external memory. Long-context models directly
consume interleaved histories, but their computational cost
grows with context length and their ability to locate rele-
vantevidenceoftendegradesashistoriesexpand(Songetal.
2024;Wangetal.2026;Renetal.2026).Memory-augmented
agents instead store and selectively retrieve past experiences
∗Corresponding author.
using summaries, structured notes, hierarchical stores, or
graphs (Lewis et al. 2020; Park et al. 2023; Packer et al.
2023;Xuetal.2026;Chhikaraetal.2025).Althoughrecent
multimodal systems preserve richer visual and personalized
information (Long et al. 2025; Feng et al. 2026), they still
committoamemoryrepresentationandaccesspolicybefore
future queries are known.
Thiscommitmentisespeciallyproblematicformultimodal
memory. Caption-based stores are efficient but permanently
lose visual attributes omitted during captioning. Contrastive
encoders such as CLIP and SigLIP align images and text
semantically (Radford et al. 2021; Zhai et al. 2023), yet do
not explicitly preserve interaction-specific bindings, such as
a subsequently assigned name for an earlier image. Unified
multimodal encoders can represent mixed inputs (Li et al.
2026), but still require a fixed granularity for compressing
heterogeneous evidence. A single representation is unlikely
to suit all information needs: factual questions may require
text, entity questions image–text associations, visual-detail
questions original pixels, and temporal or multi-hop ques-
tionsseverallinkedmemories.Existingbenchmarksaccord-
ingly report losses from caption-only compression and from
retrievingredundantorweaklyalignedmultimodalevidence
(Bei et al. 2026; Ren et al. 2026).
Conventional RAG resolves these choices only after a
query arrives by retrieving, optionally reranking, and sup-
plying a fixed number of candidates (Lewis et al. 2020).
Agenticretrievalismoreadaptive,allowingmodelstorefor-
mulate searches or interleave retrieval with reasoning (Yao
et al. 2022; Trivedi et al. 2023; Jiang et al. 2023; Asai et al.
2024;Jeongetal.2024),butrequiresadditionalonlinemodel
calls and retrieval rounds. Index-time question generation
can improve alignment between text documents and likely
queries (Lewis et al. 2021; Neeser et al. 2025), yet existing
approaches primarily use generated questions as retrieval
keys rather than compiling and verifying executable multi-
modal access procedures.
We therefore ask whether an agent can anticipate plau-
sible future information needs during memory consolida-
tion and prepare how their evidence should be accessed.
We proposeProspective Multimodal Memory Compila-
tion (PMMC), illustrated in Figure 1. AQuestionergener-
atessource-groundedprospectivequestions,aPlannercom-
arXiv:2608.00962v1  [cs.AI]  2 Aug 2026

Figure 1:Comparison of multimodal memory-access paradigms.Fixed RAG uses a predefined memory representation and
retrieval policy, whereas agentic retrieval adapts through repeated query-time reasoning. PMMC instead compiles and verifies
question-conditionedmemoryprogramsduringconsolidationandexecutesthemonline,retainingmultimodalRAGasafallback.
piles each into a typed multimodal memory program, and a
Doubterverifiestheprogramthroughexecutionandbounded
iterative refinement. Accepted question–program pairs form
a structured Question Bank. At query time, PMMC matches
theincomingquery,executestheselectedfrozenaccessstrat-
egyoverthecurrentlyvisiblememory,andanswersfromthe
recoveredsourceevidencewithoutinvokingthecompilation
agents online. Uncertain routes or insufficient evidence in-
stead invoke multimodal RAG. The Question Bank is there-
fore a routing and program index, not an answer cache.
Across MEMLENS and Mem-Gallery with four LVLM
backbones, PMMC ranks first in six of eight configurations
and improves the overall macro-average Harmonized Judge
scoreby3.2pointsoverthestrongestbaseline(Table1).Our
contributions are threefold:
•We formulateprospective multimodal memory compila-
tion, moving question-conditioned access planning from
query time to memory-consolidation time while preserv-
ing source-grounded answering.
•We introduce a Questioner–Planner–Doubter framework
that compiles and execution-validates typed multimodal
memoryprograms,withonlinefallbackwhenprospective
coverage is insufficient.
•WeevaluatePMMCagainstlong-context,fixed-retrieval,
and multimodal agent-memory baselines, and analyze
self-feedback, dynamic planning, raw-image access, and
write–query cost trade-offs.
Methodology
Prospective Multimodal Memory Compilation (PMMC)
shifts part of memory access planning from query time to
memory consolidation time. Given the multimodal history
accumulated so far, PMMC generates plausible future in-
formation needs, compiles each into an executable memory
program, and verifies the program through actual execution.
The accepted question–program pairs form a runtime Ques-
tion Bank. When a real query arrives, PMMC retrieves and
executesacompiledprogramoverthecurrentlyvisiblemem-
ory; uncertain routes or insufficient evidence invoke multi-
modal RAG fallback (Lewis et al. 2020).
Problem Formulation
Let the multimodal interaction history beH=
{m1, . . . , mN }, where
mi = (xi,I i, ci, si, ℓi, bi, µi),
H≤t ={m i ∈ H |bi ≤t}. (1)
Here,x i is conversational text,Ii denotes associated source
images,c i is an optional caption,si andℓ i denote session
and temporal order,bi is the boundary at which the memory
becomesavailable,andµ istoresmetadata.Captionsandem-
beddings serve only as auxiliary indices; original utterances
and images remain the canonical evidence.
At consolidation boundaryt, every PMMC component is
restricted toH ≤t within the same conversation and dataset

Figure2:OverviewofPMMC.Duringconsolidation,aQuestionergeneratessource-groundedprospectivequestions,aPlanner
compiles typed memory programs, and a Doubter verifies them through execution and bounded revision. Compiler-private
provisional answers and source support are removed before accepted question–program pairs enter the runtime Question Bank.
At query time, PMMC routes the incoming query to a frozen program, re-executes it over the currently visible memory, and
answersfromtherecoveredsourceevidence.FailedroutingorreadinesschecksinvokemultimodalRAGfallback;noQuestioner,
Planner, or Doubter call occurs online.
snapshot. Benchmark queries, reference answers, annotated
clues,andevaluator-sideevidenceareexcluded.PMMCcon-
structsaQuestionBankB t containingprospectivequestions
and verified access programs, rather than cached responses.
Prospective Question and Program Compilation
For each newly consolidated anchor, PMMC constructs a
bounded compilation unitU t from the anchor and earlier
supportingmemories.Supportisselectedfromcomplemen-
tary relations, including temporal proximity, lexical or en-
tity overlap, shared images, and profile or preference links,
subject to text and image budgets. A deterministic analyzer
further identifies evidence opportunitiesΩt, such as visual
attributes, image–text bindings, temporal updates, conflicts,
andmulti-evidencerelations.Onlytemporaryaliasesforvis-
ible text spans and images are exposed to the model.
Conditioned on(U t,Ω t), the Questioner generates a
boundedsetofcanonicalprospectivequestions,paraphrases,
and source-support claims:
eQt =Q θ(Ut,Ω t).(2)
The compiler validates grounding and cutoff consistency,
removes duplicates and previously observed questions, and
derives each candidate’s question type, reasoning mode, re-
quired modalities, and minimum evidence multiplicity. It
also constructs a provisional answerbaj and source support
bEj exclusively from the cited visible memories. These fields
arecompiler-privateandareneverobtainedfrombenchmark
annotations.
For candidatebqj, the compiler constructs a requirement
contractR j specifying the modalities, capabilities, and ev-
idence multiplicity required for answering it. The Planner
observes(bqj, Rj)and typed revision directives, but notbaj,
bEj, source identifiers, or benchmark labels. At refinement
roundr, it selects a constrained strategy that is deterministi-
cally lowered into a typed program:
z(r) j =P ϕ(bqj, Rj,∆ (r−1) j ),
π(r) j = Lower(z(r) j , Rj) = [o(r) j,1 , . . . , o(r) j,Lj ]. (3)
Programsdrawfromafrozenkerneloflexicalanddensetext
retrieval,cross-modalimage retrieval,image–textandlocal-
contextexpansion,temporalexpansion,raw-imagematerial-
ization,andevidence-controloperators.Thelowererenforces
boundedlength,typedacyclicdataflow,registeredoperators,
and valid prospective lineage; arbitrary code, SQL, paths,
and unrestricted tool calls are disallowed.

Method GPT-5-mini Claude Haiku 4.5 Qwen3.5-9B Qwen3.5-27B Macro Average
ML MG ML MG ML MG ML MG ML Avg. MG Avg. Overall
Full-Ctx-Caption 39.7 37.5 35.6 37.2 47.8 36.4 51.4 41.2 43.6 38.1 40.9
Full-Ctx-Raw 36.3 33.5 32.7 34.5 46.4 32.5 47.7 39.6 40.8 35.0 37.9
Caption-Text RAG45.647.4 39.8 36.658.453.2 48.7 44.2 48.1 45.4 46.7
Contrastive MM-RAG 38.8 36.2 37.6 39.4 41.7 39.6 47.3 45.8 41.4 40.3 40.8
Native MM-RAG 34.3 29.6 37.4 34.6 44.5 44.3 49.6 51.2 41.5 39.9 40.7
M3-Agent 19.5 18.4 17.2 17.8 16.6 17.8 20.6 21.4 18.5 18.9 18.7
M2A 15.4 14.2 16.7 18.6 14.5 17.6 18.3 19.6 16.2 17.5 16.9
PMMC (Ours)44.3 48.6 42.5 39.756.2 57.8 58.6 51.4 50.4 49.4 49.9
Table1:HarmonizedJudgescores(HJ,0–100;higherisbetter)ontheprimarygenerativeevidence-recoverysplitsofMEMLENS
(ML,N= 699)andMem-Gallery(MG,N= 1,446)acrossfouranswerbackbones.MLAvg.andMGAvg.aremacro-averages
over the four backbones, and Overall is the macro-average over all eight backbone–benchmark settings. Best results in each
column are inbold, and second-best results are underlined.
Execution-Grounded Verification
PMMC verifies each initial or revised program using the
same operator kernel employed online:
(T (r) j , E(r) j ) = Exec  π(r) j ,H ≤t;bqj  ,(4)
whereT (r) j is the execution trace andE(r) j is the retrieved
typed evidence. A program is structurally ready only if it
executes successfully, returns non-empty evidence, reaches
all required modalities and capabilities, and satisfies the re-
quired source multiplicity:
Ready(E, T;R) = ExecOK(T)∧ |E|>0
∧ Mreq(R)⊆ M(E)
∧ Kreq(R)⊆ K(T)
∧N(E)≥g(R).
(5)
Thisexecution-guidedcheckpreventsaplausibletextualplan
frombeing acceptedwhenitsactual evidencepathisinvalid
(Wang et al. 2018).
The Doubter evaluates the prospective question, provi-
sional answer, private source support, program, trace, and
retrievedevidence.Itreturnspass,revise,orreject.Revisable
failures are translated into typed directives, such as adding
visual retrieval, expanding temporal context, materializing
the original image, or increasing bounded retrieval depth.
The Planner receives these directives without access to the
privateanswerorsourceidentifiers,andtherevisedprogram
is executed again for at mostrmax transitions. Thus, unlike
unconstrained self-refinement (Madaan et al. 2023; Shinn
et al. 2023), every PMMC revision is tied to an observed
execution failure and a non-overridable readiness check.
The runtime Question Bank retains only the canonical
question, paraphrases, safe type and modality metadata, re-
quirement contract, earliest passing program, and version
information. Provisional answers, private source support,
Plannerrationales,andDoubterfeedbackareremoved.Con-
sequently, the Question Bank specifieshowmemory should
be accessed but cannot directly provide an answer.
Online Routing and Answering
For a real queryqwith optional imagesI q at boundary
tq, PMMC first filters Question Bank entries by conversa-
tion, snapshot, and cutoff compatibility. It then ranks candi-
datesthroughlexical,dense-text,and,whenqueryimagesare
present, multimodal matching. The rankings are combined
usingweightedreciprocal-rankfusion(Cormack,Clarke,and
Buettcher2009),andacompiledrouteisacceptedonlywhen
bothitsconfidenceandtop-twomarginpassfixedthresholds.
The selected program is validated and re-executed over
H≤tq. The incoming query determines which program is
selected but does not trigger replanning. Importantly, the
programfreezesanaccessstrategyanditsretrievalrepresen-
tations,notafixedsetofevidenceidentifiers.Itcantherefore
retrieve valid memories that became visible after its compi-
lation.
A gold-free readiness check applies Eq. 5 without the
provisional answer or private source support. If the check
passes, the retrieved references are materialized as original
dialogue text, captions, conversational context, and source
images. The answer LVLM receives the actual query, its
query images, and only this program-emitted evidence:
A(q) =



G(q,I q,
Materialize(Eq)),
if routing and readiness pass,
GMMRAG(q,I q,
H≤tq

,
otherwise.
(6)
The provisional answerbaj is never included in the answer
prompt.Missingorambiguousroutes,invalidprograms,exe-
cutionfailures,andinsufficientevidencealltriggertheNative
Multimodal-RAG fallback.
PMMC therefore removes Questioner, Planner, Doubter,
and iterative access planning from the online critical path.
For a compiled state servingnfuture queries, we report the
amortized cost
C PMMC(n) = Ccompile n +C online,(7)

Variant HJ↑F1↑Ev.R↑Img.H↑Prog.↑QTok↓WTok↓
ML MG
PMMC (full) 56.2 57.8 49.3 73.0 69.4 92.13.2 31.8
w/o Doubter 53.4 54.6 46.5 67.8 64.8 82.7 3.818.7
w/o Dynamic Planner 51.8 52.6 44.8 64.7 58.8 76.9 4.2 25.9
w/o Raw-Image Access 53.9 52.9 46.2 68.6 0.0 84.62.729.4
Table 2: Ablation results with Qwen3.5-9B on MEMLENS (ML) and Mem-Gallery (MG). HJ is reported separately for the
two benchmarks, whereas F1, prompt evidence recall (Ev.R), raw-image evidence hit (Img.H), and program success (Prog.) are
macro-averaged across them. Img.H is evaluated only on queries requiring visual evidence. QTok denotes average query-time
modeltokensperqueryandWTokdenotesaveragewrite-timemodeltokenspercompilationunit,bothinthousands.Allquality
and success metrics are on a0–100scale. Higher is better except for QTok and WTok.
GPT-5-mini
ML
GPT-5-mini
MG
Claude
ML
Claude
MG
Qwen3.5-9B
ML
Qwen3.5-9B
MG
Qwen3.5-27B
ML
Qwen3.5-27B
MG
20 30 40 50 60
PMMC
Caption-T ext RAG
Full-Ctx-Caption
Native MM-RAG
Figure 3: Radar-chart view of the main results using rep-
resentative methods: PMMC, Caption-Text RAG, Full-Ctx-
Caption, and Native MM-RAG. Each axis corresponds to
one backbone–benchmark setting from Table 1; larger val-
ues indicate better Harmonized Judge performance. PMMC
shows the strongest overall profile across the eight settings,
with especially consistent gains on Mem-Gallery.
whereC online includes routing, program execution, fallback
when invoked, and final answer generation.
Experiment
Datasets and Evaluation
WeevaluatePMMContwobenchmarksformultimodallong-
term conversational memory.MemLenscontains 789 ques-
tionscoveringinformationextraction,multi-sessionandtem-
poralreasoning,knowledgeupdates,andanswerrefusalover
interleaved textual and visual histories (Ren et al. 2026).
We use its 32K setting and exclude the 90 answer-refusal
instances, yielding 699 answerable queries.Mem-Gallery
contains1,711questionsacross20extendedmultimodalhis-
tories and evaluates factual retrieval, visual search and rea-
soning,test-timelearning,temporalandmulti-entityreason-
ing, knowledge revision, conflict detection, and answer re-
fusal (Bei et al. 2026). Excluding the 81 conflict-detection
and184answer-refusalinstancesleaves1,446queriesforour
primary generative evidence-recovery evaluation. All meth-
ods within a reported comparison use identical query iden-
tifiers and may access only memories preceding the query-
specificcutoff;referenceanswersandannotatedevidenceare
available only to the offline evaluator.
We compare against seven baselines: two long-context
variants using either captions or original images; Caption-
Text RAG, Contrastive Multimodal RAG, and Native Multi-
modalRAG;andbenchmarkadaptationsofM3-Agent(Long
etal.2025)andM2A(Fengetal.2026).Wereportamethod-
blind Harmonized Judge score in{0,0.5,1}together with
normalized exact match, token-level F1, and BLEU-1 (Ra-
jpurkar et al. 2016; Papineni et al. 2002). Retrieval quality
is measured using evidence Recall/Hit@K, visual evidence
hit,andmulti-evidencecompleteness.PMMCisfurthereval-
uated by Question-Bank Coverage@K, program success,
fallbackrate,query-timetokensandlatency,write-timeover-
head, and amortized cost.
Implementation Details
We evaluate GPT-5-mini and Claude Haiku 4.5 as closed-
source backbones, and Qwen3.5-9B and Qwen3.5-27B as
open-weightbackbones.Withineachcondition,PMMCuses
thesamebackbonefortheQuestioner,Planner,Doubter,and
answer generator, with separate role prompts and structured
output schemas. GPT-5-mini serves as the fixed method-
blind judge for all methods and backbones. Caption-Text
RAG uses Qwen3-Embedding-8B, Contrastive Multimodal
RAG uses SigLIP2-So400M, and Native Multimodal RAG
usesQwen3-VL-Embedding-8B(Zhangetal.2025;Tschan-
nen et al. 2025; Li et al. 2026). All embeddings areℓ2-
normalized and compared using exact cosine similarity.
All final-answer calls use a 32,768-token context budget
with at most 1,024 output tokens. The RAG baselines con-
struct session-bounded windows of at most 512 text tokens
and four images, retain the top 50 results for retrieval evalu-
ation,andprovidethetopfivewindowstotheanswermodel.

3 4 5 6
Query-time tokens (K/query)
44
48
52
56Macro-avg. HJ
r = 0
r = 1
r = 2 (dep.)
r = 3 (anal.)
T ext RAG
Native MM-RAG
5 10 15 20 25 30
Number of future queries served by one compiled memory state, n
5
10
15
20
25
30
35Amortized model-token cost per query (K)
PMMC (r = 2)
Caption-T ext RAG
Native MM-RAG
M3-Agent
M2A
(a) Accuracy–query-time cost trade-off. (b) Amortized write-plus-query cost.
Figure 4: Efficiency analysis under Qwen3.5-9B. In (a), HJ is macro-averaged over MEMLENS and Mem-Gallery, and the
connectedpointsshowtheeffectofincreasingPMMC’srefinementlimit.Ther= 2pointisdeployed,whereasr= 3isretained
only for analysis because of its higher write-time cost. Only the competitive fixed-retrieval baselines are shown in this panel;
M3-Agent and M2A fall outside the displayed HJ range. Panel (b) reportsCwrite/n+C query for PMMC (r= 2), Caption-Text
RAG, Native MM-RAG, M3-Agent, and M2A, wherenis the number of future queries served by one compiled memory state.
Costs are measured in thousands of model tokens.
PMMCusesaprospective-questionbudgetofb= 8,atmost
two Planner–Doubter refinement transitions, and programs
of no more than eight operators. Question-Bank routes are
fused using reciprocal-rank fusion withκ= 60and are ac-
ceptedatconfidenceα route = 0.60withatop-twomarginof
δ= 0.05;otherwisePMMCfallsbacktoNativeMultimodal
RAG. Temperature is set to zero where supported. Open-
weight models are served in bfloat16 with vLLM (Kwon
et al. 2023) on NVIDIA H100 80GB GPUs.
Empirical Results
AsshowninTable1,PMMCachievesthehighestscoreinsix
of the eight backbone–benchmark settings and ranks second
intheremainingtwo.Averagedacrossthefourbackbones,it
reaches50.4onMEMLENSand49.4onMem-Gallery,out-
performing the strongest baseline on average, Caption-Text
RAG,by2.3and4.0points,respectively;itsoverallaverageis
49.9, compared with 46.7 for the strongest baseline. PMMC
ranks first on Mem-Gallery with every backbone, while on
MEMLENS it leads with Claude Haiku 4.5 and Qwen3.5-
27BandremainssecondwithGPT-5-miniandQwen3.5-9B,
indicatingthatitsgainsarenottiedtoasinglemodelfamily.
Figure3visualizesthesetrendsusingrepresentativebase-
lines from the main comparison families. The radar chart
shows that PMMC encloses the broadest overall profile
across the eight backbone–benchmark settings, reflecting its
consistently strong performance rather than gains concen-
trated in a single condition. Compared with Caption-Text
RAG,PMMCisslightlyweakeronGPT-5-mini/MEMLENS
and Qwen3.5-9B/MEMLENS, but clearly stronger on all
four Mem-Gallery settings and substantially stronger on
Qwen3.5-27B/MEMLENS. Full-Ctx-Caption remains com-
petitive in a few settings, especially with Qwen3.5-27B on
MEMLENS, but is less stable overall, while Native MM-
RAG is more competitive on some Mem-Gallery conditions
thanonMEMLENS.Full-Ctx-Captionalsoconsistentlyout-
performs Full-Ctx-Raw in Table 1, suggesting that directly
supplying historical images does not by itself ensure ef-
fective use of multimodal evidence under a fixed context
budget. Overall, the results support prospective, question-
conditioned memory compilation as a more robust alterna-
tive to committing to a single long-context or fixed-retrieval
strategy.
Analysis
Ablation Study
Table2showsthatallthreecomponentscontributetoPMMC.
Removing the Doubter reduces the HJ score by 2.8 points
on MEMLENS and 3.2 points on Mem-Gallery, while de-
creasing program success from 92.1 to 82.7; although this
saves approximately 41% of write-time tokens, the less reli-
able programs require more online computation. Replacing
the question-conditioned Planner with a fixed retrieval plan
causes the largest overall degradation, reducing evidence re-
callby8.3points,raw-imagehitby10.6points,andprogram
success by 15.2 points. This result supports dynamically
compilingdifferentaccessstrategiesfordifferentprospective
questions rather than applying one retrieval policy univer-
sally. Finally, removing raw-image access lowers HJ by 2.3
pointsonMEMLENSbutby4.9pointsonthemorevisually
intensive Mem-Gallery, despite reducing query-time tokens
by 15.6%. Thus, captions and textual indices cannot fully
replace access to original visual evidence. Overall, PMMC
obtains the strongest answer quality and execution reliabil-
ity at the intended cost of additional memory-consolidation

Setting HJ↑Prog.↑FB↓QTok↓WTok↓
r= 0(no refinement) 54.0 82.7 22.4 3.818.7
r= 155.9 89.1 16.7 3.4 25.4
r= 2(deployed)57.0 92.1 12.6 3.2 31.8
r= 3(analysis only)57.2 92.7 12.2 3.138.5
Table3:EffectofthemaximumnumberofPlanner–Doubter
refinement transitions under Qwen3.5-9B. HJ is macro-
averaged over MEMLENS and Mem-Gallery. Prog. is the
percentage of selected programs that execute successfully
and pass the gold-free readiness check, and FB is the query-
time fallback rate. QTok and WTok denote average query-
time model tokens per query and write-time model tokens
per compilation unit, respectively, in thousands. The bold
row label marks the deployed setting; bold values are the
best in each column.
computation.
Effect of Self-Feedback Rounds
Table3andFigure4showthatexecution-groundedfeedback
improves both program reliability and online efficiency. In-
creasing the refinement limit fromr= 0tor= 2raises the
averageHJscorefrom54.0to57.0andprogramsuccessfrom
82.7% to 92.1%, while reducing fallback by 9.8 points and
query-timetokensby15.8%.Athirdtransitionprovidesonly
a further 0.2 HJ points and 0.6 program-success points, but
increases write-time tokens by 21.1% relative tor= 2; we
therefore deployr= 2. This operating point also lies above
and to the left of the competitive fixed-retrieval baselines in
Figure 4(a). Although PMMC incurs the largest initial con-
solidation cost, its lower online cost recovers the overhead
after approximately two queries relative to M3-Agent and
M2A, twelve relative to Native MM-RAG, and eighteen rel-
ative to Caption-Text RAG. These results support bounded
self-feedbackasafavorablequality–costtrade-offforrepeat-
edly accessed long-term memory.
Question Bank Coverage
Table 4 shows that the prospective Question Bank covers
a substantial, but not exhaustive, portion of future infor-
mation needs. Macro-averaged evidence coverage increases
from 55.0% atK= 1to 82.1% atK= 5, while semantic
matching rises from 48.3% to 75.2%. The 6.9-point gap be-
tween Cover@5 and Match@5 indicates that some relevant
evidenceprogramsarealreadypresentinthebankbutarenot
ranked under a sufficiently compatible prospective question,
making routing—rather than question generation alone—an
important remaining bottleneck. Oracle candidate selection
reaches an HJ score of 65.4, 8.4 points above the deployed
PMMC average of 57.0, revealing additional headroom in
candidate ranking, program selection, and downstream an-
swering. Nevertheless, only 12.6% of queries invoke fall-
back,suggestingthattheQuestionBankhandlesmostqueries
directlyratherthansucceedingthroughfrequentrecoveryby
multimodal RAG.
Metric MEMLENS Mem-Gallery Macro Avg.
QBank-Cover@1 52.1 57.8 55.0
QBank-Cover@3 70.8 76.2 73.5
QBank-Cover@5 79.6 84.5 82.1
QBank-Match@1 45.7 50.9 48.3
QBank-Match@3 63.4 69.7 66.6
QBank-Match@5 71.9 78.4 75.2
Oracle-QBank HJ 63.8 66.9 65.4
Fallback Rate 14.6 10.6 12.6
Table 4: Question-Bank coverage and routing diagnostics
under Qwen3.5-9B. Cover@Kis the percentage of queries
whoserequiredsourcegroupsarefullycoveredbytheunion
of the top-KQuestion-Bank candidates. Match@Kindi-
cates that at least one of the top-Kcandidates expresses an
information need sufficient to answer the real query. Ora-
cle HJ uses evaluator-side evidence labels only to select the
most appropriate compiled candidate, after which the same
frozen program and answer model are executed. FB denotes
the deployed fallback rate. All values are percentages except
Oracle HJ, which is reported on the0–100scale.
Conclusion
We introducedProspective Multimodal Memory Com-
pilation (PMMC), a framework that reframes multimodal
long-term memory as a prospective compilation problem
rather than relying exclusively on query-time retrieval.
During memory consolidation, PMMC generates source-
grounded prospective questions, compiles them into typed
multimodal memory programs, and verifies their evidence
paths through execution-grounded Planner–Doubter refine-
ment. The resulting Question Bank stores verified access
strategies rather than predicted answers; at query time, the
selected program is re-executed over the currently visible
memory, with native multimodal RAG retained as a fall-
back.AcrossMEMLENSandMem-GallerywithfourLVLM
backbones,PMMCranksfirstinsixofeightsettingsandim-
proves the overall macro-average Harmonized Judge score
from 46.7 to 49.9 over the strongest baseline. These results
demonstrate that moving adaptive memory-access planning
to consolidation time can provide more robust performance
across heterogeneous multimodal information needs while
reducing dependence on repeated online planning. PMMC
remains limited by prospective-question coverage and ad-
ditional write-time computation, making its benefits most
pronounced when consolidated memories are accessed re-
peatedly.FutureworkmayexplorecontinualQuestion-Bank
maintenance, learned program policies, and extension to
richer modalities and interactive environments.
References
Asai, A.; Wu, Z.; Wang, Y.; Sil, A.; and Hajishirzi, H. 2024.
Self-rag:Learningtoretrieve,generate,andcritiquethrough
self-reflection. InInternational conference on learning rep-
resentations, volume 2024, 9112–9141.
Bei, Y.; Wei, T.; Ning, X.; Zhao, Y.; Liu, Z.; Lin, X.; Zhu,
Y.; Hamann, H.; He, J.; and Tong, H. 2026. Mem-gallery:

Benchmarking multimodal long-term conversational mem-
ory for mllm agents.arXiv preprint arXiv:2601.03515.
Chhikara, P.; Khant, D.; Aryan, S.; Singh, T.; and Yadav, D.
2025. Mem0:Buildingproduction-readyaiagentswithscal-
able long-term memory.arXiv preprint arXiv:2504.19413.
Cormack, G. V.; Clarke, C. L.; and Buettcher, S. 2009. Re-
ciprocal rank fusion outperforms condorcet and individual
rank learning methods. InProceedings of the 32nd interna-
tional ACM SIGIR conference on Research and development
in information retrieval, 758–759.
Feng,J.;Xu,B.;Chen,J.;Dai,M.;Wu,C.;Li,H.;Zeng,B.;
Xie, Y.; Liang, H.; Lu, M.; et al. 2026. M2a: Multimodal
memoryagentwithdual-layerhybridmemoryforlong-term
personalizedinteractions.arXiv preprint arXiv:2602.07624.
Jeong, S.; Baek, J.; Cho, S.; Hwang, S. J.; and Park, J. C.
2024. Adaptive-rag: Learning to adapt retrieval-augmented
largelanguagemodelsthroughquestioncomplexity. InPro-
ceedings of the 2024 Conference of the North American
Chapter of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long Papers),
7036–7050.
Jiang,Z.;Xu,F.F.;Gao,L.;Sun,Z.;Liu,Q.;Dwivedi-Yu,J.;
Yang, Y.; Callan, J.; and Neubig, G. 2023. Active retrieval
augmented generation. InProceedings of the 2023 confer-
ence on empirical methods in natural language processing,
7969–7992.
Kwon, W.; Li, Z.; Zhuang, S.; Sheng, Y.; Zheng, L.; Yu,
C.H.;Gonzalez,J.;Zhang,H.;andStoica,I.2023. Efficient
memorymanagementforlargelanguagemodelservingwith
pagedattention. InProceedings of the 29th symposium on
operating systems principles, 611–626.
Lewis, P.; Perez, E.; Piktus, A.; Petroni, F.; Karpukhin, V.;
Goyal,N.;Küttler,H.;Lewis,M.;Yih,W.-t.;Rocktäschel,T.;
et al. 2020. Retrieval-augmented generation for knowledge-
intensivenlptasks.Advances in neural information process-
ing systems, 33: 9459–9474.
Lewis, P.; Wu, Y.; Liu, L.; Minervini, P.; Küttler, H.; Pik-
tus, A.; Stenetorp, P.; and Riedel, S. 2021. PAQ: 65 million
probably-asked questions and what you can do with them.
Transactions of the Association for Computational Linguis-
tics, 9: 1098–1115.
Li, M.; Zhang, Y.; Long, D.; Chen, K.; Song, S.; Bai, S.;
Yang, Z.; Xie, P.; Yang, A.; Liu, D.; et al. 2026. Qwen3-
VL-EmbeddingandQwen3-VL-Reranker:AUnifiedFrame-
workforState-of-the-ArtMultimodalRetrievalandRanking.
arXiv preprint arXiv:2601.04720.
Long,L.;He,Y.;Ye,W.;Pan,Y.;Lin,Y.;Li,H.;Zhao,J.;and
Li,W.2025. Seeing,listening,remembering,andreasoning:
Amultimodalagentwithlong-termmemory.arXiv preprint
arXiv:2508.09736.
Madaan, A.; Tandon, N.; Gupta, P.; Hallinan, S.; Gao, L.;
Wiegreffe, S.; Alon, U.; Dziri, N.; Prabhumoye, S.; Yang,
Y.; et al. 2023. Self-refine: Iterative refinement with self-
feedback.Advances in neural information processing sys-
tems, 36: 46534–46594.
Maharana, A.; Lee, D.-H.; Tulyakov, S.; Bansal, M.; Bar-
bieri, F.; and Fang, Y. 2024. Evaluating very long-term
conversational memory of llm agents. InProceedings of the
62nd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 13851–13870.
Neeser, A.; Latimer, K.; Khatri, A.; Latimer, C.; and Ra-
makrishnan,N.2025. QuOTE:Question-OrientedTextEm-
beddings.arXiv preprint arXiv:2502.10976.
Packer, C.; Fang, V.; Patil, S.; Lin, K.; Wooders, S.; and
Gonzalez, J. 2023. MemGPT: towards LLMs as operating
systems. ArXiv.
Papineni, K.; Roukos, S.; Ward, T.; and Zhu, W.-J. 2002.
Bleu: a method for automatic evaluation of machine trans-
lation. InProceedings of the 40th annual meeting of the
Association for Computational Linguistics, 311–318.
Park, J. S.; O’Brien, J.; Cai, C. J.; Morris, M. R.; Liang,
P.; and Bernstein, M. S. 2023. Generative agents: Interac-
tive simulacra of human behavior. InProceedings of the
36th annual acm symposium on user interface software and
technology, 1–22.
Radford, A.; Kim, J. W.; Hallacy, C.; Ramesh, A.; Goh,
G.; Agarwal, S.; Sastry, G.; Askell, A.; Mishkin, P.; Clark,
J.; et al. 2021. Learning transferable visual models from
natural language supervision. InInternational conference
on machine learning, 8748–8763. PmLR.
Rajpurkar, P.; Zhang, J.; Lopyrev, K.; and Liang, P. 2016.
Squad: 100,000+ questions for machine comprehension of
text. InProceedings of the 2016 conference on empirical
methods in natural language processing, 2383–2392.
Ren, X.; Wang, Z.; Du, Y.; Xie, Z.; Liu, C.; Yang, X.;
Feng, H.; Pan, W.; Zheng, T.; Xu, B.; et al. 2026. Mem-
lens: Benchmarking multimodal long-term memory in large
vision-language models.arXiv preprint arXiv:2605.14906.
Shinn, N.; Cassano, F.; Gopinath, A.; Narasimhan, K.; and
Yao, S. 2023. Reflexion: Language agents with verbal re-
inforcement learning.Advances in neural information pro-
cessing systems, 36: 8634–8652.
Song,D.;Chen,S.;Chen,G.H.;Yu,F.;Wan,X.;andWang,
B. 2024. Milebench: Benchmarking mllms in long context.
arXiv preprint arXiv:2404.18532.
Trivedi, H.; Balasubramanian, N.; Khot, T.; and Sabharwal,
A.2023. Interleavingretrievalwithchain-of-thoughtreason-
ing for knowledge-intensive multi-step questions. InPro-
ceedings of the 61st annual meeting of the association for
computational linguistics (volume 1: long papers), 10014–
10037.
Tschannen, M.; Gritsenko, A.; Wang, X.; Naeem, M. F.;
Alabdulmohsin, I.; Parthasarathy, N.; Evans, T.; Beyer, L.;
Xia, Y.; Mustafa, B.; et al. 2025. Siglip 2: Multilingual
vision-language encoders with improved semantic under-
standing, localization, and dense features.arXiv preprint
arXiv:2502.14786.
Wang, C.; Tatwawadi, K.; Brockschmidt, M.; Huang, P.-S.;
Mao,Y.;Polozov,O.;andSingh,R.2018. Robusttext-to-sql
generation with execution-guided decoding.arXiv preprint
arXiv:1807.03100.
Wang, Z.; Yu, W.; Ren, X.; Zhang, J.; Zhao, Y.; Saxena,
R.; Cheng, L.; Wong, G.; See, S.; Minervini, P.; et al. 2026.

Mmlongbench:Benchmarkinglong-contextvision-language
models effectively and thoroughly.Advances in Neural In-
formation Processing Systems, 38.
Xu, W.; Liang, Z.; Mei, K.; Gao, H.; Tan, J.; and Zhang, Y.
2026. A-mem:Agenticmemoryforllmagents.Advances in
Neural Information Processing Systems, 38: 17577–17604.
Yao,S.;Zhao,J.;Yu,D.;Shafran,I.;Narasimhan,K.R.;and
Cao, Y. 2022. React: Synergizing reasoning and acting in
language models. InNeurIPS 2022 Foundation Models for
Decision Making Workshop.
Zhai, X.; Mustafa, B.; Kolesnikov, A.; and Beyer, L. 2023.
Sigmoid loss for language image pre-training. InProceed-
ings of the IEEE/CVF international conference on computer
vision, 11975–11986.
Zhang, Y.; Li, M.; Long, D.; Zhang, X.; Lin, H.; Yang, B.;
Xie, P.; Yang, A.; Liu, D.; Lin, J.; et al. 2025. Qwen3 em-
bedding: Advancing text embedding and reranking through
foundation models.arXiv preprint arXiv:2506.05176.
