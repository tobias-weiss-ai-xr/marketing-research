---
title: 'Contrastive Bi-Encoder Models for Multi-Label Skill Extraction: Enhancing ESCO Ontology Matching
  with BERT and Attention Mechanisms'
url: https://arxiv.org/abs/2601.09119
category: consumer-behavior
subcategory: empirical
date: 2026-01
venue: ''
authors:
- Yongming Sun
source: arxiv
pdf_url: https://arxiv.org/pdf/2601.09119
pages: 15
chars: 49917
fetched_at: '2026-11-08T13:15:01+00:00'
kb_version: 1
---

# Contrastive Bi-Encoder Models for Multi-Label Skill Extraction: Enhancing ESCO Ontology Matching with BERT and Attention Mechanisms

CONTRASTIVEBI-ENCODERMODELS FORMULTI-LABELSKILL
EXTRACTION: ENHANCINGESCO ONTOLOGYMATCHING WITH
BERTANDATTENTIONMECHANISMS
Yongming Sun
School of Economics
Zhejiang University
Hangzhou, China
yongming.sun@zju.edu.cn
January 15, 2026
ABSTRACT
Fine-grained labor market analysis increasingly relies on mapping unstructured job advertisements to
standardized skill taxonomies such as ESCO. This mapping is naturally formulated as an Extreme
Multi-Label Classification (XMLC) problem, but supervised solutions are constrained by the scarcity
and cost of large-scale, taxonomy-aligned annotations—especially in non-English settings where
job-ad language diverges substantially from formal skill definitions. We propose a zero-shot skill
extraction framework that eliminates the need for manually labeled job-ad training data. The
framework uses a Large Language Model (LLM) to synthesize training instances from ESCO
definitions, and introduces hierarchically constrained multi-skill generation based on ESCO Level-2
categories to improve semantic coherence in multi-label contexts. On top of the synthetic corpus,
we train a contrastive bi-encoder that aligns job-ad sentences with ESCO skill descriptions in a
shared embedding space; the encoder augments a BERT backbone with BiLSTM and attention
pooling to better model long, information-dense requirement statements. An upstream RoBERTa-
based binary filter removes non-skill sentences to improve end-to-end precision. Experiments show
that (i) hierarchy-conditioned generation improves both fluency and discriminability relative to
unconstrained pairing, and (ii) the resulting multi-label model transfers effectively to real-world
Chinese job advertisements, achieving strong zero-shot retrieval performance (F1@5 = 0.72) and
outperforming TF–IDF and standard BERT baselines. Overall, the proposed pipeline provides
a scalable, data-efficient pathway for automated skill coding in labor economics and workforce
analytics.
KeywordsZero-shot learning; extreme multi-label classification; skill extraction; synthetic data generation; contrastive
learning; ESCO
1 Introduction
Understanding labor market dynamics increasingly requires measurement at the skill level [Turrell et al., 2019].
Standardized taxonomies such as the European Skills, Competences, Qualifications and Occupations (ESCO) [European
Commission] provide a controlled vocabulary that supports comparability across firms, regions, and time. However,
real-world job advertisements are written in informal, heterogeneous language and often express requirements implicitly
(e.g., through tasks, tools, or domain context). Bridging this gap—mapping job-ad text to a large set of standardized
skills—naturally yields an Extreme Multi-Label Classification (XMLC) problem with a very large label space and
strong label correlations.
The main obstacle for supervised XMLC in this domain is data availability. Training strong discriminative models
typically requires large corpora of job sentences annotated with taxonomy-specific skill codes, which are expensive
arXiv:2601.09119v1  [cs.CL]  14 Jan 2026

and slow to construct, difficult to maintain as taxonomies evolve, and especially scarce for non-English labor markets.
As a result, many practical systems fall back on keyword rules or generic similarity matching. These approaches are
brittle under vocabulary mismatch (synonyms, paraphrases, and local jargon) and struggle to capture compositional and
contextual skill expressions (e.g., “experience deploying models in production” implying MLOps-related skills).
This paper proposes azero-shotpipeline that bypasses manual job-ad annotation while still learning a skill-aware
representation aligned to ESCO. The core idea is to use ESCO skill definitions as supervision: we synthesize training
instances with a Large Language Model (LLM) and train a contrastive bi-encoder to align (sentence, skill-definition)
pairs in a shared embedding space. A key design choice ishierarchically constrained generation: instead of sampling
arbitrary multi-skill combinations, we condition multi-skill synthesis on ESCO Level-2 categories to induce more
realistic co-occurrence structure and reduce semantic drift. In addition, we include an upstream binary filter to discard
non-skill sentences before retrieval, improving precision and computational efficiency in end-to-end processing.
Our main contributions are:
• Hierarchy-conditioned synthetic supervision:We propose an LLM-based data generation strategy that
leverages ESCO’s hierarchy (Level-2 constraints) to produce more semantically coherent multi-skill training
instances than unconstrained pairing.
• Contrastive zero-shot XMLC for skills:We train a contrastive bi-encoder that aligns job-ad sentences with
ESCO skill definitions without using any manually labeled job-ad training data, enabling scalable zero-shot
retrieval over large skill sets.
• An end-to-end extraction pipeline:We combine a RoBERTa-based binary sentence filter with multi-label
retrieval, and show strong transfer to real-world Chinese job advertisements with substantial gains over TF–IDF
and standard BERT baselines.
The remainder of the paper is organized as follows. Section 2 reviews related work. Section 3 introduce our data.
Section 4 describes the proposed pipeline, including data generation and model training. Section 5 introduces the
experimental setup. Section 6 reports results, ablations, and robustness analyses. Section 7 concludes.
2 Related Work
Our work connects three strands of research: (i) extreme multi-label text classification (XMLC), (ii) skill extraction for
labor market intelligence, and (iii) LLM-driven synthetic supervision and contrastive retrieval. Below, we summarize
the most relevant lines of work and clarify how our framework departs from existing approaches.
2.1 Extreme Multi-Label Text Classification (XMLC)
XMLC concerns prediction over very large label spaces, often with severe label imbalance and strong label correlations.
Classical solutions used sparse linear one-vs-rest formulations [Babbar and Schölkopf, 2017, Yen et al., 2016], including
methods that emphasized optimization and sparsity to make training feasible at scale. While effective in some regimes,
these approaches typically rely on surface-feature engineering and do not explicitly model label semantics, making
transfer to new domains or label sets difficult.
More recent work has adopted deep and pretrained language-model (PLM) backbones. A prominent direction uses
tree or graph structures over labels to reduce computational cost at inference time [Prabhu et al., 2018], while another
line directly leverages Transformer encoders with attention mechanisms to improve ranking quality [You et al., 2019,
Jiang et al., 2021]. Despite strong supervised performance, most state-of-the-art XMLC systems assume access to large
amounts of labeled data and are sensitive to distribution shifts.
In contrast, our setting is explicitlyzero-shotwith respect to job-ad labels: we aim to predict ESCO skills without
manually annotated job advertisements. Instead of learning label-specific classifiers from labeled examples, we cast
XMLC as a retrieval problem in a shared semantic space, where the label side is represented by ESCO definitions and
related textual metadata. This choice naturally supports scalability to large ontologies and mitigates the dependency on
task-specific annotation.
2.2 Skill Extraction and Labor Market Intelligence
Skill extraction is a core component of labor market intelligence, enabling measurement of changing demand, skill
complementarities, and occupational transitions. Earlier pipelines commonly formulated skill detection as named entity
2

