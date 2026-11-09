---
title: 'Rethinking Clinical Relevance in Chest X-ray Machine Learning: How Evaluation References Define
  Performance'
url: https://arxiv.org/abs/2607.26333
category: ai-marketing
subcategory: measurement
date: 2026-07
venue: ''
authors:
- Panagiotis Fytas
- Ian Selby
- Clemens Karner
- Judith Babar
- Simon Baker
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.26333
pages: 67
chars: 139291
fetched_at: '2026-11-08T13:28:45+00:00'
kb_version: 1
---

# Rethinking Clinical Relevance in Chest X-ray Machine Learning: How Evaluation References Define Performance

Rethinking Clinical Relevance in Chest X-ray Machine
Learning: How Evaluation References Define
Performance
Panagiotis Fytasa,∗, Ian Selbyd, Clemens Karnerc, Judith Babard, Simon
Bakera, Jake Beckfordd, Timothy J Sadlerd,f, Shahab Shahipasandd, Arthikkaa
Thavakumard, John Li Chend,f, Alex Sawerd, Michael Robertsb, Jonathan
Weir-McCallf,g, J.H.F. Rudde, Carola-Bibiane Schönliebb, Anna Korhonena,
Anna Bregerb,c
aLanguage Technology Lab (LTL), University of Cambridge, United Kingdom
bDepartment of Applied Mathematics and Theoretical Physics, University of
Cambridge, United Kingdom
cCenter for Medical Physics and Biomedical Engineering, Medical University of
Vienna, Austria
dCambridge University Hospitals NHS Foundation Trust, United Kingdom
eDepartment of Medicine, University of Cambridge, United Kingdom
fDepartment of Radiology, University of Cambridge, United Kingdom
gSchool of Biomedical Engineering and Imaging Sciences, King’s College London, United
Kingdom
Abstract
Chest X-ray (CXR) machine learning relies heavily on automated evaluation
using reference standards that aim to approximate clinical judgment. However,
commonly used report-derived labels for pathology classification or generic im-
age quality metrics for reconstruction may not reliably reflect clinical judgment.
We systematically investigate how evaluation-reference choices affect model per-
formance and ranking in both pathology classification and image quality assess-
ment (IQA). To enable controlled comparison across evaluation references, we
collected paired expert image- and report-derived labels for thoracic findings
from a clinical cohort at Cambridge University Hospitals (CUH) and curated
a subset of the public MIMIC-CXR dataset, along with expert ratings of di-
agnostic image quality. We show that for supervised image classifiers (ResNet,
DenseNet), several zero-shot and fine-tuned vision-language models (e.g., Med-
KLIP, GLoRIA, and ConVIRT), changing the label source leads to substantial
differences not only in performance estimates but also in model rankings. In
parallel, alignment of IQA measures with expert judgment depends heavily on
the choice of measure, and commonly used IQA metrics such as SSIM and PSNR
often fail to align with expert assessments of diagnostic usability. Our results
∗Corresponding author
Email address:pf376@cam.ac.uk(Panagiotis Fytas)
arXiv:2607.26333v1  [eess.IV]  28 Jul 2026

demonstrate that evaluation choices are crucial: they can determine which mod-
els and methods appear best and are therefore selected for further development
ordeployment. Theselectionofevaluationreferencesshouldthereforebetreated
asacentralcomponentofclinicalvalidityinCXRmachinelearning, andjustified
with respect to the pathology, imaging task, and intended downstream clinical
use. The current code and information on access to the novel dataset are avail-
able athttps://github.com/PanagiotisFytas/XQA-Chest-X-ray; the per-
manent ReShare link and access instructions will be added to the repository
after the review of the repository is completed.
Keywords:Chest X-ray, Evaluation references, Report-derived labels,
Image-derived labels, Image quality assessment, Model ranking, Clinical
evaluation
1. Introduction
The application of machine learning to chest X-ray (CXR) interpretation is
often proposed as a clinical decision support tool to assist radiologists. Machine
learningmodelsarepredominantlytrained[26]andoftenevaluated[28,4,40]us-
ing labels derived from free-text radiology reports via automatic label extraction
[10], including vision-language models (VLMs) [56, 25, 48, 58, 57, 53]. Within
this heterogeneous training and evaluation landscape, Rajpurkar et al. [39] and
Irvin et al. [26] report that image classifiers trained on report-derived supervi-
sion labels occasionally exceed the performance of groups of radiologists when
assessed against an evaluation reference derived directly from chest X-rays. At
the same time, some works acknowledge disagreement between report-derived
and image-derived labels, yet still treat expert image-derived labels as implicit
ground truth [20, 27]. However, radiology report-derived and image-derived la-
bels encode different forms of clinical information: reports are shaped by clinical
context, whereas expert image annotation is typically performed without access
to patient history or indication. Apparent performance gains may therefore re-
flect alignment with a particular labeling convention rather than genuine clinical
validity. This distinction is important because report-derived and image-derived
labelsarecommonlyusedasreferencesforthesameCXRclassificationtasks, de-
spite evidence that they can disagree substantially when applied to correspond-
ing reports and images [27, 28, 26]. More broadly, systematic analyses have
highlighted recurring methodological pitfalls in CXR machine learning, includ-
ing dataset bias, confounding, unstable metrics, and limited external validation,
that can undermine clinical suitability despite strong benchmark performance
[42, 5].
In this work, we ask whether conclusions about CXR machine learning are
stable to the choice of evaluation reference for automated assessment. We study
this question in two settings: pathology classification, where models are evalu-
ated against image-derived or report-derived labels, and image quality assess-
ment, where algorithms are typically judged using generic fidelity metrics rather
than expert assessments of diagnostic usability [3].
2

To the best of our knowledge, publicly available CXR datasets typically
provide only a single source of pathology labels. MIMIC-CXR [28], PadCh-
est [4], CheXpert [26], and BRAX [40] provide labels automatically extracted
from reports, whereas VinDr-CXR [35] provides expert image-derived labels for
thoracic findings. This limits the controlled comparison of report-derived and
image-derived references. To address this gap, we curate XQA-Chest, which
comprises paired expert image-derived and report-derived labels for pathology
classification (XQA-RR) and expert ratings of diagnostic image quality under
controlled degradations (XQA-IQA), thereby allowing us to study the impact of
report-derived and image-derived labels on evaluation results. To test whether
the same effects appear beyond a single clinical cohort, we additionally annotate
a subset of MIMIC-CXR1 under the same image-only and report-only protocols.
Methodological design and annotations were conducted in a clinical setting by
a team of radiologists and radiographers from Cambridge University Hospitals
NHS Foundation Trust, with varying levels of experience.
For pathology classification, we study how the choice of reference labels af-
fects the ranking of a diverse set of deep learning models. Our experiments
span two broad model families: supervised CXR classifiers and VLMs. The
supervised classifiers are drawn from the TorchXRayVision framework [11] and
include DenseNet-121 [24] and ResNet-50 [22] models pretrained across a range
of popular CXR datasets, as well as the JF-Healthcare probabilistic-CAM pool-
ing model [54]. In our experiments, we evaluate these supervised classifiers both
with their original pretrained weights, without target-dataset adaptation, and
after fine-tuning on the target dataset, enabling comparison between transferred
and in-distribution supervised settings. The VLMs are drawn from the BenchX
framework [59] and include CONVIRT [56], GLoRIA [25], MGCA [48], MRM
[58], REFERS [57], MedKLIP [53], MedCLIP [51], MFLAG [32], and PTUnifier
[7] models. For these models, we consider both zero-shot inference, using the
pretrained image-text representations directly, and supervised variants, which
we fine-tune on the target dataset. We study whether model rankings are pre-
served when evaluated against varying label references, and whether ranking
stability varies across pathologies. For image quality assessment, we analyze
whether commonly used full-reference (FR) and no-reference (NR) IQA metrics
preserve radiologists’ rankings of diagnostic image quality or favor distortions
that are clinically irrelevant. Explored metrics include SSIM [50], PSNR [18],
FSIM [55], HaarPSI [41], NIQE [34], SNR [18] and HaarPSImed [29].
With the described data and machine learning models, we show that agree-
mentbetweenimage-derivedandreport-derivedreferencesisstronglypathology-
dependent and that these differences alter not only absolute performance esti-
1AsmallsubsetofMIMIC-CXRreportshasexistingexpert-annotatedlabels[28]. However,
these labels were produced for earlier MIMIC-CXR versions, and the associated report text
does not always match that released in MIMIC-CXR 2.0 and later. Because Findings and
Impression content may be combined or structured differently across versions, the mapping
between the original expert labels and the current reports is not always clear. We therefore
re-annotate the selected subset using a consistent protocol.
3

Pathology Classification Pipeline
Neural NetworkChest X-ray Classification Targets
 Positive
 Negative
. . .
 Lung Opacity
   Atelectasis   Atelectasis
 Positive Positive
 Negative Negative
Image Annotations as Labels Report Annotations as Labels
Radiology 
   Report
 NLP-Tool
Radiologist(s)
Classification 
      Targets
. . .
 Lung Opacity
Chest
 X-ray
 Radiologist
 Committee
   Atelectasis   Atelectasis
Classification 
     Targets    Atelectasis   Atelectasis
. . .
 Lung Opacity
Figure 1: Overview of pathology classification with deep learning models. There are two
sources of classification targets: labels derived either from expert image annotations or from
(expert or automatic) radiology report annotations.
mates but also the relative ranking of models. For some pathologies, the model
identified as best under one reference fails under another. We further show
that the correlation of IQA metrics with expert judgments of diagnostic us-
ability varies highly, and, for many commonly used metrics, it suggests that
image outputs evaluated with those metrics do not guarantee clinical relevance.
Together, these results demonstrate that common evaluation choices are conse-
quential: the selected reference can determine which models and methods are
judged best for clinically relevant downstream tasks. The design and choices
of evaluation schemes, therefore, should be treated as a central component of
clinical validity in CXR and, generally, medical machine learning.
2. Methods
We aim to determine how strongly the judgment of machine learning results
depends on common choices in the underlying evaluation schemes. In particular,
choices that are seen as standard practice and therefore, when employed, are
usually not further challenged regarding their suitability. We analyze two tasks,
pathology classification and image quality assessment, through ranking stability,
i.e., whetherchangingtheevaluationreferencechangeswhichmodelsormethods
are judged best.
4

Image Quality Assessment (IQA) Algorithm Alignment to
Clinician’s Judgement
Reference CXRs
Radiologists 
+
Radiographer
Expert’s
Quality
Scores
Degraded CXRs
Expert IQA
 Clinical Relevancy of IQA algorithms
Full-Reference (FR) IQA
Reference CXRs
FR 
Algorithm
FR 
Quality
Scores
Degraded CXRs
No-Reference (NR) IQA
NR 
Algorithm
NR 
Quality 
Scores
Degraded
     CXR
Multiple FR & NR Scores
IQA
Algorithms
RankingsMultiple 
Experts’ 
Scores
Aggregated
Experts’ 
Scores
Spearman ρ/ 
Kendall τ
Figure 2: Overview of full-reference, no-reference, and clinician-preference-based IQA. The
clinical relevance of IQA methods can be measured through ranking coefficient correlation
measures between algorithmic and expert labels.
2.1. Chest X-ray Pathology Classification
Westudymulti-labelCXRpathologyclassificationusingaCheXpert/MIMIC-
CXR-style label schema [26, 28]. The full annotation schema comprises 14 find-
ing categories: Atelectasis, Cardiomegaly, Edema, Enlarged cardiomediastinum,
Consolidation, Fracture, Lung lesion, Lung opacity, Pleural effusion, Pleural
other, Pneumonia, Pneumothorax, Support devices, and No finding. By fo-
cusing on pathologies, we exclude No finding and Support devices from our
analysis, yielding 12 pathologies. We consider both supervised and zero-shot
classification settings.
Each input image is a chest radiographx∈ X ⊂RH×W, whereXdenotes
the space of grayscale images andHandWdescribe the size of the image.
An image encoderv θ :X →R d maps the input to ad-dimensional latent
representationv=v θ(x), implemented by architectures such as DenseNet [24],
ResNet [22], or Vision Transformer [15] with some parameter spaceθ.
Inthesupervisedsetting, aclassifierheadf θ :R d →R K producespathology-
specific logits, yielding predictions
p= (p1, . . . , pK) =σ

fθ(v)

, p k ∈(0,1),fork∈ {1, . . . , K}
whereσ(·)denotes the sigmoid activation applied independently to each pathol-
ogy logit, andKdenotes the number of pathologies.
5

The image encodervθ can arise from different training paradigms: (i) classifi-
cationmodelstrainedend-to-endinafullysupervisedmanner(e.g.TorchXRayVi-
sion DenseNet/ResNet encoders), and (ii) vision-language models (VLMs) that
are first pretrained using image–text contrastive learning [38, 56] and subse-
quently fine-tuned for image classification. In both cases, training relies on
task-specific labels, typically derived automatically from radiology reports.
Specifically, VLM pretraining learns a shared embedding space via con-
trastive learning [36, 6]. Given an imagex, an associated report textt, and
image/text encodersv θ andl θ:
v=v θ(x),l=l θ(t),
training maximizes similarity between(v,l)matched pairs while minimizing
similarity to other samples. A common objective is
L=−log exp

S(v,l)/τ

P
t′ exp

S(v, lθ(t′))/τ  ,
with cosine similarityS(·,·)and temperatureτ∈R.
In the zero-shot setting, predictions are obtained directly from this shared
space. For each pathologyk, a set of promptsT k is constructed (e.g.“mild
subsegmental atelectasis”, “persistent atelectasis”). Each promptt k ∈ Tk is
encoded asl tk =l θ(tk), and the score is computed as
sk = max tk∈Tk S(v,l tk ),
which serves as a logit for pathologyk.
For evaluation, each image is associated with a reference label vector:
y(r) = (y(r) 1 , . . . , y(r) K ), y (r) k ∈ {0,1},
whererdenotes the label source (e.g. expert image-derived or report-derived la-
bels). Uncertain labels are excluded, following standard practice in benchmarks
such as CheXpert [26]. Different choices ofrdefine the evaluation references
studied in this work.
2.1.1. Deep Learning Models and Evaluation Details
Table 1 summarizes the evaluated models. We consider two model families:
(i) supervised CNN-based classification models and (ii) vision-language mod-
els (VLMs), evaluated in both supervised and zero-shot settings. Supervised
models are trained on datasets with automatically extracted radiology report-
derived labels, as shown in Table 2, reflecting common practice in CXR machine
learning.
WeincludepubliclyavailablesupervisedclassificationmodelsfromtheTorch-
XRayVision framework [11], based on DenseNet-121 [24] and ResNet-50 [22]
architectures trained on individual and pooled popular CXR datasets. We also
6

include the JF-Healthcare DenseNet-121 model with Probabilistic Class Acti-
vation Map (PCAM) pooling [54]. These models are evaluated on XQA-RR
both with their pretrained weights (without adaptation) and after fine-tuning
(in-distribution). We fine-tune the models on a non-public CXR dataset from
Cambridge University Hospitals (CUH) comprising approximately 13,000 im-
ages with labels automatically extracted by the RadPert labeler [17], using the
default TorchXRayVision hyperparameters. For MIMIC-CXR, we do not per-
form additional fine-tuning because TorchXRayVision already provides models
pretrained on MIMIC-CXR as well as models trained on other CXR datasets,
allowing comparison between in-domain and transferred settings without further
adaptation.
We evaluate VLMs from the BenchX framework [59], which provides a uni-
fied setup for pretraining a diverse set of CXR-specific VLMs under controlled
conditions. Includedmodelsspanarangeofarchitecturesandpretrainingstrate-
gies: CONVIRT [56], REFERS [57], PTUnifier [7], MGCA [48], GLoRIA [25],
MedCLIP [51], MedKLIP [53], MFLAG [32], and MRM [58].
VLMs are evaluated in both zero-shot and supervised settings. Zero-shot
classification requires no further training. Conversely, supervised VLMs are
fine-tuned for XQA-RR on the same CUH dataset described above and are
denoted with a-CUHsuffix (e.g., CONVIRT-CUH). For MIMIC-CXR, models
fine-tuned on MIMIC-derived labels are denoted with a-MIMICsuffix. Training
follows the hyperparameter settings provided by BenchX [59].
Performance is quantified using the area under the receiver operating char-
acteristic curve (ROC-AUC) [21]. We adopt ROC-AUC rather than threshold-
dependent metrics because positive-label prevalence varies substantially across
label sources. ROC-AUC measures the probability that a randomly chosen pos-
itive sample is ranked higher than a randomly chosen negative sample, and is
invariant to class prevalence under fixed positive and negative score distribu-
tions [1]. Thus, it removes changes in metric value arising purely from differ-
ent positive-label rates and provides a suitable strategy for comparing model
discrimination across reference label sets. In this setting, differences in ROC-
AUC therefore reflect changes in how each reference source defines the pos-
itive and negative cases, rather than prevalence alone. In contrast, metrics
such as the F1-score [37] depend on a chosen decision threshold and on the
precision–recall trade-off. Because precision is directly affected by the ratio of
positive to negative samples, F1-scores can change purely as a consequence of
differing label prevalence, even when the model’s underlying discrimination is
unchanged [52, 12]. We estimated ROC-AUC uncertainty using 1000-sample
non-parametric bootstrapping over patient studies and report 95% percentile
confidence intervals [16].
2.1.2. Data and Annotation of Common Thoracic Findings
As observed in Table 2, publicly available CXR datasets typically provide
pathology labels from a single source, usually either automatic extraction from
radiology reports or manual image annotation. This limits the ability to study
how evaluation conclusions change across label sources. While some prior works
7

Model Backbone Pretraining Datasets Training Objective
D-RSNA [11] DenseNet-121 RSNA Pneumonia Supervised
D-NIH [11] DenseNet-121 ChestX-ray14 Supervised
D-PC [11] DenseNet-121 PadChest Supervised
D-CheX [11] DenseNet-121 CheXpert Supervised
D-MCch [11] DenseNet-121 MIMIC-CXR (CheXpert labels) Supervised
D-MCnb [11] DenseNet-121 MIMIC-CXR (NegBio labels) Supervised
D-POOL [11] DenseNet-121 ChestX-ray14, CheXpert,
PadChest, MIMIC-CXR
(CheXpert labels), OpenI, RSNA
Pneumonia
Supervised
R-POOL [11] ResNet-50 ChestX-ray14, CheXpert,
PadChest, MIMIC-CXR
(CheXpert labels), OpenI, RSNA
Pneumonia
Supervised
JFH [54] DenseNet-121 + PCAM CheXpert Supervised
CONVIRT [56] ResNet-50 MIMIC-CXR VL
REFERS [57] ViT MIMIC-CXR VL
PTUNIFIER [7] ViT MIMIC-CXR VL
V-MGCA [48] ViT MIMIC-CXR VL
R-MGCA [48] ResNet-50 MIMIC-CXR VL
GLORIA-G [25] ResNet-50 MIMIC-CXR VL
GLORIA-B [25] ResNet-50 MIMIC-CXR VL
V-MedCLIP [51] ViT MIMIC-CXR VL
R-MedCLIP [51] ResNet-50 MIMIC-CXR VL
MedKLIP [53] ResNet-50 MIMIC-CXR VL
MFLAG [32] ResNet-50 MIMIC-CXR VL
MRM [58] ViT MIMIC-CXR VL
Table 1: Overview of evaluated chest X-ray models, their backbone architectures, training
datasets, and training objectives.
Dataset Counts Annotations
Images Reports Images Reports
ChestX-ray14 [49] 112k✗∼ ∼∼1 Automatic
CheXpert [26] 224k 224k∼ ∼∼2 Automatic
MIMIC-CXR [28] 377k 228k✗Automatic
BRAX [40] 40k✗ ✗Automatic
PadChest [4] 169k 110k✗Hybrid
OpenI [14] 8k 4k✗Manual
RSNA Pneumonia [46] 26k✗ ✓ ✗
VinDr-CXR [35] 18k✗ ✓ ✗
XQA-RR 650 650✓ ✓
1 Image annotations have been annotated previously, but for a different label set
than the report annotations, and are no longer publicly available [33].
2 Image annotations exist for 500 images, for which reports and report annotations
are nonexistent.
Table 2: Comparison of prevalent chest X-ray datasets with respect to availability of reports
and annotation sources.
8

XQA-Chest
RR
650 Studies
sampled from
~100K

 RR - Image Annotations
 Stage 1 - Annotation
Two consultant radiologists
Experience 4-6 years
Tool: speedyQC
 Stage 2 - Conflict Resolution
By a senior clinician
Experience 20+ Years
Tool: speedyQC
 Pathology Labels
14 Pathologies prevalent in CXRs
Labels:
Positive
Negative
Uncertain
 RR - Report Annotations
 Annotation
T w o cons u l t an t  radiolo g is t s
Experience 4-6  years
Tool: IN CEpT ION
 Pathology Labels
14 Pathologies prevalent in CXRs
Labels:
Positive
Negative
Uncertain
Not Mentioned

(a)XQA-RR:enables comparison of chest X-ray pathology la-
beling sources.
IQA
1571 degraded
images from 323
reference
images

XQA-Chest
 IQA - Image Annotations
 Annotation
5 annotators:
3 consultant radiologists
1 trainee radiologist
1 senior radiographer
Tool: speedyIQA
 Quality Labels
