---
title: 'MassSpecGym in the Wild: Uncovering and Correcting Evaluation Pitfalls in AI-Driven Molecule Discovery'
url: https://arxiv.org/abs/2606.19624
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Hongxuan Liu
- Roman Bushuiev
- Ivy Lightheart
- Mrunali Manjrekar
- Anton Bushuiev
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.19624
pages: 32
chars: 127288
fetched_at: '2026-11-08T13:27:39+00:00'
kb_version: 1
---

# MassSpecGym in the Wild: Uncovering and Correcting Evaluation Pitfalls in AI-Driven Molecule Discovery

MassSpecGym in the Wild:
Uncovering and Correcting Evaluation Pitfalls in
AI-Driven Molecule Discovery
Hongxuan Liu1,* Roman Bushuiev2,3,* Ivy Lightheart4,* Mrunali Manjrekar1 Anton Bushuiev2,3
Magdalena Lederbauer1 Filip Jozefov2 Yinkai Wang5 Soha Hassoun5 Josef Sivic3
James Taylor4 Runzhong Wang1 David Healey4,† Tomáš Pluskal2,† Connor W. Coley1,†
1Massachusetts Institute of Technology 2Institute of Organic Chemistry and Biochemistry of the Czech
Academy of Sciences 3Czech Institute of Informatics, Robotics and Cybernetics, Czech Technical
University in Prague 4Enveda Biosciences 5Tufts University
Correspondence to:david.healey@enveda.com;tomas.pluskal@uochb.cas.cz;ccoley@mit.edu
* Equal contribution. † Corresponding authors.
Abstract
Reliable benchmarking is critical for developing machine learning models for
tandem mass spectrometry (MS/MS)-based molecule discovery. Subtle issues in
experimental design and model evaluation procedures can degrade the trustwor-
thiness of such benchmarks and lead to erroneous conclusions. We conduct a
thorough review of model evaluation issues in the recent MS/MS machine learning
literature, using the standard MassSpecGym benchmark suite as a case study to
illustrate the impact of these issues. We find evaluation issues in at least 18 of 26
papers reporting MassSpecGym benchmark results in the first year of its adoption.
We isolate three classes of failures: (i) data leakage, (ii) shortcut learning, and
(iii) implementation bugs and metric divergence. Through extensive experimen-
tation and code replication, we quantify the impact of these issues and show how
they corrupt the evaluation standards MassSpecGym was designed to enforce. We
distill our findings into recommendations generalizable to MS/MS challenges,
benchmarks, and custom evaluation setups. We also release MassSpecGym v1.5,
an implementation of our recommendations in the MassSpecGym benchmarking
suite which addresses the failure modes identified in this audit. MassSpecGym v1.5
is publicly available athttps://github.com/pluskal-lab/MassSpecGym.
1 Introduction
Figure 1: Distribution of 34 papers utilizing MassSpec-
Gym, grouped by primary audit outcome. Benchmark-
ing issues are pervasive throughout the first year of
MassSpecGym adoption. Eight papers (gray bar) used
MassSpecGym as a dataset, not as a benchmark.
Machine learning is rapidly advancing the dis-
covery and identification of small molecules
given their tandem mass spectra (MS/MS) [1].
Public benchmarks are central to this progress
because they enable standardized and repro-
ducible comparison across methods. This is
especially important for molecule discovery, as
confirming a novel predicted molecular struc-
ture is difficult without expensive and low-
throughput experiments. [2–4]. As a result,in
silicobenchmarks serve not merely as conve-
nient proxies, but as the main operational inter-
face through which the field measures progress.
Preprint.
arXiv:2606.19624v2  [cs.LG]  29 Oct 2026

When benchmarks are misused, they silently reward shortcut learning, data leakage, and other causes
of overfitting [5–7]. As benchmark-driven development accelerates, it can be unclear to what extent
leaderboard gains reflect genuine progress on the underlying scientific task rather than artifacts
of evaluation. The increasing automation of implementation, model reuse, and hyperparameter
search further raises the standard required of benchmark design: a benchmark must be sufficiently
transparent that optimization against its blind spots does not go undetected [5].
Over the last year, MassSpecGym [ 8] has quickly emerged as the major benchmarking suite for
machine learning in computational metabolomics. MassSpecGym formulates the problem of inferring
molecular structures from tandem mass spectra as a set of standardized machine learning tasks,
including: (i) the spectrum simulation challenge, in which models predict mass spectra from molecular
structures; (ii) the molecule retrieval challenge, in which models identify the most compatible
molecule from a candidate set given an observed mass spectrum; and (iii) thede novogeneration
challenge, in which models generate molecular structures directly from a given mass spectrum.
In this paper, we conduct a systematic audit of the MassSpecGym ecosystem. Across 26 papers
reporting MassSpecGym results in the first year since its introduction, we identify evaluation issues
in at least 18 of them that affect the validity of their conclusions. Our goal is not to critique
individual papers, but to characterize recurring failure modes and quantify their impact under corrected
evaluation conditions. We organize our findings into three categories:
1. Data leakage is more complex than a binary predicate.Data leakage in molecular machine
learning admits a gradient of stringency. Splitting on exact structure matches can yield train–test
splits where the local chemical space around the test set is densely represented in training. The
choice of data splitting criterion encodes a different hypothesis about what generalization in chemical
space means [8]. Beyond training data, we identify leakage introduced by shared components that
participate in training or inference—such as formula predictors or spectral simulators—as well as
data leakage from synthetic data (§4).
2. Retrieval tasks admit strong shortcuts unrelated to spectral reasoning.Even with clean train–
test splits, discrepancies in molecular candidate sets and composition, such as inconsistent SMILES
canonicalization and ranking biases in candidate sets, can enable shortcut learning in retrieval tasks.
This can inflate hit rates (recall) to near-perfect levels without the model ever learning meaningful
spectrum–molecule relationships, or in some cases without any spectral input at all (§5).
3. Metric and implementation divergence propagates silently across codebases.Errors and
implementation inconsistencies in shared encoders, inference scripts, and metric implementations are
often reused unchecked and adopted as convention—collectively drifting from the fair evaluation
standards MassSpecGym was designed to enforce (§6).
For each category, we present controlled experiments quantifying the impact on benchmark conclu-
sions. We distill our findings into recommendations generalizable to mass spectrometry challenges,
benchmarks, and custom evaluation setups. We consolidate the best practices into MassSpec-
Gym v1.51, addressing the failure modes identified in this audit and providing canonical implementa-
tions of state-of-the-art models, standardized implementation of evaluation metrics, and an agentic
workflow for automated auditing and continuous leaderboard maintenance (Table 3) for new methods.
2 Related Work
Benchmark-driven progress and evaluation pitfalls.Benchmark overfitting is a common problem
in machine learning, related to Goodhart’s law: optimization improves the measured objective without
improving the intended one [9]. This has been demonstrated through a broad literature exploring
the misspecification and misuse of ML benchmarks [5–7, 10, 11]. In particular, common evaluation
pitfalls have been characterized in genomics [12], structural biology [13, 14], and small-molecule
machine learning [15, 16].
Benchmarking in MS/MS-based metabolomics.A number of benchmark frameworks have been
proposed over the years for the evaluation of MS/MS-based machine learning models. The Critical
Assessment of Small Molecule Identification (CASMI) competition has run six times since 2012 [17],
but its irregular schedule limits continuous method development. Goldman et al. [18] created the
1https://github.com/pluskal-lab/MassSpecGym
2

MIST-CANOPUS benchmarking set based on GNPS spectra [19], later formalizing it as NPLIB1 [20].
MassSpecGym [8] advanced this direction with comprehensive public data coverage, fixed leakage-
free splits, clearly defined tasks, and standardized metrics.
Several works in recent years have performed assessments of the state of MS/MS machine learning.
These include efforts to summarize recent developments [21], unify baselines [22], compare datasets
and metrics [23], and analyze task formulation [ 24]. Other works have demonstrated the impact
of problematic meta-scores [25], made recommendations for model evaluation best practices [26],
and introduced new evaluation frameworks [ 27, 28]. While these methods focus on individual
model development and benchmarking concerns, we take a broader lens: thoroughly evaluating the
MassSpecGym ecosystem, classifying error modes, and experimentally demonstrating problems. We
identify recurring evaluation problems in papers utilizing MassSpecGym and release a more robust
MassSpecGym v1.5 with concrete benchmarking recommendations.
3 Study Scope and Audit Protocol
Our audit covers the first year of MassSpecGym adoption, targeting papers that report results on
the MassSpecGym benchmark before May 1, 2026. For each paper, we inspect the reported task
setting, data provenance, use of external components, metric definitions, and any publicly available
implementation details or checkpoints.
This paper combines three complementary forms of evidence. First, we conduct a structured literature
and code audit to identify recurring evaluation assumptions and implementation patterns across the
ecosystem. Second, we perform controlled reproductions and ablations to quantify the effect of
design choices such as data splitting criteria, candidate canonicalization, and metric definitions. Third,
we construct targeted stress tests to probe whether published task formulations are susceptible to
adversarial or unintentional learning shortcuts. We focus on recurring failure modes that are both
scientifically consequential and practically auditable from this first year of benchmark adoption.
4 Data Leakage from Pretraining or External Model Components
Data leakageoccurs when information about test examples enters training and inflates evaluation
metrics beyond what true generalization would produce. This is problematic because performance
gains are driven by memorization rather than generalizable chemical reasoning. MassSpecGym
mitigates data leakage by introducing a Maximum Common Edge Subgraph (MCES) [16] distance-
based train–validation–test split that ensures molecules across data partitions are not similar more
than an MCES edit distance of 10. Moreover, it introduces two explicit tracks of competition, one
where formula is assumed to be known (the formula-basedbonuschallenge) and the second where it
is not known (the mass-based challenge).
Data leakage can still occur when models use external pretraining data beyond MassSpecGym. Many
recentde novogenerative models follow an encoder-decoder procedure: an encoder model predicts a
molecular fingerprint given an MS/MS spectrum, and a decoder model generates a molecule given
the predicted fingerprint. Here, we demonstrate a common pattern of MassSpecGym adoption
leading to limited model generalization: using decoders (§4.1) or encoders (§4.2) pretrained on data
overlapping with the MassSpecGym test set, or on synthetic data from simulators that violate the test
structure exclusion. Additionally, we show how models that use chemical-formula-based encoders
leak ground-truth formulas into the mass-based challenges when trained improperly (§4.3).
4.1 Limited Generalization inDe NovoModels Pre-trained to Decode Fingerprints
Many recentde novogeneration methods adopt a pretrained MIST [ 18] spectrum-to-fingerprint
encoder and focus their innovation on the fingerprint-to-molecule decoder. These decoders are
typically trained on large unlabeled molecular datasets with test compounds excluded only by exact
2D InChIKey matches—a much weaker criterion than the MCES ≥ 10 separation that defines
generalization in MassSpecGym. We hypothesize that reported gains are thus largely driven by
memorization of fingerprint–molecule pairs structurally close to the test set.
Experiments.To test this hypothesis, we train a series of molecular decoders [29] on 2.5M molecules
sampled from a curated collection of specialized databases (Appendix A.1), and on datasets of 10M
3

0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
0.00
0.05
0.10
0.15
0.20
n=2
n=59 n=252
n=579
n=886n=831 n=388
Maximum Tanimoto similarity to
encoder and decoder training sets
Top-1 accuracy
(per-compound)
Top-1 accuracy (per-compound)
35000 30000 25000 20000 15000 10000 5000 0
# of excluded structures based on splitting criterion
0.06
0.08
0.10Accuracy
Splitting criterion
1 Tanimoto < 0.6
2 Tanimoto < 0.7
3 Tanimoto < 0.8
4 exclude exact
5 include half
6 include all
Dataset size
2.5 million
10 million
50 million
Metric
Top-1 accuracy (per-spectrum)
Top-10 accuracy (per-spectrum)
Figure 2: Decoder memorization of near-identical MassSpecGym test compounds. Tanimoto similarities were
computed on 2048-bit ECFP4 Morgan fingerprints (radius 2). Further experimental setup details can be found in
Appendix A.1. (a)De novogeneration accuracy correlates with similarity to the encoder and decoder training
sets. Per-compound top-1 accuracy with 95% bias-corrected and accelerated (BCa) bootstrap confidence intervals
(where estimable) is shown across bins of maximum Tanimoto similarity to the union of these sets; n is the
per-bin count. This decoder was trained on the 50M dataset in the “exclude exact” setup. (b) Example of
near-memorization. The ground truth (left) is reproduced perfectly by the model (top right) despite a poor
encoder fingerprint prediction (Tanimoto 0.61). This is achieved by slightly modifying the closest pretraining
molecule (bottom right; Tanimoto 0.98), which differs from the target at a single fingerprint bit that the encoder
predicts correctly. (c) Benchmark sensitivity to data splitting criteria. Top-1 and top-10 accuracies for MolForge
decoders trained on datasets of 2.5M, 10M, and 50M molecules across six splitting criteria.
and 50M molecules sampled from a combined pool of approximately 1B molecules from ZINC20 [30]
and UniChem [31]. For each dataset, we train on six different filtering variants using progressively
stricter dataset splitting criteria based on exact match exclusion and Tanimoto similarity. Each trained
decoder is paired with a MIST encoder and evaluated on the formula-based MassSpecGymde novo
generation benchmark. Full condition definitions, data composition, and numerical results (including
fingerprint specifications used in Tanimoto similarity calculations) are in Appendix A.1.
Figure 2 demonstrates that benchmark performance is heavily influenced by having seen close test
structure analogs (for example, Tanimoto≥0.7 ) in the encoder or decoder training sets. In Figure 2a–
b, we see that accuracy is substantially higher when close structure analogs to test compounds are
seen during training, indicating limited generalization. This is further confirmed in Figure 2c, where
the decoders trained on datasets of 2.5M, 10M, and 50M molecules show varying sensitivity to the
filtering criterion. The 2.5M model shows additional sensitivity to training on close structure analogs
to test compounds, motivating the following recommendation.
Recommendation.When using external pretraining data, we recommend excluding exact test
matches (based on the 2D InChIKey) from all train splits. If making claims about generalization,
any close test structure analogs (for example, Tanimoto similarity2 ≥0.7 or MCES <10 ) should be
excluded as well. We also recommend reporting performance stratified by the same metric between the
test set and any structure in the encoder or decoder training sets (as in Figure 2a). To facilitate model
development, MassSpecGym v1.0 provided an official pretraining dataset of 4M curated molecules
from [32], each at an MCES >2 from every molecule in the MassSpecGym validation or testing set3.
Here, we include two datasets of 2.5M and 50M molecules as official MassSpecGym v1.5 pretraining
datasets, each filtered to exclude structural analogs (Tanimoto similarity≥0.7 ) of any MassSpecGym
2Using the fingerprint details mentioned in Appendix A.6
3https://huggingface.co/datasets/roman-bushuiev/MassSpecGym/blob/main/data/
molecules/MassSpecGym_molecules_MCES2_disjoint_with_test_fold_4M.tsv
4