recognition (NER) or dictionary matching, sometimes augmented with rule-based normalization. These methods are
interpretable and efficient, but they are brittle to paraphrase, domain drift, and the long-tail of job-ad language.
Supervised learning approaches (e.g., sequence labeling or multi-class classification) [Zhang et al., 2022, Le et al.,
2019] improve recall and robustness but are constrained by the availability and coverage of annotated corpora. This
bottleneck is particularly acute for comprehensive taxonomies such as ESCO or O*NET, where label sets are large and
definitions are fine-grained.
A further practical challenge isvocabulary mismatch: job ads frequently use informal phrasing, abbreviations, and firm-
specific terminology that diverge from ontology definitions. Several studies address this via similarity-based matching
between job text and taxonomy entries [Bhola et al., 2020, Decorte et al., 2021]; however, naïve similarity metrics often
fail under paraphrase and do not learn domain-appropriate alignment. Our approach targets this mismatch by learning a
contrastive bi-encoder that embeds job-ad sentences and ESCO skill definitions into a unified representation space,
explicitly optimizing semantic alignment rather than relying on fixed lexical overlap.
2.3 LLM-Driven Synthetic Supervision
The lack of labeled data has motivated synthetic supervision via large language models (LLMs) [Ding et al., 2023, Wang
et al., 2021, West et al., 2022, Ye et al., 2022], including prompt-based augmentation, self-instruction, and automatic
labeling. Across many NLP tasks, synthetic data can yield competitive models when real annotation is costly, provided
that the synthetic distribution is sufficiently diverse and the labeling rules are reliable.
Within skill extraction, the main difficulty is not only generating fluent text but generatingtask-faithfulsamples that
reflect realistic co-occurrence patterns and decision boundaries. Purely random or unconstrained generation can lead to
artifacts (e.g., overly stereotyped phrasing, unrealistic label combinations, or overly clean separability), which in turn
produces models that appear strong on synthetic validation but transfer poorly to real job ads.
We address this by introducing ahierarchically constrainedgeneration strategy that conditions the LLM on ESCO
Level-2 structure. Constraining multi-skill samples to remain within coherent ESCO subtrees encourages more plausible
co-occurrence and reduces spurious correlations. In effect, the ESCO hierarchy acts as distant supervision: it injects
structural priors into synthetic data so that the learned model better reflects the ontology’s semantics while remaining
agnostic to any manually labeled job-ad corpus.
2.4 Contrastive Learning for Semantic Retrieval
Contrastive learning has become a standard approach for training sentence and passage embeddings for semantic
retrieval [Gao et al., 2021]. Bi-encoder architectures [Reimers and Gurevych, 2019] are particularly attractive in
large-label settings because they support efficient approximate nearest-neighbor search and decouple encoding of
queries (job sentences) and candidates (skill definitions). Typical training objectives pull matched pairs together while
pushing apart negatives sampled within a batch or from hard-negative mining [Robinson et al., 2021].
We adopt this retrieval framing for XMLC (sentence-to-skill matching) and implement a contrastive objective that treats
a sentence and its target ESCO skill definition as a positive pair. Importantly, negative sampling is central in this setting:
the model must discriminate between semantically adjacent skills (hard negatives), not only between unrelated concepts.
Our ablation results highlight how margin choice and the number of negatives govern the trade-off between ranking
quality and training efficiency.
Finally, while many bi-encoder systems rely solely on the [CLS] representation, job-ad sentences often contain long,
compositional requirements with multiple constraints. We therefore augment the PLM backbone with lightweight
sequence modeling and pooling (e.g., BiLSTM plus attention pooling) [Conneau et al., 2017] to better aggregate
distributed evidence across the sentence, improving robustness when skill cues are not localized to a single token span.
3 Data
Our study utilizes two primary data sources: a standardized skills taxonomy for synthetic generation and a large-scale
corpus of real-world job advertisements for evaluation and application.
3.1 Standardized Taxonomy: ESCO
We adopt theEuropean Skills, Competences, Qualifications and Occupations(ESCO) ontology (v1.1) as our ground
truth for skill definitions. ESCO provides a comprehensive, hierarchical classification of skills relevant to the EU
3