Ratings of degraded image data
Likert Scale labels:
1 (very poor)
2 (poor)
3 (good)
4 (very good)
(b)XQA-IQA:allows com-
parison of IQA metrics to ex-
pert judgments of clinical rel-
evance of CXR images.
Figure 3: Overview XQA-Chest.
examinedisagreementbetweenimage-derivedandreport-derivedlabelsonpaired
studies, they do not release such paired expertly-annotated labels as a pub-
lic benchmark or systematically analyze how evaluation reference choice af-
fects downstream conclusions; instead, expert image-derived labels are typically
treated as the evaluation reference, despite the underlying assumption of their
ground-truth status remaining largely untested [20, 27]. To enable this analysis,
we collected XQA-RR (Figure 3a) from a cohort of 650 patient studies acquired
atCambridgeUniversityHospitals(CUH)between2019and2021, eachcompris-
ing a frontal chest radiograph (AP/PA) and a paired radiology report. Patient
studies were sampled to ensure representation of both normal and abnormal
examinations across 14 finding categories aligned with CheXpert/MIMIC-CXR
conventions. Cases with missing reports, non-diagnostic image quality, or du-
plicate examinations from the same encounter were excluded, and sampling was
stratified to reduce extreme class imbalance and fair demographic representa-
tion.
Images and reports were independently annotated by two consultant radiolo-
gists to avoid influence between image and report annotation sources. For image
annotation, each radiograph was reviewed in an image-only setting (no report or
clinical history) using SpeedyQC [45], and each finding was labeled asnegative,
uncertain, orpositive, with optional bounding box localization. Disagreements
between the two annotators were resolved by a senior radiologist, producing
adjudicated image-derived labels, which we refer to as conflict-resolved (CR)
9

image-derived labels. Reports were annotated separately in INCEpTION [31],
where the same two radiologists labeled the paired reports without viewing the
images. For each finding category, reports were assigned one of four values:
negative,uncertain,positive, ornot mentioned.
To complement XQA-RR with a publicly available dataset, we additionally
annotated a subset of MIMIC-CXR [28]. We selected 735 frontal (AP/PA) chest
radiographs from the MIMIC-CXR expert-annotated test set, augmenting the
selection to better reflect the demographic distribution of the broader MIMIC-
CXR population. All selected patient studies include paired radiology reports.
Images were annotated by two radiologists using SpeedyQC under the same
image-only protocol as CUH: each finding was labeled asnegative,uncertain,
orpositive, without access to the paired reports. Unlike CUH, no adjudication
step was performed; instead, we derive a consensus label using automatic fusion
of image annotator labels (Section 2.1.3), which we validate against the conflict-
resolved image-derived labels for XQA-RR. Reports were annotated manually
by the same annotators using INCEpTION, independently for the Findings and
Impressions sections of each report, without viewing the images. This yields two
distinct report-derived label sets per study, enabling direct analysis of within-
report label agreement as an additional source of annotation variability.
Because several pathologies are rare in these datasets, the primary compar-
ative analysis is restricted to four selected pathologies with at least 50 positive
cases in either the image-derived or report-derived reference: Atelectasis, Con-
solidation, Lung opacity, and Pleural effusion. Support devices and No find-
ing are excluded from pathology-focused analyses, although the full annotation
schema is retained for dataset-level summaries where stated explicitly. Positive
prevalence for XQA-RR and MIMIC-CXR is summarized in Tables A.5 and A.6,
with full label distributions for the full annotation schema provided in Appendix
Tables A.7 and A.8.
We analyze differences between label sources using both omission analysis
and agreement metrics. Omission analysis identifies cases where a positive find-
ing in one label source is absent or negative in the other, providing insight into
systematic differences in what each label source captures.
We quantify inter-annotator agreement and agreement between label sources
using quadratically weighted Cohen’sκ[8, 9]. Cohen’sκmeasures agreement
beyond chance and is defined as:
κ= po −p e
1−p e
,
wherep o is the observed agreement andp e is the expected agreement under
chance, estimated from the empirical marginal label distributions. To account
for the ordinal structure of labels (negative<uncertain<positive), quadrati-
cally weightedκpenalizes larger disagreements more strongly.
Because uncertainty handling can substantially affect agreement estimates,
we additionally compute unweighted Cohen’sκunder two binary mappings,
following Jain et al. [27]. In the optimistic mapping (High–κ), uncertain labels
are treated as agreement with the corresponding definitive label, whereas in
10

the pessimistic mapping (Low–κ), uncertain labels are treated as disagreement.
These Low–κand High–κvalues are reported alongside the central quadratically
weightedκestimate. Weighted F1-scores are reported in the Appendix for
completeness.
For XQA-RR, we also performed a qualitative review of image–report label
disagreements. The review was conducted by the adjudicating radiologist.
2.1.3. Label aggregation and supervised fusion methods
We evaluate several automatic label fusion methods for combining multiple
image-derived labels into a single consensus label. Their agreement with the
adjudicated reference is assessed on XQA-RR, where conflict-resolved image-
derived labels provide an evaluation reference, and the resulting methods are
then applied to MIMIC-CXR, where no adjudicated labels are available. Specif-
ically, we derive a single consensus label from two image annotator labels using
methods defined on the label spaceY={negative,uncertain,positive}, applied
independently for each pathology. We compare the following fusion methods:
Majority vote (MV).MV assigns each study the label chosen by the majority
of annotators; ties resolve touncertain. It serves as a non-parametric baseline,
treating all annotators equally.
Deterministic pairwise fusion.For two annotators with labelsa, b∈ Y, three
fixed rules handle disagreements differently. FUSE_OR resolves any conflict
involving a positive to positive (optimistic); FUSE_AND requires both anno-
tators to agree on positive (conservative).
Dawid–Skene (DS) and MACE.Bothareprobabilisticcrowdmodelsthatjointly
infer a latent consensus label and per-annotator reliability. Dawid–Skene [13]
models each annotator by a full confusion matrix estimated via Expectation-
maximization (EM); MACE [23] additionally estimates annotator competence,
down-weighting unreliable annotators.
Neural fusion (NN Fusion) training.We trained a multilayer perceptron to
predict conflict-resolved image-derived labels from the one-hot encoded label
pair of both annotators, concatenated across allKpathologies. The network is
trained with pathology-wise class-weighted cross-entropy, with model selection
via 5-fold cross-validation using macro-F1 on four key pathologies (Consolida-
tion, Pleural effusion, Lung opacity, Atelectasis) as the stopping criterion. A
pathology-specific variant (NN Fusion PS) replaces global predictions with ded-
icated specialist models for those four pathologies, combining shared statistical
strength with pathology-level specialization.
2.2. Image Quality Assessment
Letx∈ Xdenote a reference chest radiograph and˜x∈ Xa degraded version
of the same image. An IQA metric can be viewed as a function:
m:X × X →R,
11

which assigns a quality scoreq=m(x,˜x)reflecting the perceived similarity or
fidelity between the two images.
Given a set of degraded images{˜xi}n i=1 derived from multiple reference im-
ages, eachIQAmetricinducesarankingoverimagesaccordingtotheirpredicted
quality scores. Independently, expert annotators provide ordinal ratings of di-
agnostic usability for the same images, inducing a reference ranking based on
human judgment.
The IQA evaluation problem can therefore be formulated as the following:
we assess how well the ranking induced by an IQA metricmaligns with the
ranking induced by expert opinion. In Subsection 2.3, we introduce the statistics
utilized for measuring ranking agreement.
We evaluate a range of full-reference (FR) and no-reference (NR) IQA met-
rics commonly used in medical imaging, including PSNR [18], SSIM variants
[50], HaarPSI [41], SNR [18], and NIQE [34]. Most IQA measures differ in their
sensitivity to structural distortions, contrast changes, and noise. However, they
have not been designed for the medical image domain, and are rarely validated
against expert judgment in clinical imaging [3].
We enable comparison between metric-based and expert-based quality judg-
ments by constructing XQA-IQA (Figure 3b). We sample 323 reference frontal
CXRs from CUH clinical scanners, each subjected to a set of controlled degra-
dations directly from the scanner’s visualization settings, such as contrast or
sharpness, yielding a total of 1,571 altered images. The reference images were
selected according to the preferred settings of the clinicians in charge. These im-
ages were rated independently by radiologists and reporting radiographers using
a four-point Likert scale reflecting diagnostic usability using the SpeedyIQA app
[44]. This design enables direct comparison between metric-based rankings and
expert rankings of image quality, as well as analysis of inter-rater variability.
To account for individual rating biases, raw Likert scores are normalized per
annotator using z-score standardization. Specifically, for annotatoraand image
i, the z-score is:
zi,a = ri,a −µ a σa ,
wherer i,a is the raw rating, andµa andσ a are the mean and standard deviation
of annotatora’s ratings across all images. The z-score Mean Opinion Score (z-
MOS) for imageiis then defined as the mean z-score across allAannotators:
z-MOSi = 1 A
AX
a=1
zi,a.
2.3. Ranking Stability Metrics
We focus on rank-based analyses rather than absolute performance to de-
termine how the pathology classification evaluation reference and IQA method
affect conclusions about model performance and image quality, respectively. We
employ Spearman’s rank correlation coefficient (SRCC) [47] and Kendall’s rank
correlation coefficient (KRCC) [30] to quantify ranking stability across evalua-
tion references.
12

Spearman’s Rank Correlation Coefficient (SRCC).Given two rankings{Ri}n i=1
and{S i}n i=1 over the same set ofnmodels or image outputs, SRCC is defined
as:
ρs = 1− 6 Pn i=1 d2 i n(n2 −1) ,
whered i =R i −S i denotes the difference between the ranks assigned to itemi
under the two evaluation references. SRCC takes values in the interval[−1,1],
with higher values indicating stronger agreement between rankings.
Kendall’s Rank Correlation Coefficient (KRCC).KRCC measures the corre-
spondence between two rankings by considering all unordered pairs of items.
For a given pair(i, j), the rankings are said to beconcordantif both rankings
agree on their ordering, anddiscordantotherwise. LetCandDdenote the
number of concordant and discordant pairs, respectively. KRCC is then defined
as:
τ= C−D 1
2 n(n−1) .
For pathology classification ranking analyses on XQA-RR and MIMIC-CXR,
SRCC and KRCC uncertainty was estimated using 1000 bootstrap replicates
over patient studies [16]. In each replicate, we computed ROC-AUCs for each
model and evaluation reference, derived the corresponding model rankings, and
calculated rank correlations between references. We report 95% percentile con-
fidence intervals from the resulting bootstrap distributions.
3. Results
Wefirstpresentresultsforpathologyclassification, examininghowthechoice
of evaluation reference affects labels and conclusions about model performance.
We then report the image quality assessment results, comparing algorithmic
metrics against expert judgments of diagnostic usability.
3.1. Image Classification Models
We begin by analyzing differences between image-derived and report-derived
label sources, including omission patterns, agreement, and uncertainty sensitiv-
ity. We then examine whether these differences affect ROC-AUC estimates and
model rankings.
3.1.1. Quantitative Analysis of XQA-RR and MIMIC-CXR Labels.
Agreementresultsarepresentedinthemaintextusingquadraticallyweighted
κas the central estimate, with Low–κand High–κindicating unweighted Co-
hen’sκunder pessimistic and optimistic uncertainty mappings. Weighted F1
results follow the same qualitative trends and are reported in the Appendix for
completeness. Unless otherwise stated, reportedκvalues refer to the central
quadratically weightedκestimate.
13

Bidirectional omission patterns show substantial asymmetry between image-
derived and report-derived references (Figure 4). These differences are strongly
pathology-dependent. ForAtelectasis(Figure4b), mostpositiveconflict-resolved
(CR) pathologies are not labeled as positive in the reports (123 165 = 75%). For
Consolidation (Figure 4c), the opposite pattern is observed: most positive
report-derived labels are not labeled as positive in the CR image-derived la-
bels ( 93 148 = 63%). Across all 12 pathologies (Figure 4e), 469 of 794 positive
CR image-derived labels (59%) were labeled negative in the reports, whereas
245 of 618 positive report-derived labels (40%) were labeled negative in the
CR image-derived labels. CR image-derived labels also contain substantially
more uncertain values than report-derived labels (248 vs. 80), corresponding to
uncertain-to-positive ratios of 31% and 13%, respectively. These asymmetric
patterns of omission and uncertainty indicate that the two label sources differ
both in the frequency of positive labels and in the findings they capture.
Agreement is substantially lower for image annotators than for report anno-
tators across the four selected pathologies (Figure 5; Tables B.9 and B.10 in the
Appendix). Among image annotators, Atelectasis has the lowest quadratically
weightedκagreement (κ= 0.15), indicating the greatest ambiguity, whereas
Pleural effusion has the highest (κ= 0.67). Image inter-annotator agreement is
also sensitive to uncertainty handling, as shown by the wide low–highκinter-
vals. By contrast, the report inter-annotator agreement is consistently high (κ:
0.80–0.94) and shows narrower uncertainty intervals, indicating greater internal
reproducibility.
Cross-source agreement between conflict-resolved (CR) image-derived labels
and radiology report-derived labels is lower than report inter-annotator agree-
ment and remains similar across the two report annotators (Table B.11). Con-
solidation shows the lowest cross-source agreement (κ≈0.22), despite having
the highest report inter-annotator agreement (κ= 0.94), whereas Pleural effu-
sion shows the highest cross-source agreement (κ≈0.55).
Figure 6 reports agreement between each aggregation algorithm and the
CR reference; the corresponding weighted F1 results and the detailed tables
are shown in Appendix Figure C.15 and Table F.30. With two annotators,
Majority Vote (MV), which maps disagreements touncertain, yields nominally
high quadratically weightedκvalues (0.76–0.87) but extremely wide Low–κto
High–κintervals, withκ low as low as 0.14 for Atelectasis. This reflects strong
sensitivity to uncertainty handling, because all MV disagreements are assigned
to the uncertain class. FUSE_AND and DS-EM perform poorly on the harder
pathologies (Atelectasisκ= 0.21and0.23, respectively; Consolidationκ= 0.57
and0.60). FUSE_OR, MACE, and both neural fusion variants achieve the
highest quadratically weightedκagreement with CR alongside tighter uncer-
tainty intervals: FUSE_OR and MACE reachκ≈0.90for both Consolidation
and Atelectasis. NN Fusion and NN Fusion (PS) further improve on Atelectasis
(both withκ= 1.00) and achieve a macro-averageκof0.89–0.90across the four
selected pathologies—the highest of all methods.
Figure 7 summarizes agreement scores on MIMIC-CXR for image anno-
tators, between labels derived from the Findings and Impressions sections of
14

(a) Pleural effusion
 (b) Atelectasis
(c) Consolidation
 (d) Lung opacity
(e) Overall across 12 pathologies.
Figure4: Sankeydiagramsshowingagreementandomissionpatternsbetweenconflict-resolved
(CR) image-derived labels and report-derived labels from annotator 1. Each flow represents
the number of cases across the three label states (positive (Pos), uncertain (Unc), negative
(Neg)), revealing the types and frequencies of agreement and disagreement between label
sources. Results are shown for pathologies with more than 50 positive labels in either source
(Figures 4a–4d), as well as across all 12 pathologies (Figure 4e).
15

Atelectasis Consolidation Lung opacityPleural effusionMacro average
1.0
0.5
0.0
0.5
1.0
Cohen's
Image inter-annotator
Report inter-annotator
Image-report (CR vs Rep1)
Image-report (CR vs Rep2)
Figure 5: XQA-RR inter-annotator and cross-source label agreement summarized usingκ-
based agreement statistics: image inter-annotator, report inter-annotator, and cross-source
conflict-resolved (CR) image-derived labels vs. report-derived labels from both annotators
(Rep1/Rep2). Intervals indicate unweighted Cohen’sκunder pessimistic and optimistic un-
certainty mappings, denoted Low–κand High–κ, respectively; central points indicate the
quadratically weightedκcomputed using the original label values. Macro-average scores are
calculated across the four selected pathologies. The corresponding weighted F1 results, which
show the same qualitative pattern, are reported in Appendix Figure C.16.
Atelectasis Consolidation Lung opacityPleural effusionMacro average
1.0
0.5
0.0
0.5
1.0
Cohen's
MV
DS
FUSE-OR
FUSE-AND
MACE
NN
NN-PS
Figure 6: Agreement between each image-derived label fusion method and the XQA-RR
conflict-resolved (CR) image-derived labels, summarized usingκ-based agreement statistics.
Intervals indicate unweighted Cohen’sκunder pessimistic and optimistic uncertainty map-
pings, denoted Low–κand High–κ, respectively; central points indicate the quadratically
weightedκcomputed using the original label values. Macro-average scores are calculated
across the four selected pathologies. The corresponding weighted F1 results, which follow the
same qualitative trends, are reported in Appendix Figure C.15.
16

the same radiology report, and between FUSE_OR image aggregation labels
and the labels derived from each report section. We focus on FUSE_OR be-
cause it showed strong agreement with the conflict-resolved XQA-RR reference
while remaining a simple, non-black-box fusion rule. Tables B.12–B.15 in the
Appendix provide detailed metrics for additional fusion methods. The image
inter-annotator agreement pattern mirrors XQA-RR: quadratically weightedκ
agreement is low across the four selected pathologies, with Pleural effusion again
the most consistently annotated finding (κ= 0.62). However, the pathology-
specific profile differs: Lung opacity shows substantially lower agreement on
MIMIC-CXR (κ= 0.11) than on XQA-RR (κ= 0.42), while Atelectasis is
slightly higher (κ= 0.27vs.0.15).
Labels derived from the Impressions and Findings sections, although orig-
inating from a single document written by the same radiologist, disagree sub-
stantially: macro-averageκ= 0.31, with Atelectasis as low asκ= 0.20and
Pleural effusion atκ= 0.33. This shows that report-derived labels can vary
substantially depending on which section of the report is annotated.
For fused image-derived labels and each report section, agreement is low
across both report sections. Against the Findings section labels, FUSE_OR
agrees with Consolidation with rates ofκ= 0.08, Lung opacityκ= 0.21, and
Atelectasisκ= 0.17; Pleural effusion is again the most stable (κ= 0.45).
Agreement against labels derived from the Impressions section is even lower for
all four pathologies (with correspondingκscores of0.06,0.13,0.13and0.35),
reflecting additional divergence introduced by the Impressions section.
Atelectasis Consolidation Lung opacityPleural effusionMacro average
1.0
0.5
0.0
0.5
1.0
Cohen's
Image inter-annotator
Report Impr. vs Find.
Image-report (FUSE-OR vs Find.)
Image-report (FUSE-OR vs Impr.)
Figure 7: MIMIC-CXR image inter-annotator agreement, agreement across labels derived
from the Impression (Impr.) and Findings (Find.) sections, and cross-source agreement
between fused image-derived labels (FUSE_OR) and labels derived from the report Findings
and Impressions sections, summarized usingκ-based agreement statistics. Intervals indicate
unweighted Cohen’sκunder pessimistic and optimistic uncertainty mappings, denoted Low–κ
and High–κ, respectively; central points indicate quadratically weightedκcomputed using the
original three-class label values. Macro-average scores are calculated across the four selected
pathologies. The corresponding weighted F1 results, which show the same qualitative pattern,
are reported in Appendix Figure C.17.
17

3.1.2. Qualitative analysis of XQA-RR disagreements.
The adjudicating radiologist of XQA-RR noted that many disagreements
stemmed from the difficulty of interpreting imaging signs without access to clin-
ical history. For example, Lung opacity is a broad descriptor of increased den-
sity, whereas Consolidation refers more specifically to airspace filling processes
that may arise from infection, pulmonary edema, or pulmonary hemorrhage.
In routine clinical reporting, radiologists often use contextual information to
distinguish between these possibilities. In the absence of such context, annota-
tors may differ in whether they assign a broad label (e.g. Lung opacity) or a
more specific one (e.g. Consolidation or Edema). Other disagreements reflected
a distinction between describing visible imaging signs and inferring higher-level
diagnostic impressions.
3.1.3. Model performance across evaluation references.
ROC-AUC results for all models across the four selected pathologies and
label sources are reported in Tables D.16–D.25 in the Appendix. Some near-
random performance is expected from the training label sets of the correspond-
ing models: D-RSNA performs non-randomly only for Lung opacity, consistent
with its training on the RSNA Pneumonia Detection Challenge, whereas D-NIH,
D-PC, and JFH produce non-informative predictions for Lung opacity because
this finding is not included in their training label sets (Table 1). Several zero-
shot vision-language models also yield AUC values below 0.500 for Atelectasis
andConsolidation, indicatingthattheirsimilarityscoresareinverselyassociated
with the positive label for these pathologies.
The choice of label source affects apparent absolute ROC-AUC values. On
XQA-RR, models achieve a mean AUC of0.77against CR image-derived la-
bels for Lung opacity, compared with0.73–0.74against report-derived labels
(Table D.18). A similar directional pattern holds for Consolidation (0.77vs.
0.71–0.71; Table D.17). These differences indicate that evaluation-reference
choice can change the apparent absolute performance of models, motivating the
ranking-stability analysis below.
3.1.4. Model ranking stability across evaluation references.
To determine whether label source affects not only absolute ROC-AUC but
also the relative ordering of models, Figures 8 and 9 report Spearman rank
correlation coefficients (SRCC) between model rankings induced by each label
source for XQA-RR and MIMIC-CXR, respectively. The corresponding Kendall
rank correlation coefficients (KRCC), which show the same qualitative trends,
arereportedintheAppendix(FiguresC.18andC.19). Fullnumericalresultsare
in Tables E.26–E.29 in the Appendix. Values close to 1 indicate that two label
sources induce similar model rankings, whereas lower values indicate greater
sensitivity of model ordering to the evaluation reference.
Across the selected pathologies, SRCC values broadly track agreement be-
tween label sources, but the strength of this relationship varies by model family
(Figures 8 and 9; Tables E.26–E.29). In the All-models comparison, Pleural
18

