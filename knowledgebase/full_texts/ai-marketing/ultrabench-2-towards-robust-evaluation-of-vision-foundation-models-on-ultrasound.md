---
title: 'UltraBench 2: Towards Robust Evaluation of Vision Foundation Models on Ultrasound'
url: https://arxiv.org/abs/2609.28610
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Ashwath Radhachandran
- Adam Tupper
- Christian Gagné
- William Speier
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.28610
pages: 30
chars: 108354
fetched_at: '2026-11-08T13:25:14+00:00'
kb_version: 1
---

# UltraBench 2: Towards Robust Evaluation of Vision Foundation Models on Ultrasound

Under review
UltraBench 2: Towards Robust Evaluation of Vision Foundation
Models on Ultrasound
Ashwath Radhachandran∗ ashw athradha123@g.ucla.edu
Bioengineering Department, University of California, Los Angeles
Adam Tupper∗ adam.tupper.1@ula v al.ca
Institut Intelligence et Données (IID), Université Laval
Mila – Quebec AI Institute
Christian Gagnéchristian.gagne@gel.ula v al.ca
Institut Intelligence et Données (IID), Université Laval
Canada-CIFAR AI Chair
Mila – Quebec AI Institute
William Speier speier@ucla.edu
Radiological Sciences Department, UCLA David Geffen School of Medicine
Bioengineering Department, University of California, Los Angeles
Abstract
Benchmarking is an increasingly critical part of
research in machine learning and the domains
where it is applied, including healthcare. Yet, de-
spite the steady development of new ultrasound
foundation models in recent years, the devel-
opment of well-designed benchmarks to evalu-
ate them has lagged behind. This deficiency
has led to fragmented and inconsistent evalua-
tions of competing models, making it difficult
to measure progress. To address this issue, we
introduce UltraBench 2, a comprehensive bench-
mark with wide anatomical and task coverage,
and a focus on standardization, reproducibil-
ity, and ease-of-use. Using this benchmark, we
compare existing vision foundation models for
ultrasound image analysis. Our analyses demon-
strate that ultrasound-specific pretraining still
leads on classification, but that state-of-the-art
general-purpose models have drawn level on seg-
mentation.
Keywords:ultrasound, benchmark, foundation
models, medical imaging
Data and Code AvailabilityDatasets, models,
code, and a public leaderboard are available at
https://github.com/adamtupper/ultrabench2.
∗ These authors contributed equally.
1. Introduction
Benchmarks are crucial for capturing the attention of
researchers and driving progress on important prob-
lems (Hendrycks and Woodside, 2024). However,
despite the steady development of new ultrasound
foundation models, the establishment of well-designed
benchmarkstoevaluatethemhaslaggedbehind. Since
the core value proposition of these models is that they
are “general-purpose” and can be adapted to a wide
variety of tasks with limited supervision, we require
diverse benchmarks to evaluate their claims.
Well-designed benchmarks have several important
characteristics. They should have clear and repro-
ducible evaluation protocols to ensure fair compar-
isons, easy-to-use interfaces to minimize the barri-
ers to entry, and a wide coverage of tasks to assess
model flexibility. As summarized in Table 1 and dis-
cussed in Section 2.1, existing medical image analysis
benchmarks satisfy some, but not all of these criteria.
This limitation makes it difficult to reliably measure
progress in ultrasound analysis.
In this paper, we propose UltraBench 2, a new
benchmark for ultrasound foundation models that im-
proves upon the usability and coverage of existing
alternatives, standardizing dataset preprocessing and
model evaluation in an easy to use package. This
benchmark builds upon the foundations of existing
benchmarks (Jiang et al., 2025; Ma et al., 2026; Tup-
per and Gagné, 2025), expanding the set of tasks,
improving usability, and standardizing evaluation.
©A. Radhachandran, A. Tupper, C. Gagné & W. Speier.
arXiv:2609.28610v1  [cs.CV]  23 Sep 2026

UltraBench 2
Using UltraBench 2, we perform a retrospective
analysis of existing ultrasound foundation models and
identify areas in which they excel and struggle. We
find that existing models tend to struggle more at
pathological tasks (e.g., segmenting pathological struc-
tures, diagnosing malignancy) than non-pathological
tasks (e.g., segmenting anatomical structures or identi-
fying fetal anatomical planes). We also find that state-
of-the-art general-purpose vision foundation models,
specifically DINOv3 (Siméoni et al., 2025), have closed
the gap on image segmentation performance. These
insights provide focus for the development of future
models and highlight promising avenues for improve-
ment.
The remainder of this paper is organized as fol-
lows. First, we compare UltraBench 2 to previous
benchmarks and describe the current landscape of
ultrasound foundation models. Then, in Section 3, we
describe the design of the benchmark and it’s tasks.
Finally, we perform a retrospective analysis of exist-
ing models using the benchmark, present our findings,
and discuss the implications for future work on the
development of ultrasound foundation models.
2. Related Work
2.1. Benchmarks in Medical Imaging
Good examples of multi-domain biomedical imaging
benchmarks are MedMNIST v2 (Yang et al., 2023),
MedSegBench (Kuş and Aydin, 2024), and MedIMeta
(Woerner et al., 2025). These benchmarks satisfy
many of the important qualities described in the intro-
duction: they standardize the format of the individ-
ual datasets and the preprocessing applied to images,
define evaluation metrics, and provide user-friendly
interfaces for downloading and working with the data.
However, these datasets include few ultrasound tasks.
The few existing ultrasound-specific benchmarks
(Jiang et al., 2025; Ma et al., 2026; Tupper and Gagné,
2025) each have gaps, as shown in Table 1. Each one
covers a good range of anatomical regions and tasks,
but they fall short on reproducibility and usability.
No benchmark provides fixed train and test splits
directly. UltraBench provides code to generate the
splits, using fixed random seeds. But this still cannot
guarantee the exact same split on a different machine
or software version. The remaining benchmarks do
not release the code for splitting at all, so the original
splits cannot be recovered.
The same problem applies to preprocessing. Ultra-
Bench and US-43d release the code used to prepare
the images. This adds work for other researchers, but
the steps can still be reproduced. UniUS-Bench and
UltraFedFM do not. For these benchmarks, the exact
images cannot be reproduced at all, making repro-
ducibility impossible (without help from the original
authors) rather than just inconvenient.
Existing benchmarks also only link to the original
datasets. Researchersmustdownloadeachdatasetsep-
arately and convert it to a usable format themselves.
This creates further room for differences between se-
tups. UniUS-Bench, UltraBench, and US-43d also
include datasets with narrow, competition-specific li-
censes (Butterfly Network, 2018; Morelia et al., 2016),
which could limit their use. All other benchmarks use
datasets with non-commercial or more open licenses.
Together, these problems make results hard to repli-
cate and the benchmarks hard to use. We argue this
has led to the current situation of models being tested
on different sets of tasks and compared against dif-
ferent sets of competing models (see Appendix A).
U2-Bench (Le et al., 2026) was recently released to
address similar issues for large vision-language models,
but it is not designed to evaluate vision foundation
models.
2.2. Ultrasound Foundation Models
There has been a steady stream of ultrasound founda-
tion model releases since 2023. These models have ap-
plied and adapted self-supervised learning techniques
developed for general-purpose vision foundation mod-
els, often to train vision transformers (ViTs) (Doso-
vitskiy et al., 2021) with modifications to address
ultrasound-specific image characteristics, such as low
signal-to-noise ratio.
Nearly all models use transformer-based architec-
tures. USFM (Jiao et al., 2024), URFM (Kang et al.,
2025), USE-MAE (Megahed et al., 2026), UltraFedFM
(Jiang et al., 2025), and TinyUSFM (Ma et al., 2026)
all use variants of the ViT architecture. Both ViT and
ConvMAE (Gao et al., 2022) models were released for
DeblurringMIM (Kang et al., 2024). EchoCare (Zhang
et al., 2025a) is a Swin Transformer model (Liu et al.,
2021). UltraSam (Meyer et al., 2025) and SAMUS
(Lin et al., 2024) use Segment Anything Model (SAM)-
style ViT (Kirillov et al., 2023), but SAMUS uses a
pretrainedViTbackbonewithaparallelCNNtoadapt
the model to ultrasound. Finally, OpenUS (Zheng
2

UltraBench 2
Table 1: A comparison between ultrasound-specific and general biomedical image analysis benchmarks.
UltraBench 2 is the only benchmark integrating dataset downloading, standardized preprocessing
and evaluation, a diverse coverage of ultrasound tasks and anatomical regions, and permissive
licensing. †See Appendix B.4 for details on how anatomical regions are counted.
Benchmark Ultrasound tasks Anatomical regions† Standardized preprocessing Train/test splits Download interface Licensing Leaderboard Class. Seg.
Biomedical image
MedMNIST v2 1 – 1 Yes Yes Yes Non-commercial No
MedSegBench – 5 5 Yes Yes Yes Non-commercial No
MedIMeta 2 – 1 Yes Yes Yes Non-commercial No
Ultrasound-specific
UniUS-Bench 8 10 12 No No No Restricted No
UltraBench 7 7 10 Code Code No Restricted No
UltraFedFM 10 5 13 No No No Non-commercial No
US-43d – 43 13 Code No No Restricted No
UltraBench 2 11 10 10 Yes Yes Yes Non-commercial Yes
et al., 2025) uses the VMamba architecture (Liu et al.,
2024).
The majority of ultrasound foundation mod-
els, USFM, DeblurringMIM, URFM, USF-MAE,
EchoCare, and UltraFedFM, are pretrained via
masked image modeling (Xie et al., 2022; He et al.,
2022). USFM introduces a dual spatial-frequency
masking scheme to improve robustness to low-quality
images, while DeblurringMIM blurs its inputs, chal-
lenging reconstruction to recover fine-grained diag-
nostic detail. URFM and TinyUSFM instead target
learned representations rather than pixels. URFM re-
constructs BiomedCLIP features (Zhang et al., 2025c),
integrating additional medical insight, and TinyUSFM
distills a pretrained USFM into a ViT-Tiny student
using a curated pretraining dataset and a distillation
loss designed to prevent collapse. EchoCare adds a
second, anatomy-classifier decoder so that represen-
tations encode hierarchical anatomical relationships.
SAMUS and UltraSAM are the only models to have
been pre-trained using supervised training for seman-
tic segmentation.
Across these models, pretraining data is drawn
from public sources, private repositories, or a mix-
ture of both. Dataset sizes range from tens of thou-
sands (SAMUS), to millions (UltraFedFM, USFM,
and EchoCare) of images. Most models are trained
on diverse multi-organ, multi-center, and multi-device
sets of images. A notable exception is DeblurringMIM,
which was trained exclusively on 280,000 thyroid ul-
trasound images.
In addition to ultrasound foundation models, we
also benchmark several ViT and ConvNeXt (Liu et al.,
2022) DINOv3 models (Siméoni et al., 2025) as ref-
erences for the performance state-of-the-art general
purpose image foundation models. Further details
about each model and their pre-training data, are
included in Appendix A.
3. UltraBench 2
3.1. Design Principles
The design of UltraBench 2 follows principles drawn
from established guidance on benchmark construc-
tion (Maier-Hein et al., 2020; Reuel et al., 2024; Ott
et al., 2022; Hendrycks and Woodside, 2024) and the
shortcomings of the existing benchmarks discussed in
Section 2.
Broad coverage.Model rankings are sensitive to
the choice of evaluation tasks (Dehghani et al., 2021;
Kerssies et al., 2024), so a single dataset or task
type is insufficient for model selection. UltraBench
2 spans both segmentation and classification across
10 anatomical regions, five clinical application areas,
and multiple transducer types. Similar to Simumba
et al. (2026), we group tasks into categories to report
capability-level scores (classification vs. segmentation;
pathological vs. anatomical targets) that show where
models are strong or weak.
Standardization.We publish fixed train/test
splits, preprocessed test sets, and evaluation scripts
to ensure that submissions are evaluated on identical
inputs using identical evaluation protocols. Follow-
ing the recommendations of Jiménez-Sánchez et al.
3

