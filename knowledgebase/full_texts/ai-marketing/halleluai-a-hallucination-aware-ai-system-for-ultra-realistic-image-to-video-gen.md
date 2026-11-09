---
title: 'HALLELUAI: A Hallucination-Aware AI System for Ultra-Realistic Image-to-Video Generation at Scale'
url: https://arxiv.org/abs/2607.22959
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Aniket Sakpal
- Yang Jiang
- Rouzbeh Davoudi
- Shayan Hassantabar
- Mani Najmabadi
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.22959
pages: 10
chars: 36810
fetched_at: '2026-11-08T12:57:28+00:00'
kb_version: 1
---

# HALLELUAI: A Hallucination-Aware AI System for Ultra-Realistic Image-to-Video Generation at Scale

HALLELUAI: A Hallucination-Aware AI System for Ultra-Realistic
Image-to-Video Generation at Scale
Aniket Sakpal ∗ Yang Jiang† Rouzbeh Davoudi ‡ Shayan Hassantabar§
Mani Najmabadi ¶
July 28, 2026
Abstract
AI-generated video is increasingly used across market-
ing, product storytelling, and creative workflows, yet
automated; high-precision quality control remains a
major constraint to scaling production. We present
HALLELUAI, an end-to-end system that moderates and
regenerates image-to-video outputs to meet expert-level
creative standards and deliver ultra-realistic videos with
consistent end-user quality of experience (QoE) at scale.
The system integrates a video moderation module that
evaluates frame-level aesthetics, temporal motion fidelity,
and fine-grained hallucination risks relative to the source
image, with an agentic regeneration module that itera-
tively fixes failures through prompt refinement, controlled
camera adjustments, targeted model or image switching,
and structured retry strategies. The moderation logic
is aligned with domain-specific creative guidelines and
produces granular, machine-actionable feedback that
directly drives regeneration. In human-in-the-loop
evaluations with creative experts, HALLELUAI shows
strong alignment and reliably outputs ultra-realistic,
production-grade videos suitable for product and mar-
keting placements at scale. This framework advances
trustworthy AI generated video content by enforc-
ing visual realism, brand safety, and strict input-image
fidelity while enabling image-to-video generation at scale.
Keywords:image-to-video generation, hallucination
detection, generative AI, diffusion models
1 Introduction
1.1 Motivation and Context
AI-generated video (AIGV) has rapidly become central
to content production across visually intensive platforms
such as digital advertising, social media, and product de-
tail pages. Advances in diffusion-based image-to-video
∗Expedia Group, Email: aniket17sakpal@gmail.com
†Expedia Group, Email: jiang.yang.james@gmail.com
‡Expedia Group, Email: rouzbeh.davoudi@gmail.com
§Expedia Group, Email: s_hassantabar@yahoo.com
¶Expedia Group, Email: maninajmabadi@gmail.com
models now enable large-scale video synthesis at negli-
gible marginal cost, supporting rapid experimentation,
personalization, and localization. For domains such as
travel, real estate, and e-commerce—where visual realism
directly influences trust and conversion, AIGV offers a
scalable alternative to traditional, resource-intensive pro-
duction pipelines.
The economic incentives are substantial. Generative
video systems compress production timelines from weeks
to minutes and reduce per-asset costs by orders of magni-
tude relative to conventional workflows. These advan-
tages position AIGV as a foundational technology for
high-throughput visual storytelling. However, realizing
this potential in production environments requires robust
mechanisms to guarantee quality, realism, and strict fi-
delity to the source image.
1.2 Problem Statement – Quality Chal-
lenges in Image-to-Video Generation
Despite rapid progress, image-to-video (I2V) models still
produce artifacts that degrade quality of experience
(QoE). Common failures include frame-level degradations
(e.g., blur, noise, and brightness drift), temporal incon-
sistencies such as jitter and unnatural motion, and con-
tent hallucinations that introduce or alter scene elements
relative to the source image [19,26]. Hallucinations are
particularly problematic because the input image serves
as the ground truth. Deviations from it can misrepresent
reality, reduce user trust, and create legal risks in do-
mains such as travel and real estate [26]. Current evalua-
tion methods do not adequately address these challenges.
Distributional metrics including Inception Score (IS) [2],
Fréchet Inception Distance (FID) [6], and Fréchet Video
Distance (FVD) [20] assess dataset-level realism but not
fidelity to a specific input image. Likewise, existing video
quality assessment methods often overlook AIGV-specific
artifacts such as cross-frame inconsistencies and subtle
hallucinations [4,5,12,24]. As a result, there is no reli-
able automated mechanism for detecting and mitigating
these failures at scale. Recent experience with systems
such as OpenAI’s Sora [18] further highlights the need for
robust quality assessment and moderation frameworks for
1
arXiv:2607.22959v1  [cs.CV]  25 Jul 2026