Atelectasis Consolidation Lung opacity Pleural effusion Macro average
1.0
0.5
0.0
0.5
1.0
SRCC
All Models
VLM-0-SHOT
VLM-FT
XRV
CR vs Rep1
CR vs Rep2
Figure 8: XQA-RR rank correlation coefficients between model rankings induced by each
pair of label sources, measured by Spearman rank correlation coefficient (SRCC). CR denotes
conflict-resolved image-derived labels; Rep1/Rep2 denote report-derived labels from the two
report annotators. Results are broken down by pathology and model group. Macro average
refers to rankings induced by ROC-AUC macro-averaged across the four selected pathologies.
The corresponding Kendall rank correlation coefficients (KRCC), which show the same qual-
itative pattern, are reported in Appendix Figure C.18.
effusion, which has the highest cross-source label agreement, also shows the
highest rank stability (SRCC≈0.96). Atelectasis and Consolidation, which
have lower cross-source label agreement, show lower overall SRCC values (At-
electasis≈0.80–0.87, Consolidation≈0.88–0.89). This instability is particu-
larly important for fine-tuned VLMs (VLM-FT), which include several of the
highest-performing models in absolute ROC-AUC terms: for Atelectasis, VLM-
FT rankings induced by CR image-derived labels and report-derived labels are
close to uncorrelated (Atelectasis SRCC≈0.21±0.22). Instability within this
family, therefore, directly affects which models appear best under each evalua-
tion reference. XRV models are generally more stable across label sources than
VLM-FT models, especially for pathologies with higher cross-source agreement.
The corresponding KRCC results follow the same qualitative pattern and are
reported in the Appendix.
Lungopacitypresentsanotabledeparturefromtheagreement–rank-stability
pattern. Despite having moderate quadratically weightedκcross-source label
agreement on XQA-RR (κ= 0.42), its All-models cross-source SRCC (0.80–
0.81) is comparable to that of Atelectasis (0.80–0.87), which has lower cross-
source agreement. This indicates that cross-source label agreement alone does
not fully explain ranking stability. One possible explanation is that models
achieve similar AUCs for Lung opacity (Table D.18), so small absolute perfor-
mance differences translate into larger rank changes.
Aggregate rank correlations can obscure practically important instability at
the top of the ranking, where model selection decisions are made. Figures 10a–
14a visualize XQA-RR model rankings across label sources for each pathology
and for the macro-average across the four selected pathologies. Figures 10b–14b
show the equivalent rankings for MIMIC-CXR.
19

Atelectasis Consolidation Lung opacity Pleural effusion Macro average
1.0
0.5
0.0
0.5
1.0
SRCC
All Models
VLM-0-SHOT
VLM-FT
XRV
Fuse-OR vs Find.
Fuse-OR vs Impr.
Figure 9: MIMIC-CXR rank correlation coefficients between model rankings induced by each
pair of label sources, measured by Spearman rank correlation coefficient (SRCC). FUSE_OR
denotes automatically fused image-derived labels; Find. and Impr. denote labels derived from
the Findings and Impressions sections of the radiology report. Results are broken down by
pathology and model group. Macro average refers to rankings induced by ROC-AUC macro-
averaged across the four selected pathologies. The corresponding Kendall rank correlation
coefficients (KRCC), which show the same qualitative pattern, are reported in Appendix
Figure C.19.
On XQA-RR, the choice of evaluation reference often changes which model
appears best. For Atelectasis (Figure 10a), GLORIA-G-CUH ranks first under
both report-derived labels, yet falls to 9th when evaluated against CR image-
derived labels. Conversely, MRM-CUH ranks first under CR image-derived
labels but falls to 4th when evaluated against both report-derived references.
For Consolidation (Figure 11a), the model ranked first under CR image-derived
labels is ranked 13th under the report-derived labels. For Lung opacity (Fig-
ure 12a), MRM-CUH remains the top-ranked model across all evaluation ref-
erences, although substantial reordering is still observed among the remaining
high-performing models. Pleural effusion shows the greatest top-rank stability,
consistent with its higher cross-source agreement (Figure 13a). In the macro-
average across the four selected pathologies, MRM-CUH remains consistently
top-ranked, but instability persists among near-best alternatives (Figure 14a).
Thus, reference choice affects not only the overall ordering of models, but also
which models would be selected as best-in-class or near-best alternatives.
A similar pattern is observed on MIMIC-CXR (Figures 10b–14b). Chang-
ing the label source (FUSE_OR vs. Findings vs. Impressions) produces larger
changes for Atelectasis and Consolidation than for Pleural effusion.
On XQA-RR, the rankings induced by the two report annotators are highly
consistentacrossthefourselectedpathologies, indicatingthatevaluationagainst
report-derived labels is internally reproducible across annotators even when it
diverges from evaluation against CR image-derived labels. On MIMIC-CXR,
however, rankings derived from the Findings and Impressions section labels
of the same report, as annotated by the same radiologist, are substantially
less consistent with each other (Figures 10b–14b; Figures G.25a–G.25e in the
Appendix). Thus, the report section used for label derivation is itself a source
20

Rep1 Rep2 CR
Evaluation references
5
10
15
20
25
30
35 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT
(a) XQA-RR
Impression FUSE_OR Findings
Evaluation references
5
10
15
20
25 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT (b) MIMIC-CXR
Figure 10: Model rankings across label sources forAtelectasis.
of evaluation variability and can affect conclusions about which models perform
best.
3.2. IQA
Table 3 reports inter-rater agreement between each annotator’s ranking of
degraded images and the z-MOS, measured by SRCC and KRCC. Most annota-
tors show high agreement with the z-MOS ranking, with SRCC values ranging
from0.83to0.88. Ann. 4 is the sole exception, achieving a notably lower SRCC
of0.65.
Ann. 1 Ann. 2 Ann. 3 Ann. 4 Ann. 5 z-MOS
Ann. 1 — 0.69 / 0.60 0.65 / 0.57 0.48 / 0.43 0.74 / 0.67 0.88 / 0.76
Ann. 2 — — 0.72 / 0.65 0.34 / 0.28 0.70 / 0.61 0.83 / 0.69
Ann. 3 — — — 0.46 / 0.40 0.69 / 0.60 0.86 / 0.73
Ann. 4 — — — — 0.51 / 0.46 0.65 / 0.54
Ann. 5 — — — — — 0.87 / 0.74
z-MOS — — — — — —
Table 3: SRCC/KRCC between each annotator’s ranking and the z-score MOS ranking for
the CXR images in the XQA-IQA dataset.
21

Rep1 Rep2 CR
Evaluation references
5
10
15
20
25
30
35 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT
(a) XQA-RR
Impression FUSE_OR Findings
Evaluation references
5
10
15
20
25 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT (b) MIMIC-CXR
Figure 11: Model rankings across label sources forConsolidation.
Rep1 Rep2 CR
Evaluation references
5
10
15
20
25
30
35 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT
(a) XQA-RR
Impression FUSE_OR Findings
Evaluation references
5
10
15
20
25 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT (b) MIMIC-CXR
Figure 12: Model rankings across label sources forLung opacity.
22

Rep1 Rep2 CR
Evaluation references
5
10
15
20
25
30
35 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT
(a) XQA-RR
Impression FUSE_OR Findings
Evaluation references
5
10
15
20
25 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT (b) MIMIC-CXR
Figure 13: Model rankings across label sources forPleural effusion.
Rep1 Rep2 CR
Evaluation references
5
10
15
20
25
30
35 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT
(a) XQA-RR
Impression FUSE_OR Findings
Evaluation references
5
10
15
20
25 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT (b) MIMIC-CXR
Figure 14: Model rankings across label sources, macro-averaged across the four selected
pathologies.
23

FR-IQA
SSIM-matlab 0.78 / 0.57
MS-SSIM-matlab 0.84 / 0.63
IW-SSIM-matlab 0.80 / 0.59
CW-SSIM-matlab 0.49 / 0.35
PSNR-matlab 0.52 / 0.37
RMSE-matlab 0.66 / 0.48
DISTS-matlab 0.82 / 0.60
DISTS-python-pytorch 0.82 / 0.60
DSS-matlab 0.64 / 0.47
FSIM-matlab 0.83 / 0.61
GMSD-matlab 0.86 / 0.65
HaarPSI-matlab 0.87 / 0.66
HaarPSI-python-pytorch 0.84 / 0.63
HaarPSImed-python-pytorch 0.85 / 0.65
LPIPS-python 0.84 / 0.63
MDSI-matlab 0.83 / 0.62
VIF-python-pytorch 0.59 / 0.40
VSI-matlab 0.83 / 0.62
UQI-python 0.50 / 0.35
AMBE-matlab 0.44 / 0.32
NR-IQA
niqe-matlab 0.41 / 0.28
SNR-python 0.21 / 0.14
PAQ2PIQ-python 0.61 / 0.43
piqe-matlab 0.42 / 0.20
Table 4: SRCC/KRCC between the z-MOS
ranking and rankings induced by IQA mea-
sures for CXR images in XQA-IQA.
Table 4 presents the SRCC and
KRCC between the z-MOS ranking and
the rankings induced by each IQA met-
ric. Among FR-IQA metrics, HaarPSI
achieves the highest correlation with ex-
pert judgment (SRCC= 0.87, KRCC=
0.66), followed closely by GMSD (0.86
/0.65)andthemedicallyadaptedHaarP-
SImed variant (0.85/0.65). MS-SSIM,
HaarPSI (Python), and LPIPS also
perform competitively, all reaching an
SRCC of0.84. In contrast, sev-
eral FR-IQA metrics show substantially
weaker correlation: CW-SSIM (0.49),
UQI (0.50), PSNR (0.52), and AMBE
(0.44) fall well below the top perform-
ers. NR-IQA metrics perform poorly
across the board, with PAQ2PIQ being
the only one to achieve moderate correla-
tion (0.61/0.43), while SNR (0.21/0.14),
NIQE (0.41/0.28), and PIQE (0.42/0.20)
show negligible agreement with expert
rankings.
4. Discussion
The central finding of this study is that evaluation reference choice is not
a technical detail: it can change the scientific conclusion about which CXR
models and image processing methods perform best. We show this in two set-
tings that are usually studied separately—pathology classification and image
quality assessment—but that share the same underlying problem: reliance on
proxy evaluation targets whose alignment with clinical judgment is rarely tested.
Across both tasks, changing the evaluation reference changes benchmark rank-
ings in ways that are systematic, clinically interpretable, and consequential for
model selection.
In pathology classification, image-derived and report-derived labels are not
interchangeable. Image inter-annotator agreement is substantially lower than
report inter-annotator agreement, reflecting the different nature of the two an-
notation tasks. Image annotators must interpret visual signs without access
to clinical context, whereas report annotators label text that already encodes
clinical history. The qualitative review of XQA-RR disagreements supports this
interpretation. Annotators varied in whether they apply broad pathologies (e.g.
Lung opacity) or more specific ones (e.g. Consolidation).
The resulting disagreement rates are pathology dependent. Atelectasis is
the most ambiguous pathology for image annotators (κ= 0.15): its radio-
graphic appearance depends heavily on the clinical context. Pleural effusion,
24

by contrast, is the most consistently labeled pathology across all label sources,
reflecting its comparatively visually distinct radiological appearance that can be
recognized without patient history. In Consolidation, report annotators agree
almost perfectly (κ= 0.94), yet cross-source agreement is the lowest among all
selected pathologies (κ≈0.22). Distinguishing consolidation from lung opacity
often requires inferring an underlying etiology (infection, edema, hemorrhage)
that might be available in the radiology report but not from the image. Image
annotators, therefore, frequently label the same finding as opacity, producing
systematic divergence even when report annotators are fully consistent with one
another.
Cross-source disagreements are consistent across both report annotators,
suggesting that they reflect a structural difference between label sources rather
than an artifact of individual raters (Table B.11 in the Appendix). The Sankey
[43] visualizations (Figure 4) further reveal that omission patterns are bidi-
rectional and pathology-specific: neither label source consistently captures all
positives found by the other. Together, these patterns suggest that image-
derived and report-derived labels draw on partially distinct sources of clinical
information even when they are used to evaluate the same nominal pathology.
Comparing CUH and MIMIC-CXR further shows that pathology-specific
annotation difficulty varies across datasets and institutions. Lung opacity, for
example, shows substantiallylowerimage inter-annotator agreementon MIMIC-
CXR than on CUH, while other pathologies show the opposite pattern.
The MIMIC-CXR results also show that report-derived labels are not a sin-
gle, uniform reference source. Labels derived from the Findings and Impres-
sions sections of the same report can differ substantially, and these differences
can propagate to model rankings. This should not be interpreted only as an-
notation noise. Findings sections usually describe radiographic observations,
whereas Impressions correspond to a clinically grounded interpretation of the
examination and thus may incorporate context that is inaccessible from the
image alone. Evaluation studies using report-derived labels should, therefore,
specify which report section is used and justify whether that section is appro-
priate for the intended task.
High aggregate rank correlations do not necessarily imply stable model selec-
tion. The most consequential instability occurs at the top of the ranking, where
practical decisions are made. For Atelectasis and Consolidation, the top-ranked
model under one reference is ranked substantially lower under another, whereas
Pleural effusion shows much greater stability, consistent with its higher cross-
source agreement. The pattern of rank instability across pathologies broadly
mirrors the pattern of cross-source disagreement, supporting the interpretation
that reference choice affects rankings most strongly where image-derived and
report-derived labels encode different clinical information. In practice, a re-
searcher or clinician may select a different best-in-class system depending on
whether the evaluation is based on image-derived or report-derived labels.
At the model-family level, rank stability reflects both cross-source label
agreement and the distribution of model performance within each family. XRV
models maintain stable rankings across label sources for well-agreed patholo-
25

gies, whereas VLM-FT models show near-random rank agreement for Atelecta-
sis (SRCC= 0.21±0.22), consistent with its low cross-source agreement. This
is important because fine-tuned VLMs include several of the strongest models in
absolute ROC-AUC terms: improved absolute performance under one reference
does not guarantee stable ranking under another. One possible explanation for
the greater stability of XRV rankings is stronger performance separation within
this family: pooled or target-adapted XRV models perform substantially better
than models not fine-tuned on the target datasets, producing a more stable or-
dering across references. By contrast, VLM-FT models are all fine-tuned in a
similar setting and cluster more closely in performance, making their rankings
more sensitive to small reference-dependent AUC differences. Zero-shot VLMs
constitute a notable exception to the broader agreement–rank-stability pattern:
despite Lung opacity having moderate cross-source agreement, zero-shot models
show lower rank stability for this pathology than agreement levels alone would
predict. This exception also affects the All-models group. One plausible ex-
planation is score compression: if models achieve similar Lung opacity AUCs,
small absolute differences can translate into larger rank fluctuations.
Evaluationagainstreport-derivedlabelsisinternallyreproduciblebutnotin-
terchangeable with evaluation against image-derived labels. On XQA-RR, the
two report annotators induce highly consistent model rankings, showing that
report-derived evaluation is stable across annotators even when it diverges from
image-derived evaluation. We do not argue that image-derived or report-derived
labels are universally superior. Rather, these references answer different ques-
tions: image-derived labels reflect what is visually recoverable from the radio-
graph alone, whereas report-derived labels reflect a clinically contextualized in-
terpretation intended to guide care. Treating these references as interchangeable
risks drawing misleading conclusions about clinical relevance. This distinction
also affects absolute performance estimates: for pathologies with larger image–
report disagreement, models tend to achieve higher AUC against image-derived
references than against report-derived references, suggesting that image-derived
evaluation may give a more optimistic estimate for models trained to detect
visually recoverable findings. Whereas recent stress-testing work shows that
multimodal health-AI benchmarks can conceal fragility under input perturba-
tions [19], our results identify a distinct source of fragility: the clinical target
encoded by the evaluation reference itself.
Our IQA results reinforce the same conclusion from a complementary angle:
widely used automated evaluation metrics do not necessarily reflect clinically
meaningful judgments of image quality. This is particularly important for im-
age outputs produced by black-box methods, such as neural-network-based re-
construction or generative models, which are often evaluated primarily through
automated IQA measures. Poor alignment between metric scores and expert
judgment may therefore lead to misleading conclusions about clinical usability
and to rankings that fail to reflect even straightforward quality differences [2].
This concern is consistent with prior work showing that standard IQA metrics
often fail to capture expert assessments of medical image quality [3].
Among the full-reference metrics, HaarPSI, GMSD, and HaarPSImed align
26

most closely with expert diagnostic quality rankings, whereas commonly used
metrics such as PSNR and CW-SSIM show substantially weaker agreement.
Metric selection in IQA studies is therefore not a neutral choice: algorithms
that rank highly under PSNR or SNR may differ from those preferred by expert
radiologists, and the choice of metric shapes which post-processing methods
appear clinically effective.
5. Limitations
The employed data set XQA-RR contains 650 CUH and 735 MIMIC-CXR
patient studies, each comprising a frontal chest radiograph and associated re-
port. This sample size supports the agreement and ranking analyses presented,
but remains limited for rare pathologies, several of which were excluded from the
primary analysis due to low positive counts. Image-derived labels relied on two
annotators per dataset; for MIMIC-CXR, no adjudication step was performed,
and FUSE_OR fusion served as a proxy for conflict-resolved image-derived
labels, a choice validated against CUH but not equivalent to third-annotator
adjudication. In addition, annotations for both datasets were produced by radi-
ologists from the same institution, so annotation style and labeling conventions
may reflect a particular clinical culture rather than a universal standard. Fi-
nally, the XQA-IQA evaluation uses controlled synthetic degradations rather
than the complex real-world image quality issues encountered in clinical prac-
tice, which may limit the generalization of the metric rankings to operational
settings.
Future work should examine how automatically extracted report labels, in-
cluding those produced by large language models, affect these conclusions. How-
ever, improved report extraction alone does not eliminate the need to specify
whether the intended reference is an image-visible abnormality, a report-level
clinical interpretation, or diagnostic usability.
6. Summary
We investigated whether conclusions about chest X-ray machine learning are
stable to the choice of evaluation reference. This is important because CXR im-
age classifiers are often trained and evaluated using labels derived from different
sources, while image quality assessment (IQA) methods are commonly judged
using generic metrics rather than expert assessments of diagnostic usability.
In pathology classification, evaluation against image-derived versus report-
derived labels leads to systematic differences in performance estimates and
model rankings. These effects are pathology-dependent: image-derived and
report-derived labels appear more interchangeable for visually well-defined find-
ings such as Pleural effusion, but diverge more strongly for findings such as
Atelectasis, Consolidation, and Lung opacity. These results do not support a
single general recommendation for the use of either image-derived or report-
derived labels. Instead, the evaluation reference should be justified for each
27

pathology and intended application. Image-derived labels are more appropriate
for assessing visual detectability from the radiograph alone, whereas report-
derived labels are more appropriate for assessing alignment with the clinically
contextualized interpretation recorded in the radiology report.
In image quality assessment, automated metrics correlate inconsistently with
expert judgments of diagnostic usability. Some full-reference metrics align rela-
tively well with expert rankings, whereas commonly used metrics such as PSNR
and several no-reference measures align weakly with clinical preference. Thus,
IQA metrics should not be treated as clinical proxies without validation against
expert judgment.
Taken together, these results demonstrate that the choice of evaluation ref-
erence is central to assessing CXR machine learning. Especially when black box
models are judged mainly by benchmark performance, conclusions about utility
depend critically on whether the chosen reference is clinically meaningful. Con-
venient proxy targets, including generic IQA metrics and interchangeable image-
or report-derived labels, should therefore be used only with explicit justification.
To support further research on clinically grounded evaluation, code and cur-
rentdata-accessinformationareavailableathttps://github.com/PanagiotisFytas/
XQA-Chest-X-ray. XQA-Chest comprises 650 patient studies with paired ex-
pert image-derived and report-derived labels for pathology classification, to-
gether with expert ratings of diagnostic image quality from five clinicians for
1,571 degraded images generated from 323 reference images. The dataset will
be released through ReShare following completion of repository review, and the
permanent ReShare link and access instructions will be added to the GitHub
repository. The resource is intended to support reproducible work on clinically
grounded evaluation references for CXR machine learning.
7. Ethics
This study was conducted under ethical approval for the study “AI-assisted
diagnosisandprognosticationinCOVID-19” (REC:20/HRA/2504; IRAS:282705).
The study used retrospective anonymised or pseudo-anonymised data, and the
research team did not have access to direct personal identifiers. Informed con-
sent was not obtained because the study was retrospective and used anonymized
data. Data handling was conducted in accordance with the NHS Code of Prac-
tice on Confidentiality, UK GDPR, and the Data Protection Act 2018.
8. Code availability
Code used for the evaluation experiments is available athttps://github.
com/PanagiotisFytas/XQA-Chest-X-ray.
9. Data availability
The XQA-Chest annotations and image quality assessment ratings are cur-
rently undergoing repository review for release through ReShare. The perma-
28