UltraBench 2
(2024), details of how each task/dataset is prepared
are included in Appendix B.
A low barrier to entry.Every dataset is exposed
through a unified interface built on Hugging Face
Datasets (Lhoest et al., 2021) to maximize the ease of
use and interoperability with different deep learning
frameworks. An example of this interface is shown
in Listing 1. We also provide reference PyTorch im-
plementations of existing models and task-specific
heads. To ensure consistency and streamline submis-
sions we provide framework-independent evaluation
scripts that calculate the benchmark metrics based on
CSV prediction files (i.e., per-image/sequence/patient
labels for classification tasks and run-length encoded
(RLE) strings for segmentation tasks), similar to chal-
lenges hosted on Kaggle and Grand Challenge.
Longevity.Benchmarks lose their discriminative
power as they saturate, and design choices at con-
struction time play a part in how quickly this happens
(Akhtar et al., 2026; Ott et al., 2022). We screened
candidate datasets for reported performance ceilings
to try to retain tasks with room for improvement.
We also restrict number of training examples for each
task to a maximum of 1000 patients, sequences, or
images (depending on the granularity of the labels).
Longevity also depends on stewardship. We host mir-
rorsofthesourcedatasetswherepermittedundertheir
licenses and maintain a public leaderboard restricted
to reproducible open-source submissions.
3.2. Tasks
UltraBench 2 includes the 10 semantic segmentation
and 11 image classification tasks listed in Table 2.
These tasks cover clinical and non-clinical applications:
cancer screening, prenatal care, anatomical region
segmentation, disease diagnosis, and image quality
assessment. Detailed descriptions of each task are
included in Appendix B.2.
3.3. Dataset Curation and Processing
The 12 datasets in UltraBench 2 are curated from ex-
isting publicly available sources with non-commercial
or more open licenses. When considering datasets for
inclusion, we took particular care to exclude those
with previously raised concerns about data quality
(e.g., BUSI(Al-Dhabyanietal.,2020;Pawłowskaetal.,
2023)), that contain heavily annotated images (e.g.,
LEPset (Li et al., 2024)) or with potential licens-
ing issues (e.g., Butterfly (Butterfly Network, 2018),
POCUS (Born et al., 2021), and US Nerve (More-
lia et al., 2016)). We also preferred smaller datasets
(e.g., TN3K (Gong et al., 2023) over Stanford Thyroid
(Stanford AIMI Center, 2021)) where multiple suit-
able options were available, to avoid overly limiting
pretraining corpora.
For the selected datasets, the images are divided
into training and test splits using stratified sampling
where applicable to ensure similar label distributions
between the two splits. For datasets with multiple im-
ages per patient, the dataset is split by patient. Since
the datasets contain a mixture of RGB, RGBA, and
greyscale images, we convert all images to RGB by
either stacking single channel images, or removing the
alpha channel. Other than standardizing the number
of channels, no further pre-processing (e.g., resizing)
is applied to the training images. This provides maxi-
mum freedom for new submissions to innovate on both
data augmentation and preprocessing as well as model
architecture and training algorithms. For the test set,
two versions are published. One version with original-
sized images (with the same minimal preprocessing
as the training set) and another copy with the images
resized to256 × 256pixels using “letterbox” resizing
to preserve their original aspect ratios. Performance
is reported on this version to ensure that comparisons
between models are fair.
We provide hosted versions of datasets that we
have licenses to redistribute on the Hugging Face
Hub. These datasets are either distributed in their
preprocessed form, for those that allow derivatives, or
preprocessed (and cached) by the package at runtime
for datasets under non-derivative licenses. For the
Open Kidney and GBCU datasets, which are gated
behind research use agreements, users provide a path
to the raw data, which is processed and cached in the
same manner as a hosted non-derivative dataset.
3.4. Model Evaluation
Performance on classification and segmentation tasks
is measured using macro F1 and positive Dice scores,
respectively. The positive Dice score excludes the
background class since the object(s) of interest typi-
cally represent only a small fraction of the image and
including the background would inflate results.
The individual task scores are aggregated into four
category scores: anatomical segmentation, patho-
logical segmentation, pathological classification, and
non-pathological classification. This distinguishes a
model’s ability to segment anatomical structures (e.g.,
4

UltraBench 2
Table 2: Evaluation tasks in UltraBench 2. Frame counts are given as train/test; the training split is capped
at 1000 examples per task. For tasks with patient- or sequence-level labels, one example is one
patient or sequence, respectively. Class counts include the background class for segmentation tasks.
Task Classes Dataset Anatomy Transducer Frames (train/test) Patients Labels
Pathological classification
Breast tumor pathology 2 BUS-BRA (Gómez-Flores et al., 2024) Breast Linear 1000/875 1064 Frame
Breast tumor histology 9 BUS-BRA (Gómez-Flores et al., 2024) Breast Linear 1000/875 1064 Frame
COVID-19 2 COVID-BLUES (Wiedemann et al., 2025) Lung Convex 21528/10218 63 Patient
Gallbladder tumor 3 GBCU (Basu et al., 2022) Gallbladder Convex 1000/122 218 Frame
Liver mass 3 AUL (Xu et al., 2023) Liver Convex 588/147 735 Frame
MASLD 2 MASLD (Byra et al., 2018) Liver Convex 440/110 55 Patient
Ovarian tumor 8 MMOTU-2D (Zhao et al., 2023) Ovary Convex 1000/469 247 Frame
Thyroid nodule 2 TN3K (Gong et al., 2023) Thyroid Linear 1000/614 1119 Frame
Non-pathological classification
Cardiac image quality 3 CAMUS (Leclerc et al., 2019) Heart Phased array 17264/1968 500 Sequence
Fetal brain plane 4 Fetal Planes (Burgos-Artizzu et al., 2020) Fetus Convex 1000/2092 1082 Frame
Fetal plane 6 Fetal Planes (Burgos-Artizzu et al., 2020) Fetus Convex 1000/11400 1792 Frame
Pathological segmentation
Breast tumor 2 BUS-BRA (Gómez-Flores et al., 2024) Breast Linear 1000/875 1064 Frame
Liver mass 2 AUL (Xu et al., 2023) Liver Convex 588/147 735 Frame
Ovarian tumor 2 MMOTU-2D (Zhao et al., 2023) Ovary Convex 1000/469 247 Frame
Thyroid nodule 2 TN3K (Gong et al., 2023) Thyroid Linear 1000/614 1119 Frame
Anatomical segmentation
Liver 2 AUL (Xu et al., 2023) Liver Convex 587/147 734 Frame
Cardiac region 4 CAMUS (Leclerc et al., 2019) Heart Phased array 1000/1968 500 Frame
Kidney capsule 2 Open Kidney (Singla et al., 2023) Kidney Convex 411/103 514 Frame
Kidney regions 4 Open Kidney (Singla et al., 2023) Kidney Convex 411/103 514 Frame
Pubic symphysis–fetal head 3 PSFHS (Chen et al., 2024) Pelvis, fetus Convex 1000/358 1124 Frame
Muscle 2 STMUS (Marzola et al., 2021) Muscle Linear 1000/7169 1223 Frame
from ultrabench2 import load_dataset
from torch.utils.data import DataLoader
# A hosted dataset
dataset = load_dataset(name="AUL")
# Or, a local dataset
dataset = load_dataset(
name="OpenKidney",
path="path/to/raw/data",
)
# Use with any framework (e.g., PyTorch)
loader = DataLoader(dataset["test.256"])
Listing 1: A unified interface for using hosted and
local datasets, backed by Hugging Face Datasets.
organs) and pathological structures (e.g., nodules),
as anatomical structures tend to be larger and more
clearly defined than pathological ones. It also sepa-
rates diagnostic tasks from image quality and catego-
rization tasks. For tasks with patient- or sequence-
level labels, performance is measured per-patient or
per-sequence.
Each submission must provide test set predictions
for S = 5different seeds per task. Let Yk,r be the
performance metric of taskk under run r, and let a
category consist ofK tasks scored overS runs. The
reported category score is the unweighted mean of the
run-averaged task scores:
¯Y= 1 K
KX
k=1
¯Yk, ¯Yk = 1 S
SX
r=1
Yk,r.(1)
Uncertainty is quantified using error bars, ¯Y±
SE( ¯Y ), which combine two sources of noise: the vari-
ability across runs and the sampling noise in the test
sets. Both are computed at the level of the cate-
gory score rather than per task, so that correlations
between tasks that share a test set (e.g., BUS-BRA
pathology and histology classification) are not ignored.
SE( ¯Y)is calculated as
SE( ¯Y) =
r
σ2run
S +σ 2 boot,(2)
where σrun is the standard deviation across runs of
the per-run category score, andσboot is the standard
deviation of the category score across 2000 bootstrap
replications. Each replication resamples the test set
of each dataset and recomputes the category score
with each task’s metric averaged over the five runs.
Where a dataset provides per-image patient identifiers,
5

UltraBench 2
resampling is done at the patient level, since frames
from one patient are correlated.
Because we fix the train/test split, these standard
errors are conditional this split. They quantify sam-
pling variability of the test cohorts and stochasticity
of training, not variability that would arise from a
different split, different hyperparameter search, or a
different source population.
3.5. Leaderboard
To track the progress of ultrasound foundation models,
we provide a leaderboard for open source models and
encourage users to evaluate their models on different
categories. We restrict the leaderboard to open source
models to mitigate the risk of evaluations being per-
formed in bad faith, as the datasets are public and
there are no hidden/private test sets that could be
used to prevent bad actors from training on the test
data.
4. Evaluations of Existing Models
We performed a retrospective analysis of existing ultra-
sound foundation models to populate the benchmark.
It is important to note that some of the datasets
used in the benchmark were used in the pretraining
phase of existing models. The extent of this overlap
is documented in Appendix H.
4.1. Evaluation Setup
Each model described in Section 2.2 is evaluated via
full fine-tuning and head-only training (i.e., frozen
backbone). Full fine-tuning has a higher performance
potential as it allows models to adapt the learned
features to the specific task, at the cost of higher com-
putational requirements and the potential to overfit on
small datasets. Head-only training is computational
cheaper and limits the risk of overfitting, but relies
on the model being able to extract relevant features
for the task without adaptation.
For both training regimes, the models are trained
for a maximum of 10,000 steps using AdamW, a batch
size of 32, and a Cosine annealing learning rate sched-
uler with an initial learning rate of ηhead = 1e−3.
The models are evaluated every 100 steps on the val-
idation set and early stopping is triggered if there
is no reduction in the validation loss after 10 vali-
dation checks (i.e., 1,000 training steps). For full
fine-tuning, the backbone is frozen for the first 1,000
training steps to allow the randomly-initialized head
to warm up against fixed pre-trained features. The
backbone learning rate is then linearly warmed up
from zero over the following 1,000 steps to a ceiling of
rmax = 0.01 ×η head. We also apply layer-wise learning
rate decay (Howard and Ruder, 2018) to lower the
learning rates for shallower layers and TrivialAugment-
style data augmentation (Müller and Hutter, 2021)
that randomly applies one of identity, rotation (up to
30◦), translation, random resized crop (scale0.6–1.0),
Gaussian noise, or brightness/contrast jitter. Full
training details and hyperparameters are provided in
Appendix C.
Classification.For classification tasks, we attach
a single linear layer mapping the encoder’s finald-
dimensional feature embedding toC class logits. For
isotropic ViT backbones that produced-dimensional
patch token embeddings[B, N, d](TinyUSFM, USFM,
URFM-B/L, UltraFedFM, DeblurringMIM, DINOv3-
ViT-B/L, and UltraSAM), these are mean-pooled to
produce the final embedding vector. For models with
a d-dimensional CLS token (USF-MAE) we use this
directly. For models that produce a spatial feature
map (EchoCare, OpenUS, DINOv3 ConvNeXt, and
SAMUS), this is mean-pooled and flattened into ad-
dimensional embedding. Cross-entropy loss was used
for all tasks. For patient- and sequence-level tasks,
we evaluate each model using the average predicted
probability across all images belonging to the patient
or sequence, respectively. The parameter counts for
each combination of model and head are reported in
Table 9 of the appendix.
Segmentation.The segmentation decoder is se-
lected based on each backbone’s output structure. For
models producing patch token sequences or spatial
feature maps (all ViT-based and SAM-based models),
we use a progressive upsampler (PUP) decoder (Zheng
et al., 2021), which reshapes patch tokens[B, N, d]
onto a 2D grid and recovers the target resolution
through a sequence of transposed-convolution stages.
SAMUS and UltraSAM use this decoder because their
SAM-based architectures do not expose intermediate
transformer blocks. For hierarchical multi-scale back-
bones (EchoCare, OpenUS, DINOv3-ConvNeXt), we
use a SegFormer-style MLP decoder (Xie et al., 2021),
which projects each scale to a common width, upsam-
ples to the finest scale, and fuses them. DiceCE loss
(equal weighting for Dice and cross-entropy) was used
for all tasks. The full decoder specifications for each
model are included in Appendix G.
6

UltraBench 2
5. Results
Figure 1 shows the performance of each model in
each category, under full fine-tuning and head-only
training. The breakdown of performance on each task
is included in Appendix E.
Anatomical vs. pathological segmentation.
All models struggle more to segment pathological
structure (e.g., tumors) compared to anatomical
ones (e.g., organs). The worst model’s anatomical
score (EchoCare,0 .801 ± 0.008) exceeds the best
model’s pathological score (DINOv3 ConvNeXt-L,
0.794 ± 0.008). Despite relatively high overall perfor-
mance, some anatomical segmentation tasks remain
very challenging. In particular, for kidney region seg-
mentation all models achieve Dice scores≤0.487.
Non-pathological vs. pathological classification.
Similar to segmentation, we find that pathological
classification scores are consistently lower than the
non-pathological scores for all models. Here, the worst
model’s non-pathological score (TinyUSFM,0.641 ±
0.018) is similar to the best model’s pathological score
(URFM-L,0.645±0.021).
Utility of domain-specific pretraining.A sur-
prising result is that the general-purpose DINOv3 Con-
vNeXt models rank among the best for segmentation
tasks. DINOv3 ConvNeXt-L tops the leaderboard in
pathological segmentation (0.794±0.008) and is fourth
overall in anatomical segmentation (0.822±0.007) and
within the same tier as top performing model, SAMUS
(0.826 ± 0.007), whose pre-training dataset overlaps
with one of the tasks.
For non-pathological classification, DINOv3 ViT-B
(0.716±0.021)isfifthoverallandisthebestperforming
model without pre-training overlap. However, the best
performing DINOv3 model (ViT-L,0.583±0.025) falls
much further from the lead in the more challenging
pathological classification category led by URFM-L
(0.645±0.021).
Head-only training vs. full fine-tuning.The
fully fine-tuned models consistently perform as well
as, and usually much better, than their frozen counter-
parts across all categories. While head-only training is
interesting for evaluating the quality of the represen-
tations learned by the models, at the scale of existing
models (up to 307 million parameters), we recommend
full fine-tuning to maximize performance. All of our
training runs used less than20GB of VRAM, which
could have been further reduced using memory-saving
tricks such as gradient accumulation.
Model size vs. performance.Of the models that
are available in multiple sizes (URFM, DINOv3 ViT,
and DINOv3 ConvNeXt), the larger variants typi-
cally score higher in each category than the smaller
ones, but the differences are usually not significant.
TinyUSFM, the smallest model with only5.5 Mpa-
rameters, is among the worst performing models in
each category. Figure 6 in Appendix D visualizes the
relationship between performance and size.
The evolution of performance over time.Com-
paring the performance and release date of the mod-
els, we find that many models do not outperform
their predecessors within our setup. For example, the
URFM and DINOv3 models (released in August 2025)
and SAMUS (released in September 2023) all outper-
form subsequently released models, such as USF-MAE,
EchoCare, and TinyUSFM. Figures that illustrate per-
formance over time are included in Appendix D.
6. Discussion
6.1. Recommendations for Future Models
Our initial benchmark scores demonstrate the rela-
tive weakness of current models on pathological tasks,
which should be a focus area for future models. They
also highlight several potentially fruitful avenues for
improvement.
Models trained via knowledge distillation (URFM,
DINOv3) perform very well, with the exception of
TinyUSFM, a distilled version of USFM. In particular,
URFM’s approach of distilling knowledge from the
multi-domain BiomedCLIP model appears to be a
key differentiating factor in its leading pathological
classification performance, given that its architecture
(ViT) and training data scale (1,003,465 images) are
not outliers. URFM also leads on non-pathological
classification, though both the CAMUS and Fetal
Planes datasets that the tasks are derived from are
part of its pretraining corpus, so that result should
be interpreted with caution.
Larger pretraining datasets and greater diversity
do not necessarily result in better models. Despite
having among the largest pretraining datasets among
ultrasound models, USFM and EchoCare perform
poorly relative to other models. The Deblurring MIM
models, pretrained exclusively on private thyroid ul-
trasound images, match or exceed both models in all
7

UltraBench 2
URFM-L (0)URFM-B (0) UltraFedFM (0) OpenUS (2)
Deblurring ConvMAE (0)
USF-MAE (3)
Deblurring MAE (0)
UltraSAM (2)
DINOv3 ViT-L (0)
USFM (?)
DINOv3 ViT-B (0)
SAMUS (1)
DINOv3 ConvNeXt-L (0)DINOv3 ConvNeXt-B (0)
EchoCare (?)TinyUSFM (?)
0.50
0.55
0.60
0.65
Macro F1
Pathological Classification
URFM-L (3)URFM-B (3)USF-MAE (3)OpenUS (1)
DINOv3 ViT-B (0)DINOv3 ViT-L (0)UltraFedFM (3)
Deblurring ConvMAE (0)
Deblurring MAE (0)
UltraSAM (1)
USFM (?)
DINOv3 ConvNeXt-B (0)
EchoCare (?)
DINOv3 ConvNeXt-L (0)
SAMUS (1)
TinyUSFM (?)
0.5
0.6
0.7
Non-Pathological Classification
DINOv3 ConvNeXt-L (0)
URFM-L (0)
DINOv3 ConvNeXt-B (0)
SAMUS (1)
DINOv3 ViT-L (0)
URFM-B (0)
DINOv3 ViT-B (0)
OpenUS (2)
Deblurring ConvMAE (0)
Deblurring MAE (0)
USFM (?)
UltraSAM (2)USF-MAE (2) UltraFedFM (0)EchoCare (?)TinyUSFM (?)
0.60
0.65
0.70
0.75
0.80
Positive Dice
Pathological Segmentation
SAMUS (1)OpenUS (3)URFM-L (1)
DINOv3 ConvNeXt-L (0)
URFM-B (1)
DINOv3 ConvNeXt-B (0)
DINOv3 ViT-L (0)
USF-MAE (6)
USFM (?)
DINOv3 ViT-B (0)
Deblurring ConvMAE (0)
Deblurring MAE (0)
UltraSAM (6)UltraFedFM (1)TinyUSFM (?)EchoCare (?)
0.76
0.78
0.80
0.82
Anatomical Segmentation
Figure 1: Full fine-tuning () and head-only () performance in each category. The number in parentheses
denotes the number of tasks whose data overlaps with the pre-training datasets (“?” if the pre-
training datasets are not disclosed). Theboldmodel is the best performing model with no overlap.
categories. One key difference may be data quality:
URFM and the Deblurring MIM models are trained
partially or exclusively, respectively, on private data,
which may be higher quality than data collated from
public sources.
Modern CNN architectures and pretraining meth-
ods may warrant revisiting. The strong performance
of DINOv3 models, particularly for segmentation, sug-
gests that certain combinations of architecture (e.g.,
ConvNeXt + SegFormer), pretraining method, and
pretraining scale for general-purpose vision models
have overcome the benefits domain-specific pretrain-
ing with simpler approaches. The impact of backbone
and decoder architectures should be more deeply in-
vestigated to isolate their effects. The best ultrasound
foundation models retain their segmentation advan-
tage only when the backbone is frozen. We hypothe-
size that this reflects domain shift between DINOv3’s
pretraining data and the test data, though we have
not isolated this.
6.2. Limitations
Several limitations warrant discussion. First, the
benchmark is built on public datasets. While this
problem is not unique to UltraBench 2, it means
that we rely on collaboration from the community
to exclude these datasets during pre-training to keep
comparisons meaningful. Sourcing diverse, private
evaluation data at this scale remains a broader chal-
lenge for the field as a whole.
Second, the hyperparameters, augmentations, and
task heads were not optimized per model. As such,
our results should be viewed as a foundation from
which to build from. We invite the community to
8

