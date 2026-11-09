---
title: 'SAGE: Subpopulation-Aware Generative Enhancement for Mitigating Spurious Correlations'
url: https://arxiv.org/abs/2609.01051
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Yiming Luo
- Rongqiang Zhao
- Jie Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.01051
pages: 14
chars: 54390
fetched_at: '2026-11-08T13:30:13+00:00'
kb_version: 1
---

# SAGE: Subpopulation-Aware Generative Enhancement for Mitigating Spurious Correlations

SAGE: Subpopulation-Aware Generative Enhancement for
Mitigating Spurious Correlations
Yiming Luo1, Rongqiang Zhao1,2∗, Jie Liu1,2
1Harbin Institute of Technology
2State Key Laboratory of Smart Farm Technologies and Systems
zhaorq@hit.edu.cn
Abstract
Spurious correlations pose a significant challenge to the ro-
bustness of modern machine learning. The inherent imbal-
ance in dataset distributions often leads traditional Empir-
ical Risk Minimization (ERM) models to rely on majority
spurious attributes for classification, resulting in poor per-
formanceonminoritygroups.Thisproblembecomesparticu-
larlychallengingwhenthespuriousattributesareunavailable.
Existing group-label-free methods often upsample minority
groups or misclassified real training examples; repeating the
same instances can reduce effective diversity and encourage
overfitting. To mitigate these spurious correlations from a
data-centric perspective in the absence of prior knowledge,
we introduce Subpopulation-Aware Generative Enhancement
(SAGE),atwo-stagegenerativeaugmentationframework.Us-
ing cluster-derived sub-labels and class labels, we fine-tune
a conditional generative model and text encoder, generat-
ing targeted synthetic data to fill underrepresented regions
in the training set and construct a balanced validation set for
last-layer reweighting. We experimentally show that SAGE
achieves 89.5%, 85.7%, and 79.1% worst-group accuracy on
Waterbirds,CelebA,andMetaShift,respectively,outperform-
ingthebestgroup-label-freebaselinesbyupto7.7percentage
points.
Code— https://github.com/luoym-lym/SAGE
Introduction
Deep neural networks have achieved outstanding perfor-
mance in classification tasks (Krizhevsky, Sutskever, and
Hinton 2012; He et al. 2016). However, they often tend to
rely on easily accessible shortcut features rather than the
truly causal core features (Geirhos et al. 2020). For exam-
ple, in the task of classifying waterbirds and landbirds, if
the majority of waterbirds in the training set appear against
waterbackgroundswhilemostlandbirdsappearagainstland
backgrounds,themodelwillinherentlyadoptthebackground
(waterorland)asitsprimarybasisforclassification.Conse-
quently, when such spurious correlations are broken during
thetestingphase(e.g.,encounteringawaterbirdonland),the
modelsuffersacatastrophicdropintestperformance,which
isprimarilymanifestedaslowworst-groupaccuracy(WGA).
(Beery, Van Horn, and Perona 2018; Sagawa et al. 2020).
To mitigate spurious correlations, existing methods can
be broadly divided into two categories. The first category
∗Corresponding author.
assumes access to spurious group information and improves
robustness by modifying the model’s learning objective or
reweighting strategy (Sagawa et al. 2020; Kirichenko, Iz-
mailov,andWilson2023).Thesecondcategoryavoidsgroup
labels and reduces model bias using proxy signals inferred
from model behavior, input regions, or discovered concepts
(Liuetal.2021;Nametal.2020;Zhangetal.2022;Noohdani
et al. 2024; Asgari et al. 2022; Wu et al. 2023).
Recently, generative models have been increasingly ap-
plied to data augmentation across various domains (Azizi
et al. 2023; Dunlap et al. 2023; Sun et al. 2026), and a
nascent line of work has begun to explore their potential for
mitigating spurious correlations. This line of work uses im-
age generation to create additional samples under different
visual conditions, class-attribute combinations, or debiased
prompts (Qraitem, Saenko, and Plummer 2024; Ghosh et al.
2024; Basu et al. 2026; Parast, Azam, and Akhtar 2025).
Compared with reusing existing training examples, gener-
ated data can provide new visual instances and thus offers a
natural way to expand the available training set.
Taken together, these directions leave a gap in settings
where spurious attributes are unobserved and manually cu-
rated group-balanced validation sets are unavailable, which
more closely matches real-world scenarios than assuming
access to group annotations or curated validation data. Al-
thoughsomemethodsoperateunderthisstrictersetting,they
arestilllesscompetitiveinworst-groupaccuracy.Generative
approaches provide additional synthetic training examples,
but they often depend on complex external models to dis-
coverspuriousattributes(e.g.,LLMsorsegmentationtools),
require explicit group annotations to guide generation, or
still need a manually curated validation set for model se-
lection. Thus, it remains challenging to mitigate spurious
correlations when both spurious group labels and balanced
validation data are unavailable.
To overcome these limitations, we propose SAGE (Fig-
ure1),adata-centricgenerativeaugmentationframeworkfor
settings where spurious attributes and group-balanced val-
idation data are unavailable. SAGE mitigates spurious cor-
relations without relying on external spurious-attribute dis-
coverytools(e.g.,LLMsorsegmentationmodels),manually
annotated spurious groups, or curated validation sets. Our
key insight is that visually salient spurious cues often struc-
turethefeaturespaceofpretrainedvisionencoders:samples
arXiv:2609.01051v1  [cs.LG]  1 Sep 2026

Figure 1: Overview of SAGE. Stage 1. We cluster semantic features to obtain sub-label tokens, which are combined with
classlabelstofine-tuneaconditionalgenerativemodel. Stage2.Weuseinverse-densitysamplingtogeneratetargetedsynthetic
training data for underrepresented regions, and uniform sampling to construct a sub-label-balanced synthetic validation set for
last-layer reweighting.
sharingsimilarshortcutfeaturestendtoclustertogethereven
when spurious attributes are unlabeled. We therefore treat
cluster assignments as proxies for bias-relevant subpopula-
tions, rather than as ground-truth spurious groups.
SAGEinstantiatesthisideaintwostages.First,wecluster
semantic features and assign each cluster a learnable sub-
label token, which is used together with the class label to
fine-tune a conditional generative model. Second, we use
inverse-density sampling over the discovered sub-labels to
generate targeted synthetic data for underrepresented train-
ing regions. In parallel, we construct a sub-label-balanced
synthetic validation set via uniform sampling. Because true
spurious groups are unavailable, this synthetic set serves
as a practical proxy for the group-balanced validation data
required by Deep Feature Reweighting (DFR), allowing us
to retrain only the last classification layer without manual
validation-set curation.
We evaluate SAGE on three popular benchmarks: Water-
birds,CelebA,andMetaShift.SAGEachieves89.5%,85.7%,
and 79.1% worst-group accuracy on these datasets, respec-
tively, outperforming all prior methods that operate without
group labels or curated validation data in either training or
model selection. It also remains competitive with methods
thatrelyonstrongerpriorinformation,suchasgrouplabelsor
manually curated validation sets. Our ablation studies show
that targeted training-set augmentation and synthetic valida-
tion construction provide complementary benefits. Visual-
izationresultsonWaterbirdsandCelebAfurthersuggestthat
the learned sub-label tokens capture subpopulation-specific
visual factors.
Summaryofcontributions.Wesummarizeourcontribu-
tions as follows:
•We propose SAGE, a generative augmentation method
for mitigating spurious correlations in the practical set-
tingwherespuriousattributesareunobservedandgroup-
balanced validation data are unavailable.
•Wedesignasubpopulation-awaredataconstructionstrat-
egythatderivessub-labelsthroughsemanticfeatureclus-
tering and couples them with complementary label sam-
pling strategies, enabling targeted generation for under-
represented training regions and sub-label-balanced syn-
thetic validation data.
•We provide ablation and visualization analyses showing
thecomplementaryrolesoftraining-setaugmentationand
synthetic validation construction, as well as the ability
of learned sub-label tokens to capture subpopulation-
specific visual factors that often align with spurious at-
tributes.
Related Work
RobustLearningforSpuriousCorrelations.Alargebody
of work mitigates spurious correlations by modifying the
training or model-selection procedure. Some methods use
spurious group information directly: gDRO (Sagawa et al.
2020)dynamicallyupweightshigh-lossgroupsduringtrain-

