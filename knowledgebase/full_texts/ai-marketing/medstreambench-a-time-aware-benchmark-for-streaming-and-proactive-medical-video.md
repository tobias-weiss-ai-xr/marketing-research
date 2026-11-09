---
title: 'MedStreamBench: A Time-Aware Benchmark for Streaming and Proactive Medical Video Understanding'
url: https://arxiv.org/abs/2607.01751
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Yuan Wang
- Shujian Gao
- Songtao Jiang
- Zhengyu Hu
- Zuozhu Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.01751
pages: 10
chars: 36444
fetched_at: '2026-11-08T13:26:23+00:00'
kb_version: 1
---

# MedStreamBench: A Time-Aware Benchmark for Streaming and Proactive Medical Video Understanding

arXiv:2607.01751v1  [cs.CV]  2 Jul 2026
MedStreamBench: A Time-Aware Benchmark for Streaming and
Proactive Medical Video Understanding
YuanWang 1,4,ShujianGao 2,4,SongtaoJiang 1,ZhengyuHu 3,ZuozhuLiu 1
1College of Computer Science and Technology, Zhejiang University, Zhejiang, China
2Insititute of Trustworthy Embodied AI, Fudan University, Shanghai, China
3Department of Electrical and Computer Engineering, Carnegie Mellon University, Pennsylvania, USA
4Equal Contribution.
Abstract
Existing medical video benchmarks primarily evaluate whether a model produces the correct answer, but rarely assess
whether it answers at theright time. In real clinical settings, AI systems must decide not only what to predict,
but also when to answer, defer judgment, or proactively raise alerts. This creates a critical gap between benchmark
evaluation and deployment requirements. We presentMedStreamBench, a benchmark fortime-aware medical video
understanding. MedStreamBench integrates22 medical datasetsand5,419 QA instancesacross four temporal
settings: retrospective, present, future, and proactive. Unlike conventional benchmarks that assume full-video access,
MedStreamBench restricts models to temporally bounded evidence windows and supports both single-turn and streaming
evaluation. We further introduce aproactive monitoringsetting that requires models to determine whether and when
clinically relevant alerts should be triggered. Beyond answer correctness, MedStreamBench evaluates temporal behavior
through responsiveness and post-evidence stability. Experiments on leading general-purpose and medical vision-language
models reveal a substantial gap between offline recognition and temporally grounded decision-making, with performance
dropping markedly in streaming and proactive settings. Our benchmark is available at Venn2024/MedStreamBench.
Keywords
Medical Video Benchmark, Streaming Video Understanding, Temporal Question Answering, Proactive Monitoring
Article informations
©2026 Yuan and Shujian. License: CC-BY 4.0
Corresponding author: zuozhuliu@intl.zju.edu.cn
1. Background
M
edicalvideo understanding is becoming increas-
ingly important for surgical intelligence, endo-
scopic screening, procedural education, and real-
time clinical decision support. Unlike static medical images,
medical videos encode evolving procedural context: in-
struments enter and leave the field, anatomical exposure
changes over time, lesions may appear only transiently, and
safety-relevant events often depend on the temporal order
of visual evidence. Consequently, a clinically useful medi-
cal vision–language model should not only recognize what
is visible, but also determinewhensufficient evidence be-
comes available,whento abstain, andwhento alert. This
temporal discipline is essential in scenarios such as polyp
screening, surgical workflow monitoring, view-quality as-
sessment, and skill coaching, where premature conclusions
can be misleading and delayed responses can reduce clinical
utility.
Recent video-language benchmarks have substantially
advanced the evaluation of multimodal large language mod-
els on video understanding, including long-video reasoning
and online video analysis (Fu et al., 2025; Wu et al., 2024;
Li et al., 2025; Lin et al., 2024). However, most exist-
ing benchmarks assume either access to a complete video
or a fixed clip, and primarily measure whether the final
answer is semantically correct. Such offline evaluation is
insufficient for medical streaming video analysis, where
models must respect the information actually available at
a specified time point. In parallel, medical and surgical
datasets have enabled progress in phase recognition, instru-
ment detection, action triplet recognition, polyp detection,
capsule-endoscopy abnormality recognition, and surgical vi-
sual question answering (Stauder et al., 2016; Nwoye et al.,
2023; Smedsrud et al., 2021; Seenivasan et al., 2022; He
et al., 2024; Jiang et al., 2025a; Wang et al., 2025, 2026;
Jiang et al., 2025b). Yet these resources typically evaluate
recognition or question answering in an offline setting, and
do not explicitly test whether a model can answer, defer, or
alert at the correct moment under a strict evidence window.
1337