nent ReShare link, access conditions, and instructions will be added tohttps://
github.com/PanagiotisFytas/XQA-Chest-X-rayfollowingcompletionofrepos-
itory review.
The MIMIC-CXR component of the study is based on the publicly available
MIMIC-CXR dataset, subject to the access conditions of PhysioNet. The anno-
tation labels produced for the study will be made available through the project
GitHub repository. The non-public CUH data used for model fine-tuning can-
not be shared because they derive from clinical data governed by institutional,
ethical, and data-protection restrictions.
10. Funding
P.F. was supported by an award from the Claudia Harding Foundation
throughtheUniversityofCambridgeHardingDistinguishedPostgraduateSchol-
ars Programme. A.B. acknowledges support from the EU/EFPIA Innovative
Medicines Initiative 2 Joint Undertaking through the DRAGON project (Grant
No. 101005122). A.B. and C.K. acknowledge support from the Austrian Science
Fund (FWF) through project T1307. This work was supported by UK Research
and Innovation through the EQUATE grant (EP/Y031350/1) awarded to A.K.
J.H.F.R.ispart-supportedbytheNIHRCambridgeBiomedicalResearchCentre
(NIHR203312) and the British Heart Foundation Centre of Research Excellence
(RE/24/130011).
The funders had no role in study design, data collection, analysis, interpre-
tation, manuscript preparation, or the decision to submit the article for publi-
cation.
11. Author contributions
Panagiotis Fytas: Conceptualization, Methodology, Software, Formal analy-
sis, Data curation, Visualization, Writing – original draft, Writing – review and
editing. Ian Selby: Conceptualization, Investigation, Data curation, Software.
Clemens Karner: Methodology, Software, Formal analysis, Writing – review and
editing. Judith Babar: Investigation, Data curation, Validation, Writing – re-
view and editing. Simon Baker: Supervision, Writing – review and editing. Jake
Beckford: Datacuration, Writing–reviewandediting. TimothyJ.Sadler: Data
curation, Writing – review and editing. Shahab Shahipasand: Data curation,
Writing – review and editing. Arthikkaa Thavakumar: Data curation, Writing –
review and editing. John Li Chen: Data curation, Writing – review and editing.
Alex Sawer: Data curation, Writing – review and editing. Michael Roberts: Su-
pervision, Writing – review and editing. Jonathan Weir-McCall: Investigation,
Writing – review and editing. J.H.F. Rudd: Investigation, Writing – review and
editing. Carola-Bibiane Schönlieb: Supervision, Funding acquisition, Writing –
review and editing. Anna Korhonen: Supervision, Funding acquisition, Writing
– review and editing. Anna Breger: Conceptualization, Methodology, Investiga-
tion, Data curation, Software, Formal analysis, Supervision, Writing – original
draft, Writing – review and editing.
29

12. Declaration of Generative AI and AI-Assisted Technologies in the
Manuscript Preparation Process
During the preparation of this work, the authors used ChatGPT (OpenAI)
to assist in improving the clarity, readability, and organization of the manuscript
text. No AI tool was used to generate experimental results, perform analyses, or
make scientific conclusions. After using this tool/service, the authors reviewed
and edited the content as needed and take full responsibility for the content of
the published article.
References
[1] Brabec, J., Komárek, T., Franc, V., Machlica, L., 2020. On model evalu-
ation under non-constant class imbalance, in: International Conference on
Computational Science, Springer. pp. 74–87.
[2] Breger, A., Biguri, A., Landman, M.S., Selby, I., Amberg, N., Brunner, E.,
Gröhl, J., Hatamikia, S., Karner, C., Ning, L., et al., 2025a. A study of why
we need to reassess full reference image quality assessment with medical
images. Journal of Imaging Informatics in Medicine 38, 3444–3469.
[3] Breger, A., Karner, C., Selby, I., Gröhl, J., Dittmer, S., Lilley, E., Babar,
J., Beckford, J., Else, T.R., Sadler, T.J., Shahipasand, S., Thavakumar,
A., Roberts, M., Schönlieb, C.B., 2025b. A study on the adequacy of com-
mon iqa measures for medical images, in: Su, R., Frangi, A.F., Zhang, Y.
(Eds.), Proceedings of 2024 International Conference on Medical Imaging
and Computer-Aided Diagnosis (MICAD 2024), Springer Nature Singa-
pore, Singapore. pp. 451–462.
[4] Bustos, A., Pertusa, A., Salinas, J.M., de la Iglesia-Vayá, M., 2020. Padch-
est: A large chest x-ray image dataset with multi-label annotated reports.
Medical Image Analysis 66, 101797. URL:https://www.sciencedirect.
com/science/article/pii/S1361841520301614, doi:https://doi.org/
10.1016/j.media.2020.101797.
[5] Cabitza, F., Jurman, G., Molinari, F., Bellazzi, R., 2026. Why almost all
ml models for medicine are wrong-and what we need for evidence-based
medical ai. International Journal of Medical Informatics , 106538.
[6] Chen, T., Kornblith, S., Norouzi, M., Hinton, G., 2020. A simple frame-
work for contrastive learning of visual representations, in: International
conference on machine learning, PmLR. pp. 1597–1607.
[7] Chen, Z., Diao, S., Wang, B., Li, G., Wan, X., 2023. Towards unifying
medical vision-and-language pre-training via soft prompts, in: Proceedings
of the IEEE/CVF International Conference on Computer Vision (ICCV),
pp. 23403–23413.
30

[8] Cohen, J., 1960. A coefficient of agreement for nominal scales. Educational
and Psychological Measurement 20, 37–46.
[9] Cohen, J., 1968. Weighted kappa: Nominal scale agreement provision for
scaled disagreement or partial credit. Psychological bulletin 70, 213.
[10] Cohen, J.P., Hashir, M., Brooks, R., Bertrand, H., 2020. On the limits
of cross-domain generalization in automated x-ray prediction, in: Medical
Imaging with Deep Learning, PMLR. pp. 136–155.
[11] Cohen, J.P., Viviano, J.D., Bertin, P., Morrison, P., Torabian, P., Guar-
rera, M., Lungren, M.P., Chaudhari, A., Brooks, R., Hashir, M., et al.,
2022. Torchxrayvision: A library of chest x-ray datasets and models, in:
International Conference on Medical Imaging with Deep Learning, PMLR.
pp. 231–249.
[12] Davis, J., Goadrich, M., 2006. The relationship between precision-recall
and roc curves, in: Proceedings of the 23rd international conference on
Machine learning, pp. 233–240.
[13] Dawid, A.P., Skene, A.M., 1979. Maximum likelihood estimation of ob-
server error-rates using the EM algorithm. Journal of the Royal Statistical
Society: Series C (Applied Statistics) 28, 20–28.
[14] Demner-Fushman, D., Kohli, M.D., Rosenman, M.B., Shooshan, S.E., Ro-
driguez, L., Antani, S., Thoma, G.R., McDonald, C.J., 2015. Preparing a
collection of radiology examinations for distribution and retrieval. Journal
of the American Medical Informatics Association 23, 304–310.
[15] Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Un-
terthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkor-
eit, J., Houlsby, N., 2021. An image is worth 16x16 words: Transformers
for image recognition at scale, in: International Conference on Learning
Representations.
[16] Efron, B., Tibshirani, R., 1986. Bootstrap methods for standard errors,
confidence intervals, and other measures of statistical accuracy. Statistical
science , 54–75.
[17] Fytas, P., Breger, A., Selby, I., Baker, S., Shahipasand, S., Korhonen, A.,
2024. Can rule-based insights enhance llms for radiology report classifi-
cation? introducing the radprompt methodology., in: Proceedings of the
23rd Workshop on Biomedical Natural Language Processing, pp. 212–235.
[18] Gonzalez, R.C., Woods, R.E., 2008. Digital Image Processing. 3rd ed.,
Pearson.
[19] Gu, Y., Fu, J., Liu, X., Valanarasu, J.M.J., Codella, N.C., Tan, R., Liu,
Q., Jin, Y., Zhang, S., Wang, J., et al., 2026. Evaluating the robustness
and readiness of large frontier models in health ai applications. Nature
Medicine , 1–9.
31

[20] Gündel, S., Setio, A.A., Ghesu, F.C., Grbic, S., Georgescu, B., Maier, A.,
Comaniciu, D., 2021. Robust classification from noisy labels: Integrating
additional knowledge for chest radiography abnormality assessment. Med-
ical Image Analysis 72, 102087.
[21] Hanley, J.A., McNeil, B.J., 1982. The meaning and use of the area under
a receiver operating characteristic (roc) curve. Radiology 143, 29–36.
[22] He, K., Zhang, X., Ren, S., Sun, J., 2016. Deep residual learning for image
recognition, in: Proceedings of the IEEE conference on computer vision
and pattern recognition, pp. 770–778.
[23] Hovy, D., Berg-Kirkpatrick, T., Vaswani, A., Hovy, E., 2013. Learning
whom to trust with MACE, in: Proceedings of the 2013 Conference of the
North American Chapter of the Association for Computational Linguistics:
Human Language Technologies (NAACL-HLT), pp. 1120–1130.
[24] Huang, G., Liu, Z., Van Der Maaten, L., Weinberger, K.Q., 2017. Densely
connected convolutional networks, in: Proceedings of the IEEE conference
on computer vision and pattern recognition, pp. 4700–4708.
[25] Huang, S.C., Shen, L., Lungren, M.P., Yeung, S., 2021. Gloria: A mul-
timodal global-local representation learning framework for label-efficient
medical image recognition, in: Proceedings of the IEEE/CVF International
Conference on Computer Vision, pp. 3942–3951.
[26] Irvin, J., Rajpurkar, P., Ko, M., Yu, Y., Ciurea-Ilcus, S., Chute, C.,
Marklund, H., Haghgoo, B., Ball, R.L., Shpanskaya, K.S., Seekins, J.,
Mong, D.A., Halabi, S.S., Sandberg, J.K., Jones, R., Larson, D.B., Lan-
glotz, C.P., Patel, B.N., Lungren, M.P., Ng, A.Y., 2019. Chexpert: A
large chest radiograph dataset with uncertainty labels and expert compar-
ison. CoRR abs/1901.07031. URL:http://arxiv.org/abs/1901.07031,
arXiv:1901.07031.
[27] Jain, S., Smit, A., Truong, S.Q., Nguyen, C.D., Huynh, M.T., Jain,
M., Young, V.A., Ng, A.Y., Lungren, M.P., Rajpurkar, P., 2021. Visu-
alchexbert: addressing the discrepancy between radiology report labels
and image labels, in: Proceedings of the Conference on Health, Infer-
ence, and Learning, Association for Computing Machinery, New York, NY,
USA. p. 105–115. URL:https://doi.org/10.1145/3450439.3451862,
doi:10.1145/3450439.3451862.
[28] Johnson, A.E.W., Pollard, T., Mark, R., Berkowitz, S., Horng, S.,
2019. The mimic-cxr database. URL:https://physionet.org/content/
mimic-cxr/, doi:10.13026/C2JT1Q.
[29] Karner, C., Gröhl, J., Selby, I., Babar, J., Beckford, J., Else, T.R., Sadler,
T.J., Shahipasand, S., Thavakumar, A., Roberts, M., Rudd, J.H., Schön-
lieb, C.B., Weir-McCall, J.R., Breger, A., 2025. Parameter choices in
32

haarpsiforiqawithmedicalimages, in: 2025IEEE22ndInternationalSym-
posium on Biomedical Imaging (ISBI), pp. 1–5. doi:10.1109/ISBI60581.
2025.10981227.
[30] KENDALL, M.G., 1938. A new measure of rank corre-
lation. Biometrika 30, 81–93. URL:https://doi.org/
10.1093/biomet/30.1-2.81, doi:10.1093/biomet/30.1-2.81,
arXiv:https://academic.oup.com/biomet/article-pdf/30/1-2/81/423380/30-1-2-81.pdf.
[31] Klie, J.C., Bugert, M., Boullosa, B., Eckart de Castilho, R., Gurevych,
I., 2018. The INCEpTION platform: Machine-assisted and knowledge-
oriented interactive annotation, in: Proceedings of the 27th International
Conference on Computational Linguistics: System Demonstrations, Santa
Fe, New Mexico. pp. 5–9. URL:https://www.aclweb.org/anthology/
C18-2002.
[32] Liu, C., Cheng, S., Chen, C., Qiao, M., Zhang, W., Shah, A., Bai, W., Ar-
cucci, R., 2023. M-flag: Medical vision-language pre-training with frozen
language models and latent space geometry optimization, in: Medical Im-
age Computing and Computer Assisted Intervention – MICCAI 2023, pp.
637–647. doi:10.1007/978-3-031-43907-0_61.
[33] Majkowska, A., Mittal, S., Steiner, D.F., Reicher, J.J., McKinney, S.M.,
Duggan, G.E., Eswaran, K., Cameron Chen, P.H., Liu, Y., Kalidindi, S.R.,
et al., 2020. Chest radiograph interpretation with deep learning models: as-
sessment with radiologist-adjudicated reference standards and population-
adjusted evaluation. Radiology 294, 421–431.
[34] Mittal, A., Soundararajan, R., Bovik, A.C., 2012. Making a “completely
blind” image quality analyzer. IEEE Signal processing letters 20, 209–212.
[35] Nguyen, H.Q., Lam, K., Le, L.T., Pham, H.H., Tran, D.Q., Nguyen, D.B.,
Le, D.D., Pham, C.M., Tong, H.T., Dinh, D.H., et al., 2022. Vindr-cxr:
An open dataset of chest x-rays with radiologist’s annotations. Scientific
Data 9, 429.
[36] Oord, A.v.d., Li, Y., Vinyals, O., 2018. Representation learning with con-
trastive predictive coding. arXiv preprint arXiv:1807.03748 .
[37] Powers, D.M., 2020. Evaluation: fromprecision, recallandf-measuretoroc,
informedness, markednessandcorrelation. arXivpreprintarXiv:2010.16061
.
[38] Radford, A., Kim, J.W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S.,
Sastry, G., Askell, A., Mishkin, P., Clark, J., Krueger, G., Sutskever, I.,
2021. Learning transferable visual models from natural language supervi-
sion, in: ICML.
33

[39] Rajpurkar, P., Irvin, J., Ball, R.L., Zhu, K., Yang, B., Mehta, H., Duan,
T., Ding, D., Bagul, A., Langlotz, C.P., et al., 2018. Deep learning for
chest radiograph diagnosis: A retrospective comparison of the chexnext
algorithm to practicing radiologists. PLoS medicine 15, e1002686.
[40] Reis, E.P., De Paiva, J.P., Da Silva, M.C., Ribeiro, G.A., Paiva, V.F.,
Bulgarelli, L., Lee, H.M., Santos, P.V., Brito, V.M., Amaral, L.T., et al.,
2022. Brax, brazilian labeled chest x-ray dataset. Scientific Data 9, 487.
[41] Reisenhofer, R., Bosse, S., Kutyniok, G., Wiegand, T., 2018. A haar
wavelet-basedperceptualsimilarityindexforimagequalityassessment. Sig-
nal Processing: Image Communication 61, 33–43. doi:10.1016/j.image.
2017.11.001.
[42] Roberts, M., Driggs, D., Thorpe, M., Gilbey, J., Yeung, M., Ursprung,
S., Aviles-Rivero, A.I., Etmann, C., McCague, C., Beer, L., et al., 2021.
Common pitfalls and recommendations for using machine learning to detect
and prognosticate for covid-19 using chest radiographs and ct scans. Nature
Machine Intelligence 3, 199–217.
[43] Schmidt, M., 2008. The sankey diagram in energy and material flow man-
agement: part ii: methodology and current applications. Journal of indus-
trial ecology 12, 173–185.
[44] Selby, I., 2026a. Speedy iqa for desktop: An image viewer and labeller for
image quality assessment (iqa).https://github.com/selbs/speedy_iqa.
GitHub repository, accessed 22 April 2026.
[45] Selby, I., 2026b. Speedy qc: Customisable annotation tool for medical
images.https://github.com/selbs/speedy_qc. GitHub repository, ac-
cessed 22 April 2026.
[46] Shih, G., Wu, C.C., Halabi, S.S., Kohli, M.D., Prevedello, L.M., Cook,
T.S., Sharma, A., Amorosa, J.K., Arteaga, V., Galperin-Aizenberg, M.,
et al., 2019. Augmenting the national institutes of health chest radiograph
dataset with expert annotations of possible pneumonia. Radiology: Artifi-
cial Intelligence 1, e180041.
[47] Spearman, C., 1904. The proof and measurement of association between
two things. The American Journal of Psychology 15, 72–101. URL:http:
//www.jstor.org/stable/1412159.
[48] Wang, F., Zhou, Y., Wang, S., Vardhanabhuti, V., Yu, L.,
2022a. Multi-granularity cross-modal alignment for gener-
alized medical visual representation learning, in: Advances
in Neural Information Processing Systems, pp. 33536–33549.
URL:https://papers.nips.cc/paper_files/paper/2022/hash/
d925bda407ada0df3190df323a212661-Abstract-Conference.html.
34

[49] Wang, X., Peng, Y., Lu, L., Lu, Z., Bagheri, M., Summers, R.M.,
2017. Chestx-ray8: Hospital-scale chest x-ray database and benchmarks
on weakly-supervised classification and localization of common thorax dis-
eases. CoRR abs/1705.02315. URL:http://arxiv.org/abs/1705.02315,
arXiv:1705.02315.
[50] Wang, Z., Bovik, A.C., Sheikh, H.R., Simoncelli, E.P., 2004. Image quality
assessment: from error visibility to structural similarity. IEEE transactions
on image processing 13, 600–612.
[51] Wang, Z., Wu, Z., Agarwal, D., Sun, J., 2022b. MedCLIP: Con-
trastive learning from unpaired medical images and text, in: Goldberg,
Y., Kozareva, Z., Zhang, Y. (Eds.), Proceedings of the 2022 Confer-
ence on Empirical Methods in Natural Language Processing, Association
for Computational Linguistics, Abu Dhabi, United Arab Emirates. pp.
3876–3887. URL:https://aclanthology.org/2022.emnlp-main.256,
doi:10.18653/v1/2022.emnlp-main.256.
[52] Williams, C.K., 2021. The effect of class imbalance on precision-recall
curves. Neural Computation 33, 853–857.
[53] Wu, C., Zhang, X., Zhang, Y., Wang, Y., Xie, W., 2023. Medklip: Med-
ical knowledge enhanced language-image pre-training for x-ray diagnosis,
in: Proceedings of the IEEE/CVF International Conference on Computer
Vision (ICCV), pp. 21372–21383.
[54] Ye, W., Yao, J., Xue, H., Li, Y., 2020. Weakly supervised lesion localization
with probabilistic-cam pooling. arXiv preprint arXiv:2005.14480 .
[55] Zhang, L., Zhang, L., Shen, X., Mou, X., 2011. Fsim: A feature similarity
indexforimagequalityassessment. IEEETransactionsonImageProcessing
20, 2378–2386. doi:10.1109/TIP.2011.2109730.
[56] Zhang, Y., Jiang, H., Miura, Y., Manning, C.D., Langlotz, C.P., 2022.
Contrastive learning of medical visual representations from paired images
and text, in: Proceedings of the 7th Machine Learning for Healthcare Con-
ference, PMLR. pp. 2–25. URL:https://proceedings.mlr.press/v182/
zhang22a.html.
[57] Zhou, H.Y., Chen, X., Zhang, Y., Luo, R., Wang, L., Yu, Y., 2022. Gen-
eralized radiograph representation learning via cross-supervision between
images and free-text radiology reports. Nature Machine Intelligence 4, 32–
40. doi:10.1038/s42256-021-00425-9.
[58] Zhou, H.Y., Lian, C., Wang, L., Yu, Y., 2023. Advancing radiograph
representation learning with masked record modeling, in: The Eleventh
International Conference on Learning Representations (ICLR). URL:
https://openreview.net/forum?id=w-x7U26GM7j.
35

[59] Zhou, Y., Faith, T., Xu, Y., Leng, S., Xu, X., Liu, Y., Goh, R.S.M.,
2024. Benchx: A unified benchmark framework for medical vision-language
pretraining on chest x-rays. Advances in Neural Information Processing
Systems 37, 6625–6647.
36