reliable I2V deployment [9,15,16].
1.3 Gaps in Prior Work
Despite recent advances in generative video evaluation,
existing approaches remain insufficient for production-
grade, image-conditioned AI-generated video.
Per-asset, conditional evaluation:Metrics such as
IS [2], FID [6], and FVD [20] are designed for model-level
comparison rather than asset-level acceptance. They do
not condition on a specific input image and therefore fail
toassesssource-imagefidelity, temporalstability, camera-
motion quality, and hallucinations. FVD can also be un-
stable and may mis-rank models under limited sample
sizes [20]. Recent work further highlights the challenge of
evaluating semantic consistency and multi-level structure
in AI-generated video [10].
Actionability:Frameworks such as FVMD [12], Eval-
Crafter [14], VBench [7], and Video-Bench [17] improve
interpretability and alignment with human judgment,
while VQAScore, GenAI-Bench, and VideoScore extend
VQA-based evaluation to generative content [5,11,13,23].
However, these methods remain primarily evaluative:
they do not enforce source-image fidelity, gate individ-
ual assets, or provide diagnostics that directly support
remediation.
Hallucination detection:Existing approaches fo-
cus on prompt consistency in text-to-video generation
[3], diffusion-model hallucinations [1], or broader mul-
timodal settings using uncertainty- and self-consistency-
based techniques [8,22]. Recent multimodal research like-
wise emphasizes the need for stronger grounding and se-
mantic consistency [21,25]. However, these methods do
not condition on a source image or detect fine-grained
temporal and structural deviations.
Closed-loop deployment:Current benchmarks as-
sess model capability but do not support per-asset gating,
domain-specific compliance, or automated remediation.
Consequently, the literature lacks end-to-end frameworks
that combine expert-aligned evaluation, source-image fi-
delity, and iterative regeneration for deployment in high-
trust domains such as travel and real estate [21,25].
1.4 Contributions
This work introduces a production-oriented moderation
and regeneration framework for image-to-video genera-
tion that addresses the above gaps.
•Per-asset, conditional video moderation:a
domain-aligned module evaluating each video rela-
tive to its input image across visual quality, temporal
motion, and source-image fidelity.
•Machine-actionable, expert-aligned diagnos-
tics:structured failure taxonomies, severity assess-
ments, and pass/fail decisions mapping failure modes
to corrective actions.
•Fine-grained, temporally aware hallucination
detection:a layer identifying object-, structure-,
and identity-level deviations, temporal inconsisten-
cies, and artifacts relative to the source image.
•Closed-loop, agentic regeneration:a coupled
module translating moderation feedback into tar-
geted actions—prompt refinement, camera-control
adjustment, model switching, base-image selection—
iterating until quality criteria are met.
•Human-in-the-loop validation:an evaluation
protocol demonstrating alignment with expert judg-
ment and real-world deployability.
2 System Overview
We propose an agentic closed-loop image-to-video gener-
ation system that unifies automated moderation with au-
tonomous planning and targeted regeneration to enforce
expert-defined creative quality and strict source-image fi-
delity at scale (Fig. 1). Given an input image and creative
guidelines (1), the system generates an initial video (2),
which is evaluated by the Video Moderation Module (3)
acting as both gatekeeper and diagnostics engine. The
module assesses outputs across frame-level visual qual-
ity (3a), temporal motion quality (3b), and hallucination
relative to the source image (3c), producing a structured
moderation report (4) with dimension-wise scores, ratio-
nales, risk indicators, and a PASS/FAIL decision enforced
by a decision gate (5).
For failed outputs, control is passed to the Agentic Re-
generation Module (7), which converts feedback into au-
tonomous actions. A planning agent (7a) maps failure
categories and severities to targeted interventions, includ-
ing prompt refinement for motion constraints (7b), cam-
era direction or pacing adjustments (7c), base-image sub-
stitution for artifact-prone regions (7d), and alternative
model selection for model-specific failures (7e). These ac-
tions drive targeted regeneration (8), after which outputs
are re-evaluated by the moderation module.
The loop iterates until acceptance criteria are satisfied
and final approval is reached (6), or until iteration, la-
tency, or compute limits are exceeded (Fig. 1). By cou-
pling fine-grained diagnostics with autonomous planning
and remediation, the system enables systematic quality
control and scalable deployment of image-to-video gener-
ation.
3 Video Moderation Module
The Video Moderation Module is the system’s primary
quality gate and diagnostic engine, assessing image-to-
video outputs before approval or regeneration. For each
candidate video, it evaluates domain-aligned creative and
fidelity constraints across three dimensions: frame-level
2

