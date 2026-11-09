---
title: Are You Learning Biological Signal or Shortcuts? Auditing and Mitigating Bias in Protein-Protein
  Interaction Datasets
url: https://arxiv.org/abs/2609.10193
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Judith Bernett
- Anton Spannagl
- Joel Ås
- Markus List
- David B. Blumenthal
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.10193
pages: 33
chars: 107415
fetched_at: '2026-11-08T13:27:27+00:00'
kb_version: 1
---

# Are You Learning Biological Signal or Shortcuts? Auditing and Mitigating Bias in Protein-Protein Interaction Datasets

Are You Learning Biological Signal or Shortcuts? Auditing
and Mitigating Bias in Protein-Protein Interaction Datasets
Judith Bernett judith.bernett@fau.de
Department Artificial Intelligence in Biomedical Engineering
Friedrich-Alexander-Universität Erlangen-Nürnberg
Anton Spannaglanton.spannagl@tum.de
TUM School of Life Sciences
Technical University of Munich
Joel Ås joelkarl.as@ieo.it
Department of Experimental Oncology
IEO European Institute of Oncology IRCCS
Markus List markus.list@tum.de
TUM School of Life Sciences
Technical University of Munich
David B. Blumenthaldavid.b.blumenthal@fau.de
Department Artificial Intelligence in Biomedical Engineering
Friedrich-Alexander-Universität Erlangen-Nürnberg
Abstract
Protein-protein interaction (PPI) databases do not faithfully reflect biological realities. In-
stead, they are influenced by study and technical biases that distort certain protein and
interaction attributes. Machine learning models can exploit these as learning shortcuts if
the negative dataset is not constructed with care. So far, the shortcuts introduced during
PPIdatasetconstructionhaveonlybeenexaminedinisolation. Here, wesystematicallychar-
acterize both reported and, to our knowledge, previously unreported biases in PPI datasets
that lead machine learning models to learn shortcuts instead of biological signal. We analyze
HIPPIE, IntAct, and STRING, dedicated PPI databases, as well as two datasets derived
from 3D-structural information in the Protein Data Bank (PDB). We show that random
data splitting introduces strong topological shortcuts. When train-test protein overlap is
removed, the resulting datasets still retain usable shortcuts stemming from self-interactions,
taxonomic identity, and functional relatedness, whose prevalence interestingly depends on
the data source. We further show that sampling negatives from a set of high-confidence
non-interactors, an intuitively appealing choice, can amplify the shortcut stemming from
functional relatedness. To detect and mitigate these biases, we provide an open Nextflow
pipeline that combines similarity-aware, data-loss-minimizing dataset splitting with bias-
minimizing negative sampling, both formulated as integer linear programs. Its key concept
of quantifying biases to minimize them through optimization-based negative sampling can,
in principle, be extended to any machine learning problem where the pool of negative can-
didates is much larger than the positives and is thus of interest also beyond PPI prediction.
1 Introduction
Deep machine learning models have a well-documented tendency to learn the “path of least resistance”, a
phenomenon that has spawned an entire field dedicated to studying shortcut learning and its mitigation
1
arXiv:2609.10193v1  [q-bio.MN]  9 Sep 2026

(Geirhos et al., 2020). This has uncovered a series of reported generalization failures that revealed what
models were actually paying attention to. Cows were misclassified when displayed on a beach rather than
on grass (Beery et al., 2018). An object detection model struggled with an elephant randomly inserted into
a picture of a man sitting in a room, either missing it entirely or misclassifying it as a chair, depending on
its placement (Rosenfeld et al., 2018). An X-ray pneumonia detector failed to generalize to images from a
new hospital because it had learned to rely on the hospital token in the image and the pneumonia prevalence
in that hospital, rather than the lung itself (Zech et al., 2018). Amazon’s HR screening tool was found to
systematically favor male candidates (Dastin, 2022). Such cases are cautionary tales for anyone tempted to
take strong modeling results at face value, summarized in Geirhos et al. (2020)’s adapted maxim“Never
attribute to high-level abilities that which can be adequately explained by shortcut learning”1. Whether and
how effectively a model exploits a shortcut ultimately depends on four components that, together, determine
what the model can learn: the model architecture, the training data, the loss function, and the optimization
strategy (Geirhos et al., 2020). Before any of these can be adjusted, one must first identify which biases are
present in the dataset, a task that is inherently domain-specific and far from trivial.
The issue is pressing in deep learning models for biomedical applications. While we want to be able to
harness the full potential of deep learning for healthcare applications, it becomes all the more important
to understand what a model is learning, which (latent) features it relies on most, for which subgroups it
performs well, and whether it has, indeed, acquired a high-level ability. It is also a domain that is not as
easily understood from the human perspective as, e.g., object detection or text translation, where a human
can more easily verify whether the model performed the task adequately.
In this article, we look at the case of sequence-based protein-protein interaction (PPI) prediction, i.e., the
task to predict if two proteins bind to each other based on representations of their amino acid sequences.
Predicting PPIs is a key task in computational biomedicine, used to understand the functions of understudied
proteins, study disease mechanisms, or identify potential drug targets (Soleymani et al., 2022). The PPI
databases, however, contain data from hypothesis-driven experiments, leading to study biases (e.g., the
overstudyofhumandisease-relatedproteins)aswellastechnicalbiases(e.g., duetolowabundance)(Schaefer
et al., 2015). The negative dataset is usually constructed via random sampling. If the sampling approach is
not chosen carefully to mirror certain properties of the positive dataset, unwanted distributional differences
can emerge that machine learning models can exploit as shortcuts rather than learning causal biochemical
properties, such as matching binding sites. Previously reportedly properties used as shortcuts included
subcellular location (Ben-Hur & Noble, 2006), sequence similarity (Hamp & Rost, 2015; Bernett et al., 2024),
topology (Park & Marcotte, 2012; Bernett et al., 2024; Chatterjee et al., 2023; Zhou et al., 2025), taxonomy
(Hallee et al., 2026), and database curation and study bias (Szymborski & Emad, 2022; Makrodimitris et al.,
2020). Each of these has, however, been studied in isolation, and typically on a single dataset from a single
data source. Consequently, it remains unclear which shortcuts dominate, how strongly they interact, whether
mitigating one aggravates another, and whether shortcuts differ across PPI databases.
We address this gap with the following contributions: First, we quantify whether certain attributes (self-
interactions, taxonomy, topology, sequence similarity, embedding similarity, GO category overlap (Gene
Ontology Consortium, 2026)) can be used as a shortcut in commonly used PPI data sources, employing
the G-AUDIT bias detection framework (Drenkow et al., 2026). The framework measures whether a given
attribute is highly detectable from the input data and whether it has mutual information with the output
label. Second, we improve Bernett et al. (2024)’s previously proposed similarity- and leakage-reducing
approach by formulating similarity-aware PPI dataset splitting as an integer linear program (ILP) that
additionally minimizes data loss while giving a user control over the resulting split sizes. Third, we also
formulate bias-minimizing negative sampling as an ILP. Here, we sample pairs of non-interacting proteins
such that the distributions of the shortcut attributes identified in step 1 (self-interaction count, per-protein
degree, taxon-pair distribution, and mean GO-BP overlap) are similar in the sets of sampled negatives and
input positives, i.e., the annotated PPIs. We show that datasets derived from 3D protein complex structures
curated in the Protein Data Bank (PDB) (Berman et al., 2000) store a fundamentally different population of
1A blend of Morgan’s Canon“In no case is an animal activity to be interpreted in terms of higher psychological processes
if it can be fairly interpreted in terms of processes which stand lower on the scale of psychological evolution and development”
and Hanlon’s razor“Never attribute to malice that which can be adequately explained by stupidity”
2

interactions than the databases containing data from dedicated interaction-detection assays, limiting their
direct use to augment PPI datasets with structural information. Further, we show that sampling negatives
from a set of high-confidence non-interactors can amplify existing distributional shifts. All analyses are
implemented in an open Nextflow pipeline that the community can apply to their own datasets.
2 Results
2.1 Study overview
Figure 1: Metro map of the major steps implemented in our Nextflow PPI splitting pipeline for the five
configurations outlined in Table 1. If sequence, species, and GO information should be fetched from UniProt,
the only required input is a PPI CSV file containing pairs of UniProt IDs. If not, or if they have been pre-
fetched, they can additionally be provided to the pipeline. For the ILP split + ILP sampling from HCN
configuration (sampling from a pool of high-confidence human negatives), a candidate network is required
as additional input. Generated withseqeralabs/nf-metro.
All analyses were run with our PPI splitting Nextflow pipeline (Figure 1). Given a CSV file with PPIs,
it fetches sequences, taxonomy, and GO annotations from UniProt (UniProt Consortium, 2025), performs
similarity-based splitting of the positives into train/validation/test, samples corresponding negatives (if
requested, in a bias-reducing manner), trains a baseline classifier, and quantifies the remaining biases in the
resulting dataset. Detailed descriptions of all components are provided in Section 4.2 in Methods.
The baseline classifier is a Random Forest classifier trained on mean-pooled, concatenated embeddings pro-
duced by ESM-2-650M, a widely used BERT-style protein language model trained on huge volumes of amino
acid sequences (Lin et al., 2023). It was shown that replacing simpler protein representations with ESM-2
embeddings already improves PPI classifier performance, independent of model architecture (Reim et al.,
2025). For a protein with lengthn, ESM-2-650 produces ann×1280-dimensional embedding. Mean-pooling
overnpreserves global sequence properties such as taxonomy, structural class, enzymatic function, and lo-
calization (Elnaggar et al., 2022), but discards the residue-level information that is crucial to detect binding
sites and binding-site compatibility. Therefore, the baseline classifier is expected to perform at chance level
on an unbiased dataset. Hence, if the baseline is able to successfully separate positives from negatives, its
performance is almost certainly driven by a shortcut rather than by a learned representation of matching
binding sites. In addition to ESM-2, we ran all analyses with embeddings produced by ProtT5 (Elnaggar
et al., 2022), another popular protein language model. Overall, results are similar, as detailed in Appendix B:
The utility of the embedding similarity attribute is comparable, the Ridge regressor detects the biases slightly
better from the ESM-2 embeddings, and the baseline results are slightly better for ProtT5.
We evaluate the five configurations listed in Table 1, which combine three strategies for splitting the positives
with three strategies for sampling the negatives. The splits differ in how strictly they suppress sequence
similarity between training and test data and in how much data they discard in doing so. The samplers differ
in which statistical properties of the positive set they reproduce in the negative set. The last configuration
replaces the pool from which negatives are drawn: instead of sampling from all protein pairs not annotated
3

Table 1: The five configurations evaluated in this study. Positives are either split randomly, assigned using
a similarity-based partitioning of the input proteome (KaHIP,k= 3), or assigned by minimizing data loss
(KaHIP,k= 100+ILP).Negativescanbesampleduniformlyatrandom, bypreservingpositivenodedegrees,
or by minimizing biases using an ILP. The initial candidates for the negatives are either the complement of
the input PPI graph or a pre-computed set of high-confidence negatives (HCN).
Configuration Split of positives Negative sampling Negative pool
Maximally biased Random 80/10/10 Uniform Complement
Similarity-reduced KaHIP,k= 3Degree-preserving Complement
ILP split KaHIP,k= 100+ ILP Degree-preserving Complement
ILP split + ILP sampling KaHIP,k= 100+ ILP ILP Complement
ILP split + ILP sampling
from HCN
KaHIP,k= 100+ ILP ILP High-confidence
negatives
as interacting, it samples from a precomputed set of high-confidence human non-interactors (Ås, 2026), and
is therefore only applicable to the human datasets with canonical UniProt sequences.
Each configuration is evaluated on two test sets: a balanced test set and a realistic test set. The balanced
test set is sampled using the same strategy as the training and validation sets and contains as many negative
samples as positive samples. For the realistic test set, we always sample negatives uniformly and include ten
times as many negatives as positives, reflecting that two arbitrary proteins are far more likely not to interact
than to interact. Comparing the results on the two test sets separates the question of whether a model has
learned anything from the question of whether it remains useful under a realistic class balance. Precision,
F1, MCC, and AUPRC are always worse on the realistic test set than on the balanced one, as these metrics
are sensitive to class imbalance: a tenfold increase in negatives will turn the same false-positive rate into
many more false positives.
Weranalloftheseanalysesonninedatasets, spanningexperimentallycuratedinteractions(HIPPIE,IntAct),
score-channel subsets of STRING, and two structural datasets derived from the PDB (PINDER, PDB-
Dimers). Table 2 summarizes their sizes and characteristics, detailed dataset descriptions are provided in
Section 4.1 in Methods.
2.2 Performance under the maximally biased setting
As shown in Figure 2B and Supplementary Table A1, a simple Random Forest baseline can achieve near-
perfect performance in the maximally biased setting, exploiting different shortcuts depending on the dataset.
To identify which ones, we employ the G-AUDIT (Drenkow et al., 2026) bias analysis (Figure 2A), in which
the strongest shortcut candidates are attributes that are both highly detectable from the input and highly
informative about the label. Embedding similarity is highly detectable by construction, since the embeddings
are the input to the detector, so for this attribute, we are only interested in the mutual information, i.e.,
in whether the embedding implicitly encodes important properties of interaction. This does not seem to be
the case.
Topology is the attribute with the strongest detectability across all datasets and, for most of them, also the
highest utility. For a pair of proteins, topology is defined as their average degree ratio, where a protein’s
degree ratio is its positive degree in the training set divided by its total training degree (Chatterjee et al.,
2023). AsFigure2Cshows, positiveandnegativepairsdifferstronglyindegreeforIntAct, HIPPIE,STRING:
human/physical, and STRING-experimental, making them trivially separable by degree alone. These are
also the datasets where topology retains high utility across all splits except the realistic test set, which likely
drives the baseline’s strong performance on them. The shortcut is only available in the maximally biased
setting, because in all other configurations, there is no train-test protein overlap, so it cannot be computed.
These results illustrate the danger of train-test overlap: it allows the model to ignore the input entirely and
still perform well based on protein identity alone (Park & Marcotte, 2012; Bernett et al., 2024; Chatterjee
et al., 2023; Zhou et al., 2025).
4