Yuan and Shujian, 2026
Table 1: Comparison of MedStreamBench with representative surgical and medical video resources. We compare each
resource by source breadth (#DS), evaluation protocol, and coverage of the four temporal task modes.
Benchmark #DS Protocol Temporal Tasks
Eval Unit Prefix-Only Streaming Retrospective Present Future Proactive
Classical Surgical Datasets
Cholec80 1 frame / video× ×✓ ✓× ×
M2CAI16-Workflow 1 frame / video× ×✓ ✓× ×
JIGSAWS 1 gesture / video× ×✓ ✓× ×
Recent Surgical / Medical Video Resources
LLaVA-Surg 1 clip / video× ×✓ ✓× ×
SurgPub-Video 1 clip / video× ×✓ ✓× ×
SurgOnAir 1 streaming video✓ ✓×✓× ×
MedHorizon 1 long video× ×✓ ✓× ×
MedStreamBench
(Ours)
22 long video / stream ✓ ✓ ✓ ✓ ✓ ✓
We introduceMedStreamBench, a diverse tempo-
ral benchmark for medical video question answering. To
the best of our knowledge, MedStreamBench is the first
benchmark designed to evaluatestreamingmedical video
understanding, and the first to formulate aproactivemed-
ical video question-answering paradigm. In the stream-
ing paradigm, the same question is asked over progres-
sively growing visual prefixes, and a model must output
unanswerable until the evidence becomes sufficient. In
the proactive paradigm, the model continuously monitors
a medical video stream and must respond with one of
no alert, uncertain, or alert: <reason> , triggering
an alert only when sufficient visual evidence appears. These
two paradigms directly reflect clinically meaningful require-
ments: a model should avoid leaking future information,
avoid unsupported early alarms, detect time-sensitive find-
ings or workflow events promptly, and maintain stable be-
havior once evidence is available.
As summarized in Table 1, recent medical video re-
sources such as LLaVA-Surg (Li et al., 2024), SurgPub-
Video (Li et al., 2026), SurgOnAir (He et al., 2026), and
MedHorizon (Du et al., 2026) extend evaluation beyond
classical phase- or clip-level recognition; however, they still
provide limited coverage of prefix-only answering, stream-
ing evaluation, or future and proactive temporal reason-
ing. MedStreamBench is designed to be broad and com-
prehensive. It integrates 22 medical video and image-
sequence datasets spanning laparoscopic surgery, open
surgery, robotic skill assessment, hysterectomy, pituitary
surgery, bariatric bypass surgery, colonoscopy, gastrointesti-
nal endoscopy, and capsule endoscopy. The benchmark
contains 5,419 question-answering records, including 4,663
single-turn items and 756 streaming items, which expand
to 3,369 per-round streaming inference jobs. Its temporal
taxonomy covers four complementary modes:retrospective
questions about past evidence,presentquestions about the
current visual state,futurequestions that require prediction
or deferred answerability from partial evidence, andproac-
tivemonitoring questions that require timely alerts. The
benchmark also contains both closed and open-ended ques-
tions, and combines original annotations, category labels,
hybrid label-grounded generation, and conservative model-
assisted mining to cover both high-confidence label-based
tasks and visually grounded open-ended reasoning.
A central design principle of MedStreamBench is that
every question is tied to an explicit visual evidence window.
For single-turn tasks, the input is restricted to[ tq−w, tq],
where tq is the query time and w is the context window.
For streaming future and proactive tasks, each round is
evaluated only on[ tq, tc], where tc is the current time for
that round. This design prevents temporal leakage and
converts medical video question answering from an offline
recognition problem into a time-aware decision problem.
For open-ended questions, MedStreamBench further uses
fine-grained judge rubrics that separately assess semantic
correctness, evidence grounding, and safety, improving fair-
ness and reducing ambiguity compared with a single coarse
match criterion. In particular, the benchmark asks: given
only the frames available so far, should the model answer,
abstain, remain uncertain, or raise an alert?
To support scalable construction and reproducible eval-
uation, we develop two accompanying systems. First, the
MedStreamBench data engineharmonizes heterogeneous
medical datasets into a unified temporal QA schema. It
converts heterogeneous medical data, including structured
annotations, directory labels, and weakly labeled videos,
into unified temporal QA items, and then validates and ma-
terializes the final dataset-scoped benchmark files. Second,
theMedStreamBench inference engineexpands bench-
mark records into per-window or per-round jobs, samples
visual inputs under a fixed temporal protocol, supports local
and API-based multimodal inference, and evaluates predic-
1338

MedStreamBench
Figure 1: Overview of MedStreamBench as a resource. The benchmark integrates heterogeneous medical video and
image-sequence datasets into a unified time-aware QA format with explicit evidence windows, multiple temporal modes,
and both single-turn and streaming evaluation settings.
tions using content correctness, streaming responsiveness,
and post-evidence stability. This separation between data
construction and inference makes the benchmark extensible
to new datasets, models, and temporal protocols.
Our contributions are threefold.
• Time-aware formulation.We propose a time-aware
medical video QA formulation that unifies retrospective,
present, future, streaming, and proactive evaluation under
explicit evidence-window constraints.
• Diverse benchmark.We release a diverse benchmark
built from 22 medical datasets, covering a wide range of
procedures, anatomies, visual findings, task types, label
sources, and temporal reasoning modes.
• Reproducible engines.We provide data and inference
engines that enable reproducible benchmark generation,
per-round streaming evaluation, and metrics for both
answer correctness and temporal behavior.
2. Summary
MedStreamBench is a time-aware benchmark for medical
video question answering with explicit evidence windows,
four temporal modes, and both single-turn and streaming
evaluation. As illustrated in Figure 1 and Figure 2, it in-
tegrates 22 source datasets into a unified JSONL schema
that records the question, answer, temporal specification,
task mode, response protocol, and label provenance. The
current release contains 5,419 QA records, including 4,663
single-turn items and 756 streaming items, which expand
to 3,369 round-level inference jobs during evaluation. The
benchmark combines annotation-derived, directory-derived,
hybrid, and conservatively model-assisted items to broaden
coverage while retaining provenance information for down-
stream analysis.
2.1 AI-Readiness
The benchmark is organized in a unified machine-readable
schema with explicit temporal metadata, including query
time, input range, and round-level streaming structure
where applicable. For open-ended questions, MedStream-
Bench additionally provides fine-grained judge rubrics that
separately assess semantic correctness, evidence grounding,
and safety, enabling more consistent LLM-as-judge evalu-
ation than a single coarse matching criterion. In addition
to benchmark files, MedStreamBench is paired with a stan-
dardized inference and evaluation workflow that fixes frame
sampling, prompt construction, and temporal scoring, mak-
ing it suitable for controlled comparison of model behavior
under evidence-constrained medical video understanding.
3. Discussion
3.1 Strengths
MedStreamBench introduces a temporal evaluation setting
that is largely absent from existing medical video resources.
Its main strengths are explicit evidence-window control,
broad multi-source coverage, and evaluation of both se-
mantic correctness and temporally appropriate response
behavior.
1339

Yuan and Shujian, 2026
Figure 2: Overview of the MedStreamBench pipeline. The pipeline consists of three stages: temporal surgical data
preparation, label-grounded QA construction, and benchmark validation. Source videos are standardized and paired with
label-derived, folder-derived, or weakly mined supervision signals, which are converted into temporally aligned QA pairs
with different quality levels. Candidate items are then aggregated, refined, and verified through AI-assisted judging and
expert checking before final benchmark evaluation.
3.2 Limitations
The underlying source datasets differ substantially in anno-
tation granularity, label quality, visual scope, and temporal
density, and some benchmark items are derived from direc-
tory labels, hybrid generation, or weak supervision rather
than fully expert-authored QA annotation. In addition, not
all weakly supervised or model-assisted samples received ex-
haustive manual visual review, and the fixed frame-sampling
protocol may underrepresent brief events.
3.3 Bias and Representativeness
As a multi-source benchmark, MedStreamBench inherits
distributional biases from its constituent datasets, including
differences in procedure types, devices, recording styles,
annotation practices, and case distributions. Aggregate
scores should therefore be interpreted together with dataset-
level or domain-level analyses, especially when comparing
behavior across surgical, endoscopic, and skill-assessment
settings.
3.4 Responsible Use
MedStreamBench is intended as a research benchmark for
evaluating time-aware medical video understanding systems.
It should not be interpreted as a clinical decision-support
system or as a substitute for expert judgment. Weakly
supervised and model-assisted items are included to broaden
evaluation coverage, but they should not be treated as
expert-certified clinical labels. Any deployment-oriented use
would require additional task-specific validation, prospective
testing, and appropriate human oversight.
4. Resource Availability
4.1 Data Release
The benchmark is released as dataset-scoped JSONL files
following a unified temporal QA schema and is hosted
at Venn2024/MedStreamBench. The release provides de-
rived QA annotations and metadata under the Apache
License 2.0, while the underlying image and video assets
remain governed by the corresponding upstream sources.
4.2 Code Release and Access Policy
MedStreamBench is accompanied by a data construction
pipeline and an inference/evaluation pipeline supporting
benchmark generation, schema validation, frame sampling,
prompt construction, streaming round expansion, and met-
ric computation. Access to original videos or images remains
subject to the terms, licenses, and availability conditions
of the corresponding upstream datasets. The benchmark
release therefore distributes derived QA JSONL files and
associated metadata, but does not redistribute the original
media unless permitted by the upstream source. When
explicitly allowed by the corresponding upstream licenses
or access terms, selected source media may also be redis-
tributed or linked as part of the benchmark release, subject
to those upstream conditions. Table 2 summarizes the
current access status and license terms for the 22 source
datasets covered by MedStreamBench.
4.3 Intended Use
The intended use of MedStreamBench is the evaluation of
medical vision–language models under temporally restricted
1340

MedStreamBench
Table 2: Upstream access or license terms for the source datasets covered by MedStreamBench. The MedStreamBench
release is intended to contain derived JSONL annotations and metadata only; original images and videos are obtained
separately from the upstream sources. When a precise formal license could not be verified reliably from the source paper
or project materials, we conservatively report ‘upstream terms’ or ‘challenge terms’ rather than infer a specific license.
Dataset Access Dataset Access Dataset Access
cholec80 upstream terms M2CAI16-Workflow challenge terms EndoVis2019 challenge terms
AutoLapora public release LDPolypVideo upstream terms PitVis public release
simsurgskill 2021 public release kvasir-capsule public release hyper-kvasir public release
Colonoscopic-web upstream terms CVC-ClinicDB public release AlxSuture upstream terms
AVOS public release Surgical-phase will release JIGSAWS public release
CholecT45 public release CholecT50 public release HeiChole challenge terms
BernBypass70 upstream terms MultiBypass140 upstream terms private data will release
Colonoscopic-addi upstream terms
visual evidence. Representative use cases include benchmark
comparison, study of answerability under partial observation,
evaluation of streaming response behavior, and research
on proactive monitoring in medical video analysis. The
resource is not intended to serve as a stand-alone clinical
system.
5. Methods
5.1 Benchmark Overview
MedStreamBench is a time-aware medical video question-
answering benchmark in which each item is associated with
a visual source, an explicit temporal evidence window, a
question, a reference answer, and metadata describing task
type and label provenance. The release is stored as dataset-
scoped JSONL files and covers both closed-choice and
open-ended questions across retrospective, present, future,
and proactive settings.
Each item follows a compact unified schema:
x= (v,q,a,τ,m,r,s),(1)
where v denotes the visual source, q is the question, a is
the answer or reference answer, τ denotes the temporal
specification, m denotes the task mode, r contains evalua-
tion rubrics or response protocols, and s stores source and
quality metadata. The temporal specification includes the
query time tq, the context window length w, and the input
range[ ts,t e]. For streaming tasks, each item additionally
contains a sequence of rounds with current time tc, round-
specific input range, expected output, and answerability
flag.
5.2 Data Construction Pipeline
The MedStreamBench data engine converts heterogeneous
medical datasets into a unified temporal QA format. As
illustrated in Figure 2, the pipeline is organized into three
aligned stages: temporal surgical data preparation, label-
grounded QA construction, and benchmark validation.
Temporal surgical data preparation.We first standard-
ize the source videos or image sequences and align them
with available supervision signals. For structured datasets,
these signals come from original annotations such as phases,
tool labels, actions, masks, bounding boxes, or skill metrics;
for other sources, they may also come from directory-defined
categories or weak-label mining. Each target contains a
visual source, a task specification, an answer signal, and an
initial temporal window. For video datasets, timestamps
are converted into seconds using dataset-specific metadata,
whereas image-only datasets use the temporal range[0,0].
Label-grounded QA construction.The aligned supervi-
sion signals are then converted into temporally grounded
QA items. For label-grounded tasks, deterministic targets
are rewritten as natural-language closed or open-ended ques-
tions while preserving the answer. For weakly labeled or
unlabeled videos, the engine conservatively mines candidate
QA items from visible findings, procedural states, tool inter-
actions, or screening alerts. To broaden temporal coverage,
this stage also produces present, future, streaming, and
proactive items rather than only retrospective recognition
examples.
Benchmark validation and materialization.The result-
ing candidate items are aggregated, refined, and validated
before release. The validator checks schema completeness,
question and answer fields, formatting, media paths, tempo-
ral fields, and streaming rounds, and it enforces the temporal
contract that single-turn items end at tq while streaming
items use round-specific windows of the form[ tq,t c]. Proac-
tive items are additionally constrained to the response space
no alert, uncertain, or alert: <reason> . Accepted
items are then materialized into final dataset-scoped bench-
mark files for downstream inference and evaluation.
5.3 Temporal Task Formulation
MedStreamBench defines four temporal modes and two
task modes. Single-turn items produce one model call per
item, whereas streaming items produce one model call per
1341

Yuan and Shujian, 2026
Figure 3: Illustration of the four temporal reasoning settings in MedStreamBench. Given a surgical video timeline,
a decision point Tq defines the latest observable evidence available to the model. Retrospective questions require
understanding past events within the observation window[ Tq−w,T q], while present questions focus on the current
surgical state near Tq. Future questions evaluate whether models can predict upcoming events before the first answerable
moment Tevent using only historical observations. Proactive streaming tasks further require the model to continuously
monitor an evolving video prefix[T q,T k c ]and trigger alerts only when sufficient evidence becomes visible.
Table 3: Evaluation metrics used in MedStreamBench.
Metric Interpretation
Content
correctness
(C)
Semantic correctness under the
evidence-constrained input. For closed
questions, it is based on normalized exact
match with optional semantic fallback; for
open questions, it combines correctness,
evidence grounding, and safety.
Responsiveness
(R)
Temporal accuracy of the first positive answer
or alert relative to the expected answerable or
critical time. Early, delayed, and missed
responses are penalized.
Stability (S) Post-evidence consistency after the item
becomes answerable, measuring whether the
model remains positive in later rounds rather
than reverting to abstention or omission.
Overall score
(O)
Task-level summary score. For single-turn
items,O=C; for streaming future and
proactive items, O = 0.7 C + 0.3 R, prioritizing
correctness while rewarding timely response.
round.
Retrospective and present single-turn QA.For retro-
spective and present questions, the model receives a context
window ending at the query time:
I= [max(0,t q−w), t q].(2)
Retrospective questions ask about events or states within
the window, whereas present questions focus on the visual
state near tq. If the available evidence is insufficient, the
expected behavior isunanswerable.
Future single-turn QA.Future single-turn questions use
the same input window:
I= [max(0,t q−w), t q],(3)
but ask about an event or state after tq. The model
must reason from the available context only and return
unanswerable when the future event is not yet predictable.
Future streaming QA.For future streaming questions,
the item is evaluated over a sequence of rounds. At round
k, the model receives only the prefix:
Ik = [t q, t(k) c ],(4)
where t(k) c is the current time for that round. Before
the evidence becomes sufficient, the expected output is
unanswerable; once the target event becomes answerable,
the model should answer and remain stable in subsequent
rounds.
Proactive streaming QA.Proactive questions also use
round-specific prefixes[ tq,t (k) c ], but the response space is
constrained to:
yk∈{no alert,uncertain,alert: <reason>}.(5)
The model should alert only when sufficient evidence ap-
pears, while usingno alertoruncertainbeforehand.
5.4 Inference Protocol
The MedStreamBench inference engine expands each bench-
mark item into one or more inference jobs. Single-turn items
1342

MedStreamBench
Table 4: Main benchmark results on MedStreamBench across the four temporal modes. For retrospective and present
settings, we report content accuracy only. For future and proactive settings, we report responsiveness and stability.
Baseline Retrospective Present Future Proactive Overall
Content Content Content Resp. Stab. Content Resp. Stab. Score
Closed-source
Gemini-2.5-Pro0.3428 0.4140 0.4384 0.36360.6927 0.61580.4494 0.4742 0.3728
Open-source
Qwen3-VL-4B 0.2255 0.3491 0.4046 0.1870 0.34150.64280.2301 0.2114 0.2701
Qwen3-VL-8B 0.2008 0.2898 0.3260 0.0912 0.3293 0.6229 0.1499 0.1337 0.2324
Qwen2.5-VL-7B 0.2413 0.3446 0.3656 0.0533 0.4635 0.6255 0.0547 0.0525 0.2662
InternVL3.5-8B 0.2536 0.3461 0.3847 0.0710 0.3934 0.4441 0.0899 0.08130.2713
LLaVA-OneVision-7B 0.2498 0.2888 0.2890 0.0746 0.8142 0.5470 0.0579 0.0595 0.2572
Medical-domain
HuluMed-4B 0.2231 0.2868 0.4327 0.1456 0.2399 0.4742 0.2088 0.2248 0.2578
HuluMed-7B 0.2298 0.2798 0.3851 0.1425 0.1961 0.6258 0.0677 0.07230.2601
Lingshu-7B 0.2329 0.3302 0.3417 0.09530.71800.6302 0.0514 0.0514 0.2586
Content: content accuracy.Resp.: responsiveness score.Stab.: stability score.
yield one job, whereas future and proactive streaming items
yield one job per round.
For video inputs, the engine samples frames uniformly
at one frame every 2 seconds within the job-specific input
range, including the endpoint when needed so that evidence
at tq or tc remains visible. For image-sequence datasets,
the input range is interpreted analogously as a frame-index
interval. The textual prompt specifies the task mode, tem-
poral mode, query time, input range, and the constraint
that no evidence beyond the designated endpoint may be
used. Future streaming prompts require unanswerable
before sufficient evidence appears, while proactive prompts
restrict the response space to no alert, uncertain, or
alert: <reason>.
5.5 Evaluation Metrics
MedStreamBench evaluates both answer correctness and
temporal behavior. Table 3 summarizes the interpretation
of the reported metrics; below we specify the corresponding
scoring rules.
Content correctness.For closed questions, predictions
are evaluated by normalized exact match, with optional
judge fallback for semantically equivalent mismatches. For
open-ended questions, a rubric-based judge scores correct-
ness, evidence grounding, and safety. The resulting score is
normalized to[0,1]:
C= scorrect +s ground +s safety
5 ,(6)
where scorrect∈{ 0, 1, 2}, sground∈{ 0, 1, 2}, and ssafety∈
{0, 1}. For streaming items, content correctness is averaged
over rounds.
Responsiveness.For future and proactive streaming items,
responsiveness measures whether the first positive response
occurs near the expected response time. For future stream-
ing tasks, a positive response is any answer other than
unanswerable; for proactive tasks, it is an alert. Let t∗
be the expected response time, ˆt the first predicted posi-
tive time, and δ the tolerance. A prediction receives the
maximum responsiveness score if
|ˆt−t ∗|≤δ.(7)
Missed responses receive zero responsiveness, and prema-
ture or delayed responses are penalized according to their
temporal distance fromt ∗.
Stability.For streaming tasks, stability measures whether
the model remains positive after the item becomes answer-
able:
S= 1 |K≥t∗| ∑ k∈K≥t∗ 1[y k is positive],(8)
whereK≥t∗ denotes rounds at or after the expected response
time.
Overall score.For single-turn items, the overall score is
the content score:
O=C.(9)
For streaming future and proactive items, the overall score
combines correctness and responsiveness:
O= 0.7C+ 0.3R,(10)
whereRis the responsiveness score.
1343

Yuan and Shujian, 2026
Figure 4: Organ-level aggregated content performance across baseline models. Each cell reports the sample-count-
weighted average content score over datasets belonging to the same organ or procedural group. Darker teal indicates
better performance. The best model in each column is marked with a star and highlighted by a thin outline.
6. Validation
6.1 Baseline description
Table 4 reports representative baselines from three groups:
a closed-source model (Team et al., 2023), five general-
domain open-source models (Bai et al., 2025; Zhu et al.,
2025), and three medical-domain models (Xu et al., 2025;
Jiang et al., 2025a). All experiments were conducted on
NVIDIA H100 GPUs under the same benchmark protocol.
6.2 Main Results
Table 4 summarizes initial baseline results on MedStream-
Bench. Together with the metric definitions in Table 3,
it separates semantic accuracy from temporal responsive-
ness and stability across retrospective, present, future, and
proactive settings. This separation makes it possible to
distinguish models that perform well in offline recognition
from models that are also temporally disciplined under
prefix-only evidence. The overall score provides a compact
benchmark-level summary by aggregating item scores un-
der the task-specific evaluation rule defined in Section 4.2.
Across the evaluated models, Gemini-2.5-Pro achieves the
strongest overall performance, while InternVL3.5-8B is the
best-performing open-source model and Lingshu-7B yields
the strongest overall score among the medical-domain mod-
els. These aggregate results are useful for high-level com-
parison, but they should be interpreted together with the
mode-specific columns because temporal strengths are not
uniformly distributed across 4 task modes.
6.3 Organ-level analysis
Figure 4 aggregates dataset-level content performance by
organ or procedural domain using sample-count-weighted
averaging. Gemini-2.5-Pro achieves the strongest perfor-
Figure 5: Manual spot-check agreement between the AI-
generated answer and two human annotators.
mance across most organ groups, whereas the best open
or medical-domain models emerge in more specialized re-
gions, including InternVL3.5-8B on the GI tract and capsule
group, Qwen2.5-VL-7B on multi-organ open surgery, and
HuluMed-4B on MIS robotic surgery. This heterogeneous
pattern shows that benchmark performance is not uniform
across clinical domains and motivates organ-level analysis
beyond a single global average. Figure 1 and Figure 3
provide the corresponding resource-level and temporal-task
context for interpreting these benchmark-level quantitative
results.
6.4 Human Check
As a preliminary quality check for model-assisted items,
we compared AI-generated answers with judgments from
two independent human annotators on a random sample.
Figure 5 shows agreement with both annotators in 60%
of cases, with one annotator in 25%, and with neither
annotator in 15%.
1344

MedStreamBench
Acknowledgments
This work is supported by the ”Pioneer” and ”Leading
Goose” R&D Program of Zhejiang (Grant no. 2025C01128),
and the ZJU-Angelalign R&D Center for Intelligence Health-
care.
Conflicts of Interest
We declare we don’t have conflicts of interest.
References
Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui
Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang
Gao, Chunjiang Ge, et al. Qwen3-vl technical report.
arXiv preprint arXiv:2511.21631, 2025.
Bodong Du, Bowen Liu, Yang Yu, Xinpeng Ding, Zhiheng
Wu, Shuning Wang, Shuo Nie, Naiming Liu, Qifeng Chen,
Yangqiu Song, et al. Medhorizon: Towards long-context
medical video understanding in the wild.arXiv preprint
arXiv:2605.06537, 2026.
Chaoyou Fu, Yuhan Dai, Yongdong Luo, Lei Li, Shuhuai
Ren, Renrui Zhang, Zihan Wang, Chenyu Zhou, Yunhang
Shen, Mengdan Zhang, Peixian Chen, Yanwei Li, Shaohui
Lin, Sirui Zhao, Ke Li, Tong Xu, Xiawu Zheng, Enhong
Chen, Caifeng Shan, Ran He, and Xing Sun. Video-MME:
The first-ever comprehensive evaluation benchmark of
multi-modal LLMs in video analysis. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), 2025. arXiv:2405.21075.
Jingyi He, Yue Zhou, Long Bai, Kun Yuan, Nassir Navab,
and Yuan Bi. Surgonair: Hierarchy-aware real-time surgi-
cal video commentary.arXiv preprint arXiv:2605.21132,
2026.
Runlong He, Mengya Xu, Adrito Das, Danyal Z. Khan,
Sophia Bano, Hani J. Marcus, Danail Stoyanov,
Matthew J. Clarkson, and Mobarakol Islam. PitVQA:
Image-grounded text embedding LLM for visual question
answering in pituitary surgery. InMedical Image Com-
puting and Computer Assisted Intervention (MICCAI),
pages 488–498. Springer Nature Switzerland, 2024. .
Songtao Jiang, Yuan Wang, Sibo Song, Tianxiang Hu,
Chenyi Zhou, Bin Pu, Yan Zhang, Zhibo Yang, Yang
Feng, Joey Tianyi Zhou, et al. Hulu-med: A transparent
generalist model towards holistic medical vision-language
understanding.arXiv preprint arXiv:2510.08668, 2025a.
Songtao Jiang, Yuan Wang, Sibo Song, Yan Zhang, Zi-
jie Meng, Bohan Lei, Jian Wu, Jimeng Sun, and
Zuozhu Liu. Omniv-med: Scaling medical vision-language
model for universal visual understanding.arXiv preprint
arXiv:2504.14692, 2025b.
Jiajie Li, Garrett Skinner, Gene Yang, Brian R Quaranto,
Steven D Schwaitzberg, Peter CW Kim, and Jinjun
Xiong. Llava-surg: towards multimodal surgical assis-
tant via structured surgical video learning.arXiv preprint
arXiv:2408.07981, 2024.
Yaoqian Li, Xikai Yang, Dunyuan Xu, Yang Yu, Litao Zhao,
Xiaowei Hu, Jinpeng Li, and Pheng-Ann Heng. Surgpub-
video: A comprehensive surgical video framework for
enhanced surgical intelligence in vision-language model.
InProceedings of the AAAI Conference on Artificial
Intelligence, volume 40, pages 6628–6635, 2026.
Yifei Li, Junbo Niu, Ziyang Miao, Chunjiang Ge, Yuanhang
Zhou, Qihao He, Xiaoyi Dong, Haodong Duan, Shuan-
grui Ding, Rui Qian, Pan Zhang, Yuhang Zang, Yuhang
Cao, Jiaqi Wang, and Dahua Lin. OVO-bench: How far
is your video-LLMs from real-world online video under-
standing? InProceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition (CVPR),
2025. arXiv:2501.05510.
Junming Lin, Zheng Fang, Chi Chen, Zihao Wan, Fuwen
Luo, Peng Li, Yang Liu, and Maosong Sun. Streaming-
Bench: Assessing the gap for MLLMs to achieve stream-
ing video understanding.arXiv preprint arXiv:2411.03628,
2024.
Chinedu Innocent Nwoye, Tong Yu, Saurav Sharma, Aditya
Murali, Deepak Alapatt, Armine Vardazaryan, et al.
CholecTriplet2021: A benchmark challenge for surgical
action triplet recognition.Medical Image Analysis, 86:
102803, 2023. .
Lalithkumar Seenivasan, Mobarakol Islam, Adithya K. Kr-
ishna, and Hongliang Ren. Surgical-VQA: Visual question
answering in surgical scenes using transformer. InMedical
Image Computing and Computer Assisted Intervention
(MICCAI), pages 33–43. Springer Nature Switzerland,
2022. .
Pia H. Smedsrud, Vajira Thambawita, Steven A. Hicks, Hen-
rik Gjestang, Oda Olsen Nedrejord, Espen Næss, Hanna
Borgli, Debesh Jha, Tor Jan Derek Berstad, Sigrun L. Es-
keland, Mathias Lux, H ˚avard Espeland, Andreas Petlund,
Duc Tien Dang Nguyen, Enrique Garcia-Ceja, Dag Jo-
hansen, Peter T. Schmidt, Ervin Toth, Hugo L. Hammer,
Thomas de Lange, Michael A. Riegler, and P ˚al Halvorsen.
Kvasir-Capsule, a video capsule endoscopy dataset.Sci-
entific Data, 8(1):142, 2021. .
1345