UltraBench 2
explore these directions and submit improved results
for new and existing models alike.
Finally, we hope that UltraBench 2 will serve the
community well for years to come, but we recognize
that all benchmarks reach saturation. We intend for
the benchmark to evolve (e.g., by adding new tasks,
resolutions, etc.) to combat this and meet the evolving
needs of the community.
7. Conclusions
Through UltraBench 2, we provide a standardized
evaluation of existing ultrasound foundation models
and highlight their relative strengths and weaknesses
against one another and against general-purpose mod-
els. Our results show that pathological tasks remain
the greatest weakness across models, and that several
newer models fail to outperform older ones under our
protocol. This underscores the need for standardized,
reproducible evaluation to separate genuine capability
gains from artifacts of inconsistent evaluations. We
hope UltraBench 2 offers a more complete picture
of where ultrasound foundation models stand today
and that the community adopts this benchmark as a
common performance standard in future work.
Acknowledgments
This research was enabled in part by support provided
by Calcul Québec (calculquebec.ca) and the Digital
Research Alliance of Canada (alliancecan.ca). It was
also supported through funding from Canadian Insti-
tute for Advanced Research (cifar.ca) and the Natural
Sciences and Engineering Research Council of Canada
(nserc-crsng.gc.ca). This work was also supported by
the UCLA Radiology Exploratory Research Grant.
References
Mubashara Akhtar, Anka Reuel, Prajna Soni, San-
chit Ahuja, Pawan Sasanka Ammanamanchi, Ru-
chit Rawal, Vilém Zouhar, Srishti Yadav, Chenxi
Whitehouse, Dayeon Ki, Jennifer Mickel, Leshem
Choshen, Marek Suppa, Jan Batzner, Jenny Chim,
Jeba Sania, Yanan Long, Hossein A. Rahmani,
Christina Q. Knight, Yiyang Nan, Jyoutir Raj,
Yu Fan, Shubham Singh, Subramanyam Sahoo,
EliyaHabba, UsmanGohar, SiddheshMilindPawar,
Robert Scholz, Arjun Subramonian, Jingwei Ni,
Mykel Kochenderfer, Sanmi Koyejo, Mrinmaya
Sachan, Stella Biderman, Zeerak Talat, Avijit
Ghosh, and Irene Solaiman. When AI Benchmarks
Plateau: A Systematic Study of Benchmark Satu-
ration. InICML ’26: Proceedings of the Twenty-
First International Conference on Machine Learn-
ing, June 2026.
Walid Al-Dhabyani, Mohammed Gomaa, Hussien
Khaled, and Aly Fahmy. Dataset of breast ultra-
sound images.Data in Brief, 28:104863, February
2020. ISSN 2352-3409. doi: 10.1016/j.dib.2019.
104863.
Soumen Basu, Mayank Gupta, Pratyaksha Rana,
Pankaj Gupta, and Chetan Arora. Surpassing
the Human Accuracy: Detecting Gallbladder Can-
cer from USG Images with Curriculum Learning.
In2022 IEEE/CVF Conference on Computer Vi-
sion and Pattern Recognition (CVPR), pages 20854–
20864, June 2022. doi: 10.1109/CVPR52688.2022.
02022. URL https://ieeexplore.ieee.org/document/
9879895. ISSN: 2575-7075.
Jannis Born, Nina Wiedemann, Manuel Cossio, Char-
lotte Buhre, Gabriel Brändle, Konstantin Leider-
mann, Julie Goulet, Avinash Aujayeb, Michael
Moor, Bastian Rieck, and Karsten Borgwardt. Ac-
celerating Detection of Lung Pathologies with Ex-
plainable Ultrasound Image Analysis.Applied Sci-
ences, 11(2):672, January 2021. ISSN 2076-3417.
doi: 10.3390/app11020672.
Xavier P. Burgos-Artizzu, David Coronado-Gutiérrez,
Brenda Valenzuela-Alcaraz, Elisenda Bonet-Carne,
Elisenda Eixarch, Fatima Crispi, and Eduard Grat-
acós. Evaluation of deep convolutional neural net-
works for automatic classification of common ma-
ternal fetal ultrasound planes.Scientific Reports,
10(1):10200, June 2020. ISSN 2045-2322. doi:
10.1038/s41598-020-67076-5. URL https://www.
nature.com/articles/s41598-020-67076-5.
Butterfly Network. ButterflyNet-
work/MITGrandHack2018, 2018. URL
https://github.com/ButterflyNetwork/
MITGrandHack2018. original-date: 2018-04-
12T16:28:54Z.
Michał Byra, Grzegorz Styczynski, Cezary Szmigiel-
ski, Piotr Kalinowski, Łukasz Michałowski, Rafał
Paluszkiewicz, Bogna Ziarkiewicz-Wróblewska,
Krzysztof Zieniewicz, Piotr Sobieraj, and Andrzej
9

UltraBench 2
Nowicki. Transfer learning with deep convolu-
tional neural network for liver steatosis assess-
ment in ultrasound images.International Jour-
nal of Computer Assisted Radiology and Surgery,
13(12):1895–1903, December 2018. ISSN 1861-
6429. doi: 10.1007/s11548-018-1843-2. URL
https://doi.org/10.1007/s11548-018-1843-2.
Gaowen Chen, Jieyun Bai, Zhanhong Ou, Yaosheng
Lu, and Huijin Wang. PSFHS: Intrapartum ul-
trasound image dataset for AI-based segmenta-
tion of pubic symphysis and fetal head.Sci-
entific Data, 11(1):436, May 2024. ISSN 2052-
4463. doi: 10.1038/s41597-024-03266-4. URL https:
//www.nature.com/articles/s41597-024-03266-4.
Mostafa Dehghani, Yi Tay, Alexey A. Gritsenko, Zhe
Zhao, Neil Houlsby, Fernando Diaz, Donald Met-
zler, and Oriol Vinyals. The Benchmark Lottery,
July 2021. URL http://arxiv.org/abs/2107.07002.
arXiv:2107.07002 [cs.LG].
Alexey Dosovitskiy, Lucas Beyer, Alexander
Kolesnikov, Dirk Weissenborn, Xiaohua Zhai,
Thomas Unterthiner, Mostafa Dehghani, Matthias
Minderer, Georg Heigold, Sylvain Gelly, Jakob
Uszkoreit, and Neil Houlsby. An Image is Worth
16x16 Words: Transformers for Image Recognition
at Scale. In9th International Conference on
Learning Representations, ICLR 2021, Virtual
Event, Austria, May 3-7, 2021, 2021. URL
https://openreview.net/forum?id=YicbFdNTTy.
Peng Gao, Teli Ma, Hongsheng Li, Ziyi Lin, Jifeng
Dai, and Yu Qiao. MCMAE: Masked Convolution
Meets Masked Autoencoders. InAdvances in Neural
Information Processing Systems, volume 35, pages
35632–35644. Curran Associates, Inc., 2022. doi:
10.52202/068431-2582.
Haifan Gong, Jiaxin Chen, Guanqi Chen, Haofeng
Li, Guanbin Li, and Fei Chen. Thyroid re-
gion prior guided attention for ultrasound seg-
mentation of thyroid nodules.Computers in
Biology and Medicine, 155:106389, March 2023.
ISSN 0010-4825. doi: 10.1016/j.compbiomed.
2022.106389. URL https://www.sciencedirect.com/
science/article/pii/S0010482522010976.
Wilfrido Gómez-Flores, Maria Julia Gregorio-Calas,
and Wagner Coelho de Albuquerque Pereira. BUS-
BRA: A breast ultrasound dataset for assessing
computer-aided diagnosis systems.Medical Physics,
51(4):3110–3123, April 2024. ISSN 2473-4209. doi:
10.1002/mp.16812.
Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li,
Piotr Dollár, and Ross Girshick. Masked Autoen-
coders Are Scalable Vision Learners. InProceedings
of the IEEE/CVF Conference on Computer Vision
and Pattern Recognition, pages 16000–16009, 2022.
Dan Hendrycks and Thomas Woodside. Devising ML
Metrics, February 2024. URL https://safe.ai/blog/
devising-ml-metrics.
Jeremy Howard and Sebastian Ruder. Universal Lan-
guage Model Fine-tuning for Text Classification. In
Iryna Gurevych and Yusuke Miyao, editors,Pro-
ceedings of the 56th Annual Meeting of the As-
sociation for Computational Linguistics (Volume
1: Long Papers), pages 328–339, Melbourne, Aus-
tralia, July 2018. Association for Computational
Linguistics. doi: 10.18653/v1/P18-1031. URL
https://aclanthology.org/P18-1031/.
Vedrana Ivezić, Mara Pleasure, Ashwath Radhachan-
dran, SaarangPanchavati, ShreeramAthreya, Vivek
Sant, Benjamin Emert, Gregory Fishbein, Corey
Arnold, and William Speier. Pretext Matters: An
Empirical Study of SSL Methods in Medical Imag-
ing, March 2026. URL http://arxiv.org/abs/2603.
22649. arXiv:2603.22649 [cs.CV].
Yuncheng Jiang, Chun-Mei Feng, Jinke Ren, Jun
Wei, Zixun Zhang, Yiwen Hu, Yunbi Liu, Rui
Sun, Xuemei Tang, Juan Du, Xiang Wan, Yong
Xu, Bo Du, Xin Gao, Guangyu Wang, Shaohua
Zhou, Shuguang Cui, and Zhen Li. From pretrain-
ing to privacy: federated ultrasound foundation
model with self-supervised learning.npj Digital
Medicine, 8(1):714, November 2025. ISSN 2398-
6352. doi: 10.1038/s41746-025-02085-0. URL https:
//www.nature.com/articles/s41746-025-02085-0.
Jing Jiao, Jin Zhou, Xiaokang Li, Menghua Xia,
Yi Huang, Lihong Huang, Na Wang, Xiaofan
Zhang, Shichong Zhou, Yuanyuan Wang, and
Yi Guo. USFM: A universal ultrasound foun-
dation model generalized to tasks and organs
towards label efficient image analysis.Med-
ical Image Analysis, 96:103202, August 2024.
ISSN 1361-8415. doi: 10.1016/j.media.2024.
103202. URL https://www.sciencedirect.com/
science/article/pii/S1361841524001270.
10

UltraBench 2
Amelia Jiménez-Sánchez, Natalia-Rozalia Avlona,
Dovile Juodelyte, Théo Sourget, Caroline Vang-
Larsen, Anna Rogers, Hubert D. Zając, and
Veronika Cheplygina. Copycats: the many lives
of a publicly available medical imaging dataset.
Advances in Neural Information Processing Sys-
tems, 37:113383–113404, December 2024. doi:
10.52202/079017-3602.
QB Kang, QC Lao, J Gao, JY Liu, HH Yi, BY Ma,
XF Zhang, and K Li. Deblurring masked image
modeling for ultrasound image analysis.Medical
Image Analysis, 97, 2024. doi: 10.1016/j.media.
2024.103256.
Qingbo Kang, Qicheng Lao, Jun Gao, Wuyongga
Bao, Zhu He, Chenlin Du, Qiang Lu, and Kang
Li. URFM: A general Ultrasound Represen-
tation Foundation Model for advancing ultra-
sound image diagnosis.iScience, 28(8), Au-
gust 2025. ISSN 2589-0042. doi: 10.1016/j.isci.
2025.112917. URL https://www.cell.com/iscience/
abstract/S2589-0042(25)01178-2.
Tommie Kerssies, Daan De Geus, and Gijs Dubbel-
man. How to benchmark vision foundation mod-
els for semantic segmentation? InProceedings of
the IEEE/CVF Conference on Computer Vision
and Pattern Recognition (CVPR) Workshops, pages
1162–1171, June 2024.
Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi
Mao, Chloe Rolland, Laura Gustafson, Tete Xiao,
Spencer Whitehead, Alexander C. Berg, Wan-Yen
Lo, Piotr Dollár, and Ross Girshick. Segment Any-
thing, April 2023. URL http://arxiv.org/abs/2304.
02643. arXiv:2304.02643 [cs].
Zeki Kuş and Musa Aydin. MedSegBench: A Com-
prehensive Benchmark for Medical Image Segmen-
tation in Diverse Data Modalities.Scientific Data,
11(1):1283, November 2024. ISSN 2052-4463. doi:
10.1038/s41597-024-04159-2.
AnjieLe, HenanLiu, YueWang, ZhenyuLiu, Rongkun
Zhu, Taohan Weng, Jinze Yu, Boyang Wang, Yalun
Wu, Kaiwen Yan, Quanlin Sun, Meirui Jiang, Jialun
Pei, Siya Liu, Haoyun Zheng, Zhoujun Li, J. Alison
Noble, Jacques Souquet, Xiaoqing Guo, Manxi Lin,
and Hongcheng Guo. U2-bench: Benchmarking
large vision-language models on ultrasound under-
standing. In C. Vondrick, B. Hariharan, C. Raffel,
L. Pinto, D. Yang, and A. Faust, editors,Inter-
national Conference on Learning Representations,
volume 2026, pages 8174–8225, 2026.
Sarah Leclerc, Erik Smistad, João Pedrosa, An-
dreas Østvik, Frederic Cervenansky, Florian Es-
pinosa, Torvald Espeland, Erik Andreas Rye Berg,
Pierre-Marc Jodoin, Thomas Grenier, Carole Lar-
tizien, Jan D’hooge, Lasse Lovstakken, and Olivier
Bernard. Deep Learning for Segmentation Us-
ing an Open Large-Scale Dataset in 2D Echocar-
diography.IEEE Transactions on Medical Imag-
ing, 38(9):2198–2210, September 2019. ISSN 1558-
254X. doi: 10.1109/TMI.2019.2900516. URL
https://ieeexplore.ieee.org/document/8649738.
Quentin Lhoest, Albert Villanova Del Moral, Yacine
Jernite, Abhishek Thakur, Patrick Von Platen,
Suraj Patil, Julien Chaumond, Mariama Drame,
Julien Plu, Lewis Tunstall, Joe Davison, Mario
Šaško, Gunjan Chhablani, Bhavitvya Malik, Simon
Brandeis, Teven Le Scao, Victor Sanh, Canwen Xu,
Nicolas Patry, Angelina McMillan-Major, Philipp
Schmid, Sylvain Gugger, Clément Delangue, Théo
Matussière, Lysandre Debut, Stas Bekman, Pier-
ric Cistac, Thibault Goehringer, Victor Mustar,
François Lagunas, Alexander Rush, and Thomas
Wolf. Datasets: A Community Library for Nat-
ural Language Processing. InProceedings of the
2021 Conference on Empirical Methods in Natu-
ral Language Processing: System Demonstrations,
pages 175–184, Online and Punta Cana, Dominican
Republic, 2021. Association for Computational Lin-
guistics. doi: 10.18653/v1/2021.emnlp-demo.21.
URL https://aclanthology.org/2021.emnlp-demo.
21.
Jiajia Li, Pingping Zhang, Teng Wang, Lei Zhu,
Ruhan Liu, Xia Yang, Kaixuan Wang, Ding-
gang Shen, and Bin Sheng. DSMT-Net: Dual
Self-Supervised Multi-Operator Transformation for
Multi-Source Endoscopic Ultrasound Diagnosis.
IEEE Transactions on Medical Imaging, 43(1):64–
75, January 2024. ISSN 1558-254X. doi: 10.1109/
TMI.2023.3289859. URL https://ieeexplore.ieee.
org/document/10164159.
Xian Lin, Yangyang Xiang, Li Yu, and Zengqiang Yan.
Beyond Adapting SAM: Towards End-to-End Ul-
trasound Image Segmentation via Auto Prompting
. Inproceedings of Medical Image Computing and
Computer Assisted Intervention – MICCAI 2024,
11