test molecule4. The official datasets also include the 1B pretraining set used by FRIGID, which
excludes exact 2D InChIKey matches to MassSpecGym/NPLIB1 validation and test molecules5.
4.2 Spectrum-to-Fingerprint Encoders Pretrained on External Data Memorize Test Examples
Spectrum-to-fingerprint models [ 18, 33] play an important role in manyde novogeneration ap-
proaches, and are susceptible to inflated performance due to data leakage or other errors. Spectrum
encoders benefit from auxiliary components like formula-annotation tools, which can greatly aid
formula-conditioned methods; and spectral simulators [34, 35], which can be used for synthetic data
augmentation. Possible issues in these auxiliary components, especially when reproduced from other
sources, require closer scrutiny. For example, we identify a commonly reproduced implementation
error in the MIST encoder and discuss its impact in §6.1.
We focus on the leakage risk of using synthetic spectra generated by forward models such as
GLACIER [36] for spectrum-to-fingerprint training. The leakage risk is twofold. First, the forward
model may have been trained with a data split that is not aligned with the MassSpecGym split, and thus
may have learned spectrum–structure associations for molecules that appear in the MassSpecGym test
set. Second, generating synthetic spectra for test molecules can expose the encoder to test-molecule-
specific representations during training, effectively allowing it to overfit to the test distribution. Data
leakage thus traverses GLACIER’s generative process and spectrum-to-fingerprint encoder training
before surfacing in metrics.
Table 1:Leakage from Synthetic Spectrum Augmentation.
“GLACIER Split” denotes the MassSpecGym partition used to train
GLACIER, while “Augmented Data Source” denotes the molecules
that GLACIER generates synthetic spectra for. Setting 5 reports
MIST performance without synthetic data augmentation. Retrieval
uses the formula-based candidate set (i.e., w/bonus). Inflated results
are marked in gray.
# GLACIER Split Augmented Data Source MIST spec2fp Tanimoto↑ MIST Retrieval Hit rate@1↑
1 MSG Train + Val. + Test MSG-4M + MSG Test 0.475 47.01%
2 MSG Train + Val. + Test MSG-4M 0.449 43.42%
3 MSG Train MSG-4M + MSG Test 0.447 43.16%
4 MSG Train MSG-4M 0.433 40.31%
5 MIST (no augmentation) 0.262 9.57%
Experiments.We train two
GLACIER models: one on the
MassSpecGym training set only,
and the other on the training, valida-
tion, and test sets combined. Each
GLACIER model is then used to
generate synthetic spectra at five
collision energies for all 4 million
molecules in the MassSpecGym v1.0
pretraining dataset,
optionally spiked with MassSpecGym
test-set structures, yielding four syn-
thetic datasets (Table 1). We train four
MIST encoders on the MassSpecGym training set mixed with the respective augmented corpora and
evaluate them on the MassSpecGym test set, measuring spectrum-to-fingerprint Tanimoto similarity
and formula-based retrieval hit rate@1. Full setup and condition definitions are in Appendix A.2.
Among all settings that use synthetic data augmentation, only Setting 4—where a train-split GLACIER
generates augmentation for non-test-set structures with MassSpecGym test-set molecules excluded—
is leakage-free. According to Table 1, the other three settings exhibit varying degrees of performance
inflation. In particular, Setting 1, where GLACIER is trained on all three data splits and generates
test-split augmentation, substantially exceeds both the leakage-free synthetically augmented MIST
performance (Setting 4) and the original MassSpecGym-reported MIST performance (Setting 5).
Leakage from GLACIER’s inference-time augmentation targets and training-time leakage appear to
have comparable effects in this experiment, as Settings 2 and 3 exhibit similar performance inflation
relative to the leakage-free Setting 4.
A related issue arises when augmentation molecules are selected using test-set information, even if
exact test structures are excluded. The MIST encoder used in the earlier FRIGID evaluation was
trained with ICEBERG-generated spectra for PubChem molecules selected to closely resemble the
structures of MassSpecGym test molecules. Although exact test structures were excluded by 2D
InChIKey, this selection still used test-set structural information [37, Appendix B.2.3]. FRIGID arXiv
v2 reported 18.29% top-1 accuracy [38]; the revised evaluation with MIST4M-augreports 9.05%
[37].
4https://huggingface.co/datasets/roman-bushuiev/MassSpecGym/tree/main/data/
molecules
5https://huggingface.co/datasets/roman-bushuiev/MassSpecGym/blob/main/data/
molecules/safe-gpt-v2-train-msg-canopus-val-test-inchikey14-disjoint.txt
5

Recommendation.We encourage developers to leverage simulated data to further scale trainingonly
using simulators that respect the original training data split of the benchmark. Furthermore, synthetic
augmentation should exclude test molecules and should not use test-set structural information to
select the augmentation pool. In §6.1, we release the MIST checkpoints used in Settings 4 and 5,
which are trained with compliant synthetic data and without synthetic augmentation, respectively.
Both checkpoints address the other issues detailed in that section, and we recommend them as the
official off-the-shelf MIST checkpoints.
4.3 Implicit Formula Leakage in the Mass-Based Retrieval Challenge
Beyond trained spectral simulators for data augmentation, formula annotators can also be critical
auxiliary components of elucidation pipelines, as formula knowledge greatly constrains the search
space. While often treated as solved, formula prediction remains challenging in some cases such
as halogenated molecules or molecules with masses above 600 Da. MassSpecGym differentiates
along this axis: the formula-based evaluations provide ground-truth formula as input, and the mass-
based evaluations withhold this information. In the retrieval challenge, this additionally imposes
a constraint on candidate sets where the mass-based track includes candidates consistent with the
observed precursorm/z, while the formula-based track only includes formula-consistent isomers.
Some recent methods assume known chemical formulas yet report evaluations on the mass-based
tracks, leaking ground-truth formula information. Moreover, trained formula annotators that do not
respect the train–test split can leak ground-truth formula information into mass-based evaluations,
mirroring the transitive leakage observed with spectral simulation (§4.2). We evaluate two possible
routes of leakage through a simple filtration experiment and by training MIST-CF [39], a formula
candidate ranker, under varying amounts of test spectrum leakage.
Experiments.We first show a lower bound on the impact of formula leakage in the mass-based
challenge by pruning candidates to those whose chemical formula matches the ground truth and then
selecting one at random. This modification alone improves the random baseline’s hit rate@1 from
0.43% to 12.98% (30× higher; Table 2).
To demonstrate how a contaminated auxiliary formula annotator can influence downstream elucidation,
we next train MIST-CF on the standard MassSpecGym split, a test-only contaminated split, and a
train-and-test contaminated split. The formula accuracies of these models are recorded in Table 8.
Given a set of candidate formulas (we use the SIRIUS mass decomposition algorithm [40]), MIST-CF
ranks the candidate formulas by their agreement with the observed spectrum. We take the top-1
formula prediction on the MassSpecGym test spectra made by the three models to feed to MIST
4M-aug(which requires a molecular formula) to perform retrieval.
Here, the predicted formulas arenotused to filter structure candidates. Full experiment details are in
Appendix A.2.3.
Table 2:Examination of Formula-Prediction Leakage Impact on MIST’s Performance on the MassSpec-
Gym Mass-Based Retrieval Challenge.The first two rows indicate how ground-truth formula filtration
(mirroring the distinct formula-based challenge) can boost random retrieval. The remaining rows highlight
retrieval performance of MIST, which relies on chemical formula, when used with upstream MIST-CF-inferred
formulas. Inflated results are marked in gray. The values in parentheses indicate 99.9% BCa bootstrap confidence
intervals (20,000 resamples).
Method Hit rate@1↑Hit rate@5↑Hit rate@20↑MCES@1↓
Random 0.43 (0.29–0.61)% 2.01 (1.68–2.38)% 7.99 (7.34–8.74)% 30.91 (30.50–31.35)
Random w/ ground-truth formula 12.98 (12.15–13.83)% 39.09 (37.94–40.31)% 71.33 (70.21–72.44)% 12.46 (12.28–12.65)
MIST (MIST-CF top-1 formula) 32.14 (31.04–33.32)% 45.32 (44.08–46.51)% 60.92 (59.69–62.18)% 15.64 (15.27–16.02)
MIST (MIST-CF test-only top-1 formula) 33.55 (32.40–34.72)% 47.85 (46.65–49.15)% 62.12 (60.89–63.41)% 14.75 (14.39–15.12)
MIST (MIST-CF train-and-test top-1 formula) 36.49 (35.25–37.67)% 50.60 (49.39–51.83)% 65.60 (64.45–66.77)% 13.66 (13.32–14.01)
MIST (ground-truth formula) 52.84 (51.53–54.19)% 69.86 (68.69–71.01)% 84.17 (83.26–85.08)% 7.28 (7.03–7.54)
Here, direct or implicit leakage of ground-truth formulas can confer unfair benefits on downstream
models that compete in the mass-based track. Using top-1 formula predictions from MIST-CF trained
on both the training and test sets increases MIST’s hit rate@1 from 32.14% to 36.49%, a gain of
4.35 percentage points (13.5% relative improvement) over the data-safe setup. As an upper bound,
access to ground-truth formulas increases the accuracy of MIST retrieval by 64.4% (from 32.14%
to 52.84%) compared to using the data-safe MIST-CF trained here. Though these experiments only
6

highlight evaluations on the retrieval challenge, the same transitive leakage can also affect thede
novochallenge. As part of MassSpecGym v1.5, we provide the data-safe version of MIST-CF for use
with formula-aware architectures to facilitate comparison to formula-free models.
Recommendation.If ground-truth formulas oftestspectra are made available at inference, results
should be reported under the formula-based track. MassSpecGym v1.5 provides a data-safe MIST-CF
formula annotator for formula-based architectures to compete in the mass-based track, and welcomes
development of improved formula annotation models and strategies.
5 Shortcut Learning by Exploiting Retrieval Candidate Artifacts
The MassSpecGym retrieval task [8] requires a model to identify the correct ground-truth molecular
structure from a candidate set of decoys, given an input MS/MS spectrum. We identify two distinct
candidate-set artifacts that allow models to learn shortcuts and bypass spectral reasoning: SMILES
canonicalization inconsistency (§5.1) and ranking biases (§5.2).
5.1 Shortcut Learning Based on Canonicalization of SMILES Strings
The ground-truth SMILES strings in MassSpecGym originate directly from disparate experimental
repositories (e.g., GNPS [ 19]), which may retain repository-specific formatting conventions. In
contrast, the decoy candidates are uniformly collected from PubChem but canonicalized using
RDKit [41]. This discrepancy introduces a highly discriminative distributional signature. In effect, a
model can succeed by recognizing the one SMILES string formatted differently from the rest, rather
than by learning the intended relationship between a mass spectrum and a molecular structure.
Table 3:Updated Retrieval Performance Leaderboard on the MassSpecGym Retrieval Challenge w/Bonus
(i.e., Chemical Formula Known).The top section presents literature-reported and updated retrieval results.
The subsequent sections isolate these artifact-exploiting methods and report their corrected or spectrum-blind
performance. Problematic results are marked in gray. Models where an internal reimplementation was developed
are marked with a †. Further details of the Nearest Neighbor reproduction are provided in Appendix A.3. Code
for our reproductions is available at https://github.com/harrylaucngd/msms-models. Theauxiliary
datacolumn marks methods that rely on data beyond the MassSpecGym spectrum–molecule pairs. The values
in parentheses indicate 99.9% BCa bootstrap confidence intervals (20,000 resamples).
Method Hit rate@1↑Hit rate@5↑Hit rate@20↑MCES@1↓Auxiliary data
Performance in the Retrieval Task w/ Bonus (i.e., Formula Known)
Random [8] 3.06 (2.64–3.52)% 11.35 (10.60–12.12)% 27.74 (26.52–28.84)% 13.87 (13.70–14.03)✗
Nearest Neighbor† [42] 13.13 (12.30–13.97)% 26.56 (25.49–27.69)% 44.30 (43.14–45.59)% 12.45 (12.28–12.62)✗
DeepSets [8] 4.42 (3.92–4.97)% 14.46 (13.58–15.36)% 30.76 (29.67–31.93)% 15.04 (14.89–15.19)✗
Fingerprint FFN [8] 5.09 (4.57–5.66)% 14.69 (13.83–15.56)% 31.97 (30.86–33.10)% 14.94 (14.79–15.09)✗
DeepSets + Fourier features [8] 6.56 (5.95–7.16)% 16.46 (15.58–17.35)% 33.46 (32.39–34.59)% 14.14 (13.98–14.31)✗
MIST vMassSpecGym [8] (no augmentation) 9.57 (8.88–10.30)% 22.11 (21.10–23.13)% 41.12 (39.98–42.34)% 12.75 (12.59–12.91)✗
JESTR [43] 11.82 (11.03–12.68)% 33.48 (32.33–34.68)% 61.46 (60.21–62.63)% 11.71 (11.54–11.87)✗
MVP [44] 13.96 (13.10–14.82)% 36.88 (35.71–38.02)% 68.12 (67.00–69.26)% 10.36 (10.19–10.53)✗
FLARE [45] 22.66 (21.63–23.74)% 50.00 (48.78–51.22)% 75.15 (74.10–76.22)% 9.00 (8.82–9.18)✗
MIST4M-aug40.31 (39.05–41.47)% 58.87 (57.66–60.06)% 73.02 (71.95–74.11)% 7.62 (7.44–7.82)✓ a
ICEBERG6 [34] (forward model retrieval) 36.18 (34.96–37.32)% 60.70 (59.58–61.86)% 78.83 (77.74–79.78)% 6.61 (6.43–6.79)✗
GLACIER6 [36] (forward model retrieval) 39.47 (38.20–40.65)% 63.50 (62.35–64.66)% 80.46 (79.44–81.41)% 6.53 (6.34–6.72)✗
Exploiting Canonicalization Artifacts (Not Valid Under Corrected Candidate Canonicalization)
(1) DreaMS + ChemBERTa Alignment (inflated) 82.41 (81.46–83.33)% 92.57 (91.91–93.21)% 97.41 (97.00–97.78)% 2.86 (2.70–3.03)✓
(1) DreaMS + ChemBERTa Alignment (corrected) 6.70 (6.09–7.35)% 19.82 (18.89–20.83)% 40.62 (39.44–41.79)% 13.13 (12.97–13.28)✓
(2) Chemformer Two-Stage Retrieval (inflated) 63.89 (62.71–65.03)% 70.52 (69.37–71.70)% 75.86 (74.79–76.89)% 5.39 (5.20–5.60)✓
(2) Chemformer Two-Stage Retrieval (corrected) 7.60 (6.94–8.31)% 19.12 (18.18–20.11)% 39.31 (38.16–40.53)% 13.23 (13.06–13.39)✓
(3) ChemBERTa SMILES Classifier (inflated) 99.66 (99.50–99.79)% 99.84 (99.72–99.92)% 99.99 (99.95–100.00)% 0.05 (0.03–0.07)✓
(3) ChemBERTa SMILES Classifier (corrected) 8.20 (7.53–8.89)% 18.39 (17.38–19.36)% 38.14 (36.96–39.36)% 13.80 (13.64–13.96)✓
Exploiting Other Structure Biases (Spectrum-Blind Stress Test)
(4) PubChem Default Ranking 49.98 (48.72–51.20)% 54.13 (52.93–55.28)% 61.04 (59.83–62.22)% 7.43 (7.22–7.64)✓ b
(5) Ranking by Number of Chiral Atoms 4.88 (4.36–5.44)% 16.85 (15.92–17.79)% 37.86 (36.72–39.09)% 14.4 (14.23–14.56)✗
a The MIST4M-augmodel incorporates 4 million molecules released by MassSpecGym v1.0 which are filtered
to have an MCES distance greater than 2 from MassSpecGym test molecules, with their synthetic spectra during
training (see §4.2). b PubChem default ranking uses the PubChem PUG-REST API’s default return order (see
Appendix A.4).
Experiments.To quantify the magnitude of this shortcut effect, we evaluated several recent ar-
chitectures and constructed an explicit artifact-exploiting baseline (see Appendix A.4 for complete
formulations). Table 3 reports the results. (1) DreaMS + ChemBERTa Alignment: a DreaMS
spectral encoder [46] is aligned with a frozen ChemBERTa molecular encoder [47] via a bidirectional
7