PDB−Dimers
AUROC
AUPRC
F1
MCC Precision
Recall
Accuracy
0.98
0.98
0.94
0.88 0.95
0.93
0.94
0.98
0.88
0.77
0.76 0.66
0.93
0.95
PINDER
AUROC
AUPRC
F1
MCC Precision
Recall
Accuracy
0.95
0.95
0.88
0.76 0.87
0.89
0.88
0.95
0.74
0.56
0.55 0.41
0.89
0.87
IntAct
AUROC
AUPRC
F1
MCC Precision
Recall
Accuracy
0.88
0.89
0.83
0.58 0.75
0.92
0.79
0.88
0.52
0.37
0.34 0.23 0.92
0.65
HIPPIE
AUROC
AUPRC
F1
MCC Precision
Recall
Accuracy
0.86
0.87
0.80
0.56
0.75
0.84
0.78
0.86
0.48
0.37
0.34 0.24
0.84
0.73
STRING: human, physical
AUROC
AUPRC
F1
MCC Precision
Recall
Accuracy
0.85
0.85
0.77
0.54
0.77
0.78
0.77
0.85
0.47
0.37
0.34 0.25
0.78
0.76
STRING−900
AUROC
AUPRC
F1
MCC Precision
Recall
Accuracy
0.82
0.83
0.74
0.45
0.71
0.77
0.73
0.82
0.45
0.31
0.27 0.19
0.77
0.69
STRING−database
AUROC
AUPRC
F1
MCC Precision
Recall
Accuracy
0.86
0.87
0.78
0.54
0.73
0.84
0.77
0.86
0.49
0.35
0.33 0.22
0.84
0.71
STRING−experimental
AUROC
AUPRC
F1
MCC Precision
Recall
Accuracy
0.83
0.84
0.75
0.50
0.74
0.76
0.75
0.83
0.45
0.35
0.31 0.22
0.76
0.74
STRING−textmining
AUROC
AUPRC
F1
MCC Precision
Recall
Accuracy
0.80
0.81
0.74
0.46
0.72
0.76
0.73
0.80
0.40
0.32
0.28 0.20
0.76
0.71
Balanced
Realistic
Embedding Similarity GO−BP GO−MF GO−CC
Self interactions Same Species Topology Sequence Similarity
0 0.5 1 0 0.5 1 0 0.5 1 0 0.5 1
0.0
0.2
0.4
0.6
0.8
0.0
0.2
0.4
0.6
0.8
Detectability: Ridge Regressor
Utility: NMI(a; y)
Train
Validation
Test (balanced)
Test (realistic)
PDB−Dimers
PINDER
IntAct
HIPPIE
STRING: human, physical
STRING−900
STRING−database
STRING−experimental
STRING−textmining
A
B
C
E F
D
STRING−
900
STRING−
database
STRING−
experimental
STRING−
textmining
PDB−Dimers PINDER IntAct HIPPIE STRING human, physical
0 100 0 100 0 100 0 100
0 10 0 75 0 100 0 100 0 1000
2e+3
0
4e+3
0
3e+3
0
3e+4
0
3e+3
0
5e+4
0
2e+3
0
3e+4
0
2e+3
Degree
Count
Positive
Negative
 STRING−text
STRING
STRING−exp
STRING−DB
STRING−900
HIPPIE
IntAct
PINDER
PDB−Dimers
0.0 0.2 0.4 0.6 0.8
Proportion of self−interactions
Positive
Negative
Train
Validation
Test (balanced)
Test (realistic)
PINDER
IntAct
PDB−Dimers
0.25 0.50 0.75
Proportion of same−species interactions
Positive
Negative
Train
Validation
Test (balanced)
Test (realistic)
GO−CC
GO−BP GO−MF
0.0 0.2 0.4 0.6
0.0 0.2 0.4 0.6
STRING−text
STRING−exp
STRING−DB
STRING−900
STRING
IntAct
HIPPIE
PINDER
PDB−Dimers
STRING−text
STRING−exp
STRING−DB
STRING−900
STRING
IntAct
HIPPIE
PINDER
PDB−Dimers
Jaccard index of the GO sets
Positive
Negative
Test (balanced)
Test (realistic)
Train
Validation
Figure 2: Overview of the maximally biased setting.(caption continued on next page)
5

Figure 2:ABias analysis per attributea. The higher the utility (NMI betweenaand the labely) and
detectability (Spearmanρbetweenaanda pred, predicted by a Ridge regressor from the input), the higher
the shortcut potential fora.BPerformance of the baseline. The realistic test set has 10 times as many
negatives as positives.CDegree distribution of each protein in the positive (orange) vs. the negative
(purple) train set. Degrees cropped at 100 for readability.DRatio of self-interactions/all interactions.E
Ratio of same-species interactions/all interactions.FMean Jaccard indices of the GO terms annotated for
the interaction candidates.(continued)
For the two structural datasets, PDB-Dimers and PINDER, the self-interaction shortcut dominates. Figure
2D shows that 80% of all positive interactions in PDB-Dimers are self-interactions, and roughly 40% in
PINDER. Because negatives are sampled at random and therefore rarely pair a protein with itself, whether
two input proteins are identical becomes both highly detectable and highly predictive of the label (hence,
the strong baseline performance in Figure 2B). The shortcut also contaminates three of the other attributes:
a self-pair is, by construction, same-species, has an embedding cosine similarity of 1, and has a GO Jaccard
index of 1. Sequence similarity is unaffected, because we exclude self-interactions for its computation to be
able to separate the similarity signal from the identity signal. Self-interactions are a real shortcut rather
than an attribute we want to learn because in reality, many proteins never bind copies of themselves, and
most interactions occur between different proteins. Apart from that, the distributional differences between
the PDB and other databases pose a real issue for using the PDB to augment PPI datasets with structural
information. The PDB apparently annotates a very different population of interactions, weighted heavily
toward homo(di)mers rather than hetero(di)mers. This is unfortunate, since with AlphaFoldDB (Varadi
et al., 2024) providing structures for individual proteins and the PDB providing structures for complexes,
structure-informed PPI prediction should be within reach.
Sequence similarity, in contrast, turns out to be a weaker shortcut than prior work would suggest (Hamp
& Rost, 2015; Bernett et al., 2024). Supplementary Figure A1 shows the distribution of the percentage
of identical residues between two positive versus two negative pairs. The negatives have a strong peak at
zero across all datasets, as expected. Among the positives, similar pairs are rare in IntAct and HIPPIE,
somewhat more common in STRING: human/physical and STRING-experimental, and most frequent in
the three other STRING subsets, which is where the attribute also reaches its highest shortcut potential
in Panel A. A reason could be that the STRING-database and STRING-textmining subsets might contain
more paralogs. Gene duplication produces sequence-similar proteins that also tend to share pathway and
complex membership (Pereira-Leal et al., 2007). STRING’s use of homology transfer between organisms and
the name-based nature of text mining might amplify this further (Szklarczyk et al., 2025). While the utility
of sequence similarity stays low throughout, suppressing it between splits nevertheless remains necessary,
because isoforms, modified, or mutated sequences, paralogs, or closely related homologs should not be placed
in different splits if we want to assess whether our model has learned biological mechanisms of binding. This
matters most for the structural datasets, where the same protein occurs in many slightly different variants.
The taxonomy bias previously described by Hallee et al. (2026) is relevant for the three multi-species datasets
IntAct, PDB-Dimers, and PINDER (Figure 2A, E). About 90% of their annotated PPIs occur within the
same species, whereas fewer than 20% of the randomly sampled negative pairs do, resulting in a high
measured utility. Figure 2A further shows that species can be inferred reasonably well from the embeddings
(highly detectable). Inter-species PPIs are, however, biologically possible (e.g., host-virus interactions), and
we would ideally want our model to detect whether two proteins bind based on their sequence or structure,
independent of taxonomy. The taxonomy attribute is therefore an unwanted shortcut that must be corrected
for, as failing to do so distorts the resulting performance estimates (see the IntAct results in Panel B).
Finally, the GO category overlap is especially predictive of STRING-900, STRING-database, and STRING-
textmining, and is also sufficiently detectable from the embeddings to be exploitable. Figure 2F shows that
PPIs in these three subsets are more functionally related than those in the purely experimental sources
(HIPPIE, IntAct, and STRING-experimental) and in STRING: human/physical. This observation makes
sense since the STRING database channel uses pathway and complex annotations (which are functionally
related by design) and the textmining channel identifies protein co-mentions in the literature, which are also
6

more likely to reflect shared biological function or pathway membership (Szklarczyk et al., 2025). Since
STRING-900 aggregates all evidence channels, it inherits the functional enrichment from these two. This
is an important pitfall to keep in mind: intuitively, a user might select only the most confident STRING
interactions to train their model, expecting higher-quality labels to yield more trustworthy results. Instead,
this subset is easier to predict than a purely experimental dataset because of the functional similarity
shortcut, inflating reported performance without reflecting a model’s true ability to detect genuine physical
interactions.
2.3 Similarity-reduced versus ILP-based splitting
The similarity-reduced split previously proposed by Bernett et al. (2024) has two practical drawbacks: It
offers no control over the sizes of the resulting training, validation, and test sets, and, because it partitions
the entire proteome before assigning PPIs to splits, a large number of interactions are discarded because
their endpoints are part of different blocks. We therefore formulate splitting as an ILP that minimizes the
data loss while enforcing specified train/validation/test fractions. Figure 3A shows how the ILP-based split
fulfills the specified 80/10/10 split while retaining substantially more interactions for training. For PDB-
Dimers and PINDER specifically, overall data loss always remains low due to the self-interactions. Because
a self-interaction has both endpoints in the same cluster, it can never be split apart.
Figure 3B shows that both the similarity-reducing and ILP-based approaches successfully reduce sequence
similarity between the training and test sets. The similarity-reducing approach produces more dissimilar
splits than the ILP approach because atk= 3, KaFFPa directly minimizes the edge cut among the three
groups, which later form the splits. Withk= 100, similarity is minimized between 100 clusters, and the ILP
then regroups them into three splits according to data loss alone, so a test cluster can still be rather similar
to a train cluster. To limit this, we apply CD-HIT-2D to remove any validation or test PPI whose interactors
have more than 40% identity to a training sequence, indicated by the dotted line (see Supplementary Figure
A2 for the proportion of discarded PPIs).
Figure 3C and Supplementary Table A1 shows the effect on the Random Forest baseline. The goal is to
obtain chance-level performance, i.e., an AUPRC of 0.5 on the balanced set and roughly 0.09 on the realistic
test set. HIPPIE, STRING-experimental, and STRING-textmining come closest, falling from 0.81 to 0.87
balanced AUPRC in the maximally biased setting to between 0.54 and 0.59 in both settings. The AUPRCs
of IntAct, STRING: human/physical, STRING-database, and STRING-900 remain slightly inflated at 0.60-
0.71 (before, 0.83-0.89). The performance on the structural datasets PDB-Dimers and PINDER remains
high (0.95-0.99) due to the self-interaction shortcut, which cannot be removed by the splitting strategy. The
splitting strategy also cannot remove the taxonomy shortcut in IntAct, and the GO overlap shortcut in
STRING-900 and STRING-database. All three come from distributional differences between the positives
and the negatives, so addressing them requires intervening on the negatives.
2.4 Controlled bias-reduction through the ILP-based negative sampling
To further mitigate the biases we identified through the G-AUDIT analyses (degree shortcut, GO overlap
shortcut, self-interaction shortcut, and taxonomy shortcut), we developed a bias-minimizing ILP-based neg-
ative sampler that jointly minimizes the underlying distributional differences between sampled negatives
and positives (ILP split + ILP sampling configuration). The ILP proves optimality for every dataset and
split, so any residual bias stems from properties of the negative pool. Overall, this configuration yields
the least-biased datasets. Compared to the ILP split configuration, most attributes now carry less mutual
information (Figure 4A). Figure 4B shows the composition of the remaining objective value, which sums up
the bias terms for self-interactions, taxonomy, degree, and mean GO-BP Jaccard overlap. PDB-Dimers and
PINDER reach much higher residual objectives than the other datasets.
Importantly, the terms are not independent. For the structural datasets PDB-Dimer and PINDER, the
self-interaction deviation is the largest remaining bias term that cannot be minimized further, because a
negative self-interaction can only be sampled for a protein without a positive one. Both datasets, however,
contain positive self-interactions for the majority of the covered proteins, making it impossible for the ILP-
based negative sampler to match the numbers of positive and negative self-interactions. The problem is
7