ing, and DFR (Kirichenko, Izmailov, and Wilson 2023) re-
trains the last linear layer on a group-balanced validation
set. Another line of work avoids training-time group labels
and instead relies on proxy signals. JTT (Liu et al. 2021)
and LfF (Nam et al. 2020) identify hard or biased examples
from model behavior; CnC (Zhang et al. 2022) uses con-
trastive learning to improve robustness; and DaC (Noohdani
etal.2024)addressesspuriouscorrelationsthroughadecom-
positionaltrainingstrategy.Morerestrictivegroup-label-free
methodsincludeMaskTune(Asgarietal.2022),whichmasks
themostdiscriminativeregionsfoundbyatrainedmodeland
fine-tunes on the masked images to force exploration of al-
ternative cues, and DISC (Wu et al. 2023), which discovers
unstable human-interpretable concepts across environments
and intervenes on the training data to reduce their influence.
Generative Data Augmentation for Spurious Correla-
tions.Diffusion models have recently become a powerful
toolforcontrollableimagegeneration(Ho,Jain,andAbbeel
2020; Dhariwal and Nichol 2021; Rombach et al. 2022),
motivatingtheiruseassyntheticdatasourcesforrobustclas-
sification(Azizietal.2023;Dunlapetal.2023).Formitigat-
ingspuriouscorrelations,existingworkhasmainlyexplored
how to construct useful synthetic samples for downstream
classifiers. One line of work balances synthetic data before
real-data training; for example, FFR (Qraitem, Saenko, and
Plummer 2024) first pretrains on balanced synthetic images
and then fine-tunes on real data to avoid learning artifacts
from mixed real-synthetic training. Another line introduces
additional guidance to make generation more targeted: AS-
PIRE (Ghosh et al. 2024) uses LLMs and language-guided
image editing to identify spurious features from captions,
then personalizes a text-to-image model to generate non-
spurious images; DDB (Parast, Azam, and Akhtar 2025)
combines textual inversion, language-based segmentation,
diffusion generation, and ERM-based pruning to synthesize
samples that break spurious correlations. Closely related
to subpopulation-level generation, Clustered DreamBooth
(Basu et al. 2026) clusters samples within known groups
and fine-tunes DreamBooth models for each cluster to gen-
erate group-balanced data. Overall, these methods show the
promiseofgenerateddata, butdecidingwhattogenerateof-
teninvolvesadditionalmachinery,suchaslanguage-basedat-
tributediscovery,segmentation-assistedlocalization,group-
aware sampling rules, or validation-set-based model selec-
tion. In contrast, SAGE derives generation conditions from
cluster-derived sub-labels within the target dataset and uses
theresultinggeneratortosynthesizebothtrainingdataanda
balanced validation set.
Method
In this section, we detail our proposed framework follow-
ing the aforementioned two-stage sequence. The first stage
comprises clustering and conditional generator fine-tuning.
The second stage encompasses targeted data generation and
downstream model training.
Stage 1: Semantic Clustering and Conditional
Generator Fine-Tuning
AP Clustering.In the first stage of our framework, we par-
tition the training data into feature-space subgroups without
access to explicit spurious attribute labels. We first map the
trainingimagesintoalatentfeaturespaceZ={z 1, . . . , zN }
using a pre-trained encoder, and subsequently cluster them
usingAffinityPropagation(AP)(FreyandDueck2007).Un-
likestandardmethodssuchasK-Means,APdoesnotrequire
a pre-defined number of clusters; instead, it identifies repre-
sentative samples (exemplars) through an iterative message-
passing mechanism. The algorithm operates on a similarity
matrix defined by the negative squared Euclidean distance,
s(i, k) =−∥zi −z k∥2,wherethediagonalelementss(k, k)
serve as prior preferences that implicitly control the result-
ingnumberofclusters.APiterativelyexchangestwotypesof
dampedmessagesbetweendatapoints:responsibilityr(i, k),
which quantifies the suitability ofzk serving as an exemplar
forz i, andavailabilitya(i, k), which reflects the accumu-
lated evidence forzi choosingz k. Upon convergence, each
data pointz i is assigned to the exemplarkthat maximizes
the sumr(i, k) +a(i, k). We use these assignments as dis-
cretesub-labelsforgenerativeconditioning,treatingclusters
as proxies for bias-relevant subpopulations rather than as
ground-truth spurious groups; alignment with ground-truth
attributes is evaluated post hoc in Appendix C.
Fine-Tuning the Diffusion Model with LoRA.Condi-
tional diffusion models have established themselves as the
state-of-the-art paradigm for text-to-image synthesis (Ho,
Jain, and Abbeel 2020; Dhariwal and Nichol 2021), achiev-
ing unprecedented perceptual quality and semantic fidelity.
Inthiswork,weadoptStableDiffusion(SD)(Rombachetal.
2022) as our base generative backbone owing to its robust
synthesis capabilities and open-source availability.
To effectively inject the latent sub-labels (discovered in
Stage1)intothegenerativeprocessviacross-attentionmech-
anisms,thepre-trainedSDmodelmustbeadapted.Giventhe
prohibitivecomputationalcostoffull-parameterfine-tuning,
we employ Low-Rank Adaptation (LoRA) (Hu et al. 2022)
to efficiently update the UNet backbone. Specifically, prior
to training, we register a unique semantic token⟨tk⟩for
eachsub-labelkwithinthetextencoder’svocabulary.These
novel embeddings are initialized with the semantic prior of
the word‘photo’, serving as a domain-general initialization
that ensures the robustness and applicability of our method
across arbitrary datasets.
During the fine-tuning phase, we utilize a structured
prompt template to guide the learning process:
“a photo of [class labely], [sub-label token⟨tk⟩]”
Inthistemplate,the[classlabel]providestheglobalsemantic
anchor,whilethesub-labeltoken⟨t k⟩isoptimizedtocapture
the fine-grained subpopulation characteristics. These newly
addedtokenembeddingsarejointlyoptimizedalongsidethe
LoRA parameters, while the remaining weights of the text
encoder and UNet are kept frozen.
Concretely, letxbe a training image belonging to class
yand assigned to the latent clusterk. We mapxinto the
latent space using the frozen VAE encoder, denoted asz=