Figure 1: Architectural overview of the proposed closed-loop system for image-to-video generation. The framework
integrates a diagnostic Video Moderation Module (3), calibrated by Creative Expert Guidelines, with an Agentic
Regeneration Module (7). Candidate videos undergo iterative evaluation across frame-level, temporal, and fidelity
dimensions (3a–c). Failures trigger a Planning Agent (7a) to execute targeted remediation strategies (7b–e) until the
asset satisfies predefined quality thresholds or resource constraints are met.
visual quality, temporal motion quality, and hallucina-
tion detection relative to the input image. The evalua-
tion yields a structured, machine-actionable report with
dimension-wise scores, calibrated risk levels, localized ra-
tionales, and a unified PASS/FAIL decision—designed
to directly parameterize downstream regeneration for
targeted correction rather than unguided retries. The
module is grounded in a hierarchical problem taxonomy
(Fig. 1) categorizing common failure modes in ultra-
realistic image-to-video generation, providing a shared
abstraction layer that maps detected failures to corrective
strategies such as prompt constraints, parameter adjust-
ments, base-image substitution, or model switching.
3.1 Frame-Level Quality Signals: Blur,
Contrast, Brightness, and Noise
We compute four complementary frame-level signals over
a generated videoV={f 1, . . . , fT }and a reference in-
put imageI, with all frames andIconverted to grayscale
for statistics. Each signal is summarized via normalized
ratios and compared against calibrated thresholds to pro-
duce a unified PASS/FAIL decision with a concise reason.
Blur (Sharpness Degradation).Blur is quantified
via the variance of the Laplacian: for each frameft, we
compute a sharpness scoreL t = Var(∇ 2ft), then mea-
sure the relative sharpness drop∆blur by comparing the
anchorL 1 to the minimum sharpness across the video.
Contrast (Low/High Contrast).Contrast is quan-
tified via the standard deviation of grayscale intensi-
ties. With referenceC ref =σ(I)and frame contrast
Ct =σ(f t), we compute normalized decrease∆↓ and in-
crease∆ ↑ relativetoreference, optionallytrackingwithin-
video spread to capture excessive variability.
Brightness/Exposure (Low/High Exposure).
Brightness is quantified via mean grayscale intensity.
WithB ref =µ(I)andB t =µ(f t), we compute nor-
malized exposure decrease∆ B ↓ and increase∆ B ↑ from
the minimum and maximum brightness relative to the
reference.
Noise (Stochastic Artifacts).Noise is estimated via
a per-frame Laplacian-variance scoreN t; frames are
marked noisy whenN t exceeds a thresholdτ noise, and
3

the video is flagged if the percentage of noisy frames ex-
ceeds a small tolerance (e.g.,5%), capturing persistent
stochastic artifacts.
Algorithm 1Unified Frame-Level Quality Detection
(Blur, Contrast, Brightness, Noise)
Require:Reference imageI, videoV={f 1, . . . , fT }
Require:Thresholdsτ blur, τ↓, τ↑, τB ↓ , τB ↑ , τnoise, τp
Ensure:Decisiond∈ {PASS,F AIL}, reasonr
d←PASS,r←Acceptable Quality
ConvertIto grayscale once and computeC ref =σ(I),
Bref =µ(I)
(1) Blur / Sharpness
ComputeL t = Var(∇2ft)for allt
∆blur ←(L 1 −min t Lt)/L1
if∆ blur > τblur then
d←F AIL;r←Sharpness Degradation
end if
(2) Contrast
ComputeC t =σ(f t)for allt
∆↓ ←(C ref −min t Ct)/Cref
∆↑ ←(max t Ct −C ref )/Cref
ifd= PASSand∆ ↓ > τ↓ then
d←F AIL;r←Low Contrast
else ifd= PASSand∆ ↑ > τ↑ then
d←F AIL;r←High Contrast
end if
(3) Brightness / Exposure
ComputeB t =µ(f t)for allt
∆B ↓ ←(B ref −min t Bt)/Bref
∆B ↑ ←(max t Bt −B ref )/Bref
ifd= PASSand∆ B ↓ > τB ↓ then
d←F AIL;r←Low Exposure
else ifd= PASSand∆ B ↑ > τB ↑ then
d←F AIL;r←High Exposure
end if
(4) Noise
Compute per-frame noise scoreNt (Laplacian variance)
and mark noisy frames whereNt > τnoise
pnoise ← 1 T PT t=1 I[Nt > τnoise]
ifd= PASSandp noise > τp then
d←F AIL;r←Noise Artifacts
end if
3.2 Temporal Motion Quality
This component ensures camera motion is cinematic,
intentional, and domain-appropriate. It evaluates (i)
prompt alignment—whether the dominant motion direc-
tion/style matches the prompt intent—and (ii)motion
intensity and smoothness—whether the pace is neither
stagnant nor aggressive and free of jitter. We compute
dense optical flow using RAFT to obtain a per-pixel dis-
placement field between consecutive frames, deriving ro-
bust frame-level motion statistics that classify the video
asLow Motion,High Motion, orAcceptable, with addi-
tional jitter flags for high-frequency instability.
3.2.1 Unpleasant Camera Motion (Intensity &
Smoothness) Module
We estimate motion intensity from the RAFT flow mag-
nitude. At each stept, RAFT produces a dense displace-
ment fieldu t(x)∈R 2 mapping pixels fromf t tof t+1.
We compute the per-pixel magnitudemt(x) =∥u t(x)∥2
and summarize motion via a robust statistic: the mean
magnitude of the top-qfraction of pixels (e.g.,q= 15%),
Mt = Mean(Top q({mt(x)})), focusing on salient mov-
ing regions and reducing background-noise sensitivity.
Video-level intensity isµ M = Mean t(Mt)and stability
σM = Stdt(Mt). The module flagsLow Motionwhenµ M
falls below a threshold (stagnant/slow pans),High Mo-
tionwhenµ M exceeds a threshold (whip-pan/aggressive
moves), andJitterwhenσ M or the high-frequency vari-
ation ofM t exceeds a threshold (abrupt accelerations).
These outcomes map directly to actionable remediation
(reduce motion strength, tighten camera range, or stabi-
lize).
3.2.2 Prompt Alignment Module
This module verifies that observed camera motion
matches the prompt-specified intent (e.g., pan left-to-
right, tilt up, dolly-in/zoom-in). We estimate cam-
era motion using TAPIR point tracking: salient points
initialized on the first frame are tracked through the
video to obtain 2D trajectories. To reduce object-motion
confounds, we preferentially sample edge points (high-
gradient regions) and aggregate trajectories into group-
level displacement statistics. Lettingp t i ∈R 2 denote
tracked pointiat timet, we compute net displacement
∆pi =p T i −p 1 i and summarize motion by the dominant
direction ˆv= Normalize(Median i(∆pi)). We further use
structured point groups (e.g., left-edge setPL, top-edge
setP U) to detect zoom/dolly: ifPL moves left whilePU
moves up (divergence from the image center), the mo-
tion is consistent with zoom-in/dolly-in, whereas conver-
gence indicates zoom-out/dolly-out. The observed label
ˆyis compared against the prompt intentyprompt to yield
an alignment scores align, triggering a FAIL when below
threshold.
4