A
B
C
Max % identity to any training protein
Cumulative fraction of held−out proteins
Maximally biased
Similarity−reduced
ILP split
ILP split +
ILP sampling
0.540.56
0.87 0.59
0.67 0.55
0.89 0.71
0.60 0.53
0.85 0.62
0.64 0.55
0.83 0.66
0.70 0.58
0.87 0.64
0.570.54
0.84 0.56
0.560.54
0.81 0.58
0.98 0.77
0.950.96
0.99 0.77
0.980.94
0.5 0.60.7 0.80.9 1.0
AUPRC
Balanced
0.170.10
0.480.15
0.260.10
0.520.23
0.130.09
0.470.18
0.150.13
0.450.15
0.210.11
0.490.17
0.100.08
0.450.11
0.140.12
0.400.15
0.880.26
0.740.84
0.950.58
0.880.72
STRING−textmining
STRING−database
STRING−experimental
STRING−900
STRING: human, physical
HIPPIE
IntAct
PINDER
PDB−Dimers
0.25 0.50 0.75 1.00
AUPRC
Realistic
Maximally biased Similarity−reduced ILP split ILP split + ILP sampling
STRING−900 STRING−database STRING−experimental STRING−textmining
PDB−Dimers PINDER IntAct HIPPIE STRING: human, physical
0 25 50 75 100 0 25 50 75 100 0 25 50 75 100 0 25 50 75 100
0 25 50 75 100
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
n:38,758
ntrain:31,006
34,791
13,928
37,883
30,455
135,398
108,318
87,959
34,692
119,369
97,981
1,082,410
865,928
415,527
184,510
547,981
457,486
1,179,347
943,478
439,150
199,408
591,345
478,805
644,121
515,297
257,787
132,753
359,641
291,269
37,417
29,934
17,397
6,797
25,843
20,898
414,964
331,971
157,728
70,756
212,563
172,062
90,961
72,769
41,660
14,913
62,328
50,460
105,728
84,582
51,214
18,648
65,364
52,820
PDB−Dimers PINDER IntAct HIPPIE STRING human, physical STRING−900 STRING− experimental STRING− database STRING− textmining
Maximally
biased
Similarity−
reduced
ILP split
Train Validation Test (balanced or realistic)
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
n:
ntrain:
Figure 3: Comparison of the similarity-reduced and the ILP-based settings.AResulting dataset sizes for the
positives only.BMaximum percentage identity (BLAST output) of proteins in the test set to proteins in the
respective training set. The dotted line indicates 40% identity, the threshold for CD-HIT-2D.CPerformance
of the Random Forest classifier. The dotted line indicate the chance performance (0.5and1/11).
made worse by the split, since self-interactions are never discarded, which raises their share in the smaller
splits. In PDB-Dimers, they make up more than 90% of validation and test interactions; in PINDER, this
imbalance is only that severe in the test set (88%), which is correspondingly where its self-interaction bias is
8

A
B
Embedding SimilaritySequence SimilaritySame Species
PDB−Dimers PINDER IntAct HIPPIE STRING human, physical STRING− 900 STRING− experimental STRING− database STRING− textmining
Train ValidationTest (bal.)Test (real.)
ILP Split
ILP Split +sampling
ILP Split
ILP Split +sampling
ILP Split
ILP Split +sampling
ILP Split
ILP Split +sampling
ILP Split
ILP Split +sampling
ILP Split
ILP Split +sampling
ILP Split
ILP Split +sampling
ILP Split
ILP Split +sampling
ILP Split
ILP Split +sampling
0.00
0.25
0.50
0.75
0.00
0.25
0.50
0.75
0.00
0.25
0.50
0.75
0.00
0.25
0.50
0.75 NMI(a; y)
Self interactions GO−BP GO−MF GO−CC
STRING−
900
STRING−
database
STRING−
experimental
STRING−
textmining
PDB−Dimers PINDER IntAct HIPPIE STRING human, physical
Train Val. Test (bal.) Train Val. Test (bal.) Train Val. Test (bal.) Train Val. Test (bal.)
Train Val. Test (bal.)
0.0
0.5
1.0
1.5
2.0
2.5
0.0
0.5
1.0
1.5
2.0
2.5Objective value
Degree
Self interactions
Taxonomy
GO−BP Jaccard index
Figure 4: Influence of ILP-based negative sampling.ADecrease in normalized mutual information from
the ILP-based split (+degree-preserving random sampling) to the ILP-based split + ILP-based sampling.B
Composition of the remaining objective value of the ILP-based negative sampling. The same species term
was only included for PDB-Dimers, PINDER, and IntAct.
the highest. The failure to satisfy the self-interaction term propagates to the GO-BP term since any negative
sampled for a protein with only self-interactions will contribute a lower Jaccard index to the negative mean.
For the taxonomy term, which matches the number of interactions per taxon pair, the residual in PDB-
Dimers and PINDER is driven mainly by human-human interactions. Human proteins account for roughly
a quarter of all proteins in both datasets, so negatives are disproportionately likely to be drawn from human
proteins (up to3.7times more negative human-human interactions). The remaining bias is distributed across
rare taxon combinations, which the logarithmic weighting penalizes more heavily. In IntAct, human-human
pairs account for the vast majority of positives, so a small relative mismatch (around 1.25–1.27 times the
target) leads to a nontrivial absolute contribution.
9

For STRING-900 and STRING-database, GO-BP overlap is the largest remaining bias term. Figure 4A
shows that the mutual information between the GO categories and the label is reduced but not eliminated,
most likely because functionally similar pairs are more likely to already be annotated as interacting in
STRING-database, leaving few functionally related candidates available as negatives. For HIPPIE, STRING:
human/physical, STRING-experimental, and STRING-textmining, all four terms are reduced to near zero,
though their bias was low to begin with.
Returning to the baseline results in Figure 3C and Supplementary Table A1, ILP-based sampling yields the
lowest performance on every dataset except HIPPIE’s balanced test set, where it is marginally higher than
the ILP split alone (0.56against0.54). For all datasets except PDB-Dimers and PINDER, balanced AUPRC
now falls between0.53and0.58, and realistic AUPRC between0.08and0.13. Looking at the complementary
performance metrics (Supplementary Table A1), the reason is that the baseline can no longer distinguish
between positives and negatives and defaults to predicting positive.
2.5 The influence of high-confidence negatives
All configurations so far draw negatives from the complement of the PPI graph, which conflates untested
pairs with genuine non-interactors. We assess the consequences of sampling negatives from a precomputed
set of high-confidence human negatives (HCN) by constructing them from IntAct pairs of human proteins
that were tested together at least 3 times but were never reported to interact (Ås, 2026). Figure 5A shows
that performance on the balanced test set increases substantially for all STRING datasets, from0.53-0.58
to0.62-0.66. This is unlikely the result of higher-quality negatives improving the baseline’s ability to learn
interaction features, since performance on the realistic dataset remains at chance level. Instead, it points to
a distributional difference between the HCN and the positives that cannot be sampled away by choosing a
suitable subset.
Thebiastermsoftheresidualobjectivevalue(Figure5B)supportthisinterpretation, astheresidualobjective
term increases across all datasets. The degree term rises for most of them, consistent with the HCN set
spanning only13 557unique proteins (Table 2), which is too few to satisfy the degree constraint for many
proteins. The self-interaction term is negligible throughout, as expected.
The most substantial issue is in the GO-BP term, which appears for HIPPIE, STRING: human/physical,
and STRING-experimental, where it was previously near zero, and worsens for the remaining subsets. This
makesbiologicalsense, sinceproteinpairsconfirmednottointeractarelesslikelytosharebiologicalprocesses,
making it infeasible to sample the GO-BP bias away. Indeed, only around5%of the 25 million HCN pairs
have a GO-BP Jaccard index greater than 0, and for only1.5%is it greater than 0.1. HIPPIE is not affected
because its positives are not strongly functionally enriched to begin with. When drawing negatives from a
high-confidence set, one should therefore consider which distributional shifts this introduces and whether
they are desirable.
3 Discussion
We show that the splitting strategy and the negative sampling approach substantially affect which shortcuts
a PPI prediction model can exploit, and that the magnitude of these shortcuts varies across databases. A
Random Forest baseline trained on protein embeddings can reach near-perfect performance under a naive
random split. While removing the train-test protein overlap and minimizing inter-split sequence similarity
are effective countermeasures, several datasets retain strong shortcuts because of distributional differences
between the positive and negative sets: for the PDB-derived datasets, the high number of self-interactions
is the largest issue. For multi-species datasets, intra-taxon pairs are less likely to be sampled, but taxonomy
can be inferred well from embeddings. Finally, the STRING subsets that use database annotations and
text mining annotate pairs that are more functionally enriched than expected by chance, which can also
be detected sufficiently well from the embeddings. We jointly align these distributions using an ILP-based
negative sampler. It decreases the baseline to chance level across all datasets except PDB-Dimers and PIN-
DER, where the self-interaction bias cannot be minimized any further, since most proteins in these datasets
have positive self-interactions and a negative self-interaction can only be drawn for a protein that does not
10

0.56
0.53
0.55
0.58
0.54
0.54
0.55
0.63
0.63
0.62
0.64
0.66
0.5 0.60.7 0.80.9 1.0
AUPRC
Balanced
0.10
0.09
0.13
0.11
0.08
0.12
0.08
0.09
0.11
0.11
0.07
0.09
STRING−textmining
STRING−experimental
STRING−database
STRING−900
STRING: human, physical
HIPPIE
0.00 0.25 0.50 0.75 1.0
AUPRC
Realistic
ILP−based split and sampling from HCN ILP−based split and sampling
A
B
 HIPPIE STRING human, physical STRING− 900 STRING− database STRING− experimental STRING− textmining
T rain ValidationT est (balanced)
ILP ILP + HCN ILP ILP + HCN ILP ILP + HCN ILP ILP + HCN ILP ILP + HCN ILP ILP + HCN
0.0
0.1
0.2
0.3
0.0
0.1
0.2
0.3
0.0
0.1
0.2
0.3 Objective value
Degree Self interactions GO−BP Jaccard index
Figure 5: Influence of using a pre-defined set of high-confidence negatives for sampling with the ILP.A
Random Forest classifier baseline results.BComposition of the remaining objective values of the ILP-based
negative sampling runs.
already have a positive one. For STRING-900 and STRING-database, a residual functional-relatedness bias
remains because too few functionally related negatives are available to match the positives. For all datasets,
the baseline’s recall is greater than0.8, while its precision is at chance level in the ILP split + ILP sam-
pling configuration (Supplementary Table A1), meaning that it defaults to predicting positive. This is the
expected outcome, since a low-complexity model like our Random Forest baseline without a mechanism to
represent an interface should not be able to separate the classes.
Our results have practical implications for anyone building or evaluating a PPI prediction model. First,
reported performance figures are only interpretable together with the splitting and sampling strategy that
produced them. A high AUPRC on a randomly split, uniformly sampled dataset says little about general-
ization to unseen proteins. Second, the choice of the PPI database matters independently of the modeling
11

approach. The PDB-derived datasets encode a fundamentally different population of interactions, weighted
heavily toward homo(di)mers, which limits their use for augmenting PPI datasets with structural infor-
mation. This imbalance present in the PDB may affect complex structure prediction as well: While Han
et al. (2026) reported high-confidence AlphaFold-Multimer (Evans et al., 2021) predictions for roughly 7% of
23M predicted homodimers, only 0.7% of 7.6M predicted heterodimers were high-confidence. Furthermore,
these high-confidence heterodimers were enriched for homodimer-like properties such as similar chain length
and high inter-chain sequence identity. Third, drawing negatives from a high-confidence pool, while intu-
itively appealing, can introduce or worsen distributional shifts, particularly for the STRING datasets, since
high-confidence negatives tend not to be functionally related. For HIPPIE, which does not suffer from this
distributional bias, baseline results stayed approximately the same. It is, therefore, possible that a model
with the capabilities to grasp the biochemical mechanisms of interactions can benefit from the less noisy
signal of the high-confidence negatives.
Our analyses have several technical limitations: First, the pipeline only supports the ESM-2 and ProtT5
embedding models. Different embedding models may encode taxonomy, degree, or functional information
to varying extents, which can shift detectability and potentially reorder which shortcuts dominate for a
given dataset. Second, our attribute set is not exhaustive, and additional biases, such as protein length or
experimental detection method, may be present; however, more terms can be added to the bias analysis
and the sampler. Third, we quantify detectability using a Ridge regressor. Replacing it with a GPU-based
estimator would reduce the runtime and memory consumption (see Appendix C), while providing a tighter
lower bound on detectability than a simple linear model. Fourth, the sampling ILP is solved over a stratified
candidate pool of four times the positive count rather than over all admissible negatives, because solving
the ILP over the full pool is computationally prohibitive. The returned solution is optimal for the sampled
pool, but a better-matched negative set may exist. Fifth, the high-confidence negatives were derived only
from human IntAct pairs. The same construction could, in principle, be extended across all of IntAct, but
it does not apply to the PDB-based datasets, whose entries often contain modified rather than canonical
sequences, so we cannot assume that a modified sequence behaves like its canonical counterpart with respect
to interactions. Sixth, even our most rigorous mitigation strategy, ILP-based sampling, leaves residual bias
in PDB-Dimers and PINDER, driven by their high proportion of self-interactions. Addressing this fully
would likely require complementary strategies such as positive downsampling or loss reweighting, which we
did not evaluate empirically.
It is also important to note that the functional relatedness (GO overlap) bias attribute we identified via the
G-AUDIT analysis isnot onlya confounder: proteins in the same pathway, cellular component, or complex
genuinely do interact more often, so matching the GO overlap of the negatives to that of the positives
removes real signal along with the artifact. Nonetheless, functional relatedness isalsoa confounder because
it holds at the level of pathways and complexes rather than individual pairs, so it cannot distinguish which
members of a complex actually bind, which is precisely what a PPI model should predict. For this work, we
therefore decided to treat GO overlap as a bias attribute and include it in the objective of our ILP-based
negative sampler.
We release the splitting and bias analysis pipeline as an open tool so that the community can apply the same
bias-aware procedures to their own data. It can be adapted to other pair-input prediction tasks, such as
domain-domain, protein-ligand, or gene-gene interactions, by substituting the similarity definition and the
bias terms. Moreover, specific bias terms can be switched off for negative sampling, e.g., users who decide to
treat GO overlap as signal can simply set the weight of the corresponding component from the ILP objective
of the negative sampler to zero.
An important scope restriction is that this work is not a benchmarking paper: Our focus is to systematically
identify biases in PPI datasets and to provide a pipeline that produces maximally de-biased data splits
for machine learning model training and evaluation. Natural follow-up question are how state-of-the-art
deep learning-based PPI prediction models perform on these de-biased data splits and if they significantly
outperform the Random Forest baseline utilized here. We leave such questions to future work.
Another avenue for future work is to apply our concept of first quantifying existing shortcuts with the G-
AUDIT bias detection framework and then minimizing them through optimization-based negative sampling
12