E(x). The structured prompt is encoded byτ—whereyis
inserted as fixed textual class names in the prompt template
and only the embedding of⟨tk⟩is learnable—to yield the
conditioning vectorc=τ(y, t k). By introducing trainable
LoRA parameters∆θinto the frozen UNet weightsθ, we
formulate the joint optimization objective as the following
latent diffusion loss:
Ljoint =E z∼E(x),ϵ∼N(0,I),t
hϵ−ϵ θ+∆θ(zt, t, τ(y, tk)) 2 2 i
(1)
wheret∼ U(1, T)is the timestep,ϵis the unscaled Gaus-
siannoise,andz t isthenoisylatentatstept.Byminimizing
Ljoint, the network simultaneously learns to manipulate the
specific generative trajectories via∆θand construct the op-
timized subpopulation embeddingtk.
Stage 2: Targeted Data Generation and
Downstream Model Training
TwoLabelSamplingStrategiesforDataGeneration.With
the joint conditional generator optimized in the previous
stage, we can synthesize auxiliary samples to augment the
original dataset. However, selecting appropriate condition
combinations remains a critical challenge to effectively mit-
igatedatasetbiases.Weemployaninverse-densitysampling
strategy for the condition labels. LetNk denote the number
of training samples assigned to clusterkandqthe number
of clusters in that class. If inverse-density weights were nor-
malized only within each class (before token merging), the
per-class weight for sub-label⟨tk⟩would be
Ptrain(⟨tk⟩) = N −1 kPq
j=1 N −1 j .(2)
However, we observe that a naive application of inverse-
density sampling reduces generation diversity, which orig-
inates from the randomness of the clustering process. Ex-
tremely similar samples might be partitioned into multiple
distinct groups, resulting in an inflated total sampling prob-
ability for these redundant concepts under inverse-density
sampling. Therefore, before inverse-density sampling, we
merge nearly redundant sub-label tokens within each class.
After Stage 1 fine-tuning, we compute pairwise cosine simi-
laritiesbetweenthelearnedtext-encoderembeddingsofsub-
label tokens⟨t k⟩in the same class. Token pairs whose co-
sine similarity exceeds a threshold are merged transitively,
yielding disjoint semantic groups within each class. LetG
denote the collection of all merged groups across classes.
Because AP clustering and token merging are performed in-
dependently within each class labely(Appendix C), cluster
countsN k and merged group sizesN(Gm)are computed
withineachclass,buttraining-setsamplingprobabilitiesare
normalized globally over all sub-labels. The global training
sampling probability for sub-label⟨tk⟩belonging to group
Gm is formulated as:
Ptrain(⟨tk⟩) = 1 |Gm| · N(G m)−1 P G′∈G N(G ′)−1 (3)
whereN(G m) = P i∈Gm Ni denotes the total empirical sample size of the merged groupGm in the original training
set,|G m|represents the number of distinct sub-labels con-
tained withinGm, and the sum runs over all merged groups
inG. Because sub-labels only proxy bias-relevant subpopu-
lations,inverse-densitysamplingupweightsempiricallyrare
clustersratherthanverifiedworst-caseclass-attributegroups;
somelow-densityclustersmayreflectnon-spuriousvariation
(e.g., pose or lighting). We use global normalization in part
toaccountforpotentiallong-tailedstructure;onCelebA,for
example, the not-blond class is much larger than the blond
class in the standard benchmark split (Sagawa et al. 2020).
Conditioningonthesampled(y, t k),wesynthesizeQ=|D|
images in total, forming a synthetic training setDsyn. We
then combineD syn with the original datasetDto construct
the mixed training setDmix =D ∪ Dsyn.
Furthermore, to fully unlock the framework’s potential
withoutmanualdatacuration,weleveragetheoptimizedgen-
erator to construct a balanced validation setDval for Deep
FeatureReweighting(DFR)(Kirichenko,Izmailov,andWil-
son 2023). Our goal is globally uniform coverage of merged
groups: after the same within-class token merging as in
training, we assign each merged group the same number of
synthetic images (samples-per-token), rather than stochastic
samplingoverclustersorgroups.Thisyieldsadeterministic,
globally balanced validation set; implementation details are
giveninAppendixB.Byconditioningonthepairedclassla-
belyandsub-label⟨t k⟩foreachgeneratedimage,weobtain
Dval as a practical proxy for the group-balanced validation
set required by DFR.
Training the Model and Deep Feature Reweighting.
We utilize the newly constructed mixed training setDmix to
train the downstream classifier, which consists of a feature
extractor followed by a last linear layer. To strictly isolate
theperformancegainsattributedtoouraugmentationframe-
work,weadheretothestandardEmpiricalRiskMinimization
(ERM) paradigm without introducing any modifications to
thenetworkarchitecture,objectivefunction,ordatasampling
heuristics.
After the initial ERM training onDmix, we apply Deep
FeatureReweighting(DFR)(Kirichenko,Izmailov,andWil-
son 2023). DFR is based on the observation that an ERM-
trained feature extractor can still encode core features, even
whenthefinalclassifierreliesheavilyonspuriouscues.Inthe
original DFR setting, the feature extractor is frozen and the
last classification layer is retrained from scratch on a small
reweightingsetthatisbalancedacrossspuriousgroups,typ-
icallyconstructedfromgroup-labeledvalidationdata.Inour
setting, true spurious groups are unavailable, so we use the
syntheticsub-label-balancedsetD valasaproxyreweighting
set.RetrainingonlythelastlinearlayeronD valallowsSAGE
to approximate the group-balanced DFR procedure without
manually curated class-attribute-balanced validation data.
Further implementation details are elaborated in Ap-
pendix B.
Experiment
In this section, we present our detailed experimental setup
and results, and conduct ablation studies.