labor market but applicable globally. The taxonomy is structured into four levels, ranging from broad categories (e.g.,
"Language and communication") to granular skills.
For this study, we focus on the leaf nodes of the hierarchy, specifically theLevel-4 skills, resulting in a total of13,890
distinct skill concepts. Each concept is associated with a preferred label and a textual description (e.g.,"Python
(computer programming): The techniques and principles of software development, such as analysis, algorithms, coding,
testing and compiling of programming paradigms in Python."). These descriptions serve as the seed text for our
synthetic data generation pipeline.
3.2 Real-World Job Advertisements
To evaluate the zero-shot transfer capabilities of our model, we curate a dataset of real-world job postings collected
from Zhaopin.com, one of the largest online recruitment platforms in China. The raw corpus spans a nine-year period
from2015 to 2023, covering a diverse range of industries, regions, and job types.
From this massive collection, we construct a representative experimental dataset by randomly sampling200,000 job
advertisements. Each advertisement contains unstructured text fields describing job responsibilities and requirements.
We pre-process this text by segmenting it into individual sentences based on punctuation (periods, question marks,
and exclamation points), resulting in a pool of variable-length sentences that mix skill requirements with general
administrative information (e.g., "salary negotiable", "location: Beijing"). This real-world dataset presents significant
challenges, including colloquialisms, implied skills, and noisy formatting, which our pipeline is designed to address.
4 Methodology
We propose an Extreme Multi-Label Classification (XMLC) framework that maps real-world job vacancy text to the
standardized European Skills, Competences, Qualifications and Occupations (ESCO) skill ontology. Because large-scale
human-annotated job posting data are scarce, our approach isannotation-free on real postings: we rely on synthetic
supervision constructed from ESCO and an LLM, and then transfer the learned semantic matching capability to real job
ads.
Given a job ad, we segment it into sentences and perform a three-stage workflow: (1) synthetic data generation and
pre-processing, (2) contrastive bi-encoder training, and (3) inference via semantic retrieval and aggregation.
4.1 Synthetic Data Generation
ESCO localization.ESCO (v1.1.2) provides 13,896 distinct skills. Since our target corpus consists of Chinese job
postings, we manually translate ESCO skill names and definitions into Chinese and use the translated descriptions
consistently throughout training and inference.
Positive samples.We construct synthetic sentences using the DeepSeek-V3 LLM conditioned on ESCO skills. We
generate two types of positive samples to reflect different supervision granularity:
• Single-skill samples ( Dsingle).For each skill s∈ S, we generate a set of job-ad-like sentences Ts =
{t1, t2, . . .}that express skillsin realistic requirement language. The resulting training pairs are(t, s).
• Co-occurring skill samples ( Dmulti).To model realistic multi-skill requirements, we generate sentences
conditioned on skill pairs (si, sj). To encourage semantic coherence, we sample pairs from the same Level-2
ESCO category as a weak structural constraint. The resulting samples are(t,{s i, sj}).
We describe the per-skill generation count|T s|later (and provide prompt templates in the appendix).
Negative samples (Dnone).To train a sentence-level filter that removes non-requirement content, we additionally
generate negative sentences typical of job ads (e.g., company introductions, benefits, compliance statements) that
contain no explicit skill requirements.
Decoding settings and quality control.We use stochastic decoding with temperature T= 0.7 and nucleus sampling
top-p= 0.9 (maximum 128 tokens per sentence) to encourage lexical diversity while preserving instruction-following.
To mitigate near-duplicates and style artifacts:
• De-duplication.We remove exact duplicates and near-duplicates by thresholding cosine similarity between
sentence embeddings (Sentence-BERT) and discarding samples above a high similarity cutoff.
4

• Diversity enforcement.For each skill, we enforce minimum lexical variation (e.g., avoiding repeated n-grams
across generated sentences) and resample when violations occur.
Handling generic or overlapping skills.ESCO includes skills whose definitions are broad or lexically similar (e.g.,
generic soft skills). Such skills can induce ambiguous supervision and unstable retrieval. We therefore apply two
safeguards:
• Ambiguity-aware sampling.For skills whose translated definitions have unusually high similarity to many
other skills, we increase diversity constraints and require generated sentences to include job-context anchors
(role/task cues) beyond generic phrasing.
• Evaluation-time disambiguation.During retrieval, we rely on similarity thresholding (Section 4.5) and
sentence-to-posting aggregation to reduce spurious activation from generic sentences.
4.2 Data Pre-processing and Filtering
Real-world job postings contain substantial non-requirement content. Before skill retrieval, we apply a sentence-level
binary filter to retain only sentences that are likely to express skill requirements.
We fine-tune a RoBERTa-base classifier on a balanced dataset withDsingle as positives and Dnone as negatives, using
standard binary cross-entropy. During inference, a sentencetis discarded if
P(skill|t)< τ,(1)
where τ is selected on a held-out validation set to achieve a desired precision–recall trade-off (we prioritize high
precision to reduce downstream false positive skills).
4.3 Contrastive Bi-Encoder Architecture
We formulate XMLC as semantic retrieval: embed a job-ad sentence and each candidate ESCO skill into a shared vector
space, then retrieve the nearest skills.
4.3.1 Encoder Backbone
We use a Siamese bi-encoder withshared parametersfor both towers. The encoder ϕ(·) is initialized with
bert-base-chinese. Given an input sequence x (either a job-ad sentence t or a translated skill description s),
we extract contextualized token embeddings H∈R L×h from the last hidden layer, where L is the sequence length and
h= 768 is the hidden size. To better capture local sequential patterns and salient keywords in skill-related text, we
augment the Transformer outputs with a BiLSTM and an attention pooling layer [Yang et al., 2016]:
1.BiLSTM.We passHthrough a bidirectional LSTM:
Hlstm = BiLSTM(H)∈R L×2h′ ,(2)
whereh ′ = 256is the hidden size of each LSTM direction.
2. Attention pooling.We compute a weighted aggregation of the LSTM outputs to form a fixed-size representa-
tion. Concretely, we first compute a scalar score for each token positionℓ∈ {1, . . . , L}:
uℓ =w ⊤ tanh(W Hlstm,ℓ),(3)
where Hlstm,ℓ ∈R 2h′ denotes the ℓ-th token vector, W∈R a×2h′ and w∈R a are trainable parameters, and a
is the attention hidden dimension. We then normalize scores with a softmax over token positions:
αℓ = exp(uℓ)PL
j=1 exp(uj)
.(4)
The pooled representation is
v=
LX
ℓ=1
αℓHlstm,ℓ ∈R 2h′ .(5)
5

3.Projection.The final embedding is obtained via a linear projection followed byL 2 normalization:
e(x) = Wpv+b ∥Wpv+b∥ 2 ∈R d,(6)
where Wp ∈R d×2h′ , b∈R d, and we set d= 128. We denote sentence embeddings as et =e(t) and skill
embeddings ase s =e(s).
4.4 Training Objective
We train the model with a margin-based contrastive ranking objective. For a positive pair(t, s+), we sample K negative
skills [Robinson et al., 2021] {s− 1 , . . . , s− K} such that s− k /∈ Y(t), where Y(t) is the set of ground-truth skills used to generatet. Letsim(·,·)denote cosine similarity. The loss is
L(t, s+) = 1 K
KX
k=1
max

0, λ−sim(et, es+ ) + sim(et, es− k )

,(7)
whereλ= 0.5is the margin. For multi-label samples(t,{s 1, s2}), we average over positives:
Lmulti(t,{s 1, s2}) = 1 2  L(t, s1) +L(t, s2)  .(8)
4.5 Inference and Retrieval
We pre-compute embeddings for all translated ESCO skills S, yielding an index matrix ES ∈R |S|×d. For each filtered
sentence t, we compute et and retrieve candidates by cosine similarity. We then apply a similarity threshold to control
precision:
ˆS(t) =
n
s∈TopK s′∈S sim(et, es′)

 sim(et, es)≥γ o ,(9)
whereKis a fixed retrieval budget andγis tuned on validation data.
Posting-level aggregation.Given a job posting consisting of sentences {tm}M m=1, we produce the posting-level
predicted skill set via union aggregation:
ˆSpost =
M[
m=1
ˆS(t m)(10)
This union rule reflects the fact that job postings typically list multiple independent requirements across different
sentences.
5 Experiments
We conduct a comprehensive series of experiments to evaluate ourannotation-free transferpipeline for mapping real-
world Chinese job vacancies to standardized ESCO skills. The experiments are designed to answer three questions: (i)
whether the LLM-generated synthetic supervision is fluent and diverse, (ii) whether the sentence-level filter effectively
removes non-requirement content without suppressing genuine requirements, and (iii) whether the contrastive bi-encoder
learns a robust alignment between job-ad language and ESCO skill definitions that transfers to real postings.
5.1 Experimental Setup
All experiments are conducted on a single NVIDIA RTX 4090 GPU using PyTorch 2.0. Unless otherwise stated, we
use a learning rate of 2×10 −5, batch size 32, and train for 10 epochs. The embedding dimension is fixed to d= 128.
In contrastive training, each positive pair is trained against K= 5 sampled negative skills. We set the random seed to
42 for initialization and data splitting.
We compare three models:
• Model A: Standard BERT (Single Label) – A baseline using BERT for single-skill sentence embedding with
contrastive loss.
• Model B: BERT + BiLSTM + Attention (Single Label) – An optimized single-label model incorporating
BiLSTM for sequence modeling and attention for contextual weighting.
6

• Model C: BERT + BiLSTM + Attention (Multi Label) – Extends Model B to multi-label training, handling
one sentence mapped to multiple skills.
Across all experiments involving real job ads, evaluation is performed at theposting level. We segment each posting
into sentences, apply the binary filter with threshold τ, retrieve candidate skills for each retained sentence, and then
aggregate to a posting-level prediction by set union in Eq. 10. Retrieval uses a two-stage decision rule consistent with
our Methodology: we first retrieve Top-Kr candidates by cosine similarity, and then keep only those with similarity
above γ. Unless stated otherwise, Kr = 50is used as the retrieval budget, while γ is tuned on a development split (see
Experiment 5).
5.2 Experiment 1: Synthetic Data Quality and Diversity
We first assess whether synthetic sentences resemble real job-ad requirement language in both fluency and diversity.
We compare three synthetic variants: single-skill sentences (Dsingle), hierarchically constrained multi-skill sentences
(Dmulti), and randomly paired multi-skill sentences (Random-Dmulti).
For fluency, we compute perplexity on 1,000 randomly sampled synthetic sentences using a Chinese GPT-2 language
model (uer/gpt2-chinese-cluecorpussmall); lower perplexity indicates more natural phrasing. Since fluency
alone does not guarantee usefulness as supervision, we also evaluate transferability: for each variant, we train the same
RoBERTa sentence classifier (skill vs. non-skill) using that variant as the positive class and a common negative set,
and then test on a manually labeled set of 1,000 real Chinese sentences drawn from job ads. We report perplexity and
real-data F1, where higher F1 suggests the synthetic variant better matches real requirement semantics. To ensure that
improvements are not driven by duplicated phrasing, we additionally report the fraction of near-duplicate samples
removed by our de-duplication procedure.
5.3 Experiment 2: Binary Classification for Filtering
This experiment evaluates the sentence-level filter used to remove non-requirement content (e.g., company introductions,
benefits, compliance clauses) prior to skill retrieval. We fine-tune RoBERTa classifiers under three training mixes:
positives from Dsingle, positives from Dmulti, and the combined positives (Dsingle ∪D multi), each paired with the same
negative set Dnone (100,000 synthetic non-skill sentences). We evaluate on 1,000 manually annotated real Chinese
sentences segmented by punctuation.
Threshold selection is aligned with the overall pipeline objective: we choose τ on a held-out development set to
maximize precision subject to a minimum recall constraint. This reflects the practical need to reduce downstream false
positive skills while retaining most true requirement sentences. We compare against two baselines: a keyword-matching
heuristic and a zero-shot NLI classifier (Chinese). Results are reported using Accuracy, Precision, Recall, F1, and
AUPRC. Finally, we include an ablation that removesDnone during training to quantify the role of explicit non-skill
supervision in controlling false positives.
5.4 Experiment 3: Retrieval Performance on Synthetic Hold-out
We next evaluate whether the bi-encoder learns a meaningful alignment between synthetic job-ad sentences and ESCO
skill definitions. We use a 20% hold-out split of the synthetic data and evaluate Models A–C as pure retrieval systems.
For each query sentence, we rank all ESCO skills by cosine similarity and report standard ranking metrics including
MRR, Recall@5, and mAP. This experiment functions as a controlled diagnostic: it tests whether architectural choices
(BiLSTM+attention) and supervision choices (single-skill vs. multi-skill) improve semantic matching under known
ground truth.
To provide a non-neural retrieval reference point, we also report TF-IDF matching between sentences and ESCO
definitions, using cosine similarity in TF-IDF space to retrieve Top-Kr candidates.
5.5 Experiment 4: Component Ablation Study
To isolate which design choices drive performance, we ablate both architecture and objective components. Starting from
Model C, we (i) remove the BiLSTM layer, (ii) replace attention pooling with mean pooling or [CLS] pooling, and (iii)
vary contrastive loss hyperparameters by sweeping the margin λ∈ {0.3,0.5,0.7} and the number of negative skills
K∈ {1,5,10}. We evaluate each variant using MRR and Recall@5 on the synthetic hold-out set, and we additionally
report training throughput (samples/second) to quantify computational overhead.
7

5.6 Experiment 5: End-to-End Transfer to Real Job Ads
This is the primary evaluation of real-world utility. We test the full pipeline—sentence segmentation, filtering, retrieval
with thresholding, and posting-level union aggregation—on 500 randomly sampled real Chinese job advertisements.
Each posting is manually annotated with ESCO Level-4 skill IDs based on the translated ESCO ontology. To improve
reliability, we employ a two-stage annotation protocol: annotators follow a written guideline to map requirement
statements to ESCO IDs, each sample is independently labeled, and disagreements are resolved by adjudication; we
report inter-annotator agreement in the appendix.
We tune the retrieval similarity threshold γ on a development subset of the annotated postings. Concretely, for
each candidate γ, we run the full pipeline and select the value that maximizes posting-level F1@5 (equivalently, a
precision–recall trade-off that best matches the downstream objective). Final results are reported on a disjoint test
subset.
We compare against lexical retrieval baselines that match job text to ESCO definitions: TF-IDF cosine similarity
(primary baseline) and BM25 (where applicable). We report posting-level Precision@K, Recall@K, and F1@K for
K∈ {1,3,5}.
5.7 Experiment 6: Scalability and Robustness
Finally, we examine robustness to noisy real-world text and runtime scalability. For robustness, we inject character-level
perturbations into the real test set by applying random substitutions and deletions to 20% of characters in each posting,
reflecting common typos and low-quality text. We report the relative degradation in posting-level F1@K and in
sentence-level ranking metrics.
For scalability, we measure training convergence and retrieval latency as the synthetic training set size increases from
10k to 100k samples. Retrieval latency is reported as end-to-end time per posting (encoding + similarity search over
|S|= 13,896skills), measured under the same hardware and batching settings used elsewhere.
6 Results
This section evaluates the proposed zero-shot skill extraction framework in three steps. We first examine the quality
of the synthetic training data, then evaluate the skill-requiring sentence filter, and finally compare the XMLC models
(Models A, B, and C) on synthetic benchmarks and real-world job advertisements.
6.1 Quality of Synthetic Data
We hypothesize that hierarchically constrained generation produces synthetic sentences that are (i) linguistically fluent
and (ii) semantically discriminative for downstream supervision. We evaluate fluency using GPT-2 perplexity and assess
discriminability via a binary separability test (ROC curves).
Table 1 reports the perplexity statistics. TheMulti-Skill (Level-2)variant achieves the lowest perplexity, indicating that
ESCO Level-2 constraints improve linguistic consistency compared to unconstrained multi-skill pairing and single-skill
generation. In addition, Figure 1(b) shows that the Level-2 variant yields the strongest ROC curve in the separability
test, suggesting that taxonomy-guided generation produces more discriminative positives (i.e., easier to separate from
generic non-skill text) and reduces label noise.
Table 1: Intrinsic quality assessment of synthetic variants using GPT-2 perplexity (lower is better). Discriminability is
evaluated separately via ROC curves in Figure 1(b).
Synthetic Variant Perplexity (Mean±SD)
Single-Skill (Dsingle)18.5±3.5
Multi-Skill (Random)22.1±4.0
Multi-Skill (Level-2)15.2±2.5
6.2 Effectiveness of Skill-Requiring Sentence Filtering
A reliable pre-filter is essential because real job ads contain substantial non-skill content (e.g., company introductions
and benefits). Figure 2 reports the performance of our RoBERTa-based binary classifier. From the confusion matrix in
Figure 2(a), our model produces 58 false positives and 67 false negatives (out of 1,000), corresponding to an Accuracy
of 0.875, Precision of 0.882, Recall of 0.866, and F1 of 0.874 at the default decision threshold.
8

Figure 1: Evaluation of synthetic data quality. (a) GPT-2 perplexity distributions. (b) ROC curves from a separability
test between synthetic skill sentences and generic non-skill text; the Level-2 constrained variant dominates across
thresholds. (c) Word cloud illustrating broad topical coverage of the generated corpus.
Figure 2(b) further shows that our model maintains higher precision over a wide recall range relative to keyword
matching. Figure 2(c) summarizes the latency–accuracy trade-off: our model is slower than keyword rules but yields
materially higher accuracy, which is appropriate for offline/large-batch processing. Importantly, removing synthetic
negative samples (Dnone) increases spurious activations (higher false positives), indicating that explicit “no-skill”
supervision is necessary to calibrate the filter.
Table 2: Binary sentence filter performance on real-world Chinese job ads. ForOurs (Combined), Precision/Recall/F1
are computed from the confusion matrix in Figure 2(a).
Method Accuracy F1-Score Precision Recall
Keyword Matching 0.80 0.75 0.72 0.78
Zero-Shot NLI 0.84 0.80 0.79 0.81
Ablated (w/oD none) 0.85 0.83 0.82 0.84
Ours (Combined) 0.875 0.874 0.882 0.866
Figure 2: Binary sentence filtering. (a) Confusion matrix for our filter, showing balanced FP/FN counts. (b) Precision–
Recall curves comparing our filter to keyword matching across thresholds. (c) Inference latency vs. accuracy for
competing approaches.
6.3 XMLC Model Comparison (Synthetic Benchmark)
We next evaluate the downstream XMLC component, comparing Models A, B, and C on the synthetic hold-out
benchmark. Figure 3(a) shows that Model C converges to the best MRR, followed by Model B and Model A. Figure 3(b)
9

reports Recall@K, where Model C consistently attains higher recall across K, indicating more effective retrieval of
relevant skills when expanding the candidate set.
Finally, Figure 3(c) visualizes a t-SNE projection of the learned embeddings (Model C), colored by ESCO Level-2
categories. While overlaps remain (as expected given semantically adjacent skill groups), the projection suggests
meaningful category-level structure rather than degenerate separation.
Table 3: Comparison of XMLC models on the synthetic validation set. Reported metrics align with Figure 3: MRR
(final epoch) and Recall@K.
Model MRR Recall@5 Recall@10
Model A (Standard, Single) 0.48 0.33 0.47
Model B (Optimized, Single) 0.66 0.42 0.55
Model C (Optimized, Multi) 0.76 0.48 0.65
Figure 3: XMLC model evaluation. (a) MRR over training epochs. (b) Recall@K on the synthetic benchmark. (c)
t-SNE projection of Model C embeddings, colored by ESCO Level-2 categories.
6.4 Ablation Study
We conduct ablations to verify key design choices and characterize the sensitivity to contrastive-learning hyperparame-
ters. Table 4 and Figure 4(a) show that performance is sensitive to the margin: MRR improves as the margin increases
up to approximatelym= 0.5, after which overly aggressive separation degrades performance.
Figure 4(b) shows diminishing returns as the number of negatives increases. While larger negative sets can improve
MRR, training throughput declines substantially. In our setting, N= 8 provides a practical operating point: it is near
the MRR saturation region while avoiding the steepest efficiency loss atN= 10.
Figure 4(c) reports relative attention scores over tokens, indicating that the model assigns higher mass to skill-bearing
terms (e.g., programming languages and task keywords) rather than delimiters.
Table 4: Ablation analysis on Model B/C training choices. Throughput values correspond to training efficiency under
the same hardware and batch configuration.
Configuration MRR Throughput (samples/s)
No BiLSTM/Attention 0.55 –
Margin = 0.1 0.55 –
Margin = 0.5 0.65 –
Margin = 0.8 0.58 –
Num_Negatives = 1 0.55 250
Num_Negatives = 8 0.68 170
Num_Negatives = 10 0.68 150
Selected (Margin = 0.5, Neg = 8) 0.65 170
10

Figure 4: Ablation analysis. (a) MRR vs. contrastive margin. (b) Trade-off between training efficiency and MRR as the
number of negative samples increases. (c) Relative attention scores over tokens, highlighting emphasis on skill-bearing
terms.
6.5 End-to-End Zero-Shot Transfer (Real Data)
We evaluate end-to-end zero-shot transfer on manually annotated job advertisements. Figure 5(a) shows that Model
C dominates Models A and B in Precision–Recall space, indicating stronger zero-shot generalization from synthetic
supervision to real-world text. Qualitative case inspection (Figure 5(b)) suggests that the majority of predictions are
correct, while the remaining errors concentrate in a smaller fraction of challenging samples.
Error analysis in Figure 5(c) indicates that false negatives are the most frequent failure mode, followed by false positives.
“Misalignment” errors (cases where the model retrieves a closely related but not exactly matching skill label) are less
frequent but remain a substantive source of residual error, consistent with the inherent granularity and overlap of skill
taxonomies.
Table 5: End-to-end zero-shot performance on real-world job ads. We report AUPRC (Average Precision) and F1 at the
default threshold for comparability with Figure 5(a).
Model AUPRC F1
Model A 0.72 0.69
Model B 0.82 0.75
Model C 0.90 0.80
Figure 5: End-to-end transfer performance on real-world test data. (a) Precision–Recall curves for Models A/B/C. (b)
Correct vs. error ratio in qualitative case studies. (c) Error breakdown into false positives, false negatives, and taxonomy
misalignment.
11

6.6 Scalability and Robustness
Finally, we evaluate scalability and robustness for Model C. Figure 6(a) shows that MRR improves with synthetic
dataset size, with gains becoming smaller at larger scales (diminishing marginal returns). Figure 6(b) shows graceful
degradation under increasing noise, indicating that the model is not overly brittle to moderate text corruption. Figure 6(c)
demonstrates approximately linear scaling of training time with dataset size on a log–log scale, consistent with
expectations for minibatch training under fixed hyperparameters.
Figure 6: Scalability and robustness analysis. (a) MRR vs. synthetic training set size. (b) MRR under increasing noise
levels (0–20%). (c) Training time scaling with dataset size (log–log).
7 Conclusion
This paper targets the practical challenge of mapping unstructured job-ad text to a standardized skills ontology (ESCO)
in settings where manually annotated training data are scarce or unavailable. We propose a zero-shot XMLC framework
that couples LLM-based synthetic supervision with contrastive learning for retrieval-style skill prediction. A key design
choice ishierarchically constrainedgeneration: by sampling multi-skill sentences under ESCO Level-2 constraints, we
obtain synthetic training signals that are more coherent and more discriminative than unconstrained alternatives.
Across a suite of intrinsic and extrinsic evaluations, the results support three main conclusions. First, Level-2 constrained
generation produces synthetic text with improved fluency (lower perplexity) and stronger separability in downstream
diagnostics, suggesting reduced noise in the resulting supervision. Second, the RoBERTa-based sentence filter provides
an effective front-end for excluding non-skill content, achieving balanced false positive/false negative behavior and a
consistently stronger precision–recall profile than keyword matching, at the cost of higher inference latency. Third, in the
XMLC stage, the optimized multi-label model (Model C) converges to the best ranking quality and recall-at-K on the
synthetic benchmark, and it also exhibits superior end-to-end precision–recall behavior on real job ads. The remaining
errors are dominated by false negatives and taxonomy misalignment cases, highlighting the inherent ambiguity of
fine-grained skill definitions and the long-tail nature of job-ad phrasing.
Overall, the proposed framework offers a scalable pathway for labor market intelligence: it enables automated projection
of large volumes of job postings into standardized skill representations without requiring labeled training data. Future
work will extend the pipeline in three directions: (i) multilingual transfer and cross-lingual alignment for non-English
job markets, (ii) hierarchy-aware learning objectives (e.g., graph-based regularization or taxonomy-consistent decoding)
to better exploit ESCO structure, and (iii) generalization to additional taxonomies (e.g., O*NET) and domain-specific
skill ontologies.
References
Arthur Turrell, Bradley J. Speigner, Jyldyz Djumalieva, David Copple, and James Thurgood. Transforming naturally
occurring text data into economic statistics: The case of online job vacancy postings. Working Paper 25837, National
Bureau of Economic Research, May 2019. URLhttps://www.nber.org/papers/w25837.
European Commission. European skills/competences, qualifications and occu-
pations (esco). Website. URL https://employment-social-affairs.ec.
12

europa.eu/policies-and-activities/skills-and-qualifications/skills-jobs/
european-skillscompetences-qualifications-and-occupations-esco_en.
Rohit Babbar and Bernhard Schölkopf. DiSMEC: Distributed sparse machines for extreme multi-label classification.
InProceedings of the Tenth ACM International Conference on Web Search and Data Mining (WSDM ’17), pages
721–729, Cambridge, United Kingdom, 2017. Association for Computing Machinery. ISBN 9781450346757.
doi:10.1145/3018661.3018741. URLhttps://dl.acm.org/doi/10.1145/3018661.3018741.
Ian En-Hsu Yen, Xiaojin Zhu, Pradeep Ravikumar, and Inderjit S. Dhillon. PD-Sparse: A primal and dual sparse
approach to extreme multiclass and multilabel classification. InProceedings of the 33rd International Conference
on Machine Learning (ICML 2016), volume 48 ofProceedings of Machine Learning Research, pages 3069–3077.
PMLR, 2016. doi:10.5555/3045390.3045713. URLhttps://proceedings.mlr.press/v48/yen16.html.
Yashoteja Prabhu, Anil Kag, Shrutendra Harsola, Rahul Agrawal, and Manik Varma. Parabel: Partitioned label trees for
extreme classification with application to dynamic search advertising. InProceedings of the 2018 World Wide Web
Conference (WWW ’18), pages 993–1002, Lyon, France, 2018. International World Wide Web Conferences Steering
Committee. doi:10.1145/3178876.3185998. URLhttps://dl.acm.org/doi/10.1145/3178876.3185998.
Ronghui You, Zihan Zhang, Ziye Wang, Suyang Dai, Hiroshi Mamitsuka, and Shanfeng Zhu. AttentionXML:
Label tree-based attention-aware deep model for high-performance extreme multi-label text classification. In
H. Wallach, H. Larochelle, A. Beygelzimer, F. d’Alché Buc, E. Fox, and R. Garnett, editors,Advances in Neural
Information Processing Systems 32 (NeurIPS 2019), pages 5812–5822. Curran Associates, Inc., 2019. ISBN
9781713807933. doi:10.5555/3454287.3454810. URL https://papers.nips.cc/paper_files/paper/2019/
hash/9e6a921fbc428b5638b3986e365d4f21-Abstract.html.
Ting Jiang, Deqing Wang, Leilei Sun, Huayi Yang, Zhengyang Zhao, and Fuzhen Zhuang. LightXML: Transformer
with dynamic negative sampling for high-performance extreme multi-label text classification.arXiv preprint
arXiv:2101.03305, 2021. doi:10.48550/arXiv.2101.03305. URLhttps://arxiv.org/abs/2101.03305.
Mike Zhang, Kristian Nørgaard Jensen, Rob van der Goot, and Barbara Plank. Skill extraction from job postings
using weak supervision.arXiv preprint arXiv:2209.08071, 2022. doi:10.48550/arXiv.2209.08071. URL https:
//arxiv.org/abs/2209.08071. Accepted in RecSys in HR’22 (workshop), per arXiv record.
Van-Duyet Le, Minh Quan V o, and Quang An Dang. Skill2vec: Machine learning approach for determining the
relevant skills from job description.arXiv preprint arXiv:1707.09751, 2019. doi:10.48550/arXiv.1707.09751. URL
https://arxiv.org/abs/1707.09751.
Akshay Bhola, Kishaloy Halder, Animesh Prasad, and Min-Yen Kan. Retrieving skills from job descriptions: A
language model based extreme multi-label classification framework. InProceedings of the 28th International
Conference on Computational Linguistics (COLING 2020), pages 5832–5842, Barcelona, Spain (Online), December
2020. International Committee on Computational Linguistics. doi:10.18653/v1/2020.coling-main.513. URL https:
//aclanthology.org/2020.coling-main.513/.
Jens-Joris Decorte, Jeroen Van Hautte, Thomas Demeester, and Chris Develder. Jobbert: Understanding job titles
through skills.arXiv preprint arXiv:2109.09605, 2021. doi:10.48550/arXiv.2109.09605. URL https://arxiv.
org/abs/2109.09605. Accepted to FEAST (workshop) at ECML-PKDD 2021, per arXiv record.
Bosheng Ding, Chengwei Qin, Linlin Liu, Yew Ken Chia, Shafiq Joty, Boyang Li, and Lidong Bing. Is GPT-3 a
good data annotator?arXiv preprint arXiv:2212.10450, 2023. doi:10.48550/arXiv.2212.10450. URL https:
//arxiv.org/abs/2212.10450. Accepted by ACL 2023, per arXiv record.
Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu, and Michael Zeng. Want to reduce labeling cost? GPT-3 can
help.arXiv preprint arXiv:2108.13487, 2021. doi:10.48550/arXiv.2108.13487. URL https://arxiv.org/abs/
2108.13487. Findings of EMNLP 2021, per arXiv record.
Peter West, Chandra Bhagavatula, Jack Hessel, Jena Hwang, Liwei Jiang, Ronan Le Bras, Ximing Lu, Sean Welleck,
and Yejin Choi. Symbolic knowledge distillation: from general language models to commonsense models. In
Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies, pages 4602–4625, Seattle, United States, July 2022. Association for Computational
Linguistics. doi:10.18653/v1/2022.naacl-main.341. URL https://aclanthology.org/2022.naacl-main.
341/.
Jiacheng Ye, Jiahui Gao, Qintong Li, Hang Xu, Jiangtao Feng, Zhiyong Wu, Tao Yu, and Lingpeng Kong.
Zerogen: Efficient zero-shot learning via dataset generation.arXiv preprint arXiv:2202.07922, 2022.
doi:10.48550/arXiv.2202.07922. URL https://arxiv.org/abs/2202.07922. Accepted by EMNLP 2022 (Main
Conference), per arXiv record.
13

Tianyu Gao, Xingcheng Yao, and Danqi Chen. SimCSE: Simple contrastive learning of sentence embeddings. In
Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP 2021),
pages 6894–6910, Online and Punta Cana, Dominican Republic, November 2021. Association for Computational
Linguistics. doi:10.18653/v1/2021.emnlp-main.552. URL https://aclanthology.org/2021.emnlp-main.
552/.
Nils Reimers and Iryna Gurevych. Sentence-BERT: Sentence embeddings using siamese BERT-networks.arXiv
preprint arXiv:1908.10084, 2019. doi:10.48550/arXiv.1908.10084. URL https://arxiv.org/abs/1908.10084.
Published at EMNLP 2019, per arXiv record.
Joshua Robinson, Ching-Yao Chuang, Suvrit Sra, and Stefanie Jegelka. Contrastive learning with hard negative samples.
arXiv preprint arXiv:2010.04592, 2021. doi:10.48550/arXiv.2010.04592. URL https://arxiv.org/abs/2010.
04592. Published as a conference paper at ICLR 2021, per arXiv record.
Alexis Conneau, Douwe Kiela, Holger Schwenk, Loïc Barrault, and Antoine Bordes. Supervised learning of universal
sentence representations from natural language inference data. InProceedings of the 2017 Conference on Empirical
Methods in Natural Language Processing (EMNLP 2017), pages 670–680, Copenhagen, Denmark, September
2017. Association for Computational Linguistics. doi:10.18653/v1/D17-1070. URL https://aclanthology.
org/D17-1070/.
Zichao Yang, Diyi Yang, Chris Dyer, Xiaodong He, Alex Smola, and Eduard Hovy. Hierarchical attention networks for
document classification. InProceedings of the 2016 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, pages 1480–1489, San Diego, California, June
2016. Association for Computational Linguistics. doi:10.18653/v1/N16-1174. URL https://aclanthology.
org/N16-1174/.
A Synthetic Data Generation Details
To augment our dataset with diverse and realistic sentence-skill pairings, we employed a large language model (LLM)
for synthetic data generation. We utilized the DeepSeek V3.1 model (accessed via the ‘deepseek-chat‘ API endpoint),
leveraging its strong multilingual capabilities to generate contextually relevant Chinese job advertisement sentences
based on ESCO skill descriptions.
A.1 LLM Configuration
Based on the generation scripts, the model was configured with the following hyperparameters to ensure output diversity
while preventing repetition:
•Model: DeepSeek V3.1 Chat
•Temperature: 0.9
•Presence Penalty: 0.8
• Prompting Strategy: Few-Shot Learning (We provided specific examples of skill-to-sentence mapping within
the conversation history to guide the model’s style).
A.2 Prompt Templates
We utilized a role-playing strategy where the system was instructed to act as an "experienced recruitment ad copywriter."
Below are the specific templates used for single-label, multi-label, and non-skill sentence generation.
A.2.1 System Instruction
All generation tasks shared the following system-level instruction:
System:"You are an experienced recruitment ad copywriter expert, good at generating recruitment ad
sentences based on skills. Please respond by generating sentences used in hypothetical recruitment
ads based on user requirements, representing the demand for specific skills. Ensure diversity in the
generated sentences and do not repeat sentences or structures."
14