UltraBench 2
volume LNCS 15008. Springer Nature Switzerland,
October 2024.
Yue Liu, Yunjie Tian, Yuzhong Zhao, Hongtian Yu,
Lingxi Xie, Yaowei Wang, Qixiang Ye, Jianbin Jiao,
and Yunfan Liu. VMamba: Visual state space
model. In A. Globerson, L. Mackey, D. Belgrave,
A. Fan, U. Paquet, J. Tomczak, and C. Zhang,
editors,Advances in neural information processing
systems, volume 37, pages 103031–103063. Curran
Associates, Inc., 2024. doi: 10.52202/079017-3273.
Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei,
Zheng Zhang, Stephen Lin, and Baining Guo. Swin
Transformer: Hierarchical Vision Transformer us-
ing Shifted Windows. In2021 IEEE/CVF Inter-
national Conference on Computer Vision (ICCV),
pages 9992–10002, October 2021. doi: 10.1109/
ICCV48922.2021.00986.
Zhuang Liu, Hanzi Mao, Chao-Yuan Wu, Christoph
Feichtenhofer, Trevor Darrell, and Saining Xie.
A ConvNet for the 2020s. InProceedings of the
IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 11976–11986, 2022.
URL https://openaccess.thecvf.com/content/
CVPR2022/html/Liu_A_ConvNet_for_the_
2020s_CVPR_2022_paper.html.
Chen Ma, Jing Jiao, Shuyu Liang, Junhu Fu, Qin
Wang, Zeju Li, Yuanyuan Wang, and Yi Guo.
TinyUSFM: Towards compact and efficient ultra-
sound foundation models.IEEE Journal of Biomed-
ical and Health Informatics, pages 1–14, 2026. doi:
10.1109/JBHI.2026.3678309.
Lena Maier-Hein, Annika Reinke, Michal Kozubek,
Anne L. Martel, Tal Arbel, Matthias Eisenmann,
Allan Hanbury, Pierre Jannin, Henning Müller,
Sinan Onogur, Julio Saez-Rodriguez, Bram van
Ginneken, Annette Kopp-Schneider, and Ben-
nett A. Landman. BIAS: Transparent reporting
of biomedical image analysis challenges.Med-
ical Image Analysis, 66:101796, December 2020.
ISSN 1361-8415. doi: 10.1016/j.media.2020.
101796. URL https://www.sciencedirect.com/
science/article/pii/S1361841520301602.
Francesco Marzola, Nens Van Alfen, Jonne Doorduin,
and Kristen M. Meiburger. Deep learning segmen-
tation of transverse musculoskeletal ultrasound im-
ages for neuromuscular disease assessment.Com-
puters in Biology and Medicine, 135:104623, August
2021. ISSN 00104825. doi: 10.1016/j.compbiomed.
2021.104623. URL https://linkinghub.elsevier.com/
retrieve/pii/S0010482521004170.
Youssef Megahed, Robin Ducharme, Aylin Erman,
Mark C. Walker, Steven Hawken, and Adrian D. C.
Chan. USF-MAE: Ultrasound self-supervised foun-
dation model with masked autoencoding.Biomedi-
cal Signal Processing and Control, 122:110313, Au-
gust 2026. ISSN 1746-8094. doi: 10.1016/j.bspc.
2026.110313.
Adrien Meyer, Aditya Murali, Farahdiba Zarin, Didier
Mutter, and Nicolas Padoy. UltraSam: A Foun-
dation Model for Ultrasound using Large Open-
Access Segmentation Datasets.International Jour-
nal of Computer Assisted Radiology and Surgery,
September 2025. ISSN 1861-6429. doi: 10.1007/
s11548-025-03517-8.
Ana Lina Morelia, DJ Sterling, and Will
Cukierski. Ultrasound Nerve Segmenta-
tion, May 2016. URL https://kaggle.com/
ultrasound-nerve-segmentation.
Samuel G. Müller and Frank Hutter. TrivialAugment:
Tuning-Free Yet State-of-the-Art Data Augmenta-
tion. InProceedings of the IEEE/CVF International
Conference on Computer Vision, pages 774–782,
2021.
Simon Ott, Adriano Barbosa-Silva, Kathrin Blagec,
Jan Brauner, and Matthias Samwald. Mapping
global dynamics of benchmark creation and satu-
ration in artificial intelligence.Nature Communi-
cations, 13(1):6793, November 2022. ISSN 2041-
1723. doi: 10.1038/s41467-022-34591-0. URL
http://arxiv.org/abs/2203.04592. arXiv:2203.04592
[cs.AI].
Anna Pawłowska, Piotr Karwat, and Norbert Żołek.
Letter to the Editor. Re: “[Dataset of breast
ultrasound images by W. Al-Dhabyani, M. Go-
maa, H. Khaled & A. Fahmy, Data in Brief,
2020, 28, 104863]”.Data in Brief, 48:109247,
June 2023. ISSN 2352-3409. doi: 10.1016/j.dib.
2023.109247. URL https://www.sciencedirect.com/
science/article/pii/S2352340923003669.
Anka Reuel, Amelia Hardy, Chandler Smith, Max
Lamparth, Malcolm Hardy, and Mykel J. Kochen-
derfer. BetterBench: Assessing AI Benchmarks,
Uncovering Issues, and Establishing Best Practices.
12

UltraBench 2
InAdvances in Neural Information Processing Sys-
tems, volume 37, pages 21763–21813, December
2024. doi: 10.52202/079017-0685.
Naomi Simumba, Nils Lehmann, Paolo Fraccaro,
Hamed Alemohammad, Geeth De Mel, Salman
Khan, Manil Maskey, Nicolas Longepe, Xiao Xi-
ang Zhu, Hannah Kerner, Juan Bernabe-Moreno,
and Alexandre Lacoste. GEO-Bench-2: From Per-
formance to Capability, Rethinking Evaluation in
Geospatial AI, February 2026. URL http://arxiv.
org/abs/2511.15658. arXiv:2511.15658 [cs].
Oriane Siméoni, Huy V. Vo, Maximilian Seitzer,
Federico Baldassarre, Maxime Oquab, Cijo Jose,
Vasil Khalidov, Marc Szafraniec, Seungeun Yi,
Michaël Ramamonjisoa, Francisco Massa, Daniel
Haziza, Luca Wehrstedt, Jianyuan Wang, Timo-
thée Darcet, Théo Moutakanni, Leonel Sentana,
Claire Roberts, Andrea Vedaldi, Jamie Tolan, John
Brandt, Camille Couprie, Julien Mairal, Hervé Jé-
gou, Patrick Labatut, and Piotr Bojanowski. DI-
NOv3, August 2025. URL http://arxiv.org/abs/
2508.10104. arXiv:2508.10104 [cs.CV].
Rohit Singla, Cailin Ringstrom, Grace Hu, Victoria
Lessoway, Janice Reid, Christopher Nguan, and
Robert Rohling. The Open Kidney Ultrasound
Data Set. In Bernhard Kainz, Alison Noble, Julia
Schnabel, Bishesh Khanal, Johanna Paula Müller,
and Thomas Day, editors,Simplifying Medical Ul-
trasound, pages 155–164, Cham, 2023. Springer Na-
ture Switzerland. ISBN 978-3-031-44521-7. doi:
10.1007/978-3-031-44521-7_15.
Stanford AIMI Center. Thyroid Ultrasound
Cine-clip Dataset, October 2021. URL
https://stanfordaimi.azurewebsites.net/datasets/
a72f2b02-7b53-4c5d-963c-d7253220bfd5.
Adam Tupper and Christian Gagné. Revisiting Data
Augmentation for Ultrasound Images.Transac-
tions on Machine Learning Research, February 2025.
ISSN 2835-8856. URL https://openreview.net/
forum?id=iGcxlTLIL5.
Nina Wiedemann, Dianne de Korte-de Boer, Matthias
Richter, SjorsvandeWeijer, CharlotteBuhre, Franz
A. M. Eggert, Sophie Aarnoudse, Lotte Greven-
donk, Steffen Röber, Carlijn M.E. Remie, Wolfgang
Buhre, Ronald Henry, and Jannis Born. COVID-
BLUeS - a Prospective Study on the Value of
AI in Lung Ultrasound Analysis.IEEE Jour-
nal of Biomedical and Health Informatics, 29(9):
6301–6310, September 2025. ISSN 2168-2208.
doi: 10.1109/JBHI.2025.3543686. URL https://
ieeexplore.ieee.org/document/10903196.
Stefano Woerner, Arthur Jaques, and Christian F.
Baumgartner. A comprehensive and easy-
to-use multi-domain multi-task medical imag-
ing meta-dataset.Scientific Data, 12(1):666,
April 2025. ISSN 2052-4463. doi: 10.1038/
s41597-025-04866-4. URL https://www.nature.
com/articles/s41597-025-04866-4.
Enze Xie, Wenhai Wang, Zhiding Yu, Anima Anand-
kumar, Jose M. Alvarez, and Ping Luo. Segformer:
Simple and efficient design for semantic segmenta-
tion with transformers. In M. Ranzato, A. Beygelz-
imer, Y. Dauphin, P.S. Liang, and J. Wortman
Vaughan, editors,Advances in Neural Information
Processing Systems, volume 34, pages 12077–12090.
Curran Associates, Inc., 2021.
Zhenda Xie, Zheng Zhang, Yue Cao, Yutong Lin,
Jianmin Bao, Zhuliang Yao, Qi Dai, and Han Hu.
Simmim: A simple framework for masked image
modeling. InProceedings of the IEEE/CVF Confer-
ence on Computer Vision and Pattern Recognition
(CVPR), pages 9653–9663, June 2022.
Yiming Xu, Bowen Zheng, Xiaohong Liu, Tao Wu,
Jinxiu Ju, Shijie Wang, Yufan Lian, Hongjun Zhang,
Tong Liang, Ye Sang, Rui Jiang, Guangyu Wang,
Jie Ren, and Ting Chen. Improving artificial intel-
ligence pipeline for liver malignancy diagnosis us-
ing ultrasound images and video frames.Briefings
in Bioinformatics, 24(1):bbac569, January 2023.
ISSN 1477-4054. doi: 10.1093/bib/bbac569. URL
https://doi.org/10.1093/bib/bbac569.
Jiancheng Yang, Rui Shi, Donglai Wei, Zequan Liu,
Lin Zhao, Bilian Ke, Hanspeter Pfister, and Bing-
bing Ni. MedMNIST v2 - A Large-Scale Lightweight
Benchmark for 2D and 3D Biomedical Image Clas-
sification.Scientific Data, 10(1):41, January 2023.
ISSN 2052-4463. doi: 10.1038/s41597-022-01721-8.
Number: 1.
Hongyuan Zhang, Yuheng Wu, Mingyang Zhao, Zhi-
wei Chen, Rebecca Li, Fei Zhu, Haohan Zhao, Xi-
aohua Yuan, Meng Yang, Chunli Qiu, Xiang Cong,
Haiyan Chen, Lina Luan, Randolph H. L. Wong,
Huai Liao, Colin A. Graham, Shi Chang, Guowei
Tao, Dong Yi, Zhen Lei, Nassir Navab, Sebastien
Ourselin, Jiebo Luo, Hongbin Liu, and Gaofeng
13

UltraBench 2
Meng. A Fully Open and Generalizable Foundation
ModelforUltrasoundClinicalApplications, Septem-
ber 2025a. URL http://arxiv.org/abs/2509.11752.
arXiv:2509.11752 [cs].
Hongyuan Zhang, Yuheng Wu, Mingyang Zhao, Zhi-
wei Chen, Rebecca Li, Fei Zhu, Haohan Zhao, Xi-
aohua Yuan, Meng Yang, Chunli Qiu, Xiang Cong,
Haiyan Chen, Lina Luan, Randolph H. L. Wong,
Huai Liao, Colin A. Graham, Shi Chang, Guowei
Tao, Dong Yi, Zhen Lei, Nassir Navab, Sebastien
Ourselin, Jiebo Luo, Hongbin Liu, and Gaofeng
Meng. A Fully Open and Generalizable Foundation
ModelforUltrasoundClinicalApplications, Septem-
ber 2025b. URL http://arxiv.org/abs/2509.11752.
arXiv:2509.11752 [cs].
Sheng Zhang, Yanbo Xu, Naoto Usuyama, Hanwen
Xu, Jaspreet Bagga, Robert Tinn, Sam Preston,
Rajesh Rao, Mu Wei, Naveen Valluri, Cliff Wong,
Andrea Tupini, Yu Wang, Matt Mazzola, Swad-
heen Shukla, Lars Liden, Jianfeng Gao, Angela
Crabtree, Brian Piening, Carlo Bifulco, Matthew P.
Lungren, Tristan Naumann, Sheng Wang, and
Hoifung Poon. A Multimodal Biomedical Foun-
dation Model Trained from Fifteen Million Im-
age–Text Pairs.NEJM AI, 2(1):AIoa2400640, Jan-
uary 2025c. doi: 10.1056/AIoa2400640. URL https:
//ai.nejm.org/doi/abs/10.1056/AIoa2400640.
Qi Zhao, Shuchang Lyu, Wenpei Bai, Linghan Cai,
Binghao Liu, Guangliang Cheng, Meijing Wu, Xi-
ubo Sang, Min Yang, and Lijiang Chen. MMOTU:
A Multi-Modality Ovarian Tumor Ultrasound Im-
age Dataset for Unsupervised Cross-Domain Se-
mantic Segmentation, November 2023. URL
http://arxiv.org/abs/2207.06799. arXiv:2207.06799
[cs.CV].
Sixiao Zheng, Jiachen Lu, Hengshuang Zhao, Xi-
atian Zhu, Zekun Luo, Yabiao Wang, Yanwei
Fu, Jianfeng Feng, Tao Xiang, Philip H.S. Torr,
and Li Zhang. Rethinking Semantic Segmen-
tation from a Sequence-to-Sequence Perspective
with Transformers. In2021 IEEE/CVF Confer-
ence on Computer Vision and Pattern Recogni-
tion (CVPR), pages 6877–6886, Nashville, TN,
USA, June 2021. IEEE. ISBN 978-1-6654-4509-
2. doi: 10.1109/CVPR46437.2021.00681. URL
https://ieeexplore.ieee.org/document/9578646/.
Xiaoyu Zheng, Xu Chen, Awais Rauf, Qifan Fu,
Benedetta Monosi, Felice Rivellese, Myles J. Lewis,
Shaogang Gong, and Gregory Slabaugh. OpenUS:
A Fully Open-Source Foundation Model for Ultra-
sound Image Analysis via Self-Adaptive Masked
Contrastive Learning, November 2025. URL
http://arxiv.org/abs/2511.11510. arXiv:2511.11510
[cs.CV].
Appendix A. Additional Information
on Ultrasound
Foundation Models
A.1. USFM
USFM (Jiao et al., 2024) introduces a spatial-
frequency dual masking scheme built on a masked im-
age modeling (MIM) backbone to improve representa-
tional robustness from low-quality ultrasound images.
Pretraining was conducted on the 3M-US database,
the first multi-organ, multi-center, and multi-device
ultrasound collection at the time. This database had
over two million images from 12 human organs. Eval-
uation was conducted via full fine-tuning of USFM
as a pretrained backbone encoder for segmentation
and classification tasks. Downstream experiments
spanned three task types: segmentation of key struc-
tures (brachial plexus, thyroid nodule, breast tumor,
and fetal abdomen), image classification (breast tumor
malignancy, multi-organ presence, and fetal planes)
and image enhancement. We evaluate the released
ViT-B encoder, which contributes85.7 Mparameters.
A.2. TinyUSFM
TinyUSFM (Ma et al., 2026) addresses the computa-
tional cost of ultrasound foundation models by dis-
tilling USFM into a ViT-Tiny. The resulting student,
with 5.5M parameters, roughly 6.4% of the teacher’s
parameters, was modified to retain the same num-
ber of attention heads as the teacher so that features
could be aligned. The framework has two compo-
nents: 1) feature-gradient driven coreset selection is
used to develop a diverse 200,000-image training set
from the 2.1 million images of USFM’s 3M-US pre-
training dataset and 2) a domain-separated masked
image modeling strategy constructs two masked views
of each image, perturbing the images in spatial and
frequency domains, and scales the feature distillation
loss by the cosine similarity between the teacher’s
representations of the two views, encouraging knowl-
edge transfer where the teacher is consistent across
corruptions. Evaluation was performed with a full
14