Table1:Comparisonofworst-groupaccuracyandaverageaccuracyacrossthreedatasets.Allreportedresultsrepresentthemean
and standard deviation across three independent runs. The Group Info column indicates whether group labels are used, where
✓✓denotes that validation group labels are also utilized during training. The Category column shows the grouping criterion
used to categorize the compared methods. The bold and underlined numbers indicate the best results within each group and the
global best results, respectively.
Category Method Group Info Waterbirds CelebA MetaShift
train/val Worst Average Worst Average Worst Average
Labels in
train & val
DFR✗/✓✓92.9 ±0.2 93.3±0.5 88.3±1.1 91.3±0.3 72.8±0.6 77.5±0.6
gDRO✓/✓89.9 ±0.6 92.0±0.6 88.9±1.3 93.9±0.1 - -
Labels in val
JTT✗/✓86.7 93.3 81.1 88.064.6 ±2.3 74.4±0.6
LfF✗/✓78.0 91.2 77.2 85.1 - -
CnC✗/✓88.5 ±0.3 90.9±0.1 88.8±0.9 89.9±0.5 - -
DaC✗/✓92.3 ±0.4 95.3±0.4 81.9±0.7 91.4±1.1 78.3±1.6 79.3±0.1
No group labels
JTT✗/✗- -40.6 88.0- -
LfF✗/✗- -24.4 85.1- -
MaskTune✗/✗86.4 ±1.9 93.0±0.7 78.0±1.2 91.3±0.1 66.3±6.3 73.1±2.2
DISC✗/✗88.7 ±0.4 93.8±0.7 - -73.5 ±1.4 75.5±1.1
SAGE (ours)✗/✗89.5 ±0.1 93.5±0.1 85.7±0.3 90.1±0.2 79.1±1.8 82.3±0.2
Base (ERM)✗/✗73.2 ±4.2 90.8±0.5 44.6±0.3 95.5±0.2 64.2±3.3 77.4±1.8
Experiment setup
Datasets.Weevaluateourmethodonthreestandarddatasets,
namelyWaterbirds(Welinderetal.2010;Sagawaetal.2020),
CelebA (Liu et al. 2015) and MetaShift (Liang and Zou
2022). Below, we useai ∈ Aandyi ∈ Yto represent the
spurious attributes and true labels, respectively, illustrating
the spurious correlations in each dataset.
Waterbirds(Welinderetal.2010;Sagawaetal.2020):For
the Waterbirds dataset,Y={waterbird,landbird}andA=
{water background,land background}. 95% of the images
have the same bird typeYand background typeA.
CelebA(Liu et al. 2015): In this dataset,Y=
{blond hair,not blond hair}andA={male,female}. Only
6% of blond celebrities in the dataset are male.
MetaShift(Liang and Zou 2022): Our setup for this
dataset follows (Wu et al. 2023),Y={dog,cat}and
A={sofa,bed,bench,bike}. In the training set, "cat" co-
occurs with "sofa" and "bed", while "dog" co-occurs with
"bench"and"bike".Thiscorrelationdoesnotexistinthetest
set.
Basic Models. For a fair comparison, similar to other
compared methods, we use a ResNet-50 model (He et al.
2016) pre-trained on ImageNet as the classifier, and training
hyperparametersarethesameas(Sagawaetal.2020).Inour
method, we use CLIP (Radford et al. 2021) as the semantic
embedding model for clustering. Furthermore, we employ
theHuggingFaceimplementationofStableDiffusionv1.5 1
as the foundational generative model.
Compared Methods. We conduct our comparison in two
parts. The first part covers well-studied non-generative ap-
proaches for mitigating spurious correlations, which we cat-
1https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-
v1-5
egorize into three groups based on their reliance on prior
knowledge. The first group leverages explicit group labels
during training, represented by gDRO (Sagawa et al. 2020).
DFR (Kirichenko, Izmailov, and Wilson 2023) uses group
labels only for last-layer reweighting on a group-balanced
validation set, not during initial training. The second group,
comprising JTT (Liu et al. 2021), LfF (Nam et al. 2020),
CnC (Zhang et al. 2022), and DaC (Noohdani et al. 2024),
forgoestraining-timegrouplabelsbutstillreliesonmanually
curated, group-balanced validation sets for model selection.
The third group—MaskTune (Asgari et al. 2022) and DISC
(Wuetal.2023)—operatesstrictlywithoutanypriorknowl-
edge.AsSAGErequiresnopriorannotationsormanualcura-
tion,itnaturallyfallsintothisfinalgroup.Thesecondpartof
our comparison targets generative data augmentation meth-
ods, including Clustered DreamBooth (Basu et al. 2026),
ASPIRE (Ghosh et al. 2024), and DDB (Parast, Azam, and
Akhtar2025),whichshareSAGE’smotivationofpopulating
underrepresented data regions through synthetic generation.
For more details about all compared methods, see Related
Work .
Results
Compared with non-generative methodsWe report the
performance of all compared baselines, the base ERM, and
ourproposedSAGEacrossthreedatasets.Baselineresultsfor
WaterbirdsandCelebAaretakenfromtherespectiveoriginal
papers, MetaShift results from (Noohdani et al. 2024), and
JTT/LfF results without validation sets from (Asgari et al.
2022).
Table 1 shows that, under theNo group labelssetting (no
group labels in training or validation), SAGE achieves the
highest worst-group accuracy on all three benchmarks, ex-
ceedingthebestbaselineinthiscategoryby0.8,7.7,and5.6

Waterbirds CelebA
landbird
⟨t_5⟩
landbird
⟨t_8⟩
waterbird
⟨t_150⟩
waterbird
⟨t_177⟩
not blond
⟨t_5⟩
not blond
⟨t_11⟩
blond hair
⟨t_549⟩
blond hair
⟨t_550⟩
“a photo of [class label],
[sub-label token]”
“a photo of
[sub-label token]”
Figure 2: Visualization of images generated under different prompt conditionings across the Waterbirds and CelebA datasets.
The top row displays results using the full prompt, whereas the bottom row displays results generated by omitting the class
label. This comparison suggests that sub-label tokens provide conditional control over subpopulation-specific visual factors in
the generated images.
Table 2: Comparison with generative data augmentation
methods on Waterbirds and CelebA. The Group Info col-
umn indicates whether a method uses prior group labels
to guide generation or a group-balanced validation set for
model selection (✓), or operates without either (✗). Within
each Group Info category, the best worst-group accuracy is
underlined.
Method Group Info Waterbirds CelebA
WGA WGA
ASPIRE + ERM✗78.7 ±1.3 50.5±0.8
SAGE (ours)✗89.5 ±0.1 85.7±0.3
ASPIRE + DFR✓85.3 ±1.3 85.5±0.6
DDB✓93.0 ±0.1 85.8±1.4
Clustered
DreamBooth ✓88.1 ±0.9 84.1±0.6
percentage points on Waterbirds, CelebA, and MetaShift,
respectively. SAGE also attains the highest worst-group ac-
curacy among all listed methods on MetaShift.
Compared with generative methodsFor the generative
data augmentation comparison, we report results on Wa-
terbirds and CelebA, the two most widely used datasets
on which all compared methods have reported results. Ta-
ble 2 further compares SAGE with existing generative data
augmentation methods. Our method not only outperforms
ASPIRE+ERM—theonlyothergenerativeapproachwithout
manual group annotations—on both datasets, but also sur-
passes ASPIRE+DFR despite not using a manually curated
validation set. Although SAGE slightly trails DDB, which
relies on a complex external segmentation model, the sim-
plicityofourframeworkanditsindependencefromexternal
models make it a highly valuable solution.
Ablation Studies
Weconductablationstudiestoassessindividualcomponents
of SAGE, including the behavior revealed by conditional
generation under different sub-label tokens, the role of the
mixedtrainingsetinStage2,andtheutilityofthegenerated
validation set for DFR.
Visual Insights from Generated ImagesIn this subsec-
tion, we analyze conditional generation under different sub-
label tokens to examine the subpopulation-specific visual
factors captured by the learned tokens.
We use Waterbirds and CelebA for qualitative visual-
ization. Figure 2 shows that changing the sub-label token
alters generated images while the class label is fixed in
the full prompt, suggesting that the learned tokens encode
subpopulation-specific visual variation. On Waterbirds, the
illustrated class-token combinations can be interpreted post
hocaslandbird/land,landbird/water,waterbird/land,andwa-
terbird/water. Notably,⟨t_8⟩and⟨t_150⟩correspond to vi-
suallyconflictedclusterswithonly25trainingsampleseach;
such rare combinations are upweighted by inverse-density
sampling, consistent with the goal of reducing background
reliance in the downstream classifier.
Effect of the Mixed Training SetTo isolate the perfor-
mance gains brought solely by our data augmentation, we
conductanexperimentexcludingthefinalDFRstepinStage
2. We further disentangle the contribution of our fine-tuned
generator from generic generative augmentation by intro-
ducing a control setting where vanilla Stable Diffusion v1.5
generates synthetic data using the standard prompt “a photo
of [class label]”. These data are combined with the origi-
nal datasetDand expanded to the same total size asDmix,
forming the standard generation datasetDsg. The results are
presented in Table 3.
As shown in Table 3, merely augmenting with generic
synthetic data (Dsg) provides limited benefit or can even be
harmful, whereasDmix—built from targeted sub-label sam-
pling intoD syn—achieves substantially larger gains. This