Yuan and Shujian, 2026
Ralf Stauder, Daniel Ostler, Michael Kranzfelder, Sebastian
Koller, Hubertus Feußner, and Nassir Navab. The TUM
LapChole dataset for the M2CAI 2016 workflow challenge.
Technical report, Technical University of Munich, 2016.
arXiv:1610.09278.
Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-
Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalk-
wyk, Andrew M Dai, Anja Hauth, Katie Millican, et al.
Gemini: a family of highly capable multimodal models.
arXiv preprint arXiv:2312.11805, 2023.
Yuan Wang, Jiaxiang Liu, Shujian Gao, Bin Feng, Zhihang
Tang, Xiaotang Gai, Jian Wu, and Zuozhu Liu. V2t-
cot: From vision to text chain-of-thought for medical
reasoning and diagnosis. InInternational Conference
on Medical Image Computing and Computer-Assisted
Intervention, pages 658–668. Springer, 2025.
Yuan Wang, Shujian Gao, Jiaxiang Liu, Songtao Jiang, Xia
Haoxiang, Xiaotian Zhang, Zhaolu Kang, Yemin Wang,
and Zuozhu Liu. Beyond n-grams: A hierarchical reward
learning framework for clinically-aware medical report
generation. InProceedings of the AAAI Conference on
Artificial Intelligence, volume 40, pages 33719–33727,
2026.
Haoning Wu, Dongxu Li, Bei Chen, and Junnan Li.
LongVideoBench: A benchmark for long-context inter-
leaved video-language understanding. InAdvances in Neu-
ral Information Processing Systems (NeurIPS), Datasets
and Benchmarks Track, 2024. arXiv:2407.15754.
Weiwen Xu, Hou Pong Chan, Long Li, Mahani Aljunied,
Ruifeng Yuan, Jianyu Wang, Chenghao Xiao, Guizhen
Chen, Chaoqun Liu, Zhaodonghui Li, et al. Lingshu:
A generalist foundation model for unified multimodal
medical understanding and reasoning.arXiv preprint
arXiv:2506.07044, 2025.
Jinguo Zhu, Weiyun Wang, Zhe Chen, Zhaoyang Liu, Shen-
glong Ye, Lixin Gu, Hao Tian, Yuchen Duan, Weijie Su,
Jie Shao, et al. Internvl3: Exploring advanced training
and test-time recipes for open-source multimodal models.
arXiv preprint arXiv:2504.10479, 2025.
1346