InfoNCE loss; because the ground-truth SMILES strings retain non-canonical syntax while all decoys
are RDKit-canonicalized, the model can achieve over 82% hit rate@1 by matching formatting cues
rather than learning true structure–spectrum correspondence. (2) Chemformer Two-Stage Retrieval:
a frozen Chemformer encoder [48] is paired with a trained spectral encoder via dual-path InfoNCE
for initial re-ranking (Stage 1), followed by a cross-fusion decoder that autoregressively generates
SMILES conditioned on the top-K retrieved candidates and uses them to refine the ranking (Stage 2);
the same canonicalization discrepancy biases from Stage 1 also score true molecules higher, an effect
that cascades into Stage 2 to achieve over 63% hit rate@1. (3) ChemBERTa SMILES Classifier: a
format classifier trained only on SMILES syntax to distinguish query molecules from their retrieval
candidates achieves near-perfect hit rate@1.
Recommendation.Uniform RDKit canonicalization should be enforced across all candidate and
query SMILES before training and evaluation. MassSpecGym v1.5 applies this correction by default.7
5.2 Shortcut Learning via PubChem Ranking Biases
The chemical space of structures with measured MS/MS spectra is inherently non-uniform and
exhibits a distinct distribution from PubChem (or other potential sources of decoys). Ground-truth
molecules are typically common metabolites, widely available standards, or easily synthesizable
compounds. They tend to appear with higher deposition frequency, and may share structural features
that distinguish them from arbitrary entries in candidate pools drawn from compound libraries such
as PubChem. A model can exploit these spurious correlations to retrieve the correct candidate while
ignoring the MS/MS spectrum entirely.
Experiments.To empirically demonstrate shortcut learning from candidate pools, we evaluate
two spectrum-free baselines (Table 3; implementation details are available in Appendix A.4). (4)
PubChem Default Ranking: ranking candidates by PubChem PUG-REST API’s default return order,
ignoring the spectrum entirely, can exceed 49% hit rate@1. (5) Ranking by Number of Chiral Atoms:
a spectrum-blind baseline ranking candidate molecules by the number of chiral centers performs
on par with simple learnable fingerprint prediction baselines. More generally, the distribution shift
between query and candidate PubChem molecules is apparent from the performance of the corrected
baseline (3), which achieves 8.2% hit rate@1 by directly learning the distributional artifacts that
distinguish them.
While the canonicalization artifact can be straightforwardly fixed by enforcing uniform RDKit canon-
icalization across all query and candidate molecules (which we implement in MassSpecGym v1.5),
the ranking bias and spurious correlations between queries and candidates (e.g., num. of chiral atoms)
represent a more profound challenge for the community: molecules with available experimental
spectra for benchmarking are not uniformly distributed across the chemical space of compound li-
braries such as PubChem. Instead, they disproportionately fall into sub-regions comprising molecules
that are more routinely synthesized, characterized, and analyzed. We therefore treat this as an open
evaluation-design question: how should retrieval benchmarks disentangle a model’s true spectral
reasoning capability from shortcut learning over query and candidate molecules?
In structure-based drug design, the fact that property-matched decoys are harder to distinguish from
true binders than random decoys has been discussed for decades [49, 50]. Analogously, in their work
concurrent to this article, Gupta and Skinnider [51] showed that using property-matched decoys for
the MassSpecGym retrieval benchmark reduces the performance of a spectrum-blind baseline model
from competitive to near random. This motivates future benchmarking design in computational
metabolomics to alleviate distribution shifts with property-matched decoy structures.
Recommendation.Authors of new methods should verify that their models do not rely on spurious
correlations between query and candidate molecules—for example, by masking all input MS/MS
spectra with a constant value and confirming that performance degrades accordingly.
6ICEBERG and GLACIER are evaluated on the full MassSpecGym test split, roughly half of which lack
collision energy annotations. We imputed these missing collision energies; details of the annotation pipeline are
given in Appendix A.5.
7https://huggingface.co/datasets/roman-bushuiev/MassSpecGym
8

6 Implementation Bugs and Metric Divergence Undermine Reproducibility
Benchmark failures are not limited to data curation and task design. A subtler class of problems
emerges at evaluation time in the form of implementation bugs and configuration inconsistencies.
These may only be apparent when auditing the code.
As MassSpecGym adoption has grown, its evaluation ecosystem has become increasingly modular:
pretrained encoders are reused as frozen feature extractors, inference scripts are copied across
codebases, and configuration choices made in one project are inherited, often without examination,
by the next. We show that excessive reuse can propagate silent errors. Undocumented default settings
in shared components carry over to downstream methods and inflate their reported performance.
Separately, we show that implementation-level divergence in metric computation—fingerprint radius
or bit length for Tanimoto similarity, stereochemistry handling in InChIKey matching, or threshold
and bound settings for MCES distance—is sufficient to reorder leaderboard rankings when metric
settings differ across models, even with predictions held fixed.
6.1 The MIST Inference Batching Pitfall
MIST [18] has become a widely reused encoder in the MassSpecGym ecosystem, adopted as a feature
extractor by several subsequent works [52, 53]. Our audit found two distinct MIST-related failure
modes: a conventional padding-mask error in batched settings, and a separate checkpoint-provenance
problem in one specific commonly reused MIST model.
6.1.1 Padding Mask Bug in Batched MIST
The original MIST encoder was validated in single-spectrum settings. When inputs are batched,
its attention code as initially published in the MIST and DiffMS codebases mistakenly applied the
raw boolean mask via attn += attn_mask . Padding tokens therefore receive a finite +1 attention
offset rather than being excluded from the softmax, affecting both training and inference with padded
batches.
6.1.2 Unreproducible MIST vDiffMS Checkpoint Affecting Downstream Decoder
Development
Table 4:Comparison of Correct and Problematic MIST + MolForge Performances on the MassSpecGym
de novoGeneration Challenge w/Bonus. † indicates that the method was reimplemented. Problematic results
are marked in gray.
Top-1 Top-10 Encoder
Models and results onde novotask Accuracy↑MCES↓Tanimoto↑Accuracy↑MCES↓Tanimoto↑MIST Tanimoto↑
MIST4M-aug+ MolForge † 3.29% 31.77 0.31 5.65% 16.67 0.40 0.433
MIST vDiffMS + MolForge† (batch size = 1) 10.73% 22.15 0.37 14.48% 17.88 0.41 0.457
MIST vDiffMS + MolForge† (batch size = 24) 31.75% 12.30 0.68 40.55% 9.80 0.74 0.812
The subsequent erroneous MIST vDiffMS checkpoint trained and used for inference as described
in Section 6.1.1 produces fingerprint predictions, at least in batched mode, that are consistent with
patterns of data leakage or contamination; however, we cannot reproduce this inflation from the
documented training recipe. Moreover, this erroneous MIST checkpoint has been reused in several
de novogeneration pipelines, inflating spectrum-to-fingerprint performance far above what we obtain
from a freshly trained, data-safe MIST encoder. As Table 4 shows, replacing batched inference
settings with single-spectrum settings sharply reduces downstream MIST + MolForge performance.
Given the irreproducibility of MIST vDiffMS, we introduce and recommend the MIST4M-aug
checkpoint, trained on the MassSpecGym training set mixed with synthetic spectra generated by
GLACIER for the official 4 million unlabeled molecules released with MassSpecGym v1.0. Our aim
is to prevent further propagation of unreproducible or otherwise problematic MIST checkpoints and
provide a more unified and trustworthy basis for measuring the decoder-side capabilities ofde novo
methods. Full training details for MIST4M-augare provided in Appendix A.2.2. Table 5 provides
the full updated performance leaderboard for thede novo bonustask.
Recommendation.Practice careful review when adopting existing model components or other code,
especially for use in development settings they were not designed for. Unintended bugs can occur
during training, end-to-end fine-tuning, and/or inference. MassSpecGym v1.5 includes the corrected
9

MIST implementation.8 We recommend MIST 4M-aug as the official off-the-shelf MIST checkpoint
for future benchmarking.
6.2 Metric Implementation Divergence Hindering Reproducibility
A second reproducibility failure stems from metric implementations that vary across codebases.
We identify four metrics—InChIKey hit rate, MCES distance, Tanimoto fingerprint similarity, and
close/meaningful match rates—requiring implementation choices that are neither standardized across
works nor consistently documented (complete formal definitions are given in Appendix A.6).
Table 5:Updated Leaderboard on the MassSpecGymde novoGeneration Bonus Challenge.This table
covers methods first reporting MassSpecGym results before May 1, 2026, and includes revised evaluations. The
best-performing model for each metric isboldand the second best is underlined. † indicates our implementations
of baseline approaches without public code. Gray rows are excluded from the corrected ranking: MIST
+ MolForge uses the unreproducible MIST vDiffMS checkpoint (§6.1), while FRIGID arXiv v2 uses test-
informed synthetic augmentation (§4.2). MCES calculations for MSNovelist, Neuraldecipher, and DiffMS were
recomputed from the original DiffMS paper in [54] to correctly use a myopic threshold of 15 instead of 100.
For MS-BART, we report accuracy based on 2D InChIKey matching from Appendix C of [ 55], rather than
the full InChIKey matching accuracy reported in the main text. FRIGID uses 10 rounds of ICEBERG-guided
inference-time refinement. Theauxiliary datacolumn marks methods that rely on data beyond the MassSpecGym
spectrum–molecule pairs. Code for our reproductions is available athttps://github.com/harrylaucngd/
msms-models.
Top-1 Top-10
Model Accuracy↑MCES↓Tanimoto↑Accuracy↑MCES↓Tanimoto↑Auxiliary data
SMILES Transformer [8] 0.00% 79.39 0.03 0.00% 52.13 0.10✗
SELFIES Transformer [8] 0.00% 38.88 0.08 0.00% 26.87 0.13✗
Random generation [8] 0.00% 21.11 0.08 0.00% 18.26 0.11✗
MIST + MSNovelist [33, 52] 0.00% 39.84 0.06 0.00% 18.83 0.15✓ a
Spec2Mol [56, 52] 0.00% 36.78 0.12 0.00% 36.02 0.16✗
MIST + Neuraldecipher [57, 52] 0.00% 22.93 0.14 0.00% 21.76 0.16✓ a
MADGEN [58] 1.31% 27.47 0.20 1.54% 16.84 0.26✓ b
MS-BART [55] 1.26% 16.47 0.23 1.28% 15.12 0.28✓ c
DiffMS [52] 2.30% 13.96 0.28 4.25% 11.68 0.39✓ a
FOAM (DiffMS + PubChem) [54] 1.50%12.210.35 10.28% 6.06 0.53✓ a,d
MSAnchor [59] 2.68% 16.57 0.32 4.67% 14.12 0.41✓ e
MIST + MolForge [53]† (corrected) 3.29% 31.77 0.31 5.65% 16.67 0.40✓ a,f
MIST + MolForge† (inflated, batch size = 24) 31.75% 12.30 0.68 40.55% 9.80 0.74✓ a,f
FRIGID-base [37] (MIST4M-aug) 8.21% 13.16 0.38 9.82% 11.65 0.43 ✓f,g
FRIGID [37] (MIST4M-aug) 9.05%12.60 0.39 12.23%11.41 0.43 ✓f,g
FRIGID [38] (arXiv v2) 18.29% 13.49 0.43 22.00% 11.65 0.47✓ f,g
a The MIST + MSNovelist, MIST + Neuraldecipher, DiffMS, and MIST + MolForge decoders were pretrained
on 2.8 million curated molecules9, 2D InChIKey-disjoint with MassSpecGym test and validation molecules (see
[52]). b MADGEN ranks Murcko scaffolds over the 256 formula-matched candidate structures provided by the
MassSpecGym retrieval challenge (see [58]). c MS-BART was pretrained on the 4 million unlabeled molecules
released with MassSpecGym v1.0, at an MCES distance >2 from MassSpecGym test molecules (see [55]).
d At inference, FOAM seeds its optimization with DiffMS-based suggestions and formula-matched PubChem
structures, with the latter set 2D InChIKey-disjoint with MassSpecGym test molecules (see [54]). e The first-
stage Transformer in MSAnchor was pretrained on spectra from SDBS [60] and the multimodal spectroscopic
dataset of Alberts et al. [35], excluding molecules with MCES distance <11 from any test molecule (see [59]).
f The gray MIST + MolForge and FRIGID rows use the earlier MIST checkpoints discussed in §6.1 and §4.2,
respectively. The corrected MIST + MolForge and FRIGID results use MIST4M-aug, trained on MassSpecGym
training spectra and GLACIER-generated spectra for the official 4 million unlabeled molecules released with
MassSpecGym v1.0. These corrected results are evaluated on all 17,556 test spectra (Appendix A.1). g The
FRIGID decoder was pretrained from the 1-billion-molecule corpus of [61], with additional filtering to exclude
structures sharing a 2D InChIKey with any MassSpecGym/NPLIB1 test or validation molecule5 (see [37]).
InChIKey: as spectral information often cannot disambiguate stereochemistry, deduplication and
accuracy evaluation should only use the 14-character, 2D connectivity layer; using the full 27-
character key treats stereoisomers as distinct molecules and undercounts true overlaps. For example,
8https://github.com/coleygroup/MIST
9https://github.com/coleygroup/DiffMS/blob/master/data_processing/00_download_
fp2mol_data.sh
10

full InChIKey matching lowers FRIGID’s top-1/top-10 accuracy from 9.05%/12.23% to 4.97%/6.80%
(Table 11).MCES: the distance |E(G1)|+|E(G 2)| −2|MCES(G1, G2)| is NP-hard and computed
via heuristic solvers whose timeout and approximation parameters vary across implementations.
Tanimoto similarity: computed on molecular fingerprints, the choice of fingerprint algorithm and
parameters like radius and bit length can significantly change Tanimoto similarities.
Recommendation.Pinned, standardized metric implementations should be used: 14-character
connectivity-layer matching for InChIKey; 2048-bit ECFP4 without chirality for Tanimoto similar-
ity; myopic-mces 1.0.0 with threshold=15 and always_stronger_bound=True for MCES. We
further recommend reporting mean test-set metrics with 99.9% BCa confidence intervals computed
from 20,000 bootstrap resamples. MassSpecGym v1.5 provides reference implementations for all
metrics; metric code copied from third-party repositories should be independently verified against
the benchmark specification.
7 Discussion and Release of MassSpecGym v1.5
The evaluation failures documented in the preceding sections have been highlighted in the context
of MassSpecGym, but are broadly relevant to computational mass spectrometry. In several cases,
these effects produce unexpectedly strong performance, underscoring the need for skepticism toward
results that appear too good to be true. The failure modes we have identified have motivated specific
recommendations that will promote more defensible evaluations for this rapidly growing field.
MassSpecGym v1.5 as a benchmark revision.The revised benchmark accompanying this paper is
MassSpecGym v1.5, which operationalizes the recommendations and findings discussed above.At
the data level, we perform uniform RDKit canonicalization across all candidate SMILES, eliminating
the formatting shortcut. In addition to the dataset of 4M molecules from MassSpecGym v1.0, we
also release new 2.5M and 50M decoder pretraining sets that exclude close structure analogs (for
example, Tanimoto similarity ≥0.7 ) to any test compound, providing a safer and more interpretable
foundation for generative model training.At the model level, we release a zoo of models including
officially retrained data-safe versions of MIST [18], MIST-CF [39], ICEBERG [34], GLACIER [36]
and DreaMS [46] to provide leakage-free components for formula prediction, spectral simulation,
and MS/MS embeddings computation. We also clarify previously ambiguous evaluation procedures
and correct identified errors, updating the leaderboards for both the retrieval andde novo bonus
tasks (Tables 3 and 5). These updates standardize evaluation criteria, correct inflated retrieval
results from problematic implementations, and address encoder-induced performance inflation in
thede novotask. The resulting changes in absolutede novoscores do not substantially alter the
relative ranking of the evaluated methods.At the evaluation level, we package the pinned metric
implementations, corrected inference settings, reference results used throughout this audit, and an
LLM-augmented agentic workflow for code review outlined in Appendix A.8, so that future work
can be compared under the same benchmark assumptions. Together, these updates reduce ambiguity
in how MassSpecGym results are produced, interpreted, and reproduced.
Limitations and broader implications.The three-category audit framework we apply—data leakage
analysis, task validity stress-testing, and reproducibility verification—is likely to transfer to related
benchmark ecosystems. At the same time, our analysis has important limitations. First, the audit
covers only the first year of MassSpecGym adoption to date (34 papers), and evaluation practice may
change as the community matures and more model implementations are made publicly available.
Second, our experiments (particularly the pretraining data leakage spectrum in §4) illustrate trends
in performance under example design choices, but the quantitative results and implications (e.g.,
recommended similarity thresholds) may shift as more models and corpora are analyzed. Third,
although MassSpecGym v1.5 corrects several major sources of ambiguity, it does not resolve every
evaluative challenge exposed by this audit—most notably, the ranking bias in candidate sets (§5)
remains an open design problem inherent to the retrospective nature of this, or any, benchmark.
References
[1] Julian Pollmann, Roman Bushuiev, Anton Bushuiev, Tomáš Pluskal, and Florian Huber. Bridg-
ing ms2 spectra and chemical space: Advances in spectral similarity, molecular retrieval, and de
novo structure discovery.ChemRxiv, 2026(0309), 2026. doi: 10.26434/chemrxiv.15000536/v2.
URLhttps://chemrxiv.org/doi/abs/10.26434/chemrxiv.15000536/v2.
11