Table 3: Ablation on mixed training set without DFR. Each
entry is worst-group accuracy (%) of a ResNet-50 ERM
classifier trained on the column dataset.Dis the original
training set;D sg adds generic Stable Diffusion v1.5 aug-
mentation at the same total scale asDmix (see text above);
Dmix =D ∪ Dsyn uses targeted SAGE synthesis. Parenthe-
ses give the WGA gain ofDmix overD.
DatasetD D sg Dmix
Waterbirds 73.2 70.5 77.5 (+4.3)
CelebA 44.6 44.1 49.8 (+5.2)
MetaShift 64.2 65.6 70.3 (+6.1)
confirms that the performance improvement stems from our
targeted augmentation of underrepresented subpopulations
rather than from generative data augmentation alone. We
strictly adopt the same model architecture and hyperparam-
eters as (Sagawa et al. 2020) for the Waterbirds and CelebA
dataset, and all experiments in this ablation are conducted
using a fixed random seed for fair comparison.
Table4:Evaluationofthegeneratedbalancedvalidationset.
We compare our results against the standard DFR perfor-
mance obtained using the original, manually curated vali-
dation set. For each experiment, we report the mean perfor-
mance across three runs using a fixed set of seeds.
Waterbirds
ERM WGA (%) 73.2
OrigD val GenD val
Samples-per-token - 8 12 16
Valset Size 532 312 468 624
DFR WGA (%) 89.7 84.1 88.6 85.9
CelebA
ERM WGA (%) 44.6
OrigD val GenD val
Samples-per-token - 8 12 16
Valset Size 728 376 564 752
DFR WGA (%) 62.8 80.2 82.6 79.5
MetaShift
ERM WGA (%) 64.2
OrigD val GenD val
Samples-per-token - 2 4 6
Valset Size 68 44 88 132
DFR WGA (%) 69.5 62.6 68.5 73.4
Effect of the Synthetic Validation SetWe evaluate the
balanced validation set generated by our uniform label sam-
pling strategy in this section. For each dataset, we construct
threesyntheticvalidationsets(D val)ofvaryingsizesbyem-
ployingthreedifferentsamples-per-tokenvalues(aftermerg-
ing). The meaning of the samples-per-token hyperparameter
is explained in Appendix B. Specifically, we conduct Deep
Feature Reweighting (DFR) on the same ResNet-50 back-
bone,contrastingtheperformanceofoursyntheticD valwith
aground-truth,manually-pickedbalanceddataset.Toensure
acontrolledcomparison,weexcludeD mix fromthisanalysis
and train the classifier entirely on the original datasets. To
ensureconsistency,allexperimentsutilizeidenticalDFRhy-
perparameters, with the only variation being the size of the
validation sets. Results are summarized in Table 4.
Table 4 compares DFR using our syntheticDval against
manually curated group-balanced validation sets. Overall,
synthetic validation is competitive, but the relative perfor-
mance depends on how spurious factors are structured in
each benchmark. Manual validation balances coarse anno-
tated(y, a)groups, yet it does not control finer subpop-
ulation variation within each group—for example, images
sharing the same spurious attribute label may still be dom-
inated by a few visual subtypes. Our synthetic set instead
balances discovered sub-labels via uniform sampling, pro-
vidingfiner-grainedpseudo-balancewhenclustersalignwith
bias-relevant factors (Appendix C).
On Waterbirds, where spurious attributes are artificially
constructed and align cleanly with annotated groups, the
manuallycuratedvalidationsetremainsstrongest(89.7%vs.
at most 88.6% with generated validation). On CelebA and
MetaShift, which feature more heterogeneous, naturally oc-
curringspuriouscorrelations,syntheticvalidationcanmatch
or exceed manual validation at several scales (up to 82.6%
vs. 62.8% on CelebA and 73.4% vs. 69.5% on MetaShift).
Notably,onCelebA,ourgeneratedD valsubstantiallyout-
performs the manually curated validation set. We attribute
this jointly to finer sub-label balancing beyond coarse(y, a)
groups and to the subsampled construction of manual val-
idation (Kirichenko, Izmailov, and Wilson 2023): majority
groups are randomly downsampled to match the smallest
group, introducing selection variance among retained im-
ages. Standard DFR mitigates this via repeated subsampling
andℓ 1 regularization, but we use a single-run setup without
these measures for both validation types. Synthetic valida-
tionavoidssubsamplingentirely;togetherwithfinerpseudo-
balance, this helps explain the large gap on CelebA and the
gains on MetaShift.
Overall, these results show that our synthetically gener-
atedD val provides an effective validation set for DFR with-
outrelyingonmanuallycuratedgroup-balanceddata.Across
different validation sizes and benchmark settings, sub-label-
balanced synthetic validation consistently delivers substan-
tial gains over ERM and remains a practical substitute for
manual validation in the group-label-free setting.
Conclusion
WeproposeSAGE,atwo-stagemethoddesignedtomitigate
spurious correlations. Driven by a data-centric philosophy,
our method actively expands minority samples to force the
classifier into learning robust core features, while concur-
rently synthesizing a highly practical, balanced validation
settofurtherbolstermodelrobustness.Weachievetheseob-
jectivesbyutilizingtheclusteredsub-labelstobothfine-tune