for problems other than PPI prediction. For instance, we anticipate that it could be valuable in scenarios
such as rare disease diagnosis from biomedical imaging data where there is much more data for healthy
than diseased individuals and where model generalizability may be compromised by shortcuts due to data
provenance or patient demographics. As long as the pool of negative candidates is sufficiently large, the
approach can be extended to any binary classification problem.
4 Methods
4.1 Datasets
We selected datasets that vary along three axes relevant to shortcut formation: species scope, type of
evidence, and detection modality (Table 2). HIPPIE (Alanis-Lobato et al., 2017) and IntAct (Del Toro et al.,
2022) store interactions from dedicated experiments, the former human-only and the latter multi-species.
STRING (Szklarczyk et al., 2025), in contrast, also includes non-experimentally detected interactions, and
we analyze three of its channels separately to isolate their effects. PINDER (Kovtun et al., 2024) and
PDB-Dimers are derived from resolved PDB (Berman et al., 2000) complexes rather than from interaction
assays.
HIPPIE was downloaded fromhttps://hippie-db.net/download/(HIPPIE-current.txt.gz), and IntAct
fromhttps://www.ebi.ac.uk/intact/download/ftpasintact.zip. Most of IntAct’s stored interactions
arebetweenhumanproteins(618 796/1 082 410), followedbyS.cerevisiae(104 961), D.melanogaster(82 382),
Z.mays (50 969), and A.thaliana (41 475). IntAct also contains cross-species interactions, such as M. muscu-
lus–H. sapiens (26 586), R. norvegicus–H. sapiens (5435), or SARS-CoV-2–H. sapiens (4272).
The STRING database is chosen because it also contains interactions that were not experimentally mea-
sured. STRING scores each evidence channel separately and sums the scores into a combined score. A pair
receives a score in theexperimentschannel if it is annotated in an experimental database like IntAct, in the
databasechannel if it appears in pathway or complex databases like Reactome (Ragueneau et al., 2026),
and in thetextminingchannel if the two proteins are co-mentioned in the literature, either through simple
co-occurrence or through NLP analysis. STRING also distinguishes between physical and functional interac-
tions, with functional interactions requiring only shared complex or pathway membership rather than direct
contact, thereby substantially increasing the number of annotated pairs. Out of
(19 311
2
)
= 186 447 705possi-
ble pairwise interactions, STRING stores6 737 427, i.e., approximately every27th possible pair is annotated
as interacting. Because each of these aspects may produce a different bias, we analyze the physical hu-
man network (9606.protein.physical.links.full.v12.0.onlyAB.txt) together with four of its subsets,
selected by combined score and by evidence channel (Table 2). STRING IDs are mapped to UniProt acces-
sions using the STRING ID mapping file (9606.protein.aliases.v12.0.txt), the UniProt secondary-to-
primary accession mapping file (https://ftp.uniprot.org/pub/databases/uniprot/current_release/
knowledgebase/complete/docs/sec_ac.txt), and the UniProt API for resolving ambiguous mappings.
We additionally investigate two structure-inferred datasets, both derived from the PDB, to examine potential
differences between interaction-detection and structure-resolution databases. The first of these datasets,
PINDER, was originally created to benchmark docking algorithms. It defines an interaction as any pair
of chains within a biological assembly whose backbone atoms come within 10 Å of one another, and it
considers all PDB complexes, including those with more than two interacting proteins. We downloaded the
index.parquetfile fromgs://pinder/2024-02/and apply four filters. First, since we retrieve taxonomy
and GO annotations from UniProt, we remove interactions with an undefined UniProt ID, which are typically
small molecules (from2 319 564to2 097 729interactions). Second, the same pair of UniProt IDs can be
annotated repeatedly within one complex, because chains with identical sequences may interact at several
binding sites.3MB8, for instance, is a homo 6-mer forming a ring-like structure, resulting in 12 annotated
Q2HXR2-Q2HXR2interactions in the PINDER dataset. Since chains sharing a UniProt ID can nonetheless
differ in sequence, as in1H5R, where chain B ofP37744carries two point mutations compared to chains
A, C, and D, we deduplicate on PDB ID, UniProt IDs, and chain IDs rather than on UniProt IDs alone
(2 097 729→834 747). Third, we treat interactions as undirected and drop B–A when A–B is also present.
Fourth, we fetch the chain sequences from the RCSB FASTA API to deduplicate on sequence (often chains
13

have identical sequences, e.g., chains A, C, and D in1H5R). This leaves only135 398unique interactions with
sequence, taxonomy, and GO annotations, most of them between human (28 322), yeast (10 263), and E. coli
(5183) proteins. 37% are self-interactions. PINDER is distributed with a predefined split that minimizes
interface similarity between training, validation, and test sets. Since our aim is to characterize the dataset
rather than to benchmark docking, we pool it and apply our own splitting procedure, keeping the procedure
harmonized across all datasets.
We further construct a stricter structure-derived dataset, PDB-Dimers, containing biological assemblies
with exactly two protein-chain instances. We do so to reduce the possibility that an observed inter-
action depends on additional protein chains in a higher-order complex, rather than representing an
interaction that can occur between the two proteins in isolation. We query the PDB for structures satisfy-
ing the following criteria:rcsb_entry_info.selected_polymer_entity_types: Protein (only),
rcsb_assembly_info.polymer_entity_instance_count: 2, andrcsb_struct_symmetry.kind:
Global Symmetry. This yields97 344candidate assemblies. These criteria restrict the polymeric
components of each assembly to exactly two protein chains, while allowing non-polymeric components
such as ligands, cofactors, and ions. We retain such components because they do not constitute additional
polymeric participants and because excluding every assembly containing a non-polymeric component
would substantially reduce the available data (from97 344to22 520structures). We then apply three
sequence-based quality filters, excluding assemblies in which either chain is longer than1250residues
(leaving96 766structures), shorter than50residues (leaving84 504structures), or contains more than15%
unresolved residues (leaving84 464structures). Finally, sequence-identical interaction pairs are removed,
and interactions B-A are dropped when A-B is present, where A and B denote protein chains (leaving38 758
structures).
Both structural datasets use the sequences annotated in the PDB rather than canonical UniProt sequences.
Many PDB entries contain only part of the canonical sequence, either due to modifications or because the
complex was made synthetically and only the peptide of interest was produced. The structural datasets,
therefore, contain considerably more unique sequences than the others (Table 2), and the same underlying
protein recurs in many slightly different forms, which is why suppressing sequence similarity between splits
matters for them even though its measured utility as a shortcut is low (see Results Section).
For ILP-based negative sampling, we additionally use a pool of high-confidence human negatives (Ås, 2026)
derived from the IntAct database (Del Toro et al., 2022). The key idea here is that two proteins are treated
as a high-confidence negative pair if they are repeatedly not reported to interact, even though the same
experiment reports each of them interacting with other proteins, demonstrating that an interaction between
them would have been detected had it occurred. The original network contains99 755 235negatives. From
that, we selected negative candidates that have never been observed and have been tested at least three
times.
4.2 The PPI splitting and bias analysis pipeline
To ensure a fair comparison between datasets by using the same splitting procedure and to provide the
community with a tool for splitting their own PPI datasets in a bias-aware way, we implemented a dedicated
PPI splitting and bias analysis pipeline. The pipeline is implemented in Nextflow (version 26.04). Its steps
and the paths taken by the individual configurations are shown in Figure 1. The only input required for
the pipeline is a CSV file of PPIs given as UniProt accessions (required columns:protein1,protein2).
The pipeline uses these identifiers to query the UniProt API for the amino acid sequences, the taxonomy,
and the GO annotations (Ashburner et al., 2000; Gene Ontology Consortium, 2026) (biological process: BP,
molecular function: MF, cellular component: CC). The fetching step can also query UniParc for retired
annotations and retrieve isoform-specific sequences. The pipeline then offers three strategies for splitting the
positives (Section 4.2.1) and three for sampling the negatives (Section 4.2.2), which can be combined freely.
It then trains and evaluates a Random Forest baseline classifier with ESM-2 or ProtT5 embeddings on the
obtained data split (Section 4.2.3), carries out a bias analysis via the G-AUDIT framework (Section 4.2.4),
and generates an interactive report (Section 4.2.5). The pipeline returns the resulting training, validation,
and test sets with their sampled negatives, the bias metrics computed for each split, the baseline classifier’s
performance, and an interactive report.
14

Table 2: Datasets employed in this study.
Dataset
Name
Version
(down-
loaded)
Unique
PPIs
Unique
sequences
Key Characteristics
HIPPIE
(Alanis-
Lobato
et al.,
2017)
v3.0
(15.07.2026)
1 179 347 29 080Human, experimentally detected PPIs. Provides
confidence scores based on the amount and qual-
ity of the experimental evidence. Aggregated
from various databases.
IntAct
(Del Toro
et al.,
2022)
Jan 2026
(10.01.2026)
1 082 410 120 021Multi-species, experimentally detected PPIs.
Provides detailed information on the PPIs.
STRING:
physical,
human
(Szklar-
czyk et al.,
2025)
v12.0
(16.07.2026)
644 121 17 348Human PPIs scored via different channels. Evi-
dence for physical proximity does not only come
from experiments but also from pathway and
complex databases, literature text mining, and
homology transfer.
STRING-
900
see above37 417 8032High-confidence PPIs subsetted from STRING:
physical, human to only contain PPIs with a com-
bined score≥900.
STRING-
experimental
see above414 964 16 624Subsetted from STRING: physical, human to
only contain PPIs with score>0in the
experimentschannel.
STRING-
database
see above90 961 8744Subsetted from STRING: physical, human to
only contain PPIs with score>0in thedatabase
channel.
STRING-
textmining
see above105 728 12 852Subsetted from STRING: physical, human to
only contain PPIs with score>0in the
textminingchannel.
PINDER
(Kovtun
et al.,
2024)
2024-02
(21.07.2026)
135 398 91 902Structural, multi-species dataset derived from
PDB complexes. A PPI is recorded if the back-
bone atoms of two protein chains are closer to-
gether than10Å. Customized, deduplicated ver-
sion.
PDB-
Dimers
(Berman
et al.,
2000)
15.08.202638 758 44 706Structural, multi-species dataset, explicitly de-
rived from PDB dimers instead of complexes with
more than two protein units, reducing the like-
lihood that an observed interaction depends on
additional polymers.
High-
confidence
negatives
(Ås, 2026)
10.07.202625 059 736 13 557Human protein pairs derived from IntAct that
have been observed not to interact at least three
times, despite it being possible.
4.2.1 Splitting of the positives
Randomsplit.Thefirststrategyisanaiverandomsplit, inwhichPPIsareassignedtotraining, validation,
and test sets at specified fractions without any further constraint. This approach has repeatedly been shown
to produce overly optimistic results because models can memorize proteins seen during training rather
15

than extract binding-relevant features from their sequences (Park & Marcotte, 2012; Hamp & Rost, 2015;
Szymborski & Emad, 2022; Bernett et al., 2024). We include it not as a viable option but as an upper bound
on the performance a baseline can reach when every shortcut is available, against which the mitigations are
measured, and it lets us quantify which biases drive that inflation.
KaHIP split.The remaining two strategies are designed to minimize sequence similarity between splits,
as suggested by Hamp & Rost (2015) and Bernett et al. (2024). To calculate sequence similarities, a
custom BLAST (Altschul et al., 1990) database is created withmakeblastdb(version 2.16.0), using only the
sequences from the proteins occurring in the input CSV. Then,blastpis used for an all-against-all query
(max_hsps1) to weight a similarity graph. Because raw bit scores grow with sequence length, we define a
length-normalized bit score as
bitscorenorm(p,q) = bitscore(p,q) min(length(p),length(q))
which we use in all KaHIP runs. The graph is written in METIS format (Karypis & Kumar, 1997), as this
is the required input format for the KaHIP (Sanders & Schulz, 2013) graph partitioning tool (version 3.25).
For the first similarity-reducing implementation, we follow the gold-standard split approach proposed by
Bernett et al. (2024). For this, we run KaHIP KaFFPa (Karlsruhe Fast Flow Partitioner, solves a Max-
Flow Min-Cut problem) withk= 3to partition the proteome into three parts. Hence, sequence similarity
(edge weights) is minimized among the three resulting blocks. We then sort the input PPIs into their splits,
retaining a PPI(p,q)only if bothpandqare part of the same block (INTRA 0,INTRA 1,INTRA 2). The
largest resulting block is defined as the training dataset, the second-largest as the validation, and the smallest
as the test dataset.
ILP split.Because the KaHIP split discards many inter-block interactions and leaves the user no control
over the resulting split sizes, we implement an adaptation of DataSAIL (Joeres et al., 2025) that formulates
the assignment as an ILP. We first run KaHIP withk= 100, so that the ILP assigns entire similarity clusters
to splits rather than individual PPIs, which strongly reduces the problem size. The underlying assumption
is that proteins in different clusters are dissimilar, so that assigning whole clusters keeps similar proteins on
the same side of the split. However, because KaFFPa minimizes the cut between the100clusters and the
ILP subsequently regroups them into three splits based solely on data loss, two rather similar clusters may
still end up in different splits. We compensate for this with a redundancy-removal step (see below). As in the
KaHIP split, a PPI is retained only if the clusters of both its endpoints are assigned to the same split, and
discarded otherwise. The ILP chooses the cluster-to-split assignment that minimizes this data loss, subject
to each split receiving approximately its target share of the retained data (notation in Table 3)
The constantskii andkij are computed once, up front, from the PPI CSV and the KaHIP cluster assignment,
counting only PPIs in which both endpoints have a sequence and a cluster assignment. A PPI whose
endpoints fall in the same cluster (kii) is never at risk of being discarded. Note that the target fractions
fs refer to shares of retained PPIs, not of proteins.zs,(i,j) is an auxiliary variable linearizing the product
xs,i·x s,j. It is introduced only for cluster pairs that actually have cross-cluster PPIs at stake (P). The
following problem formulation is used to minimize the data loss:
min
x,z
∑
(i,j)∈P
kij·max s
(
xs,i−xs,j
)
s.t.
S∑
s=1
xs,c = 1∀c(C1)
zs,(i,j)≤x s,i, z s,(i,j)≤x s,j, z s,(i,j)≥x s,i +xs,j−1∀s,(i,j)∈P(C2)
(1−ε)f sT(x,z)≤
∑
i
kiixs,i +
∑
(i,j)∈P
kijzs,(i,j) ∀s(C3)
xs,c∈{0,1}, z s,(i,j)∈{0,1}
16