[2] Atanas G. Atanasov, Sergey B. Zotchev, Verena M. Dirsch, Ilkay Erdogan Orhan, Maciej Banach,
Judith M. Rollinger, Davide Barreca, Wolfram Weckwerth, Rudolf Bauer, Edward A. Bayer,
Muhammed Majeed, Anupam Bishayee, Valery Bochkov, Günther K. Bonn, Nady Braidy, Franz
Bucar, Alejandro Cifuentes, Grazia D’Onofrio, Michael Bodkin, Marc Diederich, Albena T.
Dinkova-Kostova, Thomas Efferth, Khalid El Bairi, Nicolas Arkells, Tai-Ping Fan, Bernd L.
Fiebich, Michael Freissmuth, Milen I. Georgiev, Simon Gibbons, Keith M. Godfrey, Christian W.
Gruber, Jag Heer, Lukas A. Huber, Elena Ibanez, Anake Kijjoa, Anna K. Kiss, Aiping Lu,
Francisco A. Macias, Mark J. S. Miller, Andrei Mocan, Rolf Müller, Ferdinando Nicoletti,
George Perry, Valeria Pittalà, Luca Rastrelli, Michael Ristow, Gian Luigi Russo, Ana Sanches
Silva, Daniela Schuster, Helen Sheridan, Krystyna Skalicka-Wo´ zniak, Leandros Skaltsounis,
Eduardo Sobarzo-Sánchez, David S. Bredt, Hermann Stuppner, Antoni Sureda, Nikolay T.
Tzvetkov, Rosa Anna Vacca, Bharat B. Aggarwal, Maurizio Battino, Francesca Giampieri,
Michael Wink, Jean-Luc Wolfender, Jianbo Xiao, Andy Wai Kan Yeung, Gérard Lizard,
Michael A. Popp, Michael Heinrich, Ioana Berindan-Neagoe, Marc Stadler, Maria Daglia,
Robert Verpoorte, Claudiu T. Supuran, and the International Natural Product Sciences Taskforce.
Natural products in drug discovery: advances and opportunities.Nature Reviews Drug Discovery,
20(3):200–216, March 2021. ISSN 1474-1784. doi: 10.1038/s41573-020-00114-z. URL
https://doi.org/10.1038/s41573-020-00114-z.
[3] Eberhard Breitmaier.Structure elucidation by NMR in organic chemistry: a practical guide.
John Wiley & Sons, 2002. doi: 10.1002/0470853069.
[4] Cailum M. K. Stienstra, Jaegun Song, David Healey, Gennady V oronov, Eric Gardner, Abhishek
Patel, Venkat Macherla, Christoph A. Krettler, Tobias Kind, Pieter C. Dorrestein, and Daniel
Domingo-Fernández. Structure characterization with NMR molecular networking.Communica-
tions Chemistry, 9(1):28, December 2025. ISSN 2399-3669. doi: 10.1038/s42004-025-01839-x.
URLhttps://doi.org/10.1038/s42004-025-01839-x.
[5] Thomas Liao, Rohan Taori, Inioluwa Deborah Raji, and Ludwig Schmidt. Are we learning
yet? A meta review of evaluation failures across machine learning. In Joaquin Vanschoren and
Sai-Kit Yeung, editors,Proceedings of the Neural Information Processing Systems Track on
Datasets and Benchmarks 1, NeurIPS Datasets and Benchmarks 2021, December 2021, virtual,
2021. URL https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/
hash/757b505cfd34c64c85ca5b5690ee5293-Abstract-round2.html.
[6] Rachel L. Thomas and David Uminsky. Reliance on metrics is a fundamental challenge for
AI.Patterns, 3(5):100476, 2022. ISSN 2666-3899. doi: 10.1016/j.patter.2022.100476. URL
https://www.sciencedirect.com/science/article/pii/S2666389922000563.
[7] Inioluwa Deborah Raji, Emily Denton, Emily M. Bender, Alex Hanna, and Amandalynne
Paullada. AI and the everything in the whole wide world benchmark. In Joaquin Vanschoren
and Sai-Kit Yeung, editors,Proceedings of the Neural Information Processing Systems Track on
Datasets and Benchmarks 1, NeurIPS Datasets and Benchmarks 2021, December 2021, virtual,
2021. URL https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/
hash/084b6fbb10729ed4da8c3d3f5a3ae7c9-Abstract-round2.html.
[8] Roman Bushuiev, Anton Bushuiev, Niek F. de Jonge, Adamo Young, Fleming Kretschmer, Ra-
man Samusevich, Janne Heirman, Fei Wang, Luke Zhang, Kai Dührkop, Marcus Ludwig, Nils A.
Haupt, Apurva Kalia, Corinna Brungs, Robin Schmid, Russell Greiner, Bo Wang, David S.
Wishart, Liping Liu, Juho Rousu, Wout Bittremieux, Hannes Rost, Tytus D. Mak, Soha Hassoun,
Florian Huber, Justin J. J. van der Hooft, Michael A. Stravs, Sebastian Böcker, Josef Sivic, and
Tomás Pluskal. MassSpecGym: A benchmark for the discovery and identification of molecules.
In Amir Globersons, Lester Mackey, Danielle Belgrave, Angela Fan, Ulrich Paquet, Jakub M.
Tomczak, and Cheng Zhang, editors,Advances in Neural Information Processing Systems 38:
Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver,
BC, Canada, December 10 - 15, 2024, 2024. URL http://papers.nips.cc/paper_files/
paper/2024/hash/c6c31413d5c53b7d1c343c1498734b0f-Abstract-Datasets_and_
Benchmarks_Track.html.
[9] C. A. E. Goodhart.Problems of Monetary Management: The UK Experience, pages 91–
121. Macmillan Education UK, London, 1984. ISBN 978-1-349-17295-5. doi: 10.1007/
978-1-349-17295-5_4. URLhttps://doi.org/10.1007/978-1-349-17295-5_4.
12

[10] Monte MacDiarmid, Benjamin Wright, Jonathan Uesato, Joe Benton, Jon Kutasov, Sara Price,
Naia Bouscal, Sam Bowman, Trenton Bricken, Alex Cloud, Carson Denison, Johannes Gasteiger,
Ryan Greenblatt, Jan Leike, Jack Lindsey, Vlad Mikulik, Ethan Perez, Alex Rodrigues, Drake
Thomas, Albert Webson, Daniel Ziegler, and Evan Hubinger. Natural emergent misalignment
from reward hacking in production RL, 2025. URL https://arxiv.org/abs/2511.18397.
[11] Benjamin Recht, Rebecca Roelofs, Ludwig Schmidt, and Vaishaal Shankar. Do ImageNet
classifiers generalize to ImageNet? In Kamalika Chaudhuri and Ruslan Salakhutdinov, editors,
Proceedings of the 36th International Conference on Machine Learning, ICML 2019, 9-15 June
2019, Long Beach, California, USA, volume 97 ofProceedings of Machine Learning Research,
pages 5389–5400. PMLR, 2019. URL http://proceedings.mlr.press/v97/recht19a.
html.
[12] Sean Whalen, Jacob Schreiber, William S. Noble, and Katherine S. Pollard. Navigating the
pitfalls of applying machine learning in genomics.Nature Reviews Genetics, 23(3):169–181,
November 2021. ISSN 1471-0064. doi: 10.1038/s41576-021-00434-9. URL http://dx.doi.
org/10.1038/s41576-021-00434-9.
[13] Peter Škrinjar, Jérôme Eberhardt, Gerardo Tauriello, Torsten Schwede, and Janani Durairaj.
Have protein-ligand cofolding methods moved beyond memorisation?bioRxiv, 2025. doi: 10.
1101/2025.02.03.636309. URL https://www.biorxiv.org/content/early/2025/08/
04/2025.02.03.636309.
[14] Anton Bushuiev, Roman Bushuiev, Jirí Sedlár, Tomás Pluskal, Jirí Damborský, Stanislav
Mazurenko, and Josef Sivic. Revealing data leakage in protein interaction benchmarks.CoRR,
abs/2404.10457, 2024. doi: 10.48550/ARXIV .2404.10457. URL https://doi.org/10.
48550/arXiv.2404.10457.
[15] Rıza Özçelik and Francesca Grisoni. How evaluation choices distort the outcome of generative
drug discovery.Journal of Cheminformatics, 17(1), November 2025. ISSN 1758-2946. doi: 10.
1186/s13321-025-01108-y. URLhttp://dx.doi.org/10.1186/s13321-025-01108-y.
[16] Fleming Kretschmer, Jan Seipp, Marcus Ludwig, Gunnar W. Klau, and Sebastian Böcker.
Coverage bias in small molecule machine learning.Nature Communications, 16(1):554, January
2025. ISSN 2041-1723. doi: 10.1038/s41467-024-55462-w. URL https://doi.org/10.
1038/s41467-024-55462-w.
[17] Emma L. Schymanski, Christoph Ruttkies, Martin Krauss, Céline Brouard, Tobias Kind, Kai
Dührkop, Felicity Allen, Arpana Vaniya, Dries Verdegem, Sebastian Böcker, Juho Rousu, Huibin
Shen, Hiroshi Tsugawa, Tanvir Sajed, Oliver Fiehn, Bart Ghesquière, and Steffen Neumann.
Critical assessment of small molecule identification 2016: automated methods.Journal of
Cheminformatics, 9(1):22, March 2017. ISSN 1758-2946. doi: 10.1186/s13321-017-0207-1.
URLhttps://doi.org/10.1186/s13321-017-0207-1.
[18] Samuel Goldman, Jeremy Wohlwend, Martin Stražar, Guy Haroush, Ramnik J. Xavier, and Con-
nor W. Coley. Annotating metabolite mass spectra with domain-inspired chemical formula trans-
formers.Nature Machine Intelligence, 5(9):965–979, September 2023. ISSN 2522-5839. doi:
10.1038/s42256-023-00708-3. URLhttps://doi.org/10.1038/s42256-023-00708-3.
[19] Mingxun Wang, Jeremy J. Carver, Vanessa V . Phelan, Laura M. Sanchez, Neha Garg, Yao Peng,
Don Duy Nguyen, Jeramie Watrous, Clifford A. Kapono, Tal Luzzatto-Knaan, Carla Porto,
Amina Bouslimani, Alexey V . Melnik, Michael J. Meehan, Wei-Ting Liu, Max Crüsemann,
Paul D. Boudreau, Eduardo Esquenazi, Mario Sandoval-Calderón, Roland D. Kersten, Laura A.
Pace, Robert A. Quinn, Katherine R. Duncan, Cheng-Chih Hsu, Dimitrios J. Floros, Ronnie G.
Gavilan, Karin Kleigrewe, Trent Northen, Rachel J. Dutton, Delphine Parrot, Erin E. Carlson,
Bertrand Aigle, Charlotte F. Michelsen, Lars Jelsbak, Christian Sohlenkamp, Pavel Pevzner,
Anna Edlund, Jeffrey McLean, Jörn Piel, Brian T. Murphy, Lena Gerwick, Chih-Chuang Liaw,
Yu-Liang Yang, Hans-Ulrich Humpf, Maria Maansson, Robert A. Keyzers, Amy C. Sims,
Andrew R. Johnson, Ashley M. Sidebottom, Brian E. Sedio, Andreas Klitgaard, Charles B.
Larson, Cristopher A. Boya P, Daniel Torres-Mendoza, David J. Gonzalez, Denise B. Silva,
Lucas M. Marques, Daniel P. Demarque, Egle Pociute, Ellis C. O’Neill, Enora Briand, Eric
J. N. Helfrich, Eve A. Granatosky, Evgenia Glukhov, Florian Ryffel, Hailey Houson, Hosein
13

Mohimani, Jenan J. Kharbush, Yi Zeng, Julia A. V orholt, Kenji L. Kurita, Pep Charusanti,
Kerry L. McPhail, Kristian Fog Nielsen, Lisa Vuong, Maryam Elfeki, Matthew F. Traxler,
Niclas Engene, Nobuhiro Koyama, Oliver B. Vining, Ralph Baric, Ricardo R. Silva, Samantha J.
Mascuch, Sophie Tomasi, Stefan Jenkins, Venkat Macherla, Thomas Hoffman, Vinayak Agarwal,
Philip G. Williams, Jingqui Dai, Ram Neupane, Joshua Gurr, Andrés M. C. Rodríguez, Anne
Lamsa, Chen Zhang, Kathleen Dorrestein, Brendan M. Duggan, Jehad Almaliti, Pierre-Marie
Allard, Prasad Phapale, Louis-Felix Nothias, Theodore Alexandrov, Marc Litaudon, Jean-Luc
Wolfender, Jennifer E. Kyle, Thomas O. Metz, Tyler Peryea, Dac-Trung Nguyen, Danielle
VanLeer, Paul Shinn, Ajit Jadhav, Rolf Müller, Katrina M. Waters, Wenyuan Shi, Xueting
Liu, Lixin Zhang, Rob Knight, Paul R. Jensen, Bernhard Ø Palsson, Kit Pogliano, Roger G.
Linington, Marcelino Gutiérrez, Norberto P. Lopes, William H. Gerwick, Bradley S. Moore,
Pieter C. Dorrestein, and Nuno Bandeira. Sharing and community curation of mass spectrometry
data with global natural products social molecular networking.Nature Biotechnology, 34(8):
828–837, August 2016. ISSN 1546-1696. doi: 10.1038/nbt.3597. URL https://doi.org/
10.1038/nbt.3597.
[20] Samuel Goldman, John Bradshaw, Jiayi Xin, and Connor W. Coley. Prefix-tree de-
coding for predicting mass spectra from molecules. In Alice Oh, Tristan Naumann,
Amir Globerson, Kate Saenko, Moritz Hardt, and Sergey Levine, editors,Advances
in Neural Information Processing Systems 36: Annual Conference on Neural Informa-
tion Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, December 10
- 16, 2023, 2023. URL http://papers.nips.cc/paper_files/paper/2023/hash/
97d596ca21d0751ba2c633bad696cf7f-Abstract-Conference.html.
[21] Armen G. Beck, Matthew Muhoberac, Caitlin E. Randolph, Connor H. Beveridge, Prageeth R.
Wijewardhane, Hilkka I. Kenttämaa, and Gaurav Chopra. Recent developments in machine
learning for mass spectrometry.ACS Measurement Science Au, 4(3):233–246, 2024. doi:
10.1021/acsmeasuresciau.3c00060. URL https://doi.org/10.1021/acsmeasuresciau.
3c00060.
[22] Xujun Che, Xiuxia Du, and Depeng Xu. Comparative analysis of formula and structure
prediction from tandem mass spectra, 2026. URLhttps://arxiv.org/abs/2601.00941.
[23] Mark Yu. Schneider, Daniil D. Kholmanskikh, Kirill Ya. Romanov, Elena A. Perekina, Sergei A.
Nikolenko, Ruslan Yu. Lukin, and Ivan V . Golov. De novo structure prediction from tandem mass
spectra: Algorithms, benchmarks, and limitations.Molecules, 31(5), 2026. ISSN 1420-3049.
doi: 10.3390/molecules31050769. URLhttps://www.mdpi.com/1420-3049/31/5/769.
[24] Gaetan De Waele, Marek Wydmuch, Krzysztof Dembczy´nski, Wojciech Kotłowski, and Willem
Waegeman. Small molecule retrieval from tandem mass spectrometry: what are we optimizing
for?, 2026. URLhttps://arxiv.org/abs/2602.16507.
[25] Martin A. Hoffmann, Fleming Kretschmer, Marcus Ludwig, and Sebastian Böcker. MAD
HATTER correctly annotates 98% of small molecule tandem mass spectra searching in Pub-
Chem.Metabolites, 13(3), 2023. ISSN 2218-1989. doi: 10.3390/metabo13030314. URL
https://www.mdpi.com/2218-1989/13/3/314.
[26] Niek F. de Jonge, Kevin Mildau, David Meijer, Joris J. R. Louwen, Christoph Bueschl, Florian
Huber, and Justin J. J. van der Hooft. Good practices and recommendations for using and
benchmarking computational metabolomics metabolite annotation tools.Metabolomics, 18
(12):103, December 2022. ISSN 1573-3890. doi: 10.1007/s11306-022-01963-y. URL
https://doi.org/10.1007/s11306-022-01963-y.
[27] Michael Strobel, Alberto Gil-de-la Fuente, Mohammad Reza Zare Shahneh, Yasin El Abiead,
Roman Bushuiev, Anton Bushuiev, Tomáš Pluskal, and Mingxun Wang. An evaluation method-
ology for machine learning-based tandem mass spectra similarity prediction.BMC Bioinfor-
matics, 26(1):174, July 2025. ISSN 1471-2105. doi: 10.1186/s12859-025-06194-1. URL
https://doi.org/10.1186/s12859-025-06194-1.
[28] Yunhua Zhong, Yixuan Tang, Yifan Li, Jie Yang, Pan Liu, and Jun Xia. FlexMS is a flex-
ible framework for benchmarking deep learning-based mass spectrum prediction tools in
metabolomics, 2026. URLhttps://arxiv.org/abs/2602.22822.
14