the conditional generative models and guide the final gen-
eration process. Experimental results across three distinct
benchmark datasets demonstrate the efficacy of the SAGE
framework. Furthermore, because SAGE operates indepen-
dently of any explicit prior knowledge or specific dataset
distribution characteristics, it holds significant potential for
generalization to other datasets with subpopulation shifts,
and even to broader, general-purpose datasets.
References
Asgari,S.;Khani,A.;Khani,F.;Gholami,A.;Tran,L.;Mah-
daviAmiri,A.;andHamarneh,G.2022. Masktune:Mitigat-
ing spurious correlations by forcing to explore.Advances in
Neural Information Processing Systems, 35: 23284–23296.
Azizi, S.; Kornblith, S.; Saharia, C.; Norouzi, M.; and Fleet,
D. J. 2023. Synthetic data from diffusion models improves
imagenet classification.Transactions on Machine Learning
Research.
Basu, A.; Gupta, A.; Bhat, A.; and Radhakrishnan, V. B.
2026. Harnessing diffusion-generated synthetic images for
fair image classification. InProceedings of the AAAI Con-
ference on Artificial Intelligence, volume 40, 38205–38213.
Beery,S.;VanHorn,G.;andPerona,P.2018. Recognitionin
terra incognita. InProceedings of the European conference
on computer vision (ECCV), 456–473.
Dhariwal, P.; and Nichol, A. 2021. Diffusion models beat
gans on image synthesis.Advances in neural information
processing systems, 34: 8780–8794.
Dunlap,L.;Umino,A.;Zhang,H.;Yang,J.;Gonzalez,J.E.;
and Darrell, T. 2023. Diversify your vision datasets with
automaticdiffusion-basedaugmentation.Advancesinneural
information processing systems, 36: 79024–79034.
Frey, B. J.; and Dueck, D. 2007. Clustering by passing
messages between data points.Science, 315(5814): 972–
976.
Geirhos,R.;Jacobsen,J.-H.;Michaelis,C.;Zemel,R.;Bren-
del, W.; Bethge, M.; and Wichmann, F. A. 2020. Shortcut
learning in deep neural networks.Nature Machine Intelli-
gence, 2(11): 665–673.
Ghosh, S.; Evuru, C. K.; Kumar, S.; Tyagi, U.; Sakshi,
S.; Chowdhury, S.; and Manocha, D. 2024. ASPIRE:
Language-Guided Data Augmentation for Improving Ro-
bustness Against Spurious Correlations. In Ku, L.-W.; Mar-
tins, A.; and Srikumar, V., eds.,Findings of the Associa-
tion for Computational Linguistics: ACL 2024, 386–406.
Bangkok,Thailand:AssociationforComputationalLinguis-
tics.
He,K.;Zhang,X.;Ren,S.;andSun,J.2016. DeepResidual
LearningforImageRecognition. InProceedingsoftheIEEE
Conference on Computer Vision and Pattern Recognition
(CVPR), 770–778.
Ho, J.; Jain, A.; and Abbeel, P. 2020. Denoising diffusion
probabilistic models.Advances in neural information pro-
cessing systems, 33: 6840–6851.
Hu,E.J.;Shen,Y.;Wallis,P.;Allen-Zhu,Z.;Li,Y.;Wang,S.;
Wang,L.;andChen,W.2022. LoRA:Low-RankAdaptation
of Large Language Models. InInternational Conference on
Learning Representations.
Kirichenko, P.; Izmailov, P.; and Wilson, A. G. 2023. Last
layer re-training is sufficient for robustness to spurious cor-
relations. InInternational Conference on Learning Repre-
sentations.
Krizhevsky, A.; Sutskever, I.; and Hinton, G. E. 2012. Ima-
genetclassificationwithdeepconvolutionalneuralnetworks.
Advances in neural information processing systems, 25.
Liang,W.;andZou,J.2022.MetaShift:ADatasetofDatasets
for Evaluating Contextual Distribution Shifts and Training
Conflicts. InInternational Conference on Learning Repre-
sentations.
Liu,E.Z.;Haghgoo,B.;Chen,A.S.;Raghunathan,A.;Koh,
P. W.; Sagawa, S.; Liang, P.; and Finn, C. 2021. Just train
twice: Improving group robustness without training group
information.InInternationalConferenceonMachineLearn-
ing, 6781–6792. PMLR.
Liu, Z.; Luo, P.; Wang, X.; and Tang, X. 2015. Deep learn-
ing face attributes in the wild. InProceedings of the IEEE
international conference on computer vision, 3730–3738.
Nam,J.;Cha,H.;Ahn,S.;Lee,J.;andShin,J.2020. Learn-
ing from Failure: Training Debiased Classifier from Biased
Classifier. InAdvances in Neural Information Processing
Systems, volume 33.
Noohdani, F. H.; Hosseini, P.; Parast, A. Y.; Araghi, H. Y.;
and Baghshah, M. S. 2024. Decompose-and-compose: A
compositional approach to mitigating spurious correlation.
InProceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, 27662–27671.
Parast, A. Y.; Azam, B.; and Akhtar, N. 2025. DDB: Diffu-
sion Driven Balancing to Address Spurious Correlations. In
Proceedings of the IEEE/CVF International Conference on
Computer Vision, 17526–17535.
Qraitem, M.; Saenko, K.; and Plummer, B. A. 2024. From
Fake to Real: Pretraining on Balanced Synthetic Images to
Prevent Spurious Correlations in Image Recognition. In
Leonardis, A.; Ricci, E.; Roth, S.; Russakovsky, O.; Sat-
tler, T.; and Varol, G., eds.,Computer Vision – ECCV 2024,
230–246.Cham:SpringerNatureSwitzerland. ISBN978-3-
031-73636-0.
Radford, A.; Kim, J. W.; Hallacy, C.; Ramesh, A.; Goh,
G.; Agarwal, S.; Sastry, G.; Askell, A.; Mishkin, P.; Clark,
J.; et al. 2021. Learning transferable visual models from
natural language supervision. InInternational conference
on machine learning, 8748–8763. PMLR.
Rombach,R.;Blattmann,A.;Lorenz,D.;Esser,P.;andOm-
mer, B. 2022. High-resolution image synthesis with latent
diffusion models. InProceedings of the IEEE/CVF confer-
ence on computer vision and pattern recognition, 10684–
10695.
Sagawa,S.;Koh,P.W.;Hashimoto,T.B.;andLiang,P.2020.
Distributionally robust neural networks for group shifts: On
the importance of regularization for worst-case generaliza-
tion. InInternational Conference on Learning Representa-
tions.

Sun, M.; Zhao, R.; Huang, Z.; Ding, S.; and Liu, J. 2026.
IT-OSE: Exploring Optimal Sample Size for Industrial Data
Augmentation. Preprint, arXiv:2602.15878.
Welinder, P.; Branson, S.; Mita, T.; Wah, C.; Schroff, F.;
Belongie,S.;andPerona,P.2010. Caltech-UCSDbirds200.
Technical Report CNS-TR-2010-001, California Institute of
Technology.
Wu,S.;Yuksekgonul,M.;Zhang,L.;andZou,J.2023. Dis-
coverandcure:Concept-awaremitigationofspuriouscorre-
lation. InInternational Conference on Machine Learning,
37765–37786. PMLR.
Zhang, M.; Sohoni, N. S.; Zhang, H. R.; Finn, C.; and Ré,
C. 2022. Correct-N-Contrast: A Contrastive Approach for
Improving Robustness to Spurious Correlations. InInter-
national Conference on Machine Learning, 26484–26516.
PMLR.