Table 3: Notation used for ILP-based splitting.
Symbol Meaning
Input
PPIs The input PPIs
CSet ofnKaHIP clusters (default:n= 100)
Specified, fixed parameters
SNumber of splits,S= 3(train, val, test)
fs Target fraction of splits,∑S s=1fs = 1
εAllowed fractional deviation fromf s, default0.05
Pre-computed from input
kii Number of PPIs with both endpoints in clusteri
kij,i<jNumber of PPIs with one endpoint in clusteri, the other in clusterj
P{(i,j) :i<j, k ij >0}, the cluster pairs with at least one cross-cluster PPI
Decision variables
xs,c∈{0,1}Clustercis assigned to splits,s= 1,...,S, c= 1,...,n
zs,(i,j)∈{0,1}Clustersi,jare both assigned to splits,s= 1,...,S,(i,j)∈P
For each(i,j)∈P, the corresponding summand of the objective function equalskij if the clustersiandjare
assigned to different clusters and0otherwise. The constraint (C1) assigns every cluster to exactly one split.
(C2) linearizesx s,i·xs,j, the indicator for “the PPIs between clusteriand clusterjare retained because
both clusters landed in splits”. (C3) requires each split to receive at least a(1−ε)fraction of its target
sharef s of the retained PPIs, where
T(x,z) =
n∑
i=1
kii
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
always retained
+
∑
(i,j)∈P
kij
S∑
s=1
zs,(i,j)
is the total number of PPIs retained under the assignment(x,z). The problem is built and solved via
CVXPY (version 1.9.2). A time limit for the solver can be set. If the solver reaches the time limit before
proving optimality, it returns a feasible but possibly suboptimal cluster assignment. For our experiments,
the time limit was set to 2 hours, and the GUROBI solver (version 13.0.2, academic license) was used.
Redundancy removal after similarity-based splits.Since KaFFPa partitions heuristically, and since
the ILP regroups clusters without regard to inter-cluster similarity, neither similarity-based strategy fully
separates the splits by sequence identity. We therefore run CD-HIT-2D (Li & Godzik, 2006) (40% identity,
word size 2) after splitting, for both strategies, and remove a PPI from the validation or test set if either of
its interactors shares≥40%sequence identity with a training sequence.
4.2.2 Sampling of the negatives
Uniformly random sampling.The simplest sampler draws two proteins uniformly at random from those
occurring in the positive set of the respective split. A candidate pair is retained if it does not occur among the
positives. Negative self-interactions are allowed (though unlikely). We use this sampler in two places. First,
together with the random split, it produces the maximally biased setting, in which positives and negatives
differ systematically in degree, since a protein’s positive degree carries no influence on how often it is drawn
as a negative. Second, it generates the realistic test set in every other configuration, in which we sample ten
times as many negatives as positives to reflect that two arbitrary proteins are far more likely not to interact
than to interact. We choose uniform sampling because true negatives are not expected to follow any specific
distribution.
17

Degree-preserving sampling.To prevent a model from separating positives from negatives by degree
alone (Chatterjee et al., 2023), negatives can instead be drawn from a pool in which each protein appears as
often as it does in the positive set. Each protein then receives, in expectation, as many negative as positive
annotations.
ILP-based negative sampling.Topology is not the only shortcut that an uninformed negative sampling
strategy can introduce. The pipeline, therefore, also offers a bias-aware negative sampler that selects neg-
atives by solving an ILP that explicitly matches several statistical properties of the negative set to those
of the positive set. While the ILP can be adapted to include additional or different bias terms, we focus
on up to four sources of potential bias in this study: (i) whether the two sets contain a similar number of
self-interactions, (ii) whether each protein has a similar degree in both sets, (iii) whether the number of
interactions between each (possibly identical) pair of taxa is similar across the two sets, and (iv) whether
interacting proteins have a higher mean GO biological-process Jaccard index than non-interacting proteins.
Candidates are drawn from all protein pairs not present in the positive set, optionally restricted to a user-
supplied candidate network such as the high-confidence negatives. Because the ILP scales quadratically
with the number of candidates, we subsample the pool to a size four times that of the positive network.
Uniform subsampling would frequently render the problem infeasible, since pairs relevant to a given bias
term are rare among all possible pairs and can be missed by chance. We therefore construct the pool by
stratified sampling. If the self-interaction term is active, every protein without a positive self-interaction has
its self-pair included unconditionally. The remaining budget is allocated proportionally across same-species
and cross-species strata, using the same-species fraction of the positive set as the target ratio. Within each
stratum, pairs with a nonzero GO-BP Jaccard index are drawn preferentially, as they would otherwise rarely
appear. If a stratum’s population falls short of its quota, the shortfall is filled from the unrestricted pool.
Throughout, proteins are drawn in proportion to their positive degree rather than uniformly, so that low-
degree proteins are not allotted candidates they cannot use while high-degree proteins receive enough to fill
their larger budgets.
Using the notation introduced in Table 4, we phrase the negative sampling problem as the following ILP:
min
x,u,v,τ,ζ
λself
1
Uself
τ+λ deg
∑
p
1
Udeg
cpup +λ tax
∑
t≤t′
1
Utax
γt,t′vt,t′ +λ jac
1
Ujac
ζ
s.t.
∑
c∈C
xc =n neg (C1)
∑
c∋p
xc ≤(1 +ξ)d + p ∀p(C2)
τ≥s −(x)−s +, τ≥s +−s−(x)(C3)
up≥d− p (x)−d + p, u p≥d + p−d− p (x)∀p(C4)
vt,t′≥m− t,t′(x)−m + t,t′, v t,t′≥m + t,t′−m− t,t′(x)∀t≤t ′ (C5)
ζ≥ 1 nneg ∑ c Jcxc− ¯J +, ζ≥ ¯J +− 1 nneg ∑ c Jcxc (C6)
xc∈{0,1}, u p,vt,t′,τ,ζ≥0
The constantsU self,U deg,U tax, andU jac rescale each bias term into[0,1]by dividing through the worst-case
deviation of the corresponding variable. Because the terms share candidate pairs, no two can attain their
worst case simultaneously, so these constants are upper bounds on the achievable deviation. The weights
λdeg,λ tax,λ self,λ jac ≥0control which terms are active and how strongly they contribute. The dynamic
weightsc p andγ t,t′ down-weight high-degree proteins and common taxon pairs, so that a mismatch on
a rarely observed protein or taxon pair is penalized more heavily than the same absolute mismatch on a
frequent one.
The constraints serve the following purposes: (C1) fixes the number of selected negatives tonneg. (C2)
caps each proteinp’s negative degree at(1 +ξ)times its positive degreed + p . This hard cap is necessary
18