[29] Xin Zhao, Yumin Liu, Zhuo Li, Weichu Zheng, Feng Zhu, Xiaokang Yang, Yaohui Jin, and
Yanyan Xu. MS-GPT: Rethinking MS/MS de novo structure elucidation as spectrum-induced
posterior querying of a molecule-language model.arXiv preprint arXiv:2607.23607, 2026.
[30] John J. Irwin, Khanh G. Tang, Jennifer Young, Chinzorig Dandarchuluun, Benjamin R. Wong,
Munkhzul Khurelbaatar, Yurii S. Moroz, John Mayfield, and Roger A. Sayle. ZINC20—a free
ultralarge-scale chemical database for ligand discovery.Journal of Chemical Information and
Modeling, 60(12):6065–6073, 2020. doi: 10.1021/acs.jcim.0c00675.
[31] Jon Chambers, Mark Davies, Anna Gaulton, Anne Hersey, Sameer Velankar, Robert Petryszak,
Janna Hastings, John P Overington, Christoph Steinbeck, and Andrew R Leach. UniChem:
a unified chemical structure cross-referencing and identifier tracking system.Journal of
Cheminformatics, 5(1):3, 2013. doi: 10.1186/1758-2946-5-3.
[32] Kai Dührkop, Louis-Félix Nothias, Markus Fleischauer, Raphael Reher, Marcus Ludwig, Mar-
tin A. Hoffmann, Daniel Petras, William H. Gerwick, Juho Rousu, Pieter C. Dorrestein, and Se-
bastian Böcker. Systematic classification of unknown metabolites using high-resolution fragmen-
tation mass spectra.Nature Biotechnology, 39(4):462–471, April 2021. ISSN 1546-1696. doi:
10.1038/s41587-020-0740-8. URLhttps://doi.org/10.1038/s41587-020-0740-8.
[33] Michael A Stravs, Kai Dührkop, Sebastian Böcker, and Nicola Zamboni. MSNovelist: de
novo structure generation from mass spectra.Nature Methods, 19(7):865–870, 2022. doi:
10.1038/s41592-022-01486-3.
[34] Runzhong Wang, Mrunali Manjrekar, Babak Mahjour, Julian Avila-Pacheco, Joules Provenzano,
Erin Reynolds, Magdalena Lederbauer, Eivgeni Mashin, Samuel Goldman, Mingxun Wang,
et al. Neural spectral prediction for structure elucidation with tandem mass spectrometry.
bioRxiv, 2025.
[35] Marvin Alberts, Oliver Schilter, Federico Zipoli, Nina Hartrampf, and Teodoro Laino. Unravel-
ing molecular structure: A multimodal spectroscopic dataset for chemistry. In A. Globerson,
L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang, editors,Advances in
Neural Information Processing Systems, volume 37, pages 125780–125808. Curran Associates,
Inc., 2024. doi: 10.52202/079017-3996. URL https://proceedings.neurips.cc/paper_
files/paper/2024/file/e38e60b33bb2c6993e0865160cdb5cf1-Paper-Datasets_
and_Benchmarks_Track.pdf.
[36] Rui-Xi Wang, Runzhong Wang, and Connor W Coley. GLACIER: Rethinking mass spectrum
prediction as an object detection problem.arXiv preprint arXiv:2606.29161, 2026.
[37] Montgomery Bohde, Hongxuan Liu, Mrunali Manjrekar, Magdalena Lederbauer, Shuiwang Ji,
Runzhong Wang, and Connor W Coley. FRIGID: Scaling diffusion-based molecular generation
from mass spectra at training and inference time.arXiv preprint arXiv:2604.16648, 2026. URL
https://arxiv.org/abs/2604.16648.
[38] Montgomery Bohde, Hongxuan Liu, Mrunali Manjrekar, Magdalena Lederbauer, Shuiwang Ji,
Runzhong Wang, and Connor W Coley. FRIGID: Scaling diffusion-based molecular generation
from mass spectra at training and inference time.arXiv preprint arXiv:2604.16648v2, 2026.
URLhttps://arxiv.org/abs/2604.16648v2.
[39] Samuel Goldman, Jiayi Xin, Joules Provenzano, and Connor W Coley. MIST-CF: Chemical
formula inference from tandem mass spectra.Journal of Chemical Information and Modeling,
64(7):2421–2431, April 2024.
[40] Kai Dührkop, Markus Fleischauer, Marcus Ludwig, Alexander A Aksenov, Alexey V Melnik,
Marvin Meusel, Pieter C Dorrestein, Juho Rousu, and Sebastian Böcker. SIRIUS 4: a rapid tool
for turning tandem mass spectra into metabolite structure information.Nature Methods, 16(4):
299–302, April 2019.
[41] Greg Landrum, Paolo Tosco, Brian Kelley, Ricardo Rodriguez, David Cosgrove, Riccardo
Vianello, sriniker, Peter Gedeck, Gareth Jones, Eisuke Kawashima, NadineSchneider, Dan
Nealschneider, tadhurst cdd, Andrew Dalke, Matt Swain, Brian Cole, Samo Turk, Aleksandr
Savelev, Niels Maeder, Yakov Pechersky, Alain Vaucher, Maciej Wójcikowski, Rachel Walker,
15

Hussein Faara, Ichiru Take, Vincent F. Scalfani, Daniel Probst, Kazuya Ujihara, Jeremy Monat,
and Juuso Lehtivarjo. rdkit/rdkit: 2026_03_2 (Q1 2026) release, April 2026. URL https:
//doi.org/10.5281/zenodo.19922430.
[42] Ling Min Serena Khoo. Nearest-neighbour baselines for fingerprint prediction from MS/MS
spectra under different assumptions.arXiv preprint arXiv:2610.02249, 2026. URL https:
//arxiv.org/abs/2610.02249.
[43] Apurva Kalia, Yan Zhou Chen, Dilip Krishnan, and Soha Hassoun. JESTR: Joint embedding
space technique for ranking candidate molecules for the annotation of untargeted metabolomics
data.Bioinformatics, 41(7):btaf354, 2025. doi: 10.1093/bioinformatics/btaf354.
[44] Yan Zhou Chen and Soha Hassoun. Learning from all views: A multiview contrastive framework
for metabolite annotation.Analytical Chemistry, 2026. doi: 10.1021/acs.analchem.5c05675.
[45] Yan Zhou Chen, Blake Rushing, and Soha Hassoun. FLARE: Fine-grained learning for
alignment of spectra-molecule REpresentation enhances metabolite annotation.bioRxiv, page
2026.01.27.702086, January 2026.
[46] Roman Bushuiev, Anton Bushuiev, Raman Samusevich, Corinna Brungs, Josef Sivic, and
Tomáš Pluskal. Self-supervised learning of molecular representations from millions of tandem
mass spectra using DreaMS.Nature Biotechnology, 44:630–640, April 2026. doi: 10.1038/
s41587-025-02663-3. Published online May 23, 2025.
[47] Walid Ahmad, Elana Simon, Seyone Chithrananda, Gabriel Grand, and Bharath Ramsundar.
ChemBERTa-2: Towards chemical foundation models.CoRR, abs/2209.01712, 2022. doi:
10.48550/ARXIV .2209.01712. URLhttps://doi.org/10.48550/arXiv.2209.01712.
[48] Ross Irwin, Spyridon Dimitriadis, Jiazhen He, and Esben Jannik Bjerrum. Chemformer: a pre-
trained transformer for computational chemistry.Machine Learning: Science and Technology,
3(1):015022, 2022. doi: 10.1088/2632-2153/ac3ffb.
[49] Niu Huang, Brian K Shoichet, and John J Irwin. Benchmarking sets for molecular docking.
Journal of Medicinal Chemistry, 49(23):6789–6801, 2006. doi: 10.1021/jm0608356.
[50] Michael M. Mysinger, Michael Carchia, John J. Irwin, and Brian K. Shoichet. Directory of useful
decoys, enhanced (DUD-E): Better ligands and decoys for better benchmarking.Journal of
Medicinal Chemistry, 55(14):6582–6594, July 2012. ISSN 0022-2623. doi: 10.1021/jm300687e.
URLhttps://doi.org/10.1021/jm300687e.
[51] Vishu Gupta and Michael A. Skinnider. Confronting spurious evaluations of computational
methods in small molecule mass spectrometry.bioRxiv, 2026. doi: 10.64898/2026.05.03.722532.
URLhttps://www.biorxiv.org/content/early/2026/05/06/2026.05.03.722532.
[52] Montgomery Bohde, Mrunali Manjrekar, Runzhong Wang, Shuiwang Ji, and Connor W Coley.
DiffMS: Diffusion generation of molecules conditioned on mass spectra. InInternational
Conference on Machine Learning, pages 4737–4756. PMLR, 2025.
[53] Neng Kai Nigel Neo, Lim Jing, Ngoui Yong Zhau Preston, Koh Xue Ting Serene, and Bingquan
Shen. One small step with fingerprints, one giant leap for de novo molecule generation from
mass spectra.arXiv preprint arXiv:2508.04180, 2025. doi: 10.48550/arXiv.2508.04180.
Accepted at AI4Mat-NeurIPS-2025 Workshop.
[54] Mrunali Manjrekar, Runzhong Wang, Samuel Goldman, Jenna C. Fromer, and Connor W.
Coley. Generative structural elucidation from mass spectra as an iterative optimization problem.
CoRR, abs/2602.07709, 2026. doi: 10.48550/ARXIV .2602.07709. URL https://doi.org/
10.48550/arXiv.2602.07709.
[55] Yang Han, Pengyu Wang, Kai Yu, Xin Chen, and Lu Chen. MS-BART: Unified modeling
of mass spectra and molecules for structure elucidation. InAdvances in Neural Information
Processing Systems, 2025.
16

[56] Eleni E Litsa, Vijil Chenthamarakshan, Payel Das, and Lydia E Kavraki. An end-to-end
deep learning framework for translating mass spectra to de-novo molecules.Communications
Chemistry, 6(1):1–12, June 2023.
[57] Tuan Le, Robin Winter, Frank Noé, and Djork-Arné Clevert. Neuraldecipher - reverse-
engineering extended-connectivity fingerprints (ECFPs) to their molecular structures.Chemical
Science, 11(38):10378–10389, September 2020.
[58] Yinkai Wang, Xiaohui Chen, Liping Liu, and Soha Hassoun. MADGEN: Mass-spec attends
to de novo molecular generation. InThe Thirteenth International Conference on Learning
Representations, 2025. URLhttps://openreview.net/forum?id=78tc3EiUrN.
[59] Xiaohan Qin, Chao Wang, Zhen-Qiang Zhou, Linjiang Chen, Wenjie Du, and Yang Wang.
MSAnchor: De novo molecular generation from mass spectrometry data with anchor-extended
molecular scaffolds. InAAAI Conference on Artificial Intelligence, 2026. URL https://api.
semanticscholar.org/CorpusID:286668073.
[60] National Institute of Advanced Industrial Science and Technology (AIST). Spectral Database
for Organic Compounds, SDBS.https://sdbs.db.aist.go.jp/. Accessed: 2026-10-11.
[61] Emmanuel Noutahi, Cristian Gabellini, Michael Craig, Jonathan S. C. Lim, and Prudencio
Tossou. Gotta be SAFE: A new framework for molecular design.CoRR, abs/2310.10773,
2023. doi: 10.48550/ARXIV .2310.10773. URL https://doi.org/10.48550/arXiv.2310.
10773.
[62] Christopher M Grulke, Antony J Williams, Inthirany Thillanadarajah, and Ann M Richard.
EPA’s DSSTox database: History of development of a curated chemistry resource supporting
computational toxicology research.Computational Toxicology, 12:100096, 2019. doi: 10.1016/
j.comtox.2019.100096.
[63] David S Wishart, AnChi Guo, Eponine Oler, Fei Wang, Afia Anjum, Harrison Peters, Raynard
Diber, Zinat Liang, Vasuk Gautam, Dan Wishart, et al. HMDB 5.0: the human metabolome
database for 2022.Nucleic Acids Research, 50(D1):D622–D631, 2022. doi: 10.1093/nar/
gkab1062.
[64] Maria Sorokina, Peter Merseburger, Kohulan Rajan, Mehmet Aziz Yirik, and Christoph Stein-
beck. COCONUT online: Collection of open natural products database.Journal of Cheminfor-
matics, 13(1):2, 2021. doi: 10.1186/s13321-020-00478-9.
[65] Daniil Polykovskiy, Alexander Zhebrak, Benjamin Sanchez-Lengeling, Sergey Golovanov,
Oktai Tatanov, Stanislav Belyaev, Rauf Kurbanov, Aleksey Artamonov, Vladimir Aladinskiy,
Mark Veselov, Artur Kadurin, Simon Johansson, Hongming Chen, Sergey Nikolenko, Alán
Aspuru-Guzik, and Alex Zhavoronkov. Molecular sets (MOSES): A benchmarking platform
for molecular generation models.Frontiers in Pharmacology, 11:565644, 2020. doi: 10.3389/
fphar.2020.565644.
[66] Laura Mismetti, Marvin Alberts, Andreas Krause, and Mara Graziani. Test-time tuned language
models enable end-to-end de novo molecular structure generation from MS/MS spectra.arXiv
preprint arXiv:2510.23746, 2025.
[67] Ling Min Serena Khoo and Regina Barzilay. Why machine learning fails at
mass spectrometry for small molecules.Nature Metabolism, 8(6):1247–1249, 2026.
doi: 10.1038/s42255-026-01544-6. URL https://www.nature.com/articles/
s42255-026-01544-6.
[68] Ling Min Serena Khoo. A data attribution-based approach to model diagnosis in LC-MS/MS
structure prediction. Master’s thesis, Massachusetts Institute of Technology, 2025. URL
https://dspace.mit.edu/handle/1721.1/164644.
[69] Thomas Butler, Abraham Frandsen, Rose Lightheart, Brian Bargh, Thomas Kerby, Kiana
West, Joseph Davison, James Taylor, Christoph Krettler, T J Bollerman, Gennady V oronov,
Kevin Moon, Tobias Kind, Pieter Dorrestein, August Allen, Viswa Colluru, and David Healey.
MS2Mol: A transformer model for illuminating dark chemical space from mass spectra.Chem-
Rxiv, September 2023.
17