Algorithm 2Temporal Motion Quality: Intensity &
Smoothness + Prompt Intent Alignment (TAPIR)
Require:VideoV={f 1, . . . , fT }, promptmotionintent
yprompt
Require:Top-pixel fractionq(e.g.,0.15)
Require:Thresholdsτ low, τhigh, τjit, alignment threshold
τalign
Ensure:Decisiond motion ∈ {PASS,F AIL}and reason
rmotion
dmotion ←PASS,r motion ←Acceptable Motion
(A) Unpleasant Camera Motion: Intensity &
Smoothness (RAFT)
fort= 1toT−1do
ut ←RAFT(f t, ft+1)
mt(x)← ∥ut(x)∥2 for all pixelsx
Mt ←Mean

Topq({mt(x)})

end for
µM ←Mean t(Mt),σ M ←Std t(Mt)
ifµ M < τlow then
dmotion ←F AIL;r motion ←Low Motion (Stagnant)
else ifµ M > τhigh then
dmotion ←F AIL;r motion ←High Motion (Aggres-
sive)
else ifσ M > τjit then
dmotion ←F AIL;r motion ←Jitter / Instability
end if
(B) Prompt Intent Alignment (TAPIR)
(B1) Point Initialization & Tracking:
Initialize an edge-biased point setPon the first frame
f1
Track points{p t i}T t=1 using TAPIR and compute net
displacements
∆pi ←p T i −p 1 i
(B2) Dominant Motion Estimation:
Estimate global camera translation
ˆv←Normalize(Median i∈P (∆pi))
(B3) Zoom / Dolly Detection:
Partition points into spatial edge sets (e.g., leftPL, top
PU)
δL ←Median i∈PL (∆pi),δ U ←Median i∈PU (∆pi)
(B4) Motion Intent Classification:
Infer observed motion label
ˆy←ClassifyMotion(ˆv, δL, δU )
(B5) Prompt Alignment Check:
Compute alignment scoresalign ←I[ˆy=y prompt]
ifd motion = PASSands align < τalign then
dmotion ←F AIL;r motion ←Prompt Misalignment
end if
3.3 Hallucinations
We evaluate two types of hallucination in image-to-video
generation:object hallucinationandnew-structure hal-
lucination. Object hallucination refers to failures in pre-
servingtemporalconsistency, physicallyplausiblemotion,
and coherent object interactions across frames relative
to the input image, leading to object drift, deformation,
and other artifacts.New-structure hallucinationis the
synthesis of objects or scene elements absent from the
source image—particularly important in high-trust do-
mains (e.g., travel, real estate), where introducing nonex-
istent structures may misrepresent reality and increase
legal and reputational risk. The following section details
the annotation categories for each type.
Figure2: PrompttemplateprovidedtotheVLLMforhal-
lucination detection. It defines seven hallucination cate-
gories and instructs the model to identify and track ob-
jects across frames, categorize changes as hallucinations
(distinguishing them from camera motion), assign a 1–10
severity score per category, and output results as JSON
(0 if none detected).
3.3.1 Hallucination Categories
1.Object Hallucination
•Object Fusion: Two or more objects unnat-
urally merge, exhibit boundary corruption, or
5