Table 4: Notation used for ILP-based negative sampling.
Symbol Meaning
Input
C Candidate pool of non-interacting protein pairs,|C|=n
Specified, fixed parameters
λself,λ deg,λ tax,λ jac Weights on the individual bias terms
ξ Degree-cap slack, default5
Pre-computed from input
nneg Target number of negatives=npos
Cself⊂C Subset of negative self-interaction candidates
s+ Total number of self-interactions in the positive set
d+ p Degree of proteinpin the positive set (a self-interaction contributes1, not2)
m+ t,t′ Number of PPIs between taxatandt′,t≤t ′ in the positive set ¯J + Mean GO-BP Jaccard index among the positives
cp Dynamic weight reflecting that a low-degree mismatch is worse than a high-degree
mismatch.c p = 1/log(1 +d + p )
γt,t′ Dynamic weight for taxon pairs, analogous tocp.γ t,t′ =
{
1/log(1 +m + t,t′)m + t,t′ >0
1/log 2m + t,t′ = 0
Uself Worst-case value ofτ:max
(
s+,|{(p 1,p 2)∈C:p 1 =p 2}|−s +
)
Udeg
Worst-case value ofup:∑
pcp·max
(
d+ p,|{(p 1,p 2)∈C: (p 1 =p∨p 2 =p)}|−d + p
)
Utax
Worst-case value ofvt,t′:∑
t,t′γt,t′·max
(
m+ t,t′,|{(p 1,p 2)∈C: (p 1∈t∧p 2∈t′)∨(p 1∈t′∧p 2∈t)}|−m + t,t′
)
Ujac Worst-case value ofζ:max
(
¯J +,1− ¯J +
)
Decision variables and dependent variables
xc∈{0,1} Decision variable: candidatec∈Cis selected as a negative
s−(x) Total number of negative self-interactions,s−(x) =∑ c∈Cself xc
d− p (x) Negative degree of proteinp,d− p (x) =∑ c∋pxc
m− t,t′(x) Number of negative PPIs between taxatandt′,m− t,t′(x) =∑ c∈Ct,t′xc
Jc GO-BP Jaccard index of candidatec’s two proteins,Jc∈[0,1]
τ,up,vt,t′,ζ≥0 Auxiliary deviation variables for the self-loop, degree, taxon-pair, and Jaccard-mean
terms
because (C4) only penalizes the aggregate deviation across all proteins. On its own, it cannot prevent a
small number of proteins from absorbing the entire positive/negative degree-mass mismatch. (C3) linearizes
τ=|s −(x)−s +|, matching the number of self-interactions in the negative set to the number in the positive
set, without constraining which specific self-pairs are chosen. Sinceτis minimized in the objective and
bounded below by boths−(x)−s + ands +−s−(x), the solver drivesτto exactly this absolute deviation
at the optimum. (C4) linearizes the per-protein degree deviationup =|d − p (x)−d + p|. (C5) linearizes the
deviationv t,t′ =|m − t,t′(x)−m + t,t′|for each unordered taxon pair(t,t ′), matching the global distribution
of interactions across species pairs independent of which specific proteins are involved. (C6) linearizes
ζ=
⏐⏐ 1
nneg
∑
eJexe− ¯J +⏐⏐, matching the mean GO-BP Jaccard index of the selected negatives to that of the
positives. Unlike (C3)–(C5), which match counts within discrete groups, (C6) matches a continuous statistic
averaged over the entire candidate pool.
19

4.2.3 Training the baseline model
To assess what a simple machine learning baseline can achieve on the resulting data splits, we first compute
sequence embeddings for each protein. The pipeline currently supports ESM-2-650M (Lin et al., 2023) and
ProtT5 (Elnaggar et al., 2022) embeddings, with optional GPU scheduling if specified by the user. Both
models return per-residue embeddings, which we average across residues to obtain fixed-length, per-protein
embeddings.
Using the concatenated embeddings of the two interactors, we train a Random Forest classifier (scikit-learn
v1.9.0) with100trees andmax_samplesset to 0.2. We tune the maximum tree depth over{5,10,30},
selecting the value with the highest AUROC on the validation set. We then report AUROC, AUPR, F1,
MCC, precision, recall, and accuracy on both test sets (balanced and realistic).
4.2.4 Bias analysis
The bias analysis is adopted from the G-AUDIT framework of Drenkow et al. (2026). The authors propose
a way to quantify the extent to which a certain attributeathat is not part of the input dataXcan serve
as shortcut for predicting the output labely. For this, they define two measures: the detectability ofafrom
Xand the utility ofafory, i.e., how informativeais about the label. Only if it is easy to inferafromX
and ifacarries knowledge abouty, the attribute can be considered a shortcut risk.
Whether the attribute is actually a shortcut depends on the attribute and the application case. Returning
to the introductory examples, suppose we want to classify photos of cows, dolphins, and owls. Consider
the attribute “number of green pixels”: it is easy to detect fromX(detectability) and, if most cow photos
happen to be taken in meadows, it is also predictive ofy(utility). Yet this is the kind of shortcut we want to
avoid, since a cow photographed on a beach would confuse the model, revealing that it never really learned
“cow” in the first place. In contrast, the attribute “black-and-white patches in close proximity” would also be
detectable and predictive, but since many cows genuinely do have such patches, this is a legitimate, desired
signal rather than a shortcut.
In Drenkow et al. (2026), utility is measured as the mutual informationMI(a;y) =H(y)−H(y|a). Since
the upper bound ofMIdepends on the entropies of the variables involved, raw values are not comparable
across attributes, so we report the normalized mutual information
NMI(a;y) = MI(a;y)√
H(a)H(y)
,
which is bounded in[0,1]. We computeMI(a;y)with scikit-learn, which directly estimates mutual infor-
mation via ak-nearest neighbors method when a continuous variable is involved, rather than computing
entropies first, soH(y)andH(a)have to be computed separately. Both can be obtained exactly foryand
discretea. For continuousa, we computeH(a)from a 10-bin histogram. SinceMI(a;y)andH(a)are thus
estimated by different methods, their ratio is not guaranteed to stay within[0,1], so we clipNMI(a;y)at
1.0. The reported values are hence not normalized mutual information in the strict sense.
Drenkow et al. (2026) measure detectability by fitting a model to predictafromX. For simplicity, we
use scikit-learn’s Ridge regressor (α= 1.0, stochastic average gradient solver, at most 1000 iterations) on
the concatenated embeddings of the two interactors, and compute the Spearman correlation betweenaand
its predictions. We use the same regressor for the binary attributes as for the continuous ones to keep the
measure comparable across attributes. The regressor is deliberately fit and evaluated on the same data,
since the question is whether the information aboutais present inXat all, not whether a predictor ofa
generalizes. Because the regressor is linear, the reported detectability is a lower bound.
We compute detectability and utility separately for the training set, the validation set, and the balanced and
realistic test sets. This lets us assess whether a shortcut is present in the training data and could therefore be
learned, whether it persists into the validation set and could therefore be reinforced during model selection,
and whether it persists into the test sets and could therefore inflate or bias reported test performance.
We investigate the following attributesa:
20

•Self-interactions: Indicator variable1 p1=p2.
•Same species: Indicator variable1 t1=t2, wheret 1 andt 2 are the taxa annotated forp1 andp 2.
•Functional relatedness measured by GO-BP: The Jaccard index of the GO-BP term setsS1
andS 2 annotated forp 1 andp 2.
•Functional relatedness measured by GO-MF: Analogous to GO-BP.
•Functional relatedness measured by GO-CC: Analogous to GO-BP.
•Sequence similarity: The percentage of identical residues betweenp 1 andp 2 (BLAST output),
normalized to[0,1]. Self-interactions are excluded to separate the similarity signal from the identity
signal.
•Embedding similarity: The cosine similarity between the protein embeddings ofp1 andp 2. Since
the ridge regressor takes the concatenated embeddings as input, this attribute is by construction
always highly detectable.
•Topology: The average degree ratio of the two proteins, where a protein’s degree ratio isr(p) =
d+(p)/(d+(p) +d−(p))(Chatterjee et al., 2023). For a pair, the attribute is the mean of the two
ratios if both proteins occur in training and the ratio of the single occurring protein otherwise.
Pairs in which neither protein occurs in training are excluded, though these are rare in practice,
since the random split leaves almost all proteins represented in the training set. We compute this
attribute only for the maximally biased setting, as all other configurations are constructed to have
no train-test protein overlap, which leaves the attribute without a basis.
4.2.5 Report
In the end, the pipeline renders an interactive, custom MultiQC (Ewels et al., 2016) report by collecting
individual reports from each pipeline step. This includes general statistics such as split sizes, the number of
discarded PPIs, bias analysis plots, classifier performance, ILP residuals, and a sequence similarity heatmap
between the splits as a sanity check.
5 Code and data availability
The code is available athttps://github.com/bionetslab/ppi-splitting-pipeline. All associated data
and results including precomputed dataset splits are available on figshare athttps://doi.org/10.6084/
m9.figshare.33407437.
6 Acknowledgements
The authors would like to thank Pascal Iversen for helpful discussions and feedback. This research was
enabled by the Klaus Tschira Stiftung (KTS, project 00.003.2024).
7 Broader impact statement
All data used here come from public biological databases (UniProt, IntAct, STRING, PDB, Gene Ontology),
which contain reference sequences and annotations rather than individual-level human data, so no personally
identifiable information is involved. The intended benefit is more informative benchmarks, since inflated
results misdirect methodological effort and waste laboratory resources when used to prioritize experimental
validation. The main risk is over-interpretation: treating a dataset as unbiased after a single mitigation, or
reading a chance-level baseline as evidence that the task is unlearnable. A potential indirect risk lies in the
dual-use downstream applications of a PPI prediction model (if it now were to function well enough), where
it could, e.g., predict host-pathogen interactions.
21

References
Gregorio Alanis-Lobato, Miguel A Andrade-Navarro, and Martin H Schaefer. HIPPIE v2.0: enhancing
meaningfulness and reliability of protein-protein interaction networks.Nucleic Acids Res., 45(D1):D408–
D414, 2017. doi: 10.1093/nar/gkw985.
Stephen F Altschul, Warren Gish, Webb Miller, Eugene W Myers, and David JLipman. Basic local alignment
search tool.J. Mol. Biol., 215(3):403–410, 1990. doi: 10.1016/S0022-2836(05)80360-2.
Joel Ås. Dataset for: Towards reconstruction of the human interactome from positive and negative experi-
mental evidence.Zenodo, 2026. doi: 10.5281/zenodo.22675356.
M Ashburner, C A Ball, J A Blake, D Botstein, H Butler, J M Cherry, A P Davis, K Dolinski, S S Dwight,
J T Eppig, M A Harris, D P Hill, L Issel-Tarver, A Kasarskis, S Lewis, J C Matese, J E Richardson,
M Ringwald, G M Rubin, and G Sherlock. Gene Ontology: tool for the unification of biology.Nat. Genet.,
25(1):25–29, 2000. doi: 10.1038/75556.
Sara Beery, Grant Van Horn, and Pietro Perona. Recognition in terra incognita. In Vittorio Ferrari, Martial
Hebert, Cristian Sminchisescu, and Yair Weiss (eds.),15th European Conference on Computer Vision
(ECCV 2018), volume 11220 ofLecture Notes in Computer Science, pp. 472–489. Springer, 2018. doi:
10.1007/978-3-030-01270-0_28.
Asa Ben-Hur and William Stafford Noble. Choosing negative examples for the prediction of protein-protein
interactions.BMC Bioinformatics, 7 Suppl 1(S1):S2, 2006. doi: 10.1186/1471-2105-7-S1-S2.
Helen M Berman, John Westbrook, Zukang Feng, Gary Gilliland, Talapady N Bhat, Helge Weissig, Ilya N
Shindyalov, and Philip E Bourne. The Protein Data Bank.Nucleic Acids Res., 28(1):235–242, 2000. doi:
10.1093/nar/28.1.235.
Judith Bernett, David B Blumenthal, and Markus List. Cracking the black box of deep sequence-based
protein-protein interaction prediction.Brief. Bioinform., 25(2):bbae076, 2024. doi: 10.1093/bib/bbae076.
Ayan Chatterjee, Robin Walters, Zohair Shafi, Omair Shafi Ahmed, Michael Sebek, Deisy Gysi, Rose
Yu, Tina Eliassi-Rad, Albert-László Barabási, and Giulia Menichetti. Improving the generalizability
of protein-ligand binding predictions with AI-bind.Nat. Commun., 14(1):1989, 2023. doi: 10.1038/
s41467-023-37572-z.
Jeffrey Dastin. Amazon scraps secret AI recruiting tool that showed bias against women. In Kirsten
Martin (ed.),Ethics of Data and Analytics, pp. 296–299. Auerbach Publications, 2022. doi: 10.1201/
9781003278290-44.
Noemi Del Toro, Anjali Shrivastava, Eliot Ragueneau, Birgit Meldal, Colin Combe, Elisabet Barrera, Livia
Perfetto, Karyn How, Prashansa Ratan, Gautam Shirodkar, Odilia Lu, Bálint Mészáros, Xavier Watkins,
Sangya Pundir, Luana Licata, Marta Iannuccelli, Matteo Pellegrini, Maria Jesus Martin, Simona Panni,
Margaret Duesbury, Sylvain D Vallet, Juri Rappsilber, Sylvie Ricard-Blum, Gianni Cesareni, Lukasz
Salwinski, Sandra Orchard, Pablo Porras, Kalpana Panneerselvam, and Henning Hermjakob. The IntAct
database: efficient access to fine-grained molecular interaction data.Nucleic Acids Res., 50(D1):D648–
D653, 2022. doi: 10.1093/nar/gkab1006.
Nathan Drenkow, Mitchell Pavlak, Keith Harrigian, Ayah Zirikly, Adarsh Subbaswamy, Mohammad Mehdi
Farhangi, NicholasPetrick, andMathiasUnberath. DetectingdatasetbiasinmedicalAIusingageneralized
and modality agnostic auditing approach.NPJ Digit. Med., 2026. doi: 10.1038/s41746-026-02807-y.
Ahmed Elnaggar, Michael Heinzinger, Christian Dallago, Ghalia Rehawi, Yu Wang, Llion Jones, Tom Gibbs,
TamasFeher, ChristophAngerer, MartinSteinegger, DebsindhuBhowmik, andBurkhardRost. ProtTrans:
Toward understanding the language of life through self-supervised learning.IEEE Trans. Pattern Anal.
Mach. Intell., 44(10):7112–7127, 2022. doi: 10.1109/TPAMI.2021.3095381.
22

Richard Evans, Michael O’Neill, Alexander Pritzel, Natasha Antropova, Andrew Senior, Tim Green, Au-
gustin Žídek, Russ Bates, Sam Blackwell, Jason Yim, Olaf Ronneberger, Sebastian Bodenstein, Michal
Zielinski, Alex Bridgland, Anna Potapenko, Andrew Cowie, Kathryn Tunyasuvunakool, Rishub Jain, Ellen
Clancy, Pushmeet Kohli, John Jumper, and Demis Hassabis. Protein complex prediction with AlphaFold-
multimer.bioRxiv, 2021. doi: 10.1101/2021.10.04.463034.
Philip Ewels, Måns Magnusson, Sverker Lundin, and Max Käller. MultiQC: summarize analysis results for
multiple tools and samples in a single report.Bioinformatics, 32(19):3047–3048, 2016. doi: 10.1093/
bioinformatics/btw354.
Robert Geirhos, Jörn-Henrik Jacobsen, Claudio Michaelis, Richard Zemel, Wieland Brendel, Matthias
Bethge, and Felix A Wichmann. Shortcut learning in deep neural networks.Nat. Mach. Intell., 2(11):
665–673, 2020. doi: 10.1038/s42256-020-00257-z.
Gene Ontology Consortium. The Gene Ontology knowledgebase in 2026.Nucleic Acids Res., 54(D1):D1779–
D1792, 2026. doi: 10.1093/nar/gkaf1292.
Logan Hallee, Tamar Peleg, Nikolaos Rafailidis, and Jason P Gleghorn. Protein language models are acci-
dental taxonomists.BMC Bioinformatics, 27(1), 2026. doi: 10.1186/s12859-026-06491-3.
Tobias Hamp and Burkhard Rost. More challenges for machine-learning protein interactions.Bioinformatics,
31(10):1521–1525, 2015. doi: 10.1093/bioinformatics/btu857.
Yewon Han, Maxim I Tsenkov, Niccolò A E Venanzi, Sooyoung Cha, Nilkanth Patel, Sreenath Nair, Razan
Abbara, Damian Bertoni, Alejandro Chacón, Nick Dietrich, Boris Fomitchev, Yonathan Goldtzvik, Darren
Hsu, Jeannie Austin, Joseph Ellaway, Kieran Didi, Gyuri Kim, Hyunbin Kim, Oleg Kovalevskiy, Dariusz
Lasecki, Agata Laydon, Micha Livne, Paulyna Magaña, Maciej Majewski, Urmila Paramval, Risha Patel,
Ivanna Pidruchna, Brianda Santini Lopez, Prashant Sohani, Ahsan Tanweer, Duc Tran, Kyle Tretina,
Melanie Vollmar, Quan Vu, Augustin Žídek, Sameer Velankar, Martin Steinegger, Jennifer Fleming, Milot
Mirdita, and Christian Dallago. AlphaFold database expands to proteome-scale quaternary structures.
bioRxiv, 2026. doi: 10.64898/2026.03.27.714458.
Roman Joeres, David B Blumenthal, and Olga V Kalinina. Data splitting to avoid information leakage with
DataSAIL.Nat. Commun., 16(1):3337, 2025. doi: 10.1038/s41467-025-58606-8.
George Karypis and Vipin Kumar. METIS: A software package for partitioning unstructured graphs, parti-
tioning meshes, and computing fill-reducing orderings of sparse matrices. Technical report, University of
Minnesota, 1997. URLhttps://hdl.handle.net/11299/215346.
Daniel Kovtun, Mehmet Akdel, Alexander Goncearenco, Guoqing Zhou, Graham Holt, David Baugher,
Dejun Lin, Yusuf Adeshina, Thomas Castiglione, Xiaoyun Wang, Céline Marquet, Matt McPartlon, Tomas
Geffner, Emanuele Rossi, Gabriele Corso, Hannes Stärk, Zachary Carpenter, Emine Kucukbenli, Michael
Bronstein, and Luca Naef. PINDER: The protein interaction dataset and evaluation resource.bioRxiv,
2024. doi: 10.1101/2024.07.17.603980.
Weizhong Li and Adam Godzik. Cd-hit: a fast program for clustering and comparing large sets of protein
or nucleotide sequences.Bioinformatics, 22(13):1658–1659, 2006. doi: 10.1093/bioinformatics/btl158.
Zeming Lin, Halil Akin, Roshan Rao, Brian Hie, Zhongkai Zhu, Wenting Lu, Nikita Smetanin, Robert
Verkuil, Ori Kabeli, Yaniv Shmueli, Allan Dos Santos Costa, Maryam Fazel-Zarandi, Tom Sercu, Salvatore
Candido, and Alexander Rives. Evolutionary-scale prediction of atomic-level protein structure with a
language model.Science, 379(6637):1123–1130, 2023. doi: 10.1126/science.ade2574.
Stavros Makrodimitris, Marcel Reinders, and Roeland van Ham. A thorough analysis of the contribution of
experimental, derived and sequence-based predicted protein-protein interactions for functional annotation
of proteins.PLoS One, 15(11):e0242723, 2020. doi: 10.1371/journal.pone.0242723.
Yungki Park and Edward M Marcotte. Flaws in evaluation schemes for pair-input computational predictions.
Nat. Methods, 9(12):1134–1136, 2012. doi: 10.1038/nmeth.2259.
23

Jose B Pereira-Leal, Emmanuel D Levy, Christel Kamp, and Sarah A Teichmann. Evolution of protein
complexes by duplication of homomeric interactions.Genome Biol., 8(4):R51, 2007. doi: 10.1186/
gb-2007-8-4-r51.
Eliot Ragueneau, Chuqiao Gong, Pierre Sinquin, Cristoffer Sevilla, Deidre Beavers, Alexander Grentner,
Johannes Griss, Gregory F J Hogue, Nancy T Li, Lisa Matthews, Bruce May, Marija Milacic, Helia
Mohammadi, Robert Petryszak, Karen Rothfels, Veronica Shamovsky, Ralf Stephan, Krishna Tiwari, Joel
Weiser, Adam Wright, Marc Gillespie, Guanming Wu, Lincoln Stein, Henning Hermjakob, and Peter
D’Eustachio. The Reactome Knowledgebase 2026.Nucleic Acids Res., 54(D1):D673–D681, 2026. doi:
10.1093/nar/gkaf1223.
Timo Reim, Anne Hartebrodt, David B Blumenthal, Judith Bernett, and Markus List. Deep learning
models for unbiased sequence-based PPI prediction plateau at an accuracy of 0.65.Bioinformatics, 41
(Supplement_1):i590–i598, 2025. doi: 10.1093/bioinformatics/btaf192.
Amir Rosenfeld, Richard Zemel, and John K Tsotsos. The elephant in the room.arXiv [cs.CV], 2018. doi:
10.48550/arXiv.1808.03305.
Peter Sanders and Christian Schulz. Think locally, act globally: Highly balanced graph partitioning. In
Vincenzo Bonifaci, Camil Demetrescu, and Alberto Marchetti-Spaccamela (eds.),12th International Sym-
posium on Experimental Algorithms (SEA 2013), volume 7933 ofLecture Notes in Computer Science, pp.
164–175. Springer, 2013. doi: 10.1007/978-3-642-38527-8_16.
Martin H Schaefer, Luis Serrano, and Miguel A Andrade-Navarro. Correcting for the study bias associated
with protein-protein interaction measurements reveals differences between protein degree distributions
from different cancer types.Front. Genet., 6:260, 2015. doi: 10.3389/fgene.2015.00260.
Farzan Soleymani, Eric Paquet, Herna Viktor, Wojtek Michalowski, and Davide Spinello. Protein-protein
interaction prediction with deep learning: A comprehensive review.Comput. Struct. Biotechnol. J., 20:
5316–5341, 2022. doi: 10.1016/j.csbj.2022.08.070.
Damian Szklarczyk, Katerina Nastou, Mikaela Koutrouli, Rebecca Kirsch, Farrokh Mehryary, Radja Hachilif,
Dewei Hu, Matteo E Peluso, Qingyao Huang, Tao Fang, Nadezhda T Doncheva, Sampo Pyysalo, Peer
Bork, Lars J Jensen, and Christian von Mering. The STRING database in 2025: protein networks with
directionality of regulation.Nucleic Acids Res., 53(D1):D730–D737, 2025. doi: 10.1093/nar/gkae1113.
Joseph Szymborski and Amin Emad. RAPPPID: towards generalizable protein interaction prediction
with AWD-LSTM twin networks.Bioinformatics, 38(16):3958–3967, 2022. doi: 10.1093/bioinformatics/
btac429.
UniProt Consortium. UniProt: The universal protein knowledgebase in 2025.Nucleic Acids Res., 53(D1):
D609–D617, 2025. doi: 10.1093/nar/gkae1010.
Mihaly Varadi, Damian Bertoni, Paulyna Magana, Urmila Paramval, Ivanna Pidruchna, Malarvizhi Rad-
hakrishnan, Maxim Tsenkov, Sreenath Nair, Milot Mirdita, Jingi Yeo, Oleg Kovalevskiy, Kathryn Tunya-
suvunakool, Agata Laydon, Augustin Žídek, Hamish Tomlinson, Dhavanthi Hariharan, Josh Abrahamson,
Tim Green, John Jumper, Ewan Birney, Martin Steinegger, Demis Hassabis, and Sameer Velankar. Al-
phaFold protein structure database in 2024: providing structure coverage for over 214 million protein
sequences.Nucleic Acids Res., 52(D1):D368–D375, 2024. doi: 10.1093/nar/gkad1011.
John R Zech, Marcus A Badgeley, Manway Liu, Anthony B Costa, Joseph J Titano, and Eric Karl Oermann.
Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs:
A cross-sectional study.PLoS Med., 15(11):e1002683, 2018. doi: 10.1371/journal.pmed.1002683.
Yuanqing Zhou, Haitao Lin, Lianghua Xie, Yufei Huang, Lirong Wu, Stan Z Li, and Wei Chen. Effectiveness
and efficiency: Label-aware hierarchical subgraph learning for protein-protein interaction.J. Mol. Biol.,
437(6):168737, 2025. doi: 10.1016/j.jmb.2024.168737.
24

A Additional results for ESM-2 embeddings
STRING−
900
STRING−
database
STRING−
experimental
STRING−
textmining
PDB−Dimers PINDER IntAct HIPPIE STRING human, physical
0 25 50 75100 0 25 50 75100 0 25 50 75100 0 25 50 75100
0 25 50 75100
0e+00
1e+05
2e+05
3e+05
4e+05
5e+05
0
250000
500000
750000
0
20000
40000
60000
80000
0
250000
500000
750000
0e+00
1e+05
2e+05
3e+05
0
30000
60000
90000
0
20000
40000
60000
0
10000
20000
30000
0
10000
20000
30000
Positive
Negative
Figure A1: Percentage of identical residues (BLAST pident output) between the interaction candidates of
the training datasets.
Table A1: Performance metrics across datasets, splitting strategies, and test sets.
Dataset Category Test set AUROC AUPRC F1 MCC Prec. Rec. Acc.
balanced 0.98 0.98 0.94 0.88 0.95 0.93 0.94Maximally
biased realistic 0.98 0.88 0.77 0.76 0.66 0.93 0.95
balanced 0.94 0.94 0.86 0.75 0.92 0.81 0.87Similarity-
reduced realistic 0.92 0.72 0.57 0.54 0.43 0.81 0.89
balanced 0.99 0.99 0.97 0.95 0.98 0.97 0.97ILP split
realistic 0.99 0.95 0.87 0.86 0.79 0.97 0.97
balanced 0.79 0.77 0.72 0.36 0.62 0.86 0.67
PDB-
Dimers
ILP split +
ILP sampling realistic 0.80 0.58 0.21 0.14 0.12 0.86 0.42
balanced 0.95 0.95 0.88 0.76 0.87 0.89 0.88Maximally
biased realistic 0.95 0.74 0.56 0.55 0.41 0.89 0.87
balanced 0.96 0.96 0.90 0.81 0.92 0.89 0.91Similarity-
reduced realistic 0.96 0.84 0.68 0.66 0.55 0.89 0.92
balanced 0.98 0.98 0.93 0.85 0.92 0.94 0.93ILP split
realistic 0.98 0.88 0.68 0.67 0.53 0.94 0.92
balanced 0.76 0.77 0.71 0.32 0.60 0.87 0.64
PINDER
ILP split +
ILP sampling realistic 0.65 0.26 0.17 0.03 0.09 0.87 0.23
balanced 0.88 0.89 0.83 0.58 0.75 0.92 0.79Maximally
biased realistic 0.88 0.52 0.37 0.34 0.23 0.92 0.65
balanced 0.72 0.71 0.64 0.30 0.66 0.63 0.65Similarity-
reduced realistic 0.71 0.23 0.27 0.18 0.17 0.63 0.66
balanced 0.69 0.67 0.64 0.27 0.64 0.63 0.64ILP split
realistic 0.75 0.26 0.32 0.23 0.22 0.63 0.71
balanced 0.55 0.55 0.64 0.04 0.51 0.85 0.51
IntAct
ILP split +
ILP sampling realistic 0.45 0.10 0.19 -0.03 0.11 0.85 0.19
25

Table A1: Performance metrics across datasets, splitting strategies, and test sets.(continued)
Dataset Category Test set AUROC AUPRC F1 MCC Prec. Rec. Acc.
balanced 0.86 0.87 0.80 0.56 0.75 0.84 0.78Maximally
biased realistic 0.86 0.48 0.37 0.34 0.24 0.84 0.73
balanced 0.59 0.59 0.45 0.13 0.59 0.37 0.56Similarity-
reduced realistic 0.63 0.15 0.22 0.11 0.16 0.37 0.75
balanced 0.55 0.54 0.46 0.07 0.54 0.40 0.53ILP split
realistic 0.63 0.17 0.24 0.13 0.17 0.40 0.75
balanced 0.57 0.56 0.66 0.10 0.52 0.91 0.53
HIPPIE
ILP split +
ILP sampling realistic 0.48 0.10 0.17 -0.01 0.10 0.91 0.17
balanced 0.85 0.85 0.77 0.54 0.77 0.78 0.77Maximally
biased realistic 0.85 0.47 0.37 0.34 0.25 0.78 0.76
balanced 0.62 0.62 0.54 0.16 0.60 0.49 0.58Similarity-
reduced realistic 0.67 0.18 0.24 0.15 0.16 0.49 0.71
balanced 0.60 0.60 0.51 0.14 0.59 0.45 0.57ILP split
realistic 0.61 0.13 0.20 0.09 0.13 0.45 0.67
balanced 0.52 0.53 0.66 0.00 0.50 0.97 0.50
STRING
human,
physical
ILP split +
ILP sampling realistic 0.48 0.09 0.16 -0.02 0.09 0.97 0.11
balanced 0.82 0.83 0.74 0.45 0.71 0.77 0.73Maximally
biased realistic 0.82 0.45 0.31 0.27 0.19 0.77 0.69
balanced 0.68 0.66 0.62 0.27 0.64 0.60 0.63Similarity-
reduced realistic 0.65 0.15 0.22 0.13 0.14 0.60 0.62
balanced 0.66 0.64 0.63 0.23 0.60 0.67 0.61ILP split
realistic 0.66 0.15 0.22 0.14 0.13 0.67 0.57
balanced 0.56 0.55 0.64 0.08 0.52 0.82 0.53
STRING-
900
ILP split +
ILP sampling realistic 0.60 0.13 0.18 0.07 0.10 0.82 0.33
balanced 0.83 0.84 0.75 0.50 0.74 0.76 0.75Maximally
biased realistic 0.83 0.45 0.35 0.31 0.22 0.76 0.74
balanced 0.56 0.56 0.45 0.08 0.55 0.38 0.54Similarity-
reduced realistic 0.57 0.11 0.18 0.06 0.12 0.38 0.68
balanced 0.58 0.57 0.47 0.11 0.57 0.39 0.55ILP split
realistic 0.54 0.10 0.16 0.02 0.10 0.39 0.62
balanced 0.54 0.54 0.67 0.01 0.50 1.00 0.50
STRING-
experimental
ILP split +
ILP sampling realistic 0.42 0.08 0.17 -0.01 0.09 1.00 0.09
balanced 0.86 0.87 0.78 0.54 0.73 0.84 0.77Maximally
biased realistic 0.86 0.49 0.35 0.33 0.22 0.84 0.71
balanced 0.65 0.64 0.54 0.21 0.64 0.47 0.60Similarity-
reduced realistic 0.67 0.17 0.24 0.14 0.16 0.47 0.72
balanced 0.73 0.70 0.59 0.31 0.70 0.51 0.65ILP split
realistic 0.71 0.21 0.26 0.18 0.18 0.51 0.74
balanced 0.59 0.58 0.66 0.11 0.53 0.87 0.54
STRING-
database
ILP split +
ILP sampling realistic 0.55 0.11 0.17 0.04 0.10 0.87 0.24
26

Table A1: Performance metrics across datasets, splitting strategies, and test sets.(continued)
Dataset Category Test set AUROC AUPRC F1 MCC Prec. Rec. Acc.
balanced 0.80 0.81 0.74 0.46 0.72 0.76 0.73Maximally
biased realistic 0.80 0.40 0.32 0.28 0.20 0.76 0.71
balanced 0.59 0.58 0.56 0.13 0.57 0.55 0.56Similarity-
reduced realistic 0.64 0.15 0.21 0.11 0.13 0.55 0.63
balanced 0.58 0.56 0.57 0.11 0.55 0.58 0.56ILP split
realistic 0.63 0.14 0.21 0.11 0.13 0.58 0.60
balanced 0.55 0.54 0.66 0.07 0.51 0.92 0.52
STRING-
textmining
ILP split +
ILP sampling realistic 0.57 0.12 0.18 0.06 0.10 0.92 0.22
27

STRING−
textmining
Similarity−reduced
STRING−
textmining
ILP split
STRING−
experimental
Similarity−reduced
STRING−
experimental
ILP split
STRING−
database
Similarity−reduced
STRING−
database
ILP split
STRING
human, physical
Similarity−reduced
STRING
human, physical
ILP split
STRING−900
Similarity−reduced
STRING−900
ILP split
IntAct
Similarity−reduced
IntAct
ILP split
HIPPIE
Similarity−reduced
HIPPIE
ILP split
PDB−Dimers
Similarity−reduced
PDB−Dimers
ILP split
PINDER
Similarity−reduced
PINDER
ILP split
0 50K 0 50K
0 200K 0 100K 200K 0 20K 40K 0 20K 40K
0 200K 400K 0 200K 0 10K 20K 0 10K 20K
0 500K 0 500K 0 500K 0 500K
0 10K 0 20K 0 20K 40K 0 50K 100K
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Train
Val
Test
Discarded
Kept Discarded (KaHIP/ILP) Discarded (CD−HIT−2D)
Figure A2: Data retained for training, validation, and test by the two suggested splitting approaches vs.
data discarded by them. CD-HIT-2D mostly removes leftover similar interactions in IntAct (22 380in the
similarity-reduced setting,17 951in the ILP split), and PINDER (3096and1838, respectively). For PDB-
Dimers, STRING: human/physical, and HIPPIE, fewer than 1000 interactions are removed, for the others,
fewer than 200.
28

B Results for ProtT5 embeddings
STRING−
database
STRING−
experimental
STRING−
textmining
HIPPIE STRING human, physical STRING− 900
PDB−Dimers PINDER IntAct
ESM−2
ProtT5
ESM−2
ProtT5
ESM−2
ProtT5
0.0
0.2
0.4
0.0
0.2
0.4
0.0
0.2
0.4
Embedding
Utility
Split
Train
Validation
Test (balanced)
Test (realistic)
FigureB1: ComparisonoftheutilityoftheembeddingsimilarityattributeforESM-2versusProtT5. Overall,
the utility is comparable.
STRING−
900
STRING−
database
STRING−
experimental
STRING−
textmining
PDB−Dimers PINDER IntAct HIPPIE STRING human, physical
Self interactions
Same Species
Topology
Sequence Similarity
Embedding Similarity
GO−BP
GO−MF
GO−CC
Self interactions
Same Species
Topology
Sequence Similarity
Embedding Similarity
GO−BP
GO−MF
GO−CC
Self interactions
Same Species
Topology
Sequence Similarity
Embedding Similarity
GO−BP
GO−MF
GO−CC
Self interactions
Same Species
Topology
Sequence Similarity
Embedding Similarity
GO−BP
GO−MF
GO−CC
Self interactions
Same Species
Topology
Sequence Similarity
Embedding Similarity
GO−BP
GO−MF
GO−CC
−0.1
0.0
0.1
0.2
−0.1
0.0
0.1
0.2
Bias
Detectability ESM2 − Detectability ProtT5
Split
Train
Validation
Test (balanced)
Test (realistic)
Figure B2: Comparison of the detectability of the different bias attributes in the maximally biased setting.
The ridge regressor is either applied from concatenated ESM-2 embeddings or concatenated ProtT5 embed-
dings. Overall, biases are more detectable from ESM-2.
29

0.54−0.56
0.56−0.61
0.58−0.67
0.81−0.82
0.58−0.57
0.7−0.64
0.64−0.73
0.87−0.88
0.54−0.57
0.57−0.62
0.56−0.64
0.84−0.84
0.55−0.63
0.64−0.71
0.66−0.82
0.83−0.86
0.53−0.58
0.6−0.64
0.62−0.67
0.85−0.86
0.56−0.55
0.54−0.57
0.59−0.61
0.87−0.87
0.55−0.58
0.67−0.74
0.71−0.73
0.89−0.89
0.77−0.73
0.98−0.9
0.96−0.97
0.95−0.96
0.77−0.8
0.99−0.99
0.94−0.96
0.98−0.98
−0.2 −0.1 0.0 0.1 0.2
AUPRC ESM−2 − AUPRC ProtT5
Balanced
0.09−0.07
0.12−0.11
0.14−0.17
0.15−0.25
0.4−0.41
0.11−0.12
0.11−0.09
0.21−0.18
0.17−0.25
0.49−0.53
0.07−0.07
0.08−0.1
0.1−0.2
0.11−0.2
0.45−0.46
0.11−0.12
0.13−0.16
0.15−0.24
0.15−0.38
0.45−0.5
0.09−0.07
0.09−0.11
0.13−0.21
0.18−0.24
0.47−0.48
0.08−0.08
0.1−0.08
0.17−0.11
0.15−0.17
0.48−0.5
0.1−0.07
0.26−0.28
0.23−0.22
0.52−0.52
0.26−0.24
0.88−0.58
0.84−0.87
0.74−0.76
0.58−0.48
0.95−0.96
0.72−0.8
0.88−0.89
STRING−textmining
STRING−database
STRING−experimental
STRING−900
STRING: human, physical
HIPPIE
IntAct
PINDER
PDB−Dimers
−0.50 −0.25 0.00 0.25 0.50
AUPRC ESM−2 − AUPRC ProtT5
Realistic
ILP split + ILP sampling (HCN) ILP split + ILP sampling ILP split Similarity−reduced Maximally biased
Figure B3: Comparison of the baseline Random Forest classifier results for the ESM-2 versus the ProtT5
embeddings. Overall, ProtT5 results are better.
30

Table B1: Performance metrics across datasets, splitting strategies, and test sets for ProtT5 embeddings
instead of ESM-2 embeddings.
Dataset Category Test set AUROC AUPRC F1 MCC Prec. Rec. Acc.
balanced 0.98 0.98 0.95 0.89 0.96 0.93 0.95Maximally
biased realistic 0.98 0.89 0.79 0.78 0.69 0.93 0.96
balanced 0.95 0.96 0.86 0.76 0.96 0.78 0.87Similarity-
reduced realistic 0.94 0.80 0.69 0.66 0.62 0.78 0.94
balanced 0.99 0.99 0.96 0.92 0.98 0.94 0.96ILP split
realistic 0.99 0.96 0.87 0.86 0.81 0.94 0.97
balanced 0.81 0.80 0.75 0.46 0.67 0.85 0.72
PDB-
Dimers
ILP split +
ILP sampling realistic 0.79 0.48 0.25 0.20 0.14 0.85 0.53
balanced 0.96 0.96 0.90 0.81 0.90 0.90 0.90Maximally
biased realistic 0.96 0.76 0.63 0.62 0.48 0.90 0.90
balanced 0.96 0.97 0.91 0.82 0.92 0.90 0.91Similarity-
reduced realistic 0.96 0.87 0.66 0.65 0.52 0.90 0.92
balanced 0.90 0.90 0.80 0.65 0.88 0.74 0.82ILP split
realistic 0.90 0.58 0.54 0.50 0.42 0.74 0.88
balanced 0.71 0.73 0.67 0.28 0.62 0.72 0.64
PINDER
ILP split +
ILP sampling realistic 0.62 0.24 0.18 0.05 0.10 0.72 0.39
balanced 0.89 0.89 0.82 0.63 0.79 0.86 0.81Maximally
biased realistic 0.89 0.52 0.41 0.40 0.27 0.86 0.77
balanced 0.76 0.73 0.69 0.37 0.68 0.70 0.69Similarity-
reduced realistic 0.74 0.22 0.28 0.23 0.18 0.70 0.68
balanced 0.76 0.74 0.67 0.36 0.69 0.66 0.68ILP split
realistic 0.78 0.28 0.31 0.25 0.20 0.66 0.74
balanced 0.59 0.58 0.63 0.13 0.54 0.76 0.56
IntAct
ILP split +
ILP sampling realistic 0.38 0.07 0.14 -0.09 0.08 0.76 0.18
balanced 0.87 0.87 0.80 0.59 0.78 0.82 0.79Maximally
biased realistic 0.87 0.50 0.40 0.37 0.26 0.82 0.77
balanced 0.60 0.61 0.50 0.15 0.60 0.43 0.57Similarity-
reduced realistic 0.62 0.17 0.21 0.10 0.14 0.43 0.71
balanced 0.57 0.57 0.44 0.10 0.57 0.36 0.55ILP split
realistic 0.56 0.11 0.17 0.04 0.11 0.36 0.67
balanced 0.55 0.55 0.66 0.01 0.50 0.97 0.50ILP split +
ILP sampling realistic 0.45 0.08 0.16 -0.02 0.09 0.97 0.11
balanced 0.61 0.60 0.66 0.09 0.51 0.94 0.52
HIPPIE
ILP split +
sampling (HCN)realistic 0.43 0.08 0.16 -0.07 0.09 0.94 0.10
balanced 0.85 0.86 0.78 0.55 0.78 0.77 0.78Maximally
biased realistic 0.85 0.48 0.39 0.36 0.26 0.77 0.78
balanced 0.66 0.67 0.57 0.22 0.63 0.51 0.61Similarity-
reduced realistic 0.67 0.24 0.24 0.15 0.16 0.51 0.70
balanced 0.65 0.64 0.50 0.20 0.65 0.41 0.59ILP split
realistic 0.66 0.21 0.25 0.16 0.18 0.41 0.77
balanced 0.58 0.58 0.66 0.09 0.52 0.92 0.53ILP split +
ILP sampling realistic 0.52 0.11 0.17 0.01 0.09 0.92 0.17
balanced 0.64 0.68 0.63 0.15 0.56 0.72 0.57
STRING
human,
physical
ILP split +
sampling (HCN)realistic 0.33 0.07 0.13 -0.17 0.07 0.72 0.15
31

Table B1: Performance metrics across datasets, splitting strategies, and test sets for ProtT5 embeddings
instead of ESM-2 embeddings.(continued)
Dataset Category Test set AUROC AUPRC F1 MCC Prec. Rec. Acc.
balanced 0.85 0.86 0.76 0.51 0.74 0.79 0.76Maximally
biased realistic 0.85 0.50 0.35 0.32 0.23 0.79 0.74
balanced 0.81 0.82 0.70 0.45 0.77 0.65 0.72Similarity-
reduced realistic 0.75 0.38 0.29 0.23 0.19 0.65 0.71
balanced 0.71 0.71 0.65 0.30 0.65 0.66 0.65ILP split
realistic 0.69 0.24 0.23 0.14 0.14 0.66 0.60
balanced 0.64 0.63 0.66 0.19 0.56 0.80 0.58ILP split +
ILP sampling realistic 0.64 0.16 0.20 0.10 0.11 0.80 0.40
balanced 0.73 0.73 0.67 0.31 0.64 0.70 0.65
STRING-
900
ILP split +
sampling (HCN)realistic 0.57 0.12 0.18 0.06 0.10 0.70 0.42
balanced 0.83 0.84 0.76 0.51 0.75 0.76 0.76Maximally
biased realistic 0.83 0.46 0.36 0.32 0.24 0.76 0.75
balanced 0.62 0.64 0.54 0.17 0.60 0.49 0.58Similarity-
reduced realistic 0.61 0.20 0.20 0.09 0.13 0.49 0.65
balanced 0.62 0.62 0.55 0.17 0.60 0.51 0.59ILP split
realistic 0.64 0.20 0.23 0.13 0.15 0.51 0.69
balanced 0.56 0.57 0.65 0.05 0.51 0.89 0.52ILP split +
ILP sampling realistic 0.51 0.10 0.17 0.00 0.09 0.89 0.18
balanced 0.56 0.56 0.62 0.07 0.52 0.77 0.53
STRING-
experimental
ILP split +
sampling (HCN)realistic 0.38 0.07 0.14 -0.11 0.08 0.77 0.17
balanced 0.88 0.88 0.80 0.59 0.76 0.85 0.79Maximally
biased realistic 0.88 0.53 0.38 0.36 0.24 0.85 0.75
balanced 0.73 0.73 0.62 0.34 0.72 0.55 0.67Similarity-
reduced realistic 0.72 0.25 0.28 0.20 0.19 0.55 0.75
balanced 0.65 0.64 0.48 0.20 0.65 0.38 0.59ILP split
realistic 0.67 0.18 0.24 0.15 0.18 0.38 0.79
balanced 0.57 0.57 0.64 0.08 0.52 0.82 0.53ILP split +
ILP sampling realistic 0.50 0.09 0.17 0.01 0.09 0.82 0.25
balanced 0.66 0.65 0.66 0.21 0.58 0.76 0.60
STRING-
database
ILP split +
sampling (HCN)realistic 0.57 0.12 0.18 0.05 0.10 0.76 0.37
balanced 0.82 0.82 0.74 0.49 0.74 0.75 0.74Maximally
biased realistic 0.81 0.41 0.34 0.30 0.22 0.75 0.73
balanced 0.69 0.67 0.64 0.27 0.63 0.64 0.63Similarity-
reduced realistic 0.70 0.25 0.24 0.16 0.15 0.64 0.63
balanced 0.61 0.61 0.56 0.16 0.59 0.54 0.58ILP split
realistic 0.65 0.17 0.23 0.13 0.14 0.54 0.67
balanced 0.56 0.56 0.60 0.07 0.52 0.70 0.53ILP split +
ILP sampling realistic 0.54 0.11 0.17 0.03 0.10 0.70 0.38
balanced 0.56 0.57 0.58 0.08 0.53 0.65 0.54
STRING-
textmining
ILP split +
sampling (HCN)realistic 0.37 0.07 0.13 -0.11 0.07 0.65 0.24
C Runtime and resource consumption
The ILP configurations are more expensive than their alternatives. Figure C1 reports wall-clock runtime
and peak memory per pipeline step across the five settings (maximally biased, similarity-reduced, ILP split,
ILP split + ILP sampling from the complement, and ILP split + ILP sampling from the HCN pool) applied
to all datasets using ProtT5 embeddings (results of Appendix B).
32

Data preparation Clustering Positive split Negative sampling Baseline model Quality control
Compute sequence lengths
Collect bias metrics
Sort PPIs
Remove redundant pairs
Similarity heatmap
Random split
Degree−based sampling
Build METIS graph
MultiQC report
KaHIP clustering (k=3)
Train baseline classifier
All−vs−all BLAST
Solve ILP (split)
CD−HIT2D redundancy filter
Compute embeddings
KaHIP clustering (k=100)
Solve ILP (negative sampling)
Bias analysis
0 200 400 600
Wall−clock runtime [min]
0 20 40 60
Peak memory [GB]
Figure C1: Runtime and resources taken up by the individual pipeline steps for all configurations reported
in Appendix B (ProtT5 embeddings).
The bias analysis, solving the ILPs, the KaHIP clustering into 100 clusters (which is only required for the
ILP split), and the embedding computation have the longest runtime. The bias analysis is slow because
of the Ridge regressor, which is fit once per attribute and split. Solving the ILP for the positive split
always reached the 2-hour time limit, so the reported cluster assignments are feasible but not optimal. The
negative-sampling ILP is fast on the small validation and test sets but takes close to6hours on the training
set because it scales quadratically with the candidate pool. This is why we cap the pool at four times the
positive count (here, about2million for the training set), rather than drawing from the full complement
or the full HCN set. The pool is subsampled in a way that makes it possible to find a feasible solution to
the ILP. Depending on the activated bias terms, negative self-interactions are added, pairs with a nonzero
GO-BP Jaccard index are preferred, and taxa and positive degrees are taken into account (for more details,
see Section 4.2.2). The embeddings are generated once for all259 687sequences combined.
Memory consumption is highest for baseline training, which holds the concatenated embeddings of all pairs
in memory, followed by the bias analysis. Both are highest for HIPPIE, IntAct, and STRING, the largest
datasets. All other steps stay below 15 GB. All ILPs were solved with Gurobi under an academic license.
CVXPY supports open alternatives, but these are typically slower on problems of this size, so users without
a commercial solver should expect longer runtimes than those reported here. All analyses ran on a hetero-
geneous SLURM cluster comprising Intel Xeon Gold 6148 (2.40GHz), AMD EPYC 7351, and AMD EPYC
7713 nodes, using conda environments. Embedding generation used an NVIDIA A40 GPU. The pipeline in
all 43 settings (9 datasets in four settings + sampling from the HCN for 7 datasets) completed in about 3
days and 17 hours of wall-clock time given the available concurrency.
33