A Technical Appendices and Supplementary Material
A.1 Experimental Details and Full Results of MolForge Decoder Pretraining
A.1.1 Data Contamination Condition Definitions
All structural comparisons in this section use ECFP4 Morgan fingerprints (radius 2, 2048 bits)
and the MassSpecGym test set as the reference. We curate three decoder pretraining corpora at
different scales—2.5M, 10M, and 50M molecules—with six variations of similarity-based exclusion
criteria each10, discussed in detail below. The 2.5M splits are drawn from the composite dataset of
DSSTox[ 62],HMDB[ 63],COCONUT[ 64], andMOSES[ 65] commonly used in prior work [53,
52, 58, 55]. The 10M and 50M corpora are randomly sampled from a combined pool of approximately
1B molecules fromZINC20[ 30] andUniChem[ 31]. For each size, we curate six dataset variants
according to the following criteria:
• EXCLUDE_EXACT:For each target size, we randomly draw molecules from the corresponding
source corpus until obtaining 2.5M, 10M, or 50M molecules whose connectivity-layer InChIKey
(first 14 characters, i.e., the 2D structure hash) does not match any MassSpecGym test-set molecule.
Because the first InChIKey block ignores stereochemical layers, this criterion also excludes all
stereoisomers of test molecules.
• EXCLUDE_TANI080,EXCLUDE_TANI070, andEXCLUDE_TANI060:Starting from the same
source order, we replace all molecules whose maximum fingerprint Tanimoto similarity to the
test set is greater than or equal to the specified threshold with additional molecules from the same
source corpus that satisfy the threshold. We choose Tanimoto similarity for this experiment because
MCES distance is expensive and slow to compute at scale. We expect that either metric should be
sufficient for this experiment. For all pretraining molecules x and test molecules Ttest, the retained
set satisfiesmax y∈Ttest Tan(ECFP4(x),ECFP4(y))< θ, withθ∈ {0.80,0.70,0.60}.
• INCLUDE_HALF:We construct a partially contaminated condition by starting fromEX-
CLUDE_EXACTand replacing an equal number of randomly selected non-test molecules with
50% of the unique MassSpecGym test-set molecules. This isolates the effect of direct test-structure
exposure while preserving the total number of decoder pretraining molecules.
• INCLUDE_ALL:We construct a fully contaminated condition analogously, replacing non-test
molecules inEXCLUDE_EXACTwith all unique MassSpecGym test-set molecules. This provides
an upper-bound direct-leakage condition under otherwise identical corpus size and training settings.
Table 6:Dataset Construction Audit for the Six Leakage Control Variants at Each Decoder Pretraining
Scale.Entries are the number of molecules removed relative to the size-matchedEXCLUDE_EXACTconstruction
for Tanimoto-filtered variants, or the number of MassSpecGym test-set molecules inserted into theINCLUDE
variants. Note that the 2.5M dataset is drawn from a different source corpus from the 10M and 50M datasets,
and has a much higher concentration of close structure analogs to MassSpecGym test structures. This may affect
the interpretation of Figure 2c and Table 7, giving more weight to the 2.5M model.
Target sizeEXCLUDE_EXACT EXCLUDE_TANI080EXCLUDE_TANI070EXCLUDE_TANI060INCLUDE_HALF INCLUDE_ALL
2.5M 0 removed 2,174 additionally removed 5,939 additionally removed 22,504 additionally removed 1,585 inserted 3,170 inserted
10M 0 removed 559 additionally removed 1,633 additionally removed 6,495 additionally removed 1,585 inserted 3,170 inserted
50M 0 removed 2,666 additionally removed 7,946 additionally removed 32,070 additionally removed 1,585 inserted 3,170 inserted
A.1.2 Molecular Decoder Training and Inference Configuration
We train a separate SMILES decoder [29] for each dataset variant and evaluate its checkpoints at the
three corpus sizes. Decoder training is varied while the spectrum encoder and evaluation protocol
are held fixed. The decoder uses 12 Transformer layers with hidden size 768, 12 attention heads,
dropout 0.1, and a maximum sequence length of 256, with character-level SMILES tokenization. It is
conditioned on 4096-bit Morgan fingerprints and molecular formulas through a two-layer fingerprint
encoder and cross-attention inserted after every two decoder layers. Models are trained with AdamW
(β1 = 0.9, β2 = 0.95), token-level negative log-likelihood loss, an effective batch size of 1,024,
weight decay 0.01, gradient clipping at norm 1.0, and bfloat16 automatic mixed precision. The
10https://huggingface.co/datasets/harrylau/ms-gpt-18
18

learning rate warms up over 2,000 optimizer steps to 3×10 −4 and then follows a cosine decay
schedule.
For the 2.5M, 10M, and 50M corpus sizes, respectively, we train all dataset variants for 15, 8, and 3
epochs. These schedules were chosen to ensure that models at each scale reach convergence under
the fixed training budget. For each trained model, we select the checkpoint with the best validation
performance and use that checkpoint for test evaluation. Training is run in distributed mode on a node
with 172 CPU cores, 2048 GB of memory, and 8 NVIDIA RTX PRO 6000 Blackwell Server Edition
GPUs; wall-clock training time ranges from approximately 1.5 to 6 hours per model, depending on
the corpus size and filtering condition.
Inference is implemented in https://github.com/harrylaucngd/msms-models. Each trained
decoder is paired with the same MIST4M-augcheckpoint to predict molecular fingerprints from
peak-formula–annotated spectra. No end-to-end joint fine-tuning is performed, as it was observed
to degrade performance. For each spectrum, we construct 20 binary fingerprint queries by applying
equally spaced thresholds within a density-calibrated interval to the MIST probabilities. The interval
is calibrated on the MassSpecGym training set: its endpoints yield mean predicted on-bit counts
equal to 1.5 and 0.95 times the mean reference on-bit count, respectively. We sample five SMILES
sequences per query, giving 100 candidates per spectrum, with temperature 1.0, top- k= 50 , and
top-p= 0.95. Valid candidates are canonicalized, grouped by 2D InChIKey, filtered by the known
molecular formula, and ranked by generation frequency; ties are broken by fingerprint Tanimoto
similarity to the query fingerprints. We evaluate all 17,556 input spectra in the MassSpecGymde novo
test split and report spectrum-level averages. By contrast, earlier evaluations using MIST vDiffMS
and the FRIGID evaluation in arXiv v2 [38] excluded 474 spectra whose ground-truth molecules
contain atom types outside the MIST-supported set {C,O,P,N,S,Cl,F,H} , reducing evaluation
to 17,082 spectra. The corrected MIST + MolForge and FRIGID entries in Table 5 are evaluated
on all 17,556 test spectra. MCES is not computed in these experiments; reported metrics are top-1
accuracy (Acc@1) and top-10 accuracy (Acc@10), based on 2D InChIKey matching after tautomer
canonicalization and removal of stereochemistry. Inference is also run in distributed mode on the same
172-core, 2048-GB, 8-GPU node; full 8-GPU inference over the benchmark takes approximately 1.5
hours per model.
For Figure 2a, we group the 17,556 test spectra into 2,997 compounds by InChIKey-14, average top-1
hits within each compound, and then average compounds within each similarity bin. Similarity is the
maximum over the union of the encoder’s MSG-4M augmentation molecules and MassSpecGym
training molecules, and the decoder’s 2.5M, 10M, and 50M training corpora. We use the molecular
representations used during training and compute 95% BCa intervals with 20,000 compound-level
bootstrap resamples (seed 42); intervals are omitted for bins with zero empirical variance.
A.1.3 Full Per-Condition Metric Table
Table 7 reports exact-match generation accuracy of the selected validation-best decoder checkpoint for
every corpus size and leakage variant. Each cell gives Acc@1/Acc@10, rows are ordered by decoder
pretraining scale, and columns are ordered from direct test-set inclusion to progressively stricter
exclusion. The 2.5M decoder shows the worst-case performance gradient with respect to splitting
criterion, motivating our recommendation that training datasets exclude, for example, structures with
Tanimoto similarity≥0.7to any test-set compound when reporting results about generalization.
Table 7:Exact-Match Accuracy on the MassSpecGymde novoChallenge for Molecular Decoders Trained
on All Corpus Sizes and Dataset Variants.Each decoder is paired with MIST4M-aug. Each entry reports
Acc@1/Acc@10 for the checkpoint with the best validation performance.
Target sizeINCLUDE_ALL INCLUDE_HALF EXCLUDE_EXACT EXCLUDE_TANI080EXCLUDE_TANI070EXCLUDE_TANI060
2.5M 8.26/9.76% 7.16/8.51% 7.95/9.20% 7.60/9.02% 6.41/7.49% 6.04/7.89%
10M 8.93/10.30% 9.06/10.51% 9.15/10.78% 8.75/10.01% 8.60/10.05% 8.19/9.68%
50M 9.56/11.24% 9.57/11.33% 9.50/11.39% 9.28/10.75% 8.99/10.84% 8.87/10.38%
19

A.2 Experimental Details for Shared Components and Synthetic Data Leakage Study
A.2.1 GLACIER Training and Data Augmentation Configuration
GLACIER [36] is a spectral simulator that generates synthetic MS/MS spectra from molecular
structures. A spectral simulator is also representative of a broader class of reused shared components
in recent MS/MS work, including recent test-time tuning pipelines pretrained on simulated spectra
that include ICEBERG generations [ 66]. Our implementation is based on the https://github.
com/coleygroup/ms-pred codebase. We train two GLACIER variants under controlled conditions:
• Leakage-free GLACIER:Trained only on MassSpecGym training-set spectrum–structure pairs,
with all test and validation molecules excluded. This model represents the data-safe simulator that
respects the benchmark split.
• Adversarial GLACIER:Trained on all 231,104 MassSpecGym spectrum–structure pairs from
the training, validation, and test sets combined, solely to construct an adversarial leakage scenario.
This model is not intended as a deployable simulator; it represents a forward model that has directly
learned spectrum–structure associations from the evaluation sets.
GLACIER jointly trains fragmentation and intensity prediction using a five-layer Graphormer with
hidden size 256, a four-layer fragment decoder, and a three-layer intensity encoder and decoder. We
use dropout 0.1, collision-energy, adduct, formula, element-group, and instrument embeddings, up to
200 fragmentation breakpoints and six broken bonds, and a 20 ppm tolerance. Training uses AdamW
with an effective batch size of 32, learning rate 4×10 −4, no weight decay, 2,000 warmup steps, and
learning-rate decay by 0.9 every 5,000 steps thereafter. The objective combines cosine intensity loss
with fragment supervision, using a base fragment-loss weight of 0.1; the MAGMa supervision weight
is held fixed for 2,500 steps and then decayed by 0.9 every 2,500 steps. Models are trained for up
to 200 epochs, with a minimum of 20 epochs and early-stopping patience of five epochs. For the
adversarial model, the monitored validation fold overlaps with training and serves only as a stopping
diagnostic. No contrastive fine-tuning is performed. Training and synthetic data generation are
performed on one NVIDIA RTX PRO 6000 Blackwell Server Edition GPU. GLACIER is a relatively
lightweight forward model in this setting; training each GLACIER model takes approximately 2
hours.
To examine leakage from simulator training and augmentation targets, we construct four synthetic
augmentation corpora by crossing the two GLACIER variants with two molecule pools. The base
pool is the official set of 4 million unlabeled molecules released with MassSpecGym v1.0, which
excludes molecules within MCES distance 2 of the test set. After excluding two structures whose
formula counts exceed the MIST representation’s supported range, this pool contains 3,922,525
molecules. For each molecule, five collision energies are sampled without replacement from 0 to
100 eV in increments of 5 eV and combined with two instrument types (Orbitrap and QTOF) and
two adducts ([M + H]+ and [M + Na]+), yielding 20 spectra per molecule and 78,450,500 synthetic
spectrum–molecule pairs. The test-spiked pool adds 2,998 MassSpecGym test structures under the
same 20 conditions, adding 59,960 pairs for a total of 78,510,460.
The four corpora correspond to Table 1 as follows: (1) adversarial GLACIER on the test-spiked
pool; (2) adversarial GLACIER on the base pool; (3) leakage-free GLACIER on the test-spiked
pool; and (4) leakage-free GLACIER on the base pool. Comparing Settings 3 and 4 measures the
effect of adding test structures to the augmentation pool while holding the simulator fixed; comparing
Settings 2 and 4 measures the effect of changing the simulator training corpus while holding the
augmentation targets fixed. The adversarial training corpus also includes validation spectra and
spectra with imputed collision energies, so this comparison includes these changes in simulator
training coverage.
A.2.2 MIST Training Configuration with GLACIER Augmentation Data
We train four MIST encoders, each on the MassSpecGym training set combined with one of the four
GLACIER augmentation corpora described above. Every model uses the same 194,119 experimental
spectrum–molecule pairs, mixed with synthetic spectra throughout training. Each effective optimiza-
tion batch contains 8,192 synthetic and 300 experimental pairs. We train for 478,850 optimizer steps,
corresponding to 50 passes through the base synthetic corpus, and use the same training budget and
mixing ratio for all four settings. The encoder in Setting 4 of Table 1 is MIST4M-aug.
20

In each case, the encoder predicts 4096-bit Morgan (ECFP4) fingerprints from peak-formula–
annotated spectra, using positional–cosine formula embeddings, pairwise peak featurization, and up
to 10 peaks. The model has four peak-attention layers with 16 heads, four fingerprint refinement
layers, hidden size 1024, and spectra dropout 0.1. The loss combines cosine fingerprint loss, soft
Tanimoto loss with weight 0.1, and iterative fingerprint supervision with weight 0.4; the MAGMa
auxiliary loss of the original MIST is removed. Optimization uses Adam with peak learning rate
2×10 −4, 9,577 warmup steps followed by cosine decay, weight decay 10−6, gradient clipping at
norm 5.0, bfloat16 mixed precision, and an exponential moving average of model weights with decay
approximately 0.9975. On-the-fly augmentation is applied to half of the spectra, with peak-drop
probability 0.1 and multiplicative intensity jitter with log-scale standard deviation 0.2. We evaluate
every 9,577 steps and select the EMA checkpoint with the highest validation spectrum-to-fingerprint
Tanimoto similarity. A scalar binarization threshold is calibrated on the validation set by matching
the total predicted on-bit count to the total reference on-bit count, then fixed for test evaluation. After
training, each model is benchmarked on the MassSpecGym test set using spectrum-to-fingerprint
Tanimoto similarity and formula-constrained retrieval hit rate. All training and benchmarking are
performed on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU, with training taking
roughly 12 hours per model.
The complete training implementation is available in https://github.com/coleygroup/MIST.
Building on the original https://github.com/samgoldman97/mist implementation, this up-
dated repository provides a modern training framework with native distributed data parallel (DDP)
support and integrated workflows for synthetic spectrum generation and augmented training. We
recommend this repository for future MIST training.
A.2.3 MIST-CF Formula Annotation Components
MIST-CF [39] is a machine learning model that predicts which molecular formula best explains an
MS/MS spectrum from a set of candidate formulas. Because it can provide automated inference of
formulas, it can serve as a formula annotator to pair with formula-aware architectures for evaluation
in the mass-based MassSpecGym challenge tracks. As it may be reused as a fixed auxiliary model,
its training provenance matters for the same reason as that of spectral simulators: a public checkpoint
trained on overlapping data can transmit information into downstream evaluation even when the
downstream split itself is clean.
Table 8:Performance of MIST-CF Trained and Evaluated on the MassSpecGym Benchmark.Versions of
MIST-CF with leakage of test spectra are colored in gray.
MIST-CF training setup Accuracy↑
Top-1 Top-5
Train samples 50.5% 73.2%
Both train and test samples 59.0% 80.5%
Test samples 66.5% 84%
We therefore retrain MIST-CF on the MassSpecGym dataset, as well as two contaminated splits,
and report the top-1 and top-5 formula annotation accuracies in Table 8. MIST-CF is a formula
Transformer that ranks candidate chemical formulas for an observed precursor mass using an energy-
based approach: for each spectrum, a set of candidate formulas is enumerated via the SIRIUS
decomposition algorithm, subformula assignments are precomputed for each candidate peak, and
the model is trained to score the correct formula above a set of sampled decoys. The architecture
uses 2 Transformer layers with hidden size 128, sinusoidal formula embeddings, dropout of 0.1, and
embeds adduct type, instrument type, and neutral-loss fragment formulas as additional covariates; up
to 20 subpeaks and 32 decoy formulas are used per training example. Models are trained with Adam
(learning rate 4.5×10 −4, no weight decay) and a negative log-likelihood loss over the candidate
set. The learning rate schedule applies a 100-step linear warmup followed by exponential decay
at rate 0.88 every 5,000 steps. Training runs for up to 200 epochs with early stopping (patience
5) on validation loss, and the best-validation checkpoint is selected for inference. Training uses
a single NVIDIA H100 GPU with 16 CPU workers and up to 200 GB of memory; all models
(batch size 4) trained to convergence in approximately 7 hours over a maximum of 10 epochs. As
earlier stated, we generate formula candidates from SIRIUS’s mass decomposition algorithm, which
takes the precursor m/z and determines all plausible formulas. We use the SIRIUS default element
21