Appendix A. Dataset Label Prevalence
Pathology CR Img1 Img2 Rep1 Rep2
No Finding 121 (18.6%) 91 (14.0%) 129 (19.8%) 16 (2.5%) 20 (3.1%)
Enlarg. Card. 1 (0.2%) 0 (0.0%) 1 (0.2%) 2 (0.3%) 1 (0.2%)
Cardiomegaly 21 (3.2%) 153 (23.5%) 21 (3.2%) 19 (2.9%) 17 (2.6%)
Lung Opacity 187 (28.8%) 197 (30.3%) 131 (20.2%) 200 (30.8%) 171 (26.3%)
Lung Lesion 4 (0.6%) 4 (0.6%) 3 (0.5%) 6 (0.9%) 7 (1.1%)
Edema 4 (0.6%) 1 (0.2%) 1 (0.2%) 11 (1.7%) 11 (1.7%)
Consolidation 106 (16.3%) 110 (16.9%) 66 (10.2%) 154 (23.7%) 151 (23.2%)
Pneumonia 9 (1.4%) 0 (0.0%) 10 (1.5%) 1 (0.2%) 11 (1.7%)
Atelectasis 165 (25.4%) 44 (6.8%) 165 (25.4%) 58 (8.9%) 68 (10.5%)
Pneumothorax 4 (0.6%) 5 (0.8%) 7 (1.1%) 7 (1.1%) 8 (1.2%)
Pleural Eff. 136 (20.9%) 122 (18.8%) 114 (17.5%) 92 (14.2%) 93 (14.3%)
Pleural Other 11 (1.7%) 9 (1.4%) 5 (0.8%) 17 (2.6%) 14 (2.2%)
Fracture 25 (3.8%) 14 (2.2%) 23 (3.5%) 24 (3.7%) 19 (2.9%)
Support Dev. 274 (42.2%) 309 (47.5%) 274 (42.2%) 284 (43.7%) 279 (42.9%)
Table A.5: XQA-RR positive label prevalence per CheXpert pathology and label source,
presented as counts (percentage). Label sources included conflict-resolved image labels (CR),
labels from individual image annotators 1 and 2 (Img1, Img2), and labels from individual
report annotators (Rep1, Rep2).
Pathology Img1 Img2 Find Impr
No Finding 43 (5.9%) 19 (2.6%) 0 (0.0%) 58 (7.9%)
Enlarged Card. 21 (2.9%) 5 (0.7%) 22 (3.0%) 16 (2.2%)
Cardiomegaly 27 (3.7%) 9 (1.2%) 188 (25.6%) 101 (13.7%)
Lung Opacity 23 (3.1%) 150 (20.4%) 213 (29.0%) 142 (19.3%)
Lung Lesion 25 (3.4%) 2 (0.3%) 41 (5.6%) 37 (5.0%)
Edema 7 (1.0%) 3 (0.4%) 106 (14.4%) 102 (13.9%)
Consolidation 181 (24.6%) 40 (5.4%) 37 (5.0%) 44 (6.0%)
Pneumonia 5 (0.7%) 0 (0.0%) 36 (4.9%) 54 (7.3%)
Atelectasis 186 (25.3%) 59 (8.0%) 179 (24.4%) 98 (13.3%)
Pneumothorax 15 (2.0%) 13 (1.8%) 23 (3.1%) 13 (1.8%)
Pleural Eff. 176 (23.9%) 209 (28.4%) 182 (24.8%) 161 (21.9%)
Pleural Other 19 (2.6%) 5 (0.7%) 33 (4.5%) 15 (2.0%)
Fracture 24 (3.3%) 23 (3.1%) 41 (5.6%) 22 (3.0%)
Support Dev. 176 (23.9%) 361 (49.1%) 235 (32.0%) 132 (18.0%)
Table A.6: MIMIC-CXR positive label prevalence per CheXpert pathology and label source,
presented as counts (percentage). Label sources include labels from individual image annota-
tors (Img1 and Img2) and labels from annotations of findings (Find) and impression (Impr)
radiology reports sections.
37

Pathology Source 0 1 2
No Finding CR 526 (80.9%) 3 (0.5%) 121 (18.6%)
Img1 558 (85.8%) 1 (0.2%) 91 (14.0%)
Img2 519 (79.8%) 2 (0.3%) 129 (19.8%)
Rep1 0 (0.0%) 0 (0.0%) 16 (2.5%)
Rep2 1 (0.2%) 0 (0.0%) 20 (3.1%)
Enlarged Cardiomediastinum CR 646 (99.4%) 3 (0.5%) 1 (0.2%)
Img1 647 (99.5%) 3 (0.5%) 0 (0.0%)
Img2 646 (99.4%) 3 (0.5%) 1 (0.2%)
Rep1 96 (14.8%) 24 (3.7%) 2 (0.3%)
Rep2 90 (13.8%) 23 (3.5%) 1 (0.2%)
Cardiomegaly CR 592 (91.1%) 37 (5.7%) 21 (3.2%)
Img1 457 (70.3%) 40 (6.2%) 153 (23.5%)
Img2 592 (91.1%) 37 (5.7%) 21 (3.2%)
Rep1 99 (15.2%) 10 (1.5%) 19 (2.9%)
Rep2 100 (15.4%) 10 (1.5%) 17 (2.6%)
Lung Opacity CR 416 (64.0%) 47 (7.2%) 187 (28.8%)
Img1 400 (61.5%) 53 (8.2%) 197 (30.3%)
Img2 461 (70.9%) 58 (8.9%) 131 (20.2%)
Rep1 8 (1.2%) 2 (0.3%) 200 (30.8%)
Rep2 7 (1.1%) 1 (0.2%) 171 (26.3%)
Lung Lesion CR 642 (98.8%) 4 (0.6%) 4 (0.6%)
Img1 625 (96.2%) 21 (3.2%) 4 (0.6%)
Img2 641 (98.6%) 6 (0.9%) 3 (0.5%)
Rep1 33 (5.1%) 2 (0.3%) 6 (0.9%)
Rep2 34 (5.2%) 2 (0.3%) 7 (1.1%)
Edema CR 622 (95.7%) 24 (3.7%) 4 (0.6%)
Img1 645 (99.2%) 4 (0.6%) 1 (0.2%)
Img2 614 (94.5%) 35 (5.4%) 1 (0.2%)
Rep1 24 (3.7%) 4 (0.6%) 11 (1.7%)
Rep2 23 (3.5%) 2 (0.3%) 11 (1.7%)
Consolidation CR 523 (80.5%) 21 (3.2%) 106 (16.3%)
Img1 533 (82.0%) 7 (1.1%) 110 (16.9%)
Img2 572 (88.0%) 12 (1.8%) 66 (10.2%)
Rep1 132 (20.3%) 13 (2.0%) 154 (23.7%)
Rep2 137 (21.1%) 6 (0.9%) 151 (23.2%)
Pneumonia CR 610 (93.8%) 31 (4.8%) 9 (1.4%)
Img1 650 (100.0%) 0 (0.0%) 0 (0.0%)
Img2 575 (88.5%) 65 (10.0%) 10 (1.5%)
Rep1 1 (0.2%) 1 (0.2%) 1 (0.2%)
Rep2 8 (1.2%) 8 (1.2%) 11 (1.7%)
Atelectasis CR 448 (68.9%) 37 (5.7%) 165 (25.4%)
Img1 586 (90.2%) 20 (3.1%) 44 (6.8%)
Img2 448 (68.9%) 37 (5.7%) 165 (25.4%)
Continued on next page
38

Pathology Source 0 1 2
Rep1 2 (0.3%) 0 (0.0%) 58 (8.9%)
Rep2 34 (5.2%) 3 (0.5%) 68 (10.5%)
Pneumothorax CR 640 (98.5%) 6 (0.9%) 4 (0.6%)
Img1 644 (99.1%) 1 (0.2%) 5 (0.8%)
Img2 638 (98.2%) 5 (0.8%) 7 (1.1%)
Rep1 121 (18.6%) 1 (0.2%) 7 (1.1%)
Rep2 131 (20.2%) 2 (0.3%) 8 (1.2%)
Pleural Effusion CR 482 (74.2%) 32 (4.9%) 136 (20.9%)
Img1 495 (76.2%) 33 (5.1%) 122 (18.8%)
Img2 480 (73.8%) 56 (8.6%) 114 (17.5%)
Rep1 100 (15.4%) 3 (0.5%) 92 (14.2%)
Rep2 120 (18.5%) 6 (0.9%) 93 (14.3%)
Pleural Other CR 638 (98.2%) 1 (0.2%) 11 (1.7%)
Img1 640 (98.5%) 1 (0.2%) 9 (1.4%)
Img2 640 (98.5%) 5 (0.8%) 5 (0.8%)
Rep1 2 (0.3%) 4 (0.6%) 17 (2.6%)
Rep2 23 (3.5%) 2 (0.3%) 14 (2.2%)
Fracture CR 623 (95.8%) 2 (0.3%) 25 (3.8%)
Img1 635 (97.7%) 1 (0.2%) 14 (2.2%)
Img2 625 (96.2%) 2 (0.3%) 23 (3.5%)
Rep1 6 (0.9%) 0 (0.0%) 24 (3.7%)
Rep2 8 (1.2%) 0 (0.0%) 19 (2.9%)
Support Devices CR 357 (54.9%) 19 (2.9%) 274 (42.2%)
Img1 339 (52.2%) 2 (0.3%) 309 (47.5%)
Img2 357 (54.9%) 19 (2.9%) 274 (42.2%)
Rep1 1 (0.2%) 1 (0.2%) 284 (43.7%)
Rep2 1 (0.2%) 1 (0.2%) 279 (42.9%)
Table A.7: XQA-RR label distribution per CheXpert pathology and label source. Label
sources included conflict-resolved image labels (CR), labels from individual image annotators
1 and 2 (Img1, Img2), and labels from individual report annotators (Rep1, Rep2). Values are
shown as count (percentage).
Pathology Source 0 1 2
No Finding Img1 682 (92.8%) 10 (1.4%) 43 (5.9%)
Img2 659 (89.7%) 57 (7.8%) 19 (2.6%)
Find 2 (0.3%) 0 (0.0%) 0 (0.0%)
Impr 0 (0.0%) 0 (0.0%) 58 (7.9%)
Enlarged Cardiomediastinum Img1 665 (90.5%) 49 (6.7%) 21 (2.9%)
Img2 719 (97.8%) 11 (1.5%) 5 (0.7%)
Find 146 (19.9%) 103 (14.0%) 22 (3.0%)
Impr 12 (1.6%) 28 (3.8%) 16 (2.2%)
Continued on next page
39

Pathology Source 0 1 2
Cardiomegaly Img1 655 (89.1%) 53 (7.2%) 27 (3.7%)
Img2 701 (95.4%) 25 (3.4%) 9 (1.2%)
Find 69 (9.4%) 83 (11.3%) 188 (25.6%)
Impr 33 (4.5%) 10 (1.4%) 101 (13.7%)
Lung Opacity Img1 628 (85.4%) 84 (11.4%) 23 (3.1%)
Img2 412 (56.1%) 173 (23.5%) 150 (20.4%)
Find 42 (5.7%) 0 (0.0%) 213 (29.0%)
Impr 4 (0.5%) 0 (0.0%) 142 (19.3%)
Lung Lesion Img1 628 (85.4%) 82 (11.2%) 25 (3.4%)
Img2 666 (90.6%) 67 (9.1%) 2 (0.3%)
Find 10 (1.4%) 9 (1.2%) 41 (5.6%)
Impr 0 (0.0%) 14 (1.9%) 37 (5.0%)
Edema Img1 705 (95.9%) 23 (3.1%) 7 (1.0%)
Img2 647 (88.0%) 85 (11.6%) 3 (0.4%)
Find 79 (10.7%) 16 (2.2%) 106 (14.4%)
Impr 62 (8.4%) 21 (2.9%) 102 (13.9%)
Consolidation Img1 438 (59.6%) 116 (15.8%) 181 (24.6%)
Img2 544 (74.0%) 151 (20.5%) 40 (5.4%)
Find 109 (14.8%) 23 (3.1%) 37 (5.0%)
Impr 26 (3.5%) 13 (1.8%) 44 (6.0%)
Pneumonia Img1 646 (87.9%) 84 (11.4%) 5 (0.7%)
Img2 702 (95.5%) 33 (4.5%) 0 (0.0%)
Find 70 (9.5%) 48 (6.5%) 36 (4.9%)
Impr 54 (7.3%) 81 (11.0%) 54 (7.3%)
Atelectasis Img1 459 (62.4%) 90 (12.2%) 186 (25.3%)
Img2 549 (74.7%) 127 (17.3%) 59 (8.0%)
Find 5 (0.7%) 30 (4.1%) 179 (24.4%)
Impr 3 (0.4%) 38 (5.2%) 98 (13.3%)
Pneumothorax Img1 715 (97.3%) 5 (0.7%) 15 (2.0%)
Img2 718 (97.7%) 4 (0.5%) 13 (1.8%)
Find 335 (45.6%) 10 (1.4%) 23 (3.1%)
Impr 115 (15.6%) 4 (0.5%) 13 (1.8%)
Pleural Effusion Img1 469 (63.8%) 90 (12.2%) 176 (23.9%)
Img2 441 (60.0%) 85 (11.6%) 209 (28.4%)
Find 243 (33.1%) 31 (4.2%) 182 (24.8%)
Impr 37 (5.0%) 26 (3.5%) 161 (21.9%)
Pleural Other Img1 697 (94.8%) 19 (2.6%) 19 (2.6%)
Img2 711 (96.7%) 19 (2.6%) 5 (0.7%)
Find 3 (0.4%) 4 (0.5%) 33 (4.5%)
Impr 6 (0.8%) 4 (0.5%) 15 (2.0%)
Fracture Img1 708 (96.3%) 3 (0.4%) 24 (3.3%)
Img2 695 (94.6%) 17 (2.3%) 23 (3.1%)
Continued on next page
40

Pathology Source 0 1 2
Find 48 (6.5%) 6 (0.8%) 41 (5.6%)
Impr 5 (0.7%) 2 (0.3%) 22 (3.0%)
Support Devices Img1 540 (73.5%) 19 (2.6%) 176 (23.9%)
Img2 360 (49.0%) 14 (1.9%) 361 (49.1%)
Find 10 (1.4%) 0 (0.0%) 235 (32.0%)
Impr 5 (0.7%) 0 (0.0%) 132 (18.0%)
Table A.8: MIMIC-CXR label distribution per CheXpert pathology and label source. Label
sources include labels from individual image annotators (Img1 and Img2) and labels from
annotations of findings (Find) and impression (Impr) radiology reports sections. Values are
shown as count (percentage).
41

Appendix B. Agreement Tables
Pathologyκ w κlow κhigh F1 F1 low F1high
Atelectasis 0.15 0.06 0.23 0.62 0.62 0.72
Consolidation 0.47 0.41 0.51 0.86 0.87 0.89
Lung Opacity 0.42 0.22 0.55 0.68 0.69 0.82
Pleural Effusion 0.67 0.46 0.77 0.80 0.81 0.93
Macro avg. (four selected) 0.43 0.29 0.52 0.74 0.75 0.84
Macro avg. (all 12) 0.33 0.21 0.44 0.87 0.87 0.93
Micro avg. (all 12) 0.45 0.29 0.55 0.87 0.87 0.93
Table B.9: XQA-RR inter-annotator agreement for image labels in the four selected categories,
including macro-average scores for the four selected categories and macro/micro-averaged
results for all 12 pathologies.κw denotes quadratically weighted Cohen’sκcomputed on the
original three-class labels (negative, uncertain, positive).κlow andκ high denote unweighted
Cohen’sκunder pessimistic and optimistic uncertainty mappings, respectively. F1low and
F1high are computed under the same mappings.
Pathologyκ w κlow κhigh F1 F1 low F1high
Atelectasis 0.80 0.78 0.81 0.96 0.96 0.96
Consolidation 0.94 0.89 0.96 0.97 0.96 0.98
Lung Opacity 0.84 0.83 0.85 0.93 0.93 0.94
Pleural Effusion 0.89 0.87 0.90 0.97 0.97 0.98
Macro avg. (four selected) 0.87 0.84 0.88 0.96 0.96 0.97
Macro avg. (all 12) 0.82 0.76 0.84 0.98 0.98 0.98
Micro avg. (all 12) 0.88 0.85 0.90 0.98 0.98 0.99
Table B.10: XQA-RR inter-annotator agreement for report labels in the four selected cat-
egories, including macro-average scores for the four selected categories and macro/micro-
averaged results for all 12 pathologies.κ w denotes quadratically weighted Cohen’sκcom-
puted on the original three-class labels (negative, uncertain, positive).κlow andκ high denote
unweighted Cohen’sκunder pessimistic and optimistic uncertainty mappings, respectively.
F1low and F1high are computed under the same mappings.
42

Pathologyκ w κlow κhigh F1 F1 low F1high
CR vs. Rep1
Atelectasis 0.23 0.16 0.28 0.79 0.78 0.82
Consolidation 0.22 0.16 0.27 0.70 0.69 0.74
Lung Opacity 0.43 0.33 0.50 0.73 0.71 0.78
Pleural Effusion 0.56 0.46 0.61 0.86 0.85 0.89
Macro avg. (four selected) 0.36 0.28 0.41 0.77 0.76 0.81
Macro avg. (all 12) 0.34 0.24 0.46 0.90 0.89 0.92
Micro avg. (all 12) 0.43 0.33 0.49 0.90 0.89 0.92
CR vs. Rep2
Atelectasis 0.25 0.17 0.31 0.78 0.77 0.82
Consolidation 0.24 0.19 0.28 0.72 0.71 0.75
Lung Opacity 0.40 0.30 0.47 0.74 0.72 0.79
Pleural Effusion 0.54 0.45 0.60 0.85 0.84 0.89
Macro avg. (four selected) 0.36 0.28 0.41 0.77 0.76 0.81
Macro avg. (all 12) 0.32 0.22 0.44 0.89 0.89 0.92
Micro avg. (all 12) 0.42 0.32 0.48 0.90 0.89 0.92
Table B.11: XQA-RR agreement between conflict-resolved (CR) image labels and the labels
from the two individual report annotators (Rep1 and Rep2) in the four selected categories,
including macro-average scores for the four selected categories and macro/micro-averaged
results for all 12 pathologies.κw denotes quadratically weighted Cohen’sκcomputed on the
original three-class labels (negative, uncertain, positive).κlow andκ high denote unweighted
Cohen’sκunder pessimistic and optimistic uncertainty mappings, respectively. F1low and
F1high are computed under the same mappings.
Pathologyκ w κlow κhigh F1 F1 low F1high
Atelectasis 0.27 0.00 0.49 0.66 0.67 0.85
Consolidation 0.38 0.04 0.64 0.67 0.70 0.89
Lung Opacity 0.11 -0.06 0.31 0.49 0.47 0.79
Pleural Effusion 0.62 0.37 0.75 0.73 0.72 0.90
Macro avg. (four selected) 0.34 0.09 0.55 0.64 0.64 0.86
Macro avg. (all 12) 0.38 0.16 0.64 0.82 0.83 0.94
Micro avg. (all 12) 0.44 0.16 0.65 0.82 0.83 0.95
Table B.12: MIMIC-CXR inter-annotator agreement for image labels in the four selected
categories, including macro-average scores for the four selected categories and macro/micro-
averaged results for all 12 pathologies.κ w denotes quadratically weighted Cohen’sκcom-
puted on the original three-class labels (negative, uncertain, positive).κlow andκ high denote
unweighted Cohen’sκunder pessimistic and optimistic uncertainty mappings, respectively.
F1low and F1high are computed under the same mappings.
43

Pathologyκ w κlow κhigh F1 F1 low F1high
Atelectasis 0.20 0.11 0.27 0.72 0.72 0.79
Consolidation 0.45 0.34 0.51 0.91 0.91 0.94
Lung Opacity 0.38 0.38 0.38 0.79 0.79 0.79
Pleural Effusion 0.33 0.26 0.38 0.72 0.72 0.78
Macro avg. (four selected) 0.34 0.27 0.39 0.78 0.78 0.83
Macro avg. (all 12) 0.33 0.25 0.40 0.84 0.84 0.89
Micro avg. (all 12) 0.36 0.27 0.42 0.84 0.84 0.89
Table B.13: MIMIC-CXR agreement between labels from report findings and impressions
sections in the four selected categories, including macro-average scores for the four selected
categories and macro/micro-averaged results for all 12 pathologies.κw denotes quadratically
weighted Cohen’sκcomputed on the original three-class labels (negative, uncertain, positive).
κlow andκ high denote unweighted Cohen’sκunder pessimistic and optimistic uncertainty
mappings, respectively. F1low and F1high are computed under the same mappings.
Pathologyκ w κlow κhigh F1 F1 low F1high
MACE
Atelectasis 0.17 -0.07 0.37 0.57 0.54 0.75
Consolidation 0.07 -0.01 0.16 0.68 0.69 0.82
Lung Opacity 0.19 -0.07 0.42 0.59 0.54 0.76
Pleural Effusion 0.44 0.16 0.63 0.67 0.64 0.85
Macro avg. (four selected) 0.22 0.00 0.39 0.63 0.60 0.79
Macro avg. (all 12) 0.23 0.03 0.43 0.75 0.73 0.88
Micro avg. (all 12) 0.27 0.05 0.46 0.75 0.74 0.88
FUSE_OR
Atelectasis 0.17 -0.05 0.36 0.57 0.55 0.74
Consolidation 0.08 -0.01 0.20 0.65 0.65 0.82
Lung Opacity 0.21 -0.10 0.47 0.58 0.52 0.78
Pleural Effusion 0.45 0.25 0.57 0.69 0.67 0.82
Macro avg. (four selected) 0.23 0.02 0.40 0.62 0.60 0.79
Macro avg. (all 12) 0.23 0.04 0.43 0.75 0.73 0.88
Micro avg. (all 12) 0.29 0.06 0.47 0.75 0.74 0.88
NN Fusion
Atelectasis 0.12 -0.12 0.34 0.60 0.57 0.77
Consolidation 0.10 -0.03 0.27 0.66 0.66 0.87
Lung Opacity 0.20 -0.12 0.47 0.59 0.53 0.79
Pleural Effusion 0.44 0.24 0.57 0.70 0.68 0.83
Macro avg. (four selected) 0.21 -0.01 0.41 0.64 0.61 0.81
Macro avg. (all 12) 0.18 0.03 0.31 0.75 0.74 0.87
Continued on next page
44