interpenetrate.
•Implausible Transformation: An object un-
dergoes non-causal changes in shape, color, or
identity unexplained by interactions or scene
dynamics.
•Object–Background Merge: An object
blends into the background despite being ex-
pected to remain visually distinct.
•Unnatural Object Movement: Object mo-
tion violates physical constraints (e.g., un-
supported motion, inconsistent trajectories) or
lacks plausible causation.
•Implausible Disappearance: An object
abruptly vanishes without occlusion, exit from
view, or other reasonable explanation.
•Object Splitting: A single object unnaturally
divides into multiple distinct objects.
•Text Hallucination: Textual elements (e.g.,
numbers, signs) change content, deform, or be-
come illegible.
2.New Structure Hallucination:
•Natural entry: Objects absent from the
source image appear by entering the field of
view with temporally continuous, physically
plausible motion.
•Camera-induced entry: Previously unseen
objects become visible due to global camera
motion (e.g., panning, tilting, zooming) rather
than object motion.
•Abruptemergence: Objectsnotinthesource
image appear instantaneously without reason-
able physical explanation.
3.3.2 Hallucination Detection Module
As illustrated in Fig. 3, we propose a hallucination-
detection module for videos generated by an Image2Video
model. Given a generated video, we uniformly sample
framesF={f 1, . . . , fn}. To detect object hallucina-
tions, we first extract objectsO={o 1, . . . , om}from
the input image using a multimodal large language model
(MLLM), then provideO, the input image, andFto an
MLLM (e.g., GPT-4o) to identify object-level inconsis-
tencies across time, mapped to the predefined categories
C={c 1, . . . , cm}. For each categoryc i, the MLLM
outputs a severity scoreS i o ∈[0,10]and a brief ratio-
nale when evidence is present, following the prompt tem-
plate shown in Fig. 2. The object-hallucination decision
dobject aggregates the category-wise scores, thresholding
each againstτ i object. To detect new-structure hallucina-
tions, we compare each sampled framefi with the input
image to determine whether novel objects appear under
three cases: (1) natural entry, (2) camera-induced entry,
and (3) abrupt emergence. An MLLM produces a per-
frame binary decisiond i new, and the video-level decision
isd new = Sn i=1 di new.
3.4 Scoring and Risk Assessment
Themoduleaggregatesframe-level, temporal-consistency,
and hallucination scores via domain-calibrated weights
into a unified verdict, paired with a narrative summary
contextualizing each issue against creative standards and
Quality of Experience (QoE). APASS/FAILdecision fol-
lows from thresholded expert-derived criteria, with a
standardized risk level (No,Low,Medium,High) tied to
specific failures. Outputs form a tuple of failure codes,
severities, and remediation levers (e.g., reduce motion,
adjust exposure, switch models), serving both as a gat-
ing mechanism and as input to the agentic regeneration
module for targeted, iterative corrections.
4 Agentic Regeneration Module
The Agentic Regeneration Module converts moderation
findings into targeted corrective actions via a closed-loop
planner–executor process. A planning agent interprets
frame-level, temporal, and hallucination signals relative
to the source image, selects a minimal yet effective in-
tervention set, and issues an updated generation request;
the regenerated asset is re-scored, looping until quality
thresholds or operational limits are met.
Inputs and Outputs.Inputs comprise the source im-
age and metadata (e.g., campaign, channel), prior gen-
eration configuration (prompt, model, seed, motion pa-
rameters), and the structured moderation report (failure
codes, severities, rationales, PASS/FAIL). Outputs com-
prise a next-generation plan (revised prompt, actions, pa-
rameters, chosen model or base image) and execution ar-
tifacts (regenerated video with a full action log for repro-
ducibility).
ActionPolicy.Theagentdrawsonaconstrainedinter-
vention library: (i) prompt refinements enforcing motion
clarity, objectpreservation, source-imagefidelity, andaes-
thetic stability; (ii) camera/motion adjustments to re-
duce jitter, overshoot, or blur; (iii) base-image selection
when artifacts cluster around occlusions or ambiguous
regions; and (iv) model switching or tuning for model-
specific failures. A cost- and efficacy-aware policy prior-
itizes low-cost, minimally invasive actions, escalates for
high-severity or repeated failures, and bundles actions
when interactions are likely.
Iteration and Governance.The loop (Generate→
Moderate→Regenerate) terminates on PASS, budget ex-
haustion, or escalation to human review for persistent is-
sues, loggingalldecisionsforauditability. Couplingstruc-
6