UltraBench 2
fine-tuning setup using a single linear layer head for
classification and a lightweight pyramid neck with
an FPN-style decoder for segmentation. Evaluation
was performed on UniUS-Bench, a dataset benchmark
assembled by the authors from public data comprising
8 classification and 10 segmentation tasks across 15
organs. The ViT-Tiny encoder is what we evaluate; at
5.5 Mparameters it is by a wide margin the smallest
backbone in the benchmark.
A.3. URFM
URFM (Kang et al., 2025) proposes a representation-
based masked image modeling framework that has the
ViT encoder reconstruct high-level semantic features
provided by BiomedCLIP, avoiding a potentially in-
efficient pixel-reconstruction objective (Ivezić et al.,
2026) and addressing the low signal-to-noise ratio of
ultrasound. The pretraining dataset had over one
million ultrasound images (approximately 50% was
proprietary) spanning 15 major anatomical organs.
Evaluation was based on full fine-tuning the backbone
encoder for classification tasks. Ten downstream ul-
trasound clinical applications were evaluated across
nine organs. We evaluate both released sizes: the
ViT-B encoder contributes85.8 Mparameters and the
ViT-L encoder303.3 M.
A.4. USF-MAE
USF-MAE (Megahed et al., 2026) follows a standard
masked autoencoder (MAE) framework adapted for ul-
trasound, using a ViT backbone as the encoder and a
lightweight transformer decoder for image reconstruc-
tion from masked patches. The model was pretrained
on the OpenUS-46 dataset, which has about 370,000
2D and 3D ultrasound images from 46 open-source
datasets. Evaluation was performed exclusively via
fine-tuning of the pretrained encoder for three down-
stream classification datasets: BUS-BRA (breast can-
cer), MMOTU-2D(ovariantumors), andGIST514-DB
(gastrointestinal stromal tumors). We evaluate the
ViT-B encoder, which contributes85.8 Mparameters.
A.5. EchoCare
EchoCare (Zhang et al., 2025b) extends the standard
self-supervised MAE architecture with a novel dual-
branch design: an image encoder and image decoder
perform pixel-level masked reconstruction, while a
second anatomy-classifier decoder jointly learns hi-
erarchical anatomical relationships. Pretraining was
conducted on EchoCareData, a public dataset of 4.5
million ultrasound images encompassing 9 major body
regions and 52 anatomical organs. Evaluation was
performed via full fine-tuning the backbone encoder
for 10 tasks in a downstream suite spanning disease
diagnosis classification, lesion segmentation, organ
detection, fetal brain landmark prediction, cardiac
ejection fraction regression, image quality enhance-
ment, and report generation. We evaluate the Swin
Transformer encoder, which contributes120.2 Mpa-
rameters.
A.6. OpenUS
OpenUS (Zheng et al., 2025) is an ultrasound founda-
tion model built exclusively on publicly available data.
OpenUS uses a Vision Mamba (VMamba) backbone,
which captures both local and long-range spatial de-
pendencies via selective state-space modeling. A key
novelty is the self-adaptive masking strategy during
training, which combines a teacher attention map with
a student reconstruction loss into a unified Adaptive
Learning Priority (ALP) score, directing the masking
toward the most clinically informative regions. Pre-
training was conducted on 308,584 images from 38
publicly available ultrasound datasets covering 12 or-
gans. Evaluation was performed via fine-tuning a task
head (keeping the encoder frozen) for two downstream
classification datasets (BUSI breast cancer and Fetal
Planes) and two segmentation datasets (BUS-BRA
breast lesions and TN3K thyroid nodules). We evalu-
ate the VMamba encoder, which contributes49.4 M
parameters, making it the smallest backbone in the
benchmark after TinyUSFM.
A.7. UltraFedFM
UltraFedFM (Jiang et al., 2025) was first released as
a preprint in November 2024. The main contribu-
tion is a federated pretraining framework, where 16
geographically distinct clients each pretrain a local
model (masked autoencoder) on their private ultra-
sound data, and only model parameters are shared
for aggregation. To handle cross-site image differ-
ences, the framework introduces structured masking
with adaptive thresholding (SMAT), which adjusts
masking patterns to organ- and lesion-specific texture
features, and a multi-scale image corruption (MIC)
branch for improving robustness to low-quality ultra-
sound inputs. The pretraining dataset has 1,015,754
unlabeled images covering 19 organs. Evaluation was
15

UltraBench 2
performed via full fine-tuning of the encoder for dis-
ease diagnosis tasks across 8 kinds of organs and 6
modalities and lesion segmentation across 5 datasets.
This paper also conducts a clinical comparison on
8 systemic malignant diseases, demonstrating that
UltraFedFM outperforms mid-level sonographers(4–8
years of experience) and matches expert-level sonog-
raphers (>10 years of experience). We evaluate the
ViT-B encoder, which contributes85.8 Mparameters.
A.8. Deblurring MIM
DeblurringMIM (Kang et al., 2024) was one of the
first applications of masked image modeling to ultra-
sound, the work is motivated by standard masked
autoencoder pretraining failing to account for ultra-
sound’s low signal-to-noise ratio and the importance
of fine-grained diagnostic details. DeblurringMIM ex-
tends the MAE objective by adding a blurring step,
where inputs are first blurred using one of several
blur operators before random masking. Then, the
model is trained to reconstruct the original sharp im-
age from the masked and blurred input. The encoder
is a multi-scale hybrid convolution-transformer based
on ConvMAE. Pretraining was conducted on approx-
imately 280,000 thyroid ultrasound images. Down-
stream evaluation is performed with full fine-tuning
on tasks spanning classification of thyroid nodules
and Hashimoto’s thyroiditis, and segmentation of thy-
roid nodules. We evaluate both released variants: the
ViT-B encoder contributes85.8 Mparameters and the
hybrid ConvMAE encoder88.9 M.
A.9. SAMUS
SAMUS (Lin et al., 2024) adapts SAM for ultrasound
segmentation by introducing a parallel CNN branch
alongside SAM’s ViT encoder, injecting local feature
information via cross-branch attention, and further in-
corporating a position adapter and feature adapter to
retunethe model fromlarge-scalenatural imageinputs
(1024×1024) to more practical input sizes (256×256).
The model was trained and evaluated on a compre-
hensive ultrasound dataset of approximately 30,000
images and 69,000 masks covering six anatomical ob-
ject categories from publicly available sources. Down-
stream evaluation was conducted in a full fine-tuning
paradigm. Tasks were focused exclusively on interac-
tive and automatic segmentation across the six ultra-
sound object categories in the US30K dataset. We
evaluate the full adapted encoder, which contributes
129.3 Mparameters.
A.10. UltraSAM
UltraSam (Meyer et al., 2025) was first released as a
preprint in November 2024. The framework fully fine-
tunes the Segment Anything Model on a large ultra-
sound dataset under a prompt-conditioned segmenta-
tion setup, supporting both point- and bounding-box
prompts. Pretraining data consisted of US-43d, a com-
pilation of 43 open-access ultrasound segmentation
datasetstotalingover280,000image–maskpairsacross
20 diverse clinical applications. Evaluation employed
two protocols: prompt-based zero-shot segmentation
benchmarked on three diverse public datasets, and
downstream fine-tuning of an UltraSam-initialized Vi-
sion Transformer. Downstream tasks spanned both
interactive segmentation of anatomical structures and
image-level classification. We evaluate the fine-tuned
SAM ViT encoder, which contributes85.9 Mparame-
ters.
A.11. DINOv3
DINOv3 (Siméoni et al., 2025) extends DINOv2’s self-
supervised student-teacher distillation approach to sig-
nificantly larger model scales. A main contribution is
Gram anchoring, a training technique that regularizes
cosine similarity between student and teacher patch
features using a Gram-matrix objective, reducing the
degradation of dense feature maps that emerges in
larger models trained for long schedules. The initial
7B model is distilled into a family of smaller variants
(ViT-Small, ViT-Base, ViT-Large, and ConvNeXt-
based architectures). Pretraining is conducted on
a curated set of 1.689 billion images collected from
public posts on Instagram (LVD-1689M). DINOv3 is
included in our evaluation as a strong general-purpose
vision foundation model baseline, assessed via the
standard probing and fine-tuning protocol used for
the other models. We evaluate four distilled variants:
ViT-B/16 and ViT-L/16, with86 Mand300 Mpa-
rameters, and ConvNeXt-Base and ConvNeXt-Large,
with89 Mand198 Mparameters.
Appendix B. Dataset Details
Here we detail the origin, licensing, and processing of
every dataset in UltraBench 2.0. Dataset-level details
are reported in Table 2.
16

UltraBench 2
B.1. Common Processing Pipeline
All datasets are converted to a single Hugging Face
DatasetDict format so that the training and evalua-
tion layers are dataset-agnostic. The following steps
are applied uniformly.
Splits.Every dataset is published with a train
split and atest split. Whenever patient identifiers
are present, splitting is performed at the patient level
so that there is no patient-level leakage between devel-
opment and evaluation. In our experiments, we used
a validation set for hyperparameter tuning and early
stopping that was an 80:20 split oftrain, grouped by
patient wherever patient identifiers are available and
stratified by the task label where the class distribution
is otherwise unstable. Thetest split is never touched
during model selection.
B.2. Dataset Summary
Table 3 summarizes the licensing and access terms
for each dataset. The paragraphs below describe each
dataset.
AUL.The Annotated Ultrasound Liver dataset (Xu
et al., 2023) comprises 735 liver ultrasound images
with liver and mass segmentation masks and a three-
class mass label (normal, benign, malignant). We
apply a label-stratified 80:20 split. One correction
is noted - image 374.jpg has no liver mask and is
therefore excluded from the liver segmentation task,
giving that task one fewer training frame (587) than
the mass tasks (588). Both segmentation masks and
the mass label were produced by two radiologists with
more than ten years of experience, one annotating
and the other verifying, with disagreements resolved
by consensus. Malignancy is established by biopsy
or post-surgical pathology where tissue was obtained,
and otherwise by contrast-enhanced imaging in pa-
tients with hepatitis B- or C-related cirrhosis or a
known primary cancer elsewhere, so the label is not
uniformly pathology-confirmed.
BUS-BRA.BUS-BRA (Gómez-Flores et al., 2024)
contains 1,875 breast ultrasound images from 1,064
patients with biopsy-proven tumor labels, BI-RADS
categorization, and tumor segmentation masks. The
split is performed by patient. The dataset supports
three tasks: tumor segmentation, binary pathology
classification, and nine-class histology classification.
The benign and malignant labels and the histopatho-
logical types are biopsy-proven. A senior ultrasonogra-
pher manually determined lesion outlines and assigned
the BI-RADS categories.
CAMUS.CAMUS (Leclerc et al., 2019) is a two-
dimensional echocardiography dataset of 500 patients
with expert-derived cardiac structure annotations and
sequence-level image-quality ratings. We use the origi-
nal train/validation/test split and extract frames and
masksfromthereleasedsequences. Thedatasetispub-
lished as two subsets. Image quality is a sequence-level
label and the training split contains 900 sequences,
so the classification subset retains all frames. The
segmentation subset is capped at 1,000 frames drawn
uniformly at random within each (patient, view) se-
quence, which promotes coverage of every training
patient and both views. Contours for all 500 patients
were traced by a single expert cardiologist, who also
assigned the image-quality grade.
COVID-BLUES.COVID-BLUES (Wiedemann
et al., 2025) is a lung ultrasound dataset in which
each patient is imaged at standardized BLUE-protocol
positions. We split the dataset by patient, assigning
43 patients to training and 20 to test. The 63 patients
contribute a total of 362 videos containing 31,746
frames. The label is the patient’s RT-PCR test result
rather than an image-level annotation; the label ap-
plies to every frame acquired from that patient, which
is why the task is scored per patient.
Fetal Planes.The Fetal Planes dataset (Burgos-
Artizzu et al., 2020) contains 12,400 maternal-fetal
ultrasound images from 1,792 patients labeled by
anatomical plane. We preserve the original train/test
split and derive two subsets:fetal, labeled by fetal
plane (six classes: abdomen, brain, femur, thorax,
maternal cervix, and other), and fetal_brain, re-
stricted to brain images and labeled by brain plane
(four classes: trans-thalamic, trans-cerebellum, trans-
ventricular, and other). Each subset is capped inde-
pendently at 1,000 training images by moving whole
patients into the corresponding test split. A patient
may therefore appear in the training split of one sub-
set and the test split of the other, so the two subsets
should not be pooled to avoid patient-level leakage.
All images were classified manually by a single senior
maternal-fetal specialist, who also assigned the brain
sub-plane labels.
GBCU.The Gallbladder Cancer Ultrasound
dataset (Basu et al., 2022) provides gallbladder ultra-
sound images with three-class labels of normal, benign
and malignant. We use the predefined split and cap
17

UltraBench 2
Table 3: Origin and licensing of the UltraBench 2.0 datasets. “Access” indicates whether the prepared version
is distributed directly through our Hugging Face organization, or must instead be obtained from
the original provider and then integrated with the UltraBench processing scripts. Task-level frame
counts are reported in Table 2
Dataset Access License
AUL (Xu et al., 2023) Hugging Face CC BY 4.0
BUS-BRA (Gómez-Flores et al., 2024) Hugging Face CC BY 4.0
CAMUS (Leclerc et al., 2019) Hugging Face CC BY-NC-SA 4.0
COVID-BLUES (Wiedemann et al., 2025) Hugging Face CC BY-NC-ND 4.0
Fetal Planes (Burgos-Artizzu et al., 2020) Hugging Face CC BY 4.0
GBCU (Basu et al., 2022) Original provider a Research use
MASLD (Byra et al., 2018) Hugging Face CC BY 4.0
MMOTU-2D (Zhao et al., 2023) Hugging Face CC BY-NC-ND 4.0
Open Kidney (Singla et al., 2023) Original provider b Research use
PSFHS (Chen et al., 2024) Hugging Face CC BY 4.0
STMUS (Marzola et al., 2021) Hugging Face CC BY 4.0
TN3K (Gong et al., 2023) Hugging Face MIT
a Managed through a research usage agreement that prohibits redistribution. Request
access at https://gbc-iitd.github.io/data/gbcu.
b Managed through a research usage agreement that prohibits redistribution. Request
access at https://rsingla.ca/kidneyUS/.
the training split at 1,000 images by removing frames
from the majority classes first. Patient identifiers
are not publicly available, so surplus frames are dis-
carded rather than moved to the test split, to avoid
unintentionally introducing patient-level leakage. The
three-class labels are biopsy-proven.
MASLD.The MASLD dataset (Byra et al., 2018)
comprises 550 liver ultrasound images from 55 pa-
tients with a binary label indicating a diagnosis with
Metabolic dysfunction-associated steatotic liver dis-
ease (MASLD), formerly known as nonalcoholic fatty
liver disease (NAFLD). An 80:20 split is performed at
the patient-level to establish train and test splits. The
level of steatosis was graded from a wedge liver biopsy
by a single pathologist, and a patient is counted as
positive when more than 5% of hepatocytes show fatty
infiltration. Every frame from a patient inherits the
assigned label.
MMOTU-2D.MMOTU-2D (Zhao et al., 2023)
contains 1,469 ovarian tumor ultrasound images with
eight-class tumor-type labels and binary tumor seg-
mentation masks. The eight tumor types, chocolate
cyst, serous cystadenoma, teratoma, theca cell tumor,
simple cyst, normal ovary, mucinous cystadenoma,
and high-grade serous cystadenocarcinoma, are deter-
mined through histopathological analysis. The dataset
is distributed according to the original train and test
splits.
Open Kidney.The Open Kidney dataset (Singla
et al., 2023) provides 514 kidney ultrasound images
with capsule and multi-region annotations (back-
ground, central echo complex, medulla, and cortex).
We apply an 80:20 split stratified by view label (lon-
gitudinal, transverse, other). Each image corresponds
to a distinct patient, so patient overlap is not a con-
cern during splitting. Each image was annotated
independently by two registered sonographers, each
with at least 30 years of experience, following a proto-
col agreed in advance, and two biomedical engineers
reviewed every annotation. The two annotation sets
were released separately rather than fused, and we
use those of the first sonographer throughout.
PSFHS.PSFHS (Chen et al., 2024) contains 1,358
intrapartum ultrasound images from 1,124 patients
annotated for pubic symphysis and fetal head seg-
mentation. We assign 1,000 images to the training
split and the remainder to test. Other than the to-
tal number of patients, the original dataset did not
provide patient metadata, so it is not possible to guar-
antee the absence of patient overlap between the splits.
Masks were produced by a team of 2 physicians and
18 biomedical students, all trained beforehand, with
each image annotated by two annotators and disputed
pixels reviewed and corrected by a physician with a
decade of experience.
18