This is the supplementary material of the paper “SAGE:
Subpopulation-Aware Generative Enhancement for Mitigat-
ingSpuriousCorrelations”.Thecontentcatalogisasfollows:
•Appendix A: Dataset Statistics
–Appendix A.1: Dataset Groups and Label Combina-
tions
–Appendix A.2: Group Distributions by Split
•Appendix B: Implementation Details
–Appendix B.1: Hyperparameters
–Appendix B.2: Hardware
•Appendix C: Clustering Analysis
–Appendix C.1: Clustering Hyperparameters
–Appendix C.2: Cluster Statistics
–Appendix C.3: Clustering Strategy for CelebA
•Appendix D: Effectiveness Analysis of DFR with the
Generated Validation Set
–Appendix D.1: Feature-Space Construction
–Appendix D.2: Downstream Classification Analysis
Appendix A: Dataset Statistics
We report group definitions and split-wise(y, a)distribu-
tions for the three benchmarks used in the main paper. All
countsarecomputedfromthedatasetmetadatainourexperi-
ments.SAGEperformsclusteringandgenerativefine-tuning
on the training split only (4,795 / 162,770 / 1,024 images
onWaterbirds,CelebA,andMetaShift,respectively);bench-
mark validation splits are not used in the method pipeline,
andtestsamplesareheldoutforfinalevaluation.AppendixC
reports post-hoc clustering purity on the union of training
and validation splits (5,994 / 182,637 / 1,105 images) for
numerical analysis only. Implementation details and clus-
tering analysis are given in Appendix B and Appendix C,
respectively.
Dataset Groups and Label Combinations
Figure 4 summarizes the four(y, a)groups per benchmark.
EachcolumnG i showsasquare-croppedtrainingexample,a
short group description, the class labely, and the number of
training and validation images. Example images are center-
cropped and resized to a common square size. The figure is
placed at the end of this supplementary material.
Group Distributions by Split
Tables5–7reportthenumberofimagesineach(y, a)group
on the training, validation, and test splits.
Table 5: Waterbirds group distribution by split (Ntrain =
4,795,N val = 1,199,N test = 5,794). Validation and test
splits are approximately group-balanced.
Group(y, a)Train Val Test
landbird, land background 3,498 467 2,255
landbird, water background 184 466 2,255
waterbird, land background 56 133 642
waterbird, water background 1,057 133 642
Table 6: CelebA group distribution by split (N train =
162,770,N val = 19,867,N test = 19,962).
Group(y, a)Train Val Test
not blond, female 71,629 8,535 9,767
not blond, male 66,874 8,276 7,535
blond, female 22,880 2,874 2,480
blond, male 1,387 182 180
Table 7: MetaShift group distribution by split (Ntrain =
1,024,N val = 81,N test = 460). Shelf background appears
only in validation and test.
Group(y, a)Train Val Test
cat, bed 348 0 0
cat, sofa 202 0 0
dog, bench 124 0 0
dog, bike 350 0 0
cat, shelf 0 34 201
dog, shelf 0 47 259
Appendix B: Implementation Details
This appendix supplements Section 3 and Section 4 of the
main paper with reproducibility-oriented details. Dataset
split sizes and group distributions are given in Appendix A;
clustering-specific hyperparameters and post-hoc purity
analysis are reported separately in Appendix C.
Hyperparameters
Unless stated otherwise, we use the same configuration
across Waterbirds, CelebA, and MetaShift.
Conditional generator fine-tuning (Stable Diffusion v1.5
+ LoRA).We fine-tune the Hugging Face Stable Diffu-
sion v1.5 checkpoint2 using Low-Rank Adaptation (LoRA)
on the UNet, jointly optimizing LoRA weights and newly
addedsub-labeltokenembeddings.Eachclusterkreceivesa
unique token⟨tk⟩, initialized from the wordphoto. Training
uses the prompt template“a photo of [class labely], [sub-
label token⟨t k⟩]”(Eq. 1 in the main paper). Key training
hyperparameters are:
•LoRA rankr=128; LoRAα=128
•Learning rate: 1e-5; Optimizer: AdamW
2https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-
v1-5

•Batch size (per GPU): 4; Training epochs: 100
•Image resolution: 512
•Trainablemodules:LoRAonUNetattentionlayers+sub-
label token embeddings
Token similarity merging.After fine-tuning, we merge
redundant sub-label tokens within each class (main paper,
Stage 2). For classy, letek denote the learned text-encoder
embeddingofsub-labeltoken⟨t k⟩.Wecomputeallpairwise
cosinesimilaritiescos(e i,e j)amongtokensinthatclassand
taketheirmean¯sy.Themergecriterionisnotafixedabsolute
threshold; instead, two tokens are merged if
cos(ei,e j)> τmerge =β·¯s y,(4)
whereβisadataset-specificmultiplier(sharedacrossclasses
within the same dataset). Merging is applied transitively to
formdisjointsemanticgroups.Wesetβ=2.5onWaterbirds,
4.0 on CelebA, and 4.0 on MetaShift.
Validation-set synthesis (Dval).We empirically observe
that when synthesizing a small-scale validation set, relying
onpurelystochasticprobabilitysamplingcanintroducesub-
stantial variance in the resulting data distribution. Conse-
quently,forvalidationsetconstruction,wereplacestochastic
inverse-density sampling with a deterministic samples-per-
token parameter.
Hardware
Stable Diffusion fine-tuning is run on two NVIDIA RTX
4090GPUs.Allotherstages—CLIPfeatureextraction,clus-
tering, synthetic image generation, ResNet-50 training, and
DFR—are run on a single NVIDIA RTX 4090 GPU.
Appendix C: Clustering Analysis
Clustering Hyperparameters
WeapplyAffinityPropagation(AP)clusteringindependently
within each class using CLIP embeddings as input features.
The AP algorithm has two key hyperparameters: the damp-
ingfactorλ damp,whichcontrolsnumericaloscillationduring
messagepassing,andthediagonalpreferencevaluess(k, k),
set to the mean of all pairwise similarities scaled by a mul-
tiplierα pref. For Waterbirds and MetaShift, whose training
sets are relatively small, we setλdamp = 0.5. For CelebA,
which contains over 160,000 training samples, we increase
the damping toλdamp = 0.8to ensure stable convergence.
Across all three datasets, we fixαpref = 1, meaning the
preferencevalueequalsthemeanofallpairwisesimilarities.
Cluster Statistics
Ground-truth spurious labels are used only in this post-hoc
analysis and are not available to SAGE during training or
generation. For purity evaluation, we re-cluster on the union
of training and validation splits (Table 8); this is separate
from the train-split-only clustering used in the method. For
datasetswithsuchlabels,weevaluateclusteringpurity—the
extent to which discovered clusters align with spurious at-
tributes.LetC={C 1, . . . , CK}denotethesetofdiscovered
clusters andAthe set of spurious attributes (|A|= 2for
Waterbirds and CelebA;|A|= 4for MetaShift). For each
clusterC k, its purity is defined as:
Purity(Ck) = max a∈A
|{(xi, yi, ai)∈C k :a i =a}|
|Ck| .(5)
TheoverallpurityreportedinTable8isthesample-weighted
(micro) average over clusters:
Purityoverall = 1PK
k=1 |Ck|
KX
k=1
|Ck|Purity(C k).(6)
Table 8: Number of samples, resulting clusters, and cluster-
ing purity for each dataset. Sample counts are the sum of
the training and validation splits and are used for clustering
analysis only.
Dataset Samples Clusters Purity (%)
Waterbirds 5,994 180 93.66
CelebA 182,637 1,089 98.17
MetaShift 1,105 113 72.49
As shown in Table 8, purity exceeds 90% on Waterbirds
and CelebA, indicating that clusters often align with binary
spurious attributes on these datasets. This post-hoc analysis
suggests that visually salient spurious cues may also struc-
tureCLIPfeaturesimilarity,thoughcluster–groupalignment
remains imperfect. Ground-truth spurious labels are used
here for evaluation only; during training, SAGE relies solely
on cluster-derived sub-labels. The purity on MetaShift is
comparativelylower(72.49%).Weconjecturetwocontribut-
ingfactors.First,MetaShiftinvolvesfourspuriousattributes
(sofa, bed, bench, bike) rather than two, inherently increas-
ing the difficulty of clean separation. Second, unlike birds
and human faces, cats and dogs exhibit pronounced inter-
class visual differences beyond the background, which may
compete with spurious background cues during clustering.
Despite this weaker alignment, SAGE still improves worst-
group accuracy on MetaShift (Table 1), suggesting that aug-
mentationbyrareclusterscanhelpevenwhenclustersdonot
map cleanly to spurious groups.
Clustering Strategy for CelebA
With over 160,000 training samples, CelebA poses a com-
putationalchallengeforAffinityPropagation:storingthefull
N×Nsimilarity matrix is infeasible. We therefore adopt a
three-stage strategy.
First, we reduce the dataset to a diverse core set ofK=
10,000samples via Farthest Point Sampling (FPS), which
iteratively selects points farthest from the already chosen
set, ensuring broad coverage of the feature space. Second,
we run AP clustering exclusively on this core set to identify
exemplars. Third, we build a Faiss exact nearest-neighbor
index over the exemplars and assign every sample in the
fulldatasettoitsclosestexemplar,therebyrecoveringcluster
labels for all samples.
We repeat this procedure separately for each class (blond
/ not blond) and offset cluster indices globally to prevent