A.2.2 Single-Label Generation
For the single-label dataset ( esco_sentence_one.csv), we provided the model with the ESCO skill label and
definition. The prompt included few-shot examples (e.g., for "Project Management" and "Java") to demonstrate the
desired output format.
User:
Number of sentences: [N]
Skill: [translated_skill]
Definition: [description_translation]
A.2.3 Hierarchical Multi-Label Generation
For the multi-label dataset (esco_sentence_two.csv), the prompt was designed to integrate two skills into a single
context. As detailed in the methodology, these pairs were pre-selected to belong to the same ESCO Level-2 category.
User:
Number of sentences: [N]
Skill 1: [skill_1]
Definition 1: [description_1]
Skill 2: [skill_2]
Definition 2: [description_2]
A.2.4 Negative (No-Skill) Sample Generation
To train the binary filter, we also generated sentences typical of job ads that do not contain skill requirements (e.g.,
salary, benefits, company culture).
User:
Number of sentences: [N]
Do not include any requirements regarding labor skills.
A.3 Data Post-Processing
The raw outputs were parsed to remove bullet points (e.g., "- ") and filtered to remove duplicates. We generated
approximately 100 sentences per prompt for the single-label task and smaller batches for the multi-label task, resulting
in the final datasets described in Section 4.
15