tolerances, which include a maximum tolerance of 1 for each halogen element (F, Cl, Br, I). Since
this protocol can result in potentially thousands of formula candidates for a single mass, we adopt the
fast-filter model also developed by MIST-CF to filter candidates to a maximum of 256 candidates that
MIST-CF itself needs to consider. This filter model is trained on all formulas present in the original
MassSpecGym pretraining set, with all MassSpecGym test and validation formulas excluded. We
release both the data-safe MIST-CF and the complementary fast-filter model in MassSpecGym v1.5.
The codebase also now supports evaluation of formula-aware models paired with formula annotators
on the mass-based challenge.
Table 9:Additional Results of MIST Retrieval with Top-5 MIST-CF Formula Predictions.Retrieval
performance of MIST on the MassSpecGym mass-based retrieval challenge, using top-5 formula predictions
from three MIST-CF variants (standard, test-only, and train-and-test), aggregated via average or element-wise
max across the five formula-conditioned fingerprint predictions. Inflated results are marked in gray. The values
in parentheses indicate 99.9% BCa bootstrap confidence intervals (20,000 resamples).
Method Hit rate@1↑Hit rate@5↑Hit rate@20↑MCES@1↓
MIST (MIST-CF top-5 formula, element-wise max.) 32.36 (31.23–33.48)% 47.73 (46.49–48.98)% 63.08 (61.93–64.28)% 15.24 (14.87–15.60)
MIST (MIST-CF test-only top-5 formula, average) 34.44 (33.26–35.66)% 49.71 (48.48–50.96)% 65.24 (64.04–66.41)% 14.26 (13.91–14.61)
MIST (MIST-CF test-only top-5 formula, element-wise max.) 35.42 (34.25–36.65)% 49.85 (48.59–51.11)% 64.64 (63.47–65.84)% 14.02 (13.66–14.37)
MIST (MIST-CF train-and-test top-5 formula, average) 34.61 (33.43–35.76)% 50.15 (48.92–51.39)% 65.16 (63.95–66.35)% 14.17 (13.82–14.51)
MIST (MIST-CF train-and-test top-5 formula, element-wise max.) 34.55 (33.33–35.78)% 49.67 (48.48–50.88)% 64.52 (63.39–65.67)% 14.28 (13.94–14.62)
We pair these models’ predictions with MIST4M-aug, a spectrum-to-fingerprint model, by either
using the top-1 formula prediction or aggregating the fingerprints generated from the top-5 formula
predictions by averaging or taking an element-wise maximum. We then perform retrieval (as measured
by lowest Tanimoto distance to the fingerprint) on the mass-based candidates. Prefiltration of the
mass-based candidates to only candidates that match the formula predictions is not applied here. The
main results are reported in Table 2; additional results based on MIST-CF’s top-5 formula predictions
are provided for comparison in Table 9.
A.3 Nearest Neighbor Implementation and Reproduction
Evaluating nearest-neighbor baselines.Khoo and Barzilay [67] recently argued that nearest-
neighbor search outperforms machine learning methods on mass spectrometry. However, their
headline result rests on an evaluation where the nearest-neighbor baseline was scored on an easier
subset of the test set than MIST,11 and where a method based on DreaMS [46] outperforms vanilla
nearest neighbor despite the titular claim. Nevertheless, we recognize nearest neighbor as a useful
reference baseline and include it in the official MassSpecGym setting. Results in Table 3 show that
while nearest neighbor is competitive with some earlier baselines, recent machine learning methods
significantly outperform it. Notably, MIST4M-augoutperforms nearest neighbor by a large margin,
running counter to the claim in Khoo and Barzilay [67]: “These findings contradict the hypothesis
that low performance arises primarily from insufficient training coverage. Simply adding more data
to existing models is unlikely to solve the problem.”
Earlier baseline and split definitions.The baseline described by Khoo [68] returns the fingerprint
of the training spectrum with the highest spectral similarity, without specifying a molecular-formula
restriction. The supplementary methods of Khoo and Barzilay [67] explicitly restrict this search to
training spectra with the query formula. However, in the accompanying implementation, queries
with no same-formula training spectrum are skipped rather than counted as misses, restricting the
evaluation to an easier subset of test queries.12
Separately, the custom MassSpecGym scaffold and random splits in Khoo and Barzilay[67] differ
from the official benchmark splits and exhibit substantial data leakage. In the released dataset files,
95.3% of random-split test spectra have the same molecule present in training, and the leakage
rate is 14.3% for the scaffold split, as confirmed by a follow-up study from the same author [ 42].
11A detailed analysis of the evaluation in Khoo and Barzilay [67], along with code for reproduction, is
available athttps://github.com/coleygroup/Audit_ML_MS_Analysis. Note that on Sep 30, 2026, the
commit history in the official repository was overwritten with updated methods and results that no longer
match the published paper’s table. For reproducibility, a snapshot of the original repository is preserved at
https://github.com/coleygroup/Audit_ML_MS_analysis/tree/original_repo_bkup.
12See02_compute_nn.py at commitda67d9d, where test entries without a matching training formula are
omitted from evaluation.
22

Consequently, in addition to partial test-set coverage, Khoo and Barzilay [67] primarily evaluated
training-set memorization rather than the out-of-distribution generalization targeted by most machine
learning models (and targeted by the official MassSpecGym split). Moreover, the source of identical-
molecule leakage in the scaffold split remains unclear: a standard scaffold split should assign identical
compounds to the same partition, and no open implementation is available to understand the split
creation.
Test-set coverage under formula filtering.Table 10 shows the resulting coverage. On the custom
MassSpecGym scaffold split, the original code evaluates 6,571 of 16,042 test spectra (40.96%) and
omits 9,471. A score averaged over this subset cannot be compared directly with scores over the
full test set. On the official MassSpecGym split, only 2,956 of 17,556 test spectra (16.84%) have a
same-formula training spectrum; applying the same restriction without a fallback would omit 83.16%
of the test set, making it inapplicable in a fair MassSpecGym setting.
Table 10:Same-Formula Training Coverage of MassSpecGym Test Spectra.Counts for the released scaffold
and random splits are obtained from the released files; the final row uses the official benchmark split. Coverage
is the fraction of test spectra with at least one same-formula training spectrum.
Split Test spectra With a formula match Coverage
Released scaffold 16,042 6,571 40.96%
Released random 16,250 15,777 97.09%
Official MassSpecGym 17,556 2,956 16.84%
Updated nearest-neighbor baseline with fallback search.Khoo [42] subsequently adds a fallback
search over the full training library when no same-formula match exists, and introduces a subfor-
mula method that combines fingerprints from multiple neighbors. While every test spectrum now
receives a prediction, Khoo [42] still reports results on the custom splits with the train-test overlap
described above. The subformula method uses the known precursor formula to annotate peaks, aver-
ages neighboring fingerprints, and introduces learnable parameters that are tuned on the validation
set. We reproduce the subformula_only variant,13 evaluating it across all queries in the official
MassSpecGym v1.5 retrieval setting. Under this leakage-free split, the updated nearest-neighbor
baseline remains substantially outperformed by machine learning methods, including MIST4M-aug,
ICEBERG, and GLACIER.
Features, neighbor selection, and fingerprint prediction.For each spectrum, we retain the most
intense peaks (at most 100) and assign fragment subformulas of the precursor ion within a mass
tolerance of max(20 ppm,0.01 Da). Fragment-formula and neutral-loss-formula tokens are weighted
by square-root intensity, taking the maximum weight for repeated tokens, and L2-normalized. Query
tokens absent from the training vocabulary are discarded before normalization. Training spectra
are ranked by token-vector cosine similarity plus α times the heteroatom-weighted Bray–Curtis
similarity of molecular-formula element counts, with weight w for heteroatoms and 1 for carbon
and hydrogen. We average the radius-2, 4096-bit Morgan fingerprints (without chirality) of the
top-k training spectra using softmax weights with temperature T . The required hyperparameter
tuning is performed on all 19,429 official validation spectra by mean fingerprint Jaccard similarity
after thresholding at 0.5, using the same grid as the updated implementation: w∈ {1,2,4,8,16} ,
α∈ {0,0.25,0.5,1,2,4} , T∈ {0.01,0.02,0.05,0.1,0.2,0.5} , and k∈ {1,3,5,10,20,50} . This
givesw= 2,α= 2,T= 0.1, andk= 50.
Retrieval evaluation.For retrieval, we retain the continuous weighted-average fingerprint and rank
the official formula-based candidates by Tanimoto similarity, preserving the supplied candidate order
for ties. All 17,556 test spectra are evaluated, including those without a same-formula training
spectrum. Hit rates at 1, 5, and 20 are 13.13%, 26.56%, and 44.30%, respectively, with MCES@1 of
12.45, as reported in Table 3. We compute 99.9% BCa confidence intervals from 20,000 bootstrap
resamples of test spectra. Our reproduction is available in https://github.com/harrylaucngd/
msms-models.
13Implementation of the new nearest neighbor:ML_MS_analysisat commit6817e9b.
23

A.4 Detailed Formulations of Artifact-Exploiting Stress-Test Baselines
We provide complete technical formulations for the five artifact-exploiting or spectrum-blind baselines
evaluated in Section 5, based on deep audits of the corresponding codebases.
Method 1: DreaMS + ChemBERTa Alignment.This architecture bridges the spectral and
molecular modalities via a lightweight trainable adapter between two pretrained encoders. The
spectral encoder is DreaMS [ 46], a 7-layer Graphormer-style Transformer with 8 attention
heads that encodes MS/MS peaks as ( m/z, intensity) pairs with Fourier positional features,
producing a pooled embedding zs ∈R 1024. The molecular encoder is ChemBERTa-2 [ 47]
(Derify/ChemBERTa_augmented_pubchem_13m), a RoBERTa-style masked language model pre-
trained on 13M SMILES strings, whose CLS-token output zm ∈R 768 provides a SMILES-surface
representation.
The adapter fϕ, a multi-block MLP with N= 8 residual blocks (hidden dim 2048), projects the
DreaMS embedding into ChemBERTa’s latent space: ˆzm =f ϕ(zs). Training jointly optimizes a
bidirectional InfoNCE objective with a learnable temperatureτ:
LInfoNCE =− 1 2B
BX
i=1
"
log eˆzm,i·zm,i/τ P
j eˆzm,i·zm,j /τ + log ezm,i·ˆzm,i/τ P j ezm,i·ˆzm,j /τ
#
,(1)
where the sum is over all B items in a batch, and the positive pair (i, i)is the spectrum–ground-truth-
SMILES pair. A Supervised Contrastive (SupCon) loss with isomer-aware negatives is optionally
added to handle structural ambiguity. Only the adapter fϕ and the last two DreaMS Transformer
layers are trained; ChemBERTa remains completely frozen. At retrieval, candidate molecules are
embedded by ChemBERTa and ranked by cosine similarity to the adapter output ˆzm.
Critical failure mechanism: because ChemBERTa’s training is sensitive to SMILES token-level
syntax, and the ground-truth SMILES consistently originates from non-RDKit sources (retaining
PubChem-style conventions), the adapter learns to produce ˆzm that matches thesyntactic formatting
of the positive pair, rather than encoding mass spectral information.
Method 2: Chemformer Two-Stage Retrieval.This two-stage pipeline builds upon a frozen
Chemformer BART encoder and a jointly trained spectral encoder.
Stage 1 (Pre-Retrieval):The molecular encoder is a frozen Chemformer encoder (BART architecture:
d= 512 , 6 layers, 8 heads, vocabulary size 523 SMILES tokens), producing a CLS embedding
em =f mol(xSMILES)∈R 512. The spectral encoder is an FC(2→512) projection followed by a 6-
layer Transformer encoder with mean pooling: es =f spec(xpeaks)∈R 512. Both are L2-normalized
before computing similarities. Training optimizes a dual-path InfoNCE loss atτ= 0.1:
Lmol2ms = CE

[em,i ·e s,i,e m,i ·e − s,i]/τ,0  ,L ms2mol = CE(EsET m/τ,I),(2)
where e− s,i is an augmented negative spectrum for molecule i, and Lms2mol is a full-batch CLIP-style
contrastive loss. The total loss isL= 0.5(L mol2ms +L ms2mol).
Stage 2 (Generative Retrieval):After Stage 1, the top- K= 40 candidate molecules are precomputed
per spectrum. A cross-fusion module performs cross-attention where the spectral encoder sequence
(queries) attends to the concatenated full-sequence hidden states of the K candidates (keys/values),
producing a context-enriched spectral representation. A Chemformer decoder (6-layer BART, initial-
ized from pretrained weights) then autoregressively generates a SMILES string conditioned on this
cross-fused context via teacher-forcing cross-entropy loss. At inference, beam search (beam size 5)
generates a refined candidate, which is then used to re-rank the initial top-K pool by cosine similarity
between the generated molecule embedding and each candidate embedding.
Failure propagation across stages: Stage 1 inflates the pre-retrieved candidate pool by exploiting the
canonicalization artifact in the InfoNCE training signal. The Stage 2 decoder, conditioned on these
biased top-K candidates, further consolidates the shortcut, since the cross-fusion module learns to
match the formatting signature of the positive candidate that consistently appears near the top of the
Stage 1 ranking.
Method 3: ChemBERTa SMILES Classifier.A spectrum-blind binary classifier built on top of
a pretrained SMILES Transformer [47] (DeepChem/ChemBERTa-77M-MLM, loaded via the Hugging
Face transformers library with a randomly initialized 2-class classification head) that maps a
24

single SMILES string to the probability that it is a ground-truth query molecule rather than a
decoy candidate (i.e., a randomly sampled SMILES from the corresponding candidate list, as per
MassSpecGym_retrieval_candidates_formula.json). The model is fine-tuned for two epochs
with a binary cross-entropy objective on balanced positive/negative pairs. At test time, the classifier
scores each candidate independently and ranks the candidate set in descending order of predicted
probability. No spectral input and no per-query ground-truth information are used at inference time.
Method 4: PubChem Default Ranking.This method exploits the popularity bias described in
Section 5. For a given query, candidates are ranked in the default order returned by the PubChem
PUG-REST API. No spectral information is used. Ground-truth test molecules, being predominantly
well-characterized natural products and common metabolites, systematically rank higher in this
default order, achieving >49% hit rate@1. This baseline aims to expose a critical limitation that any
benchmark whose ground-truth molecules are non-uniformly sampled from chemical space will be
susceptible to this ranking shortcut.
Method 5: Ranking by Number of Chiral Atoms.A spectrum-blind ranker that exploits a
systematic offset between ground-truth molecules and their candidates in the count of annotated
stereocenters. For each candidate moleculec, the ranker computes
n(c) =
X
a∈c
1

a.GetChiralTag()̸=Chem.ChiralType.CHI_UNSPECIFIED

,(3)
the number of atoms a in c carrying an explicit stereochemistry annotation in the SMILES (i.e., @
or @@), evaluated via RDKit’s Chem.MolFromSmiles followed by GetAtoms and GetChiralTag.
Candidates are then ranked by n(c). The ranking direction is decided based on the training set:
descending if ground-truth molecules carry on average more annotated stereocenters than their
candidates, ascending otherwise. The ranker uses no spectral input and no per-query ground-truth
information at test time.
A.5 Pipeline of Annotating Missing Collision Energies in the MassSpecGym Test Set
Because collision energy annotations are incomplete in MassSpecGym, but forward models such as
ICEBERG and GLACIER require collision energy labels, we use a staged workflow for each model
to evaluate it on the full benchmark. We first construct a subset containing spectra with observed
collision energies and train the corresponding simulator on its training split: the fragmentation
and intensity models for ICEBERG, and the joint fragmentation–intensity model for GLACIER.
These models are then used to impute missing collision energies in the original full labels. For
each spectrum lacking a collision energy, the corresponding simulator generates predictions over
a grid of normalized collision energies from 0% to 150% NCE in steps of 5%, converted to eV
using the precursor m/z. The collision energy whose predicted spectrum has the highest spectral
entropy similarity to the experimental spectrum, excluding the precursor region, is selected as a
pseudo-label. The imputed labels are written back into a derived dataset, with retrieval candidate
tables updated to use the same collision-energy values. Finally, each simulator is retrained on
the completed training split and evaluated on the full test split. The ICEBERG pipeline includes
fragmentation training, intensity training, and contrastive intensity fine-tuning; GLACIER uses joint
fragmentation–intensity training without contrastive fine-tuning. This two-pass design preserves
calibration from experimentally annotated spectra while allowing both models to be evaluated on
the full MassSpecGym test set. These ICEBERG and GLACIER results in Table 3 should not be
confused with the “simulation_challenge” setting, where only a subset of training and testing data is
involved.
A.6 Formal Metric Definitions for Reproducible Evaluation
We provide precise, implementation-pinned definitions for each evaluation metric referenced in
Section 6.
InChIKey Hit Rate.An InChIKey is a 27-character identifier whose first 14 characters encode
molecular connectivity. Since MS/MS fragmentation is largely insensitive to stereocenters, two
structures sharing the same connectivity layer should be considered equivalent. Formally, a predic-
tion ˆmis a hit for ground truth m∗ if InChIKey14( ˆm) =InChIKey14(m∗), where InChIKey14(·)
denotes the first 14 characters of the InChIKey. Using the full 27-character InChIKey incorrectly
25