UltraBench 2
STMUS.The transverse musculoskeletal ultra-
sound dataset (Marzola et al., 2021) consists of 8,169
images, with segmentation masks for three different
muscles, the tibialis anterior, gastrocnemius medialis,
and biceps brachii. The original data release included
a patient characteristics metadata file that allowed
us to match images to corresponding patients. The
dataset is then split 80:20 by patient and the train-
ing split is capped at 1,000 frames by moving whole
patients into the test split. The masks are manual
segmentations by a neurodiagnostic technician, with
5-10+ years of experience in quantitative muscle imag-
ing.
TN3K.TN3K (Gong et al., 2023) provides thyroid
ultrasound images with nodule segmentation masks
and binary malignancy labels. The dataset is divided
according to the original train and test splits of 2,879
training and 614 test images. We preserve the split
and cap the training set at 1,000 images, removing
frames from the majority classes first so that the rarer
labeled nodules are retained. The surplus frames
are discarded because the images do not have any
patient identifiers. The nodule masks and the benign
and malignant labels are attributed to experienced
radiologists.
B.3. Licensing and Access
The benchmark redistributes prepared versions of
these datasets only where the original license allows
it. Two datasets, GBCU and Open Kidney, are gov-
erned by research usage agreements and cannot be
freely redistributed. The COVID-BLUES and CA-
MUS datasets have licenses that restrict commercial
use. For every dataset, we ship download and process-
ing scripts that reconstruct the benchmark version
from the original source, so the full benchmark re-
mains reproducible by any user who obtains access
through the original terms. Users of UltraBench 2 are
asked to cite the original dataset publications listed
in Table 3 alongside this work.
B.4. Standardizing anatomical region counts
Prior benchmarks report anatomical region counts us-
ing inconsistent conventions. Some treat every named
sub-structure as a distinct region, while others report
an aggregate count that includes pathological targets
as well as the corresponding organs. To enable a fair
comparison in Table 1, we did not use each paper’s
self-reported count. Instead, we manually reviewed
the dataset-level descriptions in each benchmark and
labeled every dataset using a fixed set of anatomical
regions (e.g., breast, liver, kidney, heart, thyroid),
grouping closely related structures under a single la-
bel (e.g., carotid artery and general cardiac imaging
were both grouped undercardiovascularand multiple
muscle-specific datasets were grouped undermuscle).
Datasetsthatdidnotspecifyindividualorgans, orthat
spanned several adjacent anatomies under one label
(e.g., a general abdominal ultrasound dataset without
organ-level information), were assigned to a broader
abdomencategory rather than being split arbitrar-
ily. Under these universal definitions, we counted the
number of unique labels present in each benchmark
to standardize this tally across papers.
Appendix C. Training Setup
Table 4: Optimization hyperparameters. Shared
across both fine-tuning protocols unless
noted.
Parameter Value
Optimizer AdamW
Head LR1e−3
Weight decay1e−2
Schedule CosineAnnealingLR(η min = 0)
Max steps10 000
Batch size 32
Grad. accumulation 1
Max grad. norm 1.0
Val check interval 100 steps
Patience 10 checks
Head-only training.The backbone frozen and set
to evaluation mode normalization statistics and any
stochastic components (dropout, etc.) never update.
No augmentation is applied; with the backbone fixed,
augmentation would only add label noise to the head’s
training signal.
Full fine-tuning.For the first 1,000 steps, train-
ing is identical to head-only training, linear probing,
except augmentation is active from step 0. At step
1,000 the backbone is unfrozen (except for batch nor-
malization layers, where applicable) and trainable and
its parameters are partitioned intoG = 4contiguous
groups by parameter registration order (shallowest to
deepest). This purely order-based grouping requires
19

UltraBench 2
Normal Benign
Malignant
0
100
200
300
Images
AUL Mass
Split
Train
T est
Fibroadenoma
IDCCyst
Fibrocystic
ILC
Papilloma
Sclerosing aden.
Hyperplasia
Other
0
100
200
300
400
BUS-BRA Hist.
Benign
Malignant
0
200
400
600
BUS-BRA Path.
Negative Positive
0
2000
4000
6000
8000
10000
COVID-BLUES
Normal Benign
Malignant
0
100
200
300
400
Images
GBCU
Negative Positive
0
50
100
150
200
250
300
MASLD
Chocolate cyst
Serous cyst.
T eratoma
Theca cell tumour
Simple cystNormal ovaryMucinous cyst.
High grade serous
0
50
100
150
200
MMOTU
Benign
Malignant
0
100
200
300
400
500
TN3K
Poor
Medium
Good
0
2000
4000
6000
8000
Images
CAMUS
Thalamic
CerebellumVentricular
Other
0
200
400
600
800
1000
Fetal Brain
Abdomen
BrainFemurThoraxCervixOther
0
1000
2000
3000
4000
Fetal Plane
Figure 2: The class distributions for the training and test splits for each classification task.
20

UltraBench 2
AUL Mass
Mass
BUS-BRA
Tumour
MMOTU
Tumour
TN3K
Nodule
AUL Liver
Liver
CAMUS
LV endocardium
LV myocardium
LA
OK Capsule
Capsule
OK Regions
Central echo cx.
Medulla
Cortex
PSFHS
Pubic symphysis
Fetal head
STMUS
Muscle
Figure 3: Examples of the images and segmentation masks for each segmentation task.
no architecture-specific layer naming, so it applies uni-
formly to all ViT, ConvNeXT, and CNN backbones
alike. We use layer-wise learning rate decay to adjust
the learning rate for each group:
lrbackbone(j, t) = lrhead(t)×r max ×d (G−1−j) ×w(t)
where j = 0is the shallowest group, j = G− 1the
deepest; rmax = 0.01caps the deepest group’s rate
relative to the head’s current rate;d = 0.9discounts
each successively shallower group by an additional
factor ofd; and
w(t) = clip
 t−t unfreeze
backbone_warmup_steps,0,1

linearly ramps from 0 to 1 over the 1,000 steps
immediately after unfreezing. Because the backbone
rate is always a fixed proportion of the head’s own
decaying rate, it decays in lockstep with the head’s
cosine schedule for the rest of training rather than
following an independent trajectory.
Appendix D. Performance Trends
This appendix relates overall performance to two fac-
tors: when a model was released, and how large it is.
Figures 4 and 5 plot each model’s mean score across
all segmentation and all classification tasks against
its release date, with the dashed line tracing the best
result available at each point in time. Figure 6 places
classification against segmentation performance with
point size representing trainable parameter count, and
shows that parameter count on its own does not lead
to better models
Appendix E. Per-Task Results
Figures 7, 8, 9, and 10 give the per-task breakdown for
both head-only and full fine-tuning training. Model
names in bold are those whose pre-training corpus
do not contain the task’s dataset (see Appendix H
for more information on overlap between pre-training
corpora and UltraBench 2 evaluation datasets).
21

UltraBench 2
2023-07 2023-10 2024-01 2024-04 2024-07 2024-10 2025-01 2025-04 2025-07 2025-10
Release Date
0.56
0.58
0.60
0.62
0.64
0.66
0.68
Mean F1 Score
Deblurring ConvMAE
Deblurring MAE
DINOv3 ConvNeXt-B
DINOv3 ConvNeXt-L
DINOv3 ViT-B
DINOv3 ViT-L
EchoCare
OpenUS
SAMUS
TinyUSFM
UltraFedFM
UltraSAM
URFM-B
URFM-L
USFM
USF-MAE
Figure 4: Mean F1 score over all classification tasks for each model. The dashed line shows the evolution of
the best model over time.
2023-07 2023-10 2024-01 2024-04 2024-07 2024-10 2025-01 2025-04 2025-07 2025-10
Release Date
0.76
0.77
0.78
0.79
0.80
0.81
Mean Positive Dice Score
Deblurring ConvMAE
Deblurring MAE
DINOv3 ConvNeXt-B
DINOv3 ConvNeXt-L
DINOv3 ViT-B
DINOv3 ViT-L
EchoCare
OpenUS
SAMUS
TinyUSFM
UltraFedFM
UltraSAM
URFM-B
URFM-L
USFM
USF-MAE
Figure 5: Mean positive Dice score over all segmentation tasks for each model. The dashed line shows the
evolution of the best model over time.
22

UltraBench 2
0.56 0.58 0.60 0.62 0.64 0.66 0.68
Mean F1 Score
0.76
0.77
0.78
0.79
0.80
0.81
Mean Positive Dice Score
Deblurring ConvMAE
Deblurring MAE
DINOv3 ConvNeXt-B
DINOv3 ConvNeXt-L
DINOv3 ViT-B
DINOv3 ViT-L
EchoCare
OpenUS
SAMUS
TinyUSFM
UltraFedFM
UltraSAM
URFM-B URFM-L
USFM
USF-MAE
50.0M
100.0M
150.0M
200.0M
250.0M
300.0M
Figure 6: Overall classification and segmentation performance per model. The size of each point represents
the number of trainable parameters.
Appendix F. Results Tables
This appendix reports the numbers behind the figures
in Appendix E, giving the mean and standard error
with the best result per task in bold. Tables 5 and 6
report the macro F1 score on each classification task
under full fine-tuning and head-only training respec-
tively, and Tables 7 and 8 report the positive Dice
score on each segmentation task under the same two
protocols. We include these for full transparency.
Appendix G. Head Architectures
This appendix specifies the task heads attached to
each backbone. All heads are randomly initialized,
and are the only trainable parameters under head-only
training.
PUP decoder.Patch tokens are first reshaped from
[B, N, d]to a 2D grid[ B, d,
√
N ,
√
N ], while spatial
maps[ B, C, H, W]are passed directly. A1 ×1con-
volution projects to 256 channels, followed by four
progressive transposed-convolution upsampling stages
(256→128→64→32→16channels, stride 2), each fol-
lowed by a residual double-convolution block with
GELU activations. A final1×1classification convo-
lution and, if necessary, bilinear interpolation to the
target resolution complete the decoder.
SegFormer decoder.Each scale’s features are lin-
early projected to 256 dimensions, bilinearly upsam-
pled to the finest scale, concatenated, and fused via a
1×1convolution with batch normalization and ReLU,
before a final bilinear upsample to the target resolu-
tion.
Per-model decoder assignments and trainable pa-
rameter counts are given in Table 10.
Appendix H. Pre-Training Dataset
Overlap
Several of the evaluated models are pre-trained on
public datasets that include the datasets we evalu-
ate on, making it possible that a model may have
encountered an evaluation image before it is even fine-
tuned on that task. Table 11 records, for every model
whose pre-training datasets are available, which Ultra-
Bench 2 datasets appear among them. We use it to
mark uncontaminated model–task pairs throughout
the results, so the readers can distinguish between
genuine transfer and prior exposure. Here, we omit
three models because their release descriptions do not
enumerate their pre-training data.
23