Pathologyκ w κlow κhigh F1 F1 low F1high
Micro avg. (all 12) 0.23 0.03 0.41 0.76 0.74 0.87
NN Fusion (PS)
Atelectasis 0.14 -0.09 0.35 0.61 0.58 0.77
Consolidation 0.09 -0.03 0.25 0.66 0.66 0.87
Lung Opacity 0.21 -0.09 0.47 0.59 0.53 0.79
Pleural Effusion 0.44 0.22 0.57 0.69 0.66 0.83
Macro avg. (four selected) 0.22 0.00 0.41 0.64 0.61 0.81
Macro avg. (all 12) 0.17 0.02 0.33 0.74 0.73 0.87
Micro avg. (all 12) 0.23 0.03 0.42 0.75 0.74 0.87
Table B.14: MIMIC-CXR agreement between image-only aggregation algorithm labels and
report findings labels in the four selected categories, including macro-average scores for the
four selected categories and macro/micro-averaged results for all 12 pathologies.κw denotes
quadratically weighted Cohen’sκcomputed on the original three-class labels (negative, uncer-
tain, positive).κ low andκ high denote unweighted Cohen’sκunder pessimistic and optimistic
uncertainty mappings, respectively. F1low and F1high are computed under the same map-
pings.
Pathologyκ w κlow κhigh F1 F1 low F1high
MACE
Atelectasis 0.14 -0.04 0.31 0.59 0.59 0.78
Consolidation 0.06 -0.02 0.14 0.68 0.68 0.81
Lung Opacity 0.14 -0.08 0.35 0.62 0.58 0.78
Pleural Effusion 0.36 0.12 0.54 0.66 0.63 0.82
Macro avg. (four selected) 0.17 -0.00 0.34 0.64 0.62 0.80
Macro avg. (all 12) 0.20 0.02 0.38 0.78 0.77 0.89
Micro avg. (all 12) 0.24 0.05 0.42 0.79 0.78 0.89
FUSE_OR
Atelectasis 0.13 -0.04 0.31 0.59 0.58 0.78
Consolidation 0.06 -0.02 0.17 0.65 0.65 0.81
Lung Opacity 0.13 -0.10 0.37 0.59 0.55 0.79
Pleural Effusion 0.35 0.18 0.47 0.66 0.64 0.79
Macro avg. (four selected) 0.17 0.00 0.33 0.62 0.60 0.79
Macro avg. (all 12) 0.20 0.02 0.38 0.78 0.77 0.89
Micro avg. (all 12) 0.25 0.05 0.42 0.79 0.77 0.89
NN Fusion
Atelectasis 0.10 -0.12 0.36 0.68 0.66 0.86
Consolidation 0.08 -0.04 0.24 0.66 0.65 0.86
Continued on next page
45

Pathologyκ w κlow κhigh F1 F1 low F1high
Lung Opacity 0.13 -0.13 0.41 0.62 0.58 0.81
Pleural Effusion 0.35 0.18 0.46 0.68 0.67 0.80
Macro avg. (four selected) 0.17 -0.03 0.37 0.66 0.64 0.83
Macro avg. (all 12) 0.15 0.00 0.29 0.79 0.78 0.89
Micro avg. (all 12) 0.22 0.03 0.39 0.80 0.79 0.90
NN Fusion (PS)
Atelectasis 0.12 -0.10 0.37 0.68 0.67 0.85
Consolidation 0.07 -0.04 0.23 0.65 0.65 0.85
Lung Opacity 0.13 -0.11 0.39 0.62 0.57 0.80
Pleural Effusion 0.35 0.16 0.48 0.67 0.65 0.80
Macro avg. (four selected) 0.17 -0.02 0.37 0.66 0.64 0.83
Macro avg. (all 12) 0.15 -0.00 0.32 0.79 0.78 0.90
Micro avg. (all 12) 0.23 0.03 0.41 0.80 0.79 0.90
Table B.15: MIMIC-CXR agreement between image-only aggregation algorithm labels and
report impressions labels in the four selected categories, including macro-average scores for
the four selected categories and macro/micro-averaged results for all 12 pathologies.κw de-
notes quadratically weighted Cohen’sκcomputed on the original three-class labels (negative,
uncertain, positive).κ low andκ high denote unweighted Cohen’sκunder pessimistic and op-
timistic uncertainty mappings, respectively. F1low and F1high are computed under the same
mappings.
46

Appendix C. Supplementary Agreement and Rank Correlation Fig-
ures
Atelectasis Consolidation Lung opacityPleural effusionMacro average
0.0
0.2
0.4
0.6
0.8
1.0Weighted F1 score
MV
DS
FUSE-OR
FUSE-AND
MACE
NN
NN-PS
Figure C.15: Agreement between each image-derived label fusion method and the XQA-RR
conflict-resolved (CR) image-derived labels, measured by weighted F1. Intervals indicate the
range induced by the pessimistic and optimistic uncertainty mappings. Macro-average scores
are calculated across the four selected pathologies.
Atelectasis Consolidation Lung opacityPleural effusionMacro average
0.0
0.2
0.4
0.6
0.8
1.0Weighted F1 score
Image inter-annotator
Report inter-annotator
Image-report (CR vs Rep1)
Image-report (CR vs Rep2)
FigureC.16: XQA-RRinter-annotatorandcross-sourcelabelagreementmeasuredbyweighted
F1. Intervals indicate the range induced by the pessimistic and optimistic uncertainty map-
pings. Macro-average scores are calculated across the four selected pathologies.
47

Atelectasis Consolidation Lung opacityPleural effusionMacro average
0.0
0.2
0.4
0.6
0.8
1.0Weighted F1 score
Image inter-annotator
Report Impr. vs Find.
Image-report (FUSE-OR vs Find.)
Image-report (FUSE-OR vs Impr.)
Figure C.17: MIMIC-CXR inter-annotator and cross-source agreement measured by weighted
F1. Intervals indicate the range induced by the pessimistic and optimistic uncertainty map-
pings. Macro-average scores are calculated across the four selected pathologies.
Atelectasis Consolidation Lung opacity Pleural effusion Macro average
1.0
0.5
0.0
0.5
1.0
KRCC
All Models
VLM-0-SHOT
VLM-FT
XRV
CR vs Rep1
CR vs Rep2
Figure C.18: XQA-RR rank correlation coefficients between model rankings induced by each
pair of label sources, measured by Kendall rank correlation coefficient (KRCC). CR denotes
conflict-resolved image-derived labels; Rep1/Rep2 denote report-derived labels from the two
report annotators. Results are broken down by pathology and model group. Macro average
refers to rankings induced by ROC-AUC macro-averaged across the four selected pathologies.
48

Atelectasis Consolidation Lung opacity Pleural effusion Macro average
1.0
0.5
0.0
0.5
1.0
KRCC
All Models
VLM-0-SHOT
VLM-FT
XRV
Fuse-OR vs Find.
Fuse-OR vs Impr.
Figure C.19: MIMIC-CXR rank correlation coefficients between model rankings induced
by each pair of label sources, measured by Kendall rank correlation coefficient (KRCC).
FUSE_OR denotes automatically fused image-derived labels; Find. and Impr. denote la-
bels derived from the Findings and Impressions sections of the radiology report. Results are
broken down by pathology and model group. Macro average refers to rankings induced by
ROC-AUC macro-averaged across the four selected pathologies.
49

Appendix D. ROC-AUC Tables
Model CR Rep1 Rep2
D-POOL 0.70 (0.66, 0.73) 0.67 (0.61, 0.73) 0.71 (0.66, 0.76)
D-CheX 0.65 (0.61, 0.69) 0.60 (0.54, 0.66) 0.61 (0.56, 0.67)
D-MC_ch 0.57 (0.53, 0.61) 0.57 (0.51, 0.63) 0.59 (0.53, 0.64)
D-MC_nb 0.58 (0.54, 0.62) 0.59 (0.53, 0.66) 0.61 (0.55, 0.67)
D-NIH 0.62 (0.58, 0.66) 0.64 (0.59, 0.70) 0.67 (0.61, 0.72)
D-PC 0.64 (0.60, 0.68) 0.68 (0.63, 0.74) 0.71 (0.66, 0.76)
D-RSNA 0.50 (0.50, 0.50) 0.50 (0.50, 0.50) 0.50 (0.50, 0.50)
R-POOL 0.67 (0.63, 0.71) 0.71 (0.65, 0.76) 0.75 (0.70, 0.80)
JFH 0.73 (0.69, 0.76) 0.68 (0.62, 0.74) 0.73 (0.67, 0.78)
D-POOL-CUH 0.72 (0.69, 0.76) 0.70 (0.65, 0.75) 0.74 (0.69, 0.79)
D-CheX-CUH 0.68 (0.64, 0.72) 0.60 (0.54, 0.66) 0.65 (0.59, 0.70)
D-MC_ch-CUH 0.69 (0.65, 0.72) 0.63 (0.57, 0.70) 0.65 (0.59, 0.71)
D-MC_nb-CUH 0.68 (0.64, 0.72) 0.64 (0.58, 0.70) 0.67 (0.61, 0.73)
D-NIH-CUH 0.70 (0.66, 0.74) 0.66 (0.60, 0.73) 0.70 (0.65, 0.76)
D-PC-CUH 0.69 (0.65, 0.73) 0.67 (0.61, 0.73) 0.70 (0.64, 0.75)
D-RSNA-CUH 0.64 (0.60, 0.68) 0.59 (0.52, 0.65) 0.65 (0.59, 0.71)
D-NORMAL 0.67 (0.63, 0.71) 0.66 (0.60, 0.72) 0.66 (0.61, 0.72)
CONVIRT-CUH 0.73 (0.70, 0.77) 0.74 (0.68, 0.79) 0.77 (0.72, 0.82)
GLORIA-G-CUH 0.73 (0.69, 0.77) 0.77 (0.71, 0.82) 0.81 (0.76, 0.85)
R-MedCLIP-CUH 0.74 (0.70, 0.77) 0.74 (0.68, 0.79) 0.76 (0.71, 0.81)
V-MedCLIP-CUH 0.75 (0.71, 0.78) 0.71 (0.66, 0.77) 0.76 (0.71, 0.80)
MedKLIP-CUH 0.73 (0.70, 0.76) 0.72 (0.66, 0.77) 0.76 (0.71, 0.81)
MFLAG-CUH 0.61 (0.57, 0.65) 0.56 (0.50, 0.62) 0.63 (0.58, 0.69)
R-MGCA-CUH 0.75 (0.71, 0.78) 0.72 (0.67, 0.78) 0.76 (0.70, 0.81)
MRM-CUH 0.77 (0.73, 0.80) 0.74 (0.69, 0.79) 0.77 (0.72, 0.81)
V-MGCA-CUH 0.73 (0.69, 0.77) 0.76 (0.71, 0.81) 0.79 (0.74, 0.83)
REFERS-CUH 0.75 (0.72, 0.79) 0.75 (0.69, 0.80) 0.78 (0.73, 0.82)
CONVIRT 0.41 (0.36, 0.45) 0.50 (0.44, 0.57) 0.49 (0.42, 0.55)
GLORIA-G 0.61 (0.57, 0.66) 0.66 (0.60, 0.71) 0.67 (0.62, 0.72)
GLORIA-B 0.63 (0.59, 0.67) 0.68 (0.62, 0.74) 0.66 (0.60, 0.71)
R-MGCA 0.45 (0.41, 0.50) 0.45 (0.39, 0.52) 0.49 (0.43, 0.54)
V-MGCA 0.48 (0.44, 0.53) 0.48 (0.42, 0.54) 0.51 (0.44, 0.58)
PTUNIFIER 0.61 (0.56, 0.65) 0.67 (0.61, 0.73) 0.64 (0.59, 0.69)
REFERS 0.61 (0.57, 0.65) 0.66 (0.60, 0.72) 0.63 (0.57, 0.68)
Mean 0.65 (0.62, 0.69) 0.65 (0.59, 0.71) 0.68 (0.62, 0.73)
Table D.16: XQA-RR ROC-AUC for Atelectasis when evaluated against conflict-resolved
(CR) image labels and labels from the two report annotators (Rep1 and Rep2). The mean
scores represent the average ROC-AUC performance across all tested models.
50

Model CR Rep1 Rep2
D-POOL 0.88 (0.85, 0.90) 0.75 (0.72, 0.79) 0.76 (0.72, 0.79)
D-CheX 0.78 (0.75, 0.82) 0.71 (0.67, 0.74) 0.70 (0.67, 0.74)
D-MC_ch 0.66 (0.61, 0.71) 0.68 (0.64, 0.72) 0.66 (0.62, 0.71)
D-MC_nb 0.81 (0.78, 0.85) 0.70 (0.66, 0.73) 0.69 (0.65, 0.72)
D-NIH 0.76 (0.72, 0.80) 0.68 (0.64, 0.72) 0.67 (0.63, 0.71)
D-PC 0.82 (0.79, 0.85) 0.71 (0.68, 0.75) 0.71 (0.68, 0.75)
D-RSNA 0.50 (0.50, 0.50) 0.50 (0.50, 0.50) 0.50 (0.50, 0.50)
R-POOL 0.81 (0.78, 0.85) 0.68 (0.64, 0.72) 0.69 (0.65, 0.73)
JFH 0.90 (0.88, 0.92) 0.77 (0.73, 0.80) 0.77 (0.74, 0.81)
D-POOL-CUH 0.85 (0.82, 0.88) 0.78 (0.75, 0.81) 0.79 (0.76, 0.82)
D-CheX-CUH 0.85 (0.82, 0.88) 0.76 (0.73, 0.79) 0.77 (0.74, 0.80)
D-MC_ch-CUH 0.82 (0.79, 0.85) 0.75 (0.72, 0.79) 0.75 (0.72, 0.78)
D-MC_nb-CUH 0.83 (0.80, 0.86) 0.76 (0.72, 0.79) 0.76 (0.72, 0.79)
D-NIH-CUH 0.83 (0.79, 0.86) 0.75 (0.71, 0.79) 0.75 (0.71, 0.79)
D-PC-CUH 0.85 (0.82, 0.87) 0.77 (0.74, 0.80) 0.77 (0.74, 0.81)
D-RSNA-CUH 0.83 (0.80, 0.86) 0.75 (0.71, 0.78) 0.75 (0.71, 0.78)
D-NORMAL 0.80 (0.76, 0.84) 0.74 (0.70, 0.78) 0.74 (0.71, 0.78)
CONVIRT-CUH 0.87 (0.84, 0.89) 0.79 (0.75, 0.82) 0.79 (0.76, 0.82)
GLORIA-G-CUH 0.87 (0.84, 0.89) 0.78 (0.75, 0.82) 0.79 (0.75, 0.82)
R-MedCLIP-CUH 0.89 (0.86, 0.91) 0.80 (0.77, 0.83) 0.81 (0.77, 0.83)
V-MedCLIP-CUH 0.86 (0.83, 0.89) 0.80 (0.77, 0.83) 0.80 (0.77, 0.83)
MedKLIP-CUH 0.84 (0.81, 0.87) 0.78 (0.74, 0.81) 0.78 (0.75, 0.81)
MFLAG-CUH 0.77 (0.73, 0.81) 0.75 (0.72, 0.79) 0.75 (0.71, 0.78)
R-MGCA-CUH 0.85 (0.83, 0.88) 0.78 (0.74, 0.81) 0.78 (0.75, 0.81)
MRM-CUH 0.85 (0.83, 0.88) 0.80 (0.77, 0.83) 0.80 (0.76, 0.83)
V-MGCA-CUH 0.88 (0.85, 0.90) 0.81 (0.77, 0.84) 0.81 (0.78, 0.84)
REFERS-CUH 0.86 (0.83, 0.88) 0.78 (0.74, 0.81) 0.78 (0.74, 0.81)
CONVIRT 0.58 (0.54, 0.63) 0.58 (0.54, 0.62) 0.59 (0.55, 0.63)
GLORIA-G 0.69 (0.65, 0.73) 0.62 (0.58, 0.66) 0.62 (0.58, 0.66)
GLORIA-B 0.69 (0.64, 0.73) 0.62 (0.58, 0.66) 0.61 (0.57, 0.66)
R-MGCA 0.40 (0.35, 0.45) 0.45 (0.40, 0.49) 0.44 (0.40, 0.49)
V-MGCA 0.43 (0.38, 0.47) 0.44 (0.40, 0.48) 0.44 (0.40, 0.48)
PTUNIFIER 0.71 (0.66, 0.75) 0.64 (0.60, 0.67) 0.64 (0.60, 0.68)
REFERS 0.69 (0.64, 0.74) 0.61 (0.56, 0.65) 0.61 (0.57, 0.65)
Mean 0.77 (0.74, 0.81) 0.71 (0.67, 0.74) 0.71 (0.67, 0.74)
Table D.17: XQA-RR ROC-AUC for Consolidation when evaluated against conflict-resolved
(CR) image labels and labels from the two report annotators (Rep1 and Rep2). The mean
scores represent the average ROC-AUC performance across all tested models.
51

Model CR Rep1 Rep2
D-POOL 0.85 (0.82, 0.87) 0.75 (0.71, 0.78) 0.75 (0.72, 0.79)
D-CheX 0.71 (0.68, 0.75) 0.61 (0.57, 0.65) 0.60 (0.56, 0.64)
D-MC_ch 0.71 (0.67, 0.74) 0.62 (0.58, 0.65) 0.63 (0.59, 0.66)
D-MC_nb 0.81 (0.78, 0.84) 0.67 (0.64, 0.71) 0.69 (0.66, 0.73)
D-NIH 0.50 (0.50, 0.50) 0.50 (0.50, 0.50) 0.50 (0.50, 0.50)
D-PC 0.50 (0.50, 0.50) 0.50 (0.50, 0.50) 0.50 (0.50, 0.50)
D-RSNA 0.82 (0.79, 0.85) 0.75 (0.72, 0.78) 0.75 (0.72, 0.79)
R-POOL 0.67 (0.63, 0.71) 0.61 (0.57, 0.65) 0.60 (0.56, 0.65)
JFH 0.50 (0.50, 0.50) 0.50 (0.50, 0.50) 0.50 (0.50, 0.50)
D-POOL-CUH 0.86 (0.83, 0.88) 0.80 (0.77, 0.83) 0.82 (0.79, 0.85)
D-CheX-CUH 0.82 (0.79, 0.85) 0.77 (0.73, 0.80) 0.78 (0.75, 0.81)
D-MC_ch-CUH 0.84 (0.81, 0.87) 0.76 (0.73, 0.79) 0.78 (0.75, 0.81)
D-MC_nb-CUH 0.84 (0.81, 0.87) 0.77 (0.74, 0.81) 0.79 (0.75, 0.82)
D-NIH-CUH 0.83 (0.80, 0.86) 0.77 (0.74, 0.80) 0.79 (0.76, 0.82)
D-PC-CUH 0.85 (0.83, 0.88) 0.79 (0.76, 0.82) 0.80 (0.77, 0.84)
D-RSNA-CUH 0.86 (0.84, 0.89) 0.78 (0.75, 0.81) 0.79 (0.76, 0.82)
D-NORMAL 0.81 (0.78, 0.84) 0.75 (0.72, 0.78) 0.76 (0.72, 0.79)
CONVIRT-CUH 0.85 (0.82, 0.87) 0.82 (0.79, 0.84) 0.83 (0.80, 0.86)
GLORIA-G-CUH 0.86 (0.84, 0.89) 0.82 (0.79, 0.85) 0.82 (0.80, 0.85)
R-MedCLIP-CUH 0.86 (0.83, 0.88) 0.83 (0.80, 0.86) 0.83 (0.80, 0.86)
V-MedCLIP-CUH 0.86 (0.84, 0.89) 0.83 (0.80, 0.86) 0.83 (0.81, 0.86)
MedKLIP-CUH 0.84 (0.81, 0.87) 0.80 (0.77, 0.83) 0.80 (0.77, 0.83)
MFLAG-CUH 0.79 (0.76, 0.82) 0.71 (0.68, 0.75) 0.71 (0.67, 0.75)
R-MGCA-CUH 0.80 (0.77, 0.83) 0.80 (0.77, 0.83) 0.79 (0.76, 0.82)
MRM-CUH 0.87 (0.85, 0.90) 0.83 (0.80, 0.86) 0.85 (0.82, 0.87)
V-MGCA-CUH 0.84 (0.81, 0.87) 0.82 (0.79, 0.84) 0.82 (0.79, 0.84)
REFERS-CUH 0.85 (0.83, 0.88) 0.82 (0.79, 0.85) 0.83 (0.80, 0.86)
CONVIRT 0.82 (0.79, 0.85) 0.77 (0.74, 0.80) 0.79 (0.76, 0.82)
GLORIA-G 0.84 (0.82, 0.87) 0.81 (0.78, 0.84) 0.82 (0.79, 0.85)
GLORIA-B 0.83 (0.80, 0.86) 0.82 (0.79, 0.84) 0.83 (0.80, 0.86)
R-MGCA 0.49 (0.45, 0.53) 0.53 (0.49, 0.57) 0.54 (0.50, 0.58)
V-MGCA 0.47 (0.43, 0.51) 0.47 (0.43, 0.51) 0.48 (0.44, 0.53)
PTUNIFIER 0.82 (0.80, 0.85) 0.82 (0.79, 0.85) 0.83 (0.80, 0.86)
REFERS 0.79 (0.76, 0.82) 0.78 (0.75, 0.81) 0.78 (0.74, 0.81)
Mean 0.77 (0.75, 0.80) 0.73 (0.70, 0.76) 0.74 (0.71, 0.77)
Table D.18: XQA-RR ROC-AUC for Lung opacity when evaluated against conflict-resolved
(CR) image labels and labels from the two report annotators (Rep1 and Rep2). The mean
scores represent the average ROC-AUC performance across all tested models.
52