Figure 3: Hallucination detection module for Image2Video generation. Uniformly sampled frames are analyzed
with an MLLM to (top) detect and track input-image objects, map temporal inconsistencies to predefined object-
hallucination categories, and aggregate category scores for a final decision; and (bottom) compare each sampled
frame with the input image to identify new-structure hallucinations (natural entry, camera-induced entry, or abrupt
emergence)
tured diagnostics with a cost-aware strategy, the module
converts failing candidates into compliant assets while
preserving input-image fidelity and minimizing manual
oversight.
5 Tuning and Evaluation
Threshold calibration and parameter tuning were per-
formed using 58 AI-generated video clips across the three
moderation components. For hallucination detection, we
used GPT-4o as the underlying LLM. Prompts were iter-
atively refined to elicit accurate reasoning for each hal-
lucination category. Recall, defined as the proportion
of hallucination-containing videos correctly detected, was
used as the primary metric for selecting the final prompts.
Category-specific hallucination thresholds were then op-
timized to maximize sensitivity for detecting high-risk
videos, as defined in Section 3.4. We then evaluate the
proposed tuned system using a human-in-the-loop proto-
col designed to measure alignment with expert creative
judgment and readiness for production deployment. The
protocol consists of three stages:Shadow Mode(cal-
ibration),Pseudo Production(gating performance),
andProduction QA(longitudinal monitoring).
Table 1: HALLELUAI moderation Performance Metrics
Compared to Expert Decisions
Metric Value
Overall PASS/F AIL Agreement 86.9%
Precision on AI-approved assets 88%
Recall on AI-approved assets 74%
5.1 Stage 1: Shadow Mode
In Shadow Mode, unseen 146 AI-generated video clips
were independently evaluated by creative expert review-
ers, the HALLELUAI moderation system, and industry
benchmark methods, without cross-visibility of decisions.
Each clip was standardized through trimming and nor-
malizing the aspect-ratio before evaluation.
5.1.1 Creative Expert Alignment
First, we evaluated the alignment of moderation systems
by comparing their output to reviews from human cre-
ative experts on the video dataset. The HALLELUAI
moderation system achieves 88% precision and an agree-
ment rate of 87%. The results are summarized in Table 1
7

Agreement Analysis.Precision is the key metric, as
it directly reflects the quality and reliability of videos ap-
proved by the system.
The system exhibits conservative gating behavior, fil-
tering a portion of expert-approved clips while limiting
false approvals.
Stage-LevelDiagnosticBreakdownToanalyzeper-
formance across moderation components, we decompose
precision by category, as shown in Table 2.
The majority of precision-impacting errors arise from
fine-grained object-level hallucinations. Motion intensity
thresholdscontributeprimarilytofalsenegatives, indicat-
ing conservative rejection behavior. Frame-level degrada-
tions contribute minimally to disagreement.
5.1.2 Benchmark Comparison
Sincenoopen-sourcesystemsprovidecomprehensiveeval-
uation for image-to-video generation, we compared our
system against UGC video quality assessment (VQA)
models such as DOVER [24] and COVER [4], as well
as multimodal large language models (MLLMs) via zero-
shot prompting (See Fig. 4 for prompt details). The
MLLM prompt was designed to evaluate the three com-
ponents our system addresses—frame-level quality, tem-
poral motion quality, and hallucination—with frames uni-
formly sampled at 2 fps.
As shown in Table 3, UGC VQA models like DOVER
and COVER could not differentiate PASS from FAIL
videos, as they were not designed for image-to-video gen-
eration and lack hallucination-detection metrics. The
MLLM-based method showed low precision, unable to de-
tect artifacts in AI-generated videos—demonstrating that
withoutdetailed, comprehensiveprompting, MLLMscan-
not reliably identify such artifacts.
Figure 4: Evaluation Prompt Designed for MLLMs to
Evaluate Frame-level Quality,Temporal Motion Quality
and Hallucination in Image2Video Generation
5.2 Stage 2: Pseudo Production (Gating
Performance)
In Pseudo Production mode, we evaluate the combined
moderation + regeneration system end-to-end by sending
only system-approved clips for human creative review. Of
1,158 system-approved clips, 1,126 were also accepted by
experts, yielding 97% precision and indicating that the
vast majority of surfaced clips are production-ready. This
precision is not directly comparable to Shadow Mode,
since outputs here have undergone iterative regenera-
tion and refinement before evaluation—the system is not
merely filtering errors but actively improving clips, driv-
ing higher agreement with expert judgment.
5.3 Stage 3: Production QA (Longitudi-
nal Monitoring)
Following calibration, ongoing monitoring employs ran-
dom sampling (1–5%) of system-approved assets for ex-
pert review. Precision levels of 97% remain consistent
with Pseudo Production Mode results, and regression
testing ensures that threshold or regeneration-policy up-
dates do not degrade previously validated performance.
Deployed at scale, the system generated approximately
70,000+ videos, further validating its reliability.
5.4 Evaluation Summary
These results demonstrate that structured moderation
combined with agentic regeneration can function as a
reliable production-grade quality control layer for ultra-
realistic image-conditioned video generation.
6 Conclusion
HALLELUAI is an expert-aligned, production-oriented
system that makes image-to-video quality assurance
a controllable, closed-loop process, coupling per-asset
moderation—aesthetics, motion quality, and source-
image–conditioned hallucination detection—with an
agentic regeneration policy that converts failures into
targeted fixes rather than blind retries. Human-in-the-
loop validation shows strong agreement with creative ex-
perts, supporting deployment as a high-precision gate
for scalable AIGV. By enforcing input-image fidelity,
emitting machine-actionable diagnostics, and maintain-
ing auditable decision trails, it bridges benchmark-
style evaluation and real-world creative governance—
to our knowledge, the first integrated moderation-and-
regeneration framework purpose-built for ultra-realistic,
image-conditioned video generation at scale.
References
[1] Sumukh K Aithal, Pratyush Maini, Zachary C Lip-
ton, and J Zico Kolter. Understanding hallucina-
tionsindiffusionmodelsthroughmodeinterpolation.
Advances in neural information processing systems,
37:134614–134644, 2024.
[2] Shane Barratt and Rishi Sharma. A note on the
inception score.arXiv preprint arXiv:1801.01973,
2018.
8