UltraBench 2
Table 5: The mean and standard error of the macro F1 score for each classification task after full fine-tuning.
The best result for each task is shown in bold.
Pathological Non-Pathological
AUL Mass BUS-BRA Hist. BUS-BRA Path. COVID-BLUES GBCU MASLD MMOTU TN3K CAMUS Fetal Brain Fetal Plane
Deblurring ConvMAE 0.639±0.040 0.174±0.017 0.702±0.022 0.644±0.1000.741±0.0400.756±0.149 0.452±0.026 0.692±0.020 0.680±0.055 0.534±0.020 0.835±0.006
Deblurring MAE 0.643±0.044 0.179±0.018 0.702±0.021 0.624±0.098 0.641±0.043 0.791±0.158 0.470±0.031 0.664±0.019 0.675±0.057 0.532±0.015 0.830±0.009
DINOv3 ConvNeXt-B 0.616±0.044 0.147±0.010 0.711±0.019 0.548±0.113 0.678±0.036 0.644±0.142 0.435±0.028 0.632±0.018 0.628±0.059 0.595±0.015 0.810±0.025
DINOv3 ConvNeXt-L 0.687±0.043 0.148±0.008 0.733±0.021 0.686±0.100 0.698±0.038 0.450±0.087 0.382±0.026 0.632±0.023 0.592±0.051 0.573±0.018 0.844±0.011
DINOv3 ViT-B 0.722±0.041 0.152±0.011 0.696±0.020 0.538±0.099 0.670±0.040 0.692±0.152 0.423±0.025 0.696±0.017 0.701±0.057 0.598±0.017 0.850±0.021
DINOv3 ViT-L0.724±0.0380.156±0.007 0.735±0.023 0.585±0.110 0.631±0.040 0.804±0.138 0.366±0.027 0.664±0.021 0.639±0.055 0.623±0.017 0.868±0.007
EchoCare 0.614±0.051 0.130±0.006 0.668±0.021 0.627±0.098 0.647±0.050 0.765±0.165 0.352±0.027 0.586±0.022 0.698±0.055 0.535±0.034 0.781±0.009
OpenUS 0.707±0.039 0.153±0.013 0.710±0.021 0.766±0.094 0.696±0.040 0.708±0.151 0.458±0.029 0.654±0.0190.710±0.0550.646±0.021 0.848±0.012
SAMUS 0.644±0.044 0.163±0.018 0.731±0.021 0.735±0.093 0.643±0.039 0.570±0.149 0.360±0.031 0.664±0.018 0.630±0.059 0.500±0.015 0.802±0.009
TinyUSFM 0.619±0.042 0.148±0.010 0.721±0.020 0.576±0.109 0.627±0.041 0.644±0.161 0.384±0.023 0.601±0.019 0.675±0.054 0.462±0.015 0.787±0.008
UltraFedFM 0.684±0.041 0.163±0.015 0.687±0.0210.804±0.0840.643±0.037 0.831±0.1540.514±0.0300.612±0.019 0.673±0.060 0.556±0.023 0.823±0.007
UltraSAM 0.672±0.041 0.161±0.018 0.698±0.019 0.688±0.091 0.541±0.0410.916±0.0960.407±0.025 0.585±0.020 0.639±0.062 0.581±0.018 0.817±0.009
URFM-B 0.662±0.043 0.188±0.014 0.774±0.019 0.663±0.112 0.679±0.039 0.771±0.163 0.490±0.028 0.737±0.018 0.631±0.065 0.684±0.017 0.915±0.003
URFM-L 0.719±0.0380.201±0.016 0.794±0.0180.695±0.106 0.658±0.038 0.870±0.118 0.486±0.0290.738±0.0170.653±0.0700.688±0.016 0.930±0.004
USFM 0.680±0.042 0.145±0.005 0.753±0.020 0.608±0.103 0.686±0.039 0.612±0.171 0.419±0.031 0.697±0.018 0.582±0.070 0.581±0.021 0.870±0.005
USF-MAE 0.652±0.045 0.167±0.011 0.706±0.021 0.740±0.088 0.656±0.040 0.771±0.163 0.464±0.027 0.644±0.019 0.680±0.057 0.663±0.016 0.863±0.004
Table 6: The mean and standard error of the macro F1 score for each classification task after head-only
training. The best result for each task is shown in bold.
Pathological Non-Pathological
AUL Mass BUS-BRA Hist. BUS-BRA Path. COVID-BLUES GBCU MASLD MMOTU TN3K CAMUS Fetal Brain Fetal Plane
Deblurring ConvMAE 0.622±0.043 0.140±0.010 0.696±0.020 0.619±0.097 0.616±0.045 0.771±0.163 0.392±0.026 0.618±0.020 0.645±0.070 0.460±0.018 0.755±0.011
Deblurring MAE 0.658±0.040 0.163±0.016 0.678±0.023 0.689±0.100 0.603±0.045 0.599±0.143 0.436±0.029 0.631±0.020 0.642±0.064 0.464±0.017 0.727±0.011
DINOv3 ConvNeXt-B 0.592±0.046 0.137±0.006 0.726±0.019 0.606±0.122 0.604±0.041 0.647±0.175 0.341±0.023 0.608±0.024 0.603±0.063 0.509±0.016 0.794±0.007
DINOv3 ConvNeXt-L 0.642±0.044 0.160±0.014 0.746±0.019 0.721±0.089 0.585±0.044 0.504±0.133 0.395±0.026 0.612±0.019 0.622±0.053 0.551±0.017 0.834±0.006
DINOv3 ViT-B 0.706±0.045 0.164±0.014 0.689±0.021 0.588±0.119 0.607±0.044 0.800±0.156 0.388±0.025 0.643±0.0190.684±0.0570.535±0.016 0.838±0.006
DINOv3 ViT-L0.721±0.0400.147±0.007 0.725±0.019 0.684±0.096 0.510±0.042 0.870±0.118 0.369±0.024 0.635±0.019 0.633±0.058 0.559±0.018 0.839±0.005
EchoCare 0.632±0.045 0.128±0.005 0.620±0.025 0.658±0.093 0.515±0.045 0.730±0.178 0.347±0.025 0.574±0.018 0.672±0.055 0.423±0.023 0.717±0.010
OpenUS 0.718±0.041 0.162±0.013 0.701±0.020 0.701±0.088 0.595±0.042 0.707±0.153 0.423±0.026 0.593±0.019 0.683±0.061 0.536±0.016 0.825±0.007
SAMUS 0.544±0.048 0.129±0.007 0.625±0.021 0.719±0.099 0.510±0.046 0.694±0.192 0.242±0.017 0.600±0.020 0.508±0.045 0.377±0.014 0.682±0.006
TinyUSFM 0.642±0.047 0.117±0.005 0.636±0.023 0.601±0.112 0.419±0.038 0.675±0.155 0.256±0.015 0.569±0.020 0.460±0.033 0.312±0.009 0.620±0.006
UltraFedFM 0.657±0.044 0.158±0.013 0.691±0.0210.821±0.0790.602±0.045 0.771±0.1630.459±0.0300.575±0.020 0.650±0.063 0.455±0.015 0.794±0.006
UltraSAM 0.639±0.040 0.163±0.016 0.683±0.020 0.760±0.083 0.509±0.0411.000±0.0000.368±0.022 0.564±0.020 0.653±0.066 0.494±0.015 0.778±0.007
URFM-B 0.672±0.044 0.164±0.015 0.748±0.020 0.672±0.113 0.561±0.043 0.771±0.163 0.427±0.029 0.652±0.019 0.622±0.073 0.595±0.017 0.884±0.004
URFM-L 0.694±0.0400.186±0.019 0.769±0.0190.749±0.100 0.540±0.043 0.389±0.070 0.431±0.0270.653±0.0190.642±0.0660.607±0.017 0.904±0.003
USFM 0.646±0.044 0.131±0.006 0.675±0.021 0.619±0.106 0.495±0.046 0.389±0.070 0.302±0.015 0.574±0.020 0.567±0.052 0.418±0.016 0.757±0.006
USF-MAE 0.655±0.044 0.151±0.009 0.703±0.022 0.766±0.0900.667±0.0420.675±0.156 0.397±0.024 0.604±0.019 0.659±0.067 0.580±0.017 0.836±0.005
Table 7: The mean and standard error of the positive Dice score for each segmentation task after full
fine-tuning. The best result for each task is shown in bold.
Pathological Anatomical
AUL Mass BUS-BRA MMOTU TN3K AUL Liver CAMUS OK Capsule OK Regions PSFHS STMUS
Deblurring ConvMAE 0.573±0.029 0.869±0.006 0.789±0.012 0.804±0.008 0.900±0.006 0.893±0.004 0.821±0.024 0.439±0.024 0.941±0.002 0.874±0.003
Deblurring MAE 0.547±0.029 0.865±0.006 0.783±0.011 0.792±0.008 0.894±0.007 0.892±0.004 0.820±0.024 0.439±0.024 0.941±0.002 0.877±0.003
DINOv3 ConvNeXt-B 0.609±0.029 0.885±0.004 0.823±0.010 0.804±0.008 0.908±0.005 0.891±0.003 0.829±0.0250.487±0.0270.938±0.002 0.871±0.003
DINOv3 ConvNeXt-L0.642±0.028 0.890±0.005 0.832±0.0090.811±0.0080.914±0.0050.890±0.003 0.825±0.029 0.485±0.025 0.940±0.002 0.874±0.003
DINOv3 ViT-B 0.584±0.030 0.872±0.005 0.820±0.010 0.798±0.008 0.906±0.006 0.889±0.003 0.829±0.027 0.430±0.030 0.936±0.002 0.879±0.003
DINOv3 ViT-L 0.603±0.029 0.882±0.004 0.827±0.009 0.784±0.009 0.912±0.005 0.890±0.003 0.822±0.026 0.457±0.025 0.935±0.002 0.876±0.003
EchoCare 0.489±0.027 0.844±0.007 0.776±0.012 0.739±0.010 0.894±0.007 0.889±0.004 0.795±0.029 0.418±0.024 0.938±0.002 0.870±0.003
OpenUS 0.565±0.029 0.880±0.005 0.820±0.009 0.787±0.008 0.913±0.005 0.901±0.003 0.840±0.023 0.457±0.024 0.942±0.002 0.880±0.003
SAMUS 0.603±0.030 0.886±0.005 0.807±0.011 0.808±0.008 0.908±0.0060.906±0.003 0.853±0.0220.467±0.0260.943±0.0020.877±0.003
TinyUSFM 0.448±0.031 0.844±0.007 0.747±0.012 0.721±0.010 0.878±0.007 0.885±0.004 0.806±0.024 0.432±0.025 0.937±0.002 0.867±0.004
UltraFedFM 0.519±0.029 0.837±0.008 0.769±0.011 0.734±0.010 0.889±0.007 0.890±0.005 0.802±0.025 0.447±0.025 0.938±0.002 0.873±0.003
UltraSAM 0.532±0.031 0.860±0.006 0.758±0.013 0.747±0.010 0.890±0.006 0.892±0.003 0.804±0.025 0.450±0.024 0.941±0.002 0.876±0.003
URFM-B 0.601±0.031 0.884±0.005 0.788±0.010 0.809±0.008 0.909±0.005 0.893±0.004 0.832±0.024 0.471±0.025 0.940±0.002 0.880±0.003
URFM-L 0.627±0.028 0.887±0.005 0.796±0.0110.819±0.0070.913±0.005 0.894±0.004 0.827±0.025 0.477±0.026 0.940±0.002 0.879±0.003
USFM 0.542±0.031 0.867±0.006 0.784±0.011 0.788±0.009 0.899±0.006 0.895±0.003 0.804±0.025 0.456±0.025 0.941±0.0020.881±0.003
USF-MAE 0.515±0.031 0.839±0.007 0.774±0.011 0.742±0.009 0.901±0.006 0.898±0.003 0.813±0.024 0.450±0.025 0.941±0.002 0.876±0.003
24

UltraBench 2
DINOv3 ViT-L
DINOv3 ViT-B
URFM-L
OpenUS
DINOv3 ConvNeXt-L
UltraFedFM
USFM
UltraSAM
URFM-B
USF-MAE
SAMUS
Deblurring MAE
Deblurring ConvMAE
TinyUSFM
DINOv3 ConvNeXt-B
EchoCare
0.553
0.608
0.663
0.718
0.773
Macro F1
AUL Mass
URFM-L
URFM-B
Deblurring MAE
Deblurring ConvMAE
USF-MAE
SAMUS
UltraFedFM
UltraSAM
DINOv3 ViT-L
OpenUS
DINOv3 ViT-B
TinyUSFM
DINOv3 ConvNeXt-L
DINOv3 ConvNeXt-B
USFM
EchoCare
0.119
0.145
0.171
0.196
0.222
BUS-BRA Hist.
URFM-L
URFM-B
USFM
DINOv3 ViT-L
DINOv3 ConvNeXt-L
SAMUS
TinyUSFM
DINOv3 ConvNeXt-B
OpenUS
USF-MAE
Deblurring ConvMAE
Deblurring MAE
UltraSAM
DINOv3 ViT-B
UltraFedFM
EchoCare
0.638
0.684
0.730
0.775
0.821
BUS-BRA Path.
UltraFedFM
OpenUS
USF-MAE
SAMUS
URFM-L
UltraSAM
DINOv3 ConvNeXt-L
URFM-B
Deblurring ConvMAE
EchoCare
Deblurring MAE
USFM
DINOv3 ViT-L
TinyUSFM
DINOv3 ConvNeXt-B
DINOv3 ViT-B
0.412
0.537
0.662
0.787
0.911
COVID-BLUES
Deblurring ConvMAE
DINOv3 ConvNeXt-L
OpenUS
USFM
URFM-B
DINOv3 ConvNeXt-B
DINOv3 ViT-B
URFM-L
USF-MAE
EchoCare
SAMUS
UltraFedFM
Deblurring MAE
DINOv3 ViT-L
TinyUSFM
UltraSAM
0.486
0.563
0.640
0.718
0.795
Macro F1
GBCU
UltraSAM
URFM-L
UltraFedFM
DINOv3 ViT-L
Deblurring MAE
URFM-B
USF-MAE
EchoCare
Deblurring ConvMAE
OpenUS
DINOv3 ViT-B
DINOv3 ConvNeXt-B
TinyUSFM
USFM
SAMUS
DINOv3 ConvNeXt-L
0.330
0.509
0.687
0.866
1.044
MASLD
UltraFedFM
URFM-B
URFM-L
Deblurring MAE
USF-MAE
OpenUS
Deblurring ConvMAE
DINOv3 ConvNeXt-B
DINOv3 ViT-B
USFM
UltraSAM
TinyUSFM
DINOv3 ConvNeXt-L
DINOv3 ViT-L
SAMUS
EchoCare
0.314
0.374
0.434
0.495
0.555
MMOTU
URFM-L
URFM-B
USFM
DINOv3 ViT-B
Deblurring ConvMAE
Deblurring MAE
SAMUS
DINOv3 ViT-L
OpenUS
USF-MAE
DINOv3 ConvNeXt-B
DINOv3 ConvNeXt-L
UltraFedFM
TinyUSFM
EchoCare
UltraSAM
0.554
0.607
0.660
0.712
0.765
TN3K
OpenUS
DINOv3 ViT-B
EchoCare
USF-MAE
Deblurring ConvMAE
TinyUSFM
Deblurring MAE
UltraFedFM
URFM-L
DINOv3 ViT-L
UltraSAM
URFM-B
SAMUS
DINOv3 ConvNeXt-B
DINOv3 ConvNeXt-L
USFM
0.500
0.569
0.639
0.708
0.778
Macro F1
CAMUS
URFM-L
URFM-B
USF-MAE
OpenUS
DINOv3 ViT-L
DINOv3 ViT-B
DINOv3 ConvNeXt-B
USFM
UltraSAM
DINOv3 ConvNeXt-L
UltraFedFM
EchoCare
Deblurring ConvMAE
Deblurring MAE
SAMUS
TinyUSFM
0.434
0.505
0.576
0.647
0.717
Fetal Brain
URFM-L
URFM-B
USFM
DINOv3 ViT-L
USF-MAE
DINOv3 ViT-B
OpenUS
DINOv3 ConvNeXt-L
Deblurring ConvMAE
Deblurring MAE
UltraFedFM
UltraSAM
DINOv3 ConvNeXt-B
SAMUS
TinyUSFM
EchoCare
0.764
0.809
0.853
0.898
0.942
Fetal Plane
Figure 7: Full fine-tuning results on each classification task.Boldindicates that the task dataset was not
included in the model’s pretraining data.
25

UltraBench 2
DINOv3 ViT-L
OpenUS
DINOv3 ViT-B
URFM-L
URFM-B
Deblurring MAE
UltraFedFM
USF-MAE
USFM
TinyUSFM
DINOv3 ConvNeXt-L
UltraSAM
EchoCare
Deblurring ConvMAE
DINOv3 ConvNeXt-B
SAMUS
0.482
0.555
0.628
0.701
0.775
Macro F1
AUL Mass
URFM-L
URFM-B
DINOv3 ViT-B
UltraSAM
Deblurring MAE
OpenUS
DINOv3 ConvNeXt-L
UltraFedFM
USF-MAE
DINOv3 ViT-L
Deblurring ConvMAE
DINOv3 ConvNeXt-B
USFM
SAMUS
EchoCare
TinyUSFM
0.107
0.132
0.158
0.184
0.210
BUS-BRA Hist.
URFM-L
URFM-B
DINOv3 ConvNeXt-L
DINOv3 ConvNeXt-B
DINOv3 ViT-L
USF-MAE
OpenUS
Deblurring ConvMAE
UltraFedFM
DINOv3 ViT-B
UltraSAM
Deblurring MAE
USFM
TinyUSFM
SAMUS
EchoCare
0.585
0.638
0.691
0.744
0.797
BUS-BRA Path.
UltraFedFM
USF-MAE
UltraSAM
URFM-L
DINOv3 ConvNeXt-L
SAMUS
OpenUS
Deblurring MAE
DINOv3 ViT-L
URFM-B
EchoCare
USFM
Deblurring ConvMAE
DINOv3 ConvNeXt-B
TinyUSFM
DINOv3 ViT-B
0.448
0.566
0.685
0.803
0.922
COVID-BLUES
USF-MAE
Deblurring ConvMAE
DINOv3 ViT-B
DINOv3 ConvNeXt-B
Deblurring MAE
UltraFedFM
OpenUS
DINOv3 ConvNeXt-L
URFM-B
URFM-L
EchoCare
DINOv3 ViT-L
SAMUS
UltraSAM
USFM
TinyUSFM
0.365
0.455
0.545
0.635
0.725
Macro F1
GBCU
UltraSAM
DINOv3 ViT-L
DINOv3 ViT-B
Deblurring ConvMAE
UltraFedFM
URFM-B
EchoCare
OpenUS
SAMUS
TinyUSFM
USF-MAE
DINOv3 ConvNeXt-B
Deblurring MAE
DINOv3 ConvNeXt-L
URFM-L
USFM
0.285
0.472
0.660
0.847
1.034
MASLD
UltraFedFM
Deblurring MAE
URFM-L
URFM-B
OpenUS
USF-MAE
DINOv3 ConvNeXt-L
Deblurring ConvMAE
DINOv3 ViT-B
DINOv3 ViT-L
UltraSAM
EchoCare
DINOv3 ConvNeXt-B
USFM
TinyUSFM
SAMUS
0.212
0.285
0.358
0.430
0.503
MMOTU
URFM-L
URFM-B
DINOv3 ViT-B
DINOv3 ViT-L
Deblurring MAE
Deblurring ConvMAE
DINOv3 ConvNeXt-L
DINOv3 ConvNeXt-B
USF-MAE
SAMUS
OpenUS
UltraFedFM
USFM
EchoCare
TinyUSFM
UltraSAM
0.537
0.573
0.608
0.643
0.679
TN3K
DINOv3 ViT-B
OpenUS
EchoCare
USF-MAE
UltraSAM
UltraFedFM
Deblurring ConvMAE
URFM-L
Deblurring MAE
DINOv3 ViT-L
DINOv3 ConvNeXt-L
URFM-B
DINOv3 ConvNeXt-B
USFM
SAMUS
TinyUSFM
0.411
0.498
0.585
0.672
0.759
Macro F1
CAMUS
URFM-L
URFM-B
USF-MAE
DINOv3 ViT-L
DINOv3 ConvNeXt-L
OpenUS
DINOv3 ViT-B
DINOv3 ConvNeXt-B
UltraSAM
Deblurring MAE
Deblurring ConvMAE
UltraFedFM
EchoCare
USFM
SAMUS
TinyUSFM
0.287
0.375
0.463
0.552
0.640
Fetal Brain
URFM-L
URFM-B
DINOv3 ViT-L
DINOv3 ViT-B
USF-MAE
DINOv3 ConvNeXt-L
OpenUS
DINOv3 ConvNeXt-B
UltraFedFM
UltraSAM
USFM
Deblurring ConvMAE
Deblurring MAE
EchoCare
SAMUS
TinyUSFM
0.600
0.680
0.761
0.841
0.922
Fetal Plane
Figure 8: Linear probing results on each classification task.Boldindicates that the task dataset was not
included in the model’s pretraining data.
26