Model CR Rep1 Rep2
D-POOL 0.86 (0.82, 0.89) 0.83 (0.79, 0.87) 0.82 (0.78, 0.86)
D-CheX 0.75 (0.71, 0.78) 0.74 (0.69, 0.78) 0.73 (0.69, 0.77)
D-MC_ch 0.70 (0.66, 0.74) 0.73 (0.68, 0.77) 0.70 (0.66, 0.75)
D-MC_nb 0.70 (0.66, 0.74) 0.69 (0.64, 0.74) 0.67 (0.62, 0.72)
D-NIH 0.80 (0.76, 0.83) 0.77 (0.73, 0.81) 0.74 (0.70, 0.78)
D-PC 0.86 (0.83, 0.88) 0.82 (0.78, 0.86) 0.82 (0.78, 0.86)
D-RSNA 0.50 (0.50, 0.50) 0.50 (0.50, 0.50) 0.50 (0.50, 0.50)
R-POOL 0.88 (0.85, 0.91) 0.83 (0.79, 0.87) 0.82 (0.78, 0.86)
JFH 0.91 (0.89, 0.93) 0.86 (0.83, 0.89) 0.85 (0.82, 0.89)
D-POOL-CUH 0.89 (0.86, 0.91) 0.86 (0.83, 0.89) 0.85 (0.81, 0.88)
D-CheX-CUH 0.85 (0.82, 0.88) 0.82 (0.78, 0.86) 0.81 (0.76, 0.85)
D-MC_ch-CUH 0.84 (0.80, 0.86) 0.82 (0.78, 0.85) 0.79 (0.75, 0.83)
D-MC_nb-CUH 0.83 (0.80, 0.86) 0.82 (0.78, 0.86) 0.80 (0.76, 0.84)
D-NIH-CUH 0.85 (0.82, 0.88) 0.82 (0.78, 0.86) 0.80 (0.76, 0.84)
D-PC-CUH 0.87 (0.85, 0.90) 0.85 (0.82, 0.89) 0.84 (0.81, 0.88)
D-RSNA-CUH 0.80 (0.77, 0.84) 0.79 (0.74, 0.83) 0.78 (0.73, 0.83)
D-NORMAL 0.81 (0.78, 0.84) 0.79 (0.75, 0.83) 0.78 (0.74, 0.82)
CONVIRT-CUH 0.93 (0.91, 0.94) 0.89 (0.86, 0.92) 0.88 (0.85, 0.91)
GLORIA-G-CUH 0.91 (0.89, 0.94) 0.87 (0.84, 0.91) 0.87 (0.83, 0.90)
R-MedCLIP-CUH 0.91 (0.89, 0.93) 0.88 (0.85, 0.91) 0.87 (0.83, 0.90)
V-MedCLIP-CUH 0.93 (0.91, 0.95) 0.91 (0.88, 0.93) 0.89 (0.86, 0.92)
MedKLIP-CUH 0.89 (0.87, 0.92) 0.87 (0.84, 0.90) 0.86 (0.82, 0.89)
MFLAG-CUH 0.81 (0.77, 0.84) 0.80 (0.76, 0.84) 0.77 (0.73, 0.82)
R-MGCA-CUH 0.88 (0.86, 0.91) 0.86 (0.82, 0.89) 0.85 (0.82, 0.89)
MRM-CUH 0.93 (0.90, 0.94) 0.91 (0.88, 0.93) 0.89 (0.86, 0.92)
V-MGCA-CUH 0.92 (0.90, 0.94) 0.89 (0.86, 0.92) 0.88 (0.85, 0.91)
REFERS-CUH 0.92 (0.89, 0.94) 0.88 (0.85, 0.91) 0.87 (0.83, 0.90)
CONVIRT 0.71 (0.66, 0.75) 0.76 (0.71, 0.81) 0.75 (0.70, 0.80)
GLORIA-G 0.79 (0.76, 0.82) 0.77 (0.73, 0.81) 0.77 (0.72, 0.80)
GLORIA-B 0.72 (0.68, 0.76) 0.71 (0.66, 0.76) 0.70 (0.65, 0.74)
R-MGCA 0.57 (0.52, 0.61) 0.56 (0.50, 0.61) 0.55 (0.50, 0.60)
V-MGCA 0.58 (0.53, 0.62) 0.58 (0.53, 0.63) 0.57 (0.51, 0.62)
PTUNIFIER 0.83 (0.80, 0.87) 0.83 (0.79, 0.87) 0.82 (0.78, 0.86)
REFERS 0.68 (0.63, 0.73) 0.74 (0.69, 0.79) 0.74 (0.69, 0.79)
Mean 0.81 (0.78, 0.84) 0.80 (0.76, 0.83) 0.78 (0.74, 0.82)
Table D.19: XQA-RR ROC-AUC for Pleural effusion when evaluated against conflict-resolved
(CR) image labels and labels from the two report annotators (Rep1 and Rep2). The mean
scores represent the average ROC-AUC performance across all tested models.
53

Model CR Rep1 Rep2
D-POOL 0.82 (0.79, 0.85) 0.75 (0.71, 0.79) 0.76 (0.72, 0.80)
D-CheX 0.72 (0.69, 0.76) 0.66 (0.62, 0.71) 0.66 (0.62, 0.70)
D-MC_ch 0.66 (0.62, 0.70) 0.65 (0.60, 0.70) 0.65 (0.60, 0.69)
D-MC_nb 0.73 (0.69, 0.76) 0.66 (0.62, 0.71) 0.66 (0.62, 0.71)
D-NIH 0.67 (0.64, 0.70) 0.65 (0.61, 0.68) 0.64 (0.61, 0.68)
D-PC 0.70 (0.68, 0.73) 0.68 (0.64, 0.71) 0.69 (0.65, 0.72)
D-RSNA 0.58 (0.57, 0.59) 0.56 (0.55, 0.57) 0.56 (0.55, 0.57)
R-POOL 0.76 (0.72, 0.79) 0.71 (0.66, 0.75) 0.72 (0.67, 0.76)
JFH 0.76 (0.74, 0.78) 0.70 (0.67, 0.73) 0.71 (0.68, 0.74)
D-POOL-CUH 0.83 (0.80, 0.86) 0.79 (0.75, 0.82) 0.80 (0.76, 0.84)
D-CheX-CUH 0.80 (0.77, 0.83) 0.74 (0.69, 0.78) 0.75 (0.71, 0.79)
D-MC_ch-CUH 0.80 (0.76, 0.83) 0.74 (0.70, 0.78) 0.74 (0.70, 0.78)
D-MC_nb-CUH 0.80 (0.76, 0.83) 0.75 (0.71, 0.79) 0.75 (0.71, 0.79)
D-NIH-CUH 0.80 (0.77, 0.83) 0.75 (0.71, 0.79) 0.76 (0.72, 0.80)
D-PC-CUH 0.82 (0.79, 0.85) 0.77 (0.73, 0.81) 0.78 (0.74, 0.82)
D-RSNA-CUH 0.78 (0.75, 0.82) 0.73 (0.68, 0.77) 0.74 (0.70, 0.79)
D-NORMAL 0.77 (0.74, 0.81) 0.74 (0.69, 0.78) 0.74 (0.69, 0.78)
CONVIRT-CUH 0.84 (0.82, 0.87) 0.81 (0.77, 0.84) 0.82 (0.78, 0.85)
GLORIA-G-CUH 0.84 (0.82, 0.87) 0.81 (0.77, 0.85) 0.82 (0.79, 0.86)
R-MedCLIP-CUH 0.85 (0.82, 0.87) 0.81 (0.78, 0.85) 0.82 (0.78, 0.85)
V-MedCLIP-CUH 0.85 (0.82, 0.88) 0.81 (0.78, 0.85) 0.82 (0.79, 0.86)
MedKLIP-CUH 0.83 (0.80, 0.86) 0.79 (0.75, 0.83) 0.80 (0.76, 0.83)
MFLAG-CUH 0.74 (0.71, 0.78) 0.71 (0.66, 0.75) 0.71 (0.67, 0.76)
R-MGCA-CUH 0.82 (0.79, 0.85) 0.79 (0.75, 0.83) 0.79 (0.76, 0.83)
MRM-CUH 0.86 (0.83, 0.88) 0.82 (0.79, 0.85) 0.83 (0.79, 0.86)
V-MGCA-CUH 0.84 (0.81, 0.87) 0.82 (0.78, 0.85) 0.83 (0.79, 0.86)
REFERS-CUH 0.84 (0.82, 0.87) 0.81 (0.77, 0.84) 0.81 (0.78, 0.85)
CONVIRT 0.63 (0.59, 0.67) 0.65 (0.61, 0.70) 0.65 (0.61, 0.70)
GLORIA-G 0.73 (0.70, 0.77) 0.71 (0.67, 0.75) 0.72 (0.68, 0.76)
GLORIA-B 0.72 (0.68, 0.76) 0.71 (0.66, 0.75) 0.70 (0.66, 0.74)
R-MGCA 0.48 (0.43, 0.52) 0.50 (0.45, 0.55) 0.50 (0.46, 0.55)
V-MGCA 0.49 (0.44, 0.53) 0.49 (0.44, 0.54) 0.50 (0.45, 0.55)
PTUNIFIER 0.74 (0.70, 0.78) 0.74 (0.70, 0.78) 0.73 (0.69, 0.77)
REFERS 0.69 (0.65, 0.73) 0.70 (0.65, 0.74) 0.69 (0.64, 0.73)
Mean 0.75 (0.72, 0.78) 0.72 (0.68, 0.76) 0.72 (0.69, 0.76)
Table D.20: XQA-RR ROC-AUC macro averages across the four selected pathologies (At-
electasis, Consolidation, Lung opacity, and Pleural effusion) when evaluated against conflict-
resolved (CR) image labels and labels from the two report annotators (Rep1 and Rep2). The
mean scores represent the average ROC-AUC performance across all tested models.
54

Model FUSE-OR Impression Findings
D-POOL 0.67 (0.64, 0.70) 0.64 (0.59, 0.69) 0.61 (0.58, 0.65)
D-CheX 0.63 (0.60, 0.67) 0.62 (0.57, 0.67) 0.58 (0.54, 0.61)
D-MC_ch 0.63 (0.60, 0.67) 0.62 (0.57, 0.67) 0.60 (0.57, 0.64)
D-MC_nb 0.61 (0.58, 0.65) 0.60 (0.55, 0.65) 0.59 (0.55, 0.62)
D-NIH 0.69 (0.66, 0.72) 0.59 (0.54, 0.65) 0.62 (0.58, 0.65)
D-PC 0.64 (0.61, 0.67) 0.62 (0.57, 0.67) 0.65 (0.61, 0.69)
D-RSNA 0.50 (0.50, 0.50) 0.50 (0.50, 0.50) 0.50 (0.50, 0.50)
R-POOL 0.64 (0.61, 0.67) 0.62 (0.57, 0.67) 0.65 (0.62, 0.69)
JFH 0.69 (0.66, 0.72) 0.65 (0.60, 0.70) 0.66 (0.62, 0.70)
CONVIRT-MIMIC 0.71 (0.68, 0.75) 0.64 (0.60, 0.69) 0.62 (0.58, 0.66)
GLORIA-G-MIMIC 0.73 (0.70, 0.77) 0.65 (0.60, 0.69) 0.64 (0.61, 0.68)
R-MedCLIP-MIMIC 0.72 (0.68, 0.75) 0.63 (0.58, 0.68) 0.63 (0.59, 0.67)
V-MedCLIP-MIMIC 0.74 (0.71, 0.78) 0.65 (0.60, 0.70) 0.65 (0.61, 0.69)
MedKLIP-MIMIC 0.72 (0.69, 0.76) 0.63 (0.58, 0.69) 0.63 (0.59, 0.67)
MFLAG-MIMIC 0.72 (0.68, 0.75) 0.65 (0.60, 0.69) 0.65 (0.61, 0.69)
R-MGCA-MIMIC 0.72 (0.69, 0.75) 0.64 (0.59, 0.69) 0.64 (0.60, 0.68)
MRM-MIMIC 0.74 (0.70, 0.77) 0.64 (0.59, 0.69) 0.66 (0.62, 0.70)
V-MGCA-MIMIC 0.73 (0.69, 0.76) 0.64 (0.59, 0.69) 0.66 (0.62, 0.69)
REFERS-MIMIC 0.72 (0.69, 0.76) 0.65 (0.60, 0.70) 0.65 (0.61, 0.69)
CONVIRT 0.41 (0.37, 0.45) 0.49 (0.44, 0.55) 0.50 (0.46, 0.54)
GLORIA-G 0.55 (0.52, 0.59) 0.52 (0.48, 0.57) 0.61 (0.57, 0.65)
GLORIA-B 0.55 (0.51, 0.59) 0.56 (0.51, 0.61) 0.60 (0.55, 0.64)
R-MGCA 0.47 (0.43, 0.51) 0.51 (0.46, 0.57) 0.50 (0.45, 0.54)
V-MGCA 0.52 (0.48, 0.56) 0.53 (0.48, 0.58) 0.49 (0.45, 0.53)
PTUNIFIER 0.43 (0.39, 0.47) 0.52 (0.47, 0.57) 0.56 (0.52, 0.60)
REFERS 0.41 (0.37, 0.46) 0.43 (0.37, 0.48) 0.53 (0.48, 0.57)
Mean 0.63 (0.59, 0.66) 0.59 (0.55, 0.64) 0.60 (0.56, 0.64)
Table D.21: MIMIC-CXR ROC-AUC results for Atelectasis when evaluated against FUSE-
OR image labels and labels from the findings and impressions report sections. The mean
scores represent the average ROC-AUC performance across all tested models.
55

Model FUSE-OR Impression Findings
D-POOL 0.74 (0.71, 0.77) 0.66 (0.59, 0.72) 0.59 (0.52, 0.66)
D-CheX 0.68 (0.65, 0.72) 0.55 (0.49, 0.62) 0.50 (0.43, 0.57)
D-MC_ch 0.71 (0.68, 0.74) 0.66 (0.59, 0.72) 0.62 (0.54, 0.70)
D-MC_nb 0.72 (0.69, 0.75) 0.65 (0.59, 0.70) 0.63 (0.56, 0.70)
D-NIH 0.68 (0.65, 0.71) 0.57 (0.49, 0.64) 0.52 (0.43, 0.59)
D-PC 0.72 (0.69, 0.75) 0.68 (0.61, 0.74) 0.67 (0.60, 0.74)
D-RSNA 0.50 (0.50, 0.50) 0.50 (0.50, 0.50) 0.50 (0.50, 0.50)
R-POOL 0.66 (0.63, 0.69) 0.69 (0.62, 0.75) 0.59 (0.51, 0.66)
JFH 0.78 (0.75, 0.81) 0.66 (0.59, 0.72) 0.64 (0.57, 0.72)
CONVIRT-MIMIC 0.79 (0.76, 0.82) 0.72 (0.66, 0.78) 0.71 (0.64, 0.78)
GLORIA-G-MIMIC 0.81 (0.78, 0.84) 0.71 (0.65, 0.77) 0.70 (0.62, 0.77)
R-MedCLIP-MIMIC 0.81 (0.78, 0.84) 0.74 (0.67, 0.80) 0.72 (0.64, 0.79)
V-MedCLIP-MIMIC 0.80 (0.77, 0.83) 0.75 (0.69, 0.81) 0.74 (0.66, 0.81)
MedKLIP-MIMIC 0.82 (0.79, 0.85) 0.71 (0.65, 0.77) 0.70 (0.63, 0.77)
MFLAG-MIMIC 0.80 (0.77, 0.83) 0.73 (0.66, 0.79) 0.70 (0.62, 0.77)
R-MGCA-MIMIC 0.82 (0.79, 0.84) 0.75 (0.69, 0.81) 0.71 (0.63, 0.78)
MRM-MIMIC 0.81 (0.78, 0.84) 0.74 (0.68, 0.80) 0.74 (0.67, 0.81)
V-MGCA-MIMIC 0.80 (0.77, 0.83) 0.73 (0.66, 0.79) 0.69 (0.61, 0.76)
REFERS-MIMIC 0.81 (0.78, 0.83) 0.76 (0.70, 0.82) 0.73 (0.66, 0.80)
CONVIRT 0.58 (0.54, 0.62) 0.56 (0.49, 0.63) 0.61 (0.53, 0.70)
GLORIA-G 0.62 (0.58, 0.66) 0.65 (0.57, 0.71) 0.61 (0.53, 0.67)
GLORIA-B 0.60 (0.56, 0.64) 0.66 (0.59, 0.73) 0.58 (0.50, 0.66)
R-MGCA 0.44 (0.40, 0.49) 0.45 (0.38, 0.53) 0.47 (0.39, 0.55)
V-MGCA 0.45 (0.41, 0.49) 0.41 (0.35, 0.48) 0.36 (0.29, 0.44)
PTUNIFIER 0.73 (0.70, 0.77) 0.69 (0.62, 0.75) 0.65 (0.58, 0.72)
REFERS 0.58 (0.54, 0.63) 0.65 (0.57, 0.72) 0.66 (0.59, 0.74)
Mean 0.70 (0.67, 0.73) 0.66 (0.59, 0.72) 0.63 (0.56, 0.70)
Table D.22: MIMIC-CXR ROC-AUC results for Consolidation when evaluated against FUSE-
OR image labels and labels from the findings and impressions report sections. The mean scores
represent the average ROC-AUC performance across all tested models.
56

Model FUSE-OR Impression Findings
D-POOL 0.74 (0.71, 0.77) 0.62 (0.57, 0.66) 0.56 (0.52, 0.60)
D-CheX 0.69 (0.65, 0.72) 0.53 (0.49, 0.57) 0.54 (0.50, 0.58)
D-MC_ch 0.70 (0.67, 0.73) 0.57 (0.53, 0.62) 0.56 (0.52, 0.60)
D-MC_nb 0.72 (0.69, 0.75) 0.58 (0.54, 0.63) 0.57 (0.52, 0.60)
D-NIH 0.50 (0.50, 0.50) 0.50 (0.50, 0.50) 0.50 (0.50, 0.50)
D-PC 0.50 (0.50, 0.50) 0.50 (0.50, 0.50) 0.50 (0.50, 0.50)
D-RSNA 0.70 (0.67, 0.73) 0.58 (0.54, 0.63) 0.56 (0.52, 0.60)
R-POOL 0.66 (0.63, 0.69) 0.65 (0.61, 0.70) 0.59 (0.56, 0.63)
JFH 0.50 (0.50, 0.50) 0.50 (0.50, 0.50) 0.50 (0.50, 0.50)
CONVIRT-MIMIC 0.79 (0.75, 0.82) 0.64 (0.60, 0.68) 0.63 (0.60, 0.67)
GLORIA-G-MIMIC 0.80 (0.76, 0.83) 0.65 (0.61, 0.70) 0.62 (0.58, 0.66)
R-MedCLIP-MIMIC 0.79 (0.75, 0.82) 0.65 (0.61, 0.69) 0.64 (0.60, 0.67)
V-MedCLIP-MIMIC 0.79 (0.76, 0.82) 0.65 (0.60, 0.69) 0.64 (0.60, 0.67)
MedKLIP-MIMIC 0.79 (0.76, 0.83) 0.64 (0.59, 0.68) 0.62 (0.58, 0.65)
MFLAG-MIMIC 0.78 (0.74, 0.81) 0.64 (0.60, 0.68) 0.61 (0.57, 0.64)
R-MGCA-MIMIC 0.80 (0.77, 0.84) 0.67 (0.63, 0.71) 0.63 (0.59, 0.66)
MRM-MIMIC 0.80 (0.77, 0.83) 0.67 (0.63, 0.72) 0.65 (0.61, 0.69)
V-MGCA-MIMIC 0.77 (0.74, 0.81) 0.63 (0.59, 0.67) 0.62 (0.59, 0.66)
REFERS-MIMIC 0.78 (0.74, 0.81) 0.65 (0.60, 0.69) 0.63 (0.59, 0.66)
CONVIRT 0.73 (0.69, 0.77) 0.65 (0.60, 0.69) 0.63 (0.59, 0.66)
GLORIA-G 0.74 (0.70, 0.78) 0.64 (0.60, 0.69) 0.58 (0.54, 0.61)
GLORIA-B 0.72 (0.68, 0.76) 0.65 (0.61, 0.70) 0.61 (0.57, 0.65)
R-MGCA 0.50 (0.46, 0.55) 0.48 (0.44, 0.52) 0.48 (0.44, 0.52)
V-MGCA 0.44 (0.39, 0.48) 0.50 (0.46, 0.55) 0.45 (0.41, 0.48)
PTUNIFIER 0.72 (0.68, 0.76) 0.62 (0.58, 0.66) 0.61 (0.57, 0.65)
REFERS 0.67 (0.62, 0.71) 0.61 (0.57, 0.65) 0.61 (0.58, 0.65)
Mean 0.70 (0.66, 0.73) 0.60 (0.57, 0.64) 0.58 (0.55, 0.61)
Table D.23: MIMIC-CXR ROC-AUC results for Lung Opacity when evaluated against FUSE-
OR image labels and labels from the findings and impressions report sections. The mean scores
represent the average ROC-AUC performance across all tested models.
57