Table 2: Stage-level contribution to Precision and False Positives (FP). Percentages reflect the proportion of total
observed errors attributable to each signal.
Module Sub-Category Precision
Frame-Level Quality
Blur 100%
Contrast 97%
Brightness 100%
Noise 100%
Temporal Motion Quality Prompt Alignment 100% Motion Intensity 97%
Hallucination Detection
Object Hallucination 97%
New Structure Hallucination 97%
Text Hallucination 100%
Table3: PerformanceComparisonofDifferentEvaluation
Methods
Method Prec. Rec. F1 Acc.
DOVER 0.20 0.21 0.20 0.56
COVER 0.27 0.33 0.30 0.58
Qwen3-VL-8B 0.28 1.00 0.43 0.30
NOVA 2 Lite 0.25 0.74 0.37 0.34
HALLELUAI 0.88 0.74 0.81 0.87
[3] Zhixuan Chu, Lei Zhang, Yichen Sun, Siqiao Xue,
Zhibo Wang, Zhan Qin, and Kui Ren. Sora detec-
tor: A unified hallucination detection for large text-
to-video models.arXiv preprint arXiv:2405.04180,
2024.
[4] Chenlong He, Qi Zheng, Ruoxi Zhu, Xiaoyang Zeng,
Yibo Fan, and Zhengzhong Tu. Cover: A compre-
hensive video quality evaluator. InProceedings of
the IEEE/CVF conference on computer vision and
pattern recognition, pages 5799–5809, 2024.
[5] Xuan He, Dongfu Jiang, Ge Zhang, Max Ku, Achint
Soni, Sherman Siu, Haonan Chen, Abhranil Chan-
dra, Ziyan Jiang, Aaran Arulraj, et al. Videoscore:
Building automatic metrics to simulate fine-grained
human feedback for video generation. InProceedings
of the 2024 Conference on Empirical Methods in Nat-
ural Language Processing, pages 2105–2123, 2024.
[6] Martin Heusel, Hubert Ramsauer, Thomas Un-
terthiner, Bernhard Nessler, and Sepp Hochreiter.
Gans trained by a two time-scale update rule con-
verge to a local nash equilibrium.Advances in Neural
Information Processing Systems, 30, 2017.
[7] Ziqi Huang, Yinan He, Jiashuo Yu, Fan Zhang,
Chenyang Si, Yuming Jiang, Yuanhan Zhang, Tianx-
ing Wu, Qingyang Jin, Nattapol Chanpaisit, et al.
Vbench: Comprehensive benchmark suite for video
generative models. InProceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recog-
nition, pages 21807–21818, 2024.
[8] Saurabh Kadavath et al. Language models
(mostly) know what they know.arXiv preprint
arXiv:2207.05221, 2022.
[9] Siqi Kou, Jiachun Jin, Zetong Zhou, Ye Ma, Yu-
gang Wang, Quan Chen, Peng Jiang, Xiao Yang, Jun
Zhu, Kai Yu, et al. Think-then-generate: Reasoning-
aware text-to-image diffusion with llm encoders.
arXiv preprint arXiv:2601.10332, 2026.
[10] Jiaze Li, Haoran Xu, Shiding Zhu, Junwei He, and
Haozhao Wang. Multilevel semantic-aware model for
ai-generated video quality assessment. InICASSP
2025-2025 IEEE International Conference on Acous-
tics, Speech and Signal Processing (ICASSP), pages
1–5. IEEE, 2025.
[11] Zhiqiu Lin, Deepak Pathak, Baiqi Li, Jiayao Li, Xide
Xia, Graham Neubig, Pengchuan Zhang, and Deva
Ramanan. Evaluating text-to-visual generation with
image-to-text generation. InEuropean Conference
on Computer Vision, pages 366–384. Springer, 2024.
[12] Liuetal. Fréchetvideomotiondistance: Ametricfor
evaluating motion consistency in video generation.
arXiv preprint arXiv:2407.16124, 2024.
[13] Liu et al. Genai-bench: Evaluating and improv-
ing compositional text-to-visual generation.arXiv
preprint arXiv:2406.13743, 2024.
[14] Yaofang Liu, Xiaodong Cun, Xuebo Liu, Xintao
Wang, YongZhang, HaoxinChen, YangLiu, Tieyong
Zeng, Raymond Chan, and Ying Shan. Evalcrafter:
Benchmarking and evaluating large video generation
models. InProceedings of the IEEE/CVF conference
on computer vision and pattern recognition, pages
22139–22149, 2024.
[15] Wenping Ma, Xiaoting Yang, Licheng Jiao, Lingling
Li, Xu Liu, Fang Liu, Puhua Chen, Yuting Yang,
9