overlap. The dominant memory cost reduces from storing
theN×Nsimilarity matrix (infeasible atN≈1.6×10 5)
toO(N×D+K 2),whereDistheCLIPfeaturedimension
andK≪N.Inourexperiments,Kissimplysetto10,000.
Appendix D: Effectiveness Analysis of DFR
with the Generated Validation Set
Feature-Space Construction
Figure 3 analyzes how applying DFR on the generated vali-
dation set constructed by SAGE affects downstream classifi-
cation in the frozen feature space. For each dataset, we use
the ERM-trained backbone as a fixed feature extractor. Let
hθ(·)denote this backbone after replacing the final classifi-
cation layer with an identity map, and letf=hθ(x)∈R d
be the frozen feature of an imagex. We construct the two-
dimensional PCA space separately for each dataset. Specif-
ically, letDvis test denote the held-out test samples used in the
visualization and letDDFR val denote the generated validation
samplesusedforDFR.PCAisfitontheunionoftheirfrozen
features,
SPCA ={h θ(x) :x∈ Dvis test} ∪ {hθ(x) :x∈ DDFR val }.(7)
IfF= [f 1, . . . , fn]⊤ stacks these features, we first center
thembyµ= 1 n P i fi andcomputetheempiricalcovariance matrix
C= 1 n
nX
i=1
(fi −µ)(f i −µ) ⊤.(8)
The PCA basis is given by the two eigenvectors with the
largest eigenvalues,u1 andu 2, satisfyingCu j =λ juj with
λ1 ≥λ 2. For any frozen featuref, its two-dimensional co-
ordinate is then
z=U ⊤(f−µ), U= [u 1, u2]∈R d×2.(9)
We use the same meanµand basisUto project both the
reweighting samples and the held-out test samples, so the
two panels in each row share a common coordinate system.
The PCA basis is fit only onDvis test and the generated vali-
dationsubsetD DFR val definedabove;anyadditionalgenerated
reweighting samples shown in the left column are trans-
formedafterwardusingthisfixedPCAmap.Theleftcolumn
contains the generated reweighting samples used for DFR,
while the right column contains samples from the held-out
test split. For Waterbirds and CelebA, whose original test
splits are large,Dvis test is a balanced subset with 180 images
sampled from each(y, a)group. This keeps the visualiza-
tion readable while preserving the class-attribute structure
needed for comparing decision boundaries. Finally, for a bi-
nary final linear layer with logitsw⊤ c f+b c, the decision
boundary in the original feature space is
(w1 −w 0)⊤f+ (b 1 −b 0) = 0.(10)
SubstitutingthePCA-planeapproximationf≈µ+U zgives
the boundary drawn in Figure 3,

(w1 −w 0)⊤U  z+ (w 1 −w 0)⊤µ+ (b 1 −b 0) = 0.(11)
This allows us to compare the ERM decision boundary with
thedecisionboundaryafterDFRwhilekeepingthebackbone
representation fixed.
Downstream Classification Analysis
The six panels compare the proxy reweighting set and the
held-outtestdistributionunderthesamefrozenfeaturerepre-
sentation.ApplyingDFRwithD valupdatesonlythelastlin-
earlayer,whichshiftsthedecisionboundaryintheprojected
test feature space. This boundary shift is consistent with the
roleofD valasamorebalancedproxyreweightingset:itsup-
pliesadditionalcoverageforrareorunder-representedclass-
attribute combinations and reduces the dependence of the
final classifier on majority-dominated correlations. Together
with the quantitative results reported in the main paper, this
feature-space analysis supports the conclusion that DFR on
the generated validation set improves worst-group accuracy
whilemaintainingcompetitiveaverageaccuracy,i.e.,thero-
bustness gain is obtained without a large sacrifice in overall
classification performance.

Reweighting samples Held-out test set
(a) Waterbirds reweighting samples (b) Waterbirds test set
(c) CelebA reweighting samples (d) CelebA test set
(e) MetaShift reweighting samples (f) MetaShift test set
Figure 3: Decision-boundary visualizations for Waterbirds, CelebA, and MetaShift. Left column: reweighting samples from
Dval with the decision boundary after DFR. Right column: held-out test samples with both the ERM decision boundary and
the decision boundary after DFR. Green dashed line: decision boundary after DFR; red dashed line: ERM decision boundary.
Blue/orangepointsdenotethetwotargetclasses:landbird/waterbird,non-blond/blond,andcat/dog,respectively.Circles/squares
denote the available spurious attribute for Waterbirds and CelebA; for MetaShift, they denote merged generated-background
groups in the left panel, while test samples are triangles because all come from the held-out shelf background.

Waterbirds dataset
G1 G2 G3 G4
Description landbird on land landbird on water waterbird on land waterbird on water
Class label 0 0 1 1
# Train data 3,498 184 56 1,057
# Val data 467 466 133 133
Target:bird type;Spurious feature:background type;Minority:G 2,G 3.
CelebA hair color dataset
G1 G2 G3 G4
Description non-blond woman non-blond man blond woman blond man
Class label 0 0 1 1
# Train data 71,629 66,874 22,880 1,387
# Val data 8,535 8,276 2,874 182
Target:hair color;Spurious feature:gender;Minority:G 4.
MetaShift dataset
G1 G2 G3 G4
Description cat on bed cat on sofa dog on bench dog on bike
Class label 0 0 1 1
# Train data 348 202 124 350
# Val data 0 0 0 0
Target:animal species;Spurious feature:background object.
Figure4:Overviewofthefour(y, a)groupsforWaterbirds,CelebA,andMetaShift.Classlabelyfollowsthestandardgroup-ID
convention in each benchmark.