UltraBench 2
DINOv3 ConvNeXt-L
URFM-L
DINOv3 ConvNeXt-B
DINOv3 ViT-L
SAMUS
URFM-B
DINOv3 ViT-B
Deblurring ConvMAE
OpenUS
Deblurring MAE
USFM
UltraSAM
UltraFedFM
USF-MAE
EchoCare
TinyUSFM
0.404
0.474
0.543
0.613
0.683
Positive Dice
AUL Mass
DINOv3 ConvNeXt-L
URFM-L
SAMUS
DINOv3 ConvNeXt-B
URFM-B
DINOv3 ViT-L
OpenUS
DINOv3 ViT-B
Deblurring ConvMAE
USFM
Deblurring MAE
UltraSAM
EchoCare
TinyUSFM
USF-MAE
UltraFedFM
0.826
0.844
0.862
0.880
0.898
BUS-BRA
DINOv3 ConvNeXt-L
DINOv3 ViT-L
DINOv3 ConvNeXt-B
OpenUS
DINOv3 ViT-B
SAMUS
URFM-L
Deblurring ConvMAE
URFM-B
USFM
Deblurring MAE
EchoCare
USF-MAE
UltraFedFM
UltraSAM
TinyUSFM
0.730
0.759
0.788
0.817
0.846
MMOTU
URFM-L
DINOv3 ConvNeXt-L
URFM-B
SAMUS
Deblurring ConvMAE
DINOv3 ConvNeXt-B
DINOv3 ViT-B
Deblurring MAE
USFM
OpenUS
DINOv3 ViT-L
UltraSAM
USF-MAE
EchoCare
UltraFedFM
TinyUSFM
0.706
0.737
0.769
0.800
0.832
TN3K
DINOv3 ConvNeXt-L
URFM-L
OpenUS
DINOv3 ViT-L
URFM-B
DINOv3 ConvNeXt-B
SAMUS
DINOv3 ViT-B
USF-MAE
Deblurring ConvMAE
USFM
Deblurring MAE
EchoCare
UltraSAM
UltraFedFM
TinyUSFM
0.869
0.882
0.895
0.909
0.922
Positive Dice
AUL Liver
SAMUS
OpenUS
USF-MAE
USFM
URFM-L
URFM-B
Deblurring ConvMAE
UltraSAM
Deblurring MAE
DINOv3 ConvNeXt-B
UltraFedFM
DINOv3 ConvNeXt-L
DINOv3 ViT-L
EchoCare
DINOv3 ViT-B
TinyUSFM
0.879
0.887
0.895
0.903
0.910
CAMUS
SAMUS
OpenUS
URFM-B
DINOv3 ConvNeXt-B
DINOv3 ViT-B
URFM-L
DINOv3 ConvNeXt-L
DINOv3 ViT-L
Deblurring ConvMAE
Deblurring MAE
USF-MAE
TinyUSFM
USFM
UltraSAM
UltraFedFM
EchoCare
0.761
0.791
0.821
0.851
0.881
OK Capsule
DINOv3 ConvNeXt-B
DINOv3 ConvNeXt-L
URFM-L
URFM-B
SAMUS
DINOv3 ViT-L
OpenUS
USFM
UltraSAM
USF-MAE
UltraFedFM
Deblurring MAE
Deblurring ConvMAE
TinyUSFM
DINOv3 ViT-B
EchoCare
0.388
0.421
0.453
0.486
0.519
OK Regions
SAMUS
OpenUS
Deblurring ConvMAE
USFM
USF-MAE
UltraSAM
Deblurring MAE
URFM-L
DINOv3 ConvNeXt-L
URFM-B
UltraFedFM
EchoCare
DINOv3 ConvNeXt-B
TinyUSFM
DINOv3 ViT-B
DINOv3 ViT-L
0.933
0.936
0.939
0.942
0.945
Positive Dice
PSFHS
USFM
OpenUS
URFM-B
URFM-L
DINOv3 ViT-B
SAMUS
Deblurring MAE
DINOv3 ViT-L
UltraSAM
USF-MAE
DINOv3 ConvNeXt-L
Deblurring ConvMAE
UltraFedFM
DINOv3 ConvNeXt-B
EchoCare
TinyUSFM
0.862
0.868
0.874
0.879
0.885
STMUS
Figure 9: Full fine-tuning results on each segmentation task.Boldindicates that the task dataset was not
included in the model’s pretraining data.
27

UltraBench 2
URFM-L
URFM-B
OpenUS
DINOv3 ConvNeXt-L
USF-MAE
DINOv3 ViT-B
UltraFedFM
UltraSAM
DINOv3 ViT-L
DINOv3 ConvNeXt-B
Deblurring MAE
Deblurring ConvMAE
USFM
TinyUSFM
EchoCare
SAMUS
0.303
0.364
0.425
0.487
0.548
Positive Dice
AUL Mass
URFM-L
URFM-B
OpenUS
SAMUS
UltraSAM
USFM
Deblurring ConvMAE
USF-MAE
DINOv3 ConvNeXt-L
DINOv3 ViT-B
Deblurring MAE
UltraFedFM
DINOv3 ViT-L
DINOv3 ConvNeXt-B
TinyUSFM
EchoCare
0.687
0.736
0.785
0.833
0.882
BUS-BRA
URFM-L
URFM-B
OpenUS
DINOv3 ConvNeXt-L
USF-MAE
DINOv3 ViT-L
UltraFedFM
DINOv3 ViT-B
DINOv3 ConvNeXt-B
SAMUS
Deblurring MAE
UltraSAM
Deblurring ConvMAE
USFM
TinyUSFM
EchoCare
0.683
0.710
0.737
0.763
0.790
MMOTU
URFM-L
SAMUS
URFM-B
Deblurring ConvMAE
Deblurring MAE
OpenUS
USFM
USF-MAE
DINOv3 ConvNeXt-L
UltraSAM
DINOv3 ViT-B
DINOv3 ViT-L
UltraFedFM
DINOv3 ConvNeXt-B
TinyUSFM
EchoCare
0.564
0.629
0.694
0.760
0.825
TN3K
URFM-L
URFM-B
OpenUS
USF-MAE
Deblurring ConvMAE
UltraFedFM
DINOv3 ConvNeXt-L
DINOv3 ViT-L
USFM
UltraSAM
DINOv3 ViT-B
Deblurring MAE
DINOv3 ConvNeXt-B
SAMUS
TinyUSFM
EchoCare
0.832
0.853
0.874
0.895
0.916
Positive Dice
AUL Liver
SAMUS
OpenUS
USF-MAE
UltraSAM
URFM-L
URFM-B
UltraFedFM
USFM
Deblurring MAE
DINOv3 ViT-L
DINOv3 ViT-B
TinyUSFM
Deblurring ConvMAE
EchoCare
DINOv3 ConvNeXt-L
DINOv3 ConvNeXt-B
0.841
0.858
0.876
0.894
0.911
CAMUS
URFM-B
URFM-L
OpenUS
USF-MAE
UltraSAM
DINOv3 ViT-L
USFM
DINOv3 ViT-B
DINOv3 ConvNeXt-L
Deblurring MAE
Deblurring ConvMAE
SAMUS
DINOv3 ConvNeXt-B
UltraFedFM
TinyUSFM
EchoCare
0.690
0.728
0.767
0.805
0.843
OK Capsule
URFM-L
DINOv3 ConvNeXt-L
URFM-B
OpenUS
UltraSAM
SAMUS
DINOv3 ConvNeXt-B
USFM
DINOv3 ViT-L
USF-MAE
TinyUSFM
UltraFedFM
Deblurring MAE
DINOv3 ViT-B
Deblurring ConvMAE
EchoCare
0.339
0.374
0.409
0.443
0.478
OK Regions
OpenUS
URFM-L
USF-MAE
URFM-B
UltraSAM
USFM
UltraFedFM
Deblurring MAE
Deblurring ConvMAE
TinyUSFM
EchoCare
SAMUS
DINOv3 ViT-B
DINOv3 ConvNeXt-L
DINOv3 ViT-L
DINOv3 ConvNeXt-B
0.897
0.907
0.917
0.927
0.937
Positive Dice
PSFHS
URFM-B
USF-MAE
URFM-L
OpenUS
UltraFedFM
UltraSAM
USFM
Deblurring MAE
Deblurring ConvMAE
DINOv3 ViT-L
TinyUSFM
DINOv3 ViT-B
DINOv3 ConvNeXt-L
DINOv3 ConvNeXt-B
EchoCare
SAMUS
0.832
0.843
0.854
0.865
0.877
STMUS
Figure 10: Head-only training results on each segmentation task.Boldindicates that the task dataset was
not included in the model’s pretraining data.
28

UltraBench 2
Table 8: The mean and standard error of the positive Dice score for each segmentation task after head-only
training. The best result for each task is shown in bold.
Pathological Anatomical
AUL Mass BUS-BRA MMOTU TN3K AUL Liver CAMUS OK Capsule OK Regions PSFHS STMUS
Deblurring ConvMAE 0.395±0.029 0.806±0.008 0.724±0.013 0.746±0.009 0.880±0.007 0.861±0.007 0.764±0.024 0.378±0.024 0.917±0.003 0.855±0.004
Deblurring MAE 0.406±0.027 0.801±0.009 0.731±0.012 0.744±0.010 0.869±0.008 0.873±0.005 0.766±0.025 0.391±0.024 0.922±0.002 0.857±0.005
DINOv3 ConvNeXt-B 0.407±0.028 0.788±0.008 0.734±0.010 0.667±0.010 0.863±0.007 0.850±0.006 0.761±0.025 0.418±0.024 0.902±0.003 0.844±0.003
DINOv3 ConvNeXt-L 0.449±0.026 0.803±0.007 0.756±0.010 0.693±0.009 0.876±0.007 0.857±0.006 0.766±0.025 0.444±0.025 0.909±0.003 0.849±0.004
DINOv3 ViT-B 0.432±0.030 0.803±0.007 0.740±0.011 0.690±0.010 0.870±0.009 0.868±0.005 0.769±0.025 0.389±0.024 0.909±0.003 0.850±0.003
DINOv3 ViT-L 0.418±0.029 0.790±0.007 0.747±0.012 0.688±0.011 0.872±0.007 0.871±0.005 0.777±0.024 0.408±0.022 0.902±0.003 0.852±0.003
EchoCare 0.354±0.025 0.706±0.010 0.699±0.011 0.585±0.010 0.845±0.008 0.860±0.007 0.722±0.025 0.370±0.025 0.915±0.003 0.842±0.003
OpenUS 0.490±0.028 0.827±0.007 0.769±0.010 0.731±0.009 0.902±0.005 0.896±0.003 0.793±0.025 0.439±0.0240.933±0.0020.870±0.003
SAMUS 0.339±0.026 0.827±0.007 0.731±0.012 0.792±0.009 0.860±0.0080.905±0.0030.763±0.026 0.431±0.025 0.910±0.003 0.837±0.003
TinyUSFM 0.358±0.028 0.786±0.008 0.710±0.012 0.658±0.012 0.845±0.010 0.863±0.007 0.754±0.025 0.394±0.023 0.916±0.002 0.851±0.004
UltraFedFM 0.428±0.028 0.799±0.007 0.741±0.011 0.688±0.010 0.877±0.008 0.880±0.005 0.755±0.026 0.393±0.025 0.925±0.002 0.865±0.003
UltraSAM 0.419±0.028 0.816±0.008 0.730±0.012 0.691±0.011 0.871±0.008 0.886±0.004 0.779±0.026 0.433±0.026 0.926±0.002 0.863±0.003
URFM-B 0.491±0.029 0.862±0.005 0.769±0.011 0.790±0.009 0.903±0.005 0.882±0.0050.811±0.0250.441±0.025 0.928±0.0020.872±0.003
URFM-L0.508±0.029 0.868±0.006 0.775±0.011 0.805±0.008 0.906±0.0050.885±0.004 0.804±0.0260.446±0.0260.930±0.002 0.871±0.003
USFM 0.383±0.029 0.808±0.008 0.719±0.012 0.712±0.010 0.872±0.008 0.874±0.005 0.775±0.026 0.410±0.025 0.925±0.002 0.862±0.003
USF-MAE 0.435±0.028 0.804±0.008 0.750±0.011 0.708±0.010 0.883±0.007 0.892±0.004 0.784±0.025 0.402±0.025 0.930±0.002 0.871±0.003
Table 9: The number of trainable parameters in the linear classification head added to each model backbone
for a binary classification task.
Model Feature Dimension Trainable Parameters
Deblurring ConvMAE768 1538
Deblurring MAE768 1538
DINOv3 ConvNeXt-B1024 2050
DINOv3 ConvNeXt-L1536 3074
DINOv3 ViT-B768 1538
DINOv3 ViT-L1024 2050
EchoCare2048 4098
OpenUS768 1538
SAMUS1024 2050
TinyUSFM192 386
UltraFedFM768 1538
UltraSAM768 1538
URFM-B768 1538
URFM-L1024 2050
USFM768 1538
USF-MAE768 1538
29

UltraBench 2
Table 10: The number of trainable parameters in each segmentation decoder head compatible with each
model backbone’s output type, for a binary segmentation task.
Model Output Type Head Architecture Trainable Parameters
Deblurring ConvMAE Patch Tokens PUP764,338
Deblurring MAE Patch Tokens PUP764,338
DINOv3 ConvNeXt-B Multi-Scale Feature Maps SegFormer755,714
DINOv3 ConvNeXt-L Multi-Scale Feature Maps SegFormer1,001,474
DINOv3 ViT-B Patch Tokens PUP764,338
DINOv3 ViT-L Patch Tokens PUP829,874
EchoCare Multi-Scale Feature Maps SegFormer1,345,794
OpenUS Multi-Scale Feature Maps SegFormer632,834
SAMUS Feature Maps PUP633,266
TinyUSFM Patch Tokens PUP616,882
UltraFedFM Patch Tokens PUP764,338
UltraSAM Patch Tokens PUP764,338
URFM-B Patch Tokens PUP764,338
URFM-L Patch Tokens PUP829,874
USFM Patch Tokens PUP764,338
USF-MAE Patch Tokens PUP764,338
Table 11: Overlap between model pre-training corpora and the UltraBench evaluation datasets.• = dataset
included in pre-training;◦ = not included. EchoCare, TinyUSFM, and USFM are omitted: all three
are pre-trained in part on publicly available data, but the constituent datasets are not disclosed, so
their overlap with UltraBench cannot be determined. DINOv3 does not knowningly include any
ultrasound images in the training data, but it is not auditable.
Model AUL BUS-BRACAMUSCOVID-BLUeSFetal PlanesGBCUMASLDMMOTUOpen KidneyPSFHSSTMUSTN3K
DeblurringMIM◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦
OpenUS• ◦ • ◦ ◦ ◦ ◦ • ◦ ◦ • ◦
SAMUS◦ ◦ • ◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦ •
UltraFedFM◦ ◦ • ◦ • ◦ ◦ ◦ ◦ ◦ ◦ ◦
UltraSAM• ◦ • ◦ ◦ ◦ ◦ ◦ • • • •
URFM◦ ◦ • ◦ • ◦ ◦ ◦ ◦ ◦ ◦ ◦
USF-MAE• ◦ • • • ◦ ◦ ◦ • • • •
30