Mengru Ma, Long Sun, et al. Video diffusion gen-
eration: comprehensive review and open problems.
Artificial Intelligence Review, 58(11):338, 2025.
[16] Yue Ma, Kunyu Feng, Zhongyuan Hu, Xinyu
Wang, Yucheng Wang, Mingzhe Zheng, Xuanhua
He, Chenyang Zhu, Hongyu Liu, Yingqing He, Zeyu
Wang, Zhifeng Li, Xiu Li, Wei Liu, Dan Xu, Linfeng
Zhang, and Qifeng Chen. Controllable video gener-
ation: A survey.arXiv preprint arXiv:2507.16869,
2025.
[17] Munan Ning, Bin Zhu, Yujia Xie, Bin Lin, Jiaxi Cui,
Lu Yuan, Dongdong Chen, and Li Yuan. Video-
bench: A comprehensive benchmark and toolkit for
evaluating video-based large language models.Com-
putational Visual Media, 2025.
[18] OpenAI. Sora: Openai text-to-video model, 2026.
Product documentation and public reports, URL:
https://openai.com/research/sora.
[19] Weiming Ren, Harry Yang, Ge Zhang, Cong Wei,
Xinrun Du, Stephen Huang, and Wenhu Chen. Con-
sisti2v: Enhancing visual consistency for image-to-
video generation.arXiv preprint arXiv:2402.04324,
2024.
[20] Thomas Unterthiner et al. Towards accurate gener-
ative models of video: A new metric & challenges.
InInternational Conference on Learning Represen-
tations Workshop, 2018.
[21] Jiarui Wang, Huiyu Duan, Guangtao Zhai, Juntong
Wang, and Xiongkuo Min. Aigv-assessor: Bench-
marking and evaluating the perceptual quality of
text-to-video generation with lmm. InProceedings of
the Computer Vision and Pattern Recognition Con-
ference, pages 18869–18880, 2025.
[22] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc
Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery,
and Denny Zhou. Self-consistency improves chain
of thought reasoning in language models.arXiv
preprint arXiv:2203.11171, 2022.
[23] Zhou Wang, Alan C. Bovik, Hamid R. Sheikh, and
Eero P. Simoncelli. Image quality assessment: From
error visibility to structural similarity.IEEE Trans-
actions on Image Processing, 13(4):600–612, 2004.
[24] Haoning Wu, Erli Zhang, Liang Liao, Chaofeng
Chen, Jingwen Hou, Annan Wang, Wenxiu Sun,
Qiong Yan, and Weisi Lin. Exploring video quality
assessment on user generated contents from aesthetic
and technical perspectives. InProceedings of the
IEEE/CVF international conference on computer vi-
sion, pages 20144–20154, 2023.
[25] Zhichao Zhang, Wei Sun, Li Xinyue, Jun Jia,
Xiongkuo Min, Zicheng Zhang, Chunyi Li, Zijian
Chen, Wang Puyi, Sun Fengyu, et al. Benchmark-
ing multi-dimensional aigc video quality assessment:
A dataset and unified model.ACM Transactions on
Multimedia Computing, Communications and Appli-
cations, 21(9):1–24, 2025.
[26] Min Zhao, Hongzhou Zhu, Chendong Xiang, Kaiwen
Zheng, Chongxuan Li, and Jun Zhu. Identifying and
solving conditional image leakage in image-to-video
diffusion model.Advances in Neural Information
Processing Systems, 37:30300–30326, 2024.
10