Model FUSE-OR Impression Findings
D-POOL 0.84 (0.82, 0.87) 0.76 (0.73, 0.80) 0.75 (0.71, 0.78)
D-CheX 0.80 (0.77, 0.82) 0.70 (0.66, 0.74) 0.69 (0.65, 0.72)
D-MC_ch 0.80 (0.77, 0.82) 0.71 (0.67, 0.75) 0.70 (0.66, 0.73)
D-MC_nb 0.80 (0.77, 0.82) 0.71 (0.67, 0.75) 0.70 (0.66, 0.73)
D-NIH 0.78 (0.75, 0.80) 0.70 (0.66, 0.74) 0.69 (0.65, 0.73)
D-PC 0.81 (0.78, 0.83) 0.77 (0.73, 0.80) 0.76 (0.73, 0.80)
D-RSNA 0.50 (0.50, 0.50) 0.50 (0.50, 0.50) 0.50 (0.50, 0.50)
R-POOL 0.83 (0.81, 0.86) 0.75 (0.71, 0.79) 0.76 (0.73, 0.80)
JFH 0.90 (0.88, 0.92) 0.82 (0.79, 0.85) 0.81 (0.78, 0.84)
CONVIRT-MIMIC 0.93 (0.92, 0.95) 0.84 (0.81, 0.86) 0.83 (0.80, 0.85)
GLORIA-G-MIMIC 0.93 (0.91, 0.95) 0.83 (0.80, 0.86) 0.82 (0.79, 0.85)
R-MedCLIP-MIMIC 0.94 (0.92, 0.95) 0.85 (0.83, 0.88) 0.84 (0.81, 0.86)
V-MedCLIP-MIMIC 0.94 (0.92, 0.95) 0.86 (0.83, 0.88) 0.85 (0.82, 0.87)
MedKLIP-MIMIC 0.93 (0.92, 0.95) 0.83 (0.80, 0.86) 0.82 (0.79, 0.85)
MFLAG-MIMIC 0.93 (0.91, 0.95) 0.83 (0.80, 0.86) 0.83 (0.80, 0.86)
R-MGCA-MIMIC 0.93 (0.91, 0.94) 0.83 (0.80, 0.86) 0.83 (0.80, 0.86)
MRM-MIMIC 0.93 (0.92, 0.95) 0.84 (0.82, 0.87) 0.83 (0.80, 0.86)
V-MGCA-MIMIC 0.93 (0.91, 0.95) 0.83 (0.81, 0.86) 0.83 (0.80, 0.86)
REFERS-MIMIC 0.92 (0.90, 0.94) 0.84 (0.81, 0.86) 0.82 (0.79, 0.85)
CONVIRT 0.71 (0.68, 0.75) 0.68 (0.63, 0.72) 0.71 (0.68, 0.75)
GLORIA-G 0.78 (0.75, 0.81) 0.72 (0.69, 0.76) 0.71 (0.68, 0.75)
GLORIA-B 0.65 (0.61, 0.68) 0.64 (0.60, 0.68) 0.64 (0.61, 0.68)
R-MGCA 0.51 (0.48, 0.55) 0.52 (0.48, 0.57) 0.49 (0.45, 0.53)
V-MGCA 0.60 (0.56, 0.64) 0.55 (0.51, 0.59) 0.54 (0.50, 0.58)
PTUNIFIER 0.80 (0.78, 0.83) 0.77 (0.74, 0.80) 0.76 (0.72, 0.79)
REFERS 0.74 (0.70, 0.77) 0.72 (0.67, 0.75) 0.71 (0.67, 0.75)
Macro Avg. 0.81 (0.79, 0.84) 0.75 (0.71, 0.78) 0.74 (0.71, 0.77)
Table D.24: MIMIC-CXR ROC-AUC results for Pleural effusion when evaluated against
FUSE-OR image labels and labels from the findings and impressions report sections. The
mean scores refer to the average ROC-AUC performance of all tested models.
58

Model FUSE-OR Impression Findings
D-POOL 0.75 (0.72, 0.78) 0.67 (0.62, 0.72) 0.63 (0.58, 0.67)
D-CheX 0.70 (0.67, 0.73) 0.60 (0.55, 0.65) 0.58 (0.53, 0.62)
D-MC_ch 0.71 (0.68, 0.74) 0.64 (0.59, 0.69) 0.62 (0.57, 0.67)
D-MC_nb 0.71 (0.68, 0.74) 0.64 (0.59, 0.68) 0.62 (0.57, 0.66)
D-NIH 0.66 (0.64, 0.68) 0.59 (0.55, 0.63) 0.58 (0.54, 0.62)
D-PC 0.67 (0.64, 0.69) 0.64 (0.60, 0.68) 0.65 (0.61, 0.68)
D-RSNA 0.55 (0.54, 0.56) 0.52 (0.51, 0.53) 0.52 (0.51, 0.52)
R-POOL 0.70 (0.67, 0.73) 0.68 (0.63, 0.73) 0.65 (0.60, 0.69)
JFH 0.72 (0.70, 0.74) 0.66 (0.62, 0.69) 0.65 (0.62, 0.69)
CONVIRT-MIMIC 0.81 (0.78, 0.83) 0.71 (0.66, 0.75) 0.70 (0.65, 0.74)
GLORIA-G-MIMIC 0.82 (0.79, 0.85) 0.71 (0.66, 0.75) 0.69 (0.65, 0.74)
R-MedCLIP-MIMIC 0.81 (0.78, 0.84) 0.72 (0.67, 0.76) 0.71 (0.66, 0.75)
V-MedCLIP-MIMIC 0.82 (0.79, 0.84) 0.73 (0.68, 0.77) 0.72 (0.67, 0.76)
MedKLIP-MIMIC 0.82 (0.79, 0.84) 0.70 (0.66, 0.75) 0.69 (0.65, 0.74)
MFLAG-MIMIC 0.81 (0.78, 0.84) 0.71 (0.67, 0.76) 0.70 (0.65, 0.74)
R-MGCA-MIMIC 0.82 (0.79, 0.84) 0.72 (0.68, 0.77) 0.70 (0.65, 0.74)
MRM-MIMIC 0.82 (0.79, 0.85) 0.72 (0.68, 0.77) 0.72 (0.68, 0.77)
V-MGCA-MIMIC 0.81 (0.78, 0.84) 0.71 (0.66, 0.75) 0.70 (0.65, 0.74)
REFERS-MIMIC 0.81 (0.78, 0.84) 0.72 (0.68, 0.77) 0.71 (0.66, 0.75)
CONVIRT 0.61 (0.57, 0.65) 0.60 (0.54, 0.65) 0.61 (0.56, 0.67)
GLORIA-G 0.67 (0.64, 0.71) 0.63 (0.58, 0.68) 0.62 (0.58, 0.67)
GLORIA-B 0.63 (0.59, 0.67) 0.63 (0.58, 0.68) 0.61 (0.56, 0.65)
R-MGCA 0.48 (0.44, 0.52) 0.49 (0.44, 0.54) 0.48 (0.43, 0.53)
V-MGCA 0.50 (0.46, 0.54) 0.50 (0.45, 0.55) 0.46 (0.41, 0.51)
PTUNIFIER 0.67 (0.64, 0.71) 0.65 (0.60, 0.70) 0.64 (0.60, 0.69)
REFERS 0.60 (0.56, 0.64) 0.60 (0.55, 0.65) 0.63 (0.58, 0.68)
Mean 0.71 (0.68, 0.74) 0.65 (0.60, 0.69) 0.64 (0.59, 0.68)
Table D.25: MIMIC-CXR ROC-AUC macro averages across the four selected pathologies
(Atelectasis, Consolidation, Lung opacity, andPleural effusion)when evaluatedagainst FUSE-
OR image labels and labels from the findings and impressions report sections. The mean scores
represent the average ROC-AUC performance across all tested models.
59

Appendix E. Rank Correlation Tables
Finding /
summary target Pair All Models VLM-0-SHOT VLM-FT XRV
Atelectasis vs Rep10.80±0.07 0.79±0.11 0.21±0.22 0.62±0.14 vs Rep20.87±0.05 0.80±0.11 0.20±0.22 0.69±0.11
Consolidation vs Rep10.88±0.04 0.82±0.12 0.55±0.18 0.78±0.10 vs Rep20.89±0.03 0.80±0.14 0.63±0.16 0.82±0.09
Lung opacity vs Rep10.80±0.07 0.79±0.12 0.77±0.13 0.90±0.05 vs Rep20.81±0.06 0.82±0.11 0.78±0.11 0.89±0.05
Pleural effusion vs Rep10.96±0.02 0.86±0.09 0.83±0.11 0.93±0.04 vs Rep20.96±0.02 0.87±0.08 0.82±0.11 0.94±0.04
Macro Avg. vs Rep10.96±0.01 0.94±0.05 0.73±0.12 0.95±0.02 vs Rep20.97±0.01 0.96±0.03 0.73±0.12 0.96±0.02
Table E.26: XQA-RR SRCC across pathologies and model groups. Pairs compare conflict-
resolved (CR) image labels across the two report annotators’ labels (Rep1 and Rep2). Macro
average refers to the SRCC of rankings derived from the macro-averaged ROC-AUCs of the
four selected pathologies. SRCC is calculated across model groups that include TorchXRayVi-
sion supervised models (XRV), BenchX VLM 0-shot models (VLM-0-shot), BenchX VLM
fine-tuned models (VLM-FT), and all models combined.
Finding /
summary target Pair All Models VLM-0-SHOT VLM-FT XRV
Atelectasis vs Rep10.62±0.08 0.62±0.16 0.15±0.18 0.49±0.12 vs Rep20.69±0.06 0.65±0.16 0.14±0.19 0.55±0.10
Consolidation vs Rep10.72±0.05 0.70±0.16 0.43±0.16 0.62±0.10 vs Rep20.74±0.04 0.67±0.17 0.49±0.15 0.66±0.09
Lung opacity vs Rep10.64±0.07 0.65±0.14 0.63±0.13 0.77±0.07 vs Rep20.65±0.07 0.69±0.14 0.64±0.13 0.77±0.07
Pleural effusion vs Rep10.85±0.03 0.76±0.12 0.70±0.13 0.81±0.06 vs Rep20.85±0.04 0.76±0.12 0.69±0.13 0.83±0.06
Macro Avg. vs Rep10.85±0.03 0.87±0.10 0.60±0.13 0.85±0.04 vs Rep20.88±0.02 0.90±0.08 0.59±0.13 0.87±0.04
Table E.27: XQA-RR KRCC across pathologies and model groups. Pairs compare conflict-
resolved (CR) image labels across the two report annotators’ labels (Rep1 and Rep2). Macro
averagereferstotheKRCCofrankingsderivedfromthemacro-averagedROC-AUCofthefour
selected pathologies. KRCC is calculated across model groups that include TorchXRayVision
supervised models (XRV), BenchX VLM 0-shot models (VLM-0-shot), BenchX VLM fine-
tuned models (VLM-FT), and all models combined.
60

Finding /
summary target Pair All Models VLM-0-SHOT VLM-FT XRV
Atelectasis vs Find.0.76±0.12 0.42±0.21 0.44±0.25 0.57±0.19 vs Impr.0.78±0.12 0.61±0.23 0.15±0.33 0.51±0.19
Consolidation vs Find.0.77±0.11 0.66±0.17 0.00±0.30 0.63±0.15 vs Impr.0.79±0.09 0.79±0.13−0.04±0.31 0.46±0.16
Lung opacity vs Find.0.78±0.09 0.58±0.15 0.24±0.28 0.66±0.12 vs Impr.0.75±0.10 0.74±0.15 0.49±0.24 0.71±0.09
Pleural effusion vs Find.0.92±0.02 0.91±0.06 0.36±0.27 0.86±0.08 vs Impr.0.93±0.02 0.95±0.04 0.32±0.29 0.86±0.08
Macro Avg. vs Find.0.86±0.06 0.89±0.07 0.73±0.12 0.82±0.08 vs Impr.0.96±0.01 0.84±0.08 0.59±0.17 0.91±0.06
Micro Avg. vs Find.0.93±0.01 0.94±0.05 0.62±0.15 0.74±0.07 vs Impr.0.96±0.01 0.90±0.06 0.53±0.18 0.89±0.04
Table E.28: MIMIC SRCC across pathologies and model groups. Pairs compare FUSE-OR
image labels against labels from radiology report findings (Find.) or impressions (Impr.)
section annotations. Macro average refers to the SRCC of rankings derived from the macro-
averaged ROC-AUCs of the four selected pathologies. SRCC is calculated across model groups
that include TorchXRayVision supervised models (XRV), BenchX VLM 0-shot models (VLM-
0-shot), BenchX VLM fine-tuned models (VLM-FT), and all models combined.
Finding /
summary target Pair All Models VLM-0-SHOT VLM-FT XRV
Atelectasis vs Find.0.58±0.11 0.31±0.18 0.33±0.20 0.45±0.16 vs Impr.0.61±0.12 0.47±0.20 0.11±0.24 0.41±0.17
Consolidation vs Find.0.59±0.10 0.52±0.18−0.00±0.22 0.46±0.14 vs Impr.0.61±0.09 0.65±0.16−0.02±0.23 0.36±0.15
Lung opacity vs Find.0.61±0.08 0.44±0.16 0.17±0.21 0.50±0.14 vs Impr.0.60±0.10 0.58±0.17 0.37±0.20 0.60±0.11
Pleural effusion vs Find.0.78±0.05 0.83±0.11 0.27±0.21 0.73±0.11 vs Impr.0.80±0.05 0.89±0.09 0.24±0.22 0.74±0.10
Macro Avg. vs Find.0.67±0.05 0.57±0.15 0.13±0.20 0.36±0.13 vs Impr.0.74±0.05 0.80±0.11 0.11±0.21 0.55±0.13
Table E.29: MIMIC KRCC across pathologies and model groups. Pairs compare FUSE-OR
image labels against labels from radiology report findings (Find.) or impressions (Impr.)
section annotations. Macro average refers to the KRCC of rankings derived from the macro-
averaged ROC-AUC of the four selected pathologies. KRCC is calculated across model groups
that include TorchXRayVision supervised models (XRV), BenchX VLM 0-shot models (VLM-
0-shot), BenchX VLM fine-tuned models (VLM-FT), and all models combined.
61

Appendix F. LabelFusionMethods: AgreementwithConflict-Resolved
Image-derived Labels
Figure 6 and Appendix Figure C.15 show the agreement between each image-
derived label fusion method and the XQA-RR conflict-resolved (CR) labels,
supporting the use of FUSE_OR as a proxy for CR in MIMIC-CXR, where no
conflict resolver is available (Table F.30).
Pathologyκ w κlow κhigh F1 F1 low F1high
MV
Atelectasis 0.76 0.14 1.00 0.75 0.69 1.00
Consolidation 0.87 0.51 1.00 0.90 0.87 1.00
Lung Opacity 0.79 0.30 1.00 0.78 0.72 1.00
Pleural Effusion 0.87 0.54 1.00 0.88 0.85 1.00
Macro avg. (four selected) 0.83 0.37 1.00 0.83 0.78 1.00
Macro avg. (all 12) 0.76 0.35 1.00 0.92 0.90 1.00
Micro avg. (all 12) 0.82 0.40 1.00 0.92 0.90 1.00
DS-EM
Atelectasis 0.23 0.20 0.25 0.68 0.67 0.73
Consolidation 0.60 0.51 0.65 0.86 0.86 0.91
Lung Opacity 0.65 0.56 0.69 0.80 0.81 0.87
Pleural Effusion 0.81 0.73 0.84 0.90 0.91 0.95
Macro avg. (four selected) 0.57 0.50 0.61 0.81 0.81 0.87
Macro avg. (all 12) 0.54 0.42 0.60 0.92 0.92 0.95
Micro avg. (all 12) 0.64 0.53 0.69 0.92 0.92 0.95
FUSE_OR
Atelectasis 0.93 0.87 0.95 0.95 0.95 0.98
Consolidation 0.90 0.83 0.93 0.95 0.95 0.98
Lung Opacity 0.78 0.61 0.85 0.83 0.83 0.93
Pleural Effusion 0.89 0.75 0.94 0.92 0.91 0.98
Macro avg. (four selected) 0.87 0.77 0.92 0.91 0.91 0.97
Macro avg. (all 12) 0.78 0.59 0.89 0.95 0.95 0.98
Micro avg. (all 12) 0.82 0.69 0.87 0.94 0.94 0.98
FUSE_AND
Atelectasis 0.21 0.17 0.25 0.66 0.66 0.73
Consolidation 0.57 0.48 0.61 0.85 0.85 0.90
Lung Opacity 0.60 0.44 0.70 0.76 0.75 0.88
Pleural Effusion 0.77 0.62 0.84 0.87 0.87 0.95
Macro avg. (four selected) 0.54 0.43 0.60 0.79 0.78 0.87
Macro avg. (all 12) 0.48 0.37 0.54 0.91 0.91 0.95
Continued on next page
62

Pathologyκ w κlow κhigh F1 F1 low F1high
Micro avg. (all 12) 0.60 0.47 0.66 0.91 0.91 0.95
MACE
Atelectasis 0.93 0.87 0.94 0.95 0.95 0.98
Consolidation 0.90 0.81 0.94 0.94 0.95 0.98
Lung Opacity 0.75 0.50 0.86 0.81 0.79 0.94
Pleural Effusion 0.86 0.66 0.94 0.90 0.88 0.98
Macro avg. (four selected) 0.86 0.71 0.92 0.90 0.89 0.97
Macro avg. (all 12) 0.77 0.56 0.88 0.94 0.94 0.98
Micro avg. (all 12) 0.81 0.66 0.87 0.94 0.94 0.98
NN Fusion
Atelectasis 1.00 0.99 1.00 1.00 1.00 1.00
Consolidation 0.86 0.69 0.92 0.92 0.91 0.98
Lung Opacity 0.82 0.61 0.91 0.85 0.84 0.96
Pleural Effusion 0.87 0.73 0.93 0.91 0.90 0.98
Macro avg. (four selected) 0.89 0.76 0.94 0.92 0.91 0.98
Macro avg. (all 12) 0.71 0.53 0.82 0.96 0.96 0.99
Micro avg. (all 12) 0.89 0.75 0.94 0.96 0.96 0.99
NN Fusion (PS)
Atelectasis 1.00 1.00 1.00 1.00 1.00 1.00
Consolidation 0.87 0.76 0.92 0.94 0.93 0.98
Lung Opacity 0.84 0.68 0.90 0.87 0.87 0.96
Pleural Effusion 0.91 0.76 0.96 0.92 0.92 0.99
Macro avg. (four selected) 0.90 0.80 0.95 0.93 0.93 0.98
Macro avg. (all 12) 0.69 0.56 0.79 0.96 0.96 0.99
Micro avg. (all 12) 0.89 0.77 0.94 0.96 0.96 0.99
TableF.30: XQA-RRagreementbetweenimage-onlyalgorithmlabelsandtheconflict-resolved
image labels.κ w denotes quadratically weighted Cohen’sκcomputed on the original three-
class labels (negative, uncertain, positive).κ low andκ high denote unweighted Cohen’sκ
under pessimistic and optimistic uncertainty mappings, respectively. F1low and F1high are
computed under the same mappings.
Figures F.20–F.24 show model rankings on XQA-RR using fusion-derived
labels as the reference.
63

CR MACE FUSE_OR NN_FUSIONNN_FUSION(PS) FUSE_AND DS images FUSE_UNC
Evaluation references
5
10
15
20
25
30
35 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT
Figure F.20: XQA-RR model rankings using fusion labels as reference forAtelectasis.
CR MACE FUSE_OR NN_FUSIONNN_FUSION(PS) FUSE_AND DS images FUSE_UNC
Evaluation references
5
10
15
20
25
30
35 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT
Figure F.21: XQA-RR model rankings using fusion labels as reference forConsolidation.
64

CR MACE FUSE_OR NN_FUSIONNN_FUSION(PS) FUSE_AND DS images FUSE_UNC
Evaluation references
5
10
15
20
25
30
35 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT
Figure F.22: XQA-RR model rankings using fusion labels as reference forLung opacity.
CR MACE FUSE_OR NN_FUSIONNN_FUSION(PS) FUSE_AND DS images FUSE_UNC
Evaluation references
5
10
15
20
25
30
35 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT
Figure F.23: XQA-RR model rankings using fusion labels as reference forPleural effusion.
65

CR MACE FUSE_OR NN_FUSIONNN_FUSION(PS) FUSE_AND DS images FUSE_UNC
Evaluation references
5
10
15
20
25
30
35 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT
Figure F.24: XQA-RR model rankings using fusion labels as reference on ROC-AUC macro-
averaged across the four selected pathologies.
66

Appendix G. MIMIC: Findings vs. Impressions Label Source
Figures G.25a–G.25e show how model rankings on MIMIC-CXR change de-
pending on whether labels are derived from the Findings or Impressions section
of the report.
Impression Findings
Evaluation references
5
10
15
20
25 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT
(a) Atelectasis
Impression Findings
Evaluation references
5
10
15
20
25 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT (b) Consolidation
Impression Findings
Evaluation references
5
10
15
20
25 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT (c) Lung opacity
Impression Findings
Evaluation references
5
10
15
20
25 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT
(d) Pleural effusion
Impression Findings
Evaluation references
5
10
15
20
25 Rank (1 is best)
XRV VLM-FT VLM-0-SHOT (e) Macro-average
Figure G.25: MIMIC-CXR model rankings induced by labels derived from the Findings and
Impressions sections of the radiology report.
67