rejects stereoisomers as non-hits and—in data splitting—fails to exclude structurally similar training
molecules that differ only in stereochemistry.
MCES Distance.Given two molecular graphs G1 = (V1, E1) and G2 = (V2, E2), the Maximum
Common Edge Subgraph (MCES) is the largest subgraph (by edge count) isomorphic to a subgraph
of both. The MCES distance is:
dMCES(G1, G2) =|E1|+|E 2| −2|MCES(G1, G2)|.(4)
Since computing MCES exactly is NP-hard, we use myopic-mces 1.0.0 with PuLP 2.9.0 and the
PULP_CBC_CMD solver. We set threshold=15 and always_stronger_bound=True, with a solver
time limit of 5 seconds. Stereochemistry is ignored during graph comparison.
Tanimoto Fingerprint Similarity.Let A and B be binary fingerprint vectors of a predicted and
ground-truth molecule. Tanimoto similarity is:
T(A, B) =
P
i AiBiP
i Ai + P i Bi − P i AiBi .(5)
Fingerprints must be ECFP4 Morgan fingerprints computed with radius r= 2
and n= 2048 bits (via rdkit.Chem.AllChem.GetMorganFingerprintAsBitVect or
rdkit.Chem.rdFingerprintGenerator.FPType.MorganFP).
Close and Meaningful Match Rates.The Close Match and Meaningful Match metrics are comple-
mentary structural similarity metrics introduced outside the original MassSpecGym benchmark in
[69]. AClose Matchrequires T(A, B)≥0.675 , and aMeaningful Matchrequires T(A, B)≥0.40 ,
where T is Tanimoto similarity computed with the defaultRDKitfingerprint instead of ECFP4 (i.e.,
via rdkit.Chem.rdFingerprintGenerator.FPType.RDKitFP). Any deviation from the RDKit
fingerprint should be explicitly reported.
Confidence Intervals.Per-example metric values (e.g., per-molecule InChIKey hits or per-prediction
Tanimoto similarities) are aggregated by their mean across the test set. To quantify uncertainty around
this mean, BCa bootstrap confidence intervals are computed: the test-set values are resampled with
replacement 20,000 times, the mean is recomputed on each resample, and bias-corrected and acceler-
ated percentile levels are used to obtain the lower and upper bounds of the 99.9% confidence inter-
val. We use scipy.stats.bootstrap with confidence_level=0.999, n_resamples=20000,
method=’BCa’, and a fixed random seed for reproducibility.
A.7 Metric-Implementation Sensitivity Tables
Table 11 shows the influence of evaluation metric parameters on FRIGID performance. High deviation
in the results highlights the importance of keeping metric implementations consistent with the original
reference implementations (e.g., the ones implemented in the MassSpecGym codebase).
A.8 Agentic Infrastructure for Automated Leaderboard Submission and Code Review
To operationalize the recommendations of this audit and reduce the burden of manual review,
MassSpecGym v1.5 introduces a structured submission workflow for new leaderboard entries. Au-
thors submit a pull request to the main repository containing the relevant results, code, and a model
card that specifies method metadata including paper and code URLs, pretraining data and filtering
criteria, oracle component versions, and evaluation setup. On every pull request, a GitHub Actions
workflow automatically runs a review script, which performs an analysis and heuristic checks covering
all failure modes identified in this paper and generates a narrative review of the method. Hard failures
must be resolved unless maintainers document an override; warnings require explicit maintainer
sign-off. A second workflow runs on every merge to main and validates the full set of results for
schema consistency and confidence interval coverage. A maintainer review guide documents residual
judgment calls beyond a static analysis, which includes reading the paper methods section for implicit
formula use, verifying pretraining data safety against the InChIKey exclusion list, and spot-checking
reproducibility. The system prompt and skill to guide the code review are shown below. Examples of
identifying issues in a submission are shown in Figures 3 and 4. This resource is intended to support
both the maintainers and users of MassSpecGym with updating the leaderboard and contributors with
additional guardrails and feedback in the development of new models.
26

Table 11:Comparison of Metric Variants on Identical FRIGID Predictions for the MassSpecGymde
novoGeneration Challenge w/Bonus.Predictions are from FRIGID with MIST4M-augafter 10 refinement
rounds on all 17,556 test spectra; parentheses show 99.9% BCa confidence intervals (20,000 spectrum-level
resamples, seed 42). “r” denotes the Morgan fingerprint radius, “thld” denotes the MCES threshold parameter
below which exact computation is attempted, and “bound” denotes thealways_stronger_bound parameter
in the MCES implementation. Black rows show the reference implementation; gray rows show alternative
implementations.
Metric Variant Top-1 Top-10
Accuracy InChIKey-14 9.05 (8.35–9.74)% 12.23 (11.42–13.04)%
Accuracy Full InChIKey 4.97 (4.45–5.54)% 6.80 (6.15–7.47)%
Tanimoto Morganr= 2, 1024 bits 0.3969 (0.3906–0.4033) 0.4435 (0.4371–0.4501)
Tanimoto Morganr= 2, 2048 bits 0.3873 (0.3808–0.3938) 0.4328 (0.4262–0.4394)
Tanimoto Morganr= 2, 4096 bits 0.3827 (0.3763–0.3893) 0.4276 (0.4210–0.4344)
Tanimoto Morganr= 3, 1024 bits 0.3399 (0.3336–0.3463) 0.3871 (0.3805–0.3938)
Tanimoto Morganr= 3, 2048 bits 0.3257 (0.3193–0.3322) 0.3712 (0.3645–0.3780)
Tanimoto Morganr= 3, 4096 bits 0.3189 (0.3124–0.3255) 0.3635 (0.3566–0.3705)
MCES thld=100, bound=False 37.99 (37.03–38.89) 28.90 (28.05–29.72)
MCES thld=15, bound=False 12.56 (12.40–12.72) 11.32 (11.17–11.47)
MCES thld=15, bound=True 12.60 (12.45–12.76) 11.41 (11.26–11.56)
SKILL.md
---
name: review
description: Maintainer guide for reviewing MassSpecGym leaderboard submissions.
Covers interpreting the automated review report, performing judgment calls
the automation cannot make, and approving or rejecting PRs. The automated
review (scripts/review_submission.py, triggered by the review_submission GH
Action) handles deterministic checks; this guide covers the residual human
review.
,→
,→
,→
,→
,→
---
# MassSpecGym Submission Review — Maintainer Guide
## Role of this guide
Every leaderboard PR triggers`scripts/review_submission.py`automatically and
posts a structured report as a PR comment. That report handles all
deterministic checks (schema, CIs, tier integrity, MIST bug, pretraining
filter, metric overrides). **Your job as maintainer is to:**
,→
,→
,→
1. Read the automated report and triage any WARNINGs that require judgment
2. Fetch and read the paper if the automated LLM review flagged concerns or
couldn't access the paper,→
3. Check items the automation explicitly cannot verify (listed below)
4. Approve or request changes
Hard failures in the automated report must be resolved by the author before you
even look at the PR. Do not override hard failures without a documented
reason.
,→
,→
---
## Submission requirements (what a valid PR must contain)
1. A new row in the correct`results/*.csv`with all required metrics and 99.9%
BCa bootstrap CIs,→
2. A`submissions/<method_name>/model_card.yaml`filled from the template
27

The method name in the CSV`Method`column must exactly match`method_name`in
`model_card.yaml`(underscored folder name, spaced method name). See
`submissions/SUBMISSION_GUIDE.md`.
,→
,→
---
## Step 1: Read the automated report
The PR comment from the review bot contains:
- **Hard failures** — must be fixed; CI blocks merge
- **Warnings** — require your sign-off; use a PR review comment to document your
decision,→
- **LLM narrative review** — treat as a second opinion; verify any specific
issues it flags,→
For warnings, document your reasoning inline on the PR before approving.
---
## Step 2: Things the automation cannot check — do these manually
### 2a. Paper methods section vs. model card
Read the paper's methods/data section and cross-check against`model_card.yaml`:
- Does the paper describe using ground-truth test formulas, directly or to
filter candidates, in the **mass-based** (standard) challenge? If yes and
the model is submitted to`results/retrieval.csv`(notbonus), reject.
,→
,→
- Does the paper describe pretraining on data sources *not listed* in the model
card? Flag the discrepancy.,→
- Does the paper use ICEBERG-generated spectra for pretraining? Check which
ICEBERG version (data-safe v1.5 or upstream). If unclear, ask the author.,→
- Does the paper's reported number match the CSV entry? Values that differ from
the paper by >0.5 pp on the primary metric need explanation.,→
### 2b. Spectrum-blind shortcut check (S2)
If the model is a retrieval model, mentally check: could a model that ignores
the spectrum entirely (using the PubChem PUG-REST API's default return order
or SMILES format) achieve similar results?
,→
,→
The PubChem default-ranking baseline achieves 49.98% hit rate@1 on the
formula-based retrieval task. If the submission's hit rate@1 is at or below
this level, it may not be learning from spectra at all. Ask the author to
compare against the PubChem default-ranking baseline if not already
included.
,→
,→
,→
,→
**Spectrum-blind classifier test (run if suspicious):** The ChemBERTa SMILES
classifier achieves 99.66% hit rate@1 on non-canonicalized candidate sets.
If the candidate set for this submission is non-standard, ask the author to
confirm the v1.5 pre-canonicalized candidate set is used.
,→
,→
,→
If you have access to compute: train or run a version of the model with the
spectral input zeroed out or permuted. If performance stays substantially
above random (~1/pool_size), the model likely exploits a spurious
correlation and should be investigated further before acceptance.
,→
,→
,→
### 2c. Pretraining data — if no parquet provided
If`pretraining.used=true`but no parquet URL is given, ask the author to
either:,→
- Provide a public parquet for the InChIKey overlap check, or
28

- Run`python -m massspecgym.data.sanity_check --input their_data.parquet
--inchikey-col inchikey_14`themselves and share the output,→
Do not accept claims of data safety without this check if pretraining is
declared.,→
### 2d. Reproducibility spot-check
If the submission includes a checkpoint or inference script, spot-check one
metric:,→
```bash
# In the massspecgym conda environment (Python 3.11)
git clone <author-fork-url>
cd MassSpecGym
pip install -e ".[dev]"
python scripts/run.py \
--job_key review_run \
--run_name <model_name>_review \
--test_only \
--no_wandb \
--seed 42
```
A discrepancy >0.5 pp on the primary metric requires explanation. If the author
cannot provide a reproducible checkpoint, note this in your review but it is
not grounds for automatic rejection — reproducibility is aspirational for
submissions without public checkpoints.
,→
,→
,→
---
## Step 3: Metric specifications (reference)
All submitted metrics must match these pinned implementations:
| Metric | Specification |
|--------|--------------|
| InChIKey hit rate | First 14 characters (connectivity layer) only — **not**
full 27-char |,→
| Tanimoto similarity | Morgan ECFP4, radius=2, 2048 bits |
| MCES distance |`threshold=15`,`always_stronger_bound=True`— see
`massspecgym/utils.py:MyopicMCES`|,→
| Cosine similarity | Standard MS/MS cosine as in`massspecgym`|
| Jensen-Shannon similarity | As in`massspecgym`|
**Do not accept** metric implementations reimported from third-party codebases
unless independently verified against the specifications above.,→
---
## Step 4: Required metrics per task
### De novo (standard andBonus)
`Top-1 Accuracy`,`Top-1 MCES`,`Top-1 Tanimoto`,`Top-10 Accuracy`,`Top-10
MCES`,`Top-10 Tanimoto`— all required, all with CIs.,→
### Retrieval (standard)
`Hit rate @ 1`,`Hit rate @ 5`,`Hit rate @ 20`,`MCES @ 1`— all required, all
with CIs.,→
### Retrieval (Bonus)
`Hit rate @ 1`,`Hit rate @ 5`,`Hit rate @ 20`,`MCES @ 1`— all required, all
with CIs.,→
29

### Simulation (standard andBonus)
`Cosine Similarity`,`Jensen-Shannon Similarity`,`Hit rate @ 1`,`Hit rate @
5`,`Hit rate @ 20`— all required, all with CIs.,→
Standard andbonusvariants must not be compared in the same table row. A model
submitted to both must have two separate CSV rows.,→
---
## Step 5: MIST batching bug (I1) — background
If a submission uses the MIST encoder from an external codebase (not
`massspecgym/models/encoders/mist/`), verify the attention masking in
batched inference. The original MIST encoder added`attn += attn_mask`
without first converting the boolean mask to`-inf`, which allows padding
tokens to contribute to the softmax. The v1.5 MassSpecGym MIST encoder has
this fixed.
,→
,→
,→
,→
,→
**Observed checkpoint issue:** For MIST vDiffMS + MolForge, increasing inference
batch size from 1 to 24 raises encoder Tanimoto similarity from 0.457 to
0.812 and de novo top-1 accuracy from 10.73% to 31.75%. The documented
training recipe does not reproduce this inflation.
,→
,→
,→
**What to look for:**
```python
# BUG (wrong):
attn += attn_mask
# SUBTLE BUG — fix code present but result discarded:
new_attn_mask = torch.zeros_like(attn_mask, dtype=q.dtype)
new_attn_mask.masked_fill_(attn_mask, float("-inf"))
attn += attn_mask # still uses raw bool mask, new_attn_mask silently ignored
# FIX (correct):
new_attn_mask = torch.zeros_like(attn_mask, dtype=q.dtype)
new_attn_mask.masked_fill_(attn_mask, float("-inf"))
attn += new_attn_mask
```
The v1.5 MassSpecGym MIST encoder
(`massspecgym/models/encoders/mist/transformer_layer.py`) already applies
the fix. If the submission imports from there, this is satisfied.
,→
,→
---
## Step 6: Data leakage — gradient of stringency
Data leakage is not binary. Performance can remain sensitive to filtering out
close structural analogs even after exact test matches are excluded. This
means a model may claim "clean" data (exact-match excluded) while still
benefiting substantially from near-neighbor contamination.
,→
,→
,→
**What to report in your review:**
- What filtering criterion is declared in the model card?
- Is this consistent with what the paper states?
- Does the paper compare against baselines at the same filtering level?
The leaderboard accepts exact-match exclusion as the minimum. If the criterion
is weaker or unstated, request clarification before approval.,→
---
## Final approval checklist
30

Before approving the PR, confirm:
- [ ] Automated report has no hard failures (or failures have been resolved and
re-reviewed, or explicitly overridden with a documented reason),→
- [ ] All warnings have been signed off with a documented reason
- [ ] Paper methods section consistent with model card
- [ ] No ground-truth test formula use in a mass-based submission (from reading
the paper),→
- [ ] Pretraining data safety confirmed (parquet sanity check run or author
confirmed),→
- [ ] If MIST encoder used: v1.5 fix confirmed or external repo verified
- [ ] If MIST-CF or ICEBERG used: v1.5 data-safe version confirmed
- [ ] All required metrics present with CIs
- [ ] Method name in CSV matches model card exactly
- [ ]`df_test_path`configured so per-sample predictions are saved
(recommended),→
- [ ] Seed documented
31

A contributor
contributor main
maintainerM
A
[…]
Figure 3: Example 1 of an LLM-enabled workflow for reviewing submissions to the MassSpecGym leaderboard.
When a contributor submits a pull request for their model to be featured in the leaderboard, an automated GitHub
Action workflow is triggered that parses through the provided model card and source code to review according to
the guidelines outlined in the provided skill (vide supra) based on this publication. The output of the workflow is
a set of errors, warnings and recommendations for a human maintainer. Once approved, the source code files are
deleted, the model card is kept and the leaderboard updated.
A contributor
contributor main
Figure 4: Example 2 of an LLM-enabled workflow for reviewing submissions to the MassSpecGym leaderboard.
Similarly to Figure 3, the output of the workflow is a set of errors, warnings and recommendations for a human
maintainer. The workflow correctly identifies data leakage due to stereoisomers and the MIST inference bug.
32
